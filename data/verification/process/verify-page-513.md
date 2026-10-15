# Verification process log — verify-page-513


## [2026-10-15T02:44:16.560Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 513 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-513.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-513.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-513.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 513` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.632Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:20.044Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:20.092Z] TOOL RESULT

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


## [2026-10-15T02:44:21.979Z] TOOL CALL #2: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/agent/charts/page-513.txt; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; ls data/verification/page-5*.json | tail -5"
}
```


### [2026-10-15T02:44:22.554Z] TOOL RESULT

```
=== PDF page 513 (book page 483) ===
--- entry 0 ---
ROOT [Indo-European] Tres, Ter 2 : to tremble  (refs POK:1095)
#1 (parent #0) [Avestan] refs=KLN:1592; HRN:86; NYB:172 | tras 1 : fear ; taršta, thrâsa : frightened
  #2 (parent #1) [Persian] refs=BQT:484; FFD:81 | tarsîdan «ترسیدن (ترس)» : to be afraid ; tarsâ «ترسا» : one who is afraid (of God), Christian ; harâsîdan «هراسیدن (هراس)» : to be afraid
#3 (parent #0) [Old Persian] refs=BQT:1197 | thrah : fear ; thrah-man, thras-man, čah-man, čath-man : afraid
  #4 (parent #3) [Persian] refs=BQT:1197 | sahm «سهم (سهمگین ، سهمناک)» : fear
#5 (parent #0) [Latin] refs=AHD; KLN | terěr : to frighten
  #6 (parent #5) [French] refs=None | terreur : terror
    #7 (parent #6) [Persian] refs=AMD:569 |  | extra: ترور ، تروریست ، تروریسم
  #8 (parent #5) [English] refs=None | terrible, terror, tremble, terrific
--- entry 1 ---
ROOT [Arabic] T.r.h : to throw  (refs FVA:247)
#1 (parent #0) [Arabic] refs=KLN:949 | tarh : a plan laid out for discussion ; matrah : place where something is laid
  #2 (parent #1) [Persian] refs=MON; FVA:246 | tarh «طرح (طرّاح)» : plan, idea, program ; matrah «مطرح (مطروح)» : set forth for discussion
  #3 (parent #1) [Italian] refs=None | materasso : mattress
    #4 (parent #3) [French] refs=None | 
      #5 (parent #4) [English] refs=None | mattress
--- entry 2 ---
ROOT Tronkus -> redirect to Trenk
--- entry 3 ---
ROOT Trp -> redirect to Terp
--- entry 4 ---
ROOT [Indo-European] Tu, Tŭ : you  (refs POK:1097)
#1 (parent #0) [Avestan / Old Persian] refs=POK:1097; BQT:525 | taiy, tŭ, tŭm, tuvam, tava, tvâm : you
  #2 (parent #1) [Persian] refs=BQT:525 | to «تو ۱» : you
  #3 (parent #1) [Sogdian] refs=SOD:383 | ty, tw : you
#4 (parent #0) [Germanic] refs=AHD | thŭ : you ; thŭmaz : yours
  #5 (parent #4) [English] refs=None | thou, thee, thy, thine
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
.rw-r--r--   60k sfmqrb 14 Oct 22:14  data/verification/page-55.json
.rw-r--r--   84k sfmqrb 14 Oct 22:14  data/verification/page-56.json
.rw-r--r--   58k sfmqrb 14 Oct 22:14  data/verification/page-57.json
.rw-r--r--   79k sfmqrb 14 Oct 22:14  data/verification/page-58.json
.rw-r--r--   75k sfmqrb 14 Oct 22:14  data/verification/page-59.json
```


## [2026-10-15T02:44:25.593Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls data/verification/page-51*.json data/verification/page-499.json 2>&1; sed -n 80,200p data/verification/sources/SOURCE_MATRIX.md; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


## [2026-10-15T02:44:26.821Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat tools/verify_check.py | head -150; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));\nfor k in ['POK','KLN','HRN','NYB','BQT','FFD','AMD','AHD','FVA','MON','SOD']: print(k, json.dumps(d.get(k),ensure_ascii=False)[:500])\""
}
```


### [2026-10-15T02:44:27.328Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   99k sfmqrb 14 Oct 22:14  data/verification/page-51.json
.rw-r--r--   49k sfmqrb 14 Oct 22:33  data/verification/page-499.json
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
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SBK.txt`

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFA.txt`
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD_pages.txt`
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_abdulraheem.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_mo3rb.txt`
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KFL.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt`
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAM.txt`
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DOZ.txt`
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AKD.txt`
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SIN.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
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

## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
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
```


### [2026-10-15T02:44:27.642Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed p
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g.
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qat
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is
AMD {"title": "Hasan Amid, Farhang-e Farsi-ye Amid, 2 vols, Amir Kabir 1369/1990", "kind": "website", "url": "https://vajehyab.com/?q=<word>&d=amid ; https://abadis.ir/fatofa/<word>/ (فرهنگ عمید) ; scan on noorlib: https://noorlib.ir/book/view/28973?pageNumber=<N>&viewType=pdf", "lookup_hint": "Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Entry-level verificat
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under t
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (re
```


## [2026-10-15T02:44:29.876Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/513.jpg; cat data/extracted/batch/page-513.json | python3 -c \"import json,sys;d=json.load(sys.stdin);print(json.dumps(d,ensure_ascii=False)[:4000])\""
}
```


### [2026-10-15T02:44:30.330Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   74k sfmqrb 14 Oct 22:15  site/pages/513.jpg
{"pdf_page": 513, "book_page": 483, "entries": [{"root": {"name": "Tres, Ter 2", "lang": "Indo-European", "refs": "POK:1095", "gloss": "to tremble", "note": "May be related to the root \"Trep:to tremble\""}, "nodes": [{"id": 1, "parent": 0, "lang": "Avestan", "refs": "KLN:1592; HRN:86; NYB:172", "words": [{"translit": "tras 1", "gloss": "fear", "script": null}, {"translit": "taršta, thrâsa", "gloss": "frightened", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 2, "parent": 1, "lang": "Persian", "refs": "BQT:484; FFD:81", "words": [{"translit": "tarsîdan", "gloss": "to be afraid", "script": "ترسیدن (ترس)"}, {"translit": "tarsâ", "gloss": "one who is afraid (of God), Christian", "script": "ترسا"}, {"translit": "harâsîdan", "gloss": "to be afraid", "script": "هراسیدن (هراس)"}], "script_extra": null, "note": null, "quote": {"text": "ای کریمی که از خزانهٔ غیب - گبر و ترسا وظیفه خورداری", "poet": "Sa`dî"}}, {"id": 3, "parent": 0, "lang": "Old Persian", "refs": "BQT:1197", "words": [{"translit": "thrah", "gloss": "fear", "script": null}, {"translit": "thrah-man, thras-man, čah-man, čath-man", "gloss": "afraid", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 4, "parent": 3, "lang": "Persian", "refs": "BQT:1197", "words": [{"translit": "sahm", "gloss": "fear", "script": "سهم (سهمگین ، سهمناک)"}], "script_extra": null, "note": null, "quote": null}, {"id": 5, "parent": 0, "lang": "Latin", "refs": "AHD; KLN", "words": [{"translit": "terěr", "gloss": "to frighten", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 6, "parent": 5, "lang": "French", "refs": null, "words": [{"translit": "terreur", "gloss": "terror", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 7, "parent": 6, "lang": "Persian", "refs": "AMD:569", "words": [], "script_extra": "ترور ، تروریست ، تروریسم", "note": null, "quote": null}, {"id": 8, "parent": 5, "lang": "English", "refs": null, "words": [{"translit": "terrible, terror, tremble, terrific", "gloss": null, "script": null}], "script_extra": null, "note": null, "quote": null}]}, {"root": {"name": "T.r.h", "lang": "Arabic", "refs": "FVA:247", "gloss": "to throw"}, "nodes": [{"id": 1, "parent": 0, "lang": "Arabic", "refs": "KLN:949", "words": [{"translit": "tarh", "gloss": "a plan laid out for discussion", "script": null}, {"translit": "matrah", "gloss": "place where something is laid", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 2, "parent": 1, "lang": "Persian", "refs": "MON; FVA:246", "words": [{"translit": "tarh", "gloss": "plan, idea, program", "script": "طرح (طرّاح)"}, {"translit": "matrah", "gloss": "set forth for discussion", "script": "مطرح (مطروح)"}], "script_extra": null, "note": null, "quote": null}, {"id": 3, "parent": 1, "lang": "Italian", "refs": null, "words": [{"translit": "materasso", "gloss": "mattress", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 4, "parent": 3, "lang": "French", "refs": null, "words": [], "script_extra": null, "note": null, "quote": null}, {"id": 5, "parent": 4, "lang": "English", "refs": null, "words": [{"translit": "mattress", "gloss": null, "script": null}], "script_extra": null, "note": null, "quote": null}]}, {"root": {"name": "Tronkus", "redirect": "Trenk"}, "nodes": []}, {"root": {"name": "Trp", "redirect": "Terp"}, "nodes": []}, {"root": {"name": "Tu, Tŭ", "lang": "Indo-European", "refs": "POK:1097", "gloss": "you"}, "nodes": [{"id": 1, "parent": 0, "lang": "Avestan / Old Persian", "refs": "POK:1097; BQT:525", "words": [{"translit": "taiy, tŭ, tŭm, tuvam, tava, tvâm", "gloss": "you", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 2, "parent": 1, "lang": "Persian", "refs": "BQT:525", "words": [{"translit": "to", "gloss": "you", "script": "تو ۱"}], "script_extra": null, "note": null, "quote": null}, {"id": 3, "parent": 1, "lang": "Sogdian", "refs": "SOD:383", "words": [
```


## [2026-10-15T02:44:32.615Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; pdftoppm -f 513 -l 513 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg513 && echo ok"
}
```


### [2026-10-15T02:44:33.561Z] TOOL RESULT

```
ok
```


## [2026-10-15T02:44:35.114Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg513.png"
}
```


### [2026-10-15T02:44:35.536Z] TOOL RESULT

```

```


## [2026-10-15T02:44:35.532Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-15T02:45:04.063Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'Root /lemma: (ters|tres|tu-|tu |t[uū]-)' POK_full.txt | head; grep -n -i -E '^ *(ters-|tres-|tu-|tū-|teue)' AHD_watkins1985.txt | head; grep -n -E '^(ter-|tres-|ters-|tu)' IEC.txt | head -20"
}
```


### [2026-10-15T02:45:04.418Z] TOOL RESULT

```
1082:ters-
1087:teue-. Also teu-. To swell. 1. Extended form *teuk- in Germanic *theuham, “the swollen or fat part of the leg,” thigh, in Old English théoh, thigh: THIGH. 2. Extended form *tis- in Germanic compound *thiis-hundi-, “swollen hundred,” thousand (*hundi-, hundred; see dekm), in Old English thisend, thousand: THOUSAND. 3. Suffixed zero-grade form *tu-l- probably in Germanic *thul- in Old English thol(l), oar pin, oarlock (< “a swelling”): THOLE PIN. 4. Extended zero-grade form *tiim- in: a. Germanic *thimoén- in Old English thima, thumb (< “the thick finger”): THIMBLE, THUMB; b. suffixed (stative) form *tum-é- in Latin tumére, to swell, be swollen, be proud: TUMESCENT, TUMID, TUMOR; DETUMESCENCE, INTU- MESCE, TUMEFACIENT, TUMEFY; C. suffixed form *tum- olo- in Latin tumulus, raised heap of earth, mound: TUMULUS. 5. Extended lengthened zero-grade form *tibh- in Latin tiber, lump, swelling: TRUFFLE, TUBER; PROTUBERATE. 6. Suffixed zero-grade form *tu-r-yo- in Greek turos, cheese (< ‘“‘a swelling,” “coagulating”’): BUTTER, TYROSINE, TYROTHRICIN. 7. Suffixed variant form *tw6-ro- in Greek sdros, heap, pile: SORITES, SORUS. 8. Suffixed variant form *twd-mn, in Greek sdma, body (< “a swelling,” “stocky form”): SOMA, SOMATO-, -SOME?; PROSOMA. 9. Suffixed zero-grade form *twa-wo- in Greek saos, sds, safe, healthy (< “swollen,” “strong”), with derivative verb sdzein, to save, rescue: CREOSOTE, SOTE- RIOLOGY. 10. Perhaps nasalized extended form *tu-m-b(h)- (or extended zero-grade form *tum-) in Greek tumbos, barrow, tomb: TOMB. [Pok. téu- 1080.]
715:tum; arma “arms”; armus, 1 (shoulder, arm, haunch’: Arm. armu-kn); Ir. cf. oirim (for *airim ?) ‘suit, fit’; Go. arms (i-stem m. ‘arm’); OE earm “arm, foreleg’; ON armr; Slovene cf. jérmen, m. ‘strap’; OCS jarímü (‘yoke’: Cz. jarmo, id.) beside rame, obl. ramen- “shoulder” (a:a). There is an apparent variant iar- (q.v.) represented by Tokh. AB yàárm, B yarm ‘measure’; Gk. hárma “team”; ON jor- muni *draught-animal
7966:turn'
13948:turn; OCS cf. za-klëpe, 3s. “locked, bolted `
14017:tur-, q.v. Skt. Catasr, Catasrí, id., W pedair, Br. péder, Cor. peder, f. id.
18411:ter- (3) (tero, ið) ‘rub, wear’. WP I, 728 Hitt. cf. tattar(ami), v. (^wipe' or sim.); Gk. teiro, v. ‘rub, wear, oppress, sadden’; Lat. tero, Ere, pf: trivi, sup. tritum, v. ‘rub, wear, waste’; Ir. cf. tairisce, m. ‘file’; Swiss cf. där, adj. ‘obstinate’; OCS tro, tréti, v. (and com. Sl. ‘rub, wear down"); R cf. terjàt molokó ‘stank — milk’; po-térja, f. loss, waste’; (long- gde in) OCz. tériti & Cz. tirat, inf. ‘persecute’; Li. terioju, oti, v. “torture”; (long-gde in) Latv. tereju, et, v. waste, consume’; (extn. in) Per. taraSam, idan, v. ‘scrape’
18412:ter- (4) (tero, io, eio) ‘turn, spin, bore’. Cf. terodhlom (terotrom). WP I, 728 Gk. teréo, v. ‘bore’; (o-gde in) tórnos ‘lathe’; Alb. Gert, aor: tora, v. ‘spin — cloth or bread, For W cf. ter, s. *pervasiveness' see terp- (1)
18441:ters- (terso) (1) ‘rub, dry’. WP I, 737 Skt. (z-gde) trsyami, v. ‘thirst (o-gde in) targah ‘thirst’; tarsitab, adj. ‘thirsty’; Arm. terem, v. scorch’. Kerestedjian); Gk. térsomai, v., térso (Alexandr. poets) “get dry”; tersaíno, tr. ‘dry’; (phonol. obscure in) Alb. ter, v. “dry, wipe’; Lat. cf. terra, f. (lit. ‘dry land"). For testa, f. see těgō above, not “tosta. . .torre(0). Ainsworth, 1736); Olr. (Gei tirim, tírm, adj. “dry”; tírad, inf. ‘to dry’; Go. ga-pairsan, v. ‘parch’; ON perra, v. ‘dry, wipe’. Nominal forms in OLat. tersus, adj. (“fine — of weather. Fest.) beside terra, f. ‘earth’; Osc. terüm, tee- rúm, n. ‘land’; MIr. tír, m. id.; tirim, gsf: tiorma, adj. (‘dry’, fr. *tersimos); OBr., W tir, m. “land”, pl. -oedd in W. (fr. *tersos, -eos, n.); Cor. tyr, pl. -yow, m. id.; ON perra, f. (towel, lit. *drier); Cz. cf. ü-térka, f. dim. ‘duster, wiper’. (The Arm. form terem is doubtful in the initial, cf. next)
18442:ters- (2) (tersó), variant of type tres, q. v. ‘tremble’. WP I, 760 & trs- (2) Av. taros-, v. id.; Per. tarsam, 1dan, v. ‘fear’; tars, s. “fear”; tarsü, adj. ‘fearful’; Oss. türság, ‘fearful and Grein. v. ‘fear’; tas, s. (sic) ‘fear’; Hitt. cf. (?) tarr(ami), v. (queried: ‘tremble’, but the cluster -rs- occurs elsewhere); Lat. terreo, ere, v. ‘frighten, scare off; OCS cf. trésto, iti, v. ('shake', fr. *tersK-), cf. trásnü,
18542:ter-, radical: “through, over’. Cf. tr- and extns. R-gde in Skt. tirás, prp. & adv. “across, over'; tirayami, v. (3) ‘pervade’; W tarad, m. 'pervasion'; Ir. tar, prp. w. acc. ‘across, through’. Cf. Lat. tar- mes, m.
18919:tres- ‘fringe, border OE pras, s. id.; Cz. cf. třáseň & trásné, f. sg. & pl. ‘fringe’; Slovak cf. triesma, f. id. (and ‘tassel’. Cz. vocalism infl. by tfást, v. 'trem- ble’. Li. tresai, mpl. ‘fringe, braid? seems to be a LW fr. G Tresse, fr. French)
19212:tu, tū ‘thou’. (Oblique forms in Skt. & Olran.). WP I, 745 Per. tu, tü, id.; Oss. dí (by weak sentence position); Arm. du (W.S.P), id.; Tokh. A tu; B tuwe, twe; Gk. sú, Dor. tá; Osc. cf. tiu, tiium, id.; Ir. tà; W ti; Br. té; Cor. ty (W.S.P. sý, Ip = ÉD; Lat. tü; Go. bu, OE bú, MHG dü; ON bú; OCS (and com. SL) ty; Li. Latv. tu. Oblique forms in Skt. tvam, Av. tüm & OPer. tuvam, id.
19213:tu- (radical “care, watch") in Gk. cf. a-sü-phelos (écontemptuous' or sim. but ambig. cf. dhubh- (3)); Lat. cf. as-tus, gs: -tüs, m. ‘craftiness’; as-tütus, adj. ‘crafty’ (fr. *ad-tu-); tueor, tueri, v. ‘watch’; OCz. tba, f. “heed”; assim. in Pol. dbaly, Ukr. dbalyj, adj. ‘concerned, careful; Cz. cf. ne-dbaly, adj. («careless': Gk. -süphelos). (NB. OE dybbian, v. “heed? points to a type dhubh-)
19224:tubho, io. Cf. dhubh- (1) Skt. cf. tubhyami, v. “hurt, kill (distinct from dhubh- (1), q. v.); Ir. tobhaim, v. “force; pes- ter
19225:tubhoi, tubhio-, oblique theme of type tu, tü in Skt. tubhyam, ds.; cf. OCz. & Cz. tobé, id.
19227:tud- (tudo, ið) (1) ‘strike’. Cf. tund- and extns. below. WP II, 618 Skt. tudámi, v. id. (and ‘pound; sting; goad’); pp: tunnáh; Alb. tus, v. ‘brandish, rock’; OIr. cf. do-tuit, 3s. (fall, ambig. cf. tup-?); G dützen, v. ‘thrust, cram’
19228:tud- (tudo, io) (2) ‘scare’. WP II, 616 Gk. cf. a-tàzomai, v. ‘be astonished'; Alb. tus, v. (1) ‘scare’; Ger. cf. ver-dutzen, v. ‘startle, stupefy’; LG cf. in dutten scheiten, v. ‘scare’; Du. cf. dut, m. ‘stupor’; Srb. cf. (*-eu-) ĉu- dati se, v. ‘be scared; shy’
19229:tudorio (tudurio, radical: tud-) 'din, re- sound'. Arm. ambig. Cf. WP II, 618 Arm. cf. (Gem, v. (*fart', ambig., cf. düduro & durdurð); Lat. cf. tuditó, are, v. ‘thump’; OE poterian, v. ‘how? beside ge-pot, n. id. Ono- mat.
19230:tudmn- (1) (tudmo-, teudm- or toudm-, radi- cal: tud-) “beat, bang’. Cf. tudno- W twddf, pl: tyddfan, m. ‘punch, poke’; Ir. cf. tuaim, f. (1) ‘noise’. (NB. Gk. támma, n. “blow, wound? is from *tupmn-, see tup-)
19232:tudnos, à “strike, blow; striker; striking’. WP II, 618. Cf. tud-, tund- and extensions. (Cel-
19235:tudos, is 5jolting, noisy, projecting; noise, jolt, projection'. Cf. tud- w. extns., and tund-. WP II, 618 Skt. tudah, adj. ‘striking, thrusting, goading’; Lat. tudes, gs: tuditis, and tudis, s. (m. or f.) ‘tammer, hammer’; OE ge-pot, n. ‘din’; ON pot, n. ‘onset, impact’; pytr, m. ‘din’; MHG dus, gs: duzses, sm. ‘din’; Go. cf. put-haürn, n. ‘trumpet; W twdd, m. ‘excrescence’. A cpd. of type *tud-ped- arises in OE poft(e), f. ‘thwart, rowing-bench'; ON bopta, f. id.; EMDu. doft, id. Other synthetic cpds. of simi- lar construction arise in Ir. tota, m., Br. tóst, m. as OE; LG Ducht, f. (2) ‘thwart, bank of oars'. Cf. tudst-
```


## [2026-10-15T02:45:06.912Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'Root /lemma: (tres|ters|tu|tū)' POK_full.txt; sed -n 1080,1086p AHD_watkins1985.txt | cut -c1-1500; grep -n -E '^tu\\.' AHD_watkins1985.txt | head; grep -n -E '^(tu|tŭ)[-. ]' AHD_watkins1985.txt|head"
}
```


### [2026-10-15T02:45:07.371Z] TOOL RESULT

```
87698:Root /lemma: tuak-1, tuk- 
87808:Root /lemma: tuer-1: /it//"- and tuf- 
warp threads are stretched on the loom): TAFFETA; b. Iranian *tap-, “carpet,” in Greek tapés, carpet: TAPES- TRY. [Pok. temp- 1064.] ten-. To stretch. I. Derivatives with the basic meaning. 1. Suffixed form “ten-do- in: a. Latin tendere, to stretch, extend: TEND!, TENDER?, TENDON, TENSE!, TENT!; AT- TEND, CONTEND, DETENT, DISTEND, EXTEND, INTEND, OSTENSIBLE, PRETEND, SUBTEND; b. Latin portendere, “to stretch out before” (por-, variant of pro-, before; see per’), a technical term in augury, “to indicate, presage, foretell”: PORTEND. 2. Suffixed form *ten-yo- in Greek teinein, to stretch: TENESMUS; BRONCHIECTASIS, EPITA- SIS, HYPOTENUSE, PERITONEUM, PROTASIS, TELANGIEC- TASIA. 3. Suffixed zero-grade form *tn-nu- in Sanskrit tandéti, he stretches or weaves, with suffixed (instrumen- tal) derivative *ten-tro- in tantam, loom: TANTRA. 4. Suf- fixed form *ten-tro- in Persian ¢tdr, string: SITAR. 5. Basic form (with stative suffix) *ten-é- in Latin ten��re, to hold, keep, maintain (< “to cause to endure or con- tinue, hold on to”): TENABLE, TENACIOUS, TENACULUM, TENANT, TENEMENT, TENET, TENON, TENOR, TENURE, TENUTO; ABSTAIN, CONTAIN, CONTINUE, DETAIN, ENTER- TAIN, LIEUTENANT, MAINTAIN, OBTAIN, PERTAIN, PERTI- NACIOUS, RETAIN, (RETINACULUM), SUSTAIN. II. Derivatives meaning ‘‘stretched,” hence “thin.” 1. Suffixed zero-grade form *tn-u- in Germanic *thunw-, whence *thunniz in Old English thynne, thin: THIN. 2. Suffixed full-grade form *ten-u- in Latin tenuis, thin, rare, fine: TENUOU
70
ters-
thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (>
teu-
LOUS, TERRIGENOUS, VERDITER. 3. Suffixed o-grade form *tors-eyo- in Latin torrére, to dry, parch, burn: TOAST!, TORRENT, TORRID. 4. Suffixed zero-grade form *trs-o- in Greek tarsos, frame of wickerwork (originally for drying cheese), hence a flat surface, sole of the foot, ankle: TaRSUS. [Pok. ters- 1078.]
teu-. To pay attention to, turn to. 1. O-grade form *tou- in Germanic *thau- in Old English théaw, usage, custom (< “observance”): THEW. 2. Suffixed zero-grade form *tu-é- in Latin tuéri, to look at, watch, protect: TUITION, TUTOR; INTUITION. [Pok. 2. teu- 1079.]
```


## [2026-10-15T02:45:09.754Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'Root /lemma: *(ter|tre|tu|tū)' POK_full.txt | head -40; grep -n -E '^(tres|ters|tu)[-.0-9 ]' AHD_watkins1985.txt | head"
}
```


### [2026-10-15T02:45:10.162Z] TOOL RESULT

```
85996:Root /lemma: ter-3, tera-and ten-, tn- 
87698:Root /lemma: tuak-1, tuk- 
87808:Root /lemma: tuer-1: /it//"- and tuf- 
1082:ters-
```


## [2026-10-15T02:45:11.966Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'Page\\(s\\): *(1095|1096|1097|1098)' POK_full.txt | head; grep -n -i 'zittern' POK_full.txt | head -20"
}
```


### [2026-10-15T02:45:12.460Z] TOOL RESULT

```
87487:Page(s): 1095-1096 
87646:Page(s): 1096-1097 
88023:Page(s): 1097-1098 
41455:zitternde Bewegung, in Aufruhr geraten ', Old Lithuanian yi/o'i/s "quarrelsome', yi/o'/'a 
70154:Gothic reiran {scVwN . V.) "tremble, quiver', re/AD'Zittern, Erdbeben'. 
87237:peaceful ', arpepn^ 'fearless', rpoijoc; m. 'das Zittern', TpopEU) 'tremble', i^o\xz^6c, 
87249:Latin tremo, -e/ie 'tremble', //'e/77c»/''das Zittern', //'e/77i//i/5 'trembling', Umbrian tremitu 
87258:Lithuanian //7/77//"erzittern', //'e/77//"niederstoR)en; verbannen, austreiben', sutraminti 
87373:Old Church Slavic //'e/0e/b"das Zittern, Beben', //'eyoe/5//"tremble', //'(9y05//"palpare', 
87419:"makes erzittern'; Avestan tarsta- {kryau *trsta- "timorous'), tarssaiti, ap. /^/^^///"furchtet' 
87423:Armenian erer^ tremor, Beben, Zittern' {*tres-ri-)\ 
87432:trasana-m^e\ne bewegliche, zitternde ornament, decoration'); 
87434:Lithuanian //7Si/ "tremble' {*trs-[s]Rd)\ Latvian trisasi. PI. "Zittern', //7se/ 'tremble, quiver', 
89454:"Zittern, intense Bewegung, rush', Avestan vaeg- (vaejd-) "(a projectile) swing', vaeya-m. 
89858:"in schwingender, zitternder Bewegung sein, toss, fling, schlingen, umwickein'. Old English 
89878:Latin vibro, -are"\n zitternde, schwingende Bewegung place, sich trembling bewegen'; 
91749:Kz/'yOi/Zj/s 'Zittern the Glieder', and with the development to 'drehend toss, fling, throw,
```


## [2026-10-15T02:45:14.069Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 87405,87445p POK_full.txt; echo ======; sed -n 87640,87700p POK_full.txt"
}
```


### [2026-10-15T02:45:14.683Z] TOOL RESULT

```
Exit code 1



See also: see above S. 1037 under (s)trep-. 
Page(s): 1 095 



Root / lemma: tres- tens- ( *teres-) 

Meaning: to tremble 

Material: Old Indie trasati^ trembles ' (= gr. Tpsw), //-as/a- 'trembling' Kaus. trasayati 

"makes erzittern'; Avestan tarsta- {kryau *trsta- "timorous'), tarssaiti, ap. /^/^^///"furchtet' 

( *trs-[s]Rd) = Lithuanian tr/su); Kaus. Avestan t^rarjhayete "versetzt in fright'; perhaps 

Armenian erer^ tremor, Beben, Zittern' {*tres-ri-)\ 

Latin terreo, -ere^\v\ Schrecken versetzen, daunt, scare' (das e instead of kausativen o 
derives from:) /e/ro/'" fright'; Umbrian turs/tu ^terreto, fugato'; 

gr. Tpsu) (Aor. hom. Tpsaaai) "tremble, flee', STspasv z(p6^r\ozv Hes., aTp£aTO(; 
"unerschrocken', Tpr|p6(; (*Tpaap6(;), Tpnpwv "timorous, fleeting '; 

Middle Irish /a/rac/? "timorous' {*trs-ako-)\ Old English d^^s 'fringe' (compare Old Indie 
trasana-m^e\ne bewegliche, zitternde ornament, decoration'); 

Lithuanian //7Si/ "tremble' {*trs-[s]Rd)\ Latvian trisasi. PI. "Zittern', //7se/ 'tremble, quiver', 
perhaps Lithuanian tresiu, //lesZ/'laufig sein'. 

References: WP. I 760, WH. II 674 f., Trautmann 329; 
See also: to 1 . ter-V wriggle '. 
Page(s): 1 095 

Root / lemma: tr-eu-d- 

Meaning: to press, push, * displeasure 

Note: probably extension to ter-3, tereu-^xub' 
(eval):1: ===== not found
```


## [2026-10-15T02:45:17.359Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'lemma: tu' POK_full.txt | head; awk 'NR>=88000 && NR<=88060' POK_full.txt | grep -v '^ *$' | head -50"
}
```


### [2026-10-15T02:45:18.961Z] TOOL RESULT

```
87648:Root / lemma: tu, tutu 
87664:Root / lemma: tuak-2 
87682:Root / lemma: tuakos 
87698:Root /lemma: tuak-1, tuk- 
87723:Root / lemma: tue/-2, extended tuei-s- 
87762:Root / lemma: tuengh- 
87782:Root / lemma: tuen- 
87790:Root / lemma: tuerR- 
87808:Root /lemma: tuer-1: /it//"- and tuf- 
87885:Root / lemma: tuer-2 : tur-, tuera- 
Material: 1. Old Indie tu, tu'yeV (zur hervorhebenden and auffordernden particle has 
changed), Avestan tu6s., enkl. 'du'; Aryan */^i/-a/77 (after Old Indie aham) in Old Indie 
tuvam, tvam, Gatha-Avestan /i/a/T?, iav. turn, ap. tuvam ^du'; Armeniano'^'du'; 
gr. Doric tu, hom. Ionian Attic au (a- from the Kas. obi., where a- from tF-), hom. Tuvr), 
lak. Touvri, Boeotian touv (after sycb-v, -vr|); alb. t/{*tu); Latin tu. Old Irish tu{*tu or *tu), tu- 
ssu, -sso{*tu) 'du', cymr. //etc. {*tu); Gothic l=>u. Old Icelandic t^uaud suffix l=>u, l=>o. Old 
Saxon thu. Old High German du, du, Lithuanian tu{*tu or *ti7?). Old Prussian tou{*tu) 'du'; 
Old Church Slavic ty, Tocharian A tu, B t(u)we, Hittite zik, z/Ma^6u'{*tegairom *te+ *egd), 
tuk, tukka 'dir, you', enclitic -du- {*tu) and -ta {*te or *to/} 'dir, you'; 
2. Indo Germanic *teue- 'dein', Celtic *toue\r\ Old Irish toT, mcymr. /ei/'das Deinige', 
preceding Celtic *tou> Old Irish o^o'dein', cymr. dy, corn, the, bret. da 6s:, Hittite -ti- 'dein'. 
3. Possessivum teuo-s, tuo-s:0\6 Indie tva-h, Gatha-Avestan -dwa-, Avestan tava-, hom. 
Ionian Attic obc, (*tF6(;), hom. Lesbian Doric reoq, Boeotian ^\oc, (*t£F6(;); alb. y-t, Akk. ten-t 
(Verschmelzung of article with dem Poss.); Latin /^^5(from *tovos), Umbrian tover'tuV, 
Oscan tuva/ ^tuae'; Lithuanian tavas. Old Church Slavic tvq/'b. 
References: WP. I 745, WH. II 712, Trautmann 315, 331, Jackson Lang and Hist. 657, 
Mayrhofer 1, 507, Vasmer 3, 102 f., Pedersen Hittitisch p. 58. 
Page(s): 1097-1098 
Root / lemma: ub- 
Meaning: to drag, press 
Material: Old Indie ubJat/'haW. low, base, presses together', Avestan ubjya/te'mrd 
niedergedrijckt (auf the Wage)'; 
Prussian-Lithuanian ubyt/'zur haste, hurry urge, press, push'. 
References: WP. 1193 f., Mayrhofer 1, 107. 
Page(s):1103 
Root / lemma: udero-, uedero- 
Meaning: belly 
Material: 1 . Old Indie udara-m ^beWy, intumescence of Leibes, the thick Teil eines Dinges, 
cavity, the interior', anudara- 'bauchles', Avestan udara-^s.\ gr. 65£po(; yaarrip Hes. 
(because of Asper rather for *u5£po(;); Latin uterus^\ower abdomen, belly, esp. womb, 
uterus' (/for o^am ehesten zugleich with dem phonetic alteration from *udris^\\ose' to 
*utris, ^/eAeingetreten); Old Prussian weders^beWy, stomach', Lithuanian vedaras^ 
intestines, entrails offish, intestines, entrails; Wurstmagen', Latvian veders, vedars^bQWy, 
stomach'; 
zur preposition ^o'belong perhaps gr. uaTO(; yaoTrip Hes. (*^o'-s/c»-s "vor-stehend') and 
UGTspa 'womb, uterus' {ud-^ compounds-suffix tero). 
2. Latin venter, -//7S 'belly' (could be *uend-ri-). 
3. Latin ve(n)sTcai. 'the bubble'. Old Indie vastf-m. 'bubble, bladder' {*undt/-7); 
1/5/7/5//?^- 'Mastd arm, or ein in the Nahe of Netzes liegender Korperteil'; compare 
nvuarpov 'Labmagen', Old High German wan{a)st, i4/^/7/s/' paunch'. Modern High German 
Wansta\so ' psalterium ', ablaut, isl. v/nsfrt ' psalterium ', Norwegian dial, v/nstrt 
'Labmagen' {* uen/strd); compare also Liden KZ 61, 19 ff.
```


## [2026-10-15T02:45:22.479Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'tars|haras|harās' CHEUNG.txt | head -30"
}
```


### [2026-10-15T02:45:22.893Z] TOOL RESULT

```
9940:*NEIR: Yghn. rus-/rüsta ‘to flow, stream; to fall [of stars]’ (-3- < old. aor. ?), Yi. 
10830:(of sun, stars, sim.)’ = Samadi: 227, 54 f., 6, 226 
24959:*AVESTAN: YAV. tarsna- (m.) ‘thirst’ (V 7.70, Yt 19.69, Yt 19.96, etc.) 
24995:*SANSKRIT: tars ‘to be thirsty’ (R V+), tfsnä (f.) ‘thirst? (RV+) = EWAia I: 635 F. 
24998:*IE COGNATES: Gr. tépoopat ‘I become dry’, Hitt. /tars-/ ‘to dry’, Lat. torrére ‘to 
25584:*MIDDLE PERSIAN: MMP tyrs-, ВМР tls- (DHLLWN-) /tars-/ ‘to fear = DMMPP: 
25587:Pres.: IND. 3sg. BMP tlsyt /tarséd/, 2pl. MMP tyrsyd, 3pl. MMP tyrsynd, MMP tyrsynd, SUBJ. 2pl. 
25588:MMP "tyrs’d, IMPV. 2sg. BMP tls /tars/, 2р1. BMP tlsyt /tarsed/; Partic.: perf. pass. II MMP tyrs’d, BMP 
25589:tlsyt /tarsid/ 
25603:*NWIR: NP tarsidan/tars- ‘to fear’, NP sahistan/sah- (< OP *саһ- < Ir. *@rah-), 
25605:Kurd. tirsin/tirs-, Zaz. tersäyis/tersen-, Awrom. tarsay/tars- ‘to be afraid’, Abyan. 
25606:tarsoya/tars-, Abz. tarsowa/tars-, Gz. társ-/társa, Gil. társoen/társ-, Gur. (Kand.) tärs-/ 
25607:-tärs-, Ham. tarsayän/tärs-, Khuns. ters-/tersa, Mah. tirs-, Nn. tarsay-/tars-, Natan. 
25613:-tärs-, Qohr. tarsäda/tars-, Shamerz. -tärsi-/tarsam-, Siv. ters-/terse, Semn. -tärsäf-/ 
25614:-tärs-, Sorkh. -tars-/tars- ‘to fear, be afraid’, Gz. türsn-/társna ‘to scare’, Siv. 
25615:tarsenayän/tärsen-, Sorkh. -tärs-/tärs-, Lasg. -tars- ‘to fear’. © To Bal. tursit/turs- is 
25619:*NEIR: Oss. I. taersyn/tarst, D. tærs-/tarst ‘to be afraid’, Pash. taxtedal ‘to flee’ = text- 
33777:tarsna-, 383 
35636:tls- /tars-/, 393 
37973:harays-, haras-, 197 
41599:tarsidan/tars-, 393 
43002:tarsáy/tars-, 393 
43391:tarsowa/tars-, 393 
43484:tarsoya/tàrs-, 393 
44007:tarsayán/társ-, 393 
44698:tarsay-/tars-, 393 
44909:tarsada/tars-, 394 
45379:-tars-, 394 
45643:-tars-/tars-, 394 
45687:-társí-/tarsam-, 394
```


## [2026-10-15T02:45:24.259Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25560,25640p CHEUNG.txt"
}
```


### [2026-10-15T02:45:24.635Z] TOOL RESULT

```
*SANSKRIT: tyaj ‘to leave, dismiss, abandon’ (RV+) = EWAia I: 673 f. 

© It is uncertain whether all these Ir. forms cited here are related to each other. Some 
of them may be indeed related to tyaj ‘to leave, dismiss, abandon’ (R V+), EWAia I: 


673 f. 
*REFERENCES: Abaev, Slovar’ III: 292 f.; Steblin-Kamenskij 1999: 367 


*Orah (*trs) ‘to shake, tremble; to fear; to flee’ 

*AVESTAN: YAv. Oränh- (taras-) ‘to fear’ || (+ *abi-) caus.‘to scare hither’ || (+ 
*pati-) caus. ‘to scare thither’ || (+ *fra-) ‘to be(come) afraid (of)’ = Liste: 25 

Pres. inch.: IND. 3sg. YAv. fratorosaiti (Yt 10.97, Yt 10.134, Vyt 27, Aog 19), 3pl. YAv. tarasanti (Yt 
14.38), SUBJ. 3pl. YAv. fratorosan (Yt 11.6), IMPV. 3pl. YAv. torosentu (Yt 14.38); Caus.: pres. IND. 
med. Zeg. YAv. 6rághaiiete (Yt 10.101), YAv. auui.Oràghaiiete (Yt 10.41), YAv. paiti.Oranhaiiete (Yt 
10.41) 

*OLD PERSIAN: f(a)rs- ‘to fear’ > Kent: 186a 

Pres. inch.: IND. 3sg. t(a)rsatiy <t-r-s-t-i-y> (DPd 11), 3pl. t(a)rsa"tiy «t-r-[s]-[t]-[i]-y» (DSe 38), impf. 
3sg. at(a)rsa <a-t-r-s-> (DB 1.50), 3р1. at(a)rsa" (DPe 9), INJ. Isgt(a)r. sam «[t]-r-s-m» (DPe 21) 
*MIDDLE PERSIAN: MMP tyrs-, ВМР tls- (DHLLWN-) /tars-/ ‘to fear = DMMPP: 
332b 

Pres.: IND. 3sg. BMP tlsyt /tarséd/, 2pl. MMP tyrsyd, 3pl. MMP tyrsynd, MMP tyrsynd, SUBJ. 2pl. 
MMP "tyrs’d, IMPV. 2sg. BMP tls /tars/, 2р1. BMP tlsyt /tarsed/; Partic.: perf. pass. II MMP tyrs’d, BMP 
tlsyt /tarsid/ 

*PARTHIAN: tyrs- ‘to be afraid’, ’hr’s- (caus.) ‘to fear, frighten’ = Ghilain: 75 | 
DMMPP: 332b 

Pres.: IND. 3pl. tyrsynd, SUBJ. 2sg. tyrs’h; Partic.: perf. pass. II tyrs’d 

*SOGDIAN: SSogd. trs, CSogd. ts ‘to flee’ (Sims-Williams 1976: 58) 

Pres.: IND. 2pl. CSogd. Gr, 3р1. SSogd. tr$’nt, IMPV. 25р. SSogd. më Pret: IND. 3sg. CSogd. "tsty 
(Schwartz 1967: 46) 

*CHORESMIAN: (+ *ni-) m[nc- to fear’ © Samadi: 121 f. 

*NWIR: NP tarsidan/tars- ‘to fear’, NP sahistan/sah- (< OP *саһ- < Ir. *@rah-), 
hirasidan/hiras- ‘to fear, dread’ (< Pth.), NP sah(i)m ‘terror, dread’, Bal. tursit/turs-, 
Kurd. tirsin/tirs-, Zaz. tersäyis/tersen-, Awrom. tarsay/tars- ‘to be afraid’, Abyan. 
tarsoya/tars-, Abz. tarsowa/tars-, Gz. társ-/társa, Gil. társoen/társ-, Gur. (Kand.) tärs-/ 
-tärs-, Ham. tarsayän/tärs-, Khuns. ters-/tersa, Mah. tirs-, Nn. tarsay-/tars-, Natan. 


394 *0raH 


-tärs-, Qohr. tarsäda/tars-, Shamerz. -tärsi-/tarsam-, Siv. ters-/terse, Semn. -tärsäf-/ 
-tärs-, Sorkh. -tars-/tars- ‘to fear, be afraid’, Gz. türsn-/társna ‘to scare’, Siv. 
tarsenayän/tärsen-, Sorkh. -tärs-/tärs-, Lasg. -tars- ‘to fear’. © To Bal. tursit/turs- is 
perhaps also connected Bal. drah-/drahit ‘to shiver’, with old *@ being replaced 
(early) by d- of draps- ‘to tremble’ (*drafg). 

*NEIR: Oss. I. taersyn/tarst, D. tærs-/tarst ‘to be afraid’, Pash. taxtedal ‘to flee’ = text- 
eg-/-ed-, (Waz.) tast-/ta$-, tost-, (Wan.) test-/ters-, ? tarhedol ‘to take alarm, be 
terrified, wince (about animals)’ = tarh-eg, Yi. Xüróx-/Xüróxt, M. Xiréx- (denomin.?) 
‘to shy’ || (+ *us- ?) Wa. wes(o)y-/wost- ‘to be afraid’, (caus.) was(b1)Vv-/wasovd- ‘to 
fear’, wasvik ‘fear’. Q The Pash. form tarh-eg is rather a borrowing from 
Indo-Aryan, cf. Lah. tarahan ‘to be timid’, Si. trahanu ‘to shy’, according to 
Elfenbein, apud NEVP: l.c. 

*MISC: (+ *ui-) Orm. yus-/yusök, ywas -/ywas ek ‘to fear’ = go`š-/go`šók 
*SANSKRIT: tras ‘to tremble, quiver, shrink from, be afraid’ (RV+) © EWAia I: 678 
«PIE *tres- ‘to tremble, be afraid’ = LIV: 650 f. | Pok.: 1095 

*IE COGNATES: Gr. трёо ‘to be scared, tremble, flee’, Lith. triséti ‘to tremble, 


shiver’, etc. 

«REFERENCES: KPF I: 80a, 136a, 205b; EVP: 82 f., КРЕП: 189; IFL I: 396b; Christensen, Contributions 
I: 61, 256; IIFL II: 550a, 271a; Christensen, Contributions II: 52, 112, 156; Abrahamian 1936: 121; 
MacKenzie 1966: 110; EVS: 101b; WIM I: 73; Abaev, Slovar’ III: 273 Ё; WIM II/1: 84; WIM III: 117; 
Werba 1997: 349; Cabolov 1997: 74; Paul 1998: 315b; Steblin-Kamenskij 1999: 400 f.; Kiefer 2003: 198; 
Lecoq 2002: 122, 125, 127 (passim); NEVP: 83 f.; Korn 2005: 316, 364
```


## [2026-10-15T02:45:31.344Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'tar[sš][tš]a|taršta|tarsta' BRT.txt | head; grep -n -E 'tares-|tar[eə]s-' BRT.txt | head; grep -n -i -E 'θrāh|ϑrāh|Orah|ϑräh|9rah' BRT.txt | head"
}
```


### [2026-10-15T02:45:32.263Z] TOOL RESULT

```
3835:•  j.  aiwi'9ätö.tarstay-  Adj,  (auch  mask.) 'dem  Schrecken  beigelegt,  beigesellt  ist, schaudererregend  (durch  HässUchkeit)' : aspahe  'isis  (GSm.)  YtS.zi.
4524:•  '}.  an-usant'  Adj.  (fem,  •saitt-)  'der (etwas)  nicht  (tun)  will,  widerwillig,  ohne CS  zu  wollen':  ndit  mam  vTspe  yazatat>hs •Sf/ttfm  fraerscinta  "nicht  mich  gegen meinenWillen.."Yt  i7. 19;  19;  —  v?r3zyjt usaitica  *°ja(//Vfl(NSf.)''"..  mag  sie  wollen oder  nicht"  N.  6\  —  virszylt  usaiti  (sd.) neu  *'saili'^  N.ö;  — yat  ■j^(NS.)  vi/yei- tii'aisA.)..  M.S.  a6.  a)  "jiJNSm.  alsAdv.J» 'widerwillig':  'sS..  avat  kvar»  ätäpaite{i^) •tJ  h-tu  ma  °s5  ave  stärB  V.9.41;  — frä ahmät  parö  vlspe  daiva  'SS  tarsta  mmanle Y.  57. 18.  o)  sva,  'mit  Gewalt':  vaim>m (sd.)  's5  pai'iy3ife^.4.i,^;  53.
12117:•  j.  tarSta-  Adj.,  PPfP. :  s.  '^rah-.  [Yt I,  101:  lies  ha%raj'\
12120:j.  tarstay-  t  'Schrecken,  Furcht
13976:'gehen,  eilen;  sich  aufinachen':  advannta (Augm.)  adäunta  deteva  V.  ig.  45;  —  druxs dvarai  Yt  ^.  1 7 ;  —  patrika  .  .  Äisiöyät aca  paraia  dvaraili  (NSf.)  ".  .  hin  und wieder  gehend"  Yt  8.  54.  a)  mit  An- gabe des  Zieb;  a)  durch  Akk.:  advannta (Augm.) . .  dalva  . .  ^bunsm  ankSuS  Umaa- hahe  V.ig.4T,  —  als'a  vff  dvaraiti  boi- yqsta  "es  macht  sich  (sonst)  B.  zu  euch auf'  V.  18.  16.  P)  durch  Gen.  (?,  Sp. 649  o.):  vispe  dafva  .  .  tarsta  t?mat>hs *dvarynle''>  Y.  57. 1 8,  Yt.  g.  4  (wo  dvaränte).
16988:—  tä  (aimi. /ravasays)  el  starsta^  'möhu saoyä  Yt.  y.  a  7 ;  —  ys  'maca  ^frastfrinte gSulca  paitiiaraiti  ti.6o;6o;  —  %risum 'ma  frastjritmyA  paitila  hü  a^wansm  Yt. 12.  3;  —  ys  .  .  rapiUwiftfin  . .  fräyasäite
26645:a/sH^ra ..Slam  zjmasa^ra  ..  slärB  urvarS.-  •  j.  Starstaeii- f.,  Plur.  Bezeichnung  eines a^ra  S.2.13;  ¥1/2.28—31;  —  stäram\zara  Lager  fiir  Tiere  geeigneten  weichen aßci^ranqm  YtÄ  39;  S.1. 13.  a)  von  und  wannen  Stoffs:  upjia  hl  (nämL  der bestimmten  Sternen  uod  Sternbildern:  >  säugenden  Hündin)  gJtam  iaray»i  {stL) lisirlm  (sd.)  Uänm  razvantgm  *3fanna-  •  tumS.vantshva  (sd.)  kamcit  vä  'Üttam  V. nhuntim   YLÄ  a;  i,  3,  50,  12,27,  18.  5,  7, '  ij.  43.
4250:Pü.;  aiar;  (zu  »«);  aaerätt'},  s.  unter  'raorah'. —  >)  GelW. }.  BHOxtÖ  N,  ^ :  lies  anakaxli.
8547:yiin  . .  bloa  'CJ  zbayeiti  avaitihe  Yt  IQ. 83-86';  53,  73;  —  ahyä  yäi3  mmauhä 'tö  ra/jorahya  (sd.)  Y,  2$,  i  '*;  —  mal  vi padaU  . .  pairijasäi  .  .  'tS  .  .  n?matihä Y.50.8-'.
13952:mit  afa  Inkoh.  'sich  zum  Rüg  erheben (in  der  Richtung)  nach  -  weg'  (Dat.):  aiia druxl  yä  nasul  apaJvqsaiti  apäx?oraHbyS nalmaHbyS  V.  8.  1 6.
16030:38.  2;  *y.  1";  —  rrvlm  *'älm''>  yazamaide Vr.  7.  a.  a)  sonst  mit  raf^raäJ-:  mihnm . ,  yim  halaite  aiil .  .  'di(SS.)ea  raora%a YtiO.66;  Ä38,  *Vyt<?;  —  •älm  raorahqm S.2.as;~  •dyA{GS.)  raorakaya  S./.äs. *}  Ober  deren  Bedeutung  Sicheres  nicht  zu ermitteln  ist;  vgl.  die  GrB.-Slelle  bei  Dst.  ZA. 2,  3:1,     Meist  erscheint  sie  in  Verbind ung  mit
21440:yas3  ('wie  sva.  womit')  hwä  yazata vTstäsps  Yt77.  61;  61,  5.90,  91,  /5- 54, V.  75.  17,  Vyt.20,  3/;  — ka%a  zaota  xsäta apB ..yazäile  Y.ö^.g;  —  tim  yazät surunvata  yasna  sraol»m  . .  zaokrabyB  (DP. statt  IP.)  Y.57.  3;  Yt.>  18,  70.  31 ;  —  yö aHm  yjzäite  zaohräbyB  Yt/7.  2;  2,  8.\, 10.6,  Y.68.10;  —  yatal^a  mqm  zara- ^uära  ..  zaokrräbyS  Yt  /.  9 ;  mangelhaft  zitirt F.4g; — hvanx^aitim ..yazamaide  haomays gava  barismana  .  ,  zaohrabyasca  arsux- öaäbyasca  vayzibyS  (DP.  statt  IP.)  Ny.  7. 1 6 ; —  yazayania  %wqm  mazdayasna  pasubya staoraHbya  vayalibya  pataraialibya  (sd.)  Yt 10. 1  \(j;—ultaiaiiya  (LS.  statt \%.)ca  vTspnn asavamm  .  .yazamaide  Vr.  18, 2.  b)  Akk.; tarn  yazata  kaolyaahü . .  sat)m  aspanqm  . . hazaisr)m  gavqm  "ihr  opferte  ff. . .  hundert Rosse, .."  Yt. 5.  21;  p.  ag;  —  tarn  yaztnta .  .  hunavB  .  .  sat>m  aspanqm  Yt  5.  57; 72.  c)  paiti  mit  Gen.(?);  yqm  yazata zara'huitrS  humatahe  paiti  mananhS  Yt 16.  6.  2)  mit  Angabe  des  wozu?  durch
```


## [2026-10-15T02:45:38.146Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'tarsîdan|tarsidan|tarsldan|tarsa\\b|tarsä' HRN.txt | head; echo ---HUB; grep -n -i -E 'tars|haräs|harās|haras|sahm' HUB.txt | head; echo ---NYB; grep -n -i -E '^ *(tars|sahm|harās|tarsāk|tarsāg)' NYB_vol2_glossary.txt | head; grep -n -i -E 'tars' NYB_vol2_glossary.txt | head; echo ---PHD; grep -n -i -E '(^| )(tars|sahm|tarsāg|tarsāk)[ -]' PHD_mackenzie.txt | head"
}
```


