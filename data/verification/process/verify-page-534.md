# Verification process log — verify-page-534


## [2026-10-16T05:13:02.046Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 534 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-534.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-534.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-534.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 534` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:02.111Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:05.382Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:05.398Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe-private`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe-private/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe-private/data/verification/page-<pdf>.json` (UTF-8, no BOM):
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
279	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-10-16T05:13:05.879Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-534.txt"
}
```


### [2026-10-16T05:13:05.903Z] TOOL RESULT

```
1	=== PDF page 534 (book page 504) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Weid, Woid, Wid : to see, to know  (refs POK:1125)
4	#1 (parent #0) [Avestan] refs=POK:1125, 1126 | vaeda, vîdada : I know ; vîd- : knowing ; vidya : knowledge ; vista- : well known ; hu-vaeda : well known, apparent ☞Su 1
5	  #2 (parent #1) [Persian] refs=MON:5069,5669; BQT:2297,2401 | vîdâ «ویدا» : apparent ; Avestâ «اوستا» : well known, knowledge, Holy Book of Zoroastrians ; hovaydâ «هویدا» : apparent
6	  #3 (parent #1) [Avestan] refs=POK:1121; AEF:379; HRN:70 | vîdaiti, vînosti, vîvaĕda : find, finds ; paitiš-vaĕd : to search for | NOTE: HUB:41 does not agree with this etymology.
7	    #4 (parent #3) [Persian] refs=AEF:379 | pažuhîdan : search | extra: پژوهش ، پژوه
8	#5 (parent #0) [Latin] refs=AHD | viděre, visus : to see, look
9	  #6 (parent #5) [French] refs=None | television ; visite
10	    #7 (parent #6) [Persian] refs=MON:1136,5071 | televîzion «تلویزیون» : television ; vîzît «ویزیت (ویزا)» : visit
11	  #8 (parent #5) [English] refs=None | view, review, interview, advice, envy, evident, vision, television, visa, visit, provide, survey, video
12	    #9 (parent #8) [Persian] refs=None | vîdîyo «ویدیو» : video
13	#10 (parent #0) [Welsh] refs=AHD | pen-gwyn : white-headed (bird), penguin
14	  #11 (parent #10) [French] refs=None | 
15	    #12 (parent #11) [Persian] refs=AMD:487 | panguwan «پنگوئن» : penguin
16	#13 (parent #0) [Greek] refs=POK:1127; AHD | histôr : wise ; istoria : history, historical tales ; idea : form
17	  #14 (parent #13) [Arabic] refs=TAD:3; FVQ:56 | ostůreh : historical tale ; asâtîr : fables, myths | NOTE: FVQ:56 & VDQ:113,257 derive these from Arabic "s.t.r: write"; from Akkadian "šatarů:to write".
18	    #15 (parent #14) [Persian] refs=MON:225 | ostůreh «اسطوره» : myth ; asâtîr «اساطیر» : myths, fables
19	  #16 (parent #13) [English] refs=None | story, history, idea
20	#17 (parent #0) [Germanic] refs=AHD | wîtan : to look after, guide ; wîssaz : wisdom ; wit : wit
21	  #18 (parent #17) [English] refs=None | wit, wise, wisdom, guide
22	
```


## [2026-10-16T05:13:06.559Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-534.json"
}
```


### [2026-10-16T05:13:06.779Z] TOOL RESULT

```
1	{
2	  "pdf_page": 534,
3	  "book_page": 504,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Weid, Woid, Wid",
8	        "lang": "Indo-European",
9	        "refs": "POK:1125",
10	        "gloss": "to see, to know"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1125, 1126",
18	          "words": [
19	            {"translit": "vaeda, vîdada", "gloss": "I know", "script": null},
20	            {"translit": "vîd-", "gloss": "knowing", "script": null},
21	            {"translit": "vidya", "gloss": "knowledge", "script": null},
22	            {"translit": "vista-", "gloss": "well known", "script": null},
23	            {"translit": "hu-vaeda", "gloss": "well known, apparent", "script": null, "see": ["Su 1"]}
24	          ],
25	          "note": null,
26	          "quote": null
27	        },
28	        {
29	          "id": 2,
30	          "parent": 1,
31	          "lang": "Persian",
32	          "refs": "MON:5069,5669; BQT:2297,2401",
33	          "words": [
34	            {"translit": "vîdâ", "gloss": "apparent", "script": "ویدا"},
35	            {"translit": "Avestâ", "gloss": "well known, knowledge, Holy Book of Zoroastrians", "script": "اوستا"},
36	            {"translit": "hovaydâ", "gloss": "apparent", "script": "هویدا"}
37	          ],
38	          "note": null,
39	          "quote": null
40	        },
41	        {
42	          "id": 3,
43	          "parent": 1,
44	          "lang": "Avestan",
45	          "refs": "POK:1121; AEF:379; HRN:70",
46	          "words": [
47	            {"translit": "vîdaiti, vînosti, vîvaĕda", "gloss": "find, finds", "script": null},
48	            {"translit": "paitiš-vaĕd", "gloss": "to search for", "script": null}
49	          ],
50	          "note": "HUB:41 does not agree with this etymology.",
51	          "quote": null
52	        },
53	        {
54	          "id": 4,
55	          "parent": 3,
56	          "lang": "Persian",
57	          "refs": "AEF:379",
58	          "words": [
59	            {"translit": "pažuhîdan", "gloss": "search", "script": null}
60	          ],
61	          "script_extra": "پژوهش ، پژوه",
62	          "note": null,
63	          "quote": null
64	        },
65	        {
66	          "id": 5,
67	          "parent": 0,
68	          "lang": "Latin",
69	          "refs": "AHD",
70	          "words": [
71	            {"translit": "viděre, visus", "gloss": "to see, look", "script": null}
72	          ],
73	          "note": null,
74	          "quote": null
75	        },
76	        {
77	          "id": 6,
78	          "parent": 5,
79	          "lang": "French",
80	          "refs": null,
81	          "words": [
82	            {"translit": "television", "gloss": null, "script": null},
83	            {"translit": "visite", "gloss": null, "script": null}
84	          ],
85	          "note": null,
86	          "quote": null
87	        },
88	        {
89	          "id": 7,
90	          "parent": 6,
91	          "lang": "Persian",
92	          "refs": "MON:1136,5071",
93	          "words": [
94	            {"translit": "televîzion", "gloss": "television", "script": "تلویزیون"},
95	            {"translit": "vîzît", "gloss": "visit", "script": "ویزیت (ویزا)"}
96	          ],
97	          "note": null,
98	          "quote": null
99	        },
100	        {
101	          "id": 8,
102	          "parent": 5,
103	          "lang": "English",
104	          "refs": null,
105	          "words": [
106	            {"translit": "view, review, interview, advice, envy, evident, vision, television, visa, visit, provide, survey, video", "gloss": null, "script": null}
107	          ],
108	          "note": null,
109	          "quote": null
110	        },
111	        {
112	          "id": 9,
113	          "parent": 8,
114	          "lang": "Persian",
115	          "refs": null,
116	          "words": [
117	            {"translit": "vîdîyo", "gloss": "video", "script": "ویدیو"}
118	          ],
119	          "note": null,
120	          "quote": null
121	        },
122	        {
123	          "id": 10,
124	          "parent": 0,
125	          "lang": "Welsh",
126	          "refs": "AHD",
127	          "words": [
128	            {"translit": "pen-gwyn", "gloss": "white-headed (bird), penguin", "script": null}
129	          ],
130	          "note": null,
131	          "quote": null
132	        },
133	        {
134	          "id": 11,
135	          "parent": 10,
136	          "lang": "French",
137	          "refs": null,
138	          "words": [],
139	          "note": null,
140	          "quote": null
141	        },
142	        {
143	          "id": 12,
144	          "parent": 11,
145	          "lang": "Persian",
146	          "refs": "AMD:487",
147	          "words": [
148	            {"translit": "panguwan", "gloss": "penguin", "script": "پنگوئن"}
149	          ],
150	          "note": null,
151	          "quote": null
152	        },
153	        {
154	          "id": 13,
155	          "parent": 0,
156	          "lang": "Greek",
157	          "refs": "POK:1127; AHD",
158	          "words": [
159	            {"translit": "histôr", "gloss": "wise", "script": null},
160	            {"translit": "istoria", "gloss": "history, historical tales", "script": null},
161	            {"translit": "idea", "gloss": "form", "script": null}
162	          ],
163	          "note": null,
164	          "quote": null
165	        },
166	        {
167	          "id": 14,
168	          "parent": 13,
169	          "lang": "Arabic",
170	          "refs": "TAD:3; FVQ:56",
171	          "words": [
172	            {"translit": "ostůreh", "gloss": "historical tale", "script": null},
173	            {"translit": "asâtîr", "gloss": "fables, myths", "script": null}
174	          ],
175	          "note": "FVQ:56 & VDQ:113,257 derive these from Arabic \"s.t.r: write\"; from Akkadian \"šatarů:to write\".",
176	          "quote": null
177	        },
178	        {
179	          "id": 15,
180	          "parent": 14,
181	          "lang": "Persian",
182	          "refs": "MON:225",
183	          "words": [
184	            {"translit": "ostůreh", "gloss": "myth", "script": "اسطوره"},
185	            {"translit": "asâtîr", "gloss": "myths, fables", "script": "اساطیر"}
186	          ],
187	          "note": null,
188	          "quote": {
189	            "text": "که اساطیر است و افسانه نژند - نیست تعمیقی و تحقیقی بلند",
190	            "poet": "Molavî"
191	          }
192	        },
193	        {
194	          "id": 16,
195	          "parent": 13,
196	          "lang": "English",
197	          "refs": null,
198	          "words": [
199	            {"translit": "story, history, idea", "gloss": null, "script": null}
200	          ],
201	          "note": null,
202	          "quote": null
203	        },
204	        {
205	          "id": 17,
206	          "parent": 0,
207	          "lang": "Germanic",
208	          "refs": "AHD",
209	          "words": [
210	            {"translit": "wîtan", "gloss": "to look after, guide", "script": null},
211	            {"translit": "wîssaz", "gloss": "wisdom", "script": null},
212	            {"translit": "wit", "gloss": "wit", "script": null}
213	          ],
214	          "note": null,
215	          "quote": null
216	        },
217	        {
218	          "id": 18,
219	          "parent": 17,
220	          "lang": "English",
221	          "refs": null,
222	          "words": [
223	            {"translit": "wit, wise, wisdom, guide", "gloss": null, "script": null}
224	          ],
225	          "note": null,
226	          "quote": null
227	        }
228	      ]
229	    }
230	  ]
231	}
232	
```


## [2026-10-16T05:13:17.167Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -120; ls sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','AHD','AEF','HRN','HUB','MON','BQT','AMD','TAD','FVQ','VDQ','WLD','KLN','SKT','BRT','IEC','SYN','ARY','CHEUNG','PHD','NYB','WEB','FSD']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-10-16T05:13:17.575Z] TOOL RESULT

