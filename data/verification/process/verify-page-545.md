# Verification process log — verify-page-545


## [2026-10-17T00:00:15.379Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 545 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-545.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-545.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-545.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 545` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.433Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:24.224Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:24.269Z] TOOL RESULT

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


## [2026-10-17T00:00:24.728Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-545.txt"
}
```


### [2026-10-17T00:00:24.763Z] TOOL RESULT

```
1	=== PDF page 545 (book page 515) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wer 2, Werb, Werg 3, Wermi, Kwermi, Werp, Wert, Wrei : to turn, bend  (refs POK:1142-1157)  PART 2
4	#1 (parent #0) [Sanskrit] refs=POK:1154 | varj : to turn around
5	  #2 (parent #1) [Persian] refs=BQT:258,2273; HRN:242 | varğ «ورغ» : a dam made to turn water around | extra: برغ ، برغاب
6	#3 (parent #0) [Avestan] refs=KLN:1752,1755; POK | urvisyeiti : turns ; varep : to mark ; a-vareta : a valuable object
7	#4 (parent #0) [Latin] refs=AHD | vetere : to turn ; vergere : to turn ; vermis : worm
8	  #5 (parent #4) [French] refs=None | vermicelle
9	    #6 (parent #5) [Persian] refs=MON:5011 | vermîšel «ورمیشل» : vermicelli
10	  #7 (parent #4) [English] refs=AHD | adverse, anniversary, convert, divert, invert, version, versus, universe, university, vertebra, vice-versa, vertical, transverse, verse, verge, vermicelli, vermouth
11	#8 (parent #0) [Avestan / Old Persian] refs=POK:649 | kermi, kerma, karem : worm
12	  #9 (parent #8) [Persian] refs=BQT:1625 | kerm «کرم» : worm
13	#10 (parent #0) [Sanskrit] refs=POK:649 | krmi : worm ; krmi-ja : made from worms (a red dye) ☞Gene 1
14	  #11 (parent #10) [Persian] refs=MON:2663 | qermez «قرمز» : red
15	  #12 (parent #10) [Sogdian] refs=SOD:203 | kyrm : worm, snake
16	    #13 (parent #12) [Arabic] refs=BQT:1527 | qermez : red
17	      #14 (parent #13) [English] refs=AHD:205,303 | kermes, carmine, crimson
18	#15 (parent #0) [Indo-European] refs=IEC:1596 | Wropal : club, mace
19	  #16 (parent #15) [Persian] refs=IEC:1596; MON:3109 | kŭpâl «کوپال» : mace, club | extra: گوپال
20	  #17 (parent #15) [Greek] refs=IEC:1596; DEW:435; POK:1156 | rhopalon : club, mace
21	
```


## [2026-10-17T00:00:25.258Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-545.json"
}
```


### [2026-10-17T00:00:25.307Z] TOOL RESULT

```
1	{
2	  "pdf_page": 545,
3	  "book_page": 515,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wer 2, Werb, Werg 3, Wermi, Kwermi, Werp, Wert, Wrei",
8	        "lang": "Indo-European",
9	        "refs": "POK:1142-1157",
10	        "gloss": "to turn, bend"
11	      },
12	      "part": 2,
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Sanskrit",
18	          "refs": "POK:1154",
19	          "words": [
20	            {"translit": "varj", "gloss": "to turn around", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "BQT:258,2273; HRN:242",
30	          "words": [
31	            {"translit": "varğ", "gloss": "a dam made to turn water around", "script": "ورغ"}
32	          ],
33	          "script_extra": "برغ ، برغاب",
34	          "note": null,
35	          "quote": {"text": "دل برد و مرا نیز بمردم نشمرد - گفتارچه سوداست که ورغ آب ببرد", "poet": "Farrokhî"}
36	        },
37	        {
38	          "id": 3,
39	          "parent": 0,
40	          "lang": "Avestan",
41	          "refs": "KLN:1752,1755; POK",
42	          "words": [
43	            {"translit": "urvisyeiti", "gloss": "turns", "script": null},
44	            {"translit": "varep", "gloss": "to mark", "script": null},
45	            {"translit": "a-vareta", "gloss": "a valuable object", "script": null}
46	          ],
47	          "note": null,
48	          "quote": null
49	        },
50	        {
51	          "id": 4,
52	          "parent": 0,
53	          "lang": "Latin",
54	          "refs": "AHD",
55	          "words": [
56	            {"translit": "vetere", "gloss": "to turn", "script": null},
57	            {"translit": "vergere", "gloss": "to turn", "script": null},
58	            {"translit": "vermis", "gloss": "worm", "script": null}
59	          ],
60	          "note": null,
61	          "quote": null
62	        },
63	        {
64	          "id": 5,
65	          "parent": 4,
66	          "lang": "French",
67	          "refs": null,
68	          "words": [
69	            {"translit": "vermicelle", "gloss": null, "script": null}
70	          ],
71	          "note": null,
72	          "quote": null
73	        },
74	        {
75	          "id": 6,
76	          "parent": 5,
77	          "lang": "Persian",
78	          "refs": "MON:5011",
79	          "words": [
80	            {"translit": "vermîšel", "gloss": "vermicelli", "script": "ورمیشل"}
81	          ],
82	          "note": null,
83	          "quote": null
84	        },
85	        {
86	          "id": 7,
87	          "parent": 4,
88	          "lang": "English",
89	          "refs": "AHD",
90	          "words": [
91	            {"translit": "adverse, anniversary, convert, divert, invert, version, versus, universe, university, vertebra, vice-versa, vertical, transverse, verse, verge, vermicelli, vermouth", "gloss": null, "script": null}
92	          ],
93	          "note": null,
94	          "quote": null
95	        },
96	        {
97	          "id": 8,
98	          "parent": 0,
99	          "lang": "Avestan / Old Persian",
100	          "refs": "POK:649",
101	          "words": [
102	            {"translit": "kermi, kerma, karem", "gloss": "worm", "script": null}
103	          ],
104	          "note": null,
105	          "quote": null
106	        },
107	        {
108	          "id": 9,
109	          "parent": 8,
110	          "lang": "Persian",
111	          "refs": "BQT:1625",
112	          "words": [
113	            {"translit": "kerm", "gloss": "worm", "script": "کرم"}
114	          ],
115	          "note": null,
116	          "quote": null
117	        },
118	        {
119	          "id": 10,
120	          "parent": 0,
121	          "lang": "Sanskrit",
122	          "refs": "POK:649",
123	          "words": [
124	            {"translit": "krmi", "gloss": "worm", "script": null},
125	            {"translit": "krmi-ja", "gloss": "made from worms (a red dye)", "script": null, "see": ["Gene 1"]}
126	          ],
127	          "note": null,
128	          "quote": null
129	        },
130	        {
131	          "id": 11,
132	          "parent": 10,
133	          "lang": "Persian",
134	          "refs": "MON:2663",
135	          "words": [
136	            {"translit": "qermez", "gloss": "red", "script": "قرمز"}
137	          ],
138	          "note": null,
139	          "quote": null
140	        },
141	        {
142	          "id": 12,
143	          "parent": 10,
144	          "lang": "Sogdian",
145	          "refs": "SOD:203",
146	          "words": [
147	            {"translit": "kyrm", "gloss": "worm, snake", "script": null}
148	          ],
149	          "note": null,
150	          "quote": null
151	        },
152	        {
153	          "id": 13,
154	          "parent": 12,
155	          "lang": "Arabic",
156	          "refs": "BQT:1527",
157	          "words": [
158	            {"translit": "qermez", "gloss": "red", "script": null}
159	          ],
160	          "note": null,
161	          "quote": null
162	        },
163	        {
164	          "id": 14,
165	          "parent": 13,
166	          "lang": "English",
167	          "refs": "AHD:205,303",
168	          "words": [
169	            {"translit": "kermes, carmine, crimson", "gloss": null, "script": null}
170	          ],
171	          "note": null,
172	          "quote": null
173	        },
174	        {
175	          "id": 15,
176	          "parent": 0,
177	          "lang": "Indo-European",
178	          "refs": "IEC:1596",
179	          "words": [
180	            {"translit": "Wropal", "gloss": "club, mace", "script": null}
181	          ],
182	          "note": null,
183	          "quote": null
184	        },
185	        {
186	          "id": 16,
187	          "parent": 15,
188	          "lang": "Persian",
189	          "refs": "IEC:1596; MON:3109",
190	          "words": [
191	            {"translit": "kŭpâl", "gloss": "mace, club", "script": "کوپال"}
192	          ],
193	          "script_extra": "گوپال",
194	          "note": null,
195	          "quote": {"text": "وزو باد بر سام نیرم درود - خداوند شمشیر و کوپال و خود", "poet": "Ferdowsî"}
196	        },
197	        {
198	          "id": 17,
199	          "parent": 15,
200	          "lang": "Greek",
201	          "refs": "IEC:1596; DEW:435; POK:1156",
202	          "words": [
203	            {"translit": "rhopalon", "gloss": "club, mace", "script": null}
204	          ],
205	          "note": null,
206	          "quote": null
207	        }
208	      ]
209	    }
210	  ]
211	}
212	
```


## [2026-10-17T00:00:30.061Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','WLD','AHD','IEC','SYN','BQT','HRN','HUB','MON','ARY','KLN','SOD','DEW','BRT','KNT','CHEUNG','SKT','PHD','NYB','FVQ','LKT']:\n  v=d.get(k,{}); print(k,v.get('local_file'),v.get('page_offset'),v.get('lookup_hint','')[:100])\n\"; command ls sources/refs | head -100"
}
```


### [2026-10-17T00:00:30.430Z] TOOL RESULT

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
POK /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177
WLD ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it c
AHD /home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...i
IEC /home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n 
SYN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discu
BQT ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-bl
HRN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or gr
HUB /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part 
MON ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin t
ARY ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] printed page = pdf page + 1 Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page cita
KLN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; d
SOD ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'] printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~
DEW None None 
BRT /home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration i
KNT /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part
CHEUNG None None 
SKT /home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.
PHD /home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and glos
NYB /home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at lin
FVQ ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt'] printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p
LKT /home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but N
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


## [2026-10-17T00:00:41.041Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; command ls page-54*.json page-53*.json 2>/dev/null; sed -n 1,200p /home/sfmqrb/git/rishe-private/tools/verify_check.py | grep -n -i -E 'problem|required|min|len' | head -60"
}
```


### [2026-10-17T00:00:41.394Z] TOOL RESULT

```
page-530.json
page-531.json
page-532.json
page-533.json
page-534.json
page-535.json
page-536.json
page-537.json
page-538.json
page-53.json
page-54.json
22:    missing_pages, problems = [], []
37:        need = sum(len(e["nodes"]) for _, e in entries)
46:            problems.append(f"page {pg}: invalid JSON ({ex})")
52:                problems.append(f"page {pg}: entry {i} ({e['root']['name']}) missing")
56:                problems.append(f"page {pg}: entry {i} root verdict {rv!r} invalid")
65:                    problems.append(f"page {pg}: entry {i} ({e['root']['name']}) node #{n['id']} missing")
69:                    problems.append(f"page {pg}: entry {i} node #{n['id']} verdict {nv!r} invalid")
74:                    problems.append(f"page {pg}: entry {i} node #{n['id']} has no derivation")
88:        print(f"pages without verification ({len(missing_pages)}):", " ".join(map(str, missing_pages)))
89:    for p in problems:
90:        print("PROBLEM:", p)
94:    return 1 if problems else 0
```


## [2026-10-17T00:00:44.252Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat /home/sfmqrb/git/rishe-private/tools/verify_check.py | sed -n 20,95p; python3 -c \"\nimport json;d=json.load(open('page-538.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-10-17T00:00:44.684Z] TOOL RESULT

```
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


## [2026-10-17T00:01:05.506Z] TOOL CALL #7: Bash

```json
{
 "command": "command ls /home/sfmqrb/git/rishe-private/site/pages/545.jpg; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 545 -l 545 -r 200 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg545 && echo ok"
}
```


### [2026-10-17T00:01:06.591Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/site/pages/545.jpg
ok
```


## [2026-10-17T00:01:11.909Z] TOOL CALL #8: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg545.png"
}
```


### [2026-10-17T00:01:12.428Z] TOOL RESULT

```

```


## [2026-10-17T00:01:12.423Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-17T00:01:18.195Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 -c \"\nfrom PIL import Image; im=Image.open('pg545.png'); im.crop((350,960,900,1280)).save('crop545a.png')\""
}
```


### [2026-10-17T00:01:18.624Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image; im=Image.open('pg545.png'); im.crop((350,960,900,1280)).save('crop545a.png')
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-17T00:01:21.638Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 545 -l 545 -r 300 -png -singlefile -x 450 -y 1350 -W 900 -H 450 /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf crop545a && echo ok"
}
```


### [2026-10-17T00:01:22.175Z] TOOL RESULT

```
ok
```


## [2026-10-17T00:01:23.919Z] TOOL CALL #11: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/crop545a.png"
}
```


### [2026-10-17T00:01:23.936Z] TOOL RESULT

```

```


## [2026-10-17T00:01:29.178Z] TOOL CALL #12: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg545.png /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/545.png; cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^Root / lemma: (u̯er-|uer-|u̯erǵ|uerĝ|u̯erg|ueri|u̯ert|uert|u̯erp|uerp|u̯erb|uerb|u̯rei|urei|kʷr̥mi|kwr|u̯r̥mi|ur̥mi)\" POK_full.txt | head -40"
}
```


### [2026-10-17T00:01:29.500Z] TOOL RESULT

```
22997:Root / lemma: uer-3. E. uer-gh- {* suerg^h^: "to turn, press, strangle' < [common Latin 
74446:Root / lemma: uer-3. E. uer-gh- {* suerg^h^: "to turn, press, strangle' < [common Latin 
91293:Root / lemma: uer-12{*huer-12) 
91314:Root / lemma: uer-13{*huer-13) 
91411:Root / lemma: uer-2{*huer-2) 
91474:Root / lemma: uer-3{*huer-3) 
91513:Root / lemma: uer-3. B. uer-b-3in6 uer-k:i^-{*huer-3) 
91556:Root / lemma: uer-3. C. u(e)r-ed- {*huer-3) 
91578:Root / lemma: uer-3. D. uer-g- {*huer-3) 
91609:Root / lemma: uer-3. E. uer-gh-{*hues-3) 
91686:Root / lemma: uer-3. F. uer-k- {*hue-3) 
91713:Root / lemma: uer-3. G. uer-p-, ur-ep-{*huer-3) 
91760:Root / lemma: uer-3. H. uer-t- {* huer-3) 
91827:Root / lemma: uer-3. I. ur-ei- a) urei-n-: {* huer-3) 
91846:Root / lemma: uer-S. I. ur-e/-. p) urizd- {* huer-3) 
91929:Root / lemma: uer-3. I. ur-ek e) ureip-, unp-{*huer-3) 
91949:Root / lemma: uer-S. I. ur-ei-. Q ureit- {* huer-3) 
91970:Root / lemma: uer-4 {*huer-4) 
91991:Root / lemma: uer-5 {* huer-5) 
92098:Root / lemma: uer-6{^huer-6) 
92155:Root / lemma: uer-7{*huer-7) 
92218:Root / lemma: uer-8{*huer-8) 
92275:Root / lemma: uer-9. Ueru-s{*huer-9) 
92327:Root / lemma: uer-(e)na{*huer-(0)ri) 
93355:Root / lemma: ureik-, uereik- {*hauerk^
```


## [2026-10-17T00:01:31.059Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91474,91612p POK_full.txt; sed -n 91713,91830p POK_full.txt | cut -c1-400"
}
```


### [2026-10-17T00:01:31.475Z] TOOL RESULT

```
Root / lemma: uer-3{*huer-3) 

Meaning: to turn, bend 

Note: here perhaps die under uer-1 mentioned baltoslavischen words. Sonst only 

abstraction for derivatives and Root extensions. 

Page(s):1152 

Root/ lemma: uer-3. A. ufmi-s, ufmo-s{*huer-3) 
Meaning: worm 

Material: Latin i/e/777/s (from *vormis, *urmis)\ Gothic waurmsm. "snake'. Old Icelandic 
ormr. Old English wyrm. Old Frisian wirm diS. " worm ', Old Saxon Old High German wurm 
m. ds.; Balto-Slavic *uarma- m. "worm, insect' in Lithuanian i/a/777as "insect, mosquito ', Old 
Prussian wormyanVok. 'red' ("wurmfarben'), ablaut. urm/nan6s., Slavic vbrmbjen. 
"Insekten' in Old Russian vermije, ukrain. vermany/" red'; with same meaning Old Frisian 
worma^ Purpur', Old High German gi-uurmofxed gefarbt'. Old English wurma'C(\. " 
Mediterranean sea snail, snail emitting purple dye, woad, type of plant, Purpur', out of it 
borrowed abret. uurm ^dark', cymr. ^tv/777 "dark(blue)', from which again Old Irish gorm ds.; 
gr. PN Fap|jixo(; and p6|J0(; (Aeolic *Fp6piO(; from *urmos) "Holzwurm' Hes.; compare from 



the g- or ^/>extension in the same meaning Middle Irish frigei., Nom. PI. frigit 

Tleischwurm' {*urg{h)-ntes), cymr. PI. gwra/nt^Wurmer in the skin' ( *urg(h)ntoi), gallo- 

Latin brigantes {*vrigantes) 'WiJrmer in eyelid'; Middle Breton gruech, nbret. grec'hi. 'mite' 

(from brit. *vrigga, with intensification). 

References: WP. I 271, WH. II 760, Trautmann 342 f., Vasmer 1, 189, Frisk 501; 

See also: rhyme word to kymi-, above S. 649. 

Page(s):1152 

Root / lemma: uer-3. B. uer-b-3in6 uer-k:i^-{*huer-3) 

Meaning: to turn, bend 

Material: Gr. pa|jvo(; "a kind of briar, Rhamnus paliurus L.' (*pap-vo(;, *urb-nos), pa(35o(; 

"rod, horsewhip, staff, Aeolic Glosse pupov "sniKapTTE^'; 

Latin PI. verbera, -i//77'Ruten, Rutenschlage, ZiJchtigung' {verberare^'^Wh Ruten stroke, 
hit'), verbena^ ^\Q leaves and zarten branch of Lorbeers, Olbaums, the Myrte etc. as 
sacred herbs ' {*uerbes-na; compare den in subverbustus \he basic liegenden -es-stem); 

Lithuanian vifbasm. "rod, horsewhip', vifbalas^Vrdx^ Stabchen, knitting needle', virb'inis' 
loop, noose, snare ', Latvian i///t's"Stockchen', virba^ shaft, pole'. Old Church Slavic 
*vrbba^ willow ', russ. i/eAi&a "Weidenzweig' (with the accentuation of Akk. Sg.; russ. dial. 
verba\\2iS die older Slavic accentuation), KC»/'di&a"Zirkelschnur, Zirkelbrett', voroby^ thread 
reel, thread coil '; 

Gothic wafrpan^ihrow' ("*turn'). Old Icelandic i/eAyOa "throw' and "ein texture anzettein, 
die chain shave, shear', aldri orpinn^oi kWer bent', verpask^vor Hitze shrivel up, shrink'. 
Old English weorpan. Old Saxon werpan. Old High German werfan 'throw\ Old Icelandic 
varpu. "das Werfen, Zettel, Einschlag of texture ', Old Saxon warp. Old High German warf. 
Old English wearpu. ds.; 

die Latin and Balto Slavic words (an sich also papvoc;) could also Indo Germanic *ueib^- 
fortsetzen; auf ein solches could attributed become die auf nasalized l/''"<5/wbh- indicating 
^t\x(^OQ, TO GTopa, ri pi<; Hes., to pap(po(; "krummer Vogelschnabel', probably hybridization 
from pspcp- and pacp-), papcpn "gebogenes knife', pafjcpi(; "gebogener hook', papi|j6(; 
"gebogen'. Low German ty/'^/r7/r7e//7"zerknullen, zerknittern'; 

nasalized uremb-:gr. psppw " turn, twist, rotate in Kreise herum', Med. " turn, twist, 
rotate myself herum, treibe herum', p6ppO(; (Attic puiJpO(;) "kreisformige movement, 
Schwung, Kreisel', cymr. gwrym^hem, suture' {*urembo-)\ Middle Low German wrimpen, 
wrempen ^ {das iace) zusammenziehen, rijmpfen', wremp/ch 'd\stortus, verdreht, rijmpfig'. 



wrampachtich^\N\v\6e6, crooked', holl. wrimpen, iire/77yOe/7"distorquere' (besides Germanic 
*hremp-an6 remp-. Old High German h rim p fan, rimpfan 'rumpfen). 

References: WP. I 275 f., WH. II 756. 
Page(s):1153 

Root / lemma: uer-3. C. u(e)r-ed- {*huer-3) 

Meaning: to bend down, to sway 

Material: Gr. pa5iv6(;, Aeolic ppa5ivo(; (i.e. Fpa5ivo(;) "schwank, slim, agile', po5av6(; 

"schwank', po5avr| (by Hes. pa5avr|) "the gedrehte filament, Einschlag', pa5aA6(; " slim, 

aufgeschossen'; 

Gothic wrafon' wander, reisen', isl. rata' wander, umherschweifen, reisen, meet, find'. 
Middle High German razze/n^turn', Old High German /"az/'vagans, rapax'; Lithuanian 
randu, radau, A^sZ/'find'Cin-venire'); Latvian ruodu, rast6s.; 

suffixales -st- (Krahe PBB 71, 242) show Old Icelandic /ps/'Wasserwirbel', Old English 
wrsestlian. Middle Low German M/c»/-s/e/e/7 'wrestle, struggle' (about das as ' twiddled, 
twisted, rotated, revved, revolved, walzig' partly here or to "Ve/Y-gestellte Old High 
German wurst. Modern High German Wi/As/^ sausage 's. Kluge-Gotze''6 288). 

References: WP. I 273 f., Trautmann 236. 
Page(s): 1153-1154 

Root / lemma: uer-3. D. uer-g- {*huer-3) 
Meaning: to turn 

Material: Old Indie vrnakti, varjat/"\i\/en6et, dreht', K/7//7a- "crooked, rankevoll' (rather with g- 
forms to i//77d7/"wehrt', s. t/e/'-"umschlieften'); Latin vergd-ere's\c\r\ neigen'; verm/nan. PI. 
' the stomach ache ' {* uerg-mena); holl. werken^s\c\\ werfen, krummziehen (from wood)', 
Swedish i/^A/re/? "windschief through dampness '; Latvian sa-vergV shrivel, shrink due to 
excess dryness, wrinkle up '; Old Church Slavic vrtgg, ures//" throw' russ. ot-vergnut' 
"ablehnen' etc.; compare under S. 1181; 

cymr. gwra/nt'Wurmer' etc. (see above S. 1 152) kann gor gh in root final sound have. 

Nasalized *ureng-: 

Old English wrenc{*urongi-) '( gyration). Modulation the voice, Kunstgriff, 
insidiousness', wrencan^iwcu, coil, cheat, deceive', i4//7/7c/e "wrinkle'. Old High German 



b/renk/f luxated', Middle High German /'e/7/re/7"dreliend zielien', Middle High German 
ranc, PI. renkem. ' gyration, curvature, schnelle Bewegung', Modern High German 
verrenken, /?a/7/r'Ranke', New Swedish i//7/7/r5 'verstauchen'. New Norwegian vrinke 
"abgeschmackt become'; Lithuanian rengtis^be clumsy bucken, crook', rangus^ ductile ', 
rangstus^ hasty', n'nga'e\n crooked Dasitzender' ; perhaps Old Indie abhi-vlaiiga-vn. 
Tangnetz', abhi-vlag-' capture '; under the imagining of NasenriJmpfens kann angereiht 
become Latin ringor {rictus theu with analog, /for e) 'den Mund aufsperren and die Zahne 
fletschen, sich argern'. Church Slavic /'i^^/7(?//"hiscere', rggh^ derision, ridicule' etc. 

References: WP. I 271 f., WH. II 436, 752 f., Vasmer 2, 543 f. 
Page(s):1154 

Root / lemma: uer-3. E. uer-gh-{*hues-3) 

Meaning: to turn, press, strangle 

Root / lemma: uer-3. G. uer-p-, ur-ep-{*huer-3) 

Meaning: to turn, wind 

Material: Old Indie varpas-n. "artifice, Kunstgriff', originally "* curvature, Winkelzug'; 

gr. panTU) (*Fpaniu), *urp-) "nahe together, flicke', pani(; "needle' (also pa(pi(;, as pacprj " 
suture' with cp probably through derailment); psnu) "biege myself, schlage after a side 
from', ponn "skin rash, leaning, tendency', avTipporroq "gleichwiegend', apcpippsnnc; "sich 
auf beide Seiten neigend', KaAa-upoijj (KoAa-Fpon-) "shepherd's crook; crosier' 

Maybe alb. ke-rrabe' shepherd's crook; crosier'. 

Gr. 5£upo (*5£-Fpon) actually "here gewendet!', ponaAov "Wurfstab, cudgel, club', 
ponrpov "club, mace, joint, TiJrklopfer, Stellholz in a dragnet ', pani(; "rod, staff' (perhaps 
also pap5o(; with p from p, see above *uerb-)\ lengthened grade pwnsc; PI. " branch, 
shrubbery, shrubbery, bush', pwnriiov "shrubbery, bush, thicket '; 

alb. i//'ajO"schnellergait '; 

Latin repens^suddeu (*den Ausschlag giving)'; 

maybe alb. r/ep'pee\, skin' 

perhaps i/e/O/'es (mostly PI.) "briar, Dorngebusch', if dissimil. from *vrepres, and verpa 
"das mannliche limb, member', if actually "*rod', from * uorpa or * urpa {: panic;), verpus^\he 
Beschnittene'; 

Old Icelandic orf. Old High German worf. Middle High German {sensen)worp. Modern 
High German dial, worb "Sensenstiel' (from "*rod'; ablaut equally with pamc, and perhaps 
Latin verpa); Danish dial, vravle^ coil, maunder, drivel ', Middle English wrappen^\N\cke\Vi\ 



Lithuanian verpiu, i/e/T?// (Latvian verpt) "spinnen', va rpste ' co\\, spool, spindle', Latvian 
varpste6s., i/e/77e//" whirlwind', Lithuanian v/rp/'u, -eti, virpu, -//"waver, tremble, quiver', 
Kz/'yOi/Zj/s 'Zittern the Glieder', and with the development to 'drehend toss, fling, throw, 
release, let go, free, set free ', Old Prussian etwierpV release, let go, free, set free ' 
("*drehend toss, fling'), a/7^//'yO/s"Wasserablaft, Flutrinne', c/'5i/yaM///77S "Aderlassen', 
/OC»i//e/'yD/'freilassen', pouirps^ixee'; russ. -Church Slavic vtrpu, vbrpst/^re'\Q>e, pfliJcke, 
raube'; changing through ablaut Lithuanian varpas' ear' ('*das GepfliJckte'), Latvian varpa 
6s., Lithuanian i/a/XT/Z/'stochern'; formal comparable Czech vrapa, Kra/O "wrinkle', sloven. 
\/rapa, /'^o^'Hautrunzel', Lower Serbian ropa, Upper Serbian (w)ropa^ crease '. 

References: WP. I 276 f., WH. II 425 f., 754, Trautmann 353, Vasmer 1, 189, 229. 
Page(s):1156 

Root / lemma: uer-3. H. uer-t- {* huer-3) 
Meaning: to turn, wind 

Grammatical information: causative-iterative uorteid 

Material: Old Indie themat. present vartati(-te)^ 6re\\{\ Med. "dreht sich, rollt, verlauft', 
Avestan varat- 'sich wenden'; other Prasentia Old Indie vavartti, vartti, causative vartayati^ 
places in drehende Bewegung' (= Gothic fra-wardjan. Old Church Slavic vratiti, Lithuanian 
vartyti), vartman-n. "pathway', vartana-n. "das Drehen', by den Mitanni-lndern a/ka- 
vartanaetc. "a circle (the racecourse)'; vartu/a-' round ', i/5/Yi//a"Spinnwirter (: Middle 
High German wirtel), vrtta-^ twiddled, twisted, rotated, revved, revolved, round ' (= Latin 
vorsus, virsus, Lithuanian v/rsfas etc.), vrtt/-t "das Rollen, kind of, nature' (= Latin versi-o. 
Old Church Slavic vrbstb), i/a/Y/^Gerolltes'; ein present *vrnatmi\s because of vrnta-m. 
"Blattstiel', vrntaka- m. "Eierpflanze' anzunehmen; vrkkau {* vrtka-) " kidneys ' (actually ' 
bulge; bead; lip; torus; wreath; roll; bu\b'), kvesiau V9ra5ka- varalka- 6s., 

compare Pahlavi gurtak, npers. gurda^V\6v\ey' from Old pers. *vrt(a), 

gr. paravn (Fpar- from *urt-) " mixing spoon ', Pparavriv Topuvr|v 'HAeToi Hes., porapia 
(poT- Aeolian; -ravia?) Topuviov Hes.; appaTO(; "hard, not drehbar' (*a-FpaT-0(;); 

Latin i/e/Yo (neologism to replacement of old Kausativs?), vertT, i/e/'5i//77"kehren, turn', 
Deponens revertor; vortex, i/e/feA'" whirl, Scheitel', versus, adversus ' gegen' (/c>-participle), 
versus, -usm. "line, row, furrow'; Umbrian kuvertu, covertu^covwerWib', trahvorfi 
transverse', Latin versi-on-, Oscan Dat. Fspaopsi ein Gotterepithet; Oscan Umbrian 
vorsus Q\x\ piece of wood as field measure is ein Terminus the rom. Siedler in Campanien 
(M. Leumann); compare Old Irish forrach^eiu piece of wood as field measure '; 



Venetic goddess l//-c»/5/7"Wenderin, Geburtsgottin' (Vetter Gl. 20, 72); 

Old Irish ad-ferta ' aversatur' , adbart' adversanus', ablaut. o'/Vo/Y- "diffuse, einschenken' 
(compare French verse/), Middle Irish fertasi. " shaft, spindle, earthwall' (newer fersat), 
cymr. gwerthyd^ spindle', acorn. gurhthit<^\. "fusus', abret. PI. guirtitou <^\. "fusis'. Middle 
Breton guersit6s.\ root nouns as Adverb *urt. Old Irish preposition fri, proverb frith-, 
mcymr. gwrth, ncymr. wrth, corn. orth, bret. o^z'gegen' (zur basic form s. Thurneysen 
Grammar S. 515, Jackson Language and History S. 337); cymr. gwerthu^ sell ', corn. 
gwerthe, bret. gwerza diS. (but cymr. gwerth'pnce' kann Old English loanword sein); 

Gothic etc. wairt^an. Old High German werdan ^become' ("to turn'); Gothic fra-wardjan. 
Old High German frawarten^s'poW' (causative to frawa/rf^an'be destroyed, perish', actually 
"eine Wendung zum evil, wickedness nehmen'), Gothic etc. -wafrt^s. Old High German - 
wert. Modern High German -warts ^\no\\\v\ gewendet'; perhaps Gothic etc. wairl=>s. Old High 
German wert, Subst. ' value, worth, price' (compare Old Irish frith-, Latin i/OAS^s'gegen' 
together with dem relationship from Old Indie /0/'a//"gegen': Latin pretium^as Gegenwert 
dienender price)' Old High German wurtlate, destiny' {*urt/- " turn '); 

Balto-Slavic * uert/o^ wende, turn, twist, rotate ' (older *uertd) in Lithuanian verciu, vefsti, 
Latvian versu, verst^ turn, kehren', Intransitiv Lithuanian virstu{*vrt-std), i//?5//"umfallen, 
fall, sich in etwas transform'. Iter. Ka/Y/Z/'continual turn ', Old Prussian nvrs/'wird'; Slavic 
*vbrtjg, *vbrtet/"\n Old Church Slavic i/Ab/eZ/s^'nEpianaaGai', Iter. vrat/t/sg'oipt(pzoQa\', 
russ. -Church Slavic vreteno^ spindle'('V^/Ye/7c»-n.), Old Church Slavic vremg^Wme' {*uert- 
menn.), Lithuanian i/a^s/as'Pflugwende', compare Old Prussian a/nawarst^ once'; Balto- 
Slavic *uirstai. "Wende' in Old Church Slavic urbs/a 'nAiKia', russ. versta^ow, 
Lebensalter, Worst', compare die participle Lithuanian vfrstas. Latin versus. Old Indie vrtta- 
and Latin versus, -Js "furrow, line, row'; Old Indie vrtta-n. " way of life, lifestyle, 
Benehmen'; Balto-Slavic *uirsti-\. 'kind of in russ. -Church Slavic stvbrstb "gleiches age, 
pair', slov. vrst^ow, kind of, compare Lithuanian Infin. K/?5/A0ld Indie vrtt/'-t see above. 

Tocharian A wart- "throw', B wrattsa/ ^gegen' {*wart, *urt), ye/Ye/' "Radkranz', A werkant, 
B Obi. yerkwantai {yertwantai), Pedersen Tocharian 235. 

References: WP. II 274 f., WH. II 763 ff., Trautmann 354 f., Vasmer 1, 189, 190, 229, 230, 
235, Frick151. 
Page(s): 1156-1158 

Root / lemma: uer-3. I. ur-ei- a) urei-n-: {* huer-3) 
Meaning: to be confused; to clench the teeth
```


## [2026-10-17T00:01:35.493Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"urva[eē]s|urvis\" POK_full.txt | head; grep -n -E \"^Root / lemma: k.?r.?mi|^Root / lemma: kur?mi|kʷrmi|k\\^r?mi\" POK_full.txt | head; grep -n -i \"Page(s):649\" POK_full.txt"
}
```


### [2026-10-17T00:01:35.953Z] TOOL RESULT

```
23200:Nom. P\.durys), Latvian dur/s, durvis. Old Prussian daurisi. PI. 'door' {a u error); however, 
91881:Material: Avestan urvisyeiti {*vrisyati) 'wendet sich, dreht sich', Kaus. urvaesaye/t/'\Nen6et, 
91883:dreht', urvaesa- m. ' gyration ' (= gr. poiKOc;, Dutch wreeg); Old Indie ures/- 'Wasserwirbel';
```


## [2026-10-17T00:01:38.014Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91846,91890p POK_full.txt|cut -c1-300; grep -n -i -E \"Root / lemma: .*mi-\" POK_full.txt | head -20; grep -n -i \"Wurm\" POK_full.txt | head -20"
}
```


### [2026-10-17T00:01:38.358Z] TOOL RESULT

```
Root / lemma: uer-S. I. ur-e/-. p) urizd- {* huer-3) 

Meaning: to be confused, ashamed 

Material: viell. from an 5-Erweit. and with probably present formation d Old Indie vndate 

'wird verlegen, schamt sich', vnda- m. 'Verlegenheit, the genitals' {*uri-z-d), Latin ndeo, - 

ere 'laugh'; Old English wrgestan^iuru, bend', Norwegian dial. (i^re/s/'Weidenring; 

Querkopf, isl. Ae/s/a 'verdrehen, crook', could ein Indo Germanic 'V/'o/zo'-voraussetzen. 

Page(s):1158 

Root/ lemma: uer-3. I. ur-ei- y) ureig- {* huer-3) 

Meaning: to be crooked (?) 

Material: In Avestan un//zd-ma/5ya-'6\e Leibesmitte schnijrend', zaranyd-urvixsna^W\\h 

golden VerschniJrung (am shoe)' (unorganisches a); Gothic wra/qs'oKok\dq', Old Frisian 

wys/r 'crooked', Swedish ure/r 'stubborn person' {*uroig-uo-s)\ here das in vocalism 

irregular gr. pai(36(; 'crooked'; 

gr. poip6(; is hybridization from ^o\k6c, and paip6(;. 

References: WP. I 279. 
Page(s):1158 

Root/ lemma: uer-3. I. ur-ek 5) ureiR- {* huer-3) 

Meaning: to turn, bind 

Material: Avestan urvisyeiti {*vrisyati) 'wendet sich, dreht sich', Kaus. urvaesaye/t/'\Nen6et, 

dreht', urvaesa- m. ' gyration ' (= gr. poiKOc;, Dutch wreeg); Old Indie ures/- 'Wasserwirbel'; 

gr. poiKOt; ' writhed, crooked, humped, gebogen', piKv6(; ds.; ^xokoc, 'Koffer, hutch' 
maybe from *uriR-skos, 

Latin /Tca'Kopftuch', ncinium, originally dial, recinium ^smaW Kopftuch' {*ureika)\ 


53510:Root / lemma: ICfmi-i^ k^ehurmi-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
58394:Root / lemma: meih-5 mi-neu- 
74841:Root / lemma: semi- {*ghemi-) 
40178:Bourcils bruns ' from Old English wurma ' purple color ' borrowed (Gwynn Hermathena 20, 
55361:celebration ', iinn-ormr' dragon' = Old High German iindwurm' lindworm, wingless dragon, 
75749:'Springwurm' Hes.; ablaut. aKipiau) 'spring'; with ani. a- (blofter suggestion?) aoKapi^u) 
75750:'spring, wriggle ', wherefore aaKapi(;, -iboc, 'small Eingeweidewurm, larva a 
78017:/e'/7/re'/77e'/7/7'Eingeweidewurm' {*sllnkurh). Middle Breton /e/7c/''schleichend'; Old High 
80000:sp/^i///5'Johanneswurmchen', S/O/^^/^o/ 'shimmer'; spuoga' reflection ', spuogalasi. PI. " 
84876:lebenderfish'); Latin tinea^ moth, Holzwurm' (compare above russ. tija) probably from a 
85874:zerfressen become', trande under trandis^ maggot, Holzwurm'; ablaut. Latvian trudi^ 
86127:"Naschereien', TpcbvAn 'hole, cave', rpu)^ 'Kornwurm', i^cr^oc, ' he-goat; billy goat '; 
86289:Material: Gr. TspnScbvf. 'Bohrwurm'; Latin tarmes{termes), -///s'Hoizwurm' (probably from 
88760:in addition Old High German wibilm. 'beetle, chafer, Kornwurm'; Old Saxon wivil. 
88761:Middle Low German wevelAs., Old English M///fe/' Kornwurm', Old Icelandic V/Min tordyfiil 
91488:ormr. Old English wyrm. Old Frisian wirm diS. " worm ', Old Saxon Old High German wurm 
91490:Prussian wormyanVok. 'red' ("wurmfarben'), ablaut. urm/nan6s., Slavic vbrmbjen. 
91492:worma^ Purpur', Old High German gi-uurmofxed gefarbt'. Old English wurma'C(\. " 
91495:gr. PN Fap|jixo(; and p6|J0(; (Aeolic *Fp6piO(; from *urmos) "Holzwurm' Hes.; compare from 
91501:Tleischwurm' {*urg{h)-ntes), cymr. PI. gwra/nt^Wurmer in the skin' ( *urg(h)ntoi), gallo- 
91588:cymr. gwra/nt'Wurmer' etc. (see above S. 1 152) kann gor gh in root final sound have.
```


