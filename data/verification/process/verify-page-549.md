# Verification process log — verify-page-549


## [2026-10-17T00:00:15.536Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 549 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-549.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-549.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-549.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 549` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.606Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.387Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.479Z] TOOL RESULT

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
230	In the shell, `ls` is aliased to `eza`, which can hang without a terminal and leave your
231	command stuck. List files with `command ls` or `find` instead.
232	
233	```json
234	{
235	  "pdf_page": 126,
236	  "book_page": 96,
237	  "verified_by": "claude-opus-5",
238	  "verified_on": "2026-09-05",
239	  "entries": [
240	    {
241	      "entry": 0,
242	      "root": "Dheigh, Dhigha",
243	      "verdict": "confirmed",
244	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
245	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
246	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
247	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
248	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
249	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
250	      "nodes": [
251	        {
252	          "id": 6,
253	          "lang": "Avestan",
254	          "words": "pairi-daeza",
255	          "verdict": "confirmed",
256	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
257	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
258	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
259	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
260	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
261	        }
262	      ]
263	    }
264	  ]
265	}
266	```
267	
268	Rules:
269	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
270	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
271	- `words` = the transliterations of the node joined by "; " (copy from the chart).
272	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
273	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
274	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
275	- If a node lists several words, cover each word; if they differ in verdict, use the worst
276	  verdict for the node and explain per word in `derivation`.
277	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
278	  scholarship takes.
279	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
280	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
281	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
282	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
283	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
284	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
285	  any extraction errors (JSON differs from the printed page) the owner must fix.
286	  Do not paste the JSON back into your reply.
287	
```


## [2026-10-17T00:00:18.889Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-549.txt"
}
```


### [2026-10-17T00:00:18.979Z] TOOL RESULT

```
1	=== PDF page 549 (book page 519) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Werg 1 : to work  (refs POK:1168)
4	#1 (parent #0) [Avestan] refs=POK:1168; KLN:1751; SYN:537 | vareza : work
5	  #2 (parent #1) [Persian] refs=BQT:254,2268; MON:5002 | varzîdan «ورزیدن ( ورزه، ورزنده ، ورزیده)» : to work ; barz, varz «بَرز ، ورز» : work, farming ; barz-gar «برزگر ( ورزگر ، ورزکار)» : farmer ; varzâv «ورزاو (ورزا ، ورزو )» : strong cow ; varzeš 1 «ورزش» : activity, farming, occupation, sports
6	#3 (parent #0) [Old Persian] refs=KNT:207 | vard : work
7	#4 (parent #0) [Greek] refs=AHD | organon : tool
8	  #5 (parent #4) [Arabic] refs=MON:203 | 
9	    #6 (parent #5) [Persian] refs=BQT:106; MON:203 | arghanŭn «ارغنون»
10	  #7 (parent #4) [French] refs=AHD:296 | 
11	    #8 (parent #7) [Persian] refs=MON:205 | org «اُرگ» : organ
12	    #9 (parent #7) [English] refs=AHD:926 | organ, organon
13	#10 (parent #0) [Middle German] refs=KLN:209; AHD:155 | bolwerk : fortification work
14	  #11 (parent #10) [French] refs=None | 
15	    #12 (parent #11) [Persian] refs=MON | bolvâr «بلوار ( بولوار )»
16	    #13 (parent #11) [English] refs=AHD:155 | boulevard
17	#14 (parent #0) [Germanic] refs=AHD | werkam : work
18	  #15 (parent #14) [English] refs=None | work
19	#16 (parent #0) [Greek] refs=AHD | ergon : work
20	  #17 (parent #16) [French] refs=None | 
21	    #18 (parent #17) [Persian] refs=MON |  | extra: انرژی ، متالورژی ، آلرژی
22	    #19 (parent #17) [English] refs=None | argon, energy, allergy, metallurgy, surgery, George
23	--- entry 1 ---
24	ROOT Werg 2 -> redirect to Wer 3
25	--- entry 2 ---
26	ROOT Werg 3 -> redirect to Wer 2
27	--- entry 3 ---
28	ROOT Wermi -> redirect to Wer 2
29	--- entry 4 ---
30	ROOT Werp -> redirect to Wer 2
31	--- entry 5 ---
32	ROOT Wert -> redirect to Wer 2
33	
```


## [2026-10-17T00:00:19.367Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-549.json"
}
```


### [2026-10-17T00:00:19.615Z] TOOL RESULT

```
1	{
2	  "pdf_page": 549,
3	  "book_page": 519,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Werg 1",
8	        "lang": "Indo-European",
9	        "refs": "POK:1168",
10	        "gloss": "to work"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1168; KLN:1751; SYN:537",
18	          "words": [
19	            {"translit": "vareza", "gloss": "work", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Persian",
28	          "refs": "BQT:254,2268; MON:5002",
29	          "words": [
30	            {"translit": "varzîdan", "gloss": "to work", "script": "ورزیدن ( ورزه، ورزنده ، ورزیده)"},
31	            {"translit": "barz, varz", "gloss": "work, farming", "script": "بَرز ، ورز"},
32	            {"translit": "barz-gar", "gloss": "farmer", "script": "برزگر ( ورزگر ، ورزکار)"},
33	            {"translit": "varzâv", "gloss": "strong cow", "script": "ورزاو (ورزا ، ورزو )"},
34	            {"translit": "varzeš 1", "gloss": "activity, farming, occupation, sports", "script": "ورزش"}
35	          ],
36	          "note": null,
37	          "quote": {
38	            "text": "شما دیر مانید و خُرّم بزید - به رامش سوی ورزش خود شوید",
39	            "poet": "Ferdowsî"
40	          }
41	        },
42	        {
43	          "id": 3,
44	          "parent": 0,
45	          "lang": "Old Persian",
46	          "refs": "KNT:207",
47	          "words": [
48	            {"translit": "vard", "gloss": "work", "script": null}
49	          ],
50	          "note": null,
51	          "quote": null
52	        },
53	        {
54	          "id": 4,
55	          "parent": 0,
56	          "lang": "Greek",
57	          "refs": "AHD",
58	          "words": [
59	            {"translit": "organon", "gloss": "tool", "script": null}
60	          ],
61	          "note": null,
62	          "quote": null
63	        },
64	        {
65	          "id": 5,
66	          "parent": 4,
67	          "lang": "Arabic",
68	          "refs": "MON:203",
69	          "words": [],
70	          "note": null,
71	          "quote": null
72	        },
73	        {
74	          "id": 6,
75	          "parent": 5,
76	          "lang": "Persian",
77	          "refs": "BQT:106; MON:203",
78	          "words": [
79	            {"translit": "arghanŭn", "gloss": null, "script": "ارغنون"}
80	          ],
81	          "note": null,
82	          "quote": null
83	        },
84	        {
85	          "id": 7,
86	          "parent": 4,
87	          "lang": "French",
88	          "refs": "AHD:296",
89	          "words": [],
90	          "note": null,
91	          "quote": null
92	        },
93	        {
94	          "id": 8,
95	          "parent": 7,
96	          "lang": "Persian",
97	          "refs": "MON:205",
98	          "words": [
99	            {"translit": "org", "gloss": "organ", "script": "اُرگ"}
100	          ],
101	          "note": null,
102	          "quote": null
103	        },
104	        {
105	          "id": 9,
106	          "parent": 7,
107	          "lang": "English",
108	          "refs": "AHD:926",
109	          "words": [
110	            {"translit": "organ, organon", "gloss": null, "script": null}
111	          ],
112	          "note": null,
113	          "quote": null
114	        },
115	        {
116	          "id": 10,
117	          "parent": 0,
118	          "lang": "Middle German",
119	          "refs": "KLN:209; AHD:155",
120	          "words": [
121	            {"translit": "bolwerk", "gloss": "fortification work", "script": null}
122	          ],
123	          "note": null,
124	          "quote": null
125	        },
126	        {
127	          "id": 11,
128	          "parent": 10,
129	          "lang": "French",
130	          "refs": null,
131	          "words": [],
132	          "note": null,
133	          "quote": null
134	        },
135	        {
136	          "id": 12,
137	          "parent": 11,
138	          "lang": "Persian",
139	          "refs": "MON",
140	          "words": [
141	            {"translit": "bolvâr", "gloss": null, "script": "بلوار ( بولوار )"}
142	          ],
143	          "note": null,
144	          "quote": null
145	        },
146	        {
147	          "id": 13,
148	          "parent": 11,
149	          "lang": "English",
150	          "refs": "AHD:155",
151	          "words": [
152	            {"translit": "boulevard", "gloss": null, "script": null}
153	          ],
154	          "note": null,
155	          "quote": null
156	        },
157	        {
158	          "id": 14,
159	          "parent": 0,
160	          "lang": "Germanic",
161	          "refs": "AHD",
162	          "words": [
163	            {"translit": "werkam", "gloss": "work", "script": null}
164	          ],
165	          "note": null,
166	          "quote": null
167	        },
168	        {
169	          "id": 15,
170	          "parent": 14,
171	          "lang": "English",
172	          "refs": null,
173	          "words": [
174	            {"translit": "work", "gloss": null, "script": null}
175	          ],
176	          "note": null,
177	          "quote": null
178	        },
179	        {
180	          "id": 16,
181	          "parent": 0,
182	          "lang": "Greek",
183	          "refs": "AHD",
184	          "words": [
185	            {"translit": "ergon", "gloss": "work", "script": null}
186	          ],
187	          "note": null,
188	          "quote": null
189	        },
190	        {
191	          "id": 17,
192	          "parent": 16,
193	          "lang": "French",
194	          "refs": null,
195	          "words": [],
196	          "note": null,
197	          "quote": null
198	        },
199	        {
200	          "id": 18,
201	          "parent": 17,
202	          "lang": "Persian",
203	          "refs": "MON",
204	          "words": [],
205	          "script_extra": "انرژی ، متالورژی ، آلرژی",
206	          "note": null,
207	          "quote": null
208	        },
209	        {
210	          "id": 19,
211	          "parent": 17,
212	          "lang": "English",
213	          "refs": null,
214	          "words": [
215	            {"translit": "argon, energy, allergy, metallurgy, surgery, George", "gloss": null, "script": null}
216	          ],
217	          "note": null,
218	          "quote": null
219	        }
220	      ]
221	    },
222	    {
223	      "root": {"name": "Werg 2", "redirect": "Wer 3"},
224	      "nodes": []
225	    },
226	    {
227	      "root": {"name": "Werg 3", "redirect": "Wer 2"},
228	      "nodes": []
229	    },
230	    {
231	      "root": {"name": "Wermi", "redirect": "Wer 2"},
232	      "nodes": []
233	    },
234	    {
235	      "root": {"name": "Werp", "redirect": "Wer 2"},
236	      "nodes": []
237	    },
238	    {
239	      "root": {"name": "Wert", "redirect": "Wer 2"},
240	      "nodes": []
241	    }
242	  ]
243	}
244	
```


## [2026-10-17T00:00:26.651Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; command ls sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','BQT','MON','KNT','AHD','WLD','IEC','BRT','HRN','HUB','CHEUNG','ARY','SKT','FSD','WEB','PHD','NYB','LKT']:\n  v=d.get(k);print(k, v and {x:v.get(x) for x in ['local_file','page_offset','lookup_hint']})\""
}
```


### [2026-10-17T00:00:27.067Z] TOOL RESULT

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
KNT_full.txt
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
SKT_dli_revised.txt
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
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
KLN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
SYN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
BQT {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
KNT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt', 'page_offset': 'leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations."}
AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
WLD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
IEC {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
BRT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
HRN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
HUB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
CHEUNG None
ARY {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
SKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
FSD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt', 'page_offset': 'vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file."}
WEB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt', 'page_offset': 'not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': 'Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.'}
PHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
NYB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
LKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt', 'page_offset': 'leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."}
```


## [2026-10-17T00:00:32.957Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls data/verification/ | tail -5; sed -n 1,200p tools/verify_check.py | head -150"
}
```


### [2026-10-17T00:00:33.247Z] TOOL RESULT

```
page-97.json
page-98.json
page-99.json
process
sources
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


## [2026-10-17T00:00:37.221Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"lemma: werĝ\\|lemma: uerĝ\\|lemma: u̯erĝ\" POK_full.txt; grep -n -A25 \"lemma: u̯erĝ-\" POK_full.txt | head -60"
}
```


### [2026-10-17T00:00:37.640Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:00:40.241Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Page(s): 1168\" POK_full.txt; grep -n \"ergon\\|ἔργον\" POK_full.txt | head"
}
```


### [2026-10-17T00:00:40.606Z] TOOL RESULT

```
91215:Page(s): 1168-1169 
13406:Maybe alb. {**fergd) fergonj^ bake' \ also truncated alb. {*fertalis) /7/" sacrifice'. 
20649:'long'; also alb. {*dordga) dergonj^ send in a trip'.
```


## [2026-10-17T00:00:42.501Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91200,91260p POK_full.txt"
}
```


### [2026-10-17T00:00:42.871Z] TOOL RESULT

```
act, action', Gothic frawaurhts^ sinful ', f. " sin ' etc., Gothic waurstwr\. "work' {*waurh- 
stwa-\ similarly Avestan varstva-); Old High German were, werah. Old Saxon werk. Old 
Icelandic werkr\. (= spyov) "work, occupation, job'. Old English weorca\so " hardship, 
agony', wherefore also Old Icelandic verkr. Gen. verkjar{rw. /-stem) "pain, affliction' could 
belong here; 

Old High German liv/^e/? nanena^iicKena^eDen^en^mger^ = Old Saxon wirkian. 
Old English wircan, and das therefrom not trennbare Old High German werifi\r\ the 
meaning " coarse flax, tow, oakum ', awirihhi, awuritihi^ oakum ' show use our root auf die 
Weberei; s. against it Marstrander IF. 22, 332 f. (the l/Verg ar\d wirken^to weave' the root 
*uerg-'turr\, coil ' allot mochte); an Modern High German IVerg rerr\\r\6s cymr. cy-warc/i' 
hemp, flax' = bret. koarc'fi, abret. coarcholion <^\. " canabina '; Marstrander ZcP. 7, 362 
seeks therein ein Indo Germanic *uer-k- "turn', see above S. 11 55. 

References: WP. I 290 f.. Frisk 548 f. 
Page(s): 1168-1169 



Root / lemma: ueiy-3, uorg- {*hueiy-3) 

Meaning: to abound, to be full of strength 

Material: Old Indie urj-, urjai., urja- m. "juice, sap and power, nourishment, food' {*Uorg-l), 

urjayati' nourishes, strengthens', urjasvant-^ plentiful '; 

gr. opYH "seelischer, heftiger shoot, Affekt, rage, fury' (opyi^u) 'erzijrne jemanden' ), 
opYQU) "from dampness and juice, sap strotzen, violent lust, crave, in leidenschaftlicher 
Stimmung sein', opya^, -a5oc; (vn) "iJppigerfruchtbarer Erdboden, Marschland, Au'; 

e-grade Old Irish fere. Middle Irish fergi. "rage, fury' presumably also the (oKzavoo, 
Ou£pyiouiO(; by Ptol. (i.e. i/e/y/V/bs "the angry'? or still "the schwellende, surging '?); 
mcymr. y wer/t^ sea' (that is to say y werydd) rather from *UerJo- to *auer- above S. 80 and 
1165; compare Pedersen Celtic Gr. II, 669 f. 

References: WP. I 289, Mayrhofer 1,116. 
Page(s): 1 1 69 

Root /lemma: uer-10{*huer-10) 

Meaning: " river, flow ' 

See also: see above ayer-S. 80 f.; in addition Var-'m many FIN {Uer-). 

Page(s):1165 

Root /lemma: uer-11, uer9-{*huer-11) 

Meaning: friendship; trustworthy, true 

Material: A. root nouns uer- gr. Frip- in hom. (sni) npa cpspsiv "einen Gefallen tun', Pherek. 

npa igGi, Bacchyl. qpa with Gen. "xapiv'; £nir|pavo(; "wohlgefallig, pleasant'; Nom. PI. spi- 

npsc; " confidante ', Sg. ostem spiripoc; "traut, dear'; ppiripov fjEyaAwc; KSxapiajJEvov Hes.; 

PN Dspiriprif;, Aiu)pr|<;from Aio-Fripr|<;. 

B. derivative uera. Germanic Vera "pact, covenant, profession, declaration, covenant' 
in Old Icelandic GN l/a/'"goddess of oath of allegiance ', PI. i/a/'a/'"Treuegelubde', Old
```


## [2026-10-17T00:00:44.889Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91170,91200p POK_full.txt"
}
```


### [2026-10-17T00:00:45.280Z] TOOL RESULT

```
participle varsta-, varaza-m. " work, Verrichten from, occupation ' (npers. varz, barz 
"Feldarbeit, Ackerbau'), varsti-i. "Handein, Tun', varstva- M]. 'was to tun is'; Armenian 
gorc^work' (with secondary o); gr. spyov, Fspyov ' work' (= German Work ' work '), 
epya^OMQi 'arbeite', thereafter £pyaTr|<; 'worker' (for *£py6Tr|<;), spSu) (occasionally £p5(jo) 
"do, sacrifice ' (*F£pz5u), "i/e/g/o lengthened grade after Fspyov as in Old Saxon wirkian). 



Fut. sp^oj, Aor. sp^a, Perf. sopya), ps^w "do' (from ps^ai neologism, hom. apsKToq 
"ungetan' reconverted with metathesis from *a[F]£pKTO(;); opyavov "tool', opyia "(secret) 
worship', opYia^u) "feiere Mysterien', opyscbv "Mitglied a religiosen BriJderschaft'; opva^u), 
Ionian opvau), opyiCu) "knead, ruhre through, tan, convert hide into leather' (as Modern 
High German Teig wirken\N\Vr\ meaning- contraction in the professional jargon), wherefore 
EopYH " verticil, whorl, group of parts (leaves, flowers, etc.) arranged in a circle ' (probably 
redupl. Fs-Fopya); 

