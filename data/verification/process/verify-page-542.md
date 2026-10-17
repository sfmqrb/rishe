# Verification process log — verify-page-542


## [2026-10-17T00:00:15.279Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 542 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-542.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-542.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-542.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 542` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.331Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.305Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.359Z] TOOL RESULT

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


## [2026-10-17T00:00:18.823Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-542.txt"
}
```


### [2026-10-17T00:00:18.845Z] TOOL RESULT

```
1	=== PDF page 542 (book page 512) ===
2	--- entry 0 ---
3	ROOT Welâ -> redirect to Wel 2
4	--- entry 1 ---
5	ROOT [Indo-European] Wem : to spit, vomit  (refs POK:1146)
6	#1 (parent #0) [Avestan] refs=POK:1146; KLN:1722 | vam : to spit, vomit
7	  #2 (parent #1) [Pahlavi] refs=POK:1146; HRN:296 | vâmîtan : to vomit ; vâtâk : saliva
8	#3 (parent #0) [Latin] refs=AHD | vomere : to vomit
9	  #4 (parent #3) [English] refs=None | vomit
10	--- entry 2 ---
11	ROOT [Indo-European] Wen : to wish, desire  (refs POK:1146; OEW:434)  PART 1
12	#1 (parent #0) [Avestan] refs=POK:1146; KLN:1697 | vanaiti : he wishes ; vantar : victorious ; vayeiti 1 : he hunts ; vîtar 2 : pursuer ; vyâna 2 : pursued ; vâti : persecution
13	  #2 (parent #1) [Pahlavi] refs=POK:1146 | vânîtan : to be victorious
14	#3 (parent #0) [Avestan] refs=WLD1:259 | vanâ : woods, tree (hunting place) | NOTE: OEW:434 explains that Indian hunters used to trade animal skins under "banyan" trees.
15	  #4 (parent #3) [Pahlavi] refs=WLD1:259 | van : tree
16	    #5 (parent #4) [Persian] refs=WLD1:259; AEF:287 | van «وَن» : tree ; bon 2 (ban) «بُن ۲» : tree, tree stump | extra: سروبن ، گلبن ، خاربن ، نارَوَن ، ناروان
17	  #6 (parent #3) [Avestan] refs=AEF:291 | vana-vaxša : grown in the woods, wild pansy, violet ☞Aueg
18	    #7 (parent #6) [Pahlavi] refs=AEF:291 | vana-vašak : pansy, violet | NOTE: HUB:33 doubts this derivation
19	      #8 (parent #7) [Persian] refs=AEF:291 | banafšeh «بنفشه» : pansy ; banafsh «بنفش» : violet, blue
20	#9 (parent #0) [Avestan / Old Persian] refs=KNT:260 | van : overpower, win
21	#10 (parent #0) [Sanskrit] refs=OEW:434; AHD:1549; WLD1:259 | vanîja : Hindu trader of animal skins (obtained from hunting) ; vana : forest, trees (place of hunting or trading animal skins)
22	  #11 (parent #10) [English] refs=AHD:104 | banian : Hindu trader ; banyan : a large type of tree in tropical India
23	
```


## [2026-10-17T00:00:19.297Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-542.json"
}
```


### [2026-10-17T00:00:19.492Z] TOOL RESULT

```
1	{
2	  "pdf_page": 542,
3	  "book_page": 512,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Welâ",
8	        "redirect": "Wel 2"
9	      },
10	      "nodes": []
11	    },
12	    {
13	      "root": {
14	        "name": "Wem",
15	        "lang": "Indo-European",
16	        "refs": "POK:1146",
17	        "gloss": "to spit, vomit"
18	      },
19	      "nodes": [
20	        {
21	          "id": 1,
22	          "parent": 0,
23	          "lang": "Avestan",
24	          "refs": "POK:1146; KLN:1722",
25	          "words": [
26	            {"translit": "vam", "gloss": "to spit, vomit", "script": null}
27	          ],
28	          "note": null,
29	          "quote": null
30	        },
31	        {
32	          "id": 2,
33	          "parent": 1,
34	          "lang": "Pahlavi",
35	          "refs": "POK:1146; HRN:296",
36	          "words": [
37	            {"translit": "vâmîtan", "gloss": "to vomit", "script": null},
38	            {"translit": "vâtâk", "gloss": "saliva", "script": null}
39	          ],
40	          "note": null,
41	          "quote": null
42	        },
43	        {
44	          "id": 3,
45	          "parent": 0,
46	          "lang": "Latin",
47	          "refs": "AHD",
48	          "words": [
49	            {"translit": "vomere", "gloss": "to vomit", "script": null}
50	          ],
51	          "note": null,
52	          "quote": null
53	        },
54	        {
55	          "id": 4,
56	          "parent": 3,
57	          "lang": "English",
58	          "refs": null,
59	          "words": [
60	            {"translit": "vomit", "gloss": null, "script": null}
61	          ],
62	          "note": null,
63	          "quote": null
64	        }
65	      ]
66	    },
67	    {
68	      "root": {
69	        "name": "Wen",
70	        "lang": "Indo-European",
71	        "refs": "POK:1146; OEW:434",
72	        "gloss": "to wish, desire",
73	        "note": "This root has derivative related to sexual or hunting desires"
74	      },
75	      "part": 1,
76	      "nodes": [
77	        {
78	          "id": 1,
79	          "parent": 0,
80	          "lang": "Avestan",
81	          "refs": "POK:1146; KLN:1697",
82	          "words": [
83	            {"translit": "vanaiti", "gloss": "he wishes", "script": null},
84	            {"translit": "vantar", "gloss": "victorious", "script": null},
85	            {"translit": "vayeiti 1", "gloss": "he hunts", "script": null},
86	            {"translit": "vîtar 2", "gloss": "pursuer", "script": null},
87	            {"translit": "vyâna 2", "gloss": "pursued", "script": null},
88	            {"translit": "vâti", "gloss": "persecution", "script": null}
89	          ],
90	          "note": null,
91	          "quote": null
92	        },
93	        {
94	          "id": 2,
95	          "parent": 1,
96	          "lang": "Pahlavi",
97	          "refs": "POK:1146",
98	          "words": [
99	            {"translit": "vânîtan", "gloss": "to be victorious", "script": null}
100	          ],
101	          "note": null,
102	          "quote": null
103	        },
104	        {
105	          "id": 3,
106	          "parent": 0,
107	          "lang": "Avestan",
108	          "refs": "WLD1:259",
109	          "words": [
110	            {"translit": "vanâ", "gloss": "woods, tree (hunting place)", "script": null}
111	          ],
112	          "note": "OEW:434 explains that Indian hunters used to trade animal skins under \"banyan\" trees.",
113	          "quote": null
114	        },
115	        {
116	          "id": 4,
117	          "parent": 3,
118	          "lang": "Pahlavi",
119	          "refs": "WLD1:259",
120	          "words": [
121	            {"translit": "van", "gloss": "tree", "script": null}
122	          ],
123	          "note": null,
124	          "quote": null
125	        },
126	        {
127	          "id": 5,
128	          "parent": 4,
129	          "lang": "Persian",
130	          "refs": "WLD1:259; AEF:287",
131	          "words": [
132	            {"translit": "van", "gloss": "tree", "script": "وَن"},
133	            {"translit": "bon 2 (ban)", "gloss": "tree, tree stump", "script": "بُن ۲"}
134	          ],
135	          "script_extra": "سروبن ، گلبن ، خاربن ، نارَوَن ، ناروان",
136	          "note": null,
137	          "quote": {"text": "یکی گفت زیشان که ای سرو بن - نگر تا نداند کسی این سخن", "poet": "Ferdowsî"}
138	        },
139	        {
140	          "id": 6,
141	          "parent": 3,
142	          "lang": "Avestan",
143	          "refs": "AEF:291",
144	          "words": [
145	            {"translit": "vana-vaxša", "gloss": "grown in the woods, wild pansy, violet", "script": null, "see": ["Aueg"]}
146	          ],
147	          "note": null,
148	          "quote": null
149	        },
150	        {
151	          "id": 7,
152	          "parent": 6,
153	          "lang": "Pahlavi",
154	          "refs": "AEF:291",
155	          "words": [
156	            {"translit": "vana-vašak", "gloss": "pansy, violet", "script": null}
157	          ],
158	          "note": "HUB:33 doubts this derivation",
159	          "quote": null
160	        },
161	        {
162	          "id": 8,
163	          "parent": 7,
164	          "lang": "Persian",
165	          "refs": "AEF:291",
166	          "words": [
167	            {"translit": "banafšeh", "gloss": "pansy", "script": "بنفشه"},
168	            {"translit": "banafsh", "gloss": "violet, blue", "script": "بنفش"}
169	          ],
170	          "note": null,
171	          "quote": {"text": "هر روز که روی لاله شبنم گیرد - بالای بنفشه در چمن خم گیرد", "poet": "Khayyâm"}
172	        },
173	        {
174	          "id": 9,
175	          "parent": 0,
176	          "lang": "Avestan / Old Persian",
177	          "refs": "KNT:260",
178	          "words": [
179	            {"translit": "van", "gloss": "overpower, win", "script": null}
180	          ],
181	          "note": null,
182	          "quote": null
183	        },
184	        {
185	          "id": 10,
186	          "parent": 0,
187	          "lang": "Sanskrit",
188	          "refs": "OEW:434; AHD:1549; WLD1:259",
189	          "words": [
190	            {"translit": "vanîja", "gloss": "Hindu trader of animal skins (obtained from hunting)", "script": null},
191	            {"translit": "vana", "gloss": "forest, trees (place of hunting or trading animal skins)", "script": null}
192	          ],
193	          "note": null,
194	          "quote": null
195	        },
196	        {
197	          "id": 11,
198	          "parent": 10,
199	          "lang": "English",
200	          "refs": "AHD:104",
201	          "words": [
202	            {"translit": "banian", "gloss": "Hindu trader", "script": null},
203	            {"translit": "banyan", "gloss": "a large type of tree in tropical India", "script": null}
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


## [2026-10-17T00:00:25.824Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -120; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','AHD','WLD','WLD1','OEW','AEF','KNT','HUB','BRT','PHD','NYB','BQT','MON','ARY','CHEUNG','SKT','HJB','AID','IEC','SYN','WEB','FSD']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-10-17T00:00:26.194Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
WLD1 null
OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC n
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AID.txt", "page_offset
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
```


## [2026-10-17T00:00:29.206Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls data/verification/ | tail -20; sed -n 1,200p tools/verify_check.py | head -150"
}
```


### [2026-10-17T00:00:29.694Z] TOOL RESULT

```
page-82.json
page-83.json
page-84.json
page-85.json
page-86.json
page-87.json
page-88.json
page-89.json
page-90.json
page-91.json
page-92.json
page-93.json
page-94.json
page-95.json
page-96.json
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


## [2026-10-17T00:00:33.340Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-538.json'));e=d['entries'][1] if len(d['entries'])>1 else d['entries'][0]\nprint(d['verified_by'],d['verified_on'])\nx=dict(e);n=x.pop('nodes');print(json.dumps(x,ensure_ascii=False,indent=1)[:2500]);print(json.dumps(n[0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-10-17T00:00:33.728Z] TOOL RESULT

```
claude-opus-5.5 2026-10-16
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
   "note": "'uekᵘ- „sprechen“. Ai. vákti, vivakti „sagt, redet, spricht“ ... av. vac- „sprechen“, uxta- ... ai. vacas- n. = av. vacah- (= gr. épos) „Rede, Wort“ ... ai. vāc-,
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


## [2026-10-17T00:00:40.434Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Root / lemma: u̯em\\|Root / lemma: uem\\|Root / lemma: u̯en-\\|Root / lemma: uen-\\|Root / lemma: u̯en(\" POK_full.txt | head; grep -n \"Page(s): 1146\\|Page(s) 1146\" POK_full.txt | head"
}
```


### [2026-10-17T00:00:40.803Z] TOOL RESULT

```
90563:vemalaryovc\\\! > maybe truncated alb. {*vema/a/j y/e//\om'\t\ see Root / lemma: uem-, 
90767:Root / lemma: uem-, uema- 
91008:Root / lemma: uen-2 
91015:Root / lemma: uen- 
91006:Page(s): 1146-1147
```


## [2026-10-17T00:00:42.720Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90767,90800p POK_full.txt; echo ----; sed -n 90990,91080p POK_full.txt"
}
```


### [2026-10-17T00:00:43.104Z] TOOL RESULT

```
Root / lemma: uem-, uema- 

Meaning: to spit, vomit 

Material: Old Indie vami-ti, newer 1/5/775// "ausspeien, vomit', 1/5/7/5- "gespien', vamathu-m. 

"Erbrechen', Avestan 1/5/77- "vomit'; npers. 1/5/5/r "saliva' {*um-to-); 

gr. £fj£U) (for *£fj£-|ji), Aor. £|j£aaai "vomit', £[J£to(; m., £p£aic; f. "Erbrechen' (£|juc; 
"Sumpfschildkrote'?); 

Latin vomo {* uemo) "erbreche', i/o/77//i/s" Erbrechen', vom/ca'u\cer, abscess, boil '; 

Norwegian dial. 1///77/5 "nausea feel', i///77/'5 "nausea cause'. Old Swedish vam/m. " 
disgust, repulsion, loathing '; Old Icelandic 1/5/775 "nausea ', vamr' disgusting person'; 



Lithuanian i/e/77// "vomit', vema/arvomW, v/'mdyt/" erbrechen make', Latvian vemt's\ch 
erbrechen'; 

maybe truncated alb. {*vema/a?j iye//"vomit', older i/e/"overeat, feel nausea ' , a Lithuanian 
loanword 

very dubious is kinship from Gothic Gen. PI. wamme' stain ', gawamms Gen. PI. 
"befleckt, impure, unclean'. Old Icelandic vammn. "fault, error, disability ', Old English 
wammm. n. " stain, disability, wrong; injustice ', Adj. "mad, wicked, evil, bad'. Old Saxon 
warn n. "evil, harm'. Adj. "mad, wicked, evil' ( *uom-no-)\ compare Weisweiler IF 41 , 46. 

References: WP. I 262 f., WH. II 835, Trautmann 350, Frisk 504 f., 508. 
Page(s): 1 1 46 

Root / lemma: uerrS^-1 

----
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

References: WP. I 256 f., WH. II 732, Trautmann 351, Vasmer 1, 183. 

Page(s): 1149 

Root / lemma: u(e)rad-, Uerad- urad- 

Meaning: twig, root, branch 

Material: Gr. pa5T^, -~\koc, "twig, branch, rod' (= Latin radix), pa5apvo(; m., Aeolic 

*Fp65a[jvoq (from opoSapvoc; to erschlieften) "young twig, branch' (about pa5iv6(;, 

pa5aA6(; uer-, ured-'iuxu'); compare pi^a Lesbian ppia5a "roof (*Fp95ja?); 

alb. rranze'root' (Mann Lg. 26, 388; 28, 37); Latin radix, -Tc/st "roof; probably ramus 
"bough, twig, branch' (as *uradmos) and radius' s\.ai\, Speiche, ray bright body, 
Weberschiffchen';
```


## [2026-10-17T00:00:47.318Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90940,90992p POK_full.txt; grep -n \"Speichel\" POK_0*.txt | head"
}
```


### [2026-10-17T00:00:47.743Z] TOOL RESULT

```
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
POK_02.txt:3521:ahd.  rachisön  ,sich  räuspern',  ags.  hraca  m.,  hracu  f.  , Kehle*,  ahd.  rahho , Rachen*,  ags.  hrceca  m.  , das  Räuspern;  Speichel*,  hrcecan  ,sich  räuspern, spucken*,  anord.  hraka  m.  , Speichel';  anord.  skrcekr  m.  , Schrei'  (^skreki-)^ skrcekja,  skrcekta  , schreien*,  skrgk  n.  PI.  ,Lüge*,  skrqkva  , erdichten,  erlügen';
POK_02.txt:3556:Mit  idg.  -t- :  anord.  hrydja  f.  , Spucknapf',  isl.  hrodi  , Speichel',  norw. dial.  ryda,  skryda  f.  , Schleim  im  Halse'.
POK_02.txt:5125:lett.  slienas  f.  PI.  , Speichel'  (^sleinäs),  aksl.  sliny,  serb.  sUne  ,Rotz', russ.  slina  , Speichel';
POK_02.txt:5127:gr.  Xelixa^  , nackte  Schnecke'  (daraus  lat.  llmäx  ds.)  =  russ.  slimdk  m. , Schnecke';  vgl.  apr.  slayx  m.,  lit.  sliekas  m.,  lett.  slieka  f.  ,Regenwurm' und  lett.  sliekas  f.  Fl.  , Speichel';  vielleicht  auch  lit.  seiles,  lett.  seilas  f. PI.  , Speichel'  (aus  ^sleiläs?).
POK_02.txt:6036:mir.  blind,  blinn  ^eines  toten  Mannes  Speichel^  (wohl  '*mld-sno-?);
POK_03.txt:1497:2,  sal'  , schmutziggrau*,  auch  (nach  der  Farbe)  zur  Bezeichnung  des  Salzes (s.  1.  sal-)j  der  Grauweide  und  des  Speichels;  sa.l-uo-,  sälo-,  schmutz- farben';  sal{i)k-  ,Weide*.
POK_03.txt:1500:C.  Lat.  sallva  f.  , Speichel',  daraus  air.  saile,  cymr.  haliw  ds.
POK_03.txt:1710:Ahd.  sihj  ndl.  zeef,  mnd.   seve  n.,  ags.  sife  n.   ,Sieb*,   dazu  ags.  sift^ mnd.  siften^  sichten,  nhd.  (aus   dem  Nd.)  sichten,   und  aisl.  sef  n.  ,jun< (wegen   des   porösen   Stengels);   mnd.   afries.   sever   m.    , Schleim,    Geifer*, ahd.   seivar,   mhd.   seifer  m.    ds.   (mhd.   seifei  m.   , Speichel*   vielleicht germ.  p,  s.  u.);  md.  sife  , sumpfige  Bodenstelle*;  serb.  sipiti  ,rieseln,  feS' regnen* ;
POK_03.txt:3274:speiwan),  sthyütd-  ,gespuckt,  gespien';  av.  sjpäma-  ,Speichel,  Schleim';  gr.
POK_03.txt:3275:TCT'öa)  , spucke*,  fCTvaXov,  mveXov  , Speichel',  tivtI^w  (dissimil.  aus  *mvril^(x))
```


## [2026-10-17T00:00:57.786Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"vamiti\\|vämiti\\|vamati\" POK_0*.txt | head; grep -n \"vanati\\|vanöti\\|vanoti\" POK_0*.txt | head"
}
```


### [2026-10-17T00:00:58.157Z] TOOL RESULT

```
POK_03.txt:5527:Ai.  vdmi-ti,  jünger  vamati  ,ausspeien,   erbrechen',  vänta-    o-espien*    ea mathu-  m.  , Erbrechen',  av.  vam- , erb  rechen';  npers.  vätäk  , Speichel'  (•wH-iA.V
POK_03.txt:5535:Ai.  vdnati,  vanöti  , wünscht,  liebt,  gewinnt,  siegt',  Partiz.  vanita-,  •vätO'f väni-tr-,  vantf-  , Gewinner',  av.  vanaiti,  vanaoiti  , siegt',  mpers.  vanlian  »be- siegen, schlagen';  ai.  Aor. -Präs.  vandti  in  gleicher  Bedeutung;  Kaus.  vand* yati  und  vandyati  (ersteres  nicht  belegt);  als  -sk-  Präs.  ai.  väüchati  ,w\ÜTiSchi', vgl.  väüchä  f.  , Wunsch';  vanas-  n.  ,Lust'  (vgl.  lat.  Venus),  vani-  f.  »Verlangen» Wunsch',  wozu  vamyati  , bettelt',  vanlyaka-  ,Bettler',  vanü-  als  Nomen  agentif  ■ m.  (vgl.  av.  -vanu§  in  Nom.  Pr.);  in  Zusammensetzungen  erscheint  vdnya'\§, ferner  vantä-  als  Nom.  Sg.  m.  (av.  vantar  ^Sieger'),  vanti-  Nom.  Act.  (unbd- legt,  doch  vgl.  av.  -vantay-);  ai.  vdma-  ,link'  und  vämd-  , lieb  (lieh),  lüstern'j
```


## [2026-10-17T00:01:00.593Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5520,5545p POK_03.txt"
}
```


### [2026-10-17T00:01:01.203Z] TOOL RESULT

```
2.  uelg-:  ahd.  welc  ,feucht,  milde,  welk',  mnd.  walcheit  ,macies',  welk ,welk,  dürre',  mengl.  ivelkin  , welken';  mit  anderer  Vokalstellung  ags.  wisse, wlacii  ,lauwarm',  mnd.  wlak  ds.  (mit  anl.  s-  mhd.  swelk  ,welk',  swelken, ahd.  sioelchen  ,welken');  vermutlich  ahd.  icolchan  n.,  wolcha  f.,  r.s.  icolkan n.  y Wolke']
lit.  vilgau,  -yti,  vdlgyti  ,anfeuchten',  vUkSnas  , feucht*,  ablaut.  apr.  welgen n.  jSchnupfen',  lett.  valgums  ,Feuchtigkeit',  v^tgans  und  vatgs  , feucht',  auch lit.  valgis  , Speise',  vdlgau,  -yti  ,essen*  (vom  Begriff  der  flüssigen,  breiigen Nahrung  aus,  vgl.  russ.  volöga  ,flüssige  Nahrung');
slav.   *vhlg^k^   ,feucht'   in   russ.-ksl.   v^lg^k^,   dazu  poln.   tvilgnqc  , feucht
1146  •
werden',  russ.  volgnuth  ds.,  ablaut.  *uölgä  in  aksl.  vlaga  f.    FeuchtVlr  • russ.   volöga    , Flüssigkeit,    Zukost',    dazu   volözith  ,anfeuchten    mit  R  f*  * kochen';  hierher  der  russ.  FIN  Wolga  (==  cech.  FIN  Vlka^  poln.  FIN  TFTWv aus  slav.  *FtZ^a.  ^^'
WP.  I  306,  Trautmann  358,  Vasmer  1,  216  f.,  219.
uei22-,  ueni9-  , speien,  sich  erbrechen'.
Ai.  vdmi-ti,  jünger  vamati  ,ausspeien,   erbrechen',  vänta-    o-espien*    ea mathu-  m.  , Erbrechen',  av.  vam- , erb  rechen';  npers.  vätäk  , Speichel'  (•wH-iA.V
gr.  ifj,£0)  (für  H'(.is-ij,l)j  Aor.  eiiEGaai  , erbrechen',  ^Lsroq  m.,  ^isolc  f.  Rp! brechen'  (e^tvg  ,Sumpfschildkröte'?);
lat.  vomö  (*uemö)  ,erbreche',  vomitus  , Erbrechen',  vomica  , Geschwür Eiterbeule';
norw.  dial.  vimla  , Übelkeit  empfinden',  vimra  ,Übelkeit  verursacbon* aschwed.  vami  m.  ,Ekel';  aisl.  väma  ,Übelkeit',  vämr  , ekelhafte  Person*»
lit.  vemti  ,erbrechen',  vemalat  ,Erbrochenes',  vimdyti  ,erbrechen  maehea' lett.  vemt  ,sich  erbrechen';  •    ■  r^
sehr  zweifelhaft  ist  Verwandtschaft  von  got.  Gen.  PI.  ivammS  ,Fleck* gawamms  Gen.  PI.  , befleckt,  unrein',  aisl.  vamm  n.  , Fehler,  Gebrechen* ags.  wamm  m.  n.  , Fleck,  Gebrechen,  Unrecht',  Adj.  ,böse,  schlecht',  as.  toam n.  , Übles,  Böses',  Adj.  ,böse'  (*uoTn-no-)]  vgl.  Weisweiler  IF  41,  46.
WP.  I  262  f.,  WH.  II  835,  Trautmann  350,  Frisk  504  f.,  508.  "
1.  uen-j  Ueno-  ursprünglich  , streben',  woraus  ,wünschen,  lieben,  befriedigt sein'  und  , erarbeiten,  Mühe  haben',  perfektiv  »erreichen,  gewinnen, siegen';  uenos-  ,Verlangen'.  -    -w..
Ai.  vdnati,  vanöti  , wünscht,  liebt,  gewinnt,  siegt',  Partiz.  vanita-,  •vätO'f väni-tr-,  vantf-  , Gewinner',  av.  vanaiti,  vanaoiti  , siegt',  mpers.  vanlian  »be- siegen, schlagen';  ai.  Aor. -Präs.  vandti  in  gleicher  Bedeutung;  Kaus.  vand* yati  und  vandyati  (ersteres  nicht  belegt);  als  -sk-  Präs.  ai.  väüchati  ,w\ÜTiSchi', vgl.  väüchä  f.  , Wunsch';  vanas-  n.  ,Lust'  (vgl.  lat.  Venus),  vani-  f.  »Verlangen» Wunsch',  wozu  vamyati  , bettelt',  vanlyaka-  ,Bettler',  vanü-  als  Nomen  agentif  ■ m.  (vgl.  av.  -vanu§  in  Nom.  Pr.);  in  Zusammensetzungen  erscheint  vdnya'\§, ferner  vantä-  als  Nom.  Sg.  m.  (av.  vantar  ^Sieger'),  vanti-  Nom.  Act.  (unbd- legt,  doch  vgl.  av.  -vantay-);  ai.  vdma-  ,link'  und  vämd-  , lieb  (lieh),  lüstern'j
venet.  VN  Venetl  von  *uenetos  , geliebt';  vgl.  die  Venostes  in  ddO Alpen,  die  Venetulani  in  Latium  (Krähe  IF.  58^  137);  lat.-germ.  Ven4iU (Plin.);  ahd.  Winida  ,Wende^  weist  auf  vorgerm.  *Veneto-,  dagegen  Ut« germ.  Venedi  (Tacitus),  ags.   Winedas  ,Wenden'  auf  *FeneM-;  -    -'■^-^
lat.  venus,  -eris  f.  , Liebe,  Liebesgenuß,  Liebreiz',  Venus  Name  der  Lieb«i» göttin,  venustus  ,anmutig,  reizend,  lieblich',  veneror,  -ari  ,mit  religiöser  SchW
1147
verehren,  huldigen,  demütig  bitten',  ursprüngl.  ,die  Liebe  bezeugen';  hier- jjer  auch  venor,  -äri  , verfolge  ein  Wild,  jage';
air.^we  {*venja)  , Verwandtschaft,  Stamm,  Familie',  mir.  fin-galach  ,parri- cidalis',  coibnius  , Verwandtschaft'  (*con-venestu-),  abret.  coguenou  ,indio'ena', jnbret.  gouen  ,Rasse',  cymr.  given  ,Lächeln'  (daraus  mir.  gen  ds.  ?);
außerordentlich  reich  vertreten  ist  die  Wz.  uen-  in  den  germ.  Sprachen:
auf  idg.  *ueni-s  geht  zurück  gall.  Veni-  im  PN  Veni-carus  usw.  aisl. vinr  ,Freund',  as.  ahd.  loini,  afries.  ags.  wine]  eine  Jä-Ableituno-  ist  o-ot. loinfa  ,Weide,  Futter',  mnd.  ahd.  winne,  aisl.  vin  f.  , Weideplatz'  (vo-1.  air. fine  , Verwandtschaft');  schwundstufig  ahd.  wunnia,  lounna,  wunnl  ,Lust Wonne^,  as.  wunnia,  ags.  loynn  ds.  (mhd.  icunne  ,Weideplatz',  nur  in  der Formel  wunne  und  loeide  Ersatz  für  das  alte  winne)]
idg.  *uenistro-  wird  durch  aisl.  vinstri  ,link',  as.  ivinistar,  afries.  minister usw.  vorausgesetzt,  eine  Komparativbildg.  wie  lat.  sinister  usw.  (vgl.  hierzu ai.  väma-  ,link');
häufig  ist  der  Übergang  zu  ,bef riedigt  sein,  sich  gewöhnen'  im  Germ.; vgl.  schwundstufiges  got.  unwunands  ,sich  nicht  freuend',  aisl.  una  (^wunen) , zufrieden  sein  mit',  afries.  wonia,  as.  wonön,  tounön  , wohnen',  ahd.  wonen ,ge wohnt  sein,  sich  gewöhnen,  bleiben,  ivohnen^;  as.  giwono,  giwuno,  ags. gewun,  ahd.  giwon  ,gewohnt';  aisl.  o-stufig  vanr  ds.;  abgeleitet  as.  giwono (*-wunan-)  , Gewohnheit'  usw.,  aisl.  vani  m.  ds.;  aisl.  venja  {*wanjan),  as. gi-wennianj  ags.  tvennan  usw.  , gewöhnen';
die  Dehnstufe  hat  germ.  die  Bed.  , hoffen,  erwarten'  angenommen;  got. tuens  (i-St.) , Erwartung,  Hoffnung^  aisl.  vän,  as.  wän  ds.,  afries.  tven  ,Meinung', ahd.  wän  auch  , Vermutung,  Wahn^  Absicht'  usw. ;  Adj.  necess.  aisl.  vcenn (*venja-)  ,zu  hoffen,  hübsch,  angenehm',  wozu  aisl.  vcend  (*venipö)  , Hoffnung, Erwartung',  got.  wenjan  , erwarten,  hoffen*,  aisl.  vcena  ds.,  vcenask  ,sich rühmen',  as.  wänian  usw.;  schwundstuf.  aisl.  ösk  (*wunskö)  ,Wunsch',  ags. wüsc-y  ahd.  wunsc  ,  Wunsch'  usw.,  aisl.  "Bskja  ,wünschen',  ags.  wyscan  ds. (vgl.  gewyscan  , adoptieren'),  ahd.  wunscen  ds.  usw.  (vgl.  oben  ai.  väfichati)'^
```


## [2026-10-17T00:01:06.476Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nfor k in ['HRN','KLN','KNT','WLD','AHD','HUB','OEW','AEF','PHD','NYB','BRT']:\n  v=d[k]; print(k, v.get('page_offset'), '|', v.get('lookup_hint','')[:500]); print()\n\""
}
```


### [2026-10-17T00:01:06.979Z] TOOL RESULT

```
HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

KNT leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.

WLD Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.

AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New Colleg

HUB leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.

OEW None | Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglish00jose?q=<root>

AEF None | Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه‌شناختی فارسی' (Mehrafarin), also not online.

PHD leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).

NYB Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

BRT Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
```


## [2026-10-17T00:01:12.546Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *vam-\\|^ *van-\\|^ *vanā-\\|^ *vanå\\|^ *vantar\\|^ *vītar\\|^ *vyāna\\|^ *vaē-\\|^ *vay-\\|^ *vāiti\\|^ *vātay\\|vanaiti\" BRT.txt | head -40"
}
```


### [2026-10-17T00:01:12.978Z] TOOL RESULT

```
4218:Sprechenden  nahe  liegt,  adjektivisch,  auch sva,  'dieser  mein,  unser':  °na  bansmana imqm  zao^ram  äyese  yaH'^.2.1;  —  vlspa tarsuca  xhiärata  *vanaiti(?)  °na  masanaca i'atihanaca  .  .  ".  .  "durch  diese  (meine) Grösse  und  .,"  P,42";  —  \iimä  dakyai«^ tyil  adam  adarsty  kada  (sd.)  °«J  pärsä iärJ  D.j.z.  n)  in  schwachdeikti- schem  Sinn  'dieser,  der,  er';  l)  auf  Vor- hergenanntes, -gesagtes  (Wort  oder  Satz) zurückweisend;  i)  auf  ein  Wort,  a)  ad- jektivisch: iwt  hafat  vir^rmt  .  .  aal  °na v>r3>!ra  hacimnS  . .  YL  ig.  54;  54;  — parttum  ayasalsa  .  .  °na  parma  tanüm aizuiji/gisYl.i4.^$;  35,  /7.61';  —  mana zaya  asti  vahistjm{%A.)  ,.*na'  vaca  vanSni ..  'na  saya'V.if).<).  b)  substantivisch: yat  .  .  aoxte  alsa  .  .  kacanuha  ml  *''na^^ apirmäyüka  .  .  a%a  *hä  *xsayäe  *°na*'' Aaxisit  (sd.)  ciiva/  *'na^'>  .  .  faraakacaiti (sd.)  ". .  'geh  mit  ihm,  mein  Kind!' . ." N.;?;  —  aitatca..  uxnanam  luchs-isnum.. astica  -na  avavat  uxoala  (sd.) . .  Y.  ig,  10;
11733:manS,  vehu  manS  taj  vanaiti  Yt. /p.  96;  jA'w.;  hazannm  azinqm  .  .  ava.janyät .  . —  parä  .  .  *daiahSui  anhat  b?r3t5  (sd.)  ■  "hrisattm  frascimbananqm  frasHmbaySit ..; vSstrvm:  ttm  {ah  ASn.)  aß paurvavazai-'tat  aiAhe  aiti  paititil  tat'  ..V.  18.1  ^Z.; lyai  (sd.)  V.  2. 24;  —  hixrsm  .  .  ast^m  .  .'P.4j;  — asavamm  . .  ajyei^yai  mraomt..; aaÄai^Tm  .  .;  ta  (APa)  hdhra  frafrS-^  tat  zl  vatiks  Y.7/-13;  —  dazdi  m!  ydka vayaAi  y.S.16;  —  hixr?m  .  .  aslim  ....  mjanani  ..  dahat  ahmäi  ..  ya;%a  ta aishaihim  .  .;  ta  (APn.)  Aa'hra  /ra/rä-'(]S.)upauha(at\t.i5.^t; — iviqm  iainitiS vaySmi;  ti  (statt  NPn.)  kiitmti  yzary.-  \ . .  failySnte  . ,;  tarn  tä  (AP.)  aiibys  .  . yiarmtts..  V.5,i8£;  —  a%ra  ml  urvarä'.msirinavahi  Yt5.87;  —  yB  dim  *fra- raöhnü  vTspä  ,.;  ta  (statt  APf.)  ha%ra  hinan  {sA.)..,  anairyanqtn  tai  dahytmqm vJvärayemi^ . 5.  \^i.;  —  vTspanqm  narqm\vfrihrai  uzjasaiti  N.ffff;  —  agtmanqmat ..  vispanqm  gSus  sar^anqm  . .;  //(ADf.)'*'.  .  vazyail {sA.)  . .  ratSui  nmStum  fi-anäia- larpnava  müwaireisd.)  ..  V,2.27f.;  — 'yatayezi  tajyayata  naväj  tatyayata(sd.) mit  Numeniswechsel:  jahi  . .;  tisca  t^A-j.s;  s\  s',  4';  —  ym  i^  (tiDxi.)  yaf- mraomi  jq%wS.lara  ..  V.i&öa— 65;  — '  tatary  {sd.) 'S.  4  g;  —  ASn.  in  kollektivem "mi^rS.ao/anAs  ..  yatcit  vlmaiiim  (sd.)  Smo:  umarä  baiiazyä ..,- tat  vlsp^m /rTttä- ai^ha  s3mS,   t»mSt  tnihrS  hangrp/simnS  mahi,  tat'  vuppm'  . .  V,  20.  4£  a)  in
17859:ilvöya  *dnisanti  .  ,  yö  'urvaixti  (IS.)  '* havahe  urunB  drulaile  "weh  dem,  der lügt  . .,  der  (weil  er)  mit  Zerstörung  seiner Seele  lügt"  N.iS^'*;  —  nvBya  vananti  ..y5.. ^-urvaixti^''  havahe  (iirunö)  *vanaiti  "weh dem  der  siegt  , .,  der  (wenn  er)  mit  Zer- störung seiner  Seele  siegt"  N.  Ä^^'.
19808:—  iba  asH  vohu  °nB . .  ahm  yat  vahisitm xsa%r9m  vairTm  mana  dqmi  Yt/.a5;  — äämqn  .  .  *yqm  da%at  ahurS  mazdä  .  . ^raosla  vohu  'naaha  vaxst{sd.)  aSa  Vr,i2, 4;  —  aya  daüiaya  fraorsnta  ahurS  matda .  .  vohu  'nB  .  .  a&m  vahisbm . .  Y.57,  '4i Vt  4. 1 ;  —  ahurahe  mazda  .  .  vaahave 'naahe  alai  vahistäi  Y,  /.  i  f.;  70.  2,  Yt  2. 13,  V.^.  43  PUZ.;  —  vohu  'naaha  hactmnB aiaca..xsa%raca  FrW.j.  1;  —  yat  Htarat aarB  mainyuS  dahim  asahe  aniar»  pairi,- avaitgm  vohuca  'nd  atar/ca  Yty.  77;  — haomasia  zsiri^  srXräsQ)ca  vohu  °nS  Y. ig.  19;  —  s  te  (nämL  haomahe)  daifasa irirdhar)  (sd.)  vaahSu?  'naahd  mayaiyS Y.  10.  la.  Undeutlich:  vohu  'naaha jainti  apimHt  aarO  mainyuf  V.  18.  t PüZ.  a)  als  besondereT  Gegner  des AiaManah:  *vanaite  akimät  mang  vohu 'nB  tat  vanaiti  Yt  ig.  96;  —  spmis  main-
22547:/.  28;  —  vanüi  aia  <Sp.  ajo  m.)  akqm  verehren  wir"  Y.57.  33.  Ausser  Zu- drujim  Yljj).  95;  —  vaintj  ahmt  »matte  sammeiibang:  vanaiie  F.S;  —  verderbt: sraa/ä atruÜTm  .,*a/a(Si>.  33010.)  *är7dßm  ätary  vanhSt  vanat  und  ainhä  atar> Y.  60.  5*>;  —  *vanaiU  (pass.)**  akfmcit  vanäi  V.  7.  52  PüZ.***;  —  wertlos:  vanaf manS,  vohu  maaS  tat  vanaiti;  *vanaiU '  Vt  2.  1 1 ;  —  vanatu  Vyt  %$. (pass.)^  mi^aoxts  (vSxs),  fffhtx^  vSx/\  mit  ni'(denFemd,AklL) völligbcsiegen': t»m  vanaiti;  vanät  Aaurvätca  anantäsca  '  ya^a  aE»m  aom  ^äl^m  vanSiti . .  nivanäni ttva  luiami^a  larhamia,  vatat . .'Hx.lQ.<if>',  . ,  tdjanäni  yS  ml  paskät  vataiu  ^X.14-
22558:kavahe  (urunO)  vanaiti  N.  84;  —  sraeiim  j
22607:van-   mit   einander   zu  Tcreinigen,   holte  ich
22617:•  j,  vanaiti'vant-Adj.  'sieghaft':  sraosahe.. vanats  vanaitxi  'vatB  asaonS  .  .  Y.57.33.
22632:j.  vanaiti  N.  log:  lies  vinasti,  %.  'vatd-.
```


## [2026-10-17T00:01:21.719Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"'Baum\\|„Baum\\|siegen,\\|'siegen\\|'erbrechen\\|'ausspeien\\|'verfolgen\\|Verfolger\\|'jagen\" BRT.txt | sed -n 1,60p | cut -c1-250"
}
```


### [2026-10-17T00:01:22.072Z] TOOL RESULT

```
3518:•  j.  apat^e  Inf.  'zu  erreichen,  einzuholen': ap"  sbayäti  vyqs  apagatSe  vyära  "um  ein- zuholen ruft  (ihn)  der  Verfolger,  um  zu entkommen  der  Verfolgte"  Yty.35".
8471:'  'um  "ranqm  uzuxfyenlinam  srlranqm zairi^aoiianqm  vaxsA  (sd.)  apayasaite  V. /Ä63;  Yt. /Ä6;  —  at  aRyäi  (näml.  dem Rind)  mazdä.  'rä  vaxiaj  (sd.)  Y.4S.6;  — avi  racynyq/H  varauhmt  azuitlmca  'ranam Yt.  ^2.3;  —  nima  'vaire
13466:•  j.  därav-,  drav-  n.  i)  'Baumstamm;
14298:•  j.,  p.  '^üra-  Adj.  'siegend,  siegreich'. KoinpA.,  E.  —  Et.  ?')  —  zBed.  »gl.  anai%;  ~ ')  Die    oft  behauptete  Identität  mit  türa.  ist wenigstens  fürs  Aw.  unwahrscheinlich.
22613:•  j.  *van-  f.  'Baum':  yaäia  masyayä  vana kasyaiikam»  "nam  (GP.,  als  Obj.)  aiwi.- vgr-mvaiü  (fA.)  V.5.  2^.
22633:•  j.  vana-  f.  'Baum':  ya%a  masyayB  °na (NS.)  kasyanhqm  vanqm  aiwi.vinnvaiti (sd.)  V.5. 24;  F.  ^;  —  avi  'nqm  yqm kvapTm  (sd.)  V.5. 19;  —  upa  avqm  'nqm ..ya  vaoce  vlspS.6i^(.sd.}  nqma  Yt.i2.tyi —  upa  tqm  'nqm  aati  
22634:Vgl.  ivan:  —  np.  tun  'Stamm',  af^.  vana 'Baum';  ai.  vgl.  väna.  n.  'Baum,  Wald'.  — Pü.:  van.
22699:Eig.Bed.?    Etwa 'Verfolger'  lum  V.oä(^)-?0.
23059:•  j.  varväa-  m.  'Baum':  °s»m  avt  spmtB.- /rasnä  (sd.)  V,22. 19.
23060:KompA.;  Ab1eit.(?].  —  ai.  vfiiä-  ta.  'Baum' (Bthl.  IF.  p.  273);  oosa.  ialäs  'Baum';  np. vgl.  variän  'Waldtaube'  (? ;  FrMOlibr  WZKM. 10.  375). —  Pü.:  veiaii-)  'Wald'.  ^ ')  Dessen Gleichsetiung  mit  variia-  bei  Salemann
23433:•  j-  vä(y)-  V.  'jagen'.     Praes.  i  va^yY: vy-,  3  vaya-,  'vya-'K  —  PFP.  *vSi^wa:
23434:'jagen,  jagend  verfolgen' :^ff^a8a'a»i_j'^»t apu%ram  Janaiti  vIt  vayäti  va  xraosyäti vä  patdayeiti  (sd.)  vä  V.  75. 5 ;  —  ysi  vlsps U  apayeinti  yq  *aoe  paskät  vyeinii  ". ,  denen sie  von  hinten  her  verfolgend  nachjagen"
23436:mit  aipi  'verfolgen,  heijagen  hinter  — ' (Akk.) :  mihr»m  .,yS.,  avarvhi  Alf  api- vaHi^i  bafvart  ypnqnä  nisirinaoiti  "der., hinter  ihnen,  den  wehrlosen  herjagt,  zehn- tausend Sch^ge  austeilt"  Ytio.  37.
23978:•  j.  'vitar-  m.  i)  'der  nachjagt,  Verfolger' (mit  Akk.) :  'tartm  paskäi  hamirik»m  Jan- 1 iar?m  (sd.)  parö  dusmainyäm  "der  den Gegner  von  hinten  her  verfolgt .  ."  Yt  17. , la;  —  °ta  nama  ahmi  Yt /.  13.  j
24900:auch  ZDMG.  44-  553  lu  sbal.  rdtag.  — ')  S  3^.  —  ^*  Eine  höchst  auflallige  Diver- genz. —  4)  Ich  sehe  in  der  Sielt«  eine  .An- spielung auf  Y.  2p.  9.  —  i)  Vgl.  Pü.  lU  Iraaä-, itoöd:  —  6)  Erl.:  tuland  mai  älil
```


## [2026-10-17T00:01:27.675Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 22547 22613 23433 23978; do awk -v L=$l 'NR<=L && /^ *1[0-9][0-9][0-9] *$/ {c=$0; n=NR} END{}; NR==L{print L\": col≈\"c\" (line \"n\")\"}' BRT.txt; done; sed -n 22600,22640p BRT.txt | cut -c1-300; grep -n \"vyäna\\|vyana-\\|vyäna-\\|vāiti-\\|väiti-\" BRT.txt | head"
}
```