## [2026-10-17T00:01:40.124Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 53510,53540p POK_full.txt|cut -c1-300"
}
```


### [2026-10-17T00:01:40.542Z] TOOL RESULT

```
Root / lemma: ICfmi-i^ k^ehurmi-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 

Meaning: worm, grub 

Note: 

-/77- suffix lllyrian Greek stem formation. 

Material: Old Indie /r//77/-"worm, maggot '; np. A//777 'worm'; 

alb. krimp{krim-bi), Geg kri/m ds.; (common alb. -w- > -y-, -i-) 

Also alb. kermiir snail ' : Lithuanian kirmele^ worm ' (common Polish alb. y > e) 

Old Irish cru/m'\Norm', Proto Irish k"rimi-, cymr. pryf, corn. ds. 'worm', bret. prenv6s.; 
gall. FIN *Primia> Modern High German Pfrimm, Primantia> Modern High German Prims, 

Old Prussian g/rm/s{\eg. kirmis) ' maggot '; Lithuanian kirmism. f. etc. ds., Latvian 
cirminsrw. ds., Latvian cermet ' worm, mawworm, hook-worm, bot, helminth ' 
MiJhlenbach-Endzelin I 378 under 386; 

sloven, dr/77' carbuncle, red gemstone, finger worm ', poln. czerh{io'c *czerrhl compare 
Serbo-Croatian crn ' metallic oxide, rust ' for *crirR) ' worms in the rotting meat ', czermieh 
' Dragon tea ', czermiowka^ morel, nightshade, any of various herbs and shrubs of the 
genus Solanum '; 

in addition Adj. -formation of Slavic *cbrmbrrb 'red'. Old Bulgarian crbmbnb 'red', 
crbmbnovati s§^ turn crimson ' etc.;
```


## [2026-10-17T00:01:46.306Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"urvis|urvaēs|urvaes|avarət|avaret|kərəm|k[əe]r[əe]ma|kirm|varəp|warəp\" BRT.txt | head -30"
}
```


### [2026-10-17T00:01:46.615Z] TOOL RESULT

```
3571:.  .  avat  "apayaU^'*  nama    ahmi  yat   «ra    0  dem  Ort  nach  'der  hintere':  'rat  h, dama'apayemi    "Einholer    heisse    ich   .  .,  urvaesnt  fratarjm    urfaes^m    Vyt.2^;  — weil  ich  .  .  einhole"  Yt./5.43.  1  °raya  (LS.)  paiH  *mastrr/nya  ..paourvya
3825:(sd.)  . .  yal  ml  aiw  urvisiitli  . .  starasca Yt  72.25.  3)  'rings  hin  an  — ';  ar)dvlm
4073:•  j.  a-friÖyant-  Adj.  'nicht  verfaulend, verwesend':  yat  kirmavqn  frahm  ahüm azar}Smi3m  amarihntim  -yantim  apu- yantsm  Yt  79.  11;  —  *°yS  Vyt  45'', F.jh".
5773:—  vlsph  gaüäsca  tanvas.'a  atdiblsca  (als Obj.)  uitäiiqs^a  kihrpas^a  trvliJica  Y.  55, 1.  a)  überhaupt  'stofflicher  Leib'  im Gegensatz  zu  uUäna-  oder  baoriah-:  nöit "laca "  nBit  uStammca  tiöit  baooasca  *rl.- urvisyltt  V.ig.T,  —  vJ  mqm  urvaisayat 'laca'^  ustJnaca  V.si;  —  pasäi  "(as.'a baooan&asca  *vT.urvJstim  Y,  35.  s;  V.  i'.Si, H.  2.  r  7 ;  —  atars  haiidazaili  *ascai>  (AS.) u/tilMm^aV. ^.g;  —  «J;V  '/J  n$il  ustanaAl cinmam  Y.  /2. 3 ;  —  ffm  ahmäkäts  azdi- biscil  uitännUla yatamaidlX.3-].^.  [V,^. 49,  5.8:  lies  astd.vu°\
5982:i)  'treiben,  wegtreiben,  wegschleppen' (Vieh   und  Gefangene   als   Kriegsbeute): jvU  gqm  *vani(rm  (sd.)  aznUe'W.  S-Zl ', —   ' ya  {gäu^  varÄa  (sd.)  azimna  (Pass.)  Yt.  . ;o.86;    —    kaoa    nS  fraourvaesayälti  . drujö  vaismmda  a z;/ mn a m  (APm.)  "wann wird  er  uns,   die  zur  Wohnung  der  Dr.  ,  j.^  g,  azan-  :  asn-'^  n.  'Tag',  im  Gegens. hinweggetriebenen  (Rinder)  . ."  Yt/o.86;,2ur  Nacht:  pat/i  'sai paiti  xsa/ne  Yt./.g,
7265:13,  N.  Ö2;  —  äat  (s.  8)  yat  äpd  udiannte .  .  ä'  fralasinH  .  .  fravalayS  Yt  JJ.  65; V,  ^,40,  ^7.4;  —  yat  ('als')  mqm  Iura pazdayaiita  . .  ä°  azsm  tanüm  aguze  . . äat  (s.  3)  mamfraguzayanta  ..  Yt  i;.  553'; — yas)  Uli  mnärom  äktrirum  .  .  ü°  mam mairyd  äkasat  äat  (s.  2)  .  .  fräkirmaot V.  22.  if;    —    äat  (s.  8)  yat  mi>r)m   .  .
7711:•  }.  »rszaurvaesa-  m.  Name  des  zweiten Abschnitts  der  ersten  Hälfte  der  Nacht*'; 'Sät  F.  27  b.
7969:•  j.,  g.  ira-  n.  i)  'Anlauf;  Aa^cilCi /rava- says . .  ya  * afrö.urvisvat  (sd.)  k?miavainii '/■3m  Yt.  rj.  26;  —  yahmya  säslärS  .. paoiris  °rä'>  räzaymte  ".  .  die  vielen  An- griffe ordnen"  YL/o.  14.  2)  'Energie, Tatkraft';  tatca  mazdä  'i:wahmT  *ä  dam (sd.)  nipuaks  .  .  *mqziijcsa'irä  vazdanhä *av}m  *ira'^  "..  dass  du  darüber  wachest, grossmächtiger,  mit  beständiger  Tatkraft" Y.  4:9.  10.
8743:. .  vahistsm  paityämraot  ¥.27.4;  F.5;  — vXspäyämca  "tatim  .  .  'tätfm  aiararum yazamaide  Vt.iS.a;  —  vahistimla  ahütn .  .  vlspäyümca  HSs  (statt  Akk.)  P,  48;  — .  sadr>m  urvistnmla  (sd.)  ,  .  -tatsm  nimra- vaite tistryö  .  .  usta  ml  .  .  YLÄ  23  und I '9;  '3-93i  PrG.;  —  uslavaittm  g^qm '■  sravayS  'täfsm  nimraomns  'usta  ahmai  . .' ,  H.  2. 2 ;  Y.  7/.  1 6 ;  —  nf  -taite  nl  vahiÜai atnthe  .  .  Vyt.j'j.
9379:KompE.  ■ —  Vgl.  unter  "karsH,  "karilu,  wofür Pü.  karr  hat,  und  •frakarila-,  das  Pü.  mit  dem selben  Verbum  wie  frakirmlal  usw.  übersetzt : /nif  ^i>/-fu/7i).  — Zum  Verhältnis  von  'karsla- (mit  ar.  /■,  IF.  g.  161)  lu  kirtla-  s.  unter ajtinuila-.  —  ')  Weshalb  man  CS  auch  faisch- lich  zum  V.  kar^l-  gezogen  hat;  so  zuletzt Ggr.  GlrPh.  Jh.  219,
10013:vamm*jas»ittim^^  ahmya  nmariey. 13.22;  (.Aal'a  mit  AbL):  6a%a  alaum  apa.jasS — yh  (näml./z'aj'a.fflj'J)  *qfrSjurvisvat  (sd.)  '  (aS.)  ütibyasca  haca  ..  H.2. 16.  2)  'enl-
10041:Höhe  kommen,  gross  werden':  a<,a  taeHl usjastnii  yä  .  .  "und  es  kommen  die  in die  Hohe  (obenauf?),  welche  .  ."  V. /.  14 Gl.;  —  vTspsm  a  a/imlt  'ira^nm  kirma- vat  yat  assa  yo  apinnSyakS  uzjasat  "so lang  soll  er  Sorge  tragen,  bis  das  Kind gross  geworden  ist"  V.  75, 1 5  '^';  —  vTsp>m a  ahmät  %ra^rtm  kfrinaväl  yat  alte  ySi spana    uzjasqn    V,  15. 2 1  '*>,  a)    Kaus.
10711:j.,  g.  xäaSra-,  p.  xSsO-'a-  n.  'imperium, regnum,  Herrschaft,  Reich';  uzw.  im  Sinn von  1)  "Herrschgewalt,  Obergewalt,  Herr- schermacht'"; i)  I  im  Ap.:  c^ur^mazdä h'am  mann  fmbara''  Bh./.s,i3;  9,  'D.4. 1,17. 1 ;  —  °^^am  iyt^  bäbirauv  hauv  agar- blyaiiJ  Bh.7.  16;  11';  —  vasnä  a^urO^- mazdäA^  imJ'  °h''am  därayämiy  Bh.  /. 9;  9;  —  °'ii''amiim  adam  adlnant  Bh./. 13;  i3i  —  "''"*  "ä'^'»'«  fy<^  gaumätc^ ty^  maguS  üdin^  ia''bBßyam  aitJ'  ''i'aiii ha'ä  paruviyata''  amäxam  taumäya  aha Bh./.i2;  —  '^'am  tyJ" ..paräbarfam  aha^ .  .patipadam  akunavam  Bh.  /.  1 4.  ||  2)  im jAw.T  uparäi  amäi  .  .  v»r?'hrSi  ..  °%räi A.  /.  8;  —  '%rakela  paiti  bäiiumais  dan- yayasca  paiti  darr^S.jXtSiS  Yt  y.  135; —  ''%r)mca  paiti.astlmca  darrfö.xsa^rfin "'hrahe  darr^5.j.ttJm  ustanahe  A.  /.  8;  — yim3  asti  hr.?>e(s6.}  '^rayä  (GD,)  V.  2. -  ^ahmi  '>re  Vr. /^_2(P);  P.  2^; — yimahe  °&re  nSit  aotftn  SnHa  .  .  yavata xsaySit  (sd.)  . ,  "unter  Ks  Herrschaft  .  ," Y.^.j;  V.2.S; — yim?m  . .  ye/'jhe  ''^rula .  .  nöit  aottm  fff»ha  . .  para  ahmSl  yat . . Yt.  IQ.  33 ;  —  yimS  . .  yat  kirmaot  aiähe '"ifräha  *amarsanta  pasu  vira  Y.g.  4;  Yt 15. 16; — Auxsa'hrS.ttmaiät  al  ""kmin  äfyai A.J.6;  —  zard^ustrim  ..ya^  as  ..*%rfm huxsa^rJ.ümS  (sd.)  \t  1^.79;  A.^.4,  Vs. 5^_j; —  'ir.lt  xsayamiia  VytJ5;  — yal^a anyhsBt  ""^räl  xlayamnä  hatnö-xiahrS.- xiayamnS  Yt.  J5.  54;  —  As  araHwya  '"^ra nsit  xiayeti  Vyt  47;  —  us  nü  atühäi  vJse jamyäl  asimea  "'hrsmca  savasca  .  .  Y.  60. 2;  —  zaraiiultrahe  ,  ,  paoiryai  hanhanuse gqrnifa  ahmla  .  .  uxüahyäca  (sd.)  i
11875:Zum  V.  tak:  —  Vgl.  iarilä;  /atHu' ,  frälat,- iaril-  und  tahra-{1,  KZ.  J/,  S46).  —  Pü.  (iu 1);  tiansskr.;  s,  No.  3.  —  ')  NA.  mit  F  1  nur kirmaol  lafan  arUarf  arApni;  s.  aber  JlO. —   ')  Them.  —  ])  Pü. !    2  än  and  häsr  iana
12072:'/ravazaite  mihrS  . .  'rS  anzaki  savaki  YL 70,133)1331,  aa)  bildlich:  Hfli/afljtrfy^j- raihyanqm  (sd.)  *urvisyeiti  *V;?*'  dar^ya data    .  .    zara^uürake  P.  ^6.  ß)    zeit-
12698:Komp. :  JoiiikaD'  +  urv°,  statt  daiohuurv gescfar.;  %.  »u  tmaurvaesa-,  —  Pü.;  dek  vaitär, ed.:  otret  1  esletätak.  —  >)  Im  Gegensatz  zu fiairiJJ^cm-  (sd.).  Vgl.  Dk.  9.  6.  2,  utdaiihav- nnd  unter  haxteü.
13103:—  mi&r>m..yB  'itiAiu^  rqxsyqi'äyä  para rati/ta  baraiti  YtJO.z;;  —  'iiihavB  avi.- mi^ranyä  Yt/o.  101;  —  nasdista  'itihävö V,  /p,  41 ;  —  frat)m?m  'iählus  nava  ptr?- Ja'5(sd.)  kirmava  V.2.^0;  —  aspö  (sd.) o^ryBJ^mB  °ähve  vanmanB  F._J  h.  b)  im Ap.:   'hySuhnaiy  durui'ä  ahatiy  Bh.4.5;
13723:•  j.  dürae-urvaesa-"  i)  Adj.  'des  Wende fem  liegt',  vom  Weg:  °s)m  paili  pantqm Vt.i.35.  2)m. 'ferne  (Weges)wende':(7fl/ ti  narqm  fravaz>nti  'i»m  ",  .  zur  fernen Wegeswende"  Vt.  (J.  58.
15653:•  j.  paouru.{raourvaesa-  Adj.  (fem.  °sa-) 'mit  vielen  Ausläufern':  harqm  btrszaitim 'sam  Yt72.  23.
16279:•  j.  pouru.fraourvaesya-"  Adj.  (fem  °y3-) av^paouru/raourvaisa-:  haram  hnzaitim •syqm^''  Yt. /O.  50.
17821:yemi  , ,  imat  am>ia  spptita  .  .  imat  asäu- nqm  varguAls  °iays  (VP.)  Wjra  aiiuihüra Y.  65. 1 2 ;  Ny.  /.  I ;  —  aora  varmkis  upa.- sa^a  .  .  äps  .  .  urvarä  .  .  tüäunqm  fra- vasays  Yt  13. 147;  1. 9,  10. 100,  H.  34,  y, 79,  FrW. /.  3;  —  jamyqn  i^ra  asäunqm .  ,  'iaylf  asöis  basfaza  hacimnä  . .  istSe *vadhar»Aqm  paitiHätSe  ätaranqm  Y.  60. 4;  —  qpqmea  .  .  urvaranqmca  .  ,  asao- nqmla  'hnqm  yasnsm  Vr. 21.  \;  —  yS nä  his  hubinta  *barat  jva  a?aonqtn *says  (als  AP.)  sästa  .  .  hö  anhaiti  za- sulttmS  Yt  /J.  1 8 ;  —  fravasayS  .  .  yä a/raourvisvat  k?r»navainti  irsm  yahmya jaanti  Yt.  y.  26;  —  -says  . .  ya  ahurahe xsayats  dasinqm  upa  yü&yänti  yezi  aim bavaiti  ^alavaxsnuiW.  13. 63  ;  — frasüSTnii uyrä  asäunqm  'fayS  paoirij'  pouru^sata .  .  pouruAatanra  .  .  pouruiasvanS  apitii ashntnä  haväi  käcil  näfäi  . .  tä  yü^yeinti pfianähu  have  asahi  Yt  l^.  65if.;  —  "sayS .  .ya  avai  trayS  aiwyaxsayänti  yat  vouru- kahm  ..yä  ave  strjui  atwyäxsayeinti yqm ^haptöiringS  ..ya  avqm  k^hrpim  aiwyäxsa- yänti  yqm  .  .  hnsäspahe  .  .  ya  avqm *x^rqm  (sd)  aiwyäxSayänti  yqm . .  tara- 'huStrahe  navaca  navaitlsla  navaca  sota nava^a  hatattra  navasSs^a  baevqn  Yt  13. 59—62;  —  "iayS  .  .  yä  vts^&a  ävayänli hamaspa>:maedaim  paiti  ratüm  äat  a^ra vtcar?nii  dasa  pairi  xsa/nö  Yt/J.  49;  — asSunqmcä  'HbyS  yä  nS  iltä  urvSibys  Y. 5Ö.  2 ;  —  asäunqm  '/is  narqmcä  näiri- nqmcä  yazamaidl  Y.^7. 3;  —  °fayS  yä paeirya  (sd.)  anhan  Y.  23.  \;  —  äyeseyesti "vTspaya  asavane  'se"  Y,  2_j.  3;  —  vTspä °iayS  (als  AP.)  asäunqm  yazamaide  ädah- *yunqmca ..  'say5 ..*u%dahyunqmla . .  °iayS.. narqmca  ..'^ayD  ..näirinqmfa  ..  °sayS  yaza- maide  Vr.l6.  2;  7.  i,  10.2,  16.  i;  —  nabä- nazdiäanqm  para.iristanqm  aliirapaitinqm a!>iryanqm  narqm..näirinqm  'iayff  yaza- maide  Y.  26.  T,  8  ff.";  —  a/äunam  "sayd .  .  nmänyä  visya  zantumä  däAyumä  zara- ^ustrSJpmä  Y.  ly.  18;  —  airyanqm'  .  . /ßityanqm'  .  .  sairimanqm'  .  .  säininqm' . .  dahfnqm' . .  vTspanqm'  dakyunqm  narqm .  .  näirinqm  .  .  °sayö"  yasamaide  Yt  13. 143—145;  —  fä  'sayU  .  .  aoßstA  hittti  .  . ya  paoiryanqm  tkaihnam  ya  vä  narqm azätanqm  /rais.car>^rqM  saoiyantqm  Yt. y.i7;'Y./.i8',  23.2,  24.5;  —'  vjipä .  .  'Iay3  .  .  yä    haca   gayät    mariihnai   ä
18254:•  j.  frärai^ya-  Adj.  'was  zum  Apparat eines  Rechtshandets,  eines  gerichtlichen Verfahrens  gehört':  vispah  ahubya  ratubya d.lilya  raiwya  ya  aiahe  diltais  vahistake "und  den  ganzen  gerichtlichen  Apparat, der  gesetzlich  vorgeschrieben  und  durch den  Einzelfall  gegeben  ist,  für  den  Ober- herrn und  den  Richter  nach  den  Ge- setzen des  besten  heiligen  Rechts"  F. 40.  a)  GP.  mit  atätay-  f.  'Rechts- verweigerung"*': nSit  aläiti  *'yanqm'> *urvisyeiii  *larS  danrya  data  alaonS  sara- ^ustraAe  "nicht  verstösst  er  durch  Rechts- verweigerung gegen  die  . .  Gesetze  , ." P-  5^i  —  ratufri!  . .  yS  aZäiti  *'yanqm  J* /rapa  (Sp,  72  o.)  ". .  mit  dem,  was  man (als  Sühne)  für  Rechtsverweigerung  be- kommen hat"  N.  54.
19068:nsit  im  Sinn  von  'dass  nicht,  damit  nicht' zur  Einleitung  eines  dem  Sinn  nach  unter- geordneten Satzes;  a)  mit  Konjunktiv:  nSii kl  apastaväne  . .  damam  .  .  n'  astaca  '"• «°  ustantmca'"'^  W  baohasca"^  *vTurvisyat Y.ig.j.  b)  mit  Infinitiv:  _/ra  %wqm.. usuxlane  . .  n-  apaya  a/rapatai  Yt  75.50; 48.  HI)  nSit  als  Wo rtvem einung;  uzw.
19380:'"kirmtu  (Sp.  45a  u.)  V.  7. 38  *>.  6)  zum Part,  ist  eine  Verbalform  (aus  6av-  oder 'flÄ-)  zu  er^nzen:  rn3  ä/"  iarS  (sd.)  atvS yai  iristfm  V.3. 14-  Ausserhalb  des Zusammeohangs :  F.ö^.  Verderbt:  ma  hl bansma  pairiJifnhm  (sd.)  pairi.k>r3nlx![ . . V. /p.  19.  Ad  zerstörter  Steile:  II  mJ Am.  4-
20088:. .  frampr^öii  V.$.  4a.  3)  '(einen  Ver- trj^  aufheben':  vaii.,mi^r3m  kirmaoiti *zastS.mat5 .  .framinzaUi . .  antar^  urvaitya (sA.)  frada^aifi  V.4.3;  sf.*.  4)  'fgrt-
20338:•  j.,  g.,  p.  mah'  m.  i)  'Mond',  auch  als Gottheit*':  avat  hvan  .  .  käu  ma  .  .  ave stärS  V.p.  41 ;  —  yat  ml  starS  .  .  kacilnie (sd.) paraca  mä  ..YtS.i;  —  stärS  mSahS (NS.?)''  *ki>an  anayra  *rao^ä  FrBy.;  — i.7»hqm  (yä.m\.  fravaHnqm)  raya . .  hvars . . mä  ava  pa%a  aiiti  . .  stärS  Yt.  13.  r  6 ;  — upa  tairam  AaraihyA  .  .  yat  tnl  aiwits urvispnli  staras^a  mis^a  hvanla  Yt./2,as; V.  2. 40;  —  strSuÜca  mäahsmca  hvar?ca Y.  2.  II,  7/.  9,  G.^.6,  Yt/O.  I4s;  V.  ir.  i, 2  (statt  NS.),  7.  52  (statt  NS.),  VyL  43;  — haca  manhsm  (statt  AbL)  V.//.10;  — fravalayö  .  .  yä  strqtn  mäahS  (GS.)  hürB .  .  pa%S  dalsaym  Yt /J.  57;  Y./.  16;  — yazai  hax^r)mca  yat  asti  . .  antan  maf?- h)mca  hvanca  Yt  6.<,\8.\;  —  kj  yä  mil ux^äti  tunfsaitx  Szcß/(sd,)  Y.  .^3;  — pancaJasa  (sd.)  mä  ux^eiti  panla.dasa mh  mnßatti  Yt?.  3;  z',  F.  (?;  —  yai mätshtm  (statt  NS.)  raoxlne  täpayeiti  Yt. 7. 4;  —  raoxsrum  mafihtm  aiwi.vainsm Yt7. 3;  3^;  —  tanüm  .  .  yaha  maaAs hväraexmS  {sA.)  Yt. /0,14a;  —  ragnna- vatitwt  bavähi  yä^a  mävh^m  (statt  NS.) Az.  6;  Vyt  4;  — yatai  mäahgm  ffoaa^r^m bay»m  raSvanttm  i^annaauAantpm  YL7. 5, S.2.  12;  Yt7.3,  6,  -TZ- 33,  Y./6.4;  — mäahahe'^  gaoc^rahe  Vt?,  o;  Y.  j.  11, N.  47;  —  mmS  mänhai^^  gaocÜiräi  Yt. 7. 1 ;  —  uzayara  usTra  mnnha  (VS.) '' gaoHhra  V.  21. 9.  a)  mäahahe''^  (näml. ayari)  heisst  der  12,  Monatstag:  mäis- hahe^^  gaoevirake  S.  j.  12;  vgl.  2.1a,  Y. 16.  i,,  2)  'Monat':  dasa  ava%ra  tnäKhö (NP.)  zayana  dva  hqtiüna  V.  /.  3 ;  —  hapta
20567:'  wenn  sie  ins  künftige  Leben  kommen" Ylj.  25;  V.p.44;  —  cvat  aßimäi  naire 'dim  aakat  pas'a  astasca  baooattkasca vi.urvistim  "wie  grosser  Lohn  wird  dem Maime  werden  .  ."  V.  Ä  8 1 ;  A.  ^  4,  6;  — —  Ayai  'dim  *mavai'i:3M  (sd.)  /radadä^ä dam^byB  Y. 40.  \;  —  hyat  dairiä  vaMstl yli/^(sd.)  'dt  y.4g.g;  —  ..  iyat  *cfi,i/ts *'hudaby5  'dim  mazdä  yehyä  tu  dähnm I ".  .  zu  dem  Lohn,  der  den  Verständigen versehen  ward,  den  du,o  J/.,  festgesetzt  hastT V,^4.  13; —  hyat  'dim  zarä^ustrS  maga- vabyö  {&A.)  cdisf  para  Y.  5/.  15.  a)  mit Gen.  obj.:  yä  damä  vairJm  hanäi  'dim asahyä  yäsä  (sd.)  aslm  Y.  54. 1 ;  —  aicä vs  'dim  aahat  ahyä  magahyä  .  .ya'irä  . . "und  es  wird  euch  der  Lohn  dieses  Bundes werden . .  dort  wo  . ."  Y,  3^.  7 ;  —  disyät Ai  anAe  avat  'dim  parS.asnai  anuAe ya'ka  . .  "es  soll  ihm  dafUr  ein  so  grosser Lohn  Tür  das  künftige  Leben  zugesichert werden,  als  ob  . ."  A._j.  7,  aa)  zugleich
20826:—  kihrpasca  ya  ra^üwayäti  srTrä  .  .  Yt 13.81;  —  im  Genus  mit  dem  Praedikat  kon- gruirend:  iristanqm  urvqttB  ..  yä  aiäunqm /ravasayB  Y./ti.  7,  26.7, 11,  FrW.JO.  39;  — N.-ASn,:  s^armB ..yal  asti  ahurahe  mazda ..yat'  asti'..yat  upanhacat  haosyatihim Yt.  ig.  9-26;  66,  'P.33'; —  lair?m..yai,. aiwitB  . .  urvismti  Yt/2.25;  —  gaobaram .  .  yai   asti  pührahe  ^rimB  V.2/.  7;  Yt
20880:elegerint"  N.  i;  —  mi^r?m  tnä  janya  ,  , mä  yim  drvatat  ptnsitahe  mä  yitn  . . asaonai  "pactum  ne  frangito  .  .  ne  (id) quod  cum  .  .  feceris,  ne  (id)  quod  .  ." Yt  jo.  z;  —  usta  bä  yim  hacahi  ".  .  (ei) quem  sequeris"  Yt/7.  7;  —  taFöi  ayare mainyente  yat  (NSn.)  _>>««  ", .  halten  lür einen  Tag  (das)  was  ein  Jahr  (ist)"  V. 2.41;  —  ustä  astl  .  .  hyat  asäi  vakistäi ahm  (Sp.  233  u.)  ",  .  (id)  quod  (est)  .  . praemium"  Y.  27.  14;  —  ma  as  aFvB barB  (sd.)  yat  irUOm  "ne  quis  solus ferto  (id)  quod  mortuum  (est)"  V.5. 14; 14;  —  iva  dqma  ,  .  yas(ASa.)^a  da'hat spmlB  mainyuiyasca  äa^aj. .  ". .  utramque creaturam  . .  et  (eam)  quam  creavit  . ." Ytij.43;  —  ^riiat{sd.ya  .  .  glui  apa.- jasal  yatla  aiihal  .  .  yatca''  .  .  "et  tertia pars  . .  pecudum  . .  (eius)que  quod  (pe- cudum)  crit . ."  V.  2,  23;  —  tata  yal  paiii.- bannti  yä  (N.-APn.)  andu^at  *afaititat ^äjayaurva  yä..ya  aoäiti  *fr3raihyanqm (sd,)  Jrapa  *yai  nSit  visttm  (sd.)  drvatö "femer  wenn  sie  (das)  darbringen,  was.." N.54;  —  däya  ms  . .  yä  (ISn.)  ml  ai^hat afrasatfha  "des  mihi ..  (id)  quo.."  Y. 62. 6; —  iA;(sd.)  vTseyahmal{hh\'im)  kaca . .  Y. 68.1^; — havatqm  fiafia(sd.)yaÄmi(LSni.) "parynti  "..  (is)  apud  quem,."  N, /_j;  — a/raourvisvat  hrsnavainti  inm  yahmya jassnti  "..impetum  (eins)  quem  visitant"  Yt. 13.  26; — milGen.  pait,(?):^5<ja';w(  uslrd.- stärum  uzdasta  yerihä  (?)  vU  aSiö  usirB,- s/äfii/  (sd.)  aiikal  aetakm^yus  . .  V,  1$. a4(?);  —  im  Sinn  von  quantus  (s.  Sp.  120a m.):  cvail  yat  hi  kasihahe  irnvS  frat»- tntm ßisis" quaatam}  (tantum)  quantum.." V. /Ä44PiiZ.;  —  s.  noch  N.;oi?  unter "ii/.^nfis/J;  —  im  Sinn  von  quot:  ci'atgao- nahe  (sd.)  avabaräti  yä  (APn.)  *dvaeibya trizubya  (sd.)  * hartgtriwnät  ". .  (tot)  quot . . cohibuerit"  Ü-ÖS-  a)  wie  Sp.  1316  u.; erste  Person:  buyama  ahurafu  mazda  .  . astayl  yOi  narS  asavanS  humatäis  mai- nimna  , .  "wir  möchten  . .  sein,  die  (sva. indem)  wir  als  gläubige  Männer  . ."  Y. 70.4; —  zweite  Person:  uia  buyi  ajra- taintis  .  .  yH  mqm  .  .  nait  baxlake  Y.  u. *j  ^i  3i  —  ^^  ahi  yS  mqm  sbayehi  ye^he ..  srailUm  susruye  vaam  Yt. /J,  17;  — kä  tian  ahT  yim  , .  sralsttm  dädarpsa  Y, _().  I ;  —  Hsca  caräitis  ahi  yqm  . .  sralstqm dädarisa  H.  2.  10;  —  usihiiia  pliri.htiiaa-
21108:•  p.  ya'diy,  j.  ye8i'>,  yei8i'>  Konjn. I)  II  zeitlich 'zu  der  Zeit  als' ;  viyaxnakya\  3.-ai\i\\X, mähyn  14  raucabii  'kakaiä  äka'  y  uda- patatä  Bh./.  II.  II)  bedingend  'wenn, sofern';  i)  mit  (fiitur.)  Konj.,  a)  vor  dem Hauptsatz:  II  y  kürj'  pärsj'  patc^  aha- tty ..  siyätis  .  .  nirasstiy  .  ■  D.  5. 3;  — y  av(^a  *maniyähay  .  .  imam  pärsatn käram  pädiy  D.  5. 3;  —  y  imäm  dipim vainaAy  . .  uta  parikarähidil  J'urJ'mazda %uv3m  daufta  blyä^Bh. 4.  16;  17,10,11;! —  *(^(  sL.aSe  vacS  ustime  urvaese  gayehe /ramrai'3i{aS.)  pairt  te  tanava . .  urvamm . . Y.  7/.  ig;  —  im  Nachsatz  steht  «Sa:  °i%i zT  kvari  nUii  uzuxsyeiti  aha  datva  vTsph minnänta  "wenn  (einmal)  die  Sonne  nicht aufgehen  wird,  dann  werden  die  D.  alles zu  nichte  machen"  Yt  6.  3.  a)  ||  mit ^•^«/(^(sd.)  'wenn  etwa':  ^yadipatiy  *'ma- niyähay:  ciyJ'karam  (sd.)  .  .  patikaram dldiy  D.  6.  4.  b)  U  hinter  dem  Haupt- satz: martiy^  ky(^  draujaitJ'  ahatiy  avam *^u/iasata>n    pars3    y     avada    *mam-
```


## [2026-10-17T00:01:50.603Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^•.{0,8}(urva[eē]s|urvis|avar)\" BRT.txt | cut -c1-400 | head; grep -n -E \"k.r.ma-  *m\\.|Wurm\" BRT.txt | cut -c1-300 | head"
}
```


### [2026-10-17T00:01:51.153Z] TOOL RESULT

```
5125:•  g.  avar-  n.  'Hilfe',  mit  Akk.  verb. : ahurä  na  na  -varS  "o  AIi.^  nun  werde uns  (den  Rindern)'»  Hufe"  Y.2J..  11.
5127:•  j.  avar«'gav-  m.  EN.  eines  Gläubigen: "gSuH  fnzavaiö  *öiymatastura/ie  asaonö "des  Ä.,  Sohns  des  ^.,  Sohns  des  Ö."  Yt
5139:•  j.  avara'Srabah-  m.  EN.  eines  Gläu- bigen :  'batshs  r3starf.i'ayp)itiiii'{%A.)  aiaonS W  13.106,  —  'ba  (NS.)  Dk.  7.7,  ao,  zi,: .V.i3.i8'>.  j
11585:•  g.  Javara-  ra.  etwa 'Wägung,  Abwägung' (der  menschlichen  Taten  beim  letzten Gericht):  kn  %wöi  a^ä  a-ia(sd.)  arx/rSng isyä  vatfhSus  *mainySus  syadhananqm  °rS ". .  die  Abwägung  der  Taten  des  guten Geists?"  Y.  48. 8.
17425:•  j.  bravara-  m.  —  ?  — ,  eine  Landplage Baktriens:  bSx'ÖTm  .  .  äqt  ahe  pai^änm fmktrgtttal  aitrS  matnyus  .  .  "rtmca  usa- iasZa  V. ;,  6.
17802:•  p.  fravartay-  m.  EN.  eines  Meders,  der sid)  gegen  Darius  I.  empörte,  Phraories: 1  martiyj^  'tis  nätnt^  hauv  udapatatä madaiy  Bh.  2.  5;  13",  4.  2,  Bh.  e;  —  Aauv •iis  Aya*  mädaiy  xsäyäitiyJ'  agaubatä  ~' 2.  12;  —  iära*  msd(r  .  .  hatniViyJ' abava'  abiy  avain  'lim  aHyavc^  Bh.  2,  5; —  par%ava''  utä  variäna^ . .  °lais  *agau- ba'tä  Bh.2. 16;  —  
25553:•  j.  urvaes-  V.  '(sich)  drehen,  wenden'. Praes,  ^^  urvisya-,  30  (Kaus.)  urvals/iya-, f-Aor.  I   urvis:  —  PPfP.  urvuta-.
25755:•  j.  urvis-  f.  'Sichwenden'.
9575:Kg.  Bed.  und  Et.?>).    —    ')  Vgl.  Ggr.  OK.        *'    Er   ist  der  Sohn  ©ntos,    aus  der  Familie 311,  West  SEE.  4?.   161.    Wertlos  D st.  ZA.    der  .Sämn.    Seine  Taten  sind  Y.  9,  ii,  Vt.  5.  38, :;.  417.    —    ')  Angebl.  ' Wurmst erne',    lu  ai.    ^5-
```


## [2026-10-17T00:01:53.264Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25553,25560p BRT.txt | cut -c1-900; grep -n -E \"^•.{0,6}k.r.ma-|^•.{0,6}kirm|^•.{0,8}avar.ta\" BRT.txt | cut -c1-500"
}
```


### [2026-10-17T00:01:53.827Z] TOOL RESULT

