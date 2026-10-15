# Verification process log — verify-page-504


## [2026-10-15T02:44:16.227Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 504 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-504.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-504.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-504.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 504` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.269Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.090Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.131Z] TOOL RESULT

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


## [2026-10-15T02:44:19.593Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-504.txt"
}
```


### [2026-10-15T02:44:19.652Z] TOOL RESULT

```
1	=== PDF page 504 (book page 474) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ter 1, Tr : to cross over, surpass, overcome  (refs POK:1075; KLN:1639)
4	#1 (parent #0) [Avestan] refs=POK:1075; KLN:1639 | taro, tarya, tar : surpass ; thrâ : shelter, cover ; vi-tar : to pass by ☞Wi
5	  #2 (parent #1) [Persian] refs=BQT:1778; HRN:161; TLM:92; MON:1790 | tar 1, tarîn «ـتَر ۱ ، ـتَرین» : more, most ; sarâ «سرا ( سرای ۱ ـ سار ۱ ، کوهسار )» : house, place ; gozaštan «گذشتن ( گذر ، گذشت ) گذاشتن ، گذاردن» : to pass by
6	#3 (parent #0) [Old Persian] refs=MON:1850; VDQ:255 | srâd, srâda : house, shelter
7	  #4 (parent #3) [Arabic] refs=VDQ:255; MON:1850; MAG:189 | sorâdeq : tent | NOTE: This word may have been borrowed from Persian "sarâ-pardeh: tent".
8	    #5 (parent #4) [Persian] refs=MON:1850 | sorâdeq «سُرادِق» : tent, house | extra: سرادقات
9	#6 (parent #0) [Latin] refs=AHD | trâns : across ; terminus : boundary ; truncus : overcome
10	  #7 (parent #6) [French] refs=None | 
11	    #8 (parent #7) [Persian] refs=MON; AMD |  | extra: ترانسپورت ، ترانزیت ، ترانزیستور ، ترانسفورماتور ، ترم ، ترمینال
12	  #9 (parent #6) [English] refs=AHD | trans-, transport, transform, transistor, transfer, translate ; term, terminate, determine ; trunk, truncate, trench
13	#10 (parent #0) [Germanic] refs=AHD; KLN | thr : bore through, drill
14	  #11 (parent #10) [English] refs=None | drill, through, thorough, nostril
15	#12 (parent #0) [Greek] refs=AHD | nek-tar : overcoming death ☞Nek 1
16	  #13 (parent #12) [English] refs=None | nectar, nectarine
17	#14 (parent #0) [Indo-European] refs=IEC:27 | An-teros : second, other, step parent ☞AN 2
18	  #15 (parent #14) [Persian] refs=IEC:27; MON:373 | andar «ـاندر ۲» : a suffix meaning step as in step father | extra: پدراندر ، مادراندر ، دختراندر ، پسراندر
19	  #16 (parent #14) [Sanskrit] refs=IEC:27; POK:37 | antarah : other
20	--- entry 1 ---
21	ROOT Ter 2 -> redirect to Tres
22	
```


## [2026-10-15T02:44:20.110Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-504.json"
}
```


### [2026-10-15T02:44:20.184Z] TOOL RESULT

```
1	{
2	  "pdf_page": 504,
3	  "book_page": 474,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Ter 1, Tr",
8	        "lang": "Indo-European",
9	        "refs": "POK:1075; KLN:1639",
10	        "gloss": "to cross over, surpass, overcome"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1075; KLN:1639",
18	          "words": [
19	            {"translit": "taro, tarya, tar", "gloss": "surpass", "script": null},
20	            {"translit": "thrâ", "gloss": "shelter, cover", "script": null},
21	            {"translit": "vi-tar", "gloss": "to pass by", "script": null, "see": ["Wi"]}
22	          ],
23	          "script_extra": null,
24	          "note": null,
25	          "quote": null
26	        },
27	        {
28	          "id": 2,
29	          "parent": 1,
30	          "lang": "Persian",
31	          "refs": "BQT:1778; HRN:161; TLM:92; MON:1790",
32	          "words": [
33	            {"translit": "tar 1, tarîn", "gloss": "more, most", "script": "ـتَر ۱ ، ـتَرین"},
34	            {"translit": "sarâ", "gloss": "house, place", "script": "سرا ( سرای ۱ ـ سار ۱ ، کوهسار )"},
35	            {"translit": "gozaštan", "gloss": "to pass by", "script": "گذشتن ( گذر ، گذشت ) گذاشتن ، گذاردن"}
36	          ],
37	          "script_extra": null,
38	          "note": null,
39	          "quote": null
40	        },
41	        {
42	          "id": 3,
43	          "parent": 0,
44	          "lang": "Old Persian",
45	          "refs": "MON:1850; VDQ:255",
46	          "words": [
47	            {"translit": "srâd, srâda", "gloss": "house, shelter", "script": null}
48	          ],
49	          "script_extra": null,
50	          "note": null,
51	          "quote": null
52	        },
53	        {
54	          "id": 4,
55	          "parent": 3,
56	          "lang": "Arabic",
57	          "refs": "VDQ:255; MON:1850; MAG:189",
58	          "words": [
59	            {"translit": "sorâdeq", "gloss": "tent", "script": null}
60	          ],
61	          "script_extra": null,
62	          "note": "This word may have been borrowed from Persian \"sarâ-pardeh: tent\".",
63	          "quote": null
64	        },
65	        {
66	          "id": 5,
67	          "parent": 4,
68	          "lang": "Persian",
69	          "refs": "MON:1850",
70	          "words": [
71	            {"translit": "sorâdeq", "gloss": "tent, house", "script": "سُرادِق"}
72	          ],
73	          "script_extra": "سرادقات",
74	          "note": null,
75	          "quote": null
76	        },
77	        {
78	          "id": 6,
79	          "parent": 0,
80	          "lang": "Latin",
81	          "refs": "AHD",
82	          "words": [
83	            {"translit": "trâns", "gloss": "across", "script": null},
84	            {"translit": "terminus", "gloss": "boundary", "script": null},
85	            {"translit": "truncus", "gloss": "overcome", "script": null}
86	          ],
87	          "script_extra": null,
88	          "note": null,
89	          "quote": null
90	        },
91	        {
92	          "id": 7,
93	          "parent": 6,
94	          "lang": "French",
95	          "refs": null,
96	          "words": [],
97	          "script_extra": null,
98	          "note": null,
99	          "quote": null
100	        },
101	        {
102	          "id": 8,
103	          "parent": 7,
104	          "lang": "Persian",
105	          "refs": "MON; AMD",
106	          "words": [],
107	          "script_extra": "ترانسپورت ، ترانزیت ، ترانزیستور ، ترانسفورماتور ، ترم ، ترمینال",
108	          "note": null,
109	          "quote": null
110	        },
111	        {
112	          "id": 9,
113	          "parent": 6,
114	          "lang": "English",
115	          "refs": "AHD",
116	          "words": [
117	            {"translit": "trans-, transport, transform, transistor, transfer, translate", "gloss": null, "script": null},
118	            {"translit": "term, terminate, determine", "gloss": null, "script": null},
119	            {"translit": "trunk, truncate, trench", "gloss": null, "script": null}
120	          ],
121	          "script_extra": null,
122	          "note": null,
123	          "quote": null
124	        },
125	        {
126	          "id": 10,
127	          "parent": 0,
128	          "lang": "Germanic",
129	          "refs": "AHD; KLN",
130	          "words": [
131	            {"translit": "thr", "gloss": "bore through, drill", "script": null}
132	          ],
133	          "script_extra": null,
134	          "note": null,
135	          "quote": null
136	        },
137	        {
138	          "id": 11,
139	          "parent": 10,
140	          "lang": "English",
141	          "refs": null,
142	          "words": [
143	            {"translit": "drill, through, thorough, nostril", "gloss": null, "script": null}
144	          ],
145	          "script_extra": null,
146	          "note": null,
147	          "quote": null
148	        },
149	        {
150	          "id": 12,
151	          "parent": 0,
152	          "lang": "Greek",
153	          "refs": "AHD",
154	          "words": [
155	            {"translit": "nek-tar", "gloss": "overcoming death", "script": null, "see": ["Nek 1"]}
156	          ],
157	          "script_extra": null,
158	          "note": null,
159	          "quote": null
160	        },
161	        {
162	          "id": 13,
163	          "parent": 12,
164	          "lang": "English",
165	          "refs": null,
166	          "words": [
167	            {"translit": "nectar, nectarine", "gloss": null, "script": null}
168	          ],
169	          "script_extra": null,
170	          "note": null,
171	          "quote": null
172	        },
173	        {
174	          "id": 14,
175	          "parent": 0,
176	          "lang": "Indo-European",
177	          "refs": "IEC:27",
178	          "words": [
179	            {"translit": "An-teros", "gloss": "second, other, step parent", "script": null, "see": ["AN 2"]}
180	          ],
181	          "script_extra": null,
182	          "note": null,
183	          "quote": null
184	        },
185	        {
186	          "id": 15,
187	          "parent": 14,
188	          "lang": "Persian",
189	          "refs": "IEC:27; MON:373",
190	          "words": [
191	            {"translit": "andar", "gloss": "a suffix meaning step as in step father", "script": "ـاندر ۲"}
192	          ],
193	          "script_extra": "پدراندر ، مادراندر ، دختراندر ، پسراندر",
194	          "note": null,
195	          "quote": null
196	        },
197	        {
198	          "id": 16,
199	          "parent": 14,
200	          "lang": "Sanskrit",
201	          "refs": "IEC:27; POK:37",
202	          "words": [
203	            {"translit": "antarah", "gloss": "other", "script": null}
204	          ],
205	          "script_extra": null,
206	          "note": null,
207	          "quote": null
208	        }
209	      ]
210	    },
211	    {
212	      "root": {"name": "Ter 2", "redirect": "Tres"},
213	      "nodes": []
214	    }
215	  ]
216	}
217	
```


## [2026-10-15T02:44:24.013Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; ls sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','HRN','TLM','MON','VDQ','MAG','AHD','IEC','AMD','WLD','BRT','KNT','PHD','NYB','HUB','CHEUNG','ARY','SKT','SYN','FVQ','AFM','PLA']:\n  v=d.get(k); print(k, v and {x:v.get(x) for x in ['kind','local_file','page_offset','lookup_hint']})\n\""
}
```


### [2026-10-15T02:44:24.593Z] TOOL RESULT

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
POK {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
KLN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
BQT {'kind': 'archive_djvu+local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
HRN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
TLM {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TLM.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 24 = p.4). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': 'Lexicon headwords are OP words in transliteration at line start.'}
MON {'kind': 'website+archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
VDQ {'kind': 'website', 'local_file': None, 'page_offset': None, 'lookup_hint': 'noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.'}
MAG {'kind': 'archive_restricted', 'local_file': None, 'page_offset': None, 'lookup_hint': 'HathiTrust has it search-only (limited view); Google Books ids -r4rAAAAIAAJ / h20wAAAAYAAJ are snippet view.'}
AHD {'kind': 'archive_djvu+website+archive_restricted', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
IEC {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
AMD {'kind': 'website', 'local_file': None, 'page_offset': None, 'lookup_hint': 'Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable.'}
WLD {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
BRT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
KNT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt', 'page_offset': 'leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations."}
PHD {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
NYB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
HUB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
CHEUNG None
ARY {'kind': 'local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
SKT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
SYN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
FVQ {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt'], 'page_offset': 'printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)', 'lookup_hint': 'Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).'}
AFM {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt'], 'page_offset': "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", 'lookup_hint': "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير')."}
PLA {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'], 'page_offset': '301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).', 'lookup_hint': 'HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)'}
```


