# Verification process log — verify-page-561


## [2026-10-17T00:30:14.224Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 561 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-561.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-561.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-561.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 561` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.269Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:19.957Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:30:19.993Z] TOOL RESULT

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


## [2026-10-17T00:30:20.456Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-561.txt"
}
```


### [2026-10-17T00:30:20.472Z] TOOL RESULT

```
1	=== PDF page 561 (book page 531) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Yâ, lâ 2 : to be aroused  (refs POK:501)
4	#1 (parent #0) [Avestan] refs=POK:501 | yâ-tu : magic ; yâsâ : wish
5	  #2 (parent #1) [Pahlavi] refs=BQT:553,2419 | žâtŭk : magic ; yâsak : wish
6	    #3 (parent #2) [Persian] refs=BQT:553,2419; HRN:92; HUB:107; ARP:218 | jâdŭ «جادو» : magic ; yâseh «یاسه» : wish | NOTE: Compare with the root "Ei" from which the Sanskrit word "jadoo:sorcery" is derived.
7	#4 (parent #0) [Greek] refs=AHD | zělos : zeal
8	  #5 (parent #4) [English] refs=None | zeal, jealous
9	--- entry 1 ---
10	ROOT Yâ 3 -> redirect to Yah 5
11	--- entry 2 ---
12	ROOT [Indo-European] Yag, lag : to worship  (refs POK:501)
13	#1 (parent #0) [Avestan] refs=POK:501; HRN:95,252; KLN:1759; ZAW:38 | yaz : to worship ; yazatanam : God ; yesnya : worship ; mazda-yasna : God worshiper ☞Men 1 ; yazato-kerata : God's creation ☞Kwer
14	  #2 (parent #1) [Persian] refs=BQT:752,2432; ETM:64 | Îzad «ایزد ( یزدان ، یزد )» ; yasnâ «یسنا ( مزدیسنا )» : worship ceremony ; jašn «جشن» : celebration ; Yazdgerd «یزدگرد» : "God's creation"
15	#3 (parent #0) [Greek] refs=AHD | hagnos : sacred, holy
16	  #4 (parent #3) [English] refs=None | Agnus
17	--- entry 3 ---
18	ROOT [Avestan] Yah 5, Yâ 3 : comparative suffix  (refs POK:521,618,699,708,800)
19	#1 (parent #0) [Avestan] refs=POK:521,618,699,708,800; KLN:371,958; SYN:880 | maz-yah, mathi-yah : greater ☞Meg ; mas-yah, mas-yâ 2 ☞Mâk ; frâ-yah : more plentiful ☞Pel 1 ; kas-yah : smaller ☞Kak 3 ; sra-yah : better ☞Krei
20	
```


## [2026-10-17T00:30:20.973Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-561.json"
}
```


### [2026-10-17T00:30:20.993Z] TOOL RESULT

```
1	{
2	  "pdf_page": 561,
3	  "book_page": 531,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Yâ, lâ 2",
8	        "lang": "Indo-European",
9	        "refs": "POK:501",
10	        "gloss": "to be aroused"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:501",
18	          "words": [
19	            {"translit": "yâ-tu", "gloss": "magic", "script": null},
20	            {"translit": "yâsâ", "gloss": "wish", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Pahlavi",
29	          "refs": "BQT:553,2419",
30	          "words": [
31	            {"translit": "žâtŭk", "gloss": "magic", "script": null},
32	            {"translit": "yâsak", "gloss": "wish", "script": null}
33	          ],
34	          "note": null,
35	          "quote": null
36	        },
37	        {
38	          "id": 3,
39	          "parent": 2,
40	          "lang": "Persian",
41	          "refs": "BQT:553,2419; HRN:92; HUB:107; ARP:218",
42	          "words": [
43	            {"translit": "jâdŭ", "gloss": "magic", "script": "جادو"},
44	            {"translit": "yâseh", "gloss": "wish", "script": "یاسه"}
45	          ],
46	          "note": "Compare with the root \"Ei\" from which the Sanskrit word \"jadoo:sorcery\" is derived.",
47	          "quote": null
48	        },
49	        {
50	          "id": 4,
51	          "parent": 0,
52	          "lang": "Greek",
53	          "refs": "AHD",
54	          "words": [
55	            {"translit": "zělos", "gloss": "zeal", "script": null}
56	          ],
57	          "note": null,
58	          "quote": null
59	        },
60	        {
61	          "id": 5,
62	          "parent": 4,
63	          "lang": "English",
64	          "refs": null,
65	          "words": [
66	            {"translit": "zeal, jealous", "gloss": null, "script": null}
67	          ],
68	          "note": null,
69	          "quote": null
70	        }
71	      ]
72	    },
73	    {
74	      "root": {"name": "Yâ 3", "redirect": "Yah 5"},
75	      "nodes": []
76	    },
77	    {
78	      "root": {
79	        "name": "Yag, lag",
80	        "lang": "Indo-European",
81	        "refs": "POK:501",
82	        "gloss": "to worship"
83	      },
84	      "nodes": [
85	        {
86	          "id": 1,
87	          "parent": 0,
88	          "lang": "Avestan",
89	          "refs": "POK:501; HRN:95,252; KLN:1759; ZAW:38",
90	          "words": [
91	            {"translit": "yaz", "gloss": "to worship", "script": null},
92	            {"translit": "yazatanam", "gloss": "God", "script": null},
93	            {"translit": "yesnya", "gloss": "worship", "script": null},
94	            {"translit": "mazda-yasna", "gloss": "God worshiper", "script": null, "see": ["Men 1"]},
95	            {"translit": "yazato-kerata", "gloss": "God's creation", "script": null, "see": ["Kwer"]}
96	          ],
97	          "note": null,
98	          "quote": null
99	        },
100	        {
101	          "id": 2,
102	          "parent": 1,
103	          "lang": "Persian",
104	          "refs": "BQT:752,2432; ETM:64",
105	          "words": [
106	            {"translit": "Îzad", "gloss": null, "script": "ایزد ( یزدان ، یزد )"},
107	            {"translit": "yasnâ", "gloss": "worship ceremony", "script": "یسنا ( مزدیسنا )"},
108	            {"translit": "jašn", "gloss": "celebration", "script": "جشن"},
109	            {"translit": "Yazdgerd", "gloss": "\"God's creation\"", "script": "یزدگرد"}
110	          ],
111	          "note": null,
112	          "quote": null
113	        },
114	        {
115	          "id": 3,
116	          "parent": 0,
117	          "lang": "Greek",
118	          "refs": "AHD",
119	          "words": [
120	            {"translit": "hagnos", "gloss": "sacred, holy", "script": null}
121	          ],
122	          "note": null,
123	          "quote": null
124	        },
125	        {
126	          "id": 4,
127	          "parent": 3,
128	          "lang": "English",
129	          "refs": null,
130	          "words": [
131	            {"translit": "Agnus", "gloss": null, "script": null}
132	          ],
133	          "note": null,
134	          "quote": null
135	        }
136	      ]
137	    },
138	    {
139	      "root": {
140	        "name": "Yah 5, Yâ 3",
141	        "lang": "Avestan",
142	        "refs": "POK:521,618,699,708,800",
143	        "gloss": "comparative suffix"
144	      },
145	      "nodes": [
146	        {
147	          "id": 1,
148	          "parent": 0,
149	          "lang": "Avestan",
150	          "refs": "POK:521,618,699,708,800; KLN:371,958; SYN:880",
151	          "words": [
152	            {"translit": "maz-yah, mathi-yah", "gloss": "greater", "script": null, "see": ["Meg"]},
153	            {"translit": "mas-yah, mas-yâ 2", "gloss": null, "script": null, "see": ["Mâk"]},
154	            {"translit": "frâ-yah", "gloss": "more plentiful", "script": null, "see": ["Pel 1"]},
155	            {"translit": "kas-yah", "gloss": "smaller", "script": null, "see": ["Kak 3"]},
156	            {"translit": "sra-yah", "gloss": "better", "script": null, "see": ["Krei"]}
157	          ],
158	          "note": null,
159	          "quote": null
160	        }
161	      ]
162	    }
163	  ]
164	}
165	
```


## [2026-10-17T00:30:29.497Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','AHD','IEC','SYN','BRT','KNT','PHD','NYB','HRN','HUB','CHEUNG','BQT','MON','ARY','ARP','KLN','SKT','FSD','WEB','ZAW','ETM']:\n  v=d.get(k); print(k, v and {x:v.get(x) for x in ['local_file','page_offset','kind','lookup_hint']})\n\""
}
```


### [2026-10-17T00:30:29.861Z] TOOL RESULT

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
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
WLD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'kind': 'archive_djvu', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'kind': 'archive_djvu+website+archive_restricted', 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
IEC {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
SYN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
BRT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
KNT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt', 'page_offset': 'leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations."}
PHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
NYB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
HRN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
HUB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
CHEUNG None
BQT {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'kind': 'archive_djvu+local_scan_ocr', 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'kind': 'website+archive_djvu', 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
ARY {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'kind': 'local_scan_ocr', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
ARP {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARP.txt', 'page_offset': 'leaf = printed + 14 (e.g. leaf 97 = p.83). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': 'Continuous prose with word-index at the end; grep the Avestan/Sanskrit word.'}
KLN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
SKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
FSD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt', 'page_offset': 'vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file."}
WEB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt', 'page_offset': 'not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': 'Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.'}
ZAW {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt'], 'page_offset': 'ZAW_pages.txt: 306 leaves; printed = leaf(1-based) − 24 (leaf 60 = p.36; leaf 20 = p.X).', 'kind': 'google_books', 'lookup_hint': "Google Books page reports 'Preview' from this location, but the 1906 book is public domain and is listed on Google Play Books, so full view may be available depending on region; try https://books.google.com/books?id=agDP0HdEssEC&pg=PA<page> . Not found on IA (searched 'zum altiranischen', 'nacharbeiten vorarbeiten'); HathiTrust blocked automated access."}
ETM {'local_file': None, 'page_offset': None, 'kind': 'catalog', 'lookup_hint': 'Searched archive.org, ketabnak, noorlib, web: not found.'}
```


## [2026-10-17T00:30:33.407Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,200p tools/verify_check.py | head -150; python3 -c \"\nimport json;d=json.load(open('data/verification/page-558.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-10-17T00:30:33.751Z] TOOL RESULT

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
 "root": "Xac 1",
 "verdict": "plausible",
 "modern_form": "Skt. khac- 'shine through' (?) (Buck, after Uhlenbeck); modern view: Skt. kāca- probably a Nuristani loan, cognate with Skt. kāś- 'to shine'",
 "note": "The book files this chart under X because Nourai writes Skt. kh as X ('Xac' = Skt. khac-). The root and gloss come straight from Buck SYN 620, who gives it with a question mark: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' Wiktionary (after Mayrhofer) calls kāca- 'likely borrowed from a Nuristani language (*kāt's'a), cognate with Sanskrit kāś- to shine brightly'. Either way, a 'shining' root sits behind the glass word, so the chart is defensible, but the specific root khac- is uncertain. The extraction matches the printed page.",
 "note_fa": "نورایی ریشه را سنسکریت khac- «از درون درخشیدن» می‌گیرد (او kh سنسکریت را X می‌نویسد، از همین رو این مدخل زیر حرف X آمده). این ریشه را باک (SYN ص ۶۲۰) به پیروی از اولنبک، و خودش با علامت پرسش، آورده است. ویکی‌واژه به نقل از مایرهوفر سنسکریت kāca- «شیشه» را احتمالاً وام‌واژه‌ای از زبان‌های نورستانی (*kāt's'a) و هم‌ریشه با kāś- «درخشیدن» می‌داند. پس پیوند «شیشه» با ریشه‌ای به معنای درخشیدن پذیرفتنی است، اما خودِ ریشهٔ khac- قطعی نیست و ادعای نورایی را باید با احتیاط پذیرفت.",
 "sources": [
  "https://en.wiktionary.org/wiki/काच"
 ],
 "ref_check": [
  {
   "ref": "SYN:620",
   "status": "supports",
   "note": "SYN.txt (printed p. 620, section 9.74 GLASS), para 7: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' This is exactly Nourai's root and gloss, including Buck's hesitation."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "POK_full.txt grep 'kāca|kāś-|kāçat'",
   "stance": "silent",
   "note": "no Pokorny entry for Skt. kāca- or kāś-."
  },
  {
   "src": "WLD",
   "where": "WLD_Bd1/Bd2_pages.txt, WLD_band3.txt grep 'kāca'",
   "stance": "silent",
   "note": "no hit."
  },
  {
   "src": "AHD",
   "where": "AHD_watkins1985.txt",
   "stance": "silent",
   "note": "no IE root for Skt. kāca- (an Indo-Aryan word with no European cognates)."
  }
 ]
}
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "kâca",
 "verdict": "confirmed",
 "derivation": "Skt. kāca- m. 'glass, crystal, quartz' (classical, post-Vedic). Buck lists it as the Sanskrit word for GLASS and tentatively links it to khac- 'shine through'. Wiktionary instead suggests a Nuristani loan cognate with kāś- 'shine'. It continues in Pali kāca, Hindi kā̃c, Bengali kāc, Malay kaca. The gloss 'pearl' comes from Mo'in's BQT footnote, which cites Monier-Williams for 'شیشه، آبگینه، مروارید' (glass bead). The word and its sense 'glass' are secure.",
 "derivation_fa": "سنسکریت kāca- به معنای «شیشه، بلور، کوارتز» در سنسکریت کلاسیک به‌خوبی گواهی شده و در پالی kāca و هندی kā̃c (کانچ) و بنگالی kāc بازمانده است. باک آن را با تردید به ریشهٔ khac- «درخشیدن» می‌پیوندد و ویکی‌واژه آن را وامی از نورستانی می‌داند. معنای «مروارید» را معین در حاشیهٔ برهان قاطع به نقل از فرهنگ مونیر-ویلیامز آورده است (مهرهٔ شیشه‌ای). وجود واژه و معنای «شیشه» درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/काच"
 ],
 "ref_check": [
  {
   "ref": "SYN:620",
   "status": "supports",
   "note": "SYN p.620 GLASS table: 'Skt. kāca-'; para 7 'Skt. kāca- : khac- shine through (?)'."
  },
  {
   "ref": "BQT:1556",
   "status": "supports",
   "note": "BQT vol 3 p.1556 (pdf 349; vision file ocr/BQT/1556.vision.txt), footnote 9 to کاچ: 'قس: سانسکریت kâcá (شیشه، آبگینه، مروارید) «ویلیامز ۲:۲۶۸»'. Mo'in gives the Sanskrit word with these meanings."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "POK_full.txt grep 'kāca'",
   "stance": "silent",
   "note": "not in Pokorny."
  },
  {
   "src": "WLD",
   "where": "WLD Bd1/Bd2 grep 'kāca'",
   "stance": "silent",
   "note": "not in Walde-Pokorny."
  },
  {
   "src": "SYN",
   "where": "p.620 §9.74",
   "stance": "supports",
   "note": "'Skt. kāca-' as the Sanskrit word for 'glass'."
  }
 ]
}
```


## [2026-10-17T00:30:56.937Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/561.jpg 2>/dev/null; pdftoppm -f 561 -l 561 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg561 && echo ok"
}
```


### [2026-10-17T00:30:57.940Z] TOOL RESULT

```
site/pages/561.jpg
ok
```


## [2026-10-17T00:31:02.317Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg561.png"
}
```


### [2026-10-17T00:31:02.757Z] TOOL RESULT

```

```


## [2026-10-17T00:31:02.754Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-17T00:31:09.752Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -A12 -E \"lemma: (i̯ā-|i̯ag-|i̯ā̆-)\" POK_full.txt | head -80; grep -n -E \"lemma: .*(i̯ā|i̯ag)\" POK_full.txt"
}
```


### [2026-10-17T00:31:10.168Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:31:13.245Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"Page\\(s\\): 50[01]\" POK_full.txt | head; grep -n -i -E \"yātu|yātú|zēlos|ζῆλος\" POK_full.txt | head"
}
```


### [2026-10-17T00:31:13.566Z] TOOL RESULT

```
40878:Page(s): 501-502 
41009:Page(s): 501 
41022:Page(s): 501
```


## [2026-10-17T00:31:16.410Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 40860,41030p POK_full.txt"
}
```


### [2026-10-17T00:31:16.881Z] TOOL RESULT

```
Note: 

labialized laryngeal h2*a- > ya- Tocharian 



gr. a^opai fayjoijai) " shy', aYiO(; "holy, consecrated' (identical with it Old Indie yajya-^to 
worship ' has been used in Vopadeva as a gerund. Debrunner GGA. 1910, 9), ayi^u) " 
consecrate, sanctify, bless; ordain'; 

Note: 

labialized laryngeal h2"a- > ha- = Greek 0a- 

Meillet (BSL. 21, 126ff., EM2 845) will connect the gr. words rather with Latin sacer 
■holy'; 

References: WP. I 195, Schwyzer Gr. Gr. I 303. 
Page(s): 501-502 

Root / \emma: Jai 

Note: 

labialized laryngeal hre- > 0e-, h3"o- > hu-, h2"a- > ha- Hittite 

labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^- 
Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 
See also: see above S. 285 {e-3) 
Page(s): 502 

Root / \emma: Jam- 
Meaning: to dig 
Comment: 
Root I \emma: Jam- {*Ja-mor-): to dig, derived from a prefixed Root / lemma: mori, mori: 

sea. 

see Old Saxon mer/m. " ditch, pond '. 

Note: {or Jem- ■.Jem- :Jdm-) 

Material: 

Note: 

labialized laryngeal hre- > 0e-, h3"o- > hu-, h2™a- > ha- Hittite 

labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^- 
Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 



Old Church Slavic y5/77a" pit, pothole' (originally anlaut/ verified through Old Bulgarian 
and through that dial. russ. hama, grown from *v-bn-Jame, *jamQ). 

Note: 

labialized laryngeal h2"a- > ya-, ja- Old Indie = ja- Slavic 

Gr. apn f. "shovel, hack, mattock, hoe', Si-apaoo "dig up, excavate, dig out', s^aijaoo, -opai " 

dig out '; apapa "ditch, trench, channel, canal, furrow', afjapsuu) " irrigate '; 

Note: 

labialized laryngeal h2"a- > ha- = Greek 0a- 

References: WP. I 198 f., Berneker444. 
Page(s): 502 

Root / \emr(\a\ Jam 

Note: 

labialized laryngeal hre- > 0e-, h3"o- > hu-, h2"a- > ha- Hittite 

labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^- 
Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 
See also: see above S. 285 {e-3) 
Page(s): 502 

Root / lemma:^^- .j6- 

Meaning: to be angry; to be punish 

Material: 

Note: 

labialized laryngeal hre- > 0e-, ha^o- > hu-, h2"a- > ha- Hittite 

labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^^- 
Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 
Old Indie ved. ya-van-^ attacker, persecutor, pursuer', ya-tar-^ avenger' , rna-ya-, -ya-van-, 
-yat-' avenging the guilt ', Old \n6\c ya-tu-m. " witchery, ghost, magic demon '; 



Avestan ya-tu-m. "sorcery, magician ', ya-sa"wish'; 
Note: 
labialized laryngeal h2"a- > ya- Old Indie 

Armenian 75/75/77' I exert myself (Meillet Esquisse^ 52); 

Note: 

labialized laryngeal h2"a- > ya- Old Indie > ja- Armenian 

Slavic *jdra- "violent' in Old Church Slavic ya/^ " strict, harsh ', jarostb "rage, fury, 
vehemency', russ.ya/}^'" irascible, irritable, gamy, violent, fiery, fast, rapid, hurried', etc.; in 
addition nsloven.ya/" envy ' (: gr. ^f|Ao(;)? Different above Berneker 28. 

Note: 

labialized laryngeal h2"a- > ya- Old Indie > ja- Slavic 

In -m- formant: 

Maybe alb. ye/777 "rage, fury, vehemency'; 

gr. ^\\KoQ„ Doric l^aKoc, m. " eagerness, jealousy, envy ' (: nsloven.ya^, ^x\i^6c, "tormenter 
', CnM'Ci. Doric lsx\x\a " punishment, penance, atonement, loss'; Ijoi^oc, "fiery, strong, not 
mixed (of wine), pure, sheer, prop, of wine without water ' (: Old Church Slavic y5/7>); 
ablaut. £ni-^ap£U); " onrush, attack, press '?; 

Note: 

labialized laryngeal hre- > Proto Greek ye- > ge- > Old Greek ze-, h3"o- > Proto Greek yo- 
> go- > Old Greek zo-, h2"a- > Proto Greek ya- > ga- > Old Greek za- 

Old Irish a(i)lid^ wishes eagerly, requests, craves', cymr. iawr command, laudation ', 
iolar\ praise, laud ', eiriolaf{*are-ial-) "I beg urgently ', abret. 3. PI. Konj. iolenV precentur 



Note: 

labialized laryngeal hre- > Proto Celtic ye-. Old Celtic ie-, h3"o- > Proto Celtic yo-. Old 
Celtic io-, h2"a- > Proto Celtic ya-, Old Celtic ia- 



References: WP. I 197, 775, WH. I 718, Schwyzer Gr. Gr. I 330, Trautmann 108, J. Morris- 
Jones, Welsh Gr. 383. 
Page(s): 501 

Root / lemma:^^- 
Meaning: ' go ' 

Note: 

labialized laryngeal hre- > 0e-, h3"o- > hu-, h2"a- > ha- Hittite 

labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^- 
Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 
See also: see above S. 296 (e/-). 
Page(s): 501 

Root / lemma:7ebh- 

Note: 

labialized laryngeal hre- > 0e-, h3"o- > hu-, h2™a- > ha- Hittite 

labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East
```


## [2026-10-17T00:31:20.812Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 40820,40862p POK_full.txt; grep -n -E \"^(yag-|yē-|yā-)\" AHD_watkins1985.txt | head; grep -n -E \"^(i̯ag|iag|jag)\" IEC.txt | head"
}
```


### [2026-10-17T00:31:21.154Z] TOOL RESULT

```
Comments: 

Root / \emma: Jag- : to worship : Root / lemma: ag- : to lead. 

see Latin ago, -0/7/5 "of the priests killing the sacrificial animal', agon/um' a victim, beast 
for sacrifice '. 
Material: 
Note: 

labialized laryngeal hre- > 0e-, h3"o- > hu-, h2"a- > ha- Hittite 

labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 

Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^- 

Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 

Old Indie yay^// venerates with prayer and sacrifice, oblation' (Perf. 0, participle /sta-) = 

Avestan yaza/feds. (participle yas/a- with lengthened grade after the present). Old Indie 

satya-yaj-' really adoring, veritable ', with zero grade //i/-/y" sacrificing regularly according 

to regulation' = ' sacrificial priest ', /jya-'to worship, revere, m. teacher ', yya "sacrifice, 

oblation'; 

Note: 

labialized laryngeal h2"a- > ya- Old Indie 

Old \n6\c yajas-n. 'worship, veneration' = gr. ayoc; n. "blame, maculation, sacrifice, 
oblation', *navaYn(; " totally holy'; 

Old \n6'\c yajna-h, Avestan yasna-m. " worship (of God), sacrifice, oblation' {yajnfya-, 
Avestan yes/7y5- 'honorable offering, belonging to the sacrifice '), gr. ayvoq "holy, pure, 
candid '; 

Tocharian A yaks-' hug, embrace, hold tight ' (Van Windekens Lexique 167f.)? 

Note: 

