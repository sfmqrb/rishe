# Verification process log — verify-page-65


## [2026-09-04T23:05:07.256Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 65 only (note the recently added requirements: `derivation_fa`/`note_fa` Persian explanations, and `error_in`/`book_prints`/`correct_form` on any transcription flag). Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-65.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-65.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-65.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 65` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T23:05:12.775Z] AGENT

I'll start by reading the instructions file.


## [2026-09-04T23:05:14.918Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T23:05:14.938Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which
5	this repository (`/home/sfmqrb/git/rishe`) turned into JSON
6	(`data/extracted/batch/page-<pdf>.json`). Compact text renderings of the charts
7	are in `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-<pdf>.txt`.
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
38	   - `transcription_suspect` — the JSON data looks like a transcription error from the scan
39	     (a misread letter, an impossible form, a wrong Persian script); say what you think the
40	     book actually printed and why.
41	4. Record sources as URLs (Wiktionary page, Etymonline page, AHD appendix entry, archive.org
42	   page of Klein/Horn/Bartholomae, etc.). Also note when Nourai's own cited reference
43	   (KLN, POK, AHD, BQT, MON, HRN, HUB…) is itself the modern standard for that claim.
44	
45	
46	## Checking Nourai's OWN cited references (required)
47	
48	Every node carries `refs=` — Nourai's citations, e.g. `KLN:164; FVQ:75` (abbreviation:page;
49	`MON5:528` = MON vol. 5 p. 528). The author claims each arrow is supported by those pages.
50	You must check them:
51	
52	- The bibliography key (abbreviation → book) is in
53	  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt`.
54	- Where each reference can be read online is in
55	  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json`
56	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`).
57	- If `local_file` is set, the OCR text of that book is on disk: grep it for the headword
58	  (try several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and,
59	  if `page_offset` is given, locate the cited page (pages are separated by form-feeds; use
60	  `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one page). Read the entry and judge whether
61	  it actually says what Nourai's arrow says.
62	- **Scanned references without OCR text** (Borhan-e Qate' vols 3-5 = BQT pages ~1208-2475,
63	  Farahvashi's Iranvij = IRN, and any entry whose table record has a `scans` list): do NOT
64	  OCR whole books. Fetch only the cited page:
65	  `python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:918 --image`
66	  It renders that one page to PNG, OCRs it (Persian OCR is rough), caches both under
67	  `data/verification/sources/refs/ocr/`, and prints the text plus the PNG path. If the OCR
68	  is unreadable, Read the PNG (you can read Persian print directly), and then SAVE what you
69	  read: write the entry/entries you used (headword, Mo'in's etymological footnote, and any
70	  surrounding lines you relied on) verbatim to the companion file
71	  `data/verification/sources/refs/ocr/<ABBR>/<page>.vision.txt` (the tool prints the exact
72	  paths). The tool prefers that file next time, so nobody pays for reading the image again.
73	  If the printed page number on the image is off, re-run with `--pdf-page <n>` adjusted, and
74	  note the correct pdf page in your ref_check note.
75	- If `kind` is `website`, use the `lookup_hint` URL pattern with WebFetch.
76	- Do this for at least ONE cited reference per node (the most authoritative available:
77	  POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM/PLA for Semitic,
78	  BQT/MON for Persian). If none of a node's references is accessible, say so.
79	
80	Add to every node a `ref_check` array:
81	
82	```json
83	"ref_check": [
84	  {"ref": "KLN:164", "status": "supports", "note": "Klein s.v. 'cherub': Heb. kerūbh, prob. rel. to Akkad. karābu 'to bless', metathesis of b-r-k — exactly Nourai's claim."},
85	  {"ref": "FVQ:75", "status": "not_checked", "note": "no online copy"}
86	]
87	```
88	
89	`status` ∈ `supports` (the page says what the arrow says) · `partial` (the reference has the
90	word but a different/looser derivation) · `contradicts` (the reference says something else)
91	· `not_found` (checked the text, could not find the entry/page) · `not_checked` (reference
92	not accessible online). Quote the key phrase of the reference in `note` when you can.
93	
94	Also add to each entry a root-level `ref_check` for the root's own refs (e.g. `POK:244`).
95	
96	
97	
98	## Transcription flags: say WHERE the error is (required)
99	
100	For every node you mark `transcription_suspect`, look at the printed page itself — render it
101	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg<pdf page>`
102	(or open `site/pages/<pdf page>.jpg`) and Read the image — and add to the node:
103	
104	```json
105	"error_in": "book",            // "book" = the printed book has the odd form (author's misprint); the extraction is faithful
106	                               // "extraction" = the book prints the correct form; the JSON misread it
107	                               // "unknown" = could not decide from the image
108	"book_prints": "borrāgō",      // what the printed page actually shows
109	"correct_form": "borrāgō"      // the form that should stand (per the sources)
110	```
111	
112	Usually the extraction is faithful and the problem is in the book itself; say so plainly in
113	`derivation` too ("the book prints X; this is Nourai's misprint for Y"). Only when the JSON
114	differs from the page is it an extraction error (report those separately in your summary — the
115	owner fixes the data).
116	
117	
118	## Persian explanation (required): `derivation_fa` on every node, `note_fa` on every root
119	
120	Write the derivation a second time IN PERSIAN, for a Persian reader — not a translation of the
121	English sentence. Think about how a Persian etymologist (حسن‌دوست، ابوالقاسمی، معین در حواشی
122	برهان قاطع) would explain it to an educated Persian reader:
123	
124	- Use the established Persian terminology: هندواروپایی آغازین، ایرانی باستان، اوستایی، پارسی
125	  باستان، فارسی میانه (پهلوی)، پارتی، سغدی، فارسی نو/دری؛ وام‌واژه، وام‌گیری، دگرگونی آوایی،
126	  قلب (metathesis)، ابدال، همگونی، پیشوند، پسوند، ریشه، ستاک، تحول معنایی، معرّب، ریشه‌شناسی
127	  عامیانه (folk etymology)، هم‌ریشه (cognate)، دوگانه (doublet).
128	- Give the Persian word first in Persian script, then the older forms in Latin transliteration
129	  as Persian philology does (e.g. «آب» از فارسی میانهٔ āb / āp، از ایرانی باستان *āp-، هم‌ریشه با
130	  سنسکریت āp-). Persian-script forms for Arabic words; Greek/Latin words in Latin letters.
131	- Explain the sound changes in the way a Persian reader expects (e.g. «پ ایرانی باستان در میان
132	  دو واکه در فارسی میانه به ب نرم شده»؛ «ای کشیدهٔ فارسی میانه در فارسی نو به ی بدل شده»).
133	- Say clearly, in Persian, what the verdict means for the reader: ادعای نورایی درست است / با
134	  احتیاط پذیرفتنی است / پژوهش امروزی آن را رد می‌کند و به جای آن … می‌گوید / خطای چاپی کتاب.
135	- Keep it 2–5 sentences, formal but readable (نه ترجمهٔ لفظ‌به‌لفظ، نه ماشینی). Numbers in
136	  Persian digits are fine. Mention the key sources by their Persian-usable names (پوکورنی،
137	  بارتولومه، هرن، هوبشمان، مکنزی، نیبرگ، چونگ، معین، برهان قاطع، ویکی‌واژه).
138	
139	Field names: `derivation_fa` (node) and `note_fa` (root entry). Both required.
140	
141	## Process documentation (required)
142	
143	The owner wants to be able to audit every step later. Therefore:
144	
145	- **Every web page you rely on must be archived**: after you read a page (WebFetch or
146	  curl), run
147	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
148	  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
149	  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
150	  one Bash command to save time.)
151	- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` include
152	  the exact phrase(s) you found (with the grep pattern or page you used, e.g.
153	  "KLN.txt p.164 (ff-page 178): 'cherub … prob. rel. to Akkad. karābu'"), so the finding can
154	  be re-run.
155	- Your full transcript (every tool call and result) is exported automatically by the
156	  coordinator; nothing else needed for that.
157	
158	
159	## Use EVERY relevant book on disk (required)
160	
161	Checking only the reference Nourai cites is not enough. For every node, also consult the
162	other books in the local library that could speak to that claim, and record what each says.
163	The list of which books cover which kind of node, with file paths, is
164	`/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md`
165	(also `data/verification/sources/SOURCE_MATRIX.md`). Minimum per node:
166	
167	- an Indo-European node or root box: Pokorny (POK) AND Walde-Pokorny (WLD) AND Watkins/AHD,
168	  plus Mann (IEC) or Buck (SYN) when the word is a common noun;
169	- an Avestan / Old Persian node: Bartholomae (BRT) or Kent (KNT);
170	- a Pahlavi / Middle Persian node: MacKenzie (PHD) and Nyberg (NYB);
171	- a New Persian node: Horn (HRN), Hübschmann (HUB), Cheung (CHEUNG, for verbs), Borhan-e
172	  Qate' with Mo'in's footnotes (BQT), Mo'in (MON), and Aryanpur (ARY, once its text exists);
173	- a Sogdian node: Gharib (SOD); a Khotanese one: Bailey (ISS_alt_DKS);
174	- an Arabic node or a Persian/Arabic loan in either direction: Klein (KLN), Jeffery (FVQ),
175	  Addi Shir (AFM), Asbaghi (PLA), Fraenkel (AFA), Lokotsch (LKT); for French/Spanish
176	  Arabisms Pihan (PHN), Devic (DEV), Lammens (LAM), Dozy (DOZ);
177	- an English / Romance node: Klein (KLN), Skeat (SKT), Funk & Wagnalls (FSD), Webster (WEB);
178	  Anglo-Indian words: Hobson-Jobson (HJB), Whitworth (AID);
179	- a Turkic node: Vámbéry (TTS), Lokotsch (LKT).
180	
181	Grep each file for the headword (several spellings; Latin transliteration for the Western
182	books, Persian script for BQT/MON/ARY, Pahlavi transliteration for PHD/NYB). A grep that
183	finds nothing is also a result ("silent"). Record everything in a `consulted` array on the
184	node (separate from `ref_check`, which is only for the references Nourai himself cites):
185	
186	```json
187	"consulted": [
188	  {"src": "HRN", "where": "no. 3, p. 1", "stance": "contradicts", "note": "Horn separates āb 'Glanz' from āb 'water' and derives āftāb from the former"},
189	  {"src": "PHD", "where": "p. 5 s.v. ābād", "stance": "supports", "note": "'ābād [ʾpʾt] populous, thriving' — no water element"},
190	  {"src": "WLD", "where": "Bd. I p. 46", "stance": "silent", "note": "root ap- listed, no Persian compound"}
191	]
192	```
193	
194	`stance` ∈ supports / contradicts / partial / silent. Quote the key phrase. Books consulted
195	via the web (vajehyab for Mo'in, AHD online) go here too, with the URL archived via
196	fetch_source.py and listed in `sources`. Every node must have at least two `consulted`
197	entries from different books whenever the matrix lists two or more books for its language.
198	
199	## Sources to use (in roughly this order)
200	
201	- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
202	  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
203	  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
204	  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
205	  Use URL-encoded Persian/Arabic script for those pages.
206	- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
207	- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
208	  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
209	  appendix; the online appendix is the updated edition of the same list.
210	- **Pokorny** — via indo-european.info, starlingdb.org, or Wiktionary's Pokorny citation;
211	  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
212	- **Klein's Comprehensive Etymological Dictionary** (KLN) and **Horn's Grundriss der
213	  neupersischen Etymologie** (HRN), **Hübschmann's Persische Studien** (HUB),
214	  **MacKenzie's Concise Pahlavi Dictionary** (PHD), **Bartholomae AiW** (BRT) are on archive.org
215	  if needed for a hard case.
216	- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
217	- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
218	- Use WebSearch when you don't know the right page; use WebFetch to read a page.
219	
220	Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
221	If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
222	source covering the chain is enough; spend your effort on the Iranian and Semitic links,
223	which are where errors are likelier.
224	
225	## Output — write ONE file per page
226	
227	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
228	
229	```json
230	{
231	  "pdf_page": 126,
232	  "book_page": 96,
233	  "verified_by": "claude-fable-5-1",
234	  "verified_on": "2026-09-04",
235	  "entries": [
236	    {
237	      "entry": 0,
238	      "root": "Dheigh, Dhigha",
239	      "verdict": "confirmed",
240	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
241	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
242	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
243	      "nodes": [
244	        {
245	          "id": 6,
246	          "lang": "Avestan",
247	          "words": "pairi-daeza",
248	          "verdict": "confirmed",
249	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' (PIE *dʰeyǵʰ-, o-grade *dʰoyǵʰ-o- > Iranian *daiza-). Attested in the Vidēvdād (pairi-daēzaiiąn) …",
250	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza", "https://www.etymonline.com/word/paradise"]
251	        },
252	        {
253	          "id": 9,
254	          "lang": "Greek",
255	          "words": "paradeisos",
256	          "verdict": "confirmed",
257	          "derivation": "Borrowed from Old Iranian *paridaiza- (Median/Old Persian form with -d-, cf. Elamite par-te-taš, Akkadian pardēsu) in the 5th c. BCE; first in Xenophon (Anabasis 1.2.7) for the Persian kings' walled hunting parks. Greek -ei- renders Iranian /ai/ ~ /ē/; -os is the Greek nominative ending. The Septuagint (3rd c. BCE) used it for the Garden of Eden, whence the 'heaven' sense.",
258	          "sources": ["https://en.wiktionary.org/wiki/παράδεισος"]
259	        }
260	      ]
261	    }
262	  ]
263	}
264	```
265	
266	Rules:
267	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
268	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
269	- `words` = the transliterations of the node joined by "; " (copy from the chart).
270	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
271	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
272	- Keep `note` on the entry for root-level comments and for anything cross-cutting
273	  (e.g. "Nourai's whole Semitic branch here is rejected by Klein …").
274	- If a node lists several words, cover each word; if they differ in verdict, use the worst
275	  verdict for the node and explain per word in `derivation`.
276	- Where the chart's own NOTE already records a dispute (e.g. "POK:694 derives Latin mattus
277	  from root Mad"), evaluate it: say which side modern scholarship takes.
278	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted` (array) AND `derivation_fa` (string); every entry has `note_fa`.
279	- Valid JSON only. Test it with `python3 -m json.tool` before finishing.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason).
282	  Do not paste the JSON back into your reply.
283	
```


## [2026-09-04T23:05:15.275Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-65.txt"
}
```


### [2026-09-04T23:05:15.291Z] TOOL RESULT

```
1	=== PDF page 65 (book page 35) ===
2	--- entry 0 ---
3	ROOT [Greek] Arxein, Arkhein : to lead, begin  (refs KLN:100; AHD:1506)
4	#1 (parent #0) [Greek] refs=KLN:100; AHD:69 | arx, arxt, arkh, arkht : leader, master ; arx-tekton : master builder, architect ☞Tex ; arxeion : government, public office, government records
5	  #2 (parent #1) [Latin] refs=AHD | architectus ; archivum
6	    #3 (parent #2) [French] refs=AHD | architecte ; archive
7	      #4 (parent #3) [Persian] refs=AMD:25; MON:43 | âršîtekt «آرشیتکت» : "master builder" ; âršîv «آرشیو» : archive
8	      #5 (parent #3) [English] refs=AHD | arch- : master ; archbishop, architect, archive
9	#6 (parent #0) [Greek] refs=AHD:67 | arxaios, archaios : ancient
10	  #7 (parent #6) [Latin] refs=None | 
11	    #8 (parent #7) [English] refs=AHD | archaeo-, archaeology, archaic
12	--- entry 1 ---
13	ROOT Aryo -> redirect to Al 1
14	--- entry 2 ---
15	ROOT [Indo-European] As : to burn  (refs POK:68)
16	#1 (parent #0) [Latin] refs=KLN:102; FSD:1133 | ardĕre : to be on fire ; arĕre : to become dry (land) ; ara : an area
17	  #2 (parent #1) [French] refs=AHD:69 | are : area ; hect-are : unit of area (2.47 acres) ☞Dekm
18	    #3 (parent #2) [Persian] refs=MON:39, 5159 | âr 1 «آر» : unit of area ; hectâr «هکتار» : unit of area
19	    #4 (parent #2) [English] refs=FSD:1133 | hectare
20	#5 (parent #0) [English] refs=None | area ; arson
21	#6 (parent #0) [Germanic] refs=AHD | askôn : ashes
22	  #7 (parent #6) [English] refs=None | ash
23	--- entry 3 ---
24	ROOT A-sĕma -> redirect to Sĕma
25	--- entry 4 ---
26	ROOT Asfar -> redirect to S.f.r
27	
```


## [2026-09-04T23:05:18.933Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-65.json",
 "description": "Read page 65 source JSON"
}
```


### [2026-09-04T23:05:19.030Z] TOOL RESULT

```
{
  "pdf_page": 65,
  "book_page": 35,
  "entries": [
    {
      "root": {
        "name": "Arxein, Arkhein",
        "lang": "Greek",
        "refs": "KLN:100; AHD:1506",
        "gloss": "to lead, begin"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:100; AHD:69",
          "words": [
            {"translit": "arx, arxt, arkh, arkht", "gloss": "leader, master", "script": null},
            {"translit": "arx-tekton", "gloss": "master builder, architect", "script": null, "see": ["Tex"]},
            {"translit": "arxeion", "gloss": "government, public office, government records", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "architectus", "gloss": null, "script": null},
            {"translit": "archivum", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "architecte", "gloss": null, "script": null},
            {"translit": "archive", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "AMD:25; MON:43",
          "words": [
            {"translit": "âršîtekt", "gloss": "\"master builder\"", "script": "آرشیتکت"},
            {"translit": "âršîv", "gloss": "archive", "script": "آرشیو"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "arch-", "gloss": "master", "script": null},
            {"translit": "archbishop, architect, archive", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:67",
          "words": [
            {"translit": "arxaios, archaios", "gloss": "ancient", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "archaeo-, archaeology, archaic", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Aryo", "redirect": "Al 1"},
      "nodes": []
    },
    {
      "root": {
        "name": "As",
        "lang": "Indo-European",
        "refs": "POK:68",
        "gloss": "to burn"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:102; FSD:1133",
          "words": [
            {"translit": "ardĕre", "gloss": "to be on fire", "script": null},
            {"translit": "arĕre", "gloss": "to become dry (land)", "script": null},
            {"translit": "ara", "gloss": "an area", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "French",
          "refs": "AHD:69",
          "words": [
            {"translit": "are", "gloss": "area", "script": null},
            {"translit": "hect-are", "gloss": "unit of area (2.47 acres)", "script": null, "see": ["Dekm"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:39, 5159",
          "words": [
            {"translit": "âr 1", "gloss": "unit of area", "script": "آر"},
            {"translit": "hectâr", "gloss": "unit of area", "script": "هکتار"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "English",
          "refs": "FSD:1133",
          "words": [
            {"translit": "hectare", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "area", "gloss": null, "script": null},
            {"translit": "arson", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "askôn", "gloss": "ashes", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "ash", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "A-sĕma", "redirect": "Sĕma"},
      "nodes": []
    },
    {
      "root": {"name": "Asfar", "redirect": "S.f.r"},
      "nodes": []
    }
  ]
}
```


## [2026-09-04T23:05:20.841Z] TOOL CALL #4: Bash

```json
{
 "command": "cat \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md\"",
 "description": "Read source matrix"
}
```


### [2026-09-04T23:05:20.920Z] TOOL RESULT

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


## [2026-09-04T23:05:41.763Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['KLN','AHD','POK','FSD','MON','AMD','BQT','WLD','IEC','SYN','SKT','LEW','LAT','WEB','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-04T23:05:43.421Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && ls tools/ && echo ---- && grep -n -i -E '^(AMD|AHD|KLN|POK|FSD|MON|BQT)\\b' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -30",
 "description": "List verification dir and tools"
}
```


### [2026-09-04T23:05:43.618Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
AMD {"title": "Hasan Amid, Farhang-e Farsi-ye Amid, 2 vols, Amir Kabir 1369/1990", "kind": "website", "url": "https://vajehyab.com/?q=<word>&d=amid ; https://abadis.ir/fatofa/<word>/ (فرهنگ عمید) ; scan on noorlib: https://noorlib.ir/book/view/28973?pageNumber=<N>&viewType=pdf", "lookup_hint": "Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Entry-level verification only."}
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


### [2026-09-04T23:05:43.671Z] TOOL RESULT

```
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
process
sources
----
build_site.py
fetch_source.py
ganjoor.py
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
----
```


## [2026-09-04T23:05:47.923Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,80p /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-04T23:05:47.957Z] TOOL RESULT

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


## [2026-09-04T23:05:48.629Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-60.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:4000])\n\"",
 "description": "Sample existing verification output"
}
```


### [2026-09-04T23:05:50.698Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Apo, Apâ, Apu, Pu 3, Pô 1",
 "verdict": "confirmed",
 "modern_form": "PIE *h₂epo (*apo, with ablaut/enclitic variants *apā, *ap-u, *pu, *po) 'off, away, from'",
 "note": "Pokorny IEW 53-55 heads the entry 'apo- (pō̆, ap-u, pu) \"ab, weg\"', i.e. exactly the five shapes Nourai lists (his 'Apâ' = the long-vowel variant apā, 'Pô 1' = Pokorny's po, 'Pu 3' = Pokorny's pu). Language label (Indo-European) and gloss ('off') are right; the current reconstruction writes it *h₂epó, though Hittite āppa is used to argue for laryngeal-less *apo. The whole Latin/Greek/Iranian half of the chart hangs on Pokorny's own remark under *pos that it is 'probably *p + os, Gen.-Abl. to *apo above S. 53 f.', so the root→#3 arrow is Pokorny's, not Nourai's invention. The single weak link on this chart is the item 'eben : later time, evening' in node #1 (and 'evening' in node #2): neither Pokorny nor Watkins/AHD puts the Germanic word for 'evening' under *apo, and Klein assigns it to *epi/*opi.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82epo",
  "https://www.ahdictionary.com/word/indoeurop.html"
 ],
 "ref_check": [
  {
   "ref": "POK:53",
   "status": "supports",
   "note": "POK_01.txt 0-based leaf 61 = printed p.53 (leaf 62 carries the running number '54'): the entry 'apo-, (pō̆, ap-u, pu) \"ab, weg\"' runs pp. 53-55 and contains 'got. af Präf. und Präp. m. Dat. \"von, von—weg\" ... ags. æf, of, as. af, ahd. aba', 'Ableitungen: apo-tero-, ap-ero-, ap-io-, ap-öko-', 'ags. *afoc in engl. awkward, aus *apu-ko-s', and closes 'S. noch idg. *po-ti und *po-s' — exactly the material Nourai's chart draws."
  }
 ],
 "nodes": [
  {
   "id": 1,
   "lang": "Germanic",
   "words": "af; apo-tero; eben; afug",
   "verdict": "disputed",
   "derivation": "Three of the four items are straight reflexes of *apo. (a) 'af' = Proto-Germanic *ab/*af, unstressed preposition/prefix from PIE *h₂epo with regular loss of the final vowel: Gothic af, Old Norse af, Old English of/æf, Old Saxon af, OHG aba/ab- (POK 53; AHD apo- 1a). (b) 'apo-tero' is in fact the PIE comparative *ap(o)-tero- 'further off' (Skt. apataram, OP apataram, Gk. apōtérō), which in Germanic gives *aftar-/*after- > OE æfter, ON eptir, Goth. aftra (AHD apo- 4). Labelling the comparative itself 'Germanic' is a small imprecision, since the formation is PIE, not Germanic. (c) 'afug' = Proto-Germanic *afug-/*abuh- < *apu-ko- 'turned away', whence ON ǫfugr/afugr 'turned backwards', OS avuh, OHG abuh, OE *afoc (POK 54; AHD apo- 6). (d) 'eben : later time, evening' is the problem: this is Proto-Germanic *ēbanþ-/*ēbando- 'evening' (OE ǣfen, OS āƀand, OHG āband, ON aptann). Klein derives it not from *apo but from *epi/*opi — 'cogn. with Gk. ὄπι- in ὄπισθε(ν) \"after, behind\", ὀψέ \"late in the day\" ... hence evening lit. means \"the hinder (= latter) part of the day\"' — and Etymonline calls Proto-Germanic *æbando- 'of uncertain origin'. Neither Pokorny's apo- entry nor Watkins/AHD lists the word. Hence 'disputed' for this one item only.",
   "sources": [
    "https://www.ahdictionary.com/word/indoeurop.html",
    "https://www.etymonline.com/word/awkward",
    "https://www.etymonline.com/word/evening"
   ],
   "ref_check": [
    {
     "ref": "AHD",
     "status": "partial",
     "note": "AHD_watkins1985.txt s.v. 'apo-. Also ap-. Off, away.': '1. Germanic *af in: a. Old English of, æf (> Middle English of, of-), off: OF, OFF ... 4. Suffixed (comparative) form *ap(o)-tero- in Germanic *aftar- in Old English æfter, after, behind: AFTER ... 6. Suffixed form *apu-ko- in Germanic *afug- in Old Norse ǫfugr, turned backward: AWKWARD.' — supports af, apo-tero and afug verbatim, but the entry has no 'evening' item (the AHD index line reads 'EVEN oi-no-', 'EVENTIDE da-'); the current online AHD apo- entry likewise lists only off, ebb, awkward, puny, compote."
    }
   ],
   "consulted": [
    {
     "src": "POK",
     "where": "Bd. I pp. 53-55 (POK_01.txt l
```


## [2026-09-04T23:05:56.914Z] TOOL CALL #9: Bash

```json
{
 "command": "ls site/pages/65.jpg 2>/dev/null; pdftoppm -f 65 -l 65 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg65 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg65.png",
 "description": "Render PDF page 65"
}
```


### [2026-09-04T23:05:59.564Z] TOOL RESULT

```
site/pages/65.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 69111 Sep  4 19:05 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg65.png
```


## [2026-09-04T23:06:01.729Z] TOOL CALL #10: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg65.png"
}
```


### [2026-09-04T23:06:02.255Z] TOOL RESULT

```

```


## [2026-09-04T23:06:02.252Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-04T23:06:32.253Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg65.png')\nprint(im.size)\nim.crop((450,1450,2100,2100)).resize((1650,650)).save('crop_as.png')\nim.crop((450,450,2100,900)).resize((1650,450)).save('crop_arx.png')\n\"",
 "description": "Crop regions of page image"
}
```


## [2026-09-04T23:06:33.404Z] TOOL CALL #12: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-65.json'))\nprint(repr(d['entries'][0]['nodes'][0]['words']))\nprint(repr(d['entries'][2]['nodes'][0]['words']))\n\"",
 "description": "Print exact translit strings"
}
```


### [2026-09-04T23:06:34.354Z] TOOL RESULT

```
(2550, 3300)
```


### [2026-09-04T23:06:36.375Z] TOOL RESULT

```
[{'translit': 'arx, arxt, arkh, arkht', 'gloss': 'leader, master', 'script': None}, {'translit': 'arx-tekton', 'gloss': 'master builder, architect', 'script': None, 'see': ['Tex']}, {'translit': 'arxeion', 'gloss': 'government, public office, government records', 'script': None}]
[{'translit': 'ardĕre', 'gloss': 'to be on fire', 'script': None}, {'translit': 'arĕre', 'gloss': 'to become dry (land)', 'script': None}, {'translit': 'ara', 'gloss': 'an area', 'script': None}]
```


## [2026-09-04T23:06:38.989Z] TOOL CALL #13: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_as.png"
}
```


### [2026-09-04T23:06:39.019Z] TOOL RESULT

```

```


## [2026-09-04T23:06:54.028Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg65.png')\nim.crop((500,1650,800,1900)).resize((1200,1000)).save('crop_zoom.png')\n\"",
 "description": "Zoom on connector junction"
}
```


### [2026-09-04T23:06:56.140Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T23:06:58.793Z] TOOL CALL #15: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_zoom.png"
}
```


### [2026-09-04T23:06:58.819Z] TOOL RESULT

```

```


## [2026-09-04T23:07:09.814Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_arx.png"
}
```


### [2026-09-04T23:07:09.839Z] TOOL RESULT

```

```


## [2026-09-04T23:07:58.344Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['KLN','AHD','POK','FSD','MON','LEW','LAT','SKT','WEB','IEC','SYN','WLD']:\n    e=d.get(k,{})\n    print(k,'|',e.get('page_offset'),'|',e.get('local_file'))\n\"",
 "description": "Show page offsets"
}
```


### [2026-09-04T23:08:01.256Z] TOOL RESULT

```
KLN | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
AHD | 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
POK | POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
FSD | vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
MON | None | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
LEW | 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt
LAT | leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt
SKT | leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
WEB | not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt
IEC | TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
SYN | leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
WLD | Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt']
```


## [2026-09-04T23:08:06.173Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 61 62 63; do echo \"=== KLN_1966 leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | head -120; done",
 "description": "Print KLN leaves 61-63"
}
```


### [2026-09-04T23:08:08.039Z] TOOL RESULT

```
<persisted-output>
Output too large (36.1KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bem2btoc2.txt

Preview (first 2KB):
=== KLN_1966 leaf 61 ===
dj.,  pertaining  to  appeals.  —  L.  appel- latus,  pp.  of  appellare,  ‘to  address,  call’.  See appeal  and  adj.  suff.  -ate. appellation,  n.  —  L.  appelldtio,  gen.  -onis,  fr.  ap¬ pellants,  pp.  of  appellare.  See  prec.  word  and -ion.
Derivative:  appellation-al,  adj. appellative,  adj.  —  L.  appelldtivus,  fr.  appelldtus, pp.  of  appellare.  See  appeal,  v.,  and  -ative. appellee,  n.,  a  person  appealed  against  daw).  — F.  appele,  pp.  of  appeler,  ‘to  call,  address'.  See appeal,  v.,  and  -ee.
append,  tr.  v.,  to  attach;  to  join.  —  OF.  apendre (F.  appendre),  fr.  L.  appendere,  ‘to  hang  some¬ thing  on’,  fr.  ad-  and  pendere,  ‘to  cause  to  hang’.
See  pendant.
Derivatives:  appendage,  n.,  appendag-ed,  adj. appendant,  adj.  and  n.  —  F.,  pres.  part,  of  ap¬ pendre.  See  prec.  word  and  -ant. appendectomy,  n.,  removal  of  the  appendix  (sur¬ gery).  —  A  hybrid  coined  fr.  L.  appendix  and Gk.  -EXTOula,  ‘a  cutting  out  of’,  fr.  extout,,  ‘a cutting  out’.  See  appendix  and  -eetomy. appendicitis,  n.,  inflammation  of  the  vermiform appendix.  —  A  Medical  L.  hybrid  coined  fr.  L. appendix  (see  next  word)  and  -itis,  a  suff.  of Greek  origin.
appendix,  n.  —  L.,  ‘something  hung  on,  some¬ thing  appended’,  fr.  appendere.  See  append. Derivative:  appendix,  tr.  v.
apperceive
approximate
94  95
...
</persisted-output>
```


## [2026-09-04T23:08:11.650Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E '.{200}arch(itect|ive|aeo|aic|-)[^ ]{0,20}.{0,600}' KLN_1966.txt | head -20",
 "description": "Grep KLN for arch entries"
}
```


### [2026-09-04T23:08:13.890Z] TOOL RESULT

```
1839:dL.,  compounded  of aeto-  and  Gk.  oxupoq,  ‘lizard’.  See  sauro-. af-,  assimilated  form  of  ad-  before/, afar,  adv.  —  Formed  fr.  a-,  ‘on’,  and  far. afeard,  afeared,  adj.,  afraid  (archaic).  —  ME. afered,  fr.  OE.  aftered,  pp.  of  dfreran,  ‘to  frighten, terrify’,  formed  from  intensive  pref.  a-  and  fxran, ‘to  terrify’.  See  fear,  v.  and  n. affability,  n.  —  F.  affabilite,  fr.  L.  affdhiiitdtem, acc.  of  affabilitas,  ‘courtesy,  kindness,  affability’, fr.  affdbiiis.  See  affable  and  -ity. affable,  adj.,  easy  to  speak  to;  courteous.  —  F., fr.  L.  affabilis,  ‘kind,  friendly,  affable’,  lit.  ‘he who  can  be  (easily)  spoken  to’,  fr.  affari,  ‘to speak  to’,  fr.  ad-  and  fan,  ‘to  speak’.  See  fable and  cp.  esp.  ineffable.
1979:,  one  of  the  chief  gods  of  the  Vedas.  — OI.  Agnih,  ‘the  god  of  fire’,  fr.  agnih,  ‘fire’,  which is  cogn.  with  L.  ignis,  ‘fire’.  See  igneous, agnize,  tr.  v.,  to  recognize  (archaic).  —  Formed fr.  L.  agnoscere  on  analogy  of  recognize  (fr.  L. recognoscere).
2388:watus,  ‘staff’,  ON.  voir,  ‘a round  stick’,  fr.  I.-E.  base  *wal~,  *wel-,  ‘to  turn, bend,  twist,  roll’.  See  volute  and  cp.  words  there referred  to.  For  the  second  element  see  arch-, am,  v.  —  OE.  eom,  earn,  am,  rel.  to  ON.  em, Goth,  im,  for  I.-E.  *esmi,  whence  also  OI.  dsmi, Hitt,  esmi,  Arm.  em,  Gk.  dpi,  Lesbian  and Thessal.  ep.p.1,  Dor.  Alb.  jam,  L.  sum
2805:in  black  birds  of  the  cuckoo family.  —  Sp.  ani.  Port,  ani,  fr.  Tupi  ani. anicut,  annicut,  n.,  a  dam  (Anglo-lnd.)  —  Tamil anai  kattu,  ‘dam  building’, anigh,  adv.,  new  (pseudo-archaic).  —  Formed on  analogy  of  afar,  etc.,  fr.  a-,  ‘on’,  and nigh.
3321:ence  al¬ so  ipyp,  ‘beginning,  first  cause,  origin,  first principle,  office’),  and  in  gradational  relation¬ ship  to  iip/aptop,  ‘leader,  chief’.  Cp.  arch,  ‘chief’, -arch.  Cp.  also  archaeo-,  archaic,  archaism, arche,  architect,  archon,  -archy.
3324: archeo-, resp.  arche-,  combining  form  meaning  ‘ancient, primeval,  primitive.  —  Gk.  ap/octo-,  apyai-,  fr. ap/atop,  ‘ancient’,  lit.  ‘from  the  beginning’,  fr. ipxh,  ‘beginning’.  Sec  arch-, archaeological,  archeological,  adj.  —  Formed with  adj.  suff.  -al  fr.  Gk.  dpxatoXoyt.x6<;,  ‘per¬ taining  to  archaeology’,  fr.  dpx°uoXoyia.  See next  word.
3326:gs’,  compound¬ ed  of  apyaio-  (see  archaeo-)  and  Gk.  -Xoytd,  fr. -Xdyop,  ‘one  who  speaks  (in  a  certain  manner); one  who  deals  (with  a  certain  topic)’.  See  -logy. Derivatives :  archaeological  (q.v.),  archaeolog-ist or  archeolog-ist,  n.
3328:,  old-fashioned,  antiquated,  obso¬ lete.  —  Gk.  apyxtV.op,  ‘old-fashioned,  anti¬ quated',  fr.  ApyaTo ;,  ‘ancient’,  fr.  ap yf„  ‘be¬ ginning’.  See  arch-  and  cp.  Archaean. Derivative:  archaic-al-ly,  adv. archaism,  n.,  use  of  an  obsolete  word.  —  Gk. xp/aiapto:,  fr.  izyxeZv.'i,  ‘to  be  old-fashioned, copy  the  ancients  in  language’,  fr.  ip/atop,  ‘an¬ cient’.  See  prec.  word  and  -ism. archaist,  n.,  one  fond  of  using  archaisms.  — Formed  with  suff.  -ist  fr.  Gk.  ipyalop,  ‘ancient’. See  archaic.
3336: and  Siaxovop, ‘servant,  minister  of  a  church’.  See  deacon, arche,  n.,  the  first  principle  (Greek  philos.)  —  Gk. dpyr,,  ‘beginning,  first  cause,  origin,  first  prin¬ ciple’.  See  arch-.
3339:l.  to  yeX up,  ‘tortoise’,  lit.  ‘the  yellow  animal’, fr,  I.-E.  base  *ghel-,  ‘yellow’;  see  yellow, archenteron,  n.,  the  primitive  enteron  of  a  gas- trula  ( zool .)  —  Formed  fr.  arch-  and  Gk.  Ivxepov, ‘intestine’.  See  enteric.
3343:k .  apysTU-ov, ‘pattern,  model’,  prop.  neut.  of  the  adjective dp/rmiro?,  ‘stamped  first',  used  as  a  noun,  fr. ip yz-(=  dp/t-), ‘first’,  and  tu-oc, ‘a  blow,  mark of  a  blow'.  See  arch-  and  type, archi-,  pref.  meaning  i)  ‘chief’,  as  in  archidia- conal;  2)  ‘primitive,  original’  as  in  archiplasm.  — Gk.  dp/i-,  rel.  to  dp/6;,  ‘leader,  chief,  ruler’, dpyr.v,  ‘to  begin,  to  rule’.  See  arch-, archiater,  n.,  the  chief  physician  at  the  court  of  a Greek  king  or  Roman  emperor  ( Greek  and Roman  hisr.)  —  Gk.  dp/taxpdp,  ‘court  phy¬ sician’,  fr.  dpyi-  (see  archi-)  and  iaxpd;,  ‘physi¬ cian’.  See  iatric.
3347:sted  by the  numerous  Greek  words  beginning  with  dpyi- . archiplasm,  n.,  1)  primitive  protoplasm;  2)  ar- choplasm. — Compounded  of  archi-  and  -plasm. Derivative:  archiplasm-ic,  adj. architect,  n.  —  F.  architecte,  fr.  L.  architectus,  fr. Gk.  ap/enberav,  ‘master  builder’,  fr.  dp/t-, ‘chief’,  and  text<ov,  ‘carpenter,  builder’,  which is  rel.  to  ttiyyT,,  ‘art,  skill,  craft’.  See  archi-  and text  and  cp.  technic,  tectonic, architectonic,  adj.  —  L.  architectonicus ,  fr.  Gk, dpXiTExxovixog,  ‘pertaining  to  a  master  builder’, fr.  dpxiTEXTtnv.  See  prec.  word  and  -ic. architectonics,  n.  —  See  prec.  word  and  -ics. architecture,  n.  —  F.,  fr.  L.  architectiira,  fr.  ar¬ chitectus.  See  architect  and  -ure.
3349:  part  of  the  entablature (archil.)  —  It.  architrave ,  fr.  archi-  and  trave, ‘beam’,  fr.  L.  trabem ,  acc.  of  trabs.  See  trabeate. archive,  n.,  generally  used  in  the  pi. —  F.  archives, fr.  L.  archivum,  archium,  ‘the  archives',  trans¬ literation  of  Gk.  dp/etov,  ‘official  building’,  pi. tx  dpyetx,  ‘public  records,  archives',  fr.  dp/t], ‘beginning,  origin,  first  place,  office’.  See  arch- and  cp.  arche.
3395:argamdn,  ‘purple’.  Cp.  Ak¬ kad.  argamannu,  of  s.m.  Cp.  also  agrimony.  For the  ending  -cow)  in  apye|ic I>vr),  cp.  dcvspuiw),  ‘the wind  flower’  (see  anemone). argent,  n.,  silver  (archaic).  —  F.,  fr.  L.  argentum, ‘silver’,  which  is  cogn.  with  Gk.  Spyupo?,  ‘silver’, prop,  ‘the  white  (metal)’,  fr.  dpyo?  (dissimul¬ ated  fr.  *ipypo?),  ‘shining,  bright,  white’;  fr. I.-E.  base  *arg-,  ‘to  shine’,  whence  also  OI. rirdh,  ‘shining,  glowing,  bright’,  rajatam ,  Aves¬ tic  ‘r*zata,  ‘silver’,  OI.  drjunah,  ‘shining,  white’, Toch.  A  drki,  ‘white’  (said  of  teeth),  arkyant, ‘silver’,  B  arkwi,  of  s.m.,  arkwirme,  ‘light  color’, Hitt,  harkish.  ‘bright,  clear’,  Thracian  4pytX<x;,
4565:.  OF.  bataillier,  batailler  (F.  batailler),  ‘to fight’,  fr.  bataille.  See  battle,  n.,  and  cp.  em¬ battle,  ‘to  prepare  for  battle’, battle,  tr.  v.,  to  equip  with  battlements  ( archaic or  poetic).  —  OF.  bataillier,  ‘to  equip  with battlements,  fortify’,  fr.  batailles,  ‘battlements’, pi.  of  bataille,  ‘battle’.  See  battle,  n. battledore,  n.,  a  wooden  instrument  with  a  long handle  and  a  flat  board  used  to  strike  a  shuttle¬ cock.  —  ME.,  prob.  fr.  O Proven?,  batedor,  ‘an instrument  for  beating’,  fr.  L.  battuere,  battere, ‘to  beat,  strike’  (see  batter,  ‘to  beat’);  influenced in  form  by  beetle.
4824:  bespatter-er,  n. bespeak,  tr.  v.  —  ME.  bespeken,  fr.  OE.  be- sp(r)ecan,  ‘to  speak  about’,  rel.  to  Du.  bespreken, G.  besprechen.  See  be-  and  speak, besprent,  adj.,  sprinkled  (archaic).  —  ME.  be- spreynt,  pp.  of  besprengen,  fr.  OE.  besprengan, ‘to  besprinkle’,  rel.  to  Du.  and  G.  besprengen, of  same  meaning.  See  be-  and  sprinkle  and  cp. next  word.
5492: ME., fr.  OF.  brasseure,  formed  fr.  braz  (F.  bras), ‘arm’  (see  brace,  ‘clasp,  buckle’),  with  suff.  -cure, ure,  which  was  changed  in  English  to  -er. brach,  n.,  a  bitch  hound  (archaic).  —  ME.  brache, ‘a  scenting  hound’,  fr.  OF.  brache,  which  is  of WTeut.  origin;  cp.  MDu.  bracke,  OHG.  brac- cho,  MHG.,  G.  bracke,  ‘hound,  setter’.  It. bracco.  Proven?,  brae,  of  s.m.,  are  Teut.  loan words;  F.  braque  is  borrowed  either  fr.  Italian or  fr.  Provencal.  The  above  Teut.  words  are rel.  to  MHG.  brxhen,  ‘to  smell’,  and  cogn. with  L.  fragrdre,  ‘to  smell  sweetly’.  See  fra¬ grant.
5659:health’.  Cp.  G.  jemartdes Gesimdheit  ausbringert,  ‘to  drink  one’s  health’, brindled,  adj.,  streaked  with  a  dark, esp.  brown  or tawny,  color.  —  Formed — prob.  after  kindled — fr.  archaic  blinded,  fr.  ME.  brended,  which  is  rel. to  brand.
5734:e,  bros- me,  G.  Brosam,  Brosame,  ‘crumb’.  Cp.  debris, debruise.  Cp.  also  burst.  Cp.  also  frustum. Derivatives :  bruise,  n.,  bruis-er,  n.,  bruis-ing,  n. bruit,  n.,  noise;  rumor  (archaic).  —  F.  ‘noise’, orig.  pp.  of  bruire,  ‘to  rustle,  rumble’,  used  as  a noun.  F.  bruire  derives  fr.  VL.  *brugere,  which is  a  blend  of  L.  rugire,  ‘to  roar’,  with  VL.  *bra- gere,  ‘to  whine,  cry’  (whence  F.  braire,  ‘to  bray’ (see  bray,  ‘to  cry’).  L.  rugire  (whence  VL.  *ru- gere),  ‘to  roar’,  is  cogn.  with  Gk.  Epuystv,  ‘to bellow,  roar',  opufraySog,  ‘a  loud  noise’,  pu£etv (for  *p(>Yi£iv),  ‘to  growl,  snarl’,  OSlav.  rykati, ryknQti,  ‘to  roar,  bellow’,  OE.  ryn  (for  *ruhjan), OHG.  rohon,  of  s.m.
7216:ge  d’affaires,  n.,  1)  deputy  to  an  ambassador; 2)  representative  of  a  country  sent  to  another, smaller  country.  —  F.,  lit.  ‘charged  with  affairs’, charger,  n.,  a  large  dish  (archaic.)  —  ME.  char- geour,  fr.  ‘utensil  for  loading  or  carrying  on  it’, fr.  VL.  *carricatdrium,  fr.  *carricatus,  pp.  of *carricare.  See  charge.
```


## [2026-09-04T23:08:20.796Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'archive,  n.' in l or 'arch-,  pref' in l or 'ardent' in l.lower() or ' area,  n' in l:\n        print('=== leaf',i,'===')\n        print(l[:200].replace('\\n',' '))\n        print('...')\nEOF",
 "description": "Locate KLN leaves with arch/area entries"
}
```


### [2026-09-04T23:08:23.301Z] TOOL RESULT

```
=== leaf 28 ===
s.v.  aiyiaXA?. aegicrania,  n.,  representation  of  goats’  heads (1 Greek  and  Roman  antiq.)  —  ModL.,  fr.  Gk. at?,  gen.  aiydp,  ‘goat’,  and  xpavla,  pi.  of xpavEov,  ‘skull’.  For  the  
...
=== leaf 33 ===
e,  n„  hook,  clasp.  —  F.  agrafe,  back  forma¬ tion  fr.  agrafer,  ‘to  hook,  fasten’,  fr.  d,  to (see  a),  and  OF.  grafer,  ‘to  fasten  with  a  hook’, fr.  grafe,  ‘hook’,  fr.  OHG.  k
...
=== leaf 63 ===
c  and  duke  and cp.  the  second  element  in  viaduct,  ventiduct, aqueous,  adj.,  watery;  like  water.  —  Formed  fr. L.  aqua,  ‘water’,  on  analogy  of  F.  aqueux,  the English  suff.  -cou
...
=== leaf 64 ===
.  of  L.  arbor,  ‘tree’.  See  arbor,  ‘tree’,  and -cle. arbuscule,  n.,  a  tuft  of  hairs  (zool)  —  See  prec. word  and  -cule. arbustum,  n.,  a  copse;  an  orchard.  —  L.,  ‘a  place wher
...
=== leaf 65 ===
 an¬ archy,  monarchy,  —  L.  -archia,  fr.  Gk.  -ap/id, ‘rule’,  fr.  dpx<k,  ‘leader,  chief,  ruler’.  See  -arch and  -y  (representing  Gk.  -ta). arciform,  adj.,  having  the  form  of  an  a
...
=== leaf 66 ===
  Asia  (Ovis  am- mon).  —  Mongolian. argand  lamp.  —  Named  after  its  inventor  Aim6 Argand,  a  Swiss  physicist  (1755-1803). Argemone,  n.,  a  genus  of  plants  of  the  poppy family  (bot
...
=== leaf 68 ===
 and  revert, arpeggio,  n.,  the  playing  of  the  notes  of  a  chord in  rapid  succession  instead  of  simultaneously; a  chord  on  which  the  notes  are  so  played (mus.)  —  It.,  fr.  arpe
...
=== leaf 70 ===
uffixes  and  cp.  -arium, and  -er  in  the  sense  ‘receptacle  for’. -ary,  adj.  suff.,  meaning  ‘pertaining  to’,  as  in exemplary.  — -  L .  -arts.  The  regular  English  equiv¬ alent  of  L
...
=== leaf 269 ===
for  measuring  the magnifying  power  of  telescopes.  —  Com¬ pounded  of  dyna-  and  Gk.  pixpov,  ‘measure’. See  meter,  ‘poetical  rhythm’. Derivatives :  dynametr-ic,  dynametr-ic-al,  adjs. d
...
=== leaf 281 ===
otion  (see  motion)  to  mouvoir,  ‘to  move’.  F. emouvoir  derives  fr.  OF.  esmovoir,  fr.  VL.  *ex- movere,  which  corresponds  to  L.  emovere,  ‘to move  out,  move  away;  to  stir  up,  ag
...
=== leaf 317 ===
 ,  Russ,  paporot',  Gaul,  ratis  (for *pratis ),  OIr.  raith,  of  s.m.,  Gk.  nrlpic,  ‘fern’, 7rrcp6v,  ‘feather’.  See  feather. 585 Derivatives:  fern-ed,  adj.,  fern-ery,  n.,  fern¬ like,  
...
```


## [2026-09-04T23:08:34.561Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nkeys=['gradational  relation','architect,  n.','archive,  n.','ardent','area,  n','arson','archaeo-','arĕre','arere']\nfor i,l in enumerate(leaves):\n    hits=[k for k in keys if k in l]\n    if hits:\n        nums=re.findall(r'\\b(\\d{2,4})\\b',l)\n        print(i,hits,'| numbers:',nums[:12])\nEOF",
 "description": "Map KLN leaves to printed page numbers"
}
```


### [2026-09-04T23:08:37.183Z] TOOL RESULT

```
17 ['gradational  relation'] | numbers: ['10', '815', '11', '12']
28 ['area,  n'] | numbers: ['32', '1822', '95', '863']
33 ['ardent'] | numbers: ['40', '1494', '1555', '41', '10']
51 ['gradational  relation'] | numbers: ['1690', '1832', '1783', '76', '96', '309', '1814', '1874']
59 ['gradational  relation'] | numbers: ['90', '91', '1796', '1886', '58']
60 ['arere'] | numbers: ['92', '93', '533']
63 ['ardent', 'arere'] | numbers: ['1744', '1829', '1815', '1525', '1609']
64 ['gradational  relation', 'architect,  n.', 'archive,  n.', 'area,  n', 'archaeo-'] | numbers: ['09', '100', '101', '2877', '212']
65 ['ardent', 'area,  n', 'arson', 'arere'] | numbers: ['102', '1795', '35', '1560', '1624', '1605', '103', '1792', '1841']
66 ['ardent'] | numbers: ['1755', '1803', '1852', '1916', '1872', '1961', '1894', '1858', '1929', '336', '104', '105']
68 ['ardent', 'arson', 'arere'] | numbers: ['108', '109']
70 ['ardent', 'arere'] | numbers: ['1823', '1900', '156', '1809', '1663', '1704', '112', '30', '13', '10', '51', '27']
87 ['gradational  relation'] | numbers: ['10', '1620', '1706', '144', '145', '1893', '176']
89 ['area,  n'] | numbers: ['148', '149', '1778', '1829', '23', '403']
96 ['gradational  relation'] | numbers: ['161', '1847', '1922', '1781', '1811', '15']
97 ['gradational  relation'] | numbers: ['529', '164', '165', '35', '18', '1748', '1832']
107 ['gradational  relation'] | numbers: ['1742', '1819', '1862', '1949', '1909', '182', '183', '1740', '1866', '1951', '1907', '1843']
108 ['gradational  relation'] | numbers: ['1723', '1803', '19', '28', '184', '185', '1918', '1903', '1917', '1917', '1493', '1541']
109 ['gradational  relation'] | numbers: ['1951', '268', '707', '186', '187']
111 ['gradational  relation'] | numbers: ['1729', '1811', '258', '59', '1589', '1792', '1815', '1848']
112 ['gradational  relation'] | numbers: ['81', '1774', '1842', '193', '1818', '1799']
120 ['gradational  relation'] | numbers: ['1587', '77', '206', '207', '563', '483', '1715']
130 ['gradational  relation'] | numbers: ['1820', '93', '226', '227', '1509', '64', '1830', '200']
137 ['arere'] | numbers: ['1501', '76', '1797', '1868', '1775', '1821', '240']
141 ['arere'] | numbers: ['1688', '1744', '248', '249']
142 ['gradational  relation'] | numbers: ['597', '250', '251']
153 ['arere'] | numbers: ['1836', '48', '270', '271', '1833', '1905', '167', '1874', '1831', '1509', '64']
156 ['gradational  relation'] | numbers: ['276', '277', '255', '206']
157 ['gradational  relation'] | numbers: ['1718', '79', '278', '279']
159 ['gradational  relation'] | numbers: ['282', '283', '1791', '1609']
168 ['gradational  relation'] | numbers: ['299', '18', '1840', '1905', '300']
170 ['gradational  relation'] | numbers: ['910']
174 ['gradational  relation'] | numbers: ['310', '311', '69', '1824', '93']
182 ['gradational  relation'] | numbers: ['327', '1632', '1713', '1798', '1857']
194 ['gradational  relation'] | numbers: ['1473', '1543', '254', '350']
198 ['gradational  relation'] | numbers: ['1936', '1700', '358', '359']
203 ['gradational  relation'] | numbers: ['37']
207 ['gradational  relation'] | numbers: ['374', '05', '375', '1956', '219', '04', '1832', '1919']
209 ['gradational  relation'] | numbers: ['29', '23', '69', '378', '379']
217 ['gradational  relation'] | numbers: ['09', '393', '14', '231', '394']
238 ['gradational  relation'] | numbers: ['434', '435']
242 ['gradational  relation'] | numbers: ['81', '1805', '69']
243 ['gradational  relation'] | numbers: ['87', '81', '1833', '1908']
250 ['gradational  relation'] | numbers: ['456', '457']
257 ['gradational  relation'] | numbers: ['61', '470', '471', '860']
269 ['ardent'] | numbers: ['1646', '1716', '1748', '1832', '1833', '96', '1867', '1816', '92', '1882', '17']
275 ['gradational  relation'] | numbers: ['1879', '1955', '31', '29']
281 ['ardent'] | numbers: ['1817', '81', '1858', '516', '517']
293 ['gradational  relation'] | numbers: ['540']
304 ['gradational  relation'] | numbers: ['560', '561', '1813', '55', '61']
314 ['gradational  relation'] | numbers: ['580', '1729', '97', '581', '1882']
317 ['ardent'] | numbers: ['585', '1865', '1935', '586', '1717', '97']
323 ['gradational  relation'] | numbers: ['252']
333 ['gradational  relation'] | numbers: ['1614', '1687', '615', '1712', '80']
348 ['gradational  relation'] | numbers: ['1708', '56', '1777', '1855', '644', '1778', '1850', '646', '1774', '1856', '1775', '1815']
351 ['gradational  relation'] | numbers: ['01', '650', '651', '1808', '82', '1872', '15']
357 ['gradational  relation'] | numbers: ['661', '1714', '86', '1821', '1902', '1779', '1848']
359 ['gradational  relation'] | numbers: ['664', '1786', '1889', '665', '1813', '78', '1848', '20', '1541', '1754', '1794', '83']
361 ['gradational  relation'] | numbers: ['668', '1561', '1627', '669', '1855', '1916', '1882', '369', '1894', '1938', '670', '1728']
366 ['gradational  relation'] | numbers: ['678', '679', '1820', '1841', '1783', '1859', '1807', '43', '1792', '1857', '1840', '1778']
367 ['gradational  relation'] | numbers: ['681', '1785', '1863']
368 ['gradational  relation'] | numbers: ['682', '1684', '1757']
381 ['gradational  relation'] | numbers: ['707', '1822', '1899', '878', '1782', '1859', '1809', '91', '1853', '1870', '708', '1836']
384 ['gradational  relation'] | numbers: ['1871', '713', '1905', '100', '795', '1000', '81', '714']
385 ['gradational  relation'] | numbers: ['1770', '1831', '715', '622', '1817', '80', '1784', '1845']
388 ['gradational  relation'] | numbers: ['720', '1823', '1900', '1878', '1797', '1878', '1860', '1945', '895', '47', '1918', '721']
394 ['gradational  relation'] | numbers: ['732', '36', '7704', '6776', '460', '357', '806', '05', '05', '770', '733', '1766']
399 ['gradational  relation'] | numbers: ['56', '742', '1766', '1844', '65']
404 ['gradational  relation'] | numbers: ['750', '751']
415 ['gradational  relation'] | numbers: ['772', '773']
419 ['arson'] | numbers: ['780', '781']
433 ['gradational  relation'] | numbers: ['1809', '83', '1865', '806', '1748', '1832', '1780', '28', '1864', '1871', '1845', '205']
453 ['gradational  relation'] | numbers: ['840', '841', '25', '29']
474 ['gradational  relation'] | numbers: ['363', '882', '1781', '1855', '1820', '1750', '1817', '1791', '1821', '1902', '1865', '1837']
502 ['gradational  relation'] | numbers: ['1654', '1722', '1598', '1666', '935', '936']
513 ['gradational  relation'] | numbers: ['957']
515 ['gradational  relation'] | numbers: ['1748', '1832', '1819', '80', '16']
535 ['gradational  relation'] | numbers: ['1910', '89', '1620', '1706', '998', '999']
567 ['arere'] | numbers: ['1080', '1060', '1061', '1869']
570 ['gradational  relation'] | numbers: ['1066']
572 ['gradational  relation'] | numbers: ['427', '428', '1070', '1071']
579 ['gradational  relation'] | numbers: ['661', '750', '756', '1031', '1820', '1082', '1083', '38']
585 ['gradational  relation'] | numbers: ['1094', '1095', '185', '253']
592 ['gradational  relation'] | numbers: ['1743', '94', '1777', '1108', '1793', '1858', '1833', '1799', '1868', '1840', '25']
596 ['gradational  relation'] | numbers: ['1518', '80', '1766', '1828', '803', '1758', '1840', '1802', '642', '761', '1741', '1811']
603 ['arere'] | numbers: ['1879', '1300', '1895']
605 ['arson', 'arere'] | numbers: ['1847', '1134', '1135']
606 ['arere'] | numbers: ['1829', '1910', '12', '13', '23', '27']
610 ['arere'] | numbers: ['483', '1564', '1617', '40']
621 ['arson'] | numbers: ['1694', '1773', '1164', '100', '328', '389']
627 ['gradational  relation'] | numbers: ['05', '1817', '91', '601', '65', '765', '1559', '1622', '65', '017', '65', '15']
643 ['arson'] | numbers: ['1775', '1838', '1803', '1206', '080', '0861', '080', '06', '0861', '08', '06', '086']
648 ['gradational  relation'] | numbers: ['1721', '64', '79', '1216', '1217']
651 ['arere'] | numbers: ['93', '1832', '98', '85', '1798', '1857']
653 ['arere'] | numbers: ['1224', '1225', '1778', '1829', '1226', '1227']
662 ['arere'] | numbers: []
693 ['gradational  relation'] | numbers: ['1879', '198', '201', '598']
695 ['arson'] | numbers: ['1307', '1795', '1821', '1706', '1915']
707 ['arere'] | numbers: ['30', '1329', '30']
709 ['arere'] | numbers: ['27', '131']
720 ['gradational  relation'] | numbers: ['929', '1354', '1355', '1806', '69', '1845', '1923', '1804', '82', '1877', '1957', '464']
724 ['gradational  relation'] | numbers: ['1848', '1901', '1811', '99', '445', '446', '1798']
738 ['gradational  relation'] | numbers: ['1814', '94', '1814', '94', '1390']
743 ['gradational  relation'] | numbers: []
744 ['gradational  relation'] | numbers: ['1723', '88', '1401', '77', '308', '1402']
746 ['gradational  relation'] | numbers: []
747 ['gradational  relation'] | numbers: ['712', '1406']
755 ['gradational  relation'] | numbers: ['1802', '1843', '1422', '1717', '97', '1754']
761 ['gradational  relation'] | numbers: ['11', '21', '15', '37', '41', '29', '35', '29', '35']
764 ['gradational  relation'] | numbers: ['1439', '1761', '1842', '1440', '1441', '1488', '1755']
769 ['gradational  relation'] | numbers: ['987', '1449', '255', '206', '70', '19', '57', '194', '308', '183', '1450', '1451']
776 ['gradational  relation'] | numbers: ['1953', '1765', '1829']
778 ['gradational  relation'] | numbers: ['1466', '1467', '1830', '1797', '1871', '1583', '1645', '565', '1539', '1604', '1526', '62']
784 ['gradational  relation'] | numbers: ['1715', '87', '697', '1478', '1479']
793 ['gradational  relation'] | numbers: ['1588', '1679', '1656', '1852', '1933', '1844', '1930']
796 ['arson'] | numbers: ['1501']
798 ['gradational  relation'] | numbers: ['1504', '1505', '1787', '1864', '1844', '1929', '1882', '425', '70']
799 ['gradational  relation'] | numbers: ['1506', '1507', '90', '1719', '1772', '1748']
800 ['gradational  relation'] | numbers: ['91', '1508', '1786', '1889', '1692']
801 ['gradational  relation'] | numbers: ['705', '706', '747', '748', '1818', '89', '1854']
805 ['gradational  relation'] | numbers: ['300', '1762', '1807', '1792', '1518']
806 ['gradational  relation'] | numbers: ['686', '753', '1904', '1872', '1949', '760']
807 ['gradational  relation'] | numbers: ['1520', '36', '1644', '1737', '1662']
808 ['gradational  relation'] | numbers: ['1855', '1913', '1829', '94', '1888', '1944']
809 ['gradational  relation'] | numbers: ['604', '605']
810 ['gradational  relation'] | numbers: ['1776', '1835', '1778', '1829', '1787', '1778', '1821', '1667', '1745', '1726', '1793', '1864']
811 ['gradational  relation'] | numbers: ['552', '752', '1529', '484', '1752', '1831', '1776', '1530', '1531']
812 ['gradational  relation'] | numbers: ['499']
825 ['gradational  relation'] | numbers: ['1493', '1541', '1614', '72', '1556', '1844', '96', '1885', '96', '514', '17']
846 ['gradational  relation'] | numbers: ['1598', '1599', '1827', '1905', '1861', '1832', '1919']
849 ['gradational  relation'] | numbers: ['38', '100', '1646', '1716', '1710', '86', '1604', '1606', '61']
853 ['gradational  relation'] | numbers: ['1779', '1848', '1828', '1610', '1611']
854 ['gradational  relation'] | numbers: []
857 ['gradational  relation'] | numbers: ['13']
858 ['gradational  relation'] | numbers: ['431', '404']
860 ['gradational  relation'] | numbers: ['22', '40', '686', '500', '1000', '1907', '958', '1730', '79', '86']
861 ['gradational  relation'] | numbers: []
862 ['gradational  relation'] | numbers: ['1626', '1639', '1713', '1695']
864 ['gradational  relation'] | numbers: ['1630', '1796', '1873', '1608', '47']
869 ['arere'] | numbers: ['040', '1641', '1948', '1772', '1834', '345']
871 ['gradational  relation'] | numbers: ['1644', '1043', '1300']
872 ['gradational  relation'] | numbers: ['30', '1556', '1643', '1040', '1647', '24', '579']
873 ['gradational  relation'] | numbers: ['1795', '1878', '1841', '648', '1815', '77', '1866', '100']
875 ['gradational  relation'] | numbers: ['1834', '96', '1894', '12', '18', '36', '01', '1874', '1965']
878 ['gradational  relation'] | numbers: ['1835', '1911', '1850', '1707', '78', '1657', '23', '27', '23', '27', '1855', '1913']
879 ['gradational  relation'] | numbers: ['1884']
888 ['gradational  relation'] | numbers: ['1724', '1803', '1676', '1785', '1863', '1776', '1854', '1812', '1821', '67']
889 ['arere'] | numbers: ['1524', '85', '10', '1748', '1832', '1679', '35', '95']
891 ['arson'] | numbers: ['1755', '809', '1800', '84']
895 ['gradational  relation'] | numbers: ['1661', '1730', '1594', '1671', '1640', '93', '599', '1707', '88', '1691', '1779', '1848']
```


## [2026-09-04T23:08:44.999Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in (64,65):\n    print('===== leaf',i,'=====')\n    print(leaves[i])\nEOF",
 "description": "Print KLN leaves 64 and 65"
}
```


### [2026-09-04T23:08:47.298Z] TOOL RESULT

```
===== leaf 64 =====
.  of  L.  arbor,  ‘tree’.  See  arbor,  ‘tree’,  and -cle.
arbuscule,  n.,  a  tuft  of  hairs  (zool)  —  See  prec. word  and  -cule.
arbustum,  n.,  a  copse;  an  orchard.  —  L.,  ‘a  place where  trees  are  planted ;  an  orchard’,  prop.  neut. of  arbustus,  ‘planted  with  trees’,  used  as  a  noun, which  stands  for  *arbos-to-s,  fr.  arbds,  arbor, ‘tree’.  See  arbor,  ‘tree’.
Arbutus,  n.,  1)  a  genus  of  evergreen  trees  of  the heath  family;  2)  (not  cap.)  a  tree  of  this  genus. —  L.,  ‘the  strawberry  tree’,  of  obscure  origin, arc,  n.  —  OF.  (=  F.)  arc ,  fr.  L.  arcus,  ‘bow,  arch’, which  is  cogn.  with  Goth,  arlvazna,  ‘arrow’,  OE. earh,  ON.  dr,  of  s.m.;  but  Russ,  rakita,  Czech rokyta,  ‘willow’,  and  Gk.  apxup,  ‘net’,  are  not cognate.  Cp.  arcade,  arch,  arrow,  and  the  first element  in  arbalest,  arciform,  arcuate,  arculite, arquebus.
area,  n.,  a  chest.  —  L.,  fr.  arcere,  ‘to  enclose’.
See  arcanum  and  cp.  Arcella. arcade,  n.  —  F.,  fr.  It.  areata,  a  derivative  of  arco , ‘arc’,  fr.  L.  arcus,  of  s.m.  See  arc  and  -ade. Derivative:  arcad-ed,  adj.
Arcadia,  n.,  a  district  in  ancient  Greece,  pro¬ verbial  for  the  rural  life  of  its  inhabitants.  — L.,  fr.  Gk.  ’ApxaSia,  fr.  ’  Apxaq,  gen.  ’ApxaSop =  Areas,  the  founder  of  Arcadia.
Arcadian,  adj.,  and  n.  —  Formed  with  suff.  -an fr.  L.  Arcadia.  See  prec.  word, arcanum,  n.,  secret,  mystery.  —  L.  arcanum,  prop, subst.  use  of  the  neut.  of  arcanus,  ‘shut  up, secret’,  orig.  ‘enclosed  in  a  chest’,  fr.  area,  ‘chest, coffin’,  which  is  rel.  to  arcere,  ‘to  enclose,  keep away,  ward  off’,  and  cogn.  with  Gk.  dtpxeiv,  ‘to keep  off’,  apxop,  ‘defense’,  apxt 09,  ‘safe,  sure’. Arm.  argel,  ‘obstacle’,  argelum,  ‘I  lock  in’,  and possibly  also  with  Lith.  raktas,  ‘key’,  rakinti,  ‘to shut  lock’.  These  words  stand  in  gradational relationship  to  Orcus,  name  of  the  god  of  the infernal  regions  in  Roman  mythology.  Cp.  area, Arcella,  ark,  coerce,  exercise,  Orcus.  Cp.  also askari,  lascar,  autarchy,  ‘self  sufficiency’. Arcella,  n.,  a  genus  of  protozoans  (zool)  — ModL.,  dimin.  of  area,  ‘chest,  box’  (see  area); so  called  from  the  boxlike  shape  of  the  shell. Arceuthobium,  n.,  a  genus  of  parasitic  plants (bot.)  —  ModL.,  compounded  of  Gk.  SpxEuffoc, ‘the  juniper',  and  [stop,  ‘life’,  so  called  from its  parasitism  on  conifers.  Gk.  apxeu&oc  is  prob. rel.  to  apxup,  ‘net’.  For  the  etymol.  of  JSio c,  see bio-.
arch,  n.,  a  curved  structure.  —  OF.  (=  F.)  arche, fr.  VL.  *arca,  fr.  L.  arcus,  ‘bow’.  See  arc. Derivative:  arch,  tr.  v.
arch
ardella
arch,  adj.,  chief,  principal.  —  See  pref.  arch-.
Derivatives:  arch-ly,  adv.,  arch-ness ,  n. arch-,  pref.  meaning  ‘chief,  principal’,  as  in  arch¬ duke ,  archbishop.  —  ME.  arche-,  fr.  OE.  arce-,
- erce ,  fr.  L.  archi-,  arch-,  fr.  Gk.  apy.-,  ap/-, which  is  rel.  to  apxop,  ‘leader,  chief,  ruler’,  from the  stem  of  ap/sw,  ‘to  begin,  rule’  (whence  al¬ so  ipyp,  ‘beginning,  first  cause,  origin,  first principle,  office’),  and  in  gradational  relation¬ ship  to  iip/aptop,  ‘leader,  chief’.  Cp.  arch,  ‘chief’, -arch.  Cp.  also  archaeo-,  archaic,  archaism, arche,  architect,  archon,  -archy.
-arch,  suff.  meaning  ‘a  ruler’,  as  in  ethnarch,  oli¬ garch.  —  See  pref.  arch-.
Archaean,  also  Archean,  pertaining  to  the  oldest geological  period.  —  Formed  with  suff.  -an  fr. Gk.  ap /aloe,  ‘ancient’,  fr.  dpyr,,  ‘beginning’.  See arch-  and  cp.  archaic.
archaeo-,  before  a  vowel  archae-;  also  archeo-, resp.  arche-,  combining  form  meaning  ‘ancient, primeval,  primitive.  —  Gk.  ap/octo-,  apyai-,  fr. ap/atop,  ‘ancient’,  lit.  ‘from  the  beginning’,  fr. ipxh,  ‘beginning’.  Sec  arch-, archaeological,  archeological,  adj.  —  Formed with  adj.  suff.  -al  fr.  Gk.  dpxatoXoyt.x6<;,  ‘per¬ taining  to  archaeology’,  fr.  dpx°uoXoyia.  See next  word.
Derivative :  archaeological-ly,  archeological-ly, adv.
archaeology,  also  archeology,  n.  —  Gk.  xp/xio- Xoyix,  ‘the  study  of  ancient  things’,  compound¬ ed  of  apyaio-  (see  archaeo-)  and  Gk.  -Xoytd,  fr. -Xdyop,  ‘one  who  speaks  (in  a  certain  manner); one  who  deals  (with  a  certain  topic)’.  See  -logy. Derivatives :  archaeological  (q.v.),  archaeolog-ist or  archeolog-ist,  n.
Archaeopteryx,  also  Archeopteryx,  n.,  a  genus  of extinct  reptilian  birds  ( paleontol .)  —  ModL., compounded  of  archaeo-  and  Gk.  -repu^,  ‘wing’. —  See  pterygo-,  ptero-.
archaic,  adj.,  old-fashioned,  antiquated,  obso¬ lete.  —  Gk.  apyxtV.op,  ‘old-fashioned,  anti¬ quated',  fr.  ApyaTo ;,  ‘ancient’,  fr.  ap yf„  ‘be¬ ginning’.  See  arch-  and  cp.  Archaean. Derivative:  archaic-al-ly,  adv. archaism,  n.,  use  of  an  obsolete  word.  —  Gk. xp/aiapto:,  fr.  izyxeZv.'i,  ‘to  be  old-fashioned, copy  the  ancients  in  language’,  fr.  ip/atop,  ‘an¬ cient’.  See  prec.  word  and  -ism. archaist,  n.,  one  fond  of  using  archaisms.  — Formed  with  suff.  -ist  fr.  Gk.  ipyalop,  ‘ancient’. See  archaic.
Derivative:  archaist-ic,  adj. archaize,  tr.  v..  to  make  archaic;  intr.  v.,  to  use archaisms.  —  Gk.  xp/xuieiv.  See  archaism  and -ize.
archangel,  n.  —  Late  L.  archangetus,  fr.  Gk. apyxyysAoc,  'chief  angel’,  fr.  ap/_-  (see  arch-) and  ayyeXop,  ‘angel’.  See  angel, archangelic,  adj.  —  Late  L.  archangelicus,  fr.  Gk. apXayyeXixop,  fr.  apyayyeXop.  See  p  c.  word and  -ic.
100
101
archbishop,  n.  —  ME.  archebischop ,  fr.  OE.  arce- biscop,  fr.  Eccles.  L.  archiepiscopus,  fr.  Eccles. Gk.  apxt£mcnco7ro?,  lit.  ‘chief  bishop’,  fr.  Gk. apyi-  (see  archi-)  and  Imaxonoc,  ‘bishop’.  See
bishop.
archbishopric,  n.  —  M  H.archehischopriche,  fr.  OE. arcebiscoprlce.  See  arch-  and  bishopric  and  cp. prec.  word.
archdeacon,  n.  — -  OE.  arcediacon ,  fr.  Eccles.  L. archidiaconus ,  fr.  Eccles.  Gk.  dpyAtdxovoc,  lit. ‘chief  deacon’,  fr.  dp yy  (see  archi-)  and  Siaxovop, ‘servant,  minister  of  a  church’.  See  deacon, arche,  n.,  the  first  principle  (Greek  philos.)  —  Gk. dpyr,,  ‘beginning,  first  cause,  origin,  first  prin¬ ciple’.  See  arch-.
Archean.  —  See  Archaean.
archegonium,  n.,  the  female  sex  organ  in  ferns and  mosses  (hot.)  —  ModL.,  fr.  Gk.  apyeyovop, ‘first  of  a  race’,  fr.  dpy-  (see  arch-)  and  -yovop, which  is  rel.  to  yovf),  ‘offspring,  race,  family, generation’,  fr.  I.-E.  base  *gen-,  ‘to  produce, beget’.  See  genus.
Archelon,  n.,  a  genus  of  extinct  turtles.  —  ModL., shortened  fr.  Gk.  dpx(wv  yJz'/M'cr),  ‘ruler  tor¬ toise’.  Gk.  apycov,  ‘ruler’,  is  pres.  part,  of  apyew, ‘to  rule’ ;  see  arch-  and  cp.  archon.  Gk.  yO.covr] is  rel.  to  yeX up,  ‘tortoise’,  lit.  ‘the  yellow  animal’, fr,  I.-E.  base  *ghel-,  ‘yellow’;  see  yellow, archenteron,  n.,  the  primitive  enteron  of  a  gas- trula  ( zool .)  —  Formed  fr.  arch-  and  Gk.  Ivxepov, ‘intestine’.  See  enteric.
archer,  n.  —  OF.  archier  (F.  archer),  fr.  L.  ar- eariits ,  fr.  arcus,  ‘bow’.  See  arc  and  subst.  suff.
-er.
archery,  n.  —  OF.  archerie,  fr.  archier ,  ‘archer’.
See  prec.  word  and  -y  (representing  OF.  -ic). archetype,  n.  —  L . archciypum, fr. Gk .  apysTU-ov, ‘pattern,  model’,  prop.  neut.  of  the  adjective dp/rmiro?,  ‘stamped  first',  used  as  a  noun,  fr. ip yz-(=  dp/t-), ‘first’,  and  tu-oc, ‘a  blow,  mark of  a  blow'.  See  arch-  and  type, archi-,  pref.  meaning  i)  ‘chief’,  as  in  archidia- conal;  2)  ‘primitive,  original’  as  in  archiplasm.  — Gk.  dp/i-,  rel.  to  dp/6;,  ‘leader,  chief,  ruler’, dpyr.v,  ‘to  begin,  to  rule’.  See  arch-, archiater,  n.,  the  chief  physician  at  the  court  of  a Greek  king  or  Roman  emperor  ( Greek  and Roman  hisr.)  —  Gk.  dp/taxpdp,  ‘court  phy¬ sician’,  fr.  dpyi-  (see  archi-)  and  iaxpd;,  ‘physi¬ cian’.  See  iatric.
archidiaconal,  adj.,  I)  of  an  archdeacon;  2)  of  an archdeaconry.  —  Compounded  of  archi-  and diaconal.
archil,  orchil,  n.,  dyestuff  obtained  from  lichen. —  ME.  orchcll,  fr.  AF.  orchel,  which  is  rel.  to earlier  F.  orsolle ,  F.  orseille ,  It.  orcella’,  of  un¬ certain  origin.  Cp.  Roccella. archimandrite,  n.,  in  the  Greek  Church,  head  of a  monastery  or  of  a  group  of  monasteries.  — ML.  archimandrita,  fr.  MGk.  dpxip.avSpt-nr)p, fr.  dpyj.-,  ‘chief’  (see  archi-),  and  (zdvSpa,  ‘fold, stable’,  which  is  prob.  cogn.  with  OI.  manduri.
‘stable’,  mandiram,  ‘room,  house,  palace, temple’.
Archimedean,  adj.,  pertaining  to  Archimedes.  — Formed  with  suff.  -an  fr.  L.  Archimedeus,  ‘of  Ar¬ chimedes’,  fr.  Gk.  ’Apxip.flSr)?,  Archimedes,  the celebrated  mathematician  (2877-212  B.C.E.). archipelago,  n.,  1)  the  Aegean  Sea;  2)  a  sea  stud¬ ded  with  many  islands;  3)  a  group  of  islands.  — It.  arcipelago,  lit.  ‘the  chief  sea’,  compounded  of arci-,  ‘chief’,  fr.  Gk.  dpyi-  (see  archi-),  and  Gk. TziXayoQ,  ‘sea’  (see  pelagic).  In  ancient  and  me¬ diaeval  Greek,  the  word  apxrneXayor  does  not occur,  in  modern  Greek  it  is  an  Italian  loanword. The  fact  that  archipelago  orig.  denoted  the  Aege¬ an  Sea  may  help  us  find  the  origin  of  this  word, which  is  a  real  crux  etymologorum.  It.  arcipelago very  probably  arose  from  a  mistaking  of  Gk. Atyaiov  TtfXayo:,  ‘the  Aegean  Sea’,  for  dpy.- TrsXayo;,  ‘the  chief  sea’,  a  confusion  suggested  by the  numerous  Greek  words  beginning  with  dpyi- . archiplasm,  n.,  1)  primitive  protoplasm;  2)  ar- choplasm. — Compounded  of  archi-  and  -plasm. Derivative:  archiplasm-ic,  adj. architect,  n.  —  F.  architecte,  fr.  L.  architectus,  fr. Gk.  ap/enberav,  ‘master  builder’,  fr.  dp/t-, ‘chief’,  and  text<ov,  ‘carpenter,  builder’,  which is  rel.  to  ttiyyT,,  ‘art,  skill,  craft’.  See  archi-  and text  and  cp.  technic,  tectonic, architectonic,  adj.  —  L.  architectonicus ,  fr.  Gk, dpXiTExxovixog,  ‘pertaining  to  a  master  builder’, fr.  dpxiTEXTtnv.  See  prec.  word  and  -ic. architectonics,  n.  —  See  prec.  word  and  -ics. architecture,  n.  —  F.,  fr.  L.  architectiira,  fr.  ar¬ chitectus.  See  architect  and  -ure.
Derivatives:  architectur-a! ,  adj.,  architectur-al- ly,  adv.
architrave,  n.,  the  lowest  part  of  the  entablature (archil.)  —  It.  architrave ,  fr.  archi-  and  trave, ‘beam’,  fr.  L.  trabem ,  acc.  of  trabs.  See  trabeate. archive,  n.,  generally  used  in  the  pi. —  F.  archives, fr.  L.  archivum,  archium,  ‘the  archives',  trans¬ literation  of  Gk.  dp/etov,  ‘official  building’,  pi. tx  dpyetx,  ‘public  records,  archives',  fr.  dp/t], ‘beginning,  origin,  first  place,  office’.  See  arch- and  cp.  arche.
Derivatives:  archive,  tr.  v.,  archiv-al,  adj., archiv-ist,  n.
archivolt,  n.,  a  curved  molding  on  the  face  of  an arch  (archil.)  —  It.  archivollo,  lit.  ‘an  arched vault’,  fr.  arco,  ‘arch’,  and  volta,  ‘vault’.  See
arch  and  vault.
archo-,  combining  form  meaning  ‘rectal’  (med.) —  Fr.  Gk.  dp/6q,  ‘rectum’,  which  is  of  un¬ certain  origin.
archon,  n..  one  of  the  nine  chief  magistrates  in Athens  ( Ancient  Greek  hist.)  —  Gk.  dpycov, ‘ruler’,  prop.  pres.  part,  of  dpyeiv,  ‘to  rule’. See  arch-  and  cp.  the  first  element  in  Archelon. -archy,  combining  form  meaning  ‘rule’,  as  in 
===== leaf 65 =====
 an¬ archy,  monarchy,  —  L.  -archia,  fr.  Gk.  -ap/id, ‘rule’,  fr.  dpx<k,  ‘leader,  chief,  ruler’.  See  -arch and  -y  (representing  Gk.  -ta).
arciform,  adj.,  having  the  form  of  an  arch.  — Compounded  of  L.  arcus,  ‘bow’,  and  forma, ‘form,  shape’.  See  arc  and  form,  n. arctic,  adj.,  pertaining  to  the  North  Pole  or  the regions  near  it.  —  L.  arcticus,  fr.  Gk.  dcpxrixoc, ‘of  a  bear;  of  the  Great  Bear;  northern’,  fr. apxToc  (also  apxop),  ‘bear’;  the  constellation of  the  Great  Bear;  the  north’,  which  is  cogn. with  OI.  fksah,  Avestic  arlsho,  Arm.  arj.  Alb. arl,  ‘bear’,  L.  ursus  (for  *urksos),  OIr.,  Gael. art,  W.  arth  (for  *arkt),  ‘bear’.  Cp.  Ursus.  Cp. also  Arctium,  arcto-,  Arcturus,  antarctic,  Arthur, Nearctic.
Arctium,  n.,  a  genus  of  plants  of  the  thistle  family, the  burdock  (bot.)  —  ModL.,  fr.  Gk.  apxT&?, ‘bear’.  See  prec.  word.
arcto-,  before  a  vowel  arct-,  combining  form meaning  ‘bear’,  or  ‘the  north’.  —  Gk.  dpxro-, tipxT-,  fr.  SpxTO?,  ‘bear;  the  north’.  See  arctic. Arctogaea,  Arctogea,  n.,  a  zoogeographical realm,  comprising  North  America,  Europe,  Asia and  Africa.  —  ModL.,  compounded  of  arcto- and  Gk.  yr),  ‘earth’.  See  geo-  and  cp.  Neogaea, Notogaea.
Derivatives:  Arctogae-al  or  Arctoge-al,  Arcto- gae-an  or  Arctoge-an,  Arctogae-ic  or  Arcloge- ic,  adjs.
Arctostaphylos,  n.,  a  genus  of  plants  of  the  heath family,  the  bear  berry  (bot.)  —  ModL.,  com¬ pounded  of  Gk.  apxTop,  ‘bear’  and  OTxpuXy), ‘bunch  of  grapes’.  See  arctic  and  staphylo-. Arcturus,  n.,  the  brightest  star  in  the  constella¬ tion  Bootes  ( astron .)  —  L.,  fr.  Gk.  ’Apxro'jpoc;, lit.  ‘the  Bearguard’,  fr.  dpxxop,  ‘bear’  and  oOpop, ‘watcher,  guard,  ward’.  See  arctic  and  ware, ‘alert’.
arcuate,  arcuated,  adj..  bent  like  a  bow.  —  L, arcuatus,  pp.  of  arcudre,  ‘to  bend  like  a  bow’, fr.  arcus,  ‘bow’.  See  arc.
Derivative:  arcuate-Iy,  adv. arcuation,  n.  L.  arcudtio,  gen.  -dnis,  fr.  arcuatus pp.  of  arcudre.  See  prec.  word  and  -ion. arculite,  n.,  a  bow-shaped  crystallite  (mineral.)  — Compounded  of  L.  arcus,  ‘bow’  (see  arc),  and combining  form  -life.
-ard,  -art,  suff.  It  orig.  had  an  intensive  force; now  it  is  often  used  in  a  pejorative  sense.  — OF.,  fr.  OHG.  -hart,  which  is  rel.  to  OHG.  har- ti,  ‘hard’.  See  hard.  For  the  force  of  this  suff. cp.  coward,  dastard,  dotard,  drunkard,  sluggard. Ardea,  n.,  a  genus  of  herons  (ornithol.)  —  L.  ar- dea,  ‘heron’,  cogn.  with  Gk.  epcoSiop,  ‘heron’, Serb.,  Croat,  roda  ‘stork’,  ON.  aria,  OSwed. drta,  ‘creek  duck’.  Cp.  Erodium. ardeb.  n..  a  measure  of  capacity  used  in  Egypt.  — Arab,  irdabb,  in  vulgar  pronunciation  arddbb, ardebb,  fr.  Gk.  apriSr,,  name  of  a  Persian measure.  See  artaba.
ardella,  n.,  any  of  the  small  apothecia  of  some lichens  (bot.)  —  ModL.,  fr.  Gk.  dpSeiv,  to  wa¬ ter,  pour  forth’,  a  word  of  unknown  etymology. Cp.  Arethusa.
argue
ardency
ardency,  n.  —  Formed  fr.  next  word  with  suff.  -cy.
ardent,  adj.  —  ME.  ardaunt ,  fr.  OF.  ardant  (F.  ar¬ dent),  fr.  L.  ardentem,  acc.  of  ardens,  pres.  part, of  ardere,  ‘to  burn’,  which  stands  for  *aridere, fr.  dridus ,  ‘parched,  dry’,  and  is  rel.  to  dr  ere, ‘to  be  dry’,  fr.  *  else  re,  fr.  I.-E.  base  *&s-,  ‘to burn,  glow’,  whence  also  OI.  dsn h ,  ashes,  dust , Toch.  A  asar,  ‘dry’,  Arm.  azazem,  ‘I  dry  up’, aciurt,  ‘ashes’,  Gk.  a£etv  (for  *azd‘ein),  ‘to  dry up,  parch’,  a^oc,  ‘dryness;  dirt,  mold  ,  a^aksop, ‘dry,  parched’,  Czech  ozd,  ‘malt  drier  ,  ozditi , ‘to  dry  (malt)’,  Goth,  azgd,  OE.  asce,  xsce, ‘ashes’.  See  ash,  ‘powdery  substance’,  and  cp. ara,  ardor,  area,  arid,  arson,  asbolite,  Azalea. Cp.  also  the  second  element  in  aguardiente. Derivatives:  ardent-ly,  adv.,  ardent-ness,  n. ardennite,  n.,  a  vanadosilicate  of  aluminum  and manganese  ( mineral. )  —  Named  after  Ardennes in  Belgium.  For  the  ending  see  subst.  suff.  -ite. ardhanari,  n.,  a  form  of  Siva  in  which  he  is  rep¬ resented  as  half  male  and  half  female  ( Hindu mythol.)  —  OI.  ardha-nan-,  ‘half  woman’,  fr. cirdhah-,  ‘half,  part,  side’,  and  nari-,  ‘woman’. Ol.ardhah-k  rel.  to  OI.  rdhak, ‘especially’,  Aves- tic  ar'da-,  ‘side’,  OI.  fti,  ‘besides,  except’,  fr. I.-E.  base  *er-,  *(e)re-,  ‘loose;  to  split,  separate, be  rare’,  whence  also  L.  rdrus ,  ‘thin,  loose  ,  see rare,  ‘thin’.  OT.  nari -,  ‘woman  ,  prop,  means ‘pertaining  to  a  man’,  and  is  rel.  to  OI.  ndram (acc.),  ‘man’,  and  cogn.  with  Gk.  dvfjp,  ‘man’; see  andro-.
arditi,  n.  pi.,  Italian  volunteers  serving  in  storm troops  in  World  War  I.  —  It.,  pi.  of  ardito, ‘brave,  audacious’,  fr.  F.  hard/,  prop.  pp.  of  OF. *hardir,  ‘to  render  courageous’,  lit.  ‘to  make hard’,  fr.  Frankish  *hardjan,  fr.  *hart,  ‘hard’, which  is  rel.  to  OHG.  harti.  OE.  heard,  ‘hard’. See  hard.
ardor,  ardour,  n.  —  ME.  urdeur,  fr.  OF.  ardour (F.  ardeitr ),  fr.  L.  ardorem,  acc.  of  ardor,  ‘heat’, fr.  ardere,  ‘to  burn'.  See  ardent  and  -or. arduinite,  n.,  a  zeolite  (mineral.)  —  Named  after the  Venetian  geologist  Giovanni  Arduino.  For the  ending  see  subst.  suff.  -ite. arduous,  adj.  —  L.  arduus,  ‘high,  lofty,  steep  ,  fr. I.-E.  base  *eredh-,  * erdh -,  'to  grow;  high’, whence  also  Avestic  er*dva-,  'high',  Olr.  ard, ‘high’,  Alb.  rit,  OSlav.  rastp,  ‘I  grow’.  Cp.  I.-E. base  *weredh-,  ‘to  grow;  high’,  whence  OI. urdhvah,  ‘high’,  vardhate,  ‘causes  to  grow,  in¬ creases',  Gk.  updo c  (for  *"opd56p;  cp.  Dor. jjopdo-),  ‘straight,  right,  erect’.  See  ortho-  and cp.  vriddhi.  For  E.  -ous,  as  equivalent  to  L.  -us, see  -ous.
Derivatives:  arduous-ly,  adv.,  arduous-ness,  n. are,  v.,  pres.  pi.  indicative  of  he.  —  ME.  aren, later  are,  fr.  OE.  (Northumbrian)  aron.  rel.  to ON.  eru,  ‘(they)  are’,  for  I.-E.  *es-en,  whence also  Dor.  svxt,  Att.  elcri,  OI.  santi,  L.  sunt, Umbr.  sent ,  Goth.,  OE,  sind.  All  these  words are  derivatives  of  I.-E.  base  *es-,  ‘to  be’.  See esse  and  cp.  am,  art,  is.
102
are,  n.,  a  square  unit.  —  F.,  formed  in  1795  by  a decree  of  the  French  National  Convention,  fr.
L.  area,  ‘vacant  piece  of  ground’.  See  next  word and  cp.  the  second  element  in  hectare, area,  n.  —  L.,  ‘vacant  piece  of  ground,  building, plot’,  rel.  to  arere,  ‘to  become  dry’,  hence  area orig.  meant  ‘a  place  burned  down,  a  dry,  bare  pla¬ ce’  ;  see  ardent  and  cp.  areola,  debonair.  For  sense development  cp.  G.  Esse,  ‘chimney,  forge , which  also  derives  fr.  I.-E.  base  *&s-,  ‘to  burn’. Areca,n.,  a  genus  of  palms  of  Asia  and  the  Malay Archipelago  ( hot .)  —  ModL.,  fr.  Port,  areca,  fr. Malayalam  ddakka ,  fr.  Tamil  adaikdy,  lit. ‘having  close  clusters  of  nuts’,  fr.  ddai,  close arrangement  of  the  cluster’,  and  kay,  ‘nut’.  See OED.  and  Yule-Burnell,  Hobson-Jobson,  p.35. Arecaceae,  n.  pi.,  a  family  of  plants,  the  palm family  (bot.)  —  ModL.,  formed  fr.  prec.  word with  suff.  -aceae.
arecaceous,  adj.  —  See  prec.  word  and  -aceous. arena,  n.  —  L.  harena,  arena,  ‘sand,  sandy  place, seashore;  place  of  combat  (lit.  ‘place  strewn with  sand’),  prob.  of  Etruscan  origin.  Cp.
Arenaria.
arenaceous,  adj.,  sandy.  —  L.  arenaceus,  sandy  .
See  prec.  word  and  -aceous.
Arenaria,  n.,  a  genus  of  herbs  of  the  chickweed family ;  the  sandwort  (bot.)  —  ModL.,  lit.  ‘the sandwort’,  fr.  Late  L.  harenarius,  arendrius,  ‘of sand’,  fr.  L.  harena,  arena  (see  arena) ;  so  called because  many  representatives  of  this  species grow  in  the  sand.
arend,  n.,  bearded  vulture  (S.  Afr.)  —  Du., 'eagle’,  fr.  MDu.  arent,  rel.  to  ON.  dm,  OE. earn,  OHG.  aro,  ‘eagle’.  See  em(e). areo-  combining  form  meaning  ‘of,  or  pertaining to.  Ares  or  Mars’,  used  in  astronomy.  —  Fr. Gk.  ”Apeo?  or  ’'Apcco;,  gen.  of"Apr]<;,  ‘Ares’. See  Ares  and  cp.  Areopagite. areola,  n.,  a  small  area;  esp.  the  pigmented  ring surrounding  the  nipple  ( anat .)  —  L.  areola, ‘small  area’,  dimin.  of  area,  ‘a  vacant  piece  of ground’  (see  area) ;  introduced  into  anatomy  by the  Swiss  anatomist  and  botanist  Caspar  Bauhin (1560-1624)  in  1605.
Derivatives:  areol-ar,  areol-ate,  areol-at-ed, adjs.,  areol-ation,  n.
areole,  n.,  a  small  space  (bot.)  —  F.  areole,  fr.  L. areola.  See  areola.
areolet,  n.,  a  small  areola  (zool.)  —  A  dimin.  of areola,  hence  a  double  dimin.  of  area.  For  the ending  see  suff.  -et.
areology,  n.,  the  study  of  the  planet  Mars. Compounded  of  areo-  and  Gk.  -koyla,  fr. -koyos,  ‘one  who  speaks  (in  a  certain  manner) ; one  who  deals  (with  a  certain  topic)’.  See  -logy. Derivatives:  areolog-ic,  areolog-ic-al,  adjs.,  are- olog-ic-al-ly,  adv.
areometer,  n.,  a  hydrometer.  —  Compounded  of Gk.  ipauk,  ‘thin,  rare’,  and  ptfrpov,  ‘meas¬ ure’.  The  first  element  is  of  uncertain  origin; it  originally  began  with  digamma  (f  =  tv).
103
hence  cannot  be  cognate  with  L.  rdrus,  ‘thin, rare’  (see  rare,  ‘thin’).  For  the  second  element see  meter,  ‘poetical  rhythm’.
Derivatives:  areometr-ic,  areometr-ic-al.  adjs., areometr-y,  n.
Areopagite,  n.,  member  of  the  Areopagus.  —  Gk.
’  Ap£to7raYf'r/]?,  fr.  'A  peidroxyo^.  See  next  word. Areopagus,  n.,  name  of  a  hill  west  of  the  Acro¬ polis  in  Athens  and  of  the  tribunal  situated  on it.  —  L.,  fr.  Gk.  ’Apet6naYoi;,  for  ”ApEio? toxyoi;,  ‘hill  of  Ares  (=  Mars)’,  resp.  r\  Book))
))  iE,  ’Apetou  jtdyou,  ‘the  council  of  the  hill  of Ares*.  See  next  word.  For  the  etymol.  of  TOxyos, ‘rocky  hill’,  see  pact.
Ares,  n.,  the  Greek  god  of  war,  identified  by  the Romans  with  Mars  ( Greek  mythol .)  —  L.,  fr. Gk.  "Apr,?  (gen.  "ApEo;  or  "ApEcoc),  lit.  ‘injurer, destroyer’,  fr.  depyj,  ‘banc,  ruin’,  which  is  rel. to  xpEiv),  ‘a  cursing,  menacing’,  and  prob. cogn.  with  OI.  irasyd,  ‘ill  will’,  irasyati,  ‘bears ill  will’,  Arm.  her,  ‘anger,  envy’,  OE.  eorre,  yrre, ‘angry’.  Cp.  areo-,  Areopagus,  An  tares, arete,  n.,  virtue  ( Greek  philos.)  —  Gk.  apE-rfj, ‘virtue’,  prop,  ‘that  which  is  good’,  rel.  to apeUav,  ‘better’,  dpiarop,  ‘best’  (whence  apur- Toy.pa-ria,  ‘the  rule  of  the  best’),  apecntEiv,  ‘to make  good,  conciliate’.  See  aristo-. arete,  n.,  sharp  crest  of  a  mountain.  —  F.,  ‘fish¬ bone;  ridge’,  fr.  L.  arista,  ‘ear  of  grain’,  which is  prob.  of  Etruscan  origin.  Cp.  arista,  Aristida, arris.
Arethusa,  n.,  nymph  of  a  fountain  near  Syracuse ( Greek  mythol.)  —  L.,  fr.  Gk.  ’Ap6Uouera,  a  col¬ lateral  form  of  dpSooaa,  ‘waterer’,  fern,  pres, part,  of  SpSeiv,  ‘to  water’.  See  ardefla.
Arethusa,  n.,  a  genus  of  orchids  (bot.)  —  ModL., named  after  the  nymph  Arethusa.  See  prec.  word, arfvedsonite,  n.,  a  basic  metasilicate  (mineral.)  — Named  after  the  Swedish  chemist  Johan  August Arfvedson  (1792-1841).  For  the  ending  see  subst. suff.  -ite.
argala,  n.,  the  adjutant  bird.  —  Hind,  hargita. argali,  n.,  a  large  wild  sheep  of
```


## [2026-09-04T23:09:15.956Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in (74,75,76,77):\n    print('===== POK_01 leaf',i,'=====')\n    print(leaves[i][:2500])\nEOF",
 "description": "Print Pokorny page 68 area"
}
```


### [2026-09-04T23:09:18.093Z] TOOL RESULT

```
364
===== POK_01 leaf 74 =====
Arm.  argel  ^Hindernis',  denomin.  argelum  , wehre,  halte  ab,  halte  zurück^; vielleicht  mit  o- Abtönung  orm  ,Mauer^  (*ork-mo-?)]  i
gv.  do-aso)  , wehre,  halte  vor,  schütze,  helfe;  halte  vor,  reiche  aus,  genüge'! (dQyJffü),  }]Qy.S(Ta)  wohl  aus  *dQX£Uo;  äo-/,og  n.  jSchutz^  (Alkman);  Hgynogl ,ausreichend',  avT-dgycrj:;  ,sich  selbst  genügend',  ftoö-dQX7]g  ,mit  den  Füßen  j ausreichend,  schnell'  (s.  auch  Bechtel  Lexil.  279 f.);
lat.  arceö,  -ere  ,verschließen,  einhegen;    durch  Abschluß   fernhalten,  ab- 1 wehren,    verhindern',    ai^ca    ,Kasten,    Kiste,     Lade,     Geldschrank;    Sar, (eigentlich  , Verschluß',  vgl.  arcänus  ,unter  Vecschluß,  geheim^;    aus  dem| Lat.    stammt   got.    usw.    arka   , Kasten,   Geldkasten,  Arche^,    ahd.   arahlia^ archa  , Arche'  und  aus  dem   Germ,   wieder   aksl.    o^aka  , Grabhöhle',   apr. arkan  Akk.  Sg.  , Arche'),  arx  , feste  Höhe,  Burg',  arcera  , bedeckter  Wagen'  ; (Suffix  nach  cumera,  vgl.  WH.  I  63)  osk.  trnbarakavüm  ,aedificare^  (setzt  3 ein  *trehark-  ,ein  Haus  einhegen'  voraus);
ahd.  rigil,  mhd.  rigel  , Riegel',  mengl.  rail  (ags.  *reogol),  Güntert  '^ Kalypso  136;
lit.  räktas  , Schlüssel',  rakmti  , schließen';
hett.  har(k)-  ,halten,  haben',  Götze  und  Pedersen  Mursili  50.
Durch  die  Bed.  wenig  empfohlen  wird  Heranziehung  von  cymr.  arclien  t , Kleidung,  Schuh',  bret.  arc'henna  , Schuhe  anziehen'  (mir.  acrann  , Schuh, Kleidung^  wohl  aus  arc-  umgestellt,  Stokes  KZ.  41,  381).
Über  den  von  W.  Foy  KZ.  35,  62  als  , Burgberg'  gedeuteten  apers. Bergnamen  arkadri-  s.  Justi  lA.  17,  106  (angeblich  {H)ara-kadris  ,Berg- schlucht'),  aber  dazu  wieder  Bartholomae  Z.  altiran.  Wb.  105  Anm.  1,  116.
Gegen  Anreihung  von  slav.  racit'i  , wollen,  gönnen'  (Brückner  KZ.  45,  108 Anm.)  spricht  die  Bed.
Als   Form    mit    o-Abtönung    (oder  allenfalls  mit  or  =  r)  gilt  lat.  Orcus ,Unterweltsgott;  Unterwelt,  Totenreich'  (»Yerschließer'?  unsicher). Ähnlich  aUc[-  , abwehren,  schützen'  und  areg-  (s.  d.). WP.  I  80  f.,  WH.  62  f.,  848.
arenko-  Getreideart?
Lat.  arinca  ,Getreideart,  olyra'  (,Galliarum  propria'  Plin.  n.  h.  18,  81; fremdes,  vermutlich  gall.  Wort,  trotz  Niedermann  g  und  i  30  nicht  echt lat.),  gr.  ^Qay.og  , Hülsenfrucht,  die  unter  den  Linsen  als  Unkraut  wächst', ägav^Oi'  oanqiöv  tl.  %d  dk
===== POK_01 leaf 75 =====
er    Herkunft^   s.  Boisacq  84)^   mir.    arhar   ^Getreide^    (s.  *ar- 'pflügenO;  «^^^  ,Brot^ WP.  I  H  WH.  I  67.
Brio-'^  »Herr,  Gebieter^
Ai.  ar{i)yd-  ,Herr,  gastlich^,  är(i)ya-,  Arier,  äryaka  , ehrwürdiger  Mann^; ;vv.  airyö,  apers.  ariya-  ,arisch^;  gall.  PN.  Ario-mänus  (CIL,  III  4594); ii«.  aire  (gl.  primas)  neben  airech,  wo  *arjo-  und  *a7'jäko-  anzusetzen  ist, welches  sich  zu  ai.  äryaka  verhält  wie  gr.  [.leioa^  , Jüngling^  zu  ai.  Tna?^- jakci-  ,Männchen^  (Pedersen  Kelt.  Gr.  II  100).  Dagegen  gehört  mir.  ruire nicht  hierher,  sondern  aus  ro  +  rl  ,Großkönig^
Über  ai-  aryamdn  n.  , Gastlichkeit^,  m.  ,Gastfreund^,  av.  airyaonan-, npers.  ermän  ,Gast^,  s.  oben  unter  1.  al-.
Sollte  W.  Krause  (Runeninschriften  539)  richtig  urnord.  arjösteR  N.  PI. die  Vornehmsten^  lesen,  so  müßte  allerdings  ein  urnord.  ^ai-jaR  ,vornehm^ und  ein  idg.  "^ario-  angesetzt  werden,  das  im  Ai.  lautlich  mit  einer  Ab- leitung von  ari-  ,Fremder*^  zusammengefallen  wäre.  Kelto-germ.  PN  Äino- vistus  beweist  allerdings  nichts,  da  Ärio-  für  ^Hario-  stehen  könnte.  Auch air.  aire,  aireck  , Freier^  sind  zweideutig,  s.  oben  unter  1.  al-,
WP.  I  80.
arqu-  ,Gebogenes^
Lat.  arcuSj  -üs  (Stamm  lautet  auf  -qu-  aus,  vgl.  alat.  Gen.  arqui,  ferner arqiies,  arquitenens)  ,Bogen^,  arquätus^  arcuätus  (morbus)  ,gelbsüchtig, Gelbsucht^,  wohl  eig.  ,regenbogenfarbig,  grün  und  gelb  aussehend^  (vgl. Thes.);  arcuätus  auch  ,bogenförmig^;  umbr.  arclataf  ,arculatas^,  wozu V.  Planta  I  341,  Götze  IF.  41,  91  (*arkelo-  mit  Verlust  der  Labialisation); got.  arhazna  f.  ,Pfeil^  (ar\va-zna,  vgl.  hlaiicazna),  altn.  gr  (Gen.  orvar) f.  ,Pfeil^,  ags.  earh  f.  ds.  (engl,  arrow),  germ.  *arhvö.
Für  den  Ansatz  arqu-  (und  nicht  arqu-)  würde  sprechen  russ.  rakita,  cech. rokyta,  serb.  rokita  usw.  ,Haarweide^,  wo  "^arqüta  (Miklosich  EWb.  226, Torbjörnsson  BB.  20,  140)  zugrunde  liegt,  und  gr.  IcQv.evd-og  ,Wacholder^, welches  Wort  mit  Liden  IF.  18,  507  mit  aller  Wahrscheinlichkeit  hierzu zu  ziehen  ist;  dazu  äoy.svd-ig  ,Wacholderbeere^  Allerdings 
===== POK_01 leaf 76 =====
 nimmt  Liden Verwandtschaft  mit  gr.  äoy,vg  ,Netz^  (s.  Bezzenberger  BB.  21,  285)  an,  wo- zu man  unter  1.  ar-,  S.  61  vergleiche.
Eine  andere  Verbindung  für  gr.  IjcgT-evS-og  und  russ.  rakita  usw.  sucht Endzelin  KZ.  44,  59 ff.,  der  richtiger  lett.  ercis,  ecis  (^ercis)  , Wacholder' vergleicht;  ferner  erceties  ,sich  quälen,  grämen,  streiten',  ercesa  ,eine sehr  zänkische  Person';  lett.  erk§{k')is  ,Dornstrauch^  wäre  nach  Endzelin Mischung  von  "^erkts  und   einer   dem  lit.  ersketis  , Dornpflanze'  wurzelhaft
5*
I 68  '  I
entsprechenden   Form;   gr.  äg-  müßte   dann   Schwundstufe   von   *er-  ent halten.     S.  unter  erk-,
WP.  I  81,  WH.  I  64,  EM.  69.
aröd-,  arsd-  ,ein  WasservogeF.
Gr.  QCüÖLog,  igcüÖLÖg  ,Reiher^  (igwÖLÖg  volksetym.  im  Ausgang  nach  -tdiog), lat.  ardea  ds.  (*ardd-),  anord.  arta^  aschwed.  ärta  , Kriekente',  Demin. anord.  ertla,  norw.  erle  , Bachstelze',  serb.  röda  , Storch'  (*rdda).
WP.  I  146  f.,  WH.  I  64.
aro-m  , Schilfrohr'?
Gr.  ^Qov  n.  ,Natterwurz,  Art  Schilfrohr',  ägl-aagov  ,eine  kleine  Art  davon'j
lat.  harundö  ,Rohr';  zur  Bildung  vgl.  liirundö  und  nebrundines  :  ve^goi.
Das  von  Persson  De  orig.  gerundii  59  angereihte   lat.    arista  ,Hachel,
Granne   an    der  Ähre',    aristis  ,holcus'  unterliegt  wegen  seines  zu  genista
u.  dgl.  stimmenden   Suffixes  stark  dem  Verdachte,    etruskisch  zu  sein  (s.'|
Herbig  IF.  37,  171,  178).
Aus  einer  Mittelmeersprache? WP.  I  79,  WH.  I  635  f.
aruä  ,Darm'?  V
Gr.    dgva    f.   ,Darm',    lat.   arvina   f.  , Schmer,    Fett,    Speck',    ursprüngl."
, Darmfett'?  (vgl.  ahd.  mitta-garni  ,das  in  der  Mitte  der  Gedärme  liegende
Fett');  dgßlvvT]'  xgeag.  ^lycslol  Hes.  ist  lat.  Lw.  ^
WP.  I  182,  II  353,  WH.  I  71.  '^
Us-,  davon  azd-,  azg{h)-  ,brennen,  glühen'.
Ai.  äsa-h  , Asche,  Staub'  (über  dsita-h  , schwarz'  s.  *nsi-  ,schmutzfarben'); lat.  ära  , Altar'  (=  osk.  aasai  ,in  ära',  umbr.  are  ,arae'  usw.),  äreö,  -ere ,bin  trocken,  ausgedörrt',  äridus  ,trocken'  (davon  ardeö  , brenne',  Partiz. Pass.  assus  , trocken  gebraten'),  ärea  , freier  Platz,  Tenne  usw.'  (eigentl. , ausgebrannte,  trockene  Stelle');  ahd.  essa  f.,  nhd.  Esse  (*asiön)^  urnord. aRinaj  aisl.  arinn  ,Erhöhung,  Feuerstätte',  ahd.  erin  ,Diele,  Boden'  {*azena)] toch.  AB  as-  Präs.,  äs-  Perf.  und  Kausat.  , austr
===== POK_01 leaf 77 =====
rig,  leuchtend,  edel'  (*äs-no-).  Über  gr. ÖLipdci},  TtsLvdo)  s.  Schwyzer  Gr.  Gr.  1,  724.
Da  das  r  in  hett.  a-a-ri  (äri)  ,wird  heiß'  nicht  zum  Stamm  gehört, ist  lat.  äreö  nicht  von  ära  zu  trennen.
69
Forinaiitische  Erweiterungen:
azd'  in  ^^-  ^'^^  (*az-d-iö)  ^ dorre,  trockne^,  ^'^a  f.  ,trockner  Schmutz^, A^aXioQ  dürr;  entflammend^,  äööavov  ^rjoov.  Aä-Awvag  Hes.  {-öö  aus  -zd-)] '•ecli    apoln.  ozd  ^Malzdarre^,  cech.  slov.  ozditi  ,Malz  dörrend
azo'-  arm.  ac'iun  ^Asclie^  (Meillet  Esquisse  29),  gr.  ^aßoXog  {*Uay-ßoloq) Ruß*  (  Aschen-wurf  j;  germ.  '^askö7i  in  aisl.  aska^  ags.  asce,  cESce,  ahd.  asca, 11  hd.  xl5c7ie.
az<^h-?  in  arm.  azazim  ,dörre^  (Meillet  Esquisse  33,  EM.  70),  got.  azgo Asche^  (*azgön).  Über  das  schwierige  Verhältnis  von  germ.  *askön  :  *az- ftön  s.  Feist  72  b;  wieder  anders  Specht  Dekl.  201,  219.  Auch  ist  die Beweiskraft  der  arm.  Beispiele  nicht  ganz  einwandfrei.
WH.  I  61,  65,  818,  Feist  72,  Trautmann  22,  Pedersen  Hittitisch  27,  164.
ast{by  ,Knochen^,  s.  ost{h)-.
at'  »gehen,   Jahr^
Ai.  dtati  ,geht,  wanderte  Hierzu  lat.  annus , Jahr' aus  *atnos  =  got.  Dat.  PL itpnam  ,Jahr^  Vgl.  Fick  I^  338,  W.  Meyer  KZ.  28,  164,  Froehde  BB.  16, 196  f.  (Bedeutungsentwicklung  wie  hei  germ.  '^jeram  ,Jahr^  zu  ie-  ,gehen'').
Osk.-umhr.  entspricht  akno-  ,Jahr,  Festzeit,  Opferzeit'  (mit  -tn-  zu  -kn-, Brugmann  IF.  17,  492).  Erhalten  ist  das  "Wort  in  den  Kompositis  lat. perennis  ,das  ganze  Jahr  dauernd;  beständig',  sollennis  , alljährlich  wieder- kehrend oder  gefeiert,  feierlich;  üblich'  (Nebenform  sollemnis  sicherlich analogisch  entstanden;  Thurneysen  AflL.  13,  23 ff.,  nach  omnis?)]  umbr. sev-acni-,  'per-acni-  , sollennis',  Subst.  ,hostia'.
WP.  I  42  f.,  WH.  I  öl,  847.
ät{e)r-  ,Feuer'.
Av.  ätars  (Gen.  ädrö)  m.  , Feuer',  wozu  ai.  dtharvan-  ,Feuerpriester', Lw.  aus  av.  ad-aurvan-,  ad-aurun  (das  ^  aus  äd-rö)  ds.;
arm.  airem  ,verbrenne,  zünde  an'  (auf  Grund  von  *azV  aus  *äter)]  serb. vätra  , Feuer',  klr.  vdtra  , Feuer,  Herd',  poln.  vatra  , Strohasche'  sind  nach Jokl  WZKM.  34,  37  ff.  aus  rum.  vaträ  ,Herd'  entlehnt,  dies  wieder  aus dem  Alb.  {^Qg.  votre^  voter  mit  v-Vorschlag  vor  alb.  ot-  aus  *ä^-,  viell. iran.  Lw.).  Vielleicht  als  , verbrannt'  auch  lat.  ätey-  , schwarz,  dunkel'  == umb
```


## [2026-09-04T23:09:34.032Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E '.{0,80}as-\\.\\s*To burn.{0,900}' AHD_watkins1985.txt | head -5; echo '--- search ash/area/arson index'; grep -n -o -E '.{0,60}(ARSON|HECTARE|AREA|ASH[^A-Za-z]).{0,80}' AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins for as- root"
}
```


### [2026-09-04T23:09:39.680Z] TOOL RESULT

```
ugrep: error: error at position 201
][\x80-\xbf]*){0,900}
                     \___exceeds complexity limits


--- search ash/area/arson index
ugrep: error: error at position 407
80-\xbf][\x80-\xbf]*){0,80}
                           \___exceeds complexity limits
```


## [2026-09-04T23:09:44.061Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'as-\\.\\s*To burn', t):\n    print(repr(t[m.start()-300:m.start()+1200]))\n    print('#####')\nEOF",
 "description": "Find AHD as- root entry"
}
```


### [2026-09-04T23:09:45.975Z] TOOL RESULT

```
'ow: ARROW. 2. Latin arcus, bow: ARC, ARCADE, ARCH!, ARCHER; ARBALEST, ARCHI- VOLT, (ARCIFORM), ARCUATE. [Pok. arqu- 67.]\naryo-. Lord, ruler; self-designation of the Indo-Iranians and perhaps of the Indo-Europeans. Lengthened-grade form *dryo- in Sanskrit drya-, noble, Aryan: ARYAN. [Pok. arjo- 67.]\nas-. To burn, glow. 1. Extended form *asg- in Germanic\nasinus\n*askon- in Old English zsce, asce, ash: ASH!. 2. Suffixed form *ds-d- in Latin Gra, altar, hearth: Ara. 3. Suffixed (stative) form *ds-é- in: a. Latin Grére, to be dry, hence dridus, dry, parched: ARID; b. Latin ardére, to burn, be on fire, from dridus, parched: ARDENT, ARDOR, ARSON. 4. Extended form *asd- in: a. Greek azein, to dry: ZAMIA; b. Greek azaleos, dry: AZALEA. [Pok. as- 68.]\n[asinus. Ass. Latin noun, akin to Greek onos, probably ultimately from the same source as Sumerian anée. 1. Latin asinus, ass: ASININE, EASEL. 2. Greek onos, ass: ONAGER.]\nat-. To go; with Germanic and Latin derivatives meaning a year (conceived as “the period gone through, the revolving year”). Suffixed form *at-no- in Latin annus, year: ANNALS, ANNUAL, ANNUITY; ANNIVERSARY, BIEN- NIUM, DECENNIUM, MILLENNIUM, OCTENNIAL, PEREN- NIAL, QUADRENNIUM, QUINDECENNIAL, QUINQUENNIUM, SEPTENNIAL, SEXENNIAL, SUPERANNUATED, TRIENNIUM, VICENNIAL. [Pok. at- 69.]\nater-. Fire. 1. Suffixed zero-grade form *dér-o- in Latin ater (feminine dtra), black (< “blackened by fire’): ATRABILIOUS. 2. Suffixed zero-grade form *dér-yo- in Latin dtrium, forecourt, hall,'
#####
```


## [2026-09-04T23:10:07.209Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'ARCHITECT',r'ARCHIVE',r'arkhein',r'archein',r'ARCHAE',r'ARCHAIC',r'tek[sþ]?-\\.\\s',r'HECTARE',r'AREA']:\n    print('#####',pat)\n    for m in list(re.finditer(pat,t))[:4]:\n        print(repr(t[max(0,m.start()-350):m.start()+250]))\nEOF",
 "description": "Search Watkins for architect/archive/tek"
}
```


### [2026-09-04T23:10:09.846Z] TOOL RESULT

```
##### ARCHITECT
'threads are tied): TILLER?, ToiL2; b. Latin subtilis, thin, fine, precise, subtle (< *sub-téla, “thread passing under the warp,” the finest thread; sub, under; see upo): SUBTLE. 3. Suffixed form *teks-On, weaver, maker of wattle for house walls, builder (possibly contaminated with *teks-tdr, builder), in Greek tekton, carpenter, builder: TECTONIC; ARCHITECT. 4. Suf- fixed form *teks-nd-, craft (of weaving or fabricating), in Greek tekhné, art, craft, skill: TECHNICAL, POLYTECHNIC, TECHNOLOGY. 5. Possibly Germanic *thahsu-, badger (“the animal that builds,” referring to its burrowing skill), in'
' akwa- AQUANAUT nau-2 AQUARELLE akwa- AQUARIUM akwa- AQUATIC akwa- AQUI- akw3-\nARA as-\nARABLE are- ARBALEST arku- ARC arku- ARCADE = arku- ARCANE arek- ARCH! = arku- -ARCH arkhein ARCHAEO- arkhein ARCHAEOPTERYX pet- ARCHAIC arkhein ARCHANGEL angelos ARCHEGONIUM gene= ARCHER arku- ARCHETYPE (s)teu- ARCHI- arkhein ARCHIMAGE magh-! ARCHIPELAGO piak-1 ARCHITECT teks- ARCHITRAVE treb- ARCHIVES arkhein ARCHIVOLT arku-\nARCHON arkhein -ARCHY arkhein ARCIFORM = arku- ARCTIC rtko- ARCTURUS rtko-, wer-4 ARCUATE = arku- ARDENT as- ARDOR as- ARDUOUS erad- ARE! er-1 ARGAL? reg-! ARGENT arg- ARGENTINE arg- A'
##### ARCHIVE
'brilliance, clarity, in Latin denominative arguere, to make clear, demonstrate: ARGUE. 6. Suffixed form *arg- ro- in Greek argos (< *argros), white (see pel-2). [Pok. ar(e)g- 64.]\n[arkhein. To begin, rule, command. Greek verb of un- known origin; with derivatives arkhé, rule, beginning, and arkhos, ruler. (ARCH-), -ARCH, ARCHAEO-, ARCHAIC, ARCHI-, ARCHIVES, ARCHON, (-ARCHY); AUTARCHY, EXARCH, MENARCHE.]\narku-. Bow and arrow (uncertain which, perhaps both as a unit). 1. Germanic *arhwo in Old English ar(e)we, earh, and Old Norse *arw-, arrow: ARROW. 2. Latin arcus, bow: ARC, ARCADE, ARCH!, ARCH'
'kwa- AQUARIUM akwa- AQUATIC akwa- AQUI- akw3-\nARA as-\nARABLE are- ARBALEST arku- ARC arku- ARCADE = arku- ARCANE arek- ARCH! = arku- -ARCH arkhein ARCHAEO- arkhein ARCHAEOPTERYX pet- ARCHAIC arkhein ARCHANGEL angelos ARCHEGONIUM gene= ARCHER arku- ARCHETYPE (s)teu- ARCHI- arkhein ARCHIMAGE magh-! ARCHIPELAGO piak-1 ARCHITECT teks- ARCHITRAVE treb- ARCHIVES arkhein ARCHIVOLT arku-\nARCHON arkhein -ARCHY arkhein ARCIFORM = arku- ARCTIC rtko- ARCTURUS rtko-, wer-4 ARCUATE = arku- ARDENT as- ARDOR as- ARDUOUS erad- ARE! er-1 ARGAL? reg-! ARGENT arg- ARGENTINE arg- ARGIL arg- ARGININE arg- ARGON wer'
##### arkhein
'arg- u-ro- in Greek arguros, silver: LITHARGE, PYRARGYRITE. 4. Suffixed form *arg-i-n- in Greek arginoeis, brilliant, bright-shining: ARGININE. 5. Extended form “argu-, brilliance, clarity, in Latin denominative arguere, to make clear, demonstrate: ARGUE. 6. Suffixed form *arg- ro- in Greek argos (< *argros), white (see pel-2). [Pok. ar(e)g- 64.]\n[arkhein. To begin, rule, command. Greek verb of un- known origin; with derivatives arkhé, rule, beginning, and arkhos, ruler. (ARCH-), -ARCH, ARCHAEO-, ARCHAIC, ARCHI-, ARCHIVES, ARCHON, (-ARCHY); AUTARCHY, EXARCH, MENARCHE.]\narku-. Bow and arrow (un'
' ghend- APPRESSED per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!\nAPTERYX pet- APTITUDE ap-! APuUS ped-!\nAQUA akwa- AQUANAUT nau-2 AQUARELLE akwa- AQUARIUM akwa- AQUATIC akwa- AQUI- akw3-\nARA as-\nARABLE are- ARBALEST arku- ARC arku- ARCADE = arku- ARCANE arek- ARCH! = arku- -ARCH arkhein ARCHAEO- arkhein ARCHAEOPTERYX pet- ARCHAIC arkhein ARCHANGEL angelos ARCHEGONIUM gene= ARCHER arku- ARCHETYPE (s)teu- ARCHI- arkhein ARCHIMAGE magh-! ARCHIPELAGO piak-1 ARCHITECT teks- ARCHITRAVE treb- ARCHIVES arkhein ARCHIVOLT arku-\nARCHON'
' per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!\nAPTERYX pet- APTITUDE ap-! APuUS ped-!\nAQUA akwa- AQUANAUT nau-2 AQUARELLE akwa- AQUARIUM akwa- AQUATIC akwa- AQUI- akw3-\nARA as-\nARABLE are- ARBALEST arku- ARC arku- ARCADE = arku- ARCANE arek- ARCH! = arku- -ARCH arkhein ARCHAEO- arkhein ARCHAEOPTERYX pet- ARCHAIC arkhein ARCHANGEL angelos ARCHEGONIUM gene= ARCHER arku- ARCHETYPE (s)teu- ARCHI- arkhein ARCHIMAGE magh-! ARCHIPELAGO piak-1 ARCHITECT teks- ARCHITRAVE treb- ARCHIVES arkhein ARCHIVOLT arku-\nARCHON arkhein -ARCHY a'
' APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!\nAPTERYX pet- APTITUDE ap-! APuUS ped-!\nAQUA akwa- AQUANAUT nau-2 AQUARELLE akwa- AQUARIUM akwa- AQUATIC akwa- AQUI- akw3-\nARA as-\nARABLE are- ARBALEST arku- ARC arku- ARCADE = arku- ARCANE arek- ARCH! = arku- -ARCH arkhein ARCHAEO- arkhein ARCHAEOPTERYX pet- ARCHAIC arkhein ARCHANGEL angelos ARCHEGONIUM gene= ARCHER arku- ARCHETYPE (s)teu- ARCHI- arkhein ARCHIMAGE magh-! ARCHIPELAGO piak-1 ARCHITECT teks- ARCHITRAVE treb- ARCHIVES arkhein ARCHIVOLT arku-\nARCHON arkhein -ARCHY arkhein ARCIFORM = arku- ARCTIC rtko'
##### archein
##### ARCHAE
'. 5. Extended form “argu-, brilliance, clarity, in Latin denominative arguere, to make clear, demonstrate: ARGUE. 6. Suffixed form *arg- ro- in Greek argos (< *argros), white (see pel-2). [Pok. ar(e)g- 64.]\n[arkhein. To begin, rule, command. Greek verb of un- known origin; with derivatives arkhé, rule, beginning, and arkhos, ruler. (ARCH-), -ARCH, ARCHAEO-, ARCHAIC, ARCHI-, ARCHIVES, ARCHON, (-ARCHY); AUTARCHY, EXARCH, MENARCHE.]\narku-. Bow and arrow (uncertain which, perhaps both as a unit). 1. Germanic *arhwo in Old English ar(e)we, earh, and Old Norse *arw-, arrow: ARROW. 2. Latin arcus, bo'
" 6ku-). 5. Suffixed form *pet-yo- in Latin propitius, favorable, gracious, originally a religious term meaning “falling or rushing forward,” hence “eager,” “well-disposed” (said of the gods; pro-, forward; see per'): PROPITIOUS. 6. Suffixed zero-grade form *pt-ero- in Greek pteron, feather, wing, and pterux, wing: -PTER; ACANTHOPTERYGIAN, APTERYX, ARCHAEOP- TERYX, COLEOPTERA, MECOPTERAN, PERIPTERAL, PLE- COPTERAN, PTERIDOLOGY, PTEROCERCOID, PTERYGOID. 7. Suffixed zero-grade form “pt-ilo- in Greek ptilon, soft feathers, down, plume: COLEOPTILE. 8. Suffixed variant form *pté-no- in Greek pténos,"
'APPRESSED per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!\nAPTERYX pet- APTITUDE ap-! APuUS ped-!\nAQUA akwa- AQUANAUT nau-2 AQUARELLE akwa- AQUARIUM akwa- AQUATIC akwa- AQUI- akw3-\nARA as-\nARABLE are- ARBALEST arku- ARC arku- ARCADE = arku- ARCANE arek- ARCH! = arku- -ARCH arkhein ARCHAEO- arkhein ARCHAEOPTERYX pet- ARCHAIC arkhein ARCHANGEL angelos ARCHEGONIUM gene= ARCHER arku- ARCHETYPE (s)teu- ARCHI- arkhein ARCHIMAGE magh-! ARCHIPELAGO piak-1 ARCHITECT teks- ARCHITRAVE treb- ARCHIVES arkhein ARCHIVOLT arku-\nARCHON arkhein'
'PPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!\nAPTERYX pet- APTITUDE ap-! APuUS ped-!\nAQUA akwa- AQUANAUT nau-2 AQUARELLE akwa- AQUARIUM akwa- AQUATIC akwa- AQUI- akw3-\nARA as-\nARABLE are- ARBALEST arku- ARC arku- ARCADE = arku- ARCANE arek- ARCH! = arku- -ARCH arkhein ARCHAEO- arkhein ARCHAEOPTERYX pet- ARCHAIC arkhein ARCHANGEL angelos ARCHEGONIUM gene= ARCHER arku- ARCHETYPE (s)teu- ARCHI- arkhein ARCHIMAGE magh-! ARCHIPELAGO piak-1 ARCHITECT teks- ARCHITRAVE treb- ARCHIVES arkhein ARCHIVOLT arku-\nARCHON arkhein -ARCHY arkhein A'
##### ARCHAIC
'ded form “argu-, brilliance, clarity, in Latin denominative arguere, to make clear, demonstrate: ARGUE. 6. Suffixed form *arg- ro- in Greek argos (< *argros), white (see pel-2). [Pok. ar(e)g- 64.]\n[arkhein. To begin, rule, command. Greek verb of un- known origin; with derivatives arkhé, rule, beginning, and arkhos, ruler. (ARCH-), -ARCH, ARCHAEO-, ARCHAIC, ARCHI-, ARCHIVES, ARCHON, (-ARCHY); AUTARCHY, EXARCH, MENARCHE.]\narku-. Bow and arrow (uncertain which, perhaps both as a unit). 1. Germanic *arhwo in Old English ar(e)we, earh, and Old Norse *arw-, arrow: ARROW. 2. Latin arcus, bow: ARC, AR'
'ACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!\nAPTERYX pet- APTITUDE ap-! APuUS ped-!\nAQUA akwa- AQUANAUT nau-2 AQUARELLE akwa- AQUARIUM akwa- AQUATIC akwa- AQUI- akw3-\nARA as-\nARABLE are- ARBALEST arku- ARC arku- ARCADE = arku- ARCANE arek- ARCH! = arku- -ARCH arkhein ARCHAEO- arkhein ARCHAEOPTERYX pet- ARCHAIC arkhein ARCHANGEL angelos ARCHEGONIUM gene= ARCHER arku- ARCHETYPE (s)teu- ARCHI- arkhein ARCHIMAGE magh-! ARCHIPELAGO piak-1 ARCHITECT teks- ARCHITRAVE treb- ARCHIVES arkhein ARCHIVOLT arku-\nARCHON arkhein -ARCHY arkhein ARCIFORM = arku- ARC'
##### tek[sþ]?-\.\s
' *gatawja- (*ga-, collective prefix; see kom), equipment, in Old English geatwa, geatwe, equipment: HERIOT. 4. Ger- manic variant *t6(w)lam, implement, in Old English ol, implement (possibly borrowed from the cognate Old Norse ¢6/): TOOL. [In Pok. 2. deu- 218.]]\ntegu-. Thick. Germanic *thiku- in Old English thicce, thick: THICK. [Pok. tegu- 1057.]\ntek-. To beget, give birth to. 1. Suffixed form *tek-no-, child, in: a. Germanic *thegnaz, boy, man, servant, warrior, in Old English thegn, freeman, nobleman, mili- tary vassal, warrior: THANE; b. possibly Germanic *the- wern6, girl, in Old High Ger'
'thegn, freeman, nobleman, mili- tary vassal, warrior: THANE; b. possibly Germanic *the- wern6, girl, in Old High German thirona, diorna (> German Dirne), girl: DIRNDL. 2. Reduplicated form *ti-tk-, metathesized in Greek tiktein, to beget, and suffixed o-grade form *tok-o- in Greek tokos, birth: OXYXTOCIC, POLyTocous, TocoLocy. [Pok. 1. tek- 1057.]\nteks-. To weave; also to fabricate, especially with an ax; also to make wicker or wattle fabric for (mud-covered) house walls. 1. Latin texere, to weave, fabricate: TEXT,\nTISSUE; CONTEXT, PRETEXT. 2. Suffixed form *teks-/é in:\n69\ntemp-\na. Latin téla,'
##### HECTARE
##### AREA
```


## [2026-09-04T23:10:28.477Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt && for w in 'آرشیو' 'آرشیتکت' 'هکتار' 'آرشی'; do echo \"=== $w ===\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done",
 "description": "Grep Mo'in for Persian loanwords"
}
```


### [2026-09-04T23:10:30.592Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
=== آرشیو ===
MON_part1.txt:1
MON_part2.txt:0
=== آرشیتکت ===
MON_part2.txt:0
MON_part1.txt:0
=== هکتار ===
MON_part2.txt:1
MON_part1.txt:2
=== آرشی ===
MON_part2.txt:0
MON_part1.txt:2
```


## [2026-09-04T23:10:34.544Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    leaves=t.split('\\f')\n    for i,l in enumerate(leaves):\n        for w in ['آرشیو','هکتار','آرشی']:\n            if w in l:\n                j=l.find(w)\n                print('####',f,'leaf',i,w)\n                print(l[max(0,j-400):j+400])\nEOF",
 "description": "Print Mo'in contexts"
}
```


### [2026-09-04T23:10:36.938Z] TOOL RESULT

```
#### MON_part1.txt leaf 0 آرشیو
ایق. حریص» آزو: 
کامجوی» مرادطلب. در حسرت؛ دارندة 
ارزومندانه: (0-)302-.2 (ق‌مسر.) جون 
آرزومندان» به حال آرزومندی. 
ارستن: «داحع-27 [- بارستن ] (مسص م.) 
توانستن» جر أت کردن» دلیری کردن. 
آرشه: 806 (.) چوب باریکی که روی آن 
چند رشته (غالباً از موی اسب) کشیده و 
برای نسواخستن آلات زهسی (ویولون» 
ویولونسل» کنترباس و مانند آنها) بکار برند. 
آرشیدوک: 501451 () عنوان شاهزادگان 
خاندان سلطنتی اتریش. 

آرشیو: »27 (.) جایی که اسناد» اوراق» 
تصاویر» پرونده‌هاء صفحات موسیقی و 
مانند آن حفظ می‌شود؛ بایگانی. 

آرغده: (6-)270)2(۳02 [- ارغده - آلغده] 
(ص.) حسربص» آزم_ند. خشمگین» 
آرگ‌ون: 0 (ا.) (شیم.) عنصری 
شیمیایی» کٌازی است ساده» بی‌ر نگك» بی‌بو 
و بسی‌طعم که یکك صدم هوارا تشکیل 
می‌ دهد. 

آرم: 7 (.) نشانه‌ای مشخص و معرف 
دولت» اداره» موّسسه» کارخانه و مانند آن. 
ارمان: مقصد [- آرمان؛ زباکی)] (ا.) 
#### MON_part1.txt leaf 0 هکتار
 زینت» آواشن: رسم» 
قاعده. قانون. 


ار: :8 (پس.) پسوند فاعلی (اسم فاعل). و آن 
به آخر مصدر مرخم - سوم شخص مفرد 
ماضی پبوندد و صفت فاعلی سازد. خر بداره 
پرستار» فرماندار. پسوند مفعولی (اسم 
مفعول) گرفتار» کشتار. پسوند اسم مصدر و 
آن در اصل تار» است در مصادر مختوم به 
تن و «دار» است در مصادر مختوم به 
سدن,» گفتار؛ دیدار» کر دار. 

ار 5 (1.) واحد مقیاس سطح, برابر با ۱۰۰ 
متر مربع (یکث دکامتر مربع): هکتار - صد 
۳ 

1 ۶ 28 [ع. ف. 
رای‌هاء اند بشه‌ها. 
آراسستن: 2251 (مصم.) (آراست» 
اراید» خواهد اراست. بباراه اراینده؛ 
آراسته) زینت دادن» زیور کردن. یت 
«آرا ستن» در اصل زینت دادن با افزایش 
است در مقابل «یبراستن» چنانکه بزک کردن 


آرا] (٩)؛‏ ج. رآی؛ 


فرهنگ فارسی معین ۳۹ 


جهره «آراستن» است و زدن شاخه‌ها و 
برگ‌های زبادی درخت «بیراستن». نطم 
دادن» ترتسب دادن. آماده کردن» مها 
ساختن» حاضر کردن.
#### MON_part1.txt leaf 0 آرشی
آرزومند. 
ارزومند: 2.0 (ص‌مر.) دارنده آرزو» 
راجی. مشتاق» شایق. حریص» آزو: 
کامجوی» مرادطلب. در حسرت؛ دارندة 
ارزومندانه: (0-)302-.2 (ق‌مسر.) جون 
آرزومندان» به حال آرزومندی. 
ارستن: «داحع-27 [- بارستن ] (مسص م.) 
توانستن» جر أت کردن» دلیری کردن. 
آرشه: 806 (.) چوب باریکی که روی آن 
چند رشته (غالباً از موی اسب) کشیده و 
برای نسواخستن آلات زهسی (ویولون» 
ویولونسل» کنترباس و مانند آنها) بکار برند. 
آرشیدوک: 501451 () عنوان شاهزادگان 
خاندان سلطنتی اتریش. 

آرشیو: »27 (.) جایی که اسناد» اوراق» 
تصاویر» پرونده‌هاء صفحات موسیقی و 
مانند آن حفظ می‌شود؛ بایگانی. 

آرغده: (6-)270)2(۳02 [- ارغده - آلغده] 
(ص.) حسربص» آزم_ند. خشمگین» 
آرگ‌ون: 0 (ا.) (شیم.) عنصری 
شیمیایی» کٌازی است ساده» بی‌ر نگك» بی‌بو 
و بسی‌طعم که یکك صدم هوارا تشکیل 
می‌ دهد. 

آرم: 7 (.) نشانه‌ای مشخص و معرف 
دولت» اداره» موّسس
#### MON_part2.txt leaf 0 هکتار
ص خوانده 
می‌شد و ماه چهار هفته در میان ایرانیان پس 
از اسلام معمول شده است و حتی کامه 
رشنبه» که در همه ایام هفته به جز آدینه 
(جمعه) هست لغتی است سامی (شنبه)» ولی 
بدون شک ابرانیان عهد ساسانی از استعمال 
هفته در مبان افوام سامی آ گاه بودند. روز 
هفتم مرگ کسی. 

هفوت: ۷2۳۰ (.) لغزش» خطاء ج. 
هفوات. 

هفهف: ]20:2 (اصت ۰) آواز سک 

هق وهق: 7۰-۰6 (اصت ق.) (عم) آوای 
کر بة شد ید » صدای گر یستن سحت. 
هکتار: ۰6۱02۲ (.) واحد برایر مقیاس سطح 
صد ,آر» - یک هکتومتر مربع - و ۱۰ 
مر فرب : 

هک‌تو متر: ۱-۲ (امر.) واحدی برای 
سنجش طول - ۱۰۰ متر 

هکسچه: )۱0۲۵ (اصتد.) جستن گلوه 
فواق. ضح.- (پز.) سکسکه. 

هعکف: 6 (ص.) سیهوده» بیفایده؛ 
مزخرف (بیشتر در مورد اجسام و موجودات 
غیر ذی‌روح بکار برند). 

هل: اد (ع.] (صست. ادات استفهام) آیا. 
مطلب هل: (منط.) بر دو قسم است: بسیط و 
مرکب» بسیط برای طلب وجوده موضوع
```


## [2026-09-04T23:10:51.710Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nj=t.find('آرشیو')\nseg=t[max(0,j-9000):j+3000]\nimport re\nfor m in re.finditer(r'معین[^\\n]{0,20}', seg):\n    print(repr(m.group(0)), m.start()-9000)\nEOF",
 "description": "Find Mo'in page footers near archive entry"
}
```


### [2026-09-04T23:10:54.422Z] TOOL RESULT

```
'معین ۳۹ ' -4187
'معین ' -2955
'معین ۴۱۱ ' -549
```


## [2026-09-04T23:11:14.240Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef show(f, pats, ctx=350, limit=2):\n    try:\n        t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e:\n        print(f,'ERR',e); return\n    leaves=t.split('\\f')\n    for p in pats:\n        print('#####',f,'|',p)\n        n=0\n        for i,l in enumerate(leaves):\n            for m in re.finditer(p,l):\n                print('  [leaf %d]'%i, repr(l[max(0,m.start()-ctx):m.start()+ctx]))\n                n+=1\n                if n>=limit: break\n            if n>=limit: break\n        if n==0: print('  (none)')\n\nshow('LEW_1910.txt',[r'ära\\b',r'ärea',r'ärdeo',r'ardeo',r'ärëo'])\nshow('LAT.txt',[r'āra\\b',r'area,',r'ardeō',r'areō'])\nEOF",
 "description": "Grep Walde LEW and Ernout-Meillet"
}
```


### [2026-09-04T23:11:16.466Z] TOOL RESULT

```
##### LEW_1910.txt | ära\b
  (none)
##### LEW_1910.txt | ärea
  (none)
##### LEW_1910.txt | ärdeo
  (none)
##### LEW_1910.txt | ardeo
  (none)
##### LEW_1910.txt | ärëo
  (none)
##### LAT.txt | āra\b
  (none)
##### LAT.txt | area,
  [leaf 97] ' ex. de Varr.\nS.R. 3 ,10,3).\nCf. sans doute iri. ard "haut", gaul. Arduenna, nom d\'une montagne.\nD l autres langues prdsentent des mots k *-dh- intprieur qui ne sauraient\netre rapproch6s; car on aurait lat. b; du reste le sens de gr. op 9 o£\n"droit" (de FopGFoc;) ei meme du skr. urdhvdh "droit" est un peu dif¬\nferent. Av.areBwo "droit" est ambigu.\narea, -ae ( Sria k basse epoque) f.: rattache k areo par Varron,\nL.L.5,6,38, ubi frunenta secta, ut terantur, [et] arescunt, area. Le\nmot ne ddsigne pas seulement "1\'aire" de la grange, mais tout espace\nddpourvu de construction, la place devant le\'temple ou 1\'autel, la\ncour au milieu de 1 \'atrium (P.F. 13,17 ), ete.; cf. Flor., Dig .50,16,311,'
  [leaf 98] 'arina\n80\nlocus... sine aedificio in urbe area, rure ager appellatur-, et la apA-\ncialisation dans le aena de "aire" est peut-etre secondaire. Ancien,\nnsael. Panronan, M.L.696. - Le diminutif Sreola dAsigne une petite\ncour, une planche de jardin, un parterre; M.1.639. Adj. BreBlis: relatif\nA 1 \'aire. M.L.697; 3 retitor, -tura (Colun.).\nPas de rapprochenent sur.\narBna, -ae £.: r.harSna.\nSre'
##### LAT.txt | ardeō
  (none)
##### LAT.txt | areō
  (none)
```


## [2026-09-04T23:11:26.642Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('LAT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[97][:1500])\nprint('======98======')\nprint(leaves[98][:5000])\nEOF",
 "description": "Print Ernout-Meillet leaves 97-98"
}
```


### [2026-09-04T23:11:28.397Z] TOOL RESULT

```
79
arae
pl. arci dans Varr.; cf. Thes. II 475,8osqq. Le dat.pl. est arcubus-,
arcibus etant rdservd k arx. Nonius distingue arcus et arquus 435.11:
"arcus... onriis suspensus fornix appellatur; arquus non nisi qui in
caelo apparet, quam Irin poetae dixerunt. Vnde et arquati dicuntur
quibus color et oculi uirent quasi in arqui sinilitudinen" : arc; de la,
dans les langues techniques, tout ob j et en forme d'arc: arc-en-ciel,
arche, voute. Atteste de tout temps. Panroman. M.L.618.
Derivds et composds: arques,-itis n.: archer (Festus, Gloss.), d'aprfes.
eques, pedes; arqudtus (arcuatus) scii, norbus: jaunisse; cf. plus
haut le texte de Nonius; M.L.664a, 8348; et tardif arquaticus; arcunen;
cf.Isid.17,9,9: iris Illyrica a sinilitudine Iris caelestis nomen
accepit. Vnde et a Latinis arcunen dicitur, quod flos eius coloris
uarietate eunden arcun caelesten initatur; v. Sofer, p.8; arculus:
coussinet en forme d'arc; arculdtus: en forme de coussinet (= ombr.
arflataf "arculatas"), cf.P.F., 15,6 et 10; inarculun, P.F., 101,5;
arcuarius i adj. et subst.: qui concerne les ares; faiseur d'arcs; ar¬
cuo,-as: courber en arc, -vouter, et ses ddrivds; arcifer - xof^ocpopoS;
arc i-pot ens, arc i-tenens (arqui-) adj,(poetique); arci-selliun,{-soliun):
sifege circulaire; arcuballista: arbalbte; M.L.6i8a.
Cf. v.isLpr (gen.pruor) et v.angl. earh, avec le derive got.arhuiazna,
tous mots s igni fiant "flfeche"; de germ. 'arhtoo, ‘‘arhwas-. Les noms d'armes
n*ont generalement pas d'etymologie indo-en
======98======
arina
80
locus... sine aedificio in urbe area, rure ager appellatur-, et la apA-
cialisation dans le aena de "aire" est peut-etre secondaire. Ancien,
nsael. Panronan, M.L.696. - Le diminutif Sreola dAsigne une petite
cour, une planche de jardin, un parterre; M.1.639. Adj. BreBlis: relatif
A 1 'aire. M.L.697; 3 retitor, -tura (Colun.).
Pas de rapprochenent sur.
arBna, -ae £.: r.harSna.
SreS, -Ss, -ul, -Bre: etre sec. - Ancien, usuel.
DArivAs et conposAs: Bridus (et ardus cf.Thes. II 565,16): sec, des-
sechA (sene phya. et noral); de IA dans la Bible arida = £;r|pa "la
terre"j 3 ridun: terre ferae; Sridulus-, BriditSs , et aritudo-, aresco,
-is: se dessAcher (et exaresco), interarescS (Cic.); arefacio, -is
(arfaciti dans les ass. de Caton; Lucr. sApare encore les deux A 1 Anents
facit are 6,969).
II n’y a pas de substantif *dror correspondant A BreS ((ef. tepor,
tepeti, tepidus, etc.). Le substantif correspondant A Bridus est Brdor.
Mais Brdor a perdu le sens de "sAcheresse" qui est rAservA A BriditBs
et ne signifie plus que "cbaleur ardente, ardeur (sens pbysique et
aoral), Aclat (d'un corps en flaaae)". A ardor se rattacbe Brdeti, -es,
Brsl (ardui Acta Fr.Aru.), Brsun et *assun cf.assus "bruler, etre en
feu; brfiler de (avec ad, in, ou 1'infinitif seul)", dont le parfait
en -sl et le supin en -sun attestent le caractbre rAcent. Ardeti a un
inchoatif Brdgscti (exBrdgsco, et exBrdeo, forni sur exBrdul, M.L.9939a);
A Brsu* ae rattache Brsura.
Lea 1 . roa, ont conoervA ardire H.L.6ao, ardor 694, *ardic 5 re 699;
*ardura 695, *arsio 680, arsBra 689; toua aots qui exprinent 1 'idAede
bruler; Sridus M.L.644 qu±»est peu reprAsentA en dehors de l'italien
et a AtA concurrencA par une foraation plus expressive, siccus, pan¬
ronan. Cf. aussi *arellBre M.L.698.
On rapprocbe tokh. A 3 sar "sec"; akr. isal} "cendre", et, avec des
Alargisseaents rari As, A dentale: tch .ozditi "sAcher", gr. a£u> "Je
sAche", a^aXeoC "sec", ou A gutturale: k (ou g) v.h.a.asca "cendre",
etc., ou gh: got. ango "cendre", cf.ara. azaze* "je sAche" (avec z pouvant
etre issu de *j reprAsentant *zgh). S'y rattache peut-etre 3 ra.
arepennis (arpennis ; aripennus; arapennis d'aprAs arSre), -is a.:
arpent. Mot gaulois; cf.Colua.5,1,6, Salli... seniiugerun quoque are-
pennum uocant; A rapprocher peut-fctre de arepo, CIL HI 909. - M.L.634.
Sur les diversas foraes du aot dans les Gloaea et les textes tardifs,
v. Sofer, p.118 et s.,176. \
arferia: - aqua, quae inferis libabatur dicta a ferendo, siue uas
uini quod sacris adhibebatur. P. 7 .10,93. Terae du rituel, fAainin d'un
adjectif *arferius (et. ferti) peut-etre d'origine dialectale, cf.Xrnout
S Idn.dial. 111. Le terne latin est adferial qu'on lit CGL II 469,96;
564,48. Cf. oabr. affertur "adfertor",-
argeaOnia, -ae f,; piante. Sorte de pavot sauvage. AttestA depuia
Celse et Pline. Adaptation du gr. ipYSjittVTi (cf. argenon, argenonion dans
Pline), souvent corroapue, en agrisonia, M.L.995a , acrimonia, argi-
nonia.
argentun, -I n.: argent; argentarie, ob^et d 1 argent; argent (non-
naie, dAjA dans Plaute); argentun uluum ■ uBpapyupoc. Ancien, usuel.
Psnroaan. N.L.640.
```


## [2026-09-04T23:11:41.875Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef show(f,pats,ctx=400,limit=1):\n    try: t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e: print(f,'ERR',e);return\n    leaves=t.split('\\f')\n    for p in pats:\n        print('#####',f,'|',p); n=0\n        for i,l in enumerate(leaves):\n            for m in re.finditer(p,l):\n                print('  [leaf %d]'%i,repr(l[max(0,m.start()-ctx):m.start()+ctx])); n+=1\n                if n>=limit: break\n            if n>=limit: break\n        if n==0: print('  (none)')\nshow('LEW_1910.txt',[r'Altar',r'ardeo',r'area\\b',r'asca'])\nshow('SKT.txt',[r'ARCH-',r'arch-',r'ARSON',r'arson',r'\\bASH\\b',r'AREA',r'ARCHIVES?'])\nEOF",
 "description": "Grep Walde-1910 and Skeat"
}
```


### [2026-09-04T23:11:43.923Z] TOOL RESULT

```
##### LEW_1910.txt | Altar
  (none)
##### LEW_1910.txt | ardeo
  (none)
##### LEW_1910.txt | area\b
  (none)
##### LEW_1910.txt | asca
  [leaf 13] 'aius, Baidnius I 93 Ballio I 524 Bambalio I 90 Barginna I 97 Bar(rjonius I 97 Bellius I 100 Bilius I 865 Blaisiis (osk.) 108 Blaesus, Blaesius I 108\nWalde-Hofmann, Register\nCacus, Cacius, Ca- ca, Cacca, Cace- lius, Cacilius, Cacurius I 127\nCaesar, Caesius I 133\nCaius I 577\nCalauans (pael.) I 144\nKalaviis, Kaluviets (osk.) I 144\nCamillus I 147\nCamurius, Camu- revus, Camonius I 149/50\nCasamo I 176\nCasca I 156, 176\nCato, Catilina lI 183\nCella I 196\nCerficius I 204\nKenssurineis (osk.) I 199\nChilo I 215/6\nCicero I 211\nCicurinus I 213\nKiuipits (osk.) I 219\nCilo I 215/6\nCila, Cilonius, Cilnius I 216\nKlaverniie (umbr.) L229\nClozl. (volsk.) I 237\nClovatius, Cloven- tous I 237\nCluentius I 237\nClupiarius I 235\nKluvatiis (osk.) L237\nKluviier (ambr.)\nI 237\nCnaiviies, I 6138\nCnaives\ncneve (etr.) I 613\nC'
##### SKT.txt | ARCH-
  (none)
##### SKT.txt | arch-
  [leaf 11] 'A   CONCISE\nETYMOLOGICAL   DICTIONARY\nOP  THK\nENGLISH    LANGUAGE\nBY  THB\nREV.  WALTER  W.  SKEAT,  LiTT.D.,  LL.D.\nffUUNGTOM   AND  ftOSWOSTH   FBOFSSSOB  OF  AKGLO4AX0N  IN THK   UMIVEBSITY  OP  CAMBBIDGB\nPOUBTH   EDITION,  FUBTHEB  RBYISBD tyiTfl  ENLARGED  SUPPLEMENT\n*Were  man  to  live  co-eval  with  the  son, The  patriarch- pupil  woald  be  learainf;  still.*\nTOUNG,  Ni^hi  Thoughts,  vil,  86\nNEW  YORK HARPER   &    BROTHERS.    PUBLISHERS\nFRANKLIN    SQUARE 1900\n'
##### SKT.txt | ARSON
  [leaf 356] "  spnre.  L./anrw/ is  allied  to  Gk.  trva^i'ur,  scarce,  rare,  and to  £.  span.\nParsley.  (F.  -  L.  -  Gk.)  Formerly persciy.  —  F.  pern  J;  older  form/^nrnV.  — L.  pttrosiiinum.  —  Gk.  m*Tpoisi>^i¥oVt  rock parsley.  —  Gk.  wirpot.  rock,  stone  ;  aiktrow, a  kind  of  parsley ;  »ee  Celery.\nParsnop.  Parsnip.  (F.-L.)  ForrocA^ parjwp,  and  tUU  bcUct  pasntffi^  »*  «\n332\nPARSON.\nI\nI\nPals^nve ;  the  r  being  inlrufiive.  —  O.  F. pojUnatjue,  a  parsnip  (by  dropping  /,  and change  of  ^  to  /.  as  in  Gk.  W/iirc  «  L. qui*tqut),^\\^  pastmaca,  a  pannrp ;  orig. A  root  dog  op.—  L. /^Lf/i>«d/r,  to  dig  np.— l^pastimtm,  a  two-pronged  dibble.  %  The sumx-#fc*/ was  assimilated  to  that  ai  tumep. Farson;  see  Sound  (3). Part.  (F.  -  L.)  FJvw"
##### SKT.txt | arson
  [leaf 199] '.x  -j>  i]<vii>  bwed.  dial.^/im, kove),\ni>*.  -  Teut.>  M  E.  ghmn.  - ,  giamr  (F.  planer),  lo  glean; «fir  Ca.p.  561).  -  Low  L.  A\'.Vwa, k»d,  ■  honaful.  Of  Icut.  oiigin; *  in  A.S.  ^Vn,  a  banaful, E.  jt.\'m,  to  proviilc  hamlluU y  for  a  lltatcticr.     ^  WcaUo\nf"    "     (Levins),   aiso\ni~  c  due  to  A.S.\n■■■.    id.\nir.  -  U)      O.  F.  ^ebe,\nponging  to  a  parsonage ;\'\n,  «oU,  a  dod  of  earth.    Allied\n%  kite  (b!tt)) :  see  Qlids. I,  a  glowing  coal ;  see  Glow. ,    wnging,    (E.)      A.  S.   ^tV^, jojr,  miilh,   mnsic+Iccl.  ^, Swcd.  dial  gly,  mockery, vmlley.  i.C.)    Gael,  and r,  a  valley,  glen, ^lublc.  tDu)     Du. lo   slide  •• •way.     .VlLied    to\nt  lock  nf  hair.  (C )     Iri^h  and\n.x\\t.\nt    (E).     Hie  same '
##### SKT.txt | \bASH\b
  (none)
##### SKT.txt | AREA
  (none)
##### SKT.txt | ARCHIVES?
  (none)
```


## [2026-09-04T23:11:57.088Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('leaves',len(leaves))\nfor i,l in enumerate(leaves):\n    if re.search(r'hect[a-z]*are|hectare',l,re.I):\n        m=re.search(r'hectare',l,re.I)\n        print('[leaf %d]'%i, repr(l[max(0,m.start()-700):m.start()+700]))\n        print('---')\nEOF",
 "description": "Find hectare in Funk &amp; Wagnalls vol2"
}
```


### [2026-09-04T23:11:59.385Z] TOOL RESULT

```
leaves 774
[leaf 386] 'ily  Bible,  kept  In  the  chief ,   room.— ha’  homsc,  the  residence  of  a   Scottish  Jalrd;  the ■■■ .   hall.\n,   ha;  1   hH;  3   ha,  prore.  [Dial.,  Eng.)  He, fea,  n.  &   irtlerj.  1.  An  exclanaation  or  sound  mflde  bv  a quick  expulsion  of  breath  under  some  sudden  simotion (as  surprize,  joy,  or  grief)  or  in  the  act  of  lauphing.\nGfatem.:  Jfo/ Ho/ Ilausfi.  Nowitiatimotolauahl\n.   ;   .   Ow»N  Mbkjjdwh  Clvfemneafrii  div.  six.\n2*,  A   sound  indicating  hesitation,  indecision,  or  lack  of ,   words.  :   [Natural;  found  in  AS.,  L.  G.,  etc.] h.  a.j.aft&r.  Horse\' artillery;  ftoo  (in  this  year).\nHa.,  aftfir*  Hannah.  -   : ha.,  abbr.  Hectare.\nhaaf,  1   hat;  2   hilt.  n.  A   deep-sea  fishing-ground  oft  the  coast of  Shetland,  or  the  Orkneys.  [<  Ice.  haf,  sea.]  —   haaf\'- boat",  n.  A   boat  for  haaf-flshing.— h.-flsh,  n.  T\'he great  bearded  seal.—  h.-Hshlng,  n.  Deep-sea  fishing,  as  for\niia\'ba,  lii\'ba;  2   U\'bfl,  ».  [ha\'bas,  1   fl\'baz;  2   ii\'bag,  [Sp.J  [Rare.]  To  deal  or  traffic,  especially  In  a   small  Habenaria A   bean:  in  the  plural,  any  kind  of  pulse.  way  or  In  small  wares.—  liab\'er-dashf-  I.  tridentata\nllab\'a-cnc,  lhab\'8-kuk:21iab\'a-eflc,  M.  Hf&.  (Doual).  a.  Petty;  small.  II.  a.  Haberdashery.\nUa>ba\'lab,  l   he-bS\'ya  or  -bai\'s;  2   ha-bfi\'ya  o'
---
[leaf 388] 'm  in  a house.—  ha’  Bible,  the  family  Bible,  kept  In  the  clilcf room.— ha’  house,  the  residence  of  a   Scottish  laird;  the hall.\nna,  1   hff;  2   ha,  pron.  [Blab,  Eng.)  He.\nha,  ri.  &   inter}.  1.  An. exclamation  or  sound  made  by  a quick  expulsipn  of  breath  under  some  sudden  wmotion (as  surprize,  joy,  or  grief)  or  in  the  act  of  laiip\'hing.\nGlytem.:  Hn!  Hal  llaugh.  Nowitistirootolaulsh!  ■ OwBK  Mebbmth  OvfeOTTiesfns  div.  six.\n2.  A   sound  indicating  hesitation,  indecision,  or  lack  of words.  [Natural;  found  in  AS.,  L.  G.,  etc.)\nh.  a.,  aWr.  Horse  artillery;  Acc  anModn  this  year) .\nHa.,  a66r.  Hannah,  .\nha.,  abbr.  Hectare.\nhaaf,  1   hhf;  3   haf,  n.  A   deep-sea  fishing-ground  oft  the  coast\' of  Shetland,  or  the  Orkneys.  [   <   Ice.  haf,  sea.]  — haaf’- .   boat",  n.  A   boat  for  haaf- fishing,— h.»fi.sh,  n,  :   The great  bearded  seal.—  h. -fishing,  n.  Deep-sea  fishing,  as  for\nha\'ba,  la\'ba;  2   S\'ba.  a.  [ha\'bas,  i   STjaz;  2   a\'blig,  yiL]  [Sp.]  [Rare.]  To  deal  or  traffic,  especially  in  a   small  Hdbenarla .4  bean;  in  the  plural,  any  kind  of  pulse.  way  or  in  email  ware.s.— hab\'er-dashf-  I.  trideniata\nHab\'a-cuc,  lhab\'B-kuk:2hab\'a-cilc,  w.  J3f6.  (DounI).  a.  Petty;  small.  II.  n.  Haberdashery.\nHa-ha Tah,  l   ha-b6\'ya  or -bal\'s;  2   '
---
```


## [2026-09-04T23:12:06.879Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    for m in re.finditer(r\"ec[\\'’]?ta[rn]e|hecto-|1133|hec\\W{0,3}tare\",l):\n        print('[leaf %d]'%i, repr(l[max(0,m.start()-500):m.start()+500]))\n        print('---')\n        break\nEOF",
 "description": "Locate FSD hectare entry"
}
```


### [2026-09-04T23:12:08.957Z] TOOL RESULT

```
[leaf 386] 'An  exclanaation  or  sound  mflde  bv  a quick  expulsion  of  breath  under  some  sudden  simotion (as  surprize,  joy,  or  grief)  or  in  the  act  of  lauphing.\nGfatem.:  Jfo/ Ho/ Ilausfi.  Nowitiatimotolauahl\n.   ;   .   Ow»N  Mbkjjdwh  Clvfemneafrii  div.  six.\n2*,  A   sound  indicating  hesitation,  indecision,  or  lack  of ,   words.  :   [Natural;  found  in  AS.,  L.  G.,  etc.] h.  a.j.aft&r.  Horse\' artillery;  ftoo  (in  this  year).\nHa.,  aftfir*  Hannah.  -   : ha.,  abbr.  Hectare.\nhaaf,  1   hat;  2   hilt.  n.  A   deep-sea  fishing-ground  oft  the  coast of  Shetland,  or  the  Orkneys.  [<  Ice.  haf,  sea.]  —   haaf\'- boat",  n.  A   boat  for  haaf-flshing.— h.-flsh,  n.  T\'he great  bearded  seal.—  h.-Hshlng,  n.  Deep-sea  fishing,  as  for\niia\'ba,  lii\'ba;  2   U\'bfl,  ».  [ha\'bas,  1   fl\'baz;  2   ii\'bag,  [Sp.J  [Rare.]  To  deal  or  traffic,  especially  In  a   small  Habenaria A   bean:  in  the  plural,  any  kind  of  pulse.  way  or  In  small'
---
[leaf 388] 'ri.  &   inter}.  1.  An. exclamation  or  sound  made  by  a quick  expulsipn  of  breath  under  some  sudden  wmotion (as  surprize,  joy,  or  grief)  or  in  the  act  of  laiip\'hing.\nGlytem.:  Hn!  Hal  llaugh.  Nowitistirootolaulsh!  ■ OwBK  Mebbmth  OvfeOTTiesfns  div.  six.\n2.  A   sound  indicating  hesitation,  indecision,  or  lack  of words.  [Natural;  found  in  AS.,  L.  G.,  etc.)\nh.  a.,  aWr.  Horse  artillery;  Acc  anModn  this  year) .\nHa.,  a66r.  Hannah,  .\nha.,  abbr.  Hectare.\nhaaf,  1   hhf;  3   haf,  n.  A   deep-sea  fishing-ground  oft  the  coast\' of  Shetland,  or  the  Orkneys.  [   <   Ice.  haf,  sea.]  — haaf’- .   boat",  n.  A   boat  for  haaf- fishing,— h.»fi.sh,  n,  :   The great  bearded  seal.—  h. -fishing,  n.  Deep-sea  fishing,  as  for\nha\'ba,  la\'ba;  2   S\'ba.  a.  [ha\'bas,  i   STjaz;  2   a\'blig,  yiL]  [Sp.]  [Rare.]  To  deal  or  traffic,  especially  in  a   small  Hdbenarla .4  bean;  in  the  plural,  any  kind  of  pulse.  way'
---
[leaf 423] 'hrenia.  He\'bron,  1   Iii\'bran;  2   hS\'bron,  1.  Rift.  A   town,  19  m.  S. n.n.  One  suffering  from  hebephrenia.  he"be-phrc\'nlct.  W.  of  .Jerusalem,  Palestine.  Josh,  xv.ai.  3.  A   township He\'beri,  ihl\'bar;  2   hS\'ber,  ».  J3<6.  1   Chron.  v,  XZ.  Same  and  town,  county«.seat  of  Thayer  county.  Neb.  3.  A   town asEBEB.  In  Tolland  county,  Conn.\nHe\'beri,  ».  1.  Bcginatd  (Vnl783-4/jl826),  an  English  He-bro\'na,  Ihi-brO\'no;  2   he-brO\'na,  »,  Rib.  (Doual).\n1133\nKey  1:  {iIsle;nu  =   0Mt;©il;  iii=:feud^  <5h5n;go;  Jet;xi=sinfli;  8o;i^p;  €hln,ftd3;  s^nre;  F.  bon,diine;H  =   Ioch.t,  ofeaoZefe/fcuaWanl KkyS:  bd6k,  beat;  fyll,  rule,  ciire,  biit,  bfini;  i5il,b6f;  «J=:k;  $   =   s;  go,  gem;  ink;  srsz;  thin,  this;  F.  bou,  clUne;  h   =   1o«15.\nleawnlf\n.hedge\nHe-bro\'ni,  1   lii-l)r3\'m;  3   he-br5\'nl.  n.  JSift.  (Doiial).  r<  Tt.  ‘hekel,  <   honl:,  hook.)  — heck\'llng»nia«chlne\'\',  n..  ey«?.— h. •.setting\',  n.  Weati'
---
```


## [2026-09-04T23:12:18.135Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nl=leaves[423]\nprint(len(l))\nfor m in re.finditer(r'ect|are\\b|Gr\\.',l):\n    pass\ni=l.find('1133')\nprint(l[:6000])\nEOF",
 "description": "Print FSD leaf 423"
}
```


### [2026-09-04T23:12:20.233Z] TOOL RESULT

```
21190
ally  during  the  19th  century
have  brought  the  old  tongue  nearer  to  the  realm  of  an J   I   !   exact  science.
lit     /   /   I   I   I   Hebreio,  ia  point  of  force  and  purity,  seems  at  its  height  ia
-the/”/ (I  1   Isaiah.  Coleeidob  Taftle  Talft  Feb.  2,  1827.
a.  \/ /   1   1   [   <   F.  hebreu,  <   L.  Hebrmus,  <   Gr.  Hebraios,  <   Ara-
lent.  p   /   maia*  ebray&,  <   Heb  "ibri.  In  ref  to 'Eber,  Heber,  sup-
■'rill  \   w'C  posed  ancestor  of  the  Hebrews.]  —   He'brew-dom,  n. ugly  ffljilLS'  ~   Epistle  to  the  Hebrews,  one  of  the  New  Testament
.   -   books,  of  uncertain  authorship,  addressed  to  Christians  of
VTphP  n   Hebrew  birth,  showing  the  relation  of  the  We  and  work  of
nilntlne  on  in  Christ  to  the  Mosaic  system. antiniievuRP  He'brew-e.ss,  1   M'bru-es:  2   hc'bni-es,  n.  A   Jewess, antique  vase.  He-brew-lsm,  He'brew-ist,  Same  as  Hebraism.  Hebra-
heb'e-nont,  ».  Probably  henbane:  a   nonce-word  of  Shake-  ist.
speare.  He-brI'elan,  n.  [Rare.]  Same  as  Hebraist.
hc"be-pet'a-lous,  a.  [Rare.]  Bot.  Having  the  petals  pu-  Heb'rl-des,  1   Iieb'n-dTz;  2   lieb'ri-clEg,  n.  pi.  A   group  of  160 bescent.— Iie"be-pljrc'nl-a,  n.  Pathol.  A   mental  dis-  islands  on  the  west  coast  of  Scotland;  3,000  sq.m.;  chief order  incident  to  the  age  of  puberty;  insanity  of  pubescence.  town,  Stornoway.— He-brid'e-an,  He-brid'l-an,  a.  &   n.
—   he"be-phre'nl-ac.  I.  «.  Affected  with  hebephrenia.  He'bron,  1   Iii'bran;  2   hS'bron,  1.  Rift.  A   town,  19  m.  S. n.n.  One  suffering  from  hebephrenia.  he"be-phrc'nlct.  W.  of  .Jerusalem,  Palestine.  Josh,  xv.ai.  3.  A   township He'beri,  ihl'bar;  2   hS'ber,  ».  J3<6.  1   Chron.  v,  XZ.  Same  and  town,  county«.seat  of  Thayer  county.  Neb.  3.  A   town asEBEB.  In  Tolland  county,  Conn.
He'beri,  ».  1.  Bcginatd  (Vnl783-4/jl826),  an  English  He-bro'na,  Ihi-brO'no;  2   he-brO'na,  »,  Rib.  (Doual).
1133
Key  1:  {iIsle;nu  =   0Mt;©il;  iii=:feud^  <5h5n;go;  Jet;xi=sinfli;  8o;i^p;  €hln,ftd3;  s^nre;  F.  bon,diine;H  =   Ioch.t,  ofeaoZefe/fcuaWanl KkyS:  bd6k,  beat;  fyll,  rule,  ciire,  biit,  bfini;  i5il,b6f;  «J=:k;  $   =   s;  go,  gem;  ink;  srsz;  thin,  this;  F.  bou,  clUne;  h   =   1o«15.
leawnlf
.hedge
He-bro'ni,  1   lii-l)r3'm;  3   he-br5'nl.  n.  JSift.  (Doiial).  r<  Tt.  ‘hekel,  <   honl:,  hook.)  — heck'llng»nia«chlne'',  n..  ey«?.— h. •.setting',  n.  Weating.  A   fURpo.sition  of  the
lie'hroii-ite,  1   iil'bran-ait:  3   he'bron-It,  n.  Mineral.  Am-  Same  as  H.tTCHEn.—  hecMcr,  n.  One  ■who  hcekles.  In  hedtHiB  in  a   loom,  wlu>n  reecl.s  of  dinerent  texture  are  Inter-
blygonite.  [<  He6-o«,  Me.)  [C’ftron.  x.xvl.  30.  any  senjse:  specif.,  a   person  who  pesters  a   political  candidate  changed.— hetl'dUng,  n.  A   .set  of  weavers’ harness.
He'bron-ites,  1   W'bron-aits;  2   Ue'bron-Its,  n.  pi.  Bib.  1   ■with  vexatious  questions  in  open  meeting.  hedet>  *.  &   n.  Head.
!iec-a.s'to-the"lsm,  l   heU-as'to-thl’izrn;  2   hec-as'to-thS’istn,  hcck'ie,  n.  1.  Same  as  hackle.  3t.  [Scot.)  A   plume  in  a   hed'e-bo-  1   hod’a-bO;  2   heri'e-bo,  ».  [Dan.]  Embroidered n.  The  practise  of  making  a   god  of  each  individual  object,  Highiand  soldier’s  bonnet.  openwork.
as  In  the  religion  of  savages.  Compare  pantheism,  [<  heck'Ie-back",  1   hck'l-bak':  2   h6k'I-bak*,n.  [Scot,]  A   sea*  He'de-'inar"ken,  1   hf"'dr!-inHr'’keM;  2   lie'de-injir'ic6n,  n.  A Gr. /wfcasfos,  each,  +   f/!cos,  god.]  stickleback  (SpJnacftfa  cufffarfs).  province  in  Norway;  10,621  sq.  m.
Hec"a-tjie'as,  1   hek’a-ti'us;  2   hSc’a-tS'fls,  ft.  1.  H.  of  Heck'niond-wlke,  1   hek'm3nd-walk;2hEk'tnontl-wik,  n.  A   hed'en-berg-ite,  1   bed'en-bvirg-nil;  2   3iM'cn-berg-lt.  n. Abdera,  a   Greek  historian,  grammarian,  and  critic;  lived  market'town  and  urban  district  in  ■!¥■.  Yorkshire,  England.  Mineral.  A   calclunwron  pyroxene  (CaEeiSiO.-^)  s)  that about  .325  3.  C.  S.  H.  of  Miletus  (.5.i0?-476  B.  G.),  a   Greek  Hec'la,  n.  Same  ms  Hekla.  [ocean,
historian  and  geographer.  Ilec'Ja  and  Grl'pcr  Bay.  A   bay  In  Melville  Island,  Arctic
Hec'a-te,  1   hek'e-t!;  2   h6o'a-te  or  1   hek'it;  S   hSc'at) ,   n.  1.  Or.  hect'-  1   1   he!:t'-,  hek'to-;  2   hdet'-,  hCc'to-.  From  Greek
’   ‘       --<*-<  hec 'to-,  /   Afifca/oft,  a   hundred;  combining  forms.
Words  beginning  with  these  preftxea  will  hefound  in  alpha- betical place,  either  singly  or  In  groups, hec'tare,  1   hek'tar;  2   hSc'tar,  n.  A   measure  in  the  metric
Mylb.  A   goddess  of  undefined  attri- butes ,   having  power  over  earth,  heaven, and  the  underworld;  hence  repre- sented as  triformed,  and  the  goddess of  crossways.  She  became  conse- quently partially  identified  with  other goddesses  (Selene,  Aphrodite,  Hestia, Demeter,  Artemis,  etc.),  and  was  asso- ciated with  moon  •   worship,  ghosts, shades  of  the  dead,  sorcery,  and  the nether  world.  As  a   goddess  of  the underworld  she  appears  In  a   hideous form;  serpents  issue  from  her  feet, serpents  are  fwlned  In  her  hair,  she bears  a   lighted  torch  In  her  hand, and  two  black  shaggy  dogs  are  her attendants.  Hee'att;  Hee'eatJ.  2.
Hence,  a   h.ag;  a   witch.
But  such  a   Hecate,  such  a   very  fright.
She  shrieked  aloud  and  shuddered  at  the sight.  Saxe  The  Pride  of  Beauty  st.  2.
3.  In  Shakespeare’s  iV/acMb,  the  god- dess of  the  infernal  regions.  [   <   L.
Hecate,  <   Gr.  Hekati,  <   hekaios,  far- shooting,  <   hekas,  far  off.]  — Hec"«  o^tue a-te'an,  a.  He-cat'lct;  Hec' tinej.— Hec"a-te'Ion,  n.  [Gr.] temple  or  shrine  of  Hecate, hec'a-tee,  1   hek'a-tl;  2   “
crystallizes  in  the  mona
```


## [2026-09-04T23:12:28.132Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read()\nl=t.split('\\f')[423]\ni=l.find(\"hec'tare\")\nprint(repr(l[i:i+900]))\nj=l.find(\"hec'tare\",i+5)\nprint('---2nd---', repr(l[j:j+600]) if j>0 else None)\nEOF",
 "description": "Extract FSD hectare entry text"
}
```


### [2026-09-04T23:12:31.057Z] TOOL RESULT

```
"hec'tare,  1   hek'tar;  2   hSc'tar,  n.  A   measure  in  the  metric\nMylb.  A   goddess  of  undefined  attri- butes ,   having  power  over  earth,  heaven, and  the  underworld;  hence  repre- sented as  triformed,  and  the  goddess of  crossways.  She  became  conse- quently partially  identified  with  other goddesses  (Selene,  Aphrodite,  Hestia, Demeter,  Artemis,  etc.),  and  was  asso- ciated with  moon  •   worship,  ghosts, shades  of  the  dead,  sorcery,  and  the nether  world.  As  a   goddess  of  the underworld  she  appears  In  a   hideous form;  serpents  issue  from  her  feet, serpents  are  fwlned  In  her  hair,  she bears  a   lighted  torch  In  her  hand, and  two  black  shaggy  dogs  are  her attendants.  Hee'att;  Hee'eatJ.  2.\nHence,  a   h.ag;  a   witch.\nBut  such  a   Hecate,  such  a   very  fright.\nShe  shrieked  aloud  and  shuddered  at  the sig"
---2nd--- None
```


## [2026-09-04T23:12:43.747Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nl=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read().split('\\f')[423]\nfor m in re.finditer(r'ares|hecto-|2\\.47|acres|hectar',l):\n    print(repr(l[max(0,m.start()-250):m.start()+300]));print('....')\nEOF",
 "description": "Search FSD leaf for hectare definition text"
}
```


### [2026-09-04T23:12:47.277Z] TOOL RESULT

```
'ie  and  pungent  borb.s  or  low shrubs  of  the  mint  family,  ■with  small  leaves  ami  .small  blue or  purple  flowens.  If.  puhgioldes  is  the  common  pennyroyal. See  PENsyROYAL.  [   <   Gr.  Mtlyn,  .sweet,  osmf,  smell.]\nsystem\' £47  acres:  the  French’ unit  of  land-measure.  See  he"de-o\'jn«)l,_X  hrdi-t’i\'mdl  or -nml;  2   brde-O\'mot  o;\nMETRIC.  [P.,  <   Or. /lekfMoa,  hundred, -b  L.  area,  area.)  Client.  An  oily  ketonie  luimd  (CisH\'.sO)  occurring  in  oil  of\nThera  mast  exist  133.000  Hv-inif  worms  in  a  '
....
```


## [2026-09-04T23:13:12.840Z] TOOL CALL #38: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T23:13:12.845Z] TOOL RESULT

```


```


## [2026-09-04T23:13:17.197Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/archive",
 "prompt": "Give the full etymology of \"archive\" and \"archives\", including Greek arkheion, Latin archivum/archium, French archives, and dates of first English use."
}
```


## [2026-09-04T23:13:17.203Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/area",
 "prompt": "Full etymology of \"area\": Latin area, its origin, and whether it is connected to arere \"to become dry\"."
}
```


### [2026-09-04T23:13:26.884Z] TOOL RESULT

```
# Etymology of Archive/Archives

**Archive (verb):** First appeared in 1819, derived from the noun "archives."

**Archives (noun):** The documented history spans from ancient Greek through modern English:

- **Greek origin (c. 600 BCE):** From *ta arkheia* ("public records"), plural of *arkheion* meaning "town hall, public building," derived from *arkhē* ("government," literally "beginning, origin").

- **Latin (Late):** *Archivum* (plural *archiva*) denoted "written records" and the place storing them.

- **French (16th century):** The word evolved to *archif* in Old French, becoming *archives* in Modern French.

- **English (c. 1600):** First recorded as "records or documents preserved as evidence," adopted from the French form.

- **English expansion (1640s):** The meaning expanded to include "the place where public records and historical documents are kept."

The semantic journey reflects the word's practical purpose: from the Greek concept of a *government building* to Latin's emphasis on *stored records*, and finally to English's dual meaning encompassing both documents and their physical repository.
```


### [2026-09-04T23:13:27.783Z] TOOL RESULT

```
# Etymology of "Area"

The word "area" comes from Latin *area*, meaning "level ground, open space," used for building sites, playgrounds, and threshing floors. However, its ultimate origin is uncertain.

## Possible Connection to "Arere"

According to the etymology source, there is a proposed but unconfirmed link to the Latin verb *arere*, meaning "to become dry." The theory suggests this connection relies on the notion of "bare space cleared by burning." This derivation is described as "irregular" and speculative rather than definitively established.

## Timeline

- **1530s**: First recorded English usage meaning "vacant piece of ground"
- **1560s**: Extended to mean "any particular amount of surface contained within any set of limits"
- **1959**: "Area code" appears in North American telephone systems

The etymological record indicates uncertainty about whether *area* truly derives from *arere*, making this a plausible but unproven linguistic connection.
```


## [2026-09-04T23:13:31.049Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/arson",
 "prompt": "Full etymology of \"arson\": Anglo-French, Old French arsun, Medieval Latin arsionem, Latin ardere/arsus, dates."
}
```


## [2026-09-04T23:13:32.216Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ash",
 "prompt": "Full etymology of \"ash\" (the powdery residue): Old English æsce/asce, Proto-Germanic *askon, PIE root, and cognates."
}
```


### [2026-09-04T23:13:37.498Z] TOOL RESULT

```
# Etymology of Arson

The word "arson" entered English in the 1670s, originating from Anglo-French *arsoun* and Old French *arsion*. These derived from Late Latin *arsionem*, which came from the Latin verb *ardere*, meaning "to burn."

The term literally describes "malicious burning of property." Before the Norman French term was adopted, Old English speakers used *bærnet* (literally "burning") to describe this offense.

The ultimate root is the Proto-Indo-European *as-, meaning "to burn, glow," which also gave rise to related English words like "ardent," "arid," and "ash."
```


### [2026-09-04T23:13:41.718Z] TOOL RESULT

```
# Etymology of "Ash"

The word "ash" has two distinct etymologies:

## Ash (the residue)
This noun derives from Middle English *asshe*, tracing back to Old English *æsce*. The Online Etymology Dictionary indicates it comes from Proto-Germanic *\*askon*, ultimately from a Proto-Indo-European root meaning "to burn, glow." The volcanic sense—"finely pulverized lava thrown from a volcano"—emerged in the 1660s.

The term gained religious significance through **Ash Wednesday** (circa 1300), which developed from Pope Gregory the Great's practice of sprinkling ashes on penitents' heads on Lent's first day. By the late 13th century, "ashes" also referred to cremated human remains.

## Ash (the tree)
This noun originates from Old English *æsc*, deriving from Proto-Germanic *\*askaz/askiz*. It ultimately traces to a PIE root *\*os-* meaning "ash tree," with cognates appearing across numerous Indo-European languages including Armenian, Greek, Latin, and Russian.

The ash tree's tough, elastic wood made it prized for spear-shafts in ancient times. Consequently, Old English *æsc* sometimes meant "spear," particularly in poetic contexts like *æsc-here* ("company armed with spears").
```


## [2026-09-04T23:13:47.320Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82eh%E2%82%81s-",
 "prompt": "What is this PIE root's meaning and what derivatives are listed (Latin āra, ārēre, Hittite, Germanic *askǭ, Sanskrit āsa-)? Quote the entry."
}
```


## [2026-09-04T23:13:49.636Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%84%CF%81%CF%87%CF%89",
 "prompt": "Give the etymology of Ancient Greek ἄρχω (arkhō) - is the origin known or unknown? What derivatives are listed (ἀρχή, ἀρχός, ἄρχων, ἀρχεῖον)?"
}
```


### [2026-09-04T23:13:54.746Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂eHs-

## Root Meaning

The PIE root *h₂eHs- carries four primary meanings:

1. to be dry, to dry
2. to burn, to glow
3. hearth
4. ashes

## Key Derivatives

The entry documents extensive derivatives across Indo-European languages:

**Latin forms:** "āreō ("to be dry")" and the related stative derivative *h₂eHs-eh₁-(ye)-.

**Hittite:** The root noun form yields "ḫāšš-, "ash(es); dust; soap"" from Proto-Anatolian.

**Germanic:** Multiple formations are listed, including "*askǭ ("ash, ashes")" and "*asjō" leading to Old High German "essa ("furnace")".

**Sanskrit:** The Indo-Iranian branch preserves "ā́sa, "ashes, dust"" from Proto-Indo-Aryan *HáHsas.

The entry notes these forms reflect various morphological extensions of the root, with considerable scholarly debate about whether the original root was *h₂eHs-, *h₂eh₁s-, or *h₂es-, evidenced by differing reflex patterns across daughter languages.
```


### [2026-09-04T23:13:58.458Z] TOOL RESULT

```
# Etymology of ἄρχω (arkhō)

## Origin Status
The origin is **disputed**. The Wiktionary entry states: "Of disputed origin" with two competing theories presented.

## Proposed Etymologies

**Theory 1:** From Proto-Indo-European *h₂r̥-sḱe-ti ("to start, rule"), described as "an inchoative formation" from *h₂er- meaning "to fit, put together."

**Theory 2:** From a root *h₂ergʰ- ("to begin, rule, command"), possibly cognate with Lithuanian regė́ti ("to watch, see").

The entry notes that sourcing for the second etymology is requested, indicating scholarly uncertainty.

## Listed Derivatives

The document confirms three of your mentioned derivatives appear in the "Related terms" section:
- ἀρχή (arkhḗ)
- ἀρχός (arkhós)  
- ἄρχων (árkhōn)

Additionally, the entry lists ἀρχι- (arkhi-) as a prefix and ἀρχικός (arkhikós), though ἀρχεῖον is not explicitly mentioned in the provided content.
```


## [2026-09-04T23:14:13.632Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%B4%DB%8C%D9%88",
 "prompt": "Does this page have a Persian entry for آرشیو? What etymology does it give (borrowed from French archive?) and what is the meaning/pronunciation?"
}
```


## [2026-09-04T23:14:14.318Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/architect",
 "prompt": "Full etymology of \"architect\": French architecte, Latin architectus, Greek arkhitekton (arkhi- + tekton), dates of first English use."
}
```


### [2026-09-04T23:14:18.450Z] TOOL RESULT

```
# Persian Entry for آرشیو

Yes, this Wiktionary page contains a Persian entry for **آرشیو** (âršiv).

**Etymology:** The word is "Borrowed from French _[archives](/wiki/archives#French 'archives')_." It ultimately traces back through Latin and Ancient Greek to Proto-Indo-European roots.

**Meaning:** The entry defines it as "[archives](/wiki/archives 'archives')" with a synonym listed as بایگانی (bâygâni).

**Pronunciation:** In Iranian Persian (formal), the IPA pronunciation is given as [ʔɒːɹ.ʃíːv], with the transliteration âršiv.
```


### [2026-09-04T23:14:20.478Z] TOOL RESULT

```
# Etymology of "Architect"

The word "architect" entered English around 1560s, originating from French *architecte*, which derived from Latin *architectus*. This Latin term came from Greek *arkhitekton*, combining two elements: *arkhi-* meaning "chief" and *tekton* meaning "builder" or "carpenter."

The Greek root *tekton* traces back to the Proto-Indo-European root *teks-, which originally meant "to weave" but also extended to "fabricate."

Before adopting the Greco-Latin term, Old English used *heahcræftiga* ("high-crafter") as a direct translation of *architectus*. The word's meaning expanded by the 1580s to describe "one who plans or contrives" anything beyond just buildings, reflecting its broader metaphorical applications in modern usage.
```


## [2026-09-04T23:14:30.573Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D8%B1%D8%B4%DB%8C%D8%AA%DA%A9%D8%AA/",
 "prompt": "What do the Persian dictionaries (فرهنگ عمید Amid, فرهنگ معین Moin, دهخدا) say for آرشیتکت? Quote the entries and any origin tag such as [فرانسوی] or [فر.]."
}
```


## [2026-09-04T23:14:31.740Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%87%DA%A9%D8%AA%D8%A7%D8%B1/",
 "prompt": "What do Persian dictionaries (عمید, معین, دهخدا) say for هکتار? Quote the entries and origin tags (French?)."
}
```


### [2026-09-04T23:14:35.836Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T23:14:39.348Z] TOOL RESULT

```
# Persian Dictionary Entries for هکتار

**لغت نامه دهخدا** (origin: French):
"واحد سطح برابربا ده هزار متر مربع" used for land measurement, especially agricultural areas.

**فرهنگ معین** (origin: French):
"ده هزار متر مربع" — concise definition noting the French origin.

**فرهنگ عمید**:
"واحد اندازه گیری سطح، معادل ده هزار متر مربع" — describes it as a measurement unit equaling ten thousand square meters.

All three dictionaries consistently define هکتار as a surface measurement unit equal to 10,000 square meters, with the Dehkhoda noting its particular use in agriculture and land surveying.
```


## [2026-09-04T23:14:44.811Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D8%A2%D8%B1%D8%B4%DB%8C%D8%AA%DA%A9%D8%AA",
 "prompt": "Is there an entry for آرشیتکت in any Persian dictionary here (عمید، معین، دهخدا)? Quote what is shown, including origin tags."
}
```


## [2026-09-04T23:14:45.230Z] TOOL CALL #50: WebSearch

```json
{
 "query": "\"آرشیتکت\" فرهنگ عمید معماری فرانسوی واژه"
}
```


### [2026-09-04T23:14:49.285Z] TOOL RESULT

```
Web search results for query: ""آرشیتکت" فرهنگ عمید معماری فرانسوی واژه"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T23:14:50.912Z] TOOL RESULT

```
Yes, there are entries for آرشیتکت in multiple Persian dictionaries shown here:

**Amid Dictionary (عمید):**
"شاخه‌ای از مهندسی که به طراحی و ساخت بناها، جاده‌ها، پل‌ها، و تونل‌ها می‌پردازد؛ مهندسی ساختمان؛ مهندسی عمران."

**Moein Dictionary (معین):**
"مهندس معمار، طراح یا مشاور ساختمان"

**Dehkhoda Dictionary (دهخدا):**
The page shows three French architects with the term آرشیتکت in their biographical entries, but does not display a standalone dictionary definition for the word itself.
```


## [2026-09-04T23:15:22.479Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/archaeology",
 "prompt": "Full etymology of \"archaeology\" and, if present on the page, \"archaic\": which intermediate languages (French archéologie, Modern Latin archaeologia, Greek arkhaiologia / arkhaikos) and dates?"
}
```


## [2026-09-04T23:15:23.623Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hectare",
 "prompt": "Full etymology of \"hectare\" and of \"are\" (the metric unit): French, 1795 decree, Greek hekaton, Latin area. Dates."
}
```


### [2026-09-04T23:15:27.553Z] TOOL RESULT

```
# Etymology of "Archaeology"

**Archaeology** traces back through several intermediate languages:

- **Greek**: *arkhaiologia* ("the study of ancient things"), combining *archaeo-* (ancient) + *-ology* (study of)
- **French**: *archéologie* (16th century)
- **English**: The term entered English around 1600 initially meaning "ancient history," with the modern sense of "scientific study of ancient peoples and past civilizations" documented by 1825

The page does not provide etymology for "archaic," though it appears in the alphabetical listing of related dictionary entries.
```


### [2026-09-04T23:15:29.773Z] TOOL RESULT

```
# Etymology of "Hectare"

The term **hectare** originated in 1817 from French, combining Greek and Latin roots. According to the Online Etymology Dictionary, it was "formed from Latinized form of Greek _hekaton_ 'a hundred'" plus "Latin _area_ 'vacant piece of ground.'"

The measurement unit itself was officially established earlier through "decree of the French National Convention in 1795" and represents "a superficial measure equal to 100 ares."

The word's components break down as:
- **Hekaton** (Greek): meaning "one hundred"
- **Area** (Latin): referring to vacant or open ground

This combination reflects the metric system's logical approach to measurement, where the hectare provides a standardized unit for measuring land area.
```


## [2026-09-04T23:15:43.198Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef scan(f,pats,ctx=350,limit=2):\n    try: t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e: print(f,'ERR',e);return\n    for p in pats:\n        print('#####',f,'|',p); n=0\n        for m in re.finditer(p,t):\n            print(repr(t[max(0,m.start()-ctx):m.start()+ctx])); n+=1\n            if n>=limit: break\n        if n==0: print('  (none)')\nscan('IEC.txt',[r'\\basa\\b.{0,40}ash',r'ās-',r'arkh',r'ardēre',r'ārea'],250,2)\nscan('incoming/WLD/WLD_Bd1_pages.txt',[r'brennen,\\s*glühen',r'Asche.{0,30}Staub',r'\\bāreō',r'ära\\b'],400,2)\nEOF",
 "description": "Grep Mann IEC and Walde-Pokorny Bd1"
}
```


### [2026-09-04T23:15:45.275Z] TOOL RESULT

```
##### IEC.txt | \basa\b.{0,40}ash
  (none)
##### IEC.txt | ās-
'cf. jaru! ‘come on; Latv. jarëties ‘rave’. See next, and cf. R jarit\'sa, refl. ‘rave’\niáros, is ‘uproar, violence’. Slav. forms am- big. Cf. jaro, ior-. WP I, 197 OCS jarð ‘violent’; R jàryj ‘irate’; cf. ant, v. ‘provoke’; Latv. jāris ‘din, uproar’\niās-, sigmatic variant of theme iā- ‘go’ Skt. cf. á-yāsişam, 3s: á-yāşīt, impf. "went: OCS jaxavü “having departed’; jaxati, v. ‘go, ride’; Latv cf. jāšus, adj. ‘riding’\niät- “power, force’ Skt. yàtüh ‘sorcery; demon’; Av. yātus “magi- cian’; yātu ‘de'
'ff ‘quick, keen; secure’; m. pl. -au ‘clasp, cramp’; craffu, v. ‘secure, grip’; Cor. crafa, v. ‘grip’; crāf, adj. ‘tenacious’; s. pl. crafow "basting-stitch"; cf. crefny, adj. ‘grasping, gree- dy’; OE hrespan ‘strip, despoil’; hresp ‘spolia- tion’ krās- (?) ‘glory, praise’ ON hrósa, v. ‘praise’; hrósan, f. ‘praise; boast- ing’; hræsni, f. id.; mod. Icel. hrós, n. ‘praise’; OCS krasa ‘beauty’ (and com. Sl.); Latv. cf. krāšns \'splendid\'. See Supt. K : krās- (krast-, see karst-). Variant in W cras '
##### IEC.txt | arkh
"v. cf. arajs\narotrom, see arátrom; arotos, see artos\narg- (?) “cut, destroy Hitt. cf. arghi, ark- ‘cut; arkamas ‘tribute’; Ir. argaim, airgim, argnaim ‘plunder’; argain, s. ‘plunder’. Cf. porg-\narghos, à “point, tip” Arm. cf. arg- (px. *first-); Gk. arkhé; arkhós; OCS cf. razínü ‘goad, awl, *roasting-spit'; OCz. rožen ‘spit’. Uncertainly also Mir. arg ‘outstanding’, s. ‘champion’; Gaul. argo-\nar2ntom “white metal, silver’. WP I, 82. Cf. arĝos Skt. rajatám; cf. also rajatah ‘silvery’; Av. ərəzatə"
"arajs\narotrom, see arátrom; arotos, see artos\narg- (?) “cut, destroy Hitt. cf. arghi, ark- ‘cut; arkamas ‘tribute’; Ir. argaim, airgim, argnaim ‘plunder’; argain, s. ‘plunder’. Cf. porg-\narghos, à “point, tip” Arm. cf. arg- (px. *first-); Gk. arkhé; arkhós; OCS cf. razínü ‘goad, awl, *roasting-spit'; OCz. rožen ‘spit’. Uncertainly also Mir. arg ‘outstanding’, s. ‘champion’; Gaul. argo-\nar2ntom “white metal, silver’. WP I, 82. Cf. arĝos Skt. rajatám; cf. also rajatah ‘silvery’; Av. ərəzatəm; Ober"
##### IEC.txt | ardēre
  (none)
##### IEC.txt | ārea
  (none)
##### incoming/WLD/WLD_Bd1_pages.txt | brennen,\s*glühen
  (none)
##### incoming/WLD/WLD_Bd1_pages.txt | Asche.{0,30}Staub
'nubs „zu\nviel gebogen“, knubuls „etwas zusammengeballtes“, nisi, hnypra sig saman\n„sieh zusammenkauern“, Imypur „kauemde Stellung“ (Wood aaO.).\n\n\n2.  qen- „kratzen, schaben, reiben“, gene -, qenei-, qeneu-; vielfach mit\n      kons. Erw. zusammenfassend Persson Beitr. SOS f., 8811. (sehr vieles\n                          ;\n\n\n      schon bei Johansson PBrB. 14, 332ff.).\n   Gr. xovtg, -tog f. „Staub, Asche“ (-is-St., vgl. xovia-aalog „Staubwolke“,\ny.exovia-xai Theokr., y.ovtm „bestaube“ aus *y.ovio-ia> hom. xovirj „Staub,       ,\n\n\nSand, Asche u aus *xovtad), abl. mit lat. cinis, -eris f. m. „Asche“ (aus\n*cenis Sommer IP. 11, 328), Dimin. tin is-culus (s. Danielsson Gramm, und\n          ,\n\net. St. I 51  ;\n               nicht idg. -os nach Bartholomae BB. 17, 113; nach Brugmann\nII 2 1, 533 f. '
##### incoming/WLD/WLD_Bd1_pages.txt | \bāreō
  (none)
##### incoming/WLD/WLD_Bd1_pages.txt | ära\b
  (none)
```


## [2026-09-04T23:15:55.270Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nfor p in [r'azg[oö]',r'ask[oö]n',r'Malzdarre',r'azazim',r'trocken.{0,40}ausgedörrt',r'Altar']:\n    print('#####',p); n=0\n    for m in re.finditer(p,t):\n        seg=t[max(0,m.start()-900):m.start()+700]\n        pg=re.findall(r'\\[pdf page (\\d+)\\]',t[:m.start()])\n        print('  page tag:',pg[-1] if pg else '?')\n        print(repr(seg[-1300:]))\n        n+=1\n        if n>=1: break\n    if n==0: print('  (none)')\nEOF",
 "description": "Find Walde-Pokorny as- entry"
}
```


### [2026-09-04T23:15:57.542Z] TOOL RESULT

```
##### azg[oö]
  page tag: ?
' „glanzen“ bemerkte).\n     Auch ai. qdtrn- m. „Besieger, Feind, Nebenbuhler" mit Reihenwechsel?\ns.   Hirt    BB 24, 232, 285, der andrerseits nach Fick 1 4 43, 425 an ai. gu-\ntayatietwa „haut ab, haut zusammen, wirft nieder", gr. y.evTsco, lett. situ,\nsist„schlagen" als Yerwandte denkt, von denen aber y.evzko jedenfalls\nauszuscheiden hat (s. kent- „stechen“), wahrend lett. sit- als *ke t- und ai.\nf Citayati\n        ( catru-1) eher vereinbar wiiren.\n                   :                        Ganz unsicher vermutet   —\nSolmsen KZ. 34, 687 Yerwandtschaft auch des thrak. Yolksnamens der\nKazQai, Kazgoy.evzat.          —\n                          Ob in gr. oazivg „Streitwagen“, odztXXa\' ziXeidg zo\naoxgov, die als pliryg. AYorte mit arm. scujl „AYagen“ (arm.-phryg. *satilia )\nzusammenlhingen, die Bed. des „Streitwagens die urspriingliche ist, ist\nsehr fraglich, s. Liden aaO. 159ff. — Uber arm. Jcotor „Bruchstiick“ s. u.\nqentho- ,,Lappen“.\n     Ygl. Fick I 4 43, 425, II 66 f., Ill 4 69, Zupitza Gutt. 184, Berneker 588.\n     Gr. y.ozog „Groll, Zorn", das dem a und dem Begriff des Tatlichen der\nobigen AYorte sich nicht          fiigt, sekeint zu koi „wetzen“ zu gehoren. Auf                 —\nBthl.’s AVb. 177          Anreihung von avascasto fravasi- etwa „der die Frava^i\nerziirnt hat" ist'
##### ask[oö]n
  (none)
##### Malzdarre
  (none)
##### azazim
  (none)
##### trocken.{0,40}ausgedörrt
  (none)
##### Altar
  page tag: ?
's DrauBen“, daneben fem.\ndra     ein   idg. * aro-m pi. draan, dazu lok. flre\'i. Dieser Lok. soli in ai.\ndre „in        Ferne“ (dazu urdd „aus der Ferne“) vorliegen. Lat. fire-\n              die\n„freier Platz; Dreschtenne“ sei aus dem lok. *drci           a gebildet. Aber\nlit. oras gehort zu drti „pflugen“, lett. dra „Ackerfeld“.\n\n    Ahd. arin, erin „FuBboden“, mhd. ern „Hausflur, pavimentum“ ist Lehn-\nwort aus lat. arena (Kluge, Pauls Grdr. I 2 334\'. Die Zusammcnstellung\ndes idg. *Ciro- mit ascliw. cerin, arin „Herd“, aisl. arenn „Erh6hung, IIerd“,\nfinn.-urn. arina „Herd“. ahd. arin, erin „ Altar\' ist wegen der Bedeutung\nfernzuhalten. s. unter fis- „ausdorrende Gluthitze".\n\n\naro-ra „Schilfrohr ‘?       1,\n\n\n\n\n  Gr.       ugov     „Katterwurz, Art Schilfrohr",                     dgi-oagov       „eine    kleine         Art\ndavon“\n                     u\n  lat. harundo „Rohr                  z.   B. Yanicek        LEWb. 2 20 m. Lit.;               zur    Bildung\nvgl.   nelrmidincs     :   ve<pool,   Fick    GGA. 1894, 231, BB. 23, 222                  .\n\n\n\n  Das von Persson De orig. gerundii 59 der AnschluB an *rr-, *nr- „be-\n                                                              i\n\n\n\n\nwegen“ sucht) angereihte lat. arista „Hachel, Granno an der AlmY, uristis\n„holcus“ unterl'
```


## [2026-09-04T23:16:05.091Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'ausd[oö]rrende',t):\n    pg=re.findall(r'\\[pdf page (\\d+)\\]',t[:m.start()])\n    print('page tag',pg[-1] if pg else '?')\n    print(repr(t[max(0,m.start()-200):m.start()+2200]))\n    print('#########')\nEOF",
 "description": "Print Walde-Pokorny as- entry"
}
```


### [2026-09-04T23:16:06.994Z] TOOL RESULT

```
page tag ?
"auch der Yergleich von avasa- mit dem darnach auf *auesia zuruckgefiihrten\ngr. rjia, zuletzt Bechtel Lexil. 152; Ygl. iiber dieses noch unklare gr. Wort\nsonst noch Thumb KZ. 36, 179 f. und dazu *<is „ausdorrende Gluthitze“ und\n*ei „gehn“).\n\n\nauq n (h)- uqS(h)- und daneben wohl als andere Hochstufe ueq”(h)- (vgl.\n                :\n\n\n\n\n         nig-\n         (          :   ueg-, altest atieg-) „Kochtopf,             Warmepfanne“.\n   Lat. aulla, aula, alia „Topf, IIafen“, Demin, auxilla (osk. itlam „olIam“\nlat. Lw., fal. olna im Ausgang nach urna    lat. aulla trotz Thurneysen Thes.\n                                                                    ;\n\n\ns. v., IF. 21, 177, Solmsen IF. 31, 474 Anm. 1 nicht als *aul-ela zu gr.\nat'/o?, lat. alvus, alveus)-, wahrscheinlich alb. ane f. „Gefafi“ (aus *auq'i-na;\nJokl SBAk. Wien 168, I 3); ai. ukhd- m., ulclid „Topf, Kochtopf“; got.\nauhns „Ofen“, mit gramm. Wechsel anorw. ogn, aschvred. oghn ds. lit.                        ;\n\n\n\n*aulcsinis „Rauchkamin“ gibt es nicht (von Bezzenberger BB. 23, 315 mit got.\nauhns verbunden Meringer am u. a. O. will es richtig in auksfinis andern,\n                                    ;\n\n\n„der hohe“. Als verschiedene Gruppe lost Bezzenberger nicht iiberzeugend\nuhltd, aulla ab unter Yerbindung mit lit. auk sly s „Tute oder Schachtel\naus Birkenrinde“ Meringer halt auch letzteres wegen der Ahnlichkeit mit\n                                    ;\n\n\nGefaBformen fur mit unserer Sippe vereinbar; sehr zweifelhaft).\n   Daneben Formen mit vrohl erst einzelsprachlichem Labial: gr. Invog\n„Ofen“ (nach Fick III 4 29 zw., Ostir Wus. 5, 217, Giintert Abl. 25 aus\n*ueq“-nos; nicht          s. Boisacq m. Lit.);  ags. ofnet „kleines Gefa6“,\nofen, ahd. ovan, anord. ofn „Ofen“ (ebenfalls auf u e q’inos zuriickfiihrbar;\ndas anl. u- bewirkte wie in wulfa- „Wolf'‘ die Entwicklung von -h- zu\n      wahrend got. usw. auhns auf idg. iiq'i-nos zuriickfiihrt; der Yerlust\ndes w- in Ofen muB dann allerdings aus EinfluB dieser Schwesterform\n*alma- erklart werden). Aus der assimilierten Form aschwed. omn, mdartl.\numn „Ofen“ ist wohl apr. wumpnis „Backofen“, umnode „Baekhaus“ ent-\nlehnt. S. J. Schmidt KZ. 22, 192, Zupitza Gutt. 5 f. 71, Meillet Msl. 9, 137      1\n\n\n(Meringer IF. 21, 292 ff,, Feist Got. Wb. 37) Senn, Germ. Lw.-Studien,\n\x0c                           ;\n\n\n\n\n                                               aug     aulo-s ("
#########
page tag ?
' Zusammcnstellung\ndes idg. *Ciro- mit ascliw. cerin, arin „Herd“, aisl. arenn „Erh6hung, IIerd“,\nfinn.-urn. arina „Herd“. ahd. arin, erin „ Altar\' ist wegen der Bedeutung\nfernzuhalten. s. unter fis- „ausdorrende Gluthitze".\n\n\naro-ra „Schilfrohr ‘?       1,\n\n\n\n\n  Gr.       ugov     „Katterwurz, Art Schilfrohr",                     dgi-oagov       „eine    kleine         Art\ndavon“\n                     u\n  lat. harundo „Rohr                  z.   B. Yanicek        LEWb. 2 20 m. Lit.;               zur    Bildung\nvgl.   nelrmidincs     :   ve<pool,   Fick    GGA. 1894, 231, BB. 23, 222                  .\n\n\n\n  Das von Persson De orig. gerundii 59 der AnschluB an *rr-, *nr- „be-\n                                                              i\n\n\n\n\nwegen“ sucht) angereihte lat. arista „Hachel, Granno an der AlmY, uristis\n„holcus“ unterliegt wegen seines zu ycnista u. dgl. stimmenden Suffixes\nstark       dem Yerdachte        etruskisch zu sein               s.   Herbig IF. 37, 17!,       1   7S   \'.\n\n\n  Aus einer Mittelmeersprache?\n\x0c              ,\n\n\n\n\n80                                                             ario-      — ark-\n\nario- „Herr, Gebieter“.\n     Ai. dry a „Herr, Gebieter“, Cirya „Arier“, ary aka „ehrwiirdiger                                                           Mann“;\n                                                          Ll\nav. criryo                            Ario-manus (CIL. Ill 4594); ir. aire\n                       apers. ariya „ariseh                    ;\n                                                                   gall       .\n\n\n\n\n(^gl. priraas gen. airech wo *arjak- oder *arjak- anzusetzen ist, welches\n                       ,                          ,\n\n\nsich zu ai. tiry aka verhalt wie gr. iidoai   Jiingling“ zu ai. marjaka-                      ,,\n\n\n\n „Mannchen“ Pedersen Kelt. Gr. II 100    Dagegen gehort mir. mire nicht               .\n\n\n\nhierher, sondern aus ro -j-                           n ,,Gro8konig u                     .\n\n\n\n  Hierzu ai. aryamd „Gefahrte, Freund; Name eines Gotten \', av. airya-                                              1\n\n\n\n\nman- „folgsam npers. ermdn „Gast“.\n                                 1£\n                                      ,\n\n\n  Ygl. Fick I 4 168.  II 4 19.   Uklenbeck Ai. Wb. 14.\n  Ir. Airem, gen. Airemon      Eremon „einer der sagenhaften Stammvater\n                                      '
#########
page tag ?
'                                                      :\n\n\n\ngleicben.  Unbefriedigende Deutungen von uaig verzeichnet Yf. LEWb. 2\n699, Boisacq 87 ; asitu- kaum zu cLsa-h „Staub, Asche‘‘,   s.   *fis- „ausdorrende\n\nGluthitze“.\n\n\nnsis „Schwert‘\\\n  Ai. asi-h „Schwert, Schlachtmesser* ; av. atahu- ds. ; lat. ensis „Schwert’‘.\n  Uber weitere Anknupfungen siehe die Gruppe unter ens-.\n                                                                            ;\n  Gr. cioo   ist   nicht *nsor, sondern gehort zu gr. ueioco „hebe‘             (Prellwitz\nWb., Boisacq Wb.).\n  Zu arm. sur „Schwert“ vgl. Liden Arm. St. SO, al.\n\x0c                                                                     K.\nqa- ,-gern haben, begehren“.\n    Ai. kdyamana- ,.gern habend“ a-lcctytya „begehrenswert" mit aus diesem\n                                                             (\n\njo-Praesens verschlepptem -y-, daher keine Stiitze fiir einen Wzansatz\n*qai-, s. Persson Beitr. 574 gegen J. Schmidt Krit. 53, Wackernagel Ai.\nGr. I 15), Pf. cake „sich woran erfreuen, zu gewinnen. suchen, lieben,\nbegehren“, -kati- (in Zs.) „heischend, verlangend"\'; av. ka- „wonach ver-\nlangen“ (kayo. 1 sg., kata-, cakuse Bartholomae Airan. Wb. 462); -wo-St.\n                               .\n                                                                 ;\n\nai. kama- m. „Begehren, Wunscb, Liebe“, av. ap. kama- m. „Yerlangen,\n\nWunsch“, woraus nacb Bartholomae Airan. Wb. 462, 463 die ai. Wz. kam-\nerst sekundar entsprungen ware (Rgv. Prs. kdmayati, PPfMed. cakamand -\ndann kamra- „reizend, schon“, kamana- „begierig, liistenY) doch seheint                         ;\n\nlit. kamaros  „Geilheit“ (Nesselmann, Leskien Nom. 447) und lett. kdniet\n„hungern“ (Endzelin KZ. 44, 63) die Anfange dieser Entwicklung bereits\nin altere Zeit binaafzuriicken\n   ro-St. lat. cams „lieb, wert, teuer (auch vom Preise)“, lett. Mrs „liistern,\n               1\nbegehrlich (kdruot „begehren, verlangen“), got. hors „Ehebrecher, Hurer“,\n                   \'\n\n\n\n\naisl. horr ds., hor n. „Buhlerei, Unzueht", ags. lwr n. ds., abd. liuor n. ds.,\n\nahd. lmora (und Imorra aus *horion-) „Hure“, ags. hdre, aisl. h ora ds. (siehe\nauch Falk-Torp   u. hor; die germ. Worte nicht nach Siebs Mitteilungen\n         Ges. f. Volkskunde Hft. 11, S. 5, Anm. 3 des S. A. zu abd. lioro\nd. schles.\n\n„Schmutz“) reduktionsstufig gall, Carant-us. -Ulus usw., abrit. Carant-lnus,\n  '
#########
```


## [2026-09-04T23:16:17.089Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nidxs=[m.start() for m in re.finditer(r'Gluthitze',t)]\nprint(len(idxs))\nfor i in idxs:\n    print('----',repr(t[i-120:i+120]))\nEOF",
 "description": "List all Gluthitze mentions"
}
```


### [2026-09-04T23:16:19.104Z] TOOL RESULT

```
3
---- ' Bechtel Lexil. 152; Ygl. iiber dieses noch unklare gr. Wort\nsonst noch Thumb KZ. 36, 179 f. und dazu *<is „ausdorrende Gluthitze“ und\n*ei „gehn“).\n\n\nauq n (h)- uqS(h)- und daneben wohl als andere Hochstufe ueq”(h)- (vgl.\n                :\n'
---- 'rd“,\nfinn.-urn. arina „Herd“. ahd. arin, erin „ Altar\' ist wegen der Bedeutung\nfernzuhalten. s. unter fis- „ausdorrende Gluthitze".\n\n\naro-ra „Schilfrohr ‘?       1,\n\n\n\n\n  Gr.       ugov     „Katterwurz, Art Schilfrohr",                     '
---- 'en von uaig verzeichnet Yf. LEWb. 2\n699, Boisacq 87 ; asitu- kaum zu cLsa-h „Staub, Asche‘‘,   s.   *fis- „ausdorrende\n\nGluthitze“.\n\n\nnsis „Schwert‘\\\n  Ai. asi-h „Schwert, Schlachtmesser* ; av. atahu- ds. ; lat. ensis „Schwert’‘.\n  Uber wei'
```


## [2026-09-04T23:16:27.529Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=re.split(r'\\[pdf page (\\d+)\\]',t)\n# pages: [pre, num, text, num, text...]\nd={}\nfor i in range(1,len(pages),2):\n    d[int(pages[i])]=pages[i+1]\nprint(sorted(d)[:5], len(d))\nfor pg in (76,77,78):\n    if pg in d:\n        print('==== pdf page',pg,'====')\n        print(d[pg][:2600])\nEOF",
 "description": "Print Walde-Pokorny Bd1 pages around 68"
}
```


### [2026-09-04T23:16:29.399Z] TOOL RESULT

```
[] 0
```


## [2026-09-04T23:16:32.461Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 400 incoming/WLD/WLD_Bd1_pages.txt && echo && grep -o -m3 '\\[pdf[^]]*\\]' incoming/WLD/WLD_Bd1_pages.txt | head",
 "description": "Inspect WLD Bd1 page tags format"
}
```


### [2026-09-04T23:16:32.529Z] TOOL RESULT

```
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

               CENTRAL
            ARCHEOLOGICAL
                LIBRARY
ACCESSION NO. jj03?7
CALL No. gJ3 Wafjpok
                 f_
D.G.A. 79
                      ALOIS WALDE


VERGLEICHENDES WftRTERBDCH
                                DER


     INDOGERM ANISCHEN SPRACHEN

                HERAUSGEGEBEN UND BEARBEITET
```


## [2026-09-04T23:16:36.326Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('leaves',len(leaves))\nfor i in (76,77,78):\n    print('==== leaf',i,'====')\n    print(leaves[i][:2200])\nEOF",
 "description": "Print WLD Bd1 leaves 76-78"
}
```


### [2026-09-04T23:16:38.340Z] TOOL RESULT

```
leaves 895
==== leaf 76 ====
68                                          atis-   — ansa, ansi-
  Alb. endet. „Bliitenkelch, Blume des Weins; Freude, Annehmlichkeit”,
das G. Meyer BB. 8, 188 angereiht hatte, stellt derselbe Alb. AVb. 5 unter
einer Gdf. *anja = aksl. vonja „Duft“ zu *an- „hauchen“.
     Nicht zu gr. avg voder           (s.   *medh-, endh- „gehn, hervorkommen”).

ans- „wohlgeneigt, giinstig sein“.
     Got. ansts, ahd. anst und (tiefstufig) unst, ags. est „Gunst, Gnade“, anord.
cist,  qst ,,Gunst, Liebe“, ahd. abnnst, abunst, as. avunsf, ags. cefest „Abgunst,
Ungnade”; mhd. gund m. „Gunst“, anord. of-und ,,Ungnade“; Praeterito-
praesens ahd. an, unman (Inf. unnan Praet. onsta onda ) „gonnen“ {gi-un-
                                                          ,                          ,


rnn), as. ags. unnan „gonnen, einraumen, wiinschcn“, anord. unna (ann,
unnom Praet. unna aus *unpa) „lieben, gonnen, einraumen”.
            ,

   un-nu-m 1st ein altes Praes. der neu-, m^-Klasse, wozu der neue Sg.
ann. AVer die AVz. als grm. an-, un- ansetzt, hat in ansts die Suffixver-
bindung -s-ti- zu sehen (s. Brugmann Grdr. II 2 2, 437), wahrend mhd. gund,
an. ofund das einfacbere -ti- enthielten.     Doch ist wegen des gemein-
germ. anst(s) die AVz wo hi als grm. ans-, tins- anzusetzen (Kluge ZfdtAVtf.
                               .




9, 317, Brugmann Grdr. II
                             2
                               3, 332), unnum mithin aus *unz-num (idg. *ns-
nu-me) entstanden, wonaeh dann Sg. ann, und das neue schwache Praet.
*un-pa (ahd. onda anord. unna) neben ahd. onsta, as. gi-onsta-, auch mhd.
                           ,


gund, anord. qfand sind dann Neuschopfungen nach dem s-los gewordenen
unnum, unnan.
     Auch gr. 7iooa-gvy)g „freundlich“, du-gvr'jg „unfreundlich, hart“ (: ab-unst) ist
am wahrscheinlichsten = V-rpo?-, an-avag c (s. Pick BB. 1, 242, Brgm. aaO.).
     In     abweichender
                      formaler Beurteilung bezieht Bechtel Lexil. 49 gr.
-avt'/g auf ein neutr. Subst. *dnos dessen suffixale Tiefstufe dem germ.
                                                     ,


*an-s-ti- zugrunde liege.       gvgg nicht zu ai. ananam „Mund, Antlitz“
(s. *an-
==== leaf 77 ====
  Ai. amsadhrt „Gefat! mit Henkeln" enthalt vielmehr amsa-h „Schulter‘                                                   :




im Sinne von „vorstehender Henkel“ (s. Fick I 4 aaO., Yf. LEWb. 2 u. ansa,
Ernout Bull.      soc. lingu.     Xo. 59,             S.   LXIII).     — Idg. *unsa, *ansi- vielleicht
als „Schlinge        zum Fassen“ zu *am- „fassen“, so daS eig. *ainsa auf Grund
eines cs-St. *ames-  auch das Lit. widerspricht
                            ;                                                dem nicbt,                 s.   zuletzt Pers-
son Beitr. 4f., Hirt IF. 37, 224 f.


1. ar-,   themat. (a)re-, set-Basis (a) re- und i-Basis a)rei- (entweder aus dem
                                                        (
     ?o-Praes. *(ri)re-ip entwickelt, oder urspriinglich, so daB *(a)rc- vor-
     konsonantische Entwickluug daraus) „ftigen, passen“, mehrfach und
     vielleicht altest void planmafiigen Aufeinanderlegen beim Holzbau (auch
     Steinbau?? Meringer IF. 17, 124) und vom Aufstapeln von Rolzern,
     aber auch vielfach auf geistiges Zurechtlegen, Berechnen fibertragen.
     Ausffihrlich bes. Persson Beitr. 632 f., 666, 741 f., 856.
   Av. arante „sie setzen sich fest, bleiben stecken‘ ai. ara-h „Radspeiche“,  !

                                                                                   ,

aratn Adv. ( dramkar „zurechtmachen' und „dienen“, wozu wohl ara-ti-
                                                             £



„Diener“ und ra-li, s. unter *ere- „rudern“) „passend, genug“, av, aram
„passend, entsprechend“ ( aram-pi&icd „Mittag“ = die zum Mahle passende
Zeit“, woneben ra-pi&wa ds. mit schwundstufigem ru- neben *ara-, wovon
nrom Adv., Bartholomae Airan. Wb. 189, 1509); ai. ar-p-ayati „steckt
hinein,   befestigt“        (dasselbe           -p-   auch       in   gr.   agnsdovy          „Seil,         Strick   zum
Befestigen des Panzers, zum Fangen“?? s. Boisacq 81);
  arm. arnem „mache“ (Hiibschmann Arm. Gr. I 420), y-ar „consentaneo,
congiunto, contiguo, appresso", wovon yarem „aggiungere, congiungere"
(Bugge KZ. 32, 21), i;ar „schlecht“ (mit negativem 6~or „nicht passend"
Bugge aaO. 23);
  gr. agagtoxa),  doaga „fiige zusammen" 
==== leaf 78 ====
                                                                          -                                                 ;




70                                                                  ar-



aaO.  in gr. eiQtjvt], dial, ioava ioyva „Friede“, dob] „Yersammlungsort“,
                                                             ,


lakon. \gyv, -evos (Akzent unsicher) von Jiinglingen, die aus den Knaben-
klassen ausgetreten waren, etwa „der Taugliche“ (auf Grund eines *lga
„Tauglichkeit,                         d.gezy“,       Igeeg „dotoreig“        (vielleicht   auch   att.   f Igsoicdv)]   „ein
geschmiickter Zweig“ als Sinnbild der agezy yijg, des Gelingens der Ernte?);
unsicher,                   s.    Kretschmer Gl. 10, 238 f.
      „   .   .   .   es gibt einige Stellen im RV.,                          wo Jr- der Bed. nach eher zu dram,
agagtoxco als zu rnoti, oovvpi stimmt                   iiberdies ist vielleicht auch gthav.
                                                                     .   .


Jra-          n.,         Bartholomae Altiran. Wb. 372, nicht an Irafu, uz-lrah -, sondern
an ardm               ,
                           arante anzuschliefien, vgl. Scheftelowitz ZDMG. 59, 693“ [der aber
Jra- als „Schar“                    mit air. tall „Trupp, Herde“, lit. eile „Reihe, Schicht“
vergleicht; fur letztere steht                              ei-   „gehn“       als   Wz. zur Erwagung],
      Mit Zerdehnung opr]oos „Gatte; Geisel, Unterpfand", ourjor.co „treffe zu-
sanimen'''.
      Aus dem Slav, vielleicht poln. ko-jarzyc „kniipfen, verbinden, vereinigen“
(z.B. Miklosich EWb. 100, Berneker 31, 532).
   Uber das vielleicht verwandte gr. doa, lit. ir s. *ar „nun, also".    Zur                                        —
Bed. „Fuge — Gelenk, Glied" ( ao&oov) vgl. auch u. die Worte fur „A.rm“. Da-
gegen bleiben trotz Persson Beitr. 634 f. besser bei der Sippe von cbtevt]
die Worte ai. aratni-h   ratni-li „Ellenbogen, Elle, Arm“, Ctni-h „der un-
                                                  ,


mittelbar liber dem Knie liegende Teil des Beines“ (mind, aus *arni-
die Bed. ,in der Nabe laufender Achsenzapfen         beweist nicht fur Ye
```


## [2026-09-04T23:16:49.008Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r'azd-|azgh|Malzdarr|aska.{0,30}asce|Esse',l):\n        print('==== leaf',i,'====')\n        print(l[:2500]); print('...')\n        break\n# also list leaves mentioning 'Asche' and 'lat. ara'\nfor i,l in enumerate(leaves):\n    if 'Asche' in l and re.search(r'ara\\b|ära',l):\n        print('#### candidate leaf',i, l[:80].replace('\\n',' '))\nEOF",
 "description": "Find WP as- entry by other keywords"
}
```


### [2026-09-04T23:16:50.691Z] TOOL RESULT

```
==== leaf 10 ====
                     :   g                                                                            .                                                                       '




2                                                                                   ai-to-, ai-ti-        —   ai-




(Uklenbeck Got. Wb. s. v.) die vielleieht mit gr. alvog m. ..bedeutsame Rede,
Lob, zustimmender Zuruf der Yolksversammlung aTvt] ..Ruhm ", aiveco sage,                                             ",
                                                                                                                                                                      .




       airmofiat rede in Ratseln, deute dunkel an aXviypa dunkle Rede
         !
lobe         ',                              .                                                                                                              .




unter einer Basis *ai-, *i- ..bedeutsame Rede" zu vereinigen sind. dvaivo-
fiai v sage nein, verweigere“ (s. iiber letzteres Bechtel Lexil. 43, und, sowie
liber aho     auch Prellwitz 38     die Form dmjvtjvavio Horn, spricht gegen        —
alten Diphthong; es ist also gegen Osthoff [BB. 24, 199 ff.] vielmehr mit
Stolz [Wiener Stud. 25, 133 ff.] als /o-Ableitung der Negation av- zu be-
trachten) bleibt fern.
      tiber         dt.           Eid usw. s. u. ei-                                     .   gehen".
      S.          auch        *ai-to~, ai-ti- „Anteil“.                                         — -Fick 1 4 113.


ai-to-, ai-ti- .Anteil", vermutlich                                                              nach Fick I 4 345 zu ai- ..packen" (..das,
             was jeder an sich rafft ).
      Gr. aioa (*ahm)                                  .   Anteil, Schieksal", horn, toy, besser                                                       I'ooy    ,.der gebiik-
rende Anteil                       ',
                                            I'ooaodai         ‘
                                                                          y.hjoovodac. Aeothoi Hes.                        ;       ai’oiog              .
                                                                                                                                                            gutes Geschick
verheifiend, giinstig    cuoiiiog ..yom Schieksal bestimmt, gebiihrend ', avcu-
at,u6co,.amvenden, gebrauchen, verzehren" (s. dazu Boisacq 59, Fraenkel
KZ. 42, 236), aiovf.iva.co 
...
#### candidate leaf 120                                                                                 
#### candidate leaf 436                                                     -                      -    
#### candidate leaf 455                                   q e la°o-, qelejo   —    kelb-, kelp-         
#### candidate leaf 471                          korka (kroka?)    -ela   — kormno-, krmno-
```


## [2026-09-04T23:16:56.778Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nl=t.split('\\f')[120]\ni=l.find('Asche')\nprint(l[:120])\nprint(repr(l[max(0,i-2000):i+1500]))\nEOF",
 "description": "Print WLD Bd1 leaf 120"
}
```


### [2026-09-04T23:16:58.474Z] TOOL RESULT

```
                                                                                                      )




112         
'                                                                                                      )\n\n\n\n\n112                                                                  ek-{?),            eko\n\n\nmit     gramm. Wechsel anord. eim-yrja,                                                 ags.      cem-yrie             (engl.   embers), mhd.\neimer(e)         f.,   nhd.            mdartl.           ammer            „gliihende Asche‘\n                                                                                                              :\n\n                                                                                                                  ;\n                                                                                                                       norw.        mdartl.         orna\n„warm werden“ (* nznUn                          ;\n                                                        s. nock Falk-Torp u. oret                         ;\n                                                                                                              vielleicht als „brennend,\nhitzig   = eifrig" hierher sehwed. yster „sehr lebhaft, unbandig\'                                                                   1\n\n                                                                                                                                        ,\n                                                                                                                                            ahd. ustar\n                                                                                                                                4           4\n„gierig, gulosus“,                         ustrl „industria“,                     ustinon „fungi“ (Fick I                           360, III 32;\nlat.   industrius ist aber endo-struos).\n      Curtius 398;                      nacb Fick I 4 7, 360, Pre'
```


## [2026-09-04T23:17:11.998Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef scan(f,pats,ctx=400,limit=1):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for p in pats:\n        print('#####',f,'|',p); n=0\n        for m in re.finditer(p,t):\n            print(repr(t[max(0,m.start()-ctx):m.start()+ctx])); n+=1\n            if n>=limit: break\n        if n==0: print('  (none)')\nscan('IEC.txt',[r'as-.{0,10}burn',r'āsos|āsā|asos.{0,30}ash',r'azd-'],300,2)\nscan('SYN.txt',[r'ASHES',r'Ashes',r'1\\.85'],400,1)\nEOF",
 "description": "Grep Mann and Buck"
}
```


### [2026-09-04T23:17:13.672Z] TOOL RESULT

```
##### IEC.txt | as-.{0,10}burn
  (none)
##### IEC.txt | āsos|āsā|asos.{0,30}ash
" ern; ON annir; OCS jeseni; R Óseni; OPr. asanis\nasnu-mi (asneu-) ‘do, work, achieve” Hitt. asnumi “prepare, supply, serve’; Gk. á- nümi beside ánuo, ånd; but cf. sanu-mi; Lat. cf. (?) in-anis (Cineffectual', etc.); Go. cf. asneis ‘labourer’; OHG asni; OE esne; OSax. asna ‘pay’; OFris. esna “to pay\nāsos, à ('as-) ‘hearth, sacrificial altar’. Cf. as- Hitt. hassas; OLat. asa; Lat. āra; cf. Umb. aso, Praen. asom (pp. “burnt')\nas'r, see es'r\naster-, see oster-\nastlā (?) ‘floorboard’. WP I, 84 Lat. astla, astula (LWs in W astell *board, shingle' (?); OE æstel-); Li. aslà “floor”\nat, ati towards, ag"
"er, tie, join, link'. Cf. WP I, 771 & 802 Skt. dasmáh ‘spellbinding’, Arm. (?) ávan, čvanea “string, rope’; Myc. desomo- (desmo-); Gk. desmós ‘latch, fetter; désma, id. cf. désme ‘bundle; MHG zésem, zësen “line, row, series’; ON tjasna, f. ‘peg\ndeso “seek, find, arrive, happen’. WP I, 814\n143\nSkt. dāsāmi ‘pursue’; Gk. déo ‘shall discover’: Li. cf. dëstis, f. and dēsnē, f. ‘surprise oc- currence’\ndesuos (dues-) “evil, harm’; desuð, io (du- esó, ið) 'injure'. Cf. WP I, 782 Gk. déos, gs déous & deíous “fear, danger”; deinós ('terrible', fr. *desuino- or *duesino-); OE teosu ‘harm, wrong, calumny’"
##### IEC.txt | azd-
"bele ‘noble’; OHG edili; Go. as proper name Athala; cf. OHG adol ‘nobility’; ON cf. eðli, oðli, n. ‘nature, origin’. (For OHG uodal, OE opel ‘homeland’, see auos, ios and tol-)\nati, ati- see at, at- and cpds. below\nati-ag0 (ti-ag0) ‘go away’. Cf. at, ati, a0 Skt. tyajāmi ‘abandon, avoid”; Av. cf. syazd- ‘flee’; Olr. ti- agaim, Ir. tiaghaim, téighim ‘go’; beside aith-ighim “return”\nati-8en- Sk. ati-anam ('(remoteness', lit. ‘beyond men’); OE cf. ed-cennan, v. ‘to regenerate’; Ir. cf. aith-ghein “symbol? beside aith-gheana- mhain ‘regeneration’; W adian ‘offspring’. For Go. id-, OHG it- and ON i"
" *purt-); R bzdét, Pol. bzdziec, Cz. bzdít “fart”, beside Cz. bat ‘hum’, exten- sions in Pol. bzyczeC, Cz. bzičet (hum, fr. *bzeukijo?). The simplex occurs in Cz. bzed ‘fart’, bzdy ‘arse’, and in Cz. bez, Pol. bez, bezd, Srb. báza “elder; Lith. dial. bizdas *arse; bustle'. A variant occurs in Srb. bazd- jeti ‘stink: Bis büzdja; Li. bürzdu, det ‘bustle, rumble’; LG pusten ‘puff’, Pust ‘gust’ all from a type *busd- or *bursd- (the Slav forms ambig.). Lith. forms in bezd- are LWs from Polish (AB). Gk. psóa 'stink' is a doubt- ful relative\n59\nbha, bho — bhàginos\n60\nBh\nbha, bho ‘indeed’. WP II, 136"
##### SYN.txt | ASHES
'D MAINLAND SHORE\nWATER\nSra\nLake\nGur, Bay WavE\nRiver; Stream; Broox Sprive; WEL\x0cL Woops, Forest TREE\nWoop\nStone; Rock Sxy, Heavens Sun -\nkéapos (olxovpévn, b)\nkécpos\nmundus\nmondo\nmonde\nmundo\nlume\ndomun (bith, b, c)\ndomhan (saoghal, b, : bith, b, c)\nbed\n1.53 1.54\nMoon STAR LIGHTNING THUNDER\nBOLT Lieut (sb.) DARKNESS SHADE\nAIR\nWinp Cioup\nRain (sb.) Snow (sb.) Icz WEATHER Fire FLAME (sb.) SMoKE (sb.) ASHES Burn (vb.)\nMarc (sb.)\n1.1 WORLD\n. fairhwus (midjun- gards, manaséps, b) heimr, vergld verden Sw. verld middangeard, weorold werld, world world wereld miltilgart, weralt Ay. werlt welt\nLith. Lett. ChSI. SCr. Boh. Pol. Russ. Skt.\nearth beneath’. But\n12\nLicutnine (as Striking), Taunprr-\nMist (Foc, Hazr)\nLieut (vb.), Kinpiz\npasaulis\npasaule\nmirit (svétit)\nsvijet\nsuét\nswiat\nmir, svet\nloka-, jagat'
##### SYN.txt | Ashes
  (none)
##### SYN.txt | 1\.85
'’; VLat. *pulvus > OSp. polvos, Sp. polvo, Cat. pols, OF r. *pous, whence I’. poussiére) : Lat. pollen, Grk. raXn, ratraXy ‘fine meal, fine dust’, Lat. puls, Grk. wédros ‘por- ridge’, etc. Walde-P. 2.60. Ernout-M. 785, 824. REW 6842. Gamillscheg 714.\nRum, praf, fr. Slavic, ChSl. prachii, etc. (below, 6).\n3. Tr. luaithred, NIr. luaithreadh (also -rean, etc.) ‘ashes’ and ‘dust’, fr. luaith ‘ashes’ (1.85).\nNI. ceo ‘mist’ (1.74), also ‘dust’, esp. ceo bothair ‘dust of the road’.\nW. llwch, beside Ilwwch ‘snowdrift’, Uuchio ‘throw, hurl,’ root connection?\nW. pylor, fr. Lat. pulvis, -eris (above, 2). Loth, Mots lat. 196.\nBr. poultr, fr. OFr. pouldre (above, 2). Henry 227.\n4. Goth. mulda = OE molde ‘loose earth, soil’, ete. (1.212).\nGoth. stubjus, OHG stuppt, stoub,\x0c MHG stoup, NHG staub, MLG, Du.'
```


## [2026-09-04T23:17:22.241Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'\\bASHES\\b',t):\n    seg=t[m.start():m.start()+1800]\n    if 'OE' in seg or 'ahd' in seg or 'aska' in seg or 'asce' in seg:\n        print(repr(seg)); print('#####'); break\nfor m in re.finditer(r'asce|aska\\b',t):\n    print(repr(t[max(0,m.start()-900):m.start()+500])); break\nEOF",
 "description": "Get Buck 1.85 ashes entry"
}
```


### [2026-09-04T23:17:24.324Z] TOOL RESULT

```
"ASHES\ncg Téppa, o7o0dds Goth. azgo Lith. pelenat Teak oraxry ON aska Lett. pelni Tir aie eee Javilla Dan. aske ChSl. popelit (pepelit) Fr. ake g Sw.  aska SCr.  pepeo Sp. cent OE asce Boh. opel Riven ceriise ME ashe Pol. popidl Tr, uci, NE ashes Russ. pepel Nir. luaith Du. asch Skt. bhasman-, asa- W. — Uudw OHG  asca Av. dtrya- Bese Tain! MHG asche\nWords NHG asche ‘\nor 6 5) P * for ‘ash, ashes’ (NE now usual- through ‘washing fluid, lye’, with shifted\npe though also the ash of a ci- ae mostly either derived from a for burn’, ‘fire’, ‘be dry’, ‘warm’ ba ce (by fire), or are cognate with\nr ‘dust’. ' A few come from or\napplication to the ‘ashes’ which pro- duce it.\n1. Grk. rédpa, fr. the root seen in Skt. dah-, Lith. degti, etc. ‘burn’ (1.85). Walde-P. 1.849. Boisacq 9\x0c63 f.\nCC-O. In Public Domain. Gurukul Kangri Collection, Haridwar\nDigitized by Arya Samaj Foundation Chennai and eGangotri\n74 SELECTED INDO-EUROPEAN SYNONYMS\nGrk. oodés, etym.? Walde-P. 2.680. Boisacq 899.\nNG oraxrn (pop. vs. lit. réppa, o7ods), Byz. oraxry (Const. Porph. as ‘ashes’), fr. oraxr) xovia lit. ‘trickling dust’ (craxrés fr. cratw ‘drop, drip’) used first for ‘lye’ made from ashes and then for the ‘ashes’.\n2. Lat. cinis, cineris (> It. cenere, Fr. cendre; derivs. >It. cinigia, Sp. ceniza, Rum. cenuge) : Grk. xévis ‘dust’. Walde-P. 1.392. Ernout-M. 187f. Walde-H. 1.217 f£. REW 1929, 1930.\nLat. favilla, esp. ‘glowing ashes’, fr. the root of fovére ‘warm’, Skt. dah- ‘burn’, etc. (1.84). Ernout-M. 339. Walde-H. 1.466.\n3. Ir. luaith, W. lludw, Br. ludu : Grk. Aobw, Lat. lavere ‘wash’, OF léag, NE lye, OHG louga, NHG lage ye’, with Celtic development through ‘washing fluid, lye’ to the ‘ashes’ from which it was made. Walde-P. 2.441. Pedersen 1.63.\n4, Goth. azgd, ON aska, OF asce, OHG asca, etc., general"
#####
'xéyn ON dupt, dust Lett. pisli (pl.), putelklz (pl.) Lat. pulvis Dan. stg ChSl.  prachii It. polvere Sw. stoft SCr. oprah Fr. poussitre OE dist Boh. prach Sp. polvo ME dust Pol. proch Rum. opraf, pulbere NE dust Russ. pyl Ir. luaithred Du. stof Skt.  renu-, pansu-, dhiali- Nir. luaithreadh OHG _ stuppi, stoub (melm) Av. pasnu- W. Ulwch, pylor MHG stoup Br. poulir NHG _ staub\nMany of the words for ‘dust? are from a widespread root (*dheu-), seen in words for ‘agitate, shake’, ‘vapor, smoke’, ete., or from others having the notion of ‘stir’, ‘scatter’, or ‘blow’. All such were ne popted first to the flying ‘dust’ in the air. Others are cog- nate with words for ‘loose earth, soil’, ‘fine meal’, ‘ashes’, with the common notion of Soni mere Glen But it is only a secondary association of this kind that is shown in the Ir. derivative of the\nword for ‘ashes’ used for ‘dust’ and in the use of OE asce ‘ashes’ for ‘dust’ in the Lindisf. gospels (Lk. 9.5, 10.11, etc. asca vs. dust in the WSax. versions), since these words for ‘ashes’ were not based in origin on the notion of small particles.\nWords of this group either cover also ‘powder’, or, especially Lat. pulvis, are the source of those now used for ‘pow- der’ (so far as this notion, as for a pre- pared product—medicinal, toilet, etc.,\nCC-0. In Public Domain. Gurukul Kangri Collection, Haridwar\nOEE hat a\nPPT ST SE BRIO ESS a ee SS\nDigit'
```


## [2026-09-04T23:17:30.670Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\ni=t.find('4, Goth. azgd, ON aska')\nprint(repr(t[i:i+900]))\nEOF",
 "description": "Buck ashes Germanic paragraph"
}
```


### [2026-09-04T23:17:32.620Z] TOOL RESULT

```
'4, Goth. azgd, ON aska, OF asce, OHG asca, etc., general Gme., fr. a root *as- seen in Lat. arére ‘be dry’, aridus ‘dry’, ardére ‘burn’, Grk. étw ‘be dry’, Skt. asa- ‘ashes, dust’, Toch. A dsar ‘dry’, Arm. acium ‘ashes’. Falk-Torp 35. Feist 72. Walde-H. 1.65.\n5. Lith. pelenai (pl.), Lett. pelni (pl.), OPruss. pelanne, ChSl. popelii (later pepelti), SCr. pepeo, ete., general Balto- Slavic word, prob. (like Lat. cinis : Grk. ous ‘dust’) : Lat. pulvis ‘dust, pow- der’, pollen ‘fine flour or dust’, Grk. wéXn “fine flour or dust’, etc.; less prob. : ChSI. poléti, paliti ‘blaze, burn’ (1.84). Walde-P. 2.60. Ernout-M. 785.\n6. Skt. bhasman-, fr. bhas- ‘devour’,\nhere through (attested) ‘devour by fire,\nreduce to ashes’.\nSkt. dsa-: Goth. azgd ‘ashes’ , ete. (above, 4).\nAv. dtrya-, fr. dtar- ‘fire’ (1.81).\n1.85 BURN (vb.) (Transitive and intransitive, when distinguished, are marked “a” and iby)\nGrk'
```


## [2026-09-04T23:17:42.299Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('WEB_vol1.txt',encoding='utf-8',errors='replace').read()\nfor p in [r'archives?,?\\s*n',r'ar[·.]?chive',r'\\bar[·.]?e[·.]?a\\b.{0,60}L',r'ar[·.]?son']:\n    print('#####',p);n=0\n    for m in re.finditer(p,t,re.I):\n        print(repr(t[max(0,m.start()-200):m.start()+450]));n+=1\n        if n>=2: break\n    if n==0: print(' (none)')\nEOF",
 "description": "Grep Webster's for archive/area/arson"
}
```


### [2026-09-04T23:17:45.263Z] TOOL RESULT

```
##### archives?,?\s*n
 (none)
##### ar[·.]?chive
'ly on the column; a chief beam. |\n2. the ornament or molding at the sides of and above a door, window, or other square opening. 2\nlir/chi-trived, a. having an architrave.\nir/chi-val, a. pertaining to archives or rec- ords; contained in records. è\när’chīveş, n.pl. [Fr., pl. of archif, from L. archivum, archium; Gr. archeion, a govern- ment house; ta archeia, archives; archē, be- ginning, government. ]\n1. a place where public records, documents, etc. are kept.\n2. the public records, documents, etc. kept in such a place. l;\när’chi-vist, n. the keeper of archives or rec- ords.\när’chi:võlt, n. [Fr. archivolie; It. archivolto; archi-, chief, and vo'
'rchitrave.\nir/chi-val, a. pertaining to archives or rec- ords; contained in records. è\när’chīveş, n.pl. [Fr., pl. of archif, from L. archivum, archium; Gr. archeion, a govern- ment house; ta archeia, archives; archē, be- ginning, government. ]\n1. a place where public records, documents, etc. are kept.\n2. the public records, documents, etc. kept in such a place. l;\när’chi-vist, n. the keeper of archives or rec- ords.\när’chi:võlt, n. [Fr. archivolie; It. archivolto; archi-, chief, and volto, an arch, vault.)\n1. the inner curve of an arch or the struc- tural parts of this. i\n2. an ornamental molding on the wall side of an arch. i\nar-chi-z0/ic, a'
##### \bar[·.]?e[·.]?a\b.{0,60}L
't, lineal ancestor of tk guage of | (1150-1475) and that of the Northwest used by t poet must be passed over in r torian of the whole En\nimportant variety of ME. is that of the South Eastern Midland “area particularly as written by Chaucer.\n(a) Orthography and Pronunciation\nIf the ME. of Chaucer resembles MnE. more closely than OE., the fact is due partly to a series of orthographic. adaptations brought about by the influence of Fr. The most important of these are: (1) The use of ch for OF. c in child; (2) the use of qu- for OE. cw- in quene, queen, OF. cwén; (3) the partial displacement of p, Ò by th in with, OE. wip; (4) the introduction of'
'laware, Ottawa, and others,\nAl-gon’qui-an, n. of languages. 3 -\n2. a member of any tribe using one of these languages. 3\nAl-gon’quin, z. 1.a member of a tribe of Al- gonquian Indians who lived in the area of the Ottawa River, Canada: now called Ottawa.\n2. the language of this tribe.\n3. Algonquian.\nal-g6-pho’bi-a, n. [from Gr. algos, pain; and -phobia.] an extreme or abno: fear of pain.\nal’gor, x. [L., from algere, to be cold.] cold ora chal felt during a fever.\nal’gi-rism, al’g6-rithm, n. [OFr. algorisme;\n1. the Algonquian family\nfise, bull, brite, tGrn, up; cry, myth; cat, machine, ace, church, chord; gem, afiger, (Fr.) bon, as; this, thin; '
##### ar[·.]?son
'con, bucket, fry, gum, pork, push, sound, stew, stubble, and rip, as well as the more abstract beauty, color, heritage, honor, Judgment, noble, and tragedy. Some, like abbey, cardinal, clerk, image, parson, penance, and piety, are drawn from the special vo- ry of the Church; some, like assize, attorney, fine, forfeit, plea, suit, from that of the law; some from medicine, like my, balm, ointment, poison, stomach; some from the army, mbush, archer, chieftain, dart, lance; some from the table, petite, taste, veal, venison; some from the home, like basin,\n= Digitized by Arya Samaj Foundation Chennai and eGangotri\nOUTLINE HISTORY OF THE ENGLISH LA'
'nse resulted from a misunderstanding of the original Greek.\n3. in music, the unaccented part of a\n_, measure; upbeat.\nars lofi’ga, vita bre’vis, [L.] art (is) long,\n„hife (is) short.\nar’s6n, n. [OFr. arson, arsoun; from L., arsus, pp. of ardere, to burn.] the crime of purposely setting fire to another’s building or property, or to one’s own so as to collect insurance. By\n_, common law it is a felony.\nars-phen/a-mine, n. a yellowish arsenical powder from which an aqueous, saline solu- tion is prepared for use in the treatment of syphilis and some other diseases: also called Salvarsan.\nars po-e’ti-ca, [L.] the art of poetry.\närt, the archaic se'
```


## [2026-09-04T23:17:55.009Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('WEB_vol1.txt',encoding='utf-8',errors='replace').read()\nfor p in [r'ā.{0,3}re[-·:]a,\\s*n',r'archi[-·:]?tect,\\s*n',r'ar.{0,3}chā.{0,3}ic',r'är.{0,3}chi[-·:]tect']:\n    print('#####',p);n=0\n    for m in re.finditer(p,t,re.I):\n        print(repr(t[max(0,m.start()-150):m.start()+400]));n+=1\n        if n>=1: break\n    if n==0: print(' (none)')\nEOF",
 "description": "Webster area/architect entries"
}
```


### [2026-09-04T23:17:57.524Z] TOOL RESULT

```
##### ā.{0,3}re[-·:]a,\s*n
 (none)
##### archi[-·:]?tect,\s*n
 (none)
##### ar.{0,3}chā.{0,3}ic
 (none)
##### är.{0,3}chi[-·:]tect
 (none)
```


## [2026-09-04T23:18:05.397Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['incoming/ARY/ARY_latin_index_pages.txt','incoming/ARY/ARY_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for p in [r'ARDERE|ardere',r'ARCHI|archi',r'\\bAS[- ]',r'هکتار',r'آرشیو',r'خاکستر']:\n        ms=list(re.finditer(p,t))\n        print(f,'|',p,'->',len(ms))\n        if ms:\n            m=ms[0]; print('   ',repr(t[max(0,m.start()-200):m.start()+200]))\nEOF",
 "description": "Grep Aryanpur"
}
```


### [2026-09-04T23:18:07.134Z] TOOL RESULT

```
incoming/ARY/ARY_latin_index_pages.txt | ARDERE|ardere -> 1
    ' AITHOS GREEK) li\nIr-tF iebG oly ATER _— ALATINY a3 “a\nFO-PF Mes eal cid EIT HOLD FRISIAN) (75 523\nAITH OLD IRISH) S43 p\ndetlooy\noF AS SHA Oly al ee\na tole tad 3 dle ool ee\nwth A ws (ARDENT ¢ ARID <) ARDERE 2 oj} VATER ys isojly lt -¥\nre |\n\x0c[pdf page 51]\n» UGNUS * (LATVIAN) (33) 93) ATHRAVAN, ADAR, :(AVESTAN) gl!\nZJARR ALBANIAN) gidT ATUR, ATHRA-\nAGNIS _ ABITTITE) cox ATER {OLD PERSIAN) jheuly\nREF'
incoming/ARY/ARY_latin_index_pages.txt | ARCHI|archi -> 0
incoming/ARY/ARY_latin_index_pages.txt | \bAS[- ] -> 219
    'SIL 5 oJ ly bi ajy plat FV 5s Sy olen y AF Way lf\n\x0c[pdf page 6]\na : _\nV | elas\nSHY cols Sly LH cle (Foal apb OG) g dees yo SL\n«943.9 JS (INDO-IRANIAN)\noe pain NG tcghagslg sean jl yghte Sead gpl 9 FF AS 99 yl S gle\nBI 2S ge SE (glyasl 300 45 Se oe) eB 0b 4 ese cle po yp Ay cand\nEr PHN HS pap ST) cal ole Mak 9 oan Sir Apa tebe UT 3h easly\n: weal (hale cg) cali al y ee Obj ES UBT ty Gyale Obj dy en '
incoming/ARY/ARY_latin_index_pages.txt | هکتار -> 0
incoming/ARY/ARY_latin_index_pages.txt | آرشیو -> 0
incoming/ARY/ARY_latin_index_pages.txt | خاکستر -> 0
incoming/ARY/ARY_pages.txt | ARDERE|ardere -> 0
incoming/ARY/ARY_pages.txt | ARCHI|archi -> 0
incoming/ARY/ARY_pages.txt | \bAS[- ] -> 0
incoming/ARY/ARY_pages.txt | هکتار -> 0
incoming/ARY/ARY_pages.txt | آرشیو -> 0
incoming/ARY/ARY_pages.txt | خاکستر -> 2
    '\u200cکهن (ع۲1بها5 #6لاتل ا0): 4 (5188) رگ :8ل2آلقق ما۸\n: 0 72 عل\u200cا8\nروسی (/(۷8514): 0 1 (1075015) :0/05\nچکه (2560)): 0 6 (6(185015]) :7\nاسلواکی (8101۸4): 0 11 :47\nلیترانی (40714ل 7 7/): 1018 برهان قاطع :(خاکستر) ۲۲و ۷۰۲ و(اگر)۵۳\nیادداشت:\nممین(در پانوشت برهان قاطع) این واژه را با آتش" همريشه می\u200cداند.\nاوستابی (/4۲897۸): ۰ ۰8۸01 ,011هعم ۸\nپهلوی (۷7هالل۲۸): ۸ آلمانی (057/۸0): نراد با\nسانسکریت (54(/86(7): '
```


## [2026-09-04T23:18:19.444Z] TOOL CALL #68: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py",
 "description": "Check fetch_source usage"
}
```


### [2026-09-04T23:18:19.487Z] TOOL RESULT

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


## [2026-09-04T23:18:26.853Z] TOOL CALL #69: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/archive|page 65, root Arxein, English/French archive chain\" \\\n \"https://www.etymonline.com/word/architect|page 65, root Arxein, architect via French architecte < L architectus < Gk arkhitekton\" \\\n \"https://www.etymonline.com/word/archaeology|page 65, root Arxein, node 7/8 archaeology via French archeologie\" \\\n \"https://www.etymonline.com/word/area|page 65, root As, Latin area and its uncertain link to arere\" \\\n \"https://www.etymonline.com/word/arson|page 65, root As, English arson < OFr arson < L ardere\" \\\n \"https://www.etymonline.com/word/ash|page 65, root As, English ash < OE aesce < PGmc *askon\" \\\n \"https://www.etymonline.com/word/hectare|page 65, root As, hectare = hecto- + are (< L area), 1795 decree\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\"; done",
 "description": "Archive etymonline sources"
}
```


### [2026-09-04T23:18:32.280Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f67fe44b0bfaa606.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b29d7e690d00cb0a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9b5f33d5b37267a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c927239b6e344cc7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/344d2200ca3f8ab0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/159054d426b084ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/34d6d06ff77b92fc.txt
```


## [2026-09-04T23:18:40.919Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82eh%E2%82%81s-\" --note \"page 65, root As: PIE *h2eh1s- 'to be dry, burn, hearth, ashes'\"; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%E1%BC%84%CF%81%CF%87%CF%89\" --note \"page 65, root Arxein: Ancient Greek arkho, disputed origin\"; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%B4%DB%8C%D9%88\" --note \"page 65, node 4: Persian arshiv borrowed from French archives\"; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%87%DA%A9%D8%AA%D8%A7%D8%B1/\" --note \"page 65, node 3: Persian hektar, Dehkhoda/Moin/Amid tag it French\"; python3 tools/fetch_source.py \"https://vajehyab.com/?q=%D8%A2%D8%B1%D8%B4%DB%8C%D8%AA%DA%A9%D8%AA\" --note \"page 65, node 4: Persian arshitekt in Amid and Moin\"",
 "description": "Archive Wiktionary and Persian sources"
}
```


### [2026-09-04T23:18:46.130Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/53543260b676bbfa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/57ac597ddf428d09.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aeb9f9cdc62a0657.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a13e41e36e7932f0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/af97e3f01ec9e7d4.txt
```


## [2026-09-04T23:18:49.659Z] TOOL CALL #71: Bash

```json
{
 "command": "for f in a13e41e36e7932f0 af97e3f01ec9e7d4 aeb9f9cdc62a0657; do echo \"=== $f ===\"; head -c 300 data/verification/sources/web/$f.txt; echo; done; grep -c . data/verification/sources/web/index.jsonl",
 "description": "Verify archived Persian pages have content"
}
```


### [2026-09-04T23:18:51.479Z] TOOL RESULT

```
=== a13e41e36e7932f0 ===
URL: https://abadis.ir/fatofa/%D9%87%DA%A9%D8%AA%D8%A7%D8%B1/
FETCHED: 2026-09-04T23:18:45Z
STATUS: 200
TITLE: هکتار - معنی در دیکشنری آبادیس

هکتار - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 هکتار
 /hektAr/

 معنی ان�
=== af97e3f01ec9e7d4 ===
URL: https://vajehyab.com/?q=%D8%A2%D8%B1%D8%B4%DB%8C%D8%AA%DA%A9%D8%AA
FETCHED: 2026-09-04T23:18:46Z
STATUS: 200
TITLE: معنی آرشیتکت | واژه یاب

'
 />

 معنی آرشیتکت | واژه یاب 

 26 فرهنگ 
 17 مدخل

 همه دیکشنری مترادف طیفی آزاد 
=== aeb9f9cdc62a0657 ===
URL: https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%B4%DB%8C%D9%88
FETCHED: 2026-09-04T23:18:44Z
STATUS: 200
TITLE: آرشیو - Wiktionary, the free dictionary

آرشیو - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main pa
636
```


## [2026-09-04T23:18:56.096Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/web/af97e3f01ec9e7d4.txt',encoding='utf-8').read()\ni=t.find('آرشیتکت',2000)\nprint(t[1000:4000])\nEOF",
 "description": "Read archived vajehyab page"
}
```


### [2026-09-04T23:18:58.024Z] TOOL RESULT

```
وی هم‌آوا

 ارشیتکت
 واژه‌نامه آزاد
 معمار.

 جست‌وجوی متن

 والادگر
 واژه‌نامه آزاد
 آرشیتکت.

 رازیگر
 واژه‌نامه آزاد
 "رازیگر" به معنای معمار / آرشیتکت. این واژه در قدیم به صورت "راز نگهدار" بوده است. معمارانی که برای پادشاهان قصر می ساختند، معمولا یک یا دو راه فرار مخفی در قصر

 داویله
 لغت‌نامه دهخدا
 داویله . [ ل ِ ](اِخ ) (شارل ) آرشیتکت فرانسوی . متولد پاریس به سال 1653 و متوفی به سال 1700م . او بنیانگذار طاق نصرت پیرورا در منت پلیه است .

 دبان
 لغت‌نامه دهخدا
 دبان . [ دُ ] (اِخ ) (ژاک ) آرشیتکت و معمار فرانسوی . متولد در پاریس به سال 1796 و متوفی به سال 1870 م .

 لمرسیه
 لغت‌نامه دهخدا
 لمرسیه . [ ل ُ م ِ ی ِ ] (اِخ ) ژاک . آرشیتکت فرانسوی ، مولد پُن ْتوآز (1585-1654 م .).

 بیشتر
 ۶ واژه در متن 

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
```


## [2026-09-04T23:20:18.784Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,os\ndef cnt(f,pats):\n    if not os.path.exists(f): print('MISSING',f); return\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print(f, {p:len(re.findall(p,t)) for p in pats})\ncnt('POK_01.txt',[r'arkh',r'aQ/e',r'ἄρχ'])\ncnt('BQT_v1_pages.txt',[r'آرشیو',r'هکتار',r'آرشیتکت'])\ncnt('HRN.txt',[r'archiv',r'hektar',r'Hektar'])\ncnt('HUB.txt',[r'archiv',r'hektar'])\ncnt('SKT.txt',[r'[Aa]rchive',r'[Aa]rson',r'[Aa]sh,',r'ardent'])\nEOF",
 "description": "Final negative-check greps"
}
```


### [2026-09-04T23:20:21.035Z] TOOL RESULT

```
POK_01.txt {'arkh': 0, 'aQ/e': 0, 'ἄρχ': 0}
BQT_v1_pages.txt {'آرشیو': 0, 'هکتار': 0, 'آرشیتکت': 0}
HRN.txt {'archiv': 1, 'hektar': 0, 'Hektar': 0}
HUB.txt {'archiv': 0, 'hektar': 0}
SKT.txt {'[Aa]rchive': 0, '[Aa]rson': 5, '[Aa]sh,': 42, 'ardent': 2}
```


## [2026-09-04T23:20:26.984Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'Arson|ARSON',t):\n    print(repr(t[max(0,m.start()-200):m.start()+350]));print('---')\nfor m in list(re.finditer(r'\\bAsh\\b',t))[:3]:\n    print(repr(t[max(0,m.start()-150):m.start()+300]));print('===')\nEOF",
 "description": "Skeat arson/ash entries"
}
```


### [2026-09-04T23:20:28.986Z] TOOL RESULT

```
'  m*Tpoisi>^i¥oVt  rock parsley.  —  Gk.  wirpot.  rock,  stone  ;  aiktrow, a  kind  of  parsley ;  »ee  Celery.\nParsnop.  Parsnip.  (F.-L.)  ForrocA^ parjwp,  and  tUU  bcUct  pasntffi^  »*  «\n332\nPARSON.\nI\nI\nPals^nve ;  the  r  being  inlrufiive.  —  O.  F. pojUnatjue,  a  parsnip  (by  dropping  /,  and change  of  ^  to  /.  as  in  Gk.  W/iirc  «  L. qui*tqut),^\\^  pastmaca,  a  pannrp ;  orig. A  root  dog  op.—  L. /^Lf/i>«d/r,  to  dig  np.— l^pastimtm,  a  two-pronged  dibble.  %  The sumx-#fc*/ was  assimilated  to  that  ai  tumep. '
---
'on  athlete.  — tik.  daxtiy, to  work,  cxerciw;  aUo,  to  mortify  the body,  as  an  ascetic\nA&oititious;  sec  Soienoe.\nAscribe  ;  sec  Baribe.\nAsh,  a  tree.  (E.)  M.  £.  Ar<^^.  A.S.  icrr. -4-  Du.  ejcA ;  Icel.  atAr ;  Dan.  and  Swed, as/: ;  G.  €scAe.\nAshamed;  see  Bhamo.\nAshes.  ^E.)  The  pi.  of  asA,  whidi  is little  used.  M.E.  orM^,  a.xe,  sing.;  the pi.  is  commonly  ojrA/n,  oxen,  but  in  North- cm  E.  it  is  a'
===
"uert,  to  throw M^eotive.  \\X-)     A  ^^timTnaU.*!  v 1\n^4k\nfV,     ti\nSP\n^•1\nJTBE.\np,  to  ihift  the  booci-»n  frDin\nthe   mast  to  Another;'   Ash\ntpclt/F'^,  gyti.  —  Dan.  gib^,\n[Swcd.  dial,  gippa,  to  jcrt  up.\nred.  ptffa,  to  move  up  and\nE  jump.     ^  The  form  ^bf\nlu.  g^jp^n^  to  tuiD  suddenly,\nmore  ftftirely.  «i  x  hone.\nO.  F.  giber,  to  itniggle  with\nid    feet  (Roquefort):    whence\n(F.  rtpmt*r\\   to  kick  a"
===
"ntiiU.  -  L.  lenticmlii^  a  little  Ic» til ;  double  dimin.  of  Itnti'^  crude  lomi irnt,  a  lentil.\nLent,  a  fast  of  40  days,  beginning Ash-Wedncsday.     (E.)      The    fast sprinij-ume ;  the  old  sense  is  simply y>\\.K.ient,lenttn.    A.  S.  >Mr/^«, tKe  s; supposed  to  be  derived  from  iSsMf, because  in  sprii^  the  dajrs  lengthen  i is  possible.  4*  ^^-  It'^*,  sprisg;  C. O.  H.  G.  Itnsin,  Ungiun,      Der. ad"
===
```


## [2026-09-04T23:27:17.675Z] TOOL CALL #75: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build65.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nE = \"https://www.etymonline.com/word/\"\n\nentry0 = {\n \"entry\": 0,\n \"root\": \"Arxein, Arkhein\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Ancient Greek ἄρχω / ἄρχειν (árkhō, árkhein) 'to begin; to rule, lead' — a Greek verb with no accepted Indo-European etymology\",\n \"note\": \"The root box is right in every respect that can be checked: the verb, the language label (Greek, NOT Indo-European) and the gloss. Klein (KLN p.100, s.v. 'arch-') gives 'Gk. ἀρχ-, which is rel. to ἀρχός, \\\"leader, chief, ruler\\\", from the stem of ἄρχειν, \\\"to begin, rule\\\" (whence also ἀρχή, \\\"beginning, first cause, origin, first principle, office\\\")'. Watkins/AHD prints the item in square brackets — his convention for a non-IE etymon — '[arkhein. To begin, rule, command. Greek verb of unknown origin; with derivatives arkhē, rule, beginning, and arkhos, ruler. (ARCH-), -ARCH, ARCHAEO-, ARCHAIC, ARCHI-, ARCHIVES, ARCHON, (-ARCHY) ...]', which is exactly why Nourai heads the box 'Greek' and not 'Indo-European'. Pokorny has no entry for the verb at all (grep of POK_01 for arkh- = 0 hits), and Wiktionary calls the origin 'disputed' (either *h₂r̥-sḱe-ti from *h₂er- 'to fit', or *h₂ergʰ-). One structural fault runs through the chart: node #5 hangs English arch-/archbishop off French, whereas those two entered Old English straight from Ecclesiastical Latin (OE arcebiscop, c. 900); only architect and archive really came through French.\",\n \"note_fa\": \"ریشهٔ «آرخِین/آرخِه» همان فعل یونانی باستان ἄρχω (arkhō) «آغاز کردن، فرمان راندن» است و نورایی به‌درستی آن را ریشه‌ای یونانی — و نه هندواروپاییِ آغازین — نشانده است؛ واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ AHD این مدخل را در قلاب می‌آورد («فعل یونانی با خاستگاه ناشناخته») و پوکورنی اصلاً چنین ریشه‌ای ندارد، و ویکی‌واژه هم خاستگاه آن را «مورد اختلاف» می‌خواند (یا *h₂r̥-sḱe-ti از *h₂er- «جور شدن»، یا *h₂ergʰ-). کلاین در ص ۱۰۰ همان زنجیره‌ای را می‌دهد که نمودار کشیده است: ἀρχός «سرور، پیشوا»، ἀρχή «آغاز، فرمانروایی، دیوان»، و از آن پیشوند arkhi- که به لاتینی و سپس به زبان‌های اروپایی رفته است. پس ادعای نورایی دربارهٔ خودِ ریشه درست است؛ تنها ایراد ساختاری نمودار در بند ۵ است، چون پیشوند arch- و واژهٔ archbishop از راه فرانسه به انگلیسی نرسیده‌اند بلکه در انگلیسی کهن یک‌راست از لاتینیِ کلیسایی وام گرفته شده‌اند.\",\n \"sources\": [W+\"%E1%BC%84%CF%81%CF%87%CF%89\", E+\"architect\", E+\"archive\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:100\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt 0-based leaf 64 (carries the printed numbers '100' and '101'), s.v. arch-: 'arch-, pref. meaning \\\"chief, principal\\\", as in archduke, archbishop. — ME. arche-, fr. OE. arce-, -erce, fr. L. archi-, arch-, fr. Gk. ἀρχι-, ἀρχ-, which is rel. to ἀρχός, \\\"leader, chief, ruler\\\", from the stem of ἄρχειν, \\\"to begin, rule\\\" (whence also ἀρχή ...). Cp. also archaeo-, archaic, archaism, arche, architect, archon, -archy.' — the head of Nourai's chart, verbatim.\"},\n   {\"ref\": \"AHD:1506\", \"status\": \"supports\",\n    \"note\": \"Nourai's page is in the 1975/76 New College appendix (not online); the same entry stands in Watkins, AHD of IE Roots (1985), AHD_watkins1985.txt: '[arkhein. To begin, rule, command. Greek verb of unknown origin; with derivatives arkhé, rule, beginning, and arkhos, ruler. (ARCH-), -ARCH, ARCHAEO-, ARCHAIC, ARCHI-, ARCHIVES, ARCHON, (-ARCHY); AUTARCHY, EXARCH, MENARCHE.]' The square brackets mark it as a non-IE Greek etymon, which is exactly Nourai's 'Greek' label.\"}\n ],\n \"nodes\": []\n}\n\nentry0[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Greek\",\n  \"words\": \"arx, arxt, arkh, arkht; arx-tekton; arxeion\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Nourai's 'x' renders Greek χ, and he habitually gives a word twice, once with x and once with kh/ch (cf. node #6 'arxaios, archaios'). So the four shapes are two pairs: arx = arkh = ἀρχ- (ἀρχή arkhḗ 'beginning, rule, magistracy', ἀρχός arkhós 'leader, chief'), and arxt = arkht = ἀρχοντ-, the oblique stem of ἄρχων árkhōn 'ruler' (present participle of ἄρχω), which fits the gloss 'leader, master'. As printed, however, neither 'arxt' nor 'arkht' is a citable Greek word-form, and that abbreviation is the only reason this node is not 'confirmed'. The two compounds are exact: ἀρχι-τέκτων arkhi-tektōn 'master builder' = ἀρχι- 'chief' + τέκτων 'carpenter, builder' (PIE *teḱs-, Nourai's ☞Tex cross-reference, confirmed by Watkins's index line 'ARCHITECT teks-'), used from the 5th c. BCE (Herodotus, Attic inscriptions); and ἀρχεῖον arkheîon 'magistrate's house, town hall', plural τὰ ἀρχεῖα 'the public records', a derivative of ἀρχή in its sense 'office, magistracy' — precisely Nourai's double gloss 'government, public office, government records'.\",\n  \"derivation_fa\": \"در نویسه‌گردانی نورایی «x» همان خیِ یونانی است و او هر واژه را دو بار می‌نویسد، یک بار با x و یک بار با kh/ch (نمونه‌اش بند ۶: arxaios, archaios). پس این چهار صورت دو جفت‌اند: arx = arkh = ἀρχ- (یعنی ἀρχή «آغاز، فرمانروایی، دیوان» و ἀρχός «پیشوا») و arxt = arkht = ἀρχοντ-، ستاک غیرفاعلیِ ἄρχων «فرمانروا» که اسم فاعل ἄρχω است و با معنای «سرور، پیشوا» جور درمی‌آید. با این همه، آن‌گونه که در کتاب چاپ شده، arxt/arkht هیچ‌کدام صورتِ نقل‌پذیر یونانی نیستند و همین کوته‌نویسی سبب شده داوری ما «با احتیاط پذیرفتنی» باشد نه «تأییدشده». دو ترکیب دیگر بی‌عیب‌اند: ἀρχι-τέκτων «معمارِ سرآمد» از ἀρχι- «سر، مِهین» + τέκτων «درودگر، سازنده» (از ریشهٔ *teḱs-، همان ارجاع ☞Tex نورایی که واتکینز نیز تأیید می‌کند) و ἀρχεῖον «دیوان، دارالحکومه» و جمع آن τὰ ἀρχεῖα «اسناد دولتی» که از ἀρχή در معنای «منصب و دیوان» ساخته شده است.\",\n  \"sources\": [W+\"%E1%BC%84%CF%81%CF%87%CF%89\", E+\"architect\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:100\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 64 (printed 100/101): 'fr. Gk. ἀρχι-, ἀρχ-, which is rel. to ἀρχός, \\\"leader, chief, ruler\\\", from the stem of ἄρχειν ... (whence also ἀρχή, \\\"beginning, first cause, origin, first principle, office\\\")'; same leaf, s.v. architect: 'Gk. ἀρχιτέκτων, \\\"master builder\\\", fr. ἀρχι-, \\\"chief\\\", and τέκτων, \\\"carpenter, builder\\\"'; s.v. archive: 'transliteration of Gk. ἀρχεῖον, \\\"official building\\\", pl. τὰ ἀρχεῖα, \\\"public records, archives\\\", fr. ἀρχή'.\"},\n    {\"ref\": \"AHD:69\", \"status\": \"partial\",\n     \"note\": \"The body of the 1975/76 AHD (p.69, the 'arch-' page) is not open online; the appendix half of the same claim is checkable and supports it — AHD_watkins1985.txt index: 'ARCHI- arkhein ... ARCHIVES arkhein ... ARCHITECT teks-', i.e. AHD splits architect between arkhein and teks- exactly as Nourai's ☞Tex arrow does.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Band I, grep of POK_01.txt\", \"stance\": \"silent\",\n     \"note\": \"No entry for ἄρχω / arkh- anywhere in Pokorny (0 hits for 'arkh'); consistent with AHD's verdict 'Greek verb of unknown origin'.\"},\n    {\"src\": \"IEC\", \"where\": \"s.v. arghos\", \"stance\": \"partial\",\n     \"note\": \"Mann, IEC.txt: 'arghos, ā \\\"point, tip\\\" Arm. cf. arg- (px. *first-); Gk. arkhé; arkhós; OCS cf. razínŭ ...' — Mann does try an IE affiliation (*arghos 'point, tip', hence 'first'), which nobody else follows; it does not contradict Nourai's Greek box, it merely goes one step further back.\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. ār'chīveş\", \"stance\": \"supports\",\n     \"note\": \"'[Fr., pl. of archif, from L. archivum, archium; Gr. archeion, a government house; ta archeia, archives; archē, beginning, government.]' — same Greek base and the same 'public records' sense.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Latin\", \"words\": \"architectus; archivum\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Both are Greek words taken into Latin, not inherited: architectus is Gk. ἀρχιτέκτων latinised with the -us of the second declension (Cicero, Vitruvius; whence architectūra), and archīvum (also archīum, archēum) is a straight transliteration of Gk. ἀρχεῖον, first in imperial-age juristic Latin for the record office, with the neuter plural archīva 'the archives'. The -v- of archivum reflects the Greek diphthong ει before a vowel-less ending in the late spelling; Klein prints both variants side by side, 'L. archivum, archium, \\\"the archives\\\", transliteration of Gk. ἀρχεῖον'.\",\n  \"derivation_fa\": \"هر دو واژه در لاتینی وام‌واژه‌اند نه ارثی: architectus همان ἀρχιτέκτων یونانی است که با پایانهٔ صرفِ دومِ لاتینی (‎-us‎) لاتینی شده و از سیسرون و ویترویوس به بعد به‌کار رفته است (و از آن architectūra)؛ archīvum (با صورت‌های archīum و archēum) نیز نویسه‌گردانی مستقیم ἀρχεῖον است که در لاتینیِ حقوقیِ دورهٔ امپراتوری برای «دیوان اسناد» به‌کار می‌رفت و جمع آن archīva «بایگانی‌ها» بود. کلاین هر دو صورت را کنار هم می‌آورد: «L. archivum, archium ... نویسه‌گردانی یونانی ἀρχεῖον». پس پیکان یونانی ← لاتینی در این بند تأییدشده است.\",\n  \"sources\": [E+\"architect\", E+\"archive\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\",\n     \"note\": \"The AHD appendix (AHD_watkins1985.txt) confirms the words' membership ('ARCHIVES arkhein', 'ARCHITECT teks-') but, being a root list, prints no Latin intermediate; the Latin forms themselves are confirmed from Klein and Webster (see consulted).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 64 = printed pp. 100-101\", \"stance\": \"supports\",\n     \"note\": \"'architect, n. — F. architecte, fr. L. architectus, fr. Gk. ἀρχιτέκτων, \\\"master builder\\\"'; 'archive, n. ... — F. archives, fr. L. archivum, archium, \\\"the archives\\\", transliteration of Gk. ἀρχεῖον, \\\"official building\\\"'.\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. ār'chīveş\", \"stance\": \"supports\",\n     \"note\": \"'[Fr., pl. of archif, from L. archivum, archium; Gr. archeion, a government house ...]' — the identical Latin pair archivum/archium.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"French\", \"words\": \"architecte; archive\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"French architecte is a learned borrowing of Latin architectus (16th c.; Middle French also had the popular form architecteur), and archives (almost always plural in French) comes from Latin archīva, through an older French archif; Old/Middle French had archif, and Modern French fixed les archives. In both the Greek χ is spelled -ch- but pronounced /ʃ/ — French [aʁʃitɛkt], [aʁʃiv] — a detail that matters for node #4, because it is this French pronunciation with š, not the English one with k, that the Persian forms reproduce.\",\n  \"derivation_fa\": \"architecte در فرانسه وام‌واژه‌ای عالمانه از لاتینیِ architectus است (سدهٔ شانزدهم) و archives (که در فرانسه تقریباً همیشه جمع به‌کار می‌رود) از لاتینیِ archīva و از راه صورت کهن‌ترِ archif آمده است. نکتهٔ آوایی مهم این است که در فرانسه «ch» در این دو واژه /ش/ تلفظ می‌شود: [aʁʃitɛkt] و [aʁʃiv]؛ همین «ش» است که در فارسیِ «آرشیتکت» و «آرشیو» بازتاب یافته و ثابت می‌کند وام‌گیریِ فارسی از فرانسه بوده است نه از انگلیسی (که در آن k تلفظ می‌شود).\",\n  \"sources\": [E+\"architect\", E+\"archive\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\",\n     \"note\": \"The AHD appendix does not print French intermediates; Klein and Webster (consulted) both give F. architecte and F. archives (older archif) as the immediate sources of the English words, which is the arrow Nourai draws.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 64 (pp. 100-101)\", \"stance\": \"supports\",\n     \"note\": \"'architect, n. — F. architecte, fr. L. architectus'; 'archive, n., generally used in the pl. — F. archives, fr. L. archivum, archium'.\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. ār'chīveş\", \"stance\": \"supports\",\n     \"note\": \"'[Fr., pl. of archif, from L. archivum ...]' — Webster even preserves the older French singular archif.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Persian\", \"words\": \"âršîtekt «آرشیتکت»; âršîv «آرشیو»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Both are 20th-century French loans in Persian, taken in with the French sound-shape: French archives [aʁʃiv] > NP آرشیو âršiv (š for French ch, final v; English 'archive' with /k/ could not give š), and French architecte [aʁʃitɛkt] > NP آرشیتکت âršitekt. Wiktionary's Persian entry for آرشیو says flatly 'Borrowed from French archives', glossing it 'archives', with the native synonym بایگانی bāygāni that the Farhangestān promoted in its place. آرشیتکت is the rarer of the two — Persian normally says معمار (Arabic loan) — and survives mostly in older usage, e.g. Dehkhoda's biographical entries 'داویله ... آرشیتکت فرانسوی', 'لمرسیه ... آرشیتکت فرانسوی'. Neither word can be older than the Qajar/Pahlavi contact with French: Borhan-e Qāṭeʿ (1652) has neither, and neither Horn nor Hübschmann knows them.\",\n  \"derivation_fa\": \"هر دو واژه وام‌واژه‌های فرانسویِ سدهٔ چهاردهم خورشیدی‌اند و درست با قالب آوایی فرانسه وارد فارسی شده‌اند: فرانسویِ archives [aʁʃiv] ← «آرشیو»، و architecte [aʁʃitɛkt] ← «آرشیتکت». همان «ش» گواه قاطع است، زیرا صورت انگلیسیِ archive با /ک/ تلفظ می‌شود و هرگز «آرشیو» نمی‌داد؛ پس پیکانِ فرانسه ← فارسیِ نورایی درست است. ویکی‌واژه نیز ذیل «آرشیو» می‌نویسد: «وام‌گرفته از فرانسویِ archives»، با هم‌معنای فارسیِ «بایگانی» که فرهنگستان به‌جای آن نهاد. «آرشیتکت» کم‌کاربردتر است (فارسی معمولاً «معمار» می‌گوید) و بیشتر در متون کهنِ سدهٔ اخیر دیده می‌شود، چنان‌که دهخدا در شرح‌حال‌ها می‌نویسد «داویله ... آرشیتکت فرانسوی». هیچ‌یک در برهان قاطع و در هرن و هوبشمان نیست، چون از دورهٔ آشنایی ایران با فرانسه‌اند.\",\n  \"sources\": [W+\"%D8%A2%D8%B1%D8%B4%DB%8C%D9%88\", \"https://vajehyab.com/?q=%D8%A2%D8%B1%D8%B4%DB%8C%D8%AA%DA%A9%D8%AA\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:43\", \"status\": \"supports\",\n     \"note\": \"MON_part1.txt: the entry 'آرشیو: [French headword, OCR-garbled] (ا.) جایی که اسناد، اوراق، تصاویر، پرونده‌ها، صفحات موسیقی و مانند آن حفظ می‌شود؛ بایگانی.' stands two entries after آرشیدوک and about 550 characters after the running footer 'فرهنگ فارسی معین ۴۱', i.e. on printed p. 42/43 — Nourai's MON:43. Moʿin gives the word a Latin-script French headword, i.e. tags it a French loan. آرشیتکت is not in the OCR of the same stretch.\"},\n    {\"ref\": \"AMD:25\", \"status\": \"not_checked\",\n     \"note\": \"Amid's 2-vol. 1369 print is not paginated online (refs_online: 'page numbers ... not mappable'). The word itself is in the online Persian dictionary aggregators (vajehyab lists آرشیتکت, and Dehkhoda uses it in situ: 'آرشیتکت فرانسوی'), but p.25 could not be verified.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt, آ-section (printed pp. 39-43)\", \"stance\": \"supports\",\n     \"note\": \"آرشیو defined 'جایی که اسناد ... حفظ می‌شود؛ بایگانی' with a Latin-script (French) headword.\"},\n    {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt, grep آرشیو / آرشیتکت\", \"stance\": \"silent\",\n     \"note\": \"0 hits — as expected: Borhan-e Qāṭeʿ (1062/1652) predates the French loans by three centuries.\"},\n    {\"src\": \"HRN\", \"where\": \"HRN.txt, grep archiv/hektar\", \"stance\": \"silent\",\n     \"note\": \"Horn's Grundriss (1893) has no such entries (the single 'archiv' hit is a bibliographical 'Archiv' journal title), confirming these are post-1900 borrowings outside the inherited lexicon.\"},\n    {\"src\": \"HUB\", \"where\": \"HUB.txt, grep archiv\", \"stance\": \"silent\", \"note\": \"0 hits; Hübschmann's Persische Studien records no such loan.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"English\", \"words\": \"arch- : master; archbishop, architect, archive\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Two of the four items travel exactly as drawn: architect (1560s) from French architecte, and archive(s) (c. 1600, 'records'; 1640s 'place where records are kept') from French archives. The other two do not: the prefix arch- and archbishop reached English centuries before any French influence — Old English arce-/erce- from Ecclesiastical Latin archi-, archiepiscopus, whence OE arcebiscop (attested c. 900), ME archebischop. Klein states this plainly: 'arch-, pref. ... — ME. arche-, fr. OE. arce-, -erce, fr. L. archi-, arch-, fr. Gk.' — Latin to Old English, with no French step. So the node's ultimate origin is right, but the French parent is wrong for arch-/archbishop.\",\n  \"derivation_fa\": \"دو مورد از چهار مورد دقیقاً همان راهی را رفته‌اند که نمودار نشان می‌دهد: architect (دههٔ ۱۵۶۰) از فرانسویِ architecte و archive(s) (حدود ۱۶۰۰ به معنی «اسناد» و از دههٔ ۱۶۴۰ به معنی «بایگانی») از فرانسویِ archives. اما دو مورد دیگر چنین نیستند: پیشوند -arch و واژهٔ archbishop سده‌ها پیش از نفوذ فرانسه وارد انگلیسی شده‌اند، یعنی در انگلیسی کهن از لاتینیِ کلیسایی (archi-، archiepiscopus ← arcebiscop، گواهی‌شده در حدود سال ۹۰۰ میلادی). کلاین همین را می‌گوید: «arch- ... از انگلیسی میانه arche-، از انگلیسی کهن arce-، از لاتینیِ archi-» و هیچ میانجی فرانسوی نمی‌آورد. پس خاستگاه نهایی درست است ولی پیکانِ «فرانسه ← انگلیسی» برای arch- و archbishop نادرست است و باید از جعبهٔ لاتینی کشیده می‌شد.\",\n  \"sources\": [E+\"architect\", E+\"archive\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\",\n     \"note\": \"AHD_watkins1985.txt lists all of them under arkhein ('(ARCH-), -ARCH, ARCHAEO-, ARCHAIC, ARCHI-, ARCHIVES, ARCHON'), so the ultimate ancestry is AHD's; but a root list says nothing about whether the vehicle was French or Latin, which is where the chart slips.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 64 (pp. 100-101)\", \"stance\": \"contradicts\",\n     \"note\": \"For the prefix and archbishop Klein gives no French: 'arch-, pref. ... — ME. arche-, fr. OE. arce-, -erce, fr. L. archi-, arch-, fr. Gk.'; 'archbishop, n. — ME. archebischop, fr. OE. arcebiscop, fr. Eccles. L. archiepiscopus'. For architect and archive he gives French, as Nourai does.\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. ār'chīveş\", \"stance\": \"supports\",\n     \"note\": \"'[Fr., pl. of archif ...]' — supports the French route for archive specifically.\"},\n    {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt (A-Dive), 'arch-' region\", \"stance\": \"silent\",\n     \"note\": \"The Funk & Wagnalls OCR of the arch- pages is too damaged to quote; no usable statement either way.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Greek\", \"words\": \"arxaios, archaios : ancient\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"One word given twice in Nourai's two spellings (x = χ): ἀρχαῖος arkhaîos 'from the beginning, ancient', a regular -αιος adjective built on ἀρχή 'beginning'. Klein: 'archaeo- ... fr. ἀρχαῖος, \\\"ancient\\\", lit. \\\"from the beginning\\\", fr. ἀρχή, \\\"beginning\\\"'; hence also ἀρχαϊκός arkhaïkós 'old-fashioned' (> archaic) and ἀρχαιολογία 'the study of ancient things' (> archaeology). The semantic step 'beginning' > 'belonging to the beginning' > 'ancient' is the whole derivation, so the arrow root→#6 is sound.\",\n  \"derivation_fa\": \"این یک واژه است که نورایی دو بار نوشته است (x همان χ): ἀρχαῖος «از آغاز، کهن»، صفتی با پسوند ‎-αιος‎ ساخته‌شده بر ἀρχή «آغاز». کلاین می‌نویسد: «archaeo- ... از ἀρχαῖος «کهن»، به‌معنای تحت‌اللفظیِ «از آغاز»، از ἀρχή «آغاز»». از همین صفت، ἀρχαϊκός «کهنه‌طرز» (که archaic شده) و ἀρχαιολογία «دانش چیزهای کهن» (که archaeology شده) پدید آمده‌اند. تحولِ معنایی «آغاز ← وابسته به آغاز ← باستانی» تمام داستان این بند است و پیکان ریشه ← بند ۶ درست است.\",\n  \"sources\": [E+\"archaeology\", W+\"%E1%BC%84%CF%81%CF%87%CF%89\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:67\", \"status\": \"partial\",\n     \"note\": \"The AHD body page 67 (1975/76) is not online, but the appendix half is: AHD_watkins1985.txt indexes 'ARCHAEO- arkhein' and 'ARCHAIC arkhein', i.e. AHD does put ἀρχαῖος under arkhein, which is the arrow drawn.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 64 (p. 100)\", \"stance\": \"supports\",\n     \"note\": \"'archaeo- ... — Gk. ἀρχαιο-, ἀρχαι-, fr. ἀρχαῖος, \\\"ancient\\\", lit. \\\"from the beginning\\\", fr. ἀρχή, \\\"beginning\\\". See arch-'; and 'archaic ... — Gk. ἀρχαϊκός, \\\"old-fashioned, antiquated\\\", fr. ἀρχαῖος'.\"},\n    {\"src\": \"POK\", \"where\": \"POK_01.txt, grep arkh-\", \"stance\": \"silent\",\n     \"note\": \"0 hits: Pokorny nowhere derives the ἀρχ- family, consistent with the Greek-internal derivation given here.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Latin\", \"words\": \"\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"An empty pass-through box: Nourai routes the archaeo-/archaic words through Latin. That is only half right. archaeology does have a Latin step, but a modern one — Modern/New Latin archaeologia (16th-17th c.) beside French archéologie, whence English 'archaeology' c.1600. archaic, by contrast, has no Latin intermediary in the standard accounts: Klein takes it straight from Gk. ἀρχαϊκός, and Etymonline routes it through French archaïque (1810s). So the box should be read as 'Modern Latin / French', not as a classical Latin stage.\",\n  \"derivation_fa\": \"این جعبه تهی است و نورایی واژه‌های archaeo-/archaic را از میانجیِ لاتینی گذر داده است؛ این کار تنها نیمی درست است. برای archaeology میانجیِ لاتینی هست، اما لاتینیِ نو: صورت archaeologia در لاتینیِ علمیِ سدهٔ شانزدهم-هفدهم در کنار فرانسویِ archéologie، که از حدود سال ۱۶۰۰ به انگلیسی رسیده است. اما برای archaic هیچ میانجیِ لاتینی در منابع معتبر نیامده: کلاین آن را یک‌راست از یونانیِ ἀρχαϊκός می‌گیرد و اتیمآنلاین از راه فرانسویِ archaïque (دههٔ ۱۸۱۰). پس این جعبه را باید «لاتینی نو / فرانسه» خواند نه لاتینیِ کلاسیک.\",\n  \"sources\": [E+\"archaeology\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"The node carries no reference of its own in the book (refs=None), so there is nothing of Nourai's to check here.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 64 (p. 100)\", \"stance\": \"contradicts\",\n     \"note\": \"Klein gives no Latin step for either word: 'archaeology, also archeology, n. — Gk. ἀρχαιολογία, \\\"the study of ancient things\\\"'; 'archaic, adj. ... — Gk. ἀρχαϊκός'.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt index\", \"stance\": \"silent\",\n     \"note\": \"'ARCHAEO- arkhein', 'ARCHAIC arkhein' — the root list names no intermediate language.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"English\", \"words\": \"archaeo-, archaeology, archaic\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"archaeology entered English about 1600 in the sense 'ancient history', from French archéologie / Modern Latin archaeologia < Gk. ἀρχαιολογία (Plato, Hippias Major 285d, of 'tales of old times'); the modern sense 'scientific study of past peoples' dates from 1825, with the combining form archaeo- productive in ModL coinages (Archaeopteryx 1861). archaic is 1810s from French archaïque or directly from Gk. ἀρχαϊκός 'old-fashioned'. All three are ultimately ἀρχαῖος < ἀρχή < ἄρχω, so the chain the chart draws is right; only the language of the intermediate box (#7) is imprecise.\",\n  \"derivation_fa\": \"واژهٔ archaeology حدود سال ۱۶۰۰ به معنی «تاریخ باستان» وارد انگلیسی شد، از فرانسویِ archéologie و لاتینیِ نو archaeologia، از یونانیِ ἀρχαιολογία (که افلاطون در هیپیاس بزرگ به معنی «حکایت‌های کهن» به‌کار برده است)؛ معنای امروزیِ «باستان‌شناسی» از ۱۸۲۵ است و جزء ترکیبیِ archaeo- در واژه‌سازی‌های لاتینیِ نو زاینده شد (مانند Archaeopteryx در ۱۸۶۱). archaic نیز از دههٔ ۱۸۱۰ است، از فرانسویِ archaïque یا مستقیماً از یونانیِ ἀρχαϊκός «کهنه‌طرز». هر سه سرانجام به ἀρχαῖος و آن به ἀρχή و ἄρχω می‌رسند؛ پس زنجیرهٔ نمودار درست است و تنها برچسبِ جعبهٔ میانی (بند ۷) بی‌دقت است.\",\n  \"sources\": [E+\"archaeology\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt index: 'ARCHAEO- arkhein', 'ARCHAIC arkhein' (and 'ARCHAEOPTERYX pet-' for the second element), i.e. AHD assigns exactly these English words to arkhein.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 64 (p. 100)\", \"stance\": \"supports\",\n     \"note\": \"Klein has all three: 'archaeo-, before a vowel archae-; also archeo- ... combining form meaning \\\"ancient, primeval, primitive\\\"'; 'archaeology ... Gk. ἀρχαιολογία, \\\"the study of ancient things\\\"'; 'archaic ... Gk. ἀρχαϊκός'.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt, grep Archaeo/Archaic\", \"stance\": \"silent\",\n     \"note\": \"The Skeat scan's OCR of the A-pages is too corrupt to yield the entries (0 clean hits).\"}\n  ]\n }\n]\n\nentry2 = {\n \"entry\": 2,\n \"root\": \"As\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₂eh₁s- / *h₂eHs- (older notation *ā̆s-) 'to be dry; to burn, glow', with the derived senses 'hearth' and 'ashes'\",\n \"note\": \"Nourai's citation is exact. Pokorny IEW p.68 heads the entry 'ās-, davon azd-, azg(h)- \\\"brennen, glühen\\\"' and its material is, item for item, this whole chart: 'ai. āsa-ḥ \\\"Asche, Staub\\\"; lat. āra \\\"Altar\\\" (= osk. aasai \\\"in ārā\\\", umbr. are), āreō, -ēre \\\"bin trocken, ausgedörrt\\\", āridus \\\"trocken\\\" (davon ardeō \\\"brenne\\\") ... ārea \\\"freier Platz, Tenne usw.\\\" (eigentl. \\\"ausgebrannte, trockene Stelle\\\") ... germ. *askōn in aisl. aska, ags. asce, æsce, ahd. asca, nhd. Asche.' Watkins repeats it under 'as-. To burn, glow ... [Pok. as- 68.]'. Modern reconstruction writes the root with laryngeals; Wiktionary's page notes the debate whether it is *h₂eHs-, *h₂eh₁s- or *h₂es-, and adds Hittite ḫāšš- 'ash(es), hearth'. Two caveats worth carrying: (a) the derivation of Latin ārea from ārēre, which the whole French/Persian/English branch of this chart depends on, is standard in Pokorny, Klein and Funk & Wagnalls but is called doubtful by Ernout-Meillet ('Pas de rapprochement sûr') and 'irregular' by Etymonline, and Watkins omits area from the root; (b) the printed 'ara : an area' in node #1 conflates two different Latin words (see that node).\",\n \"note_fa\": \"ارجاع نورایی دقیق است: پوکورنی در ص ۶۸ فرهنگ ریشه‌شناسی هندواروپایی مدخل «ās- و از آن azd-، azg(h)- ‹سوختن، تافتن›» را می‌آورد و مواد همان مدخل مو‌به‌مو همین نمودار است: سنسکریت āsa- «خاکستر، غبار»؛ لاتینی āra «قربانگاه»، āreō «خشکم، سوخته‌ام»، āridus «خشک» (و از آن ardeō «می‌سوزم») و ārea «میدانِ باز، خرمن‌گاه» (در اصل «جای سوخته و خشک»)؛ و ژرمانیِ *askōn که در انگلیسی کهن asce/æsce و آلمانیِ Asche بازمانده است. واتکینز نیز همین را ذیل «as-: سوختن، تافتن» تکرار می‌کند. در بازسازی امروزی این ریشه را با حنجره‌ای‌ها می‌نویسند (‎*h₂eh₁s-‎/‎*h₂eHs-‎) و شکل هیتّیِ ḫāšš- «خاکستر، اجاق» را هم به آن می‌افزایند. دو نکتهٔ احتیاطی: نخست آنکه پیوند ārea با ārēre — که کل شاخهٔ فرانسه/فارسی/انگلیسیِ این نمودار بر آن استوار است — نزد پوکورنی و کلاین پذیرفته است اما ارنو-مِیه آن را «بی‌پیوندِ مطمئن» می‌خواند و واتکینز area را در این ریشه نمی‌آورد؛ دوم آنکه صورت چاپیِ «ara : an area» در بند ۱ دو واژهٔ جدا را درهم آمیخته است.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/h%E2%82%82eh%E2%82%81s-\", E+\"ash\", E+\"area\"],\n \"ref_check\": [\n   {\"ref\": \"POK:68\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt 0-based leaf 76 (the leaf carries the running number 'I 68'; the entry runs onto leaf 77 which is headed '69'): 'ās-, davon azd-, azg(h)- \\\"brennen, glühen\\\". Ai. āsa-ḥ \\\"Asche, Staub\\\" ...; lat. āra \\\"Altar\\\" (= osk. aasai \\\"in ārā\\\", umbr. are \\\"arae\\\" usw.), āreō, -ēre \\\"bin trocken, ausgedörrt\\\", āridus \\\"trocken\\\" (davon ardeō \\\"brenne\\\", Partiz. Pass. assus \\\"trocken gebraten\\\"), ārea \\\"freier Platz, Tenne usw.\\\" (eigentl. \\\"ausgebrannte, trockene Stelle\\\"); ahd. essa f., nhd. Esse ... azgo- ... germ. *askōn in aisl. aska, ags. asce, æsce, ahd. asca, nhd. Asche.' Every branch of Nourai's chart is on this one page.\"}\n ],\n \"nodes\": []\n}\n\nentry2[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Latin\", \"words\": \"ardĕre : to be on fire; arĕre : to become dry (land); ara : an area\",\n  \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"ara : an area\",\n  \"correct_form\": \"ārea 'open piece of ground' (the etymon of French are / English area); Latin āra is a separate word of the same root meaning 'altar, hearth'\",\n  \"derivation\": \"The first two items are right, though the book's breves are wrong for the vowel quantities: ārdēre 'to be on fire' (Klein: 'ardēre ... stands for *āridēre, fr. āridus, \\\"parched, dry\\\", and is rel. to ārēre, \\\"to be dry\\\", fr. *āsēre, fr. I.-E. base *ās-'), with perfect ārsī and participle ārsus that carry the family into Romance; and ārēre 'to be dry', the stative *h₂eh₁s-eh₁- of the root. The third is the problem. The book prints 'ara : an area', but Latin āra means 'altar, hearth' (Oscan aasaí, Umbrian are, Hittite ḫāšša-), while the word meaning 'an area' is ārea 'vacant piece of ground, threshing floor' — literally, per Pokorny, 'ausgebrannte, trockene Stelle', a burnt-off, dry place. Both belong to this root, so the entry is not wrong about the etymology, only about which word it is naming; and since the French daughter in node #2 is are < L. ārea (Klein p.102, and Nourai's own FSD:1133 which derives hectare from 'L. area, area'), the form the box should show is ārea. The extraction is faithful to the page (checked on the 300 dpi render of pdf p.65): this is Nourai's own conflation, not a scanning error. Note also that Ernout-Meillet doubt the ārea/ārēre link ('rattaché à areō par Varron ... Pas de rapprochement sûr') and Watkins leaves area out of the root altogether, while listing ARA under it.\",\n  \"derivation_fa\": \"دو مورد نخست درست‌اند، هرچند علامت‌های کوتاهیِ مصوت در چاپ کتاب نادرست است: ārdēre «سوختن، در آتش بودن» (کلاین: «ardēre ... در اصل *āridēre از āridus ‹خشک›، هم‌ریشه با ārēre ‹خشک بودن›، از ریشهٔ هندواروپایی *ās-») با ماضیِ ārsī و اسم مفعول ārsus که خانوادهٔ واژه را به زبان‌های رومی می‌برد؛ و ārēre «خشک بودن» که همان ساخت حالتیِ ریشه است. اما مورد سوم مشکل دارد: کتاب «ara : an area» چاپ کرده است، حال آنکه āraی لاتینی به‌معنی «قربانگاه، آتشدان» است (هم‌ریشه با اسکیِ aasaí و هیتّیِ ḫāšša-) و آنچه معنی «پهنه، میدان» می‌دهد ārea است، یعنی به گفتهٔ پوکورنی «جای سوخته و خشک». هر دو واژه از همین ریشه‌اند، پس خطا در ریشه‌شناسی نیست بلکه در نام‌بردن واژه است؛ و چون فرزند فرانسویِ این جعبه (بند ۲) همان are از ārea است، صورت درست در این خانه ārea بود. خطا از خودِ کتاب است نه از استخراج داده‌ها (تصویر ۳۰۰ نقطه‌ایِ صفحهٔ ۶۵ بررسی شد). افزون بر این، ارنو-مِیه پیوند ārea با ārēre را «بی‌پیوند مطمئن» می‌دانند و واتکینز area را زیر این ریشه نمی‌آورد، هرچند āra را می‌آورد.\",\n  \"sources\": [E+\"area\", W+\"Reconstruction:Proto-Indo-European/h%E2%82%82eh%E2%82%81s-\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:102\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 65 (printed 102/103), s.v. ardent: 'fr. L. ardentem, acc. of ardens, pres. part. of ardēre, \\\"to burn\\\", which stands for *āridēre, fr. āridus, \\\"parched, dry\\\", and is rel. to ārēre, \\\"to be dry\\\", fr. *āsēre, fr. I.-E. base *ās-, \\\"to burn, glow\\\" ... See ash ... and cp. ara, ardor, area, arid, arson'. Klein's own cross-reference list has BOTH ara and area — which is precisely the pair Nourai's line runs together.\"},\n    {\"ref\": \"FSD:1133\", \"status\": \"supports\",\n     \"note\": \"FSD_vol2.txt leaf 423, the leaf that carries the printed number 1133, s.v. hectare: 'A measure in the metric system[,] 2.47 acres: the French unit of land-measure. See METRIC. [F., < Gr. hekaton, hundred, + L. area, area.]' — Funk & Wagnalls spell the Latin word area, not ara, and even supply Nourai's '2.47 acres'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Band I p.68 (POK_01.txt leaf 76)\", \"stance\": \"supports\",\n     \"note\": \"'lat. āra \\\"Altar\\\" ..., āreō, -ēre \\\"bin trocken, ausgedörrt\\\", āridus \\\"trocken\\\" (davon ardeō \\\"brenne\\\") ... ārea \\\"freier Platz, Tenne usw.\\\" (eigentl. \\\"ausgebrannte, trockene Stelle\\\")' — Pokorny lists āra and ārea as two distinct derivatives, which is the distinction the book blurs.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. as-\", \"stance\": \"partial\",\n     \"note\": \"'as-. To burn, glow ... 2. Suffixed form *ās-ā- in Latin āra, altar, hearth: ARA. 3. Suffixed (stative) form *ās-ē- in: a. Latin ārēre, to be dry, hence āridus, dry, parched: ARID; b. Latin ardēre, to burn, be on fire, from āridus: ARDENT, ARDOR, ARSON.' Watkins has ardēre, ārēre and āra but pointedly NOT area (the index lists 'ARA as-' and no AREA).\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, LAT.txt leaves 97-98 (printed pp. 79-80)\", \"stance\": \"partial\",\n     \"note\": \"s.v. area: 'rattaché à areō par Varron, L.L. 5,6,38 ... Pas de rapprochement sûr.' s.v. āreō: 'être sec ... A ardor se rattache ārdeō ... On rapproche tokh. A āsar \\\"sec\\\"; skr. āsaḥ \\\"cendre\\\", ... v.h.a. asca \\\"cendre\\\" ... got. azgo \\\"cendre\\\" ... S'y rattache peut-être āra.' So E-M support the root and the ash-words, but hedge on both āra ('peut-être') and area ('pas de rapprochement sûr').\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt s.v. āsos\", \"stance\": \"supports\",\n     \"note\": \"'āsos, ā (\\\"as-\\\") \\\"hearth, sacrificial altar\\\". Cf. as- | Hitt. hassas; OLat. asa; Lat. āra; cf. Umb. aso, Praen. asom (pp. \\\"burnt\\\")' — Mann derives Latin āra from the same *as- 'burn'.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I (WLD_Bd1_pages.txt), cross-references to *ās-\", \"stance\": \"supports\",\n     \"note\": \"The OCR of the entry head is destroyed, but its cross-references survive twice, e.g. 'Die Zusammenstellung des idg. *āro- mit aschw. ærin, arin \\\"Herd\\\", aisl. arenn \\\"Erhöhung, Herd\\\" ... ahd. arin, erin \\\"Altar\\\" ist wegen der Bedeutung fernzuhalten, s. unter *ās- \\\"ausdorrende Gluthitze\\\"' — i.e. WP has the root *ās- 'scorching heat' and files the 'hearth/altar' words under it.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"French\", \"words\": \"are : area; hect-are : unit of area (2.47 acres)\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"are is not an inherited word but a deliberate metric coinage: 'F., formed in 1795 by a decree of the French National Convention, fr. L. area, \\\"vacant piece of ground\\\"' (Klein p.102) — 100 m², i.e. a square decametre, which is exactly why Nourai points ☞Dekm. hectare is the same coinage prefixed with hect(o)- < Gk. ἑκατόν 'hundred': 100 ares = 10,000 m² = 2.47 acres. The Greek-plus-Latin hybrid is deliberate metric practice (Greek prefixes for multiples, Latin for submultiples). Nourai's '2.47 acres' is taken over word for word from his own source, Funk & Wagnalls p.1133.\",\n  \"derivation_fa\": \"«آر» واژه‌ای ارثی نیست بلکه ساختِ عمدیِ نظام متریک است: کلاین در ص ۱۰۲ می‌نویسد «فرانسویِ are، ساخته‌شده در ۱۷۹۵ به فرمان کنوانسیون ملی فرانسه، از لاتینیِ area ‹زمین بایر›» — برابر با ۱۰۰ متر مربع، یعنی یک دکامترِ مربع، و همین است که نورایی ارجاع ☞Dekm می‌دهد. «هکتار» همان واژه است با پیشوند hect(o)- از یونانیِ ἑκατόν «صد»: صد آر برابر ده هزار متر مربع یا ۲٫۴۷ ایکر. آمیختن پیشوند یونانی با ستاک لاتینی در نظام متریک قاعده است (پیشوندهای یونانی برای مضرب‌ها و لاتینی برای کسرها). عبارت «۲٫۴۷ ایکر» را نورایی عیناً از منبع خودش، فرهنگ فانک و واگنالز ص ۱۱۳۳، گرفته است.\",\n  \"sources\": [E+\"hectare\", E+\"area\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:69\", \"status\": \"not_checked\",\n     \"note\": \"Page 69 of the 1975/76 AHD body (the 'arch-...are' page) is not open online; the appendix volume that IS online has no entry for the metric units (index has neither ARE nor HECTARE under as-). The claim itself is confirmed from Klein and Funk & Wagnalls.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 65, printed p.102-103\", \"stance\": \"supports\",\n     \"note\": \"'are, n., a square unit. — F., formed in 1795 by a decree of the French National Convention, fr. L. area, \\\"vacant piece of ground\\\". See next word and cp. the second element in hectare.'\"},\n    {\"src\": \"FSD\", \"where\": \"FSD_vol2.txt leaf 423 = printed p.1133\", \"stance\": \"supports\",\n     \"note\": \"'hec'tare ... A measure in the metric system[,] 2.47 acres: the French unit of land-measure ... [F., < Gr. hekaton, hundred, + L. area, area.]'\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt\", \"stance\": \"silent\",\n     \"note\": \"Only volume 1 of Webster's 2nd ed. is on disk and its 'are/hectare' pages did not survive the OCR in usable form.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"âr 1 «آر» : unit of area; hectâr «هکتار» : unit of area\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Both are French metric terms adopted in Persian in the late Qajar / early Pahlavi period, when the metric system was legislated (1926): آر âr from French are and هکتار hektâr from French hectare, the -â- of هکتار rendering the French [a] of -are. Moʿin's own definitions are the proof and match Nourai's glosses exactly: 'آر (ا.) واحد مقیاس سطح، برابر با ۱۰۰ متر مربع (یک دکامتر مربع): هکتار = صد آر' and 'هکتار (ا.) واحد برای مقیاس سطح، صد آر = یک هکتومتر مربع'. Note that Moʿin's own '= یک دکامتر مربع' is the source of Nourai's ☞Dekm cross-reference. Dehkhoda, Moʿin and Amid all tag هکتار as French.\",\n  \"derivation_fa\": \"هر دو واژه اصطلاح‌های متریکِ فرانسوی‌اند که در اواخر قاجار و آغاز پهلوی — همزمان با قانون اوزان و مقیاس‌ها در ۱۳۰۴ — به فارسی راه یافتند: «آر» از فرانسویِ are و «هکتار» از فرانسویِ hectare، که «ا»ی کشیدهٔ هجای پایانی بازتاب [a]ی فرانسوی است. گواهِ کار، تعریف‌های خودِ معین است که با معنای نورایی مو‌به‌مو می‌خواند: «آر (ا.) واحد مقیاس سطح، برابر با ۱۰۰ متر مربع (یک دکامتر مربع): هکتار = صد آر» و «هکتار (ا.) واحد برای مقیاس سطح، صد آر = یک هکتومتر مربع». همان قید «یک دکامتر مربع» در معین است که ارجاع ☞Dekm نورایی را توضیح می‌دهد. دهخدا و معین و عمید هر سه «هکتار» را فرانسوی می‌دانند.\",\n  \"sources\": [\"https://abadis.ir/fatofa/%D9%87%DA%A9%D8%AA%D8%A7%D8%B1/\", E+\"hectare\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:39\", \"status\": \"supports\",\n     \"note\": \"MON_part1.txt, in the stretch whose running footer reads 'فرهنگ فارسی معین ۳۹': 'آر (ا.) واحد مقیاس سطح، برابر با ۱۰۰ متر مربع (یک دکامتر مربع): هکتار = صد آر' — Nourai's gloss and his ☞Dekm reference in one line.\"},\n    {\"ref\": \"MON:5159\", \"status\": \"supports\",\n     \"note\": \"MON_part2.txt: 'هکتار: [Latin-script French headword] (ا.) واحد برای مقیاس سطح صد آر = یک هکتومتر مربع = ۱۰۰۰۰ متر مربع' (the OCR of the page footers in part 2 is lost, so the volume/page 5159 itself could not be re-read, but the entry is verbatim there).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt (p.39) and MON_part2.txt s.v. هکتار\", \"stance\": \"supports\",\n     \"note\": \"Both entries as quoted above; Moʿin heads each with the Latin-script French form, his tag for a French loan.\"},\n    {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt, grep هکتار / آر\", \"stance\": \"silent\",\n     \"note\": \"0 hits for هکتار; Borhan-e Qāṭeʿ has nothing on the metric units, as expected for a 1652 dictionary.\"},\n    {\"src\": \"HRN\", \"where\": \"HRN.txt / HUB.txt, grep hektar\", \"stance\": \"silent\",\n     \"note\": \"0 hits in Horn (1893) and Hübschmann (1895): the loans are later than both books.\"},\n    {\"src\": \"MON\", \"where\": \"abadis.ir aggregation of دهخدا / معین / عمید s.v. هکتار\", \"stance\": \"supports\",\n     \"note\": \"Dehkhoda: 'واحد سطح برابر با ده هزار متر مربع' tagged French; Moʿin: 'ده هزار متر مربع' tagged French; Amid: 'واحد اندازه‌گیری سطح، معادل ده هزار متر مربع'.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"English\", \"words\": \"hectare\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English took the word ready-made from French in 1817 (Etymonline), the unit itself having been created by the French National Convention's decree of 1795; it is 'a superficial measure equal to 100 ares'. Funk & Wagnalls, the very page Nourai cites, spells out the hybrid: '[F., < Gr. hekaton, hundred, + L. area, area]', and gives the equivalence '2.47 acres' that Nourai copies into the French box.\",\n  \"derivation_fa\": \"انگلیسی این واژه را در ۱۸۱۷ آمادهٔ آماده از فرانسه گرفت (اتیمآنلاین)، هرچند خودِ یکا در ۱۷۹۵ به فرمان کنوانسیون ملی فرانسه پدید آمده بود و «برابر صد آر» تعریف شده است. فرهنگ فانک و واگنالز — همان صفحه‌ای که نورایی ارجاع می‌دهد — ساختِ دورگهٔ واژه را می‌شکافد: «فرانسوی، از یونانیِ hekaton ‹صد› + لاتینیِ area»، و همان برابرنهادِ «۲٫۴۷ ایکر» را می‌آورد که نورایی در جعبهٔ فرانسه نقل کرده است.\",\n  \"sources\": [E+\"hectare\"],\n  \"ref_check\": [\n    {\"ref\": \"FSD:1133\", \"status\": \"supports\",\n     \"note\": \"FSD_vol2.txt leaf 423 (printed 1133): 'hec'tare ... A measure in the metric system[,] 2.47 acres: the French unit of land-measure. See METRIC. [F., < Gr. hekaton, hundred, + L. area, area.]'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 65 (p.102), s.v. are\", \"stance\": \"supports\",\n     \"note\": \"'... cp. the second element in hectare' — Klein derives the second element of hectare from are < L. area.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt index\", \"stance\": \"silent\",\n     \"note\": \"Neither HECTARE nor AREA appears in Watkins's index (only 'ARA as-'), so the AHD root list is silent on this branch.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"English\", \"words\": \"area; arson\",\n  \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"extraction\",\n  \"book_prints\": \"the arrow for this box is drawn from the bottom of the Latin box (node #1) — it runs down from that box, turns right and ends at the 'English | area, arson' box; the root's own spine has no arrowhead entering this line\",\n  \"correct_form\": \"parent should be #1 (Latin), not #0 (the root)\",\n  \"derivation\": \"The words themselves are exactly right and both come through Latin, which is what the printed chart draws and what the JSON's 'parent: 0' loses: area was borrowed from Latin ārea in the 1530s ('vacant piece of ground'), the sense 'amount of surface within limits' following in the 1560s; arson entered English in the 1670s as a law term from Anglo-French arsoun / Old French arson, from Late Latin arsiōnem (nom. arsiō) 'a burning', a noun of action on ārsus, the past participle of ārdēre — Webster's: 'ar'son, n. [OFr. arson, arsoun; from L. arsus, pp. of ardere, to burn.]'. So the node's content is confirmed; only the parent link in the extracted JSON is wrong (checked against the 300 dpi render of pdf p.65, where the connector unmistakably starts at the Latin box). One substantive caveat carries over from node #1: Watkins puts ARSON under as- but not AREA, and Etymonline calls area's link to ārēre 'irregular'.\",\n  \"derivation_fa\": \"خودِ واژه‌ها کاملاً درست‌اند و هر دو از راه لاتینی آمده‌اند — همان چیزی که نمودارِ چاپی نشان می‌دهد و در داده‌های استخراج‌شده («parent: 0») از دست رفته است: area در دههٔ ۱۵۳۰ از لاتینیِ ārea به معنی «زمین بایر» وام گرفته شد و معنای «مساحتِ محدود» در دههٔ ۱۵۶۰ پیدا شد؛ arson در دههٔ ۱۶۷۰ همچون اصطلاحی حقوقی از انگلونرمانِ arsoun و فرانسویِ کهنِ arson وارد شد، که خود از لاتینیِ متأخر arsiōnem «سوزاندن» است، اسم مصدرِ ساخته‌شده بر ārsus، اسم مفعولِ ārdēre؛ وبستر می‌نویسد: «arson ... از فرانسویِ کهن arson، از لاتینیِ arsus، اسم مفعول ardēre ‹سوختن›». پس داوری دربارهٔ محتوای بند «تأییدشده» است و تنها پیوندِ پدر در فایل استخراج‌شده نادرست است (تصویر ۳۰۰ نقطه‌ایِ صفحهٔ ۶۵ نشان می‌دهد پیکان از جعبهٔ لاتینی سرچشمه می‌گیرد). یک نکتهٔ احتیاطی هم از بند ۱ به اینجا می‌رسد: واتکینز arson را زیر این ریشه می‌آورد ولی area را نه، و اتیمآنلاین پیوند area با ārēre را «بی‌قاعده» می‌خواند.\",\n  \"sources\": [E+\"arson\", E+\"area\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"The box carries no reference of its own in the book (refs=None); the claims were checked against Klein, Webster, Watkins and Etymonline instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 65 (printed 102-103)\", \"stance\": \"supports\",\n     \"note\": \"s.v. ardent: '... cp. ara, ardor, area, arid, arson'; s.v. area: 'L., \\\"vacant piece of ground, building plot\\\", rel. to ārēre, \\\"to become dry\\\", hence area orig. meant \\\"a place burned down, a dry, bare place\\\" ... For sense development cp. G. Esse, \\\"chimney, forge\\\", which also derives fr. I.-E. base *ās-, \\\"to burn\\\".'\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. ar'sŏn\", \"stance\": \"supports\",\n     \"note\": \"'[OFr. arson, arsoun; from L. arsus, pp. of ardere, to burn.] the crime of purposely setting fire to another's building or property' — the Old French / Latin route, not a direct descent from the root.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. as-\", \"stance\": \"partial\",\n     \"note\": \"'... b. Latin ardēre, to burn, be on fire, from āridus, parched: ARDENT, ARDOR, ARSON.' Arson yes; area is absent from the entry and from the index.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, LAT.txt leaf 98 (printed p.80)\", \"stance\": \"partial\",\n     \"note\": \"'A ārsum se rattache ārsūra' and the Romance list 'les l[angues] rom[anes] ont conservé ardēre ..., *arsio 680, arsūra 689; tous mots qui expriment l'idée de brûler' — i.e. E-M document the *arsiō that gives arson; but on area, 'Pas de rapprochement sûr'.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Germanic\", \"words\": \"askôn : ashes\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Nourai's 'askôn' is Pokorny's Proto-Germanic *askōn, the n-stem feminine 'ashes', formed from the root with the velar extension *as-g- (Pokorny's 'azgo-' beside 'azg(h)-'): PIE *h₂eh₁s-g- > PGmc *askōn, whence Old Norse aska, OE asce/æsce, OHG asca, NHG Asche; the parallel *azgōn shows in Gothic azgō, and the awkward relation of *askōn to *azgōn is a known crux (Pokorny points to Feist p.72). Buck states the same thing in one line: 'Goth. azgō, ON aska, OE asce, OHG asca, etc., general Gmc., fr. a root *as- seen in Lat. ārēre \\\"be dry\\\", āridus \\\"dry\\\", ardēre \\\"burn\\\", Grk. azō \\\"be dry\\\", Skt. āsa- \\\"ashes, dust\\\"'.\",\n  \"derivation_fa\": \"صورت «askôn» در کتاب همان *askōn ژرمانیِ آغازینِ پوکورنی است، اسمِ مادینهٔ ستاک‌نونی به معنی «خاکستر»، ساخته بر ریشه با گسترشِ کامیِ *as-g- (که پوکورنی آن را «azgo-» در کنار «azg(h)-» می‌آورد): از *h₂eh₁s-g- به *askōn ژرمانی، و از آن نروژی کهن aska، انگلیسی کهن asce/æsce، آلمانی علیای کهن asca و آلمانیِ امروز Asche؛ صورت موازیِ *azgōn در گوتیِ azgō دیده می‌شود و نسبت دشوارِ این دو نزد پژوهشگران مشهور است (پوکورنی به فایست ص ۷۲ ارجاع می‌دهد). باک نیز در یک جمله همین را می‌گوید: «گوتی azgō، نروژی کهن aska، انگلیسی کهن asce، آلمانی علیای کهن asca و جز آن، همگانی در ژرمانی، از ریشهٔ *as- که در لاتینیِ ārēre ‹خشک بودن›، āridus، ardēre ‹سوختن›، یونانیِ azō و سنسکریتِ āsa- ‹خاکستر، غبار› دیده می‌شود».\",\n  \"sources\": [W+\"Reconstruction:Proto-Indo-European/h%E2%82%82eh%E2%82%81s-\", E+\"ash\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt s.v. as-: 'as-. To burn, glow. 1. Extended form *as-g- in Germanic *askon- in Old English æsce, asce, ash: ASH.' — Nourai's Germanic box verbatim.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Band I p.68-69 (POK_01.txt leaves 76-77)\", \"stance\": \"supports\",\n     \"note\": \"'azgo-: arm. ac'iun \\\"Asche\\\", gr. ἄσβολος \\\"Ruß\\\"; germ. *askōn in aisl. aska, ags. asce, æsce, ahd. asca, nhd. Asche. azgh-? in arm. azazim \\\"dörre\\\", got. azgo \\\"Asche\\\" (*azgōn). Über das schwierige Verhältnis von germ. *askōn : *azgōn s. Feist 72b.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 1.86 'ASHES', SYN.txt\", \"stance\": \"supports\",\n     \"note\": \"'4. Goth. azgō, ON aska, OE asce, OHG asca, etc., general Gmc., fr. a root *as- seen in Lat. ārēre \\\"be dry\\\", āridus \\\"dry\\\", ardēre \\\"burn\\\", Grk. azō \\\"be dry\\\", Skt. āsa- \\\"ashes, dust\\\", Toch. A āsar \\\"dry\\\", Arm. acium \\\"ashes\\\". Falk-Torp 35. Feist 72. Walde-H. 1.65.'\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I, cross-reference lines to *ās-\", \"stance\": \"supports\",\n     \"note\": \"WP files the 'Herd/Altar' and ash words under '*ās- \\\"ausdorrende Gluthitze\\\"' (quoted twice in the surviving OCR), i.e. the same root as Pokorny's later ās-.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"English\", \"words\": \"ash\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Old English æsce/asce (also axe in the Northern texts, whence ME asshe, axe) < Proto-Germanic *askōn, the plural 'ashes' becoming the ordinary form in Modern English; the volcanic sense is from the 1660s. It is not to be confused with the homophonous tree-name ash < OE æsc < PGmc *askaz < PIE *os- 'ash tree' — a completely different word, and Nourai rightly puts only the one here. The Old English -sc- gives ModE /ʃ/ regularly (asce > ash, fisc > fish).\",\n  \"derivation_fa\": \"انگلیسی کهن æsce/asce (و در متن‌های شمالی axe، که در انگلیسی میانه asshe و axe شد) از *askōn ژرمانی آغازین می‌آید و در انگلیسیِ نو صورت جمعِ ashes صورت رایج شد؛ معنای «خاکسترِ آتشفشان» از دههٔ ۱۶۶۰ است. این واژه را نباید با هم‌آوایش ash «درختِ زبان‌گنجشک» اشتباه گرفت که از انگلیسی کهن æsc و ژرمانیِ *askaz و ریشهٔ هندواروپاییِ *os- «درخت زبان‌گنجشک» است و واژه‌ای یکسره جداست؛ نورایی به‌درستی فقط اولی را در این جعبه آورده است. تبدیل ‎-sc-‎ انگلیسی کهن به /ش/ در انگلیسی نو قاعده‌مند است (asce ← ash، fisc ← fish).\",\n  \"sources\": [E+\"ash\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"The box carries no reference of its own (refs=None); checked against Pokorny, AHD, Klein and Buck instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 65 (p.102), s.v. ardent\", \"stance\": \"supports\",\n     \"note\": \"'... Goth. azgō, OE. asce, æsce, \\\"ashes\\\". See ash, \\\"powdery substance\\\"' — Klein explicitly ties English ash to this root and separates it from the tree.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. Ashes / Ash\", \"stance\": \"supports\",\n     \"note\": \"Skeat keeps the two words apart, as here: 'Ash, a tree. (E.) M.E. asche. A.S. æsc. + Du. esch; Icel. askr ...' and, separately, 'Ashes. (E.) The pl. of ash ... M.E. asche, axe, sing.' (the OCR of the etymology proper is damaged).\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. as-\", \"stance\": \"supports\",\n     \"note\": \"'Extended form *as-g- in Germanic *askon- in Old English æsce, asce, ash: ASH.'\"}\n  ]\n }\n]\n\ndoc = {\n \"pdf_page\": 65,\n \"book_page\": 35,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [entry0, entry2]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-65.json','w',encoding='utf-8') as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build65.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-65.json > /dev/null && echo JSON_OK",
 "description": "Write page-65 verification JSON"
}
```


### [2026-09-04T23:27:20.291Z] TOOL RESULT

```
ok
JSON_OK
```


## [2026-09-04T23:27:24.799Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 tools/verify_check.py 65",
 "description": "Run verify_check for page 65"
}
```


### [2026-09-04T23:27:26.663Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'plausible': 3, 'confirmed': 10, 'transcription_suspect': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'partial': 5, 'not_checked': 5}
books consulted: {'silent': 12, 'partial': 5, 'supports': 25, 'contradicts': 2} | by book: {'KLN': 10, 'WEB': 6, 'AHD': 5, 'POK': 4, 'MON': 3, 'IEC': 2, 'BQT': 2, 'HRN': 2, 'FSD': 2, 'SKT': 2, 'LAT': 2, 'WLD': 2, 'HUB': 1, 'SYN': 1}
```


## [2026-09-04T23:27:30.523Z] TOOL CALL #77: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -20",
 "description": "Check all cited URLs are archived"
}
```


### [2026-09-04T23:27:34.423Z] TOOL RESULT

```
526 cited URLs, 21 not yet archived
archived 21, failed 0
```


## [2026-09-04T23:27:38.974Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-65.json'))\nidx={json.loads(l)['url'] for l in open('/home/sfmqrb/git/rishe/data/verification/sources/web/index.jsonl',encoding='utf-8')}\nurls=set()\nfor e in d['entries']:\n    urls|=set(e.get('sources',[]))\n    for n in e['nodes']: urls|=set(n.get('sources',[]))\nprint('missing:',[u for u in urls if u not in idx])\nprint('total urls',len(urls))\nEOF",
 "description": "Confirm page-65 URLs archived"
}
```


### [2026-09-04T23:27:40.878Z] TOOL RESULT

```
missing: []
total urls 12
```


## [2026-09-04T23:28:00.046Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-65.json` is written, valid, and `verify_check.py 65` reports no PROBLEM lines.

**PDF page 65 (book p. 35) — 2 real entries (Arxein/Arkhein, As), 3 redirects skipped, 15 nodes**

- Roots: 2 confirmed. Nodes: 10 confirmed, 3 plausible, 2 transcription_suspect.
- Ref checks: 9 supports, 5 partial, 5 not_checked. Books consulted: 25 supports, 5 partial, 2 contradicts, 12 silent (KLN, POK, AHD/Watkins, WLD, IEC, SYN, LAT, LEW, FSD, WEB, SKT, MON, BQT, HRN, HUB, ARY).
- Key local finds: POK_01 leaf 76 = printed p.68 carries the entire "As" chart verbatim (`ās- … lat. āra "Altar", āreō, āridus (davon ardeō), ārea "freier Platz" … germ. *askōn`); KLN_1966 leaf 64/65 = printed pp.100–102 carries the whole Arxein chart plus `are … formed in 1795 by a decree of the French National Convention, fr. L. area`; FSD vol.2 leaf 423 = printed p.1133 gives hectare `[F., < Gr. hekaton + L. area]` with Nourai's own "2.47 acres"; Moʿin p.39 gives `آر … ۱۰۰ متر مربع (یک دکامتر مربع): هکتار = صد آر`, which also explains the ☞Dekm cross-ref.

Flagged items:
- **As, node #1 (Latin `ara : an area`)** — transcription_suspect, `error_in: "book"`. The page really prints "ara : an area"; but Latin *āra* = 'altar' and the word meaning 'an area' is *ārea*. Both are in Pokorny p.68, and the French daughter (are) is from *ārea*, so `correct_form: ārea`. Nourai's own conflation, not a scan error.
- **As, node #5 (English area, arson)** — transcription_suspect, `error_in: "extraction"`. On the printed chart the connector starts at the bottom of the Latin box and runs to this box; the JSON records `parent: 0` (root). **Data fix for the owner: entry index 2, node id 5, parent should be 1, not 0.** The words themselves are confirmed.

Other substantive notes (not flags): Arxein node #1's "arxt/arkht" are not citable Greek forms (read as ἀρχοντ-, stem of ἄρχων) → plausible; node #5's English `arch-`/`archbishop` did **not** come via French (OE arcebiscop < Eccles. Latin, c. 900), only architect/archive did → plausible; node #7's Latin box is Modern Latin/French, not classical → plausible. Also recorded: Watkins puts ARA but **not** AREA under *as-*, and Ernout-Meillet call the ārea/ārēre link "pas de rapprochement sûr", so the entire French→Persian→English are/hectare branch rests on a link modern Latinists treat as uncertain.