### [2026-10-15T02:45:38.605Z] TOOL RESULT

```
---HUB
334:kisag^ musag, also bal. hars aus haris =^ *haras?
1616:dr&fihayeiti — skr. trasayati und zd. tarsta- aus
1618:persischen trat tarsad er ftirchtet* fiir *tirsad = ap.
1626:vgl. drS *drei*), tastedql 'fliehen' (denom. zu zd. tarsti-)
2536:693. Ist phi. sdmdn = arm. sahman, so ist als altere
3883:tarSna- *Durst'; Bdh. 10, 7 muss sud nicht *Hunger
4087:beachten ist, in dem der Schrift nach altarsacidische, sas-
4463:ataSy arm. LW. afas (Sebeos), phi. ataocs^ zd. atars; pisan-
4637:kadar = zd. katarS, katO/rSm neben katarasdif, skr. katardr);
5018:darsti-^ tarSna-, tarsta-^ harSta-, karsvare^ karsta-, karSti-^
---NYB
3374:sahm [shm] terror 9!. — NP sah(1m; MPrs adj. shmyn ‘terrible, dreadful’; from OP "cahma, nom. of "cahman-, SW form of *Oürah-man-, from Av. (802 sqq.) 0rah-, v. tarsitan.
3375:sahmakan [~-kn'] awful 7212,
3751:tars [tls] fear, fright 52??; cas. obl. tarséh [tlsyh]: hac han be tarséh-ic for fear of this 4812,
3752:tarsčnitan [tlsynytn'] to inspire a p. with dread, to intimidate: Pourusdsp hac Zartuxšt pat viščpišn 4 haciš-aš škajt tarsēnīt 488-9, v. s. v. -&.
3753:tarsišn [tlsšn'] the act of fearing: bé ~ 4747; as pred.: cé-t nē apar ~ for thou must not fear 5829, cf s. v. -t.
3754:tarsitan [tlsytn'] imp. mā tars 61%, 1524, 5820; pret. 3d p. sg. tarsit hah 3119, to fear, to feel fear for (hac); ~ kū mà hakar lest 615; ka pat fräceh han i anē aparnāyīk fräc tarsit hénd when the lads ran fright- ened helter-skelter 527°; 3 hem ké-t 6 man tarsét three we are whom this house of thine fears 59? (6 cas. rect. of the pron.,
6824:tarsidan: tarsitan tawäh: tapäh tävastan: täpistän téh: ~ tež: ~
7475:tarsidan: tarsitan
829:a-x"ansandéh [hwnsndyh] discontent, displeasure: ~ kartan to cause offence 83". — Paz. axtarsandi; v. x"ansand.
1083:to], amāh-tc, ké-c, ka-c (ka vas-ic v.s. v. ka), bē-c, apar-ic, ö-c(i), pat-ic, peš-ic, hac-ic; hac hàn bē tarsēh-ic 4812; ete.; in
1098:candišn [cndšn'] movement, of the stars 1095. — Skr. v. caficalata (SGV VI,21). Ps.MPrs, v. Verbum 171.
1110:ea$m-kài [cšmk”y] having (all) eyes fastened (on oneself) = exposed to people’s (contemptuous) looks, an object of derision, dishonoured, pl. cas. obl. ~-kayan [-k’d’n'], comp. [c3mk’stl] cašm- kāh-tar (thus K; TD, [ešmk'dtl] cašm- kāi-tar) 1522-28, — MPrs cömg’h in the same sense (SalM III-IV, no. 9b°; Henning, GGN 1932, 223 n. 4, where, however, the pejorative sense is not recognized). The alternation -käh: -kāt is also found in the parallel formation tars-käh (PT 65? -k’s): tars-käi (DkM 4811’) ‘reveren- tial, respectful’, abstr. tars-kāhēh (-k’syh) ibd.1.21, but Cod. K (ad 1.) tars-kčiyeh (-k’dyh). Same formation in MPrs gylg’y (S; Verbum 205) < "gil-kdi ‘lamenting’ ; shyk? = sahik-ka(i) ‘frightened’ (preserv- ed -k- indicates -kk-), v. also mānā(k)-kāt.
1456:ēstišn [Pystšn', ystšn'] v. n. of ēstātan, used as pred.: has to, must stand fast, persevere 65’; subst. persistence 34?!; standstill, cessation of progress, of the stars 57. — V. also dstisn(éh).
2334:c) či rad ... ~ because 5177-52 passim; nē hast ki... tarsitan there is no reason why .. . should fear 61%; pat et kū ...
2335:adak-ic though . . . yet 5525-26; — d) after all vbs. of saying, feeling, judging and the like: göbet ku, api-$ guft ku he says, he said that, passim; very often intro- ducing direct speech, and serving as a quotation mark; often anticipated by čton: amäh čton äsnüt ku we have heard that 34; api-män eton sahist ku and it seemed to us that 89-7; ētūn ménés ku you may well think that 3312; äfrinv kart" ku prayed saying: "... P2:5; kū or ku tdi after framütan (g.v.); ku mà hakar after tarsitan (g. v.); pat én ku to the purport: “‘. . .” 922; pat én kar frestit ku sent you with orders to ask: “...” 1312; o Säsän dāt hend ku patmoc were given to S. (with the message): ''dress yourself up!" 218. — e) én ku, et ku the fact is that ..., passim; kū alone intro- duces explanatory glosses: ,,that is to say" 162. 375-8 and passim; pat späsdäreh én ku tuvān kartan ku it is through grati- tude that one can attain that ... 6511-12; fraytst kū, v. s. v. frayist. — 5. a dependent question, whether introduced or not by an interrogative, is preceded by kū placed immediately after the governing vb.: tà
3208:Rag [l'k']the name of a district and a town: né ka étar har 2 6 ham rasénd ~ u Notar not (even) when the two, Rag and Notar, come together here (i.e., never) 4316-17, 5017; fratom hac ax" 4 astomand andar ~ u Notar as the first of terrestrial beings between R. and N. (— far and wide, throughout the world) 5317-18, — A proverbial saying using op- posites to symbolize either absurdity or comprehensiveness. The saying is mean- ingless unless it refers to actual and well known geographical facts. Notar, other- wise unknown as a place-name, can only refer to the country of King Vištaspa, who derived his origin from Naotara the son of Manušcihr, thus symbolizing Eastern Iran (the Notars founded Tis, 1147-8). Rag must then be the OP Raga mentioned in the Behistun inseription (270, 32) as a district in Media ('Pdyat, called xčpoc by Arrianos III, 20, 2), thus representing Western Iran. That this dis- - trict had, already in Achaemenian time, a capital of the same name can scarcely be doubted, and is not contradicted by Strabo’s notice (C 525) that Alexander’s general Nikanor founded, besides other
3286:ravišn [Iwbšn'] l. pred.: apar-ip-im — I must ascend 4076. — 2. v. n. motion: ēstišn u ~ i stārakān station and motion of the stars 57; motion of the sun, of the moon and of the stars 872-22, 881, 8918; pat ~ ēstāt was in motion 9315-19; nıhän- ~ whose going is clandestine = sneaking 1038.
3374:sahm [shm] terror 9!. — NP sah(1m; MPrs adj. shmyn ‘terrible, dreadful’; from OP "cahma, nom. of "cahman-, SW form of *Oürah-man-, from Av. (802 sqq.) 0rah-, v. tarsitan.
---PHD
4471:sahm [shm I = M, N ......] terror.
4941:tars [tls 1 M trs, N --] fear, respect.
4945:tarsidan, tars- [tls-ytn' I (M tyrs)dn), N -..] fear, be afraid.
8203:tazenidan          \I~ t'~~             tars-
9067:sczd                        as" ),      sahm                         -GU'
```


## [2026-10-15T02:45:43.649Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 3374 3751; do head -n $n NYB_vol2_glossary.txt | tr -cd '\\f' | wc -c; done; awk 'BEGIN{RS=\"\\f\"} NR==181' NYB_vol2_glossary.txt | head -5; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));\nfor k in ['NYB','HRN','KLN','BQT','SOD','FFD']: print(k, d[k].get('page_offset'), d[k].get('lookup_hint','')[:300])\""
}
```


### [2026-10-15T02:45:44.172Z] TOOL RESULT

```
188
209
position, decay 112°.
Piitik [pwtyk] the name of a lake, “the Purifying,, 861%. — From pü-, v. pak. Av. (909) pūttika- ‘purifying’, zrayo puitikom ‘the purifying lake’.
www .parsianjoman.org | oe zl wk
rad 164
raftan
NYB Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
SOD printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
FFD 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
```


## [2026-10-15T02:45:49.053Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 179 180 181; do echo \"== leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' NYB_vol2_glossary.txt | grep -o -E '^[a-zāēīōūčšžγθx\"]+ \\[[^]]*\\]' | head -40 | tr '\\n' ' '; echo; done; for L in 187 188 208 209; do echo \"== leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' NYB_vol2_glossary.txt | grep -o -E '^[a-zāēīōūčšžγθx\"]+ \\[[^]]*\\]' | head -3 | tr '\\n' ' ';done"
}
```


### [2026-10-15T02:45:50.104Z] TOOL RESULT

```
== leaf 179
pursišn [pwrsšn'] pursitan [pwrsytn'] pus [BRH; pws 2218. 2615, 277] pušt [pwšt'; Ps. pwšty] puštēpān [pwštyp'n'] pūt [*pwt'] pūtakēh [pwtkyh] 
== leaf 180
raftan [SGYTN-tn'; Iptn'] 
== leaf 181
rag [lk'] 
== leaf 187
radišn [Iwdšn'] rop [lwp'] rospik [lwspyk] == leaf 188
ustan [lwstn'] ruvan [lwb?n'] sacakiha [~-yh’] == leaf 208
tang [tng] tanomand [tn'"wmnd] tapah [tp’h] == leaf 209
tarazčnitarčh [tl’eynyt’lyh] tārīk [t*lyk] tarist [tlyst]
```


## [2026-10-15T02:45:53.540Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 188 209; do awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' NYB_vol2_glossary.txt | grep -n -E '^ *[0-9]{3} *$|^[a-z]+ [0-9]{3}$|[0-9]{3}$' | head -5; done"
}
```


### [2026-10-15T02:45:54.127Z] TOOL RESULT

```
7:192
```


## [2026-10-15T02:45:56.245Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk -v n=209 'BEGIN{RS=\"\\f\"} NR==n+1' NYB_vol2_glossary.txt | head -8; echo; awk -v n=188 'BEGIN{RS=\"\\f\"} NR==n+1' NYB_vol2_glossary.txt | head -4"
}
```


### [2026-10-15T02:45:56.843Z] TOOL RESULT

```
shonour’ and (641) tard.mati- ‘obstinacy, recalcitrance’. V. also tar-menisneh.
tarazčnitarčh [tl’eynyt’lyh] the act of weighing 72!5. — From taräzenitan ‘to weigh', den. of
taräzük  [tl'ewk'] balance, scales for weighing 72%, — Olr *arä = Skr čula ‘balance, scale of a balance’ + Av. (223 sg.) az- ‘to convey, to conduct’
(Lat agere).
www.parsianjoman.org | col wok
tarik
192
Tatragat(i) vas

ustan [lwstn'] röd- [lwd-] to grow 6. 4074, 4122, 9218, 9518.22, — Av. (1492 sq.) 2raod-; MPrs pt. rwst, v. n. rwyysn (A-H I), Verbum 183; Paz. rustan roded (Mx 6238), pres. pass. rövihed (Sav XVI, 35, dubious); NP rustan röy- ; cf Bailey, BSOS VII, 1933, 84.
ruvan [lwb?n'] soul, the immortal part of the human being: F:2. 9!4, 125, 1326 (v. s. v. vart). 31-34 passim. 72—76 passim, etc. passim; v. also anösak. — Av. (1537 sqq.) urvan-; KZŠPrth ^rwn; MPrth rwn, rwn (A-H. III, BBB); MPrs rwn; Ps lwb’n; Paz. rua; NP ravan.
Rvänän [lw*n'-*n', and Paz.] patron.: ‘of the Rvän clan’ 371-5, v. Frahim Rwäng Zčiš.
sacakiha [~-yh’] properly, fittingly 795. 80°.
```