### [2026-10-17T00:01:28.207Z] TOOL RESULT

```
22547: col≈1350 (line 22509)
22613: col≈1350 (line 22509)
23433: col≈1401 (line 23352)
23978: col≈1439 (line 23969)
feuchten  Wolken  von  oben  her  die  grossen
Berge  verhüllen"  Vt.  i4-  41-        i)  'bergend
schützen    vor  — '  {parü  mit  Abi.):    mala
(sd.)  yat  nS  ufra.bäzäus  nivänät  tbisyanbyö
". .  damit  er  uns . .  bergend  schütze  vor . ."
Yt.  jo.  7S.
El.?  —  Die  Versuche,  die  verschiedenen  Verba
van-   mit   einander   zu  Tcreinigen,   holte  ich
nicht   für   gelungen;    Tgl.  zB.   Gdn.  3Vt.  79,
Uhlenbeck  WAiSpi.  i^.   Kluge  Wb.  unter
gnainiKit  und  wohniH.  —    Npü.;   guxr  .  .  nSs
dar  buziirg  garän    ml  fiarad,    erl.:    dar  küA  i
biisurg  gvzr  mUunaä  baräy  i  dard  i  mardumän.
•  j.  *van-  f.  'Baum':  yaäia  masyayä  vana kasyaiikam»  "nam  (GP.,  als  Obj.)  aiwi.- vgr-mvaiü  (fA.)  V.5.  2^.
Vgl.  vaHä:  —  ai.  vanäm  GP.  —  Pü.:  van. }.  vana  N.p:  lies  ana;  —  l'.SO:  lies  vai'a. ]'.  vana/ma:  s.  ^van-; —  N.pp:  lies  va  naema. j.  T-anaf  F,  ^f. :  lies  vanf.
•  j.  vanatay-  f. 'Sieg':  sraosaAe . .  vanats {Sp.i25ia.)''MttT/(AP.)va»aiü'vafS  alaond vanats  'naitls  vanaintlmca  uparatät?m yazamaide  Y.57.33.
Ablelt.  —  Zum  V.  'van-.—  Ya.-.  pavSnisnik.
•  j,  vanaiti'vant-Adj.  'sieghaft':  sraosahe.. vanats  vanaitxi  'vatB  asaonS  .  .  Y.57.33.
l'ü.:  vätü/är.
•  j.  vanat-paäana-  Adj,  {fenL  °n3-)  'die
Schlacht  gewinnend':  ya'^a  v?r>%rajA  °nS ^/raxitäne  \.g.20;  • —  aJrTnämi  vavamia ■  *'n3'^  (NSra.)''  iuye  vlspim  aurva'hsm  "ich flehe  darum,  als  Gewinner  der  Schlacht ,  siegreich  zu  werden  über  jeden  Feind" A.  i.  10;  —  fravasayS .  .ya  .,  värüsraytoi \'na  Yt./^.4o;  30
Pü.  {lu  V.):  vämtir  pa  tuiiln,  Sö.  {^a  A): lälako  yuddhtna.  —  ■>  Hds.  •hm  mit  Vw.  — »)  Falich  JN,  JAOS.  TJ.  LXl.
•  j.  vanana-  m.  'Sieger  über  —  (Gen.), ßesieger,  Überwinder':  sraossm  .  .  yS  'nS kayi^ahe  yS  'nS  käthyehe  yS  janta  daevayä
drup  V.57.  15.
Zum  V,  >MM..  — PB.:  vänIISr'i,  SQ.:  aiubhani tälayel  (i.  'van-  No.  16).  —  ')  NpErl.  in SWienAW.  67.  850.  22:  näfaida  kunanda.
•  g.  vananä-  i.  'Sieg":  ku'äirä  ayi  Aahmäi 'nqm  dadh  "welcher  von  den  beiden (Heerschaaren),  wem  wirst  du  den  Sieg verleihen?"  Y.4^.  15.
Zum  V.  'i/au-.  —  Pü.:  vthtk.
j«  j.  vanant-  Adj-  (fem.  'nainli-),  PPrA.: s.  'van:  A)  mit  itar-  m.  Name  eines
als  Gottheit  verehrten  Fixsterns*':  'nant»m stär»n  mazdahätf/n  Vt.2/.i;  r,Äi3,  /2,»6, Ny.  /.  8,  S.  2.  13;  —  'nantS  stSrS  mazda- oataAe  Yt  21.  o,  2,  S.  /.  13,  Vd.  10 (•nmtS).
•)  Er  gilt  Bd.  2.  ?,  5.  I,  Mx.  4g.  12  als  An- führer des  westlichen  (s.  DsT.  ZA.  3.  417)  Fm- sternhimmels  im  Kampf  gegen  den  Planeten Öhrmaid  (Juppiter)  und  als  Hüter  der  Narbutz. passe.  Ob  der  Stern  Wega  gemeint  ist?  S. übrigens  unter  lalavalsa-.
KorqpA-,  E.  —  mp.  (Pü.)  vanand,  gelW.
•  j.  vanar-  n.  —  ?  — :  'nar»  F.  8. Pu.:  nddakada.
j.  vanaiti  N.  log:  lies  vinasti,  %.  'vatd-.
•  j.  vana-  f.  'Baum':  ya%a  masyayB  °na (NS.)  kasyanhqm  vanqm  aiwi.vinnvaiti (sd.)  V.5. 24;  F.  ^;  —  avi  'nqm  yqm kvapTm  (sd.)  V.5. 19;  —  upa  avqm  'nqm ..ya  vaoce  vlspS.6i^(.sd.}  nqma  Yt.i2.tyi —  upa  tqm  'nqm  aati  . .  äi-re  alsmqn isaiti  (sd.)  V,5.  3;  i.
Vgl.  ivan:  —  np.  tun  'Stamm',  af^.  vana 'Baum';  ai.  vgl.  väna.  n.  'Baum,  Wald'.  — Pü.:  van.
•  j.  vanära-  m.  EN.  eines  Gläubigen: 'rahe  asaenS  Yt.  Jj.  loi.
Eig.  Bed.?
•  j.  vanamna-  Adj.,  PPM.:  s.  Han-.
•  j.  vanö.vispa-   Adj.  'alle   besiegend':
dby  Google
1355  »vanta-  —  Jvay-  1356
8663:•  g.  uz«ina-  (,  j.  asma-)  Adj.  'ehrerbietig gegen  — '  (Dat.):  ks  'mSm  cör)i  vyänayä puinm  pfkre  "wer  machte  mit  Weisheit den  Sohn  ehrerbietig  gegen  den  Vater?" Y-44.r-
11042:—  im  jAw,  nur  beim  Zahlwort:  pancä/'a haptäitim  h.  3.  q,  12  (s,  dagegen  7 ;  Sp, 569  o.).  2)  die  Glieder  sind  verbal;  mit Tmesis:  m!ncä  T  [inaz\dazdäm  fsd.)  vafdd- dam  . .  Y.59.  5.  3)  bei  beiden;  b)  im Awf.;  i)  die  Glieder  sind  nominal;  a)  sie folgen  sich  unmittelbar:  uhi  kaurvascü amsritathscä  '^■34-  n;  32.  15;  —  van,ll haurvasca  ain»ntih'a  uva  SiPum^a  tar'- n^mca  Yt  /p- 96; —  *a:'a(ND.)  .  .  vyqsca vyänasca  Yty.  35;  —  twaSm  i^arfiimca vattnmca  Y.  55.  z ;  —  yais  ap3r»saH?m mazdiscä  zara^ultrascä  Y.  /2.  5 ;  —  at hv5  . .  Tsäcä    ataitilcä  Y.4^-5i  V.5. 53;
22444:•  g.  vafav-  m.  'Spruch;  Satzung,  Bestim- mung": at  S  (Sp,  II  m.)  vaocat  ahurB masdä  vldvä  'füs  vyänayä  (sd.)  ". .  ÄhM., der  die  Satzungen  kennt"  Y.  25. 6;  — arsi  msi  sriiücam  vankSuS  'fui  manaa?ß (Sp.  1128  o.)  "recht  soll  mir  kund  werden
23470:•  j.  väiti-gaesa-  in.  Name  eines  Gebirgs*>: ; akmal  hala  garayS  fraexsyan  . .  dvadasS  j 'SS  Yt  ig.  2.
24698:•  j.  vyäna-  Adj.,  PPM.:  s.  vä{y);
24699:•  i.*vyänay-''  f.  —  ?— :  vispä  antan  °nls
27736:1)  'Jemanden,  etwas  (Akk.)  lufen,  an- rufen, aufrufen':  t!ng  sbayä  vanhiu^ uxhäis manankö  "die  will  ich  rufen  mit  den SpTÜchen  des  guten  Smns"  Y.4&.  14;  — thsla  mZ  nqma  sbaya^a  ¥1,75.49;  4.2 {^baySit);  —  urväkamcif  ibayemi  avi  imal vars  Yt.  12. 3i}).  '  a)  bes.  Gottheiten; yd  Ali  (näTai./ravasayi})  yazänS . .  ibayäti Yt  13.  24;  —  asäunqm  ..framaiayS  staomi tbayemi^  ufyemi  yazamaide^  nmänyi  .  . Y.ij.iS;  —  vUpalca  aSe  . .  ga^sfyd(ais IP.) . . tbayemi'^ yatamadal^a^  Y. 7/.  1 1 ; 1 1 ; —  tpm  vairnüi  tbayamaAiVt i5.i;j2.$,Si — yasß  vTspS.matislfm  ssraohm  £baya{iS.) avanAani{sA.)  Y.33.S; — ks  ahi  yü  mqm (näml.  ai^«)  tbayeki  yeiihe  aum  frayd{&6..) tbayiftiqm  sraislim  susruye  vsäm  Yt iy.17;  —  fravasayB  .  .  yi  äährJs  v>r?- %nm  tbayente  Yt.  ;_j.  24;  Y.  20.  3;  — nli£  yasfutnai  . .  Jathyantai  . .  zbayan- tat''''  .  .  äa%at  .  .  ayapfym  Yt  /f.  21 ;  — kal  iöi  asä  tbayentl  avarths zart^uHrai kat  tsi  voha  mananhs  "was  für  Hilfe  hast du,  o  Aia,  was  du,  o  VM.,  fiir  mich,  den Zara&uiira,  der  ich  rufe?"  Y.  4^.12;  — sara%ustra  (sd.)  tarn  aki  pouruiaspahe pukrB  barüryät  Itaca  gapi/i( jSs-AoiH.)^^ "..  von  deiner  Mutter  ward  ich  angerufen" V.  ig.  6;  —  airyamantm  . .  yS  up?mS  (sd.) yS  mähmlS  .  .  zaotlzuye  (3SPM.)*'  G.  /. 6.  a)  mitinf.:  maibyS  z^ya(_iS.)  ai^tn vaishuyä  ait  *gai.tl{sA.)  Y.  j/.  10;  —  bes. mit  avatahe^^:  tä  (Tä.r(A./ravafayll)  mazdä sbayat  *avaähe  Yt/^.  28;  jo.  S^f.*;  — /ravalqyö  ,  .  yä  *ava  *zbayat^^1  avaAke vyqsca  vyänas/aYt  13.3s;  —  "'''  hläsaatca sbayani3i*^  därasia  zbayaniai'"'  Jasaiti avaahe  Yt  ly.  2.  2)    'rufen    nach  -'
```


## [2026-10-17T00:01:44.504Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==267||NR==268||NR==269' WLD_Bd1_pages.txt | head -250"
}
```


### [2026-10-17T00:01:44.823Z] TOOL RESULT

```
258                                          uobh(e)sa   — uen-
ostpreuB. icibbehr. mlid. wnben,                wnberen ,          ivabelen „in unsteter         Bewegung
sein“, wappen „hin und her schwanken“, nhd. (nd.) wabbelig „wackelnd, z. B.
yon Gallertigem", ags. ivnfian „schwenken, schwingen", mengl. waveren.
engl. waver „wanken, scliwanken", aisl. vafla „wackeln“, vafrci ,,sich un-
stet hin und zuriick bewegen, wabern“ (vafrlogi „Waberlohe“), vefjast da.:
  aisl.         „schweben, baumeln", ags. ivmfre „unstet, flackernd“ (oder
            va fa
letzteres  nach Falk-Torp u. reeve als * wait via- zu ueipjb „drehen“? Nicht
annehmbar stellt Persson Beitr. 235 f. auch die germ. d-Formen zu letz-
terem als *ue[i \p sekundar nap-).
                             :




    Lit. vcbhl-ii -eti „wimmeln, sich verwirren, durcheinander bewegen".
                      ,

    Dazu ahd. iribil „Kafer. Kornwurm",- as. invil, mud. wevel da., ags. wifel