Zero grade alb. {*ureg-) rregj"c\ear\\ Mediopassiv rregjem^ trouble about, strain, strive' 
(stem E. Mann Lg. 26, 382 f.); (common Slavic Baltic Albanian Greek ure-> rre-see pE^co 
"do'). 

abret. guerg^ effective] capable of filling some function; (person/medicine); legally valid ', 
gall, vergo-bretus^ uppermost authority of Aeduer', also i/e/rc-it'/'e/o (Pokorny, Vox 
Romanica 10, 266 f.); mcymr. gwre/fhleat, dead, act' {*ureg-tu-), 1. PI. Imper. acymr. 
guragun, newer gwnawn etc. (/? instead of /"through influence of *gn/'- ' make' , S. 373), 
corn, gruen, mbr. gr-{u)eomp {* ureg- "make'), Lewis-Pedersen S. 336 f.; 

Old Saxon wirkian (neologism after werR), warhta. Old High German (Franconian) 
wirkan, wirchen, war{a)hta^ work, be active, work '; Gothic waurkjan{= Avestan varazyeitl). 
Old Icelandic yrkja, orta. Old English wyrcan, worhte. Old High German (Upper German) 
wurchen, wor{a)hta^ work, do, make, effectuate ', Old High German gawurhti. "feat, dead, 
act, action', Gothic frawaurhts^ sinful ', f. " sin ' etc., Gothic waurstwr\. "work' {*waurh-
```


## [2026-10-17T00:00:51.030Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^werg-\\|^wer-g\\|werg-\\b\" AHD_watkins1985.txt | head; grep -n -i \"^vard\\|vard-\\|^varz\\|vrz-\\|v.rd-\" KNT_full.txt | head -30"
}
```


## [2026-10-17T00:00:52.206Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^organ\\|^boulevard\\|^bulwark\\|^work,\\|^energy\\|^ergo-\\|^argon\\|^allergy\\|^metallurgy\\|^surgery\\|^George\" KLN_1966.txt | head -40"
}
```


### [2026-10-17T00:00:52.673Z] TOOL RESULT

```
1151:*op-wer-yo- (*op-, over; see epi) in Latin operire, to cover: COVER, OPERCULUM. II. O-grade form *wor-. 1. Germanic *war-nén in Old English war(e)nian, to take heed: WARN. 2. Germanic *war- in: a. (i) Old French garant, warrant, authorization: GUARANTY (ii) Old North French warant, warrant, and warantir, to guarantee: WARRANT, (WARRANTEE), WARRANTY; b. Old French garer, to guard, protect: GARAGE; c. Old French g(u)arir, to defend, protect: GARRET, GARRISON; d. Old North French warenne, enclosure, game preserve: WARREN; e. Old French g(ujarnir, to equip: GARMENT, GARNISH. [Pok. 5. uer- 1160.] wer-S, Also wera-. To speak. Variant *wré-, contracted from *wreo-. 1. Suffixed zero-grade form *wr-dho- in Germanic *wurdam in Old English word, word: worD. 2. Suffixed form *wer-dho- in Latin verbum, word: VERB, VERVE; ADVERB, PROVERB. 3. Suffixed form *wer-yo- in Greek eirein, to say, speak: IRONY. 4. Variant form *wré- in suffixed form *wré-tor- in Greek rhétér, public speaker: RHETOR. [Pok. 6. wer- 1162.] wer-7. To burn. Suffixed lengthened o-grade (causative) form *w6r-yo- in Russian varit’, to boil: saMovarR. [Pok. 12. wer- 1166.] wer-®, Squirrel. Reduplicated expressive form *wi-wer(r)- in Latin viverra, a ferret: VIVERRINE. [Pok. 13. uer- 1166.] wér-. Water. Suffixed zero-grade form *dr-ind- in Latin irina, urine: URINE. [In Pok. 9. au(e)- 78.] were-', Wide, broad. Suffixed form *wer(a)-u- metathe- sized in Greek eurus, wide: EURY-; ANEURYSM, EURYD- IcE. [Pok. 8. wer- 1165.] were-2, To find. Variant *wré-, contracted from *wrea-. Reduplicated form *we-wré- in Greek heuriskein (first person singular perfect indicative active heuréka), to find: EUREKA, HEURISTIC. [Pok. 4. ver- 1160.] werg-. To do. I. Suffixed form *werg-o-. 1. Germanic *werkam, work, in: a. Old English weorc, werc, work: work; b. Old High German werc, work: (BOULEVARD),
2869:vardanam = opj-, GAV. vorozóna, LAV. varozüna-, 
2884:fravartikdn), Margu&, Marduniya, -vard- in Ar- 
7818:iya- to hat- (8240), ha-mic-iya- to mitra-; Artavard- 
7884:varda-na-. 
22695:vardiya, a Persian officer, against Vahyazdata, 
23870:ta-mar-2i-ja. From arta- + vard- ‘to work’ + adj. 
23872:tice’ (not from vard- ‘to increase’, Skt. vardh-, be- 
28834:vard- vb. ‘work’: Av. varaz-, Gk. рёрүө ‘work’, 
28838:vardana- sb. ‘town’: Av. vorozona-, LAV. 
28843:vardanam nsn. DB 1.92; 2.9°, 22, 66, 95f; 3.5, 22,
```


### [2026-10-17T00:00:52.718Z] TOOL RESULT

```
740:metallurgy
1026:surgery
2264:allergy,  n.,  hypersensitiveness  of  body  cells  to certain  substances  ( immunology ).  —  ModL.  al¬ lergia,  coined  about  1905  by  Clemens  von  Pir- quet,  an  Austrian  pediatrist  (1874-1910),  fr.  Gk. ciXXoc,  ‘another’  and  Ipyov,  ‘work’.  See  alio-  and ergon  and  cp.  energy.
3404:argon,  n.,  an  inert  chemical  element.  —  ModL., fr.  Gk.  dpyov,  neut  of  xpyoc,  ‘idle,  inert’,  con¬ traction  of  dspydt;,  lit.  ‘not  active’,  fr.  dc-  (see priv.  pref.  a-),  and  £pyov,  ‘work’.  See  ergon and  cp.  the  second  element  in  lethargy.  This  ele¬ ment,  discovered  by  the  British  chemists  Sir William  Ramsay  (1852-1916)  and  Morris  Wil¬ liam  Travers  (1872-1961)  in  1894,  was  so  called by  them  because  it  does  not  readily  unite  with other  elements.
3406:argonaut,  n.,  the  paper  nautilus  (zoo!)  —  Fr. prec.  word.
16039:George,  masc.  PN.  —  F.  George(s),  fr.  Late  L. Georgius,  fr.  Gk.  yetopyoq,  ‘husbandman’,  which is  compounded  of  y?),  ‘earth’,  and  the  base  of cpYov,  ‘work’.  See  geo-  and  ergon  and  cp. georgic.
17017:George  de  Hevesy  (1885-  )  in  1923  fr.  Haf-
23674:metallurgy,  n.  —  ModL.  metallurgia ,  fr.  Gk. pexaXXoupY<i<;i  ‘worker  in  metal  ,  which  is compounded  of  p.£xaXXov,  ‘metal  ,  and  £pyov, ‘work’.  See  metal  and  ergon.
26475:organization
26534:organdie,  organdy,  n.,  a  fine  transparent  muslin.
26536:organic,  adj.  —  L.  organicus,  fr.  Gk.  opyavtxoc, ‘serving  as  an  organ  or  instrument’,  fr.  opyotvov. See  organ  and  adj.  suff.  -ic  and  cp.  homorganic. Derivative:  organic-al-ly,  adv. organism,  n.  —  Formed  fr.  organ  with  suff. -ism.
26537:organist,  n.  —  MF.  (--  F.)  organiste,  fr.  ML. organista,  ‘one  who  plays  on  an  organ’,  fr.  L. organum,  in  the  sense  of  ‘musical  instrument’. See  organ  and  -ist.
26538:organization,  n.  —  ME.  organizacion,  fr.  MF. (=  F.)  organisation,  fr.  ML.  organizdtidnem.
26539:organize
26543:organography,  n.,  description  of  the  organs  of animals  or  plants.  —  Compounded  of  organo- and  Gk.  -ypacpta,  fr.  ypaipeiv,  ‘to  write’.  See -graphy.
26545:organon,  n.,  a  system  of  philosophic  investiga¬ tion  —  Gk.  opyavov,  ‘instrument,  organ’  (often used  as  the  title  of  works  on  logic).  See  organ, organotherapy,  n.,  treatment  of  diseases  with  ex¬ tracts  from  animal  organs.  —  Compounded  of organo-  and  Gk.  &epa7rsia,  ‘a  waiting  on,  serv¬ ice,  attendance’.  See  -therapy, organum,  n.,  an  organon.  —  L.,  ‘instrument, organ',  fr.  Gk.  opyavov.  See  organon, organzine,  n.,  a  fine  kind  of  silk  made  of  several threads  twisted  together.  —  F.  organsin,  fr.  It. organzino,  fr.  Urgendj,  a  town  in  Russian Turkestan.
```


## [2026-10-17T00:00:57.841Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28825,28842p KNT_full.txt; awk 'BEGIN{RS=\"\\f\"} /vard- vb/ {print NR-1; exit}' KNT_full.txt; sed -n 1151p AHD_watkins1985.txt | grep -o \"werg-\\. To do.\\{0,1500\\}\""
}
```


### [2026-10-17T00:00:58.188Z] TOOL RESULT

```
. $233.II; JAOS 62.275, 63.67-8) DB 444 (Camer- 
on’s reading; not upa- + à + varl-, \updvalriary 
with dittography in -"tysiy*, as proposed by Tm. 
Vat. Stud. 1.30-1, Lex. 122; for other restorations, 
see Gray JAOS 23.60-2, Bthl. WZKM 22.69, Wb. 
ZDMG 61.728, HK Phil. Nov. 3.103, ApKT 1.61, 
2.28). 


vard- vb. ‘work’: Av. varaz-, Gk. рёрүө ‘work’, 
Gm. Werk, pIE *yerg-; in Artavardiya-. 


vardana- sb. ‘town’: Av. vorozona-, LAV. 
varazdna- ‘community’, Skt. wpjdna- ‘enclosed 
space’, pIE *urgeno- (830, 5147.1), to root *uerĝ-, 
Skt. yrj-, Gk. &pyo “Т enclose’ (discussion of etymol- 
ogy, with variant view, see Hall, Те. 12.297-9). 
0
werg-. To do. I. Suffixed form *werg-o-. 1. Germanic *werkam, work, in: a. Old English weorc, werc, work: work; b. Old High German werc, work: (BOULEVARD),
```


## [2026-10-17T00:01:00.959Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \"werg-\\. To do\\..\\{0,2000\\}\" AHD_watkins1985.txt | head -c 2500; echo; grep -n -B3 \"vard- vb\" KNT_full.txt | head; grep -n \"^ *20[6-8] *$\" KNT_full.txt | head"
}
```


### [2026-10-17T00:01:01.453Z] TOOL RESULT

```
1151:werg-. To do. I. Suffixed form *werg-o-. 1. Germanic *werkam, work, in: a. Old English weorc, werc, work: work; b. Old High German werc, work: (BOULEVARD),

28831-2.28). 
28832-
28833-
28834:vard- vb. ‘work’: Av. varaz-, Gk. рёрүө ‘work’, 
28664:206 
28872:207 
28937:208
```


## [2026-10-17T00:01:05.560Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28660,28668p KNT_full.txt; sed -n 28868,28876p KNT_full.txt; sed -n 1152,1153p AHD_watkins1985.txt | cut -c1-1800"
}
```


### [2026-10-17T00:01:05.855Z] TOOL RESULT

```
gen., “оп account of’; 10е, sgoof räd- (5188111), 
io root in Ski. radh- ‘effect; complete! (not to 


206 


"rad-, pIE *rej-, with Hz. ApI 280). DB 4.54; 
DNb 9, 10f; also in avahyarádiy, q.v. 
AsH 10; DB 1.11, 18f, 18, 22, 26, 59f, 68, 70, 88, 
94°; 2.3°, 25, 35, 40, 45, 54, 60, 68, 86, 97; 3.6, 


207 


17, 371, 45, 62, 67, 87; 4.4, 6, 41, 46, 52, 60, 88; 
5.16, 32; DPd 4, 9; DPe 6; DNa 16, 35, 49; DNb 
’ BULWARK. 2. Greek ergon, work, action: ERG, -URGY;
ADRENERGIC, ALLERGY, ARGON, CHOLINERGIC, DEMI- URGE, DRAMATURGE, ENDERGONIC, ENDOERGIC, EN- ERGY, ERGOGRAPH, EXERGONIC, EXERGUE, EXOERGIC, GEORGIC, LITURGY, METALLURGY, SURGERY, (SYNERGID), SYNERGISM, THAUMATURGE. II. Zero-grade form *wrg-. 1. Suffixed forms *wrg-yo-, *wrg-to- in Germanic *wurk- Jan, to work, participle *wurhta-, in Old English wyrcan, to work, participle geworht, wrought: WROUGHT. 2. Suf- fixed form *wrg-t- in Germanic *wurhtj6- in Old English wryhta, maker, wright: WRIGHT. III. O-grade form *worg- in: a. Greek organon (with suffix -ano-), tool: ORGAN, ORGANON; b. Greek orgia, secret rites, worship (< “service”): ORGY. [Pok. 2. werg- 1168.]
```


## [2026-10-17T00:01:14.445Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"varəza\\|var@za\\|varaza-\\|varoza\" BRT.txt | head -20; grep -n \"Werk\\b\\|wirken\" BRT.txt | head -20"
}
```


### [2026-10-17T00:01:14.862Z] TOOL RESULT

```
8677:•  j.  uz-varaza-  n.  'Wicdei|;utmachen' (einer  üblen  durch  eine  gute  Tat):  äs aiühe  asti  °x?m  "wie  kann  man  das  wieder gut  machen?"  V.iS.  36;  37,  S7- ab  Inf,  sbc5.
10181:•  j.  gavästrya-varaza-  n.  'Verrichten landwirtschaftlicher  Arbeit*:  'sa  F.  21.
28507:•  j.  äyaoSnä-varaza-  m.  'der  die  Tat begeht,  Täter' :  yai  tat  paiti  irisytiti  aii»kal hata  'za  a^a  bavainti  p>sS.tanvS  "wenn  .., so   werden    dadurch  die  Täter  zu  PP  V.
4235:•  j.  an-aeäam  Absol.''  'ohne  danach  zu suchen,  zu  streben,  ohne  etwas  dafür,  dazu zu  tun':  ita  tanam  iristahe  avaMsia  an' manS  an'  vacö  an'  ryad^nfm  "ich  bin  da auf  einen  Leichnam  gestossen,  ohne  dass ich  etwas  dazu  getan  hätte  in  Gedanken, Wort  und  Werk"  V.Äioo.
7607:•  j.  a-varazika-"  Adj.  (fem.  °zikii-)  'nicht wirkend,  faul':  druxi  ojfä^re  'ke  (VSf.) ' V.  /*.3o.  I
7609:•  j,  »-var«zyant-  Adj.  i)  mit  Akk,  'nicht wirkend,  begehend':  'zinbyd^"^  pascaila araiwya  syaoina  V.J.  40.  2)  ohne Obj.  'sich  nicht  übend  (tn  den  Werken der  Religion)';  yö  saite  haurvqm  tarasca xsapamm  ayazsmns  . .  'zyö  ".  ,  ohne  zu beten  . .  ohne  sich  (im  Guten)  zu  üben" V./&S-
8143:—  tiiig  zbayS  (sd.)  varthiul  "däii  manatshö Y.  ^f7. 14;  —  'iiMH  trlrpmF.jf.;  —  ra^wya 'da  F.^f.;  —  pjnse  %ioqm  rasnya  '%ahe YL  72. i;  —  gave  n>ms..'}am ..  v^r^'^rpm W  10. 20.  a)  insbes.  'von  den  Göttern verkündeter,  geoffenbarter  Spruch,  ora- culum':  Ayat  xsmä  'oJis  didaitihs  (sd.) paounJm  Y.  43- 1 1 ;  —  y<icä  vohu  'i>ä /rast  (sd.)  mananhit  yjca  asä  anhSus  Y. 44. 8 ;  —  ditidi  *asä  da  *dar3gäyü  prMvdis (sd.)  lü  '(..lis  maüdä  Y.2S.6;  —  aAm 7'oiB  manauhii  °'6il  (IS.)  yilil^  ärmaitis  .  . mazdJr  rapunm  lag^dS  (sd.)  ".  .  der  Ver- kündigung gemäss  .."  Y. 57.20;  —  aitatca aeiqm  'hanqm  uxhs.btrum  {stL)  yiit's  yaz-a fraia  vaece  ,  .  Y.  79. 10;  —  sarai^ustrahe .  .  paoiryäi  hat/hanuse  gqmca  ahmca '<ijm/a  •tiaSyäca^^  sraosjm  xsa&fvmca  Yt 7^.88.  2)  'Rede,  Reden,  Worte*  im Gegensatz  zu  Denken  (Gedanke)  und  Tun (Werk):  nüit  ttä  manä  ..  naaiä  varanä (sd.)  nSil  'hä  naldä  /yaohamJ  nett  daenä .  .  Aacaintl  Y.  45.3;  —  aiüä  hsi  scanta manatihä  'oiiis  fyao^anilisciJ  xsuüm  (sd.) mazda  Y.  5^.  2 ;  — paurvatätsm  (sd.)  mana- i^hascä  vatfhSui  .  .  syao^anakya  .  .  yäcii ^oahyJcä  .  .^  y.^j.  14;  4>8;  —  vanhSui
8341:•  }.  uparö.kairya-  Adj.  'des  Tätigkeit überlegen  ist,  überlegen  wirkend":  vayus" ys  'ryB  Yti5.4;  ai,  3;  —  vaim  "rlm Y-  25.  5,  Yt  tS-  5;  —  vayaoS  'ryehe  Y. 22.24,  V. /p.13;  —  tiltrJm  .  .  'rim  Yt A4;  —  kavalm  :^armS  .  .  'rim  Yt.  19.9; 45;  —  /w(  z/Tspanam  sravatfhqm  °rim frada'hqm  yim  airyamamm  isttn  FrW.  4. 1 ;
8357:•  j.  upairLkairya-  Adj.  (fem.  ys^  'des Wirksamkeit  oben  gelegen  ist,  von  oben her  wirkend';  fravasayS . .  °rya  .  .ya  upairi  \ */iamarmäi.,  aur7»^anqm..b3züi  scanda- yeittti  YLy.31.
9170:(blossem)  Opt,  'machen,  bewirken,  dass . .': yö  kirsnavat  yim  yazaite  mi^nm , .  xsttBlä albHtS  hyät  "der  bewirkt,  dass  M.,  den er  verehrt,  zufrieden,  ungekränkt  ist"  Vt. lo.iao.  Unklar:    ksr^take  Vyt.47;  —
9172:mit  antarS  'durch  Vermittlung  etwas (Akk.)  Jemandem  (Dat)  erwirken,  ver- schaffen': veAa  xsa^rf/zi  vatrim  biigjm aibl-bairistitn  *vTdlhmnai  (sd.)  .  .  Oiä anlar).caraiil  {i^Y^k.yT'  Y.5/.1.
10636:KompA.  —  El.?J)  —  Pü.  (zu  1);  xral  slarl*), Sü.  1  buddhija4a^,  buddhinaslah,  (zu  Y.  34.  g): ksudrajantui,  erl,:  duflasv.ipadai  pärvaliyah; (lu  l)  xta/sir  (Transskr.).  "  ')  daäiäücä  . . mafyäiirä  sind  attributiv  gedacht.  —  'i  Wie solche  hundertweis  zu  erschlagen  als  verdienst- liches Werk  gilt;  s.  auch  j-rn/j/riJf a«-.  —  31  Die Zerlegung  in  V™/-(s.  i/r>/-)-t*s/ra-  (zum  ai. V.  arfmi)  ist  wenigstens  denkbar;  ^40,1//. — *)  Vgl.  dazu  DsT.  ZA.  r.  208:  "il  ne  serail pas  imposstble  que  ceUe  etymologie  füt  exacte et  quo  ihrajsira  soit  pour  khral\ii)stara,  d'oü "khtalkslaia,  *k/ira/slara".
11862:•  p.  ^taxä-  V.,  nur  mit  Aam  'sorgend wirken  und  schaffen'.     Praes.  2  taxia-.
13167:spitama  ahmäi  dasdl{^^  dainaya  vaf- d^mnSyS . .  mraot  "dieser  Mann,  o  M.Sp., hat  es  sich  vorgenommen,  nachdem  er  es im  Innern  begrifTen  hat:  wer . .,  dem  will er  es  verkünden"  Y.  ji.  19.  4)  mit  einem Konjunktionssatz  'es  dahin  bringen,  es schaffen,  erwirken,  geben,  dass  — ";  dasla ntazdä  *Ä»fä(sd.)^J  yä  v!  md^ra  srrVim arjrfvfsd.)   Y.26'.7.  a)    mit    voraus-
13239:mit  vi  i)  'etwas  (Akk.)  verteilen  an  — ' (Dat.),  eschatologisch  von  Alay.  asi  .. yä  vi  ail/  *rändibyä  savSi  (sd.)  vidäyäf (Konj.)  Y. 43.12;  —  sraidysi  ..ya  vidä- yät  (Konj.)  aiä  räsnam  (sd.)  Y.  34. 2)  '(dahin  und  dorthin)  richten, und  Akk.:  mi^n'm  .  .  yaAmi paiti  ä^rtm  vihat>m  vlspäis  avi  karSt<qn "Af.,  (bei  dem  sva.)  des  AntliU  nach allen  K.  gerichtet  ist"  Yt.  10. 64.  3)  '(ein Haus)  griinden,  erbauen':  sraomn  ..yeAAe nmäntm  . .  Blhättm^^^  barmste  paiti  bari- zaAi  AaraihyS  ..  Y.57.  zi ;  Yt.70.44;  — s.  noch  'vtoäta-.  4)  '(ein  Urteil)  fest- setzen, fallen':  %waAml vS  masda  xsaiiröi asäicä  sSngAs  vTdqm  (35^.)^"*  "in  deinem Reich  wird  euer,  o  M.,  und  des  Asa Spruch  (darüber)  gefällt  werden"  Y.,y2. 6'*'.  s)  Med.  'sich  wo  (Lok.)  fest- setzen': yesica  aiU  asti  diitnAva  aranle ganmöAva  (sd.)  vioante  V,  75, 4.  6)  'tun, betätigen':  voAa  xsa'^rgm  vatrim  bagtm aiblMiri^m  *vldls?mnäi^''^  izilHu  a/J antar?Jarain  syao%attäis  mazdä  vaAisttm "das  gute  Reich,  das  köstliche,  wird  als frommendsten  Anteil  Aia  dem  erwirken, o  M.,  der  mit  Eifer  in  seinen  Werken das  Beste  betätigt"  Y.j/.  i "'.
13448:•  g.  dävoi  Inf.  i)  'zu  geben,  zu  verleihen', als  2PI.:  jP  v<i  .. pairT.jasüi  {^.)  ..  maibyS d'  akva  . .  ayapt^  (sd.)  V.  2Ä  2,  2)  'zu machen,  zu  bewirken':  Sniavaillm  sinqm d°  drj^.-asB  "damit  er  unter  den  Drug- genossen  den  gewaltigen  Zusammenbruch bewirke"  \.44. 14.
13592:in  Aussicht  gestelltes"' Verleihen,  Gewähren', mit  Akk.  des  Obj.,  Instr.  des  Grundes  imd DaL  des  Urhebers:  _)v7  fyao>anä  yl  vaca- !jhä  ytl  yasnä  am?r.'tijt,li>m  as.>mcä  *taiby? '  "Aä  (NS.)  mazdä  .xsu'iK'm(sd.)(ä  haur-.a- \t.iti>    "das  Werk,    das  Wort,    das   Gebet,
13871:hörig  dargebrachte  Verehning':  kö  huyesti  'J;  duiSvaräta-varaz- Adj.  'able  Werke, (sd.)  ks  y^sti  mam  zl  mainydt  yatat^m  \  U^'es  wirkend  t  frai;asayö  .  .  fravaz^U Vt/o  108  '  avaiiAe  narqm  asaoiiqm  qzartke 'varnqm
14967:•  j.  paiti.dvaeSayanti-  f.  'Fähigkeit, Kraft  den  Feinden,  Anfeindungen  entgegen- zuwirken': äicd  '^wqm  cakana  ..variiira- jqslaca  VaÄ  (IS.)  H.2. 11.
14994:•  j.  paiti.bi§ay-  Adj.  'den  Feinden,  An- feindungen entgegen  wirkend':  mqirS Spants . .  *vär>^raynis  *°ii/  bae^azyS  FrW. g.  1;  —  ime  hmti  arsuxha  vSc3  .  .  vSrv- >raynu  'sis  (AP.  als  NP.)  baliazya  Y. 70.18;  —  haemanam  .  .  vär>^rayninam
15051:•  g.  paiü.s5nda-  Adj.  (fem.  -da-)  'entgegen-  j  alwatum  Yt  12. 3.  b)  'nach  vom  hin, wirkend,  Abhilfe  schaffend"»:. o/Bj.-'a  »i..|Vom':  •/«  hl  fiB.n.J  (sd.)  antarät  namit avaocämä  .  .  näsü  faitl.vySda  (sd.)  'da  ■  bnatMyam  .  .  aBa  druxs  .  .  upaMvqsaiH Y..JÄS-  |V.<y.4i;  4a-44.5.  iSt  i6^  18';  —  pasca
15314:Werk)    vollständig    machen,    vollenden';
15322:'Jemanden  (Akk.)  zum  Verlust  von  - (Akk.)  verurteilen';  Pass.  'etwas  (Akk.) rechtskräftig  verlieren,  etwas  verwirken': puxtfmcit  (sd.)  ««  andusqm  tanUm  pir- yeHe''>  "..verwirkt  man  den  Leib"  V.4. 17; —  yö  gä'hä  asrävayS  *qsta{sA.)  va  tarS.- maiti  va  lanüm  *piryeiH  N.  .^'"'*;  42'', 45''. 7''j  —  pt^Janus  ianUm  *piryde*^^1 F.  25b;  —  ''piryäe^'i  F.  10.
```


## [2026-10-17T00:01:26.180Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"varaz-\\|var>z-\\|var3z-\\|varsz-\" BRT.txt | head -15; grep -n \"Arbeit,  Tätigkeit\\|'Tätigkeit\\|Wirken,\\|'Werk\\b\" BRT.txt | head"
}
```


### [2026-10-17T00:01:26.482Z] TOOL RESULT