## [2026-10-15T02:45:59.648Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==108' HRN.txt | head -60"
}
```


### [2026-10-15T02:46:00.084Z] TOOL RESULT

```
-> 86 --
l)(i)rr(l)8tü ('Schwalbe'; oder gehört dies zu perriden?
vergl. gr. nsQiarsQd 'Taube') u. a. m.
383. {\)ter 'ein Vogel'.
Prof. Nöldeke verweist mich auf Ahrens, Buch
der Naturgegenstände, 25, 5 nebst G. Hoff mann 's
Bemerkungen zu der dortigen Übersetzung und ver-
gleicht lat. sturnus, nhd. Staar,
384. tersTden *sich fürchten', tersä 'furchtsam; Christ'.
ap. [/'tras-, tarsatiy 'er fürchtet'; aw. [/^tras-,
teresenti; phlv. tarsitan; ai. i^tras-, träsatl.
kurd. tirsm erschrecken ; afy. tarh[edal; oss. d.
farsim, t. färsin (244); bei. trusag, tursay, n. fursay
(394); sar. inträsam 'ich mache scheu'.
385. turus 'sauer .
kurd. Urs 'sauer ; bei. trusp, triips, n. trus (395);
wa/. tresp, sar. tä/b, yidg. trisp,
386. terfend, ferfende 'Falschheit, Betrug, Nichtigkeit' 0-
aw. i/trap'^ terefyat 'durch Betrug entwenden,
stehlen; phlv. tarftlnltan durch List wegnehmen*
(y. 11 (17)), taraftagl, taraft (ZPGL); ai. (mit anderer
Bedeutung) [/^trap-^ trdpate 'verlegen werden', eigent-
lich 'sich wenden, abwenden ; vergl. gr. Tginco,
np. terb 'List', das Hübschmann (ZDMG. 26, 457)
dazu stellt, ist unbelegt-).
M ÖF, FJ und FR bieten die folgenden Belege:
(Metr. Xefif)
nebüved der keläm-i tu juz edl
nereved her zehän-i tu ierfend
Öcms-I Fa/rl.
(Metr. Heze.]):
cun x^d neküiii ciinäiiki göyl
pend-l tu büved düröy ü ter/end
Näsir Xosrö.
Ein Vers Senai's im FJ ist metrisch nicht in Ordnung.
Auch tcrwend, terwende sollen in der gleichen Bedeutung vor-
kommen, während die Worte in dieser Form gewöhnlich nur ^Erstling
einer Frucht' bezeichnen.
^J Daneben giebt es auch ein up. terkend^ ierkeude mit gleicher
Bedeutung. FJ (fehlerhaft), FR:
```


## [2026-10-15T02:46:03.761Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in terror terrible terrify terrific tremble mattress thou thee thine; do n=$(grep -n -m1 \"^$w,\" KLN_1966.txt | cut -d: -f1); [ -n \"$n\" ] && { leaf=$(head -n $n KLN_1966.txt | tr -cd '\\f' | wc -c); echo \"== $w line $n leaf $leaf\"; sed -n \"${n},$((n+5))p\" KLN_1966.txt | cut -c1-700; }; done"
}
```


### [2026-10-15T02:46:04.534Z] TOOL RESULT

```
== terror line 38718 leaf 844
terror,  n.  —  ME.  terrour,  fr.  MF.  (=  F.)  terreur, fr.  L.  terrorem,  acc.  of  terror,  ‘great  fear,  alarm’, fr.  terrere,  ‘to  frighten’.  See  terrible  and  -or. terrorism,  n.  —  F.  terrorisme,  formed  fr.  L.  terror (see  prec.  word)  with  suff.  -isme  (see  -ism), terrorist,  n.  —  F,  terroriste,  formed  fr.  L.  terror (see  terror)  with  suff.  -isle  (see  -ist). Derivatives:  terrorist-ic,  terrorist-ic-al,  adjs. terrorize,  tr.  v.  —  Formed  fr.  L.  terror  (see  terror) with  suff.  -ize.
Derivatives:  terroriz-ation,  n.,  terroriz-er,  n. terry,  n.,  uncut  loop  in  velvet.  —  Prob.  fr.  F.  tire, ‘drawn,  pulled’,  pp.  of  tirer.  See  tire,  ‘to  puli’, terse,  adj.,  concise.  —  L.  tersus,  pp.  of  tergere, ‘to  rub,  wipe  off’,  which  is  cogn.  with  Gk.  xpd>- Ye-V,  ‘to  gnaw’,  xpcuy/.r;,  ‘hole’,  Goth,  pairko, ‘hole’,  fr.  I.-E.  *tro-g-,  *tre-g~,  enlargement  of base  *ter-,  *tr-,  ‘to  go  through,  pass  beyond’. See  term  and  cp.  absterge,  abstersion,  deterge, detersion.  Cp.  also  through,  troglodyte,  trout. Derivatives:  terse-ly,  adv.,  terse-ness,  n. tertial,  adj.,  referring  to  the  flight  feathers  of  the third  row  ( ornit
tertian,  adj.,  recurring  every  other  day.  —  Prop, ‘recurring  every  third  day’,  the  first  and  the third  day  being  reckoned  inclusively,  fr.  L.  ter- tianus,  fr.  tertius,  ‘the  third’.  See  third  and  cp. words  there  referred  to.  Cp.  also  sesterce, tertian,  n.,  tertian  fever.  —  L.  tertidna,  short  for febris  tertidna,  ‘tertiam  fever’.  See  prec.  word. Tertiary,  adj.,  pertaining  to  the  era  preceded  by the  Mesozoic  (geol.)  —  L.  tertiarius,  ‘containing a  third  part’,  fr.  tertius,  ‘third’  (see  third  and  adj. suff.  -ary) ;  so  called  because  the  Mesozoic  was formerly  named  Secondary.
Derivative:  Tertiary,  n.
tertiary,  n.,  a  member  of  third  order  in  a  monas¬ tic  system.  — •  See  prec.  word, tertium  quid,  something  intermediate  between two  things.  —  L.,  ‘a  third  something’,  transla¬ tion  of  Gk.  xptxov  xt.  See  tertian  and  quiddity, teruab,  n.,  a  succession  of  9  tremulous  notes  of the  shophar  (Jewish  Religion).  —  Heb.  t6rii'dh, ‘shout,  cry,  alarm,  blast  of  trumpet  or  shophar, a  succession  of  tremulous  notes’,  formed  from the  stem  of  herfa',  ‘he  sounded  a  signal,  he shouted  in  triumph"  (in  Mishnaic  Heb.  also  ‘he blew  the  shophar’),  which  is  prob.  rel.  to  Arab. ragha,  ‘he  shouted’.
teryiene,  n.,  trademark  for  a  synthetic  textile  fiber based  on  terephthalic  acid.  —  Coined  fr.  tere- phthalic  and  suff.  -ene.
== terrify line 38712 leaf 844
terrify,  tr.  v.  —  L.  terrificare,  ‘to  frighten’  (whence also  F.  terrifier),  fr.  terrificus.  See  prec.  word and  -fy.
Derivatives:  terrify-ing,  adj.,  terrify-ing-ly,  adv. terrigenous,  adj.,  1)  earthbom;  2)  produced  by  the earth.  —  L.  terrigena,  ‘bom  of  the  earth’,  fr. terra,  ‘earth’,  and  the  stem  of  gignere  (pp.  geni- tus),  ‘to  beget,  bear,  bring  forth’.  See  terra  and genus.
terrine,  n.,  an  earthenware  dish.  —  F.,  fr.  MF., fem.  of  the  adj.  terrin,  ‘pertaining  to  the  earth, earthen’,  fr.  VL.  *terrinus,  fr.  L.  terrenus.  See terrene  and  cp.  tureen.
territorial,  adj.  — -  L.  territorialis  (whence  also  F. territorial),  fr.  territorium,  ‘domain,  territory’. See  territory  and  cp.  exterritorial,  extraterri¬ torial.
Derivatives:  territorial,  n.,  territorial-ism,  n., territorial-ist ,  n.,  territorial-ize,  tr.  v.,  territorial- iz-ation,  n.,  territorial-ly,  adv. territory,  n.  —  L.  territorium,  ‘domain,  district, territory’,  formed  fr.  terra,  ‘earth’  (see  terra), with  -orium,  a  suff.  denoting  place  (see  subst. suff.  -ory).  Cp.  dormitorium,  ‘sleeping  room’  (see dormitory).
Derivatives:  territorial  (q.v.),  territori-an,  n., territori-ed,  adj.
== tremble line 39986 leaf 872
tremble,  intr.  v.  —  F.  trembler,  fr.  VL.  tremuldre, (whence  also  It.  tremolare;  Sp.  temblor),  fr.  L. tremulus,  ‘quivering,  trembling,  tremulous’,  fr. tremere,  ‘to  shiver,  quiver,  tremble’,  fr.  I.-E. base  *terem-,  *trem-,  ‘to  tremble’,  whence  also Gk.  xpEpstv,  ‘to  shiver,  tremble’,  xpoLLoc,  ‘a trembling’,  Lith.  trimu,  tr'imti,  Lett,  tremju, tremt,  ‘to  chase  away’,  OSlav.  tr^sQ,  tn?sti,  ‘to shake’.  Alb.  Gheg  trem,  Tosk  tremp,  ‘I  frighten, terrify’,  Goth,  pramstei,  ‘grasshopper’,  Toch.  A tram-,  ‘to  tremble’,  B.  trem,  tremem,  ‘a  trem¬ bling’,  and  prob.  also  Gk.  TappuacrEiv,  ‘to frighten,  terrify’.  Cp.  tremendous,  tremo
Derivatives:  trembl-er,  n.,  trembl-ing,  n.  and adj.,  trembl-ing-ly,  adv.
Tremella,  n.,  a  genus  of  fungi  (bot.)  —  ModL., fr.  tremere,  ‘to  tremble’.  See  tremble  and  -ella. tremendous,  adj.  —  L.  tremendus,  ‘causing  shiver¬ ing,  fearful’,  lit.  ‘that  ought  to  be  feared’,  ge¬ rundive  of  tremere,  ‘to  shiver,  tremble’.  See tremble.  For  E.  -ous,  as  equivalent  to  L.  -us,  see -ous.  For  the  use  of  Latin  gerundives  and  their derivatives  in  English  cp.  agenda  and  words there  referred  to.
Derivatives:  tremendous-ly,  adv.,  tremendous¬ ness,  n.
tremolant,  adj.,  having  a  tremolo  note  (said  of musical  instruments).  —  It.  tremolante,  pres, part,  of  tremolare,  ‘to  tremble-,  fr.  VL.  tremu- lare.  See  tremble  and  -ant. tremolite,  n.,  a  mineral  of  the  amphibole  group. —  F.  trdmolite,  named  after  the  Tremola  valley in  Switzerland.  For  the  ending  see  subst.  suff. -ite.
tremolo,  n.,  tremulous  effect  (music).  —  It.,  fr.  L. tremulus.  See  tremulous.
== mattress line 23157 leaf 509
mattress,  n.  —  ME.  materas,  fr.  OF.  materas  (F. matelas),  fr.  It.  materasso,  borrowed  in  Sicily  fr. Arab,  mdtrah,  ‘place  where  something  is  thrown or  laid’,  used  also  in  the  sense  of ‘mattress’  (see Dozy-Engelmann,  Glossaire  des  mots  espagnols et  portugais  derives  de  l’arabe,  p.  151);  fr. taralja,  ‘he  threw’.  Cp.  Sp.  ulmadraque,  ‘mat¬ tress’,  which  is  formed  fr.  Arab,  al-,  ‘the’  and mdtrah,  ‘mattress’  (see  above).  Cp.  also  mate- lasse.  Cp.  also  E.  tare,  ‘allowance  in  weight’, maturate,  tr.  v.,  to  make  mature  or  ripe;  to  cause to  suppurate;  intr.  v.,  to  ripen;  to  suppurate.  — L.  maturdtus,  pp.  of  maturare,
Derivatives:  maturate  (q.v.),  maturation  (q.v.), maturative  (q.v.),  mature-ly,  adv.,  mature-ness, n.,  mature,  v,  (q.v.),  matur-er,  n.,  maturescent (q.v.),  matur-ing,  n.,  maturity  (q.v.) mature,  tr.  v.,  to  cause  to  ripen;  intr.  v.,  to  ripen. —  OF.  maturer,  fr.  L.  maturare,  ‘to  ripen’,  fr. mdturus.  See  mature,  adj. maturescence,  n.  —  Formed  from  next  word  with suff.  -ce.
maturescent,  adj.,  becoming  ripe.  —  L.  mature- scens,  gen.  -entis,  pres.  part,  of  maturescere,  ‘to become  ripe,  to  ripen’,  formed  with  inchoative suff.  -escere,  fr.  mdturus,  ‘ripe’.  See  mature,  adj., and  -escent.
maturity,  n.,  ripeness.  —  ME.  maturite,  fr.  L. mdturitas,  ‘ripeness,  maturity’  [prob.  through the  medium  of  Late  MF.  (=  F.)  maturity],  fr. mdturus.  See  mature,  adj.,  and  -ity.
Matuta,  n.,  name  of  the  goddess  of  dawn  in  Ro¬
man  Religion.  —  L.  Mdtiita  (whence  matutinus, ‘of,  or  pertainig  to,  the  morning’),  rel.  to  md¬ turus.  See  mature,  adj.,  and  cp.  next  word, matutinal,  adj.,  pertaining  to,  or  happening,  in the  morning.  —  L.  matutinalis,  fr.  matutinus,  ‘of, or  pertaining  to,  the  morning’.  See  prec.  word, adj.  suff.  -ine  (representing  L.  -inus)  and  adj. suff.  -al.
== thou line 39107 leaf 853
thou,  pron.  of  2nd  person  sing.  —  ME.,  fr.  OE. du,  rel.  to  ON.  pu,  OS.,  OFris.  thu,  Dan.,  Swed. du,  MDu.  du,  OHG.,  MHG.  du,  G.  du,  Goth. pu,  fr.  I.-E.  *tii-,  ‘thou’,  whence  also  OI.  tv-am, Avestic  lit.  Arm.  du.  Dor.  Gk.  to,  Att.  au,  L.  tu. Alb.  ti,  OSlav.  ty,  Lith.  tit,  OIr.  tu,  W.  ti.  Cp. thee,  thine,  thy.  Cp.  also  tutoyer,  tuum. Derivative:  thou,  tr.  v.
though,  conj.  —  ME.  though,  thogh ,  fr.  ON.  *poh ; rel.  to  OE.  peah,  ON.  pd,  OS.  thoh,  OFris.  thach, OHG.  doh,  MHG.,  G.  doch ,  Goth,  pduh, ‘though,  yet’.  Cp.  although.
thought,  n.  —  ME,  thoght,  thouht,  fr.  OE.  gepoht, poht,  from  the  stem  of  penkan  (past  tense  pdhte), ‘to  think".  Cp.  OS.  githdht,  Du.  gedachte, ‘thought,  idea’,  MDu.  gedachtenisse,  ‘memory’, Du.  gedachtenis,  ‘remembrance’,  OHG.  kitheht- nissi,  MHG.  gedxhtnisse,  ‘devotion’,  G.  Ge- ddchtnis,  ‘memory’  (for  Du.  and  G.  suff.  -nis  see -ness),  Du.  aandacht,  ‘attention’,  OHG.  anadaht, MHG.  andaht,  G.  Andacht,  ‘attention,  devotion’ G.  Bedacht,  ‘consideration  deliberation’,  and see  think.
Derivatives:  thought-ful,  adj.,  thought-ful-ly, adv.,  thought- ful-ness,  n.,  thought-less,  adj.,
1610  i  1611
thought-less-ly,  adv.,  thought-less-ness,  n., thought-y,  adj.
== thee line 38901 leaf 848
thee,  objective  case  of  thou.  —  ME.,  fr.  OE.  pe, dat.  and  acc.  of  pit,  ‘thou’.  See  thou.
Derivative:  thee,  tr.  v.,  to  address  as  thee ;  intr. v.,  to  use  thee  in  addressing  a  person, thee,  intr.  v.,  to  grow,  thrive.  —  OE.  theon,  rel. to  OS.  thihan,  OFris.  thigia,  MDu.  ( ghe)dien , Du.  gedijen,  OHG.  (gi)dihan,  MHG.  gedihen, G.  gedeihen,  Goth.  ( ga)peihan ,  fr.  I.-E.  base tenq-,  ‘to  be  thick  or  strong’.  Sec  tight, theelin,  n.,  a  crystalline  hormone  (biochem.)  — Formed  with  suff.  -in  fr.  Gk.  DxjXu?,  ‘female’. See  thely-.
theft,  n.  —  ME.  thefte,  thiefthe,  fr.  OE.  peofd, piefd,  pyfd,  fr.  peof,  ‘thief’.  Cp.  ON.  pyf,  pyft, and  OFris.  thiiifthe,  thiufte.  and  see  thief  and subst.  suff.  -t.
thegn,  n.  —  A  var.  of  thane, theine,  thein,  n . ,  another  name  for  caffeine  (chem.) —  F.  theine,  formed  with  chem.  suff.  -ine,  -in,  fr. Thea ;  so  called  because  it  occurs  in  tea. their,  possessive  pron.  —  ME.  their,  thair,  fr.  ON. peir(r)a,  ‘of  them',  gen.  pi.  of  the  demonstr. pron.  sd,  su,  pat,  and  rel.  to  OE.  para,  piera, gen.  pi.  of  the  def.  article.  See  they  and  cp. them,  that.
theirs,  possessive  pron.  —  Formed  from  prec. word  with  suff.  -s,  on  analogy  of  his. theism,  n.,  belief  in  a  personal  God.  —  Formed with  suff.  -ism  fr.  Gk.  &e6s,  ‘god’,  which  prob. stands  for  *dhes-os,  and  is  cogn.  with  Arm.  dik', ‘gods’  (which  prob.  stands  for  *dhes-es),  OI. dhisnyah ,  ‘pious,  devoted’,  L.  fanum  (for  *fas- nom),  ‘consecrated  place,  temple',  feriae  (fr.  OL. fesiae),  ‘holy  days,  festivals’,  festus,  ‘festive’;  fr. I.-E.  base  *dhes-  (=  L.  *fes-,  *fas-),  ‘holy’.  Cp. apotheosis,  atheism,  ditheism,  enthusiasm,  heno- theism,  hylotheism,  monotheism,  pantheism,  poly¬ theism,  Thecla,  theo-,  Theodore,  Thesp
theist,  n.,  an  adherent  of  theism.  —  See  theism  (fr. Gk.  ffcoc )  and  -ist  and  cp.  atheist,  henotheist, monotheist,  pantheist,  polytheist.
== thine line 39039 leaf 851
thine,  possessive  pron.  —  ME.  thin,  fr.  OE.  pin, orig.  gen.  of  pit,  "thou",  rel.  to  OS.,  OFris.  thin , ‘thy,  thine’.  ON.  pinn,  ‘thy,  thine’,  pin,  ‘of  thee', Dan.,  Swed.  din,  MDu.,  Du.  dijn,  OHG.  thin, din,  MHG.  din,  G.  dein,  Goth,  peins,  ‘thy,  thine’, peina,  ‘of  thee’.  All  these  words  stand  for  I.-E. *t(w)ei-no-s,  and  are  cogn.  with  L.  tuus  (for *twei-os),  ‘thv,  thine’,  fr.  I.-E.  base  *tu-,  ‘thou, thee’;  see  thou  and  cp.  thee.  In  ME.,  the  final  n was  dropped  before  a  word  beginning  with  a consonant  and  so  arose  the  form  thy  (q.v.) thing,  n.,  an  inanimate  object.  —  ME.,  fr.  OE. ping,  condition,  sta
(in  space  or  in  time)’,  and  orig.  denoted  ‘meet¬ ing  at  a  fixed  time’,  whence  developed  the  mean¬ ings  ‘affairs,  things,  thing’.  Cp.  Goth,  peihs, ‘time’,  orig.  ‘assembly  taking  place  at  a  fixed time’,  fr.  I.-E.  *teijgho-,  fr.  base  *ten-.  See  tend, ‘to  move  in  a  certain  direction’,  and  cp.  thing, ‘assembly’,  and  words  there  referred  to.  Cp.  also temporal,  ‘pertaining  to  time’.
Derivative:  thing-y,  adj.
thing,  ting,  n.,  a  legislative  assembly  in  the  Scan¬ dinavian  countries.  —  ON.  ping  (whence  also Norw.  thing,  ting,  Swed.  ting,  ‘assembly’);  de¬ rivatively  identical  with  thing,  ‘an  object’  (q.v.) Cp.  the  first  element  in  Tynwald  and  the  second element  in  busting,  storting, thingamy,  thingumbub,  thingummy,  n.,  a  thing.  — Jocose  formations  of  thing,  ‘an  object’, think,  intr.  v.,  to  seem  (obsol.)  —  ME.  thinken,  fr. OE.  pyncan,  rel.  to  OS.  thunkian,  ON.  pykkja, Swed.  tycka,  OFris.  thinka,  OHG.  dunchen, MHG.  diinken,  dunken,  G.  diinken,  Goth. pugkjan,  ‘to  seem’,  and  prob.  cogn.  with  L.  ton- gere,  ‘to  know’,  Prae
Derivatives:  thinkable,  adj.,  think-er,  n.,  think¬ ing,  n.  and  adj.,  thinkable-ness,  n.,  thinkabl-y, adv.,  think-ing-ly,  adv.
thio-,  before  a  vowel  thi-,  combining  form  used in  the  sense  of ‘containing  sulfur’  ( chem .)  —  Gk. Delo-,  Dei-,  fr.  Oetov,  Homeric  Gk.  9£eiov, ‘brimstone’,  for  *9.F£C[-(e)lov,  lit.  ‘that  which smokes’,  from  I.-E.  base  *dhewes-,  *dhwes-,  ‘to breathe,  smoke'.  Base  *dhewes-,  *dhwes-,  is  an enlargement  of  base  *dheu-,  ‘to  fly  about  like dust,  to  smoke,  whirl,  shake,  be  scattered,  van¬ ish',  whence  OI.  dhunbti,  dhuvati,  ‘shakes, moves',  Gk.  Ooei-v,  ‘to  sacrifice’,  prop,  ‘to  cause to  smoke’,  9up.ee,  ‘sacrifice’,  Oupov,  also  9upo?, ‘thyme’,  9upi£v,  ‘to  burn  so  as  to  produce smoke’,  UOptapa,  ‘incense’,  9uo<;,  ‘burned
```


## [2026-10-15T02:46:09.425Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -m2 -E '^terrible,|^terrific,' KLN_1966.txt | cut -c1-900; for L in 808 809 810; do echo \"== leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | grep -o -E '^[A-Za-z-]+,' | head -3 | tr '\\n' ' '; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | grep -o -E '15[89][0-9] *i? *15[89][0-9]'; done"
}
```


### [2026-10-15T02:46:10.261Z] TOOL RESULT

```
Exit code 1
== leaf 808
stratify, Stratiotes, strato-, == leaf 809
strict, stricture, stride, == leaf 810
strong, strontia, strontian,
```


## [2026-10-15T02:46:12.578Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E '(1590|1591|1592|1593) *[i|] *(1591|1592|1593|1594)' KLN_1966.txt | head; grep -n -E 'terrible' KLN_1966.txt | head -5 | cut -c1-600"
}
```


### [2026-10-15T02:46:13.077Z] TOOL RESULT

```
1787:Aeneas,  n.,  the  son  of  Anchises  and  Aphrodite, a  Trojan  hero  and  mythical  ancestor  of  the Romans;  the  hero  of  Virgil’s  Aeneid.  —  L. Aeneas,  fr.  Gk.  AEveEag,  a  name  of  uncertain origin.  It  is  possibly  rel.  to  aEvd;,  ‘horrible, terrible’.
10791:Demogorgon,  n.,  a  terrible  deity  ( Greek  mythol.) —  Late  L.,  first  mentioned  by  Lactantius  (or Lutatius)  Placidus  on  Statius.  The  first  element in  the  name  of  this  deity  is  of  uncertain  origin. The  second  element  certainly  derives  fr.  Gk. YopY'k,  ‘terrible’.  See  Gorgon, demography,  n.,  statistics  of  births,  marriages,
11471:Derivatives:  dinner-y,  dinner-less,  adjs. dino-,  combining  form  meaning  ‘fearful’.  —  Gk. Seivo-,  fr.  8eiv6?  (for  *8fei-vo?),  ‘fearful’,  rel. to  8ei8o>  (for  *8£-8Foi-a),  ‘I  fear’,  8£o?  (for *8Fei-o?),  ‘fearful,  terrible,  powerful,  mighty, marvelous’,  Seiko?  (for  *8Fei->,6?), 'cowardly,  and possibly  cogn.  with  L.  dims,  ‘fearful’.  See  dire. Dinobryon,  n.,  a  genus  of  flagellates  (biol.)  — ModL.,  compounded  of  Gk.  STvo?,  ‘a  whirl¬ ing’,  and  ppftov,  ‘moss’.  See  dinus  and  bryo-. Dinoceras,  n.,  a  genus  of  extinct  ungulates  (pale- on
11543:dire,  adj.,  dreadful.  —  L.  dirus,  ‘fearful,  awful, ill-omened,  horrible,  terrible’,  of  uncertain  ori¬ gin.  It  possibly  derives  fr.  I.-E.  base  *dwei-,  ‘to be  afraid,  fear’,  whence  also  Gk.  SeiSoi  (for *S£-Sfot-a),  ‘fear’,  Seop  (for  *8fet-op),  ‘fear¬ ful,  terrible,  powerful,  mighty,  marvelous’, SctXop  (for  *Sfet-Xop),  ‘cowardly’,  Savop  (for *Sfei-vop),  ‘fearful’,  OI.  dvesti,  ‘hates’,  dvisah, ’hatred’,  Avestic  dvaeba-,  'threat,  menace’,  and prob.  also  Arm.  erkncim,  'I  fear’.  Cp.  dino-, dinosaur.
15201:formicide,  n.,  substance  used  for  killing  ants.  — Contraction  of  *formici-cide,  fr.  L.  formica, ‘ant’,  and  -cida,  ‘killer’,  fr.  caedere,  ‘to  kill’.  See formic  and  -cide,  ‘killer’.  For  the  contraction  of *formici-cide  into  formicide  see  haplology. formidable,  adj.,  causing  fear.  —  F.,  fr.  L. formidabilis,  ‘causing  fear,  terrible’,  fr.  formi- dare,  ‘to  fear,  dread',  tr.  formidd,  ‘terror’,  which is  prob.  cogn.  with  Gk.  p.opp.d>,  ‘bugbear,  hob¬ goblin’.  Cp.  mormo.  For  the  dissimilation  of m-m  to  f-m  see  form,  n.
```


## [2026-10-15T02:46:14.890Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 38700,38712p KLN_1966.txt | grep -n -i 'terri' | cut -c1-1200"
}
```


### [2026-10-15T02:46:15.414Z] TOOL RESULT

```
8:Derivatives :  terrestrial,  n.,  terrestrial-ity ,  n. terret,  n.,  ring  of  a  harness  pad.  ME.  teret, toret,  fr.  OF.  toret,  touret,  ‘small  wheel’,  dimin. of  tour,  ‘circuit’.  See  tour  and  -et. terrible,  adj.  —  ME.,  fr.  MF.  (=  F.),  fr.  L.  terri- bilis,  ‘frightful,  dreadful’,  fr.  terred,  terrere,  ‘to frighten’,  which  stands  for  *terseyd  and  is  cogn. with  OI.  trasati,  ‘trembles’,  Avestic  tarshta, ‘feared,  revered',  t^r^saiti,  ‘is  afraid  of ,  Gk. xpleiv  (for  *tresein),  ‘to  tremble;  to  flee’,  Lith. trisu,  triSeti,  ‘to  tremble’,  OSlav.  rresq,  ‘I  shake  , tn>sQ  se,  ‘I  tremble’,  Mir.  tarrach,  ‘timid’,  fr. I.-E.  base  *teres-,  *tres-,  ‘to  tremble’.  Cp.  deter. Cp.  also  Tirshatha,  Treron.  For  the  ending  see suff.  -ible.  —  Cp.  the  collateral  I.-E.  bases: *trem-,  whence  Gk.  xpepiEiv,  L.  tremere,  to tremble’,  and  *trep-,  whence  L.  trepidus,  ‘rest¬ less,  anxious,  solicitous  .  See  tremble  and  trep¬ idation.
9:Derivatives:  terrible-ness,  n.,  terribl-y,  adv. terricolous,  adj.,  living  on  the  ground  (zool.  and hot.)  —  Formed  with  suff.  -ous  fr.  L.  terricola, ‘inhabiting  the  earth’,  fr.  terra,  ‘earth’,  and -cola,  ‘inhabiting',  which  is  rel.  to  colere,  ‘to  till (the  ground);  to  inhabit',  incolere,  ‘to  inhabit’, incola,  ‘inhabitant’,  coionus,  ‘cultivator  of  the ground’.  See  terra  and  colony  and  cp.  the  second element  in  pratincole.  For  the  ending  see  suff. -ous.
10:terrier,  n.,  a  kind  of  dog.  —  F.,  prop,  chien  terrier, lit.  ‘earth  dog’,  fr.  chien,  ‘dog  (fr.  L.  canis),  and ML.  terrdrius,  ‘of,  or  pertaining  to,  earth  or land’,  fr.  L.  terra,  ‘earth,  land’.  See  terra  and -ier.
12:terrier,  n.,  a  document  stating  the  boundaries  of landed  property.  —  F.,  fr.  MF.,  fr.  ML.  (liber) terrdrius,  ‘book  relating  to  land’,  fr.  L.  terra, ‘earth,  land’.  See  prec.  word, terrific,  adj. — L.  terrificus ,  ‘frightful’,  lit.  ‘caus¬ ing  terror’,  compounded  of  the  stem  of  terrere, ‘to  frighten’,  and  -ficere,  unstressed  form  of  fa- cere,  ‘to  make,  do’.  See  terrible  and  -fic. Derivatives:  terrific-al-ly,  terrific-ly,  advs., terrific-ness,  n.
13:terrify,  tr.  v.  —  L.  terrificare,  ‘to  frighten’  (whence also  F.  terrifier),  fr.  terrificus.  See  prec.  word and  -fy.
```


## [2026-10-15T02:46:20.775Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in BQT:484 BQT:1197 BQT:525; do echo \"=== $p\"; timeout 300 python3 tools/ref_page.py $p 2>&1 | head -80; done"
}
```


### [2026-10-15T02:46:21.758Z] TOOL RESULT

```
=== BQT:484
no scan of BQT covers printed page 484 (see 'scans' in refs_online.json)
=== BQT:1197
no scan of BQT covers printed page 1197 (see 'scans' in refs_online.json)
=== BQT:525
no scan of BQT covers printed page 525 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:46:22.802Z] AGENT

Vols 1–2 are in OCR text. Let me grep them.


## [2026-10-15T02:46:24.410Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'ترسیدن|ترسا ' BQT_v1_pages.txt | head; grep -n -E 'tarsatiy|tars-|taršta|tarsta|tarsâ|tarsa' BQT_v1_pages.txt | head"
}
```


### [2026-10-15T02:46:24.997Z] TOOL RESULT

```
8587:اند ترسا ومردمانی بت پرستند و مردمان وی گروهی کوهی اند و گررهی دشتی . » « حدودالعالم
18033:بلفت زند و پازند (۱) بممنی ترسیدن و رمیدن
18984:آتان بندها در دربار خلفای عباسی‌بوزارترسیدند «بارتولد: دالرةالمعارف اسلام: 2۵7۳0۵16066
29488:رك : ترسیدن .
```


## [2026-10-15T02:46:27.230Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; n=29488; leaf=$(head -n $n BQT_v1_pages.txt | tr -cd '\\f' | wc -c); echo leaf $leaf; awk -v n=$leaf 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -120"
}
```


### [2026-10-15T02:46:27.773Z] TOOL RESULT

```
leaf 710
هعئی با زای نقطه دار نیز بنظرآهده ات
ترر بان » بروزن همزبان؛ بمه‌:ی زبان
آور وشخصی که کرم کفنکو شود و خن هی
ثر وتازه بگوید - و بمعنی ترجمان هم هست
یمنی شخصی که لفتی را اززبانی بزبان دیگر
قرب کند ۷ .
فر ۵۵ بسکون ثالی بر وزن سرزده »
بیعنی اول ترده ۱ ست که قبالة خانه وباغ باشد »
- وقنح انی بروزن تبرزه هم‌آهدء ۲ ست.
تر فان بروزن ومعتی ترجمان است
یمنی شخصی که لفتی راز زبانی بز بان دیگرسیان
کند ؟- وترزبان را نیز گوبند ۴ و آن شخصی
باشد که سخنهای تروتازه نقل کند.
نرس- بخم اول و سکون انی و سین
بی‌نقطه» بمعنی سخت و محکم باشد- ودر عربی
سیر را کوبند که ترکان قلقان خوانند - و نم
اول ونانی زمین سخت باشد ؛ و باین معنی بفتح
9
اول دضم نانی هم گفته‌اند - وبفئح اول وسکون
انی ممروف است که خوف وبیم باشد ۴ .
قر سا ه بر وزن تنها » ثرسنده و یم
بر نده وء امه کننده‌را گو ند و نصرانی ٩‏ وآش-
مرست را نیز گفتهاند ۷
ترس استودان*- بنتح اود
وسکون ثانی و ثاكث و همز؛ مفتوح وسین دبگر
موقوف و فوفانی بواو زسبده و دال بالف کشده
بنون زده دعا وزند ویازند (۱) خواندن فارسیان
ات یه ووو من اه تمه منک :له که
گونند چونروح از فالب مفارقت نماید سه‌شانه
و او را دز این
سه شبانروز ترس دم بسیار است ٩‏ لهذا دراین
سه روز برسردخمة اونكك خوانند تا روح‌اواز آن
ایمن گردد . ومعنی ترکیبی اين لفت خوف فبی
است چه ترس بمعتی خوف ویم‌باشد, واستودان
دخمه ومقبره را کوند . ۶
0
)۱( چيك: زند وبا ند.
. رك : ترزفان‎ ٩
«اسشق ۰۰۷۸۶ اتکاه
رك : ترسیدن .
راهب‌نیز درعر می بهه ین معنی است
۴ بارسی اسثان و اوستابی ۳25 ‌
۱ - بهلری 2۲521
۳۸ چنانکه
ای کریمی که از خزانة غیب
٩‏ - در ندش فصل۲۸ بند۱۸] مده:
۰ کلستان ۲ *.
۵ رل : اسنودان .
. دیو وبزرش بردر دوزخ
ث رسندفه» خالف.
```


## [2026-10-15T02:46:32.546Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'هراسیدن|^هراس' incoming/BQT/BQT_v4_pages.txt | head -5; grep -n -E 'fra-?[θt]r[aā]s|frāsa|fratrās' incoming/BQT/BQT_v4_pages.txt | head; grep -n -E 'سهمگین|^سهم ' BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt | head"
}
```


### [2026-10-15T02:46:32.947Z] TOOL RESULT

```
3169:هراس اقطی ۷ « بفتح اول و کسر خصومت کردن و بکدله بودن در بد کرداری هم
15788:* لفت فری ص۲۰۱ > درین بت فعل «* هاسیدن > بمعنی هراسیدن‌آمده‌است .
16282:هراس « بفتح ول وسکون‌سین بی ناطه. هراسیدن* « بمعنی ترسیدن وواهیه
16313:‎٩‏ - امر از «هراسیدن» . ۷ - جمع «هراسنده» اسم فاعل‌از «هراسیدن»(ه.م.
BQT_v2_pages.txt:18279:                                                                             ‫بر وزن اشارات » بمعنی سهمگین و خشم آلود‬
BQT_v2_pages.txt:18338:‫وخشم| لود وسهمگین ‪ -‬وخام طمعوعیب جوی‬                            ‫در | لون ‪ -‬بروزن طلا کون ‪ ۰‬تمعتی‬
BQT_v2_pages.txt:18351:               ‫عیب جوبان ولا‪.‬زیبایان وغیره بلشد ‪.‬‬          ‫و خشمآ لود‬          ‫گاه‌است که سهمگین‬               ‫بمعنیدژآ‬    ‫شاه“‬
BQT_v2_pages.txt:18377:                                                                        ‫وخشمناله وسهمگین ‪ -‬و تیرتخش و‬
BQT_v2_pages.txt:39855:  ‫* سهمگین ‪ -‬و سپمکن (مشذف) از ‪ :‬سهم ( ترس وییم ) ‪ +‬کن ( یود اصان ) ؛‬
```


## [2026-10-15T02:46:35.436Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 16280,16320p incoming/BQT/BQT_v4_pages.txt; echo ====; n=39855; leaf=$(head -n $n BQT_v2_pages.txt | tr -cd '\\f' | wc -c); echo leaf $leaf; grep -n -E 'سهم' BQT_v2_pages.txt | sed -n 1,200p | awk -F: '$1>39700 && $1<39900' | cut -c1-300"
}
```


### [2026-10-15T02:46:36.097Z] TOOL RESULT

```
Exit code 1
خراسان ۴ . وبفتح اول هم درست است .