labialized laryngeal h2*a- > ya- Tocharian 
1182:yag-. To worship; reverence. Suffixed form *yag-yo- perhaps in Greek hagios, holy: HAGIO-. [Pok. jag- 501.]
6319:iag- ‘revere, be awed at. (Consonantism -g- or -$- obscure) Sk. yájàmi *worship'; yáje, mp. id.; Av. yaze ‘offer; praise’; OPer. yadataiy, 3s ‘worships’; Gk. házomai "be awed'
6320:iaghi, extn. of ia (2), q.v. Av. yOi-zi, rel. pn. (^who', £); Hom. hékhi "where; like’; OCz. jé-Z, as Av.; Li. jogei, jogi, jog, cj. 'that; because
6321:iaghó ‘roar, resound’. (The evidence is am- big.). Cf. iog- Gk. cf. iakhó “shout, echo"; iakhé, f. id. (but &khéo, Doric -à- is more prob. fr. suàgh-: OE swogan, q. v.); OE (also ambig.) gegan, id.
6323:iagios, -iios (iaĝ-) “holy, revered (Conso- nantism -g- or -8-. Cf. iag-) Skt. yájyah, yájiyah, yajyuh; Per. cf. yadà 'sa- crificial feast; Per. yaStan, inf. (‘pray, inter- cede’, fr. *jiagsKo) beside yazi “sacrifice, prai- se; LW in Arm. hazem “sacrifice”, v.; Gk. hágios; Tokh. B cf. yäk- “fear, be shy oP; Ir. cf. ógh (2) *holy'. Vocalism?
6326:iaghus, uos ‘dashing, swift, keen" Cf. next Skt. yáhuh, yahvah; Av. yazus ‘great, sublime’; Gk. cf. a-zékhés(?) adj. (excessive; incessant'. Px. *sm-?); MHG jac, gs jages, m., jage, sf. ‘rush, chase’; ON cf. jaga (“hunt?: Du. jagen, G id.); Mod. jagast, v. refl. ‘bicker’
6329:iagios, -iios (iaĝ-) — iãrim- (iarm-)
```


## [2026-10-17T00:31:26.295Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1180,1184p AHD_watkins1985.txt; grep -n -E \"ZEAL|JEALOUS|AGNUS|AGNES\" AHD_watkins1985.txt | head; grep -n -E \"^(ia|iā) ?\\(2\\)|^iā-|^ia \\(\" IEC.txt | head; grep -n -i -E \"^(zeal|jealous|agnus|agnus castus|Agnes)\\b\" KLN_1966.txt SKT.txt | head"
}
```


### [2026-10-17T00:31:26.614Z] TOOL RESULT

```
[xenos. Strange; stranger. Greek word (earlier form *xenwos) of uncertain origin and formation; the initial x- may be the zero-grade form *ghs- of *ghos- (see ghos-ti-): XENO-; EUXENITE, PYROXENE.]
ya-. To be aroused. Suffixed form *yd-lo- in Greek zélos, zeal: JEALOUS, ZEAL. [Pok. id- 501.]
yag-. To worship; reverence. Suffixed form *yag-yo- perhaps in Greek hagios, holy: HAGIO-. [Pok. jag- 501.]
yé-. To throw. Contracted from *yea-. 1. Extended zero-grade forms *yak-yo- in Latin jacere, to throw, lay, and *yak-é- (stative) in jacére, to lie down (< “to be thrown”), and jaculum, dart: JESS, JET?, JOIST; ABJECT,
ADJACENT, ADJECTIVE, AMICE, CONJECTURE, DEJECT, (EASE), EJACULATE, EJECT, GIST, INJECT, INTERJECT, OBJECT!, PARGET, PROJECT, REJECT, SUBJACENT, SUB- JECT, SUPERJACENT, TRAJECT. 2. Basic form *yé- and zero-grade form *ya- in Greek hienai, to send, throw: CATHETER, DIESIS, ENEMA, PARESIS, SYNESIS. [Pok. ié- 502.]
1181:ya-. To be aroused. Suffixed form *yd-lo- in Greek zélos, zeal: JEALOUS, ZEAL. [Pok. id- 501.]
1698:JAMB kamp- JANITOR ei-1 JANUARY ei-1 Janus ei-1 JAVELIN ghabholo- JEALOUS ya- JELLY gel-3 JEOPARDY yek- JESS yé-
6303:ia (2), instrumental of f. type w. adv. func- tion. Cf. io and ia (1) Skt. cf. ayå ‘thus’; Av. (ambig.) ya (‘so that’. Cf. io); Gk. cf. hé-níka, correl. of té-níka: *whenever'; Alb. cf. (elliptical ?) jo ‘no’, for *ne-ià ‘not indeed"?; Lat. ea ‘that way’; LG jo w. negative “indeed”, as in jo nich “not at all; Sw. jo, jo men ‘indeed’; OCS cf. ja-če ‘though’; Cz. cf. jo (Cindeed', fr. *iá); Li. cf. jo-8, conj. (that', fr. *ia-ghi, see ghi); Latv. jā- (debitive px. to vbs. *must-") cf. also ta-de-ja-di ‘thus. Arm. ajo “yes? seems to represent a type *oio-. Short vowel in Gk. px. za- ‘very’: Cz. jo, id.: Br. Cor. ia, ya ‘yes’; OHG, etc. ja, id.; cpd. in Gk. ē-de “and”; ëdë ‘already’: OE gjet “yet, even, also’. WP I, 312
SKT.txt:21818:Jealous.  (F.  -.  L.  -  Gk.)  M.  E.  Jal- u,  geltts.  —  O.  F.  jaious  (later  j'aJoux.) >  Low  L.  ulonu,  full  of  zeal.  —  L.  ulus,
SKT.txt:23056:jealous — EealoQS.
KLN_1966.txt:1979:Agnes,  fem.  PN.  —  L.  Agnes,  fr.  Gk.  'Ayvr(,  lit. ‘pure,  chaste-,  fem.  of  ayvo;.  See  agnus  castus and  cp.  Inez.  The  most  frequent  ME.  forms  of the  name  Agnes  were  Annis,  Annys.  Cp.  Nancy. Agni,  n.,  one  of  the  chief  gods  of  the  Vedas.  — OI.  Agnih,  ‘the  god  of  fire’,  fr.  agnih,  ‘fire’,  which is  cogn.  with  L.  ignis,  ‘fire’.  See  igneous, agnize,  tr.  v.,  to  recognize  (archaic).  —  Formed fr.  L.  agnoscere  on  analogy  of  recognize  (fr.  L. recognoscere).
```


## [2026-10-17T00:31:30.899Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"agnus +castus, n|^agnus\" KLN_1966.txt | head -3; grep -n -i -E \"^zeal\" KLN_1966.txt | head; grep -n -i \"AGNUS\" SKT.txt | head -3; grep -n -E \"^ZEAL\" SKT.txt"
}
```


### [2026-10-17T00:31:31.444Z] TOOL RESULT

```
7625:claymore,  a  Scottish  bfosflsword. ^GaeL)  Gael.  c'aUMtamk  mcr.  n  jjteil sword.  Here  ciaidheamh  is  cognate  wtili W.  deddyf^  cUddru,  a  sword,  and  with  L glAiiut  The  Gael.  mar.  great,  is  alUfld lo  W.  mawr,  L.  magnus,  great.
```


## [2026-10-17T00:31:36.385Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"agnus\" KLN_1966.txt | head -5; grep -n -E \"zeal, ?n\\.|^zeal\" KLN_1966.txt KLN_1971.txt | head -5; grep -n -E \"Zeal\" SKT.txt | head -3"
}
```


### [2026-10-17T00:31:36.751Z] TOOL RESULT

```
1979:Agnes,  fem.  PN.  —  L.  Agnes,  fr.  Gk.  'Ayvr(,  lit. ‘pure,  chaste-,  fem.  of  ayvo;.  See  agnus  castus and  cp.  Inez.  The  most  frequent  ME.  forms  of the  name  Agnes  were  Annis,  Annys.  Cp.  Nancy. Agni,  n.,  one  of  the  chief  gods  of  the  Vedas.  — OI.  Agnih,  ‘the  god  of  fire’,  fr.  agnih,  ‘fire’,  which is  cogn.  with  L.  ignis,  ‘fire’.  See  igneous, agnize,  tr.  v.,  to  recognize  (archaic).  —  Formed fr.  L.  agnoscere  on  analogy  of  recognize  (fr.  L. recognoscere).
1983:agnosticism,  n.,  the  doctrine  of  agnostics.  — Formed  fr.  prec.  word  with  suff.  -ism. agnus  castus,  n.,  an  ornamental  tree.  —  L. ;  agnus derives  fr.  Gk.  dyvo q,  ‘a  willowlike  tree,  used at  religious  festivals,  the  chaste  tree’,  which  is of  unknown  origin.  This  word  was  confused both  with  L.  agnus,  ‘lamb’,  and  Gk.  ayv6?, ‘sacred,  chaste’,  whence  arose  the  name  agnus castus,  prop,  ‘the  chaste  lamb’,  and,  as  a  loan translation  of  this  latter  name,  G.  Keuschlamm, and  E.  chaste  tree.  For  the  etymology  of  castes see  chaste.  Cp.  the  second  element  in  Elaeagnus. ago,  adv,  — -  Prop.  pp.  of  ME.  agon,  ‘to  go  away’, fr.  OE.  cigdn,  ‘to  go  away,  pass  by’,  fr.  intensive pref.  a-  and  gan,  ‘to  go’.  See  go. agog,  adverb  and  adj.,  in  a  state  of  excitement.  — F.  en  gogues,  ‘mirthful’.  Cp.  etre  en  goguette(s), ‘to  be  on  the  spree’,  goguenard,  ‘mocking,  ban¬ tering’.  All  these  words  derive  from  *gog-,  a base  of  imitative  origin.
2227:‘to  burn’ ;  cp.  kali.  The  word  alkali  first  appears in  the  writings  of  Albertus  Magnus  (i  2o6?-i  280).
5496:brachy  cephalic,  also  brachycephalous,  adj.,  short¬ headed  (anthropometry).  —  Formed  fr.  brachy-, Gk.  xetpaXf),  ‘head’  and  suff.  -ic,  resp.  -ous.  See cephalic.  Cp.  Gk.  [3pxy;jx£?x X05,  name  of  a  fish, lit.  ‘short-headed’.  The  word  was  first  used  in anthropometry  by  the  Swedish  anthropometrist Magnus  Gustaf  Retzius  (1842-1919). braehylogy,  n.,  a  concise  phrase  or  expression, brevity  in  speech.  —  Gk.  ppayvXoyix,  'brevity in  speech’,  compounded  of  ppayu;,  ‘short’,  and -Xoyii.  fr.  -koyo?,  ‘one  who  speaks  (in  a  certain manner);  one  who  deals  (with  a  certain  topic)". See  brachy-  and  -logy.
6561:carline,  n.,  an  old  woman  (Scot.)  —  ON.  ker- ling,  fern,  of  karl,  ‘man’.  See  carl  and  cp.  Carl, Charles.  Cp.  also  carting, carline  thistle.  —  F.  carline,  fr.  ML.  carlina,  for cardina.  fr.  L.  carduus,  ‘thistle’.  See  card,  ‘ma¬ chine  for  combing’,  and  cp.  words  there  referred to.  ML.  carlina  was  influenced  in  form  by  Char¬ lemagne  ( Carolus  Magnus),  with  whom  this plant  was  associated  by  legend, cariing,  n.,  one  of  the  timbers  running  length¬ wise  (naut.)  —  F.  carlingue,  fr.  ON.  kerling,  lit. ‘an  old  woman'.  See  carline,  ‘an  old  woman’. Carlovingian,  adj.,Carolingian.—  F.  carlovingien, a  blend  of  carolingicn  and  merovingien.  See Carolingian  and  Merovingian, carmagnole,  n.,  t)  jacket  (worn  by  the  French Revolutionaries  in  1793);  2)  a  revolutionary dance.  —  F.,  fr.  Carmagnola,  name  of  a  dis¬ trict  in  Piedmont,  Italy.  The  word  orig.  denoted a  coat  worn  in  Carmagnola  and  brought  to France  by  workmen  from  Piedmont.
KLN_1971.txt:234559:zealous’, fr. studium. See study, n., and -ous. 
KLN_1971.txt:270330:zeal, n. — ME. zele, fr. Late L. zelus [whence also 
KLN_1971.txt:270340:zealot, n. — Late L. zeldtes , fr. Gk. 
KLN_1971.txt:270346:zealous, adj. — ML. zelosus , fr. Late L. zelus. See 
KLN_1971.txt:270347:zeal and -ous and cp. jealous, which is a doublet
```


## [2026-10-17T00:31:44.269Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in 92 95 252; do echo \"== HRN $p\"; awk -v n=$((p+21)) 'BEGIN{RS=\"\\f\"} NR==n+1' HRN.txt | grep -n -i -E \"jād|jadu|ǰād|ja[sš]n|yazd|izad|īzad|yās\" | head; done; echo == HUB107; awk 'BEGIN{RS=\"\\f\"} NR==118' HUB.txt | grep -n -i -E \"jād|ǰād|yās|jāδ|jadu\" | head"
}
```


### [2026-10-17T00:31:44.808Z] TOOL RESULT

```
Exit code 1
== HRN 92
== HRN 95
== HRN 252
15:,J^o. ^ aw. yazatanqm; phlv. yaztün, yazdän , yaz<i\d\n
17:yazdaii (Bücher); vergl. ~ized (No. 141).
(eval):1: = not found
```


## [2026-10-17T00:31:49.378Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^ *[0-9]+\\. *(jädü|jâdû|jädu|jadü|jädü|ǰādū|jasn|jaśn|ja[sš]n|izad|ized|yäsa|yäse)\" HRN.txt | head; grep -n -E \"Zauber\" HRN.txt | head; grep -n -E \"jaSn|jaSn|jasn|ja.n .Fest\" HRN.txt | head"
}
```


### [2026-10-17T00:31:49.839Z] TOOL RESULT

```
1641:141. ized 'Gott', vergl. yezdan (No. 1127).
3856:410. JädU 'Zauberer, Jadül.
3856:410. JädU 'Zauberer, Jadül.
3857:aw. j/ätu- 'Zauberer'; i^hlw. jatuk, jatükih, arm. LW.
10715:Tomaschek stellt wa;^. mutr 'Zauberspruch' dazu;
```


## [2026-10-17T00:31:54.881Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1641,1650p HRN.txt; sed -n 3850,3866p HRN.txt; grep -n -E \"^ *1127\\.\" HRN.txt; grep -n -E \"Fest\" HRN.txt | head -5; python3 - <<'E'\nt=open('HRN.txt').read().split('\\f')\nfor i,p in enumerate(t):\n    if '410. J' in p or '141. ized' in p or '1127.' in p: print(i, i-21)\nE"
}
```


### [2026-10-17T00:31:55.300Z] TOOL RESULT

```
141. ized 'Gott', vergl. yezdan (No. 1127).
aw. yazata-; phlv. yas^d (Münzen), vergl. Izates
(N. pr.); ai. yajatd-,
oss. LW. izäd 'Engel'.
emä Vir (jüd.-pers.) s. ma (No. 955).
142. ^n 'dieser .
ai. ^na- 'ihn' etc. (EncL); päz. in (phlv. H^T).
evän 'Vorhalle, Palast* s. unter np. Iä7i 'Haus*
(No. 175).
B.
phlv. HTl (oder wie man transcribiren mag) — vd.
3 (121) == aw. tiyra-y und häufig im Bund. — soll
vielleicht tey sein. Np. tey 'Berggipfel, Höhe', oss. fty,
d. feyä 'Bergrücken (250) gehören ebenfalls hierher
(spezialisirte Bedeutung: Spitze eines Berges).
J.
410. JädU 'Zauberer, Jadül.
aw. j/ätu- 'Zauberer'; i^hlw. jatuk, jatükih, arm. LW.
jatuk; ai. yätü- 'Spuk, Hexerei; Spukdämon'.
411. Jäm 'Glas, Becher'.
aw. yama- 'Glas' ; phlv. jatn bezw. yäm (auch für aw.
gao.zasta-, vd. 3 (4)).
Reimt auf /er« fSahn. I, 22 Vers 35), /ere^gr* (Sahn. I, 78 Vers
307). Mit aw. ^afra- (Justi; auch noch Geiger, ZDMG. 37, 130) hat
np. tere nichts zu tun, vergl. Bartholomae, KZ. 29, 287.
-) Das s statt z ist von np. tes (No. 387) bezogen.
*) Bartholomae, Altiran. Verbum 105; zur Form vergl. Studien
964:warf (?) (sie zu Ekbatana in die Festung)*, d. i. 'ich setzte
2270:215. bezni *Fest'.
2502:vi + k^ dhä' , vergl. ai. vidhdna- 'Ordnung , Fest-
3938:422. JeSn 'Fest, Gelage* »).
6566:753. sür *Fest, Gelage'. •
54 33
113 92
342 321
350 329
363 342
```


## [2026-10-17T00:31:59.981Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3938,3946p HRN.txt; python3 - <<'E'\nt=open('HRN.txt').read().split('\\f')\nfor i,p in enumerate(t):\n    if '422. Je' in p: print('422 page', i-21)\n    if 'yazatanqm' in p: print('yazatanqm page', i-21); j=p.find('yazatanqm'); print(p[j-600:j+300])\nE"
}
```


### [2026-10-17T00:32:00.307Z] TOOL RESULT

```
422. JeSn 'Fest, Gelage* »).
*) Im FJ durch einen Vers Euveri's belegt. Häufig im Sähname.— 95 -
aw. yaswa-; i^hlv.jfasn bezw. yasw Test* (West, Pahl.
Texts I, Lxxm).
Salem ann, Mel. asiat. JX, 236.
423. Juy *Joch', vergl. yöy.
Käs. yü (Qohrüd).
ai. yugd" *Joeh\' arm. lue *Joch* (H. No. 129).
kurd. jülc (H.-Sch.), vergl. yüzen *der das Joch am
422 page 94
yazatanqm page 252
```


## [2026-10-17T00:32:04.585Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==274' HRN.txt | grep -n -B4 -A6 yazatanqm; echo ===HUB; grep -n -i -E \"j[aä]d[uü]|jätu|jatuk\" HUB.txt | head; grep -n -E \"ja[sš]n|jasn|ized|yazd\" HUB.txt | head"
}
```


### [2026-10-17T00:32:04.900Z] TOOL RESULT

```
Exit code 1
11-päz. yah (L 19)^).
12-kurd. aty. LW. ye/; oss. d. ye/, t. Jx Eis, Hagel'
13-^ (148); wa/. yi/.
14-'il27, yexdan 'Gott*.
15:,J^o. ^ aw. yazatanqm; phlv. yaztün, yazdän , yaz<i\d\n
16-^{^y""'"" (Gemmen, Hörn, Mitteilungen Heft IV, 24 No. 2),
17-yazdaii (Bücher); vergl. ~ized (No. 141).
18-V4128. yek *ein*.
19-X Kä^- V. yav, ikt, Q. y, l, ik.
20-C"--' ap. ^aivaka-, vergl. am/- 'ein'; aw. a^oa-; phlv.
21-rwak, ev, phlv.-päz. yak (PPGL), ai. eka-,
(eval):1: ==HUB not found
```


## [2026-10-17T00:32:08.513Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo \"-- HUB\"; grep -n -i -E \"j[aä]d[uü]|jätu|jatuk|410\\.\" HUB.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==118' HUB.txt | head -60"
}
```


### [2026-10-17T00:32:08.851Z] TOOL RESULT

```
-- HUB
292:bazU, JUdU^ zanU^ arm. LW. bazuk, jatuk.
5271:a) Ap. y im Anlaut = np. j in : jadu *Zauberer* = zd.
5393:gauba- (ZDMG. 46, 325); Jatuk 'Zauberer (5. Jhd.) = np.
5394:Jadu^ zd. ydtU' ; julhak Weber (modern) = np. Jolahj Jdldha
8629:berer = arm. jfatuk, phi. jatuk, zd. yatu-; ahu 'Gazelle'
8694:pi. bazuvdn; jadu 'Zauberer, ip\. jaduvan = ipsiz. jadvan
8695:Min. kap. 49, 16 = phi. jatukan Phi. Min. 52, Z. 12; Jmdu
— 107 —
yat Yatk. i. Zar. 57, 59, West, PT. II, 137, Bdh. Gl.
173, Dink art V, 19, arm. Spandiat Sebeos 30,
Aspandiat Mos. Kalank. I, 372, 378, 382—384 .-=
zd. speutodata-, gr. S^fFi'daddzfjc {Kte sis. s).
1123. Np. ya«a = ph.*i/asak setzt zd. ap. ^yfl^r/- voraus.
1st ayasa richtig und die altere Form, so ist eben
*ayasa anzusetzen und eine andere Etyniologie zu
suchen.
1124. Np. yabam, yaftan — paz. ayaftan setzt eine Wrzl.
yap oder ydbh, osset. ydfin wohl yaph voraus?
1124^*'* Die Bedeutungen passen nicht zusammen. Das
Wb. hat auch ein unbelegtes ydn 'iumentum, vehi-
culum' = skr. yana- 'Wagen, Vehikel' (Vullers) =
afgh. yun gait, movement, carriage, habit, custom*
(Geiger)?
1125. Darmesteter iibersetzt yavarena- durch moulin a
ble* nach der Tradition , deren jurtak drd ('Getreide-
Mehl') aber auf schlechter Etymologie beruht.
1129. Np. yd» *Jagdleopard' = arm. yovaz kann nicht zu
arm. yoiz-k 'Suchen* etc. (vgl, np. razmyoz Kampf-
suchend*) geh5ren.
Das hier fehlende np. y6y *Joch' (= skr. y^ga-^
bal. j(iy) siehe unter juy Nr. 423.
```


## [2026-10-17T00:32:13.424Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *1123\\.\" HRN.txt; n=$(grep -n -E \"^ *1123\\.\" HRN.txt | head -1 | cut -d: -f1); sed -n \"${n},$((n+8))p\" HRN.txt; grep -n -E \"Zauber\" HUB.txt | head -3; sed -n 5268,5274p HUB.txt"
}
```


### [2026-10-17T00:32:14.130Z] TOOL RESULT

```
9700:1123. yase (eyase) *Wunsch, Begierde'^).
1123. yase (eyase) *Wunsch, Begierde'^).
aw. *ayäs((k(i' 'Wunsch, Begehren', vergl. d -| yäs-,
yäsanuha 'wünschen, verlangen*.
1124. yäften 'erlangen, erreichen, erfinden*, Praes. yah-em,
..-\*^'' ••i:5n^ (Jer. 2, 24).
aw. vergl. ayapta- 'Belohnung; phlv. äyäftan
(Yasna, Spiegel, Trad. Lit. 439), yaftan (Bund.),
vergl. äyaft,
oss. d. ba]yafun, t. ba]yafin einholen, erreichen'
4453:xah = xoh 'Speise*, kaxard 'Zauberer = zd. kax^areda-.
5271:a) Ap. y im Anlaut = np. j in : jadu *Zauberer* = zd.
5393:gauba- (ZDMG. 46, 325); Jatuk 'Zauberer (5. Jhd.) = np.
Kapitel 8: ap. y.
§ 39. Ap. y (= idg. y) = phi. y wird im Anlaut meist
zu paz. np. j, bleibt aber in einigen Fallen als y.
a) Ap. y im Anlaut = np. j in : jadu *Zauberer* = zd.
yatu"^ jam *Glas, Becher = zd. yama-; jama *Kleid', vgl.
Ifoiiia, WZKM. ,8, 93 ; javBd *ewig', zd. yavaetat- ; juda ge-
^) Man umsohreibe also ap. barantiy, abaram, aber pto. brta-;
```


## [2026-10-17T00:32:18.974Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^(jādūg|jadug|jäduk|jädüg|jädug|yazd|yazad|jašn|jasn|Yazdgird|yazdgird|yāsag|ayāsag|āyās|yazišn|yašt|yaz-)\" PHD.txt PHD_mackenzie.txt | head -20; grep -n -i -E \"jādūg|yazdgird|ayāsag|jašn\" PHD_mackenzie.txt | head"
}
```


### [2026-10-17T00:32:19.370Z] TOOL RESULT

```
PHD_mackenzie.txt:5701:yaz-, ......isn, v. yastan.
PHD_mackenzie.txt:5702:yazd [y;-dt l I M yzd, N ......] god, divinity.
PHD_mackenzie.txt:5703:yazdah [y)cdh I M y)zdh, N ......] eleven.
PHD_mackenzie.txt:5704:yazdan (Y;-d)n ] (pl.) gods, spirits.
PHD_mackenzie.txt:11050:yazdan                          \~
```


