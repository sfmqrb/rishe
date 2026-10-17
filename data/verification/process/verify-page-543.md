# Verification process log — verify-page-543


## [2026-10-17T00:00:15.310Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 543 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-543.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-543.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-543.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 543` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.364Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.410Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.506Z] TOOL RESULT

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


## [2026-10-17T00:00:18.927Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-543.txt"
}
```


### [2026-10-17T00:00:19.002Z] TOOL RESULT

```
1	=== PDF page 543 (book page 513) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wen : to wish, desire  (refs POK:1146; OEW:434)  PART 2
4	#1 (parent #0) [Latin] refs=AHD | vener : to love ; venus : love ; venĕnum : love potion ; venetî : beloved people (of Venice)
5	  #2 (parent #1) [French] refs=None | Venus ; Venezia : (through Italian) ; Vennezuela : little Venice (through Spanish)
6	    #3 (parent #2) [Persian] refs=MON6:2222,2223 | Venŭs «ونوس» : Venus ; Venîz «ونیز» : Venice ; Venezŭelâ «ونزوئلا» : Venezuela
7	  #4 (parent #1) [English] refs=None | venereal, Venus, venom, Venice
8	#5 (parent #0) [Germanic] refs=AHD | winnan : seek to gain, overpower, win ; wunsk : desire
9	  #6 (parent #5) [English] refs=None | win ; wish
10	#7 (parent #0) [Latin] refs=KLN:1697 | věnârî : to hunt
11	  #8 (parent #7) [English] refs=KLN:1697 | venery : hunting
12	#9 (parent #0) [Indo-European] refs=KLN:1697 | Wedh : to lead
13	  #10 (parent #9) [Avestan] refs=KLN:1687 | vadu 2 : to lead ; vâdayeiti : leads
14	--- entry 1 ---
15	ROOT [Indo-European] Wep : to throw, spray ?  (refs POK:1149)
16	#1 (parent #0) [Avestan] refs=POK:1149 | vafra : snow
17	  #2 (parent #1) [Pahlavi] refs=POK:1149 | vafr
18	    #3 (parent #2) [Persian] refs=POK:1149; AEF:258 | barf «برف» : snow
19	#4 (parent #0) [Sogdian] refs=SOD:401 | wfr : snow
20	#5 (parent #0) [Sanskrit] refs=POK:1149 | vapati : throws
21	#6 (parent #0) [Latin] refs=POK:1149 | veprĕs : a kind of bushy plant
22	--- entry 2 ---
23	ROOT Weqw -> redirect to Wekw
24	
```


## [2026-10-17T00:00:19.536Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-543.json"
}
```


### [2026-10-17T00:00:19.611Z] TOOL RESULT

```
1	{
2	  "pdf_page": 543,
3	  "book_page": 513,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wen",
8	        "lang": "Indo-European",
9	        "refs": "POK:1146; OEW:434",
10	        "gloss": "to wish, desire",
11	        "note": "This root has derivative related to sexual or hunting desires"
12	      },
13	      "part": 2,
14	      "nodes": [
15	        {
16	          "id": 1,
17	          "parent": 0,
18	          "lang": "Latin",
19	          "refs": "AHD",
20	          "words": [
21	            {"translit": "vener", "gloss": "to love", "script": null},
22	            {"translit": "venus", "gloss": "love", "script": null},
23	            {"translit": "venĕnum", "gloss": "love potion", "script": null},
24	            {"translit": "venetî", "gloss": "beloved people (of Venice)", "script": null}
25	          ],
26	          "note": null,
27	          "quote": null
28	        },
29	        {
30	          "id": 2,
31	          "parent": 1,
32	          "lang": "French",
33	          "refs": null,
34	          "words": [
35	            {"translit": "Venus", "gloss": null, "script": null},
36	            {"translit": "Venezia", "gloss": "(through Italian)", "script": null},
37	            {"translit": "Vennezuela", "gloss": "little Venice (through Spanish)", "script": null}
38	          ],
39	          "note": null,
40	          "quote": null
41	        },
42	        {
43	          "id": 3,
44	          "parent": 2,
45	          "lang": "Persian",
46	          "refs": "MON6:2222,2223",
47	          "words": [
48	            {"translit": "Venŭs", "gloss": "Venus", "script": "ونوس"},
49	            {"translit": "Venîz", "gloss": "Venice", "script": "ونیز"},
50	            {"translit": "Venezŭelâ", "gloss": "Venezuela", "script": "ونزوئلا"}
51	          ],
52	          "note": null,
53	          "quote": null
54	        },
55	        {
56	          "id": 4,
57	          "parent": 1,
58	          "lang": "English",
59	          "refs": null,
60	          "words": [
61	            {"translit": "venereal, Venus, venom, Venice", "gloss": null, "script": null}
62	          ],
63	          "note": null,
64	          "quote": null
65	        },
66	        {
67	          "id": 5,
68	          "parent": 0,
69	          "lang": "Germanic",
70	          "refs": "AHD",
71	          "words": [
72	            {"translit": "winnan", "gloss": "seek to gain, overpower, win", "script": null},
73	            {"translit": "wunsk", "gloss": "desire", "script": null}
74	          ],
75	          "note": null,
76	          "quote": null
77	        },
78	        {
79	          "id": 6,
80	          "parent": 5,
81	          "lang": "English",
82	          "refs": null,
83	          "words": [
84	            {"translit": "win", "gloss": null, "script": null},
85	            {"translit": "wish", "gloss": null, "script": null}
86	          ],
87	          "note": null,
88	          "quote": null
89	        },
90	        {
91	          "id": 7,
92	          "parent": 0,
93	          "lang": "Latin",
94	          "refs": "KLN:1697",
95	          "words": [
96	            {"translit": "věnârî", "gloss": "to hunt", "script": null}
97	          ],
98	          "note": null,
99	          "quote": null
100	        },
101	        {
102	          "id": 8,
103	          "parent": 7,
104	          "lang": "English",
105	          "refs": "KLN:1697",
106	          "words": [
107	            {"translit": "venery", "gloss": "hunting", "script": null}
108	          ],
109	          "note": null,
110	          "quote": null
111	        },
112	        {
113	          "id": 9,
114	          "parent": 0,
115	          "lang": "Indo-European",
116	          "refs": "KLN:1697",
117	          "words": [
118	            {"translit": "Wedh", "gloss": "to lead", "script": null}
119	          ],
120	          "note": null,
121	          "quote": null
122	        },
123	        {
124	          "id": 10,
125	          "parent": 9,
126	          "lang": "Avestan",
127	          "refs": "KLN:1687",
128	          "words": [
129	            {"translit": "vadu 2", "gloss": "to lead", "script": null},
130	            {"translit": "vâdayeiti", "gloss": "leads", "script": null}
131	          ],
132	          "note": null,
133	          "quote": null
134	        }
135	      ]
136	    },
137	    {
138	      "root": {
139	        "name": "Wep",
140	        "lang": "Indo-European",
141	        "refs": "POK:1149",
142	        "gloss": "to throw, spray ?"
143	      },
144	      "nodes": [
145	        {
146	          "id": 1,
147	          "parent": 0,
148	          "lang": "Avestan",
149	          "refs": "POK:1149",
150	          "words": [
151	            {"translit": "vafra", "gloss": "snow", "script": null}
152	          ],
153	          "note": null,
154	          "quote": null
155	        },
156	        {
157	          "id": 2,
158	          "parent": 1,
159	          "lang": "Pahlavi",
160	          "refs": "POK:1149",
161	          "words": [
162	            {"translit": "vafr", "gloss": null, "script": null}
163	          ],
164	          "note": null,
165	          "quote": null
166	        },
167	        {
168	          "id": 3,
169	          "parent": 2,
170	          "lang": "Persian",
171	          "refs": "POK:1149; AEF:258",
172	          "words": [
173	            {"translit": "barf", "gloss": "snow", "script": "برف"}
174	          ],
175	          "note": null,
176	          "quote": {"text": "به برفاب رحمت مکن بر خسیس - چو کردی مکافات بر یخ نویس", "poet": "Sa`dî"}
177	        },
178	        {
179	          "id": 4,
180	          "parent": 0,
181	          "lang": "Sogdian",
182	          "refs": "SOD:401",
183	          "words": [
184	            {"translit": "wfr", "gloss": "snow", "script": null}
185	          ],
186	          "note": null,
187	          "quote": null
188	        },
189	        {
190	          "id": 5,
191	          "parent": 0,
192	          "lang": "Sanskrit",
193	          "refs": "POK:1149",
194	          "words": [
195	            {"translit": "vapati", "gloss": "throws", "script": null}
196	          ],
197	          "note": null,
198	          "quote": null
199	        },
200	        {
201	          "id": 6,
202	          "parent": 0,
203	          "lang": "Latin",
204	          "refs": "POK:1149",
205	          "words": [
206	            {"translit": "veprĕs", "gloss": "a kind of bushy plant", "script": null}
207	          ],
208	          "note": null,
209	          "quote": null
210	        }
211	      ]
212	    },
213	    {
214	      "root": {
215	        "name": "Weqw",
216	        "redirect": "Wekw"
217	      },
218	      "nodes": []
219	    }
220	  ]
221	}
222	
```


## [2026-10-17T00:00:27.652Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','OEW','AHD','MON6','MON','KLN','AEF','SOD','WLD','IEC','SYN','BRT','KNT','PHD','NYB','HRN','HUB','BQT','SKT','WEB','FSD','CHEUNG','ARY']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"; command ls data/verification/sources/refs/ | head -100"
}
```


### [2026-10-17T00:00:28.473Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC n
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON6 null
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
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
```


## [2026-10-17T00:00:41.486Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','MON','AHD','SOD','AEF','OEW','WLD']:\n  v=d[k]; print(k, {x:v.get(x) for x in ['local_file','page_offset','lookup_hint','scans']}); print()\n\"; python3 -c \"\nimport json;d=json.load(open('data/verification/page-538.json'));e=d['entries'][0];print(json.dumps({k:e[k] for k in e if k!='nodes'},ensure_ascii=False,indent=1)[:3000]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-10-17T00:00:41.936Z] TOOL RESULT

```
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", 'scans': None}

KLN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", 'scans': None}

MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", 'scans': None}

AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).", 'scans': None}

SOD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'], 'page_offset': 'printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)', 'lookup_hint': "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", 'scans': None}

AEF {'local_file': None, 'page_offset': None, 'lookup_hint': "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه\u200cشناختی فارسی' (Mehrafarin), also not online.", 'scans': None}

OEW {'local_file': None, 'page_offset': None, 'lookup_hint': "Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglish00jose?q=<root>", 'scans': None}

WLD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.", 'scans': None}

{
 "entry": 0,
 "root": "Wekw, Weqw",
 "verdict": "confirmed",
 "modern_form": "PIE *wekʷ- 'to speak' (Pokorny 1135-1136 u̯ekᵘ-; LIV² 673f.; Watkins wekw-; o-grade root noun *wṓkʷs 'voice')",
 "note": "Root, label and gloss are correct: Pokorny 1135 u̯ekᵘ- 'sprechen' with Skt. vakti, vāc-, vacas-, Av. vac-, vacah-, vāxš, Gk. épos, ops, Lat. vōx, vocāre (WP I 245f.). Cheung 2007 (*u̯ač) and Wiktionary agree. The Latin/English branch and the Avestan vāč-/vacah-/uxδa- branches are textbook. The weaker parts of the chart are the Iranian compounds Nourai reconstructs or invents to reach particular New Persian words: 'paurvatâ-vac' (for pažvāk), 'hu-ni-vak' (for xonyā), Avestan 'vaxš-ô-bara' (only a reconstruction *vaxša-bara- behind MP waxšwar) and 'Old Persian wâk/wânk' (not attested). The derivation of xonyā (MP huniyāg) from *hu-ni-vāka- is opposed by the Middle Persian form, which has no -w- (see node 9). forūxtan 'sell' is linked to vac- by Justi/Horn/Mo'in, but Cheung puts it under *waxš- 'grow' (see node 4). The extraction matches the printed page (checked against site/pages/538.jpg).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *wekʷ- «سخن گفتن» با بالاگونهٔ o در نام‌واژهٔ *wṓkʷs «آواز، صدا» در پوکورنی (ص ۱۱۳۵-۱۱۳۶)، والده-پوکورنی (ج ۱، ص ۲۴۵)، واتکینز و چونگ آمده است. بازمانده‌های آن سنسکریت vāc- و vacas-، اوستایی vāč- (حالت فاعلی vāxš) و vacah- «سخن»، یونانی épos و لاتینی vōx و vocāre است. ریشه و زبان و معنایی که نورایی داده درست است. ولی چند ترکیب ایرانی در این نمودار ساختهٔ خود اوست و در متن‌ها نیامده، مانند paurvatâ-vac و hu-ni-vak و vaxš-ô-bara. پیوند «خنیا» با این ریشه هم با پژوهش امروزی سازگار نیست.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-"
 ],
 "ref_check": [
  {
   "ref": "POK:1135",
   "status": "supports",
   "note": "POK_full.txt l.90116ff. 'Root / lemma: ueḱ- (*hueḱᵘ-) / Meaning: to speak / Material: Old Indic vakti, vivakti says, talks, speaks ... Avestan vac- speak, uxta-. Old Indic vacas- = Avestan vacah (= gr. épos) discourse, word ... vāk = Avestan vāxš (= Latin vox) voice, discourse, word ... Latin vox, vocis voice, voco, -are call ... References: WP. I 245 f.' Page(s) 1135-1136."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 245-246 (WLD_Bd1_pages.txt l.22850ff., leaf 253)",
   "stance": "supports",
   "note": "'uekᵘ- „sprechen“. Ai. vákti, vivakti „sagt, redet, spricht“ ... av. vac- „sprechen“, uxta- ... ai. vacas- n. = av. vacah- (= gr. épos) „Rede, Wort“ ... ai. vāc-, n. sg. vāk = av. vāxš (= lat. vox) „Stimme, Rede, Wort“ ... lat. vox vocis „Stimme“, voco, -āre „rufen“'."
  },
  {
   "src": "AHD",
   "where": "Watkins 1985 s.v. wekw-",
   "stance": "supports",
   "note": "AHD_watkins1985.txt: 'wekw-. To speak. 1. O-grade form *wokw- in: a. Latin vox (stem voc-), voice: VOCAL, VOICE, VOWEL ... 2. Suffixed o-grade form *wokw-a- in Latin vocare, to call: VOCABLE, VOCATION ... 3. Suffixed form *wekw-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekw- 1135.]'
{
 "id": 1,
 "lang": "Avestan / Old Persian",
 "words": "vak, vačah, vaxš 1",
 "verdict": "confirmed",
 "derivation": "Avestan has the verb vac- / vaoc- 'to speak' (Indo-Iranian *wak-, *wač- < PIE *wekʷ-, with the labiovelar becoming k and then č before a front vowel), the neuter s-stem vacah- 'speech, word' (= Skt. vacas-, Gk. épos < *wekʷ-os) and the root noun vāč- 'voice, word', nominative vāxš (= Skt. vāk, Lat. vōx < *wōkʷs). Nourai's 'vak' is the root and 'vaxš' is that nominative (Bartholomae writes it vāxš with a long vowel). All three forms and the glosses are correct. The words are Avestan; Old Persian has no attested form of this root.",
 "derivation_fa": "در اوستایی فعل vac- / vaoc- «گفتن»، نام‌واژهٔ vacah- «سخن، گفتار» (برابر سنسکریت vacas- و یونانی épos) و نام‌واژهٔ vāč- «آواز، سخن» با حالت فاعلی vāxš (برابر سنسکریت vāk و لاتینی vōx) آمده است. kʷ هندواروپایی در هندوایرانی به k و پیش از واکهٔ پیشین به č بدل شده است. بارتولومه و پوکورنی و چونگ همین را می‌گویند و ادعای نورایی درست است. تنها این صورت‌ها اوستایی‌اند و در پارسی باستان گواهی ندارند.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-",
  "https://en.wiktionary.org/wiki/آواز"
 ],
 "ref_check": [
  {
   "ref": "POK:1135",
   "status": "supports",
   "note": "POK_full.txt l.90122 'Avestan vac- speak ... Old Indic vacas- n. = Avestan vacah (= gr. épos) discourse, word ... vāk = Avestan vāxš (= Latin vox) voice, discourse, word'."
  }
 ],
 "consulted": [
  {
   "src": "BRT",
   "where": "col. 1333-1336 s.v. vāk-; col. 1340-1341 s.v. vacah-",
   "stance": "supports",
   "note": "BRT.txt l.22236 'vāk- (vāxš) m., f. 1) Stimme; 1) der Menschen (und Götter) Stimme ... 2) Rede, Wort ... Zum V. vak-'; l.22355 'vacah- n. 1) Sprechen, Rede, Wort ... im Gegensatz zu Denken und Handeln'."
  },
  {
   "src": "WLD",
   "where": "Bd. I 245",
   "stance": "supports",
   "note": "'ai. vacas- n. = av. vacah- „Rede, Wort“ ... ai. vāc-, n. sg. vāk = av. vāxš (= lat. vox) „Stimme, Rede, Wort“'."
  },
  {
   "src": "SYN",
   "where": "18.11 VOICE",
   "stance": "supports",
   "note": "'Skt. vāc-, Av. vāč- (nom. sg. Skt. vāk, Av. vāxš)'."
  },
  {
   "src": "CHEUNG",
   "where": "p. 402 s.v. *u̯ač",
   "stance": "supports",
   "note": "'AVESTAN: vaoc- (vāč-) to say' with forms vaocat, uxδa- etc."
  }
 ]
}
```


## [2026-10-17T00:00:46.862Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"lemma: u̯en-\\|lemma: uen-\\|lemma: u̯ep-\\|lemma: uep-\\|lemma: u̯edh-\\|lemma: uedh-\" POK_full.txt; sed -n 1,60p /home/sfmqrb/git/rishe-private/tools/verify_check.py | head -80"
}
```


### [2026-10-17T00:00:47.184Z] TOOL RESULT

```
90924:Root/ lemma: uen-1, uena- 
91008:Root / lemma: uen-2 
91015:Root / lemma: uen- 
91039:Root / lemma: uep-2 
91045:Root/ lemma: uep-2\ "to throw, throw out' derived from an extended Root/ lemma: uer-3. 
92770:Root / lemma: uep- : yap- {*hyek'^-) 
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


## [2026-10-17T00:00:51.895Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90924,91060p POK_full.txt"
}
```


### [2026-10-17T00:00:52.373Z] TOOL RESULT

```
Root/ lemma: uen-1, uena- 
Meaning: to strive; to wish for, to love 



Material: Old Indie vanati, Ka/7o7/"wunscht, loves, gewinnt, siegt', participle vanita-, -vata-, 
vani-tr-, vantr-^ gainer', Avestan vanaiti, vanao/t/ ^s\egt', Middle Persian i/a/7/?a/7 "defeat, 
conquer, hit'; Old Indie Aor.-present vanat/"\n same meaning; Kaus. vanayat/and vanayati 
(previously not covered); as -5^-present Old Indie i/a/7c/75//"wunscht', compare vanchat 
"wish'; vanas-n. "lust' (compare Latin Venus), vani-i. "desire, wish', wherefore vanTyati 
"bettelf, vanTyaka-^ beggar', vanu-as noun agentis m. (compare Avestan -vanus\n Nom. 
Prussian); in compositions erscheirit vanya-, s. further vanta- as Nom. Sg. m. (Avestan 
vanfar' victor'), vant/'-Hom. Act. (uncovered, yet compare Avestan -vantay-); Old Indie 
vama-' left ' and i/a/77a-"lieb(lich), lascivious'; 

venet. VN VenefHrom *uenefos 'geWebt'; compare die \/enostes'\n den Alpen, die 
Venetulani\v\ Latium (Krahe IF. 58, 137); Latin-Germanic Venethi{P\\v\.)\ Old High German 
Winida "Wende' point at auf proto Germanic *Veneto-, against it Latin-Germanic Venedi 
(Tacitus), Old English Winedas^y^eudeVi auf *Venet6-\ 

Maybe alb. {* venedi) i/e/7o'/ 'country, homeland', i/e/70'05 'place, put, settle, judge, decide' 

Latin venus, -erist "love, Liebesgenuft, Liebreiz', Venus name the Liebesgottin, 
Ke/7^5/^s "graceful, charming, mellifluous', veneror, -a/'/"with religious fear, shyness 
worship, huldigen, humbly bid, beg, ask', originally "die love bezeugen'; here also venor, - 
^/"/"pursue ein Wild, hunt, chase'; 



Old Irish fine {*venja) " kinship, stem, family ', Middle Irish fin-gaiacfi^ parricidalis ', 
coibnius^ kinship' {*con-venestu-), abret. coguenou^ indigena ', Middle Breton gouen 
"Rasse', cymr. gwen^ smile ' (out of it Middle Irish gends.l); 

extraordinary reich vertreten is die root uen- in den Germanic Sprachen: 

auf Indo Germanic * ueni-s goes back gall. Veni- in PN Ven/-carus etc., Old Icelandic 
1///7/' "friend'. Old Saxon Old High German m'ni. Old Frisian Old English wine; e\neja- 
derivative is Gothic w/nja' willow, food'. Middle Low German Old High German winne. Old 
Icelandic vini. " meadowland ' (compare Old Irish fine^ kinship'); zero grade Old High 
German wunnia, wunna, wunnr\us\., Wonne', Old Saxon wunnia. Old English wynnds. 
(Middle High German wunne^ meadowland ', only in the Formel wunne and weide^ graze' 
replacement for the old winne); 

Indo Germanic *uenlstro-mr6 through Old Icelandic vinstri^ left ', Old Saxon winistar. 
Old Frisian winisteretc. assumed, eine Komparativbildg. as Latin sinister e\.c. (compare 
moreover Old Indie vama- " left '); 



frequent, often is the junction to "befriedigt sein, sicli accustom ' in Germanic; compare 
zero grades Gothic unwunands's\c\r\ nicht freuend', Old Icelandic una {* wunen) "zufrieden 
sein with', Old Frisian wonia. Old Saxon wonon, wunon'stay, dwell'. Old High German 
wonen^ habitual, customary sein, sich accustom, abide, remain, wohnen\ Old Saxon 
giwono, giwuno. Old English gewun. Old High German giwon " habitual, customary '; Old 
Icelandic ograde vanrdiS.; derived Old Saxon giwono {*-wunan-) " consuetude ' etc.. Old 
Icelandic vanixr\. ds.; Old Icelandic venja{*wanjan). Old Saxon gi-wennian. Old English 
wennan etc. " accustom '; (under the influence of common Celtic -ns-, -nt- > -nn-). 

maybe alb. vonelate', vonoj"de\aY, stay late' 

die lengthened grade has Germanic meaning "hoffen, expect ' angenommen; Gothic 
M/e/75 (/-stem) " expectation, hope'. Old Icelandic van, Old Saxon wands., Old Frisian wen 
"opinion'. Old High German wan a\so 'Vermutung, Wahn, intention' etc.; Adj. necess. Old 
Icelandic vaenn {*venja-) 'to hoffen, pretty, pleasant', wherefore Old Icelandic vaend 
{*veniPd) 'hope, expectation ', Gothic wenjan^ expect, hoffen'. Old Icelandic v^nads., 
vaenask^ boast ', Old Saxon wanian e\.c.; zero grade Old Icelandic osk {* wunsko) 'wish'. 
Old English wOsc-, Old High German m/^/7sc 'wish' etc.. Old Icelandic 0sk/a'\N\s\r\', Old 
English wyscan ds. (compare ^etyj/sca/7'adoptieren'). Old High German wunscen ds. etc. 
(compare above Old Indie vanchati); 

the meaning 'work, suffer, bear, endure, quarrel, gain ' shows sich Germanic in the 
family Gothic i4///7/7a/7 'suffer, bear, endure'. Old Icelandic v/nna ^\Nork, align, iJberwinden', 
Old Saxon w/nnan 'quarre\, fight' etc.. Old English w/den/y/nnam. ' adversary ', Old High 
German widanA/inno ds.; Gothic winno, w/nna' affliction, -schaft'. Old Icelandic 1///7/75 
'work'. Old High German nv/7/7a 'fight'. Middle High German w/nne^pa\n'; schlieftlich 
Gothic wunns ' affliction '; (under the influence of common Celtic -ns-, -nt- > -nn-). 

Church Slavic un/'t/" veTle ', unj//, unej/" beiier'; 

Hittite uen-, uent- ' futuere '; Tocharian A wan/, B win- 'pleasure'. 

References: WP. I 258 f., WH. II 752 f., Vasmer 3, 184. 
Page(s): 1146-1147 

Root / lemma: uen-2 
Meaning: ' punch, hit, strike ' 
See also: see above under ua-l. 
Page(s):1147 



Root / lemma: uen- 

Meaning: to hit, wound 

Note: (: ua-, similarly as g^em- : g^a-qo, come') 

Material: Armenian vandem^ 6es\xoy, smash'; Gothic M/i//7o(s 'verwundet', Old High 

German Modern High German Old Saxon Old English wund, Subst. Old High German 

wunta. Old English wund. Old Icelandic 5/7o'"wound' {*un-t6s, -ta). Old English //"swelling, 

lump, growth' (originally probably "swelling, blister infolge eines Schlages'), engl. wen. 

Middle Low German wene, Danish dial, vann, vsene {\iro\o Germanic *wanja); cymr. ym- 

M/a/7 "fight', mcymr. gwe/nfl durchbohrte', 3. Sg. gwant, gwan^ punctio ', corn, yth ym- 

wanas^ percussit ', gwane^ perforare '. 

References: WP. I 212. 

Page(s):1108 

Root / lemma: uep-2 

Meaning: to throw, throw out 

Note: 

Root/ lemma: uep-2\ "to throw, throw out' derived from an extended Root/ lemma: uer-3. 

G. uer-p-, ur-ep- {* suerich^: "to turn, wind'. 

Material: Old Indie 1/405// "wirft, streut (den Samen)', vapra-xw. n. "Aufwurf (from earth), 

earthwair, i/a/0/'5"Feuerstatte', Avestan vafra-. Middle Persian vafr, npers. barf'snow' 

(actually [*Schnee]wehe?); 

Maybe alb. bore' snow ' < npers. barf " snow '. 

Old Church Slavic veprt, Latvian vepr/s'boar' (as "the Befruchter'); different about Balto 

Slavic *ueprja- "boar' above S. 323; remains far off Latin vepres "briar' (see 11 56).
```


## [2026-10-17T00:01:05.607Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^venery\\|^venereal\\|^Venus,\\|^venom,\\|^wed,\\|^win,\\|^wish,\\|^venison\\|^Venice\\|^Venezuela\\|^venerate\" KLN_1966.txt"
}
```


### [2026-10-17T00:01:05.975Z] TOOL RESULT

```
41210:venery,  n.,  sexual  love,  (archaic).  —  From  the stem  of  L.  venus,  gen.  veneris,  ‘love,  sexual desire’.  See  venerate  and  cp.  Venus.  Cp.  also prec.  word.
41216:venison,  n.,  the  flesh  of  a  deer.  —  ME.  veneson, veneison,  venison,  fr.  OF.  veneson,  veneison  (F. venaison),  fr.  L.  venatidnem,  acc.  of  venatio, ‘hunting,  chase',  fr.  venatus,  pp.  of  venari,  ‘to hunt’.  See  venery,  ‘hunting’.
41220:venom,  n.,  1)  poisonous  matter  secreted  by  some animals  (as  snakes,  spiders,  etc.);  2)  spite,  mal¬ ice-  —  ME.  venym,  venim,  venon,  fr.  OF.  venim (F.  venin),  fr.  VL.  *venimen,  which  was  formed fr.  L.  venenum,  ‘a  drug,  potion’,  through  the substitution  of  suff.  -imen  for  -enum.  L.  venenum
```


## [2026-10-17T00:01:15.174Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 41190,41240p KLN_1966.txt; grep -n \"^wed\\b\\|^wed,\\|^Venus\\|^win\\b\\|^win,\\|^wish\\b\" KLN_1966.txt"
}
```


### [2026-10-17T00:01:15.568Z] TOOL RESULT