هراس « بفتح ول وسکون‌سین بی ناطه. هراسیدن* « بمعنی ترسیدن وواهیه
نام درختی است خاردار - وبکی اول بمعنی‌ترس | کردن باشد ‏
و بیم باشد ‎٩‏ - و اهر بترسیدن و بیم بردن هم هراش - بفتح اول وسکون آخ رکه
هت بمثی بترس٩‏ ؛ و بان معنی بفتح اول هم | .شین نقطه داراست؛ بممنی قی واستفراغوشکوقه
آمده است . باشد*۱- وبتازی برهم انداختن سکها باشد از

(۱) خم۱ : - ملك .

۹ - اسم صوت . قی : افقانی 8۵۳8-80۳8 (صد! وغوغا) « خوبشمان۱*۹۱* و رك :
اسشق - هوبشمان ۱*۹۱ . قی : هربن (آوازهپیب) ؛ ترکی «هرای» (#ر‌باد » كومك خواستن,
اطلاع دادن بشخصی چیزی را) « جفتایی‌س ۴۵۱۵ :

ز هرین حمله ز هرای تیخ شده آب خون در دل تند میخ.

نظامی کنجوی « کنجینهٌ کنجوی ۰4۱۹

درل :جح ۰۱ ۴ < هرات (ه.م.) ۳ فریو (هم.) # اهری :

بهرای کنجش چو پدرام کرد به پهلو زباش «هری» نام کرد .

ظامی کنجوی «رشیدی» .

۴ < هرا (ه.م.)* هری (م.م.) * هریو (ه.م.) .در اوستا ۰۳12۳26۷2 پلرسمی
باستان 712۳81۷8 *اغپیگل ۵ ۲4 » پپلوی 118۳810 » 113۳8۷ « مار کوارت . شهرستانهای
ابران س۱۱* . [16] 111۳24 (هراتی) «اونوالا<۹؟) ؛ نام شهری بخراسان قدیم » که اکتون
درشمال غربی افغانتان ودر کنار هری رود راقع است . .8 - «هرای: تری بود . فردوسی
( طوسی ) کوید :

پیزدان هر آن کی که شد ناسپای پدلش آندر آید ز هر مو هرای »
« لغت فرس ص۱۹۱ ورله: تذ کرة الاولیاء چاپ اروپا جاص۸۸ی۰۱۲

‎٩‏ - امر از «هراسیدن» . ۷ - جمع «هراسنده» اسم فاعل‌از «هراسیدن»(ه.م.
بمنی ترسندگان . ۸ - از: هرای (ه.م.) ۸ (یسوندآلت). ‎٩‏ - از:هرای (ه.م.)
+یدن(پوند مصدری) ورك : هراسه . ۴ «هراش, قی‌باشد. دهید (بلخی) گفت :

‏از چه‌توبه لکند خواجه بهرجا که بود قدحی می‌بخورد راست کند زود هراش .>
«لغت فری ۰.۹۲۰۹
درخ صحاح‌الفرس طاعتی : « هراشی » فی باشد که مستان پاییماران کنند . شهیدگفت :
از چه توبه نکند خواجه بهرجا که رود قدحی می‌بخورد راست کند زودهراش.>
(eval):1: === not found
```


## [2026-10-15T02:46:39.796Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; n=39855; leaf=$(head -n $n BQT_v2_pages.txt | tr -cd '\\f' | wc -c); echo leaf $leaf; awk -v n=$leaf 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | grep -n -E 'سهم|tah|čah|θrah|sahm' | cut -c1-400"
}
```


### [2026-10-15T02:46:40.253Z] TOOL RESULT

```
leaf 661
27:                                                              ‫وهم ب‬      ‫سهم = بر وزن‬
62:  ‫* سهمگین ‪ -‬و سپمکن (مشذف) از ‪ :‬سهم ( ترس وییم ) ‪ +‬کن ( یود اصان ) ؛‬
63:       ‫‪ .‬سهمناك ‪:‬‬   ‫یب‬  ‫خوفناکه ) «یب رک ‪ ۹۹۱۰‬ورك ‪ :‬سه‬
67:                                             ‫سهمکین آبی که مرغابی در او ايمن تبودی‬
72:   ‫٭ سهمناك ‪ -‬از ‪ :‬سہم ( ترس و بیم)‪ ۳‬ناکه ( پود اتصاف ) ؛ نرسناکه*سهمگن‪.‬‬
```


## [2026-10-15T02:46:42.267Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 660 661; do awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | sed 's/  */ /g' | head -90; echo \"-----\"; done"
}
```


### [2026-10-15T02:46:43.108Z] TOOL RESULT

```
 ‫‪-۱۱-‬‬ ‫سه روح‬
‫سه غر هُدهاع = بسنی سه ابوان‬ ‫بود و اورا لدانته کشت‪.‬‬

‫خیال و محل‬ ‫مرحول‬
 ‫فک‬ ‫حهل‬
 ‫مت ک‬
 ‫دماغ اس‬ ‫سه روح = بارای قرشت بواو کشیده‬
 ‫حافظه باشد © ‪.‬‬ ‫و بحای حطی زده » بمعنی موالید ثلائه است که‬

‫سه غرفه هغز= پنینی سه غرفة‬ ‫حیوان ولبات وحماد باشد ‪.‬‬
 ‫ل‬‫مالحو‬
 ‫دماغ است که محل فکر و محل خی‬ ‫سه رود = با رای قرشت (‪ )۱‬بواو‬
 ‫حااظه باشد ‪. ۷‬‬ ‫رسیده و بدال زده » بمعذی سه‌تار است کهطنبور‬
‫اکل‪-‬ید ثلائه‌است که‌لبات‬
 ‫زن‬‫سه فمرو‬ ‫تساهرسته باشد ؛ و بعضی کوبند چنگ و رباب‬
 ‫جوماد وحیوان باشد ‪.‬‬ ‫و پربط است ‪.‬‬
‫سه ھانه = باکاف فارسی بالف کشیدہ‬ ‫سهستن ‪ = ۱‬بفتح اول و سکون سین‬
 ‫»نابه از جام و پیالةً شراب خوری‬
 ‫و فتح لون ک‬ ‫منیقطه بروزن اهشتن» بتمرعسنیدن‌ورمیدن‌باشد‪.‬‬
 ‫باشد ‪.‬‬ ‫سه ستبل ؟ = بنتح سین بی قطه (‪)۷‬‬
 ‫کماف فسارکسیونولام؛‬
 ‫سه گل ‪ -‬ن‬ ‫و سکون لون و بای ابجد (‪ )۳‬مضموم‌بلام زده‪,‬‬
 ‫نام درختی است که‌میوءآن چون پخته شودسرخ‬ ‫بمعنی سوستبر است » و آن سبزیی باشد میان‬
 ‫گردد و بغابت قابض باشد وآنرا بفارسی‌توت‌سه‬ ‫پودنه و عناع زبرا که چون بودنه رادست نتان‬
 ‫کل و بعربی توث العلیق خوانند چه درخت‬ ‫که ور شوو و افا یسار نر گونتهه‬
‫آلرا عربان علیق گوبند » وتوث وحشی لیزهمان‬ ‫سه شاخ ‪ -‬با شن قرعت (‪ )4‬بالف‬
 ‫اع ‪: ۷‬‬ ‫کشنده وبخای نقطه‌دار (ه) زده » بمعنی‌سهروح‬
‫سه "نید ان ‪ -‬عبارت از قلمهةٌ سنگوان‬ ‫اهبه از موالید ثلائه باثد وآن حیوان‬‫اکستن ک‬
 ‫است که در شبراز بپیدان مشهور است وآن سه‬ ‫ولبات وجماد است ‪. ۴‬‬
‫قلمه بوده که در آنجا جمشند ساخته امت ‪ :‬اول‬ ‫از تاربکی صلب‬ ‫یه‬
 ‫به ظکلمنتا‪-‬‬
 ‫استخر ودوم قلعةٌ شکته و سوم قلمه حتگوان‪:‬‬ ‫پدر و تاریکی شکم و تاریکی زهدان مادراست‬
 ‫وآ را سه ظلمات هممیگویند ‪۲ ۴‬‬
‫بوزیکصد و چهل ستون برسر پشته برآورده‬
‫شصت گر بنیاد کرده‬
 ‫و کوشکی بطول نکصد و‬ ‫سه علم کناب ازعلمالهی و طبیعی‬
 ‫بود که! کنون آثارآ ارا چپل ستون خوانند ‪. ۸‬‬ ‫و ریاضی باشد‪.‬‬
 ‫‪.‬‬ ‫بى نقطه‬ ‫‪- :‬‬ ‫چك‬ ‫(‪)۲‬‬ ‫(‪ )۱‬چك ‪ :‬بارا ‪.‬‬
 ‫‪ :‬وبا‪۰ ‎‬‬ ‫چك‬ ‫)‪(e‬‬ ‫(‪ )4‬چك‪ - :‬فرشت ‪.‬‬ ‫‪ :‬وبا ‪.‬‬ ‫چك‬ ‫(‪)۳‬‬



 ‫‪ - ۱‬يهلرى ‪ 720591135‬به‌عنی بنظر آمدن » ظاهر شدن ‪ .‬هزواری آن (‪2)010221‬‬
 ‫_‪( 69‬امراست‌بممنی بنگرودقت کن)‪.‬‬
 ‫‏‪* —mûnistan‬بونکر ‪« ۵۱۱‬اوتوالا ‪.»۰۵٩‬درنهرانی‏ ‪0 65‬‬
 ‫آلنی م رکب ازدسته‌ای چو من دارای‌سه شاخه‬ ‫‪ - ۴‬و‬ ‫رکه‪ :‬سی سنیر ‪۰‬‬ ‫‪ ۱‬؟ ‏‬

 ‫‏‪ e‬سرك‪:‬مه‌ابواندماغ»‬ ‫فلزی را کونند که بدان غلدرا بدارهند ‪.‬‏ ‪_ ۴‬رك ‪ :‬طلمات ثلاثه ‪.‬‬
 ‫‪ub‬‏ ‪uR‬‬ ‫‪ = ۷‬تمشك =‬ ‫‪٩‬‏‪ -‬ر‪:‬سه ابوان دماغ » سهغرف دماغ ‪.‬‬ ‫سرهفةٌ مغز ‪.‬‬
 ‫غ‬
 ‫درمبان هر‬ ‫‪ ۰.‬ومیه‌فلعهساخت‬ ‫اه ماخ" باری رادار الملك ساخت‬ ‫‪(۱- ۸‬جمشد)‬ ‫ی اتی ‪+۰‬‬


 ‫» برفلعةٌ‬ ‫سوم قلمةٌ شکنوان‬ ‫» دوم قلعةٌ ‪EEE‬‏‬ ‫یکی قلعةٌ اصطخر‬ ‫وآ را سهکنبدان نام لهاد ‪:‬‬

 ‫اصطخر خزاله داشتی و بر شکته فراش‌خاله واساب آن * ویر شکنوان زرادخانه‪ (».‬وقارسامه ‪۰‬‬

 ‫ابن البلخی ‪ ۱۲۱ ۰ ۲۳‬و ‪٩۵۱٩‬‏ ‪.‬‬

-----
 ‫‪-۱۱۹۷-‬‬


‫سه لو بت ه کنابه از ابامکود کی وایام‬ ‫گهوهاث ‏ باکان وهای هوز بر‬
 ‫س‬
 ‫ازنپجدواشراق‬ ‫بوه‬
 ‫ا‪-‬‬‫ناشد‬
 ‫کی‌ب‬
 ‫اانییاوم بدر‬
 ‫وزن چه‌خويك » بمعنی خارخسك‌است‪,‬و آن خاری أ جو‬
 ‫همست ‪-‬ولوبت نواختن را لز گویند‬ ‫وچاشت ه‬ ‫گهوشه ‪-‬‬
 ‫اشد م‬
 ‫نی نقاره زدن چه‌در قدیم سه لوفوتبت‌مینواخته‬
 ‫راا‬ ‫‪۱‬‬ ‫سهل ‪ -‬بفتح اول و سکون انی ولام »‬
‫منا“صتحجر‬
 ‫وضع درد و در راما‬ ‫قفا و ‪٢‬‏فو‬ ‫ا ا ‪۱٩‬‏‬ ‫‪۱‬‬ ‫زر مان باشد؟‬
 ‫‪1‬‬ ‫‪۱‬‬ ‫‪.‬‬ ‫مر ی‬ ‫است ‪. | - ۲‬‬ ‫ار‬
 ‫وابل‬
 ‫شمق‬
 ‫ددر‬
 ‫بمعنی اسان باشد که‬
 ‫ينج وقت شد وینج لومت شهرت بافت‪.‬‬
 ‫‪.‬‬ ‫ونام وزیر هامان هسمت ‏‬
 ‫درست‬
 ‫= بر وزن صفی » راست و‬ ‫سی‬
‫راگویند عموما ‪ -‬وهر چیز راست رسته راخوانند‬ ‫تری‬ ‫‪۰‬معنتی‬
 ‫وهم ب‬ ‫سهم = بر وزن‬

‫خصوصا © ‪ -‬و بمعنی ‪:‬زه و لوچه و لوجوان هم‬ ‫یکان دار را‬
 ‫و در عربی تپیر‬ ‫باشد ‪۴‬‬ ‫وم‬
 ‫‪۳‬‬ ‫آهده است‬ ‫کوبند ‪.‬٭‬
‫د هْنح اول وئانی بتحتانی رسده‬ ‫سیت‬ ‫ه بر وزن سمند ‪ ۰‬کوهی اعت‬ ‫سهنك‬
 ‫عالی را گویند‬ ‫مفوفانی زده ‪ ۰‬عمارت‬ ‫مشپور در ولایت آذرایجان تزدیك بتبریز ‪ ۴‬؛‬


 ‫بیان لست و جهارم‬

 ‫ات و‬
 ‫یت‬ ‫درسین بی نقطه بابای حطی مشتمل بریکصد وینجاه وش‬
 ‫کشنلغ‬
‫روایند و بعربی حجر خوانشد ‪ -‬و بکسر اول‬
 ‫گ‬ ‫ن»‬
 ‫گك‬ ‫اول وسکون اسنی‬ ‫یت»ح‬
 ‫ف‬ ‫س‬

 ‫است ‪ .‬رك ‪ :‬منتهی الارب و فاموس ‪.‬‬ ‫‪-‬یی‬
 ‫عر‬‫‪۱‬‬
 ‫‪ - ۴‬بهلوی ‪ ( 0۳1125‬تریس ‪ ,‬وحشت ) از ‪ 71۵5‬؛‬ ‫رك ‪ :‬منتهی الارب ‪-‬‬ ‫‪۴‬‬
 ‫پارسی استان ‪ 0210-01122-‬٭ = ایرانی باستان ‪ )8۳217-52۲0-‬٭ ‪ 0735,‬از پارسی‬
 ‫=برانی باستان ‪ = 881۳-0126‬ایرای با‪-‬تان ‪_nam_harbt‬‏ * از‬ ‫باستان ‪aÇ ۳2۱۲‬‏ ٭ ا‬
 ‫‏‪ , th rah -‬یبابرآ ‪ ( -1۳25‬ندبزرل ‪ ,‬ندیسرت ) كر[ ‪] :‬ندسرت كر ‪:‬بینركگ كرو؛‪: ۱۹۹‬‬
 ‫‪ - ۴‬کوه تش فشانی قدیمی در ‪۰٩‬‏ کلومتری دریاچه ارمیه ‪.‬‬ ‫نا که ‪.‬‬
 ‫م»‬‫هین‬
 ‫سمگ‬
 ‫سه‬
 ‫ونوب شرقی برشته‌ای موسوم به‌سهند محدود‬
 ‫دهانةٌ آش‌فشالی آن‌کاملا واضح است و ازجنوب ج‬
 ‫میشود که سهقله مرتفع آن در روی خطی ‪ ۰‬تا ‪ ۲۱‬کیلو مثر واقم شده و قلۀ مرکزی آن‬
 ‫‪-‬‏ ‪.‬‬
 ‫بارتفاع ‪ ۶۰۷۳‬متر است ‪ .‬رك ‪ :‬جفرافیای طبیعی ‪ .‬کیهان ‪ .‬ص ‪٩ ۸۵‬‬
 ‫رك ‪ :‬سرو سپی ‪.‬‬ ‫‪۵‬‬
 ‫* سهمگین ‪ -‬و سپمکن (مشذف) از ‪ :‬سهم ( ترس وییم ) ‪ +‬کن ( یود اصان ) ؛‬
 ‫‪ .‬سهمناك ‪:‬‬ ‫یب‬ ‫خوفناکه ) «یب رک ‪ ۹۹۱۰‬ورك ‪ :‬سه‬
 ‫ممپ؛‬ ‫‌آ(ور»‬
 ‫ی‪08‬‬
 ‫بهلوی ‪3‬ن‪18‬ر‪010‬‬
 ‫سهمکین آبی که مرغابی در او ايمن تبودی‬
 ‫آوسحیا سنگه ازکنارش در ربودی ‪-‬‬
 ‫کمترین م‬
 ‫دلتان ‪.* ۷۱۱‬‬
 ‫گ‬
 ‫٭ سهمناك ‪ -‬از ‪ :‬سہم ( ترس و بیم)‪ ۳‬ناکه ( پود اتصاف ) ؛ نرسناکه*سهمگن‪.‬‬

-----
```


## [2026-10-15T02:46:46.697Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'tuvam|tvam|tūm|tava' BQT_v1_pages.txt | head; grep -n -E '^ *تو ' BQT_v1_pages.txt | head"
}
```


### [2026-10-15T02:46:47.200Z] TOOL RESULT

```
2448:تو شته | ند.
17560:تو لك « بنتح اول و ثانی مضوم بواو
18170:تو از داش فیلسوفان روم بکار آر چندی‌درین مرز وبوم
21757:تو کفتی زمین داردی لرز وتب. اسدی‌طوسی
28779:تو بناگه از درخت انبر بگو
28830:تو نبوراکی بدست ومن عکی‌بربط بچنگه.
31416:تو اهه - بفتح اول وهای هوز » قليةٌ | کشیده . بلفت زند و پازند(۱) سیب را گویند
31443:تو بال . و توپال۱ , لفت اول با بای
31469:تو بر لو - با واز مجهول بروزن مو
31478:تو بك - و قو شالت اول با بای ابجد
```


## [2026-10-15T02:46:49.928Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; n=31416; leaf=$(head -n $n BQT_v1_pages.txt | tr -cd '\\f' | wc -c); echo leaf $leaf; for L in $((leaf-1)) $leaf; do awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -70; echo -----; done"
}
```


### [2026-10-15T02:46:50.829Z] TOOL RESULT

```
leaf 754
ححه اي سس
زوسن خاموش‌بودن - و فریب دادن‌هم
0
تنیده ۴ بر ون دسده ۰ سعتی
خاموش کردیده باشد -و معنی دیگر ممروفشت.
نیز ه - با زای هوزبروزن‌منیژه ؛بمعنی
سر 5
طرف وداعن باشد چنانکه اک رکویند « تنیزء
کوه» مراد ازآن دامن کوه‌باشد .
لنین فك » اشاره بمقد رای وذب
است که محل تقاطم فلك حامل قمی بأشد با
عابل <- و مجره را ثبر کون که کاهکشان
باشد(۱) ؟.
نو » پفتح اول و سکون ثالی » بمعنی
تاب است ۳ که تابشآفتاب وامثال آن بلشد -
وجاییرالیژ کونند در صحرا که آب درآن ابستاده
بود و بمریی غدیی خوانند - و بشم اول و ثانی
مجهول بممنی‌پرده ونه ولای باشد چنانکه کویتد
«ثو برتو» بمعنی هرده بر برده ولای برلای و ته
برته6 - و بممنی درون هم هست که در مقابل
بیرون‌است - و فیماق را یز گفته اند . وان
پرده ای باشد که بر روی شیر بندد - و با انی
صاکن ممروف است که بعریی ات گویند9ا -
و بینی خود هم آمده است که آنرا خویش
وخویشنن‌خوانند- ومهمالی وضبافث‌راهمه ی گویند.
و تلف باشد .
رکد: تنودن.
۴ - رة: تابونپ.
و یه « بر وزن‌خرابه . تام مبارزی‌است
تورائی که مسر او برته نام داشت.
و اده « بفتح اول بر وزن شراره .
شیمن و خانه ودبواری را کویندکه از تی‌وعلف
سازند - و بضم اول خار سر دیوار و دور باغ
وفالیز باشد - و خانه‌ای را ی زکویندکه درآن
کاه وس ر کین و پلیدبها رز ند .
تواسی -. یکر اوذ و ثانی بالف
کشیده وسن یی نقطه بتحتانی رسیده » فرش
منقش را گوبند مانند قالی وکلیم وپلای‌الوان.
و اععج ه بن‌اول وثانی بالف کشیده
و فتح غین نقطه دار وسکون جیم , بلفت ددحی
فلع پوست درختی است» وآن سفید و بسیار تلخ
می‌باشد . بواسیر رانافم است.
۴ - یز تنین - ادهای
۲ -رله: توی, ۲ -توضمیر
دومشخص مفرد (مفرد مکلطب). فردوسی هم 40 وهم 8۵ استممال کرده . پارسی باستان ۱1۷860
(تو)؛ اوستا ۲01 ,۰4۷۵۲۵ 4۵ ,2۷2 ؛ (یز 1۱۵8, 1۷3۲0 «بارتولمه *۹ ابرالی باستانی
0 3 ثبر گه ۲۹ یازند ۵ (00), عندی باستان 0 12۷2۵. ارمنی لاه (تو) , کردی
0 ,اففانی شاء امتی لا وله «استق 61۰۰ «هویتمان 44۰۰ نیز استی 426 «ل. است ۹۱۱۷ ۰
کیلکی 1۵ .
-----
ی ت یخن نازكك و کباب
هم‌آمده است .
تواهی ه بر وزن و ممنی تباهی
ات که نابود کرده شده و خابع گردیده وبکمال
نرسیده باشد ۰
توان نم اول پروزن جوان . قوت
وقدرث رتوالایی باشدا - و بمعنی ابر هم هست
که بمریی‌سحاب گویند- وممکن بودن هرچیزرا
یز کنته‌اند؟ .۶
وافچه؟ - بروزن ومعنی‌یانچه‌است
که بعربی لطمه گوبند .# قها۷ » بنم اول و بای فرسی بالف
تو اهه - بفتح اول وهای هوز » قليةٌ | کشیده . بلفت زند و پازند(۱) سیب را گویند
بادنجان را کوبند - و کوکو ۴ وخاکینهرا نیز . | وجربی تفاح خوانند .
- اوستا - 1۵۷ ۵ ( توانستن , قدرت داشتن ) ۰ 62] 2۷2 » پهلوی ۷28 ,
هندی باستان -52۵۷, 12۷141.ارمنی 46۷617 (ماندن» دوام کردن . تحمل کردن» استقامت -
داشتن) «اسشق 4*۱* «نبر ٩۷۲۸۵‏ .«مسینا ۱4۹ :۰0۲ ۴ -بمعنی اخیردر دساتیر آهده
۱۳ ۴ -لفتی است‌در: تیانچه (عم) . ۴ .ره :ک وکنك وکوکو .
۵ رك: تباهی . ۱ -مز» ۵02 20۳2), پهلوی 96۷»,سب «یونکی ۱۱۸.
۵ قوافا -لفةبشم‌اول (درتداول امروز بفتح),از: نوان ۱-۲ (پسوند فاعلی باصفت مشبهه)؛
قادر, کسیکه ازعهد؛ انجام کاربرآ ید زورمند, نیرومند:
مبازوان توانا و فوت سردست خطاست ینجهٌ مسکین ناتوان بشکست .
کلتان ۲۹*.
۵ قوالستن -لفةیض‌اول (در نداول امروز بفتح) وکسر چیارم (در لهِجدُ مرکزی)؛ از :
توان ۲+ ستن (پسوند مسدری)؛ پهلوی ۷۵0)1(50217) «اسشق 4۰۱ [رك: توان] ؛قدرت‌داشتن
مقثدر بودن .
توالنگر لغب اول (درتداول امروز بفتح) وفتح پنجم, جهلوی ۱۷20-127 «اونوالا
۵ «منا ٩۲:۱4‏ ؛ ترونمند» مالدار» غنی؛
کر کنن خاه مهد نز کی نشناسد توانگر از دروش.«گلتان ۵۱*.
۵ توانگری -لفتنم اول(درتداول امروز بفتح) وفتح پنجم , پهلوی 0۷۵-18:110)
«ب رکه ۰۲۲۸ « اونوالا ۰۵۳٩‏ مالداری» روت .
۵ قوپ _ازتر کی, سلاحیاستآتشین
دارای لوله‌ای بزر که از آهن بامفرغ که برروی
چرخ حمل‌شود- بك‌بته ازقماش‌وجز آن- توپ
زدن » توپ الداختن- در اصطلاح فمار . بروی
دست حرف برخاستن درصورنیکه دست خود
پت‌تر ازدست حربف‌باشد. «ناظم‌الاطباه» -نوپ توب
و ثشر زدن » سختان درشت و سخت بک یگفتن .
۵ توب‌جی -ازن رکی, لشکری که بانوپ کار کند , که‌سلاحش توپ است
-----
```


## [2026-10-15T02:46:54.911Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *[0-9]+ +(tγw|tw|ty|tγ'w)\\b|\\b(tγw|tγ'w)\\b\" SOD_pages.txt | head -20; awk 'BEGIN{RS=\"\\f\"} NR==450' SOD_pages.txt | head -30"
}
```


### [2026-10-15T02:46:56.137Z] TOOL RESULT

```
31205:9515 ty B, S      • JL*. j& ttsJj*- ^>*jjj -'j <>■**                 OPar ©ob. -y ^Ob^qy*, 8p>r
31324:                                                               9566 ty- ? B                                        jL^
31704:                                                            9702 tw>nty-str S                                    jftij
31845:9738 ty' S, C                                                 y
 syrnWk                                                                                                               382

 9444 syrn'm'k     B                        jM^'fiJ1**-              siryaktya   ©ob. -y ^sy^kty*, syrkty*
      sir-name     (syrntoy)
      famous                                                         BBB
                                                                     good 627;
                                                                           deed S W, C2, 133n 1, 17, syryWktfy
       BSTBL, Intox. 9; Hen. Tales. 473.7; Gersh. Sogd.
         Cpds. 1945, 144.1; CII 1990 G2                        9458 syryy(h) M =» syr'k1, syr-y
                                                               9459 sys
                                                                    thirtyM, C                                         ^
 9445 syri^my S =* syrn'm'k                                         sis ©Av. Orisqs
 9446 syrng'ryy M, C                          UjL <jf&
      sir-angare (syrnk^y) ^sy^nk^y                                  GMS 1316, 1323; BSTii 89528; C2, 54R28
      pious                                                    9460 syst C, M                                        x^-
      GMS 73 n 1; STii 1.66; VJ 412
                                                                    sesat ©Parth. hrysd
9447 syrnkVk =* syr'nk^y                                             three hundred
9448 SyrnkVy =» syrng>ryy                                            STii 1.82; BBB p84, 701
9449 syrpfiy S        (^^/ cJLt>)xj>jjj ^UU ^Ijb ^X            9461 sys- B, M                        joic-uil < jai.juf I>t
     sir-pa5e                                                       sis ©pass. st. ^s-, systk
     having good feet(/or horse)                                    (to )be scattered, (to)be dispersed
      MDii pl57.12B-9Rll                                            GMS 540, 706; BSTBL, Dhy. 23
9450 syrsy- B                                  Oj£J^>-         9462 sysq    C =* sysk-y(y)
     sir-say
                                                               9463 sysk-y(y) B, M                        J^. <ft>s <S±^
      GcOrejoice                                                    sisk (ssky, sysq) ©*siska <*sraska\ Parth. srsk
      SCE 524
                                                                      ©nom.
                                                                    tear, dropace. ob. ~y(y)\ abl. ->; pi. -r =*cskw
```


## [2026-10-15T02:46:59.542Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 31200,31215p SOD_pages.txt; sed -n 31840,31852p SOD_pages.txt; grep -n -E \"^ *9[89][0-9]{2} +(tγw|tw|tγ'w|tyw)\" SOD_pages.txt | head; grep -n -i -E 'thou|\\byou\\b' SOD_pages.txt | awk -F: '$1>31000 && $1<32500' | head"
}
```


### [2026-10-15T02:47:00.057Z] TOOL RESULT

```
     Sund. Man. Lett. 305.19; GMS 637                             TSP 2.1113, 7.138, 24.2; Hen. Tales. 478.2.30,
385

        478.6; Mack. BSOAS 1984, 534                           9528 8b>r C                                            -uja
                                                                                                                   8brt-
9515 ty B, S      • JL*. j& ttsJj*- ^>*jjj -'j <>■**                 OPar ©ob. -y ^Ob^qy*, 8p>r
     tay ©Skt. ayatana ©pi. -t                                       gift, giving
     entrance(/c»r sense organs)                                     C2, 51V28
     TSP 2.1043 etc.; Frag. Len. 103R2; Mack. BSTBL,           9529 8b»r ywz C                           \jf «£ju> jl=J ^
       Notes pl5.15                                                  G^r-xoz
                                                                     asking for alms, beggar
9516 tywny      B, S                           cJ^<^>
                                                                     STi 42.4; GMS 57 n 1, 921; Gersh. Sogd. Cpds.
      tayune, tayoni (t}ywnyy, t}ywny)                                 1945, 144.5
      theft
      TSP 9.15; BBB plOO e 6, GMS 1087; Frag. Len.             9530 BbVqy* C                      ^Sia^ijjl**
     (to)set, 0<?)go down                                          9748 tymh    B, S =* tym1
     BSTii 827.48: C2, 94V 18; GMS 662; Gersh.                     9749 tymn    B                                ojljxjyjxjl
       BSOAS 14, 1952, 488f; AVS 136
                                                                         timanagain,
                                                                         still, ^tym1then
9738 ty' S, C                                                 y
     te, ti ©<*tai ©2sg. pers. pron. gen. =4-t                           TSP; BSTBL; STii 7.6; -w, TSP 2.724, 741; Frag.
                                                                           Len.
     you, of you
     MDii p218; C2 p77.31, 31V3151V6,9                             9750 tymp^y C    (^j ^ cmJj^J)^>-<^I^a < jbl^ jU^
                                                                        tem-pase ©<*pa0raka
9739 ty2 B         (0^^^^)^^^^^*^                                       inn-keeper
     ti Ozwty) ©in compd. with pron. indf. adj. &
31085:       you Lett. 3.5, 19, 4.7; GMS 1357; S W, C2 p77.31           9482 t'ny'kh B                             oal><o>«>U.
31091:     you, thou                                                    9483 t'ny'nkh =» t>ny>kh
31113:      you, thou                                                        summit, forehead
31116:        848.5ft C2 gloss. p227; tyfsy "to you", C2 p227           9488 tVk     B,S                             J"Jt«£js
31389:       you, thou                                                9589 tmV
31687:                                                                  thou
31694:      TSP 5.55 n p20l; GMS 10l3n 1                               you,
31695:                                                                   Vf\ thou, your, of you, with you, to you
31785:       toz (twz-) -»twyt-, tw*z-, twz-                                    and you
31848:     you, of you
```


## [2026-10-15T02:47:02.937Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 31080,31095p SOD_pages.txt; sed -n 31680,31700p SOD_pages.txt; for n in 31091 31695; do head -n $n SOD_pages.txt | tr -cd '\\f' | wc -c; done"
}
```


### [2026-10-15T02:47:03.889Z] TOOL RESULT

```
9470 -t S                                         y                     so and so
     (s)t ©<OP taiy ©2sg. encl. pron. gen. =*tyw,                       TSP 5.90, 106, 17.23; STii 4.14; C2, 57R1; Hen.
          ty1, tw>, -f, -tn1, ty1                                         BBB 67.540; Benv. Notesiii 226; tym% TSP
                                                                          172; S W, JRAS 1990, 10-2
      Anc.
       you Lett. 3.5, 19, 4.7; GMS 1357; S W, C2 p77.31           9482 t'ny'kh B                             oal><o>«>U.
                                                                       tanyak (tfnytokh)
9471 Vp S =» t>f>                                                      honour, dignity
9472 t'P'kCh) B,S                                   ly<y
                                                                        TSP 8.69, 8bis. 3; SCE 17, 18
     tafatk) (t>p>) ©ace.; dat. ^t'P
     you, thou                                                    9483 t'ny'nkh =» t>ny>kh
     GMS 1352; VJ 60b, 304, 1145, 1451; MDii p212;                9484 t*p- C, M, S            ^JfJ* <^->-** l&£ j**
       Anc. Lett. 2.41, 58; KG pl90, rVJfc, 457; tyfik,                tap ©ftap-, *tapaya- ©pt. tfit =»tpt-
       MDii B17R3; t}flks}r, Anc. Lett. 3.21; tyJ3yk syn
                                                                        (to)seal
 trxqy'q                                                                                                           )y

      BSTi 846.23: C2, 69R21, 24; ace. f. trxq\ MSP               C2, 60R17; C2 n pl31.17; BSTii 889.117; Benv.
           M69; trxkw, trx'ky, Mack. AI 25, 424, 8                 Eti 310; S W, C2, 60R17 n pl31, 0tyyq 0>br,
 9688 trxqy'q C                                       J*k          "encouraged, consoled"; Bailey. AI 24, 14
      tarxkyak, trxakyak ©+ prepos. pr. adv.                9700 tw M                               (^jj^zjl
      bitterness, bitterly                                        to ©2sg. pers. pron. nom. =»tyw, Vf\ tw*
                                                                  thou
      C2 p83, 39R8, 68V 2; trxy'q, Sund. AoFviii 1981,
        186, 23R 9 nl83 p218                                     GMS 1349

9689 trzmncyk(,) B                           ^l/b^^         9701 tw}         {oy> j^a j->)(^0y *><>y ^<y J* Aj'y
     tarzamancik =»tr-\ trzmnw                                   twa, towa   ©2sg. pers. pron. ace. & ob. =4tyw,
      premature
      TSP 5.55 n p20l; GMS 10l3n 1                               you,
                                                                   Vf\ thou, your, of you, with you, to you
                                                                        tw, ty1
                                                                 EGSii 113f; GMS 1350, 1393; VJ pl20; TSP
9690 trzmnw      B                           ^ftw-i^               3.203, 218; Dhu. 113, Dhy. 366; C2; STii 598;
      tarzam(a)anu (trzmnw) =»tr-!                                 STi; Sund. AoFviii 1981 p218; Frag. Len. pi 10;
      untimely
450
459
```