## [2026-10-17T00:32:23.239Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^(jad|ja.u|jas|ayas|ayās|äyas|yast|yašt|yazdag|yazis|ayaz)\" PHD_mackenzie.txt | head -20; grep -n -i -E \"sorcer|wizard|feast, |festival\" PHD_mackenzie.txt | head"
}
```


### [2026-10-17T00:32:23.566Z] TOOL RESULT

```
3033:jad [y't l ] share, portion.
3038:jadag [y'tk I M j'dg] share, portion; case, cause.
3040:jada~-~i}(w) [y'tkgwb ] advocate, intercessor.
3044:jadArih [yt'lyh] maintenance.
3049:jadii~ [y'twk l I M j'dwg, N Jadu] sorcerer, magician.
5695:yast (yst l I = M] prayer, worship.
5696:yastan, yaz- [Y!2BHWN-tn' < Aydbfzwn, .y dbfz; ,'ftn l , yc- I M yz-]
2342: Frawardigan [plwltyk)n l I N farwardagan] festival of the frawards, the
2425:    festivals celebrated at the ends of these.
3049:jadii~ [y'twk l I M j'dwg, N Jadu] sorcerer, magician.
3050:  ....,ih: sorcery, magic.
3068: Jasn [yln l IN....,] celebration, festival.
4304:rad-passag [ltps)h l ] ceremonies of the giihanbiir festivals.
4712:lsur [swll M swr, N -] meal, feast, banquet.
5426:wistardan                        92                        wizardan
5479:wizardan, wizar- [we'l-tn l I M wye,rd, wye'r-, J bz'rd-, N guziirdan]
5482:wizard - wars                     93                              xan
```


## [2026-10-17T00:32:28.659Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"yazdg|yazdk|izad\" PHD_mackenzie.txt | head; sed -n 5694,5700p PHD_mackenzie.txt; grep -n -i -E \"^(yātūk|jātūk|yatuk|ǰātūk|jātuk|yazd|yazdān|yašt|yazišn|jašn|yašn|ayāsak|āyāsak|yāsak)\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-10-17T00:32:29.125Z] TOOL RESULT

```
1404:izAd [JcJ t ' I M uzJd, N ......] I. noble; 2. free.
1405:izAdih ['eJtyh] I. freedom; 2. gratitude, thanks.
11505:afsudan                 \\,0 I"'U ~        iibiid, iizad                \ l"e.,)'   cua
yasn [ysn l I = M] adoration, worship.
yast (yst l I = M] prayer, worship.
yastan, yaz- [Y!2BHWN-tn' < Aydbfzwn, .y dbfz; ,'ftn l , yc- I M yz-]
     worship, celebrate, recite.
 ",isn: worship.
yat [y)t l = Av. yata-] a degree of sin.
p yawed(an) [y)wyWn)1 I P y)wyden)] always, eternally.
4415:yašt [ySt'] worship, invocation, religious ceremony 6519, 7019 ( u niyäyisn u īzišn u azbäyısn) ; 1005-14-17 ete, passim; v. also yast-fravahr. — Borrowed from Av. (1280) yašti-.
4416:yaštan [yštn'; YZBHWN-tn'] yaz- [yc-] to worship; to perform or conduct the religious service: magvé-mart ke Gp u ātaxš 1 Vahräm yazend u pahrécénd 20°; den — to perform worship according to the (Mazdayasnian) religion 11525-26; fräc én $ man yaz! conduct the worship (the prayer) for me! (replacing me, who ought to do it myself, being the father of the family) 535, v. the whole episode 531-15, — Av. (1274sqq.) yaz-; MPrs pres. yz-,
4421:yaštār [yšt'l] worshipper, he to whom it belongs to perform religious service 5314; patiš (= pat den) varzitar u ~ bütan 6311-12 cf den yaštan (v. above). — Av. (1280) yastar-.
4422:yašt-iravahr [-plw’hl] he whose frava& is worshipped, of deceased holy men; of Zartuxšt 1115-9. — yašt < Av. pt. yašta-; v. fravahr.
4431:yātūkēh sorcery, witchcraft, gl. to apé- dāt (g. v.) 3716,
4432:yātūkihā through sorcery 4819,
4440:Yazdēkirt [yzdykrt'], Yazdkirt [yzdkrt'] Sassanid king (Y. I, son of Shapur III, 399-420) 114". 1158-7, 116'9. 117!9. — Cf MPrth yzdygyrd ‘divine’; Arab Yaz- dajird.
4441:Yazdekirtän, Yazdkirtan,
4451:yazišn [ycšn'] performance of religious service, worship, sacrifice 5314. 959." eto. passim. — V. yastan.
```


## [2026-10-17T00:32:33.244Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4423,4450p NYB_vol2_glossary.txt; grep -n -E \"^(jašn|yašn|ašn|āyās|ayās)\" NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:32:33.639Z] TOOL RESULT

```
yāt [y*t'] share 982-4, — Av. (1283) 'yāta-; Ps. yty ‘heritage’; MPrs 2’dg (A-H II). V. also ydt-angok.
ya0ü-ahü-vairyó [yt?k ’hwkwylywk] the most holy prayer of the Zoroastrians 58?. — V, Benveniste IIJ I, 1957, 77-85.
yatak [ytk'] form, shape: ~ % névak good fortune 1138; ~ vihiréh change of form 109°, in the Aristotelian physics uetaoxnuatiots, Bailey, ZP 82 and n. 5. — According to Bailey derived from Av. (1262) yam- 'to hold, to sustain'. [The SW form *jatak is found in MPrs ždg, which only oceurs in the expression ždg y hwm’ywn  "humalike shape’ of a bishop (A-H II, with unsatisfactory ex- planation). Hence hwédg ‘of good shape’ = uaxdpıog (A-H II), exactly correspond- ing to MPrth hwydg in the same sense (A-H III, MHC), which accordingly is to be read huyadag and not *huvidag as did Henning, comparing OInd (RV) suvita- < su + ita- — a typical ““Routine- Etymologie", to use the expression he himself coined.] — V. also yat-o.
yütango(k) [y’tngwk] solicitor 70%, — Paz. jädangö; < *ydtana- = *ydta- (v.s. v. yāt) + go < gov from guftan (-k is spurious, ef. s. v. z"étodàt). Commonly yätak-göb from yātak = yät; Arm. lw. jatagov (Hbschm.).
www.parsianjoman.org | Col )b
yat-ó
yat-6 [yt’w'] (Prth) till until 272, — MPrth yd ^w or yd alone, v. Henning, List 89; BSOAS XII, 1947, 52. I cannot accept any of his etymological attempts. In my opinion, yat < yatam*, pt. of yam- (v. s. yatak), ‘held on’ (ava ‘to’) used adverbially, cf Hom. oys8óv (from Eyw) + gen. ‘close by’. Cf yumē.
yütük [y’twk'] sorcerer, wizard, of the enemies of the Zoroastrian religion, pas- sim; pl. eas. obl. —-än 46%. 5018, 8721, 9027; sorceress 10°; sorcery 4374. 447, — Av. (1283 sq.) yätu-; Paz. jädu; NP jadi.
yātūkēh sorcery, witchcraft, gl. to apé- dāt (g. v.) 3716,
yātūkihā through sorcery 4819,
yavar [y’wl; Prs inser. y'wly] time, oc- casion: pat hän ~ ka on the occasion when P1:2; fratom ditikar u sitikar ~ first time, a second time, a third time 4617-18; —-& [y’wl + 1] once and for all 1016. — MPrth y wr; MPrs Zr (A-H II), jr (BBB); Paz. jävar; < *yäva-vara-, v. next w.
yāvēt [y"wyt'; inser. y’wyt] perpetuity: yat-6 róc ~ for all time, in perpetuity 2728. — P2:5-6 read 'nwšky (6) wy’wyt štly = anēšaky (6) u yāvēt-šahrv immortal and with eternal rule (bahu- vrihi; thus justly Frye, AO XXX, 1966, 86; clear on the photograph of Professor Luschey; my reading was that of Herz- feld, who put at my disposal a photo- graph of small size and his own tran- script; the correct reading was con- firmed on my personal visit to the monument 16. 10. 1971). — MPrth y^wyd in the expressions ^w ywyd ywyd and ^w y^wyd y’wyd’n (S), yem ywyd y’wyd’n (A-H III, BBB) ‘in secula seculorum'; Av. (1264 yav- and 1266 yavaētāt-) ya- vaēca yavaētātaēca id.; yāvēt < the nom. *yāvaitās from *yāvaitāt- (in Av. shorten- ing of -āu- > -av- and -āi- > -ay- before a vowel is the common rule). NP jāvīd.
226
.yazet
yāvētak eternal: nām i ~ 95,
yāvētān perpetual, eternal: ~ rēcān in eternity 272°. - MPrth y^wyd?n, ^w y’wyd’n ‘eternally’; MPrs Z’yd’n (S, A-H II), j”yd*n (BBB); Paz. jāvada (SGV); NP jüvidàn.
yāvētānakān for all eternity 103?9, yazdān [yzd'n'] v. yazet.
Yazdēkirt [yzdykrt'], Yazdkirt [yzdkrt'] Sassanid king (Y. I, son of Shapur III, 399-420) 114". 1158-7, 116'9. 117!9. — Cf MPrth yzdygyrd ‘divine’; Arab Yaz- dajird.
Yazdekirtän, Yazdkirtan,
preceding name: Vahräm 114%. 115°. 11733.
patr. of the (g. v.) z —
yazet [Prs inscr. and Ps. yzdty, BP yzdt'], pl. cas. obl. yazatān [yzt’n] HajB: 2. 4, commonly yazdän [inser. yzd’n, BP yzd?n'] Prth yazatān [y?ztn] HajA:3.4. SPrth 5.7.12, god: Atur ~ 252; Gosurvan ~ 3476-27; Nerösang ~ 60°; Mihr ~ 961; hin ~ (se. Zartuxst) vànom 61°; ~ a god, or possibly already (as in the Ps.) God 11918; — ~ as pl. cas. rect.: hamak ~ 104* (together with pl. cas. obl. amah- raspandan and martomčin used as pl. cas. rect.); — pl. cas. obl. yazdan (ete.) a) gen., often placed before its subst.: pat yazdan hayyäreh 314-15, 121* (but pat hayyd- reh i y. 50%); yazdān xvēš hom 6219;
. i yazdan, passim; — b) dat.: yazdan u Sähpuhry xūp sahät it may seem good to ... P 2: 7. 8-9; api-š kämak ... apürik yazdän it is the wil ... of the other gods 5911; — c) after prep.: andar yazdän 172, 70%; apāk mēnē- yan yazdän 7418, 7922; pat yazdan 841’; hac yazdän inser. passim; — d) agent: 38?. 459. 5517, 10311; — e) instead of cas. rect. pl. 3417. 8815. — Borrowed from Av. (1279 sq.) yazata-, hence the irregularities of the forms: yazét cf Syr n. pr. Yazid- panüh; NP izad < yazad, cf izišn < yazisn. MPrthPrs yzd, pl. yzd?n.
WWW .parsianjoman.org | oe ww
(Yaz)et-yad
227
yuvat-sritak
(Xaz)ét-yüd n. pr. of the scribe of P 1, v. l. 12. — “Worshipper of the god": -yad from yad-, the SW form of yaz-, v. yastan.
```


## [2026-10-17T00:32:40.502Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^(yätu|yātu|yāsā|yäsä|yesnya|yesnja|yaz-|mazdayasna|mazyah|masyah|frāyah|fräyah|kasyah|srayah|sraiiah)\" BRT.txt | head -20; grep -n -E \"Zauberei|Zauberer\" BRT.txt | head -5; grep -n -E \"Wunsch\" BRT.txt | head -8"
}
```


### [2026-10-17T00:32:41.058Z] TOOL RESULT

```
2563:mazdayasnaA^V.iO.iz:  -    hä  'U  y^ska\^^^^^  I„f_  vorausweisend;  'tat  dim..daz. H^  ¥.5.48;  -yava^  'tea»h>m  F.^c;  j    ^  ^^j_j  _  _  ^^^^,,.  ^urahi mainyiui  V. \.iij.i-,-  —ga,ri,masoaaho'takeV.s.^    /  ^^  'dann,  alsdann':  ^rUum  bar^
2600:yätumantJhe  jasaiti  •'.  .  der  verfällt  in  die  's^'"   ^■'0^'>;    —  .la/  t,f  sra-.a  dr?n-j;.\in
13176:yesnya  AauniaiiA.)  *daiaiti  N.J7;  P.,J2;
19882:yäsä  (sA)  *'inySui ..  spmtakyä  ..  ^yao%anä Y.  28.  i'\  a)  mit  vanAav-  konkret von  dem,  des  Geist,  Sinn  gut  ist,  in  koU. Sinn:  *°inySuUä  *var3hSus  vlsfä  data spintahyäca  nsrsi  syaohana  . .  Jiairigaiig (sd.)  y.  34-  2'>.  2)  im  jAw.:  oAmäi rtaetnäi  ,  .  yahmäi  .  .  mihrS.drux^  na^a Hnyu  faiti.faite  Yt  10.  19;  —  mit  sptrUa-. spmtat  haia  °nyaoi..aihm  Hhnm  FrW./o. 40.  n)  'Geist'ahBezeichnungunkÖrpei- licher  Wesen;  I)  von  dem  Geist  Verstorbe- ner; nur  im  gAwr.:  yahrä  'inyu^  dngvats anqsat{Sg.io^^  o.) par3  Y.^.j.  2) von Gottheiten;  a)  im  gAvr.;  mit  spsnista- von  Asa,  Arm.,  VM. :  at  ahura  h)S  'inyUm iara%ui^trS  v?rmif(sd.)  miuda  yasß  Hscä sfSnistö:  aäm . .  armaitii . .  vohä . .  manatifiä ^.43-  i6j  —  voaAitart  Stars  vsi  ahurahya masdh  ahT  'myuS  vSi  (sd.)  ahyä  sjifniits aMY.s6.3;  —  oAyä  Swa  a^rs  (Sp.iisu.) varPiärUl  . .  pairl.jasSmaidl . .  %wä  ^wä 'inya  spsnii'ta  Y.36.1.  b)    im  jAw.,
21411:yaz-
21412:yaz- I 3
21444:yaz-  n
21445:yaz-  Noten
21547:yätumant-
2601:Strafe  dessen,   der  sich  mit  Zauberei  be-  >'"'    paoun-a    'pataio    dnnjayan  V.  4.^5:
20010:*)  Wenn  300  Jahre  vom  Millennium  des UxsyiUjnta  vergangen  sind,  wird  dei  Zauberer M.  durch  Schnee  und  Kälte  in  drei  J&hren  fast die  ganie  Menschheit  Temichten.  Dann  soll Yima*  Vor  (sd.)  ge&fTnet  nnd  10  die  Erde  neu bevölkert  werden:  worauf  das  Millennium  des l/xiyal.nimaA  beginnt.  Vgl.  SBE.  4^.  9,  108, rS.  1Ö9,  479,  DST.  ZA.  a.  19,  SÖDERBLOM  La vie  future  iSi  nnd  tu  ir/a-  No.  i.
21546:•  j.  yätav-  -.y-ihw-  ra.  i)  'Zauberei,  Be-I hexung*:  •'hwa  (IS.)^a?S-ä  aiahe  mtrr/tntt V.  8. 3.         3)  'Zauberer',  d.  i.  der  durch '
21566:KampA.;  Ableit.  —   %\.  yäliv-  m.  'Zauberei;
21567:Zauberet';  n-p.  Jädü  'Zauberer'.  —  Pü.  (zu  I
2783:xaA/rä  (frö)  i) 'forteilen,  entweichen': ,  Y.  43. 7;  —  kyat  '^wH  xsayqs  {^A^  °hm s.  Ini./rasstö.  2)  'zum  Forteilen,  Weichen  \dy,il  imavanitm  "weil,  wer  es  vermag, bringen":  tia^a  eil  raSva  masya  /«/«/'  deinen  des  mächtigen  Wunsch  erfüllen nasoa  fraeiyeiti  "kein  .  .  vermag  (ihn)  zu  möchte"  Y.4j.  ro";  ■ —  "Ü!  *kasu.draonö töten  noch  zum  Weichen  zu  bringen"  Vt.  (sd.)  jn^a  a^rava  V.J.  45. t4Z^-       3) 'impellere,  anspornen,  dringen      KompE.  —  Zum  V.  a-j-;  aus  ar.  »iwi/a- ;  vgl.
4054:Ableit.  —  Eig.  'der  beim  (zum)  Gegenstand seinesWunsches(gelangtlist''.— Pü.!fljafiin(?). --  I)  Zum  o  s.  S  ^94  Nlr. «  j.  afraslh'vant-,  äfrasäh'vant-  Adj. (fem.  'vaili-)  'den  Wunsch,  die  Hoffnung erfüllend,  selig  machend':  a/f«  .  .  afra- satihaitim  V.  52.  i.  a)  mit  Dat  comm.: dsyh  ml  Stars  puhra  ahurahe  mazd$  yS
4056:ml    atfhat    afrasätphä  .  .  vaAishm  ahlim "verleihe   mir,  o  ^.,    Sohn   des   AAM., womit    er  mir  den  Wunsch  erfüllen  soll, das  Paradies  . ."  V.62.6. Eig.  "beatum  (beatos)  babens'  sva.'reddens'').
6083:tl  cü  asra^fyanatn  tanunqm  'iahe .  .*vToiliti P-'i"**;  —  ndit..  "iahe  nöii  asayä  fräSmti (sd)  P.4J;  —  nöit  he  gäul  bvcU  nßit  'um oMt  "raola  ndit  vahUtö  ankui  Y.40;  — ahuräi  masdai  . .  yaihe  gäus  yetihe  °hm ye^ke  raolh  Y.i2.  i;  — ■  ä  vahiliaf  atfhaot d  vahiitj/  -iat  ä  vahistaiibyö  raolsbyS  Y, /p.  6;  —  sara^uHrahe . .  paoiryäi  hanka- nuie  gqmca  '/pmca  Yl  13. 88;  —  vahilbm 'snn  .  .  vaMitqm  Jstlm  (sd.)  yazammäe yqm  'Iahe  vahistahe  Vr.  2j.  1;  —  ya^aea ttajenie  asaom  'sim  HnasH  (sd.)  V.  20.  3; f^K  Anhang  zu  II  und  HI.  Ein  be- abdchtigtes  Spiel  mit  den  Bedeutungen leigt:  '!»n  vohB  vahisttm  astt  usta  astl «Al  ahmai  hyat  °iai  vahiMi  'hm  "A/a (Bcd.  n,  III)  ist  das  beste  Gut;  nach Wunsch  wird  es,  nach  Wunsch  uns  zu  teil, das  Asa  (Bed.  III)  fUr  das  beste  A/a (BeAn)"Y.27.i4-'').  A)  als  Gottheit {A»ui'a  Sfijnta*i).  i)  im  gAw.:  '&m  .. vahiibm  . .  hyai  srazll?m  kyat  sptntim awuirm  Y.^-j.^;  —  aää  (sd.)  tasä  gSus^ P^nsal  *hm  . .  ahmai  'lä  (als  Subj.)3> paiajnravat    Y.  29.  af;    —   yä    töi    '.
6678:■Wunsch':  ya'>:a  tt5  httham  (sPKPfA.)  .  .
7288:Zam  V.  ap-.  —  ai.  'äpana-  n.  —  Pü,:  am  fa fsäa  p»rr  hati^äril  t'imak  "damit  füllt  meinen Wunsch  voll".  —  ')  D.  i.  dadurch,  dass  ihr  | sie  es  erreichen  lasst.
7339:*vana-  n,  'Wunsch',  «um  V.  fvan-;  ai.  vaiia- n.  —  mp.,  np.  äj'nn  (aus  *ä/riuan').  —  l'u, (zn  Y.):  äfrm  i  iäliil.  —  ■)  Der  selbe  Aus- gang noch  in  *Aa%rSiaribi}.
7883:1)  'hin  zu  gehen  zu -',  mit  Dat. ■>  (statt  ,_(,aj«,j,-  Vr.;5.2;  V.jff.i^s'  (wo  "0,7),  2;. Akk.):  husiti  ..  äanyuMti  (sd.)  ite  vJse  (,^  Yti-agS;  —  aim  mSt  'äS  iw/y  (sd.) afrXnümi  yahmat  haca  . .  ".  .  in  (dessen) ' yj  „5  a?i-ö  . .  Y.  2(J.8;  —  iv//tt  -ö«  . .  hvar- Haus  zu  gehen,  von  dem  .  .'■  ^.6S.^lt)m  lyaoi:ni>m  S-s^i^i; —ya>a  yat '<.a 14.  a)'einzugehenauf-':iJOTff^^ä^W/|ana/rj'rf  daiühus  hakat  m^a  us./raraysil moi  data  danga/tya  *yaoi  ySm  vä  *nagas  (sd.)  YL  75.68;  V. 5.56,  y.55;  —  ime  nö däfMt  its  vairya  stdt/isd.)  "..ihn  sollt  ihr|.  .  aspa  para  *miira  *'c,a'>  iiaymU  (sd.) mir  gewähren,  auf  den  einzugehen  keiner  yt.io.  42;  60;  —ha  hl  asti  ä>a  ..aipi.- euch  zwingen  kann,  (den  Wunsch) .."  Y.  panmnäi  'oa  aSaone  V.Ä107;  —  ktj'M 43-^'h-  'ffff(sd.)''oa  alsum  agate  Y.ig.^i;  —  'oa
```


## [2026-10-17T00:32:47.169Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"(yäs-|yās-|yäsa-|yäsä-).{0,80}(bitten|wünsch|verlang)\" BRT.txt | head -5; grep -n -E \"(mazyah|masyah|fräyah|frāyah|kasyah|srayah|sräyah)\" BRT.txt | head -10; sed -n 13176,13178p BRT.txt | cut -c1-400; grep -n -E \"mazdayasna-? *Adj\" BRT.txt | head -3"
}
```


### [2026-10-17T00:32:47.788Z] TOOL RESULT

```
9381:459  karätayaeffl  —  kasyah-  460
9385:Zum  V.  Jiari-.  —  Vgl.  ai.  kriläy-  f.  'Ansied-   *b5jim   X.31. 1 3 ;   —   "sJuIäl  nä  .  .   isväcU lung'  (woiu  FoYKZ.j4.i39ßeEenGDN.  VSt.    (sd.)   kas  faraoi  Y.4j.i^ X.  128).  —  PQ.:  kiilan,  kiil.  KompA.,  AbleLt.  —  VgL  kasyah-,  iasiUa-.  —
9428:■A.I.'.).   -  s.  »,J.,  *«A  und\ii»rÄ..   -  •  J.  kasyah- Adj.  (mch  fem.)  der  kltinere,
9431:4ÖI  kasyah-  a  —  Icata-  462
18219:•  j.  fräyah-  Adj.  (fem.  •yehl-)  1)  'der mehrere,  plus':  nait  aevB  .  .  dva  . .  %rayS .  .  'yanAs  .  .  fra/md  (Sp.  360  u.)  P.  44'^ —  caiti  na  agvahe  pasvB  (sd.)  ..  a^a  dva aha  hryqm  .  .  an/qm  *kahyacit  tdoa *°yaaAqm  '*  ". .  ebenso  bei  zwei,  ebenso bei  drei  . .;  (je)  eins  dann  bei  jedem mthr"  N.  6y,  —  paniasatbl/c'a  . .  *'yJbTs- /a/(sd.).'o">  aAmäjVr.S.i.  a)  'mehr  als geaugiZnvieV :  daAmff  daUya  draona . .'^•yii^ draonä  s^arS  mdhatte  N.  30;  —  daitrm  gSui dragnS ..  *'y?^>  \daitlm\g3its  draonö^ups.- u^mns  N.  jj.  a)  n,  als  SubsL  'Überschuss, Überfluss':  tu  bairyeinte  yaisqm  dim  'ys voAunqm  ".  .  bei  denen  schon  Überfluss vongutenDingenist"  V.j.ag.  2)  ohne kompar.  Bedeutung  'sehr  viel,  sehr  zahl- reich': aal  dl/  ava^jayamahl  'yeAts{APL) Y.  4.  S-  a)  ASn,  °yS  als  Adv.  zur  Ver- stärkung des  Superlativs*':  yaiAe  aztm  *ys tbaysntqm  sraätim  susruye  va^m  "der unter  denen,  die  (mich)  rufen,  die  schönste
18728:Zum  V.  nartp:  —  Pü, :  :*/  m  i  15  dastawar nirfsenend  ('sie  vermindern')  vai  ..  .  —  •)  Vgl. lAusdr,  nnter  kasyah-  a.
20115:Ableit  —  mp.  (Pü.)  masi  gr.  vgl.  fiax/ii;.  — Vgl.  masyah-,  maiiila-.  —  D  Them.  —  ')  Un- richtig KZ.  30.  539-
20143:j.  masyah-  Adj.  (fem.  'yehJ-Y^  'der grössere':  Ä  üsti  '_>'?(NSn.)  vatghs  srayS (sd.)  aittm  dättm . .  upairi  anyäi^..  V.5. 22 ; avai  hl  asti  'yS  ari^»n  (sd.)  V, 7.71; tisit  maslm  gag%Jm  ff?(sd.)  'ya  hacaiU (sd.)  3snS  xratui  YL/0. 107;  —  ''kaya h»nH  •yaaho  (NP.)  a^  (sd.)  .  ■  *ltaya kasyanhö  F.  j  c ;  —  ^a^  'yS  attahmäi barfsma  N.  70;  —  ^aSa  tJ'ays  (NSf.)" J/^  kasyanhqm  apqm  *avi./rädavaiie  (sd.) V.  5. 24;  —  ya%a  yayi  (NSf.)''  vana kasyanhqm  vanqm  aiwi.vfrjnvaiH  (sd.)  V. 5.  24;  —  yimö  . .  tqm  vXSävayai  (sd.)  atva 'kriha  ahm3l  'yehim  ya'^a  . .  V.3.11;  — fravasayS  .  .  yä  'yehll  ahmät  .  .  yaäsa vaca  /ramraväire  (sd.)  Yl  13.  64;  —  °yd va  ahmätäi  "oder  noch  grösseres  (ärgeres, näml.  soll  als  Strafe  ihm  geschehen)"  V. 4.  50.  a)  'von  grösserem  Wert,   wert-
20244:}.,  g,  mazyah-,  j.  mazah-'>  Adj.  'der grössere,  gewaltigere',  an  Umfang,  Bedeu- tung usw. :  ya^/a  ahtnat  aiti  'sys  . .  vatthB ,  .  srayd  .  .  ta^  nB  dsyata    Y.  ^5. 14;    — katürim  asavä  va  dngvä  vä  vfranvaiil(sd.) "sys  Y.3i.i-j''>;  —  vrsmie  avat  vTstnta^a *matyasat^'>  Yt  i^.  7  3 ;  —  izyati . .  tavavat (sd.)  ,  .  *°zyasät^  'Vyt.30;  —  'xanham'^ va  ifaram  (sd,)  N.^IJ. Komp.  zu  mtu;  matanl-.  —  u.  vgl.  mäl^ai- Adj.  —  Pü.!  miuO,  {lu  N.):  mid,  —  '»S50. 3.  —  »)  Vgl.  V,  38.  5.  —  1)  Hds,  matdyasfit (mit  Yat.),    Der  Verf.  des  Vjrt.  fand  &1eo  die Verderbnis  in  Vt  13.  72  bereits  vor.  —  4)  Zn Y.  31  mit  der  ErL  luxiamä/ar.
23805:•  '].  vouru.kaäa-'>  Adj.  'mit  weit(ausge- dehncjen  Buchten',  nur  mit  srayah-  n. Name  eines  grossen  Sees,  der  in  der  Vor- stellung mit  dem  Weltozean  zusammen- floss**;  ^'däfl  zraye  'hm  upairi  anyä  äpd "wie  das  Zr.V.  die  übrigen  Gewässer  Über- 1 (trifft)"  V.5.  23;  — ya^a  zrayJ  -um  apB asti  hanjaymarum  "wie  das  ZrV.  der Sammelort   des  Wassers  ist"  V,  2/.  4;  —
yesnya  AauniaiiA.)  *daiaiti  N.J7;  P.,J2;
—  akurä  f^alim  (sd.)  vasm  haihySm  da ohBm  Y._j4.i5;  — frasfm  (sd,)  vasna  ahüm da'iütta  Y.55.  6;  Yl  ig.  1 1,  19.  a)  mit Dat.  comm.:  ksm  nä  ..  tnavaiU  (sd.) psyBin  dadät  Y.  46-  7 ;  —  >'"'  *drpgi^yB (sd.)  dadat  (jPPrA.)  västarfm  Y.  27.  13;
—  t}mca  .  .  *paityastTm  (sd.)  . ,  /o»^?  rfiW V-  5  9.  3 ;  —  0^/(7/  /f . .  avayqm  (sd.)  Vrt//- maAi'^*  Y.6S.1;  —  anyB  vä  Ae  dahme srut.i  g'i'^S  daöäiti  . .  asrut-l  (sd.)  daoiJifi
```


## [2026-10-17T00:32:54.043Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"srayah-  Adj|sraySh|srayah- Adj\" BRT.txt | head -3; grep -n -E \"j\\.  srayah\" BRT.txt | head; grep -n -i -E \"maQiSta|maθišta|maOista|ma9ista|maÖista\" KNT_full.txt | head -3"
}
```


### [2026-10-17T00:32:54.430Z] TOOL RESULT

```
27334:•  j.  srayah-  Adj.  'der  schönere':  cä  aUi masyS  vanhs  'yS  aSstn  dätim  yim  vjdsyüm .  .  iipairi  anyäis  sraväÜ  "um  wie  viel ; grösser,  besser,  schöner  ist  dies  Gesetz  . .  1 als  die  andern  Lehren"  V.5.  22;  —  imat\ vaahs  imat  'yS  yj^a  tum  .  .  valaahe  V.  | 5.  a  I ;  —  yalca  ahmst  asti  mazyö  .  . '. vatfhS  . .  'yd  . .  parS.ar?jaslar3m    tat  .  .
27334:•  j.  srayah-  Adj.  'der  schönere':  cä  aUi masyS  vanhs  'yS  aSstn  dätim  yim  vjdsyüm .  .  iipairi  anyäis  sraväÜ  "um  wie  viel ; grösser,  besser,  schöner  ist  dies  Gesetz  . .  1 als  die  andern  Lehren"  V.5.  22;  —  imat\ vaahs  imat  'yS  yj^a  tum  .  .  valaahe  V.  | 5.  a  I ;  —  yalca  ahmst  asti  mazyö  .  . '. vatfhS  . .  'yd  . .  parS.ar?jaslar3m    tat  .  .
```


## [2026-10-17T00:33:00.477Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('POK_full.txt').read()\nblocks=t.split('Root / ')\nfor b in blocks:\n    m=re.search(r'Page\\(s\\): ([0-9\\-]+)',b)\n    if not m: continue\n    ps=m.group(1).split('-'); a=int(ps[0]); z=int(ps[-1]) if ps[-1] else a\n    for p in (521,618,699,708,800):\n        if a<=p<=z: print(p, b[:80].replace('\\n',' '), '| hits:', [x for x in ['yah','yas','i̯es','ios','kasy','mazy','masy','frāy','sray','fräy','srey','śrey'] if x in b])\nE"
}
```


### [2026-10-17T00:33:00.928Z] TOOL RESULT

```
521 lemma: kaito-   Meaning: forest   Note: (Celtic and Germanic)   Material: Acymr. | hits: []
521 lemma: kaiuf-t, kaiup-t   Meaning: hole, ravine   Material: Old Indie kevata-vc\ | hits: []
521 lemma: kakka-   Meaning: to defecate   Note: babble-word the Kindersprache   Mat | hits: []
521 lemma: kai-t-   Meaning: " light, illuminated, pale, bright '  See also: see bel | hits: []
521 lemma: kak-   Meaning: to croak   Material: Old Indie kaka-m. "crow', kakala-, k | hits: []
618 lemma: kra[u]- : kreu- :   kru-   Meaning: to heap up, put together; heap; roof, | hits: []
618 lemma: krek-1 {-k-7)  Meaning: to hit   Material: Gr. KpsKw 'hit, beat; weave, s | hits: []
521 lemma: Rak-   Meaning: to become thin   Material: Avestan kasu- ' small, little' | hits: ['yah', 'kasy']
699 lemma: mahkh-o-s, -(s)lo-   Meaning: wild, unbridled, bold   Material: Old Indie | hits: []
699 lemma: mahRo- or mohR-o- {*mahgho-)   Meaning: a kind of fly   Note: (-/o- -ko-, | hits: []
699 lemma: rnand-: hurdle, plaited twigs, horse fence, stable, derived from Root/  l | hits: []
699 lemma: mahR- : mahR-     Meaning: long, slender   Material: Avestan mas-long', c | hits: ['mazy', 'masy']
699 lemma: mah-no-, mah-ni-   Meaning: wet, damp   Material: Latin mano, -are^ to fl | hits: []
708  lemma: med-1\ to measure; to give adviee, healing.   alb. math, madh/"b\g, larg | hits: ['ios']
800 lemma: /aku-: water basin (ditch, lake, sea),  (common Slavic alb. pe- prefix).  | hits: ['yah', 'yas']
```


## [2026-10-17T00:33:06.926Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"kasyah|mazyah|masyah|fr[aā]yah|frayo|srayah|sreyas|sr[eé]yas|mazy|masy\" POK_full.txt | head -20"
}
```


## [2026-10-17T00:33:08.855Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"comparative|komparativ\" SYN.txt | head -5; python3 - <<'E'\nt=open('SYN.txt').read().split('\\f')\np=t[880+24]; import re\ni=p.lower().find('compar'); print(p[:200]); print('...',p[i-800:i+800] if i>=0 else 'no compar')\nE"
}
```


### [2026-10-17T00:33:09.130Z] TOOL RESULT

```
49310:Material: Avestan kasu- ' small, little', compounds Superl. kasyah-, kasista-. 
51896:ugly, not good looking ', Avestan 5/7?5- "beautiful', Kompar. Old Indie sreyas-, Avestan 
51898:srayah-, Superl. Old Indie srestha- {srai'stha-), Avestan sraesta-. Old Indie sreman-m. " 
57054:certain water bird, a fish '= np. may^a water bird ', Old Indie matsya- m., Avestan masya 
57569:Material: Avestan mas-long', compounds masya' the great ', Sup. masista-, ap. madista- 
57571:Indo Germanic /77a5- through influence of mazya' further, extra, in additional amounts, 
58013:mazyah-, mazista-; 
60160:(for *p6pT0(;); derived *mor-t/o-\n Old Indie martya-, Avestan masya-. Old pers. martiya-^ 
65798:frayah-, Superl. fraesta-^\hQ meiste'; here Iran. *pelu-, *polu-\v\ Plejadennamen npers.
```


### [2026-10-17T00:33:09.269Z] TOOL RESULT

```
48:Martin A. Ryerson Distinguished Service Professor Emeritus of Comparative Philology i The University of Chicago
71:The kind of thinking that distinguishes man n from brute has been built up by and is dependent upon the use of symbols. Since vocal utterance at- tained a higher development than gesture as a means of communication, these symbols are, in fact, the words. Animals, to be sure, have cries which in some cases cover a very considerable range of emotions and to a certain extent serve to communicate. But these are limited to the immediate ex- perience: they are not detachable symbols capable of expressing past or future experience or any abstract concept. Yet such cries, which comprise all that primitive man inherited from his ancestry, must perforce be the starting-point of human speech. Primitive man, with his more highly de- veloped brain, gained an awareness of a connection between the sound and something expressed by it. With this step taken, a nucleus provided, and doubtless aided by gesture, human speech progressed and in turn became the dominant factor in man’s further mental growth. That is, we have the spwal development: superior brain (there is, of course, a “why?” to this too) > primitive human speech > organized conceptual thought. Any more detailed picture of the process, of the much discussed “origin of lan- guage’, we shall never have. The relatively brief period of recorded speech is separated by a vast interval from the beginnings of human speech—far beyond the reach of the historical-comparative method. Nor are we further concerned here with this remote problem.
411:Grimm J. und W. Grimm, Deutsches Wérterbuch. GRM_ Germanisch-romanische Monatschrift. Harper Harper’s Latin Dictionary. Hatzidakis, Einl. G. Hatzidakis, Einleitung in die neugriechische Grammatik. Hatzidakis, Meo. I. Xarfidaxts, Mecawwryixa Kal véa "EAAQUKG. Hellquist E. Hellquist, Svensk etymologisk Ordbog, 2d ed. Henry V. Henry, Lexique étymologique du breton moderne. Hermann, Lit.-deutsches Gesprichsb. E. Hermann, Litauisch-deutsches Gesprichsbiichlein. Hessen Hessen’s Irish Lexicon, a Concise Dictionary of Early Irish. Hesych. Hesychii Alexandrini Lexicon. Hirt, Idg. Gram. H. Hirt, Indogermanische Grammatik. Holthausen F. Holthausen, Altenglisches etymologisches Worterbuch. Horn P. Horn, Grundriss der neupersischen Etymologie. Hiibschmann, Arm. Gram. H. Hiibschmann, Armenische Grammatik, I. Theil. Idg. Anz. Anzeiger fiir indogermanische Sprach- und Altertumskunde. Idg. Jhrb. Indogermanisches Jahrbuch. IF Indogermanische Forschungen. IG Inscriptiones Graecae. ‘Tor. Ack. ‘Ioropixdy Aetixdv ris véas ‘EAAnvexijs. Jagié, Entstehungsgesch. V. Jagié, Entstehungsgeschichte der kirchenslavischen Sprache. JAOS Journal of the American Oriental Society. JEGPh. Journal of English and Germanic Philology. JHS Journal of Hellenic Studies. Kluge-G. F. Kluge, Etymologisches Worterbuch der deutschen Sprache, 11. Aufl., bearbeitet von Alfred Gétze. 4 Kretschmer, Hinl. P. Kretschmer, Hinleitung in die Geschichte der griechischen Sprache. Kretschmer, Wortgeogr. P. Kretschmer, Wortgeographie der hochdeutschen Umgangs- sprache. Kurschat F. Kurschat, Litauisch-deutsches und Deutsch-litauisches Woérterbuch. KZ Kuhn’s Zeitschrift (Zeitschrift fiir vergleichende Sprachforschung). Lalis A. Lalis, A Dictionary of the English and Lithuanian Languages. Language Language (Journal of the Linguistic Society of America). Laws, Gloss. Ancient Laws of Ireland, vol. VI, Glossary, comp. R. Atkinson. Le Gonideec Le Gonidec, Dictionnaire frangais-breton et breton-frangais. Leskien, Ablaut A. Leskien, Der Ablaut der Wurzelsilben im Litauischen. Leskien, Bildung d. Nom. A. Leskien, Die Bildung der Nomina im Litauischen. Leskien, Gram. A. Leskien, Grammatik der altbulgarischen Sprache. Lewis-Pedersen H. Lewis and H. Pedersen, A Concise Comparative Celtic Grammar. Lidén, Arm. Stud. E. Lidén, Armenische Studien. Lidén, Stud. E. Lidén, Studien zur altindischen und vergleichenden Sprachgeschichte. Linde M.S. B. Linde, Slownik jezyka polskiego. Littré HE. Littré, Dictionnaire de la langue francaise. Lokotsch K. Lokotsch, Etymologisches Wérterbuch der europiischen Worter orientalischen Ursprungs. Loth, Mots lat. J. Loth, Les mots latins dans les langues brittaniques. LS Liddell and Scott, Greek-English Lexicon, 9th ed. Lunds Univ. Arssk. Lunds Universitets Arsskrift. Macbain A. Macbain, An Etymological Dictionary of the Gaelic Language. Macdonell-Keith A. Macdonell and A. Keith, Vedic Index of Names and Subjects. McKenna L. McKenna, English-Irish Dictionary.
420:Meillet, Introd. A. Meillet, Introduction 41’étude comparative des langues indo-européennes.
434:Morris Jones J. Morris Jones, A Welsh Grammar, Historical and Comparative.
�, sefyll ‘stand’, Br. sevel ‘rise, raise, build’, Br. sao ‘standing, eleva- tion’, whence the phrase for ‘stand’ beza (chom) enn he zao, lit. ‘be (remain) in one’s standing position’, after Fr. éire 
... no compar
```


## [2026-10-17T00:33:14.702Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -i -E \".{200}(mazy|frāy|fray[aā]h|kasy).{200}\" SYN.txt | head -5; python3 -c \"\nt=open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt').read().split('\\f')\nfor i in range(900,910):\n  if 'yah' in t[i] or 'MORE' in t[i]: print(i, i-24, t[i][:300])\""
}
```


### [2026-10-17T00:33:15.367Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:33:19.289Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nt=open('SYN.txt').read().split('\\f'); print(len(t))\nimport re\nfor i,p in enumerate(t):\n  m=re.search(r'\\b880\\b',p[:300]+p[-300:])\n  if m and 850<i<950: print(i, p[:400].replace(chr(10),' '))\n\""
}
```


### [2026-10-17T00:33:19.917Z] TOOL RESULT

```
1545
```


## [2026-10-17T00:33:23.844Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nt=open('SYN.txt').read().split('\\f')\nfor i in (903,904,905): print(i, t[i][:600].replace(chr(10),' '),'\\n')\n\"; grep -n -E \"13\\.(1[0-9]) (MUCH|MORE|GREAT|SMALL|LARGE)|12\\.5[0-9] (LARGE|GREAT|SMALL)\" SYN.txt | head"
}
```


### [2026-10-17T00:33:24.344Z] TOOL RESULT

```
903 E *fei-. Walde-P. 1.358 ff. Grk. keluat, 38g. xetrac = Skt. cele, Av. saéte. Byz., NG xetrouat (so, not xolrouac as if fr. sb. orn) with shift to thematic type and xer- fr. old 3sg. xetrax (?). Hatzidakis, Mec. 1.316 f. 3. Lat. tacére (> It. giacere, Fr. gésir, Sp. yacer, Rum. zace), orig. ‘throw one- self, be thrown down’ : iacere ‘throw’, Grk. tue ‘throw’. Cf. Sp. echarse ‘throw oneself down, lie down’. Walde- P. 1.199. Ernout-M. 466. Walde-H., 1.666 f. REW 4562. Of the Romance derivs. of iacére, Fr. gésir is obs. except in certain forms, Rum. zace is now in restricted use (esp. ‘lie dead, l 

904 �, sefyll ‘stand’, Br. sevel ‘rise, raise, build’, Br. sao ‘standing, eleva- tion’, whence the phrase for ‘stand’ beza (chom) enn he zao, lit. ‘be (remain) in one’s standing position’, after Fr. éire (rester) debout; Goth., OE standan, OHG stantan, stan, etc., general Gme. with or without nasal present; Lith. stovétz, Lett. stavét (cf. ChSl. staviti ‘cause to stand, put’), beside Lith. stoti, Lett. stat ‘take a stand, stand up’; ChSl., SCr. stojati, Russ. stojat’, beside perfect. Chil. stati, stana, ‘take a stand’ (rendering Grk. aor.), but Boh. stati, Pol. staé simply ‘stand’; Skt. stha-, Av. 

905 r’; here prob. Ir. ainmne, W. an- mynedd ‘patience’ (cf. Grk. bro-novy ‘pa- tience’). CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar 2. It. restare, Fr. rester (latter with -3- from the It. or Lat. form), fr. Lat. restare ‘stand firm, remain = be left’, epd. of stare ‘stand’. REW 7248. Gamillscheg 759 f. It. rimanere, Rum. réminea, OFr. re- maindre (> ME remayne, NE remain), fr. Lat. remanére ‘be left’ (epd. of manére, above, 1). It. aspettare ‘await, wait’, fr. Lat. aspectare ‘look at attentively, desire’, whence also by assimilation *astectare > Rum. astepia. REW 3039. Puscariu  

22432:12.55 LARGE, BIG (GREAT)
22468:12.56 SMALL, LITTLE Grk. —_pixpés Goth. leztils (smals) Lith.  maizas NG mtxpds ON litill, smar (smalr) Lett. mazs Lat. parvus Dan. lille, pl. smaa ChSl.  malit (chudit) It. piccolo Sw. liten, pl. smd SCr. mali, malen Fr. pelit OE ljtel, smal Boh. maly Sp. pequefio, chico ME litel, smal Pol. = maly Rum. mic NE small, little Russ. malyj Ir. becc Du. klein Skt. alpa-, kgudra- Nir. _ beag OHG _ luzzil, smah(i), smal Av. kasu- W. bach, bychan MHG litzel, smal, smehe, Br. bihan klein
23511:13.15 MUCH; MANY (Where only one form is entered, this is also used, either in pl. or with pl., for ‘Many’)
23561:924 SELECTED INDO-EUROPEAN SYNONYMS 13.16 MORE Grk. —-rAclwy, zAbwy Goth. managiza (maizo, Lith. daugiaus NG meptoadrepos mais adv.) Lett. vairak Lat. _pliis ON metri; fleiri (pl.) ChSl.  bolzjt, MUNOzZE;t, vedte It. pitt Dan. mer; flere (pl.) SCr. vide Fr. plus de Sw. mer; flere (pl.) Boh. _ vic(e) Sp. mas OE ma Pol. —- wiecej Rum. maz mult ME mo; more (sg.) Russ. _bol’Se Ir. mo; lia (pl.) NE more Skt. bhilyas-, bahutara- NIr. —tuilleadh; lia (pl.) Du. meer Av. Srayah- W. mwy OHG = mér, méro; manigiron Br. mut, mutoc’h (pl.)
```


## [2026-10-17T00:33:31.365Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('KLN_1966.txt').read().split('\\f')\nimport re\nfor p,cands in ((371,['comparative','compar']),(958,['compar']),(1759,['yazata','Yazd','Yezid','yaz-','yasna'])):\n  for i in range(p//2+9,p//2+16):\n    s=t[i]\n    for c in cands:\n      for m in re.finditer(re.escape(c),s):\n        print(p,i,c,'::',s[max(0,m.start()-250):m.start()+200].replace('\\n',' '));break\nE"
}
```


### [2026-10-17T00:33:31.753Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:33:35.674Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"comparative suff|compar\\. suff|suff\\. of the compar\" KLN_1966.txt | cut -c1-400 | head; grep -n -E \"^Yezidi|Yezdi|Yazata|yazata|Ized\" KLN_1966.txt | cut -c1-400 | head"
}
```