```
Derivatives:  vend,  n.,  vendee  (q.v.),  vend-er,  n., vend-ing,  n.  and  adj.,  vendor  (q.v.) vendace,  n.,  a  whitefish  ( Coregonus  vandesius).  — ModL.  vandesius,  fr.  MF.  (=  F.)  vandoise, ‘dace’,  fr.  Gaulish  *vindesia,  ‘whitefish’,  fr.  Cel¬ tic  vindo-,  ‘white’ ;  see  winter  and  cp.  Wend.  For sense  development  cp.  F.  able,  ablette,  ‘the bleak’,  fr.  L.  albus,  ‘white’,  and  E.  whitefish. vendaval,  n.,  a  strong  wind  blowing  from  the  sea in  Mexico.  —  Sp.,  fr.  F.  ventd'aval,  ‘westerly wind’,  fr.  vent,  ‘wind’  and  aval,  ‘downward  part, downward  direction'.  The  first  element  derives fr.  L.  ventus,  ‘wind’.  F.  aval  stands  for  d  val,  ‘to the  valley’.  See  wind,  n.,  and  avale.
Vendean,  adj.,  of  Vendee.  —  F.  Vendeen,  fr.  La Vendie,  name  of  a  department  in  Western France.  For  the  ending  see  suff.  -an.
Derivative:  Vendean,  n.
vendee,  n.,  the  purchaser  (law).  —  Lit.  ‘a  person to  whom  anything  is  sold’;  formed  from  the verb  vend  with  suff.  -ee.
Vendemiaire,  n„  the  first  month  (lasting  fr.  Sept. 2nd  to  Oct.  1st)  of  the  French  revolutionary calendar.  —  F.,  lit.  ‘(month)  of  vintage’,  coined by  Fabre  d’Lglantine  in  1793  fr.  L.  vindemia, ‘vintage’.  See  vintage.
vendetta,  n.,  a  blood  feud  in  the  pursuit  of  aveng¬ ing  the  slaying  of  a  near  relative.  —  It.,  re¬ venge’,  fr.  L.  vindicta,  ‘vengeance,  revenge’,  fr. vindex,  gen.  vindicis,  ‘vindicator  .  See  vindictive, vendible,  adj.,  that  which  can  be  sold,  salable.  — ME.,  fr.  L.  vendibilis,  fr.  vendere,  ‘to  sell’.  See vend  and  -ible.
Derivatives:  vendibil-ity,  n.,  vendible-ness,  n., vendibl-y,  adv.
vendition,  n.,  the  act  of  selling.  —  L.  venditid, gen.  -onis,  ‘a  selling,  sale’,  fr.  venditus,  pp.  of vendere.  See  vend  and  -ition.
t
i
i
vendor,  n.  —  AF.  vendour,  vendor,  fr.  OF.  (=  F.) vendeur,  fr.  L.  venditdrem,  acc.  of  venditor, ‘seller’,  fr.  venditus,  pp.  of  vendere.  Cp.  the  noun vender  and  see  vend  and  agential  suff.  -or. veneer,  tr.  v.,  to  overlay  (wood)  with  a  thin  sheet of  fine  wood.  —  Fr.  earlier  fineer,  fr.  G.  fur- nieren,  fr.  F.  fournir,  ‘to  furnish’,  fr.  OHG. frumjan,  ‘to  provide’.  The  word  was  borrowed from  and  re-borrowed  by  one  and  the  same language  at  two  different  periods.  See  furnish. Derivatives:  veneer,  n.,  veneer-er,  n.,  veneer-ing, n.
venenate,  tr.  v.,  to  poison  (rare).  —  L.  venenatus , pp.  of  venendre,  ‘to  poison’,  fr.  venenum,  ‘poi¬ son’.  See  venom  and  verbal  suff.  -ate. Derivative:  venenat-ion,  n. venerability,  n.  —  ML.  venerabilitds,  fr.  L.  vene- rabilis.  See  next  word  and  -ity. venerable,  adj.  —  ME.,  fr.  L.  venerdbilis,  fr.  vene- rari,  ‘to  venerate’.  See  next  word  and  -able. Derivatives:  venerable-ness,  n.,  venerabl-y,  adv. venerate,  tr.  v.,  to  revere.  —  L.  veneratus,  pp.  of venerari,  ‘to  reverence,  worship,  venerate’,  fr. venus,  gen.  veneris,  ‘love,  sexual  desire,  loveli¬ ness,  attractiveness,  beauty,  charm',  whence Venus,  gen.  Veneris,  ‘the  goddess  of  love’ ;  cogn. with  OI.  vanas-,  ‘desire’,  vanati,  vandti,  vanchati, ‘desires,  loves;  wins,  is  victorious’,  Avestic  va- naiti,  ‘he  wishes;  is  victorious’,  OE.  wynn,  ‘joy’, wunian,  ‘to  dwell’,  wenian,  ‘to  accustom,  train; to  wean’,  wyscan,  ‘to  wish’.  All  these  words  de¬ rive  fr.  I.-E.  base  *wen-,  ‘to  strive  after,  wish, desire;  to  be  satisfied;  to  be  wont’.  See  wish  and verbal  suff.  -ate  and  cp.  venery  (in  both  senses), venial,  venom,  Venus.
Derivatives:  veneration-al,  adj.,  venerat-ive,  adj., venerat-ive-ly,  adv.,  venerat-ive-ness,  n.,  vener¬ ator  (q.v.)
veneration,  n.  —  ME.  veneracion,  fr.  veneratio, gen.  -onis,  fr.  veneratus,  pp.  of  venerari.  See prec.  word  and  -ion.
Derivative:  veneration-al,  adj. venerator,  n.  —  L.  venerator,  fr.  veneratus,  pp.  of venerari.  See  venerate  and  agential  suff.  -or. venereal,  adj.,  1)  pertaining  to  sexual  love  or  in¬ tercourse;  2)  infected  with  a  venereal  disease; 3)  curing  venereal  diseases.  —  Formed  with  adj. suff.  -al  fr.  L.  venereus,  ‘pertaining  to  love  or sexual  desire’,  fr.  venus,  gen.  veneris.  See  vener¬ ate.
venereology,  n.,  the  study  of  venereal  diseases.  — A  hybrid  coined  fr.  L.  venus,  gen.  veneris,  ‘love, sexual  desire',  and  Gk.  -Xoyia,  fr.-  X6yop,  ‘one who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  venerate  and -logy.
Derivative:  venereolog-ist,  n. venery,  n.,  hunting  (archaic).  —  ME.  venerie,  fr. OF.  venerie  (F.  venerie),  ‘to  hunt’,  fr.  L.  venari, ‘to  hunt,  pursue",  which  prob.  derives  fr.  I.-E. base  *wen-,  ‘to  strive  after’.  See  venerate  and  -y (representing  OF.  -ie)  and  cp.  next  word,  vena¬
da,  venatic,  venision.  OI.  veti,  ‘follows  after’, Avestic  vayeiti,  ‘hunts’,  vitar-,  ‘pursuer’,  vyana-, ‘one  pursued’,  vdti-,  ‘persecution’,  Lith.  vejit, vyti,  ‘to  hunt,  pursue’,  OSlav.  voji,  ‘warrior’, vojina,  ‘war’,  Gk.  iep.ai  (for  ‘I  as¬
pire  to,  tend  to,  make  haste,  long  for’,  OE.  wap, ‘hunting’,  ON/  veidr,  ‘chase,  hunting,  fishing’, OHG.  weida,  MHG.,  G.  weidc,  ‘pasture,  graz¬ ing,  food;  pasture  land’,  are  prob.  derivatives of  a  denasalized  var.  of  the  above  base.  Cp.  the first  element  in  voivode.
venery,  n.,  sexual  love,  (archaic).  —  From  the stem  of  L.  venus,  gen.  veneris,  ‘love,  sexual desire’.  See  venerate  and  cp.  Venus.  Cp.  also prec.  word.
venesect,  tr.  v.,  to  phlebotomize  (med.)  —  Back formation  from  next  word, venesection,  n.,  phlebotomy  (med.)  —  Medical  L. venae  sectio,  ‘cutting  of  a  vein’,  fr.  L.  venae,  gen. of  vena,  ‘vein’,  and  sectio,  gen.  -onis,  ‘a  cutting’. See  vein  and  section.
Venetian,  adj.  and  n.  —  ML.  Venetidnus,  fr. Venetia,  ‘Venice’,  fr.  Veneti  (Gk.  Ou6verot, ’Bvexoi  or  ‘Evs-roU,  an  ancient  people  of  Illy¬ rian  origin.  For  the  ending  see  suff.  -ian. vengeance,  n.  —  ME.,  fr.  OF.  (=  F.)  fr.  venger, ‘to  avenge’,  fr.  L.  vindicate,  of  s.m.  See  vindicate and  -ance  and  cp.  avenge,  revenge, vengeful,  adj.  —  Formed  on  analogy  of  revenge¬ ful  from  the  obsol.  verb  venge  (fr.  OF.  venger), with  suff.  -ful.  See  prec.  word.
Derivatives:  vengeful-ly ,  n.,  vengeful-ness,  n. venial,  adj.,  pardonable.  —  ME.,  fr.  OF.,  fr.  L. venialis,  ‘pardonable;  gracious,  kind’,  fr.  venia, ‘forgiveness,  pardon;  graceness,  kindness’,  rel. to  venus,  gen.  veneris,  ‘love’,  venerari,  ‘to  rever¬ ence,  worship’.  See  venerate.
Derivatives:  venial-ity,  n.,  venial-ly,  adv.,  venial¬ ness,  n.
venin,  n.,  a  toxic  substance  in  snake  venom  (bio- chem.)  —  F.  venin,  ‘poison’,  fr.  L.  venenum.  See venom.
venison,  n.,  the  flesh  of  a  deer.  —  ME.  veneson, veneison,  venison,  fr.  OF.  veneson,  veneison  (F. venaison),  fr.  L.  venatidnem,  acc.  of  venatio, ‘hunting,  chase',  fr.  venatus,  pp.  of  venari,  ‘to hunt’.  See  venery,  ‘hunting’.
Venite,  n.,  name  of  the  95th  psalm.  —  L.  venite, ‘come’,  imper.  2nd  person  pi.  fr.  venire,  ‘to come’.  See  come  and  cp.  venue,  ‘meeting  place’. The  psalm  is  so  called  from  its  first  word  L(khu, ‘come’,  rendered  in  the  Vulgate  by  the  word ‘Venite’.
vennel,  n.,  an  alley  (Scot,  and  Ir.)  —  F.  venelle, ‘alley’,  dimin.  of  veine,  ‘vein’,  fr.  L.  vena.  See
vein.
venom,  n.,  1)  poisonous  matter  secreted  by  some animals  (as  snakes,  spiders,  etc.);  2)  spite,  mal¬ ice-  —  ME.  venym,  venim,  venon,  fr.  OF.  venim (F.  venin),  fr.  VL.  *venimen,  which  was  formed fr.  L.  venenum,  ‘a  drug,  potion’,  through  the substitution  of  suff.  -imen  for  -enum.  L.  venenum
venomous
169o
ioyy
orig.  meant  ‘love  potion’.  It  derives  fr.  venus, ‘love,  sexual  desire' ;  see  Venus,  venerate  and  cp. venin,  envenom.  Cp.  Rum.  venin,  It.  veleno, OProven?.  veren,  Catal.  veri,  Sp.  and  Port. \eneno,  ‘venom’,  which  derive  fr.  VL.  *vem- me(ri),  resp.  fr.  L.  venerium. venomous,  adj.,  poisonous.  —  ME.  venimous,  fr. OF.  venimeux,  which  is  formed  fr.  venim,  with suff.  -eux.  See  venom  and  -ous.  Cp.  F.  veneneux, ‘venomous’,  which  derives  fr.  L.  venendsus,  ‘ven¬ omous’,  fr.  venenum,  ’venom’, venose,  adj.,  pertaining  to  a  vein;  veiny.  —  L. venosus ,  ‘full  of  veins’,  fr.  vena.  See  vein,  n.,  and adj.  suff.  -ose  and  cp.  venous.
Derivative:  venos-ity,  n.
venous,  adj.,  pertaining  to  a  vein;  veiny.  —  L. venosus.  See  venose  and  -ous.
Derivatives:  venous-ly,  adv.,  venous-ness,  n. vent,  n..  a  slit,  opening  in  a  coat.  —  ME.  vente,  a var.  of  fente,  fent,  fr.  MF.  (=  1. )  feme,  ‘cleft, slit’,  fr.  fendre,  ‘to  cleave,  split’,  fr.  L.  finder e (pp.  fissus );  see  fissile.  The  spelling  of  ME. vente  is  due  to  a  confusion  with  F.  vent,  ‘wind’. See  next  word.
Derivative:  vent,  tr.  v.,  to  let  out  at  a  vent  . vent,  n.,  1)  outlet  for  air,  gas  or  liquid;  2)  ex¬ pression.  —  Partly  fr.  F.  vent,  ‘wind’,  fr.  L.  ven- tus ;  partly  fr.  F.  event,  ‘a  breaking  forth’,  fr. eventer,  ‘to  break  forth’,  which  is  formed  fr.  pref. i-  (=  OF.  es-,  L.  ex-),  and  vent,  ‘wind’.  See wind,  ‘air’,  and  cp.  ventilate.
Derivative:  vent,  tr.  v.,  to  let  out,  vent-age,  n., vent-less,  adj.
vent,  n.,  1)  the  act  of  selling;  2)  market  for  sale. —  MF.  (=  F.)  venfe, ‘sale’.fr.VL.  vendita,' sale’, prop.  fern.  pp.  of  L.  vendere,  ‘to  sell’,  used  as  a noun.  Cp.  It.  vendita,  Sp.  venta,  which  also  de¬ rive  fr.  VL.  vendita,  and  see  vend.  Cp.  also  next word.
venta,  n.,  inn.  —  Sp.,  ‘sale,  market;  inn’,  fr.  VL.
vendita,  ‘sale’.  See  prec.  word, ventail,  n.,  the  lower  movable  part  of  a  helmet (hist.)  —  ME.,  fr.  MF.  ventaille  (F.  ventail),  fr. OF.,  fr.  vent,  ‘wind’.  See  wind,  ‘air’,  and  cp. aventail.
venter,  n.,  the  abdominal  cavity  in  insects.  —  L. venter,  ‘belly,  womb’,  for  *wend-tri-,  rel.  to vensica,  vesica,  ‘bladder’,  and  cogn.  with  OI. vastih,  ‘bladder’,  vanifthiih,  ‘rectum’,  OHG. wanast,  MHG.,  G.  wanst,  ‘paunch,  belly’.  Cp. ventricle,  eventration,  vesicle  and  the  first  ele¬ ment  in  ventriloquism.
venter,  n.,  one  who  vents.  —  Formed  from  vent, v.,  with  agential  suff.  -er. venter,  n.,  innkeeper.  —  Sp.  ventero,  fr.  venta, ‘inn’.  See  venta.
ventiduct,  n.,  a  pipe  for  the  passage  of  air  in  ven¬ tilation  ( archit .)  —  Compounded  of  L.  ventus, ‘wind’,  and  ductus,  ‘conduit’,  fr.  ducere,  pp. ductus,  ‘to  lead’.  See  wind,  ‘air’,  and  duct  and  cp. next  word.
ventilate,  tr.  v.  —  L.  ventildtqs,  pp.  of  ventilare.
‘to  branidsh  in  the  air,  fan,  set  in  motion,  agi¬ tate’,  fr.  ventus,  ‘wind’.  See  wind,  ‘air’,  and  ver¬ bal  suff.  -ate.
Derivatives:  ventilation  (q.v.),  ventilat-ive,  adj., ventilat-or,  n.
ventilation,  n.  —  L.  ventilatio,  gen.  -onis,  fr.  ven- tilatus,  pp.  of  ventilare.  See  prec.  word  and
-ation.
```


## [2026-10-17T00:01:25.715Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"vadayeiti\\|vadhu\\|vādayeiti\\|vadu\\b\\|\\*wedh-\\|wedh-\" KLN_1966.txt | head -20"
}
```


### [2026-10-17T00:01:26.159Z] TOOL RESULT

```
3718:Derivatives:  assuag-er,  n.,  assuagement  (q.v.) assuagement,  n.  —  OF.  assouagement,  fr.  assou¬ ager.  See  assuage  and  -ment. assuetude,  n.,  custom,  habit  (med.)  —  L.  assue- tudd,  fr.  assuetus,  pp.  of  assuescere,  ‘to  accus¬ tom’,  fr.  ad-  and  suescere,  ‘to  become  used  or accustomed',  fr.  I.-E.  base  *swedh-,  ‘to  make one’s  own'.  See  custom  and  cp.  consuetude.  For the  ending  see  suff.  -tude. assume,  tr.  and  intr.  v.  —  L.  assumere,  ‘to  take to  (oneself),  take  up,  adopt,  usurp',  fr.  ad-  and sumere,  ‘to  take’ ;  which  is  compounded  of  sub-, ‘under’,  and  emere,  ‘to  take’.  See  exempt  and cp.  consume,  presume,  resume,  subsume.  Cp.  also redeem.
10016:custody,  n.  —  L.  custodia,  ‘watching,  guard,  care, protection’,  fr.  custos,  gen.  custodis,  ‘watch, guard,  preserver,  keeper,  overseer,  protector’, fr.  I.-E.  base  *(s)qeudh-,  ‘to  cover’,  whence  also L.  cudo ,  ‘helmet  made  of  skin’,  OI.  kuharam, ‘cave’,  kuhufr,  ‘new  moon’,  lit.  ‘that  which  is hidden’,  Gk.  xeijfleiv,  ‘to  cover,  hide,  conceal', W.  cudd,  ‘a  hiding’,  cuddio,  ‘to  hide’,  Mir.  codal, ‘skin’.  Cp.  custos.  For  derivatives  of  the  related base  *(s)qeut-  see  hide,  ‘skin’.  The  bases *(s)qeu-dh-  and  *(s)qeu-t-  are  dental  enlarge ments  of  base  *(s)qeu-,  ‘to  cover,  hide’.  See  sky and  cp.  words  there  referred  to. custom,  n.  —  ME.  custume,  custome,  fr.  OF.  cos¬ tume,  custume  (F.  coutume),  fr.  L.  consuetu- dinem,  acc.  of  consuetudo,  ‘custom,  habit,  use, usage’,  fr.  cdnsuetus,  pp.  of  consuescere,  ‘to  ac¬ custom’,  fr.  con-  and  suescere,  ‘to  become used  or  accustomed’,  fr.  I.-E.  base  *swedh-, whence  also  Gk.  eS>oc;,  Jj-fto?,  ‘custom,  usage’, £9vo?,  ‘race’.  Base  *swedh-  is  compounded  of *swe-,  ‘his,  her,  its,  one’s  own’,  and  *dhe-,  ‘to put,  place;  to  do,  make’,  hence  lit.  means  ‘to make  one’s  own’.  See  sui-  and  the  verb  do  and cp.  consuetude,  costume,  which  are  doublets  of custom.  Cp.  also  assuetude,  de  suetude,  man- suete,  mastiff,  sodality.  Cp.  also  ethical,  ethnic, hetaira.
13727:ethical,  adj.,  relating  to  morality;  moral.  — Formed  with  adj.  suff.  -al  fr.  Gk.  -hftMoq,  ‘per¬ taining  to  morals,  moral’,  fr.  rftoq,  ‘habit  cus¬ tom,  usage,  disposition,  character,  moral’,  rel. to  e1>o?  (for  ‘afefloc),  ‘custom,  usage’,  e-SK^eiv, ‘to,  accustom’,  sfoiUac,  (for  *  ae-af coff-a),  ‘I am  accustomed’,  and  cogn.  with  OI.  sva'dhd, ‘custom,  peculiarity’,  L.  sodalis  (for  *swedhalis), ‘fellow,  companion’,  suescere,  ‘to  become  ac¬ customed’,  Goth,  sidus,  OHG.  situ,  MHG.  site, G.  Sitte,  MDu.  sede,  Du.  zede,  ON.  sidr,  Dan. sxd,  OS.  sidu,  ‘custom,  habit,  usage’.  The  orig. meaning  of  all  these  words  was  ‘property,  pe¬ culiarity’.  They  are  traceable  to  I.-E.  *swedh-, ‘a  compound  base  lit.  meaning  ‘to  make  one’s own’,  formed  from  the  reflexive  base  *swe-,  ‘his, her,  its,  one’s’,  and  *dhe-,  ‘to  make,  do’.  See sui-  and  theme  and  cp.  ethos,  cacoethes,  ethnic. Cp.  also  custom  and  words  there  referred  to. Derivatives :  ethical-ity,  n.,  ethical-ly,  adv.,  ethi- cal-ness,  n.
26678:osmosis,  n.,  intermixture  of  two  fluids  separated by  a  porous  membrane.  —  ModL.,  formed  with suff.  -osis  fr.  Gk.  coapms,  ‘a  thrusting,  impulse’, from  the  stem  of  w&siv,  ‘to  thrust,  push’,  which is  rel.  to  2v-oot?,  ‘shaking,  quake’,  fr.  I.-E.  base *wedh-,  ‘to  strike’,  whence  also  OI.  vadhati, ‘pushes,  strikes,  destroys’,  Avestic  vadaya-,  ‘to repulse’.
40999:vaivode,  n.,  the  title  of  local  or  provincial  rulers in  certain  Slavic  countries  of  southeastern  Eu¬ rope,  formerly  used  esp.  in  Transylvania  and  in Moldavia.  —  ML.  vaivoda,  fr.  earlier  Hung. vajvoda  (later  contracted  into  vajda),  fr.  Serb vojvoda,  lit.  ‘leader  of  an  army’,  fr.  OSlav.  voji (pi.),  ‘warriors’,  and  -voda,  ‘leader’,  from  the stem  of  voditi,  ‘to  lead’.  The  first  element  is cogn.  with  OI.  veti,  ‘pursues’,  Lith.  vejii,  vyti,  ‘to hunt,  pursue',  vainoti,  ‘to  revile',  L.  venari,  ‘to hunt,  chase’;  see  venery,  ‘hunting’.  The  second element  is  rel.  to  Czech  voditi,  etc.,  and  to OSlav.  vesti,  Russ,  vest',  Czech  vesti,  etc.,  ‘to lead',  Lith.  vedu,  vesti,  and  vadaii,  vadyti,  Lett. vedu,  vest,  and  vadu,  vadit,  ‘to  lead’,  Ir ,/edim,  ‘I lead,  bring’,  Avestic  vaSayciti,  ‘leads’.  Cp. voivode.
```


## [2026-10-17T00:01:33.839Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n=split($0,a,\"\\n\"); } /vaivode,  n.,  the  title/{print \"vaivode leaf\",NR-1} /venery,  n.,  hunting/{print \"venery leaf\", NR-1}' KLN_1966.txt; command ls /home/sfmqrb/git/rishe-private/site/pages/543.jpg"
}
```


### [2026-10-17T00:01:34.608Z] TOOL RESULT

```
vaivode leaf 894
venery leaf 899
/home/sfmqrb/git/rishe-private/site/pages/543.jpg
```


## [2026-10-17T00:01:38.180Z] TOOL CALL #12: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/543.jpg"
}
```


### [2026-10-17T00:01:38.238Z] TOOL RESULT

```

```


## [2026-10-17T00:01:50.675Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-10-17T00:01:51.102Z] TOOL RESULT

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


## [2026-10-17T00:01:57.576Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F(){ python3 tools/fetch_source.py \"$1\" --note \"page 543, $2\" 2>&1 | tail -1; }\nF 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wenh₁-' 'root Wen: PIE root, Latin/Germanic derivatives'\nF 'https://en.wiktionary.org/wiki/venus' 'root Wen node 1 Latin venus'\nF 'https://en.wiktionary.org/wiki/venor' 'root Wen node 7 Latin venor'\nF 'https://en.wiktionary.org/wiki/venenum' 'root Wen node 1 venenum'\nF 'https://en.wiktionary.org/wiki/Veneti' 'root Wen node 1 Veneti'\nF 'https://en.wiktionary.org/wiki/Venezuela' 'root Wen node 2 Venezuela'\nF 'https://en.wiktionary.org/wiki/ونیز' 'root Wen node 3 Persian Veniz'\nF 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wedʰ-' 'root Wen node 9 Wedh'\nF 'https://en.wiktionary.org/wiki/برف' 'root Wep node 3 barf'\nF 'https://en.wiktionary.org/wiki/vepres' 'root Wep node 6 vepres'\nF 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wep-' 'root Wep'\nF 'https://www.etymonline.com/word/venery' 'root Wen node 8 venery'\nF 'https://www.etymonline.com/word/win' 'root Wen node 6 win'\nF 'https://www.etymonline.com/word/wish' 'root Wen node 6 wish'\nF 'https://www.etymonline.com/word/venom' 'root Wen node 4 venom'\nF 'https://www.etymonline.com/word/Venice' 'root Wen node 4 Venice'\nF 'https://www.etymonline.com/word/venereal' 'root Wen node 4 venereal'\n"
}
```


### [2026-10-17T00:02:04.237Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/326c1a748306b631.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c4d086a515d5ebf9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fba90b815aced933.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/334fe09ebc23a823.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9e0738478d591211.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/44c2883f1ca0683d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1fc7f5ed838dac2a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8f007cfce6fb527b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/342658a8019671e5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4b4f59ee6aa57cbe.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f7e7779a6f2bd86f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/442e5f20bad0b089.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/20a293f0730f6841.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/14685e4daf2e1dae.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4214523bce20b71d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/da9120699491304b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a49230054e35fb61.txt
```


## [2026-10-17T00:02:07.270Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 326c1a748306b631 c4d086a515d5ebf9 fba90b815aced933 334fe09ebc23a823 9e0738478d591211 44c2883f1ca0683d 1fc7f5ed838dac2a 8f007cfce6fb527b 342658a8019671e5 4b4f59ee6aa57cbe f7e7779a6f2bd86f; do echo \"=== $f $(wc -c <$f.txt)\"; grep -n -A6 \"^ *Etymology\\|^Etymology\\|^ *Root \" $f.txt | head -40; done"
}
```


### [2026-10-17T00:02:07.788Z] TOOL RESULT

```
=== 326c1a748306b631 7053
62: Root 
63-
64- 1.1.1 
65- Alternative reconstructions 
66-
67- 1.1.2 
68- Reconstruction notes 
=== c4d086a515d5ebf9 10011
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
112: Etymology 1 
113-
114- 5.1.1 
115- Pronunciation 
116-
117- 5.1.2 
118- Noun 
--
139: Etymology 2 
140-
141- 5.2.1 
142- Noun 
143-
144- 5.2.1.1 
145- Declension 
--
156: Etymology 
157-
158- 6.2 
159- Noun 
160-
161- 6.2.1 
162- Synonyms 
--
176: Etymology 
177-
178- 7.2 
179- Adjective 
180-
181- Toggle the table of contents 
182-
--
=== fba90b815aced933 6677
73: Etymology 
74-
75- 2.2 
76- Pronunciation 
77-
78- 2.3 
79- Verb 
--
184: Etymology
185- [ edit ] 
186-
187- From Proto-Indo-European *weyh₁- ( “ to chase, pursue ” ) , or from Proto-Indo-European *wenh₁- ( “ to strive, wish, love ” ) (disputedly). See also Latin Venus , veneror , venia , and venēnum .
188-
189- Pronunciation
190- [ edit ] 
=== 334fe09ebc23a823 6390
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
178: Etymology
179- [ edit ] 
180-
181- From Proto-Italic *weneznom ( “ lust, desire ” ) , from Proto-Indo-European *wenh₁- ( “ to strive, wish, love ” ) . See also Sanskrit वनति ( vanati , “ gain, wish, erotic lust ” ) , Latin Venus , veneror , venia , vēnor and English wish .
182-
183- Pronunciation
184- [ edit ] 
=== 9e0738478d591211 6256
62: Etymology 
63-
64- 1.2 
65- Proper noun 
66-
67- 1.2.1 
68- Synonyms 
--
88: Etymology 1 
89-
90- 2.2.1 
91- Proper noun 
92-
93- 2.2.1.1 
94- Declension 
--
100: Etymology 2 
101-
102- 2.3.1 
103- Proper noun 
104-
105- 2.3.1.1 
106- Declension 
--
194: Etymology
195- [ edit ] 
196-
197- From Latin Venetī , q.v.
198-
199- Proper noun
200- [ edit ] 
--
247: Etymology 1
248- [ edit ] 
249-
250- Of Celtic origin, from Gaulish Wenetoi ( “ the friendly ones, the kinsmen ” ) , from Proto-Celtic *wenetos , a derivation from *wenyā ( “ kindred ” ) . [ 1 ] 
251-
252- Proper noun
253- [ edit ] 
--
=== 44c2883f1ca0683d 41929
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
--
115: Etymology 
116-
117- 5.2 
118- Proper noun 
119-
120- 6 
121- Czech 
--
151: Etymology 
152-
153- 8.2 
154- Pronunciation 
155-
156- 8.3 
157- Proper noun 
--
168: Etymology 
169-
170- 9.2 
171- Pronunciation 
172-
173- 9.3 
174- Proper noun 
--
205: Etymology 
206-
207- 11.2 
208- Pronunciation 
209-
210- 11.3 
211- Proper noun 
--
=== 1fc7f5ed838dac2a 134
=== 8f007cfce6fb527b 15607
62: Root 
63-
64- 1.1.1 
65- Alternative reconstructions 
66-
67- 1.1.2 
68- Derived terms 
--
74: Root 
75-
76- 1.2.1 
77- Reconstruction notes 
78-
79- 1.2.2 
80- Alternative reconstructions 
=== 342658a8019671e5 13079
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
--
82: Etymology 
83-
84- 2.2 
85- Pronunciation 
86-
87- 2.3 
88- Noun 
--
102: Etymology 
103-
104- 3.2 
105- Pronunciation 
106-
107- 3.3 
108- Noun 
--
122: Etymology 
123-
124- 4.2 
125- Pronunciation 
126-
127- 4.3 
128- Noun 
--
147: Etymology 
148-
149- 6.2 
150- Pronunciation 
151-
152- 6.3 
153- Noun 
--
=== 4b4f59ee6aa57cbe 4260
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
164: Etymology
165- [ edit ] 
166-
167- Uncertain; [ 1 ] proposed derivations include:
168-
169- From a Proto-Indo-European root *werp- ( “ to bend ” ) common to Ancient Greek ῥέπω ( rhépō , “ to incline ” ) .
170-
=== f7e7779a6f2bd86f 165
```


## [2026-10-17T00:02:09.808Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 80,200p 326c1a748306b631.txt | grep -v '^\\s*$' | head -70; echo ====; grep -n -A4 \"Etymology\" c4d086a515d5ebf9.txt | sed -n 30,80p | grep -v '^\\S*-\\s*$'"
}
```


### [2026-10-17T00:02:10.130Z] TOOL RESULT

```
 Reconstruction:Proto-Indo-European/ wenh₁- 
 Add languages 
 Reconstruction 
 Discussion 
 English 
 Read 
 Edit 
 View history 
 Tools 
 Tools
 move to sidebar 
 hide 
 Actions
 Read 
 Edit 
 View history 
 General
 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Get shortened URL 
 Print/export
 Download as PDF 
 Printable version 
 In other projects
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Root
 [ edit ] 
 *wenh₁- [ 1 ] 
 to love 
 Alternative reconstructions
 [ edit ] 
 *h₁wenH- [ 2 ] 
 *Hwenh₁- [ 3 ] 
 *wenH- [ 4 ] 
 *h₁wenh₁- [ 5 ] 
 *h₃wenh₁- [ 5 ] 
 Reconstruction notes
 [ edit ] 
 The Hittite evidence confirms that the final laryngeal must not be *h₂ or *h₃ , as otherwise it would have been preserved in the Hittite paradigm. For an example of such a development in Hittite, see 𒉿𒀠𒄴𒍣 ( wa-al-aḫ-zi /⁠walḫzi⁠/ , “ to strike ” ) . Hittite may also show that the term must be reconstructed with an initial laryngeal *h₁ or *h₃ , as—according to Kloekhorst—the spelling with initial ú in the imperfect form 𒌑𒉿𒀭𒅆𒆠𒌋𒂗 ( ú-wa-an-ši-ke-u-en ) might indicate that the word is to be phonologically interpreted as /ʔuənsɨke-/ , in which case it ought to reflect a pre-form with initial *h₁ or *h₃ . [ 5 ] 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *wenh₁- (43 c, 0 e) 
 *wénh₁-t ~ *wn̥h₁-ént ( athematic root aorist ) 
 Proto-Anatolian: 
 Hittite: 𒌑𒂗𒍣 ( ú-en-zi /⁠wenzi⁠/ , “ to copulate ” ) 
 Proto-Indo-Iranian: *wánHt ~ *wanHánt 
 Proto-Indo-Aryan: 
 Sanskrit: वन॑ति ( vánati ) 
 *wn̥h₁-éh₁ye-ti ( eh₁ye-essive ) 
 Proto-Germanic: *wunāną ( “ to be satisfied; to dwell ” ) ( see there for further descendants )
 *wn̥h₁-néw-ti ( new-present ) 
 Proto-Germanic: *winnaną ( “ to labor; to win ” ) ( see there for further descendants )
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: वनोति ( vanoti , “ to like; to gain ” ) 
 *wn̥h₁-sḱé-ti ( sḱe-present ) 
 Proto-Anatolian: 
 Hittite: 𒌑𒉿𒀭𒅆𒆠𒌋𒂗 ( ú-wa-an-ši-ke-u-en ) 
 ⇒ Proto-Germanic: *wunskaz ( “ a wish ” ) 
 ⇒ Proto-Germanic: *wunskijaną ( “ to wish ” ) ( see there for further descendants )
 Proto-Indo-Iranian: 
(eval):1: === not found
```


## [2026-10-17T00:02:12.611Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 200,260p 326c1a748306b631.txt | grep -v '^\\s*$'; echo ====; grep -n \"From Proto-Italic\\|Proto-Indo-European\" c4d086a515d5ebf9.txt | head; echo; sed -n 240,275p 44c2883f1ca0683d.txt|grep -v '^\\s*$'; echo; cat 1fc7f5ed838dac2a.txt f7e7779a6f2bd86f.txt"
}
```


### [2026-10-17T00:02:12.959Z] TOOL RESULT