```
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/UNV.txt`
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  incoming
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ocr
drwxr-xr-x     - sfmqrb 14 Oct 22:19  pageimg
drwxr-xr-x     - sfmqrb 14 Oct 22:25  tessdata
.rw-r--r--  600k sfmqrb 14 Oct 22:19  AFA.txt
.rw-r--r--   15M sfmqrb 14 Oct 22:19  AFM.pdf
.rw-r--r--  355k sfmqrb 14 Oct 22:19  AFM.txt
.rw-r--r--  384k sfmqrb 14 Oct 22:19  AFM_alt.txt
.rw-r--r--  342k sfmqrb 14 Oct 22:19  AFM_pages.txt
.rw-r--r--  850k sfmqrb 14 Oct 22:19  AHD_watkins1985.txt
.rw-r--r--  825k sfmqrb 14 Oct 22:19  AHM.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  AID.txt
.rw-r--r--  240k sfmqrb 14 Oct 22:19  AIN.txt
.rw-r--r--  256k sfmqrb 14 Oct 22:19  AKD.txt
.rw-r--r--  285k sfmqrb 14 Oct 22:19  ARB_abdulraheem.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  ARB_mo3rb.txt
.rw-r--r--  744k sfmqrb 14 Oct 22:19  ARP.txt
.rw-r--r--  633k sfmqrb 14 Oct 22:19  AVG.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_alt_v1.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  BQT_dli_part1.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_v1.txt
.rw-r--r--   26M sfmqrb 14 Oct 22:19  BQT_v1_djvu.xml
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  BQT_v1_pages.txt
.rw-r--r--  2.4M sfmqrb 14 Oct 22:19  BQT_v2.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  BQT_v2_pages.txt
.rw-r--r--  4.8M sfmqrb 14 Oct 22:19  BRT.txt
.rw-r--r--  656k sfmqrb 14 Oct 22:19  BST.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  CHEUNG.txt
.rw-r--r--  593k sfmqrb 14 Oct 22:19  DEV.txt
.rw-r--r--  144k sfmqrb 14 Oct 22:19  DOZ.txt
.rw-r--r--  1.5M sfmqrb 14 Oct 22:19  DRM.txt
.rw-r--r--  560k sfmqrb 14 Oct 22:19  EAV_studies.txt
.rw-r--r--  891k sfmqrb 14 Oct 22:19  FRS.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  FRS_pages.txt
.rw-r--r--   16M sfmqrb 14 Oct 22:19  FSD_vol1.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol2.txt
.rw-r--r--   13M sfmqrb 14 Oct 22:19  FSD_vol3.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol4.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  FSF.txt
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  FSF_pages.txt
.rw-r--r--  650k sfmqrb 14 Oct 22:19  FVQ.txt
.rw-r--r--  628k sfmqrb 14 Oct 22:19  FVQ_pages.txt
.rw-r--r--  573k sfmqrb 14 Oct 22:19  GPL.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  HENNING_selected_papers.txt
.rw-r--r--  449k sfmqrb 14 Oct 22:19  HID.txt
.rw-r--r--  5.6M sfmqrb 14 Oct 22:19  HJB.txt
.rw-r--r--  688k sfmqrb 14 Oct 22:19  HRN.txt
.rw-r--r--  527k sfmqrb 14 Oct 22:19  HUB.txt
.rw-r--r--  3.3M sfmqrb 14 Oct 22:19  IEC.txt
.rw-r--r--  3.4M sfmqrb 14 Oct 22:19  ISS_alt_DKS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  KFL.txt
.rw-r--r--   11M sfmqrb 14 Oct 22:19  KLN_1966.txt
.rw-r--r--   10M sfmqrb 14 Oct 22:19  KLN_1971.txt
.rw-r--r--  874k sfmqrb 14 Oct 22:19  KNT.txt
.rw-r--r--  944k sfmqrb 14 Oct 22:19  KNT_full.txt
.rw-r--r--  488k sfmqrb 14 Oct 22:19  LAM.txt
.rw-r--r--  4.6M sfmqrb 14 Oct 22:19  LAT.txt
.rw-r--r--  627k sfmqrb 14 Oct 22:19  LEW_1910.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  LKT.txt
.rw-r--r--   62k sfmqrb 14 Oct 22:19  LST.txt
.rw-r--r--  4.4M sfmqrb 14 Oct 22:19  MON_part1.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  MON_part2.txt
.rw-r--r--  373k sfmqrb 14 Oct 22:19  MPP.txt
.rw-r--r--  470k sfmqrb 14 Oct 22:19  NAT_2005.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  NYB.txt
.rw-r--r--  505k sfmqrb 14 Oct 22:19  NYB_vol1.txt
.rw-r--r--  920k sfmqrb 14 Oct 22:19  NYB_vol2_glossary.txt
.rw-r--r--  664k sfmqrb 14 Oct 22:19  PEI.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD.pdf
.rw-r--r--  341k sfmqrb 14 Oct 22:19  PHD.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD_mackenzie.pdf
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_mackenzie.txt
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_pages.txt
.rw-r--r--  604k sfmqrb 14 Oct 22:19  PHN.txt
.rw-r--r--  982k sfmqrb 14 Oct 22:19  POK_01.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  POK_02.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  POK_03.txt
.rw-r--r--  4.0M sfmqrb 14 Oct 22:19  POK_full.txt
.rw-r--r--  9.8M sfmqrb 14 Oct 22:19  RCH.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SBK.txt
.rw-r--r--  226k sfmqrb 14 Oct 22:19  SDQ.txt
.rw-r--r--  1.4M sfmqrb 14 Oct 22:19  SIN.txt
.rw-r--r--  2.7M sfmqrb 14 Oct 22:19  SKT.txt
.rw-r--r--  3.0M sfmqrb 14 Oct 22:19  SKT_dli_revised.txt
.rw-r--r--  326k sfmqrb 14 Oct 22:19  SNS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SNS_pages.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  SOD.txt
.rw-r--r--  3.7M sfmqrb 14 Oct 22:19  SOD_pages.txt
.rw-r--r--  466k sfmqrb 14 Oct 22:19  SPG_keilinschriften1881.txt
.rw-r--r--  4.5M sfmqrb 14 Oct 22:19  SYN.txt
.rw-r--r--  152k sfmqrb 14 Oct 22:19  TAD.txt
.rw-r--r--  243k sfmqrb 14 Oct 22:19  TAD_pages.txt
.rw-r--r--  313k sfmqrb 14 Oct 22:19  TLM.txt
.rw-r--r--   89k sfmqrb 14 Oct 22:19  UNV.txt
.rw-r--r--   12M sfmqrb 14 Oct 22:19  WEB_vol1.txt
.rw-r--r--  317k sfmqrb 14 Oct 22:19  WLD_band3.txt
.rw-r--r--  549k sfmqrb 14 Oct 22:19  ZAP.txt
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AMD {"title": "Hasan Amid, Farhang-e Farsi-ye Amid, 2 vols, Amir Kabir 1369/1990", "kind": "website", "url": "https://vajehyab.com/?q=<word>&d=amid ; https://abadis.ir/fatofa/<word>/ (فرهنگ عمید) ; scan on noorlib: https://noorlib.ir/book/view/28973?pageNumber=<N>&viewType=pdf", "lookup_hint": "Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable."
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaSc
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
```


## [2026-10-16T05:13:24.498Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,200p tools/verify_check.py | head -150; python3 -c \"\nimport json;d=json.load(open('data/verification/page-501.json'))\ne=d['entries'][0]; print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000]); print(json.dumps(e['nodes'][1],ensure_ascii=False,indent=1)[:3500])\""
}
```


### [2026-10-16T05:13:25.026Z] TOOL RESULT

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
{
 "entry": 0,
 "root": "Ten 1, Tengh, Temp",
 "verdict": "confirmed",
 "modern_form": "PIE *ten- 'to stretch' (Pokorny 1. ten- 1065-1066; LIV 626 f.), with the enlargements *tengʰ- 'to pull, draw' (Pokorny 1067; Cheung *θanǰ) and *temp- 'to stretch' (Pokorny 1064; Watkins temp-)",
 "note": "The root box is correct: Pokorny p.1064 has 'temp- to extend, stretch, span; Note: extension from *ten-', p.1067 'tengh- to extend, stretch, span; Aryan *thengh-, yet probably extension from ten-1', and pp.1065-1066 the base '1. ten-, tend- to extend, stretch'. Nourai's citation POK:1064,1067 covers the two enlargements; the base is on p.1065. Watkins (AHD) lists ten- and temp- with exactly Nourai's English outcomes (SITAR under ten-, TAFFETA and TAPESTRY under temp-). Problems lie in individual branches: (1) Av. tauruna- 'young' (#8) belongs to a different root, PIE *ter-/teru- 'tender, weak' (Pokorny 1070-1071, Mann teren-, Klein s.v. tender), so the tar/tarāneh/tūleh/tūrah branch does not belong under Ten; (2) Greek kithara (#14) is not from Persian tār/si-tār — it is a Pre-Greek word attested from Homer (kitharis), centuries before the Persian si-tār, although Klein (whom Nourai follows) writes 'Gk. kithara, fr. Pers. sihtār'; (3) English tape is a native Old English word (tæppe), not from the Persian/Greek carpet word; (4) Persian tābīdan 'twist' comes from the *temp- enlargement (Iranian *tāp-), not from Av. tan- as drawn; (5) hanjār 'path, norm' has no secure link to *θanǰ (Wiktionary: from Parthian anjār 'behaviour'; Mo'in compares Skt saṃcāra). The Avestan 'tathra' and 'thri-thatra' are not attested: the first is the reconstructed *tąθra- of Horn and Pokorny, the second appears to be Nourai's own back-projection of si-tār. The JSON matches the printed page (checked against the page image), including the inconsistent spellings tathra / thri-thatra and the reference 'KLN:572', which is a misprint in the book for KLN:1572 (tapestry). No extraction errors.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *ten- «کشیدن، کش دادن» (پوکورنی ۱۰۶۵–۱۰۶۶) و دو گونهٔ گسترش‌یافتهٔ آن، *tengʰ- «کشیدن، بیرون کشیدن» (پوکورنی ۱۰۶۷) و *temp- «کش دادن» (پوکورنی ۱۰۶۴)، درست آمده است و واتکینز نیز همین سه را با sitar و taffeta و tapestry آورده است؛ پس سرریشهٔ نورایی درست است. ایراد در چند شاخه است: «تئوروونه» (tauruna) اوستایی به معنای «جوان» از ریشهٔ دیگری (*ter- / *teru- «نرم، نازک») است، نه از *ten-؛ «کیثارا»ی یونانی از «سه‌تار» فارسی نیست و پژوهش امروزی آن را واژه‌ای پیشایونانی می‌داند؛ tape انگلیسی واژه‌ای بومی است؛ «تابیدن» از ستاک ایرانی *tāp- (گونهٔ *temp-) است نه از tan- اوستایی؛ و پیوند «هنجار» با *θanǰ ثابت نیست. «tathra» و «thri-thatra» در اوستا گواهی نشده‌اند و بازسازی (یا ساختهٔ خود نورایی) است. خطای استخراج دیده نشد؛ «KLN:572» در خود کتاب چاپ شده و خطای چاپی به جای ۱۵۷۲ است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ten-",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tengʰ-",
  "https://en.wiktionary.
{
 "id": 2,
 "lang": "Persian",
 "words": "hanjîdan; hanjâr; âhang; farhîxtan",
 "verdict": "plausible",
 "derivation": "hanjīdan/āhanjīdan 'to pull, draw out' continue MP (ā)hanj- [hnc-, ʾhnc-] < Ir. *(ā-)θanǰaya- (Cheung *θanǰ; Horn no. 58); āhang 'pull, draught' > 'intention, purpose' (later 'melody') is MP āhang [ʾhng] 'pull, draught' (MacKenzie), a deverbal noun of the same verb with ā-; farhīxtan 'to educate' is MP frahixtan/frahanj- 'educate' < *fra-θanǰ- 'draw forth' (cf. Latin educare/educere for the same semantic path), and farhang 'education, culture' is MP frahang [plhng] (Nyberg, MacKenzie; Arm. loan hrahang). Iranian *θ > MP/NP h regularly in Persian proper. hanjār 'path, manner, norm' is the weak point: Wiktionary derives it from MP hanjār < Parthian ʾnjʾr (anjār) 'behaviour' without linking it to *θanǰ, and Mo'in (BQT 2376 fn.) compares Skt saṃcāra- 'going about, path' (*ham-čāra-), i.e. a different root; Horn and Cheung do not list it under *θanǰ. Three of the four words are confirmed; hanjār is at best uncertain.",
 "derivation_fa": "«هنجیدن / آهنجیدن» (کشیدن، بیرون کشیدن) از فارسی میانهٔ (ā)hanj- و آن از ایرانی باستان *θanǰaya- است؛ θ ایرانی در فارسی به «ه» بدل شده است. «آهنگ» از فارسی میانهٔ āhang «کشش» و سپس «قصد، آهنگ کاری» است، و «فرهیختن» و «فرهنگ» از فارسی میانهٔ frahixtan / frahang از *fra-θanǰ- «بیرون کشیدن، پروردن» (همانند educare لاتینی) آمده‌اند؛ هرن، نیبرگ، مکنزی و چونگ همه این را تأیید می‌کنند. اما «هنجار» را ویکی‌واژه از پارتی anjār «رفتار» می‌داند و معین در حاشیهٔ برهان آن را با سنسکریت saṃcāra «گردش، راه» سنجیده است؛ پس پیوند آن با این ریشه ثابت نیست. ادعای نورایی برای سه واژه درست و برای «هنجار» با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/فرهنگ",
  "https://en.wiktionary.org/wiki/آهنگ",
  "https://en.wiktionary.org/wiki/هنجار",
  "https://en.wiktionary.org/wiki/آهیختن",
  "https://abadis.ir/fatofa/هنجار/"
 ],
 "ref_check": [
  {
   "ref": "HRN:14",
   "status": "supports",
   "note": "Horn no. 58 (HRN.txt line 950-973, leaf 36 = pp.14-15): 'āhenjīden \"ziehen, herausziehen\", vergl. āhīxten (āhexten) ... phlv. ahanjītan \"ziehen, fortziehen\" ... Np. āheng \"Plan, Absicht\" wird ebenfalls hierhergehören. Desgleichen np. ferhexten, ferhīxten ... \"erziehen\"; vergl. ferheng, ferhenj \"Wissen etc.\" (phlv. frahang ...; arm. LW. hrahang)'. hanjār not mentioned."
  },
  {
   "ref": "BQT:70",
   "status": "supports",
   "note": "BQT_v1_pages.txt leaf 280 (= p.70) s.v. آهنگ, Mo'in fn.: 'آهنگ، آهنگیدن، هنجیدن، آهیختن هم‌ریشه‌اند. از ریشهٔ اوستائی θang بمعنی کشیدن «بارتولمه ۷۸۵»'."
  },
  {
   "ref": "BQT:2381",
   "status": "supports",
   "note": "s.v. هنگ (ref_page.py BQT:2381): Pur-Davud's list 'هنگ (= آهنگ)، هنجیدن، ... آهنجیدن ... فرهختن ...' from Av. θang 'کشیدن'. Does not include هنجار."
  },
  {
   "ref": "BQT:2376",
   "status": "contradicts",
   "note": "For hanjār only: BQT_v4_pages.txt [pdf 459] s.v. هنجار, Mo'in's fn.: 'درسانسکریت saṃcāra (گشتن، گردیدن، راه) «اسشق ۱۱۶۹»' — a different etymology from θang (quoted also by Dehkhoda on abadis: 'در سنسکریت سمکارا به معنی گشتن و گردیدن و راه است (حاشیه برهان چ معین)')."
  },
  {
   "ref": "SNS:126",
   "status": "partial",
   "note": "SNS index: 'frahang 126/1' — Tavoosi p.126 treats MP frahang; page OCR illegible, so only the headword is confirmed."
  },
  {
   "ref": "FFD:28",
   "status": "not_checked",
   "note": "Abolghasemi, Fe'l-ha-ye Farsi-ye Dari: PDF listed in refs_online.json but not consulted for this page."
```


## [2026-10-16T05:13:30.071Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','AHD','HRN','HUB','MON','BQT','TAD','FVQ','AEF','AMD','BRT','WLD']:\n  v=d.get(k); print('==',k); [print(' ',kk,':',str(vv)[:600]) for kk,vv in v.items() if kk in ('lookup_hint','page_offset','local_file','scans')]\n\""
}
```


### [2026-10-16T05:13:30.375Z] TOOL RESULT

```
== POK
  local_file : /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt
  page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
== AHD
  local_file : /home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt
  page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 
== HRN
  local_file : /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt
  page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== HUB
  local_file : /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt
  page_offset : leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== MON
  lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a
  local_file : ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
  page_offset : None
== BQT
  lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh
  local_file : ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sou
  page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (
  scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': 
== TAD
  lookup_hint : Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
  local_file : ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD.txt']
  page_offset : 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
== FVQ
  lookup_hint : Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
  local_file : ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt']
  page_offset : printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
== AEF
  lookup_hint : Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه‌شناختی فارسی' (Mehrafarin), also not online.
  local_file : None
  page_offset : None
== AMD
  lookup_hint : Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable.
  local_file : None
  page_offset : None
== BRT
  local_file : /home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt
  page_offset : Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== WLD
  local_file : ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt
  page_offset : Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
  lookup_hint : Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
```


## [2026-10-16T05:13:33.997Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'lemma: weid\\|lemma: u̯eid\\|lemma: ueid' POK_full.txt | head; grep -n '^weid-\\|^weid' AHD_watkins1985.txt | head"
}
```


### [2026-10-16T05:13:34.565Z] TOOL RESULT

```
89176:Root / lemma: ueid-1
```


## [2026-10-16T05:13:37.415Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89176,89330p POK_full.txt"
}
```


### [2026-10-16T05:13:37.730Z] TOOL RESULT

```
Root / lemma: ueid-1 

Meaning: to turn, bend 

Note: extension from *uei- ds. 

Material: Old Indie veda-m. " tussock of strong Grases, besenformig gebunden, zum 

Fegen etc.'; hom. i5v6opai "bend myself, krumme myself (from a *Fi5-v6-(; "gebogen'); 

Latin K/o'^/i/5 "geflochtener basket'; Latvian vld/natl\ax, wattle, braid'. 

References: WP. I 236, WH. II 785. 

Page(s):1124 

Root / lemma: u(e)id-2 
Meaning: to see; to know 



Grammatical information: (originally Aorist), Zustandsverbum u(e)ide(i)-, nasalized ui-n-d-, 
Perf. uoid-a-have seen, white', whence die meaning ' know, have knowledge of ' also auf 
other forms iJbertragen wurde; from the meaning " behold ' derives 'find' 
l\1aterial: A. Old Indie vetti, vidmasi vidantT know, have knowledge of ' (present reshuffling 
of Perf. veda vidma), vedate {a\so), vidati {a\so) " know, have knowledge of, Perf. veda 
vidma. Opt. vidyat, participle vidvan; Avestan vaeda vTdare, Opt. vTdyal, vTdva' know, have 
knowledge of (the meaning "see' in aiwi. vlsdm^haye wahrgenommen', pa/t/. vTsam 
"wurde aware', /^5i/d/zo'J/77"nehmt wahr'); /oparticiple Old Indie vitta- " recognized, known', 
Avestan vista- "known as' and Old Indie vidita- (probably to basis *uidei-)\ Inf. Old Indie 
vidmane{= gr. iSpsvai) " know, have knowledge of, Gatha-Avestan vTdvanor, Kaus. Old 
Indie i/eo'aya//" allows know, have knowledge of, kundigt an, bietet an', Avestan 
uzvae6aye/t/" aWows know, have knowledge of '; 

In the meaning "find': Old Indie vindati {vetti, vitte), avidat, viveda, vevidat, vitta-, Kaus. 
vedayati, Avestan v75aiti, vfnasti, vTvaeda, voivldait/ [Kon].), Kaus. vaedaye/ti' allows 
attain, makes teilhaftig', participle K/s/a-"(vor)gefunden, vorhanden'; die separation from 
den forms the meaning "see, know, have knowledge of ' is not quite sharp durchzufiJhren, 
compare Old Indie vindati ^\Nh\te', South Baluchi gindag'see'; 

Armenian e^//"erfand' (= Old Indie avidat, gr. sFiSs), gtaneml\n6'; reshaped from Perf. 
*uoidag/tem'\ know' (/from or, in addition get, g/taic, gitun^\N'\ssend, wise'); results of 
nasal present (= Old Indie vindati, Irish finn-, see below) perhaps in Armenian ^/>7/"profit, 
gain', if from *uind; 

Gr. £i5ofjai "erseheine, scheine, gebe mir den Anschein'; oi5a "white', i5|j£v, Konj. £i5u), 
participle zibudc, (*F£i5-), i5uTa; Aor. £l5ov (£Fi5ov) "sah', i5£Tv (: Old Indie avidat, Armenian 
egit), participle a-xaioo,, Igteov; gr. 'Ai'5r|c;, Attic "Ai5r|c; probably a-Fi5- "unsichtbar, not 
anzusehen' s. lastly Frisk 33 f.; nasalized iv5aAAo|jai "erseheine, zeige myself; gleiche'; 

also Celtic k//7o'o- "white' (Old Irish find, cymr. gwynn, (common Celtic -ns-, -nt- > -nn-), 
gall. PN Vindomagus, -bona); 

Latin video, -ere'see' (from the basis *u{e)ide-, compare Old Church Slavic videti 
Lithuanian pavydeti, Gothic witan, -a/da 'observe' etc., and with zero grade *u(e)idT-Vc\e 2. 
syllable Old Church Slavic present viditt, Lithuanian pavydime, Latin vTdi-s-tT, Old Indie 
Aor. avedJt, vedi-tar-, vedi-tum, vidi-ta-; Umbrian u/rseto Wsa' or "visum', auirseto 
"unsichtbar': Latin videre= tacitus: tacere), Perf. vTdT{= Old Church Slavic vede), participle 
vTsus {as vTsus, -i/s"das Sehen, sight' with /"for /after vTdTav\6 vTso); 



Latin vfso, -e/'e'besuchen' (i.e. "to selien wisli'), Umbrian /lei/es/^'revisito' {*ueid-s-d); 
similarly Gothic gaweison. Old Saxon Old High German M//sd/7'besuchen'; 

Old Irish ad-ffadat^s\e erzahlen' (etc.); compounds unseres Verbs are do-adbaV qx 
shows', do-adbadar^WK(i gezeigt', as-zM-e/ 'expounded'; nasal present (see above Old 
Indie vindati) nad-finnatar^s\e wissen nicht', /'c»/^/7/7ao''a/'"pflegt to wissen' {*ui-n-d-na-), 
(common Celtic -ns-, -nt- > -nn-), as-fenimm, doaisbena^ '^oiuis, shows, evinces, shows' 
(from *uid-na-) mcymr. 1. Sg. gwnn, corn, gon. Middle Breton gounl know' (die weiteren 
brit. Prasensformen, e.g. 2. Sg. mcymr. gwydost, gwdost, 1. PI. ncymr. gwyddom, are 
against it of Perf. derive ); Perf. Old Irish rofetar'\ know', AO/^/f/A'er white' = cymr. gwyr 
{*uid-rai)\ Old Irish Ao/ess "scitum est' {*uid-to-m, compare also fiss, ncymr. gwys^6as 
Wissen' from *uid-tu-s), /fess'scita' (PI. neutr.), mcymr. gwyss. Middle Breton ^0^5'wurde 
gewuftt'; Old Irish toTsech, cymr. /yi^yso^ "guide, leader' {*to-uissakos. Ogam Gen. 
TOVISACI), Old Irish tOus^ beginning ', cymr. /ynys 'guide, lead' {*to-uissus, Indo 
Germanic *-uid-tus)\ here probably also Old Irish fold- 'send', e.g. 3. PI. fdidit{= Old Indie 
vedayati. Old Icelandic veita6s)\ Old Irish /^o'o 'master, mister' {* ueidont-s); 

Gothic fraweitan' avenge ' ('animadvertere'). Old High German /^/w/zza/? 'tadeind 
vorwerfen, verweisen', ty/2za/7'bemerken, look out auf. Old Saxon Old English wTtan 
'reproach, rebuke, reproach' (therefrom Old Icelandic i//7/n. Old English wTte, Old Saxon 
wTti, Old High German wTzziv^. ' punishment '), Gothic in-weitan^6\e worship, veneration 
prove'; with ostentatious meaning-development Old English gewTtan' leave, depart, die'. 
Old Saxon giwTtan^Qo\ Old High German (Hildebrandlied) ^/Vvez/'er walked ', (Tatian) 
arawTzan^6\sce6e'ce'\ Gothic /^/>we'/^5/7'gespannt hinblicken auf, perhaps zur basis auf -e: 
-7-, as certainly die e-verbs Gothic witan, -a/io''a 'auf etwas sehen, observe'. Old Icelandic 
only participle i///5d/''beobachtet, bestimmt'. Old English (be)witian^be\xach{ev\, decide, 
define, ordain, determine'; preterit present Gothic wait, w/fum^know, we know, have 
knowledge of (Inf. w/tan, participle M///a/7o(s neologism). Old Icelandic veit vitum {vita, 
vissa) ' know, have knowledge of, also 'bemerken, erforschen, indicate, gerichtet sein 
after, look after, go after'. Old English wat, witon {witan, wisse wiste). Old High German 
weiz, wizzumes {wizzan, wissa, wessa) ' know, have knowledge of nominalized participle 
Gothic weitwdl=>s^ witness, testifier' (: eiSux;, iSuTa ' witness, testifier'); /oparticiple Gothic 
^/7by/ss'ungewifl', Old High German giwis{s). Old Saxon Old English wiss^ certainly ' (Old 
Icelandic K/ssa'Gewiftheit'); Kaus. Old Icelandic i/e//5 'grant, leisten, help; also Wasser in 
eine Richtung leiten'. Old High German weizen 'show, beweisen'; to FiSeTv seems as 
Injunktiv Old English wuton{mVc\ folgendem Inf.) from *witon^\a^\. uns' (older 'laftt uns 
zusehen, tendamus') to belong; 



Lithuanian ve/zdm/ {ior *ve/c/m / aiter 6em Imper. Old Lithuanian veizdi= *ueid-6^i, 
compare Old Indie viddhf), veizdeti^see, hinblicken', pavydziu, -vyd/me -vydef/^\nv\6ere' 
(see o); of old Perf.from Old Prussian waisei, wa/sse^6u weiftt' (= Old Church Slavic ves/) 
waidimai^ we know, have knowledge of, Inf. waist. Old Church Slavic iz/zo'lp, vidisi, videti 
"see', previous Perf. Med. vede{= Latin i/zoTwhite'), present reshaped vemb, vedetT 
know, have knowledge of '; povedeti^ know, have knowledge of let' (probably reshuffling 
eines Kaus. *uoideJd, Slavic *vediti, after vedeti^ know, have knowledge of); izvest-b 
"known, certainly '. 

B. nominal formation: 

root nouns Old Indie -vid- "kennend, expert, skillful' (e.g. asvavid-), Avestan vTd- 
"teilhaftig'; gr. vp-ic;, -iboc, "ignorant'; 

Gothic unwita. Old High German i//7w/zzc>"Unwissender', Old High German forawizzo 
"praescius'. Old English by//5"weiser man, Ratgeber', gewita^ witness, testifier'. Old High 
German ty/zzo "weiser man', giwizzo^ witness, testifier ' post-verbal e/7-stem; but Old Irish 
ffadu^ witness, testifier ' ( *ueid-udt-s) secondary />stem; 

Old Indie vida^ knowledge ', cymr. etc. gweddi. "sight, apparition'; Old Indie vidya 
"Wissen, doctrine', Avestan vidya 6s.\ Old Irish airdeu. "mark, token, sign' {*[p]ari-vidJom) 
= cymr. arwydd rr\. ds.. Old Saxon giwitt. Old High German {gi)wizzin. "Wissen, reason'. 
Old English [^///"reason, Besinnung', Gothic unwitiu. "Unwissenheit, Unverstand', 
compare also Old High German wizzTi. "Wissen, reason, Besinnung' in addition Old High 
German gi-, ir-wizzen look out' (Modern High German Witzxr\.), Middle Low German witte 
f. ds.; 

es-stem: Old Indie vedasn. " knowledge, Umsicht, sacred Schrift', gr. £i5o(; n. " 
appearance, shape', Lithuanian veidas^ front ' (to glottal stop see below). Old Church 
Slavic vidi3 (serb. vid) "sight, appearance ' (from ehemaligen Neutra), so probably also: 
Middle Irish ffadm. "Ehrenbezeigung', Old Irish ffad {* ueidos) with Dat. "coram', cymr. 
yngwydd6s., gwydd^ kvmeseuheW! , Middle Breton a goez, nbret. 5c77c»^ez"offenlich' 
("angesichts'); cymr. ad-wydd^cr\}e\, savage', gwar-adwydd^\v\su\\!\ other formations in 
Gothic ^/7M/e/s "ignorant, ungebildet', /^//5M/e/s"vollkommen weise'. Old Icelandic vTss, Old 
High German Old Saxon Old English bv/5"wise' {*ueid-s-o-). Old High German wTs(a)^{* 
appearance =) kind of, way'. Old English wTs(e) "way, state, status, direction'. Old Icelandic 
pd/z/K/s "different', perhaps also iSsa "outer apparition, shape, sight' (if *Fi5£ac(); 

gr. i5pic;, -loc; "wissend, expert, skillful ', Old Icelandic i////'"sensible, wise'; 



gr. (horn.) £i5aAi|jO(; "beautiful from Gestalt', siSaAAsrai cpaivsrai Hes., due to eines 
*£i5aAo- wherefore with suffix vowel gradation siSwAov "shape', a£i5£Ao(; "unsichtbar'; 
Lithuanian va/da/as ' appar'\t\or\' , pav/cfa/as ' shape' {*-elo-)\ gr. £i5uAi(;, -iSoc; "siSuTa, 
sniGTHpajv', Old Indie vidura-^ smari, sensible, wise', Lithuanian yC>ai//o'^//s"Ebenbild', akies 
pavydulis. Old Prussian weydulis' eyeball', Gothic /&/>we///"Schauspier; 

Old Indie vidman- m. " wisdom ' (compare also Inf. vidmane, i5|j£vai), gr. i5pu)v, -oyoc, 
"expert, skillful'; \b\xx\y cppovnaiv Hes.; 

gr. iGTCjop, Attic TaTOjp, Boeotian Fiarajp "wissend, expert, skillful; Schiedsrichter', 
ioTopeTv "erkunden', iaropia " occurrence ';
```


## [2026-10-16T05:13:43.153Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89330,89400p POK_full.txt | grep -n -i 'Page\\|WP\\|ui-n-d\\|uid-\\|pazu\\|paiti' ; grep -n -i '^ *weid-\\|^weid' AHD_watkins1985.txt | head; grep -n 'weid-' AHD_watkins1985.txt | head"
}
```


### [2026-10-16T05:13:43.480Z] TOOL RESULT

```
13:References: WP. I 236 ff., WH. II 784 f., Trautmann 338, 357 f., Vasmer 1, 176 ff., 192, 
15:Page(s): 1125-1127 
40:References: WP. II 232, WH. II 782; 
44:Page(s):1128 
369:*dru-ko- in Germanic *trugaz in Old English trog, wooden vessel, tray: TROUGH. 5. Suffixed zero-grade form *dru-mo- in Germanic *trum- in Old English trum, firm, strong (> trymman, to strengthen, arrange): TRIM. 6. Variant form *derw- in Germanic *terw- in Old Eng- lish fe(o)ru, resin, pitch (obtained from the pine tree): TAR}. 7. Suffixed variant form *dri-ro- in Latin diirus, hard (of whose English derivatives many represent a semantic cross with Latin dirdre, to last long; see deue-): DOUR, DURAMEN, DURESS, DURUM; (DURA MA- TER), ENDURE, INDURATE, OBDURATE. 8. Lengthened zero-grade form *dré- in Greek drus, oak: DRUPE, DRYAD; GERMANDER, HAMADRYAD. 9. Reduplicated form *der-drew-, dissimilated with suffix in *den-drew- on in Greek dendron, tree: DENDRO-, DENDRON; PHILO- DENDRON, RHODODENDRON. 10. Celtic compound *dru-wid-, “knower of trees” (*wid-, to know; see weid-), the Celtic priestly caste, associated with a tree-cult, probable source of Latin druides, druids: DRUID. 11. O-grade form *doru- in Sanskrit daru, wood, timber: DEODAR. [Pok. deru- 214.]
1043:swei-2. To bend, turn. 1. Germanic o-grade form *swaip- in Old English swdpan, to sweep, drive, swing: swoop. 2. Germanic zero-grade form *swip- in Old English swift, swift, quick (< “turning quickly”): swirtT. 3. Germanic full-grade form *swif- in Middle English swyvel, a swivel: SWIVEL. 4. Possibly Germanic *swih- in Middle Dutch swijch, bough, twig: SWITCH. 5. German schwappen, to flap, splash, akin to the source of Middle English swap- pen, to splash: swaP. [Pok. swei- 1041.] sweid-'. To shine. Possible suffixed form *sweid-es- in: a. Latin sidus, constellation, star: SIDEREAL; b. Latin augury terms considerdre, to examine, “observe the stars carefully” (con-, intensive prefix; see kom), and déside- rare, to long for, investigate (formed on analogy with considerdre; dé-, from; see de-): CONSIDER, DESIRE. [Pok. 1. sueid- 1042.] sweid-2. Sweat; to sweat. I.O-grade form *swoid-. 1. Germanic *swaitaz, sweat, with its denominative *swaitjan, to sweat, in Old English sw&tan, to sweat: SWEAT. 2. Suffixed form *swoid-os- in Latin sidor, sweat: SUDORIFIC; SUDORIFEROUS. 3. O-grade form *swoid-d- in Latin siddre, to sweat: SUDATORIUM, SUINT; EXUDE, TRANSUDE. II. Suffixed zero-grade form *swid-r-os- in Greek hidrds, sweat: HIDROSIS. [Pok. 2. sueid- 1043.]
1096:5. Greek trias, the number three: TRIAD. 6. Greek trikha, in three parts: TRICHOTOMY. 7. Greek compound triérés, galley with three banks of oars, trireme (-érés, oar; see era-'): TRIERARCH. 8. Suffixed form “*tri-to- in Greek tritos, third: TRITIUM; TRITANOPIA. 9. Compound form *tri-pl-, “threefold” (*-pl- < combining form *-plo-; see pel-3), in Greek ¢triploos, triple: TRIPLE. 10. Compound form *tri-plek-, “threefold” (*-plek-, -fold; see plek-), in Latin triplex, triple: TRIPLEX. 11. Compound form *tri-st-i, “third person standing by” (see sta-), in Latin testis, a witness: TESTAMENT, (TESTIMONY); ATTEST, CONTEST, DETEST, OBTEST, PROTEST, TESTIFY. 12. Per- sian si, three: straR. III. Extended zero-grade form “iris, “thrice.” 1. Latin ter, thrice: TERN?; TERPOLYMER. 2. Greek tris, thrice: TRISOCTAHEDRON. 3. Suffixed form *tris-no- in Latin trini, three each: TRINE, (TRINITY). IV. Suffixed o-grade form *troy-o- in Russian troje, three: TROIKA. [Pok. trei- 1090.] trem-. To tremble. Possibly related to trep-' and tres- through a hypothetical base *ter-. Latin tremere, to shake, tremble: TREMENDOUS, TREMOR, TREMULOUS. [Pok. trem- 1092.] trep-'. To tremble. Possibly related to trem- and tres- through a hypothetical base *ter-. Latin trepidus, agi- tated, alarmed: TREPID; INTREPID. [Pok. 1. trep- 1094.] trep-2. To turn. 1. Greek trepein, to turn: -TROPOUS; APOTROPAIC, TREPONEME. 2. O-grade form *trop- in: a. suffixed form *trop-o- in Greek tropos, a turn, way, manner: TROPE, TROPO-, TROVER; CONTRIVE, (RE- TRIEVE); b. suffixed form *trop-d- in Greek tropé, a turning, change: TROPHY, TROPIC; ENTROPY. [Pok. 2. trep- 1094.] tres-. To tremble. Possibly related to trem- and trep-1 through a hypothetical base *ter-. Metathesized form *ters- in o-grade suffixed (causative) form *tors-eyo- in Latin terrére, to frighten (< “to cause to tremble”), with vowel e from terror (< *ters-os-), terror: TERRIBLE, TERROR; DETER, TERRIFIC. [Pok. tres- 1095.] treud-. To squeeze. 1. Suffixed o-grade form *troud-o- in Germanic *thrautam in Old English thréat, oppression, use of force: THREAT. 2. Variant form *trid- in Germanic “thristjan in Old Norse thrysta, to squeeze, compress: THRUST. 3. Latin tridere, to thrust, push: ABSTRUSE, EXTRUDE, INTRUDE, OBTRUDE, PROTRUDE. [Pok. tr-eu-d 1095.] trozdo-. Thrush. 1. Germanic *thrust- in Old English throstle, thrush: THROSTLE. 2. Germanic *thruskj6n- in Old English thrysce, thrush: THRUSH}. 3. Zero-grade reduced form *trzdo- in Latin turdus, thrush: STURDY. 4. Perhaps altered in Greek strouthos, sparrow, ostrich: STRUTHIOUS; (OSTRICH). [Pok. trozdos 1096.] tu-. Second person singular pronoun; you, thou. 1. Lengthened-grade form “ti (accusative “te, *tege) in Germanic *thii (accusative *theke) in Old English thi (accusative thec, thé), thou: (THEE), THOU!. 2. Suffixed extended form *éwjei-no- in Germanic *thinaz in Old English thin, thine: THINE, THY. [Pok. tu- 1097.] twei-. To agitate, shake, toss. 1. Extended form *tweid- in Germanic *thwit- in: a. Old English thwitan, to strike, whittle down: WHITTLE; b. Middle Dutch duit, a small coin (? < “piece cut or tossed off”): DorT. 2. Extended form *tweis- in Greek seiein, to shake: SEISM, SISTRUM. [Pok. 2. tuei- 1099.] twengh-. To press in on. Germanic *thwang- in: a. Old English thwong, thwang, thong, band (< “constraint”): THONG; b. by-form *twangjan in Old English twengan, to pinch: TWINGE. [Pok. twengh- 1099.] twer-', To turn, whirl. Zero-grade *tur-. I. Variant form *stur-. 1. Suffixed form *stur-mo- in Germanic *sturmaz, storm (< “whirlwind”), in Old English storm, storm: STORM. 2. Germanic *sturjan in Old English styrian, to move, agitate: STIR!. II. Suffixed form *tur-bd in Greek turbé, tumult, disorder (> Latin turba, disorder, turbé, spinning top, and turbdre, to confuse, disorder): (TROU-
1128:wed-2, To speak. 1. Possibly oldest root form *awed- becoming *awed- in reduplicated form *awe-ud- dissimi- lated to *aweid-, with suffixed o-grade form *awoid-o- respectively in Greek aeidein (Attic aidein), to sing, and aoidé (Attic didé), song, ode (but more likely a separate root *aweid- becoming Greek *aweid-, to sing): ODE; COMEDY, EPODE, HYMNODY, MELODY, MONODY, PARODY, RHAPSODY, TRAGEDY. 2. Sanskrit vddah, sound, state- ment: THERAVADA. [Pok. 6. au- 76.]
1135:Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1285:BELLONA duellum BELLOW bhel-4 BELLOWS bhelgh- BELLY bhelgh- BELONEPHOBIA gvel-! BELUGA bhel-1 BELVEDERE deu-2, weid- BEMA gWa-
1369:CLAIM kele-2 CLAIRVOYANCE kele-2, weid- CLAMANT kele-2 CLAMMY gel-1 CLAMOR kele-2 CLAM!  gel-1 CLAM? = gel-1 CLAMP gel-1
1382:COL kwel-1 COLANDER kagh- COLCANNON kaul-, weid- COLD gel-3
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
```


## [2026-10-16T05:14:06.826Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,60p tools/fetch_source.py | head -60; ls data/verification/sources/web | head; ls data/verification/sources/web | wc -l"
}
```


### [2026-10-16T05:14:07.342Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
Permissions  Size User   Date Modified Name
.rw-r--r--   5.9k sfmqrb 14 Oct 22:15  0a00a434bf92e870.txt
.rw-r--r--   3.8k sfmqrb 14 Oct 22:15  0a088dfc130a5323.txt
.rw-r--r--    27k sfmqrb 14 Oct 22:15  0a1aca379903ce30.txt
.rw-r--r--    15k sfmqrb 14 Oct 22:15  0a2b71d06c5962d3.txt
.rw-r--r--   6.4k sfmqrb 14 Oct 22:15  0a3a255f8587a9a4.txt
.rw-r--r--   9.3k sfmqrb 14 Oct 22:15  0a6a37cf6c73cf18.txt
.rw-r--r--   9.0k sfmqrb 14 Oct 22:15  0a7ac71daf0bd129.txt
.rw-r--r--    14k sfmqrb 14 Oct 22:15  0a75a7cbfd555b2b.txt
.rw-r--r--   6.3k sfmqrb 14 Oct 22:15  0a411ea5b813ed0c.txt
5774
```


## [2026-10-16T05:14:13.815Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyd-' \\\n 'https://en.wiktionary.org/wiki/هویدا' \\\n 'https://en.wiktionary.org/wiki/اوستا' \\\n 'https://en.wiktionary.org/wiki/پژوهیدن' \\\n 'https://en.wiktionary.org/wiki/پژوهش' \\\n 'https://en.wiktionary.org/wiki/اسطوره' \\\n 'https://en.wiktionary.org/wiki/أسطورة' \\\n 'https://en.wiktionary.org/wiki/penguin' \\\n 'https://www.etymonline.com/word/penguin' \\\n 'https://www.etymonline.com/word/guide' \\\n 'https://www.etymonline.com/word/television' \\\n 'https://www.etymonline.com/word/video' \\\n 'https://www.etymonline.com/word/history' \\\n 'https://www.etymonline.com/word/visit' \\\n 'https://en.wiktionary.org/wiki/پنگوئن' \\\n 'https://en.wiktionary.org/wiki/تلویزیون' \\\n 'https://en.wiktionary.org/wiki/ویزیت' \\\n 'https://en.wiktionary.org/wiki/ویدیو' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wītaną' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wissaz' \\\n 'https://en.wiktionary.org/wiki/ἵστωρ' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wáydati' ; do echo \"$u\"; python3 tools/fetch_source.py \"$u\" --note 'page 534, root Weid: etymology check'; done 2>&1"
}
```


### [2026-10-16T05:14:23.838Z] TOOL RESULT

```
Exit code 1
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyd-
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2a3a5a1cb421b58e.txt
https://en.wiktionary.org/wiki/هویدا
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cc745ec05bfafb34.txt
https://en.wiktionary.org/wiki/اوستا
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9d0ee85cfba26942.txt
https://en.wiktionary.org/wiki/پژوهیدن
/home/sfmqrb/git/rishe-private/data/verification/sources/web/64fbc90f30d1b5c0.txt
https://en.wiktionary.org/wiki/پژوهش
/home/sfmqrb/git/rishe-private/data/verification/sources/web/86db0240d9966c04.txt
https://en.wiktionary.org/wiki/اسطوره
/home/sfmqrb/git/rishe-private/data/verification/sources/web/92cb5f047cf21151.txt
https://en.wiktionary.org/wiki/أسطورة
/home/sfmqrb/git/rishe-private/data/verification/sources/web/17a0d5f17bc4c6bd.txt
https://en.wiktionary.org/wiki/penguin
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cc4f19202101e879.txt
https://www.etymonline.com/word/penguin
/home/sfmqrb/git/rishe-private/data/verification/sources/web/292250ecaec846b9.txt
https://www.etymonline.com/word/guide
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f1f7d223f190f00a.txt
https://www.etymonline.com/word/television
/home/sfmqrb/git/rishe-private/data/verification/sources/web/02a8de82b17f5603.txt
https://www.etymonline.com/word/video
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a635a86b7d2c8289.txt
https://www.etymonline.com/word/history
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e11097805e17b650.txt
https://www.etymonline.com/word/visit
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f524e4a4ba27cc36.txt
https://en.wiktionary.org/wiki/پنگوئن
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2df9f4c3edfb71f7.txt
https://en.wiktionary.org/wiki/تلویزیون
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7a4fdff721dedbc0.txt
https://en.wiktionary.org/wiki/ویزیت
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5cfb348f710c9d0d.txt
https://en.wiktionary.org/wiki/ویدیو
/home/sfmqrb/git/rishe-private/data/verification/sources/web/141de02622fde0d0.txt
https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wītaną
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ba39d325e6e9bd1c.txt
https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wissaz
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ea4f4c10742e89e6.txt
https://en.wiktionary.org/wiki/ἵστωρ
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9e4aecd45ece45f3.txt
https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wáydati
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ed96913d7778d239.txt
```


## [2026-10-16T05:14:26.702Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -40 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l)\n  if 'page 534' in d.get('note',''): print(d['status'],d['bytes'],d['url'],d['file'])\""
}
```


### [2026-10-16T05:14:27.042Z] TOOL RESULT

```
200 3529 https://en.wiktionary.org/wiki/پژوهش data/verification/sources/web/86db0240d9966c04.txt
200 4940 https://en.wiktionary.org/wiki/اسطوره data/verification/sources/web/92cb5f047cf21151.txt
200 4984 https://en.wiktionary.org/wiki/أسطورة data/verification/sources/web/17a0d5f17bc4c6bd.txt
200 18931 https://en.wiktionary.org/wiki/penguin data/verification/sources/web/cc4f19202101e879.txt
-1 39 https://www.etymonline.com/word/penguin data/verification/sources/web/292250ecaec846b9.txt
-1 39 https://www.etymonline.com/word/guide data/verification/sources/web/f1f7d223f190f00a.txt
-1 39 https://www.etymonline.com/word/television data/verification/sources/web/02a8de82b17f5603.txt
-1 39 https://www.etymonline.com/word/video data/verification/sources/web/a635a86b7d2c8289.txt
-1 39 https://www.etymonline.com/word/history data/verification/sources/web/e11097805e17b650.txt
-1 39 https://www.etymonline.com/word/visit data/verification/sources/web/f524e4a4ba27cc36.txt
200 3283 https://en.wiktionary.org/wiki/پنگوئن data/verification/sources/web/2df9f4c3edfb71f7.txt
200 2957 https://en.wiktionary.org/wiki/تلویزیون data/verification/sources/web/7a4fdff721dedbc0.txt
-1 39 https://en.wiktionary.org/wiki/ویزیت data/verification/sources/web/5cfb348f710c9d0d.txt
200 3360 https://en.wiktionary.org/wiki/ویدیو data/verification/sources/web/141de02622fde0d0.txt
200 5563 https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wītaną data/verification/sources/web/ba39d325e6e9bd1c.txt
200 4572 https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wissaz data/verification/sources/web/ea4f4c10742e89e6.txt
200 4820 https://en.wiktionary.org/wiki/ἵστωρ data/verification/sources/web/9e4aecd45ece45f3.txt
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wáydati data/verification/sources/web/ed96913d7778d239.txt
```


## [2026-10-16T05:14:30.341Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep 'page 534' index.jsonl | head -4 | cut -c1-200; for f in 2a3a5a1cb421b58e cc745ec05bfafb34 9d0ee85cfba26942 64fbc90f30d1b5c0 86db0240d9966c04 92cb5f047cf21151 17a0d5f17bc4c6bd; do echo \"=== $f\"; grep -v '^\\s*$' $f.txt | grep -i -A12 'Etymology' | head -40; done"
}
```


### [2026-10-16T05:14:30.785Z] TOOL RESULT

```
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyd-", "file": "data/verification/sources/web/2a3a5a1cb421b58e.txt", "fetched": "2026-10-16T05:14:14Z", "status": 200, "byte
{"url": "https://en.wiktionary.org/wiki/هویدا", "file": "data/verification/sources/web/cc745ec05bfafb34.txt", "fetched": "2026-10-16T05:14:15Z", "status": 200, "bytes": 3152, "title": "هویدا - Wiktion
{"url": "https://en.wiktionary.org/wiki/اوستا", "file": "data/verification/sources/web/9d0ee85cfba26942.txt", "fetched": "2026-10-16T05:14:15Z", "status": 200, "bytes": 5639, "title": "اوستا - Wiktion
{"url": "https://en.wiktionary.org/wiki/پژوهیدن", "file": "data/verification/sources/web/64fbc90f30d1b5c0.txt", "fetched": "2026-10-16T05:14:16Z", "status": 200, "bytes": 8809, "title": "پژوهیدن - Wik
=== 2a3a5a1cb421b58e
=== cc745ec05bfafb34
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Adjective 
 Toggle the table of contents 
 هویدا 
 5 languages 
 فارسی 
 Kurdî 
 Malagasy 
 Русский 
 Türkçe 
--
 Etymology
 [ edit ] 
 Unknown.
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /hu.waj.ˈdaː/ 
 ( Dari, formal ) IPA ( key ) : [hʊ.wäj.d̪ɑ́ː] 
 ( Dari, formal ) IPA ( key ) : [hʊ.wäj.d̪ɑ́ː] 
 ( Kabuli ) IPA ( key ) : [ʔʊ.wäj.d̪ɑ́ː] 
 ( Hazaragi ) IPA ( key ) : [ʔu.wäj.d̪ɔ́ː] 
 ( Iran, formal ) IPA ( key ) : [ho.vej.d̪ɒ́ː] 
 ( Tajik, formal ) IPA ( key ) : [hu.väj.d̪ɔ́] 
 Rhymes: -aː 
=== 9d0ee85cfba26942
 Etymology 1 
 1.1.1 
 Pronunciation 
 1.1.2 
 Proper noun 
 1.1.2.1 
 Alternative forms 
 1.2 
 Etymology 2 
 1.2.1 
 Pronunciation 
 1.2.2 
 Noun 
 1.2.3 
 Adjective 
 1.3 
 References 
 Toggle the table of contents 
 اوستا 
 6 languages 
 فارسی 
--
 Etymology 1
 [ edit ] 
 Inherited from Middle Persian [Book Pahlavi needed] ( ʾp(y)stʾk' /⁠abestāg⁠/ ) . Of unknown meaning, but probably from Avestan ; possibly *𐬎𐬞𐬀𐬯𐬙𐬁𐬬𐬀𐬐𐬀 ( *upastāvaka , “ praise ” ) , from 𐬎𐬞𐬀𐬯𐬙𐬀𐬊𐬌𐬙𐬌 ( upastao i ti , “ he praises ” ) , from -𐬎𐬞𐬀 ( -upa , “ up to, at ” ) << Proto-Indo-Iranian *(s)upamás << Proto-Indo-European *upó + 𐬯𐬙𐬀𐬊𐬌𐬙𐬌 ( stao i ti , “ he praises ” ) (see Sanskrit स्तुति ( stuti , “ praise ” ) ), though this is not actually attested in any Avestan texts.
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ʔa.wis.ˈtaː/ , /ʔa.was.ˈtaː/ 
 ( Dari, formal ) IPA ( key ) : [ʔä.wɪs.t̪ʰɑ́ː] , [ʔä.wäs.t̪ʰɑ́ː] 
 ( Dari, formal ) IPA ( key ) : [ʔä.wɪs.t̪ʰɑ́ː] , [ʔä.wäs.t̪ʰɑ́ː] 
 ( Kabuli ) IPA ( key ) : [ʔä.wɪs.t̪ʰɑ́ː] , [ʔä.wäs.t̪ʰɑ́ː] 
 ( Hazaragi ) IPA ( key ) : [ʔä.wis.t̪ʰɔ́ː] , [ʔä.wäs.t̪ʰɔ́ː] 
 ( Iran, formal ) IPA ( key ) : [ʔæ.ves.t̪ʰɒ́ː] , [ʔæ.væs.t̪ʰɒ́ː] 
 ( Tajik, formal ) IPA ( key ) : [ʔäwes.t̪ʰɔ́] , [ʔä.väs.t̪ʰɔ́] 
 Rhymes: -aː 
--
 Etymology 2
 [ edit ] 
 See the etymology of the corresponding lemma form.
 Pronunciation
=== 64fbc90f30d1b5c0
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Verb 
 1.3.1 
 Conjugation 
 1.4 
 References 
 Toggle the table of contents 
 پژوهیدن 
 5 languages 
 فارسی 
--
 Etymology
 [ edit ] 
 Inherited from Middle Persian wcwstn ( /⁠wizōstan, wizōhīdan⁠/ , “ to investigate , to examine ” ) [ 1 ] . The initial 'w' phoneme most likely first turned into 'b', which is a very common sound change from Middle Persian to New Persian (change of initial w- to either b- or gw- → g-). Afterwards, the 'b' turned into a 'p' phoneme, possibly due to the ambiguities of the Perso-Arabic script at the time, which represented both 'p' and 'b' phonemes with one letter, i.e. ب . This sound change is also seen in other New Persian words such as پوزش ( pôzeš , “ apology ” ) and پزشک ( pizišk , “ doctor ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /pi.ʒoː.hiː.ˈdan/ , /pi.ʒuː.hiː.ˈdan/ 
 ( Dari, formal ) IPA ( key ) : [pʰɪ.ʒoː.ɦiː.d̪án] 
 ( Dari, formal ) IPA ( key ) : [pʰɪ.ʒoː.ɦiː.d̪án] 
 ( Kabuli ) IPA ( key ) : [pʰɪ.ʒoː.jiː.d̪án] 
 ( Hazaragi ) IPA ( key ) : [pʰi.ʒu.ji.d̪án] 
 ( Iran, formal ) IPA ( key ) : [pʰe.ʒuː.ɦiː.d̪ǽn] , [pʰæ.ʒuː.ɦiː.d̪ǽn] 
 ( Tajik, formal ) IPA ( key ) : [pʰä.ʒu.ɦi.d̪án] 
 Rhymes: -an 
=== 86db0240d9966c04
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
 Synonyms 
 1.3.2 
 Derived terms 
 Toggle the table of contents 
 پژوهش 
 7 languages 
 فارسی 
--
 Etymology
 [ edit ] 
 Etymology tree
 Persian پژوه 
 Middle Persian 𐭱𐭭 ( šn ) 
 Persian ـش 
 Persian پژوهش 
 From پژوه + ـش .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /pi.ʒoː.ˈhiʃ/ , /pa.ʒoː.ˈhiʃ/ 
 ( Dari, formal ) IPA ( key ) : [pʰɪ.ʒoː.ɦɪʃ] , [pʰä.ʒoː.ɦɪʃ] 
 ( Dari, formal ) IPA ( key ) : [pʰɪ.ʒoː.ɦɪʃ] , [pʰä.ʒoː.ɦɪʃ] 
 ( Kabuli ) IPA ( key ) : [pʰɪ.ʒoː.jɪʃ] , [pʰä.ʒoː.jɪʃ] 
 ( Hazaragi ) IPA ( key ) : [pʰi.ʒu.jiʃ] , [pʰä.ʒu.jiʃ] 
--
 Pages with etymology trees 
 Persian entries with etymology trees 
 Persian entries with etymology texts 
 Pages using etymon with no ID 
 Persian entries referencing pages with etymology sections missing etymons 
 Pages with entries 
 Pages with 1 entry 
 This page was last edited on 15 August 2026, at 21:35.
 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
 Privacy policy 
=== 92cb5f047cf21151
 Etymology 
 1.2 
 Noun 
 1.2.1 
 Descendants 
 1.3 
 Further reading 
 2 
 Persian 
 Toggle Persian subsection 
 2.1 
 Etymology 
 2.2 
 Pronunciation 
 2.3 
 Noun 
 2.3.1 
 Derived terms 
 Toggle the table of contents 
 اسطوره 
 4 languages 
 فارسی 
 Kurdî 
 Malagasy 
--
 Etymology
 [ edit ] 
 Borrowed from Arabic أُسْطُورَة ( ʔusṭūra , “ fable, myth ” ) .
 Noun
 [ edit ] 
 اسطوره • ( üstûre ) ( plural اساطیر ( esatir ) ) 
 tale , legend , myth , fable , any fictitious narrative told to excite wonder 
 Synonyms: افسانه ( efsane ) , داستان ( dasitan ) , قصه ( kıssa ) , مثل ( masal ) 
 Descendants
 [ edit ] 
 Turkish: üsture 
 Further reading
 [ edit ] 
--
 Etymology
=== 17a0d5f17bc4c6bd
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
 Declension 
 1.3.2 
 Descendants 
 1.4 
 References 
 Toggle the table of contents 
 أسطورة 
--
 Etymology
 [ edit ] 
 From phono-semantic matching of Ancient Greek ἱστορία ( historía ) , with the native Arabic سَطَرَ ( saṭara , “ to write, to compose lines ” ) .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /ʔus.tˤuː.ra/ 
 Noun
 [ edit ] 
 أُسْطُورَة • ( ʔusṭūra )  f ( plural أَسَاطِير ( ʔasāṭīr ) ) 
 myth , fable , tale , legend , story especially full of embellishments 
 609–632 CE , Qur'an , 68:15 : إِذَا تُتْلَىٰ عَلَيْهِ ءَايَـٰتُنَا قَالَ أَسَـٰطِيرُ ٱلْأَوَّلِينَ ʔiḏā tutlā ʕalayhi ʔāyātunā qāla ʔasāṭīru l-ʔawwalīna whenever Our revelations are recited to him, he says, “Ancient fables !” 
 ( chess ) bishop ( use the dual to pluralize ) 
 Declension
```


## [2026-10-16T05:14:36.233Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; grep -c . web/2a3a5a1cb421b58e.txt; grep -n -i 'Iranian\\|Avestan\\|Persian\\|vaēd\\|wáyd\\|wid' web/2a3a5a1cb421b58e.txt | head -40; grep -n -i 'paž\\|pažōh\\|pazoh\\|pežoh\\|pažuh\\|pizōh' refs/HRN.txt refs/HUB.txt | head"
}
```


### [2026-10-16T05:14:36.788Z] TOOL RESULT

```
234
165: Proto-Indo-Iranian: *Háwāytˢt ~ *Háwaytˢtan 
166: Proto-Iranian: *Háwāyst ~ *Háwaytsan ( see there for further descendants )
172: *wid-éh₁-yeti ( “ to see ” , éh₁-stative ) [ 9 ] 
173: Proto-Italic: *widēō ( “ to see ” ) 
175: *wid-é-t ( thematic root aorist ) 
179: *wóyd-e ~ *wid-ḗr ( “ to have seen, to know ” , stative ) 
188: Proto-Indo-Iranian: *wáydas 
189: Proto-Indo-Aryan: *wáydas 
192: *wéyd-ih₂ ~ *wid-yéh₂-s 
193: Proto-Indo-Iranian: *waydyáH 
201: *wéyd-ti-s ~ *wid-téy-s 
207: Proto-Indo-Iranian: 
211: *wéyd-tōr ~ *wid-tr-és ( “ viewer, witness ” ) 
213: *wéyd-tu-s ~ *wid-téw-s ( “ (act of) seeing, knowledge ” ) 
219: *n̥-wid-eh₂- 
220: Proto-Hellenic: *əwidās 
223: *n̥-wid-ḗs (<*n̥-wid-és-s)
224: Proto-Hellenic: *əwidḗs 
227: *né-wid-s 
231: *wid- mṓ [ 3 ] [ 10 ] 
235: > ? Proto-Indo-Iranian: 
239: *wid-ri-s 
240: Proto-Hellenic: *widris 
243: *wid-ró-s 
246: *wid-tó-s ( “ seen ” ) 
248: *wid-yó-s 
251: Proto-Indo-Iranian: *widyáH ( from *wid-y-éh₂ ) 
252: Proto-Indo-Aryan: *widyáH 
276: Old Prussian: widdai 
294: Proto-Indo-Iranian: *wayd- 
298: Proto-Iranian: *wayd- ( see there for further descendants )
305: ^ Cheung, Johnny ( 2007 ), “ *u̯aid¹, *u̯aid² ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , pages 408-410
```


## [2026-10-16T05:14:41.046Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==92' HRN.txt | head -80"
}
```


### [2026-10-16T05:14:41.415Z] TOOL RESULT

```
70 ~
phlv. ^patv(i)hltan , vergl. u^v(i)hTtan^ vd. 19 (16),
nv(i)himtan ^).
aw. *paitis + 1 [/'va^d-^ caeday^mi] ai. prati +
i/^ved'.
Np. h aus altem d zwischen Vokalen z. B. auch in
/'ähem aus ^svädämL Die gleiche Behandlung von d
und d (bei letzterem häufige Fälle des Übergangs in h)
zeigt, dass das d zwischen Vokalen im Persischen
ebenfalls spirantisch gesprochen wurde, daher auch
keine Scheidung im Altpersischen durch besondere
Buchstaben ; vergl. auch die allgemein durchgeführte
Spirans d bei AM., also im älteren Neupersisch, über
die Behandlung im Reim siehe Rückert, ZDM6. 8,
285, 286, 10, 263.
315. pes 'hinter, nachher, pesin 'letzter.
Käs. peCj pdc]es, pes.
ap. pasa, 'hinter', pasäva 'nachher ; aw. pasda 'nach',
paskät nachher, hinter , pasne 'hinter' ; phlv. paSj pasTn
'letzter ; ai. pagdd *hinter, nachher , pagcdt Von hinten,
hernach*.
kurd. püstve, pfisl; af/. LW. pas; oss. d. fastäge, t.
fästäg 'hinterer, nachher, zuletzt, am Ende' (280) ; bei.
pas^ Comp, pastara (287).
316. pest 'niedrig, nnoilN (Is. 2, 9; 11, 17).
ai. vergl. üpastiä, upastis 'Untergebener .
Bartholomae (briefliche Mitteilung).
LW. wa/. past, siyn. pist,
317. pistän 'Brust (der Frau)'.
a.w./stana' *Brust'; phlv. p(i)stan (vd. 9 (71)), pistän
(vd. 15 (26) 61.); ai. stdna-; arm. stin (H. No. 259).
LW. af/. pistän.
Vergl. Bartholomae, Indog. Forsch. I, 187 Anm. 2.
318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
1517 Vers 358 2), 1523 Vers 473).
*) So lese ich statt nvedlnltan.
*) An den beiden ersten SteUen vielleicht für puser zu emendireD,
doch kann bei puser wie bei pider die Izäfe fehlen, vergl. Landauer
zu S. 1517 Note 4.
```


## [2026-10-16T05:14:45.978Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==91' HRN.txt | tail -15; grep -n '314\\.' HUB.txt | head; "
}
```


### [2026-10-16T05:14:46.412Z] TOOL RESULT

```
Vers 16), pizmeranlden (Sahn. 85 Vers 433).
ap. paus bezw. aw. aiwis j- \^mar-,
piZ' Scheint wegen jüd.-pers. V\^ ein alter Fehler
für biZ" zu sein, (de Lagarde, Persische Studien,
75), doch findet sich piz- auch in pizöhiden und Ab-
leitungen (No. 314) und in pizmän (No. 312). Jeden-
falls spricht man heute p" (W o 1 1 a s t o n) ; das b
des Gazophylacium's (s. v. infracidirsi) kann
nichts beweisen. — Im Wesentlichen übereinstimmend
ist die Auffassung Nöldeke's, ZDMG. 45, 106
Anm. 3, welche ich erst nachträglich zu Gesicht
bekommen habe.
814. pizohlden 'erforschen, nachfragen*, pizöh, pizöhis^).
Reime z. B. Sahn I, 73 Vers 215, Sälin. I, 140 Vers 198. Die
Wörterbücher wissea nichts mehr voa einem Majhülvooal.
1384:314. Der Paragraph ist vollkommen verfehlt und zu streichen.
9664:p. 41, Nr. 314. Vgl. WZKM. 8, 272.
```


## [2026-10-16T05:14:49.211Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1360,1400p HUB.txt; grep -n -i 'wizō\\|wizoh\\|wcwh\\|wicoh\\|wizōy' PHD_mackenzie.txt NYB_vol2_glossary.txt CHEUNG.txt | head"
}
```