„Kornwurm“, aisl. *vifill in tordyfiU „Mistkafer“, ags. wibba „Rofikafer“;
lit. rdbalas „Kafer“:    vabuolas ds., zem. vabolS „Mistkiifer“, lett. rabuolis
„Kafer“ (daneben ostlit. mdartl. vubuolas „Kafer“, zem. vmubole, lett. vam-
balr, rambuole „Mistkiifer“.    Diese Gruppe nicht zu *u<bh- „weben“ (vom
Einspinnen beim Verpuppen. Sehade 1136, Fiekl 4 547. Trautmann Bsl.
Wb. 33fji, sondern „krabbelnd, wimmelnd".
    Vgl Fiek III 4 391, Falk-Torp u. reeve, Trautmann aaO.
    Eine Parallelwurzel nap- ist nicht nachzuweisen weder lat. vappo „ani-  ;



mal Yolans, quod vulgo animas voeant", noch gr. gmolog oder i)ni6h]z
,,Lichtmotte“,            ijnla/.oz   „Fieber" sind      etymologisch           gekliirt,   s.   Lit.   bei Vf.
LEWb. 2 und Boisacq s. vv., Immisch Gl. 6, 193.                        Andrerseits widerstrebt
auch afries. tcapul „Sumpf‘,                  ags. irapol ,, Blase" (u. dgl., a. Pick III 4 3b               I



Falk-Torp u. coble) in Laut und Bed.
   Hierher (oder zu vrbh- ,.weben") diirfte auch norw. cava „Un$inn reden".
ags. wceflian ds. mit iibertragener Bedeutung gehoren und mit lit. rap a,
vapeti „schwatzen, plappern" nichts zu tun haben.     Vgl. Fick III 4 392.


uobh(e;Sa „\Vespe", zu a ebb- „weben". vom gespinstartigen Wespennest
         ( trotz    Meiller Dial, indoeur. 20).
    Ay. nuezaka- m. Name eines daevischen Tieres, balm'i gvabz „Biene.
 Wespe. Hornis" (s. Geiger Abb. d. bail Ak. 1891, 125, Bthl. Wb. 1346):
                                                           -
                                                               .




 lat. vespa (zunachst aus * co-spa, Solmsen Stud. 24 f.j „ Wespe" abret. ynohi.             :



 corn, ijuhini „ Wespe" (Loth, s. Rc. 15, 220: air. foirh aus brit. *mtoclti
 entlehnt     Zimmer KZ. 33, 276): ahd. wafsa, u-efsa, nhd. Wespe (letzteres
 wohl nach lat. respa umgestollt: nhd. hair, urbis wold noch direkter NacK
 komme von idg. vobhesu, Kluge 9 s. v., kaum geneuert nach Weigand-Hirt
 s. v.i, ags. wwfs, weeps, weesp ds.   lit. rap'd „Wespe, Bremse", pr. wobse.
                                                  ;


 „Wespe"; ksl. osa „\Vespe" iaus vopsa. Meillet IF. 5, 333, Pedersen
 KZ. 3b, 312, Trautmann Bsl. Wb. 342).
      Vgl. Currius 382, Vf. LEWb. 2 s. v.


 lien-.      Als Grundbedeutung dieser Wz. wird „streben, erstreben" anzusehen
         sein,     woraus sich             Bedeutung „wiinschen, lieben", dann
                                       einerseits die
         „befriedigt sein,      gewohnen", andrerseits „arbeiten, Miihe haben
                                      sich
                                                                                                                  "




         und perf'ektiv „erreichen, gewinnen, siegen" ergeben kann. An eine
         Trennung der Wzn. ist nicht zu denken. Vgl. (anders) Meringer IF.
         16, 179ff., 18. 236. KZ. 40, 232, Wood Mod. lang. not. 21, 22 f.

                  :




                                                           uen-                                                             25y

     Ai. vdnati, vanoti „wiinscht,                    liebt,       erlangt,     gewinnt, siegt“, av. vanaiti.
vanaoiti         „siegt“ Bartholomae Airan. Wb. 1350 f.), mp. vanitan „be-
                               (vgl.
siegen, schlagen“; ai. Aor.-Praes. vnndti (vgl. got. wunan ) in gleicher Be-
deutung.    Kaus. vandyati und v&ndyati (ersteres nicht belegt); als -sk-
Praes. ai. vcincliuti ,,\viinscht“, vgl. v flncha f. ,,Wunsch“ (s. u.); vanas n.
„Lust“ (vgl. lat. Venus), vani-h f. ,,Yerlangen, Wunsch“, wozu vaffiyati
„bettelt“, varuynka- „Bettler“, rand- als nom. ag. m. (vgl. av. -vanus in
nom. pr.). In Zusammensetzungen erscheint vdnya-; s. ferner vantfi- als
nom. ag. m. fav. vantar „Sieger“), vanti- nom. act. (unbelegt, doch vgl. av.
-raintis). GewiB gehort auek ai. vama- „link“ und vama- „lieb(lich), 10 stern
                                                                                                                                1




unmittelbar hierher, wiihrend vama- „verkehrt, widerwiirtig“ vielleicht
anders zu verbinden ware. tJber ai. vennti „ersehnt“ usw. s. u. iiei- „auf
etwas losgehen“.
   Hierher wohl arm. oyn „Gewohnheit“, imim „haben, halten, ergreifen                                                             1




 *enn-ewi vgl. Patrubany, IF. 14, 5Sf., Pedersen KZ. 38, 203 40, 209 f..
('
                                                                                                                 ;



s. Liden KZ. 41, 395 a 2), weshalb ein idg. nten- anzunebmen ist.  Ferner
arm. gun ( *uono ) „storzo, tentativo“ (Petersson KZ. 47, 255)?
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
„Nordwales“ (Fick II 4 270; s. auch Zimmer KZ. 24, 212). Stokes KZ. 37.
                                                                                                        11
250 stellt irrig hierher ir. deoin (nicht *de-voni-) „pleasure, will auch mir. form                          ;



..Wunsch, Yergniigen" (Stokes KZ. 41 3S5f.). ir. farm, cymr. gwan „schwaeh,
                                                               ,



elend    (Zupitza KZ. 36. 73) sind nicht zu got. ivnntw, winnan zu stellen.
           11




  AuBerordentlich reich vertreten ist Wz. lien- in den germ. Sprachen,
wozu man Fick III 4 386 f. {yen 1.2.) Falk-Torp 1339, 1350, 1366. 1367.
1382. 1392, 1408, 1420 (s. auch die Nachtriige) vergleiche.
     Auf idg. *ueni-s geht zuriick altn. v'mr „Freund“,                                       as.      ahd.      ivini,    afries.
 ags. wine (vgl. air. fine „Yerwandtschaft‘ ).Eine /n-Ableitung ist got. irinja
                                                                      !




 ..Weide, Futter 11 , mnd. ahd. ivinw, altn. vin f. „Weideplatz“.   Schwund-
                                                          11
 stufig ahd. wunnia, wunna, icnnni „Wiese. Weideplatz        aber auch ..Lust.                     .



 Wonne“, as. ivunnitt nur mit der Bed. ..Wonne, Freude 11 ebenso ags. wynn.                    ,


 lYegen dieses germ. Bedeutungsiiberganges zu „Weideplatz“ wird auch ai.
 vnna-m n. „Wald, Baum, Holz“, vana f. „Reibholz‘ av. vanfi-, mp. van. np.          :

                                                                                        ,


 bun j.Baum" (wozu auch ai. vfinara- „Affe (= Waldbewohner) als Abltg.    l(




 von vanar- „Holz, Wald“ nach Macdonell IvZ. 34, 292) zu idg. uen- ge-
 zogen (Uhlenbeck Ai. Wb. 270). Der Bedeutungsubergang ist jedoch inner-
 halb der indischen Sippe unglaubhaft.
      ^Va'iie,        Etvraoloq-ischo^ "Worterbnch.   I.

260                                                                                ue-n-g-


                                                 ;
   Idg. *uenistro- wird durch altn. vinstri „link ‘, as. winistar afries. minister                                                    ,


usw. vorausgesetzt, eine Komparativbildg. wie lat. sinister usw. (vgl. hierzu
ai. vCLma „link“, s. o.).

  Haufig und allgemein verbreitet                                                       ist           der tlbergang zu „befriedigt sein,
sich    gewohnen   im Germ. Ygl. schwundstufiges got. univunands „sich
                                      11




                 altn. ttna ( *wunon) „zufrieden sein mit“, afries. ironia as.
                             11
nicht freuend                     ,                                                                                                                                 ,


ivonon, wunon „wohnen“, ahd. ivonen wonon „gewohnt sein, sich gewohnen,                 ,

sich aufhalten, bleiben, wohnen
                                                                      11
                                    as. g iicono giicu.no ags. geivun ahd. giuon
                                                                           ;                                ,                ,                ,


„gewohnt“, altn. o-stufig vcmr ds. Wovon abgeleitet as. giicono (p-vunan-)
„Gewohnheit“ usw., altn. vani m. ds. Yb. Abltg. altn. venja *wanjon ),                                                                            ('


as. gi-wennian ags. icennan usw. „gewohnen“.
                                  ,


   Die Dehnstufe hat germ, die Bedtg. „hoffen, erwarten“ angenommen;
got. wens ( - St.) „Erwartung, Hotfnung“, altn. van as. trail ds., afries. wVn
                        2
                                                                                                                     ,


„Meinung“, ags. wen „Erwartung, Hoffnung, Meinung“, ahd. van auch                                                                                  1


„Yermutung, Wahn, Absicht“ usw. Dazu adj. necess. altn. vdenn ( *vcnja -)
„zu hoffen, hiibsch, angenehm“.    wozu and. ana-irdni „verdachtig“ usw.,
altn.   vcencl     )
                     „Hoffnung,  Erwartung“,
                            ( *vcnipd          ahd. wanida „ argumentation
                                                                 11     11
```


## [2026-10-17T00:01:53.309Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^ *wām\\|^ *wan \\|^ *wan\\b\\|^ *wanīdan\\|^ *wānīdan\\|^ *wanafš\\|^ *wanawšag\\|^ *wanafšag\\|wanafš\\|^ *wāyīdan\\|^ *wāy-\\|wānīdār\\|wāmīdan\\|wādag\" PHD.txt PHD_mackenzie.txt | head -30"
}
```


### [2026-10-17T00:01:53.800Z] TOOL RESULT

```
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:909:baby waččag, kédak, kawādag.
PHD.txt:4225:violet wanafšag.
PHD.txt:5187:niwistan winastag wanafšag winjisk nizār nizārīh nizārīh- nazd nazdikih nazdik wizend nazdist wizend wizand- wizandag
PHD.txt:5274:wām- -l
PHD_mackenzie.txt:5159:wan [wn l I N bun] tree; stock, stem.
PHD_mackenzie.txt:5162:wan-, -isn, v. winidan.
```


## [2026-10-17T00:02:05.232Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^ *vām\\|^ *van \\|^ *van-\\|^ *vanīt\\|^ *vānīt\\|^ *vanafš\\|vanavšak\\|vanafšak\\|^ *vātak\\|vātāk\\|vāmītan\\|vāmēt\" NYB_vol2_glossary.txt | head -20; grep -n \"vätäk\\|vātāk\\|vatak\\b\\|vamidan\\|vämidan\\|bunafs\\|banafs\\|binafs\" HRN.txt HUB.txt | head -20"
}
```


### [2026-10-17T00:02:05.849Z] TOOL RESULT

```
3927:van [wn'] tree 409-11.26. 415, — Av. (1353) van- or (1354) vana-; Paz. van, gan (Mx); NP van ‘wood, forest’ (probably lw., but ef nar-bun, nür-vun, när-van ‘the pome- granate tree’).
3928:Van n. pr. fem.: ~ i Gulaxsän V. daughter of Gulaxš = Valaxš (g. v.), probably a prince or king of the Arsacid family; ~ the name of her town 117. — Other explanations Cat. 106 sg.
3932:Van-*FröSn [wn' plwšn'] n. pr. 478. — BdA p. 229? wn' plwksn', BAJ 779 (Paz.) Van-fryešni (but -k- in -wk- is certainly only orthographieal, warranting the pro- nunciation -6- of -w-).
4977:van-: pčravanihit vasly: vas vazrka-: vazurg viO-: vis
HUB.txt:4403:mobad etc.) = zd. paiti-, arm. -pet ; banafsa 'Veilchen' neben
HUB.txt:4404:binafsa, bunafsa, arab. banafsaj, phi. vanavsak^ etc.
HUB.txt:5459:bisyar Viel' =■ paz. vasydr Min. Gl. 210; banafsa 'Veilchen'
HUB.txt:8409:in banafsa 'Veilchen' H. 231, s. oben p. 31. Dunkel ist
HRN.txt:2056:phlv. vat^ vatak, arm. LW. vat, vatfar, vergl.
HRN.txt:2389:ar. LW. banafsaj, syr. LW. <3J^E>:32 (de Lagarde,
```


## [2026-10-17T00:02:08.624Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2380,2400p HRN.txt; echo ----; sed -n 8400,8415p HUB.txt; echo ---; sed -n 4398,4408p HUB.txt; echo; grep -n \"^ *231\\.\\|^ *23i\\.\" HRN.txt | head"
}
```


### [2026-10-17T00:02:08.957Z] TOOL RESULT

```
2) *6epäck', phlv. bunak *Gepäck, La^er', Nöldeke,
ZDM6. 46, 143 (vergl. bei. bunag, n. bunay (41)
*Gepäck').
230. bende *Sklave, Diener'.
ap. ba(n)daka- 'Sklave*; phlv. bandak,
231. henefSe Teilchen, bunefse^ binefse; bunefs *blau'
(Sahn. I, 48 Vers 265, 107 Vers 839)\
mäz. venewse,
phlv. vanawsak, vanatcsa Teilchen (Bund.).
ar. LW. banafsaj, syr. LW. <3J^E>:32 (de Lagarde,
Ges. Abh. 22), arm. LW. maniisak (de Lagarde,
No. 1427).
232. heng 'Bilsenkraut', bengi 'sinnlos '), vergl. metig *Hanf .
aw. batiha- ein Narcoticum, vergl. Banga-; skr.
bhatigä- 'Hanf; ein aus Hanfsamen bereitetes Nar-
coticum'; arm. LW. bang voaxiaiiiog, ar. LW. banj; af;\
bang 'RsLiif; nhd. Bangenkraut 'Schierling* (Grimm,
Wörterbuch I, 1105).
russ. penka, poln. pienka, czech. pcnek, p6nka scheinen
entlehnt (Hehn, Kulturpfl. 484). ^
233. huden 'sein, Praes. buv-em'^ vergl. bos-em, bad; buvis, 0Ou)
----
xem 'theile zu', basxis 'Geschenke' = np. baxs 'Theil', bax-
6'idan *schenken*, ia^rs/s 'Geschenk* ; erasa; Vothlich* (11. Jhd.)
= np. raxs 'color ruber et albus* u. s. w. ; arm. bdeasx 'Unter-
konig = syr. aptaxsd, gr. Tundirjg, lat. vitaxa,
§ 127. Idg. ps - ap. fff = np. s im Anlaut, fs im
Inlaut :
sarm *Scham' ^^ zd. fsarema-, osset. dfsarm; im In-
laut: dirafs 'Banner -= zd. drafsa-, arm. dram. Jungeren
Ursprungs ist fs (^= w-S) in afscindan H. 102, unsicheren
in banafsa 'Veilchen' H. 231, s. oben p. 31. Dunkel ist
das Verhaltniss von zd. fstdna- zu np. pistan 'Brust', siehe
oben p. 41.
§ 128. Idg. pk^ —^ zd. fs -^- arm. np. s im Anlaut:
subcLn 'Hirt' = zd. "^fsupCLna-, arm. spet *Hirt' = zd.
*fsupaiti' von zd. fsu- 'Vieh' in Kompos. (= idg. ph^u-) ^=
selbstandigem pasu- (idg. pek^u-).
---
zd. nava^); ausl. -ux aus -axv: pasux 'Antwort* = phi.
pasaxv (oben p. 36, Pandnama Gl. p. 99) ; farrux 'gliicklich'
= phi. fairaxv; suxtin ^= suxan *Wort', paz. saxun aus
sax^'arij arm. -sohun im N. pr. Bastsohun (bei Mos. Chor.).
Wechsel von a und u: -bad == -bud *Herr (vgl. herbiid,
mobad etc.) = zd. paiti-, arm. -pet ; banafsa 'Veilchen' neben
binafsa, bunafsa, arab. banafsaj, phi. vanavsak^ etc.
Fiir ap. a erscheint mp. o = np. w und 5 in 7nuy =
moy *Magier, arm. mog und (spater) mov (pi. movan), syr.
muy- in muyanandarzbad (Hoffmann, Ausziige p. 50), phi.
geschrieben magu^ gesprochen moy^ gr. f-idyog, hebr. yo, ap.

2385:231. henefSe Teilchen, bunefse^ binefse; bunefs *blau'
9904:231. Vergl. Hübschmann, ZDMG. 46, 244 No. 72.
11341:231. yask 'Krankheit, AW.-Komm., Bund. (Tsk), N. pr.
```


## [2026-10-17T00:02:14.462Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"banafsa\\|vanavs\\|vanaws\" HUB.txt; awk 'BEGIN{RS=\"\\f\"} NR==42' HUB.txt | grep -n -i -B3 -A8 \"banafs\\|vana\""
}
```


### [2026-10-17T00:02:14.842Z] TOOL RESULT

```
1029:231. Np. hiinafSu *Veilchen ^ phi. vanavsak (fiir vanafsak)
4403:mobad etc.) = zd. paiti-, arm. -pet ; banafsa 'Veilchen' neben
4404:binafsa, bunafsa, arab. banafsaj, phi. vanavsak^ etc.
5459:bisyar Viel' =■ paz. vasydr Min. Gl. 210; banafsa 'Veilchen'
5460:= phi. vanavsak Bdh. p. 66, Z. 17, paz. vanavsa ebenda
8409:in banafsa 'Veilchen' H. 231, s. oben p. 31. Dunkel ist
1-.^ 31 ~
2-228. Arm. bun 'Starnm, Schaft* ist nicht = np. bun *Baum'
3:(in gdz^bun^ sarv-hun etc.) = zd. vana- *Baum* = phi.
4-van, da ein aus dem Mittelpersischeii ins Altarmeni-
5-sche entlehntes "^van hier eben *van, nicht bun lauten
6-wurde. Also ist Horn's Bemerkung 2) zu Nr. 229
7-nicht richtig.
8-229. Ich nehme daher nach wie vor ein einheitliches arm.
9-hun *Stanun, Stiel, Schaft, Abstammung, Ursprung,
10-Grund, Wesen, Ende' an = paz. phi. bun 'Grundlage,
11-Wurzel, Ursprung, Anfang', skr. budhna- *Boden, Grund,
--
21-wenig np. buna *Lager, Gepack\ bal. LW. bunag *Gepack*
22-(Geiger, Lautlehre p. 24), arm. bnak 'Wohnung',
23-bnakem Vohne'.
24:231. Np. hiinafSu *Veilchen ^ phi. vanavsak (fiir vanafsak)
25:nach Fr. Muller WZKM. 7, 368 = zd. ^vanavaxsa-
26-(also — *im Walde wachsend). Mir nicht wahrschein-
27-lich.
28-232. Np. bang bei Abu Muwaffaq p. 54. Zu np. mang
29-vgl. phi. mang Gl. and Ind. 220.
30-234. Np. bor *Fuchs hat mit skr. babhru-^ dem im Persi-
31-schen nur *babr entsprechen wiirde (vgl. Nr. 181) nichts
32-zTi schaflfen.
33-235. Horn's Zusammenstellungen sind hochst bedenklich.
```


## [2026-10-17T00:02:22.562Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Speichel\\|speien\\|erbrech\\|Erbrech\" HRN.txt HUB.txt CHEUNG.txt | head; grep -n \"^ *229\\. \\|^ *228\\. \" HRN.txt; "
}
```


### [2026-10-17T00:02:22.826Z] TOOL RESULT

```
HUB.txt:1699:*) Vgl. die Wurzel apiv = apyu *speien*.
HUB.txt:7171:ap. *tiistdman'? (oben p. 101); siJcanam *zerbreche' = ar.
HUB.txt:7595:bildungen); gusistan 'zerbrechen =^ ap. *vi'si8tanaiy von
HUB.txt:8491:= arm. Ia§kar (Elise p. Ill); sikastan zerbrechen*, zd.
HUB.txt:9048:c) Idg. rfw, dAw — ap. np. n: sikanam zerbreche aus
HRN.txt:619:Zu arm. orc 'Speichel, Erbrochenes*, orcam erbrechen,
HRN.txt:3658:390. fü/ 'Speichel*, tufek{'% dehen)^ tiifke (Gazoph. s. v.
HRN.txt:3661:III, 34; Studien II, 42); got. speivan; arm. tüiß 'Speichel';
HRN.txt:3663:kurd. tef 'Speichel', tiw, tuw^ tu, tiik 'Spucken,
HRN.txt:3664:Speichel*; afy. tu, tük, tükal spucken*; oss. ft* (251);
2351:228. {i)hun XBaum)stamm, -Stumpf (Sahn. III, 1742 Vers
2359:229. {2)bun 'Fundament, Grund*, vergl. bunyad {*bundad),
9899:228. Vergl. auch servbun *Cypressenbaum (Sahn. I, 156
11325:228. v{i)nästan Verletzen, vernichten', häutig, v(i)näs(i)snth^
11328:229. v{i)Seft einer der päderastirt hat', v(i)sepU *einer der
```


## [2026-10-17T00:02:25.456Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2351,2362p HRN.txt; sed -n 9895,9903p HRN.txt; awk 'BEGIN{RS=\"\\f\"} NR==318' HRN.txt | head -60"
}
```


### [2026-10-17T00:02:25.741Z] TOOL RESULT

```
228. {i)hun XBaum)stamm, -Stumpf (Sahn. III, 1742 Vers
4316), vergl. gözbun *Wallnussbaum*.
Käs. bend, bene (s. v. direkt)?
aw. vanä' 'Baum'; phlv. van; ai. vdna- 'Baum,
Wald'.
af/. vana 'Baum'; oss. d. ^bun, t. -bin *Wald' (67);
bei. gvan, gön Vilde Pistazie (?) (133).
arm. LW. bun 'Stamm (eines Baumes), Schaft*.
229. {2)bun 'Fundament, Grund*, vergl. bunyad {*bundad),
aw. buna- 'Grund, Boden'; phlv. bun, mand. LW.
NDJD Tundament'; ai. budhnd^^) 'Boden, Grund,
Unterstes'; arm. bun 'Natur, (pvaig\ adj. naturalis,
216. Arm. LW. bazpayit *Sündensühnung aus ap. *bampaiiti'
(Hübschmann, Literar. Centrbl. 1892, Sp. 1627).
217. Kauk.-bergjüd. auch ves, mäz. res.- 257 —
218. Dazu arDi. LW. pastar, Hübschmann, KZ. 26, 605.
228. Vergl. auch servbun *Cypressenbaum (Sahn. I, 156
Vers 489, 160 Vers 561), /ärbun 'Teufelszwirn' (AM.
180), sowie ftürven. nürvan *ülme' (nach Abdul
Achundow, Comnientar zum sog. Liber fundamen-
torum, Dorpater Dissertat. S. 87).
— 296 —
2) *Voger, vergl. väyandak Togel* (Men. 62, 16).
aw. vay- * Vogel*; ai. vdy-, oder nach Joh. Schmidt
KZ. 32, 330 Nom. Sg. aves (RV. I, 130, 3?), dazu
vibhis (aus *vlbh!s), Schmidt stellt dann auch lat. avis,
gl*, w^rofe-, (perg.) aißerog, ouovdc (S. 374 folg.) hierher.
208. vctjTtan {cäzUan) 'fliegen; fahren, AW.-Kommentar,
z. B. vd. 5 (4), 6 (54), Bund., Aogem.
aw. {^oaz-^ vazaiti 'fliegen; fahren etc. ; ai. [/^oah-
*fahren', vergl. np. veziden (oben No. 1083).
In den erwähnten Bedeutungen wird das Verbum
im Kommentar meist nicht glossirt, während es als
'führen, bringen {vajlnUan) nur umschreibend auf-
tritt.
Vergl. bei. gvazay, n. yvazay, guzay 'über etwas
weggehen, überschreiten, vergehen (von der Zeit)' (144).
209. va^sltiifi 'wachsen, anwachsen, zunehmen, häuttg;
vaxs(i)sn^ oä/smitan.; va/s *herhsige (West, vd. 9 (132)
Gl.), Enterest (of money), increase', vergl. Va^sastän
'increase code' (West^, 139), kofoa/s 'mountain spur'
(West-, 35); arm. LW. vasx * Wucher (Hübsch-
mann, ZDMG. 46, 329 No. 6).
aw. \/^va/S' 'wachsen*; ai. [/"vaks-^ äüksat; got.
vahsjmi 'wachsen*.
Vergl. zaza vas 'Gras, Kraut, Pflanze*; af/. va/a
'Futter, Gras'; wa:^. ous, väs, si/n. vos^ vost, sar. vu/,
sangl. ö^, minj. va^s Gras, auch wa;/. vüsln, sar. vu^^ti
'Trift'.
Dialektisch neupersisch findet sich väs (mäzend.),
vos (Semn.) 'Gras etc.'; väs 'Futter (Vullers), das
Castle aus Golius anführt, vermag ich ebenso wenig
zu belegen, wie andere Worte aus dieser Quelle, z. B.
Iießden 'trocken werden*.
210. vätnltan 'speien', vd. 5 (6) ^).
aw. i^varn' 'speien'; ai. l^vam-, väiniti; lat. vomö etc.
') Brugmaun, Gruudriss 11,2 § 572 glaubt nicht an den zuerst
von de Saussure aufgestellten Satz von den zweisilbigen Wurzeln
(vergl. auch I, § 14, § 100 und Griechische Grnmnintik' § 11 Anni.),
```


## [2026-10-17T00:02:31.149Z] TOOL CALL #23: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-10-17T00:02:31.159Z] TOOL RESULT

```


```


## [2026-10-17T00:02:33.639Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/بنفشه",
 "prompt": "Give the full etymology section(s) for Persian بنفشه verbatim."
}
```


## [2026-10-17T00:02:34.139Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/banyan",
 "prompt": "Give the English etymology of banyan verbatim (and banian if mentioned)."
}
```


## [2026-10-17T00:02:34.840Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/वणिज्",
 "prompt": "Give the etymology of Sanskrit vaṇij verbatim."
}
```


## [2026-10-17T00:02:35.606Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/वन",
 "prompt": "Give the Sanskrit etymology of vana 'forest' verbatim."
}
```


## [2026-10-17T00:02:36.539Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wemh₁-",
 "prompt": "Give the root meaning and list of Indo-Iranian, Latin, English descendants verbatim."
}
```


## [2026-10-17T00:02:37.523Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wenh₁-",
 "prompt": "Give the root meaning and the Indo-Iranian descendants (Sanskrit, Avestan, Middle/New Persian), and whether Sanskrit vana 'forest' is listed."
}
```


### [2026-10-17T00:02:40.112Z] TOOL RESULT

```
# Etymology Section for Persian بنفشه

From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[wnpšk'](/wiki/wnp%C5%A1k%27#Middle_Persian "wnpšk'")_ (wanafšag, "violet"), of uncertain origin; see there for further information.
```


### [2026-10-17T00:02:41.295Z] TOOL RESULT

```
# Proto-Indo-European *wenh₁- Root Analysis

**Root Meaning:**
The root means "to love."

**Indo-Iranian Descendants Listed:**

The document explicitly mentions Sanskrit descendants:
- Sanskrit वनति (vánati) - "to like; to gain"
- Sanskrit वनोति (vanoti) - "to like; to gain"  
- Sanskrit वनस् (vánas) - "loveliness; desire"
- Sanskrit वन् (van)

**Avestan and Persian:**
No Avestan or Middle/New Persian descendants are documented in this entry.

**Sanskrit vana 'forest':**
The word "vana" meaning forest is **not listed** in this reconstruction article. The Sanskrit terms provided relate to meanings of "liking," "gaining," "desire," and "loveliness"—semantic domains connected to the root's sense of loving or desiring, but distinct from the forest meaning.
```


### [2026-10-17T00:02:41.592Z] TOOL RESULT

```
# Proto-Indo-European Root *wemh₁-

**Root Meaning:**
"To spew, to vomit"

**Indo-Iranian Descendants:**
- Kurdish (Northern): bîvêr ("sick, ill")
- Persian: بیمار (bimâr, "sick, ill")

**Latin Descendants:**
- vomitus

**English Descendants:**
The page does not list direct English descendants. However, English words related to vomiting derive from the Latin branch rather than appearing as independent English descendants in this entry.
```


### [2026-10-17T00:02:41.842Z] TOOL RESULT

```
# Sanskrit Etymology of वन (vana)

According to the Wiktionary article, the Sanskrit etymology is provided as follows:

"Thematised from _[वन्](/wiki/%E0%A4%B5%E0%A4%A8%E0%A5%8D#Sanskrit "वन्")_ (ván, "tree, wood"), from [Proto-Indo-Iranian](https://en.wikipedia.org/wiki/Proto-Indo-Iranian_language "w:Proto-Indo-Iranian language") _[\*wán-](/w/index.php?title=Reconstruction:Proto-Indo-Iranian/w%C3%A1n-&action=edit&redlink=1 "Reconstruction:Proto-Indo-Iranian/wán- (page does not exist)")_ ("tree, wood")"

In summary: The word derives from the root वन् (ván) meaning "tree, wood," which itself originates from Proto-Indo-Iranian *wán- with the same meaning.
```


### [2026-10-17T00:02:42.460Z] TOOL RESULT

```
# Etymology of Sanskrit vaṇij

According to the Wiktionary entry, the etymology is: "From Proto-Indo-Aryan *waníṭṣ ~ *waniȷ́ás, from Proto-Indo-Iranian *wanHáćš ~ *wanHȷ́ás, from Proto-Indo-European *wn̥h₁-h₂éǵ-s ~ *wn̥h₁-h₂ǵ-és."

The ultimate PIE roots are "*wenh₁-" ("to strive") combined with "*h₂eǵ-" ("to drive, lead") plus "*-s" (nominative suffix).

The entry also notes: "Possibly cognate with Ancient Greek ϝᾰ́νᾰξ (wắnăx, 'lord, king')."
```


### [2026-10-17T00:02:43.116Z] TOOL RESULT

```
# Etymology of Banyan

According to the Wiktionary entry, the English word "banyan" comes from Portuguese _baniano_, which derives from Arabic _بَنِيَان_ (baniyān). The Arabic term originated from Gujarati _વાણિયો_ (vāṇiyo, "merchant"), which traces back to Sanskrit _वाणिज_ (vāṇijá), ultimately from earlier Sanskrit _वणिज्_ (vaṇíj, "merchant, trader").

The entry notes: "The name appears to have been first bestowed popularly on a famous tree of this species growing near Bandar Abbas, under which the Bannians, or Hindu traders settled at that port, had built a little pagoda."

The word is also identified as "a doublet of _bunnia_," indicating a related etymological connection.
```


## [2026-10-17T00:02:56.617Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/wnpšk'",
 "prompt": "Give the etymology verbatim, including any mention of *wana-waxša or forest-growing."
}
```


## [2026-10-17T00:02:57.567Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/بن",
 "prompt": "Give each Persian etymology (bon/bun 'root, base' and any 'tree' sense) verbatim."
}
```


## [2026-10-17T00:02:58.171Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/vomit",
 "prompt": "Give the English etymology verbatim."
}
```