### [2026-10-17T00:33:36.093Z] TOOL RESULT

```
8976:contra-,  pref.  meaning  'against,  opposite  to’.  — L.  contra,  'against,  facing,  opposite,  contrary to,  opposed  to',  prop.  abl.  fern.  sing,  of  *com- tro,  which  was  formed  fr.  OL.  com,  ‘with,  to¬ gether  with'  and  -tr,  zero  degree  of  the  compar. suff.  -ter-,  which  appears  in  L.  alter,  'the  other (of  two)'.  Conmi  orig.  denoted  the  being  to¬ gether  
11145:deuterium,  n.,  the  isotope  of  hydrogen  of  atomic weight  or  mass  2;  heavy  hydrogen  ( chem .)  — ModL.,  coined  fr,  deuter-  and  suff.  -ium. deutero-,  before  a  vowel  deuter-,  combining  form meaning  ‘second’.  —  Gk.  Seuxepo-,  Sen-rep-,  fr. Seuxepog,  ‘second’,  orig.  ‘that  which  falls  short of  something’,  formed  with  the  comparative suff,  -repo?  from  the 
19866:ionosphere,  n.,  that  part  of  the  earth’s  atmosphere which  extends  from  the  stratosphere  to  the exosphere.  —  Compounded  of  ion  and  sphere, -ior,  suff.  representing  the  Latin  compar.  ending -ior,  as  in  anterior,  excelsior.  —  L.  -ior,  cogn. with  OI.  -iyas,  Gk.  -Lav,  Goth,  -iza,  -oza,  OE. -ra  (in  adjectives),  -or  (in  adverbs).  See  compar. suff.  -e
```


## [2026-10-17T00:33:41.367Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('KLN_1966.txt').read()\nfor key in ['-ior,  suff.  representing','agnus  castus,  n.','Agnes,  fem.  PN']:\n  i=t.find(key); print(key, 'leaf', t[:i].count('\\f'))\nE\ngrep -n -E \"^(zeal|jealous)\" KLN_1966.txt | cut -c1-300; grep -n -i -E \"Yazdegerd|Yazdgard|Yezdegerd\" KLN_1966.txt | cut -c1-200|head -3"
}
```


### [2026-10-17T00:33:41.772Z] TOOL RESULT

```
-ior,  suff.  representing leaf 437
agnus  castus,  n. leaf 32
Agnes,  fem.  PN leaf 32
```


## [2026-10-17T00:33:48.372Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -i -E \".{150}(yasna|yazat|Avest\\. yaz).{150}\" KLN_1966.txt | head -5; python3 -c \"\nt=open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt').read().split('\\f');print(len(t)); print(t[890][:300])\""
}
```


### [2026-10-17T00:33:48.994Z] TOOL RESULT

```
903
  universolog- ist,  n.
univocal,  adj.,  having  one  meaning  only.  —  Form¬ ed  with  adj.  suff.  -al  fr.  Late  L.  univocus,  which is  compounded  of  L.  unus,  ‘one’,  and  vox,  gen. vocis,  ‘voice,  sound’.  See  uni-  and  vocal, unkempt,  adj.,  not  combed;  untidy.  —  Formed fr.  p
```


## [2026-10-17T00:33:52.854Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"yazata|yasna|Yezid|Yazid\" KLN_1971.txt | head -8; sed -n 270330,270340p KLN_1971.txt; grep -n -E \"^hagio\" KLN_1971.txt | head -3"
}
```


### [2026-10-17T00:33:53.449Z] TOOL RESULT

```
269367:to Avestic yazaite, of s.m., yasna-, ‘sacrifice, 
269370:Yasna. 
269504:Yasna, n., one of the four divisions of the Avesta. 
269505:— Avestic yasna-, ‘sacrifice, worship’, rel. to OI. 
zeal, n. — ME. zele, fr. Late L. zelus [whence also 
It. zelo , OF. zel (F. zile), Sp. celo ], fr. Gk. 
CtjXo? (Dor. cotXoc j , ‘jealousy, fervor, zeal’, 
which is prob. rel. to Dor. £aTeu&>, 

Aeol. CaTTjfxi, ‘I seek for, inquire into’, 
8t-frqi*xi, ‘I seek out, demand’, and perh. also 
to Cqpda, Dor. ‘damage, penalty’. Cp. 

jealous. Cp. also zetetic, 
zealot, n. — Late L. zeldtes , fr. Gk. 
108489:hagio-, before a vowel hagi-, combining form 
108502:hagiocracy, n. t government by persons considered 
108510:hagio- and -graph. Since all the 3 parts of the
```


## [2026-10-17T00:33:57.376Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 269360,269372p KLN_1971.txt; sed -n 269504,269510p KLN_1971.txt; sed -n 108489,108500p KLN_1971.txt; grep -n -E \"^\\s*-?[0-9]{4}\\s*-?$|^- ?17[56][0-9]\" KLN_1971.txt | awk -F: '$1>269000 && $1<269700' | head"
}
```


### [2026-10-17T00:33:57.821Z] TOOL RESULT

```
Derivatives: Yahw-ism, n., Yahw-ist, n., Yahw- 
ist-ic, adj. 

Yajna, n., sacrifice personified in Vedism as the 
son of Ruchi and husband of Dakshina . — OI. 
yajhdh, ‘sacrifice, worship’, fr. yajati, ‘he reveres 
(a god) with sacrifices, he worships’, which is rel. 
to Avestic yazaite, of s.m., yasna-, ‘sacrifice, 
worship’, and prob. cogn. with Gk. * 710 ?, 
‘holy’, &yv 6 <;, ‘holy, chaste’. See hagio- and cp. 
Yasna. 

yak, n., wild ox of Tibet and Central Asia. — 
Yasna, n., one of the four divisions of the Avesta. 
— Avestic yasna-, ‘sacrifice, worship’, rel. to OI. 
yajhafa, of s.m. See Yajna. 
yatagan, n., a kind of Turkish sword. — Turk. 
yatagan. 

yaw, intr. v. f to fall away from the line of her 
hagio-, before a vowel hagi-, combining form 
meaning ‘holy, sacred’. — Gk. ayio-, ayi-, fr. 



ayt<k, ‘holy, sacred’, which is rel. to 
(for *&yteal>a0, ‘to stand in awe of, to revere’, 
<£yo<;, ‘sacrifice, expiation’, <&yt£eiv, ‘to hallow’, 
ayv6q, ‘holy, chaste’, and prob. cogn. with OI. 
ydjati, ‘reveres (a god) with sacrifices, worships’, 
yajas-, ‘worship’, yajhah , ‘worship, sacrifice’, 
OPers. a-yadana ‘temple’. Cp. the second ele-
```


## [2026-10-17T00:34:04.394Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for r in BQT:553 BQT:2419 BQT:752 BQT:2432; do echo \"-- $r\"; timeout 300 python3 tools/ref_page.py $r 2>&1 | grep -n -E \"جادو|یاسه|ایزد|یزدان|jâdû|jâtûk|yâs|yazd|îzad|izad|PNG|png|pdf page|vision\" | head -15; done"
}
```


### [2026-10-17T00:34:17.805Z] TOOL RESULT

```
-- BQT:553
-- BQT:2419
1:(no exact page map; using offset -1917 -> pdf page 502; check the printed number and re-run with --pdf-page if off)
2:REF: BQT:2419  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 502  OCR-lang: fas
19:یاسه این‌ید که له بیندهیج سیر د رکه و بیگه لقای آن امیر.
-- BQT:752
-- BQT:2432
1:(no exact page map; using offset -1917 -> pdf page 515; check the printed number and re-run with --pdf-page if off)
2:REF: BQT:2432  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 515  OCR-lang: fas
14:آفربنندء خیررا یزدان وآفربننده شرا اهرمن جمعی فلیل ومردم کمی را کویند که در مقدمه
24:ایزد «اسشق ۱۱۲۷ پزدان دراسل جمع «یزه» (* ایزد [ه م.]. +3822 ازاوستایی 782218)
28:است: «ننویان که «وکوبند: یکی یزدان ودیگر اهرمن ...> «تاصرخرو بلخی. جامع الحکمتین
30:۳۱ ۲ - درفهرست شاهنامه ولف‌نيامده. (تر کیب اسم مفعولی بمعنی «یزدان,خشیده»
36:۹ از: برد (* ایزد) ۲ کرد ( کرد کرده, آفریده) درسللهٌ ساسانی سه پادشاه پدرین نام
```


## [2026-10-17T00:34:21.454Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:553 2>&1 | head -40; "
}
```


### [2026-10-17T00:34:21.840Z] TOOL RESULT

```
no scan of BQT covers printed page 553 (see 'scans' in refs_online.json)
```


## [2026-10-17T00:34:29.731Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nfor f in ['BQT_v1_pages.txt','BQT_v2_pages.txt']:\n    t=open(f).read().split('\\f')\n    for i,p in enumerate(t):\n        for w in ['jâdû','jadu','jâtûk','yâtu','îzad','yazata','yazad']:\n            if w in p:\n                j=p.find(w); print(f,i,w,'::',p[max(0,j-300):j+300].replace('\\n',' ')); break\nE"
}
```


### [2026-10-17T00:34:30.372Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:34:35.328Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nfor f in ['BQT_v1_pages.txt','BQT_v2_pages.txt']:\n    t=open(f).read().split('\\f')\n    print(f,len(t))\n    for i,p in enumerate(t):\n        for w in ['جادو','ایزد ']:\n            c=p.count(w)\n            if c>=3: print(f,i,w,c, p[:120].replace('\\n',' '))\nE"
}
```


### [2026-10-17T00:34:35.733Z] TOOL RESULT

```
BQT_v1_pages.txt 777
BQT_v2_pages.txt 684
BQT_v2_pages.txt 11 جادو 7   ‫جاضوگ‬                                                                           ‫‪۳-‬و هب‬ ‫وبزرن ماست » جایی را‬
```


## [2026-10-17T00:34:40.420Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==12' BQT_v2_pages.txt | grep -n -E \"جادو|ztuk|tuk|yâtu|ytu|jâd|Jad|ژادو|y.tu\" | head -20"
}
```


### [2026-10-17T00:34:40.847Z] TOOL RESULT

```
9:  ‫خشخاش‌سفید ؛ چه زبدببابماعی آنبیجد‌سفید‬        ‫جادو سن د کنابه ازثاع‌بائد‬
38:  ‫‪( 1142۷‬ساحر)» هندی باستان ‪( 148۷‬خدال ‏ سحر) ‪ ۰‬پهلویا‪) ۳11008 ( 6181‬جادوبی )‬
40:   ‫‪ +‬باتو = جادو » بگروه‌شیاطن ساحر و کمراه کنند کان وفرببند کان اطلاق‌شده< بشت!‪٩۲ :‬‏ » ‪:‬‬
41:    ‫زمین را سپردی بگر زکران‪ .‬فردوسی‌طوسی‪.‬‬          ‫( لهراسب ) بهر حمله‌ای جادوبی زآن‌سران‬
42:   ‫فردوسی « جادو ‏ را غالباً بجای « دروند » پهلوی‌ویازند ودروغپرست ویبرو دبومسناآرد‬
43:                ‫‪ +‬مزدسنا‪ .» ۹۷ ۲‬آمروز جادو بمعنی سحر و جادو کربمعنی ساحر استعمال‌میشود ‪.‬‬
```


## [2026-10-17T00:34:50.679Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('BQT_v2_pages.txt').read().split('\\f')\nfor i in range(195,225):\n    p=t[i]\n    for w in ['ایزد','جشن','یسنا','yasna','yazata','yaz']:\n        if w in p:\n            j=p.find(w); print(i,w,'::',p[max(0,j-200):j+200].replace('\\n',' ')[:400]);\nE\npython3 - <<'E'\nt=open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt').read().split('\\f')\nfor i,p in enumerate(t):\n    if p.count('جشن')>=4: print('jashn leaf',i,p.count('جشن'))\nE"
}
```


### [2026-10-17T00:34:51.114Z] TOOL RESULT

```
196 جشن ::          ‫در برح جدی ‪ - ۱‬ونام روز هشتم است ازهرماه‬                                 ‫درماه د‬  ‫کیه‌ان ماه دهم است از سالهای شمی‬                     ‫شمسی » و بنا برقاعدهکلیه که نزد فارسان مقرر‬  ‫جشن کردندی‌وجامپای سفید پوشیدندی وبرفرش‬              ‫است که (‪ )۱‬نام ماه وروز (‪ )۲‬موافق آبد عید‬  ‫نشتندی ودربانر! ءنع کردندی وبار عام دادندی‬           ‫باید کرد دراین روز عید کنندوجشن سازند ‪٩‬
202 جشن ::  حشن مغان‬                   ‫بیرون رانرا ‪ - 73‬ویمعنی نشسته براه رفتن‬ ‫چون نام‬       ‫کلبه که مبان ابشان معمول استکه‬                ‫هم هت چنانکه طفلان روند ‪ - ۱‬و با تشدید‬ ‫ماه وروز موافق آید جشن کنند ‪ ۰‬وبعضی گوبند‬                    ‫تافی » در عربی جانوریست معروف که از پوست‬ ‫نام‌روز هیجدهم است ازشهر بورماه وعضی نام روز‬                                              ‫أن بوستین سازند؟ ‪-
jashn leaf 30 8
jashn leaf 31 10
jashn leaf 188 4
jashn leaf 572 6
```