## [2026-10-15T02:47:10.210Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -40; grep -n -E 'ترس|هراس' data/verification/sources/refs/incoming/FFD/FFD_pages.txt | head"
}
```


### [2026-10-15T02:47:10.690Z] TOOL RESULT

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
1286:ترسیدن
1287:«ترسید) ماده ماضی جعلی است. از مادهٌ مضارع ساختة شده است.
1288:ترس < فارسی میانه 1158 + ایرانی باستان 1782 < 178-8-4. برای 2 > آرای. 5 برای
1290:‏به 9 بدل و در 5 ادغام شده است. «هراسیدن» هم از 158 آمده است. -> هراسیدن.
2185:۱ هراسیدن
2187:«هراسید» مادةٌ ماضی جملی است: از ماده مضارع ساخته شده است.
2189:هراس + پهلوی اشکانی 21739 < ایرانی باستان ۵:392* + ۵73-9-8*. برای 2۵ >
2191:است, با ابدال 1 به ۰0 ريشهٌ 1۳8 به معنی «ترسیدن» است» ۰28739 که از صورت بالاندهٌ
2192:ريشةٌ 12 آمده به معنی «ترساندن» است. «ترسیدن) هم از 15 آمده است > ترسیدن.
2576:8 (ريشةٌ ضعیف + 6۵۷) ۶۲ (ريشه < ترسیدن) ۰۴۶ ۸۱
```


## [2026-10-15T02:47:13.000Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; sed -n 1280,1295p FFD_pages.txt; sed -n 2183,2195p FFD_pages.txt; for n in 1286 2185; do head -n $n FFD_pages.txt | tr -cd '\\f' | wc -c; done"
}
```


### [2026-10-15T02:47:13.490Z] TOOL RESULT

```
است -> تفتن» تفسیدن.
تاب < فارسی میانه 130 < ایرانی باستان 130-8*. برای 2 -> آرای.
تراشیدن
«تراشید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
تراش < پهلوی اشکانی 1۶385 < ایرانی باستان ۸۲33-2*. برای ۵ -> آرای. 8735 صورت
بالاندةٌ ریشهٌ 1525 است. 1728 و 5 هر دو «بریدن» معنی می‌دهند.
ترسیدن
«ترسید) ماده ماضی جعلی است. از مادهٌ مضارع ساختة شده است.
ترس < فارسی میانه 1158 + ایرانی باستان 1782 < 178-8-4. برای 2 > آرای. 5 برای
ساختن مادةٌ آغازی از ريشه به کار می‌رفته است. 17 صورت اصلی 178 است» « پیش از ‎٩‏
‏به 9 بدل و در 5 ادغام شده است. «هراسیدن» هم از 158 آمده است. -> هراسیدن.
تفتن
تفت < فارسی میانه 12 < ایرانی باستان 1۵۳-4*. برای 18 -> آراست. 1۸0 صورت
اصلی 1۶ است. 0 پیش از 1به ۶ بدل شده است.
تب < فارسی میانه 120 < ایرانی باستان 1۵0-2*. برای 2 -> آرای. «تأافتن» از ريشهٌ
130 به معنی «گرم‌شدن» آمده است. -> تافن و تفسیدن.
ویراستن
> پیراستن
۱ هراسیدن

«هراسید» مادةٌ ماضی جملی است: از ماده مضارع ساخته شده است.

هراس + پهلوی اشکانی 21739 < ایرانی باستان ۵:392* + ۵73-9-8*. برای 2۵ >
آرای. ۶ برای ساختن مادهٌ آغازی به کار می‌رفته است. 073۳ صورت بالاندةٌ ریشه 17۳
است, با ابدال 1 به ۰0 ريشهٌ 1۳8 به معنی «ترسیدن» است» ۰28739 که از صورت بالاندهٌ
ريشةٌ 12 آمده به معنی «ترساندن» است. «ترسیدن) هم از 15 آمده است > ترسیدن.

هستن, استن

50
85
```


## [2026-10-15T02:47:22.063Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tres-|PIE tres-\" \\\n\"https://en.wiktionary.org/wiki/ترسیدن|tarsidan\" \\\n\"https://en.wiktionary.org/wiki/ترسا|tarsa\" \\\n\"https://en.wiktionary.org/wiki/هراس|haras\" \\\n\"https://en.wiktionary.org/wiki/سهم|sahm\" \\\n\"https://en.wiktionary.org/wiki/terreo|Latin terreo\" \\\n\"https://www.etymonline.com/word/terror|terror\" \\\n\"https://www.etymonline.com/word/tremble|tremble\" \\\n\"https://en.wiktionary.org/wiki/ترور|Persian teror\" \\\n\"https://en.wiktionary.org/wiki/طرح|tarh\" \\\n\"https://en.wiktionary.org/wiki/مطرح|matrah\" \\\n\"https://www.etymonline.com/word/mattress|mattress\" \\\n\"https://en.wiktionary.org/wiki/materasso|materasso\" \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/túh₂|PIE tuh2\" \\\n\"https://en.wiktionary.org/wiki/تو|Persian to\" \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þū|PGmc thu\" \\\n\"https://www.etymonline.com/word/thou|thou\" \\\n\"https://vajehyab.com/amid/ترور|Amid teror\" \\\n\"https://vajehyab.com/moein/طرح|Moin tarh\" ; do url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"page 513: $note\" 2>&1 | tail -1; done"
}
```


### [2026-10-15T02:47:37.644Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/12c2a353e94a9611.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5a9e71acc93f264d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bf79e1b0df619f94.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e5495ade6deb3aab.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/913eec982a63dcee.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8084ed92595eff1f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f1d50e44eae8ed77.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/42fbeaa5d473439d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7c91153fa9c3b2e8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/51a0a3f30b2aa837.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5d5e489bac4819d9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/43f43e6d20d2f2e1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d458fb05aee3db62.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3107d29386278b0e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8add2845f7795843.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fbc7633622b8bf16.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9af2096c65c97954.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9260be4b9d5a2588.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b7ab6129357a88c8.txt
```


## [2026-10-15T02:47:40.398Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -25 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l)\n  if 'page 513' in d.get('note',''): print(d['status'],d['bytes'],d['file'],d['url'][:90])\""
}
```


### [2026-10-15T02:47:40.774Z] TOOL RESULT

```
-1 39 data/verification/sources/web/f1d50e44eae8ed77.txt https://www.etymonline.com/word/terror
-1 39 data/verification/sources/web/42fbeaa5d473439d.txt https://www.etymonline.com/word/tremble
200 2692 data/verification/sources/web/7c91153fa9c3b2e8.txt https://en.wiktionary.org/wiki/ترور
200 17763 data/verification/sources/web/51a0a3f30b2aa837.txt https://en.wiktionary.org/wiki/طرح
200 7145 data/verification/sources/web/5d5e489bac4819d9.txt https://en.wiktionary.org/wiki/مطرح
-1 39 data/verification/sources/web/43f43e6d20d2f2e1.txt https://www.etymonline.com/word/mattress
200 2685 data/verification/sources/web/d458fb05aee3db62.txt https://en.wiktionary.org/wiki/materasso
200 8858 data/verification/sources/web/3107d29386278b0e.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/túh₂
200 4912 data/verification/sources/web/fbc7633622b8bf16.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þū
-1 39 data/verification/sources/web/9af2096c65c97954.txt https://www.etymonline.com/word/thou
200 693 data/verification/sources/web/9260be4b9d5a2588.txt https://vajehyab.com/amid/ترور
200 850 data/verification/sources/web/b7ab6129357a88c8.txt https://vajehyab.com/moein/طرح
```


## [2026-10-15T02:47:43.178Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -c . index.jsonl; grep 'page 513' index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'],d['bytes'],d['file'].split('/')[-1],d['url'][:90])\""
}
```


### [2026-10-15T02:47:43.625Z] TOOL RESULT

```
5833
200 4650 12c2a353e94a9611.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tres-
200 13996 5a9e71acc93f264d.txt https://en.wiktionary.org/wiki/ترسیدن
200 5745 bf79e1b0df619f94.txt https://en.wiktionary.org/wiki/ترسا
200 8324 e5495ade6deb3aab.txt https://en.wiktionary.org/wiki/هراس
200 13666 913eec982a63dcee.txt https://en.wiktionary.org/wiki/سهم
200 14518 8084ed92595eff1f.txt https://en.wiktionary.org/wiki/terreo
-1 39 f1d50e44eae8ed77.txt https://www.etymonline.com/word/terror
-1 39 42fbeaa5d473439d.txt https://www.etymonline.com/word/tremble
200 2692 7c91153fa9c3b2e8.txt https://en.wiktionary.org/wiki/ترور
200 17763 51a0a3f30b2aa837.txt https://en.wiktionary.org/wiki/طرح
200 7145 5d5e489bac4819d9.txt https://en.wiktionary.org/wiki/مطرح
-1 39 43f43e6d20d2f2e1.txt https://www.etymonline.com/word/mattress
200 2685 d458fb05aee3db62.txt https://en.wiktionary.org/wiki/materasso
200 8858 3107d29386278b0e.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/túh₂
200 4912 fbc7633622b8bf16.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þū
-1 39 9af2096c65c97954.txt https://www.etymonline.com/word/thou
200 693 9260be4b9d5a2588.txt https://vajehyab.com/amid/ترور
200 850 b7ab6129357a88c8.txt https://vajehyab.com/moein/طرح
```


## [2026-10-15T02:47:49.180Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://en.wiktionary.org/wiki/terror|terror\" \"https://en.wiktionary.org/wiki/tremble|tremble\" \"https://en.wiktionary.org/wiki/mattress|mattress\" \"https://en.wiktionary.org/wiki/thou|thou\" \"https://en.wiktionary.org/wiki/terreur|French terreur\" \"https://en.wiktionary.org/wiki/tremo|Latin tremo\"; do url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"page 513: $note\" 2>&1 | tail -1; done; cd data/verification/sources/web; for f in 12c2a353e94a9611 5a9e71acc93f264d bf79e1b0df619f94 e5495ade6deb3aab 913eec982a63dcee 7c91153fa9c3b2e8 9260be4b9d5a2588 d458fb05aee3db62 fbc7633622b8bf16 b7ab6129357a88c8; do echo \"##### $f\"; grep -i -E -A3 'Etymology|From |borrowed|inherited' $f.txt | head -14 | cut -c1-500; done"
}
```


### [2026-10-15T02:48:06.645Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/eddaee03e3ccdf0b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7c0f2f2a53a90f0b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/34411b62c2fb9d4a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2ba62be32147ba82.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b01973d35caa449f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c29b0f5c68ec7ab3.txt
##### 12c2a353e94a9611
 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

--
 Terms derived from the Proto-Indo-European root *tres- (42 c, 0 e) 

 *trés-e-ti ( thematic present ) 

--
 Proto-Celtic: *tarr- ( earlier *tars- , from zero grade *tr̥s- ) 
 Old Irish: tarrach 

 References
##### 5a9e71acc93f264d
 Etymology 

 1.2 
 Pronunciation 
--
 From Wiktionary, the free dictionary

 See also: پرسیدن 

--
 Etymology
 [ edit ] 

 From Middle Persian tlsyt' ( tarsēdan , “ fear ” ) , from Proto-Iranian *tr̥šáti , from Proto-Indo-Iranian *tr̥šćáti , from Proto-Indo-European *tres- . Cognates include Latin terreō , Old Irish tarrach , and Ancient Greek τρέω ( tréō ) .
##### bf79e1b0df619f94
 Etymology 

 1.2 
 Verb 
--
 Etymology 

 2.2 
 Noun 
--
 Etymology 

 3.2 
 Pronunciation 
##### e5495ade6deb3aab
 Etymology 1.1 

 1.1.1 
 Noun 
--
 Etymology 1.2 

 1.2.1 
 Noun 
--
 Etymology 

 2.2 
 Pronunciation 
##### 913eec982a63dcee
 Etymology 1.1 

 1.1.1 
 Pronunciation 
--
 Etymology 1.2 

 1.2.1 
 Verb 
--
 Etymology 

 2.2 
 Noun 
##### 7c91153fa9c3b2e8
 Etymology 

 1.2 
 Pronunciation 
--
 From Wiktionary, the free dictionary

 Persian
 [ edit ] 
--
 Etymology
 [ edit ] 

 Pseudo-Gallicism , derived from terreur , or pseudo-anglicism derived from terror .
##### 9260be4b9d5a2588
##### d458fb05aee3db62
 Etymology 

 1.2 
 Pronunciation 
--
 From Wiktionary, the free dictionary

 Italian
 [ edit ] 
--
 Etymology
 [ edit ] 

 From Arabic مَطْرَح ( maṭraḥ , “ place where something is thrown ” ) .
##### fbc7633622b8bf16
 Etymology 

 1.2 
 Pronunciation 
--
 From Wiktionary, the free dictionary

 This Proto-Germanic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

--
 Etymology
 [ edit ] 

 From Proto-Indo-European *túh₂ .
##### b7ab6129357a88c8
```


## [2026-10-15T02:48:10.648Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in bf79e1b0df619f94 e5495ade6deb3aab 913eec982a63dcee 9260be4b9d5a2588 b7ab6129357a88c8 51a0a3f30b2aa837 5d5e489bac4819d9 fbc7633622b8bf16 3107d29386278b0e 34411b62c2fb9d4a 2ba62be32147ba82 7c0f2f2a53a90f0b eddaee03e3ccdf0b; do echo \"##### $f\"; grep -E 'Persian|Arabic|from|From|Proto|Middle|Old' $f.txt | grep -v -E '^ *(Persian|Arabic) *$|edit|Wiktionary' | head -10 | cut -c1-400; done"
}
```


### [2026-10-15T02:48:11.291Z] TOOL RESULT

```
##### bf79e1b0df619f94
 Toggle Arabic subsection 
 Toggle Persian subsection 
 Borrowed from Persian ترسا .
 From Middle Persian [Book Pahlavi needed] ( tlsʾk' /⁠tarsāg⁠/ , “ Christian ” , literally “ (God) fearer ” ) , from [Book Pahlavi needed] ( tls- /⁠tars-⁠/ , “ to fear, be afraid ” ) +‎ [Book Pahlavi needed] ( -k' /⁠-ag⁠/ ) . By surface analysis , ترس ( tars , present stem of ترسیدن ( tarsidan , “ to fear, be afraid ” ) ) +‎ ـا ( -â , suffix forming adjectives and nouns ) . Sogdian ܬܪܣܐܩ ( trsʾq /
 ( Classical Persian ) IPA ( key ) : /tar.ˈsaː/ 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=ترسا&oldid=93197447 "
 Categories : Arabic non-lemma forms 
 Arabic verb forms 
 Ottoman Turkish terms derived from Persian 
 Ottoman Turkish terms borrowed from Persian 
##### e5495ade6deb3aab
 Toggle Arabic subsection 
 Toggle Persian subsection 
 Arabic Wikipedia has an article on: هراس 
 From Parthian ʾhrʾs ( ahrās , “ fear, terror ” ) .
 ( Classical Persian ) IPA ( key ) : /ha.ˈraːs/ 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=هراس&oldid=93351487 "
 Categories : Arabic terms belonging to the root ه ر س 
 Arabic lemmas 
 Arabic nouns 
 Arabic masculine nouns 
##### 913eec982a63dcee
 Toggle Arabic subsection 
 Toggle Persian subsection 
 → Persian: سهم ( sahm ) 
 Steingass, Francis Joseph ( 1884 ), “ سهم ”, in The Student's Arabic–English Dictionary ‎ [2] , London: W.H. Allen, page 515 
 Lane, Edward William ( 1863-1893 ), “ سهم ”, in Arabic-English Lexicon , London: Williams & Norgate, page 1454 . 
 From Arabic سَهْم ( sahm ) .
 ( Classical Persian ) IPA ( key ) : /ˈsahm/ 
 Borrowed from Arabic سَهْم ( sahm ) .
 From Middle Persian [script needed] ( sahm ) , from Old Persian [script needed] ( *çahman ) , from Proto-Iranian *θráhma , from Proto-Indo-Iranian *trásma , from Proto-Indo-European *trés-mn̥ , from *tres- ( “ to tremble ” ) . Doublet of رم ( ram , “ shying ” ) .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=سهم&oldid=93351284 "
##### 9260be4b9d5a2588
##### b7ab6129357a88c8
##### 51a0a3f30b2aa837
 Toggle Arabic subsection 
 Toggle Persian subsection 
 to deduct , to discount , to subtract (five from ten)
 → Middle French: tare French: tare → Romanian: tară 
 → Ottoman Turkish: طاره ( dara ) → Middle Armenian: տառայ ( taṙay ) Armenian: տարա ( tara ) 
 → Classical Persian: طرح → Hindustani: Hindi: तरह ( tarah ) 
 → Arabic: طَرْحًا ( ṭarḥan ) 
 Borrowed from Arabic طَرْح ( ṭarḥ ) .
 ( Classical Persian ) IPA ( key ) : /ˈtarh/ , /ta.ˈrah/ 
 Arabic طَرْح ( ṭarḥ ) bor. 
##### 5d5e489bac4819d9
 Toggle Arabic subsection 
 Toggle Persian subsection 
 South Levantine Arabic 
 Toggle South Levantine Arabic subsection 
 Borrowed from Arabic مَطْرَح ( maṭraḥ , “ place where something is thrown ” ) .
 ( Classical Persian ) IPA ( key ) : /mat.ˈrah/ 
 South Levantine Arabic
 Arabic طَرَحَ ( ṭaraḥa ) 
 Arabic مَطْرَح ( maṭraḥ ) 
 South Levantine Arabic مطرح 
##### fbc7633622b8bf16
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þū
 Proto-Germanic 
 Toggle Proto-Germanic subsection 
 Reconstruction:Proto-Germanic/ þū 
 This Proto-Germanic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Germanic
 From Proto-Indo-European *túh₂ .
 Proto-Germanic personal pronouns
 Proto-West Germanic: *þū Old English: þū , ðū Middle English: þou , thou , þu , thu , þoue , thoue , þowe , thowe , þouȝ , thouȝ , þue , ðhu , þeu , þeou , thugh , thogh , þo , tu , tou , towe , you English: thou , tha ( Yorkshire , Lancashire ) , thow , thu , du ( Scotland ) , thoo ( Orkney ) , yͧ ( obsolete ) 
 Old Frisian: thū , dū North Frisian: Most dialects: dü Halligen: du Heligoland: di 
##### 3107d29386278b0e
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/túh₂
 Proto-Indo-European 
 Toggle Proto-Indo-European subsection 
 Reconstruction:Proto-Indo-European/ túh₂ 
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 Often compared with similar pronouns in other language families of Eurasia, e.g. Proto-Uralic *tinä . Kloekhorst (2008) [ 1 ] proposes that per Anatolian forms such as Hittite 𒍣𒄿𒅅 ( zīk ) , *i rather than *u should be reconstructed in the nominative, which would then suggest an original Indo-Uralic root *ti- .
 A user suggests that this Proto-Indo-European reconstruction entry be cleaned up, giving the reason: “manual table should be moved to a template” .
 Proto-Nuclear-Indo-European
 Proto-Indo-European
##### 34411b62c2fb9d4a
 Arabic طَرَحَ ( ṭaraḥa ) 
 Arabic مَطْرَح ( maṭraḥ ) bor. 
 Old French matras bor. 
 Middle English materas 
 From Middle English materas , from Old French matras , from Arabic مَطْرَح ( maṭraḥ , “ place where something is thrown ” ) , from طَرَحَ ( ṭaraḥa , “ to throw ” ) . Compare divan , from Persian via Turkish (both of Middle Eastern origin, due to the local custom of lying on padding on floor being foreign to Europeans).
 Arabic: فِرَاش   m ( firāš ) , مَرْتَبَة   f ( martaba ) 
 Algerian Arabic: مَطْرَح   m ( meṭraḥ ) 
 Egyptian Arabic: مرتبة   f ( martaba ) 
 Gulf Arabic: دوشق   m ( dawšag ) 
 South Levantine Arabic: فرشة   f ( farše ) 
##### 2ba62be32147ba82
 Middle English 
 Toggle Middle English subsection 
 From Middle English thou , tho , thogh , thoue , thouȝ , thow , thowe , tou , towe , thu , thue , thugh , tu , you ( Northern England ) , ðhu , þeou , þeu , þou ( the latter three early Southwest England ) , from Old English þū , [ 1 ] from Proto-West Germanic *þū , from Proto-Germanic *þū ( “ you ( singular ), thou ” ) , from Proto-Indo-European *túh₂ ( “ you, thou ” ) .
 The English word is cognate with Saterland Frisian du ( “ thou ” ) , West Frisian do ( “ thou ” ) , dialectal Dutch du , dou , douw ( “ thou ” ) , Limburgish doe ( “ thou ” ) , Low German du ( “ thou ” ) , dialectal German dau ( “ thou ” ) , German du ( “ thou ” ) , Danish du ( “ thou ” ) , Swedish du ( “ thou ” ) , Norwegian Nynorsk du ( “ thou ” ) , Faroese tú ( “ thou ” ) , Icelandic þú ( “ th
 The informality of thou and its replacement by ye in formal situations date only to the 14th century and come from French influence, since French (as many European languages, but not Old English) uses the second-person plural ( vous ) instead of the second-person singular ( tu ) as a mark of politeness or respect.
 1611 , The Holy Bible,   [ … ] ( King James Version ), London: [ … ] Robert Barker ,   [ … ] , →OCLC , Ephesians 5:14 : [...] Awake thou that sleepest, and arise from the dead, and Christ shall giue thee light. 
 When the subject of a verb in the indicative mood is thou , the verb usually ends in -est , in both the present and simple past tenses, as in “Lovest thou me?” (from John 21:17 of the King James Bible). This is the case even for modal verbs, which do not specially conjugate for the third person singular.
 Arabic: أَنْتَ   (ar)   m ( ʔanta ) , أَنْتِ   (ar)   f ( ʔanti ) 
 Egyptian Arabic: انت   m ( ínta ) , انت   f ( ínti ) 
 Tunisian Arabic: اِنْتِ   m or f ( ʔinti ) 
##### 7c0f2f2a53a90f0b
 From Middle English tremblen , from Old French trembler , from Late Latin tremulāre , ultimately from Latin tremere ( “ quiver, shake ” ) . Cognate with Ancient Greek τρέμω ( trémō ) .
 The dog was trembling from being in the cold weather all day. 
 Arabic: اِخْتَلَجَ ( iḵtalaja ) , اِرْتَجَفَ ( irtajafa ) 
 Iraqi Arabic: رَجَفْ ( rajaf ) , اِرْتَجَفْ ( irtajaf ) 
 Moroccan Arabic: اترعد ( ttarʕad ) 
 Middle Korean: 드러〮치다〮 ( tùléchìtá ) 
 Old English: bifian 
 Persian: لرزیدن   (fa) ( larzidan ) 
 Arabic: رَجْفَة   (ar)   f ( rajfa ) 
 English terms derived from the Proto-Indo-European root *trem- (0 c, 19 e) 
##### eddaee03e3ccdf0b
 Proto-Indo-European *tres- 
 Proto-Indo-European *-yeti 
 Proto-Indo-European *-éyeti 
 Proto-Indo-European *troséyeti 
 Proto-Italic *troseō 
 Proto-Indo-European *-os 
 Proto-Indo-European *-s 
 Proto-Indo-European *-ōs 
 Proto-Italic *-ōs 
 Old French terreur
```


## [2026-10-15T02:48:15.617Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://abadis.ir/fatofa/طرح/|Moin/Amid tarh\" \"https://abadis.ir/fatofa/ترور/|Amid teror\" \"https://abadis.ir/fatofa/مطرح/|Moin matrah\"; do url=\"${u%%|*}\"; note=\"${u##*|}\"; f=$(python3 tools/fetch_source.py \"$url\" --note \"page 513: $note\" 2>&1 | tail -1); echo $f; grep -E 'عمید|معین|فرانسوی|عربی|\\[' $f | head -12 | cut -c1-400; done"
}
```


### [2026-10-15T02:48:20.002Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/40344c12abdd1ea4.txt
 طرح. [ طَ ] ( اِ ) خُچ. درختی است که میوه آن قابل استفاده میباشد و از آن در جنگلهای ایران موجود است.
 طرح. [ طَ ] ( ع مص ) انداختن : طرحه و طرح به ؛ انداخت او را. دور گردانیدن. ( منتهی الارب ) ( آنندراج ). بیوکندن. ( زوزنی ). افکندن. بیرون انداختن. نبذ. ترک. واگذاشتن. بگذاشتن. گذاشتن. بینداختن. || گستردن. انداختن. پهن کردن. کناره گرفتن از کاری. ( غیاث اللغات ) ( آنندراج ) : و خواجه سخت بزرگ بودی در روزگار، اکنون خواجگی طرح شده است و این ترتیب گذشته است. ( تاریخ بیهقی چ ادیب ص 353 ). || فروختن جنس
 فرهنگ معین
 (طَ ) [ ع . ] ۱ - (مص م . ) انداختن ، دور کردن ، افکندن . ۲ - پیشنهاد کردن . ۳ - نقاشی کردن . ۴ - طرح اولیة چیزی را برداشتن . ۵ - فروختن جنسی به زور به رعایا. ۶ - گستردن ، پهن کردن . ۷ - (مص ل . ) کناره گرفتن از کاری . ۸ - (اِمص . ) بیرون اندازی . ۹ - (اِ. ) 
 فرهنگ عمید
۸. (اسم مصدر ) [قدیمی] دور انداختن، حذف کردن.
۹. (صفت ) [قدیمی] ویژگی آنچه به زور و اجبار فروخته شود.
* طرح افکندن: (مصدر متعدی ) [قدیمی] طرح ریختن، بنیان نهادن، پی افکندن.
* طرح ریختن: (مصدر لازم ) [مجاز]
۳. [قدیمی] فروختن.
۴. [قدیمی] دور انداختن، رها کردن.
۵. [قدیمی] تحقیر کردن. 
/home/sfmqrb/git/rishe-private/data/verification/sources/web/31d064fc8da68078.txt
 ترور. [ ت ُ ] ( ع مص ) بریده شدن و بریدن چیزی را. ( منتهی الارب ) ( آنندراج ). لازم است و متعدی. ( آنندراج ). || دور افتادن از شهر خویش. || بیرون افتادن استخوان. ( منتهی الارب ) ( آنندراج ). || ساقط شدن دست. ( منتهی الارب ). || فربه و با گوشت شدن. ( آنندراج ). به همه معانی. رجوع به تر [ ت َ ر ر ] شود.
 ترور. [ ت ِ رُ، رْ ] ( فرانسوی ، اِ ) مأخوذ از فرانسه و بمعنی قتل سیاسی بوسیله اسلحه در فارسی متداول شده است. تازیان معاصر اِهراق را بجای ترور بکار برند و این کلمه در فرانسه بمعنی وحشت و خوف آمده و حکومت ترور هم اصول حکومت انقلابی است که پس از سقوط ژیروندنها ( از 31 مه 1793 تا 1794 م. ) در فرانسه مستقر گردید و اعدامهای سیاسی فراوانی را متضمن بود. رجوع به تروریست شود. 
 فرهنگ معین
 (تِ رُ ) [ فر. ] (اِ. ) ۱ - هراس ، هراس افکندن ، ایجاد وحشت کردن . ۲ - کشتن ناگهانی یک فرد بدون آن که فرد مورد نظر فرصتی برای دفاع یا مقابله داشته باشد. ، ~شخصیت با دروغ و جوسازی شخصیت اجتماعی کسی را زیر سوال بردن و وجهة اجتماعی او را مخدوش کردن . 
 فرهنگ عمید
 [علوم سیاسی و روابط بین الملل] ← قتل سیاسی 
 [ویکی فقه] تروریسم به عنوان کاربرد زور یا تهدید به زور در داخل یک کشور به منظور ایجاد ترس و وحشت در جامعه، تضعیف و حتی سرنگونی نهادهای موجود و ایجاد تغییرات سیاسی تعریف شده است.
 [ویکی فقه] ترور (قرآن). ترور یا اعدام انقلابی نوعی قتل عمدی شخصی مهم می باشد که با هدف کیفر و یا با اهداف سیاسی انجام می گیرد. فرد کشته شده دارای مقام یا شهرت یا علایق سیاسی است و یا به دلیل اهانت به یک مرام عقیدتی مانند یک مذهب مورد سو قصد قرار می گیرد.
اصطلاحی فرانسوی به معنی رعب و وحشت فوق العاده و نیز به وحشت افکندن. نخستین بار در انقلاب فرانسه به دوره ای (۱۷۹۳ـ۱۷۹۴) اطلاق شد که در آن انقلابیون به دستگیری و اعدام مخالفان خود پرداختند و بیش از ۳۰۰هزار نفر را زندانی و ۱۷هزار نفر را با گیوتین اعدام کردند. این دوره را «حکومت ترور یا وحشت» نامیده اند. اصطلاح ترور کم کم در عرف سیاسی به عمل حکومت یا گروه ها و افرادی اطلاق شد که برای حفظ قدرت یا مبارز
 فارسی به عربی
 ... [مشاهده متن کامل] از سال ۱۷۸۹ به هراس گروهی گفته شده یعنی کاری که باعث ترس گروهی و یا هراس یک رژیم می شود. ( Le Petit Robert 1 )
 ترور واژه ای فرانسوی است و به مفهوم وحشت و حکومتی که با ایجاد وحشت اداره می شود می باشد این واژه از �ترور� در زبان لاتین و به معنای ترس و لرز گرفته شده و آنهم از واژه �ترس� در زبان فارسی گرفته شده است . 
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b5ef55ccf7df1e25.txt
 مطرح. [ م َ رَ ] ( ع اِ ) جای انداختن چیزی. ج ، مطارح. ( غیاث ) ( ناظم الاطباء ) ( آنندراج ). جای و مقام و محل و جای نهادن چیزی وجای طرح. ( ناظم الاطباء ). جایی که چیزی در آن اندازند. ( از اقرب الموارد ). || جایگاه. قرارگاه. خاصه جائی که حیوانات در آن بسر برند : 
 مطرح. [ م ِ رَ ] ( ع ص ) طرف مطرح ؛ چشم دوربین. ( منتهی الارب ) ( ناظم الاطباء ) ( از اقرب الموارد ). || رمح مطرح ؛ نیزه دراز. ( ناظم الاطباء ) ( از اقرب الموارد ). || فحل مطرح ؛ گشن که موقع منی او دور باشد از رحم ماده. ( منتهی الارب ) ( از ناظم الاطباء ) ( از ذیل اقرب الموارد ).
 مطرح. [ م ُ رِ ] ( ع ص ) آن که می افکند و دور میگرداند. ( ناظم الاطباء ).
 مطرح. [ م ُ طَرْ رَ ] ( ع ص ) افکنده شده و دور کرده شده. ( ناظم الاطباء ). و رجوع به تطریح شود. || نااستوارخلقت. ( از ذیل اقرب الموارد ) ( از لسان العرب ). || قول مطرح ؛ قولی که بدان توجه نشود. ( از اقرب الموارد ). || بنای طویل و دراز. ( آنندراج ) ( ناظم الاطباء ). 
 فرهنگ معین
 (مَ رَ ) [ ع . ] (اِ. ) ۱ - جای طرح کردن ، جای افکندن . ج . مطارح . ۲ - مورد بحث . 
 فرهنگ عمید
۲. (اسم ) [قدیمی] محل طرح کردن، محل انداختن، جای افکندن. 
 شهرستان مطرح ( به عربی: ولایة مطرح ) یکی از شهرستان های استان مسقط در کشور پادشاهی عمان است. شهرستان مطرح یکی از شهرستان های شش گانه استان مسقط است، بلکه از مهم ترین شهرستان های این استان می باشد. تاریخ این شهرستان به دوران بسیار دور بر می گردد ویکی از قدیمترین بنادر عمان است که به وسیله اسکله مشهور مطرح کالاهای مختلف به نقاط دنیا صادر می گردد. 
 مطرح. [ م َ رَ ] ( ع اِ ) جای انداختن چیزی. ج ، مطارح. ( غیاث ) ( ناظم الاطباء ) ( آنندراج ) . جای و مقام و محل و جای نهادن چیزی وجای طرح. ( ناظم الاطباء ) . جایی که چیزی در آن اندازند. ( از اقرب الموارد ) . || جایگاه. قرارگاه. خاصه جائی که حیوانات در آن بسر برند : 
 ... [مشاهده متن کامل] 
مطرح. [ م ِ رَ ] ( ع ص ) طرف مطرح ؛ چشم دوربین. ( منتهی الارب ) ( ناظم الاطباء ) ( از اقرب الموارد ) . || رمح مطرح ؛ نیزه دراز. ( ناظم الاطباء ) ( از اقرب الموارد ) . || فحل مطرح ؛ گشن که موقع منی او دور باشد از رحم ماده. ( منتهی الارب ) ( از ناظم الاطباء ) ( از ذیل اقرب الموارد ) .
```