## [2026-10-17T00:02:59.046Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyh₁-",
 "prompt": "Give root meaning and Indo-Iranian descendants (Avestan vay-, vītar-, etc.) verbatim."
}
```


### [2026-10-17T00:03:02.224Z] TOOL RESULT

```
# English Etymology of "Vomit"

The word "vomit" comes "From Middle English _vomiten_, from Latin _vomitāre_ ("vomit repeatedly"), frequentative form of _vomō_ ("be sick, vomit"), from Proto-Indo-European _*wemh₁-_ ("to spew, vomit")."

The entry notes related cognates including Old Norse _váma_ (nausea, malaise) and Old English _wemman_ (to defile).

[WebFetch note: this page's text is 102023 characters long and the answer above covers only characters 0 to 100000; the final 2023 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


### [2026-10-17T00:03:02.626Z] TOOL RESULT

```
# Proto-Indo-European Root *weyh₁-

## Root Meaning

The reconstructed root **\*weyh₁-** has two primary meanings: "to chase, pursue" and "to suppress, persecute."

## Indo-Iranian Descendants

According to the Wiktionary entry, the Indo-Iranian descendants include:

**Proto-Indo-Iranian:** "\*wáyHti" (with further descendants listed but not fully detailed in the provided content)

**Proto-Iranian:** "\*wayHukah" leading to:
- **Parthian:** "wʾywg" (hunter)
- **Sogdian:** "w'ywq" (hunter)

The entry also mentions "\*wayHuš" as a Proto-Indo-Iranian form, though specific Avestan forms (vay-, vītar-, etc.) that you requested are not explicitly provided in this excerpt of the Wiktionary page.
```


### [2026-10-17T00:03:03.982Z] TOOL RESULT

```
# Persian Etymology for بن (ben/bon)

## Etymology 1 (bun/bon - 'root, base')

"From Middle Persian \[script needed\] (bwn' /⁠bun⁠/), from Proto-Iranian _[\*buHnáh](/w/index.php?title=Reconstruction:Proto-Iranian/buHn%C3%A1h&action=edit&redlink=1 "Reconstruction:Proto-Iranian/buHnáh (page does not exist)")_"

The noun meanings listed are: "bottom," "foundation," and "root."

## Etymology 2 (bun/bon - 'tree' sense)

"From late Middle Persian \[script needed\] (bwn' /⁠bun⁠/), from earlier \[script needed\] (wn' /⁠wan⁠/, 'tree; stock, stem')"

The archaic noun meanings are: "bush" and "tree."

[WebFetch note: this page's text is 102155 characters long and the answer above covers only characters 0 to 100000; the final 2155 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


### [2026-10-17T00:03:04.320Z] TOOL RESULT

```
# Etymology of wnpšk' (Violet)

The etymology section presents two competing theories:

**Bailey's Theory:**
"The origin is uncertain. Bailey derives from the Iranian colour-name *van- ('blue'), comparing for it Khotanese banāte ('plum or pear'), Old English wann ('dark') and Old Armenian van- ('crystal')." The suffix -ap- is compared to Latin cannabis.

**Martirosyan's Theory:**
Martirosyan proposes "connection with Ancient Greek ἴον (íon, 'violet'), earlier *ϝίον (*wíon)...and Latin viola ('violet'), suggesting that 'we might be dealing with a Mediterranean-Iranian flower-name' with a proto-form like *wion- which might yield Iranian *v(y)an-."

The document notes that "Some of the descendants...presuppose a by-form *manafšak" but makes no mention of "wana-waxša" or forest-growing characteristics anywhere in the etymology section.
```


## [2026-10-17T00:03:09.120Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *van\\|\\bvan-\\|vanaiti\" KNT_full.txt | head; grep -n -i \"^banyan\\|^banian\" KLN_1966.txt SKT.txt HJB.txt AID.txt 2>/dev/null| head; command ls | grep -i \"hjb\\|AID\""
}
```


### [2026-10-17T00:03:09.473Z] TOOL RESULT

```
7183:vanl-; apariydya is not *ahap-, see Lex. s.v. ay-. 
8082:IV. Stems in -van-: artd-van-,xSaca-pd-van-,fan- ` 
8739:-an- -man- -van- -vin- -vanl-, -L- -d- -0- -s-. Some 
8806:vant, Lg. 8.1-10. 
9735:Those with suffixes (Aryan) -man- -van- -an- 
9813:vantahyd, with transfer to -o- stem ending, and 
11024:‘dig’; afahya and afahiya, to Ваћ-; avaniya, to van-; 
23783:vant- ‘running, hasting, horse’, from Ar. ar- ‘move’ 
23863:with lengthened final vowel, + ad]. suffix -van- 
24890:see under van-); DZe 10°. 
AID.txt:805:Banian.  See  Bdbhan.
AID.txt:837:Banian.  See  Bany£  or  Banyan.
AID.txt:860:Banyan.  A   corruption  of  Banyd.
AID.txt:861:Banyan.  The  name  given  in  English to  the  Indian  fig  tree — ficus  indica — known  in  Sanskrit  as  wata,  and  in the  vernaculars  as  wad  or  bar, whence  the  other  English  name burr .
HJB.txt:2850:BANYAN.
HJB.txt:2852:BANYAN,
HJB.txt:2871:BANYAN,
HJB.txt:2873:BANYAN.
HJB.txt:2897:BANYAN.
HJB.txt:2899:BANYAN-TREE,
AID.txt
HJB.txt
```


## [2026-10-17T00:03:13.127Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 24880,24895p KNT_full.txt; grep -n \"^van-\\|^ *van- \" KNT_full.txt | head; sed -n 830,866p AID.txt; grep -n \"BANYAN\" HJB.txt | head -3; grep -n -i \"^banian\\|^banyan\\|^ *banyan,\" KLN_1966.txt | head"
}
```


### [2026-10-17T00:03:13.559Z] TOOL RESULT

```
(1) ‘Cappadocia’: Katpatuka nsm. РВ 1.15f; 
DPe 12; DNa 28; DSe 27°; D8m 8^; XPh 26. 
(2) ‘Cappadocian’: Katpatuka пэш. A?P 21. 


ikan- vb. ‘dig’: Av. kan-, Skt. khan- ($100), . 
See also Adukanaiía-, kata-. ka*tanaiy ($238; 
NPers. kándón) inf. DZe 9; XV 21. akaniya imf, 
pass. ($113, $220) DSf 24, 28 (25, 29 read avaniya: 
see under van-); DZe 10°. 

ni- + kan- ‘destroy, obliterate’: пач imv. 
(§208, $237.IT) DB 4.80. 

vi- + kan- ‘dig apart, destroy’: viyakanam 1st 
28751:van- vb. ‘overpower, pack down’: Av. van- 
BANS
the  terms  of  which  the  fields  are divided  by  lot  every  six  years.
Bangash.  The  name  of  an  Afghdn tribe  settled  partly  within  the  British border  near  Kohat  and  partly  in  the Kuram  valley.
Banghy.  See  Bahangi.
Bangi.  Another  name  for  Banjogi.
Bangle.  [A  corruption  of  the  Hindu- stani bangri.1  A   bracelet.
Bangu.  The  river-thug  of  Bengal ; these  inveigle  people  into  their  boats, and,  after  strangling,  cast  them  into the  water  (//.  H.  Wilson ).
Banian.  See  Bany£  or  Banyan.
Bani  Israil.  [Arabic,  ibn,  a   son.] The  children  of  Israel,  the  name  by which  the  Afghans  proper  call  them- selves, and  also  the  name  of  a   small tribe  in  the  Konkan.  See  Beni  Israel.
Banik.  [Hindi.]  A   trader,  a   banker, a   money-changer,  a   banyd.
B&niyd.  The  Bengali  and  Panjabi form  of  Banyd.  It  is  said  that  the Bdniyds  of  the  Panjdb  are  a   sub- division of  the  despised  Chamdr caste,  and  that  they  still  privately worship  the  rdmpi,  the  symbol  of their  original  occupation.  The  Pan- jdb  Bdniyds  are  some  Vaishnawas and  some  Jains.
Baqj6r&.  [Hindi,  from  Sanskrit  banij,
’   a   trader.]  The  name  of  a   class  of traders  who  travel  over  the  country with  numerous  pack-bullocks,  carry- ing grain,  salt,  etc.,  from  market  to ^market.  Some  are  Hindus  and
/   some  Musalmdns.  Their  origin  is /obscure.  Lambdnis  and  Sukdlis  are often  spoken  of  by  this  name.
Banjdtrd.  [Hindi,  from  ban,  a   forest, and  jdtrd,  q.v.]  The  perambulation of  the  groves  sacred  to  Krishna  at Gowardhan,  near  Agrd,  made  by pilgrims  in  Bhddrapad.
Banjiga.  See  Banajiga.
Banjogi.  The  name  of  one  of  the Toungthd  tribes.  They  generally resemble  the  Lushais,  but  affirm that  they  are  sprung  from  the  Shans of  Burma.  They  acknowledge  a supreme  god  called  Patyen,  but  all their  reverence  and  sacrificial  rites are  directed  towards  Khozing,  the patron  deity  of  their  nation.  Unlike the  Lushais,  they  bury  their  dead without  first  drying  the  body,  and they  wear  their  knot  of  hair  on the  forehead  like  the  Shendus  and Kumis  (T.  H.  Lewin).
Bankar.  [Bengali,  from  bany  San- skrit, wana,  a   forest,  and  kar ,   re- venue.] Forest  produce,  such  as timber,  brushwood,  gum,  honey  ; also  the  privilege  of  cutting  wood, hunting,  and  fishing.
BAnkot  Knees.  Curved  teak  logs from  Bdnkot,  highly  prized  for  ship- building.
Bank6&l.  [Bengali,  from  the  San- skrit banik,  trade,  and  tdla,  a   house.] The  office  where  harbour  dues  and tolls  are  paid.
Bdns&i.  [Bengali,  from  bans,  a   bam- boo.] A   frame  of  bamboo-work used  as  a   harrow  for  breaking  clods after  ploughing.  *
Bansrij.  [Bengali,  Sanskrit  wanidja, from  wania ,   race,  and  ja,  born.]  Of good  family ;   the  title  given  to*the third  and  last  class  of  Gau<Ja  (sub- division) Brdhmans.
BANS
3i
BARA
Bdnaphor.  [Hindi,  from  bans,  a bamboo,  and  phor ,   to  split.]  The name  of  a   caste  who  make  baskets.
Bantar.  [Tulu.]  The  name  of  an agricultural  caste.  Many  have  mi- grated into  Coorg.  They  correspond to  the  Tamil  Velldlans  and  Malayd- lam  Nairs.
Bantarid.  [Hindi.]  A   class  of  wood- rangers  formerly  holding  rent-free land  in  quittance  of  police  duties,  in the  northern  parganas  of  Gorakhpur (H.  H.  Wilson).
Bantrotu.  [Telugu.]  A   peon,  a policeman.
Banyd.  [Hindi,  from  the  Sanskrit banik,  a   merchant.]  A   Hindu  trader, shopkeeper,  or  money-changer.  In Bengal  it  is  commonly  applied  to the  native  cashier,  or  man  of  busi- ness in  the  service  of  Europeans. In  the  west  of  India  it  ordinarily denotes  Hindu  merchants,  settled either  as  agents  or  principals  at  the chief  places  of  traffic  in  the  Persian Gulf  or  Red  Sea  (H.  //.  Wilson ). See  Wdni.
Banyan.  A   corruption  of  Banyd.
Banyan.  The  name  given  in  English to  the  Indian  fig  tree — ficus  indica — known  in  Sanskrit  as  wata,  and  in the  vernaculars  as  wad  or  bar, whence  the  other  English  name burr .
Bdogi."  [Mardfhi.]  A   well,  either with  or  without  a   flight  of  steps leading  to  the  water.
Bdoli,  Bdori.  [Hindi,  from  the  San- skrit wdpiy  a   large  oblong  pond  ; intermediate  forms  are  found  in wdOy  wdotfi,  and  bdodi.]  A   well  with a   flight  of  steps  leading  down  to  the
surface  of  the  water ;   these  are often  elaborate  constructions,  with landing-places  and  chambers  at different  levels.  Also  the  well-room of  a   palace.
Bdori.  [Hindi.]  A   vagrant  tribe  in the  Bhatti  country  and  west  of Delhi,  and  in  Tonk  and  Jdipur,  who are  professional  thieves  and  very bold  and  skilful  ;   they  go  armed  to commit  open  raids  on  villages,  and use  disguises,  especially  that  of  the jogi,  to  effect  secret  thefts.  They enter  houses  by  digging  a   hole  in the  wall  near  the  bar  of  the  door, and  so  opening  it.
Bdr.  [Panjdbi.]  Desert  or  forest land  ;   especially  the  central  table- land of  the  Chaj  Jetcli  dodb.
2850:BANYAN.
2852:BANYAN,
2859:(1)  BANYAN,  s.  a.  A  Hindu trader,  and  especially  of  the  Province of  Quzerat,  many  of  which  class  have for  aces  been  settled  in  Arabian  ports And  Imown  by  this  name  ;  but  the term  is  often  applied  by  early  travellers in  Western  India  to  persons  of  the Hindu  religion  generally.  b.  In Calcutta  also  it  is  (or  pernaps  rather was)  specifically  appliea  to  the  native brokers  attached  to  houses  of  business, or  to  persons  in  the  employment  of a  private  gentleman  doing  analogous duties  (now  usually  called  sircar).
4385:banian,  n.,  a  Hindu  merchant.  —  Hind,  vanija. ‘a  trader’,  fr.  OI.  vanij,  ‘merchant’.  Cp.  bany¬ an  tree.
4409:banyan  tree,  also  banyan,  n.  —  Orig.  ‘the  tree under  which  the  banyans  (=  Hindu  merchants) settled  near  Gombroon  (now  called  Bandar Abbas);  see  banian.  See  Yule-Buinell,  Hobson- Jobsen,  p.65.
```


## [2026-10-17T00:03:17.668Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28751,28760p KNT_full.txt; sed -n 2859,2875p HJB.txt | cut -c1-600; sed -n 2895,2905p HJB.txt | cut -c1-700; grep -n \"^vomit,\\|^vomit \" KLN_1966.txt SKT.txt | head; grep -n \"^wem-\\|^wen-1\\|^wen-\" AHD_watkins1985.txt | head"
}
```


### [2026-10-17T00:03:18.094Z] TOOL RESULT

```
van- vb. ‘overpower, pack down’: Av. van- 
‘superare’, pres. vanaiti (Bthl. AiW 1350 ал; cf. 
JAOS 53.15-6, Wb. AfOF 7.41, Hz. ApI 346-7), 
Skt. vdnati ‘desires, gets by effort, Gt. winnan 
‘suffer’, NEng. win. — avaniya imf. pass. ($220) 
DSf 25, 29 (not akaniy, as read by Scheil 21.26; 
König, Burgbau 32; Hz. AMI 3.49, 54; Schaeder, 
Ung. Jrb. 15.562). 