## [2026-10-17T00:34:54.865Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==31 || NR==32' BQT_v2_pages.txt | grep -n -E \"yasna|ysn|اوستا|پهلوی|یسن|yašn|ja.n|yesn\" | head -12"
}
```


### [2026-10-17T00:34:55.278Z] TOOL RESULT

```
41:  ‫‪ ۴‬اوستا ‪ , 80۳537 .‬بهلوی ‪ [70152‬با ‪ ( 00152۷‬جشن ) « استق ‪١۲٤‬‏ »كل‪.‬مةٌ‬
42:  ‫اوستایی ‪ 2052‬وسان کرت ‪ 802۷‬و پپلوی ‪ 015228۷‬بمعنی ستایش و پرستش است‬
```


## [2026-10-17T00:35:00.719Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('BQT_v1_pages.txt').read().split('\\f')\nfor i,p in enumerate(t):\n    c=p.count('ایزد')\n    if c>=3: print(i,c)\nE"
}
```


### [2026-10-17T00:35:01.243Z] TOOL RESULT

```
252 3
```


## [2026-10-17T00:35:04.428Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==253' BQT_v1_pages.txt | grep -n -E \"ایزد|اوستا|پهلوی|yaz\" | head"
}
```


### [2026-10-17T00:35:04.839Z] TOOL RESULT

```
18:- اوستا 358080 بمعنیسشکه « بارتولمه ۲۰۷ و ۲۲۰» رگ : آس . چون آسمان را
19:بان سنکی پنداشته اد از اين رو نام آن در اوستا و پارسی باستان نیز 2511120 میباشد که در
20:پهلوی و فارسی آسمان کویم « خرده اوستا ۹ ح | » پهلوی 257028 « منای ۲۹۸ *.
26:و آسمان ؛ ایزدانی اراده شده که بنگهیانی سیهر و خالك کماسته شده‌اند : همه ساله زاشتاد واز
29:باد شده اند . نگهبانی روز یت و هفتم هر ماه با ایزد آسمان است . ابورسسان بیروئی دد
32:ایزد آحمان باعزرائیل مأخذی صحیح تدارد . ۴ - <- آشموغ , اوسنا 3511610082138 , پهلوی
33:۵ با 2511001181 لفة بمعنی بر همزننده «اشا» ( راستی) و غالبا در اوستا بمعن ی کمراه
34:کننده اسث . در هرهزدهت بند*۱ درتفیر پهلوی ( زند ) همین بند » سه قسم اشموغ تشخیص
36:دل‌دهد و وبرا پیروی کند « خرده‌اوستا ۷۳ * :
```


## [2026-10-17T00:35:09.727Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:2432 2>&1 | sed -n 1,60p; echo; timeout 300 python3 tools/ref_page.py BQT:2419 2>&1 | sed -n 1,60p"
}
```


### [2026-10-17T00:35:10.282Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 515; check the printed number and re-run with --pdf-page if off)
REF: BQT:2432  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 515  OCR-lang: fas

بزدان ۲۳۲
آن ریزندء وبسنیپزدادی کوفته را گوبند که در | پزدگرد است که پدر بهرام کور باشد و او را
درون آن‌تخم مرغ پخته‌باهند وآنرا یزد‌ادینی | بزدجردالائیم میگفتند . بغایت ظالم بود. روزی
هم میگوبند که بمد ازبای حطی در آخر نون | درکنارچشمةٌ کلست که ازاعمال طوس است اسبی
باشد . اورا لکد زد وکشت - ونام پسرزادة انوشیروان

پردان!۱ * بنتم اول وسکون ثانی‌ودال | هم «ست که آخرملوك عجم باشد. کویند درشهن
بالف کشید» وبنون‌زده» یکی‌از نامهای‌خدای‌تعالی لیشابور بردست ملازمان خود با آسیابان ی کشته
است جل جلاله - و نام فرشته‌ای هم هست که شد. 2
فاعل خیراست وه گز ازوشرنياید. وطایفة‌ننویه بزدد؟ < بفتح اول وئانی وسکون کاف»
آفربنندء خیررا یزدان وآفربننده شرا اهرمن جمعی فلیل ومردم کمی را کویند که در مقدمه
گوبند و مچنین آفر‌بنندهنوررا بزدان وا فربنندة و پا پیش لشکر براه روند و بترکی قراول
ظلمت را اهرمن, و فقها خدای باطل راو شمرا ۸۱ 4
خدای حق را خواند (۱) ۰ خوانند9 - وپای‌وپاسپانالرانیز گفته‌ال ویمعنی
پزدان بخش؟ - نام وزیر هرمزین - جاسوی هم آهده امت .
انوشیروان بوده است . هزفه* » بروزن وزنه. شوهر خواهر را
یزدجچرد؟ - بکر جیم» معرب | کونند .
(۱) چك» چش: کوبند .
۱- اوستا ۰78281888۳0 پهلوی ۰۷221۵0 8[0] ۰7224 9824480 ۰ قی :

ایزد «اسشق ۱۱۲۷ پزدان دراسل جمع «یزه» (* ایزد [ه م.]. +3822 ازاوستایی 782218)

است دربهلوی. ر4: نیب رکه صس۱۶۹؛ کر بیتنن. ساسان ص*۲۹ - درفارسی بمعنی «فرد بکاررفته

است: «ننویان که «وکوبند: یکی یزدان ودیگر اهرمن ...> «تاصرخرو بلخی. جامع الحکمتین

۳۱ ۲ - درفهرست شاهنامه ولف‌نيامده. (تر کیب اسم مفعولی بمعنی «یزدان,خشیده»

ازقبیل«شاهنواز») (از یادداشتهای علامه محمدقزوینی) ۴ - معرب زد کرت982011۳271

(۰.)9220887۵ سربانی 208670]. اوستایی #2872201076012* «یوستی. نام نامه س۱۶۸-

۹ از: برد (* ایزد) ۲ کرد ( کرد کرده, آفریده) درسللهٌ ساسانی سه پادشاه پدرین نام

خوانده شده‌اند : پزد کرد اول (۸۲۳-۳۹۹ م.) » پزدگرد دوم (40۷-4۳۹ م) » زد کرد سوم

آخرین عاهنشاه ساسانی (۹۹۱-۹۳۲ م.) رك: کریستنشن. ساسان.

ره همرب‌آن (ازفارسی)هم پزك4 (پیش قرارل, دیده‌ور) «رزی‌ج۲ ص۵۱ ورك: سلو4
مقریزی ص۷۸۸۰۵۵۹۰۵*۳ و۱۰۵ (الیز4الاسلامی).
- ای سپاهت را ظفر لشکر کش وصبرت يزك
نی‌شین برطول وعرض اشکرت؟آ که (واقف) له شك. .
انوری آپیوردی «صحاح الفرس نشهٌ طاعتی» «فرهنگه نظام» .
۹ - رشیدی بهمین هعتی آوزده. دراصفهان 722106 (شوهر خواهر) «فرهنکه نظام» »
قی: ۸826286 درتپرانی (شوهرخواهر) . ترکی یزنه بدمنی شوهرخواهر وخاله وعمه. فرهنگه
اطفری بنقل «فرهنگه نظام» .
۶ ردگره - ر4: پزدجرد .


(no exact page map; using offset -1917 -> pdf page 502; check the printed number and re-run with --pdf-page if off)
REF: BQT:2419  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 502  OCR-lang: fas

-۱۹- ۱ باه
فحتانی آلون, بممنیباسمون است که گل‌باسمن اه - بروزن‌بافته, قبض‌الوسولوحجت. .
باشد . و اصل خط راکونبند .
یاه < بروزن‌کاسه » بممتی راء و رسم ار « بفتح ثالك بروزن‌سافر؛ بازیگر
وقاعده وقالون باشد۲ - وبمعلی خواهش وآرزو | ورقاس را .کویند؛ وبکسر ثالك هم آمده است.
هم آمده ات۲ وبمربی‌تنی کوبند . بافه۴ « بنتح ناه پروزن لافه, کم‌شده
یاشق « پم شین‌قطه دار بروزن فاشق. | و باپدید گشته را میگوبنده - و سشنان هرزه
لام درختی است.#* وییهوده وسردر کم وپربشان و هذیان و قحش را

۹ یاسا (مغولی) رك: پاسا : ْ

کان اسیران را بجز دوری لبود دیدن فرعون دستوری لبود

گر فتادندی بره در پیش او بهر آن باسه بخفتندی برو

یاسه این‌ید که له بیندهیج سیر د رکه و بیگه لقای آن امیر.

مولوی بلخی رومی «مثنوی. چاپ نیکلسن دفتر سوم ص۰۹۶۸

۴ - هوبشمان کوید: 7298 ۳ پعلوی #78821 ازاوستا وپارسی باستان- 8888 .
هوبشمان وجه اشتقاق هرن «اسشق ۱۱۲۳ را قبول ندارد. رك: هوبشمان ۰۱۱۲۳

۴ - «باف؛ بازیگن را نامند» «جهانگیری» . مرا جکوید : «ویعی رقاص نی زگفته اند
وظاهراً مبدل «یاور» است . درین صورت تصحیف دراین معنی است که «یاریگر» برای مهمله را
«یازیگر» بزای معجمه خواندهء اند.» جهانگیری ازسروری واو ازموید نقل کرده» پس سحیف از
جهانگیری لیست «فرهنگه نطام».. ‏ ۴ ۳ باوه (ه.م.) «یافه. وخله وژاژ ولك همه بیهوده
بوده ولیز کوبند خله کردم وبافه کردم و کم کردم وهرز هکردم.» «لفت قری ص۸۹۳ ۰

8 -گو بافه‌شو فلاده زرین آسمان لور کف خجتهٌ او زیور نو باد.

شمس طبسی «رشیدی» «فرهنگه نظام» .

۵ یافتی - بفتح چهارم» از : یاف ( ۳ باب) تن (پوند مصدری) پهلوی 221128 ۰
080 .فیس : اکقْلاة . استی ۸[98۲00 ۰ 2[72510 ( رسیدن ) «اسشق ۰۹۱۱۲۶
هو بشمان کوید: فارسی: پابم. بافتن ۳ پلزند 2(81188: ازربشة 720 با جاتاقلز. استی 8 گقّلا
از 712018 مشتق است؟ «هوبشمان ۱۱۲۶؛ پیدا کردن, بدست آوردن, کب کردن .
بقیه از حاشيةهٌ صفحهٌ قبل
را مخصوص سوسن‌سفید داسته‌اند... وجمهوراطبا تعربف باسمین‌نموده‌اند که درخت اومانند درخت
مورد واملی؛ برکش لرمتر ویهن‌تر و بطبری بر که مورد لیست . درخت قم سفید او ضعیفشن
وگلش مفید و با شایبةٌ سرخی وبسیار خوشبوی وازوقت شکفتن لرکس تا اول عقرب کل میدهد
ودر بلاد حاره همه » ودرخت لوع زرد او عظیم و چتری وماندد درخت موز است » ونزد بسنی
فم زرد او ممي پزلیق اسی...» 2 تحقةٌ حکیم مژمن».
```


## [2026-10-17T00:35:16.748Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==233' ARP.txt | grep -n -i -E \"y[aā]tu|jad|magic|sorc|witch\" | head; awk 'BEGIN{RS=\"\\f\"} NR==62 || NR==63' incoming/ZAW/ZAW_pages.txt | grep -n -i -E \"yaz|yesny|yazat\" | head"
}
```


### [2026-10-17T00:35:17.164Z] TOOL RESULT

```
20:       yazdêgêrd ' Götterstadt' 75, SM.; vgl. dazu voNSTACKELBERG
```


## [2026-10-17T00:35:21.345Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==62 || NR==63' incoming/ZAW/ZAW_pages.txt | grep -n -B6 -A6 \"yazdêgêrd\" | head -30; grep -n -i -E \"yātu|yatu|jādū|jadu\" ARP.txt | head -5; head -c 600 ARP.txt"
}
```


### [2026-10-17T00:35:21.653Z] TOOL RESULT

```
14-kêrdag, qêrdag 'Tat' 862 u. ö., frašêgêrdîy, gêrdîg 49 ff.2) ; man
15-vergleiche zur Wurzelsilbe des bp. 11515 kartan, Paz. ‫وو‬         ‫وس‬
16-kardan, np. ‫ کردن‬kardan BARTHOLOMAE IF. 8. 253, SALEMANN
17-GIrPh. 1. 274 und zu deren Aussprache das entlehnte arm.
18-կերտ kert gemacht am Ende von Zusammensetzungen ; s.
19-HÜBSCHMANN AGr. 1. 168 ;
20:       yazdêgêrd ' Götterstadt' 75, SM.; vgl. dazu voNSTACKELBERG
21-Oss . Erzähl. 82, MUNCKASI Revue orient. 1904. 318, BARTHOLOMAE
22-AirWb . 448 ;
23-     hašâgêrd (MÜLLER gîrd) 'discipulus' 30, 32; vgl. zur Aus-
24-sprache die Pazandwiedergabe von bp. 119          oder ‫س دام‬
25-durch_
26-     ‫دسمو‬            sowie das entlehnte arm. muhtpır ašakert ; aber
1154:§  28. Yatu.
1155:Zu  den  wichtigsten  unter  den  bösen  Wesen  gehören  die YdtuSi  welche  bei  beiden  arischen  Völkern  den  gleichen  Namen führen.  Im  Rigveda  wird  das  Wort  in  doppelter  Bedeutung gebraucht,  sowohl  abstrakt  als  Spuk,  Zauber,  wie  auch  con- cret  als  spukhafter  Geist.  An  das  einfache  ydtii  schliesst  sich ydtumat^  Spuk  treibend  an,  das  im  Masc.  und  Fem.  häufig  ge- braucht wird.  Diese  beiden  Wörter  finden  sich  ebenso  im Awestä  wieder,  neben  yatu  wird  auch  dort  ydtumad  im  Masc. und  Fem.  gebraucht,  dass  der  Ausdruck  nicht  blos  dem  Awestä angehörte,  sondern  gemein  eränisch  war,  zeigt  das  von  yatu  ab- geleitete neup.  «c^Lä.,  jddü\  dagegen  findet  sich  für  das  indische ydtudhdna  bei  den  Eräniern  nichts  Entsprechendes.  Fragen wir  nach  der  Etymologie  des  Wortes,  so  ist  dasselbe  nach  der gewöhnlichen  Ansicht  von  yd,  gehen  mit  dem  Suffixe  tu  ab- geleitet, nach  Weber  (Ind.  Studien  4,  399)  hängt  es  mit  yat^ gr.  C,rjT8a)  zusammen,  was  auch  möglich  ist,  aber  keinen  grossen Unterschied  macht,  da  die  Bedeutung  der  Wurzel  yat  Ursprung-
1717:mani  80. mati  96. matsya  59. math  68. mad  42. mada  42. madgu  58. madhu  81. madhya  63.  65. man  96. manas  96, manu  276  fg. m antra  230. mastu  68. raahimagha  231. mätar  84. mätula  86. mäyä  96.  231. mäsha  45.  59. mäs,  mäsa  98. mitra  178  fg. mithradruh  217. mithas  93. miyedha  67.  82. mishta  67. mushiti  64.  65. mürdhaja  61. müsh  53.  235. müshä  53. müshi  53. mriga  57. medh  96  . medhas  96. medhä  96. medhira  96. mesha  50.  59. mainäka  111. mlecchabhojana  43. yakrit  65. yakshman  97. yaj  228. ya^ata  179.  225. yajüa  228, yajüya  228. yam  84. yama  243  fg. yava  43. yavasa  44. yavyä  28. yavyAfVati  107. yatar  88. yatumant  218. yamätar  87.
0^/^ilfi^^/^  Ry^>(a  tfe.'^v^ÄJ^'^y^Tt^
>>
.'^/^^^yilG^.'^
V^V  '^     .^'^^^'^'^/^'^  ^^^^jf^^^Jl^^f^'^Af^^^A^'^^  ^  A^^f^Af
.^y^^^yni^^y^^^
^/J^  ?^^/^  Ji^v^>lin  R^^y
^>7^^>^'(^v^>^^voL^^J^^^^^^Ö/^x^
^/pv\J  i-/x^^^  /^\i  iX^NJ  l/'x^^  i^/^Si y/^  "^  i5^/m^  il^'/m^^/^^  <^/^  ^  /^^Nü  4^x^  ^  ^
'TX^JTÄ^Xr^Ä^Ä^
J^XÄÄ'^rsrÄ^^^^^
^^-hT^>^X:^T^X^^^>^'^
t^Ä^^ST^b^^^^^
^JTÄ'^'Ä^^^^
^1ä^^
-^W^yxW/^
^^^^y^rv'^yo^^JL'^.^V^
'^  jJ: '^  IT '^^T'^^^*^^  ^
rSiSr^Ä«^^^
^.O  (N^yi)'f5v  -^  >o7ÜL  ^^^'{t.X^^flfL'^^'fi^^yOrv^/S^l^^  ^>^^'^.^JlW^/
V
>'
^^^^^22^^
'/n^^  4?^^^  i^'/n
```


## [2026-10-17T00:35:28.354Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -40"
}
```


### [2026-10-17T00:35:28.731Z] TOOL RESULT

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


## [2026-10-17T00:35:35.285Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; N='page 561'; for u in \\\n'https://en.wiktionary.org/wiki/جادو' \\\n'https://en.wiktionary.org/wiki/𐬫𐬁𐬙𐬎' \\\n'https://en.wiktionary.org/wiki/यातु' \\\n'https://en.wiktionary.org/wiki/ζῆλος' \\\n'https://www.etymonline.com/word/zeal' \\\n'https://www.etymonline.com/word/jealous' \\\n'https://en.wiktionary.org/wiki/ایزد' \\\n'https://en.wiktionary.org/wiki/یزدان' \\\n'https://en.wiktionary.org/wiki/جشن' \\\n'https://en.wiktionary.org/wiki/یزدگرد' \\\n'https://en.wiktionary.org/wiki/ἁγνός' \\\n'https://en.wiktionary.org/wiki/agnus' \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeh₂ǵ-' \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-yōs' \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/yáȷ́ati' \\\n'https://en.wiktionary.org/wiki/یاسه' \\\n'https://www.etymonline.com/word/agnus%20castus' \\\n'https://en.wiktionary.org/wiki/Yasna' ; do python3 tools/fetch_source.py \"$u\" --note \"$N fetch\" 2>&1 | tail -1; done"
}
```


### [2026-10-17T00:35:45.250Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/baa0db3d7713247b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/befcd2a14e1729b8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7928550cdc9baf8a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/23b422fc6d55b67f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b0e16fdda49563d8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b2c698053fb4ef7f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4c86d0e9a38e9337.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d8e3498b345e7b53.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4cd8beb2dc175456.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8e2e48002bb05bc9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6cf97c0561446bda.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0685407cbcc4f62c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9a4c3d0ddbb7cff2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3dc5f692c8c86523.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c8695032abc1443c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7bb3bb9ce46d92fc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/206f5dd384cf71b8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6ea2ebefeeaa8688.txt
```


## [2026-10-17T00:35:49.161Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -18 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'],d['bytes'],d['url'][:70])\"; for f in baa0db3d7713247b befcd2a14e1729b8 7928550cdc9baf8a 23b422fc6d55b67f; do echo \"-- $f\"; grep -i -m3 -A3 \"Etymology\" $f.txt | head -12; done"
}
```


### [2026-10-17T00:35:49.597Z] TOOL RESULT

```
-1 39 https://en.wiktionary.org/wiki/𐬫𐬁𐬙𐬎
200 9624 https://en.wiktionary.org/wiki/यातु
200 6836 https://en.wiktionary.org/wiki/ζῆλος
-1 39 https://www.etymonline.com/word/zeal
-1 39 https://www.etymonline.com/word/jealous
200 5615 https://en.wiktionary.org/wiki/ایزد
200 646 https://vajehyab.com/amid/آنزیم
200 5070 https://en.wiktionary.org/wiki/یزدان
200 6629 https://en.wiktionary.org/wiki/جشن
-1 39 https://en.wiktionary.org/wiki/یزدگرد
200 6545 https://en.wiktionary.org/wiki/ἁγνός
200 11356 https://en.wiktionary.org/wiki/agnus
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeh₂
200 7037 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-yōs
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/yáȷ́a
200 2017 https://en.wiktionary.org/wiki/یاسه
-1 39 https://www.etymonline.com/word/agnus%20castus
200 2474 https://en.wiktionary.org/wiki/Yasna
-- baa0db3d7713247b
 Etymology 

 1.2 
 Proper noun 
--
 Etymology 

 3.3 
 Noun 
--
 Etymology 

-- befcd2a14e1729b8
-- 7928550cdc9baf8a
 Etymology 

 1.2 
 Pronunciation 
--
 Etymology 1 

 3.2.1 
 Pronunciation 
--
 Etymology 2 

-- 23b422fc6d55b67f
 Etymology 

 1.2 
 Pronunciation 
--
 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *yeh₂-
```


## [2026-10-17T00:35:55.145Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in baa0db3d7713247b 7928550cdc9baf8a 23b422fc6d55b67f 4c86d0e9a38e9337 d8e3498b345e7b53 4cd8beb2dc175456 6cf97c0561446bda 0685407cbcc4f62c 3dc5f692c8c86523 7bb3bb9ce46d92fc 6ea2ebefeeaa8688; do echo \"=== $f\"; python3 -c \"\nimport re,sys\nt=open('$f.txt').read()\nfor m in re.finditer(r'Etymology[^\\n]*\\n\\s*\\[ edit \\]',t):\n    print(re.sub(r'\\s+',' ',t[m.end():m.end()+700])); print('..')\n\" | head -c 1800; echo; done"
}
```


### [2026-10-17T00:35:56.213Z] TOOL RESULT