```
4484:•  j.  anu,  p.  anuv,  g.  33änü ''  i)  Praen, a)  mitAkk.,  a)  'nach,  gemäss':  hvam  'u uStim  zaoämca  V.2. 11; —  °«  a^qmi^A.) N.Äjj/Oj;  —  ftspünam  "u  mainm"n3Lch aller  Urteil"  Yt.5.93.  ß)  'in  der  Rich- tung auf— hin,  an':  Ayaj  *aenatiAe  dr}g- vatö  Ä»J»fl"  isySng  *ankayä  (sd.)  Y.  J2. 16.  b)  mit  Lok.  'längs,  entlang  an— ': !!  zäzänJ'  niima"  vardanam  °uv  ^u/ratauvä (sd.)  Bh.j.19.  2)  Praev.  (mit  '«««-, var>z-,  slü'  u.a.).  [Yt. /o.  137:  lies anu-sasträi,  anu.maiityji.]
10179:•  j.*gavä8trya-varaz-"  Adj.  'der  landwirt- schaftliche Arbeit  verrichtet':  'isit  ilstryeiti anyö  ahmät  yS  hl  'varjs  daidU  aitahmäi "man  begehl  keine  Sunde  ausser  an  dem, der  einem  landwirtschaftliche  Arbeit  tut; dem  soll  man  (Fleisch)  geben"  N.  iS.
13871:hörig  dargebrachte  Verehning':  kö  huyesti  'J;  duiSvaräta-varaz- Adj.  'able  Werke, (sd.)  ks  y^sti  mam  zl  mainydt  yatat^m  \  U^'es  wirkend  t  frai;asayö  .  .  fravaz^U Vt/o  108  '  avaiiAe  narqm  asaoiiqm  qzartke 'varnqm
23003:•  j.,  g.  'varaz-  V.  'wirken'.  Praes.  1 vatvz- :  v»r>z-,  1 6  (Des.)  vJvarfsa-,  1 7  (Fut.)
23006:■varaz-
23033:'  j,  'varsz-  Adj-  'wirkend'. KompE.
23597:•  j.  västryä-varaz-  Adj.  'Feldarbeit  ver- richtend,  in  der  Landwirtschaft  tätig': narqmca  näirinamca  apfrynäyäkanqmcit kainikanqmca  'zanqmca ''  ".  .  und  den Männern  und  Frauen  und  den  Knaben und  Mädchen  und  (Überhaupt  allen),  die in  der  Landwirtschaft  tätig  sind"  V.  68. 12;  —  dahma  näirike  apsrtnäyake  kainiki '«'■>  Y.  2^.3(?).
23889:'  •  j.  vohvaraz-  Adj,  (fem,  'zt-)  'Gutes I  wirkend':  'tarn  asaonam  ..  'sinam  aiao- \tdnqm  Vr. //.  14.
27283:•  j.  sraosä-varaz-  m.  Name  des  siebenten und  geringsten,  mit  der  Kirchenpolizei (s.  No.  2)  betrauten  Unterpriesters  (ratav-); auch  die  Kirchenzucht  liegt  ihm  ob:  *>d'> aiwySxiayai  "der  Sr.  soll  die  Aufsicht fuhren"  N.  Tj''*;  —  *anaiwi.?r?fvB^aiit (sd.)  aSa  abfrtta  *'ta  (ND,)^'  vlcarayattm N.  7p;  —  . .  paoiryS  . .  hävanatum  (sd) . . BstayHH  . .  hapla%3m  'um  N.  tfe;  —  'am Sstäya  Vr.^.i;  0.3.$;  —  rai^wiskare va  •«  vH  V.5.  57;  58;  —  a<):aB  ralui aoxtB  'zB^^  ä^qin  frä^wtrfsaiti  ". .  be- stimmt die  Strafe"  V.  7. 71*';  5.16;  —  'tahe Vyt  15.  a)  vom  Hahn,  der  als  'BUttel' des  Sraosa  gilt,  weil  er  die  Menschen aufweckt  und  so  zur  Erfüllung  ihrer  FSicht antreibt:  kB  asti  sraosahe  a^ehe  ..  '«J'V m?r>yB  yS  parö.dars  nqma  V.  7Ä  1 4  C
30689:•  j.  'hvaraz-  m.  EN.  eines  G^ubigcn, Bruders(?)  des  Ankasa:  •tä  (GD.)  ania- sayS  a/iioni  "des  JI.  und  des  A.,  der beiden  Gläubigen"  Yt. /j.  124.
30714:•  j.  hvarStä-varaz-  Adj.  (fem.  'ti-)  'gute Werke  wirkend';  'r?zqm  alaonqm  .,  •mi- nqm  alaoninqm  Vr.  j/,  14.
23036:•  j.  varara-  m.  'Wirken,  Verrichten  von  — ; Tätigkeif:  *z3mca  haomanankint^a  yasa- maiäe  "die  Tätigkeit  und  die  Wohlgemut- heit ..'"'  Y,7i,  17;  17.  DS,  -tat  als Inf.  sbes.
23717:•  j,  'vfr?a-  i)  Adj.  'wirkend'.  i)  £ 'Wirken,  Tun'.
23721:•  g.  'varaz^na-  n.  'Wirken,  Tätigkeif: ahya  Swa  ährS  (Sp,  3 1 5  u.)  'SSnB  paourtg/l pairj.jasämaidl  mazdä  ahvrä  Y.  ^jff.  i; zit.  V,  /;,  4,  wo  Vfnzäna.
23748:•  j,  varazya-  n.   i)  'Wirken,  Tätigkeit,
23760:•  g.  vnrazyah-  n.  'Wirken,  Betätigen,  ig.6T,  —  ifßrät  Äaca..ayä  t^ye/a  "na" Tun',  mit  Akk.  verbunden:  ayä  *mainivä  *yeymti  Y.J7. 14.  a)  neben  Aalnä-  t varatä  (sd.)  y!  dngvä  aHitä  (APn.)  '^j?! 'Feindesheer' r  «Ji/  i^ra  airya  äaiiihävS aiitn  mainyul  sp^msid  ^-30.5.                    ,/rq/(sd.)  Ayjt  Aafna  nsit  'na  nsit  pqma
30685:"  j.  'hvarez-  Adj.  'des  Wirken,  Tun  gut ist,  wohlwirkcnd':  vattkus  haomö ..kukanß
```


## [2026-10-17T00:01:30.794Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=22950 && NR<=23060 && /^ *1[0-9][0-9][0-9] *$/ {print NR\": \"$0}' BRT.txt; awk 'NR>=23580 && NR<=23600 && /^ *1[0-9][0-9][0-9] *$/ {print NR\": \"$0}' BRT.txt"
}
```


### [2026-10-17T00:01:31.207Z] TOOL RESULT

```
23018: 1377
23592: 1417
23595: 1418
```


## [2026-10-17T00:01:35.809Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^warz\\|^warzīdan\\|^warzīgar\\|^warzāw\\|^warzigar\" PHD.txt PHD_mackenzie.txt | head; grep -n -i \"warz\" NYB_vol2_glossary.txt | head -8; grep -n -i \"varz\\|barz\" HRN.txt | head -15; grep -n -i \"varz\\|barz\" HUB.txt | head -10"
}
```


### [2026-10-17T00:01:36.302Z] TOOL RESULT

```
PHD.txt:608:warz- 88 waxsig
PHD.txt:609:warz-, —išn, v. warzidan.
PHD.txt:610:warzag [ic k! | (N zvarzāw)] ploughing (ox).
PHD.txt:611:warzāwand [wle'wnd | M wrewynd] having miraculous power, powerful.
PHD.txt:612:warz-büm [wlcbwm] cultivated land.
PHD.txt:613:warzidan, warz- [wlc-ytn' | N ~] work, act, practise; till; beget. ~išn: work, tillage.
PHD.txt:614:warzigar [wlcykl | M zorzygr, N barzigar] worker, peasant.
PHD_mackenzie.txt:5221:warz-, -iin, v. warzidan.
PHD_mackenzie.txt:5222:warzag [wlc)k ' I (N warziiw)] ploughing (ox).
PHD_mackenzie.txt:5223:warzawand [wle)wnd I 1'1 wre)wynd] having miraculous power, powerful.
3767:*Tavvak [twpk'] a town 11616, — Cat. 94; Schwarz, Iran II, 66 sgg.; Yäqüt 1,890sg.; Arab Tawwaj, Gr Toxn, Tadxn; as to -wp- for -v- cf s. v. āstavān.
4790:Schwarz, Iran = Paul Schwarz, Iran im Mittelalter nach den arabischen Geographen. 9 Bde, 1896-1969. In einem Band Hildesheim-New York 1969 + Ergánzungsband 1970. 4
2130:aw. [/^varz- 'schaffen, tun'; phlv. varz 'Feldarbeit'
2131:(vd. 6 (71) GL), varzak (AV.), varzUan, varz(i)snTk;
2139:kurd. berz] oss. d. barzond, bärzönd (56); bei. LW.
2143:varz(i)sn, daneben arm. LW. berd 'Burg'; ai. v^dna-
2148:PehlevTworte zu varz zu kommen ; die Ortsnamen auf
2300:aw. 6ama- 'Rücken des Pferdes ; oss. d. barze, t. bärz
3538:np. teberzed (arab. tabarzad) ist Zucker, 'der so hart
7862:aw. vazra- 'Keule ; phlv. vazr, arm. LW. varz; ai.
17050:! varzdßn IÖ9.
851:von barzan noch vollkommen dunkel.
4393:arm. varz, phi. vazr^ zd. vazra-; guraz *Eber' (neben Baraz
5259:iiber , birOdar *Bruder\ barda *Gefangener , barz Teldarbeit',
5454:arm. vat ; bar *Bnist* = zd. varah-, skr. uras- ; barz = varz
5455:Teldarbeit', phi. varz, zd. Wzl. varez; harda 'Gefangener
5611:np. bar *Brust*; vard *Rose' = np. gul; varz 'Stock' = np.
5804:stand, Gedaehtniss, phi. vlr, bal. giv] varz = barz Teld-
7907:xiQh&n\bala, buland § 110, 16; barz^ varz Teldarbeit* (g^\
7935:man *Faden ; varj Xohn, Sold' (entlehnt?), np. varza *Gewinn\
7988:vgl. sn im Zend in baresnu- 'Hohe, Gipfel* = *barznu^ ;
```


