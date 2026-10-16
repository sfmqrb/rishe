# Verification process log — verify-page-519


## [2026-10-16T05:13:01.541Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 519 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-519.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-519.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-519.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 519` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.583Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:05.048Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:05.078Z] TOOL RESULT

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


## [2026-10-16T05:13:05.551Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-519.txt"
}
```


### [2026-10-16T05:13:05.571Z] TOOL RESULT

```
1	=== PDF page 519 (book page 489) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Upo : to, from below  (refs POK:1106; KLN:1105)  PART 1
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:1106; KLN:1105 | upa : to, toward ; upâ : to, toward
5	  #2 (parent #1) [Pahlavi] refs=HRN:33; AEF:190,191 | pat : to, toward ; pa : to, toward ; pad : to, toward | NOTE: HRN:33 claims these prefixes are a combination of Avestan "upa" and "paiti". See AEF:190,191 for further discussion.
6	    #3 (parent #2) [Persian] refs=MON:605; AEF:190,191 | beh «به ( به ۲ )» : to, toward | NOTE: See "Per 3" for a different derivation
7	  #4 (parent #1) [Avestan] refs=HRN:41,65,71,72,73 | upa-diti : to (in) sight, apparent ☞Dheye ; upa-sad : to agreement, selection ☞Sed ; upa-var : in belief ☞Wer 1 ; upa-drava : to good health ☞Deru 1 ; upa-gâh : to time, morning ; upa-ni-dâ : hidden ☞Dhe 2
8	    #5 (parent #4) [Persian] refs=BQT:2230,373,406 | padîd «پدید ( پدیده ، پدیدار )» : apparent ; pasand «پسند ( پسندیدن )» : selection ; bâvar «باور» : belief ; bedrŭd «بدرود ( پدرود )» : farewell ; pegâh «پگاه» : early morning ; penhân «پنهان» : hidden
9	  #6 (parent #1) [Avestan] refs=POK:916 | upa-skambem : for support, a column or pillar ☞Skabh
10	    #7 (parent #6) [Persian] refs=POK:916; BQT:410; MON:798; FRS:183 | pečkam «پچکم ( بچکم ، پشکم ، بشکم )» : roof on columns, a room open all around, porch
11	#8 (parent #0) [Germanic] refs=AHD | upp : up ; upanaz : open up ; ubilaz : over limit, evil
12	  #9 (parent #8) [English] refs=None | up ; open ; evil
13	#10 (parent #0) [Latin] refs=AHD | s-up : to below, under
14	  #11 (parent #10) [French] refs=None | sujet ; sublime'
15	    #12 (parent #11) [Persian] refs=MON:1944,1952 |  | extra: سوژه ، سوبلمه
16	  #13 (parent #10) [English] refs=AHD | sub- : under ; subject ; sublime ; submarine
17	
```


## [2026-10-16T05:13:06.206Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-519.json"
}
```


### [2026-10-16T05:13:06.232Z] TOOL RESULT

```
1	{
2	  "pdf_page": 519,
3	  "book_page": 489,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Upo",
8	        "lang": "Indo-European",
9	        "refs": "POK:1106; KLN:1105",
10	        "gloss": "to, from below"
11	      },
12	      "part": 1,
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Avestan / Old Persian",
18	          "refs": "POK:1106; KLN:1105",
19	          "words": [
20	            {"translit": "upa", "gloss": "to, toward", "script": null},
21	            {"translit": "upâ", "gloss": "to, toward", "script": null}
22	          ],
23	          "script_extra": null,
24	          "note": null,
25	          "quote": null
26	        },
27	        {
28	          "id": 2,
29	          "parent": 1,
30	          "lang": "Pahlavi",
31	          "refs": "HRN:33; AEF:190,191",
32	          "words": [
33	            {"translit": "pat", "gloss": "to, toward", "script": null},
34	            {"translit": "pa", "gloss": "to, toward", "script": null},
35	            {"translit": "pad", "gloss": "to, toward", "script": null}
36	          ],
37	          "script_extra": null,
38	          "note": "HRN:33 claims these prefixes are a combination of Avestan \"upa\" and \"paiti\". See AEF:190,191 for further discussion.",
39	          "quote": null
40	        },
41	        {
42	          "id": 3,
43	          "parent": 2,
44	          "lang": "Persian",
45	          "refs": "MON:605; AEF:190,191",
46	          "words": [
47	            {"translit": "beh", "gloss": "to, toward", "script": "به ( به ۲ )"}
48	          ],
49	          "script_extra": null,
50	          "note": "See \"Per 3\" for a different derivation",
51	          "quote": null
52	        },
53	        {
54	          "id": 4,
55	          "parent": 1,
56	          "lang": "Avestan",
57	          "refs": "HRN:41,65,71,72,73",
58	          "words": [
59	            {"translit": "upa-diti", "gloss": "to (in) sight, apparent", "script": null, "see": ["Dheye"]},
60	            {"translit": "upa-sad", "gloss": "to agreement, selection", "script": null, "see": ["Sed"]},
61	            {"translit": "upa-var", "gloss": "in belief", "script": null, "see": ["Wer 1"]},
62	            {"translit": "upa-drava", "gloss": "to good health", "script": null, "see": ["Deru 1"]},
63	            {"translit": "upa-gâh", "gloss": "to time, morning", "script": null},
64	            {"translit": "upa-ni-dâ", "gloss": "hidden", "script": null, "see": ["Dhe 2"]}
65	          ],
66	          "script_extra": null,
67	          "note": null,
68	          "quote": null
69	        },
70	        {
71	          "id": 5,
72	          "parent": 4,
73	          "lang": "Persian",
74	          "refs": "BQT:2230,373,406",
75	          "words": [
76	            {"translit": "padîd", "gloss": "apparent", "script": "پدید ( پدیده ، پدیدار )"},
77	            {"translit": "pasand", "gloss": "selection", "script": "پسند ( پسندیدن )"},
78	            {"translit": "bâvar", "gloss": "belief", "script": "باور"},
79	            {"translit": "bedrŭd", "gloss": "farewell", "script": "بدرود ( پدرود )"},
80	            {"translit": "pegâh", "gloss": "early morning", "script": "پگاه"},
81	            {"translit": "penhân", "gloss": "hidden", "script": "پنهان"}
82	          ],
83	          "script_extra": null,
84	          "note": null,
85	          "quote": {
86	            "text": "بخسب امشب و بامداد پگاه - برو تا به ایوان او بی سپاه",
87	            "poet": "Ferdowsî"
88	          }
89	        },
90	        {
91	          "id": 6,
92	          "parent": 1,
93	          "lang": "Avestan",
94	          "refs": "POK:916",
95	          "words": [
96	            {"translit": "upa-skambem", "gloss": "for support, a column or pillar", "script": null, "see": ["Skabh"]}
97	          ],
98	          "script_extra": null,
99	          "note": null,
100	          "quote": null
101	        },
102	        {
103	          "id": 7,
104	          "parent": 6,
105	          "lang": "Persian",
106	          "refs": "POK:916; BQT:410; MON:798; FRS:183",
107	          "words": [
108	            {"translit": "pečkam", "gloss": "roof on columns, a room open all around, porch", "script": "پچکم ( بچکم ، پشکم ، بشکم )"}
109	          ],
110	          "script_extra": null,
111	          "note": null,
112	          "quote": {
113	            "text": "از تو خالی نگار خانهٔ جم - فرش دیبا کشیده بر بچکم",
114	            "poet": "Rūdakî"
115	          }
116	        },
117	        {
118	          "id": 8,
119	          "parent": 0,
120	          "lang": "Germanic",
121	          "refs": "AHD",
122	          "words": [
123	            {"translit": "upp", "gloss": "up", "script": null},
124	            {"translit": "upanaz", "gloss": "open up", "script": null},
125	            {"translit": "ubilaz", "gloss": "over limit, evil", "script": null}
126	          ],
127	          "script_extra": null,
128	          "note": null,
129	          "quote": null
130	        },
131	        {
132	          "id": 9,
133	          "parent": 8,
134	          "lang": "English",
135	          "refs": null,
136	          "words": [
137	            {"translit": "up", "gloss": null, "script": null},
138	            {"translit": "open", "gloss": null, "script": null},
139	            {"translit": "evil", "gloss": null, "script": null}
140	          ],
141	          "script_extra": null,
142	          "note": null,
143	          "quote": null
144	        },
145	        {
146	          "id": 10,
147	          "parent": 0,
148	          "lang": "Latin",
149	          "refs": "AHD",
150	          "words": [
151	            {"translit": "s-up", "gloss": "to below, under", "script": null}
152	          ],
153	          "script_extra": null,
154	          "note": null,
155	          "quote": null
156	        },
157	        {
158	          "id": 11,
159	          "parent": 10,
160	          "lang": "French",
161	          "refs": null,
162	          "words": [
163	            {"translit": "sujet", "gloss": null, "script": null},
164	            {"translit": "sublime'", "gloss": null, "script": null}
165	          ],
166	          "script_extra": null,
167	          "note": null,
168	          "quote": null
169	        },
170	        {
171	          "id": 12,
172	          "parent": 11,
173	          "lang": "Persian",
174	          "refs": "MON:1944,1952",
175	          "words": [],
176	          "script_extra": "سوژه ، سوبلمه",
177	          "note": null,
178	          "quote": null
179	        },
180	        {
181	          "id": 13,
182	          "parent": 10,
183	          "lang": "English",
184	          "refs": "AHD",
185	          "words": [
186	            {"translit": "sub-", "gloss": "under", "script": null},
187	            {"translit": "subject", "gloss": null, "script": null},
188	            {"translit": "sublime", "gloss": null, "script": null},
189	            {"translit": "submarine", "gloss": null, "script": null}
190	          ],
191	          "script_extra": null,
192	          "note": null,
193	          "quote": null
194	        }
195	      ]
196	    }
197	  ]
198	}
199	
```


## [2026-10-16T05:13:12.821Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; cat tools/verify_check.py | head -150"
}
```


### [2026-10-16T05:13:13.211Z] TOOL RESULT

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


## [2026-10-16T05:13:17.027Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','AEF','MON','BQT','FRS','AHD']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]);print()\n\"; ls data/verification/page-5*.json | head; grep -l '\"Per 3\"\\|Per 3' data/extracted/batch/*.json | head"
}
```


### [2026-10-16T05:13:17.484Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 34

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe-private/data/verifi

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

Permissions Size User   Date Modified Name
.rw-r--r--   69k sfmqrb 14 Oct 22:14  data/verification/page-50.json
.rw-r--r--   99k sfmqrb 14 Oct 22:14  data/verification/page-51.json
.rw-r--r--   50k sfmqrb 14 Oct 22:14  data/verification/page-52.json
.rw-r--r--   53k sfmqrb 14 Oct 22:14  data/verification/page-53.json
.rw-r--r--   84k sfmqrb 14 Oct 22:14  data/verification/page-54.json
.rw-r--r--   60k sfmqrb 14 Oct 22:14  data/verification/page-55.json
.rw-r--r--   84k sfmqrb 14 Oct 22:14  data/verification/page-56.json
.rw-r--r--   58k sfmqrb 14 Oct 22:14  data/verification/page-57.json
.rw-r--r--   79k sfmqrb 14 Oct 22:14  data/verification/page-58.json
data/extracted/batch/page-139.json
data/extracted/batch/page-156.json
data/extracted/batch/page-215.json
data/extracted/batch/page-194.json
data/extracted/batch/page-209.json
data/extracted/batch/page-214.json
data/extracted/batch/page-202.json
data/extracted/batch/page-210.json
data/extracted/batch/page-244.json
data/extracted/batch/page-298.json
```


## [2026-10-16T05:13:21.076Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','BQT','MON','FRS']:\n  e=d[k]; print(k, {x:e.get(x) for x in ['local_file','page_offset','lookup_hint','scans']});print()\n\""
}
```


### [2026-10-16T05:13:21.548Z] TOOL RESULT

```
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", 'scans': None}

KLN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", 'scans': None}

HRN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", 'scans': None}

BQT {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", 'scans': [{'volume': '3', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]}

MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", 'scans': None}

FRS {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS.txt'], 'page_offset': 'different edition — no mapping', 'lookup_hint': 'Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.', 'scans': None}
```


## [2026-10-16T05:13:25.072Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -A12 'lemma: upo' POK_full.txt | head -60; echo ===; grep -n -B2 -A20 'lemma: (s)kabh\\|lemma: skabh\\|lemma: .*kabh' POK_full.txt | grep -n -i 'Page\\|lemma\\|upa\\|skamb\\|Meaning' | head"
}
```


### [2026-10-16T05:13:25.473Z] TOOL RESULT

```
Exit code 1
88197:Root / lemma: upo, up, eup, (e)up-s- 
88198-
88199-Meaning: under, from under, etc.. 
88200-
88201-Note: from the meaning "from under hinauf die meaning "hinauf, about', die partly here, 
88202-
88203-esp. but in related *uper(i){see d.), as well as in the group u4JnA6(; etc. ausgepragt is; Indo 
88204-
88205-Germanic upo\s proverb (e.g. Old Indie upa-i-, gr. un-£ipi, Latin sub-ed) and preposition by 
88206-
88207-variant case. 
88208-
88209-Material: /. Old Indie ^pa proverb and preposition " toward - to (Akk.); an, by, to (Lok.); in 
(eval):1: == not found
```


## [2026-10-16T05:13:29.790Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 88209,88330p POK_full.txt | grep -v '^$' | head -90"
}
```


### [2026-10-16T05:13:30.194Z] TOOL RESULT

```
Material: /. Old Indie ^pa proverb and preposition " toward - to (Akk.); an, by, to (Lok.); in 
Laufe from, gemaft, with in sense the accompaniment (Instr.)', Avestan upa, ap. upa 
proverb and preposition " toward - to, in, auf (Akk.); by, in (Lok.)'; 
gr. uno proverb and preposition "under an etwas heran, under etwas (Akk.); under an, 
under ("dative ', actually Lok. and partly perhaps Instr.); under; of Urheber beim Passiv 
(Gen. of Bereiehes); from under away, under - hervor (Abl.)'; 
Latin 5^i6'(s-from *[e]ks-, compare gr. s^unspGEv; -it* from -pas in ab= gr. airo), proverb 
and preposition "under an etwas heran, under etwas' (Akk.; also temporal, e.g. sub 
noctem); under an, under("Abl.', actually Lok.), as Oscan aun psSiKiai (partly perhaps 
Instr., as Umbrian su maronato' sub *maronatu'), besides subs- (as abs) in sustineo and 
in susque deque /fe/'d "aequo animo fero' (Gell.), compare also under die group from uijji. 
Umbrian sub-, su-, Oscan aun; Old Irish /opreverb and preposition "under' (Akk., "Dat.' = 
Lok. or partly perhaps Instr.), acymr. guo-, gu-, gua-, ncymr. go-, gwa-, corn, go-, gu-, bret. 
gou- proverb and in compound gall, vo- ( Voretus), ve- (gr. -Celtic-Latin parave-redus 
"Extrapostpferd', from which Modern High German Pferd); 
maybe alb. {*subeo, subito) shpejt 'sudden, fast'. 
perhaps cymr. gorau 'besi' from *uper-esu{= gr. UTT£p-£u "very good', L.-P. S. 186) or 
from * uper-gousom {compare S. 399) after Binchy J. C. stem 1, 148 ff.; das ofrom Celtic 
I/O-; with Old Indie upa-sthana-m ^Bed'\enung', upa-sti-, upa-stf-rc\. " subordinate, servant' 
compare Middle Irish /bss "servant' {*upo-sto-), cymr. bret. gwas, corn, guas ds., gall. PN 
Vasso-nxeic, Middle Latin vassus, vassallus, samtlich zur root sta-S. 1005, 1008, as also 
Old Irish /fc»//7 "replacement, equivalent' {fo+ ta) but Middle Irish fothae' foundation, origin, 
source, beginning; an ancestor ' from fo + suide (see 885); 
Gothic uf{ub-uh) prefix "auf, under', preposition "under' (Akk., "Dat.' = Lok. and partly 
perhaps Instr.), Old High German oba. Middle High German obe, ob^M, about' {*up6), but 
Old Icelandic orabout, an, in'. Old English ufe-{*upo). Old High German uf{ufan) "auf (to 
Old High German ^compare under Old Church Slavic vysoki,); besides with -pp- Old 
Saxon uppa, up. Old English uppe, up. Old Icelandic upp'aui, aufwarts' and (with one only 
in Old Irish ds, uas, cymr. ^c/7wiederkehrenden lengthened grade) Gothic /wpa ' droben' , 
/up'aiter, above'; Hittite up-z/'gebt auf (from the sun). 
maybe alb. {*upa) hyp, aor. hypa^ c\\xx\b, mount (a horse)' 
2. supplementary: Old Indie upama-'tbe oberste, hochste, nachste', Avestan upoma- 
ds.. Old English ufemest {and yfemest) "the hochste, oberste'; 
Latin summus {*supmos) "the hochste' = Umbrian 50/770 "summum', compare also gr. 
unaTO(; "the hochste, first'. - Gr. unTiO(; "zuriJckgelehnt, backwards, to the rear' (? after 
Sittig from 5i/p-//- "sleeping' - above S. 1048 -, compare Kretschmer Gl. 22, 247), Latin 
s^p/77^s"auf dem back lying, backwards bent, sparse, reduced ansteigend'. Old Latin 
suppus (short form to supTnu^) ds., suppo, -are "supTnare, auf den back lay, place, 
backwards, to the rear hold out, stretch forth ', Umbrian 5O/0a/77 "suppam'. 
alb. shume {* summus) [adv] " considerably, greatly, very ' 
upelo-s\n Gothic ubils. Old English yfel. Old High German ubiTevW, Middle Irish fel 
"evil, bad'. 
upes-\'c\ Gothic ubizwai. "Vorhalle', Old Icelandic upst, ups/vn. "Vorhalle a Kirche', Old 
English efes, y/fes'Dachtraufe', Old High German obosa, obasa, c»,6'/S5 'Vorhalle'; 
^rps- (compare above Latin subs-, susque) in gr. uiyi Adv. "high' (seems ubrigens as utt- 
a\ ein Lok. PI. to sein, as Old Irish os, ^55 from *oup-su), whereof uijjiT£po(;, ui^jiajv 
"higher', ui^JiaToq "the hochste'; uijjou, uijJoGi, -oas ds., uijjoGev "from hoch herab', to uy^oc, 
"height, acme, apex ', uijjr|A6(; "high'; with lengthened grade Celtic o^ (probably Indo 
Germanic eu, compare Gothic iupa): Old Irish os, Jas "above, about' {*oup-su) = cymr. 
ucb, corn, ugh, bret. uc'b6s., wherefore Adj. Old Irish uasa/'\r\\g\r\', cymr. ucbe/ 
(compounds uch. Sup. uchafj corn, huhe/, bret. uc'he/'h\g}r\', gall. Ou^sAAov, -a, Uxello- 
dunum {*oupselo-), further Old Irish J5//"Ubermut' {*oupsla) and Old Irish ochtar, uachtar 
"das Obere', cymr. ^Z/?/' "dreadful, erstaunlich' {*oup-tro-, maybe from *oupstro-, or after 
dem relationship *eks: "e/rZ/'o-dafur eingetreten); here das Old Irish proverb uss-, oss- 
{*uxs< *ups) e.g. in Old Irish osnad^sxgh' (see 38), cymr. uch-enaid, bret. huanad6s., 
where "^^^ through *c»i/x5 replaced worden is; original *uxs3iU6 l/o'-s-(see above under 
ud-) are phonetically otherwise not to distinguish, discern; compare Thurneysen Gr. 5, 
526; keltiber. PN Vxama, gall. Vxisama{: cymr. i/c/7arhochst'); 
proto Slavic. *J/7sa-"high' placed in Old Church Slavic vysokhetc. "high'. 
References: WP. I 192 f., WH. II 612 ff., Schwyzer Gr. Gr. 2, 522 ff., Trautmann 335, 
Vasmer 1 , 242, Mayrhofer 1 , 1 05 f. 
Page(s): 1106-1107 
Root / lemma: uad'^- 
Meaning: pledge 
Material: Latin vas, vad/s 'Burge', vad/mdn/um 'Burgschafi', praes. -d/'s, o\der prae-v/des 
"BiJrge'; Gothic wad/'n. " pledge, Handgeld' {wadjabokos ^PlandbneV, gawadjdn^ betroth 
'), Old Icelandic i/edn. " pledge, anvertrautes blessing'. Old Frisian M/eo'"pact, covenant, 
promise, BiJrgschaft, certainty ', Old English wedd^ pledge, pact, covenant'. Old Saxon 
weddi^ pledge ', Old High German wetti, M/e//"Pfandvertrag, Rechtsverbindlichkeit, pledge 
', Middle High German also "Einsatz bei a Wette, Schadenersatz', Modern High German 
Wette; Old Icelandic vedja "aufs Spiel place, wetten, under Hinterlegung a BiJrgschaft 
Berufung einlegen'. Old English wedd/an'pact, covenant make, promise, verheiraten' 
{weres weddian^s\c\\ einem Manne betroth ', engl. wed ^ marry'). Middle High German 
wetten^ pledge give, Strafgeld entrichten, wetten'. Modern High German wetten. 
Lithuanian vadas^ pledge, BiJrge', vaduot/ {La\.\/\an vaduot) "somewliat Verpfandetes 
einlosen', uz-vaduoti^iox \ermv\6ev\ eintreten'. 
References: WP. I 216 f., WH. II 735 f. 
Page(s): 1 1 09 
Root / lemma: uai 
Meaning: woe! 
Material: Avestan vayoi, avoi, 5Kdy5"wehe'! {voya- 'Wehruf): Armenian Kay'Wehe, 
misfortune' (i/- instead o\ g- from Indo Germanic ^-through nebenherlaufende neologism); 
similarly gr. 66 (as Latin vah!) and from alexandrinischertime ou6, ou6, ouai, ngr. p6i 
(Neuschopfungen); alb. Kay "affliction, lament'; 
Latin vae\ Middle Irish fae, cymr. ^n/ae'weh!'; with one perhaps with Latvian vaTdi 
connected with o'(/7)-suffix presumably Middle Irish faed, /5/d/"scream, sound, tone', cymr. 
gwaedd^c\arc\or, eiulatus';
```


## [2026-10-16T05:13:35.472Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^upo\\|upo\\.\\|^upo-\\|upo ' AHD_watkins1985.txt | head; "
}
```


### [2026-10-16T05:13:35.794Z] TOOL RESULT

```
1097:upo
1106:upo. Under, up from under, over. 1. Germanic *upp-, up, in: a. Old English up, uppe, up: uP; b. Old English up-, upp-, up=: UP-; C. Middle Dutch op, up: UPROAR. 2. Ger- manic *upanaz, “put or set up,” open, in Old English open, open: OPEN. 3. Germanic *ufana, “on, above,” in Old English bifan, above, over: ABOVE. 4. Possibly suffixed form *up-t- in Germanic *ufta, frequently, in Old English oft, oft: OFT, OFTEN. 5. Extended form *upes- in Germanic *ubasw6, *ubizwé6, vestibule, porch, eaves (< “that which is above or in front’), in: a. Old English efes,
1108:eaves: EAVES; b. Germanic *obisdrup-, dripping water from the eaves (*drup-, to drip, from *dhrub-; see dhreu-), in Old English yfesdrype, yfes drypx, water from the eaves: EAVESDROP. 6. Variant form *(s)up- in: a. Latin sub, under: SOUTANE, SUB-; b. Latin supinus, lying on the back (< “thrown backward or under’): SUPINE!, SUPINE?; Cc. suffixed form *sup-ter in Latin subter, secretly: SUBTERFUGE; d. Latin supplex, “with legs folded under one” (-plex, -fold; see plek-): SUPPLE. 7. Basic form *upo in Greek hupo, under: HYPO-. 8. Suf- fixed variant form *ups-o- in Greek hupsos, height, top: HYPSO-. 9. Basic form *upo- in Celtic *vo-, under, in Latin verédus, post horse (see reidh-). 10. Compound *upo-st-o- probably in Celtic *wasso-, “one who stands under,” servant, young man (*sto-, standing; see sta-), in Medieval Latin vassus, vassal: VALET, (VARLET), VASSAL. 11. Sanskrit wpa, near to, under (in upanisad, Upani- shad): OPAL, UPANISHAD. [Pok. upo 1106.]
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1440:EAVES upo EAVESDROP upo EBB apo-
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
2277:SOP seue-2 SOPOR swep-1 SOPORIFIC swep-1 SOPRANINO uper SOPRANO uper SORCERER ser-3 SORDID swordo- SORDINO swer-2 SORE sai- SORITES teue- SORORAL swesor- SORORITY swesor- SORREL! siiro- SORREL? saus- SORROW swergh- SORRY Sai- SORT ser-3 SORTILEGE leg-1, ser-3 SORUS teue- SOTERIOLOGY teue- SOUBRETTE uper SOUFFLE bhlé-2 SOUGH (s)wagh- SOUND! swen- SOUND2 swento- SOUND3 swem- SOUND4 swem- SOUP seue-2 sOUR siiro- SOURDINE swer-2 SOUSE sal-1 SOUTANE upo SOUTH sawel- SOUTHERN sawel- SOUVENIR gWa- SOVEREIGN uper SOVIET sem-! sow! sé-1
2323:sTuD2 sta- STUDENT (s)teu- sTUDY (s)teu- STULTIFY _ stel- sTUM stam- STUMBLE stam- STUMP stebh- STUN (s)tena- STUPA steu(@)- STUPE steu(9)- STUPEFY (s)teu- STUPENDOUS (s)teu- STUPID (s)teu- STURDY trozdo- STUTTER (s)teu- stTy2  steigh- STYLITE sta- STYLOBATE gWa-, sta- STYPTIC steu(@)- Styx (s)teu- SUASION swad- SUAVE swad- SUB- upo SUBALTERN al-1 SUBAUDITION au-5 SUBDUCTION deuk- SUBDUE deuk- SUBITO ei-! SUBJACENT yé- SUBJECT yé- SUBJOIN yeug- SUBJUGATE yeug- SUBLUNARY leuk- SUBMERGE mezg-! SUBMIT (s)meit(9)- SUBORDINATE ar- SUBORN ar- SUBPOENA kwei-1 SUBREPTION rép-1 SUBROGATE reg-1 SUBSCRIBE skribh- SUBSEQUENT sekw-1 SUBSIDE sed-1 SUBSIDY sed-1 sUBSIST sta- SUBSTANCE sta- SUBSTITUTE sta- SUBSTRATUM ster-2 SUBSTRUCTION | ster-2 SUBSUME em- SUBTEND ten- SUBTERFUGE bheug-', upo SUBTERRANEAN ters- SUBTLE teks- SUBTRACT tragh- SUBULATE syU- SUBVENTION gWa- SUBVERT wer-3 SUCCEED ked- succincT kenk-1 succor kers-2 succuBUS keu-2 SUCCULENT seud-2 SUCCUMB keu-2 SUCCUSSION kwét- SUCH swo-
2327:suP2 seue-2 SUPER- uper SUPERABLE uper SUPERANNUATED at- SUPERB uper SUPERCILIOUS kel-2 SUPERCILIUM kel-2 SUPEREROGATE reg-' SUPERFETATE dh@(i)- SUPERFLUOUS bhieu- SUPERIOR uper SUPERJACENT yé- SUPERLATIVE tele- SUPERNAL uper SUPERNATANT sna- SUPERNUMERARY _nem- SUPERSCRIBE skribh- SUPERSEDE sed-1 SUPERSTITION sta- SUPERVENE gWa- SUPERVISE weid- SUPINE! upo SUPINE? upo SUPPLANT plat- SUPPLE plek-, upo SUPPLICATE plek- SUPPLY pele-1 SUPPORT per-2 SUPPOSE apo- SUPPRESS per-5 SUPPURATE pu-2 SUPRA- uper SUPRALAPSARIAN leb-1 SUPREME uper SUPREMO uper SUR- uper SURCULOSE swer-3 SURD swer-2
2437:UNITY oi-no- UNIVERSE 0i-no-, wer-3 UNIVOCAL wekw- UNKEMPT gembh- UNTIL ant- UNWITTING weid- UP upo UPANISHAD sed-1, upo UPBRAID bherek- UPROAR kere-, upO UPSILON bhes-! URCHIN ghers- UREDO eus- URETER wers-2 URETHRA wers-2 URETIC wers-2 URGE wreg- -URGY werg- -URIA wers-2 URINE wér- URO-! wers-2 URO-2 ors- URONIC wers-2 -UROUS ors- URSINE rtko-
```


## [2026-10-16T05:13:43.892Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o 'EVIL [a-z-]*\\|SUBLIME [a-z-]*\\|SUBMARINE [a-z-]*\\|OPEN [a-z-]*' AHD_watkins1985.txt | sort -u; grep -n -i 'Lex 0\\|^sub-, \\|^sub,\\|^sub$' KLN_1966.txt | head; grep -n '^sub-\\|^sub,' KLN_1966.txt KLN_1971.txt | head"
}
```