(1)  BANYAN,  s.  a.  A  Hindu trader,  and  especially  of  the  Province of  Quzerat,  many  of  which  class  have for  aces  been  settled  in  Arabian  ports And  Imown  by  this  name  ;  but  the term  is  often  applied  by  early  travellers in  Western  India  to  persons  of  the Hindu  religion  generally.  b.  In Calcutta  also  it  is  (or  pernaps  rather was)  specifically  appliea  to  the  native brokers  attached  to  houses  of  business, or  to  persons  in  the  employment  of a  private  gentleman  doing  analogous duties  (now  usually  called  sircar).
The  word  was  adopted  from  Vaniya, a  man  of  the  trading  caste  (in  Qujarati vdniyo\  and    that    comes    from    Skt. tamj,    *a    merchant.'    The    terminal nasal  may  be  a  Portumiese  addition (as  in  poUanquin,  rnaruMrin,  Bassein), or  it  may  be  taken  from  the  plural form  vdwiydn.     It  is  probable,  how- ever, that  the  Portuguese  found  the word    already    in    use    by    the  Arab traders.    Sidi  'Ali,  the  Turkish  Admi- ral, uses  it  in  precisely  the  same  form, applyin£[  it  to  the  Hindus  generally ; and  m  Uie  poem  of  Sassui 
volte  il  giomo  "  (251).  See  also  Luillier below.  The  men  of  this  class  profess an  extravagant  respect  for  animal  life  ; but  after  Stanley  brought  home  Dr. Livin^tone's  letters  they  became notorious  as  chief  promoters  of  slave- trade  in  Eastern  Africa.  A.  K.  Forbes speaks  of  the  medieval  W&nias  at tne  Court  of  Anhihvara  as  "equally gallant  in  the  field  fwith  Bajputs), and  wiser  in  council  .  .  .  already in  profession  puritans  of  peace,  hut not  yet  drainea  enough  of  their  fiery Kshatri  h\ood."—{Rds  Mala,  i.  240; [ed.  1878
Bunya  is  the  form  in  which  vdniya appears  in  the  Anglo-Indian  use  of Bengal,  with  a  different  shade  of  mean- ing, and  generally  indicating  a  grain- dealer.
1516. — "There  are  three  qualities  of  these Gentiles,  that  is  to  say,  some  are  called Razbuts  .  .  .  others  are  called  Hiiwlitw, and  are  merchants  and  traders." — Barboaa, 61.
1552. — ".  .  .  Among  whom  came  cer- tain men  who  are  called  Baneanew  of the  same  heathen  of  the  Kingdom  of Cambaia  .  .  .  coming  on  board  the  ship of  Vasco  da  Gama,  and  seeing  in  his  cabin a  pictorial  image  of  Our  Lady,  to  which  our pMOople  did  reverence,  they  also  made  adora- tion with  much  more  fervency.  .  .  ." — Bcarrosy  Dec.,  I,  liv.  iv.  cap.  6.
1555.— "We  may  mention  that  the  in- habitants of  Guzerat  call  the  unbelievers Banyftns,  whilst  the  inhabitants  of  Hindu- stan call  them  HindiL" — Sidi  'Afi  Kapuddtu in  J.  As.,  1*«  S.  ix.  197-8.
1563.— "A.  If  the  fruits  were  all  as  good as  this  (mango)  it  would  be  no  such  great matter  in  the  Baneanes,  as  you  tell  me, not  to  eat  flesh.  And  since  I  touch  on this  matter,  tell  me,  prithee,  who  are  these BanaanOB  .  .  .  who  do  not  eat  flesh  i  .  .  .  " —Garcia,  f .  186.
1608.— "The  Gouemour  of  the  Towne  of Gfandeuee  is  a  BaOBjUi*  and  one  of  those kind  of  people  that  obserue  the  Law  of Pythagoras." — Jone*,  in  Purcha*^  i.  231.
[1610.—"  Baaeanei. "  See  quotation  under Bi^KSHALL,  a.]
1623. — "One  of  these  races  of  Indians  is that  of  those  which  call  themselves  VaniA, but  who  are  called,  somewhat  corruptly  by the  Portuguese,  and  by  all  our  other  Franks, Banians;  they  are  all,  for  the  most  port, traders  and  brokers." — P,  della  Valle,  i. 486-7  ;  [and  see  i.  78  Hak.  Soc.].
1630.— "A  people  presented  themselves to  mine  eyes,  cloathed  in  linnen  garments, somewhat  low  descending,  of  a  gesture  and garbe,  as  I  may  sov,  maidenly  and  well nigh  effeminate;  of  a  countenance  shy, and  somewhat  estranged  ;  yet  smiling  out a   glosed   and    bashful   familiarity.  ...  I
BANYAN,
64
BANYAN.
asked  what  manner  of  people  these  were, so  strangely  notable,  and  notably  strange. Reply  was  made  that  they  were  Bazdaas." —Lardy  Preface.
1665. — **In  trade  these  Ha-winTia  are  a thousand  times  worse  than  the  Jews;  more expert  in  all  sorts  of  cunning  triclu.  and more  maliciously  mischievous  in  their  re- venffe."— TViwnittT,  E.  T.  ii.  68 ;  [ed.  Balf, i.  136,  and  see  i.  91].
(2).  BANYAN,  8.  An  undershirt, originally  of  muslin,  and  so  called  as resemblinc  the  body  garment  of  the Hindus ;  but  now  commonly  applied to  under  body-clothing  of  elastic  cotton, woollen,  or  silk  web.  The  following quotations  illustrate  the  stages  by which  the  word  reached  its  present application.  And  they  show  that our  predecessors  in  India  used  to adopt  the  native  or  Banyan  costume in  their  hours  of  ease.  C.  P.  Brown defines  Banyan  as  **a  Uxm  dressing- gowny  such  as  Hindu  tradesmen  wear." Probably  this  may  have  been  the original  use ;  but  it  is  never  so  em- ployed in  Northern  India.
1672.— "It  is  likewise  ordered  that  both Officers  and  Souldiers  in  the  Fort  shall,  both
BANYAN.
65
BANYAN-TREE,
on  every  Sabbath  Day,  and  on  eyory  day when  they  ezerciae»  iMore  Bmglitk  ajppaard ; in  respect  the  garbe  is  most  becoming  as Souldien,  and  oorrespondent  to  their  prof  es- aon." — Sir  W,  Langhome*t  SUmdvug  Order ^ in  Wke^er,  m,  426.
1731. — "The  Bnaign  (as  it  proved,  for  his fint  appearance,  being  undressed  and  in  his bansroa  coat,  I  did  not  know  him)  came  off from  his  cot^  and  in  a  ver^  haughfy  manner cried  oat,  *None  of  your  disturbance,  Grentle- men.'  "—In  Wheeler,  iii.  109.
1781.— "I  am  an  Old  Stager  in  this Gonntrv.  having  arrived  in  Calcutta  in  the Year  1796.  .  .  .  Those  were  the  days,  when Gentlemen  studied  Etue  instead  of  Fcukion  ; when  even  the  Hon.  Members  of  the  Ooundl met  in  Baaym  Shirta,  Loo^  Drawen  (q.  v. ), and  OoDJee  (Congee)  cape ;  with  a  Case  Bottle of  good  old  Arrack,  and  a  (buglet  of  Water placed  on  the  Table,  which  we  Secretary (a  SkUfal  Hand)  frequently  converted  into Punch  .  .  . " — Letter  from  An  Old  Country Cb^tem,  in  India  Oazettey  Feb.  24th.
[1773.— In  a  letter  from  Horace  Walpole to  the  Countess  of  Upper  Ossory,  dated April  30th,  1773  {Chtnntnfham't  ed.,  v.  459) he  describes  a  ball  at  Lord  Stanley's,  at which  two  of  the  dancers,  Mr.  Storer  and Miss  Wrottealey,  were  dressed  "in  l>anian8 with  furs,  for  winter,  cock  and  hen."  It would  be  interesting  to  have  further  details of  these  garments,  which  were,  it  may  be hoped,  different  from  the  modem  Banyan.]
1810. — ".  .  .  an  undershirt,  commonly called  a  hKl^B3L"—Wiiliams(m,  V.M.  i.  19.
(3)   BANYAN,  s. TBEE.
```


## [2026-10-17T00:03:26.097Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=28700 && NR<=28800 && /^ *2[01][0-9] *$/' KNT_full.txt; awk 'NR>=28700 && NR<=28800 && /LEXICON|Lexicon/ {print NR\": \"$0}' KNT_full.txt | head -3; sed -n 2905,2930p HJB.txt | cut -c1-900; grep -n \"^wem\\|^wen\\|^ *wem-\\|^ *wen-\" AHD_watkins1985.txt IEC.txt | head"
}
```


### [2026-10-17T00:03:26.747Z] TOOL RESULT

```
(3)   BANYAN,  s. TBEE.
See  BANYAN-
BANYAN-DAY,  8.  This  is  sea- slang  for  a  jour  maigre,  or  a  day*  on whidi  no  ration  of  meat  was  allowed  ; when  (as  one  of  our  quotations  above expresses  it)  the  crew  had  "  to  observe the  Law  of  Pythagoras."
1600.— "Of  this  {Kitckery  or  Kedgeree, q.v.)  the  European  Sailors  feed  in  these  parts once  or  twice  a  Week,  and  are  forcxl  at those  times  to  a  Pagan  Abstinence  from Flesh,  which  creates  in  them  a  perfect  Dis- like and  utter  Detestation  to  those  Hii«i«<ftTi OajB,  as  they  commonly  call  them." — iMnffton,  310,  811.
BANYAN-FIGHT,  8.    Thus:
1690. — "This  Tongue  Tempest  is  termed there  a  Bantllan-Ftght,  for  it  never  rises to  blows  or  bloodshed."— (M'n^ton,  275.  Sir O.  Birdwood  teUs  us  that  this  is  a  phrase -etill  current  in  Bombay.
BANYAN-TBEE,  also  ellintically
BauDyan,    s.     The    Indian    Fi^-Tree
(Fietu  Indiea^  or  Ftcus  beng<densi8j  L.X
42alled  in  H.  bar  [or  bargalf  the  latter
E
the  ^^Bourgade**  of  Bemier  (ed.  Con- gtabUy  p.  309).]  The  name  appears  to have  b«en  first  bestowed  popularly  on a  famous  tree  of  this  species  jo^wing near  Gtombroon  (q.v.),  under  which  the Banyans  or  Hindu  traders  settled  at that  port,  had  built  a  little So  says  Tavernier  below, original  Banyan-tree  is  described  by P.  della  Valle  (ii.  453),  and  by Valentijn  (v.  202).  P.  della  VaUe^s account  (1622)  is  extremely  interesting, but  too  long  for  quotation.  He  c^ls it  by  the  Persian  name.  liU,  The  tree still  stood,  within  half  a  mile  of  the English  factory,  in  1758,  when  it  was visited  by  Ives,  who  Quotes  Tickell's verses  given  below.  [Also  see  CUBEEB BUBB.]
c.  A.D.  70.— "First  and  foremost,  there  is a  Fig-tree  there  (in  India)  which  beareth very  small  and  slender  figges.  The  propertie of  wis  Tree,  is  to  plant  and  set  it  selfe  with- out mans  helpe.  For  it  spreadeth  out  with mightie  armes,  and  the  lowest  water-boaghes underneath,  do  bend  so  downeward  to  the very  earth,  that  they  touch  it  againe,  and lie  upon  it:  whereby,  within  one  years  space they  will  take  fast  root  in  the  nonnd,  and put  foorth  a  new  Spring  round  about  the Mother- tree:  so  as  these  braunches,  thus growing,  seeme  like  a  traile  or  bonder  of arbours  most  curiously  and  artificially  made, " &c. — Plinia  Nat,  Mittoriey  by  PlUlemon Holland,  i.  860.
1624.—
'' .  .  .  The  ^oodljr  bole  being  got To  certain  cubits'  height,  from  every  side The  boughs  decline,   which,  taking  root
afresh, Spring  up  new  boles,  and  these  spring
new,  and  newer, Till  the  whole  tree  become  a  porticus. Or  arched  arbour,  able  to  receive A  numerous  troop."
Ben  Jonsorij  Neptune* s  Triumph,
c.  1650. — **Cet  Arbre  estoit  de  mdme espece  que  celuy  qui  est  a  une  lieue  du Bander,  et  qui  passe  pour  une  merveille ; mais  dans  les  Inaes  il  y  en  a  quantity.  Les Persans  I'appellent  Luly  les  Portugais  Arher de  ReySj  et  les  Francais  I'Arbre  des  Bani- aOM ;  paroe  que  les  Banianes  out  fait  b&tir deasous  une  Paf ode  avec  un  carvansera aocompagn^  de  piusieurs  petits  ^tangs  poiur se  laver/' — Tavernier,  V.  de  Perse^  liv.  v. ch.  23.    [Also  see  ed.  ^aZ/,  ii.  198.]
c.  1660.— "Near  to  the  City  of  Ormut  was a  Bannianii  tree^  hein^  the  only  tree  that grew  in  the  Island.'*— Jtoucmicr,  Eng.  Tr.  i.
c,  1666. — "Nous  vimes  k  cent  on  cent dnquante  pas  de  ce  jardin,  I'arbre  War  dans toute  son  etenduS.  On  I'appeUe  auasi  Ber, et  arbre  des  Banians,  et  arbre  det  racinet .  .  .    "—Thevenot,  v.  76.
BANYAN^TREE.
BANYAN'TBEE,
1667.— '*  The  fig-tree,  not  that  kind  for  fruit  re- nown'd; But  such  as  at  this  day,  to  Indians  known, In  Malabar  or  Decan  spreads  her  arms Branching  so  broad  and  long,  that  in  the
ground TIm  bended  twigs  take  root,  and  daughters
grow About  the  mother-tree,  a  pillared  shade High  OTor-arch'd,  and  eciioing  walks  be- tween." ParadUe  Loat^  iz.  1101.
```


## [2026-10-17T00:03:31.566Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^wem\\|^wen\\|^ *wem\\|^ *wen[-ə1]\" AHD_watkins1985.txt | head; grep -n -i \"vomit\\|banyan\\|banian\" AHD_watkins1985.txt | head; grep -n -i \"vomit\" IEC.txt SYN.txt | head -8; grep -n -i \"^vomit\" SKT.txt KLN_1966.txt | head"
}
```


### [2026-10-17T00:03:32.233Z] TOOL RESULT

```
55:Those dialects or branches of Indo- European still represented today by one or more languages are Indo-Iranian, Greek, Ar- menian, Slavic, Baltic, Albanian, Celtic, Italic, and Germanic. The present century has seen the addition of two branches to the family, neither of which has left any living trace: Hittite and other Anatolian languages, the earliest attested in the Indo-European family, spoken in what is now Turkey in the second millennium B.c.; and the two Tochar- ian languages, the easternmost of Indo- European dialects, spoken in Chinese Turke- stan (present-day Xinjiang) in the first mil- lennium A.D.
66:A number of Indo-European languages show a similar word for the kinship term “daughter-in-law”: Sanskrit snusd, Old Eng- lish snoru, Old Church Slavonic snikha (Russian snokhd), Latin nurus, Greek nuos, and Armenian nu. Albanian has nuse in the meaning “bride,” a meaning shared by the Armenian form. In a patrilocal and patriar- chal society (such as most, if not all, early Indo-European-speaking societies), where the bride went to live in her husband’s fa- ther’s house, “daughter-in-law” and “bride” were equivalents.
69:in showing an Indo-European word that be- gan with sn-. We know that an Indo- European s was lost before n in other words in Latin, Greek, Armenian, and Albanian, so we can confidently assume that Latin nurus, Greek nuds, Armenian nu, and Albanian nuse go back to an Indo-European *sn-. (Compare Latin nix (stem niv-), “snow,” with English SNOw, which preserves the s.) This principle is spoken of as the regularity of sound corre- spondences; it is basic to the sciences of etymology and comparative linguistics.
70:Sanskrit, Latin, Greek, Armenian, and Al- banian agree in showing the first vowel as -u-. We know from other examples that Slavic w regularly corresponds to Sanskrit u and that Germanic o (of Old English snoru) in this position has been changed from an earlier u. It is thus justifiable to reconstruct an Indo-European word beginning *snu-.
71:For the consonant originally following *snu-, closer analysis is required. The key is furnished first by the Sanskrit form, for we know there is a rule in Sanskrit that s always changes to s (a sh-like sound) after the vowel u. Hence a Sanskrit snus- must go back to an earlier *snus-. In the same position, after u, an old s in Slavic changes to kh (like the chin Scottish loch or German ach); hence the Slavic word, too, reflects *snus-. In Latin always, and under certain conditions in Ger- manic, an old -s- between vowels became -r-. For this reason Latin nurus and Old English snoru may go back to older *snus- (followed by a vowel) as well. In Greek and Armenian, on the other hand, an old -s- between vowels disappeared entirely, as we know from nu- merous instances. Greek nuds and Armenian nu (stem nuo-) thus regularly presuppose the same earlier form, *snus- (followed by a vowel). Finally, that -s- between vowels is still preserved—almost accidentally, one might say—in Albanian nuse. All the com- parative evidence agrees, then, on the Indo- European root form *snus-.
897:reu-2, Also reue-. To smash, knock down, tear out, dig up, uproot. 1. Suffixed o-grade form *rous-o- in Ger- manic *rawwa- in: a. Old Norse régg, réggr, woven tuft of wool: RAG}; b. Norwegian rugga, rogga, coarse cover- let, akin to the Scandinavian source of RUG. 2. Basic form *reu- in Latin ruere, to collapse, cause to collapse: RABBLE, RUIN. [Pok. 2. reu- 868.] reudh-', Red, ruddy. I. O-grade form *roudh-. 1. Ger- manic “raudaz in: a. Old English réad, red: RED; b. Old Norse rauthr, red (> reythr, rorqual): RORQUAL. 2. Ger- manic *raudnia- in Old Norse reynir, mountain ash, rowan (from its red berries), akin to the source of ROWAN. 3. Latin rijfus (of dialectal Italic origin), reddish: RUFES- CENT, RUFOUS. 4. Latin rdbus, red, in robigd, ribigo, rust: RUBIGINOUS. 5. Latin rdbur, rdbus, red oak, hard- ness, and rdbustus, strong: ROBLE, ROBORANT, ROBUST; CORROBORATE, RAMBUNCTIOUS. II. Zero-grade form *rudh-. 1. Form *rudh-d- in Germanic *rud6 in: a. Old English rudu, red color: RUDDLE, RUDDY; b. Old English rudduc, robin: RUDDOCK. 2. Suffixed form *rudh-sto- in Germanic *riist- in Old English rdst, rust: RusT. 3. Latin rubeus, red: ROUGE, RUBEOLA, RUBY; RUBEFACIENT 4. Latin rubicundus, red, ruddy: RUBICUND. 5. Latin rubidus, red: RUBIDIUM. 6. Suffixed (stative) form *rudh-é- in Latin rubére, to be red: RUBESCENT; ERUBES- CENCE. 7. Suffixed form *rudh-ro- in: a. Latin ruber, red: RUBELLA, RUBRIC; BILIRUBIN; b. Latin rutilus, reddish: RUTILANT; Cc. Greek eruthros, red (with pro- thetic vowel, from oldest root form *sreudh-): ERY- THEMA, ERYTHRO-; d. possibly remade Greek erusi-, red, reddening: ERYSIPELAS. 8. Suffixed form *rudh-to- in Latin russus, red: RISSOLE, ROUX, RUSSET. [Pok. reudh- 872.] reudh-2, To clear land. 1. Suffixed zero-grade form *rudh-yo- in Germanic *rudjan in Old Norse rydhja, to clear land: RID. 2. Possibly Germanic expressive variant *rudd- stick, club, in Old English rodd, stick: Rop. [In Pok. 2. reu- 868.] reue-. To open; space. 1. Suffixed variant form *ri-mo- (< *rua-mo-) in Germanic *riimaz in: a. Old English rim, space: ROOM; b. Old French run, ship’s hold, space: RUMMAGE. 2. Suffixed form *reu(g)-es- in Latin ris, “open land,” the country: RURAL, RUSTIC. [Pok. reuo-, ri- 874.] reug-. To vomit, belch, smoke, cloud. 1. Germanic *reu- kan in Old English réocan, to smoke, reek: REEK. 2. Suf- fixed zero-grade form *rug-to- in Latin ructdre, to belch: ERUCT. [Pok. 4. reu- 871.] reugh-men-. Cream. O-grade form *roughmen- in Ger- manic *rau(g)ma- in Middle Low German rém(e), cream: RAMEKIN. [Pok. reugh-m(e)n- 873.] reup-. Also reub-. To snatch. I. Basic form *reub- in Germanic *rupja in Flemish rippen, to rip: RIP!. II. O-grade form *roup-. 1. Germanic *raufjan in: a. Old English réafian, to plunder: REAVE!; b. Old English beréafian, to take away (be-, bi-, intensive prefix; see ambhi): BEREAVE. 2. Germanic *raubén, to rob, in: a. Middle Dutch and Middle Low German réven, to rob: ROVER; b. Old French rober, to rob: ROB; c. Italian rubare, to rob: RUBATO. 3. Germanic *raubd, booty, in Old French robe, robe (> “clothes taken as booty”): ROBE. 4. Suffixed form *roup-tro- in Sanskrit loptram, booty, from lumpati, he breaks, removes: LOOT. III. Zero-grade form *rup-. 1. Latin dsirpdre (< *isu- rup-; isus, use, usage, from iti, to use), originally “to interrupt the orderly aquisition of something by the act of using,” whence to take into use, usurp: USURP. 2. Na- salized form *ru-m-p- in Latin rumpere, to break (> riipés, rock): ROUT!, RUPTURE; ABRUPT, BANKRUPT, CORRUPT, DISRUPT, ERUPT, INTERRUPT, IRRUPT, RUPICO- Lous. [Pok. 2. reu- 868.] rezg-. To plait, weave, wind. Germanic *ruski- in Old English risc, rysc, rush: RUSH?. [Pok. rezg- 874.] [risan. To rise. Germanic word. 1. Germanic *risan in:
1142:HELMINTH; ANTHELMINTIC, PLATYHELMINTH. [Pok. 7. uel- 1140.] wel-‘, To tear, pull. 1. Suffixed form *wel-do- in Latin vellere, to tear, pull: AVULSE, CONVULSE, DIVULSION, EVULSION, REVULSION, SVELTE. 2. Suffixed form *wel-no- in Latin vullis, shaggy hair, wool: VELOURS, VELVET, VILLUS [Pok. 8. wel- 1144.] wele-'. Wool. Probably related to wel-‘. 1. Suffixed extended zero-grade form “*wi-nd- in: a. Germanic *wullé in Old English wul(l), wool: woot; b. Italic *wland in Latin lana (> French laine), wool, and its derivative laénig6, down: LANATE; DELAINE, LANIFER- OUS, LANOLIN, LANUGO; ¢. Celtic *wland in Welsh gwlan, wool (> Middle English flannel, woolen cloth): FLANNEL. 2. Possible suffixed o-grade form *wol(o)-no- in Greek oulos, wooly, curly: ULoTRICHOUs. [Pok. 4. uel- 1139.] wela-2. To strike, wound. 1. Suffixed o-grade form *wol()-o- in Germanic *walaz in Old Norse valr, the slain in battle in: a. Old Norse Valhdéll, Valhalla: VAL- HALLA; b. Old Norse Valkyrja, “chooser of the slain,” name of one of the twelve war goddesses (-kyrja, chooser; see geus-): VALKYRIE. 2. Suffixed basic form *welo-nes- in Latin vudnus (stem vulner-), a wound: VULNERABLE. [In Pok. 8. wel- 1144.] welg-. Wet. Germanic *welk- in: a. Old English wolc(e)n, cloud, sky: WELKIN; b. Middle English welken, to wilt: wILT!. [Pok. 2. welk-, uelg-, 1145.] welt-. Woods; wild. 1. Suffixed form *wolt-u- in Germanic *walthuz in: a. Old English weald, wald, a forest: WEALD, WOLD!; b. Old Norse vdllr, field: VOLE!. 2. Ger- manic *walthdn- in Middle English welde, a plant yield- ing a yellow dye, weld: WELD2. 3. Germanic *wilthigaz in: a. Old English wilde, wild: wip; b. Old English wildéor, wilddéor, wild beast (déor, animal; see dheu-'): WILDERNESS; C. Dutch wild, wild: WILDEBEEST. [In Pok. 4. uel- 1139.] weme-. To vomit. 1. Germanic *wam- in Old Norse vamla, qualm, and Danish vamle, to become sick, prob- ably akin to the Scandinavian source of Middle English wam(ejlen, to feel nausea, stagger: WAMBLE. 2. Latin vomere, to vomit: NUX VOMICA, VOMIT. 3. Greek emein, to vomit: EMESIS, EMETIC. [Pok. wem- 1146.] wen-', To desire, strive for. 1. Suffixed form *wen-w- in Germanic *winn(w)an, to seek to gain, in Old English winnan, to win: WIN}. 2. Suffixed zero-grade form *wn-ydé in Germanic *wunjé in Old English wynn, wen, pleasure, joy: WEN2, WINSOME. 3. Suffixed (stative) zero-grade form *wn-é-, to be contented, in Germanic *wunén in Old English wunian, to become accustomed to, dwell: won!, (wont). 4. Suffixed (causative) o-grade form *won-eyo- in Germanic *wanjan in Old English wenian, to accustom, train, wean: WEAN}. 5. Germanic *wéniz, hope, with denominative *wénjan, to hope, in Old English wénan, to expect, imagine, think: WEEN. 6. Suffixed zero-grade form *wn-sko- in Germanic *wunsk- in Old English wyscan, to desire, wish: WISH. 7. O-grade *won- perhaps in Germanic *wani- in: a. Old Norse Vanir, the Vanir: VANIR; b. Old Norse vana- in Vanadis, name of the goddess Freya: VANADIUM 8. Suf- fixed form *wen-es- in: a. Latin venus, love (> venerari, to worship): VENERATE, VENEREAL, VENERY!, VENUS; b. suffixed form *wen-es-no- in Latin venénum, love potion, poison: VENOM. 9. Suffixed form *wen-eto-, “be- loved,” possibly in Germanic *Weneda-, a Slavic people, in Old High German Winida, the Wends: WEND. 10, Suffixed form “wen-yd@ in Latin venia, favor, forgive- ness: VENIAL. 11. Lengthened-grade form *wén-d- in Latin véndri, to hunt: VENATIC, VENERY2, VENISON. 12. Suffixed basic form *wen-o- in Sanskrit vanam, forest: WANDEROO. 13. Possibly zero-grade suffixed form *wn-ig- in Sanskrit vanik, vdnijah, merchant (? < “seek- ing to gain”): BANIAN. [Pok. 1. ven- 1146.] wen-2. To beat, wound. 1. Suffixed zero-grade form
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
2457:VOILE weg-! VOIR DIRE wéro- VOLANT gWel-2 VOLATILE gWel-2 VOLE! welt- VOLE? gWel-2 VOLITANT gWel-2 VOLITION wel-2 VOLKSLIED léu-2 VOLLEY gWel-2 VOLT? wel-3 VOLUBLE wel-3 VOLUME wel-3 VOLUNTARY wel-2 VOLUPTUARY wel-2 VOLUPTUOUS wel-2 VOLUTE wel-3 VOLUTIN wel-3 VOLVA wel-3 VOLVOx wel-3 VOMER wogWh-ni- VOMIT weme- VORACIOUS gWere-4 VORLACE legh-, per! -VOROUS gWere-4 VORTEX wer-3 VOTARY wegh- VOTE wegWh-
IEC.txt:1015:būgð, ið “blast Gk. búzö (2), aor: ébuxa, v. id. beside büktes, adj. ‘blustering; MHG pfüchen 'spit; G pfauchen, v. id.; E to puke, v. ‘vomit
IEC.txt:1381:bhleuóo, ið “blow, bellow, belch, gush’. WP II, 212-4. Cf. bhluso Gk. phléo, phleúð; Lat. fluo, ére (here, de- spite pf. flüxi, sup. fluctum?); OCS bljujo, bljuvati ‘vomit, spew’; R bljuju, blevat,, id.; Li. bliauju, bliauti ‘bleat’; Late blauju, blaut (id. E *bluster). A long-grade form occurs in Li. bliüvà ‘bellowing’
IEC.txt:1438:in view of fluvius, ef-fluus, fluvidus & flu- idus); OCz. blváti, Cz. blevati; Blg. blávam, bálvam ‘spew, vomit. Cf. also Cz. blvoň ‘booby’. Cf. bhleuo
IEC.txt:1697:bhroulios, iə ‘seething, brew, surge’ Br. brülľ’, pl. brüP u ‘wave, billow; brew, soup’; brül'a v. ‘vomit’; OCS brulja ‘fountain’. (For a possible verbal prototype, cf. OCS brujọ, ati ‘roar’; Li. bráujuos, bráutis “rush?). A zero-gde occurs in Srb. břlļjati ‘pother’. Norw. bröle ‘roar’ is prob. fr. LG
IEC.txt:4093:Gk. glíkhomai ‘cling’; Hes. glikhós ‘niggardly, fussy’; ON klígja ‘nausea’, v. ‘vomit
IEC.txt:5115:guågh-, guåghsið ‘heave, be about to vomit, cough' Gk. bëssð ‘cough’; béx, gs békhós, s. id.; Li. góg3iu, eti ‘heave to vomit
IEC.txt:8084:krko, io ‘hawk, reach, belch; screech, croak, caw’. Cf. karko, kurk- Skt. cf. krkah ‘throat’; Lat. corcus, 1 ‘rumble in stomach’; corcinor, ari, v. id.; Gaul. cf. (am- big.) -cricon- (throat, in an exorcism); W (ambig.) cryg, adj. ‘hoarse’; crygu. v (‘be hoarse’, prob. fr. krik-, q.v.); OE horgian, horian, hyran ‘hawk, cough’; Big. krákam, kár- kam ‘gulp’; Srb. křčati ‘rumble in bowels; rattle in throat’; OCz. krcéti vomit? beside Cz. krkat ‘belch’; OCS (and com. S1.) krükü *throat'; Li. kirkiü, ti ‘screech’ beside Kark, kurkiü ‘cackle’ (variants); Latv. cf. kirkstet, inf. ‘cluck, chirp’
IEC.txt:14556:reugõ, ið (reug-mi, rüg-) ‘roar, fume, bellow, rage, belch, vomit’. WP II, 357 Arm. cf. orkor, o-st. (throat, fr. *rugeuo-); Gk. ereügomai, v. ‘belch, vomit’; OLat. cf. erugoó, ére, cpd. id. (Fest.); cf. Lat. e-ructus, pp. & adj. (belched', whence eructo, åre, v.); OHG riuhhan, MHG riechen, sv. 2. ‘belch - smoke; reek, steam’; (long-zero-gde in) rū- chen, v. ‘belch — smoke’; OE reocan, sv. 2. ‘reek, fume’; cf. reoc, adj. ‘raging’; Du. rieken, intr. as MHG riechen (2) ‘smell’; ON rjúka, sv. 2. ‘reek’; (o-gde) Gothic inrauhtjan, inf. ‘rage, fume’; (long-zero-gde in) OCS rygajo, v. ‘vomit’; (e-gde in) OCz. říhati (late form for *rühati? *fart); Cz. ríhat ‘belch’; OLI. riaügmi, Li. riaugiü, ti, v. beside raugiü, ti, and riaugü, æti and raugu, eti, id.; Late raugu, inf: raudzit, id. beside raugas, fpl. ‘belching’
SKT.txt:21053:Vomit,  sb.  (L.)  L.  uomihu,  a  vomiiing ; whence  ucmitart^  to  vomit  —  L.  uemirust pp.  of  vcmrrr,  to  vomtt.  4*  Ok.  l/ifiv,  Skt. vam,   to  vomit,  (V  WAM.)
```


## [2026-10-17T00:03:39.408Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^vomit\\|^Venus\\|^venison\\|^win, \\|^win \" KLN_1966.txt | head; grep -n \"^ *uemō\\|^ *uemo\\|^ *uenō\\|^ *ueno\\|^ *u̯em\\|^ *u̯en\" IEC.txt | head"
}
```


### [2026-10-17T00:03:40.353Z] TOOL RESULT

```
41216:venison,  n.,  the  flesh  of  a  deer.  —  ME.  veneson, veneison,  venison,  fr.  OF.  veneson,  veneison  (F. venaison),  fr.  L.  venatidnem,  acc.  of  venatio, ‘hunting,  chase',  fr.  venatus,  pp.  of  venari,  ‘to hunt’.  See  venery,  ‘hunting’.
19984:uemoó, ið ‘vomit’. Onomat. WP I, 262 Skt. vàmami & vámimi, v. id.; Av. vam-, id.; Oss. wáàmin, pp: wámd, id.; Gk. eméo, emoü- mai, id.; Lat. vomo, ére, id.; Icel. (long-gde) væma, v. (“be il esp. in mig vaemir “I feel nausea); ON váma, f. ‘nausea’; Sw. vámjas, v.; Li. vemiü, vernti, v. vomit; Latv. vemju, vemt, id. (Isophonic extn. with long vowel in Skt. vàmalürah 'ant-hil?, and Li. vemalai, mpl. vomit)
20007:uenos, -es- ‘desire’. Cf. uén- (1) and WP I, 259 Skt. vanas, n. ‘loveliness’ beside vanā & vanih, f. id.; vanús, adj. ‘keen; loving’; Lat. Venus, gs: -eris, f. ‘Venus’; beside vinulus & vinnulus, adj. ‘dainty; wanton’; W gwên, pl. gwenau, f. “smile”, cf. Gweno, f. “evening star, Venus’; (z-gde in) OHG wunja, MHG wunne, wünne, f. (2) joy’; OE wynn, f. ‘delight’; cf. wyn-sum ‘winsome’. (FK:EWDS untenable: Wonne). See next
```


## [2026-10-17T00:03:44.933Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^vomit\\|^ *vomit, \" KLN_1966.txt KLN_1971.txt | head -3; grep -n \"Av\\. *vam\\|Avest\\. *vam\" KLN_1966.txt | head; grep -n \"Av\\. *vanaiti\\|vanaiti\" KLN_1966.txt | head"
}
```


### [2026-10-17T00:03:45.576Z] TOOL RESULT

```
KLN_1971.txt:81251:vomiting. 
KLN_1971.txt:107632:vomit; to chatter’, fr. gosillier, ‘throat, gullet’, 
KLN_1971.txt:263873:vomit’. See next word.
```


## [2026-10-17T00:03:48.056Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"vomere\\|vomitus\" KLN_1966.txt | head -5; grep -n \"vanati\\|vánati\" KLN_1966.txt | head -5"
}
```


### [2026-10-17T00:03:48.535Z] TOOL RESULT

```
12967:emesis,  n.,  vomiting  (med.)  —  Medical  L.,  fr. Gk.  gp.e<Ji4,  ‘vomiting’,  fr.  £(j.etv.  See  next  word, emet-,  form  of  emeto-  before  a  vowel, emetic,  adj.,  causing  vomiting.  —  L.  emeticus, fr.  Gk.  ifienxos,  ‘provoking  sickness’,  fr. ep,cTo<;,  ‘vomiting’,  fr.  e|xeiv,  ‘to  vomit,  throw up’,  which  stands  for  *Fep.Etv,  fr.  I.-E.  base *wem-,  ‘to  spit,  vomit’,  whence  also  L.  vomere, ‘to  vomit’.  See  vomit  and  cp.  Emys.
36005:sound,  n.,  noise.  —  ME.  soun,  fr.  OF.  ( =  F.)  son, fr.  L.  sonus,  ‘sound’,  which  stands  for  *swonos, and  is  rel.  to  sonare  (for  *swendre),  ‘to  sound’, fr.  I.-E.  base  *swen-,  ‘to  sound’,  whence  also OI.  svanati,  ‘it  sounds’,  svdnas-,  ‘noise’,  svanah, ‘sound,  tone’,  svanah,  ‘rustling’,  OIr.  senim,  ‘the playing  of  an  instrument’,  OE.  geswin,  ‘music, song’,  swinsian,  ‘to  sing’,  ON.  svanr,  OE.  swan, ‘swan",  prop,  ‘the  singing  bird’.  See  sonant  and cp.  swan.  The  d  in  sound  is  excrescent.  Cp. bound,  ‘ready’,  and  words  there  referred  to.
41202:venenate,  tr.  v.,  to  poison  (rare).  —  L.  venenatus , pp.  of  venendre,  ‘to  poison’,  fr.  venenum,  ‘poi¬ son’.  See  venom  and  verbal  suff.  -ate. Derivative:  venenat-ion,  n. venerability,  n.  —  ML.  venerabilitds,  fr.  L.  vene- rabilis.  See  next  word  and  -ity. venerable,  adj.  —  ME.,  fr.  L.  venerdbilis,  fr.  vene- rari,  ‘to  venerate’.  See  next  word  and  -able. Derivatives:  venerable-ness,  n.,  venerabl-y,  adv. venerate,  tr.  v.,  to  revere.  —  L.  veneratus,  pp.  of venerari,  ‘to  reverence,  worship,  venerate’,  fr. venus,  gen.  veneris,  ‘love,  sexual  desire,  loveli¬ ness,  attractiveness,  beauty,  charm',  whence Venus,  gen.  Veneris,  ‘the  goddess  of  love’ ;  cogn. with  OI.  vanas-,  ‘desire’,  vanati,  vandti,  vanchati, ‘desires,  loves;  wins,  is  victorious’,  Avestic  va- naiti,  ‘he  wishes;  is  victorious’,  OE.  wynn,  ‘joy’, wunian,  ‘to  dwell’,  wenian,  ‘to  accustom,  train; to  wean’,  wyscan,  ‘to  wish’.  All  these  words  de¬ rive  fr.  I.-E.  base  *wen-,  ‘to  strive  after,  wish, desire;  to  be  satisfied;  to  be  wont’.  See  wish  and verbal  suff.  -ate  and  cp.  venery  (in  both  senses), venial,  venom,  Venus.
```


## [2026-10-17T00:03:52.258Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"vomit,  \\|vomit, \" KLN_1966.txt | head -5"
}
```


### [2026-10-17T00:03:52.955Z] TOOL RESULT

```
12967:emesis,  n.,  vomiting  (med.)  —  Medical  L.,  fr. Gk.  gp.e<Ji4,  ‘vomiting’,  fr.  £(j.etv.  See  next  word, emet-,  form  of  emeto-  before  a  vowel, emetic,  adj.,  causing  vomiting.  —  L.  emeticus, fr.  Gk.  ifienxos,  ‘provoking  sickness’,  fr. ep,cTo<;,  ‘vomiting’,  fr.  e|xeiv,  ‘to  vomit,  throw up’,  which  stands  for  *Fep.Etv,  fr.  I.-E.  base *wem-,  ‘to  spit,  vomit’,  whence  also  L.  vomere, ‘to  vomit’.  See  vomit  and  cp.  Emys.
18684:ignivomous,  adj.,  vomiting  fire.  —  Late  L.  igni- vomus,  compounded  of  L.  ignis,  ‘fire’,  and  vo¬ mer  e,  ‘to  vomit’.  See  igneous  and  vomit, ignoble,  adj.,  1)  of  low  birth;  2)  base;  3)  dis¬ honorable.  —  F„  fr.  L.  ignobilis,  ‘unknown,  un¬ distinguished,  obscure',  fr.  i-  and  OL.  gnobilis (L.  nobilis),  ‘known,  famous,  renowned,  noble’. See  noble.
25804:nutritive,  adj.,  nourishing,  nutricious.  —  ME. nutritif,  fr.  MF.  (=  F.)  nutritif  (fern,  nutritive ), fr.  Late  L.  nutritive,  ‘nourishing’,  fr.  L. nutrite,  pp.  of  nutrire.  See  nutrition  and  -ive. Derivatives:  nutritive-ly,  adv.,  nutritive-ness,  n. nux  vomica,  the  seed  of  an  E.  Indian  tree  con¬ taining  strychnine;  2)  medicine  made  from  this seed.  —  ML.,  lit.  ‘a  nut  to  make  (one)  vomit’, fr.  L.  nux,  ‘nut’,  and  vome're,  ‘to  vomit’.  For  the first  word  see  nucleus,  for  the  second  see  vomit, nuzzle,  intr.  v.,  to  press  the  nose  (against);  tr.  v., to  touch  with  the  nose.  —  ME.  noselen,  fr.  nose. See  nose  and  freq.  suff.  -le  and  cp.  nozzle, nyct-,  form  of  nycti-  before  a  vowel, nyctalopia,  n.,  1)  night-blindness;  2)  day-blind¬ ness  (med.)  —  Late  L.,  fr.  nyctaldps,  ‘one  who suffers  from  night-blindness  or  from  day-blind¬ ness’,  fr.  Gk.  vuxTdtXcoiJq  which  is  compounded of  vu;,  gen.  vuxt6;,  ‘night’,  txXxo;,  ‘blind’,  and gen.  <j>n6q,  ‘eye.  For  the  etymology  ofvu' see  nycti- ;  aXzoc  prob.  means  lit.  ‘not  seeing', and  is  formed  fr.  a-  (see  priv.  pref.  a-)  and  the stem  of  Xaetv,  ‘to  see’,  which  is  cogn.  with  OI. lasati,  ‘shines,  beams’;  for  the  etymology  of  Gk. ci'j'  see  -opia.  Cp.  hemeralopia.
```


## [2026-10-17T00:03:59.148Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"vanavšak\\|vanafšak\\|wanafšag\\|vanafsak\\|vanavsak\" BQT_v1_pages.txt BQT_v1.txt BQT_alt_v1.txt MON_part1.txt 2>/dev/null | head; grep -n \"^بنفشه\\|بنفشه -\\|بنفشه:\" BQT_v1_pages.txt | head -5"
}
```


### [2026-10-17T00:03:59.465Z] TOOL RESULT

```
21100:بنفشه ۱ هم اول و کر اول هردوآمده
21137:» باهش - بفتح اول و دوم . رنك کبود مانند رنك بنفشه - نوعی از جواهر کریمه
```