## [2026-10-17T00:01:40.618Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2125,2150p HRN.txt; awk 'BEGIN{RS=\"\\f\"} /phlv. varz .Feldarbeit/ {print \"HRNleaf\",NR-1}' HRN.txt; awk 'BEGIN{RS=\"\\f\"} /barz = varz/ {print \"HUBleaf\",NR-1}' HUB.txt; grep -n -i \"warz\\|varz\" CHEUNG.txt | head -12"
}
```


### [2026-10-17T00:01:41.176Z] TOOL RESULT

```
Das u findet sich nicht in den Dialekten, ebenso
auch nicht bei pu/ten, murden u. a. m. (vergl. KZ. 32,
572 flf.).
197. berz^ verz (m Is. 30, 24) 'Feldarbeit*, veme^ verzis^
verz% berztden^ versfiden^), verzgäv, verzäv Tflugstier.
aw. [/^varz- 'schaffen, tun'; phlv. varz 'Feldarbeit'
(vd. 6 (71) GL), varzak (AV.), varzUan, varz(i)snTk;
mand. LW. N'^nxi *Saaten'; arm. gorc *Werk', gorcem
Virken*.
198. hur», *Höhe, hoch' E(\burz\ bulend.
ap. vergl. Bardiya-; aw. berez^, barez- etc. Höhe,
hoch'; phlv. burz, burzak^ burz{i)sn^ burzUan^ buland;
ai. bfhdnt-; arm. barjr *hoch', barnam 'erheben' (H.
No. 52).
kurd. berz] oss. d. barzond, bärzönd (56); bei. LW.
burz etc. (36); sar. LW. büand, bilik.
199. herzen 'Stadtviertel, Quartier.
ap. vardanor- 'Stadt' ; aw. verezena-^ varezCLna- ; phlv.
varz(i)sn, daneben arm. LW. berd 'Burg'; ai. v^dna-
'Umhegung, umfriedigter, befestigter Platz, Flecken,
Ortschaft' 2).
Vergl. Bartholomae, BB. 13, 57 (nur sehe ich
keine rechte Möglichkeit, von dem värün geschriebenen
PehlevTworte zu varz zu kommen ; die Ortsnamen auf
'Verd und -gird gehören keinesfalls hierher).
200. berseiu 'Barsomzweig' (Sahn.).
HRNleaf 67
HUBleaf 165
1129:Varz. dialect of Varzeneh Yzd. dialect of Yazd 
1832:barda/ber-, Varz. barte/ber- ‘to carry, bring (to)’, Nn. barte/bir- ‘to carry off, take 
2117:(+ *ш-) ? Oss. D. ivaerzun/ivarzt ‘to promise; to give hope’ (< *‘to cushion someone 
2183:Varz. bus ‘kiss’ 
2949:čiä, Qohr. cida/cin-, Tr. Ciya/sn-, Varz. Cinde/éin- ‘to reap, gather’, Semn. -cinc- ‘to 
5555:Gil. dustan, Tal. düse, Khuns. dus-/dusa, Varz. dote/dos-, Qohr. dóta/dus-, Tr. döta/ 
6152:durow, Gz. dürün, Qohr. derün, Semn. derow, Shamerz. deru, Tr. deran, Varz. deron 
7152:gä:/amgi:, Qohr. gä-/ -T, Semn. mä-giäf-/mä-g-, Siv. (-)gä-/(-)gäs- ‘to want’, Varz. 
7713:ginn-, Siv. gärän-/gärän-, Tr. gürnä/gürn-, Varz. digirnaye/digirn- (caus.) ‘to kindle 
8081:Meim. be-gardaj-/a-gerd-, Tr. gela(yaygel-, Varz. gartäye/gart- ‘to become, turn’, 
8503:pungent’, саха ‘a biting serpent’, Zaz. gaz (f.), Abz. 207, Varz. gize ‘bite, sting’ 
9450:permit’, Siv. el-, äl-/(h)ist, Tr. hasta/hal-, Varz. heste/hel- ‘to allow, let’, Tal. haste
```


## [2026-10-17T00:01:44.843Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"uarz\\|warz-\\|varzidan\\|varzïdan\\|warzidan\" CHEUNG.txt | head -12"
}
```


### [2026-10-17T00:01:45.245Z] TOOL RESULT

```
20801:(+ *upa-) Pash. brésna ‘brightness, brilliancy’ || (+ *ui-) Sh. (Baj.) warz-/warzd ‘to 
27351:*uarz. || Although referring to Humbach, l.c., Kellens — Pirart II: 299 rather translate 
27392:derive directly from *pari-uarza-, which would have yielded **prwZ- in Chor., cf. 
27507:*uarz 425 
27564:426 *uarz 
27583:*MIDDLE PERSIAN: BMP wlc- /warz-/ ‘to work, do, practise’ (LW), MMP wre, wrz, 
27588:BMP wlc /warz/, 2р1. BMP wlcyt /warzéd/; Inf: BMP wlcytn /warzidan/; Pass.: perf. IND. 3sg. BMP 
27607:*NWIR: NP varzidan/varz- ‘to sow a field’ (LW), barz ‘a sown field; agriculture’ 
27616:9 Apparently, Schindler has argued in his lectures that the (DIr. root *uarz may have 
27618:the preceding vowel in Av. compounds with *uarz and in reduplicative formations: 
35677:wlc- /warz-/, 426 
41633:varzidan/varz-, 426
```


## [2026-10-17T00:01:47.234Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27507,27615p CHEUNG.txt | cut -c1-200"
}
```


### [2026-10-17T00:01:47.536Z] TOOL RESULT

```
*uarz 425 


m[zwrcy- ‘to turn around; to destroy; to turn into, change into’, (intr./med.) ‘to turn 
to someone; to climb, ascend’ || (+ *pari-) prwc- ‘to turn around’ || (+ *ni-) m[nwrcy- 
‘to wrap in; to ruminate (of camels)’ || (+ *ham-) m/wrd- (intr.) ‘to gather’, m/wrcy- 
(tr.) ‘to gather, amass’. 0 Samadi hesitantly proposes *aya-aia-/aua-Cina- (*éai') for 
wcy-. The form may be connected to the root *uart. > Samadi: 212, 217, 9 f., 30, 
264 f., 156, 132, 216 f. 

*NWIR: NP gardun ‘wheel; chariot’, Kurd. (Kurm.) bar (m.), (Sor.) bard, Bakht. bard, 
berd, Siv. värd(e), Yzd. (Zor.) bard ‘stone’, ? NP /aj-vard ‘lapis lazuli’ || (+ *uz-) 
Kurd. (Kurm.) zivirin ‘to turn, be spinning’ || (+ *ni-) NP nawardidan/naward- ‘to 
fold, cease; to twist; to stroll’ 

*NEIR: Oss. I. waerdyn/weerst, D. waerdun/weerst ‘to felt’, Bart. warwar0-/warwuxt 
‘to turn round [intr.]’, warwax-/warwext ‘to turn round [tr.]’ (with redupl. ?), Yi. 
wor-/wusc- ‘to knit’, M. war-/wusk- ‘to stretch the warp on the loom’ (Zarubin) || (+ 
*а-) Pash. awustol/awarom ‘to turn, change, revolve’ || (+ *uz-) Yghn. ziwört-, 
züwört-/ziwörta ‘to turn around, return [intr.]’, zıwirt-/ziwirta ‘to turn back, around 
[tr.] || (+ *para-) Sh. (Baj.) parwar0-/parwuxt ‘to slide down, fall into water with an 
inflated skin for swimming’, parwáx-/parwáxt (caus.) ‘to push, force into water for 
swimming on an inflated skin’, Bart. parward-/parwext ‘to turn upside down’ (less 
likely from *рап-) || (+ *fra-) Oss. D. lewardun/lewarst ‘to go through a certain 
mass [snow, earth], sweeping with the feet’ || (+ *ni-) Oss. I. nywerdyn/nywerst, 
nordyn/norst, D. niweerdun/niwarst ‘to wrap up’, Pash. nwaray (m.) ‘a doubled-over 
hem; draw-string’ || (+ *ham-) Oss. L ewwerdyn/ewwerst, D. zwwardun/ 
zewwarst ‘to knead, smear, rub in’ 

*MISC: Orm. ger-/gerök ‘to roll’, (caus.) Orm. g(e)raw-/g(e)rawök ‘to cause to roll’ 
*SANSKRIT: vart ‘to turn (around), to roll’ (RV+) > EWAia II: 518 

PIE *uert- ‘to turn’ = LIV: 691 f. | Pok.: 1156 ff. 

*IE COGNATES: Lat. verto ‘I tum’, OLat. уог ‘turned’, OCS vretéti ‘to turn 
(around)’, Lith. vifsti ‘to turn (around), to fall over, to become into’, Goth. warp 


‘became’, OHG werdan, NHG werden ‘to become’ (etc.) 

*REFERENCES: EVP: 13; IIFL II: 263a; Abaev, Slovar’ I: 216; Andreev — PeSéereva: 368a ff.; Abaev, 
Slovar’ II: 37, 216 f.; EVS: 92b, 60a f.; DKS: 267a; Vahman — Asatrian 1987: 71; WIM III: 349; Vahman 
— Asatrian 1991: 80 f.; Asatrian — Livshits: 84, 93; Abaev, Slovar’ IV: 92 f.; Werba 1997: 237; Cabolov 
2001: 118; Vahman — Asatrian 2002: 25; NEVP: 59 f.; Kiefer 2003: 197 


*yarz ‘to do, work, till the land’ 

*AVESTAN: voroz- ‘to do, work’ || (+ *abi-) ‘to cultivate’ || (+ *us-) ‘to work away, 
get rid off, repay’ || (+ *fra-) ‘to commit’ || (+ *ni-) ‘to commit against’ = Liste: 
51f. 


Pres. ja-: IND. 15р. YAv. varaziiami (Yt 15.44), 2sg. Y Av. aißi.voroziichi (V 3.26, V 3.28), 35р. YAv. 
voroziieiti, 1р1. OAv. vərəziiamahi (Y 35.7), 3р1. YAv. vorozinti, INJ. 3sg. OAv. varaziiat (Y 47.2), 


426 *uarz 


SUBJ. vereziiat, 3р1. varaziian (Y 35.6, etc.), OPT. 35р. YAv. varaziidit (V 19.41, N 16, FrK 73), 3pl. 
Y Av. "niuuoraziiaiion (Yt 19.80), IMPV. 25р. YAv. varaze (Aog 25), 3sg. OAv. voraziiötü ° (Y 35.6), 
voroziiatam (Y 48.5, etc.); Aor. {1} s-: SUBJ. 159. OAv. varasa (Y 50.10), med. 159. OAv. varasané (Y 
51.1), 3sg. OAv. varosaiti (Y 33.2,Y 46.19), med. 3sg. OAv. varasaité (Y 29.4, Y 33.1), 3pl. OAv. 
varosonti (Y 45.3), IMPV. med. 3sg. OAv. varosuua (Y 53.3), med. 3sg. OAv. varastam (Y 50.11); Aor. 
{2} athem.: INJ. 2sg. OAv. varoš? (Y 39.4), OPT. 1р1. OAv. varazima®, Perf.: IND. 3sg. YAv. "väuuaroza 
(P 17), med. 3sg. OAv. vauuorozoi (Y 29.4), 3du. YAv. vauuarazatara (Y 13.4); Partic.: pres. ҮАУ. 
(voreziiant- (Y 70.4, N 52), YAv. “varazint- (P 13, Vyt 12), med. OAv. varaziiamna- (Y 35.2), YAv. 
vorozimna-, fut. YAv. varasiiamna-, perf. YAv. vauuarozus- (Yt 13.88), med. OAv. vauuarozana- (Y 
35.2), perf. pass. Y Av. uzvarsta- (V 7.51); Inf.: pres. ? OAv. voroziieidiiai (Y 30.5) 


*OLD PERSIAN: (?) vrd- ‘to take’ (differently Kent, l.c.,: vart- ‘to turn’) = Kent: 207a 
Pres. ja-: SUBJ. med. 1sg. vrdiyaiy <v-r-di-i-y-i-y> (DB 4.44). 9 On the reading and interpretation of OP 
vrdiyaiy <v-r-di-i-y-i-y> (DB 4.44) see R. Schmitt 1991: 69. 

*MIDDLE PERSIAN: BMP wlc- /warz-/ ‘to work, do, practise’ (LW), MMP wre, wrz, 
BMP wlc /warz/ ‘miracle, miraculous power’ (LW ?, with suff. *-& ?) > DMMPP: 
344b 

Pres.: IND. 3sg. BMP wlcyt /warzéd/, 2р1. BMP wlcyt /warzéd/, 3р1. BMP wlcynd /warzend/, IMPV. 25р. 
BMP wlc /warz/, 2р1. BMP wlcyt /warzéd/; Inf: BMP wlcytn /warzidan/; Pass.: perf. IND. 3sg. BMP 
wlcyt (YK‘YMWN)yt /warzid éstéd/ 


*PARTHIAN: wrc ‘miracle, miraculous power’ || (+ *fra-) frwrz- ‘to further, cultivate, 


let grow’ = Ghilain: 52 | DMMPP: 344b, 157b 
(+ *fra-) Pres.: IND. 3sg. frwrzyd 


*KHOTANESE: OKh. jsafia-ulysa- ‘causing death’ (Z 24.452) 

*SOGDIAN: BSogd. wrz ‘miracle, magic’ (< MP ?) 

*CHORESMIAN: mwZy- ‘to employ, use; to exert oneself’ = Samadi: 230 

*BACTRIAN: oapCiao, oapCoico ‘farming’ 

*NWIR: NP varzidan/varz- ‘to sow a field’ (LW), barz ‘a sown field; agriculture’ 
(LW), Tr. vast/varz- ‘to happen; to be produced’, Kurd. (Kurm.) bilin/bil- ‘to exert 
(oneself); to carry out’ 

*NEIR: Yghn. warzön-/warzönta ‘to cultivate the land’ 

*SANSKRIT: svávrsti- ‘doing his own work’, epithet of Indra (RV) = EWAia II: 
7951.
```


## [2026-10-17T00:02:00.470Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; grep -l \"not the direct ancestor\\|not a direct ancestor\" page-5*.json | head -3; python3 -c \"\nimport json;v=json.load(open('page-538.json'));e=v['entries'][0];print(json.dumps({k:e[k] for k in e if k!='nodes'},ensure_ascii=False)[:1500]);print(json.dumps(e['nodes'][1],ensure_ascii=False)[:2500])\""
}
```


### [2026-10-17T00:02:01.096Z] TOOL RESULT

```
{"entry": 0, "root": "Wekw, Weqw", "verdict": "confirmed", "modern_form": "PIE *wekʷ- 'to speak' (Pokorny 1135-1136 u̯ekᵘ-; LIV² 673f.; Watkins wekw-; o-grade root noun *wṓkʷs 'voice')", "note": "Root, label and gloss are correct: Pokorny 1135 u̯ekᵘ- 'sprechen' with Skt. vakti, vāc-, vacas-, Av. vac-, vacah-, vāxš, Gk. épos, ops, Lat. vōx, vocāre (WP I 245f.). Cheung 2007 (*u̯ač) and Wiktionary agree. The Latin/English branch and the Avestan vāč-/vacah-/uxδa- branches are textbook. The weaker parts of the chart are the Iranian compounds Nourai reconstructs or invents to reach particular New Persian words: 'paurvatâ-vac' (for pažvāk), 'hu-ni-vak' (for xonyā), Avestan 'vaxš-ô-bara' (only a reconstruction *vaxša-bara- behind MP waxšwar) and 'Old Persian wâk/wânk' (not attested). The derivation of xonyā (MP huniyāg) from *hu-ni-vāka- is opposed by the Middle Persian form, which has no -w- (see node 9). forūxtan 'sell' is linked to vac- by Justi/Horn/Mo'in, but Cheung puts it under *waxš- 'grow' (see node 4). The extraction matches the printed page (checked against site/pages/538.jpg).", "note_fa": "ریشهٔ هندواروپایی آغازین *wekʷ- «سخن گفتن» با بالاگونهٔ o در نام‌واژهٔ *wṓkʷs «آواز، صدا» در پوکورنی (ص ۱۱۳۵-۱۱۳۶)، والده-پوکورنی (ج ۱، ص ۲۴۵)، واتکینز و چونگ آمده است. بازمانده‌های آن سنسکریت vāc- و vacas-، اوستایی vāč- (حالت فاعلی vāxš) و vacah- «سخن»، یونانی épos و لاتینی vōx و vocāre است. ریشه و زبان و معنایی که نورایی داده درست است. ولی چند ترکیب ایرانی در این نمودار ساختهٔ خود او
{"id": 2, "lang": "Persian", "words": "vâk; vâžeh; vâžgân; vâž", "verdict": "plausible", "derivation": "vāž / bāž / bāj 'the murmured Zoroastrian prayer, grace' continues MP wāž [wʾc] 'word, speech; grace (before meals)' < Old Iranian *wāč- (Av. vāč-). Initial w- became b- in standard New Persian (bāž, bāj), while the variant vāž keeps the older w-. The Ferdowsi line quoted on the page uses exactly this ritual sense. vāže 'word' matches MP wāzag [wʾckʾ] 'utterance, saying' < *wāčaka-. Because of its -ž- it is classed as a word from another Middle Iranian language (Wiktionary: 'Middle Iranian'); inherited MP would give -z-. Both are confirmed. vâk 'sound' and vâžgân 'vocabulary' are not old words but 20th-century learned formations. Dehkhoda knows واک only as the name of a water bird, and Mo'in gives واژگان only in its modern sense 'list of words'. Their link to the root is etymologically sound, but they are revivals, not inherited forms.", "derivation_fa": "«باژ / باج / واژ» به معنی زمزمهٔ آهستهٔ دعای زرتشتیان از فارسی میانهٔ wāž «سخن، دعای پیش از خوراک» و ایرانی باستان *wāč- (اوستایی vāč-) است. w آغازی در فارسی نو به b بدل شده («باژ»، «باج»)، ولی صورت «واژ» w کهن را نگه داشته است. «واژه» با فارسی میانهٔ wāzag «گفته» و *wāčaka- برابر است، ولی به سبب ž احتمالاً از یک گویش دیگر ایرانی میانه آمده است. بارتولومه و برهان (حاشیهٔ معین) و ویکی‌واژه این‌ها را تأیید می‌کنند. اما «واک» به معنی صدا و «واژگان» ساخته‌های نوین سدهٔ بیستم‌اند و واژهٔ کهن موروثی نیستند: دهخدا «واک» را تنها نام پرنده‌ای آبی آورده است. پس ادعای نورایی در کل با احتیاط پذیرفتنی است.", "sources": ["https://en.wiktionary.org/wiki/واژه", "https://vajehyab.com/moein/واژه", "https://vajehyab.com/moein/واژگان", "https://vajehyab.com/moein/واژ", "https://vajehyab.com/dehkhoda/واک"], "ref_check": [{"ref": "BQT:204", "status": "supports", "note": "BQT_v1_pages.txt leaf 423 (p. 203/204), Mo'in's note 9 on باج: 'باج و باژ و باز و واج و واژ باین معنی از ریشهٔ اوستایی vāč (گفتن)، سانسکریت vāc، در پهلوی vāž یا vāč، در لاتینی vox ... در انگلیسی voice. باژ بمعنی کلمه و سخن و گفتار است. کلیهٔ دعاهای مختصر را که زرتشتیان آهسته بزبان میرانند باژ گویند' + the Ferdowsi line 'پرستندهٔ آذر زردهشت ...'."}, {"ref": "BQT:218", "status": "supports", "note": "BQT_v1_pages.txt leaf 438 (running head ۲۱۸): باز '... و بمعنی خاموشیی باشد که مغان در وقت بدن شستن و چیزی خوردن بعد از زمزمه اختیار کنند' and 'باژ - بزای فارسی، بروزن و معنی باج' -- the ritual murmur sense."}, {"ref": "BQT:2260", "status": "partial", "note": "BQT
```


## [2026-10-17T00:02:05.322Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /varz|Feldarbeit|برزگر/ {print \"leaf\",NR-1}' BQT_v1_pages.txt | head; "
}
```


### [2026-10-17T00:02:06.417Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:02:13.950Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 600 BQT_v1_pages.txt; echo; grep -c \"\" BQT_v1_pages.txt; grep -n \"برز\" BQT_v1_pages.txt | head"
}
```


### [2026-10-17T00:02:14.283Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م�
32486
1115:ولیز در « کشتن هرمز وسیماه برزین ؛بهرام آنر مهانرا» آرد ٩‏ :
1412:۷۵۳۵ قح (ما میگو یم )؛ شپمبرزادی 18818 (می‌افند) .سمنانی
2343:ازد کتر مبرزا علی| کبرخان نقبسی ناظم-
3145:مبرزا اسدالة غالب, شاعر کی در کتاب «قاطع برهان» خود که رد بربرحان‌قلطع
4155:۱ آتش برزین ؛ آتش باره " آنشکده ۰ آنشگاه »
4174:ازداو یر اف » انوشروان » اوستا . بختباری » برانوش : برزوی» بزر گمپر
6534:۵ آقشیبرزیی - رك: آندبرزین  .‏ 5 آلش پاره - اخگرکرم شب‌تاب - مجازاً مخت جانی
6566:چون آتش خاطر مرا شاه بدید از خا مرا برزبر ماه کشید.. «معزی۸۱۱*
7007:است که در فاری برزین نام , شخصی از خلفای
7011:از اسب انداخت ؛ درآن ائنا صاعقه افتاد وبرزین
```


## [2026-10-17T00:02:16.904Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:254 --image 2>&1 | tail -40"
}
```


### [2026-10-17T00:02:17.278Z] TOOL RESULT

```
no scan of BQT covers printed page 254 (see 'scans' in refs_online.json)
```


## [2026-10-17T00:02:21.023Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 472 473 474 475 476; do echo \"== leaf $l\"; awk -v n=$l 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | grep -n \"برز\\|ورز\\|varz\\|barz\\|۲۵[۳۴۵]\" | head -8; done"
}
```


### [2026-10-17T00:02:21.554Z] TOOL RESULT

```
== leaf 472
== leaf 473
== leaf 474
1:برزستد ۱ 3 ۰ ج ووات
10:برزیگر و زراعت کننده را گونند . ۱
12:پرزکار و برزمگر باشد که زراعت کننده است .
27:و زراعت و کشاورزی باشد ۱ - و ماه بثابان را
36:کردن) «بارتولمه ۰۱۳۷۸ در فارسی برز و ورز «یب رکه۲۳4 .
37:۴ - در اوستابی 6162810 بمعنی بلندي و پشثه و کوه است ومشتقات زد دارد.وبرز
40:و نیز برز کوه بمعتی البرز کوه آمده » فردوسی طوسی گوید :
42:نپادند بربکدیگر تبغ وکرز  .‏ چو منکههکران‌کابد از کوه برز . اسدی‌طوسی.
== leaf 475
16:ورزیدن است که مواظبت و مداومت کردن باشد
25:که آنرا آندبرزین نام کرد و آن آنشکده ششم
26:است - و بمعنی برزن هم آمده است- و صجرا
47:ركك : ورزیدن .
== leaf 476
36:بقه از مضه ۲۵۵
```


## [2026-10-17T00:02:24.278Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==475' BQT_v1_pages.txt | sed -n 1,40p; awk 'BEGIN{RS=\"\\f\"} NR==476' BQT_v1_pages.txt | sed -n 10,20p"
}
```


### [2026-10-17T00:02:24.857Z] TOOL RESULT

```
برزستد ۱ 3 ۰ ج ووات
بنابان را نیز کفته‌اند .
بر ددن - بر وزن‌ک رکدن . آنت که
دوکس با بیشتر از دو سه طرف انگختان خودرا
پیش آورند وحساب برد وباختی کنند - و بمعنی
بهم برآوردن و از عم جدا کردن هم هنت ۴ -
و رسیدن کشتی راز گونند بکتار دربا و کنابه
از هحسری و برابری کردن باشد .
برد کار ۴ » با کاف بروزن قرض‌دار .
برزیگر و زراعت کننده را گونند . ۱
پر گر * - بنتح کاف فارسی » بمعنی
پرزکار و برزمگر باشد که زراعت کننده است .
بر د ۵ بروزن‌ریم » بمعنی‌ناز و کرشمه
باشد - و نام قلعه‌ابست بر کنار آفت آمو -
بر دن « بفتح اول بروزن ارزن » کوچه
و محله را کویند ٩‏ - و بمعتی صحرا نیز بنظر
آمده است - و آمر بزدن هم هست یمنی بزن-
- لیرد سای « بروزن بر‌دهید » بمعنی‌رسید
و آمد باش که ماضی رسیدن و آمدن است -
و بمعنی سوال کرد و پرسید هم هست که ماضی
صژال کزدن و پرسیدن باشد . #
بر دویدو یدن حکنابه از کرم‌عنان
شدن د رکفت وکوی باشد .
7 رد۵ - بروزن درکه . آراسته و خوب
وا راگن و خوی را گوستف::
رت بنتمایلبروزن طرز » بسعنی کدت
و زراعت و کشاورزی باشد ۱ - و ماه بثابان را
نیز گوبند که بدان کهگل و گچ بر دبوار مالند
- ویمعنی زسابی و معشوقی و بلندی بالای (۱)
حردم و ثنهةٌ درخت نیر آغفه است - و مطلق
بلندی راهم گفته‌اند - ویضم‌اول ۷
وقد و قامت آدمی - ود وعظمت باشد ۴ -
و بلندی‌بالای مردم وچاروا را نیز گومند وبمعنی
مطلق بلندی و تنةٌ درخت هم آمده است -ومالة
۱ - در پپلوی ۷۵2۲2 (ار کردن , اجراکردن ؛ کار . عمل) از اوستابی ۷8۳۵22 (کار
کردن) «بارتولمه ۰۱۳۷۸ در فارسی برز و ورز «یب رکه۲۳4 .
۴ - در اوستابی 6162810 بمعنی بلندي و پشثه و کوه است ومشتقات زد دارد.وبرز
فارسی بمعنی بلندی و بزرکی و شکوه از همین ربشه است . عنصری بلخ ی کوید :
فر و کوفتند آن بتان را بگرز به شان رنگه ماند و نه فر ونه پرژ.
و نیز برز کوه بمعتی البرز کوه آمده » فردوسی طوسی گوید :
پرره‌کاد ؟ « پروزن‌هرزهکار ,برژیگر
و زراعت کننده باشد.
بر ده گاو ۴ کاو زراعت را گونند»
پرره گر ه « بقنح کاف فارسی پروزن
بردمدر ؛ بوژسگر و زرات کننده را گوجه
بر ر بدن ٩‏ بر وزن لرزیدن بمعنی
ورزیدن است که مواظبت و مداومت کردن باشد
درکاری .
بر ریگر ۳ بروزن عکدیگر ۰ زارغ
و ژرامت کننده را گونند ۰
فردلن ٩‏ ۰ بروزن پروین» بمعنیآتش
```


## [2026-10-17T00:02:30.943Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:2268 --image 2>&1 | tail -60"
}
```


### [2026-10-17T00:02:39.122Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 351; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2268.png
REF: BQT:2268  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 351  OCR-lang: fas

ورد -۹۸-
اد بروزن کرمان, دانپای سشت را کویند که وجهاز عروس را دی ز گفته انده. .
ازاعضای آدمی برميآاید وبمربی‌تژلولمیگویند9- ورد و که - بنتع اول و کاف آخر,
و بممنی شاگردان و مربدان هم هس ت که جمع بمه‌نی اول وردوك است که خانهٌ علفی باشد .
شاگرد ومرید باشد چه وردیمعنی‌شا گرد ومرید ورده۷ بفتح اول وئالت » مطلق‌برج
است . را کوبند عموماً وبرج کیوتررا خصوصاً .
وردل4؟ - بفتم اول بر وزن زردك , وردیج۸ - باجیم ابجد بروزنسرپیچ.
جهاز عروس را کوبند یمنی اسبای ی که بااوبخالهٌ | بمعنی ورتیچ است که پرند كوچك نر از تیهو
شوهر برند . باغد که عربان‌سلوی وترکان بلدرچین میگویند.
ور دنه۴ - بنتح اول وئالك‌ونون,چویی ورز* « بنتح اول وسکون ثانی وزای
باشد هردوسی باريك ومیانکنده که خمین نانر! | نقطه دار » بمعنی حاصل کردن باشد - وکشت
بدان پهن سازند - وچوبی‌را نیز کوبن دکهچرخ و زراعت را لیز کوبند *۱- وهر صنعت وحرفت
برآن گردد ویعربی مور خوانند ۰ وکار باشد عنوماً۱۱- و صنعت دباغت را کوبند
وردوك - بر وزن مفلوك, خانه‌ای‌را | خصوصاً - ونام رودخانهٌ ماوراء النهرهم هست9۳,
کوبند که باچوب و علف پرشیده باشند ۴ - | وماوراءالنهررا نیز کوبند۱۴۳- وبمعنی پیاهی‌کاری
۱ - «وردان (بالکروفتح دالمپمله) زخ باشد که بهندی مه گوبند.» « رشیدی » ور4:
اجمن‌آرا ۰ ۲ وردوك (د.م.) ۴ واردن (.م.) و رك4 : رشیدی . گلپایگانی
42 ( چوبی که باآن خمیر را صاف کنند و بشکل استوانه درآورند) « قاسمی >.
ی * ورد و که («.م.) که بهندی چهپر گونند رشیدی ؛. ۵ * وردك4 («.م.)
۹ * ورد (.م.) ۷ - «ورده » چوب کبوتر بازان باشد که کبوتر براند
( پراند . دهغد! ). منجيك (ترمذی) کوید :
چون مرفش از هوا بسوی ورده از معده پاز تاوه شود نات . >
« لغت فری ص 1۷۶ >-
۸ ورتیج (ه.م.) ۳ وردج ۳ ورتك » هندی باستان 8( بادرچین (« پپلوی
۴ بونای 0۲1۴ ۰ کردی ]۷۵۲۵ ۰ 2۷8۳۵6 ( بلدرچین ) ۰ افغانی ۰8۷8782
استی ع() ۷2۳۵463 ۰ بلوچی 8۷274128 (کبك کوهی) » وخی ۷010 « اسشق ۱۰۷۸ ورك :
ژابا ص 2۳۰ . طبری ۷8748 ( مرغی است در مازندران معروف و بدیلم آنرا « وشم » بضم واو
وشین معجمه ومیم » و بعربی سمانی کوبند وخایف وجبان‌ترین طیور ات چنانکه کفته‌اند اگر
بانك رعد بشنود بمیرد » لهذا عربآنرا قتیل‌الرعد خوانده » وآن غیر سلوی است ) « انجمن‌آرا:
ورده ؟ . ‎٩‏ - پپلوی ۷2۲2 (کا رکردن » عمل ؛ کار؛ شغل ) ؛ از اوستا -۷۵۳922 ( کار
کردن ) « بارتولمه ۱۳۷۸ *. قس : فارسی برز » ورك : ورزیدن « لیب رک ص ۲۳4 *.
*- در: کشت و ورز ؛ در اراك ( سلطانآباد ) ۷8۳2 ( زراعت کردن ) « مکی‌نژاد >.
۹۱ ورز غنی بباید اندر خور غنی ورز فقیر باید در خور فقیر .
منوچهری دامغانی ص ۳۶ ۰
۴۳ سرا جکوید : « دربرهان نام رودخانةٌ ماوراءالته گفته » وان اختراع محض امت»
بنقل فرهنگه نظام ج وص مب » برهان خود اختراع نکرده » ور3 : ورز رود » ورارود .
```


## [2026-10-17T00:02:44.059Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-17T00:02:44.068Z] TOOL RESULT

```

```


## [2026-10-17T00:02:55.400Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | grep -i \"usage\\|argv\\|print\\|web/\" | head"
}
```


### [2026-10-17T00:02:55.718Z] TOOL RESULT

```
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--note" in sys.argv:
        note = sys.argv[sys.argv.index("--note") + 1]
        print(__doc__); return 2
```


## [2026-10-17T00:03:01.618Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f(){ python3 tools/fetch_source.py \"$1\" --note \"page 549, root Werg 1: $2\"; }; \nf 'https://en.wiktionary.org/wiki/ورزیدن' 'NP varzidan etymology'\nf 'https://en.wiktionary.org/wiki/ورز' 'NP varz/barz'\nf 'https://en.wiktionary.org/wiki/ارغنون' 'NP/Ar arghanun'\nf 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wergʷ-' 'PIE root'\nf 'https://www.etymonline.com/word/boulevard' 'boulevard < bulwark'\nf 'https://www.etymonline.com/word/organ' 'organ'\nf 'https://www.etymonline.com/word/work' 'work'\nf 'https://www.etymonline.com/word/energy' 'energy'\nf 'https://vajehyab.com/moein/ورزاو' 'Moin varzav'\nf 'https://vajehyab.com/moein/ورزش' 'Moin varzesh'\nf 'https://vajehyab.com/moein/ارغنون' 'Moin arghanun'\nf 'https://vajehyab.com/moein/ارگ' 'Moin org'\nf 'https://vajehyab.com/moein/بلوار' 'Moin bolvar'\nf 'https://vajehyab.com/moein/انرژی' 'Moin energy'"
}
```


### [2026-10-17T00:03:07.442Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a84c61e52a52384d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a90c6bdeaaf3c4e2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/61eebb77613545fe.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a798bf3b9d3a42b8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c1cafbbcba9b31d0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8130dec0c106d1ae.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a4295efbab29cc33.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f8516a31989b54b3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bde3d787044171c8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bb76a200b2d918c1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/422832232202408e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9e3869d13f0a3760.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/081aeab42ce6671f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5042b7dedbf3539c.txt
```


## [2026-10-17T00:03:12.108Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wérǵom' --note 'page 549, Werg 1: PIE *wérǵom'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/ὄργανον' --note 'page 549 organon'; cd data/verification/sources/web; for f in a84c61e52a52384d a90c6bdeaaf3c4e2 61eebb77613545fe a798bf3b9d3a42b8; do echo \"=== $f\"; head -c 300 $f.txt; echo; grep -i -m6 \"etymolog\\|from \\|borrowed\\|inherited\" $f.txt | cut -c1-400; done"
}
```


### [2026-10-17T00:03:13.329Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/073420d99b5965b2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/448e533f34f018eb.txt
=== a84c61e52a52384d
URL: https://en.wiktionary.org/wiki/ورزیدن
FETCHED: 2026-10-17T00:03:02Z
STATUS: 200
TITLE: ورزیدن - Wiktionary, the free dictionary

ورزیدن - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community
 Etymology 
 From Wiktionary, the free dictionary
 Etymology
 Ultimately from Proto-Iranian *wr̥jyáti ; see there for further information. Cognate with English work and Ancient Greek ἔργον ( érgon ) .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=ورزیدن&oldid=93606659 "
 Categories : Persian terms derived from Proto-Iranian 
=== a90c6bdeaaf3c4e2
URL: https://en.wiktionary.org/wiki/ورز
FETCHED: 2026-10-17T00:03:03Z
STATUS: 200
TITLE: ورز - Wiktionary, the free dictionary

ورز - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requeste
 Etymology 
 From Wiktionary, the free dictionary
 Etymology
 Ultimately from Proto-Iranian *wr̥jyáti ; see there for more. Cognate with English work and Ancient Greek ἔργον ( érgon ) .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=ورز&oldid=93606794 "
 Categories : Persian terms derived from Proto-Iranian 
=== 61eebb77613545fe
URL: https://en.wiktionary.org/wiki/ارغنون
FETCHED: 2026-10-17T00:03:04Z
STATUS: 200
TITLE: ارغنون - Wiktionary, the free dictionary

ارغنون - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community
 Etymology 
 From Wiktionary, the free dictionary
 Etymology
 From Ancient Greek ὄργανον ( órganon ) .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=ارغنون&oldid=90498078 "
 Categories : Persian terms derived from Ancient Greek 
=== a798bf3b9d3a42b8
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wergʷ-
FETCHED: 2026-10-17T00:03:04Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-10-17T00:03:19.168Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in c1cafbbcba9b31d0 8130dec0c106d1ae a4295efbab29cc33 f8516a31989b54b3 073420d99b5965b2 448e533f34f018eb; do echo \"=== $f\"; sed -n 3p $f.txt; grep -i -m4 \"bulwark\\|organum\\|weorc\\|energeia\\|wérǵom\\|from Proto\\|Etymology\" $f.txt | cut -c1-500; done; for f in bde3d787044171c8 bb76a200b2d918c1 422832232202408e 9e3869d13f0a3760 081aeab42ce6671f 5042b7dedbf3539c; do echo \"=== $f\"; sed -n 3p $f.txt; grep -m3 \"\\[\\|(اِ\" $f.txt | cut -c1-300; done"
}
```


### [2026-10-17T00:03:19.596Z] TOOL RESULT

```
=== c1cafbbcba9b31d0
STATUS: -1
=== 8130dec0c106d1ae
STATUS: -1
=== a4295efbab29cc33
STATUS: -1
=== f8516a31989b54b3
STATUS: -1
=== 073420d99b5965b2
STATUS: 200
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wérǵom
TITLE: Reconstruction:Proto-Indo-European/wérǵom - Wiktionary, the free dictionary
Reconstruction:Proto-Indo-European/wérǵom - Wiktionary, the free dictionary 
 Etymology 
=== 448e533f34f018eb
STATUS: 200
 Etymology 
 Etymology
 From Proto-Indo-European *werǵ- ( “ work ” ) , formed similarly to ξόᾰνον ( xóănon , “ statue, xoanon ” ) ; compare ἔργον ( érgon , “ work, deed ” ) . [ 1 ] 
 → Latin: organum ( see there for further descendants )
=== bde3d787044171c8
STATUS: -1
=== bb76a200b2d918c1
STATUS: 200
 (وَ زِ) 1 - (اِمص .) تمرین ، کار پیاپی و مرتب . 2 - (اِ.) انجام حرکات بدنی خاص برای تقویت عضلات .
=== 422832232202408e
STATUS: 200
 (اَ غَ) [ معر - یو. ] ( اِ.) نوعی ساز که از تعداد زیادی لوله تشکیل شده و هوا را به وسیلة انبان در آن ها می دمیدند.
=== 9e3869d13f0a3760
STATUS: 200
 ( اُ ) [ فر. ] ( اِ.) 1 - ارغنون . 2 - نوعی ساز شبیه به پیانو اما کوچکتر از آن .