### [2026-10-16T05:14:49.578Z] TOOL RESULT

```
p. 51, Anm. 16. Von dieser Pehleviform fiihrt kein
Weg zu Fr. Muller' s (WZKM. 6, 185) zd. ^paiti-ra^d-
Verlassen*", dem doch nur np. *pairextan entsprechen
wiirde. — Arm. pahrez 'Fasten' ist einmal im 14. Jhd.
belegt.
310. Zd. pairika- schlechtweg durch *Hure' zu iibersetzen,
ist falsch. Die Pairika s sind Teufelinnen, die die
Frommen zu verfuhren und vom rechten Glauben ab-
wendig zu machen suchen; phi. parlk bose Fee'
Bdh. Gl. 108, arm. parik ein Fabelwesen' (Eznik 97, 98),
np. pari 'Fee, EngeF.
312. Die Form piSman u. s. w. ist verkiirzt aus paslman, das
auch ins Afgh. {pa§Tmcin Veuig') iibergegangen ist. Vgl.
paz. poSetnan repentant', paSSmam 'penitence' Shk. 263,
Min. Gl. 157, phi. paSSmdnlh 'Reue* Phi. Min. p. 5, Z. X5,— 41 —
Die Sanskritubersetzung giebt das paz. Wort durch
pagdnttdpin- Veuig* wieder. Es wird irgendwie zu zd.
pasda nachher und Wrzl. man *denken* gehOren und
urspriinglich *nachher-bedenkend* bedeutet haben.
313. Die von Noldeke und Horn erwahnte Form gu^s-
murdan des Judenpersischen zeigt, dass piSmurdan
'verwelken iiber alteres bizmurdan (Noldeke, ZDMG.
45, 106) auf *vizmurdan zuriickgeht. Damit fallt
Horn's Etymologic, insbesondere piz- aus patis.
314. Der Paragraph ist vollkommen verfehlt und zu streichen.
Vgl. Fr. Miiller, WZKM. 7, 371, dessen positive
Ausfiihrungen {piidh-tdan = pati + s + Wzl. von
np. justan, vgl. phi. vijustan WZKM. 8, 92) freilich
auch nicht einwandfrei sind. Ich lehne also np. piz-
aus patis (wie oben bis- aus abis) ab. Ich finde patis
auch nicht in np. paSkam^ {piskam^ baskam, biSkam)
*domu8 aestiva, aula, atrium, coenaculum, porticus =
arm. patSkam (patsgam^ patsgamb, patskamb) *Gemach,
Halle, Stockwerk*, sondern fiihre np. paSkam = arm.
patskamb auf ap. *pati-skamba~^ das ich zu zd. fra-
skemba- vd. 2, 26 ('Stiitzmauer Geldner, 'batiment
avec balcon* Darmesteter) stelle, zuriick. Im mittel-
persischen wurde *patskamb zu *paskamb, ehe pat-
(vor andern Consonanten als s, s, d) zu pai- wurde.
316. Np. past niedrig, gering' ist nicht = skr. upasti-,
das zu *bast geworden ware, sondem = *patta-y skr.
PHD_mackenzie.txt:5503:wizostan, wizoh/y- [wcwstn l , wcwd- I (J bzwb-, N piziJhidan)] examine,
PHD_mackenzie.txt:6917:investigation wizoh/yisn.                  kind (a.) mihrban.
PHD_mackenzie.txt:9926:wis6b-                          - q)    t'"U,       wizohjy-                         - ~ \C; \
PHD_mackenzie.txt:9927:wis6bisnig              \ '\) t"O t,) ~ \           wizohjyisn                    \~    .. ,<;,
CHEUNG.txt:3572:*MIDDLE PERSIAN: (+ *ui-) BMP wewd- /wizöy-/ (or /wizoh-/ ?) ‘to examine, 
CHEUNG.txt:35666:/wizoh-/, 37
```


