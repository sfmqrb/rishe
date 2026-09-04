# Verification process log — verify-page-64


## [2026-09-04T23:04:23.011Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 64 only (note the recently added requirements: `derivation_fa`/`note_fa` Persian explanations, and `error_in`/`book_prints`/`correct_form` on any transcription flag). Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-64.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-64.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-64.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 64` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T23:04:25.592Z] AGENT

I'll start by reading the instructions file.


## [2026-09-04T23:04:27.059Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T23:04:27.075Z] TOOL RESULT

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


## [2026-09-04T23:04:27.898Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-64.txt"
}
```


### [2026-09-04T23:04:27.911Z] TOOL RESULT

```
1	=== PDF page 64 (book page 34) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Arg : to shine, white metal  (refs POK:64)
4	#1 (parent #0) [Avestan] refs=POK:64 | erezata : white metal
5	  #2 (parent #1) [Pahlavi] refs=SOD:56 | arzyz : tin
6	    #3 (parent #2) [Persian] refs=HRN:17 | arzîz «ارزیز» : tin
7	#4 (parent #0) [Old Persian] refs=KNT:171 | arda- : light ; ardata : shiny metal, silver ; arda-stâna : (light stand), window frame ☞Stâ
8	#5 (parent #0) [Sogdian] refs=SOD:56 | `rcyc : tin
9	#6 (parent #0) [Latin] refs=KLN; AHD | argentum : silver
10	  #7 (parent #6) [English] refs=None | argent, Argentina
11	#8 (parent #0) [Latin] refs=None | arguere : to clarify
12	  #9 (parent #8) [English] refs=AHD | argue
13	--- entry 1 ---
14	ROOT Ario -> redirect to Al 1
15	--- entry 2 ---
16	ROOT Arkhein -> redirect to Arxein
17	--- entry 3 ---
18	ROOT [Arabic] A.r.q, Araq : to sweat; sweat, juice, liquor  (refs FVA:269)
19	#1 (parent #0) [Persian] refs=FVA:269 | araq «عرق» : sweat, liquor
20	#2 (parent #0) [Arabic] refs=AHD:152 | abŭ-araq : "father of sweat", a spicy plant used in medicine ☞Ab 2
21	  #3 (parent #2) [Middle Latin] refs=AHD:152 | borrâgo
22	    #4 (parent #3) [Old French] refs=AHD | bourrache, borrace
23	      #5 (parent #4) [English] refs=AHD:152 | borage : a spicy salad dressing
24	
```


## [2026-09-04T23:04:35.365Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-64.json && echo \"=====MATRIX=====\" && cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T23:04:35.423Z] TOOL RESULT

```
{
  "pdf_page": 64,
  "book_page": 34,
  "entries": [
    {
      "root": {
        "name": "Arg",
        "lang": "Indo-European",
        "refs": "POK:64",
        "gloss": "to shine, white metal"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:64",
          "words": [
            {"translit": "erezata", "gloss": "white metal", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SOD:56",
          "words": [
            {"translit": "arzyz", "gloss": "tin", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:17",
          "words": [
            {"translit": "arzîz", "gloss": "tin", "script": "ارزیز"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:171",
          "words": [
            {"translit": "arda-", "gloss": "light", "script": null},
            {"translit": "ardata", "gloss": "shiny metal, silver", "script": null},
            {"translit": "arda-stâna", "gloss": "(light stand), window frame", "script": null, "see": ["Stâ"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:56",
          "words": [
            {"translit": "`rcyc", "gloss": "tin", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN; AHD",
          "words": [
            {"translit": "argentum", "gloss": "silver", "script": null}
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
            {"translit": "argent, Argentina", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "arguere", "gloss": "to clarify", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "argue", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Ario", "redirect": "Al 1"},
      "nodes": []
    },
    {
      "root": {"name": "Arkhein", "redirect": "Arxein"},
      "nodes": []
    },
    {
      "root": {
        "name": "A.r.q, Araq",
        "lang": "Arabic",
        "refs": "FVA:269",
        "gloss": "to sweat; sweat, juice, liquor"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "FVA:269",
          "words": [
            {"translit": "araq", "gloss": "sweat, liquor", "script": "عرق"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Arabic",
          "refs": "AHD:152",
          "words": [
            {"translit": "abŭ-araq", "gloss": "\"father of sweat\", a spicy plant used in medicine", "script": null, "see": ["Ab 2"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Middle Latin",
          "refs": "AHD:152",
          "words": [
            {"translit": "borrâgo", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Old French",
          "refs": "AHD",
          "words": [
            {"translit": "bourrache, borrace", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:152",
          "words": [
            {"translit": "borage", "gloss": "a spicy salad dressing", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=====MATRIX=====
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


## [2026-09-04T23:04:45.238Z] TOOL CALL #4: Bash

```json
{
 "command": "grep -n -i -E '^\\s*(FVA|POK|SOD|HRN|KNT|KLN|AHD|BQT|MON)' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -50; echo \"---FVA---\"; grep -n -i 'FVA' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head; echo \"---refs_online FVA/SOD/KNT/HRN---\"; python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['FVA','FVQ','POK','SOD','HRN','KNT','KLN','AHD','MON','BQT','LKT','DEV','PHN','SKT','LEW','LAT','WLD','IEC','SYN','BRT','PHD','NYB','HUB','ARY','ISS']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-04T23:04:50.057Z] TOOL RESULT

```
---FVA---
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
12: TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll 
---refs_online FVA/SOD/KNT/HRN---
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_f
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnair
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317
```


## [2026-09-04T23:04:55.121Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -40; echo \"---\"; sed -n 1,200p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-04T23:04:55.187Z] TOOL RESULT

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
---
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


## [2026-09-04T23:05:28.027Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','KNT','HRN','SOD','KLN','AHD','BRT','PHD','NYB','HUB','LEW','LAT','IEC','SYN','SKT','FVQ','AFM','LKT','DEV','PHN','MON','BQT','ARY','PLA','TAD','ARB','AFA','WEB','FSD','HJB','RCH','CHEUNG','ISS']:\n    v=d.get(k) or {}\n    print(k,'|off:',v.get('page_offset'),'|lf:',v.get('local_file'),'|hint:',(v.get('lookup_hint') or '')[:200])\n\""
}
```


### [2026-09-04T23:05:30.006Z] TOOL RESULT

```
POK |off: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt |hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.i
KNT |off: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt |hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall i
HRN |off: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt |hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered ent
SOD |off: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) |lf: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] |hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD
KLN |off: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt |hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume p
AHD |off: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt |hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the 
BRT |off: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt |hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin glos
PHD |off: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt |hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A
NYB |off: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt |hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
HUB |off: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt |hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
LEW |off: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt |hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
LAT |off: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt |hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
IEC |off: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt |hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
SYN |off: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt |hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed p
SKT |off: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt |hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
FVQ |off: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) |lf: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] |hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
AFM |off: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image |lf: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] |hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أ
LKT |off: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt |hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
DEV |off: leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt |hint: French headword in caps at line start.
PHN |off: leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt |hint: French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
MON |off: None |lf: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Aves
BQT |off: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). |lf: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] |hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'http
ARY |off: printed page = pdf page + 1 |lf: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] |hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword
PLA |off: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). |lf: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] |hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --
TAD |off: 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image |lf: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt'] |hint: Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
ARB |off: None |lf: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt'] |hint: Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.
AFA |off: leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt |hint: Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.
WEB |off: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt |hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabe
FSD |off: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt |hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
HJB |off: leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt |hint: Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers
RCH |off: leaf ~= printed + 93..94 (e.g. leaf 336 = p.242, leaf 587 = p.494); weakly detected, verify by grepping the page number. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: /home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt |hint: Entries are Persian/Arabic in script (poorly OCRed) followed by transliteration and English gloss; grep the English gloss or transliteration.
CHEUNG |off: None |lf: None |hint: 
ISS |off: DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |lf: None |hint: Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) co
```


## [2026-09-04T23:05:33.362Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==73' POK_01.txt"
}
```


### [2026-09-04T23:05:35.043Z] TOOL RESULT

```
schließen'.
WP.  I  81.  WH.  I  63.  Jokl  IF.  44.  22.
I ar{e)-g-  (arg-'?),   rgi-,  erweitert  rg-ro-,  argu-  .glänzend,  weißlich'.  :
Ai.  ärju-na-h  .licht,  weiß';  rajatä-  .weißlich',  rajatdm  hiranyam  .weiß, liches  Gold,  d.  i.  Silber',  rajatdm  , Silber'  mit  auffälligem,  trotz  Osthoff MU.  VI  33  nicht  aus  tiefstufigem  r  (oder  dgl.)  herleitbarem  Vokalismus gegenüber  av.  drgzata-  n.,  apers.  ardata-  , Silber'  (r),  lat.  argentum,  osk. aragetud  .argento',  air.  arggatj  mir.  airgetj  cymr.  arian(t),  corn.  mbret. argantj  nbret.  arc'hant  , Silber',  gall.  ON  Arganto-magus  ]  arcanto-dan  :\ ,Münzmeister',  arm.  arcat''  , Silber',  toch.  A  ärkyant  N.  PI.  f.;  mit  anderer Bildung  gr.  ^xqyvQog  , Silber'  (trotz  dieser  Gleichungen  steht  die  Kenntnis  des Silbers  für  die  Urzeit  nicht  sicher,  s.  darüber  und  über  die  Entlehnungs- frage  Schrader  RL.  IP  394,  G.  Ipsen  IF.  39,  235  f.,  Festschr.  Streitberg 228),  messap.  argorian  (:  aQyvQiov)  ds.,  argora-pandes  (^arguro-pondios) ,quaestor'.  *
Thrak.  i^gyilog  ,Maus',  FIN  "!AQZog  {^Argios).  '
Gr.  S:Qyög  ,weiß,  schnell',  in  Kompositis  dgyL-  :  ägyi-xegawog  ,mit  glänzen- dem Donnerkeil',  dgyi-ödcüv  ,mit  blendend  weißen  Zähnen*"  (danach  auch *dgyLvög  für  ägyewög,  weitergebildet  zu  ägyivösig^  Beiwort  von  auf  weißen Kalk-  oder  Kreidebergen  gelegenen  Städten) ;  ägyalvo)  ,bin  weiß'.
ägyog  wohl  nach  Wackernagel  Verm.  Beitr.  8  f.  aus  *dgygög  dissimiliert, wozu  sich  der  2-St.  agyi-  der  Komposita  verhält  wie  av.  ddrdzi-rad-a-  , feste Wagen  besitzend'  zu  ddrdzra-  ,fest'.  Das  mit  dgyog  lautlich  gleiche  ai. Xjrd-  bedeutet  auch  .glänzend',  ist  also  in  dieser  Bedeutung  mit  dgydi; ,weiß'  etymologisch  identisch  (dazu  auch  ai.  fjlti-,  fjika-  .strahlend').  Ai. Yjrd-  ,schnell',  Rji-svan-  ,der  über  schnelle  Hunde  gebietende  Verbündete Indras'  =  gr.  dgyog  , schnell'  (ebenfalls  von  Hunden,  also  bereits  ursprach- liches Beiwort,  s.  Schulze  Kl.  Sehr.  124),  dgyi-ftovg  .schnellfüßig',  PferdeN Ilöö-agyog,  hält  Persson  Beitr.  828  für  ein  von  dgyog  (rß'd-)  .weiß'  ver- schiedenes Wort  (zur  Wz.  reg-  , gerade'  in  ai.  rßsd-  , gerade  darauf  los- eilend', TJi-I>yd  , dahin  schießend',  usw.).  gegen  Bechtel  Lexil.  57.  der  den Begriff  des  Leuchtens  aus  dem  der  schnellen  Bewegung  geflossen  sein läßt  (vgl.  .blitzschnell')  wie  auch  Schulze  aaO.  Leuchtkraft  der  Farbe und  Schnelligkeit  der  Bewegung  (vgl.  lat.  micäre)  als  versch.  Seiten  der- selben Anschauunor  betrachtet.
65
lioysuov,  iiQye^a  n.  ^das  Weiße  (im  Auge,  Nagel)',  dQyi^sig,  clor,  ägyag {^ao
```


## [2026-09-04T23:05:41.736Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==74||NR==75' POK_01.txt | grep -n -i -E 'arguo|arguere|argu|arzi|Zinn|tin' "
}
```


### [2026-09-04T23:05:43.590Z] TOOL RESULT

```
4:Lat.  argentum  s.  oben;  arguö  , mache  klar,  deutlich;  helle  einen  Sach- verhalt auf,  überführe',  argütus  ,stimmkräftig,  schwatzhaft;  (seit  Cicero auch:)  strahlend,   flimmernd'  und  ^scharfsinnig'.
5:Toch.  A  äi'kij  B  ärkwi  ,weiß'  [*arguio-),  ärcune  , Beiwort  des  königl. Titels',  A  ärki-sosi  , weiße  Welt'  (vgl.  cymr.  elfydd  S.  30);  hett.  har-ki-ü (Jiarkis)  ,weiß'.
```


## [2026-09-04T23:05:48.162Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 185 186 187; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KNT.txt | head -60; done"
}
```


### [2026-09-04T23:05:50.584Z] TOOL RESULT

```
=== leaf 185 ===
ugh not mentioned in the Behistan inscription, must have followed in the same or the next year.
V. THE ACCESSION OF XERXES.
In XPf, Xerxes gives us an account of his sue- cession to the throne: Darius had a number of sons, but—-as was Ahuramazda’s desire—he made Xerxes (presumably not his eldest son, though this is not stated in the inscription) the ‘greatest after himself; and when Darius ‘went from the throne,’ Xerxes—as was Ahuramazda's desire—became king on the throne of his father.
The account given by Herodotus 7.1-4 agrees with this, but gives more details: After Darius re- ceived the news that his forces had been defeated at Marathon and somewhat later that Egypt had risen in rebellion, he started preparations for one campaign against the Athenians and another against the Egyptians. Àt this time there was a dispute between Artobazanes, eldest son of Darius by his first wife, a daughter of Gobryas, and Xerxes, eldest son of Darius by Atossa, daughter of Cyrus the Great, whom Darius had married
after his accession to the throne, as to which should have the succession. On the advice of Damaratus, exiled king of Sparta, Xerxes went to his father and pressed his claim on the ground that he was the oldest son of Darius the King, while Artobazanes was only the oldest son of Darius the private individual. Darius approved the claim, though perhaps the argument was not really needed (Atossa as daughter of Cyrus must have had great influence with Darius, and Xerxes was probably the ablest of Darius's sons), and named Xerxes to succeed him. Before he had finished the preparations for the campaigns, Darius died; whereupon Xerxes ascended to his father's throne.
5 Kent, JNES 2.109-10 ; cf. R. A. Parker, AJSLL 58.373-7. $ Parker, l.c.
164
PART III. LEXICON
This Lexicon includes a concordance to the words in the inscriptions, as well as materials for etymological comparison.
The alphabetic orderisáf dk zgejt6 edn pfo тутіоѕ §zh, while final y and v are disregarded (thus пату has the alphabetic place of nai, and pre- cedes naiba-). Raised letters inserted to show sounds omitted in the OP system of writing also have no effect on the alphabetic order.
References to Part I (the Grammar) are marked by §; they include all mentions of the word or form which add to the information given in the Lexicon, but are not in all instances complete list- ings. The Chapter on Syntax is only sparingly re- ferred to in this Lexicon, since the citations in that Chapter are mostly for passages rather than for words; there is an Index of Passages at the end of the Chapter.
а adv. as prefix and prep. ‘to’; Av. Skt. à, prep. with acc. and abl., ‘to, as far as’ (also with other uses and meanings); pIE *à if = Lt. à ‘from’ (Sturtevant, Lg. 15.145-54), or *0 if = Gk. ó- in ó-xeayós ‘(lying round about), ocean’.
(1) Prefix with verbs ay-, zšnav-, gam-, grab-, jan-, bar-, mà-, yam-; in verbal nouns dyadana-, dvahana-, and in the second parts of compounds Adiyabaukna-, Ariyáramna-, Bagabigna-, also in Akaufaciya-.
(2) Postposition attached to loc. sg. and pl. ($270.1V) and in conj. yada.
(3) Prep. with abl.: yàtà à ‘as far as’, DPh 6, 7; DH 5, 6.
(4) Prep. with adv.: DSe 48.
! a- neg. prefix before consonants (867, 67.1, 0182.1; an- antevocalie, q.v.): Av. Skt. a-, Gk. a~, Lt. ?n-, Сте. un-, pIE *n-. See akarta-, ax áaina-, axsata-, Anümaka-, ayaumani-.
* a- demonst. ‘this’: Av. a- as in GAv. gsm. ahé, Skt. a- as in gsm. asyd, Gk. lsn. є 40, Lt. nsn. tod in ecce ‘lo’; pIE *e-. See also aciy, ada-. Decl., $199.
anã ism. DPe 8 (not to Av. Skt. ana-, cf. Mt. MSLP 19.49-52); XPa 14 (with Wb. KIA 109, Mt. Gr. $326; translated by АКК. a-ga-’, Elam. hi ‘this’, which refutes interpretation of Bv. Gr. $368,
$388, as prep. w. inst. ‘throughout’, Av. ana with ace. ‘along, on’, Gk. дра 'along. ahyāyā lsf, DB 447; DNa 11; DSd 2°; DSe 10; DSf 7, 15; DSg lf; DSi lf, 4; DS} 1°; D8m 5°; D8s If, 3°; DSy 2; DZb 3; DZc 5f; DE 17; XPa 8f; XPc 7; ХВ 12, 24; XPh 9f; XPj; XV 13; A!Pa 13; РЬ if; Аа 1; Ае 4; A’Sdb 1 (ahyd de, $52.VI) ; A?Ha If; А°Не 9, 16f; А#Ра 11; Wb 6; We 7f; Wd 7. ahiydyd ($27) XPb 17; XPd 12; XPjv; XE 17.
aita- demonst. ‘this’ ($260. IIT, $266): Av. адіа-, Skt. elá, PAr. *айа-. айа nsn. ($202) DB 1.44, 45; DNa 48. aita-maty DNb 31. ай�
=== leaf 186 ===
� asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; DNa 54; XPh 60. aitä apf. XPh 30, 35.
Ainaira- sb. ‘Ainaira’, a Babylonian, father of Nidintu-Bel; Elam. ha-a-na-a-ra, АКК. a-ni-ri-’, Ainaliralhya gsm. DB 1.77f.
atva- adj. ‘one’ ($150; §204.1): Av. aéva- ‘one’, Gk. Hom. olos, Cypr. orros ‘alone’, pIE *ozyos. ашат, asm. DNa 6, 7; DSe 6°, 6f; DSf 4, 5; DE 8f, 10; XPa 4, 5; XPb 8f, 10; XPe 4, 5; XPd 6, 7; XPf 6, 7; XPh 5,6; XE 9, 10; XV 7, 8; A!Pa 6f°, 8°; A?He 5f, 6; А?Ра 6, 7.
aiš- vb. ‘hasten’, caus. azSaya- ‘send’: Av. aes-, caus. aéaya-, Skt. 15-, caus. esayatz (§117).
fra + aiš- caus. ‘send forth’: Av. fraei-, Skt. .
preg-. frdiSayam ist sg. imf. (§24, §72, 6181, §215) DB 1.82; 2.19, 30, 50, 72f, 82; 3.2, 18, 30, 84; 5.7. frütsaya imf. DB 3.55, 60, 71.
Auliyüra- sb. ‘Autiyara’, a district in Ar- menia: Elam. ha-u-ti-ja-ru-i§, АКК. ú-ti-ņa-a-ri. Auliyàra nsm. DB 2.58f.
Aura- (Le. A*ura-) sb. ‘Lord, God’: Av. ahura-, Skt. dsura- ‘demon’, pIE *esuro- (6148.1). Aurahya Mazdaha gsm. ({36.ГУЬ, $44) XPe 10. Аита ism. DPe 24 (otherwise Bv. BSLP 30.1.70-3, Gr. §179, 8889; ‘downward’, isn. of aura-, zero- grade of avara-, comparative of *ava-, cf. Ау. aora ‘down’). Elsewhere always in cpd. Auramazdah-.
Auramazdāł- sb. ‘Wise Lord, Ahuramazda’, supreme deity of the Zoroastrian religion: Av. пет, ahurd mazda, РМ. óhrmazd, NPers. hormizd; Elam.. u-ra-más-da., Akky u-ra-ma-az-da. ü-ri-mt-
=
-
LEXICON
12-00 a-hu-ru-ma-az-da-’ ete., Gk. 'Opouacdys; in Av., always two words, usually separated in the Gathas and often in reverse order (Kent, Or. Stud. Hon. Pavry 200-8), but in OP always one word except ХРе 10 (844; for Ашт alone, see under Aura-). Cpd. of *ahura- (see Aura-) + *ma(n)dzdhà- with s-suffix (another! view by Pisani, ef. $185.n3); this is cpd. of pIE *menth- (or is the full grade pIE *math-?) seen in Gk. ёшабо› ‘I learned’, + pIE *dh&- ‘put’, see “da- (Pisani, Riv. Stud. Or. 81-2, takes prior element as *mns-, zero-grade to pAr. manas-, after Wacker- nagel-Debrunner, Altind. Gram. 3.282-3): for formation, ef. Skt. érad-dhà- ‘trust’, Lt. crédit. 670, $156.I, 5160.11; decl., $185.IV.
Auramazdà nsm. AmH 7, 10; AsH 5f, 12; DB 1.12, 60; 4.35, 55, 62, 74, 76, 79f; 5.15f; DPd 1, 7, 13, 15f, 23; DPh 8, 9; DNa 1, 31, 51f, 55; DNb 1, 46, 49: DSe 1; DSf 1,8, 14, 57; DSp 1; DSs 1^, 6f; DSt 1?, 7; DZe 1; DE 1; DH 6f, 8; XPa 1, 18, 20; XPb 1, 21; XPc 1, 12, 15; XPd 1, 17; XPf 1, 45, 48; XPg 12; XPh 1, 32, 49f, 52, 57, 60; XSc 4f°; XE 1; XV 1, 25; A!Pa 1°, 22°; A?8e 7; А?Не 1,18, 19; A?Pa 1, 24, Auramazdà-maiy DB 1.24f, 25, 55, 87, 94; 2.24, 34, 891, 45, 54, 60, 68, 86, 96; 3.6, 16f, 37, 44f, 61f, 661, 87; 4.60; DNa 50 -dà- iy, With omission of m* (§52.VI); DSf 19; XPh 45. Auramazdd-taiy DB 4.78. Auramazda-lay (852.11) DB 4.58. Auramazdd-|Sém] DB 5.311.
Auramazdàm asm. DB 1.54f (Auramazám, $52. VI); 5.16, 18f, 32, 34; DPd 211; DNa 54; DSf 15f, 18; XPf 211, 29; XPh 40, 50, 53, 59; XSe 4.
Auramazdéha gsm. AmH 7f; AsH 10; DB 111, 14, 18f, 22f, 26, 60, 68, 70, 88, 94f; 2.3, 25, 35, 40, АЎ, 54f, 60, 68, 86f, 97; 3.6f, 17, 38, 45, 62, 67, 87Ї; 44, 6, 41, 44, 46, 52, 60, 88; 5.16f, 32f; DSF 12, 21°; DSfv 55f°; D812f; XPb 26f; XPd 16; XPg 3,8; X881; XV19. | Auramazdáhà DPd 4,9; DPe 6f; DNa 16, 35, 49, 56{; DNb 6, 47f; DSe 15, 35, 42; XPa 12, 16f; А?Не 16. Auramazdahà (852.1II; $131; $185.IV) X Pf 34, 43; XPh 14, 33, 37, 44; A'Pa 18f.
AM nsm. (842) DSe 50°; DSi 3°; DS} 4, 6°; DSk 4; DSn 2^; D'Sa 3; A*Sa 4° (as gen., 5818.1), 4; A’Sd 3; А?На 5° (as gen), 6. АМташ DSk 5; D8m 3. AMm asm. DSk 4. AMha gsm. DSa 4; ligature ($42) DSk 4. AMha DS] 3°, 5; Аа 3. AMha or АМ№ DSd 3°; DSi 4°; DSm 5°; D8o 3°; D’Sb 4°.
165
Akaufaciya- adj. sb. ‘man of Akaufaka’; pl. a province of the Persian Empire: АКК. a-ku-pi-i-1$. Deriv. of * Akaufaka- ‘Kohistan’, prefix à + kaufa- ‘mountain’ + adj. suffix ($113, 814411; ef. Hz. AMI 8.72; Kent, Lg. 13.298-9). Akaufaciyd npm. XPh 27. |
akarta- adj. ‘not made, no
=== leaf 187 ===
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
```


## [2026-09-04T23:05:59.198Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==193' KNT.txt | grep -n -i -E 'arda|ardata|ardastana|window|silver' ; echo \"=== full-file grep ===\"; grep -n -i -E 'ardastana|arda-stana|window' KNT.txt | head -20"
}
```


### [2026-09-04T23:06:00.811Z] TOOL RESULT

```
=== full-file grep ===
586:ardastana- ‘window-frame’, Elam. har-da-i5-da- па.
3312:DPc = Darius, PegsEPOLIS с: Trilingual, one Jine only, repeated 18 times on the window cornice of the same room of Darius's palace. Tm. Lex. 35-6 (1908); Wb. KIA xvi, 80-1 (1911); Hz. ApI 22-3 No. 9; Sen, OPI 89-90 (1941).
3363:XPe = Xerxes, Persepouis x: Trilingual, in duplicate (see below), each version 4 lines, with slightly differing line-divisions in OP; ea on a post of the north door, above the. sculptured figure of the king; eb on a post of the east door, also above the king’s figure. There are also numerous other copies of this inscription inside and outside the doors and windows, frequently in one-line and two-line arrangements (Cameron’s data). Tm.
4042:TRANSLATION оғ DPe: Stone window-frame, made in the house of King Darius.
5069:ardastāna- sb. ‘window-frame, window cor- nice’: arda- ‘light’ as in OP ardata- ‘silver’, Skt. rajatd- ‘white’, rjrá- ‘red’, Gk. àpyós ‘shining’ + stāna- ‘place’ (831, §160.Ib; Foy, KZ 35.48; hardly as with Bthl. AiW 193, or Hz. Ар! 74-6); ‘light- place’. ardasténa nsm. DPc.
5530:daru- sb. ‘wood’: Av. déuru-, Skt. dáru-, ef. Gk. доро ‘spear’. düruv (§181) nsn. DSf 41, in phrase asd атир ‘ebony’, lit. ‘stone wood’ (§308.- nl), so called because of its hardness; but also probably аз@ because of the assonance translated Akk. aban ‘stone’, ef. Hebr. eben ‘ebony’, Gk. Веро, from Egyptian hbnj ‘ebony’ (J. Duchesne- Guillemin, BSOS 10.925-7 [1942], noting that acc. to Hdt. 3.97 the Egyptians paid a tribute of ebony logs to the Persian King). Not to be normalized dārwa to root !dar- and the phrase taken as ‘copper’ (Scheil 21.30; Kent JAOS 51.208, 53.18- 9), or as ‘iron’ (Ву. BSLP 30.1.60; who also sug- gests that dáruva may be an adj. referring to some kind of tree); not asé + instr. déruv ‘window frames of wood’ (König, Burgbau 64-5); not asd süruva ‘lead’ (Hz. Ар] 299), to Av. srva- ‘lead’ (Bthl. AIW 1649), for the slight traces do not con- firm initial s". — [dár|uv asn. DSf 51 (so Hinz, Orientalia, soon to appear; not {23mal}uv, see Lex. S.V.).
```


## [2026-09-04T23:06:07.396Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# char offset of line 5069 (1-based)\noff=sum(len(l)+1 for l in lines[:5068])\nleaf=t[:off].count('\\f')\nprint('leaf',leaf,'-> printed p',leaf-21)\n\"; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==193' KNT.txt | grep -n -E '^1[0-9][0-9]$|ardata|arda-' | head"
}
```


### [2026-09-04T23:06:09.095Z] TOOL RESULT

```
leaf 193 -> printed p 172
---
```


## [2026-09-04T23:06:15.064Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 192 193; do echo \"=== 0-based leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KNT.txt | grep -n -E '^\\s*1[0-9][0-9]\\s*$|ardastāna|ardastana|LEXICON'; done"
}
```


### [2026-09-04T23:06:17.023Z] TOOL RESULT

```
=== 0-based leaf 192 ===
=== 0-based leaf 193 ===
3:LEXICON
10:ardastāna- sb. ‘window-frame, window cor- nice’: arda- ‘light’ as in OP ardata- ‘silver’, Skt. rajatd- ‘white’, rjrá- ‘red’, Gk. àpyós ‘shining’ + stāna- ‘place’ (831, §160.Ib; Foy, KZ 35.48; hardly as with Bthl. AiW 193, or Hz. Ар! 74-6); ‘light- place’. ardasténa nsm. DPc.
12:171
```


## [2026-09-04T23:06:21.910Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i -E 'arzîz|arzīz|arziz|arzīž|Zinn' HRN.txt | head -20; echo \"=== leaf 38 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==39' HRN.txt | head -40"
}
```


### [2026-09-04T23:06:23.651Z] TOOL RESULT

```
5162:574. dendün 'Zahn*^), dendäne 'Mauerzinne'.
10830:aw. aonya-, Bedeutung *Zinn sehr unwahrscheinlich;
=== leaf 38 ===
- 17 —
und Tomaschek (Pamirdialekte, 806) vergleichen
skr. ksäuma- 'gewobene Seide* {^uparaMäuma-),
ehe ohne s. he (No. 247).
66. e'iter 'Stern*.
phlv. a/tar; arm. LW. a/JarK 'Horoskop*.
Zusammenhang mit aw. apa^tara-, apa/^ra ist
unwahrscheinlich (Hübschmann, ZDMG. 38, 428,
Bartholomae, ZDMG. 42, 154).
67. erj.'Wert' (Sahn. I, 2 Vers 16), erjmend.
aw. arejah- 'Preis, Wert'; phlv. arj^ arjniand;
ai. vergl. arghd- 'Preis, Wert'.
oss. ary (31); arm. yargem 'ehren, schätzen' etc.
(Hübschmann No. 210).
gybis ^^^ 'Wert', erzan^ erzänis, erzTden,
Käs. ezü^ azün, ajiyd, ajiyd, mit Ausfall des r, wie
arm. LW. (?) azan (de Lagarde, No. 25).
aw. arejah-, arejaiti; phlv. arj, arjän, arjamk^
arJUan, päz. arzän etc., arm. LW. (?) armn 'gebührend*,
armnij armnavor; ai. drhati 'es ist wert*.
afy. yarz 'Fähigkeit, Wert*.
68. erz'Ti^ 'Blei'.
arm. arcic.
Geldner' s Gleichstellung mit aw. arezazi- (Yt. 13,
45, KZ. 25, 558) ist lautlich unmöglich; ebenso die
Ableitung von aw. erezata-, skr. rajatd-.
Die Heimat des Wortes ist noch durchaus unbekannt.
69. ers 'Thräne*.
mäz. asr; Käs. asl,
aw. asru- Thräne*; phlv. ars; ai. dgru-; lit. aszarä.
kurd. asr (Houtum-Schindler), {stir^ istir^ histir^
Jaba-Justi, sind wegen des t zweifelhaft); bei. als
(431).
Die indog. Urform war nach Bugge (BB. XIV, 72)
*ddJcru-, da auch gr. ödxpv, acymr. dacr, air. dSr, lat.
lacruma, got. tagr, ahd. zahar dazu gehören sollen.
Mindestens ist eine Dialektspaltung anzunehmen; viel-
U o r n , Qrundriss d. neup. Etymologie. 2
```


## [2026-09-04T23:06:37.755Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB ===\"; grep -n -i -E 'erz.z|arz.z|arcic' HUB.txt | head -20; echo \"=== PHD ===\"; grep -n -i -E 'arz[iī]z|tin\\b' PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i -E 'arz[iī]z|arzīz' NYB_vol2_glossary.txt | head; echo \"=== SOD grep ===\"; grep -n -i -E \"rcyc|'rzyz|arz[iī]z\" SOD.txt SOD_pages.txt | head -20"
}
```


### [2026-09-04T23:06:37.879Z] TOOL RESULT

```
=== HUB ===
313:liche Name fiir *Blei' ist surb, Urspriinglich gilt arzzz
314:fiir beide Metalle, indem man zwischen weissem arztz
315:= 'Zinn' und schwarzem arziz — 'Blei' unterschied.^)
8077:phi. tactk Bdh. Gl. 107 (oben p. 46). Nach r: arztz *Blei,
8078:Zinn = arm. arcic; hargiz = hagirz *jemals' (oben p. 105)
=== PHD ===
PHD.txt:27:r ‘Notes on the transcription of Pahlavi’, Bulletin of the School of Oriental and African Studies, xxx, pt. 1 (1967), 17--29.
PHD.txt:32:Sincethe ambiguities ofthe script make a mechanical translitera- tion of one letter by one roman symbol of no practical value, a certain amount of interpretation is essential, This interpretation can be based, either directly or by the use of analogy, on the less ambiguous evidence of the above-mentioned earlier documents of the language. With this help it is possible to go far in distin- guishing between the original values °’, й, dy, etc., of -», n, w, Р of у, and so on. But it is neither necessary nor desirable to go beyond this by attempting to give closer “phonetic” values to the letters, such as r for written /, or x for written h. For example, Sy hwl represents xwar ‘sun’, but to transliterate it *xwr entails both confusion with the true letter r \ and the introduc- tion of even greater ambiguity into the interpretation of .». It is better to accept that the scribes wrote r and / almost indis-
PHD.txt:63:1 But see Kaj Barr, ‘Remarks on the Pahlavi ligatures JO and ў’, Bulletin of the School of Oriental Studies, viii, pt. 2 (1936), 391-403.
PHD.txt:214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
PHD.txt:2577:lead (n.) arziz, srub.
PHD.txt:2579:leaden arzīzēn, srubēn.
PHD.txt:2986:opposing hambasānīg, Jud-dadestin.
PHD.txt:3221:priestly office āsrēih, hérbedih; ~ school hérbedestin; ~ studies hérbedestanih.
PHD.txt:4019:tin arziz; (a.) arzizén.
PHD.txt:4958:[126] TIN Fans -į WOS abāzī мка» пеҳу abazsart wet ren abāzsārīh!
PHD_mackenzie.txt:124:  I 'Notes on the transcription of Pahlavi', Bulletin oj the School oj
PHD_mackenzie.txt:153:of the language. With this help it is possible to go far in distin-
PHD_mackenzie.txt:314:Bulletin of the School of Oriental Studies, viii, pt. 2 (1936), 391-403.
PHD_mackenzie.txt:965: ajgahAn ['fgh'n' I M 'jg'h'n, N azgahtin] lazy, indolent.
PHD_mackenzie.txt:1198:arziz pleye I M '1"zyz, N -] tin, lead.
PHD_mackenzie.txt:1199: -en [-yn'] tin, leaden.
PHD_mackenzie.txt:1774:leidan, tin- [cytn l , cyn- I M cyydn, cyn-, N -] gather; pile up.
PHD_mackenzie.txt:2245:tin"', v. fno.
PHD_mackenzie.txt:2584:griwbin [glywp)n' I N giribtin] neck-guard, gorget.
PHD_mackenzie.txt:4669:stin-, v. stadan.
=== NYB ===
=== SOD grep ===
SOD.txt:16989:1420  >rcyc   M  (yjj)^ 
SOD.txt:16990:arziz   ©MP  }rzyz;  Arm.  arjij 
SOD_pages.txt:7869:1420 >rcyc M                                         (yjj)^          splendid
SOD_pages.txt:7870:     arziz ©MP }rzyz; Arm. arjij                                     TSP 6,15,74, 152 & etc.
```


## [2026-09-04T23:06:47.283Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:7868])\nleaf=t[:off].count('\\f')\nprint('leaf',leaf,'-> printed p',leaf-66)\n\"; echo \"=== context ===\"; sed -n '7860,7880p' SOD_pages.txt"
}
```


### [2026-09-04T23:06:49.060Z] TOOL RESULT

```
leaf 121 -> printed p 55
=== context ===
      Dhy. 358, BSTBL        :                                  1431 >r8>yp>kc B                                  tj^j.
1419 >r>sk S                                         jl^u^j          arSefakc ©f. adj. ^'r^y p'y
                                                                     radiant
      arsk ©<Av. araska; MP yrysk ©nom. -w
      envy                                                           TSP 9.37
         =>>rsk(>}
                                                                1432 Wy p»y B                                 /^„x-^
      Anc. Lett. 5.5                                                 arSefc OrS'ypy)

1420 >rcyc M                                         (yjj)^          splendid
     arziz ©MP }rzyz; Arm. arjij                                     TSP 6,15,74, 152 & etc.
     tin, lead
                                                                1433 Wyp'y pyyy       M        jUj>. J JL r0)^Uily^ Jx-
      Sogdica. 27.30
                                                                     orSefi Payi
1421 V8     B, S                            VL-T JL. <trtuo
      ar6/9 ©<*ar0a-, Khwar. V0         ^'rS'rn'k                    a Manichcan god (Jesus the Splendour) ?
      millstone
                                                                     Sund. Listc. 1994,457-8
      SCE 231; MDii p59.8
                                                                1434 VS'ypy =* 'rS'y p'y
```


## [2026-09-04T23:06:57.211Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '300,330p' HUB.txt; echo \"=== leaf/page ===\"; python3 -c \"\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (313,8077):\n    off=sum(len(l)+1 for l in lines[:ln-1]); leaf=t[:off].count('\\f'); print(ln,'leaf',leaf,'-> p',leaf-10)\n\"; echo \"=== 8070-8085 ===\"; sed -n '8070,8085p' HUB.txt"
}
```


### [2026-09-04T23:06:59.181Z] TOOL RESULT

```
ist lautlich unmoglich. Nordbal. Ciz%na = *5jfwa sieht
ans wie ein dem Persischen entlehntes *(ldina, das
sonst nicht vorliegt. Osset. aiddnd ist lautlich nicht
klar, noch weniger kurd. nainih Afgh. dhina, ahTna^
Glina ist LW.
65. Np. ahreSum *Seide' ^ arm. LW. aprisum, apresum
setzt ein phi. apresum (aus *apare§um^ *uparesum u.s. w.)
voraus. Auch die iibrigen hier angefiihrten Worter
flir *Seide' sind wohl sammtlich aus dem Neupersischen
entlehnt, ebenso das syr. Wort, vgl. de Lagarde, G. A.
p. 7.
68. Np. a/i^Tz heisst auch 'Zinn\ vgl. Gazophyl. s. v. stagno,
Rosen, Neup. Sprachfuhrer p. 35 u. s. w., der eigent-
liche Name fiir *Blei' ist surb, Urspriinglich gilt arzzz
fiir beide Metalle, indem man zwischen weissem arztz
= 'Zinn' und schwarzem arziz — 'Blei' unterschied.^)
Auch die Armenier nennen Blei schwarzes ardic, Im
Pehlevi musste das Wort *arctc lauten. Geldner's
arezazi' (nach Darmesteter = *bataille*) habe ich
schon KZ. 27, 101 abgelehnt.
69. Vor dieser Nummer konnte arts *Wachholder mit
seinen Nebenformen {avirs u. s. w.) erwahnt werden,
mit denen Geiger bal. apurs 'Wachholder* zusammen-
gestellt hat. Leider steht nicht fest, welche der ver-
schiedenen persischen Formen richtig ist.
70. Die neupers. Formen ars, aras, ras = *Elle' sind an
sich auflfallig (aus altem ars hatteias, aus altem aras:
raS werden miissen) und stimmen nicht zu zd. cLrstya- 2),
das im Neupersischen zu *ast' geworden ware. Auch
die Bedeutung von drstya- fDaumen* oder *Klafter etc. ?)
Vgl. F r e i t a g , arab. Wb. a. v. rasas.
=== leaf/page ===
313 leaf 22 -> p 12
8077 leaf 236 -> p 226
=== 8070-8085 ===
Entscheidung hat', phi. v{i)c%r , arm. vcir 'Entscheidung,
Richterspruch' (oben p. 94), vgl. Noldeke, Tab. 53, 444;
dihltz, dahliz 'Vorhalle, Halle* = arm. dahlic 'Zelle' (5. Jhd.),
s. p. 263; Vahriz N. pr. Tab. 223 — arm. Vahric (Laz.
Pharp.); Suff. zi in sagzt 'Sake' (s. p. 240), razT Von Rai'
(davon 'Pa^inrfvrj 'Rai' bei Theophylact), tctzi 'arahiscli =
arm. sagcik, phi. racik West, PT. II, 329, arm. tacik (5. Jhd.),
phi. tactk Bdh. Gl. 107 (oben p. 46). Nach r: arztz *Blei,
Zinn = arm. arcic; hargiz = hagirz *jemals' (oben p. 105)
= phi. hakard? H. 1092.
Statt z erscheint jf, in : vaj *sprich !' (dialektisch),
haji = v€l,0 *das leise Recitiren religioser Formeln (der
Parsen !) zu skr. zd. vac 'sprechen , guvctsa 'Schelten' ^= skr.
vivad- (oben p. 104) ; amdj 'Pflugsterz , g. mCLtk, arm. mac (?);
tajar *heizbares Winterhaus', arab. tazar 'Sommerhaus* =
ap. tacara-, arm. tadar 'Tempel, Palast, Haus'; varj 'Grosse,
```


## [2026-09-04T23:07:08.890Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls | head -60; echo \"=== ISS ===\"; ls -la ISS_alt_DKS.txt 2>/dev/null; grep -n -i -E \"^arzīz|^arziz|arrīza|ysāre\" ISS_alt_DKS.txt 2>/dev/null | head"
}
```


### [2026-09-04T23:07:08.975Z] TOOL RESULT

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
=== ISS ===
-rw-rw-r-- 1 sfmqrb sfmqrb 3409804 Sep  4 14:06 ISS_alt_DKS.txt
5404:büsivrássei — bihan- 293 Gara people'; v r60, 20323 süvarebdstd ‘twenty-one’; H 20, 1226 füvarebistamye hadai 'twenty-first day’; K 138:923 Айта tti bistd Пата bujse ' what are these twenty advantages, virtues?', Tib. ii-iu дар де-па K 138921-2 ttye hamgasa bistä bujse һата kaña 'of this in total the twenty virtues, advantages are to be conceived', Tib. deyi yon-tan-gyi phan-yon üi-sur ses-par bya-ste; V 34624 bástd ysāre '20,000'; Manj. 71 basta ysüra, = Мап). 71 dvi Буйга 'two myriads’. Ordinal, Sid. ra8vr pegkald bestá ' twentieth chapter! with -d for -am, Tib. lehu-ste, Hi-su-ba тасов-хо. To Tum&uq Saka bista 'ao', bista ратізі '25'; Av. visaiti, Sogd. Chr. wystmyg, Zor.P., vist, N.Pers. bist, Balóct gist, Oss. D. insdj, І. ssddz, Wanetsi їшї, Pašto wol, #1, Orm. jistu, Parāčī yust Yidya wisto, Sanglééi wist, Waxi wist, Suyni ёәдіз (='2 x то"). IE Pok. 1177 ui-km-t-i, O.Ind. vimsati, Greek tikom, Lat. uiginti, O. Welsh uceint.
6126:mästa- 'great', K 139:959 mistä rre ‘great king", Tib. rgyal-po čhen-po; v 108, 30v5 gen. plur. icuirnu mástanu rrundánu ‘of the four great kings’, BS caturnam maha- rüjüüm; voc. plur. V 108, 3ovs umyau mástyau rrundyau ‘you great kings'; V 131, 523 másta rre; acc. sing. V 38or2 mástu spdiainau Баги 'great fowery rain’, BS mahà-mündarava-puspa-varsa m; Manj. 417 siravü byan- dada mesta 'they got great joy’; ш 88:136 mistye hvande 'adult men'; K 47:53 mistä himye һе became adult’; oblique fem., SuvO. 24v5 11000 mastáñe hámemáte jsa hümáta “these arose from great becoming', BS ete mahabhüta; SuvO. 36r7 mástáiie siratete jsai ' with great joy', BS талай praharsena; SuvO. 36v3 mistáie rrutye padamgye jsa ' with great royal display’, BS mahata raja- anubhävena; with -Ка-, K. 38:134 уза yi maistáka ' (the woman) was old, adult’, =K 29:197 strriya harya mestaka uda ‘a woman remained adult (dyadic)'. Compounds, ш 1, бг2 mästa-gvāroñä jsa ' with great talk’, = 8, 16v2 mista-gvüraufe jsa, possibly BS prapanca- 'idle talk’; I 159, 73У5 mista-ujäm (gen. plur.) 'pregnant', it 45:66 maista-ujat UI 1541 (miysta-ñri тїї ' pregnant women" (see s.v. пга- 'belly"); K. 140:997 mistá-musdi gyastaud gyastá baysá ' the most merciful deva- of devas Buddha’, Tib. omits, parallel. to BS mahakarunika-. Abstract, Z 22209 mdstatele; V 343, 85vi hauda ysāre ggampha mästate ' of 7000 yojana measures large', —85v3 mástetd, BS G 37, Soar sapta-yojazta-sahasra-pramünah ‘having the measure of 7000 yojanas!. Comparative mästara-, mistara, superlative mästama-, mistama-, see s.v. mistara-,
```


## [2026-09-04T23:07:16.774Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== DKS arziz ===\"; grep -n -o -E '.{200}arz[iī]z.{200}' ISS_alt_DKS.txt | head -5; echo \"=== BQT v1 ارزیز ===\"; grep -n 'ارزیز' BQT_v1_pages.txt | head -10; echo \"=== ARY ===\"; grep -n 'ارزیز' incoming/ARY/ARY_pages.txt | head; echo \"=== MON ===\"; grep -n 'ارزیز' MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt | head"
}
```


### [2026-09-04T23:07:16.943Z] TOOL RESULT

```
=== DKS arziz ===
=== BQT v1 ارزیز ===
16979:۳ در هاون ارزیز
=== ARY ===
2281:فارسی (۳8۵۵۷):__ ارزیز (به چم قلع , فلز سپید و نقره فام) 2
=== MON ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:9925:ارزیز: 72 (.) (شیم.) فلزی است سفید؛ 
MON_part2.txt:14162:قلع: اهر [غ.] (.) (شیم.) ارزیز و آن فلزی 
MON_part2.txt:24213:لحیم کنند مانند: ارزیز» قلعی و بوره. (مج.) 
MON_part2.txt:53331:(ارزیز) برآورده شده. (ص.) استواره 
MON_part1.txt:9925:ارزیز: 72 (.) (شیم.) فلزی است سفید؛
```


## [2026-09-04T23:07:21.836Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY ctx ===\"; sed -n '2255,2300p' incoming/ARY/ARY_pages.txt; echo \"=== ARY page tag ===\"; awk 'NR<=2281 && /\\[pdf page/ {p=$0} END{}' incoming/ARY/ARY_pages.txt; grep -n '\\[pdf page' incoming/ARY/ARY_pages.txt | awk -F: '$1<2281' | tail -2"
}
```


### [2026-09-04T23:07:23.795Z] TOOL RESULT

```
=== ARY ctx ===
ن
[pdf page 79]
۰ ارزء ارزش» ارزیدن
ارمتی (۸48074): 26 پسگشت‌ها سم دا ۳
مس سم سس
ایرلندی کهن (5نج! صا0): 7 340 میت نا
هنبت (4177]78): ۸4۰ 585 (3030883 ۰۰ | تمد
برهان قاطع + : ۷
بادداشت. :
چم این واژه در زبان ارمثی: سرود. ۰
چم این واژه در زبان ابرلندی کهن: آسمان» عرش.
فارسی (/(۳88۶/4): ارزء ارزش؛ ارزیدن ۸۷ ق۸378 ,۸72
جم انگلیسی سرواژه‌ی فارسی؛ ابا
هند و اروپایی ((1۸00-81702۴4): 58 قآن ۸61" ‎٩۹۸10112,‏
‏اوستایی (۸1287:4): ۸۹۳7۸11 ,1 ۸75[۸7
پهلری (/۷ساتله): ,۸210۸81 ,۸82 پسگشت‌ها ارات اه اد ات۲
۸1137 333 یت دا
اوستی (0888770): ۸6 9 (#نات۷۸) :5 مازمط۳0
بونانی 0728/0): ۸88810 بطفاطل ۸‏ |11 :للع از
لیتوانی (00الاهتال7/): گاله 356 ناه
لنونی (لتی) (/771۵2ها): هه برهان قاطع : ۱.۲
پروسی کهن ((۶8۷351۵ 0ا0): ۸۲.6۸8
یادداشت,
معنی اين واژه در زبان بونانی؛ فایده.
معنی این واژه در زبان‌های بالتیک(لیتوانی و لتونی و پروسی کهن): دستمزد.
بفب‌
فارسی (۳8۵۵۷):__ ارزیز (به چم قلع , فلز سپید و نقره فام) 2
هند و آروپایی (10/00-8172025۸۷): -۹611 ,(۸/۸01* ,۸6۰ ۸350۰
اوستایی (4۲88740): -7۸ 0832۸ تخاری ۸ (۸ (فلقهتل70): ,286۸۲۲
پارسی باستان (۶8۹1۸/۷ 010): ۸0۸7۸۰ ۸
پهلری (۲7مانله): ۸321280 ,۸717 تخاری 8 (8 [(۵ل70701۸): ره ۳۹
[pdf page 80]
نج
رش» زش. آرش (یکان قدیمی برای سنجش دراز) / ۸۱
ساسکریت (84(/907. ۰ ,قق۸لا ۸71

1 8 ها 0 پسگشت‌ها آشک رش دنا
ارمنی (470400400): ۸ نس
یونانی 0758/0): ۸۹061805* مت 0 (۸011) اک آ رن ان
لاتین (712ل): زا رد 9 (۸653۲) ما02
فرانسه (تل/۳82): 7 7 (11) :۸4۸0/23
ایتالیایی (لمفلل7/): 0 41 (811783) ماه
رومانی (۸(74(ا): انیا 9 (۸۲0113 ۲1۲1 ۸۳) :00/5
ایرشدی کهن (تقلق! ۰:02 ,۸800۸7 ,49 (۸08317)

۸۸7 0 ((۸301) +57
=== ARY page tag ===
2226:[pdf page 78]
2256:[pdf page 79]
```


## [2026-09-04T23:07:39.933Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN borage ===\"; grep -n -E '^borage|borrago|bourrache' KLN_1966.txt KLN_1971.txt | head; echo \"=== SKT ===\"; grep -n -i -E 'BORAGE|borrago' SKT.txt | head; echo \"=== WEB ===\"; grep -n -i -E 'borage|borrago' WEB_vol1.txt | head; echo \"=== FSD ===\"; grep -n -i -E 'borrago|bourrache' FSD_vol1.txt | head; echo \"=== LKT ===\"; grep -n -i -E 'borrago|bourrache|borage|arak|araq' LKT.txt | head -20; echo \"=== DEV ===\"; grep -n -i -E 'BOURRACHE|ARAK|borrago' DEV.txt | head; echo \"=== PHN ===\"; grep -n -i -E 'BOURRACHE|ARACK|ARAK' PHN.txt | head"
}
```


### [2026-09-04T23:07:40.079Z] TOOL RESULT

```
=== KLN borage ===
KLN_1971.txt:31878:borage, n., a blue-flowered plant used in salads. 
KLN_1971.txt:31880:and F. bourrache)y fr. ML. borrdgdy ult. fr. 
KLN_1966.txt:5360:Borachio,  n.,  name  of  a  drunkard  in  Shakespeare’s Much  Ado  About  Nothing.  —  Sp.  borracho, 'drunk,  intoxicated’,  fr.  L.  burrus,  ‘red’  (see burro);  so  called  in  allusion  to  the  red  com¬ plexion  of  intoxicated  people, boracic,  adj.,  boric.  —  See  borax  and  -ie. borage,  n.,  a  blue-flowered  plant  used  in  salads. —  ME.,  fr.  OF.  borrace  (cp.  its  variant  burage and  F.  bourrache),  fr.  ML.  borrago,  ult.  fr. Arab,  abu  ‘ arak ,  lit.  ‘father  of  sweat’,  so  called by  the  Arab  physicians  because  of  its  sudorific effect.  See  abbot  andc  p.  arrack, boraginaceous,  adj.  —  Formed  with  suff.  -aceous fr.  ML.  borrago,  gen.  borrdginis.  See  prec.  word, borate,  n.,  salt  of  boric  acid  ( chem .)  —  See  boron and  chem.  suff.  -ate.
=== SKT ===
2091:Borate.  (F.  — I^wL,)  Fonnerly  iv»r- ^f».  —  y.  Ifourraihe.  —  Low  L.  terraginem^ ace.  of  hcrrago,  borage ;  prob.  named  from iU  roughnesa.  Pcrfaaps  from  Low  L.  hprra, htma,  rotigfa  hatr  (whence  F.  iomrrt,  Ital. ^rrtt);  ice  BurL
=== WEB ===
7207:a-na/qua, n. (Sp. Am.] a small tree of the borage family, with hard, close-grained wood, found in Texas and Mexico. Also spelled anagua,
22100:bor/Age (biir’), n. [ME. borage, burage; LL. borrago, borago, from borra, the hair of beasts.] a plant of the genus Borago, used medicinally for its soothing and perspiratory properties and sometimes used in salads: written also burridge.
22101:bor/Age-wort, n. any plant belonging to the borage family.
22102:Bo-rag-i-na/cé-ae, ge [L., from borago, boraginis, borage, and -acez.] a natural order of plants, with cup-shaped blossoms, known as the borage family, chiefly found in the northern temperate regions. All the species have a demulcent, mucilaginous juice and their surfaces are covered over with white hairs. Alkanet, comfrey, and the forget-me- not belong to this family.
22105:Bo-ra’go, n. (LL. borago, borage.] the type genus of the order Boraginacez, natives of the Mediterranean region. It is a small genus, consisting of three species, of which Borago officinalis is the most common.
22190:one who bought or sold the parliamentary representation of a boroagh: bor-rach’io (-ys), n. same as borachio. bor’rage, n. same as borage. bor-rag-i-na/ceous, a. same as boraginaceous. bor’rel, a. rustic; rude; ignorant. (Archaic.] bor’row, v.t.; borrowed, $t., DP.; borrowing, ppr. [ME. borowen, borwen; S. borgian, to
48278:amily Cynipide. ca 2. {c—-] an insect of this genus; a gallfly. = ¢yn-0-cé-phal/ic, a. pertaining to a cynoceph- alus; dog-headed. ‘cyn-6:ceph/a-lous, a. cynocephalic. Cyn-0:ceph’a-lus, n. [L. cynocephalus; Gr. kynokephalos, the African dog-headed ape: kyon, a dog, and kephalé, head.] _1, a genus of baboons of the family Cynopi- thecidz. _ 2. [c-} a dog-faced baboon. Cyn-6-glos’sum, n. [L. cynoglossus, a plant named the dog-tongued by Pliny.} a genus of plants of the borage fam: having about sixty species, of which six are found in North America. Cynoglossum officinale is the hound's-
87112:US. wpis séal, the common seal, Phoca vitu- ina. Har BIs wätch, a watch kept while a ship isin arbor. har’bour, n., v.t. and v.i. harbor: British spell- ing. har’béur Age, x. harborage: British spelling. har’bréugh, har’bréw, n. harbor. [Obs.] hard, a.; comp. harder; superl. hardest, (ME. ; AS. heard, hard. firm, brave]
88996:summer heliotrope; a small shrub, Tournefor- tia heliotropoides, of the borage family
89006:Hé.1i-6-tr6’pi-um, z. a genus of plants of the borage family.
=== FSD ===
46815:European  herb  ( Boraqo  officinalis) with  ovate  leaves  and  blue  flowers in  terminal  clusters.  An  infusion of  the  leaves  and  flowers  is  used  as a   demulcent  and  diaphoretic  and in  making  cooling  drinks.  [   <   LL. borrago,  <   borra,  burra,  rough  hair; 6ee  bolt2,  r.]
46821:bo-r&g*I-nS'ce-€,  n.  pi.  Bol.  A   largo family  of  gamope talons  plants  —   the  borage  family  —   chiefly rough-hairy  herbs,  having  usually  alternate  entire  leaves, 5-parted  symmetrical  flowers,  and  a   4-lobed  ovary  forming In  fruit  four  1-seeded  nutlets.  It  embraces  68  genera  and about  1,200  species.  [   <   LL.  borrago;  see  boeage.1 bo-rag"I-na'ceons,  a.  bo"ra-gIn'e-ous;,
=== LKT ===
248:'Vater  des  Schweißes',  hieraus  lat.  bor- rago,  eine  Pflanze,  die  durch  die  ar. Medizin  im  Mittelalter  verbreitet  wurde. Die  romanischen  Formen  sind:  it.  bor- race,  borragine,  borrana;  prov.  borrage; sp.  borraja ;  pg.  borragem ;  frz.  hourrache. Auch  germanisch,  z.  B.  engl,  borage, dtsch.  Burrich,  Bor( rjetsch.  Wohl  über das  Ngr.  entstand  rum.  boranjä  'dass.'. Trotz  ML  1412  scheint  diese  Ableitung noch  immer  die  beste  und  wenig  an- fechtbar zu  sein.    [Kluge  64.
430:92.  Ar.  'arak :
431:'Schweiß',  ^arak  at-lamr  'Schweiß  der Datteln',  d.  h.  Datlelsaft,  ein  berauschen- des Getränk.  In  Ostindien  heißt  'arak ein  starkes  Getränk,  das  aus  gegorenem Reis,  Zucker  und  Kokosnüssen  zube- reitet wird.  Nach  Europa  ist  das  Wort gekommen,  nachdem  im  mal.  Archipel Kolonien  errichtet  waren.  Daher  haben Italiener  und  Spanier,  die  dort  keine besaßen,  das  Wort  auf  anderem  Wege erhalten.  Sp.  arac,  altsp.  arrequi(n), frz.  arakj  rack,  pg.  araquc,  araca,  rak, engl,  arrack,  rack,  ndl.  arak,  dtsch. Arrak.  Aus  dem  ar.  Adjektiv  'araki wohl  das  frz.  Argot  woit  riquiqui 'Schnaps'.  Die  tk.  Form  ist  ebenso  raki, woraus  rum.  rachiü  'Branntwein',  rachier 'Branntweinbrenner',  racliierie  'Brenne- rei'. Russ.  arak.  [Kluge  22.  Hobson- Jobson  36/37.  DE  196/197.  Devic  DEt 33/34.  Gorjajew  5.  —  J.  de  Sousa,  Vesli- gios  da  lingua  arabiga  em  Portugal.  Col- lecijäo  etimologica  das  palavras  e  nomes portugueses  que  tem  origen  arabiga.  Lis-
538:[Horn  NpEt  S.  6,  Nr.  19]  'frei'  ergibt mit  pers.  diräht  'Baum'  [Horn  NpEt S.  121,  Nr.  548]  den  Pflanzennamen äzäddirüht,  ebenso  ar.  azädimh  oder azdiraht,  Melia  azederach  L.  [vgl.  J.  F. Gronov,  Flora  orientalis  52;  Forskäl, Flor.  aeg.  ar.  p.  LXVI,  no.  127].  Hieraus sp.  acedaraque,  frz.  asedarac,  dtsth. Zedrach.    [DE  32.    Devic  DEt  53.
661:^Vorspeise  aus  gesalzenen  und  dann  ge- stampften und  getrockneten  Fischchen oder  dergl.'  [Pijn  38  a];  hieraus  anglo- ind. balachong,  blachong,  die  charakte- ristische Speise  der  indochinesischen  und malayischen  Völker.  [Dass.  wie  hier Nr.  286.]    [Hobson-Jobson  51.
719:222.  Ar.  baraka:
760:'Grober  Stoff  oder  Mantel  daraus'  [Wohl aus  Kamelhaar,  vgl.  Dozy  DV  68  sq.); hieraus  mlat.  barracänus,  frz.  harracan 'grober  Stoff',  bouracan,  sp.  kat.  barra- gan,  sp.  pg.  barragana,  it.  baracane; engl,  huckram  [mit  Angleichung  an  buck, das  auch  im  Stotfnamen  bucJtskin  vor- liegt], barchant,  ndl.  barkan,  mhd.  bar- chät,  dtsch.  Barchent,  Berkan;  russ. barham  'Samt',  barakun,  barkan  'Bar- chent'; klr.  barchat  'Samt',  barakan 'Art  Wollstoff';  poln.  barakan,  poln. cech.  barchan  'Barchent'.  [Dozy  Oost  24. DE  237.  ML  941.  Kluge  38.  Gorja- jew  12.  Bern  SlETWb  44.  Lammens Rem  55/56.
771:Ar.  barak.]
773:257.  Ar.  barük: [Vom   Vb.   baraka    'sejrnen':  vulgär:] 'Geschenk';  hieraus  mit  dem  ar.  Art.  sp. alboroc,  alboroque  'Maklergebühr,  Trink- geld' [Dicc  Gast  107  a].    [DE  73/74.
844:[Sskr.  badara,  vadara].  einer  der  am weitesten  verbreiteten  Charakterbäume Indiens,  Ficus  indica  oder  bens^alensis. Im  Gebiete  von  Birma  bis  zum  Pänd- schäh  heimisch,  findet  er  sich  jetzt  von Queensland  und  China  bis  nach  Marokko und  Guinea  angepflanzt.  Angloind. burr  tree,  engl,  gewöhnlich  banian-tree [von  französischen  Reiseschriftstellern oft  falschlich  bananier  genannt]  nach der  Bezeichnung  der  indischen  Ein- geborenen als  Banianen  [aus  hind. banyä  'Kaufmann,  Händler'].  [Hobson- Johson  77.
1153:'Schlägel  (im  Ballspiel)'  [Horn  NpEt S.  100,  Nr.  449,  wahrscheinlich  aus präkrta  chaugäna  'vierfach',  dem  Namen für  den  Polospielplatz].  Das  Polo  ge- nannte Spiel  scheint  mediseh-persischen Ursprungs  zu  sein.  Während  es  jetzt nur  noch  in  einigen  Berglandschaften im  Norden  Indiens  erhalten  ist,  wurde es  früher  an  allen  mohammedanischen Höfen  Asiens  gespielt;  viele  Fürsten haben  es  mit  Leidenschaft  gespielt,  z.  B. Kaiser  Akbar  der  Große,  Saladin  u.  a. Vgl.  K.  Inostranzew,  Zur  Geschichte  des Polospieles.  In  Zapiski  Vostocnago  Ot- djelenija  Imp.  russk.  archeologiceskago Obsßestva.  St.  Petersburg.  Bd.  XIV, 4.  Lieferung.  Nach  Byzanz  gelangt,  hieß das  Spiel  mgr.  TluKdviov,  Vb.  tIukovi- Ceiv,  'Spielplatz  dafür'  x^uKaviaTripiov, und  in  Frankreich,  wo  es  zu  Fuß  ge- spielt wurde,  chicane.  Das  frz.  Wort bedeutete  dann,  daß  man  in  einem Kampfe  jeden  möglichen  Vorteil  wahr- nehmen durfte,  und  kam  so  zu  seiner heutigen  Bedeutung  frz.  chicane  'Kniffe, Schabernack,  Rechtsverdrehung,  Spitz- findigkeit', eigentlich  unübersetzbar,  da es  eine  wesentlich  französische  Charak- tereigenschaft bedeutet.  Dtsch.  Schikane, engl,  chicane,  chicanery.  —  Als  Name für  ein  Spiel  kommt  das  Wort  noch vor:  pg.  choca  [Constancio  Dicc  255b, freilich  mit  falscher  Etymologie]  'ein Kinderspiel  mit  Kugeln',  frz.  (Languedoc) chicane  'LochbaU',  mhd.  schaggün.  — [Ältere  Ableitungen  von  frz.  chicoter 'sich  herumzanken'  entweder  aus  lat. ciccum,  KiKKoq  'Apfelkorb,  nichtsnutziges Ding',  also  'Streit  um  eine  Nichtigkeil' oder  sp.  chico  'klein'  sind  unbegründet]. [DE  254.  Devic  DEt  93/94.  Hobson- Jobson  190/193.
1271:487.  Ar.  daraka:
1509:'Gedreht;  Docht',  ebenso  ik.fitil  'Docht': hieraus  rum.  fitil  'dass.,  Aufreizung' [vgl.  auch  ngr.  9utijX,  Jannarakis, Deutsch  -  Neugriechisches  Handwörter- buch. Hannover  1883.  S.  129a];  bulg. serh.  ßtilj,  russ.  fitil'  'Docht,  Lunte'. [Bern  SlEtWb  282.
1980:'Bauch',  dazu  kiri  'schneiden':  harakiri ist  die  Bezeichnung  für  die  jap.  Art  des Selbstmordes  in  Ehrensachen,  die  darin besteht,  daß  der  Selbstmörder  sich  selbst den  Bauch  aufschlitzt  und  dann  von einem  Diener  den  Kopf  abschlagen  läßt. Im  alten  Japan  gab  es  zwei  Arten:  das obligatorische  und  das  freiwilhge  Hara- kiri. Die  erste  Art,  die  jetzt  erloschen ist,  wurde  von  Verbrechern  der  Samurai [Adel]  Klasse  begangen;  sie  wurde  ihnen von  der  Regierung  als  Gunst  gewährt, damit  sie  so  der  Strafe  entgingen.  Die zweite  Art  wird  noch  in  schweren  Sorgen, vielfach  auch  als  Protest  gegen  Unge- rechtigkeit ausgeübt.  In  den  europäi- schen Sprachen  auch  ofl  in  übertragener Bedeutung:  Aisch.  Harakiri.  —  [Die  viel- fach angegebene  Übersetzung  'the  happy despatch',  'die  glückliche  Erledigung'  ist ganz  grundlos]  [Hobson-Jobson  411. Chamb  AllJap  243/246.
2164:Tries'  [aus  ngr.  Ziuqpöpoi;  Jannarakis Deutsch  -  Neugriechisches  Wörterbuch S.  :251  b  nach  Dozy  oder  wohl  besser aus  gr.  öq)pu?  nach  Völlers  in  ZDMG LI,  295] ;  hieraus  sp.  pg.  friso,  frz.  frise ; engl,  frieze,  ndl.  fries,  dtsch.  Fries  [auch it.  (regio,  freggial  Dieses  Wort  wird von  MENAGE  auf  lat.  fregium,  von PERRAULT  auf  Phryqia  zurückgeführt]. —  DE  270/271.
2558:Auch  karakol,  karawul,  karaul  'Wache' [vom  Stamme  kar  'Auge,  sehen',  z.  B. tk.  kara  'Augapfel',  Vämbery  TktElWb S.  78.  Nr.  831];  hieraus  rum.  caraulä 'Wächter,  Schildwache';  bulg.  karaul, karaimil,  karakol  'Wache',  serb.  kara- ula,  karawula  'Wachtturm,  Schilder- häuschen', klruss.  kalawur  'Wacht- mann',  russ.  karaul  'Wache',  karaulka 'Schilderhäuschen'.  [Gorjajew  134. Bern  SlEtWb  489.
2561:1080.  Tk.  karakol :
2562:'Schwarze  Hand,  d.  h.  schlechte  Hand- schrift' [aus  tk.  ka7-a  'schwarz'  und  kol 'Arm,  Hand'  vom  Stamme  kar,  kor, kol  'Arm,  Hand,  Spanne',  s.  hier  Nr.  1 1 94] ; hieraus  russ.  karakulja  'Gekritzel,  Krä- henfüße', [nach  MSISI  282]  'verkrüppel- ter Baum'.
2563:1081.  Tk.  karakolak: 'Schwarzohr'  ist  der  Name  eines  kleinen Raubtieres  [pers.  ebenso  sijäh  gns 'schwarzes  Ohr'  genannt];  hieraus  dtsch. Karakal,  Felis  caracal  Gmelin  'persi- scher Luchs'.
2564:1082.  Tk.  karakns:
=== DEV ===
1067:(loradille.  Es[).  ceteraque ,  ital.  celracca ,  citracca,  bas  ^rec KiTOLpaK.  t^Mauritanis  et  ofïicinis  ccterach  Arabumw,  dit Cliabré^  C'est  l'arabe  dJxii  clietrak^,  auquel  il  faut  iden- lilier  ^4^^»-^  chltaradj,  vJycxis-  tcliJtarak ,  nom  d'un  médica- ment indien,  dans  Freylag.
1085:dormliUe.  Esj).  ceteraque,  ital.  cclracca,  citracca,  bas  |jrec xnotpotx.  ç^Mauritanis  et  oiïicinis  ccterach  Arabumw,  dit Cliabré^  C'est  l'arabe  JJxii  chetrak^^  auquel  il  faut  iden- lilier  ^-h^  clûtnvadj ,  ^iiyus^^  tcliJtarak ,  nom  d'un  médica- ment indien,  dans  Freylag.
=== PHN ===
1787:ARAK ou ARAKY, s. m. (à.)
5029:*àji [farak] frotter comme le radical du latin ^'care, dont les
9907:[tarak] quitter, abandonner, par exemple , le sol natal , les Turcs
10245:Arak ou Araky, s. m. ( a. ) 4a
10312:Bourrache, s. f. compose, (a.) 74
```


## [2026-09-04T23:07:56.792Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT ctx 235-260 ===\"; sed -n '235,260p' LKT.txt; echo \"=== LKT leaf/page ===\"; python3 -c \"\nt=open('LKT.txt',encoding='utf-8',errors='replace').read(); lines=t.split('\\n')\nfor ln in (240,248,430):\n    off=sum(len(l)+1 for l in lines[:ln-1]); leaf=t[:off].count('\\f'); print(ln,'leaf',leaf,'-> p',leaf-26)\n\""
}
```


### [2026-09-04T23:07:58.860Z] TOOL RESULT

```
=== LKT ctx 235-260 ===
N.  pr.  [  Volksetymologisch  '  Vater  der Menge'].  lu  frz.  Dialekten  in  der  Be- deutung 'Milchstraße',  wallon.  abe d'Abraham  [—  arbre  d'A.]  sind  fächer- förmig vom  Horizont  aus  sich  über  den Abendhimmel  ausbreitende  Wolkenge- bilde.   [Wartbg  FEWb  8.
9.  Ar.  abras:
Auch  tk.  'Pferd  mit  weißen  und  schwar- zen Füßen'.  Hieraus  rum.  abra§  'ge- fleckt, buntscheckig',  tig.  'Unheil  ver- kündend'; im  walachischen  Dialekt iabrai^,  iambra^  'Pferd  mit  weißen Flecken'.
10.  Pers.  äbresäui:
[Horn  NpEt  S.  16,  Nr.  65]  'Seide',  ent- weder gehaspelte  od,  gedrehte,  gezwirnte 1
Ar.  ahn  kirdäii.]
2
Ganzseide  [auch  ins  Semitische  über- gegangen :  syr.  abräsom,  ahr'isüm  BrLex- Syr  ob;  ar.  ibnsam,  ibrisum,  schon häufig  mit  der  Bedeutung  'Seidenfaden, Seidenzwirn',  vgl.  Joseph  Karabacek, Über  einige  Benennungen  mittelallei'- 1  icher  Gewebe  I.  Wien  1882.  S.  21 bis  2'2.].  Ins  Tk.  übergegangen  als  ibri- sim  [offenbar  mit  Anlehnung  an  die Wurzel  ip,  ib  'winden'  Vämbeiy  Tkt- EtWb  Nr.  37].  Aus  dem  Tk.  wurde  rum. ibri^im,  ibri^in  'Seidenfaden,  Zwirn'; Ableitung  ibri^inar.
11.  Ar.  abü  kirdän:
[Wörtlich  „Vater  der  Zecken",  die  ar. kiräd,  plr.  kirdän  heißen].  Der  rein weifae  'Kuhreiher',  Ardea  bubuleus  Sa- vigny,  ein  afrikanischer  Vogel  [die Schreibung  aboogerdan  bei  ML  36  wie schon  vorher  bei  Körting,  Lateinisch- romanisches Wörterbuch.  3.  Aufl.  Pader- born 1907,  s.  V.  ist  englisch].  Durch volksetymologische  Neugestaltung  hier- aus vielleicht  frz.  bwuf-garde,  garde- bcfuf  'eine  Art  Silberreiher'.  [FASS in  RomForsch  III,  488.  KURYLOWICZ in  Rocznik  Orientalistyczny.  Tom  II. Lwöw  1925.    S.  252.
12.  Ar.  'abar:
In  der  Zusammensetzung  as-sirä  al- "abiir  'der  [sc.  auf  der  Milchstraße] wandernde  Sirius'  [hierzu  s.  hier  Nr.  1915] vom  ar.  Stamme  'fcr  'wandern'  [vgl. hebr.  "ibrl  'Hebräer',  d.  h.  derjenige,  der gewandert  ist  od.  überschritten  hat  sc. den  Euphrat  od.  Jordan].  Hieraus  Alha- bor,  Alchabar  als  Name  des  Sirius  a Ganis  majoris.  [Devic  DEt  40/41. Ideler  Sternn  237  und  246.
13.  Ar.  abü  rag':
'Vater  des  Schweißes',  hieraus  lat.  bor- rago,  eine  Pflanze,  die  durch  die  ar. Medizin  im  Mittelalter  verbreitet  wurde. Die  romanischen  Formen  sind:  it.  bor- race,  borragine,  borrana;  prov.  borrage; sp.  borraja ;  pg.  borragem ;  frz.  hourrache. Auch  germanisch,  z.  B.  engl,  borage, dtsch.  Burrich,  Bor( rjetsch.  Wohl  über das  Ngr.  entstand  rum.  boranjä  'dass.'. Trotz  ML  1412  scheint  diese  Ableitung noch  immer  die  beste  und  wenig  an- fechtbar zu  sein.    [Kluge  64.
14.  Ar.  abü  tilün:
[Vgl.  Ihn  Sinä,  Kitäb  al-känün  fi't-tibb. Romae.  In  typographia  Medicea  1593. S.  137]  'eine  Zierpflanze'  aus  der  Familie der  Malvaceen:  Abutilon  indicum.  Hier- aus frz.  abutilon  'dass.',  nämlich  abutilon striS  Abutilon  striatum  Diks.  (Sida  striata Hort.)  und  abutilon  itendard  A.  vexilla- rium  Ed.  Morrea  (S.  vexillaria  Hort.). [Devic  DEt  3.    Lammens  Rem  3.
15.  Pers.  acär:
'Sauer',  hieraus  malay.  a£ar  [Pijn  237] in  der  Bedeutung  'Eingemachtes,  pickles' und  ebenso  in  allen  Eingeborenen- sprachen Indiens;  daher  angloind.  achar 'dass.';  frz.  achars  'Obst  od.  Gemüse, das  in  Essig  eingemacht  ist',  ein  im indischen  Archipel,  auf  Mauritius  usw. sehr  beliebtes  Gericht.  [Devic  DEt  3/4. Hobson-Jobson  3.
16.  Ar.  'äda:
'Sitte,  Gebrauch',  ebenso  Ik.  adet  'dass.'; hieraus  rum.  adet  'Brauch,  Sitte,  Regel', früher  'Steuer'.    [Sain  46.
17.  Malayälam  adakka:
[Aus  arfa/ 'enge  Anordnung  einer  Traube' und  kay  'Nuß'].  Hieraus  pg.  areca, angloind.  Areca,  worunter  man  allge- mein den  Samen  od.  die  Nuß  der  Palme, Areca  catechu  L.,  versteht.  [Hobson- Jobson  35.
18.  Ar.  'adäla:
[Aus  ar.  'adl  'Gerechtigkeit']  'Gerichts- barkeit', in  vulgärer  Aussprache  'adälet, woraus  über  das  Hind.  das  angloind. adawlut  'Gerichtshof  wurde.  —  Aus- führlich in  Hobson-Jobson  4/6.
19.  Hebr.  Ädäm:
'Mensch',  dann  N.  pr.  für  den  Stamm- vater des  Menschengeschlechtes  [vgl. assyr.  admu  'Kind,  bes.  junges  Kind' Del  HWB  25  b],  daraus  bei  den  Ana- tomen des  Mittelalters  hebr.  iappü"h ha-ädäm,  wörtlich  'Apfel  des  Mannes', zur  Bezeichnung  des  Vorsprungs  am Kehlkopf  des  Mannes  [gr.  irpöXoßo;]. Da  er  nur  am  Halse  des  Mannes  zu sehen  ist,  ist  der  Name  treffend  ge- wählt, dann  aber  durch  mißverständ- liche Übersetzung  zu  Pomum  Adami 'Adamsapfel'  geworden  und  die  bekannte Fabel  entstanden,  daß  Adam  den  ihm hingereichten  Apfel  nicht  ganz  habe verschlucken  können.  Ii. morso d'Adamo, frz.  morceau  d' Adam,  pomme  d'Adatn. Engl.  Ada7n's  apple,  schwed.  adanis aepple,  dän.  adams  üble,  ndl.  adanis  appel. Poln.  jabiko  Adamowe,  ßech.  Adamavo jahlko.  Im  Angloind.  ist  Adanis  apple die  Frucht  von  Mimusops  Elengi  L., im  It.  joomo  d'Adamo  [od.  pomo  di  para- diso]  eine  Orangenart,  Citrus  decumana. [Kluge  6.  Hobson-Jobson  4.  HArllebr- An  164.
=== LKT leaf/page ===
240 leaf 28 -> p 2
248 leaf 28 -> p 2
430 leaf 35 -> p 9
```


## [2026-09-04T23:08:08.692Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read(); lines=t.split('\\n')\nfor ln in (5360,):\n    off=sum(len(l)+1 for l in lines[:ln-1]); leaf=t[:off].count('\\f'); print(ln,'leaf',leaf,'-> approx p',(leaf-12)*2)\n\"; echo \"=== KLN argent/argue/argentum ===\"; grep -n -E '^argent,|^argue,|^Argentina|^arrack,' KLN_1966.txt | head; echo \"=== PHN p74 (leaf105) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==106' PHN.txt | head -50"
}
```


### [2026-09-04T23:08:11.063Z] TOOL RESULT

```
5360 leaf 109 -> approx p 194
=== KLN argent/argue/argentum ===
3408:argue,  intr.  and  tr.  v.  —  ME.  arguen,  fr.  OF.
=== PHN p74 (leaf105) ===
76 BOU
BOURAGAN,s. m. (a.)
UV' [^rra^ati] Espèce de vêtement Doir, très-grossiér. Le
kouracan est une sorte de camelot d*un grain plus gros que le
camelot ordinaire. — G*est de l'arabe que les Espagnols et les
Portugais ont tiré harragana, subst. fém., et les Italiens bara-
coHo, mot écrit avec une seule r et employé au masculin comme
son correspondant français.
BOURNOUS,s. m. (a.)
if^ji [houmous] Ce mot , qui désignait , dans lorigine , le bmmet
pamiH porté par les religieux musulmans au commencement
de Tislamisme^ et spécialement le capuchon attaché à un vête-
ments se dit aujourdliui du wumteam de lowe, sans manches et à
cnfndion. que les Arabes ^ et surtout ceux de TAfrique septen-
trionale « ont coutume de mettre par-dessus leurs autres vête-
ments. Les boumous d*été sont de couleur blancbe , et ceux
d^biver de couleur foncée et en laine beaucoup plus épaisse. —
Depuis i830s fusage des boumous sW introduit en France,
avec plusieurs modifications, pour servir à la toilette d'hiver
des deux sexes, — Les Espagnole et les Portugais écrivent «/-
htmo:. mot qui représente a^si^x exactement le correspondant
ambe, préc^nlê toutefois de Fartide aL
ROIRRACHE. s. t composa, {k.)
>? [ M>iî ] (HUir^) j .î«Vw ] phr. ^jH [ rmirU' ] dir U smeur. Plante
ori|^iviiir^ du l^nant^ et dont rôl^mologie arabe suffit pour
imliquer la \ertu sudorilique; «mi Temploie principalement
d,^ns lt>s tivauo< jMvtomK^^. — r^^iu|virpi aussi Pespagnol
\
```


## [2026-09-04T23:08:21.442Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN leaf 109 page numerals ===\"; awk 'BEGIN{RS=\"\\f\"} NR==110' KLN_1966.txt | grep -n -oE '^[0-9]{2,4}|[0-9]{3}$' | head; awk 'BEGIN{RS=\"\\f\"} NR==110' KLN_1966.txt | head -3; echo \"=== KLN argue ===\"; sed -n '3405,3412p' KLN_1966.txt; echo \"=== KLN argent ===\"; grep -n -oE '.{0,80}argentum.{0,300}' KLN_1966.txt | head -6"
}
```


### [2026-09-04T23:08:26.948Z] TOOL RESULT

```
=== KLN leaf 109 page numerals ===
12:186
13:187
  ME.  bond,  a var.  of  band.  See  band,  ‘a  tie’,  and  cp.  the  first element  in  bonspiel.
Derivatives:  bond,  tr.  v.,  bond-ed,  adj.
bond,  n.,  serf  (archaic).  —  ME.  bond,  ‘husband, householder’,  fr.  OE.  bonda,  ‘householder’,  fr. ON.  bondi,  for  biiandi,  ‘householder’,  lit.  ‘dwel¬ ler’,  fr.  bua,  ‘to  dwell,  build’.  See  be,  build,  and cp.  Boer,  boor,  booth,  bound,  adj.,  bower,  ‘ar¬ bor’,  byre,  and  the  second  element  in  husband.
=== KLN argue ===
Argonaut,  n.  pi.,  one  of  the  heroes  led  by  Jason in  the  ship  Argo  to  fetch  the  golden  fleece  in Colchis.  —  L.  Argonauta,  fr.  Gk.  ’  Apyovau-pp, ‘sailor  of  the  Argo’,  which  is  compounded  of ’  Apyco  (see  Argo)  and  vcGrr,:,  ‘sailor,  seaman’. See  nautical.
argonaut,  n.,  the  paper  nautilus  (zoo!)  —  Fr. prec.  word.
argosy,  n.,  a  large  ship;  a  fleet  of  large  ships.  — Earlier  ragusye,  arguze,  lit.  ‘ship  from  Ragusa’ fr.  It.  Ragusea,  ‘ship  of  Ragusa'. argot,  n.,  slang,  esp.  the  slang  of  Paris.  —  F.,  of uncertain  origin.
argue,  intr.  and  tr.  v.  —  ME.  arguen,  fr.  OF.
argument
arm
( =  F.)  arguer ,  fr.  L.  argutare,  freq.  of  arguere, ‘to  make  clear,  prove’,  which  is  rel.  to  argentum, ‘silver’  ( arguere  orig.  meant  ‘to  make  as  white as  silver’).  See  argent.
Derivatives:  argu-able,  adj.,  argu-er,  n. argument,  n.  —  F.,  fr.  L.  argumentum,  fr.  arguere , ‘to  argue’.  See  prec.  word  and  -ment. argumental,  adj.  —  L.  argumentalis,  fr.  argumen¬ tum.  See  prec.  word  and  adj.  suff.  -al. argumentation,  n.  —  F.,  fr.  L.  argumentationem, acc.  of  argumentatio,  ‘an  adducing  of  proof’,  pp. of  argumentari ,  ‘to  argue’,  fr.  argumentum.  See argument  and  -ation.
=== KLN argent ===
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,300}
                         \___exceeds complexity limits
```


## [2026-09-04T23:08:38.533Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'argent,' KLN_1966.txt | head -3; echo \"---\"; sed -n '3380,3400p' KLN_1966.txt | grep -n -i 'argent' ; echo \"=== search argent entry ===\"; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('argent,')\nprint(t[i-200:i+1400])\nprint('LEAF', t[:i].count('\\f'))\nEOF"
}
```


### [2026-09-04T23:08:41.167Z] TOOL RESULT

```
3395:argand  lamp.  —  Named  after  its  inventor  Aim6 Argand,  a  Swiss  physicist  (1755-1803). Argemone,  n.,  a  genus  of  plants  of  the  poppy family  (bot.)  —  Gk.  apyEpuivT),  ‘a  kind  of  pop¬ py’,  prob.  fr.  Heb.  argamdn,  ‘purple’.  Cp.  Ak¬ kad.  argamannu,  of  s.m.  Cp.  also  agrimony.  For the  ending  -cow)  in  apye|ic I>vr),  cp.  dcvspuiw),  ‘the wind  flower’  (see  anemone). argent,  n.,  silver  (archaic).  —  F.,  fr.  L.  argentum, ‘silver’,  which  is  cogn.  with  Gk.  Spyupo?,  ‘silver’, prop,  ‘the  white  (metal)’,  fr.  dpyo?  (dissimul¬ ated  fr.  *ipypo?),  ‘shining,  bright,  white’;  fr. I.-E.  base  *arg-,  ‘to  shine’,  whence  also  OI. rirdh,  ‘shining,  glowing,  bright’,  rajatam ,  Aves¬ tic  ‘r*zata,  ‘silver’,  OI.  drjunah,  ‘shining,  white’, Toch.  A  drki,  ‘white’  (said  of  teeth),  arkyant, ‘silver’,  B  arkwi,  of  s.m.,  arkwirme,  ‘light  color’, Hitt,  harkish.  ‘bright,  clear’,  Thracian  4pytX<x;,
21921:-lith,  combining  form  meaning  ‘stone’,  used  esp. in  archaelogy,  biology  and  medicine  (as  in  eolith, chololith);  in  geology,  mineralogy,  and.  paleontol¬ ogy,  -lite  is  the  regular  combining  form.  —  F. -lithe,  fr.  Gk.  Xi&o;,  ‘stone’.  See  litho-  and  cp.  -lite. litharge,  n.,  lead  monoxide.  —  ME.  litarge,  fr. OF.  litarge  (F.  litharge),  fr.  L.  lithargyrus,  fr. Gk.  Xiffdpyupoc,  ‘vitrified  lead,  lead  monoxide’, lit.  ‘stone  silver’,  fr.  Xtffo^,  ‘stone’,  and  itpyupop, ‘silver’.  See  litho-  and  argent, lithe,  adj.,  flexible,  supple.  —  ME.  lithe,  lith,  fr. OE.  tide,  ‘soft,  mild,  gentle’,  rel.  to  OS.  lit  hi, OHG.  lindi,  MHG.  Unde,  G.  lind,  ON.  linr,  fr. I.-E.  base  *lent-,  ‘flexible’,  whence  also  L.  len- tus,  ‘flexible,  pliant;  slow’,  and  prob.  also  ON., OE.  lind,  ‘linden  tree’,  lit.  ‘the  tree  with  pliant bast’.  See  lentitude,  and  cp.  linden.
22922:margent,  n.,  margin.  —  An  archaic  var.  of  mar¬ gin.
---
16:argand  lamp.  —  Named  after  its  inventor  Aim6 Argand,  a  Swiss  physicist  (1755-1803). Argemone,  n.,  a  genus  of  plants  of  the  poppy family  (bot.)  —  Gk.  apyEpuivT),  ‘a  kind  of  pop¬ py’,  prob.  fr.  Heb.  argamdn,  ‘purple’.  Cp.  Ak¬ kad.  argamannu,  of  s.m.  Cp.  also  agrimony.  For the  ending  -cow)  in  apye|ic I>vr),  cp.  dcvspuiw),  ‘the wind  flower’  (see  anemone). argent,  n.,  silver  (archaic).  —  F.,  fr.  L.  argentum, ‘silver’,  which  is  cogn.  with  Gk.  Spyupo?,  ‘silver’, prop,  ‘the  white  (metal)’,  fr.  dpyo?  (dissimul¬ ated  fr.  *ipypo?),  ‘shining,  bright,  white’;  fr. I.-E.  base  *arg-,  ‘to  shine’,  whence  also  OI. rirdh,  ‘shining,  glowing,  bright’,  rajatam ,  Aves¬ tic  ‘r*zata,  ‘silver’,  OI.  drjunah,  ‘shining,  white’, Toch.  A  drki,  ‘white’  (said  of  teeth),  arkyant, ‘silver’,  B  arkwi,  of  s.m.,  arkwirme,  ‘light  color’, Hitt,  harkish.  ‘bright,  clear’,  Thracian  4pytX<x;,
18:argentiferous,  adj.,  containing  silver.  —  Com¬ pounded  of  L.  argentum,  ‘silver’,  and  the  stem of  L.  ferre,  ‘to  bear,  carry’.  See  argent  and -ferous.
19:argentine,  adj.,  resembling  silver.  —  L.  argen¬ tine,  ‘of  silver’,  fr.  argentum,  ‘silver’.  See  argent and  -ine  (representing  L.  -inus). argentite,  n.,  silver  sulfid,  Ag2S  (mineral.)  — Formed  with  subst.  suff.  -ite  fr.  L.  argentum, ‘silver’.  See  argent.
20:argil,  n.,  potter's  clay.  —  F.  argile,  ‘clay’,  fr.  L. argilla,  ‘white  clay,  potter’s  earth’,  fr.  Gk. dpytkkoi;,  of  s.m.,  which  is  rel.  to  apyop,  ‘shin¬ ing,  bright’.  See  argent.
=== search argent entry ===
y’,  prob.  fr.  Heb.  argamdn,  ‘purple’.  Cp.  Ak¬ kad.  argamannu,  of  s.m.  Cp.  also  agrimony.  For the  ending  -cow)  in  apye|ic I>vr),  cp.  dcvspuiw),  ‘the wind  flower’  (see  anemone). argent,  n.,  silver  (archaic).  —  F.,  fr.  L.  argentum, ‘silver’,  which  is  cogn.  with  Gk.  Spyupo?,  ‘silver’, prop,  ‘the  white  (metal)’,  fr.  dpyo?  (dissimul¬ ated  fr.  *ipypo?),  ‘shining,  bright,  white’;  fr. I.-E.  base  *arg-,  ‘to  shine’,  whence  also  OI. rirdh,  ‘shining,  glowing,  bright’,  rajatam ,  Aves¬ tic  ‘r*zata,  ‘silver’,  OI.  drjunah,  ‘shining,  white’, Toch.  A  drki,  ‘white’  (said  of  teeth),  arkyant, ‘silver’,  B  arkwi,  of  s.m.,  arkwirme,  ‘light  color’, Hitt,  harkish.  ‘bright,  clear’,  Thracian  4pytX<x;,
‘mouse’  (lit.  ‘the  white  colored  animal’).  Arm. arcat',  ‘silver’,  Olr.  argat,  W.  arian(t),  Co., MBret.  argant,  Bret,  arc'hant,  ‘silver’,  L.  ar- guere,  ‘to  make  clear,  prove’.  Cp.  argil,  Argo, argue,  Argus,  argyria,  argyrodite,  arjun,  and  the second  element  in  litharge.  Pelargonium,  Po- darge,  pygarg.
argentiferous,  adj.,  containing  silver.  —  Com¬ pounded  of  L.  argentum,  ‘silver’,  and  the  stem of  L.  ferre,  ‘to  bear,  carry’.  See  argent  and -ferous.
argentine,  adj.,  resembling  silver.  —  L.  argen¬ tine,  ‘of  silver’,  fr.  argentum,  ‘silver’.  See  argent and  -ine  (representing  L.  -inus). argentite,  n.,  silver  sulfid,  Ag2S  (mineral.)  — Formed  with  subst.  suff.  -ite  fr.  L.  argentum, ‘silver’.  See  argent.
argil,  n.,  potter's  clay.  —  F.  
LEAF 66
```


## [2026-09-04T23:08:50.875Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==67' KLN_1966.txt | grep -oE '^1[0-9]{2}$|^[0-9]{2,4}' | head; echo \"=== AHD arg- ===\"; grep -n -A6 -E '^arg-' AHD_watkins1985.txt | head -40; echo \"=== IEC ===\"; grep -n -E '^arg-|^arĝ|^argnt|^arĝ-' IEC.txt | head; echo \"=== SYN silver ===\"; grep -n -E '^9\\.6[0-9] SILVER|SILVER' SYN.txt | head"
}
```


### [2026-09-04T23:08:53.510Z] TOOL RESULT

```
104
105
=== AHD arg- ===
290:arg-. To shine; white; the shining or white metal, silver. 1. Suffixed form *arg-ent- in Latin argentum, silver: ARGENT, ARGENTINE. 2. Suffixed form “arg-i-U/l)- in Greek argillos, white clay: ARGIL. 3. Suffixed form *arg- u-ro- in Greek arguros, silver: LITHARGE, PYRARGYRITE. 4. Suffixed form *arg-i-n- in Greek arginoeis, brilliant, bright-shining: ARGININE. 5. Extended form “argu-, brilliance, clarity, in Latin denominative arguere, to make clear, demonstrate: ARGUE. 6. Suffixed form *arg- ro- in Greek argos (< *argros), white (see pel-2). [Pok. ar(e)g- 64.]
291-[arkhein. To begin, rule, command. Greek verb of un- known origin; with derivatives arkhé, rule, beginning, and arkhos, ruler. (ARCH-), -ARCH, ARCHAEO-, ARCHAIC, ARCHI-, ARCHIVES, ARCHON, (-ARCHY); AUTARCHY, EXARCH, MENARCHE.]
292-arku-. Bow and arrow (uncertain which, perhaps both as a unit). 1. Germanic *arhwo in Old English ar(e)we, earh, and Old Norse *arw-, arrow: ARROW. 2. Latin arcus, bow: ARC, ARCADE, ARCH!, ARCHER; ARBALEST, ARCHI- VOLT, (ARCIFORM), ARCUATE. [Pok. arqu- 67.]
293-aryo-. Lord, ruler; self-designation of the Indo-Iranians and perhaps of the Indo-Europeans. Lengthened-grade form *dryo- in Sanskrit drya-, noble, Aryan: ARYAN. [Pok. arjo- 67.]
294-as-. To burn, glow. 1. Extended form *asg- in Germanic
295-asinus
296-*askon- in Old English zsce, asce, ash: ASH!. 2. Suffixed form *ds-d- in Latin Gra, altar, hearth: Ara. 3. Suffixed (stative) form *ds-é- in: a. Latin Grére, to be dry, hence dridus, dry, parched: ARID; b. Latin ardére, to burn, be on fire, from dridus, parched: ARDENT, ARDOR, ARSON. 4. Extended form *asd- in: a. Greek azein, to dry: ZAMIA; b. Greek azaleos, dry: AZALEA. [Pok. as- 68.]
=== IEC ===
689:arg- (?) “cut, destroy Hitt. cf. arghi, ark- ‘cut; arkamas ‘tribute’; Ir. argaim, airgim, argnaim ‘plunder’; argain, s. ‘plunder’. Cf. porg-
692:arĝos, ios (arguios, “ar2-) ‘silvery, white, clear’. WP I, 82. Cf. ar&ntom. (Lat. arguo and Gk. argós equated by Ainsworth in 1736) Skt. árjunah, beside rjrah ‘reddish’; Av. arə- zð ‘daylight’, aroz- "be white’; OPer. arad-; Tokh. arki, obl. arkyant; Tokh. B àrkwi, adj. *white'; Hitt. harkis, id.; Gk. argós, id. beside árguros “silver” and arges, -étos; Lat. cf. arguo, argutus
=== SYN silver ===
13526:SILVER
15402:9.65 SILVER Grk. — &pyupos Goth.  silubr Lith. sidabras NG done ON silfr Lett. sidrabs Lat. argentum Dan. sfif ChSl.  s(it)rebro It. argento Sw. silver SCr.  srebro Fr. argent OE siolfor, seolfor Boh. _ sifebro Sp. plata ME - sylver Pol. __srebro Rum. argint NE silver Russ. serebro Tr. argat, airged Du. —_zilver Skt. —_ rajata- Nir. airgead OHG - sil(a)bar Av. grazata-, OPers. W. arian MHG ssilber ardata- Br. arc’hant NHG silber
```


## [2026-09-04T23:09:05.960Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC arĝntom ===\"; grep -n -E \"^ar[ĝg]ntom|arĝntom\" IEC.txt | head; sed -n '690,700p' IEC.txt; echo \"=== SYN 9.65 text ===\"; sed -n '15402,15420p' SYN.txt; echo \"=== BRT erezata ===\"; grep -n -E \"razata|rəzata|erezata|arezata\" BRT.txt | head -10"
}
```


### [2026-09-04T23:09:06.049Z] TOOL RESULT

```
=== IEC arĝntom ===
arghos, à “point, tip” Arm. cf. arg- (px. *first-); Gk. arkhé; arkhós; OCS cf. razínü ‘goad, awl, *roasting-spit'; OCz. rožen ‘spit’. Uncertainly also Mir. arg ‘outstanding’, s. ‘champion’; Gaul. argo-
ar2ntom “white metal, silver’. WP I, 82. Cf. arĝos Skt. rajatám; cf. also rajatah ‘silvery’; Av. ərəzatəm; Ober, aradata-; Oss. ärzät ‘metal, ore’; cf. Per. arzin ‘tin’; Arm. arcať, Iranian LW ‘silver’; cf. Arm. arcni ‘enamel’ beside arcnem (v. ‘polish’: Skt. rajin “shining'); Lat. argentum; Osc. aragetu-; Olr. argat, airget, Ir. airgead; Gaul. arganto-; OBrit. arga(nt); OW ariant, ereint; W arian; Cor. arghans; Br. argant. The phonology and source of Pol. ortec ‘amalgam’; Slovak ortuť, R and Cz. rtuť ‘mercury’ are obscure.
arĝos, ios (arguios, “ar2-) ‘silvery, white, clear’. WP I, 82. Cf. ar&ntom. (Lat. arguo and Gk. argós equated by Ainsworth in 1736) Skt. árjunah, beside rjrah ‘reddish’; Av. arə- zð ‘daylight’, aroz- "be white’; OPer. arad-; Tokh. arki, obl. arkyant; Tokh. B àrkwi, adj. *white'; Hitt. harkis, id.; Gk. argós, id. beside árguros “silver” and arges, -étos; Lat. cf. arguo, argutus
arimn-, see armn-
ario (1) and (2), see aro (1) and (2)
aro, ið, see Orð, ið, and cf. ar- (2)
15
20
25
30
35
=== SYN 9.65 text ===
9.65 SILVER Grk. — &pyupos Goth.  silubr Lith. sidabras NG done ON silfr Lett. sidrabs Lat. argentum Dan. sfif ChSl.  s(it)rebro It. argento Sw. silver SCr.  srebro Fr. argent OE siolfor, seolfor Boh. _ sifebro Sp. plata ME - sylver Pol. __srebro Rum. argint NE silver Russ. serebro Tr. argat, airged Du. —_zilver Skt. —_ rajata- Nir. airgead OHG - sil(a)bar Av. grazata-, OPers. W. arian MHG ssilber ardata- Br. arc’hant NHG silber
1. Derivs. of IE *arg- in words for ‘bright, white’ like Grk. dpyés, Skt. arjuna-, ete. Some variation in form of root and of suffix. Walde-P. 1,82f. Ernout-M. 71. Walde-H. 1.66, 848,
Grk. apyupos; Lat. argentum (> It.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
argento, Fr. argent, Rum. argint), Ose. abl. sg. aragetud; Gall. arganto- in Ar- ganto-marus, etc., Ir. argat, airged, NI. airgead, W. arian, Br. arc’hant; Skt. rajata-, Av. arazata-, OPers. ardata- (Dar. Sus. f. 40), all neuter; Arm. arcat’.
a en —
Pe ee <2, ee 2 ee T
— «1
NS 1 ee) Se _
MISCELL
m some common t in Asia Minor.
ee 3 siolfor, OHG sil(a)- Ha C.; OPruss. sirablan, : Lett. sidrabs; ChSl. sure- general Slavic.
bro, of Grk. &onuov fr.
3, NG dtu, dim.
copr, efydd, pres kouevr, arem
Grk, xadxés and Lat. aes covered both ‘copper’ and its alloy with tin, ‘bronze’. Their actual reference in the majority of cases would be to bronze, since this was somuch more extensively employed than pure copper. So Goth. azz (which ren- ders xadxés as the ‘copper’, really bronze coin, also in aiza-smipa for xadxebs ‘cop- persmith’), ON eir, OF ar, OHG @r, all cognate with Lat. aes and orig. words for epee were applied mainly to what a bronze. A new, specific name if Ca : nia spread over nearly all nished b 7 he Europe, was fur- eae a a a Lat. derivative of the The old “aii eae one ‘bronze’, but for thi ee somestt ton which spread a another new word, furnished aah oy all Europe, was Which is disputed ronzo, the source of
Tass, the allo ‘own in clase
es, NE b Pres) origin
with zinc, was un- antiquity. Of its "ass (whence Ir. pras, W. Y applied to bronze and
=== BRT erezata ===
```


## [2026-09-04T23:09:16.878Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"z[aä]ta.{0,40}Silber|Silber.{0,60}z[aä]ta\" BRT.txt | head -10; echo \"---alt---\"; grep -n -o -E \".{0,120}Silber.{0,120}\" BRT.txt | head -20"
}
```


### [2026-09-04T23:09:20.844Z] TOOL RESULT

```
---alt---
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,120}
                        \___exceeds complexity limits
```


## [2026-09-04T23:09:23.285Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; LC_ALL=C grep -n \"Silber\" BRT.txt | head -20"
}
```


### [2026-09-04T23:09:23.331Z] TOOL RESULT

```
7298:•  j.  ä-bar«tar-  m.  'Zuträger'  sva.  'Diener, Schaffner':  ai^qm  ?n%aüm  zarattim  *ni- bjrf^a  °ta  baraiti  "ihnen  bringtSilberund Gold  der  Schaffner  in  die  Kammer"  YL
7686:•  j.  «razatö.fraäna-  Adj.  'des  Fr.  von Silber  ist'  (oder  'sind'):  mi'ir^m  °iifm zaranyS.värj^mamm  (sd,)  YLJO.112.
7688:•  j.  «r^zatö.saepa-  Adj,  'wo(rin,  -mit) Silber  geschweisst  wird':  pisrat  hata  'pät V,<.V,88.
11254:satim  saranitH  "die  Felle  strahlen  auf  die Beschauer  Silber  und  Gold(glanz)  in  Fülle" Yt.  5.  129;  —  •mqnca  *hiku  N.55.
16149:liehe'*  Mündigkeit  erreicht  hat,  voll-,  gross-  ■  KompE.  —  Pü. :  fahUk  maiät. jährig':  °yus  .  .  *°yu'>  (ND,)  ,  .  *'yunam ''  j  •  j,  p^nskä-  f.  'Preis,  Werf  ":  hat yazat F.  2e;  — *°yu^'^  F.io;  —  ap^rpnJyu  ahmi  \  irfzaitmi  .  .  yaia  aspahe  arsnö  'ta  "wie «^'^  'y*  (als  NSm.)  ^*  ytzi  baväni  (sd.)  "yu  I  viel  Silber?  .  ,  Soviel  als  der  Wert  eines "minderjährig  bin   ich,   noch   nicht   voll-' Rosshengstes  (ist)"  V. i4. 11;  11.
29922:für  den  werktätigen  (Bauern),  ein  Teil  Silber,
```


## [2026-09-04T23:09:30.101Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7670,7700p' BRT.txt; echo \"=== leaf/col ===\"; python3 -c \"\nt=open('BRT.txt',encoding='utf-8',errors='replace').read(); lines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:7685]); leaf=t[:off].count('\\f'); print('leaf',leaf)\nimport re\nprint(re.findall(r'\\n\\s*(\\d{3,4})\\s*\\n', t[off-6000:off+3000]))\n\""
}
```


### [2026-09-04T23:09:32.300Z] TOOL RESULT

```
scheinlich;    i   falschlich    statt  ya   (wie  nach       KompA.;  Ableit.  —  Vßl.  ai.  rajaiä-  n.;  ann. Konsonanten,  S  ^^.J.  31);  s.  Bthl.  IF. //.  133. ;      arcaf.  —  Pü.:  asim.
.  j.  «rjdvöiohan-  Adj.  'des  Mund,  Ge- 1  •)•  »"?«•««■>•-  Adj.  (fem  •«-)  Von Sicht  nach  oben  gerichtet  ist':  ^oi  hl  miv  S'"'"'  *"»':  -«^  hara  l.sKiJ .  lO.  17;  - •»^».  (ASm.  sutt  ASn.)  ^„,ian^  »/»;  i  "■'  *'  'f"?  (»f"'-  '«/'""tf)  •»'  ^t/o. >,■«  «aV  /r^i  AI"*.»!'«  MI  zatt^gbya  "|;  — /°"  "7  '  ""•"■«»>«  (^^  ■  ■  •'" mannt  "so  (gross)  dass  er  (der  Xalai  i  *  Ableit!^  au/^I-«/^-  -  Pü  ■  aifm« nicht  an  seinen   (näml.   des  Toten)   mit ,    .  ^  _    .0  ,,'.,.  ,  .,,  ',     „  ,  j
dem  Gesicht  nach  oben  gerichteten  Kopf  l'^^'-^^^^o-P'^-'^dj-'^jlberg^^^^ anstosse,  nicht  vom  an  die  Füsse,  nicht  IJ"^"    ^f    V»?'^' «    (APn.) «    .y«ä«     rvi seitwärts  an  die  Hände"  V.j.ii.  !  !''.~'y^->'^' V"^,"-^''.  '^f^-'^f'««^'-
Pü.:  Vgl.  lEt.  und  Bed,  JN.  JAOS.  74.
''iTi.  erl.;
•  j.  «rsSwö.drafSa-  Adj.  (fem.  'sä-)  'mit hoch  aufgerichtetem  Banner':  Aa»tayäsca,. °/ajni  Yt.  /,  1 1 ;  —  bäxölm  srJram  "sam V.J.6.
Pü.:  ^rnük  drafi,  fr.i'räsl  drnß.
•  j.  »r«8wö.biä-  Adj.  (auch  fem.)  'der energische,  kräftige  Heilmittel  hat':  avam vanqm  .  .  yä  hubts  'bis  (NSf.)"  y<J  väoce vispS.Ul  (sd.)  ttqma  Yt.j2.r7.
')  Bd.  18.  9  übersetiti  luiciäk  iiiüi.
•  j.aradwö.zvnga-,  *«radvö.zflnga-'*  Adj. (fem.  'gä-)  'mit  aufgerichtetem  Knöchel' sva.  '(immer)  auf  den  Füssen,  Beinen'": mi'ir»m  ..  'g^m  2amaahunt9m  Yt/o.6i; —  nairyam  kqm.varjÜJm  'gqm  a:^afnyqm Y.  62.  5 ; '  —  any3  *'g3  V.  5.9  PüZ.
PH.:  stiliik  zan^ih,  Sfl.:  slidf^hajai;^halä,  erl.t /'/Yrf  kärye  yat  ptxdäfihyiitH  yujyale  karttim  vya- vasäyi  iaitaica  hkofäaiL'  —  ■)  So  V,  5;  llds.
örAib".  —  I)  Falsch  Gdn.  KZ.  3$.  Sa2.
,    j.  iridm/siiyä  Vyt.  5Ö:  lies  ir^ifuafsiiyA.
•  g.  «raihva-  Adj,  'wert,  würdig':  kvs  na firasrüidyäi  (sd.)    *-'>wB^'^  \.46.
,  i  "sUbergeschmÜckte  (Geräte?)  oder  gold- geschmtickte  oder  mit  irgend  einer  der Farben  (geschmückte)"  Aog. //.
Sü.:  raupyanirmilakS.  —  ')  Ausg.  >riz/irö paiti  zaranyS  faili;  s.  aber  Var.  zSchr.  mit ai  ti.%!6S.^.  Das*  TviAi  lu  lesen,  ergeben die  Überset lungen  1  s.  No.  3.  —  ')  Nach  Sü, 'nirmiliiii;  %  22g.  2  a.  —  3)  Vgl.  Sfl.  liiinir- milam  Y.  5/.  21   für  stihrpatiatthim.
•  j.  «razatö.fraäna-  Adj.  'des  Fr.  von Silber  ist'  (oder  'sind'):  mi'ir^m  °iifm zaranyS.värj^mamm  (sd,)  YLJO.112.
•>a/»a-  m.  Name  einer  Waffe,  wohl  einer Schui2walTe;  Windischmann  (u.  A.):  'Helm', DST.i  'eenouilldres'.
•  j.  «r^zatö.saepa-  Adj,  'wo(rin,  -mit) Silber  geschweisst  wird':  pisrat  hata  'pät V,<.V,88.
Pü.:  asTm  palkar.
•  j.  «razay-  m.  'Hodensack':  'zöiS  xa "die  Quellen  des  Hodensacks"  Yt.  i4~ 39.         a)  Du.  'Hoden':  'zi  (ND.)  F.jg.
gr.  lpx''>  »nn-  am-oijW.  aib.  bfilt;  vgl.  ai. ai-lr^Jiia-  Adj.').  —  Pü.:  A"""^l  mi'  "l^r  "P- Glosse  xjyasi».  —  *)  S.  datu  Gdm.  ZDMÖ. 52-  746-
•  g.  '«razav-  (,  p.  aräav-)  Adj.  'gerade, richtig,    recht',    vom   Weg;   yJ   «./    °züi
hö  pa>5    stsöil  (sd.)   \.43.y,   —
"t  yif'S  asaatcä  vdislä  X'auhsusca  daiing  ^dstsks  (sd.)  'züs  ptitiS  yam  dagnom  saes- manauks  '':iw}ng  mazda  ahura  aabyd  .  .  \yanlS  dadat  Y.jj-z;  ~-  apänä  (sd.)  .  . "den  klugen,  die  du  nach  ihrer  Gerechtig-  aiat  a  'zFis  /a>ä  yais'ü  mazd'i  ahurS keit   und  ihrem   guten  Denken  für  (des)  |  *saiiti  ",  ,   zu   den  geraden   Wegen   zu
dby  Google
353
"arazav-
Asa  hin,  bei  denen  MAA.  wohnt"  Y.jj. 5.  a)  als   mask.  Subst   'der  gerade,
rechte  Weg"*:  yS  zaotil  asä  "zö/  (AP.) hvd  *mainySuf  H  vakHiilt  kayit  (sd.)  Y. SS'^'i  —  '"^  äng^'ote  *mar»daili  damä *'zaos'^  Aai%Tm  "so  macht  sich  das  Ich des  Z>/-»^enossen  den  gewissen  Lohn  des rechten  Wegs  zu  nichte"  \.$i.i:i^.
KompA.;  Ableit.  (s.  auch  är/a/a-).  —  Vgl. *fr>2af'  EN.  —  ai.  //<»■  Adj.  {Öfters  »om Weg).  —  %.XiOiiV}tis,>ria/d,  raäila;  JrJSVan-, inaanl:  —  Pü.:  apSfak,  NpÜ.:  xälii.  —  ')  " dazu  DBR.VglS.  7.565.—  »)  Pt4;  NA.  ■=** —  J>  S.  iSt.  JusTl  V,l.  SS.  237  {wo  weit Litt.),  Ethi_  IFAni.  /.  10.
=== leaf/col ===
leaf 222
['351', '353']
```


## [2026-09-04T23:09:39.587Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7655,7672p' BRT.txt"
}
```


### [2026-09-04T23:09:39.636Z] TOOL RESULT

```
•  j,  »radva-fana-  Adj,,  nur  fem,  'ni-  'deren Brüste  in  die  Höhe  stehen,  mit  straffen Brüsten':   kainTiiö  hhrpa  sriraya  .  .  'r/yä
H.2.9.
/hta-  ist  Komp.-Form  lU  /sfäna-;  s.  Bthl.  IF. 7,  6>  (wogegen  das  WZKM.  9.  167  (iesagle nichts  beweist).  —  ai.  vgl.  äriilivasfaiii-  fem. Adj.  —  Pü.:  *i/fiiU  filtin.
•  j.  araSwan-  Adj,  'der  gedeihen  lüsst, fördert':   mürS   vups  masdayamanam  .  .
dby  Google
351
*ar»dvaya
■»«zav-
35«
,  denen  .
"wäca  kiniwäca  "M.   ist  aller  J/aaÄi- i  würdig  erkannt  hast,  o  MAA. yasnei  Förderer  und  HUter"  Yt/0.120.    1Y.2Ä10,
Zum  V.  and:  \     El.?  —  Vü.:/r.irSn.   —   »  So  Ji,  K5;  NA.
I      ''iioB,  mit  uiii,'ii%isch«in  i\  s.  auch  Fu. •  j.  ''■«radvaya "  Adv.  'in  aufgerichteter  j        :  „j„äüii  p.  40:  lies  irinaxä. Stellung,    im    Stehen':    yat    allqm    ^J^d'  ^  .    \^^^^^.  „.  .gilber*:  car^ma  (sd)  .  . gavastrya  *var,smi  yr7zya,,tqm  . .     dass  ^^.^^  _  _  ,^  ^^^^^.^  Ylc  129;  '7-H, ■hnen.  wenn  sie  un  Stehen  landwirtschaft-   ^       g^  _  ^^^,„^  .^^^  ^J^^^^  z<,ramm; hche  Arbeiten  verrichten  ..'  N.^j  ,^^^  .^^,  -         ^^   ^^^^,  ^^^^
Afl//d».  -     ■)  Hds.  «««%.«/;    fl^  ist  möglich  P'l^ska   (sd.)    V.  i^.  1 1.  [Aog.  /?    llCSl
(s.  unter  jjjjrmi-),    aber   nicht   gerade    wahr- |  J/-»fl/J/(7l'i(.]
scheinlich;    i   falschlich    statt  ya   (wie  nach       KompA.;  Ableit.  —  Vßl.  ai.  rajaiä-  n.;  ann. Konsonanten,  S  ^^.J.  31);  s.  Bthl.  IF. //.  133. ;      arcaf.  —  Pü.:  asim.
.  j.  «rjdvöiohan-  Adj.  'des  Mund,  Ge- 1  •)•  »"?«•««■>•-  Adj.  (fem  •«-)  Von Sicht  nach  oben  gerichtet  ist':  ^oi  hl  miv  S'"'"'  *"»':  -«^  hara  l.sKiJ .  lO.  17;  - •»^».  (ASm.  sutt  ASn.)  ^„,ian^  »/»;  i  "■'  *'  'f"?  (»f"'-  '«/'""tf)  •»'  ^t/o. >,■«  «aV  /r^i  AI"*.»!'«  MI  zatt^gbya  "|;  — /°"  "7  '  ""•"■«»>«  (^^  ■  ■  •'" mannt  "so  (gross)  dass  er  (der  Xalai  i  *  Ableit!^  au/^I-«/^-  -  Pü  ■  aifm« nicht  an  seinen   (näml.   des  Toten)   mit ,    .  ^  _    .0  ,,'.,.  ,  .,,  ',     „  ,  j
dem  Gesicht  nach  oben  gerichteten  Kopf  l'^^'-^^^^o-P'^-'^dj-'^jlberg^^^^ anstosse,  nicht  vom  an  die  Füsse,  nicht  IJ"^"    ^f    V»?'^' «    (APn.) «    .y«ä«     rvi seitwärts  an  die  Hände"  V.j.ii.  !  !''.~'y^->'^' V"^,"-^''.  '^f^-'^f'««^'-
```


## [2026-09-04T23:09:47.932Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T23:09:47.940Z] TOOL RESULT

```


```


## [2026-09-04T23:09:52.333Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er%C7%B5-",
 "prompt": "Give the reconstructed root, its meaning, and the list of derived terms/descendants, especially any Indo-Iranian (Avestan, Old Persian, Sanskrit) and Latin (argentum, arguo) forms. Quote the etymology notes."
}
```


## [2026-09-04T23:09:53.290Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/borage",
 "prompt": "Quote the full etymology of borage, including any mention of Arabic abu araq 'father of sweat' and Latin borra 'rough hair'."
}
```


### [2026-09-04T23:09:59.151Z] TOOL RESULT

```
# Etymology of Borage

The word "borage" derives from Anglo-French *burage* and Old French *borage* (13th century), tracing back to Medieval Latin *borrago*.

**Folk etymology theory:** The Medieval Latin term was believed to come from Arabic *abu arak*, literally meaning "the father of sweat," supposedly used by Arab physicians to describe its effects on the human body.

**Scholarly etymology:** However, the OED and other sources propose an alternative origin: "Latin *borra* 'rough hair, short wool,' in reference to the texture of the foliage."

The word spread across Romance and Germanic languages, appearing as Spanish *boraja*, Italian *borraggine*, and German *Boretsch*.
```


### [2026-09-04T23:10:01.076Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂erǵ-

## Reconstructed Root and Meaning
The root is **\*h₂erǵ-**, meaning "white" and "shining."

## Key Derived Terms and Descendants

**Indo-Iranian Forms:**
- Sanskrit: अर्जुन (árjuna, "silver") and ऋज्र (ṛjrá, "shining reddishly, bright-colored")
- Avestan attestations appear through Proto-Indo-Iranian developments

**Latin Forms:**
- Latin arguō ("to make clear"), derived from Proto-Italic \*argus ("bright")
- argentum (silver) derives from the root via Proto-Indo-Iranian \*Hárȷ́unam

**Other Major Descendants:**
- Hittite: ḫarkiš ("white, bright")
- Ancient Greek: ἄργυρος (árguros, "silver") and ἀργός (argós, "white, bright")
- Proto-Celtic: \*argyos ("white")
- Proto-Germanic: \*akrą ("shining")

## Etymology Notes
According to scholarly sources, the root exhibits "Schwebeablaut" variations across branches. One reference notes that "the Indo-Iranian (\*h₂r̥ĝ-ró- > ved. r̥jrá-) and Anatolian (\*h₂r̥ĝ-i- > hitt. harki- 'white')" preserve the root distinctly across language families, supporting its reconstructed status based on comparative evidence.
```


## [2026-09-04T23:10:07.983Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/borage",
 "prompt": "Quote the full etymology section for the English noun borage, including all competing proposals (Arabic abu ʿaraq, Latin burra/borra, Latin cor ago), and any references cited."
}
```


## [2026-09-04T23:10:10.088Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%B2%DB%8C%D8%B2",
 "prompt": "Quote the Persian entry ارزیز: its meaning and full etymology (Middle Persian, Proto-Iranian, any relation to *arzata- 'silver' or Avestan ərəzata-), and cited references (Hasandust, MacKenzie, Bailey, Horn)."
}
```


### [2026-09-04T23:10:13.979Z] TOOL RESULT

```
# Etymology of Borage

Based on the Wiktionary article, here is the full etymology section:

The word borage comes from Middle English, borrowed from Old French **"borage"** (related to French "bourrache"). This traces back to Medieval Latin **"borrago,"** which has two competing etymological proposals:

1. **Latin origin**: From Latin **"borra"** meaning "short wool, rough hair"

2. **Arabic origin**: From Arabic **"أَبُو العَرَق"** (ʔabū l-ʕaraq), literally translating to **"father of sweat"**

The article does not mention a Latin "cor ago" proposal. The two main competing theories are the Latin "borra" and the Arabic "abu ʿaraq" origins, with Medieval Latin "borrago" as the intermediate form linking these possibilities to the modern English word.
```


### [2026-09-04T23:10:19.172Z] TOOL RESULT

```
# Persian Entry: ارزیز (arzīz)

**Meaning:** The word denotes "tin" in Persian, with an alternative synonym being قلع (qal').

**Etymology:** The entry traces this term through several language layers:

- **Middle Persian origin:** "From Middle Persian ʾlcyc (arzīz, 'tin, lead')" in Manichaean form
- **Proto-Iranian connection:** The document suggests "perhaps ultimately from Proto-Iranian *arjata- ('silver')"
- **Avestan relation:** It is "cognate with Avestan ərəzata"
- **Sanskrit parallel:** Related to Sanskrit रजत (rajatá, 'silver')
- **Proto-Indo-European root:** Traced to "*h₂erǵ-"

The term also appears in Middle Armenian արճիճ (arčič, "lead") as an Iranian borrowing, and spawned the Arabic descendant رَصَاص (raṣāṣ).

**Cited References:** The entry cites "Rastorgujeva, V. S. and Edelʹman, D. I. (2000), Etimologičeskij slovarʹ iranskix jazykov [Etymological Dictionary of Iranian Languages]" as its primary source, though Hasandust, MacKenzie, Bailey, and Horn are not mentioned in this Wiktionary article.
```


## [2026-09-04T23:10:38.521Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 64 -l 64 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg64 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg64.png"
}
```


### [2026-09-04T23:10:41.130Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 62766 Sep  4 19:10 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg64.png
```


## [2026-09-04T23:10:41.902Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FVQ araq ===\"; grep -n -i -E \"^'araq|ʿaraq|araq\" FVQ_pages.txt | head -10; echo \"=== AFA ===\"; LC_ALL=C grep -n -i \"araq\" AFA.txt | head -5; echo \"=== DOZ ===\"; LC_ALL=C grep -n -i -E \"arak|borrago|bernagie\" DOZ.txt | head -10; echo \"=== LAM ===\"; LC_ALL=C grep -n -i -E \"bourrache|arak|araq\" LAM.txt | head -10; echo \"=== DEV bourrache ===\"; LC_ALL=C grep -n -i \"ourrache\" DEV.txt | head; echo \"=== HJB arrack ===\"; LC_ALL=C grep -n \"^ARRACK\" HJB.txt | head"
}
```


### [2026-09-04T23:10:42.024Z] TOOL RESULT

```
=== FVQ araq ===
6990:of Saraqa in Aghani, xv, 138.
9158:If we can trust the genuineness of a verse of Saraqa b. 'Auf in
=== AFA ===
=== DOZ ===
210:Vreemde karakters heb ik zooveel mogelijk vermeden. Geheel
592:In het klassieke Arab. beduidt 'arak ( jx) eigenlijk
602:vels in Morocco, II, p. 208. Dit is de eigenlijke 'arak
603:of 'arakï; maar bg verloop van tijd is dit (wat in
616:Weme {Beise nach Mandera , p. 78) geeft araki^
617:Branntwein; bij Bocthor vindt men eau-de-vie, 'arak
618:en 'araki; de laatste vorm staat ook bij Marcel op
620:p. 161. In Oost-Indië wordt de naam 'arak gegeven
629:kIko arak en rack ft batsle srhgnt wel eene Engel-
1196:(Xil^). Afgeleid van den wortel haraka, verbranden,
=== LAM ===
1055:souvent sacrifiée, par ex. : caraque^ cende, dénébola,
1177:dérivent directement d'un pluriel arabe : caraque, bu-
2024:a:{âd darakht, qui nous a été transmis par les Arabes, est
3103:Caraque. Un des plus grands vaisseaux ; il servait à la
4045:est divisée»; dejjifâreq part. prés, de J/faraq diviser,
6051:arak, araque, orraca, rak. Tous ces mots représentent
6052:l'arabe J^ 'araq, liqueur extraite du palmier, qu'on fai-
6055:forme Jy. 'araqt (Dartias), d'où dérive probablement
6057:de-vie f 1 ). En turc usuel j^ 'araq devient rake, eau-de-
6058:vie. (V. R, Youssouf. s. V. 'arak).
=== DEV bourrache ===
=== HJB arrack ===
2190:ARRACK,  RACK.
```


## [2026-09-04T23:10:44.817Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg64.png"
}
```


### [2026-09-04T23:10:45.324Z] TOOL RESULT

```

```


## [2026-09-04T23:10:45.322Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-04T23:11:03.521Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; grep -l 'error_in' *.json | head; echo \"---\"; python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('/home/sfmqrb/git/rishe/data/verification/page-*.json')):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        for n in e.get('nodes',[]):\n            if n.get('verdict')=='transcription_suspect':\n                print(f.split('/')[-1], n.get('id'), n.get('words'), '|', n.get('error_in'), '|', (n.get('book_prints') or '')[:60],'|',(n.get('correct_form') or '')[:60])\n                print('   ', (n.get('derivation') or '')[:300])\nEOF"
}
```


### [2026-09-04T23:11:05.364Z] TOOL RESULT

```
page-311.json
page-101.json
page-33.json
page-39.json
page-46.json
page-54.json
---
page-101.json 4 smaraldos | book | smaraldos : a shiny stone, emerald | smaragdos
    The Greek word is σμάραγδος smáragdos (also μάραγδος máragdos), 'emerald, green gem' (Herodotus, Theophrastus; Marcus Aurelius); 'smaraldos' with -ld- is not a Greek form and is almost certainly a misreading of the -gd- cluster (gd → ld) in the scan, since Klein (KLN:514) prints smaragdos. Etymology
page-311.json 13 hava-rd | book | hava-rd : well grown, well built, beautiful ☞ Su 1 | hu-raoda (Av. huraoδa-)
    'hava-rd' is not a possible Avestan form; the book almost certainly printed hu-raodha (Av. huraoδa-), and the scan lost/garbled letters. Av. huraoδa- 'well-grown, well-shaped, handsome' is a real Young Avestan adjective (Vidēvdād 3.24 'iδa carāiti huraoδa'; epithet of Sraoša in Yasna 57), built from
page-33.json 2 abŭ «آبو ( ابوی )» | extraction | اَبو ( ابوی )  [plain alef + fatḥa, no madda; the parenthesi | ابو ( ابوی )
    The derivation is right — Persian ابو abu is a straight Arabic loan, taken over with the kunya formula after the Islamic conquest and productive in Persian names from the 10th c. on: ابوعلی سینا, ابوالفضل, ابوالقاسم, ابوالحسن, ابوالفتح, with the colloquial contraction ابوال- > بوال- in بوالهوس bu'l-
page-39.json 12 eter «اثر» | extraction | اتر | اتر
    The word itself is right: Persian اتر eter is the modern chemistry term borrowed from French éther (diethyl ether), distinct from the older Arabic-mediated اثیر asīr of node 9, and Mo'in's entry اتر explicitly cross-refers to اثیر. But the Persian script in the JSON is wrong: the book prints اتر (al
page-46.json 3 `rtk : flower | book | `rtk : flower | `rtk : flour
    The word and the derivation are right; the GLOSS is wrong. Sogdian ʾrtk (Buddhist/Sogdian-script ārtē, also written ʾrtʾk(w), Christian-script ʾrty) means 'FLOUR', not 'flower'. It is the same *arta-ka- 'ground (stuff)' formation as the Persian word — Ir. *ārta- (< PIE *h₂l̥h₁-tós) plus the Sogdian 
page-54.json 1 anya, aimya | book | anya, aimya : other | anya, ainya
    The word is Av. anya- 'other', with its Younger Avestan by-form ainya- and OP aniya- - a *-yo- derivative of the demonstrative stem (*h₂en-yo-), regularly matched by Skt. anyá-. The JSON's second form 'aimya' is not a possible Avestan shape: Pokorny prints 'ai. anyá-, av. anya-, ainya-, apers. aniya
page-56.json 13 šatrang «شترنگ» | None |  | 
    The word itself and the chain are certain: MP čatrang > Classical NP چترنگ čatrang / شترنگ šatrang 'chess', Arabicised as شطرنج šaṭranj (Arabic has no /č/, so چ is rendered ش, and the t is written ط by attraction to the emphatic environment), and then re-borrowed into New Persian in that Arabic dres
```


## [2026-09-04T23:11:18.058Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/argue",
 "prompt": "Quote the full etymology of argue, including Latin arguere and its PIE root, and any cross-reference to argent/argentum."
}
```


## [2026-09-04T23:11:20.265Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D8%B1%D9%82",
 "prompt": "Quote the Arabic entry عرق: the root ع ر ق, the verb عَرِقَ (ʿariqa) 'to sweat', the noun عَرَق (ʿaraq) 'sweat; distilled liquor/arrack', and its etymology; also quote the Persian section for عرق if present."
}
```


### [2026-09-04T23:11:24.429Z] TOOL RESULT

```
# Etymology of "Argue"

Based on the Online Etymology Dictionary entry, here is the full etymology:

The word "argue" dates to around 1300, derived from Old French *arguer*, which ultimately traces to Latin *arguere* meaning "make clear, make known, prove, declare, demonstrate." This Latin term comes from "a suffixed form of PIE root *arg- 'to shine; white'."

**Direct quote from the source:**

"make clear, make known, prove, declare, demonstrate" (from a suffixed form of PIE root *arg- "to shine; white").

The etymology further notes that according to De Vaan, *arguere* is probably "a denominative verb 'to make bright, enlighten' to an adj. *\*argu-* 'bright' as continued in *argutus*."

**Important note:** The provided webpage does not contain any cross-reference to "argent" or "argentum," though these words would logically share the same PIE root (*arg-*) meaning "to shine; white."
```


### [2026-09-04T23:11:31.251Z] TOOL RESULT

```
# Arabic Entry: عرق

**Root:** ع ر ق (ʕ r q)

**Verb عَرِقَ (ʕariqa):** "to sweat, to perspire" — Form I verb with non-past يَعْرَقُ (yaʕraqu)

**Noun عَرَق (ʕaraq):** Multiple meanings including:
- "sweat, perspiration"
- "arrack (a clear raisin liquor that turns cloudy when water is added)"
- Verbal noun of عَرِقَ

**Etymology note:** The word shares cognate status with Ge'ez ዐረቀ (ʿäräḳä), meaning "to be naked, to be orphaned, to be childless, to be bereft."

# Persian Section

The document indicates Persian has an entry for عرق but the full content is truncated. The page structure shows Persian section 6 exists with Etymology 1, Pronunciation, Noun, Derived terms, and Further reading subsections, but the detailed definitions are not provided in the excerpt supplied.
```


## [2026-09-04T23:11:36.401Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=borage",
 "prompt": "Quote the American Heritage Dictionary entry for borage, especially its etymology (Middle English, Old French, Medieval Latin borrago, Arabic abu ʿaraq or Latin burra)."
}
```


## [2026-09-04T23:11:36.971Z] TOOL CALL #43: WebSearch

```json
{
 "query": "borage etymology \"abu araq\" Arabic not attested OED borra rough hair"
}
```


### [2026-09-04T23:11:40.256Z] TOOL RESULT

```
Web search results for query: "borage etymology "abu araq" Arabic not attested OED borra rough hair"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T23:11:41.087Z] TOOL RESULT

```
# Borage Etymology

According to the American Heritage Dictionary, borage's etymology traces back through multiple languages:

**"[Middle English, from Old French *bourage*, from Medieval Latin *borāgō*, probably from Arabic *bū'araq*]"**

The entry further explains that the Arabic root likely derives from *'abū 'araq*, meaning "source of sweat," reflecting the plant's historical use as a sudorific agent. The word's journey from Semitic origins through Romance languages into English demonstrates the interconnected linguistic heritage embedded in common English vocabulary.
```


## [2026-09-04T23:11:52.914Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LEW argentum ===\"; LC_ALL=C grep -n \"argentum\" LEW_1910.txt | head -3; echo \"=== LAT argentum ===\"; LC_ALL=C grep -n -i \"^argentum\\|argentum,\" LAT.txt | head -5; echo \"=== LAT arguo ===\"; LC_ALL=C grep -n \"^arguo\" LAT.txt | head -3; echo \"=== TLM ardata ===\"; LC_ALL=C grep -n -i \"ardata\\|ardastana\" TLM.txt | head -5; echo \"=== HJB arrack ===\"; sed -n '2190,2205p' HJB.txt"
}
```


### [2026-09-04T23:11:53.032Z] TOOL RESULT

```
=== LEW argentum ===
=== LAT argentum ===
4973:argentum est l'un des noma, tir' 4 a d'une a em e racine, par leaquels
18223:Sbur eat neutre coaae lea noas de aatifere: aurum, argentum, marmor,
40123:cialisd dans 1’eaploi de mutuum argentum, d'ou mutuum n.: argent
46127:numquam aurum, numquam argentum, uix pecuniam donauit . Conserve,
51246:argentum purum putum "argent pur [et] sans melange". Ancien (Pl.)>
=== LAT arguo ===
4962:arguo
=== TLM ardata ===
663:Ardastana  a0angaina  Darayavahaus  XSbya  vi0iya  karta
1084:a6a”gaina  or  a0a"gaina,  adj.  of  stone.  Nom.  sg.  m.  a$angaina, Dar.  Pei'S.  C.  ardastana  a$a"gaina.  Acc.  Sg.  f .   a6a"gainam,  Al’t.  Sus. c;  a0a"ganam  for  a$angainam,  Art.  Pers.  a,  b,  3.  YAv.  asanga  (New Pers.  sang,  Horn,  NS,  38,  2).  Cf.  KZ.  39,  69.
1154:ardastana,  m.  window-cornice  (?).  Nom.  sg.  ardastana,  Dar. Pers.  C.  ardastana  a#angaina  darayavahaus  XShya  vi0iya  karta.  *arda, half. \   YAv.  arada  -f-  stana,  YAv.  -stana  (New  Pel’s,  stan),  Skt.  sthana; cf.  Bartholomae,  Altiran.  Wb.,  193.  Foy,  KZ,  35,  48.  connects the  first  member  of  the  compound  with  Av.  arazo,  bright ,   Skt. rira.
=== HJB arrack ===
ARRACK,  RACK.
ABGUS  PHEASANT,  s.  This name,  which  seems  more  {)roperIy  to belong  to  the  splendid  bira  of  the Malay  Peninsula  {Argiuomus  giaantetu, Tem.,  Pavo  arguSj  Lin.),  is  confusingly applied  in  Upper  India  to  the  Hima- layan homed  pheasant  Cer%om%8  (Spp. saiyra^  and  melanocephala)  from  the round  white  eyes  or  spots  which  mark a  great  part  of  the  bird's  plumage. — See  remark  under  MOONATJIh
ABBAGK,  BACK,  s.  This  word is  the  Ar.  'arcLky  properly  *  perspira- tion,' and  then,  first  the  exudation or  sap  drawn  from  the  date  palm CaraJb  <U-tamar) ;  secondly  any  strong arini,  'distilled  spirit,'  *  essence,'  etc. But  it  has  spread  to  very  remote comers  of  Asia.  Thus  it  is  used  in the  forms  ariki  and  arki  in  Mon^lia and  Manchuria,  for  si)irit  distilled from  grain.  In  India  it  is  applied to  a  variety  of  common  spirits ;  in 8.  India  to  those  distilled  from  the fermented  sap  of  sundry  palms ;  in E.  and  N.  India  to  the  spirit  distilled from  cane-molasses,  and  also  to  that from  rice.  The  Turkish  form  of  the word,  rdiiy  is  applied  to  a  spirit made  f  roiii  grape-skins ;  and  in  syria and  Eaj-pt  to  a  spirit  flavoured  with, aniseed,  made  in  the  Lebanon.  There is  a  popular  or  slang  Fr.  word,  riquiqui^ for  Drandv,  which  appears  also  to  be derived  from  aratt  (Marcel  Devic). Humboldt  (Examen,  &c.,  ii.  300)  says that  the  woixl  first  appears  in  Pigafetta's Voyage  of  Magellan ;  but  this  is  not correct.
c.  1420.— "At  every  yam  (post-house) they  give  the  travellers  a'  sheep,  a  goose,  a fowl  ....  'arak.  .  .  r—Shah  RvWs  Em- bassy to  China,  in  N.  k  E.,  xiv.  396.
1616. — "And  they  bring  ooooa-nuts, huxraca  (which  is  something  to  drink) .  .  .  ." "-Barbosa,  Hak.  Soc.  59.
1518. — " — que  todos  os  mantimentos  asy de  pSo,  oomo  vinhos,  onaeas,  arrozes, cames,  e  pescadoe." — In  Arditv,  Port, Orient,,  fasc.  2,  57.
1521.— "When  these  people  saw  the politeness  of  the  captain,  they  presented some  fish,  and  a  vessel  of  palm-wine,  which they  call  in  their  language  maca.  .  .  ." — Pigafetta,  Hak.  Soc.  72.
1544. — "Manueli  a  cruce  ....  commendo ut  plurimum  invigilet  duobus  illis  Christian- orum  Carearum  pagis,  diligenter  attendere ....  nemo  potu  Omusaa  se  inebriet  .  .  . si  ex  hoc  deinoepa  tempore  Punicali  Oriaoha notetur,  ipsos  ad  mihi  suo  gravi  damno luituros."— &h'.  Fr,  Xav.  Epistt,,  p.  111.
1554. — "And  the  excise  on  the  orraqwu made  from  palm-trees,  of  whioh^  there^  are three  kinds,  viz.,  cvro,  which  is  as  it  is drawn ;  orra^fiia,  wnich  is  ptetv  once  boiled {potUdfi,  qu.  distilled  f) ;  aharab  {xaraa)  which IS  boiled  two  or  three  times  and  is  stronger than  orrafua.**—S,  Botelho,  Tombo,  50.
156S.— "One  kind  (of  oooo-pahn)  they keep  to  bear  fruit,  the  other  for  the  sake  of the  ptra,  which  is  vino  mosto;  and  this  when it  has  been  distilled  they  call  arraoa." — Garcia  />'0.,  f.  67.  (The  word  ncrO,  used here,  is  a  very  ancient  importation  from India,  for  Commas  (6th  century)  in  his account  of  the  oooo-nut,  confounding  (it would  seem)  the  milk  with  the  toddy  of  that palm,  says:  "The  ArgelUon  is  at  first  full of  a  very  sweet  water,  which  the  Indians drink  from  the  nut,  using  it  instead  of  wine. This  drink  is  called  rhcneosura,  and  is extremely  pleasant."  It  is  indeed  possible that  the  rhonco  here  may  already  be  the word  arrack).
1605. — "A  Chines  borne,  but  now  turned lauan,  who  was  our  next  neighbour  .... and  brewed  Araoko  which  is  a  kind  of  hot drinke,  that  is  vsed  in  most  of  these  parts  of the  world,  instead  of  Wine.  .  ." — E.  Scot,  in FurchM,  1. 178.
1631.—".  .  .  .  jecur  ....  a  potu  istius maledicti  Arao,  non  tantum  in  tempera- mento  immutatum,  sed  etiam  in  sub8tanti& SU&  corrumpitur."--Va<r.  BonHus,  lib.  ii.  cap. vii.  p.  22.
1687.—"  Two  jars  of  Araek  (made  of  rice as  I  judged)  called  by  the  Chmese  SamJtu [BajBMhooy—Ikanpier,  i.  419.
1719. — "We  exchanged  some  of  our  wares for  opium  and  some  axnick.  .  .  .** — Robiiuor^ Cntsoe,  Ft.  II.
1727.—"  Mr  Boucher  had  been  14  Months soliciting  to  procure  his  Phirmaund ;  but his  repeated  Petitions  ....  had  no  Effect. But  he  had  an  Englishman,  one  jSuun,  for his  Interpreter,  who  often  took  a  laige  Dose of  Azraok.  .  .  .  Swan  got  pretty  near  the King  (Aurungseb)  ....  and  cried  with  a loud  Voice  in  the  Persian  language  that his  Master  wanted  Justice  done  him"  (see DOAI).— ^.  Hamilton,  i,  97.
Rack  is  a  further  corruption ;  and  rack- punch  is  perhaps  not  quite  obsolete.
```


## [2026-09-04T23:12:01.706Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4955,4990p' LAT.txt"
}
```


### [2026-09-04T23:12:01.762Z] TOOL RESULT

```
argeaOnia, -ae f,; piante. Sorte de pavot sauvage. AttestA depuia
Celse et Pline. Adaptation du gr. ipYSjittVTi (cf. argenon, argenonion dans
Pline), souvent corroapue, en agrisonia, M.L.995a , acrimonia, argi-
nonia.
argentun, -I n.: argent; argentarie, ob^et d 1 argent; argent (non-
naie, dAjA dans Plaute); argentun uluum ■ uBpapyupoc. Ancien, usuel.
Psnroaan. N.L.640.8 i
arguo
Ddriy^a: argenteus, et subat, argenteus m.: monnaie d'argent, M.L.639;
argentarius: relatif 1 1'argent (monnaie), et argentdrius a.: ban~
quier, frappeur d'argent, M.L.637; argentaria-, banque, mine d'argent;
argenteolus: [monnaie] d'argent; argentatus (et inargentatus, Plin.,
Ital.): argenti; d'ob eat tir£ le yerbe argento, -as-, argentosus: neld
d 1 argent; ArgentInus : dieu de 1 'Argent (Aug.Ciu.4j4i); argentifodina :
mine d'argent (ancien juxtaposrf).
Le nom eat neutre, en face de gr. apyupoc, comme toua lea noma de
m^taux latina, cf. aurum en face de xpucroc, etc.; pour le suffixe, cf.
unguentum ; et y.Benyeniste, Origines, p.14,151.
argentum est l'un des noma, tir' 4 a d'une a em e racine, par leaquels
eat d£sign 4 1 'argent. Le celtique a la neme forme: gaul. arganto- dans
Argantomagus litt. "cbamp de 1 'argent", iri. airget, galL ariant. Mais
la forme osque aragetud "argento" ne concorde pas exactement. Arm.
areat'"argent", tokh. A drkyant, ay. arezatam et skr .rajatdm diffbrent
plus encore. Quant 1 gr. apyupoC, c'eat'un ddrivd du thbme en -u-. qui
apparait dana lat.argud (y. ce mot). On entreyoit donc ici une mime
mani&re, d 4 jk indo-europ 4 enne,.de designer 1'"argent" comme mdtal
"brillant", de meme que l'"or" itait nommi m^tal "jaune" (y. le mot
beluos), cf. gr. apyoc "clair, brillant"; maia on ne peut reatituer un
nom indo-europden: c'eat que 1'argent et l'or sont nonnis d'aprbs leur
aspect, tandis que le nom du "cuiyre" (et du "bronze"), lat. aes , etc.,
diaigne purement et aimplement l'objet et ne ae laisae pas analyser,
- La diaignation indo-europienne de 1 '"argent" a iti remplacie par un
mot amprunti qui offre des formea diyeraea en germanique, en baltique
et en slaye. - V.arguti.
argilla ( l, cf. Ettmayer Zeits.f. rom. Phil.30,544 ®,547 ), “*« f«:
argile. Emprunt au gr. apyi.Xoc (apyiXXoc), ddji dans Caton, Agr.40,4;
```


## [2026-09-04T23:12:12.888Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON عرق ===\"; LC_ALL=C grep -n \"عرق:\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -6; echo \"=== BQT v2/v3 عرق ===\"; LC_ALL=C grep -c \"عرق\" BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null; echo \"=== RCH araq ===\"; LC_ALL=C grep -n -i \"sweat, perspiration\" RCH.txt | head -5"
}
```


### [2026-09-04T23:12:13.006Z] TOOL RESULT

```
=== MON عرق ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:60709:معرق: 121012۲۲6۵ [ع.] (امف.) مرد کم گوشت 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:60714:معرق: 1۱2012116 [ع.] (افا.) آنجه که تو لید 
MON_part2.txt:60709:معرق: 121012۲۲6۵ [ع.] (امف.) مرد کم گوشت 
MON_part2.txt:60714:معرق: 1۱2012116 [ع.] (افا.) آنجه که تو لید 
MON_part1.txt:9605:استادن. ارتکاز عرق: برجستن رک بربدن 
MON_part1.txt:41567:تعرق: «221۲0) [ع.] (مص‌ل.) عرق کردن» 
=== BQT v2/v3 عرق ===
incoming/BQT/BQT_v3_pages.txt:22
BQT_v2_pages.txt:13
=== RCH araq ===
```


## [2026-09-04T23:12:16.388Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; LC_ALL=C grep -n \"^عرق\\|عرق: \" MON_part2.txt | head -10; echo \"---broad---\"; LC_ALL=C grep -n \"عرق\" MON_part2.txt | sed -n '1,25p'"
}
```


### [2026-09-04T23:12:16.488Z] TOOL RESULT

```
18280:عرق که از تقطیر جوشانده ريشه و برگ‌های 
18282:عرق... کاسنی صحرایی: (گیا.) گیاهی است 
41465:عرق شیر ین کرده است. 
53468:عرق البخیل» عرق بخبل» خومه» فرژ فرزد» 
55459:عرق از آنها ببرون آید؛ ج. تا ها نتم اج 
60709:معرق: 121012۲۲6۵ [ع.] (امف.) مرد کم گوشت 
60714:معرق: 1۱2012116 [ع.] (افا.) آنجه که تو لید 
60715:عرق کند عرق آور» خوی‌آور. (پز.) 
74396:عرق شدن هستند. 
88555:عرق فراوان است. سیر هاری از شروع 
---broad---
763:غدد بزاقی و غدد مترشحهةٌ عرق. این گونه 
1296:غرقی و مهدوم علیهم: (فق.) عرق شدگان و 
6680:معرق و زیاد کنندةٌ ترشحات صفرا تجویز 
8574:فلفل» عرق الذهب. فلفل دراز؛ بیل» پیپلی؛ 
12764:تشقرق: جعرق, [تر. - قشقره] (1.) (عم.) 
13398:و عرق آور مصرف می‌شود و در استعمال 
18262:بنام عرق کاسنی مورد استفاده قرار می‌دهند. 
18279:نوبه‌ یی مصرف می‌گر دد. عرق کاسنی: (پز.) 
18280:عرق که از تقطیر جوشانده ريشه و برگ‌های 
18282:عرق... کاسنی صحرایی: (گیا.) گیاهی است 
18570:بطوطه). کاشی غاز مغازی: کاشی. معرق. 
18975:که معرق «کاک» است به الخیز المحترق؛ 
29739:دارای اثر معرق و مدر و نرم کننده است و 
32963:معرق است؛ کزبره» کسبر ه؛ جلحلان. آش 
33668:سیفیلیس و مدر و معرق و ضد کرم می‌باشد؛ 
33809:سرفه و معرق مورد استعمال دارد. گل 
39105:(عم.) فقط صرف دون متعلقات عرق 
40914:تهیه: نیم من بادام سفید را در عرق یاس یا در 
41465:عرق شیر ین کرده است. 
42904:اندام‌ها و ترشح عرق فراوان و تب 
51233:معمولا عرق روی آن را فرا نمی‌گیرد. دورة 
53170:اثر مقوی معده و بادشکن و معرق و ضد 
53349:اين ناخوشی که بنام عرق مدنی نیز موسوم 
53455:خون و معرق و نرم کننده نیز ذ کر شده 
53467:بخیم» ار یق‌او تی؛ بسخیل» عرق الاسخیل؛
```


## [2026-09-04T23:12:28.689Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂erǵ-' --note 'page 64, root Arg: PIE *h2erg- \"white, shining\" reconstruction, descendants incl. Latin argentum/arguo, Skt arjuna/rjra' 2>&1 | tail -5; python3 tools/fetch_source.py 'https://www.etymonline.com/word/borage' --note 'page 64, entry A.r.q node 3/5: borage etymology, Arabic abu arak called folk etymology, OED prefers Latin borra' 2>&1 | tail -5; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/borage' --note 'page 64, entry A.r.q: borage etymology, competing borra vs abu l-araq' 2>&1 | tail -5"
}
```


### [2026-09-04T23:12:38.784Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/12871297dbd7fd73.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7132c6e9ee680f10.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1f5b311fdd534ea6.txt
```


## [2026-09-04T23:12:42.722Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in 'https://en.wiktionary.org/wiki/ارزیز' 'https://www.etymonline.com/word/argue' 'https://en.wiktionary.org/wiki/عرق' 'https://ahdictionary.com/word/search.html?q=borage'; do python3 tools/fetch_source.py \"$u\" --note \"page 64 verification\" 2>&1 | tail -2; done"
}
```


### [2026-09-04T23:13:05.418Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0013bab04a208776.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ed29d420d493d28c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b4ec0026f93755ac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/190cfd02015a87df.txt
```


## [2026-09-04T23:13:14.794Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ar%C7%B5atam",
 "prompt": "Quote the Proto-Iranian reconstruction for 'silver' and its descendants (Avestan ərəzata-, Old Persian ardata-, Middle Persian, Ossetian, Sogdian), and any note about Persian arzīz."
}
```


## [2026-09-04T23:13:16.467Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/argent",
 "prompt": "Quote the etymology of argent and of the PIE root *arg-, listing the descendants mentioned (Latin argentum, Greek arguros, Avestan erezata, Old Persian ardata, Sanskrit arjuna, Hittite harkis, Tocharian) and English words from it including Argentina."
}
```


### [2026-09-04T23:13:22.550Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T23:13:28.009Z] TOOL RESULT

```
# Etymology of Argent and *arg-

## Argent

"Early 15c., 'silver, silver coin,' from Old French _argent_ 'silver, silver money'" derived ultimately from Latin _argentum_ through the PIE root meaning "to shine; white."

## PIE Root *arg-

"Proto-Indo-European root meaning 'to shine; white,' hence 'silver' as the shining or white metal."

## Descendants Listed

The etymology mentions these language descendants: Sanskrit _rajata-_ and _arjuna-_ (white, shining); Avestan _erezata-_; Old Persian _ardata-_; Armenian _arcat_; Greek _arguron_; Latin _argentum_; Old Irish _argat_; Breton _arc'hant_; and Hittite _harki-_ (white).

## English Words Derived

Words formed from this root include: argent, Argentina, argentine, Argo, argue, Argus, hydrargyrum, and litharge.
```


## [2026-09-04T23:13:35.198Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://www.etymonline.com/word/argent' --note 'page 64, root Arg: PIE *arg- descendants incl. Av. erezata, OP ardata, Lat argentum; English argent, Argentina, argue' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://ahdictionary.com/word/indoeurop.html' --note 'page 64: AHD/Watkins Indo-European roots appendix, root arg- \"to shine; white; the shining or white metal, silver\"' 2>&1 | tail -2"
}
```


### [2026-09-04T23:13:38.033Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/da8fd51241d626ac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/24cd7948c66bfb96.txt
```


## [2026-09-04T23:13:45.972Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; LC_ALL=C grep -n \"ارزیز\\|ارزیر\\|ارزبز\" BQT_v1_pages.txt BQT_alt_v1.txt BQT_dli_part1.txt 2>/dev/null | head -10; echo \"=== ctx ===\"; sed -n '16970,16990p' BQT_v1_pages.txt"
}
```


### [2026-09-04T23:13:46.066Z] TOOL RESULT

```
BQT_v1_pages.txt:16979:۳ در هاون ارزیز
BQT_alt_v1.txt:30190:آنرا در هاون ارزیز 
=== ctx ===
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
```


## [2026-09-04T23:13:55.022Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== NYB ===\"; LC_ALL=C grep -n -i \"arzīz\\|arziz\\|lcyc\\|Zinn\" NYB_vol2_glossary.txt | head; echo \"=== FRS ===\"; LC_ALL=C grep -n \"ارزیز\" FRS_pages.txt FSF_pages.txt 2>/dev/null | head; echo \"=== SIN tin ===\"; LC_ALL=C grep -n -i \"arziz\" SIN.txt HENNING_selected_papers.txt 2>/dev/null | head; echo \"=== ARY latin index ARG ===\"; LC_ALL=C grep -n \"ARZIZ\\|ARDATA\\|EREZATA\\|ARGENTUM\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-09-04T23:13:55.142Z] TOOL RESULT

```
=== NYB ===
=== FRS ===
FRS_pages.txt:6662:      ‫گوید‪:‬‬        ‫آلت رویینه ومسینه بود وارزیزنی زکفشیر بود » عنصری‬
FRS_pages.txt:6686: ‫بارزیز بندند و دوشانند[ ص ‏‬     ‫ودان‬
FRS_pages.txt:6697:                       ‫‪-‬‬          ‫دوسانند نی چسبانند ]آن ارزیز کرفاشبر خوانند ‏‬
FRS_pages.txt:8324:‫با سپید است همچو سیم ارزیز"‬                  ‫گرچه زرد است همچو زر" دشیز‬
FRS_pages.txt:20186:                 ‫کاورسهایی بودکهاز زر و سم و ارزیز سازند م‬
FRS_pages.txt:20222:     ‫‪ + ۳۰ -۱‬کهله کاوزسهای سیمو زر و ارزیز بدود مستعمل دارندکه ببدادنا زززن‬
FSF_pages.txt:14767:                    ‫ستدن (با زیر اول و زبر دوم)‬                        ‫بیاورد ارزیز و رویین لويد‬
FSF_pages.txt:18030:‫مسینه و ارزیز؛ لحیم کهزر و نقره و دیگر‬          ‫به گیتی درون کامگاران بدند‬
FSF_pages.txt:20201:           ‫بیاورد ارزیز و رویین لويد‬                         ‫بدو گفت خاقان جزین رای نیست‬
=== SIN tin ===
=== ARY latin index ARG ===
2232:ARZIZ (pid o Ki g sass 5" al'A a) jay! (PERSIAN) upd
2235:ARKI ARDATA- (OLD PERSIAN) skal +s,
2236:ARKWI (TOKHARIAN B) B 555 ARZIZ, ARZIZEN (PAHLAVI) 6 ky
2244:DELAMARRE: (ARGENT) 179 ARGENTUM (LATIN) 3)
```


## [2026-09-04T23:14:52.553Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; LC_ALL=C grep -n \"Hälfte\\|halb\" BRT.txt | sed -n '1,12p'"
}
```


### [2026-09-04T23:14:52.605Z] TOOL RESULT

```
2536:nam    I3r9ztmmm     V.  4.  50,    ,.5»,    Yt  2.        Nachsati  zu  dem  Vordersatz  mit  j^:a'. u,  Vd.4;  -  t/P«  Vd.;5;  -    HaAc  yat\^   .    ^-^^^  ^^^    ^j  .^  deshalb',  auf
3256:•  j.  adairi  Praep.  'unter,  unterhalb';  i)  mit Akk.:    ao'  hax>m  nivöiryeite  V.  <¥.  69;  —
3894:Hälfte  der  Nacht'>:  -rsm  Y.-ijh.  [N.
4183:Zum  Praes,  31  anAiya.;  S  ^09-  4-  "  VgL ^at/hayav-  EN.  —  Pü. :  k?  andar  iur"J«') ahräkih  kämaktum  bül.  —  ')  Die  Abtrennung der  PaTa.gra.phen  ist  in  den  Hds.  verwirrt;  die Worte  aak-  aiac'  gehören  noch  m  %  2.  — 3)  Weshalb  man  aohuyaoi  fälschlich  als  LD. erklärte ;  zuletzt  Bn.  Stnd.  /.  39a
4231:•  g.  an-aeäa-  Adj.  'der  nichts  (auszu- richten) vermag,  unvermögend,  unwirk- sam, einflusslos':  vaeda  tat yo.  ahmt  mazdn, °sS  "ich  weiss  das,  weshalb  ich,  o  M., nichts  (auszurichten)  vermag"  Y.46.2;  — y?  'um  x/qnm3ng(sd.)  radnn  *väcim'^  Turps asürahyä  ..  ^lla.xsa'^rlm  (sd.)  Y.  2^.9.
4257:■Wortl.''eo  prias',  IS.  aus  aita-.  —  Pii, :  \.  Hälfte fehlt,    dann;    ätigäh    an    pa  mäiiit  rf^nd  afF
4330:•  j.  an-antar9  Adv.  'nicht  innerhalb,  nicht drinnen' :  "^rigiimi  antar}  'tan  aia  antar? fata>a.^  N..Vy(?).
4393:•  g.  anäi§  ä  adv.-aitige  Verb,  'dadurch, damit,  auf  diese  Weise,  deshalb,  also', zurückweisend:   "näis  ä  manoAtm   ahüm
4536:•  j.  an-us'kante  Inf.  'nicht  (wieder)  aus- zugraben':^j/  aitika  zsmS  nikante  spsnasifa irista  ,  .  ttaimtm  yär3.dräjS  an'  "wenn man  hier  in  die  Erde  eingräbt  tote  Hunde und  . .,  ein  halbes  Jahr  lang,  (um  sie  nicht sva.)  ohne  sie  wieder  auszugraben"  V.  J.36.
4567:•  j.,  g,  antarl,  p.a'^ar  i)  Adv.(?)  Innen, innerhalb;  dazwischen':  "ämyS yiin  °r>  vTta (sd.)  °r^''  ärJyff  maya  /rakäraysH  \ .  <). 11;  —  '"%rigämi    °ri   anantar)   a%a    °r?
4568:pata%a  yat  °r>  vä  aat  -rs  vä  . ."  N. i^j.  1)  Praen,  a)  mit  Akk.  'innerhalb, in,  unter,  zwischen';  a)  räumlich,  auf  die Frage  wo?  und  wohin?:  I  'r  imil  dakyävJ' tnarüyJ'  hyi^  . .  "innerhalb  dieser  lin- der.." Bh./.8;  —  lör'fftf  -r''' didäm  frä- ^ayam(sd.)  Bh.2.13;  —  "n  sairi  (sd.) varjzüne  V.  75. 17;  —  'r>  daWiku  päpsr^ täiie  Yl.  JO.8,  -15-49;  49'j  —  yS  vlräzaiti *r3  raita  räsmana  Yt. /4'47;  —  nisaim (sd.)  yim  °r»  mSurumca  iäxoTmca  W.i.T,
4575:•  j.  'an'tara-  Adj.  'der  innere,  innen  be- findlich': 'r^m  ür^Mfii  nmanahe  "ins  Innere des  Hauses"  V.6'.43;  —  'rat  W.  2.^0 PüZ.  a)  'rat  naimax  'innerhalb',  mit folg.  1)  Gen.,  z)  Lok.,  3)  Instr.,  4)  Akk., uzw.  a)  räumlich,  b)  zeitlich:"  1  a)  a'  n- hsirake  N.  Go;  104';  —  *a'  n°  *yujyastHs N.  -ji  T'*j  —  a'  W  aEi3.drajahyehe  N. Ii()',  —  a'  n°  '^rigämyt/ie  N. 65.  1  b)  a- II'  tiava.xsaparahe  V.  5. 43.  !  a)  a'  11° barj''irisi'a  y.^.^i.  3  a)  a'  n'  brrat.- byqm  V.  Ä41,  42,  g.  15,  16.  4  a)  a' tr  aSe  pa>a  "auf  diesen  Wegen"  V.  8. 104.  4b)  a°  11°  triilzär.ljaAlm'V.^.^y, —  a-  n' yanJräßV.O.a,  3,  7.77.  Tai fialinät  N.^.^3).  Ta  N.JOi(?);  —  'nm N.pj(?).
```


## [2026-09-04T23:16:29.082Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; ls | tail -3; head -c 600 ../web_index.json 2>/dev/null || ls ..; echo; grep -o '\"url\": \"[^\"]*\"' ../*.json 2>/dev/null | tail -12"
}
```


### [2026-09-04T23:16:30.840Z] TOOL RESULT

```
ff4e32f6c24b44f6.txt
ffd3321bd18bd33d.txt
index.jsonl
MISSING_REFERENCES.md
refs
refs_online.json
SOURCE_MATRIX.md
web

"url": "https://archive.org/details/handbuchderalti00bartgoog"
"url": "https://archive.org/details/studienzuraltin00lidgoog"
"url": "https://archive.org/details/BaileyH.W.ZoroastrianProblemsInTheNinthCenturyBooksk"
"url": "https://archive.org/details/anchoratlasofwor00kind"
"url": "https://archive.org/details/familiesofwords00inpeim"
"url": "https://archive.org/details/duchesne-guillemin-studies"
"url": "https://archive.org/details/w.-b.-henning-selected-papers"
"url": "https://archive.org/details/bibliography-of-important-studies-on-old-iranian-subjects"
"url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)"
"url": "https://archive.org/details/akkadischefremdw00zimmuoft"
"url": "https://archive.org/details/in.ernet.dli.2015.24303"
"url": ""
```


## [2026-09-04T23:16:33.336Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; tail -9 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('url'))\n\""
}
```


### [2026-09-04T23:16:35.130Z] TOOL RESULT

```
https://www.etymonline.com/word/argent
https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%A7%D8%B3%D8%AA%D9%86
https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%BF%CF%81%CF%80%CE%AF%CE%BF%CF%82
https://en.wiktionary.org/wiki/%D8%B9%D9%82%D8%B1%D8%A8
https://www.etymonline.com/word/scorpion
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-
https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AF%DB%8C%D8%A8%D9%87%D8%B4%D8%AA
https://en.wiktionary.org/wiki/%D9%86%D8%B1%D8%AF
https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D8%AF
```


## [2026-09-04T23:16:39.900Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; python3 - <<'EOF'\nimport json\nwant=['borage','h%E2%82%82er%C7%B5','argue','argent','indoeurop','%D8%B9%D8%B1%D9%82','%D8%A7%D8%B1%D8%B2%DB%8C%D8%B2','ahdictionary']\nfor l in open('index.jsonl'):\n    d=json.loads(l); u=d.get('url','')\n    if any(w in u for w in want): print(u)\nEOF"
}
```


### [2026-09-04T23:16:41.771Z] TOOL RESULT

```
https://ahdictionary.com/word/semitic.html
https://ahdictionary.com/word/search.html?q=cherub
https://ahdictionary.com/word/search.html?q=griffin
https://ahdictionary.com/word/search.html?q=emerald
https://www.ahdictionary.com/word/search.html?q=liberty
https://ahdictionary.com/word/indoeurop.html
https://ahdictionary.com/word/search.html?q=paradise
https://ahdictionary.com/word/search.html?q=matte
https://ahdictionary.com/word/search.html?q=checkmate
https://ahdictionary.com/word/search.html?q=margarite
https://ahdictionary.com/word/search.html?q=matador
https://ahdictionary.com/word/search.html?q=mat
https://ahdictionary.com/word/search.html?q=smaragdite
https://en.wiktionary.org/wiki/borage
https://www.etymonline.com/word/borage
https://ahdictionary.com/word/search.html?q=borage
https://www.ahdictionary.com/word/search.html?q=borage
https://www.ahdictionary.com/word/search.html?q=gibbon
https://www.ahdictionary.com/word/search.html?q=bazaar
https://www.ahdictionary.com/word/indoeurop.html
https://ahdictionary.com/word/search.html?q=admiral
https://www.ahdictionary.com/word/search.html?q=balas
https://www.etymonline.com/word/argue
https://www.ahdictionary.com/word/search.html?q=tariff
https://www.etymonline.com/word/argent
```


## [2026-09-04T23:16:46.260Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; python3 - <<'EOF'\nimport json\nfor l in open('index.jsonl'):\n    d=json.loads(l); u=d.get('url','')\n    if 'ارزیز' in u or 'عرق' in u or 'erǵ' in u or 'h₂' in u: print(repr(u), d.get('path') or d.get('file'))\nEOF"
}
```