=== 081aeab42ce6671f
STATUS: -1
=== 5042b7dedbf3539c
STATUS: 200
 (اِ نِ) [ فر. ] (اِ.) نیرو، قدرت ، توانایی انجام کار، کارمایه (فره ). ؛~ اتمی نوعی انرژی که در واکنش های هسته ای آزاد می شود، انرژی هسته ای . ؛~ خورشیدی انرژی تابشی پرتوهای خورشید. ؛~ پتانسیل انرژی که اجسام بر اثر قرار گرفتن در وضع خاصی دارا می شوند. ؛~ مکانیکی انرژی حاصل از عملیات مکانیکی . ؛~ الک
```


## [2026-10-17T00:03:26.434Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f(){ python3 tools/fetch_source.py \"$1\" --note \"page 549, root Werg 1: $2\"; }; \nf 'https://vajehyab.com/dehkhoda/ورزاو' 'Dehkhoda varzav' ; f 'https://vajehyab.com/dehkhoda/بلوار' 'Dehkhoda bolvar'; f 'https://vajehyab.com/moein/ورزیدن' 'Moin varzidan'; f 'https://vajehyab.com/moein/برزگر' 'Moin barzgar'\nf 'https://en.wiktionary.org/wiki/boulevard' 'boulevard'; f 'https://en.wiktionary.org/wiki/organ' 'organ'; f 'https://en.wiktionary.org/wiki/work' 'work'; f 'https://en.wiktionary.org/wiki/بلوار' 'bolvar'; f 'https://en.wiktionary.org/wiki/ارگ' 'org'; f 'https://en.wiktionary.org/wiki/ورزش' 'varzesh'; f 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wr̥jyáti' 'PIr *wrjyati'"
}
```


### [2026-10-17T00:03:34.018Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/76d0d448ad993eb8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fd8a45b043908698.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/86258942d1ebd8aa.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/47c8fc2dc4fc275a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bf8e3efccd85248e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/41226a7798b2a3d7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/60ab168c71a55c64.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/52cbb109ac8093a4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3e9669d72102790e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/47cbcbabd145adf0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/885b6785e25909d2.txt
```


## [2026-10-17T00:03:38.190Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 76d0d448ad993eb8 fd8a45b043908698 86258942d1ebd8aa 47c8fc2dc4fc275a; do echo \"=== $f\"; sed -n 3p $f.txt; grep -m3 \"\\[\\|(اِ\" $f.txt | cut -c1-400; done; for f in bf8e3efccd85248e 41226a7798b2a3d7 60ab168c71a55c64 52cbb109ac8093a4 3e9669d72102790e 47cbcbabd145adf0 885b6785e25909d2; do echo \"=== $f\"; sed -n 3p $f.txt; grep -A2 -m3 \"^ Etymology$\" $f.txt | cut -c1-500; done"
}
```


### [2026-10-17T00:03:39.052Z] TOOL RESULT

```
=== 76d0d448ad993eb8
STATUS: 200
 ورزاو. [ وَ ] (نف ، اِ) گاوی را گویند که زمین بدان شیار کنند، یعنی گاو زراعت . (برهان ) (آنندراج ) (ناظم الاطباء) (انجمن آرا). رجوع به ورزا شود.
=== fd8a45b043908698
STATUS: 200
 بلوار. [ ب ُل ْ ] (فرانسوی ، اِ)بولوار. (فرهنگ فارسی معین ). رجوع به بولوار شود.
=== 86258942d1ebd8aa
STATUS: 200
=== 47c8fc2dc4fc275a
STATUS: 200
=== bf8e3efccd85248e
STATUS: 200
 Etymology
 [ edit ] 

--
 Etymology
 [ edit ] 

--
 Etymology
 [ edit ] 

=== 41226a7798b2a3d7
STATUS: 200
 Etymology
 [ edit ] 

--
 Etymology
 [ edit ] 

--
 Etymology
 [ edit ] 

=== 60ab168c71a55c64
STATUS: 200
 Etymology
 [ edit ] 

=== 52cbb109ac8093a4
STATUS: -1
=== 3e9669d72102790e
STATUS: 200
=== 47cbcbabd145adf0
STATUS: 200
 Etymology
 [ edit ] 

--
 Etymology
 [ edit ] 

=== 885b6785e25909d2
STATUS: 200
 Etymology
 [ edit ]
```


## [2026-10-17T00:03:42.990Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in bf8e3efccd85248e 41226a7798b2a3d7 60ab168c71a55c64 47cbcbabd145adf0 885b6785e25909d2; do echo \"=== $f\"; grep -A4 -m2 \"^ Etymology$\" $f.txt | grep -v \"edit\\|^--\\|Etymology\" | cut -c1-600; done; grep -m4 \"ورز\\|(ف\" 86258942d1ebd8aa.txt 47c8fc2dc4fc275a.txt | cut -c1-300; grep -m3 \"Etymology\" -A3 3e9669d72102790e.txt | head"
}
```


### [2026-10-17T00:03:43.672Z] TOOL RESULT

```
=== bf8e3efccd85248e

 Borrowed from French boulevard , from Middle French boulevard , bollevart , boulevars , bolevers , bollewerc ( “ rampart ” ) , from Middle High German bolewerc , bolwerc (modern German Bollwerk ) or Middle Dutch bolwerk ( “ bulwark , bastion ” ) . Doublet of bulwark ; more at bole , work .


 Borrowed from French boulevard , borrowed from Middle Dutch bolwerk ( “ bulwark , bastion ” ) . Doublet of bolværk .

=== 41226a7798b2a3d7



 From Dutch orgaan , from Middle Dutch organe , from Latin organum , from Ancient Greek ὄργανον ( órganon ) .

=== 60ab168c71a55c64

 From English work ( verb ) .

=== 47cbcbabd145adf0




=== 885b6785e25909d2

 From Proto-Indo-Iranian *wr̥ȷ́yáti , from Proto-Indo-European *wr̥ǵyéti .

86258942d1ebd8aa.txt:URL: https://vajehyab.com/moein/ورزیدن
86258942d1ebd8aa.txt:TITLE: معنی ورزیدن | فرهنگ انتشارات معین | واژه یاب
86258942d1ebd8aa.txt:معنی ورزیدن | فرهنگ انتشارات معین | واژه یاب 
86258942d1ebd8aa.txt: ورزیدن
47c8fc2dc4fc275a.txt: (بَ گَ) (ص فا.) زارع ، کشاورز. برزیگر هم گویند.
 Etymology 1 

 1.1.1 
 Alternative forms 
--
 Etymology 2 

 1.2.1 
 Pronunciation 
--
```


## [2026-10-17T00:03:49.110Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -m3 \"^work,\\|^bulwark,\\|^boulevard,\\|^organ,\\|^energy,\\|^surgery,\\|^ergon,\\|^ergo-\" KLN_1966.txt | cut -c1-600; grep -n \"^WORK\\|^BULWARK\\|^BOULEVARD\\|^ORGAN\\b\\|^ENERGY\\|^SURGEON\\|^SURGERY\" SKT.txt | cut -c1-400"
}
```


### [2026-10-17T00:03:49.379Z] TOOL RESULT

```
12862:ORGAN.
```


## [2026-10-17T00:03:52.893Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *work, \\|^ *bulwark\\|^ *boulevard\\|^ *organ, \\|^ *energy, \\|^ *surgery\\|^ *ergon\" KLN_1966.txt KLN_1971.txt | cut -c1-500 | head; grep -n -i \"^bulwark\\|^boulevard\\|^work\\b\\|^organ\\b\\|^energy\\|^surgery\" SKT.txt SKT_dli_revised.txt | head"
}
```


### [2026-10-17T00:03:53.535Z] TOOL RESULT

```
KLN_1966.txt:1026:surgery
KLN_1971.txt:3767:surgery 
KLN_1971.txt:11566:ergon and cp. energy. 
KLN_1971.txt:29075:work, task*. These words prob. derive fr. Fran- 
KLN_1971.txt:32365:boulevard, n. — F., earlier boloart , boulevert, 
KLN_1971.txt:35193:bulwark, n., 1) rampart; 2) protection. — ME. 
KLN_1971.txt:45571:ergon and cp. surgeon, which is a doublet of 
KLN_1971.txt:54736:organ, radio or phonograph. — F., ‘console, 
KLN_1971.txt:59157:work, hurdle’. See crate and cp. words there 
KLN_1971.txt:76294:ergon and words there referred to. The word 
SKT.txt:7753:work  (HalliwcU).  — O.  F.  gob,  lit  a  moi
SKT.txt:12862:ORGAN.
SKT.txt:15687:work,  Bttch  ai  the  bars  in a  nunger,  a  frame-work irc,  A  bar  with  teeth  in  which can  work.  On  tht  rack  -  in ;  %.raek-rtnt  \%  a  rent  stretchcfl le,  or  nearly  sa  Allied  words \r,  ttnigfat,  ftkkJQ,  to  strain, to  stretch,  reach  out,  to rak,  straight.  G.  rack,  a  rack, to  stretch:  c»p.  Low  G.  rakk, E.  ptaU'TOck.  %  Kack  is \  senses  than  any  other  E. ■i  (J),  rack  (3\  &c. the  projection  of  the  extrenii- bcyond  the  Iceel,  the  tnclina- I  from  the  ijerpenilitnlar. •ca-Un^iage,  the  rake  of  a of  her  hiHl  or  main  body, both  the  ends  of  her  keel ; ' d).  Evidently  from  rake,  vb., d  (HalUwcll).  -  Swell  dial lh>  rokafram,  to  reach  over, rtigt,    to    project,  jut    out.
SKT_dli_revised.txt:9781:work (Ducauge). Of unknown origin; 
SKT_dli_revised.txt:10257:Bulwark. (Scand.) Dan. bulvcerk, 
SKT_dli_revised.txt:11936:work in timber. — L. carpentum^ a carriage ; 
SKT_dli_revised.txt:12038:bulwark, to hinder those who enter the 
SKT_dli_revised.txt:13088:work. See Ajar. Chart. (F.-D-Gk.) O.F. charte. 
SKT_dli_revised.txt:24746:work, from moles ^ heap, also effoit. So 
SKT_dli_revised.txt:25013:Energy. (F. — L. — Gk.) O. F'. e7i€rgie.
```


## [2026-10-17T00:03:57.214Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 32365,32372p KLN_1971.txt; sed -n 35193,35198p KLN_1971.txt; grep -n \"^organ, n\\|^work, n\\|^energy, n\\|^surgery, n\\|^ergon\\b\" KLN_1971.txt | head; sed -n 10257,10262p SKT_dli_revised.txt; sed -n 25013,25016p SKT_dli_revised.txt; grep -n \"^Organ\\.\\|^Work\\.\\|^Boulevard\\|^Surgeon\" SKT_dli_revised.txt"
}
```


### [2026-10-17T00:03:57.985Z] TOOL RESULT

```
boulevard, n. — F., earlier boloart , boulevert, 
balouart, belouart, orig. meaning ‘work of forti- 
fication’, fr. MDu. bolwerc . See bulwark, 
boulter, n., a long line for fishing, with hooks 
attached. — Of unknown origin, 
bounce, intr. and tr. v. — ME. bunsen . Cp. LG. 
bunsen, Du. bonzen , ‘to beat, thump’. Cp. also 
jounce. 
bulwark, n., 1) rampart; 2) protection. — ME. 
bulwerk, fr. MLG. (= Du.) bolwerk, which is rel. 
to MHG. bolwerk , G.Bollwerk, Swed. bolverk . 
These words lit. mean ‘bole work’. See bole, 
‘trunk of a tree’, and work and cp, boulevard. 
Derivative: bulwark, tr. v. 
11566:ergon and cp. energy. 
45571:ergon and cp. surgeon, which is a doublet of 
76294:ergon and words there referred to. The word 
82347:energy, n. — Late L. energia , fr. Gk. kvlpyzvx, 
84788:ergon, n., work (in terms of heat). — ModL., fr. 
168586:organ, n. — ME. organe , ‘a musical instrument’, 
172804:ergon and words there referred to. 
237552:surgery, n. — ME. surgerie, fr. OF. surgerie, con- 
268288:work, n. — ME. werk , work, fr. OE. were, wore, 
Bulwark. (Scand.) Dan. bulvcerk, 
Swed. bolverk (Ihre) ; cf. Du. bolwerk, G. 
boll-iverk (whence F. boulevard). Com- 
pounded of Dan. bul, Swed. bol, trunk of 
a tree, log, Icel. Imlr, bolr, the stem of a 
tree; and Dan. veerk, Swed. veidc, a work. 
Energy. (F. — L. — Gk.) O. F'. e7i€rgie. 

— Late 1^ energia.^- (ik. ivipy^ia, vigour, 
action — Gk. ipfpyos, at woik. — Gk. ip, 
31518:Work. 
53145:Work.^ mouth. 
77588:Surgeon, contracted foim of ehtrur^ ment. b. 111. c. 20 Eiom F. sttr, upon, in
```


## [2026-10-17T00:04:00.963Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 168586,168592p KLN_1971.txt; sed -n 268288,268296p KLN_1971.txt; sed -n 237552,237556p KLN_1971.txt; sed -n 84788,84792p KLN_1971.txt; awk 'BEGIN{RS=\"\\f\"} /work, n. — ME. werk/ {print \"KLN71 leaf\",NR-1}' KLN_1971.txt"
}
```


### [2026-10-17T00:04:01.466Z] TOOL RESULT

```
organ, n. — ME. organe , ‘a musical instrument’, 
fr. L. organum, fr. Gk. opyavov, ‘instrument; 
bodily organ; musical instrument’, which is rel. 
to 6pyta (for *F6pyia), ‘secret rites, orgies’, 
and in gradational relationship to £pyov (for 
*F£pyov ), ‘work’. See work and cp. orgy, ergon, 
energy. 
work, n. — ME. werk , work, fr. OE. were, wore, 
weorc , ‘work, act, action’, rel, to OS. OFris., 
Du. werk, ON. verk, Dan. vterk, Swed. verk, 
MDu. ware , weorc , were, OHG. werah, were , 
MHG. werch, were, G. Werk, Goth, gawaurki, 
‘work’, fr. I.-E. base *werg-, ‘work, to work’, 
whence also Avestic var e za, ‘work, activity’, 
v^r^zyeiti, ‘he works, does’, Toch. A wark, 
‘wicker work’, Arm. gore, ‘work’, Gk. £pyov 
surgery, n. — ME. surgerie, fr. OF. surgerie, con- 
tracted fr. serurgerie, cirurgerie, fr. Late L. chi- 
rurgia. See chirurgery. 
surgical, adj. — See surgeon and -krai. 

ergon, n., work (in terms of heat). — ModL., fr. 
Gk. Ipyov (dial, flpyov), ‘work’. See work and 
cp. erg. Cp. also allergy, alnrgite, anergy, argon, 
chirargeon, demiurge, dramaturge, dramaturgy, 
energumen, energy, ergasia, exergue, George, 
KLN71 leaf 0
```


## [2026-10-17T00:04:07.750Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==537+24+1' SYN.txt | head -60 | cut -c1-200"
}
```


### [2026-10-17T00:04:08.099Z] TOOL RESULT

```
al WGme. (and Dan. segl fr. MLG sekele) fr. Lat. secula ‘sickle’ (Varro), deriy. of secare ‘cut’. Walde-P. 2.475. Falk. Torp 953. KKluge-G. 561.
Sw. skdra, fr. vb. skdra ‘cut’? = NE shear, NHG scheren, etc. (9.22).
6. Lith. piautuvas, OLith. piuklas (now ‘saw’), OPruss. piuclan : piauti ‘cut, mow’ (8.32).
Lith. dalgis (> Lett. dial. dalgs, dal- gts), OPruss. doalgis : Ir. dlongim, MIr, dluigim ‘split’, ON telgja ‘whittle’, fr. *delgh- (*dlegh-), extension of *del- in Skt. dal- ‘split, burst’, etc. Wald
Lett. cirpa, through Esth. tsirp, fr. ORuss. strpit (ChSI. sriipti, above, 1). Leskien, Bildung d. Nom. 269. Thomsen, Beréringer 78. Walde-P. 2.582. Other- wise (fr. cirpt ‘shear’) Miihl.-Endz. 1.386.
Lett. sirpis, above, 1.
Lett. izkapts, fr. iz-kapat ‘hew, cut out’ ; Lith. iskapoti ‘chop’, ChSI. iskopi- ti ‘dig out’, epd. of kopati ‘dig’ (8.22). Mihl.-Endz. 1.748.
7. Ch&l. sritpi, etc., above, 1.
Slavic kosa (> Rum. coasd, NG xéca), prob. (with k fr. & by dissim.) : Skt. gas- ‘cut’, castra- ‘knife’, Lat. castrare ‘castrate’, etc. Meillet, Etudes 178. Walde-P. 1.448. Berneker 581.
8. Skt. datra-, fr. da- ‘mow’ (8.32).
Skt. srni-, above, 1.
Skt. lavitra-, above, 5 (ON /é, etc.).
SS ne ee ke ee ee
thresh’ are (apart from the f pains Som? se ‘ f ‘rub’, ‘beat’, or (rarely For ealied i different methods, ae (1) the rubbing with the hands (most primitive of all methods), extend- ed to the treading 
1, Grk. ahoaw, NG ddwvitw, derivs. of words for ‘threshing-floor’ (8.35).
Grk. rpiBw ‘rub’ (9.31), used for ‘thresh’ (by oxen) in Hom. Il. 20.496.
2, Lat. terere ‘rub’ (9.31) is the usual expression, But also, for certain proc- ih tundere ‘beat? and excutere ‘shake ut’,
Words for Grk. derivs. ©
It, tribbiare,
(rier) Sp. trillar, Rum. treera
ifr. Lat. tribulare ‘ ee: press, oppress’, aa tribulum ‘threshing-sled’ (in (above) a harrow), fr. root of terere Teta Pee, 1088. REW 8885 : Te, . b 7 ¢ , at. battuere ‘beat? aon bao
3, I rutey” do-fuairee (Wh, 10d6) lit. destig . S a to- fo- and org- ‘strike, Teysen, Gear. a3 2.250, 590. Thur-
igitized by Arya Samaj Foundation Chennai and eGangotri
AGRICULTURE, VEGETATION 509 8.34 THRESH , Lith. kulti Goth. Ariskan 1. pipe skja Lett. Kult ; anol? HP On eae, ChSl.  mlatiti, vrésti cist : Sw. ”  réska SCr.  mlatiti, vrijeci paler fribbiare OE jper
```


## [2026-10-17T00:04:11.076Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"WORK (sb\\|9.12 WORK\\|9.11 WORK\\|9.13 WORK\" SYN.txt | head; grep -n \"varaza\\|varoza\\|var\\?za-\" SYN.txt | head"
}
```


### [2026-10-17T00:04:11.383Z] TOOL RESULT

```
13593:9.12 WORK, LABOR, TOIL (sb.
13594:abstr.); WORK (sb. concr.)
13605:9.13 WORK, LABOR, TOIL (vb., intr.)
4425:8. Skt. varaha-, Av. varaza- (but both only ‘wild boar’) etym.?
24747:Ay. xsviwra-, cf. xéviwi-vaza- ‘going swiftly’, zsvatwayat- astra- ‘swinging the whip swiftly’, prob. : ON svipa ‘swoop, move quickly, whip’, ete. Cf. OB swift fr. a parallel root (above, 5). Barth. 561, IF 9.274f. Walde-P. 1.241.
27871:16.22 JOY apt Goth. fahéps Lith. dziaugsmas, links- xapt ON gledi, fagnadr mybe gaudium, laelitia Dan. glade, fryd Lett. prieks, liksma gioia Sw. glidje, fréjd ChSl. radostt joie OE geféa, blips, glednes, SCr. __radost alegria, gozo wynn Boh.  radost . veselte, bucurie ME blisse, tote, gladnes, Pol. radosé faille, sube, Githes wunne Russ. _radost’ athas, liithghair NE joy Skt. dnanda-, harsa-, lawenydd, dywenydd Du. vreugde mayas- levenez, joa OHG  gifeho, frewi, frewida, Av. mayd-, $dili-, urvaza- mendi, wunna MHG vréude, mende NHG freude
32879:OPers. vardana- prob. : Av. varazana- ‘community, state, common people’, Skt. vrjana- ‘inclosure, settlement’, etc., fr. the root in Av. varaz- ‘shut off’, Grk. elpyw ‘shut in (out)’, etc. Walde-P. 1.290. Barth. 1424f. But the OPers. word could also correspond to Skt. vardhana- in town-names like Pundra- vardhana-. R. A. Hall, Jr., Language 12.297 ff. (suggesting deriv. fr. the root of OE wardén ‘watch over, protect’). Still otherwise on Skt. vardhana- (as loanword fr. OPers.) Wackernagel-De- brunner) KZ 67.168 f.
```


## [2026-10-17T00:04:13.920Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 13593,13640p SYN.txt | grep -n -i \"werg\\|ergon\\|varz\\|var.z\\|Werk\\|537\\|538\" | cut -c1-400"
}
```


### [2026-10-17T00:04:14.211Z] TOOL RESULT

```
5:tpyacla, wévos; Ep'yor Sovderd, Epyacia; Epyo (opus) opera, labor; opus lavoro; opera travail; euvre, ouvrage trabajo; obra lucru, muncd; operd sdelhar, opair, lubair; opair obair, saothar; obatr gwaith, lafur; gwaith labour; ober . arbaips; waurstw verk, vinna, erfidi; verk arbejde; verk arbete; verk weorc, swinc; weorc worke, swinke, labour; worke work, labor, toil; work werk, arbeid
6:OHG  wer(a)h, arabeit; wer(a)h MHG were, arbeit ; werc NHG arbeit; werk;
12:Av. varaz-: Grk. épiw, epyov, etc., above, 2.
21:wyrcan, swincan worcke, swinke, laboure work, labor, toil werken, arbeiden wirken, arabeiten wirken, arbeiten arbeiten
28:varaz-
41:1. From IE *werg- in Grk. épiw, pétw ‘do’, Av. varaz- ‘work, do’, etc. (9.11). Walde-P. 1.290 ff. Feist 555, 556.
```