```
•  j.  urvaes-  V.  '(sich)  drehen,  wenden'. Praes,  ^^  urvisya-,  30  (Kaus.)  urvals/iya-, f-Aor.  I   urvis:  —  PPfP.  urvuta-.
i)  'sich  drehen,  kreisen':  lainm  (sd.) Aaraihyä  . .  yat  ml  aiwitS  urvis)nti^^  sta- rasiam  äsca  Avanca  Ytja.as,  2)'sich wenden,  umkehren':  in/a  mi  urvisyatim "zurüclc  wendeten  sie  sich  beide"  Yt. ig.  83.  3)    Kaus.    a)    'sich    wenden
machen, fugare':_c?^ittW(yii..»i/a  urvaisa- yat  karana  Yt.j.  131.  ß)  'abwenden,
abkehren  von  — '  (Abi.);  y5 paeiryS  H^nm urvaisayata  datväatia  haotät  (sd.)  . .  "der zuerst  sein  Gesicht  abkehrte  von . ."  Yl  y. 89,  3)'invertcre':  •urvisia-'^.         4)mit
iarü  und  Akk.  'sich  hinaussetzen  über  — , sich  verfehlen  gegen  — ':  nöii  a&äiti  */ra- raiisyanqm  (sd.)  ^urvhyHH^  *tarS  .  . data  .  .  sardhustraAt  P.  5Ö.
mit    apa    und  frs   'sich    (von   einem  |
Punkt)  weg  hervor  wenden,  zum  Vorschein komiKcn':  apa  hl  paskat  (sd.)  .  .  *frao- irisyeite^^ . .  al/a  druxs  yä  nasul  fiSnkanai haca  V.p.  40.
mit  ava  i) 'sich  herabwenden, -kommen': hö  .  .  vazata  .  .  *paitisa  nmamm  .  .  nStJ aora  avSirisylt^  (als  PraeL)  ".  ,  er  ver- mochte nicht  wieder  herunterzukommen" Ytj.  03.  2)  Kaus.  in  Verbindung  mit avacirista- :  yS  nar^m  ttvaoiristiin  (sd.) *avaourvalsayeiH^^  "wer  auf  Jemanden einen  Angriff  macht"  V.  4,  33,  35.
9574:•  j.  kar«ma-  Adj.,  mit  star-  m.  'Stern-  y-6"i  136;  -  nairyain  kam.varAtJm  .. schnuppe"':  pairika  .  .  ya  slürä  -mJ  ^5  a/ffw^aira/ "/^w  YL  75.39;  — /«iW^am (NP.)  ^/tf«ft'  on/fl^j  a^w  asmanmca  "die  .J"?"'  *^q'iaili  (sd.)  upanhacat  ■'psm  V. y.  ...  die  als  Sternschnuppen  zwischen  /.9;"«y"«  aojishm  baväht  ya>a  'p^m Erde  und  Himmel  stürzen"  YLiy.S.  (statt  NS.)  Az.j.
```


## [2026-10-17T00:01:59.732Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *242\\. |barγ|varγ|bargh|vargh|warγ\" HRN.txt | head; grep -n -E \"^ *(242|870|871|872|873|874)\\. \" HRN.txt HUB.txt|head; grep -n -i -E \"kirm|kerm\" HRN.txt | head; grep -n -i -E \"k[uū]p[aā]l|g[uū]p[aā]l\" HRN.txt HUB.txt | head"
}
```


### [2026-10-17T00:02:00.226Z] TOOL RESULT

```
2476:242. behä 'Wert'.
HUB.txt:1050:242. Die Suffixe np. a, a, t, U, o =■- phi. afe, Oi, Fi, uk, dk,
HUB.txt:3140:870. Np. kamzak ist durch das Deminutivsuffix ak von
HUB.txt:3144:871. Np. hutdh oder kdtah (nach dem afgh. LW. kdtah) heisst
HUB.txt:3154:872. Np. fcil^a 'irdene Krug, Kanne* = afgh. kUza an earthen
HUB.txt:3163:873. Die Zusammenstellung setzt eine idg. Wrzl. kul-
HUB.txt:3165:874. Zu streichen.
HRN.txt:2476:242. behä 'Wert'.
HRN.txt:7571:870. kentz 'Jungfrau, Mädchen', kenizek,
HRN.txt:7578:871. kiitäh, küteh 'klein, kurz'; ködek 'Kind, Kleines,
HRN.txt:7587:872. hüze 'Topf.
7416:Kälmitä 'Würmer (150); bei. LW. kirm-, sar. ser[cerm
12715:kirm 850.
```


## [2026-10-17T00:02:03.156Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==264' HRN.txt | head -60; grep -n -E \"^ *850\\. \" HRN.txt; sed -n \"$(grep -n -E '^ *850\\. ' HRN.txt | cut -d: -f1),+8p\" HRN.txt"
}
```


### [2026-10-17T00:02:03.624Z] TOOL RESULT

```
— 242 —
1078. vevd/kj 'Wachtel', rerdej, verflj, vertek.
ai. varfikä' ^WachteF; phlv. oartak (Papyrus, Hörn,
ZDMG. 43, 50); gr. oorvh
kurd. verdl, //arnfrr?^ 'Wachtel' (H.-Sch.); af/. vvaraz\
ORS. LW. (?) rärdcä; bei. f/vardäf/ Gebirgsrebhiihn' ;
WSL/. VOlc.
1079. verseng 'würdig, achtbar (unbelegt).
ap. onn(7(iyyrjC' of &vf(jyiTa( tov ßnöi'krjo^^ noorrdyyai
y.ah'ovrai nfgtöri (Herod. VII, 85), de Lagarde, Ges.
Abb. 191.
Die Grundbedeutung wird 'gewichtig sein (vei'gl.
se7ig, No. 747); rer -- ap. vpar'nj also wer, wie in
versäz {wersäz) ?
1080. very 'Wasserwehr, hery.
skr. vdrga- 'Abwender\ also zu [/^vnrj- , vdrjafi
(Nöldeke, mündliche Mitteilung).
1081. vemste, beziste nur in nnon, nnDTZ (Is. 66, 8;
66, 17).
phlv. v(i)jastak; Pärsenwort, sonst r/ujasfak,
1082. vei^ey Frosch', arab. LW. vazayat 'Eidechsenart'.
aw. vazayä' 'Frosch'; phlv. vazay, vazag.
kurd. LW. vizdq 'Frosch' (H.-Sch.).
V
1083. i^ezlden 'wichen'; bezän (Sahn. I, 284 Anm. 2).
ai. \/vah-^ väliati 'wehen (dahinfahren vom Winde);
phlv. vajttan wehen'; kurd. LW. vezin, vazdmn
'wehen (H.-Sch.).
1084. ve^lr (arab. LW.) 'Vezir; Gelehrter ^), gezJr, gizlr*^),
talm. ns^T»!:.
*) So im indischen Persisch häufig, vergl. z, B. Maä»ir-i Mah-
wiidsähl Fol. 38 (Berliner Handschrift Ms. orient. Fol. 535).
Im modernen Spaniscli ist der Vezir als alguacil, alvazil etc. zum
'Häscher, Polizeidiener* (auch veraltet 'Scharfrichter' und im Schiffs-
wesen der Beamte, Mer auf einem Kriegsschiffe für alles sorgen muss,
was zum Wasserproviant gehört*, s. F. Boooh-Arkossy, Spanisch-
Deutsches Handwörterbuch^ s. v.J degradirt, vergl. Dozy -Engel-
mann, Glossaire des mots espagnols et portugais d6riv^s de Parabe*,
S. 129.
*) Nur in einem AbuM Ma*änl- Verse.
7412:850. kirni *Wurm'.
850. kirni *Wurm'.
aw. kerema- 'Wurm'; phlv. karm; ai. kfini- (krinn-)
'Wurm'.
kurd. kuriim 'Wurm'; oss. t. ßalm 'Schlange', d.
Kälmitä 'Würmer (150); bei. LW. kirm-, sar. ser[cerm
'Eselswurm'.
851. kes 'jemand', kesT {*kese), kesän,
ap. kas[cit/ 'irgend wer, jemand'; aw. kas[cit jemand',
ka$[7iä ; päz. fcas, kasi[ca ; ai. vergl. käs.
```


## [2026-10-17T00:02:08.067Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *(850|1080)\\. \" HUB.txt; for n in 850 1080; do l=$(grep -n -E \"^ *$n\\. \" HUB.txt | head -1 | cut -d: -f1); [ -n \"$l\" ] && sed -n \"$l,+5p\" HUB.txt; done; grep -n -E \"^(kirm|karm|warg|varg)\" PHD.txt | head; grep -n -i -E \"kirm|karm\" NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:02:08.531Z] TOOL RESULT

```
3072:850. Die Bedeutung von zd. kerema- ist ganz unsicher.
850. Die Bedeutung von zd. kerema- ist ganz unsicher.
Ueber skr. krimi- siehe Idg. Forsch. Ill, 161.
852. Fur skr. kuksi- wie fiir lit. kmzys miisste man np.
*A:wi erwarten. Arab, kuss 'pudendum muliebre sieht
Freitag als LW. aus dem Griech. {vLvaog) an. Das
von Johansson Idg. Forsch. II, 19 angezogene afrd-
750:karm,
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
1612:gal [gl] coll. the gang, the villeins labouring on the estates of the kings, the satraps, the magnates, etc.; in war their military crew 207; pl. cas. obl. ~ -an + Kirm the attendants of K. KnS VI, 8 = KnA p. 275. — OP *garda- attested by the Bab. lw. gardu in deeds and docu- ments of the Achaemenian epoch (a gardu-patu = OP *garda-pati- is also mentioned), and by the Aram. lw. grd? in the Fayyum pap., v. Driver, Doc.,
2297:kirm [klm] dragon 81. — Skr krmi- ‘snake’, cf Av. (469) stáro.koroma- ‘shoot- ing star’; MPrth krm ‘comet’ (MHC); NP kirm ‘worm’.
2298:Kirmān [klm’n'] Kirman 81%. 1161, — Arab Karman or Kirmän, Yāgūt 4, 262sgg.; Cat. 90.
2744:nipast [npst'] place where a thing is deposited, depository, gl. of KLYT’ = gellāitā (v. Ideograms) 107%, — I reject the interpretation of the passage given by Bailey, ZP 152. There is no evidence what- ever of an ideogr. KLYT = QRYT’ being used for diz ‘fortress’. This Aram. w. always signifies ‘village’; in the FrP, ch. 2, it is hidden behind the somewaht be- wildering disguise MRDYN! (-DYN- common. error for -YT-) for MRYT" for QRYT* (cf MDM for QDM) = rētastak (g. v.) A form *ntptst for nipist is no- where attested, so the diz i nipist has to disappear from our context. KLYT? = Aram gellāitā (ultimately from lat. cella) refers obviously in KnS VI, 11 to the sanctuary of the Dragon of Kirman, most probably a cavern. — I deeply deplore the Ahrimanic slip of pen which made me write ntpāst, instead of nipast, as the equivalent of KLYT’ in the Index, I, 160a, 14. A benevolent critic will find the correct reading nipast in I, 157a, 30. - From nipastan; nipast is to nipastan what nisast is to nisastan.
2831:östavär [’wstwb’l] a confidant, pl. cas. obl. ~-dn 1314. — Adj. ‘faithful’ Mx 3911-33, 617, Paz. ztastvär (for xostuvdr), Skr. v. karma-kušala- ‘experimented’, SGV sudak- satara ‘very well qualified’; NP ustuvār; MPrs ’wystw’r pl. ‘the elders of the family’, not to be separated from ava-stā, ava- and avi- having already begun to coalesce in Av.
5372:stáro.koroma: kirm
5656:krm: kirm www.parsianjoman.org | Col )b
6947:khan-: kandan krmi-: kirm ksira-: Sir ksipra-: "šif(a)rg ksubh-: višuftan lapati: rāpak-karēh lup-: *uzruftak maryá-: mérak matsya-: mahik modate: mustäpät, X6sr6i-mustapat muficáti: ämöxtan mus-: must namrá-: a-namr-tom nastikya, nàstika: anäst nikrti- (nikrta-): nikérai ni-vat-: yuvat padäti(ka)-: padätak pävaka-: päk pinasti: pist prarecana-: fréc prareka-: fréc pratyafic-: paitak pravät-, pravätä: yuvat rathyä: rahy rta-: Art-vahist
```


## [2026-10-17T00:02:12.351Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 745,755p PHD.txt; grep -n -E \"^kirm|kirm \" PHD.txt | head -5; grep -n -E \"^(warg|warγ|wlg)\" PHD.txt | head"
}
```


### [2026-10-17T00:02:12.771Z] TOOL RESULT

```
afraid, be ~ tarsidan.
after fraz az, pas az, pay i.
afterwards pas.
again abaz, did, P bid.
against padirag.
karm,
hambāy, (spiritual)
age dad, -sālagīh; old -- pīrīh, zarman(ih), zarwan. aged pir.
ageless azarman. aggression hénih. aggressive mustabarmand. agile čābuk.
agility čābukīh.
agitate ayārdēnīdan. agitated, be — ayārdīdan. agitation ayārdēnišn.
428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
4996:kulang kirrdg sett kargās karkēhan kark karm, kirm karmīr karb, kirb karafs karbunag karzang kardār
```


## [2026-10-17T00:02:14.999Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"kyrm|krm'|kirm\" SOD.txt | head -15"
}
```


### [2026-10-17T00:02:15.370Z] TOOL RESULT

```
6187:/kirm/        kyrm-         snake         Pers.  Jb>m  (worm) 
20757:use-k(i)ran   =^xwrsn  qyr'n,  kyrm 
39683:4834  krm'yr   B  t^1^ 
39684:karmir,  karmir  (kyrmyr,  qrmyr,  krmyr)  ©Pahl. 
39692:4835  krm'yr  kwc'k   B  o^ry^o^r^r- 
39708:4838  qrmyr   M  =>  krm'yr 
39710:4839  krmyr  =*  krm'yr 
39720:kirmist  ©pi.  =»kyrm- 
41461:5106  kyrMn   B  =*  kyr>n,  kr»n 
41488:5111  qyrm   C  *>  kyrm- 
41490:5112  kyrm-   B,  M,  S  > 
41491:kirm,  kirm   (qyrm)  ©<Skt.  krmi   ©nom.  ob.  -y; 
41501:57V32-,  kyrm\  SCE  145,  358;  kyrmw,  TSP  13.18 
41503:5113  kyrmpwn   S  j^  r 'j>- «j^  ^^ 
41504:kirm-pun
```


## [2026-10-17T00:02:17.153Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 41488,41503p SOD.txt; sed -n 39683,39700p SOD.txt"
}
```


### [2026-10-17T00:02:17.664Z] TOOL RESULT

```
5111  qyrm   C  *>  kyrm- 

5112  kyrm-   B,  M,  S  > 
kirm,  kirm   (qyrm)  ©<Skt.  krmi   ©nom.  ob.  -y; 

inst.  -J;  ace.  -w\  pi.  qyrmyst 
snake,  worm 
GMS  140,  512;  TSP  2.1042,  1072,  1073,  1077, 

3.83,  135,  247,  6.9;  SCE  118,  233,  324;  Frag. 

2a.3,  16;  BBB  b90;  MSP  p47;  C2,  51V 12, 

57V32-,  kyrm\  SCE  145,  358;  kyrmw,  TSP  13.18 

5113  kyrmpwn   S  j^  r 'j>- «j^  ^^ 
4834  krm'yr   B  t^1^ 
karmir,  karmir  (kyrmyr,  qrmyr,  krmyr)  ©Pahl. 

karmir;  Yaghn.  kimir;  Arm.  karmir  -^qyrmyr 
red 
VJ  40d,  838;  TSP  3.60  &  etc.  7.8,  22.1;  SCE  87, 

322;  KG  2327;  CII  1990  p83 

4835  krm'yr  kwc'k   B  o^ry^o^r^r- 
karmir-kucak 

having  a  red  beak 

SCE  172;  Gersh.  Sogd.  Cpds.  1945,  144.1 

4836  krmswyn  =*  qrmswhn
```


## [2026-10-17T00:02:20.736Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in kermes crimson carmine vermicelli vermouth vermin vermis verge versus anniversary universe vertebra; do echo \"== $w\"; grep -n -i -E \"^$w[,.]\" KLN_1966.txt | head -2; done"
}
```


### [2026-10-17T00:02:21.076Z] TOOL RESULT

```
== kermes
(eval):1: bad math expression: empty string
== crimson
(eval):1: bad math expression: empty string
== carmine
(eval):1: bad math expression: empty string
== vermicelli
(eval):1: bad math expression: empty string
== vermouth
(eval):1: bad math expression: empty string
== vermin
(eval):1: bad math expression: empty string
== vermis
(eval):1: bad math expression: empty string
== verge
(eval):1: bad math expression: empty string
== versus
(eval):1: bad math expression: empty string
== anniversary
(eval):1: bad math expression: empty string
== universe
(eval):1: bad math expression: empty string
== vertebra
(eval):1: bad math expression: empty string
```


## [2026-10-17T00:02:23.653Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in kermes crimson carmine vermicelli vermouth verge universe vertebra; do echo \"== $w\"; grep -n -i -E \"^${w}[,. ]\" KLN_1966.txt | head -2 | while IFS=: read l rest; do sed -n \"${l},$((l+5))p\" KLN_1966.txt | tr '\\n' ' ' | cut -c1-600; echo; done; done"
}
```


### [2026-10-17T00:02:24.214Z] TOOL RESULT

```
== kermes
kermes,  n.,  the  bodies  of  the  females  of  an  insect found  on  the  kermes  oak.  —  F.  kermis,  fr. Arab,  qirmiz,  ult.  fr.  OI.  kfmi-dza-,  ‘produced by  a  worm’.  See  crimson  and  cp.  carmine, kermess,  kermis,  n.,  1)  an  annual  outdoor  fair in  the  Low  Countries;  2)  in  the  United  States, an  indoor  fair.  —  Du.  kermis,  ‘church-mass’, contraction  of  kerk  mes,  fr.  kerk,  ‘church’,  and mis,  ‘mass’.  See  church  and  Mass, kern,  kerne,  n.,  a  light-armed  foot  soldier  in  an¬ cient  Ireland.  —  Ir.  ceatharn,  ‘a  band  of  sol¬ diers,  a  soldier’

== crimson
== carmine
== vermicelli
== vermouth
== verge
== universe
universe,  n. _ L.  universum,  ‘the  whole  world,  the universe’,  prop.  neut.  sing,  of  the  adjective  uni- up versus,  ‘whole,  general,  universal’,  lit.  ‘turned into  one’,  fr.  Onus,  ‘one’,  and  versus,  pp.  of  ver¬ ier  e,  ‘to  turn’ ;  see  version  and  cp.  words  there referred  to.  L.  universum  is  prop,  the  loan  trans¬ lation  of  Gk.  r h  oXov,  ‘the  universe’,  subst.  use of  the  neut.  of  oXo?,  ‘whole’, university,  n.  —  ME.  universite,  fr.  OF.  universite (F.  universite),  fr.  ML.  Oniversitatem ,  acc.  of Oniversitas,  ‘university’,  fr.  Late

== vertebra
```


## [2026-10-17T00:02:26.825Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in crimson carmine vermicelli vermouth verge vertebra vermin; do echo \"== $w\"; grep -n -i -E \"^ *${w}[ ,]+(n|adj|v)\" KLN_1966.txt | head -2 | while IFS=: read l rest; do sed -n \"${l},$((l+6))p\" KLN_1966.txt | tr '\\n' ' ' | cut -c1-600; echo; done; done"
}
```


### [2026-10-17T00:02:27.458Z] TOOL RESULT

```
== crimson
== carmine
== vermicelli
== vermouth
== verge
== vertebra
== vermin
```


## [2026-10-17T00:02:29.735Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^.{0,3}(crimson|carmine|vermicelli|vermouth|verge|vermin),\" KLN_1966.txt KLN_1971.txt | head"
}
```


### [2026-10-17T00:02:30.038Z] TOOL RESULT

```
KLN_1971.txt:39964:carmine, n., a purplish-red color; adj., of pur- 
KLN_1971.txt:56001:converge, intr. and tr. v., to meet in a point. — 
KLN_1971.txt:59986:crimson, n., deep red. — Sp. cremesin , fr. Arab. 
KLN_1971.txt:74272:diverge, intr. v., to move or be in different direct- 
KLN_1971.txt:81988:encrimson, tr. v., to make crimson. — Formed 
KLN_1971.txt:260618:verge, n., 1) staff or office; 2) limit, margin, edge. 
KLN_1971.txt:260631:verge, intr. v., to bend, incline. — L. vergere, ‘to 
KLN_1971.txt:260743:vermicelli, n., a paste of wheat flour made into 
KLN_1971.txt:260800:vermin, n. — ME., fr. OF. (= F.) vermine , a col- 
KLN_1971.txt:260831:vermouth, n., a white wine flavored with aromatic
```


## [2026-10-17T00:02:32.496Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 39964 59986 260618 260631 260743 260831; do sed -n \"${l},$((l+9))p\" KLN_1971.txt | tr '\\n' ' ' | cut -c1-700; echo; echo; done; grep -n -E \"^ *(vert|wreath|wrap|worm|warp)[a-z]*,\" KLN_1971.txt | head"
}
```


### [2026-10-17T00:02:33.165Z] TOOL RESULT

```
carmine, n., a purplish-red color; adj., of pur-  plish-red color. — F. carmin , fr. ML. carminium ,  a blend of Arab, qlrmiz , ‘worm 1 and L. minium ,  ‘cinnabar, red lead, vermilion’, which is of  Iberian origin. See crimson, and miniature,  carnage, n., slaughter, massacre. — F., fr. It. car-  naggio , fr. VL. carnaticum , fr. L. card, gen.  carnis, ‘flesh, meat’. See carnal and -age and cp.  carrion, charnel.   


crimson, n., deep red. — Sp. cremesin , fr. Arab.  qirmiz, ult. fr. OI. ‘produced by a      177     


verge, n., 1) staff or office; 2) limit, margin, edge.  — ME., fr. MF. (= F.) verge, ‘rod’, fr. OF., fr.  L. virga , ‘twig, rod, wand’ (whence also It.,  Proven?., Sp., Port, verga. Rum. vargd); see  virgate and cp. whisk. The sense ‘limit, margin,  edge’, developed from the meaning ‘staff of  office’, through the medium of the term within  the verge used in the sense ‘within the sphere of  authority of the Royal Steward’.   


verge, intr. v., to bend, incline. — L. vergere, ‘to  bend, incline, turn’, prob. cogn. with OI. vf nak-  ti, vdrjati , ‘he turns, twists’, fr. I.-E. base *we-  reg-, *werg~. See wrench and cp. converge, di-  verge.   verger, n., an officer of the church. — ME., lit.  ‘one bearing a verge’, formed fr. MF. verge,  ‘staff’ (see verge, n.), with agential suff. -er. Cp.  ML. virgarius in the same sense,  


vermicelli, n., a paste of wheat flour made into  wormlike threads. — It., pi. of vermicello, ‘little  worm’, fr. VL. *vermicellus, dimin. of L. vermi-  culus, itself dimin. of vermis , ‘worm’. See Ver-  mes.   Derivative: vermicelli, adj.  vermicide, n., a substance killing worms. — Com-  pounded of vermi- and L. -cida, ‘killer’, fr. cae-  dere, ‘to kill’. See -cide, ‘killer’.  


vermouth, n., a white wine flavored with aromatic  herbs. — F. vermout, fr. Gk. Wermut, which is  rel. to wormwood (q.v.)-   vernacular, adj., native to a country; n., one’s  mother tongue. — Formed with adj. suff. -ar fr. L.  vernaculus, ‘bom in one’s house’ (said of slaves),  ‘native’, fr. verna, ‘a slave born in his master’s  house’, a word of Etruscan origin.   


8176:vertere, ‘to turn toward’, fr. ad- and vert ere, ‘to 
8205:vertir, resp. avertir. See advert and -ment. 
57137:wreath, crown’, fr. Gk.xopcov^, ‘anything curved ; 
68360:verting, distorting* fr. depravdtus , pp. of depra- 
84137:vertebra, and indeed, originally epistropheus was 
88333:warp, begin’, which is rel. to ordo, ‘a straight 
168460:warp, begin’, and cogn. with Gk. opSetv, ‘to be- 
182464:wrapper, worn over the diaper. — ■ - OE. pylece, 
260554:vert, ‘green’. Cp. It. verdeggiare. Proven?, verde- 
261034:vertical, vertigo, vervel, vice versa, vortex,
```


## [2026-10-17T00:02:40.394Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"urvis|urvaes|urva[eē]s\" KLN_1966.txt KLN_1971.txt | head; sed -n 261020,261036p KLN_1971.txt; grep -n -E \"^ *worm,|^ *wormwood,|^ *wrench,|^ *wrist,|^ *wry,\" KLN_1971.txt"
}
```


### [2026-10-17T00:02:40.683Z] TOOL RESULT

```
KLN_1971.txt:75471:ditrys , Lett, dutis , durvis , OPruss. dauris , ‘door’, 
KLN_1971.txt:268849:Avestic urvisyeiti , ‘turns, revolves’, Gk. £oix6<; 
See -ward, weird, worth, ‘to become’, and cp. 
adverse, adversity, advert, advertise, animadvert, 
anniversary, a rovescio, averse, aversion, avert, 
controverse, controversy, controvert, conversant, 
conversation, converse, convert, dextrorse, divers, 
divert, diverticulum, eversion, evert, extrorse, 
extroversion, extrovert, inadvertent, introrse, in- 
troversion, introvert, inverse, inversion, invert, 
malversation, obverse, obversion, obvert, perverse, 
perversion, pervert, quaquaversal, retrorse, re- 
troversion, retrovert, reverse, revert, sinistrorse, 
subversion, subversive, subvert, suzerain, ter- 
giversate, transverse, traverse, universe, univer- 
sity, verse, verso, verst, versus, vertebra, vertex, 
vertical, vertigo, vervel, vice versa, vortex, 
vortical, vorticism, vortiginous. For the ending 
of version see suff. -ion. I.-E. *wert- is a -/-en- 
268335:worm, n. — ME. werm, worm , wurm, fr. OE. 
268339:worm, ON. ormr, Dan., Swed. orm, Goth. 
268354:wormwood, n. — ME. wermod, fr. OE. wer mod, 
268627:wrench, n., a sharp twist. — ME. wrench , ‘guile, 
268643:wrench, intr. and tr. v. — ME. wrenchen, fr. OE. 
268718:wrist, n. — ME. wrist, wirst, fr. OE. wrist, rel. to 
268840:wry, intr. and tr. v., to twist. — ME. wrien, ‘to
```


## [2026-10-17T00:02:42.636Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 268335,268365p KLN_1971.txt; sed -n 268840,268856p KLN_1971.txt; grep -n -E \"^ *version,\" KLN_1971.txt"
}
```


### [2026-10-17T00:02:43.328Z] TOOL RESULT

```
worm, n. — ME. werm, worm , wurm, fr. OE. 
wyrm, wurm, ‘serpent, dragon, worm’, rel. to 
OS., OHG., MHG., G. wurm, OFris., Du. 

worm, ON. ormr, Dan., Swed. orm, Goth. 
waurms, ‘serpent, worm’, and cogn. with Gk. 
p6p,oi; (Arcadius), (5>6^o£ (Hesychius) (for 
*Fp6p.o<;, resp. *Fp6p,o^), ‘woodworm’, L. ver- 
mis (for *wormis, *w{mis), ‘worm’, ORuss. 
vermie (coll.) ‘insects’, OPruss. vormyan, urmi- 
nan , ‘red’, lit. ‘of the color of a worm’, Lith. 
vafmas, ‘insect, gnat’. All these words derive fr. 
I.-E. base *wer ‘to bend, turn, twist’. Cp. 
Vermes and words there referred to. For deriva- 
tives of *werg- and * wergh-, enlargements of 
base *wer- see verge, ‘to bend’, worry. 
Derivatives: worm, v., worm-er, n., worm-less, 
adj., worm-y, adj.*, worm-i-ness, n. 

wormwood, n. — ME. wermod, fr. OE. wer mod, 
rel. to OS. wermoda, MLG. wermot, wermode, 
Du. wermoet , OHG. werimuota , wermuota , 
wormuota , MHG. wermuote, wormuot , G. 
Wermut. Cp. vermuth. 

worn, pp. of wear , ‘to carry on the body’, — ME. 

worn, woren, fir. OE. geworen. See wear. 

worry, tr. and intr. v. — ME. worien, fr. OE. 

wry, intr. and tr. v., to twist. — ME. wrien, ‘to 



turn, twist’, fr. OE. wrigian, ‘to strive, go for- 
ward’, rel. to OFris. wrigia, ‘to bend’, MLG. 
wrich, ‘turned, twisted’, and prob. rel. also to 
MHG. rigel , ‘kerchief wound around the head’, 
OE. wrigels, ‘covering, veil’, and cogn. with 
Avestic urvisyeiti , ‘turns, revolves’, Gk. £oix6<; 
(for *wroikos), ‘crooked’, L. rica, (for *wreikd), 
‘veil to be thrown over the head’, Lith. raiSas, 
‘paralysed’, riSu, risti, ‘to bind, tie’, rykste , ‘rod, 
wand, stick’. All these words are derivatives 
of I.-E. *wreik -, *wrik -, ‘to turn, twist, bind’, 
which is an enlargement of base *wrei ‘to 
turn, twist’. See writhe and cp. words there re- 
261001:version, n., 1) translation; 2) account. — MF.
```


## [2026-10-17T00:02:47.044Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *(writhe|wreath|wrap|warp|wright|wrinkle|wrist),\" KLN_1971.txt | head; l=$(grep -n -E \"^ *writhe,\" KLN_1971.txt|head -1|cut -d: -f1); sed -n \"$l,$((l+15))p\" KLN_1971.txt; grep -n -i -E \"Avestic (var|a-?var|avar)\" KLN_1971.txt | head -20"
}
```


### [2026-10-17T00:02:47.592Z] TOOL RESULT

```
57137:wreath, crown’, fr. Gk.xopcov^, ‘anything curved ; 
88333:warp, begin’, which is rel. to ordo, ‘a straight 
168460:warp, begin’, and cogn. with Gk. opSetv, ‘to be- 
209701:wrinkle, furrow’, in VL. also used in the sense 
209742:wrinkle, curl’. Cp. also ruff, ‘large collar’. 
221180:writhe, dry up, shrink’, MLG. schrimpen , MHG. 
221202:writhe, dry up, shrink’. See shrimp and cp. 
265107:warp, n. — ME., fr. OE. wearp , rel. to MLG. 
265108:warp, OHG., MHG. warf, ‘warp’, ON. varp, 
265114:warp, tr. v., to bend, twist; to distort; intr. v., to 
writhe, dry up, shrink’, MLG. schrimpen , MHG. 
sc hr imp fen, and to E. scrimp and shrink. 
Derivatives: shrimp, intr. v., shrimp-er, n., 
shrimp-ish , adj., shrimp- ish- ness, n., shrimp-y, 
adj. 

shrine, n. — ME. schrin , shrin , fr. OE. serin , ‘the 
Ark of the covenant’, fr. L. scrinium, ‘a case for 
keeping books’, which is of uncertain origin. It 
possibly denoted orig. ‘a round or plaited re- 
ceptable’, and derives fr. I.-E, base *(s)qer- , -to 
bend, turn, twist’, whence also L. curvus , ‘curved, 
crooked’. See curve, n., and cp. scrinium. 
shrine, tr. v., to enshrine. — ME. shrinen , fr. 
shrin. See shrine, n. 

132734:*wollc-o-, whence also Avestic var s sa~, ModPers. 
237750:*sul~, ‘sun’, whence also Avestic Avar*, Gk. 
261007:vf ttih y ‘the act of rolling’, Avestic var*t-, ‘to 
268217:whence also OI. urnd, Avestic var^na, Arm. 
268294:whence also Avestic var e za, ‘work, activity’, 
268454:cogn. with Avestic avar^ta-, ‘a valuable object’,
```


## [2026-10-17T00:02:49.398Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 268440,268465p KLN_1971.txt; sed -n 265107,265125p KLN_1971.txt"
}
```


### [2026-10-17T00:02:49.883Z] TOOL RESULT

```
ON. rdt, ‘root’, and cogn. with Gk. p£oc, Lesb. 
Pp£a8a, ‘root’, £dc8a|xvo<;, ‘branch’, L. rddlx, 
‘root’. See radix and cp. ifiizo-. Cp. also root 
and the second element in mangelwurzel. 
wort, n., infusion of malt before fermentation. — 
ME. wurte, fr. OE. wyrt, rel. to OS. wurtia, ON. 
virtr, Du. wort, OHG. wirz, MHG., G. wurze , 
G. Bierwiirze, ‘wort’, and to OE. wyrt, ‘root, 
plant, herb’. See prec. word, 
worth, adj. — ME. wurthe, fr. OE. weord , 
word, ‘worthy’, rel. to OS., OFris. werth , ON. 
verdr, Dan. vxrd, Swed. yard, Du. waard, OHG. 
werd, MHG., G. wert, Goth, wairps, ‘worth, 
worthy’, and to OE. wierde, of s.m., and prob. 
cogn. with Avestic avar^ta-, ‘a valuable object’, 
W. gwerth , ‘price’. OSlav. vrddu, OPruss. werts 
and Lith. veftas , ‘worth’, are Teut. loan words. 
Cp. worth, n., worthy, the first element in wor- 
ship and the second element in stalwart, 
worth, n., value. — ME. wroth , fr. OE. weord , 
wurd, wyrd , ‘worth, price, redemption, ransom’, 
rel. to OS. werth, ON. verd, OFris. werd, wert , 
Du. waarde , OHG. werd, MHG., G. wert, 
‘worth, value’, Goth, walrp , ‘price, value’. 
These words are prop, substantiations of the 
adjectives: OE. weord, resp. its equivalents, in 
warp, n. — ME., fr. OE. wearp , rel. to MLG. 
warp, OHG., MHG. warf, ‘warp’, ON. varp, 
‘cast of a net’, Dan. varp, ‘warp’, and to OE. 
weorpan , ‘to throw’ ; see warp, v. In some senses 
the noun warp derives directly from the verb 
warp. 

warp, tr. v., to bend, twist; to distort; intr. v., to 
become bent or twisted. — ME. war pen, fr. OE. 
weorpan, ‘to throw’, rel. to OS. wer pan, ON. ver- 
pa, ‘to throw’, Dan. vxrpe, Swed. varpa, ‘to lay 
eggs’, OFris. werpa, MLG., Du. werpen, OHG. 
werpan,werfan, MHG., G. werfen, Goth.wairpan, 
‘to throw’, and cogn. with Lith. verpiu, verpti , 
*to spin’, varpste, ‘spool, distaff’. See vervain and 
cp. words there referred to. 

Derivatives: warp-ed, adj., warp-er, n., warp-ing, 
n. and adj.
```


## [2026-10-17T00:02:54.191Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"var.?e?p|urup|varap\" KLN_1971.txt | grep -i -E \"avest|OI|mark\" | head; grep -n -E \"^ *write,\" KLN_1971.txt; l=$(grep -n -E \"^ *write,\" KLN_1971.txt|head -1|cut -d: -f1); sed -n \"$l,$((l+14))p\" KLN_1971.txt"
}
```


### [2026-10-17T00:02:54.557Z] TOOL RESULT

```
231745:with Gk. axa\jp6^, of s.m., OI. sthdvardp, ‘thick, 
268745:write, tr. and intr. v. — ME. writen, ‘to write’, fr. 
write, tr. and intr. v. — ME. writen, ‘to write’, fr. 
OE. writan , ‘to engrave, scratch, draw, write’, 
rel. to OS. writan, ‘to tear, scratch, write’, 
OFris. writa, ‘to write’, ON. rita , ‘to scratch, 
write’, Swed. rita , ‘to draw’, OHG. ri^an, 
MHG. risen, G. reifien, ‘to tear, pull, tug, 
sketch, draw, design’, OE. writ, ON. rit, ‘writ- 
ing’, OHG. Wj, ‘stroke, letter’, MHG. riz, ‘tear’, 
G. RiJJ, ‘tear, gap; plan, design’, Grund-rifi , 
‘first sketch, design, plan’, Reifi-zeqg, ‘drawing 
instruments’, Goth, writs, ‘stroke, line, letter’, 
and possibly co gn. with Gk. ptwj (for *Fpfv?)), 
‘file, rasp’; cp. writ. The origi meaning of OE. 
writan, etc., was ‘to cut letters in bark or wood’. 
For sense development cp. Heb. kdthdb, ‘he
```


## [2026-10-17T00:02:58.753Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *wrap,\" KLN_1971.txt; l=$(grep -n -E \"^ *wrap,\" KLN_1971.txt|head -1|cut -d: -f1); [ -n \"$l\" ] && sed -n \"$l,$((l+10))p\" KLN_1971.txt; grep -n -E \"^•.{0,6}(varap|var.p|urup|urvap)\" BRT.txt | cut -c1-300 | head"
}
```


### [2026-10-17T00:02:59.196Z] TOOL RESULT

```
268542:wrap, tr. and intr. v. — ME. wrappen , of uncer- 
268820:wrap, ‘angry’, rel. to OS., OFris. wreth, ON. 
wrap, tr. and intr. v. — ME. wrappen , of uncer- 
tain origin. 

Derivatives: wrap, n., wrapp-age, n., wrapp-er , 
n. and tr. v., wrapp-ing . 

wrasse, n., a European seafish. — Co. wrach, 
gwrach , gwragh, rel. to W. gwrachen, ‘wrasse*, 
wrath, n. — ME. wrathe , wraththe , fr. OE. wrxp- 

po , wrxppu , ‘anger’, fr. wrap , ‘angry’, orig. 
22925:•  j.  varsp-  V,,  nur  mit  aiwi  'mit  einem  l-"g'  <>"  />iuuj''i>rbergs  *.  Bd.  /?.  i.  37.    Im
25526:•  j.  urupay-m.EN.  des  zweiten  iranischen Königs,  eines  altem  Bruders  Yimas,  der ihm  nachfolgt"':  taxmO  °/a  (NS.)  asinavä Yt.75,11;  —  kavann  x'ar»nB  . .  yat  upa- nhaca^  taximm  'pi  (alsAS.)*'  azinavantam .  .  yat  barata  anrim  mainyBm  framittm (sd.)  aspahe  kihrpa
```