```
=== baa0db3d7713247b
 (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) Proper noun [ edit ] جَادُو • ( jādū ) f a town in north-western Libya Baluchi [ edit ] Noun [ edit ] جادو • ( jádú ) magic enchantment See also [ edit ] جاتو ( játú ) سحر ( sihr, sahr ) جادوگر سحرگو ( sahargo ) سحر کنوخ ( sihr kanox ) Old Anatolian Turkish [ edit ] Alternative forms [ edit ] جاذو ( cazu ) Etymology [ edit ] Borrowed from Classical Persian جادو ( jādū ) . Noun [ edit ] جادو • ( cadu ) sorcerer / sorceress fair eye Descendants [ edit ] Azerbaijani: cadu Gagauz: cadı Ottoman Tur
..
 Borrowed from Classical Persian جادو ( jādū ) . Noun [ edit ] جادو • ( cadu ) sorcerer / sorceress fair eye Descendants [ edit ] Azerbaijani: cadu Gagauz: cadı Ottoman Turkish: جادو ( cadu, cadı ) , جاذو ( cazı ) , جادی ( cadu, cadı ) , جاذی ( cazı ) Turkish: cadı → Armenian: ջազի ( ǰazi ) → Bulgarian: джади́я ( džadíja ) , джиди́я ( džidíja ) → Laz: ჯაზი ( cazi ) , ჯადი ( cadi ) — Lome → Macedonian: џадија ( džadija ) → Serbo-Croatian: Cyrillic script: џа̀дија Latin script: džàdija Further reading [ edit ] Pomorska, Marzanna ( 2013 ), Materials for a Historical Dictionary of New Persian Loanwords in Old Anatolian and Ottoman Turkish from the 1
..
 Etymology tree Proto-Indo-Iranian *yaHtúš Old Persian 𐎹𐎠𐎬𐎢 ( y-a-tu-u /⁠yātu⁠/ ) Middle Persian 𐭩𐭠𐭲𐭥𐭪𐭠 ( yʾtʿkʾ /⁠ǰādūg⁠/ ) Classical Persian جادو ( jādū ) Old Anatolian Turkish جادو ( cadu ) Ottoman Turkish جادو Inherited from Old Anatolian Turkish جادو ( cadu ) , from Classical Persian جادو ( jād�
=== 7928550cdc9baf8a
 Learned borrowing from Sanskrit यातु ( yātú ) . Doublet of जादू ( jādū ) . Pronunciation [ edit ] ( Standard Hindi ) IPA ( key ) : /jɑː.t̪uː/ , [jäː.t̪uː] Noun [ edit ] यातु • ( yātu ) m ( rare , formal ) one who goes or wanders a demon , rakshasa witchcraft , black magic Declension [ edit ] Declension of यातु (masc u-stem) singular plural direct यातु yātu यातु yātu oblique यातु yātu यातुओं yātuõ vocative यातु yātu यातुओ yātuo References [ edit ] Dāsa, Śyāmasundara ( 1965–1975 ), “ यातु ”, in Hindī Śabdasāgara [ lit. “Sea of Hindi words” ] (in Hindi), Kashi [ Varanasi ] : Nagari Pracarini Sabha McGregor, Rona
..
 From Proto-Indo-Iranian *yaHtúš ( “ magic, witchcraft, sorcery ” ) , possibly from Proto-Indo-European *yeh₁- ( “ to do, make, act vigorously ” ) . Cognate with Avestan 𐬫𐬁𐬙𐬎 ( yātu ) , Old Persian 𐎹𐎠𐎬𐎢 ( yātu ) (whence Persian جادو ( jâdu , “ magic ” ) ). Pronunciation [ edit ] ( Vedic ) IPA ( key ) : /jɑː.tú/ ( Classical Sanskrit ) IPA ( key ) : /jɑː.t̪u/ Noun [ edit ] या॒तु • ( yātú ) stem , m witchcraft , black magic c. 1500 BCE – 1000 BCE , Ṛgveda 5.12.2 : नाहं यातुं सहसा न द्वयेन ऋतं सपाम्यरुषस्य वृष्णः ॥ nāhaṃ yātuṃ sahasā na dvayena ṛtaṃ sapāmyaruṣasya vṛṣṇaḥ. I use no sorcery with might or falsehood; the sacred Law of the Red Steer I follow. a kind of evi
..
 Prakritism of यातृ॑ ( yā́tṛ , “ going, travelling ” ) . Pronunciation [ edit ] ( Classical Sanskrit ) IPA ( key ) : /jɑː.t̪u/ Noun [ edit ] यातु • ( yātu ) stem 
=== 23b422fc6d55b67f
 Etymology tree Proto-Indo-European *yeh₂- Proto-Indo-European *-los Proto-Indo-European *yéh₂los Ancient Greek ζῆλος From Proto-Indo-European *yeh₂- ( “ to go, travel, search, inquire ” ) . Related to Ζητήρ ( Zētḗr ) . [ 1 ] Pronunciation [ edit ] IPA ( key ) : /zdɛ̂ː.los/ → /ˈzi.los/ → /ˈzi.los/ ( 5 th BCE Attic ) IPA ( key ) : /zdɛ̂ː.los/ ( 1 st CE Egyptian ) IPA ( key ) : /ˈze̝.los/ ( 4 th CE Koine ) IPA ( key ) : /ˈzi.los/ ( 10 th CE Medieval ) IPA ( key ) : /ˈzi.los/ ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈzi.los/ Noun [ edit ] ζῆλος • ( zêlos ) m ( genitive ζήλου ) ; second declension eager rivalry , zealous imitation , emulatio
..

=== 4c86d0e9a38e9337
 From Avestan 𐬫𐬀𐬰𐬀𐬙𐬀 ( yazata , “ worthy of reverence, worthy of devotion, worthy of worship ” ) . Compare Sanskrit यजत ( yajata ) and Classical Syriac ܝܙܕ . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ʔeː.ˈzad/ , /ʔeː.ˈzid/ ( Dari, formal ) IPA ( key ) : [ʔeː.zäd̪] , [ʔeː.zɪd̪] ( Dari, formal ) IPA ( key ) : [ʔeː.zäd̪] , [ʔeː.zɪd̪] ( Kabuli ) IPA ( key ) : [ʔeː.zäd̪] , [ʔeː.zɪd̪] ( Hazaragi ) IPA ( key ) : [ʔeː.zäd̪̥] , [ʔi.zid̪̥] ( Iran, formal ) IPA ( key ) : [ʔiː.zæd̪̥] , [ʔiː.zed̪̥] ( Tajik, formal ) IPA ( key ) : [ʔe.zäd̪] , [ʔe.zid̪] Rhymes: -ad , -id Readings Classical reading ? ēzad, ēzid Dari reading ? ēzad, ēzid Iranian r
..
 From Classical Persian ایزد ( ēzad , “ God ” ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /iː.zɪd̪/ , /eː.zɪd̪/ Proper noun [ edit ] ایزد • ( īzid or ezid ) m God Synonyms [ edit ] خدا ( xudā ) Derived terms [ edit ] ایزدی ( īzidī , “ Godly ” ) اِیزِد پَناہ ( īzid-panāh , “ protected by God ” ) References [ edit ] “ ایزد ”, in اُردُو لُغَت ( urdū luġat ) (in Urdu), Ministry of Education: Government of Pakistan, 2017 . “ ایزد ”, in ریخْتَہ لُغَت ( rexta luġat ) - Rekhta Dictionary [ Urdu dictionary with meanings in Hindi & English ] , Noida, India: Rekhta Foundation, 2026 . Retrieved from " https://en.wiktionary.org/w/index.php?ti
..

=== d8e3498b345e7b53
 Borrowed from Persian یزدان ( yazdân ) . Proper noun [ edit ] یزدان • ( Yezdan ) ( Zoroastrianism ) God , the creator of good References [ edit ] Redhouse, James W. ( 1890 ), “ یزدان ”, in A Turkish and English Lexicon ‎ [1] , Constantinople: A. H. Boyajian, page 2202 Persian [ edit ] Persian Wikipedia has an article on: یزدان Wikipedia fa Etymology [ edit ] From Middle Persian yẕdʾn' ( yazdān , “ gods, spirits ” ) , ultimately from Proto-Indo-European *yeh₁ǵ- ( “ to revere, worship, sacrifice ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /jaz.ˈdaːn/ ( Dari, formal ) IPA ( key ) : [jäz.d̪ɑ́ːn] ( Dari, formal ) IPA ( key ) : [
..
 From Middle Persian yẕdʾn' ( yazdān , “ gods, spirits ” ) , ultimately from Proto-Indo-European *yeh₁ǵ- ( “ to revere, worship, sacrifice ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /jaz.ˈdaːn/ ( Dari, formal ) IPA ( key ) : [jäz.d̪ɑ́ːn] ( Dari, formal ) IPA ( key ) : [jäz.d̪ɑ́ːn] ( Kabuli ) IPA ( key ) : [jäz.d̪ɑ́ːn] ( Hazaragi ) IPA ( key ) : [jäz.d̪ɔ́ːn] ( Iran, formal ) IPA ( key ) : [jæz.d̪ɒ́ːn] ( Tajik, formal ) IPA ( key ) : [jäz.d̪ɔ́n] Rhymes: -aːn Readings Classical reading ? yazdān Dari reading ? yazdān Iranian reading ? yazdân Tajik reading ? yazdon Noun [ edit ] Dari یزدان Iranian Persian Tajik
..
 Borrowed from Classical Persian یزدان ( yazdān ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /jəz.d̪ɑːn/ Noun [ edit ] یزدان • ( yazdān ) ? God , the creator of good, Goddess of righteousness Retrieved from " https://en.wiktionary.org/w/index.php?title=یزدان&oldid=93354439 " Categories : Ottoman Turkish terms derived from Persian Ottoman Turkish terms borrowe
=== 4cd8beb2dc175456
 From Middle Persian [Book Pahlavi needed] ( yšn' /⁠jašn⁠/ ) , from Old Persian *yašnah , from Proto-Iranian *Hyajnáh ( “ worship, sacrifice ” ) . [ 1 ] Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ˈd͡ʒaʃn/ ( Dari, formal ) IPA ( key ) : [d͡ʒäʃn] ( Dari, formal ) IPA ( key ) : [d͡ʒäʃn] ( Kabuli ) IPA ( key ) : [d͡ʒäʃn] ( Hazaragi ) IPA ( key ) : [d͡ʒäʃn] ( Iran, formal ) IPA ( key ) : [d͡ʒæʃn] ( Tajik, formal ) IPA ( key ) : [d͡ʒäʃn] Rhymes: -aʃn Readings Classical reading ? jašn Dari reading ? jašn Iranian reading ? jašn Tajik reading ? jašn Audio ( Iran ) : ( file ) Noun [ edit ] Dari جشن Iranian Persian Ta
..
 Borrowed from Classical Persian جَشْن ( jašn ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /d͡ʒəʃ(.ə)n/ Rhymes: -əʃn Hyphenation: جَشْن Noun [ edit ] جَشْن • ( jaśn ) m ( Hindi spelling जशन ) banquet , feast festival , celebration Declension [ edit ] Declension of جشن singular plural direct جَشْن ( jaśn ) جَشْن ( jaśn ) oblique جَشْن ( jaśn ) جَشْنوں ( jaśnõ ) vocative جَشْن ( jaśn ) جَشْنو ( jaśno ) Derived terms [ edit ] جَشْنِ آزادی ( jaśn-i āzādī , “ independence day ” ) جَشْنِ بَہاران ( jaśn-i bahārān , “ spring celebration ” ) جَشْنِ بُزُرْگ ( jaśn-i buzurg , “ Persian new year ” ) جَشْنِ سال گِر
..

=== 6cf97c0561446bda
 From Proto-Hellenic *hagnós , from Proto-Indo-European *h₁yáǵ-nós , from *h₁yaǵ- ( “ to sacrifice; to worship ” ) . Cognate with Proto-Indo-Iranian *Hyaȷ́nás . Pronunciation [ edit ] IPA ( key ) : /ha.ɡnós/ → /aˈɣnos/ → /aˈɣnos/ ( 5 th BCE Attic ) IPA ( key ) : /ha.ɡnós/ ( 1 st CE Egyptian ) IPA ( key ) : /(h)aˈɡnos/ ( 4 th CE Koine ) IPA ( key ) : /aˈɣnos/ ( 10 th CE Medieval ) IPA ( key ) : /aˈɣnos/ ( 15 th CE Constantinopolitan ) IPA ( key ) : /aˈɣnos/ Adjective [ edit ] ᾰ̔γνός • ( hăgnós ) m ( feminine ᾰ̔γνή , neuter ᾰ̔γνόν ) ; first / second declension pure ; chaste holy ; sacred purifying Declension [ edit ] First and second declension o
..

=== 0685407cbcc4f62c
 A user suggests that this Latin entry be cleaned up, giving the reason: “quotes should be expanded and new ones added” . Please see the discussion on Requests for cleanup ( + ) for more information and remove this template after the problem has been dealt with. From Proto-Italic *agʷnos , from Proto-Indo-European *h₂egʷnós ( “ lamb ” ) . [ 1 ] Cognates include Ancient Greek ἀμνός ( amnós ) , Old Church Slavonic агнѧ ( agnę ) , Old English ēanian (English yean ), and Albanian enjë . Pronunciation [ edit ] ( Classical Latin ) IPA ( key ) : [ˈaŋ.nʊs] ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈaɲ.ɲus] Noun [ edit ] agnus m ( genitive agnī , feminine agna ) 
..
 A verbal adjective from an unattested root *ag- ("to drive"), paralleled by Old Irish án ( “ quick ” ) < *ag-nos , Sanskrit अजिर ( ajirá- , “ agile, quick ” ) . Ultimately from Proto-Indo-European *h₂eǵ- ( “ to drive ” ) ; compare Old Irish aigid , Sanskrit अजति ( ajati ) . The Lithuanian form appears to have undergone depalatalization before the nasal . [ 1 ] The connection with Russian яглый ( jaglyj , “ active, energetic ” ) is rejected by Vasmer. [ 2 ] Pronunciation [ edit ] IPA ( key ) : /ɐɡˈnʊs/ Adjective [ edit ] agnùs m ( feminine agni̇̀ , neuter agnù ) stress pattern 4 ( Samogitian ) agile , energetic Declension [ edit ] Non-pronominal forms of agnùs
..

=== 3dc5f692c8c86523
 For **-yoss (stem + nominative *-s ). It was directly added to the e -grade root (if there was one) rather than to the stem of the adjective. This suffix was possibly innovated after Anatolian and Tocharian split off. [ 1 ] Suffix [ edit ] *-(é)-yōs [ 2 ] Forms adjectives from roots, meaning "very" or "rather". Usage notes [ edit ] Adverbs were formed by using the stem, *-yos- , without any ending. Declension [ edit ] Athematic, acrostatic masculine feminine nominative *-(é)-yōs *-(é)-yesih₂ genitive *-(é)-isos *-(é)-isyeh₂s masculine singular dual plural nominative *-(é)-yōs *-(é)-yosh₁(e) *-(é)-yoses vocative *-(é)-yos 
..

=== 7bb3bb9ce46d92fc

=== 6ea2ebefeeaa8688
 Transliteration of Avestan 𐬫𐬀𐬯𐬥𐬀 ( yasna , “ oblation; worship ” ) . Doublet of yajna . Proper noun [ edit ] Yasna ( Zoroastrianism ) The primary liturgical collection of texts of the Avesta . ( Zoroastrianism ) The principal Zoroastrian act of worship at which those verses are recited. Anagrams [ edit ] Sanya , Yanas , yanas Retrieved from " https://en.wiktionary.org/w/index.php?title=Yasna&oldid=90660181 " Categories : English terms borrowed from Avestan English transliterations of Avestan terms English terms derived from Avestan English doublets English lemmas English proper nouns English uncountable nouns en:Zoroastrianism Hidden categories: Ave
..
```


## [2026-10-17T00:36:03.644Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -A6 \"^ *Persian\" baa0db3d7713247b.txt | head -40; cat 7bb3bb9ce46d92fc.txt | head -40"
}
```


### [2026-10-17T00:36:03.956Z] TOOL RESULT

```
119: Persian 
120-
121- Toggle Persian subsection 
122-
123- 5.1 
124- Etymology 
125-
--
378: Persian
379- [ edit ] 
380-
381- Etymology
382- [ edit ] 
383-
384- Etymology tree
--
389: Persian جادو 
390-
391- Inherited from Middle Persian 𐭩𐭠𐭲𐭥𐭪𐭠 ( yʾtʿkʾ /⁠ǰādūg⁠/ , “ wizardry; wizard ” ) , from Old Persian 𐎹𐎠𐎬𐎢 ( y-a-tu-u /⁠yātu⁠/ ) , from Proto-Indo-Iranian *yaHtúš . Cognate with Sanskrit या॒तु ( yātú ) .
392-
393- Pronunciation
394- [ edit ] 
395-
--
579: Persian terms derived from Old Persian 
580: Persian terms derived from Middle Persian 
581: Persian terms derived from Proto-Indo-Iranian 
582: Persian terms inherited from Proto-Indo-Iranian 
583: Persian terms inherited from Middle Persian 
584: Persian terms inherited from Old Persian 
585: Persian terms with IPA pronunciation 
586- Rhymes:Persian/uː 
587- Rhymes:Persian/uː/2 syllables 
588: Persian lemmas 
589: Persian nouns 
590: Persian terms with archaic senses 
591: Persian terms with quotations 
592: Persian terms with obsolete senses 
593- Urdu terms derived from Middle Persian 
594- Urdu terms derived from Proto-Indo-Iranian 
URL: https://en.wiktionary.org/wiki/یاسه
FETCHED: 2026-10-17T00:35:44Z
STATUS: 200
TITLE: یاسه - Wiktionary, the free dictionary

یاسه - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in
```


## [2026-10-17T00:36:09.328Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/zeal' 'https://en.wiktionary.org/wiki/jealous' 'https://en.wiktionary.org/wiki/Yazdegerd' 'https://en.wiktionary.org/wiki/जादू' 'https://en.wiktionary.org/wiki/Agnes' 'https://en.wiktionary.org/wiki/𐬫𐬀𐬰𐬀𐬙𐬀'; do python3 tools/fetch_source.py \"$u\" --note \"page 561 fetch\" 2>&1|tail -1; done; tail -6 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'],d['bytes'],d['file'],d['url'][:60])\""
}
```


### [2026-10-17T00:36:12.444Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d1a064bfab172ce6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4ea56a37a7c382a1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8417aa345e189e6a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/29acbda8f2a55b58.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bab13fce0fe3b60f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8e8f74c4d660ee82.txt
200 12665 data/verification/sources/web/d1a064bfab172ce6.txt https://en.wiktionary.org/wiki/zeal
200 19375 data/verification/sources/web/4ea56a37a7c382a1.txt https://en.wiktionary.org/wiki/jealous
200 3822 data/verification/sources/web/8417aa345e189e6a.txt https://en.wiktionary.org/wiki/Yazdegerd
200 6985 data/verification/sources/web/29acbda8f2a55b58.txt https://en.wiktionary.org/wiki/जादू
200 17040 data/verification/sources/web/bab13fce0fe3b60f.txt https://en.wiktionary.org/wiki/Agnes
200 3495 data/verification/sources/web/8e8f74c4d660ee82.txt https://en.wiktionary.org/wiki/𐬫𐬀𐬰𐬀𐬙𐬀
```


## [2026-10-17T00:36:17.443Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in d1a064bfab172ce6 4ea56a37a7c382a1 8417aa345e189e6a 29acbda8f2a55b58 bab13fce0fe3b60f 8e8f74c4d660ee82; do echo \"=== $f\"; python3 -c \"\nimport re\nt=open('$f.txt').read()\nfor m in list(re.finditer(r'Etymology[^\\n]*\\n\\s*\\[ edit \\]',t))[:2]:\n    print(re.sub(r'\\s+',' ',t[m.end():m.end()+500])); print('..')\n\"; done"
}
```


### [2026-10-17T00:36:18.018Z] TOOL RESULT

```
=== d1a064bfab172ce6
 From Middle English zele , from Old French zel , from Late Latin zēlus , from Ancient Greek ζῆλος ( zêlos , “ zeal, jealousy ” ) , from Proto-Indo-European *yeh₂- ( “ to search ” ) . Related to jealous . Noun [ edit ] zeal ( countable and uncountable , plural zeals ) The fervour or tireless devotion for a person, cause, or ideal and determination in its furtherance; diligent enthusiasm ; powerful interest . Synonyms: ardour , eagerness , enthusiasm , intensity , passion Antonym: 
..
 (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) Noun [ edit ] zeal ( uncountable ) ( uncommon ) A light zomp . zeal: Anagrams [ edit ] Elza , Zale , laze , zale Retrieved from " https://en.wiktionary.org/w/index.php?title=zeal&oldid=93622404 " Categories : English 1-syllable words English terms with IPA pronunciation English terms with audio pronunciation Rhymes:English/iːl Rhymes:English/iːl/1 syllabl
..
=== 4ea56a37a7c382a1
 First attested in 1382. From Middle English jelous , gelous , gelus , from Old French jalous , from Late Latin zelosus , from Ancient Greek ζῆλος ( zêlos , “ zeal, jealousy ” ) . Doublet of zealous . Pronunciation [ edit ] ( Received Pronunciation , General American , Canada ) IPA ( key ) : /ˈd͡ʒɛl.əs/ Audio ( Southern England ) : ( file ) Audio ( California ) : ( file ) Audio ( Texas ) : ( file ) Audio ( Connecticut ) : ( file ) ( Australia , New Zealand ) IPA ( key ) : 
..
=== 8417aa345e189e6a
 From 𐭩𐭦𐭣𐭪𐭫𐭲𐭩 ( yzdklty ) / Middle Persian 𐭩𐭦𐭣𐭪𐭥𐭲𐭩 ( Yazdegerd, Yazdgird , literally “ made by God ” ) , from 𐭩𐭦𐭣 ( Yazd ) + 𐭪𐭥𐭲𐭩 ( -gird, -kirt ) . Proper noun [ edit ] Yazdegerd A transliteration of the Middle Persian male given name 𐭩𐭦𐭣𐭪𐭫𐭲𐭩 ( yzdklty ) or 𐭩𐭦𐭣𐭪𐭥𐭲𐭩 ( Yazdegerd, Yazdgird ) , notably borne by several Sasanian kings . Translations [ edit ] given name Arabic: يَزْدَجِرْد ( yazdajird ) Aramaic: Classical Syriac: ܝܙܕܓܪܕ ( Yazdgerd ) Armenian: Հազկերտ ( Hazk
..
=== 29acbda8f2a55b58
 Borrowed from Classical Persian جادو ( jādū ) , from Proto-Indo-Iranian *yaHtúš . Doublet of यातु ( yātu ) . Compare Assamese যাদু ( zadu ) , Bengali জাদু ( jadu ) , Marathi जादू ( jādū ) . Pronunciation [ edit ] ( Standard Hindi ) IPA ( key ) : /d͡ʒɑː.d̪uː/ , [d͡ʒäː.d̪uː] Noun [ edit ] जादू • ( jādū ) m ( Urdu spelling جادو ) jadoo ; magic ; witchcraft incantation जादू चलाना ― jādū calānā ― to cast a spell charm Declension [ edit ] Declension of जादू (masc ū-
..
 Borrowed from Classical Persian جادو ( jādū ) . Pronunciation [ edit ] IPA ( key ) : [d͡ʒɑːduː] Noun [ edit ] जादू • ( jādū ) ( Latin script jadu , Kannada script ಜಾದೂ ) magic Synonyms: चमत्कार ( camatkār ) , अजाप ( ajāp ) References [ edit ] Pushpak Bhattacharyya ( 2017 ), IndoWordNet ‎ [1] Isidore Dantas; Joel D'Souza ( 2015 ), Modern English–Konkani Dictionary ‎ [2] , Margao, Goa: Golden Heart Emporium Books, →ISBN , page 210 Marathi [ edit ] Marathi Wik
..
=== bab13fce0fe3b60f
 Borrowed from Ancient Greek Ἁγνή ( Hagnḗ ) , coming from Ancient Greek ἁγνός ( hagnós , “ pure, chaste ” ) , Ancient Greek ἁγνεία ( hagneía , “ purity, chastity ” ) . Doublet of Inez . Pronunciation [ edit ] IPA ( key ) : /ˈæɡ.nɪs/ Audio ( UK ) : ( file ) Proper noun [ edit ] Agnes A female given name from Ancient Greek . 1876 , Annie Howells Fréchette, “Reuben Dale”, in The Galaxy , W.C. and F.P.Church, 1876, page 394 : Why do you call Mrs. Stone Aggie? Agnes is such a b
..
 Borrowed from Ancient Greek Ἁγνή ( Hagnḗ ) , coming from Ancient Greek ἁγνός ( hagnós , “ pure, chaste ” ) Pronunciation [ edit ] IPA ( key ) : /ˈaː.ɡnəs/ , /ˈaːk.nəs/ IPA ( key ) : /ˈax.nəs/ ( northern and central Germany; now chiefly colloquial ) Audio ( Germany ( Berlin ) ) : ( file ) Proper noun [ edit ] Agnes f ( proper noun , genitive Agnes' or ( older ending ) Agnesens , plural Agnes ) a female given name from Ancient Greek, equivalent to English Agnes Decl
..
=== 8e8f74c4d660ee82
 From the verbal root 𐬫𐬀𐬰 ( yaz , “ to worship, honor, venerate ” ) , from Proto-Indo-European *h₁yaǵ- ( “ to worship, revere, sacrifice ” ) . The nominative form is 𐬫𐬀𐬰𐬀𐬙𐬋 ( yazatō ) , pl. 𐬫𐬀𐬰𐬀𐬙𐬂𐬢𐬵𐬋 ( yazatåŋhō ) , reflecting Proto-Iranian *yazatah and pl. *yazatāhah . Compare Sanskrit यजत ( yajata ) . Pronunciation [ edit ] IPA ( key ) : /jazata/ Noun [ edit ] 𐬫𐬀𐬰𐬀𐬙𐬀 • ( yazata ) m ( Zoroastrianism ) yazata , something worthy of veneration . Related terms [ edit ] 𐬫
..
```


## [2026-10-17T00:36:22.988Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"جادو\" \"یاسه\" \"ایزد\" \"جشن\" \"یزدگرد\" \"یسنا\"; do echo \"-- MON $w\"; grep -h -m2 -E \"^ *$w[ ‌(\\[]\" MON_part1.txt MON_part2.txt | cut -c1-250; done; for w in \"جادو\" \"جشن\" \"ایزد\" \"یزدان\" \"یسنا\"; do echo \"-- ARY $w\"; grep -n -m2 \"$w\" incoming/ARY/ARY_pages.txt | cut -c1-200; done"
}
```


### [2026-10-17T00:36:23.437Z] TOOL RESULT

```
-- MON جادو
(eval):1: invalid subscript
-- MON یاسه
(eval):1: invalid subscript
-- MON ایزد
(eval):1: invalid subscript
-- MON جشن
(eval):1: invalid subscript
-- MON یزدگرد
(eval):1: invalid subscript
-- MON یسنا
(eval):1: invalid subscript
-- ARY جادو
14102:چم این واژه در دیگر زبان‌های هند و اروپایی این فهرست: جادوگر» تواناه دانا,
-- ARY جشن
10759:۴ سور (به چم *جشن و مهمانی" *خوراک") :
10776:چم این واژه در زبان بلوچی: جشن عروسی
-- ARY ایزد
940:ایزدسازی عوامل طبیعی (ماه و خورشید و توفان و غیره) استوار بود. مثلاً واژه‌ی «شاه» در شش زبان
-- ARY یزدان
953:رسید که اساس فرهنگك و جامعه‌ی هند و اروپایی بر سه انديشه استوار است: ۱-روحانی و یزدانی ۲-
-- ARY یسنا
12573:گوتیکه ش یسنان با پبگشت‌ل ۸8۳8۴8۷۵۵۶
```


## [2026-10-17T00:36:27.253Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    t=open(f).read()\n    for w in ['جادو','یاسه','ایزد','جشن','یزدگرد','یسنا']:\n        for m in re.finditer(r'(?m)^\\s*'+w+r'\\s*[\\(\\[]',t):\n            print(f,w,'::',t[m.start():m.start()+220].replace('\\n',' ')); break\nE\nsed -n 14095,14104p incoming/ARY/ARY_pages.txt | cut -c1-250"
}
```


### [2026-10-17T00:36:28.088Z] TOOL RESULT

```
MON_part2.txt جشن :: جشن (مانند نوروز). (امر.) نوعی اتشباری.  (بز.) مخملکث» سرخکک و ابله مرغان.  گلاگل: اموقامج (.) (عم.) شکم سخت پیش  آمده (آستن) (لخ.)    گلاگونه: (6-)22 ۸201-1-11 اک و ۳    سیر    گلغو نه |(امر.) ماده‌ای سرخ رن که زنان بر 
ٍ موه
پسگشت‌ها ۸/5 6 (۸]061131۸30) ۱۸۲۲62/2:۱10677
۳ :0100/8
ات ان 6 (۸1001111۸30) ۱10613
2 1۸60 ,616ها) برهان قاطع : ۳۳۰
یادداشت.
۱- چم این واژه در زبان‌های ایرانی: روحانی زرتشتی,
چم این واژه در دیگر زبان‌های هند و اروپایی این فهرست: جادوگر» تواناه دانا,
چم این واژه در سانسکریت: توانمندی» دارایی.
۲- واژه‌های انگلیسی 81۸010 ,1۸01۳01۸۷ نیز از همین واجریشه‌اند.
```


## [2026-10-17T00:36:35.104Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"z[eē]los|yātu|yatu-|jādū\" IEC.txt | cut -c1-300 | head -5; grep -n -i -E \"i̯ā-|ja- .*eifer|ζῆλος|zēlos\" incoming/WLD/WLD_Bd1_pages.txt | head -5; grep -n -E \"zēlos|ζῆλος|jag-|iag-|yātu|jātu\" WLD_band3.txt | head -5"
}
```


### [2026-10-17T00:36:35.572Z] TOOL RESULT

```
6353:iät- “power, force’ Skt. yàtüh ‘sorcery; demon’; Av. yātus “magi- cian’; yātu ‘demon’; Per. jådu ‘magic’ (j = £); Tokh. AB yāt- ‘tame, overpower; be able’; Gk. cf. zētrós ‘executioner
```


## [2026-10-17T00:36:41.175Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; python3 - <<'E'\nt=open('WLD_Bd1_pages.txt').read().split('\\f')\nimport re\nfor leaf in range(202,208):\n    p=t[leaf]\n    for k in ['yātu','yatu','jätu','yätu','ζῆλος','ζηλος','yaz','yajati','yajati','άγνός','ayvos','hagn','jag-','jā-']:\n        i=p.find(k)\n        if i>=0: print(leaf,leaf-9+1,k,'::',p[max(0,i-150):i+150].replace('\\n',' ')); break\nE"
}
```


### [2026-10-17T00:36:41.538Z] TOOL RESULT