## [2026-10-16T05:14:51.907Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3545,3590p CHEUNG.txt; grep -n -i 'u̯aid\\|\\*uaid\\|\\*uaid' CHEUNG.txt | head"
}
```


### [2026-10-16T05:14:52.245Z] TOOL RESULT

```
*NEIR: ? Pash. candal ‘to clean by shaking’ (LW ?), ? Yi. Cad-/Cast ‘to fall, stumble’. 
© On Yi. cad-/East: "Scarcely connected with Phl. Psalter cnd- ‘to shake’...", IIFL П: 
201a. 

*MISC: ? Orm. cwan-*ék ‘to shake out dust from clothes’ = cwan-/cwanók 

© In ESIJa II: 219, a root *ёапа-/ёаа- ‘to shake, swing; to be swinging, rocking’ is 
constructed and connected to Skt. skand 'to leap, to spring, to fall off', which 
derives from IE *skend- ‘to leap, jump’, Lat. scando ‘I rise’. Both the meaning and 
form of *čand-/čad- do not agree with the Skt. root very well though. A more 
plausible etymology is a connection with Lat. quatiö, etc., despite the difficulties 
surrounding the reconstruction of the PIE root. 

PIE *(s)k"eH;t- ‘to shake’ ? ó Perhaps not *(s)kueH;t-, as reconstructed in LIV, l.c. 
c» LIV: 563 f. | Pok.: 632, 957 f. 

*IE COGNATES: Lat. quatio, -cutiö ‘I shake, winnow’, Gr. nf (aor.) ‘scattered’, 
Germ., OE scudan ‘to shake’, OHG scunten ‘to incite, drive’, etc., CS skytati se ‘to 


wander, roam’ 
*REFERENCES: Horn 1893: 271; IIFL I: 391b f.; Safari 1373: 148; Kiefer 2003: 194 


*Caud ‘to urge to, impel’ 

*MIDDLE PERSIAN: (+ *ui-) BMP wewd- /wizöy-/ (or /wizoh-/ ?) ‘to examine, 
investigate’ 

Partic.: perf. pass. BMP wewst /wizost/; Inf.: BMP wewstn /wizöstan/ 

*NWIR: NP cust ‘quick, brisk, active’ || (+ *?) NP pizohidan/pizoh- ‘to investigate’ 
(LW) 

*NEIR: Oss. I. cudyn/cudt, D. codun/cudt ‘to be shaky’ 

*SANSKRIT: cod ‘to impel, to excite, to incite’ (RV+) = EWAia I: 551 

«PIE *(s)keud- ‘to shoot, impel’ = LIV: 560 | Pok.: 955 f., 636 

*IE COGNATES: OE sceotan ‘to sling, to thrust’, NHG schießen, Engl. to shoot, etc., 


(without s-) OCS kydati ‘to throw’ 
«REFERENCES: Abaev, Slovar’ I: 316; Werba 1997: 347; ESIJa П: 248 
26507:*uaid! ‘to know? 
26531:*uaid2 409 
26678:[perf.] to know’, Ir. *yaid', *uaid?, as often assumed. 
55220:(s.v.), *kauz! (s.v.), *uaid? 
56598:*uaid^ 
57821:*Haxs', *raxs, *uaid® 
58219:*suaH, *tau, *uaid’, *xsaip/b
```


## [2026-10-16T05:15:01.047Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 26500,26600p CHEUNG.txt"
}
```


### [2026-10-16T05:15:01.346Z] TOOL RESULT

```
*REFERENCES: EVP: 87; IIFL I: 280b f.; KPF II: 187; IIFL II: 240a; MacKenzie 1966: 112; EVS: 60a; 
WIM I: 74; WIM 1/1: 85; Monchi-Zadeh 1990: 24; Abaev, Slovar’ IV: 108; Werba 1997: 233; Paul 
1998: 317b, 309a; Steblin-Kamenskij 1999: 278; Cabolov 2001: 170; Lecoq 2002: 126; NEVP: 88 f.; 
Shahbakhsh: s.v. gec- 


*uaid! ‘to know? 

*AVESTAN: vid- (vió-, vaed-, va&ö-) ‘to know’ || (+ *abi-) ‘to proffer’ || (+ *a-) ‘to 
announce’ || (+ *uz-) ‘threaten; [MP transl.] to promise’ || (+ *pati-) ‘to make 
known’ || (+ *ni-) ‘to invite a deity to the sacrifice, dedicate’ || (+ *ui-) ‘to 
announce’. 0 The formation with *uz- has acquired a more specific meaning ‘to 
threaten’, which is attested in several Ir. languages, on which see see Henning 1958: 
112; Benveniste 1959: 136; Gershevitch 1977: 63. || Also the formation with *ni- 


shows a specialised meaning, which is mirrored in other languages. — Liste: 54 

Aor. s-: INJ./IMPV. med. 2р1. OAv. frauudizdum (Y 33.8); Perf: IND. 159. OAv. vaeda (Y 28.10, Y 
34.7, Y 45.4, etc.), YAv. vae0a "(Yt 1.26), 2sg. OAv. voista (Y 28.10, Y 32.6, Y 46.10), 3sg. OAv. vaeda 
(Y 31.2, Y 35.6), Y Av. va@da, ? Y Av. va&0a, 3pl. Y Av. vióaro (N 39), SUBJ. 3р1. YAv. vaeonti (V 4.50 
f£), 3sg. YAv. vaé@at (N 11), OPT. 3sg. OAv. vidiiat (Y 48.9); Partic.: pres. caus. YAv. aifi.vaeóaiiant- 
(Vr 9.3), med. Y Av. aifi.vaeóaiiamna- (Vr 9.3), perf. OAv. viduuah-, Y Av. viöuuäh-, perf. pass. YAv. 
vista- (Y 29.6); Inf.: aor. OAv. voizdiiai (Y 43.13), perf. OAv. viduiie (29.3, Y 31.5, Y 44.3), OAv. vr 
viduiie (Y 43.9), OAv. viduuanoi (Y 31.3); Caus.: pres. IND. 1sg. YAv. vaeóaiiemi (Y 1.21 £, V 17.9), 
Y Av. niuuaeóaiiemi (Y 1.1 ff., Vr 1.1 ЁЁ), ҮАУ. niuuaeóaiiemi (Vr 1.7), 3sg. ҮАУ. aifi.vaeóaiieiti (N 81), 
1р1. OAv. auuaedaiiamahi (Y 36.6, Y 41.1), YAv. vaeóaiiamahi, med. 1р1. YAv. auuaeóaiiamaide (Y 
58.2 Е), 3р1. YAv. paiti.vaeóaiieinti (У 17.10), INJ. 1sg. YAv. paiti.vaeóaem (V 2.17, V 2.9), 3sg. ҮАУ. 


*uaid2 409 


uzuuaeóaiiat (V 19.5), Y Av. niuuaeóaiiat (Yt 5.85), SUBJ. 1р1. YAv. vaeóaiiama (F 410), med. 3pl. YAv. 
aißi vaédaiiante (Yt 10.120) 

*MIDDLE PERSIAN: ? MMP whyh ‘wisdom’ || (+ *ni-) BMP nwyd- /niwéy-/ ‘to 
announce, consecrate’ = DMMPP: 341b 

Pass.: pperf. IND. 3sg. BMP nwydyt (YK ‘YMWN)t /niweyid éstad/ (Dk. 7) 

*PARTHIAN: (+ *uz-) ‘zwyd- *‘to threaten’ || (+ *ni-) nwydg ‘invitation’ = Ghilain: 
95 | DMMPP: 103a, 248b 

Partic.: perf. pass. II 'zwyd'd 

*SOGDIAN: (+ *uz-) CSogd. zwyó ‘to threaten’, CSogd. zwydm’ (f.) ‘threat’ || (+ 
*pati-) SSogd. ptwyó ‘to know’, MSogd. ptwyó ‘to offer, show’ || (+ *ni-) BSogd. 
nw’yö-, MSogd. nwyö- ‘to invite, request, inform’, BSogd. nwyömh, CSogd. 
nwydm’ (Е) ‘invitation’ 

(+ *pati-) Pres.: IND. 1sg. SSogd. ptwyö’m; Impf.: IND. 1sg. MSogd. ptywyów || (+ *ni-) Pres.: SUBJ. 
3sg. BSogd. nw’yö’t, POT.-SUBJ. 3sg. BSogd. nw’yst’ wn’’t, Impf.: IND. 3sg. BSogd. nyw’y6; Inf: 
BSogd. nw’yö’y 

*CHORESMIAN: (+ *uz-) m/zwyzy- (caus.) ‘to threaten, fill with fear’ © Samadi: 266 
*NWIR: (+ *ui-) Kurd. (Kurm.) bihistin/bihis-, bihiz-, bihe-, (Sor.) bistin/biya- ‘to 
hear, listen, get to know’ 

*NEIR: (+ *uz-) Oss. I. zvzidyn/evzyst, D. avzedun/evzist ‘to threaten; to shake 
with one’s arm or weapon’ 

*MISC: (+ *ni-) Arm. (LW) nuér ‘oblation, sacrifice’ (*yaid(H) ‘to be devoted to’ ?) 
*SANSKRIT: ved ‘to (get to) know’ (RV+) = EWAia II: 579 

0 The root is originally identical with *yaid’. 

«PIE (perf. stem) *uoid- ‘to know’ = LIV: 686 ff. | Pok.: 1125 ff. 

*IE COGNATES: Gr. 0180 ‘I know’, Arm. gitel, Olrish ro-fetar, MWelsh gwyr, OCS 


védé, Goth. wait, witum, ON vita, OE witan ‘to know’, Engl. wit, etc. 
*REFERENCES: Abaev, Slovar’ I: 212; Werba 1997: 377 f.; Cabolov 2001: 174 


*yaid? ‘to find’ 
*AVESTAN: vaéd- (va&ö-, vid-, vió-) ‘to find’ || (+ *fra-) ‘to receive, be presented ?’, 
caus. ‘to present’. 0 On the formation with *fra- cf. Skt. RV 8.24.6b рга... vevidama 


‘let us receive’, see Insler, Gathas: 247. = Liste: 54f. 

Pres. {1} n-: IND. 35р. OAv. vmasti (Y 31.15, V 7.78 £), ҮАУ. vinasti (N 109), med. 3sg. YAv. viste (F 
377, Aog 82), 3р1. YAv. vindonti (V 2.17, V 2.9), INJ. 3pl. YAv. vinden (V 2.16, V 2.8), OPT. med. 3sg. 
YAv. vindita (Yt 17.54); Pres. {2} them. n-: INJ. 3sg. YAv. vindat (F 382), SUBJ. med. 2sg. YAv. vindai 
(V 19.6), 1р1. YAv. vindama (Yt 15.40, V 19.46), med. 3pl. ? YAv. vindante (? V 18.36); Pres. {3} 
them.: IMPV. med. 2р1. OAv. vaedo.düm (Y 53.5); Aor. them.: IND. 3pl. ? YAv. vidanti (Yt 6.3, Ny 
1.13), INJ. Zeg OAv. vido (Y 51.18), 3sg. OAv. vidat (Y 51.5), SUBJ. Zeg YAv. vióaiti (P 14), IMPV. 
2sg. OAv. vida (Y 49.1); Perf.: IND. 35р. YAv. viuaeóa (Yt 13.99); Partic.: pres. {1} YAv. vindana- (N 
16), pres. {2} med. YAv. vindomna- (V 19.4), pres. (3) med. OAv. vaedomna-, Y Av. frauuaeóomna- (Yt 


410 *yaid3 


5.126), perf. pass. YAv. vista-; Intens.: pres. IND. med. 159. OAv. frauuoiuuide (Y 44.11), SUBJ. (med. 
?) 3sg. OAV. убшшаапё/ (Y 30.8) 

*MIDDLE PERSIAN: MMP w(y)nd-, ВМР wnd- /wind-/ ‘to find, obtain, gain’ || (+
```


## [2026-10-16T05:15:05.622Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:2297 2>&1 | head -80"
}
```


### [2026-10-16T05:15:13.996Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 380; check the printed number and re-run with --pdf-page if off)
REF: BQT:2297  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 380  OCR-lang: fas

۹۷ ۷- وبضا
باشد وخواء صد ب رکه ؛ وبکسرتالت‌هم کفته‌اند. ٍ معالی بفتح اول هم‌آمده است - و بکسراول‌وثانی
وید « بکر اول وسکون ثانی و دال» | مجهول , دام کتابی است آسمانی باعتفاد کفرء
بمهنی کم باشد که درمقابل بسیاراست ۱ -وبمعنی | هند ۲ . .
کم در برابر بیدا همست ۱ - واهر چیز عفص وید| - بکراول بروزن بیجا » بمعنی
را نیز کوبند مانند مازو وپوست اناروامثال آن- وید است که کم و ناپیدا و ناپدید کشته۴ سوکم
ر بسنی چاره وعلاج همگفته‌اند جنانکه کید | و راز اداخته باشد؟۴ - و بسی بدا
« چه وید کنم ؟» پمنی چه چاره کنم ؛ و باین و ناص و دور و و بمعی اف
۱ - امدی گوید : « وید ,گم باشد » وید! نیز گویند . رود کی (سمرقندی) گوید:
ای غافل از شمار چه پنداری کت خالق آ فریده بهرکاری (نه‌برکاری؟دهشدا)
عمر ی که مر تراست سرمایه وید است وکارهات بدین زاری .»
« لغت فری ص *۹۱۱ ۰
و هم اسدی‌آرد : ۶ وبدا ,کم شده باشد چون وید » « لغت فرس ص 0 [ ر4 : ویدا ]|ظ. کدك+
مصحف « وند؟ ومعنی آن «کم» ( بفتح‌کاف تازی ) است بمنی اندك . ابن‌الندیم درالفهرست(چاپ
مصرص۳۳۸) درداستان کردالیدن دفاتر دیوانی‌ازفارسی بمربی‌آرد: « فقال‌له ( لسالح‌ین‌عبدالرحمن)»
مردانشاه‌ین زادافروخ : کیف هنم , *دهوبه» و «ششویه ( ظ: پنجوبه )»۲ قال : اکتب«عشرا» و
« صف هعر» . قال : فکیف تستع , « وید ۲ قال : اکنب « وایضاً > قال [ فکیف تصنع , *وند»؟
قال : اکتب « الئیف >] ( سوّال وجواب اخیر دراصل نیامده و ظ. لازم است ) و |(« وید » (ا[
« وند » ظ. ) النیف.» لیف پروزن کیس درعربی بمعتی افزونی وزبادت چپزی است*منتهی‌الارب»
و «وند > اند ( ۶ اند , شمار مجهول هم‌هست ازسه تا نه » وآلرا بمربی لیف و جضم خوانند.»
برهان ). رك : آند . ۲ -۷۵42 از رشه ۷16 بمعنی دادتن است «وبلیامز ۷:۹۹۳»
وخود «ودا» بمعنی معرفت و داش است وآن مجموعهة کتابپای مقدی هندوان و متعلق به آیین
برهمائی‌است‌بز بان ماسکریت و شامل چهار کتاب است : ۷۵۵48 818 ۷۵48- ناژ ۰
8-۸ 58. ۸138۲۷۵-۷۵۵۵ .هرهودا» عبارتست ازمجموعه‌ای از رودها که باوزانمختلف
و در باره خدایان متمدد سروده شده است . ۴ -« ویدا گم شده باغد چون‌وید . دقیقی
( طوسی ) کفت :
آمیرا ! جان شیرین‌برفشام اکرویدا شود پیکارعمرم(نل: گروبداشوديك‌بارکی‌همر)».
ورك : وید (ح۱ ). « لغت فری ص ۵ >.
و در سخهة صحاح‌الفری آمده : « وبداکم باشد بفتح‌کاف . دقیقی گفت :
امیرا ! جان شیرین برفعغام اگر وبد! شود یکبا رکی‌عمر.» ‏ «طاعتی».
ودر سخهٌ دیگر صحاح‌الفری : « وبدا پمنی کم و ناقص . دقیقی گفت :
امیرا ! از برای مدحت تو شده همر عزیزم زود وبدا . »
« فرهنگه نظام > .
این لفت درجهانگیری وسروری نیز «گم‌شده > معنی شده . چنالکه درمتن لغت قری (ص 0 )-
ولی معلوم لیست فی‌الحقیقه این جملةٌ کم شده > دراین کنتابها باید با فتح‌کاف خوانده شود با با
ضم‌گاف | در سخهٌ ۸« منتخب فرس » میرزا ابراهیم هم این لغت چنین معنی شده : « وید - کم
شده >. با توجه بضبط صحاح‌الفری » توان گفت این جمله دراصل همان «کم‌شده > بفتح‌کاف برده.
سپس فتحةکای را شاخ دوم کاف پارسی کمان کردهآ نرا «کم» بضم کاف خواندماند. « طاعتی >.
```


## [2026-10-16T05:15:19.043Z] TOOL CALL #21: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/ | grep -E '^(2297|2401)'"
}
```


## [2026-10-16T05:15:19.554Z] TOOL CALL #22: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2297.png"
}
```


### [2026-10-16T05:15:19.831Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-16T05:15:20.141Z] TOOL RESULT

```

```