```
Exit code 1
 Proto-Germanic: *wanjaną ( “ to accustom ” ) ( see there for further descendants )
 *wénh₁-ih₂ ~ *wn̥h₁-yeh₂-s 
 Proto-Germanic: *wunjō ( “ joy, delight ” ) ( see there for further descendants )
 Proto-Italic: *weniā ( “ indulgence ” ) ( see there for further descendants )
 *wénh₁-os 
 Proto-Italic: *wenos 
 Latin: venus ( “ loveliness, charm ” ) , Venus ( theonym ) , venēnum ( “ potion; poison ” ) 
 Proto-Indo-Iranian: *wánHas 
 Proto-Indo-Aryan: *wánHas 
 Sanskrit: वनस् ( vánas , “ loveliness; desire ” ) 
 *wn̥h₁-tro-m 
 Proto-Germanic: *wundrą ( “ wonder ” ) ( see there for further descendants )
 *wónh₁-i-s ~ *wn̥h₁-éy-s 
 Proto-Germanic: *winiz ( “ friend ” ) ( see there for further descendants )
 *wonh₁-ó-s 
 Proto-Germanic: *wanaz ( “ accustomed ” ) ( see there for further descendants )
 Unsorted formations 
 > ? Proto-Albanian: *vōnja 
 Albanian: vuaj ( “ I suffer ” ) 
 Proto-Albanian: *wana- [ 6 ] 
 Albanian: uni ( “ hunger ” ) 
 Albanian: uri ( “ hunger ” ) 
 Descendants
 [ edit ] 
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: वन् ( van ) 
 References
 [ edit ] 
 ^ De Vaan, Michiel ( 2008 ), “ venus ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 658 
 ^ Kümmel, Martin Joachim ( 2011–2026 ), Addenda und Corrigenda zu LIV² ‎ [1] 
 ^ Kroonen, Guus ( 2013 ), “*wana- 2”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [2] , Leiden, Boston: Brill , →ISBN , page 573 
 ^ Rix, Helmut , editor ( 2001 ), “*u̯enH-”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 682 
 ↑ 5.0 5.1 5.2 Kloekhorst, Alwin ( 2008 ), “u̯en- zi / uu̯an-”, in Etymological Dictionary of the Hittite Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 5), Leiden, Boston: Brill, →ISBN , pages 999-1000 
 ^ Orel, Vladimir ( 1998 ), “ uri ~ û ”, in Albanian Etymological Dictionary , Leiden; Boston; Cologne: Brill, →ISBN , page 489 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wenh₁-&oldid=92171688 "
 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European roots 
 Proto-Indo-European ReRH-shaped roots 
(eval):1: === not found
```


## [2026-10-17T00:02:16.118Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n \"Proto-Italic\\|Proto-Indo-European\" c4d086a515d5ebf9.txt | head -5; echo -----; sed -n 240,275p 44c2883f1ca0683d.txt|grep -v '^\\s*$'; echo -----; cat 1fc7f5ed838dac2a.txt f7e7779a6f2bd86f.txt"
}
```


### [2026-10-17T00:02:16.471Z] TOOL RESULT

```
372: From Proto-Indo-European *wénh₁-os ~ *wénh₁-es-os   n ( “ loveliness ” ) , from the root *wenh₁- ( “ to wish, love ” ) . [ 1 ] Cognate with Sanskrit वन॑स्   n ( vánas , “ loveliness; desire ” ) and possibly also cognate with Old Norse vanir . Although comparative evidence suggests that the name of the goddess Venus originated as a personification of the noun “ loveliness ” , this Latin noun can be interpreted in the historical period as a figurative or transferred use of the goddess's name (note its feminine gender, as opposed to the neuter gender that is reconstructed for the original noun). Accordingly, many edited works capitalize the term. 
595: Latin terms derived from Proto-Indo-European 
596: Latin terms derived from the Proto-Indo-European root *wenh₁- 
597: Latin terms inherited from Proto-Indo-European 
-----
 13.3 
 See also 
 14 
 Italian 
 Toggle Italian subsection 
 14.1 
 Pronunciation 
 14.2 
 Proper noun 
 14.2.1 
 Related terms 
 14.3 
 References 
 15 
 Norwegian Bokmål 
 Toggle Norwegian Bokmål subsection 
 15.1 
 Proper noun 
 15.1.1 
 Related terms 
 16 
 Norwegian Nynorsk 
 Toggle Norwegian Nynorsk subsection 
-----
URL: https://en.wiktionary.org/wiki/ونیز
FETCHED: 2026-10-17T00:02:01Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not FoundURL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wep-
FETCHED: 2026-10-17T00:02:02Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-10-17T00:02:19.180Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n \"Spanish\\|Venecia\\|Vespucci\\|Ojeda\\|diminutive\\|little Venice\" 44c2883f1ca0683d.txt | head -8; echo -----; grep -n \"Proto-\\|Middle Persian\\|wafr\" 342658a8019671e5.txt | head -10; echo ----; grep -n \"From\\|Proto-Indo-European\" 8f007cfce6fb527b.txt | head -20; echo -----; sed -n 164,185p 4b4f59ee6aa57cbe.txt | grep -v '^\\s*$'"
}
```


### [2026-10-17T00:02:19.674Z] TOOL RESULT

```
360: Spanish 
362: Toggle Spanish subsection 
576: English Albanian •  Asturian •  Central Huasteca Nahuatl •  Central Nahuatl •  Czech •  Danish •  Dutch •  Finnish •  French •  German •  Haitian Creole •  Hungarian •  Italian •  Norwegian Bokmål •  Norwegian Nynorsk •  Portuguese •  Romanian •  Serbo-Croatian •  Slovak •  Slovene •  Spanish •  Sranan Tongo •  Swedish •  Tatar •  Turkish •  Western Huasteca Nahuatl Page categories 
589: Borrowed from Spanish Venezuela , from Italian Veneziola , diminutive of Venezia ( “ Venice ” ) , after the stilt houses reminiscent of Venetian architecture.
790: Spanish: Venezuela   (es)   f 
899: Borrowed from Spanish Venezuela .
991: Borrowed from Spanish Venezuela , from Italian Veneziola .
1011: ( historical ) Venezuela ( South American province of the Spanish Empire ) [from 18th c.] 
-----
269: Proto-Indo-Iranian *wapras 
270: Proto-Iranian *wafrah 
271: Middle Persian 𐭥𐭯𐭫 ( ʿpl ) 
324: Proto-Indo-Iranian *wapras 
325: Proto-Iranian *wafrah 
326: Middle Persian 𐭥𐭯𐭫 ( ʿpl ) 
329: From Middle Persian 𐭥𐭯𐭫 ( ʿpl /⁠wafr⁠/ ) , from Proto-Iranian *wafrah ( “ snow ” ) . Compare Baluchi برپ ( barp ) , Central Kurdish بەفر ( befr ) , Northern Kurdish berf , Pashto واوره ( wāwra ) , Wakhi ورف ( warf ) .
550: Proto-Indo-Iranian *wapras 
551: Proto-Iranian *wafrah 
552: Middle Persian 𐭥𐭯𐭫 ( ʿpl ) 
----
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wedʰ-
4:TITLE: Reconstruction:Proto-Indo-European/wedʰ- - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/wedʰ- - Wiktionary, the free dictionary 
57: Proto-Indo-European 
59: Toggle Proto-Indo-European subsection 
90: Reconstruction:Proto-Indo-European/ wedʰ- 
142: From Wiktionary, the free dictionary
144: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
146: Proto-Indo-European
166: Terms derived from the Proto-Indo-European root *wedʰ- (lead) (24 c, 0 e) 
219: ^ Kölligan, Daniel ( 2018 ), “Chapter XX: Proto-Indo-European”, in Klein, Jared S., Joseph, Brian D. , Fritz, Matthias , editors, Handbook of Comparative and Historical Indo-European Linguistics: An International Handbook (Handbücher zur Sprach- und Kommunikationswissenschaft [ Handbooks of Linguistics and Communication Science ] ; 41.2 ), volume 3, Berlin; Boston: De Gruyter Mouton, →ISBN , § The lexicon of Proto-Indo-European, page 2262 : “ ‘lead (esp. the bride)’: *u̯edʰ- ” 
261: Terms derived from the Proto-Indo-European root *wedʰ- (bind) (18 c, 0 e) 
364: ^ Ringe, Donald ( 2006 ), From Proto-Indo-European to Proto-Germanic (A Linguistic History of English; 1)‎ [5] , 1st edition, Oxford: University Press, →ISBN , page 88 : “ PIE *wédʰstis ‘act of joining’ (*wedʰ- ‘to join’, cf. PGmc *(ga)wedana˛; Skt vádhram ‘leather strap’, Welsh gwedd ‘yoke’) > PGmc *(ga)wissiz ‘joint’ (cf. Goth. gawiss) ” 
376: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wedʰ-&oldid=91809259 "
378: Categories : Proto-Indo-European lemmas 
379: Proto-Indo-European roots 
380: Proto-Indo-European ReC-shaped roots 
381: Proto-Indo-European homonymic roots 
383: Hidden categories: Proto-Indo-European entries with more than one part of speech 
385: Proto-Indo-European entries with etymon 
-----
 Etymology
 [ edit ] 
 Uncertain; [ 1 ] proposed derivations include:
 From a Proto-Indo-European root *werp- ( “ to bend ” ) common to Ancient Greek ῥέπω ( rhépō , “ to incline ” ) .
 From a root common to Russian чуб ( čub , “ tuft, lock of hair ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Latin ) IPA ( key ) : [ˈwɛ.preːs] , [ˈwɛp.reːs] 
 ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈvɛː.pres] , [ˈvɛp.res] 
 Noun
 [ edit ] 
 veprēs   m or f ( genitive vepris ) ; third declension 
 ( usually in the plural ) thornbush , briar bush , bramble
```


## [2026-10-17T00:02:23.943Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 255,272p 342658a8019671e5.txt|grep -v '^\\s*$'; echo ----; sed -n 166,200p 8f007cfce6fb527b.txt | grep -v '^\\s*$' | head -30; for f in 442e5f20bad0b089 20a293f0730f6841 14685e4daf2e1dae 4214523bce20b71d da9120699491304b a49230054e35fb61; do echo \"-- $f\"; grep -o \"[^.]*\\(from\\|From\\)[^.]*\\.[^.]*\\.[^.]*\\.\" $f.txt | head -3 | cut -c1-600; done"
}
```


### [2026-10-17T00:02:24.653Z] TOOL RESULT

```
 hide 
 From Wiktionary, the free dictionary
 See also: برق and ترف 
 Ottoman Turkish
 [ edit ] 
 Etymology
 [ edit ] 
 Etymology tree
 Proto-Indo-Iranian *wapras 
 Proto-Iranian *wafrah 
 Middle Persian 𐭥𐭯𐭫 ( ʿpl ) 
 Persian برف ( barf ) bor. 
----
 Terms derived from the Proto-Indo-European root *wedʰ- (lead) (24 c, 0 e) 
 *wédʰ-e-ti ( thematic root present ) 
 *wédʰ-se-ti ( se-desiderative ) [ 2 ] 
 Proto-Indo-Iranian: *wádzʰati [ 2 ] 
 Proto-Iranian: *wájati 
 Younger Avestan: 𐬬𐬀𐬰𐬌𐬌𐬀𐬨𐬥𐬁 ( vaziiamnā , “ leading ” , fut med ptcp ) 
 ⇒ Proto-Iranian: *wājayati [ 6 ] 
 Khwarezmian: 𐾶𐾰𐾸𐾺𐿄 ( wʾzyt /⁠wāzēt⁠/ , “ to lead out ” , 3 sg impf caus ) 
 *wḗdʰ-s-t ~ *wédʰ-s-n̥t ( s-aorist ) [ 1 ] [ 7 ] [ 8 ] 
 Proto-Balto-Slavic: 
 Proto-Slavic: *věsъ ( 1 sg aor ) 
 Old Church Slavonic: вѣсъ ( věsŭ , “ I lead, I conducted ” ) 
 Proto-Celtic: *-wīss ( 3 sg subj ) 
 Old Irish: do-n·fé 
 *wodʰ-éye-ti ( eye-causative ) [ 1 ] 
 Proto-Anatolian: 
 ⇒ Hittite: [script needed] ( u-watemi , “ bring forth ” ) 
 Proto-Balto-Slavic: *wádīˀtei ( “ to lead, conduct ” ) ( see there for further descendants )
 Proto-Indo-Iranian: *wādʰáyati 
 Proto-Iranian: *wādáyati ( “ to lead, conduct; to bring ” ) ( see there for further descendants )
 → ? Proto-Uralic: *wetä- ( “ to lead, guide, pull ” ) 
 *wedʰ-o-s 
 Proto-Anatolian: *wedos 
 Hittite: *wedaš [ 9 ] 
 ⇒ Hittite: 𒌋𒄿𒁕𒀀𒂊𒍣 ( ú-i-da-a-ez-zi /⁠wedaezi⁠/ ) ~ 𒌋𒂊𒁕𒀭𒍣 ( ú-e-da-an-zi /⁠wedanzi⁠/ , “ to bring (here) ” ) 
-- 442e5f20bad0b089
-- 20a293f0730f6841
-- 14685e4daf2e1dae
-- 4214523bce20b71d
-- da9120699491304b
-- a49230054e35fb61
```


## [2026-10-17T00:02:27.077Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 442e5f20bad0b089 20a293f0730f6841 14685e4daf2e1dae 4214523bce20b71d da9120699491304b a49230054e35fb61; do echo \"-- $f $(wc -c < $f.txt)\"; head -5 $f.txt | sed -n 4p; grep -n \"Old English\\|Latin\\|Old French\\|Proto-Indo\\|PIE\" $f.txt | head -4 | cut -c1-500; done"
}
```


### [2026-10-17T00:02:27.632Z] TOOL RESULT

```
-- 442e5f20bad0b089 133
TITLE: 
-- 20a293f0730f6841 130
TITLE: 
-- 14685e4daf2e1dae 131
TITLE: 
-- 4214523bce20b71d 132
TITLE: 
-- da9120699491304b 133
TITLE: 
-- a49230054e35fb61 135
TITLE:
```


## [2026-10-17T00:02:32.224Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F(){ python3 tools/fetch_source.py \"$1\" --note \"page 543, $2\" 2>&1 | tail -1; }\nfor w in win wish venom Venice venereal venery; do F \"https://en.wiktionary.org/wiki/$w\" \"root Wen English $w\"; done\nF 'https://en.wiktionary.org/wiki/वपति' 'root Wep node 5 Skt vapati'\nF 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wafrah' 'root Wep Proto-Iranian wafrah'\nF 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/winnaną' 'root Wen node 5 winnan'\nF 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wunskaz' 'root Wen node 5 wunsk'\nF 'https://en.wiktionary.org/wiki/Venezia' 'root Wen node 2 Venezia'\nF 'https://en.wiktionary.org/wiki/veneror' 'root Wen node 1 veneror'"
}
```


### [2026-10-17T00:02:39.590Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1d118f546d9dc3d4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/90f938b0ea97982f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f0fc7c77bb4c0c49.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4f08c3db5c8bd565.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d633287e4b6e46c3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6d1a7deddcaaefe2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/611d0c7c4ba140f7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/85a84d475bd44e49.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/33feee69515b1318.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c8f9c9ac47e63af4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2f79bab768c0d136.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c5198d0c4cc8c272.txt
```


## [2026-10-17T00:02:42.476Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 1d118f546d9dc3d4 90f938b0ea97982f f0fc7c77bb4c0c49 4f08c3db5c8bd565 d633287e4b6e46c3 6d1a7deddcaaefe2 611d0c7c4ba140f7 85a84d475bd44e49 33feee69515b1318 c8f9c9ac47e63af4 2f79bab768c0d136 c5198d0c4cc8c272; do echo \"-- $f $(sed -n 1p $f.txt)\"; grep -n \"^ *From \\|^ *Borrowed\\|^ *Inherited\\|^ *Learned\" $f.txt | head -3 | cut -c1-450; done"
}
```


### [2026-10-17T00:02:43.091Z] TOOL RESULT

```
-- 1d118f546d9dc3d4 URL: https://en.wiktionary.org/wiki/win
602: From Wiktionary, the free dictionary
650: From Middle English winnen , from Old English winnan ( “ to labour, swink, toil, ” ) (compare Old English ġewinnan ( “ conquer, obtain, gain; endure, bear, suffer; be ill ” ) ), from Proto-West Germanic *winnan , from Proto-Germanic *winnaną ( “ to swink, labour, win, gain, fight ” ) , from Proto-Indo-European *wenh₁- ( “ to strive, wish, desire, love ” ) . 
1244: From Middle English winn , winne , from Old English winn ( “ toil, labor, trouble, hardship; profit, gain; conflict, strife, war ” ) , from Proto-Germanic *winną ( “ labour, struggle, fight ” ) , from Proto-Indo-European *wenh₁- ( “ to strive, desire, wish, love ” ) . Cognate with German Gewinn ( “ profit, gain ” ) , Dutch gewin ( “ profit, gain ” ) .
-- 90f938b0ea97982f URL: https://en.wiktionary.org/wiki/wish
230: From Wiktionary, the free dictionary
262: From Middle English wisshen , wischen , wüschen , from Old English wȳsċan ( “ to wish ” ) , from Proto-West Germanic *wunskijan , from Proto-Germanic *wunskijaną ( “ to wish ” ) , from Proto-Indo-European *wenh₁- ( “ to wish, love ” ) .
895: From Middle English fisch , from Old English fisċ , from Proto-West Germanic *fisk .
-- f0fc7c77bb4c0c49 URL: https://en.wiktionary.org/wiki/venom
209: From Wiktionary, the free dictionary
221: From Middle English venym , from Old French venim , from Vulgar Latin *venīmen , from Early Medieval Latin venīnum , from Classical Latin venēnum ( “ drug; poison; a charm ” ) , ultimately derived from Proto-Indo-European *wenh₁- ( “ to love ” ) . Doublet of venin and venene .
-- 4f08c3db5c8bd565 URL: https://en.wiktionary.org/wiki/Venice
176: From Wiktionary, the free dictionary
190: From Middle English Venyse , from Old French Venise or Old Italian , from Medieval Latin Venetia , from Latin Venetī + -ia ( suffix forming place names ) , a local tribe in antiquity whose own little-attested language is now known as Venetic . Initial scholarly agreement that they were Illyrian was based on arguments since refuted. They worshipped Belenus and were possibly Celtic or heavily influenced by Celtic culture, despite repeatedly su
-- d633287e4b6e46c3 URL: https://en.wiktionary.org/wiki/venereal
173: From Wiktionary, the free dictionary
183: From Middle English venereal , venerealle ( “ of or relating to sexual intercourse ” ) , from Latin venereus , venerius ( “ of or relating to sexual love ” ) , [ 1 ] from Venus ( “ Roman goddess of love ” ) [ 2 ] (from Proto-Indo-European *wenh₁- ( “ to love ” ) ) + -eus , -ius ( suffix forming adjectives from nouns ) .
-- 6d1a7deddcaaefe2 URL: https://en.wiktionary.org/wiki/venery
162: From Wiktionary, the free dictionary
180: From Middle English venerie , borrowed from Middle French venerie , from Old French venerie ( “ hunting ” ) , derived from vener , from Latin vēnor ( “ to hunt ” ) .
222: From Middle English venery , venerie , venerye , borrowed from Medieval Latin veneria , from venus ( “ love ” ) .
-- 611d0c7c4ba140f7 URL: https://en.wiktionary.org/wiki/वपति
155: From Wiktionary, the free dictionary
240: From Proto-Indo-Iranian *(H)wap- ( “ to strew, scatter ” ) , from Proto-Indo-European *h₂wep(h₁)- ( “ to scatter, harass ” ) . Cognate with Avestan 𐬬𐬍𐬎𐬎𐬁𐬞𐬀𐬝 ( vīuuāpat̰ , “ strews apart, plunders ” ) , and Hittite 𒄷𒉿𒀊𒍣 ( /⁠ḫuwapp- i ⁠/ , “ to hurl, throw; to mistreat, harass ” ) . See वप् ( vap ) for more etymological information.
662: From Proto-Indo-Iranian *(H)wap- ( “ to shave, shear ” ) . See वप् ( vap ) for more etymological information.
-- 85a84d475bd44e49 URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wafrah
130: From Wiktionary, the free dictionary
140: From Proto-Indo-Iranian *wapras .
-- 33feee69515b1318 URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/winnaną
138: From Wiktionary, the free dictionary
148: From Proto-Indo-European *wen- ( “ to win, achieve, overcome ” ) ; cognate with Sanskrit वनोति ( vanóti , “ to win, defeat, procure ” ) . [ 1 ] The root may be the basis of Proto-Indo-European *wenh₁- ( “ to love ” ) , with semantic connection "to feel achieved with a given thing" > "to love". ( Can this ( + ) etymology be sourced ?) 
-- c8f9c9ac47e63af4 URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wunskaz
142: From Wiktionary, the free dictionary
-- 2f79bab768c0d136 URL: https://en.wiktionary.org/wiki/Venezia
210: From Wiktionary, the free dictionary
218: From Italian Venezia . Doublet of Venetia and Venice .
249: Borrowed from Latin Venetia . [ 1 ] 
-- c5198d0c4cc8c272 URL: https://en.wiktionary.org/wiki/veneror
147: From Wiktionary, the free dictionary
155: From venus +‎ -or , from Proto-Indo-European *wenh₁- ( “ to strive, wish, love ” ) . See also Latin Venus , venia , venēnum , vēnor and English wish .
```


## [2026-10-17T00:02:52.318Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; W=incoming/WLD/WLD_Bd1_pages.txt; grep -n \"^ *[0-9]*\\.* *u̯en-\\|^uen-\\|^ *u̯edh-\\|^uedh-\\|^ *u̯ep-\\|^uep-\\|u̯en- „\\|uen- „\\|uedh- „\\|u̯edh- „\\|uep- „\\|u̯ep- „\" $W | head; echo -----; grep -n \"^wen-\\|^wedh-\\|^wep-\" AHD_watkins1985.txt"
}
```


### [2026-10-17T00:02:53.311Z] TOOL RESULT

```
1712:   Daneben idg. uedh- „binden, verbinden“ (wozu als nas.Form. wohl uendh-).
19390:uen- „schlagen, verwunden                          11
19425:   An m. Dieses uen- ist kaum gleichzusetzen mit uen- „streben, gewinnen“,
19928:an *uedh- „binden‘ oder „fiihren“.
23727:uen-s- in ags. wSs, aisl. vets „Feuchtigkeit, Nasse“?? s. u. ties- „feuchten“).
23791: l.    uedh- „sto8en, schlagen“.
23997: uep- „\verfen, streuen“.
24513:     Idg. *uendh-           ist vielleicht           nasalierte            Form zu uedh- „kniipfen,                          bindeir'
29694:uedh- „fiihren, heimfiihren                             .
44493:kuen- „feiern; heilig(en)“.
-----
1129:wedh-. To push, strike. Suffixed lengthened o-grade form *w6dh-eyo- in Greek dthein, to push: osmosis. [Pok. 1. uedh- 1115.]
```


## [2026-10-17T00:02:55.937Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; W=incoming/WLD/WLD_Bd1_pages.txt; grep -n \"streben, gewinnen\\|uen- „streben\\|u̯en- „streben\" $W | head; sed -n 23997,24012p $W; awk 'BEGIN{RS=\"\\f\"} /uep- „.verfen, streuen/{print \"leaf\",NR}' $W; echo ----; grep -n \"^wen-\\|^wedh\\|^wen\\b\\|^wen\\.\" AHD_watkins1985.txt; grep -n -i \"^wen\" AHD_watkins1985.txt|head"
}
```


### [2026-10-17T00:02:56.297Z] TOOL RESULT

```
19425:   An m. Dieses uen- ist kaum gleichzusetzen mit uen- „streben, gewinnen“,
 uep- „\verfen, streuen“.
     Ai. rapati „wirft, streut.              silt",     av. aor. vi- caput „veroden”                      stande nach
 Pedersen KG. I 93 im Zusammenhang mit                                               ir.   feinmuin , fcmnacli ..Meer-
                                                            ueb-    — ucbb-                                                               25    t

                                 4


gras“,    was ganz unwahL'scheinlich ist.                                     Ygl. unter \Yz.          mm- „speien. sich
erbrechen“.
     Gr. vmp’Tj (Fick I              312)        liat       mit     ai.      capati nichts zu tun; vgl. Bois. s. v.


ueb- „Waffe“.
   Germ. Sippe ohne auswartige Ankniipfungen. Got. wepna n. I* 1 „Waff'en \                                          .
                                                                                                                                            -
leaf 265
----
1129:wedh-. To push, strike. Suffixed lengthened o-grade form *w6dh-eyo- in Greek dthein, to push: osmosis. [Pok. 1. uedh- 1115.]
```


## [2026-10-17T00:03:00.005Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; W=incoming/WLD/WLD_Bd1_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR>=266 && NR<=269 && /venus|Venus|vanati|wunsk|winnan/{print \"LEAF\",NR; print}' $W | grep -n \"uen\\|venus\\|Venus\\|venor\\|vanati\\|winnan\\|wunsc\\|Veneti\\|LEAF\" | head -30; echo; sed -n 29694,29705p $W"
}
```


### [2026-10-17T00:03:00.331Z] TOOL RESULT

```
1:LEAF 268
7:                                                           uen-                                                             25y
15:„Lust“ (vgl. lat. Venus), vani-h f. ,,Yerlangen, Wunsch“, wozu vaffiyati
44:     Lat. venus, -eris „Liebe,LiebesgenuB, Anmut, Liebreiz", Venus Name
55:aus *couenor (vgl. ahd. giwinnmt usw.). Weitere Erkliirungen bei Yf.
60:cidalis", coibnes „Verwandtschaft“ ('*con-vcnestu ), abret.                                    coguenou „indigena“,
73:elend    (Zupitza KZ. 36. 73) sind nicht zu got. ivnntw, winnan zu stellen.
82:     Auf idg. *ueni-s geht zuriick altn. v'mr „Freund“,                                       as.      ahd.      ivini,    afries.
109: von vanar- „Holz, Wald“ nach Macdonell IvZ. 34, 292) zu idg. uen- ge-
114:LEAF 269
119:   Idg. *uenistro- wird durch altn. vinstri „link ‘, as. winistar afries. minister                                                    ,
134:nicht freuend                     ,                                                                                                                                 ,
173:,,Wunsch“, ags. wusc    ahd. ivitnsc, wunsch usw., mit Abltg. altn. dskja
185:in der Sippe got. winnan „leiden“, altn. vinnn „arbeiten, ausrichten, iiber-
186:           as. winnan „stroiten, kampfen

uedh- „fiihren, heimfiihren                             .



  Fick I 4 133. Curtius 322. Yanieek 279.
  Fraglich bleibfc es, ob lat. vilis ,/wohlfeil, von geringem Werte ££ unter
irgendeiner Bedingung hierherzustellen sei, da bisher keine zweifelsfreie
Erklarung und Etymologie gefunden ist. Tiber die verschiedenen Versuche
vgl. Yf. LEWb. 2 837.


ill-    in Schallworten.
```


## [2026-10-17T00:03:02.649Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; W=incoming/WLD/WLD_Bd1_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR==268' $W | sed -n 40,60p; awk 'BEGIN{RS=\"\\f\"} /uedh- „f.ihren, heimf/{print \"leaf\",NR}' $W; grep -n \"vadayeiti\\|va.ayeiti\\|vädayeiti\" $W | head"
}
```


### [2026-10-17T00:03:03.160Z] TOOL RESULT

```
     Gr.        Parallelen       iiberzeugender            Art sind            bisher       nicht      gefunden:            aval;
„Herr‘' (vgl. Prellwitz, Boisacq) wird kaum hierherzustellen sein, iiber evvg
„Bett.          Lager“ vgl. cm- und             iiber owro,'          Solmsen KZ. 32, 288.
     Lat. venus, -eris „Liebe,LiebesgenuB, Anmut, Liebreiz", Venus Name
der Liebesgottin, vcnustus „anmutig, reizend, lieblich“. vcneror -uri „mit                                           ,



religidser Scheu verehren. hoch verehren, huldigen, demiitig bitten", ursprgl.
„die Liebe bezeugen".     Zweifelhaft bleibt die Yerbindung mit lat. Conor                                                            ,



-fin ,.den Anlauf zu einem Unternehmen machen, versuchen", vielleicht
aus *couenor (vgl. ahd. giwinnmt usw.). Weitere Erkliirungen bei Yf.
LE\Yb. 2" 86 f.   1


     Air. fine          (fvenja) „Verwandtschaft,                   Stamm, Familie",                   ftn-galach „parri-
cidalis", coibnes „Verwandtschaft“ ('*con-vcnestu ), abret.                                    coguenou „indigena“,
nbret. gwenn „race, germe", cymr. given „risus, subrisio, arrisio".                                                      Gwynedd
leaf 321
23850:Frau  vadayeiti (Kaus.) „fiihrt, zieht, schleppt". mit upa- „eine Frau zur
```


## [2026-10-17T00:03:06.160Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; W=incoming/WLD/WLD_Bd1_pages.txt; sed -n 23840,23856p $W; awk 'BEGIN{RS=\"\\f\"} /vadayeiti \\(Kaus/{print \"leaf\",NR}' $W; grep -n \"lemma: uedh-\\|lemma: u̯edh-\" POK_full.txt"
}
```


### [2026-10-17T00:03:06.498Z] TOOL RESULT

```
vielleicht ahd. wascan „waschen“ (s. Pedersen IvG. II 515; oder letzteres
zu TFos.w, s. *ued „netzen“?).


2.    uedh „fiihren; heimfiihren, heiraten (vom Manne)“.
     rudhu-h „Braut, junge Frau; Sehwiegertoehter“. av. radii- ,,Weib.
      Ai.
Frau  vadayeiti (Kaus.) „fiihrt, zieht, schleppt". mit upa- „eine Frau zur
         1
             ',