## [2026-10-17T00:04:20.812Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==300' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i \"werg\\|uerg\\|varz\\|var.z\\|έργον\\|spyov\\|organ\\|Werk\" | head; awk 'BEGIN{RS=\"\\f\"} NR==299' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i \"werg\\|uerg\\|varz\\|var.z\\|organ\\|Werk\" | head; grep -n \"^werg-\\|^uerg-\\|^werĝ\" IEC.txt | head"
}
```


### [2026-10-17T00:04:21.196Z] TOOL RESULT

```
67:seits Zugehorigkeit zu *uerg- „drehen, winden                    ,
80:die Weberei wie dgyd£a>, Trig wirken auf die Biickerei), s. Kluge u. Werg.
88:Marstrander IF. 22, 332 f. (der Werg und wirken ,.weben -< der YVz. *uerg-
94:dt. Werg erinnert cymr. cy-warch „Hanf, Flaclis"       bret. koarh   =abret. co-                ,
6:290                                     ue:g-. m’ e g-   uerg-
55:dazu air. frui<i ..Wand”, nir. fraiyh ..Wand aus Flechtwerk, Dach, Fliirde
76:2   uerg- ..wirken. tun -.
81:   Av. vara.- ivarazyeiti — got. wcidrlcelp: s. auch gr. gtfm) wirken, tun,
86:varz:, barz ..Feldarbeit. Ackerbau”). cur'd/- f. ..Handeln, Tun”, v nrltva-
87:Adj. ..was zu tun isf. Arm. yore ..Werk" (* uoryo -: Hiibschmann Arm.
88:Gr. I 439;. Gr. toy or, v-tgyor ..Werk, Arbeit" = dt. Werk), toydfo/iai
```


## [2026-10-17T00:04:24.997Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^u\\?wer[gĝǵ]\\|^uerg\\|^werg\" IEC.txt | head; grep -n -i \"'work'\\|“work”\\|\\\"work\\\"\" IEC.txt | head -8; grep -n \"ورز\\|برز\" incoming/ARY/ARY_pages.txt | head -8; grep -n \"VARZ\\|BARZ\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:04:25.377Z] TOOL RESULT

```
20039:uergho, io (1) “annoy, plague, torture’. Cf. uorgh- Skt. cf. upa-valhami, v. & válhe, mp. ‘quizz’; Ir. feargaim, v. "be angry” (here?); MHG wér- gen, sv. 3. ‘strangle’ beside (o-gde) wergen, wv. ('téar', fr. *uorghejo); Li. vérgiu, ti, v. *en- slave’. Nominal types: Ir. fearg, f. (anger. Here?); Li. vérgas, m., vérge, f. ‘slave’; Latv. vérgs, m. id.
20040:uergho (2) (?) ‘come, go’ Gk. érkhomai, v. ‘come’; Lat. (?) vergo, ére, v. ‘incline’
20041:uergo, io (1) “tie, twist, squeeze, strain,
20068:uergh-, uergh- — uéros
112:کشاورزی و اهل‌سازی دام‌ها نو آوری شد و این نوآوری‌ها شهرزیستی و ازدیاد جمعیت و ایجاد
162:دارای ارابه و اسب پودند» تحرکك آنها از کشاورزان روستانشین بیشتر بود و در ناحیه‌ی وسیع‌تری
290:کشاورزی شده است. چون واژه‌های «اسب» و «ارابه؛ و «چرخ» در اکثر زبانهای هند و اروپایی
294:«شخم» و «آهن) و «جوه و «گاوه و «بز» و «خوکک» نشان می‌دهد که این مردم به کشاورزی هم اشتغال"
954:رزمی ۳_کشاورزی و بازرگانی. این انگارگان سه گانه پس از انشعاب هند و اروپائیان به زبانها د .,
960:هسر بدست آورد و بدینوسیله موجب ازدیاد جمعیت و رونق کشاورزی و بازرگانی شد. :
965:( کشاورزان و شبانان و سوداگران) وجود داشتند که نقش اجتماعی آنها با الگوی سه گانه‌ی فوق
1081:نظامی غیر متحمل است. ظاهراً در جامعه‌ی هند و اروپائیان هر مرد هم کشاورز یا شبان بود وهم .۱
298:BARZ (guy! BHURIA 4 Sle (e0lé1 uw 8) BHERGO colyy I y 22 Gofly Se
3411:FOIA gens antic BARBARZYNCA (POLISH) gt)
15170:VERK (SWEDISH) (58 yo VARZ, VARZISHN, WARZIDAN
15193:VOL (4LE}(SERBIAN) 0 VARZA, WARZAG PAHLAVI) 5 Jha,
```


## [2026-10-17T00:04:31.640Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"VARZ\\|WARZ\\|ERGON\\|ORGAN\" incoming/ARY/ARY_latin_index_pages.txt | head -20; awk 'BEGIN{RS=\"\\f\"} /VERK \\(SWEDISH\\)/ {print \"leaf\", NR-1}' incoming/ARY/ARY_latin_index_pages.txt; grep -n \"\\[pdf page\" incoming/ARY/ARY_latin_index_pages.txt | awk -F: '$1<15170' | tail -1"
}
```


### [2026-10-17T00:04:32.054Z] TOOL RESULT

```
3081:‘WARZA «(OLD SCANDINAVIAN), AS Ele!
3082:WARZE (GERMAN) glalT VARTA
7138:vay sebi iby SWARZ.
15170:VERK (SWEDISH) (58 yo VARZ, VARZISHN, WARZIDAN
15172:‘WERK (DUTCH) gia WARZISH «AFGHANI) (5%) elit
15175:ERGON, ERDO GREEK) oli
15180:(WORK) 140, (WARZ-) 88 OLD SAXON) pS ip S te
15193:VOL (4LE}(SERBIAN) 0 VARZA, WARZAG PAHLAVI) 5 Jha,
leaf 518
15161:[pdf page 519]
```


## [2026-10-17T00:04:37.410Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 15161,15200p incoming/ARY/ARY_latin_index_pages.txt | cut -c1-200"
}
```


### [2026-10-17T00:04:37.826Z] TOOL RESULT

```
[pdf page 519]
gins Oka iesas | Ov
TYPO: YYOV.YYFA T@budlay REFERENCES beh
FAVA FANT A AMA fgg Baa POKORNY: 113
8, J rror lasts aaa
ne
WEORC (OLD ENGLISH) oS gosSl AVESTAN) gles)
WORK ENGLISH) gJS3\ VAREZA, VaRQZYEITI
VARK DANISH) Sylails—- :(PAHLAV]) § ap
VERK (SWEDISH) (58 yo VARZ, VARZISHN, WARZIDAN
VERK (NORWEGIAN) $395 WERZA, WERZ (KURDISH) 535
‘WERK (DUTCH) gia WARZISH «AFGHANI) (5%) elit
OLD IRISH) S54) 2! WARK H(TOKHARIAN A) A 5,88
OPAIR, FAIRGED GORC ARMENIAN) 2)
ERGON, ERDO GREEK) oli
REFERENCES eth GOTHIC) $38
POKORNY. ~~~S~S*~*«SdGALTIOVN WAURSTW, WAURKJAN
BARNHART: (WORK) 1244 OLD SCANDINAVIAN) 4S 54a!
‘MACKENZIE: VERK, YAKJA, VERKA
(WORK) 140, (WARZ-) 88 OLD SAXON) pS ip S te
BUCK: 539.542, 537 WERK, WIRKIAN
ONIONS: (WORK) 1012 HOLD FRISIAN) S523
SKEAT: (WORK) 732 WERK, WERKIA
TYPA 9 OF tebU day (OLD HIGH GERMAN) aS gli
TTY g PIF. Hashas eal cid WERAH, WERC, WIRCHEN
WERK, WIRKEN (GERMAN) gal
deadloal
apts oe po Sina) “shoe 2 Sid ea olds 2 zl tN
Cad Sy CS get ge WERE 528 9 gi 9 uss 3 IF 252,545 22 139 al eV
—
[pdf page 520]
ONT C5 IS" 6 4) shas ding
VOL (4LE}(SERBIAN) 0 VARZA, WARZAG PAHLAVI) 5 Jha,
VOL (4L¢}(BOHEMIAN) gun y WERSA KURDISH) 53,5
VERSHIS (LITHUANIAN) (gy VASA, VRSABHA (SANSKRIT) cy Sil.
VERSIS LATVIAN) (3) gs VACCA LATIN) 553
VACHE FRENCH) Wit
REFERENCES bethany VACA SPANISH) glityal
POKORNY VACCA AUTALIAN) «gly!
BARNHART: (VACCINE) 1191 VACA (RUMANIAN) gly,
```


## [2026-10-17T00:04:49.506Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 15200,15230p incoming/ARY/ARY_latin_index_pages.txt | cut -c1-200; awk 'BEGIN{RS=\"\\f\"} NR==521' incoming/ARY/ARY_pages.txt | head -30"
}
```


### [2026-10-17T00:04:49.877Z] TOOL RESULT

```
BARNHART: (VACCINE) 1191 VACA (RUMANIAN) gly,
DELAMARRE: (VACHE) 139 VACA PORTUGUESE) i »
MACKENZIE: HOLD CHURCH SLAVIC) pS «5391
(PLOUGHING OX) 127 vod (4)
BUCK: (OX) 152-155 WoL (AyLEX(POLISH) legs
rret_rry. iebGoby VoL (AEYRUSSIAN) 55,
WEWARE |. :(OLD PRUSSIAN) iS gos 9 VIVERRA . A(LATIN) 3
GWIWER WELSH) 5 3 “WEORNA (OLD ENGLISH) yf nd i
GWIBER BRETON) 35» NEVERICA ARUSSIAN) gy ae ney
VEVERKA sy, tezECH Se "
‘REFERENCES botky VERVERIKA ‘ *\ (BULGARIAN) ¢ js,
POKORNY. «1166 LITHUANIAN) «gi ys} ;
DELAMARRE: (ECUREIL) 138 VAIVERE, VOVERE
rrivy Mass aabicaid LATVIAN) (3) 66.95
VAVERE, VAVERIS
[pdf page 521]
vty warns | OY
Edad VAGA (SWEDISH) 54 y+ AVESTAN) gl 3)
VEIE NORWEGIAN) 153343 VAZ-, VAZAITI, VAZAH-
WEGEN (DUTCH) che VAZITAN, WAYIDAN :(PAHLAVI) 5}
OLD CHURCH SLAVIC) 345 5 %<1 VEZIN KURDISH) 52,5
VEZO, VESTI VATAL (AFGHANI) (4) gill
(LITHUANIAN) ¢\ ¢3 (SANSKRIT) <4 Sike
YVEZBU, VEZO, VEZHTI YAH, VAHATI, VAHAYATI
FEN HOLD IRISH) 45 5-4) 2 WEKHTO, OCHEIN (GREEK) gli»
vJZBU ALBANIAN) gis XLATIN) 3
VEHO, VEHERE, VEHICULUM
‘REFERENCES beh, GAWIGAN GOTHIC) 53
POKORNY SS*S~*«wTBLTD {OLD SCANDINAVIAN) 45.521!
BARNHART: (WEIGH) 1226 VEGA
DELAMARRE:(ALLER WEGAN — (OLD SAXON) pS gS
[pdf page 521]
۲ /_ورزیدن, وزش
۱
اوستایی (1ل47787۸): سوئدی (7ل81780/8): 0
-7ل۸ ۷۸2 ,۷۸2۸13 ,۷۸2۳ نروژی (088014/۷/): ۷۱8
پهلوی (1ماتلم۳): ۷۷۸310۸ ,۷۸277۸۷ هلندی (7لع07ا0): ۰ را یدنا(
کردی (8.0157م): ۷2 اسلاوی کهن (۲70ما5 64ات0 صز0):
اففانی (پشتر) (/۸۳07۸(۷): ۷۸۲۸ 71 ,۷820
سانسگریت (84/9707): لیتوانی (لفاههلآ 7
1 ۷21۸7 +اق۷۸ 41 ۷۳20 نا ۷۴23
بونانی (028۸): ۰ 0671818 ,۷۷8710 ایرلندی کهن (4دلغ[ صاه): ان ۱
لاتین (7100ا): آلبانی (فالمقتم). ۷
۷8۲10۲-۸ ,۷۳۳5۳ ,۷۸۵
گرتیکد (007[470): 0۸/10۸2 پسگشت‌ها 22505
ایسلندی کهن (/01۸72ای5 صزمم: 9 ور
۷0۸ 6 8165 ی ام ادن
ساکسونی کهن (/54:0 2ا0): 1۲86۸۲ آخ) عمجم هنم 02
فریزی کهن (۷فاکلة۲ 012): ۲۷51۸ ,1۷20۸ 1 (031۸3 571
آلمانی کهن (4۸ل027 بزهزبز ها): 4 (810۷ داد هام
ندانت دی 8 ۲۲۴167 :010075
آلمانی ((0273(/4): ۷۷۸688 ,3۳/503 0 (۲۷۳6) :7
انگلیسی کهن (نتولن2۸/0 صا۵): ۱80۸0۷ 1۲80719 :مه #3متتمهر
انگلیسی (8(701/5[4): ان درا برهان قاطع : ۳۳۷۹
دانمارکی (0۸13/1): زدیا
یادداشت:
چم این واژه در زبان‌های سانسکریت و لیتوانی: حمل کردن؛ بردن» کشیدن.
چم این واژه در زبان افغانی: پریدن.
چم این واژه در زبان ایرلندی کهن: ارایه» وسیله‌ی ترابری,
چم این واژه در زبان ژرمنی: تکان خوردن؛ جنبیدن» وزن کردن.
33333333
```


## [2026-10-17T00:04:56.143Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/ورزا' --note 'page 549 Werg 1: varzâ ox'; f=$(python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/ورزا' --note x | tail -1); grep -A3 \"Etymology\" $f | head -12"
}
```


### [2026-10-17T00:04:57.374Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/edabed02f2535828.txt
 Etymology 

 2.3 
 Noun 
--
 Etymology
 [ edit ] 

 From ورز ( varz ) +‎ گاو ( gâv ) , literally “ tilling-cow ” .
```


## [2026-10-17T00:05:01.793Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for f in AFM.txt FVQ.txt LKT.txt AFA.txt PLA.txt DOZ.txt; do [ -f $f ] && { echo \"== $f\"; grep -n -i \"ارغن\\|arghan\\|argan[uū]n\\|urghun\\|organon\\|ὄργανον\\|opyavov\\|orgel\\|Orgel\" $f | head -5 | cut -c1-300; }; done"
}
```


### [2026-10-17T00:05:02.387Z] TOOL RESULT

```
== AFM.txt
== FVQ.txt
== LKT.txt
== AFA.txt
== DOZ.txt
```


## [2026-10-17T00:05:06.404Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"رغن\\|رغنون\\|ارغون\" AFM.txt AFM_alt.txt AFM_pages.txt 2>/dev/null | head -5 | cut -c1-300; grep -n -i \"organ\" AFA.txt LKT.txt | head -5 | cut -c1-300; command ls ../refs_online.json 2>/dev/null; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json'));print({k:d[k].get('local_file') for k in ['PLA','AFM','FVQ'] if k in d})\""
}
```


### [2026-10-17T00:05:06.780Z] TOOL RESULT

```
LKT.txt:632:'Fahne',  mit  pers.  Endung  bairakdar 'Fahnenträger';  hieraus  rum.  bairac 'Fahne',  6aiV«cc?ar 'Fahnenträger'.  Eben- so bulg.  bajrak,  serb.  barjak  'Fahne'. Bei  den  Räuberorganisationen  auf  dem Balkan  ist  der  Bairaktar  derjenige  Ober- räuber, der  die  Kasse  führt  und
LKT.txt:2114:'Gott'  [Horn  NpEt  S.  104,  Nr.  471],  da- von demin.  nach  der  ar.  Form  fu'ail [vgl.  Hasan  >  Husain  hier  Nr.  835] hudaiw  'kleiner  Gott',  vulg.  Aussprache hedlw,  die  frühere  Bezeichnung  des Vizekönigs  von  Ägypten,  der  sich  jetzt wieder  sultän  'Herrscher'  od
LKT.txt:2298:961.  Tk.  jorgan:
LKT.txt:2299:Decke';  hieraus  bulg.  jurgan  'dass.', rum.  iorgan  'Bett-  oder  Steppdecke', iorgangiü  'Polsterer'.
LKT.txt:3264:'Koralle'  [aus  gr.  laapTapiTr^q  ZDMG  LI, 304],  tk.  mergan  'dass.';  hieraus  rura. märgean,  mnrgicä;  bulg.  merdzan  'Ko- ralle'. Mit  ar.  Art.  und  Imäla  [ä  >  e] «rgab  sich  der  alte  pharmazeutische Ausdruck  frz.  almargen:  poudre  d^al- margen  'gepulverte  iiorall
../refs_online.json
{'PLA': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'], 'AFM': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt'], 'FVQ': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt']}
```


## [2026-10-17T00:05:11.909Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for l in 314 315 316 317 318 319; do awk -v n=$l 'BEGIN{RS=\"\\f\"} NR==n+1' data/verification/sources/refs/BQT_v1_pages.txt | grep -n \"ارغن\\|organ\\|organon\\|0۲841\\|یونانی\" | head -5 | sed \"s/^/leaf $l: /\"; done; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/أرغن' --note 'page 549 Werg 1: Arabic urghun organ'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/أرغنون' --note 'page 549 Werg 1: Arabic arghanun'"
}
```


### [2026-10-17T00:05:13.314Z] TOOL RESULT

```
Exit code 1
leaf 317: 9:ارغنون » نام حکیمی است زوه‌ی و او اعل‌وافضل
leaf 318: 27:۱ 0 : ارغنون .
leaf 318: 35:و رومیان نوازند . و ارغنون همان است .
leaf 318: 43:است ؛ و بعضی گویند ارغنده آب است وارغنده
leaf 318: 46:ارغنفه ۲ » بر وزن‌شرمنده » بمعنی
leaf 318: 54:ارغنون است . و آن سازی باشد که رومیان
leaf 319: 3:ی گونند .ارغنون
leaf 319: 8:آدمی از پبر و جوان ارغنون باریری ۷
leaf 319: 16:ارغنون دستی مك چیز را بیکبار و (۲)
leaf 319: 31:وتیز را کوند ۴ ,- و مخفف ارغنون هم هست
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c0c491397610d2de.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/51804211e9bed065.txt
```


## [2026-10-17T00:05:19.493Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; awk 'BEGIN{RS=\"\\f\"} NR==320' refs/BQT_v1_pages.txt | sed -n 1,60p; for f in c0c491397610d2de 51804211e9bed065; do sed -n 3p web/$f.txt; grep -A3 -m1 \"^ Etymology$\" web/$f.txt; done"
}
```


### [2026-10-17T00:05:19.885Z] TOOL RESULT

```
Exit code 1
سس سا
مشهور که افلاطون وضع (۱) کرده است ؛» و
ی گونند .ارغنون
ترجبة مزامیر است
بعنی جمیم ساز های
»؛ وبسنی دیگر
کرنند چرن هزار
آدمی از پبر و جوان ارغنون باریری ۷
همه پیکبار بآراز های مخالفبکدیگر چیزی
بخواد هد آن حات را
ارعنون خوانند » و
جمعی دمگر گفته اند
که ارغتون ساز وآواز
هفتاد دختر خواننده
و ماژنده است که همه
ارغنون دستی مك چیز را بیکبار و (۲)
پيك‌آهنگه باهم بخوانند و بنواژند .
ارغوان ی رت
پهلوان ۰ ممروف است و آن
بهار درختی باشد بفایت سرخ
ورنگین؛ طبیعت آن‌سرد وخشك
است اگراز بهارآن (۳) شربتی
ساژند و بخورند رفم خمار کند
و چوب آنرا بوزانند (4) ی
ابرو مالند » سیاه برآبد ومعرب
آن ارجوان ۴ است ؟ .
)۱ چش : آن .
)4( خم۳ : سوزند .
اراد
ادغون » بر وزن کردون » اسب تند
وتیز را کوند ۴ ,- و مخفف ارغنون هم هست
که ماز ممروف باشد ۵ . ۱
ارغیده « بر وزن غمدیده . ناه
وخشم آلود را کونند ۱ .
ار ان » با قاف بر وزن درمان . بلفت
رومی ۷ حنایی باشد که بر دست و پا بندند .
خوردن نیم متقال از آن قولشج را بکشابد .
گوند چون طفلی را ایدای ابله ی آوردن
باشد فدري ب رکف بای او صالند ایمن بود از
آنکه از (4) چشم او برآید » و باین معتی‌بجای
نون قاف هم بنظر آمده است - و بلفت فرب
الافصی نوعی از بادام کوهی است که آنرا
لوزالبربر کونند و روغن آنرا زیت الهرجان
خوانند .
ار قش بکسر قاف بر وزن ورزش »
بمعنی فهیده و کار دان باشد » و درجای دیگر
بجای فانی فای مقتوح ( ٩‏ ) نوشنه بودند بمعنی
ار لك - بفتح اول و سکون ثالی و کاف
فارسی قلمة کوچکی باشد که در مبان فلمبزر که
لاف وم زیت بو علایت مساق -
و بزبان علمی اهل ند اسمی است از اسامی نیر
اعنلم کهآ فتاب باشد - و بفتح اول وانی‌رسمانی
«باشد که کاهی بر درخت آویزند و برآن‌نشینند
"و در هوا آیند و روند و کاهی بر پای اسب
۳( خم ۳ : آن بهار.
)٩(‏ خم ۳ : سعنس .
؟ ‏ رك : این درد .
۴ ی ره ؛ توروزنامه ص ۳ ۱۱۱ -
* ای ۱۷۰ * .
بفه درصفحةٌ ۱۰۸
STATUS: 200
STATUS: -1
```