## [2026-10-15T02:48:26.763Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo \"## WLD\"; grep -n -E '^ *(tres-|ters-)|tres- .zittern|très-' incoming/WLD/WLD_Bd1_pages.txt | head -5; grep -n -E '^ *tu[ ,]|^ *tū' incoming/WLD/WLD_Bd1_pages.txt | head -5; echo \"## SKT\"; grep -n -E '^(terror|terrible|mattress|thou|tremble)[,. ]' SKT.txt | head; echo \"## LKT\"; grep -n -i -E 'matra[hḥ]|materasso|matelas' LKT.txt | head -5; echo \"## DEV\"; grep -n -i -E 'matelas|materas' DEV.txt | head -3; echo \"## PHN\"; grep -n -i 'matelas' PHN.txt | head -3; echo \"## DOZ\"; grep -n -i -E 'matras|matrah' DOZ.txt | head -3; echo \"## SYN\"; grep -n -i -E 'tremble|thou\\b' SYN.txt | head -5"
}
```


### [2026-10-15T02:48:27.664Z] TOOL RESULT

```
## WLD
69778:ters- ,.trocknen, verdorren: Durst, diirsten                                                                                                    -
71998:tres-, ters- (** teres-) „zittern".
49850:tu ,     -aft,         galsti         „saumen,         sick   aufhaltcn,      zogern,     nachlassen“,    gaismti
70491:                                                          tu,   tutu   — tul(o)-                                                        745
70502:tu, tutu Yogelruf; auch von andern dunkeln Schalleindrucken.
70508:                                                                                                                       tu u         usque
70535:tu „du“, Stamme                          la-, tern,      teiie-,   tuo-, tuc-          und (vgl. ai. te, gr. toi, lat. fP,
## SKT
8023:terrible.  Formed  with  suffix  -He  ^ike (rom  grosen  •  «■  grprcn,  pp.  of  gre6san, '.« afflict  with  hoiror.  AIHm  lo  G.grttusi^ causing  horror,  and  to  QruMome.
19433:terrible.  tF.  -  L.)  F.  terribU.  -  L. terribilis,  causing  terror. —  L.  terrere^  to frighten.
## LKT
3323:1446.  Ar.  matralt: 'Ort,  wohin  etwas  geworfen  oder  gelegt wird ;  Kissen' ;  hieraus  it.  materasso, materassa  'Matratze',  denn  diese  war ursprünglich  ein  Netz,  das  man  auswarf, wo  man  sich  hinlegen  wollte;  prov.  al- mairac,  frz.  materas,  matelas,  kat.  alma- trach,  matalds,  sp.  py.  almadraque  'Ma- tratze', pg.  dem.  ahnadraguexa,  verkürzt almntrixa  'Pferdedecke',  pg.  madrago 'Faulenzer':  engl,  maitress,  ndl.  mafras, disch.  Matratze,  russ.  matrac,  poln.  ma- terac,  öech.  matrace.   [Dozy  Oost  63  ff.
6625:mahalep  135ti maharadja  1692 mahari  1"560 mahonfnje  144!) maimon  1365 malamoque  1384 malcuss  dial.  1379 mamlouk  1381 manimouth  1385 inandole  2016 mandore  2015 mangliev  1394 mangoustan  1395 mangue  1393 manguier  1393 «irtiime  1398 mardbout  141U marcassite  1374 Marion  1417 marionnette  1417 tnaroquin  1406 marotte  1417 mascarade  1436 masque  1436 massepain  1452 masser  1440 massicot  1735 »lai!  1443 matasse  476 matassin  1525 matelas  1446 mater  1443 materas  1446 maugrebin  674 milangine  161 melchites  1379 meranghie  161  • meschin(e)  afz.  1470 mesquin  1470 Messie  1437 migerat  afz.  1476 mimonet  1365 minaret  1463  a miqueht  1469 (grand)  Mogol  1494 moirS  1497 moirer  1497 »MoZoc/?  1379 momie  1510 momine  1365 >noMa  1365 morceau  d' Adam  19 mortaise  1713 mort-de-chien  1478 mosquee  1435 mosquete  afz.  1435 moucayarde  1497 moucre  1507 mousquet  1520 mousseline  1484 mousson  1451 mudzzin  1485
## DEV
1706:Matelas.  Esp.  et  portug.  almadraque ,  prov.  almatrac, ital.  matarazzo  y  maierasso,  bas  lat.  almatracum,  matera- cium,  mataricium,  almatricmm,  vieux  fr.  materas,  mathelas, mnUeral,  matelat.  De  l'arabe  ^-k^  matrah,  lit,  matelas,  dans Boctbor.  Ce  mot  vient  de  la  racine  •^■Ji^  tarah,  jeter,  qui  a donné  un  autre  mot  de  sens  analogue,  iCa^Lb  tarfdia, coussin.
1707:Pour  comprendre  comment  le  lieu  où  l'on  jette,  ou bien  la  chose  jetée  [matrah,  motrah)  a  pu  s'entendre  d'un lit,  d'un  matelas,  il  suffit  de  se  rappeler  que  les  Orien- taux n'ont  ou  n'avaient  pas  de  lits  proprement  dits,  à  la façon  des  nôtres,  avec  un  châlit,  mais  qu'une  simple  cou- verture, un  matelas  jeté  à  terre  en  tenait  lieu.  On  peut comparer  les  expressions  latines  stratum,  stragulum,  ratta- chées à  sternere.
1712:Matras.  Vase  employé  dans  les  opérations  chimiques. Ambroise  Pare  écrit  matelas;  on  trouve  au  xiv^  siècle  ma- theras  par  un  th.  Tournefort  parle  de  ^bouteilles  en  cuir faites  en  pyramide  w^  en  usage  dans  l'île  de  Samos  et  ai^- \^Q\ées  mata  ras '^.  Ce  dernier  mot  est  assurément  identique à  l'arabe  «-Lxo  matara,  outre  de  cuir.  En  est-il  de  même de  notre  matras  et  de  l'espagnol  matraz  ?  Silv.  de  Sacy, trouvant  le  mot^lijuoî,  vases,  dans  la  traduction  arabe  de l'évangile  de  saint  Jean  (ch.  n,  vers.  6),  pense  que  c'est un  terme  d'origine  grecque^.
## PHN
## DOZ
1927:MATRAS.
1928:Van het Arab. matrah. Het werkwoord taraha,
1930:werpen y en Freytag geeft voor matrah geene andere
## SYN
10405:OE wé@fels ‘covering’ and ‘cloak’ (e.g. Mt. 5.40), fr. the root of OE (b:-)w@fan, Goth. bi-waibjan ‘wrap about, clothe’ : ON veifa ‘vibrate’, Skt. vip- ‘tremble’, etc. Walde-P. 1.240. Feist 97.
14545:2. Lat. premere (> It. premere), perf. presst, pple. pressus, with frequent. pressdre (> Fr. presser, Sp. prensar; Rum. presa, fr. Fr.), fr. parallel stems *prem- and *pres- (ef. *trem-, *tres- in words for ‘tremble’), outside connec- tions dub. Walde-P. 2.43. Ernout-M. 807 f. REW 6738, 6741.
14594:MHG schit(t)en, NHG schiitten, in MHG also ‘shake hard, move violently’, in this sense OHG scutan : OE sciidan ‘shake, tremble’, OS scuddian ‘shake’, Lith. kutétz ‘shake up’, etc. Weigand-H. 2.805 f. Walde-P. 2.601.
16152:4. Goth., ON skal, OE sceal, ME s(c)hal, NE shall, Du. zal, OHG scal, MHG sol, NHG soll (but NE shall, Du. zal, NHG soll mostly in other uses; as ‘must’ bibl., e.g. thou shalt not steal, or uncommon) pret.-pres. of Goth. skulan, OE, OHG sculan ‘owe’ (11.63). Hence for ‘ought’ NE should, NHG sollte, orig. pret. subj. NED s.v. shall.
16172:‘Ought, must? also expressed by fut. of verb ‘be’, lit. ‘it will be’, e.g. Lith. rytoj bus 7 giria vaziuoti ‘tomorrow we must ride into the forest’ (NSB p. 93; ef. Senn, Lit. Sprachlehre p. 58), Lett. tev nebiis zagt ‘thou shalt not steal’ (Mihl.- Endz. 1.359).
```


## [2026-10-15T02:48:30.855Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 71998,72010p incoming/WLD/WLD_Bd1_pages.txt | cut -c1-300; sed -n 70535,70545p incoming/WLD/WLD_Bd1_pages.txt | cut -c1-250; grep -n -i -E '\\bfear\\b' SYN.txt | head -5; grep -n -E \"'fear'|“fear”|FEAR\" SYN.txt | head -5; grep -n -E '^thou[,. ]|^mattress' SKT.txt | head"
}
```


### [2026-10-15T02:48:31.453Z] TOOL RESULT

```
tres-, ters- (** teres-) „zittern".
   Ai. trasati „zittert"                     (= gr. zqeoj),                    trasta-h           „zitternd“     (= gr. a-zgeozog),
Kaua. trasayati ,,macht erzittern"; av. tarsta- (ar. *trsta „furchtsam"),                                                          t,rra-

saiti ,    ap. tarsatiy „ffirchtet" {*trs-[s]kd                                       = lit. trim      ;
                                                                                                           a.   zuletzt       Trautmann
KZ. 46, 240), Kaua. av. prarahayeiti ,.versetzt in Sehrecken"; vielleicht arm.
erer „Erschfitterung,Beben, Zittern" (* tres-ri-, Bugge Beitr. 13; Hfibsch-
mann Arm. Gr. I 443 f. zieht redupl. er-er vor). Lat. terreo, -ere „in Scbrecken
versetzen, scbrecken", terror „Schrecken“, umbr. tursitu „terreto, fugato".
Gr. zgsco (aor. horn. zgeooai) „zittere, fliehe", k'zegoev • icpojjrjosv Hes., aroso-
rog ,.unerach rock err', zgrjgog {*zgaogog), zgrjgrov „furchtsam, fliichtig" (ver-
achieden von toy gov Harpoon       zayv Hea., daa mit drgaXeog zu *tuer-
tu „du“, Stamme                          la-, tern,      teiie-,   tuo-, tuc-          und (vgl. ai. te, gr. toi, lat. fP,
      ahd. di-h usw.)                        te-,   s.   Bgm. Dem. 30 f., Grdr. II 2 2, 383, 4 0 3 ff                           .   ,
                                                                                                                                        410,
      413ff. m. Lit.; dort                          auch genaueres zu den Flexionsformen.
   Ai. tu,        tu         zur         hervorhebenden und auffordernden Partikel geworden
(siehe Osthoff               HU. IY 268, weitere Lit. bei Bgm. II 2 2, 410, s. auch Bgm.
IF. 33, 175               wegen des
                            vielleicht analogen got. pault, ahd. dolt „doch“),
av. tu     end. „du“      *tim-dm (nach ai. ahum) in ai. tuvdm, team, gthav.
                                     ;
                                           ar.
92:Words for thought processes or emotions are, all theoretically and a great many demonstrably, based upon indicative physical acts or conditions. Thus ‘understand’ from ‘seize, grasp’, or ‘stand on or under’; ‘forget’ from ‘lose’; ‘fear’ from ‘trembling’; ‘anger’ and some other emotions from physical ‘agitation’.
94:Interchange between subjective and objective or personal and impersonal. This is seen in words for sense perception, as I taste, smell vs. it tastes, smells (in some languages differentiated), or emotion, as sad of persons but also sad news, and many others. Several words for ‘safe, sure’, or ‘difficult’ were first used only of persons (‘without care, anxiety’; ‘hard to please’) and only secondarily of things. The old form of fear denoted the objective ‘danger’, hence the emotion which it excited.
149:tions to another that does clearly belong there, e.g. under Emotion, ‘danger because of its relation to ‘fear’, or ‘good fortune’ which leads to ‘happiness’. Many a heading in a given chapter might equally well be put in another, e.g. ‘swift? under Time or Motion. Any infelicities of grouping will not be a seri- ous drawback to use, for an alphabetical index according to the English words will be a necessary complement.
2281:2.21 MAN? (vs. Woman) , Goth. wair (guma, manna) Lith.  vyras Gr Fes ON karl, karlmadr Lett. _virs Lat. vir Dan. mand ChSl. mazt It. uomo Sw. man SCr.  Covjek, muSkarac Fr, homme OE wer (wépnedman, Boh. muz Sp. hombre, varén ceorl, man) Pol. maz, meszczyzna Rum. bdrbat, om ME — man (were) Russ. mu3éina ifs fer NE man Skt. —_nar-, nara-, vira-, Nir. fear Du. man pumaiis- W. guwr OHG man, gomman (wer, Ay. nar-, virad~, OPers. Br. gwaz karl) martiya- MHG man NHG mann
2285:at. vir, Umbr. uiro (ace. pl.): Ir. Jer, Nir. fear, W. gur, Nie nas Ge ae with neg. for ‘no one’); Goth. wair Gat Chee OE wer, ete. (old : ) Dut now obs. except in epds.,
29058:16.53 FEAR, FRIGHT Goth. agis, faurhtei Lith. baimeé, bailé, i8gqstis rk §to5, oe st ON atti, dgn, hrezla, Lett. bailes ; NG $6805, ai tus, pavor, skelkr ChSl.  strachit, bojaznt ot. timory Dan. frygt, skrak SCr.  strah, bojazan terror iinore;_ spe Sw. fruktan, skraéck Boh. _ strach, bdzer It. paura, d OE ege, egesa, fyrhto Pol. bojazi, strach, trwoga vento ainte, effrot ME fere, eye, frizt Russ. strach, bojazn’ peur ria pavura, NE fear, fright, terror Skt.  bhaya-, bhiti-, bhi-, Sp. pieeee ’ Du. vrees, schrik trasa- oe teamd, spaimd OHG  forhta, egi, egiso Av. Owaésah-, byah-, Rum. Ug ia MHG  vorht(e), ege, eis, tarSti- I ae faitcheas, schreke Nir. age han NHG _ furcht, schrecken
```


## [2026-10-15T02:48:35.267Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 29059,29075p SYN.txt | grep -n -i -E 'tars|tras|terr|tarsti' | cut -c1-500; echo; grep -n -E 'THOU|17\\.[0-9]+ .*(THOU|YOU)' SYN.txt | head -3; grep -n -i -E 'tarsîdan|tarsidan|tarsa' incoming/ARY/ARY_latin_index_pages.txt | head -5; grep -n -E 'ترسیدن|^ *تو |هراسیدن' incoming/ARY/ARY_pages.txt | head -8"
}
```


### [2026-10-15T02:48:35.863Z] TOOL RESULT

```
2:Words for ‘fear’ and the stronger (and in part more sudden) ‘fright, terror’ are mostly based upon those for physical ac- tions expressive of fear, especially ‘trem- ble, shake’, also ‘flee’, ‘be struck’, etc. Insome cases there has been a shift from the objective ‘danger’ to the subjective fear’, as, conversely, words for fear’ are often used objectively for what inspires fear, ‘a horror, a terror, danger’. Anim- portant cognate group is common to Balto-Slavic and Indo-Iranian.
5:'. Gr 5 L AS 8 terroy? tie (latter often obj. °F attested ] Vb. del5u (fr. *Be-d¢o10;
9:Grk. tpéunos ‘a trembling’, esp. with fear, whence NG ‘terror, fright’ : rpéuw, Lat. tremere ‘tremble’, Lith. trimti ‘shake’, IE *trem- beside *tres- in Skt. iras- ‘tremble, be afraid’, Grk. rpew ‘tremble, flee’, Lat. terrére ‘terrify’, terror ‘terror’. Walde-P. 1.785. Er- nout-M. 1054.
17:Lat. terror (> It. terrore, Fr. terreur, etc., NE terror), see above under Grk. Tpopos.

30146:CHAPTER 17 MIND, THOUGHT
30175:MIND, THOUGHT.
30227:MIND, THOUGHT
5539:TRIAST s(RUSSIAN) 33 TTARSATIY {OLD PERSIAN) jel gah
5662:۴ / ترس ترسیدن
6010:تو (مخاطب مفرد) / ۲۰۵
```


## [2026-10-15T02:48:39.807Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 5535,5542p ARY_latin_index_pages.txt; sed -n 5655,5665p ARY_pages.txt; sed -n 6005,6012p ARY_pages.txt; for n in 5662 6010; do head -n $n ARY_pages.txt | grep -o '\\[pdf page [0-9]*\\]' | tail -1; done; grep -n -E 'TUVAM|TVAM|TU \\(' ARY_latin_index_pages.txt | head -3"
}
```


### [2026-10-15T02:48:40.178Z] TOOL RESULT

```
leatloal
asi yay gles! 20319 ol
‘TERROR (PORTUGUESE) J AVESTAN) gles}
DRAES — {OLD ENGLISH) pS p15: TARSHTA, T@RQSAITI
TRIAST s(RUSSIAN) 33 TTARSATIY {OLD PERSIAN) jel gah
TRISH (LITHUANIAN) gi e3 TARSITAN, TARS — -(PAHLAV)) 5.
‘TRISAS, TRISET (LATVIAN) (3) 53 TARSIN, TIRSUN —-{OSSETIC) 3!
TARRACH — (OLD IRISH) 35 544! TARS, TIRSIN (KURDISH) 52,8
انگلیسی کهن (لالا20/0 0۱2): 7083
و
فارسی (۳8۶/4۷). ۰ ترخینه, تلخینه, ترخنه (به چم "آب کشک)
اوستایی (/4:97۸): 7۸31۸ سانسکریت (54۸/577):
افغانی (پشتو) (470(۸71): ان 01 ۳۸۳۸۷ ,7۸۸67 :7۸26
تخاری ۸ (۸ (7017۸7۸): ال گوتیکد (0077470): 7:88
[pdf page 193]
۴ / ترس ترسیدن
ایسلندی کهن (/(۵ یی صا0): برتونی (88870/7): اند ای با
717
نررس کهن (۸/082 010): 78 پسگشت‌ها ۳ 5
آلمانی کهن (/(052-44 از صا): لغت‌نامه دهخدا: ۷.۷۶
أ (0 0
۹
[pdf page 204]
لگ ی
تو (مخاطب مفرد) / ۲۰۵
بادداشت,
۱ واژه‌های "تار" و "تور" و انفنگه" هم از همین واجریشه هند و اروپایی هستند.
[pdf page 193]
[pdf page 204]
3809:BYT, BIT, BYTU (RUSSIAN) 9 FUL, FIO, ESSE LATIN) 3
5170:PYCHATU (RUSSIAN) 59) PUK, PUKK ARMENIAN) gs)
5886:DU (GERMAN) JUST ‘TU, TAVA, TOM, TVAM
```


## [2026-10-15T02:48:44.907Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^tu\\b|^tu-|Pok\\. tu 1097|Pok\\. tu' AHD_watkins1985.txt | head; grep -n -o -E '.{300}\\[Pok\\. (tu|tres-?).{0,30}' AHD_watkins1985.txt | head; grep -n -i -o -E '.{200}TERROR.{100}' AHD_watkins1985.txt | head -3"
}
```


### [2026-10-15T02:48:47.054Z] TOOL RESULT

```
1096:5. Greek trias, the number three: TRIAD. 6. Greek trikha, in three parts: TRICHOTOMY. 7. Greek compound triérés, galley with three banks of oars, trireme (-érés, oar; see era-'): TRIERARCH. 8. Suffixed form “*tri-to- in Greek tritos, third: TRITIUM; TRITANOPIA. 9. Compound form *tri-pl-, “threefold” (*-pl- < combining form *-plo-; see pel-3), in Greek ¢triploos, triple: TRIPLE. 10. Compound form *tri-plek-, “threefold” (*-plek-, -fold; see plek-), in Latin triplex, triple: TRIPLEX. 11. Compound form *tri-st-i, “third person standing by” (see sta-), in Latin testis, a witness: TESTAMENT, (TESTIMONY); ATTEST, CONTEST, DETEST, OBTEST, PROTEST, TESTIFY. 12. Per- sian si, three: straR. III. Extended zero-grade form “iris, “thrice.” 1. Latin ter, thrice: TERN?; TERPOLYMER. 2. Greek tris, thrice: TRISOCTAHEDRON. 3. Suffixed form *tris-no- in Latin trini, three each: TRINE, (TRINITY). IV. Suffixed o-grade form *troy-o- in Russian troje, three: TROIKA. [Pok. trei- 1090.] trem-. To tremble. Possibly related to trep-' and tres- through a hypothetical base *ter-. Latin tremere, to shake, tremble: TREMENDOUS, TREMOR, TREMULOUS. [Pok. trem- 1092.] trep-'. To tremble. Possibly related to trem- and tres- through a hypothetical base *ter-. Latin trepidus, agi- tated, alarmed: TREPID; INTREPID. [Pok. 1. trep- 1094.] trep-2. To turn. 1. Greek trepein, to turn: -TROPOUS; APOTROPAIC, TREPONEME. 2. O-grade form *trop- in: a. suffixed form *trop-o- in Greek tropos, a turn, way, manner: TROPE, TROPO-, TROVER; CONTRIVE, (RE- TRIEVE); b. suffixed form *trop-d- in Greek tropé, a turning, change: TROPHY, TROPIC; ENTROPY. [Pok. 2. trep- 1094.] tres-. To tremble. Possibly related to trem- and trep-1 through a hypothetical base *ter-. Metathesized form *ters- in o-grade suffixed (causative) form *tors-eyo- in Latin terrére, to frighten (< “to cause to tremble”), with vowel e from terror (< *ters-os-), terror: TERRIBLE, TERROR; DETER, TERRIFIC. [Pok. tres- 1095.] treud-. To squeeze. 1. Suffixed o-grade form *troud-o- in Germanic *thrautam in Old English thréat, oppression, use of force: THREAT. 2. Variant form *trid- in Germanic “thristjan in Old Norse thrysta, to squeeze, compress: THRUST. 3. Latin tridere, to thrust, push: ABSTRUSE, EXTRUDE, INTRUDE, OBTRUDE, PROTRUDE. [Pok. tr-eu-d 1095.] trozdo-. Thrush. 1. Germanic *thrust- in Old English throstle, thrush: THROSTLE. 2. Germanic *thruskj6n- in Old English thrysce, thrush: THRUSH}. 3. Zero-grade reduced form *trzdo- in Latin turdus, thrush: STURDY. 4. Perhaps altered in Greek strouthos, sparrow, ostrich: STRUTHIOUS; (OSTRICH). [Pok. trozdos 1096.] tu-. Second person singular pronoun; you, thou. 1. Lengthened-grade form “ti (accusative “te, *tege) in Germanic *thii (accusative *theke) in Old English thi (accusative thec, thé), thou: (THEE), THOU!. 2. Suffixed extended form *éwjei-no- in Germanic *thinaz in Old English thin, thine: THINE, THY. [Pok. tu- 1097.] twei-. To agitate, shake, toss. 1. Extended form *tweid- in Germanic *thwit- in: a. Old English thwitan, to strike, whittle down: WHITTLE; b. Middle Dutch duit, a small coin (? < “piece cut or tossed off”): DorT. 2. Extended form *tweis- in Greek seiein, to shake: SEISM, SISTRUM. [Pok. 2. tuei- 1099.] twengh-. To press in on. Germanic *thwang- in: a. Old English thwong, thwang, thong, band (< “constraint”): THONG; b. by-form *twangjan in Old English twengan, to pinch: TWINGE. [Pok. twengh- 1099.] twer-', To turn, whirl. Zero-grade *tur-. I. Variant form *stur-. 1. Suffixed form *stur-mo- in Germanic *sturmaz, storm (< “whirlwind”), in Old English storm, storm: STORM. 2. Germanic *sturjan in Old English styrian, to move, agitate: STIR!. II. Suffixed form *tur-bd in Greek turbé, tumult, disorder (> Latin turba, disorder, turbé, spinning top, and turbdre, to confuse, disorder): (TROU-
1100:twerk-. To cut. Zero-grade form *twrk- in Greek sarx, flesh (< “piece of meat”): SARCASM, SARCO-, (SARCOID), (SARCOMA), (SARCOUS); ANASARCA, ECTOSARC, PERISARC, (SARCOCARP), SARCOPHAGUS, (SARCOPTIC MANGE), SYS- SARCOSIS. [Pok. tuerk- 1102.]
1096:-. To tremble. Possibly related to trem- and trep-1 through a hypothetical base *ter-. Metathesized form *ters- in o-grade suffixed (causative) form *tors-eyo- in Latin terrére, to frighten (< “to cause to tremble”), with vowel e from terror (< *ters-os-), terror: TERRIBLE, TERROR; DETER, TERRIFIC. [Pok. tres- 1095.] treud-. To squeeze. 1.
1096:tu-. Second person singular pronoun; you, thou. 1. Lengthened-grade form “ti (accusative “te, *tege) in Germanic *thii (accusative *theke) in Old English thi (accusative thec, thé), thou: (THEE), THOU!. 2. Suffixed extended form *éwjei-no- in Germanic *thinaz in Old English thin, thine: THINE, THY. [Pok. tu- 1097.] twei-. To agitate, sh
325:ench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic s
1096:trem- and trep-1 through a hypothetical base *ter-. Metathesized form *ters- in o-grade suffixed (causative) form *tors-eyo- in Latin terrére, to frighten (< “to cause to tremble”), with vowel e from terror (< *ters-os-), terror: TERRIBLE, TERROR; DETER, TERRIFIC. [Pok. tres- 1095.] treud-. To squeeze. 1.
2361:OMY _ trei- TERRIFIC tres- THROSTLE trozdo- TOUPEE tap- -TRICHOUS _ thrix TERRIGENOUS §ters- THROUGH tere-2 Tow! deuk- TRICHURIASIS ors- TERRITORY ters- THROW tere-1 Tow? taw- TRICLINIUM klei-, trei- TERROR tres- THRUM?2 ter- TOWN dhino- TRICORN ker-1 TERTIAN trei- THRUSH! trozdo- TOXIC tekw- TRICROTIC  k
```


## [2026-10-15T02:48:57.934Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 513 -l 513 -r 400 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf pg513hi; python3 -c \"\nfrom PIL import Image\nim=Image.open('pg513hi.png'); W,H=im.size; s=400/200\nim.crop((int(360*s),int(590*s),int(560*s),int(660*s))).save('crop513a.png')\nim.crop((int(360*s),int(1430*s),int(560*s),int(1520*s))).save('crop513b.png')\n\"; echo ok"
}
```


### [2026-10-15T02:49:00.177Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'
ok
```


## [2026-10-15T02:49:03.607Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; s=1.0; magick pg513hi.png -crop 400x140+720+1180 crop513a.png 2>/dev/null || convert pg513hi.png -crop 400x140+720+1180 crop513a.png; magick pg513hi.png -crop 400x180+720+2860 crop513b.png 2>/dev/null || convert pg513hi.png -crop 400x180+720+2860 crop513b.png; ls crop513*"
}
```


### [2026-10-15T02:49:04.635Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   898 sfmqrb 14 Oct 22:49  crop513a.png
.rw-r--r--  1.5k sfmqrb 14 Oct 22:49  crop513b.png
```


## [2026-10-15T02:49:09.718Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; magick pg513hi.png -crop 520x120+800+1360 crop513a.png; magick pg513hi.png -crop 520x150+800+3200 crop513b.png"
}
```


## [2026-10-15T02:49:10.763Z] TOOL CALL #55: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/crop513a.png"
}
```


## [2026-10-15T02:49:11.394Z] TOOL CALL #56: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/crop513b.png"
}
```


### [2026-10-15T02:49:12.471Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-15T02:49:12.511Z] TOOL RESULT

```

```


### [2026-10-15T02:49:12.519Z] TOOL RESULT

```

```


## [2026-10-15T02:49:18.606Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==510' KLN_1966.txt | grep -o -E '\\b9[0-9]{2} *[i|] *9[0-9]{2}\\b|\\b9[4-9][0-9]\\b' | head; awk 'BEGIN{RS=\"\\f\"} NR==487' KLN_1966.txt | grep -o -E '^[a-z]+,' | head -3; grep -n -o -E '\\b(949|950) *[i|]? *(950|951)\\b' KLN_1966.txt | head -3; mkdir -p ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg513.png ocr/BOOK/513.png"
}
```


### [2026-10-15T02:49:19.274Z] TOOL RESULT

```
948
949
logometric,
logotype,
loir,
```


## [2026-10-15T02:49:22.594Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; n=38707; leaf=$(head -n $n KLN_1966.txt | tr -cd '\\f' | wc -c); echo $leaf; awk -v n=$leaf 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | grep -o -E '\\b1[5-6][0-9]{2}\\b' | head"
}
```


### [2026-10-15T02:49:23.007Z] TOOL RESULT

```
844
```


## [2026-10-15T02:49:27.909Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *(tars-|tuvam|taiy)' KNT_full.txt | head; grep -n -E 'tars- ' KNT_full.txt | head -3; grep -n -E '^ *-?taiy|tuvam ' KNT_full.txt | head -5; grep -n -E '^ *(tū|tava-|tuvəm|ϑwąm)' BRT.txt | head"
}
```


### [2026-10-15T02:49:28.320Z] TOOL RESULT

```
2899:tarsatiy with Iran. tars- because of NPers. (0708, $ 
7225:-frastam, tuvam but ace. ийт, akariya but 
10053:(a) Personal pronouns: adam ‘T, tuvam ‘thou’. 
10130:I. Nom. sg. tuvam is the same as Skt. tuvdm, 
12432:I. The personal pronouns adam ‘Y and tuvam 
14080:tion which introduces it: DB 4.37 tuvam Ка xSaya-
```


## [2026-10-15T02:49:32.337Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2895,2902p KNT_full.txt; sed -n 10128,10140p KNT_full.txt; grep -n -E 'tars- .*(fear|be afraid)|^tars-' KNT_full.txt | head -3; grep -n -E \"^ *[•.]? *j?\\.? *tū|^ *[•]? *[j.]* *tava-|^ *[•]? *[j.]* *tvąm\" BRT.txt | head; grep -n -E 'tvqm|Owqm|ϑwąm|8wqm|0wqm' BRT.txt | head -3"
}
```


### [2026-10-15T02:49:32.882Z] TOOL RESULT

```
ardastana- ‘window-frame’, Elam. har-da-i5-da- 
па. 


tarsatiy with Iran. tars- because of NPers. (0708, $ 
despite Av. drasaiti, from is-, both with IE Ж 
suffix -ske-; but Skt. trásati from "ireseti. 1 
cartanaty: the c shows that a front vowel formerly 3 
$194. Tux SEcoxp PERSONAL Pronoun. 

I. Nom. sg. tuvam is the same as Skt. tuvdm, 
from pIE *tū + -om (spreading from 1st person 
adam, etc.): tuva without -m, §52.V. 

IL. Acc. Sg. @uvam is the same as Skt. ат, 
from pIE *tué + асе. -m of nouns (cf. тат ‘me’). 

ПІ. Gen. encl. -taty is the same as Skt. gen.- 
dat. że, pIE Чот; -tay, §52.IT. 


6869:Ikät^  'rynt    masdqm..aat  mr€oH^Xvtxz.,\ jnier  I  1)    "rö  mazda  V.  2.  if.;  usw.;    — j  dim  p9r^sat  sarai^uslrS  -rahe  (statt  Akk.) ' masdi    Nile  i ;    —    wii    mraot  (Stverz-,  [ nnter  1  3)      °rJ    masdä    V.iS.i;  usw.;  — miinm    .  .  y5   gimatte    'rät    mazdai  Yt. ' '''■53;    8.  to',   — frSmraot  °rS  mazda  Y. M.  1; — jiimäi ..paoiryS  maiyänqm  apsnse^ oum    y3     "rö    mazdä    V.  2.  2;  1 ;    —    äat ioxta   *rj  masds  V.  2.  21,  40,  42;  31,  Vr. 3.  3,  Y,  10.  9;  — paiti  sS  aoxta  'rS  mazds A.4.6,  H./.  2,  7,  P.27,  FrW./o.40,  Nik. 2;  —   aite  sl  vä^ . .  "rS  mazdn  främraot zara^ultrai  Y.  7/,  14;  ig.  i,  15;  —  rätayS ..*yqm    °rv  mazdil  xaraisuiträi /ravavaca frä    tara^uitrS  gaiHäiyö  ..  Y,6§.g;  — ja'ia    dim    isat    °rS    mazdh    V.2.32;  — jaia  . .  zaois  mana  yat  °rahe  masdä  Yt. ir).%z;    &35;    —    xmaoi:ra    (sd,    auch fdSt.)   'rahe  masdä  Yt.  7.0,  usw.;  — j;As- maitie  'rahe  mazda  Y._^.  i,  22.4,  23;  — frasasti  °rah*  mazdil  Y.  S.  i;  —  staotala .  .  yat  a^a  'rahe  mazda  Vt.i}.  6;  —  /ava 'ra  mazda  yasrum  . .  vahm>mca  Vr.  21.  a; P._3P;    —    ramasf    ti  'ra    mazda    "hrlsHt pars  anyäis  ääman  Ny,  /.  i ;  Y.6S.X2,  Yt. 7.1,  V.ig.25;    —  fumahl  iyiJmS    *'ra.- wiazdä'"'*    Y.  5>y.  3;    —   yat   zaota    'rsm ma-uiam  yazäiti  N.  70;  Y,  25. 4,  57.  a,  V. 7q.  19,  Vt  6.  4,  77. 18,  Vr.  jj.  I,  i8. 1,  23. 1, G.5.S;usw,;  —  kö  mqm  staoiti  yim  'r^m mazdqm  H.7. 3;    —    'rai  mazdäi  haomq äJoAayamahi  Y.  24- 1 ;  Vr.  //.  16,12.1;  — zbayamahi    JrJnämahi     mqm    ytm     °r>m mazdqm     Yt/2.3(?);    Vyt2.^(;    —    'nm mazdqm    danyo.yas/fmca  (si)    hqm.parl- timca  H-2, 14;    —    ks  itvqm  yim  °rgm mazdqm  . .  mazista  ibaisatiha  tbaisayeiti  V. /iS'.6i*;zitY.(?.8PiiZ.; — mä  zl  ahmt  nmane . .  fnm  i-aocata   mqm  yim  'nm  mazdqm yaia  ..  P.  17;    —    i^a    dim  ^ara-cinasti yim    'nm    mazdqm     .  .    damabyS    Y.  ig. la.        a)  in  Verbindung  mit  andern  Gott- heiten: 'rahe  mazda  . .  varahSus  mananks ..asahe  vahisiahe  .  ,  xia^rahe  vairyehe.. tpmtayB    ärmatöil .  .  haurvatä  amir^täta  , . .  ^ui  urune  gSUs    lalne  .  .  ä^re  °rahe  1 mazda  Y.  70.  z;  /.  if,,  57.24,  Vr.  i/.  16,  j ^-  5-  5«  V.  7p,  1 1 ;  —  -räica  mazdäi  srao- , s.Wa    a^.li    rasnvalta    razilläi   mt^räica Vr.  //.  6;  Y.  4. 2,  Vyt  i4;  —  «Äu  me  'ra , mazda   uäa    üpS  urvar&sca  usia  daine  .  . , VlÄ  29;  23.  a.)  bes.  häufig  mit  den
10599:-yekya  (ISf,)  frasrnUi  "..  die  zweite  Hälfte  1  mazää  yasamaiäe  dar»%rai  .  .  'tum  ('Ge- mit  lauterem  Vortrag"  Y.ß.  i4'>.  dächtniskraft')    ..  marf^rJt  ..  hitvqm  ..
12935:•  j.,  g.  daradi^i  InC  i)  'in  seinen  Besitz zu  bringen,  sich  zu  erwerben':  kads  .  . uxfanS  (sd.)  asnqm  anhJuf  d'  frö  alahyä /rannt!  ".  .  auf  das  die  Welt  das  ^a sich  erwerbe"  Y.  46'.3.  3)  'au&ufassen, zu  vernehmen':  uH  ahurahe  masda  yata- maide  d'  mq%rahe  spmtahe  . .  xratüm  .  , marä^rai  .  .  Aitvqm  .  .  fravakai  "wir  ver- ehren die  Ohren  (das  Gehör)  des  AAM., dass  er  das  heilige  Wort  vernehme, . .  die Gedächtniskraft  . .,  dass  er  (es)  behalte, die  Zunge  ,  .,  dass  er  (es)  verkünde"  Yt
```


## [2026-10-15T02:49:41.568Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1610,1626p HUB.txt; grep -n -E 'sahm|sahim' HUB.txt HRN.txt | head -5; grep -n -E '^ *[0-9]+\\. *(tu|tü|tō)\\b' HRN.txt | head -3; grep -n -E '^ *(tô|tū|tu) ' HUB.txt | head"
}
```


## [2026-10-15T02:49:43.750Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *[0-9]+\\. +t[uüō] '|^ *[0-9]+\\. +tu |'du'|„du“\" HRN.txt | head -5; grep -n -E \"\\btö\\b|\\btü\\b|'du'\" HUB.txt | head -5; grep -n -E '^ *tō |^ *tu \\[' PHD_mackenzie.txt NYB_vol2_glossary.txt | head -5"
}
```