## [2026-10-17T00:04:02.268Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 21085,21140p BQT_v1_pages.txt; awk 'NR<21100 && /\\[pdf page/ {p=$0} END{print p}' BQT_v1_pages.txt"
}
```


### [2026-10-17T00:04:03.114Z] TOOL RESULT

```
۴ تاواک دصق ۵ بر( :
ست * فرهنك دساتیر ۲۳۹ >. ۷ - فرحنك
4 رله : نشاختن . ۰- رگ : تین -
3 حس مشتر
چ جل - رك : برافوش .
شه در صفحه ۳۶۸مصفر بن است ۳ که حبة الخترا و چنلافوج .
باشد , و آن بیثثر در کوهها و جنگلها حاسل
۰ میگردد -ونوعی از قماش زمین اطلس بودکه
برآن کلهای زربفت باشد و کلها ونشانها رائیز
گویند که برروی مهوشان از خوردن شراب بهم
میرسد باعرق برپیشانی ابشان شیندب وبشم اول
مصفر بنه است یعنی درخت کوچك ۴ - وبمعنی
کشان واثرهم هست چنانکه گوند «از فلانی بااز
فلانه چیز بنك نمانده است » اراده آن باشد که
نشان واثر تمانده است - وینم اول وسکون ثانی
بنفشه ۱ هم اول و کر اول هردوآمده
است ۰ گلی باشد ممروف
وطبیعت آن سرد وتراست
دردوم وسوم ؛ وممرب آن
بنفسج باشد- ونام کیاهی‌هم
هست که ات روبث.
بفشه گون‌طار م-
۲۳۳
بشثه گون مهد کنابه از آسان
وزهین هردو باشد .
بنقه - فح اول وفاف و سکون نون ؛
نوعی از غله باشد مانتد عدی » و قوت و منغعت
آهم مانثد عدس است .
ماش « بننح اول وئانی وسکون کاف »
وثالث » پوست بیخ ام غیلان باشد. وآن درختی
است صحرانی درولات عصمر ۰
بن کار خوددن.- منم اول رکس:
نانی, کنابه ازاندبشه نمودن بجهت عاقبت وانتها
ویایان کار باشد .3۶
۱ -یهلوی۷20۵)502او نوالام». هرن نرابفتح و کسروض‌اول خوانده«اسفا۷:۱ص۲4»,
طبری ۰۷۵1۱1502 مازندرانی کنونی ۷60۵۵56 « واژه نامه ۸۱۰ کیلکی ۵2086512. یره
بننشه ۷۱۵۱2۳1665 دارای کل های نامنظم و مهمیزدار است و دو جنس دارد : بنفشة عمطر
212 ۷۱۵۱۵ که کل آن بمنوان ملین بکار رود و دیگر بنفشة سه رنك با بنفثةٌ فرنگی
65 کهیرای زشت کاشته میشود. « گل گلاب ۲۱۲. ۴ - رك: بن. ۴ - رل: بنه.
بفبه در صفحهٌ ۳۰۹
بقّه از صفحٌ ۳۰۷
۵ ند گی _ بفتح‌اول‌وسوم, از:بنده (بند گه) + ی(حاصل‌مصدد) . په‌لوی 002811 قط
«اسفا ۱ : ۱ ص ۲۵۷ ؛ بنده و غلام بودن - اطاعت و انقیاد . رلك : بنده .
۵ بنده - بقتح اول وسوم» پهلوی معط «منای 6۲۹۹ «یونکره 6۷ یارسی باستان
2 هبد«بار تولمه »٩۲4‏ ازممدر بستن («. م), جمع‌آن بندگان» در پهلوی 3808127
«یب رکه ۳۲»؛ عبده غلام. مقابل آزاد . رك : داثرغالمعارف اسلام .
۵ بنديی - رد : منف ضم اول. (س۳۰۵ح).
۵ بر - رك : بنذ بنم اول . (سه ۳۰ج) ِ
۵ بترئی - بکر اول. ازفرانسه ۳6۵2186 ازابتالبابی 0602108 (روغن بان), کلم
بان از عربی بلغات ارویایی نقل شد. . درسال ۱۸۲۵ ماده ای که اکنون بنزین مینتاميم توسط
علمای شیمی کشف گردید «تقس». ماد شیمیابی مزبور برای حر کت اتومبیل وهواییسا و موتور
کارخانه‌ها نیز با کردن پارچه‌ها ازچربی وغیره بکار روده
» باهش - بفتح اول و دوم . رنك کبود مانند رنك بنفشه - نوعی از جواهر کریمه
6 نی ود.بنگان - بکس اول وکاف فارسی بالف
کشید بروزن فنجان . طاسی باشد که دهقادان
بنآنرا سوزاخ کرده باشند وآترا درطفار پرآیی
```


## [2026-10-17T00:04:10.075Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"vanā\\|vana-\\|vanâ\\|vanä\" BQT_v1_pages.txt | head; grep -n \"nārvan\\|närvan\\|ناروَن\\|نارون\" BQT_v4_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -5"
}
```


### [2026-10-17T00:04:10.401Z] TOOL RESULT

```
7128:عم رنگه باشد . تزديك به بيشةٌ تپمیشه‌مشهور به‌بيشةٌ نارون ۸ -
7135:مدتی ‎)٩(‏ خوانند ۴ . اول نارون است که درخت خوش اندام باشد .
7152:۴ - ر4 : نارون .
7158:ولف در فپرست شاهنامه « ناروان » را بمعنی 8۳8288180161 (اثار) آورده است . رك : نارون-
7165:۸ - رك : فهرست ولف: نارون » بیشه ۲ ‎٩‏ - از : نار ( انار )ون ( اوستایی
```


## [2026-10-17T00:04:13.030Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7150,7172p BQT_v1_pages.txt; awk 'NR<7165 && /pdf page/ {p=$0} END{print p}' BQT_v1_pages.txt"
}
```


### [2026-10-17T00:04:13.313Z] TOOL RESULT

```
ای رجا روط
فرشته‌ییت موکل بر آتش و پیوسته در آتش
مقام دارد ؛ و معنی ترکیبی آن آتش جهنده
باشد چه آذر بمعنی آش و کشپ بمنی‌جهنده
و خیز کننده آمده است واین‌منی مناسبتی نملم
ببرق دارد .
آذّد گون - جنم کاف فارسی و سَئون
واو و تون . نوعی از شفائق است که کنار
های آن سرخ و میانش سیاه می باشد » و بعضی
کون دکیاهی است سرخ رن که در میان آب
میروید - دمگر گفته‌اند که نوعی از بابونه است
و گل هميشه بپار را نیز کویند ۱ ؛ و حعنی
تر کیبیآن اس داد ات چه آند بسنی‌آاش
و گون بمعشی مانند باشد - ونلم اسی هم هست.-
و سمندر را هم میگویشد .
٩‏ - درعربی «آذربون». کیاهی‌است بباندی يك نراع » دارای بر گهای کشیده بطول يك
انگشت و گلهای سرخزرد . و بوی بد , و میان‌آن سیاه رن است . هوبت اب نگیاه هنوز تعیبن
شده دربونانی 8278۲108 206۲۵ مترادف ۷۷۱۵۵۲15 568630 (60۳۲۲۷۵ 56۳608) است.
تفصیلاتی که لو ند گان عرب در یاب این کیاه آورده اند «خحر باتخاب بن 06( و
کتاهمنع: ۵6۲ 2160012 ( کل‌همیشه‌بهار) گردیده‌است . «داثرة المعارف اسلام : آذرگون»
مت رد ِ مدع و «مزدستا ۱۸۷-۸ .
وا ۵ 1 دوف و ۷۳ ۵ مخفف آذر رنگ یمعتی آتش رنگه .
۹ - این همان آتشکده است که فردوسی آیرا « نوش‌اذر » خوانده جاي انرا بلیع داند
```


## [2026-10-17T00:04:19.223Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/ون",
 "prompt": "Quote the Mo'in entry for ون (van) including any etymology (Pahlavi/Avestan) verbatim."
}
```


### [2026-10-17T00:04:21.249Z] TOOL RESULT

```
# Mo'in Dictionary Entry for ون (Van)

According to the Mo'in Dictionary (Farhang-e Entesharat-e Mo'in), the entry for ون is:

"(وَ) (اِ.) درخت زبان گنجشک"

This translates to a tree associated with sparrows' language. The entry does not include any Pahlavi or Avestan etymology.
```


## [2026-10-17T00:04:25.680Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -i \"BANAFSH\\|^ *BON\\b\\|VANA\\b\\|VAM\\b\\|BAN \\|WEN\\b\\|WEM\\b\" ARY_latin_index_pages.txt | head -20; grep -n \"بنفشه\\|بیمار\" ARY_pages.txt | head"
}
```


### [2026-10-17T00:04:26.150Z] TOOL RESULT

```
350:SDRAVIDIAN s-tsshjo0 St) alsa! ga yb GUIL; 55 Oban yr 49
2992:WEBAN WAR :(TOKHARIAN B) B «5,3
3183:BABAN CELTIC) (1S) gle BABAE, PAPAE LATIN) 3
3184:BABAN WELSH) 5) BEBE (FRENCH) W313
3185:BABAN AGABLIC) SSE NENE, BEBE (SPANISH) gly
4326:VAWEN :(MIDDLE GERMAN) aly glalT PUITIKA AVESTAN) glee 3\
4341:oo FOWEN
4350:FOWEN PALAIDAN, PALAIDAN,
5478:[wen moist tees lyre re |
5490:POKORNY, —=SSOS*~*~*~*~*~«dS DOUWEN, DOAN
5570:SERRACH :(IRISH) 43 p\ STERBAN (OLD SAXON) oS py-St
5689:SPUWEN (DUTCH) goa (SANSKRIT) cy Seale
5729:DOWEN
5886:DU (GERMAN) JUST ‘TU, TAVA, TOM, TVAM
5888:THOU ENGLISH) galSi ——TAVA, TUVAM
5896:TY, VY (SLOVAK) 51 gle ‘70, TAVA, TUAM, TVAM
6153:JUNJA LATVIAN) (3) 523 YAW, JAM, JAWEN  (PAHLAVD) sly
6220:KAUWEN (DUTCH) «sicla ZHOVAL, ZHOYAL
6254:KINNUS GOTHIC) Sa SANWEM _:(TOKHARIAN A) A 6,58
6417:HEBBAN (OLD ENGLISH) oa lS CHASP, CHASPAN
1339:سخت بیمار برد خوب شد و تب او «ریختء و لذا نام شهر را «تبریز» نهادند! باید پرسید قبل از این
2634:چم این واژه در زبان سانسگریت: بیماری,
```


## [2026-10-17T00:04:31.384Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -i \"VOMIT\\|VAMITI\\|VAMATI\\|VANATI\\|VENUS\\|VANAITI\" ARY_latin_index_pages.txt | head; "
}
```


### [2026-10-17T00:04:31.804Z] TOOL RESULT

```
7177:ae ° SVAN-, SVANATI :(SANSKRIT) ey Suile
15250:(POLISH) glen VAMATI, VAMITL (SANSKRIT) 24 Sit
15253:EMI, VEMT — (LATVIAN) (3) 93 VOMITUS, VOMG, VOMERE
15255:‘REFERENCES eth VOMITAR SPANISH) glilyat
15256:POKORNY ——~S~S~S~S*~«wLAG-AAT | VOMITARE ITALIAN) giSls\
15257:BARNHART: (VOMIT) 1211 YOMITA HRUMANIAN) «ges,
15259:MACKENZIE: (VOMIT) 139 , YOMITO, VOMITAR
15261:ONIONS: ~ (VOMIT) 986 VAMA
15262:SKEAT: (VOMIT) 695 VOMYTE (OLD ENGLISH) oS gudSth
```


## [2026-10-17T00:04:34.656Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 15235,15265p ARY_latin_index_pages.txt; awk 'NR<15250 && /pdf page/ {p=$0} END{print p}' ARY_latin_index_pages.txt"
}
```


### [2026-10-17T00:04:35.128Z] TOOL RESULT

```
MALLORY & ADAMS: (WEGH.) WEGAN (OLD ENGLISH) op .g-5\
rrva sebG ob, WEIGH ENGLISH) galSil
VEJE DANISH) Saito
teetlook
ili 009 2 2S Jeo ieghad 9 SAL Blok; 2 ly ot!
Bg 5 BU OLS 29 019 aa
SAF thee y cal gS 54) 2} Ob 22 03a ot
92S O9 Wdege 02g OST 545 OWS 2 N9 atl
we
[pdf page 522]
L
OY | (12S Lata!” 6 4) Gens aheny
[vot nee trp |
OLD CHURCH SLAVIC) pS 53% VAM- HAVESTAN) glen)
VAMA WAM. WAMIDAN (PAHLAVI) 53h
(POLISH) glen VAMATI, VAMITL (SANSKRIT) 24 Sit
WOMITOWAC, WYMIOTY EMEO, EMEIN GREEK) lig
VEMTI LITHUANIAN) i 3 (LATIN) 3)
EMI, VEMT — (LATVIAN) (3) 93 VOMITUS, VOMG, VOMERE
VOMIR HPRENCH) Wis
‘REFERENCES eth VOMITAR SPANISH) glilyat
POKORNY ——~S~S~S~S*~«wLAG-AAT | VOMITARE ITALIAN) giSls\
BARNHART: (VOMIT) 1211 YOMITA HRUMANIAN) «ges,
DELAMARRE: (VOMIR) 292 PORTUGUESE) lis »
MACKENZIE: (VOMIT) 139 , YOMITO, VOMITAR
BUCK: 265-266 HOLD SCANDINAVIAN) 48 (5131
ONIONS: ~ (VOMIT) 986 VAMA
SKEAT: (VOMIT) 695 VOMYTE (OLD ENGLISH) oS gudSth
114-118 (Glpieal) obaply YoMIT ENGLISH) ,gulSi
VIMLA — (,Jou):(NORWEGIAN) 15353
an
[pdf page 522]
```


## [2026-10-17T00:04:40.918Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Verfolgung\" BRT.txt | head; sed -n 23433,23440p BRT.txt | cut -c1-600; sed -n 24698,24702p BRT.txt | cut -c1-400"
}
```


### [2026-10-17T00:04:41.382Z] TOOL RESULT

```
22704:Eig.  vll.  'der  der  Verfolgung  ein  Ende  macht' ; *vayah-  n.  zum  V.  v^y.  —  <)  Falsch  JüSTl
23462:•  j.  vätay-  f.  'Verfolgung',  Bezeichnung eines  strafbaren  Delikts :  väiti  F.  25  a.
•  j-  vä(y)-  V.  'jagen'.     Praes.  i  va^yY: vy-,  3  vaya-,  'vya-'K  —  PFP.  *vSi^wa:
'jagen,  jagend  verfolgen' :^ff^a8a'a»i_j'^»t apu%ram  Janaiti  vIt  vayäti  va  xraosyäti vä  patdayeiti  (sd.)  vä  V.  75. 5 ;  —  ysi  vlsps U  apayeinti  yq  *aoe  paskät  vyeinii  ". ,  denen sie  von  hinten  her  verfolgend  nachjagen" ¥.57.29;  —  y&  *ava  ^xbayats  avaähe vyqsca  vyanasca  apatse  (sd.)  zbayeitt vyqs  apagaße  vyänS  "welche  beide  um Hilfe  rufen  der  Verfolger  und  der  Ver- folgte .  ."  Vt  i^.  3S;  —  aval  vayul .  . yat  xtia  dqma  vayemi  Yt/J.  43''.  1
mit  apa  'wegjagen  von  — '  {haca  mit Abi) :  apa  dlm  adäi  vyeiti  trayaahal  hala vourukasät  Yt.  Ä  23.
mit  aipi  'verfolgen,  heijagen  hinter  — ' (Akk.) :  mihr»m  .,yS.,  avarvhi  Alf  api- vaHi^i  bafvart  ypnqnä  nisirinaoiti  "der., hinter  ihnen,  den  wehrlosen  herjagt,  zehn- tausend Sch^ge  austeilt"  Ytio.  37.
vata-  1408
mit  vT  'wegjagen  von  -'  {Aaia  mit  Abi.) ; tistryS ..vlväiti  hü zrayankai kaca  vouru- kaiki  YL  8. 40;  — fravalayB . .  yä  rqtvmS vTväiiT/*^  ". .  die  (jetzt)  zur  Ruhe  bringen, (jetzt)  aufjagen"  YL/j.4o(?).
mit  Aam  'zusammenjagen':  sraofs  .  , VTspaiiby!!  nalmaßbyll  hqm.vätti  paiti  %rS- tära  yatata  "Sr.  jagt  sie  von  allen  Seiten zusanmien  den  schirmenden  K  entgegen" Yt70.4i,
ai.  viti-.vyänH  (»,  dazu  GdN.  VSt  3.  156); lal.  vitter,  liL  vejü  'ich  jage  nach'.  —  Pii. (tD  V.  j/);  kandixla«,  (zu  V./g)-  undeutlich (ob  handäfitT),  aber  erl.:  Aai  fat .  .  davct  'er läuft  hinterdrein',  ».  dazu  Bthl.  IF.  10. 197.  — >)  In  apa. .vyeinii,  t.  dazu  BTHL.  IF.  lO.  197. —  ')  Eine  missglilckte  Etymologie.  -^  3)  Man verlangte  'väid.  Ob  them.  und  mit  ai.  pdrä- dat  nsw.  lu  vergleichen?  —  <i  Nach  dem Muster  sturer  ä-Wurzeln. j.  vU  N.  43i  lies  i'i.
•  j.  vyäna-  Adj.,  PPM.:  s.  vä{y);
•  i.*vyänay-''  f.  —  ?— :  vispä  antan  °nls
P.?7.
Pii. ;  vaS  fa  harvisp  andark  api  pärihä  (bei Blochet  partkS),  erl. :  kus  afie  päyihä ;  mir unverständlich;  s.  No.  2.  —  O  So  Blocket; DST.  tiiän'.  —  »)  DsT.  ZA.  j.  66  überset«: "et  ne  faire  qae  regarder  dans  rinlervalle" und  verweist  auf  V.  ig.  19.
•  g-  *vyänä-  f.  'Gescheitheit,  Weisheit', ur  IS  :  kl  uzamSm  (sd.)  cSrti  •naya  pu- .  r)m  pi^fl  Y.  44-  7 ;  —  <^t^  vaocat  ahur5
```


## [2026-10-17T00:04:47.335Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"vayeiti\\|väyeiti\\|vaySiti\" POK_full.txt POK_0*.txt | head -5"
}
```


### [2026-10-17T00:04:47.753Z] TOOL RESULT

```
POK_01.txt:1124:iO-Präs.  (oder  von  einer  Wzf.  '-"^nei-?):  ai.  väyati  ^weht^^  av.  fraväyeiti verlöscht^;  got.  waian  loaiwö,  ags.  wäwan,  ahd.  wäjan,  wäen  ^wehen^,  aksl. ^eio  vejet^  ^wehen^  und  ^worfeln^  (davon  russ.  vejalo,  sloven.  vevnicaj r,o\n.  loiejaczka  ^Worfschaufel^  Kornschwinge^);  Nominal:  lit.  ue/as  ^Wind^ ; ai.  väyiH,  av.  väyus  ,Wind^  Luft^
POK_01.txt:1155:Ai.  vi/i^  vBh  m.  ,Vogel'  (Gen.  ve/i,  Akk.  vim),  av.  vis  ds.  (G.  PL  vayam^ auch  mit  themat.  Kasus  vom  St.  vaya-),  mpers.  vCii,  väyandalz  ;Vogel', ai.  vayas-  n.  ^Geflügel,  Vogel",  väyasa-h  ,Vogel,  Krähe';  verbal  av.  ä-vayeiti ^fliegt  heran'  (von  Gottheiten),  ai.  vevlyate  ^flattert'.
POK_02.txt:1697:ar.  grab-  , greifen'  in  hdngrabdm  (casmainl)  ,ich  erfaßte  (mit  dem  Auge)', perf.  jigaurva,  gdurvayeiti  (vgl.  ai.  grbhdyant)  , ergreift,  hält  fest,  be- kommt, nimmt  wahr',  Partiz.  Perf.  Pass.  gdrdjpta-^  grab-  ^Fassung  von Wörtern,  Satz';  Akk.  gdrdbqm  , das  Festhalten  an';  nipers.  giriftan  , ergrei- fen', glrad  , ergreift';
POK_02.txt:1702:Ai.  grbhnäti,  gxbhäydti  .ergreift,  hält  fest,  erlangt';  Neuerungen  sind: dgrabhlt  , ergriff',  Infin.  grdJiUum,  Partiz.  gfbliltd-  , regiert,  gefangen, festgehalten',  grdbhltr,  grahUr  , Ergreifer';  av.  g9r9wnäüi,  gdurväyeiti. apers.  garbäyaiti  , ergreift,  erobert,  bekommt,  nimmt  wahr,  begreift'.
POK_03.txt:1988:Av.  hävayqn  ,sie  schmoren',  hävayeiti  ,er  schmort*  (3.  Sg.  Opt.  huyär9i  '^ =  ai.  *suyür  zu  einem  Präs.  *haoiti  nach  der  Wurzelklasse);
```


## [2026-10-17T00:04:51.620Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"vltar-\\|vītar-\\|vitar-\\|vyäna\" POK_0*.txt | head -5; grep -n \"Root / lemma: uei-3\\|Root / lemma: uei-, uei\" POK_full.txt | head"
}
```


### [2026-10-17T00:04:52.022Z] TOOL RESULT

```
POK_03.txt:5168:A.  Ai.  vdyati  ,webt,  flicht'  (paradigmatisch  freilich  mit  Perf,  ftml^ Partiz.  Uta-,  Inf.  ötum  zusammengefaßt,  die  zur  Wz.  *aw-,  vermutlich  d«r Grundlage  von  uei-,  gehören);  väya-  m.  ,Weber,  das  Weben',  «Ä] -, Weber,  Näher';  vydyati  ,windet,  wickelt,  hüllt'  (:  lat.  vieö),  Parti«. , gewunden,  gewickelt',  vyäna-  n.  ,das  Winden,  Umhüllen';  vayd  ,Zwf|gf Ast',  vgl.  dehnstufig  aksl.  v^ja  , Zweig,  Ast*);  über  veviyate  ,fl*ttiff s.  oben  S.  86 ;  .         -'-
POK_03.txt:5216:av.  vöi  Inf.  ,zu  erfreuen,  zu  gefallen';  väy-  {yayeitij  vlväiti  ,jagt  weg', 3.  PL  vyeinti)  , verfolgen,  jagen',  vyäna-  ,der  Verfolgte',  vöidwa-  Adj.  ,zu jagen,  jagend  zu  verfolgen*,  vltar-  , Verfolger',  vätay-  , Verfolgung';
89754:Root / lemma: uei-3, ueia- : uT-
```


## [2026-10-17T00:04:57.058Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5205,5225p POK_03.txt | cut -c1-500"
}
```


### [2026-10-17T00:04:57.741Z] TOOL RESULT

```
;>Ring',  ;.r
WP.  I  223  ff.,  WH.  II  799  f.,  802  £f.,  806,  Trautmann  345  f.,  Vasmer  1,  iWt .195  f.,  2Q1,  205  f.,  Morris-Jones  Welsh  Gr.  101,  Frisk  462.  .  -ul     ■
1123
^  i^ei-,   t^ep- :  ui-,  erweitert  ul-t-  und  uei-s-  , welken'.
Lat.  viescö,  -ere  ^verwelken,  verschrumpfen^,  vieins, welk,  verschrumpft';
air.  feugud  gl  ,marcor*  ist  von  feo  ,welk'  {*m-uo-)  =  cymr.  gwyw  ds! abgeleitet ;
aisl.  visinn  ^welk^,  Partiz.  eines  *ivisan,  wovon  germ.  *wis-n-ön  -en  in jisl.  visna^  ags.  ivisnian  und  (mit  gramm.  Wechsel)  weornian,  ahd.  wesanen ^vvrelken'  (auch  nhd.  vericesen  gehört  wie  ags.  fonveoren  ,verwest'  zeio-t, ursprünglich  hierher);  mhd.  luesel  ,schwach,  matt',  engl.  dial.  weasel,  weazen ^dünn,  mager*,  aisl.  vesall  ^elend',  vesligr  ds,,  norw.  visa  ,schwache  Person*, schwed.  vesa  ^ermüden';
lit.  vysti  , welken*  (Prät.  vytaii),  vytinu,  pa-vaitinü  ,mache  welken',  lett. fietet,  vitet  ds.
WP.  I  227  f.,  WH.  II  787  f. ;  Beziehung  zu  ueis-  ,zerfließen*  ist  wahr- scheinlich.
,  uei-,  ueio-i  ui-  1.  ,auf  etwas  losgehen^,  einerseits  ,gehen^  gerade  Richtung nehmen;  Weg,  Reihet  andererseits  ,worauf  losgehen,  es  erstreben, erjagen,  ersehnen,  wollen'.  2.  ,kräftig  sein';  ui-to-  ^verfolgt,  er- wünscht', ui-ti-  ,das  Nachjagen,  Genuß';   uis-  , Kraft*.
Ai.  vkij  3.  PI.  vydntij  auch  vdyati  ^verfolgt,  strebt,  führt  (die  Waffen), treibt,  lenkt',  auch  , genießt*,  Partiz.  vltd-  ,verfo1gt,  beliebt*,  Adj.  ,gerad- linig*,  vltä  , Reihe*,  vlthi-j  vlthi  f.  »Reihe,  Weg',  pravayana-  ,zum  Antreiben dienlich*,  m.  , Stachelstock',  pravBtar-  ,.Wagenlenker',  viti-  ,Pferd*  (,*Ver- folger'  ?) ;  pada-vi  f.  ,Spur,  Weg,  Pfad*,  padaväyd-  ,Wegweiser,  Anführer' (dehnstufig);  mit  der  Bedeutung  , erstreben  —  gern  haben
av.  vöi  Inf.  ,zu  erfreuen,  zu  gefallen';  väy-  {yayeitij  vlväiti  ,jagt  weg', 3.  PL  vyeinti)  , verfolgen,  jagen',  vyäna-  ,der  Verfolgte',  vöidwa-  Adj.  ,zu jagen,  jagend  zu  verfolgen*,  vltar-  , Verfolger',  vätay-  , Verfolgung';
mit  der  Bed.  ,fliegen'  ai.  ved.  vevlyate  , fliegt'  und  av.  ä-vayeinti  ,sie fliegen  heran*;  ai.  venati  , ersehnt',  vend-  , sehnsüchtig,  verlangend';
gr.  Ufxai  ,bewege  mich  vorwärts,  eile,  strebe,  begehre',  (Umbildung eines  *J^i-ioixaL\  Asper  nach  dem  Medium  von  i^/u),  lif-isvog  ,cupidus', «IffaTo (/-),  i[J^]eLaaTO  ;ging  los',  ol(j.og  ,Gang,  Weg,  Bahn',  (*SoLi.Log),  hom. liüy,rj  , Verfolgung'  (/-),  Akk.  fwxof  ds.,  iojxixog  (l  metr.  Dehnung)  , Schlacht- getümmel', Ttaltcj^Lg,  naXi-lcD^ig  ,Wiederzurückdrängen  im  Kampfe',  korinth. fi(byi€i  ,verfolgt'  (vgl.  ÖLcjyc-a):  dieiiai)]  IsQÖg  [fuqog),  dor.  
71*
1124  9
ig  ,Kraft'  (=  lat.  vis,  vim),  yig'  lo^vg  Hes.,  \(pi   ,mit  Kraft^  (Instr -hhi),  wovon  Y(pLog]  über  lg  , Sehne'  s.  oben  S.  1121;  \,_
lat.  via  f.  ,WegS  osk.  viü,  umbr.  Ablativ  vea,  via  ds.,  osk.  amviarif  \ , Straßenviertel,  Straße'  (*wetä);  lat.  vis  ,du  willst'  {*uei-si  =  ai.  t?^*\ vim  , Kraft,  Gewalt'  (=  gr.  fe  ds.),  PI.  vires  (von  einem  s-Stamm)-  inlt^ , bewirten,  einladen^  mit  in-  ,em'-  gegenüber  verneinendem  in-  ,un'-  in  ^^
tus  jwider  Willen'  (:   ai.   vUd-   , beliebt');    ob    vindex  , Bürge,  Rächer*    t. jBestimmer  der  Sühne'  zu  aksl.  vlna  , Schuld'?
(über  Siir.-fiad  ,Wild',  fiadach  ;Jagd'  usw.  s.  u.  *uidhu-  ,Baum*V
mcymr.  gwit  , Speise*,  mel-wit  , Honigseim'  (:  ai.  vUi-  , Genuß  MM^ Ifor  Williams  BBCS.  11,  143;  '  ^**«Uj,
```


## [2026-10-17T00:05:08.137Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"vanavax\\|vana.vax\\|vanavaxs\" BRT.txt HRN.txt HUB.txt NYB_vol2_glossary.txt PHD.txt | head; grep -n -i \"wanafšag\\|vanafšak\\|vanavšak\" NYB_vol2_glossary.txt | head -3"
}
```


### [2026-10-17T00:05:08.649Z] TOOL RESULT

```
HUB.txt:1030:nach Fr. Muller WZKM. 7, 368 = zd. ^vanavaxsa-
```


## [2026-10-17T00:05:12.440Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -n 28751 KNT_full.txt | tr -cd '\\f' | wc -c; awk 'NR>=28650 && NR<=28760' KNT_full.txt | grep -n \"^ *[0-9][0-9][0-9] *$\\|LEXICON\" | head"
}
```


### [2026-10-17T00:05:12.800Z] TOOL RESULT

```
0
15:206
```


## [2026-10-17T00:05:16.516Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/542.jpg && python3 -c \"from PIL import Image; im=Image.open('site/pages/542.jpg'); print(im.size)\""
}
```


### [2026-10-17T00:05:16.894Z] TOOL RESULT

```
Exit code 1
site/pages/542.jpg
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    from PIL import Image; im=Image.open('site/pages/542.jpg'); print(im.size)
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-17T00:05:28.720Z] TOOL CALL #58: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/542.jpg"
}
```


### [2026-10-17T00:05:28.768Z] TOOL RESULT

```

```


## [2026-10-17T00:05:33.889Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^vām\\|^vamī\\|^vāmīt\\|^vān-\\|^vānīt\\|^vānītan\\|^vanītan\" NYB_vol2_glossary.txt | head; grep -n \"vomit\\|conquer\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-10-17T00:05:34.189Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:05:36.185Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3915,3935p NYB_vol2_glossary.txt | cut -c1-300; grep -n \"^ *vān\\|^ *vam\\|^ *vām\" NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:05:36.657Z] TOOL RESULT

```
Vahuman [whwmn'] one of the Amah- raspands (g.v.), in the Phl. literature occupying the first place next to Ohur- mazd: 394-10.27, 404.19. 509. 513-4. 56-57 passim. 585. 593, 655, — The name of the llth month, and of the 2nd day of the month. — Av. (1129 sqq.) Vohu- manah- ; MPrs whmn (S; the 2nd da
lvüi [wy] bird 72°. — Av. (1356) ?vag-, (1358) vaya-vant- ‘possessing birds’, (1359) vayö.-barata- ‘carried away by birds’; Paz. vač.
?vài the Wind as a mythic cosmic power: ~ + veh 72°, ~ 4 vattar 12199; ~ 4 derang- xauatdi (g. v.) 9913-14. 1065. — Av. (1357, 1358) vayu-, vaya-; OlInd väyu-; Paz. vač.
3yäi woe!: ~ 6 martom bavāt woe be to mankind! 118. — Av. (1359) vayi.barat- ‘erying woe’; MPrth wy (MHC); Paz. vaé (SGV).
| Valaxš [wlhš] n. pr.: ~ 4 Aškānān V. of
the Askän (= Arsacid) dynasty 10818; — —-Šahpuhr the name of a town 1277. —.
| KZŠPrth 1. 25 wlgšy, Prs 1. 30 wrdhšy,
www .parsianjoman.org | ool wok
Valaxš
202
vāparīkānihistan
Gr. v. OvaAA«aocov (gen.); cf Lat Volageses. V. also Gulaxsan
van [wn'] tree 409-11.26. 415, — Av. (1353) van- or (1354) vana-; Paz. van, gan (Mx); NP van ‘wood, forest’ (probably lw., but ef nar-bun, nür-vun, när-van ‘the pome- granate tree’).
Van n. pr. fem.: ~ i Gulaxsän V. daughter of Gulaxš = Valaxš (g. v.), probably a prince or king of the Arsacid family; ~ the name of her town 117. — Other explanations Cat. 106 sg.
Vanand [wnnd] one of the fixed stars 87%; regarded as the ruler of the Western celestial sphere, v. Mx 4912-14, — Av. (1354) Vanant-.
Vandöi-Sähpuhr [wndwd-šhpwhl] n. pr. of a town, later form Gundē-šāpūr 11621. — Originally Vahy-Andiyok-Šahpuhr *bet- ter than Antiochos Sahpuhr (built) KZS Prth 1. 26 = Prs 1. 32 init.; Gr. v. Tove Avrıoy LaBwe; Arab Jundaisabur, Yagut 2,130, where also Wandi-säbür is quoted after Ibn al-Fagih.
Vānēt-xvarr(ah) [wnyt! GDH] n. pr. 1061913, — "The Khwarenah will gain victory’, cf s. v. x“arrah.
Van-*FröSn [wn' plwšn'] n. pr. 478. — BdA p. 229? wn' plwksn', BAJ 779 (Paz.) Van-fryešni (but -k- in -wk- is certainly only orthographieal, warranting the pro- nunciation -6- of -w-).
vàng [w?ng, Ps. w’ngy; K?L?] voice, sound, shout, cry: ~ kartan to give a shout 1616; to shout; to sound, of a musical instrument 201%; of a horse’s call: to neigh 282; ~ burtan to shout 469; ~ be burtan 6 to shout to a p. 388. 4326; ~ zxröstan to yell, of Hešm 615; — war-cry 25%; — invocation (Chri
vànitan [w’nytn'], pres. Ist p. sg: vänom 615, to vanquish, to defeat 1065. 109?2, —
| Av. (1350) !van-; MPrs pres. w’n-; pt.
7491:vam, äväm: apam
```


## [2026-10-17T00:05:45.624Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; T=tools/fetch_source.py; \npython3 $T 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wemh₁-' --note 'page 542, root Wem: PIE *wemh1- spew, vomit' ;\npython3 $T 'https://en.wiktionary.org/wiki/vomit' --note 'page 542, root Wem: English vomit < Latin vomitare' ;\npython3 $T 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wenh₁-' --note 'page 542, root Wen: PIE *wenh1- to love, Skt vanati' ;\npython3 $T 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyh₁-' --note 'page 542, root Wen node 1: Av. vay- hunt belongs to *weyh1- chase' ;\npython3 $T 'https://en.wiktionary.org/wiki/بنفشه' --note 'page 542, root Wen node 8: banafshe < MP wanafsag, uncertain origin' ;\npython3 $T \"https://en.wiktionary.org/wiki/wnpšk'\" --note 'page 542, root Wen nodes 6-7: MP wanafsag etymology (Bailey *van- blue; Martirosyan)' ;\npython3 $T 'https://en.wiktionary.org/wiki/بن' --note 'page 542, root Wen node 5: bon tree < MP wan; bon base < *buHna' ;\npython3 $T 'https://en.wiktionary.org/wiki/वन' --note 'page 542, root Wen node 10: Skt vana < PII *wan- tree' ;\npython3 $T 'https://en.wiktionary.org/wiki/वणिज्' --note 'page 542, root Wen node 10: Skt vanij < *wenh1- + *h2eg-' ;\npython3 $T 'https://en.wiktionary.org/wiki/banyan' --note 'page 542, root Wen node 11: banyan < Port. baniano < Gujarati vaniyo < Skt vanij' ;\npython3 $T 'https://vajehyab.com/moein/ون' --note 'page 542, root Wen node 5: Moin van = ash tree' 2>&1 | tail -3"
}
```


### [2026-10-17T00:05:49.007Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2c42fcb0fd815df9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8099e093b22c7078.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/326c1a748306b631.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b64c1ae914faefaa.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/59e5aeaf057b24db.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/396db7045784aa88.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1f62bc9dde79b6fa.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e1a15b92414e7a95.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/11cafba225dc2286.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/efc335242ec4ffcf.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/91b8a9c514bbe2a9.txt
```