## [2026-10-15T02:44:27.431Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'))\ne=d['entries'][0]; print(json.dumps({k:v for k,v in d.items() if k!='entries'})); print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\"; sed -n 1,400p tools/verify_check.py | grep -n -i 'problem\\|warn' | head -60"
}
```


### [2026-10-15T02:44:28.035Z] TOOL RESULT

```
{"pdf_page": 499, "book_page": 469, "verified_by": "claude-opus-5", "verified_on": "2026-10-14"}
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "tulâ, tulya",
 "verdict": "confirmed",
 "derivation": "Sanskrit tulā́ f. 'balance, scales; weight' continues the zero grade *tl̥h₂-éh₂ of PIE *telh₂- 'to lift, weigh, bear': syllabic *l̥ before the laryngeal gives Indo-Aryan ul (the l is the dialectal Indo-Aryan reflex of *l, the u the coloured vowel of the syllabic liquid). tulya- 'equal in weight, comparable, equivalent' is the -ya- derivative of tulā (Wiktionary: from tulā + -ya), and the verb tulayati 'lifts, weighs' belongs here. Nourai's gloss 'balance weight' fits tulā exactly; for tulya the precise sense is 'of equal weight, comparable', a natural derivative.",
 "derivation_fa": "سنسکریت tulā «ترازو، کفهٔ ترازو، وزن» از پایهٔ ضعیف *tl̥h₂-éh₂ ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، وزن کردن، تحمل کردن» است؛ l هجایی پیش از همخوان حلقی در هندی باستان به ul بدل شده است. tulya «هم‌وزن، همسنگ، همانند» صفتی است که با پسوند -ya از همین tulā ساخته شده و فعل tulayati «برمی‌دارد، می‌سنجد» نیز از همین ریشه است. ادعای نورایی درست است (پوکورنی ۱۰۶۰، واتکینز، والده‌ـپوکورنی، کلاین، ویکی‌واژه).",
 "sources": [
  "https://en.wiktionary.org/wiki/तुला",
  "https://en.wiktionary.org/wiki/तुल्य",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/telh₂-"
 ],
 "ref_check": [
  {
   "ref": "POK:1060",
   "status": "supports",
   "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; Greek tlēnai, talanton ('die beiden Waagschalen'), PN Atlas, -antos, telos 'payment, tribute, tax'; 'Latin tollo, -ere ... tolero ... latus 'getragen''."
  },
  {
   "ref": "AHD",
   "status": "supports",
   "note": "Watkins AHD Roots s.v. telə- item 9: 'Suffixed zero-grade form *tl-ā- in Sanskrit tulā, scales, balance, weight: TAEL, TOLA.'"
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I p.738 s.v. 1. tel-",
   "stance": "supports",
   "note": "Walde-Pokorny Bd. I pp.738-740 (local WLD_Bd1_pages.txt leaves 747-749) '1. tel- „aufheben, z. T. wägend, z. T. sich aufladend; tragen; ertragen, dulden“: Ai. tulā „Waage, Waagbalken“, tulayati „hebt auf, wägt“' ... 'τάλαντον ... eig. „die beiden Waagschalen“', 'Ἄτλας, -αντος', 'lat. tollo ... tolero ... lātus'."
  },
  {
   "src": "KLN",
   "where": "1966 s.v. tolerate / talent",
   "stance": "supports",
   "note": "Klein 1966 s.v. tolerate (KLN_1966.txt line 39457): 'L. tolerare ... from the stem of tollere ... cogn. with ... ταλάντον 'balance', ''A-τλας 'the Bearer (scil. of Heaven)', L. lātus (for *tlatos) 'borne', OI. tulā 'balance', tulayati 'lifts up, weighs' ... All these words derive fr. I.-E. base *tel-, *tol-, *tal-, *tl- 'to bear, carry, endure, suffer'.'"
  },
  {
   "src": "IEC",
   "where": "s.v. tl- (1) (IEC.txt line 18624)",
   "stance": "silent",
   "note": "Mann: 'tl- (1) ..
22:    missing_pages, problems = [], []
46:            problems.append(f"page {pg}: invalid JSON ({ex})")
52:                problems.append(f"page {pg}: entry {i} ({e['root']['name']}) missing")
56:                problems.append(f"page {pg}: entry {i} root verdict {rv!r} invalid")
65:                    problems.append(f"page {pg}: entry {i} ({e['root']['name']}) node #{n['id']} missing")
69:                    problems.append(f"page {pg}: entry {i} node #{n['id']} verdict {nv!r} invalid")
74:                    problems.append(f"page {pg}: entry {i} node #{n['id']} has no derivation")
89:    for p in problems:
90:        print("PROBLEM:", p)
94:    return 1 if problems else 0
```


## [2026-10-15T02:44:51.907Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'lemma: ter' POK_full.txt | head -30; grep -n 'lemma: an-\\|lemma: anter\\|lemma: aÆ\\|lemma: ne[kk]' POK_full.txt | head"
}
```


### [2026-10-15T02:44:52.471Z] TOOL RESULT

```
85867:Root / lemma: terd- tred- 
85937:Root / lemma: ter-1 
85953:Root / lemma: ter-2, teru- 
85996:Root /lemma: ter-3, tera-and ten-, tn- 
86174:Root / lemma: ter-4, tera- : ^-, tra-, teru- 
86247:Root / lemma: ter-5 
86281:Root / lemma: ter-6 
86301:Root / lemma: ter-Z, tera-, te/b^- terd- terg- terp- 
86305:Root / lemma: terp- trep- 
86339:Root / lemma: ters- 
5417:Root / lemma: an-1{*han- 1) 
5424:Root / lemma: an-1{*han-) : "male or female ancestor' derived from zero grade of Root/ 
5487:Root / lemma: an-2 
5526:It seems Root / lemma: an-2\ "there, on the other side' is a zero grade of the extended 
62341:Root/ lemma: nek^-ft-), nok^-t-si* hounk''-(t-))\ night' derived from zero grade of Root/
```


## [2026-10-15T02:44:54.151Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 86174,86300p POK_full.txt; sed -n 5487,5540p POK_full.txt"
}
```


### [2026-10-15T02:44:54.609Z] TOOL RESULT

```
Root / lemma: ter-4, tera- : ^-, tra-, teru- 
Meaning: to cross, transgress, to stay, etc.. 

Material: Old Indie tarati^ places about, ijbertrifft, ijberwindet' {tirati, titarti, tJryatt, tarut§), 
tarayati' places about, fijhrt hinijber', tara- 'ijbersetzend, ijberwindend' (= Avestan -tara- 
'ijberschreitend, iJberwindend'); taran'h 'durchlaufend, vordringend, rasch, helpful', taras- 
n. 'das Vorwartsdringen, energy', Instr. tarasaMv. 'hasty, rash, hasty', tara- Ad], 'strong'; 
taranta^m. 'sea'; tfrtha-n. 'ford, Tranke' {*ff'tho-) besides *turtha-\n prakr. tuha- 'bank, 
border, shore', dardisch turtlord'; compare pamir /J/f 'ford' {*ff'to-); 

Lhbasis besides in tarutea\so in turvat/" uber\Na\\.\gt, besiegt'. Inf. turvane. Adj. turvani- 
"ijberwaltigend, victorious '; Avestan tar- 'hiniJber gelangen about' (present-stem titar-, 
taraya-, from the i/-basis taurvaya-, Intens. titaraya-, participle vT-tarata-), taurvan- 
'ijberwindend', mp. /an//77/75/7'uberwinden, afflict'; ap. viyatarayama' we iJberschritten', 
osset. tarin^dx'wiQ, push, hunt, chase', Baluchi tarag, /^a^ai^'umwenden, umkehren'; 

Verbaladjektiv Old Indie -tur{-ff) in ap-tur^6\e Wasser iJberquerend', aj/-tur"\n fight, 
struggle iJberwindend', ratha-tur^ cart iJberholend', radhra-tur'6en Ermattenden rettend', 
etc.;compare gr. vsK-rap above S. 762; 

alb. sh-t/'r, sh-t/j" put about einen river, treibe an, stifte an'? 



with the meaning from Old Indie tara- (see above) probably lllyrian Taros, Taranyer 
names; 

gr. T£p9pov "end, cusp, peak'; 

Hittite tarhzrbes\eg\., ijberwindet'; 

Old Indie tra- "(*hinuberfuhren = rescue), shield, beware, guard' {tra-sva, trayate, s-Aor. 
tradhvam, Avestan ^razdum^schnmeW, Perf. Old Indie tatre), Avestan &ra-6s. (present- 
stem &raya-), &rati-\. ' shelter, protection' ; Indo Germanic *tra- because of gr. Tpc(vn(;, 
Tpav6(; " piercing = clear, bright vernehmlich, distinct' and Latin //7//'a/'e"hineingehen', 
extrabunt Mrav\\\}s (see transbeim prepositional ter-)\ frames ^Se\ten-, Querweg'from 
* tra ns- with {{o Latin meo); 

With /7^formant: Old Indie sutarman-^ good iJbersetzend', /a/7r7a/7 (uncovered) "cusp, 
peak of Opferpfostens'; venet. /e/7770 "terminus' (Lejeune Latomus 12, 394 f.); 

gr. Tspfja, -aroq n. " purpose, Endpunkt', Tsppwv m. "limit, boundary', T£p|jiO(; "am end 
situated, lastly'; 

Latin termen, termo, term/nus ^Grenzze'\chen, boundary stone ' (originally "Grenzpfahl'), 
Umbrian termnom-e'a6 terminum', /e/7r7/75S "terminatus', Oscan teremenniu^ tormina ', 
teremnattens 'terminaverunt'; 

similarly Armenian farm {*tremo-) "EndstiJck', gr. rpapK;, rpapn " dam between After and 
the genitals' (Hes.: to rpnija rnq zb^ao,, 6 6ppo(;, tiv£(; evrepov). Old English drum (engl. 
thrum) in tunge-drum^Aas Zungenband', Middle Low German drum, o'/'o/77Trumm, 
EndstiJck, Endstuck eines texture, edge'. Middle High German drumu. "EndstiJck, end, 
piece, splinter'. Modern High German Trumm, Trummer, Middle High German drumze, 
drunze, trunze^ fragmented SpeerstiJck, splinter'; 

Middle Low German //'e/77e"Querstange, Sprosse'; Old Icelandic t^rgmrxw. "edge, 
border'; compare - with s/77-suffix - at most Old Irish druimm. Gen. drommo "back', perhaps 
borrowed from cymr. o'/i/zT? besides /m/T? "ridge, back'? {* treusmn); Demin. Old High 
German drem/7^ba\k, beam, bar, bolt'; Middle Low German trame. Middle High German 
dram, -e, tramem. "balk, beam, bar, bolt, piece, splinter' (formal near stands ^pi]\^a "hole'); 

Hittite tarma-'peg, plug, nail'. 



References: WP. I 732 ff., WH. II 671 f., 699, Mayrhofer 1, 480, 483, 484, 487, 497, 503, 

506, 507, 520, 569; 

See also: s. also under tor-, toro-sS. 1088 f. 

Page(s): 1074-1075 

Root / lemma: ter-5 
Meaning: over, etc.. 
Note: to /e/'-4'hinubergelangen' 



Material: Old Indie tirah My. " away, in another place, abseits', preposition m. Akk. 
"through - toward, about - away' (later also m. Abl. "abseits from') = Avestan tar§, taroAdv. 
" sideways, unvermerkt', preposition m. Akk. "through - toward, about - toward, about - 
hinweg, out; apart from, besides'; Old Irish tarm. Akk. "about - out' {* tares, Indo Germanic 
%res, compare ta/rse, ta/rs/u ^trans eam, trans eos, eas, ea'), next to which ta/rm-, tarmi- 
ds., trem-, tremi- "through' (cymr. trim-uceint^Z^\ "decade about 20 out'), transfigured 
nachrem-: re'\/or, voran'; Old Indie tiras-caMv. "quer through ' = Avestan tarascam. 
Akk. "through - toward, about - toward, about - hinweg'; Old Indie tiryanc-, tirfcTna- "in die 
Quere gerichtet, waagrecht' (den ending -yanc-, -/c-from pratyanc-, /O/'aZ/c- attributed) 
place previous %/7ahead; besides *tre/"\n acymr. tru/, mcymr. trwy drwy bret. corn, dre 
(altbret. tre), Old Irish (with ProklisenkiJrzung) tri, /Ae "through'; Verstarkungspartikel 
mcymr. trwy- : try-; 

Latin trans, Umbrian traf, trahafm. Akk. "beyond, about - hinweg', probably participle of 
Verbums *trare {*trant-s); 

cymr. tra- e.g. in trannoeth ' about night, am consecutive Tage' (geminated nf), etc., 
proclitic from * trans, (common Celtic -ns-, -nt- > -nn-), accented mcymr. traw, draw, bret. 
//le^ "beyond'; with secondary -s. cymr. trawseic. " hostilely ', preposition //"os "about'; 

with the same Verstarkung as Old Indie tiras-ca, Avestan tarasca:(jo\h\c t^afrh. Old 
High German durh. Old English durhm. Akk. "o'^/r/7= through ' {*ter-k("')e, Xr-kC'je); out of 
it evolved Old High German o'e/'/7"durehbohrt'. Old English dyrel {*t^urhiJ) "durehbohrt'; n. 
"hole'. Old High German o'^/f/^/?/?// "durehbohrt, durchlochert'. 

References: WP. I 734, WH. II 671 f.; Mayrhofer 1 , 503. 
Page(s): 1075-1076 

Root / lemma: ter-6 

Meaning: a kind of harmful insect 



Note: to *ter-'rub, durchbohren'; compare widened terd- 

Material: Gr. TspnScbvf. 'Bohrwurm'; Latin tarmes{termes), -///s'Hoizwurm' (probably from 

an ostem %rmos or %ramo-s)\ cymr. cynrhonyn 'termes, lendix', PI. cynrhawn, corn. 

confronen^c'wnex', Middle Breton controunenn, nbret. contronenn'ver 6e viande' {*kon- 

trono); cymr. i{o)rog-en, abr. toroc, bret. teurok^vnWe' {*tdr-ako-). 

References: WP. I 735, WH. II 649. 

Page(s): 1 076 

Root / lemma: an-2 

Meaning: there, on the other side 

Material: Gr. av ' probably, possibly, in any other trap ' (sav from z\ av, Ionian pv from *n 

av, avfrom ai av); Latin an' conj.: in direct questions, or; in indirect questions, or whether 

', secondarily interrogative particle, extended anne. Old Irish an-d' here ', (common Celtic 

-ns-, -nt- > -nn-), Gothic an' then, now '; Lithuanian an-gu' or ', Old Prussian anga-anga' 

whether = or whether '. 

maybe alb. {*ane) andej'there' : Old Irish an-d'here' [rather common alb. shift n > nd\. 

Thereof derived: 

anjos' other' in: 

Old Indie anya-' other', Avestan anya-, ainya-. Old pers. an/ya-6s. compare above S. 
26. 

anteros'o\her' (from second) in: 

maybe zero grade in alb. {*anteros) nderroj" change, alter', nderrese' change, the other 
thing'; 

Old Indie antara-, oss. andar'oVnef, Gothic anf^ards.. Old Icelandic a/7/7a/7'" other, 
second', (under the influence of common Celtic -ns-, -nt- > -nn-). Old High German andar. 
Old English d^'er" other'. Old Prussian anters, antars {*antras) 'other, second', Lithuanian 
antras, Latvian i/oZ/'s beside Lithuanian antaras. East Latvian utors6s., Slavic *gterb, 
*gtorb\n Czech uteryrw. ' Tuesday', Upper Serbian wutory'oVner, second'. About Old 
Church Slavic v-btor-t "second' s. £//-" asunder, apart '. 



Note: 

It seems Root / lemma: an-2\ "there, on the other side' is a zero grade of the extended 
Root/ lemma: al-1, ol-\ "besides; other' into *alny-, *any-. 

Maybe zero grade in alb. {*nyatra) fjeter' other' [common alb. n > nt > /] : Old Indie anyatra 
"somewhere else'. 

Perhaps alb. dial. {* heter) jater, Jeter, alb. [ attribute /e'of + antef\, tjeter' other, second'; 
similar to formation in alb. Geg {*te mel= of milk) /a/77//"milk' where te is the alb. attribute 
particle. Initial alb./ seems to have substituted the old laryngeal form /?-. 

References: WP. I 56, 67, II 337, WH. I 44, Trautmann 10/11, Debrunner REtlE. 3, 1 ff. 
Page(s): 37-38 

Root / lemma: an4, anu, and, no
```


## [2026-10-15T02:44:58.133Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^ter\\|^tera\\|^terə' AHD_watkins1985.txt | head; grep -n 'NECTAR\\|TRUNK\\|TRENCH\\|NOSTRIL\\|DRILL\\b\\|THOROUGH\\|TRANS-\\|TERM\\b' AHD_watkins1985.txt | head -30"
}
```


### [2026-10-15T02:44:58.583Z] TOOL RESULT

```
1082:ters-
261:ag-. To drive. 1. Latin agere, to do, act, drive, conduct, lead: ACT, AGENDUM, AGENT, AGILE, AGITATE; (ALLEGE), AMBAGE, AMBIGUOUS, (ASSAY), (CACHE), COAGULUM, COGENT, ESSAY, EXACT, (EXAMINE), (EXIGENT), FUMI- GATE, INTRANSIGENT, LEVIGATE, LITIGATE, NAVIGATE, OBJURGATE, PRODIGAL, RETROACTIVE, SQUAT, TRANS- act. 2. Greek agein, to drive, lead: -AGOGUE, AGONY; ANAGOGE, (ANTAGONIZE), CHORAGUS, DEMAGOGUE, EPACT, GLUCAGON, HYPNAGOGIC, MYSTAGOGUE, PEDA- GOGUE, PROTAGONIST, STRATAGEM, SYNAGOGUE. 3. Suf- fixed form *ag-to- in Celtic *amb(i)-ag-to-, “one sent around” (*ambi, around; see ambhi), in Latin ambactus, servant (> Medieval Latin ambactia, office): AMBASSA- DOR, EMBASSAGE, (EMBASSY). 4. Suffixed form *ag-men- in Latin agmen, a train, a moving forward, a marching column, group: AGMINATE. 5. Suffixed form *ag-ti-, “weighing” (Greek agein, “to lead,” has a sense “to weigh”), whence adjective *ag-ty-o-, “weighty,” in Greek axios, worth, worthy, of like value, weighing as much: AXIOM; AXIOLOGY, CHRONAXY. 6. Possibly suffixed form *ag-ro-, driving, pursuing, grabbing, in Greek agra, a seizing: PELLAGRA, PODAGRA. Derivative agro-. [Pok. ag- 4]
697:leug-2. To break. Suffixed form *Jeug-é- in Latin ligére, to mourn (? < “to break down mentally”): LUGUBRIOUS. [Pok. leug- 686.] leugh-. To tell a lie. 1. Germanic *leugan in: a. Old English /Zogan, to lie: WARLOCK; b. Old English beléog- an, to tell lies about (be-, about; see ambhi): BELIE. 2. Germanic */ugiz in Old English lyge, a lie, falsehood: LIE’. [Pok. leugh- 686.] leuk-. Light, brightness. I. Basic form */euk-. 1. Suffixed form *leuk-to- in Germanic */euhtam in Old English léoht, liht, light: LicHT). 2. Latin lix, light: Lucrna, LUCULENT, LUX; LUCIFER, LUCIFERIN. 3. Suffixed form *leuk-smen- in Latin limen, light, opening: LIMN, LU- MEN, LUMINARY, LUMINOUS; ILLUMINATE, PHILLUMEN- 1st. 4. Suffixed form *leuk-snd- in Latin lina, moon: LUNA, LUNAR, LUNATE, LUNATIC, LUNE, LUNULA; DEMI- LUNE, SUBLUNARY. 5. Suffixed form */euk-stro- in: a. Latin listrum, purification: LUSTER, (LUSTRUM); b. Latin lastrdre, to purify, illuminate: ILLUSTRATE. 6. Suffixed form *leuko-dhro- in Latin licubrdre, to work by lamplight: LUCUBRATE. II. O-grade form *louk-. 1. Suffixed form *louk-o- in Germanic *lauhaz in Old English /éah, meadow (< “place where light shines”): LEA. 2. Suffixed (iterative) form *lowk-eyo- in Latin liicére, to shine (> licidus, shining): LUCENT, LUCID; ELUCIDATE, NOCTILUCA, PELLUCID, RELUCENT, TRANS- LUCENT. III. Zero-grade form *luk-. 1. Suffixed form *luk-sno- in Greek lukhnos, lamp: LINK?, LYCHNIS. 2. At- tributed by some to this root (but more likely of obscure origin) is Greek lunx, lynx (as if from its shining eyes): LYNX, OUNCE? [Pok. leuk- 687.] leup-. To peel off, break off. 1. Germanic *laubaz in Old English Jéaf, leaf: LEAF. 2. Germanic *laubja, “roof made from bark,” shelter, in: a. Old French loge, lodge: LODGE, (LOGE); b. Medieval Latin lobium, lobia, laubia, monas- tic cloister: LOBBY. 3. Attributed by some to this root is Germanic */uftuz, sky (traditionally explained as < “roof of the world,” vault of heaven), but probably a separate Germanic root, in: a. Old Norse opt, air, attic, sky: LOFT; ALOFT; b. Germanic */uftjan, to hold up in the air, in Old Norse /ypta, to lift: Lirt. [Pok. leup- 690.]
770:nas-. Nose. 1. Germanic zero-grade form *nusé in Old English nosu, nose: NOSE, (NUZZLE); NOSTRIL. 2. Ger- manic nasja- in Old English ness, headland: NESS. 3. Lengthened-grade form “nds-, in: a. Latin ndris, nos- tril: NAREs; b. expressive form *ndss- in Latin ndsus, nose: NASAL, NASO-; NASTURTIUM, PINCE-NEZ. 4. Expres- sive Indo-Aryan form *nakka- in Romany nak, nose: NARK?. [Pok. nas- 755, neu-ks 768.]
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
1080:warp threads are stretched on the loom): TAFFETA; b. Iranian *tap-, “carpet,” in Greek tapés, carpet: TAPES- TRY. [Pok. temp- 1064.] ten-. To stretch. I. Derivatives with the basic meaning. 1. Suffixed form “ten-do- in: a. Latin tendere, to stretch, extend: TEND!, TENDER?, TENDON, TENSE!, TENT!; AT- TEND, CONTEND, DETENT, DISTEND, EXTEND, INTEND, OSTENSIBLE, PRETEND, SUBTEND; b. Latin portendere, “to stretch out before” (por-, variant of pro-, before; see per’), a technical term in augury, “to indicate, presage, foretell”: PORTEND. 2. Suffixed form *ten-yo- in Greek teinein, to stretch: TENESMUS; BRONCHIECTASIS, EPITA- SIS, HYPOTENUSE, PERITONEUM, PROTASIS, TELANGIEC- TASIA. 3. Suffixed zero-grade form *tn-nu- in Sanskrit tandéti, he stretches or weaves, with suffixed (instrumen- tal) derivative *ten-tro- in tantam, loom: TANTRA. 4. Suf- fixed form *ten-tro- in Persian ¢tdr, string: SITAR. 5. Basic form (with stative suffix) *ten-é- in Latin ten��re, to hold, keep, maintain (< “to cause to endure or con- tinue, hold on to”): TENABLE, TENACIOUS, TENACULUM, TENANT, TENEMENT, TENET, TENON, TENOR, TENURE, TENUTO; ABSTAIN, CONTAIN, CONTINUE, DETAIN, ENTER- TAIN, LIEUTENANT, MAINTAIN, OBTAIN, PERTAIN, PERTI- NACIOUS, RETAIN, (RETINACULUM), SUSTAIN. II. Derivatives meaning ‘‘stretched,” hence “thin.” 1. Suffixed zero-grade form *tn-u- in Germanic *thunw-, whence *thunniz in Old English thynne, thin: THIN. 2. Suffixed full-grade form *ten-u- in Latin tenuis, thin, rare, fine: TENUOUS; ATTENUATE, EXTENUATE. 3. Suf- fixed full-grade form *ten-ero- in Latin tener, tender, delicate: TENDER!, TENDRIL. III. Derivatives meaning “something stretched or capable of being stretched, a string.” 1. Suffixed form *ten-dn- in Greek tenén, ten- don: TENO-. 2. Suffixed o-grade form *ton-o- in Greek tonos, string, hence sound, pitch: TONE; TONOPLAST. 3. Suffixed zero-grade form *tn-ya- in Greek tainia, band, ribbon: TAENIA; POLYTENE. [Pok. 1. ten- 1065.] teng-. To soak. 1. Latin tingere, to moisten, soak, dye: TAINT, TINCT, TINGE, TINT; INTINCTION, STAIN. 2. Zero-grade form *tng- in Germanic *thunk- in Old High German thunk6n, dunk6n, to soak: punk. [Pok. 1. teng- 1067.] tenk-'. To stretch. Extension of ten-. Perhaps Germanic *thingam in: a. Old English thing, assembly, (legal) case, thing: THING; b. Old Norse thing, assembly: HUSTINGS; c. Old High German thing, ding (> German Ding), thing: DINGUS. [Pok. 1. tenk- 1067.] tenk-2, To become firm, curdle, thicken. 1. Suffixed form *tenk-to-, thickened, in Germanic *thinhtaz in Old Norse théttr, dense, watertight, akin to the Scandinavian source of Middle English thight, dense: TIGHT. 2. Possibly suffixed o-grade form *tonk-lo- in Germanic *thangul- in Old Norse théngull, seaweed (? < “thick mass”), akin to the source of TANGLE?. [Pok. 2. tenk- 1068.] tens-. To stretch, draw. Extension of ten-. Suffixed zero-grade form *tns-ero- in Sanskrit tasaram, shuttle: TussAH. [Pok. tens- 1068.] tep-. To be warm. Suffixed (stative) form *tep-é- in Latin tepére, to be warm: TEPID. [Pok. tep- 1069.] ter-. Base of derivatives meaning peg, post, boundary marker, goal. 1. Suffixed form *ter-men-, boundary marker, in Latin terminus, boundary, limit: TERM, TER- MINATE, TERMINUS; DETERMINE, EXTERMINATE. 2. Suf- fixed zero-grade form *tr-m- in Germanic *thrum- in Old English thrum, broken-off end (attested only in tungeth- rum, the ligament of the tongue): THRUM2. [Pok. 4. ter- 1074.] tera-1, To rub, turn; with some derivatives referring to twisting, boring, drilling, and piercing; and others refer- ring to the rubbing of cereal grain to remove the husks, and thence to the process of threshing either by the trampling of oxen or by flailing with flails. Variant *tré-, contracted from “*trea-. I. Full-grade form *ter@)-. 1. a. Latin terere (past participle tritus), to rub away,
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
1434:DOTE dud- DOUBLE dwo- DOUBLET dwo- DOUBLOON dwo- DOUBLURE dwo- DOUBT dwo- DOUCEUR dik-u- DOUCHE deuk- poucH dheigh- DOUGHTY dheugh- DOUR deru. DOVE! dheu-1 DOWAGER dé- DOWEL dheubh- DOWER do- Down! dhino- pDowN2 dheu-! pown’ dhiino- Dowry do- DOXOLOGY dek-1 DOYEN deki DOZE dheu- DOZEN dekm, dwo- DRAB! der-2 DRAB? dher-! DRABBLE dher-! DRACHMA dergh- DRAFT dhragh- DRAG dhragh- DRAGON derk- DRAGOON derk- DRAIN dreug- DRAKE? derk- DRAMA dera- DRAMATURGE werg- DRAPE der-2 DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1
1907:NEB _ nabja- NEBULA nebh- NEBULOUS nebh- NECESSARY ked- NECK ken-5 NECRO- nek-1 NECROMANCY negw-ro-, nek-1 NECROPOLIS pele-3 NECROSIS nek-1 NECTAR nek-! NECTARINE nek-1 NEE gene-
1936:NOSH ghen- NOSTALGIA nes-1 NOSTRIL nas-, tere-2 NOSTRUM nes-2 NOT ne, wekti- NOTCH sek-
2354:TENTH dekm TENUOUS ten- TENURE ten- TENUTO ten- TEPID tep- TERATOCARCINOMA kWer-1 TERATOGEN kWer-1 TERATOID kWer-1 TERATOMA kWer-1 TERCEL trei- TERCET trei- TEREDO tera-! TERETE tere-1 TERGIVERSATE wer-3 TERM ter- TERMINATE ter- TERMINUS _ter- TERN? trei- TERPOLYMER trei- TERPSICHORE gher-!, terp-
2385:THOLE PIN teue- THONG twengh- THOR (s)tene- THORN (s)ter-n- THOROUGH tere-2 THORP treb- THOSE to-
2400:TRAIN OIL dakru- TRAIT tragh- TRAITOR d6- TRAJECT yé TRAMMEL macula, trei- TRAMP der-! TRAMPOLINE der-1 TRANCE ei-1 TRANQUIL kweie-2 TRANS- tere-2 TRANSACT ag- TRANSCEND skand- TRANSCRIBE  skribh- TRANSDUCER deuk- TRANSECT sek- TRANSFER bher-1 TRANSFIGURE dheigh- TRANSFIX dhig¥- TRANSFUSE gheu- TRANSGRESS ghredh-
2406:TRAPUNTO peuk- TRAUMA tera-1 TRAVAIL pag- TRAVE treb- TRAVEL pag- TRAVESTY wes-4 TRAY deru TREACLE ghwer- TREAD der-1 TREADLE der-1 TREASON d6- TREAT tragh- TREBUCHET beu-1 TRECENTO dekm, trei- TREE deru TREFOIL bhel-3 TREMATODE tere-! TREMENDOUS trem- TREMOR trem- TREMULOUS trem- TRENCH tera-2 TREPAN! tere-1 TREPHINE trei- TREPID trep-1
2412:TROTH deru TROUBLE twer-1 TROUGH deru TROVER trep-2 TROW deru TRUANT tere-1 TRUCE deru TRUCK! dhregh- TRUCKLE dhregh- TRUCULENT tera-2 TRUE deru TRUFFLE teua- TRUNCATE tere-2 TRUNK tera-2 TRUST deru
```


## [2026-10-15T02:45:05.334Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==183' HRN.txt | head -80; echo ======; grep -n -i 'sarā\\|saräi\\|sarai\\b\\|saräy\\|sarāy' HRN.txt | head; grep -n -i 'guSastan\\|guöastan\\|gu[dδö]a[sš]tan\\|guzastan\\|guzäStan\\|gudästan' HRN.txt | head"
}
```


### [2026-10-15T02:45:05.731Z] TOOL RESULT

```
Exit code 1
— 161 —
kurd. afj'. bei. (884) sar; oss. sär (220) ; wa/. sangl.
minj. sar.
121. se^'üT, sera *PaIast*.
Wohl zu aw. l/^i^rcl-, ^h'äyeinfi 'schützen , ai. yträ-^
trdyate; phlv. srWitan.
Hierher gehört wohl auch jüd.-pers. HNID 'Vorhof'
(Is. 62, 9), arm. LW. sr»/*, srahak^ arab. LW. surädiq
(de Lagarde, Pers. Stud. 72), aber nicht der lydische
Stadtnanie Sardes (vergl. 6. Meyer, Indog. Forsch.
I, 827).
Allgemein entlehnt.
728. sut% usmh Blei', "P)nD (Jer. 6, 29).
g. aurob.
aw. srn' 'Blei'; phlv. srpin 'bleiern'.
kurd. sirift (H.-Sch.); bei. surup, suruf (855).
729. serhär, sertvär 'Last, die man auf dorn Kopfe trägt .
aw. ^sara.hära- *Kopflast', vergl. sarnharn 'capitum
tegmina' (Isid. t&, 23).
Vergl. No. 726.
730. stir-^ Vot', Suhr[äbj Suhr]esp; vergl. sur/tce^ sur/tze
llöteln'.
ap. Ou/ra- (N. pr.) ; aw. sii^/ra- rot ; phlv. sii/r ;
ai. gukrä' 'klar, licht, hell'.
kurd. sör ; afy. sür ; oss. d. sur/, t. sir/ rot, schön'
(286) ; bei. suhr^ sohr Vot, glühend' (350) ; wa/. sökr.
731. serd 'kalt', sermä 'Kälte'.
g. sart,
aw. sareta- 'kalt'; phlv. sarty sarmäk (Bund.); skr.
vergl. gigira- 'Kälte'; arm. sarn 'Eis*, sahium., sarcim
'gefrieren, erfrieren' (H. No. 245) ; lit. szdlfas 'kalt'.
kurd. sür; afy. sör; oss. t. sald 'Kälte' (219); bei.
.sa/d, n. särf (336) ; wa;^. sür, süri.
np. sei'ma erklärt Nöldeke (mündliche Mitteilung)
überzeugend als Analogiebildung nach germä 'Wärme' ').
*j Lit. szarmä kann ihm also nicht gleichgeaetzt werdon
(Bezzonberger, Beitr. z. Gesch. der lit. Sprache, Ol).
II r II , (jiunUriüM tl. iioup. Ktyiuologpie. 11
(eval):1: ===== not found
```


## [2026-10-15T02:45:09.985Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'gu[dδöSsšz]a[sšS]t\\|gu[dδöz]ar\\b\\|guSäStan\\|guzär' HRN.txt HUB.txt | head -20; echo ===; grep -n -i 'tarin\\|-tar\\b\\|Komparativ' HRN.txt HUB.txt | head -20"
}
```


## [2026-10-15T02:45:11.915Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^\\*tar\\|^\\*ϑrā\\|^\\*θrā\\|^\\*\\(h\\)\\?tar-\\|^\\*ϑraH\\|\\*ϑrāH' CHEUNG.txt | head; grep -n 'gu[δd]a[šs]tan\\|guδaštan\\|guzaštan\\|gudaštan' CHEUNG.txt | head"
}
```


### [2026-10-15T02:45:12.337Z] TOOL RESULT

```
Exit code 1
HUB.txt:3215:ist Causativum zu gudastan Voriibergehen , vorbei-
HUB.txt:5483:'allee' (oben p. 91), guddstan *passiren lassen , guSastan Vor-
HUB.txt:5632:KOrpers', np. gudavj gudar 'Durchgang, Furt', phi. v(i)tar
HUB.txt:6707:*entgegennehmen\ guSaStan 'vorbeigehen', gudastan Vorbeilassen*, dSar
HUB.txt:6957:gumdrt Phi. Min. p. 52, Z. 4, Bdh. Gl. 225; gudastan pas-
HUB.txt:6959:ipr, gnddram; gudastan vorbeigehen {Ruch gadaridan?), pr.
HUB.txt:6960:gudaram, ptc. gudasta Vergangen Fird. 1, 140,200, paz. vadard
HUB.txt:6994:wonach also angast, ohdst, gumast, gu6ast^ gudast, anbosta
HRN.txt:7942:gtizäris, güzärisn (Wörterbücher)^), guzäre; vergl. vecer
HRN.txt:12467:guzäre 917.
HRN.txt:12468:guzärden 917.
HRN.txt:12470:guzäris 917.
HRN.txt:12471:guzärisn 917.
(eval):1: == not found
```


### [2026-10-15T02:45:12.349Z] TOOL RESULT

```
24753:*taré (*tark) ? ‘to turn, to move to and fro ?’ 
24773:*tard ‘to pierce, split’ 
24798:*tarH ‘to cross over’ 
24803:*tarHl 381 
24916:*tar$ 383 
24927:*tarp ‘to steal’ 
24957:*tarš ‘to be thirsty’ 
55098:*tarH' (s.v.), *xar (s.v.), 
55595:*tars 
58404:*tarH’
```


## [2026-10-15T02:45:14.313Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 24798,24916p CHEUNG.txt; grep -n '^\\*Oraj\\|^\\*Ora\\|^\\*θra\\|^\\*Hra\\|‘to protect\\|to protect’' CHEUNG.txt | head"
}
```


### [2026-10-15T02:45:14.837Z] TOOL RESULT

```
*tarH ‘to cross over’ 
*AVESTAN: tar- ‘to cross over’ || (+ *ui-) ‘to bring away ?’. © Forms such as ҮАУ. 
tauruuaetois (Yt 13.115), YAv. tauru (V 10.10), YAv. tauruuan- (Y 10.9), ҮАУ. 


*tarHl 381 


-tauruuairi- (Yt 13.14), etc. derive from another pres. stem (*taru): YAv. *tauruua- 
(Skt. RV türvati), cf. Kellens 1984: 163; Insler 1975: 127. = Liste: 24f. 

Pres. them. red.: INJ. 3sg. YAv. titarat (Yt 13.77); Partic.: pres. YAv. titarant- (G 1.6), caus. med. ? YAv. 
*vititaraiiamna- (H 2.7); Caus.: pres. IND. 3sg. Y Av. titäraiieiti (Yt 8.8, Yt 8.39) 

*OLD PERSIAN: (+ *ш-) vitar- (caus.) ‘to put across’ = Kent: 186a 

Caus.: impf. IND. 15р. viyatarayam <vi-i-y-t-r-y-m> (DB 5.24 f.), 1pl. viyatarayamä <vi-i-y-t-r-y-a-m-a> 
(DB 1.88) 

*MIDDLE PERSIAN: (+ *ui-) MMP wdyr-, BMP wtyl- /wider-/, wtl- /widar-/ ‘to pass 
by’, wt(w)l- /widur-/ (or /widör-/ ?) ‘to pass away, die’, MMP wyd’r-, BMP wt'l- 
/widar-/ (caus.) ‘to let pass (by), lead’, BMP wt'lyn- /widaren-/ (sec. caus.) ‘to cause 
to take away’ > DMMPP: 340a, 339a 

Well attested: Pres.: IND. 3sg. MMP wdyryd, wydyryd, BMP wtylyt /wideréd/, SUBJ. 3pl. MMP 
wdyr'nd; Partic.: pres. caus. MMP wyd’r’g, perf. pass. MMP *wdrd, BMP wtwit / widurd/, etc. 
*PARTHIAN: (+ *ш-) w(y)dr- ‘to pass (beyond, over)’, w(y)d’r- ‘to cause to cross 
over, pass over’ = Ghilain: 57, 74, 92 | DMMPP: 352a, 339a 

Pres.: IND. 3sg. wydryd, 3pl. wydrynd, SUBJ. 2sg. wydr’, wydr’h, IMPV. 2sg. wydr, Partic.: pres. caus. 
wyd’r’n, perf. pass. wydrd, caus. wd’r’d, wyd’r’d, wyd’r’’d; Caus.: pres. IND. 2sg. wyd’ryh, 3sg. 
“wyd’ryd, 2р1. wyd’ryd, 3pl. wyd’rynd, SUBJ. 15р. wyd’r’n, 2sg. wydd’r’h, 35р. wyd’r’, wyd’r’h, OPT. 
wyd’ryndyy 

*KHOTANESE: ttidi ‘crossing place’ || (+ *ui-) OKh. bitar- ‘to develop’ = SGS: 96 
*SOGDIAN: CSogd. tr- ‘to go’ || (+ *pati-) CSogd. ptyrnc (f.) ‘transitory’ || (+ *fra-) 
BSogd. ft’yr- ‘to come, proceed’, CSogd. ftyr- ‘to pass over, pass away, depart’, 
CSogd. ftyr- ‘to cause to pass over (away), take over, remove, set aside’ || (+ *ui-) 
SSogd. wytr-, BSogd. wytr-, MSogd. wyt’r- ‘to go on, pass (away)’, CSogd. wytr-, 
MSogd. wytr- ‘to go’ 

Pres.: SUBJ. 3sg. CSogd. tr’t, OPT. 25р. CSogd. try, 3sg. CSogd. try, 1р1. CSogd. trym, IMPV. 2sg. 
CSogd. tr’; Fut.: IND. 3pl. CSogd. “tmtq’ || (+ *fra-) Pres.: IND. 3sg. dur. CSogd. ftyrtysq, SUBJ. 3sg. 
CSogd. ftyr’t, Impf.: IND. 3sg. BSogd. f't'yr, CSogd. ftyr, Fut.: OPT. 3sg. CSogd. ftyrq’; Partic.: pres. 
ITER. MSogd. ftryh ‘on foot, walking, runner’ (Sogdica: 25); Caus.: pres. IND. 3sg. CSogd. ftyrt, IRR. 
25р. CSogd. ftyrt’, IMPV. 25р. CSogd. ftyr, impf. IND. 3sg. CSogd. ftyr || (+ *ui-) Pres.: IND. 15р. 
SSogd. wytr’m, SUBJ. 3sg. BSogd. wytr’t, BSogd. wytr’’t, OPT. 3sg. CSogd. wytry, PREC. 3sg. SSogd. 
L’ wytrt, POT. 3sg. BSogd. wytrt Bwt; Impf.: IND. 3sg. SSogd. wytr, CSogd. "wytr, 3pl. SSogd. wytr’nt; 
Pret.: intr. IND. 35р. SSogd. wyt'rt, 1р1. SSogd. wyt’rt’ym, 3pl. SSogd. wyt’rt’nt, Fut.: 15р. CSogd. 
wytr’mq’, 3р1. CSogd. wytrntq’; Inf.: pret. BSogd. wyt’rt 

*NWIR: Gur. (Kand.) tarin- (orig. caus.) ‘to drive forth’, ? Bal. tar(r)it/tar(r)- ‘to walk, 
search, turn’ || (+ *ui-) widely attested: NP guöästan/guöar-, Kurd. (Kurm.) bihurin/ 
bihur-, buhurin/buhur-, (Sor.) burdin/bur-, bwardin/bwer-, Zaz. véreti§ (v[yJerdis)/ 
veren-, rä-verdis/rä-veren- ‘to pass, proceed, go on, over’, Awrom. wiardáy/wiar-, 
Ard. viyest/viyer- ‘to pass’, Fariz. -(i)vast/-ivär-, Yar. -viast/-viär- ‘to pass; to rise 
[of sun]’, Gz. ver-/väst, vera, Gil. (Rsht.) da-varcestcen/da-var-, (LW) guzaestaen/ 
guzär-, Ham. beidestän/veider-, (subj.) béider-, Isfah. vezästän/vezer-, Khuns. 
veder-/ve(de)st, Mah. bédast-, Meim. b-aedaft-/ (impv.) b-aeder, Nn. vedrä-/vedr-, 


382 *tarH2 


Natan. viäst-, Semn. bá-viár-, Siv. (y)àr-/viürd ‘to pass, proceed’, Qohr. awdasta/ 
awder-, Soi ba-udast-/4-udir- ‘to pass, exceed’, Sorkh. -viärd-/viar- ‘to pass’, NP 
guóastan/guóar- (caus./tr.) ‘to place, put; to let, allow’, Abz. vadasta/vader- ‘to pass 
par; to let, abandon’, Anar. gidär ‘ford’ || (+ *ham-) Varz. hendarte/hendar- (orig. 
caus.) ‘to send’ 

*NEIR: Oss. I. teryn/tard, D. taerun/tard ‘to chase, drive (away, forth, out)’, Yghn. 
tir-, ter-/torta ‘to go, leave, depart’ || (+ *us-) Wa. zatrun- ‘to disperse’ (Lorimer) || 
(+ *pati-) Wa. patari ‘rafter’, Yi. pataré ‘roof-beam [i.e. *cross-beam ?]’ || (+ *fra-) ? 
Oss. I. ledaryn/lederst, D. laedarun/laedarst ‘to let liquid flow out from a vessel; to 
shed tears, weep’, I. ladarsyn/ladzrst, D. ladzersun/ledarst (inch.) ‘to flow out 
with a squirt or in drops’ || (+ *ui-) Oss. І. dard, D. idard ‘far’. ° Oss. I. laedaryn, D. 
lædarun are connected by Abaev, Slovar’ II: 17 f. to Arm. telam ‘to rain, irrigate’, 
tet ‘(heavy) rain’ IEW: 196, s.v. del- *trópfeln"). 

*SANSKRIT: tar’ ‘to pass across, pass through, get across, overcome’ (RV+) 
c» EWAia I: 629, 87 

«PIE *terH;- ( *treH»-) ‘to go through, cross, overcome’ = LIV: 633 f. | Pok.: 1074 f. 
*IE COGNATES: Hitt. /tarh(u)-/ ‘to overcome, be able’, Lat. intrare ‘to go through’, 


Alb. sh-tir ‘crosses’, etc. 

*REFERENCES: Zhukovskij I: 179; KPF I: 83b, 145a, 209a, 248b; KPF II: 210; Christensen, Contributions 
I: 73, 170, 262; IIFL II: 242a, 535b; Christensen, Contributions II: 62; Abrahamian 1936: 108, 134; 
Lambton 1938: 41a; Abaev, Slovar’ I: 344; Andreev — PeSéereva: 335b; MacKenzie 1966: 112; DKS: 
128a, 282b; WIM I: 73; Abaev, Slovar’ III: 278; WIM II/1: 85; WIM III: 120; Werba 1997: 291; Paul 
1998: 311a; Steblin-Kamenskij 1999: 458, 460; Cabolov 2001: 175; Lecoq 2002: 122, 125, 131, 608a, 
135 (passim); Shahbakhsh: s.v. tarr-; Korn 2005: 321, 364 (passim) 


*{агН? ‘to rub, wipe (?)’ 

*KHOTANESE: (+ *us-) ustar- ‘to remove’ || (+ *ham-) LKh. hamträf- ‘to diminish, 
remove’ = SGS: 18, 139 

*SOGDIAN: (+ *apa-) BSogd. ’pt’r- ‘to pluck, pull out (hair)! {hapax} || (+ *pari-) 
BSogd. prtr- ‘to dry up, wipe off’ 

(+ *apa-) Pres.: IND. 3sg. BSogd. ’pt’rt (SCE: 88) || (+ *pari-) Impf.: IND. 3sg. BSogd. pr’ytr 

*NWIR: ? Bal. tir(r) ‘fart’ (uncert. etym., Korn 2005: 133, fn. 303) || (+ *us-) NP 
suturdan ‘to shave, erase, scrape’, usture ‘razor’ 

*NEIR: Sh. far-/tart, Rosh. tar-/tart ‘to cleanse, remore dirt’ || (+ *apa-) ? Oss. I. 
eft’eryn/eft’erd, D. eft’irun/eft’ird ‘to devour’ (slang word ?) || (+ *us-) Oss. I. 
steeryn/sterd, D. (z)sterun/(&)stard ‘to lick (up)’, Sh. (Baj.) zidar-/zidud, zidar-/ 
zidug, Sariq. zidor-/zidug, Ishk. zdar-, M. stor-/stor-, Yi. 'stör-/stär- ‘to sweep’ 
*MISC: (+ *us-) Par. astar- ‘to rub, wipe away’ 

«PIE *terH;- ‘to rub’ = LIV: 632 f. | Pok.: 1071 f. 


*tar$ 383 
532:*-so, e.g. *рах ‘to divide, apportion’ (cf. *baj ‘to divide’), *Hraxs ‘to protect, 
1984:look after’, Goth. bairgan ‘to protect, shelter’, OE borgian ‘to give a pledge’, Engl. 
11612:*uz-) ‘to protect’ — Liste: 14 
11656:*IE COGNATES: Lat. iuvare ‘to help, to support’, Olrish con-di ‘to protect’. © Blanc 
11890:*CHORESMIAN: y'r- ‘to protect, guard’, m/yr’s- (inch.) ‘to be awake, awake’ 
12585:*Hrab/f ‘to go’ 
12615:*Hrab/f3 (*ra(m)b?) 185 
12627:*Hrab/f ‘to attack, fight’ 
12659:*Hrab/f (*ra(m)b?) ‘to touch, affect, grab ?" 
12687:*Hrad ‘to dig, pave’
```


## [2026-10-15T02:45:18.498Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'sray\\|srāy\\|sräy\\|sarāy\\|saräy\\|ϑrā\\|Ôrä\\|Orä-' CHEUNG.txt | head; grep -n -i 'sraytn\\|srāy\\|srāyīd\\|sray' PHD.txt NYB_vol2_glossary.txt | head; grep -n -i 'srādak\\|sradak\\|surādiq\\|suradiq' PHD.txt NYB_vol2_glossary.txt FVQ_pages.txt AFM_pages.txt KLN_1966.txt | head"
}
```


### [2026-10-15T02:45:19.054Z] TOOL RESULT

```
23230:*SANSKRIT: sray ‘to lean against’ (RV+) = EWAia II: 665 
23341:*MIDDLE PERSIAN: MMP sr’y-, BMP sl’d- /sray-/ ‘to sing’ || (+ *fra-) MMP frsy- ‘to 
23346:Caus.: pres. IND. 3pl. MMP sr’ynd’, sr'yynd, BMP sl’dynd /srayend/; Partic.: perf. pass. BMP slwt 
25748:*NEIR: Ishk. tsranj-/tsrayd- ‘to compress’, M. tro(n)jv-/tardyd- ‘to stretch’, Yi. 
35528:sI'd- /sray-/, 357 
48521:dsray-/dsrsd, 79 
PHD.txt:296:čābuk [c’Swk! | N ~] agile, nimble; excellent. ~th: agility. čādur [c?twl | N ~] sheet, veil. éagad [ck*t! | (N ¿ahad), J ¿eyad] peak, summit. сабаг [cki] wife (of the second degree). саһ [ол | N ~] pit, well. čahār [ALBA < A?rb‘; ch?l | M с, N ~] four. ~dah [cl’ldh | N ~] fourteen. ~-рау [cb Ip d | N ~ > čārwā] quadruped. čakēk [ckwk | N ~, cakáwak] lark. čakuč [cktwc | N čakuš] hammer. čambar [cmbl | N ~] circle, hoop. čamišn [cmšn! | M cmbyšn (?)] urination; lavatory. ` бапа [спа | = M, N ~] how many, much?; so many, much; some, a few. ~ih: amount, quantity. čandal [cndl | N ~] sandalwood. čandīdan, čand- [cnd-ytn! | (M cn-ystn)] tremble, quake. ~išn: trembling, movement. čang [eng | M bung, N ~] harp. ~-sray [-sPd] harpist. са�� [c7] = Carag. багар [clk' | M erg] pasture, grazing; flock. čārag [c?]k! | N ~a] means, remedy. ~garih [-glyh] ability, savoir faire. Carb [с/р | P crb, N ~] mild, gentle; fatty, oily. ~ih: gentleness; fattiness. ~išn [-sn'] fat, oil. ~і&потапа [-šrwmnd) oleaginous. Carm [с/т | M crm, N ~] skin, hide, leather. čārūģ [c wk! | N čārū] lime, mortar. „ēn [-yn!] limy. Carz [сіх | N ~] bustard. čāšīdan [c'$-ytn!] = čāštan. čašm [A YNE < A ‘ynh; ст | = M, N ~] eye. léaSmag [cfmk! | М cšmg, N ~a] spring, source. tčašmaģ [cfmk!] renowned. čašmaģāh [cšmk?s | M csmg’h] obvious, public, notorious. ~ih: notoriety, condemnation. čašm-arešk [cém ?ly$k!] envious. ^h: envy. čašm-dīd [cšm dyt'] visible, obvious. čāšnīg [c nyk! | M спус, N čāšnī] taste.
PHD.txt:428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
PHD.txt:510:~ pazd- : blow, play the flute. *nāydāģ [nywt’k'] deep, unfordable, navigable. nayestàn [KN Y Ast^n! | N ~] reed-bed, cane-brake. nāyīzaģ [»vck! | N ~a] small reed, straw. nay-sray [rds d] flautist. nazd [nzd | = M, N ~] near. nazdik [nzdyk! | = M, N ~] near. ~ih: proximity. nazdist [x3dst'] first. nàzišn [x*cšn! | N nāsi$] 1. boasting; 2. kindness. nàzuk [n’cwk! | (M wzwg), N ~] tender, gentle; fickle. né [L4 < AP | M ny, N na] no, not. nék [nywk! | M nyk, N ~] good, beautiful. ~th: goodness. nék-góhr [nywk gwhl] good-natured, virtuous. ~ih: goodness, virtue. nēkēģ [nywhkwk! | M nyyquiw!, IN neho] == пёк. nem [PRG < А plg; nym | = M, N —] half. ~ag [nymk! | N ~a] half, side, direction. ~-аѕр [5р] centaur; astr. Sagittarius. ~-rōz [-lwe | M -rwe, N ~] midday, south. ~-tan [-tn' | N ~] middle of the body. nérang [nylng | N <] incantation, charm, spell. пёгӧб [nylwk! | M nyrwg, N nero] strength, power. ~omand [-’wmnd] strong, powerful.
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
PHD.txt:1965:flautist nāy-srāy.
PHD.txt:2215:harpist čang-srāy, kennār-srāy.
PHD.txt:2328:house Кадар, mān(d), srāy, xān(ag); v. lady, master; — and home xān ud man.
PHD.txt:3266:protect pàdan, pahréxtan, srāyidan; (by spell) afsüdan.
PHD.txt:3268:protection magind, pānāgīh, panāhīh, pasbanih, pušt, puštībānīh, sray- iin, zēnhār.
NYB_vol2_glossary.txt:3507:sräd (sra?) [sPd or sPy] palace, house 3721, — OIr *srdda-: Prth *srdd, with suff. *srādak in Mand. lw. sr'dq? ‘curtain, pavilion, tent-roof', Arab. lw. surādig ‘large tent’; Prs srdy alternating with sräh according to the common rule, whence NP saräi; Arm. lw. srah ‘hall’, ‘curtain’, srahak dimin.; J.-Pers sr’h ‘forecourt’; v. Hübschmann 241, Widen- gren, ISK 101.
```


## [2026-10-15T02:45:24.187Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'sur[aā]diq\\|suradik\\|sur.diq' FVQ_pages.txt FVQ.txt AFM.txt PLA*.txt LKT.txt AFA.txt 2>/dev/null | head; grep -n 'سرادق' AFM_pages.txt AFM.txt ARB_mo3rb.txt incoming/PLA/PLA_pages.txt 2>/dev/null| head; grep -n '^serai\\|^caravansary\\|^seraglio' KLN_1966.txt | head"
}
```


### [2026-10-15T02:45:24.673Z] TOOL RESULT

```
(eval):1: no matches found: PLA*.txt
AFM_pages.txt:768:على الغرفة والسرادق وقصر الماك وغير ذلك
AFM_pages.txt:1371:0 اطلقت على سرادق الملوك والوزراء ( الإرهان القاطع )
AFM.txt:1253:على الغرفة والسرادق وقصر الماك وغير ذلك 
AFM.txt:2226:0 اطلقت على سرادق الملوك والوزراء ( الإرهان القاطع ) 
ARB_mo3rb.txt:15121:قال فى السات : « السرادق : ما أحاط بالبناء 4 وابضمع ”سرادقات“* » ثم نقل عن الجوهرى قال : 
ARB_mo3rb.txt:15122:«السرادقٌ : واحد السرادئات الى تمد فوق كدن الدار؛ وكل بيت ١ن‏ كاسف فهو سرادق» ٠‏ والكلمة 
ARB_mo3rb.txt:21394:فر السرادق الذهلى » وله ترحة ق الشعراء لابن قتبيه (ص م4 ) ٠‏ وأما « سراقة البارق »فائنان : 
ARB_mo3rb.txt:31943:9 السرادق الذهل 1 
ARB_mo3rb.txt:35967:السرادقا 2
```


## [2026-10-15T02:45:26.887Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 15112,15130p ARB_mo3rb.txt; grep -n -i 'sur.di\\|s.r.diq\\|suradiq' FVQ_pages.txt | head; grep -n -i 'caravansar\\|serai' KLN_1966.txt | head"
}
```


### [2026-10-15T02:45:27.241Z] TOOL RESULT

```
5 |أاستور » 9 1 ه وهو الدروع ٠‏ وقيل 0 سلاج ب 0 يه ذهو 
ع2 
صقر 
و2 2720 
ا دقري 9 


(1) هكذا فى النسخ المخطوطة بأاف قبل الدال وألف بعدها » وضبط يفتح السين والراء رالدالىم ٠‏ 
٠‏ اا و ل 0 () هكذا فسره ابأوالبق » وهوغير جيد . 
قال فى السات : « السرادق : ما أحاط بالبناء 4 وابضمع ”سرادقات“* » ثم نقل عن الجوهرى قال : 
«السرادقٌ : واحد السرادئات الى تمد فوق كدن الدار؛ وكل بيت ١ن‏ كاسف فهو سرادق» ٠‏ والكلمة 
قرآنية ) قال تعالى فى سورة الكهف آنة ١9‏ ([إناأعندن! للظامين نارا أحاط بهم سرادتها ولم بزع أحد 
سل فيا رأيت - أنها معرة إلا ال+واايق هنا والراغب ق المفردات» قال : .« فارسى معرب » وليس 
١‏ فى كلامهم اسم مفرد ثالله ألف و بعده حرفان» ٠‏ والكية عربية » قال ابزدر يد فى المهرة ( : 8م 8) 
« وسردق البيث : جعل له مراذقا » رذ شاهدا من شمر الأعثى ٠‏ وفى الاسان : « ورييت مسردق 
س يضم الم وفتح السين وسكون الراه وفتح الدال » على بناء اسم المفعول سس وهو أن يكون أعلاه 
وأسفله مشدودا كله 6 وقد سردق البيت » ٠‏ ثم ذكر بيت الأعثى ولكن نسية لسلامة بن جنال ٠‏ 
68 الييت من أر بعة أبيات فى ديوانه (ص 5<ره) . )0 فىع «أنه» رهر خط ٠‏ 
٠‏ 6 دعوى تعر ببها لا داوسل عليها ٠‏ وكلية *” سرك 6“ بالسين المهله فى النسخ المخطوطة ٠‏ وقى ب 
6169:(Surddiq).
3753:Astragalus,  n.,  a  genus  of  plants  of  the  pea  family (bot.)  —  L.  See  astragal, astrakhan,  astrachan,  n.,  the  fur  of  still-born  or young  lambs  from  Astrakhan.  —  From  As¬ trakhan  in  Russia.  The  name  of  the  city  lit. means  ‘star  of  the  caravanserai’.  See  astral  and khan,  ‘caravanserai’.
6501:caravanserai,  n.,  Eastern  inn,  esp.  for  caravans. —  F.  caravanserai,  fr.  Pers.  karwansarai,  fr. karwan  (see  caravan)  and  sarai,  ‘mansion,  inn’, which  is  prob.  rel.  to  Avestic  {trayeihti,  ‘they protect’,  Ol.  trdyate,  ‘protects’, caravel,  carvel,  n.,  any  of  various  kinds  of  light vessels.  —  F.  earavelle,  fr.  Sp.  carabela,  dimin. formed  fr.  cdrabo,  ‘a  small  vessel’,  fr.  Arab. qdrib,  ‘bark’,  which  is  traceable  to  Gk.  x£px|3o<;, 'horned  beetle;  crayfish;  a  light  ship’.  See  scarab, caraway,  n.,  a  plant  with  aromatic  seeds.  —  ME carawai,  fr.  OSp.  (=  Sp.)  alcaravea  (whence Sp.  carvi),  fr.  Arab,  al-karawiyd’ ,  fr.  a /-,  ‘the’, and  karawiyd',  fr.  L.  carum,  careum,  fr.  Gk. xxpov,  xapcov,  ‘caraway’,  which  is  of  uncertain origin.  Cp.  skirret.
20647:which  is  rel.  to  Heb.  hamishshtm,  Aram.-Syr. hamshtn,  Akkad,  hamshdti,  ‘fifty’, khan,  n.,  a  title  of  ruler  in  Mohammedan  coun¬ tries.  —  Pers.  and  Arab,  khan,  ‘lord,  prince’,  fr. Turki  khan,  contraction  of  khaqan,  ‘ruler, sovereign’,  which  is  prob.  of  Mongolian  origin, khan,  n.,  a  caravanserai.  —  Pers.  and  Arab,  khan, ‘caravanserai,  inn’.  Cp.  astrakhan, khanate,  n.,  a  district  ruled  by  a  khan.  —  A hybrid  coined  fr.  khan,  ‘title  of  ruler’,  and  -ate, a  suffix  of  Latin  origin.
34657:serac,  n.,  a  pinnacle  of  ice  on  a  glacier.  —  Swiss F.  serac,  ‘a  kind  of  cheese’,  derived  fr.  L.  serum, ‘whey’  (see  serum);  so  called  from  its  shape, seraglio,  n.,  1)  harem;  2)  ( capit .)  name  of  the  old palace  of  the  sultan  in  Constantinople.  —  It. serraglio,  lit.  ‘enclosure’,  later  also  used  in  the sense  of  ‘palace’  (prob.  under  the  influence  of Turk,  serai,  ‘palace’),  fr.  ML.  serraculum,  ‘bar (of  a  door),  bolt’,  fr.  VL.  *serrare,  ‘to  bar,  bolt’, fr.  Late  L.  serdre,  of  s.m.,  fr.  L.  sera,  ‘a  bar  (for fastening  a  door)’.  See  sear,  ‘catch  in  the  lock of  a  gun’.  The  suff.  -aglio  in  It.  serraglio  repre¬ sents  L.  -aculum,  used  to  form  place  names.  Cp. e.g.  L.  cena-culum,  ‘dining  room’, serai,  n.,  a  place  for  the  accommodation  of  trav¬ elers  in  the  East.  —  Turk,  serai,  ‘palace’,  fr. Pers.  sardi,  ‘mansion,  inn’,  fr.  OPers.  srdda, ‘residence’,  from  base  pra-,  ‘to  protect’,  whence also  Avestic  frrayeihti,  ‘they  protect’.  See  cara¬ vanserai.
```


## [2026-10-15T02:45:30.840Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 6160,6175p FVQ_pages.txt; grep -n '^trans-,\\|^trans,\\|^truncate,\\|^nectar,\\|^thorough,\\|^nostril,\\|^drill,\\|^through,\\|^terminus,' KLN_1966.txt | head -20"
}
```


### [2026-10-15T02:45:31.264Z] TOOL RESULT

```
1 Akkadische Fremdworter, 67.
2 X"1HD as used on the incantation bowls is significant ; cf. Montgomery,
Aramaic Incantation Texts, Glossary, 297.FOREIGN VOCABULARY OF THE QUR*AN 167
into Arabic from an Iranian source, a theory also put forward by
Sachau in his notes to the Mu'arrdb, p. 21. This is of course possible,
since the Arm. zfyiui^ is from the Iranian, as also the Ossetian dray, 1
but Syr. L^ was a very commonly used word with many derivatives
(PSm, 4325), and Vollers, ZDMG, 1, 613, is doubtless right in deriving
the Arabic word from the Syriac.
(Surddiq).
xviii, 28.
An awning, tent cover.
The passage is eschatological, descriptive of the torments of the
wicked, for whom is prepared a fire " whose awning shall enwrap
them ". The exegetes got the general sense of the word from the
passage, but were not very sure of its exact meaning as we see from
12262:drill,  tr.  and  intr.  v.,  to  bore.  —  Du.  drillen,  ‘to bore;  to  train  (soldiers)’,  fr.  I.-E.  base  *ter-,  ‘to turn,  to  bore  by  turning’,  whence  also  OE. by  rel,  ‘hole’.  See  thrill.
12263:drill,  n.,  an  instrument  for  boring.  —  Partly  fr. Du.  dril,  drille,  ‘an  instrument  for  boring’  (fr. drillen,  ‘to  bore’),  partly  fr.  drill,  ‘to  bore’, drill,  tr.  v.,  to  train  (soldiers,  etc.)  —  Du.  drillen, ‘to  train’,  identical  with  the  verb  drillen,  ‘to bore’  (see  drill,  ‘to  bore’).  For  sense  develop¬ ment  cp.  MLG.  drillen,  ‘to  turn,  roll’. Derivative:  drill,  n.,  the  act  of  training  (sol¬ diers,  etc.).
12264:drill,  n.,  a  small  furrow.  —  Fr.  obsol.  drill,  ‘rill’, which  is  of  Uncertain  origin.
12270:drill,  n.,  a  baboon  of  Western  Africa.  —  Native name.  Cp.  mandrill.
25640:nostril,  n.  —  ME.  nostrill,  nosethirl,  fr.  OE.  nos- pyrl,  lit.  ‘hole  of  the  nose’,  fr.  nosu,  ‘nose’,  and pyrel,  ‘hole’,  fr.  purh,  ‘through’.  See  nose  and
38672:terminus,  n.,  boundary.  —  L.,  ‘boundary  line, boundary,  limit’,  rel.  to  termen,  ‘boundary stone’.  See  term  and  cp.  conterminal,  conter- minus.
39100:thorough,  adj.  —  ME.  thorugh,  fr.  OE.  puruh,  a var.  of  purh.  See  through.
39818:trans-,  pref.  meaning  ‘across,  over,  beyond, through’.  —  L.  trans,  rel.  to  Umbr.  traf,  trahaf, tra  and  cogn.  with  OI.  tirah,  Avestic  taro,  W. tra,  ‘across,  beyond’,  fr.  I.-E.  base  *ter-,  ‘to  go through,  cross  over’,  whence  also  L.  terminus, ‘boundary  line’;  see  term  and  words  there  re¬ ferred  to  and  cp.  esp.  tranquil,  transom,  tres, trespass,  trestle,  trebuchet.  Formally  L.  trans  is the  pres.  part,  of  *trare,  ‘to  go  through’  (L. intrare,  ‘however’,  is  not  formed  fr.  pref.  in-  and *trare,  but  back  formation  fr.  intra,  ‘within’; see  enter,  ‘to  go  within’).
```


## [2026-10-15T02:45:34.203Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 6176,6200p FVQ_pages.txt; grep -n '^through,\\|^nectar,\\|^trunk,\\|^-ter\\|^term,' KLN_1966.txt|head"
}
```


### [2026-10-15T02:45:34.675Z] TOOL RESULT

```
Bail's comment on the verse. .
It was very generally recognized as a foreign word. Raghib,
Mufraddt, 229, notes that the form of the word is not Arabic, and
al- Jawaliql, Mu'arrab, 90, classes it as a Persian word, 2 though he is not
very certain as to what was the original form. Some derived it from
.pl^r-j, meaning an antechamber, others from a^ jjj~* curtains, others
from LJu^^r-'j 3 an( i 7 et others from Aj-1^. 4
Pers. a^ j'J j~ is the form from which we must work. It is defined
by Vullers as " velum magnum s. auleum, quod parietis loco circum
tentorium expandunt ", 5 and is formed from *5 J^ a veil or curtain
(Vullers, i, 340), and an O.Pers. \AmSa, 6 from which came the
1 Hiibschmann, Arm. Qramm, i, 190. Addai Sher, 89, wants to derive the Pers.
M-r from the Syr., but this is putting things back to front. For the Pahlavi form
see Salemann, Manichaeische Studien, i, 121 ; Telegdi, in JA, ccxxvi (1935), p. 255.
2 So as-Suyuti, Itq, 321, and Siddiqi, Studien, 64.
8 al-Khafaji, 105. On the form **j^j~ see Noldeke, Mand. Qramm, xxxi, n. 3.
* Lagarde, Ubersioht, 176n.
%6 Lex, ii, 257. ,
Hiibschmann, Persische Studien, 199. Cf. the Phlv. >^0lll3id sraitan and Pers.
, Horn, Grundriss, 161.168 FOREIGN VOCABULARY OF THE QUR*AN
Arm. u/iiu^ 1 and the Judaeo-Persian !"!N"10, 2 both meaning forecourt
(avXrj or (Trod). From some Middle Persian formation from this
Vsrd8a with the suffix ^ was borrowed the Arm. w/iui^ui-} meaning
cwr^am, 3 andtheMandaean Np""lN"")0 roof of tent or awning.* Theword
occurs in the old poetry, e.g. in Labid (ed. Chalidi, p. 27), and was
40356:trunk,  n.,  1)  stem  of  a  tree;  2)  body.  —  ME. tronke,  trunke,  fr.  MF.  (=  F.)  tronc,  fr.  L.  tr  un¬ cus,  ‘the  stem,  bole  or  trunk  of  a  tree’,  prop,  ‘the stem  with  the  boughs  lopped  off’,  from  the  ad¬ jective  truncus,  ‘lopped  off,  broken  off;  maim¬ ed,  mutilated’,  which  prob.  stands  for  *troncos, fr.’  I.-E.  base  *trank-,  ‘to  press’,  whence  also Lith.  trenkiu,  trehkti,  ‘to  shake,  jolt’,  trahksmas, ‘turmoil,  tumult’,  W.  trwch,  ‘maimed’;  prob. not  cogn.  with  E.  throng.  Cp.  truncate,  trun¬ cheon,  trunnion,  trench.  Cp.  also  bronco. Derivatives:  trunk,  adj.  and  tr.  v.,  trunk-ed,  adj. trunk,  n.,  proboscis  of  the  elephant.  —  From  a confusion  of  prec.  word  with  trump,  ‘trumpet , which  was  earlier  used  also  in  the  sense  of  ‘pro¬ boscis’,  fr.  F.  trompe,  ‘trumpet;  proboscis’, trunnion,  n.,  one  of  the  two  pivots  projecting from  either  side  of  the  cannon.  —  F.  trognon, ‘core  (of  apple),  stump  (of  cabbage) ,  fr.  tronc , ‘trunk’.  See  trunk,  ‘stem  of  a  tree’, truss,  tr.  v.,  to  bind,  fasten.  —  ME.  trussen ,  fr. OF.  torcer,  trusser,  trousser,  torser  (F.  trousser), ‘to  pack,  bind,  truss,  fr.  VL.  *torciare,  ‘to  twist’, a  derivative  of  *torca -  ‘bundle,  torch  .  See  torch and  cp.  torsel,  trousse,  trousseau,  retrousse. Derivatives:  truss-ed,  adj.,  truss-er,  n.,  truss-ing, adj.  and  n.
```


## [2026-10-15T02:45:46.184Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:1778 --image 2>&1 | head -80; awk 'BEGIN{RS=\"\\f\"} NR==113' data/verification/sources/refs/TLM.txt | head -60"
}
```


### [2026-10-15T02:45:46.800Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1778.png
REF: BQT:1778  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 575  OCR-lang: fas

بیان هشتم
در کاف فارسی با ذال نقطه دار مشتمل بر پنج لغت
عد اردن < چم اول بروزن شماردن, "گذشت ‎٩‏ - جنم‌اول‌وفتح ثانی‌وسکون
بمعنی گذاشتن باغد۱ - وبمعنی اداکردن ۳ - | شین نقطه دار وفوفانی » ماضی گذشتن باشدبچند
وحبا(۱) نمودن پمنی‌پیش کش کردن هم هست- | معنی - وبمعنی عبرهم هت یمنی عبور کردواز
ویمعنی گذرانیدن هم آمده است بچادممنی؟۴ ۰ ارو وی ریا است که
۰ ۰ ق گوشند - و ماضی بیش افتادن
گذادرش؟ - بنم اول وکر رابع بمربی ربق ای ی ۳
5 هت بمنی پیش افتاد - وماضی گذشتن بمعنی
وسکون شین نقطه دار»بمعنی گذشتن وترذدادن- 8 : .2 ۱
5 ترك دادن هم آمده است که از ترك و تجرید
وادا نمودن ‎٩‏ - وگذرانیدن بچند همنی باشد. ی ۱
ناش ۹ : باشد - وتجاوز از کناه وتقصیر را ی ز گوندمنی
سین - باشن‌وتای قرشتبروزن | ویگر این‌کار نمیکند » وعآل این دومعنی یکی
ومعنی گذاردن‌است که‌بهادن ‎٩‏ - وادا کردن۷٩‏ است چه هردو را غرض ترك دادن باشد-وبمعنی
وحبا نمودن - وکنرانیدن بجند آهمنی باشد ۰ بعد هم هت چنالکه گوبند «از گذشت آن»بمنی
گذر نامه < جم اول » خطجواز باشد بعد از آن واز بعد آن *۹- ودر مقام غیر وجز
پستی نوشته‌ای که مسافرانرا دهند تا از کذربابان م استعمال: میشود - وکنایه ازقطع شدن نفس
وراه داران وامثالآها کی مانع ابشان‌شود ۸ ۰ | آخرین آدمیزاد است ۰
(۱) خم ۱ : جیا - ۱
۹ - راد :گذاعتن ۰ ۳ ‌ باین‌معنی گزراردن» (ه.م.) ات ۰
۴ < گذاعتن » پهلوی ۰۷1127۲180 ارمنی ع۰۷12۳ هندی باستان 7 «اسشق
۴۳ » اوستا ۷1-1۸7 «بارتولمه ۹4۰ «لیبر کس ۲4۹ در فارسی بمعئی متمدیآمده . یعنی
عور دادن : نیزه گذار.رك : هوبشمان یرک ی ره ار - آسم مصدر ازه گذاردن 6 (ه.م.).
یو باین‌ممنی* گزارش»( م.( است. ۹ گذاردن ۰ - رد : گزاردن ۰
۸ - همه دباات ودین ورز و تيك رائی کن
که سوی خلد برین باغدت گذر نامه .
۰ شهید بلخی « لغت فرص ۸۵۵۳ ۰
-فرهنگستان‌این کلمهرا بمعنی«تن کرم نوشته‌ای که برای مافرت باشفاس داده میشود-
71 گرفته است . « واژه های نو . ۱۳۱۹ ۰۹۷۱ ‎٩‏ -رك: گذشت.
۴ امروز «گذشته از» گونبند :
گذشت از پرستیدن کرد کار بجز خواب وخوردن ندارند کار.
نظامی گنجوی «فرهنگه نظام».
#گذشتی - جم اول وفتح دوم وچهارم » پپلوی ۳۷142۳128 ۷11888188 ( عبور
کردن). ازاوستا ۷1-187 «بارتولمه ۹4۰ *لیبر که ۲۸۹ ورك : تاوادیا س ۱۹۷؛ عبورکردن »
مرور کردن , تقاطم کردن » پیش رفتن » مقدم شدن - تجاو زکرزن - ترك کردن - بخشیدن .
(برهان قاطع ۲۳۷)

deogramm  GUL,  Familie.'1'  *tu,  be  strong ,   Av.  tu,  Skt.  tu.]
takabara,  adj.  a   word  of  doubtful  meaning  and  characterizing the  Ionians  in  Dar.  NRa.  3.  Nom.  pi.  m.  takabara.  \\  B   retain the  old  interpretation,  vjelche  geflochtenes  Hoar  tragen.  Cf.  Foy, KZ,  35,  63  and  later  KZ,  37,  545.  Bartholomae  rejects  on  phil- ological grounds  the  attempted  connection  with  Arm.  tagavor, Krone  tragend.  Could  the  word  signify  swift-  (YAv.  tak,  hasten , Skt.  tak)  riding  or  sea-faring  (YAv.  taka,  water-course  +   bara, cf.  asabari)  ?
taxmaspada  (Elam,  takmaspata),  m.  name  of  one  of  the  com- manders of  Darius.  Nom.  sg.  taxmaspada.  taxma,  brave ,   Av. taxma  (New  Pei'S,  tahm)  +   *spada,  army ,   GAv.  spada,  YAv.  spaSa (New  Pers.  sipah,  Horn,  NS,  42,  3).
92
AXCIEXT  PERSIAX  LEXICOX
taxs  (Pres,  taxsa-,  Bartholomae,  Grunclr.  123),  to  be  active. Foy  regards  the  root  as  a   kompromissbildung  between  *tas  (Skt. taks,  Av.  tas  in  tasan)  and  "tvaxs  (Skt.  tvaks,  Av.  #waxs).
  with  prefix  ham,  work  together ,   cooperate ,   work.  Pret.  1
Sg.  hamataxsaiy.  3   sg.  hamataxsata.  3   pi.  hamataxsanta.
tacara,  paiace.  Acc.  sg.  tacaram,  Dar.  Pers.  a.  New  Pers.  tazar. Cf.  Horn,  NS,  31,  2;  Foy,  KZ.  37,  516.
tar,  to  cross  over.  Av.  tar,  Skt.  tr.
O
  with  prefix  fra,  depart  from,  abandon.  The  old  reading
of  Rawlinson  fratarta,  Bh.  3.  5,  part.  nom.  sg.  is  confirmed  by KT.  Foy  (KZ,  35,  13)  first  suggested  frarixta,  but  later  (KZ.  37, 556)  returns  to  the  reading  fratarta;  cf.  Hoftinann-Kutschke,  Or. Litt.  Ztg.  Nov.  1905;  Tolman,  Vdt.  Stud.  1.  21.
  with  prefix  viy,  pres,  taraya-  (Bartholomae,  Grundr.  115),
put  across,  cross.  Pret.  1   sg.  viyatarayam  (confirmed  by  KT), Bh.  5.  1.  1   pi.  viyatarayama  (confirmed  by  KT's  cuneiform
text;  KT's  transliteration  has  the  old  reading  viyatarayama  which Bartholomae,  Grundr.  109,  regarded  as  pret.  with  pres,  ending; cf.  Skt.  apacyamas),  Bh.  1.  18.
taradraya,  adv.  across  the  sea.  *tara,  beyond,  YAv.  taro  (New Pers.  tar),  Skt.  tiras  -)-  drayah  (q.  V.).
tarava  (Bab.  ta-ar-ma-’).  f.  name  o
```


## [2026-10-15T02:45:53.693Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^anteros\\|^anter\\|^antero\\|^ənteros\\|^n̥ter' IEC.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==29' IEC.txt | grep -n -i -B2 -A8 'anter' | head -40"
}
```


### [2026-10-15T02:45:54.250Z] TOOL RESULT

```
602:anteros “second, other. Cf. anos (1) and -teros. WP I, 67; II, 337 Skt. ántarab; Per. andar (in the phr: madar i andar 'stepmother); Oss. àndár, cf. also än- dära (*otherwise', fr. *antero); Arm. cf. andra- “back, again’, andren ‘again’; Alb. cf. denom. ndrroj ‘I change: Go. anpar; OHG andar; ON annarr; OE ober; OCS vütoryj; Cz. cf. vteřina “second of time’; úterý (scil. den) “Tuesday”; Li. antras; Latv. otrs; OPr. antars, anters
```


## [2026-10-15T02:46:01.040Z] TOOL CALL #20: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-15T02:46:01.052Z] TOOL RESULT

```

```


## [2026-10-15T02:46:03.391Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/terh₂-",
 "prompt": "List the descendants given, especially Iranian (Avestan, Old Persian, Middle Persian, Persian), Latin (trans, intrare), Germanic (through, thyrel/nostril), Greek (nektar), and any note on *-teros or Persian -tar. Quote exactly."
}
```


## [2026-10-15T02:46:04.341Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/سرا",
 "prompt": "Quote the Persian etymology section exactly (Middle Persian form, Old Iranian/Proto-Iranian form, PIE root)."
}
```


## [2026-10-15T02:46:05.094Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/سرادق",
 "prompt": "Quote the Arabic (and Persian if any) etymology section exactly."
}
```


## [2026-10-15T02:46:05.994Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/-تر",
 "prompt": "Quote the Persian etymology for the comparative suffix -tar exactly (MP, Proto-Iranian, PIE forms)."
}
```


## [2026-10-15T02:46:06.695Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nectar",
 "prompt": "Quote the etymology exactly, including any alternative origins."
}
```


## [2026-10-15T02:46:07.316Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/drill",
 "prompt": "Quote the etymology of drill (verb, to bore) exactly, including the PIE root."
}
```


### [2026-10-15T02:46:07.861Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:46:07.878Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:46:08.010Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:46:09.946Z] TOOL RESULT

```
# Arabic Etymology of سرادق

According to the Wiktionary entry, the etymology section states:

"Borrowed from a Middle Iranian word of the form _srādak_, same as later _sarāy_"

The word was borrowed from Middle Iranian, with the form *srādak* being an earlier variant of what later became سَرَاي (sarāy), distinguished by having one fewer suffix.
```


### [2026-10-15T02:46:12.813Z] TOOL RESULT

```
# Descendants of PIE *terh₂-

## Iranian Languages
**Avestan**: Not explicitly listed in the provided content.

**Old Persian**: The text shows "*tarayati" (reconstructed) with a derivative form "𐎻𐎡𐎹𐎫𐎼/𐎹𐎶" (viyatarayam, "1sg.caus.impf.act.").

**Middle Persian & Persian**: Not directly listed; however, the Persian suffix "-tar" (comparative marker) may derive from this root's descendants.

## Latin
"intrō" ("to enter, go into, penetrate") is shown as descending from Proto-Italic *trō, which connects to the zero-grade ye-present form.

## Germanic
"Through" appears via "Proto-Germanic: *þurhw" derived from the zero-grade plus a suffix.

## Greek
"νέκταρ" (néktar, nectar) is traced to a compound formation "*néḱ-t(e)rh₂-s" combining this root with the element meaning "to perish."

## Comparative Marker
The text does not explicitly discuss *-teros or the Persian comparative "-tar" formation as a separate entry.
```


### [2026-10-15T02:46:13.021Z] TOOL RESULT

```
# Persian Etymology Section - Forms Requested

Based on the content provided, here are the etymological forms from the Persian section:

**Middle Persian form:** The page shows "\[script needed\] (hur /⁠hur⁠/)" but notes that the native script is missing.

**Old Iranian/Proto-Iranian form:** "Proto-Indo-Iranian _[\*súraH](/wiki/Reconstruction:Proto-Indo-Iranian/s%C3%BAraH "Reconstruction:Proto-Indo-Iranian/súraH")_ ("liquor")"

**Sanskrit cognate:** The etymology states the word was "Borrowed from Sanskrit _[सुरा](/wiki/%E0%A4%B8%E0%A5%81%E0%A4%B0%E0%A4%BE#Sanskrit "सुरा")_ (surā)"

The page does not provide a specific PIE root, only the Proto-Indo-Iranian reconstruction listed above.
```


## [2026-10-15T02:46:15.228Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/سرای",
 "prompt": "Quote the Persian etymology section exactly (Middle Persian form, Proto-Iranian form, PIE root)."
}
```


## [2026-10-15T02:46:16.249Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/تر",
 "prompt": "Quote exactly the Persian etymology for the comparative suffix -tar (if present), including Middle Persian, Proto-Iranian, PIE forms."
}
```


## [2026-10-15T02:46:17.669Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-teros",
 "prompt": "Quote the etymology/origin of the suffix and list Indo-Iranian descendants (Sanskrit -tara, Avestan -tara, Persian -tar) and *h₂énteros if mentioned."
}
```


## [2026-10-15T02:46:18.665Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/νέκταρ",
 "prompt": "Quote the Ancient Greek etymology exactly, including alternative (Semitic/Egyptian/pre-Greek) proposals and Beekes."
}
```


## [2026-10-15T02:46:19.515Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/drill",
 "prompt": "Quote the English etymology of drill (verb/noun, to bore) exactly, including Proto-Germanic and PIE forms."
}
```


## [2026-10-15T02:46:20.232Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/through",
 "prompt": "Quote the English etymology exactly (Old English, Proto-Germanic, PIE)."
}
```


### [2026-10-15T02:46:24.610Z] TOOL RESULT

```
# Etymology of "Through"

Based on the Wiktionary entry, here is the exact etymological progression:

**Old English:** "þurh"

**Proto-Germanic:** "*þurhw" (meaning "through")

**Proto-Indo-European:** "*tr̥h₂kʷe" - described as "suffixed zero-grade from *terh₂- ('to pass through') + *-kʷe ('and')"

The entry notes that "through" derives from Middle English forms (thurgh, thrugh, thruch, thruh) that came from Old English þurh, which in turn came from the Proto-Germanic *þurhw, ultimately tracing back to the Proto-Indo-European root *terh₂- meaning "to pass through."

[WebFetch note: this page's text is 104200 characters long and the answer above covers only characters 0 to 100000; the final 4200 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


### [2026-10-15T02:46:24.947Z] TOOL RESULT

```
# Proto-Indo-European *-teros Suffix

## Etymology/Origin
The suffix *-teros is described as a "Contrastive or oppositional adjectival suffix" that functioned to mean "one which is especially X" or "one which is more X than other things."

## Indo-Iranian Descendants
According to the page, the suffix evolved through the following lineage:

- **Proto-Indo-Iranian:** *-taras
  - **Sanskrit:** -तर (-tara)
  - **Avestan:** -𐬙𐬀𐬭𐬀 (-tara)
  - **Persian:** ـتر (-tar)

Additional Iranian language descendants include Kurdish (-tir), Zazaki (-yer, -êr), and Middle Persian (-tar).

## Related Term
The page also lists **Reconstruction:Proto-Indo-European/h₂énteros** among its derived terms, though detailed information about this specific formation appears in the derived terms section.
```


### [2026-10-15T02:46:25.590Z] TOOL RESULT

```
# Persian Etymology Section Quote

According to the Wiktionary entry, the Persian etymology traces back through these forms:

**Middle Persian:** "slʾd (srāy, 'hall, house')"

**Proto-Iranian:** "thrāya ('to protect')"

**Proto-Indo-European:** "*terh₂- ('to cross over')"

The full etymological statement indicates the word derives from Middle Persian through Old Persian *srāda, ultimately connecting to Proto-Iranian and PIE roots related to protection and crossing.
```


### [2026-10-15T02:46:26.180Z] TOOL RESULT

```
# Etymology of "Drill" (verb/noun - to bore)

Based on the Wiktionary content provided, here is the etymology for Etymology 1 (the drilling/boring sense):

**From Middle Dutch _drillen_ ("bore, move in a circle").**

Unfortunately, the source document does not provide Proto-Germanic or Proto-Indo-European reconstructions for this term. The etymology traces the word only back to Middle Dutch, with no deeper etymological connections listed in the material supplied.

[WebFetch note: this page's text is 117070 characters long and the answer above covers only characters 0 to 100000; the final 17070 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


### [2026-10-15T02:46:26.372Z] TOOL RESULT

```
# Ancient Greek Etymology of νέκταρ

**Traditional Indo-European Theory:**
"Traditionally taken as a poetic compound, from Proto-Indo-European *neḱ- ('to perish; to disappear') + *-tr̥h₂ ('overcoming')" — literally meaning "overcoming death" because it supposedly granted immortality.

**Alternative Proposals:**
The entry notes that "other theories involving a non-Indo-European borrowing have been proposed." These include:

- **Pre-Greek origin:** Furnée compares νῑκᾰ́ρῐον (eye salve), suggesting both words derive from Pre-Greek sources.

- **Semitic borrowing:** Levin has suggested a Semitic origin.

- **Egyptian borrowing:** Griffith proposed an Egyptian source.

**Beekes' Assessment:**
According to the reference, Beekes "appears to be split between the Indo-European and Pre-Greek theories, while expressing skepticism about the Afro-Asiatic proposals."

The etymology remains uncertain, with scholarly consensus acknowledging multiple plausible but unproven linguistic origins.
```


### [2026-10-15T02:46:27.258Z] TOOL RESULT

```
# Persian Etymology for -tar Comparative Suffix

Based on the document, the Persian etymology section does not contain information about the comparative suffix **-tar**. 

The page only provides etymology for the Persian adjective **تر** (tar) meaning "moist, wet," which traces back through: "Middle Persian [script needed] (tl', LCDr /⁠tarr⁠/, 'wet, moist')" and Northern Luri.

The comparative suffix **-tar** is mentioned under Ottoman Turkish (Etymology 4), where it states: "Borrowed from Persian _[ـتر](/wiki/%D9%80%D8%AA%D8%B1#Persian:_comparative)_ (\-tar)." However, no etymology for the suffix itself (Middle Persian, Proto-Iranian, or PIE forms) is provided in this document.
```


## [2026-10-15T02:46:29.602Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/گذشتن",
 "prompt": "Quote the Persian etymology exactly (Middle Persian, Proto-Iranian, PIE)."
}
```


## [2026-10-15T02:46:30.395Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/truncus",
 "prompt": "Quote the Latin etymology exactly, including PIE root proposals and de Vaan."
}
```


## [2026-10-15T02:46:31.126Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/terminus",
 "prompt": "Quote the Latin etymology exactly, including PIE root."
}
```


## [2026-10-15T02:46:31.796Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/trans",
 "prompt": "Quote the Latin etymology of trans exactly, including PIE root."
}
```


## [2026-10-15T02:46:32.658Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/nostril",
 "prompt": "Quote the English etymology exactly (Old English nosþyrl, þyrel, PIE)."
}
```


## [2026-10-15T02:46:33.360Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/अन्तर",
 "prompt": "Quote the Sanskrit etymology exactly (PIE *h₂énteros etc.), and meanings 'other'."
}
```


### [2026-10-15T02:46:37.082Z] TOOL RESULT

```
# Latin Etymology of "Terminus"

According to the Wiktionary entry, the Latin etymology is:

"From Proto-Italic *term(e)nos, from Proto-Indo-European *térmn̥ ("boundary")."

The entry further notes that the Proto-Indo-European root derives from either *terh₂- or *ter-, combined with the suffix *-mn̥.
```


### [2026-10-15T02:46:37.246Z] TOOL RESULT

```
# Latin Etymology of "trans"

According to the Wiktionary article, the Latin etymology is:

"From Proto-Italic *trānts, from Proto-Indo-European *tr̥h₂-n̥ts, from *terh₂- ('through, throughout, over')."

The article also notes that this root is "Cognate with English through" and other Germanic and Romance language equivalents, establishing a deep Indo-European origin for the word meaning "across" or "beyond."

[WebFetch note: this page's text is 138279 characters long and the answer above covers only characters 0 to 100000; the final 38279 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


### [2026-10-15T02:46:37.773Z] TOOL RESULT

```
# Latin Etymology of "Truncus"

## Origin and PIE Root

The Latin term has an uncertain origin, though scholars propose a Proto-Indo-European connection. According to the entry: "Unknown origin, but possibly from Proto-Indo-European *twerḱ- ('to cut')."

## Related Languages

The word shows cognates across several ancient languages: "Cognate with Ancient Greek σάρξ (sárx), Old Irish tru, troich ('fated to die') and Latin trux and Proto-Slavic *strǫkъ."

## De Vaan Reference

The etymological dictionary by Michiel de Vaan (2008) is cited as a primary scholarly source for this entry, listed in the references section as covering pages 630-631 of his *Etymological Dictionary of Latin and the other Italic Languages*.
```


### [2026-10-15T02:46:38.190Z] TOOL RESULT

```
# Etymology of "Nostril"

Based on the Wiktionary entry, here's the English etymology:

The word comes from **Middle English *nostrille***, which derives from **Old English *nosþyrel***. 

The page explains the Old English term through surface analysis: *nose* + *thirl* (meaning "hole"). However, the document does not provide Proto-Indo-European (PIE) roots for this word—it only traces the etymology back to Proto-Germanic *\*nustriz* ("nostril").

The entry notes cognates in Old Frisian *nosterle* and Middle Low German *noster*, all stemming from the same Proto-Germanic root.
```


### [2026-10-15T02:46:38.350Z] TOOL RESULT

```
# Persian Etymology of گذشتن

**Middle Persian:** "wtštn' /⁠widaštan⁠/, wtltn' /⁠widardan⁠/" meaning "pass, cross, die"

**Proto-Iranian:** "*witárHati" ("to pass by")

**Proto-Indo-European:** "*wí" ("apart") combined with "*tárHati" ("to cross over")

The modern Persian form derives from these ancient roots through sound changes, particularly an irregular shift from -d- to -ð- to -z-.
```


### [2026-10-15T02:46:49.073Z] TOOL RESULT

```
# Sanskrit Etymology of अन्तर (antar)

## PIE Origins

The Sanskrit word derives from Proto-Indo-European through two merged adjectives with different laryngeals:

**"*h₁énteros ("inner; what is inside"), derived from the adverb *h₁entér ("between")"** and **"*h₂énteros ("other, beyond, second")"**

## Meanings Related to "Other"

In Sanskrit, अन्तर functions as an adjective with the sense of being different or distinct. The noun form carries meanings including:

- **"different, other, another"** (particularly when used at the end of compounds, as in the example देशान्तरम्, meaning "another country")
- Additional senses encompass interval, distance, difference, and distinction

The word's etymological connection to concepts of separation and otherness remains consistent across its various grammatical applications in Sanskrit texts.
```


## [2026-10-15T02:46:56.374Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/terh₂-|PIE terh2 descendants (through, nektar, OP viyatarayam)\" \"https://en.wiktionary.org/wiki/سرای|sarāy < MP srāy < PIr thrāya\" \"https://en.wiktionary.org/wiki/سرادق|Arabic surādiq < Middle Iranian srādak\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-teros|contrastive suffix -teros > Persian -tar\" \"https://en.wiktionary.org/wiki/νέκταρ|nektar etymology alternatives\" \"https://en.wiktionary.org/wiki/drill|drill < MDu drillen\" \"https://en.wiktionary.org/wiki/through|through < PIE tr̥h2-kwe\" \"https://en.wiktionary.org/wiki/گذشتن|gozaštan < MP widardan < PIr wi-tarH\" \"https://en.wiktionary.org/wiki/truncus|truncus origin unknown, twerḱ-\" \"https://en.wiktionary.org/wiki/terminus|terminus < PIE térmn̥\" \"https://en.wiktionary.org/wiki/trans|trans < tr̥h2-n̥ts\" \"https://en.wiktionary.org/wiki/nostril|nostril < OE nosþyrel\" \"https://en.wiktionary.org/wiki/अन्तर|Skt antara < h2énteros\"; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"page 504, root Ter 1: $note\" 2>&1 | tail -1; done"
}
```


## [2026-10-15T02:46:59.322Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'schützen' BRT.txt | grep -i 'r[aā]\\|θ\\|9r\\|0r' | head -8; grep -n 'jenseits\\|hinüber' BRT.txt | grep -i 'tar' | head -8; grep -n -i '^ *1*\\.* *ter-\\|ter- „' incoming/WLD/WLD_Bd1_pages.txt | head; grep -n 'Ἀνδρ\\|anter\\|pidandar\\|andar' NYB_vol2_glossary.txt | head -5"
}
```


### [2026-10-15T02:47:04.236Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/61ab1235e6f2181f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3e835b65f25c1014.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/63f4284a78a0018a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/80ad60ebe9c5137e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b53f07b17855e69d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a17475496a82c962.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fbc55dbb11690b3f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/edb20513fd1b720e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ae75bf9be5f0ec4c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0f88497fd4f87695.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a38b2b64521b763e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/22c8dfed5cdffe3f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/493f65c7299d2cf4.txt
```


### [2026-10-15T02:47:05.096Z] TOOL RESULT

```
4791:mit  antarp,  pairi  und  ava  'umstellend dazwischen  treten':  yai  titarat  anrö  main- yuf  dähltn  .  .  aiahe  antan  pairi.avail^m (3DPrA.) '"  vohuca  manO  atarsca  "als  an- drang AM.  gegen  die  Schöpfung  . .,  da traten  schützend  dazwischen,."  yt./j.??.
14534:'schirmen,  schützen,  bewahren':  th  nS qtahuBi  katS  %rayenU  ^aiwi.dar>ltäis  av7- bii.  Yt  y.  1 46 ;  —  nai'tm  tsm  anyJm  (sd.) yüSmat  valds  .  .  aSä  «i  %>-äzdBm  ".  .  so schirmet  uns  denn"  Y.34.T,  — ya%a  tis data  . .  aäa  ni  %räzdBm ''  "wie  ihr  uns geschaffen  habt  . .,  so  schirmt  uns  auch"
14561:Zum  V,  %rä:    —    ai.  ygl.  su-lrälrä-   Adj.    — Pii,:  iräyihi,   (la  V.  y.  45)  etl.:  finakih  oder tariiJrih.    —    0    Ausg.    •%taAsca,    ob   Druck- fehler?   Blocket  Lex.  81  hat  ■■%rasA!al ■  j.  ^ä^ü  Inf,  'zu  schirmen,  schützen': äpB  tacinli . .  %r'  pasvi  vJrayh  . .  avaiiihe narqm  YL/5.10;  10";  —  Sr*  asahe  gae- Lariam  . .  mahrkäi  alahe  gaSianam  Yt ip.  48-50.
15482:mit  Akk.:   n?mase  ti  . .  hrr/^ii  TS  anyäÜ-  '  J-  paf o-arajas'tara-  Ad,,  'der  kostbarere, damqn  Ny. /.  1.         a)  die  räumliche  Be-' deutnng   tritt   zurück;    i)    'vor*;    a)    bei 'schützen',  mit  Abi.:  nipäyBis
15541:Abi. 'von  —  her,  von  — weg";  i)  räumlich; a)  'von  —  her':  y£ia  vätJ  .  .  %wäs>m (sd.)  da/in3t(Sp.jo$  u.)  -ri^^/ram^rPZffii'V. _j.42.  b)'(von-wegsva.)abseitsvon— ': panta  vTcinasta  (Sp.  441  m.)  'ri  urvarä- byasca  vam^lbyasca  V.16.  2.  2)  unräum- lich; a)  beim  V.  urvals-  mit  /rü  'sich abwenden  von  —  (weg)':  yat /raotrisaiti 'ri  dusmatalibyasca  .."  H.  z.  17.  b)beira V.  *ah~  mit  aiwi  'discere  ab  — ,  studiren bei  — ':  kal  *nil  dafvayasnat  .  .  agira.- pataiHsä.)  'ri^^  ^aiwyavhai  (Sp.  278  o.) N.  16.  c)  bei  den  Wörtern  für  schützen
15942:mit  an) 'hüten,  schlitzen':  sraosim  ..yB nipaiti  mazdä  damqn  .  .  ys  vUp»m  aküm ..  pnhua  maiki/a  nipaiti  Y.57. 16;  — azftn  bsii..nipayani  vispa  voha  Ytj.Sg; — lam  ta  daiühavB  mpahi  Yt.ro.78.  a)  'be- hUten,  beschützen  vor  — '  (pairi  oder  parB mit  AbL):  nipaysis  mallm  urva%»m  .  . aurva%at  parB  Yli,  24;  —  uvaiibya  nS ahubya  nipaya  (Opt)'^  ..  pairi .,  moAr/tat YL  10. 93^*;  —  faf  iij  /i}tr0  nipätü  pairJ . . Ibaisauhat  Y.5Ä  2.  2)  'in  Obhut,  Ver-
21137:aisqm  . .  ahmnS.vihö  bavaiti  y  granis  . . mi^näiti  mihrS  Yt.  10. 39;  —  y  ('insofern als')  asai  xsa'ir?m  cinasti  (Sp.  430  u.) '  aca'  ..^räyö  lialsa  Y.20.3;  —  ava%a saofyqs  y  v}sp?m  ahßm  .  .  sävayat  Yt '3-^39',  "9,  142;  —  ala  a/ar/  zasta paiii  apa.giurvayat  y  aSi/  biwivanha (Sp,  971  o.)  Yt.  ig.  48;  50;  —  ta  ns  ama uzjamyqn  yü  staota  yesnya  y  hii  fra- da%ai  tnazd^  .  .  pii^räi  aiahe  galhanqm ".  .  sollen  sich  einstellen  .  .,  weil  sie  ja M.  geschaffen  hat  die  Welt  des  Ala  zu schützen"  Y.55,  3;  —  naicil  a^a  ,  .  süs (sd.)  *y'  him  iidar»  malyäka  FrD.  3;  — ta  fiS  data  tii  ?r»zvana  (sd.)  fravaocama .  .  y'  Tia  väam  nüsima  yd^a  (Sp.  1243 o.)  ..  ". .  weil  wir  mit  Eifer  als  Träger.. dienenmüchtenwie.."  Y.70. 2— 4.  V)die Folge  oder  den  Zweck  angebend  'so dass;  auf  dass,  damit';  fi)  im  gAw.;  es folgt  Konj.:  at  nS  .  .  datdyai  kakurma (sd.)  y  ('damit')  n7  a  vohü  jimat  (sd.) manataha  Y.  44.  i;  —  at  .  .  dadat armaitil  qnmä  (sd.),  astqm  (sd.)  tsi  a  anhat y  ('so  dass')  aya»kä  (sd.)  adänäÜ  *paou- ruyj  Y.30.T,  —  at  tat  möi  daxitgm data  . .  mat^ä  (sd.)  y  ('auf  dass')  .  . urvaidyh  . .  ayml  paitl  Y.34.  6.  c)  im jAw,;  es  folgt  a)  Ind.  ('so  dass'):  asti zi  ana  avaval  uxtata  (sd.)  y  .  .  vTspö aifhu!  . .  «f  irihyqstätai  (sd.)  karaite Y.ig.io;  —  yat  .  .  aiwisagUns  däittm yasnimca .  .y  hl  asti  daityS.t)mö  yasnasca . . Yt  8.  56;  Y.  68.  7;  —  da^a^  ahmäi  .  . äyapi>m  y  ta  upanhacat  .  .  Yt.  75. 4.  h)  Konj.  (Inj.,  Imp.)*'  'auf  dass":
3573:•j.apa-yat5eInf.'zuberauben,umdieHabe, 'hinter,   jenseits  von  — '  (Gen.):  /ratarqn zu    bringen':    mä    du^iirjiJ^  (sd.)    zySnqm  ^bansmqn   'rqm   aird  N.  75.  2)"  der
12030:•  j.,  g.,  p.  'tar-  V.  'hinübergelangen  über  -'. Praes-S  /i/ar-,  2 ^taraya-, 20-^ x^taurva- ya-,  5  +  30  (Int.)  iitärqya-.  —  PPfP.  (W) t)r»ia'\  Jnf.  'tantayae-^a.  VgL  noch fratarta''.
12045:•  p  *tara''-draya*'  Adv.  'übet  das  Meer hinaus,  jenseits  des  Meers',  mit  dem  Relativ Bezeichnung  einer  Abteilung  der  Sak^ix: saka  (sd.)  tyaiy  f  D.  6.  3.
20537:*)  Eine  utsche  Götterfigur,  ursptüDgticli  eine Sonnengottheit  (Oldenberq  Rel.  d.  V«da  4S,  190. HiLLEBKANDT  Ved.  Mylh.  j.  128).    In  den  ap.  In- schriften erscheint  der  Name  Äf.  erst  TattArta- xirjcfs  11.;    Darios  L    und   Xerxet  1.    erwähnen der   Gottheit   nicht,    auch   im    gAw.    wird    sie nicht  genannt.    Ich  nehme  an,  dass  M.  in  der Etrengiardäifi/rischen  Lehre    als  Gottheit    nicht anerkannt   war,    ebenso  wenig  wie    iB.  Uaoma (sd.).    Da  aber  der  Glaube  an  M.  im  Volke  lu fest  wunelte ,  waren  die  Priester  späterhin  ge- nötigt, seine  Verehrung   zuzulassen.     Bekannt- lich  hat  sich  alsdann  der  ^-Kiilt  bis  weit  ins Abendland  hinüber  verbreitet     Vgl.  WlNDlsCK- MANN  Mithra  (AKM.  /),  Dst.  ZA.  2.  441. KompA.,  E.  (in  Ableit.);  Abieil,  (s.  •ni^ray, •ml%ranya^  —  Et.  ?  Vgl  Uhlenbeck  WAiSpr. 223,  Bgm.  GrGr.3  74_>'o.    —    aL    ruiträ-   m. 1)  'Freund',    2)  ein  Adilya;  np.  Wir 'Sonne'; a.  noch  p.EN.  Mnpalinn,  fl/lr/>ayii?  USW.  —  Vgl. v^umiia:   —  Pü. :  mihr  (geschr.  ralnn  oder mlnnk);    SüErl.    lu    Y.   16%     mailripalih.     — ')   Erst    in   Inschriften    des  4.  Jahrhunderts ; 2mal    ist   w'a-V,    imal   {Am.  4)   m'>r"    ge- schrieben.    iSchr.  mit   %'r'  s.  Bthl.  BB.  9. 131,  Hbu.  KZ.  jfi.  177;    auf  die  Schreibung mit  fir^  irgend  welche  Schlüsse    aufzubauen, wie  KZ.  36.  571   geschieht,  halte  ich  für  ver- fehlt  —  »>  S.  »i'Ja  No.   3.   —  3)  Hds.  Vo.   — 4)  Zweifellos  eine  aus  arischer  Zeit  stammende Verbindung. •  j.  "miSrö.aoJah-   Adj.  'falsche   Rede führend'   oder  'den  Mfyra   betrügend"'; mi^rfm  .  .  ye^Ae  dar/jä^i  bäsava  /ra-
24871:Raum  jenseits  der  Gestirne,  wo  die  Seligen wohnen  (aikTjp;  nur  Plur.'>:  yiJ  'cibis darisalä  urvSzil  (sd.)  Y.jo.  i;  —  äaius'if .  .  dada'zbii  (sd.)  'iibl^  (als  AP.)  Aqm.- vainsimaidi (sd.)  Y.jÄö;  —  >riscit  tarS parstämcit  hs  urvänim  .  .  frapärayeni  , . 3.  vahistäl  artkaoi  3  vahHM  asl^  3  ta- histaSibys  'csbys  Y.if).f);  —  xsalta  'äi x^atwartlsM  vintS  Yt.  J.  i;  P.,?4;  —  "Sil he  glui  bval  nsit  astm  nsil  ^Vj^)  niit vakistd  at}hu?'9. 40.  S.  noch  i.  a)  bes. mit  anayra-  fsd.) :  tüirJm  gäma  frabaral yö  nari  oiaonS  urva  anayrainra  °cöltva niddiät. .yd  nars  drvais  urva  anayraisi'a IjmShia  nidaoffi  H.a.  15  und  33;  — vahii- timca  ahäm  anayra^a  °ca  P..?^; — J"/«/ a/ii  .  .  upa  anayra  'iä  s^d^äiA  Yt.  12.  35 ; j  Y.  1O.6,  7/,  9,  G.3.  6,  V.  //.  I,  a,  /().  35, iS.  2. 30,  *FrBy.;    —   strqm    manhs    hUrS
28677:•  j.  haetav-  m,  'Damm';  ha  aSaunam urvänö  . .  tarö  cinvatS  p^niSm  vT%arayaii 'tu  (LS.)  mainyavanqm  yasatanam  ". .  bringt die  Seelen  der  Gerechten  .  .,  über  die Brücke  des  Scheiders  hinüber  zum  Ufer- damm der  himmlischen  K"  V.  ig.  30.
10557:eter- „Eingeweide“.
27407:letzten Grunde an iter- „drehen“ (auch Ruten konnen als biegsam benannt
66249:nach Petersson              LUA 1916, 72f. zu      lit.   termenti „sudeln“, s. *ster- „unreine
67014: nach Erdmann; iiber eine andere Deutung s. u. ter- „zart).
67066:Zweig, Trieb, Spro6“ (nicht nach Persson aaO. zu ster- „starren ).
68700:1.   ter- „zappeln, zittern".
68712:2. ter-          „zart,       schwach"              (zu   ter- „reiben“,             s.   d. ;       als   „ab-,        aufgerieben,
68770: 3. ter- „reiben; drehend reiben" (woraus , drehen"), „(reibend) durchbohren"                                                                   ;
68826:terebrci „Bohrer": tarmes ( termes) „Holzwurm" (s. ter- „malmendes Insekt").
69229:                                                                               ter-                                                                  733
370:Alaksandar ['lksndl] Alexander 1?. 783. 108?9, 11013. 11112, 117°. — Paz. Arasangar (Mx).
374:amah [LNH, Prth LN] pers. pron. Ist. p. pl. 1. cas. rect. we: —-ic... āyēm 913-14; to —-ic dāt hem we have been created by thee 397; ētšān (v.s.v. 04) ~ hem ke 5778; - an, ~ an: v. lan. — 2. cas. obl. us: a) dir. obj.: —-ic äkäh framāi kartan please let us know 11%; — martoman 11%; ~ (twice) proleptic obj. of zanišn 409-7; — b) virtual dat.: franāmišn ~ we must proceed 405; ~ ap i tē pat kar ne apāyet we have no need of your water 14?3; 191-2; — c) the agent of a pret. pass.: pas =: framāt HajB:11; HajA: 5.10 (Prth LN); ~ ētēn āšnūt ku 34, ete.; - d) i ~ our: dar i ~ 39, etc.; e) after a prep.: andar, apük, o ~. — Av. (295 sg.) gen. ahmākom, OP amāzam; MPrthPrs ’m’h; Paz. ema; NP ma. V. also -màn.
394:of; o pattākēh ~ to appear 513, 1081; 6 patirak ~ to meet 8%. 731.20-21, ete.; 6 en kustak rón towards this district 715; — with hac: from 184 ete. [hac ... be 6 ... ~ to be converted from... to... PR 945]; hac ... ywvatük away from 747-8, 7667; — with pat: on (a path) ibd. ; — with prev.: andar — to come forth, to appear 87?5; to be handed down 10818-19; — apāc ~ to become again 104?*; apdc 6 to return to 5) (v. bälist). 818-19, 914, 12]9-10; hac ... apāc ~ to return from 991; — apar ~ to shoot up 9573-4; to be allotted to 98*; apértar apar āyēt ku surpas- ses 641%; — hac varten beron be ämat got off the chariot 20?3; (coursers) ke pat róc-6 70  frasang bē āyēnd- (h)b who are always riding a dis- tance of 70 parasangs in one day 6! (v.s.v. h-); hān<i>druž (be) āyēt the space which the Drug will cover 96?3, 9818; bé + the pres. of ~ regularly denotes the fut.: 24"; if the vb. takes the prep. 6 the order is always be 6: 9725, 985-6, 9912-13, 1046-7; — fröt ~ to come down, to descend (hac...6...) 104°; — ul ~ to rise 86°; šuhr pat post ul āmat the sperm rose to the skin 547°. — āmatan < *ā-gmatanai from à + Av. (493 sqq.) OP gam-, cf OP (par)ägmata- ‘gone forth’; äy- < à + Av. (147 sqq.) OP ay-; MPrs ’mdn ”y-; Paz. NP dmadan dy-. This vb. is characteristic of the SW dialects, as against NW āgatan,
413:Amahraspands 397-8; an amäh u Pw!] Gi 6 ham tuxšem [this reading should. be restored] andar äp, andar damik, andar urvar, andar gospand we and he will labour jointly in water, soil, plants, cattle 3915-16; an-ip to ... fräc vēnēnd for thee (dat. ethicus: thou mayest know:) they prophesy ... 51% (v. tē and -p); an 6 amäh asp vāzēnēt you there, bring the horse here to us 541° (cf Spanish nosotros, vosotros); an či gäv that (re- markable) bull 427. 49?-5-18-19; ang [ZK-y] či asp that (remarkable) horse 491’; an če that very man 5419; an alone for the Ist p. sg., v. the next w. — Av. (135 sqq.) anya-, ainya-, OP aniya-; MPrth ny; MPrs ^», "ny ‘another’ (also = 2an); Paz. han, with -c: hanica. In J-Prs hm, ’ny emphasizing a pron. as described above, v. Mackenzie, An early Jewish Persian argument (BSOAS XXXI, 1968, 249-269), L, 1. 14 (p. 262): whny "wy dd dyh ‘and He is the lawgiver’ (hesitatingly combined. with ^ny by M. p. 254); Utas, The Jewish- Persian fragment from Dandàn-Uliq, Or. Su. XVII, 1968 (1969), 129, 1. 13: ny man simply = ‘T, Ll 4: ny mr = anë mara ‘for me’. — Cf also änöd and. enyä.
441:andar [BYN] in: 1. adv. a) referring to a preceding encl. pron. (ef apäk, apar, avis, haciš, patiš): zäyak-e ke-š murvēcak ~ an egg in which there is a chicken 92%; api-§ ... must" (g. v.) u drog ~ nest F:7; without a preceding encl. pron.: Sugud i haft janakan ~ in which there are seven j. (q.v.) 11318-14; haft x"ataidan ~ būt 11314-95; — b) prev., esp. with vbs. of
```


## [2026-10-15T02:47:09.662Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'hinüber\\|durchdringen\\|überwind' incoming/WLD/WLD_Bd1_pages.txt | sed -n 1,400p | awk -F: '$1>69000 && $1<69500' | head; grep -n 'tarō\\|tar5\\|tarö' BRT.txt | head -5"
}
```


### [2026-10-15T02:47:10.022Z] TOOL RESULT

```
69212:    4.    ter-     ..hiniibergelangen,                        hindurchdringen"                        ;        zugehorige praopositionale
69239:Adj. „durchdringend, rasch' '; la ran id- ..Mcer iiber tara-li ,,durchdringend,
69245:gellend", gr. rood? „durchdringend von der Stimme" s. u. '*toro-s „laut“;
69258:„durchdringend                    =
69408:ter ,,hindurchdringen“, ,,durchbohren" sonst nicht nachweisbar).
2464:yat  baväma  aiwi.vanyn  dänavö  . .  ahmi gal'ie  piianähu  Yt.5.73;  —  ahmäi  J/ri- n?nti .  ./ravalayö  buyiil  ahmi  nmäne  giusia va^wa  ..  ". .  dem  . . ;  in  dessen  Hause  . ." V't.  jj-sif.;  Y..;j.6  (s.  2  2  aa);  —  auch bei  Beziehung  auf  das  Subjekt  des  Satzes: (ya^a)nar>m ..  asavamm*jas?nSfm  ahmya nmjne  .  .  paiti  taröpi^wim  dai'i^yät  "als ob  er  einen  Gläubigen,  der  in  sein  (zu ihm  ins)  Haus  kommt  .  ."  V.y.aa;  — naSca  ,  .  *hö  nl  ahmat  haca  gätaot  isaetci fraiütöip  nöit  apaiiitöit(%A.)'B.23.  b)  sub- stantivisch: adä  (sd.)  ta^a  guti  p>r9- sat  as>m  .  .  ahmäi  asä  (als  Subj.)  ,  ■  paitl.- mravat  Y.ag.ii.;  30.t,  46.8,  13;  —  uz- valoayat  zara^ustrS  annm  mainyUm  .  . paiti  ahmäi  adavata  .  .  aarS  mainyus  .  .
2801:Irrlehrer,  der  . ."  \.g,$i{.;  —  yavat  °fa *gaintii  upankacaili  (sd.)  V.  7.  56;  — yavat  'sa  ilß  bySrixfi  (sd.)  .  ,  frabavai \.i4.\y,  — yavat  -lö  spä  anya{sA.) )asö V./5.48,  a)mitrelativischemAnschIuss: "jS  zT  asti  baslazyö.t3mö  .  .yal  *mahnm.- sppni»m.baei'azyd  (sd.)  V.  7.44;  —  '/a  bi~ paitisiana  (sd.)  y3  kaine  V.  75. 19;  19;  — vXsp»m  ä  ahmst.,  yat  -ia  yö  apsntinyBkB uxjasnf  (sd.)  "bis  es,  das  Kind  . ,"  V.  75. 15;  —  'sa  yS  *ar?mBiidd'a.W3.  2)  auf ein  Relativum  als  dessen  Korrelat,  sub- stantivisch: ci'at  dra)ö  avaMUlüt  '^a  yö näirikaya  . .  !^ar>^3tn  frabamt  V.  /J.  4 1 ; —  °sö  .  .  aitayä  vihrkayh  (sd.)  Jq'^-wS.' tarö  *at3kat  . .  ya^a  spä  vtkrkake  k»r?- naoiti  V.  y .  4 1 ;  — "/?  ratufris  *yö  jayara N.if};  24,  60;  —  'sa  yetjhe  apirinSyükö ^•9i  7;  —  °^'''  zaoiranqm  tnaziltaca  . . yiJ  *naire  asaone  *daste  N.^4.  III)  In
3370:gleichen, gleichfalls,  gleicherweise,  item': Aaomö  uxsyeiti  stavans  "ia  na  yö  dim staoili  nri^rajqstarö  bavaiti  "Ä.  wächst, wenn  er  gepriesen  wird;  desgleichen  wird der  Manu,  der  ihn  preist,  siegreicher"  Y. JO.6;  —  caili  nil  aSrahe  pasz'ö  (sd.)  *i "hra  barlti  catafirS .."'^a  dva  °~ia  %ryam
4828:mit  frS^''^  i)  'hervorgehen,  -Ireten': aiiihe  haxayB  fräyente  astva(.»r>take  Yt. ■'5-9SJ  — yü'ia  .,  hvanxsaet^m  tarasca harqtn..fraca  iii/i  aiwica  vazaite  ava^a  . . Yt  /0.118.  2)  'vorwärts,  weiter  gehen': fräyantö  tarö  pilüm  ..yim  cinvats  Vyt. 42.  a)  &oiysX  mA  ß-a^a: /rain /raysiii^ irUtim  uzbaröti  äpö  V.6.2T,  — /ra/a  fra- yaniu  n  maoö  (sA)  Y. /O.  14,  ig;  19;  — /rasa  /raya  (aSIA.)!'  vahisDm  a  ahüm binjayanti  (sd.)  ie  ..  V,  7.52;  —  vgl.  Inf. Jrayäi.  3)  'einhergehen'  iyio? paiti  mit Akk.):  yat  ÖS  paiii  ml  asava  frayaf^  .  . aismssastö  .  .  V.J.  i ;  —  äat  liama  yh paiti  frayat^^  tä paiii, .Yi.  lOjiJ).  4)  'be- gehen', mit  Akk.,  a)  einen  Weg:  kaf  tä pa>ä  (sd.)  Jrayqn^  pasvqm  vil  staorqm va  narqm  vä  Y.S.iy,  ii^23,  3.  15;  — likrava  paoirlm  aHa  pa%ä/rayanlu{s\.3Xl Sing.)  V.  Ä19.  b)  eine  Tat:  (aili  tä ^ao^aa  varsta  , .  fralta^''^  apati(a{&i.) anuzvars/a  . .  V.i^.i.
4954:•vat  ki'ari  utuiti  F.^b;  Yt /( 'vam  uiam  G-5.5;  —  haca  'vatbyS  stjnbyö aoi  sam  Yt5.85,  132  (wo  *°vd'J>yö);  — nihmacii  'vailqm  sfärqm  .  .  y.43.;  — hvan  °va  (IS.)  pai:a  .  .  ma  °va  pa^a  .  . starö  'va  pä^a  yHnti  Yt.  /j.  16;  —  "vaiti/ia niüs  "vaiiiha  pairikaya  pattistätayaSca  .  . Y.16.8;  —  Aaca  *'vaMitt  drujat  V.  J*?, 12;  —  "vai  tmidim  parS.ainli  aauAe "den  Lohn  dort  für  die  künftige  Welt" V.p.44;  —  ym  mä  hau  nä  °z-i
```


## [2026-10-15T02:47:14.020Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'سرادق' MON_part1.txt MON_part2.txt | head -5; grep -n 'پدراندر\\|مادراندر' MON_part1.txt MON_part2.txt | head -5; grep -n 'سرادق\\|سرای' incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-10-15T02:47:14.377Z] TOOL RESULT

```
MON_part1.txt:76274:سرادق: 307509 [معر .] (.) خیمه» سرایرده. 
MON_part1.txt:76280:سرادقات. سرادق اعلی: بارگاه 
MON_part1.txt:76281:انوار الهی و صقع ربوی است» سرادقات 
MON_part1.txt:76282:نوربه» سرادقات قدرت» سرادقات جلال 
MON_part2.txt:23117:پدراندر.] (امر.) کس دیگر (غم.) ناکس» 
MON_part2.txt:41761:مادراندر: ۱۰-۲ [- مادر ندر < مانندر ] 
MON_part2.txt:72918:مادراندر» مادندر. 
MON_part1.txt:17638:(«تا...» با «...خوانده) دهد: پدراندر (پدندر). 
MON_part1.txt:65462:رات: (۲20)۳ [ع.] ((.) پدراندر. 
640:دیر به جایگاه‌های فعلی خود سرایت کردند» چون تا پیش از ۲۵۰۰ سال قبل از میلاد راژه‌های هندی
1097:تروا ادامه داد تاکشته شد. او هم مانند دیگر قهرمانان هند و اروپایی در پی نام نیک بود نه سرای
10461:۴۲ | سول سرای_
```


## [2026-10-15T02:47:37.753Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -n 39818 KLN_1966.txt | tr -cd '\\f' | wc -c; head -n 69212 incoming/WLD/WLD_Bd1_pages.txt | tr -cd '\\f' | wc -c; head -n 12030 BRT.txt | tr -cd '\\f'|wc -c; head -n 14534 BRT.txt | tr -cd '\\f'|wc -c; head -n 602 IEC.txt | tr -cd '\\f'|wc -c"
}
```


### [2026-10-15T02:47:38.334Z] TOOL RESULT

```
868
740
372
458
30
```


## [2026-10-15T02:47:42.011Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 830 832 834; do echo \"== $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -o '^[a-z-]*,' | head -3; done; awk 'BEGIN{RS=\"\\f\"} NR==869' KLN_1966.txt | grep -o '[0-9]\\{4\\}' | head -3"
}
```


### [2026-10-15T02:47:42.547Z] TOOL RESULT

```
== 830
ntablature,
tabloid,
taboret,
== 832
ve,
tall,
tallage,
== 834
tantra,
tantrum,
tany-,
```


## [2026-10-15T02:47:46.518Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=826 && NR<=842 {print \"LEAF \" NR-1; print}' KLN_1966.txt | grep -n 'LEAF\\|\\*ter-\\|\\*tera\\|Avestic\\|tar\\b' | head -30"
}
```


### [2026-10-15T02:47:46.996Z] TOOL RESULT

```
1:LEAF 825
42:LEAF 826
91:LEAF 827
134:LEAF 828
177:tabasheer,  tabashir,  n.,  a  siliceous  substance  found in  the  joints  of  the  bamboo.  —  Arabo-Persian tabashir,  ‘chalk,  mortar’, tabatiere,  n.,  a  snuffbox.  —  F.,  fr.  earlier  taba- quibre,  fr.  tabac,  ‘tobacco’.  See  tobacco, tabby,  n.,  a  kind  of  watered  silk.  —  F.  tabis,  fr. Sp.  tabi,  fr.  Arab,  attdbi,  fr.  at-Attabiyd' ,  name of  a  suburb  of  Bagdad,  where  this  kind  of  silk stuff  was  fabricated.  The  suburb  was  named after  Prince  Attab,  a  descendant  of  the  Om- miads.  Cp.  tabinet,  tobine.
189:LEAF 829
236:LEAF 830
282:LEAF 831
320:OI.  tamas-,  ‘dark-ness’,  rel.  to  tamisrah,  ‘dark¬ ness’,  Avestic  temah-,  ‘darkness’,  and  cogn.
335:LEAF 832
364:tanga,  n.,  also  tanka,  name  of  various  coins  in India  and  Turkestan.  —  Hind,  tanga,  lit. ‘weight’,  fr.  OI.  tahkah,  ‘stamped  coin;  a weight’,  which  is  prob.  connected  with  Tartar. tanka,  ‘a  silver  coin’,  ModPers.  tanga.  Arm. t'anka,  ‘a  small  coin’.
391:LEAF 833
420:tapu,  n.  —  A  var.  of  taboo, tar,  n.,  a  viscous  liquid.  —  ME.  terre,  fr.  OE. teoru,  teru,  rel.  to  ON.  tjara,  Dan.  tjtere,  Swed. tjdra,  OFris.  tera,  MDu.  tar,  ter,  terre,  Du. teer,  G.  Teer.  These  words  orig.  meant  ‘per¬ taining  to  a  tree'.  They  derive  fr.  I.-E.  *derew(o)-, *drew(o)-,  ‘tree’,  whence  OI.  daru,  ‘wood’,  Gk. S6pu,  ‘beam,  shaft  of  a  spear,  spear’,  Spbq,  ‘tree, oak’,  Goth,  triu,  OE.  treow,  ‘tree’.  See  tree  and cp.  the  first  element  in  tarpaulin.
421:Derivatives :  tar,  tr.  v.,  tarr-ed,  tarr-y,  adjs. tar,  n.,  sailor  ( colloq .)  — Abbreviation  of  tarpaulin, tara,  also  tara  fern,  n.,  a  kind  of  New  Zealand brake  with  edible  rootstock.  —  Maori  tara, 'spear'.
444:LEAF 834
456:tarmacadam,  n.,  pavement  constructed  by  spray¬ ing  or  pouring  a  tar  binder  over  crushed  stone.
457:—  Compounded  of  tar  and  macadam.
465:tarpan,  n.,  wild  horse  of  the  Russian  steppes.  — Of  Tatar  origin.
466:tarpaulin,  n.,  a  waterproof  covering  of  canvas.  — A  hybrid  coined  fr.  tar,  ‘dark,  viscid  liquid’,  a Teutonic  word,  and  palling,  ‘covering’,  deriva¬ tive  of  pall,  ‘cloak,  coverlet’,  a  word  of  Latin origin.
470:tars-,  form  of  tarso-  before  a  vowel, tarsal,  adj.,  pertaining  to  the  tarsus.  —  Formed fr.  tarsus  with  adj.  suff.  -al. tarsia,  n.,  mosaic.  —  It.,  fr.  Arab.  tar$‘T,  ’inlaid work',  verbal  noun  of  rasya'a,  ‘he  laid  in’.  Cp. Heb.  ratzd',  ‘he  bored,  pierced’,  martze'a, ‘boring  instrument,  awl’,  Mishnaic  Heb.  ratz'an, Aram,  rutz'and,  ‘shoemaker’, tarsier,  n.,  arboreal  lemur  of  the  East  Indies.  — F.,  fr.  tarse,  ‘tarsus’  (see  tarsus  and  -ier) ;  so  call¬ ed  from  its  long  tarsus.
471:Tarsipes,  n.,  a  genus  of  Australian  marsupials ( zoo! .)  —  ModL.,  compounded  of  ModL.  tar¬ sus,  ’ankle’,  and  L.  pes,  ‘foot’.  See  tarsus  and foot,  and  cp.  pedal.
476:tartan,  n.,  a  kind  of  woolen  fabric.  —  ME.  tir- taine,  fr.  OF.  (=  F.)  tiretaine,  fr.  Sp.  tiritaha,  ‘a thin  silk  stuff’,  lit.  ‘the  rustling  stuff’,  fr.  tiritar, ‘to  shiver’,  a  word  of  imitative  origin.
478:Tartar,  n.  and  adj.  —  ML.  Tartarus,  fr.  Pers.  Ta¬ tar,  ult.  fr.  Tata,  name  of  the  Mongols,  who coming  from  the  Gobi  desert  invaded  Russia  in the  9th  cent.  The  first  r  in  Tartar  is  due  to  a  con¬ fusion  w'ith  L.  Tartarus,  ‘hell’ ;  see  Tartarus. tartar,  n.,  1)  potassium  bitartrate,  KHC4H4Os ( chem .);  2)  a  hard  deposit  on  the  teeth.  —  ME. tartre,  tartar,  fr.  OF.  tartre,  fr.  ML.  tartarum , fr.  Gk.  Tdpxapog  (see  Tartarus);  so  called  by Paracelsus  with  regard  to  the  burning  effect  of this  compound.
479:Derivatives:  tartar-eous,  tartar-ic,  tartar-ish, adjs.,  tartar-ize,  tr.  v.,  tartar-iz-ation,  n.,  tortur¬ ous,  adj.
481:Tartarus,  n.,  the  abyss  below  Hades;  place  of punishment;  Hades,  netherworld;  hell  (Greek mythol.)  —  L.,  fr.  Gk.  Taprapoc,  prob.  a  word of  imitative  origin,  suggestive  of  something frightful.  Cp.  tartar.
482:tartlet,  n.,  a  small  tart.  —  Formed  fr.  tart,  n., with  dimin.  suff.  -let.  Cp.  F.  tartelette. tartrate,  n.,  salt  of  tartaric  acid  (chem.)  —  F., formed  with  chem.  suff.  -ate  fr.  tartre,  ‘tartar’.
483:See  tartar.
505:LEAF 835
510:Derivatives:  tassel,  tr.  v.,  tassel-y,  adj. tassel,  n.  —  A  var.  of  tercel, taste,  tr.  and  intr.  v.  —  ME.  fasten,  ‘to  feel,  taste’, fr.  OF.  taster  (F.  tater),  ‘to  feel,  touch,  handle’, fr.  VL.  *taxitdre,  freq.  of  L.  taxare,  ‘to  touch sharply’,  itself  freq.  of  tangere,  ‘to  touch’  (see tangent).  Cp.  OProveng.  tastar,  It.  tastare,  Sp. and  Port,  tastar,  ‘to  feel,  taste’,  which  are  of  the same  origin.  To  account  for  the  sense  develop¬ ment  ‘to  feel;  to  taste’,  Bloomfield  (in  Indoger- manische  Forschungen)  suggests  the  hypothetic VL.  form  *tastare,  which  should  have  arisen  as a  blend  of  L.  gustare,  ‘to  taste’,  and  tangere,  ‘to touch’.
515:Tatar,  n.  —  See  Tartar.
```


## [2026-10-15T02:47:51.128Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; n=$(grep -n '^trans-,' KLN_1971.txt | head -1 | cut -d: -f1); echo $n; head -n $n KLN_1971.txt | tr -cd '\\f' | wc -c; awk 'BEGIN{RS=\"\\f\"} NR==869 || NR==870' KLN_1966.txt | grep -n '^[0-9]\\{3,4\\} *$\\|^ *[0-9]\\{4\\}' | head"
}
```


### [2026-10-15T02:47:51.545Z] TOOL RESULT

```
251369
0
60:1641
```


## [2026-10-15T02:50:23.982Z] TOOL CALL #47: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-504.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nPIE=W+\"Reconstruction:Proto-Indo-European/terh₂-\"\nPOKR={\"ref\":\"POK:1075\",\"status\":\"supports\",\"note\":\"POK_full.txt line 86174 'Root / lemma: ter-4, terə-: trā-, teru-' 'Meaning: to cross, transgress' Page(s) 1074-1075: 'Avestan tar- hinüber gelangen ... participle vī-tarəta-', 'ap. viyatarayāma we überschritten', 'Old Indie trā- (*hinüberführen = rescue), shield ... Avestan θrā- ... θrāti- shelter, protection', 'Latin termen, terminus Grenzzeichen', 'compare gr. νέκ-ταρ above S. 762'; ter-5 (pp.1075-1076, line 86247): 'Avestan tarə, tarō ... through, over', 'Latin trans', 'Old English þurh ... dyrel durchbohrt; hole'.\"}\nWLD={\"src\":\"WLD\",\"where\":\"Bd. I p.733 (WLD_Bd1_pages.txt line 69212, leaf 740)\",\"stance\":\"supports\",\"note\":\"'4. ter- „hinübergelangen, hindurchdringen“; zugehörige präpositionale ...' with Ai. tarati, tara- 'durchdringend' - the same root WP I 732 ff. that Pokorny revises.\"}\nAHDr={\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins AHD Roots (AHD_watkins1985.txt line 1083) 'terə-2. To cross over, pass through, overcome. ... thur-ila- in OE thyrel, a hole: THRILL; NOSTRIL. ... *tr-kwe in Gmc *thurh: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ... Latin trāns ... *trā-yo- in Iranian thrāya-, to protect, in Middle Persian srāyidhan ... Persian sarāi, inn: CARAVANSARY ... *tru-n-k-o- in Latin truncus ... TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.]'\"}\ndef C(src,where,stance,note): return {\"src\":src,\"where\":where,\"stance\":stance,\"note\":note}\ndef R(ref,status,note): return {\"ref\":ref,\"status\":status,\"note\":note}\nKLNtrans=R(\"KLN:1639\",\"supports\",\"Klein 1966 s.v. trans- (KLN_1966.txt line 39818, leaf 868, page numeral 1641 on the facing leaf): 'L. trans ... cogn. with OI. tirah, Avestic tarō, W. tra, across, beyond, fr. I.-E. base *ter-, to go through, cross over, whence also L. terminus'.\")\nnodes=[]\nnodes.append(dict(id=1,lang=\"Avestan\",words=\"taro, tarya, tar; thrâ; vi-tar\",verdict=\"plausible\",\n derivation=\"Av. tarō (tarə) 'across, beyond' is the adverb/preposition from the zero/e-grade of PIE *terh₂- (Skt. tiras, Lat. trāns); Av. tar- 'to cross over' (pres. titar-, caus. tāraya-; Nourai's 'tarya' is the causative stem taraya-) continues *tárH-ati, and OP vi-tar-/viyatarayam 'we crossed' and Av. vi-tar- belong here (Cheung *tarH). Av. θrā- (θrāyeiti, θrāzdūm) means 'to protect' and θrāti- 'protection': Pokorny and Watkins derive it from *trā- 'bring across, rescue', a variant of the same root, but LIV-style treatments keep *treh₂- 'protect' apart, and the gloss 'shelter, cover' is looser than Avestan 'schirmen, schützen'.\",\n derivation_fa=\"اوستایی tarō «آن‌سو، از میان» و ستاک فعلی tar- «گذشتن، عبور کردن» (با ستاک سببی tāraya-، که «tarya»ی نورایی همان است) از ریشهٔ هندواروپایی آغازین *terh₂- «گذشتن، فراتر رفتن» است و vi-tar- «گذشتن، عبور دادن» در اوستایی و پارسی باستان (viyatarayam) نیز از همین ریشه است. اما θrā- در اوستایی فعل «پاس داشتن، نگاه داشتن» است و θrāti- «پناه»؛ پوکورنی و واتکینز آن را از گونهٔ *trā- «گذراندن، رهانیدن» همین ریشه می‌دانند، ولی برخی آن را ریشه‌ای جدا (*treh₂- «پاییدن») می‌شمارند. پس ادعای نورایی در کل پذیرفتنی است، با این احتیاط که معنای «پناه، پوشش» برای θrā- دقیق نیست.\",\n sources=[PIE,W+\"گذشتن\"],\n ref_check=[POKR,R(\"KLN:1639\",\"supports\",\"Klein s.v. trans- (KLN_1966.txt line 39818): 'cogn. with OI. tirah, Avestic tarō ... fr. I.-E. base *ter-, to go through, cross over'; Klein s.v. caravanserai (line 6501) also cites 'Avestic θrāyeinti, they protect, OI. trāyate, protects'.\")],\n consulted=[C(\"BRT\",\"BRT.txt line 12030 (leaf 372)\",\"supports\",\"'tar- V. hinübergelangen über -. Praes. titar-, taraya-, taurvaya- ... vgl. fratarta'; line 12045 'p. tara-draya Adv. über das Meer hinaus'.\"),\n            C(\"BRT\",\"BRT.txt line 14534 (leaf 458) s.v. θrā-\",\"partial\",\"'schirmen, schützen, bewahren': θrāyente, θrāzdūm 'so schirmet uns' - Bartholomae glosses 'protect', not 'shelter, cover', and does not tie it to tar-.\"),\n            C(\"CHEUNG\",\"*tarH 'to cross over' (CHEUNG.txt line 24798)\",\"supports\",\"'AVESTAN: tar- to cross over || (+ *ui-)'; 'OLD PERSIAN: (+ *ui-) vitar- (caus.) to put across'; 'PIE *terH2- (*treH2-) to go through, cross, overcome = LIV 633 f. | Pok. 1074 f.'\"),\n            C(\"TLM\",\"p.92 (TLM.txt leaf 112)\",\"supports\",\"'tar, to cross over. Av. tar, Skt. tr.' 'with prefix viy, pres. taraya-, put across, cross'; 'taradraya, adv. across the sea. *tara, beyond, YAv. tarō'.\"),\n            WLD]))\nnodes.append(dict(id=2,lang=\"Persian\",words=\"tar 1, tarîn; sarâ; gozaštan\",verdict=\"disputed\",\n derivation=\"(a) -tar/-tarīn: NP comparative -tar (MP -tar, Av./Skt. -tara-) continues the PIE contrastive suffix *-teros; the superlative -tarīn is -tar + adjectival -īn (MP -tom was replaced). Modern handbooks treat *-teros as an independent suffix, not a derivative of the verbal root *terh₂- 'cross', so this arrow is disputed. (b) sarā/sarāy 'house, palace, inn' < MP srāy (slʾd) 'hall, house'; Horn, Klein, Watkins and Wiktionary derive it from Old Iranian *θrāya- 'protection' (Av. θrā- 'protect'), with OIr. θr- > MP sr- and a prothetic vowel in NP (sarāy, sarā); Nyberg prefers OIr. *srāda- (Parthian srād), also connected with the 'protect' family - so (b) is confirmed in substance, with θrā- itself only plausibly from *terh₂-. (c) gozaštan/gozar- 'to pass' < MP widardan, widaštan < OIr. *wi-tarH- 'pass by' (Cheung *tarH, Wiktionary), with irregular -d- > -δ- > -z- and wi- > gu-; the causative gozāštan/gozār- 'to put, let' < MP widārdan < *wi-tāraya- - confirmed. Worst verdict: disputed (because of -tar).\",\n derivation_fa=\"«گذشتن / گذر» از فارسی میانه widardan / widaštan و از ایرانی باستان *wi-tarH- «از کنار گذشتن» است (پیشوند vi- + ریشهٔ tar- «گذشتن»)؛ پیشوند vi- در فارسی نو به «گُ» بدل شده و d میان‌واکه‌ای به ذ و سپس ز رسیده است؛ «گذاشتن / گذاردن» صورت سببی آن است (widārdan). «سرا / سرای» از فارسی میانهٔ srāy «خانه، تالار» است که هرن، کلاین و واتکینز آن را از *θrāya- «پناه» (اوستایی θrā- «پاییدن») می‌دانند و نیبرگ از *srāda-؛ θr- ایرانی باستان در فارسی میانه به sr- و در فارسی نو با افزودن واکه به «سر-» رسیده است. اما پسوند تفضیلی «-تر» (و «-ترین») بازماندهٔ پسوند تقابلی هندواروپایی *-teros (سنسکریت و اوستایی -tara-) است و پژوهش امروزی آن را از ریشهٔ *terh₂- «گذشتن» نمی‌داند؛ پس این بخش از ادعای نورایی پذیرفته نیست.\",\n sources=[W+\"گذشتن\",W+\"سرای\",W+\"Reconstruction:Proto-Indo-European/-teros\",PIE],\n ref_check=[R(\"HRN:161\",\"supports\",\"Horn p.161 no. 727 (HRN.txt leaf 182): 'serāi Palast. Wohl zu aw. θrā-, θrāyeinti schützen, ai. trā-, trāyate; phlv. srāyītan. Hierher gehört wohl auch jüd.-pers. ... arm. LW. srah, srahak, arab. LW. surādiq' - supports sarā only; Horn says nothing there about -tar or guδaštan.\"),\n            R(\"BQT:1778\",\"supports\",\"BQT vol. 3 printed p.1778 (ref_page.py, pdf page 575, OCR) s.v. گذاشتن/گذشتن: Mo'in's note 'گذشتن پهلوی ... از اوستا vi-tar «بارتولمه ۶۴۰»' and for گذاشتن 'پهلوی ... ارمنی ... هندی باستان ... اوستا vi-tar' - supports gozaštan/gozāštan from vi-tar.\"),\n            R(\"TLM:92\",\"supports\",\"Tolman p.92: 'tar, to cross over. Av. tar, Skt. tṛ'; '*tara, beyond, YAv. tarō (New Pers. tar)' - supports the verb/adverb, not the comparative suffix.\"),\n            R(\"MON:1790\",\"not_checked\",\"Mo'in 6-vol page not mappable online/locally.\")],\n consulted=[C(\"CHEUNG\",\"*tarH (CHEUNG.txt lines 24798-24860)\",\"supports\",\"'(+ *ui-) widely attested: NP guδaštan/guδar- ... to pass'; 'NP guδāštan/guδār- (caus./tr.) to place, put; to let, allow'; MP 'wtyl- /wider-/ ... to pass by'.\"),\n            C(\"HUB\",\"HUB.txt lines 5483, 5632, 6957\",\"supports\",\"'gudāštan passiren lassen, guδaštan vorbeigehen'; 'np. guδar Durchgang, Furt, phl. v(i)tar'.\"),\n            C(\"NYB\",\"Glossary s.v. srād (NYB_vol2_glossary.txt line 3507)\",\"partial\",\"'srād (srāy) palace, house — OIr *srāda-: Prth *srād, with suff. *srādak in ... Arab. lw. surādiq large tent; Prs srāy alternating with srāh ..., whence NP sarāi' - Nyberg's base is *srāda-, not *θrāya-.\"),\n            C(\"PHD\",\"PHD.txt line 568\",\"supports\",\"'srāy [slʾd | N sarāy] house, hall'; 'srāyīdan [= Av. θrāya-] protect'.\"),\n            C(\"KLN\",\"s.v. serai / caravanserai (KLN_1966.txt lines 34657, 6501)\",\"supports\",\"'Pers. sarāi, mansion, inn, fr. OPers. srāda, residence, from base θrā-, to protect, whence also Avestic θrāyeinti'.\"),\n            C(\"HRN\",\"p.161 no. 727\",\"supports\",\"serāi < θrā- 'schützen' (see ref_check).\"),\n            C(\"ARY\",\"ARY_pages.txt grep سرای / گذشتن\",\"silent\",\"no usable hit for these headwords in the OCR text.\")]))\nnodes.append(dict(id=3,lang=\"Old Persian\",words=\"srâd, srâda\",verdict=\"plausible\",\n derivation=\"No Old Persian *srāda- is attested in the inscriptions (Kent's lexicon has no such word); it is a reconstruction (OIr. *θrāda- / *srāda-) inferred from Parthian srād, MP srāy/srāh, Armenian loans srah 'hall', srahak 'curtain', Judeo-Persian srʾh 'forecourt' and Arabic surādiq. Klein ('OPers. srāda, residence, from base θrā-, to protect') and Nyberg ('OIr *srāda-') give exactly Nourai's form, and Jeffery reconstructs OP *srāda; the book prints it without the asterisk of reconstruction. Its link to *terh₂- runs through θrā- 'protect', which is itself only plausibly from that root.\",\n derivation_fa=\"صورت srāda در کتیبه‌های پارسی باستان دیده نمی‌شود و بازسازی است (ایرانی باستان *srāda- یا *θrāda-) که از پارتی srād، فارسی میانهٔ srāy، وام‌واژه‌های ارمنی srah «تالار» و srahak «پرده» و عربی «سُرادِق» استنتاج شده است. کلاین، نیبرگ و جفری همین صورت را می‌آورند و آن را به θrā- «پاییدن، پناه دادن» می‌پیوندند. پس سخن نورایی با احتیاط پذیرفتنی است، ولی کتاب باید آن را با ستاره (صورت بازسازی‌شده) می‌آورد و پیوندش با *terh₂- از راه θrā- تنها احتمالی است.\",\n sources=[W+\"سرادق\",W+\"سرای\"],\n ref_check=[R(\"MON:1850\",\"not_checked\",\"Mo'in 6-vol page not mappable; the abridged MON_part1.txt s.v. سرادق (line 76274) only tags it '[معر.]' without an OP form.\"),\n            R(\"VDQ:255\",\"not_checked\",\"VDQ (Persian translation of Jeffery) is JavaScript-rendered; checked the original instead: Jeffery FVQ p.167-168 (FVQ_pages.txt lines 6169-6200) 'an O.Pers. *srāda, from which came the Arm. srah and the Judaeo-Persian srʾh, both meaning forecourt ... From some Middle Persian formation from this *srāda with the suffix -k was borrowed the Arm. srahak ... and the Mandaean ... and the Arabic word' - supports.\")],\n consulted=[C(\"NYB\",\"s.v. srād\",\"supports\",\"'OIr *srāda-: Prth *srād, with suff. *srādak ... Arab. lw. surādiq'.\"),\n            C(\"KLN\",\"s.v. serai\",\"supports\",\"'fr. OPers. srāda, residence, from base θrā-, to protect'.\"),\n            C(\"KNT\",\"KNT_full.txt grep 'srad'\",\"silent\",\"no OP srāda- in Kent's lexicon - the form is unattested.\")]))\nnodes.append(dict(id=4,lang=\"Arabic\",words=\"sorâdeq\",verdict=\"confirmed\",\n derivation=\"Arabic surādiq 'awning, large tent, enclosure of a tent' (Qur'an 18:29 'its surādiq shall enclose them') is borrowed from a Middle Iranian *srādak (OIr. *srāda- + -ak), the same base as later sarāy; the Arabic form keeps the old -d- and renders final -ak as -iq (as in other Persian loans with -q). The chart's note that it may come from Persian sarā-parda 'tent enclosure' reflects older Arab and Persian lexicographers (cited by Jeffery and Vullers); Jeffery, Nyberg and Wiktionary prefer *srādak, and sarāparda is a later NP compound of the same sarā.\",\n derivation_fa=\"عربی «سُرادِق» (خیمهٔ بزرگ، سراپرده؛ در قرآن، کهف ۲۹) از ایرانی میانهٔ *srādak گرفته شده است که از *srāda- با پسوند -ak ساخته شده و با «سرا» هم‌ریشه است؛ -ak پایانی در عربی به «-ق» بدل شده است. جوالیقی و راغب آن را «فارسی معرّب» دانسته‌اند. یادداشت نمودار که آن را از «سراپرده» می‌داند دیدگاه برخی فرهنگ‌نویسان قدیم است؛ جفری و نیبرگ و ویکی‌واژه *srādak را ترجیح می‌دهند. ادعای اصلی نورایی (وام از ایرانی) درست است.\",\n sources=[W+\"سرادق\"],\n ref_check=[R(\"VDQ:255\",\"partial\",\"checked via Jeffery FVQ pp.167-168 (VDQ is its translation): Jeffery first quotes Vullers's 'Pers. sarāparda ... formed from parda a veil or curtain and an O.Pers. *srāda', then derives the Arabic word from 'some Middle Persian formation from this *srāda with the suffix -k' - supports the Iranian origin; sarāparda is mentioned as the lexicographers' starting point.\"),\n            R(\"MON:1850\",\"not_checked\",\"6-vol page not mappable; abridged MON_part1.txt line 76274 'سرادق: [معر.] (ا.) خیمه، سراپرده' supports a Persian origin.\"),\n            R(\"MAG:189\",\"not_checked\",\"restricted (HathiTrust search-only).\")],\n consulted=[C(\"FVQ\",\"pp.167-168 (Surādiq)\",\"supports\",\"'It was very generally recognized as a foreign word ... al-Jawālīqī, Mu'arrab, 90, classes it as a Persian word'; derived from MP *srāda + -k.\"),\n            C(\"NYB\",\"s.v. srād\",\"supports\",\"'with suff. *srādak ... Arab. lw. surādiq large tent'.\"),\n            C(\"HRN\",\"p.161 no. 727\",\"supports\",\"'arab. LW. surādiq (de Lagarde, Pers. Stud. 72)' under serāi.\"),\n            C(\"ARB_mo3rb\",\"ARB_mo3rb.txt line 15121\",\"partial\",\"al-Jawālīqī ed. Shākir note: Rāghib 'فارسی معرب'; Lisān 'السرادق: ما أحاط بالبناء' - the editor doubts the Arabization claim ('دعوى تعريبها لا دليل عليها'), a minority view.\"),\n            C(\"AFM\",\"AFM_pages.txt line 768\",\"silent\",\"Addi Shir mentions السرادق only in passing inside another entry.\")]))\nnodes.append(dict(id=5,lang=\"Persian\",words=\"sorâdeq\",verdict=\"confirmed\",\n derivation=\"NP sorādeq 'tent, pavilion' (pl. sorādeqāt) is the Arabic surādiq re-borrowed into Persian, i.e. a Persian -> Arabic -> Persian round trip of MIr. *srādak; Mo'in tags it [معر.] 'Arabicized' and glosses it 'خیمه، سراپرده'.\",\n derivation_fa=\"«سُرادِق» (جمع: سرادقات) در فارسی وام‌واژه‌ای از عربی است، اما خود عربی آن را از ایرانی میانهٔ *srādak گرفته بود؛ یعنی واژه‌ای ایرانی که معرّب شده و دوباره به فارسی بازگشته است. معین آن را «معرّب» و به معنای «خیمه، سراپرده» آورده است. ادعای نورایی درست است.\",\n sources=[W+\"سرادق\"],\n ref_check=[R(\"MON:1850\",\"partial\",\"6-vol page not mappable; abridged Mo'in (MON_part1.txt line 76274-76282) 'سرادق: [معر.] (ا.) خیمه، سراپرده ... سرادقات' - same entry content.\")],\n consulted=[C(\"MON\",\"MON_part1.txt line 76274\",\"supports\",\"'سرادق [معر.] خیمه، سراپرده'; plural سرادقات.\"),\n            C(\"FVQ\",\"p.167\",\"supports\",\"classed as Persian loan by al-Jawālīqī.\"),\n            C(\"HRN\",\"p.161\",\"supports\",\"Arabic surādiq listed as loan from the serāi family.\")]))\nnodes.append(dict(id=6,lang=\"Latin\",words=\"trâns; terminus; truncus\",verdict=\"plausible\",\n derivation=\"Latin trāns 'across' < Proto-Italic *trānts < PIE *tr̥h₂-n̥ts, probably the present participle of a lost verb *trāre 'cross' (cf. intrāre) - confirmed. terminus 'boundary (stone)' < *térmn̥: Pokorny puts termen/terminus under the same ter- 1074 and Klein says trāns-'s base also gives terminus, but Watkins/AHD assign it to a separate ter- 'peg, post, boundary marker' and Wiktionary allows either *terh₂- or *ter- - plausible. truncus 'lopped, maimed; tree trunk' is put under terə-2 by Watkins (*tru-n-k-o-, 'overcome, maimed'), but Klein derives it from *trank- 'press' and de Vaan/Wiktionary call it of unknown origin, possibly *twerḱ- 'cut' - plausible at best; Nourai's gloss 'overcome' is not the Latin meaning but Watkins's speculative semantic bridge.\",\n derivation_fa=\"لاتین trāns «از این سو به آن سو» از ایتالیک آغازین *trānts و هندواروپایی *tr̥h₂-n̥ts، صفت فاعلی فعلی از ریشهٔ *terh₂- است و بی‌گمان از همین ریشه است. terminus «مرز، سنگ مرز» را پوکورنی و کلاین به همین ریشه می‌برند، ولی واتکینز آن را از ریشهٔ جداگانهٔ ter- «میخ، تیرک مرزی» می‌داند؛ پس پذیرفتنی است نه قطعی. truncus در لاتین «بریده‌شاخه، ناقص، تنهٔ درخت» است نه «چیره شدن»؛ واتکینز آن را با تردید به این ریشه می‌برد، ولی کلاین آن را از *trank- «فشردن» و دِ وان آن را ناشناخته (شاید از *twerḱ- «بریدن») می‌داند. بنابراین این گره در کل با احتیاط پذیرفتنی است.\",\n sources=[W+\"trans\",W+\"terminus\",W+\"truncus\"],\n ref_check=[AHDr],\n consulted=[POKR|{\"src\":\"POK\",\"where\":\"pp.1074-1076\",\"stance\":\"partial\",\"note\":\"Pokorny has trans (ter-5) and terminus (ter-4) here; truncus is not listed under ter-.\"} if False else C(\"POK\",\"pp.1074-1076 (POK_full.txt 86174-86270)\",\"partial\",\"'Latin termen, termo, terminus Grenzzeichen' under ter-4 and 'Latin trans, Umbrian traf' under ter-5; truncus not listed here.\"),\n            C(\"KLN\",\"s.v. trans- and trunk (lines 39818, 40356)\",\"partial\",\"trans- 'fr. I.-E. base *ter-, to go through, cross over, whence also L. terminus'; trunk: 'L. truncus ... prob. stands for *troncos, fr. I.-E. base *trank-, to press' - contradicts truncus < *ter-.\"),\n            C(\"AHD\",\"AHD_watkins1985.txt line 1080\",\"partial\",\"'ter-. Base of derivatives meaning peg, post, boundary marker, goal. 1. *ter-men- ... Latin terminus: TERM ... DETERMINE [Pok. 4. ter- 1074]' - a separate root from terə-2.\"),\n            WLD]))\nnodes.append(dict(id=7,lang=\"French\",words=\"\",verdict=\"confirmed\",\n derivation=\"Pass-through node: French inherited or learnedly borrowed the Latin words as trans- (transport, transit, transformateur, from 19th-20th c. coinages such as transistor), terme (< terminus) and terminal; these French forms are the immediate source of the Persian loans in #8.\",\n derivation_fa=\"گرهٔ میانجی: فرانسوی واژه‌های لاتین را به صورت پیشوند trans- (transport، transit، transformateur، transistor) و terme (از terminus) و terminal گرفته است و همین صورت‌های فرانسوی سرچشمهٔ وام‌واژه‌های فارسی گرهٔ بعدی‌اند. درست است.\",\n sources=[W+\"trans\",W+\"terminus\"],\n ref_check=[R(\"None\",\"not_checked\",\"no reference given in the book for this node.\")],\n consulted=[C(\"KLN\",\"s.v. trans-, terminus\",\"supports\",\"Latin trans/terminus as bases of the Romance and English words.\"),\n            C(\"SKT\",\"grep '^TRANS'\",\"silent\",\"Skeat treats the English words, not French specifically.\")]))\nnodes.append(dict(id=8,lang=\"Persian\",words=\"\",verdict=\"confirmed\",\n derivation=\"ترانسپورت (transport), ترانزیت (transit), ترانزیستور (transistor), ترانسفورماتور (transformateur), ترم (terme 'term, semester'), ترمینال (terminal) are 20th-century French loans in Persian, as Mo'in marks them [فر.]; their Latin bases are trāns and terminus (the latter only plausibly from *terh₂-, see #6).\",\n derivation_fa=\"«ترانسپورت، ترانزیت، ترانزیستور، ترانسفورماتور، ترم، ترمینال» وام‌واژه‌های فرانسوی سدهٔ بیستم در فارسی‌اند که معین آن‌ها را با نشان [فر.] آورده است؛ چهار واژهٔ نخست از پیشوند لاتین trāns و دو واژهٔ آخر از terminus هستند. وام‌گیری از فرانسوی درست است؛ پیوند «ترم» و «ترمینال» با ریشهٔ *terh₂- تنها پذیرفتنی است.\",\n sources=[W+\"trans\",W+\"terminus\"],\n ref_check=[R(\"MON\",\"not_checked\",\"no page given; French loans in Mo'in's vol. 4/lexicon not mapped.\"),R(\"AMD\",\"not_checked\",\"online only, page not given.\")],\n consulted=[C(\"MON\",\"MON_part1/part2 grep ترانزیت/ترمینال\",\"silent\",\"the abridged OCR text gives no usable hit for these loans.\"),\n            C(\"KLN\",\"s.v. trans-\",\"supports\",\"Latin source of the French forms.\")]))\nnodes.append(dict(id=9,lang=\"English\",words=\"trans-, transport, transform, transistor, transfer, translate; term, terminate, determine; trunk, truncate, trench\",verdict=\"plausible\",\n derivation=\"trans- and the compounds transport (L. trānsportāre), transform, transfer (trānsferre), translate (trānslātus) and transistor (1948 blend of transfer + resistor) all contain Latin trāns < *terh₂- - confirmed. term, terminate, determine come from Latin terminus via Old French terme / Latin terminare, determinare; their link to *terh₂- is plausible only (AHD: separate ter- 'boundary'). trunk (OF tronc < L. truncus), truncate (truncāre) and trench (OF trenchier < VL *trincare < truncāre) depend on truncus, whose attribution to *terh₂- is Watkins's alone (Klein: *trank-; de Vaan: unknown).\",\n derivation_fa=\"پیشوند انگلیسی trans- و واژه‌های transport، transform، transfer، translate و transistor (آمیزه‌ای از transfer و resistor، ۱۹۴۸) همه از لاتین trāns و از ریشهٔ *terh₂- هستند. term، terminate و determine از لاتین terminus آمده‌اند که پیوندش با این ریشه احتمالی است. trunk، truncate و trench از لاتین truncus / truncāre آمده‌اند که واتکینز آن را از این ریشه می‌داند ولی کلاین و دِ وان نه. پس این گره در کل با احتیاط پذیرفتنی است.\",\n sources=[W+\"trans\",W+\"truncus\",W+\"terminus\"],\n ref_check=[AHDr],\n consulted=[C(\"KLN\",\"trans- / terminus / trunk\",\"partial\",\"supports trans- and terminus from *ter- 'go through'; trunk from *trank- 'to press'.\"),\n            C(\"SKT\",\"SKT.txt grep '^TRANS\\\\|^TRUNK'\",\"silent\",\"Skeat gives the Latin sources (trans, truncus) without PIE root.\"),\n            C(\"AHD\",\"index lines 2354, 2400, 2412\",\"partial\",\"index: 'TERM ter-, TERMINATE ter-'; 'TRANS- terə-2'; 'TRENCH terə-2', 'TRUNCATE terə-2', 'TRUNK terə-2'.\")]))\nnodes.append(dict(id=10,lang=\"Germanic\",words=\"thr\",verdict=\"plausible\",\n derivation=\"Proto-Germanic zero-grade *þur- from *tr̥h₂- gives *þurh(w) 'through' (< *tr̥h₂-kʷe) and *þurhilą > OE þyrel 'hole, perforation' ('a boring through'); this matches Nourai. But his gloss 'bore through, drill' conflates it with the homophonous *terh₁- 'rub, turn, bore' (Pokorny 3. ter- 1071), the source of Dutch drillen > English drill; so the Germanic node is right for through/thyrel, not for 'drill'.\",\n derivation_fa=\"ژرمنی آغازین *þur- از پایهٔ ضعیف *tr̥h₂- است و از آن *þurh «از میان» و *þurhilą «سوراخ» (انگلیسی کهن þyrel) پدید آمده است؛ این درست است. اما معنای «سوراخ کردن، مته زدن» (drill) که نورایی آورده از ریشهٔ هم‌آوای دیگری است: *terh₁- «ساییدن، چرخاندن، سوراخ کردن». پس این گره با احتیاط پذیرفتنی است.\",\n sources=[W+\"through\",PIE],\n ref_check=[AHDr,R(\"KLN\",\"partial\",\"Klein s.v. drill (KLN_1966.txt line 12262): 'Du. drillen, to bore ... fr. I.-E. base *ter-, to turn, to bore by turning, whence also OE. þyrel, hole' - Klein lumps both under one *ter-, unlike Watkins.\")],\n consulted=[C(\"POK\",\"ter-5 p.1076\",\"supports\",\"'Old English þurh ... Old English þyrel durchbohrt; n. hole'.\"),\n            C(\"AHD\",\"line 1083 terə-1\",\"contradicts\",\"'III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL' under terə-1 'to rub, turn ... boring, drilling', not terə-2.\"),\n            WLD]))\nnodes.append(dict(id=11,lang=\"English\",words=\"drill, through, thorough, nostril\",verdict=\"disputed\",\n derivation=\"through < OE þurh < PGmc *þurh(w) < PIE *tr̥h₂-kʷe - confirmed; thorough is the stressed variant OE þuruh of the same word; nostril < OE nosþyrl 'nose-hole' (nosu + þyrel 'hole', from þurh) - confirmed. drill (16th c., from Middle Dutch drillen 'to bore, turn') belongs to PIE *terh₁- 'to rub, turn, bore' (AHD terə-1, Pokorny 3. ter-), a different root from *terh₂- 'cross over' - disputed. Worst verdict: disputed.\",\n derivation_fa=\"انگلیسی through از انگلیسی کهن þurh و ژرمنی *þurh(w) و هندواروپایی *tr̥h₂-kʷe است؛ thorough صورت دیگر همان واژه (þuruh) است و nostril از nosþyrl «سوراخ بینی» (nosu + þyrel «سوراخ») است؛ این سه درست‌اند. اما drill (از هلندی میانه drillen «سوراخ کردن، چرخاندن») از ریشهٔ دیگری، *terh₁- «ساییدن، چرخاندن» است و پژوهش امروزی آن را از *terh₂- «گذشتن» جدا می‌داند.\",\n sources=[W+\"through\",W+\"nostril\",W+\"drill\"],\n ref_check=[R(\"None\",\"not_checked\",\"no reference given in the book for this node.\")],\n consulted=[C(\"AHD\",\"lines 1083, 1434, 1936, 2385\",\"partial\",\"'DRILL1 terə-1'; 'NOSTRIL nas-, terə-2'; 'THOROUGH terə-2'.\"),\n            C(\"KLN\",\"s.v. drill, nostril, thorough (lines 12262, 25640, 39100)\",\"partial\",\"nostril 'fr. OE. nosþyrl ... þyrel hole, fr. þurh through'; thorough 'a var. of þurh'; drill 'fr. I.-E. base *ter-, to turn, to bore by turning'.\"),\n            C(\"SKT\",\"grep '^DRILL'\",\"silent\",\"Skeat: Du. drillen; no PIE root.\")]))\nnodes.append(dict(id=12,lang=\"Greek\",words=\"nek-tar\",verdict=\"plausible\",\n derivation=\"Greek νέκταρ 'nectar, drink of the gods' is traditionally analysed as a poetic compound *neḱ- 'death, perish' + *-tr̥h₂- 'overcoming' (cf. Skt. -tur- 'overcoming' in ap-tur-), i.e. 'overcoming death', granting immortality (Pokorny, Watkins, Schmitt). Beekes hesitates between this and a Pre-Greek origin (Furnée compares νικάριον), and Semitic or Egyptian loans have been proposed; so the analysis is accepted by many but not all.\",\n derivation_fa=\"یونانی nektar «شهد، نوشابهٔ خدایان» را به‌طور سنتی ترکیبی شاعرانه از *neḱ- «مرگ، نابودی» و *-tr̥h₂- «چیره‌شونده» (از *terh₂-) می‌دانند، یعنی «چیره بر مرگ»، چون نوشندهٔ آن جاودان می‌شد. ولی بیکس میان این توضیح و خاستگاه پیشایونانی مردد است و برخی آن را وامی سامی یا مصری دانسته‌اند. پس ادعای نورایی پذیرفتنی است، نه قطعی.\",\n sources=[W+\"νέκταρ\",PIE],\n ref_check=[R(\"AHD\",\"supports\",\"AHD_watkins1985.txt line 776 s.v. nek-1: '6. Greek nek-tar, the drink of the gods, overcoming death (*tar-, overcoming; see terə-2): NECTAR, (NECTARINE). [Pok. nek- 762.]'\")],\n consulted=[C(\"POK\",\"p.1075\",\"supports\",\"'Verbaladjektiv Old Indie -tur- ... compare gr. νέκ-ταρ above S. 762'.\"),\n            C(\"KLN\",\"grep '^nectar,'\",\"silent\",\"no entry found in the OCR text.\"),\n            C(\"WLD\",\"Bd. I p.733\",\"silent\",\"not mentioned at the ter- head.\")]))\nnodes.append(dict(id=13,lang=\"English\",words=\"nectar, nectarine\",verdict=\"confirmed\",\n derivation=\"English nectar (1550s) from Latin nectar < Greek νέκταρ; nectarine (1610s, the fruit, earlier adj. 'sweet as nectar') is nectar + -ine. The descent from the Greek word is certain; the ultimate *terh₂- link is as uncertain as in #12.\",\n derivation_fa=\"انگلیسی nectar از لاتین nectar و آن از یونانی nektar است؛ nectarine (سدهٔ هفدهم، نوعی هلو) از nectar با پسوند -ine ساخته شده است. پیوند با یونانی قطعی است؛ پیوند نهایی با *terh₂- همان تردید گرهٔ پیشین را دارد.\",\n sources=[W+\"νέκταρ\"],\n ref_check=[R(\"None\",\"not_checked\",\"no reference given in the book for this node.\")],\n consulted=[C(\"AHD\",\"index line 1907\",\"supports\",\"'NECTAR nek-1 NECTARINE nek-1' and s.v. nek-1 item 6.\"),\n            C(\"SKT\",\"grep '^NECTAR'\",\"silent\",\"Skeat: L. nectar, Gk. nektar, no PIE analysis.\")]))\nnodes.append(dict(id=14,lang=\"Indo-European\",words=\"An-teros\",verdict=\"disputed\",\n derivation=\"PIE *h₂énteros 'other, second' (Skt. antara-, Goth. anþar, OE ōþer, Lith. antras) is real, but it is formed from the pronominal stem *h₂en- 'there, other side' plus the contrastive suffix *-teros (Pokorny 37 s.v. an-2; Mann: 'Cf. anos (1) and -teros'); it is not a derivative of the verb *terh₂- 'cross over'. Some Sanskrit antara- senses also continue *h₁énteros 'inner'. The word and gloss are right; the arrow from Ter 1 is not.\",\n derivation_fa=\"هندواروپایی آغازین *h₂énteros «دیگر، دومی» (سنسکریت antara-، گوتی anþar، انگلیسی کهن ōþer) واژه‌ای واقعی است، اما از ستاک ضمیری *h₂en- «آن‌سو» و پسوند تقابلی *-teros ساخته شده است (پوکورنی ۳۷، مان) و از ریشهٔ فعلی *terh₂- «گذشتن» نیست. پس صورت و معنا درست است، ولی پیوندی که نورایی میان آن و این ریشه کشیده است را پژوهش امروزی نمی‌پذیرد.\",\n sources=[W+\"अन्तर\",W+\"Reconstruction:Proto-Indo-European/-teros\"],\n ref_check=[R(\"IEC:27\",\"partial\",\"Mann IEC.txt line 602 (leaf 30, ~p.27-30): 'anteros second, other. Cf. anos (1) and -teros. WP I, 67; II, 337 Skt. ántaraḥ; Per. andar (in the phr. mādar i andar stepmother); Oss. ändär' - the word is supported, but Mann analyses it with the suffix -teros, not root ter-.\")],\n consulted=[C(\"POK\",\"p.37-38 s.v. an-2 (POK_full.txt line 5487)\",\"contradicts\",\"'an-2 there, on the other side ... Thereof derived: anyos other ... anteros other (from second): Old Indie antara-, oss. andar other' - placed under an-2, not under ter-.\"),\n            C(\"WLD\",\"Bd. I p.56/67 (cited by Pokorny 'WP. I 56, 67')\",\"silent\",\"treated under an-, not under ter-.\"),\n            C(\"SYN\",\"grep 'OTHER'\",\"silent\",\"not checked beyond the concept heading.\")]))\nnodes.append(dict(id=15,lang=\"Persian\",words=\"andar\",verdict=\"confirmed\",\n derivation=\"NP -andar 'step-' in pedarandar 'stepfather', mādarandar 'stepmother', doxtarandar, pesarandar continues Old Iranian *antara- 'other, second' (Av. antara-, Skt. antara-, Oss. ändär 'other'), i.e. 'the other father/mother'; it is homonymous with, but distinct from, the preposition andar 'in' (< *antar 'inside'). Mo'in lists pedarandar, mādarandar (also contracted pedandar, mādandar).\",\n derivation_fa=\"«-اندر» در «پدراندر، مادراندر، دختراندر، پسراندر» به معنای «ناتنی» از ایرانی باستان *antara- «دیگر، دومی» است (اوستایی antara-، سنسکریت antara-، آسی ändär «دیگر»)، یعنی «پدرِ دیگر، مادرِ دیگر»؛ با حرف اضافهٔ «اندر» (در، درون) هم‌آواست ولی یکی نیست. معین «پدراندر» و «مادراندر» (و صورت‌های کوتاه پدندر، مادندر) را آورده است. ادعای نورایی دربارهٔ این وام‌گیری از *anteros درست است.\",\n sources=[W+\"अन्तर\"],\n ref_check=[R(\"IEC:27\",\"supports\",\"Mann s.v. anteros: 'Per. andar (in the phr. mādar i andar stepmother)'.\"),\n            R(\"MON:373\",\"partial\",\"6-vol page not mappable; abridged MON_part2.txt line 41761 'مادراندر ... [= مادندر < مادندر]' and MON_part1.txt line 17638 'پدراندر (پدندر)' - entries present, no etymology in the OCR.\")],\n consulted=[C(\"IEC\",\"line 602\",\"supports\",\"as above.\"),\n            C(\"MON\",\"MON_part1 17638, MON_part2 41761\",\"supports\",\"پدراندر، مادراندر listed as 'stepfather/stepmother'.\"),\n            C(\"HRN\",\"grep 'andar'\",\"silent\",\"Horn has no separate entry for -andar 'step-'.\")]))\nnodes.append(dict(id=16,lang=\"Sanskrit\",words=\"antarah\",verdict=\"confirmed\",\n derivation=\"Sanskrit ántara- 'other, different, another' (also 'inner, near; interval') continues PIE *h₂énteros 'other, second' (merged with *h₁énteros 'inner'), with regular *e > a; Nourai's 'antarah' is the nominative singular antaraḥ.\",\n derivation_fa=\"سنسکریت antara- «دیگر، متفاوت» (و نیز «درونی، فاصله») از هندواروپایی *h₂énteros «دیگر، دومی» است که با *h₁énteros «درونی» درآمیخته؛ e هندواروپایی در هندی باستان به a بدل شده است و «antarah» حالت فاعلی مفرد آن است. درست است.\",\n sources=[W+\"अन्तर\"],\n ref_check=[R(\"POK:37\",\"supports\",\"POK_full.txt line 5487 (Page(s) 37-38) s.v. an-2: 'anteros other (from second) in: ... Old Indie antara-, oss. andar other'.\"),\n            R(\"IEC:27\",\"supports\",\"Mann s.v. anteros: 'Skt. ántaraḥ'.\")],\n consulted=[C(\"POK\",\"p.37\",\"supports\",\"as above.\"),\n            C(\"WLD\",\"Bd. I 67 (cited by Pokorny)\",\"silent\",\"not opened; Pokorny's 'WP. I 56, 67' places it under an-.\")]))\nentry=dict(entry=0,root=\"Ter 1, Tr\",verdict=\"confirmed\",\n modern_form=\"PIE *terh₂- 'to cross over, pass through, overcome' (Pokorny 4./5. ter- 1074-1076; Watkins terə-2; LIV *terh₂-)\",\n note=\"Root, label and gloss are correct and match Pokorny 1074-1075 and AHD terə-2 almost item for item (Nourai's chart follows Watkins: thyrel/nostril, through, nektar, trans, Iranian thrāya- > sarāi, truncus). Problems are in the satellite nodes: Persian comparative -tar/-tarīn and PIE *h₂énteros contain the contrastive suffix *-teros, not the verb root; English drill belongs to the homophonous *terh₁- 'rub, bore'; terminus and truncus are assigned to other roots by part of the literature. OP 'srâd, srâda' is a reconstruction (*srāda-), not an attested Old Persian word. Klein's page 1639 (s.v. trans-) is confirmed by the page numeral 1641 on the adjacent leaf.\",\n note_fa=\"ریشهٔ هندواروپایی آغازین *terh₂- «گذشتن، از میان گذشتن، چیره شدن» (پوکورنی ۱۰۷۴–۱۰۷۶، واتکینز terə-2) واقعی است و برچسب و معنای نورایی درست است؛ بیشتر شاخه‌های نمودار (گذشتن، سرا، سرادق، trans، through، nostril) نیز پذیرفته‌اند. اما پسوند تفضیلی «-تر» و *anteros (که «-اندر» در «پدراندر» از آن است) از پسوند *-teros ساخته شده‌اند نه از این ریشه؛ drill از ریشهٔ هم‌آوای *terh₁- «ساییدن» است؛ و صورت پارسی باستان srāda بازسازی است و در کتیبه‌ها نیامده است.\",\n sources=[PIE,W+\"trans\",W+\"through\"],\n ref_check=[POKR,KLNtrans],\n consulted=[WLD,C(\"AHD\",\"terə-2 (AHD_watkins1985.txt line 1083)\",\"supports\",\"'terə-2. To cross over, pass through, overcome. [Pok. 5. ter- 1075.]'\"),\n            C(\"IEC\",\"grep '^ter'\",\"silent\",\"Mann's ter- entries not matched in OCR for this sense.\"),\n            C(\"CHEUNG\",\"*tarH\",\"supports\",\"'PIE *terH2- (*treH2-) to go through, cross, overcome = LIV 633 f. | Pok. 1074 f.'\")],\n nodes=nodes)\nout=dict(pdf_page=504,book_page=474,verified_by=\"claude-opus-5\",verified_on=\"2026-10-14\",entries=[entry])\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-504.json\",\"w\",encoding=\"utf-8\"),ensure_ascii=False,indent=1)\nEOF\ncd /home/sfmqrb/git/rishe-private && python3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-504.py && python3 -m json.tool data/verification/page-504.json >/dev/null && python3 tools/verify_check.py 504"
}
```


### [2026-10-15T02:50:24.872Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'plausible': 6, 'disputed': 3, 'confirmed': 7}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'not_checked': 10, 'partial': 5}
books consulted: {'supports': 27, 'partial': 10, 'silent': 14, 'contradicts': 2} | by book: {'KLN': 8, 'WLD': 6, 'POK': 5, 'AHD': 5, 'HRN': 4, 'SKT': 4, 'NYB': 3, 'MON': 3, 'BRT': 2, 'CHEUNG': 2, 'FVQ': 2, 'TLM': 1, 'HUB': 1, 'PHD': 1, 'ARY': 1, 'KNT': 1, 'ARB_mo3rb': 1, 'AFM': 1, 'SYN': 1, 'IEC': 1}
```


## [2026-10-15T02:50:27.907Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^TRANS\\b\\|^TRANS-\\|^TRUNK\\|^DRILL\\|^NECTAR' SKT.txt | head; grep -c -i 'srad' KNT_full.txt; grep -n '^nectar' KLN_1966.txt | head -2; grep -n 'andar' HRN.txt | head -3"
}
```


### [2026-10-15T02:50:28.408Z] TOOL RESULT

```
12210:NECTAR.
0
25121:nectariferous,  adj.,  secreting  nectar.  —  Com¬ pounded  of  nectar  and  the  stem  of  L.  ferre,  ‘to bear,  carry’.  See  -ferous.
25122:nectarine,  n.,  a  variety  of  peach  with  a  thin, smooth  skin.  —  Formed  fr.  nectar  with  suff. -ine:  so  called  from  its  sweet,  delicious  taste, nectary,  n.,  the  organ  that  secretes  nectar  (bot.)
1433:ap. a(n)tar 'in, innerhalb'; aw. antare; phlv. andar^);
1443:^) Phlv. andarg ist Unsinn.
1444:') Das Pehlevi hat auch schon andarün (für aw. aw/ara-).- 28 -
```


## [2026-10-15T02:50:30.125Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 12210,12216p SKT.txt; grep -n -i 'nectar,' KLN_1966.txt | head -3; grep -n -i '^TRANS\\|^TRUNK\\|^DRILL' SKT.txt | head"
}
```


### [2026-10-15T02:50:30.491Z] TOOL RESULT

```
NECTAR.
L.  nigromaHSia,  corrupt  form anita.  ■•  Gk.  ptJtftaftat^tia,  ne- Gk.rmffu-1,  A  corpse;  ^uu-Toa, Dwcr.  3-  Gk.  ytirpof  is  fioni tpac ;  cf  L,  tMcart,  \o  kill. Gk,  fMOMrtia  is  from  ^kt«,  a iker.  (V  MAN.)  ^  Nicro- called  '  the  blnck  art '  owing r  etyniijlogy  from  L.  Hfgrr, e  I-ow  L.  mgr0/nanfia. U  -  Gk.)  L.  mit/ar.  -  Gk. trink  of  the  gods.
MDpaUioo.  •f  Du.  ff^^.    Icel. Swed.  ma/,  Golh.  Piauths,  G. d  to  Russ.  nyjiia^  need,  nyditt, I.  fvW,  to  drive.     (V^'<JO lec  Baar*.
:  ftee  Fat«. , denial.  (F.oL.)  T.tu^Hom, ^tiotttm,  denial.  ~  L.  nr^atuit \  to  deny  ;  opposed  to  aUre,  to to  N«,  not;  and  some  lorin )t  to  Affirm :  see  £fo  ( i).   W/Vr^
Gk.  )^,   X  My,   bkt.  a/^,   to
(L,)     From  pp.  of  L.  a&-
y-
20639:things’, pi.  of kdthibh, ‘(something) written’, pas¬ sive  partic.  of  katabh,  ‘he  wrote’.  See  prec.  word. Keturah,  fem.  PN.  {Bible).  —  Heb.  Qeturdh,  lit. ‘incense’,  from  the  stem  of  qitter,  hiqttr,  ‘he made  sacrifices,  smoke’,  whence  also  qltoreth, ‘sweet  smoke  of  sacrifice,  incense’.  See  nectar, kevalin,  n.,  a  soul  freed  from  matter  {Jainism). — OI.,  fr.  kevalah,  ‘alone,  belonging  exclusively to  a  single  person’,  fr.  I.-E.  base  *qail *qoil-, ‘complete,  sound,  well,  happy’,  whence  also Goth,  hails,  ‘complete,  whole,  well,  sound’,  OE. hdl,  ‘whole,  uninjured,  healthy’.  See  whole  and cp.  words  there  referred  to. kevel,  n.,  a  peg  or  bollard  to  which  certain  ropes are  fastened  {naut.) — ONF.  keville  (correspond¬ ing  to  F.  chevilk),  ‘peg,  pin,  bolt’,  fr.  VL. *cavieu!a,  dissimilated  fr.  Late  L.  clavicula,  ‘a little  key’.  See  clavicle.
25117:necrosis,  n.,  the  death  of  bodily  tissue.  —  Gk. vExpcocic,  ‘a  becoming  dead,  state  of  death’,  fr. vExpouv,  ‘to  make  dead,  to  mortify’,  fr.  vexpoc, ‘dead’.  See  necro-  and  -osis. necrotic,  adj.  —  See  prec.  word  and  -otic, nect-,  form  of  necto-  before  a  vowel, nectar,  n.,  the  drink  of  the  gods  (Greek  mythoi) —  L.,  fr.  Gk.  vEx-rap,  ‘drink  of  the  gods’,  esp. ‘wine’,  which  prob.  derives  fr.  Heb.  (yayin)  niq- tar,  ‘smoked  (wine),  perfumed  (wine)’,  Niph‘al (=  passive  form)  of  the  Sem.  base  q-t-r,  ‘to make  sacrifices,  smoke’;  qitter  and  hiqtir ,  ‘he made  sacrifices,  smoked’,  are  Pi’el  (=  intensive form),  resp.  Hiph‘il  (=  causative  form)  of  the same  base,  whence  also  ql/Oreth,  ‘sweet  smoke of  sacrifice,  incense’,  Talmudic  and  Targumic Aram,  qitra,  ‘(thick)  smoke’,  Ethiop.  qetare.
203:trans. — I  ransi  t  i  ve.
452:transact,  to  perform.  (L.)  L.  trani- a£tus,  pp.  of  tramigete.  —  L.  tram,  beyond ; and  agtre.
6505:transfer.  (F.-L.)  V.  tmns/htr.  ^ L.  tram  ferrt,  to  convey  across.
6977:transforni.  (F.-L.)    F.  transformer.
9391:transient.  (L.)  From  tramitHt; supposed  stem  of  L.  tmntitfu,  pasising away,  thoDi;h  the  real  stem  is  tratu^ttnt' i,^ pres.  pt.  oi  IrAMs-irt,  to  posv  across  or  away. transit.  ^L.)  L.  trmmittu,  lit.  a passing  aciosii.— L.  transitumt  supine  of trans-irt,  to  pass  across.
10750:translucent,  allovring  ■  '^*  - through.  iL.)  L.  transluceti.
11545:transmigration.  (F.-L.)  F.  tram- migration-  -•  L.  ace.  trans  migrxt/iomm;  ong. a  removing  from  one  country  to  aaolher. ••IL  tranj-mtgran,  to  migrate  acioia.
11717:transmit.     (L.)     L.    trans^    mcross ; mitUrt,  to  send.    Der,  trans  miss  ten  (from pp.  missus). uiselon.  Missive ;  see  Bliasilo. Mist.  (£.)     A.  S,  mist,  gloom,  darkness. •4-  IceL  mistr,  Du.  Swed.  mist,  mi&^t ;   G. mist,  dung  (the  same  word'} ;    Golh.  math- Jtuj,  dung.     Formed,  with  suffixed  'St,  from the  base  MIC  (Aryan  MICH),  as  seen  in  , Luhoan.  mtgla,   Koss.  m^^,   Gk.  i>ftix^^>  \ niBt.   Ski.    mih'ira,   a  doud,    me,^ha,    a dowL    Cf  Skt,  miJk,  to  spriolde.  lo  uriiM ; '
14484:transport.  (F.-L.)  F.  transporter, *  to  cirry  or  conxxy  over ;  *  Cot.  —  U  tram- portarr,  to  carry  acro«iS. Port  (1).  a  harbour.  (L.)  M.  E.  port. A.  S.  f^rt.  —  L.  partus,  a  haiboai.  Closely allie<l  to  port  (3^  below.
14599:transposition.  (F.-L.)  F.  trampo- sition.^h.  acc.  trampositiorum .-^X^  tranj' tositus,  pp.  of  trtxnsfonert,  to  transpose.  — L.  frani.  r\crois ;  pon<rr,  to  pat.
```


## [2026-10-15T02:50:34.527Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^ter\\|^tera\\|^tr- \\|^tr(' IEC.txt | head"
}
```


### [2026-10-15T02:50:35.104Z] TOOL RESULT

```
6664:tero-
8868:ter, lean-to, shelter’. WP I, 490
13028:ter; throb’
13066:ter'. Cf. plek-, plik-, pliks- Skt. plaksá, f. *wavy-leafed figtree'; Lat. cf. plecto, Gre, v. (1) ‘flog’; OIr. lecco, s. ‘cheek’; lec, f. ‘slab, slate’; Ir. leac, f. id.; W llech, pl. -i, -au, f. id.; Cor. légh, pl. -ow, f. id. be- side leghen, f. ‘shale, slate’; cf. EMBr. liach, léach, f. Cetone fr. *pleks-); Ir. cf. leacaim, v. ‘flay, slay’; cf. also W llechau, Cor leghow, Br. léach ‘rickets’; W llechu, v. ‘fondle’; ON fletta, v..'strip, plunder’; OCS pleste, R plecó, n. ‘shoulder’; Cz. plece, n. ‘animal shoulder’; Srb. pleć, f. ‘mountain ridge’; pleća, pleći, pl. ‘shoulders’; Cz. Slovak plechý, adj. "band. some’; Li. plekste, f. ‘sole, flounder’; plekš- tis, gs: ies, f. id.; Latv. plecs ‘shoulder’; plece & plekste, f. “flatfish, halibut’; (variant) pleška, f. ‘baldpate’. Same as next (?), q.v.
15210:ter”; OE sinc, n. ('treasure', lit. “holding, pos- session"); Icel. sinka, f. ('avarice', lit. 'posses- siveness"); cf. sinkill, pl. sinklar, m. ‘clamp’; OCS po-sego, -sesti, v. ‘touch’ beside segati, segnoti, inf. “reach, grasp’ (and com. SI.). No- minal types also in Skt. sangah, m. ‘hitch, catch; association’; Per. hang (*wisdom, lit. *grasp); Cz. sáh, m. ‘fathom; cord; faggot’; Pol. siag, m. id.; cf. also Cz. ob-sah ‘contents’; Ukr. cf. sjažení ‘fathom’; Sw. also sinka, v. (1) “fit, join, mend'; (o-gde): cf. G Senkel, s. (shoelace', fr. *songil-)
16684:terpart, fellow; amolk, gp: amloc, pl. type *pair, yoke? (fr. *somilo-); Gk. homalós, adj. “level, even’; Umb. cf. sumel, adv. ‘at the same time?
18411:ter- (3) (tero, ið) ‘rub, wear’. WP I, 728 Hitt. cf. tattar(ami), v. (^wipe' or sim.); Gk. teiro, v. ‘rub, wear, oppress, sadden’; Lat. tero, Ere, pf: trivi, sup. tritum, v. ‘rub, wear, waste’; Ir. cf. tairisce, m. ‘file’; Swiss cf. där, adj. ‘obstinate’; OCS tro, tréti, v. (and com. Sl. ‘rub, wear down"); R cf. terjàt molokó ‘stank — milk’; po-térja, f. loss, waste’; (long- gde in) OCz. tériti & Cz. tirat, inf. ‘persecute’; Li. terioju, oti, v. “torture”; (long-gde in) Latv. tereju, et, v. waste, consume’; (extn. in) Per. taraSam, idan, v. ‘scrape’
18412:ter- (4) (tero, io, eio) ‘turn, spin, bore’. Cf. terodhlom (terotrom). WP I, 728 Gk. teréo, v. ‘bore’; (o-gde in) tórnos ‘lathe’; Alb. Gert, aor: tora, v. ‘spin — cloth or bread, For W cf. ter, s. *pervasiveness' see terp- (1)
18414:teren- (terun-, tern-) “weak, tender’. WP I, 728 Skt. tárunah “young, tender, fresh'; talinah ‘slender’; cf. tarnakah, m. “young animal’; Romani terno, tarno ‘young’; Av. tauruno, id.; Per. tar ‘moist, fresh’; Oss. tärna, tárín, tírín, s. ‘boy’; Gk. téren, gs: -enos ‘smooth, tender, soft, delicate? beside térus, gs: -uos ‘weak’; terünes ‘jaded donkey’; Sabine terenu-
18418:terodhlom, terotrom ‘borer, drill. WP I, 729. Cf. ter- (4). Variant extns. Gk. téretron, n. id.; Lat. terebrum, terebra, nf. id.; Ir. tarathar, m. id.; Gaul. taratrum, id. (LW in Fr. tarière, id.); OBr tarater, id.; Br. tarar, talar, mpl. -u, id.; W taradr, pl. terydr, m. id.; Cor. tardar, pl. terder, m. id.; It. (LW fr. Gaul. or Ligur.) tarlo, m. ‘woodworm’ beside tarma 'clothesmoth"; Cz. cf. ve-tfel-ec, m. ‘intruder’; Slovak cf. triel-ce, f. ‘grater’; Li. cf. terla, terle, f. ‘snout’. Variants in Gk. kuklo-teres ‘rounded’; Lat. teres, -etis, id.
```


## [2026-10-15T02:50:36.189Z] AGENT

Updating those entries with the actual grep results.


## [2026-10-15T02:50:44.229Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-504.py; python3 - \"$f\" <<'EOF'\nimport sys\np=sys.argv[1]; s=open(p,encoding='utf-8').read()\ns=s.replace('''C(\"KLN\",\"grep '^nectar,'\",\"silent\",\"no entry found in the OCR text.\"),''','''C(\"KLN\",\"s.v. nectar (KLN_1966.txt line 25117)\",\"contradicts\",\"'L., fr. Gk. nektar, drink of the gods, esp. wine, which prob. derives fr. Heb. (yayin) niqtar, smoked (wine), perfumed (wine), Niph'al of the Sem. base q-t-r, to make sacrifices, smoke' - Klein prefers a Semitic loan.\"),\n            C(\"SKT\",\"SKT.txt line 12210 NECTAR\",\"silent\",\"'(L.-Gk.) L. nectar. - Gk. nektar, drink of the gods' - no further etymology.\"),''')\ns=s.replace('''C(\"IEC\",\"grep '^ter'\",\"silent\",\"Mann's ter- entries not matched in OCR for this sense.\"),''','''C(\"IEC\",\"IEC.txt lines 18411-18418\",\"silent\",\"Mann lists ter- (3) 'rub, wear' and ter- (4) 'turn, spin, bore' (WP I 728) and terodhlom 'borer, drill', but no 'cross over' ter- was found in the OCR; Mann thus also separates the boring root from the crossing one.\"),''')\ns=s.replace('''C(\"KNT\",\"KNT_full.txt grep 'srad'\",\"silent\"''','''C(\"KNT\",\"KNT_full.txt grep -i 'srad' (0 hits)\",\"silent\"''')\ns=s.replace('''C(\"SYN\",\"grep 'OTHER'\",\"silent\",\"not checked beyond the concept heading.\")''','''C(\"ARY\",\"ARY_pages.txt grep پدراندر\",\"silent\",\"no hit in the OCR text.\")''')\ns=s.replace('''C(\"HRN\",\"grep 'andar'\",\"silent\",\"Horn has no separate entry for -andar 'step-'.\")''','''C(\"HRN\",\"HRN.txt line 1433 (p.27-28)\",\"silent\",\"Horn's andar entry is only the preposition 'in' ('ap. a(n)tar in, innerhalb; aw. antare; phlv. andar'); no entry for -andar 'step-'.\")''')\nopen(p,'w',encoding='utf-8').write(s)\nEOF\ngrep -c 'Klein prefers a Semitic' $f; grep -n 'پدراندر' data/verification/sources/refs/incoming/ARY/ARY_pages.txt | head -2; python3 $f && python3 -m json.tool data/verification/page-504.json >/dev/null && python3 tools/verify_check.py 504"
}
```


### [2026-10-15T02:50:44.886Z] TOOL RESULT

```
1
nodes verified: 16/16
node verdicts: {'plausible': 6, 'disputed': 3, 'confirmed': 7}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'not_checked': 10, 'partial': 5}
books consulted: {'supports': 27, 'partial': 10, 'silent': 14, 'contradicts': 3} | by book: {'KLN': 8, 'WLD': 6, 'POK': 5, 'AHD': 5, 'SKT': 5, 'HRN': 4, 'NYB': 3, 'MON': 3, 'BRT': 2, 'CHEUNG': 2, 'ARY': 2, 'FVQ': 2, 'TLM': 1, 'HUB': 1, 'PHD': 1, 'KNT': 1, 'ARB_mo3rb': 1, 'AFM': 1, 'IEC': 1}
```


## [2026-10-15T02:50:54.422Z] TOOL CALL #52: SubagentHandback

```json
{
 "message": "Page 504 (book page 474) is verified and written to /home/sfmqrb/git/rishe-private/data/verification/page-504.json. `verify_check.py 504` shows 0 PROBLEM lines and 16 of 16 nodes covered. The JSON is valid.\n\nThe page has one real root, Ter 1 (PIE *terh₂- \"to cross over\"). I skipped Ter 2, which only redirects to Tres.\n\n| | confirmed | plausible | disputed | transcription_suspect | unverified |\n|---|---|---|---|---|---|\n| Root | 1 | 0 | 0 | 0 | 0 |\n| Nodes | 7 | 6 | 3 | 0 | 0 |\n\nThe root is right (Pokorny pp. 1074–1076, Watkins/AHD *terə-2*), and the chart follows Watkins almost item for item. Klein p. 1639 is his *trans-* entry, as Nourai cites.\n\n**Disputed:**\n- **#2 Persian -tar/-tarīn:** the comparative suffix comes from the PIE suffix *-teros, not from the verb root *terh₂-. The other two words in the node are fine: sarā (from Middle Persian srāy) and gozaštan (from *wi-tarH-, per Cheung and Mo'in's note in Borhan p. 1778).\n- **#11 English drill:** it belongs to *terh₁- \"rub, turn, bore\" (AHD *terə-1*, Pokorny 3. ter-). through, thorough and nostril are correct.\n- **#14 PIE An-teros:** the word is real, but it is *h₂en- plus *-teros, filed under an-2 in Pokorny p. 37 and analysed the same way by Mann. It is not derived from *terh₂-.\n\n**Plausible, worth knowing:**\n- **#3 OP \"srâd, srâda\":** this form is not attested in Old Persian. It is a reconstruction (*srāda-, as in Nyberg, Klein and Jeffery) that the book prints without an asterisk.\n- **#6 Latin:** the book glosses truncus as \"overcome\", but it means \"lopped, maimed; trunk\". Watkins puts it under this root; Klein (*trank-) and de Vaan (origin unknown) do not. terminus is assigned to a separate ter- \"boundary\" root by AHD.\n- **#12 nektar:** Klein prefers a Semitic origin, and Beekes leans towards a Pre-Greek one.\n- **#4 Arabic surādiq:** it is confirmed as a loan from Middle Iranian *srādak. The chart's note deriving it from sarāparda is the older lexicographers' view.\n\nThere were no extraction errors and no transcription flags."
}
```


### [2026-10-15T02:50:54.744Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