Ehe geben“, mit vs- „(Fraueni entfiihren, rauben“, vadrya- ..heiratsfahig
(von Madchen)“:
leaf 264
```


## [2026-10-17T00:03:12.656Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *[0-9]* *va[dδ8]u-\\|^ *[0-9]* *vad-\\|^[0-9]*vad\\|vadayeiti\\|vädayeiti\\|vä8ayeiti\" BRT.txt | head -20; grep -n \"^ *[0-9]* *vafra\\|vafra-\" BRT.txt | head"
}
```


### [2026-10-17T00:03:13.255Z] TOOL RESULT

```
22418:vadar-
11544:•  ').  JaiwLvafra-  Adj.  'mit  tiefem  Schnee' : ipmö  ('des  Winters')  .  .  °raAe  V.  7.  27.
22448:vafra-
22453:•  j.  vafra-  m.  'Schnee*:  vftaxti{sä.)  -rohe V.2.34;  —  WM<»3^  (sd.)  Vfl  (als  AP.) sna^^  V.  2.  22;  F.  8.  [Az.  4,  Vyt  2: lies  vifrS?\
```


## [2026-10-17T00:03:14.642Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22400,22460p BRT.txt | cut -c1-300"
}
```


### [2026-10-17T00:03:14.982Z] TOOL RESULT

```
mit  US  '(Frauen)  entfllhren,  rauben':  yai
kainyS  usvsoayeinti  . .  ayrvff  mjämayanti
(Sp.  1081  o.)  Yt  ly.  59.
mit  VT  'hin  und  herführen':  spsngm  (sd.)
. .  airilim   taoa   aaä  pa^a  vfväoayantu
V.Ä16.
PDs.  du'v'tiata  'ich  bringe  hinein',  ar^.  rä- vali 'er  bringt';  ksL  vaiq,  liLiin/ü  'ich  fahre, heirate'.  S.  noch  ZuBATif  ASlPh.  l6.  104.  — Fü. :  väitnltan,  zu  V.  4  erL :  bii  lau  l  dafund^ (lu  V.  18]'.  frarämenUan.  —  ')  Das  zweite Praer.  wiederholt;  a,  V.  8.  16
•  j.  vada-  m.  'Keil'  zum  Spalten  des Holzes":  'dtm  titiMrim  tiiiJnüttm  V. 14.  7.
Vgl,  vadoT'.  —  ai.  vadhä-  m.  von  Indrat  Ge- EchosE.   —   Pü.:   kartinak  (Tgl.  tärt  'Messer*) □der  kultnak  (vgl.  np.  kudina  'Hammer')?  — 0  VgL  därv  .  .  äpävadlüi  RV.  10.  146.  4. j.  viAcürttyoi,  Var.  *yoB  F.  8-.  lies  'iairya^.
*  j.  va<)a')^n-  m.  EN.  eines  glaubensfeind- lichen  Fürsten:  adavata  ..  aarS  mainyui: ,  ,  tard^uilra  .  .  apastavartuha  .  .  dabtqm mätdayasnJm  vindäi  ystum  ya^a  vindai °nS  (NS.)  ■'  daiähupaitis  ". .  Zar. !  schwör der  maid.  Religion  ab,  um  die  Gunst  zn erlangen,  wie
*)  Nach  mp.  Schriften  mit  AiDahik  identisch; vgl.  Mx.  j/.  24f. :  ahraman  e  sara%u!l  dräyitt  itt haiar  hal  in  din  . .  i  matdaymnän  aj>ik  itti än^äk  at  1000  säl  j^aläiJi  . .  dahem  Hgön  1/08070«« (geschr.  ntkann)»  dahyupeU  dahAk  dir.
Eig.  Bed.?  —  ■)  Them.  —  '}  Hds.  vatara; '  ■  -      dy).  -   J)  S.  dazu  West  SEE.  24.
103.  ■
-  3»-
•  j.  va8ay- :  vaili-  f.  'Wasserlauf,  Be- wässerungskanal': nil  tat  3p»m  hintatä ' yavd.caränlm  (sd.)  ana  tä  '%Tnt  ayä  ana bittm  . .  pasla  tüirJm  nasäum  ava.iansfnti (sd.)  "entlang  dem  Kanal  läuft  es  (das Wasser)  alsdann,  entlang  zum  zweiten Mal  . .,  dann  .  ."  V.  5
Zum    au   V.   undlä.   —    VgL   *uia:  —   Vgl.
dby  Google
1345
vadar-
vafav-
*346
arm.    gil    'fluss';     PDw.     v5d    'Kanal'.     —
•  j.,  g.  vadar-  n.  'Waffe  (zum  Schlagen)': yasla  'dar!  vSisdai  aläuns  "und  der  die Waffe  wider  den  Rechtgläubigen  erhebt" Y._j2.  lo;  —  paifi  .  .  kihrpim  .  .  haoma . .  'dar}  /ai\i^'>  "gegen  den . .  Leib  schlag . . die  Waffe"  Y.o.  30;  30—32*,
Vgl,  vada-  und  vädäya:  —  ai,  vidhar-  n.  (bes. von  Indrai  Waffe).  —  PS-  (lu  Y,  32):  hacai pa  ptAlikik  ösiin  dal  ö  oAravän,  (lu  Y,  9); paltäklne  (SQ.:  paraiäiaya)  lanän,  erl,;  ia! iärai  api  gäw,  —  ')  VgL  jahi  vädhak  RV.  4. i%.  9.
•  j.  vaSairyav-"  Adj.  'nach  Begattung veitangend,  brünstig',  vom  Kamelhengst'': uitrS  'rii^^  Yt.i4.39;  12;  —  uÜrahe hhrpa  'ryaol  Yt  i^.  n ;  *F.  8;  —  uitr&nh5 .  .  p»r3tamna  (sd.)  'ryavd  Yt, /7. 13,
PPA,  (Saqp.  4),  aus  •i^iaiVj'i- den.  Praes.  31 ; s.  i'oJü-.  —  ai.  vgl.  vadküyäv-  Ad],  (und  vadhar- yäniim  RV.  /.  161.9?);  Gdn.  3Yt  68,  —  Pu.: vaharn),  Npii.:  xabar  dar  n  rik  däHnnda.  — •)  NA.  auLh  •lar:  —  >)  VgL  zBed.  Yt,  14.11 mit  7,  15.  —  J>  Sta(t  'ryiä 
•  g.  vad^mna-  Adj.  'zuredend,  mahnend': süx^Sal  vatyamnähyS  kainibys  mraomi xsmaiiyica  'nU  "Lehren  künde  ich  den heiratenden  Mädchen  und  euch  (den Freiem),  mahnend"  Y.jj,  5"'.
PPM.,  lu  ai.  vadali  'er  sprichl*.  ~  Pü.;  äiä- iJA,  nach  der  geringwertigen  Lesart  vtud'.  — >)  Der  Sprecher  der  Strophe  ist  wie  überall in  Y.  S3  ausser  in  Str.  4,  die  das  Geldbnis des  Bräutigams  enthalt,  der  Brautvater,  Zara- %iistra.  Bei  Gdn.s  Deutung  von  vad'
•  j.  va8ü-  f.  'Weib,  Frau":  'lu  (NS.)'> wöaz-fl  (sd)  F.  2  f.
ai.  vadhu-  f.;  np.  vgl.  bayög  'Braut'.  Vgl,  va- irya-.  —  ■)  Nach  dem  Musler  der  T-Slämme (lu  S  409:  vgl.  S  407\
•  j.vaSut-  f.EN.  eines  gläubigen  Mädchens; kanyä  *'%utö''>  asaonyh  Yt/J.  141.
Vgl.  V(^ü;  ziairya-  und  Jayrut-.  —  ')  So  F  1.
•  j,  vaSrya-  Adj.  'heiratsfähig',  von Mädchen '' :  'äwam  kaimn3  're'''  yaona xia^-ra  hväpi  jav>yaiiie  Yt5.  87.
Zu  VA.vidU,  ksl.^fo'q'ich  heirate' ;  s,  vad-.  —  Vgl. miSh-,  v/Aairymi-.  —  ')  Die  Bedeutung  scheint mir  durch  das  folgende  /aräi/iJ  lixanäilii  ge- sichert, —  ")  NPm.,  für  'rya  stehend,  S  sS*. 32.    iainin-  ist  als  mask,  behandelt,  vgl.  ana-
•  p,  Vaa^a-bara-  m.  'Stabträger"  (?) '>, Titel  eines  persischen  HofwUrdenträgers: aspacanä  'ra'  D.p.
np,  bär  'Zweig'  (rfoRN  GlrPh.  /  b,  170);  gol. vgl,  wandus  'Rute'.  —  ■)  So  nach  JusTI  ZDMG. 50.  663,  53.  9z,  GIrPh.  2.  426.  Dagegen neuerdings  Fov  ZDMG.  54.  356,  55.  509.
•  g.  vap- V.,  nur  mit  wr 'disiccre'.  Praes.  4 väpa-,
'zerstören,  verwüsten' :  yascä  västr3  vT- vapat  "imd  der  die  Weideländer  verwüstet" Y.  J2,  10.
ai,  väpali  'er  wirft'.  —  Vgl.  vniäpa-.  —  Pü. : viyäfäninitan^),  erl.:  lapsh  ape  iarlan;  Sü. : udiiäsayüum,  erl.:  iimäiayitum.  —  ')  Wegen des  Anlilangs(s.np,£iyä<^);  etym.  Verknüpfung der  Wörter  ist  unm&glich,
•  j.  vawzaka-  m.  Name  eines  ^aAÜchen Tiers:  yas)  %wä  nSit  aiwiMrushnti  aiisla (sd)  ariknaim  'käiÜca  (als  Subj.)  Yt 5,90.
Ableil.  aus  'vawia-,  mit  tvS  aus  M-t-J,  %  53^. —  nbal.  gvaiz  'Biene,  Wespe,  Horniss';  ai. vgl.  ürnavaöhay-  m.  'Spinne';  s,  BthL,  AF, /.  21,  ZDMG.  44.  552,  Bgm.  Grdr."  /,  704, 724.      Gani  faUch   DsT,  ZA.  2.  388.
•  j.,  g,  vaf-  V.  'besingen'.  Praes.  37 ufya:
'besingen,  einen  Sang  dichten  auf  — ' (Akk.):  *yavat3  %ivä  matda  *ilaomT ujyäcä  (iSPA,)  "(immer)  so  lang  ich  dich, Q  M.,  lobe  und  besinge"  Y.4:_J,  8;  — yS  va  asä  ufyäni  manaüS  vohQ  apaourvlm (sd.)  Y.  2Ä  3 ;  —  asäunqm  va>3uhJl . . fravalayS  staomi  zbayemi  ufyemi  
Eig,  'weben',  mit  Übertragung  auf  die  künal- liche  Fügung  der  Worte  (s,  ai,  väyali);  »gl, va/mi-.  —  Vgl.  np.  iJ/ad  'er  webt'.  —  Pü. (dRn.):  ^^eitnisnO,  eil :  pa  ^ii  därisit  und  ö x'i!  iuniin;  j^m  D  iülaa,  erl. ;  fa  s^esiA  ittälan; x'isenTia« ').  —  ')  an  d  da'
•  g.  vafav-  m.  'Spruch;  Satzung,  Bestim- mung": at  S  (Sp,  II  m.)  vaocat  ahurB masdä  vldvä  'füs  vyänayä  (sd.)  ". .  ÄhM., der  die  Satzungen  kennt"  Y.  25. 6;  — arsi  msi  sriiücam  vankSuS  'fui  manaa?ß (Sp.  1128  o.)  "recht  soll  mir  kund  werden
43
dby  Google
1347
vafra-
vaDhäna-
1348
die   Bestimmung    fUc    den    guten    Sinn"
Zun  V.  va/'-i  eig.   'cumen';    1.   auch  Tible Go4«<].*  3.  132.  —  Pü.:  visdfän,  Sü.:  vinäia-
•  j.  vafra-  m.  'Schnee*:  vftaxti{sä.)  -rohe V.2.34;  —  WM<»3^  (sd.)  Vfl  (als  AP.) sna^^  V.  2.  22;  F.  8.  [Az.  4,  Vyt  2: lies  vifrS?\
KompE.  —  mp.  (Po.)  vafr,  np.  ^o^.
•  j.  vefra'yä-  m.  Name  eines  Bergs  oder Gebirgs**:  ahmat  haca garayS fraoxSyqn . . lyämakasca  {sA.)  'yäscä***  Ytip.  5.
*)    Bd.  13.  3  steht  dafür  Tia/rmami    ('schnee-
trich').  —    ••)  Nach  West  SliE.  J.  39  meiaen
die  beideo  Namen  den  Ja/ji/;t»4('Weissenberg'J
and  den  Siyähküh  ('Schwaiienberg'),  die  Qstlich
von  Harit  den  Narirüä  einfassen.
```


## [2026-10-17T00:03:18.806Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22370,22400p BRT.txt | cut -c1-400"
}
```


### [2026-10-17T00:03:19.202Z] TOOL RESULT

```
pü.:  fehlt.  —  ')  Die  Worte  stehen  in  Fä.i ■"■?  marl  .  .  fa  . .  a/räi  öimurihüh  äslaret  ka mariö.mar?/anifmca    nc    kunll  agdn  ^änS  ia
db,Google
1343
va£ö.urvatay-
•  j.  vafcö.urvatay-  t  'Vertrag,  der  auf dem  (blossen)  Wort  beruht,  bloss  durch mündliche  Verabredung  abgeschlossen  ist': •urvaiti/  V.J.  51  PUZ.">,
KompE.  —  1)  Wird  «U  afiaitjt  'Aweitastelle' beteichnet,  deren  Aufsagen  eine  Taiui.pft7%a- Sünde  aasgleicht
•  p.  »»  "vajanam  »»  Bh.5.  i. Hentellnngsversuch    bei    Fov    KZ.   J5.  48; JOppebt  Le  Peuple  ..  des  M6des  159   sieht in  dem  Wort  einen  EN.
p,  a-i/aja-m  Bh,  2.  I3,  14;  s.  Sp.   170  o.
•  j-i  g-  vat-  V,  'gnanim  esse,  fieri',  nur mit  I^aev.  Praes.  2  vata-,  30  (Kaus.) vataya-;  PrP.  vaitl,  —  Inf.  *°vaUe.
wXaipi  1)  'einerSachekund(—  kundig) sein,  etwas  verstehen,  vertraut  sein  mit  — ' (Gen.):  yS  fraistiin  apivaLlite  dainayä  .  . yaoidä^ryät  (sA.)  kaca  V.g.i;  47,  52;  — ■ usta  tl  aipivatahe .  .  *vacam  ir>^uxoanam Y,  5.  25.  a)    absoL    'die    (verlangten)
Kenntnisse  besitzen  sva.  ausgelernt  haben': *yai?  tat  apivalaiti^^  pärantarfm  (sd.)  isöit "wenn  er  dann  (bei  diesem  Lehrer)  aus- gelernt  hat, . ."  N.iS.  2)  'kund  (—  be- kannt) werden,  zugesagt  werden':  kä)ia  . . tai  mXiä>in  hanäni  (sd) . ,  Ayat  mBi  mazdä apivaitl  . .  yah3  .  .  *taibyS  dar»ha  (sd.) Y.  44.1 8.
mit^5Kaus,'enaiTare,JemaDdem(Dat) etwas  zum  Verständnis  bringen':  siada (sd.)  v?r3syBtacä  l^  akmäi  fracä  väiffystü  li aiiöyB  ySi  . .  ". .  soll  er  es  fiir  seine  Person betätigen  und  es  zum  Verständnis  bringen denen,  die  .  ."  Y.35.6;  —  tat  at  vP v>n^3mahl  fraüä  vätsyämahl  Y._J5.  7.
mi.  äpivataü,  äprvät<qnUi.  —   Vgl,  aol-.  —    Pü.
(rär  aipi  v/W):  aitdar  äSmitan,    [(äi /rä  väf) :
äkäihülan.    —    ")  Hds.  afyaiili,   s.  aber  Pü.;
kaci  fa  äi  andardänel  kum  cäit.
'].  vaiie  F.  8:  lies  vasti,  s.  ivah-;  —  F.  r3:
lies  latle,  s.  säy-, j.  ryi  vailua  N.  pO:  lies  ,y3vaitü.
•  j.    vad-    'führen'.     Praes.  30    (Iter.)
väoaya-.
'führen,  ziehen,  schleppen':  ^o^a  banda- yeni  ..franrasyänim  Uta  baitsm  vä%aymi Yt.p.  18;  ^yat ..  baslB  atakat  väiayamnS (pass.)  Yt  15.52;  —  z'itansi}  (sd.)  datvS .  .  urvämm  bast?m  väliayeiti  W.ir/.ti).
mit  upa  'zuführen,  zur  Ehe  geben';  upa va  nairikam  vaöayaSa  "(so)  möge  man (ihnen)  eine  Frau  zur  Ehe  geben"  V.4.44; —  jfanAa  vä  duyöa  vä  , ,  *näiri^watiai
vaÄay-  1344
upa.v/iaayaäa    "es    möge    eine   Schwester
oder  Tochter . .  zur  Ehe  gegeben  werden"
V.  74.15.
mit  upa  und  vT  'hinzu  imd  (dann)  hin
und  herführen':  yesi  nsit  upa  vl..span?m
(sd.)  x^aiayafit  tarn   aRa  pa%i  vlfaZo'
yatttu^'>  y.S.iT,  18.
mit  US  '(Frauen)  entfllhren,  rauben':  yai
```


## [2026-10-17T00:03:26.857Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^wen\\|^wedh\\|To lead\\|wen-1\\|^wen-\" AHD_watkins1985.txt | head; grep -n \"lemma: u̯edh\\|lemma: uedh\\|lemma: [0-9]*\\.* *uedh\" POK_full.txt; grep -n \"uedh-\\|u̯edh-\" POK_full.txt | head"
}
```


### [2026-10-17T00:03:27.328Z] TOOL RESULT

```
372:deuk-. To lead. 1. Germanic *teuhan in Old English téon (> Middle English tuggen), to pull, draw, lead: TUG; WANTON. 2. Suffixed zero-grade form *duk-d- in Ger- manic *tugdn in Old English togian, to draw, drag: TOW}. 3. Suffixed o-grade form *douk-eyo- in Old English *tiegan, tigan, to bind: TIE. 4. Suffixed o-grade form *douk-mo- in Germanic *tau(h)maz in Old English téam, descendant, family, race, brood: TEAM. 5. Germanic denominative *tau(h)mjan in Old English téman, tieman, to beget: TEEM!. 6. Basic form *deuk- in Latin diicere, to lead: DOCK!, DOGE, DOUCHE, (DUCAL), (DUCAT), (DUCH- ESS), (DUCHY), DUCT, DUCTILE, DUKE; (ABDUCENS), AB- DUCT, ADDUCE, CIRCUMDUCTION, CON3, (CONDOTTIERE), CONDUCE, CONDUCT, DEDUCE, (DEDUCT), EDUCE, (EN- DUE), INDUCE, INTRODUCE, PRODUCE, REDOUBT, RE- DUCE, SEDUCE, SUBDUCTION, SUBDUE, TRADUCE, TRANSDUCER. 7. Suffixed zero-grade form *duk-d- in Latin éducdre, to lead out, bring up (é- < ex-, out; see eghs): EDUCATE. [Pok. deuk- 220.]
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
839:parative) form *pro-tero- in Greek proteros, before, former: HYSTERON PROTERON, PROTEROZOIC. VI. Exten- ded forms *prai-, *prei-. 1. Latin prae, before: PRE-; PRETERIT. 2. Suffixed (comparative) form *prei-yos- in Latin prior, former, higher, superior: PRIOR2. 3. Suffixed form *prei-wo- in: a. Latin privus, single, alone (< “standing in front,” “isolated from others”): PRIVATE, PRIVILEGE, PRIVITY, PRIVY; DEPRIVE; b. Latin proprius, one’s own, particular (< pré priv6, in particular, from the ablative of privus, single): PROPER, PROPERTY; APPRO- PRIATE, PROPRIOCEPTION, PROPRIOCEPTOR. 4. Extended form *preis- in: a. suffixed (superlative) form *preis-mo in (i) Latin primus (< *prismus; ablative plural primis), first, foremost: PREMIER, PRIMAL, PRIMARY, PRIMATE, PRIME, PRIMITIVE, PRIMO, PRIMUS; IMPRIMIS, PRIMA FACIE, PRIMAVERA, PRIMEVAL, PRIMIPARA, PRIMOGENI- TOR, PRIMOGENITURE, PRIMORDIAL (ii) Latin compound princeps, “he who takes first place” (-ceps, “-taker”; see kap-), leader, chief, emperor: PRINCE, PRINCIPAL, PRIN- CIPLE; b. suffixed form *preis-tano- in Latin pristinus, former, earlier, original: PRISTINE. VII. Extended form *pres- in compound “*pres-g“u-, “going before” (*gvu-, to go; see gWa-), in Greek presbus, old, old man, elder: PRESBYTER, (PRIEST); PRESBYOPIA. VIII. Extended form *proti in Greek pros, against, toward, near, at: PROS-; PROSOPOPEIA. Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-’. [Pok. 2. A. per 810.] per-?. To lead, pass over. A verbal root belonging to the group of per’. I. Full-grade form *per-. 1. Suffixed form *per-tu-s in Germanic “*ferthuz, place for crossing over, ford, in Old Norse fjérdhr, an inlet, estuary: FIRTH, FJORD. 2. Suffixed form *per-ond in Greek peroné, pin of a brooch, buckle (< “that which pierces through”): PERONEAL. II. O-grade form *por-. 1. Germanic *faran, to go, in: a. Old English faran (> Middle English faren), to go on a journey, get along: FARE; WAYFARER, WAY- FARING, (WELFARE); b. Old High German faran, to go, travel: GABERDINE. 2. Suffixed form *por-o-, passage, journey, in Greek poros, journey, passage: PORE”; EMPO- RIUM, POROMERIC. 3. Suffixed (causative) form *por- eyo-, to cause to go, lead, conduct, in Germanic *farjan, to ferry, in Old English ferian, to transport: FERRY. 4. Lengthened-grade form *pdér- in: a. Germanic suffixed form *f6r-ja- in Old English (ge)féra, “fellow-traveler,” companion (ge-, together, with; see kom): FERE; b. Ger- manic suffixed (causative) form *fér-jan in Old High German fuoren, to lead: FUHRER. 5. Possibly suffixed form *por-no-, feather, wing (< “that which carries a bird in flight”), in: a. Germanic *farnd, feather, leaf, in Old English fearn, fern (having feathery fronds): FERN; b. Sanskrit parnam, leaf, feather: PAN2. III. Zero-grade form pr-. 1. Suffixed form *pr-tu-, passage, in: a. Ger- manic *furdu- in Old English ford, shallow place where one may cross a river: FORD; b. Latin portus, harbor (< “passage”): PORT!; IMPORTUNE, OPPORTUNE. 2. Suffixed form *pr-té in Latin porta, gate (> Old French porte, door): PORCH, PORT’, PORTAL, PORTCULLIS, PORTE-CO- CHERE, PORTER®, PORTICO, PORTIERE, PORTULACA. 3. Suffixed (denominative) form *pr-to- in Latin portdre, to carry: PORTS, PORTABLE, PORTAGE, PORTAMENTO, PORTATIVE, PORTER}; COMPORT, DEPORT, EXPORT, IM- PORT, (IMPORTANT), PORTFOLIO, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT. [Pok. 2. B. per 816.]
1129:wedh-. To push, strike. Suffixed lengthened o-grade form *w6dh-eyo- in Greek dthein, to push: osmosis. [Pok. 1. uedh- 1115.]
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
2445:VAIR wer-1 VaisyA_ weik-1 VALE! wel-3 VALEDICTION deik- VALENCE wal- VALET upo VALETUDINARIAN wal- VALHALLA kel-2, wele-2 VALIANT wal- VALID wal- VALKYRIE wele-2 VALLATION walso- VALLEY wel-3 VALONIA gWele-2 VALOR wal- VALUE wal- VALVE wel-3 VAMOOSE wadh-2 VAMP! ped-1 vaAN3 wet-1 VANADIUM wen-1 VANDAL wendh- VANE pan- VANG pag- VANILLA wag- VANIR wen-! VANISH eu-2 VANITY eu-2 VANQUISH welk-5 VAPID kwép- VAPOR kwép- VAQUERO wak- VARA wa- VARIEGATE wer-1 VARIETY wer-1 VARIOLA wer-! VARIORUM wer-! VARIOUS wer-1 VARIX wer-1 VARLET upo VaRUNA wel-1 VARUS wa- VARVE kwerp-
2447:VARY wer-? VASSAL upo vaT ped-2 vaTic wet-1 VAULT! wel-3 VAULT2 wel-3 VAUNT eu-2 VEAL wet-2 VECTOR wegh- VEDA weid- VEDANTA ant- VEDETTE weg-2 VEER2 per! VEGETABLE weg-2 VEHICLE wegh- VEIL weg-! VELDT pele-2 VELIGER gerere VELLEITY wel-2 VELOCITY weg-2 VELOURS wel-4 VELUM weg-1 VELVET wel-4 VENAL wes-1 VENATIC wen-1 VEND d6-, wes-! VENDETTA deik- VENEER per! VENERATE wen-! VENEREAL wen-! VENERY! wen-1 VENERY2 wen-! VENIAL wen-! VENIRE gWa- VENISON wen-! VENOM wen-! VENT wé- VENTAIL wé- VENTER udero- VENTILATE weé-
2449:VENUE gWa- VENUS wen-1 VERACIOUS wéro- VERB wer-6 VERBENA wer-3 VERBOTEN bheudh- VERDANT virére VERDICT deik-, wéro- VERDITER ters- VERGE? wer-3 VERIDICAL deik-, wéro- VERIFY wéro- VERISIMILAR wéro- VERISM Wéro- VERITY wéro- VERMEIL wer-3 VERMI- wer-3 VERMICELLI wer-3 VERMICULAR wer-3 VERMIN wer-3 VERNAL west VERRUCA wer-1 VERSATILE wer-3 VERSE! wer-3 VERSION wer-3 VERST wer-3 VERSUS wer-3 VERTEBRA wer-3 VERTEX wer-3 VERTIGO wer-3 VERVAIN wer-3 VERVE wer-6 VERY weéro- VESICA udero- VESPER weS-pero-
```


## [2026-10-17T00:03:30.461Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o \"wen-[1!']*\\. To desire[^[]*\\[Pok[^]]*\\]\" AHD_watkins1985.txt | head -3; grep -o \"wedh-[^.]*\\. To lead[^[]*\\[Pok[^]]*\\]\" AHD_watkins1985.txt|head"
}
```


## [2026-10-17T00:03:32.155Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^wen\\|wedh-\\. To lead\\|wedh-. To lead\" AHD_watkins1985.txt|head; grep -n -o \".\\{0,20\\}wen-[^ ]*\\. To .\\{0,800\\}\" AHD_watkins1985.txt | head -3"
}
```


### [2026-10-17T00:03:32.649Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-17T00:03:36.927Z] TOOL RESULT

```
ugrep: error: error at position 389
xbf])*\. To (?:[^\n\x80-\xbf][\x80-\xbf]*){0,800}
                    exceeds complexity limits___/
```


## [2026-10-17T00:03:39.907Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt').read()\nfor pat in [r'wen-[^\\s]*\\s*To desire', r'wedh-[^\\s]*\\s*To lead', r'VENERY', r'Pok\\. 1\\. uen', r'uen-',r'uedh-']:\n    for m in re.finditer(pat,t):\n        print(pat, '::', t[max(0,m.start()-50):m.start()+900].replace('\\n',' '));print('---'); break\nEOF"
}
```


### [2026-10-17T00:03:41.298Z] TOOL RESULT

```
wen-[^\s]*\s*To desire :: mein, to vomit: EMESIS, EMETIC. [Pok. wem- 1146.] wen-', To desire, strive for. 1. Suffixed form *wen-w- in Germanic *winn(w)an, to seek to gain, in Old English winnan, to win: WIN}. 2. Suffixed zero-grade form *wn-ydé in Germanic *wunjé in Old English wynn, wen, pleasure, joy: WEN2, WINSOME. 3. Suffixed (stative) zero-grade form *wn-é-, to be contented, in Germanic *wunén in Old English wunian, to become accustomed to, dwell: won!, (wont). 4. Suffixed (causative) o-grade form *won-eyo- in Germanic *wanjan in Old English wenian, to accustom, train, wean: WEAN}. 5. Germanic *wéniz, hope, with denominative *wénjan, to hope, in Old English wénan, to expect, imagine, think: WEEN. 6. Suffixed zero-grade form *wn-sko- in Germanic *wunsk- in Old English wyscan, to desire, wish: WISH. 7. O-grade *won- perhaps in Germanic *wani- in: a. Old Norse Vanir, the Vanir: VANIR; b. Old Norse vana- in Vanadis, name of the goddess Freya: VANADIUM 8. Suf- f
---
VENERY :: ove (> venerari, to worship): VENERATE, VENEREAL, VENERY!, VENUS; b. suffixed form *wen-es-no- in Latin venénum, love potion, poison: VENOM. 9. Suffixed form *wen-eto-, “be- loved,” possibly in Germanic *Weneda-, a Slavic people, in Old High German Winida, the Wends: WEND. 10, Suffixed form “wen-yd@ in Latin venia, favor, forgive- ness: VENIAL. 11. Lengthened-grade form *wén-d- in Latin véndri, to hunt: VENATIC, VENERY2, VENISON. 12. Suffixed basic form *wen-o- in Sanskrit vanam, forest: WANDEROO. 13. Possibly zero-grade suffixed form *wn-ig- in Sanskrit vanik, vdnijah, merchant (? < “seek- ing to gain”): BANIAN. [Pok. 1. ven- 1146.] wen-2. To beat, wound. 1. Suffixed zero-grade form wer-3 *wn-to- in Germanic *wundaz in Old English wund, a wound: WOUND!. 2. Suffixed o-grade form *won-yo- in Germanic *wanja-, a swelling, in Old English wen(n), wen{n), wen: WENI. [In Pok. 1. ué- 1108.] wendh-. To turn, wind, weave. 1. Germanic *windan, to
---
uen- :: c *duniz in Old English dyne, noise: DIN. [Pok. dhuen- 277.] dhwene-. To disappear, die. Suffixed zero-grade form dhwna-tos in Greek thanatos, death: THANATOS; EUTHA- NASIA, TANSY. [In Pok. 4. dheu- 261.] dhwer-. Door, doorway (usually in plural). Originally an apophonic noun *dhwor-, *dhur-, in the plural, designat- ing the entrance to the enclosure (*dhwor-o-) surround- ing the house proper. 1. Zero-grade form *dhur- in suffixed forms *dhur-ns (accusative plural) and *dhur-o- (neuter) respectively in Germanic *durunz and *duram in Old English duru, door (feminine, originally plural), and dor, door (neuter): DooR. 2. Suffixed o-grade form dwo- *dhwor-dns (accusative plural) in Latin fords, (toward) out of doors, outside: FOREIGN. 3. Suffixed o-grade form *dhwor-ois (locative plural) in Latin foris, (being) out of doors: FOREST; (AFFOREST), FAUBOURG, FORECLOSE, FORFEIT. 4, Suffixed o-grade form *dhwor-o- in Latin forum, marketplace (ori
---
uedh- ::  desolate): WASTE; DEVASTATE. [Pok. 1. eu- 345.] euedh-. Udder. 1. Suffixed zero-grade form *idh-r in Germanic *ddr- in Old English adder, udder: UDDER. 2. Suffixed o-grade form *oudh-r in Latin dber, “breast,” with derivative adjective aber, fertile: (EXUBERANT), EXUBERATE. [Pok. éudh- 347.] euk-. To become accustomed. Zero-grade form *uk- in: a. suffixed (feminine) form *uk-sor- in Latin uxor, wife (< “she who gets accustomed to the new household” after patrilocal marriage): UXORIAL, UXORIOUS; UXORICIDE; b. nasalized form *u-n-k- in Old Irish to-ucc, to under- stand, “get accustomed to” (> Irish Gaelic tuigim, I understand): Tw1G2. [Pok. euk- 347.] eus-. To burn. 1. Latin drere, to burn: UREDO; ADUST, COMBUSTION. 2. Zero-grade form *us- in: Germanic *uzj6n, to burn, in compound *aim-uzj6n-, ashes (*aim-, ashes, ember), in Old English @merge, ember: EMBER. 3. Possibly in the non-Greek source of Greek Euros, the east wind: Eurus. [Pok. 
---
```


## [2026-10-17T00:03:47.773Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt').read()\nfor pat in [r'wedh-2', r'Pok\\. 2\\. uedh', r'2\\. uedh']:\n    for m in re.finditer(pat,t):\n        print(pat, '::', t[max(0,m.start()-500):m.start()+60].replace('\\n',' '));print('---')\nEOF\ngrep -n -i \"^ *wen-\\|^ *wep-\\|^ *wedh-\\|^ *wen\\b\" IEC.txt | head -20"
}
```


### [2026-10-17T00:03:48.340Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:03:51.203Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *[uw]en[ōoā]\\|^ *[uw]enos\\|^ *[uw]ed[hʰ]\\|^ *[uw]epr\\|^ *[uw]ep[oō]\\|venus\\|vapati\\|vafra\" IEC.txt | head -30"
}
```


### [2026-10-17T00:03:51.620Z] TOOL RESULT

```
19625:uabhlos, uabhros ‘unsteady, fickle, variable” Lat. vaber, f: vabra; dial. vafer, vafra ‘shifty, crafty’; G wabern and wábern, v. ‘flap, flicker, flutter; OE wzeflian, v. ‘twaddle, *waffle'^; ON vafla, v. ‘sway, wobble’ beside vafra, v. “hover; wander’. (NB. For E waver, OE waefre *unsteady', see uoip- (1)). Cf. also Fris. waf- felje, v. 'gibber'; Du. waffelen, id.; hou je waf- fel! “hold your tongue"
19800:uedh- (1) “marry; marriage; bride, bridal. Cf. ufuédh- and WP I, 254 Skt. vadhüh, f. ‘bride’; Av. cf. vaóryo, adj. ‘marriageable’; Oss. cf. ár-wád, s. &bride-price'; W cf. dy-weddi, pl. -iau, mf. ‘marriage’; Li. vedýs, gs: védzZio, m. ‘bridegroom’; védes *married'; Latv. vedēji, mpl. ^wedding-guests of the bridegroom’; vedibas, fpl. ‘homing of the bride’; Gk. cf. n&thís, f. (spinster, fr. *ne- uedhi-); eitheos (bachelor, fr. a type *ne- ufuédh-, see ufuédh-); G cf. Wittum (confu- sion w. type uedm- and w. OHG widamo *widow's endowment. See uidheua)
19801:uedh- (2) “lead, bring, carry’. WP I, 254 Skt. vadhami, v. (“take home’. Infl. of uedh- (D, q.v); Av. vad-, v. tr. & intr. “lead; go’; Tokh. AB, cf. wày-, v. “lead”; Hitt. wedàmi, v. ‘carry, bring’; Olr. fedim, v. “lead, bring"; OCS vedo, vesti (and com. SLL v. tr. "lead, bring’; Li. vedü, vèsti, v. lead, guide; wage, carry on’; Latv. vedu, vest, v. “lead; travel’; OPr. cf. wedeis, 2sg. opt. ‘mayest lead"; prob. o-gde in Gk. oth-neios (stranger, newcomer’, cf. neu-)
19802:uedh- (3) “join, fit’. Cf. uedh- (1) OW E W gweddu, inf. ‘suit, fit, yoke’; gwedd, pl. au, f. ‘yoke’; gweddw, adj. (1) “fitting,
19814:uedh- (4) “fight Tokh. B wat. wet-, v. id.; weta, s. id.; Gk. cf. á-ethlon, n. (contest', fr. *sm-uedhlom); Hes. cf. éthon, gs: -ontos ‘striking’; (alleged) étho, v. tr. ‘strike’; Lat. cf. bellum, n. (war, fr. *dui-uedhlom) beside pro-ellium, n. (battle, fr. *pro-uedhlio-); Olr. cf. feidm, m. ‘effort’; Ger. cf. Wett- in Wett-streit (icontest'. Su. un- tics of R o-gde po-vodevàt' ‘wage war’)
19815:uedher- (uedhr-) ‘weather’. WP I, 222. Cf. auedhr- Skt. vadhar, n. ‘thunderbolt’; vadharyàmi, v. ‘hurl thunderbolts; OHG wétar, OE weder, ON veðr, n. “weather, wind, lower air, sky”; OCS vedrü, vedro, mn. (‘fine weather; heat- wave’, and com. Sl.);
19816:uedhlom, see uedh- (4)
19817:uedhris ‘castrated animal; wether’. WP I, 255 Skt. vádhrih, adj. (castrated'; m. ‘castrated animal’; Hes. ethrís, m. ‘wether’; OE weder, m. id. (but weóer, id. unrelated. See uetos, -es-); ON (ambig.) veðr, gs: veórs, m. ‘wether’
19988:nus’; venia, f. ‘pardon, grace’; cf. venustus, adj. ‘graceful, happy’; OBr. cf. er-guinit, s. (“passion”, fr. *per-°); Go. wëns, f. ‘hope’; wen- jan, v. id.; OS wānian, OE wēnan, OFris. wēna, ON vána, v. ‘hope, imagine’; Ger. wähnen, v. ‘fondly imagine’; Du. wanen, id.; cf. also MHG wan, sm., wæne, sf. ‘supposition, hope’; ON ván, pl. -ir, f. id.; væni, n. ‘outlook’; vænn, adj. ‘likely’; OS wānam, adv. ‘brilliantly’; wān- līko ‘beautifully’; Sw. vän, adj. ‘pleasant’; Li. vēnios, fpl. ‘strength’. (Isophonic: Latv. pa- vēnis ‘shade, shadow, shelter’)
20007:uenos, -es- ‘desire’. Cf. uén- (1) and WP I, 259 Skt. vanas, n. ‘loveliness’ beside vanā & vanih, f. id.; vanús, adj. ‘keen; loving’; Lat. Venus, gs: -eris, f. ‘Venus’; beside vinulus & vinnulus, adj. ‘dainty; wanton’; W gwên, pl. gwenau, f. “smile”, cf. Gweno, f. “evening star, Venus’; (z-gde in) OHG wunja, MHG wunne, wünne, f. (2) joy’; OE wynn, f. ‘delight’; cf. wyn-sum ‘winsome’. (FK:EWDS untenable: Wonne). See next
20184:uesnom (uosnom) ‘price’. Cf. ues- (1). WP I, 311 Skt. vasnám, n. id.; Oss. cf. wäi, s. ‘sale’; Hitt. cf. wesiya(s), s. ‘cost, price’; Arm. gin, gs: gno, s. id.; Lat. venum in — dare ‘sell’; venus, gs: -üs, m. ‘sale’; Umb. cf. (?) uestisia *JJibation'; OCS venjo, -iti, v. (1) "sell
```


## [2026-10-17T00:03:53.555Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 19980,19990p IEC.txt | cut -c1-900; grep -n \"uep-\\|uepr\" IEC.txt | head"
}
```


### [2026-10-17T00:03:54.221Z] TOOL RESULT

```
cf. werumata (queried: 'straps"); Icel. cf. vö- lundar, pl. ‘labyrinth’; Li. cf. velanas, m. ‘rol- ler, cylinder’. Cf. WP I, 298. The radical arises in Oss. wàrdin, pp. wärst, (1) roll,
uelumn- (2) “pull, téar, jerk; fleece’. Cf. uel- (4) and uelmn- Arm. geymn, gs: geyman, s. ‘fleece’; OLat. velümen, n. id. beside Class. Lat. vellümina ‘fleeces’; vellus, eris, n. id. The radical arises in Oss. wárdin, pp: wärst, v. (2) “full — cloth. See next
ueluó, ið (1) ‘twist, turn, bend, roll" Cf. uoluo, ulu-. WP I, 298 Arm. gelum, aor. geli, v. ‘twist, sprain’; Gk. eilümi, eilúð, eloo, eild, eillo, v. ‘roll, enve- lop’; Lat. volvo, ére, v. (turn, rol. Vowel ambig. Cf. uoluo); Umb. cf. amb-oltu! “let him turn round"; Ir. cf. fillim, v. “turn, bend? and MHG wëllen, pp: ge-wollen, v. (1) “roll, trun- dle’; OE wilian, v. “bind, connect’. (Isophone: W gwelw, adj. *pale")
ueluó, io (2) ‘snatch, pluck, rob’. Cf. uelso, and ueluo (1). Lat. ambig. Lat. vello, ére, v. id. (fr. *ueluo, *uelno or expressive *uello? For ueluo, see poluos above in relation to Lat. pullus); Aib. cf. vjel, aor: vola, v. ‘pluck, gather, garner’; Go. wilwan, sv. 3. ‘rob’; wilwa, m. ‘robber’; cf. (z-gde) wulwa, f. *robbery'; (o-gde in) Gk. oulé, f. ‘wool
uemoó, ið ‘vomit’. Onomat. WP I, 262 Skt. vàmami & vámimi, v. id.; Av. vam-, id.; Oss. wáàmin, pp: wámd, id.; Gk. eméo, emoü- mai, id.; Lat. vomo, ére, id.; Icel. (long-gde) væma, v. (“be il esp. in mig vaemir “I feel nausea); ON váma, f. ‘nausea’; Sw. vámjas, v.; Li. vemiü, vernti, v. vomit; Latv. vemju, vemt, id. (Isophonic extn. with long vowel in Skt. vàmalürah 'ant-hil?, and Li. vemalai, mpl. vomit)
(uemstr-, see Supt: U, and cf. uenter-)
uén- (1) “desire, hope, favour, outlook, charm'. Cf. WP I, 26, 298 & 301 Skt. vanih, f. “wish, desire’; vánas, n. ‘beauty’; vanüh ‘eager’; vanisthah “most favourable’; (*-é- in) vánih, f. ‘musical recital; vanáh, m. *musical instrument, music'; Av. vàunus, adj. ‘favourable’; Gk. cf. ap-énés “harsh, rough’; pros-enés ‘gentle, mild’; Lat. Venus, -eris *Ve-
1513
nus’; venia, f. ‘pardon, grace’; cf. venustus, adj. ‘graceful, happy’; OBr. cf. er-guinit, s. (“passion”, fr. *per-°); Go. wëns, f. ‘hope’; wen- jan, v. id.; OS wānian, OE wēnan, OFris. wēna, ON vána, v. ‘hope, imagine’; Ger. wähnen, v. ‘fondly imagine’; Du. wanen, id.; cf. also MHG wan, sm., wæne, sf. ‘supposition, hope’; ON ván, pl. -ir, f. id.; væni, n. ‘outlook’; vænn, adj. ‘likely’; OS wānam, adv. ‘brilliantly’; wān- līko ‘beautifully’; Sw. vän, adj. ‘pleasant’; Li. vēnios, fpl. ‘strength’. (Isophonic: Latv. pa- vēnis ‘shade, shadow, shelter’)
uën- (2) “lacking, defective, immature; lack’, etc. Cf. uän-. Gk. ambig. Hom. Cf. énis, gs: énios, adj. (immature, un- mated, virgin’ of heifer); LG Du. wàn-, wan-, cpds. *mis-; cf. G Wahn-sinn (infl. by Wahn, see uen- (1). Semantics of Lat. jünix fr. ieun-, q. v.). See Supt: U
uendh- (1) ‘turn’. WP I, 261. Cf. uondh-, undh- Skt. cf. vandhürabh, m. *chariot-seat'; Arm. cf. gind, gs: gndi, ab. s. -av, also gint, gs: gnti, s. (ring; gndak, dim. ‘tendri’; Tokh. AB wánt-, v. ‘wrap’; Gk. cf. peirins, gs: peírinthos, f. “wicker body of chariot if fr. *peri-uendh-); Umb. (queried) aha-uendu “let him turn aside’; Go. bi-windan, sv. 3. “wind, wrap’; MHG winden, winten (and com. Gmc.),id.; G & MHG Winde, winde, wf. *winder, spool, capstan, convolvulus'; OHG winta, f. id. (and “spiral staircase’); ON vinda, sv. 3. ‘wind’; f. ‘hank’; vindr, adj. fawry'; cf. vindli, m. ‘wisp’; Sw. vind, adj. ^warped'; OE windan, sv. 3. ‘wind’; wind, n. ‘wind, path, weave, textile’; Srb. (?) vedja, f. ‘eyebrow’. (A hapax arises in Ir. feann, s. *flaying, skinning’)
8499:(kuep- (kuuep-, kuép-) (redolent; vapour. See kuap-, kuip- Li. kvepiü, kvépti (smell', intr.); cf. kvépalai, mpl. ‘aromas’; Latv. kvepstu, kvept ‘smoke, get blackened'; kvēpi, mpl. 'soot
17977:suepo, ið (1) “be drowsy, sleep’; suopeio ‘tull’. WP II, 523 Skt. svápami, svápimi, v. ‘sleep’; Av. xwap-, v. id.; Per. xuftan, inf. beside xabam, xabidan, v. id.; (variant in) Per. xuspidan, Av. xwafs-, Oss. xüssin, inf. id. (fr. *sueps- or *suepsK-); Lat. sopiO, Ire, v. Cu fr. *suep-); OE swefan, sv. 5. “sleep; cease’; ON sofa, p. t. svaf, id.; Sw. sova, id.; cf. (o-gde) OHG swebjan, swebben, v. lul; ON (e-gde) svæfa, inf. id.
18156:suop- ‘sleep’; suópeio, ið “put to sleep’. See suep-, supnos Av. xwafno, adj. ‘sleeping, sleepy’; m. “sleep”; Ir. cf. sámhan, n. ‘nap’; Li. cf. (variant) sap- nas, m. ‘sleep’; Latv. sapnis, s. “dream; (*suep- in Lat. somnus ‘sleep’; somnium, n. ‘dream’; sopor "deen sleep; ON, OE svefn, swefn ‘sleep’; MHG swébe 'hovering"). Verbal types: Skt. svapáyàmi, v. ‘put to sleep’; Lat. sópio, ire, v. id.; ON soefa, v. 'kil; Sw. sóva, tr.
```


## [2026-10-17T00:03:58.380Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"vafra\\|barf\\b\" SYN.txt | head -5; grep -n \"venari\\|venor\\b\" SYN.txt | head -5; grep -n \"wyscan\\|wiscan\\|wunsc\" SYN.txt | head -3; grep -n \"vepres\" SYN.txt LAT.txt LEW_1910.txt | head -5"
}
```


### [2026-10-17T00:03:59.241Z] TOOL RESULT

```
2005:Grk.  xidy (vida poet.) Goth. snaiws Lith. snie, NG xtdve ON 8n@r (snjor, snjar) Lett. shee Lat. nix Dan.  sne ChSl.  snégit It. neve Sw. snd SCr.  snijeg Fy. neige OE snaw Boh. snth Sp. nieve ME snow Pol. — fnieg Rum. zdpadé NE snow Russ. sneg Ir. snechte Du. Sneeuw Skt. hima- Nir. sneachta OHG  snéo Ay. vafra- W. etra (nyf) MHG nz ;
2027:Slavic o-(na-)metati ‘heap up’, hence ‘heap of snow, snow’. Tiktin 1032, 1088. 4. W. eira, Corn. er, Br. erc’h : Ir. arg ‘drop’, Lat. spargere ‘strew, sprinkle’, etc. Walde-P. 2.674. Pedersen 1.104. 5. Av. vafra-, rare but confirmed by
2028:Pahl. vafr, NPers. barf ‘snow’, etym.? Barth. 1347.
22756:6. Skt. gabhira-, gambhira-, Av. fafra- (and jaiwa- in jaiwa-vafra- ‘with deep snow’), beside Skt. gambhan- ‘depth’, Av. jafnu- ‘depression’, perh. : Grk. Barrw ‘dip, dye’, Bay ‘dipping, dye’; ON kvefja ‘submerge, overwhelm’, intr. ‘be swamped, sink’, OSw. kvaf ‘depth of
27897:& fr. ‘bright’. Walde- ‘joyful a 324. NED s.v. at: ¢, Falk-Torp o ME blisse (but the as in NE bliss, in- fr. adj. es 7c . NED 8.V.), : og oa Goyful’, ME, NE blithe pe ‘kD ; MHG blide, ae rahe vet? Goth. bleips “mercitul, tov~ bly 1 mY blidr ‘gentle, pleas- dub., perh. through . OE bléo vio, Walde-P. 2.210. Falk-Torp 81. OE wynn, ME wunne, winne (cf. ne winsome), OHG wunna ‘sreat joy, bliss (NHG wonne) : Lat. venus ‘charm’ (and Venus), Skt. van- ‘desire, seek, gain’, Goth. wens ‘hope’, OHG wunscan, OK wyscan ‘wish’, etc. Walde-P. 1.258. OHG frewi, frewida, MHG vréude, NHG freude, Du. vreugde (Dan. fryd, Sw. frojd, sense prob. influenced by German; ON frygo ‘bloom, magnificence’), fr. adj. OHG jré (inflected frawer, etc.), MHG wo, NHG froh joyful, glad’, in OHG also ‘swift? as ON frar, this prob. the earlier meaning, hence perh. : Skt. pru- ‘spring up’, prava- ‘hovering’, Russ. pryt’ ‘swift pace’, etc. Walde-P. 2.88. Weigand-H. oe Somewhat otherwise formally ut much the same semantically (as ne forward moving’ Gme. *frawa- = 3 Bi Pw0-) Falk-Torp 278. <i NE joy, fr. Fr. joie (above, 2). G mendt, MEG mende, with vb. :OHG muntar ‘eager, unter), Goth. mundon ’, Lith. mandras ‘live- » Grk, avbave ‘ ? Havbavw ‘learn’, etc. a - Feist 367. 8 : Sire’ (6.63) me aad OE lust, ete. ‘de- in OF (cf. NED
28071:Lat. venus ‘love, charm’ (but com- mon only in the personified Venus) § Skt. van- ‘seek, desire, gain’, Goth. wens ‘hope’, OF wyn, OHG wunna ea , bliss’, OHG wunscan, OF wyscan, = - ‘wish’ (16.61). Walde-P. 1.2588. ** nout-M. 1037.
29224:1160 SELECTED INDO-EUROPEAN SYNONYMS 16.61 WILL, WISH (vb.) Grk. (é)8éAw, BobrAopat Goth. wiljan Lith.  noréti NG 6aw ON vilja, eskja Lett.  gribat (vélet) Lat. __velle Dan. ville, énske ChSl. chotéli, chits; It. volere Sw. vilja, 6nska SCr.  htjeti Fr. vouloir OE willan, wijscan Boh.  chtéti Sp. querer ME _ wille, wisshe Pol. cheiéé Rum. voi, vrea NE will, wish, want Russ. chotet’ Ir. dithraccar Du. willen, wenschen Skt. vag-, i3- NIr. toil (in phrases) OHG  wellen, wunscen Av. vas-, i§- W. ewyllysio, mynnu MHG wellen, wollen, wiin- Br. mennout, yoult schen NHG_ wollen, wiinschen The words listed are the most com- | delAouar, 84 Aopuar, Bée\Nonar, etc., all
```


## [2026-10-17T00:04:03.313Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"HUNT\\b\\|venari\\|vénari\\|vendri\" SYN.txt | head -5; grep -n \"vepres\" LAT.txt LEW_1910.txt | head; grep -n \"^venor\\|^Venus\\|^venus\\|^vēnor\\|^veneror\" LAT.txt LEW_1910.txt | head"
}
```


### [2026-10-17T00:04:03.656Z] TOOL RESULT

```
5064:3.79. HUNT (vb.)
LAT.txt:4539:Venus; cf. les references de Goetz-Schoell ad loc. Quelquefois aussi
LAT.txt:33639:Venus Libentina et Libitina avec les t 4 moignages citds par Goetz-SchoeJl
LAT.txt:63287:Venus,-eris, mais 1 1 w ne s'explique pas, et c 1 est le seul exemple
LAT.txt:67309:Venus, -eris f.: 1' 1 1 amour, 1 'acte amoureux, 1 'objet aim» 5 ; 3° per-
LAT.txt:67323:Venus"; ueneria f. (sc. concha): sorte de coquillage (Plin.^ M.L.919G;
```


## [2026-10-17T00:04:06.181Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5064,5090p SYN.txt | grep -n -i \"venari\\|vēnārī\\|venor\\|Walde\\|Lat\\.\" | head; sed -n 67300,67345p LAT.txt | cut -c1-200; grep -n \"^ *uepr\\|^ *uepr[eē]s\\|uepres\" LAT.txt | head"
}
```


### [2026-10-17T00:04:06.535Z] TOOL RESULT

```
4:Téw, Kunyew ON veida Lett... medit NG Kun Dan. jage ChSl.  loviti Lat. —_vénairi, sectart Sw. jaga SCr. _loviti It. cacciare OE huntian, wepan Boh.  loviti Ty. chasser ME _hunte Pol. —_ polowaé Sp. cazar, montear NE hunt Russ. ocholit'sja Rum. vina Du. —jagen Skt.  mrgaya- Tr. adclaidim OHG  weidon, jagon Av. soatte Nir. fiadhachaim MHG jagen W. hela NHG jagen
11:2, Lat. vénadrt (> Rum. vina), prob. (with grade *wén- beside *wen-) : Skt. van- ‘seek, desire’, OE winnan ‘strive, fight’, etc. Walde-P. 1.230. Ernout-M. 1085.
12:Lat. sectart ‘follow, pursue’ also used for ‘hunt’ animals, fr. *sectus, old pple. of sequi ‘follow’ (10.52).
14:Fr. chasser, Sp. cazar fr. for Lat. captare ‘try to
19:W. hela, Br. hemolc’hi (for holc’hi), with Ir. selg ‘hunt’ (sb.) : Skt. srj- ‘loose, emit, shoot’. Semantic de- yelopment in Celtic through loosing the hunting dogs (cf. Skt. srjatt. cgunas). Walde-P. 2.508. Pedersen 1.106.
21:4, ON veida, OE we&pan (with nouns for ‘the hunt’ ON veidr, OF wap), OHG weidon (also ‘pasture’, NHG wevden, 3.15), fr. an extension of *we7- in Lith. veju, vyti ‘pursue’, Skt. veti ‘seeks, fol- lows’, Av. vayeiti ‘pursues’, etc. Walde- P. 1.230. Falk-Torp 1361 f.
27:Goth. fra-hinpan ‘capture’, Sw. hinna ‘reach’, wpphinna ‘overtake’ (10.54) fr. parallel root forms (*ken-d-, *ken-t-?), but outside connections dub. Walde-P. 1.460. Feist 161. NED s.v. hunt. OHG jagon, MHG, NHG jagen (> Dan. jage, Sw. jaga), Du. jagen, etym. dub., but perh.: Skt. yahu-, yahva- ‘restless, active, swift’, (pra-)yaks- ‘has- ten, press on’, Grk. txavdw ‘desire’, etc. Walde-P. 1.195f. Weigand-H. 1.940.
souvent pl.gtnfe , gnoc ) "prix d'achat, valeur" (d'ou gnen "j'achete").
L'0) de hom.oovoc "prix d'achat", att. tovT] "achat, prix d^chat", suppose
un ancien *o; mais lesb.ovva repose sur *wosnd. On ne saurait dire
si lat. uenum repose sur *wesno- ou sur *wesno-', on pourrait meme
penser a une forne sans -s- si 1 1 on rapproche v.sl. veno "prix de
la fiancee, dot". Le hittite a ussaniya "vendre" et v>as- "acheter",
celui-ci sans le suffixe -no-.
L'usage fait de uenum, ueno est parallele a celui du supin, comme
1 'indique le uenui d'Apulee. Cf. 1 'infinitif osco-ombrien en -un.
Venus, -eris f.: 1' 1 1 amour, 1 'acte amoureux, 1 'objet aim» 5 ; 3° per-
sonnifie et divinise, Venus, deesse de 1 'Amour et "Venus" planete;
3° qualites qui excitent 1'amour, grace, seduction, charme; 4 0 au jeu
de d^s, le coup de Venus.
Par sa forme, Venus est un ancien theme neutre en -os/-es (d'ou
sans doute uenenun). Designant une deesse, correspondant a 1 ’ Acppo 5 l/Tri
grecque, et, ainsi con<;u, a le genre feminin. Cf. Te Ilus, Cupido.
Usite de tout temps. Conserve en roman et en britt. surtout dans
ueneris dies, M.L.9197; britt. gwener.
Derives: uenustus (cf. onus/onustus): qui excite 1 'amour, d'oil "char-
mant, s^duisant", etc.; uenuste ; uenustas (cf .honestus, honestas)',
uenustulus, diminutif d'affection, uenusto, -ds "parer, embellir"
(Naev. et Ambr.); inuenustus', deuenusto (Geli.); uenereus {uenerius) :
de Venus; d'ou uenereus m. (sc. iactus) ou uenereun n. "le coup de
Venus"; ueneria f. (sc. concha): sorte de coquillage (Plin.^ M.L.919G;
uenereun labrum "cardaire", etc.; ueneriuagus.
Pour la forme, lat.wenus repond a ved.vdnas-, atteste une fois
dans un instrumental vdnasa d'un texte v^dique qui ne suffit pas
a garantir 1'antiquite d'un vanas- isole, et surtout dans le compose
gir-vanas- "aimant les hymnes" (epithbte des dieux), et aussi yajnd-
vanas- "aimant les sacrifices".
L'emploi d'un nom de la forme de uenus pour indiquer une puissance
de caractbre divin est exceptionnel. II 8'explique en partie par
ceci que le type a vocalisme -o- a pris en latin la valeur d'un pur
abstrait, de genre masculin, dans le type tepor, si bien que le nom
de l M, aurore" a du recevoir un ^largissement, d'ou aurora.
La racine a laquelle appartient uenus a fourni de nombreuses formes
dont les sens sont aberrants au premier abord. Parmi les plus proches
de uenus, on peut citer skr.vdnchati "il desire" et v.h.a.w unskan
"desirer" - got.umounands "ne se souciant pas de"; v.h.a .wunna, wunnl
"grande joie", dont la forme rappelle celle de lat. uenia. - En latin,
y.ueneror (ou, comme dans uenus, apparait 1'emploi de la racine a des
fins religieuses), uenenun, uenia, uenor.
uepres, -ium m. et f.pl.: buisson d’epine. Usit 4 ordinairement
au pluriel, quoique le sg. soit atteste dans la 1. imperiale (Ov.,
Coi., Plin.); aussi la forme de nom.sg. est-elle peu Sure: uepres,
uepris et meme ueper.1377
67342:uepres, -ium m. et f.pl.: buisson d’epine. Usit 4 ordinairement
67344:Coi., Plin.); aussi la forme de nom.sg. est-elle peu Sure: uepres,
67345:uepris et meme ueper.1377
```


## [2026-10-17T00:04:08.665Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 67346,67352p LAT.txt; grep -n \"^uenor\\|^ *uenor, \\|^uenenum\\|^ *uenenum\" LAT.txt | head; "
}
```


### [2026-10-17T00:04:09.112Z] TOOL RESULT

```
uerbera
Derivas: uepretum ; uepraticus (Coi.).; ueprecula.
Sans etymologie.
ugr, uSris n.: printemps; printemps de la vie (Cat., Ov.); pro-
ductions du printemps, cf. uer sacrum. tJsite de tout temps. M.L.9313;
beaucoup de formes romanes remontent a. primum uer (cf. primum tempus),
cf. Caton, Agr.S 0 , prata primo uere stercerato luna silenti', et dans
```


## [2026-10-17T00:04:12.975Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"wafr\\b\\|wafr \\|wʾpl\\|wTpl\\|wapl\" PHD.txt PHD_mackenzie.txt | head -5; grep -n -i \"vafr\\b\\|wafr\\b\" NYB_vol2_glossary.txt NYB.txt | head -5; grep -n \"barf\\b\" HRN.txt HUB.txt | head -8"
}
```


### [2026-10-17T00:04:13.347Z] TOOL RESULT

```
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:3714:snow snéxr, snézag, wafr.
PHD.txt:5145:wafr
PHD.txt:5146:nifrin wafrūnag nifrīdag Obad-/oft-1 Obastan! nibard- nibardīdan nibard nibardag nibastan wabz wafišn xwest xwestant nibistan 1-2paft waz- wizār wizür- wizarisn wizārdan wizārdwars wizīh-
PHD_mackenzie.txt:5136:wafr [wpll M wpr, N barf] snow.
NYB_vol2_glossary.txt:3906:vafr [wpl] snow 97%. — Av. (1347) vafra-; MPrthPrs wfr (S, MHC); NP barf.
NYB_vol2_glossary.txt:5415:vafra-: vafr
NYB_vol2_glossary.txt:6163:wfr: vafr
NYB_vol2_glossary.txt:7047:barf: vafr
HUB.txt:5456:= phi. vartak, zd. vareta-; barf 'Schnee' = paz. vafr Min.
HUB.txt:6568:laut = rf {barf *Schnee' = zd. vafra-), siehe Kap. 32.
HUB.txt:9540:c) Ap. /r ~ np. rf: barf *Schnee* = phi. i;a/*r = zd. y«/n/- ;
```


## [2026-10-17T00:04:15.994Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Schnee\" HRN.txt | head -5; grep -n \"برف\" incoming/ARY/ARY_pages.txt | head -5; grep -n \"^برف\\|برف  \\|برف ـ\\|برف[ .:]\" BQT_v1_pages.txt | head -8"
}
```


### [2026-10-17T00:04:16.460Z] TOOL RESULT

```
2163:202. &^r/ 'Schnee.
2165:aw. vafra- 'Schnee'; phlv. vafr.
2167:vävra 'Schneeflocke*, Plur. 'Schnee'; bei. LW. harpi
5880:jiun 'Schnee', jmern 'Winter', jmerem 'überwintern
5884:si/n. zimjy zinj 'Schnee'.
3587:ضمناً در زبان‌های اوستایی ((881۸0711۸) و پهلری (5۸:8708 (96۸0) چم "برف" را داشته‌اند و ممکن است
9589:ی , چم واژه‌ی در زبان ارملی؛ برف,
952:تورنان1۵۶۷۵۳ ۱ ) -18 (دیدن)» - 50816 (برف باریدن)- 988
1497:جزاز برف وشیرش نبودی خورض فزو نیش روغن بدی پرورش ۱ .
1498:خورش ساختن از برف وشیر چه معنی دارد ۲ صحیح < ترف > است
4161:برف » بستن » بسیار» بلیل » بنده» بنیاد وغیره.
4933:برف ( فارسی ) ۵۸6
15048:برف
18751:است که آب برف و آب سرد باشد - و کنابه
18762:برفره - بر وزن شه‌تره ۰ بمعنی برقر
```


## [2026-10-17T00:04:19.296Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2160,2170p HRN.txt; sed -n 15040,15056p BQT_v1_pages.txt; awk 'NR<=15048 && /\\[pdf page/{p=$0} END{}; NR==15048{print p}' BQT_v1_pages.txt; sed -n 3580,3592p incoming/ARY/ARY_pages.txt; awk 'NR<=3587 && /\\[pdf page/{p=$0} NR==3587{print p}' incoming/ARY/ARY_pages.txt"
}
```


### [2026-10-17T00:04:19.883Z] TOOL RESULT

```
rösten'; af;\ writ geröstet', wrat-Sddl 'rösten'; bei.
brijag , brejag 'backen , rösten (39) ; wsi/, waresam,
sar. wirzam.
202. &^r/ 'Schnee.
g. mäz. gel. Ka§. varf^ verf.
aw. vafra- 'Schnee'; phlv. vafr.
kurd. vafr (H.-Sch.), befir, bafer, berf (LW.); af>.
vävra 'Schneeflocke*, Plur. 'Schnee'; bei. LW. harpi
sangl. varf, min], värfa,
203. hery 'Blatt'.
g. niaz. varak; gel. velg, valk; Käö. valg^ velg\ (vergl.
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
چم و وه دج مان ک و هی مه من مب اب نم مها ما عحکردن باشد و آلرا بعربی جارت خوانند که
کتاخی باشد ؟ .
اوستاك » بر وزن نوشباد ۰ داننده

اسلاوی کهن (۲12ما5 تلع#تانط صام): 288 :۸000
۷۱ برهان قاطع : ۳۹۵۹ ۰
1
[pdf page 123]
۹ ی
۱ ۴ / برگ
بادداشت:
ضمناً در زبان‌های اوستایی ((881۸0711۸) و پهلری (5۸:8708 (96۸0) چم "برف" را داشته‌اند و ممکن است
۱ امروزه هم در گویش‌های محلی فلات ایران وجود داشته باشند. شاخه گیری این واژه‌ها چنین است:
: هسند و اروپایی: 881161713* -۱۳887010۷717 سانسکریت(پرا کریت): 5187311۸ او سناین:ها۸013 یی
۱ 2۸ بوتانی: ۹3۷1۳13۸ لانین: ۸۷1 ,8۷۲۷18 انگلیسی کهن: 824817 (انگلیسی: 8801#۷)؛ آلسانی کم ۳*۰
0 (آلمانی: 5 فریزی کهن: )58؛ ساکسونی کهن: 8۸۷80 ایسلندی کهن: 15۸1۸14 گوتیکه:
5 ایرلندی کهن: 53150177۸0: لیستراننی: 15۸۷126۸8 اسلاوی کهن: ۹831861 پروسی کهن:
[pdf page 123]
```


## [2026-10-17T00:04:24.886Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3555,3580p incoming/ARY/ARY_pages.txt; grep -n \"BARF\\|BARP\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:04:25.207Z] TOOL RESULT

```
۹ اا ‏ نگ ی
برشتن» بریان / ۱۳۲۳
پهلری (۸1ات۸ط): لا نی ۱:۹ لهستانی (877ق۳0): هد بای ۱:1۹
نانک انا روسی (ف95لا#): امن نی دا
کردی (00/5): بان لیتوانی (/۵ا(۸نا7): کشآ2ع813
افغانی (پشتو)(//۵26017۸۸): ,۷7817۸۷/7 نوی (لتی) (471401ل): ,816۸
سانسکریت (6/۸/۶88/7): 811877۸7 پروسی کهن (/لفا55ن2۳ صا0): 81360(ناه
نا کی رانا برتونی (8070/1): 3817۸
یونانی 028/0): ۳118100 ,۲11856710 ۱
لاتین (4710ا): ,185 ,7100 پسگشت‌ها یت تا
اد 7 20000
فرانسه (/(۳3): 8 ,۲818 42 (۲8) درآ میت 1
آسپانبایی (8۳۸(۷/3): اد دا 1 (8۵۸۶) :1/۸20/218 ِ
ایتالیایی (۸4(4ال7۸/): ات اد نان دا 33339 لاه أ
روانی (/(44/4(): آل8۸ ,۲8165 9 (۲83) :0/05 ۱
پرتغالی (۳071701285): ۳1 8 (۲8) : +37 ۱
انگلیسی میانه (باعلا8(/0 قاط0ر4م: 8 (۲89) 00
5 و7812 برهان قاطع + ۵۸
ی دورو رو
خی اوستایی :(4887424): ۷۸۸ لتونی (لتی) (477۵۸ا): ناد دیا
پهلو ی*(1ماَمع): ظ ۰ ۷۹
کردی (7ل2//5): زد دز پسگشت‌ها شید دا
افقانی (پشتو) (4۳017۸۷7): ه۷18 9 و2
سانسکریت (5۸(786/7): ۷۸28۸ ,۷۸۳۸31 3 (830۷) اد ماد 1
لاتین (4712سا): ند راد 6869 8
اسلاوی کهن (۲12ما5 تلع#تانط صام): 288 :۸000
```


## [2026-10-17T00:04:30.388Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls data/verification/sources/refs/ocr/ARY/ 2>/dev/null | grep -i \"12[234]\"; timeout 300 python3 tools/ref_page.py ARY:124 --image 2>&1 | tail -15"
}
```


### [2026-10-17T00:04:42.564Z] TOOL RESULT

```
‎LAPAS ALITHUANIAN) ‏لیترانی‎ PHLLON AGREEK) gLy
BILE, BLATH :(OLD IRISH) ‏ایرلندی کهن‎ FOLIUM (LATIN) ‏لاتین‎
‎BLAWD «(GAULIsH) ‏گالی‎ FEVILLE AFRENCH) ‏فرانسه‎
‎FOGLIA AITALIAN) ‏ایتالیابی‎
‎REFERENCES ‏پسگشت‌ها‎ LAUFS HGOTHIC) &5 5
POKORNY: 1212 :(OLD SCANDINAVIAN) ‏ایسلند یکهن‎
(BLADE) 97, (FOLIAGE) BLADH
BARNHART: 397 BLATH :(OLD NORSE) ‏نورس کهن‎
DELAMARRE: (FEVILLE) 156 BLAD :(OLD SAXON) ‏ساکسونی کهن‎
MACKENZIE: (LEAF) 121 BLED A(OLD FRISIAN) ‏فریزی کهن‎
‏لاه‎ (LEAF) 525 {(OLD HIGH GERMAN) ‏آلمانی کهن‎
SKEAT: (FOLIAGE) 220 BLUOT, BLAT
AMINDAROV: (LEAF) 248 BLATT :(GERMAN) ‏آلمانی‎
‎۳۶۰ + ‏برهان قاطم‎ BLAD :(OLD ENGLISH) ‏انگلیسی کهن‎
```


## [2026-10-17T00:04:44.122Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py ARY:124 --image 2>&1 | head -60"
}
```


### [2026-10-17T00:04:44.551Z] TOOL RESULT

```
(no exact page map; using offset -1 -> pdf page 123; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/0124.png
REF: ARY:124  PDF: data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf page 123  OCR-lang: fas+eng

R ۹)
‏برگ‎ ۴ ۱
‏یادداشت:‎ ۱
‏چم "برف" را داشته‌اند و ممکن است‎ (SNEZAG, SNEXR) ‏و پهلوی‎ SNAOTHA)) ‏ضمناً در زبان‌های اوستایی‎ ,
‏امروزه هم در گویش‌های محلی فلات ایران وجود داشته باشند. شاخه گیری این واژه‌ها چنین است:‎ :
‏او سای 0711۸ 9۸پ‎ SINEHA ‏سانسکریت(پراکریت):‎ *SNOIGWH- *SNIGWH ‏هسند و اروپایی:‎ ;
T ‏آلمانی کهد:‎ (SNOW ‏(انگلیسی:‎ SNAW ‏انگلیسی کهن:‎ ۸۷1۷18, NIX ‏لاتین:‎ (NIPHA ‏یونانی:‎ ۷8252۸
‏گوتیکه:‎ SNAR ‏ایسلندی کهن:‎ SNEO ‏ساکسونی کهن:‎ SNE ‏فریزی کهن:‎ (SHNEE ‏(آلمانی:‎ SNEO
‏پروسی کهن:‎ SNEGU ‏اسلاوی کهن:‎ SNIEGAS ‏لیستوانی:‎ SNECHTAE ‏ایرلندی کهن:‎ 5
‏لهستانی:‎ SNEF ‏روسی:‎ SNE ‏دانمارکی:‎ SNO ‏نروژی‎ SNO ‏سوئدی:‎ SNEEUW ‏ملندی:‎ 58
SNIH ‏پوهمی:‎ (NEVE ‏ایتالیابی:‎ (NIEVE ‏اسپانیایی:‎ (NEIGE ‏فرانسه:‎ 6
۵۸7 eS|
BLADE A(ENGLISH) ‏انگلیسی‎ VAREKA AAVESTAN) ‏اوستابی‎
‎BLAD {DANISH) ‏دانمارکی‎ WARG, VALG {(PAHLAVD) ‏پهلوی‎
‎BLAD HSWEDISH) ‏سوئدی‎ BELG, BELCHIM,  :(KURDISH) ‏کردی‎
‎BLAD :(NORWEGIAN) ‏نروژی‎ BERU ۱
BLAD :(bUTCH) ‏هلندی‎ PALT {(TOKHARIAN A) A ‏تخاری‎
‎LAPAS ALITHUANIAN) ‏لیترانی‎ PHLLON AGREEK) gLy
BILE, BLATH :(OLD IRISH) ‏ایرلندی کهن‎ FOLIUM (LATIN) ‏لاتین‎
‎BLAWD «(GAULIsH) ‏گالی‎ FEVILLE AFRENCH) ‏فرانسه‎
‎FOGLIA AITALIAN) ‏ایتالیابی‎
‎REFERENCES ‏پسگشت‌ها‎ LAUFS HGOTHIC) &5 5
POKORNY: 1212 :(OLD SCANDINAVIAN) ‏ایسلند یکهن‎
(BLADE) 97, (FOLIAGE) BLADH
BARNHART: 397 BLATH :(OLD NORSE) ‏نورس کهن‎
DELAMARRE: (FEVILLE) 156 BLAD :(OLD SAXON) ‏ساکسونی کهن‎
MACKENZIE: (LEAF) 121 BLED A(OLD FRISIAN) ‏فریزی کهن‎
‏لاه‎ (LEAF) 525 {(OLD HIGH GERMAN) ‏آلمانی کهن‎
SKEAT: (FOLIAGE) 220 BLUOT, BLAT
AMINDAROV: (LEAF) 248 BLATT :(GERMAN) ‏آلمانی‎
‎۳۶۰ + ‏برهان قاطم‎ BLAD :(OLD ENGLISH) ‏انگلیسی کهن‎
```


## [2026-10-17T00:04:47.224Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py ARY:123 --image 2>&1 | head -60"
}
```


### [2026-10-17T00:04:56.113Z] TOOL RESULT

```
(no exact page map; using offset -1 -> pdf page 122; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/0123.png
REF: ARY:123  PDF: data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf page 122  OCR-lang: fas+eng

اه ‎e‏ و
برشتن» بریان / ۱۳۲۳
پهلوی ‎BARSTAN, {(PAHLAVI)‏ لهستانی ‎BARGIEL (POLISH)‏
‎BHURAJANTA‏ روسی ‎BERGLEZU A(RUSSIAN)‏
کردی ‎BIRASHTIN {KURDISH)‏ لیتوانی ‎BIRGELAS (LITHUANIAN)‏
اففانی (پشتو)(//4۳0/7۸۸): ۰ ‎VRETAWEL‏ لنونی (لتی) ‎BIRGA, {LATVIAN)‏
سانسکریت ‎BHRJJATL +(SANSKRIT)‏ پروسی کهن ‎(AU)BIRGO :(OLD PRISSIAN)‏
‎FRITA :(BRETON) 5 » BHURAJANTA‏
بونانی ‎PHRYGEIN, PHRUGO :(GREEK)‏ ۱
لائین ‎(LATIN)‏ ,78100 پسگشت‌ها ‎REFERENCES‏
‎FERTUM‏ رک 0 ۳۳
فرانسه ‎BARNHART: (FRY) 412 FRIRE, FRITE :(FRENCH)‏ ' ۱
اسپانبایی ‎L MACKENZIE: (ROAST) 131 FREIR A(SPANISH)‏
ایتالیایی ‎BUCK: 336-339 FRIGGERE J(ITALIAN)‏ ۱
رومائی ‎ONIONS: (FRY) 9 FRIGE, FRAJL  (RUMANIAN)‏ :
پرتغالی ‎SKEAT: ۱ (FRY) 228 FRIGIR :(PORTUGUESE)‏ ‘
انگلیسی میانه ‎AMINOAROV: (FRY) 228 :(MIDDLE ENGLISH)‏
‎FRIEN, FRYE‏ برهان قاطع : ۳۵۸
@
% اوستایی ‎VEPRIS JLATVIAN) () 45 VAERA JAVESTAN)‏
پهلو ی( اتمه): ‎VAFR o‏
کردی ‎BERF :(KURDISH)‏ پسگشت‌ها ‎REFERENCES‏
‏افغائی (پشتو ) ‎POKORNY:  11# WAWRA {AFGHAND)‏
سانسکریت ‎MACKENZIE: (SNOW) 133 VAPATI, VAPRA :(SANSKRIT)‏
لاتین ‎‘BUCK: 68-69 VEPRES {LATIN)‏
اسلاوی کهن ‎AMINDAROV: 288 +(OLD CHURCH SLAVIC)‏
‎VEPRU‏ برهان قاطع : رد :
‎e‏
```


## [2026-10-17T00:05:00.032Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"wfr\\b\\|wfr \\|wpr \" SOD_pages.txt | head; grep -n -i \"snow\" SOD_pages.txt | head"
}
```


### [2026-10-17T00:05:00.390Z] TOOL RESULT

```
13152:                                                                             3301 cwpr                     (u>>>^- jj)j'><^<^'jf
30725:      Ashoka                                                      9368 -swpr M
32368:                                                                   wafra    ©Av. vafra    ©f. n. -hP =»wfr»
32492:       STi 54.16; GMS 60n 1; wlrz-, STii 2.1                            9980 wfr' M
42939:                        A<lV\iA<*M           .>>>^     *n»Y*r*WiYnf       iWawwfr                ^
43257:<w\<v*fr<v<irv<wfr<w^                  j^^          <x*rhA\\bA\\r A*rxA*r\ jlJj^
44497:                VAY^VA^wvr^wfr                                                                                                        ^YY.A^VY           v>-^
3144: /casm/      csm-         eye          Av. casman-               /wafr/      w/r-        snow
30592:         (ro)snow                                                         83R6
32363:                                                                   Himalaya (snowy)
32369:9914 wp,a                                                          snow
32495:                                                                             snow
39449:silent   9352                                10043, 10265, 10266, 10789             snow    9931, 9980
39450:silk 3177, 3178, 8240                     sixth day of the month      1482          GcOsnow   9312
39451:silk cloth  8854                          sixth month of the year      4549,        snowy   9930
```


## [2026-10-17T00:05:02.593Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 32360,32372p SOD_pages.txt; sed -n 32488,32497p SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} /9914 wp,a/{print \"leaf\",NR-1} /9980 wfr/{print \"leaf\",NR-1}' SOD_pages.txt"
}
```


### [2026-10-17T00:05:03.027Z] TOOL RESULT

```
      wipaz, uPaz ©Av. vibdzu                                 9929 wbr't C = w+br>t =» w-, Pr't
      fathom                                                  9930 wp^r     B                            (jbJ>^)UU&
      BSTBL, Dhy. 88; Ben v. Notesii 221; Hen. JRAS                wafr-5ar
                                                                   Himalaya (snowy)
        1942, 236.4: GMS 218, 954
                                                                   BSTBL, Dhy. 209; GMS 1135
9913 wp>'
     uPa ©2sg. impv. =*wp-, p>3                               9931 wpr-h     B                                     J^
                                                                   wafra    ©Av. vafra    ©f. n. -hP =»wfr»
9914 wp,a                                                          snow
     upa ©3sg. impf. =*wp-
                                                                   Rust. TSP 13.22 n p228; GMS 1175; BBB p57.72;
9915 wp}m
       wi6/larz (wlrz-) -»wyr*rz-
                                                                        9979 wfcmbd      C = w+ fembd «» w-, fcmbS
       (/cOtremble, (ro)shake
                                                                                                                              <G&
       STi 54.16; GMS 60n 1; wlrz-, STii 2.1                            9980 wfr' M
                                                                             wafra ©f. n. ace. ->; loc. wfry} =*wpr-h
9968 w8-w   M               (jy> ^* j->)<=rjj«jj
                                                                             snow
     wa/u6u (wd-w, w6w(h)) ©A v. vadii\ Ved.
                                                                             GMS 311, 1175; BBB 496 p57, 577 p72
leaf 468
leaf 470
```


## [2026-10-17T00:05:07.910Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F(){ python3 tools/fetch_source.py \"$1\" --note \"page 543, $2\" 2>&1 | tail -1; }\nF 'https://vajehyab.com/moein/ونیز' 'root Wen node 3 Moin Veniz'\nF 'https://vajehyab.com/moein/ونوس' 'root Wen node 3 Moin Venus'\nF 'https://vajehyab.com/moein/ونزوئلا' 'root Wen node 3 Moin Venezuela'\nF 'https://vajehyab.com/moein/برف' 'root Wep node 3 Moin barf'\nF 'https://vajehyab.com/dehkhoda/ونیز' 'root Wen node 3 Dehkhoda Veniz'"
}
```


### [2026-10-17T00:05:10.178Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f93d11ca9d247c9a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bf2725526f91ef3b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/43e06e25d18a5424.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/91c07a802d5fe88a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d41a002a60e05597.txt
```


## [2026-10-17T00:05:12.738Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in f93d11ca9d247c9a bf2725526f91ef3b 43e06e25d18a5424 91c07a802d5fe88a d41a002a60e05597; do echo \"-- $f $(sed -n 3p $f.txt) $(wc -c <$f.txt)\"; grep -n \"ونیز\\|ونوس\\|ونزوئلا\\|برف\" $f.txt | head -6 | cut -c1-400; done"
}
```


### [2026-10-17T00:05:13.218Z] TOOL RESULT

```
-- f93d11ca9d247c9a STATUS: -1 130
1:URL: https://vajehyab.com/moein/ونیز
-- bf2725526f91ef3b STATUS: 200 972
1:URL: https://vajehyab.com/moein/ونوس
4:TITLE: معنی ونوس | فرهنگ انتشارات معین | واژه یاب
6:معنی ونوس | فرهنگ انتشارات معین | واژه یاب 
14: ونوس
18: ونوس در فرهنگ‌های دیگر
19: معنی ونوس در لغت‌نامه دهخدا 
-- 43e06e25d18a5424 STATUS: -1 136
1:URL: https://vajehyab.com/moein/ونزوئلا
-- 91c07a802d5fe88a STATUS: 200 1542
1:URL: https://vajehyab.com/moein/برف
4:TITLE: معنی برف | فرهنگ انتشارات معین | واژه یاب
6:معنی برف | فرهنگ انتشارات معین | واژه یاب 
14: برف
18: برف در فرهنگ‌های دیگر
19: معنی برف در لغت‌نامه دهخدا 
-- d41a002a60e05597 STATUS: 200 2067
1:URL: https://vajehyab.com/dehkhoda/ونیز
4:TITLE: معنی ونیز | لغت‌نامه دهخدا | واژه یاب
6:معنی ونیز | لغت‌نامه دهخدا | واژه یاب 
14: ونیز
17: ونیز. [ وِ ] (اِخ ) وندیک . بندقیه . (یادداشت مرحوم دهخدا). شهری است در ایتالیا که در میان قسمت کم عمق دریای آدریاتیک و بر روی چندین جزیرهٔ کوچک مجتمع بنیان نهاده شده است که خلیج ونیز را نیز تشکیل میدهد. این شهر در حدود 323000 تن سکنه دارد. در این شهر صنایع ظریف زرگری و جواهرسازی و همچنین صنایع کشتی سازی و آهن و پولاد رواج دارد. میدان و کلیسای معروف سن مارک ، قصرهای رؤسای جمهوری و نود کلیسا و 
20: ونیزد
```


## [2026-10-17T00:05:15.674Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 14,18p bf2725526f91ef3b.txt; sed -n 14,18p 91c07a802d5fe88a.txt; cd ..; python3 ../../../tools/fetch_source.py 'https://vajehyab.com/dehkhoda/ونزوئلا' --note 'page 543, root Wen node 3 Dehkhoda Venezuela' | tail -1"
}
```


### [2026-10-17T00:05:16.275Z] TOOL RESULT

```
 ونوس

 فرهنگ انتشارات معین
 (وِ) [ فر. ] (اِ.) 1 - زهره ، ناهید. 2 - رب النوع عشق در نزد یونانی ها.
 ونوس در فرهنگ‌های دیگر
 برف

 فرهنگ انتشارات معین
 (بَ) [ په . ] ( اِ.) آب منجمد که به صورت بلورهایی به شکل منشور مسدس - القاعده متبلور می گردد و در فصل سرما از ابرها به زمین می بارد.
 برف در فرهنگ‌های دیگر
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d8536c1acf06a325.txt
```


## [2026-10-17T00:05:19.584Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; grep -n \"ونزوئلا\" web/d8536c1acf06a325.txt | head -3 | cut -c1-300; grep -n -i \"vafr\\|vafra\\|wafr\" refs/BQT_v1_pages.txt refs/BQT_v1.txt refs/BQT_alt_v1.txt | head"
}
```


### [2026-10-17T00:05:19.957Z] TOOL RESULT

```
1:URL: https://vajehyab.com/dehkhoda/ونزوئلا
```


## [2026-10-17T00:05:23.618Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^برف \\|^برف-\\|^برف ـ\\|برف - \\|برف ـ بفتح\\|برف بفتح\" BQT_v1_pages.txt BQT_v1.txt | head; grep -n \"برفاب\" BQT_v1_pages.txt | head -3"
}
```


### [2026-10-17T00:05:23.905Z] TOOL RESULT

```
BQT_v1_pages.txt:4161:برف » بستن » بسیار» بلیل » بنده» بنیاد وغیره.
BQT_v1_pages.txt:4933:برف ( فارسی ) ۵۸6
BQT_v1.txt:6569:برف » بستن » بسیار» بلیل » بنده» بنیاد وغیره. 
BQT_v1.txt:7868:برف ( فارسی ) ۵۸6 
BQT_v1.txt:29026:برف
```


## [2026-10-17T00:05:27.296Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR<=18762 && /\\[pdf page/{p=$0} NR==18762{print p}' BQT_v1_pages.txt; sed -n 18735,18770p BQT_v1_pages.txt"
}
```


### [2026-10-17T00:05:27.747Z] TOOL RESULT

```
حرف الث قاف هم آمده است .
و عو ‏ منم اول بروزن پرکو » شاخی
باشد مان تهی که درا مانند نضر نوازند .
۰ ‌ ۳
برغوفی ۴ «بانی مثلله بر وزن
سر کوشی ۰ تخمی است که آنرا بفارسی اسفیوش
: مرفره
وبعربی‌بز رقطوها ومشیراژی‌بشکووییوفانی‌فلیون #
خوائند .
برغول س با واومجهول بروزن مرغول»
حلوابی را گوبند که از آرد پزند و آنرا افروشه
نیز خوانند - و کندمی را گون دکه درهم‌شکته
باشند - و هرچیزی که آنرا درهم کوفه باشندد
و آشیکه از کندم دلیده کرده‌پزند ؛ و بدوممنی
آخر بضم اول هم آعده است . #*
بر قاب ۴ هبافا بروزن مهتاب. ممروف
است که آب برف و آب سرد باشد - و کنابه
از آب دهان است که وفت خوردن شخصی‌چیزی
را سیب میل و خواهش طبیمت در دهن‌دیگری
مرگردد و گاه باخد که از دهن یرون آید وی
اختیار بر رد ۰
بر ف آب‌دادن - کنابه از دل سرد
کردن و ناامید ساختن باشد.
رفر « بر وزن صرصر » بیعنی خان
و شوکت و علو در و حنزلت باشد ٩‏ .
بر فر وشان ۱ بروزن برده بوشان.
بمعنی بربروشان است که امت مینمبر باشد .
برفره - بر وزن شه‌تره ۰ بمعنی برقر
باشد که شان و شوکت و عظمت امت ۷ .
۴ . را: برقندان.
۴ - م رکب از : برف + آب .
از ؛: بر فر (فره ‏ خره) .
۲ رکه : برفر .
1 0216» برنی ۷2/۲ , نطنزی ۷۵۲۲
فریزندی بهر دو صورت «کك. ۱ ص ۲۸۵ ۰
سمناتی ۰۷۵۶ ۷۵2۲۵ » سنگری ۷۵۲۲ ۰
```


## [2026-10-17T00:05:31.012Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"\\[pdf page\" BQT_v1_pages.txt | awk -F: '$1<18762' | tail -2; "
}
```


### [2026-10-17T00:05:31.528Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:05:34.486Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 600 BQT_v1_pages.txt; echo; awk 'BEGIN{RS=\"\\f\"} /برفره - بر وزن/{print \"block\",NR}' BQT_v1_pages.txt; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json'));print(d['BQT'].get('page_offset'))\""
}
```


### [2026-10-17T00:05:35.089Z] TOOL RESULT

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
block 480
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-10-17T00:05:38.053Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==479' BQT_v1_pages.txt | grep -n \"برف\\|vafr\\|varf\\|۲۵\" | head -20; awk 'BEGIN{RS=\"\\f\"} NR==479' BQT_v1_pages.txt | tail -25"
}
```


### [2026-10-17T00:05:38.691Z] TOOL RESULT

```
48:شّه ازسفحهٌ ۲۵۷
آن جزیره بانگی عظیم و صدایی ههیپ‌می آبذ ,
و بضی کویند کوهی است در آن جزبر هکه‌شبها
از آن کوه صدای طبل و دهل و سنج میآید .
بر طیسقون - بختح اول و سکون ثانی
و اث بتحتاتی دسیده و بین بی‌نفطهٌ زده و ضم
فاف و واو و نون ساکن ؛ بلقت بونالی گل‌سرخ
را کویند و بعربی طی‌الاحمر خوانند » وبهترین
وی آن بودکه از مصر آورند » و آن قایم مقام
گل‌مخنوم است .
یرم ۴ ۰ تم اول و سکون ثامی و غين
نقطمدار ۰ شدی باشد که از چوب و خاشاكوخاله
وگل در پیش آب بندند » و بفتح اول و کسر
ثانی هم کفته‌اند . و بفتح اول و تالی‌هم‌ینآمده
است. و باین معنی بازای‌نقطه‌دار نیز درست‌است.
بر غاب * - بروزن غرقاب » بند آب‌است
یعنی جایبکه پیش آبرا بندند تا آب در آن
جمع شود .
برست ۲ - بر وزن سرمست .کیاهی
جوی‌آب رود و آنرا مج هگونند ویعربی‌قنابری
و عملول و تملول و شجردالبهق خوانند ۰۷
وبعنی گوبن دگیاهی است که کل‌زردی داردو آ ترا
«لكثاص ۰۲۱۵ . ۲ واگ ناس :
دزی ۱ : ۰*۷۳
۴ - بیواانی 9۳60۵1016 «لك ۱ص ۲۰۵»
شّه ازسفحهٌ ۲۵۷
```


## [2026-10-17T00:05:41.315Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==480' BQT_v1_pages.txt | head -40"
}
```


### [2026-10-17T00:05:41.700Z] TOOL RESULT

```
-- ۷6 سس
بیشتراوفات‌بخر وکاو دهند» وبخورند وبسنی‌دمگر
گفته‌اند ترمایست بپاری و طعم تیژی دارد » تازهٌ
آنرا بپزند وبخورند و چون‌خشك شودبخر و کاو
دهند - و جل وزغ را نیز کویند و آن چیزی
ماشد سب که بر دوی آبهای استاده می‌استد -
بحانب زراعت بر ند ۰
بر غالا فیفان « بالامبروزن‌خرچرانیدن,
بمعتی برانگیختن و تحریض نمودن شخصی باشد
برغهان » بامیم بروزن همزبان. سار
بز رکه و اژدها را گویند .
برغندان - بر وزن د:ندان» جشن
ونشاطی را گوبند که بسبب‌ترديك شدن ماءرهضان
در آخر های شعبان کنند . و بسنی گوبند نام
روز اخر ماه شمبان است ۰ و باین هعنی بجای
حرف الث قاف هم آمده است .
و عو ‏ منم اول بروزن پرکو » شاخی
باشد مان تهی که درا مانند نضر نوازند .
۰ ‌ ۳
برغوفی ۴ «بانی مثلله بر وزن
سر کوشی ۰ تخمی است که آنرا بفارسی اسفیوش
: مرفره
وبعربی‌بز رقطوها ومشیراژی‌بشکووییوفانی‌فلیون #
خوائند .
برغول س با واومجهول بروزن مرغول»
حلوابی را گوبند که از آرد پزند و آنرا افروشه
نیز خوانند - و کندمی را گون دکه درهم‌شکته
باشند - و هرچیزی که آنرا درهم کوفه باشندد
و آشیکه از کندم دلیده کرده‌پزند ؛ و بدوممنی
آخر بضم اول هم آعده است . #*
بر قاب ۴ هبافا بروزن مهتاب. ممروف
است که آب برف و آب سرد باشد - و کنابه
از آب دهان است که وفت خوردن شخصی‌چیزی
را سیب میل و خواهش طبیمت در دهن‌دیگری
مرگردد و گاه باخد که از دهن یرون آید وی
اختیار بر رد ۰
بر ف آب‌دادن - کنابه از دل سرد
کردن و ناامید ساختن باشد.
رفر « بر وزن صرصر » بیعنی خان
و شوکت و علو در و حنزلت باشد ٩‏ .
```


## [2026-10-17T00:05:48.031Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"ونیز\\|ونزوئلا\\|ونوس\" MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -8 | cut -c1-300; grep -n -i \"^venery\\|^win\\b\\|^wish\\b\\|^venom\\|^Venus\" SKT.txt | head"
}
```


### [2026-10-17T00:05:48.561Z] TOOL RESULT

```
MON_part2.txt:35519:پرو و اکوادر و ونزوئلا به فراوانی می‌رو بد. 
MON_part2.txt:50739:کلی مخچه عضو تنظیم تونوس و قوای 
MON_part2.txt:54508:ملاکه و قطرات اشکك ونوس (زهره؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:35519:پرو و اکوادر و ونزوئلا به فراوانی می‌رو بد. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:50739:کلی مخچه عضو تنظیم تونوس و قوای 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:54508:ملاکه و قطرات اشکك ونوس (زهره؛ 
20673:Venery,  bunting  ;  see  Veniaon.
20679:Venom.  (F.-L.)  M.E.rrt#i'jw.-O.F. Vfuim  (K.  s/tfrtinV  — L.  utncnum,  poison.
21484:WIN,
21487:Win.  to  gatu  by  labour,  earn.  (E.) M.  £.  winuen,  pt.  t.  wan,  won,  pp.  vfontttn. A.S.  U'imian,  to  fight,  struggle,  try  lo  get. Labour,  suff^er ;  pt.  t.  iira/in,  pp.  wuntuM.'^ Du.  win/Kn,  Icel.  vinna,  Dan.  vindet Swcd.  vitina  ;  G.  gcwinnen,  0.  H.  G.  xum* an,  to  tight,  strive,  earo';  Goth,  v/innartt lo  Buffer.  Allied  to  Skt  van,  to  beg,  ask for.  honour:  L.  urnerari^xo  honour, M^nuj, desire.     (V  WAN.)      /
21538:Wish.  verb.  (,E.)  M.E.  wi/fArt*.  A.  S. wyscan,  to  wish ;  formed  (by  the  usnal change  from  «/  to  v)  from  A.  S.  wiiu,  sb.,  a wish  ^obsolete).  ^.  This  A.  S.  vnhc  stands for  wunsc  •.  cognate  with  O.  Du.  wunsch, loel.  6sk,  G.  it/ittisch,  O.  H.G.  wunsc,  a wish ;  whence  are  derived  Icel.  askjoy  G. vninschtn,  to  wish.  Allied  to  Skt.  v4nksk, vaUch,  to  wish,  ft  dcsideralive  form  from van,  to  ask.  Similarly  the  E.  word  is  a dcsideralive  form  from  V  WAN,  to  desire, whence  E.  win  ;  see  Win.  Der,  wisA-ful; and  see  wistful.
```


## [2026-10-17T00:05:51.251Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^Venison\\|^Venice\\|^Venereal\\|^Venerate\" SKT.txt | head; sed -n \"$(grep -n '^Venison' SKT.txt | head -1 | cut -d: -f1),+2p\" SKT.txt | cut -c1-500; grep -n \"^Venetian\\|^Venice\\|^Venus\" KLN_1966.txt | head -3"
}
```


### [2026-10-17T00:05:51.868Z] TOOL RESULT

```
20678:Venison.  (F.  «>  L.)  M.£  vtmisoH.^ O.K.  veneisun,  later  vettaijcn,  'venison, flesh  of  beasts  of  cham:; '  CoL  — L.  ufNa- tiawm,  ace.  of  ucmtfic,  the  chose,  al»o game.  — L,  uenafus,  pp.  oiutnari,  lo  bunt venery.  hunting.  (F.  — L.)  V.wneru, 'hunting ;'  CoL  — O.  F.  vitier,  to  bunL  — L.  uenari.
Venison.  (F.  «>  L.)  M.£  vtmisoH.^ O.K.  veneisun,  later  vettaijcn,  'venison, flesh  of  beasts  of  cham:; '  CoL  — L.  ufNa- tiawm,  ace.  of  ucmtfic,  the  chose,  al»o game.  — L,  uenafus,  pp.  oiutnari,  lo  bunt venery.  hunting.  (F.  — L.)  V.wneru, 'hunting ;'  CoL  — O.  F.  vitier,  to  bunL  — L.  uenari.
Venom.  (F.-L.)  M.E.rrt#i'jw.-O.F. Vfuim  (K.  s/tfrtinV  — L.  utncnum,  poison.
Venous ;  sec  Vehicle.
41212:Venetian,  adj.  and  n.  —  ML.  Venetidnus,  fr. Venetia,  ‘Venice’,  fr.  Veneti  (Gk.  Ou6verot, ’Bvexoi  or  ‘Evs-roU,  an  ancient  people  of  Illy¬ rian  origin.  For  the  ending  see  suff.  -ian. vengeance,  n.  —  ME.,  fr.  OF.  (=  F.)  fr.  venger, ‘to  avenge’,  fr.  L.  vindicate,  of  s.m.  See  vindicate and  -ance  and  cp.  avenge,  revenge, vengeful,  adj.  —  Formed  on  analogy  of  revenge¬ ful  from  the  obsol.  verb  venge  (fr.  OF.  venger), with  suff.  -ful.  See  prec.  word.
```


## [2026-10-17T00:05:54.741Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^win,\\|^win, \\|^wish,\\|^wish, \\|^win  \\|^wish  \" KLN_1966.txt | head; grep -n \"^Venus\" KLN_1966.txt"
}
```


### [2026-10-17T00:05:55.076Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:05:58.604Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \"win,  [a-z]*\\.,  [^—]*—  [^.]*\\.[^.]*\\.[^.]*\\.[^.]*\\.[^.]*\\.\" KLN_1966.txt | grep -i \"winnan\" | head -2 | cut -c1-700; grep -n -o \"wish,  [a-z]*\\.[^—]*—  [^.]*\\.[^.]*\\.[^.]*\\.[^.]*\\.\" KLN_1966.txt | head -2 | cut -c1-700; grep -n -o \"Venus,  n[^—]*—[^.]*\\.[^.]*\\.[^.]*\\.\" KLN_1966.txt | head -2|cut -c1-500"
}
```


### [2026-10-17T00:05:59.462Z] TOOL RESULT

```
35063:wish,  adj.  —  Formed  fr.  shrew,  n.,  with  adj. suff.
41256:Venus,  n.  —  L.  Venus,  gen.  Veneris,  ‘the  goddess of  love’.
```


## [2026-10-17T00:06:03.311Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"lead, lead home\\|to lead; to marry\\|uedh-2\\|uedh- 2\\|lemma: [0-9]\\. *uedh\\|lemma: uedh\" POK_full.txt | head; grep -n \"vādayeiti\\|vadayeiti\" POK_full.txt | head -3"
}
```


### [2026-10-17T00:06:03.625Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:06:05.216Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"vadhu\\|vadhū\" POK_full.txt | head -5"
}
```


### [2026-10-17T00:06:05.571Z] TOOL RESULT

```
88808:Material: Old Indie vadhu-i. "bride, young wife, woman', Avestan va5u- ds., vaSayeiti
```


## [2026-10-17T00:06:07.437Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 88800,88812p POK_full.txt; awk 'NR>88808 && /Page\\(s\\)/{print NR\": \"$0; exit}' POK_full.txt"
}
```


### [2026-10-17T00:06:07.771Z] TOOL RESULT

```
References: WP. I 254 f.. Frisk 446 f., 449 f. 
Page(s):1115 

Root/ lemma: ue6y-2, vor Nasalen ued- 

Meaning: to lead 

Material: Old Indie vadhu-i. "bride, young wife, woman', Avestan va5u- ds., vaSayeiti 

(Kaus.) "leads, zieht', with upa- "eine Frau zur matrimony give', with us- "(Frauen) 

entfijhren, rob', KaJ/ya-"heiratsfahig (from girl)'; 
88867: Page(s): 1115-1116
```


## [2026-10-17T00:06:35.285Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *uenor\\|uenor, -aris\\|uenor,-aris\\|uenor -aris\" LAT.txt | head -3; grep -n \"^ *uenenum\\|uenenum, -i\" LAT.txt | head -3"
}
```


### [2026-10-17T00:06:35.722Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:06:37.621Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"uenor\\b\" LAT.txt | head -5; grep -n \"uenenum\" LAT.txt | head -4"
}
```


### [2026-10-17T00:06:38.202Z] TOOL RESULT

```
10939:pour la longue, cf. uenor, lego, etc. CSlator n 1 est atteste que par 3
13479:Si l'on rapproche uSnor, on peut etre tent 4 de voir ici un *co-uenor,
13480:avec la racine qui est dans Venus, uenor. Pure hypothfese. Peut-etre
15355:Fenus, uenor et aerusco) par un aot nouveau expressif. Qn rapproche
31437:emploie iuuenor, A.P.346, qui est glose vewrepet qui traduit
67068:50,16,336: qui uenenum dicit, adicere debet utrum malum an bonum;
```


## [2026-10-17T00:06:40.242Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 67060,67085p LAT.txt | cut -c1-200; grep -n \"^u[eē]nor\\|^ugnor\\|^uSnor\\|^uenor\\|nor, -aris\" LAT.txt | head"
}
```


### [2026-10-17T00:06:40.622Z] TOOL RESULT

```
uend 5 , ueneB: v. ugnun.
uenSnum, -I n.: ddcoction de plantea nagiques,- charne, philtre.
Sena ancien e.g. Afranius, R 3 3O0 et s. aetas et corpus tenerum et
morigeratio | haec sunt uenena formosarum mulierum. Synonyne de gr.
q&Pliotxov, et .conne lui, a pria vite le sena' p 4 joratif de "poison"
(classique, Cic.), bien que Salluste pr 4 cise le sena du non par un
adj., Cat. 11,3: ea (auarttta) quasi venenis malis imbuta, et que le
Digeste reconnande de prdciser le not par bonum ou malum, cf.Dig.
50,16,336: qui uenenum dicit, adicere debet utrum malum an bonum;
nam et medicamenta uenena sunt. Ancien, usuei; panronan, en partie
sons des fornes savantes, M.L.9195. Celt.: britt. gtoenuyn,
Les d 4 riv 4 s et conpoqds ont tona le aena pdjoratif: uenenStus
et uengng, - 3 s; uenSndrius (dpoq.iap.); uengnifer (po 4 t .); uenenosusueneror
l« 7 b ~
(tard.). Par oontre, il faut peut-§tre expliquer par *uenes-fico-s
plntfit que par *uenSni-fico-s (avec haplologie) le coaposd veneficus,
d'ob veneficus, uengfica "eapoisonneur, eapoisonneuse", trivenefica
(Pl .), veneficium (class.).
Un ancien *wenes-no- a-vec sens de "philtre" (cf. Venus) fournirait
une explication plausible.
ueneror, -Srls, -&tus sum, -iri (et actif uenerS, -Ss chez les
anciens): adresser une deaande aux dieux, demander aux dieux une far
veur 'ou une gr&ce (jointA precor, k uenian peto dans une vieille forau-
le citde par T.L.8,g,C: (sc .omnes deos) precor, ueneror, uenian peto
feroque uti e.q.s*; cf.Pl., Ru.357: quisquis est deus, ueneror ut
nos ex hac aerumna eximat} 1349 (en allitdration avec V^nus): illaec
2890:nd dans la aaison" (= Gpercxoc;, et remplace uerna); de IA alumnor, -aris
3049:alucinor, -aris, -ari (et hal(l)ucinor graphie tardive; 1'^ initiale
4351:D 6 riv 4 s: apindrius (ape-) a. A. Trebell., Gall.8,3; apinor, -aris: ei-
7644:bouinor, -aris ( bobinor): = cpnuicior. Forme et sens pen sfirs;
12736:Derives: co cionor, -aris, et coci strio (?): tabernarius Gloss., cf.
13636:continor, -aris, -atus sum, -ari: rencontrer. Verbe rare, ar-
13645:de "disconrs prononce devant le penple assembld"; de IA contionor, -aris
38046:minor, -aris, -atus sum,-ari sp^cialisi? dans le sens moral de "menacer";
40502:natinor, -aris (quamtite de l'a inconnue; l*t est sans doute long
48851:Ddrivds: popinor, -aris: frdquenter les cabarets; poplnS,-Snis m.
```


## [2026-10-17T00:06:44.813Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BOOK; cp site/pages/543.jpg /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg543.jpg 2>/dev/null; pdftoppm -f 543 -l 543 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf data/verification/sources/refs/ocr/BOOK/543 && command ls -la data/verification/sources/refs/ocr/BOOK/543.png"
}
```


### [2026-10-17T00:06:46.243Z] TOOL RESULT

```
-rw-r--r-- 1 sfmqrb sfmqrb 73840 Oct 16 20:06 data/verification/sources/refs/ocr/BOOK/543.png
```


## [2026-10-17T00:09:28.251Z] TOOL CALL #73: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/draft-543.py",
 "content": "import json\nW = \"https://en.wiktionary.org/wiki/\"\nWEN = W + \"Reconstruction:Proto-Indo-European/wenh₁-\"\nWEDH = W + \"Reconstruction:Proto-Indo-European/wedʰ-\"\n\nPOK_WEN = {\"ref\": \"POK:1146\", \"status\": \"supports\", \"note\": \"POK_full.txt l.90924ff. 'Root/ lemma: uen-1 ... Meaning: to strive; to wish for, to love ... Latin venus, -eris love ..., Venus ..., veneror ... here also venor ... pursue game, hunt, chase ... zero grade Old Icelandic osk (*wunsko) wish, Old English wysc-, Old High German wunsc ... Gothic winnan suffer ... Old Saxon winnan quarrel, fight ... References: WP. I 258 f.' Page(s): 1146-1147.\"}\nOEW = {\"ref\": \"OEW:434\", \"status\": \"not_checked\", \"note\": \"Shipley, Origins of English Words: lending-only on archive.org; not accessible.\"}\nAHD_WEN = {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. wen-1 'To desire, strive for. 1. Suffixed form *wen-w- in Germanic *winn(w)an, to seek to gain, in Old English winnan, to win: WIN ... 6. Suffixed zero-grade form *wn-sko- in Germanic *wunsk- in Old English wyscan, to desire, wish: WISH ... venerari, to worship: VENERATE, VENEREAL, VENERY1, VENUS; b. suffixed form *wen-es-no- in Latin venenum, love potion, poison: VENOM. 9. Suffixed form *wen-eto-, \\\"beloved,\\\" possibly in Germanic *Weneda- ... the Wends ... 11. Lengthened-grade form *wen-a- in Latin venari, to hunt: VENATIC, VENERY2, VENISON. [Pok. 1. uen- 1146.]'\"}\nWLD_WEN = {\"src\": \"WLD\", \"where\": \"Bd. I 259-260 (WLD_Bd1_pages.txt leaves 268-269)\", \"stance\": \"supports\", \"note\": \"'uen- ... Lat. venus, -eris „Liebe, Liebesgenuß, Anmut, Liebreiz“, Venus Name der Liebesgöttin ... veneror -ari „mit religiöser Scheu verehren ...“, ursprgl. „die Liebe bezeugen“'; further 'ags. wusc, ahd. wunsc, wunsch' and 'got. winnan „leiden“, altn. vinna „arbeiten ...“, as. winnan „streiten, kämpfen“'.\"}\nIEC_WEN = {\"src\": \"IEC\", \"where\": \"p. 1512-1513 s.v. uén- (1); uenos, -es-\", \"stance\": \"supports\", \"note\": \"'uén- (1) desire, hope, favour, outlook, charm ... Lat. Venus, -eris; venia, f. pardon, grace' and 'uenos, -es- desire ... Lat. Venus'; Mann does not list venari here.\"}\nKLN_VENERATE = {\"src\": \"KLN\", \"where\": \"p. ~1696 s.v. venerate (KLN_1966.txt l.41201)\", \"stance\": \"supports\", \"note\": \"'venus, gen. veneris, love, sexual desire ... whence Venus ... cogn. with OI. vanas- desire, vanati ... Avestic vanaiti ... OE. wynn joy ... wyscan to wish. All these words derive fr. I.-E. base *wen-, to strive after, wish, desire'.\"}\n\nentries = []\n\n# ---------------- entry 0: Wen ----------------\nn = []\nn.append({\n \"id\": 1, \"lang\": \"Latin\", \"words\": \"vener; venus; venĕnum; venetî\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Latin venus, gen. veneris 'love, charm' (Venus the goddess) continues a PIE neuter s-stem *wénh₁-os 'loveliness' (= Skt. vánas- 'desire'); 'vener' is not a Latin word in itself but the oblique stem vener- of venus, which underlies the deponent verb venerārī 'to worship' (originally 'to show love'), so the gloss 'to love' is loose. venēnum (the book marks a short ĕ; Latin has long ē) is from *wenes-no- 'love potion, philtre' and only later 'poison' (Ernout-Meillet, AHD, Wiktionary). The Venetī: Nourai follows AHD's *wen-eto- 'beloved', but AHD applies this to the Wends, and Wiktionary derives Gaulish/Celtic Wenetoi 'the friendly ones, kinsmen' from *wenyā 'kindred', itself from *wenh₁-; Klein simply calls the Veneti 'an ancient people of Illyrian origin'. So venus and venenum are confirmed, the Veneti link is plausible only.\",\n \"derivation_fa\": \"لاتینی venus (حالت اضافی veneris) «عشق، دلربایی» و نام ایزدبانو Venus از نام‌واژهٔ هندواروپایی آغازین *wénh₁-os «زیبایی، دلخواهی» است و با سنسکریت vánas- «آرزو» هم‌ریشه است. «vener» به‌تنهایی واژهٔ لاتینی نیست، ستاک صرفی همان venus است که فعل venerārī «پرستیدن» از آن ساخته شده. venēnum در اصل «معجون عشق» (از *wenes-no-) بوده و بعدها معنای «زهر» گرفته است. پیوند قوم Venetī با «محبوب» را واتکینز دربارهٔ قوم وند گفته و ویکی‌واژه نام آنان را از سلتی *wenetos «خویشاوندان، دوستان» می‌داند که آن هم از همین ریشه است. پس venus و venenum درست است و بخش Venetī با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"venus\", W + \"venenum\", W + \"veneror\", W + \"Veneti\", WEN],\n \"ref_check\": [AHD_WEN],\n \"consulted\": [\n  {\"src\": \"LAT\", \"where\": \"s.v. Venus and uenēnum (LAT.txt l.67061, 67309ff.)\", \"stance\": \"supports\", \"note\": \"'Venus, -eris f.: l'amour ... Par sa forme, Venus est un ancien thème neutre en -os/-es (d'où sans doute uenenum)'; s.v. uenēnum 'décoction de plantes magiques, charme, philtre ... Un ancien *wenes-no- avec sens de \\\"philtre\\\" (cf. Venus) fournirait une explication plausible.'\"},\n  {\"src\": \"KLN\", \"where\": \"p. ~1696 s.v. Venetian (KLN_1966.txt l.41212)\", \"stance\": \"partial\", \"note\": \"'Venetia, Venice, fr. Veneti ..., an ancient people of Illyrian origin' — no link of the Veneti to *wen-.\"},\n  WLD_WEN, IEC_WEN]})\nn.append({\n \"id\": 2, \"lang\": \"French\", \"words\": \"Venus; Venezia; Vennezuela\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"Vennezuela\",\n \"correct_form\": \"Venezuela\",\n \"derivation\": \"The book prints 'Vennezuela' with a double n; this is Nourai's misprint for Venezuela (the extraction is faithful, see site/pages/543.jpg). The box is labelled French but only Venus (French Vénus, from Latin Venus) is French; Venezia is the Italian name of Venice (from Medieval Latin Venetia < Venetī + -ia; French Venise), and Venezuela is Spanish, from Italian Veneziola 'little Venice', the name given in 1499 (Ojeda/Vespucci expedition) to stilt-house villages on Lake Maracaibo (Wiktionary). The node's real role is the French/Italian/Spanish intermediary through which the names reached Persian.\",\n \"derivation_fa\": \"در کتاب «Vennezuela» با دو n چاپ شده که خطای چاپی خود کتاب است و صورت درست Venezuela است؛ استخراج داده درست است. این خانه «فرانسوی» نام گرفته، ولی تنها Venus (فرانسوی Vénus) فرانسوی است؛ Venezia نام ایتالیایی شهر ونیز است (از لاتینی میانه Venetia، از نام قوم Venetī) و Venezuela اسپانیایی و برگرفته از ایتالیایی Veneziola «ونیز کوچک» است که در ۱۴۹۹ بر روستاهای خانه‌های پایه‌دار دریاچهٔ ماراکائیبو نهاده شد. پس روند کلی درست است ولی برچسب زبان و املای واژه نادرست است.\",\n \"sources\": [W + \"Venezuela\", W + \"Venezia\", W + \"Venice\"],\n \"ref_check\": [{\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"No reference cited by Nourai for this node.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"p. ~1696 s.v. Venetian (KLN_1966.txt l.41212)\", \"stance\": \"supports\", \"note\": \"'ML. Venetianus, fr. Venetia, Venice, fr. Veneti' — supports Venezia < Venetia < Veneti.\"},\n  {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/ونوس\", \"stance\": \"supports\", \"note\": \"'ونوس (وِ) [فر.] (اِ.) 1- زهره، ناهید. 2- رب النوع عشق' — Mo'in tags Venus as a French loan, i.e. the French intermediary is right for Venus.\"}]})\nn.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"Venŭs; Venîz; Venezŭelâ\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Modern Persian learned borrowings of the 19th-20th c.: ونوس venus from French Vénus (Mo'in marks it [فر.] 'French'); ونیز veniz from French Venise (with Persian -iz for French -ise; older Persian used وندیک and Ottoman-Arabic بندقیه, as Dehkhoda notes); ونزوئلا venezuelā from French/Spanish Venezuela. All three are real Persian words with the given meanings.\",\n \"derivation_fa\": \"این سه واژه وام‌واژه‌های تازهٔ فارسی (سدهٔ نوزدهم و بیستم) هستند: «ونوس» از فرانسوی Vénus (معین آن را با نشان [فر.] آورده)، «ونیز» از فرانسوی Venise (در فارسی کهن‌تر «وندیک» و صورت معرّب-ترکی «بندقیه» به کار می‌رفت، چنان‌که دهخدا یاد کرده) و «ونزوئلا» از فرانسوی/اسپانیایی Venezuela. ادعای نورایی درست است.\",\n \"sources\": [\"https://vajehyab.com/moein/ونوس\", \"https://vajehyab.com/dehkhoda/ونیز\"],\n \"ref_check\": [{\"ref\": \"MON6:2222,2223\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 6 (proper names) is not online; vajehyab has the lexicon entry ونوس only ('[فر.] زهره، ناهید ... رب النوع عشق'), consistent with Nourai; ونیز and ونزوئلا return no Mo'in entry online.\"}],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/ونوس\", \"stance\": \"supports\", \"note\": \"'ونوس (وِ) [فر.] (اِ.) 1- زهره، ناهید. 2- رب النوع عشق در نزد یونانی‌ها'.\"},\n  {\"src\": \"DEH\", \"where\": \"vajehyab.com/dehkhoda/ونیز\", \"stance\": \"supports\", \"note\": \"'ونیز [ وِ ] (اِخ) وندیک. بندقیه ... شهری است در ایتالیا ...'.\"},\n  {\"src\": \"HRN\", \"where\": \"HRN.txt (grep ونیز / Venedig)\", \"stance\": \"silent\", \"note\": \"Horn 1893 covers inherited vocabulary; no entry for these modern loans.\"},\n  {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (grep ونوس, ونیز)\", \"stance\": \"silent\", \"note\": \"No entry.\"}]})\nn.append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"venereal, Venus, venom, Venice\",\n \"verdict\": \"plausible\",\n \"derivation\": \"venereal: Middle English, from Latin venereus 'of sexual love' < venus, veneris + -al. Venus: direct from Latin. venom: ME venym, venim < Old French venim < Vulgar Latin *venīmen (suffix swap for -ēnum) < Latin venēnum 'potion, poison', originally 'love potion' (Klein, Wiktionary). Venice: ME Venyse < Old French Venise / Italian, from Medieval Latin Venetia, land of the Venetī. The first three are securely from *wenh₁-; Venice depends on the uncertain etymology of the tribal name Venetī (see node 1), so the node as a whole is plausible.\",\n \"derivation_fa\": \"venereal از لاتینی venereus «وابسته به عشق جنسی» از venus است؛ Venus مستقیم از لاتینی آمده؛ venom از انگلیسی میانهٔ venym، از فرانسوی کهن venim، از لاتینی عامیانه *venīmen، از لاتینی venēnum «معجون، زهر» که در اصل «معجون عشق» بوده است. Venice از فرانسوی کهن Venise و لاتینی میانه Venetia «سرزمین قوم Venetī» است. سه واژهٔ نخست بی‌گمان از ریشهٔ *wenh₁- اند، ولی پیوند Venice به این ریشه به ریشه‌شناسی نام Venetī بسته است و تنها پذیرفتنی است.\",\n \"sources\": [W + \"venereal\", W + \"venom\", W + \"Venice\", W + \"venus\"],\n \"ref_check\": [{\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"No reference cited by Nourai for this node.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"p. ~1696 s.v. venereal, venom (KLN_1966.txt l.41201, 41220)\", \"stance\": \"supports\", \"note\": \"'venereal ... fr. L. venereus, pertaining to love or sexual desire, fr. venus, gen. veneris'; 'venom ... fr. OF. venim ... fr. VL. *venimen ... fr. L. venenum ... L. venenum orig. meant love potion. It derives fr. venus'.\"},\n  {\"src\": \"SKT\", \"where\": \"s.v. Venom (SKT.txt l.20679)\", \"stance\": \"supports\", \"note\": \"'Venom. (F.-L.) M.E. venim - O.F. venim - L. uenenum, poison.'\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. Venetian (l.41212)\", \"stance\": \"partial\", \"note\": \"Venice < Venetia < Veneti, 'an ancient people of Illyrian origin' — no *wen- link.\"}]})\nn.append({\n \"id\": 5, \"lang\": \"Germanic\", \"words\": \"winnan; wunsk\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *winnaną 'to toil, strive, win' (Gothic winnan 'suffer', OE winnan 'labour, fight', OHG winnan) from a nu-present *wn̥h₁-néw- of *wenh₁- (Wiktionary, LIV), and *wunskaz 'a wish' (OHG wunsc, ON ósk) with verb *wunskijaną, from the sḱe-present *wn̥h₁-sḱé-. 'winnan' is the attested Gothic/OE/OHG form and 'wunsk' is the Germanic stem (OHG wunsc); glosses agree with AHD.\",\n \"derivation_fa\": \"ژرمنی آغازین *winnaną «کوشیدن، رنج بردن، به دست آوردن» (گوتی و انگلیسی کهن winnan) از ستاک *wn̥h₁-néw- و *wunskaz «آرزو» (آلمانی علیای کهن wunsc) از ستاک *wn̥h₁-sḱé- ریشهٔ *wenh₁- ساخته شده‌اند. واتکینز، پوکورنی و ویکی‌واژه همین را می‌گویند و ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Germanic/winnaną\", W + \"Reconstruction:Proto-Germanic/wunskaz\", WEN],\n \"ref_check\": [AHD_WEN],\n \"consulted\": [POK_WEN | {\"src\": \"POK\", \"where\": \"p. 1146-1147\", \"stance\": \"supports\"},\n  WLD_WEN,\n  {\"src\": \"SYN\", \"where\": \"16.27 LOVE (SYN.txt l.28071)\", \"stance\": \"supports\", \"note\": \"'Lat. venus love, charm ... : Skt. van- seek, desire, gain, Goth. wens hope, OE wyn, OHG wunna joy, bliss, OHG wunscan, OE wyscan wish. Walde-P. 1.258.'\"}]})\nn.append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"win; wish\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"win: ME winnen < OE winnan 'to labour, fight', ġewinnan 'conquer, gain' < PGmc *winnaną; the sense narrowed from 'strive' to 'gain by striving'. wish: ME wisshen < OE wȳsċan < PWGmc *wunskijan < PGmc *wunskijaną, with i-umlaut of u to y and later unrounding to i, and palatalisation of -sc- to -sh-.\",\n \"derivation_fa\": \"win از انگلیسی میانهٔ winnen و انگلیسی کهن winnan «کوشیدن، جنگیدن» است و معنای آن از «کوشیدن» به «با کوشش به دست آوردن» تنگ شده است. wish از انگلیسی کهن wȳsċan و ژرمنی آغازین *wunskijaną است؛ u با دگرگونی i-umlaut به y و سپس i بدل شده و sc به sh. ادعای نورایی درست است.\",\n \"sources\": [W + \"win\", W + \"wish\"],\n \"ref_check\": [{\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"No reference cited by Nourai for this node.\"}],\n \"consulted\": [\n  {\"src\": \"SKT\", \"where\": \"s.v. Win, Wish (SKT.txt l.21487, 21538)\", \"stance\": \"supports\", \"note\": \"'Win ... A.S. winnan, to fight, struggle, try to get ... Allied to Skt van ... L. uenerari, Venus'; 'Wish ... A.S. wyscan ... from A.S. wusc ... cognate with ... O.H.G. wunsc ... Allied to Skt. vāñch ... from √WAN, to desire, whence E. win'.\"},\n  KLN_VENERATE]})\nn.append({\n \"id\": 7, \"lang\": \"Latin\", \"words\": \"věnârî\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Latin vēnārī (vēnor) 'to hunt' has a long ē (the book's breve is wrong in quantity but the word is right). Pokorny, Walde-Pokorny's successor AHD (*wēn-ā-, lengthened grade), Buck and Klein connect it with *wen- 'strive after', the sense 'pursue (game)' coming from 'seek to gain'. Wiktionary, however, gives an alternative from *weyh₁- 'to chase, pursue' (Skt. véti, Av. vayeiti, Lith. vyti) and marks the *wenh₁- derivation as disputed; Klein himself cites the *wei- forms as a 'denasalized var.' So the link to Wen is accepted by many but not all.\",\n \"derivation_fa\": \"لاتینی vēnārī «شکار کردن» (با ē کشیده) را پوکورنی، واتکینز، باک و کلاین با درجهٔ بالاندهٔ ریشهٔ *wen- «در پی چیزی کوشیدن» پیوند می‌دهند و معنای «دنبال کردن شکار» را از «جستن، به دست آوردن» می‌دانند. ولی ویکی‌واژه احتمال دیگری را هم می‌آورد: ریشهٔ *weyh₁- «دنبال کردن» (سنسکریت véti، اوستایی vayeiti). پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"venor\", WEN],\n \"ref_check\": [{\"ref\": \"KLN:1697\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.41208 (leaf 899, printed pp. 1696-1697) s.v. venery, n., hunting: 'fr. OF. venerie, fr. L. venari, to hunt, pursue, which prob. derives fr. I.-E. base *wen-, to strive after. See venerate ...'; also notes Av. vayeiti 'hunts' etc. as 'prob. derivatives of a denasalized var. of the above base'.\"}],\n \"consulted\": [\n  POK_WEN | {\"src\": \"POK\", \"where\": \"p. 1146\", \"stance\": \"supports\"},\n  AHD_WEN | {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wen-1 §11\", \"stance\": \"supports\"},\n  {\"src\": \"SYN\", \"where\": \"3.79 HUNT (SYN.txt l.5074)\", \"stance\": \"supports\", \"note\": \"'Lat. vēnārī (> Rum. vâna), prob. (with grade *wēn- beside *wen-) : Skt. van- seek, desire, OE winnan strive, fight, etc. Walde-P. 1.230. Ernout-M. 1085.'\"}]})\nn.append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"venery\",\n \"verdict\": \"plausible\",\n \"derivation\": \"venery 'hunting' (archaic): ME venerie < Old/Middle French venerie, from vener 'to hunt' < Latin vēnārī (Klein, Skeat, Wiktionary). The French-to-English route is certain; the ultimate link to Wen depends on node 7. (A homonym venery 'sexual love' from Medieval Latin veneria < venus also exists, and that one is certainly from *wenh₁-.)\",\n \"derivation_fa\": \"venery «شکار» (کهنه) از انگلیسی میانهٔ venerie، از فرانسوی کهن venerie، از فعل vener «شکار کردن»، از لاتینی vēnārī است. این راه درست است، ولی پیوند نهایی آن با ریشهٔ Wen به ریشه‌شناسی vēnārī بسته است و تنها پذیرفتنی است. واژهٔ هم‌آوای دیگری venery «عشق جنسی» هم هست که از venus آمده و بی‌گمان از همین ریشه است.\",\n \"sources\": [W + \"venery\"],\n \"ref_check\": [{\"ref\": \"KLN:1697\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.41208 'venery, n., hunting (archaic). — ME. venerie, fr. OF. venerie ... fr. L. venari, to hunt, pursue, which prob. derives fr. I.-E. base *wen-, to strive after'; next entry l.41210 'venery, n., sexual love ... From the stem of L. venus'.\"}],\n \"consulted\": [\n  {\"src\": \"SKT\", \"where\": \"s.v. Venison (SKT.txt l.20678)\", \"stance\": \"supports\", \"note\": \"'venery, hunting. (F. - L.) M.E. venerie, hunting ... O.F. vener, to hunt. - L. uenari.'\"},\n  {\"src\": \"KLN\", \"where\": \"p. 1697 s.v. venison\", \"stance\": \"supports\", \"note\": \"'venison ... fr. L. venatio ... fr. venatus, pp. of venari, to hunt. See venery, hunting.'\"}]})\nn.append({\n \"id\": 9, \"lang\": \"Indo-European\", \"words\": \"Wedh\",\n \"verdict\": \"disputed\",\n \"derivation\": \"PIE *wedʰ- 'to lead (home), marry' (Pokorny 1115-1116 uedh-2, WP I 254-255, Mann uedh- (2)) is a real root, but it is a separate root, not a derivative of *wenh₁- as the arrow claims: the two share only the initial *we- and no source derives one from the other. Nourai's citation shows how the link arose: Klein p.1687 s.v. vaivode analyses Slavic vojevoda as voji 'warriors' (cognate with Latin venari, 'see venery') + -voda 'leader' from *wedh- 'to lead' (Lith. vedu, Avestic vādayeiti); Nourai transferred the second element to the Wen chart. Klein p.1697 (venery) does not mention *wedh-.\",\n \"derivation_fa\": \"ریشهٔ هندواروپایی *wedʰ- «بردن، به خانه بردن عروس، زن گرفتن» (پوکورنی ص ۱۱۱۵-۱۱۱۶، والده-پوکورنی ج ۱ ص ۲۵۴-۲۵۵، مان) ریشه‌ای واقعی است، ولی ریشه‌ای جداگانه است و از *wenh₁- مشتق نشده؛ هیچ منبعی این دو را به هم پیوند نمی‌دهد. خاستگاه این پیوند نزد نورایی مدخل vaivode در کلاین است که بخش نخست آن (voji «جنگاوران») را با لاتینی venari و بخش دوم (-voda «رهبر») را با *wedh- «بردن» سنجیده است. پژوهش امروزی این پیکان را رد می‌کند.\",\n \"sources\": [WEDH],\n \"ref_check\": [{\"ref\": \"KLN:1697\", \"status\": \"contradicts\", \"note\": \"KLN_1966.txt p.1697 (leaf 899) s.v. venery: derives venari from *wen- and compares Skt. veti, Av. vayeiti 'hunts' (a 'denasalized var.'), but says nothing about *wedh- 'to lead'. The *wedh- material is on p.1687 s.v. vaivode (l.40999): 'The second element is rel. to ... OSlav. vesti ... Lith. vedu, vesti ... to lead, Ir. fedim, I lead, bring, Avestic vādayeiti, leads' — as an element of a compound, not as a derivative of *wen-.\"}],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"p. 1115-1116 (POK_full.txt l.88803ff.)\", \"stance\": \"contradicts\", \"note\": \"'Root/ lemma: uedh-2, vor Nasalen ued- / Meaning: to lead / Material: Old Indic vadhū- bride, young wife, woman, Avestan vaδu- ds., vāδayeiti (Kaus.) leads, zieht ...' — a separate lemma, not under uen-1 (p.1146).\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I 255 (WLD_Bd1_pages.txt l.23844, leaf 264)\", \"stance\": \"contradicts\", \"note\": \"'2. uedh „führen; heimführen, heiraten (vom Manne)“. Ai. vadhū-h „Braut, junge Frau“, av. vaδu- „Weib, Frau“ vāδayeiti (Kaus.) „führt, zieht, schleppt“' — separate root from uen- (Bd. I 258f.).\"},\n  {\"src\": \"IEC\", \"where\": \"p. ~1505 s.v. uedh- (2) (IEC.txt l.19801)\", \"stance\": \"contradicts\", \"note\": \"'uedh- (2) lead, bring, carry. WP I, 254 ... Av. vad-, v. tr. & intr. lead; go ... OCS vedo, vesti ... Li. vedu, vèsti' — independent root.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wedh-\", \"stance\": \"silent\", \"note\": \"Only 'wedh-. To push, strike ... [Pok. 1. uedh- 1115.]'; the 'lead' root is not in the 1985 appendix.\"}]})\nn.append({\n \"id\": 10, \"lang\": \"Avestan\", \"words\": \"vadu 2; vâdayeiti\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Avestan vāδayeiti 'leads, draws, drags' (Bartholomae col. 1343 s.v. vad- 'führen', iterative-causative stem vāδaya-; with upa- 'give a woman in marriage') is the regular causative *wodʰ-éye-ti of *wedʰ- (PIIr *wādʰáyati, PIr *wādáyati; Wiktionary). 'vadu 2' glossed 'to lead' is not an Avestan verb: the verbal root is vad-, while the attested noun vaδū- (Bartholomae col. 1345) means 'woman, wife' (= Skt. vadhū- 'bride'). Nourai seems to have taken vaδu- from Pokorny's lemma 'uedh-2' (hence the '2') and given it the root's gloss. vādayeiti is confirmed; vadu is a real word with the wrong gloss.\",\n \"derivation_fa\": \"اوستایی vāδayeiti «می‌برد، می‌کشد» (بارتولومه، ستون ۱۳۴۳، ریشهٔ vad- «بردن»، با upa- «زن به همسری دادن») صورت سببی منظم *wodʰ-éye-ti از ریشهٔ *wedʰ- است و درست است. ولی «vadu» در اوستایی فعل «بردن» نیست؛ ریشهٔ فعلی vad- است و نام‌واژهٔ vaδū- (بارتولومه، ستون ۱۳۴۵) به معنای «زن، همسر» است و با سنسکریت vadhū- «عروس» برابر است. گویا نورایی این واژه را از مدخل uedh-2 پوکورنی برداشته و معنای ریشه را به آن داده است. پس بخش vādayeiti درست و بخش vadu با معنای نادرست آمده است.\",\n \"sources\": [WEDH],\n \"ref_check\": [{\"ref\": \"KLN:1687\", \"status\": \"partial\", \"note\": \"KLN_1966.txt l.40999 (leaf 894, p.1687) s.v. vaivode: '... Lith. vedu, vesti, and vadau, vadyti, Lett. vedu, vest, and vadu, vadit, to lead, Ir. fedim, I lead, bring, Avestic vādayeiti, leads' — supports vādayeiti 'leads'; the form 'vadu' 'to lead' here is LATVIAN, not Avestan.\"}],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"col. 1343-1345 (BRT.txt l.22392ff.)\", \"stance\": \"partial\", \"note\": \"'vad- führen. Praes. 30 (Iter.) vāδaya- ... führen, ziehen, schleppen ... urvānəm bastəm vāδayeiti'; and col. 1345 'vaδū- f. Weib, Frau ... ai. vadhū- f.; np. vgl. bayōg Braut' — vādayeiti confirmed, vaδū- means 'woman', not 'to lead'.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I 255\", \"stance\": \"supports\", \"note\": \"'av. vaδu- „Weib, Frau“, vāδayeiti (Kaus.) „führt, zieht, schleppt“, mit upa- „eine Frau zur Ehe geben“'.\"},\n  {\"src\": \"SOD\", \"where\": \"no. 9968 (SOD_pages.txt l.32499)\", \"stance\": \"partial\", \"note\": \"Sogdian 'wδ-w M ... wa/u6u (wδ-w, wδw(h)) © Av. vadū, Ved. [vadhū]' 'wife' — confirms the Avestan noun means 'wife'.\"}]})\n\nentries.append({\n \"entry\": 0, \"root\": \"Wen\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *wenh₁- (*wen-) 'to strive for, wish, desire, love' (Pokorny 1146-1147 uen-1; LIV² *u̯enH-; Watkins wen-1)\",\n \"note\": \"Root, label and gloss are right: Pokorny 1146 uen-1 'to strive; to wish for, to love', WP I 258f., Watkins wen-1 'to desire, strive for', Wiktionary *wenh₁-. Latin venus/Venus, venerārī, venēnum, Germanic *winnaną, *wunsk- and English win, wish, venereal, venom are standard derivatives. Weaker points: Latin vēnārī 'hunt' is attached to this root by Pokorny, Watkins, Buck and Klein but Wiktionary also offers *weyh₁- 'chase'; the Veneti/Venice link rests on *wen-eto- 'beloved' (AHD applies it to the Wends) or Celtic *wenetos 'kinsmen'. The last branch (Wedh 'to lead' with Avestan vādayeiti) is a separate root that Nourai took from Klein's entry vaivode; it does not derive from Wen. 'Vennezuela' is a misprint in the book. Otherwise the extraction matches the printed page (site/pages/543.jpg).\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *wenh₁- «کوشیدن برای چیزی، آرزو کردن، دوست داشتن» در پوکورنی (ص ۱۱۴۶-۱۱۴۷)، والده-پوکورنی (ج ۱، ص ۲۵۸)، واتکینز و ویکی‌واژه آمده است و ریشه، زبان و معنایی که نورایی داده درست است. لاتینی venus و venerārī و venēnum، ژرمنی winnan و wunsk و انگلیسی win و wish و venereal و venom از این ریشه‌اند. پیوند لاتینی vēnārī «شکار کردن» و نام قوم Venetī (ونیز) با این ریشه پذیرفتنی است ولی قطعی نیست. شاخهٔ آخر، یعنی ریشهٔ Wedh «بردن» و اوستایی vādayeiti، ریشه‌ای جداگانه است که نورایی از مدخل vaivode در فرهنگ کلاین برداشته و از Wen مشتق نشده است. «Vennezuela» هم خطای چاپی کتاب است.\",\n \"sources\": [WEN, W + \"venus\", W + \"venor\"],\n \"ref_check\": [POK_WEN, OEW],\n \"consulted\": [WLD_WEN, AHD_WEN | {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wen-1\", \"stance\": \"supports\"}, IEC_WEN, KLN_VENERATE],\n \"nodes\": n})\n\n# ---------------- entry 1: Wep ----------------\nPOK_WEP = {\"ref\": \"POK:1149\", \"status\": \"supports\", \"note\": \"POK_full.txt l.91039ff. 'Root/ lemma: uep-2 / Meaning: to throw, throw out ... Old Indic vapati wirft, streut (den Samen), vapra- Aufwurf (from earth) ..., Avestan vafra-, Middle Persian vafr, npers. barf snow (actually [*Schnee]wehe?) ... remains far off Latin vepres briar'.\"}\nWLD_WEP = {\"src\": \"WLD\", \"where\": \"Bd. I 256 (WLD_Bd1_pages.txt l.23997, leaf 265)\", \"stance\": \"partial\", \"note\": \"'uep- „werfen, streuen“. Ai. vapati „wirft, streut (Saat)“, av. aor. vī-vāpat „verödete“' — root and Sanskrit confirmed; the snow words are not listed here.\"}\nm = []\nm.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"vafra\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Avestan vafra- m. 'snow' is well attested (Vendidad 2.22, 2.34; Bartholomae col. 1347-1348, with compound jaiwi-vafra- 'with deep snow'), from Proto-Iranian *wafrah < PIIr *wapras, with Iranian spirantisation of p to f before r. The word is certain; its derivation from *wep- 'to throw, strew' (snow as 'what is strewn' or 'snowdrift') is Pokorny's suggestion, marked with '?' by him; Buck writes 'etym.?' and Wiktionary stops at PIIr *wapras. So the arrow from the root is plausible, not proven.\",\n \"derivation_fa\": \"اوستایی vafra- «برف» در وندیداد آمده است (بارتولومه، ستون ۱۳۴۷-۱۳۴۸) و از ایرانی آغازین *wafrah و هندوایرانی *wapras است؛ p پیش از r در ایرانی به f سایشی بدل شده است. خود واژه بی‌گمان درست است، ولی پیوند آن با ریشهٔ *wep- «افشاندن، پراکندن» (برف چون «چیز پاشیده» یا «برف‌انباشت») پیشنهاد پوکورنی با نشان پرسش است و باک ریشهٔ آن را نامعلوم می‌داند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Iranian/wafrah\", W + \"برف\"],\n \"ref_check\": [POK_WEP],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"col. 1347-1348 s.v. vafra- (BRT.txt l.22453)\", \"stance\": \"partial\", \"note\": \"'j. vafra- m. Schnee: ... V. 2.34; ... V. 2.22 ... KompE. — mp. (Pü.) vafr, np. barf' — confirms word and MP/NP descendants; gives no root.\"},\n  {\"src\": \"SYN\", \"where\": \"1.73 SNOW (SYN.txt l.2027)\", \"stance\": \"partial\", \"note\": \"'Av. vafra-, rare but confirmed by Pahl. vafr, NPers. barf snow, etym.? Barth. 1347.'\"},\n  WLD_WEP,\n  {\"src\": \"SOD\", \"where\": \"no. 9931 (SOD_pages.txt l.32366)\", \"stance\": \"supports\", \"note\": \"'9931 wpr-h B wafra © Av. vafra © f. n. ... snow'.\"}]})\nm.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"vafr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian wafr [wpl] 'snow' (MacKenzie; Manichaean MP wpr, Parthian wfr) is the regular continuation of Old Iranian *wafra- (Av. vafra-) with loss of the final thematic vowel. The Pahlavi writing wpl uses l for r, as usual.\",\n \"derivation_fa\": \"پهلوی wafr (به خط wpl) «برف» (مکنزی؛ فارسی میانهٔ مانوی wpr) دنبالهٔ منظم ایرانی باستان *wafra- (اوستایی vafra-) است که واکهٔ پایانی آن افتاده است. در خط پهلوی r با نشانهٔ l نوشته شده است. ادعای نورایی درست است.\",\n \"sources\": [W + \"برف\"],\n \"ref_check\": [POK_WEP],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p. 87 s.v. wafr (PHD_mackenzie.txt l.5136)\", \"stance\": \"supports\", \"note\": \"'wafr [wpl | M wpr, N barf] snow.'\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary p. 206 s.v. vafr (NYB_vol2_glossary.txt l.3906)\", \"stance\": \"supports\", \"note\": \"'vafr [wpl] snow ... — Av. (1347) vafra-; MPrthPrs wfr (S, MHC); NP barf.'\"}]})\nm.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"barf «برف»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian barf 'snow' < MP wafr: initial w- > b- (the regular Persian change, cf. wahār > bahār) and metathesis of -fr > -rf (Hübschmann: 'Ap. fr ~ np. rf: barf Schnee = phl. vafr = zd. vafra-'). Dialects keep older shapes: Kurdish befr/berf, Mazandarani/Gilaki varf (Horn), Pashto wāwra. Sa'di's verse 'به برفاب رحمت مکن بر خسیس' uses the compound barfāb 'snow-water' (Borhan: برف + آب).\",\n \"derivation_fa\": \"«برف» در فارسی نو از پهلوی wafr است: w آغازی در فارسی به b بدل شده (مانند wahār > بهار) و خوشهٔ fr با قلب به rf درآمده است؛ هوبشمان همین را آورده است (fr پارسی باستان ~ rf فارسی نو). گویش‌ها صورت‌های کهن‌تری نگه داشته‌اند: کردی befr/berf، مازندرانی و گیلکی varf (هرن)، پشتو wāwra. بیت سعدی واژهٔ «برفاب» (برف + آب، به گفتهٔ برهان) را دارد. ادعای نورایی درست است.\",\n \"sources\": [W + \"برف\", \"https://vajehyab.com/moein/برف\"],\n \"ref_check\": [POK_WEP, {\"ref\": \"AEF:258\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Persian translation of Horn is not online; checked the original instead: HRN no. 202 (HRN.txt l.2163) 'barf Schnee. ... mäz. gel. Kaš. varf, verf. aw. vafra- Schnee; phlv. vafr. kurd. vafr, befir, bafer, berf; af. vāvra' — supports.\"}],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"no. 202, p. 47\", \"stance\": \"supports\", \"note\": \"'202. barf Schnee. ... aw. vafra- Schnee; phlv. vafr. kurd. ... berf; af. vävra Schneeflocke, Plur. Schnee'.\"},\n  {\"src\": \"HUB\", \"where\": \"p. 27 and p. 236 (HUB.txt l.6568, 9540)\", \"stance\": \"supports\", \"note\": \"'rf (barf Schnee = zd. vafra-)' and 'c) Ap. fr ~ np. rf: barf Schnee = phl. vafr = zd. vafra-'.\"},\n  {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/برف\", \"stance\": \"supports\", \"note\": \"'برف (بَ) [په.] (اِ.) آب منجمد ...' — Mo'in tags it Pahlavi.\"},\n  {\"src\": \"ARY\", \"where\": \"p. 123 s.v. برف (ocr/ARY/0123.png)\", \"stance\": \"supports\", \"note\": \"Avestan VAFRA, Pahlavi VAFR, Kurdish BERF, Pashto WAWRA, Sanskrit VAPATI, VAPRA, Latin VEPRES, OCS VEPRU, Latvian VEPRIS; refs Pokorny, MacKenzie (snow) 133, Buck 68-69 — follows Pokorny's grouping.\"},\n  {\"src\": \"BQT\", \"where\": \"p. 259 s.v. برفاب (BQT_v1_pages.txt leaf 480)\", \"stance\": \"partial\", \"note\": \"'برفاب ... معروف است که آب برف و آب سرد باشد'; Mo'in's footnote '۴ - مرکب از: برف + آب' — no etymology of barf itself.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"-\", \"stance\": \"silent\", \"note\": \"Cheung covers verbs only; no entry.\"}]})\nm.append({\n \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"wfr\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Sogdian wfr', wprh /wafra/ 'snow' (Gharib nos. 9931 Buddhist and 9980 Manichaean) is the exact Sogdian cognate of Av. vafra- and MP wafr, from Proto-Iranian *wafrah. The word is confirmed; as in node 1, only its ultimate derivation from *wep- is uncertain.\",\n \"derivation_fa\": \"سغدی wfr و wprh /wafra/ «برف» (قریب، شماره‌های ۹۹۳۱ و ۹۹۸۰) هم‌ریشهٔ دقیق اوستایی vafra- و پهلوی wafr و از ایرانی آغازین *wafrah است. خود واژه درست است، ولی چنان‌که دربارهٔ vafra گفته شد، پیوند نهایی آن با ریشهٔ *wep- قطعی نیست و با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Iranian/wafrah\"],\n \"ref_check\": [{\"ref\": \"SOD:401\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaves 468-470 (printed pp. ~401-404): '9931 wpr-h B wafra © Av. vafra © f. n. ... snow' and '9980 wfr' M wafra ©f. n. ... snow. GMS 311, 1175'.\"}],\n \"consulted\": [\n  {\"src\": \"SOD\", \"where\": \"nos. 9931, 9980\", \"stance\": \"supports\", \"note\": \"'wafra © Av. vafra ... snow'.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. vafr\", \"stance\": \"supports\", \"note\": \"'MPrthPrs wfr' — Nyberg lists the Manichaean form wfr alongside Pahlavi vafr.\"}]})\nm.append({\n \"id\": 5, \"lang\": \"Sanskrit\", \"words\": \"vapati\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sanskrit vápati 'strews, scatters, sows (seed); throws' (also vapra- 'mound, earthwork') from PIIr *(H)wap- < PIE *h₂wep(h₁)- 'to scatter, harass' (Wiktionary), Pokorny's uep-2 'to throw, strew'; cognate with Avestan vī-vāpat 'devastated' and Hittite ḫuwapp- 'to hurl, mistreat'.\",\n \"derivation_fa\": \"سنسکریت vápati «می‌افشاند، می‌پاشد (بذر)، می‌افکند» از هندوایرانی *(H)wap- و هندواروپایی *h₂wep(h₁)- «پراکندن» است و با اوستایی vī-vāpat «ویران کرد» و هیتی ḫuwapp- «پرتاب کردن» هم‌ریشه است. ادعای نورایی درست است.\",\n \"sources\": [W + \"वपति\"],\n \"ref_check\": [POK_WEP],\n \"consulted\": [\n  WLD_WEP | {\"stance\": \"supports\"},\n  {\"src\": \"BRT\", \"where\": \"col. 1345 s.v. vap-\", \"stance\": \"supports\", \"note\": \"'g. vap- V., nur mit vī ... vī-vāpat zerstören, verwüsten ... ai. vapati er wirft'.\"},\n  {\"src\": \"ARY\", \"where\": \"p. 123 s.v. برف\", \"stance\": \"supports\", \"note\": \"lists Sanskrit VAPATI, VAPRA under barf.\"}]})\nm.append({\n \"id\": 6, \"lang\": \"Latin\", \"words\": \"veprĕs\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Latin veprēs (usually plural) 'thornbush, briar, bramble' is a real word, but its etymology is unknown: Ernout-Meillet say 'sans étymologie', Wiktionary 'uncertain' (proposals *werp- 'bend' or a link with Russian čub), and Pokorny himself, on the very page Nourai cites, says that Latin vepres 'remains far off' (bleibt fern) from uep-2. Only Aryanpur repeats the connection. The arrow from Wep is therefore not supported.\",\n \"derivation_fa\": \"لاتینی veprēs «بوتهٔ خار، تمشک» واژه‌ای واقعی است، ولی ریشهٔ آن ناشناخته است: ارنو و میه آن را «بی‌ریشه‌شناسی» می‌دانند، ویکی‌واژه آن را نامعلوم می‌خواند و خود پوکورنی در همان صفحه‌ای که نورایی به آن ارجاع داده می‌گوید vepres از این ریشه «دور می‌ماند». تنها آریان‌پور این پیوند را تکرار کرده است. پس پژوهش امروزی ادعای نورایی را نمی‌پذیرد.\",\n \"sources\": [W + \"vepres\"],\n \"ref_check\": [{\"ref\": \"POK:1149\", \"status\": \"contradicts\", \"note\": \"POK_full.txt l.91053 under uep-2: 'remains far off Latin vepres briar (see II 56)' — Pokorny excludes vepres.\"}],\n \"consulted\": [\n  {\"src\": \"LAT\", \"where\": \"s.v. uepres (LAT.txt l.67342-67347)\", \"stance\": \"contradicts\", \"note\": \"'uepres, -ium m. et f. pl.: buisson d'épine ... Sans étymologie.'\"},\n  WLD_WEP | {\"stance\": \"silent\", \"note\": \"uep- 'werfen, streuen' (Bd. I 256) lists Ai. vapati and Av. vī-vāpat only; no vepres.\"},\n  {\"src\": \"ARY\", \"where\": \"p. 123 s.v. برف\", \"stance\": \"supports\", \"note\": \"lists Latin VEPRES under barf (following Pokorny's material without his reservation).\"}]})\n\nentries.append({\n \"entry\": 1, \"root\": \"Wep\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₂wep(h₁)- / *wep- 'to throw, strew, scatter' (Pokorny 1149 uep-2; WP I 256)\",\n \"note\": \"The root is real and Nourai's gloss ('to throw, spray ?') matches Pokorny's 'to throw, throw out' and Walde-Pokorny's 'werfen, streuen' (Wiktionary *h₂wep(h₁)- 'to scatter'). Sanskrit vapati is the core witness. The Iranian 'snow' word (Av. vafra-, MP wafr, NP barf, Sogd. wafra) is placed here by Pokorny with a question about the sense ('snowdrift?'); Buck calls its etymology unknown, so those arrows are plausible rather than certain; within Iranian the chain vafra- > wafr > barf is textbook (Horn 202, Hübschmann). Latin vepres is explicitly excluded by Pokorny and has no etymology in Ernout-Meillet: disputed. Extraction matches the printed page.\",\n \"note_fa\": \"ریشهٔ هندواروپایی *wep- (در نگارش امروزی *h₂wep(h₁)-) «افکندن، پاشیدن، پراکندن» در پوکورنی (ص ۱۱۴۹) و والده-پوکورنی (ج ۱، ص ۲۵۶) آمده و معنایی که نورایی داده درست است؛ گواه اصلی آن سنسکریت vapati است. واژهٔ ایرانی «برف» (اوستایی vafra-، پهلوی wafr، سغدی wafra) را پوکورنی با تردید زیر این ریشه آورده و باک ریشهٔ آن را نامعلوم می‌داند، پس این پیوند تنها پذیرفتنی است؛ ولی زنجیرهٔ vafra- > wafr > برف درون ایرانی بی‌گمان درست است. لاتینی vepres را خود پوکورنی از این ریشه جدا می‌داند و پژوهش امروزی آن را نمی‌پذیرد.\",\n \"sources\": [W + \"वपति\", W + \"برف\"],\n \"ref_check\": [POK_WEP],\n \"consulted\": [WLD_WEP, {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"No wep- root in the 1985 appendix (grep '^wep-' finds nothing).\"}, {\"src\": \"IEC\", \"where\": \"IEC.txt (grep uep-)\", \"stance\": \"silent\", \"note\": \"Mann has no uep- 'throw' entry.\"}, {\"src\": \"SYN\", \"where\": \"1.73 SNOW\", \"stance\": \"partial\", \"note\": \"'Av. vafra- ... Pahl. vafr, NPers. barf snow, etym.?'\"}],\n \"nodes\": m})\n\nout = {\"pdf_page\": 543, \"book_page\": 513, \"verified_by\": \"claude-opus-5\", \"verified_on\": \"2026-10-16\", \"entries\": entries}\njson.dump(out, open(\"/home/sfmqrb/git/rishe-private/data/verification/page-543.json\", \"w\", encoding=\"utf-8\"), ensure_ascii=False, indent=1)\nprint(\"ok\")\n"
}
```


### [2026-10-17T00:09:28.274Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/draft-543.py (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:09:39.100Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'EOF'\np='draft-543.py'; s=open(p).read()\ns=s.replace('entries = []\\n','def asc(r, src, where, stance):\\n    return {\"src\": src, \"where\": where, \"stance\": stance, \"note\": r[\"note\"]}\\n\\nentries = []\\n',1)\ns=s.replace('POK_WEN | {\"src\": \"POK\", \"where\": \"p. 1146-1147\", \"stance\": \"supports\"}','asc(POK_WEN, \"POK\", \"p. 1146-1147\", \"supports\")')\ns=s.replace('POK_WEN | {\"src\": \"POK\", \"where\": \"p. 1146\", \"stance\": \"supports\"}','asc(POK_WEN, \"POK\", \"p. 1146\", \"supports\")')\ns=s.replace('AHD_WEN | {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wen-1 §11\", \"stance\": \"supports\"}','asc(AHD_WEN, \"AHD\", \"Watkins 1985 s.v. wen-1 §11\", \"supports\")')\ns=s.replace('AHD_WEN | {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wen-1\", \"stance\": \"supports\"}','asc(AHD_WEN, \"AHD\", \"Watkins 1985 s.v. wen-1\", \"supports\")')\ns=s.replace('\"where\": \"p. 87 s.v. wafr (PHD_mackenzie.txt l.5136)\"','\"where\": \"s.v. wafr (PHD_mackenzie.txt l.5136)\"')\ns=s.replace('\"where\": \"Glossary p. 206 s.v. vafr (NYB_vol2_glossary.txt l.3906)\"','\"where\": \"Glossary s.v. vafr (NYB_vol2_glossary.txt l.3906)\"')\ns=s.replace('\"where\": \"no. 202, p. 47\"','\"where\": \"no. 202 (HRN.txt l.2163)\"')\ns=s.replace('\"where\": \"p. 27 and p. 236 (HUB.txt l.6568, 9540)\"','\"where\": \"HUB.txt l.5456, 6568, 9540\"')\ns=s.replace('\"where\": \"p. ~1505 s.v. uedh- (2) (IEC.txt l.19801)\"','\"where\": \"s.v. uedh- (2) (IEC.txt l.19801)\"')\nopen(p,'w').write(s)\nEOF\ngrep -n \" | {\" draft-543.py; python3 draft-543.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-543.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 543"
}
```


### [2026-10-17T00:09:39.993Z] TOOL RESULT

```
201:  WLD_WEP | {"stance": "supports"},
213:  WLD_WEP | {"stance": "silent", "note": "uep- 'werfen, streuen' (Bd. I 256) lists Ai. vapati and Av. vī-vāpat only; no vepres."},
ok
nodes verified: 16/16
node verdicts: {'plausible': 7, 'transcription_suspect': 1, 'confirmed': 6, 'disputed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'not_checked': 5, 'contradicts': 2, 'partial': 1}
books consulted: {'supports': 33, 'partial': 8, 'silent': 5, 'contradicts': 4} | by book: {'WLD': 7, 'KLN': 6, 'ARY': 4, 'MON': 3, 'SKT': 3, 'POK': 3, 'SYN': 3, 'BRT': 3, 'SOD': 3, 'LAT': 2, 'IEC': 2, 'HRN': 2, 'AHD': 2, 'NYB': 2, 'DEH': 1, 'PHD': 1, 'HUB': 1, 'BQT': 1, 'CHEUNG': 1}
```


## [2026-10-17T00:09:50.554Z] TOOL CALL #75: SubagentHandback

```json
{
 "message": "I verified PDF page 543 (book page 513) and wrote `/home/sfmqrb/git/rishe-private/data/verification/page-543.json`. `verify_check.py 543` shows 0 PROBLEM lines and all 16/16 nodes are covered. The Weqw entry is a redirect and was skipped.\n\n**Roots:** 2 confirmed.\n- **Wen** is PIE *wenh₁- \"to strive, wish, love\" (Pokorny 1146; Watkins wen-1).\n- **Wep** is Pokorny's uep-2 \"to throw, strew\" (Pokorny 1149), written *h₂wep(h₁)- today.\n\n**Nodes:** 6 confirmed, 7 plausible, 2 disputed, 1 transcription_suspect.\n\n**Disputed:**\n- **Wen #9, IE \"Wedh: to lead\"**: *wedʰ- \"lead, marry\" is a real root, but it is separate and does not come from *wen-. Pokorny (1115), Walde-Pokorny and Mann all list it on its own. Nourai seems to have taken it from Klein p.1687 s.v. *vaivode*, where the second part of that compound is traced to *wedh-. His cited page, Klein p.1697 (*venery*), says nothing about *wedh-.\n- **Wep #6, Latin veprēs \"bushy plant\"**: on the very page Nourai cites, Pokorny says vepres \"remains far off\" from this root. Ernout-Meillet give it \"sans étymologie\" and Wiktionary calls it uncertain. Only Aryanpur repeats the link.\n\n**Transcription_suspect:**\n- **Wen #2, \"Vennezuela\"**: the book itself prints the double n, so this is Nourai's misprint for Venezuela (error_in: book). The page image is copied to `data/verification/sources/refs/ocr/BOOK/543.png`. The box is also labelled French, but Venezia is Italian and Venezuela is Spanish (from Italian Veneziola, \"little Venice\").\n\n**Other points:**\n- In Wen #10, \"vadu 2: to lead\" is really Avestan vaδū- \"woman, wife\". The Avestan verb root is vad-. I marked the node plausible because vādayeiti \"leads\" is confirmed (Bartholomae col. 1343–1345).\n- The Iranian \"snow\" words (Avestan vafra-, Sogdian wfr) are plausible rather than confirmed. Pokorny puts them under this root with a question mark, and Buck says their etymology is unknown. Within Iranian, the chain vafra- > Pahlavi wafr > Persian barf is confirmed (Horn 202, Hübschmann, MacKenzie, Nyberg).\n\n**Extraction errors:** none. The JSON matches the printed page."
}
```


### [2026-10-17T00:09:50.863Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