### [2026-09-04T23:16:48.387Z] TOOL RESULT

```
'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ep-' data/verification/sources/web/2ad2207866f2073f.txt
'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂eǵ-' data/verification/sources/web/c66eb6fbbf324c5e.txt
'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂lek-' data/verification/sources/web/430e42a1f689a61f.txt
'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂elgʷʰ-' data/verification/sources/web/0180d09c6db6728a.txt
'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂enǵʰ-' data/verification/sources/web/ee3da74eac73c282.txt
'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂éngʷʰis' data/verification/sources/web/a48283df89e37d9e.txt
'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂enk-' data/verification/sources/web/9226fe598862fa48.txt
'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂erǵ-' data/verification/sources/web/12871297dbd7fd73.txt
'https://en.wiktionary.org/wiki/ارزیز' data/verification/sources/web/0013bab04a208776.txt
'https://en.wiktionary.org/wiki/عرق' data/verification/sources/web/b4ec0026f93755ac.txt
```


## [2026-09-04T23:23:54.924Z] TOOL CALL #60: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-64.json << 'JSONEOF'\n{\n  \"pdf_page\": 64,\n  \"book_page\": 34,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Arg\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂erǵ- 'white, shining', with the *-n̥t- derivative *h₂erǵ-n̥t-om 'the shining/white metal, silver'\",\n      \"note\": \"Pokorny p.64 heads the entry 'ar(e)-g- (arg-?), r̥gi-, erweitert r̥g-ro-, argu- «glänzend, weißlich»' and lists there Av. ərəzata-, OP ardata- 'Silber', Lat. argentum, Gk. árguros; Watkins in the AHD Indo-European appendix defines the root as 'arg-. To shine; white; the shining or white metal, silver. […] [Pok. ar(e)g- 64.]' — which is verbatim Nourai's gloss 'to shine, white metal'. Language label ('Indo-European'), gloss and the POK:64 page reference are all correct; the only modernisation is that the root is now written with the initial laryngeal, *h₂erǵ-. Cross-cutting caveats for the chart: (a) Ernout-Meillet warn that the branch words for 'silver' (Lat. argentum, Osc. aragetud, Gaul. arganto-, Arm. arcatʿ, Av. ərəzatəm, Skt. rajatám) diverge too much to reconstruct one inherited noun — they are parallel derivatives of one root, which is how Nourai draws them; (b) the arzīz / ʾrcyc 'tin' branch (#2, #3, #5) is only a possible, not a proven, member of this family, and Horn — Nourai's own reference for it — denies it.\",\n      \"note_fa\": \"ریشهٔ بازسازی‌شدهٔ هندواروپایی آغازین *h₂erǵ- به معنی «سپید، درخشان» و از همین‌رو «فلز درخشان/سپید، یعنی نقره» است. پوکورنی در صفحهٔ ۶۴ آن را با همین معنا («glänzand, weißlich») می‌آورد و در ذیل آن اوستایی ərəzata-، پارسی باستان ardata- «نقره» و لاتین argentum را می‌شمارد؛ واتکینز نیز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage آن را «to shine; white; the shining or white metal, silver» تعریف کرده است — یعنی همان معنایی که نورایی نوشته. بنابراین برچسب زبانی، معنا و ارجاع POK:64 هر سه درست است؛ تنها تفاوت با پژوهش امروزی این است که این ریشه اکنون با حنجریِ آغازین *h₂erǵ- نوشته می‌شود. تنها بخش سست این نمودار شاخهٔ «ارزیز» است که در جای خود توضیح داده شده.\"\n      ,\n      \"ref_check\": [\n        {\"ref\": \"POK:64\", \"status\": \"supports\", \"note\": \"POK_01.txt \\\\f-leaf 72 (printed p. 64): 'ar(e)-g- (arg-?), r̥gi-, erweitert r̥g-ro-, argu- «glänzend, weißlich». Ai. árjuna-h «licht, weiß»; rajatá- «weißlich» … gegenüber av. ərəzata- n., apers. ardata- «Silber» (!), lat. argentum, osk. aragetud «argento» …' — root, language, gloss and page all as Nourai gives them.\"}\n      ],\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂erǵ-\",\n        \"https://www.etymonline.com/word/argent\",\n        \"https://ahdictionary.com/word/indoeurop.html\"\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"erezata\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan ərəzata- (neuter) 'silver' continues the PIE *-n̥t-o- derivative *h₂erǵ-n̥t-om: the palatal *ǵ becomes Indo-Iranian *ȷ́ and then Avestan z (so -rz- against Latin -rg-), and syllabic *n̥ shows up as -a-, giving Proto-Iranian *arȷ́ata- > ərəzata- (with the usual Avestan anaptyctic ə before r). It is attested in the Yašts (Yt. 5.129 ərəzatəm 'silver' beside zaranaēnəm 'golden') and in the compounds ərəzatō.fraēšna- 'whose front is of silver' and ərəzatō.saēpa-. Its exact cognates are Skt. rajatá-, OP ardata-, Armenian arcatʿ (an Iranian loanword), Latin argentum, Greek árguros. Nourai's transliteration 'erezata' is the standard pre-1970s rendering of ərəzata-, and his gloss 'white metal' is Watkins's own phrasing for the root; Bartholomae simply glosses it 'Silber'.\",\n          \"derivation_fa\": \"واژهٔ اوستایی ərəzata- (خنثی) به معنی «سیم، نقره» دنبالهٔ مستقیم ساخت *h₂erǵ-n̥t-om هندواروپایی است: کامیِ *ǵ در ایرانی باستان به *ȷ́ و سپس در اوستایی به «ز» بدل شده (از این‌رو -rz- در برابر -rg- لاتین)، و *n̥ هجایی به «a» تبدیل شده؛ حاصل *arȷ́ata- ایرانی باستان است که در اوستایی با واکهٔ میانجی ə پیش از r به ərəzata- رسیده. این واژه در یشت‌ها (یشت ۵ بند ۱۲۹) و در ترکیب‌هایی چون ərəzatō.fraēšna- آمده است. هم‌ریشه‌های دقیق آن سنسکریت rajatá-، پارسی باستان ardata-، ارمنی arcatʿ (وام‌واژهٔ ایرانی) و لاتین argentum است. آوانویسی «erezata» در کتاب همان شیوهٔ کهنِ نگارش ərəzata- است و معنای «فلز سپید» برگرفته از تعریف واتکینز برای خودِ ریشه است؛ بارتولومه آن را ساده «Silber» معنی می‌کند. ادعای نورایی در این گره درست است.\",\n          \"ref_check\": [\n            {\"ref\": \"POK:64\", \"status\": \"supports\", \"note\": \"POK_01.txt \\\\f-leaf 72 (p.64): '… gegenüber av. ərəzata- n., apers. ardata- «Silber» (!), lat. argentum …' — the Avestan word is placed directly under the root, exactly as the chart draws it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 351/352 s.v. ərəzata-\", \"stance\": \"supports\", \"note\": \"BRT.txt \\\\f-leaf 222: 'j. ərəzata- n. «Silber»: carəma (sd.) … Yt.5.129 … KompA.; Ableit. — Vgl. ai. rajatá- n.; arm. arcatʿ. — Pü.: asīm.' Note that Bartholomae's Pahlavi equivalent is asēm, NOT arzīz — relevant to node #2.\"},\n            {\"src\": \"SYN\", \"where\": \"9.65 SILVER\", \"stance\": \"supports\", \"note\": \"SYN.txt: 'Skt. rajata-, Av. arazata-, OPers. ardata- (Dar. Sus. f. 40), all neuter; Arm. arcatʿ' under '1. Derivs. of IE *arg- in words for «bright, white» … Walde-P. 1,82f.'\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed. p.104/105 s.v. argent\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *arg-, «to shine», whence also OI. r̥jráh …, rajatam, Avestic ərəzata, «silver» …'\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. arĝntom\", \"stance\": \"supports\", \"note\": \"Mann: 'arĝntom «white metal, silver». WP I, 82. Cf. arĝos. Skt. rajatám; … Av. ərəzatəm; OPer. ardata-; Oss. ärzät «metal, ore»; cf. Per. arzīz «tin» …'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. arg-\", \"stance\": \"supports\", \"note\": \"'arg-. To shine; white; the shining or white metal, silver. […] [Pok. ar(e)g- 64.]'\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/argent\", \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂erǵ-\"]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"arzyz\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Middle Persian word is real: MacKenzie's Concise Pahlavi Dictionary p.13 has 'arzīz [ʾlcyc | M ʾrzyz, N ~] tin, lead' with the derivative arzīzēn 'of tin, leaden'. But it is NOT the phonetic descendant of Av. ərəzata- that the arrow claims. The Middle Persian continuation of the inherited word for 'silver' is asēm (that is precisely the Pahlavi gloss Bartholomae prints under ərəzata-), and Old Iranian *arzata- would have yielded MP *arzād / *ardād, not arzīz with its -īz. What the sources actually support is a sister formation from the same root: an Old Iranian *arzi- / *arzi-ča- 'the shining (metal)', to which Ossetic ærzæt 'ore, metal' also belongs. Wiktionary, following Rastorgueva & Edelman's Etimologičeskij slovarʹ iranskix jazykov, says arzīz is 'from Middle Persian ʾlcyc (arzīz «tin, lead»), perhaps ultimately from Proto-Iranian *arjata- «silver»', cognate with (not descended from) Av. ərəzata-; Mann lists 'Per. arzīz «tin»' under *arĝntom. Horn — the reference Nourai cites on the very next node — rejects the derivation from ərəzata- outright. So: right family, wrong arrow; a parallel *arzi-derivative, not a child of the Avestan noun.\",\n          \"derivation_fa\": \"واژهٔ فارسی میانه واقعی است: مکنزی در فرهنگ کوچک پهلوی (ص ۱۳) می‌آورد «arzīz [ʾlcyc | مانوی ʾrzyz] قلع، سرب» با صفتِ arzīzēn «ارزیزین». اما این واژه دنبالهٔ آوایی ərəzata- اوستایی نیست، چنان‌که پیکان نمودار ادعا می‌کند: بازماندهٔ فارسی میانهٔ واژهٔ موروثی «نقره» asēm است (بارتولومه خود در ذیل ərəzata- می‌نویسد «Pü.: asīm»)، و *arzata- ایرانی باستان در پهلوی باید *arzād می‌شد، نه arzīz با آن «ای» کشیده. آنچه منابع تأیید می‌کنند ساختی خواهرـگونه از همان ریشه است: ایرانی باستان *arzi-/*arzi-ča- «فلز درخشان» که آسی ærzæt «سنگ معدن» نیز از آن است. ویکی‌واژه به پیروی از فرهنگ ریشه‌شناختی زبان‌های ایرانی راستارگویوا و ادلمان می‌گوید ارزیز «شاید سرانجام از ایرانی آغازین *arjata- «نقره»» باشد و آن را هم‌ریشهٔ ərəzata- (نه بازماندهٔ آن) می‌داند؛ مان نیز «فارسی arzīz» را ذیل *arĝntom آورده است. پس: خانوادهٔ درست، پیکان نادرست؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"ref_check\": [\n            {\"ref\": \"SOD:56\", \"status\": \"partial\", \"note\": \"Gharib, Sogdian Dictionary, entry no. 1420 (SOD_pages.txt \\\\f-leaf 121, printed p. 55/56): 'ʾrcyc M … arzīz ©MP ʾrzyz; Arm. arjij … tin, lead'. The page does confirm a Middle Persian ʾrzyz beside the Sogdian word, so the citation is genuine, but Gharib offers no Avestan/Indo-European etymology at all — nothing on the page supports the drawn edge ərəzata- → arzīz. (It is also an odd reference for a Pahlavi node: SOD is a Sogdian dictionary.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p.13 s.v. arziz\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'arziz [ʾlcyc | M ʾrzyz, N ~] tin, lead. ~ēn [-yn'] tin, leaden.'; English index p.126 'tin arziz', p.? 'lead (n.) arziz, srub' — the word and both meanings confirmed.\"},\n            {\"src\": \"HRN\", \"where\": \"p.17 no. 68 (HRN.txt \\\\f-leaf 38)\", \"stance\": \"contradicts\", \"note\": \"Horn: '68. erzīz «Blei». arm. arcic. Geldner's Gleichstellung mit aw. arezazi- (Yt. 13,45, KZ. 25,558) ist lautlich unmöglich; ebenso die Ableitung von aw. erezata-, skr. rajatá-. Die Heimat des Wortes ist noch durchaus unbekannt.' — an explicit rejection of exactly this arrow.\"},\n            {\"src\": \"HUB\", \"where\": \"p.12, note to Horn no. 68\", \"stance\": \"partial\", \"note\": \"Hübschmann: 'Np. arzīz heisst auch «Zinn» … der eigentliche Name für «Blei» ist surb. Ursprünglich gilt arzīz für beide Metalle, indem man zwischen weissem arzīz = «Zinn» und schwarzem arzīz = «Blei» unterschied. … Im Pehlevi musste das Wort *arcīc lauten.' Corrects Horn's gloss but endorses no Avestan etymology.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. arĝntom\", \"stance\": \"supports\", \"note\": \"Mann puts 'cf. Per. arzīz «tin»' in the same entry as Av. ərəzatəm, OPer. ardata-, Oss. ärzät — i.e. he does connect the word with the root, though only with 'cf.'\"},\n            {\"src\": \"ARY\", \"where\": \"printed p.80 (ARY_pages.txt pdf page 79)\", \"stance\": \"supports\", \"note\": \"Aryanpur's Persian dictionary of Indo-European roots gives the entry 'فارسی: ارزیز (به چم قلع، فلز سپید و نقره‌فام)' with 'هند و اروپایی: ARĜ-, *ARĜENT-; اوستایی: ƏRƏZATA-; پارسی باستان: ARDATA-; پهلوی: ARZĪZ' — a modern Persian source that does file arzīz under this root.\"},\n            {\"src\": \"NYB\", \"where\": \"Part II glossary\", \"stance\": \"silent\", \"note\": \"grep for 'arziz', 'lcyc', 'Zinn' in NYB_vol2_glossary.txt returns nothing; Nyberg's Pahlavi glossary does not carry the word.\"}\n          ],\n          \"sources\": [\"https://en.wiktionary.org/wiki/ارزیز\"]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"arzîz «ارزیز»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The Pahlavi → New Persian step itself is straightforward and certain: MP arzīz (Book Pahlavi ʾlcyc, Manichaean ʾrzyz) passes unchanged into New Persian ارزیز arzīz 'tin', the Book-Pahlavi spelling merely reflecting the script's l/r and c/z ambiguities. The word is well attested in classical Persian: Asadi Tusi's Loghat-e Fors quotes ʿOnṣorī ('ālat-e rōyīna o mesīna bovad, o arzīz…'), and it is in the Shahnameh ('biyāvard arzīz o rōyīn…', Nūshīn's Vāzhanāmak). Middle Armenian arčič 'lead' is a borrowing from the Iranian word, and Arabic رصاص raṣāṣ 'lead' is usually taken from the same source. Hübschmann notes that arzīz originally covered both metals — white arzīz = tin, black arzīz = lead — so Nourai's 'tin' is the narrower later sense, and MacKenzie's 'tin, lead' is the fuller one. What is wrong here is the citation, not the step: Horn p.17 (no. 68), the page Nourai cites, glosses the word 'Blei' and expressly denies any connection with Av. ərəzata- or Skt. rajatá-.\",\n          \"derivation_fa\": \"پلهٔ پهلوی ← فارسی نو در این زنجیره قطعی است: فارسی میانهٔ arzīz (به خط پهلوی کتابی ʾlcyc، به خط مانوی ʾrzyz) بی هیچ دگرگونی به فارسی نو «ارزیز» رسیده است؛ نگارش پهلوی تنها بازتاب ابهام حروف l/r و c/z در آن خط است. این واژه در فارسی دری کهن به‌خوبی گواه دارد: اسدی طوسی در لغت فرس بیتی از عنصری می‌آورد («آلت رویینه و مسینه بود و ارزیزی…») و در شاهنامه نیز آمده است («بیاورد ارزیز و رویین…»). ارمنی میانهٔ arčič «سرب» وام‌گرفته از همین واژهٔ ایرانی است و رَصاص عربی را نیز معمولاً از همین ریشه می‌دانند. هوبشمان یادآور می‌شود که ارزیز در آغاز هر دو فلز را دربر می‌گرفت — ارزیز سپید = قلع، ارزیز سیاه = سرب — پس معنای «قلع» که نورایی داده معنای متأخر و باریک‌تر است. اشکال این گره در ارجاع است نه در خودِ پله: هرن در همان صفحهٔ ۱۷ که نورایی به آن ارجاع می‌دهد، واژه را «سرب» معنی می‌کند و پیوند آن را با ərəzata- اوستایی صریحاً رد می‌کند.\",\n          \"ref_check\": [\n            {\"ref\": \"HRN:17\", \"status\": \"contradicts\", \"note\": \"HRN.txt \\\\f-leaf 38 (printed p.17), entry 68: 'erzīz «Blei». arm. arcic. Geldner's Gleichstellung mit aw. arezazi- … ist lautlich unmöglich; ebenso die Ableitung von aw. erezata-, skr. rajatá-. Die Heimat des Wortes ist noch durchaus unbekannt.' The cited page contains the word (so the page number is right) but says the opposite of what the chart draws, and glosses it 'lead' rather than 'tin'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"p.12 (note on Horn 68)\", \"stance\": \"partial\", \"note\": \"'Np. arzīz heisst auch «Zinn» … Ursprünglich gilt arzīz für beide Metalle … Im Pehlevi musste das Wort *arcīc lauten.' — supports the gloss 'tin' but not the Avestan derivation.\"},\n            {\"src\": \"FRS\", \"where\": \"Loghat-e Fors, s.v. (FRS_pages.txt l.6662, 6686, 6697)\", \"stance\": \"supports\", \"note\": \"Asadi Tusi attests the classical word: 'آلت رویینه و مسینه بود و ارزیزی … عنصری' and 'به ارزیز بندند و دوشانند' — the New Persian headword is genuine and old.\"},\n            {\"src\": \"FSF\", \"where\": \"Vāzhanāmak (Shahnameh glossary), l.14767 / 20201\", \"stance\": \"supports\", \"note\": \"'بیاورد ارزیز و رویین' — the word is Ferdowsian, i.e. inherited rather than a late borrowing.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. ارزیز\", \"stance\": \"supports\", \"note\": \"MON_part1.txt l.9925: 'ارزیز: … (شیم.) فلزی است سفید…' — Mo'in has the headword and glosses it as a white metal (tin); no origin tag such as [ع.] is attached, i.e. he treats it as native Persian.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ vol.1\", \"stance\": \"silent\", \"note\": \"grep of BQT_v1_pages.txt / BQT_alt_v1.txt finds only an incidental use ('در هاون ارزیز', s.v. باقلی); the alef-section headword is not recoverable from this OCR, so Mo'in's etymological footnote could not be read.\"},\n            {\"src\": \"ARY\", \"where\": \"printed p.80\", \"stance\": \"supports\", \"note\": \"Aryanpur files 'ارزیز (به چم قلع)' under Indo-European ARĜ- with Avestan ƏRƏZATA- and Pahlavi ARZĪZ.\"}\n          ],\n          \"sources\": [\"https://en.wiktionary.org/wiki/ارزیز\"]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old Persian\",\n          \"words\": \"arda-; ardata; arda-stâna\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Of the three forms only one is securely attested. (1) ardata- 'silver' is real, occurring in Darius's Susa foundation charter (DSf 40) and matching Av. ərəzata-, Skt. rajatá- exactly; the Old Persian outcome of Indo-Iranian *ȷ́ before a stop is d (cf. OP adam vs Av. azəm), hence -rd- against Avestan -rz-. Buck files it under IE *arg- 'bright, white', Pokorny prints 'apers. ardata- «Silber»' on p.64. (2) arda- 'light' is not independently attested in Old Persian: Kent extracts it from the compound, writing 'ardastāna- sb. «window-frame, window cornice»: arda- «light» as in OP ardata- «silver», Skt. rajatá- «white», r̥jrá- «red», Gk. argós «shining» + stāna- «place» … «light-place»'. (3) ardastāna- itself IS attested — in DPc, the one-line trilingual repeated on the window cornices of Darius's palace at Persepolis ('stone window-frame, made in the house of King Darius'), with Elamite har-da-iš-da-na. But Kent's 'light-place' reading, which he takes from Foy (KZ 35.48) and which Nourai reproduces as '(light stand), window frame', is only one of two: Bartholomae (AiW 193) and Tolman analyse the first element as Av. arəδa- 'half, side'. So the node's core (ardata-) is confirmed, its supporting analysis (arda- 'light', ardastāna- = 'light-place') is one scholar's reading against another's.\",\n          \"derivation_fa\": \"از سه صورت این گره تنها یکی گواه استوار دارد. نخست، ardata- «نقره» واژه‌ای واقعی از پارسی باستان است که در سنگ‌نبشتهٔ بنیاد شوش داریوش (DSf بند ۴۰) آمده و برابر دقیق ərəzata- اوستایی و rajatá- سنسکریت است؛ *ȷ́ هندوایرانی در پارسی باستان پیش از همخوان به «د» بدل می‌شود (سنجید با adam پارسی باستان در برابر azəm اوستایی)، و از این‌رو -rd- در برابر -rz- اوستایی. دوم، arda- «روشن» به‌تنهایی در پارسی باستان گواهی ندارد؛ کنت آن را از دل همان ترکیب بیرون کشیده است. سوم، ardastāna- خود گواه دارد: در کتیبهٔ DPc که بر چارچوب‌های سنگی پنجرهٔ کاخ داریوش در تخت‌جمشید تکرار شده («چارچوب پنجرهٔ سنگی، ساختهٔ خانهٔ داریوش شاه»)، با برابر ایلامی har-da-iš-da-na. اما تحلیل کنت («جای روشنایی»، به پیروی از فوی) تنها یکی از دو خوانش است: بارتولومه (فرهنگ ایرانی باستان، ستون ۱۹۳) و تولمن جزء نخست را arəδa- اوستایی به معنی «نیم، سو» می‌گیرند. پس هستهٔ گره درست است و تحلیل پشتیبان آن محل اختلاف.\",\n          \"ref_check\": [\n            {\"ref\": \"KNT:171\", \"status\": \"supports\", \"note\": \"KNT.txt \\\\f-leaf 193, with the page numeral '171' printed immediately below the entry: 'ardastāna- sb. «window-frame, window cornice»: arda- «light» as in OP ardata- «silver», Skt. rajatá- «white», r̥jrá- «red», Gk. argós «shining» + stāna- «place» (§31, §160.Ib; Foy, KZ 35.48; hardly as with Bthl. AiW 193, or Hz. ApI 74-6); «light-place». ardastāna nsm. DPc.' — Nourai's three words and his gloss '(light stand), window frame ☞Stâ' are a direct transcript of this entry, page number included.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon s.v. ardastāna\", \"stance\": \"partial\", \"note\": \"'ardastāna, m. window-cornice (?). Nom. sg. ardastāna, Dar. Pers. C. … *arda, half. YAv. arəδa + stāna … cf. Bartholomae, Altiran. Wb., 193. Foy, KZ, 35, 48, connects the first member of the compound with Av. arəzō, bright, Skt. r̥jra.' — Tolman prefers 'half', relegating Kent's/Foy's 'bright' to a note.\"},\n            {\"src\": \"POK\", \"where\": \"p.64\", \"stance\": \"supports\", \"note\": \"'apers. ardata- «Silber» (!)' listed beside av. ərəzata- directly under the root — supports the second word of the node.\"},\n            {\"src\": \"SYN\", \"where\": \"9.65 SILVER\", \"stance\": \"supports\", \"note\": \"'OPers. ardata- (Dar. Sus. f. 40)' with the exact attestation, filed under 'Derivs. of IE *arg-'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. arĝos / arĝntom\", \"stance\": \"supports\", \"note\": \"Mann lists 'OPer. arad-' under arĝos 'silvery, white, clear' and 'OPer. ardata-' under arĝntom — i.e. he too posits an Old Persian 'bright' stem.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW col. 193 (via Tolman's citation)\", \"stance\": \"contradicts\", \"note\": \"Bartholomae's alternative — first element = Av. arəδa- 'half, side' — is the reading Kent explicitly rejects ('hardly as with Bthl. AiW 193'); the OCR of BRT.txt does not render this column legibly, so it is cited here at second hand through Tolman.\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/argent\"]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Sogdian\",\n          \"words\": \"`rcyc\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Sogdian ʾrcyc 'tin, lead' is genuine and well attested — Gharib's Sogdian-Persian-English Dictionary no. 1420 gives 'ʾrcyc M … arzīz ©MP ʾrzyz; Arm. arjij … tin, lead', citing the Manichaean texts (TSP 6, 15, 74, 152) and Sogdica 27.30. But it is not an independent branch off the root, as the chart's arrow from the root box implies: it is the very same Old Iranian *arzi-ča- formation as MP arzīz of node #2 (Sogdian writes c where Book Pahlavi's ambiguous letter is read z), so the two nodes are one word, and the eastern-Iranian form is if anything the better-preserved shape (Hübschmann in fact predicted a Pahlavi *arcīc). Gharib gives no Indo-European etymology at all; the tie to *h₂erǵ- rests on the same 'perhaps ultimately from Proto-Iranian *arjata-' that ESIJa attaches to arzīz, plus Ossetic ærzæt 'ore'. Hence plausible rather than confirmed.\",\n          \"derivation_fa\": \"واژهٔ سغدی ʾrcyc «قلع، سرب» اصیل و پرگواه است: بدرالزمان قریب در فرهنگ سغدی (شمارهٔ ۱۴۲۰) می‌آورد «ʾrcyc … arzīz، فارسی میانه ʾrzyz؛ ارمنی arjij؛ قلع، سرب» و به متن‌های مانوی ارجاع می‌دهد. اما این واژه شاخهٔ جداگانه‌ای از ریشه نیست، چنان‌که پیکانِ نمودار از خودِ ریشه به آن می‌رسد؛ همان ساخت *arzi-ča- ایرانی باستان است که در گرهٔ ۲ به‌صورت arzīz فارسی میانه آمده — سغدی «c» می‌نویسد آنجا که خط پهلوی حرفی مبهم دارد که «ز» خوانده می‌شود. پس این دو گره در حقیقت یک واژه‌اند، و صورت ایرانی خاوری اگر نگوییم اصیل‌تر، دست‌کم کهن‌نماتر است (هوبشمان خود پیش‌بینی کرده بود که شکل پهلوی باید *arcīc می‌بود). قریب هیچ ریشه‌شناسی هندواروپایی نمی‌دهد؛ پیوند با *h₂erǵ- بر همان «شاید» متکی است که فرهنگ ریشه‌شناختی زبان‌های ایرانی دربارهٔ ارزیز می‌گوید. از این‌رو: با احتیاط پذیرفتنی.\",\n          \"ref_check\": [\n            {\"ref\": \"SOD:56\", \"status\": \"supports\", \"note\": \"SOD_pages.txt \\\\f-leaf 121 (printed p. 55/56, the two-column layout makes the last digit uncertain), entry 1420: 'ʾrcyc M … arziz ©MP ʾrzyz; Arm. arjij … tin, lead … TSP 6,15,74,152 & etc.' — the Sogdian word, the gloss and the Middle Persian comparison are exactly as Nourai reports; the page reference is right (or off by one). No Indo-European etymology on the page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p.13 s.v. arziz\", \"stance\": \"supports\", \"note\": \"MacKenzie's Book-Pahlavi spelling 'ʾlcyc' is graphically the same word as Sogdian ʾrcyc, confirming that #2 and #5 are one lexeme, not two branches.\"},\n            {\"src\": \"HUB\", \"where\": \"p.12\", \"stance\": \"supports\", \"note\": \"'Im Pehlevi musste das Wort *arcīc lauten' — Hübschmann's predicted Middle Iranian shape is precisely the Sogdian form.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. arĝntom\", \"stance\": \"partial\", \"note\": \"Mann connects the Persian word ('cf. Per. arzīz «tin»') with the root but lists no Sogdian form.\"},\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka\", \"stance\": \"silent\", \"note\": \"grep for 'arziz'/'arcic' in ISS_alt_DKS.txt returns nothing; Khotanese offers no comparandum here.\"}\n          ],\n          \"sources\": [\"https://en.wiktionary.org/wiki/ارزیز\"]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Latin\",\n          \"words\": \"argentum\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin argentum 'silver' is the Italic member of the same *-nt- derivative *h₂erǵ-n̥t-om, with syllabic *n̥ > Latin -en- and palatal *ǵ > g; like every Latin metal name (aurum, ferrum, plumbum) it is neuter. Its immediate relatives are Oscan aragetud (abl.), Gaulish arganto- (Arganto-magus 'silver field'), Old Irish argat, Welsh arian, Armenian arcatʿ. Ernout-Meillet caution that these branch forms 'diffèrent plus encore' and that no single Indo-European noun can be restored — they are parallel derivatives, each language naming silver as the 'bright' metal — which is exactly the shape of Nourai's chart, where Latin hangs off the root and not off the Iranian words. Both of Nourai's citations are apposite: Klein s.v. argent and Watkins s.v. arg- ('Suffixed form *arg-ent- in Latin argentum, silver: ARGENT, ARGENTINE').\",\n          \"derivation_fa\": \"لاتین argentum «نقره» عضو ایتالیک همان ساخت *h₂erǵ-n̥t-om است: *n̥ هجایی در لاتین به -en- و کامیِ *ǵ به g بدل شده؛ و مانند همهٔ نام‌های فلز در لاتین (aurum، ferrum) خنثی است. خویشاوندان نزدیک آن اسکی aragetud، گُلی arganto-، ایرلندی کهن argat، ولزی arian و ارمنی arcatʿ هستند. ارنو و مِیه هشدار می‌دهند که این صورت‌های شاخه‌ای چندان از هم دورند که نمی‌توان یک اسمِ واحد هندواروپایی بازسازی کرد؛ هر زبان جداگانه نقره را «فلز درخشان» نامیده است — و این دقیقاً همان ساختاری است که نمودار نورایی نشان می‌دهد، یعنی لاتین مستقیماً از ریشه و نه از صورت‌های ایرانی. هر دو ارجاع نورایی (کلاین و واتکینز) درست‌اند. ادعای نورایی در این گره درست است.\",\n          \"ref_check\": [\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt \\\\f-leaf 66 (pp.104/105) s.v. argent: 'F., fr. L. argentum, «silver», which is cogn. with Gk. árguros, «silver», prop. «the white (metal)», fr. argós … fr. I.-E. base *arg-, «to shine» …'\"},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. arg-: '1. Suffixed form *arg-ent- in Latin argentum, silver: ARGENT, ARGENTINE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. argentum\", \"stance\": \"supports\", \"note\": \"'argentum est l'un des noms, tirés d'une même racine, par lesquels est désigné l'argent … Arm. arcatʿ «argent», tokh. A ārkyant, av. ərəzatəm et skr. rajatám diffèrent plus encore … On entrevoit donc ici une même manière, déjà indo-européenne, de désigner l'«argent» comme métal «brillant» … mais on ne peut restituer un nom indo-européen.'\"},\n            {\"src\": \"POK\", \"where\": \"p.64\", \"stance\": \"supports\", \"note\": \"'lat. argentum, osk. aragetud «argento», air. argat, mir. airget, cymr. arian(t) … «Silber»' listed under the root.\"},\n            {\"src\": \"SYN\", \"where\": \"9.65 SILVER\", \"stance\": \"supports\", \"note\": \"'Grk. árguros; Lat. argentum (> It. argento, Fr. argent, Rum. argint), Osc. abl. sg. aragetud; Gall. arganto- in Arganto-marus … all neuter.'\"},\n            {\"src\": \"LEW\", \"where\": \"Walde 1910 s.v. argentum\", \"stance\": \"silent\", \"note\": \"grep for 'argentum' in LEW_1910.txt returns no hit — the headword is not recoverable from this OCR.\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/argent\", \"https://ahdictionary.com/word/indoeurop.html\"]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"argent, Argentina\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"argent entered English about 1400 from Old French argent 'silver, silver money' < Latin argentum, first in heraldry (the white/silver tincture) and for silver coin; it is a learned/heraldic word, not an inherited one. Argentina is the same Latin word in Spanish dress: the Río de la Plata basin was 'the land of silver' to the 16th-century Spaniards, and Martín del Barco Centenera's poem La Argentina (Lisbon, 1602) fixed the adjective argentina 'silvery' (Latin argentum + -īnus) as the country's name, adopted officially in the 1826 constitution. Klein files both under argent, and Etymonline lists 'argent, Argentina, argentine' among the English descendants of *arg-; Watkins lists ARGENT, ARGENTINE. The node carries no reference in the book, but the chain Latin → Old French/Spanish → English is uncontroversial.\",\n          \"derivation_fa\": \"واژهٔ argent در حدود سال ۱۴۰۰ میلادی از فرانسهٔ کهن argent «نقره، پول نقره» و آن از لاتین argentum وارد انگلیسی شد، نخست در نشان‌شناسی (رنگ سیمین بر سپر) و برای سکهٔ نقره؛ یعنی وام‌واژه‌ای فرهیخته است نه واژه‌ای موروثی. «آرژانتین» همان واژهٔ لاتین در جامهٔ اسپانیایی است: حوضهٔ ریودولاپلاتا در سدهٔ شانزدهم نزد اسپانیایی‌ها «سرزمین نقره» بود و منظومهٔ La Argentina سرودهٔ مارتین دل بارکو سنتنرا (لیسبون، ۱۶۰۲) صفت argentina «سیمین» (از argentum لاتین + پسوند -īnus) را به‌عنوان نام کشور تثبیت کرد که در قانون اساسی ۱۸۲۶ رسمیت یافت. کلاین هر دو را ذیل argent می‌آورد و اتیمآنلاین نیز argent، Argentina و argentine را در شمار بازماندگان انگلیسی ریشهٔ *arg- می‌شمارد. ادعای نورایی درست است.\",\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book; the parent node's KLN and AHD citations cover it (Klein s.v. argent, Watkins s.v. arg- 'ARGENT, ARGENTINE').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed. pp.104/105 s.v. argent, argentine\", \"stance\": \"supports\", \"note\": \"'argent, n., silver (archaic). — F., fr. L. argentum'; 'argentine, adj., resembling silver. — L. argentīnus, «of silver», fr. argentum.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. arg-\", \"stance\": \"supports\", \"note\": \"'Suffixed form *arg-ent- in Latin argentum, silver: ARGENT, ARGENTINE.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"no separate 'argent' headword found in SKT.txt; Skeat treats the family only under 'argue'.\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/argent\"]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"arguere\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin arguō, arguere 'to make clear, make known, prove, demonstrate' belongs to the u-extension of the very same root, and Pokorny prints it on the continuation of the p.64 entry: 'Lat. argentum s. oben; arguō «mache klar, deutlich; helle einen Sachverhalt auf, überführe», argūtus «stimmkräftig, schwatzhaft; (seit Cicero auch:) strahlend, flimmernd» und «scharfsinnig»' (p.65). Ernout-Meillet and de Vaan treat it as a denominative to an adjective *argu- 'bright' — preserved in argūtus and matching the *arǵ-u- stem behind Greek árguros — so the semantic path is 'make bright' → 'make clear' → 'prove'. Klein states it flatly: arguere 'is rel. to argentum, «silver» (arguere orig. meant «to make as white as silver»)'. Nourai's gloss 'to clarify' is a fair short rendering of 'make clear'. The node carries no reference in the book; POK:64-65 and KLN s.v. argent cover it.\",\n          \"derivation_fa\": \"فعل لاتین arguō/arguere «روشن کردن، آشکار ساختن، اثبات کردن» به گسترشِ -u- همان ریشه تعلق دارد و پوکورنی آن را در دنبالهٔ همان مدخل صفحهٔ ۶۴ (یعنی صفحهٔ ۶۵) می‌آورد: «lat. argentum s. oben; arguō «mache klar, deutlich»، argūtus «… strahlend, flimmernd» und «scharfsinnig»». ارنو و مِیه و دِ فان آن را فعلی برساخته از صفت *argu- «درخشان» می‌دانند که در argūtus بازمانده و همان ستاک *arǵ-u- است که árguros یونانی نیز از آن است؛ پس مسیر معنایی چنین است: «درخشان کردن» ← «روشن کردن» ← «اثبات کردن». کلاین صریح می‌گوید که arguere با argentum خویشاوند است و در اصل یعنی «چون نقره سپید کردن». معادل «to clarify» که نورایی داده برگردان کوتاه و درستی از «make clear» است. ادعای نورایی درست است، هرچند این گره در کتاب بی‌ارجاع مانده.\",\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference is printed on this node; the claim is nevertheless covered by the root's own POK:64 citation, which continues onto p.65 with arguō (POK_01.txt \\\\f-leaf 74).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p.65 (POK_01.txt \\\\f-leaf 74)\", \"stance\": \"supports\", \"note\": \"'Lat. argentum s. oben; arguō «mache klar, deutlich; helle einen Sachverhalt auf, überführe», argūtus «stimmkräftig, schwatzhaft; (seit Cicero auch:) strahlend, flimmernd» und «scharfsinnig».'\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed. p.104 s.v. argue / argent\", \"stance\": \"supports\", \"note\": \"'L. argutare, freq. of arguere, «to make clear, prove», which is rel. to argentum, «silver» (arguere orig. meant «to make as white as silver»)'; and under argent: '… L. arguere, «to make clear, prove».'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. argentum (cross-ref to arguo)\", \"stance\": \"supports\", \"note\": \"'Quant à gr. árguros, c'est un dérivé du thème en -u- qui apparaît dans lat. arguō (v. ce mot).'\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. arĝos\", \"stance\": \"supports\", \"note\": \"Mann: 'Lat. cf. arguo, argutus' listed under arĝos 'silvery, white, clear' (WP I, 82).\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. arg-\", \"stance\": \"supports\", \"note\": \"'5. Extended form *argu-, brilliance, clarity, in Latin denominative arguere, to make clear, demonstrate: ARGUE.'\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/argue\", \"https://ahdictionary.com/word/indoeurop.html\"]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"argue\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English argue is first recorded c.1300 in the sense 'to make reasoned statements, to prove', borrowed from Old French arguer, which continues Latin argūtāre / argūtārī, the frequentative of arguere; the modern quarrelling sense ('dispute with someone') grows out of 'contend in debate' only in the later Middle English and early modern period. Klein: 'argue, intr. and tr. v. — ME. arguen, fr. OF. (=F.) arguer, fr. L. argutare, freq. of arguere, «to make clear, prove», which is rel. to argentum, «silver»'; Etymonline gives the same chain and traces arguere to 'a suffixed form of PIE root *arg- «to shine; white»', citing de Vaan's denominative *argu- 'bright'. Nourai's AHD citation is exact: Watkins lists ARGUE under the extended form *argu-.\",\n          \"derivation_fa\": \"فعل انگلیسی argue نخستین بار حدود سال ۱۳۰۰ به معنای «استدلال کردن، اثبات کردن» ثبت شده و وام‌گرفته از فرانسهٔ کهن arguer است که خود دنبالهٔ argūtāre لاتین، صورت تکراری (frequentative) فعل arguere، است؛ معنای امروزی «مشاجره کردن» تنها در انگلیسی میانهٔ متأخر و آغاز دورهٔ نو از دل «در بحث ستیزیدن» پدید آمده است. کلاین می‌نویسد: «argue … انگلیسی میانه arguen، از فرانسهٔ کهن arguer، از لاتین argutare، صورت تکراری arguere «روشن کردن، اثبات کردن» که با argentum «نقره» خویشاوند است». اتیمآنلاین همین زنجیره را می‌آورد و arguere را به «صورت پسوندداری از ریشهٔ هندواروپایی *arg- «درخشیدن؛ سپید»» بازمی‌گرداند. ارجاع نورایی به AHD دقیق است: واتکینز ARGUE را ذیل گسترشِ *argu- آورده. ادعای نورایی درست است.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. arg-: '5. Extended form *argu-, brilliance, clarity, in Latin denominative arguere, to make clear, demonstrate: ARGUE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed. p.104 s.v. argue\", \"stance\": \"supports\", \"note\": \"'argue, intr. and tr. v. — ME. arguen, fr. OF. (=F.) arguer, fr. L. argutare, freq. of arguere, «to make clear, prove», which is rel. to argentum, «silver» (arguere orig. meant «to make as white as silver»). See argent.'\"},\n            {\"src\": \"POK\", \"where\": \"p.65\", \"stance\": \"supports\", \"note\": \"arguō and argūtus are printed under the root, so the ultimate connection is Pokorny's too.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. ARGUE\", \"stance\": \"silent\", \"note\": \"the entry is not legible in this OCR of SKT.txt (grep on 'ARGUE' at line start finds no hit); Skeat's known text derives argue from OF arguer, L. argūtāre, in agreement with Klein.\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/argue\"]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"A.r.q, Araq\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic root ع ر ق ʿ-r-q; عَرِقَ ʿariqa 'to sweat', عَرَق ʿaraq 'sweat; sap/exudation, distilled spirit'\",\n      \"note\": \"The root, the language label and the gloss are all right. Arabic ʿariqa 'to perspire' with the verbal noun ʿaraq 'sweat' is standard Classical Arabic; the transferred senses run 'sweat' → 'the exudation or sap drawn from the date palm (ʿaraq al-tamr)' → 'any distilled spirit', which is exactly Nourai's 'to sweat; sweat, juice, liquor'. Yule-Burnell put it in one sentence: 'This word is the Ar. ʿaraq, properly «perspiration», and then, first the exudation or sap drawn from the date palm (ʿaraq al-tamar); secondly any strong … «distilled spirit»'. Nourai writes the ʿayn as a plain A ('A.r.q'), his usual convention. His only reference here, FVA:269 (Nahvi, Farhang-e Vāzhehā-ye ʿArabi dar Fārsi), has no digital copy anywhere and could not be checked. The one weak point of the whole entry is the borage branch: the passage of ʿaraq into Medieval Latin borrāgō is a contested hypothesis, not a fact (see node #3), and the printed gloss of node #5 is wrong.\",\n      \"note_fa\": \"ریشه، برچسب زبانی و معنا هر سه درست است. فعل عربی عَرِقَ «عرق کردن» با مصدرِ عَرَق «خوی، عرق» عربی فصیح معیار است؛ گسترش معنایی آن چنین است: «عرق بدن» ← «شیرابه یا افشرهٔ درخت خرما (عَرَق التَّمر)» ← «هر نوشیدنیِ تقطیرشده»، که دقیقاً همان «to sweat; sweat, juice, liquor» نورایی است. یول و برنل در Hobson-Jobson همین زنجیره را در یک جمله می‌آورند. نورایی طبق شیوهٔ همیشگی‌اش عینِ عربی را با A نشان داده («A.r.q»). تنها ارجاع او در این مدخل، FVA:269 (نحوی، فرهنگ واژه‌های عربی در فارسی)، هیچ نسخهٔ دیجیتالی ندارد و بررسی نشد. نقطهٔ سستِ این مدخل شاخهٔ «گاوزبان» است: گذر عَرَق به لاتین میانهٔ borrāgō فرضیه‌ای مورد اختلاف است نه واقعیت (گرهٔ ۳)، و معنایی که کتاب برای گرهٔ ۵ چاپ کرده نادرست است.\",\n      \"ref_check\": [\n        {\"ref\": \"FVA:269\", \"status\": \"not_checked\", \"note\": \"FVA = S. M. Nahvi, Farhang-e Vāzhehā-ye ʿArabi dar Fārsi (dakhil), Tohi/Azadi 1368/1989. refs_online.json records: 'Searched archive.org, ketabnak, noorlib, web: no digital copy found' — only an OpenLibrary catalogue record (OL2012991M) exists. Not accessible.\"}\n      ],\n      \"sources\": [\"https://en.wiktionary.org/wiki/عرق\"],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"araq «عرق»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian عرق araq is a straight Arabic loan — there is no Iranian word of this shape, and the ʿayn is preserved in the spelling although Persian pronounces it as a plain vowel onset. It came in with the whole Galenic-Arabic medical and pharmacological vocabulary after the Islamic conquest, and both of Nourai's glosses are right: 'sweat' is the primary Arabic sense, and 'liquor' is the specialisation of Arabic ʿaraq al-tamr 'sweat of the dates', i.e. the distillate of date-palm sap, whence Persian and Turkish araq/rakı, the Indian and Malay arrack (Yule-Burnell, s.v. ARRACK, RACK), Ottoman-mediated European arrack/arac/rack, Russian arak and even the French argot riquiqui 'brandy'. Modern Persian keeps both senses plus a third, 'herbal distillate' (عرق نعناع, عرق کاسنی), which Mo'in's dictionary documents. The direction of the arrow (Arabic → Persian) is correct.\",\n          \"derivation_fa\": \"«عرق» در فارسی وام‌واژه‌ای مستقیم از عربی است — هیچ واژهٔ ایرانیِ هم‌ساخت با آن وجود ندارد و «ع» در املا نگه داشته شده هرچند فارسی‌زبانان آن را تلفظ نمی‌کنند. این واژه همراه با کل واژگان پزشکی و داروشناسیِ عربیِ برگرفته از جالینوس، پس از فتح اسلامی وارد فارسی شد. هر دو معنای نورایی درست است: «خوی» معنای نخستینِ عربی است و «عرق (نوشیدنی)» تخصیصِ عربیِ عَرَق التَّمر «خویِ خرما» یعنی تقطیرِ شیرهٔ نخل است؛ از همین‌جا رَکیِ ترکی، arrack هندی و مالایایی (نک. Hobson-Jobson ذیل ARRACK)، arak روسی و حتی riquiqui در زبان عامیانهٔ فرانسه پدید آمده‌اند. فارسی امروز افزون بر این دو، معنای سومِ «عرقیّات گیاهی» (عرق نعناع، عرق کاسنی) را نیز دارد که در فرهنگ معین ثبت است. جهت پیکان (عربی ← فارسی) درست است.\",\n          \"ref_check\": [\n            {\"ref\": \"FVA:269\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi's Farhang-e Vāzhehā-ye ʿArabi dar Fārsi exists (see the entry-level ref_check); the claim is however trivially confirmable elsewhere.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"s.v. ARRACK, RACK\", \"stance\": \"supports\", \"note\": \"'This word is the Ar. ʿaraq, properly «perspiration», and then, first the exudation or sap drawn from the date palm (ʿaraq al-tamar); secondly any strong … «distilled spirit». But it has spread to very remote corners of Asia … The Turkish form of the word, rāḳī …'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 92, p.9\", \"stance\": \"supports\", \"note\": \"'92. Ar. ʿarak: «Schweiß», ʿarak at-tamr «Schweiß der Datteln», d.h. Dattelsaft, ein berauschendes Getränk … Sp. arac, altsp. arrequi(n), frz. arak, rack … engl. arrack, rack, ndl. arak, dtsch. Arrak. Aus dem ar. Adjektiv ʿaraki wohl das frz. Argot-Wort riquiqui «Schnaps». Die tk. Form ist ebenso raki …'\"},\n            {\"src\": \"DOZ\", \"where\": \"Oosterlingen s.v. arak\", \"stance\": \"supports\", \"note\": \"'In het klassieke Arab. beduidt ʿarak eigenlijk [zweet] … Dit is de eigenlijke ʿarak of ʿarakī; maar bij verloop van tijd … In Oost-Indië wordt de naam ʿarak gegeven …'\"},\n            {\"src\": \"LAM\", \"where\": \"Lammens, Remarques s.v. arak\", \"stance\": \"supports\", \"note\": \"'arak, araque, orraca, rak. Tous ces mots représentent l'arabe ʿaraq, liqueur extraite du palmier … En turc usuel ʿaraq devient rakè, eau-de-vie.'\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi, compounds of عرق\", \"stance\": \"partial\", \"note\": \"the bare headword عرق is not recoverable from this OCR, but Mo'in's derivatives carry the Arabic origin tag, e.g. 'معرق [ع.] (افا.) آنچه که تولید عرق کند، عرق‌آور، خوی‌آور (پز.)' (MON_part2.txt l.60714-60715), and he documents the herbal-distillate sense 'عرق کاسنی: (پز.) عرقی که از تقطیر جوشاندهٔ ریشه و برگ‌های … ' (l.18279-18280).\"}\n          ],\n          \"sources\": [\"https://en.wiktionary.org/wiki/عرق\"]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Arabic\",\n          \"words\": \"abŭ-araq\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The compound أبو العرق ʾabū l-ʿaraq, literally 'father of sweat', is the form the whole Western etymological tradition puts behind Medieval Latin borrāgō. Klein s.v. borage: 'ult. fr. Arab. abu ʿaraq, lit. «father of sweat», so called by the Arab physicians because of its sudorific effect'; Lokotsch no. 13: 'Ar. abū ʿaraq: «Vater des Schweißes», hieraus lat. borrago, eine Pflanze, die durch die ar. Medizin im Mittelalter verbreitet wurde'; Pihan s.v. BOURRACHE: 'père (de) la sueur … Plante originaire du Levant, et dont l'étymologie arabe suffit pour indiquer la vertu sudorifique'; the AHD (Nourai's own citation) has 'Medieval Latin borāgō, probably from Arabic būʿaraq, from ʾabū ʿaraq «source of sweat»'. The formation is impeccable Arabic — the kunya pattern abū + noun is the ordinary Arabic way of naming plants and animals (cf. Lokotsch no. 11 abū kirdān 'father of ticks' = the cattle egret). What it lacks is attestation: the classical Arabic name of Borago officinalis is لسان الثور lisān al-thawr 'ox-tongue', and abū l-ʿaraq is not quotable from any Arabic herbal — which is why the whole derivation is only 'probably'/'perhaps' in the dictionaries that accept it. Plausible, not confirmed. (The '☞Ab 2' cross-reference to Arabic ab/abū 'father' is correct.)\",\n          \"derivation_fa\": \"ترکیب «أبو العَرَق» به معنی تحت‌اللفظیِ «پدرِ عرق» همان صورتی است که کل سنت ریشه‌شناسی غربی پشت لاتینِ میانهٔ borrāgō می‌گذارد. کلاین می‌نویسد که borage «سرانجام از عربی abu ʿaraq، تحت‌اللفظ «پدر عرق»، چنین نامیده شده به دست پزشکان عرب به سبب خاصیت عرق‌آورش»؛ لوکوچ (شمارهٔ ۱۳) و پیهان (ذیل BOURRACHE) و فرهنگ American Heritage (همان ارجاع نورایی) نیز همین را می‌گویند. این ساخت از نظر دستور عربی بی‌عیب است: الگوی کنیه‌ای «أبو + اسم» شیوهٔ رایج نام‌گذاری گیاهان و جانوران در عربی است (سنجید با أبو کِردان «پدر کَنه‌ها» = گاوچرانک). آنچه کم دارد گواه متنی است: نام کلاسیک عربی گاوزبان «لسان الثور» است و «أبو العرق» از هیچ کتاب گیاه‌داروییِ عربی نقل نشده — و از همین‌روست که همان فرهنگ‌هایی هم که آن را می‌پذیرند با قید «احتمالاً» می‌آورند. پس: با احتیاط پذیرفتنی، نه قطعی. ارجاع «☞Ab 2» به «أب/أبو» عربی درست است.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"The 1976 AHD main dictionary p.152 is not open online, but the same house's current entry (ahdictionary.com/word/search.html?q=borage) prints: '[Middle English, from Old French bourage, from Medieval Latin borāgō, probably from Arabic būʿaraq]', explained as from ʾabū ʿaraq 'source of sweat', because of the plant's sudorific use. That is exactly what Nourai's node says, hedge included.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed. pp.186/187 s.v. borage\", \"stance\": \"supports\", \"note\": \"'borage, n., a blue-flowered plant used in salads. — ME., fr. OF. borrace (cp. its variant burage and F. bourrache), fr. ML. borrago, ult. fr. Arab. abu ʿaraq, lit. «father of sweat», so called by the Arab physicians because of its sudorific effect. See abbot and cp. arrack.'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 13, p.2\", \"stance\": \"supports\", \"note\": \"'13. Ar. abū ʿaraq: «Vater des Schweißes», hieraus lat. borrago … Trotz ML 1412 scheint diese Ableitung noch immer die beste und wenig anfechtbar zu sein. [Kluge 64.]'\"},\n            {\"src\": \"PHN\", \"where\": \"s.v. BOURRACHE (printed p.74/76)\", \"stance\": \"supports\", \"note\": \"'BOURRACHE, s. f. composé, (a.) [abū] [ʿaraq] … «père (de) la sueur». Plante originaire du Levant, et dont l'étymologie arabe suffit pour indiquer la vertu sudorifique; on l'emploie principalement dans les tisanes pectorales.'\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\", \"note\": \"grep for 'araq' in FVQ_pages.txt yields only the proper name Suraqa; ʿaraq is native Arabic and so is outside Jeffery's scope.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"no BOURRACHE headword recoverable from DEV.txt (grep 'ourrache' finds nothing).\"}\n          ],\n          \"sources\": [\"https://ahdictionary.com/word/search.html?q=borage\", \"https://en.wiktionary.org/wiki/borage\"]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Middle Latin\",\n          \"words\": \"borrâgo\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"That Medieval Latin borrāgō, -inis (the Salernitan/Arabic-derived medical Latin of the 11th-12th c., whence Linnaeus's genus Borāgō) is the source of every Romance and Germanic name of the plant is certain. What is disputed is where borrāgō itself comes from, and Nourai prints one of two competing hypotheses as fact. (a) The Arabic route he follows — ML borrāgō < Arabic ʾabū l-ʿaraq — is that of AHD:152 (his citation), Klein, Lokotsch ('trotz ML 1412 scheint diese Ableitung noch immer die beste und wenig anfechtbar zu sein') and Pihan. (b) The competing and now more widely held view derives it from Late Latin borra / burra 'coarse wool, rough hair' (whence It. borra, Fr. bourre) with reference to the plant's bristly, hairy leaves: Skeat 'prob. named from its roughness. Perhaps from Low L. borra, burra, rough hair (whence F. bourre, Ital. borra)'; Webster '[LL. borrago, borago, from borra, the hair of beasts]'; Funk & Wagnalls '[< LL. borrago, < borra, burra, rough hair]'; the OED, followed by Etymonline, which calls the Arabic story a 'folk etymology theory' and prefers 'Latin borra «rough hair, short wool», in reference to the texture of the foliage'. Wiktionary lists both without deciding. Phonology and morphology favour (b): -āgō is a productive native Latin plant-name suffix (plantāgō, farrāgō, filāgō), whereas ʾabū l-ʿaraq should have given something like *abularac-, with no obvious way to lose the initial syllable and gain -āgō. Modern scholarship therefore leans against Nourai's arrow, though it does not rule it out.\",\n          \"derivation_fa\": \"اینکه لاتینِ میانهٔ borrāgō (از لاتینِ پزشکیِ مکتب سالرنو در سده‌های یازدهم و دوازدهم، که نام جنس گیاه‌شناسیِ Borāgō نیز از آن است) سرچشمهٔ همهٔ نام‌های رومی و ژرمنیِ گاوزبان است، جای تردید ندارد. آنچه محل اختلاف است خاستگاه خودِ borrāgō است و نورایی یکی از دو فرضیهٔ رقیب را به‌جای واقعیت نشانده. الف) راه عربی که او پی گرفته — borrāgō از «أبو العرق» — رأی فرهنگ American Heritage (همان ارجاع خودش)، کلاین، لوکوچ و پیهان است. ب) رأی رقیب و امروز پذیرفته‌تر آن را از لاتین متأخر borra/burra «پشم زبر، موی درشت» می‌داند (که bourre فرانسه و borra ایتالیایی از آن است) با اشاره به برگ‌های کُرک‌دار و زبرِ این گیاه: اسکیت، وبستر، فانک و واگنالز، و فرهنگ آکسفورد به‌پیروی اتیمآنلاین که روایت عربی را «ریشه‌شناسی عامیانه» می‌خواند. ویکی‌واژه هر دو را بی‌داوری می‌آورد. آواشناسی و ساخت‌واژه به سود (ب) است: پسوند -āgō پسوندی زایا و بومی برای نام گیاهان در لاتین است (plantāgō، farrāgō، filāgō)، حال آنکه «أبو العرق» می‌بایست چیزی مانند *abularac- می‌داد. پس پژوهش امروزی به پیکان نورایی گرایش ندارد، هرچند آن را یکسره رد هم نمی‌کند.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"AHD does print the Arabic derivation, hedged: '[Middle English, from Old French bourage, from Medieval Latin borāgō, probably from Arabic būʿaraq]' (< ʾabū ʿaraq 'source of sweat'). So Nourai reports his source faithfully — the problem is that the source itself is only one side of a standing dispute, and says 'probably'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Borage\", \"stance\": \"contradicts\", \"note\": \"'Borage. (F. — Low L.) … F. bourrache. — Low L. borraginem, acc. of borrago, borage; prob. named from its roughness. Perhaps from Low L. borra, burra, rough hair (whence F. bourre, Ital. borra); see Burl [= Burr].' No Arabic at all.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict. s.v. borage\", \"stance\": \"contradicts\", \"note\": \"'bor'age, n. [ME. borage, burage; LL. borrago, borago, from borra, the hair of beasts.] a plant of the genus Borago, used medicinally for its soothing and perspiratory properties and sometimes used in salads.'\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dict. s.v. borage\", \"stance\": \"contradicts\", \"note\": \"'European herb (Borago officinalis) with ovate leaves and blue flowers … [< LL. borrago, < borra, burra, rough hair; see bolt2, n.]'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 13, p.2\", \"stance\": \"supports\", \"note\": \"Lokotsch defends the Arabic derivation explicitly against Meyer-Lübke: 'Trotz ML 1412 scheint diese Ableitung noch immer die beste und wenig anfechtbar zu sein' — which itself shows that ML (Meyer-Lübke's REW no. 1412) already preferred the borra etymology in 1927.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed. pp.186/187 s.v. borage\", \"stance\": \"supports\", \"note\": \"'fr. ML. borrago, ult. fr. Arab. abu ʿaraq'.\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/borage\", \"https://en.wiktionary.org/wiki/borage\", \"https://ahdictionary.com/word/search.html?q=borage\"]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old French\",\n          \"words\": \"bourrache, borrace\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French borrace (13th c., also burage; modern French bourrache) is the regular popular development of the Medieval Latin accusative borrāginem: intervocalic -g- before the ending palatalises and the syllable yields -ache, the same treatment as Latin -āticum > French -age. Klein: 'ME., fr. OF. borrace (cp. its variant burage and F. bourrache), fr. ML. borrago'; Skeat likewise 'F. bourrache. — Low L. borraginem, acc. of borrago'. The rest of the Romance family points to the same accusative stem: It. borragine/borrace/borrana, Prov. borrage, Sp. borraja, Pg. borragem (Lokotsch no. 13), with Rum. boranjă probably through Modern Greek. Both spellings Nourai prints are attested. This link is uncontested whatever the ultimate origin of borrāgō turns out to be.\",\n          \"derivation_fa\": \"فرانسهٔ کهن borrace (سدهٔ سیزدهم، با گونهٔ burage؛ فرانسهٔ امروز bourrache) دنبالهٔ عادی و مردمیِ صورت مفعولیِ لاتینِ میانه borrāginem است: -g- میان‌واکه‌ای پیش از پایانه کامی می‌شود و هجا به -ache می‌رسد، همان‌گونه که -āticum لاتین در فرانسه -age می‌دهد. کلاین می‌نویسد: «انگلیسی میانه، از فرانسهٔ کهن borrace (با گونهٔ burage و فرانسهٔ bourrache)، از لاتین میانه borrago»؛ اسکیت نیز همین را می‌آورد. دیگر صورت‌های رومی هم به همان ستاکِ مفعولی می‌رسند: ایتالیایی borragine/borrana، پروانسی borrage، اسپانیایی borraja، پرتغالی borragem. هر دو املایی که نورایی آورده گواه دارند. این پله بی‌اختلاف است، هر خاستگاهی که borrāgō داشته باشد.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD: '[Middle English, from Old French bourage, from Medieval Latin borāgō …]' — the Old French link is exactly as drawn (AHD's headform is bourage/bourrache rather than borrace, but Klein gives borrace as the older spelling).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed. pp.186/187 s.v. borage\", \"stance\": \"supports\", \"note\": \"'ME., fr. OF. borrace (cp. its variant burage and F. bourrache), fr. ML. borrago'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Borage\", \"stance\": \"supports\", \"note\": \"'F. bourrache. — Low L. borraginem, acc. of borrago, borage.'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 13, p.2\", \"stance\": \"supports\", \"note\": \"'Die romanischen Formen sind: it. borrace, borragine, borrana; prov. borrage; sp. borraja; pg. borragem; frz. bourrache.'\"},\n            {\"src\": \"PHN\", \"where\": \"s.v. BOURRACHE\", \"stance\": \"supports\", \"note\": \"Pihan lists BOURRACHE as a French word of Arabic origin, 'plante originaire du Levant' — confirming the French form though not, of course, adjudicating the ML question.\"}\n          ],\n          \"sources\": [\"https://en.wiktionary.org/wiki/borage\", \"https://ahdictionary.com/word/search.html?q=borage\"]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"borage\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"borage : a spicy salad dressing\",\n          \"correct_form\": \"borage : a blue-flowered herb (Borago officinalis) whose leaves are used in salads and cool drinks\",\n          \"derivation\": \"The word and the route are right: Middle English borage / burage, borrowed in the 13th-14th c. from Anglo-French burage / Old French borrace, is Borago officinalis, a bristly, blue-flowered Mediterranean herb whose cucumber-tasting leaves and flowers went into salads and into cooling drinks such as claret cup, and which the medieval pharmacopoeia used as a demulcent and diaphoretic. The GLOSS, however, is wrong: borage is a plant, not a dressing. Nourai has compressed Klein's definition — 'borage, n., a blue-flowered plant used in salads' — and lost the head noun, turning the salad herb into 'a spicy salad dressing'. I rendered pdf page 64 at 300 dpi and read it: the printed page 34 does read 'borage : a spicy salad dressing', so the extraction is faithful and the slip is the book's own. Note also that the whole branch above this node rests on the contested Arabic etymology of node #3.\",\n          \"derivation_fa\": \"خودِ واژه و مسیر آن درست است: انگلیسی میانهٔ borage/burage که در سده‌های سیزدهم و چهاردهم از انگلوـفرانسهٔ burage و فرانسهٔ کهن borrace وام گرفته شده، نام گیاه Borago officinalis (گاوزبان) است؛ گیاهی مدیترانه‌ای با گل‌های آبی و برگ‌های زبر و کرک‌دار که مزهٔ خیار می‌دهد و برگ و گلش را در سالاد و نوشیدنی‌های خنک می‌ریختند و در داروشناسی سده‌های میانه نرم‌کننده و عرق‌آور می‌شمردند. اما معنایی که کتاب داده نادرست است: گاوزبان یک گیاه است، نه «سُس سالاد». نورایی تعریف کلاین را — «گیاهی با گل آبی که در سالاد به کار می‌رود» — فشرده کرده و هستهٔ اسمی را انداخته و از آن «سُسِ تندِ سالاد» ساخته است. من صفحهٔ ۶۴ پی‌دی‌اف را با تفکیک ۳۰۰ نقطه بر اینچ رندر و بازخوانی کردم: صفحهٔ چاپیِ ۳۴ عیناً همین «borage : a spicy salad dressing» را دارد؛ پس استخراج داده درست بوده و خطا از خودِ کتاب است. افزون بر این، تمام این شاخه بر ریشه‌شناسی عربیِ محل اختلافِ گرهٔ ۳ استوار است.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"partial\", \"note\": \"AHD supplies the etymology Nourai reproduces ('[Middle English, from Old French bourage, from Medieval Latin borāgō, probably from Arabic būʿaraq]'), but its definition is of course a plant ('a Mediterranean herb … having blue flowers and hairy leaves used as flavoring'), not a dressing — so AHD does not support the printed gloss.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed. pp.186/187 s.v. borage\", \"stance\": \"contradicts\", \"note\": \"'borage, n., a blue-flowered plant used in salads' — evidently Nourai's model, and it says plant, not dressing.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's 2nd s.v. borage\", \"stance\": \"contradicts\", \"note\": \"'a plant of the genus Borago, used medicinally for its soothing and perspiratory properties and sometimes used in salads: written also burridge.'\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. borage\", \"stance\": \"contradicts\", \"note\": \"'European herb (Borago officinalis) with ovate leaves and blue flowers in terminal clusters. An infusion of the leaves and flowers is used as a demulcent and diaphoretic and in making cooling drinks.'\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Borage\", \"stance\": \"supports\", \"note\": \"confirms the ME < OF < ML chain of the node itself ('F. bourrache. — Low L. borraginem, acc. of borrago, borage').\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/borage\", \"https://en.wiktionary.org/wiki/borage\", \"https://ahdictionary.com/word/search.html?q=borage\"]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-64.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-04T23:24:00.190Z] TOOL RESULT