### [2026-10-15T02:49:44.214Z] TOOL RESULT

```
3740:ap. iuvam 'du'; aw. tum, tväm, tu, tava; päz. tö {tu);
3741:ai. tvdm, tdva; arm. du 'du' (H. No. 85).
5007:'du' aus alterem td = pj«z. td (ths) Min. Gl. 128 = zd. taoa.
```


### [2026-10-15T02:49:44.255Z] TOOL RESULT

```
tar *ein Vogel' (avis parva, parum quiescens et canora',
Vullers) =^ lat. sturnus, d. Staar wahrscheinlich zu
machen. Der 'Staar heisst sonst im Np. sar.
384. Vgl. Fr. Muller, WZKM. 6, 186. Zd. teresaiti =
ap. trsatiy = idg. trssk^hefi^) (inchoat.) wie zd. pere-
saiti -= ap. prsatiy = idg. prk^-sk^he-ti. Daneben zd.
dr&fihayeiti — skr. trasayati und zd. tarsta- aus
Hrsta- = Hrsta- (skr. trasta- fiir ^trsfa-), Im Neu-
persischen trat tarsad er ftirchtet* fiir *tirsad = ap.
trsatiy^) ein. Dazu aus dem Afghanischen nach Geiger:
tarhsdql *sich fiirchten, fliehen* („alte Umstellung aus
d^rah-'^, wofiir ich aber drah- oder darh erwarten wiirde.
*) Sal. Shuk. p. 12 abersetzen: 'Rebhuhn*.
*) Vgl. Brugmann, Grundriss II, p. 1031.
'J Vgl. bal. turaag^ tniaag *8ich ffirohten* mit ur aus r-Vokal
wie in tunnag Murstig* aus *trSna'Jca,— 48 —
vgl. drS *drei*), tastedql 'fliehen' (denom. zu zd. tarsti-)
HRN.txt:6091:phlv. sämän, bezw. sahmän (z. B. AV. 'boundary-
HRN.txt:6092:mark'), arm. LW. sahman o()ocj oQ^o/ndc^ -nQoacayua (de
HUB.txt:2536:693. Ist phi. sdmdn = arm. sahman, so ist als altere
HUB.txt:9003:Ob np. paz. phi. sdmdn 'Grenze* = arm. sahman hierher
```


## [2026-10-15T02:49:47.462Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3736,3741p HRN.txt; n=3740; head -n $n HRN.txt | tr -cd '\\f' | wc -c; sed -n 5003,5008p HUB.txt; grep -n -E '^tō |^tō\\b|^ *tō \\[' PHD_mackenzie.txt | head -3; grep -n -E '^tō? *\\[tw|^tō \\[' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-15T02:49:47.850Z] TOOL RESULT

```
'Zettel, Aufzug (am Webstuhl)'.
aw. [/^tan-; phly, tatak, vd. 7 (36) (für aw. täfdaena-):
ai. |/"^aw-, tanoti, 'dehnen, spannen'.
400. tHj tu, tö (FirdüsT)^) 'du, vergl. -et 'dein', -tan 'euer'.
ap. iuvam 'du'; aw. tum, tväm, tu, tava; päz. tö {tu);
ai. tvdm, tdva; arm. du 'du' (H. No. 85).
110
dstat; uftadan *fallen' = Oftadan, phi. oftdtan, Opastan ; ustdm
= 05^aw 'treu\ vgl. skr. avasthita- 'standhaft' (oben p. 20);
umH = umm^j DmBd 'Hpffnung* = paz. GmSd Shk. 261.
Auslautendes 6 aus av ist zu u geworden in: tu, iU
'du' aus alterem td = pj«z. td (ths) Min. Gl. 128 = zd. taoa.
Sonst ist auch -av zu -au geworden, s. Kap. 9.
```


## [2026-10-15T02:49:51.903Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '(^| )tō \\[' PHD_mackenzie.txt | head -3; grep -n -E '^tō|^to \\[|^tū \\[' NYB_vol2_glossary.txt | head -3; grep -n -E '^ *t[oō] +\\[' PHD.txt | head -3"
}
```


### [2026-10-15T02:49:52.275Z] TOOL RESULT

```
3784:to [LK; tw 5113], with -e: tē-c [LK-c], toy-ic [LK-yc], pers. pron. 2nd p. sg., cas. rect. and eas. obl., thou, thee, thy: l. subj. passim; emphasizing the subj. 2nd p. sg. inherent in the vb.: tē xtēš daneh 41"; nē... to frac yazé, han... é yazét it is not thou that shalt perform my sacrifice 53°; with an imp.: tē pattā- ken giyāk 398; to mà Sav 2019; in nominal sentences together with the copula: tō,- Jāmāsp, danak ... hah 21?3; tō kēhē...? 732. 155-5; but the copula may be missing: tē ham yātūk 22%; hac har dam u dahišn to pātiyāvandtar 331-12; tē peroz u veh patröc 279; to Kai-Xosroi ...? 9917; hé may also be missing in the pret. pass. having tē as its subj.: tē x"atà4 i
```


## [2026-10-15T02:49:55.664Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '\\bthou\\b|you \\(sg' PHD_mackenzie.txt | head -3; sed -n 4471p PHD_mackenzie.txt; sed -n 4941,4945p PHD_mackenzie.txt"
}
```


### [2026-10-15T02:49:56.074Z] TOOL RESULT

```
5003: to [LK < A l-k I M tw, N tu] thou, thee.
7762:   (priest) herbed.                       thou to.
sahm [shm I = M, N ......] terror.
tars [tls 1 M trs, N --] fear, respect.
tarsag [tls)k l 1 M trs)g, N tarsal Christian.
tarsAgah [tls<»k)s] respectful, reverent.
 --ih: respect, reverence.                             .
tarsidan, tars- [tls-ytn' I (M tyrs)dn), N -..] fear, be afraid.
```


