# Verification process log — verify-page-544


## [2026-10-17T00:00:15.343Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 544 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-544.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-544.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-544.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 544` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.400Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.433Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.515Z] TOOL RESULT

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


## [2026-10-17T00:00:18.943Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-544.txt"
}
```


### [2026-10-17T00:00:19.021Z] TOOL RESULT

```
1	=== PDF page 544 (book page 514) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wer 1 : to speak  (refs POK:1162)
4	#1 (parent #0) [Avestan] refs=POK:1162; KLN:1751; SYN:1254 | ver 2 : to decide, command ; verâta, urvata, vrvata, varah, wrvâta ; upa-var : in belief ☞Upo
5	  #2 (parent #1) [Persian] refs=MON:4995; BQT:230 | var «وَر» : tests, such as passing through fire, used to judge the innocence of a defendant ; bâvar «باور» : believing as true | NOTE: See root "Wel 1" for another possible root of "bâvar"
6	#3 (parent #0) [Germanic] refs=AHD | wurdam : word
7	  #4 (parent #3) [English] refs=None | word
8	#5 (parent #0) [Latin] refs=AHD | verbum : word
9	  #6 (parent #5) [English] refs=None | verb, adverb, proverb
10	#7 (parent #0) [Greek] refs=AHD | eirein : to say
11	  #8 (parent #7) [English] refs=None | irony
12	--- entry 1 ---
13	ROOT [Indo-European] Wer 2, Werb, Werg 3, Wermi, Kwermi, Werp, Wert, Wrei : to turn, bend  (refs POK:1142-1157)  PART 1
14	#1 (parent #0) [Avestan / Old Persian] refs=KLN:1703; ISS:223; KNT:207 | varet, wars, vart : to turn ; ni-vart : roll down ☞Nî 1
15	  #2 (parent #1) [Persian] refs=HRN:198,201; BQT:1820,1787; BLY:75 | gardîdan «گردیدن» : to turn ; gardan «گردن» : neck | extra: گردش ، گشتن ۱، گاشتن، گرد ۱، جهانگرد ، گردانیدن ، گردان ، گردون ، گردونه ، گردنه ، گردنکش
16	  #3 (parent #1) [Persian] refs=HRN:198, 201; BQT:1820, 1787 | gerd «گرد ۲» : round ; gerdŭ «گردو» : walnut ; gard «گرد ۳» : dust, makeup powder | extra: گرده
17	  #4 (parent #1) [Persian] refs=HRN:235; BQT:2186 | vardaneh «وَردَنه» : rolling pin ; navardîdan «نوردیدن» : to roll, travel | extra: نورد ، دریانورد ، کوهنورد
18	#5 (parent #0) [Sogdian] refs=SOD:176 | gwrdtq : kidney
19	#6 (parent #0) [Avestan] refs=POK:1157 | verdeka, veredka : kidney | NOTE: because of its round shape
20	  #7 (parent #6) [Pahlavi] refs=MON:3255 | gurtak : kidney
21	    #8 (parent #7) [Persian] refs=MON:3255 | gordeh «گرده» : kidney
22	
```


## [2026-10-17T00:00:19.430Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-544.json"
}
```


### [2026-10-17T00:00:19.627Z] TOOL RESULT

```
1	{
2	  "pdf_page": 544,
3	  "book_page": 514,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wer 1",
8	        "lang": "Indo-European",
9	        "refs": "POK:1162",
10	        "gloss": "to speak"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1162; KLN:1751; SYN:1254",
18	          "words": [
19	            {"translit": "ver 2", "gloss": "to decide, command", "script": null},
20	            {"translit": "verâta, urvata, vrvata, varah, wrvâta", "gloss": null, "script": null},
21	            {"translit": "upa-var", "gloss": "in belief", "script": null, "see": ["Upo"]}
22	          ],
23	          "note": null,
24	          "quote": null
25	        },
26	        {
27	          "id": 2,
28	          "parent": 1,
29	          "lang": "Persian",
30	          "refs": "MON:4995; BQT:230",
31	          "words": [
32	            {"translit": "var", "gloss": "tests, such as passing through fire, used to judge the innocence of a defendant", "script": "وَر"},
33	            {"translit": "bâvar", "gloss": "believing as true", "script": "باور"}
34	          ],
35	          "note": "See root \"Wel 1\" for another possible root of \"bâvar\"",
36	          "quote": null
37	        },
38	        {
39	          "id": 3,
40	          "parent": 0,
41	          "lang": "Germanic",
42	          "refs": "AHD",
43	          "words": [
44	            {"translit": "wurdam", "gloss": "word", "script": null}
45	          ],
46	          "note": null,
47	          "quote": null
48	        },
49	        {
50	          "id": 4,
51	          "parent": 3,
52	          "lang": "English",
53	          "refs": null,
54	          "words": [
55	            {"translit": "word", "gloss": null, "script": null}
56	          ],
57	          "note": null,
58	          "quote": null
59	        },
60	        {
61	          "id": 5,
62	          "parent": 0,
63	          "lang": "Latin",
64	          "refs": "AHD",
65	          "words": [
66	            {"translit": "verbum", "gloss": "word", "script": null}
67	          ],
68	          "note": null,
69	          "quote": null
70	        },
71	        {
72	          "id": 6,
73	          "parent": 5,
74	          "lang": "English",
75	          "refs": null,
76	          "words": [
77	            {"translit": "verb, adverb, proverb", "gloss": null, "script": null}
78	          ],
79	          "note": null,
80	          "quote": null
81	        },
82	        {
83	          "id": 7,
84	          "parent": 0,
85	          "lang": "Greek",
86	          "refs": "AHD",
87	          "words": [
88	            {"translit": "eirein", "gloss": "to say", "script": null}
89	          ],
90	          "note": null,
91	          "quote": null
92	        },
93	        {
94	          "id": 8,
95	          "parent": 7,
96	          "lang": "English",
97	          "refs": null,
98	          "words": [
99	            {"translit": "irony", "gloss": null, "script": null}
100	          ],
101	          "note": null,
102	          "quote": null
103	        }
104	      ]
105	    },
106	    {
107	      "root": {
108	        "name": "Wer 2, Werb, Werg 3, Wermi, Kwermi, Werp, Wert, Wrei",
109	        "lang": "Indo-European",
110	        "refs": "POK:1142-1157",
111	        "gloss": "to turn, bend"
112	      },
113	      "part": 1,
114	      "nodes": [
115	        {
116	          "id": 1,
117	          "parent": 0,
118	          "lang": "Avestan / Old Persian",
119	          "refs": "KLN:1703; ISS:223; KNT:207",
120	          "words": [
121	            {"translit": "varet, wars, vart", "gloss": "to turn", "script": null},
122	            {"translit": "ni-vart", "gloss": "roll down", "script": null, "see": ["Nî 1"]}
123	          ],
124	          "note": null,
125	          "quote": null
126	        },
127	        {
128	          "id": 2,
129	          "parent": 1,
130	          "lang": "Persian",
131	          "refs": "HRN:198,201; BQT:1820,1787; BLY:75",
132	          "words": [
133	            {"translit": "gardîdan", "gloss": "to turn", "script": "گردیدن"},
134	            {"translit": "gardan", "gloss": "neck", "script": "گردن"}
135	          ],
136	          "script_extra": "گردش ، گشتن ۱، گاشتن، گرد ۱، جهانگرد ، گردانیدن ، گردان ، گردون ، گردونه ، گردنه ، گردنکش",
137	          "note": null,
138	          "quote": {"text": "بفرمود تا گاو و گردون برند - سراپرده از شهر بیرون برند", "poet": "Ferdowsî"}
139	        },
140	        {
141	          "id": 3,
142	          "parent": 1,
143	          "lang": "Persian",
144	          "refs": "HRN:198, 201; BQT:1820, 1787",
145	          "words": [
146	            {"translit": "gerd", "gloss": "round", "script": "گرد ۲"},
147	            {"translit": "gerdŭ", "gloss": "walnut", "script": "گردو"},
148	            {"translit": "gard", "gloss": "dust, makeup powder", "script": "گرد ۳"}
149	          ],
150	          "script_extra": "گرده",
151	          "note": null,
152	          "quote": {"text": "زگرده به رخ بر نگارش نبود - جز آرایش کردگارش نبود", "poet": "Ferdowsî"}
153	        },
154	        {
155	          "id": 4,
156	          "parent": 1,
157	          "lang": "Persian",
158	          "refs": "HRN:235; BQT:2186",
159	          "words": [
160	            {"translit": "vardaneh", "gloss": "rolling pin", "script": "وَردَنه"},
161	            {"translit": "navardîdan", "gloss": "to roll, travel", "script": "نوردیدن"}
162	          ],
163	          "script_extra": "نورد ، دریانورد ، کوهنورد",
164	          "note": null,
165	          "quote": {"text": "بر این بارهٔ گامزن برنشین - که زیر تو اندر نوردد زمین", "poet": "Ferdowsî"}
166	        },
167	        {
168	          "id": 5,
169	          "parent": 0,
170	          "lang": "Sogdian",
171	          "refs": "SOD:176",
172	          "words": [
173	            {"translit": "gwrdtq", "gloss": "kidney", "script": null}
174	          ],
175	          "note": null,
176	          "quote": null
177	        },
178	        {
179	          "id": 6,
180	          "parent": 0,
181	          "lang": "Avestan",
182	          "refs": "POK:1157",
183	          "words": [
184	            {"translit": "verdeka, veredka", "gloss": "kidney", "script": null}
185	          ],
186	          "note": "because of its round shape",
187	          "quote": null
188	        },
189	        {
190	          "id": 7,
191	          "parent": 6,
192	          "lang": "Pahlavi",
193	          "refs": "MON:3255",
194	          "words": [
195	            {"translit": "gurtak", "gloss": "kidney", "script": null}
196	          ],
197	          "note": null,
198	          "quote": null
199	        },
200	        {
201	          "id": 8,
202	          "parent": 7,
203	          "lang": "Persian",
204	          "refs": "MON:3255",
205	          "words": [
206	            {"translit": "gordeh", "gloss": "kidney", "script": "گرده"}
207	          ],
208	          "note": null,
209	          "quote": null
210	        }
211	      ]
212	    }
213	  ]
214	}
215	
```


## [2026-10-17T00:00:29.510Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -120; command ls data/verification/sources/refs/ | head -100; sed -n 1,200p tools/verify_check.py"
}
```


### [2026-10-17T00:00:29.954Z] TOOL RESULT

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


## [2026-10-17T00:00:42.453Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; grep -l -E 'gardîdan|bâvar|verbum' page-*.json | head; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','MON','BQT','AHD','ISS','KNT','HRN','BLY','SOD','WLD','IEC','PHD','NYB','HUB','CHEUNG','ARY','BRT','SKT']:\n  v=d.get(k,{}); print(k, {x:v.get(x) for x in ['kind','local_file','page_offset','lookup_hint','url']})\n\""
}
```


### [2026-10-17T00:00:43.030Z] TOOL RESULT

```
page-530.json
page-519.json
POK {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", 'url': 'https://archive.org/details/indogermanisches01pokouoft'}
KLN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", 'url': 'https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein'}
SYN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.", 'url': 'https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca'}
MON {'kind': 'website+archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", 'url': 'https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)'}
BQT {'kind': 'archive_djvu+local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", 'url': "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249."}
AHD {'kind': 'archive_djvu+website+archive_restricted', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).", 'url': 'https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only'}
ISS {'kind': 'google_books_preview+archive_restricted', 'local_file': None, 'page_offset': 'DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.", 'url': 'https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)'}
KNT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt', 'page_offset': 'leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.", 'url': 'https://archive.org/details/oldpers'}
HRN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", 'url': 'https://archive.org/details/grundrissderneu00horngoog'}
BLY {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BLY/BLY_Hvatanica_II_BSOS9_1937_pp69-78.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BLY/BLY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BLY/Bailey_Studies_1930-1993_bedrosian.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BLY/BLY_bailey_studies_pages.txt'], 'page_offset': 'BLY_pages.txt: 11 leaves; printed = leaf(1-based) + 67 (leaf 2 = p.69 ... leaf 11 = p.78).', 'lookup_hint': "JSTOR only (BSOAS 9, 1937-39). Not on IA. Bailey's Dictionary of Khotan Saka (ISS_alt_DKS.txt, open) supersedes Hvatanica for the same words.", 'url': 'https://archive.org/details/bailey-studies-1930-1993 (Robert Bedrosian\'s open compilation "Selected Writings of H. W. Bailey"; Hvatanica II = PDF pp. 313-322)'}
SOD {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'], 'page_offset': 'printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)', 'lookup_hint': "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", 'url': 'https://archive.org/details/SogdianDictionary'}
WLD {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.", 'url': "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)"}
IEC {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", 'url': 'https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987'}
PHD {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).", 'url': 'https://archive.org/details/a-concise-pahlavi-dictionary'}
NYB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", 'url': 'https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg'}
HUB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", 'url': 'https://archive.org/details/persischestudie00hbgoog'}
CHEUNG {'kind': None, 'local_file': None, 'page_offset': None, 'lookup_hint': None, 'url': None}
ARY {'kind': 'local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", 'url': ''}
BRT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.", 'url': 'https://archive.org/details/altiranischeswr00bartgoog'}
SKT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", 'url': 'https://archive.org/details/aconciseetymolo01skeagoog'}
```


## [2026-10-17T00:00:49.371Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json\nfor p in [519,530]:\n  d=json.load(open(f'page-{p}.json'))\n  for e in d['entries']:\n    for n in e['nodes']:\n      s=json.dumps(n,ensure_ascii=False)\n      if 'bâvar' in s or 'gardîdan' in s or 'verbum' in s: print(p,e['root'],s[:6000]); print()\n\""
}
```


### [2026-10-17T00:00:49.717Z] TOOL RESULT

```
519 Upo {"id": 5, "lang": "Persian", "words": "padîd; pasand; bâvar; bedrŭd; pegâh; penhân", "verdict": "disputed", "derivation": "padīd 'visible' < MP pad dīd 'in sight' (Nyberg; Hübschmann: 'erst im Mittelpers. componirt aus pa und dīt'), not Av. *upa-dīti. pasand 'liking' < MP passand < *pati-sand- (Wiktionary, Nyberg, MacKenzie; Cheung's *sand 'seem'). bāvar 'belief' < MP wābar < upā + var- 'choose/believe' (Horn, Wiktionary) - plausible, though Nyberg prefers reduplicated *vā-vara-. bedrūd/padrūd 'farewell' < pa + drōd 'health' (MP drōd < *druvatāt-), Wiktionary 'be + dorud'. pegāh 'early morning' < pa + gāh 'time' ('betimes', Hübschmann/Nöldeke; Mo'in '= بگاه، بهنگام'). penhān 'hidden' < MP pad + nihān (Wiktionary; Horn himself 'phlv. pa nihān'). Five of six words therefore come from *pati-, not upa; worst verdict disputed.", "derivation_fa": "«پدید» از فارسی میانهٔ pad dīd «در دید» است؛ «پسند» از passand و ایرانی باستان *pati-sand-؛ «بدرود / پدرود» از pa + drōd «تندرستی»؛ «پگاه» از pa + gāh «به‌گاه، بهنگام»؛ و «پنهان» از pad + nihān. پس پیشوند همهٔ این‌ها pa- (از *pati-) است نه upa. تنها «باور» (فارسی میانه wābar) را می‌توان با هرن و ویکی‌واژه از upā + var- «برگزیدن، باور داشتن» دانست، هرچند نیبرگ صورت دوتایی *vā-vara- را ترجیح می‌دهد. هوبشمان همان زمان سخن هرن را درباره «پدید» و «پگاه» رد کرده بود.", "sources": ["https://en.wiktionary.org/wiki/پدید", "https://en.wiktionary.org/wiki/پسند", "https://en.wiktionary.org/wiki/باور", "https://en.wiktionary.org/wiki/بدرود", "https://en.wiktionary.org/wiki/پنهان", "https://en.wiktionary.org/wiki/پگاه"], "ref_check": [{"ref": "BQT:373", "status": "partial", "note": "BQT_v1_pages.txt leaf 597 (≈p.373) s.v. پدید: Mo'in's footnote 'پهلوی ... کارنامه ... اوستا ... نیبرگ پهلوی آنرا ... نوشته ... آشکار' - gives the Pahlavi pad-dīd form; OCR rough."}, {"ref": "BQT:406", "status": "not_found", "note": "leaf ≈632 not clearly matched; پگاه appears as 'بگه ... مخفف بگاه است که سحر و صبح باشد' at leaf 640 (≈p.414), i.e. be-gāh."}, {"ref": "BQT:2230", "status": "not_found", "note": "ref_page.py BQT:2230 (vol.4 pdf 313) shows نیک / نیکو entries; نهان is at pdf 296-297 (≈p.2213-2214)."}], "consulted": [{"src": "HUB", "where": "p. 42-43, notes to Horn nos. 289, 324 (HUB.txt l.1268-1276, 1440-1446)", "stance": "contradicts", "note": "'289. Streiche die Worte: \"also aw. *upadīti-\" ... Das Wort padīd sichtbar ist erst im Mittelpers. componirt aus pa und dīt = \"in Sicht\" wie padrūd aus pa und drūt'; '324. Np. pagāh ... kann weder = zd. *upakasa- noch = zd. *paitikāsa- gesetzt werden, sondern wird am besten mit Nöldeke als mp. Neubildung aus pa und gāh \"Zeit\"... gefasst'"}, {"src": "NYB", "where": "vol. II s.v. dīt, passand, vāvarīkānēh (l.1293, 2990, 3938)", "stance": "contradicts", "note": "'NP padid'; 'NP pasand; < *pat-sand-'; for vāvar: '*vā-vara- \"choice\" ... from Av. var-, pres. vāvar-'."}, {"src": "PHD", "where": "s.v. passand, paydāg, nihān, drōd (l.4087, 4135, 3762, 2066)", "stance": "partial", "note": "'passand [psnd | N pasand] pleasure, liking'; 'nihān [nyhʾn] concealment, secrecy'; 'drōd ... health, well-being' - components of pa-compounds; no upa."}, {"src": "MON", "where": "2-vol. Mo'in (MON_part1.txt l.32365, 21615)", "stance": "supports", "note": "'پگاه ... [= بگاه، بهنگام] صبح' and 'بدرود [= پدرود] سلامت' - support pa/be + gāh, be + drūd."}, {"src": "HRN", "where": "pp.41,65,71-73", "stance": "partial", "note": "Horn's upa-derivations (see ref_check); for penhān he himself gives 'phlv. pa nihān'."}]}

530 Weg 2 {"id": 12, "lang": "Germanic", "words": "waken; wakjan; waht", "verdict": "confirmed", "derivation": "These are Watkins's Proto-Germanic forms: *wakēn (stative, o-grade *wog-ē-) 'to be awake' > OE wacian, Goth. wakan; *wakjan (causative *wog-eyo-) > OE weccan, wæccan 'to keep watch', Goth. uswakjan 'awaken'; and *waht- / *wahtwō 'watch, guard' > OHG wahta, Frankish *wahtu. Germanic *k and *h(t) regularly reflect PIE *ǵ (Grimm's law: *ǵ > *k; before t, *kt > *ht).", "derivation_fa": "این‌ها صورت‌های ژرمنی آغازینِ واتکینز هستند: *wakēn «بیدار بودن» (انگلیسی کهن wacian، گوتی wakan)، *wakjan به معنای سببی «بیدار نگه داشتن، پاییدن» (انگلیسی کهن weccan، گوتی uswakjan) و *waht- / *wahtwō «پاس، نگهبانی» (آلمانی کهن wahta). k ژرمنی بنا به قانون گریم از ǵ هندواروپایی است و kt در ژرمنی به ht بدل شده است. ادعای نورایی درست است.", "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weǵ-", "https://en.wiktionary.org/wiki/watch", "https://en.wiktionary.org/wiki/wait"], "ref_check": [{"ref": "AHD", "status": "supports", "note": "AHD_watkins1985.txt line 1132, weg-2: '1. ... Germanic *wakēn in Old English *wacan, to wake up, arise, and wacian, to be awake: WAKE ... 3. Germanic *wakjan in Old English weccan, to be awake: WATCH. 4. Germanic *wahtwō ... 5. Germanic *waht- in: a. Old North French waitier, to watch: WAIT'."}], "consulted": [{"src": "POK", "where": "p. 1117 (POK_full.txt line ~89068)", "stance": "supports", "note": "'Gothic gawaknan \"wake up\" ... Kaus. Gothic uswakjan \"awaken\" ... Zustandsverbum Germanic *wakēn: Gothic wakan ... Old English wacian ... Old High German wahta'."}, {"src": "WLD", "where": "Bd. I pp. 246-247 s.v. ueg- (WLD_Bd1_pages.txt line ~22993-23040)", "stance": "supports", "note": "'ueg- \"frisch, rege, kräftig sein\". Lat. vegeō ... vigeō ... vigil ... Ai. vāja-h \"Kraft, Schnelligkeit, Wettkampf\" ... vajra-h \"Donnerkeil (des Indra)\" = av. vazra- \"Keule\" ... ap. vazarka- \"groß\" (nach Bartholomae Altiran. Wb. 1390 aus iran. *uazrka-, Ableitung von *uazar n.)' and 'ahd. wachar \"regsam, frisch, wacker\" (formell = ai. vajra-, av. vazra-)'."}, {"src": "SYN", "where": "Buck, 'wake' section (SYN.txt line 6993)", "stance": "supports", "note": "'In ME the forms of the strong OE (wæcnan), wōc, wōcon coalesced with the weak OE wacian ... Hence NE wake, awake, waken, awaken'; '(cf. the Gmc. group ...)' linked to Lat. vigil, vigēre."}]}
```


## [2026-10-17T00:01:19.786Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"Page\\(s\\): 11(42|43|44|56|57|58|62|63)\" POK_full.txt | head -30; grep -n -E \"lemma: (5\\. )?u̯er-|lemma: u̯ert|lemma: uer\" POK_full.txt | head -30"
}
```


### [2026-10-17T00:01:20.239Z] TOOL RESULT

```
90752:Page(s): 1144-1145 
91825:Page(s): 1156-1158 
91927:Page(s): 1158-1159 
92153:Page(s): 1162-1163 
92214:Page(s): 1163-1164 
22997:Root / lemma: uer-3. E. uer-gh- {* suerg^h^: "to turn, press, strangle' < [common Latin 
74446:Root / lemma: uer-3. E. uer-gh- {* suerg^h^: "to turn, press, strangle' < [common Latin 
90799:Root / lemma: uerrS^-1 
90836:Root / lemma: uervS^-2 
91045:Root/ lemma: uep-2\ "to throw, throw out' derived from an extended Root/ lemma: uer-3. 
91141:Root /lemma: uerg-1, ureg-{*huerg-1) 
91166:Root / lemma: uerg-2, ureg- {*hueig-2) 
91239:Root /lemma: uer-10{*huer-10) 
91247:Root /lemma: uer-11, uer9-{*huer-11) 
91293:Root / lemma: uer-12{*huer-12) 
91314:Root / lemma: uer-13{*huer-13) 
91335:Root/ lemma: uer-1, also suer-{*huer-f) 
91411:Root / lemma: uer-2{*huer-2) 
91474:Root / lemma: uer-3{*huer-3) 
91484:Root/ lemma: uer-3. A. ufmi-s, ufmo-s{*huer-3) 
91513:Root / lemma: uer-3. B. uer-b-3in6 uer-k:i^-{*huer-3) 
91556:Root / lemma: uer-3. C. u(e)r-ed- {*huer-3) 
91578:Root / lemma: uer-3. D. uer-g- {*huer-3) 
91609:Root / lemma: uer-3. E. uer-gh-{*hues-3) 
91615:Root/ lemma: uer-3. E. uer-gh-{*hueiy''h^\ "to turn, press, strangle' derived from g- 
91637:Root/ lemma: uer-3. E. uer-gh- {* suerg^h^: 'to turn, press, strangle' < [common Latin 
91686:Root / lemma: uer-3. F. uer-k- {*hue-3) 
91713:Root / lemma: uer-3. G. uer-p-, ur-ep-{*huer-3) 
91760:Root / lemma: uer-3. H. uer-t- {* huer-3) 
91827:Root / lemma: uer-3. I. ur-ei- a) urei-n-: {* huer-3) 
91846:Root / lemma: uer-S. I. ur-e/-. p) urizd- {* huer-3) 
91860:Root/ lemma: uer-3. I. ur-ei- y) ureig- {* huer-3) 
91877:Root/ lemma: uer-3. I. ur-ek 5) ureiR- {* huer-3) 
91929:Root / lemma: uer-3. I. ur-ek e) ureip-, unp-{*huer-3) 
91949:Root / lemma: uer-S. I. ur-ei-. Q ureit- {* huer-3)
```


## [2026-10-17T00:01:29.959Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92100,92215p POK_full.txt; echo ----; sed -n 91760,91830p POK_full.txt; grep -n -i -E \"vərəδka|vfrka|Niere\" POK_full.txt | head -20"
}
```


### [2026-10-17T00:01:30.246Z] TOOL RESULT

```
Meaning: to talk, speak 

Note: also uere-, ure- 

Material: Avestan urvata-n. " determination, command ' (= phtov), next to which from the 

light basis *uere-: Avestan urvata- n. " determination ' = Old Indie vrata-n. " command, 

statute, profession, declaration ', and Old Church Slavic rota^oaVn'; ablaut. Old Prussian 

wertemmaT we schworen'; 

gr. £ipu) "say' (*F£pju)), Fut ep. Ionian spsu), Attic spw. Pass. Aor. Ionian dpsOnv 
(*£Fp£0r|v), Attic sppnOnv (*£Fpn0r|v), Perf. £ipr|-Ka, -|jai diss, from *F£Fpr|-, compare 
geneuertes = renamed, has changed?? arg. F£Fpr|M£va; phtoc; "verabredet = festgesetzt', 
PHToop, Aeolic Fpniajp "Redner', pnrpa, el. Fparpa f. " saying, pact, covenant', diss, to 



Cypriot Fpnra, whereof £uFpr|TaaaTU "pact, covenant, law ', pnija "word", pf\a\(; " discourse 
', £ipu)v ' someone, the sich verstellt' (*F£pju)v), eipwvEia "Verstellung"; 

russ. vru{*vbrg), vratb'We, maunder, drivel ', with /r-suffix {*uorka): russ. ura/ra "empty 
gossip'. Old Church Slavic vracb ( *uorkios) 'physician, medicine man (*sayer of a magic 
spell), magician, sorcerer'; 

Maybe alb. Geg vra, Tosc vras'V\\\, wound' is related to the revenge killing examined by 
the medicine man. 

Hittite uenia- "call, shout, cry, beauftragen', particle -^aA- actually "sagte'; 

perhaps (in spite of Vasmer 2, 508 f. and above S. 860) here Balto-Slavic urek-, urek- in 
Lithuanian rekiu, rekti, Latvian /e/r/'cry', r^kuoV be entertained ', Old Church Slavic rekQ, 
resti^saY, ablaut. Old Church Slavic rokb " time, period, Termin', recb " accusation ' and 
*urdk-\v\ Germanic Gothic wrohs^ accusation ', by/'(9/7ya/7'beschuldigen' = west-Germanic 
*wrdgjan. Old High German ruogen. Modern High German rugen; 

d^-extension uer-6^o-e\.c.: 

Gr. pepGei cpeEyyeTai Hes. (Specht KZ 59, 65); 

Latin verbum' word' (not from *i/c»/t'o/77 because of:) Umbrian uerfale^ an open place for 
observation, place marked off by the augur's staff '; 

Gothic waurd. Old High German worteic. "word' = Old Prussian mrcfs'\Nor6'; Lithuanian 
vardas' name'. 

References: WP. I 283 f., WH. II 756 f., Trautmann 238, 360, Vasmer 1 , 234 f., 2, 539, 

Frisk 469 ff.; 

See also: here probably urek-. 

Page(s): 1162-1163 

Root / lemma: uer-7{*huer-7) 

Meaning: to tear 

Note: base for extensions: 

Material: A. uerd-: kvesiau varadva- 'soit, lax ', Old Church Slavic vredb, russ. vered 

"wound'; ured-:0\6 Indie avradanta ' s\e wurden weich', vrand/n- 'murbe werdend'; ured-: 

Old Prussian /'eo'c»"Ackerfurche', Old Danish vraade, i//'c»ofe"dig, aufbohren'; urdd-:\-aWv\ 

rodo, -ere^ gnaw, consume', rostrum {* rod -troni) n. "Nagewerkzeug, snout, bill, beak, neb'. 



Old English wrotan^ gnaw, dig', Old Icelandic rota 6s., Old High German z^yoz// 'suscitat, 
movet'. Old English wrot. Middle High German ruozel, ruezel. Modern High German 
Russel{ *wrdtila-)\ in addition zero grade in Swedish dial, rota, ruta'6\g'; after Frisk (Etyma 
Armen. 30) in addition still Armenian gercum ' s\r\a\/e' from *^e/'o'-s- (originally Aorist 
formation). 

B. uoma:a\b. varre^\N0un6', russ. KC»/'c»/75"Ruderloch in Schiffsheck, Hennensteift' 
(therefrom i/c»/'d/7/ra"Trichter'), poln. wrona, Czech vrana ^ aperture '; ure-no-, uro-no-\r\ Old 
Indie vrana-rr\. n. 'wound, crack' besides urd-na\r\ Old Church Slavic russ. etc. rana 
"wound'. 

Maybe alb. {*varna) Ka/r'grave' [common alb. /77->/7'- shift]. 

C. uergh-:0\6 Indie vrhat/" re\Q>tiro{r\', Aor. varh/, participle vrdha-, mu/a-vrt'6'\e roots 
ausreiftend' (Wackernagel KZ. 67, 166 ff.). 

D. uerk-, urek-sgr. paKO(;, Aeolic ppaKO(; (*FpaKoc;) n. "rag, zerlumptes dress; wrinkle'; 
ppaKaAov ponaAov Hes.; ppaKSTOV 5p£navov, KAaSsurripiov Hes., paKSTpov ds.; 

E. uresk- {from *urek-sk-), ufsk-0\6 Indie vrscat/ 'hautab, splits', vrascana- 'abbauend', 
n. "das Abhauen', pra-vraska-m. "cut'; ava-vrasca- 'sp\\r\ter'; russ.-Church Slavic vraska 
etc. "wrinkle' {*uorska). 

Maybe alb. Kras'kill' [alb. possible -ska > -s] 

F. ur-ei-, un-:gr. pivri "file, tool for smoothing surfaces, Raspel' {*yr/ha; or onomatopoeic 
word?) and "Haifisch' (from seiner zum Polieren verwendeten rauhen RiJckenhaut'); pTv6(; 
"skin; Lederschild', (Aeolic) YpTvo(; (i.e. FpTvo(;) Ssppa Hes., hom. laKaOpwoq 
"schildtragend' (compare M. Leumann, Homer. Worter 196 ff.); 

with o<-extension (originally o<-present?) Old English wrTtan^ dig in, ritzen, write, paint ', 
Old Saxon wrTtan^iear, verwunden, ritzen, write ', Middle Low German wrften^ rend, write, 
draw, sign ', Modern High German reiden, Proto Norse wrait^sc\\r\eb, ritzte' (besides 
Germanic *rTtan\r\ Old Swedish rftads., compare unter/"©/-, rei-d- "ritzen'); Gothic writs 
"line'. Old English M//7/"Schrift', m//'^// "ornament, decoration, jewellery, jewel' ; 

after Frisk (Etyma Arm. 28 ff.) here Armenian erg/canem 'tear, break, rupture, grind, 
carve, slit, injure, stir, tease, irritate' from *ureid-s-. 

References: WP. I 286 f., Trautmann 236, Vasmer 1 , 229. 



Page(s): 1163-1164 

----
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


66767:from Latin pr/fsjmus s'wnWar *pnsemi-, -e/Old Irish rem- prefix (lenierend) "before, voran' 
68387:Middle Low German flomei. ' raw Bauch- and Nierenfett', Modern High German Flom, 
72705:s/7"Schleuse, Ablaufkanal', s/7e/7"dranieren'; Old English seohtrei. {*sihtrdn-). Middle Low
```


## [2026-10-17T00:01:37.327Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^wer-|^wert-|^werə|^wē?r-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-10-17T00:01:37.668Z] TOOL RESULT

```
1143:wer-3
1145:wer-4
1147:wer-4. To perceive, watch out for. I. O-grade form *wor-. 1. Suffixed form *wor-o- in Germanic *waraz in: a. Old English wer, watchful: wary; b. Old English gewer, aware (ge-, collective and intensive prefix; see kom): AWARE; C. Old English warian, to beware: WARE?. 2. Suffixed form *wor-to- in Germanic *wardaz, guard, and *wardén, to guard, in: a. (i) Old English weard, a watching, keeper: WARD; STEWARD (ii) Old English wear- dian, to ward, guard: WARDER?; b. Old North French warder, to guard: WARDEN; REWARD, WARDROBE; C. Old French guarder, to guard: GUARD; d. Anglo-Norman warde, guard: REARWARD?. 3. Germanic *ward in: a. Old English waru, goods, protection, guard: WARE}; b. Old English -ware (probably plural of waru, “goods”’), inhabi- tants (< “defenders’’): FIELDFARE. 4. Suffixed form *wor-wo- in Greek ouros, a guard: ARCTURUS. 5. Variant *(s)wor-, s(w)or- probably in Greek horan, to see: EPHOR, PANORAMA. II. Suffixed (stative) form *wer-é- in Latin veréri, to respect, feel awe for: REVERE!. [Pok. 8. wer- 1164.]
1148:wer-5. To cover. I. Basic form *wer-. 1. Germanic *wer- jon- in Old English wer, dam, fish trap: WEIR. 2. Com- pound form *ap-wer-yo- (*ap-, off, away; see apo-) in Latin aperire, to open, uncover: APERIENT, APERITIF, APERTURE; OVERT, OVERTURE, PERT. 3. Compound form
```


## [2026-10-17T00:01:40.174Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1140,1160p AHD_watkins1985.txt | cut -c1-2500"
}
```


### [2026-10-17T00:01:40.692Z] TOOL RESULT

```
for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bisontés), bison: BISON. [Pok. 3. ueis- 1134.] weit(a)-. To speak, adjudge. Extended o-grade form *woito- in Russian véti, council (see sem-'). wekti-. Thing, creature. Germanic *wihti- in Old English wiht, person, thing: WIGHT!; (AUGHT?), NAUGHT, NOT. [Pok. wek-ti- 1136.] = wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will power: WILL. 4. Germanic *wil(Ijan in Old English wyllan, willan, to desire: WILL?; NILL. 5. Ger- manic compound *wil-kumon- (see g¥a-). 6. O-grade form *wol- in Germanic *wal- in Old French galloper and Old North French waloper, to gallop: GALLOP, WALLOP. 7. Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY; BENEVO- LENT, MALEVOLENT. 8. Suffixed form *wel-up- in Latin voluptds, pleasure: VOLUPTUARY, VOLUPTUOUS. [Pok. 2. uel- 1137.] wel-3, To turn, roll; with derivatives referring to curved, enclosing objects. 1. Germanic *walt- in: a. Old High German wailzan, to roll, waltz: wALTz; b. Middle Dutch welteren, to roll: WELTER. 2. Germanic *weluka- in Old English weoluc, weoloc, mollusk (having a spiral shell), whelk: WHELK!. 3. Perhaps Germanic *wel- in Old Eng- lish welig, willow (with flexible twigs): wILLOw. 4. Per- haps Germanic *welk- in Old English wealcan, to roll, toss, and wealcian, to muffle up: WALK. 5. O-grade form *wol- in Germanic *wall- in: 
wel-4
HELMINTH; ANTHELMINTIC, PLATYHELMINTH. [Pok. 7. uel- 1140.] wel-‘, To tear, pull. 1. Suffixed form *wel-do- in Latin vellere, to tear, pull: AVULSE, CONVULSE, DIVULSION, EVULSION, REVULSION, SVELTE. 2. Suffixed form *wel-no- in Latin vullis, shaggy hair, wool: VELOURS, VELVET, VILLUS [Pok. 8. wel- 1144.] wele-'. Wool. Probably related to wel-‘. 1. Suffixed extended zero-grade form “*wi-nd- in: a. Germanic *wullé in Old English wul(l), wool: woot; b. Italic *wland in Latin lana (> French laine), wool, and its derivative laénig6, down: LANATE; DELAINE, LANIFER- OUS, LANOLIN, LANUGO; ¢. Celtic *wland in Welsh gwlan, wool (> Middle English flannel, woolen cloth): FLANNEL. 2. Possible suffixed o-grade form *wol(o)-no- in Greek oulos, wooly, curly: ULoTRICHOUs. [Pok. 4. uel- 1139.] wela-2. To strike, wound. 1. Suffixed o-grade form *wol()-o- in Germanic *walaz in Old Norse valr, the slain in battle in: a. Old Norse Valhdéll, Valhalla: VAL- HALLA; b. Old Norse Valkyrja, “chooser of the slain,” name of one of the twelve war goddesses (-kyrja, chooser; see geus-): VALKYRIE. 2. Suffixed basic form *welo-nes- in Latin vudnus (stem vulner-), a wound: VULNERABLE. [In Pok. 8. wel- 1144.] welg-. Wet. Germanic *welk- in: a. Old English wolc(e)n, cloud, sky: WELKIN; b. Middle English welken, to wilt: wILT!. [Pok. 2. welk-, uelg-, 1145.] welt-. Woods; wild. 1. Suffixed form *wolt-u- in Germanic *walthuz in: a. Old English weald, wald, a forest: WEALD, WOLD!; b. Old Norse vdllr, field: VOLE!. 2. Ger- manic *walthdn- in Middle English welde, a plant yield- ing a yellow dye, weld: WELD2. 3. Germanic *wilthigaz in: a. Old English wilde, wild: wip; b. Old English wildéor, wilddéor, wild beast (déor, animal; see dheu-'): WILDERNESS; C. Dutch wild, wild: WILDEBEEST. [In Pok. 4. uel- 1139.] weme-. To vomit. 1. Germanic *wam- in Old Norse vamla, qualm, and Danish vamle, to become sick, prob- ably akin to the Scandinavian source of Middle English wam(ejlen, to feel nausea, stagger: WAMBLE. 2. Latin vomere, to vomit: NUX VOMICA, VOMIT. 3. Greek emein, to vomit: EMESIS, EMETIC. [Pok. wem- 1146.] wen-', To desire, strive for. 1. Suffixed form *wen-w- in Germanic *winn(w)an, to seek to gain, in Old English winnan, to win: WIN}. 2. Suffixed zero-grade form *wn-ydé in Germanic *wunjé in Old English wynn, wen, pleasure, joy: WEN2, WINSOME. 3. Suffixed (stative) zero-grade form *wn-é-, to be contented, in Germanic *wunén in Old English wunian, to become accustomed to, dwell: won!, (wont). 4
wer-3
*wn-to- in Germanic *wundaz in Old English wund, a wound: WOUND!. 2. Suffixed o-grade form *won-yo- in Germanic *wanja-, a swelling, in Old English wen(n), wen{n), wen: WENI. [In Pok. 1. ué- 1108.] wendh-. To turn, wind, weave. 1. Germanic *windan, to wind, in: a. Old English windan, to wind: WIND2; b. Old Norse vinda, to wind: WINDLASS. 2. Germanic causative *wandjan in: a. Old English wendan, to turn to: WEND; b. Dutch wenden, to turn: WENTLETRAP. 3. Germanic *wandr6n, to roam about, in: a. Old English wandrian, to wander: WANDER; b. German wandern, to wander: WANDERLUST. 4. Germanic *wanduz in Old Norse véndr, a supple twig: WAND. 5. Germanic *wandljaz, “wan- derer,” perhaps in Latin Vandalus, a Vandal: VANDAL. [Pok. 1. uwendh- 1148.] weng-. To bend, curve. 1. Germanic *wink- in Old Eng- lish wincian, to close the eyes (< “to bend down the eyelids”): WINK. 2. Germanic *winkja in Old English wince, a reel, roller: WINCH. 3. Germanic *winkil- in Old English -wincel, spiral shell: PERIWINKLE!. 4, Germanic *wankil-, *wankul- in: a. Old English wencel, youth, maid (< “inconstant one’): WENCH; b. Old English wancol, inconstant, unsteady: wonky. 5. Germanic *wankj- in: a. Old French gauchir, to turn aside: GAUCHE; b. Anglo-Norman *wencir, to turn aside, avoid (> Middle English wincen, to kick): w1NcE. [Pok. we-n-g- 1148.] wep-. Bad, evil. From earlier *awep-. Suffixed zero-grade form *up-elo- in Germanic *ubilaz, evil, in Old English yfel, evil: EVIL. [wépnam. Weapon. Germanic root. 1. Old English wé- P(e)n, weapon: WEAPON. 2. Old Norse vapn (plural vdpn), weapon: WAPENTAKE.] wer-', High raised spot. 1. Suffixed form *wer-d- in Germanic *wartén- in Old English wearte, wart: WART. 2. Possibly Germanic *war- in obsolete Swedish var- bulde, “pus swelling” (bulde, swelling; see bhel-2), akin to the source of WARBLE2. 3. Latin varius (genitive plural variérum), spotty, speckled, changeable: (VAIR), VARIE- GATE, (VARIETY), VARIOLA, VARIORUM, VARIOUS, VARY; (MINIVER). 4. Latin varix, varicose vein: VARIX. 5. Suf- fixed and extended zero-grade form *wrsu-ko- in Latin verriica, a wart: VERRUCA. [Pok. 2. wer- 1151, 2. ud- 1108.] wer-2. To raise, lift, hold suspended. Earlier form *ower-. 1. Basic form *awer- in Greek aeirein, to raise, and Greek artéria, windpipe, artery: AORTA, ARSIS, ARTERIO-, ARTERIOLE, ARTERY. 2. Possibly referred to this root (obscure basic form *dwer-) is Greek aér (> Latin aer > Italian aria), air: AERIAL AERO-, AIR, ARIA, MALARIA. 3. Related to 
wer-4
TRORSE, SUBVERT, TERGIVERSATE, TRANSVERSE, UNI- VERSE. 5. Balto-Slavic *wirstd-, a turn, bend, in Russian versta, line: VERST. II. Root *wreit-, to turn. Germanic *writh-, *wraith- in: a. Old English writha, band (< “that which is wound around”): WREATH; b. Old English writhan, to twist, torture: WRITHE; Cc. Old English wrath, angry (< “tormented, twisted”): WRATH, WROTH. III. Root *wergh-, to turn. 1. Germanic *wurgjan in Old English wyrgan, to strangle: WORRY. 2. Nasalized vari- ant *wrengh- in: a. Germanic *wreng- in Old English wringan, to twist: WRING; b. Germanic *wrang- in (i) Old Norse *vrangr, rangr, curved, crooked, wrong, akin to the Scandinavian source of Middle English wrong, wrong: WRONG (ii) Low German wrangeln, to wrestle, akin to the Low German source of Middle English wranglen, to wrangle: WRANGLE. IV. Root *werg-, to turn. 1. Nasalized variant form *wreng- in Germanic *wrankjan in: a. Old English wrencan, to twist: WRENCH; b. Old English gewrinclian, to wind (ge-, col- lective prefix; see kom): WRINKLE. 2. Latin vergere, to turn, tend toward: VERGE?; CONVERGE, DIVERGE. V. Root *wreik-, to turn. 1. Germanic *wrig- in: a. Old English wrigian, to turn, bend, go: wRy; b. Middle Low German wriggeln, to wriggle: WRIGGLE. 2. Germanic *wrthst- whence *wristiz in Old English wrist, wrist: wRIsT. 3. Secondary Germanic derivative *wraistjan in Old English wréstan, to twist, with its frequentative *wréstlian, to wrestle: WREST, WRESTLE. 4. Possibly o-grade form *wroik- in Gaulish *briiko, heather (> French bruyére, heath): BRIAR}. VI. Germanic root *wrib- in Old French riber, to be wanton: RIBALD. VII. Root *werb-, also *werbh-, to turn, bend. 1. Ger- manic *werp-, *warp-, “to fling by turning the arm,” in Old English weorpan, to throw away: WARP. 2. Latin verber, whip, rod: REVERBERATE. 3. Latin verbéna, sacred foliage: VERBENA, (VERVAIN). 4, Zero-grade form *wrb- in Greek rhabdos, rod: RHABDOMANCY, RHABDOVI- Rus. 5. Nasalized variant form *wrembh- in Greek rhom- bos, magic wheel, rhombus: RHOMBUS. VIII. Root *werp-, to turn, wind. 1. Metathesized form *wrep- in Germanic *wrap- in Danish dialectal vraule, to wind, akin to the source of Middle English wrappen, to wrap: wraP. 2. Zero-grade form *wrp- in Greek rhaptein, to sew (> rhaphé, suture): RAPHE, RAPHIDE; RHAPSODY, STAPHYLORRHAPHY, TENORRHAPHY. IX. Root *wrmi-, worm; rhyme word to k*rmi-. 1. Germanic *wurmiz in Old English wyrm, worm: worm. 2. Latin vermis, worm: VERMEIL, VERMI-, VERMICELLI, V
wer-4. To perceive, watch out for. I. O-grade form *wor-. 1. Suffixed form *wor-o- in Germanic *waraz in: a. Old English wer, watchful: wary; b. Old English gewer, aware (ge-, collective and intensive prefix; see kom): AWARE; C. Old English warian, to beware: WARE?. 2. Suffixed form *wor-to- in Germanic *wardaz, guard, and *wardén, to guard, in: a. (i) Old English weard, a watching, keeper: WARD; STEWARD (ii) Old English wear- dian, to ward, guard: WARDER?; b. Old North French warder, to guard: WARDEN; REWARD, WARDROBE; C. Old French guarder, to guard: GUARD; d. Anglo-Norman warde, guard: REARWARD?. 3. Germanic *ward in: a. Old English waru, goods, protection, guard: WARE}; b. Old English -ware (probably plural of waru, “goods”’), inhabi- tants (< “defenders’’): FIELDFARE. 4. Suffixed form *wor-wo- in Greek ouros, a guard: ARCTURUS. 5. Variant *(s)wor-, s(w)or- probably in Greek horan, to see: EPHOR, PANORAMA. II. Suffixed (stative) form *wer-é- in Latin veréri, to respect, feel awe for: REVERE!. [Pok. 8. wer- 1164.]
wer-5. To cover. I. Basic form *wer-. 1. Germanic *wer- jon- in Old English wer, dam, fish trap: WEIR. 2. Com- pound form *ap-wer-yo- (*ap-, off, away; see apo-) in Latin aperire, to open, uncover: APERIENT, APERITIF, APERTURE; OVERT, OVERTURE, PERT. 3. Compound form
77
wers-2
*op-wer-yo- (*op-, over; see epi) in Latin operire, to cover: COVER, OPERCULUM. II. O-grade form *wor-. 1. Germanic *war-nén in Old English war(e)nian, to take heed: WARN. 2. Germanic *war- in: a. (i) Old French garant, warrant, authorization: GUARANTY (ii) Old North French warant, warrant, and warantir, to guarantee: WARRANT, (WARRANTEE), WARRANTY; b. Old French garer, to guard, protect: GARAGE; c. Old French g(u)arir, to defend, protect: GARRET, GARRISON; d. Old North French warenne, enclosure, game preserve: WARREN; e. Old French g(ujarnir, to equip: GARMENT, GARNISH. [Pok. 5. uer- 1160.] wer-S, Also wera-. To speak. Variant *wré-, contracted from *wreo-. 1. Suffixed zero-grade form *wr-dho- in Germanic *wurdam in Old English word, word: worD. 2. Suffixed form *wer-dho- in Latin verbum, word: VERB, VERVE; ADVERB, PROVERB. 3. Suffixed form *wer-yo- in Greek eirein, to say, speak: IRONY. 4. Variant form *wré- in suffixed form *wré-tor- in Greek rhétér, public speaker: RHETOR. [Pok. 6. wer- 1162.] wer-7. To burn. Suffixed lengthened o-grade (causative) form *w6r-yo- in Russian varit’, to boil: saMovarR. [Pok. 12. wer- 1166.] wer-®, Squirrel. Reduplicated expressive form *wi-wer(r)- in Latin viverra, a ferret: VIVERRINE. [Pok. 13. uer- 1166.] wér-. Water. Suffixed zero-grade form *dr-ind- in Latin irina, urine: URINE. [In Pok. 9. au(e)- 78.] were-', Wide, broad. Suffixed form *wer(a)-u- metathe- sized in Greek eurus, wide: EURY-; ANEURYSM, EURYD- IcE. [Pok. 8. wer- 1165.] were-2, To find. Variant *wré-, contracted from *wrea-. Reduplicated form *we-wré- in Greek heuriskein (first person singular perfect indicative active heuréka), to find: EUREKA, HEURISTIC. [Pok. 4. ver- 1160.] werg-. To do. I. Suffixed form *werg-o-. 1. Germanic *werkam, work, in: a. Old English weorc, werc, work: work; b. Old High German werc, work: (BOULEVARD),
’ BULWARK. 2. Greek ergon, work, action: ERG, -URGY;
ADRENERGIC, ALLERGY, ARGON, CHOLINERGIC, DEMI- URGE, DRAMATURGE, ENDERGONIC, ENDOERGIC, EN- ERGY, ERGOGRAPH, EXERGONIC, EXERGUE, EXOERGIC, GEORGIC, LITURGY, METALLURGY, SURGERY, (SYNERGID), SYNERGISM, THAUMATURGE. II. Zero-grade form *wrg-. 1. Suffixed forms *wrg-yo-, *wrg-to- in Germanic *wurk- Jan, to work, participle *wurhta-, in Old English wyrcan, to work, participle geworht, wrought: WROUGHT. 2. Suf- fixed form *wrg-t- in Germanic *wurhtj6- in Old English wryhta, maker, wright: WRIGHT. III. O-grade form *worg- in: a. Greek organon (with suffix -ano-), tool: ORGAN, ORGANON; b. Greek orgia, secret rites, worship (< “service”): ORGY. [Pok. 2. werg- 1168.]
wéro-. True. 1. Germanic *wéra- in Old English wér, faith, pledge: WARLOCK. 2. Latin vérus (> Old French voir, truth), true, with its derivative vérax, truth: VERA- CIOUS, VERISM, VERITY, VERY; AVER, VERDICT, VERIDI- CAL, VERIFY, VERISIMILAR, VOIR DIRE. 3. Latin sevérus, grave, serious; regarded by some as a compound of se-, sed, without (see s(w)e-), and vérus, true, but the semantic difficulties make this explanation improbable: SEVERE; ASSEVERATE, PERSEVERE. [Pok. 11. yer- 1165.]
wers-'. To confuse, mix up. Compare ers-'. I. Suffixed basic form. 1. Germanic *werz-a-, whence *werra- in: a. Old North French werre, war: WAR; b. Spanish gue- rra, war: GUERRILLA. 2. Germanic comparative *wers- izon- in Old English wyrsa, worse: WORSE. 3. Germanic superlative *wers-istaz in Old English wyrsta, worst: worst. II. Suffixed zero-grade form *wrs-ti- in Germanic *wursti- in Old High German wurst (> German Wurst), sausage (< “mixture”): WURST; (LIVERWURST). [Pok. uers- 1169.]
wers-2. To be wet. Compare ers-2. Suffixed o-grade (causative) form *wors-eyo- in Greek ourein, “to make water,” to urinate, whence ouron, urine: URETER, URE-
wes-!
THRA, URETIC, -URIA, URO-!, URONIC; DIURETIC, ENURE- sts. [In Pok. 9. au(e)- 78.]
wes-1. To buy. 1. Suffixed form *wes-no- in Latin vénum, sale: VENAL, VEND. 2. Suffixed o-grade form *wos-nd- in Greek dneisthai, to buy: DUOPSONY. [Pok. 8. wes- 1173.]
wes-?. Wet. Germanic *wdés- in Old English wés, juice: 00ZE}. [Pok. 3. wes- 1171.]
```


## [2026-10-17T00:01:46.768Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==293' WLD_Bd1_pages.txt | grep -n -i -E \"sagen|urvata|verbum|waurd|ειρ|eir\" | head; echo ===; for n in 279 280; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' WLD_Bd2_pages.txt | grep -n -i -E \"varət|vərəd|gurt|gurd|Niere|wenden|vart\" | head; echo --; done"
}
```


### [2026-10-17T00:01:47.131Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-10-17T00:01:52.084Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n -i -E \"urvata\" WLD_Bd1_pages.txt | head; grep -n -i -E \"gurtak|gurda|vərədka|vərəδka|Niere\" WLD_Bd1_pages.txt | head; grep -c . WLD_Bd1_pages.txt"
}
```


### [2026-10-17T00:01:52.412Z] TOOL RESULT

```
26792:      av. urvata- n. ..Bestiminuug, Gebot” (=m;rdr: BezzenbergerBB.   233 f.                                                                          1       .
4210:                                                      die     allgemeniere Bed. .Kraut, Blute"        entwickelt haben.
7736:geworden, wahrend sonst *ollod zu lenierendem *ollo, oil wurde auch ce-n                                                       ;
8822:ziert,       womit       identiscli               air.    a „sein“                (len.)        und „ibr“ (geminierend), cymr.
11362:   air. i n- „in“ (adnominal m. Dat. und Acc.       nasalierend), in- (lenierend,               ;
11510:: mit lit. mhstas „Niere“ als *eng-stro-, -sro- zu einem *cng- „Fett“, das
12107:  *neg'ih-ros „Niere, Hode“ („rundliche Anschwellung", vgl. zur Bed.
12108:lit.inkstas „Niere“ und „Hode“; -ro- und -en- vielleicht Entwicklungen
12110:       gr. vEfpgog,       meist PI., ,,Nieren“, praenestin. nefrones, lanuvin. nebrundines
12111:„Nieren,        Hoden“ (a. zum lautlichen Yf. IF. 19, 102);
12112:       ahd. nioro „Niere“,T. auch „Hode“, mengl. mnd. nere, aschwed. mure,
55196
```


## [2026-10-17T00:01:56.181Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 26770,26830p WLD_Bd1_pages.txt | cut -c1-200; grep -n -i -E \"gurtak|gurda|vərədka|varəδka|Niere|varət-\" WLD_Bd2_pages.txt | head"
}
```


### [2026-10-17T00:01:56.545Z] TOOL RESULT

```
sind unvereinbar (s. Falk-Torp u. rent).


5.    uer-             ..sagen, spreeheir ,                      auch * ur.--,

                                                                                      t
                                                                                           rc[i-            "/•?-?
                                                                                                                           j
                                                                                                                                 s.   Hirt PBrB. 23,
          203, Abb 111, Persson Beitr. (543. 732).
      Gr. ciqco              ..sage                                   tut.   ep. jon. ?o£ro,               att.       tnv>.           Pass. Aor. jon.
tiotOij                                              att.   enoi'jDijf                                Pf. eioij-y.n,                  -   tea        igliss.           aus
                       vgl.       geneuertes arg.                                           Solmsen Unt. 23b), oijnK ..ver-
abrodet               — festgesetzt”.                   /> i'/tojo,     itol.    _i   oi]row , Redner   dijTon, el. ypdr on
                                                                                                                      ',

..Sprueh,               Yertrag”,                diss.       zu kypr.                       woven f/yiyrawir                                       ..decrevit”.
pij/iu               .Rede”, iYoojv ..eincr. der etwas nur sagt. oline es
              .AVort',              dijoi;
zu meinen    \*ffnuvv. Solmsen Unt. 203. sielie auch Boisaeq s. v. mit
Kachtr.), tioojvda ..Yerstollung im Reden. um zu neckon odor zu be-
schlimen";
      av. urvata- n. ..Bestiminuug, Gebot” (=m;rdr: BezzenbergerBB.   233 f.                                                                          1       .
                                                                                                                                                                           ,



woneben von der leichten Basis                            ..Bostimmung” = ai.a -re-, av.    lumin-                n.
vrntu- n. ..Gebot, Satzung. Geliibde. religiose Pflicht und aksl. m/a..Eid”                                       •




(Meillet Msl. 0, 142. Liden Ein bsl. Anlautges. 20: s. auch Pedersen KZ.
30, 3.75 gegen Anreihung von arm. ctihuon ..sehwore"        mss. era *m„-,i),                                              ;


rriifb ..sich in der Rede beriehtigen”, mit /.-Suffix mss. erdin  leeres Ge-                                                                   .




schwatz”, aksl. rracb ,.Arzt (*Bespreclier\ Zaubercr, Hexenmeiscer” (Solmsen
aaO. fiber ferazuhalteiules slav. s. Strekelj AfslPh. 27, 505).
          ;


      Sehr fraglich
                 ist dagegen, ob mit si. mi/;- auch got. terdhs ..Anklage”.

irrohjmi .jbescliuldigen”. anord. i dijj-i ..verleumden”. ahd. /v.x/m ..anklagen.
beschuldigen”, nhd.       by/, it, as. wrOyinn,  ags. irieijan ds. zu verbinden ist
                                                 /


(v. Sabler KZ. 31, 2S3, z\v. Ilirt PBrB. 23, 203). Eher als in-ij/c - im Ab-
laut zu lit. riJch), -ia H ..schreien", wo 111 auch aksl. n’/’b ..Redo”, re/: it ..sage”
(Lewy PBrB.                       32,          142).        — Ganz verseliieden left, n'd ..schelten. tadeln.
strafen" (zu                 lit.         rojod ..kriihen \ apr. attrdhcei                        .   antworten"). sowie                                      lit      rb ti
..beiBen” (von Ilunden)                                     s.   Yf. LEWb. 2 u. vcrlmm                      und bes. iucw>                            .

2298:klisenkiirzung aus "^priSe^nei^,) air. rem- Praef, (lenierend) „vor, voran^^
6667:   Nd. flom „rohes Bauch- oder Nierenfett^^, ahd. floum „Sahne, rohesNieren-
14792:nach Wood Mod. Phil. 11, 316f. aisl. mate ,,schinieren“); as.              gimakon
18854:melm ^Staub, Sand^, lit. melmit ^Nierenstein, Steinkrankheit^^;
21378:a); aber kaum hieher air. no (lenierend), cymr. 7ieu „odern als erstarrte
21853:   gr. vspoj „teile aus, teile Weideland zu, weide; disponiere, beherrsche“,
26788:   S. u.       Jep „beschinieren‘\
29128:2.     lendh- „Lende; Niere‘^
29131:„]Sriere^ (usw., s. Berneker 705 f.); ahd. Ifnti f. „Niere^S PI. lentl{n) „Nieren,
29137:fleisch in der Nahe der Nieren“, norw. mdartl. hmd f. „Hufte, Lende^, ags.
```


## [2026-10-17T00:02:04.310Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} {n+=gsub(/\\n/,\"\\n\"); print NR, n}' WLD_Bd1_pages.txt | awk '$2>=26792' | head -1; grep -n -E \"vartati|varat-|varət\" WLD_Bd1_pages.txt | head; "
}
```


### [2026-10-17T00:02:04.964Z] TOOL RESULT

```
292 26843
```


## [2026-10-17T00:02:12.136Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==283||NR==284' WLD_Bd1_pages.txt | grep -n -i -E \"uert|vart|drehen|Niere|gurt|vṛkk|vrkk|av\\.\" | head -20"
}
```


### [2026-10-17T00:02:12.576Z] TOOL RESULT

```
8:treffen, findenA mhd. raffidn ,,\venden, drehenA ahd. rnzi „vagans, rapax“ (vgl.
24:zu *ucr- „drehen“ Beziehung hat (die Wurzeln sind meist verbogener als
29:..gedreht. valzig“ z. T. hierher oder zu *uert gestellto ahd. wurst, nhd.
31:      uert - „drehen, venden                    :   ai. vartalef-ti), vavartti,   vartti „dreht sich, rollt.
32:verliiuft.           geht vonstatten.         ist   da, lebt", av. varot „sich \venden“,
34:•         drehende Bewegung“ (= got. frawardjan, slav. vratiti, lit. vartyti),
36:rnrianu- n. „das Drehen“, vartida- „rund“, -a ..Spinnvirtol" (: mhd. wirtel),
40:vrr- als Bildung vie arm. gerandi); void av. rarsdka-, ai. vrldca- ..Niere".
42:fare ..Buekel" usv. auf *uert-hl oder *uerl,--<i zuriickfuhrt) gr. gaxdvij
49:versus, vorsus ..kehren. venden. drehen“,tw/-fer, vertex „(*Wirbel =) ScheiteF,
51:                                   enuertu
73:ai.    vartida, mhd. wirtel, si. vreteno), air. Praef. frith-. Praep. fri, meymr.
106:ebenfalls?); lit. vrrciii, verst ..wenden, kehren”, vartyti ..fortgesetzt wenden,
108:drehen, bobren", vratiti ,.drehen‘‘, vratt ..Hals”, vr'taio ..Spindel”. vtoshi
156:iiltere     slav.      Betonung [Yasmer briefl.J, vurbba ..Zirkelschnur. Zirkelbretf,
158:  Got. intitpntt ..werfen” L.*drehcn”   ..in drehende Bewegung setzen” oder
164:besser ..mit drehend geschwungenem      Anne sehleudern \ vgl. lat. toryuPrr
```


## [2026-10-17T00:02:17.370Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"Gottesurteil|Ordal\" BRT.txt | head; grep -n -E \"Niere\" BRT.txt | head; grep -n -E \"Gebot|Satzung\" BRT.txt | grep -i urv | head; grep -n -E \"sich wenden|wenden, \" BRT.txt | head"
}
```


### [2026-10-17T00:02:17.747Z] TOOL RESULT

```
3058:•  j.  *a-gar»mo.varah- ''  Adj.  'der  keine (Zulassung  zur)  Hilzeprobe  hat,  vom  Hitze- ordal  ausgeschlossen  isf:  myazdavä  ratus atnyaadavamm  ratunaim  "ratflum  daste antan  mazdayasiiilts  ". .  macht  (erklärt) der  Ji.  . .  den  Laien  . .  (für)  untähig,  eine Hitzeprobe  abzulegen  .  ."  A.j.9"
3646:Pü.:  dnddtdd.  —  0  Die  beiden  Stellen können  ursprunglich  nicht  den  gleichen  Wort- laut gehabt  haben.  An  der  1.  Stelle  wird  etwa gestanden  haben:  Wer  eines  Verbrechens  be- zichtigt wird  und  leugnet ,  soll  das  Ordal- wasser  trinken.  An  der  2.:  Wer  das  Ordal- wasser  trinkt,  (rolzdem  er  sich  einer  Schuld bewusst  ist,  wird. .  bestraft.  H erste II ungs ver- suche —  von  vornherein  aussichtslos  —  bei Sp.  Komm.  i.  156,  Gdn.  Stud.  i.  103.
7152:"^raoitS  (sd.)  V,  46. 7  •'.  a)  vom  Opfer- feuer: at  a  ^wahmäi  '%r!  ratam  iiima- t>hs  .,  asahyä  mä  ..  manyäi  (sd.)  Y.  47- 9.  b)   vom   eschatologischen   Ordal-
7927:*)  Die  Worte  beziehen  sich  auf  das  Wohl- gefühl des  Gerechten  und  die  Pein  der  Gott- losen beim  Durehschreiten  des  glühenden  Metall- stromes im  letzten  Gericht,  wovon  Bd.  jo.  19 eriihlt;  s.  aj-ai-  A  und  'ä/ar-  3  b.  Pii.  erl.: /äi-  am  fa  pasäxl  i/aiiiri  tu  öaväl  "damit  mit beim  Ordal  Brand  nicht  iterde";  5.  dam  Jk. JAOS.  14-  LViii   und    lu  V.  34-  4  unter  Äärj.-
9157:—  yat  {mafiatum')  kjnniiun^^^  amtSa. spiiita  (ahc)yti ..  YLiO.  51;  —  hqmJaptibyS aiwyö  cäxrare'*'  (3PPfM.)  nfnbyö  "mit heissem  Wasser  stellen  sie  es  (das  Ordal) an  den  Männern  an"  V..;.  46.  5)  'Je- manden, etwas  (Akk.)  machen  zu  -' (Akk.):  II  hy^  durayaf'Ti^um  xsäya^iyam akunau/  D.  6.  i;  4,X. /.  i,  6".  i,Ao. ;.  i;  — uiHsäm  I  martiyam  maHislam  akunau^''\iaA er  machte  einen  Mann  zu  ihrem  Obersten" Bh.  j.  9;  2.  6, 14,  J.  6, 14, 5.  i;  —  aniyam (sd.)    ''uslrabärim    akunavam    Bh.j.iSi;
22809:•  j.  'varah-  n.  'Probe,  Prüfung,  Ordal'*': urvdhqmcit  (sd.)  zbayem  avi  imai  TS uzdatTm  aviätnmca  bargsmäca  avipfnnqtn vjyzarayeintTm  avi  raoynyqm  varauhsm (sd.)  aeui/rmca  urvaranqm  ".  .  zu  dem hier  angestellten  Ordal,  zu  dem  Feuer  und Bansman,  zu  der  Uberfliessenden  Hohl- hand, zu  der  Ordalbutter  und  zum  Schmalz derPflanzen"  Yl/2.  3; — ys  *naire  *p3ri- mmnai  (sd.)  nsit  paiti-dmäiti  gatumca *'rasca'-^  zrvämmca  "..  Ort  (des  Gerichts) und  Ordal  =>  und  Termin  (des  Gerichts)" F.4C.
22810:♦)  Vgl.  DsT.  ZA.  2.  492-  liber  die  Ordale handelte  nach  Dk.  S.  42  ein  besonderer  Ab- schnitt des  iS.  Naiia  des  Awesta,  das  Varaslän. Über  die  verschiedenen  in  mp-  Schriften  ge- nannten Ordalarten  s.  SBE.  5,  iS,  57  im  Index unter  'Ordeal'.
22811:KompE.  —  Eig.  'Beglaubigung,  Erhärtung' des  Rechts,  der  Unschuld;  lum  V.  'var-,  — Vgl.   yvaroA:    —    mp.  (Pü.)   z«ir  'Ordal'.    —
22813:Ordals  gemeint.
22814:•  j.  ^varah-  Adj.  (auch  fem.)  'beim  Ordal verwendet,Ordal-';  urva%qmäti.%d^ zbayemi avi  imatvarS{%A.^uzd3t>m.. avi  raoynyqm 'ranhim  (AS£)  ". .  zu  der  Ordalbutter" Yt  12.  z*\
20024:der  (tierischen)  Eingeweide:  ya^  antar» vfrüika  *as  'ja  "was  zwischen  den  Nieren sitzt,  (näml.)  M."  V.i6:joPuZ.'\
23649:•  j.  varaSka-,  '''varatka-'J  m.  Du. 'Nieren':  yat  antarf  'ka  *as  manja  (sd.) V.  18.  70  PüZ.;  —  *-ka  F.  Jg».
5348:•  j.  ar«m,  g.  arvm  Adv.  'recht,  passend, wie  sichs  gehört':  y3cä  alä  arttau!  °r}m *vaiidyäiisd.)\.44.S;—'KimF.y.  a)  mit V.  'man-  und  Dat.  der  Pcrs.  'so  denken, wies  einem  recht  ist'  sva.  'ergeben  sein': yastä  da!i'3ng  aparS  masyqscä  tarS.mqstä ySi  Im  tarS.mainyanta  anySng  ahmlt  yS Aoi  'rSm  mainySii  "wer  danim  kUnfÜg die  Daiva  und  Menschen  missachten  wird, die  ihn  (den  Saoiyant)  missachten,  die andern  (alle)  ausser  den,  der  ihm  ergeben ist"  Y.  45.11.  b)  adjektivisch"  'füg- sam, gehorsam',  mit  Dat:  nSit  urvsha (sd.)  dätinbyas^  iarapanS  väsiräi  'rfm "den  Geboten  und  Satzungen  fdr  die  Land- wirtschaft" wollen  sich  dieÄ",  nicht  fUgen"
7542:•  j.,  g.  ä-zutay-  f.''  'Fett,  Schmalz':  raoy- nyqtn  i'aranhim  "suitlmca  urvaranqm  Yt. /2.3.  a)  überhaupt  sva.  'feste  Ndirung' gegenüber  der  flüssigen,  im  Gegensatz  zu ' xsi'td-  'Milch' :  pars  xsvisät  (sd.)  -zaitUca  "  1 girii mal  V.  13. z8;  — xhioaica  'sBlayaEca  ■> ^.68.2;  —  t!m  'iSdiis'''  ahurB  mq%r)m tasal  .  .  mazdä  gavei  xhildimcil  *ki'B.- umiaHbys  spmt3  säsnayä  "das  Wort  vom Fett  hat  AhM. ..  für  das  Rind  geschaffen und  die  Milch  für  die  Nahrung  begehren- den durch  sein  Gebot,  der  heilige"  Y. 29.71'.  a)  Du.  in  Verbindung  mit  xhild- Du.:  xsviöa  'zütH  yazamaide  .  .  ilzSis  .  . hamsistri  \.i6.8.  2)  'Üppigkeit,  strotzende Kraft  und  Fülle':  vaKuAlm  'zBülm*^  . . frasasttm  .  .   *p3r»ndlm  yazamaidl  Y.jS.
12953:1)  'festbinden,  fesseln':  apq^  (sd.)  gavs dam^äti  Ytro.48.  a)  Des.  '(Satzungen) aofirecht  erhalten,  (daran)  festhalten  wollen' ; aväU  urvamis  (sd.)  ya  tu  dldsrdö  (aS.)'' maa£i  Y- 4^.15,         S.  noch  dimanB.'.
25230:•  g.  razaii-:raÄ-''  n, 'Ordnung,  Satzung': yS..drlta  ayatOim  urvatBif{sd.)..hutSntui .  .  rainH  (IS.)  fvas  yS  aiavä  drsgoanttm
25677:•  g.  urväta-  d.  'Bestimmui^,  Gebot'; a)derGfitter:  %waAyä  matää  qstä  Uahyä "aus  Feindschaft  wider  dein  Gebot,  o  M."  j Y.  J4. 8  ■>;  —  hyat  tä  Uä  sasa^a  (sd.)  j-ä mazää  dadat  ^.30.  ii'^;  —  ta  v!  'tä mannte  . .  sfnghamahT  "eurer  Gebote  ein- gedenk . ."  Y.31. 1  "j  —  aväts  'täfi  yä ts  matää  dfdarizS  "nach  jenen  Bestim- mungen, an  denen  du,  o  M.,  festhalten willst"  Y. 44..  IS-  b)  der  Drug:  asibyS ySi  •läii  drüjS  .  .  vlm^rmcaia  (sd.)  Y. 31.1.
25679:•  g.  urvätay-  f.  'Gelübde':  y7  va  xlayqi aäqs  drtta  ayantpm  'ISil  vä  huzSntus  mt- hrsiiys  vä  ramä  jvqs  yS  asavä  dngvan- tfm  "wenn  ein  wissender  einen  zu  halten vermag,  nachdem  er  ihn  dazu  gebracht hat,  von  seinem  Gelübde  und  seinen  Bin- dungen weg  (zu  ihm)  überzugehen,  einer der  nach  der  Satzung  lebt,  ein  .i^ntanhänger einen  Druggiuos&en"  Y.46".  5.
25688:•  g.  urvlS^-  f.  'Gebot,  Bestimmung' nsit  *%a  däßibyasiä  karapanö  västrä^ aT7m  (Sp.  18S  u.)  Y.51. 14.
2761:Z  verlangen,  dass  er  (dem  Freund)  Schutz gewähre"  Y.  7/.  13,  a)  statt  des  praed. Akk.  ein  Adv.:  yimS  avai^a  ktrsnaot yaia  dim  Ual  ahurö  mazäi  "V.  tat  so, wie  es  AhM.  von  ihm  verlangte"  V.  2. 31.  4)  spez.  'zu  hören  verlangen,  hören wollen':  ^J  tsi  asä  yi  asäi gius  ia/.i  (sd.) mraot  is3ntl  tnä  tu  isi  vohB  manaaAl "was  ,  .  kund  getan  hat,  hören  wollen  sie dasdurchdeinenKji/."  Y.4Ö.9.  a)  ohne Ob],":  at  tä  vaxfyj  is?ntd  "ich  will  davon reden  zu  denen,  die  hören  wollen"  Y. _jo.i;  47-6*>;  — yalüä  asnat  yaila  anrät (sd)  isa:iä  Y.  45- 1-  5)  'Jemand  (Akk.) angehen,  sich  an  ihn  wenden,  ihn  bitten': ise  'i/wqm  aAura  mazda  ptrsst  '^wqm  . . Yt  12. 1 ;  —  *yas»  tat  *afivataiti  (sd.) paranlarfm  (sd.)  isöit  N./2;  —  vayö  .  . harn  istmmm  painyätte  ".  .  stellt  sich ein  bei  dem,  der  sich  (an  ihn)  wendet" Yt-/>S3;  —  al  yastim  nsii  na  is7mnS (inpass.Bcd.)9*Jj'i7/(sd.)Y.4ö.6.  a)  mit Inf.:  amslacit  .  .  avaiahe  isinli  masya- kanhs  "die  ^Ienschen  bitten  die  Am.  um Beistand"  Aog.  41.  6)  'Jemand  (Akk.) angehen  (in  feindlichem  Sinn),  angreifen, nachstellen';  avae^amai  ^iff  pantö  yim isfnli    mi^röjiruiS  Yt.  io.45.  7)    'er-
3160:•  j,  a-£i9'öiri§ta-  Adj.  'nicht  durch  Busse zu  wenden,  unsiihnbar':  *paoirya  *vtträa (LS.)  asSqm  syaoian)in\c(i\  'tjm  "schon wenn  sie  sie  zum  ersten  Mal  begehen, ist  ihre  Tat  nicht  mehr  zu  sühnen"  N.  23.
4797:mit  aoi  und  paiti  'zurückkehren,  sich zurückwenden  gegen  -  (Akk.)':  yö  tayui ..  tsm  aoi  ibaiSa  pattyantv  ..  t'hyeja yatitu yS  t  daoa  "wer..,  gegen  den  zurück  sollen sich  die  Feindseligkeiten  wenden,  . .  sollen sich  die  Gefahren  wenden  (gegen  den,) der  sie  hervorgerufen  hat"  Y.  65. 8.
5259:mit  paili  'sich  feindlich  wenden,  auf- treten gegen  — '  (Akk.) :  yS  mä  dr»gvä  %viä savä  (sd.)  paitianti  \.  44.12  '";  —  'paiii.- inta-,  s.  ap°;  —  s.  noch  Inf.
10049:wenden,  begeben  zu  — ';  a)  mit  Akk.: yezua  äpS  vaauAls  hansnüm  vayoanifm pourum  paitiJasaitiY.S.^i;  —  nqmistahyä mmatikä  iiS  mazi^täi  yär>Aqm  failljamyä Y.36.2  (zit  Y.5d'.7);  a;  —  asaya  tie*paill.- Jamylt  Y.  7.  24;  —  käu  .,*nx'iB.vaht9hqm uxoB.vaiashmö  paiü.jasat  *dritümla  dri- vtmla  T.26;  2.V»  b)'niit  Dat.:  xM- aaScii  azütaya^ca  mSvayaca  zaoire  paiti.- jamyä  Y.flS.a;  —  akmät  iaAmSiät  {&d.) naimanqm  .  .  paiti.jasaiti  ütarf  V.  8. 80,  c)  mit  Akk,  und  Dat;  taota{sA) *syaoi/iSJäitya  *häva7taHbya  faitt.ja»- hsit''i>  *iavaiian3  gatüm  ".  .  soll  sich zum  Mörser  begeben  auf  den  Platz  . ." N.A'/.
18406:•  j.  ßuß-'J  f.  'Käse':  nSiipayS  °/a'^  sao'kre tiSit  gSui  zao%re  bansmaine  palH.baire "nicht  darf  man  (von  dem  Rind)  die Milch,  den  Käse*'  beim  Z.  verwenden, nicht  das  Fleisch  .  ."  V.  7.  77;  *F.y3).
20468:•  j.  '*'m^0'r«in.sp9iit«[n.baeSaza-*)  Adj. 'der  mit  dem  heiUgen  Wort  heilt,  kurirt': tim  ihra  AanjasätUe  yat  'tarn  "sie  sollen sich  an  den  wenden,  der  . ."  V.  7. 44.
21858:•  j.  yütö  Inf.  'zu  verwenden,  zu  gebrau- chen, in  Gebrauch  zu  nehmen'",  praedi- kativ  gebraucht:  pasca  %rixiaparat  y gatus  y  x^ar;/^a  y°  vastra  y  anya^byB mazdayasnatibyB  "nach  drei  Tagen  sind Lager,  Speisen  und  Kleider  fiir  die  übrigen M.  verwendbar"  V.5.  55.
24144:•  j.  vi-tbaeäah-  Adj.  'gegen  die  Anfein- dungen (der  Datva  usw.)  gerichtet,  sich wendend;  sie  abwehrend':  aityaman^ni i!tm  , .  amavanfym  vprf^rä/an^m  'iatthtm Y.  54. 2,  G.  J.  6.
25554:i)  'sich  drehen,  kreisen':  lainm  (sd.) Aaraihyä  . .  yat  ml  aiwitS  urvis)nti^^  sta- rasiam  äsca  Avanca  Ytja.as,  2)'sich wenden,  umkehren':  in/a  mi  urvisyatim "zurüclc  wendeten  sie  sich  beide"  Yt. ig.  83.  3)    Kaus.    a)    'sich    wenden
```


## [2026-10-17T00:02:23.988Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"'wählen|glauben\" BRT.txt | grep -E \"var-|ver\" | head; grep -n -E \"varat-|varət-|'sich drehen\" BRT.txt | head; for l in 22809 25677 23649; do awk -v l=$l 'NR<l && /^[0-9]{3,4} *$/ {c=$0} NR==l{print l, \"col~\", c}' BRT.txt; done"
}
```


### [2026-10-17T00:02:24.487Z] TOOL RESULT

```
6951:•  g.  abmä.rafsnab- Adj.'uns  (den  Priestern) treu  ergeben,  unsres  Dienstes  beflissen"': d3idr  al  tarqs  asSunS  aiacinanhö  aidyüf västrySng  dar>gäi  izyäi  bizvaitl  haxmaim aktnaibyä  'ttatshs  "mach,  dass  die  Ritter glauben  und  nach  dem  Aia  verlangen, dass  die  Bauern  tUchtig  werden  zu  dauern- der eifervoller  fester  Genossenschaft,  für uns  (aber)",  dass  sie  (beide)  uns  treu  er- geben seien"  Y.40.3.
19731:tSm  Vi  ala  mjAmaiäl  *htiJtaxaim  (sd.)  Y. 4lS-  ij;  —  sptutjm  ai  %wa  maxdä  nOngkl oAwa  hyat  . .  "als  den  Heiligen  erkannte ich  dich  da,  o  AfAi^  als  . ."  Y.4j.  5; —  atfmcti  akyä  masda  ^wam  mfAAr foMtrDim  vaBi»m{sA.)  Y.2g.  10;  —  matdä yasmmla  vakm^mcä  vafditim  amshmaidl (Angm.)  Y.J5.  7;  —  Xmatyi^  ..  avaiya pama  *^adayä^  (ad.)  ^a*  mana  kartam mailitn  vamavätaiy  tlurvxtam{sA^  *mam- yataiy  Bh.^8; — pass.:  lUAi  aysm  angrS (sd.)  *maüiyae(Kony)  Y.  44. 1 2,  a)  zum praed.  Aide  tritt  der  In&nitiv  'sein':  al ^wä  m^hJ^paaurvlm  .,*yaxüm{sA.)  stSt manaifÄa  Y.JJ.S.  6) Med. 'sich halten fQ[  — ,  sich  voilcommen  wie  — ,  sibi  videri' mit  piaed.  Nom.  eines  Fait  sva.  'glauben, vermeinen  zu  — ':  nmati^m  hs  mariyaZla paraJahlf  "der  mag  ein  Haas  zu  ver- schenken glauben"  V.  /<?.  a8;  — yS  *main~ yäU'^  davayänti  (Sp.  680  o.)  ^rava- n^mta..  Y.i0.i$;  — yS,.na^a  mai^ett jaynvä  "der  . .  und  nicht  geschlagen  zu hai>en   vermeint"   Yljo.  71.  7)    mit
28320:•  j.  'zraz-dä-  kompV.  'vertrauen,  glauben'. Praes.  i  zrazda-.  —  Inf.  *sraiäatai-ia.
28334:•  j.  *zrazdätae-i-a "  Inf.  'zu  vertrauen auf—,  zu  glauben  an  — ':  yamaheca  hapia-
22809 col~ 1365
25677 col~ 1541
23649 col~ 1419
```


## [2026-10-17T00:02:29.884Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"vartati|vartate|'sich wenden|vart-\" BRT.txt | head; sed -n 22811p BRT.txt | cut -c1-400; grep -n -E \"^•  [gj]\\.  ['*]?var-\" BRT.txt | head"
}
```


### [2026-10-17T00:02:30.270Z] TOOL RESULT

```
24997:Richter,  Schiedsrichter'"  von  dem,  der beim  Gerichtsverfahren  —  im  Gegensatz zum  Gcrichtsherm  ('aAß-)  -  das  Urteil schöpft  und  verkündet;  a)  im  gAw;.;.. neben  'o//S-:  nSit  ainä  ahü  (sd.)  vists naida  'lui  aiatclt  hacä  Y.25.6;  —  neben 'ahura-.  Aakä  tBi  gavBi  'iuP''  hyal  . . da/ii  .  .  'iwax/j  (sd.)l  ifm  kst  uslä  (Sp. 1382  m.)  akunm  y7 . .  aiif/wm  {sA.)  vada- y~'i/?  "hast  du  einen  Richter  für  das  Rind, auf  dass  . .?  Wen  bestimmtet  ihr  ihm  als Gerichtsherm,  der . ,"  Y.  2g.  2.  a)  ins- bes.  von  Zardi:ustra  als  dem  Richter  bei der  Resurrektion;  *ydhä  *iiil  thä  vart- SaiU  .  .  'tBs  (NS.)  lyaöianä  ratists  (sd.) drsgvataicä  hyatcä  *asaom  Y.33.  i;  —  at vä  vTspSng  aySi  yaiiä  (Sp.  124S  o.)  'tum ahurS'^^  vawdä  masdä  ayS  qsayl  (sd.)  Y. 31.  z.  S.  noch  Y.  27,  13  unter  b  a a.  b)  im  jAw.  (unvollständig);   hier
25554:i)  'sich  drehen,  kreisen':  lainm  (sd.) Aaraihyä  . .  yat  ml  aiwitS  urvis)nti^^  sta- rasiam  äsca  Avanca  Ytja.as,  2)'sich wenden,  umkehren':  in/a  mi  urvisyatim "zurüclc  wendeten  sie  sich  beide"  Yt. ig.  83.  3)    Kaus.    a)    'sich    wenden
KompE.  —  Eig.  'Beglaubigung,  Erhärtung' des  Rechts,  der  Unschuld;  lum  V.  'var-,  — Vgl.   yvaroA:    —    mp.  (Pü.)   z«ir  'Ordal'.    —
```


## [2026-10-17T00:02:37.066Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^\\*?u̯ar|^\\*war|^\\*u̯art|\\*u̯art-|\\*u̯ar¹|choose, believe|to turn\" CHEUNG.txt | head -30"
}
```


### [2026-10-17T00:02:37.437Z] TOOL RESULT

```
3395:‘to turn, move’, Carag “pasture, grazing’, Kurd. (Kurm.) čērīn/čēr-, Zaz. Cérayis/ 
7676:*gar? ‘to turn, wind’ 
7682:? micyyr- ‘to turn intr.], be(come) curved’ = Samadi: 83 Ё; 85; 50 
7694:yeyron (caus.) ‘to let it turn, revolve’, Wa. yir-/yird ‘to turn (into) [intr.]’ 
8027:© The root seems to be an "enlarged" root, i.e. *so-formation, of *gar? *to turn, wind'. 
8055:*gart ‘to turn’ 
8070:develop’, LKh. *hamggeils- (hamge’-) ‘to turn’. Ф The LKh. forms, gai’sättä, etc. 
8084:-(g)il- ‘to go about, wander’, Fariz. -gälä-/-gäl-, Ham. gärdayän/gärd- ‘to turn’, bär- 
8088:Meim. bem-garn-/a-gern- ‘to turn (a)round, change, alter, etc.’, Awrom. geinay/ 
8089:geh- ‘to turn over; relate’, Abyan. gelloya/gell-, Abz. gelowa/gel-, Qohr. gelada/gel- 
8090:‘to turn [tr.]’ Yzd. (Zor.) gisnudvun, gisnddvun ‘to turn’ 
8093:quietly’, Ishk. yurs- (inch.) ‘to turn’, Sariq. yirs-/yerd ‘to revolve, go round, cross a 
8864:*MISC: ? Orm. Sar-ék ‘to turn, revolve’ 
13976:171), ‘to turn hither’ (Insler, Gäthäs: 259), *entourer (Kellens — Pirart I: 157). Humbach, l.c. also cites a 
14134:*Huarj ? ‘to turn, lay around ?’ 
14151:*SANSKRIT: varj ‘to turn (around), lay around’ (RV+) = EWAia П: 516 
14157:(cf. IEW: 1154 f.). The Skt. root varj goes back to IE *H;uerg- ‘to turn (around)’, 
15383:*SOGDIAN: CSogd. qmp- (f.) ‘strategem, ruse’ || (+ *apa-) BSogd. pk’np- ‘to turn 
16273:*CHORESMIAN: kncy- ‘to turn (one’s head)’ || (+ *ham-) ? m/nkn- ‘to sow’, "nknc (Ё) 
16854:*NEIR: Yghn. mayd- ‘to curdle’, Wa. moö-, mod-/mo6t- ‘to turn sour, curdle’, Oss. 
16858:Sariq. патиӨ-/патиӨ ‘to turn sour’, Khf. nimöö ‘cream coagulated in a trough’, 
18813:*naj ? ‘to turn, roll’ 
18825:*NEIR: Sh. noy-/näyd, Rosh. noy-/néyd ‘to turn, whirl [intr.], wander about’, (caus.) 
18826:Sh. näy-/näyd, Rosh. niy-/niyd, nayén-/nayént ‘to turn round’, Sh. ndyijak, Khf. 
18829:dish, raise one’s hand (against)’, (Baj.) barnäy-/barnäyd ‘to turn, twist around some- 
18830:body/something' || (gil- < ?) Sh. gilnäy-/gilnäyd ‘to turn, wind’ 
20532:*MISC: Par. ram-/rami ‘to go round’, (caus.) Par. rém- (supplet.?) rhant ‘to turn’ 
23193:*AVESTAN: YAv. sri- ‘to lean’ || (+ *apa-) ‘to turn away from, averse from’ || (+ 
24368:Yzgh. tozan-/tazant ‘to turn, whirl’, Sh. (Baj.) täz-/täzd, Rosh. téz-/tézd, Bart. toz-/ 
24592:*NWIR: NP tanidan/tan- ‘to turn, spin’, Kurd. (Sor.) tan- ‘to braid, weave’, Gz.
```


## [2026-10-17T00:02:45.787Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 8050,8115p CHEUNG.txt; grep -n -E \"choose|believe\" CHEUNG.txt | head -20"
}
```


### [2026-10-17T00:02:46.128Z] TOOL RESULT

```
a Skt. correspondence, cannot be ascertained. => LIV: – | Pok.: 439 f. 
*REFERENCES: EVP: 10; IIFL II: 211a, 212a, 189a; Werba 1997: 181; NEVP: 31,8 


*gart ‘to turn’ 

*MIDDLE PERSIAN: MMP grd-, BMP glt- /gard-/ ‘to revolve, tum; to become’ 
c DMMPP: 163b 

Pres.: IND. 35р. BMP gltyt /gardéd/, 3р1. MMP grdynd; Partic.: pres. MMP grd'g; Inf.: caus. MMP 
grdynydn 

*KHOTANESE: OKh. ggal- ‘to lie about’, ggei("I)s- ‘to revolve, return’ || (+ *pati-) ? 
LKh. pajsith- ‘to store away’ || (+ *ham-) *hamggad- (hamggal-, hage-) ‘to result; 


*garz 111 


develop’, LKh. *hamggeils- (hamge’-) ‘to turn’. Ф The LKh. forms, gai’sättä, etc. 
‘he returned’ appears to show contamination (< ? *ggei’sätä + atá) according to 
Bailey (apud SGS: 31). The reconstruction and etymology cited by Emmerick (SGS: 
66) for LKh. pa-jisth- (< *pa-jar@ia-), MMP gys-/gyst-, Pash. yaral ‘to twist, spin’ is 
dubious. > SGS: 31, 66, 136, 138 

*CHORESMIAN: yrcy- ‘to roll; to get rid of; to smear with clay’ || (+ *ati-) cyrcy- (tr.) 
‘to roll down (a stone)’, cyrd (intr.) ‘to roll down’; ? m/ncyrcy- ‘to gin (cotton) (with 
n- < *ni-?) © Samadi: 79, 49, 119 

*NWIR: Widely attested: NP gastan/gard-, Tt. (Esh.) gard/gahast, Anar. getäye/gert-, 
Meim. be-gardaj-/a-gerd-, Tr. gela(yaygel-, Varz. gartäye/gart- ‘to become, turn’, 
NP gardidan (< *uart- ?), (Tadj.) Selidan ‘to roll’ (LW, cf. Yghn. yil-), Abyan. va 
gelloyan, Gil. (Rsht.) va-gärd- ‘to re-turn’, Awrom. geläy/get-, Gur. (Kand.) git-/ 
-(g)il- ‘to go about, wander’, Fariz. -gälä-/-gäl-, Ham. gärdayän/gärd- ‘to turn’, bär- 
gardayän/bär-e-gärd-, Isfah. ve-gärtän/ve-gärt-, Natan. va gola ‘to re-turn’, Mah. 
gird- ‘to walk (around)’, Nn. girta-/girt- ‘to become, be; to go round’, Siv. gir(1)-/ 
girià (+ va) ‘to return’, NP gardänidan/gardän- (sec. caus.), Jow. bam-gerna/a-gern-, 
Meim. bem-garn-/a-gern- ‘to turn (a)round, change, alter, etc.’, Awrom. geinay/ 
geh- ‘to turn over; relate’, Abyan. gelloya/gell-, Abz. gelowa/gel-, Qohr. gelada/gel- 
‘to turn [tr.]’ Yzd. (Zor.) gisnudvun, gisnddvun ‘to turn’ 

*NEIR: Pash. yaxt-/yar- ‘to twist, spin, turn’, Yghn. yil-/yilta ‘to roll; to flow 
quietly’, Ishk. yurs- (inch.) ‘to turn’, Sariq. yirs-/yerd ‘to revolve, go round, cross a 
pass’ (LW ?), ? Sangl. yart-, yort-/yost ‘to walk about’ (< early NP ?), ? Wa. 
Ysırt-/Yort- ‘to gather; to roll; to heap’ 

*MISC: Orm. gal-/galök ‘to weave’ = gal-/galök, galaw-/galawok 

9 The Ir. root with no exact IE correspondences seems to be an enlarged root of 
*gar”. It has probably been influenced by *yart. 

*PIE — = LIV: - | Pok.: 385 

*REFERENCES: КРЕТ. 83b, 142a, 145a; EVP: 27 f.; IIFL I: 394b; КРЕП: 219; Christensen, Contributions: 
I: 60, 166, 256; IIFL II: 524, 395a; Abrahamian 1936: 108, 133; Lambton 1938: 41b f., 78b; Andreev — 
PeSéereva: 258a; MacKenzie 1966: 95; Yarshater 1969: 182; EVS: 37а, 60b; Lecoq 1974: 60; WIM III: 


108; Steblin-Kamenskij 1999: 191; Lecoq 2002: 122, 125, 127 (etc., passim); Vahman — Asatrian 2002: 
25; NEVP: 32; Kiefer 2003: 196 


*garz ‘to lament, weep’ 

*AVESTAN: goroz- ‘to lament, weep’ => Liste: 19f. 
504:admittedly subjective, but I believe this is preferable to a long catalogue of meanings 
2898:*AVESTAN: Av. caii- ‘to heap up, gather’ || (+ *ui-) ‘to select, choose’ || (+ *ham-) ‘to 
2910:(past stem) ‘to choose” = DMMPP: 132, 283a, 240a, 337b 
2916:(+ *ш-) wZyn- ‘to choose’ = Ghilain: 85 | DMMPP: 132a, 240a, 338 
2924:‘to choose, select’ 
2952:‘bramble’ || (+ *ui-) NP guzidan/guzin-, Bal. gicint/gicin- ‘to choose, select, elect’ 
2955:‘to pick, choose’ (< *ёіпџа- ?), M. Cin-/Einoy- ‘to build a wall’, cinv- ‘to collect; to 
3404:&vzurst ‘to pick out, choose; to separate [etc.]" (v. *yar(H)'), pace Cabolov, l.c. 
15884:ingastan/ingar- ‘to suppose; consider, believe’, angaridan/ angär- ‘to think, imagine, 
16934:‘to contemplate, consider, believe’ || (+ *fra-) frm’y- ‘to order’ || (+ *ni-) nm’y- ‘to 
17407:*NWIR: Qohr. münoya/mün- ‘to believe’, man ‘mind, character’ || (+ *ui-) NP guman 
17413:*SANSKRIT: man ‘to think, believe, consider’ (RV+) = EWAia II: 305 
17420:do-moin- ‘to think, believe’, Lith. mifiti ‘to remember, recall’, Goth. man ‘to think, 
17423:believe’, Engl. to mean, mind, etc. 
19154:*pair ‘to believe’ 
19156:*KHOTANESE: pir- ‘to believe’, pirättäti- ‘belief? = SGS: 84 
19157:*SOGDIAN: BSogd. pyr-, CSogd. pyr- ‘to believe, trust’ 
19167:*MISC: Toch. (LW) perak ‘believing’ (7 BSogd. pyr’k ‘believer’, Isebaert 1980: 160, 
25831:away; to choose’, Yghn. cos$- ‘to spread, scatter, sow’ 
26458:*MIDDLE PERSIAN: BMP wyc- /wéz-/ ‘to sift, select, elect, choose (etc.); separate’
```


## [2026-10-17T00:02:53.409Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^\\*(y|u|ц|w)ar[a-zH0-9¹²³'’]* \" CHEUNG.txt | head -20; grep -n -E \"^\\*(y|u|ц|w)art\" CHEUNG.txt"
}
```


### [2026-10-17T00:02:53.844Z] TOOL RESULT

```
27146:*uar 419 
27179:*uar ‘to turn’ 
27221:*yard ‘to drag, to put in pieces ? 
27344:*yarHz ‘to (make) grow, nourish, be brimming with’ 
27387:*uart 423 
27441:*yart ‘to turn’ 
27507:*uarz 425 
27553:*yarz ‘to do, work, till the land’ 
55346:*uarHz 
55368:*yarHz (s.v.), *zars', *zaus 
56147:*yar 
56470:*yarHz (s.v.), *zars', *zaus 
57108:*uarHz 
57500:*uarc 
57535:*yarHz (s.v.), *zars', *zaus 
58228:*yarz 
27387:*uart 423 
27441:*yart ‘to turn’ 
58248:*yart, *urais
```


## [2026-10-17T00:02:56.734Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27060,27220p CHEUNG.txt; sed -n 27387,27506p CHEUNG.txt"
}
```


### [2026-10-17T00:02:57.122Z] TOOL RESULT

```
13.154 Ё), OPT. 3sg. YAv. vaoniiat (Yt 13.13); Partic.: pres. YAv. vanant-, med. (+ priv.) ҮАУ. 
auuanomna- (Yt 1.8, Yt 8.55, Yt 13.133, etc.), fut/aor. {1} ? YAv. vanhant- (Yt 13.155), perf. YAv. 
vauuanuuah- (Y 57.12), ? Y Av. *vaonus- (Yt 13.155); Desid.: pres. IMPV. 35р. OAv. viuuenghatü (Y 
53.5) 

*OLD PERSIAN: 9 On OP avaniya see *HyanH. 

*MIDDLE PERSIAN: MMP w’n-, BMP w’n- /wan-/ ‘to conquer; attack” = DMMPP: 
335b 

Pres.: IND. 1sg. BMP w’nwm /wanum/, SUBJ. 3р1. MMP w’n’nd, IMPV. 2sg. MMP win Partic.: pres. 
MMP w’n’g ‘conqueror’, perf. pass. BMP w’nyt /wanid/, MMP w’nyst, Inf.: BMP w’nytn /wanidan/; 
Pass.: pres. IND. 3sg. BMP w’nyhyt/wanihéd/, 3р1. MMP w’nyhynd 

*SOGDIAN: SSogd. wnw- ‘victorious’ PN, CSogd. wnwngy’ (f), SSogd. 
wn’wn’ky’kh ‘victory’, CSogd. wnyqcyq ‘captive’, MSogd. wnwnyy ‘victorious’ 
*BACTRIAN: ocvtv6- in place and personal names = S-W, Bact.: 209b 

*NWIR: Siv. vin(1)- ‘beating’ (in vin(i)-d-/vin(i)-da ‘to beat’) 

*NEIR: Oss. I. waendyn ‘to dare, be bold, decide’ (< *wand(&) wyn ‘to be trium- 
phant’) || (+ *ham-) Oss. I. ewweaendyn, D. ewweendun ‘to (en)trust, believe’ 


418 *ua(n)é 


*SANSKRIT: van ‘to win, conquer’ (RV+) = EWAia II: 499 
«PIE *uen- ‘to win, conquer’ = LIV: 680 f. | Pok.: 1146 f. 


*IE COGNATES: OHG gi-winnan ‘to win, to get’, OE winnan, Engl. to win, etc. 
*REFERENCES: Abaev, Slovar’ I: 215 f.; WIM 1988: 119, 350; Sims-Williams — Hamilton: 75, 87; Abaev, 
Slovar' IV: 85; Werba 1997: 232 f. 


*ua(n)é ‘to stagger, shake ?' 

*AVESTAN: OAv. vaš- ‘to erupt, well up ?'. © The interpretation of this hapax form is 
uncertain. Humbach 1956: 75 (recently repeated in Humbach 1991 II: 155) 
translates it as ‘to well (up)’ ("wogen") comparing it to Skt. RV vacyáte ‘issues 
forth’ (< vañc), whereas Insler, Gathas: 247 ad 44.11 considers it a passive 
formation of vac corresponding to Skt. ucyate ‘is taught! (< oc). Insler's 
interpretation is formally difficult, especially because the Ir. cognate root of Skt. oc 
has acquired a secondary *j- (*jauc), not to mention the fact that the expected Av. 
correspondence would be *usiiaté On the other hand, Humbach’s translation is 
semantically unsatisfactory: how can daéna, the subject of vasiiete, "stagger" on, if 
we keep the Skt. connection (which is semantically compatible with the other Ir. 
forms) ? Obviously ‘to well up, vel. sim.’ is just a stylistically more acceptable 


interpretation of ‘to stagger’. = Liste: 50 
MED. Pres. ja-: IND. 3sg. OAv. vasiiete (Y 44.11) 


*CHORESMIAN: wc- ‘to swing, shake’ (rather from *uaij ?) || (+ *uz-) m/zwxs- ‘to be 
curved, be twisted’ || (+ *pari-) prwxs- ‘to embrace’ — Samadi: 211, 265, 156 
*NEIR: (+ *fra-) Oss. D. raewaexsun/rewexst ‘to shake, shiver; to have a seizure’ || (+ 
*ш-) Oss. D. iwaexsun/iwexst (inch. ?) ‘to sprain, wrench’ 

*SANSKRIT: vafic 'to totter, to go staggering (of a horse)’ (RV+) = EWAia II: 492 

9 An IE origin for this apparently Пг. root cannot be ascertained. The Germanic 
nominal forms, OE woh ‘crooked, wrong’, OSax. wäh (n.) ‘evil’, are frequently 
cited. 


*PIE — => LIV: 687 | Pok.: 1134 
*REFERENCES: Abaev, Slovar’ I: 559; Abaev, Slovar’ II: 391; Werba 1997: 232 


*yap! ‘to disperse, scatter" 

*AVESTAN: (+ *ui- OAv. viuuap- ‘to cut down [Insler, Gathas: 47.], plunder 
[Humbach 1991 II: 84], devastate [Kellens — Pat I: 120] ?’. % The interpretation of 
OAv. viuuap- is uncertain. The YAv. nominal form viuuapa- (Y 12.2 f., P 21), 
which is connected to OAv. verbal form, appears to mean ‘destruction, plundering 


vel sim.’. = Liste: 49 
Pres. them.: INJ. 3sg. OAv. viuuapat (Y 32.10) 


*MIDDLE PERSIAN: ? BMP w’py ‘sheaf (Ps.) 


*uar 419 


*NWIR: Nn. vave, Yzd. vova ‘sheaf’ 

*NEIR: Sh. wäb, Rosh. web (CL Orosh. wob, Yzgh. wab, Wanji web ‘sheaf’, Sh. 
wäbak ‘bundle, truss’, Yghn. wop ‘sheaf’, Yzgh. web ‘box for flour’ 

*SANSKRIT: vap! ‘to scatter, strew (out), spread (out)’ (RV+) > EWAia II: 503 

© The root is apparently IIr.: an IE provenance cannot be ascertained. 


*PIE — — LIV: 684 | Pok.: 1149 
*REFERENCES: EVS: 87b; Werba 1997: 418; Lecoq 2002: 639a 


*uap? ‘to shave’ 

*KHOTANESE: (+ *pati-) OKh. patävutta- ‘shaven’ (Z 2.12) 

*SANSKRIT: vap’ ‘to shave’ > EWAia II: 504 

0 The root *uap”, which appears to be continued in a single Ir. language, is likely to 
be originally identical to *yap’ ‘to disperse, scatter’. 

*PIE — = LIV: 684 | Pok.: — 


*IE COGNATES: — 
*REFERENCES: DKS: 206b 


*uar ‘to turn’ 

*AVESTAN: var- ‘to turn’ || (+ *pari-) “о turn around, pervert’ = Liste: 60 

Pres. {1} nu-: IND. med. 3sg. YAv. voronüite (V 18.35, V 18.41, V 18.47), 3pl. YAv. varanuuainti (Yt 
13.15), SUBJ. med. 35р. OAv. varanauuaité (Y 31.17), IMPV. 2sg. YAv. voronüiói (Y 9.28); Pres. {2} 
them. nu-: IND. 35р. YAv. pairi.voronauuaiti (Yt 14.41), med. 3р1. YAv. vorononte (V 18.32), INJ. 35р. 
YAv. voronauuat (F 420), SUBJ. med. 3р1. YAv. ham.varanante (V 5.59, V 7.5 Ё); Aor. athem.: SUBJ., 
IMPV. med. 25р. ? OAv. hàm *varosuua (Y 53.3); Caus.: pres. IND. 3sg. YAv. varaiieiti (V 19.29), 3pl. 
Y Av. “varaiieinti (Yt 14.5), IMPV. med. 2р1. YAv. pairi varaiiadBom (Yt 1.27); Intens.: pres. SUBJ. med. 
3sg. OAv. vauraite (Y 47.6), OPT. med. 15р. OAv. vauraiia (Y 31.3), med. 1р1. OAv. vauroimaidi (Y 
28.5) 


*PARTHIAN: (+ *ni-) пута (pret. stem) ‘to sink, set in (of sun)’ = Ghilain: - | 
DMMPP: 248a 


Partic.: perf. pass. nwrd 

*CHORESMIAN: (+ *ni-) m/nwry- ‘to turn (away, down) [intr.]’, (caus.) m/nw’ry- ‘to 
turn (away, down)’ = Samadi: 133 f. 

*NWIR: (+ *uz-) Zaz. zivirnayis/zivirnen- (sec. caus.) ‘to turn around, let circle’ 
*NEIR: Yghn. wer-/wérta, M. war-/wusk (Zarubin) ‘to stretch the warp on the loom’, 
Yi. wor-/wus£- ‘to knit’, wor-/wisc- ‘to weave (?)’ || (+ *ni-) Yzgh. nowir/nowüg 
‘to set [of sun]’ 

*SANSKRIT: ? val ‘to turn’ (late). Š It remains uncertain whether the late Skt. root val 
is a continuation of IE *uel- ‘to turn’ or a popular development of Skt. vart, cf. 
EWaAia, l.c. = EWAia III: 460 

«PIE Zuel ‘to roll, turn’ = LIV: 675 | Pok.: 1140 ff. 


420 *пагё 


*IE COGNATES: Gr. € éco, Arm. gelum ‘I turn’, Lat. uoluö ‘Troll’ 
*REFERENCES: JIFL II: 263a; Andreev — PeSéereva: 352a; Edel’man 1971: 172 f.; Paul 1998: 320b 


*uart 423 


*CHORESMIAN: (+ *pari-) prwr- ‘to rear, nourish, feed’ (LW). © Not from the root 
*bar ‘to carry, bring’, *pari-bar, as suggested by Samadi. || The Chor. forms cannot 
derive directly from *pari-uarza-, which would have yielded **prwZ- in Chor., cf. 
MacKenzie 1983, l.c. They may well be borrowed from Persian instead. = Samadi: 
156 

*NWIR: Abz. varz ‘fertiliser, dung’ || (+ *pari-) NP parvardan/parvar- ‘to nourish, 
feed’, parvardegar ‘Creator, Provider’ 

*NEIR: Oss. I. warzyn/warzt, D. warzun/warzt ‘to love’ (< *‘to take care of, foster’) 
*SANSKRIT: ürj- (f.) ‘nourishment, refreshment, strength” > EWAia I: 242 f. 

«PIE *uerH)g- ‘to be filled, nourished, brimming with life (energy)’. > A laryngeal is 
reconstructed on account of the long vowel in Skt. ürj-. => LIV: — | Pok.: 1169 

*IE COGNATES: Hitt. /uarkant-/ ‘fat, fattened’, Gr. opge ‘I am getting ready to bear, 
growing ripe; I swell with lust’, оруй ‘natural impulse, temperament, disposition’ 
*REFERENCES: Henning 1965: 176, fn. 38; Abaev, Slovar’ IV: 53 f.; Lecoq 2002: 604a; NEVP: 92 


*yarS ‘to be hungry’ 

*MIDDLE PERSIAN: ? MMP gwrsgyh ‘hunger’? > DMMPP: 167b 

*PARTHIAN: wsynd, wsyynd ‘hungry; hunger > DMMPP: 348a 

*SOGDIAN: BSogd. ws’y-, CSogd. wš- ‘to be hungry’ 

Pres.: IND. 3sg. BSogd. ws’yt (SCE 29) 

*CHORESMIAN: m[w$y- ‘to be(come) hungry’, ’wsyk ‘hunger’ (477.5), ’wsynd 
‘hungry’ (412.7) = Samadi: 222 f. 

*NWIR: NP gusnah, Bal. gusnag (< NP), Gz. vässe, vesse, visse, Jow. vefa ‘hungry’, 
Abyan. vasa, Abz. veša, Anar. vase, Ard. veSe, Nn. vassa, Qohr. veša ‘who is 
hungry’ 

*NEIR: М. (w)usay-/(w)usyad- ‘to become hungry’ (Zarubin), Pash. wogay, Yi. 
wusi(y)aday ‘hungry’, Yi. wúšřyo ‘hunger, hungry’ 

*MISC: Par. yurcá ‘hungry’ 

© The root *uars/S- appears to be a kind of "Reimbildung" after *tar$ ‘to be thirsty’ 
(q.v.), cf. Hübschmann1895: 92; Samadi, l.c. 


*PIE — > LIV: - | Pok.: 
*REFERENCES: IFL I: 256b Ё; IIFL П: 264a; EVP: 95; Lambton 1938: 75b; WIM II/2: 749; Lecoq 2002: 
604a, 587a, 612b, 623b (passim); NEVP: 86; Korn 2005: 100, 127, 397 (passim) 


*yart ‘to turn’ 

*AVESTAN: Y Av. varat- ‘to turn’ > Liste: 51 

MED. (exc. Caus.); Pres. them.: INJ. 3sg. Y Av. varetata (F 8); Caus.: IND. 3pl. ? YAv. ham.varontaiionti 
(N 97) 


424 *yart 


«OLD PERSIAN: ? vart- ‘to turn’. 9 According to Gershevitch 1959: 184, OP 
<..-r-t-i-y-i-y> (DB 4.44) rather reads *vratiyaiy ‘I swear, take an oath’. = Kent: 
207 

Pres.: IND. 1sg. med. “vartaiyaiy OP <[v]-r-t-i-y-i-y-> (DB 4.44) 

*MIDDLE PERSIAN: MMP (intr.) wrd-, BMP wlt- /ward-/ ‘to turn; twist; writhe [intr. ], 
be tormented’, (caus.) BMP wit’n- /wardan-/, BMP wityn- /wardén-/ ‘to cause to 
change, turn, convert’ || (+ *uz-) ? MMP ‘zwrd- ‘to return to the body, be reborn; to 
turn back, revert, renege’ || (+ *ham-) MMP "mwrd- ‘to turn ёо’ = DMMPP: 344b, 
102b, 40b 

Widely attested: Pres.: IND. 1sg. BMP wltym /wardém/, 25р. BMP wityh /warde/, 3sg. MMP wrdyd etc. || 
(+ *uz-) Pres.: IND. 3pl. MMP ‘zwrdynd; Partic.: perf. pass. MMP ‘zwstg’n (pl.) || (+ *ham-) Pres.: IND. 
3sg. MMP ’mwrdyd, IMPV. 25р. ‘туга; Partic.: perf. pass. ’mwst 

*PARTHIAN: wrt-, wrd- ‘to turn, twist, writhe’? || (+ *a-) ’C)whr- ‘to turn to, be 
converted’ || (+ *uz-) ‘zwrt- ‘to turn back, return’ || (+ *ham-) ’mwrd- ‘to gather, 
collect, heap’ — Ghilain: 53 f. | DMMPP: 345a, 5b, 102b, 40b 

Pres.: IND. 25р. wrdyh, 3sg. wrtyd, SUBJ. 15р. wrt’n, 25р. wrt’h, OPT. wrdyndyh; Partic.: perf. pass. wst 
|| (+ *a-) Pres.: SUBJ. 3pl. "whr'nd, IMPV. 2pl. ’whryd || (+ *uz-) Pres.: IND. 3sg. *‘zwrtyd, 3р1. 
‘zwrtynd, SUBJ. 15р. *‘zwrt’n, 2sg. ‘zwrt’, ‘zwrt’h; Partic.: perf. pass. ‘zwst; Inf.: 'zwstn || (+ *ham-) 
Pres.: IND. 25р. "mwrdyh, 3sg. *’mwrdyd, 3р1. ’mwrtynd, SUBJ. 25р. ’mwrd’, ’mwrd’h, IMPV. 2sg. 
’mwrd, 2р1. 'mwrdyd, ’mwrtyd; Partic.: perf. pass. "mwst, II * ‘туга (short for *’mwrd’d, Sundermann 
1981: 151); Inf.: *mwrdn 


*KHOTANESE: OKh. bal- (bad-) ‘to move; writhe’, LKh. bith- ‘to writhe; twist’, LKh. 
*bei’ss- (bais-) ‘to make turn’ (*uart-s-aja-) || (+ *a-) OKh. äbeis- ‘to turn’ || (+ 
*ham-) LKh. hambith- ‘to retain’ > SGS: 92, 104, 100, 9, 142 f. 

*SOGDIAN: BSogd. wrtn, MSogd. "wm ‘carriage’ || (+ *apa-) BSogd. ’pw’rt, 
MSogd. pw’rt ‘to turn away’, CSogd. pwyrt- (caus.) ‘to turn away, estrange’ || (+ 
*а-) BSogd. "wirt MSogd. ’’wrt ‘to (re)turn’ || (+ *uz-) BSogd. ’zw’rt, BSogd. 
zw’rt, CSogd. zwrt, MSogd. zw(’)rt ‘to (re)turn’, CSogd. zwyrt, MSogd. zw’yrt ‘to 
cause to return, turn away, return’ || (+ *pati-) BSogd. ptw’rt ‘divergence, turning 
Y || (+ *pari-) BSogd. prw’rt, CSogd. prwrt, MSogd. prwrt ‘to turn, change, 
become’, (caus.) MSogd. prw(’)yrt ‘to turn, transform’, BSogd. prw’yrt ‘to turn, 
transform, covert, translate’ || (+ *ni-) MSogd. nwrt- ‘to turn’ 

(+ *apa-) Pres.: IND. 25р. MSogd. pw’rtyy, 3sg. BSogd. ’pw’rt || (+ *ä-) Partic.: pres. MSogd. "wrt 
(Sogd. Tales: 473); Inf.: BSogd. ’’w’rty || (+ *uz-) widely attested: Pres.: IND. 3sg. CSogd. zwrtt, SUBJ. 
159. CSogd. zwrtn, 3sg. CSogd. zwrtt, 3р1. MSogd. “zwrt’nd, OPT. 3sg. MSogd. zwrtyy (BBB: 49), 
IMPV. 2sg. SSogd. ’zw’rt, etc. || (+ *pari-) well attested: Pres.: IND. 3pl. dur. CSogd. prwrtntq; Impf.: 
IND. 3sg. MSogd. prywrt (cf. GMS: §624); az-Impf.: IND. 3sg. CSogd. prwrt’z; Fut.: IND. 3pl. CSogd. 
prwrtntq'm; Partic.: perf. pass. BSogd. prw’st-, MSogd. prwst-; Caus.: IND. impf. MSogd. prwyrt, etc. || 
(+ *ni-) Partic.: pres. MSogd. nwrtyy (Sogd. Tales: 473) 

*CHORESMIAN: ? wcy- ‘to braid’, wrd- (intr.) ‘to become’ || (+ *a-) m/’wrd- ‘to turn 


back, return’, m/’wrcy- (caus.) ‘to lead back’ || (+ *upa-) bwcy- ‘to propel’ || (+ *uz-)
```


## [2026-10-17T00:03:05.179Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27506,27552p CHEUNG.txt; grep -n -E \"^\\*uar[0-9¹²³]|^\\*yar[0-9¹²³]|‘to choose’$|to choose, believe|‘to choose|believe’\" CHEUNG.txt | sed -n 1,30p"
}
```


### [2026-10-17T00:03:05.603Z] TOOL RESULT

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


2910:(past stem) ‘to choose” = DMMPP: 132, 283a, 240a, 337b 
2916:(+ *ш-) wZyn- ‘to choose’ = Ghilain: 85 | DMMPP: 132a, 240a, 338 
2924:‘to choose, select’ 
2952:‘bramble’ || (+ *ui-) NP guzidan/guzin-, Bal. gicint/gicin- ‘to choose, select, elect’ 
15884:ingastan/ingar- ‘to suppose; consider, believe’, angaridan/ angär- ‘to think, imagine, 
16934:‘to contemplate, consider, believe’ || (+ *fra-) frm’y- ‘to order’ || (+ *ni-) nm’y- ‘to 
17407:*NWIR: Qohr. münoya/mün- ‘to believe’, man ‘mind, character’ || (+ *ui-) NP guman 
17420:do-moin- ‘to think, believe’, Lith. mifiti ‘to remember, recall’, Goth. man ‘to think, 
17423:believe’, Engl. to mean, mind, etc. 
19154:*pair ‘to believe’ 
19156:*KHOTANESE: pir- ‘to believe’, pirättäti- ‘belief? = SGS: 84 
27081:phant’) || (+ *ham-) Oss. I. ewweaendyn, D. ewweendun ‘to (en)trust, believe’ 
27239:*uar(H)! ‘to choose; convince; (med.) to believe’ 
27241:*AVESTAN: var- ‘to choose; to convince’ || (+ *fra-) ‘to choose’ — Liste: 50 
27249:*OLD PERSIAN: v(a)r- ‘to choose, convince’ = Kent: 206b 
27255:*MIDDLE PERSIAN: MMP wrw- (BMP HYMNWN-) ‘to believe’ = DMMPP: 345 
27259:*PARTHIAN: wrw- ‘to believe’ — Ghilain: 79, 85 | DMMPP: 345a 
27263:*SOGDIAN: CSogd. wrn-, MSogd. wrn- ‘to have faith, believe’ || (+ *ui-) SSogd. yw’r 
27270:*CHORESMIAN: m/wrw- ‘to believe’ || (+ *apa-) bw’r- ‘to separate oneself, diverge’, 
27290:*NEIR: Oss. I. wyrnyn ‘to believe’, Yi. war-/wat-, M. wet-/wetta ‘to separate’ || (+ 
27302:*SANSKRIT: var” ‘to choose, pick’ (RV+) > EWAia II: 511 
27328:verb, which means ‘to choose; to convince; (med.) to believe’. Perhaps, m/w’r-, 
27679:‘to distinguish, separate’ || (+ *ham-) hmwd- ‘to believe’ = Ghilain: 53, 96 |
```


## [2026-10-17T00:03:08.806Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27239,27343p CHEUNG.txt"
}
```


### [2026-10-17T00:03:09.100Z] TOOL RESULT

```
*uar(H)! ‘to choose; convince; (med.) to believe’ 

*AVESTAN: var- ‘to choose; to convince’ || (+ *fra-) ‘to choose’ — Liste: 50 

MED.; Pres. n-: IND. 1sg. OAv. varané (Y 46.3), YAv. vorone (Y 12.2, Vr 5.3), 3sg. OAv. varanté (Y 
43.16, Y 51.18), INJ. 35р. YAv. verenta (Yt 10.92), 3р1. OAv. voronata (Y 30.6), OPT. 35р. them. ҮАУ. 
fraoronaeta (V 19.2); Aor. athem.: INJ. 3sg. OAv. varata (Y 30.5, Y 32.12), OAv. frauuarata (Y 31.10), 
1р1. OAv. varomaidi (Y 32.2, Y 35.3), SUBJ. 1sg. YAv. frauuarane (Y 12.1, Y 12.8, VdPZ 9.32), 35р. 
Y Av. "frauaraite (ЕТА 5); Inf.: pres. YAv. vorondiiai (Vr 4.2) 

*OLD PERSIAN: v(a)r- ‘to choose, convince’ = Kent: 206b 

MED.; Pres. them. nu- IND. 3sg. v(a)rnavataiy <v-r-n-v-t-i-y> (DNb 23), impf. 35р. av(a)rnavatä 
<a-v-r-[n]-[v]-[t]-[a]> (DSf 17), SUBJ. 3sg. v(a)mavataiy <v-r-n-v-a-t-i-y> (DB 4.49), IMPV. 35р. 
v(a)rnavatam <v-r-n-v-t-a-m> (DB 4.42, DB 4.53) 

*MIDDLE PERSIAN: MMP wrw- (BMP HYMNWN-) ‘to believe’ = DMMPP: 345 
Pres.: SUBJ. 3sg. MMP wrw'd, OPT. 2pl. MMP wrwwyd; Partic.: perf. pass. MMP wrwyd, II MMP 
wrwyst-; Inf.: MMP wrwystn 

*PARTHIAN: wrw- ‘to believe’ — Ghilain: 79, 85 | DMMPP: 345a 

Pres.: IND. 3pl. wrwynd; Partic.: perf. pass. "wrw’d 

*SOGDIAN: CSogd. wrn-, MSogd. wrn- ‘to have faith, believe’ || (+ *ui-) SSogd. yw’r 
‘separation’, SSogd. yw’r, BSogd. yw’r, CSogd. yw’r, MSogd. yw’r ‘but, never- 
theless, except’ 

Well attested: Pres.: IND. 15р. CSogd. wrn’m, dur. CSogd. wrn'msqn, CSogd. wrn'msq, 2sg. dur. CSogd. 
wrnysqn, 1р1. CSogd. wrnymsqn, etc. 

*CHORESMIAN: m/wrw- ‘to believe’ || (+ *apa-) bw’r- ‘to separate oneself, diverge’, 
bw’ry- (caus.) ‘to separate’ || (+ *upa-) ? bw’ry- ‘to select’ || (+ *ui-) yw’ry- ‘to 
know, experience, understand’. ó Rather than putting Chor. bw’ry- ‘to select’ and 
bw’ry- ‘to separate’ together under a single entry (as done by Samadi), we may 


*yar(H)2 421 


distinguish two differently prefixed formations, viz. with the pref. *upa- and *apa- 
respectively. > Samadi: 217, 29, 258, 208 f. 

*BACTRIAN: (о)оосро, 000000, oxoapo (etc.) ‘valid’ = S-W, Bact.: 209b 

*NWIR: NP giravidan ‘to believe, confide in; to obey’, NP bavaridan (denomin. ?) ‘to 
believe; credit’, NP bavar ‘belief; credit’ (< old intensive), Kurd. (Kurm.) bariya (Е) 
‘wish’, bavar, bawar (m.), (Sor.) bawar, birwa ‘belief; hope’ (Pers. LW ?) || (+ *uz-) 
? Bal. zurag, zirag, zorag ‘to take (out ?)’ || (+ *ui-) ? Bal. giwart/giwar- ‘to make 
equal’ (but in dial. also “о choose, select’, ‘to part, separate’) 

*NEIR: Oss. I. wyrnyn ‘to believe’, Yi. war-/wat-, M. wet-/wetta ‘to separate’ || (+ 
*apa-) Yzgh. bawurn ‘canal’ || (+ *uz-) Oss. І. evzaryn/avzarst, evzerd, D. 
evzerun/evzurst ‘to get separated; to sprout (of plants); to occur, appear’, (orig. 
caus.) Oss. I. avzarum/evzarst, D. avzarum/avzurst ‘to pick out, choose; to 
separate; to make out (of), understand; to experience’, Wa. zvor, z(o)wor, Sh. ziwor 
(f.) ‘offset, offshoot; the head part of an irrigation channel branching off from a 
main canal or river’, Sariq. ziwur ‘mouth of a river’ || (+ *ui-) Oss. I. waryn/weerst, 
D. iwarun/iurst ‘to divide, distribute; to be divided, divide up possessions’, Wa. 
yo(r)wor-/yo(r)word- ‘to divide, disperse (cattle)’ 

*MISC: Arm. (LW) vawer ‘true’ 

*SANSKRIT: var” ‘to choose, pick’ (RV+) > EWAia II: 511 

«PIE *uelH;- ‘to want, wish’ = LIV: 677 f. | Pok.: 1137 f. 

*IE COGNATES: Lat. volo ‘I want’, OCS velits ‘wants, orders’, Lith. vélti ‘to wish, to 
prefer’, Goth. wiljan ‘to want’, Engl. will, etc. 

*REFERENCES: JIFL II: 262b, 555b; Henning, Cosmog.: 310; Abaev, Slovar’ I: 209 ff.; EVS: 21b, 109b; 


Abaev, Slovar’ IV: 123 f., 51 f.; Werba 1997: 378 f.; Steblin-Kamenskij 1999: 434, 439; Cabolov 2001: 
124, 158 f.; Shahbakhsh: s.v. giwar- 


*uar(H)? *to mix, mingle' 

*CHORESMIAN: (+ *ham-) m/w’r- ‘to be mixed, confused’, (caus.) m/w’ry- ‘to mix, 
confuse’ — Samadi: 208 f. 

*NEIR: (+ *ni-) Wa. ni(y)or-/ni(y)ord-, nayor-/nayerd ‘to mix, mingle’. > 
Steblin-Kamenskij 1999: 245 derives the Wa. verb from *ni-uar (*yar ‘to turn’), but 
we may now assign it to *uar(H). 

© According to Samadi (ibid.) Chor. m/w’r-, m/w’ry- are counter-formations of 
bw’r- ‘to be separated’, bw’ry- to separate’ (< *upa-°). It remains unclear though 
how this procedure would have taken place, especially if we consider the simplex 
verb, which means ‘to choose; to convince; (med.) to believe’. Perhaps, m/w’r-, 
m/w’ry- has a different origin, being related to the well-attested Germanic forms for 
‘to confuse’. No further Ir. cognates can be cited though, with the exception of the 
Wa. forms. 


422 *yarHz 


«PIE ? *uer(H)- ‘to confuse, mix’. 9 The geminated -rr- in the Germanic forms 
possibly points to the presence of *H, on which see Lühr 1976: 92. = LIV: – | Pok.: 
1169 

*IE COGNATES: OSax., OHG werran, Du. (ver)warren, NHG verwirren ‘to confuse’
```


## [2026-10-17T00:03:31.512Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 219 220 222 223 256; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' HRN.txt | grep -n -E \"^ *[0-9]{3,4}\\. |gard|gird|gurd|nav|vard|var\" | head -30; done"
}
```


### [2026-10-17T00:03:32.331Z] TOOL RESULT

```
=== leaf 219
2:886. ijästen Vendun, drehen' (8ähn. I, 368 Vers 8-1:9; 369
9:ai. [/^vart-, vdrtate *sich wenden, drehen'-); aw. vergl.
10:güd^ö.]varetanqm (vd. 14, 6) und varetata (ZPGL); phlv.
11:O'istan (PV.), gast (vd. 9 (84) GL, West), vartitan,
12:gartitan (Bund.), vart{i)sn, gart{i)sn (Bund.), vartänT-
15:gardag , n. garday umkehren , umwenden (70) ; sar.
17:887. (/am Schritt'.
19:888. f/äv llind', gö, gög 'Kalb' {^gavaka-)'''), göban 'Hirte'.
=== leaf 220
2:889. ffäh *Ort (in Comp.) ; Thron*.
6:890. f/e^^Mörtel'.
10:891. (ßtidüften 'schmelzen', Praes. gudäz-em, gudäzclnlden
14:892. f/iidäre 'Brett (zum Dachdecken)' (unbelegt).
18:893. ffudästen hinüberführen, hinüberziehen', Praes. gu-
30:894. -ger '-tuend, -Macher', z. B. ähenger, dadger,
=== leaf 222
2:Dialektisch (K*ä§än, Q.) bedeutet (jurd, gurdl *hoch,
4:900. {lygird (Endung von Ortsnamen).
7:Die Ableitung von ap. vardana- (vergl. Mordtmann,
10:u. a. m. kann nur auf ap. *varta- zurückgehen ; vergl.
11:-varta^) in indischen Städtenamen (PW. s. v. und
15:901. {2)ffird rund; rings herum (begirdf , girde rundes
16:Brot* (arab. LW. jardaqat), girdü *Wallnuss'.
20:902. (/ertl *Staub* (ursprünglich 'wirbelnd, sich drehend).
21:ai. i/'^vart", vdrtatB 'sich drehen .
22:wa/. LW. gard, minj. y(fräi.
23:903. ff er den 'Nacken, Hals', gerdene 'Gebirgspass'^).
24:ap. *vartana', etwa 'Wirbel', zu [/^vart-; phlv. gartan
26:LW. kurd. gerdan *Hals'; af^'. bei. (71) gardan
27:'Nacken, Hals'; wa;^. §iyn. gardan, sar. gardan,
28:904. gerdün ^Firmament; Wagen.
29:ai. vartani^ 'Radkreis, Radfelge'.
32:>)Hüb8chinann steUt a. a. 0. auch zweifelnd np. sägird *Schüler*
36:Zu np gird gehört vielleicht auch oss. kärt *Hof* (von Stackel-
=== leaf 223
6:905. ffurde *Niere\
9:kurd. gurdale (H. -Seh.), gu7*cik{y)\ bei. guttiy;
12:906. ffuri^j gurze 'Keule', arab. LW. jurz,
13:aw. vazra- 'Keule ; phlv. vazr, arm. LW. varz; ai.
21:907. {\)gtir8 'Hunger, gursene, gursenegt; gtcsne, n22/}^
29:908. {2)gur8 Xockenhaar (unbelegt).
30:aw. varesa- 'Haar; phlv. vars, arm. LW. vars;
32:909. yiriften 'ergreifen*, Praes. glr-etn,
38:910. gurg 'Wolf.
39:Käs. var, varg, mrg\ mäz. vurg.
=== leaf 256
5:1049. ueved neunzig .
6:aw. naoaiti' 'neunzig; phlv. uaoat; ai. navatl-,
8:1050. neverdtden (neverden) *drehen, winden, wandern',
16:1051. niwiSteu^ miwisten, nibistm, ]n2/2^ (jüd.-pers.)
```


## [2026-10-17T00:03:36.574Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==220' HRN.txt | sed -n 1,18p; awk 'BEGIN{RS=\"\\f\"} NR==223' HRN.txt | sed -n 1,40p; awk 'BEGIN{RS=\"\\f\"} NR==224' HRN.txt | sed -n 1,12p; awk 'BEGIN{RS=\"\\f\"} NR==257' HRN.txt | sed -n 5,16p"
}
```


### [2026-10-17T00:03:37.021Z] TOOL RESULT

```
- 198 —
886. ijästen Vendun, drehen' (8ähn. I, 368 Vers 8-1:9; 369
Vers 852), Praes. yär-em (unbelegt) ^) ; gesten, Praes.
gerd-em, gerdlden, gerdämden, vergl. berd packe dich*,
berdtden 'sich vom Wege entfernen, abwenden* (s.
No. 195).
g. västmün ; vergl. Käs. K. gelnoimün [l = rd, wäh-
rend in V. Z. r erscheint, Seite 180).
ai. [/^vart-, vdrtate *sich wenden, drehen'-); aw. vergl.
güd^ö.]varetanqm (vd. 14, 6) und varetata (ZPGL); phlv.
O'istan (PV.), gast (vd. 9 (84) GL, West), vartitan,
gartitan (Bund.), vart{i)sn, gart{i)sn (Bund.), vartänT-
tan (AV.).
kurd. geriyän 'spazieren, sich wenden; bei. LW.
gardag , n. garday umkehren , umwenden (70) ; sar.
yirs-am, yerd-ao etc.
887. (/am Schritt'.
aw. gäma- 'Schritt'; phlv. gäm.
— 201 —
Dialektisch (K*ä§än, Q.) bedeutet (jurd, gurdl *hoch,
Höhe'.
900. {lygird (Endung von Ortsnamen).
ap. *-fcf^a-. (Hübschmann, KZ. 27, 112)^); phlv.
^kart, vergl. Därähkart.
Die Ableitung von ap. vardana- (vergl. Mordtmann,
ZDMG. 32, 724) ist unmöglich, da ap. rd im Np. zu
l geworden sein müsste. Np. -verd dagegen in Ablverd
u. a. m. kann nur auf ap. *varta- zurückgehen ; vergl.
-varta^) in indischen Städtenamen (PW. s. v. und
PäninT ed. Böhtlingk-, IV, 2, 126)? Material-
zusanimenstellung bei Blau, ZDMG. 31, 495 flf.; vergl.
dann auch Nöldeke, ZDMG. 33, 144 ff.
901. {2)ffird rund; rings herum (begirdf , girde rundes
Brot* (arab. LW. jardaqat), girdü *Wallnuss'.
ai. vfttä^ gedreht, rund'; phlv. vurtak 'runder Kuchen'
(Papyrus, unsicher; Hörn, ZDMG. 43, 51), gart (vd.
19 (15) für aw. skarena-; Men.).
902. (/ertl *Staub* (ursprünglich 'wirbelnd, sich drehend).
ai. i/'^vart", vdrtatB 'sich drehen .
wa/. LW. gard, minj. y(fräi.
903. ff er den 'Nacken, Hals', gerdene 'Gebirgspass'^).
ap. *vartana', etwa 'Wirbel', zu [/^vart-; phlv. gartan
(vd. 19 (94) Gl.).
LW. kurd. gerdan *Hals'; af^'. bei. (71) gardan
'Nacken, Hals'; wa;^. §iyn. gardan, sar. gardan,
904. gerdün ^Firmament; Wagen.
ai. vartani^ 'Radkreis, Radfelge'.
kurd. LW. gerdün 'Wagen ; oss. värdon * Wagen' (258).
Np. gerdün steht für *gerdan (dasselbe gilt für oss.
>)Hüb8chinann steUt a. a. 0. auch zweifelnd np. sägird *Schüler*
(arm. LW. asakert^ phlv. asökart) hierher, doch geben die Lexikographen
auch vird als 'Schüler' an. Wenn diese Form irgend welchen Wert hat,
80 ist die Etymologie Fr. Müller's, WZKM. 5, 66 unmöglich.
Zu np gird gehört vielleicht auch oss. kärt *Hof* (von Stackel-
berg, Fünf osset. Erz. 82).
*j Oder viti" 'Einzäunung' (?j
') VuUers s. v. g erden (gerdengäfi).
— 202 -
värdon, vgl. Hübschmann, S. 86); andere Bei-
spiele dieses der Umgangssprache entnommenen Laut-
wandels sind enderän (No. 119), heran (No. 252),
dehün (unter No. 589).
905. ffurde *Niere\
aw. (Du.) vereöka- (vd. 18, 70), veretka- *beide Nieren
(ZPGl.) ; phlv. gurtak ; ai.-präkr. (Du.) vfkkd- *Nieren'.
kurd. gurdale (H. -Seh.), gu7*cik{y)\ bei. guttiy;
wa/. velk.
Hübschmann, KZ. 25, 109.
906. ffuri^j gurze 'Keule', arab. LW. jurz,
1049. ueved neunzig .
aw. naoaiti' 'neunzig; phlv. uaoat; ai. navatl-,
kurd. nöt^ nüd; af/. «at'c.
1050. neverdtden (neverden) *drehen, winden, wandern',
ueoesten (AM. 2 Zeile 7), neverd.
ai. w/ f- Ki^ar^- zurückkehren, fortgehen, den
Kücken kehren etc.*.
Wenn die Etymologie richtig ist, so wäre die ur-
sprüngliche Form *mverdlden bezw. *nivesten,
nöx siehe hemz (No. 1108).
nöS, nöse 'lieblich' siehe enöse (No. 128).
1051. niwiSteu^ miwisten, nibistm, ]n2/2^ (jüd.-pers.)
```


## [2026-10-17T00:03:42.291Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *(886|901|902|903|904|905|1050)\\. |gurtak|gurde|gerdan|nawar|neverd|bävar|bāvar|wäwar|vāvar\" HUB.txt | head -30"
}
```


### [2026-10-17T00:03:42.792Z] TOOL RESULT

```
3230:901. Np. gird 'Umkreis, rund, rings* liegt im Phi. als
3242:902. Np. gard *Staub* = phi. vart ^Staub', Yfitk. i. Zar. 68,
3248:904. Die Annahme, dass garden 'Wagen, Firmament' fiir
4202:anagah, phi. anakds ^unaware* Shk. 228; nar *6ranatapfer
4789:nabard *Kampf ' ^= p z. naward quarrel* Min. Gl. 143, phi.
5504:in hqmvareti' ; gurda *Niere* = phi. gurtak ZPGl. 10, 1. Z.>
5679:Gl. 223 = zd. vehrka-; 15) gurtak *Niere' = zd. veretka-
5694:gumdn, gumext, gurbak (?), gurt, gursak, gurg, gurtak, gusn,
5699:vf {gurt, gursak, gurg^), gurtak, gusn), danach in der An-
7398:dafiir ist np. d eingetreten in gurda *Niere* = phi. gurtak
7403:'^vurtak^ *gurtak = np. gurda.
```


## [2026-10-17T00:03:46.367Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3225,3256p HUB.txt; sed -n 5500,5506p HUB.txt; sed -n 7395,7404p HUB.txt; grep -n -E \"va-gard|w\\s*=\\s*g|v im Anlaut|anlaut. v\" HUB.txt | head -5"
}
```


### [2026-10-17T00:03:46.797Z] TOOL RESULT

```
899. Vgl. zd. vareti' in hqmvareti- *Tapferkeit\ Phi. gurt
steht fiir alteres *vurt = ap. "^vrta-.
900. Vgl. auch ZDMtt. 30, 138—141. Das in der Note
angefiihrte vird 'Schiiler hat keinesfalls etwas mit np.
sdgird 'Schiiler' = phi. asdkert zu thun.
901. Np. gird 'Umkreis, rund, rings* liegt im Phi. als
g(i)rt vor, vgl. Phi. Vd. p. 211, Z. 9, Bdh. Gl. 219,
6uj. Abal. 74 u. s. w. und das dazu gehOrige gird<i
rundes Brot' ^= arab. jardaqa im Armenischen als
grtak *Laib Brot', das ein phi. *girtak voraussetzt.
Ich wtirde danach als Grundform ap. *grta- ansetzen.
Dem steht allerdings die ansprechende Zusammen-
stellung von np. gird mit skr. vart *sich drehen' == np.
gardidan entgegen. Aber skr. *varta- ware = phi.
*vart = np. *gard, skr. "^vHa^ = phi. *giirt = np.
*gurd. Das von Horn erwahnte phi. vartdk ist seiner
Bedeutung nach dunkel.
902. Np. gard *Staub* = phi. vart ^Staub', Yfitk. i. Zar. 68,
Anm. 69.
908. Die Etym. ist m5glich, aber unsicher, so lange der
Beweis fiir die Entstehung von g aus v nicht aus dem— 92 —
Iranischen erbracht ist. Phi. gartan mit g auch 61.
und Ind. 261.
904. Die Annahme, dass garden 'Wagen, Firmament' fiir
gardan stehe, ist willkiirlich und wird durch die von
Horn citirten Beispiele nicht gestiitzt. Np. gardun
kann nur = phi. "^gartUn, *gart(^ oder '^vartun, *var~
ton gesetzt werden. Ueber osset. vdrdun^ vdrdon (als
LW. aus deni Mittelpers.) vgl. Miller-Stackelberg,
Fiinf osset. Erzahlungen p. 69.
906 ****• Das Parsenwort (!) garzmdn ^Himmel' = paz. garod^-
man Min. Gl. 86 = phi. garOtman (fiir garOdman)
'wachsen*, skr. vi + Wzl. vardh; guvdh 'Zeuge* = phi. gukas,
skr. *vikaga-?; guvam 'Schmahung', skr. vivac-; Gustasp
N. pr. = phi. V(i)stasp Yatk. i. Zar. 51, ap. Vistaspa-; gurd
'Held*, phi. gurt Gl. and Ind. 284, aus *vfta-^ vgl. zd. vareti-
in hqmvareti' ; gurda *Niere* = phi. gurtak ZPGl. 10, 1. Z.>
zd. veredka-^ veretka-; gurs 'Hunger*, gursina^ gusna, gusna
'hungrig', paz. gursnal 'Hunger Min. Gl. 94, phi. gursak
Ueber ap. ri9 aus rs = np. hi siehe § 103, b.
Ueber idg. ts = iran. s = pers. A siehe § 88.
Fur urspr. tk sollte man ap. &k ~ np. hk erwarten,
dafiir ist np. d eingetreten in gurda *Niere* = phi. gurtak
= zd. veredka- (vgl. adka-) oder veretka- ZPGl. 10 (d. i.
*Deretka')j skr. vrkka-. Lautgesetzlich ware nach den
jijngeren iranischen Fornien (siehe Horn 905) vielmehr ein
ap. *vrta^ anzusetzen ■= phi. *vrt + Suffix ak = *vrtak,
'^vurtak^ *gurtak = np. gurda.
Np. h aus & ist mehrfach vor r (§ 96) und I (in pul,
```


## [2026-10-17T00:03:52.711Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^(gardan|gardīdan|gardēnīdan|gird|gurdag|gard|wābar|wāwar|war |war\\b|wardīdan|nawardīdan|naward|wardag|wābarīgān|wābarīh|wābarīgānīh|warrah)\" PHD.txt | head -30"
}
```


### [2026-10-17T00:03:53.438Z] TOOL RESULT

```
603:wābar [w’Al | M wbr, (N bāwar)] truth; belief. wābarīģān [w?/yk?n' | M wbryg’n) true, trustworthy. “Аһ: trustworthiness. wabz [wpc, wpz] wasp. wačast [wcst! = Av. vwacas-tasti-] strophe (of the Gathas). watéag [wck!, (bck!) | N bacca] child, baby, cub. wad [SL Y.ÀA < A sry’; wt! | M wd, N bad] bad, evil. ^ Áh : badness, evil. маа [w?t! | M wd, N bad] wind, breath, spirit; cal. 22nd day. wadag [wtk'] evil, vile, wicked. ~ih: evil, vileness. wādām [w’t?m | N bádám] almond. wādbān [w°tp’n' | N bādbān] sail.
2074:garden bày ; (flower) ~ bēyestān.
2075:gardener boyestanban.
2102:girdle kamar; sacred ~ ēbyānghan, kustig.
5257:wābarīgān
```


## [2026-10-17T00:04:01.133Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o -E \"(gardan|gardīdan|gird|gurdag|gurdag|gard|war|wardīdan|nawardīdan|wardēnīdan|wardišn|wardyūn) \\[[^]]*\\][^.]{0,160}\" PHD.txt | head -30; grep -o -E \".{0,40}ordeal.{0,80}\" PHD.txt | head"
}
```


### [2026-10-17T00:04:04.586Z] TOOL RESULT

```
gard [B, 8, y, Z] as possible realizations of postvocalic b, d, g, j
war [b'hl(k)wl | N bahrawar| partaking, parti- cipator, partner. ~th : participation, advantage. balay add M by. add balgam |[blgm | N balyam] phlegm
war [hnw!] the holiest prayer, beginning Yadā ahū wairyē
war [поў] mortal
war [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v
war [?*cwl | N ~] greedy
war [bhlwl | N bahrawar] endowed, provided
war [Буш | M bywr, N ~] myriad, ten thousand
war [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge
gird [Y DE., dst-krt! | M dstygyrd, N dastgird] estate
war [dstwbl | М dstwr, N dastür] authority, priest, minister
war [gtwl = Av. gaóawara-] bearing a club
war [-wbl | M -wr, N ~] treasurer
gard [g/t! | N ~] dust
gardan [gitn! | M grdn, N ~] neck
gird [git! | M gyrd, N ~] round, circular; gathered
gird [оо | M gwgyrd, N ~] sulphur
gurdag [gwltk! | N ~a] kidney
war [-wl | (P -br), N jánwar] animate; animal
war [mkyfwl | M. -wr] universe
war [hmwl | N hamwār] level, abreast
war [kynwl | (M kynw’r), N kinawar] vengeful, vindictive
war [Rystol | M kyswr, N ~] region, clime, continent
war [-w/] essential, especial, principal
war [-wbl | N -àr] hireling
war [ptshwl] dish, bowl
war [plwl | M prwr] winged
war [Incwl | (M rnzwr), N ranjūr] troubled, distressed
war [snwl = Av. 0anwar-] bow
war [-w/ | N sazāwār] = затар
ugrep: error: error at position 82
bf][\x80-\xbf]*){0,80}
                      \___exceeds complexity limits
```


## [2026-10-17T00:04:08.283Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o -E \"ordeal.{0,60}\" PHD.txt | head; grep -o -E \"\\bwar \\[[^]]*\\][^.]{0,80}ordeal\" PHD.txt; grep -o -E \"(gardīdan|wardīdan|nawardīdan|wardēnīdan|gardēnīdan) \\[[^]]*\\][^.]{0,120}\" PHD.txt | head"
}
```


### [2026-10-17T00:04:08.826Z] TOOL RESULT

```
ordeal. ģarmsēr [gimsyl | N ~] warm region, lowlands. garódman [gl
ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”
ordeal war; heat ~ garmówat(ih).
```


## [2026-10-17T00:04:13.814Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o -E \".{0,200}ordeal. ‘war \\[wl\\]\" PHD.txt; grep -o -E \"gard-,? .{0,100}\" PHD.txt | head -5; grep -o -E \"gardīdan.{0,100}\" PHD.txt | head -5; grep -o -E \"ward-, .{0,100}|wardīdan.{0,100}\" PHD.txt | head -5; grep -o -E \"nawar.{0,120}\" PHD.txt | head -5"
}
```


### [2026-10-17T00:04:14.636Z] TOOL RESULT

```
yh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl]
gard- [git-yin' | M grd-, N ~] turn, revolve. ~išn: revolution, turning. garm [gim | M grm, N ~] warm, hot
gard- gardān- gardānāg gardānīdan dardūmand girdīh gardīdan dard, gard, gird gardan girdag gardisn dam- za
gardīdan.
gardīdan dard, gard, gird gardan girdag gardisn dam- zamanig zaman
ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on 
nawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y
naware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] In
nawar Pzrw/l | M ?zn] noble. azraw-, v. azruftan. azray- ['zr'd-] adorn. azruftan, azraw- [)zlwp-tn! | M *zrw-] go out, be ex
nawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, fa
naware anagah.
```


## [2026-10-17T00:04:35.823Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"ordeal|^gurtak|^gartan|^girt|^vartītan|^gartītan|^vart|^vāvar|kidney\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-10-17T00:04:36.214Z] TOOL RESULT

```
1081:buxtan [bwhtn'] bēž- [bwe-], to save, to preserve (hac from) 701, 8519-20, 8825, pass. buxtém we are saved 61; inf. buxtan in pass. sense: to be saved = to come out of the ordeal (of fire) safe and sound (pat: ‘thus proving the truth of .. .’) 10916. . Av. (916 sq.) baog-; Ps. bwhty, bwe-; MPrthPrs bwatn, pres. MPrth bwy-, bwas-, MPrs bwz-; Arm. lw. bužem; Paz. boxtan, buxtan, bož-. — V. božišn.
1640:gartan [gltn'] neck 312°. — MPrs gr[dn] (A-H I); NP gardan.
1657:girt
1665:girt [glt'] round 941%; ~ kartak 38%4, ~ kart 394 "fully developed (?); [späh pat vas marak ~ kart he brought to- gether an army of a large number KnS IV, 12 = KnA p. 22?-10]. - MPrs gyrd ‘all around’ (S), subst. ‘round’ (A-H I); Paz. NP gird; NP gird kartan ‘to collect, to assemble, to bring together”; Güräni gi(rd), gist ‘all, everyone’ (KPF III, II, 248 sg.). From gart-, v. gartišn.
1667:girtak
1668:girtak: ~ pērāmēn all around 92!9,
2992:passäxt [ps'ht'] 108° pat-säxt [PWN- s?ht'], accomplishment, performance, esp. of the var, the ordeal: var ~ DkM 74312, 77117; hence ~ alone: ordeal; ~ gah the place of the ordeal 10117; pat gobišn i m through the decision of the ordeal 10915; Āturpāt i Mahraspandčin kē patiš pat-sāxt + pat den kart, rod + vitàxtak apar var réxt A. i M., who accomplished the ordeal upon it (patiš: in order to prove its truth) conformably to Religion, melted metal being poured on his breast 1085-5. The ordeal either acquits or condemns, either proves or denies the truth of an assertion, a witness, etc., the terms being buxtan and éraxtan (črixtan) (v. these ws.) which are often asyndetically co- ordinated so as to form a sort of dvandva: buxtan-éraxtan, buxt-éraxt indicating the alternative decisions of the ordeal. Cf also DkM 644?’-21, The vb. passáxtan may be used in the sense of ‘to accom- plish the ordeal’, DkM 4543. — Pt. of passäxtan < *pat-säc-, v. sdxtan. Paz. pasdat, Skr. v. mahadivya ‘great oath’ (SGV X, 70); MPrthPrs ps’ztn ps?c- ‘to arrange’, MPrth also psat. |
3981:vart [wlt'] captive = the next w.?: Mihrak 4 —-ruvän M. whose soul is (to be) captured (?) 132%, cf 6512-18. — MPrth wrd ‘captive’ (MHC).
3982:vartak captive 19%. — Av. (1368) ?varota-; Ps. wldky; MPrthPrs wrdg; NP bardah.
3983:vartčn [wltyn'] wheel: and cand vartén-é [7--?y] as large as a wheel 3118; war-cha- riot 2012-23, — From vart-, v. vaštan. Hen- ning, List 82, reads 3113 vartēnāt and identifies it with MPrs grd(y)n’g, which seems, however, to be the pt. of gardén- and only to refer to the Zodiac.
3984:varten-där [wltynd?l] charioteer 2012,
3985:vartčnišn [wltynän'] transformation
3987:varténitan to change, to alter, to trans- form 7625. 7779.26.27 782.4, 791.3, — Caus. of vart-, v. vastan; Paz. vardinidan.
3988:vartišn [wltšn'] the act of turning: 1. han i avdom ~ the last turn, of the end of the world and the fraškart (q. v.) 4619; ~ 4 axtarün u gartišn 4 spahr the revolu- tion of the fixed stars and the rotation of the sphere 1205-5; ~ u gartišn + muhrak the moving and transposing of the draughtsmen 12015, — 2. pred.: turned, became 41??, — V. vastan.
3991:vartišnēh det. v. n.: hac tan bod bē ~ the departure of the consciousness from the. body (= death) 642°.
6860:vartin: varan
```


## [2026-10-17T00:04:40.827Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1655,1664p NYB_vol2_glossary.txt; grep -n -E \"^gartišn|^gartītan|^gart-|^var \\[|^var\\b|^vāvar|^vāvarīkānēh|^vaštan\" NYB_vol2_glossary.txt | head; "
}
```


### [2026-10-17T00:04:41.268Z] TOOL RESULT

```
gēhān [gyh’n'] pl. and coll., the world of creatures, men and animals, esp. the world of man: astömandän ~ 3913; han 4 mänisnömand (q.v.) göspandömand ~ 5714-15; herds of grazing animals 4913; — the material world in general: 21. 418 etc. passim. — < *gaidānām, gen. pl. of Av. (476 sqq.) gaēdā-; OP gai0à- “live-stock’; Aram. lw. (Targ, Talm) gyty ‘herds’; MPrth gyh (< gaia) ‘world’, pl. gyh?n ‘worlds’; Paz. geha; NP gehän, gihän, jihän. Cf gétah.
Gēpakān [gypk’n'] patron. 11425-26, — < Vepakän, v. Cat. 61.
girt
gétah [gyt*h], gētē [gytyd; gyty 10915] the material, corporeal world, passim. — Borrowed from Av. gačda, v. gehän; Paz. gēdī, gētī = NP.
getähik [gyt’hyk] belonging to the mate- rial world, corporeal, material 8976.
gétik [gytyk] terrestrian, subst. pl. the material, terrestrian beings, cas. obl. —-ün [eytyk'n'] 8811135, 897, 9314, 1052; — yazdän + getikän the terres- trian gods 34!” (for cas. rect., mixed constr.) — MPrs gytyg ‘world’ (A-H II); Paz. pl. gēdya, ge0ia, Skr. v. thalokiyäh, thacarinah.
gil [TYN?] clay 951%. — = NP.
gil- pres. 3d p. sg. gilēt wrongly written ‘HDWN-yt' for gylyt', which also could be read girét (from griftan): to weep, to complain 1021, — < "girdet < *grd-, SW form of girz-, v. girzitan, garzitan and gristan; another instance of wrong *HDWN- v. *gir-. — From *grd- also
gilak [gylk'] distress 761, — Paz. gila, Skr. v. aparddha; NP gilah ‘complaint, re- proach’, cf MPrs gylg’y ‘complaining’ (S, cf s. v. cašm-kāt).
*gir- [HDWN-] pres. Ist p. sg. giram [HHDWN-m], to praise 35. — Written with the ideogr. of griftan gir-, which gives no sense in this context; another vb. must be meant (ci "gil-, which is wrongly written with the same ideogr.): gir- < *girr- < *girn-, Av. (512) ?gar-, pres. goron-. Of. āžarm, apažīrišnīk, garämik.
1393:var(e)št (Mx), corresponding to Phl *duš- varšt; from varz-, v. varzitan.
1642:gartišn [gltšn'] turning, rotation, revo- lution 1206.16.20. — MPrs pres. grd- ‘to turn, to become’ (BBB), caus. grdnydn trans. ‘to turn’ (S); NP gaštan or gardidan gard-, gardiš; etymologically not identical with vart- (v. vaštan) by which it is semasialogically influenced. OIr *gart- probably ‘to twist, to wreathe’, cf Skr jata ‘plait’, probably a Sanskritized Prakrit-w. < *jartä. Hence girt (g. v.).
3950:varāg [wl'g] raven 9471-28, — BdA p. 1556? én-ic göbet ku murv hamäk zirak u varag ziraktar bavet = BdJ 47°, where -g is written with the original form of k found in the Ps. (= Paz. y); BdJ 47% wbPk, 31!! (Paz.) varay.
3954:varäz [wl’c'] boar; hero 225-9, 26%, — Av. (1366) vardza-; KZŠPrth 1. 23. 25 wrc = Prs, Gr. v. Topat, Tovupat; NP gurāz; cf Gardzak.
4027:vaštan [wštn'] vart- (Ps. wld-, v. vard-) to turn 1. intr. to return, to go back 105; hamešak hac hom ap. vast always water came out from the H. 39%, with the gl. it [viz. the tree where the Haoma dwelt] was humid [= always had humidity]"; hamäk varténd they have all their being 12018, v. vihe-; vartet andar Vizak it (the pedigree) turns, starts from another side, with V. 473; — with prev.: apāc ~ to turn back, to return 84, 137°; apar apāk vast he went back preci- pitately 5118; — apar 6 ax" + astomand bé vašt hend they went down (from Heaven) on to the material world 40!; — (taräzük kē) cand mode tak bē ne vartēt (the balance that) does not deviate a hairbreadth
5423:var-: varan varah-: !var varana-, varona-: varan varaza-: varaz varocah-: vare vareda-: gul varoka-: varg Varo0rayna-: Varhran väroma-: várom varosa-: vars varot-: vastan ?varota-: vartak varoz-: varzitan varoza-: lvarz vari-: ?var
5424:varšni-: gušn vastra-: vastarg vastra-: vastr
6853:var: !var, ?var
6857:varéxtan: viréxtan
6859:varčišni: virrdyistan
```


## [2026-10-17T00:04:54.682Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-17T00:04:54.713Z] TOOL RESULT

```

```


## [2026-10-17T00:04:58.040Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -50"
}
```


### [2026-10-17T00:04:58.698Z] TOOL RESULT

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


## [2026-10-17T00:05:05.562Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f(){ python3 tools/fetch_source.py \"$1\" --note \"page 544, $2\"; }\nf 'https://en.wiktionary.org/wiki/باور' 'root Wer 1, bâvar etymology'\nf 'https://en.wiktionary.org/wiki/ور' 'root Wer 1, var ordeal'\nf 'https://en.wiktionary.org/wiki/گردیدن' 'root Wer 2, gardîdan'\nf 'https://en.wiktionary.org/wiki/گردن' 'root Wer 2, gardan neck'\nf 'https://en.wiktionary.org/wiki/گرد' 'root Wer 2, gerd/gard'\nf 'https://en.wiktionary.org/wiki/گردو' 'root Wer 2, gerdu walnut'\nf 'https://en.wiktionary.org/wiki/گرده' 'root Wer 2, gorde kidney'\nf 'https://en.wiktionary.org/wiki/نوردیدن' 'root Wer 2, navardidan'\nf 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/werh₁-' 'root Wer 1 speak'\nf 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wert-' 'root Wer 2 turn'\nf 'https://www.etymonline.com/word/irony' 'root Wer 1, irony'\nf 'https://www.etymonline.com/word/word' 'root Wer 1, word'\nf 'https://www.etymonline.com/word/verb' 'root Wer 1, verb'\nf 'https://en.wiktionary.org/wiki/گشتن' 'root Wer 2, gaštan/gard-'"
}
```


### [2026-10-17T00:05:11.661Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bfee4ddb48131f7c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/36498fe3fb616843.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/58d4777a851cc2ab.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/486cd2ffe4805411.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/660671ff5494c6e4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9245c8173a1e369f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b1283d745dcf086f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ab55e2953d2be063.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/798e2abbd9ab30ee.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8e5cb39fa2dd5f56.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1cb6c7e296407f61.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e950c126daed8204.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8f7237ce80a240b9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7fd1b031201159af.txt
```


## [2026-10-17T00:05:15.714Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in bfee4ddb48131f7c 36498fe3fb616843 58d4777a851cc2ab 486cd2ffe4805411 660671ff5494c6e4 9245c8173a1e369f b1283d745dcf086f ab55e2953d2be063 7fd1b031201159af; do echo \"=== $f\"; head -c 300 $f.txt | head -3; grep -n -A6 \"^ *Etymology\" $f.txt | grep -v \"^--$\" | head -40 | cut -c1-400; done"
}
```


### [2026-10-17T00:05:16.112Z] TOOL RESULT

```
=== bfee4ddb48131f7c
URL: https://en.wiktionary.org/wiki/باور
FETCHED: 2026-10-16T05:14:51Z
STATUS: 200
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
93- 2.3 
94- Noun 
102: Etymology 
103-
104- 3.2 
105- Noun 
106-
107- Toggle the table of contents 
108-
183: Etymology
184- [ edit ] 
185-
186- Inherited from Middle Persian 𐭥𐭠𐭯𐭫 ( w'pl /⁠wābar⁠/ ) , [ 1 ] from Avestan 𐬎𐬞𐬁𐬬𐬀𐬭 ( upāvar , “ in belief ” ) , from Proto-Indo-European *upó and either Proto-Indo-European *werh₁- ( “ to speak ” ) or Proto-Indo-European *welh₁- ( “ to wish, desire ” ) . [ 2 ] Compare Old Armenian վաւեր ( vawer ) , an Iranian borrowing.
187-
188- Pronunciation
189- [ edit ] 
344: Etymology
345- [ edit ] 
346-
347- Borrowed from Classical Persian بَاوَر ( bāwar ) .
348-
349- Pronunciation
350- [ edit ] 
364: Etymology
365- [ edit ] 
366-
367- From Urdu باوَر ( bāvar ) .
368-
=== 36498fe3fb616843
URL: https://en.wiktionary.org/wiki/ور
FETCHED: 2026-10-17T00:05:07Z
STATUS: 200
62: Etymology 
63-
64- 1.2 
65- Verb 
66-
67- 2 
68- Mazanderani 
95: Etymology 
96-
97- 4.2 
98- Pronunciation 
99-
100- 4.3 
101- Noun 
112: Etymology 
113-
114- 5.2 
115- Pronunciation 
116-
117- 5.3 
118- Noun 
126: Etymology 1 
127-
128- 6.1.1 
129- Noun 
130-
131- 6.2 
132: Etymology 2 
133-
134- 6.2.1 
135- Adverb 
136-
137- Toggle the table of contents 
138-
211: Etymology
212- [ edit ] 
213-
214- See the etymology of the corresponding lemma form.
215-
216- Verb
=== 58d4777a851cc2ab
URL: https://en.wiktionary.org/wiki/گردیدن
FETCHED: 2026-10-17T00:05:07Z
STATUS: 200
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
140: Etymology
141- [ edit ] 
142-
143- From Proto-Iranian *wart- ( “ to turn, spin, rotate; to writhe ” ) , ultimately from Proto-Indo-European *wert- . More at گرد ( gerd ) .
144-
145- This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term. 
146-
=== 486cd2ffe4805411
URL: https://en.wiktionary.org/wiki/گردن
FETCHED: 2026-10-17T00:05:08Z
STATUS: 200
78: Etymology 
79-
80- 3.2 
81- Pronunciation 
82-
83- 3.3 
84- Noun 
98: Etymology 
99-
100- 4.2 
101- Pronunciation 
102-
103- 4.3 
104- Noun 
250: Etymology
251- [ edit ] 
252-
253- Cognate with Khotanese gaḍaa- ( “ throat, neck ” ) , etc.
254-
255- Pronunciation
256- [ edit ] 
405: Etymology
406- [ edit ] 
407-
408- Borrowed from Classical Persian گَرْدَن ( gardan ) . [ 1 ] First attested in c. 1635 as Middle Hindi گردن ( grdn /⁠gardan⁠/ ) . [ 2 ] 
409-
410- Pronunciation
411- [ edit ] 
=== 660671ff5494c6e4
URL: https://en.wiktionary.org/wiki/گرد
FETCHED: 2026-10-17T00:05:08Z
STATUS: 200
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
93: Etymology 1 
94-
95- 3.1.1 
96- Pronunciation 
97-
98- 3.1.2 
99- Adjective 
114: Etymology 2 
115-
116- 3.2.1 
117- Pronunciation 
118-
119- 3.2.2 
120- Noun 
132: Etymology 3 
133-
134- 3.3.1 
135- Pronunciation 
136-
137- 3.3.2 
138- Noun 
219: Etymology
220- [ edit ] 
221-
222- From Proto-Iranian *gr̥Híš , from Proto-Indo-Iranian *gr̥Híš , from Proto-Indo-European *gʷerH- .
223-
224- Pronunciation
225- [ edit ] 
323: Etymology 1
324- [ edit ] 
325-
326- Inherited from Middle Persian [Book Pahlavi needed] ( wlt- /⁠ward-⁠/ , “ to turn, twist, writhe; to change ” ) , Manichaean Middle Persian 𐫇𐫡𐫅 ( wrd ) , from Old Persian 𐎺𐎼𐎫 ( vart- ) , from Proto-Iranian *wart- ( “ to turn ” ) , from Proto-Indo-Iranian *wart- , ultimately from Proto-Indo-European *wert- ( “ to turn, rotate ” ) . [ 1 ] [ 2 ] 
327-
=== 9245c8173a1e369f
URL: https://en.wiktionary.org/wiki/گردو
FETCHED: 2026-10-17T00:05:09Z
STATUS: 200
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
146: Etymology
147- [ edit ] 
148-
149- From گرد ( gerd , “ round ” ) + ـو ( -u ) .
150-
151- Pronunciation
152- [ edit ] 
=== b1283d745dcf086f
URL: https://en.wiktionary.org/wiki/گرده
FETCHED: 2026-10-17T00:05:09Z
STATUS: 200
65: Etymology 1 
66-
67- 1.2.1 
68- Noun 
69-
70- 1.3 
71: Etymology 2 
72-
73- 1.3.1 
74- Noun 
75-
76- 1.4 
77: Etymology 3 
78-
79- 1.4.1 
80- Noun 
81-
82- 1.5 
83- References 
166: Etymology 1
167- [ edit ] 
168-
169- Noun
170- [ edit ] 
171-
172- گرده • ( garde ) 
176: Etymology 2
177- [ edit ] 
178-
179- Ultimately from the Proto-Indo-European root *wer- .
180-
181- Noun
182- [ edit ] 
190: Etymology 3
191- [ edit ] 
192-
193- From Middle Persian gwltk’ ( gurdag , “ kidney ” ) , from Proto-Indo-Iranian *wr̥tkás ( “ kidney ” ) ; compare Avestan 𐬬𐬆𐬭𐬆𐬜𐬐𐬀 ( vər ə δka ) and Sanskrit वृक्क ( vṛkka ) , Northern Luri گۏردالٱ ( gördāla ) .
194-
195- Noun
196- [ edit ] 
=== ab55e2953d2be063
URL: https://en.wiktionary.org/wiki/نوردیدن
FETCHED: 2026-10-17T00:05:09Z
STATUS: -1
=== 7fd1b031201159af
URL: https://en.wiktionary.org/wiki/گشتن
FETCHED: 2026-10-17T00:05:11Z
STATUS: 200
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Verb 
160: Etymology
161- [ edit ] 
162-
163- Inherited from Middle Persian [Book Pahlavi needed] ( gltyt /⁠gardēd⁠/ ) , from Proto-Iranian *gártati ( “ to turn ” ) , possibly a merger with *gárati ( “ to turn, wind ” ) and *wártati ( “ to turn ” ) , the former being of uncertain origin and the latter from Proto-Indo-European *wert- ( “ to turn ” ) . [ 1 ] Cognate with Tat gəştən and akin to the Iranian borrowings: Old Armenian վաշտ ( va
164-
165- Pronunciation
166- [ edit ]
```


## [2026-10-17T00:05:24.696Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 230,252p 486cd2ffe4805411.txt | tr -s '\\n' | head -20; echo ====; sed -n 300,420p 660671ff5494c6e4.txt | grep -v \"^\\s*$\" | cut -c1-300 | head -60"
}
```


### [2026-10-17T00:05:25.049Z] TOOL RESULT

```
Exit code 1
 بینی 
 دهان 
 چانه 
 فک 
 گوش 
 گیجگاه 
 گردن 
 Click on labels in the image
 The template Template:picdicimg does not use the parameter(s): lang=en Please see Module:checkparams for help with this warning. 
 body 
 Etymology
 [ edit ] 
(eval):1: === not found
```


## [2026-10-17T00:05:27.893Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 300,420p 660671ff5494c6e4.txt | grep -v \"^\\s*$\" | cut -c1-300 | head -60; grep -n -i -E \"ordeal|var\\b\" 36498fe3fb616843.txt | head"
}
```


### [2026-10-17T00:05:28.232Z] TOOL RESULT

```
 گردلرچه 
 ablative
 گردده 
 گردلرده 
 instrumental
 گردله 
 گردلرله 
 equative
 گردواره 
 گردلرواره 
 Persian
 [ edit ] 
 Etymology 1
 [ edit ] 
 Inherited from Middle Persian [Book Pahlavi needed] ( wlt- /⁠ward-⁠/ , “ to turn, twist, writhe; to change ” ) , Manichaean Middle Persian 𐫇𐫡𐫅 ( wrd ) , from Old Persian 𐎺𐎼𐎫 ( vart- ) , from Proto-Iranian *wart- ( “ to turn ” ) , from Proto-Indo-Iranian *wart- , ultimately from Proto-Indo-European 
 Cognates include Sanskrit वर्तते ( vártate , “ to turn, roll ” ) , Proto-Slavic *vьrtě̀ti ( “ to turn ” ) , Latin vertere ( “ to turn ” ) , German werden ( “ to turn (into), become ” ) , English worth ; also Avestan 𐬬𐬀𐬭𐬆𐬙- ( var ə t- ) , Khotanese [script needed] ( bal- /⁠baḍ-⁠/ , “ to move, writhe
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ˈɡird/ 
 ( Dari, formal ) IPA ( key ) : [ɡɪɹd̪] 
 ( Dari, formal ) IPA ( key ) : [ɡɪɹd̪] 
 ( Kabuli ) IPA ( key ) : [ɡɪɹd̪] 
 ( Hazaragi ) IPA ( key ) : [ɡiɹd̪̥] 
 ( Iran, formal ) IPA ( key ) : [ɡʲeɹd̪̥] 
 ( Tajik, formal ) IPA ( key ) : [ɡiɹd̪] 
 Rhymes: -ird 
 Readings
 Classical reading ? 
 gird
 Dari reading ? 
 gird
 Iranian reading ? 
 gerd
 Tajik reading ? 
 gird
 Adjective
 [ edit ] 
 گرد • ( gird / gerd ) ( Tajik spelling гирд ) 
 round , circular 
 Derived terms
 [ edit ] 
 گردی ( girdī  / gerdi ) 
 گردباد ( girdbād  / gerdbâd ) 
 گردالی ( girdālī  / gerdâli ) 
 Related terms
 [ edit ] 
 گردیدن ( gardīdan  / gardidan , “ to rotate, spin, circulate ” ) 
 گردو ( girdū  / gerdu , “ walnut ” ) 
 Descendants
 [ edit ] 
 → Chagatai: کرد ( krd /⁠gird⁠/ ) 
 Uzbek: gir , gird 
 Verb
 [ edit ] 
 گرد • ( gard ) ( Tajik spelling гард ) 
 present stem of گشتن ( gaštan , “ to wander; to change ” ) 
 Etymology 2
 [ edit ] 
 Inherited from Middle Persian [Book Pahlavi needed] ( glt' /⁠gard⁠/ , “ dust ” ) , [ 3 ] ultimately from the same root as the verb گَشتَن ( gaštan , “ to wander around ” ) .
 Pronunciation
229: ور ( var ) ( وَر ) 
269: Cognate with Baluchi گور ( gwar ) , Mazanderani ور ( var ) , Talysh ور ( var ) , etc.
301: var
305: var
310: ور • ( var ) 
317: این ور ( in var ) 
319: آن ور ( ân var ) 
337: ور • ( var )  m ( Gurmukhi spelling ਵਰ ) 
352: ور ( var )
```


## [2026-10-17T00:05:37.153Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"gwrtk|γwrtk|ywrtk|gwrdtq|gwrtq|kidney\" SOD_pages.txt | head; grep -n -E \"^word,|^verb,|^irony,|^vertere|^version,\" KLN_1966.txt | head; grep -n -E \"^vart-|vart- \" KNT_full.txt | head -5; grep -n -E \"^WORD|^VERB|^IRONY\" SKT.txt | head"
}
```


### [2026-10-17T00:05:37.563Z] TOOL RESULT

```
16306:                 TSP 6.46, 147; VJ 1262; BSTBL, Padm. 21, 50;              kidneyCr)
16322:                TSP 3.220, swk}nt Ywrtk; Schwartz. SI, Et.                  first day of the month
16353:                  Ywrdtq-y "kidney" ?; C2 n pi 78                     4430 Ywrt B, S          {uj^ y^ ^)cJL^tS^i^jy>--
16363:       xwart, xurt (ywrtk-) ©pt. st. & inf. =*ywr-\            4443 Ywry zync(h) =» ywryznych
16371:4432 Ywrt'k S =» ywrtk                                         4445 Yws'nty'kh     B                               ^^->
16384:4435 Ywrtk B                                      U*<^lj>.          xusenc ©Khwar. xwsy
16389:4436 Ywrtk- *» ywil-
38677:(to)pin 6605, 6732, 7580, 7621         kidney      4423                        knowledgable       8109
2908:Lex. s.v. vart- for reff. ; | 
28821:vart- vb. ‘turn’, trans. in active, гей. or in- 
20687:VERB,
20734:VERBENA.
```


## [2026-10-17T00:05:40.702Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 16296,16360p SOD_pages.txt | cut -c1-120; awk 'BEGIN{RS=\"\\f\"}{n+=gsub(/\\n/,\"\\n\"); if(n>=16353){print NR-1; exit}}' SOD_pages.txt; sed -n 28815,28830p KNT_full.txt"
}
```


### [2026-10-17T00:05:41.123Z] TOOL RESULT

```
            4411 ywpyh S                                         ^^         STi 39.7; BBB p84.703; GMS 215, 421
                 xOpya, xupl                                           4422 Ywr'ytfk B                                  
■! # < '         goodness                                                   xwarene ©pres. part. =»xwrynyy
                 Frag. Len. 68.7                                            eater
            4412 Ywr B, S                                                   TSP 2.803
                   xwr0xur
                 xwar, Yyy ©ob. -y      ^YwrW, YwYr> xwr>              4423 Ywrdtq C                          6i/<(U)«jr
                                                                            Yur5ak ? ©Av. vdrd8ka\ Yaghn. Yurkakx Yidg.
                 sun
                                                                             ww/^a; MP gurdag; Knot. Z>//£<2 ©f. gen. -y
                 TSP 6.46, 147; VJ 1262; BSTBL, Padm. 21, 50;              kidneyCr)
                   Frag. Lcn. 94.6; GMS 223, 1611; Hen. Tales.               ^Y^^tqy'
                                                                           C2, 102V30 n pl78; S W, BSOAS 1983, 49
                    481.34; Sogdica. 34.8, cYwr, "of sun"
            441 3 Ywr-1 B, S                                          4424 Ywrm(h) B                                    
                                                 (j,>> >^ ^)0^>
                  xwar, xur ©<*xwar ~>Ywrt~. xwr-                          xurm ©<*xrum-, Av. paxruma ©ob. -y
                  (ro)cat           \                                        =»xwrm, ywrwm
                                                                            earth, dust
                 EGSii 9; GMS 229, 592; inf. Ywr'y, TSP 2.134;
                                                                            GMS 415; SCE 15g, 133; Bailey. Asica. 33
                   Dhy. 279, trans, pret. YwrtS}r-> AVS 103
                                                                              xruma; Gersh. AHM 189; VJ 1466, 1470, 1477
           4414 Ywr-J S                               j^^xf^
                xur ©*hvan IE *swel -»swk'nt                          4425 Ywrmzt rwc     S                 jjj-*^^ "u J
                (to)swear                                                   xurmazd roc ^xwrmzl* rwc, 'ywrmzt rwc
                TSP 3.220, swk}nt Ywrtk; Schwartz. SI, Et.                  first day of the month
                  Lazard, cahicr 7, 293-5                                  MDii;MDiii, B-ll R3
                                                                      4426 Ywrn- B                                     u
           4415 Ywr'Ywr'k B                        ? jjK* «j.p-Up
                xwar-xware, xura-xure ?                                    xurn ©Av, vohuna-, Khot. huna\ Parth. gwxn\
                eater, glutton                                                Yaghn. waxin ©nom. -y, -w, ob. -(>,y; abl.
                TSP 24.6                                                      =>wYrn-(h), ywxn-, xwrn-
                                                                            blood
           4416 Ywr'k(h) B                             jj>o^*               GMS 209, 417; TSP 2.114, 348, 297 etc.; VJ 2
                yure, Yurak ©<*garu ? =»Ywrv                                 783; Bailey. Prolexis. 426
                proud, haughty
                                                                      4427 Y^r rwc S                    jjj-^jj^ *A* f*>
                SCE 370; TSP 5.51; GMS 1074a
                                                                           xur roc =»xwr rwc
           4417 YwrYS B                                      VU*7          eleventh day of the month
                xwar-arG, xur-ar9 ©<xwar+ar9 <*a&r                         MDii B-3, 3, B-19, 11
                sunlight
                                                                      4428 Ywrs B, C                                ;/<-
                TSP 22.20 n p235
                                                                           Yurs ©<*garsu <*gartsu
           4418 Ywr't- =* wYr}ty(y)                                        round, around
           4419 Ywr>t>nyh B                              jjJ"J&            GMS 488, 954; SCE 299; TSP 5.10, 58; STi 19.1
                Yuratanya ©f. n.                                             C2, 60V23, 111R6; Hen. Sogdica. 57
                haughtiness                                           4429 Ywrst^ny B          (^<^>)^->>^ ^jX'OjJ
                SCE 72; GMS 1074a
                                                                           Yurstane ©<*gavar6 ?; Khot. gausa-> Pash. Yos
           4420 Ywr>tqy) C                         ? tfJ-'wJ^                OP *gavar&a= EL kamirOa
                Yuratakya ? =*yv/rdtq                                      millet
                watchfulness ?
                                                                           TSP 2.1019 n pl82; Hen. Texts. 724; Gersh.
                BSTii 831.30; Mack. BSOAS 33, 12; S W,                       Amber. 1969, 198
                  Ywrdtq-y "kidney" ?; C2 n pi 78                     4430 Ywrt B, S          {uj^ y^ ^)cJL^tS^i^jy>--
           4421 Ywr'ty C                           jU^Li*                  xwart, xurt ©<xvarti =*xwrt
                yurate ©Yaghn. Yurah <wYrHk <*wigrataka                    food, meal
                  ©pi. -r                                                  GMS 947 263n 1; VJ; TSP 3.216, 13.7 etc.; SCE
                watchful, awake                                              BSTBL; Frag. Len^ Frag. 2a.l5; MDii; Ywrtw 
 177
                                                                       *=^xwrjn(y)c
  TSP 6.87; Ywrty, TSP 2.416; VJ 110 etc.; YwrPk, MDii                                                            Yws'yc
241
the third a’s may have been long). 


varga- sb., see haumavarga-. 


vart- vb. ‘turn’, trans. in active, гей. or in- 
trans. in middle: Av. varat-, Skt. vrl-, pres. várlati 
vdrtate, LA. vertit, Gm. werden ‘become’, pIE *uert-. 
[valriaiyary ist sg. mid. caus. (831, $48, $215, 
. $233.II; JAOS 62.275, 63.67-8) DB 444 (Camer- 
on’s reading; not upa- + à + varl-, \updvalriary 
with dittography in -"tysiy*, as proposed by Tm. 
Vat. Stud. 1.30-1, Lex. 122; for other restorations, 
see Gray JAOS 23.60-2, Bthl. WZKM 22.69, Wb. 
ZDMG 61.728, HK Phil. Nov. 3.103, ApKT 1.61,
```


## [2026-10-17T00:05:49.199Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^(word|verb|irony|verse|version)\\b\" KLN_1966.txt | head; grep -n -E \"^(word|verb|irony)\\b\" KLN_1971.txt | head"
}
```


### [2026-10-17T00:05:49.623Z] TOOL RESULT

```
1068:verb
1328:word  and  -ion.
1795:word  of  uncertain  origin,  and  of  fipvu;,  ‘bird’, for  which  see  ornitho-.
6406:word  with  dimin.  suff.  -et. canto,  n.,  chief  division  of  a  long  poem.  —  It., ‘song’,  fr.  L.  cantus,  ‘song',  fr.  cant-(um),  pp. stem  of  canere,  ‘to  sing’.  See  cant,  ‘slang  of beggars’.
9403:word  from  which  Buffon  coined  F.  couguar. cough,  intr.  v.  —  ME.  cowhen,  coughen,  fr.  OE. *cohhian  (whence  OE.  cohhetan,  ‘to  make  a noise’),  rel.  to  MDu.  cochen,  Du.  kuchen,  ‘to cough’,  MHG.  kuchen,  ‘to  breathe’.  Cp.  G. keuchen,  ‘to  pant,  gasp’,  which  is  a  blend  of MHG.  kuchen,  ‘to  breathe’,  and  kichen,  ‘to pant’.  For  this  latter  see  chincough. Derivatives;  cough ,  n.,  cough-er,  n. could,  aux.  v.  —  Past  tense  of  can,  fr.  ME.  coude, fr.  OE.  cuj ’e.  The  /  in  could  is  etymologically  in¬ correct  and  due  to  the  analogy  of  should  and would.
9513:word  and  cp.  Swed.  krabapple. crabbed,  adj.,  peevish,  morose.  —  Lit.  ‘resembling a  crab’.  Formed  fr.  crab,  the  animal,  with  suff.
14003:word  and  -ic,  resp.  also  -al.
14201:word  and  -ion.
15818:word  gas  was  used  for  the  first  time  by  Para¬ celsus  (died  in  1541),  who  named  the  air  by  it. Derivatives :  gas,  tr.  v.,  gaseity,  gaseous,  gasser, gassy  (qq.v.)
16351:word  with  frequent,  suff.  -/. gnarled,  adj.,  knotted.  —  A  var.  of  knurled, ‘knotted’,  fr.  knurl  (q.v.);  first  used  by  Shake¬ speare.
422:word with the second element in acrobat. (Acrobats are used to display their art in the height.) 
3770:word) 
3805:verb 
4421:word and -ive. 
4662:word. 
4921:word and -ent 
5255:word. 
5284:word and -ant. 
5338:word. 
5346:word and -ion.
```


## [2026-10-17T00:05:57.228Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o -E \"(^| )word, n\\.[^.]{0,40}.{0,500}\" KLN_1966.txt | head -3; grep -o -E \"irony, n\\..{0,400}\" KLN_1966.txt | head -2; grep -o -E \"verb, n\\..{0,300}\" KLN_1966.txt | head -2"
}
```


### [2026-10-17T00:05:58.257Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:06:01.574Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"irony,  ?n\" KLN_1966.txt | head -3; grep -n -E \"word,  ?n\\.  ?—\" KLN_1966.txt | head; grep -n -E \"verb,  ?n\\.\" KLN_1966.txt | head -3"
}
```


### [2026-10-17T00:06:01.933Z] TOOL RESULT

```
19901:Derivative:  ironmoid,  tr.  and  intr.  v. irony,  n.  —  L.  ironia,  fr.  Gk.  eEpcoveta,  ‘irony’, fr.  Eipcov,  ‘dissembler’,  for  *frpicov,  lit.  ‘sayer’ (i.e.  one  who  speaks  in  order  to  hide  his thoughts),  fr.  etpco  (for  *T£pico),  ‘I  say,  speak’, which  is  rel.  to  pf)T&>p,  Aeol.  fpf]Tojp,  ‘public speaker,  orator;  rhetor’,  and  cogn.  with  L. verbum,  ‘word’,  Goth,  waiird,  OE.  word,  ‘word’. See  word  and  cp.  rhetor.  Cp.  also  verb, irony,  adj.  —  Formed  fr.  iron  with  adj.  suff.  -y. irradiance,  irradiancy,  n.  —  Formed  from  next word  with  suff.  -ce,  resp,  -cy. irradiant,  adj.  —  L.  irradians,  gen.  -antis,  pres, part,  of  irradiare.  See  next  word  and  -ant. irradiate,  tr.  and  intr.  v.  —  L.  irradiatus,  pp.  of irradiare,  ‘to  illumine,  cast  forth  rays,  irradiate’, fr.  in-,  ‘in’,  and  radidre,  ‘to  shine  with  rays’.  See radiate.
15162:See  forest  and  agential  suff.  -er. forestry,  n.  —  OF.,  fr.  forestier,  ‘forester’.  See prec.  word  and  -y  (representing  F.  -ie). foreword,  n.  —  Loan  translation  of  G.  Vorwort.
37760:sword,  n.  —  ME.  swerd.  fr.  OE.  sweord,  swurd, sword,  rel.  to  OS.,  OFris.  swerd,  ON.  sverd.
1748:adverb,  n.  —  F.  adverbe ,  fr.  Late  L.  adverbium, ‘adverb’,  lit.  ‘that  which  is  added  to  the  verb’, coined  by  the  grammarian  Flavius  Sosipater Charisius  fr.  ad,  ‘to’,  and  verbum,  ‘word;  verb’ (see  ad-  and  verb),  as  a  loan  translation  of  Gk. i~i-p  r/j.oc,  ‘adverb’,  lit.  ‘that  which  is  said  after¬ ward’  (see  epi-  and  rhetor). adverbial,  adj.  —  Late  L.  adverbialis,  ‘pertaining to  an  adverb’,  fr.  adverbium.  See  prec.  word and  -iai,
30716:Derivative:  provender,  tr.  v. provenience,  n.,  provenance.  —  Formed  with suff.  -ce  fr.  L .  praveniens,  gen.  -ends,  pres.  part, of  provenire.  See  provenance, proverb,  n.  —  ME .  proverbe,  fr.  OF.  (=  F.)  pro- verbe,  fr.  L.  proverbium,  ‘proverb’,  fr.  1st  pro- and  verbum,  ‘word’.  See  verb, proverbial,  adj.  —  Late  L.  proverbialis,  fr.  L.  pro¬ verbium.  See  prec.  word  and  adj.  suff.  -al. Derivatives:  proverb,  tr.  v.,  proverbial-ist,  n., proverbial-ly ,  adv.
```


## [2026-10-17T00:06:05.626Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \"word,  ?n\\.  ?— .{0,700}\" KLN_1966.txt | grep -i \"wurd\\|Goth\" | head -2; grep -n -o -E \"verb,  n\\.  — .{0,400}\" KLN_1966.txt | head -2; grep -n -o -E \"(vertere|version,  n\\.).{0,300}\" KLN_1966.txt | head -3"
}
```


### [2026-10-17T00:06:06.004Z] TOOL RESULT

```
37760:word,  n.  —  ME.  swerd.  fr.  OE.  sweord,  swurd, sword,  rel.  to  OS.,  OFris.  swerd,  ON.  sverd.
1748:verb,  n.  —  F.  adverbe ,  fr.  Late  L.  adverbium, ‘adverb’,  lit.  ‘that  which  is  added  to  the  verb’, coined  by  the  grammarian  Flavius  Sosipater Charisius  fr.  ad,  ‘to’,  and  verbum,  ‘word;  verb’ (see  ad-  and  verb),  as  a  loan  translation  of  Gk. i~i-p  r/j.oc,  ‘adverb’,  lit.  ‘that  which  is  said  after¬ ward’  (see  epi-  and  rhetor). adverbial,  adj.  —  Late  L.  adverbiali
30716:verb,  n.  —  ME .  proverbe,  fr.  OF.  (=  F.)  pro- verbe,  fr.  L.  proverbium,  ‘proverb’,  fr.  1st  pro- and  verbum,  ‘word’.  See  verb, proverbial,  adj.  —  Late  L.  proverbialis,  fr.  L.  pro¬ verbium.  See  prec.  word  and  adj.  suff.  -al. Derivatives:  proverb,  tr.  v.,  proverbial-ist,  n., proverbial-ly ,  adv.
1754:vertere.  See  advert.
1755:vertere,  ‘to  turn  toward’,  fr.  ad-  and  vertere,  ‘to turn’.  In  English,  the  word  has  been  refashion¬ ed  after  L.  advertere.  See  version  and  cp.  adver¬ tise  and  the  second  element  in  animadvert.  Cp. also  avert,  controvert,  convert,  covert,  culvert, divert,  extrovert,  intr
1757:vertere.  See  advert  and -ent  and  cp.  inadvertent.
```


## [2026-10-17T00:06:11.240Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \".{0,10}Goth\\.  ?waurd.{0,300}\" KLN_1966.txt | head -5; grep -n -o -E \"version,  n\\.  —.{0,600}\" KLN_1966.txt | head -2"
}
```


## [2026-10-17T00:06:13.433Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \" verb,  n\\.  —.{0,600}\" KLN_1966.txt | head -2; grep -n -o -E \" word,  n\\.  —.{0,700}\" KLN_1966.txt | head -2; grep -n -o -E \"Avestan  ?urvata|Avest\\.  ?urv.{0,80}\" KLN_1966.txt | head; grep -n -o -E \".{0,200}varetaiti.{0,300}|.{0,100}Avestan  varst.{0,200}\" KLN_1966.txt | head -3"
}
```


### [2026-10-17T00:06:15.940Z] TOOL RESULT

```
4108:version,  n.  —  F.,  fr.  L.  aversidnem,  acc.  of  dver- sio,  ‘a  turning  away’,  fr.  aversus,  pp.  of  aver- tere.  See  next  word  and  -ion. avert,  tr.  v.,  to  prevent,  ward  off.  —  L.  avertere, ‘to  turn  away’,  fr.  d,  ‘away  from’,  and  vertere, ‘to  turn’.  See  a-,  ‘away  from’,  and  version. Derivatives:  avert-ed,  adj.,  avert-ed-h ,  adv., avert-ible,  adj.
9062:version,  n.  —  F.,  fr.  L.  conversionem,  acc.  of conversio,  ‘a  turning  round’,  fr.  convertere,  ‘to turn  round'.  See  con-  and  version  and  cp. convert.
```


### [2026-10-17T00:06:19.222Z] TOOL RESULT

```
ugrep: error: error at position 176
?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
       exceeds complexity limits___/
```


## [2026-10-17T00:06:25.308Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^verb,|^word,|^version,| verb,  n\\.| word,  n\\.  —  ME|version,  n\\.  —  F\\.,  fr\\.  ML\" KLN_1966.txt | head; python3 - <<'E'\nimport re\nt=open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt').read()\nfor pat in [r'verb, +n\\. +— +F\\. verbe',r'word, +n\\. +— +ME\\. word',r'version, +n\\. +— +F\\.',r'urvata']:\n    for m in re.finditer(pat,t):\n        print(pat,'::',t[m.start():m.start()+700].replace('\\n',' '));print()\nE"
}
```


### [2026-10-17T00:06:25.779Z] TOOL RESULT

```
version, +n\. +— +F\. :: version,  n.  —  F.,  fr.  L.  aversidnem,  acc.  of  dver- sio,  ‘a  turning  away’,  fr.  aversus,  pp.  of  aver- tere.  See  next  word  and  -ion. avert,  tr.  v.,  to  prevent,  ward  off.  —  L.  avertere, ‘to  turn  away’,  fr.  d,  ‘away  from’,  and  vertere, ‘to  turn’.  See  a-,  ‘away  from’,  and  version. Derivatives:  avert-ed,  adj.,  avert-ed-h ,  adv., avert-ible,  adj. Aves,  n.  pi.,  the  class  of  birds  ( zool .)  —  L.  axes pi.  of  avis,  ‘bird’.  See  aviary. Avesta,  n.,  the  sacred  books  of  the  Parsees.  — Pers.,  earlier  form  Avistak,  lit.  ‘text’.  Cp.  Zend- Avesta. Derivatives:  Avest-an,  Avest-ic,  adjs. aviarist,  n.,  one  who  keeps  an  aviary

version, +n\. +— +F\. :: version,  n.  —  F.,  fr.  L.  conversionem,  acc.  of conversio,  ‘a  turning  round’,  fr.  convertere,  ‘to turn  round'.  See  con-  and  version  and  cp. convert. Derivatives:  conversion-al,  conversion-ary,  adjs. conversive,  adj.  —  F.  conversif  (fem.  conversive), fr.  L.  conversus,  pp.  of  convertere.  See  convert and  -ive. convert,  tr.  v.  —  OF.  (=  F.)  convertir,  fr.  VL. *convertire,  corresponding  to  L.  convertere,  ‘to turn  round’,  which  is  formed  fr.  con-  and  ver- tere,  ‘to  turn’.  See  version. Derivatives:  convert,  n.,  convert-er,  n.,  con¬ vertible  (q.v.),  convert-ive,  adj. convertible,  adj.  —  F.,  fr.  Late  L.  convertibilis, ‘chang

version, +n\. +— +F\. :: version,  n.  —  F.  eversion,  fr.  L.  eversionem,  acc. of  eversio,  ‘a  turning  out,  overthrowing’,  fr. eversus,  pp.  of  evertere,  ‘to  turn  out,  twist,  over¬ throw’,  fr.  e-  and  vertere,  ‘to  turn’.  See  version, evert,  tr.  v.,  1)  to  overthrow  (archaic)  -,  2)  to  turn inside  out.  —  L.  evertere.  See  prec.  word, every,  adj.  —  ME.  everilk,  everich,  even,  lit.  ‘ever each’,  fr.  OE.  S/re,  ‘always,  ever’,  and  xlc, ‘each’.  See  ever  and  each, evict,  tr.  v.,  to  dispossess  by  law.  —  L.  evictus, pp.  of  evincere,  ‘to  overcome  completely,  van¬ quish;  to  recover  one’s  property’.  See  evince, eviction,  n.  —  Late  L.  evict  id,  g
```


## [2026-10-17T00:06:31.836Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nfor fn in ['KLN_1966.txt','KLN_1971.txt']:\n  t=open(fn).read()\n  for pat in [r'vartate',r'urvata',r'\\bverbum, +.word.',r'wordy,']:\n    ms=list(re.finditer(pat,t))\n    print(fn,pat,len(ms))\n    for m in ms[:2]:\n        print('   ',t[max(0,m.start()-500):m.start()+400].replace('\\n',' '));print()\nE"
}
```


### [2026-10-17T00:06:33.122Z] TOOL RESULT

```
KLN_1966.txt vartate 0
KLN_1966.txt urvata 0
KLN_1966.txt \bverbum, +.word. 4
    fr. OF.  aventurer,  fr.  aventure.  See  adventure,  n. Derivatives:  adventur-er,  n.,  adventur-ess,  n. adventurous,  adj.  —  ME,  aventurous,  fr.  OF.  aven- turos  (F.  aventureux),  fr.  aventure.  See  adven¬ ture,  n.,  and  -ous. Derivatives:  adventurous-ly,  adv.,  adventur-ous- ness,  n. adverb,  n.  —  F.  adverbe ,  fr.  Late  L.  adverbium, ‘adverb’,  lit.  ‘that  which  is  added  to  the  verb’, coined  by  the  grammarian  Flavius  Sosipater Charisius  fr.  ad,  ‘to’,  and  verbum,  ‘word;  verb’ (see  ad-  and  verb),  as  a  loan  translation  of  Gk. i~i-p  r/j.oc,  ‘adverb’,  lit.  ‘that  which  is  said  after¬ ward’  (see  epi-  and  rhetor). adverbial,  adj.  —  Late  L.  adverbialis,  ‘pertaining to  an  adverb’,  fr.  adverbium.  See  prec.  word and  -iai, derivative:  adverbial-ly,  adv. •dversaria,  n.  pi.,  miscellaneous  notes.  —  L.  ad¬ versaria  (s

    tered  fr.  iron  mole  by  folk  ety¬ mology,  which  associated  this  word  with  mold. See  iron  and  mole,  ‘spot’. Derivative:  ironmoid,  tr.  and  intr.  v. irony,  n.  —  L.  ironia,  fr.  Gk.  eEpcoveta,  ‘irony’, fr.  Eipcov,  ‘dissembler’,  for  *frpicov,  lit.  ‘sayer’ (i.e.  one  who  speaks  in  order  to  hide  his thoughts),  fr.  etpco  (for  *T£pico),  ‘I  say,  speak’, which  is  rel.  to  pf)T&>p,  Aeol.  fpf]Tojp,  ‘public speaker,  orator;  rhetor’,  and  cogn.  with  L. verbum,  ‘word’,  Goth,  waiird,  OE.  word,  ‘word’. See  word  and  cp.  rhetor.  Cp.  also  verb, irony,  adj.  —  Formed  fr.  iron  with  adj.  suff.  -y. irradiance,  irradiancy,  n.  —  Formed  from  next word  with  suff.  -ce,  resp,  -cy. irradiant,  adj.  —  L.  irradians,  gen.  -antis,  pres, part,  of  irradiare.  See  next  word  and  -ant. irradiate,  tr.  and  intr.  v.  —  L.  ir

KLN_1966.txt wordy, 0
KLN_1971.txt vartate 0
KLN_1971.txt urvata 1
    L. verbum , ‘word’. (For the change of  I.-E. dh to b in Latin cp. L. ruber and E. red, L.  barba and E. beard.) I.-E. *werdh- is an en-  larged form of base *wer~, * were-, * were-, ‘to  speak’, whence Gk. efpo> (for *f£pio>), ‘I say,  speak’, etpcov (for *F£puov), ‘dissembler’, lit.  ‘sayer’ (i.e. one who speaks in-order to hide his  thoughts), elpcoveta, ‘irony’, p7)Tcop, Aeol.  fp7)Ta>p, ‘public speaker, orator; rhetor’,   (for *fp95p.a), ‘word’, OI. vratam, ‘command-  ment, order’, Avestic urvata-, of s.m., OSlav.  rota (for *vrota), ‘oath’, vraci, ‘physician, magi-  cian’, Hitt, weriya-, ‘to call’, and prob. also  Hitt, huwart-, ‘to curse’. Cp. hermeneutic, irony,  rhetor, verb, verve.   Derivatives: word, tr. v., word-able, adj., word-  -abl-y, adv., word-age, n., word-ed , adj., word-er,  n., word-ing, n., word-less, adj., wordy (q.v.)  wordy, adj. — ME., fr. OE. wordig, fr. word

KLN_1971.txt \bverbum, +.word. 3
     ModL.,  coined by the French naturalist Jean-Bap tiste  Audebert (1759-1800).   rhetor, n., teacher of rhetoric; orator. — L., fr,  Gk. ^Tjxtop (Aeol. *Fp^xtopj, ‘public speaker,  orator; rhetor’, rel. to'^pwc, ‘word’, lit. ‘that  which is spoken’, pTjou;, ‘speech’, and to etpoi  (for *F£pto>), ‘I say, speak’, elpcov (for *F&-  picov), ‘dissembler’, lit. ‘sayer’ (i.e. one who  speaks in order to hide his thoughts), el p cove! a,  ‘irony’, and cogn. with OI. vratdm , ‘command-  ment, order’, L. verbum, ‘word’, Goth, waurd,  OE. word , ‘word’. See word and cp. irony. Cp.  also verb.   rhetoric, n. — ME. rethorik, fr. OF. rhetorique  (F. rhetorique ), fr. L. rhetorica, rhetorice ', fr. Gk.  £7)Top»d) (scil. ‘art of rhetoric’, fem. of   ^7jToptx6?, ‘fit for a public speaker or public  speaking, oratorical; rhetorical’, fr. fa t T6jp, gen.  ^T)Topog. See prec. word and -ic.   Derivatives : r

    id,  word; verb’.   verbal, adj. — Late L. verbalis, fr. L. verbum,  ‘word’. See verb and adj. suff. -al.   Derivatives: verbal-ism, n., verbal-ist, n., verbal-  ize, tr. and intr. v,, verbal-iz-ation , n., verbal-iz-  er, n., verbal-ly , adv., verb-y, adj.   Verbascum, n., a genus of plants, the mullein  (bot.) — L. verbascum, ‘mullein’, prob. of Ligu-  rian origin. Cp. b&rbasco.  verbatim, adv., word for word; adj., following  word for word. — ML. verbatim, ‘word for  word, literally’, fr. L. verbum, ‘word’. See verb.  For the suff. -dtim see gradatim and cp. words  there referred to.   Verbena, n., a genus of plants, the vervain (bot.)  — L. See vervain.   Verbenaceae, n. pi., the vervain family (bot.) —  ModL., formed fr. prec. word with Suff. -aceae.  verbenaceous, adj. — See prec. word and -aceous.  Verbesina, n., a genus of herbs, the crownbeard  (bot.) — ModL., arbitrarily formed

KLN_1971.txt wordy, 1
    a, ‘irony’, p7)Tcop, Aeol.  fp7)Ta>p, ‘public speaker, orator; rhetor’,   (for *fp95p.a), ‘word’, OI. vratam, ‘command-  ment, order’, Avestic urvata-, of s.m., OSlav.  rota (for *vrota), ‘oath’, vraci, ‘physician, magi-  cian’, Hitt, weriya-, ‘to call’, and prob. also  Hitt, huwart-, ‘to curse’. Cp. hermeneutic, irony,  rhetor, verb, verve.   Derivatives: word, tr. v., word-able, adj., word-  -abl-y, adv., word-age, n., word-ed , adj., word-er,  n., word-ing, n., word-less, adj., wordy (q.v.)  wordy, adj. — ME., fr. OE. wordig, fr. word. See     word and -y (representing OE. -ig).   work, n. — ME. werk , work, fr. OE. were, wore,  weorc , ‘work, act, action’, rel, to OS. OFris.,  Du. werk, ON. verk, Dan. vterk, Swed. verk,  MDu. ware , weorc , were, OHG. werah, were ,  MHG. werch, were, G. Werk, Goth, gawaurki,  ‘work’, fr. I.-E. base *werg-, ‘work, to work’,  whence also Avestic var e
```


## [2026-10-17T00:06:40.466Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('KLN_1971.txt').read()\nfor pat in [r'version, n\\.',r'Avestic var.?t',r'verb, n\\.']:\n    for m in list(re.finditer(pat,t))[:3]:\n        print(pat,'::',t[max(0,m.start()-100):m.start()+900].replace('\\n',' '));print()\nE"
}
```


### [2026-10-17T00:06:40.861Z] TOOL RESULT

```
version, n\. ::  anile. — L. anllitas,  ‘the old age of a woman, anility’, fr. anllis. See  anile and -ity.   animadversion, n., criticism; blame. — L. ani-  madversio, gen. -dnis, ‘perception, observation,  attention’, fr. animadversus, pp. of animadver-  tere. See animadvert and -ion.   Derivative: animadversion-al , adj.      37     ANNOY     animadversive, adj., percipient. — Formed with  suff. -ive fr. L. animadversus , pp. of animadver-  tere. See next word.   Derivative: animadversive-ness, n.  animadvert, intr. v., to criticize, blame, censure.  — L. animadvertere, contraction of animum ad -  vertere , ‘to direct one’s mind, attend’, fr. ani-  mum, acc. of animus , ‘mind’, and advertere, ‘to  turn toward’. See animus and advert,  animal, n. — L., lit. ‘a living being’, fr. animate ,  neut. of animalis, ‘of air, living’, fr. anima,  ‘breath of air, air, breath, soul, life* ; see animus  and adj. suff. -al. For sense development cp. Gk.  £<£ov, ‘animal, which is rel. to Conf), ‘life’, and  OE. d

version, n\. :: rsus, ‘turned away’, pp. of  dvertere. See avert.   Derivatives: averse-ly, adv., averse-ness, n.  aversion, n. — F., fr. L. aversionem , acc. of dver-  sio, ‘a turning away’, fr. aversus , pp. of dver-  tere. See next word and -ion.  avert, tr. v., to prevent, ward off. — L. avert ere,  ‘to turn away’, fr. a, ‘away from’, and vertere,  ‘to turn’. See a-, ‘away from’, and version.  Derivatives: avert-ed y adj., avert-ed-ly, adv.,  avert-ible, adj.   Aves, n. pi., the class of birds (zool.) — L. aves  pi. of avis, ‘bird’. See aviary.   Avesta, n., the sacred books of the Parsees. —  Pers., earlier form Avistak, lit. ‘text’. Cp. Zend-  Avesta.   Derivatives: Aves t- an, Avest-ic , adjs.  aviarist, n., one who keeps an aviary. — See next  word and -ist.   aviary, n., a place in which birds are kept. —  L. aviarium , ‘a place where birds are kept, an  aviary’, fr. avis , ‘bird’, which is cogn. with OI.  vih, v£h, Avestic vish, ‘bird’, OI. vayas-, ‘fowl,  bird’, Gk. oderoc, Att. < 4 er 6 <;

version, n\. :: se, adj., reversed in order. — L. comersus,  pp. of conver ter e, ‘to turn about’. See convert,  conversion, n. — F., fr. L. comer sionern, acc. of  conversio, ‘a turning round’, fr. convertere, ‘to  turn round’. See con- and version and cp.  convert.   Derivatives: comersion-al , conversion-ary, adjs.  conversive, adj. — F. conversif (fem. comersive),  fr. L. comersus, pp. of convertere. See convert  and -ive.   convert, tr. v. — OF. (= F.) convertir, fr. VL.  *comertire, corresponding to L. convertere, ‘to  turn round’, which is formed fr. con- and ver-  tere, ‘to turn*. See version.   Derivatives: 4 convert, n., convert-er, n., con-  vertible (q.v.), convert-ive , adj.  convertible, adj. — F., fr. Late L. comer tibilis,  ‘changeable’, fr. L. convertere. See prec. word  and -ible.   Derivatives: convertible, n., conver tibil-ity, n.,  comer tible-ness, n., convertibl-y , adv.  convex, adj. — F. convexe, fr. L. convex us, ‘vault-  ed, arched’, which is usually explained as lit.  meani

Avestic var.?t ::  (intr.), var-  tulah , ‘round’, vgttdh, ‘rolled, twisted, round’,  vf ttih y ‘the act of rolling’, Avestic var*t-, ‘to  turn’ (intr.), OSlav. vruteti, ‘to turn, roll’, vratiti ,  of s.m., vreteno , Russ, vreteno , ‘spindle, distaff’,  OSlav. vrime, ‘time’, vriisti, ‘condition, situa-  tion’, vrusta, ‘stadium’, Gk. ponrotVT), ‘stirrer,  ladle’, Lith. verciu , vefsti, ‘to turn’, vartyti , ‘to  turn to and fro’, virstu, vifsti , ‘to fall over’,  Mir. fersaid, ‘club’, W. gwerthyd , ‘spindle, dis-  taff’, OIr. frith , ‘against’, Toch. B wrattsai , of  s.m., Goth, walrpan , OHG. werdan, MHG., G.  werden , OE. wenrdo/i, ‘to become’. For the sense  development of these Teut. words cp. E. to turn  in the sense of to become (e.g. ‘to turn cold’).  See -ward, weird, worth, ‘to become’, and cp.  adverse, adversity, advert, advertise, animadvert,  anniversary, a rovescio, averse, aversion, avert,  controverse, controversy, controvert, conversant,  conversation, converse, convert, dextrorse, divers

verb, n\. ::  See adven-  ture, n., and -ous.   Derivatives: adventurous-ly , adv., adventur-ous -  ness, n.   adverb, n. — F. adverbe , fr. Late L. adverbium,  ‘adverb’, lit. ‘that which is added to the verb’,  coined by the grammarian Flavius Sosipater  Charisius fr. ad, ‘to’, and verbum , ‘word; verb’  (see ad- and verb), as a loan translation of Gk.  errlpp7){xa, ‘adverb’, lit. ‘that which is said after-  ward’ (see epi- and rhetor).  adverbial, adj. — Late L. adverbialis , ‘pertaining  to an adverb’, fr. adverbium. See prec. word  and -ial.   Derivative: adverbial-ly, adv.  adversaria, n. pi., miscellaneous notes. — L. ad-  versaria (scil. scripta ), lit. ‘writings turned to-  ward one’, neut. pi. of adversarius. See ad-  versary.   adversary, n. — OF. aversier , adversier, fr. L.  adversarius, ‘opponent, adversary, rival’, lit.  ‘turned toward one’. See adverse and subst.  suff. -ary. The insertion of the letter d in F. ad-  versaire, and E. adversary is due to the influence  of L. adversariu

verb, n\. :: d with  suff. -ce fr. L . proveniens, gen. - entis , pres. part,  of provenire. See provenance,  proverb, n. — ME. proverbe, fr. OF. (== F.) pro-  verbe, fr. L. proverbium , .‘proverb’, fr. 1st pro-  and verbum , ‘word’. See verb,  proverbial, adj. — Late L. pro verb ialis, fr. h.pro-  verbium. See prec. word and adj. suff. -al.  Derivatives: proverb, tr. v., proverbial-ist , n.,  proverbial-ly , adv.   provide, tr. and intr. v. — ME. providen, fr. L.  provider e, ‘to see beforehand, to act with fore-  sight’, fr. 1st pro- and videre , ‘to see’. See vision  and cp. purvey, which is a doublet of provide.  Cp. also improvise.   Derivatives: provid-ed , conj., providence (q.v.),  provid-er , n., provid-ing, conj. (prop. pres. part,  of provide ).     providence, n. — ME., fr. OF..(= F.) providence ,  fr. L. providentia, ‘foresight, foreknowledge’, fr.  providens , gen. -entis. See next word and -ce and  cp. prudence, which is a doublet of providence.  provident, adj. — ME., fr. L, provide

verb, n\. :: low’. See very.   Veratrum, n., a genus of plants, the false helle-  bore (bot.) — See prec. word,  verb, n. — ME. verbe , fr. MF. ( — F.), fr. OF., fr.  L. verbum , ‘word, verb’, which derives fr. I.-E.  base *werdh-, whence also Goth, waiird, OE.  word, ‘word’. See word and cp. also veracious,  veracity, veratrine, verbatim, verbiage, verbose,  proverb. For the change of I.-E. dh to b in Latin,  cp. L. ruber and E. red, L. barba and E. beard.  In its grammatical pense, L. verbum is a loan  translation of Gk. ^[xa, ‘that which is said,  word; verb’.   verbal, adj. — Late L. verbalis, fr. L. verbum,  ‘word’. See verb and adj. suff. -al.   Derivatives: verbal-ism, n., verbal-ist, n., verbal-  ize, tr. and intr. v,, verbal-iz-ation , n., verbal-iz-  er, n., verbal-ly , adv., verb-y, adj.   Verbascum, n., a genus of plants, the mullein  (bot.) — L. verbascum, ‘mullein’, prob. of Ligu-  rian origin. Cp. b&rbasco.  verbatim, adv., word for word; adj., following  word for word. — ML. verbati
```


## [2026-10-17T00:06:44.568Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"urvata|urvāta|vratá|vrata\" SYN.txt | head; grep -n -E \"KIDNEY|NECK|BELIEVE|WALNUT|DUST\" SYN.txt | head"
}
```


### [2026-10-17T00:06:45.129Z] TOOL RESULT

```
955:line hill Pol. gora; pagérek, Sp. montajia; colina, cerro Du. berg; heuvel wzg6rek Rum. munte; deal, colina OHG _ berg; buhil, houc Russ. gora; cholm Ir. sliab; telach, cnoc, bri MHG berg; biihel, hiibel, Skt. giri-, parvata-, acala-, NIr. — sliabh; cnoc (tulach) houc etc. W. mynydd; bryn (bre) NHG berg; hiigel Av. gairi-, paurvata, bara- Br. menez; Icrec’h, bre zah-, OPers. kaufa.
1016:Skt. parvata- ‘mountain, mountain range, rock’, Av. paurvata- ‘mountain range’, fr. adj. Skt. parvata- ‘knotty, rugged’, fr. parvan- ‘knot’.
7928:ChSl. vract, Russ. vraé = SCr. vraé ‘sorcerer, fortuneteller’, etc., orig. ‘con- jurer’ : Russ. voréat' ‘growl, grumble, mutter’, vraka ‘nonsense, idle talk’, etc., fr. the root *wer- in Grk. etpw ‘say’, Skt. vrata- ‘command, vow’, etc. Walde-P. 1.283. Solmsen, Unters. 263.
11719:» Opa; , : ys (pl.);  vartaz Tat, forés (pL), ore ON dyrr Ql), hurd; hlid, (pl.) inva; nora grind Lett. duris (pl.); vdrti (pl.) Br Perla, uscio 5 an. dr; port ChSI. dvtrt; vrata (pl.) Sh, Porle ae dérr; port SCr. vrata (pl.); vrata, Rum, Puerta Sai duru; geat, dor, port kapija Ir, Py Poarte ve dore; set Boh.  dvere (pl.); vrata (pl.), Nir, Ped (comla) ae door; gate rana Y. drwy 1a, doras, geata On, deur; poort Pol.  drzwi (pl.); brama, h, aiee dor; por th, ete, sae turt; tor, pforta wrota
11742:6. Lith. vartai, Lett. varti, OPruss. warto, ChS]., SCr., Boh. vrata, Pol. wrd- ta, Russ. vorota, all pl., general Balto- Slavic for ‘gate’ (but SCr. vrata also the
20562:Boh. vrata = Russ. utrata ‘loss’, cf. Boh. stratiti ‘lose’ fr. the root in Chl. tratitt ‘consume’ (11.33).
24214:3 Grk. rpcods, Att. rpirrds fr. *rpi- ys, also rpréds (Ion., but rerpatés, zeratés also in Aristotle), fr. *rprx8.s, formed fr. the advs. rpixa and rprx0a ‘n three parts’. In use often not dis- tinguishable from zpurAods in its various uses (which include the coll.) or in pl. ftom the simple cardinal. But the coll. sense seems dominant. Cf. Hdt. 6d:f6s Moos ‘twofold account’ = ‘two ac- counts’, Aristot. Metaph. érimeda rpirra, Yeaupal rerpatal, orvypal revratat ‘three (four, five) classes of planes (lines, points), and esp. the frequent use in the Ppytt for triplicate (etc.) copies, as ap Tploon Ypadetca ‘triplicate bill of te 1698.23) » Ypaupara Terpagod (ight) ag Ypagérra, contract in four ee bles (POxy. 1638.30, 171.4), Cre oa,
31586:Grk. fut. é&, perf. etpnxa, aor. pass. éppnOnv (pres. etpw Hom., but not com- mon), common in Hom. and later supple- menting déyw in both senses, beside de- rivs. sy7wp ‘public speaker’, piua ‘word, saying’, py7pa ‘agreement, covenant’, fr. Fep-, Fen- (cf. Arg. refpnuévos, El. cparpa, etc.), IE *wer- seen elsewhere in derivs. as Lat. verbum, OE word, etc. ‘word’, Av. urvata- ‘command’, Skt. vrata- ‘com- mand, vow’, etc. Walde-P. 1.283 f. Ernout-M. 1088f. Here also Hitt. weriya- ‘call, summon’ (Pedersen-Goetze, Mursilis Sprachlihmung 74).
845:1.213 DUST Grk. — xévts Goth. mulda, stubjus Lith. dulkés (pl.) NG oxéyn ON dupt, dust Lett. pisli (pl.), putelklz (pl.) Lat. pulvis Dan. stg ChSl.  prachii It. polvere Sw. stoft SCr. oprah Fr. poussitre OE dist Boh. prach Sp. polvo ME dust Pol. proch Rum. opraf, pulbere NE dust Russ. pyl Ir. luaithred Du. stof Skt.  renu-, pansu-, dhiali- Nir. luaithreadh OHG _ stuppi, stoub (melm) Av. pasnu- W. Ulwch, pylor MHG stoup Br. poulir NHG _ staub
6001:a 4.28 NECK NG ath? T#AxvAos, Bion Goth. als Lith. kaklas Lat. ob ON _hals, sviri Lett.  kakls ee colla Dan. _hals ChSl. vyja, Sia coy Sw. hals SCr. _ vrat (Sija) Sp. cuello OE heals, sweora Boh.  fkrk, sje om git Ms hals, swere, necke Pol. — szyja, kark I, = A D ve a faa ae Du. hals ar reel kantha-
11204:; i-, ap- : ES = ffe t wrist’) fr. ap at B clinking ornament’ (cf. kénkani- ‘adorn- lh a oka ‘hanes © Chsl grivina | ment with little bells’) fr. IE *kan-, in a Le Bulg. rine © Lat. canere ‘sing’, ete. Walde-P. 1.351. ee 6.75). h, ndramek, Pol. | Uhlenbeck 38. EG narubyicd, Bow ds. of na- ‘on’ Skt. karabhisana-, lit. ‘hand-adorn- ee im. ¢ ' = ranniennt hy all dim a SCr, ruka, | ment’, epd. of kara- ‘hand’ and bhisana- ve the d e. ' ‘adornment’ (6.71). 4 |. ram é, Pol. poh. ram 6.75 NECKLACE = ON men, halsgjord Lith. kaklarysis, karieliat Grk. pH arpentés, TEPt Dan. halsbaand Lett. kakla ruota i Sut halsband ChSl. meen grivina, iG xeptdtpato OE mene, healsbéag, ozrélt tat monile, torques sig(e)le SCr.  derdan it,  collana ME coler Boh.  ndhrdelnit Rr. Bie NE necklace Pol. naszynik §p. oe ghiordan Du. halssnoer Russ. ozerel’e (monisto) a Bones eanintore OHG menni, halsboug, hals- Skt. kanthika-, kantha- ; i golt bhiisa- a oo MHG _halsbouc, halsgolt Av. minu- Aue NHG  halsband
30147:17.27 TEACHER il a nor, REASON 17.28 ScHooL 7.12 tax! (= Reflect, etc.) 17.31 REMEMBER 17.18 Tams? (= Be of the Opinion) 17.32 Forcet 114 BELIEVE 17.33 Mranine
30326:17.15 BELIEVE
```


## [2026-10-17T00:06:50.427Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"\\*vart-|uart-|vart-\" ISS_alt_DKS.txt | head -8; awk 'BEGIN{RS=\"\\f\"} NR==8' incoming/BLY/BLY_pages.txt | grep -n -i -E \"gard|vart|gird|turn\" | head"
}
```


### [2026-10-17T00:06:50.905Z] TOOL RESULT

```
355:Puspaka'. Either base art- variant with vart- 'to roll', whence Sogd. wrin *vartana- and related words, or "urtara- from vari-, as in üdüra- 'crystal' to varta- ‘топе’, and a- replacing u-.
709:ahauda- ‘gourd’, п 1:8 ahauda vastya; Sid. 1872-3 ahoga, BS alabu-, Tib. ku-ba; и 88:153 ttird ahaudä hiya sará ' nut of bitter gourd’. See also byara- BS ervüru-. Base vart- 'to be round', hence aha-vri-a-, with üdara- * erystal! and Waxi wurt, Kurd. bard ‘stone’ (JRAS 1955, 22), naming the gourd "round like the belly’.
1087:üdára- ‘crystal’, Sid. 148vs ysirà, éamgd üdürd, її camdan ‘ochre, conch, crystal, white sandal-wood', BS sā- sankha-camdana-, 'Tib. ldon-ros dan, dun dan, mčhiv-bu dap, éandan dan. From base vart-:urt- with suffix -ára- as in gitsára-, gatsa- ' gypsum’ and Ау. daxsára- ' mark’ (and more frequently O.Ind. dngüra-, karmüra-, see Wack., Suffixe p. 386ff.). Hence with Iran. varta- ' stone', see ЈКАЗ 1955, 22, Waxi wurt, Kurd bard 'stone', Nüristini Aškun ша{, Kati шо, Dardic Khowar bort; second component N.Pers. làzavard, lasuvard, lájavard, BS lw rájavatya-, rüjapatta. То ТЕ Pok. 1138 uel- ' press together’, as Got. stama- ‘stone’ to IE stái- ‘Бе hard’. Sec also ira- ' jade', and urvarinai gará.
2499:nvistyi 'diarrhoea', 1 191, 111v2-3 aviysára vasiljáka noistyi büma va pirmüttam ' diarrhoea clearing, best for diarrhoea (BS atisara-), vomiting’, BS sarvütisara-vinüsana-; I 191-1122 pvistyi vasujaka u niysimümi ‘clearing diarrhoea and flux’; 1 191, 11372 si nä Вн aviysára jimdä pvistyä baña uskyüstà grrahagi padausa baña 'this amrta-medi- cament checks all kinds of atiszra-; it binds diarrhoea; it binds up grahami, padauga- (dyadic)', BS grahani 'chronic diarrhoea’, From *ni-ursti- to base vart- 'to roll’, with z- changed from n- by the former presence of -r-, rather than *ni-pasti 'falling down’, Parallel to pa- dausa, and 1 131, 61v3 badausta- from pa- and dau-i-, the form with suffix -£ to base dau-:du- ' ta run’, see padausa.
3808:nyüdàre ‘roll down’, 2 17:14 kho bassá nyüdāre samu ‘as streams roll down’; Z 17-14 Ru vàteo nyültte ' when then it rolls down’, Z 24-419 Ай mulu тийи nyültte harbisia hina ‘when indeed (- < uta) little by little the whole troop rolls down'. From ni-vart-, see cognates s.v. badàri ‘they roll’ (-iva- > -yi), secondary contact -rtat- > -Ítt-, аз baltte ' rolls'.
4625:pülsta- ‘hidden’, Z 24:387 pülstá kho ye ratanu nasta u di #fandau prīhä ‘hidden as one should take a jewel and hide it under the earth’ (simile of the tatAiágata-garbha ‘Buddha embryo"); Z 3:12 klaisyau pūlstä ‘hidden by klesa-afflictions’; Z 21-22 prrahonána pūlstä ‘hidden with clothes’, From *pa(ti)-vart- or *(a)pi-vart-, base var-, vart- ‘to cover’, beside "ni-vari- 'cover', Armen. lw nouartan (*nivartana-) 'covering'; Oss, D. miüárdun 'cover?, For var- ‘cover’ see s.v. bafha-, nyülte. IE Pok. 1160 yer- ‘cover’, With -Ist < -rt-t-.
4856:poaicam jsa jsü yadama ‘a (Turkish) yalma (‘raincoat’) with white coverings '; tt 110-8 pajsa pveca ' five coverings', taken as бета "woven stuff' by the asr (aryika) nun; п 9156-8 in a list ttu vai ysyai puaica ѓа haiysdai kaumadai fai u hada Фаїна cha u civarau phaurthaka fau büsinai їй pvaica üra 'that of his he carried off, one covering, to hand, one trousers and twenty feet of a cloak and robes (BS civara, -u ' and") and one phaurthaka (BS phuftaka-), one роаіса of byssus cloth in value (ara- ' price’ *arga-)'; п 51:95 (confused miscellany) байда pvaica 'twenty coverings’; II 77-24-27 (list sent to officials) ttasikau kādara íau drrai saca ära u pvaica dvi и baicakama dva и bina drraya и dvi boirükau u fa pyatsausaña и tvanakau hiyai ttarkana vaska pvaica haiste' he despatched coverings (pvaica) both for two Bbuiruk-officials and one woman attendant and the zarkan-official of the Tvanakas(?) (con- sisting of) one Tażik sword, valued at three faci-silk pieces, and two coverings and two Dickam-knives and three coats’ (not pZna, pürna 'arrow'). The syllables -aia, -eca ore like Aambeca 'summary' from older hasnbirsta-, hence possibly *pati-ursta- to vart- ‘to cover? (see s.v. pülsta-). But possibly rather to base pau- Чо cover’ (see s.v. pūstya-) to Zor.P. рб? (*pavasta-) ‘covering, skin’, hence #pavastya- > pveca (for -с-, note п 100°‹215 pacai ‘he ordered", older paste, parste). With ni- see also nyüd-, nyültte (*ni-vartatai).
4998:bad- ‘tum’, Z 24:503, 3 plur. trámu vara ššando dukhána yseru badüri ‘о there on the ground they roll with woe, wretchedly'; Z 20:57 Бій райе ‘the tongue rolls’. Base vart- “turn, roll’, derivatives bada- ‘time’, bada- ‘country’, Preverbs ni-, nyüd-, ham-, hambad-, hambálsta-, BS samgraha-. See also bais-, bih-, hambifh-, abeisa-, beisa-, То Av., O.Pers. vart-, Zor.P. vart-, тайап, causa- tive vartén-, N.Pers. gard-, gaštan (or base gart-), Sogd. Bud. wrin ‘сагі? (*vartana-), MLParth.T. wrt-, wrd-, шїї, пита, "mort, "most, 'mwštg, 'zwrt-, 'zwit-, "whr-, 'whr-, М.Регѕ.Т. wrd-, soft, “хиті, ‘swt, 'mwrd, Uahr=, 'whr-, Pahlavi Psalter wid-, Oss. D. aüiárdun, I. äüüärdyn, äüüärst 'make turn, roll’, nymät-uärdäg ‘rolling felt’, D. aüárdun, Y. ййтйоп ‘саті’, Pašto awarom, āwuštal ' turn, change’; arawsl ‘overturn’, Waxi wert- ' knead (clothes in washing)", ywrz 'pounding-stone' (*ewarta-), yzort= 'roll up’. IE Pok. 1156-8 uer-t-, Lat. uertü, O.Ind. odrtate, orttd-, Got. wairpan, frawardjan ‘destroy’, Lit. verciü, versti, O.Slav. vritéti, vratiti. For gart-, see ggad-, ggaltte.
57:ggadaa- ' throat' (?), then to gart- 'turn ', cf. NPers. gardan ' neck'.
```


## [2026-10-17T00:06:57.220Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 230 1787 1820 2186; do echo \"=== BQT:$p\"; timeout 300 python3 tools/ref_page.py BQT:$p --image 2>&1 | head -60; done",
 "timeout": 600000
}
```


### [2026-10-17T00:07:18.627Z] TOOL RESULT

```
=== BQT:230
no scan of BQT covers printed page 230 (see 'scans' in refs_online.json)
=== BQT:1787
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1787.png
REF: BQT:1787  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 584  OCR-lang: fas

2-۱۷۸۷ کردان
وبکس اول بممتی مدور ودوری باشد۱ - ودور | بالف کشیده وبسین بی نقطفزده . ستمگر وظالم
وحوالی واطراف را نیز کفته‌اند ۴ - وافادهجمع | راکوبند ۸ ؛ وبا شین قطه دار هم آمفماست .
هم میکند که کرد آمده و جمع شده باشد - گرد آفتاب - بنتم‌اول و کسرناك.
ویستی شهر و مدینه همست ؟ همجو داداب | رات راکوبندوآن خباری باشد که درپرتوآفتاب
کرد وسیاوش کرد که مراد از آن شپر داراب 2 یب
7 | کهازروزنه برجایی‌افتدظاهر کردد وبعریی‌سعراره
وشهر سیاوتی است - و بمعتی خرگاه نیز بنطن | خواشد .
آمده است ۴ - اول وفتح نانی, مخفف
کیرد * باعغد ویکسی اول وج ای گر دا گرد - بنتحاول بروزن‌تنهاکرد.
َ ۹۵ ۹8 و بمعنی پی‌دریی وهمیشه‌د رگردش‌باشد ‎٩‏ سوپکس
گر - بفتح اول بروزن قرداءمخفف اول وکاف فارسی؛ اطراف وجواب را کوبند*۱.
کردان است ۷ - و بادیر را نیز کوبند و آن
گرد آلوده » معروف‌است که‌هرچیز
چوبی باشد مخروط ی که طفلان رسمانی بر آن | . تاه ام
غبار آلود باشد - وکنایه از شخصی که اسباب
بیجند. و از دست رها کنند تا در زمن گردان ۴ َ ۲
پیج ۳ واموال دنیوی را حامل است .
شود۷ - وبکر اول بمعنی حجت باشد . َ سا
گرداباد - یک اولوبای ابجدبالف گرد آلوده سازد - پنی‌اسباب
کشیده وبدال زده . نام شهر مداین است وآبرا واموال دلیوی دهد بکسی .
طهمورت دیوبند که از جملةٌ پیغدادیان است بنا گردان!۱۱- بر وزن فرزان . نوعی از
کرده وجمشید باتمام رسالید . کباب است. وآن‌چنان باشد که کوشت مرغ با
گرداس جنم اول وسکون انی‌ودال | کوشت کوسفند در آب بجوشانند و بعد از آن
۹ - پهلوی 8)1(۳6 . ر4: هوبشمان - اسشق ۰۹*۱ وئیزپهلوی 81۳1 (مدور)ءارمنی‌ع
1 (کردء نان) . از 81718 0 «تیی رکه ص ۷۹ «اسشق ۰۹*۱
تبعات ج ۱ص ۰.۲۸۳ ۴ - پارسی باستان - 6۲18 - ۰ پهپلوی 18۲1 - (قی :
1 ) . رك : اسشق - هوبعمان **۹؛ استی ۰80720 80۳861 2 4 . ۱۲۱۱
فاعلی وصفت مشبپه) . ۷ - رك : کردنا. «کردا گردان باشد . عجدی (مروزی) گفت :
کی کز خدمتت دوری کند هیچ برو دشمن شودکردون گردا . *
: لغخت فری ص ۰.6۱۷۲
۸ - خدایا بی شبان بگذاشتی این بی زبانالرا
هگر توهم از ابشان باز داری شرکرداسان ۰
تزاری قهستانی «فرهنکه نظام» .
۹ - از: گرد (کردیدن) +۱ (واسطه) ۳+ کرد (گردیدن) ۰ قی : دمادم» سراسس ۰
*- از: کرد (بکراول) ۱ (واسطه) + کرد (اسا) .
۱- از :کرد (کردیدن) + ان (یسوند فاعلی) » یعنی کردنده : کردو ن کردان .
چنین گفت خرو که‌کردان سپهر کهی خشم بار آورد گاه مهر .
فردوسی طوسی « امثال وحکم دهشد! ی ۰۴۱۲۸۹

=== BQT:1820
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1820.png
REF: BQT:1820  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 617  OCR-lang: fas

گشت ب رکشت ۱۸
گشت برگشت » بنتم اول وبای ۱ نیز گوبند .
ابجد » بهمنی پیج برپیج باشد - و نام رستنیی گشسپ - بنم اول وفتح ثانی وسکون
بود بر هم پیچیده ۱ ومانند ریمان بهم تافته سن بی‌نقطه وبای ابجد . همان کشتاسب اس ت که
واز پنج عدد بیشتر نمی‌باشد و قاطم‌شهوت‌است. | پدر اسفندیار روبین تن باشد۴ - و بمعتی‌جهنده
اگرطفلی در کهواره کربه بمیارکند در زیر او | و خیزکننده نیز آمده است 9 - و بفتح اول
قدری ازآن بگذارند آرام گیرد و بخواب رودء | تفیر اشراق باشد ‎)٩(‏ چه گشپی اشراقی
و بعربی عشقه کوبند . راگوبند ‎٩‏ - و بمعنی پرست هم‌هست که مشق
گشتسب ؟ - ینم اولوفح‌نالك‌وسکون | از پرستیدن است چه ایزدکشب خدا پرست را
سین بی‌نقطه و بای ابجد ٍ مخفف کفتاسب است | کوبند ۷
که پادشاهی بوده معروف و مشپور . گشف ۸ - بفح اول وسکون ثای‌وفاء
گشتات - بروزن‌چنمك.سر کین گردانرا | بمعنی کزف باشد و آن صهغی است سیاه که بر
گوبند و بعربی جمل خوانند .98 درزهای کشتی‌مالند - وسیم سوخته‌وسوادز رگری
گشته ؟ » بنتح اول و ثالك , بمعنی راهم میگوبند .
گردیده وممکوی باشد - وکاج ولوج واحولرا گلشن * - بفتح اول و نانی و سکون
۱ يجك «رشیدی». از -مخفف« گشتاسب» (و.م.)
۴ آسم مفمول از «گشتن ن ار * کناسب(هم.) گناب («.م.)
8 - مخفف «کشنب » رك : آذ رکشب ؛ پهلوی ۷۱۶18290 « اوتوالا ۸۶ ب » .
- از برساخته‌های فرقهٌ آذرکیوان . رك : فرهنگه دساتیر ص ۲۹4 ۰
۷ - باین معنی بت » بلکه همان ممنی اصلی « اسب کشن نر » است ؛ جمماً بمعنی
فرشتةٌ اسب‌تر. رك : ایزد »آذرکشب . ۸ #کرزن < کرف . ‎٩‏ - دراوستا 2۳91188
و درپپلوی 805118 با ۷۵۶ بمعنی ثر و مردانه آمده » ودر فارسی نی زکشن بم‌اول‌وسکون
دوم بهمین معنی است - اماکشن وکشن (با حرکات مختلف) را بمعنی‌بسیار وانبوه نی ز گرفته‌اند.
درین بت بکر دوم آمده
سوی رود با کاروا ن کشن زهابی بدو اندرون سهمگن. ابوشکور بلخی.
درین بیت لیز حرف دوم متحرك است :
ازایوانکشتاسپ تا پیش کاخ درخت ی گشن بیخ وبیارشاخ . دفیقی‌طوسی (کشتاسپ تامه).
بقیدءٌ محققان اي ن کلمات بپردو معنی از يك ربشه میباشند واصلا بمعتی‌بر وفحل و مجازابممنی
بسیار ۰ آلبوه و فراوان استعمال شده . این بیت آبوشکور بلخی مویدآاست که بمعنی دوم هم در
اسل بسکون دوم بوده وجضرورت شعر متحرك آورده‌اند :
سپاه اندك ورای او داش فزون به از لشکرکشن بی‌رهنمون.
رك : مزدیسنا بقلم نگارنده ص ۳۳ بر کزیدء شمر بقلم نگارنده چاص ۲۷ ح ۰
۰ * تن - بفتح اول و سوم ** کردیدن » پهلوی ۷2511120 ؛ اوستا ۷8۳91 «بارتولمه
۵۸ هندی باستان ۷8۳1216 «نیب رکه ص ۲۳۹ > ورك : اسشق ۸۸۹؛ گردیدن,چرخیدن,
دور زدن - با زگردیدن - تغیی رکردن » تبدیل شدن - بازآمدن - شدن: ۶ مقرب حضرتسلطان
و مثارالیه و معتمد علیه کعت > «کلتان ص ۰۳۷ .

=== BQT:2186
(no exact page map; using offset -1917 -> pdf page 269; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2186.png
REF: BQT:2186  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 269  OCR-lang: fas

نوراهان -۱۸۹-
ظرفی باشد از برنج که آن را مانند دبةٌ روغن | وزن و برابر را نی زکوبند ‎٩‏ - و به‌منی‌اندوخته
سازید ‎٩‏ . وجمع آهده باشد ۷ - وجنگه و ناورد وخصومت

نوراهان ۲ بفتح‌اول بروزن‌همر اهان, را نز کفته‌اند ۸ - و بمعتی پسندیده و در خور
چبز بر گوبند که کی ازجایی برسم تحفه‌وهدایا ولایق ویسند کرده شده هم‌آهده ات٩‏ - ونورد
و پیشکش وارمغان بیاورد۴ - ومژدکانی و خبر [ پیراهن را نیز کوبند (۳) یعنی دامن پیراهن که
خوش را نز گوبند (۱). آنرا واشکنند و بدوزند *۱- و فاعل نور دیدن
ور یمین - یکی رای قرمت وه [ ند ۱ که پیچنده ات جر ی 3
بای فارسی» آشاره بحضرت رسول ملوات‌الط عله باین معنی‌هم‌هست یعتی بنورد و هیچ ۴ وم
وآله باشد . ۰ اول و سکون ثانی مجپول وثالث ورابع »نام‌اصلی
نورد ۴ بفتح اول وثانی وسکون‌اك شهر کازرون است ۱۳۴.
و دال ایجد » بمعنی پیج و تاب و پیچی(۷) که نو ردان « بنتح اول بر وزن قلمزن »
درچیزی افتد ‎٩‏ - ونام افزاری است‌جولاهگایر۱ | مخفف نوردیدن است که بمعنی پیچیدن و طتی
وآن چوبی باشد مدور وطولانی بعنی استوانی که | کردن باشد ۱۴- و نورد را نیز گفته اند و آن
هر قدرکه از پارچه که بافته شود برآن چوب چوبی باشد که آنچه از جامه بافته میشود برآن
پیچند ‏ - و شبه ومانند وهم فد وهم‌پهنا و هم | دیچند ۱8.
(۱) چش : هم گفته‌اند . () چش : ییجشی . (۳) چك » چش : کفته‌اند .
۱ - رك : جهانگیری . ۲ - از : نو (تازه) + را + ان (نسیت) * نورهان ‏
نورهانی ۳ نورهی « رشیدی >.
۳ - صبح آمده زرین سلب » نوروز نوراهان طلب
زهره شکاف افتاده شب . از زهره صفر| ربخته.
« خاقانی شروان ۸۷
۴ برد (رك : نردبان ) ورك : نوردیدن . نی شروانی ص
9 - هرنورد ی که ز طومار غمم با زکنی حرفها بینی آغشته بخون جگرم .
سعدی شیرازی « رشیدی ».
‎٩‏ - باین معنی هم نورد یعنی برابر وشبیه است:
با رعنا زناکو شیرمرد است با مرداکه با زن هم‌نورداست.»
« رشیدی » ۸« فرهنگه نظام لک
۷۲ -دد انبارآ کنده خوردی نماند همان در خزبنه نوردی نماند .
« رشیدی ؟ .
۸ «ناورد (ه.م.) ‎٩‏ - « نورد » درخورنده باشد کالی (مروزی ) گوید 7
نورد بودم تا ورد من مورد بود برای ورد مرا ترك من همی پرورد -
کنون کران‌شدموسردونانوردشدم ‏ ازآن‌سبب که بچیزی(,خیری.دهشدا) همی پپوشم‌ورد.»
« لفت فری ص ‎۸٩‏ ۰۴
*- همان معنی اول است. ۹۱ اسم فاعل مرخم . رك : نوردیدن .
۴ رك : توردیدن . ۴- با اول مضموم و واو مجهول و. رای موقوف, نام شهر
کازرون کهنه است . «جپانگیری» ورك : رشیدی . ۱۴ * نوردیدن (ه.م.) 9 * بورد(ه.م.)
( برهای قاطع ۲۷۹ )
```


## [2026-10-17T00:07:25.727Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:2186 --pdf-page 266 --image 2>&1 | head -50",
 "timeout": 400000
}
```


### [2026-10-17T00:07:26.236Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2186.png
REF: BQT:2186  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 269  OCR-lang: fas

نوراهان -۱۸۹-
ظرفی باشد از برنج که آن را مانند دبةٌ روغن | وزن و برابر را نی زکوبند ‎٩‏ - و به‌منی‌اندوخته
سازید ‎٩‏ . وجمع آهده باشد ۷ - وجنگه و ناورد وخصومت

نوراهان ۲ بفتح‌اول بروزن‌همر اهان, را نز کفته‌اند ۸ - و بمعتی پسندیده و در خور
چبز بر گوبند که کی ازجایی برسم تحفه‌وهدایا ولایق ویسند کرده شده هم‌آهده ات٩‏ - ونورد
و پیشکش وارمغان بیاورد۴ - ومژدکانی و خبر [ پیراهن را نیز کوبند (۳) یعنی دامن پیراهن که
خوش را نز گوبند (۱). آنرا واشکنند و بدوزند *۱- و فاعل نور دیدن
ور یمین - یکی رای قرمت وه [ ند ۱ که پیچنده ات جر ی 3
بای فارسی» آشاره بحضرت رسول ملوات‌الط عله باین معنی‌هم‌هست یعتی بنورد و هیچ ۴ وم
وآله باشد . ۰ اول و سکون ثانی مجپول وثالث ورابع »نام‌اصلی
نورد ۴ بفتح اول وثانی وسکون‌اك شهر کازرون است ۱۳۴.
و دال ایجد » بمعنی پیج و تاب و پیچی(۷) که نو ردان « بنتح اول بر وزن قلمزن »
درچیزی افتد ‎٩‏ - ونام افزاری است‌جولاهگایر۱ | مخفف نوردیدن است که بمعنی پیچیدن و طتی
وآن چوبی باشد مدور وطولانی بعنی استوانی که | کردن باشد ۱۴- و نورد را نیز گفته اند و آن
هر قدرکه از پارچه که بافته شود برآن چوب چوبی باشد که آنچه از جامه بافته میشود برآن
پیچند ‏ - و شبه ومانند وهم فد وهم‌پهنا و هم | دیچند ۱8.
(۱) چش : هم گفته‌اند . () چش : ییجشی . (۳) چك » چش : کفته‌اند .
۱ - رك : جهانگیری . ۲ - از : نو (تازه) + را + ان (نسیت) * نورهان ‏
نورهانی ۳ نورهی « رشیدی >.
۳ - صبح آمده زرین سلب » نوروز نوراهان طلب
زهره شکاف افتاده شب . از زهره صفر| ربخته.
« خاقانی شروان ۸۷
۴ برد (رك : نردبان ) ورك : نوردیدن . نی شروانی ص
9 - هرنورد ی که ز طومار غمم با زکنی حرفها بینی آغشته بخون جگرم .
سعدی شیرازی « رشیدی ».
‎٩‏ - باین معنی هم نورد یعنی برابر وشبیه است:
با رعنا زناکو شیرمرد است با مرداکه با زن هم‌نورداست.»
« رشیدی » ۸« فرهنگه نظام لک
۷۲ -دد انبارآ کنده خوردی نماند همان در خزبنه نوردی نماند .
« رشیدی ؟ .
۸ «ناورد (ه.م.) ‎٩‏ - « نورد » درخورنده باشد کالی (مروزی ) گوید 7
نورد بودم تا ورد من مورد بود برای ورد مرا ترك من همی پرورد -
کنون کران‌شدموسردونانوردشدم ‏ ازآن‌سبب که بچیزی(,خیری.دهشدا) همی پپوشم‌ورد.»
« لفت فری ص ‎۸٩‏ ۰۴
*- همان معنی اول است. ۹۱ اسم فاعل مرخم . رك : نوردیدن .
۴ رك : توردیدن . ۴- با اول مضموم و واو مجهول و. رای موقوف, نام شهر
کازرون کهنه است . «جپانگیری» ورك : رشیدی . ۱۴ * نوردیدن (ه.م.) 9 * بورد(ه.م.)
( برهای قاطع ۲۷۹ )
```


## [2026-10-17T00:07:31.667Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=440 && NR<=452 && /باور/ {print \"LEAF\",NR-1; print}' BQT_v1_pages.txt | grep -n -E \"LEAF|باور|wābar|vāvar|اوستا|پهلوی\" | head -30"
}
```


### [2026-10-17T00:07:32.019Z] TOOL RESULT

```
1:LEAF 450
2:ِ باور ۱ عم بر وزن خاور » بمعنی قبول
5:باوره ۲ بفتح واو و سکون زا و دال
19:هم حست که آرا پهلوی و رامندی خوانند ..
45:دوم در بهاوی ۷۵۳ و دراوستا ۷2:۵ از مصدر ۷26 اوستایی و پارسی باستان بمعنی بازشناختن
46:واعتقادداشتن وباور کردن . اصطلاحا «ور» درابران باستان عبارت بوده از آزمایشهای کونا کونی که
51:ت درسانسکر بت لا( ۵2, دراوستالا 082 وب 252( ندیم عراژدست اقب
55:۷ در پپلوی 202254 «منای ۲۹۹ :  .»۲‏ ۸ - درپهلوی 20225021 «منای۲:۲۹*.
56:د بایستن - در پهلوی 202228420 «منای ۲۹ : ۲» *«اونوالا۳۲۴» و 0هال(22د.
```


## [2026-10-17T00:07:36.642Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==451' BQT_v1_pages.txt | sed -n 1,8p; awk 'BEGIN{RS=\"\\f\"} NR==451' BQT_v1_pages.txt | sed -n 40,52p"
}
```


### [2026-10-17T00:07:37.041Z] TOOL RESULT

```
ِ باور ۱ عم بر وزن خاور » بمعنی قبول
و دیق سخن باشد - و بمعثی اسئواد و راست
- واستوار داشتن هم‌بنظن آمده است .
باوره ۲ بفتح واو و سکون زا و دال
کاورزعینی ساوردین کودرز بافطاع مقرر فرهء‌وده
بود , ار اين شهر را در آن زمين بنا نمود ونام
خود کرد .
باوددی - ی پامردی . حنسوب
الیه باشد - وبمعنی چنانکه می‌بابد ومی‌شایدهم
ممول است 4۴
پایست4 * - بروزن‌ایسته. بمعنی‌بایست
: ۲ ) م رکب ازدو جزو: جزو
دوم در بهاوی ۷۵۳ و دراوستا ۷2:۵ از مصدر ۷26 اوستایی و پارسی باستان بمعنی بازشناختن
واعتقادداشتن وباور کردن . اصطلاحا «ور» درابران باستان عبارت بوده از آزمایشهای کونا کونی که
مدعی ومدعی‌علبه بدان‌وسایل میباست‌حقانیت خودرا اثات کنند مشلامتهم‌حیبایست چندی‌دست‌خوورا
درآعشی تگیدارد» ا گراسی‌نمیدید بگناه‌مسوب مشد؛بامدعی ومدعی‌علیه هردومبایست‌درآبی
فرو رونده نفس هريك زود تر تنگه ت_ و سر از آب بیرون میکرد محکوممیگشت « مزدسنا
ی ۷ سعد». ۴اه ایسورد. _ باول» تهریاست بزر گه طبرستان ۷ معجم‌البلدان».
ت درسانسکر بت لا( ۵2, دراوستالا 082 وب 252( ندیم عراژدست اقب
مکی‌از بادشاهان‌هندبوده «الجماهر سرء‌نیس۲۵ این اخت‌رابه «ماهو> تصحیف کرده‌اند. ركك:بارولمه
4 ممقالة #دراز دست» بقلم نگار نده درمجلهٌ روابط فرهشگی‌ابران وعند ج4شمارء۲. ورك؛ بلزو..
```


## [2026-10-17T00:07:45.087Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f(){ python3 tools/fetch_source.py \"$1\" --note \"page 544, $2\"; }\na=$(f 'https://vajehyab.com/moein/ور' 'Mo in s.v. var ordeal (MON:4995)'); b=$(f 'https://vajehyab.com/moein/گرده' 'Mo in s.v. gorde kidney (MON:3255)'); c=$(f 'https://vajehyab.com/moein/وردنه' 'Mo in s.v. vardane'); d=$(f 'https://vajehyab.com/moein/نوردیدن' 'Mo in s.v. navardidan'); for x in $a $b $c $d; do echo \"== $x\"; head -4 $x; grep -n -E \"ور|گرده|وردنه|نورد\" $x | grep -E \"\\[|پهلو|اوستا|آزمایش|کلیه\" | head -8 | cut -c1-400; done"
}
```


### [2026-10-17T00:07:46.932Z] TOOL RESULT

```
== /home/sfmqrb/git/rishe-private/data/verification/sources/web/0b9000b88b7576b9.txt
URL: https://vajehyab.com/moein/ور
FETCHED: 2026-10-17T00:07:45Z
STATUS: 200
TITLE: معنی ور | فرهنگ انتشارات معین | واژه یاب
== /home/sfmqrb/git/rishe-private/data/verification/sources/web/7923574a849b3dc3.txt
URL: https://vajehyab.com/moein/گرده
FETCHED: 2026-10-17T00:07:46Z
STATUS: 200
TITLE: معنی گرده | فرهنگ انتشارات معین | واژه یاب
17: (گِ دِ) [ په . ] (ص مر.) 1 - هرچیز گرد و مدور مانند: نان . 2 - نوعی برنج .
== /home/sfmqrb/git/rishe-private/data/verification/sources/web/3760ac4d548592ae.txt
URL: https://vajehyab.com/moein/وردنه
FETCHED: 2026-10-17T00:07:46Z
STATUS: 200
TITLE: معنی وردنه | فرهنگ انتشارات معین | واژه یاب
== /home/sfmqrb/git/rishe-private/data/verification/sources/web/f30b3c1defeae766.txt
URL: https://vajehyab.com/moein/نوردیدن
FETCHED: 2026-10-17T00:07:46Z
STATUS: 200
TITLE: معنی نوردیدن | فرهنگ انتشارات معین | واژه یاب
```


## [2026-10-17T00:07:54.096Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for x in 0b9000b88b7576b9 7923574a849b3dc3 3760ac4d548592ae f30b3c1defeae766; do echo \"== $x\"; sed -n 8,40p $x.txt | grep -v \"^\\s*$\" | cut -c1-300 | head -14; done"
}
```


### [2026-10-17T00:07:54.609Z] TOOL RESULT

```
== 0b9000b88b7576b9
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 ور
 فرهنگ انتشارات معین
 ( ~.) [ په . ] (اِ.) 1 - بغل ، پهلو. 2 - سینه . 3 - کمر.
 ور در فرهنگ‌های دیگر
 معنی ور در لغت‌نامه دهخدا 
 معنی ور در فرهنگ فارسی عمید / قربان‌زاده 
 معنی ور در دیکشنری فارسی به انگلیسی 
 معنی ور در گویش مازنی 
 معنی ور در فرهنگ مترادف و متضاد 
 معنی ور در واژه‌نامه آزاد 
 معانی دیگر ور
== 7923574a849b3dc3
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 گرده
 فرهنگ انتشارات معین
 (گِ دِ) [ په . ] (ص مر.) 1 - هرچیز گرد و مدور مانند: نان . 2 - نوعی برنج .
 گرده در فرهنگ‌های دیگر
 معنی گرده در لغت‌نامه دهخدا 
 معنی گرده در فرهنگ فارسی عمید / قربان‌زاده 
 معنی گرده در دیکشنری فارسی به عربی 
 معنی گرده در دیکشنری فارسی به انگلیسی 
 معنی گرده در گویش مازنی 
 معنی گرده در فرهنگ مترادف و متضاد 
 معانی دیگر گرده
== 3760ac4d548592ae
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 وردنه
 فرهنگ انتشارات معین
 (وَ دَ نِ) (اِ.) نورد؛ چوب استوانه شکلی که خمیر را با آن پهن می کنند.
 وردنه در فرهنگ‌های دیگر
 معنی وردنه در لغت‌نامه دهخدا 
 معنی وردنه در فرهنگ فارسی عمید / قربان‌زاده 
 معنی وردنه در دیکشنری فارسی به انگلیسی 
 معنی وردنه در گویش تهرانی 
 واژه‌های مشابه
 ورنه 
 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
== f30b3c1defeae766
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 نوردیدن
 فرهنگ انتشارات معین
 (نَ وَ دَ) (مص م .) 1 - پیچیدن ، تا کردن . 2 - پیمودن .
 نوردیدن در فرهنگ‌های دیگر
 معنی نوردیدن در لغت‌نامه دهخدا 
 معنی نوردیدن در فرهنگ فارسی عمید / قربان‌زاده 
 معنی نوردیدن در دیکشنری فارسی به انگلیسی 
 واژه‌های مشابه
 نوردیده 
 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدید
```


## [2026-10-17T00:07:59.060Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"آزمایش.{0,40}(آتش|گناه)|سوگند.{0,20}آتش\" MON_part2.txt | head -5; grep -n -E \"^گرده|کلیه\" MON_part2.txt | grep -E \"گرده\" | head -5; grep -n -E \"^باور\" MON_part1.txt | head -3"
}
```


### [2026-10-17T00:07:59.666Z] TOOL RESULT

```
31259:گرده: (ه-) ۲2ج (امر .) زغال سوده‌ای که در 
31277:گرده 
31289:گرده: (0-)0۳02ع [قس. کلبه ] (ا.) کلیه» قلو ه. 
31297:گرده‌بالش: ۲0-0226 (امر.) متکای گر د؛ 
21088:باور: ۲ (.) قول سخن» بذبرش قول 
31924:باور» کمک حامی؛ معین » معاصد» ملاذ» 
41098:باور. (منط.) حکم کردن بر تصوری که در
```


## [2026-10-17T00:08:03.822Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; for w in باور گردیدن گردن گرده نوردیدن; do echo \"== $w\"; grep -n -E \"^\\s*$w\\b|$w\" ARY_pages.txt | head -3; done; grep -n -E \"WER|BAVAR|GARDAN|GORDE\" ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:08:04.221Z] TOOL RESULT

```
== باور
85:باور می‌کردند که آریایی‌های راستین مردمی بلند قامت با چشمان آبی ر موی طلایی بودند که از نظر
532:را بوجود آورد. طسبق این باور مردود کلیه‌ی زبانهای دنیا متعلق به یکی از این سه .
3159:۰ باور
== گردیدن
763:اسپانیایی و پرتغالی و رومانی و غیره گردیدند. کوچگران زبان‌های رومانس را به امریکای جنوبی و
13018:گشنن, گردیدن, گشت / ۴۳۹
13037:چم این واژه در آلمانی: شدن؛ گردیدن. ۱
== گردن
604:متون آنها معرفی می‌گردند: :
6446:جماین واژه در زبان لاتین کیت وکا ر گردن,
11999:چم این واژه در زبان هلندی: تنرمند» گردن کلفت.
== گرده
258:هزارهی گذشته (به استتنای هجوم و ماندگری قبایل ترک و مجار و فنلاندی) تغییر زیادی نگرده است
== نوردیدن
1680:WERIEN, WESTER VANHAN@M, WASTR@M
1681:WERIAN  :(OLD ENGLISH) gS godt WASTAR, (PAHLAVI) 5 34,
3156:BOBR (POLISH) gly) BAVARAK
4229:POWER ENGLISH) goSSi PADIXSHAYA-, PATI-
4243:SKEAT: (POWER) 469 PUTERE, PUTERNIC
4610:‘SPERWER DUTCH) sola PARISTOG, PARISTOK.
5925:(CAN) 106, (POWER) 128, (ABLE) 101 OLD ENGLISH) oS pf
6570:FIUWER, FIOR CHATHWARO, CHATHRO-
6573:FEOWER | :(OLD ENGLISH) aS gJ&il CHAR (KURDISH) 52,5
6645:ave ieGoby FEUWERTICH ©
```


## [2026-10-17T00:08:07.980Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 13010,13040p ARY_pages.txt; sed -n 3150,3170p ARY_pages.txt; awk 'BEGIN{RS=\"\\f\"}{n+=gsub(/\\n/,\"\\n\"); if(n>=13018){print \"pdfpage\",NR; exit}}' ARY_pages.txt"
}
```


### [2026-10-17T00:08:08.298Z] TOOL RESULT

```
: سرئدی (88015[7): 87۸ 7 برهان قاطع : ۸۸
ُ نروژی (078017/+ 11 فرهنگ معین + ۲۳۲۲
أ هلندی (0177۴[7): ایا لغت‌نامه دهخدا: 1۹۳۵
یادداشت:
۱ واژه‌های انگلیسی و فرانسه (و غیره) ۳۸101۸۴ و 2۸/۱3010106 نیز از همین واجربشه مشتق شده‌اند.
ا
۱ را ‌
[pdf page 438]
گشنن, گردیدن, گشت / ۴۳۹
اوستایی (4557/2): ۷۸ لگ ای نا :
پهلوی (7/مائله۳): اسلاوی کهن (51416 670863 00): ا
,6۸0۸0110۸ ,0۸30120۸ ۱ 71 ۲۸717 1
۷۲۸817۲۸۵ لهستانی ([5لا0: 00 :
کردی (ل610.015): لا دادن روسي (/(5514): 077
افغانی (پشس) (/(4۳0۸): ,آظ۸۷/28117 ینرانی ((فالهتا3 7 آر): :
تخاری 4 (۸4 708277۸۸): ۷۷7 ۷۳61311 ,[۷۳387 ,۷۸371 ۰
سانسکر یت (54(/5777): لدرنی (لتی) (7ل77۵ل): ۷7
۰ ۷۸ ,۷۸۳۸75
لاتین (4710): ۰ ۷8۳۸7582 ,۷8870 پسگشت‌ها 5
رومانی (0۷لالاتام: 171 7 20/050۸
گوتبکه (00777/0): ی ۹۱ 2 (101-3188) :ما05
آلمانی کهن (05721۸(1 07[ 012): 7 (080 :۸/25
دای ادن 67 0 :
آلمانی (0870/۸): رانرای دبا برهان قاطع : ۱۷۹۲
انگلیسی کهن (للقلا8۸۷0ظ صا0):
۱ بادداشت:
چم این واژه در تخاری ۸ : افکندن» گرداندن. ۱
چم این واژه در آلمانی: شدن؛ گردیدن. ۱
۱ ۰ :
ِ ِ
هار ا
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
pdfpage 438
```


## [2026-10-17T00:08:15.522Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -E \"\\bBAVAR|BAWAR|WABAR|WAWAR\" ARY_latin_index_pages.txt | head; grep -n -E \"WILL|VOLJA|WILJAN|VELLE\" ARY_latin_index_pages.txt | head -5"
}
```


### [2026-10-17T00:08:15.995Z] TOOL RESULT

```
3107:OLD SAXON) pS p-S WABAR, VAVAR, VAR
3108:WILLIO, WILLIAN BAWAR HAFGHANI) (p-4) gi
3156:BOBR (POLISH) gly) BAVARAK
290:€53,) 9 BEE) 14 45538 9 (OAK) «gin 5 (WILLOW) gp 5 (SALMON) al3T gal
496:eit ps i yo ghtbaly Lary (GIR WILLIAM JONES, 1746-94) 39x ls + eal
3104:WILJA, WILJAN (GOTHIC) Sa VAR., VARATA, VAIRYA
3108:WILLIO, WILLIAN BAWAR HAFGHANI) (p-4) gi
3110:WILLA, WELLA VARASA, VARAYATI, VRTA, VRNATI
```


## [2026-10-17T00:08:20.384Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"verbum|wertō|wert-|urvata|vərəδka|vṛkk\" IEC.txt | head -8"
}
```


### [2026-10-17T00:08:20.711Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:08:27.045Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^u?w?erdh|verb|vert[oō]|vertere\" IEC.txt | head -8"
}
```


### [2026-10-17T00:08:27.474Z] TOOL RESULT

```
89:LESKIEN, A.: Handbuch der Altbulgarischen Sprache. 9. Auflage (unveründerter Nachdruck d. 8., verbess. u. erw. Auflage v. 1962) 1969, Winter, Heidelberg
140:adv. adverb
214:Sp. Spanish subj. subjunctive substr. substrate sup. supine superl. superlative Sw. Swedish Thrac. Thracian Tokh. Tokharian Ukr. Ukrainian Umb. Umbrian v. verb
223:abhmn-, abhnis ‘river, water’. WP I, 46 Alb. âmë, f. pl. -a 'riverbed'; Lat. amnis, gp: amnium, mf. 'river; Gallo-Lat. ambis; Gaul. abono-; W afon, pl. -ydd, f.; Br. aven, Cor. avon, id.; Olr. aba, gs: abann, aband & abhond; Ir abha, gs. & gp. abhann, npl. aibhne, f. id.
284:-ai, adverbial theme Oss. rástài (rightly; Arm. i veraj “on top’; Gk. parai, pálai; Lat. prae; OCS lëpë ‘fittingly’; Li. kadai, visai, skersai, etc.
324:-àio (1) intensive continuant extn. of verb
331:type; (2) durative-freq. of verb type; (3) de- nominative extn. of verb type (1) Gk. outáo, geláo, eráo, damáo, skirtáo; Lat. crepo, seco, tono, veto, domo, sono, frico, all with inf. in -are, pf. in -u1; OS fol- gon; OHG tholon, holon and halon, volgon beside -en in all forms; OCS prijajo (beside prijo, inf. prijati: Skt. prinami: Go. frijon, see below: priià-, vrüzajo, vrükajo, tüpajo; Li. plasnóju, inf.-óti, riaumóju, pléscioju; Latv. bokaju, at. bojaju; (2) sedare, ducare, placare; Go. miton (mitan), hvarbon (hvairban); OCS tékajo, -ati (eko, testi); OCz. vídaju, -ati (vizu, viděti); Li. pa-jaújoju, -oti(jauti) Latv. plūkāju, -āt (plükt); (3) Gk. timáo (timé), ereunáo; Lat. fumare; OHG zilon (:Go. tilon) (zil), faston (fasta), fülön (fül); OCS dymajo, -ati (Lat. fümare)(dymü), düzdajo (düZzdi), kosajo (kosü); Li. ráudoju, -oti (ráuda), vo- Dom (vðlas). See below: *siiā- (sia), skiia-, neuà-, dhuma-, etc.
334:-ăk, -åkis, an adverbial extension Arm. cf. er-aki “trebly'; Gk. is-ákis ‘equally’; OCS inače ‘otherwise’; Cz. jin-ak, id.; Latv. péc-ak ‘afterwards’, labaki, labāk; cf. also trij-acis «three, at cards’.
```


## [2026-10-17T00:08:33.827Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"‘word’|'word'|‘kidney|‘to turn’\" IEC.txt | head -10"
}
```


### [2026-10-17T00:08:34.139Z] TOOL RESULT

```
3751:etór (etrom, Str) “internal organ’. WP I, 117 (Arm. irank “body, trunk’ is ambig.); Gk. étor “heart”; étron ‘belly’; OHG adara ('vein'; pl. tintestines); MHG àder (as OHG, also = ‘sinew, nerve); OE ædre ‘veim’; pl. ‘kidneys’; ON cf. æðr, as. & ds æði ‘vein’. (OCS jadro “bosom? indicates a variant consonant, cf.
3909:gars- ‘shout, cry, resound, echo’. Cf. gouor-, gar-, garm-, gers- and see WP I, 537, 609 & 686 Arm. kar-a£, anc o-st. “shout, shouting’; Lat. garriō, ire; garrulus; Olr. gair ‘word’; W gair, Br. gér, id.; cf. Mir garim, gairim ‘cry’ (am- big. cf. garëið); MHG karren; Li. garsēju, eti beside gařsas “noise, echo, speech’; garsùs ‘shrill, loud. (For MHG kérren, OE ceorran & cierran ‘creak’, see gers-)
6084:ghodh- (?) “address, beg, imprecate'. (ambig. cf. ghed- and ghodh-). Cf. WP I, 673 Av. (ambig.) jaióyemi ‘implore, wish sb. sth; Umb. cf. hufie, ds "a god’; Ir. guidhim "be seech'; guidhe ‘prayer’; Li. Zadü, -éti "pro. mise’; Zadà, f. id.; Zádas “power of speech; speech, confession'; (*-à- in) Li. Zostu, inf. Zosti, pf. Zodau ‘pronounce, declare’; Zódis, m. ‘word’
6387:pl. igártà, id.; Gk. &par, gs épatos; Lat. jecur, gs jecoris & jecinoris; Umb. iepru (queried: "ver": Li. jéknos, fpl. beside jáknos, id.; Latv. aknas, pl. id. (Oss. has also a form wrg, Dig. urg ‘kidney’
9918:Indhuis, os, io (Indhis) ‘loin, waist’. Cf. londh-. WP II, 438 Cf. Lat. lumbus, m.; Ir. cf. luan, m. ‘loin, kidney’ beside léan, gs. léin, m. ((2) Join’. Vocalism for Lat. & Ir. uncertain); OE lynd, f. gelyndu, n. pl. ‘loins’; lyndu ‘small of the back! beside (Kentish) lendenu ‘loins’, cf. also OE lund-lage ‘kidney’; ON hrygg-iundir, fpi. ‘Joins’; OCS ledvije, n. id.; Srb. ledja, n. pl. ‘back’; R ljàdveja, f. ‘haunch’. The vocalism of G Lenden ‘loins’ is obscure. Finn. LW: lanne
10974:mníros (mntor-, mnstro-, montro-), cf. mnt- (1) Av. måðrð, m. ‘word’; Gk. dial. cf. mastrós ‘assessor’; LLat. cf. mentor ‘inventor; Li. mintrüs ‘thoughtful; gifted; Skt. cf. e- or o- gde: mantrah ‘reflection; worship; hymn’
11579:neguhros, ó(n) (reguhnos, õn) ‘kidney’. WP I, 134 Gk. nephrós, m. id.; Praen. nefrones, pl. id.; Lat. dial. cf. nebrundines, pl. id. (synth. cpd.?); beside Lat. renés, pl. (w. metath.); OHG nioro, wm. id. (& ‘testicle’); G Nieren, pl. id.; Sw. njure, wm. sg. id.
14523:renos, is “narrow, slim; waist, small of the back’. (Lat. ambig. cf. srén-) Lat. ren, gs: renis, m. ‘kidney’; Av. rano, m. (thigh. Ambig. cf. Ién-); Per. ràn, id.; (LW in) Arm. erank, gpl. eranac, ab. pl. eranawk ‘haunch, hip, groin, lap’; MHG ran, adj. ‘slim, thin’; G rahn, id. beside Rahne, f. ‘tapering beet, taproot’; Latv. rēns, adj. ‘sparse; porous; lukewarm’. (Isophones: Icel. rán, Sw. rån, n. ‘robbery’; råna ‘swell — of wood’)
17080:sren- ‘loin, kidney’. Cf. rénos, is Lat. rén, gs: rénis, m. ‘kidney’; Li. dial. srénos, usu. strenos, fpi. ‘loins, waist'. (NB. The initial str- is characteristic of Latv., where the wd. does not occur).
18155:Olr. son, m. ‘word’; (Lat. sonus, 1 “sound, noise, note, word' is fr. *suen-))
```


## [2026-10-17T00:08:41.537Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^u?r?dho|^u(e|o)rdh|^uert|^ue?rt|^urt\" IEC.txt | head; grep -n -E \"waurd|vertō|vertö\" IEC.txt | head -5"
}
```


### [2026-10-17T00:08:42.119Z] TOOL RESULT

```
2880:dhodhorio see dhadhlo, dhedher-
2881:dhom- (1) (dhm-, dhm-) (theme of a radical “blow, puff, swell. See dhum-). WP I, 851 Skt. dhámami, pp. dhmatah “blów?; Av. dam- ‘blow, breathe’; Per damam, "dan ‘blow’ beside dam ‘breath’, dame ‘bellows; asthma’; Oss. dimin, dumun ‘blow, smoke’; Hitt. dann- aras, -attas ‘empty’; Gk. cf. ásthma (fr. *n-Ks- . dhmn, cf. n-px. and eks); Lat. cf. fam-ex, mf. ‘tumour’ beside fam-faluca ‘pustule’; OHG cf. a-tum ‘breath’; Ger. Atem; OCS dümgo, doti ‘blow’; dümljo, dommt ‘inflate’; Cz. dma ‘throes’; roze-dma ‘emphysema’; Li. dumiü, dümti “blow, get cloudy
2882:dhom- (2) (dham-, dhóm-) (theme of a rad- ical “set, fixed’. See dhê- (2), etc.) Gk. thamüs fcompact', thamá, adv.; thámnos ‘thicket’; thaminós, adj. “close, frequent’; cf. also Hes. thaimós “family, household’; Lat. fam-ul, -ulus, -ilia; W daf, pl.-oedd “issue, output; MHG tam, gs. tammes; Du. dam ‘dam’; Go. faür-dammjan (‘dam up’. -mm- unexplained, cf. Li. domüs, j-domus “atten- tive; interesting; dome “attention? *-a- and Gk. thomós ‘pile’ *-o-)
2883:dhotos (r-gde of type dhéio- (2), q.v. Cf. dhetós “placed”, etc. Skt. cf. sam-dhitah beside dhitáh; Gk. cf. sún- thetos beside thetós
2884:dhou- (1), see dhau- “admire”
2885:dhou- (2), see dhou-
2955:dhob- ‘hollow’. Cf. dhoub- MHG cf. tuofzre “hole in wall; Li. duoburys ‘hollow’; duoba “hole in tree’; duobe ‘hollow, grave’; duobiu, ti ‘hollow out: Latv. dobjs ‘deep’; dobe ‘hollow’
2956:dhodh-, dhodhlo- ‘bemused, silly; simple- ton’ Gk. cf. totházo ‘mock’; Du. cf. doedel-dop *simpleton'; EME doodle, id.; Cz. dadati “to sleep’; Big. dada “elder sister’, dadilja “child's nurse’; Srb. dadilja, id.; Li. cf. duolas ‘horn- less’; duoklas ‘silly’
2957:dhoguheið ‘make burn, heat; keep burning’. Cf. dheguh-. WP I, 849 Lat. foveo; Alb. ndez ‘ignite’ (fr. *en-dho- Buh-); Olr. cf. addoaim ‘kindle’; Ir. dóghaim, tr. & intr. ‘burn’; OHG tagen, OE dagian ‘dawn’; Li. (Zemait&) dagéju, éti “get hot, flare up’; (IE *-ó- in alleged Cz. dahnéti ‘to glow")
2958:dhoguhlos, à ‘inflammable; fuel, wick, touchwood'. Cf. dheguh- Ir. cf. de-dól ‘twilight, daybreak’; Li. dáglas ‘pied, branded”; Latv. dagla (touchwood of birch'. Cf. variant (*dhoguhslos) in G (fr. LG?) Dassel-fliege ‘gadfly’; Li. dágslas “mark, brand’. (The vocalism of Lat. favilla ‘ember’ is obscure. LLat. fomen ‘poultice’? repre- sents a formula *dhoguhmn-)
```


## [2026-10-17T00:08:51.583Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^(WORD|VERB|IRONY)\\b\" SKT.txt SKT_dli_revised.txt | head; grep -n -A3 -E \"^IRONY\" SKT.txt | head -8; grep -n -A4 -E \"^WORD,\" SKT.txt | head -8"
}
```


### [2026-10-17T00:08:52.074Z] TOOL RESULT

```
SKT.txt:20687:VERB,
```


## [2026-10-17T00:08:55.017Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 20687,20700p SKT.txt; grep -n -E \"IRONY|Irony\" SKT.txt | head -3; grep -n -E \"^WORD|WORD, sb\" SKT.txt | head"
}
```


### [2026-10-17T00:08:55.366Z] TOOL RESULT

```
VERB,
ventail,  lower    half  of  the  moveable '     ooven&at.  s^reoncot .  (F.—L^
pait  of  a  helmet.  (F.  — L.)  }t\,'E.iiiffnfiiiU (With  prefix  a  =  F.  a  -  L.  a*/).  — K  tvw- taiHe,  'breathing-part  of  a  hetiuet ;'  Cot. —  F,  vcftter^  to  puff;  with  suffix  ailU  (  = L-  -acuIuni\.'-¥,  vftit^  wind  (above).
ventilate.  (L.)     From  pp.  of  L  umti- late,  to  blow,  winnow.     Ftoin  an  unused fldj   uentiitis  *,  due  to  uffttus,  wind. Ventral,  belonging  to  the  belly.    (L.) L.  yenfralist  adj.,  from  uenter,  the  belly.
Tontricle.  i;F.  —  L,)  F.  vcntriatlc, '  the  ventricle,  tlie  place  wherein  the  meat sent  (rom  the  slomack  is  digested;'  Cot ■-  L.  ueHincuiumt  ace.  of  uenfn'i-ufuj, stomach,  ventricle,  double  dimin.  of  iten/tr, belly.
ventriloquist.  (L.)  Coined  from  L. urn/ri/ot/U'ifS,  lit.  5[)eaktng  from  (or  in)  the belly.  —  L.  uentri-.  crude  form  of  uenUr <nbove)  ;  loqui^  to  speak.  See  iJoq.aft' oioua.
"Venture,  sb.  (F.-L.)  A  headless  form of  M.  E.  atunfun  {avaUure),  an  adventure, chance,  —  F.  avenlurc,  a  chance,  occorrcncc. ^l^at/ugn/ut-a,{cm,of  aJifen/urw  about  to happen.  — L.  a^,  to;  ucntunu,  fut.  pt.  of venire,  to  come.  Cognate  with  E.  Oome. (^GAM.)     Doublet,  aJventun.
advent,  approach.  (L.)  L.  aduentus, approach.  — L.  aduentus,  pp.  oi  adHeitirt^ to  approacli.  — L.  a*/,  to;  uenire,  to  come. adventure.  (K.-L.)  Formerly  spelt 'mattitun ;  the  F.  prefu  a-  was  need- W&ly  turned  into  the  L.  aJ- ;  tec  Venture (above).  Der.  advtnture^  verb  ;  pcrad' venturt,  \.  t.  by  chance,  where  the  prefix should  I  .ither  be  fntr  [Jf.  par,  I^  /rr).
avenue.  (P\  —  L.)  F.  avenutt  advenut, access;  hence  an  apptonch  lo  a  house  (e&p. one  shaded  by  tict-sl.  — F.  avenir,  to  come to.— L.  ad,  to;  uenire,  to  come.
contravene,  to  hinder.  (L.)  I.ow  I.. tonirauenire,  to  oppose ;  to  break  a  law. —  L.  contra,  against ;  uenire,  to  come.
convene,  to  as^iemble.  (F.  —  L.)  F. tonvenir,  to  assemble.  —  L.  ron'Uenirt,  to come  tOiiclh(?r.
oonvenlent,  suitable.  (F.  — L.)  From stem  of  X*.  canueniens,  suitable  ;  orig,  pres. pt.  oi  eon-uenirt,  to  come  together,  suit.
convent.    (L.)     L.  lonuentus,  an  as* setubly.  —  L.  eonuintus,  pp.  of  ion-uenin, tnvention.  (F.-L.)    F.  eonvention, compact;'  Cot.  —  L.  ace.  «wi«/«/it'«*«, tccting,  com\>akCl.  —  L-  eoMutnttts,  pp.  of rni/t,  to  come  logcthtr,  meet.
finv»<i'ft,    .lUo    iamfnant,     agr«
```


## [2026-10-17T00:09:01.515Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -o -E \"eiron.{0,300}\" 1cb6c7e296407f61.txt | head -2; grep -o -E \"Proto-Germanic \\*wurda.{0,200}\" e950c126daed8204.txt | head -1; grep -o -E \"verbum.{0,200}\" 8f7237ce80a240b9.txt | head -1; grep -o -E \"Etymology.{0,10}\" 798e2abbd9ab30ee.txt | head -2; grep -n -E \"urvāta|urwāta|wərəs|Avestan\" 798e2abbd9ab30ee.txt | head -5; grep -n -E \"Avestan|vərəδka|Persian\" 8e5cb39fa2dd5f56.txt | head -8"
}
```


### [2026-10-17T00:09:01.980Z] TOOL RESULT

```
199: Old Avestan: 𐬎𐬭𐬎𐬎𐬀𐬙𐬀 ( uruuata ) , 𐬎𐬭𐬎𐬎𐬁𐬙𐬀 ( uruuāta , “ rule, order, indication ” ) 
212: Middle Persian: [script needed] ( wrd- ) 
213: Persian: گرد ( gerd ) 
277: Requests for native script for Middle Persian terms
```


## [2026-10-17T00:09:05.650Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; head -5 1cb6c7e296407f61.txt; grep -i -o -E \".{0,200}dissembl.{0,200}\" 1cb6c7e296407f61.txt | head -2; head -5 e950c126daed8204.txt; grep -o -E \".{0,100}wurd.{0,200}\" e950c126daed8204.txt | head -1"
}
```


### [2026-10-17T00:09:11.334Z] TOOL RESULT

```
URL: https://www.etymonline.com/word/irony
FETCHED: 2026-10-17T00:05:10Z
STATUS: -1
TITLE: 

ugrep: error: error at position 87
0-\xbf][\x80-\xbf]*){0,200}
                           \___exceeds complexity limits


URL: https://www.etymonline.com/word/word
FETCHED: 2026-10-17T00:05:10Z
STATUS: -1
TITLE: 

ugrep: error: error at position 82
f][\x80-\xbf]*){0,200}
                      \___exceeds complexity limits
```


## [2026-10-17T00:09:29.486Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -E \"wr̥dʰh|werdʰ|verbum|wurdą|eírō|εἴρω|vratá|Proto-Iranian\" 798e2abbd9ab30ee.txt | head -12 | cut -c1-200; grep -n -E \"kidney|vṛkk|gurd|wartana|gardan|nawar\" 8e5cb39fa2dd5f56.txt | head | cut -c1-200"
}
```


### [2026-10-17T00:09:29.784Z] TOOL RESULT

```
167: ⇒ *werdʰom 
196: Sanskrit: व्रत ( vratá ) ( see there for further descendants )
198: Proto-Iranian: *wratám 
217: ^ De Vaan, Michiel ( 2008 ), “ verbum ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN 
223: ^ Lubotsky, Alexander ( 2011 ), “vratá-”, in The Indo-Aryan Inherited Lexicon (in progress) (Indo-European Etymological Dictionary Project), Leiden University, pages 597-8
```


## [2026-10-17T00:09:34.286Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 140,215p 798e2abbd9ab30ee.txt | grep -v \"^\\s*$\" | cut -c1-160 | head -50"
}
```


### [2026-10-17T00:09:34.685Z] TOOL RESULT

```
 *werh₁- ( perfective ) [ 1 ] 
 to speak , say 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *werh₁- (50 c, 0 e) 
 *werh₁-i-dʰ-e-ti [ 2 ] [ 3 ] [ 4 ] 
 > ? Proto-Anatolian: *wer(H)ideti ( or from *wer- ( “ to heed ” ) ) 
 Hittite: 𒌑𒂊𒊑𒋾𒄑𒍣 ( ú-e-ri-ti-iz-zi /⁠u̯eritit͡si⁠/ , “ fears, is frightened ” , 3sg.pres.act. ) 
 *wérh₁-t ~ *wr̥h₁-ént ( athematic root aorist ) [ 5 ] 
 Anatolian:
 Hittite: 𒌑𒂊𒊑𒀜 ( ú-e-ri-at ) , 𒌑𒂊𒊑𒀉 ( ú-e-ri-et , 3sg.pret.act. ) 
 Palaic: 𒌑𒂊𒅕𒋾 ( ú-e-er-ti , 3sg.pret.act. ) 
 ( perhaps ) Hellenic:
 Ancient Greek: ἐρρήθην ( errhḗthēn ) 
 *wér-dʰe-ti ( laryngeal deleted per the Lex Schmidt–Hackstein rule ) [ 6 ] 
 Proto-Hellenic: *wértʰō 
 Ancient Greek: ἔρθει ( érthei , “ utters ” , 3s.act.ind.pres. ) 
 ⇒ *werdʰom 
 *wér-ye-ti ( ye-present ) 
 *wer-yeh₂ 
 Proto-Hellenic: *wéřřā 
 Ancient Greek: εἴρη ( eírē ) 
 *wr̥h₁-tós 
 Proto-Hellenic: 
 Ancient Greek: ῥητός ( rhētós ) 
 Unsorted formations 
 Armenian:
 Old Armenian: յորջորջեմ ( yorǰorǰem ) 
 Old Armenian: ( possibly ) առաւիր ( aṙawir ) 
 Old Armenian: ( possibly ) վեռ ( veṙ ) 
 Balto-Slavic:
 Proto-Slavic: *vьrati ( “ to lie ” ) 
 Russian: врать ( vratʹ ) 
 Proto-Germanic: *wrōgijaną ( see there for further descendants )
 > ? Proto-Indo-Iranian: *wratám ( unrelated according to Lubotsky [ 7 ] ) 
 Proto-Indo-Aryan: *wratám 
 Sanskrit: व्रत ( vratá ) ( see there for further descendants )
 Proto-Iranian: *wratám 
 Old Avestan: 𐬎𐬭𐬎𐬎𐬀𐬙𐬀 ( uruuata ) , 𐬎𐬭𐬎𐬎𐬁𐬙𐬀 ( uruuāta , “ rule, order, indication ” ) 
 Root
 [ edit ] 
 *werh₁- 
 alternative reconstruction of *wreh₁- 
 References
 [ edit ] 
 ^ Rix, Helmut , editor ( 2001 ), “*u̯erh₁-”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr.
 ^ Oettinger, Norbert ( 2001 ), “Hethitisch -ima- oder: Wie ein Suffix affektiv werden kann”, in G. Wilhelm, editor, Akten des IV. Internationalen Kongresses fü
 ^ Kloekhorst, Alwin ( 2008 ), “u̯erite- zi / u̯erit-”, in Etymological Dictionary of the Hittite Inherited Lexicon (Leiden Indo-European Etymological Dictionar
```


## [2026-10-17T00:12:35.829Z] TOOL CALL #74: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-544.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nPOK1162={\"src\":\"POK\",\"where\":\"pp. 1162-1163, 6. u̯er- (POK_full.txt l.~92100-92153)\",\"stance\":\"supports\",\"note\":\"'Meaning: to talk, speak ... Avestan urvata- n. \\\"determination, command\\\" ... gr. εἴρω \\\"say\\\" ... εἴρων \\\"someone who dissembles\\\", εἰρωνεία ... Latin verbum \\\"word\\\" ... Gothic waurd, OHG wort'.\"}\nWLD283={\"src\":\"WLD\",\"where\":\"Bd. I p. 283 (WLD_Bd1_pages.txt leaf 292, l.26773-26792)\",\"stance\":\"supports\",\"note\":\"'5. u̯er- \\\"sagen, sprechen\\\" ... Gr. εἴρω \\\"sage\\\" ... εἴρων \\\"einer der etwas nur sagt, ohne es zu meinen\\\" ... av. urvata- n. \\\"Bestimmung, Gebot\\\"'.\"}\nAHD6={\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt l.1148, wer-6 'To speak': '1. Suffixed zero-grade form *wr-dho- in Germanic *wurdam in Old English word: WORD. 2. Suffixed form *wer-dho- in Latin verbum, word: VERB, VERVE; ADVERB, PROVERB. 3. Suffixed form *wer-yo- in Greek eirein, to say, speak: IRONY. [Pok. 6. wer- 1162.]'\"}\nPOK1156={\"src\":\"POK\",\"where\":\"pp. 1156-1158, uer-3 H. uer-t- (POK_full.txt l.91760-91825)\",\"stance\":\"supports\",\"note\":\"'to turn, wind ... Avestan varət- \\\"sich wenden\\\" ... vṛkkāu \\\"kidneys\\\" ... Avestan vərəδka- varətka- ds., compare Pahlavi gurtak, npers. gurda \\\"kidney\\\"'.\"}\nWLD274={\"src\":\"WLD\",\"where\":\"Bd. I pp. 274-275 s.v. uert- (WLD_Bd1_pages.txt leaf 283)\",\"stance\":\"supports\",\"note\":\"'uert- \\\"drehen, wenden\\\": ai. vartate ... av. varət \\\"sich wenden\\\" ... av. varədka-, ai. vṛkkā- \\\"Niere\\\"'.\"}\nCH_uart={\"src\":\"CHEUNG\",\"where\":\"pp. 423-425 s.v. *u̯art 'to turn' (CHEUNG.txt l.27441-27552)\",\"stance\":\"supports\",\"note\":\"'YAv. varət- \\\"to turn\\\" ... OP ? vart- (According to Gershevitch ... rather reads *vratiyaiy \\\"I swear\\\") ... NP gardun \\\"wheel; chariot\\\" ... (+ *ni-) NP nawardidan/naward- \\\"to fold, cease; to twist; to stroll\\\" ... PIE *u̯ert- Pok. 1156 ff.'\"}\nCH_gart={\"src\":\"CHEUNG\",\"where\":\"p. 110-111 s.v. *gart 'to turn' (CHEUNG.txt l.8055-8100)\",\"stance\":\"contradicts\",\"note\":\"'MMP grd-, BMP glt- /gard-/ \\\"to revolve, turn; to become\\\" ... NP gaštan/gard-, ... NP gardidan (< *u̯art- ?) ... The Ir. root with no exact IE correspondences seems to be an enlarged root of *gar \\\"to turn, wind\\\". It has probably been influenced by *u̯art.'\"}\nNYB_gart={\"src\":\"NYB\",\"where\":\"vol. II s.v. gartišn, girt (NYB_vol2_glossary.txt l.1642, 1665)\",\"stance\":\"contradicts\",\"note\":\"'gartišn turning ... NP gaštan or gardīdan gard-; etymologically not identical with vart- (v. vaštan) by which it is semasiologically influenced. OIr *gart- probably \\\"to twist, to wreathe\\\" ... Hence girt'; 'girt round ... From gart-'.\"}\nnodes0=[\n {\"id\":1,\"lang\":\"Avestan\",\"words\":\"ver 2; verâta, urvata, vrvata, varah, wrvâta; upa-var\",\"verdict\":\"disputed\",\n  \"derivation\":\"The node mixes two Avestan roots. urvata- / urvāta- (Gathic uruuata-, uruuāta- 'decree, commandment, rule'; 'vrvata', 'wrvâta', 'verâta' are Nourai's variant spellings of the same word) is the form Pokorny, Walde-Pokorny, Buck and Klein put under PIE *wer(h₁)- 'to speak', next to Skt. vratá- 'vow, command'. Wiktionary (after Lubotsky) notes that *wratám may be unrelated to *werh₁-, so this link is plausible, not certain. But 'ver 2' 'to decide, command' is Bartholomae's var- 2 'to choose; to convince; (med.) to believe'. With varah- 'ordeal' (Bartholomae: 'Probe, Prüfung, Ordal', literally 'Beglaubigung, Erhärtung' of one's innocence, from that verb) and upā-var 'in belief' it belongs to Proto-Iranian *u̯ar(H)- < PIE *u̯elH₁- 'to wish, choose' (Cheung 2007; Pokorny 1137, Nourai's 'Wel 1'), not to *wer- 'to speak'. Worst verdict: disputed.\",\n  \"derivation_fa\":\"در این گره دو ریشهٔ اوستایی با هم آمده‌اند. urvata- / urvāta- «فرمان، دستور» (گاهانی uruuata-) را پوکورنی، والده‌ـپوکورنی، باک و کلاین در کنار سنسکریت vratá- «پیمان، فرمان» زیر ریشهٔ هندواروپایی *wer- «گفتن» آورده‌اند، و این پیوند با احتیاط پذیرفتنی است. اما var- (ور ۲ بارتولمه) «برگزیدن، باوراندن، باور داشتن» و varah- «ور، آزمایش ایزدی» و upā-var «در باور» به ریشهٔ ایرانی *u̯ar(H)- و هندواروپایی *u̯elH₁- «خواستن، برگزیدن» بازمی‌گردند (چونگ؛ پوکورنی ۱۱۳۷)، نه به «گفتن». پس این بخش از ادعای نورایی را پژوهش امروزی رد می‌کند.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/werh₁-\",W+\"باور\"],\n  \"ref_check\":[\n   {\"ref\":\"POK:1162\",\"status\":\"partial\",\"note\":\"POK_full.txt l.~92100: 6. u̯er- 'to talk, speak': 'Avestan urvata- n. \\\"determination, command\\\"' — supports urvata only; Av. var- 'choose' and varah- are not listed here (Pokorny treats them under 2. u̯el- p. 1137).\"},\n   {\"ref\":\"KLN:1751\",\"status\":\"partial\",\"note\":\"KLN_1971.txt s.v. word: 'I.-E. *werdh- is an enlarged form of base *wer-, *were-, \\\"to speak\\\", whence ... OI. vratam, \\\"commandment, order\\\", Avestic urvata-, of s.m.' — urvata only.\"},\n   {\"ref\":\"SYN:1254\",\"status\":\"partial\",\"note\":\"SYN.txt l.31586 (18.22 'say'): 'IE *wer- seen elsewhere in derivs. as Lat. verbum, OE word ... Av. urvata- \\\"command\\\", Skt. vrata- \\\"command, vow\\\"' — urvata only.\"}],\n  \"consulted\":[\n   {\"src\":\"BRT\",\"where\":\"col. ~1365-1366 s.v. varah-; col. ~1541 s.v. urvāta- (BRT.txt l.22809-22811, 25677)\",\"stance\":\"partial\",\"note\":\"'varah- n. \\\"Probe, Prüfung, Ordal\\\" ... Eig. \\\"Beglaubigung, Erhärtung\\\" des Rechts, der Unschuld; zum V. var- ... mp. (Pü.) var \\\"Ordal\\\"'; 'urvāta- n. \\\"Bestimmung, Gebot\\\"' — varah- is tied to var- 'choose/believe', not to a verb 'speak'.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"pp. 420-421 s.v. *u̯ar(H)¹ (CHEUNG.txt l.27239-27330)\",\"stance\":\"contradicts\",\"note\":\"'*u̯ar(H)¹ \\\"to choose; convince; (med.) to believe\\\" — AVESTAN var- \\\"to choose; to convince\\\" ... OP v(a)r- ... MMP wrw- \\\"to believe\\\" ... NP bavar \\\"belief\\\" (< old intensive) ... PIE *u̯elH₁- \\\"to want, wish\\\" Pok. 1137 f.'\"},\n   WLD283,\n   {\"src\":\"KNT\",\"where\":\"p. 206b s.v. var- (via Cheung's citation 'Kent: 206b')\",\"stance\":\"silent\",\"note\":\"OP v(a)r- 'choose, convince' is in Kent, cited by Cheung; not grepped separately.\"}]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"var; bâvar\",\"verdict\":\"disputed\",\n  \"derivation\":\"NP var 'ordeal' < MP war (PHD 'war [wl] oath, ordeal'; Nyberg s.v. passāxt: 'the var, the ordeal') < Av. varah- 'ordeal'. NP bāvar 'belief' < MP wābar 'truth; belief' (PHD 'wābar [wʾbl | M wbr, N bāwar]'), Manichaean wbr. Cheung explains bāvar as an 'old intensive' of *u̯ar(H)- 'to choose; (med.) to believe'; Wiktionary has *upa- + var-. Both words come from Iranian *u̯ar(H)- < PIE *u̯elH₁- 'to wish, choose' (Lat. volō, Goth. wiljan), not from *wer- 'to speak'. Nourai's own NOTE ('see root Wel 1 for another possible root of bâvar') points to the side modern scholarship (Cheung, Aryanpur) takes, and the same holds for var. Wiktionary still lists both PIE roots as possible.\",\n  \"derivation_fa\":\"«وَر» (آزمایش ایزدی مانند گذشتن از آتش) از فارسی میانهٔ war «سوگند، وَر» و اوستایی varah- است، و «باور» از فارسی میانهٔ wābar «راستی، باور» (مانوی wbr). چونگ «باور» را صورت شدیدیِ کهنِ ریشهٔ *u̯ar(H)- «برگزیدن؛ باور داشتن» می‌داند و معین در حاشیهٔ برهان جزء دوم آن را از مصدر اوستایی و پارسی باستان var «بازشناختن، اعتقاد داشتن» می‌گیرد. این ریشه هندواروپایی *u̯elH₁- «خواستن، برگزیدن» است (هم‌ریشه با لاتین volō و گوتی wiljan)، نه *wer- «گفتن». یادداشت خودِ نورایی که به ریشهٔ Wel 1 اشاره می‌کند همان دیدگاهی است که پژوهش امروزی (چونگ، آریان‌پور) می‌پذیرد.\",\n  \"sources\":[W+\"باور\"],\n  \"ref_check\":[\n   {\"ref\":\"BQT:230\",\"status\":\"partial\",\"note\":\"BQT_v1_pages.txt leaf 450 (≈p.230), Mo'in's footnote to باور: 'مرکب از دو جزو ... جزو دوم در پهلوی var و در اوستا varah از مصدر var اوستایی و پارسی باستان بمعنی بازشناختن واعتقادداشتن وباور کردن. اصطلاحا «ور» درایران باستان عبارت بوده از آزمایشهای گوناگونی که مدعی ومدعی‌علیه ... حقانیت خودرا اثبات کنند' — supports the var/bāvar/Av. var- link, says nothing of a root 'to speak'.\"},\n   {\"ref\":\"MON:4995\",\"status\":\"not_found\",\"note\":\"vajehyab Mo'in s.v. ور (https://vajehyab.com/moein/ور) shows only the homograph 'بغل، پهلو، سینه' [په.]; the ordeal sense on p. 4995 is not online. Page numbers cannot be mapped.\"}],\n  \"consulted\":[\n   {\"src\":\"PHD\",\"where\":\"s.v. war, wābar (PHD.txt l.603 and running text)\",\"stance\":\"partial\",\"note\":\"'war [wl] oath, ordeal'; 'wābar [wʾbl | M wbr, (N bāwar)] truth; belief. wābarīgān ... true, trustworthy' — gives forms, no IE root.\"},\n   {\"src\":\"NYB\",\"where\":\"vol. II s.v. passāxt (NYB_vol2_glossary.txt l.2992)\",\"stance\":\"partial\",\"note\":\"'accomplishment, performance, esp. of the var, the ordeal: var ~ ... hence ~ alone: ordeal' — confirms MP var 'ordeal'.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"p. 421 s.v. *u̯ar(H)¹\",\"stance\":\"contradicts\",\"note\":\"'NP giravidan \\\"to believe\\\" ... NP bavaridan (denomin. ?) ... NP bavar \\\"belief; credit\\\" (< old intensive) ... PIE *u̯elH₁- \\\"to want, wish\\\"'.\"},\n   {\"src\":\"ARY\",\"where\":\"pdf p. 109 s.v. باور; ARY_latin_index_pages.txt l.3104-3110\",\"stance\":\"contradicts\",\"note\":\"Aryanpur's cognate list for باور is the *wel- 'will' set: 'WILJA, WILJAN (GOTHIC) ... VAR, VARATA, VAIRYA'; 'WILLIO, WILLIAN ... BAWAR (AFGHANI)'; 'WILLA, WELLA ... VARAYATI, VRTA, VRNATI'.\"},\n   {\"src\":\"BQT\",\"where\":\"vol. 1 p. 230 (leaf 450)\",\"stance\":\"partial\",\"note\":\"Mo'in: جزء دوم از var «بازشناختن، اعتقاد داشتن» — Iranian link only.\"}]},\n {\"id\":3,\"lang\":\"Germanic\",\"words\":\"wurdam\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Proto-Germanic *wurdą (Watkins *wurdam) < PIE zero-grade *wr̥-dʰh₁-o- 'that which is said' (root *werh₁- with the *-dʰh₁- 'put, make' suffix). PIE *dʰ > Gmc *d, syllabic *r̥ > *ur. Goth. waurd, OE/OS word, OHG wort; Baltic cognates are OPruss. wirds and Lith. vardas 'name'.\",\n  \"derivation_fa\":\"ژرمنی آغازین *wurdą «واژه» از درجهٔ صفرِ *wr̥-dʰh₁-o- «آنچه گفته شده» است، از ریشهٔ *werh₁- «گفتن». dʰ هندواروپایی در ژرمنی d شده و r̥ هجایی ur. هم‌ریشه‌های آن گوتی waurd، انگلیسی کهن word، آلمانی کهن wort و لیتوانیایی vardas «نام» هستند. ادعای نورایی درست است.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/werh₁-\"],\n  \"ref_check\":[AHD6],\n  \"consulted\":[POK1162,WLD283,{\"src\":\"KLN\",\"where\":\"KLN_1971.txt s.v. word\",\"stance\":\"supports\",\"note\":\"'I.-E. *werdh- is an enlarged form of base *wer-, *were-, \\\"to speak\\\"' with Goth. waurd, OE word.\"}]},\n {\"id\":4,\"lang\":\"English\",\"words\":\"word\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English word < OE word < Proto-Germanic *wurdą (node #3). The form has barely changed since Old English; the meaning 'speech, utterance, single word' is inherited.\",\n  \"derivation_fa\":\"انگلیسی word از انگلیسی کهن word و آن از ژرمنی آغازین *wurdą (گره ۳) است. صورت واژه از دورهٔ انگلیسی کهن تقریباً دگرگون نشده است. ادعای نورایی درست است.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/werh₁-\"],\n  \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference given on the chart; checked against AHD wer-6 and Klein instead\"}],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1971.txt s.v. word\",\"stance\":\"supports\",\"note\":\"'word ... I.-E. *werdh- is an enlarged form of base *wer- \\\"to speak\\\"... Cp. hermeneutic, irony, rhetor, verb, verve'.\"},{\"src\":\"AHD\",\"where\":\"wer-6 (AHD_watkins1985.txt l.1148)\",\"stance\":\"supports\",\"note\":\"'Germanic *wurdam in Old English word, word: WORD'.\"}]},\n {\"id\":5,\"lang\":\"Latin\",\"words\":\"verbum\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Latin verbum 'word' < Proto-Italic *werðom < PIE *wer-dʰh₁-om (e-grade). Word-internal *dʰ became Latin -b- next to r (compare ruber : red, barba : beard; Klein). It is the exact cognate of Gmc *wurdą, with a different ablaut grade.\",\n  \"derivation_fa\":\"لاتین verbum «واژه» از ایتالیک آغازین *werðom و هندواروپایی *wer-dʰh₁-om (درجهٔ e) است. dʰ میانی در لاتین پس از r به b بدل شده (سنجیدنی با ruber در برابر red). این واژه هم‌ریشهٔ دقیق ژرمنی *wurdą است، با درجهٔ واکه‌ای دیگر. ادعای نورایی درست است.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/werh₁-\"],\n  \"ref_check\":[AHD6],\n  \"consulted\":[POK1162,{\"src\":\"KLN\",\"where\":\"KLN_1971.txt s.v. verb\",\"stance\":\"supports\",\"note\":\"'L. verbum, \\\"word, verb\\\", which derives fr. I.-E. base *werdh-, whence also Goth. waurd, OE. word ... For the change of I.-E. dh to b in Latin, cp. L. ruber and E. red'.\"},{\"src\":\"SYN\",\"where\":\"SYN.txt l.31586 (18.22)\",\"stance\":\"supports\",\"note\":\"'IE *wer- seen elsewhere in derivs. as Lat. verbum, OE word'.\"}]},\n {\"id\":6,\"lang\":\"English\",\"words\":\"verb, adverb, proverb\",\"verdict\":\"confirmed\",\n  \"derivation\":\"verb < ME verbe < OF verbe < Lat. verbum. The grammatical sense is a loan translation of Greek rhēma. adverb < F adverbe < Late Lat. adverbium, coined (Charisius) from ad + verbum as a calque of Greek epirrhēma. proverb < ME proverbe < OF proverbe < Lat. prōverbium (prō + verbum). All three entered English through Old/Middle French in the 14th century.\",\n  \"derivation_fa\":\"verb از فرانسوی کهن verbe و لاتین verbum است، و معنای دستوری آن گرته‌برداری از یونانی rhēma است. adverb از لاتین متأخر adverbium (ad + verbum) است، که گرتهٔ یونانی epirrhēma است. proverb از لاتین prōverbium (prō + verbum) است. هر سه از راه فرانسوی کهن در سدهٔ چهاردهم به انگلیسی میانه رسیده‌اند. ادعای نورایی درست است.\",\n  \"sources\":[],\n  \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference on the chart; AHD wer-6 lists 'VERB, VERVE; ADVERB, PROVERB'\"}],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt l.1748 s.v. adverb; l.30716 s.v. proverb; KLN_1971 s.v. verb\",\"stance\":\"supports\",\"note\":\"'adverb ... Late L. adverbium ... coined by the grammarian Flavius Sosipater Charisius fr. ad and verbum ... as a loan translation of Gk. epirrhēma'; 'proverb ... L. proverbium, fr. 1st pro- and verbum'.\"},{\"src\":\"AHD\",\"where\":\"wer-6\",\"stance\":\"supports\",\"note\":\"'Latin verbum, word: VERB, VERVE; ADVERB, PROVERB'.\"}]},\n {\"id\":7,\"lang\":\"Greek\",\"words\":\"eirein\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Greek eírō (Homeric) 'I say' < *wer-yō (PIE *wer(h₁)- + ye/o-present). Intervocalic *-ry- gave -ir- with compensatory change, and digamma *w- was lost (*werj- > eir-). The fut. erô and aor. pass. errhḗthēn (< *ewrēthēn) and rhḗtōr (Aeolic wrḗtōr) keep the root.\",\n  \"derivation_fa\":\"یونانی eírō «می‌گویم» از *wer-yō است، یعنی ریشهٔ *wer(h₁)- با پسوند مضارع -ye/o-. w آغازی (دیگاما) افتاده و ry به ir بدل شده است. آینده erô و rhḗtōr «سخنور» (ائولی wrḗtōr) همین ریشه را دارند. ادعای نورایی درست است.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/werh₁-\"],\n  \"ref_check\":[AHD6],\n  \"consulted\":[POK1162,WLD283,{\"src\":\"SYN\",\"where\":\"SYN.txt l.31586\",\"stance\":\"supports\",\"note\":\"'Grk. fut. erô, perf. eirēka ... (pres. eirō Hom., but not common) ... fr. wer-, wrē- ... IE *wer-'.\"}]},\n {\"id\":8,\"lang\":\"English\",\"words\":\"irony\",\"verdict\":\"plausible\",\n  \"derivation\":\"irony < Lat. īrōnīa < Greek eirōneía 'dissimulation, feigned ignorance', from eírōn 'dissembler'. Pokorny, Walde-Pokorny, Klein and AHD derive eírōn from eírō 'say' (*wer-yōn 'one who only says, without meaning it'). Beekes (EDG) regards eírōn as of unclear origin, so the last link is traditional but not secure. English took it in the 16th century, through Latin and French ironie.\",\n  \"derivation_fa\":\"انگلیسی irony از لاتین īrōnīa و یونانی eirōneía «خودرا به نادانی زدن، تجاهل» است، از eírōn «تجاهل‌کننده». پوکورنی، والده‌ـپوکورنی، کلاین و واتکینز eírōn را از eírō «گفتن» می‌دانند، یعنی «کسی که چیزی می‌گوید و مقصودش آن نیست». بیکس خاستگاه eírōn را روشن نمی‌داند، پس این پیوند پذیرفته ولی نه قطعی است و با احتیاط پذیرفتنی است.\",\n  \"sources\":[],\n  \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference on chart; AHD wer-6: 'Greek eirein, to say, speak: IRONY'\"}],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt l.19901 s.v. irony\",\"stance\":\"supports\",\"note\":\"'L. ironia, fr. Gk. eirōneia, \\\"irony\\\", fr. eirōn, \\\"dissembler\\\", for *wer-yōn, lit. \\\"sayer\\\" (i.e. one who speaks in order to hide his thoughts), fr. eirō ... \\\"I say, speak\\\"'.\"},POK1162]}]\nentry0={\"entry\":0,\"root\":\"Wer 1\",\"verdict\":\"confirmed\",\"modern_form\":\"PIE *werh₁- (*wer-, *wreh₁-) 'to speak, say' (LIV *u̯erh₁-; Pokorny 6. u̯er- 1162)\",\n \"note\":\"The root, its gloss and Pokorny p. 1162 are correct. The Western branch (word, verbum, eirō/irony) is textbook. The Iranian branch is the problem: only Av. urvata-/urvāta- 'command' is put here by Pokorny (and even that is doubted by Lubotsky). Av. var- 'choose, believe', varah- 'ordeal', NP var and bāvar belong to *u̯elH₁- 'to wish, choose' (Nourai's 'Wel 1'). His own NOTE on bâvar already points that way, and modern scholarship (Cheung 2007) takes that side.\",\n \"note_fa\":\"ریشهٔ هندواروپایی *werh₁- «گفتن» با معنا و ارجاع پوکورنی ۱۱۶۲ درست است، و شاخهٔ غربی آن (word، verbum، eirō و irony) پذیرفتهٔ همگان است. اما در شاخهٔ ایرانی تنها urvata- «فرمان» اوستایی را پوکورنی در این ریشه آورده است. var- «برگزیدن، باور داشتن»، varah- «وَر» و واژه‌های فارسیِ «وَر» و «باور» از ریشهٔ *u̯elH₁- «خواستن، برگزیدن» (Wel 1 نورایی) هستند. یادداشت خودِ نورایی هم به همین سو اشاره دارد و چونگ همین را می‌پذیرد.\",\n \"sources\":[W+\"Reconstruction:Proto-Indo-European/werh₁-\"],\n \"ref_check\":[{\"ref\":\"POK:1162\",\"status\":\"supports\",\"note\":\"POK_full.txt l.~92100-92153: '6. u̯er- ... Meaning: to talk, speak ... Page(s): 1162-1163'.\"}],\n \"consulted\":[WLD283,{\"src\":\"AHD\",\"where\":\"wer-6 (AHD_watkins1985.txt l.1148)\",\"stance\":\"supports\",\"note\":\"'wer-6. Also werə-. To speak. Variant *wrē- ... [Pok. 6. wer- 1162.]'\"},{\"src\":\"SYN\",\"where\":\"SYN.txt l.31586\",\"stance\":\"supports\",\"note\":\"'IE *wer- ... Lat. verbum, OE word ... Av. urvata- \\\"command\\\" ... Walde-P. 1.283 f.'\"}],\n \"nodes\":nodes0}\n\nnodes1=[\n {\"id\":1,\"lang\":\"Avestan / Old Persian\",\"words\":\"varet, wars, vart; ni-vart\",\"verdict\":\"plausible\",\n  \"derivation\":\"YAv. varət- 'to turn' (inj. varətata, caus. ham.varətaiianti; Cheung *u̯art) = Skt. vártate, Lat. vertō < PIE *wert-. The OP vart- (DB 4.44 *vartaiyaiy) rests on a damaged passage that Kent reads as caus. of vart- 'turn', while Gershevitch reads *vratiyaiy 'I swear' instead, so OP vart- is uncertain. 'wars' cannot be identified as an attested Avestan/OP form; it may stand for the s-extension (*wert-s-, cf. Khot. bais- < *u̯art-s-aja-). ni-vart 'roll down' is a reconstructed compound *ni-u̯art-, attested in Khotanese nyūdāre 'they roll down' (Bailey: 'From ni-vart-') and Sogd. nwrt-, Parth. nwrd 'set (of sun)', and behind NP navardīdan.\",\n  \"derivation_fa\":\"اوستایی varət- «گشتن، چرخیدن» هم‌ریشهٔ سنسکریت vártate و لاتین vertō است و از هندواروپایی *wert- می‌آید. صورت پارسی باستان vart- بر پایهٔ سطری آسیب‌دیده از بیستون است که کنت آن را «گرداندن» و گرشویچ «سوگند می‌خورم» می‌خواند، پس قطعی نیست. «wars» در متون شناخته نیست. ni-vart «فروغلتیدن» صورتی بازسازی‌شده است که در ختنی nyūdāre «فرو می‌غلتند» و سغدی nwrt- دیده می‌شود و پشتوانهٔ «نوردیدن» فارسی است. در کل با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/wert-\"],\n  \"ref_check\":[\n   {\"ref\":\"KLN:1703\",\"status\":\"supports\",\"note\":\"KLN_1971.txt s.v. version (L. vertere): 'OI. vartate ... vṛttah ... Avestic varət-, \\\"to turn\\\" (intr.), OSlav. vrŭteti'.\"},\n   {\"ref\":\"ISS:223\",\"status\":\"not_checked\",\"note\":\"Khotanese Texts VI not on disk; Bailey's DKS (ISS_alt_DKS.txt l.3808) s.v. nyūdāre: '\\\"roll down\\\" ... From ni-vart-' and l.4998 s.v. bad- 'turn': 'Base vart- \\\"turn, roll\\\" ... To Av., O.Pers. vart- ... N.Pers. gard-, gaštan (or base gart-)'.\"},\n   {\"ref\":\"KNT:207\",\"status\":\"supports\",\"note\":\"KNT_full.txt l.28821: 'vart- vb. \\\"turn\\\", trans. in active, refl. or intrans. in middle: Av. varət-, Skt. vṛt-, pres. vártati vártate, Lat. vertit, Gm. werden \\\"become\\\", pIE *wert-. [va]rtaiyaiy 1st sg. mid. caus. ... DB 4.44 (Cameron's reading...)'.\"}],\n  \"consulted\":[CH_uart,\n   {\"src\":\"BRT\",\"where\":\"varət- (BRT.txt; OCR of the headword unreadable), cited by Horn and Mo'in as 'Bartholomae ... varət-'\",\"stance\":\"supports\",\"note\":\"Horn p.198 quotes 'aw. ... varətanąm (vd. 14, 6) und varətata (ZPGl.)' from Bartholomae; Mo'in BQT:1820 footnote 'اوستا varət «بارتولمه ...»'.\"},\n   POK1156]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"gardîdan; gardan\",\"verdict\":\"plausible\",\n  \"derivation\":\"NP gardīdan / gaštan (pres. gard-) < MP gard- 'turn, revolve' (PHD 'gard- [glt-] turn, revolve'; MMP grd-). Horn (no. 886), Mo'in, Aryanpur and Wiktionary derive it from Iranian *wart- (Av. varət-) with a Western Iranian *wa- > ga- development. Hübschmann already doubted that g from v was proven. Nyberg and Cheung separate MP gard- (from an Iranian root *gart- 'twist, turn', perhaps an enlargement of *gar-) from the genuine *u̯art- reflex MP ward- 'turn, writhe', and allow only that it was 'semasiologically influenced' by *u̯art-. Cheung writes 'NP gardidan (< *u̯art- ?)'. gardan 'neck' < MP gardan [gltn'] (PHD, Nyberg 'gartan neck'); Horn derives it from *vartana- 'turning (part)'. Bailey instead connects Khot. ggaḍaa- 'throat' 'to gart- \\\"turn\\\", cf. NPers. gardan', and Wiktionary also compares Khotanese gaḍaa-, which points to *gart- rather than *wart-. The broader 'turning' etymology holds, but the *wart- route is contested, hence plausible.\",\n  \"derivation_fa\":\"«گردیدن / گشتن» (ستاک گرد-) از فارسی میانهٔ gard- «گشتن، چرخیدن» است. هرن، معین، آریان‌پور و ویکی‌واژه آن را از ایرانی *wart- (اوستایی varət-) با دگرگونی wa- به ga- می‌دانند. اما هوبشمان بدل شدن w به g را ثابت‌نشده می‌دانست، و نیبرگ و چونگ gard- را از ریشهٔ جداگانهٔ ایرانی *gart- «پیچیدن، گشتن» می‌گیرند که تنها از نظر معنا زیر نفوذ *wart- (فارسی میانهٔ ward-) بوده است. «گردن» از فارسی میانهٔ gardan است. هرن آن را از *vartana- «چرخنده» می‌داند، ولی بیلی آن را با ختنی ggaḍaa- «گلو» به *gart- پیوند می‌دهد. پس معنای «چرخیدن» درست است ولی راه *wart- مورد اختلاف است، و ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"گردیدن\",W+\"گشتن\",W+\"گردن\"],\n  \"ref_check\":[\n   {\"ref\":\"HRN:198\",\"status\":\"supports\",\"note\":\"HRN.txt leaf 219 (p.198) no. 886: 'gaštan \\\"wenden, drehen\\\" ... gerdīden ... ai. √vart-, vártate \\\"sich wenden, drehen\\\"; aw. vergl. ... varətanąm (vd. 14, 6) und varətata (ZPGl.); phlv. ... vartitan, gartitan (Bund.)'.\"},\n   {\"ref\":\"HRN:201\",\"status\":\"supports\",\"note\":\"HRN.txt leaf 222 (p.201) no. 903: 'gerden \\\"Nacken, Hals\\\" ... ap. *vartana-, etwa \\\"Wirbel\\\", zu √vart-; phlv. gartan'; no. 904 'gerdūn \\\"Firmament; Wagen\\\". ai. vartani-'.\"},\n   {\"ref\":\"BQT:1820\",\"status\":\"supports\",\"note\":\"ref_page.py BQT:1820 (vol.3 pdf 617), Mo'in's footnote to گشتن: '«گردیدن» پهلوی vaštan ؛ اوستا varət «بارتولمه ...» هندی باستان vart «نیبرگ ص ۲۳۹» ... گردیدن، چرخیدن، دور زدن'.\"},\n   {\"ref\":\"BQT:1787\",\"status\":\"partial\",\"note\":\"ref_page.py BQT:1787 (vol.3 pdf 584): entries گرد / گردان / گردا گرد; Mo'in: 'از: گرد (گردیدن) + ان (پسوند فاعلی) یعنی گردنده' — treats gardān etc. as from gardīdan, no older form given for گردن on this page.\"},\n   {\"ref\":\"BLY:75\",\"status\":\"contradicts\",\"note\":\"Bailey, Hvatanica (via DKS, ISS_alt_DKS.txt l.57): 'ggaḍaa- \\\"throat\\\" (?), then to gart- \\\"turn\\\", cf. NPers. gardan \\\"neck\\\"' — Bailey links gardan to *gart-, not *vart-. BLY_pages leaf 8 (p.75) OCR shows no gard/vart match.\"}],\n  \"consulted\":[CH_gart,NYB_gart,\n   {\"src\":\"HUB\",\"where\":\"p. 91-92, notes to Horn 903-904 (HUB.txt l.3242-3255)\",\"stance\":\"partial\",\"note\":\"'903. Die Etym. ist möglich, aber unsicher, so lange der Beweis für die Entstehung von g aus v nicht aus dem Iranischen erbracht ist. Phl. gartan mit g'; '904 ... Np. gardūn kann nur = phl. *gartūn ... oder *vartūn gesetzt werden'.\"},\n   {\"src\":\"PHD\",\"where\":\"s.v. gard-, gardan\",\"stance\":\"partial\",\"note\":\"'gard- [glt-yin' | M grd-, N ~] turn, revolve. ~išn: revolution'; 'gardan [gltn' | M grdn, N ~] neck' — separate from 'ward-, v. waštan'.\"},\n   {\"src\":\"ARY\",\"where\":\"pdf p. 438 (printed 439) s.v. گشتن، گردیدن، گشت\",\"stance\":\"supports\",\"note\":\"Aryanpur lists Avestan, Pahlavi, Sanskrit, Latin, Gothic, OHG cognates of the *wert- set; 'چم این واژه در آلمانی: شدن؛ گردیدن' (German werden); 'برهان قاطع: ۱۷۹۲'.\"},\n   {\"src\":\"BQT\",\"where\":\"vol. 3 p. 1820\",\"stance\":\"supports\",\"note\":\"Mo'in: اوستا varət, هندی باستان vart.\"}]},\n {\"id\":3,\"lang\":\"Persian\",\"words\":\"gerd; gerdŭ; gard\",\"verdict\":\"plausible\",\n  \"derivation\":\"gerd/gird 'round' < MP gird [glt] 'round, circular' (PHD; Nyberg girt). Horn (no. 901) compares Skt. vṛttá- 'turned, round' < *wr̥tá-, and Wiktionary follows *wart-. But Hübschmann notes that *vṛta- should give NP *gurd, not gird, and so posits OP *gṛta-. Nyberg derives girt 'From gart-'. The 'round = turned' semantics is clear, but the root is again *gart- rather than *wart- for these scholars. gerdū 'walnut' = gird + -ū 'the round one' (Horn 901 'girdū \\\"Wallnuss\\\"'; Wiktionary 'گرد + ـو'). gard 'dust' < MP gard [glt] 'dust' (PHD), Pahl. vart/gart 'Staub' (Hübschmann 902). Horn explains it as 'ursprünglich wirbelnd, sich drehend', and Wiktionary as 'from the same root as gaštan'. That sense link is reasonable but speculative. The quoted gorde 'round loaf; powder' (script_extra گرده) is gird + -a.\",\n  \"derivation_fa\":\"«گِرد» از فارسی میانهٔ gird «گرد، مدوّر» است. هرن آن را با سنسکریت vṛttá- «چرخیده، گرد» می‌سنجد و ویکی‌واژه هم *wart- را می‌پذیرد، اما هوبشمان می‌گوید از *vṛta- باید «گُرد» پدید می‌آمد نه «گِرد»، و نیبرگ girt را از *gart- می‌داند. «گردو» از «گرد» + پسوند «ـو» به معنای «گِردینه» است. «گَرد» (غبار) از فارسی میانهٔ gard است و هرن آن را در اصل «چرخنده، گردباد» می‌داند. پیوند معنایی «گرد = چرخیده» روشن است ولی ریشهٔ دقیق (*wart- یا *gart-) مورد اختلاف است، پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"گرد\",W+\"گردو\",W+\"Reconstruction:Proto-Indo-European/wert-\"],\n  \"ref_check\":[\n   {\"ref\":\"HRN:201\",\"status\":\"supports\",\"note\":\"HRN.txt leaf 222 (p.201): '901. (2) gird rund; rings herum ... girde \\\"rundes Brot\\\" ... girdū \\\"Wallnuss\\\". ai. vṛttá- \\\"gedreht, rund\\\"'; '902. gerd \\\"Staub\\\" (ursprünglich \\\"wirbelnd, sich drehend\\\"). ai. √vart-, vártate \\\"sich drehen\\\"'.\"},\n   {\"ref\":\"HRN:198\",\"status\":\"partial\",\"note\":\"p.198 no. 886 gaštan/gerdīden < √vart- — the verb, not the adjectives.\"},\n   {\"ref\":\"BQT:1787\",\"status\":\"supports\",\"note\":\"ref_page.py BQT:1787 (vol.3 pdf 584), entries گرد 'مدور ... گرد آفتاب ... غبار'; Mo'in's footnote: 'پهلوی gird ... هوبشمان اسشق ۹۰۱ ... (گرده، نان)' — gird = Pahl. gird, Hübschmann no. 901.\"},\n   {\"ref\":\"BQT:1820\",\"status\":\"partial\",\"note\":\"vol.3 pdf 617: footnote on گشتن/گردیدن < Av. varət — the verb only.\"}],\n  \"consulted\":[\n   {\"src\":\"HUB\",\"where\":\"p. 91 notes to Horn 901-902 (HUB.txt l.3230-3243)\",\"stance\":\"partial\",\"note\":\"'901. Np. gird ... liegt im Phl. als g(i)rt vor ... Ich würde danach als Grundform ap. *gṛta- ansetzen. Dem steht allerdings die ansprechende Zusammenstellung von np. gird mit skr. vart ... entgegen. Aber skr. *vṛta- wäre = phl. *gurt = np. *gurd'; '902. Np. gard \\\"Staub\\\" = phl. vart \\\"Staub\\\"'.\"},\n   NYB_gart,\n   {\"src\":\"PHD\",\"where\":\"s.v. gird, gard\",\"stance\":\"partial\",\"note\":\"'gird [glt' | M gyrd, N ~] round, circular; gathered'; 'gard [glt' | N ~] dust' — forms only.\"},\n   {\"src\":\"MON\",\"where\":\"vajehyab s.v. گرده (https://vajehyab.com/moein/گرده)\",\"stance\":\"supports\",\"note\":\"'[په.] (ص مر.) 1 - هرچیز گرد و مدور مانند: نان' — gorde = gird + -a.\"}]},\n {\"id\":4,\"lang\":\"Persian\",\"words\":\"vardaneh; navardîdan\",\"verdict\":\"confirmed\",\n  \"derivation\":\"navardīdan 'to fold, roll up; to traverse' (pres. navard-) < *ni-u̯art- 'turn/roll down'. Cheung lists 'NP nawardidan/naward- \\\"to fold, cease; to twist; to stroll\\\"' under *u̯art, and Khot. nyūd- (Bailey) and Sogd. nwrt- are its cognates. Here the initial w- is kept after the preverb (ni-w- > naw-), so the *wart- reflex is regular. The sense 'travel' (daryānavard, kuhnavard) comes from 'roll up (the road)'. vardane 'rolling pin' (Mo'in: 'نورد؛ چوب استوانه شکلی که خمیر را با آن پهن می‌کنند') is from the simplex ward- 'roll' + -an-a. It keeps w-, as in MP ward- 'turn, writhe'.\",\n  \"derivation_fa\":\"«نوردیدن» (ستاک نَوَرد-) «پیچیدن، تا کردن، پیمودن» از *ni-u̯art- «فروغلتاندن، پیچیدن» است. چونگ آن را زیر ریشهٔ *u̯art «گشتن» آورده است، و ختنی nyūd- و سغدی nwrt- هم‌ریشهٔ آن‌اند. در اینجا w پس از پیشوند ni- مانده است، پس دگرگونی آوایی آن منظم است. معنای «پیمودن» (دریانورد، کوه‌نورد) از «درنوردیدنِ راه» برآمده است. «وَردَنه» (چوب پهن کردن خمیر) از ستاک ساده ward- «غلتاندن» با پسوند -ana است. ادعای نورایی درست است.\",\n  \"sources\":[],\n  \"ref_check\":[\n   {\"ref\":\"HRN:235\",\"status\":\"supports\",\"note\":\"HRN.txt leaf 256 (p.235) no. 1050: 'neverdīden (neverden) \\\"drehen, winden, wandern\\\" ... neverd. ai. ni + √vart- \\\"zurückkehren...\\\" Wenn die Etymologie richtig ist, so wäre die ursprüngliche Form *niverdīden' — Horn supports, with a caveat.\"},\n   {\"ref\":\"BQT:2186\",\"status\":\"partial\",\"note\":\"ref_page.py BQT:2186 (vol.4 pdf 269, running head OCR '-۱۸۹-'): entries نورد 'بمعنی پیچ و تاب ... ونام افزاری است جولاهگان را ... چوبی باشد مدور وطولانی', نوردان 'مخفف نوردیدن است که بمعنی پیچیدن و طی کردن باشد'; Mo'in only cross-refers 'رك : نوردیدن'. No older form on this page.\"}],\n  \"consulted\":[CH_uart,\n   {\"src\":\"ISS_alt_DKS\",\"where\":\"DKS s.v. nyūdāre (ISS_alt_DKS.txt l.3808)\",\"stance\":\"supports\",\"note\":\"'nyūdāre \\\"roll down\\\" ... From ni-vart-, see cognates s.v. badāri \\\"they roll\\\"'.\"},\n   {\"src\":\"MON\",\"where\":\"vajehyab s.v. نوردیدن, وردنه\",\"stance\":\"supports\",\"note\":\"'نوردیدن (مص م.) 1 - پیچیدن، تا کردن. 2 - پیمودن'; 'وردنه (اِ.) نورد؛ چوب استوانه شکلی که خمیر را با آن پهن می کنند'.\"}]},\n {\"id\":5,\"lang\":\"Sogdian\",\"words\":\"gwrdtq\",\"verdict\":\"plausible\",\n  \"derivation\":\"Gharib no. 4423 'γwrdtq C, γurδak ? < Av. vərəδka, Yaghn. γurkak ... MP gurdag ... kidney (?)' gives Christian Sogdian γwrdtq 'kidney'. The meaning is marked with a query (Sims-Williams). Nourai's 'gwrdtq' is the same word with g for γ. It is the Sogdian cognate of Av. vərəδka- (*wr̥tka-), with Sogdian γ- < *w- before r (as in Yaghnobi γurkak). It should hang under the Av. kidney node rather than directly under the root, but that is only a matter of how the chart is drawn.\",\n  \"derivation_fa\":\"سغدی مسیحی γwrdtq (خوانش γurδak) «گُرده، کلیه» را قریب (شمارهٔ ۴۴۲۳) با نشانهٔ پرسش آورده و با اوستایی vərəδka-، یغنابی γurkak و فارسی میانهٔ gurdag سنجیده است. g در نوشتهٔ نورایی همان γ سغدی است. این واژه هم‌ریشهٔ اوستایی vərəδka- (از *wr̥tka-) است و w پیش از r در سغدی به γ بدل شده است. با احتیاط پذیرفتنی است.\",\n  \"sources\":[],\n  \"ref_check\":[{\"ref\":\"SOD:176\",\"status\":\"supports\",\"note\":\"SOD_pages.txt l.16302-16353 (page headed 177; entry 4423): 'γwrdtq C ... γurδak ? <Av. vərəδka, Yaghn. γurkak ... MP gurdag; Khot. ... kidney(?) ... S W, BSOAS 1983, 49'; also entry 4420 'γwrdtq-y \\\"kidney\\\" ?'.\"}],\n  \"consulted\":[{\"src\":\"SOD\",\"where\":\"no. 4423\",\"stance\":\"supports\",\"note\":\"'kidney(?)' with Av. vərəδka, MP gurdag.\"},{\"src\":\"POK\",\"where\":\"p. 1157\",\"stance\":\"partial\",\"note\":\"Pokorny lists Av. vərəδka-, Pahl. gurtak, NP gurda under uer-t-; Sogdian not mentioned.\"}]},\n {\"id\":6,\"lang\":\"Avestan\",\"words\":\"verdeka, veredka\",\"verdict\":\"plausible\",\n  \"derivation\":\"YAv. vərəδka- (dual 'the two kidneys', V. 18.70), Pazand-glossary varətka- (Bartholomae 'varəδka-, *varətka- m. Du. \\\"Nieren\\\"') = Skt. vṛkká- (dual vṛkkáu) < Indo-Iranian *wr̥tká-. Pokorny and Walde-Pokorny put it under *wert- 'turn' ('actually \\\"bulge, roll\\\"'), which matches the chart's NOTE 'because of its round shape'. Mayrhofer and Wiktionary reconstruct *wr̥tká- without committing to that root, so the forms are confirmed and the root link is a plausible traditional one.\",\n  \"derivation_fa\":\"اوستایی vərəδka- (به صورت دوگانه «دو گُرده»، وندیداد ۱۸٫۷۰) و varətka- هم‌ریشهٔ سنسکریت vṛkká- است و از هندوایرانی *wr̥tká- می‌آید. پوکورنی و والده‌ـپوکورنی آن را زیر ریشهٔ *wert- «گشتن» آورده‌اند، به معنای «برآمدگی گرد». این با یادداشت نورایی («به سبب شکل گرد آن») همخوان است. صورت‌ها درست‌اند و پیوند با ریشه پذیرفتنی ولی نه قطعی است.\",\n  \"sources\":[W+\"گرده\"],\n  \"ref_check\":[{\"ref\":\"POK:1157\",\"status\":\"supports\",\"note\":\"POK_full.txt l.~91770: 'vṛkkāu (*vṛtka-) \\\"kidneys\\\" (actually \\\"bulge; ... roll\\\"), Avestan vərəδka- varətka- ds., compare Pahlavi gurtak, npers. gurda \\\"kidney\\\"' (Page(s): 1156-1158).\"}],\n  \"consulted\":[\n   {\"src\":\"BRT\",\"where\":\"col. ~1419 s.v. varəδka- (BRT.txt l.23649)\",\"stance\":\"supports\",\"note\":\"'varəδka-, *varətka- m. Du. \\\"Nieren\\\": yat antarə °ka as ... V. 18.70'.\"},\n   WLD274,\n   {\"src\":\"HUB\",\"where\":\"§ on tk (HUB.txt l.7398-7403)\",\"stance\":\"supports\",\"note\":\"'np. gurda \\\"Niere\\\" = phl. gurtak = zd. vərədka- ... oder varətka- ... skr. vṛkka-'.\"}]},\n {\"id\":7,\"lang\":\"Pahlavi\",\"words\":\"gurtak\",\"verdict\":\"confirmed\",\n  \"derivation\":\"MP gurdag [gwltk'] 'kidney' (MacKenzie; older transliteration gurtak) < *wr̥tka-ka- / *wr̥t-ak. Initial *wr̥- > MP gur- is regular (cf. gurg 'wolf' < *wr̥ka-, gurs- 'hunger'). Hübschmann notes the -d- (rather than expected -hk-) as a peculiarity.\",\n  \"derivation_fa\":\"فارسی میانهٔ gurdag (خوانش کهن‌تر gurtak) «گرده، کلیه» از *wr̥tka- است. wr̥- آغازی در فارسی میانه به‌طور منظم gur- شده است، مانند gurg «گرگ» از *wr̥ka-. ادعای نورایی درست است.\",\n  \"sources\":[W+\"گرده\"],\n  \"ref_check\":[{\"ref\":\"MON:3255\",\"status\":\"not_checked\",\"note\":\"Mo'in's 6-vol. page not online; vajehyab shows only the 'round thing' homograph of گرده. 2-vol. Mo'in (MON_part2.txt l.31289): 'گرده ... [قس. کلیه] (ا.) کلیه، قلوه'.\"}],\n  \"consulted\":[\n   {\"src\":\"PHD\",\"where\":\"s.v. gurdag\",\"stance\":\"supports\",\"note\":\"'gurdag [gwltk' | N ~a] kidney'.\"},\n   {\"src\":\"HUB\",\"where\":\"p. 78/§ (HUB.txt l.5504, 5679)\",\"stance\":\"supports\",\"note\":\"'gurda \\\"Niere\\\" = phl. gurtak ZPGl. ... zd. vərədka-'.\"},\n   {\"src\":\"NYB\",\"where\":\"vol. II\",\"stance\":\"silent\",\"note\":\"grep '^gurtak' finds no headword in the glossary.\"}]},\n {\"id\":8,\"lang\":\"Persian\",\"words\":\"gordeh\",\"verdict\":\"confirmed\",\n  \"derivation\":\"NP gurda / gorde 'kidney' < MP gurdag with loss of final -g (-ag > -a), as in all MP -ag nouns. Kurdish gurdale and N. Luri gördāla are cognates. Horn no. 905 and Wiktionary agree.\",\n  \"derivation_fa\":\"«گُرده» (کلیه) از فارسی میانهٔ gurdag است که در آن -ag پایانی، مانند همهٔ نام‌های -ag فارسی میانه، به -a (ـه) بدل شده است. کردی gurdale و لری شمالی gördāla هم‌ریشهٔ آن‌اند. ادعای نورایی درست است.\",\n  \"sources\":[W+\"گرده\"],\n  \"ref_check\":[{\"ref\":\"MON:3255\",\"status\":\"partial\",\"note\":\"2-vol. Mo'in (MON_part2.txt l.31289): 'گرده ... [قس. کلیه] (ا.) کلیه، قلوه' — meaning confirmed, no etymology in the abridgement; 6-vol. p. 3255 not online.\"}],\n  \"consulted\":[\n   {\"src\":\"HRN\",\"where\":\"p. 202 no. 905 (HRN.txt leaf 223)\",\"stance\":\"supports\",\"note\":\"'905. gurde \\\"Niere\\\". aw. (Du.) vərəδka- (vd. 18, 70), varətka- \\\"beide Nieren\\\" (ZPGl.); phlv. gurtak; ai.-prākr. (Du.) vṛkkā- \\\"Nieren\\\". kurd. gurdale'.\"},\n   {\"src\":\"HUB\",\"where\":\"HUB.txt l.7398\",\"stance\":\"supports\",\"note\":\"'np. d eingetreten in gurda \\\"Niere\\\" = phl. gurtak = zd. vərədka-'.\"},\n   {\"src\":\"PHD\",\"where\":\"s.v. gurdag\",\"stance\":\"supports\",\"note\":\"'gurdag ... N ~a kidney'.\"}]}]\nentry1={\"entry\":1,\"root\":\"Wer 2, Werb, Werg 3, Wermi, Kwermi, Werp, Wert, Wrei\",\"verdict\":\"confirmed\",\"part\":1,\n \"modern_form\":\"PIE *wer- 'to turn, bend' with its enlargements *wert-, *werg-, *werb-, *werp-, *wreyH- etc. (Pokorny uer-3, pp. 1152-1160; AHD wer-3)\",\n \"note\":\"Pokorny's uer-3 complex and the gloss are correct; modern handbooks (LIV) treat *wert- etc. as separate roots, but the grouping is standard. On this page all Iranian nodes use *wert- (uer-3 H, Pok. 1156-1158). The genuine *u̯art- reflexes are Av. varət-, navardīdan, vardane, and the kidney words (vərəδka-, gurdag, gorde). gardīdan/gaštan, gardan and gird are assigned by Nyberg, Cheung and Bailey to a separate Iranian *gart- 'twist, turn', so their link is only plausible.\",\n \"note_fa\":\"ریشهٔ هندواروپایی *wer- «گشتن، خم کردن» با گسترش‌های *wert-، *werg-، *werb-، *werp- و جز آن (پوکورنی uer-3) و معنای آن درست است. گره‌های ایرانی این صفحه از *wert- (پوکورنی ۱۱۵۶ تا ۱۱۵۸) گرفته شده‌اند. بازتاب‌های بی‌گمان *u̯art- اوستایی varət-، «نوردیدن»، «وردنه» و واژه‌های «گرده» (کلیه) هستند. اما «گردیدن / گشتن»، «گردن» و «گرد» را نیبرگ، چونگ و بیلی از ریشهٔ جداگانهٔ ایرانی *gart- «پیچیدن» می‌دانند، پس پیوند آن‌ها تنها پذیرفتنی است.\",\n \"sources\":[W+\"Reconstruction:Proto-Indo-European/wert-\"],\n \"ref_check\":[{\"ref\":\"POK:1142-1157\",\"status\":\"supports\",\"note\":\"POK_full.txt l.91474-91950: 'uer-3' with sections A. u̯ṛmi-s (worm), B. uer-b-, D. uer-g-, E. uer-gh-, G. uer-p-, H. uer-t- 'to turn, wind' (Page(s): 1156-1158), I. ur-ei- — matches Nourai's root list (Wermi, Werb, Werg, Werp, Wert, Wrei).\"}],\n \"consulted\":[WLD274,{\"src\":\"AHD\",\"where\":\"wer-3 (AHD_watkins1985.txt l.1145)\",\"stance\":\"supports\",\"note\":\"wer-3 'To turn, bend' with 'II. Root *wreit-... III. Root *wergh-... IV. Root *werg-... VII. Root *werb-... VIII. Root *werp-... IX. Root *wṛmi-, worm; rhyme word to kʷṛmi-'.\"},{\"src\":\"CHEUNG\",\"where\":\"p. 423-424 s.v. *u̯art\",\"stance\":\"supports\",\"note\":\"'PIE *u̯ert- \\\"to turn\\\" — LIV: 691 f. | Pok.: 1156 ff.'\"}],\n \"nodes\":nodes1}\nout={\"pdf_page\":544,\"book_page\":514,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":[entry0,entry1]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-544.json','w'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-544.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-544.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 544"
}
```


### [2026-10-17T00:12:37.361Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'disputed': 2, 'confirmed': 8, 'plausible': 6}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 9, 'not_found': 1, 'supports': 13, 'not_checked': 5, 'contradicts': 1}
books consulted: {'partial': 9, 'contradicts': 6, 'supports': 34, 'silent': 2} | by book: {'POK': 6, 'CHEUNG': 5, 'PHD': 5, 'KLN': 5, 'HUB': 5, 'WLD': 4, 'NYB': 4, 'BRT': 3, 'ARY': 2, 'BQT': 2, 'AHD': 2, 'SYN': 2, 'MON': 2, 'KNT': 1, 'ISS_alt_DKS': 1, 'SOD': 1, 'HRN': 1}
```


## [2026-10-17T00:12:50.618Z] TOOL CALL #75: SubagentHandback

```json
{
 "message": "I wrote the page 544 verification file and ran verify_check.py 544. It shows 16/16 nodes and 0 PROBLEM lines.\n\nFile: /home/sfmqrb/git/rishe-private/data/verification/page-544.json\n\n- **Roots:** 2 confirmed (Wer 1 \"to speak\", Pokorny 1162; Wer 2 / Wert \"to turn\", Pokorny 1156-1158).\n- **Nodes:** 8 confirmed, 6 plausible, 2 disputed, 0 transcription_suspect.\n\n**Disputed:**\n- Wer 1 #1, Avestan \"ver 2; varah; upa-var\": only urvata-/urvāta- \"command\" belongs under *wer- \"speak\" (Pokorny, Klein, Buck), and Wiktionary, after Lubotsky, doubts even that. Av. var- \"choose, believe\", varah- \"ordeal\" and upā-var come from Iranian *u̯ar(H)- < PIE *u̯elH₁- \"wish, choose\" (Cheung; Bartholomae ties varah- to var- \"choose\").\n- Wer 1 #2, Persian \"var; bâvar\": MP war \"ordeal\" and MP wābar \"belief\" come from the same *u̯elH₁- root. Cheung calls bāvar an \"old intensive\" of it, and Aryanpur's cognates for باور are the Gothic wiljan / \"will\" set. Nourai's own NOTE pointing to \"Wel 1\" is the side modern scholarship takes.\n\n**Plausible items worth knowing:** gardîdan/gardan (Wer 2 #2) and gerd/gerdu/gard (#3). Horn, Mo'in, Aryanpur and Wiktionary derive them from *wart-. Nyberg, Cheung and Bailey instead put MP gard-/gird/gardan under a separate Iranian *gart- \"twist, turn\", and Hübschmann doubted that g- can come from v-. The other plausible items are #1 (OP vart- rests on a doubtful reading, and \"wars\" is not an attested form), #5 (Gharib marks Sogdian γwrdtq \"kidney\" with a query) and #6 (Av. vərəδka- is linked to *wert- only by tradition). For the Wer 1 nodes, I rated irony plausible because Beekes treats eirōn as of unclear origin.\n\n**Extraction errors:** none found, and no page image was needed.\n\n**Reference gaps:**\n- MON:4995 and MON:3255 cannot be mapped online.\n- The image of BQT:2186 (vol. 4, pdf 269) shows the نورد/نوردان entries. Its running-head number did not OCR cleanly.\n- ISS:223 is not on disk; I used Bailey's Dictionary of Khotan Saka instead.\n- The Etymonline fetches failed, so they are not cited."
}
```


### [2026-10-17T00:12:50.932Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