```
203 195 yajati :: o, xeorgov. so dab „heilen“ aus „einschneiden, chirurgisch behan- deln" entwiokelt und xo ay.og postverbal ware).    iag- „religios verehren".    Ai. yajati „verehrt mit          Gebet und Opfer" (Pf. tje. Ptc. istci-) = av. ya- zaite       ds.     (Ptc. yasta-mit Hochstufe naeh dem Praesens), ai. s
204 196 yaz :: er Begriff ..Kind, Sohn" wohl aus „der muntere, bewegliehe" entwickelt sei; jedenfalls entspricht                        der letzteren Yerwendung av. yazus pu&ro „der jiingste Sohn",                 yezivi     dugsdrqm „die       jiingste der Tochter" (field ner KZ. 28, 195, Bartholomae Airan. Wb. 1
205 197 yatu :: cht“,        Ad-iatu-marus, Ad-iatunnus Ad-ietu-                                        gall.                                    ,  auus     (: ai.   yatu-na-), nasaliert (vgl. mit Nasalsuffix ai. yat-nd-) cymr. add-  iant „Sehnsucht", ir. Ut (nir. end) „Eifer, Eifersucht", gall. Jantu-mdros (= ir.
```


## [2026-10-17T00:36:45.986Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; python3 - <<'E'\nt=open('WLD_Bd1_pages.txt').read().split('\\f')\np=t[205]\nfor k in ['Zauber','yātu','yatu-m','ya-tu','Wunsch','jädu']:\n    i=p.find(k)\n    print(k,i, p[max(0,i-300):i+200].replace('\\n',' ') if i>=0 else '')\np=t[203]; i=p.find('ayvo'); i2=p.find('yasna'); print(p[i2-100:i2+300].replace('\\n',' '))\nE"
}
```


### [2026-10-17T00:36:46.348Z] TOOL RESULT

```
Zauber 3479 ung bei Solmsen aaO. ved. ytlvan- etwa ,,Angreifer,                                                       ;      Yerfolger", yatdr- etwa „Riicher" (Avaf /<;’.), run yd-, -ydcan-, -ynt- ,,eine   Schuld rachend" (immerhin in ihrer Zugehorigkeit ziemlich wahrscheinlich),   ai. yutu- m. „Spuk, Hexerei, Zauberdiimon". av. ycdu- m. .,Zauberei, Be-    hexung; Zauberer“, npers. jildn „Zauberer" (kann aus dem Begriff ,.auf  jemanden losgehn" geflossen sein), ferner aksl. jan „acaTt]g<k. streng, herb",  j
yātu -1 
yatu-m -1 
ya-tu -1 
Wunsch -1 
jädu -1 
ajas- „verehrend" = gr. dyog n. „Yer-  ehrung. Opfer", jz avayyg „ganz heilig";    ai. yajna-h  av. yasna- m. „Gottesverehrung, Opfer“ ( yajmya                          ,                                                                       av. yas- nya- „opferwiirdig, zum Opfer gehorig"), gr. ayvog „heilig, rein, lauter".    Lit. z. B. bei Boisacq 7.      Ohne zureichenden Grund bestritten von Me
```


## [2026-10-17T00:37:11.797Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 49310 51896 57569 58013 65798; do awk -v n=$n 'NR<=n && /Root \\/ /{r=$0; rl=NR} NR>n && /Page\\(s\\)/{print n\": \"r\" | \"$0; exit}' POK_full.txt; done"
}
```


### [2026-10-17T00:37:12.451Z] TOOL RESULT

```
49310: Root / lemma: Rak-  | Page(s): 521-522 
51896: Root / lemma: Rrei-  | Page(s):618 
57569: Root / lemma: mahR- : mahR-  | Page(s): 699 
58013: Root / lemma: mehg(h)- : m^(h)-  | Page(s): 708-709 
65798: Maybe alb. {*pe-lagu) pe//gu^poo\' see Root / lemma: /aku-: water basin (ditch, lake, sea),  | Page(s): 798-801
```


## [2026-10-17T00:37:18.363Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg561.png data/verification/sources/refs/ocr/BOOK/561.png && echo ok"
}
```


### [2026-10-17T00:37:18.821Z] TOOL RESULT

```
ok
```


## [2026-10-17T00:40:00.479Z] TOOL CALL #67: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-561.py",
 "content": "import json\n\nW = {\n \"jadu\": \"https://en.wiktionary.org/wiki/جادو\",\n \"yatu_skt\": \"https://en.wiktionary.org/wiki/यातु\",\n \"jadu_hi\": \"https://en.wiktionary.org/wiki/जादू\",\n \"zelos\": \"https://en.wiktionary.org/wiki/ζῆλος\",\n \"zeal\": \"https://en.wiktionary.org/wiki/zeal\",\n \"jealous\": \"https://en.wiktionary.org/wiki/jealous\",\n \"izad\": \"https://en.wiktionary.org/wiki/ایزد\",\n \"yazdan\": \"https://en.wiktionary.org/wiki/یزدان\",\n \"jashn\": \"https://en.wiktionary.org/wiki/جشن\",\n \"yazdegerd\": \"https://en.wiktionary.org/wiki/Yazdegerd\",\n \"hagnos\": \"https://en.wiktionary.org/wiki/ἁγνός\",\n \"agnus\": \"https://en.wiktionary.org/wiki/agnus\",\n \"agnes\": \"https://en.wiktionary.org/wiki/Agnes\",\n \"yos\": \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-yōs\",\n \"yazata\": \"https://en.wiktionary.org/wiki/𐬫𐬀𐬰𐬀𐬙𐬀\",\n \"yasna\": \"https://en.wiktionary.org/wiki/Yasna\",\n}\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Yâ, Iâ 2\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *i̯ā- (Pokorny 501, 'heftig erregt sein; to be angry, punish'); AHD yā- 'to be aroused'; modern *yeh₂- 'to seek, strive' (Wiktionary, for ζῆλος)\",\n \"note\": \"The root, its label and the gloss 'to be aroused' come straight from Pokorny 501 and Watkins' AHD appendix (AHD 1985: 'yā-. To be aroused. Suffixed form *yā-lo- in Greek zēlos, zeal: JEALOUS, ZEAL. [Pok. iā- 501.]'). Pokorny puts Ved. yātú-, Av. yātu- 'sorcery, sorcerer', Av. yāsā 'wish' and Gk. ζῆλος under the same root, and Walde-Pokorny I 197 does the same. Modern sources split the group: Wiktionary derives ζῆλος from *yeh₂- 'to go, search' (related to ζητέω), and Sanskrit yātú- from Proto-Indo-Iranian *yaHtúš, 'possibly from PIE *yeh₁- to do, act vigorously'. Mann (IEC) gives yātu its own root *iāt- 'power, force', with Tocharian yāt- 'be able'. The Greek/English branch is secure. The Iranian branch is a classic Pokorny grouping that newer work no longer takes for granted. The chart's NOTE ('Sanskrit jadoo: sorcery', from a root 'Ei') is wrong: Hindi/Urdu jādū is a loan from Persian, and the native Sanskrit word is yātú-. The extraction matches the printed page. Note that 'Iâ' is a capital I, Nourai's spelling of i̯ā-.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *i̯ā- «برانگیخته شدن، به هیجان آمدن» را پوکورنی (ص ۵۰۱) و واتکینز در پیوست AHD با همین معنا آورده‌اند. هر دو سنسکریت yātu- و اوستایی yātu- «جادو، جادوگر»، اوستایی yāsā «خواهش» و یونانی ζῆλος «غیرت، شور» را زیر این ریشه گذاشته‌اند. پژوهش امروزی این گروه را یکپارچه نمی‌داند. ویکی‌واژه ζῆλος را از *yeh₂- «جستن، کوشیدن» و yātu را به احتمال از *yeh₁- «کوشیدن، کار کردن» می‌گیرد، و مان برای yātu ریشهٔ جداگانهٔ *iāt- «توان» پیشنهاد می‌کند. پس ادعای نورایی با احتیاط پذیرفتنی است. یادداشت نمودار دربارهٔ «jadoo» سنسکریت درست نیست، چون «جادو»ی هندی و اردو وام‌واژه‌ای از فارسی است.\",\n \"sources\": [W[\"zelos\"], W[\"yatu_skt\"], W[\"jadu_hi\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:501\", \"status\": \"supports\", \"note\": \"POK_full.txt (lemma 'i̯ā-', 'Meaning: to be angry; to be punish', Page(s): 501): 'Old Indic ... yā-tu-m. witchery, ghost, magic demon'; 'Avestan yā-tu-m. sorcery, magician, yā-sā wish'; 'gr. ζῆλος, Doric ζᾶλος m. eagerness, jealousy, envy'. These are exactly the root and branches on Nourai's chart.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1181\", \"stance\": \"supports\", \"note\": \"'yā-. To be aroused. Suffixed form *yā-lo- in Greek zēlos, zeal: JEALOUS, ZEAL. [Pok. iā- 501.]' This is the source of Nourai's gloss. AHD lists no Iranian derivative.\"},\n  {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt leaf 205 = Bd. I p. 197\", \"stance\": \"supports\", \"note\": \"Under iā-: 'ai. yātu- m. Spuk, Hexerei, Zauberdämon, av. yātu- m. Zauberei, Behexung; Zauberer, npers. jādū Zauberer (kann aus dem Begriff auf jemanden losgehn geflossen sein)'. This is the same grouping as Pokorny.\"},\n  {\"src\": \"IEC\", \"where\": \"IEC.txt line 6353\", \"stance\": \"contradicts\", \"note\": \"Mann gives a separate root: 'iāt- power, force. Skt. yātuḥ sorcery; demon; Av. yātus magician; Per. jādu magic; Tokh. AB yāt- tame, overpower; be able'. He does not link it to zēlos.\"}\n ],\n \"nodes\": [\n  {\n   \"id\": 1, \"lang\": \"Avestan\", \"words\": \"yâ-tu; yâsâ\", \"verdict\": \"plausible\",\n   \"derivation\": \"Av. yātu- m. means 'sorcery; sorcerer' (Bartholomae col. 1283 f.: 'yātav- m. 1) Zauberei, Behexung, 2) Zauberer'). It is an inherited Indo-Iranian *yaHtú-, the same word as Ved. yātú- 'sorcery, sorcery-demon', with OP yātu as well. Av. yāsā 'wish' belongs to the verb yās- 'to ask for, desire' (yāsaiti, Gathic), which Pokorny and Horn place under the same root *i̯ā- with an -s- (-sk̂-) extension. Both words are real. Whether they derive from *i̯ā- 'be aroused' is Pokorny's view. Wiktionary instead derives yātu from *yeh₁-, and Mann gives it a root *iāt-.\",\n   \"derivation_fa\": \"اوستایی yātu- به معنای «جادو، جادوگری؛ جادوگر» است (بارتولومه، ستون ۱۲۸۳). این واژه با سنسکریت ودایی yātú- یکی است و از هندوایرانی *yaHtú- می‌آید. اوستایی yāsā «خواهش، آرزو» از ستاک yās- «خواستن، درخواست کردن» است. پوکورنی و هرن هر دو را به ریشهٔ *i̯ā- می‌برند. وجود و معنای هر دو واژه درست است، اما پیوندشان با ریشهٔ «برانگیخته شدن» تنها با احتیاط پذیرفتنی است، چون ویکی‌واژه و مان برای yātu خاستگاه دیگری پیشنهاد می‌کنند.\",\n   \"sources\": [W[\"yatu_skt\"], W[\"jadu\"]],\n   \"ref_check\": [\n    {\"ref\": \"POK:501\", \"status\": \"supports\", \"note\": \"POK_full.txt, lemma i̯ā-, p. 501: 'Avestan yā-tu-m. sorcery, magician, yā-sā wish'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"BRT.txt line 21546 (col. 1283 f.)\", \"stance\": \"supports\", \"note\": \"'yātav- m. 1) Zauberei, Behexung ... 2) Zauberer'; 'n-p. jādū Zauberer'.\"},\n    {\"src\": \"ARP\", \"where\": \"ARP.txt §28 'Yatu' (p. 218)\", \"stance\": \"partial\", \"note\": \"Spiegel, Arische Periode: yātu occurs in both the Rigveda and the Avesta, 'zeigt das von yatu abgeleitete neup. jādū'. Etymology: 'nach der gewöhnlichen Ansicht von yā gehen mit dem Suffixe tu ... nach Weber hängt es mit yat, gr. ζητέω zusammen'. He confirms the word but gives other roots.\"},\n    {\"src\": \"IEC\", \"where\": \"line 6353\", \"stance\": \"contradicts\", \"note\": \"Mann: 'iāt- power, force ... Av. yātus magician' (separate root).\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 197\", \"stance\": \"supports\", \"note\": \"'av. yātu- m. Zauberei, Behexung; Zauberer' under iā-.\"}\n   ]\n  },\n  {\n   \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"žâtŭk; yâsak\", \"verdict\": \"transcription_suspect\",\n   \"derivation\": \"The Middle Persian word for 'sorcerer, magician' is Book Pahlavi y'twk, read jādūg (MacKenzie: 'jādūg [y'twk; M j'dwg, N jādū] sorcerer, magician; -īh sorcery') or historically yātūk (Nyberg: 'yātūk sorcerer, wizard ... Av. yātu-; Paz. jādu; NP jādū'). OIr. initial y- became the affricate ǰ- in SW Iranian, and intervocalic -t- was voiced to -d-. The book prints 'žâtŭk' with ž. That is not a known reading: no source has a fricative ž- here, and the form should be jâdûk/jādūg (or yātūk in Nyberg's notation). This is Nourai's misprint or idiosyncratic spelling, and the extraction is faithful. MP *yāsak 'wish' is only reconstructed: Hübschmann (no. 1123) writes 'Np. yāsa = phl. *yāsak setzt zd. ap. *yāsā- voraus' and doubts Horn's etymology. No Pahlavi text attestation was found in MacKenzie or Nyberg.\",\n   \"derivation_fa\": \"واژهٔ پهلوی برای «جادوگر» در خط کتابی y'twk نوشته و jādūg خوانده می‌شود (مکنزی؛ مانوی j'dwg). نیبرگ آن را به شیوهٔ تاریخی yātūk می‌نویسد. y- آغازی ایرانی باستان در فارسی میانهٔ جنوب غربی به ج بدل شده و t میان دو واکه به d نرم شده است. کتاب «žâtŭk» با ژ چاپ کرده که در هیچ منبعی نیامده است. این خطای چاپی یا شیوهٔ نگارش خودِ نورایی است و صورت درست jādūg است. خوانش اسکن با چاپ کتاب یکی است. صورت پهلوی yāsak «خواهش» را هوبشمان فقط بازسازی کرده (*yāsak) و در متون پهلوی یافته نشد.\",\n   \"error_in\": \"book\",\n   \"book_prints\": \"žâtŭk\",\n   \"correct_form\": \"jādūg (Book Pahl. y'twk; Nyberg yātūk)\",\n   \"sources\": [W[\"jadu\"]],\n   \"ref_check\": [\n    {\"ref\": \"BQT:553,2419\", \"status\": \"partial\", \"note\": \"Printed page 553 is not in the local scans (ref_page.py: 'No scan of BQT covers printed page 553'). The جادو entry is on BQT_v2_pages.txt leaf 11 (≈ p. 554). Mo'in's footnote there gives Av. yātu (ساحر), Old Indic yātu (جادوگری، سحر) and the Pahlavi form for جادویی, and notes 'فردوسی «جادو» را غالباً بجای «دروند» پهلوی ... آورد'. p. 2419 (vol. 4, pdf 502), footnote to یاسه: 'هوبشمان گوید: yāsa، پهلوی *yāsak از اوستا و پارسی باستان *yāsā ... هوبشمان وجه اشتقاق هرن (اسشق ۱۱۲۳) را قبول ندارد'. Mo'in has the Pahlavi forms, but yāsak is starred, and neither page has a ž- form.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 3049\", \"stance\": \"partial\", \"note\": \"'jādūg [y'twk | M j'dwg, N jādū] sorcerer, magician. -īh: sorcery.' Supports the word with ǰ-, not ž-. There is no entry for yāsag.\"},\n    {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 4430 (p. 226)\", \"stance\": \"partial\", \"note\": \"'yātūk [y'twk'] sorcerer, wizard ... Av. (1283 sq.) yātu-; Paz. jādu; NP jādū'. No yāsak.\"},\n    {\"src\": \"HUB\", \"where\": \"HUB.txt p. 107 no. 1123; §39\", \"stance\": \"partial\", \"note\": \"'Np. yāsa = ph. *yāsak setzt zd. ap. *yāsā- voraus. Ist āyāsa richtig und die ältere Form, so ist eben *āyāsa anzusetzen und eine andere Etymologie zu suchen.' §39: 'jatuk Zauberer (5. Jhd.) = np. jādu, zd. yātu-'.\"}\n   ]\n  },\n  {\n   \"id\": 3, \"lang\": \"Persian\", \"words\": \"jâdŭ; yâseh\", \"verdict\": \"plausible\",\n   \"derivation\": \"NP jādū 'magic, sorcerer' < MP jādūg (y'twk) < OIr. *yātu- (Av. yātu-, OP yātu), with the regular SW Iranian change of initial y- to ǰ- (cf. jām < yāma-, jāvīd < yāvaitāt-) and loss of final -g. This is confirmed by Horn no. 410, Hübschmann §39 and Wiktionary. NP yāse/āyāse 'wish, longing' (Borhan; attested in Rumi) is derived by Horn (no. 1123) from *ā-yāsa- 'Wunsch, Begehren' to Av. ā + yās- 'wünschen'. Hübschmann accepts a *yāsā- base but questions it if āyāsa is the older form, so yāse is plausible but less secure. The chart's NOTE about a 'Sanskrit jadoo' is mistaken: Hindi/Urdu jādū 'magic' is borrowed from Persian (a doublet of the learned Sanskritism yātu), and the inherited Sanskrit word is yātú-.\",\n   \"derivation_fa\": \"«جادو» از پهلوی jādūg و آن از ایرانی باستان *yātu- (اوستایی و پارسی باستان yātu) است. y- آغازی در فارسی میانهٔ جنوب غربی به ج بدل شده (مانند «جام» از yāma- و «جاوید» از yāvaitāt-) و g پایانی در فارسی نو افتاده است. هرن (ش ۴۱۰)، هوبشمان و ویکی‌واژه این را تأیید می‌کنند. «یاسه» (و «آیاسه») به معنای «خواهش، آرزو» را هرن (ش ۱۱۲۳) از ā + yās- «خواستن» اوستایی می‌داند. هوبشمان در این اشتقاق تردید دارد، پس این بخش با احتیاط پذیرفتنی است. یادداشت نمودار دربارهٔ «jadoo»ی سنسکریت نادرست است، چون «جادو»ی هندی و اردو وام‌واژه از فارسی است و واژهٔ بومی سنسکریت yātu- است.\",\n   \"sources\": [W[\"jadu\"], W[\"jadu_hi\"], W[\"yatu_skt\"]],\n   \"ref_check\": [\n    {\"ref\": \"HRN:92\", \"status\": \"supports\", \"note\": \"HRN.txt p. 92 (leaf 113), no. 410: 'jādū Zauberer, Jadū. aw. yātu- Zauberer; phlw. jātuk, jātūkīh, arm. LW. jatuk; ai. yātu- Spuk, Hexerei; Spukdämon'.\"},\n    {\"ref\": \"HUB:107\", \"status\": \"partial\", \"note\": \"HUB.txt p. 107 (leaf 118), no. 1123: 'Np. yāsa = ph. *yāsak setzt zd. ap. *yāsā- voraus. Ist āyāsa richtig und die ältere Form, so ist eben *āyāsa anzusetzen und eine andere Etymologie zu suchen.' This is a hedged reading of yāse.\"},\n    {\"ref\": \"BQT:553,2419\", \"status\": \"supports\", \"note\": \"p. 2419 (vol. 4 pdf 502): 'یاسه ... بمعنی خواهش و آرزو هم آمده است', with a quotation from Rumi's Masnavi and Hübschmann's etymology in the footnote. جادو (BQT_v2 leaf 11, ≈ p. 554; p. 553 itself not scanned): Av. yātu, OInd. yātu, 'امروز جادو بمعنی سحر و جادوگر بمعنی ساحر استعمال میشود'.\"},\n    {\"ref\": \"ARP:218\", \"status\": \"supports\", \"note\": \"ARP.txt §28 Yatu (index 'yatumant 218'): 'gemein eränisch ... zeigt das von yatu abgeleitete neup. jādū'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"no. 1123\", \"stance\": \"supports\", \"note\": \"'yāse (āyāse) Wunsch, Begierde. aw. *āyāsa- Wunsch, Begehren, vergl. ā + yās-, yāsanuha wünschen, verlangen'.\"},\n    {\"src\": \"HUB\", \"where\": \"§39 (HUB.txt line 5271)\", \"stance\": \"supports\", \"note\": \"'Ap. y im Anlaut = np. j in: jādu Zauberer = zd. yātu-, jām Glas, Becher = zd. yama-'.\"},\n    {\"src\": \"PHD\", \"where\": \"line 3049\", \"stance\": \"supports\", \"note\": \"'jādūg ... N jādū'.\"},\n    {\"src\": \"MON\", \"where\": \"MON_part1/2.txt grep جادو / یاسه\", \"stance\": \"silent\", \"note\": \"The abridged 2-vol OCR has no clean headword hit for either word.\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_pages.txt grep جادو\", \"stance\": \"silent\", \"note\": \"No headword entry for جادو. The only hit is under مغ (gloss 'جادوگر').\"}\n   ]\n  },\n  {\n   \"id\": 4, \"lang\": \"Greek\", \"words\": \"zělos\", \"verdict\": \"confirmed\",\n   \"derivation\": \"Gk. ζῆλος (Doric ζᾶλος) means 'eager rivalry, emulation, zeal, jealousy' (Homeric/classical). Initial ζ- < *y-, and Doric ᾱ shows original *ā (*yā-lo-). Pokorny (*i̯ā-), Watkins (*yā-lo-) and Wiktionary (*yéh₂-los from *yeh₂- 'to go, search', related to ζητέω 'seek') all reconstruct the same root shape and differ only in the gloss. Klein adds Doric ζατέω 'seek' and ζαμία 'penalty'.\",\n   \"derivation_fa\": \"یونانی ζῆλος (دوری ζᾶλος) به معنای «رقابت پرشور، شور و غیرت، رشک» است. ζ آغازی یونانی از *y هندواروپایی است و ā دوری نشان می‌دهد که واکهٔ اصلی *ā بوده است (*yā-lo-). پوکورنی، واتکینز و ویکی‌واژه همه آن را از همین ریشه (*i̯ā- / *yeh₂-) می‌گیرند. تنها معنای ریشه را «برانگیخته شدن» یا «جستن، کوشیدن» می‌دانند. ادعای نورایی درست است.\",\n   \"sources\": [W[\"zelos\"], W[\"zeal\"]],\n   \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1181: 'yā-. To be aroused. Suffixed form *yā-lo- in Greek zēlos, zeal: JEALOUS, ZEAL.'\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p. 501, lemma i̯ā-\", \"stance\": \"supports\", \"note\": \"'gr. ζῆλος, Doric ζᾶλος m. eagerness, jealousy, envy'.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1971.txt line 270330 s.v. zeal\", \"stance\": \"supports\", \"note\": \"'Gk. ζῆλος (Dor. ζᾶλος), jealousy, fervor, zeal, which is prob. rel. to Dor. ζατέω ... I seek for, inquire into'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 197\", \"stance\": \"supports\", \"note\": \"The iā- entry includes the Greek ζῆλος group, as Pokorny's revision of it does.\"}\n   ]\n  },\n  {\n   \"id\": 5, \"lang\": \"English\", \"words\": \"zeal, jealous\", \"verdict\": \"confirmed\",\n   \"derivation\": \"zeal: Gk. ζῆλος → Late Lat. zēlus (Christian Latin, Vulgate) → OFr. zel → ME zele (14th c.) → zeal. jealous: Late Lat. zēlōsus 'full of zeal' (Vulgar Lat. *zelosus) → OFr. gelos/jalous (Lat. z- > j-/g- [dʒ]) → ME jelous, gelus (first attested 1382) → jealous. It is a doublet of zealous, which was re-borrowed from Medieval Latin zēlōsus. The meaning shifted from 'ardent' to 'possessive, suspicious of rivals'.\",\n   \"derivation_fa\": \"انگلیسی zeal «شور، غیرت» از یونانی ζῆλος از راه لاتین متأخر zēlus و فرانسوی کهن zel و انگلیسی میانه zele آمده است. jealous «حسود، رشک‌ورز» از لاتین متأخر zēlōsus «پرشور» است که در فرانسوی کهن به gelos/jalous بدل شد (z لاتین به ج فرانسوی) و در انگلیسی میانه jelous شد. این واژه با zealous دوگانه است. ادعای نورایی درست است.\",\n   \"sources\": [W[\"zeal\"], W[\"jealous\"]],\n   \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is cited on this node. See consulted.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1971.txt lines 270330-270347\", \"stance\": \"supports\", \"note\": \"'zeal, n. — ME. zele, fr. Late L. zelus ... fr. Gk. ζῆλος'; 'zealous ... cp. jealous, which is a doublet'.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt line 21818\", \"stance\": \"supports\", \"note\": \"'Jealous. (F.-L.-Gk.) M.E. jalous, gelus. — O.F. jalous ... Low L. zelosus, full of zeal. — L. zelus'.\"},\n    {\"src\": \"AHD\", \"where\": \"line 1181\", \"stance\": \"supports\", \"note\": \"'JEALOUS, ZEAL' listed under yā-.\"}\n   ]\n  }\n ]\n}\n\ne2 = {\n \"entry\": 2,\n \"root\": \"Yag, Iag\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₁yaǵ- / *yeh₂ǵ- 'to worship, revere, sacrifice' (Pokorny 501 i̯ag-)\",\n \"note\": \"The root, label and gloss are correct and standard: Pokorny 501 'i̯ag- to worship', AHD 'yag-. To worship; reverence', Walde-Pokorny I 195, Wiktionary *h₁yaǵ-. The Indo-Iranian reflexes (Skt. yajati, Av. yazaite, yasna-, yazata-) and Gk. ἁγνός, ἅγιος, ἅζομαι are textbook cognates. The weak link is the final English box: 'Agnus' (Agnus Dei) is Latin agnus 'lamb' < *h₂egʷnós and has nothing to do with this root. The English derivatives of hagnos are the name Agnes (Gk. Hagnē) and, through ἅγιος, the prefix hagio-. The extraction matches the printed page ('Yag, Iag', with capital I for i̯).\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₁yaǵ- (پوکورنی ص ۵۰۱: i̯ag-) به معنای «پرستیدن، ستودن، قربانی کردن» در همهٔ منابع آمده است: پوکورنی، والده-پوکورنی، AHD و ویکی‌واژه. سنسکریت yajati، اوستایی yaz-، yasna- و yazata- و یونانی ἁγνός «پاک، مقدس» هم‌ریشه‌های شناخته‌شدهٔ آن‌اند. پس ادعای نورایی دربارهٔ ریشه درست است. تنها خانهٔ انگلیسی «Agnus» نادرست است، چون این واژه لاتین agnus «بره» است و به این ریشه ربطی ندارد. وام‌واژهٔ انگلیسی درست از ἁγνός نام «Agnes» است.\",\n \"sources\": [W[\"hagnos\"], W[\"yazata\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:501\", \"status\": \"supports\", \"note\": \"POK_full.txt, lemma 'i̯ag- : to worship', Page(s): 501-502: 'Old Indic yajati venerates with prayer and sacrifice = Avestan yazaiti'; 'Old Indic yajñá-, Avestan yasna- m. worship (of God), sacrifice (yajñiya-, Avestan yesnya- belonging to the sacrifice), gr. ἁγνός holy, pure'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1182\", \"stance\": \"supports\", \"note\": \"'yag-. To worship; reverence. Suffixed form *yag-yo- perhaps in Greek hagios, holy: HAGIO-. [Pok. jag- 501.]'\"},\n  {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt leaf 203 = Bd. I p. 195\", \"stance\": \"supports\", \"note\": \"'iag- religiös verehren. Ai. yajati verehrt mit Gebet und Opfer = av. yazaite ... av. yasna- m. Gottesverehrung, Opfer (av. yesnya- opferwürdig), gr. ἁγνός heilig, rein, lauter'.\"},\n  {\"src\": \"IEC\", \"where\": \"IEC.txt line 6319\", \"stance\": \"supports\", \"note\": \"'iag- revere, be awed at ... Sk. yájāmi worship; Av. yaze offer; praise; OPer. yadataiy worships; Gk. házomai be awed'.\"}\n ],\n \"nodes\": [\n  {\n   \"id\": 1, \"lang\": \"Avestan\", \"words\": \"yaz; yazatanam; yesnya; mazda-yasna; yazato-kerata\", \"verdict\": \"plausible\",\n   \"derivation\": \"Av. yaz- 'to worship, sacrifice to' (pres. yazaite) is the direct cognate of Skt. yaj- (PIE *h₁yaǵ-; Iranian z < *ǵ). The other words: (1) yazata- 'worthy of worship, a divine being' (= Skt. yajata-). The cited yazatanąm is its genitive plural 'of the yazatas', the form Horn quotes as the base of NP yazdān, so the gloss 'God' is loose. (2) yesnya- 'worthy of worship, belonging to the sacrifice' (Bartholomae), from yasna- 'worship'. (3) mazdayasna- 'Mazda-worshipper, Mazdayasnian', the Zoroastrians' self-designation, so 'God worshiper' is a free rendering. (4) 'yazato-kerata' is not an attested Avestan compound. It is a back-projection, *yazata-kṛta- 'made/created by the gods', of MP Yazdgird/Yazdēkirt, so it should be starred. The forms and meanings are otherwise correct.\",\n   \"derivation_fa\": \"ستاک اوستایی yaz- «پرستیدن، ستودن، قربانی کردن» هم‌ریشهٔ سنسکریت yaj- است (ز اوستایی از *ǵ هندواروپایی). yazata- یعنی «سزاوار پرستش، ایزد»، و yazatanąm حالت اضافی جمع آن «ایزدان» است. پس معنای «خدا» در نمودار آزاد است. yesnya- یعنی «سزاوار ستایش، وابسته به یسن»، و mazdayasna- یعنی «مزداپرست» که نام دینی زرتشتیان است. صورت «yazato-kerata» در اوستا گواهی نشده و تنها بازسازی پشتِ نام پهلوی «یزدگرد» است و باید ستاره‌دار باشد. بقیهٔ واژه‌ها درست‌اند، پس این خانه با احتیاط پذیرفتنی است.\",\n   \"sources\": [W[\"yazata\"], W[\"yasna\"]],\n   \"ref_check\": [\n    {\"ref\": \"POK:501\", \"status\": \"supports\", \"note\": \"lemma i̯ag-, p. 501: 'Avestan yazaiti ... Avestan yasna-m. worship ... Avestan yesnya- belonging to the sacrifice'.\"},\n    {\"ref\": \"HRN:95,252\", \"status\": \"supports\", \"note\": \"HRN p. 252 (leaf 274), no. 1127 yezdān 'Gott': 'aw. yazatanąm; phlv. yaztān, yazdān'. p. 95 (no. 422 ješn 'Fest, Gelage'): 'aw. yasna-; phlv. jašn bezw. yašn'.\"},\n    {\"ref\": \"KLN:1759\", \"status\": \"supports\", \"note\": \"KLN_1971.txt (1-vol. ed., Y section) s.v. Yajna / Yasna: 'yajati ... rel. to Avestic yazaite, of s.m., yasna-, sacrifice, worship, and prob. cogn. with Gk. ἅγιος holy, ἁγνός holy, chaste'. The page number was not mapped in the local OCR.\"},\n    {\"ref\": \"ZAW:38\", \"status\": \"partial\", \"note\": \"ZAW_pages.txt leaf 62 (= p. 38): 'yazdêgêrd Götterstadt 75, SM.; vgl. dazu von Stackelberg ... Bartholomae AirWb. 448'. Bartholomae discusses -gêrd forms there (one reading of a Pazand yazdêgêrd as 'city of the gods'). This is relevant to the -gird element but does not attest an Avestan *yazato-kərəta.\"},\n    {\"ref\": \"ETM:64\", \"status\": \"not_checked\", \"note\": \"ETM is not available (refs_online: 'Searched archive.org, ketabnak, noorlib, web: not found').\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"BRT.txt line 21411 (yaz-), 13176 (yesnya), 2563 (mazdayasna-)\", \"stance\": \"supports\", \"note\": \"The headwords yaz-, yesnya-, mazdayasna- are all present. There is no Avestan compound *yazata-kərəta-.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 195\", \"stance\": \"supports\", \"note\": \"'av. yazaite ds. (Ptc. yašta-) ... av. yasna- ... yesnya- opferwürdig'.\"},\n    {\"src\": \"AHD\", \"where\": \"line 1182\", \"stance\": \"silent\", \"note\": \"AHD lists only Greek/English derivatives under yag-.\"}\n   ]\n  },\n  {\n   \"id\": 2, \"lang\": \"Persian\", \"words\": \"Îzad; yasnâ; jašn; Yazdgerd\", \"verdict\": \"confirmed\",\n   \"derivation\": \"Each word goes back to Av./OIr. yaz- 'worship': (1) īzad/ēzad 'God, angel' < MP yazad/yazd (BP yzdt', Manichaean yzd) < Av. yazata-. Nyberg calls it a learned borrowing from Avestan and derives 'NP izad < yazad' (initial ya- > ē-/ī-, cf. izišn < yazišn). Its plural yazdān 'God' < MP yazdān < OIr. gen. pl. *yazatānām. Yazd the city is the same yazd. (2) yasnā/yasna 'worship ceremony' (in mazdayasnā) is a modern learned borrowing of Av. yasna-. (3) jašn 'feast, celebration' < MP jašn (yšn) < OIr. *yašna- 'worship, sacrifice' (= Av. yasna-), with the regular SW change of initial y- to ǰ-. Its meaning shifted from 'act of worship' to 'festival'. (4) Yazdgerd/Yazdegerd < MP Yazdgird/Yazdēkirt 'made (created) by God/the gods' (yazd + kird 'made', from kar- 'to make'). It was the name of three Sasanian kings and was arabicized as Yazdajird. Mo'in and Wiktionary give the same analysis.\",\n   \"derivation_fa\": \"«ایزد» از پهلوی yazad/yazd و آن از اوستایی yazata- «سزاوار پرستش» است. نیبرگ آن را وام‌واژه‌ای دینی از اوستا می‌داند و ya- آغازی در فارسی نو به ای بدل شده است (مانند «ایزش» از yazišn). «یزدان» جمع پهلوی yazdān از *yazatānām است و «یزد» نیز همین واژه است. «یسنا» وام‌گیری عالمانه و تازه از اوستایی yasna- است. «جشن» از پهلوی jašn و ایرانی باستان *yašna- «ستایش، قربانی» است. y- آغازی به ج بدل شده و معنا از «نیایش» به «جشن و سور» تحول یافته است. «یزدگرد» از پهلوی Yazdgird «ایزدآفریده، آفریدهٔ ایزد» (یزد + کرد «کرده») و نام سه پادشاه ساسانی است. معرّب آن «یزدجرد» است. ادعای نورایی درست است.\",\n   \"sources\": [W[\"izad\"], W[\"yazdan\"], W[\"jashn\"], W[\"yazdegerd\"], W[\"yasna\"]],\n   \"ref_check\": [\n    {\"ref\": \"BQT:752,2432\", \"status\": \"partial\", \"note\": \"p. 2432 (vol. 4 pdf 515, running head 'یزدان ۲۴۳۲') supports: یزدان footnote 'یزدان در اصل جمع «یزد» (← ایزد) ... از اوستایی yazatanam'; Yazdgerd footnote 'از: یزد (← ایزد) + کرد (کرده، آفریده)؛ در سلسلهٔ ساسانی سه پادشاه بدین نام خوانده شده‌اند: یزدگرد اول (۳۹۹-۴۲۰ م.)، یزدگرد دوم، یزدگرد سوم'. p. 752 was not identified. It falls in vol. 2 (ح/خ range), not in the entries for ایزد or جشن. The جشن footnote (BQT_v2 leaf 30, ≈ p. 574) reads 'اوستا yasna، پهلوی jašn/yašn (جشن)، هوبشمان ۱۲۴ ... کلمهٔ اوستایی yasna و سانسکریت yajna و پهلوی yasn بمعنی ستایش و پرستش است'.\"},\n    {\"ref\": \"ETM:64\", \"status\": \"not_checked\", \"note\": \"ETM is not available online or on disk.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"no. 141 (p. 33), no. 422 (p. 95), no. 1127 (p. 252)\", \"stance\": \"supports\", \"note\": \"'141. ized Gott, vergl. yezdān. aw. yazata-; phlv. yazd (Münzen)'; '422. ješn Fest, Gelage. aw. yasna-; phlv. jašn bezw. yašn'; '1127. yezdān Gott. aw. yazatanąm'.\"},\n    {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt lines 3068, 5702, 5704\", \"stance\": \"supports\", \"note\": \"'jašn [yšn] celebration, festival'; 'yazd [yzdt'; M yzd] god, divinity'; 'yazdān (pl.) gods, spirits'.\"},\n    {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt pp. 226-227\", \"stance\": \"supports\", \"note\": \"'Yazdēkirt, Yazdkirt Sassanid king ... MPrth yzdygyrd; Arab Yazdajird'; s.v. yazet: 'Borrowed from Av. yazata- ... NP izad < yazad, cf izišn < yazišn'.\"},\n    {\"src\": \"HUB\", \"where\": \"HUB.txt\", \"stance\": \"silent\", \"note\": \"Part I (keyed to Horn's numbers) has no separate remark on nos. 141/422/1127 found by grep.\"},\n    {\"src\": \"MON\", \"where\": \"MON_part2.txt grep جشن\", \"stance\": \"silent\", \"note\": \"The abridged OCR has only compound hits ('جشن (مانند نوروز)'), with no etymological tag.\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_pages.txt grep جشن/ایزد/یزدان\", \"stance\": \"silent\", \"note\": \"There are only prose hits, no headword entries.\"}\n   ]\n  },\n  {\n   \"id\": 3, \"lang\": \"Greek\", \"words\": \"hagnos\", \"verdict\": \"confirmed\",\n   \"derivation\": \"Gk. ἁγνός 'pure, chaste, holy' < Proto-Hellenic *hagnós < PIE *h₁yaǵ-nó-s (initial *y- > Greek h-). It is the exact formal match of Skt. yajñá- / Av. yasna- 'worship' (*yaǵ-no-). Related Greek words are ἅγιος 'holy', ἅζομαι 'stand in awe of' and ἅγος 'religious awe, expiation'.\",\n   \"derivation_fa\": \"یونانی ἁγνός «پاک، پارسا، مقدس» از یونانی آغازین *hagnós و هندواروپایی *h₁yaǵ-nó-s است (y آغازی در یونانی به h بدل شده). این واژه هم‌ساخت دقیق سنسکریت yajñá- و اوستایی yasna- «یسن، ستایش» است. ἅγιος «مقدس» و ἅζομαι «حرمت نهادن» نیز از همین ریشه‌اند. ادعای نورایی درست است.\",\n   \"sources\": [W[\"hagnos\"]],\n   \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 1182 names only 'Greek hagios, holy: HAGIO-' under yag-, not hagnos. Its root is the same.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p. 501\", \"stance\": \"supports\", \"note\": \"'gr. ἁγνός holy, pure, candid'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 195\", \"stance\": \"supports\", \"note\": \"'gr. ἁγνός heilig, rein, lauter'.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1971.txt line 108489 s.v. hagio-\", \"stance\": \"supports\", \"note\": \"'ἅγιος holy, sacred, which is rel. to ἅζεσθαι to stand in awe of, ἅγος sacrifice, ἁγνός holy, chaste, and prob. cogn. with OI. yajati'.\"}\n   ]\n  },\n  {\n   \"id\": 4, \"lang\": \"English\", \"words\": \"Agnus\", \"verdict\": \"disputed\",\n   \"derivation\": \"English 'Agnus' (as in Agnus Dei, 'Lamb of God') is Latin agnus 'lamb' < Proto-Italic *agʷnos < PIE *h₂egʷnós 'lamb', cognate with Gk. ἀμνός and English yean. It is unrelated to ἁγνός or the root *yag-. The only real English descendants of ἁγνός are the name Agnes (Lat. Agnes < Gk. Ἁγνή 'chaste') and, by folk association, agnus castus 'chaste tree'. In that plant name, agnus renders Gk. ἄγνος, a willow-like tree 'of unknown origin', which was confused with both Lat. agnus 'lamb' and Gk. ἁγνός 'chaste' (Klein). If Nourai meant Agnes, the arrow would be correct. As printed, 'Agnus' is wrong. The book prints 'Agnus' and the extraction is faithful.\",\n   \"derivation_fa\": \"انگلیسی «Agnus» (در Agnus Dei «برهٔ خدا») همان لاتین agnus «بره» است که از هندواروپایی *h₂egʷnós «بره» می‌آید و با یونانی ἀμνός هم‌ریشه است. پس با ἁγνός و ریشهٔ yag- پیوندی ندارد. وام‌واژهٔ درست انگلیسی از ἁγνός نام «Agnes» (از یونانی Ἁγνή «پاکدامن») است. در نام گیاه agnus castus نیز تنها ریشه‌شناسی عامیانه این دو واژه را به هم آمیخته است (کلاین). پژوهش امروزی این پیوند را رد می‌کند. شاید نورایی Agnes را در نظر داشته، اما آن‌چه چاپ شده نادرست است.\",\n   \"sources\": [W[\"agnus\"], W[\"agnes\"]],\n   \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is cited on this node. See consulted.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 32 s.v. Agnes, agnus castus\", \"stance\": \"contradicts\", \"note\": \"'Agnes, fem. PN. — L. Agnes, fr. Gk. Ἁγνή, lit. pure, chaste, fem. of ἁγνός'; 'agnus castus ... agnus derives fr. Gk. ἄγνος, a willowlike tree ... of unknown origin. This word was confused both with L. agnus, lamb, and Gk. ἁγνός, sacred, chaste'. So Agnes descends from ἁγνός, and Agnus does not.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt grep AGNUS/AGNES\", \"stance\": \"silent\", \"note\": \"No AGNUS under yag-. The only English derivative listed is HAGIO-.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt grep Agnus\", \"stance\": \"silent\", \"note\": \"no entry.\"}\n   ]\n  }\n ]\n}\n\ne3 = {\n \"entry\": 3,\n \"root\": \"Yah 5, Yâ 3\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE comparative suffix *-yos- / *-yes- (nom. *-yōs) > Av. -yah- (nom. -yå), Skt. -(ī)yas-, Lat. -ior, Gk. -ίων, Goth. -iza\",\n \"note\": \"The 'root' is the primary comparative suffix. It is correctly labelled Avestan (-yah-), and it is the inherited PIE *-yos-/*-yes- added directly to the root (Wiktionary *-yōs; Klein s.v. -ior: 'L. -ior, cogn. with OI. -īyas, Gk. -ίων, Goth. -iza'). Nourai's five Pokorny pages are the root entries of the five adjectives on the chart, and each lists the Avestan comparative: 521 k̂ak- (kasyah-), 618 k̂rei- (srayah-), 699 māk̂- (masyah-), 708 meĝh₂- (mazyah-), 800 pel- (frāyah-). The chart's right-hand box is empty in the book. It is a blank placeholder, not an extraction loss.\",\n \"note_fa\": \"این «ریشه» در واقع پسوند صفت تفضیلی است: اوستایی -yah- (فاعلی -yå)، از هندواروپایی آغازین *-yos-/*-yes-. این پسوند با سنسکریت -īyas-، لاتین -ior و یونانی -ίων هم‌ریشه است و مستقیم به ریشهٔ صفت افزوده می‌شد. پنج صفحه‌ای که نورایی از پوکورنی آورده، مدخل‌های ریشهٔ پنج صفت نمودارند و در هر یک صورت تفضیلی اوستایی آمده است. ادعای نورایی درست است.\",\n \"sources\": [W[\"yos\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:521,618,699,708,800\", \"status\": \"supports\", \"note\": \"POK_full.txt: lemma k̂ak- (pp. 521-522) 'Avestan kasu- small, little, compar. kasyah-'; lemma k̂rei- (p. 618) 'Kompar. Old Indic śreyas-, Avestan srayah-'; lemma māk̂- (p. 699) 'Avestan mas- long, compar. masyah-, Sup. masišta-'; lemma meĝh₂- (pp. 708-709) 'mazyah-, mazišta-'; pel- 'full' (pp. 798-801) 'frāyah-, Superl. fraēšta- the most'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"WLD_Bd1/Bd2 grep -yah-\", \"stance\": \"silent\", \"note\": \"The suffix has no separate entry. The comparatives appear under the individual roots, as in Pokorny.\"},\n  {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\", \"note\": \"No entry for the suffix *-yos- in the root list.\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 437 s.v. -ior\", \"stance\": \"supports\", \"note\": \"'-ior, suff. representing the Latin compar. ending -ior ... cogn. with OI. -īyas, Gk. -ίων, Goth. -iza, -ōza'.\"}\n ],\n \"nodes\": [\n  {\n   \"id\": 1, \"lang\": \"Avestan\", \"words\": \"maz-yah, mathi-yah; mas-yah, mas-yâ 2; frâ-yah; kas-yah; sra-yah\", \"verdict\": \"plausible\",\n   \"derivation\": \"These are all genuine Avestan primary comparatives in -yah- (nom. sg. -yå), formed on the root without the positive's suffix. mazyah- 'greater, mightier' is the comparative of mazant- (PIE *meǵh₂-; Skt. máhīyas-). masyah- 'greater (in size)' is the comparative of mas- 'long' (Bartholomae: 'der grössere'). frāyah- 'more, more plentiful' is from *prH-yos- (cf. Skt. prā́yas, Gk. πλείων; PIE *pelh₁- 'full'). kasyah- 'smaller' goes with kasu- 'small'. srayah- is 'more beautiful' (Bartholomae 'der schönere'), the cognate of Skt. śréyas- 'better', so the gloss 'better' follows Sanskrit. 'mathi-yah' is not attested in Avestan. OP has only the superlative maθišta- 'greatest', from which an OP comparative *maθiyah- can be reconstructed (OP θ = Av. s/z < *ǵ). It should be starred. 'mas-yâ 2' is a cross-reference to the chart's other root (Mâk) rather than a separate word.\",\n   \"derivation_fa\": \"همهٔ این صورت‌ها صفت تفضیلی اوستایی با پسوند -yah- (فاعلی -yå) هستند که مستقیم بر ریشه ساخته شده‌اند. mazyah- «بزرگ‌تر، تواناتر» از ریشهٔ maz- است (هم‌ریشه با سنسکریت máhīyas-). masyah- «بزرگ‌تر، درازتر» از mas- «دراز» است. frāyah- «بیشتر، فراوان‌تر» هم‌ریشه با سنسکریت prā́yas و یونانی πλείων است. kasyah- «کوچک‌تر» از kasu- «کوچک» است. srayah- به معنای «زیباتر» است (بارتولومه) و برابرِ سنسکریت śréyas- «بهتر». صورت «mathi-yah» در اوستا گواهی نشده و تنها از عالی‌ترین صفت پارسی باستان maθišta- «بزرگ‌ترین» بازسازی می‌شود، پس باید ستاره‌دار باشد. ازین رو این خانه با احتیاط پذیرفتنی است.\",\n   \"sources\": [W[\"yos\"]],\n   \"ref_check\": [\n    {\"ref\": \"POK:521,618,699,708,800\", \"status\": \"supports\", \"note\": \"Each cited page lists the Avestan comparative: kasyah- (521), srayah- (618), masyah- (699), mazyah- (708), frāyah- (800). See the root-level ref_check for quotations.\"},\n    {\"ref\": \"KLN:371,958\", \"status\": \"not_found\", \"note\": \"KLN_1966 leaves ≈197-201 and ≈488-492 (pp. 371, 958) were searched for 'compar', with no hit. The relevant Klein entry is s.v. '-ior' (leaf 437): 'cogn. with OI. -īyas, Gk. -ίων, Goth. -iza'.\"},\n    {\"ref\": \"SYN:880\", \"status\": \"partial\", \"note\": \"SYN §12.55-12.56 LARGE/SMALL (around printed p. 880) lists 'Av. kasu-' for SMALL. §13.16 MORE lists Av. frāyah- (OCR 'Srayah-'). Buck has the base adjectives, not the suffix itself.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"BRT.txt lines 20244, 20143, 18219, 9428, 27334\", \"stance\": \"supports\", \"note\": \"'mazyah- Adj. der grössere, gewaltigere'; 'masyah- Adj. der grössere'; 'fräyah- Adj. 1) der mehrere, plus'; 'kasyah- Adj. der kleinere'; 'srayah- Adj. der schönere'. There is no Avestan 'maθiyah-'.\"},\n    {\"src\": \"KNT\", \"where\": \"KNT_full.txt grep maθišta\", \"stance\": \"silent\", \"note\": \"The OCR does not render θ reliably, and no hit was found. OP maθišta- 'greatest' is standard (DB), but no comparative is attested.\"},\n    {\"src\": \"POK\", \"where\": \"pp. 521, 618, 699, 708, 800\", \"stance\": \"supports\", \"note\": \"See ref_check.\"}\n   ]\n  }\n ]\n}\n\nout = {\"pdf_page\": 561, \"book_page\": 531, \"verified_by\": \"claude-opus-5.5\", \"verified_on\": \"2026-10-16\", \"entries\": [e0, e2, e3]}\nwith open(\"/home/sfmqrb/git/rishe-private/data/verification/page-561.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"written\")\n"
}
```