## [2026-10-17T00:05:52.278Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"speien\\|ausspeien\" BRT.txt | head -5 | cut -c1-300"
}
```


### [2026-10-17T00:05:52.613Z] TOOL RESULT

```
5221:Yt  /0.9, 24.        e)  *zu  Gunsten  von-,  pro':   ,  j.  avi  vanta  Inf.'>  'zu  bespeien,  Gewöl!
22666:/5.i;Vr.(f.i.         I) 'Flehen- (OUT  AbleiL).!     "«  '«''  "bcspeien';  s.  Inf.
```


## [2026-10-17T00:05:53.924Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22660,22672p BRT.txt | cut -c1-500"
}
```


### [2026-10-17T00:05:54.261Z] TOOL RESULT

```
•  j-.  K-  ^anta-  m,  l)  "Lob,  Preis, Huldigung':  »e™ech5elt  werden.  —  Pü. ;  vas  .fiiHf ta  yatüi  :g'aif  namJnIs  pairica  /asai(sA.)      ('"""""''^
'ta  (IS.)    Y.5/.a2;   —    */am  ya^äi  *tam   '  J-  vanya-  n.  'Sieg,  Besiegen'.
pairi.Jasai  -ta  *yam  amss!  spmtS  Y.70.'i;       ^»™P^  ^  ^"■"  V-  ■^■^-
—  Mi>>r9m..t?m  pairi.Jasäi'tat'ammatf  •  J-  ^<"»-  V.  'ausspeieo,  -brechen'.     Inf.
A1Ä7  Yt./0.6;  — /«r/ftVä  -«Äi  rafnankäca  •vinia'*;  Absol.  •vantim'l
amisf  sfmts  .  .  trlräi/  näman  äzbaya  Y.        '»»t  «'«"'  'bespcien';  s.  AbsoL
/5.i;Vr.(f.i.         I) 'Flehen- (OUT  AbleiL).!     "«  '«''  "bcspeien';  s.  Inf.
KompA.;  Ableil. -ZumV.3i.j».;vgl.i-(biwa-.         "■  ™™"4  'vomif,    mp.  (Fä.)  MMSa«,    wois.
—  Pn, ;  ayäwirih.  vomuti.    S.  auch  mp,  7Jtäk  (anter  ^•ämo').  —
^  >)   V^,  iBild,  Bthu  1F,  /.  58,  70.
•  j.  vantä.bar9tay-'>  f.  'Darbringung  von ;  •  j.  «vay-  V,  'fliegen',  nur  mit  a  'heran- Haldigaiigta' :  *Aui?r7itrmca  *ufta^>fyit[mA  äiegea',  von  Gottheiten.  Praes.  2  z^ya-. *T3inmca  afrlnami  tava  atars  Y.Ö2,  i;  amiianqm  spntanam  ..yailqm  ragxmS- 7,  CTo.ö",  P..y5;  —  hub}r)ti  usia.bmii  „hs  panistß  avay'atqm'^  'avi  taohrS •nti  atari  afrtnami  \.68.\\.  a)  mit  ".  ,  deren  Pfade  leuchten,  wenn  sie  zu Gen.  des  Empfängers:  :ia3;i/?/'fA-o,.'M>W/.-'<i
^■._^yiwär_b^inih    tT\.:  pa  hamnk  rä,  aj-ä- I  ^i^    N.   «   Und   Ol,   WO    'yanti.
6i.  7.  _  .)  NA.  ohne  Trennung.  „  ffi^^^  j  ^g^  ^^
```