### [2026-10-16T05:13:44.210Z] TOOL RESULT

```
EVIL g
EVIL wep-
OPEN upo
KLN_1971.txt:190824:sub-, ‘under’, and emere , ‘to take’. See assume 
KLN_1971.txt:226125:sub- and L. talus , ‘ankle bone’. See talus, ‘ankle’. 
KLN_1971.txt:226267:sub- and L. umbra, ‘shadow, shade’. See umbra 
KLN_1971.txt:235087:sub, n. ( colloq .) — Short for subaltern, submarine, 
KLN_1971.txt:235089:sub, prep., under. — L. See sub-, 
KLN_1971.txt:235090:sub-, pref. of Latin origin meaning ‘under’. — 
KLN_1971.txt:235126:sub- and acute. 
KLN_1971.txt:235158:sub- and aquatic. 
KLN_1971.txt:235214:sub- and dolus , ‘guile, deceipt, deception’. See 
KLN_1971.txt:235926:sub- and cingo, cingere, ‘to gird’. See cincture
```


## [2026-10-16T05:13:50.127Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 235089,235110p KLN_1971.txt; grep -n '^sub-, \\|^sub, prep' KLN_1966.txt | head; grep -n '^sublime\\|^subject, \\|^submarine\\|^evil, \\|^open, \\|^up, ' KLN_1971.txt | head -20"
}
```


### [2026-10-16T05:13:50.554Z] TOOL RESULT

```
sub, prep., under. — L. See sub-, 
sub-, pref. of Latin origin meaning ‘under’. — 
Sub - regularly becomes sue- before c, suf- before 
/, sug- before g, and sup- before p. It often be- 
comes sum- before m and sur- before r. It is 
simplified to su- before sp. Before c, p and t it 
sometimes has the form sus- (for subs-, an ear- 
lier form of sub-). — L. sub-, etc., fr. sub (for 
*sup), ‘under, below, beneath’, rel. to Oscan 
ctutc, Umbr. su , ‘under’, and cogn. with OI. upa , 
‘near, under, up to, on’, Gk. bn6, ‘under, 
below’, Goth, uf, ‘under’, OIr. fo , W. guo -, 
Gaul, vo-, ve-, ‘under’, Goth, iup, ON., OE. upp, 
‘up, upward’, Hitt, up-zi , ‘rises’ (said of the 
sun). All these words derive fr. I.-E. base *upo -, 
‘from below’, whence arose the meanings ‘turn- 
ing upward, upward; up, over, beyond’. See up 
and cp. supine, sum, summary, summit, soutane 
and the first element in surge and in Upanlshad; 
cp. also hypo-. Fr. I.-E. base *upo- developed 
the comparative *uper- , *uperi- , ‘over, above, 
beyond’, whence OI. updri , ‘over, above, be- 
14145:up, collect’, fr. ava (see ana-) and Xeyetv, ‘to 
19101:up, parch*, &>, ‘dryness; dirt, mold’, 
20523:up, mount’, fr. ad- and scandere, ‘to climb*. See 
33196:up, agitate’. See brassage and -ery. 
50722:up, raise’, tolerate , ‘to bear, support’. See toler- 
52596:up, complete’. See complement. 
55012:up, make, fabricate, join together’, fr. con- and 
79940:up, raise’, tolerare , ‘to bear, support’. See toler- 
87113:evil, adj. — ME. evil , evel, ivel , uvel, fr. OE. yfel, 
117595:submarines. — Compounded of hydro- and Gk. 
121799:up, confinement’, fr. inclusus, pp. of includere. 
128799:subject, superjacent, synesis, traghetto, trajectory. 
135384:open, make wide, slacken, relax, relieve’, fr. 
164954:up, wall up; to bar, render impassable’, lit. ‘to 
167476:open, adj. — ME., fr, OE., rel. to OS. opan, ON. 
167485:open, tr. v., to make open; intr. v., to become 
208544:subject, which is repeated at least twice after the 
220649:up, shine’, OI. chayd , Gk. axia, ‘shade’. See 
234532:up, support’, OHG. stuzzen (in untarstuzzen ), 
235268:subject, adj. — ME. suget, subget, fr. OF. suget,
```


## [2026-10-16T05:13:53.048Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 87113,87125p KLN_1971.txt; echo ==; sed -n 167476,167486p KLN_1971.txt; echo ==; sed -n 235268,235280p KLN_1971.txt; grep -n '^sublime, ' KLN_1971.txt; grep -n '^submarine, ' KLN_1971.txt"
}
```


### [2026-10-16T05:13:53.421Z] TOOL RESULT

```
evil, adj. — ME. evil , evel, ivel , uvel, fr. OE. yfel, 
yfil, rel. to OS. u'Bil, OFris., MDu. evel, Du. 
euvel, OHG. ubil, MHG., G. iibel, Goth, ubils, 
fevil*. These words are prob. rel. to up, above, 
over (qq.v.) Accordingly, the orig. meaning of 
OE. yfel, etc., seems to have been ‘going up- 
ward’, hence ‘going beyond, transgressing’. 
Derivatives: evil, n. and adv., evil-ly, adv. 
evil-starred, adj. — Coined by the English poet 
Alfred Tennyson (1809-92) fr. evil, star and adj. 
suff. -ed. Cp. ill-starred. 

evince, tr. v., t) to show; 2) to exhibit. — L. evin- 
(eval):1: = not found
```


## [2026-10-16T05:13:55.660Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 167476,167490p KLN_1971.txt; echo ==; sed -n 235268,235280p KLN_1971.txt; grep -n '^sublime\\|^submarine' KLN_1971.txt | head -4"
}
```


### [2026-10-16T05:13:55.988Z] TOOL RESULT

```
Exit code 1
open, adj. — ME., fr, OE., rel. to OS. opan, ON. 
opinn, opin, Swed. bppen, Dan. aaben, OFris. 
epen, Du. open, OHG. offan , MHG., G. offen, 
‘open’, and prob. also to E. up (q.v.) For sense 
development cp. G. aufmachen , ‘to open’, lit. ‘to 
make up’. 

Derivatives: open , n., the open space, the open 
air, open-ly , adv., open-ness , n. 
open, tr. v., to make open; intr. v., to become 
open ; Jo begin. — ME. openen , fr. OE. openian , 
fr. open, ‘open’. Cp. OS. opanon , oponon, ON. 
opna, MDu., Du. openen, OHG. offanon , MHG. 
ojfenen, G. offnen , ‘to open’, and see open, adj. 
open-eyed, adj. — First used by Shakespeare, 
(eval):1: = not found
```


## [2026-10-16T05:14:02.554Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -A6 '^subject, adj\\|^sublime, \\|^submarine, ' KLN_1971.txt | head -40"
}
```


## [2026-10-16T05:14:03.378Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==55' HRN.txt | head -80"
}
```


### [2026-10-16T05:14:03.793Z] TOOL RESULT

```
235268:subject, adj. — ME. suget, subget, fr. OF. suget, 
235269-subject (F. sujet), fr. L. subjectus, pp. of subicere , 
235270-less correctly subjicere , ‘to subject, include, 
235271-comprise’, lit. ‘to throw under’, fr. sub- and 
235272-jacere (pp. jactus), ‘to throw’. See jet, ‘to spirt 
235273-forth’, and cp. words there referred to. For the 
235274-change of Latin a (in jactus) to e (in sub-jectus) 
--
235285:subject, adj., and cp. object. 
235286-
235287-Derivative: subject-less , adj. 
235288-subject, n., person owing allegiance to a ruler. — 
235289-L. subjectus , pp. of subicere. See prec. word. 
235290-
235291-
--
235360:sublime, adj., 1) noble; 2) lofty. — F., fr. L. su- 
235361-blimis, ‘high, lofty, exalted’, back formation fr. 
235362-sub limen , hence lit, meaning ‘(coming) up to 
235363-below the lintel’, fr. sub (see sub-) and limen, 
235364-‘lintel’. See limen. 
235365-
235366-Derivatives: sublime, n., sublime-ly , adv., sub- 
--
235369:sublime, tr. and intr. v. — ME. sublimen, fr. MF. 
235370-(= F.) sublimer, fr. L. sublimdre. See sublimate, v. 
235371-Sublime Porte, former title of the Ottoman 
235372-Government. — F. la Sublime Porte , lit. ‘the High 
235373-Gate’, loan translation of Arab. Bab 'Alt , title 
235374-of the Ottoman Court in Constantinople. Cp. 
235375-Porte. 
--
235393:submarine, adj., living or occurring below the 
235394-surface of the sea. — Formed fr. sub- and 
235395-marine, adj. 
235396-
235397-Derivatives : submarine, n., submarin-er , n. 
235398-submerge, tr. v., to place under water, cover with 
235399-water; ijitr. v., to plunge into water; to be sub-
```


### [2026-10-16T05:14:04.220Z] TOOL RESULT

```
- 33 -
haben sollte (vergl. aber unter np. herhud, No. 1115,
nebst Anmerkung dazu), so wäre Nöldeke geneigt
(mündliche Mitteilung), np. ermän 'Gast' hieran
anzuschliessen ; also ursprünglich ein *am Feuer
Sitzender, Teilnehmender. Die Ableitung von ar.
aryaman- wäre dann aufzugeben.
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
148. &i-, Verbalpraefix.
päz. M- (phlv. NHD).
Wie es scheint, ursprünglich identisch mit he- 'ohne,
ausser (No. 247).
Fr. Müller construirt WZKM. 5, 65 als Grund-
form ein ap. baiy- = (aw.) hd^it und setzt ap. ha
(alles ohne Sterne, als wenn die Formen wirklich
belegbar seien) gleich aw. ha, bäd, ai. hat 'fürwahr.
^44. be, bed (vor Vokalen), Praeposition, 'zu, bei, mit, an,
V ; auf.
ap. patiy bezw. upd; aw. paiti bezw. upa; phlv.
pat[as, pat- bezw. päz. pa (JIS); ai. prdti bezw. üpa.
vergl. kurd. pe, he; af/. paU pa-; oss. fa- fä- (266);
bei. pa, n. pa (274) ; PD. pet-, pa- etc.
In der Form he sind die beiden Praepositionen tipa
und (irregulär) pati zusammengefallen, ein Vorgang,
der scharf beachtet werden muss. Über pati- als
U o r n , Orundriss d. neup. Etymologie. 3
```


## [2026-10-16T05:14:24.913Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in 41 65 71 72 73; do echo \"=== HRN p$p\"; awk -v n=$((p+22)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | grep -n -i -B1 -A7 'padid\\|pad[iî]d\\|pasand\\|bäva\\|bävar\\|bavar\\|bedrüd\\|drüd\\|pegäh\\|pagäh\\|penhän\\|pinhän\\|upa' | head -50; done"
}
```


### [2026-10-16T05:14:25.250Z] TOOL RESULT

```
=== HRN p41
23-178**'* bäver 'Glaube'.
24:Zu [/^var- 'glauben' mit upä (d. i. upa+ä)^),
25-179. baylsten müssen, nötig sein' (Imperson.), Praes.
26-^\fy^ bäg-ed; vergl. ender wm 'Bedürfniss'^).
27-Kä§. apä (mit folgendem Futurum), vergl. ßmpeyd
28-etc. (S. 115).
29-\i
30-') Nie selbständig. Ghrest. Schahn. 10 ist hä an suwärän zu
31-lesen. Auf diesen Yullers^ sehen auch von Darmesteter wieder-
=== HRN p65
=== HRN p71
=== HRN p72
13-sincdti ist unklar, aber doch wohl vorhanden.
14:324. pegäh *Frühlicht, früher Morgen .
15:aw. upa ~r (Jäh (s. No. 889).
16-325. pul^) 'Brücke.
17-gel. purd.
18-aw. peretU' 'Brücke', pesu- 'Furt' (d. i. peretü-, peäu-^
19-Bartholomae, Ar. Forsch. II, 35 folgg.); phlv.
20-puhrj puhl ^Brücke, Furt'.
21-kurd. per^ pir, pird, purd, pel (H.-Sch.); af/. LW.
22-pul.
=== HRN p73
22-y. 45, 5, 6)^); Nöldeke, Kärnämak 49, Note 2.
23:332. penhän, pinhän Verborgen'.
24-phlv. pa (pO) nihan (s. No. 1058) ; Nöldeke, Kärnämak
25-67, Note 2.
26-Np. pendm bedeutet ebenfalls Verborgen, bedeckt';
27:es wird von den Wörterbüchern als aus penhän con-
28-trahirt angesehen (zu m für n vergl. bam, bau 'Dach') ^) ;
29-mit parsisch penäm (jpenöm)^ aw. paiti.däna-, phlv.
30-padäm, wird np. penäm Verborgen' nichts zu thun
31-*) loh orgreife diese Gelegenheit, um den BB. XVII, 261 Note 2
32-begangenen Irrtum zu berichtigen, dass ich auch Darmesteter die
33-unmögliche Erklärung des Wortes aus sem. p^ + dästen zugeschrieben
34-habe. Sie bleibt vielmehr Fr. Müller allein reservirt.
```


## [2026-10-16T05:14:33.567Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in 64 65 66 70 71; do echo \"=== HRN p$p\"; awk -v n=$((p+22)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | grep -n -i -A6 'pad.d\\|pas.nd\\|drüd\\|drud\\|^ *[0-9]\\{3\\}\\. p' | head -40; done"
}
```


### [2026-10-16T05:14:34.053Z] TOOL RESULT

```
=== HRN p64
5:283. päyi;^ 'Herbst*.
6-phlv. pätej^ päz. pädez 'Herbst'.
7-oss. fäzzäg 'Herbst' (269) (?); sar. pij 'Herbst'.
8-Fr. Müller nimmt (WZKM. 5, 261) als Grund-
9-form ein ap. '^patidaiza-y aw. ^paitidaeza- 'Anhäufung,
10-Sammlung, Emdte' an.
11:284. petyäre 'Unglück' etc. (Vis und Rämin, Seite 81,
12-Vers 5 v. u.).
13-aw. paitt/ara- 'Gegenschöpfung'; phlv. patyardk,
14-püyärak (Men., K 43).
15:285. pulten 'kochen, Praes. pez-em^ pezamden,
16-g. pa/tmün, P<^yß (= np. ptixt^) ; Käs. patSn, pa^te-
17-man; mäz. pa/ta,
18-aw. skr. [/^pac- 'kochen' ; phlv. pu^tan^ pazem, pazBt
19-(PPGl.), pazämlnUan (Bund., Men.).
20-kurd. patin 'kochen', bepiz; afy. pa/avul; oss. d. ficun^
21-t.ßcin (291) (?) ; bei. pacag, n. pasay (276) ; wa;t'- pöcam,
--
24:286. pider (peder) 'Vater'.
25-Käs. pei (aus ped),
26-ap. pitar- 'Vater'; aw. pitar-; phlv. pit, pitar (in
27-"inlON), P(i)tar\böxt N. pr. (Kanheri-Inschr.j; ai.
28-pitar- ; arm. hair 'Vater* (H. No. 155).
29-kurd. pier^) 'Vater'; af;'. plar\ oss. d. fidä, t. fid
30-(283) ; bei. pit n. pis, pid- (296) ; siyn. ped, sar. pit.
=== HRN p65
5:287. pidräm 'schön, fröhlich' (Sahn. III, 1803, V. 372).
6-aw. *2)aiti.raman' ; vergl. np. räm (No. (504).
7:288. pedrad 'Heil, Lebewohl*.
8-phlv. pa i]^t) + drüt (Nöldeke, Kam. 65).
9-Vergl. np. durüd (No. 555).
10:289. pedJd 'sichtbar.
11-phlv. pa du {^\y\rr^^\ ps), Nöldeke, Karn. 40; also
12-aw. Sipa.dHi-,
13:290. peölruften 'empfangen, annehmen', jüd.-pers. J nenne,
14-Praes. peöJr-em, peSlr,
15-ap. *patit/ -f- i/^grufj-; phlv. patgriffan bezw.
16-«
17-patiraftan (Bund., sonst stets inJltJ^pD), päz. padlraftan
18-'empfangen, annehmen .
19-Vergl. np. giriften (No. 909).
20:291. peöfre entgegen*.
21-phlv. patlrak *) (mit verkürztem k , nicht patirag),
22-übersetzt aw. paiti.
23-Zur vorhergehenden Nummer.
24:292. per-, Praefix.
25-1) ap. /)am- 'weg {paräbara, parägmata); aw. para
26-Vor, weg* ; phlv. par-, ai. pdrä- 'weg, fort*.
27-In dieser Bedeutung auch in der' Form pera- vor-
28-kommend.
29-2) ap. pariy 'um , herum' ; aw. pairi ; phlv. par- ;
30-ai. pari.
31:293. perr Teder, Flügel*; pemden^ penden^ perend 'Vogel'^),
32-perre.
33-aw. parena- 'Feder, Flügel'; phlv. par bezw. parr^
34-par(r)Uan (Bund.), par(r)is (Nöldeke, ZDMG. 46,
35-143); ai. parnd- 'Feder, Flügel*; lit. spafnas 'Flügel*.
36-kurd. per^ zaza pel 'F]ügel\ firin 'fliegen*; wa/. parr.
37-^) Auch vd. 5 (28) steht patlrak^ nicht patir, gegen Spiegel,
=== HRN p66
18:295. perfuf enden zerstreuen; erschrecken, pergenden,
19-phlv. pargantan (Bund.).
20-ap. "^para -\~ y/kan- (?). Der Bedeutungswechsel ist
21-allerdings sehr auffällig. Vergl. efgenden (No. 103).
22:296. pertew 'Glanz*.
23-para j- ^fap-^ vergl. np. fäßen (No. 372).
24:297. perdayten 'ausführen, ausleeren; streben, sich be-
25-mühen* ; Praes. ,perdazem.
26-phlv. parda/tan (AV.).
27-aw. *para + l^tac-; Bedeutungswechsel wie bei
28-end (Ixten (No. 117). Die np. Bedeutung 'ausleeren'
29-lässt sich aus 'weglaufen lassen' erklären.
30-von Stackeiberg (briefl. Mitteilung) vergleicht
--
34:298. perest 'Verehrer , verehrend*, perestTde7i , perestür^
35-perestis.
=== HRN p70
16:315. pes 'hinter, nachher, pesin 'letzter.
17-Käs. peCj pdc]es, pes.
18-ap. pasa, 'hinter', pasäva 'nachher ; aw. pasda 'nach',
19-paskät nachher, hinter , pasne 'hinter' ; phlv. paSj pasTn
20-'letzter ; ai. pagdd *hinter, nachher , pagcdt Von hinten,
21-hernach*.
22-kurd. püstve, pfisl; af/. LW. pas; oss. d. fastäge, t.
--
25:316. pest 'niedrig, nnoilN (Is. 2, 9; 11, 17).
26-ai. vergl. üpastiä, upastis 'Untergebener .
27-Bartholomae (briefliche Mitteilung).
28-LW. wa/. past, siyn. pist,
29:317. pistän 'Brust (der Frau)'.
30-a.w./stana' *Brust'; phlv. p(i)stan (vd. 9 (71)), pistän
31-(vd. 15 (26) 61.); ai. stdna-; arm. stin (H. No. 259).
32-LW. af/. pistän.
33-Vergl. Bartholomae, Indog. Forsch. I, 187 Anm. 2.
34:318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
35-1517 Vers 358 2), 1523 Vers 473).
36-*) So lese ich statt nvedlnltan.
37-*) An den beiden ersten SteUen vielleicht für puser zu emendireD,
38-doch kann bei puser wie bei pider die Izäfe fehlen, vergl. Landauer
39-zu S. 1517 Note 4.
=== HRN p71
9:319. pesend zufrieden, angenehm', pesendlden.
10-ap. *M/)rt -T- K^arf-; aw. [^sad- (Geldner 1 [/sad-,
11-KZ. 27, 242), vergl. sendah-, vahmö.sendah- (?)2) (auch
12-l/"sac/- 'sitzen' kommt mit inligirtem Nasal vor, vergl.
13-ai. ilsandt- 'Sessel*, ksl. sedq 'ich sitze', apr. sindäts),
14-Spiegel, Commentar II, 311 (nur fälschlich mit
15-Praep. paiti; die Aussprache pisend findet sich nur
--
17:320. pist 'Mehr.
18-aw. pistra-; ai. l/'pes- 'zerreiben, zerstampfen {pistä-^
19-skr. pistaka-),
20-wa/. pös^; siyn. pist, sar. pa/t geröstetes Korn , zu
21-Mehl zerrieben'.
22-321. 2>ie«f 'Rücken'.
23-Kä§. mäz. past.
--
27:322. pusek, pösek *Katze' ('Dialekt von Transoxanien' BQ.)^).
28-gel. plöa (?).
29-In Indien spricht man piser ; die nämUche Aussprache soll auch
30-})yser bei Fleischer, Neup. Gramm. 2, S. 7 ausdrücken. Piser ist in
31-seinem / durch pider beeinilusst; die Endung -er ist nach der der
32-anderen Verwandtschaftsnamen angefügt (Bartholomae, BB. IX,
33-129).
```


## [2026-10-16T05:14:37.752Z] TOOL CALL #18: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-10-16T05:14:37.762Z] TOOL RESULT

```


```


## [2026-10-16T05:14:45.334Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -40"
}
```


### [2026-10-16T05:14:45.626Z] TOOL RESULT

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


## [2026-10-16T05:14:49.403Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in به پدید پسند باور بدرود پگاه پنهان پشکم سوژه; do python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/$w\" --note \"page 519, root Upo, Persian $w etymology\"; done; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁upo\" --note \"page 519, root Upo\"; python3 tools/fetch_source.py \"https://www.etymonline.com/word/evil\" --note \"page 519 evil\"; python3 tools/fetch_source.py \"https://www.etymonline.com/word/open\" --note \"page 519 open\"; python3 tools/fetch_source.py \"https://www.etymonline.com/word/sub-\" --note \"page 519 sub-\""
}
```


### [2026-10-16T05:14:54.616Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7d91bafe1108caff.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/be7baac48b6dcc51.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d434a189feb06a73.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bfee4ddb48131f7c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/330fd6d2e14d6c99.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2a0d8f347bbce242.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4e3cff8aa2c43c89.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cdbab0feebc04a58.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8d15f26a6d5885ed.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f2d65af8df4cd22d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a530a6b396a062fa.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f219d07d318354e8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d06e8e168f7ebab8.txt
```