## [2026-10-17T00:05:23.561Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; awk 'BEGIN{RS=\"\\f\"} NR==319' refs/BQT_v1_pages.txt | sed -n 25,80p; grep -A4 -m1 \"^ Etymology$\" web/c0c491397610d2de.txt"
}
```


### [2026-10-17T00:05:24.060Z] TOOL RESULT

```
آرغامونی
(۱) خم ۳: + به.
۱ 0 : ارغنون .
وت
دستها را برهم زلنث .
ار غلك » بفتح اول و الث وسکون‌انی
و کاف » گیاهی است که بردرخت ییچد و بربی
عشفه گوند .
ادغی " » بر وزن ارزن » نام‌سازست
که آن را افلاطون وضع کرده و خر اسرانبان
و رومیان نوازند . و ارغنون همان است .
او خن " - بر وزن فرزند » بمعنی
خسم افنکن و دلیر و شجاع باشد - و خشمکن
را نیز گویند .
ار غنداب نام رودخانه ات که
مابین عراق و آذربایجان کذرد - و تام رورخانة
قندهار هم هست؛ و معنی ترکیبی آن خشمگین
آب بافد : چه ارفتد بمعنی خشمگین عم آمده
است ؛ و بعضی گویند ارغنده آب است وارغنده
نیز بحعنی خشمگین باشد وها بکثرت استعمال
افاده است .
ارغنفه ۲ » بر وزن‌شرمنده » بمعنی
حرص و خداوند شره.باشد - و مسثی را نیز
گوبند که طالب و حرص‌شراب‌باشد - وبمعنی
قهر آلود و غنبناك هم آمده است .
ار نگ - بر وزن وممنی ارژنگ‌است
که نکارخانةٌ مانی نقاش باشد .
ادغنی ؟ « بنتح اول و سکون ثانی
واكك مفتوح و رابع مضموم بنون زده , عخفف
ارغنون است . و آن سازی باشد که رومیان
نوازند و افلاطون واضم ( ۳
ارغنون ۴ بی وژن آندرون » سازیست
۴ - از بوانی ۳92900 .
۴ رك : ارغنون.
```


## [2026-10-17T00:05:26.969Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; grep -i -m5 \"from\\|borrowed\" web/c0c491397610d2de.txt | cut -c1-400"
}
```


### [2026-10-17T00:05:27.392Z] TOOL RESULT

```
 From Wiktionary, the free dictionary
 Likely from English organ .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=أرغن&oldid=91378388 "
 Arabic terms derived from English
```


## [2026-10-17T00:05:34.328Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^varz\\|^warz\\|varzītan\\|varzitan\" NYB_vol2_glossary.txt NYB.txt | head -8; awk 'BEGIN{RS=\"\\f\"} /warzidan, warz-/ {print \"PHDleaf\",NR-1}' PHD.txt"
}
```


### [2026-10-17T00:05:34.799Z] TOOL RESULT

```
NYB_vol2_glossary.txt:1393:var(e)št (Mx), corresponding to Phl *duš- varšt; from varz-, v. varzitan.
NYB_vol2_glossary.txt:1477:ēvarz ['dwlc'] review, muster, as a mili- tary term: ~ kartan to review, to muster (an. army) 2014; — [hence ēvarzīk kas probably *a man called up for military service, DkM 750!?]. — Originally ‘com- putation, calculation, account’, ef the following examples: ~ 4 x“atdydn 6 osti- kan the rulers’ calling of their trustees to account DkM 40416; étar *zarvan i (K drang) àivan (< K) andak, ~ züt; änöd dātavār (!) rāst here (in this world) the term of the court is short, and the account swift; there (in heaven) is & righteous *judgment DkM 5481-11; apar hān 4 andar nihvārēh ~ about the items (necessary) in combat FrP 14, heading. In all probability to be connected with NP dvàr(ah) ‘calculation, reckoning; an account-book’ (of which dvārjah, dvarcah ‘a cash-book, a book of receipts and dis- boursments, a diary, or register’ is the diminutive) < *abi-varda- SW form of *abi-varza-; dvdr : ēvarz, cf ēvāc, Evar, évar. (Wrong interpretation by Nyberg, TMK 69 sq., Pagliaro, Iscr. Dura-Europo 592. 595). — From varz-, v. varz, varzitan.
NYB_vol2_glossary.txt:1576:frazand [prznd; inser. plend], fradand [prdnd] child: 1. frazand 6522-25, 661"; with the indef. art. —-e [~ + 1] 86%; ~ varzitan to produce children 67%; pl. cas. rect. ~ 963, 9726, 10514; pl. cas. obl. ~-dn 6913, ~-in [plendyn] F:5. — 2. fra- dand 16, 1013-18, 1119.11.24, 123.12.21.25. 1526 (after numeral). 1676; pl. cas. obl. —-ān 210, 37186 99, 12% 1423-5, [51% 2217, = Av. (1004 sq.) frazanti- ; MPrthPrs frzynd, MPrs also przynd; Ps. plendy; Paz. far- zand frazand; NP farzand. — fradand is the authentic SW form, preserved as an orthographical archaism, and listed in FrP ll with the gl. frazand ; the first -d- of fradand is not a dwarfed z, which only occurs in ideograms, and in the inscript- ions has a form wholly different from d.
NYB_vol2_glossary.txt:2089:"huvaršt [hwwlšt'] what is well done, good deeds, the third and last station preced- ing Paradise 632%. 7316-27, 8916, 1209, cf humat and hūxt. — Borrowed from Av. (1850) hvarsta-, ci varzitan.
NYB_vol2_glossary.txt:2094:hu-varziha [hwwlcyh’] adv. in a state of good working, or: of working good things 6415, — V. varzitan.
NYB_vol2_glossary.txt:3994:varzč-kar [wlcykl] farmer 1478.17, 1519.27,
NYB_vol2_glossary.txt:3995:varzišn [wlešn'] the act of performing: ~ + uučškareh 63°.
NYB_vol2_glossary.txt:3996:varzišnčh det. v. n.: yumč ~ 431, v. yume.
PHDleaf 113
```


## [2026-10-17T00:05:38.109Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3985,3994p NYB_vol2_glossary.txt | cut -c1-700; awk 'BEGIN{RS=\"\\f\"} /varzč-kar/ {print \"NYBleaf\",NR-1}' NYB_vol2_glossary.txt"
}
```


### [2026-10-17T00:05:38.584Z] TOOL RESULT

```
vartčnišn [wltynän'] transformation
9921.25 v, n. of
varténitan to change, to alter, to trans- form 7625. 7779.26.27 782.4, 791.3, — Caus. of vart-, v. vastan; Paz. vardinidan.
vartišn [wltšn'] the act of turning: 1. han i avdom ~ the last turn, of the end of the world and the fraškart (q. v.) 4619; ~ 4 axtarün u gartišn 4 spahr the revolu- tion of the fixed stars and the rotation of the sphere 1205-5; ~ u gartišn + muhrak the moving and transposing of the draughtsmen 12015, — 2. pred.: turned, became 41??, — V. vastan.
204
vas
vartišnēh det. v. n.: hac tan bod bē ~ the departure of the consciousness from the. body (= death) 642°.
iyarz [wle'] farming: ~ u āpātānēh farming and cultivation 6322. 8114. 90%; ~ 4 kirpak cultivation of virtue 66°. — Av. (1378) varaza-; MPrs wrz ‘farming’ (A-H II); NP varz ‘a sown field, agri- culture’, but also ‘gain, profit’, cf Arm. lw. varj ‘salary’.
2varz [wlz] mace 311, 9621, 100%. — < vazr with metathesis, v. this w.; NP gurz.
varzč-kar [wlcykl] farmer 1478.17, 1519.27,
NYBleaf 222
```


## [2026-10-17T00:06:08.059Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; grep -c -i \"arghan\\|arγan\\|argan[uū]n\\|organon\" refs/HRN.txt refs/HUB.txt; grep -c -i \"bulvar\\|bolvar\\|boulevard\" refs/HRN.txt refs/HUB.txt refs/LKT.txt refs/SKT_dli_revised.txt; grep -n -m2 \"^Boulevard\\|Boulevard\\. \" refs/SKT_dli_revised.txt | cut -c1-300; grep -n -m2 \"^Organ\\. \\|^Organ \" refs/SKT_dli_revised.txt | cut -c1-300; sed -n 31518,31524p refs/SKT_dli_revised.txt; grep -v \"^\\s*$\" web/86258942d1ebd8aa.txt | grep -m3 \"ورزیدن\" -A2 | cut -c1-200"
}
```


### [2026-10-17T00:06:08.572Z] TOOL RESULT

```
refs/HUB.txt:0
refs/HRN.txt:0
refs/HUB.txt:0
refs/HRN.txt:0
refs/LKT.txt:0
refs/SKT_dli_revised.txt:1
Work. 

Geranium, a plant. (L.~Gk.) L. 
geranium, Latinised from Gk. ycpdviov, a 
geranium or crane’s bill (from the shape 
of the seed-pod). — Gk. ylpavos, a crane; 
allied to Crane. 
URL: https://vajehyab.com/moein/ورزیدن
FETCHED: 2026-10-17T00:03:27Z
STATUS: 200
TITLE: معنی ورزیدن | فرهنگ انتشارات معین | واژه یاب
معنی ورزیدن | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد +
```


## [2026-10-17T00:06:17.477Z] TOOL CALL #59: Bash

```json
{
 "command": "command ls -la /home/sfmqrb/git/rishe-private/site/pages/549.jpg"
}
```


### [2026-10-17T00:06:17.827Z] TOOL RESULT

```
-rw-r--r-- 1 sfmqrb sfmqrb 69246 Oct 14 22:15 /home/sfmqrb/git/rishe-private/site/pages/549.jpg
```


## [2026-10-17T00:06:19.632Z] TOOL CALL #60: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/549.jpg"
}
```


### [2026-10-17T00:06:19.739Z] TOOL RESULT

```

```