## [2026-10-17T00:08:48.840Z] TOOL CALL #64: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-542.json",
 "content": "{\n  \"pdf_page\": 542,\n  \"book_page\": 512,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-16\",\n  \"entries\": [\n    {\n      \"entry\": 1,\n      \"root\": \"Wem\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *wemh₁- 'to spew, vomit' (Pokorny 1146 u̯emə-; Watkins weme-; Mann uemō)\",\n      \"note\": \"Root, label and gloss correct. Pokorny 1146 'u̯emə-, u̯emə- speien, sich erbrechen' with Skt. vamiti, Av. vam-, npers. vātāk 'Speichel' (*u̯m̥-to-), Gk. emeō, Lat. vomō, Lith. vemti. Watkins and Wiktionary agree. The extraction matches the printed page (site/pages/542.jpg).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *wemh₁- «قی کردن، تف کردن» در پوکورنی (ص ۱۱۴۶)، واتکینز و مان آمده است. بازمانده‌های آن سنسکریت vamiti، اوستایی vam-، یونانی emeō، لاتینی vomō و لیتوانیایی vemti است. ریشه و معنایی که نورایی داده درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wemh₁-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1146\", \"status\": \"supports\", \"note\": \"POK_03.txt l.5526-5527 'u̯emə-, u̯emə- ‚speien, sich erbrechen'. Ai. vami-ti, jünger vamati ‚ausspeien, erbrechen' ... av. vam- ‚erbrechen'; npers. vātāk ‚Speichel' (*u̯m̥-to-)'; page marker 1146 just above (l.5522).\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. weme- (AHD_watkins1985.txt l.1142)\", \"stance\": \"supports\", \"note\": \"'weme-. To vomit. ... 2. Latin vomere, to vomit: NUX VOMICA, VOMIT. 3. Greek emein, to vomit: EMESIS, EMETIC. [Pok. wem- 1146.]'\"},\n        {\"src\": \"IEC\", \"where\": \"s.v. uemō (IEC.txt l.19984)\", \"stance\": \"supports\", \"note\": \"'uemoó, ió \\\"vomit\\\". Onomat. WP I, 262 Skt. vàmami & vámimi, v. id.; Av. vam-, id.; ... Gk. eméo ...; Lat. vomo, ére, id.'\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I 262 f. (cited by Pokorny)\", \"stance\": \"supports\", \"note\": \"Pokorny's entry ends 'WP. I 262 f.', i.e. Walde-Pokorny treats the same root u̯emə- with the same Indo-Iranian and Latin material.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"vam\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan vam- 'to vomit, spew' (Young Avestan, Vīdēvdād; infinitive vantē 'to spit on') continues Indo-Iranian *wam- < PIE *wemh₁-, exactly matching Skt. vamiti/vamati 'vomits'. The PIE e became Indo-Iranian a; the laryngeal left no trace in Avestan. Root and gloss are correct.\",\n          \"derivation_fa\": \"اوستایی vam- «قی کردن، بیرون انداختن از دهان» از هندوایرانی *wam- و آن از هندواروپایی *wemh₁- است و با سنسکریت vamiti «قی می‌کند» برابر است. e هندواروپایی در هندوایرانی به a بدل شده است. بارتولومه و پوکورنی و هرن همین را آورده‌اند و ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wemh₁-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1146\", \"status\": \"supports\", \"note\": \"POK_03.txt l.5527 'av. vam- ‚erbrechen''.\"},\n            {\"ref\": \"KLN:1722\", \"status\": \"partial\", \"note\": \"The KLN 'vomit' entry (p.1722) is not legible in the local OCR; the cross-referring entry emesis (KLN_1966.txt l.12967) says 'fr. I.-E. base *wem-, ‘to spit, vomit’, whence also L. vomere ... See vomit' — supports the root, no Avestan form quoted in the legible part.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. ~1355 s.v. vam- (BRT.txt l.22663-22668)\", \"stance\": \"supports\", \"note\": \"'j. vam- V. ‚ausspeien, -brechen'. Inf. vantē ... ‚bespeien' ... ai. vam- ... S. auch mp. vātāk'.\"},\n            {\"src\": \"HRN\", \"where\": \"p. 296 no. 210 (HRN.txt leaf 318)\", \"stance\": \"supports\", \"note\": \"'210. vāmītan ‚speien', vd. 5 (6). aw. vam- ‚speien'; ai. vam-, vāmiti; lat. vomō etc.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"vâmîtan; vâtâk\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"vāmītan: Pahlavi wāmīdan, present wām- 'to vomit' (MacKenzie), from Old Iranian *wām-aya- (causative/iterative with lengthened ā, or a denominative of *wāma- 'vomit') to the root vam-; glossed in the Pahlavi Vīdēvdād 5.6 (Horn). Confirmed. vātāk 'saliva': Pokorny gives it as New Persian vātāk 'Speichel' from a zero-grade *u̯m̥-to- (> Iranian *wata- + suffix -āk) and Bartholomae refers to a Middle Persian vātāk under vam-, but the word is absent from MacKenzie and Nyberg, so the Pahlavi label and the form rest on Bartholomae/Pokorny only. Hence plausible for the node.\",\n          \"derivation_fa\": \"«وامیدن» در پهلوی wāmīdan با ستاک مضارع wām- «قی کردن» است (مکنزی) و از ریشهٔ اوستایی vam- با واکهٔ بلند ساخته شده؛ هرن آن را از گزارش پهلوی وندیداد آورده است و این بخش درست است. واژهٔ vātāk «آب دهان» را پوکورنی فارسی نو می‌داند و از بالاگونهٔ تهی *wm̥-to- می‌گیرد و بارتولومه آن را فارسی میانه می‌خواند، ولی در فرهنگ مکنزی و نیبرگ نیامده است؛ پس این بخش با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wemh₁-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1146\", \"status\": \"supports\", \"note\": \"POK_03.txt l.5527 'npers. vātāk ‚Speichel' (*u̯m̥-to-)' — supports vātāk (as New Persian, not Pahlavi).\"},\n            {\"ref\": \"HRN:296\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 318 = printed p.296, no. 210 'vāmītan ‚speien', vd. 5 (6). aw. vam- ‚speien'; ai. vam-, vāmiti; lat. vomō'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 87 s.v. wāmīdan (PHD.txt l.605)\", \"stance\": \"supports\", \"note\": \"'wāmīdan, wām- [w’m-ytn'] vomit.' — no vātāk entry found (grep 'wādag|vātāk').\"},\n            {\"src\": \"NYB\", \"where\": \"Part II glossary, s.v. v- (NYB_vol2_glossary.txt)\", \"stance\": \"silent\", \"note\": \"grep '^vām|vātāk|vāmītan' finds nothing; neither word in Nyberg's glossary.\"},\n            {\"src\": \"BRT\", \"where\": \"col. ~1355 s.v. vam- (BRT.txt l.22667)\", \"stance\": \"supports\", \"note\": \"'S. auch mp. vātāk (unter vāmō)' — Bartholomae records a Middle Persian vātāk.\"},\n            {\"src\": \"ARY\", \"where\": \"pdf page 522 (ARY_latin_index_pages.txt l.15247ff.)\", \"stance\": \"supports\", \"note\": \"Entry lists 'VAM- (AVESTAN) ... VAMA, WAM-, WAMIDAN (PAHLAVI) ... VAMATI, VAMITI (SANSKRIT) ... VOMITUS, VOMO, VOMERE (LATIN)' with references Pokorny, MacKenzie (VOMIT) 139.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"vomere\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin vomō, vomere 'to vomit' < Proto-Italic *wemō < PIE *wemh₁-; the e > o change before m after w is regular Latin (as in *swesōr > soror-type backing of e after w). Cognate with Gk. emeō (< *wemeō, with loss of digamma).\",\n          \"derivation_fa\": \"لاتینی vomō, vomere «قی کردن» از ایتالیک آغازین *wemō و آن از هندواروپایی *wemh₁- است؛ e پس از w و پیش از m در لاتینی به o بدل شده است. هم‌ریشهٔ یونانی emeō است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/vomit\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.1142 'weme-. To vomit ... 2. Latin vomere, to vomit: NUX VOMICA, VOMIT.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1146 (POK_03.txt l.5529)\", \"stance\": \"supports\", \"note\": \"'lat. vomō (*u̯emō) ‚erbreche', vomitus ‚Erbrechen', vomica ‚Geschwür'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. emesis (KLN_1966.txt l.12967)\", \"stance\": \"supports\", \"note\": \"'I.-E. base *wem-, ‘to spit, vomit’, whence also L. vomere, ‘to vomit’.'\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. uemō (l.19984)\", \"stance\": \"supports\", \"note\": \"'Lat. vomo, ére, id.'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"vomit\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English vomit (late 14th c., Middle English vomiten / vomit n.) from Latin vomitāre, frequentative of vomere, and vomitus 'a vomiting' (partly via Anglo-French vomite). Chain Latin → (Anglo-French) → Middle English is standard.\",\n          \"derivation_fa\": \"انگلیسی vomit «قی» در سدهٔ چهاردهم از لاتینی vomitāre (بسامدیِ vomere) و vomitus «قی کردن» وام گرفته شده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/vomit\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"s.v. Vomit (SKT.txt l.21053)\", \"stance\": \"supports\", \"note\": \"'Vomit, sb. (L.) L. uomitus, a vomiting; whence uomitare, to vomit — L. uomitus, pp. of uomere ... Gk. emein, Skt. vam, to vomit. (√WAM.)'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 index 'VOMIT weme-' (l.2457) and root entry l.1142\", \"stance\": \"supports\", \"note\": \"'VOMIT weme-'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Wen (Part 1)\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *wenh₁- 'to strive for, desire, love; win' (Pokorny 1146-1147 1. u̯en-; Watkins wen-¹; LIV² *u̯enH-)\",\n      \"note\": \"The root itself is right (Pokorny 1146 '1. u̯en-, u̯enə- ursprünglich ‚streben', woraus ‚wünschen, lieben, befriedigt sein' und ... ‚erreichen, gewinnen, siegen''), with Skt. vanati, Av. vanaiti 'conquers', MP wānīdan, Lat. venus, Eng. win, wish, ween. Nourai's added note that the root 'has derivatives related to sexual or hunting desires' rests on Latin venus and venārī 'hunt' (Watkins lists venārī under wen-¹). Problems lie in the branches: (1) Avestan vay- 'hunt', vītar- 'pursuer', vyāna- 'pursued', vāiti- 'persecution' belong to a different root, PIE *weyh₁- 'go after, chase' (Pokorny 1123 u̯ei-), not to *wen-. (2) The tree word Av. vanā-, MP wan, NP bun/van is linked to *wen- only by Uhlenbeck, a link Walde-Pokorny (I 259) calls 'unglaubhaft'. Watkins accepts it. (3) The Avestan 'vana-vaxša' behind banafše is only F. Müller's reconstruction, which Hübschmann rejected. Modern scholars treat MP wanafšag as of uncertain origin. (4) Skt. vaṇij 'merchant' did not mean 'trader of animal skins' and is not derived from vana 'forest'. Watkins and Wiktionary derive it from *wenh₁- ('seeking to gain'). The banyan tree is named after the Banian (Hindu) traders who held a pagoda under such a tree at Gombroon (Bandar Abbas), not after a skin trade. Nourai's KNT:260 is a misprint for Kent p. 206 (s.v. van-). The extraction matches the printed page.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *wenh₁- «کوشیدن برای چیزی، خواستن، دوست داشتن؛ به دست آوردن، پیروز شدن» در پوکورنی (ص ۱۱۴۶-۱۱۴۷)، والده-پوکورنی و واتکینز آمده و درست است. بازمانده‌های آن سنسکریت vanati، اوستایی vanaiti «پیروز می‌شود»، پهلوی wānīdan «شکست دادن»، لاتینی venus و انگلیسی win و wish است. ولی چند شاخهٔ این نمودار جای درستی ندارد. واژه‌های اوستایی vay- «شکار کردن»، vītar- «دنبال‌کننده» و vyāna- «دنبال‌شده» از ریشهٔ دیگری‌اند (*weyh₁- «دنبال کردن»). پیوند «بُن/وَن» (درخت) با این ریشه را والده-پوکورنی نمی‌پذیرد. صورت اوستایی vana-vaxša برای «بنفشه» ساختگی است. معنای «سوداگر پوست جانوران» برای سنسکریت vaṇij هم در منابع نیامده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wenh₁-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1146\", \"status\": \"supports\", \"note\": \"POK_03.txt l.5534-5535 '1. u̯en-, u̯enə- ursprünglich ‚streben', woraus ‚wünschen, lieben, befriedigt sein' und ‚erarbeiten, Mühe haben', perfektiv ‚erreichen, gewinnen, siegen' ... Ai. vánati, vanóti ‚wünscht, liebt, gewinnt, siegt' ... av. vanaiti, vanaoiti ‚siegt', mpers. vanīdan ‚besiegen, schlagen''; page 1146-1147.\"},\n        {\"ref\": \"OEW:434\", \"status\": \"not_checked\", \"note\": \"Shipley 1984 is lending-only on archive.org; not accessible.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 258-259 (WLD_Bd1_pages.txt leaves 267-268)\", \"stance\": \"supports\", \"note\": \"'uen-. Als Grundbedeutung dieser Wz. wird „streben, erstreben“ anzusehen sein, woraus sich ... „wünschen, lieben“ ... „erreichen, gewinnen, siegen“ ergeben kann.'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wen-¹ (l.1142)\", \"stance\": \"supports\", \"note\": \"'wen-¹. To desire, strive for. 1. ... Old English winnan, to win ... 6. ... wyscan, to desire, wish ... 8. ... Latin venus, love ... 11. Lengthened-grade form *wēn-ā- in Latin vēnārī, to hunt ... 12. *wen-o- in Sanskrit vanam, forest ... 13. Possibly zero-grade suffixed form *wn-ig- in Sanskrit vaṇik, vāṇijaḥ, merchant (? < \\\"seeking to gain\\\"): BANIAN. [Pok. 1. wen- 1146.]'\"},\n        {\"src\": \"IEC\", \"where\": \"s.v. uenos (l.20007)\", \"stance\": \"supports\", \"note\": \"'uenos, -es- ‘desire’. Cf. uén- (1) and WP I, 259 Skt. vanas, n. ‘loveliness’ ... Lat. Venus'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"vanaiti; vantar; vayeiti 1; vîtar 2; vyâna 2; vâti\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"vanaiti and vantar are correct: Av. vanaiti/vanaoiti '(he) conquers, wins' (Bartholomae col. 1350) and vantar- 'victor' (= Skt. vantṛ-) continue Indo-Iranian *wan- < PIE *wenh₁-. Avestan uses the verb only in the sense 'conquer, overcome', so Nourai's gloss 'he wishes' comes from the Sanskrit sense (Klein glosses it 'he wishes; is victorious'). The other four words belong to a different root. vayeiti 'hunts, pursues' (vāy-), vītar- 'pursuer' (Yt 17.12), vyāna- 'pursued' (passive participle, Yt 13.35 'vyąsca vyānasca, the pursuer and the pursued') and vāiti-/vātay- 'persecution' (a punishable offence) all come from Indo-Iranian *wayH- 'chase, pursue' < PIE *weyh₁- (Pokorny 1123 u̯ei-). Their cognates are Skt. veti, vīta-, Lat. vīs, invītus and Lith. vejù 'I chase'. They are not from *wen-, so they are wrongly placed under this root.\",\n          \"derivation_fa\": \"دو واژهٔ نخست درست‌اند. vanaiti «پیروز می‌شود» و vantar- «پیروز» از هندوایرانی *wan- و آن از هندواروپایی *wenh₁- است. معنای «می‌خواهد» از سنسکریت گرفته شده و در اوستایی این فعل تنها «چیره شدن» معنی می‌دهد. چهار واژهٔ دیگر از ریشهٔ دیگری‌اند: vayeiti «شکار می‌کند»، vītar- «دنبال‌کننده»، vyāna- «دنبال‌شده» و vāiti- «آزار و پیگرد». این‌ها بازماندهٔ هندواروپایی *weyh₁- «دنبال کردن، شکار کردن» (پوکورنی ص ۱۱۲۳) و هم‌ریشهٔ سنسکریت veti و لیتوانیایی vejù «دنبال می‌کنم»‌اند. پس جای دادن آن‌ها زیر *wen- نادرست است و پژوهش امروزی آن را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wenh₁-\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyh₁-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1146\", \"status\": \"partial\", \"note\": \"POK_03.txt l.5535 lists 'av. vanaiti, vanaoiti ‚siegt' ... vantṛ- ‚Gewinner' ... (av. vantar ‚Sieger')' under u̯en-, but the hunting words are at POK 1123-1124 under u̯ei- (POK_03.txt l.5216): 'av. ... vāy- (vayeiti, vīvāiti ‚jagt weg') ‚verfolgen, jagen', vyāna- ‚der Verfolgte', ... vītar- ‚Verfolger', vātay- ‚Verfolgung''.\"},\n            {\"ref\": \"KLN:1697\", \"status\": \"partial\", \"note\": \"KLN_1966.txt l.41202 s.v. venerate (p.1697): 'cogn. with OI. vanas-, ‘desire’, vanati ... Avestic vanaiti, ‘he wishes; is victorious’ ... fr. I.-E. base *wen-' — supports vanaiti only; no hunting words.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1350-1354 s.v. van-, vanaiti.vant-, vanant-; col. 1401 s.v. vā(y)-; col. 1439 s.v. vītar-; col. ~1408 s.v. vātay- (BRT.txt l.22547ff., 23433ff., 23462, 23978, 24698)\", \"stance\": \"partial\", \"note\": \"van- 'siegen' with vanaiti; 'j. vā(y)- V. ‚jagen' ... ‚jagen, jagend verfolgen' ... vyąsca vyānasca ... ‚der Verfolger und der Verfolgte' Yt 13.35 ... ai. vīti-, vyāna ... lit. vejù ‚ich jage nach''; 'vītar- m. ‚der nachjagt, Verfolger''; 'vātay- f. ‚Verfolgung', Bezeichnung eines strafbaren Delikts: vāiti'; 'vyāna- Adj., PPM.: s. vā(y)' — the hunting words are under vāy-, not van-.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 259\", \"stance\": \"partial\", \"note\": \"'av. vanaiti, vanaoiti „siegt“ (vgl. Bartholomae Airan. Wb. 1350 f.) ... vantā- (av. vantar „Sieger“) ... Über ai. veti „ersehnt“ usw. s. u. uei- „auf etwas losgehen“' — the *wei- words are kept apart.\"},\n            {\"src\": \"POK\", \"where\": \"p. 1123-1124 u̯ei- (POK_03.txt l.5212-5216)\", \"stance\": \"contradicts\", \"note\": \"'u̯ei- ... 1. ‚auf etwas losgehen' ... ‚worauf losgehen, es erstreben, erjagen' ... av. ... vāy- ‚verfolgen, jagen', vyāna- ‚der Verfolgte', ... vītar- ‚Verfolger', vātay- ‚Verfolgung'' — these words belong to a separate root.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"vânîtan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pahlavi wānīdan, present wān- 'to conquer, overcome, destroy' (Manichaean MP w’n-) is the Middle Persian continuation of Old Iranian *wan-aya- (causative with lengthened root vowel) to Av. van- 'conquer' < PIE *wenh₁-. Pokorny and Walde-Pokorny cite 'mpers. vanītan besiegen, schlagen', and Nyberg (vānītan 'to vanquish, to defeat') gives Av. van- as the source.\",\n          \"derivation_fa\": \"پهلوی wānīdan با ستاک wān- «شکست دادن، چیره شدن» (فارسی میانهٔ مانوی w’n-) بازماندهٔ ایرانی باستان *wan-aya- از ریشهٔ اوستایی van- «پیروز شدن» است. مکنزی، نیبرگ و پوکورنی همین را آورده‌اند و ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wenh₁-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1146\", \"status\": \"supports\", \"note\": \"POK_03.txt l.5535 'mpers. vanīdan ‚besiegen, schlagen''.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 87 (PHD.txt l.605)\", \"stance\": \"supports\", \"note\": \"'wānīdan, wān- [wn-ytn' | M w’n-yst] conquer, overcome, destroy.'\"},\n            {\"src\": \"NYB\", \"where\": \"Part II p. 202-203 s.v. vānītan (NYB_vol2_glossary.txt l.3933ff.)\", \"stance\": \"supports\", \"note\": \"'vānitan [w’nytn'], pres. 1st p. sg. vānom ... to vanquish, to defeat ... — Av. (1350) van-; MPrs pres. w’n-'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 259\", \"stance\": \"supports\", \"note\": \"'mp. vanītan „besiegen, schlagen“'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan\",\n          \"words\": \"vanâ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan vanā- f. (also root noun van-) 'tree' (Vd. 5.24, Yt 12) is a real word, = Skt. vána- n. 'tree, wood, forest' (Vedic root noun ván-), from Indo-Iranian *wán-. Its connection with PIE *wen- 'desire' is disputed. Uhlenbeck and Watkins posit a semantic chain 'desired place → pasture/forest' after Germanic *winjō 'pasture'. Walde-Pokorny I 259 judges the semantic transfer 'unglaubhaft', and Pokorny 1146 does not include vana- under u̯en-. Nourai's gloss 'hunting place' and his note (after Shipley, OEW 434) about Indian hunters trading skins under banyan trees have no support in the standard sources.\",\n          \"derivation_fa\": \"اوستایی vanā- (و van-) «درخت» واژه‌ای واقعی است و با سنسکریت vána- «درخت، بیشه» برابر است و هر دو از هندوایرانی *wán- می‌آیند. ولی پیوند آن با ریشهٔ *wen- «خواستن» قطعی نیست. واتکینز آن را می‌پذیرد، اما والده-پوکورنی این تحول معنایی را باورنکردنی می‌داند و پوکورنی آن را زیر این ریشه نیاورده است. معنای «جای شکار» و داستان داد و ستد پوست زیر درخت بانیان هم در منابع معتبر نیامده است. پس این ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/वन\"],\n          \"ref_check\": [\n            {\"ref\": \"WLD1:259\", \"status\": \"partial\", \"note\": \"WLD_Bd1_pages.txt leaf 268 (p.259): 'wird auch ai. vana-m n. „Wald, Baum, Holz“, vanā f. „Reibholz“, av. vanā-, mp. van, np. bun „Baum“ ... zu idg. uen- gezogen (Uhlenbeck Ai. Wb. 270). Der Bedeutungsübergang ist jedoch innerhalb der indischen Sippe unglaubhaft.' — the word is there, but WLD rejects the link Nourai draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1353-1354 s.v. van-, vanā- (BRT.txt l.22613, 22633-22634)\", \"stance\": \"partial\", \"note\": \"'j. vanā- f. ‚Baum': yaϑa masyayå vana ... V.5.24 ... Vgl. van: — np. bun ‚Stamm', afγ. vana ‚Baum'; ai. vgl. vána- n. ‚Baum, Wald'. — Pü.: van.' — no root connection given.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wen-¹ §12\", \"stance\": \"supports\", \"note\": \"'12. Suffixed basic form *wen-o- in Sanskrit vanam, forest: WANDEROO.'\"},\n            {\"src\": \"POK\", \"where\": \"p. 1146-1147\", \"stance\": \"silent\", \"note\": \"Pokorny's u̯en- entry (POK_03.txt l.5534ff.) lists no word for 'tree/forest'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"van\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pahlavi wan [wn'] 'tree; stock, stem' (e.g. wan ī harwisp-tōhmag 'the Tree of All Seeds') directly continues Av. vanā-/van- 'tree'. Bartholomae notes that the Pahlavi translation renders vanā- by van, and Nyberg derives Phl. van from Av. van-/vana-.\",\n          \"derivation_fa\": \"پهلوی wan «درخت؛ تنه، ساقه» (مانند wan ī harwisp-tōhmag «درخت همه‌تخمه») بازماندهٔ مستقیم اوستایی vanā- «درخت» است. مکنزی، نیبرگ و بارتولومه این را تأیید می‌کنند و ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/بن\"],\n          \"ref_check\": [\n            {\"ref\": \"WLD1:259\", \"status\": \"supports\", \"note\": \"WLD_Bd1_pages.txt leaf 268: 'av. vanā-, mp. van, np. bun „Baum“'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 87 (PHD.txt l.605; PHD_mackenzie.txt l.5159)\", \"stance\": \"supports\", \"note\": \"'wan [wn' | N bun] tree; stock, stem. ~ ī Šurgānīg: pistachio tree. ~ ī was-tōhmag: the Tree of Many Seeds.'\"},\n            {\"src\": \"NYB\", \"where\": \"Part II p. 202 s.v. van (l.3927)\", \"stance\": \"supports\", \"note\": \"'van [wn'] tree ... — Av. (1353) van- or (1354) vana-; Paz. van ...; NP van ‘wood, forest’ (probably lw., but cf nār-bun, nār-vun, nār-van ‘the pomegranate tree’).'\"},\n            {\"src\": \"HRN\", \"where\": \"no. 228 (HRN.txt l.2351ff.)\", \"stance\": \"supports\", \"note\": \"'228. (1)bun ‚(Baum)stamm, -Stumpf' ... aw. vanā- ‚Baum'; phlv. van; ai. vána- ‚Baum, Wald'.'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"van; bon 2 (ban)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"bon/bun 2 'tree, bush, (tree) stem' as in sarv-bun 'cypress tree', gol-bun 'rose bush', xār-bun 'thorn bush' (Ferdowsi's 'ای سرو بن') is the late Middle Persian bun < earlier wan, with the initial w- becoming b- (as in wahār > bahār) and a > u next to the labials. Horn 228, Hübschmann p. 31, MacKenzie (wan, N bun) and Wiktionary keep it apart from homonymous bun 'base, bottom' < Av. bū̆na- < *bʰudʰ-no-. van 'tree' (Mo'in: 'the ash tree, Fraxinus') and nār-van/nārvan 'elm, pomegranate tree' keep the old w-. Nyberg thinks free van may be a dialect loan, and Mo'in derives nārvan from nār + Av. vanā-. All forms are real and descend from Av. vanā-, so the edge from Phl. wan is confirmed. Whether they ultimately go back to *wen- is a separate question (see node 3).\",\n          \"derivation_fa\": \"«بُن» به معنی «درخت، بوته» در «سروبن، گلبن، خاربن» (بیت فردوسی: «ای سرو بن») از فارسی میانهٔ متأخر bun و آن از wan پیشین است. واو آغازی به ب بدل شده (مانند wahār > بهار) و a کنار حرف لبی به u گراییده است. هرن، هوبشمان، مکنزی و ویکی‌واژه این «بن» را از «بن» به معنی «بنیاد، ته» (اوستایی būna-) جدا می‌دانند. «وَن» (در فرهنگ معین: درخت زبان‌گنجشک) و «ناروَن/ناروان» واو کهن را نگه داشته‌اند. معین «نارون» را از «نار» و اوستایی vanā- می‌گیرد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/بن\",\n            \"https://vajehyab.com/moein/ون\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"WLD1:259\", \"status\": \"supports\", \"note\": \"WLD_Bd1_pages.txt leaf 268: 'mp. van, np. bun „Baum“'.\"},\n            {\"ref\": \"AEF:287\", \"status\": \"not_checked\", \"note\": \"Khaleqi-Motlaq's Persian translation of Horn is not online; its source Horn no. 228 (HRN.txt l.2351) supports: 'bun ‚(Baum)stamm, -Stumpf' ... aw. vanā- ‚Baum'; phlv. van', with note 228 (l.9899) 'servbun ‚Cypressenbaum' ..., xārbun ..., sowie nārven, nārvan ‚Ulme''.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"p. 31 no. 228 (HUB.txt leaf 42)\", \"stance\": \"supports\", \"note\": \"'np. bun ‚Baum' (in gōz-bun, sarv-bun etc.) = zd. vana- ‚Baum' = phl. van'.\"},\n            {\"src\": \"PHD\", \"where\": \"p. 87\", \"stance\": \"supports\", \"note\": \"'wan [wn' | N bun] tree; stock, stem.'\"},\n            {\"src\": \"NYB\", \"where\": \"Part II p. 202\", \"stance\": \"supports\", \"note\": \"'NP van ‘wood, forest’ (probably lw., but cf nār-bun, nār-vun, nār-van ‘the pomegranate tree’)'.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 1, footnote on نارون (BQT_v1_pages.txt l.7165)\", \"stance\": \"supports\", \"note\": \"Mo'in: 'نارون ... از: نار (انار) + ون (اوستایی ...)' — nārvan from nār + Av. van-.\"},\n            {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/ون\", \"stance\": \"partial\", \"note\": \"'(وَ) (اِ.) درخت زبان گنجشک' — van = ash tree; no etymology given.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Avestan\",\n          \"words\": \"vana-vaxša\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"No Avestan *vana-vaxša- 'growing in the woods' is attested: Bartholomae has no such word. It is a reconstruction by Friedrich Müller (WZKM 7, 368), made from vanā- 'tree, forest' + vaxš- 'to grow' to explain Phl. wanafšag. Hübschmann (Persische Studien p. 31, no. 231) rejected it ('Mir nicht wahrscheinlich'), and Nourai's own note cites that doubt. Modern treatments (Wiktionary s.v. wnpšk', after Bailey and Martirosyan) call wanafšag of uncertain origin. Bailey proposes an Iranian colour word *van- 'blue/dark'. Martirosyan proposes a Mediterranean flower name related to Gk. íon (*wíon) and Lat. viola. The form should at least be starred, and the derivation is not accepted.\",\n          \"derivation_fa\": \"صورت اوستایی vana-vaxša «روییده در بیشه» در هیچ متن اوستایی نیامده و در فرهنگ بارتولومه نیست. این صورت را فریدریش مولر از vanā- «درخت، بیشه» و vaxš- «روییدن» ساخته تا «بنفشه» را توضیح دهد. هوبشمان آن را نپذیرفت و خود نورایی هم به این تردید اشاره کرده است. پژوهش امروزی ریشهٔ wanafšag را نامعلوم می‌داند. بیلی آن را از یک نام رنگ ایرانی *van- «کبود» و مارتیروسیان از نام گلی مدیترانه‌ای هم‌ریشه با یونانی íon و لاتینی viola می‌گیرد. پس این صورت ساختگی است و ادعا رد می‌شود.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/wnpšk'\"],\n          \"ref_check\": [\n            {\"ref\": \"AEF:291\", \"status\": \"not_checked\", \"note\": \"AEF not online; its source Horn no. 231 (HRN.txt l.2385-2389) gives only 'banefše ‚Veilchen' ... phlv. vanawšak ... ar. LW. banafsaj' — no Avestan form; the *vanavaxša idea comes from Hübschmann's report of F. Müller.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"p. 31 no. 231 (HUB.txt l.1029-1031)\", \"stance\": \"contradicts\", \"note\": \"'231. Np. bunafša ‚Veilchen' = phl. vanavšak (für vanafšak) nach Fr. Müller WZKM. 7, 368 = zd. *vanavaxša- (also = ‚im Walde wachsend'). Mir nicht wahrscheinlich.'\"},\n            {\"src\": \"BRT\", \"where\": \"whole dictionary (grep 'vanavax|vana.vax')\", \"stance\": \"silent\", \"note\": \"No such Avestan word.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 231\", \"stance\": \"silent\", \"note\": \"Horn gives the Pahlavi and Arabic forms only, no Avestan etymon.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"vana-vašak\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Pahlavi word is real: wanafšag [wnpšk'] 'violet' (MacKenzie). Horn and Hübschmann quote it as vanawšak/vanavšak from the Bundahišn, with Pazand vanavša. Nourai's hyphenated 'vana-vašak' presupposes his compound with vana- 'forest', which is not established (see node 6). The word itself and its gloss are confirmed. Its descent from *vana-vaxša- is unproven, which Nourai's own note (HUB) concedes. Hence plausible.\",\n          \"derivation_fa\": \"واژهٔ پهلوی wanafšag «بنفشه» واقعی است و مکنزی آن را آورده است. هرن و هوبشمان آن را به صورت vanawšak از بندهش و پازند vanavša نقل کرده‌اند. ولی خط تیرهٔ «vana-vašak» در نوشتهٔ نورایی آن را ترکیبی با vana- «بیشه» نشان می‌دهد و این ترکیب ثابت نشده است. پس خود واژه درست است ولی اشتقاق آن از *vana-vaxša- تنها با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/wnpšk'\"],\n          \"ref_check\": [\n            {\"ref\": \"AEF:291\", \"status\": \"not_checked\", \"note\": \"AEF not online; Horn no. 231 (its source) has 'phlv. vanawšak, vanawša ‚Veilchen' (Bund.)' — supports the word, not the compound analysis.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 87 (PHD.txt l.605)\", \"stance\": \"supports\", \"note\": \"'wanafšag [wnpšk' | N bunafša] violet.'\"},\n            {\"src\": \"HUB\", \"where\": \"p. 31 no. 231; p. 70 (HUB.txt l.5459-5460)\", \"stance\": \"partial\", \"note\": \"'banafša ‚Veilchen' = phl. vanavšak Bdh. p. 66, Z. 17, paz. vanavša' — the word yes; the vana-vaxša etymology 'Mir nicht wahrscheinlich'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 231 (l.2385)\", \"stance\": \"supports\", \"note\": \"'phlv. vanawšak, vanawša ‚Veilchen' (Bund.)'.\"},\n            {\"src\": \"NYB\", \"where\": \"Part II glossary\", \"stance\": \"silent\", \"note\": \"grep 'wanafš|vanafšak|vanavšak' — no entry.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"banafšeh; banafsh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"banafše/bonafše/benafše 'violet (Viola odorata)' < MP wanafšag, with the regular initial w- > b- and the suffix -ag > -a/-e. banafš 'violet, blue' is a back-formation (Horn: bunafš 'blau', Šāhnāme). Arabic banafsaj and Syriac forms are loans from Persian. Mazandarani venewše and the Tabari and Gilaki forms keep the old v-/w- (Horn, Mo'in). The descent from Pahlavi is confirmed. The deeper origin is unknown (see node 6).\",\n          \"derivation_fa\": \"«بنفشه» (با فتحه، ضمه یا کسرهٔ «ب») از فارسی میانهٔ wanafšag است. واو آغازی به ب و پسوند -ag به -a/-e بدل شده است. «بنفش» به معنی «رنگ کبود» از خود «بنفشه» برگرفته شده است. عربی «بنفسج» وام‌واژه‌ای از فارسی است. مازندرانی venewše و گویش‌های تبری و گیلکی واو کهن را نگه داشته‌اند (هرن، معین در حاشیهٔ برهان). ادعای نورایی در پیوند با پهلوی درست است، ولی ریشهٔ کهن‌تر واژه نامعلوم است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/بنفشه\"],\n          \"ref_check\": [\n            {\"ref\": \"AEF:291\", \"status\": \"not_checked\", \"note\": \"AEF not online; Horn no. 231 (HRN.txt l.2385) supports: 'banefše ‚Veilchen', bunefše, binefše; bunefš ‚blau' (Šāhn. I, 48 Vers 265 ...); māz. venewše, phlv. vanawšak ... ar. LW. banafsaj'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 231\", \"stance\": \"supports\", \"note\": \"quoted in ref_check.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 31, p. 70, §127 (HUB.txt l.8409)\", \"stance\": \"supports\", \"note\": \"'banafša ‚Veilchen' neben binafša, bunafša, arab. banafsaj, phl. vanavšak' and 'unsicheren [Ursprungs] in banafša ‚Veilchen' H. 231'.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 1, s.v. بنفشه, footnote 1 (BQT_v1_pages.txt l.21100, 21126-21128; printed p. ~309)\", \"stance\": \"supports\", \"note\": \"Headword 'بنفشه ... گلی باشد معروف ... ومعرب آن بنفسج باشد'; Mo'in's footnote: 'پهلوی vanafšak ... هرن ... طبری ... مازندرانی کنونی ... گیلکی ...' — Pahlavi source, no Avestan etymon.\"},\n            {\"src\": \"PHD\", \"where\": \"p. 87\", \"stance\": \"supports\", \"note\": \"'wanafšag [wnpšk' | N bunafša] violet.'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"van\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. van- (vanaiti, vanaoiti) 'to conquer, overcome' and Old Persian van- 'overpower, pack down' (imperfect passive avaniya 'was packed down', DSf 25, 29, in the Susa foundation charter: the earth was dug down and the gravel packed) both continue Indo-Iranian *wan- < PIE *wenh₁-. Their cognates are Skt. vanati 'desires, gains', Goth. winnan and English win. Kent's lexicon has this entry on p. 206, so Nourai's 'KNT:260' is a misprint for 206.\",\n          \"derivation_fa\": \"اوستایی van- (vanaiti) «پیروز شدن، چیره شدن» و پارسی باستان van- «فشردن، کوبیدن» (فعل مجهول avaniya در کتیبهٔ ساختمانی شوش DSf) هر دو از هندوایرانی *wan- و آن از هندواروپایی *wenh₁- است. سنسکریت vanati، گوتی winnan و انگلیسی win هم‌ریشهٔ آن‌اند. کنت این را در واژه‌نامهٔ خود در صفحهٔ ۲۰۶ آورده است و شمارهٔ ۲۶۰ در کتاب نورایی خطای چاپی است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wenh₁-\"],\n          \"ref_check\": [\n            {\"ref\": \"KNT:260\", \"status\": \"supports\", \"note\": \"Entry is on Kent p. 206, not 260 (KNT_full.txt l.28751, page number 206 a few lines above): 'van- vb. ‘overpower, pack down’: Av. van- ‘superare’, pres. vanaiti (Bthl. AiW 1350 ...), Skt. vánati ‘desires, gets by effort’, Gt. winnan ‘suffer’, NEng. win. — avaniya impf. pass. (§220) DSf 25, 29'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1350-1353 s.v. van- (BRT.txt l.22547ff.)\", \"stance\": \"supports\", \"note\": \"'vanaiti ... mit ni- ... völlig besiegen'; 'vanaiti-vant- Adj. ‚sieghaft''; 'vananā- f. ‚Sieg''.\"},\n            {\"src\": \"POK\", \"where\": \"p. 1146\", \"stance\": \"supports\", \"note\": \"'av. vanaiti, vanaoiti ‚siegt''.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 259\", \"stance\": \"supports\", \"note\": \"'av. vanaiti, vanaoiti „siegt“ (vgl. Bartholomae Airan. Wb. 1350 f.)'.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"vanîja; vana\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both words are real Sanskrit: vaṇij- / vāṇija- 'merchant, trader' and vána- 'forest, tree, wood'. The glosses and the link between them are not supported. vaṇij- means 'merchant' in general (Ṛgveda onward), never 'trader of animal skins (obtained from hunting)'. It is not derived from vana 'forest'. Wiktionary reconstructs *wn̥h₁-h₂éǵ-s ('one who drives for gain', from *wenh₁- + *h₂eǵ-), and Watkins tentatively derives it from *wn̥-ig- 'seeking to gain'. Both thus tie it to the root through 'gain', not through hunting or forests. vána- (Indo-Iranian *wán-) is linked to *wen- only by Uhlenbeck and Watkins. Walde-Pokorny rejects that link, and Wiktionary leaves the word as Indo-Iranian *wán- without a PIE etymon (see node 3). Nourai's 'hunting/skin-trade' explanation, taken from Shipley, has no support in the sources.\",\n          \"derivation_fa\": \"هر دو واژهٔ سنسکریت واقعی‌اند: vaṇij- / vāṇija- «بازرگان، سوداگر» و vána- «بیشه، درخت». ولی معنایی که نورایی برای vaṇij داده («سوداگر پوست جانوران شکاری») در هیچ منبعی نیامده و vaṇij از vana «بیشه» ساخته نشده است. ویکی‌واژه آن را از *wenh₁- و *h₂eǵ- («کسی که برای سود می‌راند») و واتکینز با تردید از *wn̥-ig- «سودجو» می‌داند؛ پس پیوند آن با ریشه از راه معنای «سود» است، نه شکار. پیوند vana با *wen- هم مورد اختلاف است. پس این گره را پژوهش امروزی رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/वणिज्\",\n            \"https://en.wiktionary.org/wiki/वन\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"OEW:434\", \"status\": \"not_checked\", \"note\": \"Shipley 1984 lending-only; not accessible.\"},\n            {\"ref\": \"AHD:1549\", \"status\": \"partial\", \"note\": \"1985 Watkins text (AHD_watkins1985.txt l.1142, wen-¹ §12-13): '*wen-o- in Sanskrit vanam, forest: WANDEROO. 13. Possibly zero-grade suffixed form *wn-ig- in Sanskrit vaṇik, vāṇijaḥ, merchant (? < \\\"seeking to gain\\\"): BANIAN' — supports both words under wen-, but with the sense 'merchant' via 'gain', not 'skin trader' or 'forest'.\"},\n            {\"ref\": \"WLD1:259\", \"status\": \"contradicts\", \"note\": \"WLD_Bd1_pages.txt leaf 268: ai. vana-m 'Wald, Baum, Holz' ... 'zu idg. uen- gezogen (Uhlenbeck ...). Der Bedeutungsübergang ist jedoch innerhalb der indischen Sippe unglaubhaft.' No mention of vaṇij.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AID\", \"where\": \"s.v. Banyá, Banik, Bankar (AID.txt l.835-860)\", \"stance\": \"partial\", \"note\": \"'Banyá. [Hindi, from the Sanskrit banik, a merchant.] A Hindu trader, shopkeeper, or money-changer'; 'Bankar. [Bengali, from ban, Sanskrit wana, a forest, and kar, revenue]' — the two words are separate, and vaṇij means simply 'merchant'.\"},\n            {\"src\": \"HJB\", \"where\": \"p. 63 s.v. BANYAN (1) (HJB.txt l.2859)\", \"stance\": \"partial\", \"note\": \"'The word was adopted from Vaniya, a man of the trading caste (in Gujarati vāṇiyo), and that comes from Skt. vaṇij, ‘a merchant.’' — no animal-skin sense.\"},\n            {\"src\": \"POK\", \"where\": \"p. 1146\", \"stance\": \"silent\", \"note\": \"Neither vaṇij nor vana is listed under u̯en-.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"banian; banyan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"banian/banyan 'Hindu trader' (16th c.) comes from Portuguese baniane/baniano, probably via Arabic baniyān. The source is Gujarati vāṇiyo 'man of the trading caste', from Skt. vāṇija- / vaṇij- 'merchant'. The tree name banyan (Ficus benghalensis) was first given to a famous tree near Gombroon (Bandar Abbas), under which the Banian traders of that port had built a small pagoda (Tavernier, Hobson-Jobson, Klein). From there it spread to the species in general. The English words and their source are correct. The 'animal-skin' story behind them (node 10) is not.\",\n          \"derivation_fa\": \"انگلیسی banian/banyan «بازرگان هندو» در سدهٔ شانزدهم از پرتغالی baniano (احتمالاً از راه عربی baniyān) و آن از گجراتی vāṇiyo «مرد طبقهٔ بازرگان» و سنسکریت vaṇij- «بازرگان» وام گرفته شده است. نام درخت banyan نخست به درخت مشهوری نزدیک گمبرون (بندرعباس) داده شد. بازرگانان بانیان در آن بندر زیر این درخت بتکدهٔ کوچکی ساخته بودند (تاورنیه، هابسن-جابسن، کلاین). سپس این نام به همهٔ درختان این گونه گسترش یافت. پس خود واژه‌ها درست‌اند، ولی داستان «داد و ستد پوست» در گره پیشین پذیرفتنی نیست.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/banyan\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:104\", \"status\": \"supports\", \"note\": \"Watkins 1985 index 'BANIAN wen-1' (AHD_watkins1985.txt l.1276) and root entry wen-¹ §13 '... merchant (? < \\\"seeking to gain\\\"): BANIAN'. AHD:104 refers to the main dictionary page s.v. banian/banyan (not online); the appendix supports the chain.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. banian, banyan tree (KLN_1966.txt l.4385, 4409)\", \"stance\": \"supports\", \"note\": \"'banian, n., a Hindu merchant. — Hind. vanija, ‘a trader’, fr. OI. vaṇij, ‘merchant’. Cp. banyan tree.' and 'banyan tree ... Orig. ‘the tree under which the banyans (= Hindu merchants) settled near Gombroon (now called Bandar Abbas)’; see banian. See Yule-Burnell, Hobson-Jobson, p.65.'\"},\n            {\"src\": \"HJB\", \"where\": \"p. 63-65 s.v. BANYAN, BANYAN-TREE (HJB.txt l.2859, 2905)\", \"stance\": \"supports\", \"note\": \"'The name appears to have been first bestowed popularly on a famous tree of this species growing near Gombroon, under which the Banyans or Hindu traders settled at that port, had built a little pagoda.'\"},\n            {\"src\": \"AID\", \"where\": \"s.v. Banyan (AID.txt l.860-861)\", \"stance\": \"supports\", \"note\": \"'Banyan. A corruption of Banyá. Banyan. The name given in English to the Indian fig tree — ficus indica — known in Sanskrit as wata'.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-17T00:08:48.891Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-542.json (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:08:52.398Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -i 's/\"where\": \"p\\. 87 (PHD/\"where\": \"s.v. (PHD/; s/\"where\": \"p\\. 87\"/\"where\": \"s.v. wan (PHD.txt l.605)\"/' data/verification/page-542.json; grep -c \"p\\. 87\" data/verification/page-542.json; python3 -m json.tool data/verification/page-542.json >/dev/null && python3 tools/verify_check.py 542"
}
```


### [2026-10-17T00:08:53.149Z] TOOL RESULT

```
1
nodes verified: 15/15
node verdicts: {'confirmed': 9, 'plausible': 3, 'disputed': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'partial': 5, 'not_checked': 6, 'contradicts': 1}
books consulted: {'supports': 33, 'silent': 6, 'partial': 7, 'contradicts': 2} | by book: {'BRT': 6, 'PHD': 6, 'HRN': 5, 'NYB': 5, 'POK': 5, 'HUB': 4, 'WLD': 3, 'KLN': 2, 'AHD': 2, 'BQT': 2, 'AID': 2, 'HJB': 2, 'ARY': 1, 'IEC': 1, 'SKT': 1, 'MON': 1}
```


## [2026-10-17T00:08:54.470Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; grep -n \"p\\. 87\" data/verification/page-542.json | cut -c1-200"
}
```


### [2026-10-17T00:08:54.806Z] TOOL RESULT

```
56:            {"src": "PHD", "where": "p. 87 s.v. wāmīdan (PHD.txt l.605)", "stance": "supports", "note": "'wāmīdan, wām- [w’m-ytn'] vomit.' — no vātāk entry found (grep 'wādag|vātāk')."},
```


## [2026-10-17T00:08:56.483Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -i 's/\"where\": \"p\\. 87 s\\.v\\. wāmīdan/\"where\": \"s.v. wāmīdan/' data/verification/page-542.json; python3 -m json.tool data/verification/page-542.json >/dev/null && python3 tools/verify_check.py 542 | grep -c PROBLEM"
}
```


### [2026-10-17T00:08:56.961Z] TOOL RESULT

```
0
```


## [2026-10-17T00:09:04.275Z] TOOL CALL #68: SubagentHandback

```json
{
 "message": "I verified page 542 (book p. 512) and wrote `/home/sfmqrb/git/rishe-private/data/verification/page-542.json`. It is valid JSON and `verify_check.py 542` shows 0 PROBLEM lines, with all 15 nodes covered.\n\n**Counts:**\n- **Roots** (2): both confirmed (Wem, Wen part 1). Welâ is a redirect and was skipped.\n- **Nodes** (15): 9 confirmed, 3 plausible, 3 disputed, 0 transcription_suspect.\n\n**Disputed:**\n- **Wen #1, Avestan vayeiti / vîtar / vyâna / vâti:** these four \"hunt / pursue / persecution\" words come from a different root, PIE *weyh₁- (Pokorny 1123, Bartholomae under vāy-), not from *wen-. vanaiti and vantar in the same node are correct.\n- **Wen #6, Avestan \"vana-vaxša\":** this form is not attested. It is F. Müller's reconstruction, which Hübschmann (p. 31) rejected, and modern sources treat MP wanafšag as of uncertain origin.\n- **Wen #10, Sanskrit vaṇij / vana:** vaṇij just means \"merchant\", never \"trader of animal skins\", and it does not come from vana \"forest\". Watkins and Wiktionary link it to *wen- through the sense \"seeking gain\". Walde-Pokorny I 259 also rejects linking vana to *wen-.\n\n**Plausible:**\n- **Wem #2:** vāmīdan is confirmed. vātāk \"saliva\" is known only from Pokorny and Bartholomae, and MacKenzie and Nyberg do not have it.\n- **Wen #3:** the vanā \"tree\" link to *wen- is doubted by Walde-Pokorny.\n- **Wen #7:** wanafšag is real, but the compound analysis \"vana-vašak\" is unproven.\n\n**Book misprint:** the chart cites KNT:260 for the van- node, but the entry is on Kent p. 206.\n\n**Extraction errors:** none. The JSON matches the printed page (checked against `site/pages/542.jpg`)."
}
```


### [2026-10-17T00:09:04.552Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