## [2026-10-16T05:14:58.345Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -13 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['url'],d.get('status'),d.get('bytes'))\"; for f in 7d91bafe1108caff be7baac48b6dcc51 d434a189feb06a73 bfee4ddb48131f7c 330fd6d2e14d6c99 2a0d8f347bbce242 4e3cff8aa2c43c89 cdbab0feebc04a58 8d15f26a6d5885ed; do echo \"##### $f\"; grep -A8 -m3 'Etymology' $f.txt | grep -v '^$' | head -24; done"
}
```


### [2026-10-16T05:14:58.825Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/باور 200 6178
https://en.wiktionary.org/wiki/umeo 200 5971
https://en.wiktionary.org/wiki/بدرود 200 3220
https://en.wiktionary.org/wiki/vazaγā -1 39
https://en.wiktionary.org/wiki/پگاه 200 3950
https://en.wiktionary.org/wiki/پنهان 200 4392
https://en.wiktionary.org/wiki/پشکم -1 39
https://en.wiktionary.org/wiki/سوژه 200 2344
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁upo -1 39
https://www.etymonline.com/word/evil -1 39
https://www.etymonline.com/word/open -1 39
https://www.etymonline.com/word/sub- -1 39
-h -1 36
##### 7d91bafe1108caff
 Etymology 
 1.2 
 Verb 
 2 
 Malay 
 Toggle Malay subsection 
--
 Etymology 1 
 2.1.1 
 Noun 
 2.2 
 Etymology 2 
 2.2.1 
 Noun 
 2.3 
##### be7baac48b6dcc51
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Adjective 
 1.3.1 
--
 Etymology 
 2.2 
 Adjective 
 Toggle the table of contents 
 پدید 
--
 Etymology
 [ edit ] 
##### d434a189feb06a73
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
--
 Etymology 
 2.2 
 Pronunciation 
 2.3 
 Adjective 
 2.4 
--
 Etymology 
 3.2 
 Pronunciation 
 3.3 
 Adjective 
 3.4 
##### bfee4ddb48131f7c
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
--
 Etymology 
 2.2 
 Pronunciation 
 2.3 
 Noun 
 3 
--
 Etymology 
 3.2 
 Noun 
 Toggle the table of contents 
 باور 
##### 330fd6d2e14d6c99
 Etymology 
 1.3 
 Pronunciation 
 1.4 
 Interjection 
 Toggle the table of contents 
--
 Etymology
 [ edit ] 
 Equivalent to به ( be , “ to ” ) +‎ درود ( dorud , “ health; well-being ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /bad.ˈroːd/ 
##### 2a0d8f347bbce242
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.4 
--
 Etymology
 [ edit ] 
 (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /pa.ˈɡaːh/ 
 ( Dari, formal ) IPA ( key ) : [pʰä.ɡɑːʱ] 
##### 4e3cff8aa2c43c89
 Etymology 
 1.3 
 Pronunciation 
 1.4 
 Adjective 
 1.4.1 
--
 Etymology
 [ edit ] 
 From Middle Persian [Book Pahlavi needed] ( PWN /⁠pad⁠/ , “ to, at, in, on ” ) + Middle Persian [Book Pahlavi needed] ( nyhʾn' /⁠nihān⁠/ , “ concealment, secrecy ” ) . originally a contraction of elements equivalent to New Persian به ( be , “ in ” ) + نهان ( nehân , “ hiding ” ) , i.e. "in hiding".
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /pin.ˈhaːn/ 
##### cdbab0feebc04a58
##### 8d15f26a6d5885ed
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
--
 Etymology
 [ edit ] 
 Borrowed from French sujet .
 Pronunciation
 [ edit ] 
 ( Iran, formal ) IPA ( key ) : [suː.ʒé]
```


## [2026-10-16T05:15:02.266Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 7d91bafe1108caff be7baac48b6dcc51 d434a189feb06a73 bfee4ddb48131f7c; do echo \"##### $f\"; grep -n -A3 '^ Etymology[ 0-9]*$' $f.txt | grep -i 'from\\|equivalent\\|borrow\\|inherit' | head -8; done"
}
```


### [2026-10-16T05:15:02.549Z] TOOL RESULT

```
##### 7d91bafe1108caff
341- From Middle Persian 𐭯𐭥𐭭 ( pʿn ) / PWN ( pad , “ to, at, in, on ” ) , from Old Persian 𐎱𐎫𐎡𐎹 ( p-t-i-y /⁠patiy⁠/ ) , from Proto-Iranian *pati- . Northern Luri ڤە ( ve ) .
590- From Middle Persian [Term?] ŠPYL / wyh ( weh , “ better, good ” ) , from Old Persian *vahuš ( “ good ” ) , from Proto-Iranian *Hwáhuš , from Proto-Indo-Iranian *Hwásuš , ultimately from Proto-Indo-European *h₁wésus ( “ good ” ) . Northern Luri بێ ( bı ) . Related to Old Armenian վեհ ( veh , “ sublime ” ) , an Iranian borrowing.
678- From Sanskrit अपि ( api , “ close by; also ” ) .
##### be7baac48b6dcc51
228- Borrowed from Classical Persian پدید ( padīd ) .
##### d434a189feb06a73
214- Inherited from Middle Persian [script needed] ( psnd /⁠passand⁠/ ) , from Proto-Iranian *pati- ( “ towards ” , from Proto-Indo-Iranian *práti- , from Proto-Indo-European *préti ) + *sand ( “ to look good ” , from Proto-Indo-Iranian *sčand ( “ to look good ” ) , from Proto-Indo-European *(s)ḱend- ( “ to agree, approve; to appear, seem (to agree) ” ) ) . Related to
327- Borrowed from Classical Persian پسند ( pasand ) . Compare Hindi पसंद ( pasand ) .
362- Borrowed from Classical Persian پَسَنْد ( pasand ) .
394- Borrowed from Classical Persian پَسَنْد ( pasand ) . First attested in c. 1649 as Middle Hindi پسند ( psnd /⁠pasand⁠/ ) . [ 1 ] 
##### bfee4ddb48131f7c
186- Inherited from Middle Persian 𐭥𐭠𐭯𐭫 ( w'pl /⁠wābar⁠/ ) , [ 1 ] from Avestan 𐬎𐬞𐬁𐬬𐬀𐬭 ( upāvar , “ in belief ” ) , from Proto-Indo-European *upó and either Proto-Indo-European *werh₁- ( “ to speak ” ) or Proto-Indo-European *welh₁- ( “ to wish, desire ” ) . [ 2 ] Compare Old Armenian վաւեր ( vawer ) , an Iranian borrowing.
347- Borrowed from Classical Persian بَاوَر ( bāwar ) .
367- From Urdu باوَر ( bāvar ) .
```


## [2026-10-16T05:15:07.249Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^pad \\|^pad,\\|^\\s*pad\\b.*prep\\|^ō \\|paydāg\\|padīd\\|pasand\\|wābar\\|wāwar\\|pagāh\\|nihān\\|pidrōd\\|drōd' PHD_mackenzie.txt | head -30"
}
```


### [2026-10-16T05:15:07.748Z] TOOL RESULT

```
3895:pad [PWN, for ·pty I M pd, N pal to, at, in, on.
4087:passand [psnd I N pasand] pleasure, liking.
4088:passandidan, passand- [psnd-ytn I M psynd-, N pasandidan] like,
```


## [2026-10-16T05:15:11.415Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'payda\\|paydag\\|w.bar\\b\\|w.war\\|pag.h\\b\\|nih.n\\b\\|pidr\\|drod\\|dr.d\\b\\|^[ō6o] \\[' PHD_mackenzie.txt | head -30; grep -n -i 'upa' PHD_mackenzie.txt | head"
}
```


### [2026-10-16T05:15:12.080Z] TOOL RESULT

```
590:       nigiin, "'sir [-s'l I (P ngws'r)] downwards.
2066:drod [SRM < A f1m; d1wt l I M drwd, N darod] health, well-being,
2258:ew-bAr [)ywb)l] once.
3755: --ih: depth, downward direction.
3756: -sar [-s'll M ngwns'r] downwards.
3762:nihan [nyh'n I N --] concealment, secrecy.
3832:o [OL < A <l: )w I M )w] to, at: v. also oh.
4079:pas-danisnih                        66                            payda~
4135:payda~ [pyt)k l I M pyd'g, N payda] .visible, obvious, revealed.
4136:payda~ih                                                        pazzlftan
4138:paydagenidan, payda~en- [pyt'kyn-ytn' I M pyd'gy"yd] reveal,
4140:payda~ihistan, paydagih- [pyt'kyh-stn l ] appear, be revealed.
4458:sad [IOO I M sd, N ] hundred.
5590:xwAbar [hw'pll M xw'br] beneficent.
6052:belief astawanih, wabar, wurroyisn,         blazing waxsendag.
6067:   kar, xwabar.                                wayidan, wazidan; -- flute pazd-.
6225:collect (vt.) hambaridan, harrob-, P     concealment nihan.
6314:crow waray.                                darkness tar. tarig/kih. tom.
6409:   downward -- nigfmih; upward --       dog sag.
6427:disobedience aburdframanih, spoz,       downwards nigilnsar.
6513:   yawedan.                                        explain paydagenidan, wizardan.
6748:hair moy, wars; (a.) moyen.              health drod, drustih, tandrostih.
6813:hollow gabr.                                   hundred sad.
7156:news, good'" niwe.                        paydag, rosnag.
7218:over-confidence wastarih.              peace iisanih, iiStih, drod, ram(isn);
7342:prevent abaz dastan.                              drod, friixih, padexih.
7430:remedy car; darman.                      reveal askadgenidan, paydagenidan.
7431:remember ayad kardan, ayasidan,          revealed paydag; be ,...., paydagihistan.
7821:trade pesag; wazar(a)ganih.              truth rastih, wabar, wizurdih.
7930:visibility paydagih.                     water-holder abdan.
6671:gather (vt.) cidan, gird kardan, 0 ham           hupiidixsayih; ,..., ruler hupadix-
7483:roof-tree frasp.                           satisfaction hupassandagih, sahisn,
11926:hupadixsay   ~~'Q)""                       handes·                    -~...,
11928:hupadixsayih ~ttJ'Q)'"                     handesidar          ~~t"
11931:hupassandagih          .AU U   ru   Q) ~   handesisn                 '~t'"
```


## [2026-10-16T05:15:18.025Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'upa.skamb\\|upaskamb' BRT.txt POK_full.txt HRN.txt HUB.txt | head; grep -n 'lemma: skamb\\|lemma: (s)kamb\\|lemma: skabh\\|lemma: .*kabh' POK_full.txt; grep -n 'بچکم\\|پچکم\\|پشکم\\|بشکم' BQT_v1_pages.txt FRS_pages.txt MON_part1.txt MON_part2.txt incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-10-16T05:15:18.351Z] TOOL RESULT

```
BRT.txt:8370:•  j.  upa.skamb3m  '>  AbsoL  'unter  Fest- machen': dva  dim  iiara  isSii^  . .  z^mäistfe vä  sarstvt  Vil  up'  vicitaesva  dim  patH airihä    z^mö    mdai>yqn    "zwei    Männer
BRT.txt:19136:issihe .  .  upa-skambim  (sd.)  vlHcaehia  dim paiti  aiäka  z?m!l  nid'  V.8.  lo.
BRT.txt:24577:•  ]*.  vi-zöista-  Adj,  'der  regsamste,  wach- samste': dva  dim  nara  issike  'Iqm'^ vTgvSrmtam  ">  .  .  upa.skambttn  (sd.)  .  .  ni- daiäyan'V.S.  10.
FRS_pages.txt:14438: ‫ن ‪ :‬پچکم[ کذا خانهتاستانی‌بود چون غرد ‪ ۰‬چ ؛ خم وبچکم ک[ذا] خانة تابستانی‬
FRS_pages.txt:15016:  ‫از شبستان بیشکم آمد شاه کشت بشکم ز دلبران چون ماء‬
FRS_pages.txt:22195:         ‫بشکم ‪۱۰۳‬‬                       ‫برد ‪5۰‬‬      ‫‪۰‬‬             ‫بانوی ‪۸۳۰‬‬
BQT_v1_pages.txt:17650:۹ سئظء مصخف چرباك (ه.م).بچکم - بفتح اول و کاف بروزن شبتم»
BQT_v1_pages.txt:20001:بشکم » بنتح اول و ثالث و سکون‌الی
BQT_v1_pages.txt:24075:5 راد بچکم وبشک
BQT_v1_pages.txt:25969:پشکم ه بکر اول بر وزت اشکم »
MON_part1.txt:23870:بشکم: که ,فده [- بچکم ۱ پشکم] 
MON_part1.txt:29451:پشکم ] (.) خانه‌ای که از همه سوی در و 
MON_part1.txt:29460:پسچکم: «صلهم (- بچکم] (.) (جان.)
```


## [2026-10-16T05:15:21.538Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 17648,17660p BQT_v1_pages.txt; echo ===; sed -n 25965,25985p BQT_v1_pages.txt; echo; awk 'BEGIN{RS=\"\\f\"} {n=split($0,a,\"\\n\")} /پشکم ه بکر اول/{print \"LEAF\",NR-1}' BQT_v1_pages.txt; sed -n 29449,29458p MON_part1.txt; sed -n 8366,8372p BRT.txt | cut -c1-400"
}
```


### [2026-10-16T05:15:22.289Z] TOOL RESULT

```
Exit code 1
۷ رد : یج
ره :پزخك .
۹ سئظء مصخف چرباك (ه.م).بچکم - بفتح اول و کاف بروزن شبتم»
خانة 7 اطراف آن را شکه
کرده بشند ۱ - و ابوان و سفه و بارکده را
نیز گویند - و بمعتی کر که هم آهده است که
بعربی ذئب‌خوانند » وبکسر اول هم درست‌است
بچل - بر وزن کچل . شخصی را گویند
که پیوسته لیای خود راضایم کند و چرلگوملوث
گرهاند .
چم ع بکر اول بروزن شکم » کاریرا
وید که با نظام و آراستگی بود ۴ - و اعر
بچمیدن هم هست که خرامدن بناز باه یعنی
(eval):1: == not found
```


## [2026-10-16T05:15:28.430Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25965,25990p BQT_v1_pages.txt"
}
```


## [2026-10-16T05:15:29.545Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /پشکم ه بکر اول/{print \"LEAF\",NR-1} /بچکم - بفتح اول/{print \"LEAF2\",NR-1}' BQT_v1_pages.txt; sed -n 29449,29462p MON_part1.txt; sed -n 8368,8371p BRT.txt | cut -c1-500"
}
```