## [2026-10-17T00:08:51.807Z] TOOL CALL #61: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-549.json",
 "content": "{\n  \"pdf_page\": 549,\n  \"book_page\": 519,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-16\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Werg 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *werǵ- 'to work, do' (Pokorny 1168-1169 2. u̯erĝ- 'wirken, tun'; WP I 290 f.; Watkins werg-; thematic noun *wérǵom 'work')\",\n      \"note\": \"Root, label and gloss are correct. Pokorny 1168 groups exactly Nourai's material: Av. varəz- / varəza- 'work' (with 'npers. varz, barz Feldarbeit, Ackerbau'), Gk. érgon, órganon, Germanic *werka- (OE weorc, OHG werc). Watkins (AHD) lists work, bulwark, (boulevard), ergon (allergy, argon, energy, metallurgy, surgery, georgic) and organ/organon under werg-. Cheung 2007 (*u̯arz 'to do, work, till the land') notes NP varzidan and barz are not regular SW Persian forms (inherited SW Persian has d < PIr *ź, as in OP vard-); they come from a NW Iranian (Parthian-type) source. Weak spots on the chart: the gloss 'strong cow' for varzāv (it is the plough-ox), the label 'Middle German' for bolwerk (the French word comes from Middle Dutch, or possibly Middle High German, bolwerc), and the claim that argon and allergy came through French (they are modern coinages from Greek). The extraction matches the printed page (checked against site/pages/549.jpg). The page also has an empty, unlabelled box to the right of the Old Persian node that the JSON leaves out; it holds no word.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *werǵ- «کار کردن، انجام دادن» در پوکورنی (ص ۱۱۶۸-۱۱۶۹)، والده-پوکورنی (ج ۱، ص ۲۹۰) و واتکینز آمده است. اوستایی varəz- و varəza- «کار»، یونانی érgon و órganon، ژرمنی *werka- (انگلیسی work) و فارسی «ورز، برز، ورزیدن» از همین ریشه‌اند. پس ریشه و معنایی که نورایی داده درست است. نکتهٔ مهم آن است که «ورز» و «ورزیدن» با z گونهٔ شمال‌غربی (پارتی) است. گونهٔ بومی جنوب‌غربی باید d می‌داشت، چنان‌که در پارسی باستان vard- دیده می‌شود. معنای «گاو نیرومند» برای «ورزاو» هم دقیق نیست و معنای درست آن «گاو شخم» است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wérǵom\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wr̥jyáti\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1168\", \"status\": \"supports\", \"note\": \"POK_full.txt lemma block ending 'Page(s): 1168-1169' (lines ~91150-91215): 'Avestan ... varaza- m. work, Verrichten ... (npers. varz, barz Feldarbeit, Ackerbau) ... gr. ergon, Fergon work (= German Werk) ... organon tool ... Old English weorc ... Old High German werc'. The root, gloss and the Avestan, Persian, Greek and Germanic reflexes are all there.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 290 (WLD_Bd1_pages.txt leaf 299)\", \"stance\": \"supports\", \"note\": \"'2. uerg- „wirken, tun“ ... Av. varəz- (varəzyeiti) ... npers. varz, barz „Feldarbeit, Ackerbau“ ... Gr. ergon „Werk, Arbeit“ (= dt. Werk)'\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1151-1152, s.v. werg-\", \"stance\": \"supports\", \"note\": \"'werg-. To do. I. Suffixed form *werg-o-. 1. Germanic *werkam, work ... WORK; b. Old High German werc: (BOULEVARD), BULWARK. 2. Greek ergon ... ALLERGY, ARGON, ENERGY, ... METALLURGY, SURGERY ... III. O-grade *worg- in Greek organon, tool: ORGAN, ORGANON. [Pok. 2. werg- 1168.]'\"},\n        {\"src\": \"SYN\", \"where\": \"§9.12-9.13 WORK (SYN.txt lines 13593-13640)\", \"stance\": \"supports\", \"note\": \"'1. From IE *werg- in Grk. erdō, rhezō ‘do’, Av. varəz- ‘work, do’, etc. Walde-P. 1.290 ff.'\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt, grep '^uerg'\", \"stance\": \"silent\", \"note\": \"Only uergh- 'annoy', uergho 'come', uergo 'twist' found; no entry for *uerĝ- 'work' located in the OCR.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"vareza\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. varəza- m. 'working, performance of; activity' (Bartholomae col. 1378) is the thematic action noun of the verb varəz- 'to work, do' (pres. varəziia-) < PIr. *warj- < PIE *werǵ-, with PIE palatal *ǵ > Av. z. It appears in compounds such as gavāstrya-varəza- 'performing agricultural work', which already shows the farming sense later found in NP barz/varz.\",\n          \"derivation_fa\": \"اوستایی varəza- «کار، انجام دادن، کوشش» نام‌واژه‌ای از ستاک فعلی varəz- «کار کردن» است. این ستاک از ایرانی باستان *warj- و هندواروپایی آغازین *werǵ- است و ǵ کامی هندواروپایی در اوستایی به z بدل شده است. ترکیب gavāstrya-varəza- «کار کشاورزی» در اوستا معنای کشاورزیِ «برز و ورز» فارسی را از پیش نشان می‌دهد. ادعای نورایی درست است (بارتولومه، ستون ۱۳۷۸؛ پوکورنی).\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wr̥jyáti\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1168\", \"status\": \"supports\", \"note\": \"'Avestan varəz- ... participle varšta-, varəza- m. work, Verrichten, occupation (npers. varz, barz)' (POK_full.txt ~line 91170).\"},\n            {\"ref\": \"KLN:1751\", \"status\": \"supports\", \"note\": \"Klein s.v. work (KLN_1971.txt line 268288): 'fr. I.-E. base *werg-, work, to work, whence also Avestic varəza, work, activity, vərəzyeiti, he works, does ... Gk. ergon'.\"},\n            {\"ref\": \"SYN:537\", \"status\": \"supports\", \"note\": \"Buck §9.12-9.13 WORK: 'Av. varəz- work, do', listed under IE *werg-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1376-1378 (BRT.txt lines 23003-23036)\", \"stance\": \"supports\", \"note\": \"'varəz- V. wirken' and 'varəza- m. Wirken, Verrichten von —; Tätigkeit'; also line 10181 'gavāstrya-varəza- n. Verrichten landwirtschaftlicher Arbeit'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"pp. 425-426 *u̯arz\", \"stance\": \"supports\", \"note\": \"'*u̯arz to do, work, till the land. AVESTAN: varəz- to do, work ... (+ *abi-) to cultivate'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 290\", \"stance\": \"supports\", \"note\": \"'Av. varəz- (varəzyeiti) ... varəza-'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"varzîdan; barz, varz; barz-gar; varzâv; varzeš 1\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Persian words belong to the same Iranian root as Av. varəz-, but they do not descend from Avestan. They continue MP warz 'farming, tillage', warzīdan / warz- 'to work, practise, till', warzīgar 'worker, peasant', warzišn 'work, tillage' and warzāw / warzag 'ploughing ox' (MacKenzie p. 88). Their -z- is the NW Iranian (Parthian-type) reflex of PIr *ź. Inherited SW Persian would have d (OP vard-, cf. Nyberg's *abi-varda- 'SW form of *abi-varza-'), so Cheung marks NP varzidan and barz as loans from that dialect. Initial w- > b- gives the doublets barz / varz and barzgar / varzgar. varzāv (varzā, varzu) means 'plough-ox' (Horn: 'Pflugstier'; Wiktionary: varz + gāv, 'tilling-cow'), not 'strong cow'. Aryanpur instead puts varzā with Skt. vṛṣabha 'bull' (PIE *wers- 'male'), but MP warzāw/warzag 'ploughing ox' supports Nourai's root. varzeš 'exercise, practice' < MP warzišn; the meaning 'sport' is a 20th-century specialisation.\",\n          \"derivation_fa\": \"«ورزیدن، ورز، برز، برزگر، ورزش» از فارسی میانهٔ warzīdan / warz-، warz «کشاورزی»، warzīgar «برزگر» و warzišn «کار، کشت» آمده‌اند. این واژه‌ها هم‌ریشهٔ اوستایی varəz- هستند ولی از خود اوستایی نیامده‌اند. z در آن‌ها گونهٔ شمال‌غربی (پارتی) است، زیرا گونهٔ بومی جنوب‌غربی d می‌داشت (پارسی باستان vard-). به همین دلیل چونگ و نیبرگ این صورت‌ها را وام‌واژهٔ گویشی می‌دانند. ابدال w به b در آغاز واژه دوگانه‌های «ورز/برز» و «ورزگر/برزگر» را ساخته است. «ورزاو» (ورزا، ورزو) از «ورز + گاو» و به معنی «گاو شخم» است، نه «گاو نیرومند» (هرن، مکنزی، برهان قاطع). آریان‌پور آن را با سنسکریت vṛṣabha «گاو نر» هم‌ریشه گرفته، ولی فارسی میانهٔ warzāw این را تأیید نمی‌کند. معنای «ورزش» به‌عنوان sport ساختهٔ سدهٔ بیستم است. پس ادعای نورایی در کل با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ورزیدن\",\n            \"https://en.wiktionary.org/wiki/ورز\",\n            \"https://en.wiktionary.org/wiki/ورزا\",\n            \"https://vajehyab.com/moein/ورزش\",\n            \"https://vajehyab.com/moein/برزگر\",\n            \"https://vajehyab.com/dehkhoda/ورزاو\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:254\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 474 (p. 254): 'برز ... بمعنی کشت و زراعت و کشاورزی باشد' with Mo'in's note 1: 'در پهلوی varz (کار کردن، اجرا کردن؛ کار، عمل) از اوستایی varəz (کار کردن) «بارتولمه ۱۳۷۸» در فارسی برز و ورز'. The same page has 'برزگر ... زراعت کننده' and 'برزه گاو، گاو زراعت را گویند'.\"},\n            {\"ref\": \"BQT:2268\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:2268 (vol. 4 pdf p. 351, OCR): 'ورز ... بمعنی حاصل کردن باشد - وکشت و زراعت را نیز گویند' and Mo'in's note: 'پهلوی varz (کار کردن، عمل؛ کار؛ شغل)؛ از اوستا varəz (کار کردن) «بارتولمه ۱۳۷۸». قس: فارسی برز، رک: ورزیدن'.\"},\n            {\"ref\": \"MON:5002\", \"status\": \"partial\", \"note\": \"The 6-volume page cannot be opened. On vajehyab, Mo'in s.v. ورزش has '1- تمرین، کار پیاپی و مرتب. 2- انجام حرکات بدنی خاص برای تقویت عضلات' and s.v. برزگر 'زارع، کشاورز. برزیگر هم گویند'. These confirm the meanings but give no etymology online.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 88 (PHD.txt lines 608-614)\", \"stance\": \"supports\", \"note\": \"'warzag (N warzāw) ploughing (ox)'; 'warzīdan, warz- work, act, practise; till; beget. ~išn: work, tillage'; 'warzīgar ... worker, peasant (N barzīgar)'.\"},\n            {\"src\": \"NYB\", \"where\": \"Part II p. ~204-205 (NYB_vol2_glossary.txt line 3993)\", \"stance\": \"supports\", \"note\": \"'varz farming ... Av. (1378) varəza-; MPrs wrz farming; NP varz a sown field, agriculture'. Line 1477: '*abi-varda- SW form of *abi-varza-', which confirms the SW/NW split.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 197, p. 46 (HRN.txt leaf 67)\", \"stance\": \"supports\", \"note\": \"'197. berz, verz Feldarbeit, verzīden, berzīden; verzgāv, verzāv Pflugstier. aw. varz- schaffen, tun; phlv. varz Feldarbeit'.\"},\n            {\"src\": \"HUB\", \"where\": \"p. ~155 (HUB.txt leaf 165)\", \"stance\": \"supports\", \"note\": \"'barz = varz Feldarbeit, phl. varz, zd. Wzl. varez'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 426 *u̯arz\", \"stance\": \"partial\", \"note\": \"'NP varzidan/varz- to sow a field (LW), barz a sown field; agriculture (LW)'. Same root, but Cheung marks the NP forms as dialect loanwords, not inherited SW forms.\"},\n            {\"src\": \"ARY\", \"where\": \"pdf p. 519-520 (printed 520-521), ARY_latin_index_pages.txt\", \"stance\": \"partial\", \"note\": \"ورزیدن entry: 'AVESTAN VAREZA, VARƏZYEITI; PAHLAVI VARZ, VARZISHN, WARZIDAN ... POKORNY 1168; MACKENZIE (WARZ-) 88', which supports. But the ورزا entry lists 'VARZA, WARZAG (PAHLAVI) ... VRSABHA (SANSKRIT), VACCA (LATIN) ... MACKENZIE (PLOUGHING OX) 127'. That puts varzā under the 'bull' root and contradicts Nourai for that word.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Old Persian\",\n          \"words\": \"vard\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"OP vard- 'to work' is the regular SW reflex of PIr *warj- (PIE *ǵ > PIr *ź > OP d). Kent lists it (p. 206-207: 'vard- vb. work: Av. varəz-, Gk. rhezō, Gm. Werk, pIE *u̯erĝ-; in Artavardiya-'), but it is attested only in the personal name Artavardiya- 'doing right', not as a free verb. Cheung reads the only possible verbal form (DB 4.44 vrdiyaiy) differently ('?vrd- to take'). The form is linguistically right, but the attestation is indirect.\",\n          \"derivation_fa\": \"پارسی باستان vard- «کار کردن» صورت قاعده‌مند جنوب‌غربیِ ریشهٔ ایرانی باستان *warj- است، چون ź ایرانی در پارسی باستان به d بدل می‌شود. کنت (ص ۲۰۶-۲۰۷) آن را آورده است، ولی تنها در نام خاص Artavardiya- «درست‌کردار» دیده می‌شود و فعل مستقلی از آن در کتیبه‌ها نیامده است. چونگ تنها صورت فعلی احتمالی (DB 4.44) را به گونهٔ دیگری می‌خواند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wr̥jyáti\"],\n          \"ref_check\": [\n            {\"ref\": \"KNT:207\", \"status\": \"supports\", \"note\": \"KNT_full.txt line 28834, between the page markers 206 and 207: 'vard- vb. ‘work’: Av. varəz-, Gk. ῥέζω ‘work’, Gm. Werk, pIE *u̯erĝ-; in Artavardiya-'. Kent marks it as occurring only inside the name.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"p. 426 *u̯arz\", \"stance\": \"partial\", \"note\": \"'OLD PERSIAN: (?) vrd- to take (differently Kent, l.c., ...) = Kent: 207a'. Cheung doubts a verbal attestation.\"},\n            {\"src\": \"BRT\", \"where\": \"col. 1376-1378\", \"stance\": \"supports\", \"note\": \"Gives Av. varəz- 'wirken' as the Avestan counterpart. BRT treats OP vardana- under a separate lemma (col. 1424 f.).\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"organon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gk. órganon 'tool, instrument; bodily organ; musical instrument' is formed from the o-grade *worǵ- with the suffix -ano- (Watkins: *worg-ano-). Digamma *w- was lost in Attic-Ionic. It is ablaut-related to érgon 'work' (Wiktionary: 'formed similarly to xóanon, compare érgon').\",\n          \"derivation_fa\": \"یونانی órganon «ابزار، اندام، ساز» از بالاگونهٔ o ریشه، یعنی *worǵ-، با پسوند -ano- ساخته شده است. w آغازی (دیگاما) در یونانی آتیکی افتاده است. این واژه با érgon «کار» در رابطهٔ دگرگونی واکه‌ای است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/ὄργανον\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1152: 'III. O-grade form *worg- in: a. Greek organon (with suffix -ano-), tool: ORGAN, ORGANON'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1168\", \"stance\": \"supports\", \"note\": \"'organon tool' listed under u̯erĝ-.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. organ (KLN_1971.txt line 168586)\", \"stance\": \"supports\", \"note\": \"'Gk. organon, instrument; bodily organ; musical instrument ... in gradational relationship to ergon (for *Fergon), work'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Arabic\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Empty pass-through node for Arabic arġanūn / urġun 'organ'. Classical Arabic took the Greek word órganon, through Syriac ʾorganon, in the ʿAbbāsid translation period: Greek o- became a-/u-, Greek g became ġ, and the ending -on became -ūn. Mo'in marks ارغنون '[معر - یو.]', i.e. an Arabicised Greek word. No independent Arabic etymological dictionary on disk has the word, so the Syriac step is not confirmed from the library.\",\n          \"derivation_fa\": \"این خانهٔ تهی نمایندهٔ عربی «ارغنون / اُرغُن» است. عربی در دورهٔ ترجمه (عباسی) واژهٔ یونانی órganon را احتمالاً از راه سریانی گرفته است. o یونانی به a/u، g به غ و پایانهٔ -on به -ūn بدل شده است. معین آن را «معرّب از یونانی» می‌داند. پس ادعای نورایی پذیرفتنی است، ولی گام سریانی در منابع موجود تأیید نشد.\",\n          \"sources\": [\"https://vajehyab.com/moein/ارغنون\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:203\", \"status\": \"supports\", \"note\": \"vajehyab Mo'in s.v. ارغنون: '(اَ غَ) [معر - یو.] (اِ.) نوعی ساز که از تعداد زیادی لوله تشکیل شده ...' (معرّب from Greek).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFM\", \"where\": \"AFM.txt / AFM_pages.txt grep 'رغن'\", \"stance\": \"silent\", \"note\": \"Not found (Addi Shir covers Persian loans in Arabic).\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt grep 'organ'\", \"stance\": \"silent\", \"note\": \"No arġanūn entry; only unrelated hits (jorgan, mergan).\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 1 p. ~106 (BQT_v1_pages.txt leaf 318)\", \"stance\": \"supports\", \"note\": \"Mo'in's note on ارغنون: 'از یونانی organon'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"arghanŭn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP arġanūn 'a (pipe-)organ; a concert of many voices' is the Arabicised Greek órganon (see #5). It entered Persian with Arabic learning and is common in classical poetry. Borhan also records the short forms arġan and arġun. The book prints 'arghanŭn' with a breve; the usual transliteration is arġanūn.\",\n          \"derivation_fa\": \"«ارغنون» در فارسی به معنی سازی بادی با لوله‌های بسیار و نیز هم‌آوایی چند آواز است. این واژه معرّبِ یونانی órganon است و از راه عربی به فارسی آمده و در شعر کلاسیک فراوان است. برهان قاطع صورت‌های کوتاه «ارغن» و «ارغون» را هم آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/ارغنون\", \"https://vajehyab.com/moein/ارغنون\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:106\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 318-319: 'ارغنون ... سازیست ... افلاطون وضع کرده' and 'ارغن ... مخفف ارغنون است. و آن سازی باشد که رومیان نوازند', with Mo'in's note 'از یونانی organon'.\"},\n            {\"ref\": \"MON:203\", \"status\": \"supports\", \"note\": \"vajehyab Mo'in: 'ارغنون [معر - یو.] نوعی ساز ...'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"HRN.txt grep 'arghan|argan[uū]n|organon'\", \"stance\": \"silent\", \"note\": \"0 hits.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt same grep\", \"stance\": \"silent\", \"note\": \"0 hits.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Pass-through node for French orgue / organe < Latin organum < Gk. órganon. The chart leaves out Latin. French is the right source for Persian org (#8), but English organ came partly from OE organa / ME organe (direct from Latin organum, partly via Old French organe), and organon came straight from Greek.\",\n          \"derivation_fa\": \"خانهٔ تهی برای فرانسوی orgue / organe است که از لاتینی organum و یونانی órganon آمده است. نورایی گام لاتینی را حذف کرده است. فرانسوی برای «ارگ» فارسی درست است، ولی انگلیسی organ بخشی از لاتینی و فرانسوی کهن آمده و organon مستقیم از یونانی است. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/organ\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:296\", \"status\": \"partial\", \"note\": \"The 1976 page cannot be opened. The 1985 Watkins text (s.v. werg-) gives only 'Greek organon ...: ORGAN, ORGANON' with no French stage.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. organ\", \"stance\": \"partial\", \"note\": \"'ME. organe, a musical instrument, fr. L. organum, fr. Gk. organon'. Latin is the immediate source.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 12862 'ORGAN.'\", \"stance\": \"silent\", \"note\": \"Headword found, but the etymology text is not legible in the OCR.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"org\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP org 'organ (instrument); harmonium' is a 19th/20th-century loan from French orgue, which continues Latin organum (Old French orgene / orgue). Mo'in marks it [فر.] and glosses it 'ارغنون'. So Persian has the same Greek word twice: arġanūn (old, via Arabic) and org (modern, via French).\",\n          \"derivation_fa\": \"«اُرگ» وام‌واژهٔ نوین (سدهٔ ۱۹-۲۰) از فرانسوی orgue است که از لاتینی organum آمده است. معین آن را [فر.] و هم‌معنی «ارغنون» آورده است. پس فارسی این واژهٔ یونانی را دو بار گرفته است: یک بار «ارغنون» (کهن، از راه عربی) و یک بار «ارگ» (نو، از راه فرانسوی). ادعای نورایی درست است.\",\n          \"sources\": [\"https://vajehyab.com/moein/ارگ\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:205\", \"status\": \"supports\", \"note\": \"vajehyab Mo'in s.v. ارگ: '( اُ ) [فر.] (اِ.) 1 - ارغنون. 2 - نوعی ساز شبیه به پیانو اما کوچکتر از آن'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"-\", \"stance\": \"silent\", \"note\": \"A modern French loan, not in Borhan (BQT ارگ is 'citadel', a different word).\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. organ\", \"stance\": \"supports\", \"note\": \"Gives the Greek > Latin > French chain.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"organ, organon\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English organ: OE organa / ME organe 'musical instrument' < Latin organum (partly via Old French organe) < Gk. órganon. organon 'instrument of thought, logical system' (16th c., after Aristotle's Organon) is borrowed straight from Greek. Both are correctly derived from órganon, but neither came through French in the simple way the chart shows.\",\n          \"derivation_fa\": \"انگلیسی organ از انگلیسی کهن organa / میانه organe آمده که از لاتینی organum (بخشی از راه فرانسوی کهن) و یونانی órganon است. organon «ابزار اندیشه» (سدهٔ ۱۶، به پیروی از ارغنون ارسطو) مستقیم از یونانی گرفته شده است. ریشه درست است، ولی راه فرانسوی ساده‌سازی است. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/organ\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:926\", \"status\": \"supports\", \"note\": \"Watkins s.v. werg-: 'Greek organon ... ORGAN, ORGANON'. The 1976 page cannot be opened.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. organ, organon (KLN_1971.txt 168586; KLN_1966.txt 26545)\", \"stance\": \"supports\", \"note\": \"'organ, n. — ME. organe ... fr. L. organum, fr. Gk. organon'; 'organon ... Gk. organon, instrument, organ (often used as the title of works on logic)'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt 'ORGAN.'\", \"stance\": \"silent\", \"note\": \"Entry not legible in the OCR.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Middle German\",\n          \"words\": \"bolwerk\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"bolwerc 'bulwark, rampart', literally 'plank-work' (bole 'tree trunk, plank', PIE *bʰel- 'swell', + werc 'work' < Gmc *werka-), is Middle Dutch / Middle Low German (also MHG bolwerc). Klein derives French boulevard from MDu. bolwerc. Wiktionary gives MHG bolwerc or MDu bolwerk. Nourai's label 'Middle German' fits only if read broadly, and only the second element belongs to this root.\",\n          \"derivation_fa\": \"bolwerc «بارو، استحکامات» در هلندی میانه و آلمانی میانه به معنای لفظی «کارِ تیر و الوار» است. جزء نخست bol «تنهٔ درخت، الوار» است و جزء دوم werc «کار» از ژرمنی *werka-. کلاین واژهٔ فرانسوی boulevard را از هلندی میانه می‌گیرد و ویکی‌واژه هر دو احتمال را آورده است. برچسب «آلمانی میانه» تنها با تسامح درست است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/boulevard\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:209\", \"status\": \"supports\", \"note\": \"Klein s.v. bulwark (KLN_1971.txt 35193): 'ME. bulwerk, fr. MLG. (= Du.) bolwerk, which is rel. to MHG. bolwerk, G. Bollwerk ... lit. mean bole work. See bole ... and work and cp. boulevard'.\"},\n            {\"ref\": \"AHD:155\", \"status\": \"supports\", \"note\": \"Watkins s.v. werg-: 'Old High German werc, work: (BOULEVARD), BULWARK'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT_dli_revised.txt line 10257\", \"stance\": \"supports\", \"note\": \"'Bulwark ... Du. bolwerk, G. bollwerk (whence F. boulevard). Compounded of ... bol, trunk of a tree ... and ... værk, a work'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. boulevard (KLN_1971.txt 32365)\", \"stance\": \"partial\", \"note\": \"'F., earlier boloart, boulevert ... orig. meaning work of fortification, fr. MDu. bolwerc'. Middle Dutch, not Middle German.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pass-through node for French boulevard < 15th-century boloart, boulevert 'rampart' < MDu. bolwerc. Folk reshaping changed -werc to -vard / -vert. The sense moved from 'rampart' to 'broad tree-lined promenade on a razed rampart', after the Paris walls were levelled under Louis XIV (1670s).\",\n          \"derivation_fa\": \"خانهٔ تهی برای فرانسوی boulevard است، از boloart / boulevert سدهٔ ۱۵ به معنی «بارو» و آن از هلندی میانه bolwerc. -werc در فرانسوی به -vard دگرگون شده است. معنا پس از ویران شدن باروهای پاریس در روزگار لویی چهاردهم از «بارو» به «خیابان پهنِ درخت‌کاری‌شده بر جای بارو» تغییر کرد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/boulevard\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node has no reference of its own.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. boulevard\", \"stance\": \"supports\", \"note\": \"'F., earlier boloart, boulevert, balouart ... orig. meaning work of fortification, fr. MDu. bolwerc'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Bulwark\", \"stance\": \"supports\", \"note\": \"'(whence F. boulevard)'.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Persian\",\n          \"words\": \"bolvâr\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP bolvār / bulvār 'boulevard, wide avenue' is a modern (Pahlavi-era urban planning, 20th c.) loan from French boulevard. The final -d was dropped and the vowel shortened. Mo'in marks it French.\",\n          \"derivation_fa\": \"«بلوار / بولوار» وام‌واژهٔ نوین سدهٔ بیستم (همراه با شهرسازی دورهٔ پهلوی) از فرانسوی boulevard است. d پایانی افتاده و واکه کوتاه شده است. معین آن را فرانسوی دانسته است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://vajehyab.com/dehkhoda/بلوار\"],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Dehkhoda (vajehyab) s.v. بلوار: '(فرانسوی، اِ) بولوار. (فرهنگ فارسی معین)'. Mo'in's own page could not be opened (vajehyab/moein/بلوار fetch failed).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"grep 'bulvar|bolvar|boulevard'\", \"stance\": \"silent\", \"note\": \"0 hits (19th-c. work, before the loan).\"},\n            {\"src\": \"HUB\", \"where\": \"same grep\", \"stance\": \"silent\", \"note\": \"0 hits.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"boulevard\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English boulevard (1769) is borrowed from French boulevard 'promenade on a former rampart' (< MDu. bolwerc). It is a doublet of bulwark, which English took earlier (ME bulwerk) directly from Low German / Dutch.\",\n          \"derivation_fa\": \"انگلیسی boulevard (۱۷۶۹) از فرانسوی boulevard گرفته شده است. این واژه با bulwark دوگانه است، که انگلیسی میانه آن را زودتر مستقیم از آلمانی پست یا هلندی گرفته بود. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/boulevard\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:155\", \"status\": \"supports\", \"note\": \"Watkins s.v. werg-: '(BOULEVARD), BULWARK'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. boulevard\", \"stance\": \"supports\", \"note\": \"'boulevard, n. — F., earlier boloart ... fr. MDu. bolwerc. See bulwark'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Bulwark\", \"stance\": \"supports\", \"note\": \"'G. bollwerk (whence F. boulevard)'.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Germanic\",\n          \"words\": \"werkam\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *werką 'work, deed' (Watkins *werkam) < PIE *wérǵom, a thematic neuter of the e-grade, with Grimm's law *ǵ > *k. It is the exact equivalent of Gk. (w)érgon. Reflexes: OE weorc, OS/OFris. werk, OHG werah/werc, ON verk.\",\n          \"derivation_fa\": \"ژرمنی آغازین *werką «کار» از هندواروپایی آغازین *wérǵom است، با دگرگونی ǵ به k بر پایهٔ قانون گریم. این صورت درست برابر یونانی (w)érgon است. بازمانده‌های آن انگلیسی کهن weorc، آلمانی کهن werc و نوردی کهن verk هستند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wérǵom\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"'Suffixed form *werg-o-. 1. Germanic *werkam, work'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1168\", \"stance\": \"supports\", \"note\": \"'Old High German werc, werah, Old Saxon werk, Old Icelandic verk (= ergon) work'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 290\", \"stance\": \"supports\", \"note\": \"'Gr. ergon Werk, Arbeit (= dt. Werk)'.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"English\",\n          \"words\": \"work\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English work < ME werk < OE weorc / werc 'work, deed' (with OE breaking e > eo before r + consonant; later wo- > wu- rounding) < PGmc *werką.\",\n          \"derivation_fa\": \"انگلیسی work از انگلیسی میانه werk و انگلیسی کهن weorc / werc «کار، کردار» آمده و آن از ژرمنی *werką است. e در انگلیسی کهن پیش از r به eo بدل شده و سپس پس از w گرد شده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/work\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node has no reference of its own.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. work (KLN_1971.txt 268288)\", \"stance\": \"supports\", \"note\": \"'work, n. — ME. werk, fr. OE. weorc, ... fr. I.-E. base *werg-'.\"},\n            {\"src\": \"AHD\", \"where\": \"s.v. werg-\", \"stance\": \"supports\", \"note\": \"'Old English weorc, werc, work: WORK'.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Greek\",\n          \"words\": \"ergon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gk. érgon 'work, deed' (dialectal wérgon, with digamma, in Elean / Boeotian inscriptions) < PIE *wérǵom. Attic-Ionic lost *w-. Its derivatives include energeia 'activity', -ourgos 'worker' (kheirourgos, geōrgos, metallourgos) and argos 'idle' < *a-ergos.\",\n          \"derivation_fa\": \"یونانی érgon «کار، کردار» از هندواروپایی آغازین *wérǵom است. صورت wérgon با دیگاما در کتیبه‌های گویشی آمده و w در آتیکی-ایونی افتاده است. energeia «کنش‌وری»، پسوند -ourgos «کارگر» (در kheirourgos «جراح» و geōrgos «کشاورز») و argos «بیکار» (از *a-ergos) از آن ساخته شده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wérǵom\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"'2. Greek ergon, work, action: ERG, -URGY; ALLERGY, ARGON, ... ENERGY ... METALLURGY, SURGERY'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1168\", \"stance\": \"supports\", \"note\": \"'gr. ergon, Fergon work (= German Werk), ergazomai arbeite'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. ergon (KLN_1971.txt 84788)\", \"stance\": \"supports\", \"note\": \"'Gk. ergon (dial. Fergon), work. See work ... Cp. also allergy, argon ... energy ... George'.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Pass-through node for French énergie, métallurgie, allergie, chirurgie. It is right as the source of the Persian words (#18) and of energy and surgery, which came through Old/Middle French. It is not the route for argon (coined in English by Ramsay and Travers, 1894) or allergy (German Allergie, coined by von Pirquet, 1906).\",\n          \"derivation_fa\": \"خانهٔ تهی برای فرانسوی énergie، métallurgie، allergie و chirurgie است. این برای واژه‌های فارسی (#۱۸) و برای energy و surgery درست است. ولی argon در انگلیسی (رمزی و تراورس، ۱۸۹۴) و allergy در آلمانی (فون پیرکه، ۱۹۰۶) ساخته شده‌اند و از راه فرانسوی نیامده‌اند. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://vajehyab.com/moein/انرژی\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node has no reference of its own.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. allergy (KLN_1966.txt 2264), argon (3404)\", \"stance\": \"partial\", \"note\": \"'allergy ... ModL. allergia, coined about 1905 by Clemens von Pirquet'; 'argon ... ModL., fr. Gk. argon, neut. of argos, idle ... discovered by ... Ramsay ... and Travers in 1894'. Neither goes through French.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT_dli_revised.txt 25013\", \"stance\": \"supports\", \"note\": \"'Energy. (F. — L. — Gk.) O.F. energie — Late L. energia — Gk. energeia'.\"}\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"Persian\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The node has no transliteration; the script gives انرژی، متالورژی، آلرژی (enerži, metālurži, āleržī). All three are 20th-century loans from French énergie, métallurgie, allergie. The French -gie [ʒi] is rendered -ži, which shows the French route. Mo'in marks انرژی [فر.]. Each contains Gk. ergon (en-ergeia, metall-ourgia, all-ergia).\",\n          \"derivation_fa\": \"«انرژی، متالورژی، آلرژی» وام‌واژه‌های سدهٔ بیستم از فرانسوی énergie، métallurgie و allergie هستند. «ژ» در پایان آن‌ها برابر -gie فرانسوی [ʒi] است و راه فرانسوی را نشان می‌دهد. معین «انرژی» را [فر.] آورده است. هر سه جزء یونانی ergon «کار» را دارند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://vajehyab.com/moein/انرژی\"],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"vajehyab Mo'in s.v. انرژی: '(اِ نِ) [فر.] (اِ.) نیرو، قدرت، توانایی انجام کار، کارمایه'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. allergy, metallurgy, energy\", \"stance\": \"supports\", \"note\": \"'metallurgy — ModL. metallurgia, fr. Gk. metallourgos, worker in metal ... and ergon, work'; 'energy, n. — Late L. energia, fr. Gk. energeia'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Energy\", \"stance\": \"supports\", \"note\": \"'(F. — L. — Gk.) O.F. energie'.\"}\n          ]\n        },\n        {\n          \"id\": 19,\n          \"lang\": \"English\",\n          \"words\": \"argon, energy, allergy, metallurgy, surgery, George\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All six contain Gk. ergon, but they reached English by different routes. energy: MF énergie < LL energia < Gk. energeia. surgery: ME surgerie < OF surgerie, cirurgerie < L chirurgia < Gk. kheirourgia 'hand-work'. George: OF George < L Georgius < Gk. Geōrgios < geōrgos 'earth-worker, farmer'. metallurgy: ModL metallurgia < Gk. metallourgos (via French or directly). allergy: German Allergie (von Pirquet 1906) < Gk. allos + ergon. argon: coined in English in 1894 by Ramsay and Travers from Gk. argon, neuter of argos 'idle' < *a-ergos 'not working'. So the root is right for all six, but the 'via French' route holds only for some.\",\n          \"derivation_fa\": \"هر شش واژه جزء یونانی ergon را دارند، ولی از راه‌های گوناگون به انگلیسی رسیده‌اند. energy از فرانسوی میانه، لاتینی و یونانی energeia آمده است. surgery از فرانسوی کهن cirurgerie، لاتینی chirurgia و یونانی kheirourgia «کار دست» است. George از یونانی geōrgos «کشاورز» و از راه فرانسوی آمده است. metallurgy از لاتینی نو metallurgia است. allergy را فون پیرکه در ۱۹۰۶ در آلمانی ساخت. argon را رمزی و تراورس در ۱۸۹۴ از argos «بیکار» (*a-ergos) ساختند. پس ریشه درست است، ولی راه فرانسوی تنها برای برخی صدق می‌کند و ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wérǵom\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node has no reference of its own. AHD (Watkins, s.v. werg-) lists ALLERGY, ARGON, ENERGY, GEORGIC, METALLURGY, SURGERY under Greek ergon.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. argon (KLN_1966 3404), allergy (2264), George (16039), metallurgy (23674), surgery (KLN_1971 237552)\", \"stance\": \"supports\", \"note\": \"'argon ... fr. Gk. argon, neut. of argos, idle, contraction of aergos, lit. not active'; 'George ... Gk. geōrgos, husbandman ... ge, earth, and the base of ergon'; 'surgery — ME. surgerie, fr. OF. surgerie, contracted fr. serurgerie, cirurgerie, fr. Late L. chirurgia'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Energy; Surgeon (SKT_dli_revised.txt 25013, 77588)\", \"stance\": \"supports\", \"note\": \"'Energy. (F. — L. — Gk.)'; 'Surgeon, contracted form of chirurgeon'.\"},\n            {\"src\": \"AHD\", \"where\": \"s.v. werg-\", \"stance\": \"supports\", \"note\": \"Lists all of these under Greek ergon.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-17T00:08:51.850Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-549.json (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:08:55.675Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -m json.tool data/verification/page-549.json >/dev/null && echo ok; python3 tools/verify_check.py 549"
}
```


### [2026-10-17T00:08:56.197Z] TOOL RESULT

```
ok
nodes verified: 19/19
node verdicts: {'confirmed': 11, 'plausible': 8}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 19, 'partial': 2, 'not_checked': 4}
books consulted: {'supports': 30, 'partial': 6, 'silent': 9} | by book: {'KLN': 12, 'SKT': 8, 'CHEUNG': 3, 'HRN': 3, 'HUB': 3, 'POK': 3, 'BRT': 2, 'WLD': 2, 'BQT': 2, 'AHD': 2, 'PHD': 1, 'NYB': 1, 'ARY': 1, 'AFM': 1, 'LKT': 1}
```


## [2026-10-17T00:09:05.833Z] TOOL CALL #63: SubagentHandback

```json
{
 "message": "Page 549 (book page 519) is verified. I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-549.json`; `verify_check.py 549` passes with 0 PROBLEM lines and all 19 nodes covered. Only one entry has nodes (Werg 1); the five redirects (Werg 2, Werg 3, Wermi, Werp, Wert) are skipped as the instructions say.\n\n- **Root:** confirmed. Werg 1 is PIE *werǵ- 'to work' (Pokorny 1168, Walde-Pokorny I 290, Watkins werg-).\n- **Nodes:** 11 confirmed, 8 plausible, 0 disputed, 0 transcription_suspect.\n- **Plausible nodes and why:**\n  - **#2 Persian varzîdan / barz / varz / barzgar / varzâv / varzeš:** these continue Middle Persian warz-, but their -z- is a dialectal (northwestern, Parthian-type) form, not native southwestern Persian, which would have -d- (Cheung and Nyberg). The gloss \"strong cow\" for varzâv is wrong; it means plough-ox (MacKenzie, Horn, Wiktionary). Aryanpur instead links varzā to Sanskrit vṛṣabha 'bull'.\n  - **#3 Old Persian vard:** Kent has it only inside the personal name Artavardiya-, and Cheung reads the one possible verb form differently.\n  - **#5 Arabic (empty node):** arġanūn is an Arabicised Greek word according to Mo'in. The Syriac step could not be checked in the books on disk.\n  - **#7 French and #9 English organ, organon:** the chart leaves out Latin organum, and organon came into English directly from Greek.\n  - **#10 bolwerk:** labelled \"Middle German\", but Klein derives French boulevard from Middle Dutch bolwerc (Wiktionary allows either).\n  - **#17 French and #19 English argon, energy, allergy, metallurgy, surgery, George:** all contain Greek ergon, but argon (coined in 1894) and allergy (German, 1906) did not come through French.\n- **Extraction errors:** none. The JSON matches the printed page (site/pages/549.jpg). One small gap: the page has an empty, unlabelled box to the right of the Old Persian node that the JSON leaves out. It holds no word.\n\nNourai's own references were checked where they could be read: POK, KNT, KLN, SYN, AHD (via the 1985 Watkins text), BQT 254, 2268 and 106 (Mo'in's footnotes), and Mo'in via vajehyab. The 1976 AHD page numbers and the 6-volume Mo'in pages cannot be opened. Etymonline would not load, so English routes rest on Klein, Skeat, Watkins and Wiktionary. All web pages cited are archived under data/verification/sources/web/."
}
```


### [2026-10-17T00:09:06.105Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