## [2026-10-16T05:15:20.137Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-16T05:15:30.974Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat > data/verification/sources/refs/ocr/BQT/2297.vision.txt <<'EOF'\n[BQT p.2297, read from page image by verifier for pdf page 534]\nوید - بکسر اول وسکون ثانی و دال، بمعنی کم باشد که درمقابل بسیاراست (۱) - وبمعنی کم در برابر پیدا هم هست (۱) - و هر چیز عفص را نیز گویند مانند مازو وپوست انار وامثال آن - و بمعنی چاره وعلاج هم گفته‌اند چنانکه گویند «چه وید کنم؟» یعنی چه چاره کنم؛ ... - و بکسر اول وثانی مجهول، نام کتابی است آسمانی باعتقاد کفرهٔ هند (۲).\nویدا - بکسر اول بروزن بیجا، بمعنی وید است که گم و ناپیدا و ناپدید گشته (۳) - و کم و ناقص و دور انداخته باشد (۳) - و بمعنی پیدا ... [continues on p.2298]\nFootnotes (Mo'in): ۱- اسدی گوید: «وید، کم باشد، ویدا نیز گویند.» ... ۲- Veda از ریشهٔ vid بمعنی دانستن است «ویلیامز ۲:۹۶۳» وخود «ودا» بمعنی معرفت و دانش است ... ۳- «ویدا، گم شده باشد چون وید. دقیقی (طوسی) گفت: امیرا! جان شیرین برفشانم / اگر ویدا شود پیکار عمرم» «لغت فرس ص ۵» ... صحاح الفرس: «ویدا کم باشد بفتح کاف» ... «ویدا یعنی کم و ناقص».\nEOF\npython3 tools/ref_page.py BQT:2298 2>&1 | head -30; python3 tools/ref_page.py BQT:2401 2>&1 | head -60"
}
```


### [2026-10-16T05:15:38.508Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 381; check the printed number and re-run with --pdf-page if off)
REF: BQT:2298  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 381  OCR-lang: fas

وبدايك -م۷۹۸-<
وهویدا وظاهرهم آمده است ‎٩‏ - ودرد والم‌وآ زار وعلاج کردن باشد ؛ و بفتح اول هم‌آمده است.
را نیز کویند ؛ و باین معنی بقتح اول‌هم کمته‌اند ویده ؟۴ - بنتم‌اول بروزن‌میده. بعمنی
و اسح این است . چاره جسته و چاره جوبنده باشد ؛ ویکسراولهم

وبدانك ه با اول بثالی مجهول‌رسشده آمده است.

و دال بالف کشیده وفتح نون وسکون‌کاف,بمعنی وید یدن « بنتح اول بروزن کردیدن,
کاری و چیزی بهم ناپیوسته باشد و آنرا بعری بممنی گم شدن وناپدید گشتن ونقصان کردن* -
طفره و درهندوستان باغه کوبند . وچاره وعلاج جتن باشد ‎٩‏ .

و پدستر ؟ -« با تای قرغت بروزن بی ور ۷ » بکراول بروزن میر ؛ بهعنی
لشکر . نام حیوانی است بحری و در خشکی‌هم | از بر است که ازحفظ کردن و بخاطرنگاهداغتن
میباشد وخصبهٌ او راآش بچگان کوبند . باشد ۸ - و بمه‌نی‌فهم وهوش و ادرادعم‌هت۹-

ویدن ۴ بروزن دیدن , چاره جتن | و نله و فرباد را نیز کویند *۱- و نام دجی‌است

۱ -فی : هوبدا. ۴ *<بیدستر (ه.م.) وارك : رشیدی .
۴ -ر4 : وبدیدن . ۴ - ر4 : ویدن» وبدیدن ۰
8 - رك : وید , وندا. ۹« ویدیدن ( بفتح واو و سکون هردو با ) چاره
جستن » وبدیده چاره جستّه .» ۸ رشیدی» « موْبدالفسلاء » و رك : ویدن » ویده .۰
۷ *بیر (هم.) * بر(ه.م.) » قن : وبرا (۸.م.) اوستایی -5۷178 (هوش) «دارمتش.
تبعات ج ۲ ص ۱۸۳ ؛ پپلوی ۷1۲ ۰ ۷۸72۴ (وبرا ) »کردی 1۳ظ ( حافظه ) » بلوچی 817۲
( حافظه , تذکار ) * اسدق ۱۶۸۹ . رك : بیر.- ولف *وبر» را درشاهنامه بمعمنی هوش وحافظه
آورده: اورامانی۷۷1۳ (باد . حافظه) «ک4 . اورامان. ۶۱۲۷ » دراراك (-لطان؟ باد)8154 ۷1۳-02
( نظرم لیست » فراموش کرده‌ام ) « مکی‌نژاد > .
۸ - چه افتاد ای عزیزان مر شما را که شد یکبارتان پاد من از ور.
(no exact page map; using offset -1917 -> pdf page 484; check the printed number and re-run with --pdf-page if off)
REF: BQT:2401  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 484  OCR-lang: fas

-۱)- حوبد4
نتاح یکمرد میباشند و هريك مر دیگریرا هوو | وکسر ثالی است اوآ ن کلیمی باشد پشم آکنده
خوانند . بعنی‌پرپشم کهآ برا بردور کوهان‌شتردر آوزند؟ -
هوی - بم اول وسکرن ثالیوتحتانی» هوید)۲ * جم اول بر وزن سوبدا,
بمعنی کرس وبیم باشد۹ . بمعنی ظاهر و روشن و بین باشد بعنی در نهایت
هو ید » بنم اول وفتح ثالی وسکون ۱ ظهور.
تحتالی ودال» جهاز شتر را گوبند وآن بمنزلهٌ هویدند؟ « م‌اول‌وفتح الی‌وسکون
پالان اوست ؛ و بح ی کوبند این لفت بفتح اول | تحتالی ودال بی‌فطةٌ مفتوح بکاف زده » یکی از
۹ - هوی (80۵9,86)کلمه افضوس است :
همه چشم پرآب ودل پر ز هوی به طوس سپهید لمودند روی .
فردوسی طوسی«فرهنگه فظام».
وکلمهٌ تشه است :
هان‌مردا هوی وهان جوانمردا هوی مردی کنی و نگاه داری سر کوی.
منسوب بابوسمید ابوالخیر «فرهنکه نظام».
۲ - برآوردم زمامش(غت) تا بناگوش فرو هشتم هوبدش نا بکاهل .
«منوچهری دامفالی. دیوان ۰.۴۵۰
۴ - از: « ( ۳ 8 اوستایی بمعنی خوب )۳۲ ویدا (* پیدا ) مرحوم بهار در حواشی
مخطوط خود برلغفت فرس آاسدی چاپ مرحوم‌اقبال ص6 همین گونه اظهار عقیده کرده‌اند . قی :
کردی 30818 (ظاهر, بدیهی) «ژابا ص۱۹۷>. «هوبدا. سخت پیدا بود , چنانکه عنصری (بلشی)
کوید :
درشتی دل شاه ولرمی دلش ندانی هوید!ا کنی حاصلش .»
«لفت فری ‎۰.۹٩‏
‏ور4:صحاح‌الفری لغهٌ طاعتی . ۴ - جهانگیری «هوبديك» آورده کوید: « نام یکی از
پیشوایان ملحدان بوده که حکم خاقالی فرماید :
او کیست که با روان تاريك باشد ‏ بمثابت هوبديك . »
پوستی این نام را 1108۷21411 ضبط کرده باستناد فولری 1 ۰ 8۱۶۷۰ و بکتاب ,[6 570168
۰ 2 .410 ول[ ۳0۳۳۵81۵7 ارجاع کرده «یوستی . نام نامه س ۱۸۰ اشپیگل درکتاب
مزبور («مان صفحه) دربحث از كلمهٌ اوستابی 808013942 ( که طبقه‌ای ازدروجان [ درو غ‌یرستان»
پیروان کیش باطل] هتند. ر4: پوستی. فرهنکه اوستا ص۳۲۸) کوید: من اکنون کرجیح‌میدهم
که كلمهٌ مز بورعنوانی‌باشد برای انگره میئو (اهریمن). اسپندبارجی مقدم, این کلمه را «زیانکار»
(مضر) تعبیر میکند واسپند,ارجی موّخر آبرا 118068 با 82۷1086 (رك: فرلری . عوبد4)
میداند که شانه‌ایست برای تشخیص بی دینان . > ممکن است احتمال داد ۶ هوبدك» متن
ممحف «* بوند که » 32۷28480 پهلوی ( در ارمنی ۳0۷۵8026 ) بمننی کامل ۳ بوندی
8 ۴ بوندهء * بوندباشد.بام یکی‌ازمالويهٌ روم که با کرش رسمی مانویه مخالفت کرد و او
پیشرو مزدك بود. ر: کرستنشن. ساسان ۳۳۷ ببعد؛ ترجمةٌ آن طبم دوم ۳۹۲ بیمد؛ ایا
کربتنشن . ترجمهٌ تاریخ سلطنت قباد وظهور مزدك ص۲۰۲ ببعد. درهرحال خاقانی آین اسم را
```


## [2026-10-16T05:15:44.888Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in اوستا هویدا ویدا پژوهیدن اسطوره تلویزیون ویزیت ویدیو پنگوئن; do u=\"https://vajehyab.com/moein/$w\"; python3 tools/fetch_source.py \"$u\" --note \"page 534, root Weid: Mo'in s.v. $w\" >/dev/null; done; u='https://vajehyab.com/amid/پنگوئن'; python3 tools/fetch_source.py \"$u\" --note 'page 534, AMD penguin' ; grep 'page 534' data/verification/sources/web/index.jsonl | grep vajehyab | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'],d['bytes'],d['url'],d['file'])\""
}
```


### [2026-10-16T05:15:49.213Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/59d81e10909092c5.txt
200 585 https://vajehyab.com/moein/اوستا data/verification/sources/web/236515b15782e1e5.txt
200 549 https://vajehyab.com/moein/هویدا data/verification/sources/web/4cc6d76971b319e7.txt
200 474 https://vajehyab.com/moein/ویدا data/verification/sources/web/cc31ce3089cc4b23.txt
200 581 https://vajehyab.com/moein/پژوهیدن data/verification/sources/web/4af5f00402243c6a.txt
200 651 https://vajehyab.com/moein/اسطوره data/verification/sources/web/99eb753515e7efc7.txt
200 656 https://vajehyab.com/moein/تلویزیون data/verification/sources/web/a92995478dd2cb6a.txt
200 464 https://vajehyab.com/moein/ویزیت data/verification/sources/web/f93077e24e92046b.txt
200 420 https://vajehyab.com/moein/ویدیو data/verification/sources/web/f9c09d539b7cdf56.txt
200 635 https://vajehyab.com/moein/پنگوئن data/verification/sources/web/28bc02e970469fb1.txt
200 575 https://vajehyab.com/amid/پنگوئن data/verification/sources/web/59d81e10909092c5.txt
```


## [2026-10-16T05:15:51.496Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 236515b15782e1e5 4cc6d76971b319e7 cc31ce3089cc4b23 99eb753515e7efc7 a92995478dd2cb6a f93077e24e92046b 28bc02e970469fb1 59d81e10909092c5; do echo \"== $f\"; cat $f.txt | head -20; done"
}
```


### [2026-10-16T05:15:51.789Z] TOOL RESULT

```
== 236515b15782e1e5
URL: https://vajehyab.com/moein/اوستا
FETCHED: 2026-10-16T05:15:45Z
STATUS: 200
TITLE: معنی اوستا | فرهنگ انتشارات معین | واژه یاب

معنی اوستا | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 اوستا

 فرهنگ انتشارات معین
 (اَ وِ) (اِ.) کتاب دینی زرتشتیان که شامل پنج بخش می باشد. 1 - یسنا. 2 - اوستا، ویسپَرد. 3 - وَندیداد. 4 - یشتا. 5 - خرده اوستا.
 اوستا در فرهنگ‌های دیگر
 معنی اوستا در لغت‌نامه دهخدا 
 معنی اوستا در فرهنگ فارسی عمید / قربان‌زاده 
== 4cc6d76971b319e7
URL: https://vajehyab.com/moein/هویدا
FETCHED: 2026-10-16T05:15:45Z
STATUS: 200
TITLE: معنی هویدا | فرهنگ انتشارات معین | واژه یاب

معنی هویدا | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 هویدا

 فرهنگ انتشارات معین
 (هُ وَ) (ص .) 1 - آشکار، پیدا. 2 - روشن .
 هویدا در فرهنگ‌های دیگر
 معنی هویدا در لغت‌نامه دهخدا 
 معنی هویدا در فرهنگ فارسی عمید / قربان‌زاده 
== cc31ce3089cc4b23
URL: https://vajehyab.com/moein/ویدا
FETCHED: 2026-10-16T05:15:46Z
STATUS: 200
TITLE: معنی ویدا | فرهنگ انتشارات معین | واژه یاب

معنی ویدا | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 ویدا

 فرهنگ انتشارات معین
 (وَ یْ) (ص .) آشکار، پیدا.
 ویدا در فرهنگ‌های دیگر
 معنی ویدا در لغت‌نامه دهخدا 
 معنی ویدا در فرهنگ نام‌ها 
== 99eb753515e7efc7
URL: https://vajehyab.com/moein/اسطوره
FETCHED: 2026-10-16T05:15:47Z
STATUS: 200
TITLE: معنی اسطوره | فرهنگ انتشارات معین | واژه یاب

معنی اسطوره | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 اسطوره

 فرهنگ انتشارات معین
 (اُ طُ رِ) [ ع . ] ( اِ.) 1 - افسانه ، قصه . 2 - سخن بیهوده و پریشان . ج . اساطیر.
 اسطوره در فرهنگ‌های دیگر
 معنی اسطوره در لغت‌نامه دهخدا 
 معنی اسطوره در فرهنگ فارسی عمید / قربان‌زاده 
== a92995478dd2cb6a
URL: https://vajehyab.com/moein/تلویزیون
FETCHED: 2026-10-16T05:15:47Z
STATUS: 200
TITLE: معنی تلویزیون | فرهنگ انتشارات معین | واژه یاب

معنی تلویزیون | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 تلویزیون

 فرهنگ انتشارات معین
 (تِ لِ یُ) [ فر. ] (اِ.) دستگاهی است که تصاویر اشیاء و اشخاص را از مسافت دور به وسیلة امواج الکترونیکی انتقال دهد.
 تلویزیون در فرهنگ‌های دیگر
 معنی تلویزیون در لغت‌نامه دهخدا 
 معنی تلویزیون در فرهنگ فارسی عمید / قربان‌زاده 
== f93077e24e92046b
URL: https://vajehyab.com/moein/ویزیت
FETCHED: 2026-10-16T05:15:47Z
STATUS: 200
TITLE: معنی ویزیت | فرهنگ انتشارات معین | واژه یاب

معنی ویزیت | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 ویزیت

 فرهنگ انتشارات معین
 [ فر. ] (اِ.) 1 - دیدار، بازدید. 2 - ملاقات بیمار از طرف پزشک .
 ویزیت در فرهنگ‌های دیگر
 معنی ویزیت در لغت‌نامه دهخدا 
 معنی ویزیت در فرهنگ فارسی عمید / قربان‌زاده 
== 28bc02e970469fb1
URL: https://vajehyab.com/moein/پنگوئن
FETCHED: 2026-10-16T05:15:48Z
STATUS: 200
TITLE: معنی پنگوئن | فرهنگ انتشارات معین | واژه یاب

معنی پنگوئن | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 پنگوئن

 فرهنگ انتشارات معین
 (پَ ئَ) [ فر. ] (اِ.) پرنده ای از راستة پرندگان دریایی و بی پرواز است . بال هایش از پره های پولک مانند به رنگ سیاه و سفید پوشیده شده و بدون شاهپر است . در زیر پوست چربی فراوان ذخیره دارد و می تواند به صورت قائم بایستد. در قطب جنوب دیده می شود.
 پنگوئن در فرهنگ‌های دیگر
 معنی پنگوئن در فرهنگ فارسی عمید / قربان‌زاده 
 معنی پنگوئن در دیکشنری فارسی به انگلیسی 
== 59d81e10909092c5
URL: https://vajehyab.com/amid/پنگوئن
FETCHED: 2026-10-16T05:15:49Z
STATUS: 200
TITLE: معنی پنگوئن | فرهنگ فارسی عمید / قربان‌زاده | واژه یاب

معنی پنگوئن | فرهنگ فارسی عمید / قربان‌زاده | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 پنگوئن
 تلفظ /pangu(o)van/ 
 نوع واژه (اسم) [فرانسوی: pingouin] (زیست‌شناسی) 

 فرهنگ فارسی عمید / قربان‌زاده
 پرنده‌ای ساکن در قطب جنوب با پاهای پرده‌دار و بال‌های کوتاه که نمی‌تواند پرواز کند و در آب شنا می‌کند.
 پنگوئن در فرهنگ‌های دیگر
```


## [2026-10-16T05:15:55.957Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; grep -v '^\\s*$' web/cc4f19202101e879.txt | grep -i -A8 '^ *Etymology$' | head -30; grep -v '^\\s*$' web/9e4aecd45ece45f3.txt | grep -A5 '^ *Etymology$' | head; grep -v '^\\s*$' web/ea4f4c10742e89e6.txt | grep -A5 '^ *Etymology$' | head; awk 'BEGIN{RS=\"\\f\"} NR==74' refs/FVQ_pages.txt | head -60"
}
```


### [2026-10-16T05:15:56.420Z] TOOL RESULT

```
 Etymology
 [ edit ] 
 Etymology tree
 Proto-Celtic *kʷennom 
 Proto-Brythonic *penn 
 Welsh pen ? 
 Proto-Indo-European *weyd- der. ? 
 Proto-Celtic *windos 
 Proto-Brythonic *gwɨnn 
--
 Etymology
 [ edit ] 
 Internationalism 
 Pronunciation
 [ edit ] 
 ( Standard Indonesian ) IPA ( key ) : /peˈŋuin/ [peˈŋu.ɪn] 
 Rhymes: -in 
 Syllabification: pe‧ngu‧in 
 Noun
 Etymology
 [ edit ] 
 From Proto-Hellenic *wístōr , from Proto-Indo-European *wéydtōr ( “ knower, wise person ” ) , from *weyd- ( “ to see ” ) . [ 1 ] 
 Pronunciation
 [ edit ] 
 IPA ( key ) : /hís.tɔːr/ → /ˈis.tor/ → /ˈis.tor/ 
 Etymology
 [ edit ] 
 From Proto-Indo-European *wid-tó-s . [ 1 ] 
 Pronunciation
 [ edit ] 
 IPA ( key ) : /ˈwis.sɑz/ 
56 FOREIGN VOCABULARY OF THE QUR ? AN
*^>\^\ (Asatir)
vi, 25 ; viii, 31 ; xvi, 26 ; xxiii, 85 ; xxv, 6 ; xxvii, 70 ; xlvi, 16 ;
Ixviii, 15 ; Ixxxiii, 13.
Fables, idle tales.
We find the word only in the combination (j
" tales of the ancients ", which was the Meccan characterization of the
stories brought them by Muhammad. Sprenger, Leben, ii, 396 ff.,
thought that the reference was to a book of this title well known to
Muhammad's contemporaries, but this theory has been combated in
Noldeke-Schwally, i, 16 if., 1 and its impossibility becomes clear from a
passage in Ibn Hisham, 235, where Nadr b. al-Harith is made to say
" By Allah, Muhammad is no better a raconteur than I am. His stories
are naught but tales of the ancients (^J^l j*L>U) which he
writes down just as I do/'
The Muslim authorities take it as a form ^^i from * t
write, considering it as a phi. of aj^Lu-i or SjUa^l (Sijistam, 10),
**
or the plu. of a plu. (LA, vi, 28). The verb Jb.** , however, as Fraenkel
">'*'
has shown (Fremdw, 250), is a denominative from Jb.**, and this
itself is a borrowing from Aram. N"1D!2J, \&* (Noldeke, Qomns,
13). It is possible but not probable that ^kLJ was formed from this
borrowed
Sprenger, Leben, ii, 395, 2 suggested that in ^-^L^l we have the
Gk. 'uTTOpla, a suggestion also put forward by Fleischer in his review of
Geiger (Kkinere Schriften, ii, 119), and which has been accepted by
many later scholars. 3 The objections to it raised by Horovitz, KU 9 70,
are, however, insuperable. The word can hardly have come into
Arabic directly from the Greek, and the Syr. "U'G&flDl occurs only
1 See also Hirschfeld, New Researches, 22, 41 If., on Sprenger's Suhuf theories.
2 Vide also his remarks in JASB, xx, 119, and see Freytag, Lexicon, sub voc.
3 Vollers, ZDMG, Ii, 312. See also Kunstlmgcr in OLZ, 1936, 481 ff.
```


## [2026-10-16T05:15:58.980Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; awk 'BEGIN{RS=\"\\f\"} NR==75' refs/FVQ_pages.txt | head -25; grep -n 'اسطور\\|اساطير' refs/TAD_pages.txt | head; grep -v '^\\s*$' web/cc4f19202101e879.txt | grep -i -B2 -A6 'pen gwyn\\|uncertain\\|Welsh' | head -40"
}
```


### [2026-10-16T05:15:59.376Z] TOOL RESULT

```
FOREIGN VOCABULARY OF THE QUR*AN 57
as a learned word (PSm, 298). The derivation from Syr.
suggested by Noldeke-Schwally, i, 16 n., is much more satisfactory.
1^4*1 (cf. Aram. N*")M$) is the equivalent of the Gk. ytipoypafyov*
and is a word commonly used in a sense in which it can have come
into Arabic. It was doubtless borrowed in this sense in the pre- Islamic
period, 2 for in a verse of the Meccan poet 'Abdallah b. az-Ziba'ra,
quoted in 'Aim, iv, 140, we read j*
" the stories liave averted Qusay from glory ".
In S. Arabian, as D. H. Miiller points out (WZKM, i, 29) we have
)|H I l | ji 1 meaning an inscription, and ^^ is the usual verb for
scripsit (Rossini, Glossarinm, 194), so it is not impossible that there was
S. Arabian influence on the form of the word. See further under
(AM)
ii, 130, 134 ; iii, 78 ; iv, 161 ; vii, 160.
The Tribes. Flu. of ia*-

It occurs only in Madman passages and always refers to the
Children of Israel. In vii, 160, it is used normally of the Twelve Tribes,
but in all the other passages the J^L^1 are spoken of as recipients of
revelation, and one suspects that here Muhammad is confusing the
Jewish use of " the Twelve " for the Minor Prophets with that for the
Twelve Tribes. 3
The philologers derive it from a.+~ a thistle, their explanation
thereof being interesting if not convincing (LA, ix, 1 82). Some, however,
190:‫معاه أخبار تارمحية وقد استعمابا العرب ععى‬           ‫اساطير ‏ بوناني ‪8‬‬
 Proto-Celtic *kʷennom 
 Proto-Brythonic *penn 
 Welsh pen ? 
 Proto-Indo-European *weyd- der. ? 
 Proto-Celtic *windos 
 Proto-Brythonic *gwɨnn 
 Welsh gwyn ? 
 Proto-Indo-European *peyh₂- der. 
 Proto-Indo-European *bʰenǵʰ- influ. ? 
 Latin pinguis der. ? 
 English penguin 
 Uncertain. [ 1 ] First attested in the 16th century in reference to the auk of the Northern hemisphere; the word was later applied to the superficially similar birds of the Southern hemisphere (as was woggin ). Possibly from Welsh pen ( “ head ” ) and gwyn ( “ white ” ) , or from Latin pinguis ( “ fat ” ) . See citations and the Wikipedia article .
 Sense 3 originates from the often black-and-white habit worn by nuns, which resemble the bird's colors.
 Pronunciation
 [ edit ] 
 ( Received Pronunciation , General American ) IPA ( key ) : /ˈpɛŋ.ɡwɪn/ 
 Audio ( US ) : ( file ) 
 ( pin – pen merger ) IPA ( key ) : /ˈpɪŋ.ɡwɪn/ 
--
 → Korean: 펭귄 ( penggwin ) 
 → Thai: เพนกวิน ( pen-gwîn ) 
 → Welsh: pengwin 
 Translations
 [ edit ] 
 flightless sea bird
 Abkhaz: апингви́н ( apʼingvín ) 
 Afrikaans: pikkewyn   (af) 
 Aghwan: please add this translation if you can 
--
 Vietnamese: chim cánh cụt   (vi) , chim cụt cánh 
 Volapük: pinguen 
 Welsh: pengwin   m 
 Xhosa: oonombombiya 
 Yámana: ŝúŝa 
 Yiddish: פּינגווין   m ( pingvin ) 
 Yoruba: pẹ́ńgúìnì 
 Zazaki: penguen   (diq) 
 Zhuang: gingoz 