### [2026-10-16T05:15:29.932Z] TOOL RESULT

```
ی ماد و کسك
کلیدانرا لیز گوبند .
پشکلید » بکر اول و لام بروزن دل
کشد * یعنی بناخن وانکشت رخن ه کرد
پشکم ه بکر اول بر وزت اشکم »
اموان وبا ر گاه وا گز نش ۰ رضتح اول نیز همسن
معنی آهده اس ۷ :
بشل -
ی
هد چز را کو ند که مکدنگز زشیفا مدا کند:
و بفتح ال و ثانی هم بنظر آمده است ؛ ویسنی
که مد دو چیز است که با مکدیگر بگیرند
وبکوبند» و پاین معتی بجای حرف اول نون هم
گفته اند؟ .
بشلنگ - نم اول و فثح لام بر وذت
۱ قلمه‌ای را کون دکه برقلهٌ کوحی واقع
شده باشد - و بمعنی تافص و هرزه وعوب‌ویی
نیز گوندد که بنابان بدان دبوار سوراخ کنئد -
ویشنگه‌یدراف راسیاب رانیز یشاک میگفته‌اند. #۷
پشما گنف* م بنخ اول و سکون انی
۹۹ رك: بشکلیدن. «لغت نامه*.
۳ وك: بشلیدن: «لفت نامه» .
--م ۰ ح
و میم بالف کشیده وکاف‌فارسی مفتوح پنون‌ودال
ابجد زده , چیزی باشد که نرا پریشم کنند و ما
بين پشت‌ستود و تنگک بار گذارند وپالان الاغ‌را
```


### [2026-10-16T05:15:30.276Z] TOOL RESULT

```
LEAF2 457
LEAF 636


پشکم ] (.) خانه‌ای که از همه سوی در و 


بجر ۵ 0 خازه تابستانی. بارگاه ایوان» 


صقه. 


پسچکم: «صلهم (- بچکم] (.) (جان.) 


Obfniu,  LP.  aus /arf-?  Die  beiden  andern Wörter  scheinen  l'äzand  lusein.  —  Pü.;  fehlt.
•  j.  upa.suxta-  Adj.,  PPfP.:  s.  sai^i-.
•  j.  upa.skamb3m  '>  AbsoL  'unter  Fest- machen': dva  dim  iiara  isSii^  . .  z^mäistfe vä  sarstvt  Vil  up'  vicitaesva  dim  patH airihä    z^mö    mdai>yqn    "zwei    Männer
sollen  .  .,  indem  sie  ihn  (den  Leichnam) an  (mittelst)  Lehmziegeln  oder  Steinen festmachen,  ihn  Über  einer  Kalkunterlage auf  die  Erde  hinlegen"  V.  Äio'^.
```


## [2026-10-16T05:15:35.962Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -B30 'Page(s): 91[56]' POK_full.txt | grep -n 'lemma\\|skamb\\|Page' | head"
}
```


### [2026-10-16T05:15:36.300Z] TOOL RESULT

```
31:74946:Page(s): 915-916 
63:75059:Page(s): 916-917
```


## [2026-10-16T05:15:38.667Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=74900 && NR<=75059' POK_full.txt | grep -v '^$' | grep -i 'lemma\\|meaning\\|skamb\\|Avest\\|Page' "
}
```


### [2026-10-16T05:15:38.998Z] TOOL RESULT

```
Page(s):915 
Root/ lemma: siu-{*kf-u\n centum languages) 
Meaning: to sew 
Root / lemma: s/u- : to sew, derived from Root / lemma: se(i)-3, -sai- : 5/- and sei- : si- : to 
Page(s): 915-916 
Root / lemma: sArab^- skarrt^- 
Meaning: to support 
Material: Old Indie skabhnati, skabhnotr propped ', Perf. caskambha, skabhayatF 
fastened, ligated, strengthened, reinforced, made fast; fortified '; skambha-rc\., 
skambhana-m^ prop, pillar', Avestan i/y055/r5/77i6'a/77 'under fastening, strengthening ', 
fraskamba-, frascimbana- " girders, pillars '; npers. paskam " a covered walk between 
columns, colonnade, piazza, arcade, gallery, porch, portico ', sogd. sk'np- {*skamb) " base 
die Aryan within nasalization, as well as the e-vocalism from Avestan frascimbana- 
(compared with Old Indie skambhana-m) reshuffling through Aryan from skabh- after 
Page(s):916 
Root /lemma: (sjkamb- and (s)kemb- 
Meaning: to curve, bend 
Root/ lemma: {sjkamb- and (s)kemb-\ "to curve, bend' derived from Root/ lemma: kam-p- 
gripped by the hand ' (also ' stuff of hemp ', in which meaning certainly influenced by hamp 
from a basic meaning " go crookedly ' from reiht man an: gr. *OK£|jpu) " limp ' 
Page(s):918 
Root / lemma: (s)kand- (s)kend- 
Meaning: shine 
Page(s):918 
Root / lemma: (s)kai- (d-), (t-) 
Meaning: shining, bright 
splendid, bright', n. 'apparition' = Avestan c/^ra- ' augenia\\\g, clear, bright' (ablaut, with Old 
Page(s): 916-917
```


## [2026-10-16T05:15:42.684Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'skamb\\|skabh' CHEUNG.txt | head; grep -n -i 'paskam\\|pa.kam\\|b.kam' HRN.txt HUB.txt CHEUNG.txt IEC.txt | head; grep -n -i 'upa.d.ti\\|upa.d[iī]ti\\|upa.gāh\\|upa.g[aā]h' BRT.txt | head -5"
}
```


### [2026-10-16T05:15:43.196Z] TOOL RESULT

```
22503:344 *skamb 
22506:*skamb ‘to support, use as support’ 
22536:*SANSKRIT: skambh ‘to support, prop’ (RV+) = EWAia II: 750 
52003:skambh, 344 
55869:*Hmai', *skamb (s.v.), *suaH 
58098:*rap/f, *skamb 
58269:*skamb 
HUB.txt:1390:auch nicht in np. paSkam^ {piskam^ baskam, biSkam)
HUB.txt:1393:Halle, Stockwerk*, sondern fiihre np. paSkam = arm.
HUB.txt:1397:persischen wurde *patskamb zu *paskamb, ehe pat-
HUB.txt:1544:oben Nr. 312—314 gezeigt. Nach np. paskam = arm.
HUB.txt:6764:np. paskam *aula' = arm. patskainb = ap. ^patiskanba- (s.
HUB.txt:9171:paskam 'domus aestiva' = arm. patskam, patskamb *6emach*
HUB.txt:10644:paskam 41, 191.
CHEUNG.txt:15455:surround; to apply’, ? LKh. parkam- (parküfi-) ‘to sprinkle, scatter’ || (+ *ui-) OKh. 
CHEUNG.txt:22521:*NWIR: (+ *pati-) NP paskam ‘court, vestibule’, Yzd. (Zor.) paskam ‘portico’ || (+ 
CHEUNG.txt:37189:parkam- (parküü-), 230 
13191:dazu  tun':  yni  *pai(isii (sd.)  unuini  upa.- daoJüi^"*  i-atufris  parö  upa.dätii^"''  \fra- slirmte  aratu/ri^'Ü.toi  (?).  b)  'hinbringen zu  — ,  unterbringen  in  — '  (Lok.);  upa sUninaiiu  (sd.)  värfma  äaiie  (3SPM.)  .  . *vtspqmAu}yaitXm  Yt.5.  130.
```


## [2026-10-16T05:15:45.560Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1385,1400p HUB.txt; sed -n 9169,9173p HUB.txt; sed -n 22503,22525p CHEUNG.txt"
}
```


### [2026-10-16T05:15:45.910Z] TOOL RESULT

```
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
arab. sunbok (de Lagarde, Symmicta p. 60), arm. smbak
(5. Jhd.), ap. *su(n)ba' oder *sn(n)pa-j vgl. zd. sofa- *Huf';
paskam 'domus aestiva' = arm. patskam, patskamb *6emach*
= ap. *pati'skamba' (oben p. 41).
b) ni ist urspriinglich in: dtmi = dunb^), dnnba,
344 *skamb 


*skamb ‘to support, use as support’ 
*AVESTAN: (+ *fra-) YAv. frascinb- ‘to support’ = Liste: 63 
Partic.: perf. pass. YAv. frascimbana- (V 18.74); Caus.: pres. OPT. 3sg. YAv. frascinbaiiöit (V 18.74) 


*MIDDLE PERSIAN: (+ *pati-) MMP *pdyskmb’n ‘rooms’ > DMMPP: 273b 
*KHOTANESE: skim- ‘to create’ || (+ *pari-) LKh. paltcimph- ‘to check’ || (+ *fra-) 
haskim- (haskau-) ‘to make’ || (+ *nis-) LKh. *naltcimph- (nitciph-) ‘to remove’ 
= SGS: 128, 76, 150, 49 

*SOGDIAN: BSogd. sk’np, BSogd. ’Sk’np ‘world’ || (+ *pati-) BSogd. ptsknpy ‘porch, 
eaves’ 

*CHORESMIAN: (+ *para-à-) pr’Skm- to rob; to deceive’ = Samadi: 150 

*NWIR: (+ *pati-) NP paskam ‘court, vestibule’, Yzd. (Zor.) paskam ‘portico’ || (+ 
*ш-) Kurd. (Kurm.) biskavtin/biskév-, (Sor.) piskiwin/piskiw- ‘to take out, loosen 
[thread]; open [of flowerbuds]’ 

*NEIR: Pash. skam ‘tent-pole’, ? Yi. Skob-/Skaboy ‘to lift up, raise’ (Zarubin) || (+
```


## [2026-10-16T05:15:53.440Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'pagāh\\|pakāh\\|pagah\\b\\|pakah\\b' NYB_vol2_glossary.txt PHD_mackenzie.txt HUB.txt | head; grep -n -i 'paitid\\|padid\\|paydāk\\|paitak\\b\\|paitāk' NYB_vol2_glossary.txt | head -5; grep -n -i 'pasand\\|wāvar\\|vāvar\\|wābar' NYB_vol2_glossary.txt | head -5"
}
```


### [2026-10-16T05:15:53.837Z] TOOL RESULT

```
HUB.txt:10609:pagah 42.
1073:paitak ku 912811; u hac-ic öisän 4011; pat tan brah ...u pat-ic zor u nérok 141°; Yam u an-ic varcävand 44%, ete. — c) corre- sponding coordination: -c... -e: tdi ērān- ic viyan kunénd tai amäh-ic be daném 2022;
1123:cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921; exclama- tory: how...! 614. — 2. indirect inter- rogation: äkäh hom ku ~ hän 571; vēnēt ki Bastvar kārēcār ~ nev kunēt saw how valiantly B. fought 2815-16; ~ 6, 6 ham pursem 57°, andar Garodman dätistän ~, api-m nē dit 527-3; ete. — B. rel. adv. so as: l. har 3 šap x"amn ~ dit Estät ... guft such as he had seen it 2%; 215, 48, 520, 4527, ete.; introducing quotations: ~ den göbet 387, ~... paitāk ku 4571-5, etc. passim; parenthetic, e.g. 7718, 818%; — with a demonstr. antecedent: hamgönak hast ~-am guft 1216-17; šmāh bat ētūn m to gobeh 2329; 4524-25, 782.4, etc. — 2. with- out a clause, used prepositionally: as, as (for instance), as it were, like: ~ agäh aköc martom 2678-27; ~~ martom kë šarm 43913; 12813; varcāvandān i ~ Yam u Frétón ... 45°; hàn 4 ~ én such a th. 438; namely 1078; — with a demonstr. antecedent: &ön ~ āluh-ē 9%; eton ~ to 1516; ét6n but ~ amahraspand-ē 38°”; — čton, or ógón, homänäk (a. v.) ~ 69%, ete.; mänäk(k)äi (g. v.) i õi ~ ke pus... bare (opt.) 418. — C. conj. 1. causal be- cause: ~~... hdn mazantom bit 613-4; 1081. 11812; almost as a rel. pron. with a sec- ondary causal sense (as in Lat. quippe qui): 6 xuähar i x*"e$, ~ zan 4 Artaxsér būt, nämak nipišt 822; 718%, 7916. 116%. 11819; — hac han ~ in view of the fact that, considering that 38. — 2. temporal as soon as: 6°. 15°. 44°, more emphatically ham-~ 1317. - 3. ~ ka as if 11214.17, 10120722 — 4. almost = that 8722. — MPrth cw'gwn; MPrs ewn (read ci'on < *ciwön <
1256:én apčcak ~ i mäzdesn 244; veh ~ 4 apčcak 5914; (En) apécak veh ~ 4 maz- desnān 819. 844; ~ i Ohurmazd 60%; ~ stayitan, ~ yastan: v. these ws; — in particular: the authoritative canonical texts of this religion: én ~, cigon hamäk apastak u zand namely, the whole Avesta and commentary 1078; the quotations from these texts are introduced by the following formula: cigén ~ göbet followed by ku 3613-14, 421-13, 4520, 4615, 484-18, 491-16. 5224, 53%. 541-17; followed by hat (q. v.) 387-8. 4375-26, 4414-15, 503-5; without following particle 41196; (7) cigon et i ~ gobet ku 5323-24, 563. 581. 608. 617-8; cigon pat ~ 7718, pat hàn i ~ göbet kū 4345; andar ~ guft estet 8011; an-ic ~ gobet ku 3819; hac ~ (čičn) paitäk kü 341. 8612-115; cigón hac apécak veh- ~ i mäzdesnän paitäk 819-9; v. further paitäk and paitakéh; v. also s.v. dipivareh. — Av. (662 sqq.) daenä-; Arm. lw. den; MPrthPrs dyn religion, religious community, church; Paz. din. — Cf ak-dénéh, dén-burtàr, denik, dušden, huden.
1293:dit [HZYTN-t'; 1116 with wrong ideogr. TWB for dyt' misread as dit] sight: pat ~ visibly 1116; pat ~ ävurtan to make manifest, to give evidence of 4%. — NP padid; p. ävurdan = BP.
1671:giyak [gyw’k] place, with the indef. art. „«-ē [+1 or -y] 718.21, 814 ete. passim; pl. eas. obl. ~-dn 861’; as a philosophical term 31?. 109%; hac an ~ paitak from another passage it is evident (that) 4524-25, pat ~ bütan to be at the place 626-26, 71; — apar ~ 321, 107, pat ~ 947-8 on the spot, immediately; ~ without prep. id. 145; — —-č in a place 97?*; ~ ~ from place to place 9326-27, everywhere 977°; ham ~ on this very spot 122%; hamäk ~ all over 5721; visen (g. v.) ~ in all places 9718; Z ~ to one place 981; katüm ~ whither? where? 75. 85. — Inscr. and Ps. gyw’k; MPrs gy'g; Paz. jāt, gà; NP jā; < *vivāka-, whence viyāk (q. v.).
2019:hömikän [hwmyk’n'] containing haoma, “haomic”: äp + ~ 5623.15, — As to the suff., cf östikän, vāvarīkān; šāhīkān ‘royal’ FrP 2. — V. also *huhömikän.
2990:side: though according to law a daughter only inherits half as much as her brother, yet, in order to prevent the fatality that she, as a poor maid, must remain at home and suffer the contumely of not being married, she may be given the same share in the inheritance as her brother: this is beh-dädastäneh (Phl: veh-dätistäneh) ‘surplus award’. — Paz. NP pasand; < *pat-sand-, v. next w.
3940:Ghilain 79, is an error]; Arm. lw. vawer, vawerakan < *vāvarya(kana)- ‘true, valid, authorized’ (thus in the sense of *vä- para-); — MPrs wbr, wbryg ‘faith’, w?bryg?n ‘true’, possibly also pl. cas. obl. 'the believers'; on the other hand MPrs w^wrydn ‘to believe’, in all probability borrowed from Prth; Verbum 195, Ghi- lain 79, S, Gloss. s. v. w’bryg’n. — BP always w’pl-, mostly in the sense of ‘true, truth’, seldom ‘belief’; Ps. w’plyk’n ‘true’; Paz. vawar ‘truth’, but vafringqni (SGV) through confusion with Gfrinakan;
6769:patmoxtan pašsār: patisär padvazed: pat-vac- padyavand- patiyavand pšč: pad paēdā, paidà: paitäk pačma(n): patman pačvand: patvand pačvastan: patvastan pahalim, pahlum : pahlom paharčxtan, paharčž-: pahrčxtan parastidan: paristätan pardazašn: pardaxtan pasand: passand pasaxt: passaxt päsux: passaxu paščman, -màni: pašč- mančh patit: patit patkàr: ~ päya: pädak péda: paitäk pédabar: paitäm-bar pčrož: pérdz pēš: ~
```


## [2026-10-16T05:15:57.358Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3936,3940p NYB_vol2_glossary.txt | cut -c1-900; grep -n '^pinhän\\|^pinhan\\|pinhän' NYB_vol2_glossary.txt | head -3; grep -n -i 'drōt\\|drut \\[' NYB_vol2_glossary.txt | head -3"
}
```


### [2026-10-16T05:15:57.704Z] TOOL RESULT

```
w’nyst (BBB).
vanj- [wnc-] *to hold exactly, pres. pass. 3d p. sg.: dek i catrusvätak vanjihet [wneyhyt', restore the reading of M] a pot in which is contained (which holds) a quarter (?) 428-9. — NP gunjidan ‘to be contained or held; to hold exactly, to be filled’.
vaparikanéh [w’plyk’nyh] truth, trust- worthiness 361. — Two ws. of kindred meanings have intersected here: 1. *vā- vara- ‘choice’, ‘adoption of the true faith’, hence ‘conviction, belief, faith’, from Av. (1360 sqq.) ?var-, pres. vävar-, vdur-; 2. *päpara- ‘fulfilment, realization of the conviction or the faith chosen’, hence ‘the realized faith: truth, validity’, from Av. (850) ?par- ‘to fill, to fulfil, to perform (e. g. an act of piety)’, pres. pāfr-, the zero-stage of *päpar-. Original *pa- para- became *väpara- through dissimi- lation, certainly prompted by the in- fluence of *vàvara- whose meaning falls within the same semantic range. In Prth
vüvara-, in Prs *väpara- prevailed: MPrth wwr, wwryft ‘faith’, ’w’wryg ‘unbeliever’? [w’wryg’n ‘the believers’,
Ghilain 79, is an error]; Arm. lw. vawer, vawerakan < *vāvarya(kana)- ‘true, valid, authorized’ (thus in the sense of *vä- para-); — MPrs wbr, wbryg ‘faith’, w?bryg?n ‘true’, possibly also pl. cas. obl. 'the believers'; on the other hand MPrs w^wrydn ‘to believe’, in all probability borrowed from Prth; Verbum 195, Ghi- lain 79, S, Gloss. s. v. w’bryg’n. — BP always w’pl-, mostly in the sense of ‘true, truth’, seldom ‘belief’; Ps. w’plyk’n ‘true’; Paz. vawar ‘truth’, but vafringqni (SGV) through confusion with Gfrinakan;
```


## [2026-10-16T05:16:01.071Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'pag[aä]h\\|pegäh\\|upa.g\\|upagä' HUB.txt | head; grep -n -i 'pad[iî]d\\|pidid\\|upa.dait\\|upa.diti\\|padrud\\|pedrud\\|bedrud' HUB.txt | head"
}
```


### [2026-10-16T05:16:01.437Z] TOOL RESULT

```
10609:pagah 42.
648:blieb pa in jiingeren Zusammensetzungen [padrud,
649:padid^), pinhan, pinddstan) , in denen seine urspr.
1273:oben Nr. 144. Das Wort padid sichtbar ist erst im
1275:wie padrud aus pa und drut (Horn, Nr. 288).
1444:*Zeit' (wie padrud^ padtd u. s. w. siehe Nr. 144) ge-
2128:Das Wort gehSrt zupadrUd (Horn Nr. 288), das bei
5984:paz. drud Min. Gl. 64, Shk. 242 und np. padrud
6091:padrud *Lebewohl') = ^druvatdt-^ arm. druatHc; durudan
6189:frah ; np. ba (neben pa in padrud u. s. w.) = paz. pa (s.
```


## [2026-10-16T05:16:03.555Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 640,652p HUB.txt; sed -n 1268,1278p HUB.txt; sed -n 1438,1448p HUB.txt"
}
```


### [2026-10-16T05:16:03.938Z] TOOL RESULT

```
daher nichts tibrig, als np. ba = bad liber paz. pa =
pad nur auf ap. patiy zuriickzufUhren. 3) Als erstes
Glied von Compositen wurde pati- mp. zu pat- (neben
paJ- und pa-y vgl. Nr. 345), das im Neup. erhalten
blieb, wahrend das selbstandige pati mp. zu pad (vor
Vocalen) oder pa (vor Consonanten, zuerst wohl vor Den-
talen) wurde, um dann (allerdings gegen die Kegel : anl.
p = np. p) im Neup. in bad^ ba uberzugehen. Erhalten
blieb pa in jiingeren Zusammensetzungen [padrud,
padid^), pinhan, pinddstan) , in denen seine urspr.
Bedeutung verwischt war und nicht mehr gefiihlt wurde.
145. Np. bd, aba *mit' geht durch paz. awd [nicht awdkl]
mit* (Min. Gl. 25, Shk. 232), phi. *apak (in apakth
(haca parumyata Von Alters her') ? Vgl. mirad *stirbt*
aus *infyatai.
287. Np. pid/ram erfreut' wird aus ^paiti-raman- erklart.
Warum dann nicht *pairam*i^
289. Streiche die Worte: „al80 aw. ^upadtti-'' und vgl.
oben Nr. 144. Das Wort padid sichtbar ist erst im
Mittelpers. componirt aus pa und dU == 'in Sicht'
wie padrud aus pa und drut (Horn, Nr. 288).
291. Np. padtra 'entgegen = paz. padtra Min. Gl. 151,
Shk. 261, phi. patlrak Gl. and Ind. 95 etc. lasst sich,
da phi. paVSrak fest steht, nicht auf ein phi. "^patglrak
(fur *fra'hincanti) haben, wie im Phi. asindttan *be-
giessen* (Horn p. 267) fiir *ahindUan.
324. Np. pciffdh *der fruhe Morgen, friih' (Fird. I, 456, 391
u. s. w.) kann weder =-- zd. *upakasa' noch = zd.
^paitikOsa- gesetzt werden, sondern wird am besten
mit N old eke als mp. Neubildung aus pa und gdh
*Zeit' (wie padrud^ padtd u. s. w. siehe Nr. 144) ge-
fasst, so dass es urspriinglich *bei Zeiten, zeitig
bedeutet.— 43 -
327. Np. panah 'Zuflucht, Hulfe' = paz. panah Min.
Gl. 154, Shk. 262, phi. panah Phi. Min. p. 15, 10,
```


## [2026-10-16T05:16:14.571Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in 'پگاه' 'پدید' 'پسند' 'پنهان' 'بدرود' 'باور'; do echo \"== $w\"; grep -n \"^$w\\|^ *$w *[:\\[(]\" MON_part1.txt | head -3; done"
}
```


### [2026-10-16T05:16:15.226Z] TOOL RESULT

```
== پگاه
6343:پگاه خیزانیدن» به وقت از خواب بیدار 
24581:پگاه‌خیزی» سحرخیزی. 
32365:پگاه: : 0۵-28 [- بگاه» بهنگام] (ق‌مر.) صبح 
== پدید
2037:پدید آید» زايندةٌ آتش. 
14547:پدید ساختن. (ا.) آ گهی؛ ج. اعلانات. 
14861:پدید آوردن. (صر.) یکی از پایه‌های لائی 
== پسند
8916:پسندیده» صفات نیکك. ترکث ادب: آزرم و 
9511:پسندبدن» خشنود شدن. اختبار کردن؛ 
31847:پسندیدن) بپذیر! قبول کن! مطبوع خاطر. 
== پنهان
24312:پنهان» نهانگاه» بن‌بغل. بغل باز کردن: در 
30347:پنهانی» برده غیب. (تص.) مرحله» مرحلهة 
32936:پنهان: 060.۰ ,۳2130 (ص. ق.) نهفته» 
== بدرود
21615:بدرود: ۷21۳14 [- پدرود] (.) سلامت. 
== باور
21088:باور: ۲ (.) قول سخن» بذبرش قول 
31924:باور» کمک حامی؛ معین » معاصد» ملاذ» 
41098:باور. (منط.) حکم کردن بر تصوری که در
```


## [2026-10-16T05:16:20.923Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://vajehyab.com/?q=سوبلیمه&d=moein\" \"https://vajehyab.com/?q=سوژه&d=moein\" \"https://vajehyab.com/?q=پشکم&d=moein\" \"https://www.etymonline.com/word/evil\" \"https://www.etymonline.com/word/sublime\" \"https://www.etymonline.com/word/open\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 519, root Upo\"; done 2>&1 | tail -8"
}
```