### [2026-10-17T00:40:00.503Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-561.py (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:40:12.026Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'E'\np='build-561.py'; s=open(p).read()\ns=s.replace('\"root\": \"Yâ, Iâ 2\"','\"root\": \"Yâ, lâ 2\"').replace('\"root\": \"Yag, Iag\"','\"root\": \"Yag, lag\"')\ns=s.replace(\" Note that 'Iâ' is a capital I, Nourai's spelling of i̯ā-.\",\" The second spelling 'Iâ/lâ' (I and l look alike in the book's sans-serif) stands for Pokorny's i̯ā-.\")\ns=s.replace(\"The extraction matches the printed page ('Yag, Iag', with capital I for i̯).\",\"The extraction matches the printed page. In 'Yag, lag' the second spelling is Iag = Pokorny's i̯ag-, since I and l are indistinguishable in the book's font.\")\nopen(p,'w').write(s)\nE\npython3 build-561.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-561.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 561"
}
```


### [2026-10-17T00:40:12.584Z] TOOL RESULT

```
written
nodes verified: 10/10
node verdicts: {'plausible': 4, 'transcription_suspect': 1, 'confirmed': 4, 'disputed': 1}
root verdicts: {'plausible': 1, 'confirmed': 2}
ref checks: {'supports': 9, 'partial': 6, 'not_checked': 4, 'not_found': 1}
books consulted: {'supports': 21, 'partial': 4, 'contradicts': 2, 'silent': 9} | by book: {'WLD': 4, 'KLN': 4, 'BRT': 3, 'PHD': 3, 'HUB': 3, 'POK': 3, 'AHD': 3, 'NYB': 2, 'HRN': 2, 'MON': 2, 'ARY': 2, 'SKT': 2, 'ARP': 1, 'IEC': 1, 'KNT': 1}
```


## [2026-10-17T00:40:23.374Z] TOOL CALL #69: SubagentHandback

```json
{
 "message": "I wrote /home/sfmqrb/git/rishe-private/data/verification/page-561.json. `verify_check.py 561` shows 0 PROBLEM lines: 10 of 10 nodes are verified across 3 entries, and the redirect \"Yâ 3\" was skipped.\n\n**Verdicts:**\n- **Roots:** 2 confirmed (Yag/lag \"to worship\"; Yah 5 comparative suffix), 1 plausible (Yâ/lâ 2 \"to be aroused\").\n- **Nodes:** 4 confirmed, 4 plausible, 1 disputed, 1 transcription_suspect.\n\n**Flagged items:**\n- **Disputed – Yag, English \"Agnus\":** Agnus (as in Agnus Dei) is Latin agnus \"lamb\", from PIE *h₂egʷnós, and has nothing to do with hagnos or *yag-. The real English descendant of hagnos is the name Agnes. In the plant name agnus castus the link is only folk etymology (Klein).\n- **Transcription_suspect – Yâ 2, Pahlavi \"žâtŭk\":** the attested form is jādūg (MacKenzie; written y'twk, read yātūk by Nyberg). No source has a ž-. The error is in the book, not the extraction; the page image is saved at data/verification/sources/refs/ocr/BOOK/561.png.\n\n**Other notes:**\n- **Root Yâ 2 (plausible):** Pokorny p. 501 and the AHD both group Avestan yātu, yāsā and Greek zēlos under one root. Modern sources split them: Wiktionary takes zēlos from *yeh₂- \"seek\" and gives yātu a different origin, and Mann (IEC) gives yātu its own root *iāt-.\n- **The chart's note on a Sanskrit \"jadoo\" is wrong:** Hindi/Urdu jādū is borrowed from Persian, and the native Sanskrit word is yātú-.\n- **Unattested forms to star:** \"yazato-kerata\" (Avestan) is not attested; it is only reconstructed from Middle Persian Yazdgird. \"mathi-yah\" is not attested either; it is only inferred from the Old Persian superlative maθišta-. Pahlavi \"yâsak\" is starred in Hübschmann.\n- **Nourai's own references:** the five Pokorny pages for the comparative suffix (521, 618, 699, 708, 800) each list the matching Avestan comparative. BQT:752 could not be identified, KLN:371 and 958 were not found, and ETM is not available.\n\n**Extraction errors for the owner to fix:** none. The JSON matches the printed page; the empty right-hand box in the last chart is blank in the book."
}
```


### [2026-10-17T00:40:23.681Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