--
 English terms derived from Latin
```


## [2026-10-16T05:16:02.073Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 180,195p TAD_pages.txt; awk 'BEGIN{RS=\"\\f\"}{ if (index($0,\"اساطير\")) print NR}' TAD_pages.txt"
}
```


### [2026-10-16T05:16:02.402Z] TOOL RESULT

```
                          ‫لا رائحةولالمول لاون وقد يدخل بتركيب الموا‪.‬‬
 ‫ايطالي ‪ 0‬عمعناه وحدة وهو ورقة من ورقاللعب ذات نقطة واحدة‬        ‫اس ‪-‬‬

 ‫إسبائخ س فارسي«اسفائغ» وهو ببقسلتةانية تشبهالسلق 'يسلق ورقها وبوكل‬
‫إسبيداج ‪ -‬قارسي « سفيداتك » سفيد في الفارسية معناه أبيض وأنّكفي‬
 ‫العبرائية معناه رصاص وهو بياض الرصاص وبال لدفيالكيميا كربونات الرصاص‬
                                    ‫استاذ فارمي «استاد معناه مع‬
‫يوناني ‪ 761818‬تاد أزانفة وهو لقنفضة كان يساوي فى أثينا‬          ‫إستار‬
      ‫ْ‬                                                       ‫أربعة دراهم‬
                                               ‫)‪ (0‬سى بالدهر مأئة سئة‬
‫معاه أخبار تارمحية وقد استعمابا العرب ععى‬           ‫اساطير ‏ بوناني ‪8‬‬
                                                            ‫خرافات وحكابات‬
                                     ‫استبرق ‪ -‬فارسي معناه الديباج الغديظ‬
                                   ‫اسرب ‪ -‬فارسي «سيرب» معناه رصاص‬
        ‫إسطيل واصطيل ‪ -‬لاتيني ‪#‬دااناطهاة معناه مأوى الخيل والدواب‬
‫خا لان | رانم كن من ‪ 807653‬أى ك كب وهلاةطه‪:‬ذا أُخذ وكان‬
7
```


## [2026-10-16T05:16:06.695Z] TOOL CALL #29: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe-private/site/pages/534.jpg && echo ok"
}
```


## [2026-10-16T05:16:07.074Z] TOOL CALL #30: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/534.jpg"
}
```


### [2026-10-16T05:16:07.118Z] TOOL RESULT

```

```


### [2026-10-16T05:16:07.135Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   74k sfmqrb 14 Oct 22:15  /home/sfmqrb/git/rishe-private/site/pages/534.jpg
ok
```


## [2026-10-16T05:16:16.235Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'vlnasti\\|vInasti\\|vīnasti\\|vinasti' BRT.txt | head -5; grep -n -i 'vldar\\|vidarə\\|vIdar' BRT.txt | head -5; grep -n -i '^ *vldya\\|vidya-\\|vldyä' BRT.txt | head -5; grep -n 'huvaed\\|huvaēd\\|hu-vaed' BRT.txt | head; grep -n -i 'hoveid\\|huvaid\\|huvēd\\|huweyd' HRN.txt HUB.txt PHD_mackenzie.txt NYB_vol2_glossary.txt| head"
}
```


### [2026-10-16T05:16:16.712Z] TOOL RESULT

```
2733:holz  zum  mindesten  darbringend  ist  man  Inf-  <^t^^;  Absol.  'agi?m,  •iünbrn. r.f'  N.106;  —  iat  tä  °ma  (^V.)  yaoz-  i)  '(etwas)  suchen,  suchen  nach  -, dayqn  ar>h>n  V.  7. 28;  ■ — ■  pairi  urvarä-  aufsuchen':  yd  aüm  mainimnö  ahm byasca  varsoäbyasca  'tnaiil^ö  "abseits  von  isimnS  ahm  apa.rao'iayeiU  {sA.)  .  .  dru- Bäumen  und  Sträuchem,  die  Brennholz  jimca  vinasti  V.  7.78;  —  Med.  auch  in sind  (geben)"  V. /6'.  2;  —  Auskam  °m»m  reflex,  Sinn:  vSrrinahe  .  .  yS  vazaite  .  . Y.JI.8; — Auskanqm  ..  'manqm  ,.  nafi-  axsa/hi  {sä.)  xsa/hTm  tsfmnS  \'t  14.  20; tanqm  ..  xraozdvanam  ..  varidvanamY.    ao.  a)  mit  Dat.  comm.:  vlstäspahe  ..
6063:30.  8 ;  —  yäis  *gr!hmä  (sd.)  »/J/  varata . . xsahrimca  ll'anqm  *drujim  Y.j2. 12;  — aHbys  yBi  urvätäU  drBjö  'iahyä  gag^ä*> vitrwfncaitg  (sd.)  Y.  j/.  i;  —  s.  noch: yf  ra%3ms  (sd.)  °sat  haia  \,44.  17  und drüp  haia  ra^fptS  Y.  5J.  6 ;  —  ae^l 'Sahyä  Y.  28.  4  und  isanqm  *drujim  Y, 32.  12.  b)  im  jAw.:  vainn  akmi nmäne..  ar^uxoö  växl  mikaext  m  väHm *'sa  (als  Subj.)^*  ^drujim  Y.  60.  5;  — vanät  '/a  (als  Subj.)^>  aJtqm  drujim  Yt ^9-  9S>  —  agvayoHt  bar?smSjt?rAH  banzyS *-ümi''  zaraÄeMs  (sd.)  drupm  '2.24;  Yt 10.  86  (s.  2  b  a);  —  ks  .  .  yS  'A«  mal- nimnS  'ssm  ispmnö  'spm  aparaoüayeite (sd.)  {'simca  mainimns]  drujimca  vinasti V.  7. 78.  a)  sonst;  a)  im  gA^v.: hyat  akSyä  (sd.)  ängväitl  usta  vi  'sim dädrl  Y.  j/.  8;    —    nSit   3r?s.vacS   sarSm
22632:j.  vanaiti  N.  log:  lies  vinasti,  %.  'vatd-.
24926:\as)mca  mainimns]  drujimca  vlnasti  ".,  der an  das  A.  denkend,  das  A.  suchend  das A.  vernachlässigt  [. .]  und  die  Dr.  findet" V.  7.78".
25012:—  *i^ra  *a^-!vayarjÄpm  {sd.)  yaira  'tu/\2.iT,  —  '%wqm  vJspe.maztUanqm  A-J.i; %wayatgAsm  yaHra  ap>rfnäyakS  ..  N.  — apanS.l?mpm''^wqm..yaitu^lfm3m yaza- 10,  2)  der  Begriff  der  richterlichen  j /u«««  Y.  7/.  3;  Vr.p.  6;  —  tmqm  arahii- Autorität  tritt  völlig  zurück  gegenüber  dem '_)'amÄi  *a/ajqm^a  '^wamca  ratu/rifim[ea] der  Autorität  überhaupt  Jedes  Wesen  der  1  Y.  j.  4;  —  mq^rahe  spgntahe  'äaiff  &ttr. Ala^iAx.,    das   auf  irgend   einem   Gebiet  Ij;  —  datahe  .  .  vidarvahe  . .  '%wd  Extr.
HUB.txt:6196:apam; huvaida 'deutlich*, aus hu + paidd; vdrUn 'inversus,
HUB.txt:7646:und in Humdi (§ 105) sowie in huvaida oflfenbar , hamana
```


## [2026-10-16T05:16:21.122Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 6188,6198p HUB.txt; sed -n 7640,7648p HUB.txt; grep -n -i 'paidā\\|paida\\b\\|pēdāg\\|paydāg' PHD_mackenzie.txt | head -3; grep -n -i 'paitiš.vaēd\\|paitis.vaed\\|paiti.vaed' BRT.txt | head -3; grep -n '^vaed\\|vaēd-\\b' AVG.txt|head -2"
}
```


### [2026-10-16T05:16:21.512Z] TOOL RESULT

```
badafrdh 'Vergeltung* (Parsenwort), zu korrigiren in pada-
frah ; np. ba (neben pa in padrud u. s. w.) = paz. pa (s.
oben p. 21) mit unerklartem Uebergang von p in b. Dazu
birinj *Kupfer = arm. plinj, s. oben p. 27 — 28. Das von
Brockelmann, Lexicon syriacum p. 288 angefiihrte syr.
:ii1£» 'cyprum' ist nach N 6 Id eke unsicher.
Ap. p nach Vokalen = np. v oder b (iiber mp. w);
§ 66. Ap. p = np. 2^ in : avam, vam ^) Schuld = phi.
apam; huvaida 'deutlich*, aus hu + paidd; vdrUn 'inversus,
perversus, infaustus' = paz. awarUn *schlecht', phi. dparun
Gl. and Ind. 9; zdv *Spalt*, (?) s. oben p. 68 und 70; kavtis
skr. suvapus' (oben p. 57); xujasta gesegnet, gliicklich' =
zd. ^hujasta-; xurram^) *fr5hlich*, s. oben p. 55.
Ueber xun *Blut' siehe oben p. 58; iiber a?fm oben
p. 59 ; iiber vorgeschlagenes x Kap. 31 ; iiber xu- = a?^a-
§ 108.
Dagegen blieb u in den erwahnten huilVj hujtr sch5n'
und in Humdi (§ 105) sowie in huvaida oflfenbar , hamana
fiir humand (s. oben p. 106), also in Zusammensetzungen
mit hU' = zd. hu- *gut'. Im Paz. liegt x vor in xunar
```


## [2026-10-16T05:16:27.621Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -6196 HUB.txt | tr -cd '\\f' | wc -c; awk 'BEGIN{RS=\"\\f\"} NR==203' HUB.txt | head -3; grep -n -i 'paydag\\|paydāg\\|pēdāg\\|paidag' PHD_mackenzie.txt | head -3; grep -n -i 'abestag\\|abastāg\\|abestāg\\|apastak' PHD_mackenzie.txt NYB_vol2_glossary.txt | head -4"
}
```


### [2026-10-16T05:16:28.018Z] TOOL RESULT

```
185
'messe*, up. pati-ma., paivastan Verbinden*, paz. paivasian
Min. Gl. 153, \M.patvastan, SLvm. pafvast 'ty^svxQtmq; payam
aus und neben paiyam *Botschaft', phi. paitdm oder paytam
4138:paydagenidan, payda~en- [pyt'kyn-ytn' I M pyd'gy"yd] reveal,
4140:payda~ihistan, paydagih- [pyt'kyh-stn l ] appear, be revealed.
6513:   yawedan.                                        explain paydagenidan, wizardan.
PHD_mackenzie.txt:782:abestag ['p(y)st'k ] Avesta, the Mazdean scriptures.
PHD_mackenzie.txt:5975:  sahr, £ranwez.                         Avesta abestag.
PHD_mackenzie.txt:7073:   scriptures abestag.                     middle mayan; nemtan.
PHD_mackenzie.txt:11348:abestag                        ,~    te.1' 4,)1    ahesih-                        -~ClY
```


## [2026-10-16T05:16:32.247Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==245 || NR==246' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i 'ueid\\|u̯eid\\|sehen\\|wissen\\|vaēd\\|vaed\\|236\\|237' | head -12; grep -n -i '^ *u̯eid\\|^ *ueid\\|^weid\\|^ *woid' IEC.txt | head -5"
}
```


### [2026-10-16T05:16:32.564Z] TOOL RESULT

```
6:236                                                                [vjeit-]   — neid
78:  2. ueid-     „erblicken, sehen“, Pf. uoida „liabe gesehen, weiB", woher die
79:          Bed. „wissen“ auch auf andere Formen iibertragen wurde. Aus der
81:       Ai. cdti. vidmdsi, viddnti ,,wissen“ (praesentische Umbildung des Pf. reda
85:                             germ,            w/tan), viddti (ebenso               )   „wissen“, Pf. veda vidmd           ,
90:  „sehen‘- in aiioi-visam „habe wahrgenommen“, paitivlsdm       wurde gewahr                                  ,
99:  wohl zur Basis *nidei-,                                    s.   u.);   inf.    ai.    vidmune (= gr. id/uevai) „wissen“,
107:Heidelbg. Ak. 1919,                 X7           f.,    1 7 f.) ;     Ivaus. ai. vedayati „la£St wissen, kiindigt
108:an. bietet an", av. usvavdayeiti „la8t wissen“.
110:kaiis.       vedayati, av. vidaiti, vinasti, vTvaeda                                    ,
111:                                                                                             voividaiti (konj.), kaus. vaedo-
113:Die Seheidung von den Pormen der Bed. „sehen, wissen" Bartholomae
19845:ueid- (uid-) “see; look; appear; show; watch; know'. Cf. uoid-, uid-. WP I, 237 Tokh. A cf. wit-, v. ‘see, look’; Arm. gitem, gitnam, v. ‘know; learn’; Gk. eidéso, Doric idéso, v. “shall know? beside Hom. eídomai, mp. “appear; am seen’; Lat. cf. video, ere, pf: vidi, v. ‘see, look’; MHG wizen sv 1. “observe; reprove’; Go. cf. witan, wv. “look at, see? be- side faír-weitjan, wv. “look around: id-weit- jan, wv. ‘despise’; G weisen, v. ‘show’; ver- weisen, v. ‘reproach’: OE witan, v. ‘guard, watch": Du. wijten v. “attribute; reproach’; Mir fíadaim, v. ‘declare, proclaim’; ar-fía- daim, id., cf. also as-ind-fédim, v. “narrate, set forth’; Ir. féadaim, v. ‘I can’; ní féid ʻI cannot'; defective: féadar *I know'; type *uid- in W gwŷdd, m. ‘knowledge’; OCS and com. Sl. vizdo, viděti, v. ‘see’; OLith. veizdmi, v. ‘see’; mod. véizdZiu, veizdéti, v. look; Latv. (o-gde?) cf. viedu & viedēju, viedét, v. ‘see, ob- serve’. Nominal types: Av. cf. vidus, adj. (knowing, fr. *uid-); Gk. eidos, eos, n. “shape, aspect’; cf. also óneidos, n. (*blame, shame’. To ónomai, v. see uon- (2) below); Go. cf. id- weit, OE ed-wit, n. ‘scorn’; Lat. cf. form-1ido,
19856:ueidolos (ueidel-, ueidul-) “sight, image, shape'. Cf. ueid-, uid-, uidul- Gk. cf. eidál-imos, adj. ‘good-looking’; a-eíde- los ‘unseen, dark’; eidüllion, n. ‘idol’; Go. cf. faír-weitl, n. ‘theatre’; Srb. vidjelo, n. "light"; OPr. weidulis, s. “pupil of the eye’; Li. cf. vei- zÓlas, m. usu. -lai, mpl. (dial.) ‘staring eyes’; pa-vyduolis, s. *jealous person”
19857:ueids- (ueidso, io, ueidsaio), extn. of type ueid-, q.v. in Gk. eísomai, v. ‘shall know’; Lat. viso, Ere, v. “see, survey, visit; OS wisian, wv. “show, de- clare, teach? beside wison, v. ‘visit, frequent, pester’; MHG wisen, wv. ‘show, teach; guide; warn; seek, visit’; ON vísa, v. ‘show’; vísi, m. “leader”?
```


## [2026-10-16T05:16:35.642Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -m3 '^penguin' KLN_1971.txt SKT.txt; grep -n -i -m2 '^guide' KLN_1971.txt SKT.txt; grep -n -i -m2 '^history\\b\\|^story' SKT.txt; grep -n -i -m2 '^television' KLN_1971.txt; grep -n -i -m2 '^video' KLN_1971.txt"
}
```


### [2026-10-16T05:16:35.984Z] TOOL RESULT

```
SKT.txt:13716:Penguin,  Pinguin,  a  bird.  (C a  tract  piinlcd  m  i<;>>8,  we  read  thi Drake  gave  a  certain  island  the  r Penguin  Island  in  1587,  from  the  { found  there.  The  word  appei pen  £iv)'n,  i.  e.  white  head.  If rirst  have  been  given  to  another the  auk  (the  puOin  is  common  in  An since  the  penguin's  head  u  black.
KLN_1971.txt:177344:penguin, n. — Compounded of W. pen, ‘head’, 
KLN_1971.txt:177441:penguin. 
KLN_1971.txt:6470:guide’, L. ago, ‘I drive, lead’. See agent and cp. 
KLN_1971.txt:9298:guide, govern ; to do, act’, whence agmen , ‘army, 
SKT.txt:8115:Guide.  (F.^Teut.)  Vi.Z.  gyden  (also gyen'\  —OF.  guider,  to  (^juide.  Cf.  Ual. piidare,  Span,  guiar.  The  gu  (for  w) shews  the  word  lo  be  of  Tcul.  origin ;  it  must be  from  a  <.onrce  allied  to  Goth,  wi/an.  to watch,  observe,  and  to  A.  S.  wifan,  to know.  The  orig.  sense  was  '  to  shew  ;'  cf. Icel.  viti,  a  leader,  si^'nal,  A.S.  witan,  to observe      Allied  to  ^^'it,
18629:story  (2\  set  of  rooms  on  a  level  or  (laL (F.  —  L.)  Orig.  merely  'a  building'  or '  thing  built'  -  O.  F.  tsfor^t,  %  tiling built;  fem.  of  pp.  of  tstertr.  to  build.  ~ Low  L.  staurart*,  put  for  L.  instaurart,  lo con&.tnJcl,  build,  Slc.  See  Store.  Der fUnstorjf^  i.e.  cUar-story,  %\orf  lighicd with  wmdowt,  as  distinct  from  Ui tttry.
18638:Story  ( 1 ),  a  oamtive ;  see  History.
242866:television, n. — Lit. ‘seeing at a distance’, a hy-
```