### [2026-10-16T05:16:22.911Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/38c3c12d31703f88.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e720e7fcc61ab291.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/088daaaa118a5dd5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a530a6b396a062fa.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1655249fb605dfcf.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f219d07d318354e8.txt
```


## [2026-10-16T05:16:28.279Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 38c3c12d31703f88 e720e7fcc61ab291 088daaaa118a5dd5 a530a6b396a062fa 1655249fb605dfcf; do echo \"#### $f $(wc -c <$f.txt)\"; grep -m3 -n 'سوبلیمه\\|سوژه\\|پشکم\\|Old English\\|Latin sublimis' $f.txt | cut -c1-400; done"
}
```


### [2026-10-16T05:16:28.684Z] TOOL RESULT

```
#### 38c3c12d31703f88 712
1:URL: https://vajehyab.com/?q=سوبلیمه&d=moein
4:TITLE: معنی سوبلیمه | واژه یاب
6:معنی سوبلیمه | واژه یاب 
#### e720e7fcc61ab291 3691
1:URL: https://vajehyab.com/?q=سوژه&d=moein
4:TITLE: معنی سوژه | واژه یاب
6:معنی سوژه | واژه یاب 
#### 088daaaa118a5dd5 2902
1:URL: https://vajehyab.com/?q=پشکم&d=moein
4:TITLE: معنی پشکم | واژه یاب
6:معنی پشکم | واژه یاب 
#### a530a6b396a062fa 131
#### 1655249fb605dfcf 134
```


## [2026-10-16T05:16:31.150Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 6,40p e720e7fcc61ab291.txt | head -30; echo; sed -n 6,30p 088daaaa118a5dd5.txt; cat a530a6b396a062fa.txt"
}
```


### [2026-10-16T05:16:31.495Z] TOOL RESULT

```
معنی سوژه | واژه یاب 

 26 فرهنگ 
 48 مدخل

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 سوژه
 suže
 معنی

 موضوع؛ مضمون.
 مترادف

 ۱. مطلب، موضوع 
۲. مضمون، مفاد 
۳. فاعل

 جست‌وجوی دقیق

 ۱ واژه 
 سوژه
 فرهنگ انتشارات معین
 (ژِ) [ فر. ] (اِ.) موضوع ، آن چه که دربارة آن بحث یا آزمایش کنند.

 جست‌وجوی مترادف

 ۵ واژه 

معنی پشکم | واژه یاب 

 26 فرهنگ 
 60 مدخل

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 پشکم
 pa(e)škam
 معنی

 = بشکم
 دیکشنری

 porch, portico

 جست‌وجوی دقیق

 ۱ واژه 
 پشکم
 فرهنگ انتشارات معین
 (پِ کَ) (اِ.) ایوان و بارگاه .

URL: https://www.etymonline.com/word/evil
FETCHED: 2026-10-16T05:14:54Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
```


## [2026-10-16T05:16:38.576Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in evil open up sujet sublimé; do f=$(python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/$w\" --note \"page 519, root Upo, $w\" 2>&1|tail -1); echo \"## $w $f\"; grep -n -A2 '^ Etymology[ 0-9]*$' $f | grep -i 'from\\|borrow\\|inherit' | head -3 | cut -c1-500; done"
}
```


### [2026-10-16T05:16:41.189Z] TOOL RESULT

```
## evil /home/sfmqrb/git/rishe-private/data/verification/sources/web/f4fdcd517c200749.txt
## open /home/sfmqrb/git/rishe-private/data/verification/sources/web/e7e275e7559dcfc9.txt
## up /home/sfmqrb/git/rishe-private/data/verification/sources/web/34172a1e96b8e2ea.txt
## sujet /home/sfmqrb/git/rishe-private/data/verification/sources/web/ae9fc02cbaf281cf.txt
## sublimé /home/sfmqrb/git/rishe-private/data/verification/sources/web/d96265082159697d.txt
```


## [2026-10-16T05:16:44.228Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in f4fdcd517c200749 e7e275e7559dcfc9 34172a1e96b8e2ea ae9fc02cbaf281cf d96265082159697d; do echo \"## $f $(head -3 $f.txt | tail -1)\"; grep -m3 'Proto-Germanic\\|Latin subiectum\\|Latin sublim\\|from Latin' $f.txt | cut -c1-500; done"
}
```


### [2026-10-16T05:16:44.563Z] TOOL RESULT

```
## f4fdcd517c200749 STATUS: 200
 Proto-Germanic *ubilaz 
 From Middle English yvel , evel , ivel , uvel , from Old English yfel , from Proto-West Germanic *ubil , from Proto-Germanic *ubilaz , [ 1 ] from Proto-Indo-European *h₂up(h₁)élos , a deverbal derivative of *h₂wep(h₁)-, *h₂wop(h₁)- ( “ treat badly ” ) . See -le for the supposed suffix.
 ^ Kroonen, Guus ( 2013 ), “*ubila-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN , page 557 
## e7e275e7559dcfc9 STATUS: 200
 Adjective from Middle English open , from Old English open ( “ open ” ) , from Proto-West Germanic *opan , from Proto-Germanic *upanaz ( “ open ” ) , from Proto-Indo-European *upo ( “ up from under, over ” ) .
 Verb from Middle English openen , from Old English openian ( “ to open ” ) , from Proto-West Germanic *opanōn , from Proto-Germanic *upanōną ( “ to raise; lift; open ” ) , from Proto-Germanic *upanaz ( “ open ” , adjective ) . Cognate with Saterland Frisian eepenje ( “ to open ” ) , West Frisian iepenje ( “ to open ” ) , Dutch openen ( “ to open ” ) , German öffnen ( “ to open ” ) , Danish åbne ( “ to open ” ) , Swedish öppna ( “ to open ” ) , Norwegian Bokmål åpne ( “ to open ” ) , Norwegian N
 From Dutch openen , from Middle Dutch ōpenen , from Old Dutch opanon , from Proto-Germanic *upanōną .
## 34172a1e96b8e2ea STATUS: 200
 Proto-Germanic *ub 
 Proto-Germanic *upp 
 From Middle English up , op , oup , from Old English upp , up , ūp ( “ up ” ) , from Proto-West Germanic *upp , *ūp , from Proto-Germanic *upp , *eup ( “ up ” ) . 
## ae9fc02cbaf281cf STATUS: 200
 Learned borrowing from Latin subiectus .
 Learned borrowing from Latin subiectum .
 Borrowed from Latin subiectum .
## d96265082159697d STATUS: 200
```


## [2026-10-16T05:16:49.966Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'باور\\|پسند\\|پگاه\\|پدید\\|پنهان\\|بدرود\\|پشکم' incoming/ARY/ARY_pages.txt | head -10; grep -n -i 'upo\\b\\|UPA' incoming/ARY/ARY_latin_index_pages.txt | head -5; sed -n 14436,14439p FRS_pages.txt"
}
```


### [2026-10-16T05:16:50.386Z] TOOL RESULT

```
85:باور می‌کردند که آریایی‌های راستین مردمی بلند قامت با چشمان آبی ر موی طلایی بودند که از نظر
532:را بوجود آورد. طسبق این باور مردود کلیه‌ی زبانهای دنیا متعلق به یکی از این سه .
1120:دیگر همه ناپدید شوند.
1329:واژه‌ی لاتین ۳1۸7 و واژه انگلیسی کهن 118100 (به چم «پنهان کردن») همریشه‌اند ولی
3159:۰ باور
8476:چم این واژه در زبان‌های ژرمنی نوین: پسندیدن» گزیدن,
8477:چم این واژه در زبان‌های یونانی: مورد پسند» ارزشمند. 1
11894:چم اين واژه در سانسکریت: نهفته؛ پنهان.
15604:۳ چم این واژه در زبان‌های کهن: راحت» دلپسند.
311:AKUPO: 34-5 yl (KAPAS: gl ga) SCUAN 24S ot) | HHLAINS eS (KAUFA,
2091:‘APAR, ABAR, ABRAG,(PAHLAVD) «5 4 UPARA., UPARIY. (AVESTAN) glo, |
2092:ABARAGAN, ABARIGAN UPAIRI i
2093:UPARI, UPARA :(SANSKRIT) 2» Sit. UPARIY — (OLD PERSIAN) sul, 4 |
4134:(4, exow CHURCH SLAVIC) 4S 53%) VADHUPA AVESTAN) glen)
 ‫که‌مثل او نبود برای تنوئدوقامت » ص ‪ :‬تهمبی‌همنا بود ببزرگی وحشمت ومردی‬
 ‫‪۲‬ج ‪ ۰‬تخت ‪ - ۴‬این بت فقط در س هست بجای بیت پیش ‪- 4‬‬                ‫وقامت‬
 ‫ن ‪ :‬پچکم[ کذا خانهتاستانی‌بود چون غرد ‪ ۰‬چ ؛ خم وبچکم ک[ذا] خانة تابستانی‬
‫ناشد و نشستتگاه کهدر زبرزمین سازند چون غرد و بادغرد» س ‪ :‬بجکم نامگز‬
```