```
JSON OK
```


## [2026-09-04T23:24:05.993Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 tools/verify_check.py 64"
}
```


### [2026-09-04T23:24:07.958Z] TOOL RESULT

```
nodes verified: 14/14
node verdicts: {'confirmed': 8, 'plausible': 4, 'disputed': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'partial': 2, 'contradicts': 1, 'not_checked': 3}
books consulted: {'supports': 43, 'contradicts': 8, 'partial': 5, 'silent': 8} | by book: {'KLN': 8, 'IEC': 5, 'SKT': 5, 'POK': 4, 'LKT': 4, 'SYN': 3, 'AHD': 3, 'HUB': 3, 'BRT': 2, 'PHD': 2, 'ARY': 2, 'MON': 2, 'LAT': 2, 'PHN': 2, 'WEB': 2, 'FSD': 2, 'HRN': 1, 'NYB': 1, 'FRS': 1, 'FSF': 1, 'BQT': 1, 'TLM': 1, 'ISS_alt_DKS': 1, 'LEW': 1, 'HJB': 1, 'DOZ': 1, 'LAM': 1, 'FVQ': 1, 'DEV': 1}
```


## [2026-09-04T23:24:25.171Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-64.json`; `verify_check.py 64` is clean (no PROBLEM lines).

**Page 64 (book p. 34) — 2 non-redirect entries, 14 nodes**
- Root verdicts: confirmed 2 (Arg = PIE \*h₂erǵ-, POK:64 verbatim; Arabic ʿ-r-q).
- Node verdicts: confirmed 8, plausible 4, disputed 1, transcription_suspect 1.
- Ref checks: supports 9, partial 2, contradicts 1, not_checked 3. Books consulted: 29 distinct titles.