## [2026-10-16T05:16:38.529Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 177344,177348p KLN_1971.txt; sed -n 242866,242870p KLN_1971.txt; grep -n -i -m3 'guide, v\\.\\|^guide,' KLN_1971.txt; grep -n -m2 -i '^history, n' KLN_1971.txt; grep -n -m2 -i '^visit, ' KLN_1971.txt"
}
```


### [2026-10-16T05:16:38.957Z] TOOL RESULT

```
penguin, n. — Compounded of W. pen, ‘head’, 
and gwyn, ‘white’. The name orig. denoted the 
garefowl (also called the great auk), in allusion 
to the large white patch between the bill and the 
eye of this bird, now extinct. For the first ele- 
television, n. — Lit. ‘seeing at a distance’, a hy- 
brid coined by Hugo Gernsback in 1911 fr. Gk. 
TvjXe, ‘far off, at a distance', and L. visid, gen. 
- onis , ‘the act of seeing, sight'. See tele- and 
vision. 
9298:guide, govern ; to do, act’, whence agmen , ‘army, 
15878:guide, lead, rule’. See regent, adj., and cp. 
107138:guide, tr. v. — ME. guiden , guyden , gyden, fr. F. 
114338:history, n. — L. historia, ‘narrative, story, nar- 
262953:visit, tr. and intr. v. — ME. visiten, fr. OF..( =
```


## [2026-10-16T05:16:41.948Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 107138,107145p KLN_1971.txt; sed -n 114338,114345p KLN_1971.txt; sed -n 262953,262958p KLN_1971.txt; mkdir -p ocr/BOOK; cp /home/sfmqrb/git/rishe-private/site/pages/534.jpg ocr/BOOK/534.jpg; pdftoppm -f 534 -l 534 -r 150 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf ocr/BOOK/534 && ls ocr/BOOK/534*"
}
```


### [2026-10-16T05:16:43.009Z] TOOL RESULT

```
guide, tr. v. — ME. guiden , guyden , gyden, fr. F. 
guider , ‘to guide, lead, conduct’, refashioned— 
after the noun guide — fr. OF. guier (whence 
ME. gyen), ‘to guide, lead’, which derives fr. 
Frankish *witan, ‘to show’ (whence also OProv- 
eng. guidar, guizar). Cp. OS. ms tan, ON. visa, 
Dan. vise, Swed., Norw. visa, OFris. wi$a, 
MDu. wisen, Du. wijzen, OHG., MHG. wisen, 
history, n. — L. historia, ‘narrative, story, nar- 
ration, account’, fr. Gk. Icxopla, ‘learning by 
inquiry, knowledge obtained by inquiry; ac- 
count of one’s inquiries; narration, historical 
narrative; history’, fr. I'cmop (Boeot. Ftcxcop), 
‘knowing, learned’, which stands for *fi8xwp 
and is rel. to oI8a (for *FoT8a), ‘I know’, el&ov 
(for *£fi8ov), ‘I saw’, ISetv (for *FtSetv), ‘to 
visit, tr. and intr. v. — ME. visiten, fr. OF..( = 
F.) visiter, fr. L. visitare , { to see frequently, to go 
to see’, freq. of visere , ‘to look at often or at- 
tentively’, itself a freq. of videre (pp. visus ), ‘to 
see’. See prec. word. 

Permissions Size User   Date Modified Name
.rw-r--r--   74k sfmqrb 16 Oct 01:16  ocr/BOOK/534.jpg
.rw-r--r--   61k sfmqrb 16 Oct 01:16  ocr/BOOK/534.png
```


## [2026-10-16T05:16:55.091Z] TOOL CALL #38: Bash

```json
{
 "command": "rm /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/534.jpg; mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad"
}
```


### [2026-10-16T05:16:55.436Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:19:44.734Z] TOOL CALL #39: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-534.py",
 "content": "import json\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE = W + \"Reconstruction:Proto-Indo-European/weyd-\"\nPOKQ = \"POK_full.txt line 89176 ff. 'Root / lemma: u(e)id-2 Meaning: to see; to know ... Page(s): 1125-1127'\"\nAHDQ = \"AHD_watkins1985.txt line 1135 s.v. 'weid-. To see.'\"\n\ndef rc(ref, status, note):\n    return {\"ref\": ref, \"status\": status, \"note\": note}\n\ndef cs(src, where, stance, note):\n    return {\"src\": src, \"where\": where, \"stance\": stance, \"note\": note}\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"vaeda, vîdada; vîd-; vidya; vista-; hu-vaeda\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"Av. vaēda 'I know / he knows' is the old perfect of *u̯oid-a (PIE perfect *wóyd-e, = Skt veda, Gk oida, Goth. wait); vīd- 'knowing, partaking' is the root noun, vīdyā- 'knowledge' (= Skt vidyā) and vista- 'known, found' the -ta participle *wid-tó- (dental cluster d+t > st as in Iranian generally). All four are in Pokorny, Bartholomae and Cheung (*u̯aid¹). But 'vîdada' is not an Avestan form: Pokorny and Walde-Pokorny print 'Avestan vaēda vīdarə' (3 pl. perfect 'they know'), so the book's vîdada is a misprint for vīδarə. 'hu-vaeda' 'well known, apparent' is not attested in Avestan (not in Bartholomae or Cheung); it is Nourai's back-projection of NP hoveydā following Mo'in/Bahar's analysis hu- + vīdā (BQT 2401 fn.). The JSON reproduces the printed page; the error is in the book.\",\n \"derivation_fa\": \"«vaēda» در اوستایی ماضی نقلی کهن به معنی «می‌دانم / می‌داند» است (هم‌ریشه با سنسکریت veda، یونانی oida و گوتی wait) و vīd- «دانا»، vīdyā- «دانش» و vista- «دانسته، یافته» نیز همه از ریشهٔ هندواروپایی *weyd- «دیدن، دانستن» گواهی شده‌اند (پوکورنی، بارتولومه، چونگ). اما «vîdada» صورت اوستایی نیست و خطای چاپی کتاب به جای vīδarə «می‌دانند» است که پوکورنی آورده؛ و «hu-vaeda» در اوستا گواهی نشده و بازسازی خود نورایی از روی «هویدا» است. پس ریشه درست است ولی دو صورت از این خانه خطای چاپی یا ساختگی است.\",\n \"error_in\": \"book\",\n \"book_prints\": \"vaeda, vîdada ... hu-vaeda\",\n \"correct_form\": \"vaēda, vīδarə (3 pl. perf.); no Avestan *hu-vaēda (only NP hoveydā)\",\n \"sources\": [PIE],\n \"ref_check\": [\n  rc(\"POK:1125\", \"supports\", POKQ + \": 'Avestan vaeda vTdare, Opt. vTdyal, vTdva ... know' ; 'participle ... Avestan vista- known as' ; 'Avestan vīd- teilhaftig' ; 'Avestan vidya ds.' — supports vaēda, vīd-, vīdyā, vista-; prints vīdarə where Nourai has vîdada; no hu-vaēda.\"),\n  rc(\"POK:1126\", \"partial\", \"same lemma p.1126 (nominal formations): 'Old Indic vidya Wissen, doctrine, Avestan vidya ds.' — supports vidya only.\")\n ],\n \"consulted\": [\n  cs(\"CHEUNG\", \"pp. 408-409 s.v. *u̯aid¹ 'to know' (CHEUNG.txt line 26507 ff.)\", \"supports\", \"'AVESTAN: vid- (vīδ-, vaēd-, vaēδ-) to know ... Perf.: IND. 1sg. OAv. vaēdā ... 3pl. YAv. vīδarə ... perf. pass. YAv. vista-' — no hu-vaēda.\"),\n  cs(\"WLD\", \"Bd. I p. 236-237 (WLD_Bd1_pages.txt leaf 245-246) s.v. 2. u̯eid-\", \"supports\", \"'erblicken, sehen, Pf. u̯oida habe gesehen, weiß ... av. vaēda vīδarə'\"),\n  cs(\"BRT\", \"BRT.txt grep 'vīnasti/vidarə'\", \"silent\", \"OCR of the Avestan headwords too noisy to locate vaēd- 'wissen' directly; no hu-vaēda found (grep 'huvaed' = 0 hits).\"),\n  cs(\"IEC\", \"IEC.txt line 19845 s.v. ueid-\", \"supports\", \"'Nominal types: Av. cf. vidus, adj. knowing, fr. *uid-'\")\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"vîdâ; Avestâ; hovaydâ\",\n \"verdict\": \"disputed\",\n \"derivation\": \"vīdā (ویدا) is a lexicographers' word: Borhan p.2297-2298 gives it as = vīd 'lost, vanished, little', and also 'هویدا و ظاهر' 'apparent'; Mo'in's dictionary glosses it آشکار، پیدا. No Middle Persian antecedent is known, so its link to Av. vaēd- is speculative. hoveydā 'evident' (MP *huwēdāg) is explained by Mo'in (BQT 2401 fn., following Bahar) as Av. hu- 'good' + vīdā; but Hübschmann (Persische Studien §66, p.175) derives it from hu- + paidā (= peydā, MP paydāg 'visible', from *pati-dā-, root *dī 'see'), with intervocalic p > v, and Wiktionary calls it 'Unknown' — so the *weyd- link is at best one of two views. Avestā is the weakest: it continues MP abestāg ['p(y)st'k] 'the Mazdean scripture' (MacKenzie), whose origin is unclear; the usual proposals are *upa-stāvaka- 'praise' or *abi-stāka- 'foundation, basic text', not *ā-vista- 'knowledge'. The 'well known, knowledge' gloss is folk etymology. The node is therefore disputed for Avestā, uncertain for hoveydā and vīdā.\",\n \"derivation_fa\": \"«ویدا» واژه‌ای فرهنگ‌نامه‌ای است که برهان قاطع آن را هم به معنی «گم و ناپیدا» (= وید) و هم به معنی «هویدا و ظاهر» آورده و پیشینهٔ فارسی میانه ندارد؛ پیوندش با vaēd- اوستایی حدسی است. «هویدا» را معین در حاشیهٔ برهان (به پیروی از بهار) از hu- «خوب» + «ویدا» دانسته، اما هوبشمان آن را از hu- + «پیدا» (فارسی میانه paydāg) با ابدال پ به و می‌داند و ویکی‌واژه ریشه‌اش را نامعلوم می‌خواند. «اوستا» از فارسی میانهٔ abestāg است که ریشه‌اش روشن نیست (پیشنهادهای رایج: *upa-stāvaka- «ستایش» یا «بنیاد، متن اصلی») و معنی «دانش، شناخته» ریشه‌شناسی عامیانه است. پس ادعای نورایی دربارهٔ «اوستا» را پژوهش امروزی نمی‌پذیرد و دربارهٔ دو واژهٔ دیگر محل تردید است.\",\n \"sources\": [W + \"اوستا\", W + \"هویدا\", \"https://vajehyab.com/moein/ویدا\", \"https://vajehyab.com/moein/هویدا\", \"https://vajehyab.com/moein/اوستا\"],\n \"ref_check\": [\n  rc(\"BQT:2297\", \"partial\", \"ref_page.py BQT:2297 (BQT_v4 pdf 380; page image read, saved as ocr/BQT/2297.vision.txt): 'ویدا - بکسر اول بروزن بیجا، بمعنی وید است که گم و ناپیدا و ناپدید گشته - و کم و ناقص ... و بمعنی پیدا' continued on p.2298 'وهویدا وظاهرهم آمده است'. Mo'in's footnote on وید/Veda: 'Veda از ریشهٔ vid بمعنی دانستن است' — the vid- etymology is given for Skt Veda, not for ویدا.\"),\n  rc(\"BQT:2401\", \"supports\", \"ref_page.py BQT:2401 (BQT_v4 pdf 484), s.v. هویدا 'بمعنی ظاهر و روشن و بین باشد'; Mo'in fn.: 'از hu اوستایی بمعنی خوب + ویدا (= پیدا) مرحوم بهار در حواشی ... لغت فرس ... همین گونه اظهار عقیده کرده‌اند' — supports hoveydā < hu + vīdā.\"),\n  rc(\"MON:5069\", \"not_checked\", \"Mo'in vol. 5 (proper names, s.v. Avestā presumably); print page not online. Online Mo'in lexicon (vajehyab) s.v. اوستا only: 'کتاب دینی زرتشتیان' — no etymology.\"),\n  rc(\"MON:5669\", \"not_checked\", \"Mo'in vol. 5/6 page not accessible; online Mo'in s.v. ویدا '(ص.) آشکار، پیدا', s.v. هویدا '1 - آشکار، پیدا' — meanings confirmed, no etymology.\")\n ],\n \"consulted\": [\n  cs(\"HUB\", \"§66, p.175 (HUB.txt line 6196, leaf 185)\", \"contradicts\", \"'Ap. p nach Vokalen = np. v oder b ... huvaidā deutlich, aus hu + paidā' — hoveydā from hu + peydā, not from vaēd-.\"),\n  cs(\"PHD\", \"p. 4 (PHD_mackenzie.txt line 782)\", \"partial\", \"'abestāg [ʾp(y)stʾk] Avesta, the Mazdean scriptures' — MP form confirmed, no 'knowledge' sense or etymology.\"),\n  cs(\"NYB\", \"NYB_vol2_glossary.txt grep 'abestāg/apastāk'\", \"silent\", \"no hit in the OCR.\"),\n  cs(\"HRN\", \"HRN.txt grep 'huvaid/hoveid'\", \"silent\", \"Horn has no entry for hoveydā or vīdā.\"),\n  cs(\"MON\", \"vajehyab Mo'in s.v. ویدا, هویدا, اوستا\", \"partial\", \"ویدا '(ص.) آشکار، پیدا'; هویدا 'آشکار، پیدا'; اوستا 'کتاب دینی زرتشتیان' — meanings only.\")\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Avestan\",\n \"words\": \"vîdaiti, vînosti, vîvaĕda; paitiš-vaĕd\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The 'find' verb is the same PIE *weyd- (Pokorny: 'from the meaning behold derives find'), Iranian *u̯aid² (Cheung): Av. vīδaiti (thematic aorist subj. 'finds'), vīnasti (nasal present *wi-n-ad-ti = Skt vindati), vīvaēδa (perfect) are all attested. The book prints 'vînosti', a misprint for vīnasti (Pokorny, Bartholomae V.7.78 'drujimca vīnasti', Cheung). 'paitiš-vaēd' 'to search for' is not attested Avestan: it is Horn's reconstruction 'aw. *paitiš + vaēd-' (starred in Horn p.70) for NP pažūhīdan; Avestan only has paiti.vaēδaya- 'make known' (Cheung). The JSON follows the printed page; the misprint is the book's.\",\n \"derivation_fa\": \"فعل اوستایی «یافتن» نیز از همان ریشهٔ *weyd- است (پوکورنی: از «دیدن» معنی «یافتن» برآمده) و صورت‌های vīδaiti «می‌یابد»، vīnasti (مضارع با میانوند n، هم‌ریشه با سنسکریت vindati) و vīvaēδa (ماضی نقلی) در اوستا گواهی شده‌اند. «vînosti» در کتاب خطای چاپی به جای vīnasti است. «paitiš-vaēd» به معنی «جستجو کردن» در اوستا وجود ندارد و صورت ستاره‌دار و بازسازی‌شدهٔ هرن برای توضیح «پژوهیدن» است. پس صورت‌ها درست‌اند ولی یکی غلط چاپی و یکی ساختگی است.\",\n \"error_in\": \"book\",\n \"book_prints\": \"vînosti; paitiš-vaĕd\",\n \"correct_form\": \"vīnasti; *paiti-š + vaēd- (Horn's reconstruction, unattested)\",\n \"sources\": [PIE],\n \"ref_check\": [\n  rc(\"POK:1121\", \"not_found\", \"POK p.1121 is the lemma 1. u̯ei- / u̯eiə- 'to turn, twist'; the 'find' forms are on p.1125: 'In the meaning find: ... Avestan vīδaiti, vīnasti, vīvaēda, voiviδait (Konj.)' (POK_full.txt line ~89205). Nourai's page number is off.\"),\n  rc(\"HRN:70\", \"supports\", \"HRN.txt leaf 92 = p.70, end of no. 314 pizōhīden: 'phlv. patv(i)hītan ... aw. *paitiš + vaēd- [caus. vaēdayēmi] ai. prati + vid' — Horn himself stars the Avestan compound.\"),\n  rc(\"AEF:379\", \"not_checked\", \"Khaleqi Motlaq's translation of Horn is not available; it should reproduce Horn no. 314.\")\n ],\n \"consulted\": [\n  cs(\"CHEUNG\", \"p. 409-410 s.v. *u̯aid² 'to find' (CHEUNG.txt line 26590 ff.)\", \"supports\", \"'AVESTAN: vaēd- (vaēδ-, vid-, viδ-) to find ... Pres. n-: IND. 3sg. OAv. vīnastī ... Aor. ... SUBJ. 3sg. YAv. vīδāiti ... Perf.: IND. 3sg. YAv. vīuuaēδa'.\"),\n  cs(\"BRT\", \"col. 1313 (BRT.txt line 24926)\", \"supports\", \"'drujimca vīnasti ... und die Dr. findet V. 7.78' — vīnasti, not vīnosti.\"),\n  cs(\"WLD\", \"Bd. I p. 237 (WLD_Bd1_pages.txt leaf 246)\", \"supports\", \"'kaus. vedayati, av. vīδaiti, vīnasti, vīvaēda, voiviδaiti (konj.)'\"),\n  cs(\"HUB\", \"p. 41 no. 314 (HUB.txt line 1384)\", \"contradicts\", \"'314. Der Paragraph ist vollkommen verfehlt und zu streichen ... Ich lehne also np. pis- aus patiš ... ab' — the NOTE in the chart is accurate.\")\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"pažuhîdan\",\n \"verdict\": \"disputed\",\n \"derivation\": \"NP pažūhīdan / pižōhīdan 'to investigate', pažūh, pažūheš continue MP wizōy-/wizōh-, wizōstan [wcwstn, wcwd-] 'examine, investigate' (MacKenzie, who gives the NP descendant 'pizōhīdan'), with MP initial w- > b- and then b > p (Wiktionary). Cheung places the MP verb under Ir. *čaud 'to urge, impel' with preverb *wi- (*wi-čaud- > wizōy-), noting NP pizōhīdan. Horn's derivation (no. 314) from Av. *paitiš + vaēd- 'find', which Nourai follows, was rejected already by Hübschmann (§314 'vollkommen verfehlt') as the chart's NOTE says; modern scholarship sides with Hübschmann.\",\n \"derivation_fa\": \"«پژوهیدن» و «پژوه» و «پژوهش» از فارسی میانهٔ wizōy- / wizōstan «بررسی کردن، جستجو کردن» آمده‌اند؛ w آغازین فارسی میانه نخست به b و سپس به p بدل شده است (مکنزی، ویکی‌واژه). چونگ این فعل را از ریشهٔ ایرانی *čaud «برانگیختن» با پیشوند *wi- می‌داند. ریشه‌شناسی هرن (از *paitiš + vaēd- اوستایی «یافتن») که نورایی پذیرفته، همان است که هوبشمان آن را «سراسر نادرست» خوانده و پژوهش امروزی نیز آن را رد می‌کند؛ پس پیوند «پژوهیدن» با ریشهٔ *weyd- پذیرفتنی نیست.\",\n \"sources\": [W + \"پژوهیدن\", W + \"پژوهش\"],\n \"ref_check\": [\n  rc(\"AEF:379\", \"not_checked\", \"Khaleqi Motlaq (Persian Horn translation) not accessible; it renders Horn no. 314 (HRN p.69-70), which does make this claim: '314. pizōhīden erforschen, nachfragen, pizōh, pizōhiš ... aw. *paitiš + vaēd-'.\")\n ],\n \"consulted\": [\n  cs(\"PHD\", \"p. 93 (PHD_mackenzie.txt line 5503)\", \"contradicts\", \"'wizōstan, wizōh/y- [wcwstn, wcwd- (J bzwh-, N pizūhidan)] examine, investigate' — the MP etymon has wi-, not paitiš.\"),\n  cs(\"CHEUNG\", \"p. 40 s.v. *čaud (CHEUNG.txt line 3570-3576)\", \"contradicts\", \"'*čaud to urge to, impel ... MIDDLE PERSIAN: (+ *ui-) BMP wcwd- /wizōy-/ (or /wizoh-/?) to examine, investigate ... NWIR: ... (+ *?) NP pizōhīdan/pizōh- to investigate (LW)'.\"),\n  cs(\"HUB\", \"p. 41 no. 314 (HUB.txt line 1384)\", \"contradicts\", \"'314. Der Paragraph ist vollkommen verfehlt und zu streichen. Vgl. Fr. Müller ... (pižōhīdan = pati + š + Wzl. von np. jōstan, vgl. phl. vijustan)'.\"),\n  cs(\"HRN\", \"pp. 69-70 no. 314 (HRN.txt leaf 91-92)\", \"supports\", \"'314. pizōhīden erforschen, nachfragen ... aw. *paitiš + vaēd- ... ai. prati + vid'.\")\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Latin\",\n \"words\": \"viděre, visus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin vidēre 'to see', perfect vīdī, participle vīsus (< *weid-to- with -dt- > -ss- > -s- after long vowel), is the PIE stative *wid-éh₁-ye- 'be seeing' (Proto-Italic *widēō), cognate with OCS viděti and Lith. pavydėti. Watkins lists it as 'Form *wid-ē- (with participial form *weid-to-) in Latin vidēre (past participle vīsus), to see, look'.\",\n \"derivation_fa\": \"لاتینی vidēre «دیدن» با صفت مفعولی vīsus از ستاک *wid-ē- هندواروپایی (فعل حالت «در حال دیدن بودن») آمده و با اسلاوی کهن viděti هم‌ریشه است؛ vīsus از *weid-to- با همگونی dt به ss ساخته شده است. ادعای نورایی درست است.\",\n \"sources\": [PIE],\n \"ref_check\": [\n  rc(\"AHD\", \"supports\", AHDQ + \": '4. Form *wid-ē- (with participial form *weid-to-) in Latin vidēre (past participle vīsus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA ...'\")\n ],\n \"consulted\": [\n  cs(\"POK\", \"p. 1125 \" + \"(POK_full.txt line ~89225)\", \"supports\", \"'Latin video, -ēre see (from the basis *u(e)idē-) ... Perf. vīdī ... participle vīsus'\"),\n  cs(\"WLD\", \"Bd. I p. 237\", \"supports\", \"u̯eid- with Lat. videō listed in the same entry.\"),\n  cs(\"IEC\", \"IEC.txt line 19845 s.v. ueid-\", \"supports\", \"'Lat. cf. video, ēre, pf. vīdī, v. see, look'\")\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"French\",\n \"words\": \"television; visite\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French visite 'visit' is a deverbal noun of visiter < Latin vīsitāre 'to see often, go to see', frequentative of vīsere, itself a frequentative of vidēre (Klein). télévision is a learned hybrid of Greek tēle 'far' + Latin vīsiō 'seeing' (vīsiō < vīs-, participle of vidēre), coined around 1900 (French télévision, Perskyi at the Paris exposition; Klein credits the English form to Gernsback 1911); Persian took both words from French.\",\n \"derivation_fa\": \"فرانسوی visite از فعل visiter و آن از لاتینی vīsitāre «بارها دیدن، به دیدار رفتن» (بسامدی vīsere و آن از vidēre) است؛ télévision واژه‌ای دورگه از یونانی tēle «دور» و لاتینی vīsiō «دیدن» است که حدود سال ۱۹۰۰ ساخته شد. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [rc(\"None\", \"not_checked\", \"no reference cited by Nourai for this node.\")],\n \"consulted\": [\n  cs(\"KLN\", \"KLN_1971.txt line 262953 s.v. visit\", \"supports\", \"'visit ... fr. OF. (= F.) visiter, fr. L. visitare, to see frequently, to go to see, freq. of visere, ... itself a freq. of videre (pp. visus), to see'\"),\n  cs(\"KLN\", \"KLN_1971.txt line 242866 s.v. television\", \"supports\", \"'television, n. — Lit. seeing at a distance, a hybrid coined by Hugo Gernsback in 1911 fr. Gk. τῆλε, far off, and L. visio, gen. -onis, the act of seeing'\"),\n  cs(\"AHD\", AHDQ, \"partial\", \"lists VISION, VISA under vidēre; television/visit not listed separately.\")\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Persian\",\n \"words\": \"televîzion; vîzît\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian televizion تلویزیون and vizit ویزیت 'visit; a doctor's visit, consultation fee' are 20th-century loans from French télévision and visite (Mo'in tags both [فر.]); the parenthetical ویزا vizā 'visa' is French visa < Latin vīsa 'things seen' (neuter plural participle of vidēre). Persian keeps the French vowels, rendering French é/e by e and -ion as -iyon.\",\n \"derivation_fa\": \"«تلویزیون» و «ویزیت» (دیدار، دیدار پزشک از بیمار) در سدهٔ بیستم از فرانسوی télévision و visite به فارسی آمده‌اند و معین هر دو را [فر.] نشان داده است؛ «ویزا» نیز از فرانسوی visa و آن از لاتینی vīsa «دیده‌شده‌ها» است. ادعای نورایی درست است.\",\n \"sources\": [\"https://vajehyab.com/moein/تلویزیون\", \"https://vajehyab.com/moein/ویزیت\", W + \"تلویزیون\"],\n \"ref_check\": [\n  rc(\"MON:1136\", \"supports\", \"print page not online; the same Mo'in entry on vajehyab s.v. تلویزیون: '[فر.] (اِ.) دستگاهی است که تصاویر ... از مسافت دور ... انتقال دهد'.\"),\n  rc(\"MON:5071\", \"supports\", \"print page not online; Mo'in on vajehyab s.v. ویزیت: '[فر.] (اِ.) 1 - دیدار، بازدید. 2 - ملاقات بیمار از طرف پزشک'.\")\n ],\n \"consulted\": [\n  cs(\"MON\", \"vajehyab Mo'in s.v. تلویزیون, ویزیت\", \"supports\", \"both tagged [فر.] (French).\"),\n  cs(\"KLN\", \"s.v. television, visit\", \"supports\", \"French/Latin chain as in node #6.\"),\n  cs(\"AMD\", \"not fetched for these words\", \"silent\", \"not consulted\")\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"English\",\n \"words\": \"view, review, interview, advice, envy, evident, vision, television, visa, visit, provide, survey, video\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All from Latin vidēre/vīsus, mostly via (Anglo-)French: view and review < AF vewe, OF veue (fem. pp. of veoir < vidēre); interview < MF entrevue; advice < OF avis (ce m'est a vis < Lat. mihi est vīsum); envy < OF envie < Lat. invidia (invidēre 'look askance at'); evident < Lat. ēvidēns; vision < OF < vīsiō; visa < F visa < vīsa; visit < OF visiter < vīsitāre; provide < Lat. prōvidēre; survey < AF surveier < Med. Lat. supervidēre; television hybrid (Gk tēle + vision, 20th c.); video (1935) is Latin vidēo 'I see' used as a noun. Watkins lists almost all of these under weid-.\",\n \"derivation_fa\": \"همهٔ این واژه‌های انگلیسی از لاتینی vidēre / vīsus هستند و بیشترشان از راه فرانسوی کهن یا فرانسوی-نورمن آمده‌اند: view و review از veue، advice از avis، envy از invidia، survey از supervidēre، visit از vīsitāre؛ television دورگهٔ یونانی-لاتینی است و video (۱۹۳۵) همان vidēo لاتینی «می‌بینم» است. واتکینز همه را زیر ریشهٔ weid- آورده است؛ ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [rc(\"None\", \"not_checked\", \"no reference cited by Nourai for this node.\")],\n \"consulted\": [\n  cs(\"AHD\", AHDQ, \"supports\", \"'Latin vidēre ...: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SUPERVISE, SURVEY'\"),\n  cs(\"KLN\", \"s.v. visit (line 262953), television (line 242866)\", \"supports\", \"visit < OF visiter < L. visitare < videre; television hybrid Gk + L. visio.\"),\n  cs(\"SKT\", \"SKT.txt\", \"silent\", \"not looked up word by word; chain uncontroversial.\")\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Persian\",\n \"words\": \"vîdîyo\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian vidiyo ویدیو is a late-20th-century loan of English (or French vidéo) video, itself Latin vidēo 'I see', 1st sg. of vidēre; the glide -iy- breaks the hiatus i-o in Persian.\",\n \"derivation_fa\": \"«ویدیو» در اواخر سدهٔ بیستم از انگلیسی video (یا فرانسوی vidéo) به فارسی آمده و آن خود صیغهٔ اول شخص لاتینی vidēo «می‌بینم» از vidēre است. ادعای نورایی درست است.\",\n \"sources\": [W + \"ویدیو\"],\n \"ref_check\": [rc(\"None\", \"not_checked\", \"no reference cited by Nourai for this node.\")],\n \"consulted\": [\n  cs(\"AHD\", AHDQ, \"partial\", \"VIDE (from vidēre) listed; video not in the 1985 list.\"),\n  cs(\"MON\", \"vajehyab Mo'in s.v. ویدیو\", \"silent\", \"page fetched (420 bytes) but carries no Mo'in entry text.\")\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Welsh\",\n \"words\": \"pen-gwyn\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Welsh gwyn 'white' (fem. gwen) < Proto-Celtic *windo- < PIE *wi-n-d-o- 'clearly visible', the nasalised zero grade of *weyd- (Watkins; Pokorny: Celtic *uindo- 'white'), and pen 'head' < *kʷenno-. English penguin (1570s, first for the great auk, later transferred to the southern birds) is often explained as Welsh pen gwyn 'white head' (Watkins, Klein, Skeat), but the etymology is not certain: Wiktionary calls it 'Uncertain' and gives Latin pinguis 'fat' as an alternative, and Skeat notes the penguin's head is black (the name would fit the auk's white face patch). The Welsh-*weyd- link of gwyn is solid; the penguin derivation is only one of two views.\",\n \"derivation_fa\": \"ولزی gwyn «سفید» از سلتی آغازین *windo- و آن از صورت نون‌دار *wi-n-d- ریشهٔ *weyd- («آشکار و دیدنی») است و pen «سر» است. اینکه انگلیسی penguin (نخست نام مرغ اوک بزرگ) از pen gwyn «سرسفید» باشد را واتکینز، کلاین و اسکیت گفته‌اند، اما ویکی‌واژه ریشهٔ آن را نامطمئن می‌داند و احتمال لاتینی pinguis «چاق» را هم مطرح می‌کند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"penguin\", PIE],\n \"ref_check\": [\n  rc(\"AHD\", \"supports\", AHDQ + \": '7. Suffixed nasalized form *wi-n-d-no- in: a. Irish fionn, white (< clearly visible) ...; b. Welsh gwyn, gwynn, white: PENGUIN'.\")\n ],\n \"consulted\": [\n  cs(\"KLN\", \"KLN_1971.txt line 177344 s.v. penguin\", \"supports\", \"'penguin, n. — Compounded of W. pen, head, and gwyn, white. The name orig. denoted the garefowl (also called the great auk), in allusion to the large white patch between the bill and the eye'\"),\n  cs(\"SKT\", \"SKT.txt line 13716 s.v. Penguin\", \"partial\", \"'The word appears to be Welsh pen gwyn, i.e. white head. If so, it must first have been given to another bird ... the auk ... since the penguin's head is black'\"),\n  cs(\"POK\", \"p. 1125\", \"supports\", \"'also Celtic *uindo- white (Old Irish find, cymr. gwynn)'\")\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"French\",\n \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Pass-through node: French pingouin (17th c.), borrowed from English penguin (or Dutch pinguin); in French it now denotes the auk/razorbill, while the southern bird is manchot, but Persian panguwan was taken from pingouin (Amid: [فرانسوی: pingouin]). The French link is right; the ultimate Welsh origin is uncertain (see #10).\",\n \"derivation_fa\": \"این خانهٔ خالی همان فرانسوی pingouin است که در سدهٔ هفدهم از انگلیسی penguin (یا هلندی pinguin) گرفته شد؛ «پنگوئن» فارسی به گواهی فرهنگ عمید از همین واژهٔ فرانسوی است. پیوند فرانسوی درست است ولی ریشهٔ ولزی واژه قطعی نیست.\",\n \"sources\": [\"https://vajehyab.com/amid/پنگوئن\"],\n \"ref_check\": [rc(\"None\", \"not_checked\", \"no reference cited by Nourai for this node.\")],\n \"consulted\": [\n  cs(\"AMD\", \"vajehyab Amid s.v. پنگوئن\", \"supports\", \"'[فرانسوی: pingouin]'\"),\n  cs(\"MON\", \"vajehyab Mo'in s.v. پنگوئن\", \"supports\", \"'[فر.] (اِ.) پرنده‌ای از راستهٔ پرندگان دریایی و بی پرواز است'\")\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Persian\",\n \"words\": \"panguwan\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian panguwan / pangu'an پنگوئن 'penguin' is a 20th-century loan from French pingouin (Amid: pronunciation /pangu(o)van/, [فرانسوی: pingouin]; Mo'in: [فر.]); French nasal -in /ɛ̃/ is rendered -an.\",\n \"derivation_fa\": \"«پنگوئن» در سدهٔ بیستم از فرانسوی pingouin به فارسی آمده است؛ عمید تلفظ آن را /pangu(o)van/ و اصلش را فرانسوی pingouin آورده و معین نیز آن را [فر.] نشان داده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://vajehyab.com/amid/پنگوئن\", \"https://vajehyab.com/moein/پنگوئن\", W + \"پنگوئن\"],\n \"ref_check\": [\n  rc(\"AMD:487\", \"supports\", \"page number not mappable online; the Amid entry on vajehyab: 'پنگوئن تلفظ /pangu(o)van/ نوع واژه (اسم) [فرانسوی: pingouin] (زیست‌شناسی)'.\")\n ],\n \"consulted\": [\n  cs(\"MON\", \"vajehyab Mo'in s.v. پنگوئن\", \"supports\", \"'[فر.]'\"),\n  cs(\"AMD\", \"vajehyab Amid s.v. پنگوئن\", \"supports\", \"'[فرانسوی: pingouin]'\")\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Greek\",\n \"words\": \"histôr; istoria; idea\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek hístōr (Boeotian wístōr) 'knowing, judge, witness' < *wid-tōr (dental cluster dt > st), whence historeîn 'inquire' and historía 'inquiry, knowledge, narrative, history'; idéā 'form, appearance, idea' < *wid-es-yā. Initial w- was lost in Attic-Ionic; the h- of hístōr is secondary. Pokorny, Watkins and Klein agree.\",\n \"derivation_fa\": \"یونانی hístōr «دانا، داور» از *wid-tōr (با دگرگونی dt به st) و از آن historeîn «پرسیدن، پژوهیدن» و historía «پژوهش، دانش، روایت، تاریخ» ساخته شده؛ idéā «صورت، ظاهر، اندیشه» از *wid-es-yā است. w آغازین در یونانی آتیک افتاده است. ادعای نورایی درست است.\",\n \"sources\": [W + \"ἵστωρ\", PIE],\n \"ref_check\": [\n  rc(\"POK:1127\", \"supports\", POKQ + \" (end of entry, p.1127): 'gr. ἵστωρ, Attic ἴστωρ, Boeotian Fίστωρ wissend, expert, skillful; Schiedsrichter, ἱστορεῖν erkunden, ἱστορία'.\"),\n  rc(\"AHD\", \"supports\", AHDQ + \": '5. Suffixed form *wid-es-yā in Greek idea ...: IDEA; 6. Suffixed form *wid-tor- in Greek histōr, wise, learned ...: HISTORY, (STORY¹)'.\")\n ],\n \"consulted\": [\n  cs(\"KLN\", \"KLN_1971.txt line 114338 s.v. history\", \"supports\", \"'L. historia ... fr. Gk. ἱστορία, learning by inquiry ... fr. ἵστωρ (Boeot. Fίστωρ), knowing, learned, which stands for *Fίδτωρ and is rel. to οἶδα'\"),\n  cs(\"IEC\", \"IEC.txt line 19845 s.v. ueid-\", \"supports\", \"'Gk. eidos, eos, n. shape, aspect'\"),\n  cs(\"WLD\", \"Bd. I p. 238\", \"supports\", \"same u̯eid- entry (Greek ἵστωρ listed in POK's revision of WP I 236 ff.)\")\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Arabic\",\n \"words\": \"ostůreh; asâtîr\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Arabic usṭūra, pl. asāṭīr 'fables' (Qur'an: asāṭīr al-awwalīn 'tales of the ancients'). Two views exist, as the chart's NOTE records: (a) from Greek historía, proposed by Sprenger and Fleischer and adopted by Unaysi (TAD) and by Wiktionary as a phono-semantic match of historía with native saṭara 'to write lines'; (b) Jeffery (FVQ 56-57), following Fraenkel and Nöldeke-Schwally, rejects direct Greek borrowing (with Horovitz) and prefers Aramaic/Syriac šṭārā 'writing, document', from s-ṭ-r 'write', ultimately Akkadian šaṭāru 'to write'. Modern opinion is split, with the Greek etymology (perhaps blended with the s-ṭ-r root) slightly ahead; the chart's main arrow is therefore plausible, and its NOTE fairly states the alternative.\",\n \"derivation_fa\": \"عربی «اُسطوره» و جمع آن «اساطیر» (در قرآن: «أساطیر الأوّلین») دو ریشه‌شناسی دارد: گروهی (اشپرنگر، فلایشر، العنیسی و ویکی‌واژه) آن را از یونانی historía می‌دانند که با ریشهٔ عربی «سطر» (نوشتن) هم‌آوا و هم‌معنا شده است؛ اما جفری به پیروی از فرنکل و نولدکه وام‌گیری مستقیم از یونانی را نمی‌پذیرد و آن را از آرامی/سریانی šṭārā «نوشته، سند» از ریشهٔ s-ṭ-r و در نهایت اکدی šaṭāru «نوشتن» می‌داند. پس ادعای نورایی با احتیاط پذیرفتنی است و یادداشت خود او دیدگاه دیگر را درست بازگو کرده است.\",\n \"sources\": [W + \"أسطورة\"],\n \"ref_check\": [\n  rc(\"TAD:3\", \"supports\", \"TAD_pages.txt leaf 7 (≈ p.3): 'اساطير - يوناني [historia] معناه أخبار تاريخية وقد استعملها العرب بمعنى خرافات وحكايات'.\"),\n  rc(\"FVQ:56\", \"contradicts\", \"FVQ_pages.txt leaf 74-75 = pp.56-57 s.v. Asāṭīr: 'Sprenger ... suggested that in asāṭīr we have the Gk. ἱστορία ... accepted by many later scholars. The objections to it raised by Horovitz ... are, however, insuperable ... The derivation from Syr. ... suggested by Nöldeke-Schwally ... is much more satisfactory' — Jeffery prefers the Aramaic s-ṭ-r origin, as the chart's NOTE says.\")\n ],\n \"consulted\": [\n  cs(\"FVQ\", \"pp. 56-57\", \"contradicts\", \"'The verb saṭara ... is a denominative from saṭr, and this itself is a borrowing from Aram. שְׁטָרָא'\"),\n  cs(\"KLN\", \"s.v. history\", \"silent\", \"Klein does not mention the Arabic word.\")\n ]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Persian\",\n \"words\": \"ostůreh; asâtîr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian osṭūreh اسطوره 'myth, fable' and its broken plural asāṭīr اساطیر are borrowed from Arabic usṭūra / asāṭīr (Mo'in [ع.]), with Arabic final -a(t) rendered by Persian -eh; the Mowlavi verse 'که اساطیر است و افسانه نژند' shows the plural in classical use. The Arabic → Persian step is certain whatever the Arabic word's ultimate origin (see #14).\",\n \"derivation_fa\": \"«اسطوره» و جمع مکسر آن «اساطیر» از عربی وارد فارسی شده‌اند (معین: [ع.]) و «ـة» پایانی عربی در فارسی «ـه» شده است؛ بیت مولوی «که اساطیر است و افسانه نژند» کاربرد کهن واژه را نشان می‌دهد. این گام (عربی ← فارسی) قطعی است، هرچند ریشهٔ دورتر واژهٔ عربی محل بحث است.\",\n \"sources\": [W + \"اسطوره\", \"https://vajehyab.com/moein/اسطوره\"],\n \"ref_check\": [\n  rc(\"MON:225\", \"supports\", \"print page not online; the same Mo'in entry on vajehyab: 'اسطوره (اُ طُ رِ) [ع.] (اِ.) 1 - افسانه، قصه. 2 - سخن بیهوده و پریشان. ج. اساطیر'.\")\n ],\n \"consulted\": [\n  cs(\"MON\", \"vajehyab Mo'in s.v. اسطوره\", \"supports\", \"'[ع.] ... ج. اساطیر'\"),\n  cs(\"FVQ\", \"p. 56\", \"partial\", \"Arabic asāṭīr discussed; Persian not mentioned.\"),\n  cs(\"TAD\", \"leaf 7\", \"partial\", \"Arabic word from Greek; no Persian.\")\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"English\",\n \"words\": \"story, history, idea\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English history < Latin historia < Greek historía; story (narrative) is an aphetic Anglo-French estorie < OF estoire < Lat. historia (Skeat: 'Story (1), a narrative; see History'); idea < Latin idea < Greek idéā. Watkins lists HISTORY, (STORY¹) and IDEA under weid-.\",\n \"derivation_fa\": \"انگلیسی history از لاتینی historia و آن از یونانی historía است؛ story (داستان) کوتاه‌شدهٔ فرانسوی-نورمن estorie از همان historia است؛ idea از لاتینی idea و یونانی idéā است. واتکینز هر سه را زیر weid- آورده؛ ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [rc(\"None\", \"not_checked\", \"no reference cited by Nourai for this node.\")],\n \"consulted\": [\n  cs(\"AHD\", AHDQ, \"supports\", \"'*wid-es-yā in Greek idea ...: IDEA ... *wid-tor- in Greek histōr ...: HISTORY, (STORY¹)'\"),\n  cs(\"SKT\", \"SKT.txt line 18638\", \"supports\", \"'Story (1), a narrative; see History'\"),\n  cs(\"KLN\", \"line 114338 s.v. history\", \"supports\", \"'L. historia ... fr. Gk. ἱστορία'\")\n ]\n})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Germanic\",\n \"words\": \"wîtan; wîssaz; wit\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Proto-Germanic *wītaną 'to look after, observe; reproach' (full grade *weid-; OE wītan 'reproach', Goth. fraweitan 'avenge', Frankish *wītan 'show, guide' > OProv. guidar) and *witaną 'to know' (zero grade) / *witją 'wit, knowledge' are correct. *wissaz (< *wid-tó-) means 'known, certain' (OE gewiss) and *wīsaz 'wise' (< *weid-to-), not 'wisdom' as the chart glosses it: wisdom is OE wīs + -dōm. Forms right, one gloss loose.\",\n \"derivation_fa\": \"ژرمنی آغازین *wītaną «مراقبت کردن، نگریستن؛ سرزنش کردن» (از درجهٔ کامل *weid-) و *witaną «دانستن» و *witją «خرد، دانش» (درجهٔ صفر) درست‌اند. اما *wissaz به معنی «دانسته، مسلّم» است و «خردمند» از *wīsaz است، نه «خرد» (wisdom از wīs + -dōm ساخته شده است). پس صورت‌ها درست‌اند و تنها معنای یکی دقیق نیست؛ ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Germanic/wītaną\", W + \"Reconstruction:Proto-Germanic/wissaz\"],\n \"ref_check\": [\n  rc(\"AHD\", \"supports\", AHDQ + \": '1. Germanic *witan, to look after, guard, ascribe to, reproach, in ... b. Old Provençal guida, a guide: GUIDE ... 2. Suffixed form *weid-to- in Germanic *wissaz in: a. Old English wīs, wise: WISE¹; b. Old English wīsdōm ...: WISDOM' — Watkins himself puts *wissaz under 'wise', so the chart's 'wisdom' is a loose rendering.\")\n ],\n \"consulted\": [\n  cs(\"POK\", \"p. 1126\", \"supports\", \"'Old English witan reproach ... Gothic witan look at, observe ... wait, witum know ... Old Icelandic víss, OHG OS OE wīs wise (*u̯eid-s-o-)'\"),\n  cs(\"IEC\", \"IEC.txt line 19845\", \"supports\", \"'Go. witan, wv. look at, see ... OE witan, v. guard, watch'\"),\n  cs(\"WLD\", \"Bd. I p. 237-238\", \"supports\", \"same entry, Germanic forms listed.\")\n ]\n})\n\nnodes.append({\n \"id\": 18, \"lang\": \"English\",\n \"words\": \"wit, wise, wisdom, guide\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"wit < OE witt 'understanding' (PGmc *witją); wise < OE wīs; wisdom < OE wīsdōm (wīs + -dōm); guide < OF guider/guier, from Frankish *wītan 'to show, direct' (OProv. guidar), with Germanic w- rendered gu- in Romance as in guise (Klein, Skeat, Watkins).\",\n \"derivation_fa\": \"wit از انگلیسی کهن witt «فهم»، wise از wīs، wisdom از wīsdōm (wīs + پسوند -dōm) است؛ guide از فرانسوی کهن guider و آن از فرانکی *wītan «نشان دادن، راه نمودن» آمده و w ژرمنی در زبان‌های رومی به gu- بدل شده است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [rc(\"None\", \"not_checked\", \"no reference cited by Nourai for this node.\")],\n \"consulted\": [\n  cs(\"AHD\", AHDQ, \"supports\", \"WIT¹, WISE¹, WISDOM, GUIDE all listed under weid-.\"),\n  cs(\"KLN\", \"KLN_1971.txt line 107138 s.v. guide\", \"supports\", \"'fr. OF. guier ... which derives fr. Frankish *witan, to show (whence also OProvenç. guidar)'\"),\n  cs(\"SKT\", \"SKT.txt line 8115 s.v. Guide\", \"supports\", \"'The gu (for w) shews the word to be of Teut. origin; it must be from a source allied to Goth. witan, to watch, observe, and to A.S. witan, to know'\")\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Weid, Woid, Wid\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *weyd- 'to see' (perfect *wóyd- 'have seen > know'); Pokorny 2. u̯(e)id- 1125-1127; Watkins weid-; LIV *u̯ei̯d-\",\n \"note\": \"Root, label and gloss are correct (Pokorny pp.1125-1127, Walde-Pokorny I 236 ff., Watkins weid-, Mann ueid-, Cheung *u̯aid¹/²). Watkins (AHD) supports nearly every Western branch (Latin, Greek, Welsh gwyn/penguin, Germanic, English). Problems lie in the Iranian half: (1) Avestā (#2) is MP abestāg of unclear origin, not 'knowledge'; hoveydā is hu + peydā for Hübschmann (Mo'in/Bahar: hu + vīdā); (2) pažūhīdan (#4) continues MP wizōy-/wizōstan (*wi-čaud-, Cheung), Horn's *paitiš + vaēd- having been rejected by Hübschmann exactly as the chart's NOTE says; (3) book misprints: Av. 'vîdada' for vīδarə and 'vînosti' for vīnasti; 'hu-vaeda' and 'paitiš-vaēd' are unattested (Horn's starred reconstruction / Nourai's back-formation). Penguin < Welsh pen gwyn is a traditional but uncertain etymology. Arabic usṭūra from Greek historía is one of two current views (the other, Jeffery's Aramaic s-ṭ-r, is recorded in the chart's NOTE). Nourai's POK:1121 for the 'find' forms should be POK:1125. The JSON matches the printed page (site/pages/534.jpg, copy at sources/refs/ocr/BOOK/534.png); no extraction errors.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *weyd- «دیدن» (و از ماضی نقلی آن *wóyd- «دیده‌ام، پس می‌دانم») درست آمده است (پوکورنی ۱۱۲۵–۱۱۲۷، والده-پوکورنی، واتکینز، چونگ). شاخه‌های لاتینی، یونانی، ولزی، ژرمنی و انگلیسی را واتکینز تأیید می‌کند. ایراد در شاخهٔ ایرانی است: «اوستا» از فارسی میانهٔ abestāg با ریشهٔ نامعلوم است و معنی «دانش» ندارد؛ «هویدا» را هوبشمان از hu + «پیدا» می‌داند؛ «پژوهیدن» از فارسی میانهٔ wizōy- است و ریشه‌شناسی هرن را خود هوبشمان رد کرده است. «vîdada» و «vînosti» خطای چاپی کتاب به جای vīδarə و vīnasti‌اند و «hu-vaeda» و «paitiš-vaēd» در اوستا گواهی نشده‌اند. ریشهٔ ولزی «پنگوئن» و یونانی بودن «اسطوره» محتمل ولی قطعی نیست. خطای استخراج دیده نشد.\",\n \"sources\": [PIE],\n \"ref_check\": [\n  rc(\"POK:1125\", \"supports\", POKQ + \" 'Grammatical information: (originally Aorist) ... Perf. u̯oid-a have seen, whence the meaning know'; 'References: WP. I 236 ff.'\")\n ],\n \"consulted\": [\n  cs(\"AHD\", AHDQ, \"supports\", \"'weid-. To see. ... [Pok. 2. u̯(e)id- 1125.]'\"),\n  cs(\"WLD\", \"Bd. I p. 236 (WLD_Bd1_pages.txt leaf 245)\", \"supports\", \"'2. u̯eid- erblicken, sehen, Pf. u̯oida habe gesehen, weiß, woher die Bed. wissen auch auf andere Formen übertragen wurde'\"),\n  cs(\"IEC\", \"IEC.txt line 19845\", \"supports\", \"'ueid- (uid-) see; look; appear; show; watch; know. ... WP I, 237'\"),\n  cs(\"CHEUNG\", \"pp. 408-410\", \"supports\", \"'*u̯aid¹ to know ... PIE (perf. stem) *u̯oid- to know = LIV 686 ff. | Pok.: 1125 ff.'; '*u̯aid² to find'\")\n ],\n \"nodes\": nodes\n}\n\nout = {\"pdf_page\": 534, \"book_page\": 504, \"verified_by\": \"claude-opus-5\", \"verified_on\": \"2026-10-16\", \"entries\": [entry]}\nwith open(\"/home/sfmqrb/git/rishe-private/data/verification/page-534.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\n"
}
```


### [2026-10-16T05:19:44.778Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-534.py (file state is current in your context — no need to Read it back)
```