## [2026-10-15T02:50:09.728Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==487' KLN_1966.txt >/dev/null; grep -n -i 'tarah\\|taraha' AFM.txt | head -2; grep -n -E \"^ *1446\\.\" LKT.txt | head -2; grep -n -i -E 'tremble' SKT.txt | head -3"
}
```


### [2026-10-15T02:50:10.223Z] TOOL RESULT

```
3323:1446.  Ar.  matralt: 'Ort,  wohin  etwas  geworfen  oder  gelegt wird ;  Kissen' ;  hieraus  it.  materasso, materassa  'Matratze',  denn  diese  war ursprünglich  ein  Netz,  das  man  auswarf, wo  man  sich  hinlegen  wollte;  prov.  al- mairac,  frz.  materas,  matelas,  kat.  alma- trach,  matalds,  sp.  py.  almadraque  'Ma- tratze', pg.  dem.  ahnadraguexa,  verkürzt almntrixa  'Pferdedecke',  pg.  madrago 'Faulenzer':  engl,  maitress,  ndl.  mafras, disch.  Matratze,  russ.  matrac,  poln.  ma- terac,  öech.  matrace.   [Dozy  Oost  63  ff.
6287:fiaaoon.  (F.-L.)  M.  E./(i«r<»».-O.F. faufOM, /auUon.^VMt  V.. /tUcon^m,  ace.  of /a/rt),  a  falcon,  so  named  from  its  hooked claws.  — L./a/r-,  item  otjaix,  a  sickle. Faldatobl ;  sec  Fold. Fall,  to  drop  down.  (E.)  M,  Kfaltm. A-S./ia/Zan.'^Du.  vaJien,  lcz\.faiia,  Dan. /aid*  iSotfaiit),  S^cd. /aUa,  G./a/ZeH.  L. /eU/erf,  to  deceive, /a//j',  to  err ;  Gk.  ctpaX- Ktof,  to  cause  to  fall,  trip  np  ;  Ski.  sj>^a/, to  tremble.  (^SPAK.)  fl^  Grimiii's  law does  not  apply,  because  an  initial  /  is  lost in  Teut.  and  Latin.  Der,  b€-Jalt,  fiom  A.S. bt'/taJian,  to  fall  out,  happen.
14408:Poplar,  a  tree.  (F.-L.)  O.  F.  popHcr\ F.  ptupUer.  Formed  with  sufBx  'ier  ( =  L. -arimS  from  O.  F.  pefU*.  later  peupU,  a poplar.  — L.  po^tlum,  ace.  o(  pepu/uj,  a poplar.  Named  from  its  trembling  leaves ; populm  —  palpuius*  ;  cf.  palpUan,  10 tremble ;  Ke  Falpit«te.
17133:Shiver  (i),  to  tremble.  (.Scand.)  For- merly shever,  in  liarct  (^580);  M.  E. tMitUftn,  fktuertn  {chivtrtn^  eHrvertn), where  th  stands  for  cailicr  k,  so  thnt  the orijg.  form  was  kivtrtm*^  which  1  sapposc
```


## [2026-10-15T02:50:11.837Z] AGENT

Now I'll write the JSON.


## [2026-10-15T02:53:19.093Z] TOOL CALL #67: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-513.py",
 "content": "import json\n\nW = \"https://en.wiktionary.org/wiki/\"\nPOK_TRES = {\"ref\": \"POK:1095\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.1095 (POK_full.txt line ~87412, 'Root / lemma: tres- ters- (*teres-) Meaning: to tremble'): 'Old Indie trasati trembles ... Avestan taršta- (*tṛsta- timorous), tərəsaiti, ap. tarsatiy fürchtet ... Latin terreo, -ēre in Schrecken versetzen ... terror'. Exactly Nourai's root, gloss and Avestan/OP/Latin branches.\"}\nWLD_TRES = {\"src\": \"WLD\", \"where\": \"Bd. I p.760 (WLD_Bd1_pages.txt line 71998)\", \"stance\": \"supports\", \"note\": \"'tres-, ters- (*teres-) „zittern“. Ai. trasati „zittert“ ... av. tarsta- (ar. *tṛsta „furchtsam“), tərəsaiti, ap. tarsatiy „fürchtet“ ... Lat. terreo, -ēre „in Schrecken versetzen“, terror „Schrecken“'.\"}\nAHD_TRES = {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. tres- (AHD_watkins1985.txt line 1096)\", \"stance\": \"supports\", \"note\": \"'tres-. To tremble. Possibly related to trem- and trep-1 through a hypothetical base *ter-. Metathesized form *ters- in o-grade suffixed (causative) form *tors-eyo- in Latin terrēre, to frighten ... terror: TERRIBLE, TERROR; DETER, TERRIFIC. [Pok. tres- 1095.]'\"}\nCHEUNG_TRES = {\"src\": \"CHEUNG\", \"where\": \"pp.393-394 s.v. *θrah (*trs) (CHEUNG.txt line ~25568)\", \"stance\": \"supports\", \"note\": \"'*θrah (*trs) to shake, tremble; to fear; to flee' — YAv. θrånh- (taras-), OP t(a)rsatiy, MP tars-, Pth. tyrs-, 'hr's- (caus.); 'NP tarsīdan/tars- to fear, NP sahistan/sah- (< OP *çah- < Ir. *θrah-), hirāsīdan/hirās- to fear, dread (< Pth.), NP sah(i)m terror, dread'; 'PIE *tres- ... Pok.: 1095'.\"}\n\nentries = []\n\n# ---------------- entry 0: Tres ----------------\ne0_nodes = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"tras 1; taršta, thrâsa\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"PIE *tres- gives Proto-Iranian *θrah- / zero grade *tṛs-; Young Avestan has the inchoative present tərəsaiti (fra-tərəsaiti 'becomes afraid', Yt 10.97) and the past participle taršta- 'frightened, terrified' (< *tṛs-ta-, with s > š after r), plus the abstract taršti- 'fear' and the causative θrånhaiiete 'scares'. So taršta is a real Avestan word with the right meaning. 'tras' is the root (Skt. tras-) rather than an Avestan word, and 'thrâsa' is the lengthened-grade Old Iranian *θrāsa- that underlies Parthian (a)hrās and NP harās (< *fra-θrāsa-), not an attested Avestan form; Nourai's box thus mixes attested Avestan with root forms.\",\n  \"derivation_fa\": \"ریشهٔ هندواروپایی آغازین *tres- «لرزیدن» در ایرانی باستان به صورت *θrah- و پایهٔ ضعیف *tṛs- درآمده است. در اوستای نو فعل آغازی tərəsaiti «می‌ترسد» و صفت مفعولی taršta- «ترسیده، هراسان» (از *tṛs-ta- با تبدیل s به š پس از r) و اسم taršti- «ترس» گواهی شده است؛ پس taršta درست است. اما «tras» خودِ ریشه است (سنسکریت tras-) و «thrâsa» صورت بالاندهٔ ایرانی باستان *θrāsa- است که در «هراس» (از *fra-θrāsa-) دیده می‌شود، نه واژه‌ای گواهی‌شده در اوستا. ادعای نورایی در اصل درست ولی در جزئیات با احتیاط پذیرفتنی است (بارتولومه، چونگ، پوکورنی).\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/tres-\", W + \"ترسیدن\"],\n  \"ref_check\": [\n   {\"ref\": \"KLN:1592\", \"status\": \"supports\", \"note\": \"Klein 1966 s.v. terrible (KLN_1966.txt line 38707, leaf 844; leaf 853 carries 'p.1610/1611', so leaf 844 = c. p.1592): 'L. terrere, to frighten, which stands for *terseyō and is cogn. with OI. trasati, trembles, Avestic tarshta, feared, revered, tərəsaiti, is afraid of ... fr. I.-E. base *teres-, *tres-, to tremble'.\"},\n   {\"ref\": \"HRN:86\", \"status\": \"supports\", \"note\": \"Horn p.86 no. 384 (HRN.txt leaf 107): 'tersīden sich fürchten, tersā furchtsam; Christ. ap. √tras-, tarsatiy er fürchtet; aw. √tras-, teresenti; phlv. tarsitan; ai. √tras-, trāsati'.\"},\n   {\"ref\": \"NYB:172\", \"status\": \"supports\", \"note\": \"Nyberg Manual II p.~172 (NYB_vol2_glossary.txt line 3374, leaf 188) s.v. sahm: 'terror ... NP sah(i)m ... from OP *čahma, nom. of *čahman-, SW form of *θrah-man-, from Av. (802 sqq.) θrah-, v. tarsītan' — the page cited is the sahm entry, which names Av. θrah- (Bartholomae col. 802) as the root.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.v. taršta-, taršti- (BRT.txt lines 12117-12120)\", \"stance\": \"supports\", \"note\": \"'taršta- Adj., PPfP.: s. θrah-'; 'taršti- f. Schrecken, Furcht' — Bartholomae files both under the root θrah- (col. 802).\"},\n   CHEUNG_TRES,\n   {\"src\": \"HUB\", \"where\": \"p.47-48 on Horn 384 (HUB.txt line 1614)\", \"stance\": \"supports\", \"note\": \"'Zd. teresaiti = ap. tṛsatiy = idg. tṛs-skheti (inchoat.) ... zd. tarsta- aus *tṛsta-'.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"tarsîdan; tarsâ; harâsîdan\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"tarsīdan: NP present stem tars- < MP tars- (Book Pahlavi tls-, Manichaean tyrs-) < OP tṛsatiy / Av. tərəsaiti < Proto-Iranian inchoative *tṛs-sa-ti- (*tṛš-ća-) from PIE *tres-; the infinitive tarsīdan is a secondary -īdan formation on the present stem. tarsā 'fearing; Christian' < MP tarsāg 'Christian', literally '(God-)fearer' (tars- + -āg), used by Sasanian Persians for Christians (Sogdian trsʾq likewise); Sa'di's verse 'gabr o tarsā' (Zoroastrian and Christian) is quoted by Mo'in. harāsīdan / harās is the Parthian-origin doublet: Pth. ahrās (ʾhrʾs) < Old Iranian *fra-θrāsa- (preverb fra- + lengthened grade of *θras-), with initial fr- > h(a)r- as in other NW loans; Cheung and Abolqasemi both derive it so.\",\n  \"derivation_fa\": \"«ترسیدن» از ستاک مضارع «ترس» ساخته شده که از فارسی میانهٔ tars- و پارسی باستان tṛsatiy / اوستایی tərəsaiti (ستاک آغازی *tṛs-sa-) از ریشهٔ هندواروپایی *tres- است. «ترسا» از فارسی میانهٔ tarsāg «مسیحی»، به معنای لفظی «ترسندهٔ (از خدا)» است و ساسانیان مسیحیان را چنین می‌خواندند (بیت سعدی «گبر و ترسا»). «هراسیدن/هراس» دوگانهٔ پارتیِ همین ریشه است: پارتی ahrās از ایرانی باستان *fra-θrāsa- (پیشوند fra- + صورت بالاندهٔ θrās-)؛ fr آغازی در وام‌واژه‌های شمال‌غربی به hr بدل شده است. ادعای نورایی درست است (هرن، نیبرگ، مکنزی، چونگ، ابوالقاسمی، برهان قاطع).\",\n  \"sources\": [W + \"ترسیدن\", W + \"ترسا\", W + \"هراس\"],\n  \"ref_check\": [\n   {\"ref\": \"BQT:484\", \"status\": \"supports\", \"note\": \"Borhan vol.1 p.~484 (BQT_v1_pages.txt leaf 710): 'ترس ... خوف وبیم'; 'ترسا بر وزن تنها، ترسنده و بیم برنده و عبادت کننده را گویند و نصرانی و آتش‌پرست را نیز گفته‌اند'; Mo'in's notes give پهلوی tarsāk and quote Sa'di 'ای کریمی که از خزانهٔ غیب / گبر و ترسا وظیفه خور داری' (Golestān) — the same verse as on Nourai's chart.\"},\n   {\"ref\": \"FFD:81\", \"status\": \"supports\", \"note\": \"Abolqasemi, FFD (FFD_pages.txt leaf 85 = p.~81) s.v. هراسیدن: 'هراس < پهلوی اشکانی ... < ایرانی باستان *fra-θrāsa- ... صورت بالاندهٔ ریشهٔ θras به معنی «ترسیدن» ... «ترسیدن» هم از θras آمده است'; s.v. ترسیدن (leaf 50): 'ترس < فارسی میانه tars < ایرانی باستان *tṛsa- ... «هراسیدن» هم از θras آمده است'.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 384, p.86\", \"stance\": \"supports\", \"note\": \"'tersīden sich fürchten, tersā furchtsam; Christ' < ap. tarsatiy, aw. tərəsaiti, phlv. tarsitan.\"},\n   {\"src\": \"PHD\", \"where\": \"s.v. tars, tarsāg, tarsīdan (PHD_mackenzie.txt lines 4941-4945)\", \"stance\": \"supports\", \"note\": \"'tars [tls] fear, respect'; 'tarsāg [tlsʾk] Christian'; 'tarsīdan, tars- fear, be afraid'.\"},\n   {\"src\": \"NYB\", \"where\": \"s.v. tars, tarsītan (NYB_vol2_glossary.txt lines 3751-3754)\", \"stance\": \"supports\", \"note\": \"'tars [tls] fear, fright'; 'tarsītan [tlsytn'] ... to fear, to feel fear for'.\"},\n   CHEUNG_TRES,\n   {\"src\": \"BQT\", \"where\": \"vol.4 s.v. هراس (BQT_v4_pages.txt line 16282)\", \"stance\": \"partial\", \"note\": \"'هراس ... بمعنی ترس و بیم باشد' — meaning confirmed, no etymological footnote on the derivation.\"},\n   {\"src\": \"ARY\", \"where\": \"pdf p.193 s.v. ترس، ترسیدن\", \"stance\": \"supports\", \"note\": \"Latin index lines: 'TARSHTA, TƏRƏSAITI (AVESTAN)', 'TARSATIY (OLD PERSIAN)', 'TARSITAN, TARS (PAHLAVI)', 'TERROR', 'TRISH (LITHUANIAN)' — Aryanpur files tarsīdan under PIE *tres-.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Old Persian\", \"words\": \"thrah; thrah-man, thras-man, čah-man, čath-man\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"These are not attested Old Persian words but the reconstruction chain behind NP sahm: Old Iranian *θrah-man- / *θras-man- 'fear' (root *θrah- < PIE *tres-, with -man- action-noun suffix; Wiktionary *θráhma < PIE *trés-mn̥) gives, by the south-western change Ir. *θr > OP ç, an Old Persian *çahman- (Nourai's čah-man; 'čath-man' is an intermediate spelling of the same). Nyberg, Mo'in (Borhan p.1197) and Cheung all reconstruct exactly this; the gloss should be 'fear, terror' (a noun), not 'afraid', and the label 'Old Persian' should be read as 'reconstructed (Old) Persian'.\",\n  \"derivation_fa\": \"این صورت‌ها در کتیبه‌های پارسی باستان گواهی نشده‌اند و بازسازی‌اند: ایرانی باستان *θrah-man- / *θras-man- «ترس» از ریشهٔ *θrah- (هندواروپایی *tres-) با پسوند اسم‌ساز -man- ساخته شده و چون θr ایرانی در گویش جنوب‌غربی (پارسی باستان) به ç بدل می‌شود، صورت پارسی باستانِ فرضی *çahman- پدید آمده که به فارسی میانهٔ sahm رسیده است. نیبرگ، معین (حاشیهٔ برهان ص۱۱۹۷) و چونگ همین زنجیره را آورده‌اند؛ پس ادعای نورایی پذیرفتنی است، فقط باید آن را «بازسازی» دانست و معنا «ترس» (اسم) است نه «ترسیده».\",\n  \"sources\": [W + \"سهم\"],\n  \"ref_check\": [\n   {\"ref\": \"BQT:1197\", \"status\": \"supports\", \"note\": \"Borhan vol.2 p.1197 (BQT_v2_pages.txt leaf 661, page head '-۱۱۹۷-'), Mo'in's footnote to سهم: 'پهلوی sahm (ترس، وحشت) ... پارسی باستان *čah-man- = ایرانی باستان *θrah-man- ... θrah- ... رک: ترسیدن'; the OCR is rough but the forms thrah-, *čah-man-, *θrah-man- are legible — the source of Nourai's list.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"s.v. sahm (NYB_vol2_glossary.txt line 3374)\", \"stance\": \"supports\", \"note\": \"'from OP *čahma, nom. of *čahman-, SW form of *θrah-man-, from Av. (802 sqq.) θrah-, v. tarsītan'.\"},\n   CHEUNG_TRES,\n   {\"src\": \"KNT\", \"where\": \"§ on tarsatiy (KNT_full.txt line 2899)\", \"stance\": \"partial\", \"note\": \"Kent attests only OP 'tarsatiy' (Iran. tars-), with no *çahman-; the noun is unattested in OP.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Persian\", \"words\": \"sahm\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"NP sahm 'fear, awe, terror' (with sahmgīn, sahmnāk 'terrible') < MP sahm [shm] 'terror' < OP *çahman- < Proto-Iranian *θráhma(n)- < PIE *trés-mn̥ (root *tres- 'tremble'). It must be kept apart from the homonymous Arabic loan سهم sahm 'arrow; share', which has nothing to do with this root. sahmgīn = sahm + -gīn (MP -gēn 'full of'), sahmnāk = sahm + -nāk.\",\n  \"derivation_fa\": \"«سهم» به معنی «ترس، هیبت» (و «سهمگین»، «سهمناک») از فارسی میانهٔ sahm «هول، وحشت» و آن از پارسی باستان *çahman- و ایرانی باستان *θrahman- از ریشهٔ هندواروپایی *tres- «لرزیدن» است. این واژه را نباید با «سهم» عربی (تیر؛ بهره) یکی دانست که هم‌آوای تصادفی است. «سهمگین» با پسوند «-گین» (فارسی میانه -gēn «پُر از») و «سهمناک» با «-ناک» ساخته شده‌اند. ادعای نورایی درست است (نیبرگ، مکنزی، معین، چونگ، ویکی‌واژه).\",\n  \"sources\": [W + \"سهم\"],\n  \"ref_check\": [\n   {\"ref\": \"BQT:1197\", \"status\": \"supports\", \"note\": \"Borhan p.1197 (BQT_v2_pages.txt leaf 661): 'سهمگین ... از: سهم (ترس و بیم) + گین (پسوند اتصاف)'; 'سهمناک از: سهم (ترس و بیم) + ناک'; footnote 'پهلوی sahm (ترس، وحشت)' from *čah-man- / *θrah-man-.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"s.v. sahm (PHD_mackenzie.txt line 4471)\", \"stance\": \"supports\", \"note\": \"'sahm [shm] terror'.\"},\n   {\"src\": \"NYB\", \"where\": \"s.v. sahm (line 3374)\", \"stance\": \"supports\", \"note\": \"'sahm [shm] terror — NP sah(i)m; MPrs adj. shmyn terrible, dreadful; from OP *čahma ... *θrah-man-'.\"},\n   CHEUNG_TRES,\n   {\"src\": \"HRN\", \"where\": \"grep 'sahm'\", \"stance\": \"silent\", \"note\": \"Horn has only sahmān (boundary), no entry for sahm 'fear'.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"Latin\", \"words\": \"terěr\",\n  \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"book\", \"book_prints\": \"terěr\", \"correct_form\": \"terrēre (terreō)\",\n  \"derivation\": \"Latin terreō, terrēre 'to frighten, terrify' < Proto-Italic *torseō < PIE causative *tros-éye-ti (o-grade of *tres-, with -rs- > -rr-; the e-vowel is analogical from terror < *ters-os-). The meaning and the derivation are correct, but the book prints 'terěr', a truncated form (no such Latin word; Nourai uses ě for ē) — the extraction is faithful, the misprint is the book's; it should read terrēre.\",\n  \"derivation_fa\": \"لاتین terreō, terrēre «ترساندن، به وحشت انداختن» از ستاک سببی هندواروپایی *tros-éye- (پایهٔ o ریشهٔ *tres-) است؛ rs در لاتین به rr همگون شده و واکهٔ e از قیاس با terror آمده است. معنا و ریشه‌شناسی درست است، ولی کتاب «terěr» چاپ کرده که صورت ناقص و نادرستی است؛ این خطای چاپی کتاب است (استخراج با صفحهٔ چاپی مطابقت دارد) و صورت درست terrēre است.\",\n  \"sources\": [W + \"terreo\", W + \"Reconstruction:Proto-Indo-European/tres-\"],\n  \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. tres-: 'o-grade suffixed (causative) form *tors-eyo- in Latin terrēre, to frighten (< to cause to tremble), with vowel e from terror'.\"},\n   {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"Klein s.v. terrible: 'L. terreō, terrēre, to frighten, which stands for *terseyō'.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.760\", \"stance\": \"supports\", \"note\": \"'Lat. terreo, -ēre „in Schrecken versetzen, schrecken“, terror „Schrecken“'.\"},\n   {\"src\": \"SYN\", \"where\": \"§16.53 FEAR (SYN.txt line ~29067)\", \"stance\": \"supports\", \"note\": \"'IE *trem- beside *tres- in Skt. tras- tremble, be afraid, Grk. τρέω tremble, flee, Lat. terrēre terrify, terror terror. Walde-P. 1.785'.\"},\n   {\"src\": \"IEC\", \"where\": \"s.v. ters- (2) (IEC.txt line 18442)\", \"stance\": \"supports\", \"note\": \"'ters- (2), variant of type tres ... tremble ... Lat. terreo, ere, v. frighten, scare off'.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"French\", \"words\": \"terreur\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"French terreur (Old/Middle French terreur, terror) continues Latin terrōrem, accusative of terror 'great fear', a noun in -or from terrēre; Latin -ōrem > Old French -our/-eur by regular diphthongization of stressed ō. English terror was borrowed from it in late Middle English (terrour).\",\n  \"derivation_fa\": \"فرانسوی terreur از لاتین terrōrem (حالت مفعولی terror «ترس شدید») است که با پسوند -or از فعل terrēre ساخته شده؛ ō تکیه‌دار لاتین در فرانسوی کهن به -our/-eur بدل شده است. انگلیسی terror نیز در دورهٔ انگلیسی میانه از همین واژهٔ فرانسوی گرفته شده. ادعای نورایی درست است (کلاین، باک، ویکی‌واژه).\",\n  \"sources\": [W + \"terreur\", W + \"terror\"],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed for this box.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. terror (KLN_1966.txt line 38718)\", \"stance\": \"supports\", \"note\": \"'terror, n. — ME. terrour, fr. MF. (= F.) terreur, fr. L. terrorem, acc. of terror, great fear, alarm, fr. terrere, to frighten'.\"},\n   {\"src\": \"SYN\", \"where\": \"§16.53\", \"stance\": \"supports\", \"note\": \"'Lat. terror (> It. terrore, Fr. terreur, etc., NE terror)'.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Persian\", \"words\": \"ترور ، تروریست ، تروریسم\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian teror 'political assassination; terror', terorist, terorism are 20th-century borrowings from French terreur, terroriste, terrorisme (the latter two formed in French from Latin terror during the Revolution, 1793-94). In Persian the word shifted from 'terror, reign of terror' to 'assassination'; Wiktionary calls it a pseudo-Gallicism from terreur (or pseudo-anglicism from terror). Mo'in and Dehkhoda mark it [فر.] and note the French sense 'وحشت و خوف'.\",\n  \"derivation_fa\": \"«ترور»، «تروریست» و «تروریسم» وام‌واژه‌های سدهٔ بیستم از فرانسوی terreur, terroriste, terrorisme هستند (دو واژهٔ اخیر در انقلاب فرانسه، ۱۷۹۳–۱۷۹۴، از لاتین terror ساخته شدند). در فارسی معنا از «وحشت، حکومت وحشت» به «قتل سیاسی» تحول یافته است. معین و دهخدا آن را [فر.] دانسته‌اند. ادعای نورایی درست است؛ ادعای عامیانه‌ای که ترور را از «ترس» فارسی می‌گیرد (در برخی یادداشت‌های کاربران آبادیس) نادرست است، هرچند هر دو از یک ریشهٔ هندواروپایی‌اند.\",\n  \"sources\": [W + \"ترور\", \"https://abadis.ir/fatofa/ترور/\"],\n  \"ref_check\": [{\"ref\": \"AMD:569\", \"status\": \"partial\", \"note\": \"Amid's printed page not accessible; abadis.ir (archived) shows the Mo'in entry '(تِ رُ) [فر.] ۱- هراس، هراس افکندن ۲- کشتن ناگهانی...' and Dehkhoda 'مأخوذ از فرانسه و بمعنی قتل سیاسی'; the Amid section shown online gives only the sense 'قتل سیاسی', no origin tag.\"}],\n  \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"abadis.ir s.v. ترور\", \"stance\": \"supports\", \"note\": \"'(تِ رُ) [فر.] (اِ.) ۱ - هراس ... ۲ - کشتن ناگهانی یک فرد'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. terrorism, terrorist\", \"stance\": \"supports\", \"note\": \"'terrorism — F. terrorisme, formed fr. L. terror'; 'terrorist — F. terroriste'.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"English\", \"words\": \"terrible, terror, tremble, terrific\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"terrible (ME, from (M)F terrible < L terribilis), terror (ME terrour < MF terreur < L terrōrem) and terrific (L terrificus 'causing terror', terrēre + -ficus) all go back to Latin terrēre and PIE *tres- — confirmed. tremble does NOT: it comes from Old French trembler < Vulgar Latin *tremulāre < Latin tremulus < tremere 'to quiver', PIE *trem- (Pokorny 1092), a separate root. Watkins and Klein only call *trem-, *tres-, *trep- 'collateral bases', possibly from a hypothetical *ter-; so tremble is at best a distant root-relative, not a descendant of terrēre as drawn.\",\n  \"derivation_fa\": \"terrible (از فرانسوی و لاتین terribilis)، terror (از فرانسوی میانه terreur و لاتین terrōrem) و terrific (لاتین terrificus «هراس‌انگیز») همه از لاتین terrēre و ریشهٔ *tres- هستند و درست‌اند. اما tremble از فرانسوی کهن trembler و لاتین عامیانه *tremulāre و لاتین tremere «لرزیدن» از ریشهٔ جداگانهٔ *trem- (پوکورنی ۱۰۹۲) است، نه از terrēre؛ واتکینز و کلاین تنها احتمال می‌دهند که *trem- و *tres- هر دو گسترش‌های یک پایهٔ فرضی *ter- باشند. پس دربارهٔ tremble ادعای نورایی را پژوهش امروزی نمی‌پذیرد.\",\n  \"sources\": [W + \"terror\", W + \"tremble\", W + \"tremo\"],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed for this box.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. terrible, terrific, tremble (KLN_1966.txt lines 38707-38712, 39986)\", \"stance\": \"partial\", \"note\": \"terrible/terrific 'fr. terrere, to frighten'; but tremble: 'F. trembler, fr. VL. tremulāre ... fr. L. tremulus ... fr. tremere ... fr. I.-E. base *terem-, *trem-, to tremble'; s.v. terrible: 'Cp. the collateral I.-E. bases *trem- ... and *trep-'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. trem-, tres-\", \"stance\": \"contradicts\", \"note\": \"'trem-. To tremble. Possibly related to trep-1 and tres- through a hypothetical base *ter-. Latin tremere ...: TREMENDOUS, TREMOR, TREMULOUS. [Pok. trem- 1092.]' — tremble is not listed under tres-, which gives 'TERRIBLE, TERROR; DETER, TERRIFIC'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. terrible (SKT.txt line 19433)\", \"stance\": \"supports\", \"note\": \"'terrible. (F.-L.) F. terrible. - L. terribilis, causing terror. - L. terrēre, to frighten' (for the three terr- words).\"}\n  ]\n }\n]\nentries.append({\n \"entry\": 0, \"root\": \"Tres, Ter 2\", \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *tres- 'to tremble, be afraid' (Pokorny tres-/ters- 1095; Watkins tres-; LIV² 650)\",\n \"note\": \"Root, gloss and label are correct: Pokorny p.1095 'tres- ters- (*teres-) to tremble', Watkins/AHD tres-, Walde-Pokorny I 760, Cheung *θrah (*trs) with 'PIE *tres- ... Pok. 1095'. The chart's own note ('may be related to Trep: to tremble') matches Watkins and Klein, who call *tres-, *trem-, *trep- collateral bases possibly from a hypothetical *ter-; that is speculative. Problems lie in the leaves: the Avestan box mixes the root (tras) and a reconstructed *θrāsa with the real participle taršta; the 'Old Persian' box is a reconstruction (*θrah-man- > OP *çahman-, from Nyberg/Mo'in), not attested OP; the Latin form is misprinted in the book as 'terěr' for terrēre; and English tremble belongs to PIE *trem- (Latin tremere), not to terrēre. All Nourai references checked support him (KLN:1592 = Klein s.v. terrible; HRN:86 = Horn no.384; NYB:172 = Nyberg s.v. sahm; BQT:484, BQT:1197, FFD:81 = Abolqasemi s.v. هراسیدن). No extraction errors: the JSON matches the printed page.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *tres- «لرزیدن، ترسیدن» است (پوکورنی ص۱۰۹۵، واتکینز، والده‌ـپوکورنی، چونگ)؛ نام، برچسب و معنای ریشه در کتاب درست است. یادداشت نمودار که آن را با «Trep» مرتبط می‌داند همان گمان واتکینز و کلاین است که *tres- و *trem- و *trep- را گسترش‌های پایهٔ فرضی *ter- می‌دانند و قطعی نیست. «ترسیدن»، «ترسا»، «هراسیدن» و «سهم» (ترس) همه به‌درستی از این ریشه‌اند؛ «هراس» از راه پارتی آمده است. اشکال‌ها: خانهٔ «پارسی باستان» بازسازی است نه واژهٔ گواهی‌شده؛ کتاب صورت لاتین را به‌خطا «terěr» به جای terrēre چاپ کرده؛ و انگلیسی tremble از ریشهٔ دیگر *trem- (لاتین tremere) است. خطای استخراج دیده نشد.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/tres-\", W + \"ترسیدن\", W + \"سهم\"],\n \"ref_check\": [POK_TRES],\n \"consulted\": [WLD_TRES, AHD_TRES, CHEUNG_TRES,\n   {\"src\": \"IEC\", \"where\": \"s.v. ters- (2) (IEC.txt line 18442)\", \"stance\": \"supports\", \"note\": \"'ters- (2) (tersō), variant of type tres, q.v. tremble. WP I, 760 ... Av. tarəs-, v. id.; Per. tarsam, -īdan, v. fear; tars, s. fear ... Lat. terreo, ēre, v. frighten'.\"},\n   {\"src\": \"SYN\", \"where\": \"§16.53 FEAR, FRIGHT\", \"stance\": \"supports\", \"note\": \"'IE *trem- beside *tres- in Skt. tras- tremble, be afraid, Grk. τρέω ... Lat. terrēre terrify'; lists Av. taršti- among words for 'fear'.\"}],\n \"nodes\": e0_nodes\n})\n\n# ---------------- entry 1: T.r.h ----------------\nKLN_MATT = {\"src\": \"KLN\", \"where\": \"s.v. mattress, p.949 (KLN_1966.txt line 23157, leaf 509 carrying '948/949')\", \"stance\": \"supports\", \"note\": \"'mattress, n. — ME. materas, fr. OF. materas (F. matelas), fr. It. materasso, borrowed in Sicily fr. Arab. maṭraḥ, place where something is thrown or laid, used also in the sense of mattress (see Dozy-Engelmann ... p.151); fr. ṭaraḥa, he threw'.\"}\nLKT_MATT = {\"src\": \"LKT\", \"where\": \"no. 1446 (LKT.txt line 3323)\", \"stance\": \"supports\", \"note\": \"'Ar. maṭraḥ: Ort, wohin etwas geworfen oder gelegt wird; Kissen; hieraus it. materasso, materassa Matratze ... frz. materas, matelas ... engl. mattress'.\"}\nDEV_MATT = {\"src\": \"DEV\", \"where\": \"s.v. Matelas (DEV.txt line 1706)\", \"stance\": \"supports\", \"note\": \"'ital. materasso, ... vieux fr. materas ... De l'arabe matrah, lit, matelas ... Ce mot vient de la racine tarah, jeter'.\"}\nDOZ_MATT = {\"src\": \"DOZ\", \"where\": \"s.v. MATRAS (DOZ.txt line 1927)\", \"stance\": \"supports\", \"note\": \"'Van het Arab. matrah. Het werkwoord taraha, werpen'.\"}\ne1_nodes = [\n {\n  \"id\": 1, \"lang\": \"Arabic\", \"words\": \"tarh; matrah\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Arabic ṭaraḥa 'to throw, cast away; to propose' (root ṭ-r-ḥ) gives the verbal noun ṭarḥ 'throwing; proposing, a proposal' and the noun of place maṭraḥ (pattern maf'al) 'place where something is thrown or laid down', which in colloquial Arabic also meant 'cushion, mattress' (Algerian meṭraḥ 'mattress' still). Nourai's glosses ('plan laid out for discussion' for ṭarḥ is a modern/Persian-influenced sense) are acceptable.\",\n  \"derivation_fa\": \"فعل عربی «طَرَحَ» (ریشهٔ ط-ر-ح) به معنی «انداختن، افکندن؛ پیش نهادن» است؛ مصدر آن «طَرْح» (انداختن، پیشنهاد) و اسم مکان آن بر وزن مَفْعَل «مَطْرَح» (جای انداختن یا نهادن چیزی) است که در عربی عامیانه به معنای «تشک، بالش» هم به کار رفته است. ادعای نورایی درست است (کلاین، لوکوچ، دویک، دُزی).\",\n  \"sources\": [W + \"طرح\", W + \"مطرح\"],\n  \"ref_check\": [{\"ref\": \"KLN:949\", \"status\": \"supports\", \"note\": \"Klein 1966 p.949 s.v. mattress: 'Arab. maṭraḥ, place where something is thrown or laid ... fr. ṭaraḥa, he threw'.\"}],\n  \"consulted\": [KLN_MATT, LKT_MATT, DEV_MATT]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"tarh; matrah\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian ṭarḥ (طرح) and maṭraḥ (مطرح) are direct loans of Arabic ṭarḥ and maṭraḥ. In Persian ṭarḥ developed the senses 'design, sketch, plan, project, proposal' (from 'laying out/putting forward'), with the agent noun ṭarrāḥ 'designer' (Arabic intensive fa''āl); maṭraḥ 'place of throwing' > 'under discussion, put forward' (Mo'in sense 2 'مورد بحث'), and maṭrūḥ (passive participle) 'proposed, discussed'.\",\n  \"derivation_fa\": \"«طرح» و «مطرح» وام‌واژه‌های مستقیم از عربی «طَرْح» و «مَطْرَح» هستند. در فارسی «طرح» از «افکندن، پیش نهادن» به «نقشه، الگو، برنامه، پیشنهاد» تحول معنایی یافته و «طرّاح» (صیغهٔ مبالغهٔ فَعّال) سازندهٔ طرح است؛ «مطرح» از «جای افکندن» به «مورد بحث، پیش‌کشیده» رسیده و «مطروح» اسم مفعول آن است. ادعای نورایی درست است (معین، دهخدا، ویکی‌واژه).\",\n  \"sources\": [W + \"طرح\", W + \"مطرح\", \"https://abadis.ir/fatofa/طرح/\", \"https://abadis.ir/fatofa/مطرح/\"],\n  \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in via abadis (archived) s.v. طرح: '(طَ) [ع.] ۱ - انداختن، دور کردن، افکندن. ۲ - پیشنهاد کردن. ۳ - نقاشی کردن. ۴ - طرح اولیهٔ چیزی را برداشتن'; s.v. مطرح: '(مَ رَ) [ع.] ۱ - جای طرح کردن، جای افکندن. ج. مطارح. ۲ - مورد بحث'.\"},\n   {\"ref\": \"FVA:246\", \"status\": \"not_checked\", \"note\": \"Nahvi's Farhang-e vazheha-ye Arabi dar Farsi: no digital copy (refs_online.json).\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"abadis.ir s.v. طرح, مطرح\", \"stance\": \"supports\", \"note\": \"Both tagged [ع.] (Arabic); senses 'انداختن ... پیشنهاد کردن' and 'جای افکندن ... مورد بحث'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. mattress p.949\", \"stance\": \"supports\", \"note\": \"Gives Arabic maṭraḥ < ṭaraḥa 'he threw', the source of the Persian loans.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Italian\", \"words\": \"materasso\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Italian materasso (also materassa, older matarazzo) was borrowed, probably in Sicily during Arab rule (9th-11th c.), from Arabic maṭraḥ 'place where something is thrown; cushion, mattress', since Arab bedding was a pad thrown on the floor. Arabic ṭ and ḥ were rendered t and -ss-/-zz- in the Romance adaptations; Spanish almadraque, Catalan almatrac keep the Arabic article.\",\n  \"derivation_fa\": \"ایتالیایی materasso (و materassa، کهن‌تر matarazzo) احتمالاً در سیسیلِ دورهٔ فرمانروایی عرب (سده‌های ۹ تا ۱۱ م.) از عربی «مَطْرَح» «جای انداختن؛ بالش، تشک» گرفته شده است، چون بستر عربی تشکی بود که بر زمین می‌انداختند. اسپانیایی almadraque و کاتالانی almatrac حرف تعریف عربی «ال» را نگه داشته‌اند. ادعای نورایی درست است (کلاین، لوکوچ، دویک، ویکی‌واژه).\",\n  \"sources\": [W + \"materasso\", W + \"mattress\"],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed for this box.\"}],\n  \"consulted\": [KLN_MATT, LKT_MATT, DEV_MATT, DOZ_MATT]\n },\n {\n  \"id\": 4, \"lang\": \"French\", \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Empty pass-through box for French: Old French materas (12th-13th c., later matelas by dissimilation r...r > l...r? rather r > l), from Italian materasso; English took materas from Old French.\",\n  \"derivation_fa\": \"خانهٔ خالی فرانسوی: فرانسوی کهن materas (سده‌های ۱۲–۱۳ م.، بعدها matelas) از ایتالیایی materasso گرفته شده و انگلیسی آن را از فرانسوی کهن برداشته است. ادعای نورایی درست است (کلاین، لوکوچ، دویک).\",\n  \"sources\": [W + \"mattress\"],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed for this box.\"}],\n  \"consulted\": [\n   {\"src\": \"DEV\", \"where\": \"s.v. Matelas\", \"stance\": \"supports\", \"note\": \"'vieux fr. materas, mathelas, materal, matelat. De l'arabe matrah'.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1446\", \"stance\": \"supports\", \"note\": \"'frz. materas, matelas'.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"English\", \"words\": \"mattress\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English mattress < Middle English materas (c. 1300) < Old French materas < Italian materasso < Arabic maṭraḥ 'place where something is thrown, cushion' < ṭaraḥa 'to throw'.\",\n  \"derivation_fa\": \"انگلیسی mattress از انگلیسی میانهٔ materas (حدود ۱۳۰۰ م.)، از فرانسوی کهن materas، از ایتالیایی materasso و سرانجام از عربی «مَطْرَح» (جای انداختن، بالش) از «طَرَحَ» (انداخت) است. ادعای نورایی درست است.\",\n  \"sources\": [W + \"mattress\"],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed for this box.\"}],\n  \"consulted\": [KLN_MATT, LKT_MATT]\n }\n]\nentries.append({\n \"entry\": 1, \"root\": \"T.r.h\", \"verdict\": \"confirmed\",\n \"modern_form\": \"Arabic ṭ-r-ḥ (طرح) 'to throw, cast; to propose'\",\n \"note\": \"The Arabic root ṭ-r-ḥ 'to throw' is correct (the book's 'T.r.h' stands for emphatic ṭ and ḥ). The chain Arabic maṭraḥ > Italian materasso > Old French materas > English mattress is standard (Klein p.949, Lokotsch 1446, Devic, Dozy, Wiktionary). Nourai's FVA:247 (Nahvi) has no digital copy and could not be checked. No extraction errors.\",\n \"note_fa\": \"ریشهٔ عربی «ط‌ر‌ح» به معنی «انداختن، افکندن» درست است (نوشتار T.r.h در کتاب همان ط و ح است). «طرح» و «مطرح» فارسی وام‌واژه‌های مستقیم عربی‌اند و زنجیرهٔ «مَطْرَح» عربی ← ایتالیایی materasso ← فرانسوی کهن materas ← انگلیسی mattress را کلاین، لوکوچ، دویک و دُزی همگی تأیید می‌کنند. ادعای نورایی درست است؛ مأخذ FVA در دسترس نبود.\",\n \"sources\": [W + \"طرح\", W + \"materasso\", W + \"mattress\"],\n \"ref_check\": [{\"ref\": \"FVA:247\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e vazheha-ye Arabi dar Farsi: no digital copy found (refs_online.json).\"}],\n \"consulted\": [KLN_MATT, DEV_MATT, DOZ_MATT],\n \"nodes\": e1_nodes\n})\n\n# ---------------- entry 4: Tu ----------------\nPOK_TU = {\"ref\": \"POK:1097\", \"status\": \"supports\", \"note\": \"Pokorny IEW pp.1096-1098 (POK_full.txt line 87648 'Root / lemma: tu, tū'): 'Old Indie tu ... Avestan tū, enkl. du; Aryan *tu-am in Old Indie tuvam, tvam, Gatha-Avestan tvə̄m, jav. tūm, ap. tuvam du ... Latin tū ... Gothic þu, Old Icelandic þū, Old Saxon thū ... Old Church Slavic ty'; possessive 'Avestan tava-'.\"}\nKNT_TU = {\"src\": \"KNT\", \"where\": \"§194 (KNT_full.txt lines 10128-10140)\", \"stance\": \"supports\", \"note\": \"'Nom. sg. tuvam is the same as Skt. tuvám, from pIE *tū + -om ... Acc. sg. θuvām ... Gen. encl. -taiy is the same as Skt. gen.-dat. te'.\"}\ne4_nodes = [\n {\n  \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"taiy, tŭ, tŭm, tuvam, tava, tvâm\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All are Old Iranian forms of the 2nd-person singular pronoun from PIE *tú(h₂) / *tu-: Avestan tū (nom., also enclitic), Young Avestan tūm and Gathic tvə̄m (nom. *tu-am, -am spread from the 1st person), Old Persian tuvam (nom.), Avestan/OP tava (gen., PIE *téwe), OP enclitic -taiy (gen.-dat., = Skt. te, PIE *toi), and tvām (acc.; Gathic θβąm, Skt. tvā́m). Nourai's ŭ marks length (tū, tūm); 'tvâm' is the Sanskrit-like spelling of the accusative (Avestan θβąm).\",\n  \"derivation_fa\": \"همهٔ این‌ها صورت‌های ضمیر دوم شخص مفرد در ایرانی باستان از هندواروپایی *tú(h₂) هستند: اوستایی tū (فاعلی و پیوسته)، اوستای نو tūm و گاهانی tvə̄m، پارسی باستان tuvam (فاعلی)، tava (اضافی، از *téwe)، پیوستهٔ پارسی باستان -taiy (اضافی‌ـ‌برایی، برابر سنسکریت te) و tvām (مفعولی؛ گاهانی θβąm). نشانهٔ ŭ در کتاب کشیدگی واکه را می‌رساند. ادعای نورایی درست است (پوکورنی، کنت، هرن، معین در حاشیهٔ برهان).\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/túh₂\"],\n  \"ref_check\": [\n   POK_TU,\n   {\"ref\": \"BQT:525\", \"status\": \"supports\", \"note\": \"Borhan vol.1 p.~525 (BQT_v1_pages.txt leaf 754), Mo'in's note to تو: 'ضمیر دوم شخص مفرد ... پارسی باستان tuvam (تو)؛ اوستا tū, tvəm, tūm, ... هندی باستان tvam، ارمنی du (تو)، کردی tu، افغانی tə ...'.\"}\n  ],\n  \"consulted\": [\n   KNT_TU,\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.745 (WLD_Bd1_pages.txt line 70535)\", \"stance\": \"supports\", \"note\": \"'tu „du“ ... av. tū encl. „du“, *tu-am (nach ai. aham) in ai. tuvám, tvam, gthav. ...'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 400, p.89\", \"stance\": \"supports\", \"note\": \"'tū, tu, tō (Firdūsī) du ... ap. tuvam du; aw. tūm, tvām, tū, tava; pāz. tō; ai. tvám, táva'.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"to\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"NP to (classical tū/tō) < MP tō [LK, Manichaean tw] 'thou, thee' < Old Iranian genitive *tava (Av./OP tava): -ava- contracted to -ō- in Middle Persian, and the oblique form replaced the nominative, as with man 'I' (< gen. mana). Classical Persian had tū (with majhūl ō); modern Iranian Persian pronounces to.\",\n  \"derivation_fa\": \"«تو» در فارسی نو (کلاسیک tū / tō) از فارسی میانهٔ tō (هزوارش LK) و آن از صورت اضافی ایرانی باستان *tava (اوستایی و پارسی باستان tava) است؛ -ava- در فارسی میانه به ō منقبض شده و صورت غیرفاعلی جای فاعلی را گرفته، همان‌گونه که «من» از اضافی mana آمده است. ادعای نورایی درست است (هرن، هوبشمان، نیبرگ، مکنزی، معین).\",\n  \"sources\": [W + \"تو\"],\n  \"ref_check\": [{\"ref\": \"BQT:525\", \"status\": \"supports\", \"note\": \"Borhan vol.1 p.~525 (leaf 754): 'تو ضمیر دوم شخص مفرد (مفرد مخاطب). فردوسی هم tu و هم to استعمال کرده. پارسی باستان tuvam ...'.\"}],\n  \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"§ on auslautend -ō (HUB.txt line 5006)\", \"stance\": \"supports\", \"note\": \"'Auslautendes ō aus av ist zu u geworden in: tu, tū du aus älterem tō = pāz. tō ... = zd. tava'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 400, p.89\", \"stance\": \"supports\", \"note\": \"'tū, tu, tō (Firdūsī) du' < OP tuvam, Av. tava.\"},\n   {\"src\": \"NYB\", \"where\": \"s.v. tō (NYB_vol2_glossary.txt line 3784)\", \"stance\": \"supports\", \"note\": \"'tō [LK; tw], pers. pron. 2nd p. sg., cas. rect. and cas. obl., thou, thee, thy'.\"},\n   {\"src\": \"PHD\", \"where\": \"s.v. tō (PHD_mackenzie.txt line 5003)\", \"stance\": \"supports\", \"note\": \"'tō [LK < A l-k | M tw, N tu] thou, thee'.\"},\n   {\"src\": \"ARY\", \"where\": \"pdf p.204 (printed 205) s.v. تو\", \"stance\": \"supports\", \"note\": \"'تو (مخاطب مفرد) / ۲۰۵'; Latin index: 'TU, TAVA, TŪM, TVAM'.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"ty, tw\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Sogdian has the 2nd-singular pronoun tw (nom., Manichaean/Christian script; Buddhist tγw), oblique twʾ, and the enclitic genitive -t / ty(ʾ) 'of you' < Old Iranian *taiy (OP -taiy), i.e. the same PIE *tu-/*toi forms. Gharib's dictionary lists them exactly so.\",\n  \"derivation_fa\": \"در سغدی ضمیر دوم شخص مفرد tw (فاعلی، در خط مانوی و مسیحی؛ بودایی tγw)، صورت غیرفاعلی twʾ و پیوستهٔ اضافی -t / tyʾ «ازِ تو» آمده که از ایرانی باستان *taiy (پارسی باستان -taiy) است. قریب در فرهنگ سغدی همین صورت‌ها را آورده است. ادعای نورایی درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/túh₂\"],\n  \"ref_check\": [{\"ref\": \"SOD:383\", \"status\": \"supports\", \"note\": \"Gharib, SOD (SOD_pages.txt leaves 449-450, printed pp.383-384): '9470 -t ... < OP taiy, 2sg. encl. pron. gen. ... you'; '9738 tyʾ ... te, ti < *tai 2sg. pers. pron. gen. ... you, of you'; '9700 tw M ... to, 2sg. pers. pron. nom. ... thou'; '9701 twʾ ... 2sg. pers. pron. acc. & ob. ... you'.\"}],\n  \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"nos. 9470, 9700, 9701, 9738\", \"stance\": \"supports\", \"note\": \"As quoted in ref_check; entry numbers allow re-lookup.\"},\n   {\"src\": \"POK\", \"where\": \"p.1097\", \"stance\": \"partial\", \"note\": \"Pokorny lists Avestan/OP forms of *tu but no Sogdian.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Germanic\", \"words\": \"thŭ; thŭmaz\",\n  \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"book\", \"book_prints\": \"thŭ : you ; thŭmaz : yours\", \"correct_form\": \"*þū 'thou'; *þīnaz 'thy, thine'\",\n  \"derivation\": \"Proto-Germanic *þū 'thou' < PIE *tú(h₂) by Grimm's law (*t > þ) with lengthened ū (Nourai's ŭ marks length) — correct. The possessive, however, is *þīnaz (Gothic þeins, ON þinn, OE þīn) < *tewei-no- (Watkins *t(w)ei-no-), as AHD (Nourai's cited reference) prints; 'thŭmaz' does not exist and is the book's misprint for *thīnaz. The extraction reproduces the printed form faithfully.\",\n  \"derivation_fa\": \"ژرمنی آغازین *þū «تو» از هندواروپایی *tú(h₂) با قانون گریم (t > þ) است و درست است. اما صفت ملکی ژرمنی *þīnaz (گوتی þeins، انگلیسی کهن þīn) از *tewei-no- است، چنان‌که در واتکینز (مأخذ خود نورایی) آمده؛ «thŭmaz» در هیچ منبعی نیست و خطای چاپی کتاب به جای *thīnaz است. استخراج با صفحهٔ چاپی مطابقت دارد.\",\n  \"sources\": [W + \"Reconstruction:Proto-Germanic/þū\", W + \"thou\"],\n  \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins s.v. tu- (AHD_watkins1985.txt line 1096): 'Lengthened-grade form *tū ... in Germanic *thū (accusative *theke) in Old English thū ... THOU. 2. Suffixed extended form *t(w)ei-no- in Germanic *thīnaz in Old English thīn, thine: THINE, THY. [Pok. tu- 1097.]' — supports thū, but gives *thīnaz, not 'thŭmaz'.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. thine (KLN_1966.txt line 39039)\", \"stance\": \"contradicts\", \"note\": \"'thine — ME. thin, fr. OE. þīn, orig. gen. of þū ... Goth. þeins ... All these words stand for I.-E. *t(w)ei-no-s' — no *-maz form.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.745\", \"stance\": \"supports\", \"note\": \"Lists got. þu, ahd. du under tu „du“.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"English\", \"words\": \"thou, thee, thy, thine\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"thou < OE þū (PGmc *þū); thee < OE þē, dat./acc. of þū (PGmc *þek / *þiz); thine < OE þīn, originally the genitive of þū (PGmc *þīnaz); thy is the Middle English form of thine with final -n dropped before consonants (13th c.).\",\n  \"derivation_fa\": \"انگلیسی thou از انگلیسی کهن þū (ژرمنی *þū)؛ thee از þē، حالت مفعولی و برایی þū؛ thine از þīn که در اصل حالت اضافی þū بوده (ژرمنی *þīnaz)؛ و thy صورت انگلیسی میانهٔ thine است که n پایانی آن پیش از همخوان افتاده است. ادعای نورایی درست است (کلاین، واتکینز، ویکی‌واژه).\",\n  \"sources\": [W + \"thou\", W + \"Reconstruction:Proto-Germanic/þū\"],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed for this box.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. thou, thee, thine (KLN_1966.txt lines 39107, 38901, 39039)\", \"stance\": \"supports\", \"note\": \"'thou — ME., fr. OE. þū ... fr. I.-E. *tū-'; 'thee, objective case of thou — OE. þē'; 'thine — OE. þīn, orig. gen. of þū ... In ME. the final n was dropped before a word beginning with a consonant and so arose the form thy'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. tu-\", \"stance\": \"supports\", \"note\": \"'Germanic *thū ... THEE, THOU ... Germanic *thīnaz ... THINE, THY'.\"}\n  ]\n }\n]\nentries.append({\n \"entry\": 4, \"root\": \"Tu, Tŭ\", \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *tú(h₂), *tu- 'you (sg.), thou' (Pokorny tu, tū 1097; Watkins tu-)\",\n \"note\": \"Root, gloss and label correct (Pokorny pp.1097-1098, Watkins tu-, Walde-Pokorny I 745). Iranian forms (Av. tū, tūm, OP tuvam, -taiy, tava), NP to < MP tō < *tava, and Sogdian tw/ty are confirmed by Kent, Horn, Hübschmann, Nyberg, MacKenzie, Gharib and Mo'in. The Germanic box prints 'thŭmaz : yours', a misprint in the book for *þīnaz (AHD, Nourai's own reference, has *thīnaz). No extraction errors; the JSON matches the page.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *tú(h₂) «تو (مفرد)» است (پوکورنی ص۱۰۹۷، واتکینز، والده‌ـپوکورنی) و برچسب و معنا درست است. صورت‌های اوستایی و پارسی باستان (tū، tūm، tuvam، -taiy، tava)، «تو»ی فارسی از فارسی میانهٔ tō (از *tava) و سغدی tw/ty را کنت، هرن، هوبشمان، نیبرگ، مکنزی، قریب و معین تأیید می‌کنند. تنها اشکال، «thŭmaz» در خانهٔ ژرمنی است که خطای چاپی کتاب به جای *þīnaz «مال تو» است. خطای استخراج دیده نشد.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/túh₂\", W + \"thou\"],\n \"ref_check\": [POK_TU],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.745\", \"stance\": \"supports\", \"note\": \"'tu „du“, Stämme tu-, te-, tewe-, two- ... ai. tvam, av. tū ...'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. tu-\", \"stance\": \"supports\", \"note\": \"'tu-. Second person singular pronoun; you, thou ... [Pok. tu- 1097.]'\"},\n   {\"src\": \"IEC\", \"where\": \"s.v. tu, tū (IEC.txt line 19212)\", \"stance\": \"supports\", \"note\": \"'tu, tū thou ... Per. tu, tū, id. ... Lat. tū; Go. þu, OE þū ... Oblique forms in Skt. tvam, Av. tūm & OPer. tuvam'.\"},\n   KNT_TU],\n \"nodes\": e4_nodes\n})\n\nout = {\"pdf_page\": 513, \"book_page\": 483, \"verified_by\": \"claude-opus-5\", \"verified_on\": \"2026-10-14\", \"entries\": entries}\nwith open(\"/home/sfmqrb/git/rishe-private/data/verification/page-513.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\n"
}
```


### [2026-10-15T02:53:19.121Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-513.py (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:53:26.110Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-513.py; python3 - \"$S\" <<'EOF'\nimport sys\np=sys.argv[1]; s=open(p).read()\ns=s.replace(\"Old French materas (12th-13th c., later matelas by dissimilation r...r > l...r? rather r > l), from Italian materasso; English took materas from Old French.\",\"Old French materas (13th c.; modern matelas, with r > l by dissimilation of the two r's in *materas > matelas), from Italian materasso; English took materas from Old French.\")\nopen(p,'w').write(s)\nEOF\nf=$(python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/تو\" --note \"page 513: Persian to\" | tail -1); grep -E 'Middle Persian|From' $f | head -5 | cut -c1-300; python3 $S && python3 -m json.tool data/verification/page-513.json >/dev/null && echo valid; python3 tools/verify_check.py 513"
}
```


### [2026-10-15T02:53:27.074Z] TOOL RESULT

```
 From Wiktionary, the free dictionary
 From Middle Persian 𐭫𐭪 ( LK /⁠tō⁠/ , “ you, thou ” ) , from Old Persian (compare 𐎬𐎺𐎶 ( tuvam ) ), from Proto-Iranian *tuHám (compare Northern Kurdish tu , Pashto ته ( tə ) , Avestan 𐬙𐬏𐬨 ( tūm ) ), from Proto-Indo-Iranian *tuHám , from Proto-Indo-European *túh₂ .
 Persian terms inherited from Middle Persian 
 Persian terms derived from Middle Persian 
 Middle Persian terms with non-redundant manual transliterations 
valid
nodes verified: 18/18
node verdicts: {'plausible': 2, 'confirmed': 13, 'transcription_suspect': 2, 'disputed': 1}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 15, 'not_checked': 7, 'partial': 2}
books consulted: {'supports': 46, 'partial': 4, 'silent': 1, 'contradicts': 2} | by book: {'KLN': 9, 'CHEUNG': 4, 'HRN': 4, 'NYB': 4, 'LKT': 4, 'PHD': 3, 'WLD': 3, 'DEV': 3, 'HUB': 2, 'ARY': 2, 'KNT': 2, 'SYN': 2, 'MON': 2, 'AHD': 2, 'BRT': 1, 'BQT': 1, 'IEC': 1, 'SKT': 1, 'DOZ': 1, 'SOD': 1, 'POK': 1}
```


## [2026-10-15T02:53:36.052Z] TOOL CALL #69: SubagentHandback

```json
{
 "message": "I wrote the page 513 verification file (book page 483). `verify_check.py 513` passes with 0 PROBLEM lines, and all 18 of 18 nodes are covered.\n\n**Verdict counts:**\n- Roots: 3 confirmed (Tres, T.r.h, Tu). The two redirects, Tronkus and Trp, were skipped.\n- Nodes: 13 confirmed, 2 plausible, 1 disputed, 2 transcription_suspect.\n- The 2 plausible nodes are both in the Tres entry. The Avestan box mixes the real participle taršta with the root \"tras\" and a reconstructed *θrāsa. The \"Old Persian\" box (thrah-man, čah-man and so on) is not attested Old Persian; it is the reconstruction behind sahm, as given by Nyberg, Mo'in (Borhan p.1197) and Cheung.\n\n**Disputed:**\n- Tres, #8 English \"tremble\": tremble comes from Latin tremere (PIE *trem-, Pokorny 1092), not from terrēre. Watkins and Klein link the two roots only through a hypothetical *ter-. terrible, terror and terrific are confirmed.\n\n**Transcription_suspect (the misprint is in the book; the extraction matches the page):**\n- Tres, #5 Latin \"terěr\": a truncated, non-existent form; it should be terrēre (terreō).\n- Tu, #4 Germanic \"thŭmaz : yours\": no such form exists. Nourai's own reference (AHD) gives *thīnaz (Old English þīn).\n\n**Extraction errors:** none. The JSON matches the printed page in every box.\n\nEvery Nourai reference I could reach supports the chart. KLN:1592 is Klein s.v. terrible, NYB:172 is Nyberg s.v. sahm, and FFD:81 is Abolqasemi s.v. هراسیدن; HRN:86, BQT:484/1197/525, SOD:383 and KLN:949 also check out. FVA:246/247 (Nahvi) could not be checked because no copy is available. AMD:569 is only partly checked: the online Amid entry gives no origin, though Mo'in and Dehkhoda mark ترور as French.\n\nI archived the web pages I used with `fetch_source.py`. The four Etymonline fetches failed, so I left them out and used Wiktionary instead. I copied the page image to `data/verification/sources/refs/ocr/BOOK/513.png`.\n\nOutput file: `/home/sfmqrb/git/rishe-private/data/verification/page-513.json`"
}
```


### [2026-10-15T02:53:36.670Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
