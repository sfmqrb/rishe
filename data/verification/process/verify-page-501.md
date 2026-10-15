# Verification process log — verify-page-501


## [2026-10-15T02:44:16.153Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 501 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-501.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-501.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-501.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 501` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.191Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:18.985Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.011Z] TOOL RESULT

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


## [2026-10-15T02:44:19.527Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-501.txt"
}
```


### [2026-10-15T02:44:19.630Z] TOOL RESULT

```
1	=== PDF page 501 (book page 471) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ten 1, Tengh, Temp : to stretch, pull  (refs POK:1064,1067)  PART 1
4	#1 (parent #0) [Avestan] refs=BQT:1481,2376,2381; SNS:7 | thang, â-thax, hanč : to pull, also a path, way ; far-thang : pull forward, educate ☞Per 1
5	  #2 (parent #1) [Persian] refs=BQT:70,516,2381; MON; HRN:14; SNS:126; FFD:28,67 | hanjîdan «هنجیدن ( آهنجیدن )» : to pull or dig out ; hanjâr «هنجار ( ناهنجار )» : path ; âhang «آهنگ» : intention ; farhîxtan «فرهیختن ( فرهنگ ، فرهنج )» : to educate
6	  #3 (parent #1) [Persian] refs=BQT:70, 516, 2381; HRN:14; SNS:126 | âhîxtan «آهیختن» : to pull out | extra: هیختن ، برهیختن ، فروهیختن
7	#4 (parent #0) [Avestan] refs=SNS:147 | tan : to pull, stretch
8	  #5 (parent #4) [Persian] refs=POK:1064 | tâbîdan «تابیدن ۱ ( تافتن ۱ )» : to spin
9	    #6 (parent #5) [French] refs=None | 
10	      #7 (parent #6) [English] refs=SKT:542; KLN:572 | taffeta, tape, tapestry
11	#8 (parent #0) [Avestan] refs=KLN:1585 | tauruna : stretched, tender, young
12	  #9 (parent #8) [Persian] refs=HRN:90; BQT:217, 532; FIB:217 | tar 2 «تَر ۲» : wet ; tarâneh «ترانه» : "a tender" love song ; tŭleh «توله» : "a tender" animal baby ; tŭrah «توره» : jackal
13	#10 (parent #0) [Avestan] refs=POK:1065 | tathra : string ; thri-thatra : sitar ☞Trei
14	  #11 (parent #10) [Persian] refs=None | târ «تار ( سه‌تار )» : a stringed musical instrument
15	    #12 (parent #11) [Hindustani] refs=AHD:1210 | 
16	      #13 (parent #12) [English] refs=None | sitar
17	    #14 (parent #11) [Greek] refs=KLN:687 | kithara : sitar
18	      #15 (parent #14) [Arabic] refs=SAP:1381 | qîtâr, qĕtarah
19	        #16 (parent #15) [Spanish] refs=None | 
20	          #17 (parent #16) [French] refs=KLN:687 | guitare
21	            #18 (parent #17) [Persian] refs=MON:3502 | gîtâr «گیتار»
22	            #19 (parent #17) [English] refs=KLN:687 | guitar
23	      #20 (parent #14) [Latin] refs=AHD | cithara
24	        #21 (parent #20) [English] refs=AHD | zither, zithern, cither, cittern
25	
```


## [2026-10-15T02:44:20.438Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-501.json"
}
```


### [2026-10-15T02:44:20.538Z] TOOL RESULT

```
1	{
2	  "pdf_page": 501,
3	  "book_page": 471,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Ten 1, Tengh, Temp",
8	        "lang": "Indo-European",
9	        "refs": "POK:1064,1067",
10	        "gloss": "to stretch, pull"
11	      },
12	      "part": 1,
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Avestan",
18	          "refs": "BQT:1481,2376,2381; SNS:7",
19	          "words": [
20	            {"translit": "thang, â-thax, hanč", "gloss": "to pull, also a path, way", "script": null},
21	            {"translit": "far-thang", "gloss": "pull forward, educate", "script": null, "see": ["Per 1"]}
22	          ],
23	          "note": null,
24	          "quote": null
25	        },
26	        {
27	          "id": 2,
28	          "parent": 1,
29	          "lang": "Persian",
30	          "refs": "BQT:70,516,2381; MON; HRN:14; SNS:126; FFD:28,67",
31	          "words": [
32	            {"translit": "hanjîdan", "gloss": "to pull or dig out", "script": "هنجیدن ( آهنجیدن )"},
33	            {"translit": "hanjâr", "gloss": "path", "script": "هنجار ( ناهنجار )"},
34	            {"translit": "âhang", "gloss": "intention", "script": "آهنگ"},
35	            {"translit": "farhîxtan", "gloss": "to educate", "script": "فرهیختن ( فرهنگ ، فرهنج )"}
36	          ],
37	          "note": null,
38	          "quote": {
39	            "text": "زهنجار دیگر درآمد به روم - فروماند گنج اندرون مرز و بوم",
40	            "poet": "Nezâmî"
41	          }
42	        },
43	        {
44	          "id": 3,
45	          "parent": 1,
46	          "lang": "Persian",
47	          "refs": "BQT:70, 516, 2381; HRN:14; SNS:126",
48	          "words": [
49	            {"translit": "âhîxtan", "gloss": "to pull out", "script": "آهیختن"}
50	          ],
51	          "script_extra": "هیختن ، برهیختن ، فروهیختن",
52	          "note": null,
53	          "quote": {
54	            "text": "خوب گفتن پیشه کن با هرکسی - کاین برون‌آهیخد از دل بیخ کین",
55	            "poet": "Nâser-Khosrow"
56	          }
57	        },
58	        {
59	          "id": 4,
60	          "parent": 0,
61	          "lang": "Avestan",
62	          "refs": "SNS:147",
63	          "words": [
64	            {"translit": "tan", "gloss": "to pull, stretch", "script": null}
65	          ],
66	          "note": null,
67	          "quote": null
68	        },
69	        {
70	          "id": 5,
71	          "parent": 4,
72	          "lang": "Persian",
73	          "refs": "POK:1064",
74	          "words": [
75	            {"translit": "tâbîdan", "gloss": "to spin", "script": "تابیدن ۱ ( تافتن ۱ )"}
76	          ],
77	          "note": null,
78	          "quote": {
79	            "text": "خواب آن نرگس فتّان تو بی چیزی نیست - تاب آن زلف پریشان تو بی چیزی نیست",
80	            "poet": "Hâfez"
81	          }
82	        },
83	        {
84	          "id": 6,
85	          "parent": 5,
86	          "lang": "French",
87	          "refs": null,
88	          "words": [],
89	          "note": null,
90	          "quote": null
91	        },
92	        {
93	          "id": 7,
94	          "parent": 6,
95	          "lang": "English",
96	          "refs": "SKT:542; KLN:572",
97	          "words": [
98	            {"translit": "taffeta, tape, tapestry", "gloss": null, "script": null}
99	          ],
100	          "note": null,
101	          "quote": null
102	        },
103	        {
104	          "id": 8,
105	          "parent": 0,
106	          "lang": "Avestan",
107	          "refs": "KLN:1585",
108	          "words": [
109	            {"translit": "tauruna", "gloss": "stretched, tender, young", "script": null}
110	          ],
111	          "note": null,
112	          "quote": null
113	        },
114	        {
115	          "id": 9,
116	          "parent": 8,
117	          "lang": "Persian",
118	          "refs": "HRN:90; BQT:217, 532; FIB:217",
119	          "words": [
120	            {"translit": "tar 2", "gloss": "wet", "script": "تَر ۲"},
121	            {"translit": "tarâneh", "gloss": "\"a tender\" love song", "script": "ترانه"},
122	            {"translit": "tŭleh", "gloss": "\"a tender\" animal baby", "script": "توله"},
123	            {"translit": "tŭrah", "gloss": "jackal", "script": "توره"}
124	          ],
125	          "note": null,
126	          "quote": {
127	            "text": "تنها من و یک شهر پر از خصم و تو با من - شیری و یکی دشت پراز روبه و توره",
128	            "poet": "Qatrân Tabrîzî"
129	          }
130	        },
131	        {
132	          "id": 10,
133	          "parent": 0,
134	          "lang": "Avestan",
135	          "refs": "POK:1065",
136	          "words": [
137	            {"translit": "tathra", "gloss": "string", "script": null},
138	            {"translit": "thri-thatra", "gloss": "sitar", "script": null, "see": ["Trei"]}
139	          ],
140	          "note": null,
141	          "quote": null
142	        },
143	        {
144	          "id": 11,
145	          "parent": 10,
146	          "lang": "Persian",
147	          "refs": null,
148	          "words": [
149	            {"translit": "târ", "gloss": "a stringed musical instrument", "script": "تار ( سه‌تار )"}
150	          ],
151	          "note": null,
152	          "quote": null
153	        },
154	        {
155	          "id": 12,
156	          "parent": 11,
157	          "lang": "Hindustani",
158	          "refs": "AHD:1210",
159	          "words": [],
160	          "note": null,
161	          "quote": null
162	        },
163	        {
164	          "id": 13,
165	          "parent": 12,
166	          "lang": "English",
167	          "refs": null,
168	          "words": [
169	            {"translit": "sitar", "gloss": null, "script": null}
170	          ],
171	          "note": null,
172	          "quote": null
173	        },
174	        {
175	          "id": 14,
176	          "parent": 11,
177	          "lang": "Greek",
178	          "refs": "KLN:687",
179	          "words": [
180	            {"translit": "kithara", "gloss": "sitar", "script": null}
181	          ],
182	          "note": null,
183	          "quote": null
184	        },
185	        {
186	          "id": 15,
187	          "parent": 14,
188	          "lang": "Arabic",
189	          "refs": "SAP:1381",
190	          "words": [
191	            {"translit": "qîtâr, qĕtarah", "gloss": null, "script": null}
192	          ],
193	          "note": null,
194	          "quote": null
195	        },
196	        {
197	          "id": 16,
198	          "parent": 15,
199	          "lang": "Spanish",
200	          "refs": null,
201	          "words": [],
202	          "note": null,
203	          "quote": null
204	        },
205	        {
206	          "id": 17,
207	          "parent": 16,
208	          "lang": "French",
209	          "refs": "KLN:687",
210	          "words": [
211	            {"translit": "guitare", "gloss": null, "script": null}
212	          ],
213	          "note": null,
214	          "quote": null
215	        },
216	        {
217	          "id": 18,
218	          "parent": 17,
219	          "lang": "Persian",
220	          "refs": "MON:3502",
221	          "words": [
222	            {"translit": "gîtâr", "gloss": null, "script": "گیتار"}
223	          ],
224	          "note": null,
225	          "quote": null
226	        },
227	        {
228	          "id": 19,
229	          "parent": 17,
230	          "lang": "English",
231	          "refs": "KLN:687",
232	          "words": [
233	            {"translit": "guitar", "gloss": null, "script": null}
234	          ],
235	          "note": null,
236	          "quote": null
237	        },
238	        {
239	          "id": 20,
240	          "parent": 14,
241	          "lang": "Latin",
242	          "refs": "AHD",
243	          "words": [
244	            {"translit": "cithara", "gloss": null, "script": null}
245	          ],
246	          "note": null,
247	          "quote": null
248	        },
249	        {
250	          "id": 21,
251	          "parent": 20,
252	          "lang": "English",
253	          "refs": "AHD",
254	          "words": [
255	            {"translit": "zither, zithern, cither, cittern", "gloss": null, "script": null}
256	          ],
257	          "note": null,
258	          "quote": null
259	        }
260	      ]
261	    }
262	  ]
263	}
264	
```


## [2026-10-15T02:44:23.455Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; ls data/verification/page-49*.json data/verification/page-50*.json 2>/dev/null",
 "description": "Read source matrix and list refs"
}
```


### [2026-10-15T02:44:23.849Z] TOOL RESULT

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
Permissions Size User   Date Modified Name
.rw-r--r--   68k sfmqrb 14 Oct 22:14  data/verification/page-49.json
.rw-r--r--   69k sfmqrb 14 Oct 22:14  data/verification/page-50.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  data/verification/page-490.json
.rw-r--r--   55k sfmqrb 14 Oct 22:14  data/verification/page-491.json
.rw-r--r--   70k sfmqrb 14 Oct 22:14  data/verification/page-492.json
.rw-r--r--   68k sfmqrb 14 Oct 22:14  data/verification/page-493.json
.rw-r--r--   62k sfmqrb 14 Oct 22:14  data/verification/page-494.json
.rw-r--r--   60k sfmqrb 14 Oct 22:14  data/verification/page-495.json
.rw-r--r--   66k sfmqrb 14 Oct 22:14  data/verification/page-496.json
.rw-r--r--   35k sfmqrb 14 Oct 22:14  data/verification/page-497.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  data/verification/page-498.json
.rw-r--r--   49k sfmqrb 14 Oct 22:33  data/verification/page-499.json
```


## [2026-10-15T02:44:27.134Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,200p tools/verify_check.py | head -150; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000]);print(json.dumps(e['nodes'][1],ensure_ascii=False,indent=1))\"",
 "description": "Inspect checker and example output"
}
```


### [2026-10-15T02:44:27.788Z] TOOL RESULT

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
 "root": "Tel",
 "verdict": "confirmed",
 "modern_form": "PIE *telh₂- 'to lift, bear, weigh; endure' (Pokorny 1. tel-, telə-, tlē-, tlā- 1060-1061; Watkins/AHD telə-; LIV² 622-623)",
 "note": "Pokorny IEW pp.1060-1061 heads the entry '1. tel-, telə-, tle(i)-, tlā-' 'to transport, carry; to bear, suffer', Watkins (AHD) 'telə- to lift, support, weigh', modern notation *telh₂-. Nourai's 'Tel : to lift', the label Indo-European and both his citations (POK:1060; KLN:122 = Klein s.v. Atlas, which spells out the base *tel-, *tal-, *tol- 'to bear, lift, suffer') are correct. The Greek, Latin, Sanskrit and English branches are standard (Pokorny, Walde-Pokorny, Watkins, Klein all list them). Two Iranian/Persian problems: (1) the 'Avestan' tara-āz(u) is Nyberg's reconstructed Old Iranian *tarā-āzu-, not an attested Avestan word; (2) the Persian tarāz/طراز box mixes tarāzū 'balance' (correct) with ṭarāz/tarāz 'adornment' and the city Ṭarāz of Farrokhī's verse, and the Persian atlas 'world' (falak-e atlas) is native Arabic aṭlas 'plain, smooth', not Greek Atlas. Toll's Greek origin is contested (Wiktionary prefers a native Germanic word). No extraction errors: the JSON matches the printed page, including the odd ref 'MON5:5155' (a misprint in the book, presumably for MON5:155).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، بردن، سنجیدن؛ تاب آوردن» است؛ پوکورنی (ص۱۰۶۰–۱۰۶۱) آن را «tel-، telə-، tlā-» با معنای «بردن، حمل کردن؛ تحمل کردن» و واتکینز «telə- برداشتن، نگه داشتن، وزن کردن» آورده‌اند. «Tel: برداشتن» نورایی، برچسب «هندواروپایی» و هر دو مأخذ او (پوکورنی ۱۰۶۰ و کلاین ۱۲۲ ذیل Atlas) درست است. شاخه‌های یونانی، لاتین، سنسکریت و انگلیسی همه پذیرفته‌اند. اشکال‌ها در بخش ایرانی است: «tara-âz» اوستایی نیست بلکه بازسازی ایرانی باستانِ نیبرگ است؛ در خانهٔ فارسی «ترازو» درست است ولی «طراز» (زینت، و شهر طراز در بیت فرخی) واژهٔ دیگری است؛ و «اطلس» به معنای «فلک اطلس/جهان» از صفت عربی «أطلس» (صاف، بی‌نقش) است نه از تیتان یونانی. خطای استخراج دیده نشد.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/telh₂-",
  "https://en.wiktionary.org/wiki/Ἄτλας",
  "https://en.wiktionary.org/wiki/τάλαντον"
 ],
 "ref_check": [
  {
   "ref": "POK:1060",
   "status": "supports",
   "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; Greek tlēnai, talanton ('die beiden Waagschalen'), PN Atlas, -antos, telos 'payment, tribute, tax'; 'Latin tollo, -ere ... tolero ... latus 'getragen''."
  },
  {
   "ref": "KLN:122",
   "status": "supports",
   "note": "Klein 1966 (KLN_1966.txt leaf 75 = c. pp.122-127 by the two-pages-per-leaf offset; the Atlas entry is the one Nourai means) s.v. Atlas: 'Gk. τλῆναι derives fr. *tl-, zero degree of I.-E. base *tel-, *tal-, *tol-, 'to bear, lift, suffer', whence τάλας ... τ
{
 "id": 2,
 "lang": "Avestan",
 "words": "tara-âz, tara-âzu",
 "verdict": "plausible",
 "derivation": "Nourai's 'tara-âz, tara-âzu' is the Old Iranian reconstruction proposed by Nyberg (Manual of Pahlavi II 191) and repeated by Mo'in (BQT p.480 fn.1) and Asbaghi (PLA 194): MP tarāzūg 'balance' < OIr *tarā-āzu-, from *tarā- 'scale, balance' (= Skt tulā, PIE *tl̥h₂-eh₂-, with the regular Iranian *ar from a syllabic liquid before a laryngeal) + *āz- 'to lead, drive' (Av. az-, Skt aj-, Lat agere), i.e. 'that which carries the scale-pans'. The form is not attested in the Avestan corpus — Bartholomae's Altiranisches Wörterbuch has no tarāzu-/tara-āzu- — and Mo'in marks it with the asterisk-symbol as reconstructed 'Old Iranian' (ایرانی باستان), Asbaghi as 'air.'; so the box label 'Avestan' overstates the evidence (Wiktionary's Persian entry nonetheless writes an Avestan-script source form without an Avestan entry of its own). The link to Sanskrit tulā/PIE *telh₂- is accepted; the second element *āz- is Nyberg's analysis and remains a hypothesis.",
 "derivation_fa": "«tara-âz, tara-âzu» که نورایی آورده، صورت بازسازی‌شدهٔ ایرانی باستان است که نخست نیبرگ (راهنمای پهلوی، ج۲ ص۱۹۱) پیشنهاد کرده و معین در حاشیهٔ برهان قاطع (ص۴۸۰) و اسباغی (ص۱۹۴) تکرار کرده‌اند: پهلوی tarāzūg از ایرانی باستان *tarā-āzu-، مرکب از *tarā- «کفهٔ ترازو» (هم‌ریشه با سنسکریت tulā) و *āz- «راندن، بردن» (اوستایی az-، سنسکریت aj-، لاتین agere). این صورت در متن‌های اوستایی گواهی نشده است و بارتولومه آن را ندارد؛ معین نیز آن را با نشانهٔ ستاره «ایرانی باستان» خوانده است، پس برچسب «اوستایی» در کتاب دقیق نیست. پیوند آن با ریشهٔ *telh₂- پذیرفته است، ولی جزء دوم (*āz-) فرضیهٔ نیبرگ است؛ ادعای نورایی با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/ترازو"
 ],
 "ref_check": [
  {
   "ref": "PLA:194",
   "status": "partial",
   "note": "Asbaghi, Persische Lehnwörter im Arabischen p.194 (PLA_pages.txt leaf 209; ref_page.py PLA:194 --pdf-page 209): 'ṭirāz: „Stickerei, Rand, Saum“ pers. tarāz, mp. taraz' and 'ṭirāzdārān: „Futteral der Waage“ pers. tarāzūdārān, mp. tarāzūk „Balance, Gleichgewicht“ air. *tarā = skr. tulā + aw. az „zuführen“; tk. terazi, serb., kl.russ. terezy'. The cited page is the source of Nourai's tara-āz analysis, but it labels the form Old Iranian (air.), not Avestan."
  }
 ],
 "consulted": [
  {
   "src": "NYB",
   "where": "Part II p.191 s.v. tarāzūk",
   "stance": "supports",
   "note": "Nyberg, Manual of Pahlavi II p.191 (NYB_vol2_glossary.txt line 3737): 'tarāzūk [tlʾcwkʾ] balance, scales for weighing ... — OIr *tarā = Skr tulā 'balance, scale of a balance' + Av. (223 sq.) az- 'to convey, to conduct' (Lat agere)'; the Sanskrit index of the same volume lists 'tulā: tarāzūk'."
  },
  {
   "src": "BRT",
   "where": "AiW, grep 'tara.?az', 'tarazu', 'taräzu' in BRT.txt",
   "stance": "silent",
   "note": "No Avestan tarā-, tarāzu- or tara-āzu- in Bartholomae (grep returned nothing) — the form is unattested in Avestan; Av. az- 'to drive' is itself well attested."
  },
  {
   "src": "BQT",
   "where": "vol.1 p.480 fn.1 s.v. ترازو",
   "stance": "partial",
   "note": "BQT vol.1 p.480 (archive.org borhan-ghate-v1 leaf n706, read from image; saved ocr/BQT/0480.vision.txt) s.v. ترازو, Mo'in's fn.1: 'پهلوی tarâzûk، ایرانی باستان ☼tarâzu = ☼tara-âzu : ☼tara از سانسکریت tulati، tulya، âz، az از سانسکریت aj (راهنمایی کردن، راندن، پیش‌بردن)، «نیبرگ ۲۲۳»'. Asterisked = reconstructed Old Iranian, after Nyberg. Same analysis, but labelled Old Iranian, not Avestan."
  }
 ]
}
```


## [2026-10-15T02:45:01.089Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','SNS','MON','HRN','FFD','FIB','KLN','SKT','AHD','SAP','WLD','CHEUNG','ARY']:\n  v=d.get(k);print(k,json.dumps(v,ensure_ascii=False)[:700] if v else None);print()\n\"",
 "description": "Look up reference keys"
}
```


### [2026-10-15T02:45:01.546Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based lea

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read pri

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or g

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe-private/data/verifica

FIB {"title": "Ebrahim Pur-Davud, Farhang-e Iran-e Bastan, vol. I, Tehran University Press 1326/1947", "kind": "website", "url": "https://noorlib.ir/book/info/104334 (viewer: https://noorlib.ir/book/view/104334?pageNumber=<N>&viewType=pdf) ; PDFs also offered at kashanketab.com / kaffeketab.ir (62 MB)", "lookup_hint": "Not on archive.org; browser needed for noorlib.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Scan exists online but not fetched here."}

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966:

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/de

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only. Google Books no-view records 4y

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015

CHEUNG None

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe-
```


## [2026-10-15T02:45:04.933Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Root /lemma: ten\\|Root /lemma: temp\\|Root /lemma: tengh\\|Root /lemma: ter-6\\|Root /lemma: ter-[0-9]*, teru\\|Root /lemma: teren\" POK_full.txt | head -20",
 "description": "Find Pokorny lemmas for ten/temp/tengh"
}
```


### [2026-10-15T02:45:05.412Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:45:07.537Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^Root /lemma: te[nmr]\" POK_full.txt | head -30; grep -n \"Root /lemma\" POK_full.txt | head -3",
 "description": "List Pokorny te- lemmas"
}
```


### [2026-10-15T02:45:07.893Z] TOOL RESULT

```
85996:Root /lemma: ter-3, tera-and ten-, tn- 
6244:Root /lemma: a/d^- 
7517:{ve- 5/7///-e (participle of alb. 5/7/KA7y"push with difficulty') see Root /lemma: (s)teu-1\ "to 
9659:Considering Phrygian P£5u "water' : nasalized lllyrian B/ndus 'waier god' Root /lemma:
```


## [2026-10-15T02:45:10.200Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Page(s): 106[3-9]\\|Page(s): 1070\\|Page(s): 107[0-9]\" POK_full.txt | head -30",
 "description": "Find Pokorny entries on pages 1063-1079"
}
```


### [2026-10-15T02:45:10.539Z] TOOL RESULT

```
85388:Page(s): 1063-1064 
85498:Page(s): 1064-1065 
85746:Page(s): 1065-1066 
85785:Page(s): 1068-1069 
85865:Page(s): 1069-1070 
85883:Page(s): 1076 
85994:Page(s): 1070-1071 
86172:Page(s): 1071-1074 
86245:Page(s): 1074-1075 
86279:Page(s): 1075-1076 
86335:Page(s): 1077-1078 
86390:Page(s): 1078-1079 
86460:Page(s): 1079-1080
```


## [2026-10-15T02:45:12.277Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 85494,85900p POK_full.txt | cut -c1-260",
 "description": "Print Pokorny temp/ten/tengh entries"
}
```


### [2026-10-15T02:45:12.655Z] TOOL RESULT

```
Tocharian A tampe' power', AB camp- " to be able, to be capable of '. 

References: WP. 1721 f., WH. 154, II 659 f., 662, Trautmann 317f., Vasmer3, 95, 101, 
153, Frisk Goteborgs Hogsk. Arsskr. 57, 1951: 4. 
Page(s): 1064-1065 

Root / lemma: tend- 

See also: see below tem-1. 

Page(s):1067 

Root / lemma: tenagos, tenagos 

Meaning: ground in water 

Material: Gr. TEvayog n. "ford'; Latvian tTgas {* tingas) "Tiefe between zwei shallows'. 

References: WP. I 724. 

Page(s): 1 067 

Root / lemma: tengh- 

Meaning: to extend, stretch, span 

Note: Aryan *thengh-, yet probably nevertheless extension from ten- 1 6s. 

Material: Avestan dang- {danjasante, danjayente, participle daxta-) "ziehen, Bogen 

spannen'; but danvare, Abl. &anvanaTb<y^ (as Schuftwaffe)' after Mayrhofer through 

contamination with *danvan- (= Old Indie dhanvan-, above S. 234) originated; osset. t'lnjjn 

" distend '; Armenian t'anjr. Gen. t'anju 'dense, thick' {*tnghiu-); 

Latin temo, -onisrw. "shaft' {*tenksmd); Old Church Slavic */^^/7(?//"ziehen', rastggg, 
/'55/^s//"distrahere', russ. /^^ty" straff, tight, firm, strong, heavy ', poln. tgg/6s.. Old Church 
Slavic /p^5"auvoxn, irepiaTaaic;', slov. tgga' sluggishness, Schwermut' etc.; die meaning " 
heavy ' also in Slavic *fggbkb: 0\6 Church Slavic otggbc/f/'^apzw', tgzbkb "papu(;', 
tggostb "papo(;', tggota ds. etc.; also Old Church Slavic istgsklb "emaceratus, tabidus', 
/s/^s/r/7(?//"tabescere' with s/r-suffix; here Old Church Slavic tgza' litigation '; 

Lithuanian t/ngus"\6\e' (= Slavic */i^^fc in tggostb etc., and: Old Icelandic l=>ungr), t'ingiu, 
ting'eti'\6\e, unlustig sein', ting-stu, -au, -//"trage become'; 



Old Icelandic l=>ungr^ heavy ', t^ungerw. "burden, load', l=>yngia^ grouch', l=>yngd 
"Unannehmlichkeit, Verlegenheit', t^yngsr distress, crowdedness'; Old High German 
dThsala, Old English t^Txl, Old Icelandic t^TsI 'shaft' {proto Germanic *f^enxs/d actuaWy 
"Zugstange'); Tocharian A tank-, B tank- 'hinder'. 

References: WP. I 726 f., WH. II. 658, Trautmann 318, VasmerS, 166. 
Page(s):1067 

Root / lemma: teng-1 

Meaning: to soak, wet 

Material: Gr. teyyw " wet, befeuchte'; Latin tingd{o\6er tinguo, das after unguo: unx/ior 

older */e'/7^deingetreten is), -ere, -nxi, -nctum' make damp, moisten; paint '; Old High 

German thunkon, dunkon' dip, immerse in a liquid '; Swiss ///7/r"humid, wet'. 

References: WP. I 726, WH. II 684. 
Page(s):1067 

Root / lemma: teng-2 

See also: s. S. 1088 {tong^. 

Page(s): 1 067 

Root / lemma: tenk-1 

Meaning: to extend, stretch, span 

Note: (root-extension from ten-1 ds.); only Germanic 

Material: Gothic t^eihs{*tenkos), PI. t^eihsau. "time'; with gramm. variation Old Icelandic 

l=>ingv\. 'Gerichtsversammlung, property, object ', Old English dingds.. Old Saxon thing. 

Old High German ding. Modern High German Ding, langob. /^/aA-'rechtliche gathering, 

assembly, convention, congregation, meeting'. Old Germanic GN l\/1ars Thinxus 

(Germanic *7/i/Sjfc'//7^5az 'the god the congregation, meeting'); Old English dingan'e\nen 

pact, covenant make'. Modern High German dingen. 

References: WP. I 724 f., Kluge-Goetze 137; identical with: 

Page(s): 1 067 

Root / lemma: tenk-2 

Meaning: to clot, thicken; solid, thick 

Material: Old Indie tahc- tanakti'z\e\r\t together', with a- "makes curdle, coagulate, harden ', 

atangana-m'M\tte\ zum Gerinnen, rennet', takra-m' buttermilk ' {*tnk-i6-m: *tenk-io-m\v\ 



isl. I=>el), npers. /5/A/775 "sour milk'; Avestan taxma-\a\'\ar\t, proficient, energetic, 
heldenhaft', compounds tqsyah-. Sup. tancista-, np. tanjTSan^^uW together', afghan. tat 
"dense, thicl<' ( *tahta-)\ 

Middle Irish tecar^ protection', techt {*tenkto-, compare Old Icelandic t^etti) "clotted, 
congealed, coagulated', /ec/7/e "proper, right', cymr. /©//^/"characteristics', mcymr. brenhin 
teithiawc^rex legitimus' (from "tight, firm'). Old Irish cc»/7-/ec/"gerinnt' (= Gothic t^eihan, 
Indo Germanic *tenkd), techtaid6s. {*tenktd)\ ablaut, tocad, cymr. /y/7^eo'" luck', bret. tonket 
"fate, destiny', PN Tunccetace, Latin Gen. in Wales; zero grade cymr./a/7cf. "peace' 
{*tnka), tangnef6s.\ compare Old Danish taknem^ grateful ' under tong-\ gall. PN Tanco- 
/'ZV"Friedensfurst'; 

nisi. A'e/n. " buttermilk '; Old Icelandic A'e///'"dicht', Middle High German dJhte, Modern 
High German dichtav\6 dial. de/cM{proto Germanic *Penxtu-); nisi, f^ett/" sour m'\\k'; 
Gothic A'e//75/7 "thrive'. Old High German gidThan, Old English gedeon6s., participle Old 
English gedungen. Old Saxon githungan " perfect ', in addition das Kaus. Old Saxon 
theng/an \o\\en6en' (of present *A'/775/7 from junction in die /^row), Gothic gat^aih, German 
gediegen^ solid ', Middle Low German dege^ prospering; flourishing, advance'; 
Verschmelzung with cognate from Lithuanian tinku tikti^ be good for, be suitable for, 
passen', yC>5///7/r^"schmecke, behage'. Iter, taikau, -yti^ piece together a jigsaw puzzle, fit 
together, bring in order ', //'Aras "right', das to Lithuanian tiekti, /e/7r// belongs). Modern High 
German Bavarian deihen^ parch, dry and dadurch dichter become', compare with 
gradation "A'a/?;^- Modern High German steir. dahen^Avj, dorren' and die appellation the 
Tonerde Gothic t^aho. Old English dohse, do. Old High German daha. Modern High 
German Ton{*t^anxdn), Old Icelandic A'5"loam', Old Saxon thah/^\r6en'; 

Old Icelandic Peng/7/, Old English denge/'pnnce, lord, master, mister' {*l=>angilaz); 

Old Icelandic l=>ang. Middle Low German dank^ seaweed. Tang', Old English dung 
"Aconitum napellus'. Low German M/c»o'e/7o'^/7g"Schierling' ("*dichte mass, tussock'?); 

Lithuanian /a/7/ri/s "dense, frequent, often'; 

kir. t'aknuty^ use, take advantage of, slov. /e/r" prospering; flourishing '; presumably 
Old Church Slavic tgca'ra\n', slov. t'gca^haW, and likewise; whether Gothic Pe/fvd 
"thunder' belongs, with from "Wetterwoike' verschobener meaning, is hochst dubious. 

References: WP. I 725 f., Trautmann 313 f., Vasmer 3, 158 f. Marstrander ZcP. 7, 369 f., 
J. Loth RC.41,225f.; 



See also: root-extension from ten-1 "dehnen'. 
Page(s): 1 068 



Root / lemma: ten-1, tend- 

Meaning: to extend, stretch, span 

Grammatical information: ten-bMei in Indo Germanic an unthematic root aorist (ved. atari, 

atata'er has gespannt') and ein Perfekt (ved. tatana, tatne, Latin tetini). Das present wird 

with -e^-extension (ved. tanoti, tanute, gr. hom. Tavurai) or vie/o-suffix shaped (gr. Tsivoj); 

compare /e/7i/-5"thin' and die extensions tengh-, tenk-, temp-, tens-. 

Note: 

Root/ lemma: ten-1, tend-: "to extend, stretch, span' derived from the extended Root/ 

lemma: 6^6-2: "to put, place'. 

Material: Old Indie /a/7d7/"dehnt, spannt, erstreckt sich, dauert', Avestan pairi-tanava 1 . Sg. 

Konj. Akt. "I will fernhalten', pairi-tanuya \ . Sg. Opt. Med.; Old Indie ut-tana- "ausgestreckf 

= Avestan ustana- ds. ( *tnn6-, compare Old Indie tani-man- n. "Dunne', also Lithuanian 

t'inti, Latin tene-re); np. tamdan^iuru, spinnen'; as o^-present (as Latin tendd) Old Indie 

tandate^ aWows after, ermattet' {tandra^UaVaqkeW., Abspannung'); 

participle Old Indie tata- m. "gestreekf (= gr. tqtoc;, Latin tentus); tat/'-m. "row, cord, 
sacrifice, immolation ' (= gr. mo\q "Spannung, lengthening ', Latin //?-, con-tent/d), next to 
which zero grade tant/- "cord, string, row', tantu-' filament, cord, string, Aufzug of texture '; 
tan- "Ausbreitung, Fortdauer, Fortpflanzung, progeny ', Instr. /a/75 "continue', tana- m. " 
descendant ', tana-m, tana, tanas- n. " progeny '; tantra-m 'Zette\, Aufzug am loom' = np. 
/^/'(Avestan *t^&ra-) ds., afghan. /©/""net'; Old Indie tana- m. "clay, filament ' (compare gr. 
t6vo(;); perhaps here tanu-i. "body, person, Selbst' = Avestan tanu-i. ds. (Mayrhofer 475); 

gr. TavuTQi "streckt sich' (= Old Indie tanute), ravucjo (sravuaa etc.) "streeke, dehne'; 
T£ivu) ds. (tqtoc;), TiToivu) ds.; Toivia "(long) stripe, bandage' (due to eines Adj. *Tavi6c;); 
TETOvoi; "Spannung, twitch '; T£Tav6(; "gestreekt, long, straff; tevojv, -ovto(; "sinew', t£vo(; n. 
"sinew, straff angezogenes Band' (= Latin tenus, -oris, compare also Old Indie tanas-v\.), 
a-T£vn(; "very gespannt, straff (a- probably with Ionian reduction = srn-), whereof aTSvi^u) 
"hefte den Bliek angespannt auf etwas'; tovoc; "Spannung, Anspannung; also the voice, 
lifting of Verses, musikaliseher sound, tone' (: Lithuanian tanas); ma\c,i. "Spannung' 
{*tnt/s); about tovu- "sich ausbreitend' see below tenus, 

alb. /7o'e/7y"breite from, pull, spanne die Saiten'; katund, ketunt {*ke-tn-t-) "village' 
("*ausgespanntes tent'); 



alb. Geg. me ndjejV to stay', past participle {*tentum) ndejtun^ stayed'. 

Latin tendo, -ere, tetendi, tentum, newer M/75i//77'spannen, distend, ausstrecken' 
(originally o'-present) = Umbrian an-, e/7-/e/7/^"intendito', i/s/e/7/^"ostendito' etc., Latin 
tentus, (in-)tentia, teneo, -ere, tenui{0\6 Latin tetinT= Old Indie tatan§), tentum^\\o\6, stop 
etc' (originally Durativ, trans, and intrans. "somewhat gespannt halten', hence tenere a\so 
"endure' = vast, spacious sein), at-tinere, pertinere, continuus, tenere aliquid ouQ\v\a\\)j W\\.\\ 
Akk. of Zieles "auf etwas to ausgereckt, gespannt sein' (/e/7e-/'e belongs to Old High 
German donen'vast, spacious, ausgestreckt sein' and Lithuanian tinstu, f/nf/"to swell'); 
tenus, -or/'sn. "cord with loop, noose, snare ' (= gr. itvoq), tenor, -dr/src\. 
"ununterbrochener run, flow, Fortdauer, connection; (jur.) sense, mind, content eines 
Gesetzes', /e/7^s preposition m. Abl. Gen. Akk. "sich erstreckend bis, bis an', prot/nus ' s\c\n 
after vorn erstreckend, vorwarts' (compare Old Indie nutanah, -//75/7 "present, current', 
Latin diu-tinus, Lithuanian dabart/'n/s' present, current'), tenax^ tenacious, tenacious'; 
Umbrian ten/tu ^teneto'; 

Maybe alb. tendos' strech ' a Latin loanword. 

Old Irish tan "time' ( %n^, actually "Fortdauer, zeitliche Ausdehnung' {/n tain "when, if) 
(: Latvian tina). Old Irish /e/" string ' {*tnta) = cymr. tant ds. (compare Old Indie tantu-, isl. 
t^ind) = bret. ar-dant ^Pi\6cke am cart zur Befestigung of Seiles'; Old Irish te/t^goes' {*ten- 
ti, alter root Aorist, originally "streckte'); 

Gothic uf-l=>anjan ^s\c\\ distend, sich ausstrecken'. Old Icelandic A'e/7/5"ausspannen, 
ausstrecken'. Old English denian, dennan^s\xeckev\, spannen'. Old High German den(n)en 
"dehnen'; Old Icelandic ^inuirxope, hawser, dasein net einfaftt and in addition dient, es to 
spannen'. Old Icelandic Nnd, Norwegian tindert " phren' (Old Irish tet. Old Indie tantu-); 
d'^-present Old English dindan\o swell, angry, irate sein'; in addition Old Icelandic t^undi. 
"river'; Old English dun/an's\ch heben, sich dehnen, to swell', alike Old High German 
Middle High German donen ' s'\c\r\ distend, to swell, strotzen'; oto/? "ausgespannf. Middle 
High German done, o'c/7"Spannung', Old High German dona. Old Saxon thona't\N\g, 
branch, tendril ', Modern High German Dohne, Old English ^/Adc»/7e"Albranke, Solanum 
dulcamara'; Old Icelandic t^gni. "Holzstabchen, with dem Felle zum Trocknen 
ausgespannt become', Swedish /a/7a "sinew'. Old Danish tan^ phren'; 

Lithuanian tinstu, t/nt/'to swell', /a/75S "swelling, lump, growth' ("*sich distend ', also of 
Spannen the skin an geschwollenen Stellen; gefordert through das reimende tv/nt/^to 
swell'); Lithuanian t/n-k/as^ net'. Old Prussian sasin-tinclo^ hare's snare', Latvian tinu, t?t 



'flax, wattle, braid, coil, wicKeTrv, f/na'e'\n Setznetz' (: Old Irish tan), ///7e/r//s "somewhat 
Gewundenes, Gewickeltes'; Lithuanian tandus"\6\e'; 

Old Church Slavic teneto, tonoto'rope'. 

References: WP. I 723 f., WH. II 662 ff., Trautmann 323 f., Vasmer 3, 93, Mayrhofer 1, 
475, BerginEriu 12, 227ff. 
Page(s): 1065-1066 

Root / lemma: ten-2 

See also: see above S. 1021 under (s)ten-1. 

Page(s): 1 067 

Root / lemma: tens- 

Meaning: to extend, stretch, span 

Note: extension from ten- 1 6s. 

Material: Old Indie tamsayat/^z\e\r\t hin and her, schijttelt', tartisat/ {uncovered), Aor. a- 

tasat^puW, with Gewalt set in motion ', /asa/a-zr? 'Weberschiffchen', v/tast/'-m.; Avestan 

v/'tast/-' span'; 

Latin to/es, -/um'craw am neck', Demin. tdns/7/ae ' 6\e Mandein in neck', prote/um' 
towing rope for Ochsen, ununterbrochener Fortgang', whereoi prote/are "\n die Lange 
Ziehen' (during prote/are ^ dme away, fortjagen' as telTs^ propellerd to understand, 
comprehend is); /e/7sa'Prozessions- or Gotterwagen', das subst. Fem. of participle 
tensus, 

Gothic 5/A'//75a/7'heranziehen', anid. thinsan^ z\e\\en, rend ', Old High German dinsan 
"Ziehen, drag', Hessian dinse, dans^z\ehen\ participle Modern High German gedunsen 
(actually 'aufgezogen'). Old High German danson^ z\e\\en, dehnen'; 

Lithuanian t§siu, t^st/" through Ziehen dehnen, verlangern', prat^sa 'Verzug, Aufschub', 
^z/i^S5s"Leichentuch', Intr. t/stu, t/st/"s\c\r\ dehnen, sich reckon', t^sau -yti{: Old Indie 
tamsayati) 'pull, reckon'. Old Prussian tienstwei^ sWr, tease, irritate', 2. PI. Imp. tenseiti, 
participle entensTts "gefaftf, /e5/75/5 "shaft'. 

References: WP. I 727, WH. II 666, 688, 691, Trautmann 318 f., Mayrhofer 1, 465, 491, 

532. 

Page(s): 1068-1069 



Root / lemma: tenu-s, tenu-s 

Meaning: thin 

Grammatical information: fern. tenuT 

Note: to ten-1 "dehnen' 

Material: Old Indie tanu-, fern. /5/71/rthin, tender, fragile, flimsy, insignificant ' {tanuka-6s. 

= Slavic tbnbkb); substantivized Old Indie tanu- f., tanus- n., Avestan tanO- f., tanus- n., np. 

/a/7 'body, body'; 

gr. TQVU- "long', fern. ravsTai "long balk, beam'; Tava(F)6(; "langgestreckt, long'; perhaps 
eherzu 1. ten-, s. Specht KZ 59, 35, SommerZur Gesch. d. gr. Nominalkomp. 127; 

Latin tenuis ^\h\v\, fine, tender' (from fem. *tenuT= Old Indie tanvT); gr. lavaFoq kann from 
*T£vaF6(; assimilated sein; 

Old Irish tan{a)e{W\\h secondary -e), corn, tanow, bret. tanao, /5/7c»"thin' (proto Celtic 
*tanauo-\ cymr. /e'/7e^verdankt sein edem influence of Latin tenuis); 

Old High German dunni Old Saxon tfiunni. Old Icelandic t^unnr^VcWu' (/7/7from nu)\ here 
also *l=>ennd, *l=>unnd\. "Stirne, temple, flattened region on either side of the forehead ' in 
Old High German tinna. Middle High German tinne, tunnels.; in den compounds. Old 
High German tinna-bacho " temple, flattened region on either side of the forehead ' and 
Old High German dun-wangi, -wengiu.. Old English dun-wang(e)i.. Old Icelandic t^un- 
vangi m., Swedish tinning^ temple, flattened region on either side of the forehead '; 

Lithuanian tQvas, Latvian tievs " slim '; 

Old Church Slavic tbnbl<b "thin' (assimil. *tbnbl<b, russ. t6nl<ij). 

References: WP. I 724, WH. II 666, K. Jackson Lang, and Hist. 376, Trautmann 319. 
Page(s): 1 069 

Root / lemma: tep- 
Meaning: warm 

Material: Old Indie tapati 'erwarmt, burns' (also "kasteit sich, ijbt penance, atonement'), 
participle tapta- "erwarmt, erhitzt', tapas-n. "heat, blaze, glow', tapu- " burning, hot', Kaus. 
tapayati 'erwarmt, erhitzt'; Avestan tapaiti"\s warm', Kaus. tapayeiti' erwarmt, erhitzt', 
Inchoh. tafsaiti {*tepasReti) "wird hot', participle tapta- 'erwarmt, hot', tafnu-m. 
"Fieberhitze, fever', tafnah-r\. "heat, blaze, glow; fever'; np. taftan'hwrr\, warm, gleam, 
shine'; 



alb. Tosc ftoh, Geg ftofruake cold, extinguish from, injure with words' {*vetep-sRd 
"entwarme'); 

Latin tepeo-ere^ lukewarm sein', tep/dus '\Narm', tepor' warmth '; presumably Oscan 
tefurum "a kind of (blaze-) sacrifice, oblation' ( *teps-ro-)\ Umbrian Abl. Sg. with 
postposition tefru-to, Akk. PI. Umbrian tefra ^ caxues cremandas'; 

Old Irish /e'hot', PI. teit {* tepent- = Old Indie participle tapant-); ten and tene. Gen. -ed 
"fire' {*tepnet-), cymr. corn. bret. fan6s., corn. bret. tana'k\n6\e, inflame'; Old Irish fess, 
cymr. corn, tes, bret. /ez'heat' {*teps-tu-, to es-stem Latin tepor. Old Indie tapas-); Middle 
Irish ///77/77e'heat, iear\*teps-rnia)\ cymr. /ny/77'heat', acorn. /c»//77"hot'. Middle Breton 
toe/77, nbret. tomm^hoi' {* tepesmo); 

Norwegian /ei/a "vor heat keuchen'. Old English de/^a/7"pant, gasp'. Old Icelandic t^efr 
m. smell, odor, taste', t^efa^smeW trans., t^efja^smeW intr.; (Grundvorstellung of warmen 
Dampfes from Speisen); 

Old Church Slavic *tep/b{\r\ tep/ostb 'Bzp[i6ir\q'), Czech tep/y, russ. tep/yj and (with o 
after top/t/) Old Church Slavic top/b "warm'; Kaus. serb. tdp/t/"me\t', russ. top/tb " heat; 
zerlassen'; Prussian PN Tap/awken actuaWy "Warmfeld'; 

Hittite tapassa- lever, heat' (Old Indie loanword?). 

References: WP. I718f., WH. II 667 f., Trautmann 319, Vasmer3, 111, Mayrhofer 1, 477, 

569. 

Page(s): 1069-1070 

Root / lemma: terd- tred- 
Meaning: to drill 

Note: (see also ter- "malmendes insect'), extension from */©/"- "rub, durchbohren' 
Material: Old Indie trnatti, Kaus. tardayat/ {tardat/ Gramm.), Perf. tatarda' durchbohren, 
split', tardman-n. "hole, aperture ', tarda- rr\. 'ein insect', //■o'//a-"locherig, durchbohrt', 
trada- "the (through Bohren) eroffnet'; Lithuanian trendu, -e//"from Motten, WiJrmern 
zerfressen become', trande under trandis^ maggot, Holzwurm'; ablaut. Latvian trudi^ 
mould, dank decay ', //'^o'e/"verwittern, decayed '; Lithuanian //7'0'e "diarrhea'; Old Church 
Slavic //po'fc "tinder' and "kind of disease, malady, 5ua£VT£pia' (compare above S. 1073 
Lithuanian trfedziu^haye diarrhea': cymr. frwyddo' bore'), Czech //Y/^/'Zitterich am face'. 
References: WP. I 736, Trautmann 328, Vasmer3, 144, Kuiper Indo Germanic Nasalpras. 
96 f., 183 f., Mayrhofer 1,521 f. 



Page(s): 1076 



Root / lemma: tei1(-, trek- {fork-, trok-) 

Meaning: to turn 

Note: probably extension from ter-3'rub, drehend reiben' 

Material: Old Indie farku- m. ' spindle', n/starkya- '\Nas sich aufdrehen allows'; figurative 

tarkayat/" assumes, sinnt after'; 

gr. aTpaKTO(; m. f. ' spindle (figurative: arrow, sprit)' a = /7'in', as ('Stabchen zum 
Aufdrehen'), aTp£Kn(; "unverhohlen, geradeheraus' ('unumwunden'); alb. fjerr'sp\n' 
{*terknd)\
```


## [2026-10-15T02:45:16.703Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 85440,85494p POK_full.txt | cut -c1-260; grep -n \"ter-6\\|Root / lemma: teru\\|Root / lemma: tereno\\|Root / lemma: ter-[0-9]\" POK_full.txt|head",
 "description": "Print Pokorny temp- entry and search ter-"
}
```


### [2026-10-15T02:45:17.260Z] TOOL RESULT

```
abstem/us' sober'; Middle Irish tarn {* tomu-) "disease, malady, Ohnmacht, death'; tamaid 
"dies'; mcymr. /5M/"death'; Modern High German damisch, dam//ch ^betaubt, benommenen 
Geistes', westFaliscan dumme/n ' cboke; suppress, crush'; russ. -Church Slavic tom/t/ 
"torment, smite; distress; exhaust'. 

References: WP. I 720, WH. II 657, 664, Trautmann 313, Vasmer 3, 118, Mayrhofer 1, 

495, 503; 

See also: probably to consecutive {tem(a)-). 

Page(s): 1 063 

Root / lemma: temp- 

Meaning: to extend, stretch, span 

Note: extension from *ten- ds. 

Material: Npers. tab-ad. Inf. taffanan6 tab-F-dan 'turn, spinnen', intr. "sich drehen, afflicted 

become' (from one to *tap = Indo Germanic *tmp- analogical refined Kaus. *tapayati), 

wherefore probably as Iran. loanword gr. rann^, 5aniq "cover, rug'; 

Armenian /'5/77it>"(*gestopftes Sattelkissen), saddle; das weiche flesh an Tierbeinen'; gr. 
PN Tsjjnn (: Latin tempus' temple, flattened region on either side of the forehead '); 

here Latin tempus, -or/sr\. " temple, flattened region on either side of the forehead ' 

Maybe alb. Geg (*tempus) tamth, Tosc temth' temple ' Latin loanword. 

(from the thin gespannten skin, compare Old Icelandic etc. Punn-vang/m. " temple, 
flattened region on either side of the forehead ') = Latin tempus "Zeitspanne', in addition 
temperare' measure halten, measure give' (hence "mix'); templum' an open place for 
observation, place marked off by the augur's staff ' ("*ausgespannt = ausgemessen'); 
perhaps antemnai. "sprit' ("die Aufgespannte') from *an{a)-temp-na; templa, -drum'6\e 
gespannten Querholzer, auf denen die Schindein befestigt become'; contemplari' arsveq 
pAsTTsiv ', tempto, -a/ie (iterative to * tempo) " touch, befijhlen, assail, examine, auf die 
Probe place ' (see Persson Beitr. 488 ff.); 

Old Icelandic l=>ambr's\No\\er\, thick', l=>gmb Subsi. " swollen Bauch, bowstring '; 

Lithuanian temptT through Ziehen spannen, dehnen'. Iter. tampyti6s., t/mpt/"s\ch 
reckon', t/'mpa "sinew', temptyva " bowstring ' = Old Church Slavic tgtiva "sinew'. 



Lithuanian y?a/77yOas"Anspannung, exertion ' (ablaut. //^/77/7a5" beginning zum Sprunge'), 
/a/TT/OAi/s "tenacious, elastic'; Latvian //e'yO//es"hartnackig sein'; 

Old Church Slavic tgph 'obtusus, crassus'? perhaps from "gedunsen"; russ. tepst/'strafi 
lure, tempt '; 

Tocharian A tampe' power', AB camp- " to be able, to be capable of '. 
82030:" infertile ', s. ster-6^ infertile '), OTspsiJvioq ds.; 
82687:Root / lemma: ster-6 
82697:Armenian sterj^ infertile, from animals', also sterd {*ster-6^-o-, -Jo); 
85937:Root / lemma: ter-1 
85953:Root / lemma: ter-2, teru- 
86002:faded ', compare Latin mollis : mold), and ter-6\'r\ Worten for "malmendes insect' 
86174:Root / lemma: ter-4, tera- : ^-, tra-, teru- 
86247:Root / lemma: ter-5 
86281:Root / lemma: ter-6
```


## [2026-10-15T02:45:20.624Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 85953,85996p POK_full.txt | cut -c1-260",
 "description": "Print Pokorny ter-2, teru- entry"
}
```


### [2026-10-15T02:45:21.078Z] TOOL RESULT

```
Root / lemma: ter-2, teru- 

Meaning: feeble, fragile, weak 

Note: (to ter-^mb' as 'ab-, faded, weakened ') 

Material: Gr. Tspnv 'tender', sabin. /e'/'e'/7^/77"molle', Latin (after /e'/7^/s reconverted with 

metathesis) tener, -a, -um "tender, soft'; 

from the ^-basis: Old Indie taruna-, dial, talina-' young, tender' (m. f. ' youngling, girl', n. 
"sprout, stem '), Avestan tauruna-^ young ', osset. tarin^ knave, boy'; 

gr. Tspu daQzvto,, Aehtov Hes., Tspusc; TnTTOi "abgejagte horse' (tspugketo STsipero Hes.: 
Tspu = (jeGuoku) : psGu), T£puvr|<; 'iZ^p\\x\xiyo(; 6vo(;, Kai yspcov Hes.; 

Latin tarcfus's\o\N, slack, zogernd' as c/lo-derivative of a reduced-grade %ru-7; Old Irish 
terc' sparse, small'; 

zur T£pr|v-group as " young, tender; young boy, the young of an animal ' also tomo-s\n 
Lithuanian /a/775S "servant'. Old Indie tarna-, tarnaka-m. " the young of an animal, calf; 
Armenian t'orn, Gen. /'0/7/7 "grandchild, grandson'; 

alb. //7/77 "valiant, gamy; m. young man', PI. //7/77a"bewaffnete Gefolgsmanner' {trmo), if 
"young boy, jugendkraftig' die meaning-development war; 

Note: 



This seems wrong etymology since alb. maybe alb. trim "brave, not scared' is related to 
alb. alb. Tosc tremp, Geg trem^\ scare'; Latin tremo, -e/ie 'tremble' from Root / lemma: 
trem-, trems-: "to thump; to tremble' (see below). 

Armenian farm^ young, fresh, green', perhaps Old Icelandic Ay/777a "spare, look after' as 
derivative eines *f^ormaz^ weak, tender'; is Latin termes, -///s"abgeschnittener twig, 
branch' die lengthened grade in addition? men-iorxus in gr. Tspapwv "tender, light kochbar', 
QTspapajv "hard, raw', hom. aiEpapvoc; "hard, unerbittlich, unbeugsam'; presumably Gothic 
^a/7/75"ungewalkt, new (from kerchief, cloth)', actually "fresh'. 

References: WP. I 728, WH. II 648 f., 665, 670 f., Mayrhofer 1 , 483. 
Page(s): 1070-1071 

Root /lemma: ter-3, tera-and ten-, tn-
```


## [2026-10-15T02:45:24.522Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['KLN','SKT','HRN','BQT','SNS','MON','AHD']:print(k,d[k].get('page_offset'),'|',d[k].get('lookup_hint'),'\\n')\"",
 "description": "Get page offsets for references"
}
```


### [2026-10-15T02:45:25.018Z] TOOL RESULT

```
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages. 

SKT leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags. 

HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann. 

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor) 

SNS 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping. 

MON None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks). 

AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
```


## [2026-10-15T02:45:27.385Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in '^tender,' '^taffeta,' '^tape,' '^tapestry,' '^guitar,' '^cithara,' '^zither,' '^cittern,' '^sitar,' '^kithara'; do echo \"== $w\"; grep -n \"$w\" KLN_1966.txt | head -3; done",
 "description": "Find Klein headwords"
}
```


### [2026-10-15T02:45:27.799Z] TOOL RESULT

```
== ^tender,
38537:tender,  tr.  and  intr.  v.,  to  offer.  —  MF.  tendre,  ‘to stretch,  hold  out;  to  offer’  (whence  F.  tendre, ‘to  stretch’),  fr.  L.  tendere.
== ^taffeta,
38011:taffeta,  taffety,  n.,  a  fine  smooth  lustrous  silk cloth.  —  ME.  taffeta,  fr.  MF.  (=  F.)  taffetas,  fr. It.  taffeta,  fr.  Pers.  tdftah,  ‘twisted  fabric’,  fr. taftan,  ‘to  shine;  to  spin,  twist’.  See  tapestry, taffrail,  also  tafferel,  n.,  the  rail  across  the  stern of  a  ship.  —  Du.  tafereel,  dimin.  of  tafel,  ‘table’, which,  together  with  OHG.  zabal  (MHG. zabel),  ‘board,  plank’,  OHG.  tavala,  tabala (MHG.  tavele,  G.  Tafel),  ‘table,  board’,  is  bor¬ rowed  fr.  L.  tabula,  ‘board,  plank’;  see  table. The  form  taffrail  arose  through  the  assimilation of  the  ending  of  tafferel  to  E.  rail. taffy,  n.,  candy  made  of  sugar  or  molasses.  —  F. tafia.  See  tafia.
== ^tape,
38174:tape,  n.  —  ME.  tappe,  tape ,  fr.  OE.  tseppa,  teeppe, ‘tape,  ribbon’,  prob.  back  formation  fr.  L. tapete,  ‘carpet’,  whose  ending  -te  was  mistaken for  a  suff.,  and  consequently  dropped.  See tapestry  and  cp.  words  there  referred  to. Derivative:  tape,  tr.  v.
== ^tapestry,
38176:tapestry,  n.  —  ME.  tapistry,  fr.  MF.  (=  F.)  ta- pisserie,  fr.  tapis,  ‘carpet’,  fr.  OF.  tapiz,  fr. tapition,  the  MGk.  pronunciation  of  Gk.  xa- itrj xtov,  dimin.  of  tivrqc,,  gen.  xa7n)xoq,  ‘hang¬ ing,  carpet’  (whence  L.  tapes,  gen.  tapetis),  a word  of  Iranian  origin.  Cp.  ModPersian  tab-ad, inf.  tdftan,  tab-i-San,  ‘to  turn,  twist’,  fr.  Iranian *tap-,  corresponding  to  I.-E.  *tmp-,  ‘to  stretch, extend',  whence  L.  tempium,  ‘place  of  observa¬ tion,  temple'.  See  temple,  ‘place  of  worship’, and  cp.  words  there  referred  to.  Cp.  also  taffeta, tape,  tapetum,  tapis.
== ^guitar,
== ^cithara,
== ^zither,
== ^cittern,
== ^sitar,
== ^kithara
```


## [2026-10-15T02:45:32.800Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; leaf(){ awk -v L=$1 'NR<=L' KLN_1966.txt | tr -cd '\\f' | wc -c; }; for l in 38011 38176; do echo \"line $l leaf $(leaf $l)\"; done; grep -n \"^guitar\\|^gittern\\|^cithara\\|^zither\\|^cittern\\|^cither\\b\\|^sitar\\|^tender, adj\\|^tender\\b\" KLN_1966.txt | head; grep -n -i \"^tender\" KLN_1966.txt|head",
 "description": "Compute Klein leaves and find more headwords"
}
```


### [2026-10-15T02:45:33.324Z] TOOL RESULT

```
line 38011 leaf 830
line 38176 leaf 833
7787:cither,  aiso  cithern,  a  stringed  musical  instru¬ ment.  —  F.  cithare,  fr.  L.  cithara,  fr.  Gk.  xtftapa, fr.  Pers.  sihtdr.  Cp.  cithara,  citole,  cittern,  git- tern,  guitar,  kit,  ‘a  small  fiddle’,  zither, citizen,  n.  —  ME.  citezein,  formed — prob.  under the  influence  of  denizen — fr.  OF.  citeain  (F. citoyen),  which  was  formed  fr.  cite  (F.  cite)  with suff.  -am.  See  city  and  -an.
12741:cither,  adj.,  pron.,  conj.  and  adv.  —  ME.  aither, either,  fr.  OE.  xghwseder,  xgder,  ‘each  of  two, both’,  for  *a-gi-hwseder,  which  is  formed  fr.  a, ‘ever’,  pref.  gi-  (for  ge-)  and  hwseder,  ‘whether’. See  aye,  ‘ever’,  pref.  y-  and  whether  and  cp. neither.  Cp.  also  Du.  ieder,  OHG.  eogiwedar, iowedar,  MHG.  iegeweder,  ieweder,  ieder,  G. jeder,  ‘either,  each,  every’, ejaculate,  tr.  v.,  to  exclaim.  —  L.  ejaculdtus,  pp. of  ejaculari,  ‘to  throw  out,  shoot  out’,  fr.  e-  and jaculari,  ‘to  throw,  hurl,  cast’,  it.jaculum,  ‘dart, javelin’,  from  the  stem  of  jacere,  ‘to  throw’.  See jet,  ‘to  spirt  forth’.
38537:tender,  tr.  and  intr.  v.,  to  offer.  —  MF.  tendre,  ‘to stretch,  hold  out;  to  offer’  (whence  F.  tendre, ‘to  stretch’),  fr.  L.  tendere.
38537:tender,  tr.  and  intr.  v.,  to  offer.  —  MF.  tendre,  ‘to stretch,  hold  out;  to  offer’  (whence  F.  tendre, ‘to  stretch’),  fr.  L.  tendere.
```


## [2026-10-15T02:45:39.902Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; leaf(){ awk -v L=$1 'NR<=L' KLN_1966.txt | tr -cd '\\f' | wc -c; }; echo cither $(leaf 7787); grep -n -i \"guitar,\\|^gui-\\|zither,\\|cittern,\\|cithara,\\|^sitar\\|sitar,\" KLN_1966.txt | head; grep -n \"tender,  adj\\|^tender, *adj\" KLN_1966.txt",
 "description": "Find more Klein entries"
}
```


### [2026-10-15T02:45:40.448Z] TOOL RESULT

```
cither 165
7786:Derivatives :  cit-abie,  adj.,  citation (q.v.),cit-er,n. cithara,  n.,  an  ancient  musical  instrument  re¬ sembling  a  lyre.  —  L.,  fr.  Gk.  xibdtpx.  See next  word.
7787:cither,  aiso  cithern,  a  stringed  musical  instru¬ ment.  —  F.  cithare,  fr.  L.  cithara,  fr.  Gk.  xtftapa, fr.  Pers.  sihtdr.  Cp.  cithara,  citole,  cittern,  git- tern,  guitar,  kit,  ‘a  small  fiddle’,  zither, citizen,  n.  —  ME.  citezein,  formed — prob.  under the  influence  of  denizen — fr.  OF.  citeain  (F. citoyen),  which  was  formed  fr.  cite  (F.  cite)  with suff.  -am.  See  city  and  -an.
7789:citizen  of  the  world,  a  cosmopolitan.  —  Loan translation  of  Gk.  xocrfiOTroXlT/ji;,  ‘a  cosmopoli¬ tan’,  lit.  ‘a  citizen  of  the  world’, citole,  n.,  a  kind  of  dulcimer  (obsol.)  —  OF.,  fr. L.  cithara,  fr.  Gk.  xtDapx ;  see  cither.  The  ending of  L.  cithara  was  mistaken  for  a  suff.  and  this alleged  suff.  was  changed  into  suff.  -ole. citra-,  pref.  meaning  ‘on  this  side  of’.  —  L.  citrd, rel.  to  cis,  ‘on  this  side’.  See  cis-. citramontane,  adj.,  on  this  side  of  the  noun- tain.  —  Formed  fr.  citra-  and  montane.  See  cis¬ montane.
7792:Citrus,  n.,  genus  of  shrubs  and  trees,  including citrons,  lemdns,  etc.  —  L.  citrus,  ‘citron  tree’, fr.  Gk.  xsSpo?.  See  citron, citric,  adj.  —  Formed  fr.  prec.  word  with  suff.  -ic. cittern,  n.  —  A  var.  of  cither(n). city,  n.  —  ME.  cite,  fr.  OF.  cite  (F.  cite),  fr.  L. civitatem,  acc.  of  civitas,  ‘citizens  of  a  commu¬ nity,  citizenship,  state’,  fr.  civis,  ‘member  of  a community,  citizen’.  See  civil  and  -ty  and  cp. Olt.  cittade  (whence  It.  cittd),  OProveng.  and Catal.  ciutat,  Sp.  ciudad.  Port,  cidade,  ‘city, town’,  Rum.  cetate,  ‘castle,  fortress’,  which  all derive  fr.  L.  civitatem.
11878:dital,  n.,  a  fingerkey  by  which,  in  a  harp  guitar, the  pjtch  can  be  raised  a  semitone  (music).  — Formed  with  suff,  -al  fr.  It.  dito,  ‘finger’,  fr.  L. digitus.  See  digit  and  cp.  digital, ditch,  n.  — •  ME.  dich,  fr.  OE.  die,  rel.  to  ON. diki,  ‘dike,  ditch’,  OS.,  OFris.,  MLG,</iJi,  MDu. dijc,  Du.  dijk,  MHG.  dich,  G.  Deich,  ‘dike’, MHG.  tich,  G.  Teich,  ‘pond’  (F.  digue,  ‘dike, dam’,  is  a  Dutch  loan  word).  These  words  prob. meant  orig.  ‘something  cut  out’,  and  derive  fr. I.-E.  base  *dheig-,  ‘to  cut  out’,  whence  also  L. figere,  ‘to  fix,  fasten,  drive  in’,  Lith.  diegiu, diegti,  Lett,  diegt,  ‘to  prick,  sting’,  Lith.  dygstu, dygti,  Lett,  dipt,  ‘to  sprout,  germ’,  Lith.  dygus, ‘pointed’,  dyglys,  ‘thorn’,  OPruss.  deicktas, ‘place’,  orig.  ‘point’  (for  sense  development  cp. point)  See  dike,  which  is  a  doublet  of  ditch. See  also  dig,  finis,  fix.
16185:gittem,  n.,  an  obsolete  musical  instrument  re¬ sembling  a  guitar.  —  ME.  giterne,  fr.  OF.  gai¬ ter  ne,  fr.  L.  cithara,  fr.  Gk.  xiffapa.  See  cither. Derivative:  gittern,  intr.  v.  (obsol.)  v
16845:guiser,  n.,  a  mummer  (Engl,  and  Scot.)  —  Formed fr.  guise  with  agential  suff.  -er. guitar,  n.,  a  stringed  musical  instrument.  —  F. guitare,  fr.  Sp.  guitarra,  fr.  Arab.  qitdrah,  fr. Gk.  xiffapa,  fr.  Pers.  sihtar.  See  cither  and  cp. gittern,  zither.
20728:kistvaen,  n.,  a  stone  coffin.  —  W.  cistfaen,  lit.  ‘a stone  chest’.  See  cistvaen. kit,  n.,  a  wooden  tub,  tankard.  —  MDu.  kitte (Du.  kit),  rel.  to  Norw.  kitte,  ‘bin’.  Cp.  kid, ‘a  small  tub’,  and  caboodle, kit,  n.,  a  small  fiddle  used  formerly  by  dancing teachers.  —  Abbreviation  of  OE.  cythere,  fr. L.  cithara,  ‘lute’,  fr.  Gk.  xiOxpx.  See  cither, kit,  n.  —  Abbreviation  of  kitten, kitab,  n„  a  book:  esp.  the  Koran  or  the  Bible {Mohammedanism).  —  Arab,  kitab,  book  ,  lit. ‘a  writing’,  fr.  Aram.  kfthdbh,  ‘a  writing’, klthabh,  ‘he  wrote’  (whence  Arab,  kdtaba,  he wrote’).  See  ketubah  and  cp.  words  there  re¬ ferred  to.
29135:Plectognathi,  n.  pi.,  an  order  of  teleost  fishes (ichthyol.)  —  ModL.,  compounded  of  plecto- and  Gk.  vvixll 05,  ‘jaw’.  See  gnatho-. plectrum,  n.,  a  small  piece  of  metal,  bone,  etc., used  for  plucking  the  strings  of  a  guitar,  man¬ dolin,  zither,  etc.  —  L.  plectrum,  fr.  Gk.  TrXrjx- Tpov,  ‘an  instrument  to  strike  with,  instrument for  striking  the  lyre’,  a  derivative  of  7tXfjaaeiv, ‘to  strike’.  See  plague  and  cp.  Aplectrum. pledge,  n.  —  ME.  plegge,  fr.  OF.  plege,  pleige, plaige,  etc.  (F.  pleige),  ‘hostage,  security,  war¬
33445:sack,  n.,  strong  wine.  —  Formerly  spelled  seek, fr.  F.  (v/n)  sec,  ‘dry  wine’,  fr.  L.  siccus,  ‘dry’. See  siccative  and  cp.  sec,  secco. sackbut,  n.,  1)  a  medieval  wind  instrument,  fore¬ runner  of  the  trombone;  2)  a  stringed  instru¬ ment  resembling  the  guitar,  in  Dan  3:5  used wrongly  to  translate  Aram.  sabb*kha.  —  MF. (=  F.)  saquebute,  fr.  OF.  saqueboute,  com¬ pounded  of  saquer,  ‘to  pull,  draw  out  ,  and bouter,  ‘to  thrust'.  See  saccade  and  butt,  ‘to strike’.
38538:Derivative:  tender,  n.,  offer,  tender-er,  n. tender,  adj.,  soft,  easily  broken.  —  ME.,  fr.  OF. (=  F.)  tendre,  ‘soft,  delicate,  tender’,  fr.  L.  tene- rum,  acc.  of  tener,  ‘soft,  delicate,  tender',  which is  prob.  rel.  to  Sabine  tereno-,  ‘soft,  delicate’, and  cogn.  with  OI.  tdrunah,  ‘young,  tender’, Avestic  tauruna-,  ‘young’,  Gk.  -reprjv,  ‘tender, delicate’.  Arm.  t'arm,  ‘young,  fresh,  green’, Goth,  parihs,  ‘not  fulled’,  prop,  ‘fresh’  (see  S. Feist,  Vergleichendes  Worterbuch  der  gotischen Sprache,  3rd  edition,  Leiden,  1936  ff.,  p.  490). It.  tenero.  Proven?,  tenre,  tendre,  Sp.  tierno, Port,  tenro,  ‘tender’,  also  derive  fr.  L.  tenerum. Derivatives:  tender-ize,  tr.  v.,  tender-ling,  n., tender-ly,  adv.,  tender-ness,  n.
```


## [2026-10-15T02:45:43.836Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; leaf(){ awk -v L=$1 'NR<=L' KLN_1966.txt | tr -cd '\\f' | wc -c; }; echo guitar $(leaf 16845) tender $(leaf 38538) tapestry $(leaf 38176); grep -n -i \"zither\" KLN_1966.txt | head -3",
 "description": "Compute Klein leaves for guitar, tender"
}
```


### [2026-10-15T02:45:44.398Z] TOOL RESULT

```
guitar 370 tender 840 tapestry 833
7787:cither,  aiso  cithern,  a  stringed  musical  instru¬ ment.  —  F.  cithare,  fr.  L.  cithara,  fr.  Gk.  xtftapa, fr.  Pers.  sihtdr.  Cp.  cithara,  citole,  cittern,  git- tern,  guitar,  kit,  ‘a  small  fiddle’,  zither, citizen,  n.  —  ME.  citezein,  formed — prob.  under the  influence  of  denizen — fr.  OF.  citeain  (F. citoyen),  which  was  formed  fr.  cite  (F.  cite)  with suff.  -am.  See  city  and  -an.
16845:guiser,  n.,  a  mummer  (Engl,  and  Scot.)  —  Formed fr.  guise  with  agential  suff.  -er. guitar,  n.,  a  stringed  musical  instrument.  —  F. guitare,  fr.  Sp.  guitarra,  fr.  Arab.  qitdrah,  fr. Gk.  xiffapa,  fr.  Pers.  sihtar.  See  cither  and  cp. gittern,  zither.
29135:Plectognathi,  n.  pi.,  an  order  of  teleost  fishes (ichthyol.)  —  ModL.,  compounded  of  plecto- and  Gk.  vvixll 05,  ‘jaw’.  See  gnatho-. plectrum,  n.,  a  small  piece  of  metal,  bone,  etc., used  for  plucking  the  strings  of  a  guitar,  man¬ dolin,  zither,  etc.  —  L.  plectrum,  fr.  Gk.  TrXrjx- Tpov,  ‘an  instrument  to  strike  with,  instrument for  striking  the  lyre’,  a  derivative  of  7tXfjaaeiv, ‘to  strike’.  See  plague  and  cp.  Aplectrum. pledge,  n.  —  ME.  plegge,  fr.  OF.  plege,  pleige, plaige,  etc.  (F.  pleige),  ‘hostage,  security,  war¬
```


## [2026-10-15T02:45:48.974Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 370 830 833 840; do echo \"=== leaf $L\"; awk -v L=$L 'BEGIN{RS=\"\\f\"} NR==L+1' KLN_1966.txt | grep -o \"\\b1[0-9]\\{3\\}\\b\\|\\b[5-9][0-9]\\{2\\}\\b\" | head -5 | tr '\\n' ' '; echo; done",
 "description": "Find printed page numbers on Klein leaves"
}
```


### [2026-10-15T02:45:50.103Z] TOOL RESULT

```
=== leaf 370
686 1738 1814 1789 1663 
=== leaf 830
1566 
=== leaf 833
1572 1922 
=== leaf 840
1936
```


## [2026-10-15T02:45:54.275Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==563' SKT.txt | grep -n -i -A3 \"taff\\|tape\\|tapis\\|tapest\" | cut -c1-300 | head -40",
 "description": "Read Skeat page 542"
}
```


### [2026-10-15T02:45:54.735Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:45:57.244Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^TAFFETA\\|^TAPE\\|^TAPESTRY\\|^TAPIS\\|^SITAR\\|^GUITAR\\|^ZITHER\\|^CITTERN\\|^CITHERN\\|^GITTERN\" SKT.txt; grep -c $'\\f' SKT.txt",
 "description": "Find Skeat headwords"
}
```


### [2026-10-15T02:45:57.959Z] TOOL RESULT

```
639
```


## [2026-10-15T02:46:00.022Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"taffeta\\|tapestry\\|guitar\\b\\|zither\\|cittern\" SKT.txt | cut -c1-400 | head -20",
 "description": "Search Skeat text loosely"
}
```


### [2026-10-15T02:46:00.465Z] TOOL RESULT

```
976:Arraa.  tapestry.  (F.)  So  named  tnm Arras,  in  Aitois,  north  of  Fraiice.
7756:Gobelin,  a  French  tapestry.  (F.)  Nai
8124:Guitar ;  see  CMthem.
19055:K)Ur.  Tabor,  a  small  druio.  (F.- ^Atab.)  F.  tabour  tmod.  F.  tarn- .  —  Spun,  tambor,  atambor  { where  a  ^ e  Arab.  def.  article).  — Ar.ib.  tamhiir^ ]d  of  lute  or  guitar  with  a  long  neck. ix  bnu%  stnng5,  also  a  drum.*  Prob. litative  origta;  cf.  Arab,  iabbdl,  a mrr.  Der.  ta^ur-et  or  tabret,  a i.  form.
19081:flay,  co^tate  with  Tear  (i), Tadiwl©  :  see  Toad. Tafforel.  Ta^roil ;  see  Table, Taffeta,  Taffety.  a  thin  silk  staff.  (F.
19083:-  Ilal.  taffeU'i,  *  taffeta  ; '  Horio--  Pers.  tdf- iah,  twisted,  woven,  laffcta.  —  Pcrj. /d//aw, to  twist,  ftpin,  curl.
19180:Tapestry.  (F.-L.-Gk.)  Acorrupti of  the  old  form  tapisserie.^V.  tapiijerie, tapestry.  —  F.  tapisser,  to  fumiih  with taj^cstry,  —  F.  tapis,  ta]->cilry  hangings  ; Low  L.  tapen'us.^L.  tapttt,  cloth,  hang- ings.—Gk.  TQ»7T-,  stem  of  i^Mffi,  a  carpet, woollen  rag.  Cf.  Pers.  tabastah,  a  fringed carpet
22989:cithern  — guitar, clause  —dose,  xS,
23620:Freneh  from  Italian  from  Persian:  car- case (^carcass),  jargonelle,  mommy,  orange« rebeck,  taffeta  (u(^tV^^.
```


## [2026-10-15T02:46:03.030Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; leaf(){ awk -v L=$1 'NR<=L' SKT.txt | tr -cd '\\f' | wc -c; }; echo taffeta $(leaf 19081) tapestry $(leaf 19180); sed -n 19160,19185p SKT.txt | grep -i -A2 \"tape\" | cut -c1-300; grep -n -i \"cithern\\|Cittern\" SKT.txt | head",
 "description": "Skeat leaves and tape entry"
}
```


### [2026-10-15T02:46:03.614Z] TOOL RESULT

```
taffeta 514 tapestry 517
Ri,  and  G.  iopf,  a  top  of  a  tree,  a hail,  Iccl.  feppr,  a  tuft  or  lock  of Allied  to  Top  and  Tuft.  Der. ';  tap-sftr,  A.S.  tappistre^  a  fern. roa  or  ttrppen  tabove). tampicm,  a  kind  of  ping.  (F.-Teut.) I  tmmpam,  bong,  stopple;  nasalisrd  form F.  tapion,  the  same
taper  (s).  long  and  alendcr.  (C.  7) !■//''  means  (operlike,  shaped  like  the vtn,  use*!  in  churches,  which  were  soiiie> Lj^hlnner  at  the  top.  Hollami  has: ^Hbrur,  tharp-poioteu  b  the  top;*  tr.of
TARDY
491
--
Tapestry.  (F.-L.-Gk.)  Acorrupti of  the  old  form  tapisserie.^V.  tapiijerie, tapestry.  —  F.  tapisser,  to  fumiih  with taj^cstry,  —  F.  tapis,  ta]->cilry  hangings  ; Low  L.  tapen'us.^L.  tapttt,  cloth,  hang- ings.—Gk.  TQ»7T-,  stem  of  i^Mffi,  a  carpet, woollen  rag.  Cf.  Pers.
tape.  (L.  -Gk.)  M.  E.  iape,\\&o  tappt. A.  S.  tappt,  a  tape,  a  fillet ;  closely  allied to  AS.  tiUppet,  a  tippet.  The  A.S.  pl. ta/foH  probably  meant  strips  of  stuff  or cloth,  uorrowed  from  L  tapttt,  cloth ; see  above.
tippet  (L.-Gk.)  M.E.  tiptt,  teftt. A.S.  tappttt  a  tippet.  — L.  tapttt,  cloth (above).
Tapioca  (Brarilian.)  Brazilian  tipioka, the  poisonous  jnice  which  issues  from  the root  of  the  ca.^<>nva  when  pressed  (.Littr^) ; hence  tapioca,  which  is  also  prepared  from the  root  of  the  cassava.
7608:Gist;  see  Jet  (i). Gittern ;  see  Cithern. Give.  tF«)  M.E.gelun,yflun(So^x^hcTn^. ^^ (.Northern) ;  pi- ya/ or  ga/.  pp.  yitsen, gifen,  youiH,  A.  S.  gt/an,  pi.  L  gea/,  pp. ^/m.  +  Du.  geven,  Icel.  gefa,  Don.  gwt, Swed.  gi/va,  Goth,  giban.  G.  gebetf.
9710:Kit  (3),  a  small  violin.  (L..Gk.)  Sht for  A.S.  tytere,  a  citiexn  ;  from  L  citkan see  Cithern.
22989:cithern  — guitar, clause  —dose,  xS,
```


## [2026-10-15T02:46:09.169Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *[θ0Ѳ]a[nq]g\\|ϑang\\|θang\\|^ *tan- \\|tauruna\\|taurvna\" BRT.txt | head -30",
 "description": "Search Bartholomae for Avestan forms"
}
```


### [2026-10-15T02:46:09.998Z] TOOL RESULT

```
12100:•  j.  tauruna-  Adj.  'jung'  von  Menschen und  Tieren:  yS  yaiia  pu'hnm  "mm  hao- mam  vanäalta  masyS  "wer  den  H.  wie einen  jungen  Sohn  lobt"  Y.  10. 8;  —  spä 'äj  "ein  junger  Hund"  V, 5. 30";  —  spämm .  .  yim  »ffw»  V.  13. 1  $,  23,  27».  a)  m. 'Knabe':  ma  apinnHyu  'na  mS  kainina anupaitä  (sd.)  mafyänqm  "nicht  unmündige Knaben,  nicht ..  Mädchen"  Yt,/7. 54;  55.
20914:iiäyu  tauruna  ySi  iainina  anupaSa  Yt 17.  SS'  d)  NPC:  upa  IB  n3  iaa  ya alaonam  mosu  *ti3ntö  fravasayö  Yt.  13. 46;  —  vfaärayat  sp)ntB  mainyus  yä  a
```


## [2026-10-15T02:46:13.737Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"ang-  \\|anj- \\|anj-  \\|ang-\\s*V\\|'ziehen\\|„ziehen\\|spannen'\" BRT.txt | cut -c1-250 | head -30",
 "description": "Search Bartholomae for thang entries"
}
```


### [2026-10-15T02:46:14.100Z] TOOL RESULT

```
6993:drang-  V.  ('festhalten')  'an':  ydi  ä  vanhsus mananAs  didray%S.duy?  Y.  4S.  7.  b)  un- räumlich,  zur  Angabe  a)  des  Mittels  'mit- telst, durch,  kraft':  ys  zaotä  aSä  imüS hvS "mait^Sui  3  vahistat  kayä  (sd.)  , .  västrya ^-
13612:mp,  Praes.  {aft)  dandel  'er  ve^isst'  N.  //> (Fol.  ig.  21,  10.  7),  Vr.  2.  8  (Sp-),  Y.  /p.  12 (Sp.).  54. 21  ISp.).  dand'  (wenn  richtig  gelesen -  West  SBE.  37.  455  'i=st  yang-  -)  würde ein  taa.'dam'  venreteui   s.
14063:■drang-  77  a
14068:•  j.,   g.    'drang-  V.   'firmare'.     Praes.
14075:•  j.  "drang-  V.  'auswendig  lernen'.  Praes, 7  i/iu/rJg-''<,  24  drmjaya-. — VVi^.draxta'.
14081:Ar.  *ii(iyaiig(/i)-,  m^.  dranJJian  (wohl  gelW.), ifraj^/ 'gelernt'.  —  Gehört  dazu  air.  rfrÄ-Afsong' (IFAni.  3.  lZ4)f  —  Vgl.  'äraag-,  womit  ich 'drang-  semasiologlsch  nicht  wohl  zu  ver- milteln  weist, —  Pä. :  dranjenitan
14259:•  j.  {t^ng-  V.  'ziehen'.  Praes.  14b  (In- koh.)  Sax/aru- ■',  30  (Iter.)  %anjaya-.  — PPfP.  ^axta-,  Inf.  •'haxta.
14266:von  allen  Gespannen  das  vorderste  lenke" Ytj.  50.  4)  '{das  Schwert,  den  Dolch) zücken':  haxiayat  pars  ankuyät  (Sp. iiou.)  Ytij.46;  —  %axta  arytaslifsd.) Vv  13.45-  5)  '(den  Pfeil)  anziehen, (denBogen)  spannen':  s.Auhaxi
14269:np.  öAanJida»  'ziehen';  1.  Hbm.  PSt.  10,  wozu
19849:•  g.  mang-  V.  'verherrlichen'.  Praes.  14 (Des.)  mimaySa-,
22839:•  j.  varak-  V.   'ziehen,  schleppen';  nur mit  Praev.     Praes.  a    varfca-,    3   v>rp!a:
23166:1)  'fahren';  i)  Irans.;  a)  von  Zugtieren sva.  'ziehen*:  srao&m  ..yim  ..  aurvanlS .. vatmti  Y.57.  37;  Yt.  ;o.  68,  47,  77. 12;  — aurvants  . .  vazimna  yim  vohüm  sraohm Y. 57.29;  —  s.  noch  'vazäna-,  b)  vom Wind;  a'hra
25162:•  j.  rang-  V.  'leicht,  flinlc  machen'. Fraes.  a  rmja-,  ranja-,  20  rava-'^,  30 (Iter.)  nnjaya-.
```


## [2026-10-15T02:46:16.568Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 14259,14275p BRT.txt | cut -c1-400; leaf(){ awk -v L=$1 'NR<=L' BRT.txt | tr -cd '\\f' | wc -c; }; echo leaf $(leaf 14259) tauruna $(leaf 12100)",
 "description": "Read Bartholomae thang entry"
}
```


### [2026-10-15T02:46:17.047Z] TOOL RESULT

```
•  j.  {t^ng-  V.  'ziehen'.  Praes.  14b  (In- koh.)  Sax/aru- ■',  30  (Iter.)  %anjaya-.  — PPfP.  ^axta-,  Inf.  •'haxta.
i)  '(den  Wagen,  Akk.)  ziehen',  von Rossen  usw.;  Med.:  yahmäi  .  .  aurvanta *yuxta  väia  (als  AP.)  ^anjasante  Yt  10. 13Ö;  —  te  mt  vai>m  "kanjayänte  \l.  ig, 44.  2)  '(den  Strang,  Akk.)  anziehen', von  Rossen,  Med. ;  sva. ',  am  Strang)  ziehen' : aspaahs  .  .  mrätim  canma  (sd.)  %anja- ymfe  \X.i'j.i2.  3)  '(den Wagen, Akk.) lenken',  vom  Fahrer,  Akt:  yat  vTspan
dby  Google
78s
Onngav-
■Swa-  I  I
786
von  allen  Gespannen  das  vorderste  lenke" Ytj.  50.  4)  '{das  Schwert,  den  Dolch) zücken':  haxiayat  pars  ankuyät  (Sp. iiou.)  Ytij.46;  —  %axta  arytaslifsd.) Vv  13.45-  5)  '(den  Pfeil)  anziehen, (denBogen)  spannen':  s.Auhaxia-.  ^ax- tanqm  Yt.  74.63:  lies  'hraxf.]
mit/ra  'heranfahren',  absol.voraFahrer: a^m  .  .  ya  .  .  fra%anjayäti  Yt  i-].  a.
mit  «r  '(das  Ross)  lenken,  zügeln',  vom Reiter:  s.  Inf.
np.  öAanJida»  'ziehen';  1.  Hbm.  PSt.  10,  wozu
Bthl.  IF.  10.  19z.    Vgl.  ferner  Zupitza  BB.
35.  89.  -  Pö.!  s.  Inf.  -  ')  S  3^9-
m  j.  Sangav-''  m.  Name  einer  Pflanze: yB  bansmqn  ^frasbrimte   Aaomasca  van-
lisca  (sd.)  %amasca  (AP.)"'  N.57.
Pü.  i  satrvar,  erl. ;  iamSn  i  (?,  Hds.  ad)  (^ren ; Tgl.  la  %aiaiatt:  —  O  SUmmansati  aruicher. -  '>  S  a/J.
•  j.  9'anvaii-,  S-anvar-  n.  'Bogen',  als Waffe  zumSchiessen:  hukaxtai  ha^a  'vanat YtiO.39;  —  aritayasca  kantayasca  'vanca (NP.)  isavasca  V.  ly.  9.  a)  Plur.  'Schiess- geiät',  d.  i.  Bogen  mit  Zubehör :  yailqm sayanam  ra%Sisti  .  .  tüirya  'van  (NP.) V.  14'.^.
leaf 448 tauruna 374
```


## [2026-10-15T02:46:21.356Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"tan-  V\\|tan-  V\\.\\|•  j.  tan-\\|tan- V\\.\" BRT.txt | cut -c1-400 | head; grep -n \"tauruna\" BRT.txt | head -3; awk 'BEGIN{RS=\"\\f\"} NR==375' BRT.txt | grep -o \"\\b6[0-9][0-9]\\b\" | head -3",
 "description": "Find Bartholomae tan- entry and col"
}
```


### [2026-10-15T02:46:22.313Z] TOOL RESULT

```
11936:•  j.,  g.  tan-  V.  'dehnen,  recken';  nur  mit Praev.  Praes.  lo  ianav- :  ianv-.  —  PPtP.
12100:•  j.  tauruna-  Adj.  'jung'  von  Menschen und  Tieren:  yS  yaiia  pu'hnm  "mm  hao- mam  vanäalta  masyS  "wer  den  H.  wie einen  jungen  Sohn  lobt"  Y.  10. 8;  —  spä 'äj  "ein  junger  Hund"  V, 5. 30";  —  spämm .  .  yim  »ffw»  V.  13. 1  $,  23,  27».  a)  m. 'Knabe':  ma  apinnHyu  'na  mS  kainina anupaitä  (sd.)  mafyänqm  "nicht  unmündige Knaben,  nicht ..  Mädchen"  Yt,/7. 54;  55.
20914:iiäyu  tauruna  ySi  iainina  anupaSa  Yt 17.  SS'  d)  NPC:  upa  IB  n3  iaa  ya alaonam  mosu  *ti3ntö  fravasayö  Yt.  13. 46;  —  vfaärayat  sp)ntB  mainyus  yä  a
643
644
```


## [2026-10-15T02:46:24.650Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 11936,11950p BRT.txt | cut -c1-300; sed -n 12100,12106p BRT.txt | cut -c1-500; awk 'BEGIN{RS=\"\\f\"} NR==372' BRT.txt | grep -o \"\\b6[0-9][0-9]\\b\" | head -3",
 "description": "Read Bartholomae tan- and tauruna"
}
```


### [2026-10-15T02:46:25.247Z] TOOL RESULT

```
•  j.,  g.  tan-  V.  'dehnen,  recken';  nur  mit Praev.  Praes.  lo  ianav- :  ianv-.  —  PPtP.
mit  US  'ausrecken,  ausstrecken':  uslänaii
:.  sastail^'>  "mit  (zum  Gebet)  ausgestreckten Händen"  Y-Z^-s-
mit  pairi  fernhalten  von  — '  {hala  mit AbL):  pairi  ß tanava (iSKA.)  .  .  untärum ha^a  acisist  anhaol  Y.7/.  15;  Y.ig.j;  — urvan9m..avavaitya  pairi.tanuya{i50M..)'^ ya>a  im  sä  Y.  ig.  7.
ai.  taiiiti,  uttäHÖi;  np.  tanidan  'spinnen';  s. DOCh  Pö.  —  Pü  (tu  Y.  19.  ^  1.  St.):  api  laaa- vän,  erl.!  afii girim.  {ru  Y.  /p.  ^  2.  St):  afZ tamtvihüh;  Sü,:  vüUiayilum;  Vü.  {^X  usläna-): unSwiSü.:  uttäna'.  — ")  Vgl.  Komp.,  Sp.407m. —  »)  w,  lanvTyä,  %  3^6  No
•  j.,  g.  tanü-  f.,  m.'*,  g.  tanuS-'*  n.  Xeib' 1)  der  Menschen  (und  menschenähnlich gedachten  Götter);  auch  sva.  'Person', wobei  die  obliquen  Ka^us  auch  im  Sinn von  ihn'  usw.,  sowie  -  mit  oder  ohne  Ava-, hava-  —  in  reflexiver  Bedeutung^*  im  Sinn von  'sich,  mich'
tanu-  I  634
zasta  ..hl..  frasttdhay?n  . .  ap»r3ttayBkahe ahe  (Sp. 6  m.)  havayhss  'nvB  V.  16.T,  —  im Gegensatz  lu  i'awj«-:  malsnta  yalibyS  alte I  nasu.kasa  frasnylnte  var^säsla  'nümca ". .  Leib(sva.Hau  t  J  und  Haare"  V.&  1 1 ;  Vd.4 ;
  iva  narqm  irislanam  'nüm  barüma
..  ksa  nidä^äma?  V.  o.  44;  Vd. /2;  — fraiä  fraydit  .  .  äpS  .  .  ya&Sii  upa.jasüit iristam  'nüm  V.  6^,27;  —  dättyS  kata  .  . attdüa  hs  uzbao\qm  'nüm  nidaihyqn  V. 3. 1 1  f.;  —  yal  *vTjvaA»  (sd.)  paiti  '««A astvä  gayü  *daryeite  FrW.  4.y,  —  ayarf ämi^naiti  (sd.)  
—  ayaahamaiS  kantaü  aidibii paiti  ava.- h^rp^yät  i&d.)  aosai»hai^ySs>  'nvif'V.4.$o;
—  'nvS  (VS.)  ikyejanuhaiti  Ao%.  25—28*;
—  yaiia  hl  hqm  ta/nS  Jasat  avi  'nuye zsi^uyt  \.y.^a■,  —  vohu  manö  paiti.- ral%waya/i  haifa  avaahat  'nvatyat  daivö.- jatayä  V.ig.io;  — yS  nairikayi  ä^ra- vaiiya  ..  'nüm  iri^yat  'W.i6.ii\;  —  iata MH  (sd.)  *paitisama  frya  paüi  -nvi-  Yt ij.  10;  —  fra  'nvo  rmjayeiti  
—  kaomsm  .  .  patär>m  °nuye  haire  Yt 14.ST,  —  par^ndTm  . .  ya  narqm  v^srsp- tacif(sA.)  'nvS  baoxtärim  dahäiti  Vr.7, 3;
—  haom  'nüm  gutaUa  Yt.  4-  4 ;  —  <iat  az?m (näml.  aus)  'nüm  agute  (sd.)  ". .  mich  . ," Yt.  77.55;  S^i  — yS  . .  havaiibya  bäsubya 'nuye  ravs  aisiits  (sd.)  ".  .  sibi  . ."  Vt 7^.107;  —  narSm  nar)m  s^ahyäi  'nuyl . .  ahmai  nS  sazdyai  (sd.)  baodants  paiti Y.30.2; — 
•  j.  tauruna-  Adj.  'jung'  von  Menschen und  Tieren:  yS  yaiia  pu'hnm  "mm  hao- mam  vanäalta  masyS  "wer  den  H.  wie einen  jungen  Sohn  lobt"  Y.  10. 8;  —  spä 'äj  "ein  junger  Hund"  V, 5. 30";  —  spämm .  .  yim  »ffw»  V.  13. 1  $,  23,  27».  a)  m. 'Knabe':  ma  apinnHyu  'na  mS  kainina anupaitä  (sd.)  mafyänqm  "nicht  unmündige Knaben,  nicht ..  Mädchen"  Yt,/7. 54;  55.
ai.  tdruffa-  Adj. ;  np.  vgl.  lar.  —  Wegen  np. eh  'jniiEer  Hund'  s.  IFAni.  10.  22.  —-  Pü.! faranai,  Sfi.:  JiSuA.  —  >)  ifiä  'no  bezeichnet nach  meiner  Ansicht  den  un ausgewachsenen Hund  jeder  beliebigen  Basse  (vgl.  V.  /j.  10  fT.), '. der  eben  wegen  seiner  Jugend  noch  nicht  in  1 bestimmter  Richtung  Tervrendet  werden  kann.  | DST.  ZA.  3.  197  meint  mit  Andern,  ea  sei  . der  Jagdhund  darunter  lu  verliehen,  vgl, draxlB-kunara-,  s.  aber  die 
•  j.  tanp-  V.  'stehlen',  Praes.  27  trpjya-'\
mit  Akk.  der  Person  und  der  Sache:  yH
mam    tal   draenS  zinät  (sd.)  va  tnjyäl^''
vä  apa  vä  yäsaiii  Y.  11. 5.
Vgl.  ai-  'Irt-  Adj.  'stehlend'  (KZ.  35.  311). mp.  lirß*)  'DiebsUhl';  alles  übrige  (Horn NpEt.  86,  Hbm.  PSt  185)  ist  unsicher.  — Pü.:  HrflFnUan').  —  ')  Statt  bn/y',  %  368. 39.  —  ")  Vgl.  zu  taya-  und  l^vis:  Wie  zu lesen?  Wl.  Iri/t°,  Analogiebildung  nach^r^* (IF.  II.  ia6),  wenn  man  annehmeD  darf,  dass air.  *lffjati  zu  mp.  'Grcl  führte,  wie  "g^iiaii zu  gira  (IF.  12.  107).
639
640
```


## [2026-10-15T02:46:30.431Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"hanj\\|farhang\\|frahang\\|ähang\\|ahang\\|hixtan\\|hlxtan\\|hïxtan\\|tâftan\\|täftan\\|taftan\\|tö'la\\|tula\\|tôla\\|tär \\|tar  \\|taräna\" HRN.txt | cut -c1-250 | head -40",
 "description": "Search Horn for headwords"
}
```


### [2026-10-15T02:46:30.784Z] TOOL RESULT

```
675:24. ästär nur in IxnDN (Is. 24, 20) 'Sünde , jN:nNnDN
850:ämurzltär Verzeihen' ; ai. ä -j- [/'marj- Vegwischen .
961:phlv. ahanjitan 'ziehen, fortziehen* (vd. 5 (146) 61.;
963:Die Bedeutungen von ap. l/^hanj-, frahanfam *ich
973:Kärn. 38; arm. LW. hrahang), ferhenjukn 'erziehen.
1394:ap. *hanjäma' 'Ende, Abschluss' ; aw. vergl. henjas-
1403:ap. *hanjamana-; phlv. hanjaman bezw. anjaman;
3282:Bei Ibn Beitär (Leclerc, Vol. III, No. 1655) ist das
3468:369. {i)tär 'Faden.
3471:370. {2)tär 'finster', tarik, I^nDDnND (Is. 50, 10).
3492:Fieber*; ai. [^tap-, tdpati; phlv. täftan 'sieden' (vd. 4
6761:phlv. östaftan ') (vd. 7 (27) GL, 18 (98), Meii.) eilen,
9556:Vergl. s. V. rthenjuien (No. 58); phlv. päz. hanjifan,
9557:hanjet (PPGl.).
9771:58. Lies ap. ha(n)j-, fraha{n)jam statt hanj-, frahanjam,
10053:11. amültär unverletzbar'.
10120:24. artestär 'Krieger, artestärän salär (Karnäm. S. 67
10591:105. hamestär Gegner, Widersacher, hamestärih (Men.,
10700:125. katär 'welcher von beiden?' (AW.-Komm., AV.).
10978:177. sästär 'Herrscher, Tyrann* (AW.-Komm., AV.).
11381:241. i^tnitan 'wegnehmen'; zlmtär (ZPGL). Selten.
13284:perestär 298.
13507:röc/ftär 158, 627.
15617:arfeStär 24.
15716:besitär 49.
16125:' hanj&mxi-Vnn 118.
16656:I portär 360.
16839:f<ästär 177.
17157:rOJcärtär 917.
20844:n. tär 370.
22259:' hrahang 58, 812 Anm.
```


## [2026-10-15T02:46:33.657Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 950,980p HRN.txt; echo ----; sed -n 3460,3500p HRN.txt; leaf(){ awk -v L=$1 'NR<=L' HRN.txt | tr -cd '\\f' | wc -c; }; echo leaf58 $(leaf 961) leaf369 $(leaf 3468)",
 "description": "Read Horn nos. 58 and 368-371"
}
```


### [2026-10-15T02:46:34.488Z] TOOL RESULT

```
{ahe/ten)^); ahenje^),
*) So (Wörterbücher: ävengän) steht im facsimilirten Text des
Seljuqname, bei Sohefer 76, 7. (Ich verdanke dieses Citat Prof.
Nöldeke.)
^) Nach dem BQ soll äyen eine Nebenform zu np. ähen sein;
Belege fehlen.
^) Schrader, Sprachvergleichung und Urgeschichte*, 286 be-
friedigt nicht; die zweite Auflage ist mir nicht zur Hand.
*) Rück er t zieht ZDMG. 8, 264 vielleicht mit Recht auch np.
ä/tcn hierher; dann vergl. auch yä/ten^ yäzlden,
5) Bei. LW. C?) ähihjag, n. ähenjuy *ßaiid, Gürtel' (U).- 15 -
phlv. ahanjitan 'ziehen, fortziehen* (vd. 5 (146) 61.;
19 (94) GL); vergl. Mxtan, Mjah 'Eimer (Kärn. 65).
Die Bedeutungen von ap. l/^hanj-, frahanfam *ich
warf (?) (sie zu Ekbatana in die Festung)*, d. i. 'ich setzte
sie gefangen und ai. i^sanj- *hängen* passen nicht, doch
soll np. ahenjiden auch Verfen* bedeuten ^. Np. aheng
'Plan, Absicht* wird ebenfalls hierhergehören. Des-
gleichen np. ferhe/teiiy ferhi/ten^ ferdhi/Un (phlv. fra-
hä/Jan 'erziehen etc., frasäxtan, AV., sind nur fraJtä/tun
zu lesen), die ebenso wie berhe/ten^ berki/teu 'ziehen,
herausziehen* und 'erziehen bedeuten sollen; vergl.
ferheng, ferhenj 'Wissen etc.' (phlv. /raAaw^, Nöldeke,
Kärn. 38; arm. LW. hrahang), ferhenjukn 'erziehen.
59. ähu 'Gazelle*.
phlv. ahük 'Gazelle'.
kurd. ask; afy, ösai; bei. äak (19), LW. aü (15); ya/.
LW. ahü.
60. äyem 'ich komme*, äyende.
ap. *el + l^«y- ; päz. ü^d, aend {üyad, äyand),
kurd. e/w, ei, et etc. (Justi, Gramm. S. 235, Houtum-
----
(vd. 5 (57)), tacet (vd. 8 (287) flf.), tazad (vd. 8 (280),
13 (161)), tacak, tac{i)sn^ tacimtan (P. Vend.).
afy. tast\edal, tasal bezw. taxt\edal, ta/al 'fliehen,
weglaufen'; oss. d. t. fayd 'schnell', tajin 'fliessen,
t. fäjin 'tropfen* (241); bei. tacag ^ n. fasay, fäcag,
n. fäsay (Caus.) (374, 382); wa/. töcam 'ich bewege
mich', taydam 'ich ging, sar. tajam, tajänam (Caus.).
Vielleicht gehört np. tejä *heftig hierher.
369. {i)tär 'Faden.
aw. Hqx^ra-, vergl. ai. täntra- 'Zettel, Aufzug des
Gewebes.
370. {2)tär 'finster', tarik, I^nDDnND (Is. 50, 10).
aw. tqdra- 'finster (aus Hamsra-^ Hansra-, Brug-
mann, Grundriss II, 171); ai. tämisra- 'finster', tamisrä-
'Finsterniss, finstere Nacht' ; phlv. tär^ tar[tum (Bund.),
tärik, täriklh.
kurd. LW. tan; af/. tör^ LW. tärik; oss. d. talingä,
t. faliny 'Finsterniss, finster', far 'dicht, düster (vom
Wald)' wohl LW. (243); bei. LW. tär, n. tar (269);
sar. LW. tär, minj. tarävi,
371. täze 'frisch'.
bei. tajak 'frisch' (383); kurd. LW. taze,
Wohl zu No. 368.
'J Nicht causative Bedeutung.— 83 —
372. täften 'brennen, wärmen, leuchten', Praes. täb-em,
tob (vergl. aftah, mahtah), taw (Sahn. I, 149 Vers 367),
tahan, tabistan 'Sommev\ (jNnozxn, Jer. 40, 10; niwNP,
Ezech. 4, 3), teb Tieber, tebis^), tef 'Hitze (AM. S. 9,
Zeile 1), teften, feff.
g. tö (= tab); Käs. fömin^ töwessün, töwöHmun, tew
u. s. w.
aw. iXfap-, täpay^iii Varm machen', tafnu- 'Hitze,
Fieber*; ai. [^tap-, tdpati; phlv. täftan 'sieden' (vd. 4
(128) Gl.), tapet, taftak (vd. 3 (110)), tap (vd. 7 (145)),
fap(i)sn (vd. 20 (10)) 'Fieber ; arm. LW. tap, tauf,
tapak 'Esse' (phlv. täpak, ar. fabaq),
kurd. täw; af/. taba, töd (= "^faptd); oss. fö//,
t. /(?/' 'Hitze', fatcin 'wärmen' (247), äntäf, antaf (23) ;
bei. tap n. fap, taf, tafay, tafenay (379) ; wa/. andaw,
&avam, taf etc., sar. &avam, siyn. tSbam.
np. tefsiden 'heiss werden' (aw. tafsat, lat. tepesco)
leaf58 36 leaf369 103
```


## [2026-10-15T02:46:38.939Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3500,3520p HRN.txt; echo ----; awk 'BEGIN{RS=\"\\f\"} NR==111 || NR==112' HRN.txt | grep -n -B1 -A8 \"^ *[0-9]\\{3\\}\\. *ter\\|^ *[0-9]\\{3\\}\\. *tere\\|^ *[0-9]\\{3\\}\\. *tül\\|tül\"",
 "description": "Read Horn tāftan and tar entries"
}
```


## [2026-10-15T02:46:40.237Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *39[0-9]\\. \\|^ *40[0-9]\\. \" HRN.txt | head -30",
 "description": "List Horn entries 390-409"
}
```


### [2026-10-15T02:46:40.570Z] TOOL RESULT

```
np. tefsiden 'heiss werden' (aw. tafsat, lat. tepesco)
scheint entlehnt in oss. ftr/siw 'Hitze empfinden', bei.
tafsay *heiss werden .
Eine andere Wurzel fap liegt zu Grunde in
täften 'drehen, spinnen etc.', Praes. täh-em, täbiden^
tafte *Taflfet', tefne 'Spinnengewebe' (teblne, tef in, tefni
sind unbelegt) 2).
wa/. tow-am, si^^n. teb-am, sar. tab-am, Caus. tabän-
am 'winden, drehen etc.'
Sekundär wird zu täften ein Infinitiv tayten gebildet;
z. B. hat Sahn. I, 68 Vers 125 C. tä/ten statt des sonst
gewöhnlichen sinän täften 'drehen', ebenso wie sich ara-
bisch täytaj 'kostbares Tuch (in Nesäpür)' statt täftaj
findet (de Goeje, Bibl. geogr. arab. IV, 196). Vergl.
auch die Angabe des FS bei Vullers s. v. täyten.
*) AM. tehus S. 9 Zeile 9 (nach h mit n wie in cevhus ib. S. 75
Zeile 8).
V V
*) Np. tefne wird bei SF und ausserdem in FR, FJ durch einen
Vers Ö e h I d ' 8 belegt :
(Metr. Xeflf;
----
52-(21), Bund.), türuk bezw. töruk (vd. 5 (98), Var.,
53:Thonnelier)-); ai. tdruna-; kurd. tüle (LW.) junger
54-Hund, Jagdhund'.
55-Dagegen np. töre 'Schakal' ^) (g. törCy Käs. törä, türe^
56-tiird s. V. röbah und seyäl); phlv. törak (PPGl.); kurd.
57-tiire 'Otter' (H.-Sch.) ; bei. tölag, n. May 'Schakal' (398).
58-Np. töle etc. beruhen auf «-Epenthese.
59-404. tih 'leer', tiht, tehi, ^mn (Is. 19, 3).
60-g. tohl,
61-aw. tusen^^ie entleeren sich' (Bartholomae, Studien
```


### [2026-10-15T02:46:40.652Z] TOOL RESULT

```
3658:390. fü/ 'Speichel*, tufek{'% dehen)^ tiifke (Gazoph. s. v.
3684:392. tem 'Staar (der Augen)' (AM.), ^Oin Finsterniss' (Is.
3689:393. ten 'Körper, Leib*, tenömend, vergl. arab. LW.
3696:394. tenjlden zusammenziehen ; trinken' (jüd.-pers., z. B.
3718:395. tund schnell, heftig, stark'.
3720:396. tunder, tundur ^Donner .
3725:397. tenuk *düun, zart, fein'.
3729:398. teng 'en^Q,
3735:399. tenlden 'drehen, spinnen', tede 'Spinnengewebe*, tane
3739:400. tHj tu, tö (FirdüsT)^) 'du, vergl. -et 'dein', -tan 'euer'.
3744:401. tuvan 'vermögend, mächtig', tuvanä, tuvanisten.
3749:402. töften 'sammeln; ausgeben, zahlen', Praes. töz-em;
3765:403. töle 'junger Hund' (SF).
3774:404. tih 'leer', tiht, tehi, ^mn (Is. 19, 3).
3796:405. teheniy tehm *stark'^).
3800:406. Ur^) 'Pfeil', tlrkes, terkes 'Köcher 5^).
3834:407. tere *finster , tereyt^) (auch in Indien spricht man heute
3838:408. f^;s: *scharf, heftig; schnell', tej 'PfeiF; tese *Axt*2).
3846:409. tey *spitz, Schwert', % (nicht belegt).
9922:391. Zu phlv. tag vergl. Justi, ZDMG. 46, 289.
```


## [2026-10-15T02:46:44.086Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3735,3739p HRN.txt; sed -n 3765,3774p HRN.txt; grep -n \"^ *3[0-9][0-9]\\. *t[eä]r\\b\\|^ *3[0-9][0-9]\\. *ter \\|ter 'feucht\\|'feucht\\|terane\" HRN.txt | head; leaf(){ awk -v L=$1 'NR<=L' HRN.txt | tr -cd '\\f' | wc -c; }; echo leaf403 $(leaf 3765)",
 "description": "Read Horn 399, 403, and search tar"
}
```


### [2026-10-15T02:46:44.598Z] TOOL RESULT

```
399. tenlden 'drehen, spinnen', tede 'Spinnengewebe*, tane
'Zettel, Aufzug (am Webstuhl)'.
aw. [/^tan-; phly, tatak, vd. 7 (36) (für aw. täfdaena-):
ai. |/"^aw-, tanoti, 'dehnen, spannen'.
400. tHj tu, tö (FirdüsT)^) 'du, vergl. -et 'dein', -tan 'euer'.
403. töle 'junger Hund' (SF).
aw. {spO) taiirimö; phlv. taritk (vd. 13 (45), y. 10
(21), Bund.), türuk bezw. töruk (vd. 5 (98), Var.,
Thonnelier)-); ai. tdruna-; kurd. tüle (LW.) junger
Hund, Jagdhund'.
Dagegen np. töre 'Schakal' ^) (g. törCy Käs. törä, türe^
tiird s. V. röbah und seyäl); phlv. törak (PPGl.); kurd.
tiire 'Otter' (H.-Sch.) ; bei. tölag, n. May 'Schakal' (398).
Np. töle etc. beruhen auf «-Epenthese.
404. tih 'leer', tiht, tehi, ^mn (Is. 19, 3).
3582:{d)ter, terr, terri (AM.) 'feucht, frisch*; vergl. terane
9003:1039. nem 'feucht; Feuchtigkeit'.
9004:aw. napta- 'feucht' {[/^nab-, namb- d. i. nabh-,
9008:kurd. LW. tiem; afy. lünd 'feucht'; bei. wami *Tau,
leaf403 111
```


## [2026-10-15T02:46:48.404Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3576,3592p HRN.txt; leaf(){ awk -v L=$1 'NR<=L' HRN.txt | tr -cd '\\f' | wc -c; }; echo $(leaf 3582)",
 "description": "Read Horn tar entry"
}
```


### [2026-10-15T02:46:49.371Z] TOOL RESULT

```
11), Bartholomae, Ar. Forsch. II, 181; phlv. tarlmi-
n(i)smh 'Hochmut*, far^ ta7*tli anmassend' (AV., Men.) ;
ai. vergl. tirds, sowie skr. tiras +- Aar- (PW. tirds c, /)
*schmähen , tadeln , verachten*, tiraskära- 'Schelten,
Schmähen, Geringachtung', tiraskriya, wozu np. ter
§uden gewissermassen das Passiv ist.
{d)ter, terr, terri (AM.) 'feucht, frisch*; vergl. terane
'schöner Jüngling' ä).
aw. vergl. tauruna- jung'; ai. tdruna- jung, zart';
gr. Ti()7jy.
oss. färin 'Knabe' (246).
Die Etymologie wird wohl trotz des Bedeutungs-
unterschiedes durch Abu Mansür Muvaffaq's terr^)
gesichert; allerdings schreibt dieser auch nerr,
*) Vergl. Hell II, Kulturpflanzen und Haustiere'', 299.
*) Ich glaube nicht, dass hier eine übertragene Bedeutung von
ter *feucht* Yorliegt ; vielleicht auch nicht in der Phrase ter kerden zebän
106
```


## [2026-10-15T02:46:54.307Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"hi/ten\\|hixten\\|hiyten\\|hi/ten\\|äh[iï][x/y]t\" HRN.txt | head; sed -n 935,950p HRN.txt",
 "description": "Search Horn for āhīxtan"
}
```


### [2026-10-15T02:46:54.638Z] TOOL RESULT

```
968:gleichen np. ferhe/teiiy ferhi/ten^ ferdhi/Un (phlv. fra-
11443:ähixten 58.
lasse. Die von Fr. Müller (WZKM. 5, 184) verglichene
altslavische Wurzel stimmt lautlich nicht zu den
iranischen Formen.
57. ähen 'Eisen'; ähemn 'eisern 2).
Semn. ösün; g. vuhen,
phlv. äsm (z. B. vd. 5, 121), ämtm 'eisern*.
kurd. hasin ^ hesin (Jaba-Justi), üsin (Houtum-
Schindler) 'Eisen ; bei. LW. ahin (18); wa;^- «'^'^ (?)•
Das Verhältniss zu af/. öspana ,, öspma; oss. äfsan
(42); ^iyn, sar. spiu 'Eisen* ist nicht aufgeklärt^). Fr.
Müller (WZKM. 5, 258) denkt für diese Worte an
Zusammenhang mit phlv. spenäk; eine Wurzel ad^-
schneiden* im Altpersischen anzunehmen, liegt jeden-
falls meines Erachtens kein genügender Grund vor.
58. ahen^J^den 'ziehen, herausziehen*, vergl. ahi/Jen
{ahe/ten)^); ahenje^),
```


## [2026-10-15T02:46:59.184Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"θanj\\|θanǰ\\|Oanj\\|θang\\|\\*tanH\\|\\*tan-\\b\\|\\*tap\\b\\|\\*tap-\\|\\*taf\" CHEUNG.txt | head -20",
 "description": "Search Cheung for roots"
}
```


### [2026-10-15T02:46:59.844Z] TOOL RESULT

```
3298:*tap ‘to seize, attach, stick, strike’ 
5447:*NEIR: (?) Pash. téyal ‘to roast’ (rather *tap ?), Sh. 0aw-/0ud (f. баа), 0áw-/Qud 
5718:fire’ (or < *ham- + *tap ?) 
20279:hardly yield NP -v in final position, cf. tab ‘fever’, tab ‘glow’ (*tap), x'ab ‘sleep’ 
21672:*Oanj ? 
24669:*tap ‘to warm up, heat’ 
24686:*tap 379 
25332:*tap ‘to twist, wind’ 
25351:*tmp- (> Ir. *tap-), cf. LIV, ibid. Explaining the forms as a secondarily arisen 
25464:Pres. aja-: IND. 3sg. YAv. fradanjaiieiti (Yt 17.2), med. 3р1. YAv. Oanjaüente (Yt 17.12), SUBJ. 15р. 
25465:YAv. Oanjaiieni (Yt 5.50), 3pl. YAv. Oanjaiiante (Yt 19.44) 
25892:development can be noticed in OCS pri-teZo (pri-teZati) ‘I acquire, work’, s.v. *Oanj. 
55127:*tap (s.v.), *zarH' (s.v.) 
55479:*rais (s.v.), *saiH (s.v.), *tap 
56887:ear), *tap 
58250:*kart’, апе, *tap 
58372:*Hrau, *naij, *snaH, *tap, 
58399:*gar’, *gars', *tap
```


## [2026-10-15T02:47:01.948Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25332,25360p CHEUNG.txt; echo -----; sed -n 25440,25510p CHEUNG.txt",
 "description": "Read Cheung *tap and *θanj entries"
}
```


### [2026-10-15T02:47:02.295Z] TOOL RESULT

```
*tap ‘to twist, wind’ 

*KHOTANESE: Khot. thauna- ‘cloth, silk’. © Initial th- is the result of the transfer of 
friction from internal to initial position, Sims-Williams 1983: 48. 

*CHORESMIAN: (+ *upa-) bd’by- ‘to twist’ || (+ *us-) ? m/(w)stnb- ‘to throw up, 
vomit’, m/stnby- (caus.) ‘to cause to throw up’. Ф As for m/(w)stnb-, m/stnby- cf. 
Samadi: "doch schwerlich zur stamb ‘stützen’.". = Samadi: 14 

*NWIR: NP täftan/täb- ‘to turn, twist, spin’, NP tab ‘twisting, curling lock’, Nn. 
tovna/tov-, Varz. towna/town- ‘to twist’ 

*NEIR: Yghn. tob-/tóbta, top-/tópta, Wa. tov-/tovd, Sh. täb-/täpt, Rosh. teb-/tept, 
Bart. tob-/topt, Sariq. top-/tipt-, Yzgh. tab-/tabt ‘to wind, spin’, ? Oss. I. tyn, D. tune 
‘sheet’, ? Oss. I. taebyn ‘prepared wool’ (LW), Pash. taw ‘twist, contortion, winding’ 
(prob. genuine) 

© The consistently long stem vowel of these Iranian (verbal) forms is puzzling (the 
inclusion of Chor. m/(w)stnb- is uncertain): it cannot be explained from a zero grade 
*tmp- (> Ir. *tap-), cf. LIV, ibid. Explaining the forms as a secondarily arisen 
causative is difficult in the absence of the corresponding regular formation. Perhaps, 
the long vowel has been imported from the semantically and formally similar Ir. 
causative continuations of *yab/f ‘to weave’. 

«PIE (?) *temp- ‘to draw, twist" = LIV: 626 | Pok.: 1064 f. 

*IE COGNATES: Lith. terüpti ‘to stretch; to draw, drag’, Russ. (dial.) tepsti ‘to tighten, 
straiten’, Lat. tempus ‘time (span)’ 

-----
notebook, with an etymological clue: > Arm. vhat ‘disconsolate, discouraged, 
fainthearted, desperate’. = DMMPP: 353b 

*SOGDIAN: CSogd. Oty'q (Ё) ‘comfort’ {hapax} 

*CHORESMIAN: (+ *fra-) т/гӨт- ‘to wake up’, mrO’my- (caus.) ‘to wake" = Samadi: 
173 

© The root *0am appears to be exclusively Iranian. On the other hand, it bears a 
striking formal and semantic similarity to Gr. корёо ‘I take care of, look after’ 
(%їтло-конос (m.) ‘horse-watcher’, Olrish cumal ‘female slave’), which is usually 
connected to xdjvo ‘I am tired’, etc. (*samH) despite the obvious semantic 
difference, cf. Pokorny: 557; (hesitantly) LIV: 324. The initial 0- of the root points 
to contamination with semantically similar roots (e.g. *Ouax$, *OraH) ? 


*PIE— > LIV: – | Pok.: 
*REFERENCES: Schwartz 1970: 292; Sims-Williams, 1985: 131 


*Өапј ‘to pull, draw’ 

*AVESTAN: Y Av. anj- ‘to pull, draw’ || (+ *fra-) ‘to drive to’ = Liste: 26 

Pres. aja-: IND. 3sg. YAv. fradanjaiieiti (Yt 17.2), med. 3р1. YAv. Oanjaüente (Yt 17.12), SUBJ. 15р. 
YAv. Oanjaiieni (Yt 5.50), 3pl. YAv. Oanjaiiante (Yt 19.44) 

*MIDDLE PERSIAN: BMP hnc- /hanj-/ ‘to draw (water)’ (h- is from *haié or the pre- 
figated forms?) || (+ *a-) MMP "hynz- ‘to pull, draw up, tow’, BMP "hnc- ‘to draw 
up (water)’ || (+ *fra-) BMP pl’hnc- /frahanj-/ ‘to educate, instruct, teach’ || (+ *ni-) 
MMP nhynz-, BMP nhh- /nihax-/ (pret. stem) ‘to hold back = DMMPP: 36a, 242b 
Pres.: IND. 1sg. BMP hncm /hanjam/, 3sg. BMP hncyt /hanjéd/; Inf: BMP hyhtn /hixtan/; Partic.: BMP 
hyxt /hixt/ || (+ *а-) Pres.: IND. 3sg. MMP *’hynzyd, 3р1. MMP "hynzynd (MacKenzie 1980: 291), BMP 
/ahanjénd/, SUBJ. 3sg. MMP ’hynz’d, 3pl. MMP ’hynz’nd, IMPV. 2р1. BMP ’hncyt /ahanjéd/; Partic.: 
pres. MMP ’hynz’g, perf. pass. MMP "hxt, BMP ’hht /ähixt/ || (+ *fra-) Partic.: perf. pass. BMP plhhtk(-) 
/frahixtag(-)/ ‘educated, trained’, BMP plhht /frahixt/ || (+ *ni-) Pres.: IND. 3pl. MMP nhynzynd, SUBJ. 
3sg. MMP nhynz’d, IMPV. 2sg. MMP “nyhynj; Pass.: perf. pass. ВМР nh'ht (HWH)nd /nihaxt/, nhht 
/nihaxt/ 

*PARTHIAN: (+ *4-) "hynj- ‘to draw up’ || (+ *pati-) pdhynj- ‘to weigh’ || (+ *fra-) 
frhynj- ‘to instruct, educate’ || (+ *ni-) nhynj- ‘to retain, hold back’, nhng 
‘oppression’ — Ghilain: 51 | DMMPP: 36a, 269b, 155, 242a f. 

(+ *4-) Pres.: IND. 3sg. "hynjyyd, *’hynjyd, 3р1. "hynjynd || (+ *pati-) Pres.: SUBJ. 2sg. pdhynj’h ‘weigh 
[i.e. judge]’ || (+ *fra-) Pres.: SUBJ. 2sg. frhynj’h || (+ *ni-) Pres.: SUBJ. 3sg. nhynj’, IMPV. 2pl. 
“nhynjyd ‘protect!’; Partic.: perf. pass. nhxt|| (+ *ui-) Pres.: IND. 2sg. whynj’h; Partic.: perf. pass. whxt 
*KHOTANESE: OKh. this- (this-) ‘to pull at’, OKh. thamj- (caus.) ‘to pull’ || (+ *apa-) 
OKh. pathis- (pathis-) ‘to refrain’, OKh. pathamj- ‘to restrain’ || (+ *upa-a-) LKh. 
bathamy- ‘to pluck out’ || (+ *us-) OKh. usthamj- ‘to draw, pull out’ || (+ *ni-) OKh. 
nuhamj- ‘to hold back; open’ = SGS: 42, 94, 68, 18, 59 


392 *0jaj (*ti(n)j2) 


*SOGDIAN: BSogd. óync ‘to pull out’ || (+ *pati-) BSogd. pö’ync, MSogd. pddync ‘to 
pull out’ || (+ *pari-) BSogd. prö’y, CSogd. prOync ‘to stretch’ 

Partic.: pres. BSogd. dync’k || (+ *pati-) Pres.: SUBJ. 35р. BSogd. pö’ync’t, Pass.: pres. IND. 35р. 
MSogd. pöö’ytyy Pwt ‘is pulled out’ || (+ *pari-) Impf.: IND. 3pl. CSogd. pry@ynent, Pret.: intr. IND. 3sg. 
BSogd. pró'yt'kw y’y, (£) BSogd. prö’ytch y’y; Partic.: perf. pass. BSogd. prö’yt’kw, BSogd. prö’ytch 
(#); Pass.: pperf. IND. 3sg. intr. BSogd. pró yt'kw х у, BSogd. prö’ytch "y 

*CHORESMIAN: (+ *pati-) ? p@xs- ‘to take refuge in (God)’ © Samadi: 163 f. 
*BACTRIAN: vayyo ‘load’ || (+ *apa-) aBavay- ‘to charge’ ? || (+ *4-) av-avaydo 
‘without deduction’, avayyo ‘neighbourhood’ || (+ *ni-) vavayyo, vavayyivdo 
c» S-W, Bact.: 227b, 174a, 173a, 179b, 208a 

*NWIR: NP sanjidan ‘to measure; reflect; compare, put in balance’, (LW) NP linj- ‘to 
pull’ (< Sogd./Bactr.), Gz. säng-/sängä ‘to rock’, Semn. (impv.) bi-hänj ‘stab !’, 
-tä/-änj- ‘to draw || (+ *a- NP ahixtam/ahiz- ‘to draw (a sword), NP
```


## [2026-10-15T02:47:04.137Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25510,25540p CHEUNG.txt",
 "description": "Continue Cheung *θanj entry"
}
```


### [2026-10-15T02:47:04.637Z] TOOL RESULT

```
-tä/-änj- ‘to draw || (+ *a- NP ahixtam/ahiz- ‘to draw (a sword), NP 
ahanjidan/ahanj- (caus.) ‘to drink; to drag; to fling’, Zaz. antis/anjen- ‘to pull’ || (+ 
*fra-) NP farhang ‘culture, education; dictionary’ || (+ *ni-) NP nihang ‘a kind of 
sea-monster, crocodile; sword’ 

*NEIR: Pash. länga (Ё) ‘lace or rope for tightening the web of a charpoy’ || (+ *abi-) 
Oss. I. ivtynzyn/ivtygd, D. evtinzun/evtigd ‘to yoke a horse; to load a gun; to wind 
up a watch, vel sim.’, I. ivtong, D. evtong ‘equipped, ready for action, under way, 
sim.)’ || (+ *a-) Pash. anang, alang ‘span from thumb to forefinger’ || (+ *ui-) Oss. I. 
tynzyn/tygd, D. itinzun/itigd ‘to spread, stretch out; to crucify’ 

*MISC: (+ *ni-) Arm. (LW) nhang ‘a kind of water beast’ 

9 The initial *0- of the root is puzzling: does it point to the presence of a following 
laryngeal ? The assumption of an older IE *f’-, as found in LIV, l.c. is unacceptable. 
One may also think of influence from the antonym *@ra(n)é ‘to press’. 

«PIE *teng"- ‘to draw, pull back’. > A slightly different preform is reconstructed by 
Kümmel in LIV, Le: zeng. His objections against the postulation of *tH- (on 
account of the Iranian evidence) and his explanation (invoking the loss of an 
s-mobile variant) are incomprehensible to me. *teng^- is clearly an enlarged root of 
*ten- (*tan). => LIV: 657 | Pok.: 1067 

*IE COGNATES: Toch. tänk- ‘to check, stop, restrain’, OCS rastesti ‘distrahere’, 
pri-teZati ‘to acquire, work’, Russ. tuZit’sja ‘to exert oneself’, Russ. tjaZély] ‘heavy’ 
(etc.), Lith. tingéti ‘to be slow, lazy’, tingus ‘slow, lazy’ 

*REFERENCES: KPF I: 206a, 208b; Morgenstierne 1942: 262; Abaev, Slovar’ I: 555; DKS: 148a, 207a f., 
43a, 190b; Abaev, Slovar’ III: 337 £; WIM II/1: 82; Sims-Williams 1989: 329; Paul 1998: 291a; Cheung 
2002: 108 ff., 194 £; NEVP: 44
```


## [2026-10-15T02:47:09.091Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^\\*tan\\b\\|^\\*tanH\\|^\\*tan ‘\\|^\\*tanH ‘\" CHEUNG.txt; grep -n \"tanidan\\|tanïdan\\|tanïdan\" CHEUNG.txt | head",
 "description": "Search Cheung *tan entry"
}
```


### [2026-10-15T02:47:09.604Z] TOOL RESULT

```
24557:*tané 377 
24582:*tan ‘to extend, stretch’ 
24615:*tanó ‘to twist (together), become narrow, dense, constrict’ 
55658:*tané 
16290:‘work’ + tanidan ‘to spin’ or a connection to Skt. kart. NP kartana(k) have similar 
24592:*NWIR: NP tanidan/tan- ‘to turn, spin’, Kurd. (Sor.) tan- ‘to braid, weave’, Gz. 
41587:tanidan/tan-, 377
```


## [2026-10-15T02:47:11.564Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 24582,24614p CHEUNG.txt",
 "description": "Read Cheung *tan entry"
}
```


### [2026-10-15T02:47:12.095Z] TOOL RESULT

```
*tan ‘to extend, stretch’ 


*AVESTAN: (+ *pari-) Y Av. pairi.tan- ‘to extend, stretch’ = Liste: 24 
MED.; Pres. nu-: OPT. 15р. Y Av. pairi.tanuiia (Y 19.7 = Y 71.15) 


*MIDDLE PERSIAN: BMP tn- /tan-/, (pret. stem) tt- /tad-/ ‘to spin (thread)’, BMP tnnd 
/tanand/ ‘spider’ 

*NWIR: NP tanidan/tan- ‘to turn, spin’, Kurd. (Sor.) tan- ‘to braid, weave’, Gz. 
tén-/ténà ‘to spread [intr.]’, tēn-/tēnā ‘to spin’, Khuns. ten-/tenä ‘to string’ 

*NEIR: Oss. I. tonyn/tynd, D. tonun/tund ‘to tear (off); to reap (berries, fruits, corn); 
to scratch; to pull (strongly)’, Sh. tan-/tant, Rosh. tan-/tant, Bart. tan-/tant ‘to stretch, 
tighten, wind’, Yzgh. tant/tan- ‘to spin’ (< Pers. ?), Wa. tem-/tond- ‘to form (from 
dough, clay, dung)’ || (+ *us-) Wa. istind- ‘to yawn’ || (+ *ui-) Yi. wien-/wiet-, M. 
wien-/wiet- ‘to untie, loosen’ 

*SANSKRIT: tan ‘to stretch, to extend’ (RV+) = EWAia I: 618 

«PIE *ten- ‘to draw, stretch’ = LIV: 626 f. | Pok.: 1065 f. 

ТЕ COGNATES: Gr. teivo ‘I draw, pull tight’, OHG den(n)en ‘to stretch’, МНС 


dehnen ‘to stretch’, etc. 

*REFERENCES: Horn 1893: 89; IIFL II: 545b, 262a; Edel’man 1971: 263; MacKenzie, Pahlavi: 81; EVS: 
80b; WIM I: 73; WIM ПЛ!. 84; Abaev, Slovar’ III: 301 ff; Werba 1997: 348; Cabolov 1997: 73; 
Steblin-Kamenskij 1999: 367 f., 457
```


## [2026-10-15T02:47:18.018Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^frahang\\|^ahanj\\|^āhanj\\|^āhang\\|^frahixt\\|^frahixtan\\|^hixtan\\|^tār\\b\\|^tar\\b\\|^tarr\\|^tāftan\\|^tāb\\b\\|^tōrag\\|^tan-\\|^tanīdan\\|^hanj\\|^hixt\" PHD_mackenzie.txt | head -30",
 "description": "Search MacKenzie PHD headwords"
}
```


### [2026-10-15T02:47:18.528Z] TOOL RESULT

```
2904:hixtan, hanJ~ [hyhtn', Imc- I P hxt] draw (water).
4905:tan-bahr [tn1b)hl] physique.
4908:tan-drust [tn'drw(y)st 1 N --] healthy, whole.
4918:tan-tOhmag [tn'twhmk ] (sap) of plants.
4922:tar [LCDr l < A l-~d; tll M tr] over, through, across.
4925:tar [t)ll M t)r] darkness.
4935:tar-manih [tlm)nyh] perversity.
4936:tar-menisn [tlmynfn 1 N tarmani;t] perverse; contemptuoua.
4939:tarr [tl, LCDr (in error, v. tar) IN,.....,] moist, fresh.
8302:tan-                                 tasidan
8690:frahixtan         ,,~V           potk, pildag
8692:frahixtag        \'~cz)          pazzam-                  -~Cl>
12300:hixtan                 \\~         axwasihI                ~-Y'
```


## [2026-10-15T02:47:21.543Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"frahang\\|frahixtan\\|frahanj\\|ahanj\\|a.hang \\|^tan-\\|tan- \\[\\|taftan\\|tāftan\\|tab- \\[\\|tar- \\|tar  \\|tAr \\|tär \\|tōlag\\|tolag\\|torag\\|tōrag\" PHD_mackenzie.txt | head -30",
 "description": "Further PHD searches"
}
```


### [2026-10-15T02:47:22.039Z] TOOL RESULT

```
367:nouns in -dar/-tar [-t'l], and past participles in -dag/-ta~
720:labAxtar ['p'htll M 'b'xtr] planet.
721:labixtar ['p'htll (N baxtar 'west')] north.
869:   i.ldurestar ['twrystl] ashes.
1184:artestar ['Ityft'll N arUMiir!] warrior.
1242:astar ['st'/l M 'st'r] sin.
1285:astar ['Itl] whip.
1317:awestardan, awestar- ['wstl-tn l I P )wystr-, N suturdan] wipe; shave.
1344:axtar ['htll M )xtr, N .......] star, constellation, sign of the zodiac.
1595:boxtar [bwht)ll M bwxt)r] saviour.
1718:   tar [ell] = tarag.
1835:daftar [dptll N ,...,] register, account-book.
1934:dastar [d'ft'l] keeper, preserver.
2028: dosastar [dwlst1] west.
2226:iraxtAr eylht)l] warrior.
2297:frahanJ-, v. frahlxtan.
2301:frahlxtan, frahanJ- [plhhtn', pl'hnc- I P frhynj-, N far--] educate,
2384:frettAr                               34
2385:freftAr [plypt)l] deceiver; deceived.
2577:grtftar [glpt)ll N gir-] held, taken; captive.
2594:guftar [gwpell N .....] speaker.
2660:haftar [hpt)i/ (N kafttir I)] hyena.
2767:hammOxtAr [hmwht'l] learner.
2796:handaxtar [hnd)ht)l] planner.
3101: Juttar [ywdtl I M jwtr] different, otherwise.
3122:kabotar [kpwtll M kbwtr, N --] pigeon.
3257:kastar [kst'l] destroyer, wrongdoer.
3259:kastar [k'st)l] diminisher.
3277: -tar [-tll N -] = keh.
3532:mehtar [mstl, ms)tl « P ms)dr) IN . . . . ] elder, senior.
```


## [2026-10-15T02:47:25.129Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2297,2304p PHD_mackenzie.txt; grep -n \"^frahang\\|frahang \\[\\|^ahang\\|ahang \\[\\|ahixtan\\|ahanJ\\|^tan- \\|^tan \\[\\|^taftan\\|^tab-\\|^tOlag\\|^tOrag\\|^tAr \\|^tar-\\|tAftan\\|tAb-\" PHD_mackenzie.txt | head -20",
 "description": "More PHD lookups"
}
```


### [2026-10-15T02:47:25.516Z] TOOL RESULT

```
frahanJ-, v. frahlxtan.
frahlst [plh(y)st' I (M pr)yst)] most (superlative of freh).
frahlxta~ [plhhtk I N farhixta] educated, trained, skilled.
                      '
frahlxtan, frahanJ- [plhhtn', pl'hnc- I P frhynj-, N far--] educate,
     teach, instruct.
framadar [plm)t)l] commander, ruler, chief.
framan [plm)n l I M frm'n, N farman] order, command; a minor degree
2297:frahanJ-, v. frahlxtan.
2301:frahlxtan, frahanJ- [plhhtn', pl'hnc- I P frhynj-, N far--] educate,
4865:tab-, .....isn, v. taftan.
4866:tAb-, --iln, v. tMtan.
4875: tAbidan [t)pytn l IN .....] = tAftan.
4880: tAftan, tAb- [t)p-tn l I P t)b-, N .....] heat, burn; shine.
4935:tar-manih [tlm)nyh] perversity.
4936:tar-menisn [tlmynfn 1 N tarmani;t] perverse; contemptuoua.
6433:disposition menisn, ragih, xog.           '" out, -- water ahixtan, hixtan.
6481:educate frahixtan, parwardan.                entrust abespurdan, gumardan.
6523:    dusxwadt; ,.... eye as, duJdoysarih;           extract ahixtan; (juice) hunidan.
6890:  instruct frahixtan.                      jet sabag.
7371:  up ahixtan.                                  ray tex.
7759:teach castan, frahixtan, hammoxtan,       thorn xar.
8176:tab-                          -cuP      tars
8187:taftan
8302:tan-                                 tasidan
8690:frahixtan         ,,~V           potk, pildag
11572:ahangar              )~tUY        amar                      ~
12369:                                              ahixtan, haxtan              \\\(.J'VU'
```


## [2026-10-15T02:47:28.598Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ahixtan\\|^Ahixtan\\|ahixtan, \\|ahang\\b\\|Ahang\\|frahang\\|^tan- \\|tan-, \\|tand-\\|^tar \\[t\\|tAr \\[\\|tArag\" PHD_mackenzie.txt | head -15; sed -n 4860,4880p PHD_mackenzie.txt",
 "description": "Find PHD ahixtan, frahang, tan"
}
```


### [2026-10-15T02:47:28.971Z] TOOL RESULT

```
1714:   tandidan, tand- [end-ytn' I (M en-ystn)] tremble, quake.
2385:freftAr [plypt)l] deceiver; deceived.
2767:hammOxtAr [hmwht'l] learner.
3645:nahang, [nsng] province.
4901: tan-, v. tadan .
4925:tar [t)ll M t)r] darkness.
6431:dispense with wiziristan.               draught ahang.
6433:disposition menisn, ragih, xog.           '" out, -- water ahixtan, hixtan.
6481:educate frahixtan, parwardan.                entrust abespurdan, gumardan.
6483:education frahang, parwarisn.                entwine pecidan.
6937:  frahang, sniisagih.                     learn hammoxtan; ....., by heart warm
7362:pro'nince awestam, nahang, paygos,             rain (n.) waran.
7369:pull (n.) ahang.                               rat musk.
7499:ruin(ation) abesihisn(ih), tabahih,        school     dibirestiin,    frahangestiin,
7759:teach castan, frahixtan, hammoxtan,       thorn xar.


                                  T
tA rOD < A cd I (M d», N .....] until; so that.
tab [tp IN .....] fever.
tab-, .....isn, v. taftan.
tAb-, --iln, v. tMtan.
tAbag [t)pk l I N taba] frying-pan.
tabAh [tp)h I N -] ruined, spoilt, destroyed•
   .....ih: ruin, destruction.
tabAhihistan, tabahih- [tp)hyh-stn l I J tb)hh-] be ruined.
tabangog [tpngwk ' I N tabango] box, chest.
tabarzad [tplzt IN .....] manna.
                         '
tabestAn [epst)n' IN -] summer.
 tAbidan [t)pytn l IN .....] = tAftan.
 tadan, tan- [ttn', tn- I N tan-] spin (thread).
 tadar(w) [ttl I (N ta8arw)] pheasant.
 taftan, tab- [tp-tn l ] grow hot; shine.
    -iin: heat, fever.
 tAftan, tAb- [t)p-tn l I P t)b-, N .....] heat, burn; shine.
```


## [2026-10-15T02:47:33.346Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *Ahang\\|^ *ahang \\[\\|^ *Ahixtan\\|^ *ahixtan\\|^ *frahang \\[\\|^ *frahang\\b\" PHD_mackenzie.txt | head; grep -n \"ahang \\[\\|Ahang \\[\\|ahixtan, \\|Ahixtan, \\|frahang \\[\" PHD_mackenzie.txt | head",
 "description": "Find PHD āhang/frahang entries"
}
```


### [2026-10-15T02:47:33.851Z] TOOL RESULT

```
6937:  frahang, sniisagih.                     learn hammoxtan; ....., by heart warm
12369:                                              ahixtan, haxtan              \\\(.J'VU'
6433:disposition menisn, ragih, xog.           '" out, -- water ahixtan, hixtan.
6481:educate frahixtan, parwardan.                entrust abespurdan, gumardan.
7759:teach castan, frahixtan, hammoxtan,       thorn xar.
12369:                                              ahixtan, haxtan              \\\(.J'VU'
```


## [2026-10-15T02:47:36.562Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"hang \\[\\|hixtan, hanJ\\|hixtan, ahanJ\\|hixtan, AhanJ\" PHD_mackenzie.txt | head; grep -n \"hang\\b.*education\\|culture\\|education, learning\" PHD_mackenzie.txt | head -5",
 "description": "PHD hang entries"
}
```


### [2026-10-15T02:47:37.042Z] TOOL RESULT

```
931:               ihang [)hng] pull, draught.
2904:hixtan, hanJ~ [hyhtn', Imc- I P hxt] draw (water).
3765:nihang [nsng] small, few.
1682:Burz [bwlc] the god of agriculture.
2295:frahan~ [pPhng I N farhang] education; knowledge.
5217:lwarz [wlc I M wrz, N harz] work, agriculture.
5921:agriculture warz.                         any, not....., ee.
```


## [2026-10-15T02:47:40.048Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 925,935p PHD_mackenzie.txt; grep -n \"^ *Ahixtan\\|^ *[aA]hixtan\\|hixtan, Ahanj\\|^ *ihixtan\" PHD_mackenzie.txt; grep -n \"hhtn\" PHD_mackenzie.txt|head -5; grep -n \"^ *tar \\|tarr \\[\" PHD_mackenzie.txt|head",
 "description": "More PHD lines"
}
```


### [2026-10-15T02:47:40.559Z] TOOL RESULT

```
               igustan [)kwstn' 1M Hgwst] hang up, suspend. ~'~.l lwc..-
               ihan [)h(y)n', )s(y)n I M uhwn, N ....,] iron.
                                             '
                 ....,en esynyn ] iron, of iron.
                                 '
                  ....,gar [-kll N ....,] blacksmith.
               ihang [)hng] pull, draught.
               ihanJidan [)hncytn ] = ihlxtan.
               ahaniiz [)hnwc I M ')hnwn-c, N hanilz] yet, still.
               ihen = ihan, q.v.
               ihid r>hyt I M C»hyd] stain, impurity; confused.
12369:                                              ahixtan, haxtan              \\\(.J'VU'
938:               ihlxtan, ihanJ- [)hhtn ' , )hnc- I M )hxtn, Chynz-), N tihixtan, -] draw
2301:frahlxtan, frahanJ- [plhhtn', pl'hnc- I P frhynj-, N far--] educate,
1718:   tar [ell] = tarag.
4922:tar [LCDr l < A l-~d; tll M tr] over, through, across.
4925:tar [t)ll M t)r] darkness.
4939:tarr [tl, LCDr (in error, v. tar) IN,.....,] moist, fresh.
```


## [2026-10-15T02:47:44.384Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"thread\\|warp\\|string\" PHD_mackenzie.txt | head; grep -n \"^ *tadan\\|t)l\\]\" PHD_mackenzie.txt | head",
 "description": "Search PHD for thread/string"
}
```


## [2026-10-15T02:47:45.948Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"tār\\b\\|tār \\|tarr\\b\\|frahang\\|āhang\\|āhixtan\\|frahixtan\\|tāftan\\|tōrag\\|tarāzūk\" NYB_vol2_glossary.txt | head -20",
 "description": "Search Nyberg glossary"
}
```


### [2026-10-15T02:47:46.247Z] TOOL RESULT

```
262:aeürénitan [>c*lynytn'] to make ineffec- tive: bé acdrénét (sc. your work) with the explanation akartārēh-ic 6 šmāh dahét he will create ineffectiveness for you, he will make your work inefficacious 45?. — Den. of a-cär, v. car. V.s.v. axtäyisneh.
295:a-griftār ['glpt?]] “not catching", not involving liability or responsibility 65!. — V. griftār and griftärömand.
356:a-kartaréh [’krt’lyh] inactivity: šmāh dahēt gl. to bē acārēnēt (g. v.) 45?. — V. kartār, kartàreh.
497:apākēh [’p’kyh] 1. company; pat ~ together 5712, — 2. backward movement: pat ~ back 418; v. pat-apākēnītan. — 3. help, assistance 5919-20, 729-26 (opp. ha- mēstārēh). — V. lapāk and ?apäk. Paz. āvāgī. V. also apar-apākēh.
511:apar-burtārēh [MDM bwlt'lyh] the act of procuring, or the state of having procured 4425-26, — V, s. v. burtan.
558:apa-zär [’pz’l] 1. adj. mighty: —-góspand whose cattle is powerful 588-13, 6014. — 2. subst. power, predominance 84°; cos- mic, heavenly force 89?7, 922. 1061; mili- tary forces 121157; — ~ u frahang power and teaching powerful teaching 108!%-!!; nök- having new force, renew- ed 1122-12, — < *upa- (or api-, v. apa-) züvar, v. zävar and zor; MPrs ’bz’r, hw?bzr *very mighty'. Often confounded with the late form avzār < apacār (g. v.), hence the erroneous Skr. renderings by Sastra ‘arms’ (Mx, SGV, but 845 sädhana). — FrP, Cod. P, fol. 7^, with the NP gl. qudrat.
651:artēštār ['Ityšt'l] warrior; 4517 ~-éh = 7-6 with -yh for the indef. art. -ē; pl. cas. rect. ~ 28. 6617; pl. cas. obl. —-än 168. 119%, — Borrowed and remodelled (cf below artik) from Av. (1506) radač-štar- ‘he who stands on the chariot’ (ef s. v. rahy); Paz. pl. cas. obl. ar(a)tištārg (Mx).
848:Pywe't'] cikāmcihē Pourusäsp ku yazišn kunät whenever P. intends to perform a sacrifice 5313-14, — Av. (1231) yaoz- ‘to be agitated’; MPrth rzmy(y)wz ‘eager for battle’ (A-H III); Arm. lw. yoiz 'commo- tion, trouble’, but also ‘research, investi- gation’ (den. vb. yuz-em ‘to agitate; to scrutinize’); — ä-yaoz- ‘to agitate, to MPrth ”ywštn, ?ywz- (’y-) (A-H III), ”*ywštg ‘tossing’ (sea), ’ywz ‘violent; disturbance’ (MHC). Borrowed in MPrs in the same sense (Verbum 183) and also in BP: razmik adydzisn ["ywešn'] ‘the act of fighting in battle-array', NSt § 3; äyöz renders Av. yaozante Y. 654. In SW, where Z changed to z, āyēz- coincided with āyēž- and adopted its inf. āyuxtan, ef DkM 695 pres. äyöz-, but 6815 äyux- tārēh in the sense ‘strive for’. The genuine SW form of yaoz-: OP yaud-, v. yöd-; possibly represented by *āhēyēnītan (q.
992:bēšēnītār [~-ynyt’l] causing pain, pain- ful, excruciating: ~ dart 43%.
1046:burtārēh v. apar-burtārēh and framän- burtäreh.
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
1133:5314. — Not -c? as in the Index, cf katār-.
1224:dāštārēh [d*št*lyh] the act of keeping, maintaining ete. 713-4, 9210.20,
1230:dātār [d^t?]] the Creator 5711; epithet of Ohurmazd, passim; creative principle 64°. dātārēh 1. the act of giving 704. — 2. the quality of being the Creator 71°.
1394:duš-hūxt [dwšhwht'] evil speech 63°’. 6510; Evil Speech, the second stage down to Hell 7524, — The negative of hüxt (q. v.). Av. (756 sq.) duž-ūxta-; Paz. dūžūst corresponding to Phl *dusüzt. duš-kām-kartārēh [dwSk’mkrt’lyh] bad exercise of authority, outrage, violence 7211. — Cf kam.
1426:3.8 [the figure l; -’y, -y, -yh] the enel. indef. art.: tigr-é [-1] 339; duxt-ē [BRTH- ^y] 14%; gad-ē [gt'-”y] one stroke with the mace 312°, 4 ēvak-ē [HD-wk!-y] one fourth 998; vāt-ē [-1] 4 hubod 73°; hec ctš-ē [-l] nö 16%; har kas-ē PYS-1] 10018; and cand yašt-ē [-1] 651°; pat har 40 sal hac zan-ē u mart-é frazand-é [al -ē's spelt -1] zāyēt every forthieth year a child is born of a woman and a man (= of one couple) 8622-23; 6 artestäreh for 6 artēštār-ē 4517. — Identical with ?e; MPrs ‘yw placed after its subst.; Paz. -é, NP -é. — The spelling [-1] is sometimes erroneously used for other suffixes -é: mēd4-1 = mode cas. obl. 72??; har marg- arzanik+-1 = -aržānīkē for the abstr. -arzanikéh 10199.
1484:frahang
1506:frahang [plh’ng] education, breeding, training, instruction 226.27, 35.7.16, 6612,
1508:frahang
1511:704, 8823. 10811 (1105 restore frda%). — | a-burt-framānēh, framān-burtār, -r&h. —
```


### [2026-10-15T02:47:46.281Z] TOOL RESULT

```
4404:riital\ [1(y)ltk ' I N ""'0] rope, string, thread.
4411:IIrod [lwtl IN .....] stringed instrument.
4876: tadan, tan- [ttn', tn- I N tan-] spin (thread).
5822:zib [zyh I N zih] bow-string.
6103:bow-string zih.                        buffalo gawmes.
6891: instrument abzar, zay; (stringed) rod.    Jew jahud.
7702:string ristag, wandag.                     superior       abar(ag),    abaragiin(ag),
7767:tend pahrextan.                           thread ristag.
920: ~"".          a-grlftir [)glpt)l] intangible, impalpable.
1009:a-menidir ['mynyt)l] unthinking.
1564:bes- burdar [byfbwlt)l] hostile.
1674:burdar [bwlt)l] bearer; womb.
2226:iraxtAr eylht)l] warrior.
2303:framadar [plm)t)l] commander, ruler, chief.
2385:freftAr [plypt)l] deceiver; deceived.
2417:gAdar [g)t)l] husband.
2796:handaxtar [hnd)ht)l] planner.
3133:kadar [kt)l] who, which.
```


## [2026-10-15T02:47:49.281Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1506,1508p NYB_vol2_glossary.txt | cut -c1-900; grep -n \"^āhang\\|^ähang\\|^āhixtan\\|^ähixtan\\|^ahixtan\\|^tarr\\|^tar \\|^tār\\b\\|^frahixtan\\|^hixtan\\|^ēhang\" NYB_vol2_glossary.txt | head",
 "description": "Read Nyberg frahang and others"
}
```


### [2026-10-15T02:47:49.753Z] TOOL RESULT

```
frahang [plh’ng] education, breeding, training, instruction 226.27, 35.7.16, 6612,
www.parsianjoman.org | ool wok
frahang
1971:hixtan
2009:hixtan [hyhtn'] hanj- [hne-] to draw up: water 1419.?1; the bucket from the well 153.8.19, — V. s. v. Ghanj-. i
3745:tārīk [t*lyk] dark 377°. 762. 859.1339, - M PrthPrs t’ryg, derived from Av. (650) iq0ra- ‘darkness’, MPrthPrs vr; NP tar ‘dark, obscure’; tārīk < *tqOriya-ka-, Av. taūrya- ‘dark’.
3749:tarr [tl] humid, moist 3929.25, 4016, — Probably < *tarna-, cf perhaps Av. (643) tauruna- ‘young’, Skr taruna- ‘young, fresh’; Skr tarna-ka- ‘calf, young animal in general’. NP tar.
3750:tarrök [tlwk'] tender 48?. — From tarr; as to the ending cf s. v. nē(va)kēk.
6978:ähixtan; ähanj-: ähanj-
```


## [2026-10-15T02:47:53.193Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"hanj-\\|θanj\\|Oanj\\|danj\" NYB_vol2_glossary.txt | cut -c1-600 | head",
 "description": "Search Nyberg hanj entries"
}
```


### [2026-10-15T02:47:53.777Z] TOOL RESULT

```
298:ahanj- Phnc-] pres., to draw up (water): imp. pl. ähanjet 14%, — MPrs pt, hat, pres. ?hynz-, Verbum 198; NP aähixtan ahanj-. Alternates in the same context with the simplex vb. hixtan hanj- (q.v.).
1514:frahaxtan [plhhtn'] to educate, to train, pt. = pret. pass. 3d p. sg. frahaxt 2*7. — Pres. frahanj-. MPrth pres. frhynj- ‘to teach’; NP farhaxtan, farhanjidan. From fra + Av. (784sg.) 0ang- ‘to draw’; Verbum 198; Ghilain 51.
1919:hanj- [hnc-] v. hixtan.
1968:haxtan [h’htn'] to pull: api-m ... carm bē haxt and I stripped off his skin 3211-12, — Av. (784sg.) 6ang-. The pres. ähanj- (g. v.) and kanf- (v. hixtan) belong to this root.
2009:hixtan [hyhtn'] hanj- [hne-] to draw up: water 1419.?1; the bucket from the well 153.8.19, — V. s. v. Ghanj-. i
5747:’hxt: āhanj- www.parsianjoman.org | vll
5759:*hynz-: ahanj-
6978:ähixtan; ähanj-: ähanj-
```


## [2026-10-15T02:48:00.467Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; f=BQT_v1_pages.txt; for w in 'آهنگ' 'آهیختن' 'آهنجیدن' 'برهیختن' 'ترانه' 'توله' 'توره' 'تابیدن' 'تافتن'; do echo \"== $w\"; grep -n \"$w\" $f | head -4 | cut -c1-200; done",
 "description": "Grep Borhan vol 1 for headwords"
}
```


### [2026-10-15T02:48:00.953Z] TOOL RESULT

```
== آهنگ
4159:آهنگر » ابرو » اردك » اردو ۰ اره » انگشتری » انگور » باداس >
6625:( بر های قاطع ۷)و مطیخی و آهنگر و امثال آنرایز کوند . *
6921:آش گاه ۵ و کلشن حمام - وکور؛ آهنگری
9222:آهنگه , آهنگیدن » هنجیدن , آهیختن همربثه‌اند . از رسةٌ اوستائی 1308) بمعن ی کشیدن
== آهیختن
9222:آهنگه , آهنگیدن » هنجیدن , آهیختن همربثه‌اند . از رسةٌ اوستائی 1308) بمعن ی کشیدن
9227:۷۳-۲ »- نز آهیختن » سل - جذب کردن ؛ و درآ هنجیدن » در کشیدن چنانکه گوشت را به
9357:؟ ‏ ره : آهیختن . ۴ ساژه‌صدر
17766:ت 4 . «واژه‌نامه >٩۲‏ رك : آهیختن
== آهنجیدن
9171:و آهنجیدن «فاب. ۱ : ۸٩‏ ۶ :
9221:دلت‌نامه ۰ ۴ رك : آهنجیدن. ۵ بهلوی ات2202 « منای ۹٩٩۵‏ * , فذارسی
9272:۶ مناس ۵ ۰ بر : هنگه و آهنجیدن .
18208:[رك: آهنجیدن].
== برهیختن
19227:۵ - رگ : برهیختن .
19273:کوهی آتشفشانی چاه مشهور به‌بثر برهوت واقع‌است «دائر:المماری اسلام». ٩‏ رث: برهیختن.
== ترانه
4457:۴ ود انی یاترانه‌های کردی. دکتر محد مکری. تبران.
29221:ازهمین ربثه است ترانهةٌ فارسی ( جوان خوش روی و دویرتی و سرود ) و تولة نارسی (بمسك)
29224:سرخة #۲) «ثك. ۲س ۰۱۹۳ دزفولی هم 8۲ (خیس ؛ مرطوب). ر که: ترانه. نوره , توله.ی
29263:هر نسفته دری دری می‌سفت هرترانه ترانه‌ای میگفت فرخی سیستانی.
== توله
1828:دساتیر بعنی حقیقت و آمیفی یعنی حقیقی» بوزه بمعنی تولهٌشکاری در ست‌است
3521:با - عر اقی : توله ( ذیل : دزتاج ) » شروانی(ذیل: چارطان» چپار
4568:۰( بارتوله <-) .1950 566255008
7345:ومشی آرد توله اس ت که آش کاچی مانند باشد .
== توره
3228:چرخ ) » بکاول (ذیل : چآشنی گیر)» توره » جاء جنتر» جوجن » جوله» چال»
12232:استنتوره بکسر
24573:حرم را کونند خصوساً و بفربی مضدره و مستوره
24634:رده فشیون - مستوره و خلوت شین
== تابیدن
28033:ه تابان اسم فاعل‌از تابیدن, درخشان» منور. معرب آن‌نیزتابان." «دزیج ۱ص ۱۳*.وجام و شیلةٌ آلوان کنند وگاهی خالی گذارند .
== تافتن
23742:بای لیچیدن - کنایه از سرتافتن-
24123:بی نقطه » بمعت ی گدازش وکاهش بدن و تافتن‌دل
24441:تافتن *اسشق ۲۹۹». ؟ ‏ معرب کلم بودانی 6608.
28083:درخشیدن - وتاب و طافت- آوردن - و تافتن تا تول بروزن شاقول» شخصی‌را گویند
```


## [2026-10-15T02:48:03.903Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; f=BQT_v1_pages.txt; leaf(){ awk -v L=$1 'NR<=L' $f | tr -cd '\\f' | wc -c; }; echo l9222 $(leaf 9222) l29221 $(leaf 29221) l19227 $(leaf 19227); sed -n 9215,9230p $f; echo ----; sed -n 29214,29226p $f",
 "description": "Read Borhan footnotes for āhang and tar"
}
```


### [2026-10-15T02:48:04.291Z] TOOL RESULT

```
l9222 280 l29221 705 l19227 488
سمتانی 5110 ۰ منکری 21180 , سرخ 8987 , لاسگردی 888 , شهمیرزادی 8580
٩۱۸۱-۷۲. 3‏ * .کلکی 2010 م فریزندی ویرنی » ۵180 , نطنزی 2008 , دك .ص۷۸۵»:
ی دا و ار کف رت
خلقانی «لفت نامد».
۴ - درلمات مرکب : آب‌آهنج » جان آهنج . دم‌آهنج , دودآخنج , گوشتآهنج »
معده آهنج بممنی آهنجنده یمنی بر آورنده , ب رکننده » یرون کنندم و پر کشنده است . رف :
دلت‌نامه ۰ ۴ رك : آهنجیدن. ۵ بهلوی ات2202 « منای ۹٩٩۵‏ * , فذارسی
آهنگه , آهنگیدن » هنجیدن , آهیختن همربثه‌اند . از رسةٌ اوستائی 1308) بمعن ی کشیدن
« بارنولمه ۷۸4 > « تب رکه ۷۰ ذیل ۲۵۳2908) >. ۱ - بر آهنجدن نژ بمحنی
بآوردن » جدا کردن : « پیدا شد که صورت معروف کنند؛ هیولی است ازمجهولی او » ومادت
مطلق اندر وهم آینده نیست مگ رکه نفس یاری عقل ازنخست مراورا بمیانجی سورت ثابت کند:
آنگاه مرصورت را بوهم ازاو برآهنجد وعجپولی ثابت کندش بی آن صورت . » « زاد المسافرین
۷۳-۲ »- نز آهیختن » سل - جذب کردن ؛ و درآ هنجیدن » در کشیدن چنانکه گوشت را به
سیخ « لت نامه * .
بقبه از صفحةٌ ٩٩‏
تأنی : تهور و نیزی کرد و پیش آن لشکر بازشد و هرچه محمد. بن هززن آهستکی فرمود تعجبل
----
بقبه از صفْحٌ 1۷۸
ور همه آهنین ترا باشد. شهید بلخی.
«لت فرس ۱4*.
۵ رك : ثراو ندن:
کآب‌چنان ازسفال نوبترابد(ثرابد. دهخدا).
خروانی. «لفت فری۲۲*.
پونانی 166۵0 .استی 48118 (یسر بجه) . فارسی : ثر ء تازه . پپلوی ۰12۲۲ *صسیشال ۱8:»»
ازهمین ربثه است ترانهةٌ فارسی ( جوان خوش روی و دویرتی و سرود ) و تولة نارسی (بمسك)
وتوره (شغال) دیتتا اص ۱۷۱ ب ٩۷۲‏ , گوراای ۲ ( خبی » 9 گورالی ۷۵ ۰ , فر یز ندی
وبرنی ونطنزری 4۲ « دك . ٩ص‏ ۳ ,: سمنانی و سنگری و لاسکردی و شهمیرزادی ۹:۹9
سرخة #۲) «ثك. ۲س ۰۱۹۳ دزفولی هم 8۲ (خیس ؛ مرطوب). ر که: ترانه. نوره , توله.ی
تر اژوی دد - کنابه از آقاب
تراش - بقتح اول بروزن نواش " طمع
```


## [2026-10-15T02:48:13.261Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; f=BQT_v1_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR==704' $f | tail -25; ",
 "description": "Read Borhan leaf 703 tail"
}
```


### [2026-10-15T02:48:13.671Z] TOOL RESULT

```
تخحهگان ‏ بان فارسی بروزن‌استخوان,
بیشهایآدمی را گویند وبعربی خمیتین خوانند
وئخم روبیدنیها را کویند عموماء و تخم خرفه را
گویند خصوصاً .
تخحمه؟ بضم اول وسکون ثانی و فتح
ماشث» مایت که آدمی و حبوانات دبگررا
از چیزی خوردن‌بسباربيم میرسد خصوصا کبوثروا
و آنرا بربی هیضه خوانند - و بمعنی اصل
و نژاد هم‌آمده اه
نو اره بضم‌اول و وأومعدوله بروزن
دچار ؛ نام بادشاه دهستان است کهاز مبارژان
لشکر کیخضرو بوده .
لو » بفتح اول وانی بوا و کشیده » نام
مرغی است صحرایی شبیه بخروس درنهات خوش
روبی وخوش رفتاری۷ .
(۱) چش: سیم.
٩‏ سس رک 0 بشگگ.
بهلوی 0۳021 ۶ آ براهامبان» .
للم بنتح اول و انی » بمعثی تنیده
باشد که ازننبدن مدنقاست۸ .
(۳) چك : بکرخا.
۴ - از: نخم ۰-۳ ( فسبت )»
ومانند تنقل‌خورند .
«بوستی. تام نامه» «فرهنگه شاهنامد» .
۷۲ - رث :نذرو .
```


## [2026-10-15T02:48:20.214Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for r in BQT:1481 BQT:2381; do echo \"######## $r\"; timeout 300 python3 tools/ref_page.py $r --image 2>&1 | head -80; done",
 "description": "Fetch Borhan pages 1481 and 2381",
 "timeout": 600000
}
```


### [2026-10-15T02:48:20.740Z] TOOL RESULT

```
######## BQT:1481
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1481.png
REF: BQT:1481  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 274  OCR-lang: fas

۱4۸۱۳ رهیخشن
فرهنگ ۱ -باکان فارسی » بروزن دیگر بهتر ازآن صورت بگیرد مثلاصورت‌جماد
ومعتی فرهنج است که علم و داش و عقل (۱) رها کند و صورت نبات بگیرد و صورت نبات
و آدب و بزرکی و سنجیدگی ۴ -وکتاب لفات | بگذارد مورت حیوان بگیرد و سورت حیوان
فارسی ۴ - و نام مادر کیکاوس باشد - و شاخ | رهاکند صورت انان قبول نماید» این‌همه‌مراب
درختی را نیز گوبند که‌درزمین خواباننده ازجای نخ است.#
بیگر سریرآورند ۴ - وکاریز آب را نیز گفته‌ان ۱
دیثر سربر آور وریز آب را یز ند ۷ .
چه « دهن فرهنگه » جاییرا میگونند از کاریز فرهودی بروزن‌محمودی کی
2 را گوبند که دردین و هلت و کیش ومذهب خود
که‌آب بر روی زمین آید . ۱
۰ 8 ری ست بماشد .
فرهنگاخ * - با اف فارسی بای ۱ لا ال ۵
کشیده وبخای نقطه‌دار زده» بمعنی میانه ووسط فرهو - با میم‌پروزن‌افروزند»
باشد . مرد نورانی پا کیزه روزگار باشد .
فرهنگ سار ‎٩‏ - با سین بی ضد | فری* - بت اول وکرفای مشدد
بالف کشیده و برای بی نقطةٌ زده » بمعنی سخ | وتالث‌بتختانی رسیده » بمعنی فر وشان و شوکت
است ونخ در لفت بمه‌نی‌زایل کردن‌وباطل‌نمودن | وشکوه وعظمت وافزونی داشتن باشد.
چیزی باشد » و باصطلاح اهل تناسخ عبارت از فرهیختن *۱- بروزن‌انگیختن, بممنر
آنت که چیزی صورتی که دارد رها کندرصورت آدب آموختن و تأدب و ترییت کردن-و آوختن
69 چك » چش :- عقل .
وفرهختن درست مطابق امت درمفهوم با 601021 و 604176 لاتینی بمعنی کششن و کشیدن‌ونیز
بمعنی آموزش و تعلیم و تربیت (که در زبانهای آروپایی 61621108 و 6۵100067 شده)«قاب
۸۷-۹۱ ). در پپلوی 1۳۹8 «تاوادیا ۱۹۶ : ۲ ۴ -رك : فرهنج :
بت فرهنگی اندرین کیتی که نیاموخت از شه آن فرهنگه .
« فرخی سبتانی ۲۱۲ .۰
۴ - ر4 : فرهنج . ۴ - رك : فرهنج » فرهانج , فرنج - - برساختهٌ دساتیر
« فاب 4۷:۱ » « فرهنگه دساتیر ۲۵۹ . ‎٩‏ - برساختهٌ دساتیر ۶« فرهنگه دساتیر۲۵۸*.
۷ - « فرهودی بمعنی ربودی است که مرقوم شد *< جهاتگیری > . مبدل «فربودی»
(«.م.) . بمعنی مذکور درمتن دساتیری است .۸ - « فرهومند, مد نورانی راکوبند وآنرا
فرمند نیز کوبند .> «جهانگیری». رك: فرمند. ‎٩‏ - از 518/۲6 (قی : سربانی
18 هوبشمان ص۸۰۸ > رك:فر » فره » خوره :
فرخ همای دولت وسعد سپهر ملك ایآ تکه‌سایه‌ات بجهان فرهی دهد.
مجد همگر « جهانگیری >
۶ مخفف آن « فرهختن » (و.م.) . رك : فرهنگه » پرهیختن .
0 فرهنگستان - بفتح اول وسوم وکر پنجم » از : فرهنگهستان ( پسوند مکان) ؛
پپلوی ۲۳۵120838138 ( مکتب, مدرسه ) « اونوالا ۹*۷ > ؛ درسالهای اخیراین لفت رامعادل
۸66 (انجمن عالی‌ادبیان ونوسندکان و داشمندان ) بر گزبده‌اند. رك:فاب ص6۵ ۰۹۰-۸

######## BQT:2381
(no exact page map; using offset -1917 -> pdf page 464; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2381.png
REF: BQT:2381  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 464  OCR-lang: fas

-۷۳۸۱- هنگه
باغد ‎٩‏ - و کنایه از تیغ و شمشیر هندی «م ِ وکاف فارسی » چند هعنی دارد : ۱ - سنگینی
هت؟ . 4 وتمکین ووقارباشد۴ . ۲- قسد واراده وآهنگه

هی ؟ - بفتح اول و سکون نالی | طرفی وجائی9 . ۳- غار وشکاف کوه باشد۹ ۰
۱-یزهندی * هندوستانی را بزبان مردم هندوستان که زبانی است مرکب از

ساسکریت و لهجه‌های هندی و فارسی وعربی» اطلاق کنند. ۰

۲ -« وآن (شمغیر) چفارده کونه است : یکی بمانی » دوم هندی ... > * نوروژنامه

س ۳۹ > وهندی شمشیرست که آهن آنرا از هندوستان آورده و یا در هندوستان ساخته

باشند» وآن را هندوانی ومپند وهند کی ( مأٌخون ازهندو4 فأرسی [پهلوی] ) نیز خوانده اند .
«تملیقات نوروزنامه ص۵ ۰.۳۱ ۴ - درپپلوی ۳888 (فم » معرفت) «اوتوالا ۲۳۹ ۰ در
اوراق مانوی بپارنی 13888 [ مر۳ ( بمعنی * بیزاری » تنفر ) (؟ ) ر4 :

.0 ,1 ,176 ,8505 ...صهاومه8 16 3۸:۵4 ‎٩۶‏ اعنا ۸ ,قاط 1162 آقای پورداود
نوشته‌اند: «هنکه درفارسی‌بم‌منی قصد ولیت گرفته شده, آهنکه با پیشاوند «3» درزمان ها رایج تر
است . نازیر هنکه ( * آهنکه ) از پارسی باستان بما رسیده . اگر از زبان آن روز کاران
این‌واژه بجا مانده‌بود بایستی نپنکه 118808 باشد. اینکه حرف « تم > ازپارسی باستان واوستایی
درفارسی به «ه» تبدبل میگردد , نظایر بسیار دارد چون میتهر 1۵1110۳2 ۳ مپر؛ چیتهر6111078

چهر و مانند اینها . دراوستا فعل تهنگه 180888 بمعنی کشیدن بسیار بکار رفته وازین مصدر

(رشه) چندین واژه درفارسی‌یجا مانده؛ ازآنهاست: هنگه ( * آهنکه)» هنجیدن, با پیشاواد7۸»
آهنجیدن وهیأت دیگرآن هختن( ۳ «یختن), با پیشاوند «1» آهختن ( ۳ آهیختن)! با پیشاوند
«فر» فرهختن, باپیشاوند « بر» برهیختن . باپیشاوند «فرو» فروهخشن وجز اینها . ازهمین پنیاه »
آختن با پیشاوند 79 بسیار مع‌ول است». «فاب ۰۴۸۹-۸۵۱ ۴ - ر4: ح۱ و۷ صفحه‌بعد:

ای همه سیرت نو هنگه وثبات چکنم بی ثبات و بی هنگم.
انوری آبیوردی.
8 - «هنکه... آهنگه بجیزی کردن» لفت فری ص۲۸۲ 6 :
دلستانی را لفظ تو همی سازد ساز حان ربایی را تیغ توهمی‌داردهنکه.
: مختاری «فرهنگه فظام».
رك : ح۳ . ‎٩‏ - این معتی را از « هنک افراسپاب » (ه.م.) استنباط کرده‌اند» ورك : دژ

آهنگه افراسیاب .

۵ هنر - بشم اول‌وفتح دوم: اوستا - 12111278 عظمت, استعداد قابلیت, هندی‌باستان

- 900478 ۰ سانکربت 81804878 ( زیبا ؛ قهنگه ) . پهلوی 1388۴ ۰ ارم ع 888۴ ۰
افغانی وبلوچی 83188۲ «اسشق ۱۱*۸ ورك : نیب رک صس*۱۱؛ کردی 1106۳ (فن» معرفت)
«زابا ص4۵۳ ؛ صنمت» معرفت امری توأم با ظرافت و ریزه کاری : ۶ آورده‌اند که ظرافت بسیار
کردن هنرندیمان است وعب‌حکیمان» «کلتان ص۳4 » - هنرهای زیبا » صنایم مستظرفه .

8 هنرمند - بشم اول وفتح دوم وچهارم, از: هنر(ه.م.) ۳ مند (پسوند اتصاف)! پارسی
ماه ۵۵۲۵۷۵۵۵ . رك : ۰۸۲۷ 36۳8۲۳۲۵۵ 218۳6 067 ر و6۲ان8 ۷۷۰)

(.0.271 «1954 ,]67 ,07162111 ؛ آنکه دارای هنراست : «کفت محال است اگر

هنرمندان بمیرند که بیهنران جای ایشان بگیرد .» «کلان ص۲۰ .
```


## [2026-10-15T02:48:25.269Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; f=incoming/BQT/BQT_v4_pages.txt; grep -n \"هنجار\" $f | head -5 | cut -c1-300; grep -n \"گیتار\\|توره\" incoming/BQT/BQT_v*_pages.txt | head -5 | cut -c1-200",
 "description": "Grep Borhan vol 4 for هنجار"
}
```


### [2026-10-15T02:48:25.837Z] TOOL RESULT

```
18667:پوستی باشد که درست از گوسفند بر آورده باشند هنجار۲ * باجیم ابجد پروزن زنگاره
18685:* که اسرموج خون گم کرده هنجار که اسر بخر قم ببریده لنگر .
18687:۹-«هنجاره کسی باشد که راه بگذارد. وبراپر راء همی رود. عنضری (بلخی) کوید :
18688:همی‌شدند به بیچارکی هزیمتیان اشکسته پشت وکرفته کریغ‌راهنجار.
18691:هنجار صفت نیست, بلکه اسم است» پی «کسی باشد...» درست لیست, درشمر عنصری‌هم «هنچار
incoming/BQT/BQT_v5_pages.txt:537:است (رك .کاتوره در کتاب حاض) .
incoming/BQT/BQT_v4_pages.txt:3021:دارویی‌است کهآبرا بهندی داتوره کوبند وبتاتوله مرقون * - بروزن مجنون. دام یکی
incoming/BQT/BQT_v4_pages.txt:3032:۲ - در تداول مغرب داتوره ۳ 421۳0 ( فر ) راگوبند « دزی ج۱ ص ۵4۷ ۰
incoming/BQT/BQT_v4_pages.txt:13829:سوبمعلی آغاز وابتدا هم بنظرآمده است۹ . وخشور #۴ بنتح اول بروزن دستوره
incoming/BQT/BQT_v3_pages.txt:25331:«کاتوره » سر گشته (سر کشتگی . ظ.) بود. رودکی ( سمرقندی ) گوید :
```


## [2026-10-15T02:48:27.626Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; f=incoming/BQT/BQT_v4_pages.txt; sed -n 18665,18700p $f",
 "description": "Read Borhan هنجار entry"
}
```


### [2026-10-15T02:48:27.978Z] TOOL RESULT

```
عريك ونظیرباشد. ودو شخص که بريك قصد و يك عزم وايك آراده
هنپان؟ « بروزنوممنی انبان است‌وآن | باشند وامثال اینها .
پوستی باشد که درست از گوسفند بر آورده باشند هنجار۲ * باجیم ابجد پروزن زنگاره
ودبافت کنند وچیزها درآن نهند وبعربی جراب | پممنی‌راء وروش‌وطریقه - وطرز- وقاعطموقالون-
کوبند - و زببیل درویشان را نیز گفته اند که | ورنگه ولون باشد - و بمعنی جاده وراه راست
سفرة گرد چرمین باشد . هم آمده است : و بستی راء غیر جاده راکوبیند
هنج؟ بفتح‌اولپروزن رنج(۱)بمعتی | لیکن‌محاذی‌ره راست باشد که‌براء روند۹ -وبتنی
کشیدن باشد - وامرباین معنی هم اهست بعنی | از غیرجاده براء رفتن را باین معنی کفته اند که
بکش - و بممنی انداختن هم کفته‌اند - و دو | بجهت بزدیکی‌منزل بربیراهه براه روند تازودتر
چرزرالیز کوبند که بحسب کیفیت يك فدرداشته | بمنزل برسند وبکسر اول هم‌آمده است۷ .
(3ه چش : بروزن ومعنی راج )0
«اباز (ه.م.) * همباز:
بهرچه رای تو روآورد.رتا بدهد بدین‌قد رکه قنا باهش درآن هنباز.
قطران «فرهنگه نطام» .
۴ سابان (.م.). پهلوی 1182028 ۳ 28082 «تاوادیا س۲:۱۹۱ >
۴ - ریعه اوستایی 18288 ( کشیدن ) بارتولمه ۷۸۶ . از همین ريشه است : آهنج
(آهنجیدن) (ه.م.) آهیختن, فرهنگه. رك : هنجیدن. این کلمه درت ر کیب آید :.
کمند عدو هنج از بغر کین فروهشته چون اژدهایی ز زین.
«لبیبی. دبیر سیاقی تهران ۱۳۳۷ ص۳۰ .
۴ - درساسکریت - 58826478 (کشتن » گردیدن, راء ) «اسشق ۰۴۱۱۶۹
* که اسرموج خون گم کرده هنجار که اسر بخر قم ببریده لنگر .
عمعق بخاری « فرهنگه نظام >
۹-«هنجاره کسی باشد که راه بگذارد. وبراپر راء همی رود. عنضری (بلخی) کوید :
همی‌شدند به بیچارکی هزیمتیان اشکسته پشت وکرفته کریغ‌راهنجار.

* لت قری ۰۴۱۸۲
هنجار صفت نیست, بلکه اسم است» پی «کسی باشد...» درست لیست, درشمر عنصری‌هم «هنچار
گرفتن» بممنی را گذاشتن وبرایر راه رفتن امت ومراد آسدی ازین قول آست که راه معموزر۲
بگذارد واز ببراهه که اقسرفاسله است برود . صحاح الذرس (سخة طاعتی) نوید: « هنجار» آن
باش د که کسی‌را بگذارد وبرابر راه رود »کوبند پرهنجار راء میرود» دراینجا پیت مذکور عنصری
را بعنوان «لاادری قائله» آرد وسپس کوید : لامعی گفت:

همراء تست وبارمن» پوینده برهنجارمن خاراشکن رهوارمن,شید یز خال‌وزخش غم(غم).>
رشیدی کوید: ۶ درتحفه گفته راه غیرجاده ». ۷ - جهانگیری این ببت فغر گرا گانی را
شاهد آورده :
```


## [2026-10-15T02:48:33.798Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; f=incoming/BQT/BQT_v4_pages.txt; awk 'NR<=18667' $f | grep -c \"\\[pdf page\"; awk 'NR<=18667' $f | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1",
 "description": "Find pdf page of هنجار entry"
}
```


### [2026-10-15T02:48:34.327Z] TOOL RESULT

```
459
[pdf page 459]
```


## [2026-10-15T02:48:37.852Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-10-15T02:48:38.216Z] TOOL RESULT

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


## [2026-10-15T02:48:45.174Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; N='page 501, root Ten/Tengh/Temp'; for u in \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ten-' \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tengʰ-' \\\n'https://en.wiktionary.org/wiki/فرهنگ' \\\n'https://en.wiktionary.org/wiki/آهنگ' \\\n'https://en.wiktionary.org/wiki/هنجار' \\\n'https://en.wiktionary.org/wiki/آهیختن' \\\n'https://en.wiktionary.org/wiki/تافتن' \\\n'https://en.wiktionary.org/wiki/تابیدن' \\\n'https://en.wiktionary.org/wiki/تار' \\\n'https://en.wiktionary.org/wiki/تر' \\\n'https://en.wiktionary.org/wiki/ترانه' \\\n'https://en.wiktionary.org/wiki/توله' \\\n'https://en.wiktionary.org/wiki/سه‌تار' \\\n'https://en.wiktionary.org/wiki/sitar' \\\n'https://en.wiktionary.org/wiki/κιθάρα' \\\n'https://en.wiktionary.org/wiki/guitar' \\\n'https://en.wiktionary.org/wiki/zither' \\\n'https://en.wiktionary.org/wiki/قيثارة' \\\n'https://en.wiktionary.org/wiki/taffeta' \\\n'https://en.wiktionary.org/wiki/tape' \\\n'https://en.wiktionary.org/wiki/tapestry' \\\n'https://en.wiktionary.org/wiki/τάπης' \\\n'https://www.etymonline.com/word/taffeta' \\\n'https://www.etymonline.com/word/tape' \\\n'https://www.etymonline.com/word/tapestry' \\\n'https://www.etymonline.com/word/guitar' \\\n'https://www.etymonline.com/word/sitar' \\\n'https://www.etymonline.com/word/zither' \\\n'https://www.etymonline.com/word/cittern' \\\n'https://en.wiktionary.org/wiki/tauruna' \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/temp-' \\\n; do python3 tools/fetch_source.py \"$u\" --note \"$N\" 2>&1 | tail -1; done",
 "description": "Archive web sources for page 501",
 "timeout": 600000
}
```


### [2026-10-15T02:49:05.585Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/94de91440ef68db4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/286c085416faf881.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/230584df740153a3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bf7c7d38cc0f1676.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d8a41c5eafe63504.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1dd625ac16e2f4ed.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dddf1b4762e87563.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/24b0a25c595f14af.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/43b9c7a3a1f7d7ee.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/40db141b402e9d09.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/19afbb56211ded08.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/237fe5b4c78ded82.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/223810e93712a689.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4f0007efba68ca07.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9fae7ffb1bbfef4b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fb369480c8d82900.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c1548b4e6860b31f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8e73a48a54fae3b6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/24d86a77ef2eca99.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c61d87204ca77af8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/01b7aae4b0476850.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/44226b5e67f65194.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9252a86b33f58fd3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/48a794f5a827ce8f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/70e63fdb90bcafae.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f57c28f3a4d9149f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2fe9b41983a0c372.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3421457908353205.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/878efc51d4dbb993.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/24eac4cbf50db92c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d653df26e423065c.txt
```


## [2026-10-15T02:49:07.840Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -31 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l);print(d.get('status'),d.get('bytes'),d['file'],d['url'])\"",
 "description": "Check fetch statuses"
}
```


### [2026-10-15T02:49:08.444Z] TOOL RESULT

```
-1 39 data/verification/sources/web/838b5757e76d2d4e.txt https://www.etymonline.com/word/peacock
-1 39 data/verification/sources/web/f57c28f3a4d9149f.txt https://www.etymonline.com/word/guitar
-1 39 data/verification/sources/web/2fe9b41983a0c372.txt https://www.etymonline.com/word/sitar
-1 39 data/verification/sources/web/87c1c0952f7df9da.txt https://www.etymonline.com/word/testimony
200 2386 data/verification/sources/web/64a619d67fcc0a6b.txt https://en.wiktionary.org/wiki/தோகை
200 11857 data/verification/sources/web/536ae7dbba16918a.txt https://en.wiktionary.org/wiki/پدر
200 8507 data/verification/sources/web/b5ef55ccf7df1e25.txt https://abadis.ir/fatofa/مطرح/
-1 39 data/verification/sources/web/3d9681270a6826c9.txt https://en.wiktionary.org/wiki/پاو
200 6234 data/verification/sources/web/2303b39172968337.txt https://en.wiktionary.org/wiki/tertius
200 6468 data/verification/sources/web/286c085416faf881.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tengʰ-
200 8433 data/verification/sources/web/230584df740153a3.txt https://en.wiktionary.org/wiki/فرهنگ
200 4668 data/verification/sources/web/bf7c7d38cc0f1676.txt https://en.wiktionary.org/wiki/آهنگ
200 3460 data/verification/sources/web/d8a41c5eafe63504.txt https://en.wiktionary.org/wiki/هنجار
200 8585 data/verification/sources/web/1dd625ac16e2f4ed.txt https://en.wiktionary.org/wiki/آهیختن
200 4293 data/verification/sources/web/dddf1b4762e87563.txt https://en.wiktionary.org/wiki/تافتن
200 18736 data/verification/sources/web/40db141b402e9d09.txt https://en.wiktionary.org/wiki/تر
200 4280 data/verification/sources/web/19afbb56211ded08.txt https://en.wiktionary.org/wiki/ترانه
200 5381 data/verification/sources/web/237fe5b4c78ded82.txt https://en.wiktionary.org/wiki/توله
200 10209 data/verification/sources/web/c1548b4e6860b31f.txt https://en.wiktionary.org/wiki/zither
200 6203 data/verification/sources/web/8e73a48a54fae3b6.txt https://en.wiktionary.org/wiki/قيثارة
200 7201 data/verification/sources/web/24d86a77ef2eca99.txt https://en.wiktionary.org/wiki/taffeta
200 30159 data/verification/sources/web/c61d87204ca77af8.txt https://en.wiktionary.org/wiki/tape
200 8744 data/verification/sources/web/01b7aae4b0476850.txt https://en.wiktionary.org/wiki/tapestry
200 5074 data/verification/sources/web/44226b5e67f65194.txt https://en.wiktionary.org/wiki/τάπης
-1 39 data/verification/sources/web/9252a86b33f58fd3.txt https://www.etymonline.com/word/taffeta
-1 39 data/verification/sources/web/48a794f5a827ce8f.txt https://www.etymonline.com/word/tape
-1 39 data/verification/sources/web/70e63fdb90bcafae.txt https://www.etymonline.com/word/tapestry
-1 39 data/verification/sources/web/3421457908353205.txt https://www.etymonline.com/word/zither
-1 39 data/verification/sources/web/878efc51d4dbb993.txt https://www.etymonline.com/word/cittern
-1 39 data/verification/sources/web/24eac4cbf50db92c.txt https://en.wiktionary.org/wiki/tauruna
200 6575 data/verification/sources/web/d653df26e423065c.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/temp-
```


## [2026-10-15T02:49:11.883Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for h in 94de91440ef68db4 24b0a25c595f14af 43b9c7a3a1f7d7ee 223810e93712a689 4f0007efba68ca07 9fae7ffb1bbfef4b fb369480c8d82900; do grep \"$h\" index.jsonl | tail -1 | python3 -c \"import sys,json;d=json.loads(sys.stdin.read());print(d['status'],d['bytes'],d['url'])\"; done",
 "description": "Check status of other fetched pages"
}
```


### [2026-10-15T02:49:12.673Z] TOOL RESULT

```
200 9802 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ten-
200 2811 https://en.wiktionary.org/wiki/تابیدن
200 13470 https://en.wiktionary.org/wiki/تار
200 5072 https://en.wiktionary.org/wiki/سه‌تار
200 19012 https://en.wiktionary.org/wiki/sitar
200 7991 https://en.wiktionary.org/wiki/κιθάρα
200 19980 https://en.wiktionary.org/wiki/guitar
```


## [2026-10-15T02:49:15.712Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; ety(){ echo \"######## $1\"; python3 - \"$1\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1]+'.txt').read()\nfor m in re.finditer(r'Etymology',t):\n    print(t[m.start():m.start()+900].replace('\\n',' '));print('--')\nEOF\n}; for h in 230584df740153a3 bf7c7d38cc0f1676 d8a41c5eafe63504 1dd625ac16e2f4ed dddf1b4762e87563 24b0a25c595f14af; do ety $h; done 2>&1 | cut -c1-1200",
 "description": "Print Wiktionary etymologies (Persian)"
}
```


### [2026-10-15T02:49:16.470Z] TOOL RESULT

```
######## 230584df740153a3
Etymology    2.2   Pronunciation    2.3   Noun    2.3.1   Inflection    2.3.2   Derived terms    2.4   Proper noun    2.4.1   Descendants    2.5   References    Toggle the table of contents    فرهنگ    22 languages    Azərbaycanca   Čeština   Deutsch   فارسی   Français   Magyar   Bahasa Indonesia   日本語   한국어   Kurdî   Кыргызча   ລາວ   Lietuvių   Malagasy   Nederlands   Polski   پښتو   Português   Русский   Тоҷикӣ   Türkçe   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   Mazanderani  
--
Etymology  [ edit ]    Deverbal noun of فرهیختن ( farhixtan ) . From Middle Persian plʾhng ( /⁠frahang⁠/ , “ education, knowledge; dictionary ” ) , ultimately from Proto-Iranian *θanǰáyati ; see there for further information. Compare Old Armenian հրահանգ ( hrahang ) , an Iranian loanword.   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /far.ˈhanɡ/    ( Dari, formal ) IPA ( key ) : [fäɾ.háŋɡ]    ( Dari, formal ) IPA ( key ) : [fäɾ.háŋɡ]   ( Kabuli ) IPA ( key ) : [fä.ɾáŋɡ]    ( Hazaragi ) IPA ( key ) : [fä.ɾáŋɡ̥]    ( Iran, formal ) IPA ( key ) : [fæɹ.hǽɲɡʲ̥]    ( Tajik, formal ) IPA ( key ) : [fäɾ.háŋɡ]    Rhymes: -anɡ    Readings   Classical reading ?    farhang   Dari reading ?    farhang   Iranian reading ?    farhang   Tajik reading ?    farhang   Audio ( Iran ) : ( file )    Noun  [ edit ]    فرهنگ • ( farhang ) ( plural فرهنگ‌ها ( farhang-hā / farhang-hâ ) , Tajik 
--
######## bf7c7d38cc0f1676
Etymology 1    2.1.1   Pronunciation    2.1.2   Noun    2.1.2.1   Synonyms    2.1.2.2   Related terms    2.1.2.3   Descendants    2.1.3   References    2.2   Etymology 2    2.2.1   Noun    Toggle the table of contents    آهنگ    11 languages    العربية   Français   Magyar   Kurdî   Lietuvių   Malagasy   Polski   Română   Русский   Тоҷикӣ   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   See also: آهنك and آہنگ    Pashto  [ edit ]    Noun  [ edit ]    آهنگ • ( āháng )  m    melody , mu
--
Etymology 2    2.2.1   Noun    Toggle the table of contents    آهنگ    11 languages    العربية   Français   Magyar   Kurdî   Lietuvių   Malagasy   Polski   Română   Русский   Тоҷикӣ   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   See also: آهنك and آہنگ    Pashto  [ edit ]    Noun  [ edit ]    آهنگ • ( āháng )  m    melody , musical theme , tune    sounding , sound    tone , intonation    Persian  [ edit ]    Persian Wikipedia has an article on: آهنگ    Wikipedia fa    Etymology 1  
--
Etymology 1  [ edit ]    From Middle Persian ʾʾhng ( āhang , “ pull, draught; melody ” ) , derived from آهیختن ( âhixtan , “ to pull, draw out ” ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ʔaː.ˈhanɡ/    ( Dari, formal ) IPA ( key ) : [ʔɑː.ɦäŋɡ]    ( Dari, formal ) IPA ( key ) : [ʔɑː.ɦäŋɡ]   ( Kabuli ) IPA ( key ) : [ʔɑːäŋɡ]    ( Hazaragi ) IPA ( key ) : [ʔɔːäŋɡ̥]    ( Iran, formal ) IPA ( key ) : [ʔɒː.ɦæɲɡʲ̥]    ( Tajik, formal ) IPA ( key ) : [ʔɔ.ɦäŋɡ]    Rhymes: -anɡ    Readings   Classical reading ?    āhang   Dari reading ?    āhang   Iranian reading ?    âhang   Tajik reading ?    ohang   Noun  [ edit ]    Dari   آهنگ    Iranian Persian   Tajik   оҳанг    آهنگ • ( āhang / âhang ) ( plural آهنگ‌ها ( āhang-hā / âhang-hâ ) , Tajik spelling оҳанг )    tune    melody   Synonym: ملودی ( melodi )    harmony   Synonym: هماهنگی ( hamâhangi )    song    medley    ( p
--
Etymology 2  [ edit ]    Deverbal noun of آهیختن ( âhixtan , “ to draw out, to pull ” ) .   Noun  [ edit ]    آهنگ • ( āhang / âhang ) ( plural آهنگ‌ها ( āhang-hā / âhang-hâ ) , Tajik spelling оҳанг )    ( archaic ) intention ; determination    Retrieved from " https://en.wiktionary.org/w/index.php?title=آهنگ&oldid=92368339 "   Categories : Pashto lemmas   Pashto nouns   Pashto masculine nouns   Persian terms derived from Middle Persian   Persian terms inherited from Middle Persian   Persian terms with IPA pronunciation   Rhymes:Persian/anɡ   Rhymes:Persian/anɡ/2 syllables   Persian lemmas   Persian nouns   fa:Poetry   Persian terms with archaic senses    Hidden categories: Pages with entries   Pages with 2 entries   Persian entries referencing missing etymons   Pages with etymon   Persian entries with etymon   Pages using etymon with no ID    This page was last edited on 28 August 2026,
--
######## d8a41c5eafe63504
Etymology    1.2   Pronunciation    1.3   Noun    1.3.1   Derived terms    1.3.2   References    Toggle the table of contents    هنجار    4 languages    فارسی   Kurdî   Malagasy   Русский    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   Persian  [ edit ]    Etymology  [ edit ]    Inherited from Middle Persian 𐭤𐭭𐭰𐭠𐭥 ( hanjār ) , from Parthian ʾnjʾr ( anjār , “ behaviour ” ) . Akin to Old Armenian հանճար ( hančar ) , an Iranian borrowing.   Pronunciation  [ edit ]    ( Classical Persian ) I
--
Etymology  [ edit ]    Inherited from Middle Persian 𐭤𐭭𐭰𐭠𐭥 ( hanjār ) , from Parthian ʾnjʾr ( anjār , “ behaviour ” ) . Akin to Old Armenian հանճար ( hančar ) , an Iranian borrowing.   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /han.ˈd͡ʒaːr/    ( Dari, formal ) IPA ( key ) : [hän.d͡ʒɑːɾ]    ( Dari, formal ) IPA ( key ) : [hän.d͡ʒɑːɾ]   ( Kabuli ) IPA ( key ) : [ʔän.d͡ʒɑːɾ]    ( Hazaragi ) IPA ( key ) : [ʔän.d͡ʒɔːɾ]    ( Iran, formal ) IPA ( key ) : [hæn.d͡ʒɒːɹ]    ( Tajik, formal ) IPA ( key ) : [hän.d͡ʒɔɾ]    Rhymes: -aːr    Readings   Classical reading ?    hanjār   Dari reading ?    hanjār   Iranian reading ?    hanjâr   Tajik reading ?    hanjor   Noun  [ edit ]    هنجار • ( hanjār / hanjâr ) ( plural هنجارها ( hanjār-hā / hanjâr-hâ ) , Tajik spelling ҳанҷор )    norm , convention   هنجارها ی اجتماعی ― hanjār-hā -ye ejtemâ'i ― social norms    way , rule , law    h
--
######## 1dd625ac16e2f4ed
Etymology    1.3   Pronunciation    1.4   Verb    1.4.1   Conjugation    1.4.2   Derived terms    1.5   References    Toggle the table of contents    آهیختن    2 languages    فارسی   Malagasy    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   Persian  [ edit ]    Alternative forms  [ edit ]    آختن ( âxtan ) ( literary , poetic )    آهختن ( âhextan ) , آهنجیدن ( âhanjidan ) , آهنگیدن ( âhangidan ) , هنجیدن ( hanjidan ) , هیختن ( hixtan ) , هختن ( hoxtan )    Etymology  [ edit ]    From Midd
--
Etymology  [ edit ]    From Middle Persian ʾhhtn', 'hnj- ( āhixtan, āhanj- , “ to draw out , pull up , extract ” ) , from Proto-Iranian *ā- ( “ ad ” ) + *θanǰáyati ( “ to pull, draw ” ) . [ 1 ] The prefix is from Proto-Indo-European *h₂éd ( “ near, at ” ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ʔaː.heːx.ˈtan/    ( Dari, formal ) IPA ( key ) : [ʔɑː.ɦeːx.t̪ʰán]    ( Dari, formal ) IPA ( key ) : [ʔɑː.ɦeːx.t̪ʰán]   ( Kabuli ) IPA ( key ) : [ʔɑː.jeːx.t̪ʰán]    ( Hazaragi ) IPA ( key ) : [ʔɔː.jeːx.t̪ʰán]    ( Iran, formal ) IPA ( key ) : [ʔɒː.ɦiːx.t̪ʰǽn]    ( Tajik, formal ) IPA ( key ) : [ʔɔ.ɦeχ.t̪ʰán]    Rhymes: -an    Readings   Classical reading ?    āhēxtan   Dari reading ?    āhēxtan   Iranian reading ?    âhixtan   Tajik reading ?    ohextan   Verb  [ edit ]    آهیختن • ( āhēxtan  / âhixtan ) ( present stem آهنج ( âhanj ) , Tajik spelling оҳехтан )    to pull
--
######## dddf1b4762e87563
Etymology 1    1.2.1   Pronunciation    1.2.2   Verb    1.2.2.1   Related terms    1.2.3   References    1.3   Etymology 2    1.3.1   Verb    1.4   Further reading    Toggle the table of contents    تافتن    3 languages    فارسی   Кыргызча   Malagasy    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   See also: بافتن    Persian  [ edit ]    Alternative forms  [ edit ]    تاویدن ( tāvidan )    تابیدن ( tābidan )    Etymology 1  [ edit ]    From Proto-Iranian *tāp- ( “ to twist, wind ” ) , per
--
Etymology 2    1.3.1   Verb    1.4   Further reading    Toggle the table of contents    تافتن    3 languages    فارسی   Кыргызча   Malagasy    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   See also: بافتن    Persian  [ edit ]    Alternative forms  [ edit ]    تاویدن ( tāvidan )    تابیدن ( tābidan )    Etymology 1  [ edit ]    From Proto-Iranian *tāp- ( “ to twist, wind ” ) , perhaps from Proto-Indo-European *temp- ( “ to span, stretch, extend ” ) . [ 1 ]    Pronunciation  [ edit ]    ( C
--
Etymology 1  [ edit ]    From Proto-Iranian *tāp- ( “ to twist, wind ” ) , perhaps from Proto-Indo-European *temp- ( “ to span, stretch, extend ” ) . [ 1 ]    Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /taːf.ˈtan/    ( Dari, formal ) IPA ( key ) : [t̪ʰɑːf.t̪ʰán]    ( Dari, formal ) IPA ( key ) : [t̪ʰɑːf.t̪ʰán]   ( Kabuli ) IPA ( key ) : [t̪ʰɑːf.t̪ʰán]    ( Hazaragi ) IPA ( key ) : [t̪ʰɔːf.t̪ʰán]    ( Iran, formal ) IPA ( key ) : [t̪ʰɒːf.t̪ʰǽn]    ( Tajik, formal ) IPA ( key ) : [t̪ʰɔf.t̪ʰán]    Rhymes: -an    Readings   Classical reading ?    tāftan   Dari reading ?    tāftan   Iranian reading ?    tâftan   Tajik reading ?    toftan   Verb  [ edit ]    تافتن • ( tâftan ) ( present stem تاب ( tâb ) )    to twist    to twine    Related terms  [ edit ]    تابیدن ( tâbidan )    References  [ edit ]    ^ Cheung, Johnny ( 2007 ), Etymological Dictionary of the Iranian Verb 
--
Etymology 2  [ edit ]    From Proto-Indo-European *tep- ( “ to be warm, tepid ” ) .   Verb  [ edit ]    تافتن • ( tâftan ) ( present stem تاب ( tâb ) )    to heat    to shine    Further reading  [ edit ]    Vullers, Johann August ( 1855 ), “ تافتن ”, in Lexicon Persico-Latinum etymologicum cum linguis maxime cognatis Sanscrita et Zendica et Pehlevica comparatum, e lexicis persice scriptis Borhâni Qâtiu, Haft Qulzum et Bahâri agam et persico-turcico Farhangi-Shuûrî confectum, adhibitis etiam Castelli, Meninski, Richardson et aliorum operibus et auctoritate scriptorum Persicorum adauctum ‎ [1] (in Latin), volume I, Gießen: J. Ricker, page 414    Vullers, Johann August ( 1867 ), “ تافتن ”, in Supplementum lexici Persico-Latini continens verborum linguae persicae radices e dialectis antiquioribus Persicis et lingua Sanscrita et aliis linguis maxime cognatis erutas atque illustratas ‎ [2] (in
--
######## 24b0a25c595f14af
```


## [2026-10-15T02:49:22.357Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; ety(){ echo \"######## $1\"; python3 - \"$1\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1]+'.txt').read()\nms=[m.start() for m in re.finditer(r'Etymology( \\d)?\\s+\\[ edit \\]',t)]\nfor s in ms: print(t[s:s+700].replace('\\n',' '));print('--')\nEOF\n}; for h in 43b9c7a3a1f7d7ee 40db141b402e9d09 19afbb56211ded08 237fe5b4c78ded82 223810e93712a689 4f0007efba68ca07 9fae7ffb1bbfef4b; do ety $h; done 2>&1 | cut -c1-800",
 "description": "Print more Wiktionary etymologies"
}
```


### [2026-10-15T02:49:23.191Z] TOOL RESULT

```
######## 43b9c7a3a1f7d7ee
Etymology  [ edit ]    Borrowed from Classical Persian تَار ( tār ) , from Proto-Iranian *tánθram , from Proto-Indo-Iranian *tántram , ultimately from Proto-Indo-European *ten- ( “ to stretch ” ) .   Pronunciation  [ edit ]    IPA ( key ) : [taːr]    Noun  [ edit ]    تار • ( tār )  f    string ; cord    ( music ) cord , wire ( of an instrument )    Khalaj  [ edit ]    Adjective  [ edit ]    تار ( târ )    Arabic spelling of târ ( “ narrow , tight ” )    Persian  [ edit ]    Persian Wikipedia has an article on: تار    Wikipedia fa    Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ˈtaːr/    ( Dari, formal ) IPA ( key ) : [t̪ʰɑːɾ]    ( Dari, formal ) IPA ( key ) : [t̪ʰɑːɾ]   (
--
Etymology 1  [ edit ]    Etymology tree   Proto-Indo-European *temH-    Proto-Indo-European *-os    Proto-Indo-European *témHos    Proto-Indo-European *-rós    Proto-Indo-Iranian *támHsram   Persian تار    From Middle Persian 𐭲𐭠𐭥 ( tʾr /⁠tār⁠/ , “ darkness ” ) , from Proto-Iranian *támHsram , from Proto-Indo-Iranian *támHsram , from Proto-Indo-European *temH- .   Cognate to Avestan 𐬙𐬄𐬚𐬭𐬀 ( tąθra ) , Pashto تور ( tor , “ black ” ) , Sanskrit तमिस्र ( tamisra ) , Latin tenebrae .   Adjective  [ edit ]    تار • ( târ )    dark ; obscure ; dim   هوای تار ― havâ-ye târ ― dark sky; dark weather    bleary ; dim    faint ; unclear    Related terms  [ edit ]    تاریک ( târik )    Etymology 2  [ edit 
--
Etymology 2  [ edit ]    From Proto-Iranian *tánθram , from Proto-Indo-Iranian *tántram , ultimately from Proto-Indo-European *ten- ( “ to stretch ” ) , Northern Luri تال ( tal ) ; see there for further information. Cognate to Sanskrit तन्त्र ( tantra ) .   Noun  [ edit ]    تار • ( târ ) ( plural تارها )    string ; cord   Synonym: رشته ( rešte )    warp   Coordinate term: پود ( pud )    tar (a classical musical instrument of Persia )   Derived terms  [ edit ]    تار عنکبوت ( târ-e ankabut , “ spiderweb ” )   تار و پود ( târ o pud , “ warp and weft; basic structure ” )    Descendants  [ edit ]    → Armenian: թառ ( tʻaṙ )    → Assamese: তাৰ ( tar )    → Bengali: তার ( tar )    → English: tar
--
Etymology  [ edit ]    Borrowed from Classical Persian تار ( tār ) .   Pronunciation  [ edit ]    ( Standard Punjabi ) IPA ( key ) : /t̪äːɾ/ , [t̪äːɾ(ə̆)]    Noun  [ edit ]    تار • ( tār )  f ( Gurmukhi spelling ਤਾਰ )    wire , cable , line , string    string of a musical instrument   References  [ edit ]    Iqbal, Salah ud-Din ( 2002 ), “ تار ”, in vaḍḍī panjābī lughat (in Punjabi), Lahore: عزیز پبلشرز [ ʻazīz pabliśarz ], page 712    “ تار ”, in Punjabi-English Dictionary , Patiala: Punjabi University , 2026    Sindhi  [ edit ]    Etymology  [ edit ]    Borrowed from Classical Persian تار ( tār ) .   Pronunciation  [ edit ]    This entry needs pronunciation information. If you are familia
--
Etymology  [ edit ]    Borrowed from Classical Persian تار ( tār ) .   Pronunciation  [ edit ]    This entry needs pronunciation information. If you are familiar with the IPA then please add some!   Noun  [ edit ]    تارَ • ( tāra )  f ( Devanagari तार )    wire , chord , string , thread    string of a musical instrument   References  [ edit ]    Khānu, Balocu (1960– 1988 ), “ تارَ ”, in Jāmiʻ Sindhī lughāta (in Sindhi), Hyderabad, Sindh: Sindhī Adabī Borḍ, page 430    Parmanand, Mewaram ( 1910 ), “ تارَ ”, in Sindhi-English Dictionary , Hyderabad, Sindh: The Sind Juvenile Co-operative Society, page 85    Stack, George ( 1849 ), “ तार ”, in A dictionary, English and Sindhi , American Mission
--
Etymology  [ edit ]    Inherited from Arabic ثَارَ ( ṯāra ) .   Pronunciation  [ edit ]    IPA ( key ) : /taːr/ , [tɑːrˤ]    Audio ( al-Lidd ) : ( file )    Verb  [ edit ]    تار • ( tār ) I ( present بتور ( bitūr ) )    to rebel , to revolt    Conjugation  [ edit ]    Conjugation of تار    singular   plural   1 st person   2 nd person   3 rd person   1 st person   2 nd person   3 rd person   past   m    ترت ( turt )    ترت ( turt )    تار ( tār )    ترنا ( turna )    ترتو ( turtu )    تارو ( tāru )    f    ترتي ( turti )    تارت ( tārat )    present   m    بتور ( batūr )    بتتور ( bittūr )    بتور ( bitūr )    منتور ( mintūr )    بتتورو ( bittūru )    بيتورو ( bitūru )    f    بتتوري ( bit
--
Etymology  [ edit ]    Borrowed from Classical Persian تَار ( tār ) . First attested in c. 1657 as Middle Hindi تار ( tar /⁠tār⁠/ ) . [ 1 ]    Pronunciation  [ edit ]    ( Standard Urdu ) IPA ( key ) : /t̪ɑːɾ/    Rhymes: -ɑːɾ    Noun  [ edit ]    تار • ( tār )  m    cord , wire    ( technology ) cable    ( dated sense ) telegraph    string , thread    ( music ) cord , wire ( of an instrument )    Declension  [ edit ]    Declension of تار    singular   plural   direct   تار ( tār )    تار ( tār )    oblique   تار ( tār )    تاروں ( tārõ )    vocative   تار ( tār )    تارو ( tāro )    References  [ edit ]    ^ “ تار ”, in اُردُو لُغَت ( urdū luġat ) (in Urdu), Ministry of Education: Government
--
Etymology 1  [ edit ]    From Proto-Turkic *tār . [ 1 ] Cognates with Turkish dar .   Adjective  [ edit ]    تار • ( tar )    narrow , cramped    tight , taut    Etymology 2  [ edit ]    From Persian تار ( târ )    Noun  [ edit ]    تار • ( tar ) ( plural تارلار ( tarlar ) )    string , cord    References  [ edit ]    ^ Clauson, Gerard ( 1972 ), “ ta:r ”, in An Etymological Dictionary of pre-thirteenth-century Turkish , Oxford: Clarendon Press, →ISBN , →OCLC , page 528    Further reading  [ edit ]    Schwarz, Henry G. ( 1992 ), An Uyghur-English Dictionary (East Asian Research Aids & Translations; 3), Bellingham, Washington: Center for East Asian Studies, Western Washington University, →ISBN
--
Etymology 2  [ edit ]    From Persian تار ( târ )    Noun  [ edit ]    تار • ( tar ) ( plural تارلار ( tarlar ) )    string , cord    References  [ edit ]    ^ Clauson, Gerard ( 1972 ), “ ta:r ”, in An Etymological Dictionary of pre-thirteenth-century Turkish , Oxford: Clarendon Press, →ISBN , →OCLC , page 528    Further reading  [ edit ]    Schwarz, Henry G. ( 1992 ), An Uyghur-English Dictionary (East Asian Research Aids & Translations; 3), Bellingham, Washington: Center for East Asian Studies, Western Washington University, →ISBN , page 156    Retrieved from " https://en.wiktionary.org/w/index.php?title=تار&oldid=92283670 "   Categories : Kashmiri terms borrowed from Classical Persian   K
--
######## 40db141b402e9d09
Etymology 3  [ edit ]    Verb  [ edit ]    تِرْ • ( tir ) ( form I ) /tir/    second-person masculine singular imperative of وَتَرَ ( watara )    Etymology 4  [ edit ]    Verb  [ edit ]    تَرِ • ( tari ) ( form I ) /ta.ri/    inflection of وَرَى ( warā ) :   second-person masculine singular non-past active jussive    third-person feminine singular non-past active jussive    References  [ edit ]    “ twr 4 ”, in The Comprehensive Aramaic Lexicon Project , Cincinnati: Hebrew Union College, 1986–    Dozy, Reinhart Pieter Anne ( 1881 ), “ تر ”, in Supplément aux dictionnaires arabes ‎ [1] (in French), volume 1, Leiden: E. J. Brill, page 142    Fraenkel, Siegmund ( 1886 ), Die aramäischen Fremdw
--
Etymology 4  [ edit ]    Verb  [ edit ]    تَرِ • ( tari ) ( form I ) /ta.ri/    inflection of وَرَى ( warā ) :   second-person masculine singular non-past active jussive    third-person feminine singular non-past active jussive    References  [ edit ]    “ twr 4 ”, in The Comprehensive Aramaic Lexicon Project , Cincinnati: Hebrew Union College, 1986–    Dozy, Reinhart Pieter Anne ( 1881 ), “ تر ”, in Supplément aux dictionnaires arabes ‎ [1] (in French), volume 1, Leiden: E. J. Brill, page 142    Fraenkel, Siegmund ( 1886 ), Die aramäischen Fremdwörter im Arabischen (in German), Leiden: E. J. Brill, page 255    Freytag, Georg ( 1830 ), “ تر ”, in Lexicon arabico-latinum praesertim ex Djeuha
--
Etymology  [ edit ]    From Proto-Iranian *-tarah , from Proto-Indo-European *-teros .   Pronunciation  [ edit ]    IPA ( key ) : /tɪɾ/    Suffix  [ edit ]    -تِر ( -tir )    A suffix forming the comparative degree of an adjective.   See also  [ edit ]    -تِرین ( -tirîn )    Gawar-Bati  [ edit ]    Etymology 1  [ edit ]    Borrowed from Sanskrit तॄ ( tṝ ) .   Noun  [ edit ]    تر ( tar )    a place for swimming    Etymology 2  [ edit ]    Borrowed from Pashto تر , from Persian تر .   Noun  [ edit ]    تر ( tar )    a shrub whose leaves are put into rice seedling fields    Khalaj  [ edit ]    Noun  [ edit ]    تَر ( tər ) ( definite accusative تَری , plural تَرلَر )    Arabic spelling of tə
--
Etymology 1  [ edit ]    Borrowed from Sanskrit तॄ ( tṝ ) .   Noun  [ edit ]    تر ( tar )    a place for swimming    Etymology 2  [ edit ]    Borrowed from Pashto تر , from Persian تر .   Noun  [ edit ]    تر ( tar )    a shrub whose leaves are put into rice seedling fields    Khalaj  [ edit ]    Noun  [ edit ]    تَر ( tər ) ( definite accusative تَری , plural تَرلَر )    Arabic spelling of tər ( “ sweat ” )    Declension  [ edit ]    Declension of تر    singular   plural   nominative   تر    ترلر    genitive   ترۆݧ    ترلریݧ    dative   ترکه    ترلرکه    definite accusative   ترۆ    ترلری    locative   ترچه    ترلرچه    ablative   ترده    ترلرده    instrumental   ترله    ترلرله    equativ
--
Etymology 2  [ edit ]    Borrowed from Pashto تر , from Persian تر .   Noun  [ edit ]    تر ( tar )    a shrub whose leaves are put into rice seedling fields    Khalaj  [ edit ]    Noun  [ edit ]    تَر ( tər ) ( definite accusative تَری , plural تَرلَر )    Arabic spelling of tər ( “ sweat ” )    Declension  [ edit ]    Declension of تر    singular   plural   nominative   تر    ترلر    genitive   ترۆݧ    ترلریݧ    dative   ترکه    ترلرکه    definite accusative   ترۆ    ترلری    locative   ترچه    ترلرچه    ablative   ترده    ترلرده    instrumental   ترله    ترلرله    equative   ترواره    ترلرواره    Kipchak  [ edit ]    Etymology  [ edit ]    From Proto-Turkic *tẹr ( “ sweat ” ) .   Noun  [
--
Etymology  [ edit ]    From Proto-Turkic *tẹr ( “ sweat ” ) .   Noun  [ edit ]    تر ( ter )    sweat    Descendants  [ edit ]    North Kipchak  Bashkir: тир ( ter )    Tatar: тир ( tir )    West Kipchak  Crimean Tatar: ter    Karachay-Balkar: тер ( ter )    Karaim: тэр    Kumyk: тер ( ter )    Central Kipchak  Karakalpak: тер    Kazakh: тер ( ter )    Nogai: тер ( ter )    East Kipchak  Kyrgyz: тер ( ter )    Southern Altai: тер ( ter )    References  [ edit ]    Houtsma, Martin Theodor ( 1894 ), Ein türkisch-arabisches Glossar, nach der Leidener Handschrift herausgegeben und erläutert ‎ [7] , Leiden: E. J. Brill, page 66    Houtsma, Martin Theodor ( 1894 ), Ein türkisch-arabisches Glossar,
--
Etymology 1  [ edit ]    Inherited from Proto-Turkic *tẹr ( “ sweat ” ) .   Pronunciation  [ edit ]    IPA ( key ) : [tɛɾ]    Noun  [ edit ]    تر • ( ter )    sweat ( also figurative )    Related terms  [ edit ]    ترلمك , ترله‌مك ( terlemek , “ to sweat ” )    ترلتمك ( terletmek , “ to make sweat ” )    ترلی ( terli , “ having sweated ” )    ترلك ( terlik , “ slipper; sweatshirt; sweath-cloth ” )    Descendants  [ edit ]    Turkish: ter    Etymology 2  [ edit ]    Onomatopoeic    Pronunciation  [ edit ]    IPA ( key ) : [tɯɾ]    Interjection  [ edit ]    تر • ( tır )    used to imitate a tremble or vibrating sound , falling nails or the like, also a cat’s purr    Alternative forms  [ edit 
--
Etymology 2  [ edit ]    Onomatopoeic    Pronunciation  [ edit ]    IPA ( key ) : [tɯɾ]    Interjection  [ edit ]    تر • ( tır )    used to imitate a tremble or vibrating sound , falling nails or the like, also a cat’s purr    Alternative forms  [ edit ]    تیر ( tır ) , طر ( tır, dır )    Related terms  [ edit ]    طرطر ( dırdır , “ grumble, buzz ” )    طرطرلی ( dırdırlı , “ engrailed ” )    Etymology 3  [ edit ]    Borrowed from Persian تر ( tar ) .   Pronunciation  [ edit ]    IPA ( key ) : [tɛɾ]    Noun  [ edit ]    تر • ( ter )    humid , wet , moist , damp   Synonym: یاش ( yaş )    fresh , not flaccid , juicy   Synonym: تازه ( taze )   تر و تازه ― ter ve taze, terütaze ― fresh and jui
--
Etymology 3  [ edit ]    Borrowed from Persian تر ( tar ) .   Pronunciation  [ edit ]    IPA ( key ) : [tɛɾ]    Noun  [ edit ]    تر • ( ter )    humid , wet , moist , damp   Synonym: یاش ( yaş )    fresh , not flaccid , juicy   Synonym: تازه ( taze )   تر و تازه ― ter ve taze, terütaze ― fresh and juicy    Descendants  [ edit ]    Turkish: ter    Etymology 4  [ edit ]    Borrowed from Persian ـتر ( -tar ) .   Adverb  [ edit ]    تر • ( ter )    more than the others, excessively , much , quite ( also in compounds, and written together or not )    Persian  [ edit ]    Etymology  [ edit ]    From Middle Persian [script needed] ( tl’, LCDr /⁠tarr⁠/ , “ wet, moist ” ) , Northern Luri تٸڕ ( təərr
--
Etymology 4  [ edit ]    Borrowed from Persian ـتر ( -tar ) .   Adverb  [ edit ]    تر • ( ter )    more than the others, excessively , much , quite ( also in compounds, and written together or not )    Persian  [ edit ]    Etymology  [ edit ]    From Middle Persian [script needed] ( tl’, LCDr /⁠tarr⁠/ , “ wet, moist ” ) , Northern Luri تٸڕ ( təərr ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ˈtar/    ( Dari, formal ) IPA ( key ) : [t̪ʰäɾ]    ( Dari, formal ) IPA ( key ) : [t̪ʰäɾ]   ( Kabuli ) IPA ( key ) : [t̪ʰäɾ]    ( Hazaragi ) IPA ( key ) : [t̪ʰäɾ]    ( Iran, formal ) IPA ( key ) : [t̪ʰæɹ]    ( Tajik, formal ) IPA ( key ) : [t̪ʰäɾ]    Rhymes: -ar    Readings   Cl
--
Etymology  [ edit ]    From Middle Persian [script needed] ( tl’, LCDr /⁠tarr⁠/ , “ wet, moist ” ) , Northern Luri تٸڕ ( təərr ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ˈtar/    ( Dari, formal ) IPA ( key ) : [t̪ʰäɾ]    ( Dari, formal ) IPA ( key ) : [t̪ʰäɾ]   ( Kabuli ) IPA ( key ) : [t̪ʰäɾ]    ( Hazaragi ) IPA ( key ) : [t̪ʰäɾ]    ( Iran, formal ) IPA ( key ) : [t̪ʰæɹ]    ( Tajik, formal ) IPA ( key ) : [t̪ʰäɾ]    Rhymes: -ar    Readings   Classical reading ?    tar   Dari reading ?    tar   Iranian reading ?    tar   Tajik reading ?    tar   Adjective  [ edit ]    تر • ( tar )    moist , wet    Related terms  [ edit ]    تره ( tare )    Retrieved from " https:/
--
######## 19afbb56211ded08
Etymology  [ edit ]    Probably from Proto-Indo-European *terh₂- ( “ to pass through ” ) , as songs pass through air. Compare Northern Kurdish terrane ( “ joke, fun ” ) , following a different route of sense development.   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ta.raː.ˈna/    ( Dari, formal ) IPA ( key ) : [t̪ʰä.ɾɑː.ná]    ( Dari, formal ) IPA ( key ) : [t̪ʰä.ɾɑː.ná]   ( Kabuli ) IPA ( key ) : [t̪ʰä.ɾɑː.ná]    ( Hazaragi ) IPA ( key ) : [t̪ʰä.ɾɔː.ná]    ( Iran, formal ) IPA ( key ) : [t̪ʰæ.ɹɒː.né]    ( Tajik, formal ) IPA ( key ) : [t̪ʰä.ɾɔ.ná]    Rhymes: -a    Readings   Classical reading ?    tarāna   Dari reading ?    tarāna   Iranian reading ?    tarâne   Tajik r
--
######## 237fe5b4c78ded82
Etymology 1  [ edit ]    This section or entry lacks references or sources. Please help verify this information by adding appropriate citations . You can also discuss it at the Tea Room .  Particularly: “Are we certain the term was borrowed from Avestan and not inherited from a common ancestor?”   Inherited from Middle Persian twlkʾ ( /⁠tōlag⁠/ , “ baby animal, whelp ” ) , from Avestan 𐬙𐬀𐬎𐬭𐬎𐬥𐬀 ( ta u runa , “ young ” ) , Northern Luri تیله ( tilə ) . Cognate with Sanskrit तरुण ( taruṇa , “ juvenile ” ) . Cf. تور ( tōr  / tur , “ uncivilized ” ) .   Noun  [ edit ]    توله • ( tōla / tule )    whelp    Alternative forms  [ edit ]    توره ( tōra  / ture )    Derived terms  [ edit ]    توله‌سگ (
--
Etymology 2  [ edit ]    Inherited from Middle Persian *tōlag , whence also Arabic طَوْلَق ( ṭawlaq , “ mallow ” ) . Probably a variation of ترشه ( turša  / torše , “ sorrel, dock ” ) , تور ( tōr  / tur , “ rosy dock ” )    Noun  [ edit ]    توله • ( tōla / tule )    mallow    Etymology 3  [ edit ]    Borrowed from Hindustani   तोला / تولا ( tolā ) . The weight corresponds to the weight of an Indian silver rupee during the whole Mughal Empire .   Noun  [ edit ]    توله • ( tōla / tule )    alternative form of تولا ( tōlā  / tulâ , “ weight measure for especially silver and gold of about 11.6 grams ” )    References  [ edit ]    Vullers, Johann August ( 1855 ), “ توله ”, in Lexicon Persico-La
--
Etymology 3  [ edit ]    Borrowed from Hindustani   तोला / تولا ( tolā ) . The weight corresponds to the weight of an Indian silver rupee during the whole Mughal Empire .   Noun  [ edit ]    توله • ( tōla / tule )    alternative form of تولا ( tōlā  / tulâ , “ weight measure for especially silver and gold of about 11.6 grams ” )    References  [ edit ]    Vullers, Johann August ( 1855 ), “ توله ”, in Lexicon Persico-Latinum etymologicum cum linguis maxime cognatis Sanscrita et Zendica et Pehlevica comparatum, e lexicis persice scriptis Borhâni Qâtiu, Haft Qulzum et Bahâri agam et persico-turcico Farhangi-Shuûrî confectum, adhibitis etiam Castelli, Meninski, Richardson et aliorum operibus et 
--
######## 223810e93712a689
Etymology  [ edit ]    Etymology tree   Proto-Indo-European *tréyes   Proto-Indo-Iranian *tráyas   Proto-Iranian *θráyah   Old Persian 𐏂 ( ç )   Persian سه    Proto-Indo-European *ten-   Persian تار    Persian سه‌تار    From سه ( si  / se , “ three ” ) +‎ تار ( tār  / târ , “ string ” ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /si.ˈtaːr/    ( Dari, formal ) IPA ( key ) : [seː.t̪ʰɑːɾ]    ( Dari, formal ) IPA ( key ) : [seː.t̪ʰɑːɾ]   ( Kabuli ) IPA ( key ) : [seː.t̪ʰɑːɾ]    ( Hazaragi ) IPA ( key ) : [seː.t̪ʰɔːɾ]    ( Iran, formal ) IPA ( key ) : [se.t̪ʰɒːɹ]    ( Tajik, formal ) IPA ( key ) : [se.t̪ʰɔɾ]    Rhymes: -aːr    Readings   Classical reading ?    si-tār   Dar
--
######## 4f0007efba68ca07
Etymology  [ edit ]    From Hindi सितार ( sitār ) / Urdu ستار ( sitār ) , from Classical Persian سه‌تار ( si-tār , literally “ three strings ” ) . [ 1 ] [ 2 ] Doublet of setar .   Pronunciation  [ edit ]    ( General American ) IPA ( key ) : /ˈsɪtɑɹ/ , /sɪˈtɑɹ/    Audio ( US ) : ( file )    Rhymes: -ɑː(ɹ)    Noun  [ edit ]    sitar ( plural sitars )    ( music ) A Hindustani / Indian classical stringed instrument , typically having a gourd as its resonating chamber .   Derived terms  [ edit ]    clitar   electric sitar   sitarist   sitarlike   Sitarmaker    Translations  [ edit ]    musical instrument   Arabic: please add this translation if you can    Armenian: սիտար ( sitar )    Chinese:  
--
Etymology 1  [ edit ]    Undetermined.   Alternative forms  [ edit ]    sita    Verb  [ edit ]    sitar    to accost ; to approach and speak to boldly or aggressively, as with a demand or request   Etymology 2  [ edit ]    Etymology tree   Proto-Indo-European *tréyes   Proto-Indo-Iranian *tráyas   Proto-Iranian *θráyah   Old Persian 𐏂 ( ç )   Persian سه    Proto-Indo-European *ten-   Persian تار    Persian سه‌تار ( se-târ )   English sitar der.   Cebuano sitar    Derived from English sitar , from Persian سه‌تار ( se-târ , “ three strings ” ) .   Noun  [ edit ]    sitar    sitar ( a Hindustani / Indian classical stringed instrument , typically having a gourd as its resonating chamber )    Fin
--
Etymology 2  [ edit ]    Etymology tree   Proto-Indo-European *tréyes   Proto-Indo-Iranian *tráyas   Proto-Iranian *θráyah   Old Persian 𐏂 ( ç )   Persian سه    Proto-Indo-European *ten-   Persian تار    Persian سه‌تار ( se-târ )   English sitar der.   Cebuano sitar    Derived from English sitar , from Persian سه‌تار ( se-târ , “ three strings ” ) .   Noun  [ edit ]    sitar    sitar ( a Hindustani / Indian classical stringed instrument , typically having a gourd as its resonating chamber )    Finnish  [ edit ]    Etymology  [ edit ]    Ultimately from Persian سه‌تار ( se-târ ) .   Pronunciation  [ edit ]    IPA ( key ) : /ˈsitɑr/ , [ˈs̠it̪ɑ̝r]    Rhymes: -itɑr    Syllabification ( key ) : s
--
Etymology  [ edit ]    Ultimately from Persian سه‌تار ( se-târ ) .   Pronunciation  [ edit ]    IPA ( key ) : /ˈsitɑr/ , [ˈs̠it̪ɑ̝r]    Rhymes: -itɑr    Syllabification ( key ) : si‧tar    Hyphenation ( key ) : si‧tar    Noun  [ edit ]    sitar    ( music ) sitar ( instrument )    Declension  [ edit ]    Inflection of sitar ( Kotus type 6/ paperi , no gradation)   nominative   sitar    sitarit    genitive   sitarin    sitarien   sitareiden   sitareitten    partitive   sitaria    sitareita   sitareja    illative   sitariin    sitareihin    singular   plural   nominative   sitar    sitarit    accusative   nom.    sitar    sitarit    gen.   sitarin    genitive   sitarin    sitarien   sitareiden
--
Etymology  [ edit ]    From Persian سه‌تار ( se-târ ) , meaning “three strings”.   Noun  [ edit ]    sitar   m ( invariable )    ( music ) sitar    Anagrams  [ edit ]    -astri , Taris , Trias , astri , rista , rista' , ristà , sarti , stari , stira , stria , tarsi    Northern Kurdish  [ edit ]    Noun  [ edit ]    sitar   f    alternative form of star    Portuguese  [ edit ]    Etymology  [ edit ]    Etymology tree   Proto-Indo-European *tréyes   Proto-Indo-Iranian *tráyas   Proto-Iranian *θráyah   Old Persian 𐏂 ( ç )   Classical Persian سه    Proto-Indo-European *ten-   Classical Persian تار    Classical Persian سِه‌تَار ( si-tār ) bor.   Hindi सितार ( sitār ) bor.   Portuguese sitar    Bo
--
Etymology  [ edit ]    Etymology tree   Proto-Indo-European *tréyes   Proto-Indo-Iranian *tráyas   Proto-Iranian *θráyah   Old Persian 𐏂 ( ç )   Classical Persian سه    Proto-Indo-European *ten-   Classical Persian تار    Classical Persian سِه‌تَار ( si-tār ) bor.   Hindi सितार ( sitār ) bor.   Portuguese sitar    Borrowed from Hindi सितार ( sitār ) .   Pronunciation  [ edit ]    ( Brazil ) IPA ( key ) : /siˈtaʁ/ [siˈtah]    ( Brazil ) IPA ( key ) : /siˈtaʁ/ [siˈtah]   ( São Paulo ) IPA ( key ) : /siˈtaɾ/    ( Rio de Janeiro ) IPA ( key ) : /siˈtaʁ/ [siˈtaχ]    ( Caipira ) IPA ( key ) : /siˈtaɻ/    ( Portugal ) IPA ( key ) : /siˈtaɾ/    ( Portugal ) IPA ( key ) : /siˈtaɾ/   ( Southern Portug
--
Etymology  [ edit ]    Unknown.   Noun  [ edit ]    sitar   m ( plural sitari )    Eurasian woodcock ( Scolopax rusticola )   Declension  [ edit ]    singular   plural   indefinite   definite   indefinite   definite   nominative - accusative    sitar    sitarul    sitari    sitarii    genitive - dative    sitar    sitarului    sitari    sitarilor    vocative    sitarule    sitarilor    Spanish  [ edit ]    Alternative forms  [ edit ]    shitar (historic)   Noun  [ edit ]    sitar   m ( plural sitares )    ( music ) sitar ( Indian string instrument )    Further reading  [ edit ]    “ sitar ”, in Diccionario de la lengua española [ Dictionary of the Spanish Language ] (in Spanish), online vers
--
Etymology  [ edit ]    From Hindi सितार ( sitār ) and Urdu ستار ( sitār ) , from Classical Persian سه‌تار ( si-tār ) .   Pronunciation  [ edit ]    IPA ( key ) : /sɪˈtɑːr/    Noun  [ edit ]    sitar   c    ( music ) sitar ( Indian string instrument )    Declension  [ edit ]    Declension of sitar    nominative    genitive    singular   indefinite    sitar    sitars    definite    sitaren    sitarens    plural   indefinite    sitarer    sitarers    definite    sitarerna    sitarernas    References  [ edit ]    “ sitar ”, in Svensk ordbok [ Dictionary of Swedish ] (in Swedish)    Anagrams  [ edit ]    Ritas , riats , ritas    Retrieved from " https://en.wiktionary.org/w/index.php?title=sitar&o
--
######## 9fae7ffb1bbfef4b
Etymology  [ edit ]    According to Beekes, acquired from Pre-Greek . [ 1 ] Said Pre-Greek term may be ultimately derived from or at least related to Proto-Hurro-Urartian *kinnar ( “ lyre, harp ” ) .   Pronunciation  [ edit ]    IPA ( key ) : /ki.tʰá.raː/ → /ciˈθa.ra/ → /ciˈθa.ra/    ( 5 th BCE Attic ) IPA ( key ) : /ki.tʰá.raː/    ( 1 st CE Egyptian ) IPA ( key ) : /kiˈtʰa.ra/    ( 4 th CE Koine ) IPA ( key ) : /ciˈθa.ra/    ( 10 th CE Medieval ) IPA ( key ) : /ciˈθa.ra/    ( 15 th CE Constantinopolitan ) IPA ( key ) : /ciˈθa.ra/    Noun  [ edit ]    κῐθᾰ́ρᾱ • ( kĭthắrā )  f ( genitive κῐθᾰ́ρᾱς ) ; first declension    ( music ) lyre   Synonyms: λύρα ( lúra ) , φόρμιγξ ( phórminx ) , ψάλτιγξ
--
Etymology  [ edit ]    Semantic loan from Italian chitarra (from Arabic قِيثَارَة ( qīṯāra ) , from Latin cithara ), adapted to the form of Ancient Greek κιθάρα ( kithára ) .   Pronunciation  [ edit ]    IPA ( key ) : /ciˈθa.ra/    This entry needs an audio pronunciation . If you are a native speaker with a microphone, please record this word . The recorded pronunciation will appear here when it's ready.   Noun  [ edit ]    κιθάρα • ( kithára )  f ( plural κιθάρες )    ( music ) guitar    ( historical ) cithara , an ancient Greek musical instrument.   Declension  [ edit ]    Declension of κιθάρα    singular   plural   nominative   κιθάρα ( kithára )    κιθάρες ( kitháres )    genitive   κιθά
--
```


## [2026-10-15T02:49:35.012Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; ety(){ echo \"######## $1\"; python3 - \"$1\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1]+'.txt').read()\nms=[m.start() for m in re.finditer(r'Etymology( \\d)?\\s+\\[ edit \\]',t)]\nfor s in ms[:3]: print(t[s:s+800].replace('\\n',' '));print('--')\nEOF\n}; for h in fb369480c8d82900 c1548b4e6860b31f 8e73a48a54fae3b6 24d86a77ef2eca99 c61d87204ca77af8 01b7aae4b0476850 44226b5e67f65194; do ety $h; done 2>&1 | cut -c1-900; for h in 94de91440ef68db4 286c085416faf881 d653df26e423065c; do echo \"#### $h\"; grep -i -o \".\\{0,200\\}\\(Iranian\\|Persian\\|Avestan\\).\\{0,200\\}\" $h.txt | head -12; done",
 "description": "Print remaining Wiktionary etymologies"
}
```


### [2026-10-15T02:49:45.439Z] TOOL RESULT

```
######## fb369480c8d82900
Etymology  [ edit ]    Etymology tree   Pre-Greek der.   Ancient Greek κῐθᾰ́ρᾱ ( kĭthắrā ) bor.   Aramaic קיתרא ( qīṯārā ) bor.   Arabic قِيثَارَة ( qīṯāra ) bor.   Old Spanish guitarra   Spanish guitarra bor.   English guitar    From Spanish guitarra , from Arabic قِيثَارَة ( qīṯāra ) , from Ancient Greek κῐθᾰ́ρᾱ ( kĭthắrā ) . Doublet of cithara , cither , and zither , but not related to sitar .   Pronunciation  [ edit ]    ( Received Pronunciation ) IPA ( key ) : /ɡɪˈtɑː/   Audio ( UK ) : ( file )    ( General American ) IPA ( key ) : /ɡɪˈtɑɹ/   Audio ( US ) : ( file )    ( Southern US ) IPA ( key ) : /ˈɡɪt.ɑɹ/    Hyphenation: gui‧tar    Rhymes: -ɑː(ɹ)    Noun  [ edit ]    guitar ( plural guitars )    ( music ) A stringed musical instrument , of European origin, usually with a fretted fi
--
Etymology  [ edit ]    From guit +‎ -ar .   Pronunciation  [ edit ]    IPA ( key ) : ( Northern , Balearic , Central , Northwestern ) [ɡiˈta]    IPA ( key ) : ( Valencia ) [ɡiˈtaɾ]    Verb  [ edit ]    guitar ( first-person singular present guito , first-person singular preterite guití , past participle guitat )    ( intransitive ) to kick , to buck ( of horses and mules )    Conjugation  [ edit ]        Central Catalan conjugation of guitar ( first conjugation )   infinitive    guitar    gerund    guitant    past participle    masculine   feminine   singular   guitat    guitada    plural   guitats    guitades    person   singular   plural   first   second   third   first   second   third   indicative    jo    tu    ell / ella   vostè    nosaltres   nós    vosaltres   vós    ells / elles  
--
######## c1548b4e6860b31f
Etymology  [ edit ]    Borrowed from German Zither , from Old High German zithara , from Latin cithara , from Ancient Greek κιθάρα ( kithára , “ a kind of harp ” ) . Doublet of cithara , cither , and guitar .   Pronunciation  [ edit ]    ( Received Pronunciation ) IPA ( key ) : /ˈzɪ.ðə/    Audio ( Southern England ) : ( file )    ( General American ) IPA ( key ) : /ˈzɪ.ðɚ/    Rhymes: -ɪðə(ɹ)    Noun  [ edit ]    zither ( plural zithers )    ( music ) A musical instrument consisting of a flat sounding box with numerous strings placed on a horizontal surface , played with a plectrum or fingertips .  1999 August 24, Japhet Asher and Peter Gaffney , “Insomnia” (5:30 from the start), in Downtown ‎ [1] , season 1, episode 4, spoken by Alex Henson (Gregory Gilmore), archived from the original on 
--
######## 8e73a48a54fae3b6
Etymology  [ edit ]    Etymology tree   Pre-Greek der.   Ancient Greek κῐθᾰ́ρᾱ ( kĭthắrā ) bor.   Aramaic קיתרא ( qīṯārā ) bor.   Arabic قيثارة    Borrowed from Aramaic קיתרא ( qīṯārā ) , from Ancient Greek κῐθᾰ́ρᾱ ( kĭthắrā ) .   Pronunciation  [ edit ]    IPA ( key ) : /qiː.θaː.ra/    This entry needs an audio pronunciation . If you are a native speaker with a microphone, please record this word . The recorded pronunciation will appear here when it's ready.   Noun  [ edit ]    قِيثَارَة • ( qīṯāra )  f ( plural قِيثَارَات ( qīṯārāt ) or قَيَاثِير ( qayāṯīr ) )    ( music ) guitar    Declension  [ edit ]    Declension of noun قِيثَارَة ( qīṯāra )   singular   singular triptote in ـَة ( -a )    indefinite   definite   construct   informal   قِيثَارَة   qīṯāra    الْقِيثَارَة   al-qīṯāra   
--
######## 24d86a77ef2eca99
Etymology  [ edit ]    From Late Middle English , from Old French taffetas , from Medieval Latin taffata , from Classical Persian تافته ( tāfta ) , from تافتن ( tāftan ) .   Pronunciation  [ edit ]    IPA ( key ) : /ˈtæ.fɪ.tə/ , /ˈtæ.fə.tə/    Audio ( Southern England ) : ( file )    Noun  [ edit ]    taffeta ( countable and uncountable , plural taffetas )    A crisp , smooth woven fabric made from silk or synthetic fibers .  1634 (first performance), William D’avenant [ i.e. , William Davenant ], The Wits: A Comedie;   [ … ] , published 1636 ; republished in Two Excellent Plays:   [ … ] , London: [ … ] G. Bedel, and T [ homas ] Collins,   [ … ] , 1665 , →OCLC , Act I, page 1 : Could a Taff'ta ſcarf, a long Eſtridge vvhing, / A ſtiffe Iron Doublet, and a Brazeel Pole / Tempt thee from Camb
--
######## c61d87204ca77af8
Etymology  [ edit ]    Etymology tree   Old English tæppa   Middle English tape   English tape    From Middle English tape , tappe , from Old English tæppa , tæppe ( “ ribbon, tape ” ) ; further origin unclear.   Probably akin to Old Frisian tapia ( “ to pull, rip, tear ” ) , Middle Low German tappen , tāpen ( “ to grab, pull, rip, tear, snatch ” ) , Middle High German zāfen , zāven ( “ to pull, tear ” ) .   Pronunciation  [ edit ]    enPR : tāp , ( Received Pronunciation , General American ) IPA ( key ) : /teɪ̯p/ , [tʰeɪ̯p]    Audio ( General American ) : ( file )    Rhymes: -eɪp    Noun  [ edit ]    tape ( countable and uncountable , plural tapes )    A videotape   Flexible material in a roll with a sticky surface on one or both sides; adhesive tape .  Hand me some tape . I need to fix a
--
Etymology 1  [ edit ]    From English tape ( “ adhesive tape ” ) .   Pronunciation  [ edit ]    IPA ( key ) : /tɛjp/ , [tˢɛjb̥]    Noun  [ edit ]    tape   c ( singular definite tapen , not used in plural form )    Scotch tape , adhesive tape    Synonyms  [ edit ]    klisterbånd    klæbestrimmel    Further reading  [ edit ]    tape on the Danish Wikipedia. Wikipedia da    Etymology 2  [ edit ]    From English tape ( “ magnetic tape ” ) .   Pronunciation  [ edit ]    singular IPA ( key ) : /tɛjp/ , [tˢɛjb̥]    plural IPA ( key ) : /tɛjpə/ , [ˈtˢɛjb̥ə]    Noun  [ edit ]    tape   n ( singular definite tapet , plural indefinite tapes or tape )    ( rare ) video or audio cassette tape  Synonym: ( more common ) bånd    Etymology 3  [ edit ]    From English tape ( “ to bind with adhesive tape ” 
--
Etymology 2  [ edit ]    From English tape ( “ magnetic tape ” ) .   Pronunciation  [ edit ]    singular IPA ( key ) : /tɛjp/ , [tˢɛjb̥]    plural IPA ( key ) : /tɛjpə/ , [ˈtˢɛjb̥ə]    Noun  [ edit ]    tape   n ( singular definite tapet , plural indefinite tapes or tape )    ( rare ) video or audio cassette tape  Synonym: ( more common ) bånd    Etymology 3  [ edit ]    From English tape ( “ to bind with adhesive tape ” ) .   Pronunciation  [ edit ]    infinitive IPA ( key ) : /tɛjpə/ , [ˈtˢɛjb̥ə]    imperative IPA ( key ) : /tɛjp/ , [tˢɛjb̥ˀ]    Verb  [ edit ]    tape ( imperative tape , infinitive at tape , present tense taper , past tense tapede , perfect tense er/har tapet )    tape ( to bind with adhesive tape ) [from 1965]    Dutch  [ edit ]    Etymology  [ edit ]    Borrowed from E
--
######## 01b7aae4b0476850
Etymology  [ edit ]    From Middle English tapestrie , from Old French tapisserie ( “ tapestry ” ) , from Ancient Greek τάπης ( tápēs ) , from an Iranian source.   Pronunciation  [ edit ]    enPR : tă'pəstrē , IPA ( key ) : /ˈtæpəstɹi/    Audio ( US ) : ( file )    Noun  [ edit ]    Tapestry Room from Croome Court.   tapestry ( countable and uncountable , plural tapestries )    A heavy woven cloth , often with decorative pictorial designs , normally hung on walls.  1963 , Margery Allingham , chapter 3, in The China Governess: A Mystery , London: Chatto & Windus , →OCLC : Sepia Delft tiles surrounded the fireplace, their crudely drawn Biblical scenes in faded cyclamen blending with the pinkish pine, while above them, instead of a mantelshelf, there was an archway high enough to form a balco
--
######## 44226b5e67f65194
Etymology  [ edit ]    The origin is uncertain. Traditionally derived from Iranian (compare Persian تنبسه ( tanbase , “ carpet, rug ” ) ), but Beekes argues for a Pre-Greek origin, and implies that the Iranian forms are not cognate. [ 1 ]    Noun  [ edit ]    τᾰ́πης • ( tắpēs )  m ( genitive τᾰ́πητος ) ; third declension    carpet , rug , mat    Declension  [ edit ]    Third declension of ὁ τᾰ́πης ; τοῦ τᾰ́πητος ( Attic )   Case / #   Singular   Dual   Plural   Nominative   ὁ τᾰ́πης   ho tắpēs    τὼ τᾰ́πητε   tṑ tắpēte    οἱ τᾰ́πητες   hoi tắpētes    Genitive   τοῦ τᾰ́πητος   toû tắpētos    τοῖν τᾰπήτοιν   toîn tăpḗtoin    τῶν τᾰπήτων   tôn tăpḗtōn    Dative   τῷ τᾰ́πητῐ   tōî tắpētĭ    τοῖν τᾰπήτοιν   toîn tăpḗtoin    τοῖς τᾰ́πησῐ / τᾰ́πησῐν   toîs tắpēsĭ(n)    Accusative   τὸν τᾰ́πητᾰ   
--
#### 94de91440ef68db4
ugrep: error: error at position 104
vestan)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
               exceeds complexity limits___/


#### 286c085416faf881
ugrep: error: error at position 104
vestan)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
               exceeds complexity limits___/


#### d653df26e423065c
ugrep: error: error at position 104
vestan)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
               exceeds complexity limits___/
```


## [2026-10-15T02:49:48.462Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for h in 94de91440ef68db4 286c085416faf881 d653df26e423065c; do echo \"#### $h\"; python3 -c \"\nimport sys,re\nt=open('$h.txt').read().replace('\\n',' ')\ni=t.find('Reconstruction'); \nfor k in ['Meaning','Etymology','Proto-Iranian','Persian','Avestan','Derived terms']:\n  for m in list(re.finditer(k,t))[:2]: print(k,'::',t[m.start():m.start()+350]); \n\"; done | cut -c1-500 | head -60",
 "description": "Inspect PIE reconstruction pages"
}
```


### [2026-10-15T02:49:49.062Z] TOOL RESULT

```
#### 94de91440ef68db4
Proto-Iranian :: Proto-Iranian: *tánθram [ 19 ] ~ *tā́nθram [ 14 ]   Persian: تار ( târ )   Tajik: тор ( tor )    Yidgha: [script needed] ( tūr )    Pashto: تور ( tōr )    *tén-tu-s ~ *tn̥-téw-s [ 3 ]   Proto-Indo-Iranian: *tántuš   Proto-Indo-Aryan: *tántuṣ   Sanskrit: तन्तु ( tántu )    *tn̥-néh₂ [ 3 ] [ 20 ]    *-tn̥-nó-s , *-tn̥-nis ( suffix denoting extent of 
Persian :: Persian: تار ( târ )   Tajik: тор ( tor )    Yidgha: [script needed] ( tūr )    Pashto: تور ( tōr )    *tén-tu-s ~ *tn̥-téw-s [ 3 ]   Proto-Indo-Iranian: *tántuš   Proto-Indo-Aryan: *tántuṣ   Sanskrit: तन्तु ( tántu )    *tn̥-néh₂ [ 3 ] [ 20 ]    *-tn̥-nó-s , *-tn̥-nis ( suffix denoting extent of time ) [ 21 ]    *tn̥-tós [ 3 ] [ 22 ]    *tón-os [ 
Persian :: Persian: [script needed] ( ttn' /⁠tadan⁠/ )    References  [ edit ]    ^ Pokorny, Julius ( 1959 ), Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 3, Bern, München: Francke Verlag, page 1065f    ↑ 2.0 2.1 2.2 2.3 2.4 2.5 2.6 Rix, Helmut , editor ( 2001 ), Lexikon der indogermanischen Verben [
Derived terms :: Derived terms    1.2   References    Toggle the table of contents    Reconstruction:Proto-Indo-European/ ten-    Add languages    Reconstruction    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   
Derived terms :: Derived terms  [ edit ]    Terms derived from the Proto-Indo-European root *ten- (87 c, 0 e)    *tén-t ~ *tn-ént ( athematic root aorist )   Proto-Celtic: *tenti   Old Irish: téit    Proto-Indo-Iranian: *Hátant   Proto-Indo-Aryan: *Hátant   Sanskrit: अतन् ( átan )    *tén-ye-ti ( innovative ye-present ) [ 2 ] [ 4 ] [ 5 ] [ 6 ]   Proto-Albanian: *en
#### 286c085416faf881
Etymology :: Etymology    1.2   Root    1.2.1   Derived terms    1.3   References    Toggle the table of contents    Reconstruction:Proto-Indo-European/ tengʰ-    Add languages    Reconstruction    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links he
Etymology :: Etymology  [ edit ]    Extension of *ten- ( “ to stretch; to extend ” ) . [ 1 ]    Root  [ edit ]    *tengʰ- [ 2 ]    to pull ( back ) [ 2 ]    to be heavy , difficult [ 3 ]    Derived terms  [ edit ]    Terms derived from the Proto-Indo-European root *tengʰ- (49 c, 0 e)    *téngʰ-t ~ tn̥gʰ-ént ( root aorist ) [ 2 ]   Proto-Balto-Slavic: *tengtei ~
Proto-Iranian :: Proto-Iranian: *θanǰáyati ( “ to pull; to weigh (down) ” ) ( see there for further descendants )   *tn̥gʰ-eh₁(yé)-ti ( eh₁-stative )   Proto-Balto-Slavic: *tingēˀtei   Lithuanian: tingė́ti ( “ to be lazy ” ) [ 6 ]    Proto-Slavic: *tęžati ( see there for further descendants )  ⇒ Proto-Slavic: *tęžava ( “ weight ” ) ( see there for further descendan
Derived terms :: Derived terms    1.3   References    Toggle the table of contents    Reconstruction:Proto-Indo-European/ tengʰ-    Add languages    Reconstruction    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file 
Derived terms :: Derived terms  [ edit ]    Terms derived from the Proto-Indo-European root *tengʰ- (49 c, 0 e)    *téngʰ-t ~ tn̥gʰ-ént ( root aorist ) [ 2 ]   Proto-Balto-Slavic: *tengtei ~ *tingtei   Proto-Slavic: *tęťi   pf ( “ to pull ” ) [ 4 ] ( see there for further descendants )  ⇒ Proto-Slavic: *tędzati   impf ( “ to pull, to extract ” ) [ 5 ] ( see there f
#### d653df26e423065c
Etymology :: Etymology    1.2   Root    1.2.1   Reconstruction notes    1.2.2   Derived terms    1.3   References    1.4   Further reading    Toggle the table of contents    Reconstruction:Proto-Indo-European/ temp-    Add languages    Reconstruction    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions  
Etymology :: Etymology  [ edit ]    Perhaps an extension of *ten- . [ 1 ]    Root  [ edit ]    *temp- [ 2 ] [ 3 ]    to stretch , exert an effort on   Reconstruction notes  [ edit ]    According to the EIEC, if the root is connected with tempus ( “ time ” ) , then it may indicate that the Proto-Indo-European people viewed time as a linear construct. [ 1 ]    De
Proto-Iranian :: Proto-Iranian: *tāp- ( “ to twist, wind ” ) [ 10 ]   Persian: تاب ( tâb , “ swing ” ) , تافتن ( tâftan , “ to twist, twine ” )    Proto-Tocharian: [ 11 ]   Tocharian A: tampe    References  [ edit ]    ↑ 1.0 1.1 Mallory, J. P. , Adams, D. Q. , editors ( 1997 ), “*temp-”, in Encyclopedia of Indo-European Culture , London, Chicago: Fitzroy Dearborn P
Persian :: Persian: تاب ( tâb , “ swing ” ) , تافتن ( tâftan , “ to twist, twine ” )    Proto-Tocharian: [ 11 ]   Tocharian A: tampe    References  [ edit ]    ↑ 1.0 1.1 Mallory, J. P. , Adams, D. Q. , editors ( 1997 ), “*temp-”, in Encyclopedia of Indo-European Culture , London, Chicago: Fitzroy Dearborn Publishers, page 187    ↑ 2.0 2.1 Rix, Helmut , editor
Derived terms :: Derived terms    1.3   References    1.4   Further reading    Toggle the table of contents    Reconstruction:Proto-Indo-European/ temp-    Add languages    Reconstruction    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Relate
Derived terms :: Derived terms  [ edit ]    Terms derived from the Proto-Indo-European root *temp- (2 c, 0 e)    *témp-e-ti ( thematic root present ) [ 2 ]   Proto-Balto-Slavic: *témptei [ 4 ]   > ? Lithuanian: tem̃pti ( “ to pull, stretch ” ) ( or < ye-present *témp-ye-ti [ 5 ] )    Proto-Tocharian:   Tocharian A: cämp-    Tocharian B: cämp-    *tḗmp-s-t ~ *témp-s
```


## [2026-10-15T02:49:54.174Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; N='page 501, root Ten/Tengh/Temp'; for u in 'https://abadis.ir/fatofa/گیتار/' 'https://abadis.ir/fatofa/توره/' 'https://abadis.ir/fatofa/ترانه/' 'https://abadis.ir/fatofa/هنجار/' 'https://ahdictionary.com/word/search.html?q=sitar' 'https://ahdictionary.com/word/search.html?q=zither' 'https://ahdictionary.com/word/search.html?q=cittern' 'https://ahdictionary.com/word/search.html?q=guitar'; do python3 tools/fetch_source.py \"$u\" --note \"$N\" 2>&1|tail -1; done; tail -8 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l);print(d.get('status'),d.get('bytes'),d['file'],d['url'])\"",
 "description": "Archive abadis and AHD pages",
 "timeout": 300000
}
```


### [2026-10-15T02:50:01.616Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7a84b9c8dc75f783.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8fd7992668f9bc68.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cd9ec6f84ce544aa.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/506a7580260d2e99.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6ac3aefeb0281c7e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b3333730ea904770.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d67e163e9ca44d36.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b604ace6b606f5a7.txt
200 10227 data/verification/sources/web/8fd7992668f9bc68.txt https://abadis.ir/fatofa/توره/
200 15009 data/verification/sources/web/cd9ec6f84ce544aa.txt https://abadis.ir/fatofa/ترانه/
200 8729 data/verification/sources/web/506a7580260d2e99.txt https://abadis.ir/fatofa/هنجار/
200 4576 data/verification/sources/web/6ac3aefeb0281c7e.txt https://ahdictionary.com/word/search.html?q=sitar
200 4491 data/verification/sources/web/b3333730ea904770.txt https://ahdictionary.com/word/search.html?q=zither
200 4306 data/verification/sources/web/d67e163e9ca44d36.txt https://ahdictionary.com/word/search.html?q=cittern
200 784 data/verification/sources/web/4bb8bcd960615f28.txt https://vajehyab.com/moein/تخم
200 4426 data/verification/sources/web/b604ace6b606f5a7.txt https://ahdictionary.com/word/search.html?q=guitar
```


## [2026-10-15T02:50:04.793Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep \"7a84b9c8dc75f783\" index.jsonl | tail -1 | cut -c1-200; for h in 7a84b9c8dc75f783 8fd7992668f9bc68 cd9ec6f84ce544aa 506a7580260d2e99; do echo \"### $h\"; grep -o \"فرهنگ معین.\\{0,400\\}\" $h.txt | head -2; done; for h in 6ac3aefeb0281c7e b3333730ea904770 d67e163e9ca44d36 b604ace6b606f5a7; do echo \"### $h\"; grep -o \"\\[.\\{0,300\\}\\]\" $h.txt | head -3; done",
 "description": "Extract Mo'in and AHD text"
}
```


### [2026-10-15T02:50:05.246Z] TOOL RESULT

```
{"url": "https://abadis.ir/fatofa/گیتار/", "file": "data/verification/sources/web/7a84b9c8dc75f783.txt", "fetched": "2026-10-15T02:49:56Z", "status": 200, "bytes": 18879, "title": "گیتار - معنی در دیک
### 7a84b9c8dc75f783
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
### 8fd7992668f9bc68
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
### cd9ec6f84ce544aa
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
### 506a7580260d2e99
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
### 6ac3aefeb0281c7e
[Hindi sit ā r , from Persian : si , three; see trei- in the Appendix of Indo-European roots + t ā r , string; see ten- in the Appendix of Indo-European roots .]
### b3333730ea904770
[German, from Middle High German *zitter , from Old High German zitera , from Latin cithara , cithara, from Greek kithar ā .]
### d67e163e9ca44d36
[Perhaps blend of Latin cithara , cithara; see CITHARA , and obsolete English gittern (from Middle English, from Old French guiterne , from Latin cithara ).]
### b604ace6b606f5a7
[French guitare , fromSpanish guitarra , fromGreek kithar ā , cithara.]
```


## [2026-10-15T02:50:07.982Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for h in 7a84b9c8dc75f783 8fd7992668f9bc68 cd9ec6f84ce544aa 506a7580260d2e99; do echo \"### $h\"; grep -n \"معین\\|\\[ \\?فر\\|په\\.\\|(اِ\\.)\\|( اِ . )\" $h.txt | head -8 | cut -c1-300; done",
 "description": "Locate Mo'in entries in abadis pages"
}
```


### [2026-10-15T02:50:08.328Z] TOOL RESULT

```
### 7a84b9c8dc75f783
26: فرهنگ معین
28: [ فر. ] (اِ. ) از سازهای زهی که دارای شش سیم می باشد و با انگشتان دست نواخته می شود. 
41:جد بزرگ تمام سازهایی که ما به عنوان کوردوفون از آن ها یاد کردیم یک کمان موسیقی است که تنها یک سیم ساده به دو سر آن متصل بوده است که با کشیدن و رها کردن سیم صدایی در کمان ایجاد می شده و این صدا به وسیله یک تقویت کننده صوت که به آن متصل بوده تقویت می شده است. ازآنجاکه این سیم تنها یک صدای ساده ایجا
122:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
135:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
192: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرد
### 8fd7992668f9bc68
19: ( تورة ) تورة. [ ت َ رَ ] ( ع اِ ) دختری که میانجی گری کند میان عشاق. ( منتهی الارب ) ( ناظم الاطباء ). رجوع به تور شود. توره. [ رَ / رِ ] ( اِ ) جانوری است که او را شغال گویند. ( برهان ) ( از فرهنگ جهانگیری ) ( از فرهنگ رشیدی ) ( از انجمن آرا ) ( از آنندراج ) ( از شرفنامه منیری ) ( از ناظم الاط
23: توره. [ ت َ رِ ] ( اِ ) فرزند عزیز و گرامی را گویند. ( برهان ) ( از شرفنامه منیری ) ( ناظم الاطباء ). خواه پسر باشد یا دختر. ( ناظم الاطباء ). در اوستا تئورونه صفت است به معنی جوان و برای بچه آدمی و جانور بکار رفته و توره ( شغال ) و توله از همین ریشه است. ( حاشیه برهان چ معین ). || محبوب و معشوق
32: فرهنگ معین
98:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
197: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرد
### cd9ec6f84ce544aa
27: ترانه. [ ت َ ن َ / ن ِ ] ( اِ ) جوان خوش صورت و شاهد تر و تازه و صاحب جمال. ( برهان ) ( ناظم الاطباء ). جوان خوش صورت و صاحب کمال. ( فرهنگ جهانگیری ). جوان خوش صورت و شاهد تر و تازه. ( فرهنگ رشیدی ) ( انجمن آرا ) ( آنندراج ). شاهدان تر و تازه. ( شرفنامه منیری ) ( فرهنگ خطی کتابخانه سازمان ). جوا
48: فرهنگ معین
81:(برگرفته از ریشۀ اوستایی تورونه Tauruna) در لغت به معنای خُرد، تَر و تازه و جوان خوش صورت، و در اصطلاح سرودۀ کوتاهی که به بلندی و کوتاهی مصراع های آن چندان توجهی نشود و با یکی از الحان موسیقی هماهنگ باشد. خاستگاه و منشأ ترانه ها به درستی روشن نیست، و اهمیت آن ها بیشتر به جهت خاستگاه ملّی و مردمی 
219: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرد
### 506a7580260d2e99
20: هنجار. [ هَِ / هََ ] ( اِ ) راه و روش و طریق و طرز و قاعده و قانون. ( برهان ). در سنسکریت سمکارا به معنی گشتن و گردیدن و راه است. ( حاشیه برهان چ معین ) : 
68: فرهنگ معین
161:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
211: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرد
```


## [2026-10-15T02:50:12.425Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; for w in 'فرهنگ' 'آهیختن' 'تافتن' 'تار' 'توله' 'سه‌تار\\|سه تار\\|ستار'; do echo \"== $w\"; grep -n \"$w\" ARY_pages.txt | head -3 | cut -c1-250; done; grep -n \"TAFTAN\\|FARHANG\\|AHIXTAN\\|TULE\\|TOLE\\|TAR\\b\" ARY_latin_index_pages.txt | head",
 "description": "Search Aryanpur for headwords"
}
```


### [2026-10-15T02:50:12.830Z] TOOL RESULT

```
== فرهنگ
83:می‌بردند و وپژگی‌های بدنی و اجتماعی و فرهنگی آنان را مورد ستایش قرار می‌دادند. در دوران
177:فرهنگی و زبانشناسی آنها را روشن می‌کند. بررسی کوچگری مردمان ترکك زبان مثال بسیار مفیدی
352:باعث شد که این زبان و فرهنگك غیر هند و اروپایی نابود گردد. مدارکك موجود نشان می‌دهد که در
== آهیختن
== تافتن
5459:فارسی (//۳85۸54): تابیدن, تافتن, تاب (به چم اگرداندن" و "پیچیدن)
5820:تف» تفت» تفتان» تافتن» نفسیدن / ۱۹۹
5832:فارسی (۷(ی۳8): تفء تفت, تفتان, تافتن, تفسیدن
== تار
12:۰ پیشگفتار ۳
13:پیش گفتار
176:بررسی جنبش‌های کوچگرانه‌ی دیگر در دوران‌های تاریخی الگوی کلی این کوج‌ها و پيامدهای
== توله
== سه‌تار\|سه تار\|ستار
1306:ضمناً چون این واژه‌ها از راه بازسازی به وجود آمده‌اند. طبق رسم معمول جلو آنها یک ستاره (:)
4837:اس نی باین واژه+در تخاری ۸ و نخاری 8 توجه و پرستاری کردن.
6243:چم این واژه در زبان‌های ابرلندی کهن و گالی: خواستار شدن» درخواست (کردن). :
981:ght Le (ayaa gas GPITAR © PITER 9 (ity gx 4 JOVE+ JU) JUPITER
1633:US-+MATAR-
1681:WERIAN  :(OLD ENGLISH) gS godt WASTAR, (PAHLAVI) 5 34,
1682:WEAR ENGLISH) 5-JS3! WASTARAG-, ASTAR
1701:¢ (enlace Si (laS ge 22 eat cal slasdls Sao ASTAR shy)" 1" ody all “1
1703:| wae WSU, ale CASTAR os slay Godly a) Sab cl slansly Geen oY
2511:TAR (SWEDISH) (528 y« ASRU, ASHRU, :(SANSKRIT) cy Ste
2525:BUCK: (TEAR) 1130 TAR
2526:ONIONS: (TEAR) 906 TAR HOLD NORSE) eS p95
2527:SKEAT: (TEAR) 633 TAR HOLD FRISIAN) oS 532
```


## [2026-10-15T02:50:15.322Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 5445,5465p ARY_pages.txt; awk 'NR<=5459' ARY_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1; grep -n \"تنیدن\\|تَنیدن\" ARY_pages.txt | head -3",
 "description": "Read Aryanpur tāftan entry"
}
```


### [2026-10-15T02:50:15.699Z] TOOL RESULT

```
اوستی (05587[76): 7 ,31۷ نروژی (۸/0۳780۵۸)+ 77
کردی (7ل0/5ل0): زر هلندی (007677): ۷7
بلوچی (31ل6لام): ۳6 لینرانی (۵(۷1۸0تا77ل): دا
سانسکریت (854867): ایرلدی کهن (نل5لجا 0ا :)0‏ " 11
۸ ل ۴17 ,۸5 ۷]ظ َ
یونانی (07280): 85 ,۶1۸ پسگشت‌ها اند ای دی دنا ۲
لاین ۰:07 2618 ,0710405 8 ۶00800
ابسلندی کهن (/0/0447/7۸9آل5 صاه): 1 (۳1۸7) تا اما
3 ود 9 (885تم#ه) بت ۱۸ وا
نورس کهن (۸0788 012): ۳7۸ 4 (1۸1) :۸۸52/5
سا کسونی کهن (/542:00 ل0): 77 47 (5۸1) :005
فریزی کهن (514(7ل۲۸ 2ا0): 7 9 (5۸7) +57
آلمانی کهن ((ف02794 07اب صاه): ۲812 برهان قاطم + ۳۵۰
آلمانی (/(0571۸): 7 ,7787
فارسی (//۳85۸54): تابیدن, تافتن, تاب (به چم اگرداندن" و "پیچیدن)
اوستایی (۸(897/۷): 1 لاتین (147100):
پپلری (7ماتل۳۸): 727۸7۸ ,72810۸ 01 ,783170875 ,718240105
تخاری 4 (۸ ۸4ل70727۸7): ۳11 فرانسه (7[ع/(۳8): را ان ۷
تخاری 8 (8 4( 70827۸7): دا ابتالیایی (ف4ا7۸). 713/17۸
ارمنی (۸4814): 718 رومانی (24۸(2): 78/7۲۸
پونانی 082570): ندرا پرتغالی (0070010532): 71821708۸
[pdf page 185]
5519:۴ بازگشت به: تنیدن و تار, ۰
5979:۴ ا_تنیدن
```


## [2026-10-15T02:50:19.044Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 5975,5995p ARY_pages.txt; awk 'NR<=5979' ARY_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1; sed -n 5430,5440p ARY_pages.txt",
 "description": "Read Aryanpur تنیدن entry"
}
```


### [2026-10-15T02:50:19.409Z] TOOL RESULT

```
کردی (7215[7/): 6 ,736 ایسلندی کهن (0/017۸71۵7م5 صا0):
بلوچی (/7لجلال8۸): 71 ادا
افغانی (پشتو) (/7۸۷[ج۸7). 41 فریزی کهن (/نفا5ل7۶۶ صا0):
[pdf page 203]
۴ ا_تنیدن
7 ,71۸۳۲1 چک (2501)): ان :۷ با
آلمانی کهن (/(057014 101 صاه): اسلو| کی (5101430): 5 706۸
0۸135 لونی (نی) 00 8تاعهو7
آلمانی ((68894۸): 207 ایرلندی کهن (ن5لع] صان): تباید با مد
انگلیسی کهن (نلخلا800 صام: ۳037
انگلیسی (ت5لا8(/0): اون ایا پسگشت‌ها : ات تن
دانمارکی (5ا#ه): 712۸7 68 ۶0502200
سوئدی (8105015/7): 77 2 (11637) اه
نروژی (0/0777201۸۸: 77 7 016131 اد مد سا
هلندی (7لع017): 2107 3 (116111) :0702/5
اسلاوی کهن (ع۷1شا5 77637ل) صام). :57
۰ ال ران ن ۷ 9 (78310) ,647 (010151
لهستانی (3آ]۳0): اد ی برهان قاطع : ۵۱۹
روسی (/5314): 7637
پادداشت:
چم این واژه در اوستایی: نیرومند
[pdf page 203]
۱ 1۸ برهان قاطع : ۳۴۹
انگلیسی کهن (0ل8ل/80/0 2 7۸3/8 فرهنگ معین : ۹۶۹-۰
روژی (اممزه من دا لغت‌نامه دهخدا ۶۳
بادداشت:. ۹
۱- به احتمال زیاد واژه‌ی "پنیر" (پهلوی: ۱۳۸۷1 کردی: ۳338131) نیز از همین ريشه است.
۲- چم این واژه در سانسکریت: ورم کردن؛ یاد کردن,
چم این واژه در زبان‌های ژرمنی: خامه» سرشیر,
چم این واژه در زبان لیتوانی؛ شیر,
[pdf page 185]
اٍ ۶ پیه
| م‌انکلیسی سرواژهی نار رو 1385
```


## [2026-10-15T02:50:23.576Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"frahang\\|ahixt\\|āhixt\\|ahang\\|frahixt\\|hixtan\" SNS_pages.txt | head -10 | cut -c1-200; grep -c \"pdf page\\|\\f\" SNS_pages.txt",
 "description": "Search SNS glossary"
}
```


### [2026-10-15T02:50:24.083Z] TOOL RESULT

```
545:                                                                              FrO. :    H. Reichelt, Ver Frahang; dim. Wien 1900.
881:                                                                       Junker, H.F.J.        :   The Frahang i Pahlavik, Heidel-
892:Reichelt, H.: ber Frahang                                                                :   K.R. Cama Oriental Institute. Golden
16271:                                                         ey/e 9/15                   frahang 126/1
242
```


## [2026-10-15T02:50:27.234Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \" 7/[0-9]\\b\\| 147/[0-9]\\b\\| 126/[0-9]\\b\" SNS_pages.txt | cut -c1-250 | head -20",
 "description": "Find SNS index references to pages 7,126,147"
}
```


### [2026-10-15T02:50:27.587Z] TOOL RESULT

```
14894:                                                               prayah 126/7                 nambh-nabh- 282/3
15101:vis- 286/16              suwra 192/16                      ha&o-, haya 89/10        havista- 7/8
15183:                                                             pasus.haurva- 124/19       frayah- 126/7
15298:fi-hanc   7/3
15510:                                                        fr*y 126/8            h^rayn 6/13
15779:tuhtg 147/1-151/3-1 0-153/8ustur 325/1
15818:sab 197/12-235/6      skanSd 147/7                     t    145/1             tan tCxra 152/17
15819:sabag 197/18-20       skast 147/4-9-200/6              ta 285/14              tapisn 153/17
16141:                     havist 7/7                             ham-gum5zisnlh 54/13    harvisp 45/2
16143:                     hflvistan 7/9                          ham-kar 51/10           harvisp 3gSh 45/7
16271:                                                         ey/e 9/15                   frahang 126/1
16296:                                                         fray 126/6                  fraraQdan 131/6
16541:ahanjisn 7/2                arzSg Sraand tar 42/14                 axezend 220/10              299/21
```


## [2026-10-15T02:50:33.118Z] TOOL CALL #74: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe-private/site/pages/501.* 2>/dev/null; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && pdftoppm -f 501 -l 501 -r 150 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf pg501 && ls -la pg501.png",
 "description": "Render page 501 image"
}
```


### [2026-10-15T02:50:34.122Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   81k sfmqrb 14 Oct 22:15  /home/sfmqrb/git/rishe-private/site/pages/501.jpg
Permissions Size User   Date Modified Name
.rw-r--r--   68k sfmqrb 14 Oct 22:50  pg501.png
```


## [2026-10-15T02:50:35.638Z] TOOL CALL #75: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg501.png"
}
```


### [2026-10-15T02:50:35.652Z] TOOL RESULT

```

```


## [2026-10-15T02:51:07.645Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ten-\\|^tenə\\|^temp-\\|^tengh\" AHD_watkins1985.txt | head; grep -n \"SITAR\\|TAFFETA\\|TAPESTRY\" AHD_watkins1985.txt | head; grep -n -i \"frahajam\\|frāhajam\\|hanj-\\|θanj\\|\\bhang-\" KNT_full.txt | head -5 | cut -c1-250",
 "description": "Search Watkins and Kent"
}
```


### [2026-10-15T02:51:08.053Z] TOOL RESULT

```
1077:temp-
1079:ten-
1080:warp threads are stretched on the loom): TAFFETA; b. Iranian *tap-, “carpet,” in Greek tapés, carpet: TAPES- TRY. [Pok. temp- 1064.] ten-. To stretch. I. Derivatives with the basic meaning. 1. Suffixed form “ten-do- in: a. Latin tendere, to stretch, extend: TEND!, TENDER?, TENDON, TENSE!, TENT!; AT- TEND, CONTEND, DETENT, DISTEND, EXTEND, INTEND, OSTENSIBLE, PRETEND, SUBTEND; b. Latin portendere, “to stretch out before” (por-, variant of pro-, before; see per’), a technical term in augury, “to indicate, presage, foretell”: PORTEND. 2. Suffixed form *ten-yo- in Greek teinein, to stretch: TENESMUS; BRONCHIECTASIS, EPITA- SIS, HYPOTENUSE, PERITONEUM, PROTASIS, TELANGIEC- TASIA. 3. Suffixed zero-grade form *tn-nu- in Sanskrit tandéti, he stretches or weaves, with suffixed (instrumen- tal) derivative *ten-tro- in tantam, loom: TANTRA. 4. Suf- fixed form *ten-tro- in Persian ¢tdr, string: SITAR. 5. Basic form (with stative suffix) *ten-é- in Latin ten��re, to hold, keep, maintain (< “to cause to endure or con- tinue, hold on to”): TENABLE, TENACIOUS, TENACULUM, TENANT, TENEMENT, TENET, TENON, TENOR, TENURE, TENUTO; ABSTAIN, CONTAIN, CONTINUE, DETAIN, ENTER- TAIN, LIEUTENANT, MAINTAIN, OBTAIN, PERTAIN, PERTI- NACIOUS, RETAIN, (RETINACULUM), SUSTAIN. II. Derivatives meaning ‘‘stretched,” hence “thin.” 1. Suffixed zero-grade form *tn-u- in Germanic *thunw-, whence *thunniz in Old English thynne, thin: THIN. 2. Suffixed full-grade form *ten-u- in Latin tenuis, thin, rare, fine: TENUOUS; ATTENUATE, EXTENUATE. 3. Suf- fixed full-grade form *ten-ero- in Latin tener, tender, delicate: TENDER!, TENDRIL. III. Derivatives meaning “something stretched or capable of being stretched, a string.” 1. Suffixed form *ten-dn- in Greek tenén, ten- don: TENO-. 2. Suffixed o-grade form *ton-o- in Greek tonos, string, hence sound, pitch: TONE; TONOPLAST. 3. Suffixed zero-grade form *tn-ya- in Greek tainia, band, ribbon: TAENIA; POLYTENE. [Pok. 1. ten- 1065.] teng-. To soak. 1. Latin tingere, to moisten, soak, dye: TAINT, TINCT, TINGE, TINT; INTINCTION, STAIN. 2. Zero-grade form *tng- in Germanic *thunk- in Old High German thunk6n, dunk6n, to soak: punk. [Pok. 1. teng- 1067.] tenk-'. To stretch. Extension of ten-. Perhaps Germanic *thingam in: a. Old English thing, assembly, (legal) case, thing: THING; b. Old Norse thing, assembly: HUSTINGS; c. Old High German thing, ding (> German Ding), thing: DINGUS. [Pok. 1. tenk- 1067.] tenk-2, To become firm, curdle, thicken. 1. Suffixed form *tenk-to-, thickened, in Germanic *thinhtaz in Old Norse théttr, dense, watertight, akin to the Scandinavian source of Middle English thight, dense: TIGHT. 2. Possibly suffixed o-grade form *tonk-lo- in Germanic *thangul- in Old Norse théngull, seaweed (? < “thick mass”), akin to the source of TANGLE?. [Pok. 2. tenk- 1068.] tens-. To stretch, draw. Extension of ten-. Suffixed zero-grade form *tns-ero- in Sanskrit tasaram, shuttle: TussAH. [Pok. tens- 1068.] tep-. To be warm. Suffixed (stative) form *tep-é- in Latin tepére, to be warm: TEPID. [Pok. tep- 1069.] ter-. Base of derivatives meaning peg, post, boundary marker, goal. 1. Suffixed form *ter-men-, boundary marker, in Latin terminus, boundary, limit: TERM, TER- MINATE, TERMINUS; DETERMINE, EXTERMINATE. 2. Suf- fixed zero-grade form *tr-m- in Germanic *thrum- in Old English thrum, broken-off end (attested only in tungeth- rum, the ligament of the tongue): THRUM2. [Pok. 4. ter- 1074.] tera-1, To rub, turn; with some derivatives referring to twisting, boring, drilling, and piercing; and others refer- ring to the rubbing of cereal grain to remove the husks, and thence to the process of threshing either by the trampling of oxen or by flailing with flails. Variant *tré-, contracted from “*trea-. I. Full-grade form *ter@)-. 1. a. Latin terere (past participle tritus), to rub away,
2265:SITAR ten-, trei- SITH sé@-2 SITUATE tkei- situs tkei-
2336:TaaL del-2 TABES ta- TACET tak-1 TACHE dek-? TACHISM deik- TACHYLYTE leu-! TACHYPNEA pneu- TACIT tak-1 Tack! dek-2 TACT tag- TACTICS tag- TACTORECEPTOR tag- TAEL tele- TAENIA ten- TAFFETA temp- TAG! dek-2 TAHSILDAR dher-2 TAIL! dek-2 TAINT teng- Tad (s)teg- TAKE tak-2 TALE del-2 TALENT tela- TALES to- TALION tele- TALISMAN kWel-1 TALK del-2 TALLOW del-4 TAME deme-2 TAMPON tap- TANDEM to- TANG! denk- TANGENT tag- TANGIBLE tag- TANGLE? tenk-2 TANGORECEPTOR tag- TANSY dhwene- TANTALIZE tele- TANTALUS tele- TANTAMOUNT to- TANTRA ten- Tap! tap-
2338:TAPE tap- TAPESTRY temp-
17236:78 gmatanaty : atar :didim :frahajam : ðātiy : Dárayavaus : x3 
29586:frahajam 1st sg. imf. ($213) DB 2.78.
```


## [2026-10-15T02:51:10.911Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1077,1079p AHD_watkins1985.txt | cut -c1-700; grep -n \"^ *hanj-\\|hang-\\|hanj- \\|ahanj\" KNT_full.txt | head -5 | cut -c1-300; sed -n 29580,29590p KNT_full.txt | cut -c1-300; grep -n \"^tap-\\|TAPE\" AHD_watkins1985.txt | head -3; grep -n \"^ter-\\|teru\" AHD_watkins1985.txt|head -3",
 "description": "Read AHD temp- and Kent hanj-"
}
```


### [2026-10-15T02:51:11.298Z] TOOL RESULT

```
temp-
a. Latin téla, web, net, warp of a fabric, also weaver’s beam (to which the warp threads are tied): TILLER?, ToiL2; b. Latin subtilis, thin, fine, precise, subtle (< *sub-téla, “thread passing under the warp,” the finest thread; sub, under; see upo): SUBTLE. 3. Suffixed form *teks-On, weaver, maker of wattle for house walls, builder (possibly contaminated with *teks-tdr, builder), in Greek tekton, carpenter, builder: TECTONIC; ARCHITECT. 4. Suf- fixed form *teks-nd-, craft (of weaving or fabricating), in Greek tekhné, art, craft, skill: TECHNICAL, POLYTECHNIC, TECHNOLOGY. 5. Possibly Germanic *thahsu-, badger (“the animal that builds,” referring to its burrowing skill), in Old High German da
ten-

ha”j- vb. ‘hang’: Skt. safj- ‘fasten’, pres. 
зан. 
fra- + ha"j- ‘hang out’ for display (Foy, KZ 
35.39), namely the rebel’s skin, stuffed with straw 
(König, RuID 73-4; wrongly ‘imprison’, Sen 45): 
frahajam 1st sg. imf. ($213) DB 2.78. 


had- vb. ‘sit’: Av. had-, Skt. sad-, Lt. sedet, 
NEng. si. See also hadiš, and possibly 
1068:[tap-. Germanic base of various loosely related deriva- tives; “plug, wad, small compact object, projecting part; to plug, strike lightly.” Variants *tap-, *tapp-, *topp-, *tupp-. 1. Old English teppa, spigot: TAP. 2. Dutch tap, spigot: TATTOO!. 3. Old French tampon, plug: TAMPON. 4. Old French taper, to strike lightly: TAP!. 5. Old Eng- lish top, summit: ToP!. 6. Old English top, a child’s plaything, perhaps a spinning top: ToP?. 7. Old French toup, top, tuft of hair: TOUPEE. 8. Old Norse typpi (> Middle English tip), end: TIP!. 9. Old French tof(fe, tuft: TUFT. 10. Old English téppe, strip of cloth: TAPE.]
1080:warp threads are stretched on the loom): TAFFETA; b. Iranian *tap-, “carpet,” in Greek tapés, carpet: TAPES- TRY. [Pok. temp- 1064.] ten-. To stretch. I. Derivatives with the basic meaning. 1. Suffixed form “ten-do- in: a. Latin tendere, to stretch, extend: TEND!, TENDER?, TENDON, TENSE!, TENT!; AT- TEND, CONTEND, DETENT, DISTEND, EXTEND, INTEND, OSTENSIBLE, PRETEND, SUBTEND; b. Latin portendere, “to stretch out before” (por-, variant of pro-, before; see per’), a technical term in augury, “to indicate, presage, foretell”: PORTEND. 2. Suffixed form *ten-yo- in Greek teinein, to stretch: TENESMUS; BRONCHIECTASIS, EPITA- SIS, HYPOTENUSE, PERITONEUM, PROTASIS, TELANGIEC- TASIA. 3. Suffixed zero-grade form *tn-nu- in Sanskrit tandéti, he stretches or weaves, with suffixed (instrumen- tal) derivative *ten-tro- in tantam, loom: TANTRA. 4. Suf- fixed form *ten-tro- in Persian ¢tdr, string: SITAR. 5. Basic form (with stative suffix) *ten-é- in Latin ten��re, to hold, keep, maintain (< “to cause to endure or con- tinue, hold on to”): TENABLE, TENACIOUS, TENACULUM, TENANT, TENEMENT, TENET, TENON, TENOR, TENURE, TENUTO; ABSTAIN, CONTAIN, CONTINUE, DETAIN, ENTER- TAIN, LIEUTENANT, MAINTAIN, OBTAIN, PERTAIN, PERTI- NACIOUS, RETAIN, (RETINACULUM), SUSTAIN. II. Derivatives meaning ‘‘stretched,” hence “thin.” 1. Suffixed zero-grade form *tn-u- in Germanic *thunw-, whence *thunniz in Old English thynne, thin: THIN. 2. Suffixed full-grade form *ten-u- in Latin tenuis, thin, rare, fine: TENUOUS; ATTENUATE, EXTENUATE. 3. Suf- fixed full-grade form *ten-ero- in Latin tener, tender, delicate: TENDER!, TENDRIL. III. Derivatives meaning “something stretched or capable of being stretched, a string.” 1. Suffixed form *ten-dn- in Greek tenén, ten- don: TENO-. 2. Suffixed o-grade form *ton-o- in Greek tonos, string, hence sound, pitch: TONE; TONOPLAST. 3. Suffixed zero-grade form *tn-ya- in Greek tainia, band, ribbon: TAENIA; POLYTENE. [Pok. 1. ten- 1065.] teng-. To soak. 1. Latin tingere, to moisten, soak, dye: TAINT, TINCT, TINGE, TINT; INTINCTION, STAIN. 2. Zero-grade form *tng- in Germanic *thunk- in Old High German thunk6n, dunk6n, to soak: punk. [Pok. 1. teng- 1067.] tenk-'. To stretch. Extension of ten-. Perhaps Germanic *thingam in: a. Old English thing, assembly, (legal) case, thing: THING; b. Old Norse thing, assembly: HUSTINGS; c. Old High German thing, ding (> German Ding), thing: DINGUS. [Pok. 1. tenk- 1067.] tenk-2, To become firm, curdle, thicken. 1. Suffixed form *tenk-to-, thickened, in Germanic *thinhtaz in Old Norse théttr, dense, watertight, akin to the Scandinavian source of Middle English thight, dense: TIGHT. 2. Possibly suffixed o-grade form *tonk-lo- in Germanic *thangul- in Old Norse théngull, seaweed (? < “thick mass”), akin to the source of TANGLE?. [Pok. 2. tenk- 1068.] tens-. To stretch, draw. Extension of ten-. Suffixed zero-grade form *tns-ero- in Sanskrit tasaram, shuttle: TussAH. [Pok. tens- 1068.] tep-. To be warm. Suffixed (stative) form *tep-é- in Latin tepére, to be warm: TEPID. [Pok. tep- 1069.] ter-. Base of derivatives meaning peg, post, boundary marker, goal. 1. Suffixed form *ter-men-, boundary marker, in Latin terminus, boundary, limit: TERM, TER- MINATE, TERMINUS; DETERMINE, EXTERMINATE. 2. Suf- fixed zero-grade form *tr-m- in Germanic *thrum- in Old English thrum, broken-off end (attested only in tungeth- rum, the ligament of the tongue): THRUM2. [Pok. 4. ter- 1074.] tera-1, To rub, turn; with some derivatives referring to twisting, boring, drilling, and piercing; and others refer- ring to the rubbing of cereal grain to remove the husks, and thence to the process of threshing either by the trampling of oxen or by flailing with flails. Variant *tré-, contracted from “*trea-. I. Full-grade form *ter@)-. 1. a. Latin terere (past participle tritus), to rub away,
2338:TAPE tap- TAPESTRY temp-
425:eghs. Out. 1. Variant *eks in: a. Latin ex, ex-, out of, away from: EX!, Ex-; b. Greek ex, ek, out of, from: ECTO-, EXO-, EXOTERIC, EXOTIC; SYNECDOCHE. 2. Suffixed (com- parative) variant form *eks-tero- in Latin exterus, out- ward (feminine ablative extera, extra, on the outside): EXTERIOR, EXTERNAL, EXTRA-, STRANGE. 3. Suffixed (superlative) form in Latin extrémus, outermost (*-mo-, superlative suffix): EXTREME. 4. Suffixed form *eghs-ko- in Greek eskhatos, outermost, last: ESCHATOLOGY. [Pok. eghs 292.]
559:i-. Pronominal stem. 1. Germanic *is-lik-, same (*lik-, like; see lik-), in Old English ilca, same: ILK. 2. Germanic *jaino-, *jeno-, in Old English geon, that: Yon. 3. Ger- manic *jend- in Old English geond, as far as, yonder: YOND, (YONDER). 4. Extended forms *ydm, *ydi, in Ger- manic */d, *jai, in Old English géa, affirmative particle, and gése, yes (see es-): YEA, YES. 5. Old English giet, gieta (preform uncertain), still: yET. 6. Old English gif (preform uncertain), if: 1F. 7. Basic form *i-, with neuter *id-em, in Latin is, he (neuter id), and idem, same: 1D, IDEM, (IDENTICAL), IDENTITY; (IDENTIFY). 8. Suffixed form *i-tero- in Latin iterum, again: ITERATE; (REITER- ATE). 9. Suffixed and extended form ‘*iéa)-em in Latin item, thus, also: ITEM. 10. Suffixed variant form *e-tero- (see ko-). [Pok. 3. e- 281.]
642:h. Anglo-Norman aloper, to run away from one’s hus- band with a lover: ELOPE. kneigwh-. To lean on. 1. Latin cdnivére (< *con-niguére; com-, together; see kom), “to lean together” (said of eyelids), to close the eyes, be indulgent: CONNIVE. 2. Suf- fixed zero-grade form *knigvh-to- in Latin nictdre, to move the eyelids, wink: NICTITATE. 3. Uncertain preform in Latin niti, to lean forward, strive: NISUS; RENITENT. [Pok. knei-geh- 608.] knid-. Egg of a louse. Suffixed form *knid-d in Germanic *hnito in Old English hnitu, egg of a louse: NIT. [Pok. knid- 608.] ko-. Stem of demonstrative pronoun meaning “this.” I. Variant form *ki-. 1. Germanic *hi- in: a. Old English he, he: HE!; b. Old English him, him: HIM; c. Old English his, his: 1s; d. Old English hire, her: HER; e. Old English Ait, it: 1r. f. Old English hér, here: HERE; g. Old English heonane, heonon, from here: HENCE. 2. Suffixed form “ki-tro- in Germanic *hi-thra- in Old English hider, hither: HITHER. 3. Suffixed form *ki-s in Latin cis, on this side of: cis-. II. Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin céterus (neuter plural cétera), the other part, that which remains: ET CETERA. 2. Latin -ce (see nu-). III. Attrib- uted by some to this root (but more likely of obscure origin) is Germanic root *hind-, behind. 1. Old English bihindan, in the rear, behind (bi, at; see ambhi): BE- HIND, HIND!. 2. Old High German hintar (> German hinter-), behind: HINTERLAND. 3. Germanic derivative verb *hindron, to keep back, in Old English hindrian, to check, hinder: HINDER}. [Pok. ko- 609.] k6-. To sharpen, whet. Contracted from *koo-. 1. Suffixed extended form “kooi-no- in Germanic *haind in Old English hdn, stone: HONE!. 2. Perhaps Greek kénos, cone, conical object (< “a sharp-pointed object”): CONE. [Pok. Aéi- 541.] kob-. To suit, fit, succeed. Germanic *hap- in Old Norse happ, chance, good luck: HAP, (HAPPEN), (HAPPY); (HAP- LEss), (MISHAP). [Pok. kob- 610.] [kokkos. Kermes berry, pit, grain. Greek noun of un- known origin: COCCID, COCCUS, COCHINEAL; MONO- COQUE.] koksa. Body part. Latin coxa, hip: Coxa, CUISSE, CUSH- ION. [Pok. koksd 611.] kolem-. Grass, reed. Suffixed form *kolsm-o-. 1. Ger- manic “*halmaz in Old English healm, halm, straw: HAULM. 2. Latin cudmus, stalk: CULM!. 3. Zero-grade form “kibpm-o- in Greek kalamos, a reed, straw: CALA- MITE, CALAMUS, CALUMET, CARAMEL, SHAWM. [Pok. kolomo-s 612.] koli-. Glue. Suffixed variant form *koly-a in Greek kolla, glue: COLLAGE, COLLO-, COLLODION; PROTOCOL. [Pok. Rolfeji- 612.] kom. Beside, near, by, with. 1. Germanic *ga-, together, with (collective and intensive prefix and marker of the past participle), in Old English ge-, with, also participial, collective, and intensive prefix: ENOUGH, HANDIWORK, YCLEPT. 2. Latin cum, co-, with: CUM; CONQUIAN. 3. Old Latin com, with (collective and intensive prefix): co-, com-. 4, Suffixed form *kom-trd in Latin contra, against, opposite: (CON!), CONTRA-, CONTRARY, (COUNTER!), COUNTER-, COUNTRY; ENCOUNTER. 5. Suffixed form *kom-yo- in Greek koinos, common, shared: COENO-; CENOBITE, EPICENE, KOINE. 6. Reduced form *ko- (see gher-', mei-', smei-). [Pok. kom 612.] konemo-. Shinbone, bone, Reduced form *kemmo- per- haps in Germanic *hamma in Old English hamm, ham, thigh: HAM. [Pok. konamo- 613.] konk-. To hang. 1. Germanic *hanhan in: a. Old English hon, to hang: HANG; b. Dutch (dialectal) hankeren, to long for; HANKER; ¢C. possibly Middle English he(e)ng, hinge, hinge (ultimately from the base of Old English hangian, to hang): HINGE. 2. Suffixed form *konk-t-d- in
```


## [2026-10-15T02:51:17.363Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n \"tanïdan\\|tanidan\\|tantra\\|tänïdan\\|täftan\\|taftan\\|tauruna\\|ϑanǰ\\|danjay\\|Danjay\" WLD_Bd1_pages.txt | head -12 | cut -c1-200",
 "description": "Search Walde-Pokorny vol 1"
}
```


### [2026-10-15T02:51:17.711Z] TOOL RESULT

```
66541:taftan „niederdriicken“
66548:hitzt, qualt; ist warm, wird gequalt, leidet“, np. taftan „brennen, warmen,
66549:leuchten“ seien, ist besonders wegen np. taftan „niederdriieken“ nicht vor-
67770:tafnah- n. ,.Hitze, Glut; Fieber“; np. taftan „brennen, wiirmen. leuchten";
68088:   npers. tab-ad Inf. taftan und tab-t-dan „drehen, wenden. spinnen“, intr.
68214: tana, tanas- n. „Nachkommenschaft‘'; tantra-m „Zettel, Aufzug am Web-
```


## [2026-10-15T02:51:20.493Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 68080,68095p WLD_Bd1_pages.txt; sed -n 68210,68220p WLD_Bd1_pages.txt; for l in 68088 68214; do awk -v L=$l 'NR<=L' WLD_Bd1_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1; done; grep -n \"Tıvruna\\|tauruna\\|taurunas\\|taruna\" WLD_Bd1_pages.txt | head -3",
 "description": "Read WLD entries temp- and ten-"
}
```


### [2026-10-15T02:51:21.102Z] TOOL RESULT

```
spannung, Anstrengung 44 uibl. [tumpas „Ansatz zum Sprunge“), tampras
„zah, hartnackig, elastisch 44      lett. tdepties „hartnackig sein, sich auf etwas
                                                                          ;

                                               44
steifen 44 ; aksl. ta-jn „obtusus, crassus ?         Bed. dann etwa aus „gedunsen“,
s. zum Germ.), russ. mdartl. trpsti (eig. *tjapstl                  anziehen";
                                                          ) „straff
   npers. tab-ad Inf. taftan und tab-t-dan „drehen, wenden. spinnen“, intr.
                                   ,


                                      (aus einem zu *tap = idg. *tmp- analogisch
                                  4>
.,sich drehen, gequiilt werden
gebildeten Kaus. Hdpayati), wozu wohl als iran. Lw. (Schrader KZ. 30, 484,

 Nachkommenschaft", instr. tana „continuo“, tdna-li ,,Nachkomme“, tdna-m                                                ,


 tana, tanas- n. „Nachkommenschaft‘'; tantra-m „Zettel, Aufzug am Web-
 stuhl" = np. tar (av. *tadra-) ds. (weitere iran. Worte dieser Bed. „spinnen“
                                                                              ;          ;




68938:   Ai. taruna-h, gr. regv usw., s. u. Her- „zart“; gr. dzeig/js (pa-zegf-yg)
```


## [2026-10-15T02:51:23.726Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -c \"pdf page\" WLD_Bd1_pages.txt; awk 'NR<=68088' WLD_Bd1_pages.txt | tr -cd '\\f' | wc -c; awk 'NR<=68214' WLD_Bd1_pages.txt | tr -cd '\\f' | wc -c; awk 'NR<=68938' WLD_Bd1_pages.txt | tr -cd '\\f' | wc -c; sed -n 68936,68940p WLD_Bd1_pages.txt",
 "description": "Locate WLD leaves"
}
```


### [2026-10-15T02:51:24.159Z] TOOL RESULT

```
0
729
730
738
sehr ab.
  Wzform tereu- (J. Schmidt Yok. II 267 f.):
   Ai. taruna-h, gr. regv usw., s. u. Her- „zart“; gr. dzeig/js (pa-zegf-yg)
etwa „unverwfistlich“ s. Ehrlich KZ. 39, 570, Bechtel Lex. 72); zgvco, zgi
%co ,.reibe auf, erschopfe‘"', zegvoy.ezo heigezo Hes., xocoxm zgvyei [pyoatvei,
```


## [2026-10-15T02:51:28.635Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *ten[ōo]\\b\\|^tenō\\|^tenghō\\|^temp[ōo]\\|tantrom\\|tər[eu]nos\\|^teru\" IEC.txt | head -10 | cut -c1-250; grep -n -i \"tār\\b\\|tantra\" SYN.txt | head -5 | cut -c1-200",
 "description": "Search Mann and Buck"
}
```


### [2026-10-15T02:51:29.030Z] TOOL RESULT

```
18345:tempo (1), (tempt-) *feel, touch, grope' Lat. cf. tempto, are, v. & (late) tento, are, v. *feel, touch, try, attack; seize; harm; tempt'; Cz. tápu, tápám, inf. tápat, v. Cgrope', phonol. as for sahat ‘grab’, see sengh-); Slovak tapat; inf. ‘pat
18347:tempos, -es- “stretch; period’. Cf. tempo (2) and templom
```


## [2026-10-15T02:51:32.269Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 18340,18350p IEC.txt | cut -c1-400; grep -n \"^tenō\\|^tenō,\\|^tenō \\|^ten[oō] \\|^teno\\b\\|^tenk\\|^tenghō\\|^tenĝh\\|teng\" IEC.txt | head -8 | cut -c1-250; grep -n \"^te[rn][ue]n\\|^terun\\|^ter[eə]n\" IEC.txt | head | cut -c1-250",
 "description": "More Mann lookups"
}
```


### [2026-10-15T02:51:32.806Z] TOOL RESULT

```
1378
Lat. cf. templum, n. “court, recess, sacred plot if for *temlo- (?)
temnó ‘cut, lop’. (Variant: təm-, tm-). Cf. tmnó Attic témnó beside Ionic támno, v. id.; Lat. temnó, ére, v. ‘despise’. Semantics of therízo ‘cut’; a-therízo ‘despise’; ON sneiða, v. *cold- shoulder’: Ger. schneiden eut Osc. cf. per- temust “will inhibit’; -temum, inf.; Olr. ten- nim, tennaim & tamnaim, v. “cut off, lop’; Br. (denom.) tamma, inf. ‘cut, chop up’; OCS cf. tíno, teti, v. ‘cut off, lo
temos, -es- ‘darkness’; teminos, à ‘darkness; dark’. Cf. tem- (1), temoasros Skt. tamas, n. ‘darkness’; Av. tomo, obl. -áh-, n. id.; tomáha-, adj. ‘dark’; Tokh. tamàsse, adj. id.; Lat. cf. temero, are, v. ‘defile’; temere *rashly'; OHG (ambig.) démar, n. ‘dusk’; Olr. teime, f. ‘darkness’; Ir. teimhe and teimhne, f. id.; OS thimm, adj. ‘dark’; G dial. cf. dim- mer, dimber, id.; OCS and com. SI. tím
templom, à, io “stretch, extent, spread, ex- panse, space, period'. Cf. tempos & tempo (2) Lat. templum, n. *quarter of the sky; heaven; court; recess; sacred plot; temple); Mir & Ir. tamall, m. “space, period'; Li. temple, f. *bowstring, cord". Cf. WP I, 722
tempo (1), (tempt-) *feel, touch, grope' Lat. cf. tempto, are, v. & (late) tento, are, v. *feel, touch, try, attack; seize; harm; tempt'; Cz. tápu, tápám, inf. tápat, v. Cgrope', phonol. as for sahat ‘grab’, see sengh-); Slovak tapat; inf. ‘pat, paw’; Cz. dial, id.
tempó, io (2) ‘stretch, pul. Cf. templom, tempos Li. tempiù, tepti, v. (stretch, pull, drag’; Latv. tiepju, t, v. id. (and ‘stiffen, assert); (uncertainly Olr. timm, adj. ‘scant, slim’ and o-gde MHG demmen, v. ‘gorge oneself’, if fr. *tompeióo)
tempos, -es- “stretch; period’. Cf. tempo (2) and templom
1379
Lat. tempus, -óris (OLat. gs: -éris), n. ‘time’; Olr. timm, adj. ‘scant, slim’ (?); cf. tamall, m. (space, while’. See templom above); W cf. tafar, m. “spreading substance, spread”: Li. cf. tempiù, tempti, v. “stretch, tug, pull
ten- (1) “hither, here; thither, there'. Cf. te-, -tenos Tokh. B tane, tne “here, there’; Lat. cf. tenus “as far as’; quà-tenus, adv. “how far; so far”: Hes. cf. tënës ‘until; ON pinig ‘hither’; Li. teñ, tenai, tenais ‘there’; long-gde in Dor. tenei, id.
72:HOLTHAUSEN, F.: Altenglisches etymologisches Wörterbuch, 1934. 3. unveränderte Auflage Winter, Heidelberg 1974
2178:dengho, ið (1) ‘thrust, press, urge’. Cf. dongheið, donghis. WP I, 791 Olr. & Ir. dingim, id.; OE tingan, id. (o-gde in OE tenge 'close); OCS cf. degü ‘strap’; Li. déng, déngti “run, rush’; Latv. diedzu, id.
2388:dongheió ‘press, press on, hasten’. Cf. dengho and next. Arm. tangem ‘torture’; OE tengan “press to- wards, assail'; ON tengja ‘tie’; Pol. dążyć
2391:donghis, ios ‘pressing; pressure, haste’. Cf. dengh-, dongheio Arm. (pl. form) tan£ék (i-st. "torturei Ir. daingean ‘firm’; OHG gi-zengi ‘touching, reaching’; OS bi-tengi, id.; OE tenge, prp. "Close beside tang, id.; tenge, adj. “oppres- sive’; 
3006:dhongheio ‘bang? Cf. dhenguho, dhengh-, dhngh- Oss. cf. dáng! 'bang'!; ON dengja; Sw. dänga, Norw. denge (“beat, hammer, sharpen by ham- mering’, etc.); cf. MHG tengeln “hammer”
17186:stembo, ið (sth-) ‘press, force’. Cf. stenguó. (Gk. ambig.). WP II, 623 Per. cf. sitam, s. ‘oppression’; sitam-dide, pp. ‘oppressed’; Gk. (ambig.) stémbo, v. ‘stamp; insult’; Icel. stimpast, refl. ‘tug at; Li. stem- biù, “ti, v. ‘oppose, resist
17189:(stengh-, ambig. for Lith. forms, see stenguo, but cf. ON stinga, sv. 3. w. dat. 'thrust'; stingi, m. ‘stitch in the side")
17190:stenguo (sth-) ‘thrust, push, press, jostle’. Cf. stembo. (Gk. ambig.). WP II, 613 Gk. (ambig.) stémbo, v. ((trample; buffet, browbeat’, but cf. stemb-); Lat. cf. ex-stinguo, ére, v. beside OLat. stingo & stinguo 'extin- guish"; Go. stigqan, sv
18414:teren- (terun-, tern-) “weak, tender’. WP I, 728 Skt. tárunah “young, tender, fresh'; talinah ‘slender’; cf. tarnakah, m. “young animal’; Romani terno, tarno ‘young’; Av. tauruno, id.; Per. tar ‘moist, fresh’; Oss. tärna, tárín, tírín, s. ‘boy’
```


## [2026-10-15T02:51:36.396Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ten-\\|^tenō\\|^tenó\\|^tentrom\\|^tntrom\\|^ton[oó]s\" IEC.txt | head | cut -c1-300; grep -n \"Per\\. t[aā]r\\b\\|Per\\. tār\\|tanidan\\|tanīdan\" IEC.txt | head -5 | cut -c1-300",
 "description": "Find Mann ten- entries"
}
```


### [2026-10-15T02:51:36.764Z] TOOL RESULT

```
18350:ten- (1) “hither, here; thither, there'. Cf. te-, -tenos Tokh. B tane, tne “here, there’; Lat. cf. tenus “as far as’; quà-tenus, adv. “how far; so far”: Hes. cf. tënës ‘until; ON pinig ‘hither’; Li. teñ, tenai, tenais ‘there’; long-gde in Dor. tenei, id.
18351:ten- (2) radical: ‘stretch; spread; thin’. Cf. teneuos, tend (1), ton-, tnu- Long-gde in Skt. tànah, m. ‘fibre’; tanavam, n. ‘thinness’; Srb. tjena, f. ‘membrane’; Latv. tena, f. id.; Latv. cf. also tievs ((thin', cf. tnui-)
18352:ten- (3) ‘stiff, hard; harden, grip’. See tend (2)
18356:ten- — tenk-
18776:tonos, à, us, u, io 'stretch, bulge'. Cf. ten- (2) and extns., ton-, tn- Skt. tanuh, üh, mf. “body, person'; Av. tanus, tanu, f. & n. ‘belly’; Ober, tanus ‘body’; Per. tan, id.; tane,s. 'treetrunk; web’; Oss. tàn, s. ‘hip, thigh; side; string of instrument’; Gk. tónos, m. “tension, tone, cable
18414:teren- (terun-, tern-) “weak, tender’. WP I, 728 Skt. tárunah “young, tender, fresh'; talinah ‘slender’; cf. tarnakah, m. “young animal’; Romani terno, tarno ‘young’; Av. tauruno, id.; Per. tar ‘moist, fresh’; Oss. tärna, tárín, tírín, s. ‘boy’; Gk. téren, gs: -enos ‘smooth, tender, soft, deli
```


## [2026-10-15T02:51:40.871Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^SITAR\\|sitar, s\\|SITTAR\\|setar\" HJB.txt | head -5 | cut -c1-400; grep -n -i \"sitar\\|sitär\" AID.txt | head -3 | cut -c1-300; grep -n -i \"gitar\\|guitarre\\|guitare\" DEV.txt LKT.txt PHN.txt DOZ.txt | head -8 | cut -c1-300",
 "description": "Search Hobson-Jobson and Arabism books"
}
```


### [2026-10-15T02:51:41.389Z] TOOL RESULT

```
8301:1772. — "Suppose  every  farmer  in  the pirovince  was  enjoined  to  maintain  a  num- ber of  good  serviceable  bullocks  .  .  . obliged  to  furnish  the  Government  with them  on  a  requisition  made  to  him  by  the Collector  in  writing  (not  by  sepoya,  delects {sic),  or  hercarras^'  (see  bUBCfAB&A).- »r.  ffailings,  to  G.  Vansittart,  in  GMg,  i.  237.
9210:1768.— "The  digni^  and  benefit  of  mur DiuifeiickB  are  the  chief  baiteeB  of  hoooiir, or  at  least  interest,  we  enjoy  from  our  Phir- maatsMf." — From  the  Chief  apd  Council  at Dacca,  in  Van  Sittart,  L  210.
9914:1762. — "A  co£fre  who  oommanded  the Telingaa  and  Qardeee  .  .  .  asked  the  horse- man whom  the  horse  belonged  to  ?  *'^Naiive Letter,  in  Van  Sittart,  i.  141.
10356:1762.— "You  will  direct  the  gentleman, Qomastahs,  Muttatvddies  (see  MOOT- BUDDY),  and  Moonthiei,  and  other  officers of  the  English  Company  to  relinquish  their farms,  taalues  (see  TALOOE),  gonges,  and golaluk"- 7A«  Nabob  to  the  Gofvemor,  in  Vaai Sittarty  i.  229.
11469:IMPALE,  V.  It  is  startling  to  find an  injunction  to  impale  criminals  given by  an  English  governor  (Vansittart, apparently)  little  more  than  a  century ago.    [See  CALUETE.]
PHN.txt:9737:ne s'applique , chez les Orientaux , qu'à une espèce de guitare à
PHN.txt:9740:passant, que celui qui joue de cette guitare s'appelle en arabe
```


## [2026-10-15T02:51:44.702Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"kithar\\|cithar\\|qît\\|qit[aâ]r\\|kîtâr\\|guitar\" DEV.txt LKT.txt DOZ.txt LAM.txt AFA.txt | head -10 | cut -c1-300; grep -n -i \"taffet\\|tafta\\|tâfta\" DEV.txt LKT.txt PHN.txt | head -5 | cut -c1-300",
 "description": "Search Arabism books for guitar/taffeta"
}
```


### [2026-10-15T02:51:45.102Z] TOOL RESULT

```
LAM.txt:6974:lyre (2), guitare, ou mandoline, comme traduit M. Bar-
DEV.txt:1150:CiNNOR  ou  KiNNOR.  Instrument  de  musique  chez  les  Hé- breux. Transcription  de  l'hébreu  li^D  kinnôr,  qu'on  inter- prète par  le  latin  cithara,
PHN.txt:9480:tabby en anglais), qui désigne un gros taffetas onde, tantôt
DEV.txt:2168:Taffetas.  C'est  sans  doute  le  persan  *aX>  iajïah  ou  lej- teh,  même  signification,  comme  l'indiquait,  il  y  a  près  de deux  cents  ans,  le  P.  Ange  de  Saint-Joseph^;  à  moins  que ce  ne  soit  une  simple  onomatopée,  reproduisant  le  bruit produit  par  le  taff
DEV.txt:4386:Taffetas.
DEV.txt:4704:xxjb'  pers.  voy.  Taffetas.
LKT.txt:3659:N.  pr.,  Name  einer  auf  einer  Insel  am Eingang  zum  pers.  Meerbusen  gelegenen blühenden  Handelsstadt  [bei  den  Alten (Ptolemaeus)  "ApiaouZa,  Hormozia;  vgl. auch  MP  99/104  und  504  sowie  v. Oppen- heim, Vom  Miltelmeer  zum  pers.  Golf II,  320  und  336];  nach  ihr
```


## [2026-10-15T02:51:51.476Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; python3 -c \"\nt=open('24b0a25c595f14af.txt').read().replace('\\n',' ');i=t.find('Etymology');print(t[i:i+500])\"",
 "description": "Check تابیدن Wiktionary text"
}
```


### [2026-10-15T02:51:51.905Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:55:59.914Z] TOOL CALL #87: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-501.json",
 "content": "{\n  \"pdf_page\": 501,\n  \"book_page\": 471,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-14\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ten 1, Tengh, Temp\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ten- 'to stretch' (Pokorny 1. ten- 1065-1066; LIV 626 f.), with the enlargements *tengʰ- 'to pull, draw' (Pokorny 1067; Cheung *θanǰ) and *temp- 'to stretch' (Pokorny 1064; Watkins temp-)\",\n      \"note\": \"The root box is correct: Pokorny p.1064 has 'temp- to extend, stretch, span; Note: extension from *ten-', p.1067 'tengh- to extend, stretch, span; Aryan *thengh-, yet probably extension from ten-1', and pp.1065-1066 the base '1. ten-, tend- to extend, stretch'. Nourai's citation POK:1064,1067 covers the two enlargements; the base is on p.1065. Watkins (AHD) lists ten- and temp- with exactly Nourai's English outcomes (SITAR under ten-, TAFFETA and TAPESTRY under temp-). Problems lie in individual branches: (1) Av. tauruna- 'young' (#8) belongs to a different root, PIE *ter-/teru- 'tender, weak' (Pokorny 1070-1071, Mann teren-, Klein s.v. tender), so the tar/tarāneh/tūleh/tūrah branch does not belong under Ten; (2) Greek kithara (#14) is not from Persian tār/si-tār — it is a Pre-Greek word attested from Homer (kitharis), centuries before the Persian si-tār, although Klein (whom Nourai follows) writes 'Gk. kithara, fr. Pers. sihtār'; (3) English tape is a native Old English word (tæppe), not from the Persian/Greek carpet word; (4) Persian tābīdan 'twist' comes from the *temp- enlargement (Iranian *tāp-), not from Av. tan- as drawn; (5) hanjār 'path, norm' has no secure link to *θanǰ (Wiktionary: from Parthian anjār 'behaviour'; Mo'in compares Skt saṃcāra). The Avestan 'tathra' and 'thri-thatra' are not attested: the first is the reconstructed *tąθra- of Horn and Pokorny, the second appears to be Nourai's own back-projection of si-tār. The JSON matches the printed page (checked against the page image), including the inconsistent spellings tathra / thri-thatra and the reference 'KLN:572', which is a misprint in the book for KLN:1572 (tapestry). No extraction errors.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ten- «کشیدن، کش دادن» (پوکورنی ۱۰۶۵–۱۰۶۶) و دو گونهٔ گسترش‌یافتهٔ آن، *tengʰ- «کشیدن، بیرون کشیدن» (پوکورنی ۱۰۶۷) و *temp- «کش دادن» (پوکورنی ۱۰۶۴)، درست آمده است و واتکینز نیز همین سه را با sitar و taffeta و tapestry آورده است؛ پس سرریشهٔ نورایی درست است. ایراد در چند شاخه است: «تئوروونه» (tauruna) اوستایی به معنای «جوان» از ریشهٔ دیگری (*ter- / *teru- «نرم، نازک») است، نه از *ten-؛ «کیثارا»ی یونانی از «سه‌تار» فارسی نیست و پژوهش امروزی آن را واژه‌ای پیشایونانی می‌داند؛ tape انگلیسی واژه‌ای بومی است؛ «تابیدن» از ستاک ایرانی *tāp- (گونهٔ *temp-) است نه از tan- اوستایی؛ و پیوند «هنجار» با *θanǰ ثابت نیست. «tathra» و «thri-thatra» در اوستا گواهی نشده‌اند و بازسازی (یا ساختهٔ خود نورایی) است. خطای استخراج دیده نشد؛ «KLN:572» در خود کتاب چاپ شده و خطای چاپی به جای ۱۵۷۲ است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ten-\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tengʰ-\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/temp-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1064\", \"status\": \"supports\", \"note\": \"POK_full.txt line 85474 ff. (Page(s): 1064-1065), 'Root / lemma: temp- Meaning: to extend, stretch, span; Note: extension from *ten- ds.; Material: Npers. tāb-ad, Inf. tāftan and tāb-ī-dan \\\"drehen, spinnen\\\" ... (from one to *tap = Indo Germanic *tmp- ...), wherefore probably as Iran. loanword gr. tapēs, tapis \\\"cover, rug\\\"'.\"},\n        {\"ref\": \"POK:1067\", \"status\": \"supports\", \"note\": \"POK_full.txt line 85513 ff. (Page(s): 1067), 'Root / lemma: tengh- Meaning: to extend, stretch, span; Note: Aryan *thengh-, yet probably nevertheless extension from ten-1; Material: Avestan θang- (θanjasante, θanjayente, participle θaxta-) \\\"ziehen, Bogen spannen\\\"'. The base 1. ten- itself is on pp.1065-1066 (line 85746), not cited by Nourai but consistent.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I pp.~721-725 (WLD_Bd1_pages.txt leaves 729-730)\", \"stance\": \"supports\", \"note\": \"temp-: 'npers. tāb-ad Inf. tāftan und tāb-ī-dan \\\"drehen, wenden, spinnen\\\" ... (aus einem zu *tap = idg. *tmp- analogisch gebildeten Kaus. *tāpayati), wozu wohl als iran. Lw. ...'; ten-: 'tantra-m \\\"Zettel, Aufzug am Webstuhl\\\" = np. tār (av. *taθra-) ds.' (grep 'tab-ad', 'tantra').\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, roots temp- and ten- (AHD_watkins1985.txt line 1079-1080)\", \"stance\": \"supports\", \"note\": \"temp-: '... TAFFETA; b. Iranian *tap-, \\\"carpet,\\\" in Greek tapēs, carpet: TAPESTRY. [Pok. temp- 1064.]'; ten-: '4. Suffixed form *ten-tro- in Persian tār, string: SITAR ... [Pok. 1. ten- 1065.]'.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann col. ~1378-1379, s.v. ten- (2), tempó (2)\", \"stance\": \"supports\", \"note\": \"'ten- (2) radical: \\\"stretch; spread; thin\\\"'; 'tempó (2) \\\"stretch, pull\\\" ... Li. tempiù, tępti \\\"stretch, pull, drag\\\"'. Mann files Av. tauruna- under a separate 'teren- (terun-) \\\"weak, tender\\\"'.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"pp. 377-392, s.vv. *tan, *tap 'to twist, wind', *θanǰ\", \"stance\": \"supports\", \"note\": \"*tan 'to extend, stretch' '<PIE *ten- ... Pok.: 1065 f.'; *tap 'to twist, wind' '<PIE (?) *temp- ... Pok.: 1064 f.'; *θanǰ 'to pull, draw' '<PIE *tengʰ- ... *tengʰ- is clearly an enlarged root of *ten- (*tan) ... Pok.: 1067'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"thang, â-thax, hanč; far-thang\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Young Avestan θang- / θanj- 'to pull, draw (a chariot), draw (a sword), draw (a bow)' (Bartholomae col. 785-786; pres. θanjaya-, ppp. θaxta-; with fra- 'to drive forward', fraθanjayeiti Yt 17.2) is the regular Iranian reflex of PIE *tengʰ- (Iranian *θanǰ-, with the unexplained θ- discussed by Cheung). 'â-thax' corresponds to the ā-prefixed participle *ā-θaxta- underlying MP āhixt (not itself attested in Avestan), and 'far-thang' to fra-θanj-, which in Avestan means 'drive forward'; the sense 'educate' belongs to MP frahanj-/frahixtan and NP farhang. 'hanč' is not Avestan: it is the Old/Middle Persian development *θ > h (MP hanj-, Kent's OP ha(n)j- in frāhajam, which Kent however derives from a different verb 'hang'). The core claim (Av. θang- 'pull') is confirmed; the extra forms are reconstructed or belong to later Persian, hence 'plausible'.\",\n          \"derivation_fa\": \"فعل اوستایی θang- / θanj- به معنای «کشیدن (گردونه، شمشیر، کمان)» در فرهنگ بارتولمه (ستون ۷۸۵–۷۸۶) گواهی شده و با پیشوند fra- به معنای «پیش راندن» است؛ چونگ آن را از ایرانی *θanǰ- و هندواروپایی *tengʰ- (گونهٔ گسترش‌یافتهٔ *ten-) می‌داند. ولی «â-thax» صورت بازسازی‌شدهٔ *ā-θaxta- است و «hanč» اوستایی نیست بلکه صورت پارسی/فارسی میانه (hanj-) است که در آن θ ایرانی به h بدل شده؛ معنای «آموزش» نیز از فارسی میانهٔ frahang است. اصل ادعای نورایی درست است، ولی برچسب «اوستایی» برای همهٔ صورت‌ها دقیق نیست؛ با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tengʰ-\",\n            \"https://en.wiktionary.org/wiki/آهیختن\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2381\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:2381 (vol.4 pdf p.464), s.v. هنگ, Mo'in quotes Pur-Davud: 'دراوستا فعل تهنگه (θang) بمعنی کشیدن بسیار بکار رفته وازین مصدر (ریشه) چندین واژه درفارسی بجا مانده؛ ازآنهاست: هنگ (= آهنگ)، هنجیدن، با پیشاوند ā آهنجیدن ... هختن (= هیختن)، با پیشاوند ā آهختن (= آهیختن)، با پیشاوند فر فرهختن، باپیشاوند بر برهیختن، باپیشاوند فرو فروهختن'.\"},\n            {\"ref\": \"BQT:2376\", \"status\": \"supports\", \"note\": \"BQT_v4_pages.txt [pdf page 459] = printed 2376, s.v. هنج fn.: 'ریشهٔ اوستایی θang (کشیدن) بارتولمه ۷۸۶. از همین ریشه است: آهنج (آهنجیدن)، آهیختن، فرهنگ'.\"},\n            {\"ref\": \"BQT:1481\", \"status\": \"partial\", \"note\": \"ref_page.py BQT:1481 (vol.3 pdf p.274) s.v. فرهنگ / فرهیختن: 'فرهیختن بروزن انگیختن، بمعنی ادب آموختن ... فرهختن درست مطابق است درمفهوم با educere و educare لاتینی بمعنی کشیدن ... در پهلوی frahixtan'. Confirms the 'pull' > 'educate' sense, but this page does not itself name Av. θang-.\"},\n            {\"ref\": \"SNS:7\", \"status\": \"partial\", \"note\": \"SNS_pages.txt index (OCR poor): 'ahanjišn 7/2', '-hanc 7/3' — p.7 of Tavoosi's glossary has MP āhanjišn 'drawing' (the Avestan-Pahlavi pair), consistent with Nourai; the page text itself is not legible in the OCR.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 785-786 s.v. θang-\", \"stance\": \"supports\", \"note\": \"BRT.txt line 14259: '• j. θang- V. \\\"ziehen\\\". Praes. 14b (Inkoh.) θaxšaiti?, 30 (Iter.) θanjaya-. — PPfP. θaxta- ... 4) \\\"(das Schwert, den Dolch) zücken\\\" ... 5) \\\"(den Pfeil) anziehen, (den Bogen) spannen\\\" ... mit fra \\\"heranfahren\\\" ... np. āhanjīdan \\\"ziehen\\\"; l. Hbm. PSt. 10'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"pp. 391-392 s.v. *θanǰ\", \"stance\": \"supports\", \"note\": \"'*θanǰ \\\"to pull, draw\\\" AVESTAN: YAv. θanj- \\\"to pull, draw\\\" || (+ *fra-) \\\"to drive to\\\" ... MIDDLE PERSIAN: BMP hnc- /hanj-/ \\\"to draw (water)\\\" ... (+ *fra-) BMP frahanj- \\\"to educate\\\" ... PIE *tengʰ- \\\"to draw, pull back\\\"'.\"},\n            {\"src\": \"KNT\", \"where\": \"Lexicon s.v. ha(n)j- (KNT_full.txt line 29580)\", \"stance\": \"partial\", \"note\": \"'hanj- vb. \\\"hang\\\": Skt. sañj- \\\"fasten\\\" ... fra- + hanj- \\\"hang out\\\" for display ... frāhajam DB 2.78' — Kent does not connect the OP verb with Av. θang-, against Horn's 'ap. hanj-' (HRN no. 58).\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"hanjîdan; hanjâr; âhang; farhîxtan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"hanjīdan/āhanjīdan 'to pull, draw out' continue MP (ā)hanj- [hnc-, ʾhnc-] < Ir. *(ā-)θanǰaya- (Cheung *θanǰ; Horn no. 58); āhang 'pull, draught' > 'intention, purpose' (later 'melody') is MP āhang [ʾhng] 'pull, draught' (MacKenzie), a deverbal noun of the same verb with ā-; farhīxtan 'to educate' is MP frahixtan/frahanj- 'educate' < *fra-θanǰ- 'draw forth' (cf. Latin educare/educere for the same semantic path), and farhang 'education, culture' is MP frahang [plhng] (Nyberg, MacKenzie; Arm. loan hrahang). Iranian *θ > MP/NP h regularly in Persian proper. hanjār 'path, manner, norm' is the weak point: Wiktionary derives it from MP hanjār < Parthian ʾnjʾr (anjār) 'behaviour' without linking it to *θanǰ, and Mo'in (BQT 2376 fn.) compares Skt saṃcāra- 'going about, path' (*ham-čāra-), i.e. a different root; Horn and Cheung do not list it under *θanǰ. Three of the four words are confirmed; hanjār is at best uncertain.\",\n          \"derivation_fa\": \"«هنجیدن / آهنجیدن» (کشیدن، بیرون کشیدن) از فارسی میانهٔ (ā)hanj- و آن از ایرانی باستان *θanǰaya- است؛ θ ایرانی در فارسی به «ه» بدل شده است. «آهنگ» از فارسی میانهٔ āhang «کشش» و سپس «قصد، آهنگ کاری» است، و «فرهیختن» و «فرهنگ» از فارسی میانهٔ frahixtan / frahang از *fra-θanǰ- «بیرون کشیدن، پروردن» (همانند educare لاتینی) آمده‌اند؛ هرن، نیبرگ، مکنزی و چونگ همه این را تأیید می‌کنند. اما «هنجار» را ویکی‌واژه از پارتی anjār «رفتار» می‌داند و معین در حاشیهٔ برهان آن را با سنسکریت saṃcāra «گردش، راه» سنجیده است؛ پس پیوند آن با این ریشه ثابت نیست. ادعای نورایی برای سه واژه درست و برای «هنجار» با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/فرهنگ\",\n            \"https://en.wiktionary.org/wiki/آهنگ\",\n            \"https://en.wiktionary.org/wiki/هنجار\",\n            \"https://en.wiktionary.org/wiki/آهیختن\",\n            \"https://abadis.ir/fatofa/هنجار/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:14\", \"status\": \"supports\", \"note\": \"Horn no. 58 (HRN.txt line 950-973, leaf 36 = pp.14-15): 'āhenjīden \\\"ziehen, herausziehen\\\", vergl. āhīxten (āhexten) ... phlv. ahanjītan \\\"ziehen, fortziehen\\\" ... Np. āheng \\\"Plan, Absicht\\\" wird ebenfalls hierhergehören. Desgleichen np. ferhexten, ferhīxten ... \\\"erziehen\\\"; vergl. ferheng, ferhenj \\\"Wissen etc.\\\" (phlv. frahang ...; arm. LW. hrahang)'. hanjār not mentioned.\"},\n            {\"ref\": \"BQT:70\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 280 (= p.70) s.v. آهنگ, Mo'in fn.: 'آهنگ، آهنگیدن، هنجیدن، آهیختن هم‌ریشه‌اند. از ریشهٔ اوستائی θang بمعنی کشیدن «بارتولمه ۷۸۵»'.\"},\n            {\"ref\": \"BQT:2381\", \"status\": \"supports\", \"note\": \"s.v. هنگ (ref_page.py BQT:2381): Pur-Davud's list 'هنگ (= آهنگ)، هنجیدن، ... آهنجیدن ... فرهختن ...' from Av. θang 'کشیدن'. Does not include هنجار.\"},\n            {\"ref\": \"BQT:2376\", \"status\": \"contradicts\", \"note\": \"For hanjār only: BQT_v4_pages.txt [pdf 459] s.v. هنجار, Mo'in's fn.: 'درسانسکریت saṃcāra (گشتن، گردیدن، راه) «اسشق ۱۱۶۹»' — a different etymology from θang (quoted also by Dehkhoda on abadis: 'در سنسکریت سمکارا به معنی گشتن و گردیدن و راه است (حاشیه برهان چ معین)').\"},\n            {\"ref\": \"SNS:126\", \"status\": \"partial\", \"note\": \"SNS index: 'frahang 126/1' — Tavoosi p.126 treats MP frahang; page OCR illegible, so only the headword is confirmed.\"},\n            {\"ref\": \"FFD:28\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Fe'l-ha-ye Farsi-ye Dari: PDF listed in refs_online.json but not consulted for this page.\"},\n            {\"ref\": \"MON\", \"status\": \"not_checked\", \"note\": \"No page given; Mo'in's lexicon tags are visible online but carry no Avestan forms.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 4, 33 (PHD_mackenzie.txt lines 931-938, 2295-2301)\", \"stance\": \"supports\", \"note\": \"'āhang [ʾhng] pull, draught'; 'āhanjīdan [ʾhncytn] = āhixtan'; 'āhixtan, āhanj- [ʾhhtn, ʾhnc- | M ʾhxtn, ʾhynz-, N āhixtan] draw'; 'frahang [plhng | N farhang] education; knowledge'; 'frahixtan, frahanj- [plhhtn, plʾhnc- | P frhynj-, N far-] educate, teach, instruct'. No *hanjār.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II pp. 4, 76, 92 (NYB_vol2_glossary.txt lines 298, 1506, 1514, 1968)\", \"stance\": \"supports\", \"note\": \"'frahaxtan ... to educate ... Pres. frahanj- ... NP farhaxtan, farhanjidan. From fra + Av. (784 sq.) θang- \\\"to draw\\\"'; 'haxtan ... to pull ... Av. θang-. The pres. āhanj- and hanj- belong to this root'; 'frahang [plhʾng] education, breeding'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 392 s.v. *θanǰ (NWIr.)\", \"stance\": \"supports\", \"note\": \"'(+ *ā-) NP āhixtam/āhiz- \\\"to draw (a sword)\\\", NP āhanjidan/āhanj- (caus.) \\\"to drink; to drag; to fling\\\" ... (+ *fra-) NP farhang \\\"culture, education; dictionary\\\"'. hanjār absent.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.10 (cited by Bartholomae col. 786 'Hbm. PSt. 10')\", \"stance\": \"supports\", \"note\": \"Bartholomae's entry for θang- refers to Hübschmann PSt 10 for np. āhanjīdan; not re-read in HUB.txt here.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"âhîxtan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP āhīxtan (Classical āhēxtan), pres. āhanj-, 'to draw out (a sword), pull up' < MP āhixtan/āhanj- [ʾhhtn, ʾhnc-], Manichaean ʾhxt/ʾhynz- < Ir. *ā-θixta-/*ā-θanǰaya- (Cheung *θanǰ with ā-). The past stem -hixt- shows the zero grade *θiǰ-ta- > *θixta- with MP θ > h; the present -hanj- keeps the nasal. The 'extra' forms hīxtan (MP hixtan 'draw water'), barhīxtan (bar- 'up') and forūhīxtan (forū- 'down') are the same verb with other preverbs, all listed by Pur-Davud/Mo'in (BQT 2381). Nāṣer-e Khosrow's 'barun-āhixad az del bix-e kin' ('draws the root of hatred out of the heart') shows the literal sense.\",\n          \"derivation_fa\": \"«آهیختن» (آهختن، با ستاک حال «آهنج») به معنای «بیرون کشیدن (شمشیر)، برکشیدن» از فارسی میانهٔ āhixtan / āhanj- و آن از ایرانی باستان *ā-θanǰ- (پیشوند ā + *θanǰ «کشیدن») است؛ ستاک گذشته -hixt- صورت ضعیف ریشه است و θ ایرانی در فارسی میانه به h رسیده است. «هیختن»، «برهیختن» و «فروهیختن» همان فعل با پیشوندهای دیگرند و معین و پورداود همه را هم‌ریشه شمرده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/آهیختن\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:14\", \"status\": \"supports\", \"note\": \"Horn no. 58: 'āhenjīden \\\"ziehen, herausziehen\\\", vergl. āhīxten (āhexten) ... phlv. ahanjītan \\\"ziehen, fortziehen\\\"; vergl. hīxtan ... berhexten, berhīxten \\\"ziehen, herausziehen\\\"'.\"},\n            {\"ref\": \"BQT:70\", \"status\": \"supports\", \"note\": \"BQT vol.1 p.70 (leaf 280) fn.: 'آهنگ، آهنگیدن، هنجیدن، آهیختن همریشه‌اند. از ریشهٔ اوستائی θang بمعنی کشیدن «بارتولمه ۷۸۵»'.\"},\n            {\"ref\": \"BQT:2381\", \"status\": \"supports\", \"note\": \"'هختن (= هیختن)، با پیشاوند ā آهختن (= آهیختن) ... باپیشاوند بر برهیختن، باپیشاوند فرو فروهختن' — exactly the four forms of Nourai's box.\"},\n            {\"ref\": \"SNS:126\", \"status\": \"not_found\", \"note\": \"SNS index lists only frahang at 126/1; no āhixtan entry located (OCR poor).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 4 (line 938)\", \"stance\": \"supports\", \"note\": \"'āhixtan, āhanj- [ʾhhtn, ʾhnc- | M ʾhxtn, ʾhynz-, N āhixtan] draw'; p.40 'hixtan, hanj- [hyhtn, hnc- | P hxt] draw (water)'.\"},\n            {\"src\": \"NYB\", \"where\": \"II p.4 s.v. āhanj-, p.97 s.v. hixtan\", \"stance\": \"supports\", \"note\": \"'āhanj- [ʾhnc-] pres., to draw up (water) ... MPrs pt. ʾhxt, pres. ʾhynz- ... NP āhixtan āhanj-. Alternates in the same context with the simplex vb. hixtan hanj-'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 391-392 s.v. *θanǰ\", \"stance\": \"supports\", \"note\": \"'BMP ʾhht /āhixt/ ... NP āhixtan/āhanj- ... (+ *ā-) MMP ʾhynz- \\\"to pull, draw up, tow\\\"'.\"},\n            {\"src\": \"BRT\", \"where\": \"col. 786\", \"stance\": \"supports\", \"note\": \"'np. āhanjīdan \\\"ziehen\\\"' under θang-.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"tan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan tan- 'to stretch, extend' (Bartholomae col. ~632: 'tan- V. \\\"dehnen, recken\\\"; nur mit Praev.', pres. tanav-/tanu-; us.tāna- 'stretched out (hands)', pairi.tan- 'keep away') = Skt tanóti, Gk teínō, from PIE *ten- (zero grade *tn̥-néw- > Ir. *tanu-). Its MP and NP continuants are tadan/tan- 'to spin' and tanīdan 'to spin, weave' (Cheung *tan). Nourai's gloss 'to pull, stretch' is correct.\",\n          \"derivation_fa\": \"فعل اوستایی tan- «کش دادن، گستردن» (بارتولمه، ستون ۶۳۲؛ تنها با پیشوند، مانند us.tāna- «گشاده (دست)») هم‌ریشه با سنسکریت tanóti و یونانی teínō و از هندواروپایی *ten- است؛ دنبالهٔ آن در فارسی میانه tadan / tan- «رشتن» و در فارسی «تنیدن» است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ten-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SNS:147\", \"status\": \"not_found\", \"note\": \"SNS index lines checked for '147/': only 'tuhīg 147/1' and 'skast 147/4-9'; no tan- entry on p.147 identified (OCR poor; tan appears at 152/17).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. ~632 s.v. tan- (BRT.txt line 11936)\", \"stance\": \"supports\", \"note\": \"'• j., g. tan- V. \\\"dehnen, recken\\\"; nur mit Praev. Praes. 10 tanav-: tanv- ... mit us \\\"ausrecken, ausstrecken\\\": ustānaiš zastaiš ... ai. tanōti, uttānáḥ; np. tanīdan \\\"spinnen\\\"'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 377 s.v. *tan\", \"stance\": \"supports\", \"note\": \"'*tan \\\"to extend, stretch\\\" AVESTAN: (+ *pari-) YAv. pairi.tan- ... MIDDLE PERSIAN: BMP tn- /tan-/, (pret. stem) tt- /tad-/ \\\"to spin (thread)\\\" ... NP tanidan/tan- \\\"to turn, spin\\\" ... PIE *ten- ... Pok.: 1065 f.'.\"},\n            {\"src\": \"POK\", \"where\": \"p.1065-1066 s.v. 1. ten-\", \"stance\": \"supports\", \"note\": \"'Avestan pairi-tanava ... Old Indic ut-tāna- = Avestan ustāna- ...; np. tanīdan \\\"turn, spinnen\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"tâbîdan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP tābīdan / tāftan (pres. tāb-) 'to twist, spin, curl' (Hafez: tāb-e ān zolf 'the twist of that tress') goes back to Iranian *tāp-/*tap- 'to twist, wind' (Cheung *tap 2; NWIr. and Pamir cognates Yghn. tob-, Wa. tov-, Sh. tāb- 'wind, spin'), which Pokorny (p.1064), Watkins and Cheung derive from PIE *temp- 'to stretch', an enlargement of *ten-. So the link to the root box is right, but the arrow from Avestan tan- (#4) is not: tābīdan is not built on tan- (whose NP continuant is tanīdan), but on the parallel *temp- stem, with an unexplained long ā (Cheung). It must also be kept apart from the homonym tāftan/tābīdan 'to shine, heat' < *tap- 'warm' (PIE *tep-; MP tāftan 'heat, burn, shine', Horn no. 372); Nourai's superscript 1 marks the 'twist' verb correctly.\",\n          \"derivation_fa\": \"«تابیدن / تافتن» (ستاک حال «تاب») به معنای «پیچاندن، رشتن» (چنانکه در «تاب آن زلف پریشان» حافظ) از ایرانی *tāp- «پیچیدن» است که پوکورنی، واتکینز و چونگ آن را از هندواروپایی *temp- «کش دادن» (گونهٔ گسترش‌یافتهٔ *ten-) می‌دانند. پس پیوند با ریشهٔ اصلی درست است، ولی این فعل از tan- اوستایی (که دنباله‌اش «تنیدن» است) برنیامده، بلکه از ستاک موازی *tap- است. باید آن را از «تافتن / تابیدن» به معنای «درخشیدن، گرم کردن» (از *tep- «گرم بودن») جدا کرد. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/تافتن\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/temp-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1064\", \"status\": \"supports\", \"note\": \"POK_full.txt p.1064 s.v. temp-: 'Npers. tāb-ad, Inf. tāftan and tāb-ī-dan \\\"turn, spinnen\\\", intr. \\\"sich drehen, gequält werden\\\" (from one to *tap = Indo Germanic *tmp- analogical refined Kaus. *tapayati)' — i.e. under *temp-, not under Av. tan-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"p. 379 s.v. *tap 'to twist, wind'\", \"stance\": \"supports\", \"note\": \"'NWIR: NP tāftan/tāb- \\\"to turn, twist, spin\\\", NP tāb \\\"twisting, curling lock\\\" ... The consistently long stem vowel ... is puzzling ... it cannot be explained from a zero grade *tmp- (> Ir. *tap-) ... PIE (?) *temp- \\\"to draw, twist\\\" = LIV: 626 | Pok.: 1064 f.'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 372, p.83 (HRN.txt line 3503)\", \"stance\": \"partial\", \"note\": \"'Eine andere Wurzel tap liegt zu Grunde in tāften \\\"drehen, spinnen etc.\\\", Praes. tāb-em, tābīden, tāfte \\\"Taffet\\\", tefne \\\"Spinnengewebe\\\" ... wax. tow-am ... \\\"winden, drehen\\\"' — separates it from tāften 'brennen' but gives no IE root.\"},\n            {\"src\": \"PHD\", \"where\": \"p.81 (line 4875-4880)\", \"stance\": \"silent\", \"note\": \"Only 'tābīdan = tāftan' and 'tāftan, tāb- heat, burn; shine' (the homonym); 'tadan, tan- spin (thread)' is the tan- verb. No MP 'twist' tāftan.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 185], entry under *temp-\", \"stance\": \"supports\", \"note\": \"'فارسی: تابیدن، تافتن، تاب (به چم \\\"گرداندن\\\" و \\\"پیچیدن\\\")' listed with Latin, Lithuanian etc. cognates of the *temp- root (OCR rough).\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.~721 (leaf 729)\", \"stance\": \"supports\", \"note\": \"'npers. tāb-ad Inf. tāftan und tāb-ī-dan \\\"drehen, wenden, spinnen\\\" ... (aus einem zu *tap = idg. *tmp- analogisch gebildeten Kaus.)'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Pass-through French box for the English words: French taffetas (14th c.), from Italian taffettà / Medieval Latin taffata < Persian tāfta 'twisted, woven' (pp. of tāftan) — confirmed (Klein, Skeat, Devic); and French tapis 'carpet' / tapisserie 'tapestry', from Old French tapiz < Medieval Greek tapētion, dim. of Greek tápēs 'carpet' — here the Persian link exists only if Greek tápēs is itself Iranian (traditional view, Pokorny/Watkins/Klein; Beekes: Pre-Greek). English tape did not pass through French. Hence 'plausible' for the box as a whole.\",\n          \"derivation_fa\": \"این خانهٔ فرانسوی گذرگاه واژه‌های انگلیسی است: taffetas فرانسوی از ایتالیایی taffettà و آن از فارسی «تافته» (بافتهٔ تابیده) است که درست است؛ ولی tapis و tapisserie فرانسوی از یونانی tápēs «فرش» آمده‌اند و پیوند آن با ایرانی تنها بنا بر دیدگاه سنتی (پوکورنی، واتکینز، کلاین) پذیرفته است و بیکس آن را پیشایونانی می‌داند. tape انگلیسی اصلاً از فرانسه نگذشته است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/taffeta\",\n            \"https://en.wiktionary.org/wiki/tapestry\",\n            \"https://en.wiktionary.org/wiki/τάπης\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The French box carries no reference in the book.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale, s.v. Taffetas (DEV.txt line 2168)\", \"stance\": \"partial\", \"note\": \"'Taffetas. C'est sans doute le persan tāfteh ou tefteh, même signification ... à moins que ce ne soit une simple onomatopée, reproduisant le bruit produit par le taffetas'.\"},\n            {\"src\": \"KLN\", \"where\": \"p.1566 s.v. taffeta (KLN_1966.txt leaf 830)\", \"stance\": \"supports\", \"note\": \"'ME. taffeta, fr. MF. (= F.) taffetas, fr. It. taffetà, fr. Pers. tāftah, \\\"twisted fabric\\\", fr. tāftan, \\\"to shine; to spin, twist\\\"'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Taffeta, Tapestry (SKT.txt leaves 514-517)\", \"stance\": \"supports\", \"note\": \"'Taffeta ... F. taffetas — Ital. taffetà ... — Pers. tāftah, twisted, woven, taffeta. — Pers. tāftan, to twist, spin, curl'; 'Tapestry ... F. tapisserie ... F. tapis ... L. tapēte ... Gk. tapēs, a carpet ... Cf. Pers. tabastah, a fringed carpet'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"taffeta, tape, tapestry\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"taffeta: confirmed — Late ME taffeta < OF taffetas < It. taffettà / ML taffata < Persian tāfta 'twisted (silk)', past participle of tāftan 'to twist, spin' (Klein, Skeat, Wiktionary, Watkins under temp-). tapestry: plausible — ME tapistry < MF tapisserie < tapis < OF tapiz < Medieval Greek tapētion < Greek tápēs 'carpet', which Pokorny, Watkins and Klein regard as an Iranian loan (Iranian *tap- 'twist' or Persian tanbase 'rug'), while Beekes argues for a Pre-Greek origin (Wiktionary τάπης). tape: disputed — ME tape, tappe < OE tæppe, tæppa 'strip of cloth, ribbon'; Wiktionary gives 'further origin unclear, probably akin to Old Frisian tapia \\\"to pull, tear\\\", MLG tappen' and Watkins files it under a Germanic base tap-, not under temp-; Klein's and Skeat's suggestion of a back-formation from Latin tapete is a minority view and in any case would not make it Persian. Worst verdict (tape) applies.\",\n          \"derivation_fa\": \"taffeta (تافته) درست است: از فرانسهٔ taffetas و ایتالیایی taffettà از فارسی «تافته» (ابریشم تابیده)، صفت مفعولی «تافتن». tapestry با احتیاط پذیرفتنی است: از فرانسهٔ tapisserie و tapis از یونانی tápēs «فرش» که پوکورنی و واتکینز و کلاین آن را وام‌واژه‌ای ایرانی می‌دانند، ولی بیکس پیشایونانی‌اش می‌شمارد. tape را پژوهش امروزی واژه‌ای بومی انگلیسی (انگلیسی کهن tæppe «نوار پارچه») می‌داند که احتمالاً با واژه‌های ژرمنی به معنای «کشیدن، دریدن» هم‌ریشه است؛ پیوند آن با فارسی رد می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/taffeta\",\n            \"https://en.wiktionary.org/wiki/tape\",\n            \"https://en.wiktionary.org/wiki/tapestry\",\n            \"https://en.wiktionary.org/wiki/τάπης\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:572\", \"status\": \"supports\", \"note\": \"Misprint in the book for KLN:1572: Klein 1966 leaf 833 (printed p.1572) s.v. tapestry: 'fr. tapition, the MGk. pronunciation of Gk. tapētion, dimin. of tapēs, gen. tapētos, \\\"hanging, carpet\\\" ... a word of Iranian origin. Cp. ModPersian tāb-ad, inf. tāftan, tāb-ī-dan, \\\"to turn, twist\\\", fr. Iranian *tap-, corresponding to I.-E. *tmp-, \\\"to stretch, extend\\\" ... Cp. also taffeta, tape'. s.v. tape (same page): 'OE. tæppa, tæppe, \\\"tape, ribbon\\\", prob. back formation fr. L. tapete, \\\"carpet\\\"'. Klein supports all three as Nourai draws them.\"},\n            {\"ref\": \"SKT:542\", \"status\": \"partial\", \"note\": \"The local Skeat (1911 Concise, SKT.txt) has the entries on different pages (leaves 514-517, printed ~491-494), so Nourai used another edition. Content: taffeta < Pers. tāftah; tapestry < Gk. tapēs, 'Cf. Pers. tabastah, a fringed carpet'; tape 'A.S. tæppe ... probably meant strips of stuff ... borrowed from L. tapēte'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, temp- and index (AHD_watkins1985.txt lines 1068, 1080, 2338)\", \"stance\": \"partial\", \"note\": \"temp-: 'Persian tāftan, to twist, spin ... TAFFETA; b. Iranian *tap-, \\\"carpet,\\\" in Greek tapēs: TAPESTRY'; but 'TAPE tap-': '[tap-. Germanic base ... 10. Old English tæppe, strip of cloth: TAPE.]' — contradicts the Persian link for tape.\"},\n            {\"src\": \"FSD\", \"where\": \"not searched\", \"stance\": \"silent\", \"note\": \"Funk & Wagnalls not grepped for these headwords; Klein, Skeat and Watkins already cover the chain.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. tape\", \"stance\": \"partial\", \"note\": \"'tape (L.-Gk.) M.E. tape, also tappe. A.S. tæppe, a tape, a fillet; closely allied to A.S. tæppet, a tippet' — Skeat accepts a Latin loan, not a Persian word.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Avestan\",\n          \"words\": \"tauruna\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Avestan tauruna- 'young' (of humans and animals; spā tauruna- 'a young dog' V 5.30; m. 'boy', Bartholomae col. ~640) is real and = Skt táruṇa- 'young, tender', Gk térēn 'tender', Lat. tener. But it is not from PIE *ten- 'stretch': Pokorny files it under 'ter-2, teru- feeble, fragile, weak' (pp.1070-1071), Mann under 'teren- (terun-) weak, tender', Walde-Pokorny under ter- 'zart', and Klein (s.v. tender) cites only these cognates. Nourai's gloss 'stretched' has no support. (Watkins does put Latin tener under ten- as *ten-ero- 'stretched, thin', but he does not include the Indo-Iranian táruṇa-/tauruna-, whose -ru- cannot come from *ten-.) The word is right; its attachment to this root is rejected.\",\n          \"derivation_fa\": \"صفت اوستایی tauruna- «جوان» (برای آدمی و جانور؛ spā tauruna «سگ جوان»، بارتولمه ستون ۶۴۰) واژه‌ای درست و هم‌ریشه با سنسکریت táruṇa- «جوان، نازک» و یونانی térēn «نرم» است. اما پوکورنی (۱۰۷۰–۱۰۷۱)، مان و والده-پوکورنی آن را از ریشهٔ دیگری، *ter- / *teru- «نرم، ناتوان، نازک»، می‌دانند، نه از *ten- «کشیدن»؛ معنای «کشیده» که نورایی آورده در هیچ منبعی نیست. پس واژه درست است ولی نسبت دادن آن به این ریشه را پژوهش امروزی رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/توله\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1585\", \"status\": \"contradicts\", \"note\": \"Klein 1966 leaf 840 (≈ p.1585-1586) s.v. tender, adj.: 'fr. L. tenerum, acc. of tener, \\\"soft, delicate, tender\\\", which is prob. rel. to Sabine tereno-, \\\"soft, delicate\\\", and cogn. with OI. táruṇah, \\\"young, tender\\\", Avestic tauruna-, \\\"young\\\", Gk. terēn, \\\"tender, delicate\\\", Arm. t'arm ...'. Klein confirms the word and meaning but connects it with tener/tereno-, not with *ten- 'stretch'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp.1070-1071 s.v. ter-2, teru- (POK_full.txt line 85953)\", \"stance\": \"contradicts\", \"note\": \"'Root / lemma: ter-2, teru- Meaning: feeble, fragile, weak ... Gr. terēn \\\"tender\\\", sabin. terenum \\\"molle\\\", Latin ... tener ...; from the u-basis: Old Indic taruṇa- ... \\\"young, tender\\\", Avestan tauruna- \\\"young\\\", osset. tærin \\\"knave, boy\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.~728 (leaf 738)\", \"stance\": \"contradicts\", \"note\": \"'Wzform tereu-: Ai. taruṇa-ḥ, gr. terēn usw., s. u. ter- \\\"zart\\\"'.\"},\n            {\"src\": \"BRT\", \"where\": \"col. ~640 s.v. tauruna- (BRT.txt line 12100)\", \"stance\": \"partial\", \"note\": \"'• j. tauruna- Adj. \\\"jung\\\" von Menschen und Tieren ... spā tauruna \\\"ein junger Hund\\\" V. 5.30 ... a) m. \\\"Knabe\\\" ... ai. táruṇa- Adj.; np. vgl. tar.' — confirms word and NP comparison, no root *ten-.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. teren- (IEC.txt line 18414)\", \"stance\": \"contradicts\", \"note\": \"'teren- (terun-, tern-) \\\"weak, tender\\\". WP I, 728 Skt. táruṇah \\\"young, tender, fresh\\\" ... Av. tauruno, id.; Per. tar \\\"moist, fresh\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"tar 2; tarâneh; tŭleh; tŭrah\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"tūla 'whelp, young of an animal' (Classical tōla) is the best-supported: Horn no. 403 'tōle \\\"junger Hund\\\" < aw. (spā) tauruna-; phlv. tarūk / tōruk; ai. táruṇa-; kurd. tūle', with u-epenthesis (*taurna- > *tōrn- > tōl-), and Wiktionary 'MP twlkʾ /tōlag/ \\\"baby animal, whelp\\\", from Avestan tauruna \\\"young\\\"'. tar 'wet, moist, fresh' = MP tarr [tl] 'moist, fresh' (MacKenzie, Nyberg), which Nyberg derives 'probably < *tarna-, cf. perhaps Av. tauruna- \\\"young\\\", Skr táruṇa- \\\"young, fresh\\\"' and Horn compares with tauruna- 'trotz des Bedeutungsunterschiedes' — accepted with hesitation. tarāna 'handsome youth' > 'quatrain, song' is explained by Mo'in and Horn as a derivative of tar 'fresh' (+ -āna), while Wiktionary proposes *terh₂- 'pass through' — uncertain. tūra 'jackal' (MP tōrag, Bal. tōlag 'jackal') is put with tūla by Mo'in ('توره (شغال) و توله از همین ریشه'), but Horn introduces it with 'Dagegen' as a separate word, and Wiktionary lists tōra only as a variant of tōla 'whelp'. All four belong, if anywhere, to PIE *ter-/teru- (see #8), not to *ten-.\",\n          \"derivation_fa\": \"«توله» (بچهٔ سگ و جانوران) استوارترین است: هرن (شمارهٔ ۴۰۳) و ویکی‌واژه آن را از پهلوی tōlag / tarūk و اوستایی tauruna- «جوان» می‌دانند، با درج u در هجا (*taurna > tōl-). «تر» (خیس، تازه) از فارسی میانهٔ tarr است که نیبرگ «احتمالاً از *tarna- و شاید هم‌ریشه با tauruna» دانسته و هرن نیز با تردید سنجیده است. «ترانه» را معین و هرن از «تر» (تازه، جوان خوش‌روی) می‌دانند، ولی ویکی‌واژه ریشهٔ دیگری پیشنهاد می‌کند. «توره» (شغال) را معین با «توله» هم‌ریشه می‌داند، اما هرن آن را جدا آورده است. همهٔ این واژه‌ها، اگر از tauruna باشند، از ریشهٔ *ter- «نرم، جوان»اند نه *ten-؛ ادعای نورایی دربارهٔ پیوند ایرانی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/توله\",\n            \"https://en.wiktionary.org/wiki/تر\",\n            \"https://en.wiktionary.org/wiki/ترانه\",\n            \"https://abadis.ir/fatofa/توره/\",\n            \"https://abadis.ir/fatofa/ترانه/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:90\", \"status\": \"partial\", \"note\": \"Horn no. 403, p.90 (HRN.txt line 3765, leaf 111): 'tōle \\\"junger Hund\\\" (SF). aw. (spā) tauruno; phlv. tarūk bezw. tōruk ...; ai. táruṇa-; kurd. tūle (LW.) \\\"junger Hund, Jagdhund\\\". Dagegen np. tōre \\\"Schakal\\\" (g. tōrä ...) ; phlv. tōrak (PPGl.); kurd. tūre \\\"Otter\\\"; bel. tōlag ... \\\"Schakal\\\" (398). Np. tōle etc. beruhen auf u-Epenthese.' Supports tūla; treats tūra separately. tar is at Horn p.85 ('ter, terr \\\"feucht, frisch\\\"; vergl. terane \\\"schöner Jüngling\\\". aw. vergl. tauruna- \\\"jung\\\"').\"},\n            {\"ref\": \"BQT:532\", \"status\": \"supports\", \"note\": \"Not rendered; the same footnote is in BQT vol.1 s.v. تر (BQT_v1_pages.txt leaf 705, 'بقیه از صفحهٔ ۴۷۸'): 'فارسی: تر، تازه. پهلوی tar ... ازهمین ریشه است ترانهٔ فارسی (جوان خوش روی و دوبیتی و سرود) و تولهٔ فارسی (بچهٔ سگ) و توره (شغال)'; Dehkhoda (abadis توره) quotes Mo'in: 'در اوستا تئورونه صفت است به معنی جوان و برای بچه آدمی و جانور بکار رفته و توره (شغال) و توله از همین ریشه است (حاشیه برهان چ معین)'.\"},\n            {\"ref\": \"BQT:217\", \"status\": \"not_checked\", \"note\": \"Page not rendered; the Mo'in footnote that carries Nourai's claim was read at the تر entry instead.\"},\n            {\"ref\": \"FIB:217\", \"status\": \"not_checked\", \"note\": \"Pur-Davud, Farhang-e Iran-e Bastan: not available locally (noorlib viewer needs a browser).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"II p.190 s.v. tarr (NYB_vol2_glossary.txt line 3749)\", \"stance\": \"partial\", \"note\": \"'tarr [tl] humid, moist ... Probably < *tarna-, cf perhaps Av. (643) tauruna- \\\"young\\\", Skr taruṇa- \\\"young, fresh\\\"; Skr tarṇa-ka- \\\"calf, young animal in general\\\". NP tar.'\"},\n            {\"src\": \"PHD\", \"where\": \"p.82 (line 4939)\", \"stance\": \"silent\", \"note\": \"'tarr [tl, LCDr ... N tar] moist, fresh' — no etymology given.\"},\n            {\"src\": \"HRN\", \"where\": \"p.85 (HRN.txt line 3582)\", \"stance\": \"partial\", \"note\": \"'(d)ter, terr, terri (AM.) \\\"feucht, frisch\\\"; vergl. terane \\\"schöner Jüngling\\\". aw. vergl. tauruna- \\\"jung\\\"; ai. táruṇa- \\\"jung, zart\\\"; gr. terēn ... Die Etymologie wird wohl trotz des Bedeutungsunterschiedes durch Abu Mansur Muvaffaq's terr gesichert'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. teren-\", \"stance\": \"partial\", \"note\": \"'Av. tauruno, id.; Per. tar \\\"moist, fresh\\\"' under teren- 'weak, tender' (not ten-).\"},\n            {\"src\": \"BRT\", \"where\": \"col. ~640 s.v. tauruna-\", \"stance\": \"supports\", \"note\": \"'np. vgl. tar. — Wegen np. ... \\\"junger Hund\\\" s. IFAnz. 10.22' — Bartholomae too compares tar and the NP word for 'young dog'.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Avestan\",\n          \"words\": \"tathra; thri-thatra\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"No Avestan *tąθra- 'string, warp' is attested; it is the form Horn (no. 369: 'tār \\\"Faden\\\". aw. *tąθra-, vergl. ai. tántra- \\\"Zettel, Aufzug des Gewebes\\\"') and Pokorny (p.1065: 'tantra-m \\\"Zettel, Aufzug am Webstuhl\\\" = np. tār (Avestan *tąθra-)') reconstruct for the ancestor of NP tār, i.e. Proto-Iranian *tánθram < PIIr *tántram < PIE *ten-tro- 'instrument for stretching' (Wiktionary, Watkins). The Iranian cluster *-nθr- loses its nasal and lengthens the vowel (*tanθra- > tār), as in Horn's account. 'thri-thatra' 'sitar' (Av. θri- 'three' + *θatra-) is not attested anywhere and is a back-projection of NP si-tār, a much later instrument name; the book also spells the second element inconsistently (tathra vs thatra). The derivation of tār from *ten- is sound, but both 'Avestan' forms are unattested.\",\n          \"derivation_fa\": \"صورت اوستایی «tathra» (درست‌تر *tąθra-) در متن‌های اوستایی گواهی نشده است؛ این صورتی است که هرن (شمارهٔ ۳۶۹) و پوکورنی (ص ۱۰۶۵) برای نیای «تار» فارسی بازسازی کرده‌اند: ایرانی آغازین *tánθram از هندوایرانی *tántram (هم‌ریشه با سنسکریت tantra «تار و پود») و هندواروپایی *ten-tro- «ابزار کشیدن». خوشهٔ -nθr- با افتادن خیشومی و کشش واکه به «تار» رسیده است. «thri-thatra» (سه‌تار) در هیچ منبعی نیامده و برساختهٔ نورایی از روی «سه‌تار» فارسی است؛ کتاب حتی آن را با املای ناهمسان (tathra / thatra) آورده است. اشتقاق «تار» از *ten- درست است ولی دو صورت «اوستایی» بازسازی‌اند؛ با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/تار\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ten-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1065\", \"status\": \"supports\", \"note\": \"POK_full.txt p.1065-1066 s.v. 1. ten-: 'tantra-m \\\"Zettel, Aufzug am loom\\\" = np. tār (Avestan *tąθra-) ds., afghan. tār \\\"net\\\"' — the Avestan form is starred (reconstructed) in Pokorny; no θri- compound.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 369, p.82 (HRN.txt line 3468)\", \"stance\": \"supports\", \"note\": \"'369. (1) tār \\\"Faden\\\". aw. *tąθra-, vergl. ai. tāntra- \\\"Zettel, Aufzug des Gewebes\\\"' — reconstructed, not attested.\"},\n            {\"src\": \"BRT\", \"where\": \"grep 'taθra', 'tąθra'\", \"stance\": \"silent\", \"note\": \"Bartholomae has only tąθra- 'darkness' (the homonym behind NP tār 'dark', Horn no. 370); no *tąθra- 'string' and no θri-compound for an instrument.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.~723 (leaf 730)\", \"stance\": \"supports\", \"note\": \"'tantra-m \\\"Zettel, Aufzug am Webstuhl\\\" = np. tār (av. *taθra-) ds.'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins ten- I.4\", \"stance\": \"supports\", \"note\": \"'Suffixed form *ten-tro- in Persian tār, string: SITAR'.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"târ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP tār 'string, thread, warp' and, by extension, the name of the long-necked lute tār; si-tār (se-tār) 'three strings' = sih 'three' (OP θri-, Av. θri-) + tār. tār < MP *tār < Proto-Iranian *tánθram < PIIr *tántram (Skt tantra- 'warp, loom') < PIE *ten-tro-, from *ten- 'to stretch' (Wiktionary تار Etymology 2; Horn no. 369; Watkins). It must be kept apart from the homonym tār 'dark' < *támHsram (Av. tąθra- 'darkness', Horn no. 370). Nourai's derivation from the *ten- branch is correct.\",\n          \"derivation_fa\": \"«تار» به معنای «رشته، نخ، تار پارچه» و سپس نام ساز «تار»، و «سه‌تار» (سه + تار)، از ایرانی آغازین *tánθram و هندوایرانی *tántram (سنسکریت tantra «تار و پود») از ریشهٔ هندواروپایی *ten- «کشیدن» است؛ هرن، واتکینز و ویکی‌واژه همین را می‌گویند. باید آن را از «تار» به معنای «تاریک» (از اوستایی tąθra- «تاریکی») جدا کرد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/تار\",\n            \"https://en.wiktionary.org/wiki/سه‌تار\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box has no reference in the book; the claim was checked against Horn no. 369 and Pokorny 1065 (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 369, p.82\", \"stance\": \"supports\", \"note\": \"'(1) tār \\\"Faden\\\". aw. *tąθra-, vergl. ai. tāntra-' — and no. 370 '(2) tār \\\"finster\\\" ... aw. tąθra- \\\"finster\\\"' as a separate word.\"},\n            {\"src\": \"POK\", \"where\": \"p.1065 s.v. 1. ten-\", \"stance\": \"supports\", \"note\": \"'tantra-m ... = np. tār (Avestan *tąθra-)'.\"},\n            {\"src\": \"PHD\", \"where\": \"grep 'thread', 'string'\", \"stance\": \"silent\", \"note\": \"MacKenzie has no MP tār 'string' (only tār 'darkness', line 4925, and rōd 'stringed instrument').\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt grep تار\", \"stance\": \"silent\", \"note\": \"The تار entry's footnote could not be isolated in the OCR (too many hits for the substring); not used.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Hindustani\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pass-through box for Hindi sitār / Urdu sitār, borrowed in the Mughal period from Persian si-tār / se-tār 'three-stringed (lute)'; the Indian instrument was developed in the 18th c. and kept the Persian name although it now has many more strings. AHD: 'Hindi sitār, from Persian: si, three + tār, string'.\",\n          \"derivation_fa\": \"این خانه گذرگاه «ستار» هندی/اردو (sitār) است که در دورهٔ گورکانیان از «سه‌تار» فارسی وام گرفته شد؛ ساز هندی که در سدهٔ هجدهم شکل گرفت نام فارسی را نگه داشت، هرچند سیم‌هایش بسیار بیش از سه است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/sitar\",\n            \"https://ahdictionary.com/word/search.html?q=sitar\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1210\", \"status\": \"supports\", \"note\": \"AHD online (the updated text of the dictionary entry Nourai cites at p.1210): 'sitar [Hindi sitār, from Persian: si, three; see trei- in the Appendix of Indo-European roots + tār, string; see ten- in the Appendix of Indo-European roots.]'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"grep 'sitar', 'sittar', 'setar'\", \"stance\": \"silent\", \"note\": \"Hobson-Jobson has no sitar entry (hits only 'Vansittart').\"},\n            {\"src\": \"AID\", \"where\": \"grep 'sitar'\", \"stance\": \"silent\", \"note\": \"Whitworth's Anglo-Indian Dictionary: no hit.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 index 'SITAR ten-, trei-'\", \"stance\": \"supports\", \"note\": \"Index line 2265: 'SITAR ten-, trei-'.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"sitar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English sitar (first recorded mid-19th c.) from Hindi/Urdu sitār < Persian si-tār 'three strings' (sih 'three' < PIE *tréyes + tār 'string' < PIE *ten-). Wiktionary: 'From Hindi sitār / Urdu sitār, from Classical Persian si-tār, literally \\\"three strings\\\". Doublet of setar'.\",\n          \"derivation_fa\": \"sitar انگلیسی از «ستار» هندی/اردو و آن از «سه‌تار» فارسی (سه + تار) است؛ «سه» از هندواروپایی *tréyes و «تار» از *ten- «کشیدن». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/sitar\",\n            \"https://ahdictionary.com/word/search.html?q=sitar\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed for this box; AHD (cited on the Hindustani box) covers it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, ten- I.4\", \"stance\": \"supports\", \"note\": \"'Suffixed form *ten-tro- in Persian tār, string: SITAR'.\"},\n            {\"src\": \"KLN\", \"where\": \"grep '^sitar' in KLN_1966.txt\", \"stance\": \"silent\", \"note\": \"Klein has no entry sitar; s.v. cither he cites 'Pers. sihtār' as the (alleged) source of Greek kithara.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Greek\",\n          \"words\": \"kithara\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Greek kithára 'lyre, cithara' (Homeric kítharis, 8th c. BCE) is real, but its derivation from Persian tār / si-tār is rejected by modern scholarship: Beekes treats it as a Pre-Greek word (possibly related to Hurro-Urartian/Semitic *kinnār- 'lyre'), and the Persian si-tār is a New Persian compound attested only from the Islamic period, more than a millennium after kithara, with no Old Iranian instrument name *θri-tār in evidence. Phonetically, Greek k- and the -ith- vowel pattern have no match in Persian s(i)-tār. Klein's 'Gk. kithara, fr. Pers. sihtār', which Nourai reproduces, is an old popular comparison. Wiktionary's guitar entry explicitly says guitar is 'Doublet of cithara, cither, and zither, but not related to sitar'.\",\n          \"derivation_fa\": \"«کیثارا»ی یونانی (در هومر kítharis) واژه‌ای درست است، ولی برگرفتن آن از «تار» یا «سه‌تار» فارسی را پژوهش امروزی رد می‌کند: بیکس آن را پیشایونانی (شاید هم‌ریشه با kinnār «چنگ» در زبان‌های خاور نزدیک) می‌داند و «سه‌تار» ترکیبی فارسی نو و هزار سال دیرتر از کیثاراست؛ از نظر آوایی نیز k- و ساخت یونانی با «سه‌تار» نمی‌خواند. نورایی این را از کلاین گرفته که نوشته است «یونانی kithara از فارسی sihtār»؛ ولی ویکی‌واژه صریحاً می‌گوید guitar با cithara هم‌ریشه است «اما با sitar پیوندی ندارد».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/κιθάρα\",\n            \"https://en.wiktionary.org/wiki/guitar\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:687\", \"status\": \"supports\", \"note\": \"Klein 1966 leaf 370 (printed pp.686-687) s.v. guitar: 'F. guitare, fr. Sp. guitarra, fr. Arab. qitārah, fr. Gk. kithara, fr. Pers. sihtār. See cither'; s.v. cither (leaf 165): 'fr. L. cithara, fr. Gk. kithara, fr. Pers. sihtār'. Klein supports Nourai's arrow; modern sources do not.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD online s.v. guitar, zither\", \"stance\": \"contradicts\", \"note\": \"'guitar [French guitare, from Spanish guitarra, from Greek kitharā, cithara.]'; zither '... from Latin cithara, from Greek kitharā' — AHD stops at Greek and does not derive kithara from Persian.\"},\n            {\"src\": \"DEV\", \"where\": \"s.v. Cinnor (DEV.txt line 1150)\", \"stance\": \"partial\", \"note\": \"'CINNOR ou KINNOR. Instrument de musique chez les Hébreux ... qu'on interprète par le latin cithara' — the Semitic kinnōr comparison that underlies the modern Pre-Greek/Near Eastern view, not a Persian one.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. cither (leaf 165)\", \"stance\": \"supports\", \"note\": \"'cither, also cithern ... F. cithare, fr. L. cithara, fr. Gk. kithara, fr. Pers. sihtār' — the source of Nourai's claim.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Arabic\",\n          \"words\": \"qîtâr, qĕtarah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic qīṯāra (also qīṯār; Klein's 'qitārah') 'lute, guitar', pl. qayāṯīr, borrowed via Aramaic qīṯārā from Greek kithára, Greek kh/th rendered by Aramaic/Arabic q- and ṯ (Wiktionary قيثارة). The second spelling 'qĕtarah' reflects the vocalisation given by Nourai's source (Sayyah's Munjid translation) and Klein. The arrow Greek → Arabic is correct.\",\n          \"derivation_fa\": \"«قیثاره / قیثار» عربی (جمع: قیاثیر) به معنای «عود، گیتار» از راه آرامی qīṯārā از یونانی kithára وام گرفته شده است؛ k یونانی به ق و th به ث برگردانده شده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/قيثارة\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SAP:1381\", \"status\": \"not_checked\", \"note\": \"Sayyah's Farhang-e Jame' is purchase-only (refs_online.json); not accessible.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p.687 s.v. guitar\", \"stance\": \"supports\", \"note\": \"'fr. Arab. qitārah, fr. Gk. kithara'.\"},\n            {\"src\": \"AFA\", \"where\": \"grep 'qît', 'kithar', 'cithar' in AFA.txt\", \"stance\": \"silent\", \"note\": \"Fraenkel's Aramäische Fremdwörter: no hit in the OCR text.\"},\n            {\"src\": \"LKT\", \"where\": \"grep 'kithar', 'qit', 'guitar'\", \"stance\": \"silent\", \"note\": \"Lokotsch: no hit.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Spanish\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pass-through box for Spanish guitarra (13th c., Old Spanish guitarra), from Andalusian Arabic qīṯāra (Wiktionary, Klein); some Romance specialists derive it instead directly from Latin cithara via Mozarabic, but the Arabic route is the standard account in Klein and Wiktionary. Arabic th > Spanish t, initial q > g(u).\",\n          \"derivation_fa\": \"این خانه گذرگاه guitarra اسپانیایی است که در سدهٔ سیزدهم از عربی اندلسی «قیثاره» گرفته شد (ق به g و ث به t بدل شده)؛ برخی آن را مستقیماً از لاتین cithara می‌دانند، ولی کلاین و ویکی‌واژه راه عربی را می‌پذیرند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/guitar\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed on the Spanish box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p.687 s.v. guitar\", \"stance\": \"supports\", \"note\": \"'F. guitare, fr. Sp. guitarra, fr. Arab. qitārah'.\"},\n            {\"src\": \"DOZ\", \"where\": \"grep 'guitar' in DOZ.txt\", \"stance\": \"silent\", \"note\": \"Dozy-Engelmann OCR has no guitarra entry.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"French\",\n          \"words\": \"guitare\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French guitare (17th c.; earlier guiterne, guitere) from Spanish guitarra (Klein, AHD, Wiktionary). Older French guiterne (> ME gittern) represents an earlier, separate borrowing of the same Arabic/Latin word.\",\n          \"derivation_fa\": \"guitare فرانسوی (سدهٔ هفدهم) از guitarra اسپانیایی گرفته شده است؛ guiterne کهن‌تر فرانسوی (و gittern انگلیسی) وام‌گیری جداگانه و پیشین همان واژه است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://ahdictionary.com/word/search.html?q=guitar\",\n            \"https://en.wiktionary.org/wiki/guitar\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:687\", \"status\": \"supports\", \"note\": \"Klein p.687 s.v. guitar: 'F. guitare, fr. Sp. guitarra'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD online s.v. guitar\", \"stance\": \"supports\", \"note\": \"'[French guitare, from Spanish guitarra, from Greek kitharā, cithara.]'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 8124\", \"stance\": \"partial\", \"note\": \"'Guitar; see Cithern' — Skeat treats it with cithern, from Latin/Greek.\"}\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"Persian\",\n          \"words\": \"gîtâr\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian gītār 'guitar' is a 20th-c. loan from French guitare (Mo'in tags it [فر.] 'French'); French gu- [g] rendered by Persian g, final -e dropped. It is therefore a Western loan returning to Persian and has nothing to do with native tār.\",\n          \"derivation_fa\": \"«گیتار» فارسی در سدهٔ بیستم از guitare فرانسوی گرفته شده و معین آن را با نشانهٔ [فر.] آورده است؛ پیوندی با «تار» بومی ندارد و وام‌واژه‌ای اروپایی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/گیتار/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:3502\", \"status\": \"supports\", \"note\": \"Mo'in's entry (abadis, فرهنگ معین): 'گیتار [ فر. ] (اِ.) از سازهای زهی که دارای شش سیم می باشد و با انگشتان دست نواخته می شود' — origin French, as Nourai draws; the print page 3502 could not be mapped online.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir s.v. گیتار\", \"stance\": \"supports\", \"note\": \"'[ فر. ]' = French.\"},\n            {\"src\": \"BQT\", \"where\": \"grep گیتار in BQT_v1-v5\", \"stance\": \"silent\", \"note\": \"Not in Borhan (a modern loan).\"}\n          ]\n        },\n        {\n          \"id\": 19,\n          \"lang\": \"English\",\n          \"words\": \"guitar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English guitar (17th c.) from French guitare < Spanish guitarra < Arabic qīṯāra < (Aramaic) < Greek kithára (Klein, AHD, Wiktionary). Doublet of cithara, cither and zither.\",\n          \"derivation_fa\": \"guitar انگلیسی (سدهٔ هفدهم) از guitare فرانسوی، از guitarra اسپانیایی، از «قیثاره» عربی و آن از یونانی kithára است و با cithara و zither دوگانه است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/guitar\",\n            \"https://ahdictionary.com/word/search.html?q=guitar\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:687\", \"status\": \"supports\", \"note\": \"Klein 1966 leaf 370 (pp.686-687): 'guitar, n., a stringed musical instrument. — F. guitare, fr. Sp. guitarra, fr. Arab. qitārah, fr. Gk. kithara, fr. Pers. sihtār. See cither and cp. gittern, zither.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD online s.v. guitar\", \"stance\": \"supports\", \"note\": \"'[French guitare, from Spanish guitarra, from Greek kitharā, cithara.]'.\"},\n            {\"src\": \"SKT\", \"where\": \"line 8124\", \"stance\": \"supports\", \"note\": \"'Guitar; see Cithern' (Latin/Greek cithara).\"}\n          ]\n        },\n        {\n          \"id\": 20,\n          \"lang\": \"Latin\",\n          \"words\": \"cithara\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin cithara 'lyre, cithara' is a direct loan of Greek kithára, Greek k rendered c and th kept as th in learned spelling (Klein, AHD, Wiktionary). It is the source of Old French citole, guiterne, OHG zitera and English cither, cittern, gittern.\",\n          \"derivation_fa\": \"cithara لاتینی وام‌گیری مستقیم از یونانی kithára است و خود سرچشمهٔ citole و guiterne فرانسوی کهن، zitera آلمانی کهن و cither و cittern انگلیسی شده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/zither\",\n            \"https://ahdictionary.com/word/search.html?q=zither\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD s.v. zither: '... from Latin cithara, cithara, from Greek kitharā'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. cithara (KLN_1966.txt line 7786)\", \"stance\": \"supports\", \"note\": \"'cithara, n., an ancient musical instrument resembling a lyre. — L., fr. Gk. kithara.'\"},\n            {\"src\": \"LAT\", \"where\": \"not grepped\", \"stance\": \"silent\", \"note\": \"Ernout-Meillet not searched; the Greek loan is uncontested.\"}\n          ]\n        },\n        {\n          \"id\": 21,\n          \"lang\": \"English\",\n          \"words\": \"zither, zithern, cither, cittern\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"zither (1850s) from German Zither < MHG *zitter < OHG zitera/zithara < Latin cithara (AHD, Wiktionary); zithern is the German plural/variant form used in English. cither, cithern (16th c.) from French cithare < Latin cithara (Klein). cittern (16th c.) is a variant of cithern, perhaps a blend of Latin cithara with gittern (AHD: 'Perhaps blend of Latin cithara ... and obsolete English gittern'). All four go back to Latin cithara < Greek kithára, as the chart shows.\",\n          \"derivation_fa\": \"zither از آلمانی Zither و آلمانی کهن zitera از لاتین cithara است؛ zithern گونهٔ آلمانی همان است؛ cither از فرانسهٔ cithare و لاتین cithara؛ و cittern گونهٔ cithern است که شاید از آمیختن cithara با gittern پدید آمده باشد. همه به لاتین cithara و یونانی kithára می‌رسند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/zither\",\n            \"https://ahdictionary.com/word/search.html?q=zither\",\n            \"https://ahdictionary.com/word/search.html?q=cittern\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD online: zither '[German, from Middle High German *zitter, from Old High German zitera, from Latin cithara, cithara, from Greek kitharā.]'; cittern '[Perhaps blend of Latin cithara, cithara; see CITHARA, and obsolete English gittern (from Middle English, from Old French guiterne, from Latin cithara).]'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. cither, cittern (KLN_1966.txt lines 7787-7792)\", \"stance\": \"supports\", \"note\": \"'cither, also cithern ... F. cithare, fr. L. cithara, fr. Gk. kithara ... Cp. cithara, citole, cittern, gittern, guitar, kit, zither'; 'cittern, n. — A var. of cither(n).'\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Gittern, Kit (SKT.txt lines 7608, 9710)\", \"stance\": \"supports\", \"note\": \"'Gittern; see Cithern'; 'Kit (3), a small violin ... for A.S. cytere, a cithern; from L. cithara'.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-15T02:55:59.978Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-501.json (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:56:11.908Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 - <<'EOF'\np='page-501.json'\ns=open(p).read()\nreps=[\n('\"MacKenzie pp. 4, 33 (PHD_mackenzie.txt lines 931-938, 2295-2301)\"','\"MacKenzie s.vv. āhang, āhixtan, frahang, frahixtan (PHD_mackenzie.txt lines 931-938, 2295-2301)\"'),\n('\"Manual of Pahlavi II pp. 4, 76, 92 (NYB_vol2_glossary.txt lines 298, 1506, 1514, 1968)\"','\"Manual of Pahlavi II s.vv. āhanj-, frahang, frahaxtan, haxtan (NYB_vol2_glossary.txt lines 298, 1506, 1514, 1968)\"'),\n('\"where\": \"p. 4 (line 938)\"','\"where\": \"s.v. āhixtan (PHD_mackenzie.txt lines 938, 2904)\"'),\n(\"p.40 'hixtan, hanj-\",\"'hixtan, hanj-\"),\n('\"II p.4 s.v. āhanj-, p.97 s.v. hixtan\"','\"II s.vv. āhanj-, hixtan (NYB_vol2_glossary.txt lines 298, 2009)\"'),\n('\"where\": \"p.81 (line 4875-4880)\"','\"where\": \"s.vv. tābīdan, tāftan, tadan (PHD_mackenzie.txt lines 4875-4880)\"'),\n('\"where\": \"II p.190 s.v. tarr (NYB_vol2_glossary.txt line 3749)\"','\"where\": \"II s.v. tarr (NYB_vol2_glossary.txt line 3749)\"'),\n('\"where\": \"p.82 (line 4939)\"','\"where\": \"s.v. tarr (PHD_mackenzie.txt line 4939)\"'),\n('{\"ref\": \"BQT:532\", \"status\": \"supports\", \"note\": \"Not rendered; the same footnote','{\"ref\": \"BQT:532\", \"status\": \"not_checked\", \"note\": \"Page 532 not rendered; Nourai\\'s claim was instead verified in Mo\\'in\\'s footnote'),\n]\nfor a,b in reps:\n    assert a in s, a\n    s=s.replace(a,b)\nopen(p,'w').write(s)\nEOF\npython3 -m json.tool page-501.json >/dev/null && echo OK; python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 501",
 "description": "Fix unverified page refs, validate, run checker"
}
```


### [2026-10-15T02:56:12.810Z] TOOL RESULT

```
OK
nodes verified: 21/21
node verdicts: {'plausible': 6, 'confirmed': 12, 'disputed': 3}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 18, 'partial': 5, 'contradicts': 2, 'not_checked': 10, 'not_found': 2}
books consulted: {'supports': 36, 'partial': 11, 'silent': 14, 'contradicts': 4} | by book: {'KLN': 7, 'AHD': 7, 'BRT': 6, 'CHEUNG': 5, 'PHD': 5, 'SKT': 5, 'HRN': 4, 'NYB': 3, 'POK': 3, 'WLD': 3, 'DEV': 2, 'IEC': 2, 'BQT': 2, 'KNT': 1, 'HUB': 1, 'ARY': 1, 'FSD': 1, 'HJB': 1, 'AID': 1, 'AFA': 1, 'LKT': 1, 'DOZ': 1, 'MON': 1, 'LAT': 1}
```


## [2026-10-15T02:56:23.637Z] TOOL CALL #89: SubagentHandback

```json
{
 "message": "I verified page 501 (book p.471), which has one entry: Ten 1, Tengh, Temp. All 21 nodes are covered. The checker `verify_check.py 501` reports 21/21 nodes and 0 PROBLEM lines.\n\nThe output file is `/home/sfmqrb/git/rishe-private/data/verification/page-501.json`.\n\n**Verdicts**\n- Root: confirmed. PIE *ten- is Pokorny 1065, *tengʰ- is 1067 and *temp- is 1064.\n- Nodes: 12 confirmed, 6 plausible, 3 disputed, 0 transcription_suspect.\n\n**Disputed**\n- **#7, English \"taffeta, tape, tapestry\":** taffeta (from Persian tāfta) is confirmed. Tapestry is plausible: Greek tápēs is traditionally Iranian, but Beekes calls it Pre-Greek. Tape is native Old English tæppe. Watkins puts it under a Germanic base tap-, and Wiktionary also says it is not Persian.\n- **#8, Avestan \"tauruna\":** the word \"young\" is real. But Pokorny (1070–71), Walde-Pokorny, Mann and Klein put it under *ter-/teru- \"tender\", not *ten-. Nothing supports the gloss \"stretched\". So the tar / tarāneh / tūleh / tūrah branch belongs under a different root.\n- **#14, Greek \"kithara\" from Persian târ:** modern sources reject this. Beekes calls the word Pre-Greek, and Homer has kitharis long before the Persian si-tār. Nourai is following Klein (KLN:687, \"fr. Pers. sihtār\").\n\n**Plausible nodes worth knowing about**\n- **#2 hanjâr:** Wiktionary derives it from Parthian anjār. Mo'in (BQT:2376) compares it with Sanskrit saṃcāra, so it is not securely from θanj.\n- **#5 tâbîdan:** it comes from Iranian *tāp- < *temp-, not from Avestan tan-.\n- **#10 tathra / thri-thatra:** both are unattested. tathra is the starred *tąθra- in Horn and Pokorny. thri-thatra looks like Nourai's own back-projection of si-tār.\n\n**Extraction errors:** none. The JSON matches the printed page image. The book itself prints \"KLN:572\", which is a misprint for KLN:1572 (Klein's tapestry entry). It also spells the same word two ways, \"tathra\" and \"thri-thatra\"; that inconsistency is in the book, not the extraction.\n\n**Sources:** 35 web pages were archived with `fetch_source.py`, all from Wiktionary, abadis/Mo'in and AHD; Etymonline did not load. Locally I used POK, WLD, AHD, IEC, KLN, SKT, BRT, KNT, CHEUNG, PHD, NYB, HRN, BQT (pages 70, 1481, 2376 and 2381), ARY, DEV and others."
}
```


### [2026-10-15T02:56:24.019Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