## [2026-10-16T05:19:51.283Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; sed -i 's/\"p. 93 (PHD_mackenzie.txt line 5503)\"/\"PHD_mackenzie.txt line 5503 s.v. wizōstan\"/; s/\"col. 1313 (BRT.txt line 24926)\"/\"BRT.txt line 24926 (s.v. vaēd- finden)\"/; s/\"p. 40 s.v. \\*čaud (CHEUNG.txt line 3570-3576)\"/\"s.v. *čaud (CHEUNG.txt line 3570-3576)\"/; s/\"Bd. I p. 238\", \"supports\", \"same u̯eid- entry/\"Bd. I p. 236 ff.\", \"supports\", \"same u̯eid- entry/; s/\"Bd. I p. 237-238\", \"supports\", \"same entry, Germanic/\"Bd. I p. 236 ff.\", \"supports\", \"same entry, Germanic/' build-534.py && python3 build-534.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-534.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 534"
}
```


### [2026-10-16T05:19:51.894Z] TOOL RESULT

```
nodes verified: 18/18
node verdicts: {'transcription_suspect': 2, 'disputed': 2, 'confirmed': 10, 'plausible': 4}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'partial': 2, 'not_checked': 10, 'not_found': 1, 'contradicts': 1}
books consulted: {'supports': 35, 'silent': 7, 'contradicts': 6, 'partial': 7} | by book: {'KLN': 9, 'MON': 6, 'WLD': 5, 'AHD': 5, 'IEC': 4, 'SKT': 4, 'CHEUNG': 3, 'HUB': 3, 'POK': 3, 'AMD': 3, 'BRT': 2, 'PHD': 2, 'HRN': 2, 'FVQ': 2, 'NYB': 1, 'TAD': 1}
```


## [2026-10-16T05:20:00.663Z] TOOL CALL #41: SubagentHandback

```json
{
 "message": "Page 534 (book page 504) is verified and written to /home/sfmqrb/git/rishe-private/data/verification/page-534.json. `verify_check.py 534` shows 0 PROBLEM lines and 18 of 18 nodes covered.\n\nVerdicts: root Weid/Woid/Wid is confirmed (PIE *weyd- 'see', Pokorny 1125-1127). Nodes: 10 confirmed, 4 plausible, 2 disputed, 2 transcription_suspect.\n\n**Disputed:**\n- #2 Persian vīdā / Avestâ / hovaydâ:\n  - **Avestâ:** it comes from Middle Persian abestāg, whose origin is unclear. The 'knowledge' gloss is folk etymology.\n  - **hovaydâ:** Hübschmann (§66) derives it from hu + paidā (peydā). Mo'in/Bahar instead give hu + vīdā.\n  - **vīdā:** Borhan pp. 2297-98 gives both 'lost' and 'apparent'.\n- #4 pažūhīdan: it comes from Middle Persian wizōy-/wizōstan (MacKenzie; Cheung puts it under *wi-čaud-). Horn's *paitiš + vaēd- was rejected by Hübschmann (\"vollkommen verfehlt\"), so the chart's own NOTE is right.\n\n**Transcription_suspect (both misprints in the book, not the extraction):**\n- #1 Avestan: the book prints \"vîdada\" where Pokorny and Walde-Pokorny have vīδarə. \"hu-vaeda\" is not attested in Avestan; it is a back-formation from hoveydā.\n- #3 Avestan: the book prints \"vînosti\" for vīnasti. \"paitiš-vaĕd\" is Horn's own starred reconstruction, not an attested form.\n\n**Plausible:**\n- #10 and #11 (penguin): the Welsh pen gwyn origin is traditional but uncertain.\n- #14 Arabic usṭūra: the Greek historía origin is contested by Jeffery, who prefers Aramaic s-ṭ-r; the chart's NOTE records this.\n- #17 Germanic: *wissaz is glossed 'wisdom' but means 'known/certain'.\n\n**Extraction errors:** none. The JSON matches the printed page; a copy of the page image is at data/verification/sources/refs/ocr/BOOK/534.png.\n\n**Other:**\n- Nourai's POK:1121 for the 'find' forms should be POK:1125.\n- I saved a reading of the Borhan page 2297 image to data/verification/sources/refs/ocr/BQT/2297.vision.txt."
}
```


### [2026-10-16T05:20:00.935Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