## [2026-10-17T00:03:01.186Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22925,22928p BRT.txt | cut -c1-1200; grep -n -E \"varsp|varəp|varp\" BRT.txt | head -5 | cut -c1-200"
}
```


### [2026-10-17T00:03:01.589Z] TOOL RESULT

```
•  j.  varsp-  V,,  nur  mit  aiwi  'mit  einem  l-"g'  <>"  />iuuj''i>rbergs  *.  Bd.  /?.  i.  37.    Im
Zeichen  versehen'.     Praes.  i  var>6-.  ^"'.fT.^f^'  j  ilS"?  ^^"^■*'-  ''*■
,,        /»iiv       -L                                 ■       I  Ablot  —  EL  und  Bed.p   VgL  vonFuiuncbk
etwas  (AkL)  zeichnen,  signiren  mit  -  k;:.  3^.  ^^^  „n  Johanssow  Bß.  /*.  19.   Die
3684:sa3^3rJ{iA.)  . .  ya  ..  vav}r?SSi  pairlJült ..  yäia  var?^aitg  '/LcTblJ  Y.  25,4;  — ai^qmät  ä  ahtnJ  .  .  vTci>3i  (sd.)  -/)"■■>  Y. j2. 8.  a)  mit  Neg.;  'nicht  hinfort  mehr, län
6656:—  hyalca  msi  Ayjt  vaxi  aeüf  (sd.)  Y.  ij.ioo.  Anhang,  i)  Bei  mehreren 4^.17;  4j-i6; — yii*zrazd^  (sd.)  avk?/i  Subjekten  kann  das  adjektivische  Praedi- mazdli  Y.j/.  i;  —  dmj
6861:garS  nmartptn  mai^anpm  'rahe  mazdä  V, '5-3*i  Vr.7.  I,  Vt.j.4(?);  —  vahiits aiphul  yö  mana  yat  °rahe  mazda  P.  4"; '^'^•33\  —  "vi  'rahe  mazdä  .  .  gätvS zaranyöjants  V,  ;p.
8686:•  j.  u§-  n.  'Ohr'  uzw.  «^»rischer  Wesen'': k/(NS.)  F.9(?).  A)  sonst  nur  Du.;  a)  'die Ohren':  yezi  *kva£ibya  ''-sibya''^^  aiwi.- srunvaifi  . ,  yezi  äat  nöit  /ivagibya  "Hbya
8860:amanha  asti  masyd  gfurvaya  hl . .  zUvarp Y.p.28;  —  ai  .  .  mainyßm  zara%uströ v^jtttl  (sd.)  yaste  I  ascil  spSmstd  Y.  43.16; —  ySi  mffi  ahmii  s^rao/^m  dqn  I  cayasla (NP.) "
```


## [2026-10-17T00:03:05.240Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^•.{0,6}a?var.ta-\" BRT.txt | cut -c1-600 | head"
}
```


### [2026-10-17T00:03:05.567Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:03:07.499Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"avar[^ ]{0,3}ta-\" BRT.txt | cut -c1-500 | head"
}
```


### [2026-10-17T00:03:07.964Z] TOOL RESULT

```
5116:avarata-  176
```


## [2026-10-17T00:03:09.650Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5108,5124p BRT.txt | cut -c1-800"
}
```


### [2026-10-17T00:03:10.026Z] TOOL RESULT

```
•  j.  ava-yam-"  f.  'Abwendung*;  aSat  te .  .  aiAke  °yqm  (AS.)  *dqnmaki  yat  %'W3 didvtsma  "das  machen  wir  dir  .  .  zur  Ab- wendung dessen,  dass  wir  dich  beleidigt haben"  Y.  68.  i.
KompE.  —  Zum  V.  j-a«- 1) ;  ai.  vgl.  avayäldr- m.  —  Fü. :  pa  aySviirik.  —  ■)  Anders  (falsch) Gdh.  KZ.  iS.  407,  Jn.  JAOS.  13.  ccxu,  Bthi. JF.  3.  37  und  S  SSi- j.  avayäl  F.  7:  lies  avdiil.
•  j.  avavaitya  Adv.  'tantundem',  mit  Akk. der  Beziehung;  als  Korrelat  folgt  ya^a: pairi  dim  tanava . .  urväntm  . .  av  bazascä frakasla  fairi.tanuya  yai^a  Im  zS  Y.79.7,
LS.  aus  atiavanl-,  —  Pü.:  pa  äiti  and  takäk  » faknäk.
•  j.  avavat  Adv.  'in  solcher  Grösse,  Masse, Entfernung,  Weise;  ebensosehr,  ebenso': *av'  F.  7  " ;  —  'vatat  Vd.  75.  a)  sonst  1 mit  dem  Korrelat. ^a^u :  ye^Ju  av  . .  tüti  1 SpS  ava.barpnte  yaia  vupa  imi  äpS  .  . Yt  5.  1 S ;  —  ^^  haca  iristaäbyS  yaia ^rigäim  V.Äii;  39,  76,  p.39;  — yd^a iattm  kaydhanqm  av  asava./aalYt  JO.z; — y3  av°  xSva^zvs  vasaiti .. yäka  tiyris.. YtÄö;  —  'vaiai  yaka  kv5  ptruahe'^. 7.53  PüZ.
ASn,  aus  avavant-.  —  K.:  an  i  and,  (Vd.):  and {and.  —  ')  Hds.  aj-aial.
'].  avaz'at  Yl.  5.  ISO:  s.  iaV:
•  j.  ava'vant-  Adj.  (fem.  'vaitf-)  'tantus; talis':  °Tani>m  asavayny,li  (sd.)  tarn  ctiqm daisayS  V.  5. 14(?).  A)  sonst  mit  dem Korrelat',!'!!^!!;   1) 'wie,  als':   -i'atät yaka
avarata-  176
sükaya  (sd.)  bräZ3m  Yt  14.  33;  33;  — jainü  mqm  ahuna  vairya  "vata  snai>isa ya%a  asma  . .  YtZ/.ao;  P.22;  —  kthrpa 'vatS  (GS.)  *sraya  (sd.)  ya%a  dämqii sralstail'^.2.^;  —  ifkrpa  "vatqm  sraya ydka  di'iayatqm  zaosS  (sd.)  Yt  17. 1 1 ;  — st»r)naoili  aria  *°vat  starim  .  .  ya'ia  .  . P.25(?).  a)  substantivisch  'Wntum',  mit Gen.  part:  yat  mS  'va(  daüvayasnanqm ni/atitn  ydka  .  .  Yt  J.77;  —  upa  .  .  'vat siWi/  (sd.)  urva  *isaiti  yd^a  .  .  H.  2. 2.  b)  mit  Akk.  der  Beziehung:  andern .  .  y3  asti  'vaiti  masö  yd^a  vJspa  ima äpS  Y.  65. 3 ;  — yash  . .  "vant^m  (als  ASn.) mass  vikilnayät  ya'ia  hi  tanus  atphat  V. 7.51.  a)  mit  ya'i:a  yat  'wie  wenn,  als ob':  °vaia  aejanha  yd^a  yat  panca  narS "mit  solcher  Kr
ana  'vat  uxhaia  (sd.)  ya^a..  nT..  haraite Y.ig.io.  a)  mit ^yaSd^a/ 'dass':  astü'a 'ahmt  'vat  kavaim  o^arinS  ya'^a  yat .  . \us./raz>ayffii(sd.)  Yt/p.68.  ASn.  -vat und  LS.  'vaitya  als  Adv.  sbes.  [V.  6.  i  o,
aa,  ^'.23:  lies  avat\
Pü.:  an  i  and,  (lU  H.)r  llön.
•  j.  nSit  aitahe  uzarsnS  nai6a  varS  ava- väite  (3S.)  P.5^:-?-.
Pü.:  apc  äycl;  also  lu  ^ay-  mit  ui'ij?
•  j.  avam  Adv.  'hinab,  herab';  F.  7.
KompA.(?).  —  Vgl.  >u7fl,  aoj-Ji),  —  ai.  avar Adv.  {RV,  /.  133.  7).  —  Pü.:  aväk.  —  »  Vgl. liTHL.  IF.  //,    140;  E.  auch  aiia:in^.
```


## [2026-10-17T00:03:12.440Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"avar.{1,3}ta[- ]\" BRT.txt | cut -c1-300 | head -20"
}
```


### [2026-10-17T00:03:12.853Z] TOOL RESULT

```
5116:avarata-  176
7036:aahat  ästais  . .  ä°  yezi  aahaj  anäsiütS  . . V.^.40;  5.28-35",  7.13,  IS,  75',  ■^'■37, 99,  106;  —  yeüca  hz  anya  aya  fyao%na fravarita  .  .  ä'  yezi  //  .  .  rigij  fravarila Y.3.21;  Vd.2  aSt  ß)  yezi  .  .  aiwi.- srunvaili  .  .  yezi  J-  nsit  aiwi.surunvaiH N.  26;  
7262:atihat  äsfütS  . .  ä°  yezt  atihat  anastals  . . V.J.40;  5.28-35",  7.13,  15,  75',  ,V.37, 99,  106;  — yeiica  ht  anya  aya  syao%iia fravarsta  .  .  ä°  yeii  sl  .  .  nsit  fravarSta V.J. 21;  Vd.2  2 St  ß)  yezi  .  .  aiwt.- srunvaiti  .  .  yezi  ä°  nOii  aiwi.surunvaiti N.  2
14937:•  j.  paitita-  Adj.  (fem.  =«-),  PPfP.:  s. ^ay.  A)  n.  a)  'Begleich'  von  Schuld und  Strafe:  äa^  jim  il  anya  aya  i'yao%na nSil  fravarsta  'Dm  ahe  nars  yaval'a yavaSataica  "wenn  er  aber  andre  Übel- taten nicht  begangen  hat,  so  gilt  der (Schuld)begleich  dieses  Man
21771:ipaläl  barSit  '^.bg;bg; — y  nasus  aiwL- ynixta  ..  aitihä  £>mU  nidai^yqn  V.  7. 30; ag;  —  neben  *yat:  yast  %ina  . ,  pahqm (sd.)  Jasaiti  vq%waits,  bsiwranqm  . .  *sica hwaifä{sd.)  tanvB  a'ha  imqm  vaSs  drm- Jayöil  Yt  13.  30.  d)  ist  das  Verbum weggelassen:  y  hsi  
28470:yöi  vtnsinti  masyaka  V.  75,  : 4.  20  ("ä«-),  so  {-^s«');  —  aat  yeti  h anya  aya  '^na  »Sil  /ravar/ta  paitifym (sd.)  ..  V.^.  21;  ji;  —  ^riiBm  aSake -'hnahe  baxhnli  V.  8.  100;  —  cval  aitaliqm '%nanqm  ästäraiti  (sd.)  V.  13.  20 ;  —  aita/ie '  nahe yaha  uatijrtt
```


## [2026-10-17T00:03:17.025Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^•  j.  a.{0,4}var\" BRT.txt | cut -c1-250 | head -20"
}
```


### [2026-10-17T00:03:17.809Z] TOOL RESULT

```
3882:•  j.  aiwi.varSta-  Adj.  (fem,  "/(-)  'be- regnet, worauf  es  geregnet  hat':  vlsp3m\ a  ahmät  nasunam  -a  'ianqm  daxmanqmca ' 'tanqm  hixranqmla  'tanqm  vayanqmüi frariuhantanqm  "bis  dass  es  auf  die  Leich- name geregnet  und  .  
4713:•  j.  anvarJitavas't?ma-<>  Adj.  (fem,  °m3-) etwa  'der  am  will  fahrigsten,  geeignetsten wirkt*:  fravasayö  'tfmä  frascimbananqm ". .  die  geeignetsten  unter  den  StÜUbalken" yt.y.26.
4748:•  j.  anyo.var«na-''  Adj.  'der  einen  an-  Vt. ä  12;  H.  j.4,  V.  1^64.  AJalsGott- dern  Glauben  hat,  andersgläubig':  °ii<ii  vä  heil  (der  AngrilTskraft)*' :  ^^«/. .  ,y//«  w/am anys.lkaliai  vä  V.  15. 2 ;  —  yal  iqinät  vä  
5127:•  j.  avar«'gav-  m.  EN.  eines  Gläubigen: "gSuH  fnzavaiö  *öiymatastura/ie  asaonö "des  Ä.,  Sohns  des  ^.,  Sohns  des  Ö."  Yt
5129:•  j.  a-var»tä-f.  'Wertgegenstand,  Besitz- tum': siaritasca  g3tus  any5sia  bfrfxiia^sA.) °tä  Yt  //.  7 ;  —  yesi  rn'it  iavan  .  .  pas^m staoräca  aw^qm  hl  'Iqm  altahmifi  naire frabi!ray?n  V.5.39;  ig.id;  —  zur5.bir»ta ,'iä  F
5139:•  j.  avara'Srabah-  m.  EN.  eines  Gläu- bigen :  'batshs  r3starf.i'ayp)itiiii'{%A.)  aiaonS W  13.106,  —  'ba  (NS.)  Dk.  7.7,  ao,  zi,: .V.i3.i8'>.  j
5918:•  j.  a-svar-  :  'ssr-  n.  'Morgendunis  el, -dämmening':   'sSiri  (LS.)  süirim  ispmnS .»  j.  'a-srata-  Adj.  (fem.  'tä-)  'nicht  ge-
6548:•  j.  as-varacah-  Adj.  'der  grosse  Kraft,  j  eines    Gebrechens    od.    dgl.:    paitistatse Tatkraft  besitzt':  frar^rase  tarS  'ia  Yt.  19.  yaskaAe  .  .  makrkahe  .  .  'hvaAe  V.  20.  3. 57,58;    —    Vö    yai:a    kava    u
7607:•  j.  a-varazika-"  Adj.  (fem.  °zikii-)  'nicht wirkend,  faul':  druxi  ojfä^re  'ke  (VSf.) ' V.  /*.3o.  I
```


## [2026-10-17T00:03:19.678Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5129,5132p BRT.txt | cut -c1-900"
}
```


### [2026-10-17T00:03:20.006Z] TOOL RESULT

```
•  j.  a-var»tä-f.  'Wertgegenstand,  Besitz- tum': siaritasca  g3tus  any5sia  bfrfxiia^sA.) °tä  Yt  //.  7 ;  —  yesi  rn'it  iavan  .  .  pas^m staoräca  aw^qm  hl  'Iqm  altahmifi  naire frabi!ray?n  V.5.39;  ig.id;  —  zur5.bir»ta ,'iä  F.:.'0;  —  Ptspanqm  *°tanqm  saiiavai-
dby  Google
177
avareS'a-
```


## [2026-10-17T00:03:24.277Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"wropal|ropal|r[oō]palo|k[uū]p[aā]l|gopal|g[uū]p[aā]l\" IEC.txt | head; grep -n -i -E \"k.?rmi|qrmi|kwrmi\" IEC.txt | head -5"
}
```


### [2026-10-17T00:03:24.619Z] TOOL RESULT

```
19013:tropolos, is (tropil-) ‘turn, twist’. Cf. tropeio and next Br. tróel, pl. -u, f. ‘bindweed’; W troell, pl. -au, f. ‘whirl; pulley’ beside trol, pl. iau, f. ‘cylinder, roll’; (for Gk. tropalízo, v. ‘turn’, see troqueió below)
8445:kurmos (2) (?) (a creature ‘creeper, crawler’ ?) Skt. cf. kürmah, kurmih, m. f. ‘tortoise’; Li. kurmis, io, m. (‘mole’, zool.); Latv. kurmis, id.
14261:red See next and cf. WP I, 523 Alb. cf. i krym(b)un ‘worm-eaten’; W pryfyn, m. ‘worm’; OCS érümini, adj. "red R Cerm- nyj, id.; Li. kirminas, adj. of a worm’; kif- minas ‘worm’
14262:qurmis (i-basis) *worm, grub'. WP I, 523. (Variant: qurmà) Skt. krmih, m. id.; Av. (variant) koroma, f. id.; Per. kirm, id.; Oss. kalm, pl: kàlmitá, id.; (LW in Arm. Seram, o-st. 'silkworm"); Alb. krimb, krymb, krym, m. ‘worm, grub’; MIr. cruim, Ir. cruimh, m. id.; Br. prév, prénv, m. id.; W pryf, pl. -ed, m. id.; Cor. pryf, coll. (sg: preven), f. id.; OCS cf. éórüminü, R čermnyj, adj. “crim- son’; Li. kirmis, gs: -iés, f. ‘worm, grub’; Latv. cirmis, kirmis, id. Extn. of type qurmón-, -en- in Br. préon, m. *worm' beside am-prévan, m. ‘vermin’; Cor. preven, f. ‘worm’; Li. kirmuó, gs: -efis, id. (a parallel formation occurs in Lat. vermen, n. ‘colic’, vermina, npl. ‘vermin’ in relation to vermis ‘worm’. Cf. uerm-, urm-)
15496:harr, herr, v. *weed'; Old Lat. scarreo, ere, v. ‘be rough'; G scharren, v. ‘scratch, root, scrab- ble, shuffle, hawk, cough'; Scharre, f. ‘rasp; raspings'; ON skarr, n. ‘skirmish’ beside skars, skass, n. ‘ogress’. (NB. A form *skors- in im- plied in Arm. xorem, v. (dig). Cf. also Norw. skarre, v. (‘burr the ‘r as in Bergen dialect) (skat- (1) jump, dash, spout'. See sKat-) skat- (2) “hit, strike, touch'. Cf. skot-. (Alb. ambig.) Alb. has, v. aor: hasa “hit, touch, meet: MIr. & Ir. scathaim, scaithim, v. “cut, lop, destroy” skaudhos (ksaudhos?) ‘miserable, poor, lean, abject'. Variants in OPer. & Arm. Ober. cf. skauðis, adj. ‘mean, poor, feeble’; Arm. xawt, i-st. (ilU, fr. a type *skaustis, but cf. Ober, fr. *skauth-); ON skauó, f. *cow- ard”; Du. cf. schooien, v. (cringe, beg’, if fx. *skaudh- in this sense); Blg. skuden, f: skud- na, adj. “poor, wretched'; cf. Ukr. pa-skuda, s. ‘lecher’; Li. skaudüs, adj. ‘painful, offen- sive; man skauda “it aches’; skaudZiü, inf: skaüsti, v. ‘offend’; Latv. cf. skaudrs, adj. ‘keen, painful. (Variant of uncertain phono- logy in Srb. hud ‘bad’; Cz. chudý ‘poor’, dial: Jean’, and R xudój ‘bad; ill; lean’; xudà ‘blame, abuse’, fr. *ksaudh-, *qusoudh- or sim. Cf. Oss. cawd "bad fr. a variant *sKaudh-?) skaug- Sw. skóka, f. ‘whore’; Li. skaugüs, adj. *miser- ly’; skáugis, ‘miser’; Latv. skaugis, m. ‘envious person’ but cf. skaudigs ('envious'. See above) (skaul-, see ksaul-. Thus only in W ysgawl, adj. ‘vehement, dashing’) skaupos, å ‘tuft, bunch, sheaf Lat. (dial.) scopae, fpl. ‘broom’; scopo, are, v. (sweep. WH & EM untenable); (W cf. ysgaw, Br. skað, Cor. scaw.'elder? but the semantic link is obscure); MHG schoup, gs: schoubes, sm., Du. schoof, f., OE sceaf, m., ON skauf, n. ‘sheaf, bundle’; LG Schauw, wf. “flock, swarm’; cf. ON sküfr, m. ('tuft, topknot,, fr. *sküp- or *skübh-); Big. cf. (dial.) skupü, m. “collection, heap', sküpom ('to- gether, unless from a dialect of Srb. type, *su- and *komp-. Thus Mladenov. Isophonic: OCS pro-skupü *depraver, profaner’; -sku- pístvo 'depravity')
15786:skolbh- (2) (?) “shake; iris, reed" Mir & Ir. scolb, m. (2) ‘skirmish, battle’; ON skelfr, adj. ‘shaky’; skelfa, wv. (cf. OE scelfan, sv. 3. ‘shake, sway”, e-gde fr. *skelbh-: ON skjálfa, sv. 3.); Du. schelf, f. ‘rushes’; G (fr. LG) Schilf, n. ‘reed’
```


## [2026-10-17T00:03:27.523Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"wrop|uropal|rhop|r[hp]opalon|club, mace|mace\" IEC.txt | cut -c1-600 | head"
}
```


### [2026-10-17T00:03:27.820Z] TOOL RESULT

```
186:Mac. Macedonian ME Middle English
1094:bhakso, io (bhask-) (1) ‘strike dumb; be dumbstruck. Arm. baxuk ‘mad’; Gk. (fr. Thrac. or Maced.) baskaíno ‘charm’: Gk. phaskaíno, id. beside báskanos ‘malicious; sorcerer’; Lat. fascinum ‘charm’; Alb. cf. beh ‘surprise’; MIr. cf. bas- call, baisceall “mad; lunatic; Sw. baksna ‘surprise’; Slovene (?) bo&iti ‘gape, stare’ (infl. by Tk. bos ‘empty’)
1326:bhisoros, bhisros “bright, clear” Gk. phiarós, id.; Blg. bistár, id.; cf. OCS bisrü, Blg. biser “pearl” (Maced. bírrox is said to mean dense?)
1734:bhrüs (1) (oqu-bhrüs, -bhrüues) ‘brow’. Cf. bhrün-. WP IT, 206 Skt. bhrüs, bhruva; Av. brvat, du.; Per. abrü; Kurd. biro; Oss. árfíg; Tokh. pårwan, párwane, du.; Maced. abroütes (err. for *abroüwes?) (AM); Alb. (?) bri, def. brija (edge, side"; G Braue, id.: MIr. brú, d: Gk. ophrüs be- side ophrúë (also = ‘dike, vallum’: ON brú ‘bridge’ (?); MIr. brú (2) ‘bank, border’); MIr. brói, dual: dabrúad; Ir. cpd. fo-bhar, fa-bhar, fa-bhra (phon. obscure); Br. abrant; OE brū,
1918:176. See bhullios, io Gk. phülon, phülé beside phülios, adj.; ON -bjll, Mod. býli “home, farm, household’; Norw. bule “den, dive’; OCS byli ‘nobleman; plant; R byli "event fact; OCS cf. also by- lije (‘plant and com. SL); cf. Maced. Bu- liones, Illyr. Tri-bulium (cf. Gk. trí-phulos, adj.) and Latv. -bulis (in viz-bulis “herb paris, anemone’)
2007:bhutios, om “container, cask’ Gk. (fr. Maced.? Thrac.? Phryg.?) cf. bütinë, beside Mod. Gk. bution ‘cask’; LWs in Alb. buti, gs butini, id. beside but, id. (perh. via LL buttis, id.); Per. (?) büte ‘crucible’; ON cf. boðn “vessel, pot Li. bücias, bücius *fish- trap, lobsterpot'. (A *wanderword' in Rom- ance and Gmc.)
2395:dontio, iio (dnt-) ‘put out teeth; teethe; provide w. teeth; grin'. See dont-, dnt-, ednt- Lat. dentio, ire; MHG zannen; G záünnen ‘grimace’ beside záhnen, tr. “provide w. teeth’; Li. dantiju, yti, id.
3216:dhübhàa ‘stump’. WP I, 848 Gk. tüphé ‘reedmace; cockade’; (LW in) Lat. tüfa ‘cockade’; Upper G Tuppe ‘trunk, bole’; Frankish Doppe ‘peg used in gem-cutting'"; OCS dyba ‘trunk, bole’; R cf. dybom “on eng’. Extn. in MHG tübel ‘peg, pestle’; (E dibble is of uncertain origin). (LG, G Dóbel ‘dowel’ is fr. OFr. doille, Fr. douelle). Cf. Icel dufl ((1) "buov (Ð)
3528:el- (theme 2) ‘tree, forest". Cf. WP I, 152 Skt. cf. aranyam (forest; Arm. cf. eyevin, gs. -vno ‘pine’; (for an alleged Macedonian ílax, see WH and EM: ilex w. speculations. and cf. Fr houx ‘holly’ if fr. *ílicem. Alb. ilge, ilnje, f. holm-oak' are LWs fr. ilicem & lignea respectively); MIr. cf. allaid ‘wild; deer" beside elit ‘hind’; G dial. Ilme ‘elm’. (For OCS jelí “white poplar' & jela ‘fir see edhla). Br. cf. elw ‘aspen’
3788:omros (omoros, ombros, mros) 'sour, bitter'. Cf. WP I, 179 & II, 235 Skt. amlah ‘sour; vinegar; wood-sorrel'; Gk. cf. am- in am-oómon (“Indian spice’, for *om- osmo- 'sharp-smelling"); Maced. (?) cf. abro- ‘astringent’; abarü ‘marjoram’; Lat. cf. amärus (-à- unexplained); Olr. amar ‘grief; W afar, id.; OHG ampfaro ‘sour; wood-sorre; OE ampre ‘sorrel’; Du. dial. amper ‘sharp, sour”; Sw. amper, id.; Li. amaras ‘barberry’. Cf. õm-
```


## [2026-10-17T00:03:31.261Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"r[hó]?[oó]palon|rópal|rhopal|uropal|wrop|ropalo\" IEC.txt | cut -c1-900 | head"
}
```


### [2026-10-17T00:03:31.672Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:03:34.276Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^u?rop|^urep|^uerp|^urp\" IEC.txt | cut -c1-900 | head; grep -n -i \"club\" IEC.txt | grep -i -E \"Per\\.|pal\" | cut -c1-500 | head"
}
```


## [2026-10-17T00:03:35.689Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"k[üu]p[aä]l|gopal|g[üu]p[aä]l|kopal\" IEC.txt | cut -c1-600 | head"
}
```


### [2026-10-17T00:03:36.039Z] TOOL RESULT

```
20094:uerpo — uertos
1612:bhrater- (bhratr-, bhrate) ‘brother’. WP II, 193 Skt. bhràtr; Av. brátà, acc.sg. bràtarom, braürom; Ober, bràtar, Per. biràdar; Tokh. A pracar, pl. pracre; B procer; Oss. árvad; Arm. eybajr, pl. eybarK; Phryg. brater-; Gk. phráter, adj. “of same tribe’; Ven. vhraterei, ds.; Hes. phréter; Lat. frāter; Osc. Umb. fra- ter, Osc. gp fratrüm; Mir & Ir. bráthair, pl. bráithre; W brawd, pl. brodyr, cf. also brodor (*club-member': Gk. phrátor, id.); Br. broer, pl. broedoer; Cor. broder, pl. breder; 
3974:geul- (3) “lump, knob, ball’. (Variant: goul-) Skt. golah, golà ‘ball’; Per. zaure ‘backbone’; zawale “lump of leaven’; MHG kiule “stick, club’; Srb. Zülj ‘tumour, callouse'
4468:gül- “head, knob’. See gulos, ios Per. (ambig.) gül ‘blockhead’; güle ‘cannon- ball'; G Kaule “little ball’, cf. Keule ‘club’, Kaul-quappe ‘tadpole’; MHG küle (2) ‘ball, bowl, head’; LG kül ‘club’, kūl-pogg 'tad- pole’; ON kúla ‘knob’; kýli ‘tumour’; R (?) gili ‘redstart; Cz. hýl ‘bullfinch’ beside pa- bel ‘stump’. (For Per. gül cf. also gurd-)
5065:ghulgh- “lump, clump’. (?ghlugh-) Per. gurz “club, mace’; Arm. guydz, guydzn ‘clod’. (Isophonic is Oss. gurdz embryo?)
8374:kumbos, à ‘hump, dome, hollow, basin, bel- lied pot'. (Variant: kumbhos) Ski. kumbah, -am, m. n. ‘knuckle-bone, club- head, chignon’ (variant: kumbháh “jar, pot, urn’; kumbhih, f. id.); Av. xumbo (‘pot, < *-b- or *-bh-); Per. xum “jar, alembic'; Tokh. A umpa ((pot', *-b- or *-bh-); Arm. kumb ‘hump, boss’; Gk. kúmbos ‘hollow; pot’; kúm- bë “helmet, pot, cup, boat’; Phrygian (? Thra- . ^n) kúbba ‘cup’; LW in LLat. cumbia ‘cups’; Gaul. cumba ‘hold of ship; valley’; MIr. comm (*vessel, pot', fr
10265:mak- (2), see makəros (2) Per. cf. makū (‘shuttle’; LW in Arm. makujk, makok, id.); Arm. cf. makan, i, av ‘stick, club’
18477:teuk- (teukos, à) (1) “tip, point, peak, beak’. Cf. tuk- (1) & keukos, à (1) Skt. Gokab, am. mn. ‘a root'; Per. cf. Caugan, s. “bat, club’; čukuš, s. ‘hammer’; Alb. suké, f. “hill, peak’; Ligur. (in Swiss) tschuggi, f. id.; Mir tuag, f. ‘axe’; Br. Suk, m. ‘nape, shoulder, chignon’: Blg. čuk, m. ‘hammer’; Srb. &üka, f. Cpeak, point’, fr. a variant *keuka); Latv. cf. Cukurs, m. “peak, point, gable’. (Indo-Iran. forms ambig.)
```


### [2026-10-17T00:03:36.048Z] TOOL RESULT

```
15791:(skopelos, skopalos. See Supt:S)
```


## [2026-10-17T00:03:40.502Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^u?r[oó]p|uropal|urop|rópalon|r6palon|ropalom\" IEC.txt | head; awk 'BEGIN{RS=\"\\f\"} /uerpo — uertos/{print NR}' IEC.txt; grep -n -i -E \"Per\\. (cf\\. )?(g|k)[uüū]p\" IEC.txt | cut -c1-300|head"
}
```


### [2026-10-17T00:03:41.536Z] TOOL RESULT

```
2:Stuart E. Mann AN INDO-EUROPEAN COMPARATIVE DICTIONARY
3:AN INDO-EUROPEAN COMPARATIVE
27:An Indo-European comparative dictionary /
45:“As to many words which we have in common with the Germans, it is doubtful whether the old Teutons borrowed them from the Latins, or the Latins from the Teutons, or both had them from some common original”. The object of the present work is to indicate what words in the living or the dead languages of the Indo-European family appear to have a common origin, and to give them an acceptable prototype form. Equations are sometimes tentative, but they are based on the “sound-laws” that have proved their validity by the rational process of analogy, a mode of thought also present in the work of the Latin lexi- cographer Robert Ainsworth, who began his Latin dictionary in 1720, and who died in 1736.
47:Some may be tempted to see the present work as the restoration of a lost language. What- ever its ultimate background, and wherever its ultimate homeland, the reconstruction here attempted does not indicate a starting-point but rather a point of departure, a stage that the Indo-European complex had reached before differentiation, say some 4500-5000 years ago. The resulting groups were differentiated still further some 2000 years ago. In general the features favouring linguistic near-unity are (a) the mobility of its speakers; (b) the degree of contact between them. Such mobility and contact have helped to preserve the unity of the English language throughout the world, and the Russian language from Leningrad to Vladivostok.
48:No prehistoric culture was possessed of a powerful political centre able to impose its norm over a large area, and it is therefore idle to search for a single Indo-European homeland for a culture that reflects both the animal husbandry of nomads and the agriculture of a static community, both of which are implied in the reconstructed language as presented herewith. This must therefore be regarded not as a beginning, but as an end-product, a language caught
51:My thanks are due to all previous lexicographers (“harmless drudges”) and etymologists who have unknowingly contributed to the material of this Dictionary, and who have served as a necessary corrective to a work whose only aim is to present a common denominator rather than a lost primitive speech. As an independent study, Indo-European linguistics can claim to be an exact, albeit empirical science, since it fulfils the three requisites of science, viz. collection, classification and interpretation. For such a science, absolute and final proof is probably unattainable, but if a relationship can, in terms of Euclid, be “de- monstrated" by an adequate amount of analogy, the result can be both probable and con- vincing. Historical linguistics is unique in being probably the only exact science that is linked exclusively to human behaviour. It stands or falls by the logic inherent within it, and does not depend op the dicta of any one scholar, dead or alive. In bringing this work to a close after 55 years of intense and unremitting labour, the author has tried to avoid the German fault of overloading etymologies with irrelevancies, the French fault of trim- ming the evidence to achieve a neat pattern, and the Anglo-Saxon fault of being content with approximations.
95:MANN, S. E.: Armenian and Indo-European. Luzac, London 1963
175:Hitt. Hittite (H-Hitt. Hieroglyphic Hittite) Hom. Homeric Hung. Hungarian Icel. (Modern) Icelandic IE Indo-European impf. imperfect indef. indefinite inf. infinitive
467:al^sios (aliksos, al?snos, alksnios) ‘alder’. WP 1, 151 Mac. álixa ‘white poplar’; Lat. alnus; OHG alansa, alunsa, elirs; G Else with variants (see Kluge 17: Erle, Eller); Gmc. LW in Sp. aliso; ON alri, elti, elrir, ọlr; Sw. al; Du. els; OE alor, ellen; Russ. olíxa; Cz. ol$e; Slovak jelša; Srb. jelša and joha; Pol. olcha, olsza; Slovene jelša, olša; Li. alksnis, gs. io; Latv. alksnis, gs. alkšna. Cf. Basque altz “alder”. (The great variety of forms points to a non-IE origin, and the rhyme of Basque altz < *alks-: artz ‘bear’ < *arks- lends colour to this view. The laryngal posited for the prototype is re- flected in the forms o?st- (“bone”, cf. -k- in Li. kab-akštis ‘skeleton’, cf. Gk. ostéon; r?s- “bear”, cf. Gk. árktos; au?som: Lat. aurum: Li. auksas, cf. Basque urhe ‘gold’, in which glottalism is indicated in Lithuanian and Latvian by -k-. The a-vocalism is, for H. Krahe, an indication of *pre-European' origin in names of major lakes and rivers in Europe and W. Asia)
839
```


## [2026-10-17T00:03:43.614Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=826 && NR<=840' IEC.txt | grep -n -i -E \"club|mace|Per\\.\" | cut -c1-500 | head -20"
}
```


### [2026-10-17T00:03:44.117Z] TOOL RESULT

```
19:ueibo, ið (uib-) “twist, turn’. Cf. uoib- Lat. cf. vibicés, pl. ^weals'; ? cf. vibones, pl. *patience-flower, britannicus'; Gk. cf. am- eíbo, v. (change, if from *sm-ueibo) beside o-gde am-oibé, f. id.; Go. weipan, sv. 1. ‘wreathe’; MHG wifen, sv. 1. (twist; sway’; OE wipian, wv. (^wipe, clean? here?); Latv. viebju, viebt, v. ‘twist, wriggle; pull faces’. Nominal types: OHG in Latin laws wifa, f. *boundary-mark'; LG wipe, f. ‘bunch of straw, wisp’; MHG wife, sf. as OHG; Latv. viebas, fpl. ‘gr
70:ueies ‘we’ Skt. cf. vayám, id.; OPer. vayam, id.; Av. cf. vaem, id.; LG wi, Sw. vi, id.; MHG wir, wér & wier, id.; ON vær, id.; Go. weis, id.
97:ueks- ‘grow, thrive’. (ueks-?). Cf. aue-, eks-, uåks- and aueks-. Apparently a cpd. of pre- fixes. Cf. WP I, 23 and see next OPer. vaxi-, v. ‘grow’; Gk. aéxo, v. ‘make grow’; Li. vešiù, éti, v. “luxuriate, thrive’
99:ueKsueros, uesKueros, à ‘evening, west’. WP I, 311 Per. xavar, s. ‘west’; Tokh. kastwer, B kástwer, s. ‘night’; Arm. gäer, o, ov & i, av, s. id; Gk. hésperos, m. “evening star’; hespéra, f. ‘evening, west’; Gk. dial. wespáros, Locr. wes- parion, adj. & n. ‘evening’; Lat. vesper, gs: vesperis, m. “evening, west’; vesper, a, um, adj. id. beside vespera, f. ‘evening’; Olr. fescer, fescor, Ir. feascar, m. id.; W ucher, pl. -au, m. id.; Cor. cf. gorth-ewer, m. id. (fr. *urt-^); OCS and còm. Sl. ve
118:uel- (6) “big, great; greater, stronger; be big, be strong, be able; greatly; strongly; very’. WP I, 285 & 294. Cf. ual- (2) (r-gde) Skt. cf. variyas, mfn. ‘broader’; Per. cf. bis ‘more’; Osc. cf. valaemo-, superl. "best": OBr. guell, Cor. W. gwell, adj.
119: ‘better’; OE cf. we- lig, adj. ‘rich, prosperous, abundant, fertile, luxurious’; Du. welig, id.; LG welig “bright, gay, luxuriant’; Go. cf. ga-wiljis, adj. “willing, agreeable’; Scots walie, adj. ‘ample, large; jol- ly’; ON cf. vilgi, adv. “very, at al’; OCS velij, adj. ‘big’; OCz. velí, Srb. velji, id.; Li. vély, adv. ‘rather’. Compounding forms in Per. bali- *up- beside bali (“indeed, certainly, yes’: Li. vély “rather?); Ir. feile- ‘very’; Go. waila-, px. *well2; OE, Du. wel, wel- ‘very, 
196:uequó (uequmi, uiuéqumi) “call, say, speak, ask’. Cf. uoóqu-. WP I, 245 Skt. vátmi, vakmi, vívakmi, 2, 3s: vaksi, vakti, *say, speak, tell, name, call, announce, des- cribe, reproach’; pp: uktáh, inf: váktum; Av. vað-, v. ‘talk’; Per. güvam, inf: guftan, v. ‘say’; Tokh. B wek-, v. ‘say, speak’; Arm. (?) goéem, v. Cer, if to Skt. vivaksami ‘wish to say"); Gk. eípo, v. ‘say’; Olr. cf. in-fét, 3s. ‘tells’; pf: in-féccid (sic) “he told’; OCz. vece Che said”: inf: vecéti); OPr. wack-, v. ‘cal? (d
209:uer- (1) (uero, io, uro, ið) open, close’. WP I, 280 Skt. várami, v. pp: vrtab, id.; Av. var-, v. ‘cover; Lat. cf. ambig. ap-erio, erte, v. ‘open’; cop- erio, -erire, v. ‘close, cover, hide’; Li. veriü, vérti, v. tr. (9) open or shut — a door or window’; Latv. veru, vērt, tr. ‘open’; (z-gde in) OCS (and com. SL) vro, vréti, v. ‘close’; cf. Cz. ote-vfit, inf. "open": za-vřít, inf. ‘close’. Nominal types: Osc. vereias, adj. f. ʻofa door’; R verejà, f. 'doorpost; Cz. vefeje, f. id.; cf. roz-ver
213:uer- (4) (?) *up, upon' Per. bar, adv. & prp. id.; Arm. ger, cpds: gera-, id.; Lat. (?) cf. the hapax: verones plum- bei ‘sheets of lead”
239:‘work’; (denom. in) OHG wérkon, w&rchon, v. "work do’; Swiss werchen, id.; Du. werken, id.; OE weorcan, id. beside (z-gde) wyrcan, id.; ON verka, v. ‘work’; Alb. virdhem, v. ‘gain a skill, win sympathy’, mp. fr. *uergemoi or sim.. Nomi- nal types: Pahl. varz, s. “practice, work? (Per. id. fr. Pahl.); cf. also Per. barz-gar, s. 'farm-labou- rer’; Arm. (e- or o-gde), o-st. "work act, fact’; Myc. we(r)k-, cpds. *draught-, work": cf. were- kara- (“tooP or sim.); Gk. érgon, n. "work op- eration, 
270:uéros, ios (2) “true, right, proper. WP I, 268 Lat. verus, id.; MIr. fir, Ir. fior, id.; Br. W gwir, Cor. gwyr, id.; OBr. guir, id.; OHG war, wāri, id. beside wara, f. (truth, loyalty’: Sl. véra); MHG were, adj. ‘true, loyal’; OCS (and com. Sl.) věra, f. (faith: OHG wara)
274:uers- (1) ‘droplet, sprinkling, shower, dew, rain’. WP I, 269. Cf. uersó (1) Skt. varsáh, -Á, Am. mfn. “rain, shower’; Av. cf. varo&-, v. ‘sprinkle’; Per. baris “rain”; Hitt. warsas (queried), id.; Gk. hérse, hérsé, f. (1) ‘dew’; Olr. cf. feraim, v. ‘pour, rain? beside Mir, fear-thuinn, Ir. fearthain, vbl. n. f. ‘raining’ (vocalism obscure in Olr. fross, f. “shower, downpour’, fr. *urost-?); Li. cf. versmas, m. ‘eruption’; versme, f. ‘spring, source’
278:uersi- (?). Cf. WP I, 267 Skt. cf. vargi-sthah ‘highest’; Per. bi$, adj. “much, more’; Olr. ferr, Ir. fearr, adj. “better”. (ISophonic: Go. waírsiza, OHG wirsiro, ON verri ‘worse’; G wirs, wirsch “bad, raging’; Du. cf. wars 'averse") (!)
293:uertenos, ā, is ‘turn, roll, roller, axle-tree, cart’. Cf. uerto. WP I, 274 Skt. vartaníh, f. ‘felloe of wheel’; Oss. wär- don, pl. wärdättä, s. Ceart LW in Romani vardon, id.); Per. vardāne, s. ‘rolling-pin’; (z- gde in) Gk. rhatánē, f. (/stirring-stick'. fr. *ur- tona); Lat. cf. Vertumnus, m. ‘god of change: LLat. vertumnum, n. *ironwort, heliotrope'; OCS (and com. Sl.) vréteno, n. ‘spindle’; LW in Finn. värttinä, id.
317:ues- (1) ‘put, place, give, offer, sell’. Cf. uosn-, uesnom. WP I, 311 Skt. (vowel ambig.) vasnám, n. ‘price, value’; Tokh. AB wäs-, B was-, v. ‘give’; Hitt. was-, 2s: wasti, v. 'buy' beside usniyami, id.; Per. cf. far-üSam, fir-ü$am, inf: -üxtan, v. ‘sell’; Lat. cf. venum dare, v. "sell" beside vendére, id.; Umb. cf. ues- ‘liberate’
318:ues- (2) ‘be, dwell’. WP I, 306 Skt. vásāmi, v. ‘dwelľ; Av. váhai(mi), v. ‘stay, dwell’; Per. bāšīdan, inf. ‘dwell, be’; Tokh. B wäs-, wsask-, v. “lie, rest, be'; Oss. win, wn, Dig. un, inf. ‘be’; Arm. cf. gom, v. "Tam": geri, s. & adj. ‘slave; enslaved’; Hitt. (?) hwes- (mi), v. dive; Gk. cf. á-esa núkta, v. “have spent the night'; Lat. cf. verna, mf. “house- slave’; Sabine verna, mf. ‘native, aboriginal’; Olr. cf. fiu, 3s: femmir, defect. ‘have spent the night; MHG weésen, sv. 5. ‘be, rema
```


## [2026-10-17T00:03:47.729Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"cudgel|‘club’|'club'|“club”|club'\" IEC.txt | cut -c1-400 | head -20"
}
```


### [2026-10-17T00:03:48.202Z] TOOL RESULT

```
1230:bhér- (2) ‘strike, striker’. Cf. bherio Arm. bir (a-st. 'cudgel); Alb. borë ‘snow’; Icel. bára ‘breaker, wave’
1250:bherà ‘striker’. See bherió above Arm. bir, a-st. ‘cudgel; Alb. borë ‘snow’; Icel. bára ‘breaker’
1558:bhoust- “lump, clump, bump, bulge’. WP II, 117 Lat. füstis ‘cudgel’; Olr. búas, Ir. buas ‘paunch, pouch’; W bus "Ip": QGallo-Lat. in) It. busto “bust”; ON beysti “ham. Variant in Cz. buchta ( bun, fr. *bhouksta?)
1825:bhrt- (bhrt-) (1) ‘strike, blow; striker; fate’. Cf. bherio & bhrio (1) Oss. bårdin ‘cudgel; Arm. bah ‘spade’; Per. bil, id.; Lat. fors; Ir. bráth ‘judgment; W brawd, id.; Br. breed ‘ple; MHG burt ‘pledge, duty’; OE byrd ‘fate’; Du. beurt ‘turn, lot; OFrankish, cf. staim-bort (a weapon: *stone-throwing catapult’)
1880:bhugo, ið (2) ‘beat Gk. cf. s-phuzo ‘pulsate’, s-phugmós ‘pulse’; MHG bochen ‘knock’ beside buch ‘cudgel’; (Alemannic) G pochen: Dan. poge ‘knock’
2377:dombos “lump, block W dom ‘dung’; Norw. tamp ‘knotted rope’; Sw. tamp (‘knotted rope; lout'; cf. Norw. tampa ‘hoyden’); OCS dobü ‘tree, timber”. In com.. SL “oak'; cf. OCS dobrü, dobrava ‘forest’; R cf. dubina ‘club’. (A variant arises in ON teppa, Sw. täppa, Norw. teppe, v. ‘to bung’, whence Fr. LWs tampon and tapon)
4155:glubh- ‘cut open, split’. Cf. gleubh-. WP I, 661 Hitt. cf. kullupi ‘digger’; Gk. glüpho, glüpto ‘gouge, carve’; gluphis ‘notch, of arrow’; MHG klobe ‘slit, chink; peg, wedge’; OFris. klova ‘cleft, division’; OE dote ‘buckle’; ON klofi, klof ‘cleft, groove; fork of legs’; G Kloben ‘chip, log, socket, clamp’; MHG kloben, v. ‘split; ON klyfja, id. beside klofna, id. Long-gde in MHG klüben ‘chip 
4180:glb- (glbh-) Lat. galba *meat-maggot'; galbulus 'cypress- cone’; (either) Du. kollop ‘puck in icehockey, chock, polo-bal; EME collop “lump of lard for frying; LG külp ‘bulging eye’; kulp-ig ‘fat, blunt’; külpen, pl. “hard unripe fruit’ (fr. *glb-), (or) OHG kolbo ‘cudgel’; Du. kolf “butt of gun’; Sw. kolb “club, pommel’; ON kólfr *bell-clapper'; kylfi, id. & kylfa ‘cudger. (Isophonic is Ir. g
4205:scraping noise’, fr. *gnitio); Ir. gníoth ‘noise’. (For Lat. nitor ‘strive’, see kneit- in view of Li. knieciu “strive”, despite Fest. gnixus: nixus) gnod- ‘knot, lump’. Cf. gnót- Lat. nodus (knot. WP & EM untenable); Du. knoet ‘scourge’; Sw. knota *knuckle- bone’; ON cf. (GA) knatt-, knottr ‘ball’: LG knautschen, v. (for *knotschen "ball up"); (*-ó- in) knasch, knass, adj. ‘tight. (R knut 'k
4465:gughelos, à “lump, ball’. Cf. gugh-, gughaà MHG kugele ‘ball’; G Kugel ‘bullet; OE cycgel ‘cudgel’; Du. kogel ‘bullet’; Li. güZulas (bundle, sheaf ambig., cf. güigos)
4468:gül- “head, knob’. See gulos, ios Per. (ambig.) gül ‘blockhead’; güle ‘cannon- ball'; G Kaule “little ball’, cf. Keule ‘club’, Kaul-quappe ‘tadpole’; MHG küle (2) ‘ball, bowl, head’; LG kül ‘club’, kūl-pogg 'tad- pole’; ON kúla ‘knob’; kýli ‘tumour’; R (?) gili ‘redstart; Cz. hýl ‘bullfinch’ beside pa- bel ‘stump’. (For Per. gül cf. also gurd-)
7147:kolok-, kolk- (klk- w. u-basis) (1) “ankle, heel, hock, knee'. (Variants: klk-, kolquos, kuluk-, kalks-, kalk-). WP II, 599 Lat. calx, gs calcis, m.f. (2) “heel, tip’; OE healh, pl. hal(h)as “corner, nook, dingle'; OCS klüka ‘bend of knee’; Blg. Kaka ‘hip’; Cz. klk “fold of intestine’; Li. cf. kulkšis, kul- šis, f. ‘haunch, hip, ankle, heel"; cf. pa-kulšē ‘thigh’; Latv. cf. cilksnis “hand of
7148:kələk-, kəlk- (kəlkəl-, klk- w. u-basis) (2) ‘stone, pebble’. Variants as for (1) Skt. karakā “hail” beside karkarah, -am ‘stone, limestone"; Lat. calx limestone’ beside calcu- lus ‘pebble’; Ir. calc ‘conglomerate’; Br. kalch (testicle'. Br. & Ir. fr. *kolks-); Big. kláka (2) ‘club’; Cz. klk (2) “lump, clot
7540:kokos, à “club, stick’ Ir. cág, f. “handle of implement’; Li. küokas ‘cudgel’, küoka, id.
7713:kortos, is (2) “pike, pole, spear Cret. (?) kórton (an object in an inventory); Li. kártis, ies, f. ‘pole’; Latv. kārts, id.; Finn. LW karttu “stick, cudgel’
8040:krunk- (2) “bend, fold” Skt. krüficami Chend Pp: kruktáh “bent, crooked'; Go. hrugga ‘stick’; OE hrung ‘crossbar, pole, rung; MHG runge “staff, shaft; G Runge ('side-stay of cart’. LW in Li. rungas ‘side-stay, rib, rung’ and in Latv. runga, f. ‘stick, cudgel’). (LW fr. Eng. in Ir. ronga ‘rung, spar); Latv. kroka (2) and krunka (fr. Li.) ‘crease, pleat, wrinkle’
8293:(küios, à ‘beater, club, mallet, stick’. Only in Slav. & Balt. Long-gde form of kau-, kau-, q. v.) OCS kyj ‘hammer’; Cz. kyj ‘cudgel’; Pol. kij ‘stick’; Li. kūjis, m. “hammer” beside kūjos, fpl. ‘stilts’; Late küja ‘crutch, stick?
9055:Skt. cf. Sáras, n. “head of milk, cream; Hes. cf. korütei, ds. ‘to the head’; Gk. cf. also kor- in cpds kór-udos ‘tufted lark’; kórumbos, m. *corymb'; korü-ne ‘club, round bud’; kor-dúlë ‘cudgel, hump, headdress’, etc.; Myc. koruto, gs. of koru- ‘helmet’
9447:lakstis, à (lakt-) ‘stick, stem, branch, bar. Cf. variant slaKtis Prakritic, Pali latthi ‘stick’ (cf. Skt. lakutah *cudgel); Arm. laxt, Let ‘stick; cudgel’; Gk. laktis, gs -os, f. ‘pestle’; Alb. las&, Ilasë ^wash- ing-stick'; Sw. läckt, pl. -er, m. ‘stick, slat, lath’; Blg. lost, m. Char, bolt. LW in Mod. Gk. lostós, id.); Li. lakstà, laktà ‘perch’; Latvian laksts, m. ‘shoot, sucker’ beside l
10198:lurgos (lrg-?) ‘stick, stafP. WP II, 443 Olr. lorg, f. (1) ‘shaft, log, club’; (2) ‘leg, shank’; ON lurkr, m. ‘cudgel’; Norw. lurk, id.; OE (misspelt lorg & lorh for *lorc ‘pole, beam’); EME lurch (a measure of 187); LW in Corn. torch “stick, staff"
```


## [2026-10-17T00:03:51.377Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 811 812 813 814 815 816; do echo \"== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | grep -o -E \"^[^ ]+ [^‘]{0,40}‘[^’]{0,40}’\" | head -40 | tr '\\n' '|'; echo; done"
}
```


### [2026-10-17T00:03:52.236Z] TOOL RESULT

```
== leaf 811
a sentence-particle ‘and, so’|equivalence of Li. tvinkseti: tunkseti ‘pulsate’|uderos, om ‘belly, stomach’|udn (üd-ono) ‘out, outside’|udór (udor, obl: udn-) ‘water’|
== leaf 812
de vysòkij, adj. ‘high’|üd-ter- (ŭter-) ‘extreme, outer, upper, fur- ther’|üg- (1) ‘grow’|not *toroc'; tosca & toxa ‘toad’|(ugueio ‘moisten; get damp’|ūĝā, io, (-on) ‘slimy creature’|üio ‘howl’|-ukos, dim. extn. Cf. Skt. laghukah ‘trivial, light’|ükos, à ‘hoot, shrill cry; hooting bird’|Oss. ug, s. ‘owl’|uksó(n), uksen- *ox'. WP I, 249 Skt. uksán, m. ‘bull’|
== leaf 813
-ulos, à, dim. suffix in Skt. vid-urah ‘wise’|ululo, aio ‘howl’|ungó(n) ‘reptile’|unguros, ios ‘reptile’|-üniə, fem. suffix in ON ás-ynja ‘goddess’|untis, os, io (?) trage, temper OHG undea, f. ‘billow’|
== leaf 814
adv. ‘upper; above’|üpið ‘hoot, howl’|ür- ‘moist, wet; moisture, wetness’|
== leaf 815
ch'; Osc. uruvü, f. ‘boundary’|us- (1), radical: ‘burn’|-us, (3) absolute part. exnt. in Vedic vidüs ‘attentive’|usdh- (usdhios) ‘spike, spur Gk. hussós, m. ‘javelin’|üst- (2) ‘spike, spear, awn’|
== leaf 816
uadhis ‘pledge, surety’|uadhmn-, uadhor ‘thrust’|uàdhð ‘go, wade’|uāgh- (2) ‘bitter’|uagh- (uåghos) (3) ‘surge, billow, swell’|
```


## [2026-10-17T00:03:55.198Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==814 || NR==815' IEC.txt | grep -i -E \"^ur|club|mace|staff|rh\" | cut -c1-600"
}
```


### [2026-10-17T00:03:55.787Z] TOOL RESULT

```
ursis (ursis) *wickerwork, basket, withy’ Per. više (1) ‘ivy, woodbine’; Arm. uf, o-st. ‘vine-shoot’; uri, gs: -vo, ab. s. -eav, s. ‘willow’; Gk. hurrís, gs: -ídos, f. ‘basket’; Cz. vrš, f. *fish-basket, creel’; Pol. wiersza, f. id.; R vér3a, f. id. (Isophonic: Alb. urrë, f. 'sapwood")
uruos (uruos) ‘ditch, boundary-ridge'. Cf. uruos as separate entry. WP II, 352. (Skt. un- certain and ambig.) Skt. ülvam, n. (^womb'. Ambig.); Av. cf. urva (ambig. name of a territory); Hitt. cf. (?) irha- ('boundary'. Vocalism?); Myc. wo(r)wo- (que- ried: *boundary-ditch, boundary); Gk. ourós, m. ‘holloway, slipway'; oüros, m. ‘boundary’; Lat. urvus, gs: -i, m. *boundary-dit
ute, utə, uti, ut (fr. autos) sentence-particle Vedic utá “and, or'; u-ta-u "and also); Av. uta, id.; uiti ‘thus’; OPer. uta ‘and’; Hom. Gk. ē-úte “as; than’; Lat. ut, uti, conjunctive pt., cf. uti-nam “would that . . ^; uti-que ‘so, in- deed": ut-pote ‘since, as’, ali-uta “otherwise; Umb. ute "but: OE op “up to, till; op-, px. “away”; cf. op-pe ‘and, or: op pe ‘till’; MHG od, ode "or: Latv. cf. ka-ut “if, though’. Cpd. in Alb. ndo-fta ‘perhaps’; Go. ibai ufto, cj. “if perchance’ beside aüfto “perhaps”; OE ofpe ‘or: L
```


## [2026-10-17T00:03:59.785Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^u?r[oóō]p|^urep|^urp\" IEC.txt | cut -c1-700"
}
```


### [2026-10-17T00:04:00.152Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:04:02.232Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \".{0,200}(rh[oó]p|rópal|ropal|ropt|rhópt).{0,300}\" IEC.txt | head"
}
```


### [2026-10-17T00:04:05.365Z] TOOL RESULT

```
ugrep: error: error at position 122
f][\x80-\xbf]*){0,300}
                      \___exceeds complexity limits
```


## [2026-10-17T00:04:07.357Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"rh[oó]p|r[oó]pal|r[oó]ptron\" IEC.txt | cut -c1-800 | head"
}
```


### [2026-10-17T00:04:07.661Z] TOOL RESULT

```
15314:sarbac (zero-u-basis), id.; OCS cf. srübanije, n. ‘supping’; other variants represented in R serbat (zero-i-basis); Cz. stfebat (metathesis); Li. surbiü, surbti (u-basis); srebiü, -ti (meta- thesis); Latv. surbju, surbt beside strebinàju, at, id., and a descriptive *slrb- (1) in G schlür- fen, Du. slorpen, and Eng. slurp and (dial.) slorp; (o-gde in) Gk. rhophéo, id. WP II, 704
17093:srübh- (one of several variants in sense of ‘sup, slurp’. Cf. srebh-, srubh-, srb-, sorb-, surb-, etc.). (Onomat.) Gk. rhopháo, rhophéo, v. id.; Li. sruobiù & sriuobiü, ^ti, id.; cf. sr(ijuobalas, m. ‘soup’
19013:tropolos, is (tropil-) ‘turn, twist’. Cf. tropeio and next Br. tróel, pl. -u, f. ‘bindweed’; W troell, pl. -au, f. ‘whirl; pulley’ beside trol, pl. iau, f. ‘cylinder, roll’; (for Gk. tropalízo, v. ‘turn’, see troqueió below)
```


## [2026-10-17T00:04:12.534Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=813 && NR<=814' IEC.txt | grep -n -i -E \"Per\\.|ropal|pal\" | cut -c1-500"
}
```


### [2026-10-17T00:04:12.907Z] TOOL RESULT

```
21:uper, uperi (upor, upor) “over, above’. WP I, 192. Cf. upo and extns. Skt. upári, adv. prp. “above; upwards; up’; cf. üparab, adj. “lower, later’; Av. upairi, prp. “on to; upon’; uparo, adj. ‘upper’; Ober upariy, prp. as Av.; Per. bar, prp. ‘on’; Arm. ver, i ver, adv. “above? (beside the ambiguous var, adv. ‘down’, see aper-); Myc. upar, Gk. hupér, Hom. hupeir, prp. ‘over, above’; OIr. for, for-, prp. & px. ‘on, upon’; cf. for-od, s. (‘dais, platform’, fr. *upor-pod-. Whitley-Stokes); Gaul. c
38:*-stor- (Skt. $1.); *-sthàn-, -sthon- (Skt. Ir. W); *-sthat-, -sthot- (Skt. Ober Gk. OIr. W. OE. SI.); *-sthos (Skt. Av. Per. Ir. Br. W “servant; OE ‘haste, zeal’; OS ‘fast’; Gk. ‘crypt, tomb’, etc.)
41:ursis (ursis) *wickerwork, basket, withy’ Per. više (1) ‘ivy, woodbine’; Arm. uf, o-st. ‘vine-shoot’; uri, gs: -vo, ab. s. -eav, s. ‘willow’; Gk. hurrís, gs: -ídos, f. ‘basket’; Cz. vrš, f. *fish-basket, creel’; Pol. wiersza, f. id.; R vér3a, f. id. (Isophonic: Alb. urrë, f. 'sapwood")
```


## [2026-10-17T00:04:18.380Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 258 2273 1625 1527; do echo \"=== BQT:$p\"; timeout 300 python3 tools/ref_page.py BQT:$p --image 2>&1 | tail -60 | grep -E \"png|PNG|vision|برغ|ورغ|کرم|قرمز|^\\[\" | head -20; done",
 "timeout": 600000
}
```


### [2026-10-17T00:04:42.912Z] TOOL RESULT

```
=== BQT:258
=== BQT:2273
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2273.png
۳ ورغ
است» « تحفةٌ حکیم موْمن » رل4: سطاخیص . ۸ - برغ (هم.)؛ ساسکریت ۷۵788
دل برد ومرا لیز بمردم نشمرد گفتار چه سودست که ورغ آب ببره -
=== BQT:1625
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1625.png
-۱۹۲۰- کرمائیل
وال بتحتانی رسیده, کرمان شهان * - با شین نقطه‌دار
: کلنك راد کرما ثیل * بروزن عزرائیل . نامبکی
در رو زکار «یچ تشان دیدی ا زکرم جز در میان سبزه اطراف بوستان .
غشاه مخاطی که حدقهٌ چشم را بیلکها متصل‌سازد . ۸ > کرمانشاهان, ناحیتی‌است‌درمغرب
ازینقرار بود : ۱-کرمانشاه وحومه ۲- سنقر وکلیائی ۳- میان دربند و بالا دربند و زیر دربند
وقصر *۱- هرسین « کیهان . جفرافیای سیاسمی س ۵۲-۶40۱ رد : کرمانشاه ۰ (س۱۹۲۹ح).
7 کرم - بکراول, پهلوی 1۳37771 . سانسکریت 87181 (کرم )» کردی(17۷17»
استی 1۳2[12 (مار) . ۴3180118 ( کرمها ‎ )‏ بلوچی ع 20 اسشق - هوبشمان *۸۵ ۰
کیلکی ۴81 : کرمها جانورانی هستند غیر زی‌فقا رکه عموماً بدن دراز و ترم دارند و بدون پا
هستند , و آنها رایهدسته :کرمهای خلقوی ۰ کرمهای پپن و کرمهای کرد تیم میکنند .
کرمان - بکراول . نخت بناحیتی اطلاق معشود که از شمالز محدود است بخراسان
=== BQT:1527
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1527.png
قرمز ۱ بکر اول و میم واسکون | و هم زمانه - و اطرف روی و طرف سر و موی
رنگه‌کنند (۱) وگوبند قرمز جانوری است میباشد - و مناره - و طرف بالایین آفتاب وقتی
فرانوی شده 9غ(678گظ . ۴ - قرمز املا بکرمی‌ریزء دارای قطعاتی خارداراطلاق میشود.
قرمز ملون ( 02010102 ۲۵۲۱69 ) است «لاروس بزرکه» و رك : الجباهر ص ۳۷ .
```


## [2026-10-17T00:04:46.090Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:2273 2>&1 | grep -n -E \"ورغ|برغ|ساسکریت|سانسکریت\" ; timeout 300 python3 tools/ref_page.py BQT:1527 2>&1 | grep -n -E \"قرمز|کرم|معرب|سانسکریت|ساسکریت\" ; timeout 300 python3 tools/ref_page.py BQT:258 2>&1 | head -30",
 "timeout": 600000
}
```


### [2026-10-17T00:04:46.624Z] TOOL RESULT

```
4:۳ ورغ
46:است» « تحفةٌ حکیم موْمن » رل4: سطاخیص . ۸ - برغ (هم.)؛ ساسکریت ۷۵788
49:دل برد ومرا لیز بمردم نشمرد گفتار چه سودست که ورغ آب ببره -
7:قرمز ۱ بکر اول و میم واسکون | و هم زمانه - و اطرف روی و طرف سر و موی
9:رنگه‌کنند (۱) وگوبند قرمز جانوری است میباشد - و مناره - و طرف بالایین آفتاب وقتی
21:فرانوی شده 9غ(678گظ . ۴ - قرمز املا بکرمی‌ریزء دارای قطعاتی خارداراطلاق میشود.
23:قرمز ملون ( 02010102 ۲۵۲۱69 ) است «لاروس بزرکه» و رك : الجباهر ص ۳۷ .
no scan of BQT covers printed page 258 (see 'scans' in refs_online.json)
```


## [2026-10-17T00:04:48.432Z] TOOL CALL #60: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2273.png"
}
```


### [2026-10-17T00:04:48.963Z] TOOL RESULT

```

```


## [2026-10-17T00:04:48.958Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:04:50.087Z] AGENT

Saving the vision transcription.


## [2026-10-17T00:04:53.811Z] TOOL CALL #61: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2273.vision.txt <<'EOF'\n[BQT p. 2273, read from page image; entry ورغ and footnote 8]\nورغ - بفتح اول و سکون ثانی و غین نقطه دار ، بندی را گویند که از چوب و علف وخاک وگل درپیش رودخانه‌ها بندند ۸ - وفروغ ...\nFootnote 8: برغ (ﻫ.م.)؛ سانسکریت várga (برگرداننده)، نیز ازریشهٔ várjati, varj (بقول نلدکه) «اسشق ۱۰۸۰»:\nدل برد ومرا نیز بمردم نشمرد       گفتار چه سودست که ورغ آب ببرد .\nفرخی سیستانی «لغت فرس ص۲۳۳». درصحاح الفرس: گفتا که چه سوداست «طاعتی». ورك: لغت فرس ص۳۰۶ ح۶.\nEOF\necho ok"
}
```


### [2026-10-17T00:04:54.385Z] TOOL RESULT

```
ok
```


## [2026-10-17T00:04:55.587Z] TOOL CALL #62: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1527.png"
}
```


### [2026-10-17T00:04:56.165Z] TOOL RESULT

```

```


## [2026-10-17T00:04:56.140Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:05:01.986Z] TOOL CALL #63: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1527.vision.txt <<'EOF'\n[BQT p. 1527, read from page image; entry قرمز and footnotes 1-2]\nقرمز ۱ - بکسر اول و میم و سکون ثانی وزای نقطه دار، چیزی است که بدان چیزها رنگ کنند (۱) وگویند قرمز جانوری است کوچك و بر بوتهای خار می‌نشیند آنرا میگیرند و خشك میکنند وبعربی دودالصباغین خوانند ۲ - و حبی دیگر هم هست مانند عدس و آنرا نیز قرمز گویند ...\nFootnote 1: = قرمز «المعجم چاپ مدرس ص۲۲۴ س۸» ازسانسکریت «ژابا ۳۰۹» و از عربی وارد فرانسوی شده kermès .\nFootnote 2: قرمز املا بکرمی‌ریز، دارای قطعاتی خاردار اطلاق میشود، نرینهٔ آن ریزتر از مادینه و دارای پر است ... قرمز ملون (kermes baphica) است «لاروس بزرگ» و رك : الجماهر ص ۳۷ .\nEOF\ncd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['MON'],ensure_ascii=False)[:1500]); print(json.dumps(d.get('DEW'),ensure_ascii=False)[:500])\""
}
```


### [2026-10-17T00:05:02.680Z] TOOL RESULT

```
{"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmq
null
```


## [2026-10-17T00:05:03.817Z] AGENT

Now BQT for کوپال/گوپال, ARY, and web lookups.


## [2026-10-17T00:05:05.598Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"کوپال\" \"گوپال\" \"ورمیشل\" \"قرمز\" \"برغ\"; do echo \"== $w\"; grep -n \"$w\" MON_part1.txt MON_part2.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v3_pages.txt BQT_v1_pages.txt incoming/ARY/ARY_pages.txt 2>/dev/null | cut -c1-250 | head -6; done"
}
```


### [2026-10-17T00:05:06.108Z] TOOL RESULT

```
== کوپال
incoming/BQT/BQT_v4_pages.txt:21697:بدیدند کر کان بر وبال اوی میان وبلی چنگه وکوپال اوی.
incoming/BQT/BQT_v3_pages.txt:37659:کوپال ‎bo‏ بای فارسی بروزن ‎hoy‏ | بروزن حوصله هم‌آمده است ‎٩‏ .
incoming/BQT/BQT_v3_pages.txt:37677:‏ییا آورد (آردش ؟ دهخدا) زخم کوپال من ‎aly‏ کسی لیزه بر ‎Sk‏ من .
incoming/BQT/BQT_v3_pages.txt:37679:‎gle - ٩‏ کوپال و نیرو نماند زمن هیچ جز نام لیکو نماند .
incoming/BQT/BQT_v3_pages.txt:50916:را 55 گفته‌اند - و بمعنی بال و کوپال هم‌آمده
BQT_v1_pages.txt:2887:مقدم یامعاصر اوست: چهلفت فرس‌اسدی حرف آخز حرلفت‌را ملاث فرار داده‌استر مثلاء کوپال»را
== گوپال
MON_part2.txt:27644:کوپال: (قد. -۲5۳26 |گوپال] (.) گرز 
== ورمیشل
MON_part1.txt:10989:باریک ولی عریضتر از ورمیشل و سفت و 
MON_part2.txt:35427:ورمیشل . گندم مصری: ( گیا.) بلال؛ ذرت. 
MON_part2.txt:85607:ورمیشل: [۹۵] ۷۰۳ (.) نوعی رشته فرنگی 
== قرمز
incoming/ARY/ARY_pages.txt:11980:واژه‌ی آقرمز" نیز از همین واجريشه است. ضمناً واژه‌هاي انگلیسی ۲38880 و ذرانب‌ی ۲8۸3/0181 و
BQT_v1_pages.txt:3758:و لفت ها با مر کب قرمز و ریزتر و موضوع هر عنوان با مر کب مشکی
BQT_v1_pages.txt:3886:متن لفات وعنوان ها خط قرمز ؛ دارای ۱۰۰۰ صفحه نمام » هر صفحه ۲۵
BQT_v1_pages.txt:11612:ودارای ربشة قرمز دنگ وب رگهای خوراکی و کلهای نرومادء آن جداست . « کل گلاب4 ۰*۲۷
incoming/BQT/BQT_v4_pages.txt:2619:. ‏بیضی وگلهای سفید یا قرمز «کل گلاب ص ۰۲۸۸ . رك : مرزنگوش‎
incoming/BQT/BQT_v4_pages.txt:14292:ذرین‌اواخر کشف کرده‌اند که ورس؛ غدد خارجی و قرمز رنگه ۲00068708 ۳100710818
== برغ
incoming/ARY/ARY_pages.txt:10934:| سیم (به چم آبخشی از برغ)
incoming/BQT/BQT_v4_pages.txt:1976:انگوری باشد - و شمع را نیز گوبند - و نام جویآب روید وآنرا در (٩)آش‌کنند‏ و برغشت
incoming/BQT/BQT_v4_pages.txt:2001:وزن تگر3 . بمعنی‌بیگار(٩)‏ وکار فرمودن بزور | برغت راکویند و آن گیاهی است بهاری مانند
incoming/BQT/BQT_v4_pages.txt:7287:پایة سقف داررا کویند ؛ و بعشی پوشش‌سرنردبان ناف برغم ددن -آن‌است که‌ماماچه
incoming/BQT/BQT_v4_pages.txt:7317:۴ - ناف توبرغم زدند , غم‌خورخافانیا ۱ کانکه جهان‌را شناخت غمکده شد جان او.
incoming/BQT/BQT_v4_pages.txt:13236:شترواری جو- وبممنی‌مقدارهم آمده‌است همچو | بممنی برغ است وآن بندی باشد که درپیشآب
```


## [2026-10-17T00:05:08.181Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 37655,37685p incoming/BQT/BQT_v3_pages.txt; sed -n 11970,11985p incoming/ARY/ARY_pages.txt; sed -n 27642,27646p MON_part2.txt; sed -n 85605,85609p MON_part2.txt"
}
```


### [2026-10-17T00:05:08.705Z] TOOL RESULT

```
‏جوباره , کله و رمةٌ خر وکاو و کوسفند و سلیس کوبله ۸ ‎pa‏ اود و فتح بای ‎um!‏

‏حیوانات را گویند . و لام 6 موی سر و کل سرآدمی باشد ؛ ویفتجاول
کوپال ‎bo‏ بای فارسی بروزن ‎hoy‏ | بروزن حوصله هم‌آمده است ‎٩‏ .

‏عمود و گرز آهنين را گویند ۴ ‎ -‏ وگردن (۱) کوپله = بشم اول و فتح بای فارسی

‎ee‏ وکنده را یز گفته‌اند ۵ - و نام مبارزی | و لام + قبه‌ای را کویندکه در ایام شادی وآیین

‏بوده از خوبشان پادشاه روی ؛ و باین معتی با | بندی و جشن و عروسی پندند ‎VY‏ و سواران

‏کاف فارسی همآمده است ۰ آب را یز کوبند که حباب باشد - و ‎Bye‏

‎۰ ot: ‏چش‎ ()

‏۱ - پپلوی ۲۵۲ (کوه) « ایرانی باستان - ]81 « بارتولمه 4۳۱ » « پیب رکه ص
۰ > رك : کوه . ۴ رك : کوب . ۴ - سحیح «کویاره © (هیم.) است .

‏۴ کویال کردی 0۳21 ( ععا . چوبدست چوپان ) 6۵۳1۰ ( چویست ‎(ols‏
‏«ژابا س ۳۵۵ * ولف در قپرست خاهنامه 86۳2 ( باکاف پارسی ) آورده است :

‏ییا آورد (آردش ؟ دهخدا) زخم کوپال من ‎aly‏ کسی لیزه بر ‎Sk‏ من .
۱ فردوسی طوسی «لفت فری ‎AYRE‏
‎gle - ٩‏ کوپال و نیرو نماند زمن هیچ جز نام لیکو نماند .

‏فردوسی طوسی « رشیدی * .
۲ - الامی‌فی‌الاسامی «الاقحوان , کوبل» (الامی چاپ تهران ص۱۰۲س ۳) رله: کوپل.

‎T= ۷‏ (ه.م.) ‎gail‏ پیت ‎ple Gaol‏ ممنی شکوفه را استتباط کردماند :

افغانی (پشتو) (/0۸۸/): 0 پسگشت‌ها 5
سانسکریت (5۸4۸/582077): 9 ۸00820
1 ,۳3118 ,134 5 (8301800)) +8۸07
لهستانی (8[3آء۳0)+ 27 0 ۷۵83/۸ 2/3
روسی (۸ا85لا#): دید دا 4 (373807)) تن
اسلواکی (81.01434): 20 41 (/۷۵83) هم
لینرانی (9ف1اهاتالل7آر): 5 اناد دنه :هام بل لت هه
لتونی (لتی) (17۵بم): برهان قاطع + ۱۳۳۵
5 ,2133/1085 ۷
یادداشت:
واژه‌ی آقرمز" نیز از همین واجريشه است. ضمناً واژه‌هاي انگلیسی ۲38880 و ذرانب‌ی ۲8۸3/0181 و
اسپانبایی ۲۸384281 و ایتالیایی کهن ۲1۹884881800 و لاتین ۳0138/858107118 از ریشه‌ی سانسکریت يا ایرانی
این واژه ناشی شده‌اند.
| راگیس سوازی نارس 695
4
پهلری ماه ندب را ۹ دانمارکی (0۸1377): 110
که تتنستت: اد (ص.) کسی که پیرو 
کوبیسم نقاشی کند. ۳ ۳ 
کوپال: (قد. -۲5۳26 |گوپال] (.) گرز 
آهنین؛ شمو د. 

مواد عط رآ گین شین آمتز نک 

ورمیشل: [۹۵] ۷۰۳ (.) نوعی رشته فرنگی 
که به شکل رشته‌هایی باریکتر از اسپا گتی. 
تهیه شود و آن را در سوپ و آش بکار
```


## [2026-10-17T00:05:13.052Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR<=11980 && /\\[pdf page/ {l=$0} END{}; NR==11980{print l}' incoming/ARY/ARY_pages.txt; sed -n 11940,11968p incoming/ARY/ARY_pages.txt | head -30; grep -n -E \"KERM|KIRM|KORM|^KOPAL|GOPAL|VARGH|BARGH|VERM\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:05:14.037Z] TOOL RESULT

```
[pdf page 402]
تخاری ۸ (۸ للم ۰:70 8۸۲۵0 لیتوانی (/(۵4ا07فتا777).
سانسکریت (54/577): 0 ت30
۷6۰ کته دنله شنز لترنی (لتی) (7۲1۵/۷ا):
ارمنی (47ا۸7/87): ننشای ۱ 7 203۵۳
بونانی (072510): کید اه پروسی کهن (انفاکدت۲۸ صامم): ۸۲70
لانین (4700ه): ‏ 0۸88 ,ق0830 ایرلندی کهن (577ل8[ )+ جتفی
ایسلندی کهن (/70770(ی5 صران):

۸ ,6 ها پسگشت‌ها شک در
انگلیسی کهن (2۷60880 صا0): 17816۸01 8 وم
انگلیسی (877لا5(70): ۴ 0 (۸136) با
دانمارکی (0۸(71873): دای ۱ 9 (۸33) 2
سوئدی (8750157): 16۸ 8 (816) :00/5
نروژی (۵/08۳8007: ۸1۲618 ,81۳65 0 (16) :57
ملندی (007777)+ نداد یلا۱4 لغت‌نامه دهخدا: ۱۸۳۷۳
اسلاوی کهن (4۲76ا5 7ل#ناتن) طام): پرهان قاطع : ۱۶۳۲

زان ناد ۱
یادداشت: :
۱ واژه‌های فارسی "کرکس " و اوستایی 1۸11816۸8۸ و سانسکریت 1678۸8۸ نیز از همین واجريشه آمده‌اند.
۲- چم این واژه در زبان پهلوی: قرقاول
چم این واژه در زبان‌های غیرایرانی و غیرهندی: غرید» غدغد کردن» صدای قورباغه ایجاد کردن. :
[pdf page 402]
نی
کع ۲۳۱
اوستایی (۸887407): رای ایکا پروسی کهن (594تا۳ 0۱2): 6133118
پهلری (4۲1الل۸): 41 ,1۸6 ایرلندی کهن (لْ5ل#[ 01): ارازای هی
آوستی (05587/6): ها ولزی (7ل3ا): دیا
کردی (2782157: ۰ 831 ,6انا 1178 آلبانی (71۸07(هقم): اناد ها
5606:POKORM:SSS~*~*~*~«Sd THORN — {OLD SAXON) gySfy-Ste
6363:SRENU (RUSSIAN) yo, KARATA, KIRMIRA
8011:POKORM: = SS*SC«AT DASTAK ARMENIAN) «ga!
10845:PoKORM t™C*~=<CS~s*~‘CSs*~*«S SHAH, PADSHAH (KURDISH) 53,6
11704:cRUIM (OLD IRISH) oS 53 p! KARM, KIRM APAHLAVD) 05 ay
11707:KIRM ABALUCHD) gx se
12352:poKORME SSS 482 KYR (OLD SCANDINAVIAN) 345 sth!
12476:POKORM, = SSSOS*~*«w GURDALE, GURDILE:(KURDISH) «52,5
13618:POKORM: sSC*~CS~S*~«S MORK
```


## [2026-10-17T00:05:17.795Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/کوپال' --note 'page 545, root Wer 2, Persian kopal/gopal etymology' 2>&1 | tail -5"
}
```


### [2026-10-17T00:05:18.512Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/56c48e3b7b9b7289.txt
```


## [2026-10-17T00:05:19.979Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f=data/verification/sources/web/56c48e3b7b9b7289.txt; wc -c $f; grep -n -i -A12 \"Etymology\" $f | head -40"
}
```


### [2026-10-17T00:05:20.267Z] TOOL RESULT

```
2010 data/verification/sources/web/56c48e3b7b9b7289.txt
```


## [2026-10-17T00:05:21.658Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/web/56c48e3b7b9b7289.txt | head -40"
}
```


### [2026-10-17T00:05:21.949Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/کوپال
FETCHED: 2026-10-17T00:05:18Z
STATUS: 200
TITLE: کوپال - Wiktionary, the free dictionary

کوپال - Wiktionary, the free dictionary 

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


## [2026-10-17T00:05:26.862Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/گوپال' 'https://en.wiktionary.org/wiki/کرم' 'https://en.wiktionary.org/wiki/قرمز' 'https://en.wiktionary.org/wiki/ῥόπαλον' 'https://www.etymonline.com/word/vermouth' 'https://www.etymonline.com/word/kermes' 'https://www.etymonline.com/word/crimson' 'https://www.etymonline.com/word/carmine' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kʷŕ̥mis' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wr̥mis' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wert-' 'https://en.wiktionary.org/wiki/vergo' 'https://en.wiktionary.org/wiki/vermicelle' 'https://en.wiktionary.org/wiki/ورمیشل'; do f=$(python3 tools/fetch_source.py \"$u\" --note \"page 545, root Wer 2, checking derivation\" 2>&1 | tail -1); echo \"### $u -> $f $(wc -c < $f)\"; done",
 "timeout": 300000
}
```


### [2026-10-17T00:05:33.317Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/گوپال -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/c8645fa403e90b6f.txt 7363
### https://en.wiktionary.org/wiki/کرم -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/7738476aa3dfe87a.txt 11353
### https://en.wiktionary.org/wiki/قرمز -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/4c186094cecc737a.txt 12057
### https://en.wiktionary.org/wiki/ῥόπαλον -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/4e416277abbd0b92.txt 5158
### https://www.etymonline.com/word/vermouth -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/5f816a1edc291941.txt 135
### https://www.etymonline.com/word/kermes -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/f56e68d4313669ff.txt 133
### https://www.etymonline.com/word/crimson -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/f956d16f33359865.txt 134
### https://www.etymonline.com/word/carmine -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/8e5c815659732565.txt 134
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kʷŕ̥mis -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/3d1eee89938bdd1b.txt 3537
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wr̥mis -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/71b5cf1da772c268.txt 4838
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wert- -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/8e5cb39fa2dd5f56.txt 7055
### https://en.wiktionary.org/wiki/vergo -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/06de8ed08ac8079f.txt 14108
### https://en.wiktionary.org/wiki/vermicelle -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/99c8268bcbf7a81c.txt 2831
### https://en.wiktionary.org/wiki/ورمیشل -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/feef0b610ff14e08.txt 138
```


## [2026-10-17T00:05:36.337Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in c8645fa403e90b6f 7738476aa3dfe87a 4c186094cecc737a 4e416277abbd0b92 3d1eee89938bdd1b 71b5cf1da772c268 99c8268bcbf7a81c 5f816a1edc291941; do echo \"##### $f\"; sed -n '1p' $f.txt; grep -n -A8 -E \"^ ?Etymology\" $f.txt | grep -v -E \"^\\-?-?$|edit\" | head -25 | cut -c1-500; done"
}
```


### [2026-10-17T00:05:36.957Z] TOOL RESULT

```
##### c8645fa403e90b6f
URL: https://en.wiktionary.org/wiki/گوپال
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
154: Etymology
156-
157- Akin to the synonymous Northern Kurdish gopal , kopal , Armenian կոպալ ( kopal ) , Udi кӏовал ( ḳoval ) , Georgian კომბალი ( ḳombali ) , კობალი ( ḳobali ) , კობალა ( ḳobala ) , Laz კოპალი ( ǩop̌ali ) , Mingrelian კოპული ( ḳoṗuli ) , Ossetian къобала ( k’obala ) , къобола ( k’obola ) , Pontic Greek κοπάλι ( kopáli ) , Turkish gobal , gopbal , koppal , kobal , kubal , kopali , Romani kopal ( “ mallet; washerwoman's beetle ” ) , probably also to Jewish Babylonian Aramaic קולפא ( qwlpˀ ) , גולפ
158-
159- The origin is uncertain. Perhaps from کوب ( kôb- ) , the present stem of کوفتن ( kôftan , “ to beat, strike ” ) , with the same suffix as in چنگال ( čangâl ) . [ 1 ] [ 2 ] [ 3 ] Others derive this group of words from Greek: compare Ancient Greek κόπανον ( kópanon , “ pestle ” ) , Greek κόπανος ( kópanos , “ pestle; laundry dolly, washing beetle, battledore ” ) , Pontic Greek κοπάνιν ( kopánin ) , κοπάνι ( kopáni , “ pestle ” ) . [ 4 ] [ 5 ] [ 6 ] A native origin has been suggested for the K
160-
161- Pronunciation
##### 7738476aa3dfe87a
URL: https://en.wiktionary.org/wiki/کرم
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
79: Etymology 1 
80-
81- 2.1.1 
82- Pronunciation 
83-
84- 2.1.2 
85- Noun 
86-
87- 2.1.2.1 
94: Etymology 2 
95-
96- 2.2.1 
97- Pronunciation 
98-
99- 2.2.2 
100- Noun 
##### 4c186094cecc737a
URL: https://en.wiktionary.org/wiki/قرمز
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Declension 
69-
70- 1.2.2 
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
93- 2.3 
94- Noun 
95-
96- 2.3.1 
111: Etymology 
112-
113- 3.2 
114- Pronunciation 
115-
116- 3.3 
117- Noun 
##### 4e416277abbd0b92
URL: https://en.wiktionary.org/wiki/ῥόπαλον
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
148: Etymology
150-
151- Traditionally derived from ῥέπω ( rhépō , “ to decline, descend ” ) , but perhaps not related to the verb.
152-
153- Pronunciation
155-
156- IPA ( key ) : /r̥ó.pa.lon/ → /ˈro.pa.lon/ → /ˈro.pa.lon/ 
##### 3d1eee89938bdd1b
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kʷŕ̥mis
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Descendants 
69-
70- 1.3 
134: Etymology
136-
137- The root is unknown; compare *wr̥mis of the same meaning. This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term. 
138-
139- Noun
141-
142- *kʷŕ̥mis   m 
##### 71b5cf1da772c268
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wr̥mis
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Reconstruction notes 
69-
70- 1.2.2 
140: Etymology
142-
143- Possibly from the root *wer- ( “ to turn, to bend ” ) . [ 1 ] Alternatively, a mutation of the synonymous *kʷr̥mis . [ 2 ] 
144-
145- Noun
147-
148- *wr̥mis 
##### 99c8268bcbf7a81c
URL: https://en.wiktionary.org/wiki/vermicelle
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
146: Etymology
148-
149- Borrowed from Italian vermicelli . Doublet of vermisseau .
150-
151- Pronunciation
153-
154- IPA ( key ) : /vɛʁ.mi.sɛl/ 
##### 5f816a1edc291941
URL: https://www.etymonline.com/word/vermouth
```


## [2026-10-17T00:05:39.955Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 159,160p c8645fa403e90b6f.txt | cut -c400-1500; for f in 7738476aa3dfe87a 4c186094cecc737a; do grep -n -A4 -E \"^ ?(From|Borrowed|Inherited|Etymology [0-9]?$)\" $f.txt | grep -v \"^--\" | cut -c1-500 | sed -n 1,30p; done; grep -n -i \"Persian\\|Old Persian\\|Avestan\\|kərəm\" 3d1eee89938bdd1b.txt | head; cat 5f816a1edc291941.txt"
}
```


### [2026-10-17T00:05:40.476Z] TOOL RESULT

```
, κοπάνι ( kopáni , “ pestle ” ) . [ 4 ] [ 5 ] [ 6 ] A native origin has been suggested for the Kartvelian terms: see Proto-Kartvelian *ḳaṗ- .

62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
147: Etymology 
148-
149- 3.2 
150- Pronunciation 
151-
236: From Wiktionary, the free dictionary
237-
238- See also: كرم and گرم 
239-
240- Central Kurdish
246: From Proto-Iranian *kŕ̥miš , from Proto-Indo-Iranian *kŕ̥miš , from Proto-Indo-European *kʷŕ̥mis ( “ worm ” ) .
247-
248- Pronunciation
249- [ edit ] 
250-
276: Etymology 1
277- [ edit ] 
278-
279- PIE word 
280- *kwŕ̥mis 
282: From Proto-Iranian *kŕ̥miš , from Proto-Indo-Iranian *kŕ̥miš , from Proto-Indo-European *kʷŕ̥mis ( “ worm ” ) . Cognate with Sanskrit कृमि ( kṛ́mi , “ worm ” ) , Proto-Slavic *čьrvь ( “ worm ” ) , Lithuanian kirmi̇̀s ( “ worm ” ) .
283-
284- Pronunciation
285- [ edit ] 
286-
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
111: Etymology 
112-
113- 3.2 
114- Pronunciation 
115-
195: From Wiktionary, the free dictionary
196-
197- Arabic
198- [ edit ] 
199-
219: From Persian *کرمست ( *kermest ) , ultimately from Proto-Indo-Iranian *kŕ̥miš ( “ worm ” ) . Compare Old Armenian կարմիր ( karmir ) , Hebrew כַּרְמִיל ( karmīl ) , Iranian borrowings. First attested in 791
220-
221- Noun
222- [ edit ] 
223-
374: Borrowed from Arabic قِرْمِز ( qirmiz ) , from Persian *کرمست ( *kermest ) , ultimately from Proto-Indo-Iranian *kŕ̥miš ( “ worm ” ) , whence also the inherited doublet کرم ( kerm , “ worm ” ) .
375-
376- This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term. 
377-
378- Pronunciation
URL: https://www.etymonline.com/word/vermouth
FETCHED: 2026-10-17T00:05:29Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
```


## [2026-10-17T00:05:47.320Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/vermouth' 'https://en.wiktionary.org/wiki/Wermut' 'https://en.wiktionary.org/wiki/crimson' 'https://en.wiktionary.org/wiki/kermes' 'https://en.wiktionary.org/wiki/carmine' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wer-' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/werg-' 'https://en.wiktionary.org/wiki/verto' 'https://en.wiktionary.org/wiki/vermis' 'https://en.wiktionary.org/wiki/कृमिज' 'https://en.wiktionary.org/wiki/वृज्'; do f=$(python3 tools/fetch_source.py \"$u\" --note \"page 545, root Wer 2, checking derivation\" 2>&1 | tail -1); echo \"### $u -> $f $(wc -c < $f)\"; done",
 "timeout": 300000
}
```


### [2026-10-17T00:05:52.983Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/vermouth -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/e17a2cf269b1dc88.txt 10383
### https://en.wiktionary.org/wiki/Wermut -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/a5eb5acfd623a45f.txt 4478
### https://en.wiktionary.org/wiki/crimson -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/07e38678e8120ff7.txt 16247
### https://en.wiktionary.org/wiki/kermes -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/fd9b9b8fbaaf8d3c.txt 8122
### https://en.wiktionary.org/wiki/carmine -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/4678bb1ab35e4618.txt 13050
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wer- -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/ea35cd705403d15f.txt 8683
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/werg- -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/dace87619cc3bfaa.txt 166
### https://en.wiktionary.org/wiki/verto -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/6325187d30fdb0ad.txt 20472
### https://en.wiktionary.org/wiki/vermis -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/ff05f1c1b7cb48a4.txt 8302
### https://en.wiktionary.org/wiki/कृमिज -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/2ff756310e127d4a.txt 141
### https://en.wiktionary.org/wiki/वृज् -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/9211c1a40497e823.txt 6571
```


## [2026-10-17T00:05:56.213Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in e17a2cf269b1dc88 a5eb5acfd623a45f 07e38678e8120ff7 fd9b9b8fbaaf8d3c 4678bb1ab35e4618 ea35cd705403d15f 6325187d30fdb0ad ff05f1c1b7cb48a4 9211c1a40497e823 06de8ed08ac8079f; do echo \"##### $(sed -n 1p $f.txt)\"; grep -n -E \"^ ?(From|Borrowed|Inherited|Uncertain|Possibly|Of uncertain|Root|Probably|Related)\" $f.txt | head -4 | cut -c1-450; done"
}
```


### [2026-10-17T00:05:56.997Z] TOOL RESULT

```
##### URL: https://en.wiktionary.org/wiki/vermouth
166: Related changes 
186: From Wiktionary, the free dictionary
194: From French vermout , vermouth , from German Wermut ( “ wormwood ” ) . Doublet of wormwood .
363: Borrowed from German Wermut .
##### URL: https://en.wiktionary.org/wiki/Wermut
134: Related changes 
154: From Wiktionary, the free dictionary
164: From Middle High German wërmuote , from Old High German werimuota , from Proto-West Germanic *warjamōdā .
##### URL: https://en.wiktionary.org/wiki/crimson
89: Related terms 
171: Related changes 
191: From Wiktionary, the free dictionary
481: Related terms
##### URL: https://en.wiktionary.org/wiki/kermes
161: Related changes 
181: From Wiktionary, the free dictionary
277: Borrowed from French kermesse , from Dutch kermis .
##### URL: https://en.wiktionary.org/wiki/carmine
185: Related changes 
205: From Wiktionary, the free dictionary
229: From French carmin , from irregular Medieval Latin carminium , itself from Arabic قِرْمِز ( qirmiz , “ crimson, kermes ” ) from Persian *کرمست (*kermest), ultimately from Proto-Indo-Iranian *kŕ̥miš (“worm”), plus or with influence from Latin minium . Compare crimson and kermes . [ 1 ] 
##### URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wer-
62: Root 
74: Root 
83: Root 
127: Related changes 
##### URL: https://en.wiktionary.org/wiki/verto
142: Related terms 
243: Related changes 
263: From Wiktionary, the free dictionary
271: Borrowed from Italian vertice and Latin vertex , perhaps also Russian верши́на ( veršína ) .
##### URL: https://en.wiktionary.org/wiki/vermis
108: Related terms 
199: Related changes 
219: From Wiktionary, the free dictionary
238: From Latin vermis ( “ worm ” ) , from Proto-Italic *wormis , from Proto-Indo-European *wr̥mis . Doublet of worm .
##### URL: https://en.wiktionary.org/wiki/वृज्
71: Root 
120: Related changes 
140: From Wiktionary, the free dictionary
186: From Proto-Indo-European *h₂werg- ( “ to turn ” ) . Cognate with Latin vergō , the source of English converge etc. 
##### URL: https://en.wiktionary.org/wiki/vergo
192: Related changes 
212: From Wiktionary, the free dictionary
228: Borrowed from French verge , from Latin virga .
282: Inherited from Proto-Italic *wergō , from Proto-Indo-European *h₂wérg-e-ti , [ 1 ] from *h₂werg- ( “ to turn ” ) . Related to Hittite 𒄷𒌨𒆠𒅖 ( ḫu-ur-ki-iš /⁠ḫurkis⁠/ , “ wheel ” ) , Ancient Greek ἐέργω ( eérgō , “ to stop, scare away ” ) , Ancient Greek εἶρξαι ( eîrxai , “ to hold off ” ) , Sanskrit वृणक्ति ( vṛṇakti , “ to turn around, ward off ” ) , Sanskrit वरीवृजत्- ( varīvṛjat- , “ bending again and again ” , ptcp. ) , Sanskrit प्र वावृजे
```


## [2026-10-17T00:06:00.007Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i -E \"Arabic|qirmiz|kermes\" 07e38678e8120ff7.txt | head -5 | cut -c1-400; grep -n -i -E \"qirmiz|Arabic\" fd9b9b8fbaaf8d3c.txt | head -3 | cut -c1-400; sed -n 62,100p ea35cd705403d15f.txt | grep -v \"^ *$\" | head; grep -n -E \"turn|bend\" ea35cd705403d15f.txt | head -5 | cut -c1-300; grep -n -A3 \"Etymology\" 6325187d30fdb0ad.txt | grep -i \"Proto\" | head -3 | cut -c1-300"
}
```


### [2026-10-17T00:06:00.470Z] TOOL RESULT

```
206: Late Middle English cremesyn , from obsolete French cramoisin or Old Spanish cremesín , from Arabic قِرْمِز ( qirmiz ) , from Classical Persian کرمست ( kirmist ) , from Middle Persian ; see Proto-Indo-Iranian *kŕ̥miš . Cognate with Sanskrit कृमिज ( kṛmija ) . Doublet of kermes ; also see carmine .
238: Arabic: قِرْمِز   (ar)   m ( qirmiz ) 
279: Hindi: क़िरमिज़ी   m ( qirmizī ) 
356: Arabic: قِرْمِزِيّ   m ( qirmiziyy ) 
384: Hindi: क़िरमिज़ी ( qirmizī ) 
199: First attested ca. 1600, from French kermès , from Medieval Latin cremesinus (compare Italian chermes , Spanish carmes ), from Arabic قِرْمِز ( qirmiz ) (whence also Portuguese quermes , alquermes ), from a Persian word meaning “worm-colored” (compare modern Persian قرمز ( qermez ) ), ultimately Proto-Indo-Iranian *kŕ̥miš ( “ worm ” ) , possibly via borrowing from a Sanskrit formation. Relate
240: Hindi: किरिमदाना   (hi)   m ( kirimdānā ) , क़िरमिज़   m ( qirmiz ) , क़िरमिज़ी ( qirmizī ) , किरमिजी   (hi) ( kirmijī ) 
592: English terms derived from Arabic 
 Root 
 1.1.1 
 Alternative reconstructions 
 1.1.2 
 Derived terms 
 1.1.3 
 References 
 1.2 
 Root 
 1.2.1 
1030- From Proto-Italic *wertō , from Proto-Indo-European *wert- . [ 1 ]
```


## [2026-10-17T00:06:04.660Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^(wer-|werg-|wert-|werp-|wrmi|kwrmi|kwr|wer- ?[0-9]|wer-2|wer-3|wrmi-)\" AHD_watkins1985.txt | head; grep -n -i -E \"kermes|crimson|carmine|vermouth|vermicelli\" AHD_watkins1985.txt | head"
}
```


### [2026-10-17T00:06:04.976Z] TOOL RESULT

```
1143:wer-3
1145:wer-4
1147:wer-4. To perceive, watch out for. I. O-grade form *wor-. 1. Suffixed form *wor-o- in Germanic *waraz in: a. Old English wer, watchful: wary; b. Old English gewer, aware (ge-, collective and intensive prefix; see kom): AWARE; C. Old English warian, to beware: WARE?. 2. Suffixed form *wor-to- in Germanic *wardaz, guard, and *wardén, to guard, in: a. (i) Old English weard, a watching, keeper: WARD; STEWARD (ii) Old English wear- dian, to ward, guard: WARDER?; b. Old North French warder, to guard: WARDEN; REWARD, WARDROBE; C. Old French guarder, to guard: GUARD; d. Anglo-Norman warde, guard: REARWARD?. 3. Germanic *ward in: a. Old English waru, goods, protection, guard: WARE}; b. Old English -ware (probably plural of waru, “goods”’), inhabi- tants (< “defenders’’): FIELDFARE. 4. Suffixed form *wor-wo- in Greek ouros, a guard: ARCTURUS. 5. Variant *(s)wor-, s(w)or- probably in Greek horan, to see: EPHOR, PANORAMA. II. Suffixed (stative) form *wer-é- in Latin veréri, to respect, feel awe for: REVERE!. [Pok. 8. wer- 1164.]
1148:wer-5. To cover. I. Basic form *wer-. 1. Germanic *wer- jon- in Old English wer, dam, fish trap: WEIR. 2. Com- pound form *ap-wer-yo- (*ap-, off, away; see apo-) in Latin aperire, to open, uncover: APERIENT, APERITIF, APERTURE; OVERT, OVERTURE, PERT. 3. Compound form
642:h. Anglo-Norman aloper, to run away from one’s hus- band with a lover: ELOPE. kneigwh-. To lean on. 1. Latin cdnivére (< *con-niguére; com-, together; see kom), “to lean together” (said of eyelids), to close the eyes, be indulgent: CONNIVE. 2. Suf- fixed zero-grade form *knigvh-to- in Latin nictdre, to move the eyelids, wink: NICTITATE. 3. Uncertain preform in Latin niti, to lean forward, strive: NISUS; RENITENT. [Pok. knei-geh- 608.] knid-. Egg of a louse. Suffixed form *knid-d in Germanic *hnito in Old English hnitu, egg of a louse: NIT. [Pok. knid- 608.] ko-. Stem of demonstrative pronoun meaning “this.” I. Variant form *ki-. 1. Germanic *hi- in: a. Old English he, he: HE!; b. Old English him, him: HIM; c. Old English his, his: 1s; d. Old English hire, her: HER; e. Old English Ait, it: 1r. f. Old English hér, here: HERE; g. Old English heonane, heonon, from here: HENCE. 2. Suffixed form “ki-tro- in Germanic *hi-thra- in Old English hider, hither: HITHER. 3. Suffixed form *ki-s in Latin cis, on this side of: cis-. II. Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin céterus (neuter plural cétera), the other part, that which remains: ET CETERA. 2. Latin -ce (see nu-). III. Attrib- uted by some to this root (but more likely of obscure origin) is Germanic root *hind-, behind. 1. Old English bihindan, in the rear, behind (bi, at; see ambhi): BE- HIND, HIND!. 2. Old High German hintar (> German hinter-), behind: HINTERLAND. 3. Germanic derivative verb *hindron, to keep back, in Old English hindrian, to check, hinder: HINDER}. [Pok. ko- 609.] k6-. To sharpen, whet. Contracted from *koo-. 1. Suffixed extended form “kooi-no- in Germanic *haind in Old English hdn, stone: HONE!. 2. Perhaps Greek kénos, cone, conical object (< “a sharp-pointed object”): CONE. [Pok. Aéi- 541.] kob-. To suit, fit, succeed. Germanic *hap- in Old Norse happ, chance, good luck: HAP, (HAPPEN), (HAPPY); (HAP- LEss), (MISHAP). [Pok. kob- 610.] [kokkos. Kermes berry, pit, grain. Greek noun of un- known origin: COCCID, COCCUS, COCHINEAL; MONO- COQUE.] koksa. Body part. Latin coxa, hip: Coxa, CUISSE, CUSH- ION. [Pok. koksd 611.] kolem-. Grass, reed. Suffixed form *kolsm-o-. 1. Ger- manic “*halmaz in Old English healm, halm, straw: HAULM. 2. Latin cudmus, stalk: CULM!. 3. Zero-grade form “kibpm-o- in Greek kalamos, a reed, straw: CALA- MITE, CALAMUS, CALUMET, CARAMEL, SHAWM. [Pok. kolomo-s 612.] koli-. Glue. Suffixed variant form *koly-a in Greek kolla, glue: COLLAGE, COLLO-, COLLODION; PROTOCOL. [Pok. Rolfeji- 612.] kom. Beside, near, by, with. 1. Germanic *ga-, together, with (collective and intensive prefix and marker of the past participle), in Old English ge-, with, also participial, collective, and intensive prefix: ENOUGH, HANDIWORK, YCLEPT. 2. Latin cum, co-, with: CUM; CONQUIAN. 3. Old Latin com, with (collective and intensive prefix): co-, com-. 4, Suffixed form *kom-trd in Latin contra, against, opposite: (CON!), CONTRA-, CONTRARY, (COUNTER!), COUNTER-, COUNTRY; ENCOUNTER. 5. Suffixed form *kom-yo- in Greek koinos, common, shared: COENO-; CENOBITE, EPICENE, KOINE. 6. Reduced form *ko- (see gher-', mei-', smei-). [Pok. kom 612.] konemo-. Shinbone, bone, Reduced form *kemmo- per- haps in Germanic *hamma in Old English hamm, ham, thigh: HAM. [Pok. konamo- 613.] konk-. To hang. 1. Germanic *hanhan in: a. Old English hon, to hang: HANG; b. Dutch (dialectal) hankeren, to long for; HANKER; ¢C. possibly Middle English he(e)ng, hinge, hinge (ultimately from the base of Old English hangian, to hang): HINGE. 2. Suffixed form *konk-t-d- in
657:kermi-. Mite, worm. Rhyme word to *wrmi-, worm (see wer-3). Sanskrit krmi-, worm, in compound krmi-ja-, “(red dye) produced by worms” (ja-, produced; see gene-), borrowed into Arabic as girmiz, kermes: (CRIM- SON), KERMES. [Pok. kermi- 649.]
1146:TRORSE, SUBVERT, TERGIVERSATE, TRANSVERSE, UNI- VERSE. 5. Balto-Slavic *wirstd-, a turn, bend, in Russian versta, line: VERST. II. Root *wreit-, to turn. Germanic *writh-, *wraith- in: a. Old English writha, band (< “that which is wound around”): WREATH; b. Old English writhan, to twist, torture: WRITHE; Cc. Old English wrath, angry (< “tormented, twisted”): WRATH, WROTH. III. Root *wergh-, to turn. 1. Germanic *wurgjan in Old English wyrgan, to strangle: WORRY. 2. Nasalized vari- ant *wrengh- in: a. Germanic *wreng- in Old English wringan, to twist: WRING; b. Germanic *wrang- in (i) Old Norse *vrangr, rangr, curved, crooked, wrong, akin to the Scandinavian source of Middle English wrong, wrong: WRONG (ii) Low German wrangeln, to wrestle, akin to the Low German source of Middle English wranglen, to wrangle: WRANGLE. IV. Root *werg-, to turn. 1. Nasalized variant form *wreng- in Germanic *wrankjan in: a. Old English wrencan, to twist: WRENCH; b. Old English gewrinclian, to wind (ge-, col- lective prefix; see kom): WRINKLE. 2. Latin vergere, to turn, tend toward: VERGE?; CONVERGE, DIVERGE. V. Root *wreik-, to turn. 1. Germanic *wrig- in: a. Old English wrigian, to turn, bend, go: wRy; b. Middle Low German wriggeln, to wriggle: WRIGGLE. 2. Germanic *wrthst- whence *wristiz in Old English wrist, wrist: wRIsT. 3. Secondary Germanic derivative *wraistjan in Old English wréstan, to twist, with its frequentative *wréstlian, to wrestle: WREST, WRESTLE. 4. Possibly o-grade form *wroik- in Gaulish *briiko, heather (> French bruyére, heath): BRIAR}. VI. Germanic root *wrib- in Old French riber, to be wanton: RIBALD. VII. Root *werb-, also *werbh-, to turn, bend. 1. Ger- manic *werp-, *warp-, “to fling by turning the arm,” in Old English weorpan, to throw away: WARP. 2. Latin verber, whip, rod: REVERBERATE. 3. Latin verbéna, sacred foliage: VERBENA, (VERVAIN). 4, Zero-grade form *wrb- in Greek rhabdos, rod: RHABDOMANCY, RHABDOVI- Rus. 5. Nasalized variant form *wrembh- in Greek rhom- bos, magic wheel, rhombus: RHOMBUS. VIII. Root *werp-, to turn, wind. 1. Metathesized form *wrep- in Germanic *wrap- in Danish dialectal vraule, to wind, akin to the source of Middle English wrappen, to wrap: wraP. 2. Zero-grade form *wrp- in Greek rhaptein, to sew (> rhaphé, suture): RAPHE, RAPHIDE; RHAPSODY, STAPHYLORRHAPHY, TENORRHAPHY. IX. Root *wrmi-, worm; rhyme word to k*rmi-. 1. Germanic *wurmiz in Old English wyrm, worm: worm. 2. Latin vermis, worm: VERMEIL, VERMI-, VERMICELLI, VERMICULAR, VERMIN. [Pok. 3. ver- 1152.]
1399:CRANIUM ker-1 CRANK! ger-2 CRASH? ker-4 CRATE kert- CRATER kere- CRAW gWere-4 CRAWL! gerbh- CRAYFISH gerbh- CREATE ker-3 CREATINE kreue-1 CRECHE ger-2 CREDENCE kerd-1 CREDIBLE kerd-1 CREDIT kerd-1 CREDO kerd-1 CREDULOUS_ kerd-1 CREEK ger-2 CREEP ger-2 CREMATE ker-4 CREODONT kreue-1 CREOLE ker-3 CREOSOTE kreue-1, teus- CREPE sker-3 CREPITATE ker-2 CRESCENDO ker-3 CRESCENT ker-3 CRESS gras- CREST sker-3 CREVICE ker-2 CREW! ker-3 CRIB ger-2 CRIBRIFORM krei- CRICKET! ker-2 CRICOID  sker-3 CRIME krel- CRIMP! ger-2 CRIMSON k*rmi- CRINGE ger- CRINGLE ger-2 CRINITE sker-3 CRINKLE ger-2 CRINOLINE fino-, sker-3 CRIOSPHINX ker-1 CRIPPLE ger-2 CRISIS krei- CRISP sker-3 CRISPATE sker-3 CRISSUM sker-3 CRISTA sker-3 CRISTATE sker-3 CRITERION krei- CRITIC krei- CROCHET ger-2 CROCIDOLITE krek-1 CROCK! ger-2 GROCK® ger-? CROCKET ger-2 CROFT ger-2 CROMLECH léu-1, skerbh- CRONE sker-1 CROOK ger-2
1711:KEEL’ gel-3 KEELHAUL kele-2 KEELSON ku- KEESHOND kwon- KEN gno- KENNEL! kwon- KENNING gno- KENO penkwe KENOSIS ken-4 KERATIN ker-! KERATO- ker-1 KERCHIEF kaput KERF gerbh- KERMES k*rmi- KERN! kat-2 KERNEL gre-no- KEVEL kleu-3 KEY? kagh-
2449:VENUE gWa- VENUS wen-1 VERACIOUS wéro- VERB wer-6 VERBENA wer-3 VERBOTEN bheudh- VERDANT virére VERDICT deik-, wéro- VERDITER ters- VERGE? wer-3 VERIDICAL deik-, wéro- VERIFY wéro- VERISIMILAR wéro- VERISM Wéro- VERITY wéro- VERMEIL wer-3 VERMI- wer-3 VERMICELLI wer-3 VERMICULAR wer-3 VERMIN wer-3 VERNAL west VERRUCA wer-1 VERSATILE wer-3 VERSE! wer-3 VERSION wer-3 VERST wer-3 VERSUS wer-3 VERTEBRA wer-3 VERTEX wer-3 VERTIGO wer-3 VERVAIN wer-3 VERVE wer-6 VERY weéro- VESICA udero- VESPER weS-pero-
```


## [2026-10-17T00:06:08.687Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o -E \"VERMOUTH [a-z0-9-]+|WORMWOOD [a-z0-9-]*|ANNIVERSARY [a-z0-9-]+\" AHD_watkins1985.txt | head; sed -n 1143,1144p AHD_watkins1985.txt; sed -n 1146p AHD_watkins1985.txt | cut -c1-900; grep -n -o -E \"(VERMOUTH|wermod).{0,200}\" WLD_band3.txt SKT.txt | head -3"
}
```


### [2026-10-17T00:06:09.043Z] TOOL RESULT

```
ANNIVERSARY at-
wer-3
*wn-to- in Germanic *wundaz in Old English wund, a wound: WOUND!. 2. Suffixed o-grade form *won-yo- in Germanic *wanja-, a swelling, in Old English wen(n), wen{n), wen: WENI. [In Pok. 1. ué- 1108.] wendh-. To turn, wind, weave. 1. Germanic *windan, to wind, in: a. Old English windan, to wind: WIND2; b. Old Norse vinda, to wind: WINDLASS. 2. Germanic causative *wandjan in: a. Old English wendan, to turn to: WEND; b. Dutch wenden, to turn: WENTLETRAP. 3. Germanic *wandr6n, to roam about, in: a. Old English wandrian, to wander: WANDER; b. German wandern, to wander: WANDERLUST. 4. Germanic *wanduz in Old Norse véndr, a supple twig: WAND. 5. Germanic *wandljaz, “wan- derer,” perhaps in Latin Vandalus, a Vandal: VANDAL. [Pok. 1. uwendh- 1148.] weng-. To bend, curve. 1. Germanic *wink- in Old Eng- lish wincian, to close the eyes (< “to bend down the eyelids”): WINK. 2. Germanic *winkja in Old English wince, a reel, roller: WINCH. 3. Germanic *winkil- in Old English -wincel, spiral shell: PERIWINKLE!. 4, Germanic *wankil-, *wankul- in: a. Old English wencel, youth, maid (< “inconstant one’): WENCH; b. Old English wancol, inconstant, unsteady: wonky. 5. Germanic *wankj- in: a. Old French gauchir, to turn aside: GAUCHE; b. Anglo-Norman *wencir, to turn aside, avoid (> Middle English wincen, to kick): w1NcE. [Pok. we-n-g- 1148.] wep-. Bad, evil. From earlier *awep-. Suffixed zero-grade form *up-elo- in Germanic *ubilaz, evil, in Old English yfel, evil: EVIL. [wépnam. Weapon. Germanic root. 1. Old English wé- P(e)n, weapon: WEAPON. 2. Old Norse vapn (plural vdpn), weapon: WAPENTAKE.] wer-', High raised spot. 1. Suffixed form *wer-d- in Germanic *wartén- in Old English wearte, wart: WART. 2. Possibly Germanic *war- in obsolete Swedish var- bulde, “pus swelling” (bulde, swelling; see bhel-2), akin to the source of WARBLE2. 3. Latin varius (genitive plural variérum), spotty, speckled, changeable: (VAIR), VARIE- GATE, (VARIETY), VARIOLA, VARIORUM, VARIOUS, VARY; (MINIVER). 4. Latin varix, varicose vein: VARIX. 5. Suf- fixed and extended zero-grade form *wrsu-ko- in Latin verriica, a wart: VERRUCA. [Pok. 2. wer- 1151, 2. ud- 1108.] wer-2. To raise, lift, hold suspended. Earlier form *ower-. 1. Basic form *awer- in Greek aeirein, to raise, and Greek artéria, windpipe, artery: AORTA, ARSIS, ARTERIO-, ARTERIOLE, ARTERY. 2. Possibly referred to this root (obscure basic form *dwer-) is Greek aér (> Latin aer > Italian aria), air: AERIAL AERO-, AIR, ARIA, MALARIA. 3. Related to Greek aér, air, is Greek aura (< zero-grade form *aur-), breath, vapor: AURA. [Pok. 1. wer- 1151.] wer-3, Conventional base of various Indo-European roots; to turn, bend. I. Root *wert-, to turn, wind. 1. Germanic *werth- in: a. Germanic variant *warth- in (i) Old Eng- lish -weard, toward (< “turned toward”): -WARD (ii) Germanic *inwarth, inward (*in, in; see en), in Old English inweard, inward: INWARD; b. perhaps Germanic derivative *werthaz, “toward, opposite,” hence “equiv- alent, worth,” in Old English weorth, worth, valuable, and derivative noun weorth, wierth, value: WORTH}; STALWART. 2. Germanic *werthan, to become (< “to turn into”), in Old English weorthan, to befall: worTH?. 3. Zero-grade form *wrt- in Germanic *wurth- in Old English wyrd, fate, destiny (< “that which befalls one”): WEIRD. 4, Latin vertere, to turn, with its frequentative versare, to turn, and passive versari, to stay, behave (< “to move around a place, frequent”): VERSATILE, VERSE}, VERSION, VERSUS, VERTEBRA, VERTEX, VERTIGO, VOR- TEX; ADVERSE, ANNIVERSARY, AVERT, BOULEVERSE- MENT, CONTROVERSY, (CONVERSE!), CONVERT, DEXTRORSE, DIVERT, EVERT, (EXTROVERSION), EXTRO- VERT, INTRORSE, INTROVERT, INVERT, MALVERSATION, OBVERT, PERVERT, PROSE, RETRORSE, REVERT, SINIS-
TRORSE, SUBVERT, TERGIVERSATE, TRANSVERSE, UNI- VERSE. 5. Balto-Slavic *wirstd-, a turn, bend, in Russian versta, line: VERST. II. Root *wreit-, to turn. Germanic *writh-, *wraith- in: a. Old English writha, band (< “that which is wound around”): WREATH; b. Old English writhan, to twist, torture: WRITHE; Cc. Old English wrath, angry (< “tormented, twisted”): WRATH, WROTH. III. Root *wergh-, to turn. 1. Germanic *wurgjan in Old English wyrgan, to strangle: WORRY. 2. Nasalized vari- ant *wrengh- in: a. Germanic *wreng- in Old English wringan, to twist: WRING; b. Germanic *wrang- in (i) Old Norse *vrangr, rangr, curved, crooked, wrong, akin to the Scandinavian source of Middle English wrong, wrong: WRONG (ii) Low German wrangeln, to wrestle, akin to the Low German source of Middle English wranglen, to wrangle: WRANGLE. IV. Root *werg-, to turn. 1. Nasalized variant form *wreng- in Germanic
```


## [2026-10-17T00:06:12.211Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n -E \"urvisy|urvaes|vrnakti|vŗnakti|krmi|kfmi|kŗmi|q.ermi\" WLD_Bd1_pages.txt | head; grep -n -E \"rhopalon|ponaAov|p.palon\" WLD_Bd1_pages.txt | head -3"
}
```


### [2026-10-17T00:06:12.814Z] TOOL RESULT

```
49509:      Ai. krmi- „Wurm. Made“; np. kirm „AYurm“; alb. krimp ( krimb-i ), geg. I rum
49532:                      :   kfmi-h.
```


## [2026-10-17T00:06:15.229Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 49503,49512p WLD_Bd1_pages.txt; awk 'NR<=49509 && /\\[pdf page|leaf/ {l=$0} NR==49509{print l}' WLD_Bd1_pages.txt; grep -n -i -E \"urvi|vrnak|vfnak|varjati|vergo|verto\" WLD_Bd1_pages.txt | head"
}
```


### [2026-10-17T00:06:15.611Z] TOOL RESULT

```
„wo“ (s. o. 1 B,); auch lit. (dial.) ku „was?“ aus *kunl (Bezz. KZ. 47, 158);
apr. quei „wo“ nach Bezz. KZ. 44, 310a 1 aus *q“u-ei, und wohl der Aus-
gangspunkt des qu- statt k- im fem. nom. quai, qitoi usw.
   Ags. lift „wie“ ist aber = as. hwn, gr. tkx>.

qSrrai-     „Wurm, Made“.
      Ai. krmi- „Wurm. Made“; np. kirm „AYurm“; alb. krimp ( krimb-i ), geg. I rum
ds. (G. Meyer   EW. 206). Ir. crunn „Wurm“, cymr. pryf, corn. ds. „Wurm“
(brit. p- sichert Ansatz eines idg. Labiovel.), bret. preuu ds. Apr. ginnis
(leg. kirmis vgl. Trautmann Bsl.Wb. 134) „Made“: lit. kirm'is usw. (vgl. Traut-
junger Hund", umbr.     leaf el, gen. katles „catulus“; aisl. hadna f. „junge
58:endung ihm leider nicht vergonnt war. Zwar lagen die Buchstaben P, Ph,
1657:sal vergonnt, gewahrt", anord. audna „Schicksal, Gliick“, auelr „Keichtum“,
8866:      *e,    e   Augment (*„dann, damals“) ai. a- (auch                                                            z.   B. d-vrnak),                 av. a-,
14587:ygl. curviis ), liquis ds.               '                                             •
25703: zu *ucr- „6ffnen, schliefien", s. auch Yf. LEWb. 2 u. aperio vergo verna,                       ,            ,
25882:                                          ga s. Fick KZ. 42, 290); lat. verto,
27456:   Aber abret. guerg ..efficax", gall, vergo-bretus zu very- ..wirken”. Lat.
27633:   Abret. gtierg „efficax", gall, vergo-brelus „oberste Behorde der Aeduer"
80755: Umkehr, Ruckkehr“, Kaus. darjuranem „verto, averto, converto, reddo";
```


## [2026-10-17T00:06:18.653Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 25870,25890p WLD_Bd1_pages.txt | cut -c1-200; grep -n -E \"^ *[0-9]\\. *u.er-|„drehen, biegen\" WLD_Bd1_pages.txt | head"
}
```


### [2026-10-17T00:06:19.131Z] TOOL RESULT

```
rnrianu- n. „das Drehen“, vartida- „rund“, -a ..Spinnvirtol" (: mhd. wirtel),
vT-ttd- „gedreht, rund“ (= lat. vorsits, versus, o. u. vorsus, lit. verst as, aksl.
vnbsta), rrtti- „das Rollen“ (= lat. versi-o. aksl. vrusfa), nasaliert vnita- n..
vrntihl „Stiel, Blattstiel" (nicht nach Petersson KZ. 47, 290 zum einfachen
vrr- als Bildung vie arm. gerandi); void av. rarsdka-, ai. vrldca- ..Niere".
eigentlich „Gerolltes, \Vulst“ (Marstrander ZfceltPh. 7, 362,° der auch nir.
fare ..Buekel" usv. auf *uert-hl oder *uerl,--<i zuriickfuhrt) gr. gaxdvij
                                                                                             ;


..Ruhrloftel, RiihrkelleA figardvar                           rogvvrjv. ’H/.eToi lies, goxdoia' rogvvior
Hes. (zum Akzent und zum aol. go                                =
                                          ga s. Fick KZ. 42, 290); lat. verto,
versus, vorsus ..kehren. venden. drehen“,tw/-fer, vertex „(*Wirbel =) ScheiteF,
umbr. kuvnrtu                  ,
                                   enuertu
                                     „convertitoA trahuorft ..transverse ', osk. fegoogn 1




1607:          lung unter „drehen, biegen" denkbar ist (was aber eine formale Schei-
20624:1.     uei-  „drehen, biegen“, z. T. ncir-; viclfach von biegsamen Zweigen.
51348:gei- „drehen, biegen
```


## [2026-10-17T00:06:23.457Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; for l in 25882 49509; do awk -v L=$l 'BEGIN{n=1} {if(NR==L){print L, \"leaf\", n, \"p\", n-9; exit} n+=gsub(/\\f/,\"\")}' WLD_Bd1_pages.txt; done; grep -n -E \"ura.t|urva.sa|\\*ureik|ureik\" WLD_Bd1_pages.txt | head -5 | cut -c1-200; grep -n -E \"rhap|gonalov|gojialov|Wurfstab|Keule\" WLD_Bd1_pages.txt | head -5 | cut -c1-200"
}
```


### [2026-10-17T00:06:23.823Z] TOOL RESULT

```
25882 leaf 283 p 274
49509 leaf 532 p 523
31539:Gdf., mit Riickenverwandlung von uratt. *y.dja/.a zu *xd^ald durch Assi-
36541:unhaltbaren Gutturaltheorie aunimmt     lit. Lemerai PI. „Alpkraut, Wasser-
48367:                 m. (acc. catura/t), catvdri n., catasrah f.: ay. eadwclro m.
66413: zunehmen, daB die gleiche Bed.-Entw. im Germ. u. Lat. auf einer uralten
23001: -m    „Donnerkeil           (des      Indra)“ = av. vazra-            „Keule.       bes.          Haukeule (des
34080:  Ndl. hijze, hijs f. „Muskel, Muskelbiindel; Lendenstiick, Keule, Schlegel",
37859:camba- m. „Keule“ ( gambara „EN. eines Damons; Hirschart“? gambara-
41663:  Stock mit verdicktem Ende, Knuppel, Keule“, umbr. klavlaf ..clavolas,
41667: Keulen (des Opfertiers)“ (oder nach Thurneysen Tlies. als *dadua niiher
```


## [2026-10-17T00:06:27.187Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"WORM|kirm|kfmi|krmi\" SYN.txt | head -8 | cut -c1-200; l=$(grep -n -E \"3\\.[0-9]+ +WORM\" SYN.txt | head -1 | cut -d: -f1); echo $l; grep -n -E \"kirm|Av\\. k|Skt\\. kr\" SYN.txt | sed -n 1,5p | cut -c1-200"
}
```


### [2026-10-17T00:06:27.570Z] TOOL RESULT

```
4407:8. SCr. krme ‘swine’ (with krmaca ‘sow’), deriv. of krma ‘fodder’ (5.12), krmiti ‘feed animals’, hence orig. the animal fattened for slaughter, but com- pletely specialized to ‘swine’. Berneker 6
5140:3.84 WORM Gtk. oxdiAné Goth. mapa (waurms) Lith. kirmele a oKoUNARL ON ormr, madkr Lett. tarps ; 3 «vermis Dan. orm ChSl. ériivt th me Sw. mask SCr. crv Sp ead OE wyrm, wurm Boh.  éerv Rum, yf ae
5155:Skt. krmi-, NPers. kirm (here prob. Av. karama- used with star- of a shooting star); Ir. cruim, NIr. cruimh, cnuimh, W. pruf, Br. prenv; OLith. kirmis, now kirmélé (Lett. cerms ‘maw-worm’); here 
18580:Grk. —-rmdddtov Goth. Lith.  vairas NG Tipove ON sliri, reort Lett. stare Lat. guberndculum Dan. — styr, ror ChSI.  kritma, kritmitg It. timone Sw. _ styre, roder SCr.  krmilo Ty. gouvernail OE 
26739:6. ChSI. ériimint (Russ. cermnyj ‘pur- ple-red’, fr. the ChSl., SCr. old érman), fr. *Sirmt ‘worm’ (Slov. érm ‘finger- worm, carbuncle’, etc.) : Skt. krmi- ‘worm’, etc. (3.84). Semantic develop-
5140
997:Du. heuvel, MAG hiibel ‘hill’ : OHG hovar, OE hofer ‘hump’, Lith. kupra ‘hump’. Here also Av. kaofa- ‘mountain peak, camel’s hump’, OPers. kaufa Mountain’ (NPers. kwh ‘mountain’) : Lith. kaupas, C
1144:Av. karsvar- (: Av. karga-, Skt. kar- sa- ‘furrow’) is used in the same way as Skt. dvipa-, that is, ‘continent’. Barth. 459.
1486:Av. éat- ‘well’, NPers. éah ‘well’ : Av. kan- ‘dig’, parallel form to Skt. khan-, Barth. 583.
2019:cold’? ji i ae, N cognates is secondary, 1. Grk, Kpborany, OS frost’, Lat, crusia crust’, Skt. krad-
2410:Grk. ais 8, Kbpos xopn, xoplrat, kowé\Aa aa.sl Bpédos, pwpd NG  é7#pt puella puert infans Lat. si x ragazza fanciullo, bimbo bambino ie It. rag ‘oune fille enfant petit enfant, bébé n J he : Tr.
```


## [2026-10-17T00:06:32.237Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in CRIMSON KERMES CARMINE VERMICELLI VERSE VERGE; do grep -n -E \"^$w[, ]\" SKT.txt | head -1 | while IFS=: read l r; do sed -n \"$l,$((l+3))p\" SKT.txt | tr '\\n' ' ' | cut -c1-400; echo; done; done; grep -n -i \"Vermicelli\\|ورمیشل\" HUB.txt HRN.txt | head -2"
}
```


### [2026-10-17T00:06:32.706Z] TOOL RESULT

```
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
```


## [2026-10-17T00:06:34.608Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -A3 -E \"^(CRIMSON|KERMES|VERMICELLI|VERSE)\" SKT.txt | cut -c1-300 | head -24"
}
```


### [2026-10-17T00:06:34.982Z] TOOL RESULT

```
20748:VERSE.
20749-541
20750-be  on  the  vtrgr  of  is  quite  distinct,  and belongs  to  Verge  { 1 ).
20751-converge.  (L.>  Coined  from  L,  tan- (cwff»),  together  ;  and  verxe.
```


## [2026-10-17T00:06:36.944Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^ *(crimson|kermes|vermicelli|verge)[ ,.]\" SKT.txt | head; grep -n -i \"kermes\" SKT.txt | head -3 | cut -c1-300"
}
```


### [2026-10-17T00:06:37.547Z] TOOL RESULT

```
20755:Vermicelli,  Vermicular,  Vermi- lion :  sec  Vermin.
20757:vermicelli.  (Ital.  -  L.)  Ilal.  wrmi- f//fi,  lit.  'little  worms;*  from  the  shape. Pt.  of  vermicelU,  dimin.  of  f^rmt,  a worm.  —  Lk  Uirmtm,  ace.  of  turmit,  a worm.
3626:CochineaL  <Span.  -  L.  -  Gk.)  Sp< cochinilla^  cochineal  (made  from  iasM which  look  like  berries).  — L.  •»«'««, a  scarlet  colonr.  -  L.  c^fum,  a  Un also  kermes,  iuppo<;ed  to  Ik  a  benyt— C VMtitof.  a  berry,  cuchinnt.
```


## [2026-10-17T00:07:01.521Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in ورمیشل قرمز کوپال; do f=$(python3 tools/fetch_source.py \"https://vajehyab.com/moein/$w\" --note \"page 545, root Wer 2, Mo'in entry $w\" 2>&1 | tail -1); echo \"### $w $f $(wc -c < $f)\"; grep -n -m3 -E \"\\[|$w\" $f | cut -c1-300 | head -6; done",
 "timeout": 200000
}
```


### [2026-10-17T00:07:02.886Z] TOOL RESULT

```
### ورمیشل /home/sfmqrb/git/rishe-private/data/verification/sources/web/76c04baa90e9feca.txt 852
1:URL: https://vajehyab.com/moein/ورمیشل
4:TITLE: معنی ورمیشل | فرهنگ انتشارات معین | واژه یاب
6:معنی ورمیشل | فرهنگ انتشارات معین | واژه یاب 
### قرمز /home/sfmqrb/git/rishe-private/data/verification/sources/web/6f4ea71ee484ce57.txt 1335
1:URL: https://vajehyab.com/moein/قرمز
4:TITLE: معنی قرمز | فرهنگ انتشارات معین | واژه یاب
6:معنی قرمز | فرهنگ انتشارات معین | واژه یاب 
### کوپال /home/sfmqrb/git/rishe-private/data/verification/sources/web/75645dd9dc516b1e.txt 1041
1:URL: https://vajehyab.com/moein/کوپال
4:TITLE: معنی کوپال | فرهنگ انتشارات معین | واژه یاب
6:معنی کوپال | فرهنگ انتشارات معین | واژه یاب
```


## [2026-10-17T00:07:04.716Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 76c04baa90e9feca 6f4ea71ee484ce57 75645dd9dc516b1e; do sed -n '6,40p' $f.txt | grep -v \"^\\s*$\" | head -8; echo ----; done"
}
```


### [2026-10-17T00:07:05.056Z] TOOL RESULT

```
معنی ورمیشل | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 ورمیشل
 فرهنگ انتشارات معین
 (وِ شِ) [ فر. ] (اِ.) نوعی ماکارونی خیلی نازک که در سوپ می ریزند.
 ورمیشل در فرهنگ‌های دیگر
----
معنی قرمز | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 قرمز
 فرهنگ انتشارات معین
 (قِ مِ) [ سنس . ] (ص .) سرخ ، یکی از رنگ های سه گانة اصلی .
 قرمز در فرهنگ‌های دیگر
----
معنی کوپال | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 کوپال
 فرهنگ انتشارات معین
 (اِ.) عمود، گرز آهنین .
 کوپال در فرهنگ‌های دیگر
----
```


## [2026-10-17T00:10:06.364Z] TOOL CALL #88: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-545.py <<'PYEOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nWER=W+\"Reconstruction:Proto-Indo-European/wer-\"\nWERT=W+\"Reconstruction:Proto-Indo-European/wert-\"\nWRMIS=W+\"Reconstruction:Proto-Indo-European/wr̥mis\"\nKWRMIS=W+\"Reconstruction:Proto-Indo-European/kʷŕ̥mis\"\nPOK_A={\"src\":\"POK\",\"where\":\"p. 1152 (POK_full.txt l.91474ff.)\",\"stance\":\"supports\",\"note\":\"'uer-3 ... Meaning: to turn, bend ... Note: ... only abstraction for derivatives and Root extensions. Page(s):1152', followed by sub-entries A. ur̥mi-s 'worm', B. uer-b-, D. uer-g-, E. uer-gh-, G. uer-p-, H. uer-t-, I. ur-ei- (incl. ureik-).\"}\nPOK_KW={\"ref\":\"POK:649\",\"status\":\"supports\",\"note\":\"POK_full.txt l.53510ff. 'kʷr̥mi- ... Meaning: worm, grub ... Material: Old Indic kr̥mi- worm, maggot; np. kirm worm; alb. krimp ...; Old Irish cruim ...; Lithuanian kirmis'. Pokorny gives no Avestan or Old Persian form here.\"}\nentry={\n \"entry\":0,\n \"root\":\"Wer 2, Werb, Werg 3, Wermi, Kwermi, Werp, Wert, Wrei\",\n \"verdict\":\"plausible\",\n \"modern_form\":\"PIE *wer- (3) 'to turn, bend' (Pokorny 1152-1160 u̯er-3, with extensions *werb-, *werǵ-/*h₂werg-, *wergʰ-, *werp-, *wert-, *wreyk-; Watkins wer-3), plus the separate 'worm' word *kʷŕ̥mis (Pokorny 649)\",\n \"note\":\"The root box is right for wer-3 'to turn, bend' and its enlargements: Pokorny 1152-1158 and Watkins (wer-3, sections I-IX) list *wert- (Lat. vertere), *werg- (Skt. vṛṇákti/várjati, Lat. vergere), *werb-, *werp- (Gk. rhopalon under 1156), *wreyk- (Av. urvisyeiti) and *wr̥mi- 'worm' (Lat. vermis). 'Kwermi' (*kʷŕ̥mis, Skt. kṛmi, NP kirm) is a different root. Pokorny 649 and Watkins call it only a 'rhyme word' to *wr̥mi-, and Wiktionary gives its root as unknown. So nodes 8-14 hang under the wrong root. Problems in the nodes: Latin 'vetere' is the book's misprint for vertere (node 4); English 'vermouth' is Germanic (German Wermut), not from Latin (node 7); Persian kopāl/gopāl is an areal Caucasian-Iranian word and cannot come from the ancestor of Greek rhopalon (node 16). Extraction check against the printed page (site/pages/545.jpg, re-rendered at 300 dpi): all words match the print, but the JSON makes Arabic qermez (#13) a child of Sogdian kyrm (#12). On the page both Sogdian and Arabic hang from one trunk that drops from the Sanskrit krmi box (#10), so the parent of #13 should be 10.\",\n \"note_fa\":\"ریشهٔ هندواروپایی آغازین *wer- «گرداندن، خم کردن» با گسترش‌های *wert- و *werg- و *werp- و *wreyk- و نام‌واژهٔ *wr̥mi- «کرم» در پوکورنی (ص ۱۱۵۲-۱۱۵۸)، والده-پوکورنی و واتکینز آمده است. تا اینجا ادعای نورایی درست است. ولی «Kwermi» یعنی *kʷŕ̥mis (سنسکریت kṛmi و فارسی «کرم») ریشهٔ جداگانه‌ای است. پوکورنی (ص ۶۴۹) و واتکینز آن را فقط «هم‌قافیه» با *wr̥mi- می‌دانند، پس شاخهٔ «کرم» و «قرمز» زیر ریشهٔ نادرستی آمده است. در این صفحه vetere خطای چاپی کتاب به جای vertere است. vermouth از آلمانی Wermut آمده و لاتینی نیست. «کوپال» هم با یونانی rhopalon پیوندی ندارد. در استخراج داده، پدرِ گرهٔ عربی «قرمز» باید سنسکریت (#10) باشد نه سغدی.\",\n \"sources\":[WER,WERT,WRMIS,KWRMIS],\n \"ref_check\":[{\"ref\":\"POK:1142-1157\",\"status\":\"supports\",\"note\":\"POK_full.txt l.91474 'Root / lemma: uer-3 ... Meaning: to turn, bend ... Page(s):1152'; sub-entries D (l.91578, 1154), G (l.91713, 1156), H (l.91760, 1156-1158), I δ ureik- (l.91929, 1158) cover the extensions named in the box. Kwermi is not here; it is a separate lemma on p. 649.\"}],\n \"consulted\":[\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wer-3 (AHD_watkins1985.txt l.1146)\",\"stance\":\"supports\",\"note\":\"'wer-3. Conventional base of various Indo-European roots; to turn, bend. I. Root *wert- ... Latin vertere ... ANNIVERSARY ... UNIVERSE ... IV. Root *werg- ... Latin vergere ... IX. Root *wrmi-, worm; rhyme word to kʷrmi- ... Latin vermis: VERMICELLI ... [Pok. 3. wer- 1152.]'\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. kʷrmi- (l.657)\",\"stance\":\"partial\",\"note\":\"'kʷrmi-. Mite, worm. Rhyme word to *wrmi-, worm (see wer-3) ... [Pok. kʷrmi- 649.]', a separate root, not part of wer-3.\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I 274 (WLD_Bd1_pages.txt l.25882, leaf 283)\",\"stance\":\"supports\",\"note\":\"under uert-: 'lat. verto, versus, vorsus „kehren, wenden, drehen“'.\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I 523 (l.49508, leaf 532)\",\"stance\":\"partial\",\"note\":\"'qʷr̥mi- „Wurm, Made“. Ai. kr̥mi- „Wurm, Made“; np. kirm „Wurm“'. A separate lemma.\"}\n ],\n \"nodes\":[]\n}\nN=entry[\"nodes\"]\nN.append({\"id\":1,\"lang\":\"Sanskrit\",\"words\":\"varj\",\"verdict\":\"confirmed\",\n \"derivation\":\"Sanskrit vṛj- (present vṛṇákti, várjati) means 'to turn, twist, turn aside, ward off'. It continues PIE *werg- / *h₂werg- 'to turn' (Pokorny 1154 u̯er-g-), the same root as Latin vergere and Hittite ḫurkis 'wheel'. 'varj' is the guṇa grade of the root and the gloss 'to turn around' is correct.\",\n \"derivation_fa\":\"ریشهٔ سنسکریت vṛj- (vṛṇákti و várjati) «گرداندن، پیچاندن، بازگرداندن» است. از هندواروپایی آغازین *werg- (یا *h₂werg-) «گرداندن» آمده و با لاتینی vergere و هیتی ḫurkis «چرخ» هم‌ریشه است. پوکورنی (ص ۱۱۵۴) و ویکی‌واژه همین را می‌گویند و ادعای نورایی درست است.\",\n \"sources\":[W+\"वृज्\",W+\"vergo\"],\n \"ref_check\":[{\"ref\":\"POK:1154\",\"status\":\"supports\",\"note\":\"POK_full.txt l.91578ff. 'uer-3. D. uer-g- ... Meaning: to turn / Material: Old Indic vr̥nakti, varjati wendet, dreht ...; Latin vergō, -ere sich neigen'.\"}],\n \"consulted\":[\n  {\"src\":\"WLD\",\"where\":\"via POK references 'WP. I 271 f.'\",\"stance\":\"supports\",\"note\":\"Pokorny's entry cites Walde-Pokorny I 271f. for the same equation ai. vr̥nákti : lat. vergere (not re-read separately).\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.260631 s.v. verge (v.)\",\"stance\":\"supports\",\"note\":\"'L. vergere, to bend, incline, turn, prob. cogn. with OI. vṛnakti, varjati, he turns, twists, fr. I.-E. base *wereg-, *werg-'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 wer-3 IV\",\"stance\":\"supports\",\"note\":\"'IV. Root *werg-, to turn ... 2. Latin vergere, to turn, tend toward: VERGE'.\"}\n ]})\nN.append({\"id\":2,\"lang\":\"Persian\",\"words\":\"varğ\",\"verdict\":\"plausible\",\n \"derivation\":\"NP varğ / barğ means 'weir, dam of brushwood, earth and mud set across a stream' (Borhan) and is attested in Farrokhi's verse quoted on the chart. Horn no. 1080 (p. 242), following Nöldeke, compares Skt. várga- 'remover, averter' from √varj- / várjati, and Mo'in's footnote to Borhan repeats this. So the word would be the Iranian cognate *warga- 'that which turns (water) away' of the Sanskrit root. It is not a descendant of the Sanskrit word, as the arrow implies. The link is only a comparison: no Middle Persian or Old Iranian intermediate is attested, and the fricative ğ for expected g is unexplained. Treat it as possible but unproven.\",\n \"derivation_fa\":\"«ورغ» یا «برغ» به معنی بندی است که از چوب و علف و خاک و گل پیش رودخانه می‌بندند و در شعر فرخی آمده است. هرن (شمارهٔ ۱۰۸۰) به پیروی از نلدکه آن را با سنسکریت várga- «برگرداننده» از ریشهٔ varj- سنجیده و معین هم در حاشیهٔ برهان همین را آورده است. بنابراین «ورغ» در بهترین حالت هم‌ریشهٔ ایرانی واژهٔ سنسکریت است، نه بازماندهٔ آن. صورت فارسی میانه یا ایرانی باستانِ آن گواهی ندارد و «غ» به جای «گ» هم توضیح داده نشده است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"HRN:242\",\"status\":\"supports\",\"note\":\"HRN.txt leaf 263 (p. 242): '1080. verγ „Wasserwehr“, berγ. skr. vārga- „Abwender“, also zu √varj-, várjati (Nöldeke, mündliche Mitteilung)'.\"},\n  {\"ref\":\"BQT:2273\",\"status\":\"supports\",\"note\":\"BQT p. 2273 (read from image, saved as ocr/BQT/2273.vision.txt): 'ورغ ... بندی را گویند که از چوب و علف وخاک وگل درپیش رودخانه‌ها بندند'; footnote 8: 'برغ (ﻫ.م.)؛ سانسکریت várga (برگرداننده)، نیز ازریشهٔ várjati, varj (بقول نلدکه) «اسشق ۱۰۸۰»' with Farrokhi's verse.\"},\n  {\"ref\":\"BQT:258\",\"status\":\"not_checked\",\"note\":\"tools/ref_page.py: 'no scan of BQT covers printed page 258'; BQT_v1_pages.txt OCR has no readable برغ entry.\"}],\n \"consulted\":[\n  {\"src\":\"HUB\",\"where\":\"HUB.txt (Horn-number index)\",\"stance\":\"silent\",\"note\":\"grep for '1080.' finds no Hübschmann comment on Horn 1080.\"},\n  {\"src\":\"BQT\",\"where\":\"vol. 4 p. 2273 + BQT_v4_pages.txt l.13236\",\"stance\":\"supports\",\"note\":\"another entry: 'بمعنی برغ است وآن بندی باشد که درپیش آب ...', which confirms the meaning 'dam'.\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_pages.txt l.10934\",\"stance\":\"silent\",\"note\":\"only '(به چم آبخشی از برغ)' in passing; no etymology of برغ found.\"}\n ]})\nN.append({\"id\":3,\"lang\":\"Avestan\",\"words\":\"urvisyeiti; varep; a-vareta\",\"verdict\":\"plausible\",\n \"derivation\":\"(1) urvisyeiti 'turns (himself)' is the present of Av. urvaēs- 'to turn' (causative urvaēsaya-, noun urvaēsa- 'turning-point'), from Indo-Iranian *wrayš- / PIE *wreyk- (Pokorny 1158 ureik-; cf. Gk. rhoikós 'crooked', OE wrigian > wry). This is confirmed. (2) 'varep' is Av. varəp-, attested only with aiwi- in the sense 'to mark, put a sign on' (Bartholomae). Bartholomae marks its etymology and meaning as uncertain, so a link to *werp- 'turn, wind' is possible but unproven. (3) a-varəta- (Bartholomae avarətā- f. 'Wertgegenstand, Besitztum', a valuable object or possession) is linked by Klein, s.v. worth, 'probably' to Germanic *werþa- 'worth' and so to *wert- 'turn'. The prefix a- and the formation are unclear and this is not standard. Worst verdict for the node: plausible.\",\n \"derivation_fa\":\"urvisyeiti «می‌گردد، برمی‌گردد» از ستاک اوستایی urvaēs- «گشتن» است (سببی urvaēsaya- و نام‌واژهٔ urvaēsa- «پیچ، نقطهٔ بازگشت») و از هندواروپایی *wreyk- می‌آید (پوکورنی ص ۱۱۵۸، کلاین ذیل wry). این بخش درست است. varəp- در اوستایی تنها با پیشوند aiwi- به معنی «نشان گذاشتن» آمده و بارتولومه ریشه‌شناسی آن را نامعلوم می‌داند. avarətā- «چیز گران‌بها، دارایی» نزد بارتولومه آمده و کلاین آن را «احتمالاً» با worth انگلیسی هم‌ریشه می‌داند. این دو پیوند پذیرفتنی‌اند ولی ثابت نشده‌اند.\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"KLN:1752\",\"status\":\"supports\",\"note\":\"KLN_1971.txt l.268840ff. s.v. wry: '... cogn. with Avestic urvisyeiti, turns, revolves, Gk. rhoikós (for *wroikos), crooked ... derivatives of I.-E. *wreik-, *wrik-, to turn, twist, bind'.\"},\n  {\"ref\":\"KLN:1755\",\"status\":\"partial\",\"note\":\"KLN_1971.txt l.268449ff. s.v. worth: '... prob. cogn. with Avestic avarəta-, a valuable object, W. gwerth, price'. Klein says only 'probably'. No 'varep' found in Klein.\"},\n  {\"ref\":\"POK\",\"status\":\"supports\",\"note\":\"POK_full.txt l.91929ff. 'uer-3. I. ur-ei- δ) ureik- ... to turn, bind / Material: Avestan urvisyeiti (*vrisyati) wendet sich, dreht sich, Kaus. urvaēsayeiti wendet, dreht, urvaēsa- m. gyration (= gr. rhoikós ...)' (p. 1158).\"}],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"col. 1544ff. s.v. urvaēs- (BRT.txt l.25553)\",\"stance\":\"supports\",\"note\":\"'urvaēs- V. (sich) drehen, wenden. Praes. urvisya-, Kaus. urvaēsaya- ... 1) sich drehen, kreisen ... 2) sich wenden, umkehren'.\"},\n  {\"src\":\"BRT\",\"where\":\"varəp- (BRT.txt l.22925)\",\"stance\":\"partial\",\"note\":\"'varəp- V., nur mit aiwi „mit einem Zeichen versehen“ ... etwas (Akk.) zeichnen, signiren ... Et. und Bed.?' — the word exists; its etymology is left open.\"},\n  {\"src\":\"BRT\",\"where\":\"col. 176 s.v. a-varətā- (BRT.txt l.5129)\",\"stance\":\"partial\",\"note\":\"'a-varətā- f. „Wertgegenstand, Besitztum“ (Yt 11.7; V. 5.39 ...)'. The meaning matches Nourai's gloss. No link to *wert- is given.\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I (WLD_Bd1_pages.txt)\",\"stance\":\"silent\",\"note\":\"grep 'urvisy|urvaes' finds nothing in the OCR.\"}\n ]})\nN.append({\"id\":4,\"lang\":\"Latin\",\"words\":\"vetere; vergere; vermis\",\"verdict\":\"transcription_suspect\",\n \"derivation\":\"'vetere : to turn' is a misprint for Latin vertere 'to turn' (PIE *wert-, Proto-Italic *wertō; Pokorny 1156-1158). The book itself prints 'vetere' (checked on site/pages/545.jpg and a 300-dpi render), so the extraction is faithful and the r is missing in Nourai's print. vergere 'to bend, incline, turn' < Proto-Italic *wergō < PIE *h₂werg- (Pokorny 1154; Watkins wer-3 IV) is confirmed. vermis 'worm' < Proto-Italic *wormis < PIE *wr̥mis (Pokorny 1152 'uer-3. A. ur̥mi-s'; Watkins wer-3 IX) is confirmed, and Wiktionary calls the link to *wer- 'turn' only possible.\",\n \"derivation_fa\":\"«vetere» خطای چاپی خود کتاب به جای لاتینی vertere «گرداندن» است، که از هندواروپایی *wert- می‌آید. در صفحهٔ چاپی هم vetere آمده و استخراج داده درست است. vergere «خم شدن، گراییدن» از *h₂werg- است (پوکورنی ص ۱۱۵۴). vermis «کرم» از *wr̥mis است، که پوکورنی و واتکینز آن را زیر *wer- آورده‌اند و ویکی‌واژه این پیوند را «ممکن» می‌داند. بنابراین دو واژهٔ دیگر درست‌اند و تنها خطا، خطای چاپی کتاب است.\",\n \"error_in\":\"book\",\"book_prints\":\"vetere\",\"correct_form\":\"vertere\",\n \"sources\":[W+\"verto\",W+\"vergo\",W+\"vermis\",WRMIS,WERT],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 wer-3: 'I. Root *wert- ... 4. Latin vertere, to turn ...'; 'IV. Root *werg- ... Latin vergere'; 'IX. Root *wrmi-, worm ... Latin vermis, worm'.\"}],\n \"consulted\":[\n  {\"src\":\"POK\",\"where\":\"pp. 1152, 1154, 1156-1158\",\"stance\":\"supports\",\"note\":\"l.91488 'Latin vermis (from *vormis, *urmis)'; l.91583 'Latin vergō, -ere sich neigen'; l.91793 'Latin vertō ..., versum kehren, turn'.\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I 274\",\"stance\":\"supports\",\"note\":\"'lat. verto, versus, vorsus „kehren, wenden, drehen“, vertex'.\"},\n  {\"src\":\"KLN\",\"where\":\"s.v. verge v.; worm\",\"stance\":\"supports\",\"note\":\"'L. vergere, to bend, incline, turn ... I.-E. base *werg-'; s.v. worm: 'L. vermis (for *wormis, *wr̥mis), worm ... fr. I.-E. base *wer- to bend, turn, twist'.\"},\n  {\"src\":\"LAT\",\"where\":\"not opened\",\"stance\":\"silent\",\"note\":\"not consulted further: the Latin forms are uncontroversial.\"}\n ]})\nN.append({\"id\":5,\"lang\":\"French\",\"words\":\"vermicelle\",\"verdict\":\"confirmed\",\n \"derivation\":\"French vermicelle is a borrowing of Italian vermicelli, the plural of vermicello 'little worm'. This continues Vulgar Latin *vermicellus, a diminutive of Latin vermiculus / vermis 'worm'. The pasta is named for its worm-like threads. The French word is a learned or culinary loan and not inherited; it is a doublet of vermisseau. The chain Latin vermis → (Italian) → French is correct, although the chart skips the Italian step.\",\n \"derivation_fa\":\"فرانسوی vermicelle از ایتالیایی vermicelli «کرمک‌ها» وام گرفته شده است. vermicelli جمع vermicello، تصغیرِ لاتینی vermis «کرم» است و این خوراکی را از شکل رشته‌های کرم‌مانندش چنین نامیده‌اند. نورایی میانجی ایتالیایی را نیاورده، ولی پیوند با لاتینی vermis درست است.\",\n \"sources\":[W+\"vermicelle\"],\n \"ref_check\":[{\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"node has no reference (refs=None).\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.260743 s.v. vermicelli\",\"stance\":\"supports\",\"note\":\"'It., pl. of vermicello, little worm, fr. VL. *vermicellus, dimin. of L. vermiculus, itself dimin. of vermis, worm'.\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt l.20757\",\"stance\":\"supports\",\"note\":\"'vermicelli. (Ital. - L.) Ital. vermicelli, lit. little worms; from the shape. Pl. of vermicello, dimin. of verme, a worm. - L. vermem, acc. of vermis'.\"}\n ]})\nN.append({\"id\":6,\"lang\":\"Persian\",\"words\":\"vermîšel\",\"verdict\":\"confirmed\",\n \"derivation\":\"NP vermišel 'vermicelli, very thin noodles for soup' is a modern (19th-20th c.) loan from French vermicelle, with French -c- /s/ rendered as š. Mo'in labels it [فر.] (French). The route is Latin vermis → Italian vermicelli → French vermicelle → Persian.\",\n \"derivation_fa\":\"«ورمیشل» نوعی ماکارونی بسیار نازک برای سوپ است و وام‌واژه‌ای نو از فرانسوی vermicelle است. معین آن را [فر.] نشان داده است. این واژه از لاتینی vermis «کرم» از راه ایتالیایی vermicelli و فرانسوی vermicelle به فارسی رسیده و ادعای نورایی درست است.\",\n \"sources\":[\"https://vajehyab.com/moein/ورمیشل\"],\n \"ref_check\":[{\"ref\":\"MON:5011\",\"status\":\"supports\",\"note\":\"vajehyab Mo'in: 'ورمیشل (وِ شِ) [ فر. ] (اِ.) نوعی ماکارونی خیلی نازک که در سوپ می ریزند'. The page number cannot be checked online.\"}],\n \"consulted\":[\n  {\"src\":\"MON\",\"where\":\"2-vol abridgement, MON_part2.txt l.85607\",\"stance\":\"supports\",\"note\":\"'ورمیشل: [فر.] (اِ.) نوعی رشته فرنگی که به شکل رشته‌هایی باریکتر از اسپاگتی تهیه شود'.\"},\n  {\"src\":\"KLN\",\"where\":\"s.v. vermicelli\",\"stance\":\"supports\",\"note\":\"Italian/Latin source of the French word (see node 5).\"}\n ]})\nN.append({\"id\":7,\"lang\":\"English\",\"words\":\"adverse, anniversary, convert, divert, invert, version, versus, universe, university, vertebra, vice-versa, vertical, transverse, verse, verge, vermicelli, vermouth\",\"verdict\":\"disputed\",\n \"derivation\":\"Most of the list is right. adverse, anniversary, convert, divert, invert, version, versus, universe, university, vertebra, vice versa, vertical (via vertex), transverse and verse all go back to Latin vertere / versus 'to turn, turned' (PIE *wert-), through Old French or directly from Latin (Watkins wer-3 I.4; Klein s.v. version). verge 'to incline' is from Latin vergere. Note that the noun verge 'rod, edge' is a separate word from Latin virga. vermicelli is from Italian, from Latin vermis. vermouth is the error: it comes through French vermout from German Wermut 'wormwood' (OHG werimuota, Proto-West Germanic *warjamōdā), a doublet of English wormwood. It does not come from Latin. Its Germanic etymology is obscure and it is not usually referred to *wer- 'turn'. Because of vermouth the node is marked disputed.\",\n \"derivation_fa\":\"بیشتر این واژه‌های انگلیسی (adverse، anniversary، convert، divert، invert، version، versus، universe، university، vertebra، vice versa، vertical، transverse، verse) از لاتینی vertere/versus «گرداندن، گردانده» و ریشهٔ *wert- آمده‌اند. verge (فعل) از vergere و vermicelli از ایتالیایی و در اصل از vermis است. ولی vermouth از راه فرانسوی vermout از آلمانی Wermut «افسنتین» آمده و هم‌زاد wormwood انگلیسی است. لاتینی نیست و ریشهٔ ژرمنی آن هم روشن نیست. پس این یک واژه نادرست در این شاخه آمده است.\",\n \"sources\":[W+\"vermouth\",W+\"Wermut\",W+\"verto\"],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 wer-3 I.4 lists 'VERSATILE, VERSE, VERSION, VERSUS, VERTEBRA, VERTEX, ... ADVERSE, ANNIVERSARY, ... CONVERT, DIVERT, ... INVERT, ... TRANSVERSE, UNIVERSE'; IV.2 'VERGE, CONVERGE, DIVERGE'; IX.2 'VERMICELLI'. VERMOUTH is not under wer-3 (not in the index list VERMEIL ... VERMIN ... VERSE).\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.260831 s.v. vermouth; l.268354 s.v. wormwood\",\"stance\":\"contradicts\",\"note\":\"'vermouth ... F. vermout, fr. G. Wermut, which is rel. to wormwood'; 'wormwood ... OE. wermod ... OHG werimuota ... G. Wermut'. Germanic, not Latin.\"},\n  {\"src\":\"KLN\",\"where\":\"l.261020ff. s.v. version; l.260618 s.v. verge n.\",\"stance\":\"supports\",\"note\":\"version entry lists 'adverse ... anniversary ... convert ... divert ... invert ... transverse, universe, university, verse ... versus, vertebra ... vertical ... vice versa' under I.-E. *wert-. Separately, 'verge, n. ... fr. L. virga, twig, rod'.\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt l.20748ff.\",\"stance\":\"supports\",\"note\":\"'Verge (1)' (rod) is kept apart from 'converge ... verge (2)'; vermicelli 'Ital. - L.'.\"}\n ]})\nN.append({\"id\":8,\"lang\":\"Avestan / Old Persian\",\"words\":\"kermi, kerma, karem\",\"verdict\":\"plausible\",\n \"derivation\":\"The Iranian 'worm' word is Proto-Iranian *kŕ̥miš (PIE *kʷŕ̥mis). Avestan has kərəma- only in stārō.kərəma- 'shooting star' (literally 'star-worm'). Horn and Mann gloss Av. kərəma- as 'worm', but Hübschmann notes 'the meaning of Av. kərəma- is quite uncertain' and Buck says it is 'probably' the same word. No Old Persian form is attested. 'kermi' is not an Iranian form at all: it is the Sanskrit-like stem. The node therefore mixes the Avestan form, a reconstruction and an unattested Old Persian label. Its parent is also *kʷŕ̥mis, not *wer- 'turn'. The worm word itself is real.\",\n \"derivation_fa\":\"واژهٔ ایرانی برای «کرم» از ایرانی آغازین *kŕ̥miš و هندواروپایی *kʷŕ̥mis است. در اوستایی kərəma- تنها در ترکیب stārō.kərəma- «شهاب» (به معنای لفظی «ستاره-کرم») آمده است. هوبشمان معنای kərəma- را «بسیار نامطمئن» می‌داند. در پارسی باستان هیچ صورتی گواهی نشده و «kermi» صورت سنسکریت‌گونه است، نه ایرانی. این واژه از ریشهٔ جداگانهٔ *kʷŕ̥mis است، نه از *wer- «گرداندن». پس ادعای نورایی تنها با احتیاط پذیرفتنی است.\",\n \"sources\":[KWRMIS,W+\"کرم\"],\n \"ref_check\":[POK_KW],\n \"consulted\":[\n  {\"src\":\"HRN\",\"where\":\"no. 850 (HRN.txt l.7412)\",\"stance\":\"supports\",\"note\":\"'850. kirm „Wurm“. aw. kərəma- „Wurm“; phlv. karm; ai. kr̥mi- (krimi-) „Wurm“'.\"},\n  {\"src\":\"HUB\",\"where\":\"no. 850 (HUB.txt l.3072)\",\"stance\":\"contradicts\",\"note\":\"'850. Die Bedeutung von zd. kərəma- ist ganz unsicher.'\"},\n  {\"src\":\"NYB\",\"where\":\"Glossary s.v. kirm (NYB_vol2_glossary.txt l.2297)\",\"stance\":\"partial\",\"note\":\"'kirm [klm] dragon ... Skr kr̥mi- „snake“, cf Av. stārō.kərəma- „shooting star“; MPrth krm „comet“; NP kirm „worm“'.\"},\n  {\"src\":\"SYN\",\"where\":\"3.84 WORM (SYN.txt l.5155)\",\"stance\":\"partial\",\"note\":\"'Skt. kr̥mi-, NPers. kirm (here prob. Av. kərəma- used with star- of a shooting star)'.\"},\n  {\"src\":\"IEC\",\"where\":\"s.v. qʷrmis (IEC.txt l.14262)\",\"stance\":\"supports\",\"note\":\"'qʷrmis ... worm, grub. WP I, 523 ... Skt. kr̥mih; Av. (variant) kərəma, f. id.; Per. kirm, id.'.\"},\n  {\"src\":\"BRT\",\"where\":\"BRT.txt l.9574\",\"stance\":\"partial\",\"note\":\"only 'kərəma- Adj., mit star- m. „Sternschnuppe“' found in the OCR; no separate 'worm' noun.\"}\n ]})\nN.append({\"id\":9,\"lang\":\"Persian\",\"words\":\"kerm\",\"verdict\":\"confirmed\",\n \"derivation\":\"NP kerm/kirm 'worm' < MP kirm [klm] 'worm, serpent' (Manichaean krm) < Proto-Iranian *kŕ̥miš < PIE *kʷŕ̥mis. The Old Iranian syllabic *r̥ became ir/ar in Middle Persian (MP spellings kirm/karm). Cognates are Skt. kṛmi-, Kurdish kurm, Ossetic kalm 'snake', Lith. kirmis and Old Irish cruim. The word is real and the arrow from the Iranian worm word is right. Only the higher attachment to *wer- is wrong (see the root note).\",\n \"derivation_fa\":\"«کرم» از فارسی میانهٔ kirm «کرم، مار» (مانوی krm) و ایرانی آغازین *kŕ̥miš، از هندواروپایی *kʷŕ̥mis آمده است. r هجایی ایرانی باستان در فارسی میانه به ir یا ar بدل شده است. سنسکریت kṛmi-، کردی kurm، آسی kalm «مار» و لیتوانیایی kirmis هم‌ریشهٔ آن‌اند. هرن و مکنزی و برهان (حاشیهٔ معین) همین را می‌گویند و ادعای نورایی درست است.\",\n \"sources\":[W+\"کرم\",KWRMIS],\n \"ref_check\":[{\"ref\":\"BQT:1625\",\"status\":\"supports\",\"note\":\"BQT p. 1625 (ref_page OCR): 'کرم - بکسر اول، پهلوی karm (kirm). سانسکریت kr̥mi (کرم)، کردی ...، استی ... (مار) ... بلوچی ... هوبشمان ۸۵۰'.\"}],\n \"consulted\":[\n  {\"src\":\"HRN\",\"where\":\"no. 850\",\"stance\":\"supports\",\"note\":\"'kirm „Wurm“. aw. kərəma-; phlv. karm; ai. kr̥mi-; kurd. kurm; oss. t. kalm „Schlange“'.\"},\n  {\"src\":\"PHD\",\"where\":\"p. 51 (PHD.txt l.428)\",\"stance\":\"supports\",\"note\":\"'kirm [klm | M krm, N ~] worm, serpent'.\"},\n  {\"src\":\"NYB\",\"where\":\"s.v. kirm\",\"stance\":\"supports\",\"note\":\"'NP kirm „worm“' < MP kirm.\"},\n  {\"src\":\"ARY\",\"where\":\"pdf page 402 (ARY_pages.txt l.11940ff.)\",\"stance\":\"supports\",\"note\":\"entry کرم with Pahlavi karm, kirm (Latin index l.11704 'KARM, KIRM (PAHLAVI)'), and the note that «قرمز» comes from the same root.\"}\n ]})\nN.append({\"id\":10,\"lang\":\"Sanskrit\",\"words\":\"krmi; krmi-ja\",\"verdict\":\"confirmed\",\n \"derivation\":\"Sanskrit kṛ́mi- 'worm, maggot' < PIE *kʷŕ̥mis (Pokorny 649). kṛmi-ja- 'produced by worms', i.e. the red dye from the kermes or lac insect, is kṛmi- + -ja- 'born of' (from jan- 'to be born', PIE *ǵenh₁-; hence the chart's cross-reference to Gene 1). Both words and glosses are correct. As in the root note, the worm word belongs to *kʷŕ̥mis and not to *wer- 'turn'.\",\n \"derivation_fa\":\"سنسکریت kṛ́mi- «کرم» از هندواروپایی *kʷŕ̥mis است (پوکورنی ص ۶۴۹). kṛmi-ja- «زاده از کرم» نام رنگ سرخی است که از حشرهٔ قرمزدانه به دست می‌آید و از kṛmi- و -ja- «زاده» (از ریشهٔ jan- «زادن») ساخته شده است. هر دو واژه و معنایشان درست است، ولی ریشهٔ آن‌ها *kʷŕ̥mis است، نه *wer-.\",\n \"sources\":[KWRMIS,W+\"crimson\"],\n \"ref_check\":[POK_KW],\n \"consulted\":[\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. kʷrmi- (l.657)\",\"stance\":\"supports\",\"note\":\"'Sanskrit kr̥mi-, worm, in compound kr̥mi-ja-, „(red dye) produced by worms“ (ja-, produced; see gene-), borrowed into Arabic as qirmiz, kermes: CRIMSON, KERMES'.\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I 523\",\"stance\":\"supports\",\"note\":\"'Ai. kr̥mi- „Wurm, Made“'.\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt s.v. kermes\",\"stance\":\"supports\",\"note\":\"'Arab. qirmiz, ult. fr. OI. kr̥mi-ja-, produced by a worm'.\"},\n  {\"src\":\"IEC\",\"where\":\"s.v. qʷrmis\",\"stance\":\"supports\",\"note\":\"'Skt. kr̥mih, m. id.'.\"}\n ]})\nN.append({\"id\":11,\"lang\":\"Persian\",\"words\":\"qermez\",\"verdict\":\"plausible\",\n \"derivation\":\"NP qermez 'red, crimson' is written with Arabic q and z and is a loan back from Arabic qirmiz 'kermes, crimson'. Arabic took that word from an Iranian form, MP/early NP *kirmist / kirmiz 'worm(-dye)', from *kŕ̥mi- 'worm' plus a suffix (Wiktionary; cf. Armenian karmir, MP karmīr 'red'). So it is an Arabic-mediated round trip of the Iranian worm word. Mo'in (Borhan footnote, citing Jaba; vajehyab tag [سنس.]) and Klein give the older view that it comes straight from Skt. kṛmija. The ultimate root is right. The direct Sanskrit-to-Persian arrow is not supported by modern sources, which route the word through Iranian and Arabic.\",\n \"derivation_fa\":\"«قرمز» با «ق» و «ز» نوشته می‌شود و وام‌واژه‌ای از عربی قِرْمِز است. عربی آن را از صورتی ایرانی مانند *kirmist یا *kirmiz «رنگِ کرمی» گرفته است، که از *kŕ̥mi- «کرم» با پسوند ساخته شده است (سنجیده با ارمنی karmir و پهلوی karmīr «سرخ»). پس «قرمز» واژه‌ای است که از فارسی به عربی رفته و دوباره معرّب به فارسی بازگشته است. معین (به پیروی از ژابا) و کلاین آن را مستقیماً از سنسکریت kṛmija می‌دانند و نورایی هم همین را آورده است. ریشهٔ نهایی درست است، ولی راه مستقیم سنسکریت به فارسی را پژوهش امروزی تأیید نمی‌کند.\",\n \"sources\":[W+\"قرمز\",\"https://vajehyab.com/moein/قرمز\",W+\"crimson\"],\n \"ref_check\":[{\"ref\":\"MON:2663\",\"status\":\"partial\",\"note\":\"vajehyab Mo'in: 'قرمز (قِ مِ) [ سنس . ] (ص .) سرخ ، یکی از رنگ های سه گانة اصلی'. Mo'in tags it Sanskrit, which agrees with Nourai; modern sources go via Arabic.\"}],\n \"consulted\":[\n  {\"src\":\"BQT\",\"where\":\"p. 1527 fn. 1 (ocr/BQT/1527.vision.txt)\",\"stance\":\"partial\",\"note\":\"'قرمز «المعجم ...» ازسانسکریت «ژابا ۳۰۹» و از عربی وارد فرانسوی شده kermès'.\"},\n  {\"src\":\"ARY\",\"where\":\"pdf page 402 (l.11980)\",\"stance\":\"supports\",\"note\":\"'واژهٔ «قرمز» نیز از همین واجریشه است' (same root as کرم), with English crimson etc. from the Sanskrit or Iranian root.\"},\n  {\"src\":\"SOD\",\"where\":\"no. 4834 krm'yr\",\"stance\":\"partial\",\"note\":\"Sogd. krm'yr 'red' '©Pahl. karmir; Arm. karmir'. This shows the Iranian red-dye derivative of *kŕ̥mi-.\"},\n  {\"src\":\"KLN\",\"where\":\"s.v. crimson, kermes\",\"stance\":\"partial\",\"note\":\"'Arab. qirmiz, ult. fr. OI. kr̥mi-ja-'.\"}\n ]})\nN.append({\"id\":12,\"lang\":\"Sogdian\",\"words\":\"kyrm\",\"verdict\":\"confirmed\",\n \"derivation\":\"Sogdian kyrm- /kirm/ 'snake, worm' (Buddhist, Manichaean and Christian texts; plural qyrmyšt) continues Proto-Iranian *kŕ̥miš. Gharib compares Skt. kṛmi. The word and gloss are right. It is a cognate of the Sanskrit word inherited through Iranian, not a descendant of it, so the arrow should be read as 'cognate'.\",\n \"derivation_fa\":\"سغدی kyrm- (خوانش kirm) «مار، کرم» در متن‌های بودایی و مانوی و مسیحی آمده (جمع qyrmyšt) و بازماندهٔ ایرانی آغازین *kŕ̥miš است. قریب آن را با سنسکریت kṛmi سنجیده است. واژه و معنا درست است. تنها باید دانست که این واژه هم‌ریشهٔ سنسکریت است و از راه ایرانی به ارث رسیده، نه اینکه از سنسکریت آمده باشد.\",\n \"sources\":[KWRMIS],\n \"ref_check\":[{\"ref\":\"SOD:203\",\"status\":\"supports\",\"note\":\"SOD.txt l.41490ff. entry 5112: 'kyrm- B, M, S ... kirm, kirm (qyrm) <Skt. kr̥mi ... pl. qyrmyst / snake, worm / GMS 140, 512; TSP ...'.\"}],\n \"consulted\":[\n  {\"src\":\"SOD\",\"where\":\"l.6187 (Persian index)\",\"stance\":\"supports\",\"note\":\"'/kirm/ kyrm- snake Pers. کرم (worm)'.\"},\n  {\"src\":\"NYB\",\"where\":\"s.v. kirm\",\"stance\":\"supports\",\"note\":\"'Skr kr̥mi- snake ... MPrth krm comet'. This gives the 'snake/dragon' sense in Iranian.\"},\n  {\"src\":\"HENNING_selected_papers\",\"where\":\"not searched\",\"stance\":\"silent\",\"note\":\"not needed: Gharib cites the primary texts.\"}\n ]})\nN.append({\"id\":13,\"lang\":\"Arabic\",\"words\":\"qermez\",\"verdict\":\"plausible\",\n \"derivation\":\"Arabic qirmiz 'kermes insect; crimson dye' (attested from the 8th c.) is a loan from an Iranian form, Persian *kirmist / *kirmiz 'worm-dye' < *kŕ̥mi- 'worm'. Wiktionary and the 'carmine' entry follow this. Klein and Watkins (AHD) derive it directly from Skt. kṛmi-ja-. Either way it goes back to the Indo-Iranian worm word. The chart's parent is ambiguous. The extracted JSON makes it a child of Sogdian kyrm (#12), but the printed page draws it from the Sanskrit box (#10). This is an extraction error and the parent should be 10. Modern sources favour an Iranian (Persian) source over direct Sanskrit.\",\n \"derivation_fa\":\"عربی قِرْمِز «حشرهٔ قرمزدانه، رنگ سرخ» از سدهٔ دوم هجری گواهی دارد و وام‌واژه‌ای ایرانی است، از صورتی مانند *kirmist یا *kirmiz «رنگِ کرمی» از *kŕ̥mi- «کرم». کلاین و واتکینز آن را مستقیماً از سنسکریت kṛmi-ja- می‌دانند، ولی ویکی‌واژه و پژوهش تازه‌تر منبع ایرانی را ترجیح می‌دهند. در نمودار چاپی این گره از سنسکریت (#10) منشعب شده، ولی در داده‌های استخراج‌شده زیر سغدی (#12) آمده است. این خطای خوانش داده است و باید اصلاح شود.\",\n \"sources\":[W+\"قرمز\",W+\"carmine\",W+\"crimson\"],\n \"ref_check\":[{\"ref\":\"BQT:1527\",\"status\":\"partial\",\"note\":\"BQT p. 1527 (read from image, ocr/BQT/1527.vision.txt): 'قرمز - بکسر اول ... چیزی است که بدان چیزها رنگ کنند ... جانوری است کوچك ... وبعربی دودالصباغین خوانند'; fn. 1: 'ازسانسکریت «ژابا ۳۰۹» و از عربی وارد فرانسوی شده kermès'. This supports the Sanskrit-ultimate origin and the Arabic → French route, but names no Sogdian link.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt s.v. kermes; KLN_1971 l.59986 s.v. crimson\",\"stance\":\"supports\",\"note\":\"'F. kermès, fr. Arab. qirmiz, ult. fr. OI. kr̥mi-ja-, produced by a worm'; 'crimson ... Sp. cremesín, fr. Arab. qirmiz, ult. fr. OI.'.\"},\n  {\"src\":\"AHD\",\"where\":\"s.v. kʷrmi-\",\"stance\":\"supports\",\"note\":\"'kr̥mi-ja- ... borrowed into Arabic as qirmiz, kermes'.\"},\n  {\"src\":\"FVQ\",\"where\":\"FVQ_pages.txt\",\"stance\":\"silent\",\"note\":\"qirmiz is not a Qur'anic word; no entry in Jeffery.\"},\n  {\"src\":\"LKT\",\"where\":\"LKT.txt\",\"stance\":\"silent\",\"note\":\"not located by grep in the OCR (spelling variants qirmiz/kirmiz tried).\"}\n ]})\nN.append({\"id\":14,\"lang\":\"English\",\"words\":\"kermes, carmine, crimson\",\"verdict\":\"confirmed\",\n \"derivation\":\"kermes (c. 1600) comes from French kermès, from Arabic qirmiz. crimson (late ME cremesyn) comes from Old Spanish cremesín / Medieval Latin cremesinus, from Arabic qirmizī 'kermes-red'. carmine comes from French carmin, from Medieval Latin carminium, a blend of Arabic qirmiz with Latin minium 'red lead'. All three are doublets going back through Arabic to the Indo-Iranian *kŕ̥mi- 'worm'.\",\n \"derivation_fa\":\"انگلیسی kermes از فرانسوی kermès و آن از عربی قرمز آمده است. crimson از اسپانیایی کهن cremesín و لاتینی میانه cremesinus، از عربی قرمزی است. carmine از فرانسوی carmin و لاتینی میانه carminium است، آمیزه‌ای از عربی قرمز و لاتینی minium «سرنج». هر سه هم‌زادند و از راه عربی به واژهٔ هندوایرانی *kŕ̥mi- «کرم» می‌رسند. ادعای نورایی درست است.\",\n \"sources\":[W+\"kermes\",W+\"crimson\",W+\"carmine\"],\n \"ref_check\":[{\"ref\":\"AHD:205,303\",\"status\":\"supports\",\"note\":\"The 1976 page numbers cannot be checked; Watkins 1985 s.v. kʷrmi- gives '(CRIMSON), KERMES' and the index has 'CRIMSON kʷrmi-', 'KERMES kʷrmi-'.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.39964 carmine; l.59986 crimson; KLN_1966 kermes\",\"stance\":\"supports\",\"note\":\"'carmine ... F. carmin, fr. ML. carminium, a blend of Arab. qirmiz, worm and L. minium'; 'crimson ... Sp. cremesín, fr. Arab. qirmiz'.\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt l.3626 (s.v. cochineal)\",\"stance\":\"partial\",\"note\":\"mentions 'kermes' only in passing; no separate etymology found in the OCR.\"}\n ]})\nN.append({\"id\":15,\"lang\":\"Indo-European\",\"words\":\"Wropal\",\"verdict\":\"plausible\",\n \"derivation\":\"'Wropal' is not a standard PIE reconstruction. It is Nourai's (or Mann's) back-projection of Greek rhópalon 'club', which Homeric metrics and Aeolic spellings show had initial ϝρ- (*wr-). Pokorny 1156 puts rhópalon 'Wurfstab, Keule' and rhóptron 'club' under the extension *werp- / *wrep- 'to turn, wind' (also rhépō 'to incline'). So a *wrop-alo- built on wer-3 is defensible. Wiktionary (after Beekes) says only 'traditionally derived from rhépō, but perhaps not related', so the link is not certain. Mann's entry could not be found in the local OCR.\",\n \"derivation_fa\":\"«Wropal» ریشهٔ پذیرفته‌شده‌ای در هندواروپایی نیست. نورایی یا مان آن را از روی یونانی rhópalon «چماق» که در آغاز ϝρ- (*wr-) داشته بازسازی کرده‌اند. پوکورنی (ص ۱۱۵۶) rhópalon و rhóptron را زیر *werp- «گرداندن، پیچیدن» آورده است. ویکی‌واژه به پیروی از بیکس می‌گوید: «به‌طور سنتی از rhépō، ولی شاید بی‌پیوند». پس این پیوند با احتیاط پذیرفتنی است.\",\n \"sources\":[W+\"ῥόπαλον\"],\n \"ref_check\":[{\"ref\":\"IEC:1596\",\"status\":\"not_found\",\"note\":\"IEC.txt leaves 813-815 (≈ pp. 1594-1600: uper, ursis, uruos ...) and full-file grep for 'ropal|rhop|wrop|uropal|club' found no Wropal/rhópalon entry; the OCR may have missed it.\"}],\n \"consulted\":[\n  {\"src\":\"POK\",\"where\":\"p. 1156 (POK_full.txt l.91713ff.)\",\"stance\":\"supports\",\"note\":\"'uer-3. G. uer-p-, ur-ep- ... to turn, wind ... gr. ... rhópalon „Wurfstab, cudgel, club“, rhóptron „club, mace ...“'.\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I 276f. (cited by Pokorny 'WP. I 276 f.')\",\"stance\":\"supports\",\"note\":\"the same Greek material is cited at WP I 276f.; the club word was not separately found in the WLD OCR (grep 'Keule' gives other roots).\"}\n ]})\nN.append({\"id\":16,\"lang\":\"Persian\",\"words\":\"kŭpâl\",\"verdict\":\"disputed\",\n \"derivation\":\"NP kopāl / gopāl 'iron mace, club' (Ferdowsi) belongs to an areal word family: Kurdish gopal/kopal 'shepherd's staff', Armenian kopal, Georgian ḳombali/ḳobali, Laz ḳoṗali, Ossetic k'obala, Pontic Greek kopáli, Turkish gobal/kopal. Wiktionary calls its origin uncertain. The suggestions are a native formation from kōb- 'to beat' (kōftan) + -āl (as in čangāl), a loan from Greek kópanon 'pestle', or a Kartvelian *ḳaṗ-. Mo'in's footnote to Borhan gives only the Kurdish parallel. It cannot come from the ancestor of Greek rhópalon. Initial ϝρ-/wr- does not give Persian k-/g-, and an inherited Iranian *wrāp- would give NP *ra- or *gura-. Nourai's link rests only on the formal resemblance -pal.\",\n \"derivation_fa\":\"«کوپال» یا «گوپال» به معنی «گرز آهنین» (فردوسی) جزو گروهی از واژه‌های منطقه‌ای است: کردی gopal/kopal «چوبدست چوپان»، ارمنی kopal، گرجی ḳombali، آسی k'obala، یونانی پونتی kopáli و ترکی gobal. ویکی‌واژه ریشهٔ آن را نامعلوم می‌داند و احتمال می‌دهد از «کوب» (کوفتن) با پسوند -āl (مانند «چنگال») یا از یونانی kópanon «دسته‌هاون» باشد. معین در حاشیهٔ برهان تنها صورت کردی را آورده است. واج آغازین wr- در rhópalon هرگز در فارسی به ک یا گ بدل نمی‌شود. پس پیوند «کوپال» با rhopalon را پژوهش امروزی نمی‌پذیرد و این تنها شباهت ظاهری است.\",\n \"sources\":[W+\"گوپال\",\"https://vajehyab.com/moein/کوپال\"],\n \"ref_check\":[\n  {\"ref\":\"MON:3109\",\"status\":\"partial\",\"note\":\"vajehyab Mo'in: 'کوپال (اِ.) عمود، گرز آهنین'. The meaning is confirmed; no etymology and no Greek link.\"},\n  {\"src_note\":\"\",\"ref\":\"IEC:1596\",\"status\":\"not_found\",\"note\":\"no Persian kopāl/gopāl found in IEC.txt (grep 'k[uū]p[aā]l|gopal|kopal').\"}],\n \"consulted\":[\n  {\"src\":\"BQT\",\"where\":\"vol. 3 s.v. کوپال (BQT_v3_pages.txt l.37659-37679)\",\"stance\":\"contradicts\",\"note\":\"'کوپال ... عمود و گرز آهنین را گویند'; footnote: 'کوپال کردی kopāl (عصا، چوبدست چوپان) ... «ژابا ص ۳۵۵»' with Ferdowsi's verses. Mo'in gives a Kurdish parallel and no IE etymology.\"},\n  {\"src\":\"MON\",\"where\":\"2-vol abridgement MON_part2.txt l.27644\",\"stance\":\"partial\",\"note\":\"'کوپال: (قد.) [= گوپال] (اِ.) گرز آهنین'.\"},\n  {\"src\":\"HRN\",\"where\":\"HRN.txt\",\"stance\":\"silent\",\"note\":\"grep 'kūpāl|gūpāl|kopal|gopal' finds nothing.\"},\n  {\"src\":\"HUB\",\"where\":\"HUB.txt\",\"stance\":\"silent\",\"note\":\"same grep, nothing.\"}\n ]})\nN.append({\"id\":17,\"lang\":\"Greek\",\"words\":\"rhopalon\",\"verdict\":\"plausible\",\n \"derivation\":\"Ancient Greek rhópalon 'club, cudgel' is old (Homeric). Its initial ϝ- is shown by the metre and by the related rhóptron. Pokorny 1156 sets it under *werp- / *wrep- 'to turn, wind' beside rhépō 'to incline, sink (of a scale)'. Beekes, followed by Wiktionary, says 'traditionally derived from rhépō, but perhaps not related', so the IE etymology is possible but not secure. The word and gloss are correct.\",\n \"derivation_fa\":\"یونانی باستان rhópalon «چماق، گرز» واژه‌ای کهن (هومری) است که در آغاز ϝ- داشته است. پوکورنی (ص ۱۱۵۶) آن را زیر *werp- «گرداندن، پیچیدن» در کنار rhépō «خم شدن، سنگینی کردنِ کفهٔ ترازو» آورده است. بیکس و ویکی‌واژه این پیوند را سنتی ولی نامطمئن می‌دانند. پس واژه و معنا درست است و ریشه‌شناسی آن پذیرفتنی ولی قطعی نیست.\",\n \"sources\":[W+\"ῥόπαλον\"],\n \"ref_check\":[\n  {\"ref\":\"POK:1156\",\"status\":\"supports\",\"note\":\"POK_full.txt l.91721ff. 'Gr. ... rhópalon „Wurfstab, cudgel, club“, rhóptron „club, mace, joint, Türklopfer ...“ ... Page(s):1156'.\"},\n  {\"ref\":\"IEC:1596\",\"status\":\"not_found\",\"note\":\"see node 15.\"},\n  {\"ref\":\"DEW:435\",\"status\":\"not_checked\",\"note\":\"DEW has no local file or online pointer in refs_online.json.\"}],\n \"consulted\":[\n  {\"src\":\"WLD\",\"where\":\"WP I 276f. (via Pokorny)\",\"stance\":\"supports\",\"note\":\"Pokorny's references 'WP. I 276 f.' for the uer-p- material including rhópalon.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 wer-3 VIII\",\"stance\":\"partial\",\"note\":\"'VIII. Root *werp-, to turn, wind ... Zero-grade form *wrp- in Greek rhaptein, to sew'. rhopalon is not listed (no English derivative).\"}\n ]})\nfor n in N:\n    for rc in n[\"ref_check\"]:\n        rc.pop(\"src_note\",None)\nout={\"pdf_page\":545,\"book_page\":515,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":[entry]}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-545.json\",\"w\"),ensure_ascii=False,indent=1)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-545.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-545.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 545"
}
```


### [2026-10-17T00:10:07.021Z] TOOL RESULT

```
nodes verified: 17/17
node verdicts: {'confirmed': 7, 'plausible': 7, 'transcription_suspect': 1, 'disputed': 2}
root verdicts: {'plausible': 1}
ref checks: {'supports': 13, 'not_checked': 3, 'partial': 5, 'not_found': 3}
books consulted: {'supports': 33, 'silent': 9, 'partial': 11, 'contradicts': 3} | by book: {'KLN': 10, 'WLD': 6, 'AHD': 4, 'BRT': 4, 'HUB': 3, 'BQT': 3, 'ARY': 3, 'SKT': 3, 'HRN': 3, 'NYB': 3, 'POK': 2, 'MON': 2, 'IEC': 2, 'SOD': 2, 'LAT': 1, 'SYN': 1, 'PHD': 1, 'HENNING_selected_papers': 1, 'FVQ': 1, 'LKT': 1}
```


## [2026-10-17T00:10:16.692Z] TOOL CALL #89: SubagentHandback

```json
{
 "message": "I verified PDF page 545 (book p. 515, root \"Wer 2 … Wrei\", part 2) and wrote `/home/sfmqrb/git/rishe-private/data/verification/page-545.json`. It is valid JSON and `verify_check.py 545` shows 0 PROBLEM lines; all 17 nodes are covered.\n\n**Verdict counts**\n- Root: plausible. PIE *wer- \"turn, bend\" and its extensions are right (Pokorny 1152–1158, Watkins wer-3). \"Kwermi\" (*kʷŕ̥mis) is a different root: Pokorny 649 and Watkins call it only a \"rhyme word\", so nodes 8–14 hang under the wrong root.\n- Nodes: 7 confirmed, 7 plausible, 2 disputed, 1 transcription_suspect.\n\n**Disputed and transcription items**\n- **#7 English list, \"vermouth\": disputed.** It comes from German Wermut \"wormwood\" through French, not from Latin (Klein, Wiktionary). The other words on the list are fine.\n- **#16 Persian kopāl/gopāl \"mace\": disputed.** It belongs to a regional word family (Kurdish gopal, Armenian kopal, Georgian ḳombali, Turkish gobal) of uncertain origin. Mo'in's Borhan footnote gives only the Kurdish word. It cannot come from the ancestor of Greek rhopalon, because initial *wr- never becomes Persian k-/g-.\n- **#4 Latin \"vetere\": transcription_suspect, error in the book.** The printed page has \"vetere\"; the correct form is \"vertere\". The extraction copied it faithfully.\n\n**Extraction error to fix**\n- **page-545.json, #13 Arabic qermez:** the parent should be 10 (Sanskrit krmi), not 12 (Sogdian). On the printed page, Sogdian and Arabic both branch from the trunk that comes down from the Sanskrit box.\n\n**Other points**\n- #11 and #13 (Persian and Arabic qermez) are plausible only. Modern sources (Wiktionary) take Arabic qirmiz from an Iranian *kirmist/*kirmiz, and Persian qermez is a loan back from Arabic. Mo'in, Klein and Nourai take it straight from Sanskrit kṛmija.\n- I could not find the Mann entry Nourai cites as IEC:1596 for \"Wropal\" in the local OCR, and there is no copy of DEW at all.\n\n**Files saved**\n- `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2273.vision.txt` and `1527.vision.txt`: my readings of the Borhan page images.\n- `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/545.png`: the page render used for the checks."
}
```


### [2026-10-17T00:10:16.982Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