## [2026-10-16T05:16:52.931Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3150,3175p incoming/ARY/ARY_pages.txt; awk 'BEGIN{RS=\"\\f\"} /\\n۰ باور/{print \"pdf\",NR}' incoming/ARY/ARY_pages.txt | head -2"
}
```


### [2026-10-16T05:16:53.343Z] TOOL RESULT

```
:
پهلوی (41اتل۸): 20 ‎ -‏ نورس کهن (۱۷0788 010):
سانسکریت (8۷5077): ۷۸5۸۷ ساکسونی کهن (/(54300 00): ۰ ۲۷/۸۲۸
ارمثی ((۸45(4/): لا زان فریزی کهن (40ا5ل۶۸ صا۵): ۰ ۷۷۸35
لاتین (۸710): شاد د دیا آلمانی کهن (۷ل087014 07 آتز صا0):
ایسلند یکین ((7۵ مهم صا۵): ۷۸۸
۷۸7۸ آلمانی (08701۸00): دس ای
زر ی با
[pdf page 109]
۰ باور
انگلیسی ,گهن (5/0/3/7ظ ۰:۵۵ ,۲۷/5۸7 اپرلندی کهن (#اکل۸ا صه). ی ادن |
انگلیسی (ن82للا0/(ق): ۷ برتونی (88870/1): اد 8( بد 11 ری
دانمارکی (0۸0۷1870): ۷۱07 و
سرئدی (/3(780/5): ۷۸ پسگشت‌ها اس ۳
نروژی (/(0/08۷014: ۷78 51 موووهرن ۷
هلندی (070[7): ۷۸5 0 0۸۵ 7
اسلاوی کهن (0//شا5 ۲27064 صا0): 2 (۷۸33) :541
۷۲ (1101130) :۸2(5 ۸ لت
روسی (/81/5542): راد دیا برهان قاطع + ۲۳۴
لینرانی (7214(/142/.): ۸35 ,۷1513178 فرهنگ معین : ۴۷
آغرنی (لتی) (71۸(1ما): در ۱/۱
بادداشست:
۱- 0810818 و 8168۸7 ریشه‌های غیرژرمنی اين واژه نمی‌دهند.
۲- فرهنگ معین و برهان قاطع : و لفت‌نامه‌دهخدا ریشه‌های این واژه را نمی‌دهند. ۱
۳ معنی این واژه در برتونی: دُمل
۴ معلی این واژه در لیتوانی و لتونی: وزغ
pdf 109
```


## [2026-10-16T05:16:58.547Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:2230 2>&1 | head -60"
}
```


### [2026-10-16T05:17:05.561Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 313; check the printed number and re-run with --pdf-page if off)
REF: BQT:2230  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 313  OCR-lang: fas

ید نی

وشلوارباشد- وبقچه رانیز گوبند ۱ وآن پارچه‌ای | لیف پوستین کفته‌اند و از آن رویاه خواسته‌اند .
باشد مربع که رخت پوشیدنی و غیره را در آن | اسّاعلم. 6
پندند - و پوست شکم جالوری هم‌هست اوپوستین یل « بر وزن دیل . حشیشی باشد که
را نیز کفته‌اند چه لیغةٌ روباء بمعنی پوستین روباه
باشد ۴ - و بمعنی‌رویاء نیز بنظر آمده‌است‌چنانکه عصارة آنرا یمنی‌فشردء آنرا لیله کوبند و بدان

- فرهنگه شرفنامه این بیت نظامی را شاهدآ ورده :

بمی تافهٌ مهر باکرده باز ز لیفه بسی جامهٌ دلنواز .

رشیدی کوید : ۶ درین تأُمل است » ء رشیدی خود این بیت را شاهد پوستینآورده است.

۴ - شیرکز مالش عدل نو دباغت پاید کردش نرم تر از لیفهٌ روباه شود.

شرف شفروه « رشیدی >.

6 تيك - تلفظ قدیم 28۴ « اسشق ۰۱۳۹۸ تلفظ کنونی 816 ؛ قس: نیکو ,یکی
پارشی باستان -28188 ( خوب , فشنگه ) . پپلوی 38۷2 , 8869۷ « اسشق ۶*۱۰۹۸اودوالا
۰ » کردی ع ۶ ليك > (خوب) «ژابا ۸۲۸ ؛ خوب - مردخوب » شخص نیک و کردار:
پرئو لیکان نگیرد هر که بنیادش بد است تربیت با اهل را چون کردکان بر گنبداست.

کلتان س ۲۲ >.
ور : نیکی. - سخت » بسیار :
چه سخت ست کرفتی وليك بد کردی هزار پار ازین رأی باطل استغفار .
سعدی « فرهنکه نظام >.
این‌کلمه در ترکیباتی نظیر: ليك‌بخت . ديك‌بختی » بيك‌نام . ليك‌نامی » ليك‌اختر , ديك اختری,
بیك‌پی, نيك‌اندیش . بيك دل ونيك سرشت آید .

5 لیکو - تلفظ فدیم 886۵ «اسشق ۰۱*۹۸ تلفظ کنوبی 2150 ؛پهلوی 88۷/216
«اونوالا ۱۳. 88)۷8(6۵6 3 نیبر که ص ۱۵۷ > دراوراق مانوی ( پهلوی) ‎8٩7۷۳۷‏ (زیبا)
(.۰86 12 ,18 ,8805 ,مققن86۳ 3۸:4016 0۶ انا هروهنط 1100 ) این که
توسمه‌ایست با ۵۴ - ( برای صفت . ۵1 - از 2۷8-52 -) و محتملا جدید است « لیب رکه
س ۱۵۷ ؛ خوب . ليك - شخص خوب رفتار - زیبا . اين‌کلمه در ثر کیبانی نظیرنیکو خصال »
لیکو رای ۰ نیکوسیرت ۰ لیکوکار » نیکونام » لیکونهاد » لیکو کمان آید .

۰ نیکویی - نلفظ قدیم 885۵1 تلفظ کنوبی 81601 ؛ از : نیکو (هم.) + ای
( حاصل مصدر » اسم معنی ) ؛ خوبی » خوشی, نیکی : * عمرو او را ( احمدین ابی‌الاسبع را >
کرامت کرد بسیار وبتواخت ... و به نیکوبی با ز کردانید .» « تاریخ سیستان صس ۲4۹ >-زیبایی.

2 لیکی - تلفظ قدیم 1ا26 « اسشق ۱۰۹۸ ۰ تلفظ کنوبی 8161 ؛ از: يك(.م.) +

ای ( حاصل مصدر » اسم معنی ) ؛ خوبی » نیکوبی : * پیداکردن شاید بود هتیها ازجهت یکی .
وبدی . لیکی‌دو معنی راکوبند : یکی مرآن لیکی راکه چیزی را بخود برد که خود لك بوده
وآن آن بود که کمال وی ودرا بود » وچون نود ناقص بود ... » و یکی نیکی‌آن بو د که از وی
مرچیزی دیگر راآن یکی بیشتر بود...» ۸« این‌سینا. دانشنامه . الهمی مسحح نگارنده رام هه
```


## [2026-10-16T05:17:10.758Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; grep -n 'نهان -\\|نهان ـ' BQT_v4_pages.txt | head; awk 'BEGIN{RS=\"\\f\"} /نهان - /{print \"pdf\",NR}' BQT_v4_pages.txt | head"
}
```


### [2026-10-16T05:17:11.517Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:17:14.679Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; grep -n 'نهان' BQT_v4_pages.txt | head -20; grep -n 'pdf page 30[0-9]\\]' BQT_v4_pages.txt | head"
}
```


### [2026-10-16T05:17:15.147Z] TOOL RESULT

```
1534:ری چهره را بچه بد در نهان آزان شاد شد شهربار جهان ...
1853:پنهان شدم باشد که (۳) مقابل آشکار: است - ودر مقیل « بکس اول واثانی و سکون
4775:۲ - برکی ومتبلی وحرص واز چون کنی پنهان بشید , ای مکرساز!
5235:زمی‌دالانهانی حفر و برروی آنها تپه‌ای ازخاشاك بنا میکنند . جمع مورچه » مورچگان آید :
5412:پوزء مخروطی و دست وپای بسیار کوتاه . چشمهای كوچك موش کور زیر موهای باحيةٌ سر پنهان
6780:نابسی ۱ - بنتح ثالك و سین بی قله | بوشیده وینهان هم‌آمدت است .
7553:عربی « ناموس » ساحب رازآ کاه بر نهانی امن - با صاحب راز خبن - و نام جبرئیل علره‌اللاي
7555:نهانی - وخوایگاه شیر» ناموسة «ثله. > «منتهی‌الارب * وایز وحی - وخانةٌ راهب - و دروغزن -
7984:فیناك ۴ - بر وزن فرهاد . بسسنی طلق | و بمعنی پوشیده وپنهان هم کفته‌اند ۸ .
8008:و مولف فرهنکه نظام نویسد : ازظاهرشعرمعنی پنهان «نهوم میشود. درحاشيةٌ تاریخ بیهقی مصحح
8010:جوانی که بهرات میبود و پنهان از پدر شراب میخورد » پوشیده ازریحان خادم فرودسرای خلوتها
8020:و معنی وید است که مدکالی و خبر خوش | و پنهان هم بنظر آمده است۷ .
9012:نشغان ‎٩‏ « بکسر اول بر وزن نهان » نشغاندن *۱- معروف آمت۱۱- وومعنی
9828:وکس زای نفطه‌دار و رای بي‌قطةٌ مفتوح بدال | کفته‌اند پمنی آنچه درزمین و غیره پنهان کنند
10417:مانند مخزلی‌بجهت پنهان کردن چیزها- وبسمتی | بندند ؛ وجم اول هم آمده است .
11855:نهانگاه > بروزن و معنی شکارگاه 0 ول * یی
11890:8 نهامین - بنتح اور و کر میم بروزن نهان دره - بنتح دال ورای بی‌ضله ۰
11891:سلاطین » بمعلی آهنگر باشد ۴ که عربان حداد بمعنی نهانخانه است که کنجینه ومخزن و خالهٌ
11895:نهان پیگران - بنتم بای فرسی . نهاوند * - بکراولوتحواووسکون
11898:نهان خانه - بروزن‌میان‌خانه, کنجینه آشهر بسیار میاخته‌اند ‎٩۹‏ - و بمعنی شهرستان‌هم.
12044:[pdf page 300]
12078:[pdf page 301]
12126:[pdf page 302]
12171:[pdf page 303]
12204:[pdf page 304]
12243:[pdf page 305]
12282:[pdf page 306]
12320:[pdf page 307]
12367:[pdf page 308]
12405:[pdf page 309]
```


## [2026-10-16T05:17:17.763Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; awk 'NR<11855' BQT_v4_pages.txt | grep -n 'pdf page' | tail -1; sed -n 11860,11895p BQT_v4_pages.txt"
}
```


### [2026-10-16T05:17:18.136Z] TOOL RESULT

```
11844:[pdf page 296]
[ از کی ] با از چیزی . طیان ( مرغزی ) گوید :
لبت کوبی که نیم کفته گل‌است می و نوش اندرو بهفتستی »
زلف کوبی ز لب نهازیده امت بگله سوی چشم رفتستی -
لغت فری ص ۰4۱۶۵
۴ - اسم مفعول از ۸ نهازیدن > . ۴ <نهاله ( «.م. )کردی 2081 (کیاه ۰
درختچه) « ژابا ص4۲۹ >. « لهال » درخت نونشانده بود . عنصری ( بلخی )کفت :
بيك ماء بالاگرفت آن بهال فزون زانکه دیگر درختان بال.»
« لغت فری ص ۰۳۱۲
۴ <هالی < نهالین :
بروز جوانی بدین مایه سال چرا خاك را برکزیدی تال ؟
« فردوسی طوسی . شاهنامة بخ ج ۷ ۰۴۱۹۱۵
و رك : فهرست ولف . - ماله (و.م.) قن :کردی [20۷8 ( کردنه , دره ,
تنکه) , [28۷8 . وقی : هندی 201180 « ژابا س 4۷4 *. ‎٩‏ - از : ال (و.م.) +
کاء ( پوند مکان ) * نپالگه ۳ نهاله کاه (هم). ۷ < نپانگاه < نهاله گاء (ه.م.)
۸ - نهال (هم.)
‎٩‏ - تا زهوای توام ببند ویتاله ( به ندبه وناله . دحخدا )
عشق تو بر جان من نپاد تهاله ‏
شهره آفاق « لغت فری ص 4۳۰ >.
*- باین معنی اصل « نهالهگاء » (ه.م.) است . ۱ از : هاله (ه.م.) + کاه
( پوند مکان ) ۳ نپانگاه ۳ نهاله گه * نهالگه :
ا ز که ری در نهالهگاه توآیند روز شکار تو صد هزار شکاری .
فرخی سیستانی « رشیدی > +
[pdf page 297]
نهائه که ۷۱-۳

نهاله 4۳ ۱ - بکر اول و قح کاف خانه پسازند - وخانه‌ای را نیز گونتد که درژیر

فارسی , عمخفف نهاله گاه است که شکارکاه | زمین سازند بجهت لشستن درهواهای گرموبغریی
باهد #۰ حقره(۱) خواند ۴ .

8 نهامین - بنتح اور و کر میم بروزن نهان دره - بنتح دال ورای بی‌ضله ۰
سلاطین » بمعلی آهنگر باشد ۴ که عربان حداد بمعنی نهانخانه است که کنجینه ومخزن و خالهٌ
میگویند ؛ و باین معنی بحذف نون آخرهم بنظن زیرزمینی باشد ۴ .
آمد. است که نهامی بروزن تعامی باشد. | اه

نهان پیگران - بنتم بای فرسی . نهاوند * - بکراولوتحواووسکون
```


## [2026-10-16T05:17:24.100Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /پدید -|پدید ـ|پدید ه|پدیدار/{print \"padid\",NR-1} /پسند -|پسند ه|پسندیدن/{print \"pasand\",NR-1} /پگاه/{print \"pagah\",NR-1} /بدرود/{print \"badrud\",NR-1} /پدرود/{print \"padrud\",NR-1} /پنهان -/{print \"penhan\",NR-1}' BQT_v1_pages.txt | sort | uniq | head -40"
}
```


### [2026-10-16T05:17:24.647Z] TOOL RESULT

```
badrud 463
padid 201
padid 490
padid 597
padrud 463
pagah 640
pasand 500
```


## [2026-10-16T05:17:27.355Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==598' BQT_v1_pages.txt | grep -n -A4 'پدید' | head -30; echo ======; awk 'BEGIN{RS=\"\\f\"} NR==641' BQT_v1_pages.txt | grep -n -B1 -A5 'پگاه' | head -30"
}
```


### [2026-10-16T05:17:27.728Z] TOOL RESULT

```
Exit code 1
25:کوبند + پدیدار آمد» یعنی موجود شد.
26:پد سار باسینبی‌نقطه بروزن پدیدار,
27-برسرکاری دفئن باشدکه پیش ازین شروع درآن
28-کرده باشند و
29-پر قت « یکر اول و سکون شانی
30-و رای بیطةٌ مضموم بفا و فوفالی زده » ماضی
--
42:۱ - از: پدید ار (پسوند). ۲ - رك:پذیرفتن.
43-» بدید -بفتح اول. بهلوی 4 0۵ د«یرند که .کرنامه 44۰ ؛ فر اوستانااه 00۳02
44-«اسشق ۲۷۸۹ , نبرک پهلوی آنرا 16 084 نوشنه. «یب رکه 0۷»؛ آشکار. سامان,
(eval):1: ===== not found
```


## [2026-10-16T05:17:39.380Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==641' BQT_v1_pages.txt | grep -n -B1 -A4 'پگاه' | head -30; awk 'BEGIN{RS=\"\\f\"} NR==501' BQT_v1_pages.txt | grep -n -A3 'پسند' | head -12"
}
```


### [2026-10-16T05:17:39.812Z] TOOL RESULT

```
5-بدان بازی کنند - و بمعنی کاوری نیز آمدم یگ« بنتح اول و ثانی وظهور ها" مخثف
6:امت ۹ ۱ پگاه است که سحر و صبح باشد ۴ .
7-۲۰ ی و عتاه» و ۱
8-1 ینت دنت ون پگین» بروزن بقن‌بلت زسوپازیه (6۱. .
9-۰ ارزن‌را گونند» وآن ظهایت محروف ؟ .
10-بگوی. ختح اول و ثابی بواو کشیده
2:بسقا یمن ۲ -بروزن پسندیدن»بمعنی
3-ساخته شدن و مهیا کشتن وآنلده گردبدن باشد؛
4-و بکسی اول و فتح ثانی » و بکسر اول وضم‌ثالی
5-حردو آمده است .
```


## [2026-10-16T05:17:48.418Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f=$(python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/upo\" --note \"page 519, root Upo\" | tail -1); head -3 $f; grep -m5 -i 'upo\\b.*under\\|Avestan\\|Old Persian' $f | cut -c1-300; f2=$(python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/upa\" --note \"page 519 upa\" | tail -1); head -3 $f2; grep -m6 'Middle Persian\\|Persian' $f2 | cut -c1-300"
}
```


### [2026-10-16T05:17:51.098Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/upo
FETCHED: 2026-10-16T05:17:50Z
STATUS: 200
 Avestan: 𐬎𐬞𐬀𐬨𐬀 ( upama ) , 𐬎𐬞𐬆𐬨𐬀 ( upəma , “ uppermost; highest ” ) 
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/upa
FETCHED: 2026-10-16T05:17:51Z
STATUS: -1
```


## [2026-10-16T05:17:54.263Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; f=$(grep -l 'Reconstruction:Proto-Indo-European/upo$' *.txt | head -1); grep -n 'Proto-Indo-European \\*upó\\|under\\|Indo-Iranian\\|Iranian\\|Persian\\|Latin: sub\\|Germanic' $f | head -20 | cut -c1-250"
}
```


### [2026-10-16T05:17:54.749Z] TOOL RESULT

```
212: Proto-Germanic: *ufumô ( see there for further descendants )
214: Proto-Indo-Iranian: *upamás 
218: Proto-Iranian: *upamáh 
232: Proto-Germanic: *ub ( see there for further descendants )
237: Proto-Indo-Iranian: *úpa , *upa- 
281: Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy.
```


## [2026-10-16T05:18:01.178Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; f=$(grep -l 'Reconstruction:Proto-Indo-European/upo$' *.txt | head -1); echo $f; sed -n 180,275p $f | grep -v '^\\s*$' | head -70 | cut -c1-200"
}
```


### [2026-10-16T05:18:01.628Z] TOOL RESULT

```
4a6e9918920ea16b.txt
 *(s)up-s 
 Proto-Italic: 
 Latin: sus- 
 *(s)up-s-i 
 Proto-Hellenic: 
 Ancient Greek: ῠ̔́ψῐ ( hŭ́psĭ ) 
 *(s)up-s-os ~ *(s)up-s-es- 
 Proto-Hellenic: 
 Ancient Greek: ῠ̔́ψος ( hŭ́psos ) 
 Proto-Celtic: *ouxsos [ 3 ] ( from the o -grade ) 
 Old Irish: úas 
 ⇒ Proto-Celtic: *ouxselos 
 *(s)up-ti-os 
 Proto-Hellenic: 
 Ancient Greek: ῠ̔́πτῐος ( hŭ́ptĭos ) 
 *(s)up-iH-nos 
 Proto-Italic: 
 Latin: supīnus 
 *(s)up-ér(i) 
 *(s)úp-m̥mo-s ( “ uppermost ” ) 
 Proto-Celtic: *uɸamos 
 Lepontic: 𐌖𐌅𐌀𐌌𐌏- ( uvamo- ) 
 Proto-Germanic: *ufumô ( see there for further descendants )
 Proto-Indo-Iranian: *upamás 
 Proto-Indo-Aryan: *upamás 
 Sanskrit: उ॒प॒म ( upamá , “ uppermost ” ) 
 Proto-Iranian: *upamáh 
 Avestan: 𐬎𐬞𐬀𐬨𐬀 ( upama ) , 𐬎𐬞𐬆𐬨𐬀 ( upəma , “ uppermost; highest ” ) 
 Proto-Italic: *supemos 
 Latin: summus 
 Descendants
 [ edit ] 
 Proto-Celtic: *uɸo 
 Old Irish: fo , fu , fú Irish: faoi , fá ( Ulster ) , fé ( Munster ) , fó ( dialectal ) 
 Manx: fo 
 Scottish Gaelic: fo 
 Proto-Germanic: *ub ( see there for further descendants )
 Proto-Hellenic: 
 Ancient Greek: ῠ̔πό ( hŭpó ) 
 Proto-Indo-Iranian: *úpa , *upa- 
 Proto-Indo-Aryan: *úpa , *upa- 
 Sanskrit: उप॑ ( úpa ) , उप- ( upa- ) 
 Hindi: उप- ( up- ) 
 Proto-Italic: *supo ( see there for further descendants )
 Tocharian B: spe 
 References
 [ edit ] 
 ^ Kloekhorst, Alwin ( 2008 ), Etymological Dictionary of the Hittite Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 5), Leiden, Boston: Brill, →ISBN , page 920 
 ↑ 2.0 2.1 Dunkel, George E. ( 2014 ), “*úp 'oben', *úpo 'hinauf'”, in Lexikon der indogermanischen Partikeln und Pronominalstämme [ Lexicon of Indo-European Particles and Pronominal Stems ]‎ [1] (in 
 ↑ 3.0 3.1 Matasović, Ranko ( 2009 ), “*owxsos”, in Etymological Dictionary of Proto-Celtic (Leiden Indo-European Etymological Dictionary Series; 9), Leiden: Brill , →ISBN , pages 303–304 
 ^ Dunkel, George E. ( 2014 ), “*súp 'unten', *súpo 'hinab'”, in Lexikon der indogermanischen Partikeln und Pronominalstämme [ Lexicon of Indo-European Particles and Pronominal Stems ]‎ [2] (in German
 ^ Hackstein, Olav ( 2023 ), “ When words coalesce II: Preverb incorporation in Indo-European ”, in Indo-European Linguistics , volume 11 , number 1, →DOI , →ISSN , page 28-30 of 1–40 
 Further reading
 [ edit ] 
 Fortson, Benjamin W. ( 2004 ), Indo-European Language and Culture: An Introduction , first edition, Oxford: Blackwell 
 De Vaan, Michiel ( 2008 ), Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN 
 Pokorny, Julius ( 1959 ), Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 3, Bern, München: Francke Verlag, page 1105 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/upó&oldid=92151842 "
 Categories : Proto-Indo-European terms suffixed with *-o 
 Proto-Indo-European lemmas 
 Proto-Indo-European adverbs 
 Hidden categories: Pages with etymon 
 Proto-Indo-European entries with etymon
```


## [2026-10-16T05:18:08.930Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^ *upo\\b\\|^upo,\\|^upo ' incoming/WLD/WLD_Bd1_pages.txt | head -5; grep -n '^upo\\|^ūpo\\|^upo-' IEC.txt | head -5; grep -n -i '\\bup\\b.*\\bupo\\|UP, UPWARD' SYN.txt | head -3"
}
```


## [2026-10-16T05:18:10.025Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'upo' incoming/WLD/WLD_Bd1_pages.txt | head -8; grep -n -i 'upo\\b' IEC.txt | head -8"
}
```


### [2026-10-16T05:18:10.365Z] TOOL RESULT

```
2264:Sippe von               air.    os,     ttas   „oben, iiber“   (a. u.   upo).
4020:=   idg. *ato (vgl. zum Ausgang *apo, *upo ) spricht:
5290:arkad. evopupog „evo/j,os“ verwandt sei, ist ganz fraglich <p aus gh - - suf-      j
7525:schimmernd“ ( *aoyeo-vog) vielleieht auch in agyeupov rgg Beiwort dea Hermes
17486:                 s. v.); [eher zu  upo (S. 193) air. (nur als Praefix: b-, u- (mit
17669:192                                                         nper(i)       — upo
17671:     hinaus“, uperos „der obere“; verwandt mit upo s. d., s. Bgm. II 2 2.
17687:super (zum s- s. u. upo) Praeverb „fiber, drfiber** und Praep. „fiber, fiber                                                                   —
645:apo (apo, apo, po) “away; from, after", WP L 47. See next Skt. ápa; Av. apa; Oss. fá-, px.; Tokh. -àp, suffix; Arm. v-, px.; Hitt. appa 'afterwards; again, back"); -apa (suff. ‘so, then" queried); Myc. apu; Gk. apó; Alb. pa ‘without’; f-, px.; Lat. ab (perhaps also as a fused px. in Lat. p-arco, p-av6o, paro, pudeo, pando, etc.); Ir. fo-, px.; OBr. W o; Bret. (WSP) a; Cor. a; Go. af; OHG aba “away; from’, abo "but: OE of; ON af; OCS po ('after. In sense of "about see upo); Srb. pa (fr. *po “and, then, so’: Hitt. -apa); Li. po (WSP in sense of 'after); cf. apa-6ià ((bottom?. See apetios above); Latv. cf. apa-k3 “below? apo-, px. *not-, un-'. See apo above Skt. cf. ápa-bhis ‘fearless’; Gk. apó-thrix ‘hair- less"; Alb. pa, pa- ‘without; un-'; Go. af-guds ‘godless’
896:auodios, à, om (oauod-, uod-) “voice, song”. Cf. aued- Skt. vadyam 'speech'; Oss. wadz 'prayer'; Per. avaz "voice: Arm. (?) cf. -awn (in gey-awn *ode?); Gk. aoidé; MIr. Ad ‘poem’; W awd ‘song, lay? indicates a prototype *auti-. Of uncertain origin is Latv. paudas, f.pl. ((ru- mour’, fr. *apo-/upo- ?(?))
2058:daló, ið ‘divide’. Cf. dalis Skt. dalàmi, pp. dalitah, intr. ‘burst’; Ir. fo- dailim (*upo- ?); MHG zeln; Sw. tälja, etc: Alb. cf. (a-st. denom.) dalloj ‘distinguish’
2278:diKos, iom, à ‘manifestation’. Cf. deik-, diK- etc. WP I, 776 Skt. dis, disa; Av. disyəm ‘teaching’; Gk. díkë ‘custom, right’; W cf. go-ddeg Cutter: ance’, fr. *upo- ?); MHG zic, gs ziges (oxy- tonic: *diKós «accusation"); ON tigi, n. id.
2424:dotis (dotis), io ‘giving, gift. Cf. do-, dí- dómi, etc. Skt. cf. (redup.) dadatib; Av. daitis; Per. dad “gift, justice’; Arm. cf. -tu (in sdon-tu ‘nurse’; dzern-tu “helpful, cf. 8her-); Myc. dos-; Gk. dós beside dósis; Lat. dos, gs dotis; Venet. cf. doóto; W dawd, pl. dodion; OCS dati be- side dašta; Srb. daća ‘tax; fertility; prosper- ity’; Cz. na-dace ‘charitable foundation’; Latv. cf. pa-dots (‘subordinate’, adj. fr. *upo- °); Li. duotis, ies ‘gift
2594:durduró, ið (durdər-) “hum, drone, mutter, grunt, rumble’ Oss. cf. dírdir ‘fart; Arm. trtram ‘mutter, grumble, grunt? beside trtngem ‘growl’; Hes. cf. dárda ‘bee’; Ir dordaraim beside dórdaim (sic) ‘hum, buzz’; W cf. dwrdd, s. ‘rumble, stir beside go-dyrddio, v. (Crumble, fr. *upo-^?; Slovene drdrati ‘rattle’; Slovak cf. drdlat ‘mutter, hum, buzz’. Substr. or LW in Rum. durdui (thunder, v.)
3558:emo Omg, mö) ‘take, get. Cf. iem-, iom-. WP I, 124 Arm. cf. imanam, aor. imacaj “understand”; (Tokh. cf. ? ime ‘thought: Lat. imago & imitor VWind. LEDT); Lat. emo, ére beside ad-imo (: em! ‘take’; eme! *buy'); cf. auris ima ‘flap of the ear; Umb. emps, for *emptos, pp. ‘taken’; MIr. do-emim ‘protect’; air-imim ‘receive’; fo-emaim, id. (fr. *do-, *pri-, *upo-?); OCS imo, jeti “hold, seize’; emljo, imati ‘take’; OCz. jmám ‘have’; Li. imu, imti, aor. emiau (: Lat. emi) ‘take’; Latv. cf. n-emu, -emt, id. (The apparent reduction in the initial vowel is traditionally regarded as ‘shva se- cundum’, here represented as "Í-. Cf. que- tuores, sked-)
3582:enduio (1) ‘dip, immerse, sink’. Cf. endo and next Arm. nerkem ‘dye’; Gk. endüo (1) “enter”; Alb. ndyj ‘dip; defile’; Lat. induo (2) 'be- smear'; Olr. indaim 'immerse, wash? beside foro-bindim ‘dye’, fr. *upo-pro-. Cf. *en- dumn- in Gk. énduma, Lat. indumen
```


### [2026-10-16T05:18:10.378Z] TOOL RESULT

```
17723:upo etwa ,,unten an etwas heran“; aus der Bed. „von unten hinauf*                                                                              er-
19574:upoto-, upəti- Av. upato, adj. “high, long’; Hitt. upati- (que- ried: *east'); Gk. cf. hüpatos, adj. ‘highest’; Ir. cf. fada “long: faide, s. “length”
19577:upo (upo) ‘upon, on to; down, under, below; at; like; near’. WP I, 192 Skt. úpa, prp. “to, near, in, on’; px. 'up-, at-, near-'; Av. upa, prp. as Skt.; Ober upà, as Skt.; Oss. fá-, px. “like-?, also an intensive px. of verbs; Myc. & Gk. hupó, prp. “under, at’; Osc. úp, Umb. op, prp. ‘under; near’; Gallo-British Vo- (in place-names: Vo-luba, Vo-reda); Olr. fo, Ir. fo & fa, prp. ‘under, amid’; OBr. guo-, px.; W gwo-, go-, px. as Olr. Ir.; also gwa-, in some cpds.; Go. uf, prp. 'under; OHG oba, adv. & prp. “over, above; MHG obe, as OHG; Runic ub, id.; OFris. uva, ova, as OHG; ON of-, px. ( from’, infl. of af, see apo); Ger. cf. Ob- in Ob-mann, -dach; OCS (and com. Sl.) po, prp. w. dat. (about, according to’. Isophonic with type apo, q.v.). As a prefix: ‘somewhat, -ish? in Skt. Gk. Ir. W. OCS. Li. and Latv. (NB. For Lat. pono, ére, positum, see pod-; also in pudeo, ere, if for *pod-uid- “look down" For ponti-fex, cf. pouó ‘make firm', qua *pouonts, pres. pt. “fixing”, etc.). Compound formulae: *upo-bhütis (Skt. Gk. Alt *upo-do (OBr. gud-, Olr. fod-, SI. podü); *upo-ijo-ne (?) (Lat. paene; Blg. poné, cj. “at least"); *-logh- (Ir. Cz. Li.); *-màn- (Skt. Ukr. Blg. Li. Latv.); *-pod- (Skt. Gk. Ir. W. SL); *-sàul- (Gk. Li. Latv.); *-sd- (Arm. Hes.);
19578:upoto-, upoti- — us-
```


## [2026-10-16T05:18:14.600Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'upā\\b\\|upa ' KNT_full.txt | head -5; grep -n '^ *upa  \\|upa  Präp\\|•  upa ' BRT.txt | head -3; grep -n -i 'patiy\\b' KNT_full.txt | head -3"
}
```


### [2026-10-16T05:18:15.196Z] TOOL RESULT

```
8248:upa  I  I  b
19101:upa   va  »a^/  rai>wat  -Aanai  haca  V.  f^^^^tmU  mi%rs  Yt/o.  133-
21768:upa  va  nairikqm  va'hayaSa  (Opt,  zu  c)  _y'  *aß  antarat  nalmSi   %rigamyehe  paili
5455:pli ghu- in ОР patiy-azbayam Ч proclaimed’, 
6971:The ethnic Pátisuvaris (to patiy ?). 
7242:Postpositions: d, patiy; both also as separate
```


## [2026-10-16T05:18:20.450Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'upā \\|upa, \\|^upā\\|upā ' KNT_full.txt | head -8; grep -n -B2 -A3 'Präp.*Postp\\|upa  Präp' BRT.txt | head -12"
}
```


### [2026-10-16T05:18:20.776Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:18:25.253Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'upā\\|upa' KNT_full.txt | grep -v 'upari\\|upast' | head -10; sed -n 8244,8252p BRT.txt | cut -c1-300"
}
```


### [2026-10-16T05:18:25.590Z] TOOL RESULT

```
7139:aríü > Хіауатіа; *upa-àyam > updyam, *fra- 
7722:‘house’, séd- in upa-stá- ‘aid’, zam- ‘earth’ in u- 
7748:^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, 
8489:here. Or names may denote occupations, as per- 
10001:Ending in -ї: apiy (also enclitic), uparty, -diy, 
12386:айй dahydva tyaiy uparty nipištā ‘within these 
18132:60 hamahyáya : Sarda : vašnă : Auramazdàha : akunavam : Auramazdimaiy : upas 
18299:confirming uparty[üyam] of WB, HK, Wb. KIA; Sakaurim 
18341:fupahyahyă Cameron, with і" not absolutely certain and 
23628:upa- + ay- ‘go to, arrive at’: [ulpayam Ist sg. 
pü.:  ä%  (in  Aw.-Buchst.)  rawiinlh,  erl.:  mazg 'Hirn'.
•  J->  S->  P-  UP^  1)  Praea  i)  mit  Akk.; a)  räumlich,  a)  "hin  -  zu':  mi%r)m  yO  .  . fravazaiU  Aaea  karsvar»  yat  arjsaAi  'pa karsvar»  yat  ifaniraitm  Yt  lO.  67;  — "iräyS  °pa  naz'a.paötm  (sd.)  asatUi ..bar^is V.9,11;  Vd.J2;  —  ui'trö  .  .  yS  kapm aipi.spayeiti  spaeit
dby  Google
3S9
upa  I  I  b
upa.paoirya-
390
.,  upa  tarn  srirqm  ifianaahrTm  Ytß.izT, V.jj.  30;  —  lUfiJ  Ais  bardil  °pa  iaüm ti.2i(;  —  iiära*  .  .  /ija*  °pa  mäm  ähJ' Bh.2.6;  ^.6;  —  'pa  %wä  'Vyt.isl?);  — t/m  yazata  AaosyauhS . .  °pa  lair^m  harayh YL  /5.  7 ;  —  yftcit  ahi  .  .  'pa  karivari  .  .
Yt.i2.9-14;  ös)",  20, 21,^  23-37;  —
```


## [2026-10-16T05:18:31.034Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23620,23632p KNT_full.txt"
}
```


### [2026-10-16T05:18:31.343Z] TOOL RESULT

```
6228.11) DB 1.98; 2.67; 3.35, 43. 

à + ay- ‘come’: aya"là 3d pl. imf. mid. ($181, 
$208) DZe 11. 

ali- + ay- ‘go beyond, go along’: aliyäiš imf. 
(872, 8122, 5298.11) DB 3.73. 

upa- + ay- ‘go to, arrive at’: [ulpayam Ist sg. 
imf. (8122, §131, 8226.IT) DB 1.91f. 


169
```


## [2026-10-16T05:20:43.472Z] TOOL CALL #61: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-519.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nPOKr={\"src\":\"POK\",\"where\":\"pp. 1106-1107 s.v. upo (POK_full.txt l.88197)\",\"stance\":\"supports\",\"note\":\"'upo, up, eup, (e)up-s- Meaning: under, from under ... Avestan upa, ap. upa proverb and preposition \\\"toward - to, in, auf\\\"'\"}\nWLDr={\"src\":\"WLD\",\"where\":\"Bd. I pp. 192-193 s.v. upo (WLD_Bd1_pages.txt l.17723)\",\"stance\":\"supports\",\"note\":\"'upo etwa \\\"unten an etwas heran\\\"; aus der Bed. \\\"von unten hinauf\\\"...'\"}\nAHDr={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. upo (AHD_watkins1985.txt l.1106)\",\"stance\":\"supports\",\"note\":\"'upo. Under, up from under, over. 1. Germanic *upp-, up ... 2. Germanic *upanaz ... open ... 6. Variant form *(s)up- in: a. Latin sub, under: SOUTANE, SUB- ... [Pok. upo 1106.]'\"}\nIECr={\"src\":\"IEC\",\"where\":\"s.v. upo (IEC.txt l.19577)\",\"stance\":\"supports\",\"note\":\"'upo (upo) \\\"upon, on to; down, under, below; at; like; near\\\". WP I, 192 Skt. úpa ... Av. upa, prp. as Skt.'\"}\nHUB144={\"src\":\"HUB\",\"where\":\"pp. 12-13, note to Horn no. 144 (HUB.txt l.640-650)\",\"stance\":\"contradicts\",\"note\":\"'...nichts übrig, als np. ba = bad über paz. pa = pad nur auf ap. patiy zurückzuführen ... Erhalten blieb pa in jüngeren Zusammensetzungen [padrud, padid, pinhan, pindastan]' - Hübschmann derives be/ba and the pa- compounds from patiy only, not from upa.\"}\nHUBc={\"src\":\"HUB\",\"where\":\"p. 42-43, notes to Horn nos. 289, 324 (HUB.txt l.1268-1276, 1440-1446)\",\"stance\":\"contradicts\",\"note\":\"'289. Streiche die Worte: \\\"also aw. *upadīti-\\\" ... Das Wort padīd sichtbar ist erst im Mittelpers. componirt aus pa und dīt = \\\"in Sicht\\\" wie padrūd aus pa und drūt'; '324. Np. pagāh ... kann weder = zd. *upakasa- noch = zd. *paitikāsa- gesetzt werden, sondern wird am besten mit Nöldeke als mp. Neubildung aus pa und gāh \\\"Zeit\\\"... gefasst'\"}\nentry={\n\"entry\":0,\"root\":\"Upo\",\"verdict\":\"confirmed\",\n\"modern_form\":\"PIE *upo (*h₁upó) 'under, up from under, over'; s-mobile variant *(s)up- (Latin sub)\",\n\"note\":\"Root, label and gloss correct: Pokorny 1106-1107 upo 'unter, von unten an etwas heran'; AHD/Watkins upo 'under, up from under, over'; Klein s.v. sub- 'I.-E. base *upo-, \\\"from below\\\"'. The Germanic, Latin, French and English branches are sound (only Gmc. *ubilaz 'evil' is contested: Kroonen derives it from *h₂wep- 'treat badly'). The Iranian branch is the weak part: following Horn 1893, Nourai traces Pahlavi pad/pa and NP be, padīd, pasand, padrūd, pagāh, penhān and paškam to Avestan upa-, but Hübschmann (1895) already corrected Horn, and modern scholarship (Nyberg, MacKenzie, Cheung, Wiktionary) derives all of them from OIr. *pati- (OP patiy, MP pad/pa-). Only bāvar (MP wābar < *upa-/upā-vara-, Horn; Wiktionary) is a reasonable upa- case, and even there Nyberg prefers a reduplicated *vā-vara-. Nourai's own note under be ('see Per 3 for a different derivation') points to the *pati- etymology, which is the one modern scholarship accepts.\",\n\"note_fa\":\"ریشهٔ هندواروپایی آغازین *upo «زیر، از زیر به بالا» (پوکورنی ۱۱۰۶، واتکینز) با گونهٔ *(s)up- در لاتین sub درست آمده و شاخه‌های ژرمنی، لاتین، فرانسه و انگلیسی آن پذیرفتنی است. اما شاخهٔ ایرانی جای تردید است: نورایی به پیروی از هرن «به»، «پدید»، «پسند»، «بدرود»، «پگاه»، «پنهان» و «پشکم» را از پیشوند اوستایی upa- می‌گیرد، حال آنکه هوبشمان همان زمان این را رد کرد و پژوهش امروزی (نیبرگ، مکنزی، چونگ، ویکی‌واژه) همهٔ این واژه‌ها را از ایرانی باستان *pati- (پارسی باستان patiy، فارسی میانه pad / pa-) می‌داند. تنها «باور» (فارسی میانه wābar) را می‌توان با احتیاط از upā + var- دانست.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/upo\"],\n\"ref_check\":[\n {\"ref\":\"POK:1106\",\"status\":\"supports\",\"note\":\"POK_full.txt l.88197 'Root / lemma: upo, up, eup, (e)up-s- Meaning: under, from under' ... 'Page(s): 1106-1107'; lists Av. upa, OP upa, Latin sub, Gothic uf/iup, OE up, Gothic ubils.\"},\n {\"ref\":\"KLN:1105\",\"status\":\"supports\",\"note\":\"KLN_1971.txt l.235090 s.v. sub-: 'cogn. with OI. upa ... Gk. hypo ... Goth. iup, ON., OE. upp, \\\"up, upward\\\" ... All these words derive fr. I.-E. base *upo-, \\\"from below\\\"' (1971 edition; 1966 p.1105 is the same entry).\"}],\n\"consulted\":[WLDr,AHDr,IECr],\n\"nodes\":[]}\nN=entry[\"nodes\"]\nN.append({\"id\":1,\"lang\":\"Avestan / Old Persian\",\"words\":\"upa; upâ\",\"verdict\":\"confirmed\",\n\"derivation\":\"PIE *upo > Proto-Indo-Iranian *úpa > Avestan upa (preverb and preposition with acc. 'to, toward', with loc. 'at, in'), Sanskrit úpa. Old Persian has upa- as preverb (upa-ay- 'go to, arrive at') and the lengthened upā 'under, at'. Regular: PIE *o > Indo-Iranian *a; *p unchanged.\",\n\"derivation_fa\":\"پیشوند و حرف اضافهٔ اوستایی upa «به، به سوی» و پارسی باستان upa- / upā از هندوایرانی *úpa و هندواروپایی آغازین *upo است؛ o هندواروپایی در هندوایرانی به a بدل شده است (همانند سنسکریت úpa). بارتولومه و پوکورنی این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/upo\"],\n\"ref_check\":[{\"ref\":\"POK:1106\",\"status\":\"supports\",\"note\":\"'Avestan upa, ap. upa proverb and preposition \\\"toward - to, in, auf (Akk.); by, in (Lok.)\\\"' (POK_full.txt l.88210).\"},\n {\"ref\":\"KLN:1105\",\"status\":\"supports\",\"note\":\"s.v. sub-: 'cogn. with OI. upa, \\\"near, under, up to, on\\\"' (KLN_1971.txt l.235099).\"}],\n\"consulted\":[{\"src\":\"BRT\",\"where\":\"col. 389 s.v. upa (BRT.txt l.8244-8250)\",\"stance\":\"supports\",\"note\":\"'upa 1) Praev. ... mit Akk. a) räumlich \\\"hin - zu\\\"' with Yt. 10.67 etc.\"},\n {\"src\":\"KNT\",\"where\":\"lexicon s.v. ay- (KNT_full.txt l.23628)\",\"stance\":\"supports\",\"note\":\"'upa- + ay- \\\"go to, arrive at\\\": upayam 1st sg. imf. DB 1.91f.'\"},IECr]})\nN.append({\"id\":2,\"lang\":\"Pahlavi\",\"words\":\"pat; pa; pad\",\"verdict\":\"disputed\",\n\"derivation\":\"MP pad (written PWN, Manichaean pd, 'to, at, in, on'), proclitic pa- before consonants, older spelling pat, continues OP patiy / Av. paiti, OIr. *pati (PIE *proti/*preti), not upa. Hübschmann (1895) rejected Horn's view (HRN no. 144) that be/pad fuse upa and pati: 'nichts übrig, als ... pad nur auf ap. patiy zurückzuführen'. OP upā survives instead as MP ō 'to, at' (MacKenzie). So the edge upa → pad is wrong in modern scholarship; the chart's own note (HRN 'combination of upa and paiti') is the outdated side.\",\n\"derivation_fa\":\"«پد / پ» فارسی میانه (هزوارش PWN، مانوی pd) به معنای «به، در» از پارسی باستان patiy و اوستایی paiti (ایرانی باستان *pati-) است، نه از upa. هرن آن را آمیزه‌ای از upa و paiti می‌دانست، ولی هوبشمان همان زمان رد کرد و مکنزی و نیبرگ نیز pad را از pati می‌گیرند؛ upā پارسی باستان در فارسی میانه ō «به» شده است. پس این پیوند را پژوهش امروزی رد می‌کند.\",\n\"sources\":[W+\"به\"],\n\"ref_check\":[{\"ref\":\"HRN:33\",\"status\":\"partial\",\"note\":\"HRN p.33 no.144 (HRN.txt leaf 54): 'be, bed (vor Vokalen), Praeposition \\\"zu, bei, mit, an, auf\\\". ap. patiy bezw. upā; aw. paiti bezw. upa; phlv. pat ... In der Form be sind die beiden Praepositionen upa und (irregulär) pati zusammengefallen' - Horn indeed says what Nourai's note reports, but derives the form mainly with pati.\"},\n {\"ref\":\"AEF:190,191\",\"status\":\"not_checked\",\"note\":\"Khaleqi Motlaq's Persian translation of Horn is not online or on disk.\"}],\n\"consulted\":[{\"src\":\"PHD\",\"where\":\"s.v. pad, ō (PHD_mackenzie.txt l.3895, 3832)\",\"stance\":\"contradicts\",\"note\":\"'pad [PWN, for pty | M pd, N ba] to, at, in, on'; 'ō [OL < A ʿl; ʾw | M ʾw] to, at' - upa/upā continues as ō, not pad.\"},\n {\"src\":\"NYB\",\"where\":\"vol. II glossary, index pad → pat (NYB_vol2_glossary.txt l.6769)\",\"stance\":\"silent\",\"note\":\"Nyberg lists 'pad: pat' in the Pazand/NP index; no upa etymology.\"},HUB144]})\nN.append({\"id\":3,\"lang\":\"Persian\",\"words\":\"beh\",\"verdict\":\"confirmed\",\n\"derivation\":\"NP be / ba (به) 'to, toward' < MP pad (before vowels) / pa (before consonants), with irregular initial p > b in this unstressed proclitic (Hübschmann: 'gegen die Regel'). The edge pad → be is correct. Ultimately from OP patiy (Wiktionary, Hübschmann, MacKenzie), which is exactly the 'Per 3' derivation Nourai's note refers to; that side is the one modern scholarship accepts.\",\n\"derivation_fa\":\"حرف اضافهٔ «بِه / بَه» در فارسی نو از فارسی میانهٔ pad (پیش از واکه) و pa (پیش از همخوان) است و p آغازی در این واژهٔ بی‌تکیه به ب بدل شده است. این گام درست است، ولی ریشهٔ دورتر آن پارسی باستان patiy است (همان که نورایی در «Per 3» آورده) و نه upa.\",\n\"sources\":[W+\"به\"],\n\"ref_check\":[{\"ref\":\"MON:605\",\"status\":\"not_checked\",\"note\":\"6-vol. Mo'in page numbers cannot be mapped; the 2-vol OCR (MON_part1.txt) gives no etymology for be.\"},\n {\"ref\":\"AEF:190,191\",\"status\":\"not_checked\",\"note\":\"not online or on disk.\"}],\n\"consulted\":[{\"src\":\"HRN\",\"where\":\"p.33 no.144\",\"stance\":\"partial\",\"note\":\"'be, bed ... ap. patiy bezw. upā; aw. paiti bezw. upa; phlv. pat ... päz. pa' - MP pat/pa → NP be agreed.\"},HUB144,\n {\"src\":\"PHD\",\"where\":\"s.v. pad\",\"stance\":\"supports\",\"note\":\"'pad [PWN ... M pd, N ba] to, at, in, on' - gives NP ba as the reflex.\"}]})\nN.append({\"id\":4,\"lang\":\"Avestan\",\"words\":\"upa-diti; upa-sad; upa-var; upa-drava; upa-gâh; upa-ni-dâ\",\"verdict\":\"disputed\",\n\"derivation\":\"These are Horn's (1893) reconstructed 'Avestan' prototypes, mostly unattested: upa-dīti (Horn no.289 'also aw. upa.dīti-', struck out by Hübschmann), upa-sad (Horn no.319 '*upa + sand-'), upa-gāh (Horn no.324), upa-drava and upa-ni-dā are not Avestan words but back-projections of NP padrūd, penhān. Modern scholarship derives the NP words from MP compounds with pad/pa- (< *pati-): pa + dīd, *pati-sand-, pa + drōd, pa + gāh, pa + nihān. Only upa-var (Av. var- 'choose, believe' with upa/upā) is a defensible prototype (for bāvar). The node therefore does not stand as drawn.\",\n\"derivation_fa\":\"این صورت‌ها بیشتر ساختهٔ هرن‌اند و در اوستا گواهی نشده‌اند: upa-dīti را خود هوبشمان خط زد؛ upa-drava و upa-ni-dā بازسازی از روی «پدرود» و «پنهان» است. پژوهش امروزی این واژه‌ها را ترکیب‌های فارسی میانه با pad / pa- (از *pati-) می‌داند. تنها upa-var (برای «باور») پذیرفتنی است؛ بنابراین این گره به صورتی که کشیده شده درست نیست.\",\n\"sources\":[W+\"پسند\",W+\"باور\"],\n\"ref_check\":[{\"ref\":\"HRN:41,65,71,72,73\",\"status\":\"supports\",\"note\":\"Horn gives exactly these: p.41 no.178 'bāver \\\"Glaube\\\". Zu √var- \\\"glauben\\\" mit upā'; p.65 no.289 'pedīd \\\"sichtbar\\\". phlv. pa dīt ... also aw. upa.dīti-'; p.71 no.319 'pesend ... ap. *upa + √sand-'; p.72 no.324 'pegāh ... aw. upa + gāh'; p.73 no.332 'penhān ... phlv. pa nihān' - Nourai follows Horn faithfully (Horn himself gives pa nihān for penhān).\"}],\n\"consulted\":[HUBc,\n {\"src\":\"NYB\",\"where\":\"vol. II glossary s.v. dīt, passand (NYB_vol2_glossary.txt l.1293, 2990)\",\"stance\":\"contradicts\",\"note\":\"'dit ... pat dit visibly ... NP padid'; 'Paz. NP pasand; < *pat-sand-'.\"},\n {\"src\":\"BRT\",\"where\":\"grep upa.dīti / upa.gāh\",\"stance\":\"silent\",\"note\":\"no such Avestan compounds in Bartholomae (only upa.skambəm, upa.suxta- etc.).\"}]})\nN.append({\"id\":5,\"lang\":\"Persian\",\"words\":\"padîd; pasand; bâvar; bedrŭd; pegâh; penhân\",\"verdict\":\"disputed\",\n\"derivation\":\"padīd 'visible' < MP pad dīd 'in sight' (Nyberg; Hübschmann: 'erst im Mittelpers. componirt aus pa und dīt'), not Av. *upa-dīti. pasand 'liking' < MP passand < *pati-sand- (Wiktionary, Nyberg, MacKenzie; Cheung's *sand 'seem'). bāvar 'belief' < MP wābar < upā + var- 'choose/believe' (Horn, Wiktionary) - plausible, though Nyberg prefers reduplicated *vā-vara-. bedrūd/padrūd 'farewell' < pa + drōd 'health' (MP drōd < *druvatāt-), Wiktionary 'be + dorud'. pegāh 'early morning' < pa + gāh 'time' ('betimes', Hübschmann/Nöldeke; Mo'in '= بگاه، بهنگام'). penhān 'hidden' < MP pad + nihān (Wiktionary; Horn himself 'phlv. pa nihān'). Five of six words therefore come from *pati-, not upa; worst verdict disputed.\",\n\"derivation_fa\":\"«پدید» از فارسی میانهٔ pad dīd «در دید» است؛ «پسند» از passand و ایرانی باستان *pati-sand-؛ «بدرود / پدرود» از pa + drōd «تندرستی»؛ «پگاه» از pa + gāh «به‌گاه، بهنگام»؛ و «پنهان» از pad + nihān. پس پیشوند همهٔ این‌ها pa- (از *pati-) است نه upa. تنها «باور» (فارسی میانه wābar) را می‌توان با هرن و ویکی‌واژه از upā + var- «برگزیدن، باور داشتن» دانست، هرچند نیبرگ صورت دوتایی *vā-vara- را ترجیح می‌دهد. هوبشمان همان زمان سخن هرن را درباره «پدید» و «پگاه» رد کرده بود.\",\n\"sources\":[W+\"پدید\",W+\"پسند\",W+\"باور\",W+\"بدرود\",W+\"پنهان\",W+\"پگاه\"],\n\"ref_check\":[{\"ref\":\"BQT:373\",\"status\":\"partial\",\"note\":\"BQT_v1_pages.txt leaf 597 (≈p.373) s.v. پدید: Mo'in's footnote 'پهلوی ... کارنامه ... اوستا ... نیبرگ پهلوی آنرا ... نوشته ... آشکار' - gives the Pahlavi pad-dīd form; OCR rough.\"},\n {\"ref\":\"BQT:406\",\"status\":\"not_found\",\"note\":\"leaf ≈632 not clearly matched; پگاه appears as 'بگه ... مخفف بگاه است که سحر و صبح باشد' at leaf 640 (≈p.414), i.e. be-gāh.\"},\n {\"ref\":\"BQT:2230\",\"status\":\"not_found\",\"note\":\"ref_page.py BQT:2230 (vol.4 pdf 313) shows نیک / نیکو entries; نهان is at pdf 296-297 (≈p.2213-2214).\"}],\n\"consulted\":[HUBc,\n {\"src\":\"NYB\",\"where\":\"vol. II s.v. dīt, passand, vāvarīkānēh (l.1293, 2990, 3938)\",\"stance\":\"contradicts\",\"note\":\"'NP padid'; 'NP pasand; < *pat-sand-'; for vāvar: '*vā-vara- \\\"choice\\\" ... from Av. var-, pres. vāvar-'.\"},\n {\"src\":\"PHD\",\"where\":\"s.v. passand, paydāg, nihān, drōd (l.4087, 4135, 3762, 2066)\",\"stance\":\"partial\",\"note\":\"'passand [psnd | N pasand] pleasure, liking'; 'nihān [nyhʾn] concealment, secrecy'; 'drōd ... health, well-being' - components of pa-compounds; no upa.\"},\n {\"src\":\"MON\",\"where\":\"2-vol. Mo'in (MON_part1.txt l.32365, 21615)\",\"stance\":\"supports\",\"note\":\"'پگاه ... [= بگاه، بهنگام] صبح' and 'بدرود [= پدرود] سلامت' - support pa/be + gāh, be + drūd.\"},\n {\"src\":\"HRN\",\"where\":\"pp.41,65,71-73\",\"stance\":\"partial\",\"note\":\"Horn's upa-derivations (see ref_check); for penhān he himself gives 'phlv. pa nihān'.\"}]})\nN.append({\"id\":6,\"lang\":\"Avestan\",\"words\":\"upa-skambem\",\"verdict\":\"plausible\",\n\"derivation\":\"Avestan upa.skambəm is real (Vd. 8.10), an absolutive of skamb- 'to support, prop' with upa: 'unter Festmachen' (fastening underneath, propping up), from PIE *skabʰ-/*skamb- (Pokorny 916; Sanskrit skambha- 'pillar'). The word exists, but it is a verbal absolutive, not a noun 'column or pillar'; the related nouns are Av. fraskəmba- 'girder, pillar', Skt. skambha-.\",\n\"derivation_fa\":\"اوستایی upa.skambəm (وندیداد ۸٫۱۰) گواهی شده و صورت مصدری (absolutive) از ستاک skamb- «پشتیبانی کردن، ستون زدن» با پیشوند upa است، به معنای «از زیر استوار کردن» (بارتولومه). ریشه درست است، ولی این واژه اسم «ستون» نیست؛ اسم آن fraskəmba- «تیرک، ستون» است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n\"sources\":[],\n\"ref_check\":[{\"ref\":\"POK:916\",\"status\":\"supports\",\"note\":\"POK_full.txt Page(s) 915-916 s.v. skabh-, skambh- 'to support': 'Old Indic skabhnāti ... skambha-m \\\"prop, pillar\\\", Avestan upa.skambəm \\\"under fastening, strengthening\\\", fraskamba- \\\"girders, pillars\\\"'.\"}],\n\"consulted\":[{\"src\":\"BRT\",\"where\":\"col. ~390 s.v. upa.skambəm (BRT.txt l.8370)\",\"stance\":\"supports\",\"note\":\"'upa.skambəm Absol. \\\"unter Fest-machen\\\" ... indem sie ihn (den Leichnam) an Lehmziegeln oder Steinen festmachen' V.8.10.\"},\n {\"src\":\"CHEUNG\",\"where\":\"p.344 *skamb (CHEUNG.txt l.22503-22521)\",\"stance\":\"partial\",\"note\":\"'*skamb \\\"to support, use as support\\\"' - lists YAv. frascinb-, not upa.skamba-; NP paskam under (+ *pati-).\"}]})\nN.append({\"id\":7,\"lang\":\"Persian\",\"words\":\"pečkam\",\"verdict\":\"disputed\",\n\"derivation\":\"NP paškam / baškam / bačkam / pačkam 'summer-house, porch, portico, room open on all sides' (Borhan; Asadi's Loghat-e Fors quotes Rudaki for بچکم). The root *skamb 'prop' is right (Pokorny 916 lists 'npers. paskam ... porch, portico'), but the prefix is *pati-, not upa: Hübschmann derives paškam = Arm. patškamb (loan) from OP *pati-skamba-, with *patskamb > *paskamb in MP; Cheung likewise lists 'NP paskam \\\"court, vestibule\\\"' under *skamb (+ *pati-), with Manichaean MP pdyskmbʾn 'rooms' and Sogdian ptsknpy 'porch'. The forms with č (pačkam, bačkam) are later variants of paškam. So Av. upa.skambəm is a cognate formation, not the ancestor.\",\n\"derivation_fa\":\"«پشکم / بشکم / بچکم / پچکم» به معنای «خانهٔ تابستانی، ایوان، بارگاه» (برهان قاطع، لغت فرس با شاهد رودکی) به ریشهٔ skamb- «ستون زدن، پشتیبانی» برمی‌گردد و پوکورنی نیز آن را آورده است. اما پیشوند آن *pati- است نه upa: هوبشمان آن را از پارسی باستان *pati-skamba- (ارمنی patškamb وام‌واژهٔ ایرانی) می‌داند و چونگ نیز همین را با فارسی میانهٔ مانوی pdyskmbʾn و سغدی ptsknpy آورده است. پس ریشه درست، ولی پیوند مستقیم با upa.skambəm اوستایی را پژوهش امروزی نمی‌پذیرد.\",\n\"sources\":[\"https://vajehyab.com/?q=پشکم&d=moein\"],\n\"ref_check\":[{\"ref\":\"POK:916\",\"status\":\"partial\",\"note\":\"'npers. paskam \\\"a covered walk between columns, colonnade, piazza, arcade, gallery, porch, portico\\\"' listed beside Avestan upa.skambəm, without stating the prefix.\"},\n {\"ref\":\"BQT:410\",\"status\":\"supports\",\"note\":\"BQT_v1_pages.txt leaf 636 (≈p.410): 'پشکم - بکسر اول بر وزن اشکم، ایوان و بارگاه را گویند' (meaning only; OCR shows no etymological footnote).\"},\n {\"ref\":\"MON:798\",\"status\":\"supports\",\"note\":\"vajehyab (Mo'in): 'پشکم (پِ کَ) (اِ.) ایوان و بارگاه'; MON_part1.txt l.29451 'پشکم (اِ.) خانه‌ای که از همه سوی در و ...' - meaning confirmed, no etymology.\"},\n {\"ref\":\"FRS:183\",\"status\":\"supports\",\"note\":\"FRS_pages.txt l.14438: 'پچکم ... خانه تابستانی ... بچکم ... خانهٔ تابستانی' (different edition; page not mapped).\"}],\n\"consulted\":[{\"src\":\"HUB\",\"where\":\"p.41 no.315 & p.191 (HUB.txt l.1390-1398, 9171)\",\"stance\":\"contradicts\",\"note\":\"'np. paškam (piškam, baškam, biškam) \\\"domus aestiva, aula, atrium, porticus\\\" = arm. patškam (patskamb) ... auf ap. *pati-skamba- ... zurück. Im Mittelpersischen wurde *patskamb zu *paskamb'.\"},\n {\"src\":\"CHEUNG\",\"where\":\"p.344 *skamb (l.22521)\",\"stance\":\"contradicts\",\"note\":\"'(+ *pati-) NP paskam \\\"court, vestibule\\\", Yzd. (Zor.) paskam \\\"portico\\\"'; 'MMP *pdyskmbʾn \\\"rooms\\\"'; 'BSogd. ptsknpy \\\"porch, eaves\\\"'.\"},\n {\"src\":\"BQT\",\"where\":\"vol.1 leaf 457 s.v. بچکم\",\"stance\":\"supports\",\"note\":\"'بچکم - بفتح اول و کاف بروزن شبنم، خانه‌ای که اطراف آن را شبکه کرده باشند - و ایوان و صفه و بارگاه را نیز گویند' (meaning).\"}]})\nN.append({\"id\":8,\"lang\":\"Germanic\",\"words\":\"upp; upanaz; ubilaz\",\"verdict\":\"plausible\",\n\"derivation\":\"Proto-Germanic *upp / *ūp 'up' (with expressive gemination) and *upanaz 'open' (lit. 'put up, raised', adj. in *-ana-) both continue PIE *upo (AHD; Wiktionary 'open ... from Proto-Germanic *upanaz, from PIE *upo'). *ubilaz 'evil' (Gothic ubils, OE yfel) is assigned to *upo by Pokorny ('upelo- in Gothic ubils') and Klein ('prob. rel. to up, above, over ... going beyond, transgressing'), but Kroonen (2013) and Wiktionary derive it from *h₂up(h₁)élos, a derivative of *h₂wep- 'treat badly', and AHD (Watkins) puts EVIL under wap-. upp and upanaz confirmed; ubilaz disputed between two views.\",\n\"derivation_fa\":\"ژرمنی آغازین *upp «بالا» و *upanaz «باز» (در اصل «بالا برده») هر دو از *upo هستند و منابع (واتکینز، کلاین، ویکی‌واژه) همداستان‌اند. اما *ubilaz «بد، شرّ» را پوکورنی و کلاین از *upo «فراتر رفتن از حد» می‌گیرند، در حالی که کروونن و واتکینز آن را از ریشهٔ دیگر *h₂wep- «بدرفتاری کردن» می‌دانند. پس دو واژهٔ نخست درست و سومی محل اختلاف است.\",\n\"sources\":[W+\"up\",W+\"open\",W+\"evil\"],\n\"ref_check\":[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"AHD_watkins1985.txt l.1106: 'Germanic *upp-, up ... Germanic *upanaz, \\\"put or set up\\\", open' under upo; but index 'EVIL wap-' (wep-) - Watkins does not put evil under upo.\"}],\n\"consulted\":[POKr,\n {\"src\":\"KLN\",\"where\":\"s.v. evil, open (KLN_1971.txt l.87113, 167476)\",\"stance\":\"supports\",\"note\":\"evil: 'Goth. ubils ... prob. rel. to up, above, over ... orig. meaning ... going upward, hence going beyond, transgressing'; open: 'OHG offan ... prob. also to E. up'.\"},\n {\"src\":\"WLD\",\"where\":\"Bd. I 192-193\",\"stance\":\"supports\",\"note\":\"upo entry, Germanic up/uf forms.\"}]})\nN.append({\"id\":9,\"lang\":\"English\",\"words\":\"up; open; evil\",\"verdict\":\"plausible\",\n\"derivation\":\"up < OE up, upp < Gmc *upp; open < OE open (adj.), openian (v.) < Gmc *upanaz; evil < ME yvel, evel < OE yfel < Gmc *ubilaz (OE y by i-umlaut of u before -il-). The OE → English steps are uncontroversial; evil's ultimate link to *upo is contested (see #8).\",\n\"derivation_fa\":\"انگلیسی up از انگلیسی کهن upp، و open از انگلیسی کهن open / openian است که هر دو به *upo برمی‌گردند. evil از انگلیسی کهن yfel (ژرمنی *ubilaz) است و پیوند آن با *upo میان پژوهشگران اختلافی است؛ پس این گره با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"up\",W+\"open\",W+\"evil\"],\n\"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference cited by Nourai for this node.\"}],\n\"consulted\":[{\"src\":\"KLN\",\"where\":\"s.v. evil, open\",\"stance\":\"supports\",\"note\":\"'evil, adj. — ME. evil, evel, ivel, uvel, fr. OE. yfel'; 'open, adj. — ME., fr. OE., rel. to OS. opan, ON. opinn'.\"},\n {\"src\":\"AHD\",\"where\":\"upo 1-2; index EVIL wap-\",\"stance\":\"partial\",\"note\":\"up and open under upo; evil under wap-.\"}]})\nN.append({\"id\":10,\"lang\":\"Latin\",\"words\":\"s-up\",\"verdict\":\"confirmed\",\n\"derivation\":\"Latin sub 'under, below; up to' < *sup (s-mobile variant *(s)up-o of *upo), cf. Oscan sup, Umbrian su-; also subs-/sus- (sustineō), summus < *sup-mos, supīnus. Pokorny explains the s- as from *(e)ks- ('sub (s- from *eks-, compare gr. ex-upertheń)'); Dunkel and de Vaan treat *súp(o) as the s-mobile variant. The gloss 'to below, under' is right.\",\n\"derivation_fa\":\"لاتین sub «زیر، تا زیر» از *sup، گونهٔ s-دار *(s)up-o است (هم‌ریشه با اسکی sup، اومبری su-، و لاتین summus از *sup-mos). خاستگاه s را پوکورنی از *eks- و دیگران s متحرک (s-mobile) می‌دانند. ادعای نورایی درست است.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/upo\"],\n\"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"'6. Variant form *(s)up- in: a. Latin sub, under: SOUTANE, SUB-; b. Latin supinus' (AHD_watkins1985.txt l.1108).\"}],\n\"consulted\":[POKr,{\"src\":\"KLN\",\"where\":\"s.v. sub- (KLN_1971.txt l.235090)\",\"stance\":\"supports\",\"note\":\"'L. sub-, etc., fr. sub (for *sup), \\\"under, below, beneath\\\", rel. to Oscan sup, Umbr. su'.\"},WLDr]})\nN.append({\"id\":11,\"lang\":\"French\",\"words\":\"sujet; sublime'\",\"verdict\":\"confirmed\",\n\"derivation\":\"French sujet < Old French suget, subget < Latin subiectus/subiectum 'placed under' (sub + iacere 'throw'); OF suget is inherited, modern spelling re-Latinized. 'sublime'' = French sublimé 'sublimated', in chemistry the mercury salt (sublimé corrosif), pp. of sublimer < Latin sublimāre 'raise', from sublīmis 'lofty' (sub + līmen 'lintel' per Klein, or sub + līmus 'oblique').\",\n\"derivation_fa\":\"فرانسوی sujet از فرانسوی کهن suget و لاتین subiectum «زیر نهاده» (sub + iacere «انداختن») است؛ sublimé (اسم مفعول sublimer «تصعید کردن»، در شیمی نمک جیوه) از لاتین sublimāre و sublīmis «بلند» است. ادعای نورایی درست است.\",\n\"sources\":[W+\"sujet\"],\n\"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference cited by Nourai for this node.\"}],\n\"consulted\":[{\"src\":\"KLN\",\"where\":\"s.v. subject, sublime (KLN_1971.txt l.235268, 235360, 235369)\",\"stance\":\"supports\",\"note\":\"'subject, adj. — ME. suget, subget, fr. OF. suget, subject (F. sujet), fr. L. subjectus'; 'sublime, tr. and intr. v. — ME. sublimen, fr. MF. (= F.) sublimer, fr. L. sublimāre'.\"},\n {\"src\":\"AHD\",\"where\":\"index SUBJECT yē-; SUB- upo\",\"stance\":\"supports\",\"note\":\"'SUB- upo ... SUBJECT yē-' - prefix from upo.\"}]})\nN.append({\"id\":12,\"lang\":\"Persian\",\"words\":\"\",\"verdict\":\"confirmed\",\n\"derivation\":\"Persian سوژه suže 'subject, topic' is a 20th-century loan from French sujet (Mo'in '[فر.] موضوع'; Wiktionary 'Borrowed from French sujet'); سوبلیمه (the book prints سوبلمه) 'sublimate, mercuric chloride' is a pharmacy/chemistry loan from French sublimé. Both entered Persian via French in the Qajar-Pahlavi period.\",\n\"derivation_fa\":\"«سوژه» (suže) به معنای «موضوع» وام‌واژه‌ای از فرانسوی sujet است (فرهنگ معین: [فر.]) و «سوبلیمه» (در کتاب «سوبلمه») به معنای «سوبلیمهٔ جیوه، کلرید جیوه» از فرانسوی sublimé در داروسازی و شیمی گرفته شده است. هر دو در دورهٔ قاجار و پهلوی از راه فرانسه به فارسی آمده‌اند؛ ادعای نورایی درست است.\",\n\"sources\":[W+\"سوژه\",\"https://vajehyab.com/?q=سوژه&d=moein\"],\n\"ref_check\":[{\"ref\":\"MON:1944,1952\",\"status\":\"supports\",\"note\":\"vajehyab Mo'in: 'سوژه (ژِ) [فر.] (اِ.) موضوع، آن چه که دربارهٔ آن بحث یا آزمایش کنند' (page numbers of the 6-vol. edition not mappable); سوبلیمه not returned by vajehyab.\"}],\n\"consulted\":[{\"src\":\"MON\",\"where\":\"vajehyab (Mo'in)\",\"stance\":\"supports\",\"note\":\"'[فر.]' tag on سوژه.\"},\n {\"src\":\"KLN\",\"where\":\"s.v. subject\",\"stance\":\"supports\",\"note\":\"'(F. sujet), fr. L. subjectus' - the French source of the loan.\"}]})\nN.append({\"id\":13,\"lang\":\"English\",\"words\":\"sub-; subject; sublime; submarine\",\"verdict\":\"confirmed\",\n\"derivation\":\"English sub- is the Latin prefix sub 'under'; subject < ME suget, subget < OF suget < L subiectus; sublime < MF sublime < L sublīmis 'lofty'; submarine is a modern English formation sub- + marine (adj. 1640s, noun 'U-boat' 1899). All rest on Latin sub < *(s)up-o.\",\n\"derivation_fa\":\"پیشوند انگلیسی sub- همان لاتین sub «زیر» است؛ subject از فرانسوی کهن suget و لاتین subiectus، sublime از لاتین sublīmis «بلند»، و submarine ساختهٔ انگلیسی از sub- + marine است. همه به لاتین sub و ریشهٔ *(s)up-o برمی‌گردند؛ ادعای نورایی درست است.\",\n\"sources\":[W+\"sujet\"],\n\"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"index 'SUB- upo', 'SUBTERFUGE bheug-, upo', 'SUPINE upo' (AHD_watkins1985.txt l.2323-2327).\"}],\n\"consulted\":[{\"src\":\"KLN\",\"where\":\"s.v. sub-, subject, sublime, submarine (KLN_1971.txt l.235090, 235268, 235360, 235393)\",\"stance\":\"supports\",\"note\":\"'sub-, pref. of Latin origin meaning \\\"under\\\"'; 'submarine, adj. ... Formed fr. sub- and marine, adj.'; 'sublime ... fr. L. sublimis ... fr. sub (see sub-) and limen'.\"},\n {\"src\":\"POK\",\"where\":\"p.1106\",\"stance\":\"supports\",\"note\":\"'Latin sub ... proverb and preposition \\\"under an etwas heran, under etwas\\\"'.\"}]})\nout={\"pdf_page\":519,\"book_page\":489,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":[entry]}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-519.json\",\"w\",encoding=\"utf-8\"),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-519.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-519.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 519"
}
```


### [2026-10-16T05:20:44.064Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'confirmed': 6, 'disputed': 4, 'plausible': 3}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 10, 'partial': 4, 'not_checked': 5, 'not_found': 2}
books consulted: {'supports': 20, 'contradicts': 9, 'silent': 2, 'partial': 5} | by book: {'KLN': 6, 'HUB': 5, 'BRT': 3, 'PHD': 3, 'NYB': 3, 'POK': 3, 'HRN': 2, 'MON': 2, 'CHEUNG': 2, 'WLD': 2, 'AHD': 2, 'KNT': 1, 'IEC': 1, 'BQT': 1}
```


## [2026-10-16T05:20:54.451Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -i 's/(the book prints سوبلمه)/(spelled سوبلمه in the extracted chart)/; s/(در کتاب «سوبلمه»)/(در متن استخراج‌شده «سوبلمه»)/' data/verification/page-519.json; python3 -m json.tool data/verification/page-519.json >/dev/null && python3 tools/verify_check.py 519 | grep -c PROBLEM"
}
```


### [2026-10-16T05:20:55.006Z] TOOL RESULT

```
0
```


## [2026-10-16T05:21:05.098Z] TOOL CALL #63: SubagentHandback

```json
{
 "message": "Page 519 (book page 489) is done. It has one entry, the root Upo, with 13 nodes. I wrote /home/sfmqrb/git/rishe-private/data/verification/page-519.json, and `verify_check.py 519` shows 0 PROBLEM lines.\n\n**Verdicts:** root confirmed. Nodes: 6 confirmed, 3 plausible, 4 disputed, 0 transcription_suspect.\n\nRef checks: 10 support, 4 partial, 2 not found, 5 not checked (AEF is not available; Mo'in's 6-volume page numbers cannot be mapped).\n\n**Disputed:**\n- **#2, Pahlavi pat/pa/pad:** these come from OP patiy / OIr. *pati, not from upa. Hübschmann (1895) already corrected Horn's \"upa + pati merger\", and MacKenzie's dictionary gives pad < patiy, with OP upā surviving as MP ō. Nourai's own pointer to \"Per 3\" is the side modern scholarship accepts.\n- **#4, the Avestan upa-diti, upa-sad, upa-drava, upa-gâh, upa-ni-dâ:** these are Horn's reconstructions and are not found in Avestan. Hübschmann struck out *upa.dīti. Only upa-var (for bâvar) holds up.\n- **#5, Persian padîd, pasand, bedrûd, pegâh, penhân:** all are pa-/pad- compounds from *pati- (pa + dīd, *pati-sand-, pa + drōd, pa + gāh, pad + nihān), per Hübschmann, Nyberg and Wiktionary. bâvar (from MP wābar) is the exception and is plausible from upā + var-, though Nyberg prefers a doubled form *vā-vara-.\n- **#7, Persian pečkam/paškam \"porch\":** the root *skamb \"to prop\" is right (Pokorny 916), but the prefix is *pati-, not upa. Hübschmann gives OP *pati-skamba-, matching the Armenian loan patškamb, and Cheung lists it under *skamb (+ *pati-).\n\n**Plausible, for reference:** #6, because Av. upa.skambəm is a verb form meaning \"propping underneath\", not a noun \"pillar\". #8 and #9, because Kroonen derives Germanic *ubilaz \"evil\" from *h₂wep- and Watkins files evil under wap-, while Pokorny and Klein keep it under upo.\n\n**Extraction errors:** none found, but I did not look at the printed page because no node was flagged. Node 12's سوبلمه is the extraction's spelling; standard Persian is سوبلیمه, and I did not confirm against the image which one the book prints.\n\n**Refs that did not match:** BQT:2230 is a page of نیک entries (نهان is at about p. 2213), and BQT:406 did not clearly match any headword."
}
```


### [2026-10-16T05:21:05.376Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