Flagged items:
- **disputed** — A.r.q #3, Middle Latin `borrâgo`: Nourai (after AHD:152, Klein, Lokotsch, Pihan) derives it from Arabic ʾabū l-ʿaraq; OED/Etymonline, Skeat, Webster, Funk & Wagnalls prefer Late Latin *borra/burra* "rough hair" (bristly leaves), and -āgō is a native Latin plant-name suffix. One of two live hypotheses, presented as fact.
- **transcription_suspect (error_in: book)** — A.r.q #5, English `borage`: printed page reads "borage : a spicy salad dressing"; borage is a *plant* (Klein: "a blue-flowered plant used in salads"). Extraction is faithful — checked the 300 dpi render of pdf p. 64 — so this is Nourai's own slip.

Other notable findings (not flagged as disputed but worth the owner's eye):
- **Arg #2/#3/#5 (arzīz branch, marked plausible)**: Horn p. 17 no. 68 — the very page Nourai cites on #3 — *contradicts* the chart: "die Ableitung von aw. erezata-, skr. rajatá- … ist lautlich unmöglich; die Heimat des Wortes ist noch durchaus unbekannt", and glosses it 'Blei'. MP for 'silver' is *asēm* (Bartholomae). Mann (IEC), Aryanpur and ESIJa (via Wiktionary) do connect arzīz to the root, but as a sister \*arzi-ča- formation, not a descendant of Av. ərəzata-. Nodes #2 and #5 are also the *same* word, not two branches.
- **Arg #4 (plausible)**: KNT:171 is quoted verbatim and correctly, but Kent's "arda- 'light'" is extracted from the compound only (Foy's reading); Bartholomae AiW 193 and Tolman read arda- = 'half, side'. OP *ardata-* itself (DSf 40) is certain.
- No extraction errors found in the JSON for this page. Nourai's `FVA:269` (Nahvi) has no digital copy anywhere — the only not_checked reference.
