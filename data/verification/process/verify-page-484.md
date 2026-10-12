# Verification process log — verify-page-484


## [2026-09-14T03:08:21.243Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 484 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-484.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-484.json. Write /home/sfmqrb/git/rishe/data/verification/page-484.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 484` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:22.327Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:23.123Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:23.138Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
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
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T03:08:23.561Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-484.txt"
}
```


### [2026-09-14T03:08:23.582Z] TOOL RESULT

```
1	=== PDF page 484 (book page 454) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Su 1, Esu, Wesu : well, good  (refs POK:342,1037,1174; KLN:548)  PART 1
4	#1 (parent #0) [Avestan] refs=POK:1037 | hu 1 : good
5	  #2 (parent #1) [Avestan] refs=POK:780,1037; HRN:111; HUB:57 | hu-apah : good deed ☞Op ; hu-čitra : nice faced ☞Skai ; hu-nara : good virtue, art ☞Ner 1 ; hu-vaeda : well known ☞Weid
6	    #3 (parent #2) [Persian] refs=BQT:2174,2297,2401 | xŭb «خوب» : good ; hožîr «هژیر» : "well faced" ; honar «هنر» : "nice work" ; hovaydâ «هویدا» : "well apparent"
7	      #4 (parent #3) [Hindustani] refs=AHD:328 | xuši : pleasant
8	        #5 (parent #4) [English] refs=None | cushy
9	#6 (parent #0) [Avestan] refs=POK:780,1037; HRN:111; HUB:57 | hu-nivâk : nice sound ☞Wekw ; hu-šnŭta : well satisfied ☞Kes 2
10	  #7 (parent #6) [Persian] refs=BQT:2174,2297,2401 | xonyâ «خُنیا (خنیاگر)» : "nice sound" ; xošnŭd «خشنود (خوش)» : "well satisfied"
11	#8 (parent #0) [Avestan] refs=BQT:717,737,748,2365; HRN:108 | hu-jasta : well wished, blessed ☞Gwhedh ; hu-parathwa : good to be crossed ☞Per 2 ; hu-rama : well rested ☞Rem ; hu-srav : well famed, famous (ruler) ☞Kleu 1 ; hu-mâyâ : well, blessed
12	  #9 (parent #8) [Persian] refs=BQT | xojasteh «خجسته» : "blessed" ; Forât «فُرات» : a river "to cross over" ; xorram «خرّم» : "well rested" ; xosor «خسرو (کسری)» : "well known" king ; xosrow «خُسر (خسور،خسوره)» : "famous" in-law ; homâ «هما (همای ، همایون)» : blessed
13	  #10 (parent #8) [Greek] refs=AHD | Euphrates : Euphrates river
14	    #11 (parent #10) [English] refs=None | Euphrates
15	#12 (parent #0) [Avestan] refs=BQT; FAF:708; ZMA:48 | hu-mana : well mannered ☞Men 1 ; hav-sivanga, hao-šyangh : good builder, with good household
16	  #13 (parent #12) [Persian] refs=BQT; FAF:708; ZMA:48 | Hŭman «هومن» : "well mannered" ; Hŭšang «هوشنگ» : "good builder"
17	#14 (parent #0) [Avestan] refs=VDQ:39; MAG:186 | hava-rd : well grown, well-built ☞Leudh
18	  #15 (parent #14) [Pahlavi] refs=MAG:186 | hu-rust : well built, beautiful
19	    #16 (parent #15) [Arabic] refs=VDQ:39; MAG:186 | hŭr : heavenly women
20	      #17 (parent #16) [Persian] refs=MON:1378 | hŭr 1 «حور» : heavenly women | extra: حوری ، حوروش
21	
```


## [2026-09-14T03:08:26.436Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-484.json | head -200",
 "description": "Read source JSON for page 484"
}
```


### [2026-09-14T03:08:26.477Z] TOOL RESULT

```
{
  "pdf_page": 484,
  "book_page": 454,
  "entries": [
    {
      "root": {
        "name": "Su 1, Esu, Wesu",
        "lang": "Indo-European",
        "refs": "POK:342,1037,1174; KLN:548",
        "gloss": "well, good"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1037",
          "words": [
            {
              "translit": "hu 1",
              "gloss": "good",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:780,1037; HRN:111; HUB:57",
          "words": [
            {
              "translit": "hu-apah",
              "gloss": "good deed",
              "script": null,
              "see": [
                "Op"
              ]
            },
            {
              "translit": "hu-čitra",
              "gloss": "nice faced",
              "script": null,
              "see": [
                "Skai"
              ]
            },
            {
              "translit": "hu-nara",
              "gloss": "good virtue, art",
              "script": null,
              "see": [
                "Ner 1"
              ]
            },
            {
              "translit": "hu-vaeda",
              "gloss": "well known",
              "script": null,
              "see": [
                "Weid"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:2174,2297,2401",
          "words": [
            {
              "translit": "xŭb",
              "gloss": "good",
              "script": "خوب"
            },
            {
              "translit": "hožîr",
              "gloss": "\"well faced\"",
              "script": "هژیر"
            },
            {
              "translit": "honar",
              "gloss": "\"nice work\"",
              "script": "هنر"
            },
            {
              "translit": "hovaydâ",
              "gloss": "\"well apparent\"",
              "script": "هویدا"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Hindustani",
          "refs": "AHD:328",
          "words": [
            {
              "translit": "xuši",
              "gloss": "pleasant",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "cushy",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:780,1037; HRN:111; HUB:57",
          "words": [
            {
              "translit": "hu-nivâk",
              "gloss": "nice sound",
              "script": null,
              "see": [
                "Wekw"
              ]
            },
            {
              "translit": "hu-šnŭta",
              "gloss": "well satisfied",
              "script": null,
              "see": [
                "Kes 2"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:2174,2297,2401",
          "words": [
            {
              "translit": "xonyâ",
              "gloss": "\"nice sound\"",
              "script": "خُنیا (خنیاگر)"
            },
            {
              "translit": "xošnŭd",
              "gloss": "\"well satisfied\"",
              "script": "خشنود (خوش)"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "همی باده خوردند تا نیمه شب - زخنیاگران بر گشاده دو لب",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:717,737,748,2365; HRN:108",
          "words": [
            {
              "translit": "hu-jasta",
              "gloss": "well wished, blessed",
              "script": null,
              "see": [
                "Gwhedh"
              ]
            },
```


## [2026-09-14T03:08:27.155Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T03:08:27.201Z] TOOL RESULT

```
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt`
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SBK.txt`

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt`
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt`
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt`
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KFL.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt`
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt`
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt`
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`

## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
- **RCH** — J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
- **NAT** — C. Berlitz, Native Tongues, New York 1982
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt`
- **PEI** — M. Pei, The Families of Words, New York 1962
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt`

## Turkic / Mongolian

- **TTS** — H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **VIE** — M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf`

## Sanskrit / Hindustani

- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
```


## [2026-09-14T03:08:30.606Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-484.json'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        if n['id']>=9:\n            print(json.dumps(n,ensure_ascii=False))\n\"",
 "description": "Show nodes 9+ of page 484"
}
```


### [2026-09-14T03:08:31.683Z] TOOL RESULT

```
{"id": 9, "parent": 8, "lang": "Persian", "refs": "BQT", "words": [{"translit": "xojasteh", "gloss": "\"blessed\"", "script": "خجسته"}, {"translit": "Forât", "gloss": "a river \"to cross over\"", "script": "فُرات"}, {"translit": "xorram", "gloss": "\"well rested\"", "script": "خرّم"}, {"translit": "xosor", "gloss": "\"well known\" king", "script": "خسرو (کسری)"}, {"translit": "xosrow", "gloss": "\"famous\" in-law", "script": "خُسر (خسور،خسوره)"}, {"translit": "homâ", "gloss": "blessed", "script": "هما (همای ، همایون)"}], "script_extra": null, "note": null, "quote": {"text": "همای بر همه مرغان از آن شرف دارد - که استخوان خورد و جانور نیازارد", "poet": "Sa`dî"}}
{"id": 10, "parent": 8, "lang": "Greek", "refs": "AHD", "words": [{"translit": "Euphrates", "gloss": "Euphrates river", "script": null}], "script_extra": null, "note": null, "quote": null}
{"id": 11, "parent": 10, "lang": "English", "refs": null, "words": [{"translit": "Euphrates", "gloss": null, "script": null}], "script_extra": null, "note": null, "quote": null}
{"id": 12, "parent": 0, "lang": "Avestan", "refs": "BQT; FAF:708; ZMA:48", "words": [{"translit": "hu-mana", "gloss": "well mannered", "script": null, "see": ["Men 1"]}, {"translit": "hav-sivanga, hao-šyangh", "gloss": "good builder, with good household", "script": null}], "script_extra": null, "note": null, "quote": null}
{"id": 13, "parent": 12, "lang": "Persian", "refs": "BQT; FAF:708; ZMA:48", "words": [{"translit": "Hŭman", "gloss": "\"well mannered\"", "script": "هومن"}, {"translit": "Hŭšang", "gloss": "\"good builder\"", "script": "هوشنگ"}], "script_extra": null, "note": null, "quote": {"text": "ای به لشکر شکنی بیشتر از صد رستم - ای به هشیار دلی بیشتر از صد هوشنگ", "poet": "Farrokhî"}}
{"id": 14, "parent": 0, "lang": "Avestan", "refs": "VDQ:39; MAG:186", "words": [{"translit": "hava-rd", "gloss": "well grown, well-built", "script": null, "see": ["Leudh"]}], "script_extra": null, "note": null, "quote": null}
{"id": 15, "parent": 14, "lang": "Pahlavi", "refs": "MAG:186", "words": [{"translit": "hu-rust", "gloss": "well built, beautiful", "script": null}], "script_extra": null, "note": null, "quote": null}
{"id": 16, "parent": 15, "lang": "Arabic", "refs": "VDQ:39; MAG:186", "words": [{"translit": "hŭr", "gloss": "heavenly women", "script": null}], "script_extra": null, "note": null, "quote": null}
{"id": 17, "parent": 16, "lang": "Persian", "refs": "MON:1378", "words": [{"translit": "hŭr 1", "gloss": "heavenly women", "script": "حور"}], "script_extra": "حوری ، حوروش", "note": null, "quote": null}
```


## [2026-09-14T03:08:33.067Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','HRN','HUB','BQT','MON','VDQ','MAG','FAF','ZMA','BRT','PHD','NYB','ARY','HJB','AID','IEC','SYN','WLD']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\"",
 "description": "Look up refs_online entries"
}
```


### [2026-09-14T03:08:34.065Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "

MAG {"title": "G. Widengren, Muhammad, the Apostle of God, and his Ascension (King and Saviour V), Uppsala 1955, ch. VIII 'Iranian elements in the Kuranic vocabulary'", "edition_found": null, "kind": "archive_restricted", "url": "https://archive.org/details/muhammadapostled0000geow (1955, lending) ; HathiTrust pst.000011130420 search-only", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": "HathiTrust has it search-only (limited view); Google Books ids -r4rAAAAIAAJ / h20wAAAAYAAJ are snippet view.", "notes": "RE-SEARCH 2026-09: borrowable only; not in DiVA; Google no view

FAF {"title": "A. Daneshgar, Farhang-e A'lam-e Farsi, Hafez Novin 1370/1991", "kind": "none", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}

ZMA {"title": "Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian, Bonyad-e Neyshabur 1374/1995", "kind": "purchase", "url": "https://www.gisoom.com / iketab.com listings (Balkh / Bonyad-e Neyshabur, in print)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only; no open or lending copy (grey PDF sites exist, not used)."}

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lo

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
```


## [2026-09-14T03:09:45.829Z] TOOL CALL #7: Bash

```json
{
 "command": "pdftoppm -f 484 -l 484 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg484 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg484.png",
 "description": "Render PDF page 484"
}
```


### [2026-09-14T03:09:47.648Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 100595 Sep 13 23:09 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg484.png
```


## [2026-09-14T03:09:48.487Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='POK_full.txt'\ntry:\n    t=open(p,encoding='utf-8',errors='replace').read()\nexcept FileNotFoundError:\n    t=''\nprint(len(t))\nfor m in re.finditer(r'\\besu-|\\bsu-\\s*\\(|Seite 1037|1037', t[:0] or ''):\n    pass\nEOF\nls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80",
 "description": "List refs dir"
}
```


### [2026-09-14T03:09:49.587Z] TOOL RESULT

```
3967710
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
```


## [2026-09-14T03:09:51.298Z] TOOL CALL #9: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg484.png"
}
```


### [2026-09-14T03:09:52.027Z] TOOL RESULT

```

```


## [2026-09-14T03:09:52.024Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:10:14.279Z] AGENT

Now let me grep the local reference texts.


## [2026-09-14T03:10:16.222Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"=== $f\"; grep -n -c '' $f; done",
 "description": "Check POK files size"
}
```


### [2026-09-14T03:10:17.283Z] TOOL RESULT

```
=== POK_01.txt
5152
=== POK_02.txt
6716
=== POK_03.txt
5975
=== POK_full.txt
93771
```


## [2026-09-14T03:10:17.343Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E 'esu-s|u̯esu-|vesu-s|wesu' POK_full.txt | head -40",
 "description": "Grep Pokorny for esu/wesu"
}
```


### [2026-09-14T03:10:17.414Z] TOOL RESULT

```
28606:Root / lemma: esu-s{\ su-) 
28773:See also: esu-s 
56232:agent ' in Old High German Id, Gen. lowesu. Modern High German Lohe, Middle Low 
69345:"pus', puti- 'faul, stinkend; Jauche, pus' = Avestan pJ/ay-'Fauligwerden, Verwesung'; 
84857:"Abzehrung, consumption, tuberculosis, Verwesung'; 
84867:verwesen', /i>^a "Verwesung', russ. tlja^ moth ' (compare under Latin tinea), "Blattlaus'; 
89997:poison ', vaesah-^ mould, dank decay, Verwesung'; Armenian ges^ carrion ';
```


## [2026-09-14T03:10:20.295Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28595,28640p' POK_full.txt; echo ---; sed -n '28765,28790p' POK_full.txt",
 "description": "Read Pokorny esu-s entry"
}
```


### [2026-09-14T03:10:20.377Z] TOOL RESULT

```
Serb. -Church Slavic ye'se'/?^, Serbo-Croatian yese/?; russ. osenb, \Nruss. Jes/eh; Old 
Prussian assanis (from *esenis or *asanis)\ Common h- > j- Slavic Albanian; h- >J-, y- Old 
Indie Tocharian. 

doubtful, whether here Middle Irish eorna {* esor-n-Ja) 'barley'; 

References: WP. I 161 f., Trautmann 71, Feist 58 f. 
Page(s): 343 

Root / lemma: esu-s{\ su-) 

Meaning: good, *noble, master, owner, lord 

Material: Gr. £u^, nuc; "proficient, good'. Adverb su (Akk. n.), belongs to prefix £u- 

Hittite a-as-su-us (assus) "good'; to a- s. Pedersen Hittite 167 under Anm.; perhaps as 
zero grade in addition (Friedrich IF. 41, 370 f.) the prefix su- see there; 

moreover perhaps Latin erus' the master of a house, head of a family, mister, master, 
owner, lord ', fem. era, Old Latin esa^ mistress, lady '; 

however, Hittite is-ha-a-as {ishas) "master, mister' is to be kept away, because this 
belongs to Armenian /sa-s/? "master, mister', /5A'a/"rule, reign' (?), even it is not of Indo 
Germanic origin (Couvreur H 9); 

gall. GN Esi/s (with §■) remains far off, probably because of the names with Aes-, A/s- in 
the earliest 1. a/s- or 2. a/s- (above S. 16), less probably 2. e/s- (above S. 299); also the 
Old Irish PN Eogan {*ivogenos) and the cymr. PN Owe/n {o\6er Ywe/n, Euge/n, Ougen) = 
Old Irish PN Uga/ne {*ouo-gen/os), compare in addition Bergin Eriu 12, 224 f. 

References: WP. I 161, WH. I 419, 863. Bin etymol. Versuch by Kretschmer, object. 
Konjugation 16 ff. 
See also: es- 
Page(s): 342 

Root / lemma: es- 
Meaning: to be 

Note: 

Root/ lemma: es-\ "to be' derived from Root/ lemma: eg-, eg(h)om, egd\ I' [Old Indie 

asmi'\ am' = a/iam ( *eg(/i)om) 'I'] 

---
not present ' ; 



about that perhaps belonging here gr. za-BK6q "proficient, good, lucky', Doric ioKoq, 
Arcadian tokoq compare Schwyzer Gr. Gr. I 533^, Specht Dekl. 256. 

References: WP. I 160 f., Schwyzer Gr. Gr. I 676 ff., Trautmann 71 , etc. 
See also: esu-s 
Page(s): 340-342 



Root / lemma: et(e)n- 

Meaning: seed; corn 

Material: Gr. swoq n. "a thick soup of pulse, pea-soup, mash of legumes ' one places to 

Middle Irish eitnem. "seed', Scots Gaelic e/fe"unhusked ear of corn', e/tean'see6, corn, 

grain'; the unlenierte voiceless -/- between vowels is puzzling though, because it can only 

go back to -//-. 

References: W P. I 117.
```


## [2026-09-14T03:10:21.560Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E 'Page\\(s\\): 1037|Page\\(s\\): 342|Page\\(s\\): 1174|Page\\(s\\): 780' POK_full.txt | head -20",
 "description": "Find Pokorny page markers"
}
```


### [2026-09-14T03:10:21.633Z] TOOL RESULT

```
28630:Page(s): 342 
29465:Page(s): 342-343 
63997:Page(s): 780 
64065:Page(s): 780 
83273:Page(s): 1037-1038 
92826:Page(s): 1174-1175
```


## [2026-09-14T03:10:25.599Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '83230,83280p' POK_full.txt; echo \"=== 1174\"; sed -n '92780,92830p' POK_full.txt",
 "description": "Read Pokorny p.1037 and p.1174 entries"
}
```


### [2026-09-14T03:10:25.676Z] TOOL RESULT

```
Page(s):1037 

Root / lemma: stru- 

Meaning: gray-haired, old 

Note: only Celtic and Balto-Slavic 

Material: Old Irish sru/th ^o\d, venerable ' {*stru-t/-s), acymr. strut/ug\. 'antiquam'; 

Lithuanian strujus^ graybeard '; Old Church Slavic stryjb 'patruus', 5//y/7ya'amita'. 

References: WP. II 651, Trautmann 290, Vasmer 3, 29. 

Page(s):1037 

Root / lemma: su-, su- 



Meaning: well, good 

Material: Old Indie su-, Avestan hu-. Old pers. u-, e.g. in Old Indie su-dr'u- "strong wood', 

su-bhaga- lucky, begliJekend', Avestan hu-baya-'good Ehegluek granting '; 

gr. UYin<; "fit, healthy' (*5^-^7/e5"wohllebend'); 

gall, su- (e.g. Su-carus=) eymr. /7y-^a/'"liebenswurdig', eorn. hy-, bret. he-. Old Irish su-, 
so- (e.g. su-thain^ eternal ', so-scel(a)e^Eyax\ge\\wxx\'); 

Germanie sJ-in Su-gambr/\/N, Old leelandie su-svgrtt 'Sehwarzamsel' ("die whole 
Sehwarze'); 

Lithuanian sudrus'horny, lustful, luseious'; Old Chureh Slavie Sbdravb ' u\/\r\q' , Czeeh 
zo'/'aKy (eompare above Old Indie su-dr'u-) ete.; Slavie *si>bozbje, Czeeh Zi&oz/'Besitztum' 
from *s-b-bog-b (= Old Indie subhaga-, above S. 107); 

su-\s zero grade to "s^e- (above S. 882 f.); eompare Old Indie sva- in sva-dha= su-dha 
" sweet drink, beverage, liquid whieh is swallowed to queneh one's thirst, draught, potion' 
(above S. 241), sva-dhita-= su-db/ta- 't\ght, firm, fit, healthy'; 

References: WH. II 512, E. Fraenkel Mel. Pedersen 443 ff., Vasmer 1, 450 f. 
Page(s): 1037-1038 

Root / lemma: suard- 

Meaning: to laugh 

Material: oapSavioc; 'hohniseh, spottiseh', aap5i^£iv 'hohnlaehen'; eymr. chwarddu, eorn. 

=== 1174
still vappa, i/5/O/o'kahmiger wine '. 

Maybe alb. i/S/oa 'summer heat' 

References: WP. I 379 f., WH. II 732 f. 

Page(s): 1149-1150 

Root / lemma: yes-6{*hyes-) 

Meaning: ' you ' 

See also: see above S. 514 l/'u-). 

Page(s):1173 

Root / lemma: yesu- {*hyesu-) 
Meaning: good 

Material: Old Indie vasu- 'good' (in addition i/asK/"' night'), vasun. 'blessing, Besitztum, 
property, richness ' (das Subst. after pronunciation and ablaut das primare), Avestan 
varjhu-, vohuds.. Old Indie Kas/ya/? 'better', vasistha- 'best', Avestan vahya, vahistods.; 
alt-lllyrian Ves-cleves, compare Old Indie vasu-sravas-, 

Germanic in proper name, e.g. Wisu-rTh, -mar, also Wisi-Gothae; gall, in proper name as 
Bello-, Sigo-vesus, Vesu-avus, Old Irish */ei6'(only in den case oblique covered, e.g. Dat. 
Sg. feib) ' excellence ' from *uesu-a, febas^ excellence ', *febtu. Gen. febtadql 
'substantiae'; ablaut. Old Irish /d'good, Gute' {*uosu-)\ besides *uesu- in Irish fiu^ 
dignified, honorable ', cymr. gwiwds., bret. ^tv/bi/ 'cheerful', gall. UTsu-nx, about uesu- in 
asian. Sprachen s. Bossert Mitteil. Inst. Orientf. 2, 78 ff.; 

besides eus- (with metathesis as in gr. £upo(;from F£po(;) in: 



Gothic /us/za' better', /i/s//a"Erholung, Erieichterung' (after Wissmann, D. alt. Postverb. 
d. Germanic 72 ff. post-verbal to *iusilon, as //7//o"Entschuldigung, excuse, alleged reason 
' to *inilon)\ Old Church Slavic i//7ye 'better' (Kompar. to an *uno- from *eus-no-); 

lllyrian PN l/ese/zaTelicitas'; Latvian 1/^5^/5 "fit, healthy, heil, unbroken, unmarred, 
unscathed, undamaged '; Old Church Slavic veseli^, Czech veselyetc. 'cheerful'; 

Tocharian A wse, B yss/'night' as *uesu^ the good '. 

References: WP. 1311, Vasmer 1 , 191 f.. Frisk 594 f. 
See also: probably to ues-2. 
Page(s): 1174-1175 

Root / lemma: uag- : uag- {*huegh^ 

Meaning: to be bent
```


## [2026-09-14T03:10:26.462Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '63950,64070p' POK_full.txt",
 "description": "Read Pokorny p.780"
}
```


### [2026-09-14T03:10:26.543Z] TOOL RESULT

```
Aryan A/? Old Indie nakham., n., nakhara-m. n., "nail, claw, talon ', np. naxun ds. (Aryan 

kh- an innovation); perhaps Armenian eiungnds. {*e-nungn): 

gr. (*/7j6vu^) ovu^, -uxo(; "nail, claw, talon ' (from *6vxu-?); 

The origin of labialized Old laryngeals: 

common Armenian Celtic *hue- > gw- > g- ; Latin gw- > u-. 

Latin ungu-is^Vr\e nail an Fingern and Zehen', ungula^ claw, nail, hoof, later also "nail' 
{*ongh-(em; 

Maybe zero grade in alb. {*huengla) thua " nail ', thundia, thundra^ hoof ' : Italian unghia : 
Spanish una : Calabrese ugna : Catalan ungia : Furlan ongule : Galician unlla; una : Ladin 
aundia : Portuguese unha : Romanian unghie : Romansh ungIa : Sardinian Campidanesu 
unga: Sardinian Logudoresu ungra: Sicilian ugnu: Valencian ungIa: Wallon ongue^ nail 

i 

Ladin aundia^ nail ' = alb. thundia, thundra^ hoof, thembra^ heel ' reflects common alb. - 
ng- > -nd-, -mb-. 

Also alb. ke-the-ter, kthetec "nail, claw, talon '. 

Note: alb. thoi, thua, pi. thonj^ nail ' : alb. thengjiir {*co3\) ash'; Root/ lemma: onogh-{: 
ongh-, nogh-, Celtic Qgh^, ongh-li-{* huen(e)gh-)\ "fingernail, claw' : Root/ lemma: ong- 
(better ang^ {*heng-)\ "coal'; alb. has preserved the old laryngeal. 

Old Irish ingent Dat. PI. ingnib, Nom. PI. ingnea, acymr. eguin, ncymr. em'nf., corn. 
euu/n, bret. /v/n{m. has changed) "nail' {*nghu-Tna); 



Old High German nagal, Old English n^gerv\a\\\ Old Icelandic nag/6s. (conservative 
stem has changed, PI. neg/); neg/ perhaps originally reinterpreted Sg. /-stem, compare Old 
Indie atighri-, and to PI., whereof are attached the additional conservative Dekl.), Gothic 
ga-nagljan^ nail '; 

Lithuanian nagas m. " nail in fingers and toes; claw of birds of prey ', Latvian nags ds.; 
Lithuanian naga'hooT, Old Prussian nageloot', Old Bulgarian noga, russ. nogaloot' 
(collective a-formation); Lithuanian nagutis. Old Prussian nagutis^ fingernail ', Old 
Bulgarian nog-btb, russ. nogotb "nail, claw, talon '; 

after Specht to gr. oyKoq (above S. 46), also root on-. 

References: WP. I 180 f., Trautmann 192, Specht Indo Germanic Dekl. 253^. 
Page(s): 780 

Root / lemma: o/70-and one-, also (o)no-d- 

Meaning: to scold 

Material: Gr. ovopai ' scolds, reproves ', ovoto^ ' reproved, reproachable ', ovotq^w " 

scolds, reproves '; with -a- the second syllable of hom. wvaro and ovarai aripia^STai. 

IjepcpETai Hes.; 

Middle Irish 0/7' shame'; perhaps with reduplication-stem also the first syllable of Middle 

Irish anim {i-siero) 'blemish, fault, error', acymr. anamou^ mendae ', ncymr. anaf. Middle 

Breton a/7a^'blemish, fault, error'. 

extension (o)no-d-\v\: Avestan nadento^ blaspheming, slandering ones ', gr. 
ovoaaaaGai "rebuke, reproach' etc., ovogtoc; " reproachable '. 

References: WP. I 180. 
Page(s): 779 

Root / lemma: opi 
See also: see below epi. 
Page(s): 781 

Root / lemma: op-1 {* hue-p-) 

Meaning: to work, perform 

Material: Old Indie apas-u. "work' (= Latin opus), Avestan hv-apah-'goo6 work 

(verrichtend)'; apas-n. "work, religious action'; apnas-n. "yield, property, possession ', 

Avestan afnah-vant- " richly in possession '; 



gr. {* h3^\^T^\/^\) 6|jnvr| f. "nourishment, food, BromicnT ', opTTVioq " nourishing '; 

The origin of labialized Old laryngeals: 

common Armenian Celtic *hue- > gw- > g- ; Albanian gw- > v-. 

Maybe in e-grade alb. {*hueper) veper' work' : Latin opus, -e/75"work'. 

Latin opus, -er/s'work, occupation, action, work', opus est ^ it is necessary ', whereof 
opero, -a/ie'work', Oscan upsannam^ operandam ', (under the influence of common Celtic 
-ns-, -nt- > -nn-), upsatuh senti^ fact! sunt '), Perf. upsed^ fecit ', uupsens ' fecerunt ', 
(lengthened grades Perf. as in Latin odl), Umbrian osatu^ facito ', Paelignian upsaseter^ 
fieret '; Latin ops, O/O/s "fortune, richness, power; help, assistance ', by Ennius also " 
endeavor, service ', officium ' obligation ' < *opi-ficium ' working performance ', Ops " 
(Latin: "Plenty") was a fertility deity and earth-goddess in Roman mythology of Sabine 
origin ', inops, cdpia{*co-opia), opulentus^ incredibly rich in property, mighty ', probably 
also opt/mus't\r\e best' (actually "the wealthiest') ; perhaps the name the Oscl, OpscT, 
'OniKoi as ' admirers of the Ops' and Latin omnis 'all, whole, each, every ' ( *op-ni-s); 
perhaps Old Irish somme^ncW, domme^ poor' {su-, dus-op-smjo-); 

Old English efnan. Old Icelandic efna^ work, do'; lengthened grade Old High German 
uobo^ land farmer', uoben^ place at the work, exercise, revere, worship ', Modern High 
German ijben. Old High German uobam. PI. " celebration ', Middle High German uop^ 
practice, agriculture ', Old Saxon dbian^\\o\6 festivities'. Old Icelandic 0fa^ train, practice ', 
j0/^"vast, grand, violent'. Old Icelandic efna^ commit ', efni^ material, stuff for something '; 
about Old Icelandic afr power ' etc. see above S. 52; Hittite happinahh- ' make rich '. 

References: WP. I 175 f., WH. II 209, 217 f. 
Page(s): 780 

Root / lemma: op-2 

Meaning: to choose; to suggest
```


## [2026-09-14T03:10:40.291Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in 'hvapah' 'hv-apah' 'huc̨iθra' 'hucithra' 'hunara' 'huuaēδa' 'hu-nivāka' 'hunivāka' 'huxšnuta' 'hujasta' 'hupərəθβa' 'huparathwa' 'husrava' 'haosrav' 'humāya' 'hūmanah' 'haošyaŋha' 'huraoδa' 'huraodha'; do echo \"--- $w\"; grep -n -i \"$w\" BRT.txt | head -5; done",
 "description": "Grep Bartholomae for Avestan compounds"
}
```


### [2026-09-14T03:10:41.507Z] TOOL RESULT

```
--- hvapah
30643:hvapah-
--- hv-apah
30647:•  j'i  g-  hv-apah-  i)  (im  gAw.)  n.  'gutes Werk,  Wirken':  ahyd  xsa'i'racä  maifitUca *'pa»hauca ''  tSm  at . .  yatamaidf  "wegen seiner  Herrschgcwalt  und  Grösse  und  seiner schönen  Werke  wollen  wir  ihn  . .  verehren" Y._57.  2.  a)  (im  jAw.)  Adj.  'gute,  schöne Werke  verrichtend,  wohlwirkend',  von AhM. :  azim  . .  dämanam  nipBta  ahmt  'pg (VS,,  nämL  ahura  mazäa)  Yt  70.54;  54;
--- huc̨iθra
--- hucithra
--- hunara
6346:•  ].  aäahunara-  Adj,  'des  Können  (usw.) gross  ist,  vielvermögend':  ««'är?* Yt  10.  25.
7035:yeü,  ß)  vorausgehendem  yen  'Svenn  aber, wenn  jedoch",  kondiz.:  a)  *yujyastis  hala *nmä>tat  . .  a°  yat  he  aoxte  .  .  dka  *hä *x!ayae  .  .  haxtöit{%A.)  N.A'f.;  V.7.3 äat  (s.  ?•)  yg  .  .  upairi  hunarain  (sd.)  maiiü barst  .  .  J'  yaj  .  .  faiti  barät  aat  (s.  z) yat  .  .  ava  baraite  "wer  .  .  aber  wenn  er .  .    und    wenn    er    .  ."    P.^jjf.;    —  yezi
14059:•  j.  draxtö.hunara-  Adj.  'der  gelernte Fertigkeiten  besitzt,  Kunststücke  kann' vom  Luxushund'*:  iünqm  .  .  'narattam V.  IJ.&;  —  *ui  *täät  Spina  patfnti  pasus.- Aaurvam äi  (sd.)  ..  "naranamia  V.  jy.  42.
16818:hinzubringen  zu  — ,  an  —  hin'  (Akk,)i haoma  .  ,  ya  nasäum  ava.b?r»ta  Y.6. 42 '"'.  5)  'wegtragen,  wegbringen':  ava aS?m  iristfm  baraym  V.8.2;  3.  Un- deutlich P.jA';  s.  unter  hunara-.
18454:•  j.,  g.  nae-kay-  neg.  Pron.  interrog.  'non quisquam',  nur  substantivisch  'nemo;  nihil': %waAy3  xratsus  ylm  'Si  dabayäti  (sd.) y.43i>\  —  y3m  vä  '''üs  dänst  iil  (sd.) Y.  43-  13;  —  *frasafntlmca  .  .  yeäha pourBsta  htyjayan  'cisca  aiii/ia  yäsaili zyänäi  (sd.)  Y.  05.  1 1 ;  —  yahmat  haca °eii  bunjayai  .  .  nSit  ^usyqs  i^A^  tacö  .  . Aog.jSB.;  —  yaf  mqm  'a/  taurvaySi nsil  dafuö  nai^a  .  .  Yt  /.  6.  a)  mit Gen.  pari.:  'iil  a^arftiiam  tva  rait  .  . asayqm  (sd.)  nsit  .  .  V.^.iy,  —  yS  'Sm isaiti  hunaranqm  V.  jj.  19;  —  a^qm alnauhqm  'clt  vJdvh  aojöi  (sd.)  Y.  32. 7.  na^im,  naiHs  als  Neg.  sbes.;  vgl. auch  na^üxit  mit  No.
--- huuaēδa
--- hu-nivāka
--- hunivāka
--- huxšnuta
--- hujasta
--- hupərəθβa
--- huparathwa
--- husrava
--- haosrav
4810:1.  a)  "herausgehen  aus  — '  (Gen.):  vai- \anhS  (sd.)  n5/V  uzSis  (aSPrA.)  V.J.  15 PüZ.(?).  a)  'aufgehen',  von  Gestirnen: yaira  avat  hvars  uzliti'J^F.4h.  3) 'hin- auskommen über  — ,  über  werden',  mit Äaca  und  Gen.r  ya'ia  as»m  uzayeni  haia kavsis  haosravauhahe  Vt  i^.  32.
6305:•  j.  aäavasta-  n.  'Besitz,  Erwerb  des (höchsten)  Anrechts':^»  "^wä yäsämahi havauhum  't*m?a  haosravaahftn  Imru- mauii  Yt  10.33;  —  yüimäkim  yasnäica paimaUa  yal  am3sanam  spmtanqm  a/imä- ifM    hmHiauhäica    °täica  yal  taosyantqm
6372:•  j.  aää'vaohav- m,  EN.  eines  Gläubigem 'störend':  -mirmls  (als  NS.)  yaiia  kava ^ifh}us  hii'attdatihahe  asaonS  Vt. /J.  uo.     ^*haosrava  Vyt.  2  (?)'*.
6888:"  j-i  g-  'ahura-  m.  i)  jAw.  'Herr,  Macht- haber, Fürst":  'rO  *sästr)nqin  äaiiihupai/is VliJ.  37;  —  ^wqm  yazante  aurvanhB -ränhs  äai^hu.patayS  ¥1.5.85;  —  yim fnäml.  z'jrf^raytam)  vasiinte  'rät^hö  .  . ähuiryarffa  .  .  haosravatahanS  Yt  i4-  39;
7096:•  j.  ä'xrüra-  m.  EN.  eines  Gläubigen: "rahe  haosravanhalte  asifOHü  "des  A.,  Nach- kommens des  //.  .  ."  Vt.7y.137".
--- humāya
--- hūmanah
--- haošyaŋha
--- huraoδa
--- huraodha
```


## [2026-09-14T03:10:51.563Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in 'wohlgestaltet' 'schön gewachsen' 'schöngewachsen' 'hu-raoS' 'huraoS' 'hu-rao' 'haosyaiih' 'haosyan' 'Hao!yan' 'hu-mäy' 'humäy' 'hu-manah' 'hümanah' 'hu-sravah' 'husravah' 'hu-parat' 'huparat' 'hu-jasta' 'hujasta' 'hu-rSma' 'huräma' 'hu-räma'; do echo \"--- $w\"; grep -n -i -- \"$w\" BRT.txt | head -4; done",
 "description": "Grep Bartholomae with OCR-tolerant patterns"
}
```


### [2026-09-14T03:10:52.762Z] TOOL RESULT

```
--- wohlgestaltet
30150:•  j.  hu-kshrp- Adj. 'wohlgestaltet':  vatihus haomS  .  .  'kfnfi  Y.p.  16;  F.  ja.
30156:wohlgestaltetste':  ahurahe  mazdä  .  .  'ma- heca    Y.  I.  i;    —    fravallnt    avqm    yqm ahurahe  masda  .  .  •mqmca  Y.  26.  a. Pü. :  htitarplum,  erl. :  hii  hatidäm  eBok  5  diß-
--- schön gewachsen
--- schöngewachsen
--- hu-raoS
--- huraoS
--- hu-rao
30486:•  j.  hu-rao5a-  Adj.  (fem.  -oa-)  'von  gutem äusseren  Ansehen,  von  schönen  Formen'; a)  von  a)  Menschen  und  ß)  Göttern;  n a):  caräili  -sa  (NSf.)  V._y.  34;  ig.  30;  — kainJnö  kthrpa  'oayi  H,  2.  9,  Yt5.  64;  — '})0  ¥.3  a.  zu  ß):  sraosS  afys  "Wf  V. z^.  40;  —  srao/a  asya  'oa  Y.  57.  35,  JÖ, 65.12,  Y. 18.2a,  31;  Y.2.7,  57.3,  V./9 15,  Az.6,  Vd.i2;  —  nairlm/a  saakM •&/«  Y.37,3,  Vyt40;  —  amaktla  hutääahi 'oaie  Y.1.6;  2.6,  Yt/47;  —  astm  ■■ 'äara  Y,2.r4,  Yt77.i;  —  andvTm  ..'if* Yt.5.  15;  —  drvaspqm  ..  'lam  Vtp. 2.  b)  sonst:  ianüm  ya  mf  valnaüe 'f^ Y.  io.  14;  —  yetihä  (sd.)  k>Arj>s  •oayä  Yt
30492:•  j.  *hu-rao8ay-'>  f.  'gutes  äusseres  An- sehen'; nSil  astS  *hutastlm  nsit  tanvS *'raoiljm ''  "nicht  guten  Knochenbau  noch schöne  Leibesform"  P.  4?.
30494:•  j.  hu-rao8ah-  Adj.  (auch  fem.)  sva. huraoaa-  (sd.) :  y>nS  ,  ,  'hatshB  (APf.)  Vr. 2.7.
--- haosyaiih
--- haosyan
15384:•  j.  'para-Sita-  Adj.  Ehrentitel  des Fürsten    Haolyaaka:    haoSyanhö    'td   Yt
28795:haoSyanha-
--- Hao!yan
--- hu-mäy
30428:•  g.j.'hu-mäyä-,  j.'hu-mayä-(mask.*^a-) Adj.  'segensreich;  gesegnet':  °mälm  i)Wä iilmyazat>m  alatihääm  dadamaidt'aizAeYi segensreichen  setzen  wir  dich  ein,  als  den erfolgreichen  . ."  Y. 41. z;—  yai  hJs  (näml. däman)  'mayaca  liyäca"  äna^amaideVi. 12, 4";  —  'maya  aita  däman  *dähimaide 'maya  clsmaide  'maya  matnyämaide  *yam da^at  ahurS  mazdä  Vr.  72.4'';  —  'maya upar»ha  (sd.)  cllmaide  ahunahe  vairye?u Vr.  12. 2;   —    'maya   nö  buyati
--- humäy
15591:•  j.  pairi.}a9«n-  Adj.  'herumgehend',  vom Priester,  der  auch  ausserhalb  des  Lands Dienst  tut');  daiAhäurvaisim  Sstäya  Au- mäim  '%n?m  astüya  Vr.j.  3;  —  *daiti- häurvassahe  . .  humäyeke  '^nd  Vyt.  ij;  — ava  baiiaza  ,  .  htimäyehe  °%tiS  Vr.  ^.  2.
20906:—  vahilla  cCira..yii  slaoia  yesnyaYt.23.  rake  masda  X.26.z;  — yazaEta  ml  him i;  —  vupäca  diima  .  .  yä  asava.däia  Y.  ..yqm  ar?dflm  Yt5.i.  c)  APm.:^i> 7/.  6.  a.)  ava  bai&aza  .  .  yl  humäyehe  . . /myatät  (&d.)  *aAma  *yq  am.'sS  spmif yäi  .  .  Yi.g.  a;  —  tä  ..yä  staota  yesnya  YLi.24.  «)  ave  strSus  yq  kapHiringa Y.55. 3;  70. 3 f.'*;  —  täca  vohü.,yä  antar?-  YlÄ  la;  —  yä-  ave  sIrSus  aiwyäxiayänti itä  Yt7^.i53; — aaa  dämqn  ..  yä  hätqm  yqm  Aaptöiritig}  ..Yt.  13.60;  —  *tqm  ya- mazistata  ..  Vr.  i2.  4;  ■ —  aiwyäxsayeinti  zäi..*yqm  am>is sp?nisY.~Q.\.  d)ISmT avqm*x^örqm.,yqm{h¥a.)  zardktdtrahe  n,:  vohu  mana^ha  haHmng  asä(a  yä  va- Yt.13.fi2.  g)t^.-AD{.:a)gae^yäi  te  ydi  hisia  xsa^räca  yä  vairya  FrW.j.i;  — abd3.t}meYt.S.3i,.  Z)mandemKasusJ'>;  *tarynya  aoira  (sd.)  *piifi.smuxia  yä a)  ASm.:  yS  janal  azim  ..yim  aspB.-  vlspü.pTsa  bämya  Yt5.  78.  e)IPm.,  n.: ganm  .  .  yim  vUavantim  .  .  yim  (s.  I)  rao^ibJs  .  .  yäis  afuirahz  matdä  Y, J<i'6; upairi  *vi/  *raooat  Y.g.  11;  42. 4,  57,  4;  |  —  vTspais  .  .  karhqn  yäit  Aapta  Y.  61.
20920:asavJ  eara'iuslrOY.i2.6;\t-4.T,  —  zatö  be'.mraomi  (sd.)  ..yam  dahmqm  ..  S/rTlTm yS  a/ava  saraiiuärB  y.ip.  46;  Vr. //.  19, '  P.j;^.  c)  IPm.,  n.:  pairi  yäi/  hapta Yt5.io4,  14.2S,  IJ.47;  —  nazdyB  tqm^  karsvqrt  mairyB  apatat /ratgrase  "Vt.  ig.%3; upahi^tat  y  B  spitilfnB  zara^us'tr jYt.  ij.  21;  —  humäyQ.tarala  .  .  inhäma  yäü  ipm- 1 8, 10,  V.  JJ.  1 7 ;  —  uHa  nd  siitB  lihrava  yB  tahe  mainySul  dlmqn  Vr.  12.  4. spittimB  sara^ui/rB  Yt  13. 94  fodcr  zu  A); —  [  Von  undeutlichen  oder  verderbten  Stelleo jasani  il  ava»ha?ca  rafttai>ha!'a  (iwffi_j'5|  erwähne  ich:  hamSm  tatvahUtähtySusu- (zu  A)  ahurS  mazda  fasäiti  .  .yB  varthui  ruy!  syascU  dahmahya  Y.J2. 16;  —  tiBit sraosS  .  .  jasaiiti  .  .  yä  (s.  d)  äpB  Yt  /.  9;  i  ftä  xsnäul yä  v»r>ZSnä  hScä  Y.  4^- 1 ;  — 10. 100;  — yaiä  aha  vairyB  zaotä  frä  tnl  yä  (NDra.)  nara  gatum  baraite  F.^d;  — mrütg ya'iia  aha  vairyB  yä  zaota  frä  mZjaht  ..yB  xsudra  ham.raS%wayäH  V.lS. m^fi/f  Y.J.  25;  N._y7*,  Vr._j,  7; — paoinm  6a '^^i — yS  hapta  hmdu  V./,i8;  —  upa gtima  frabarat  yö  narif  asaonS  urva  H.  2.  |  a^a^u  (sd.)  rauhaya  yB  asärO  aiwyiixia- 15;  7i  8,  15;  —  bavat  aiwl.vanyh  yasi  yanti  V.l.  19;  —  psityh  ähitya  yä  anrö taxmS  kava  vlsiäspö  \X.iy.%i;    —   yim  mainyui  fraksrtniat  V.  20.  3;  —  aridvim
30423:•  j.  'hu-mayä- Adj.  (mask. ''_>w-):  5.  unter humäyä-.
--- hu-manah
30417:•  j.  hu-manah-  Adj.  i)  'des  Denken  gut ist',  stets  in  Verbindung  mit  ?tvacah', husyaö^na-  und  kudainä-:  yvSfum  °na- aham  kvaca^ham  husyaokmm  hudalmm ^^-  J-  3  i  —  yUnü  fiumanatfhö  kvacanAs huiyao^nahe  kudafnahe  H.2.18;  Vytl*;
--- hümanah
--- hu-sravah
30511:•  j,  hu-sravah-  Adj.  'der  einen  guten Ruf  hat;  berühmt'.
--- husravah
--- hu-parat
--- huparat
--- hu-jasta
--- hujasta
--- hu-rSma
--- huräma
--- hu-räma
```


## [2026-09-14T03:11:00.627Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30380,30560p' BRT.txt",
 "description": "Print Bartholomae hu- section"
}
```


### [2026-09-14T03:11:00.679Z] TOOL RESULT

```
'iqm  fräyaayarUqm  \T.14.  i.  ;  alles  was  (man)  kann  und  vermag*:  /iwW-
yavJniA  frac  yatem,    (lu  Vr.  /Ö);    fehlt.    —  ■;,  j  ■         ■        „  i
■)  rBild.  s.  a^m.  -  «)  S.  lu  hufram^^lqm     ■  ■  ^^  "O^  «"<*  »"*  all«™.  ^^  d«»  S^^
No.  2.  jSinn  vennag"  V.jo.  8.
.    ,        ,  _,  .  ,.   ,,  ,  .  .  '       AbleiL  BUS  '^nar-,  »va,  kunara..  —  Pö.:  ö*.
•  j.  hu-fra'yuxta-  Adj.  '(gut  geschmt  sva.)      „-  i„ik  ^  j,  ,  z-aÄ«™«  a^mt  «»i;»«,  eri.:
gut  geführt,  geschwungen"':  iaritacit  aiiam\  frärm  kvnarih  rSl  yam  atl;  Si:  rvam  yai  te •ta    .  .   Yt  /0. 40.  "         '  ■  ■  *'"'"*  pravarlamänäÄ  ianü.
4i.  ™/raj.»*/a-  Adj.  -  .)  Vgl.  Yt  13.  1%.      ! ,   j     hunairySnk-  Adj.   'geschickt,  ge-
j.  hufräimi.d-  a.so:  lies  Aü /r".  'wandt":  mthnm  ..  'yinäm  raialstqm  Vt.
•  j.,  g.  hunav-  m.  'Sohn'  uzw.  i^aÄnschcr!  ^O-  '<";  —  «""^  kihrpa  .  .  yancö  Yl Wesen'*:  kvB  datnBil  drUjS  'nul  "der  ist  \  ^'-  •3-
ein  Sohn  aus  der  Schöpfuiw  der  .Dr."|  Komp.  mit  (Ableit.  ans)  •*,«fl/rr--(?)f..  sn. \.  51. 10 -j  —  'navO  {UV.)  i0uru.*ao>:ranqm\  '*    ''  ' -^  ^
(sd.)  Ytfo.  113;  —  nurvii  'H.it'J  j'aäti-]»  j.  hu-oi'vixta-  Adj.  'gut  hera,bge- kaya  (sd,)  Vtj.  57;  —  >ff  /a«a/  °navB  Schwüngen,  gescbleuderf :  vazrvm  -ttm {ais  AP.)  yai  pa^^sanaya  nava  •ruivasca\kamfr^e  paiti  daffvanqm  Yt().%;  10.  1^2; nivikahe  •navascd*  ..  Yt.  7(^.41;  5.  54.        , —    vatrö  'tB  Yt.i^.'jt;    —    vaxracit  .  .
Znm  V.  ihav-.   —  Vgl,  kaola..    —    ai.  süniv-    'ta  (NP.)    Yt,  10. 40.
m,,  goL  sUHUs;  iVerSch.  «  -  »  s.  BtHl.  IF.7.  1  Zum  V.  t«i<p-.  —  Vgl  vaa-  i  hufixl  fVd.i.  —
107.    —    Pa.  (lu  y.  5/):  humiSait).  —  ■)  Im  I  po.;  ^kuvixt')  (NpÜ.i  ^ii  miida),     d«iu    die
Gegen».  lu /uSra-.   —  >)  Aus  dem  Aw.-Won  Erl.:  ^kuvixOk')   e  tu   iäsiän   mtnöü/ij    oft
gefonnt,  vgL  Pü.  lu  luuat!rö.kuna-  und  hutm- '  ^avtl  u  vinäiiärän  päli/räi  afii  iuntt  u  m/nä-
Saitnilan  (unter  ihav)  und  JusTi  PrJ.  88. 147, :  iiAi  5  kanCir  {i^it).   —    '»  Geschi.  an  o  mam
WEST  SBF_  4^.  40.  51,  39.  \,km,ixm-i)  sUtt  annd«;  B.  No.  2.  —  »)  G«chi.
•  j-,  g.  hunara-  m.  i)  -Können,  Kunst':'     «"""°>'  «""  »"dstda;  s.  No.  i. kyal     da     ^yaohana     mlidavqn    (sd.)    .  .  •  j.  huovana-  Adj.,  PPM.:  s.  'Aai-. %wä   'ra   ".  .  durch   dein   Können"   Y.  ,  j.  hunvant-  Adj.  (fem.  'vaintt-),  PPA.: 4^.5".         a)  'Kunstfertigkeit,  Geschick- js,  'hav.
lichkeit':    kva    asti    spä    vokunazgB  (sd)  1      .         ,  .  ,.  ,  ,     ,
daityBgätusl  .  .  ys  nfi^m  haiti  'ranam  '  "  >•  g- »»"-mata-  Adj.  gut  gedacht" ;  stets V.  13. 1 9-  3)  Tüchtigkeit,  persönlicher  ■  "«be-i  huxta-yx.^  hvarsia-  (Stverz.) :  nar^w.
Wert':  yS  .  .  upairi  'r>m  manS  barät  .  .  ■""»«""«  dat>rän?m  Hfmca  manB  hOx/fmca yat  hl  *man3  ^ahe  patti  bar3i  . .  yät  hl  ^"'"'^  hvaHt«nca  lyao-htam  Vr.  2.  5;  usw.; *mafas*aht\paiü-\  ava  barait'e  pascaäa . .  "  ™  Gegensatz  zu  äumaia-.  yupa  'ta "wer  seinen  Sinn  höher  als  seinen  Wert  ■  ■  .'*»^«  ■ ;  ^'"'"'«  b<foB.varsta,  vlspa trägt«,  ..;  wenn  er  aber  seinen  Sinn  ihm  y"^"^«  ■■ 'i^'^'' -■ '^"^''"''^  «*'-' '*'«'^-- entsprechend  trägt,  . .  und  wenn  er  seinen  1  ^f  ^''t^^  :?"  '="*"'■  .  ^]  ""  ,!'°S-  ""'' Sinn  darunter  trägt,  dann  ,.  P.jjf.  Plur.  Name  des  ersten  der  drei  Vorräume
KompE.;  Ableit  -  S.  auch  hunir.iit.,  das  I  des  Paradieses:  paoirlm  gäma  . .  yg  nan
ein  *Aunar-  vorauMetit.  —  ai.  iSndra-  Adj.;  asaonS  UTVa  'te  paiH  niäaöäi  bütm  .. mp.  (PQ.),  np.  hunar  'Fertigkeit'  usw. ;  s.  daiu  \  haxU  .  .  ^rittm  .  .  hvarHe  (sd.,  Stven.) Hbm.  AGr.  /.  i8i.  —  Et.?    Schwerlich  richtig  ,  ti  „      , .
OLnKNBERG    ZDMG.  JO.  442.  —  ')  Vgl.  diutvä:  |  "^^  .  ■  '  5 '      ="'-  B-        1  ,  /T  L    ,
-  ')  D.  i.  wer  sich  mehr  dünkt  ds  er  wert ,  ""  "™'^-  •»■  EN.-Pu.:  humat  (Trans.Vr.). ist    Pü. :  ki ..  afar  hai  kunar  menisn  baräi, '  ,   j,  humatanam    litirt   die    damit   \>i-
daiu  die  Ert.  von  «i/arwamA,; durch /fliawtr  S^^'"^^     t"  ?   %    ■-^■^      - -T  ^
•Anmassung'  in  SWieoAW.  S/.  838. 19,  temer  «pastuyat  bts  hu'  ^rts  huxsdkrüjmat  .. Mx.  2.  4  ff.  \Jrasr3vayBit  V.  jÄ  43.
dby  Google
1833
*humatay-
humizda-
1834
•  j.  *hu-inatay-"  f.  'gutes  Denken';  niana-
Khasia  'maiti  kizvasca  häxti  zastayasca *Avariti  *raüwyB.V(trsti{aA.)  F.sS,
ai.  sumaläy-  f.  —  PQ, :  Aac  minisn  humal,  — ')  Hds,  ahum'. j.  humat  P.  7J:  lies  ahumal.
•  j.  hu-manah-  Adj.  i)  'des  Denken  gut ist',  stets  in  Verbindung  mit  ?tvacah', husyaö^na-  und  kudainä-:  yvSfum  °na- aham  kvaca^ham  husyaokmm  hudalmm ^^-  J-  3  i  —  yUnü  fiumanatfhö  kvacanAs huiyao^nahe  kudafnahe  H.2.18;  Vytl*;
—  yum  'nS  kvacS  *hulyao^na  *hudaina H.2.ir,  12;  —  haxayS  . .  'natakB  hva- ioTihS  hu^aöiinäahö  huoa^na   Yt/^.  95;
—  yünat  haca  'nanhai  hvaiarfhat  hu^ao- %nat  hudainal  P.33.  2)  'gutes  Muts, wohlgemut':  ydäa  valm  °na^hs  (NPm.)  . . vanäma  vlsps  *ham3r?k}  Yt.  10.  34,
AbleiL  —  ai.  sumänoi-  Adj.  'wohlgesinnt; wohlgemut'.  —  Pü.:  huminisn.
•  j.  humayaka-  m,  EN,  eines  von  Zairi.- varay  besiegten  Feinds  der  «laai^schen , Religion:  tarn  (nätnl.  aradvini)  yazata  .  .\ tairi.vairiS  .  .  avai  äyapiim  dazdi  mW  .  . yat  bavsni  aiwi.vanyk  pisd.Htigham  astö.- künim  'kfm  dalvayasnim  ". .  den  £>atva- anbeter  Hum.,  der  mit  weit  ausgestreckten Klauen  in  den  acht  Höhleniäumen  hauste" Vt.J...3'>.
Ableit.  aus  hiimayä-,  —  Vgl.  den  arm.  EN. Amayeai,  Hbsi.  AGr.  /.  47.  —  ')  Danach  war Hiim.  ein  Und  wurmartiges  Ungeheuer.
•  j.  'hu-mayä- Adj.  (mask. ''_>w-):  5.  unter humäyä-.
Ableil.
•  j.  'humayä-  f.  EN.:  s.  \mX.ex  humaya-,
p.  kumavarkä  D.  6,  3:  lies  hauma'.
•  p.  *'u-martiya-  Adj.  (fem.  °y<i-)  'wo  die Menschen  schön,  gut,  tüchtig  sind';  dahyäuS pärsa*  .  .  Ayä  .  .  ''uvaspä  °ya  D.4.2;  — xsa&''am  . .  lya''  ''uvaspam  yam  D./7.  i.     ,
•  g.j.'hu-mäyä-,  j.'hu-mayä-(mask.*^a-) Adj.  'segensreich;  gesegnet':  °mälm  i)Wä iilmyazat>m  alatihääm  dadamaidt'aizAeYi segensreichen  setzen  wir  dich  ein,  als  den erfolgreichen  . ."  Y. 41. z;—  yai  hJs  (näml. däman)  'mayaca  liyäca"  äna^amaideVi. 12, 4";  —  'maya  aita  däman  *dähimaide 'maya  clsmaide  'maya  matnyämaide  *yam da^at  ahurS  mazdä  Vr.  72.4'';  —  'maya upar»ha  (sd.)  cllmaide  ahunahe  vairye?u Vr.  12. 2;   —    'maya   nö  buyati
'hävana  ayanhama  hävana  Vr. /2.  5;  —
ava    baslasa   .  .  ya    'm3yehe    alaenS  yä
'mäyehe  pairi/dhnö  Vr.  g.  i ;  Vyt  ij.
Ableit.  —  Vgl.  'humäyä-  und  humayaia-'E.'A. —
PD.  :  hufrantän,  hu/ramänlh  (Sü. :  iuihäätialä).
—  ')  Vgl.  Y.  4'-  3-  -  »  Vgl.  iSt.  Gdn.  BB. 15-  253-  Mir  ist  der  Sinn  von  Vr.  u.  4  nicht ganz  deutlich.
•  j.  'hu'mäyä-,  "hu'mayä-  f.  EN.  einer Tochter  Vl/täspas:  tarn  yazata  ..  visiäipS .  .  dazdi  ml  .  .  ya'ha  .  .  uta  azfm fraourvaaayeni  'maya  (IS.)  *värioJianqm (sd.)  hyaonya  haca  daiAAävs  ".  .  und dass  ich  wieder  heimbringe  sammt  der H.  die  V..."  Ytp.  29ff.'>;  —  'mayä (GS.)  aSaonyi  Yt/J.  139.
Vgl.  f/mmiyä-  Adj.  —  mp.  humäy,  np.  Immäi.
—  I)  Ich  beliebe  den  Sati  auf  die  ZDMG. 36.  584  eiwibnte  Enählung  det  Sn.
•  j.  humäyö.tara-  Adj.  'der  gesegnetere, glücklichere':  a^a  zT nS  °racd  jiye.tara/a'> anhama  yäts    spsntahe   mainySul  damqn
'yat  hts  hitmayaca  .  .  cina&amatdt  "so wollen  wir  denn  noch  gesegneter  und erfolgreicher  sein  (werden) . ."  Vr.  /2.  4;  — di:a  zT  nS  'ra  at»h9n  kuittaya  (sd.)  atta däman  *d^3maide  Vr.  J2. 4.
Pü,':  iiän  amäi  hu/ramänlar  em,  erl.:  man xüpiar  hart  bavil.  —  ■)  Vgl.  Y.  41.  3.
•  g.  hu-mMatay-"'  f.  'gute  Verkündigung, Botschaft':  nöit  matdä  anastryS  davqsana 'ISii  baxStS  "der  Nichtbauer  wird,  o  M., auch  wenn  er  sich  danach  drängt,  keinen Teil  haben  an  der  guten  Botschaft"  Y. 31. 10".
Zum  V.  «war-;  %  S7.  —  Vgl.  mir>lS  Inf.  — ai.  sntflay-  f.  'Erinnerung,  traditioneller  Aus- ipnich'.  —  Pü. :  tit  Shrma^  5  H  i  avaräiär .  .  pa  an  i  xüp  östnuriimh  baiet.  —  >)  Darf man  den  EN.  KtaiiapTAtir^  heranziehen?  S. Bthl.  LC.  i8g6.  160;  doch  vgl.  auch  KZ. 36.  571.  -  >)  iSt.  vgl,  Y.  47-  5.
•  g,  hu-mazdar-  m.  'der  (etwas)  gut,  recht im  Gedächtnis  behält,  (es)  gut  merkt': °zdrä  aiä  yaä'^  yä  raocibl!  dansatä urvätä  "und  von  der  Wonne,  die  von dem,  der  es"  sich  gut  merkt,  (zugleich) mit  dem  ..^rä^',  die  (zugleich)  mit  dem  Licht- raum erschaut  werden  wird"  Y._J0.  i.
Zum  V.  mqsi/ä-.  —  ai.  vgl.  maniihätär-  m. ; s.  dazu  Bthl.  AF.  a.  118.  —  Pü.:  humtnilär.
•  j.  hu-mizda-  Adj.  (fem.  'da-)  'schönen, guten  Lohn  bringend ,  eintragend' :  tä (nämL^aSi)  nS  buyan  °da  aijniidä  a^.-
dby  Google
i835
humna-
huraoJIa-
1836  :
miJi/ä  farffuim/li  amtke  "diese  {Gahäi) mOgeo  uns  guten  Lohn,  reichen  Lohn, den  Lohn  der  Gerechtigkeit  eintragen  fiir das  künftige  Leben"  Y.  55. 3.
■i.  V£l.  sumVhä-  m-  E>^.  —  Pü. :  kumitd.
•  j.  humna-  m.  —  ?  — :  ■» Fr.  9.  a.
G^Qi  uDskberes  Wort,  daher  jeder  Vergleich mililich.
•  j,  hu-yaona-  Adj.  (fem.  'nä-)  'an  guter Stätte  stehend' './rava$ays..yh  'na  p3r3%u.- yaeith  \tis.  39,
Vgl.  ifäyaima;
•  j.  'hu-yazata-  Adj.  {fem.  '/J-)  'wohl, hoch  zu  verehren':  aslm  vaimhlm . .  •tarn Yt  ly.i.
Vgl.  'iKfosata-  £N.
•  j.  'hu'yazata-  m.  £N.  eines  Gläubigen: •tatahe  asaonö  Yt  13. 117.
Vgl.  liu/azata-.
•  j.  bu-yaita-  Adj.  i)  wohl  gebetet': tarn  yatäi  sumnvata  yasna  tarn  yazJi  'ta yasna'i  ..taohräbyö  Yti-p.  3)  'wohl verehrt'  (nur  Ableit.).
.\bleil.  —  li.  sv)i/a-  Adj. —  Npü.:  ba  an  nii yaita  yimin.  —  »)  Vgl.  RV.  /.   162.  5.
•  j  huyaäta'tara- ''  Adj.  (fem.  °rJ-)  'der besser  verehrte':  ana  buyä  'latara  "so mögest  du  noch  besser  verehrt  werden"
Npii. :  an  biid  nii  yaiiJn,  —  ■)  Ny.  4.  9  iteht dafür  huyailara;  vgL  %  lOO  a,  306  'Haplo- logie'.
•  j.  hu-yaStay-  f.  'gutes  Opfern,  Weihen': alyelfica  'yestiia  Au/rahrfti(,%A.)ca  zao- %ranqm  Y,  68.  9.  3)  'gute  Verehrung': kS  *yesti  ks  dulyt^li  mam  xT  matnyete ya%at»m  "wer  meint,  dass  ich  mit  guter, wer  dass  ich  mit  schlechter  Verehrung zu  verehren  sei?"  Yt./o.  108;  —  'yest't tava  aAuräne  sfnnäini  Y.  68. 14.
ai.  vgl,  niiffaji-  f.  —  Pü.:  xüp  yeuisniA.
•  j.  huyä)Tia-  Adj,  'das  Lager  teilend, Lager-,  Stubengenosse';  vlsaitivä  asti miirS  aniar»  ha!a  suptioarynga  (sd.)  .  , pama.sa%wa  autark  'na  (AD.)  \t  10.116.
El  ?  —  ')  Sva.  hämö.giltiv-.
•  j.  huyäirya-  Adj.  (fem.  'yä-)  a)  'gutes Jahr,  gute  Ernte  habend':  kaaa  airys daitihävS  'ya  bavanti  YtÄ36;  —  'ya avi  dairihus  Yt.<?.  9.  b)  'gutes  Jahr, gute  Ernte  verschaffendgbewirkend':  masya ..  'ya    äpd    barmtil    Yt.  A*.  40;  —  pairi-
kayäi  .  .  yä  duiyatrya  yqm  mafyska  «a duivacanhs  'yqm  nqma  aojaite  Yt  6. 51.  A)  als  neuti.  Subst  'Gutjahr,  gute
Erntejahr':  tütrxm  , .  ytm  . .  ^>^(IS.)ä daiAhave  uzjasmtfm  duiyäiryJ{sd.)cä  Vl Ä36.
Ableit  aas  *hu-yär-  n. j.  Au.vaxJ'  N.  46' :  lies  iä  varl".
•  j.  hu.vaxJia-  ra,  'gutes  Wachstum,  G^ deihen':  'lai  frm>mnahe  V.  4,2  Gl.
PiL;  fa  httvaxs.
•  p.  "u'vaxätra-"  m.  EN.  eines  medischec Königs,  KyiXAie.i'' i /ravartis  nSma'  Uta- i/a*  .  ,  aiaÄa*  adam  xsa^rit^  amij 'rahyä  taumäya  Bh.s.s;  4.3,  Bh.  e;  — I  cih'c^taxmt^  namd"  asagartiyt^  .. dhaAer  adam  xsahrita^  atnty  'rakf9 taumayS  Bh.  4.  3 ;  2,  1 4,  Bh.  g.
Eig.  *»on  gulcm  Wuchi';  *vaxstra-  n-,  IHD V.  ifflji-.  —  ')  Andre  lesen  'xiaiar",  'jcialr»-. 'xilara-,   s.  iB.  JusTI  NB.  140  (der    in   dem
ferner  Fov  KZ.  j/.  49J-  —  '>  VgL  Jm GltPh.  2.  410.  Ein  Versuch,  die  per»,  nod die   griech.   Namensfonn  lu  TCrmitteln,   bej
WSCHULIZ   KZ,  _JJ.   3J3.
p.  *«i'flya.,  '•uvajiya-:  s.  Sp.   1846  f.
•  p.  naiy  "saiaurim  naty  •»  "huvatam'' züra*  (sd.)  akunavam  Bh.  4.13.
Vgl.  lu  ziirah:  —  ')  So  die  Lesung  derN.t., die  aber  unmöglich  ist,  da  k  vor  »  nicht  ge- schrieben wird;  IF.  12.   129.
•  j. yä  aridulai  *apailital  *äjayaurva  (sii yä  "hu.varashana  N.  54.
fa.:  e  tc  andar  an  i  fa  var  i  a/e(. .);  dulieli also  wobi  zu  'iKiraA-.  Die  Lesung  yöAu  vtr" gibt  auch  keinen  Sinn.
p.  ^laiä':  1.  unter  hv',  Sp.  1853  f.
•  j.  huvira-  Adj.  (fem.  'rä-):  s.  unter 'livira:
•  j.  hu-rao5a-  Adj.  (fem.  -oa-)  'von  gutem äusseren  Ansehen,  von  schönen  Formen'; a)  von  a)  Menschen  und  ß)  Göttern;  n a):  caräili  -sa  (NSf.)  V._y.  34;  ig.  30;  — kainJnö  kthrpa  'oayi  H,  2.  9,  Yt5.  64;  — '})0  ¥.3  a.  zu  ß):  sraosS  afys  "Wf  V. z^.  40;  —  srao/a  asya  'oa  Y.  57.  35,  JÖ, 65.12,  Y. 18.2a,  31;  Y.2.7,  57.3,  V./9 15,  Az.6,  Vd.i2;  —  nairlm/a  saakM •&/«  Y.37,3,  Vyt40;  —  amaktla  hutääahi 'oaie  Y.1.6;  2.6,  Yt/47;  —  astm  ■■ 'äara  Y,2.r4,  Yt77.i;  —  andvTm  ..'if* Yt.5.  15;  —  drvaspqm  ..  'lam  Vtp. 2.  b)  sonst:  ianüm  ya  mf  valnaüe 'f^ Y.  io.  14;  —  yetihä  (sd.)  k>Arj>s  •oayä  Yt
dbyGoot^Ie
'837
*hiira(M!ay-
10.  go;    —    zrayanhö  amavatS  'SaAe   Yt
Vgl.  'Ypoi-rit.  —  Pu.;  Aurusl(ai\  erl.:  ^gön xüpih  pa  jTöU  "gemeint  ist  Schönheit  hinsicht- lich des  Fleisches";  s,  dazu  liKmoSoj'.,  Autaita-, hukihrp-.
•  j.  *hu-rao8ay-'>  f.  'gutes  äusseres  An- sehen'; nSil  astS  *hutastlm  nsit  tanvS *'raoiljm ''  "nicht  guten  Knochenbau  noch schöne  Leibesform"  P.  4?.
Zum  V.  'raad-;  vgl,  AuraJi-i-').  —  Pu,:  /ab  (' hurust.  —  ')  Hds.  huradim.  —  *)  huraöiay- könnle  direkte  Neubildung  zum  Adj.  huracia- sein,  nach  dem  Muster  Imtasla- -.  hulastay-.
•  j.  hu-rao8ah-  Adj.  (auch  fem.)  sva. huraoaa-  (sd.) :  y>nS  ,  ,  'hatshB  (APf.)  Vr. 2.7.
ai.  rshas-  n.   'Erhebung'.  —  Pü.:  hurust.
•  j.  hurä-  f.  Name  eines  alkoholischen Getränks,  'Milchwein",  Kumys"':  dahmö •rqm  :faraiH  ma%d  *aspya.payar3hs  (sd.) "ein  D.  trinkt  H.  -  (d.  i.)  der  Wein  der (aus)  Pferdemilch  -"  N._jO;  —  -rayäsät  aha  . aiiavatJ  daiäyai  ä  dit  franharayat  sraolät dqhista  .  .  "er  soll  vom  Milchwein  ein hinreichend  Mass  spenden,  er  soll  es trinken  lassen  die  . ."  A.^.  4;  —  duye navaiti  narqm ..  västryaSa  gSul  vä  s^an- %ahe  z'il  'rayä  vä  *>na6Sus  vä  "..soll  er laben  mit  Fleischspeise  oder  mit  Milch- oder Beerenwein"  V.  74. 17.
Zum  V.  'hav-^).  —  ai.  sürä-  f.]),  mp.  (PÜ.) Aur.  —  Pü.  (2U  V.):  Aur,  (zu  A.  und  H.): iaiar.—  0  Wein  aus  Pferdemilch  bereiten), im  Cegeniaiz  zu  rnaiav-  (sd.).  Das  gebt  aus der  etlaulernden  Glosse  maiä  aifiya.payasAö (sd.)  klar  hervor;  s.  schon  ZDMG.  S7-  549- Vgl.  noch  No.  3.  —  •>  Ganz  verfehlt  DsT. £tlr.  2.  331,  —  3)  Worüber  zuletzt  EKüHN KZ.  SS-  3'3-  Stoffliche  Gleichheit  der  ai. sürä'  und  der  ür.  Aiirä-  anzunehmen,  ist  selbst- verständlich nicht  nötig.  —  4)  Der  Kumys der  Kirgisen  enthalt  je  nach  seinem  Alter  1,2 bis  2,0  Prozent  Alkohol;  5.  Ksuc,  Ersch. Grub  er  Enzykl.
•  j.  *hurä(h'a-''  Adj.  'mit  schönem  Wagen- zeug versehen':  hvaspS  aki  '%vS  Yl. 10. 76.
Statt  '■%iva-  geschr.,  %26S.  17  {daher  f,  nicht Kl,  S  ^^S.  38).  —  Ableit.  mit  va-'''i  aus  *hu- tä%ay  m.  (Ableit.  aus  ra%a-).  —  ')  NA.  hat Aurä%yö,  eine  kritisch  wertlose  Variante;  man erwartete  auch  Epenthese;  '%v^  bieten  F  1, jiousw.  31.  —  '1  Oder  ist  •Si'e  Vok.Sing. aus -iiiivi«;-?  Schwerlich.—  3)  Für  K  40  gibt Gdm.  zwei  verschiedene  Lesungen  anl
•  j.  hu.irixtam  Absol.'*  'mit  gutem  Frei-, Schiessenlassen',  in  Verbindung  mit  dem
huzantav-  1838
V.  rarf-*':  västm  ..yat  dim  dämsil  ypa- mata  °t3m . .  irinaxti  "den  Wagen . .,  dahin wohin  ihn  DU.  in  mächtigem  Schuss  dahin- schiessen  lässt"  Yt.  10. 68.
Zum  V.  rcük:  —  ')  zBild.  s.  airut/m.  — =)  Vgl.  Aviulim  und  Zubaty  IF.  j.   135.
•  j.  hu-ruOroan-  n,  'schönes  Gewächs': staomi  s»nS  yd^a  raöhahe  kubaemÜ  .  . Uta  mazda  °ma  ". .  und  als  M.s  schönes Gewächs"  Y.  10. 4.
Pü. ;  vat  ilön  mos  (für  maidä)  ärviiJit  'und  so ist  dir  grosses  Wachstum'.
•  j.  hurunya-  n.  'Seelenfriede,  Seelen- seligkeil':  dazdi  aAmäitm  .,  haesravaiahitn 'nlmca  Vt  10.  33;  —  haosravashe  'nyätla Y.68.2;  —  aAmäkfUt  havaiahäica .  .'nyäica yat  saolyantqm  Vr.5.  i.
Ableit.  aus  *Aa-rvan-\  -run-  Adj.;  eig.  'Zu- stand dessen,  des  Seele  gut  ist'.  —  PB.:  Au-
'•  j.hu-sasta-'*Adj.  (fem, '/J-) 'gut  bekannt
I  gegeben,    gehörig  verkündet':    saauhasca \paiti  °taya  . .  amuyamnaya  . .  avarwnnayä Yty.133. I      ')   So   NA.   nach   Mf3;    aber  F  I,  J  10  usw.
•  j.  hu-star9ta-  Adj.  'schön  gebreitet, gespreitet*:  a/sqm  gätava  kistmte  *ta  Yt. //.  9.
•  j,  hu-sravah-  Adj.  'der  einen  guten Ruf  hat;  berühmt'.
Ableit.  (Äflfljr".).  —  ai.  siärmias-  Adj.
•  j.  yä  aAmäf{Sp.  297  m.)  staota  yasnya srävaymi  ahummca  vairttn  trävaygni aamca  vahislim  "husraväni"  afiasca vattuhil  yaoidä^äne  Ny.  1^.  8.
I)  Mit  vielen  Varianten.  Man  verlangt  die t.  Sing.  Konj.  des  Verbs,  das  vom  Aufsagen des  ^ifiR- Gebets  gebraucht  wird,  s.  Sp.  1593  f., etwa  upastaväni.  GdN.s  Vorschlag  (in  der  NA.),
•  j.  hu-zaena-  Adj,  'mit  schönen,  guten Waffen';  mihnm . .  'n^m  . .  vn-Hsravastittum
zayanqm  V. 79. 15;  z8.
•  j,  hu-zantav-  1)  f.  '(rechtes  Kennen- lernen sva.)  rechtes  Inne-,  Teilhaftigwerden'; *tsus  paiti  aparaya  *vyär3^yaya  vakistahe ankSui  "um  künftiges  rechtes  TeÜhaflig- werden,  um  tmbesirittenes,  des  besten Lebens"  Yt.  13.  134.  2)  Adj.  sva. kusSntav  (nur  Ableit).
AbleiL  {haozi^wa-).  —  Vgl.  AusSnlav-. j.  hiaarilayä  H,  3.  9;  lies  uzarsf.
db,Google
»839
huzämay-
huäkö.zsmö.tsma-
1840
•  j.  hu-zämay-  m.  'gute,  leichte  Geburt': %wam  earaitif  zitanäilis  jaityänte  •mim Yt5.87.
AbleiL  —  Zum  V.  'mb-  (^tä-may-).
•  j.  huzämit-  Adj.  (auch  fem.)  'leicht gebärend';  ärthqm  (näml.  fravasmqm) raya  .  .  häirilli  pu&ri  vgrmvainti  .  .  *tB (NPf.)  srsuw«/!  Ytij.  15;  —  aiyävfm.. yS  . .  hairini  US  (APf.)  dalaiti  Y.  65.  a.
Ableit  «US  Auzämayi  %  i8i.  —  Pü.  {lu  Y.): ke  .  ,  husäyiltüA  dähil.
•  g.  hu-zäntav-  Adj.  'der  gute  Kunde hat  von  -,  wohlvertraut  ist  mit  -'  (Gea); yS  dalnqm  vehü  *jar>st3  (sd.)  mananhä armaüsÜ  kasht  asä  -tu!  ". .  weil  er  durch ASa  mit  dem  rechten  Deoken  wohlvertraut ist"  V.  4g.  5.  a)  absolut  'der  die  gute, rechte  Kunde  in  Glaubenssachen  hat, wissend"*:  andrS '^wavas {sA.)  °iusi  sf^nis matdä  Y.  4.^.  y,  —  yf--  dritä  ayantsm  \ urvätsi!  {%A.)  vä  Uui  .  .  Y.  4^.  5.  j
Ableil.  (s.  Amiiqispa-).  —  Vgl.  AÜtanlan:  —  I Pa.  (zu  Y.  43):  xüp  inäsai,  (sonst):  xüp  sitä- , latTA.  —  I)  Vgl.  iBed.  BB.  8.  213,  IF.  7. 224.
•  j.  huSata-  Adj.  'getrocknet,  trocken': alsmanqmSt  .  .  'tarn  (GP.)  pairjltanqm vazyail  A.J.  5;  V.  14.  2.
PPfP.  lum  V.  haos-i-).  —  PÖ.:  huik.  —  ')  Die Bildung  ist  ungewöhnlich.  Sie  scheint  ein Praei.  3  huia-  varäusiuseticn;  s.  Sp.  501  No.  d,
•  j.  hu-§ayana-  Adj.  'gutes  Wohnen  ge- während*: tistrlm  .  .  rämajayangm  'ti>m Yt.S.2.  a)  mit  Dat.  comm.:  mUnm räma/ayansm  'mm  atryabyS  dai^hubyS Yt.  10.  4.
Npü.;  nXk  sädKi).
•  g.  hu-ääna-  Adj.  'guten  Verdienst,  Lohn verschaffend':  tattiksi  "mm  aaAat"deikR das  wird  ihm  guten  Lohn  verschaffen'' V.5JS
•/uBo-  m.,  lum  V.  iait:  —  ai,  lufäna-  Adj, 'leicht  lu  erwerben'.  —  Pü. :  humäniinJA.
•  g.  hu-iöiS^man-  n,  'gute  Wohnung, gutes  Wohnen':  As  zl  nS  "mä  hä  n5 iitayüitiin  dät  trvTslm  vatahtui  mananhs binxai  (sd.)  "sie  (näm!.  Ärm^  schenke uns  gutes  Wohnen,  sie  uns  Bestand  und Kraft  .  ."  Y.  48. 6.
Zum  V.  iiy-;  aus  ar.  *xhilman-  n.;  vgl.  ai. kllma-  m.  'Wohnsiti'  und  gr.  Xarr/iB  :  Xsi/ig(; I.  noch  '/raa%man-,  vä%man-,  väri%man-.  — Pü.:  ^ärih.
•  j.  hu-äit-  Adj.  'gutes  Wohnen  bietend, wo,  bei  dem  es  sich  gut  wohnen  lässt':
'ydha  ^w3  (näml.  mikrim)  *aiwisayama  . . 'ttm  b?rffmya.saS3m  (sd.)  Yt.iO.77. ■AV-  f.,  lum  V.  iay-.  —  ai.  'kfU-  Adj.
•  j-,  g.  hu-sitay-  f.  i)  im  gAw.;  a)  'gutes Wohnen':  kads  .  .  ärmaitii  jintat  (Sp. 494  m.)  xsdhrä  'Mtis'''  västravaiii  Y. 4S.11;  — yä  'I^lli'^  rämqm(sd-)cä  dät Y.  25.  10.  b)  'gute  Wohnung,  Wohn^ statf :  at  asistä  yaojanis  (sd.)  ä  'sitsil vaiahJui  manaahö  masdä  asahyacä  Y. 30.  10.  a)  im  jAw.  mit  ysirya-  Adj. 'das  ganze  Jahr  hindurch  währendes  gutes
,  Wohnen'  als  Gottheit:  asäunqm  .  .  /ra- :  vasayS . .  ynas^a  vTrB.vakwä  . .  yairyqmca '"lim  Y.  2. 6;  1.6;  —  haurvatais  raiiwS \yäiryayasca  'sttsii' sariüaHbyS  asahe  ratuiyS iS.7.6;2.6.         IS.  -H  als  Inf.  sbes.
ai.  iuifilay-  l.  —  Pu. ;  humänisrü/i,  (zu  3} : sälän  niänisnVi  —  Sü.:  samvatsaränamca  s«j> vaiüh  -,  erl.;  ia  andar  sil  pa  ftärdnlh  i  vek täyit  mäHÜtaa.  —  ')  iSchr.  s.  S  »5*-  9-
•  j.  hu-§iti  Inf.  'gut  zu  wohnen':  '«ft' ramS.siti  danyS.Iiti  (sd.)  ite  vXse  a/rlnaiiä Y.6K14;  14;  ät.  V.rp.2  Pü.
Vgl.  husilay-,  —  Pü.;  AumänilniA.
•  j.  hugka-,  p.  Niäka-  i)  Adj.  'trocken, ausgetrocknet':  'i^m  alsmim  Y.  7/.  8;  — aHavat  'kanam  alsmanqm  aSavat  nafia- nqm  V.  7. 31;  —  vtlastiJrap  yat  (Sp. 1252  u.)  'kanqm  (als  Obj.)  ..  aitiha  s^mS nidaüyqn  "sie  sollen  in  der  Länge  einer V.  vom  trockenen  (Holz) , .  auf  der  Erde hier  niederlegen"  V,  7. 29;  3c,  33,  34;  — 'kanqm  yavanqm  V.  7.  35;  —  'hm  p>htn raicayat  Ytj.  78;  77;  —  aSavat  apat haca  nilbarayjn  °ke  z)me  nidathya»  "so- viel sollen  sie  aus  dem  Wasser  heraus-
I  holen  und  im  Trockenen,  auf  dem  Land ■  niederlegen"  V,  6.  »9;  31.  3)  n.  *Fesl- lland'":  yauna  (sd.)  tyaiy  'kahya  utä ^  tyaiy  *drayaAya  D.5.  2,  [V.Ä34:  lies '  kiiku.]
KompA,,  E.   —    Zum  V.  iaos-.  —   np.  xuit;
ai.  vgl.  iu,iä.  Adj.  [s  sA-  —  Pü-;  ^^-  r
')  S.  dam  lat  rtrra  geg.  goL  Jmursas  'fjipV^-
•  j.  huSkö.zam-  1)  f.  'trockene  Erde'; I  istyehe  v3  sarstvahe  va  'amanam ''  vä \pqsnam    "Staub    von  . ,  trockenen    Etd-
I  (ärt)en"  V,  <S'.  8,  2)  Adj.  'trockenenÜg" (nur  Ableit.).
I       Ableit.  —  Pü.!  husk  zamlk.  —   >)  Them.
:  •  j.  huäkö.zamö.tama-  Adj.  'wo  die lErdei  der  Erdboden  am  trockensten  ist':
dby  Google
i84i
"huS.psrssö
'hya-  I
1S42
j/at  anhat  at^ha  umS  vt.äpSJ>mmt{%^la
..  •»»,«.  V.j.,s;5.46. Superl.  aus  kHikS.sam-,  itn  Anschluss  an  den AS,  gebildet.  —  Pü. :  hasktamiktum.
```


## [2026-09-14T03:11:25.284Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in 'hu-ci' 'hu-vae' 'hu-niv' 'huniv' 'hu-x' 'hu-jas' 'hu-p' 'haoiyan' 'haoSyan' 'huparj' 'hu-gnu' 'hu-snu' 'hu-Snu'; do echo \"--- $w\"; grep -n -- \"$w\" BRT.txt | head -6; done",
 "description": "Grep more Avestan hu- compounds in Bartholomae"
}
```


### [2026-09-14T03:11:26.377Z] TOOL RESULT

```
--- hu-ci
30193:•  j.  hu-ci3ra-  Adj.  (fem.  'rä-)  i)  'von guter  Abstammung,  Herkunft':  nfm!  *nm .  .  yeAhl  n/maahs  ciinm  Aumahmcä AoxDmcä  hvarsUmcä  Y.^S.i.  t)  'des Anblick  gut  ist,  schön*:  äuiäia  aki  'ra (NSf.)  Yt. /-.  15.
30197:•  g.  hu-cistay-  f.  'die  gute  Lehre':  AvS' tsng  frd^h  pa%m}/tg  (sd.)  'tdis  *carat  Y. 46. 4.  a)  'Inhalt  der  guten  Lehre,  was sie  enthält,  insbes.  was  sie  in  Aussicht stellt,  verheisst':  tai  .  .  vairJm  (näml. mXid^m)  astvaiti  ustänäi  (sd.)  data  .  . xsmäkqm  'tim  ahurä  xrafSui  asä  fraäS v>nz7nä  "diesen  köstlichen  (Lohn) . .  werdet ihr  . .  verschaffen  . .:  was  eure  gute  Lehre verheisst,  o  Ah.,  die  der  Weisheit,  die durch  Äsa  die  Gemeinden  fördert"  Y. 34.\it.
--- hu-vae
--- hu-niv
--- huniv
23256:!  •  j.  vazra-  m.  'Keule';  insbes.  Ilaukeule' " : yailqm    zayanqm    raäsSiili  .  .  '^ritys    'rS V.  J4.9;  —  •rif  Aunivix/if{sd.)  Ytlj.jx; 10.133;  —   'ra^J  (NP.)  .  .  hunivixia  ydi niyraire  saraiu  YL 10. 40;  —  tisit  kanta ndii  'ra  Ytl.  18;  —  apayüxtai  (sd.)  paiti 'rät  V.iS.^o,  36;  —  ist  Mi^rai  Haupt- waffe'': mihrahe'nm  ..satafitän^m  sats.- danm  ß-avafy»m  vjrd.nyancim  xar^i/(sd.) ayanhB frakixhm  amavats^tantiyehe  ama- vattmum  tayanqm  Yt.  10. 132 ;  96,  6. 5. ai.  vijta'  m. ;  np.  jk«.  —  Pü. :  vaa-.  —  i)  Im Gegens.  tu  gaiä-;   sd.  —  »1  Wie  der  väjra^ die  des  Indra.
30368:•  j.  hu-fra'uharSta-  Adj.  'gut  losgelassen  haiaya  'tayh  Vr.  i.  4;  2. 6;  —  staotanam sva.  gut  in  Gang  gebracht,  geschwungen'»:  ■  y^nyanam  handätanam  'tanam  Vr.  /.  3/  3. kantö  -tS  .  .   vasrS  hunivixtS  Yt.  13.  7  2.  PQ, :  /üp/rä^yasiin  't,  -yaiUnJA.  —  ■)  iT.  an  p*
--- hu-x
30170:•  j.,  g.  hu-xratav-  Adj.  'des  Einsicht  gut ist,  ems  ich  tsvoll':  haomö ..  •tus\.g,  23;  — fratanmät  lg  (näml.  haomahe)  havamm  . . 'tvSiyS.)  Y.10.2;  3; —  vastryö ^ao^anäii snsvS  hqs  'tul  ntmanhä  (Sp.  1068  u.)  Y.
30172:•  j.,  g.  hu-xSaSra-  Adj.  'der  gute  Herr- schaft führt,  guierHenscher':  äims  mazdä •rä  daiva  aahars  "sind  denn  wohl  die Daiva  gute  Herrscher  gewesen?"  \.44. jo'l;  —  'ra  xsintqm  fSp.  551  m,)  mS  nS^ *duhxiahr3  xSintä  Y.4S.  s;  —  -rasia  ni na  vä  nSirJ  vä  xsaltä  "ein  guter  Herrscher möge  über  uns  -  Mann  oder  Weib  -  die Herrschaft  führen"  Y.  41.  3;  —  'raii j}mrqm  (sd.)  .  .  rämqmcä  Sil  dadätü  Y. 55.  S.  a)  bes.  von  AhM.  und  den AmSp.:  ahuräi  mazdai ..yat  'rät  Vr.ii.x; —  am»ia  spsntä  'rä  hutataks  (Stverz.) yasamaide  Y.jj.  j ;  usw.  -  'ra  (NP,,  AP.),
30179:•  j.  'hu-xsnaoOra-  Adj.  'leicht  befriedigt, leicht  zufrieden  zu  stellen*:  •rj(NSm,,  näml. ist  der  Hund)  yc^a  ahrava  AväzSrd  (sd.) yaha  ährazia  V.  J_J.  45.
30181:•  j.  *hu-xönaoi)Ta-  n.  'gutes  Knie'": ustrahe  . .  yS  kafim  aipijpayeiü  spaHtittm upa  vaylatum  '^re  (AD.)  Aupaitisläiu'* "des  Kamel(hengst)s,  der  weisslichen Schaum  auf  seinen  Kopf  zurückwirft, auf  seine  guten  Knie  und  Beine"-  Yt 14.  iZ'^.
30188:•  j.  hu-xsnuta-  Adj.  (fem.  •«•)  'gutge- schärft, scharfgespitzt':  aritayasat  , ,  'ia YtJO.  39;   —  ar^tSis  -taya  Yl. /O.  24.
--- hu-jas
--- hu-p
12701:•  j.  daÜhu-patay-')  m-  'Herr,  Gebieter einer  Provioz,  eines  Landes,  Landesherr'; i)  im  eig.  Sinn:  a!%rapatay3  .  .  *°tayS Aog.59;  —  va%ayanö  'paitts  V.  ig.  6 Yt.  15.  31;  —  yim  yazmte  "tayö  arjzahe ttva.jaspras  Yl  JO.  8;  —  ahurö  ^sästrfnqm •paiHl  Yt.  J^  37;  —  akuranhS  'tayS pu%ränhs  'paitinqm  Yt,  5. 8  5 ;  —  ä/rlitami tava  nara  ••paiti(VS.)Az.i;  A.i.8.  a)  mit Gen.  aus  ^Xyav,  daiAAav-.  nmanaAe  va KMätuspaitil  .  .  daijihfui  va  "paitis  Yt 10.18;  83,  l6.\%  VyL46';  —  dai^hsus yatffiM  Vr.J.  3,  V.  7.41,5.37;  —  daiMiuf •mVV.iO.S,  Y.y.  I,  Vyl-iö;  —  liairihSus 'tSe  Yt  /o.  17;  —  da/ryunam  'pattil (AP.)  Yt  /O.  18;  —  äaiAhyui  'painm*> nSirikqm  "die  Frau  ebes  Landesherrn" V.  7,  4a.  2)    von   Göttern;    a)    von
30265:•  j.  hu-paitiStäna-  n.  'gutes  Bein':  ustrS
30287:n  gaospmta..*gaohula''^  (:y%.)Y.2i.i;Y.  .  j.  hu-pairi'tan- Adj. '(sich)  wohl  hcrum-
30293:'da  Y.  12.  7:  —  gJu/  'iaukö  urvamm  Y.  j  •  j.  hu-pairi'spl-  Adj.  "ringsum  wohl  ge- JÖ'.  4,  20".  4,  S.  2. 14;  FrW.  Ö.  1;  —  gsusca  deihend'(?);  Aupatritä  nama  ahmi  'sph •däiilsS  gay€hyäiä  mardinS  Y. /j.  7.  nama  ahmt  (närol.  vayus)  Yt/5. 46.
30300:•  j,  hu-pairt§ta-  Adj.  'wohl,  gut  ausge- !  Abstammung':   ywii  Aubayi  '/nrif'^  Vr.
30304:Pü. :  mkirU. •  j.  hu-parana-  Adj,  'wohlbeflügelt':  th dim  ava  nifrävaymte  mqnaym  ahe  ydha nH  jmrr/S  'nS  ". .,  gerade  als  ob  man (es)  ein  wohlgeflügelter  Vogel  wäre"  Yt 13. 70.
--- haoiyan
--- haoSyan
15384:•  j.  'para-Sita-  Adj.  Ehrentitel  des Fürsten    Haolyaaka:    haoSyanhö    'td   Yt
28795:haoSyanha-
--- huparj
--- hu-gnu
--- hu-snu
--- hu-Snu
```


## [2026-09-14T03:11:57.277Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== haosyanha\"; sed -n '28780,28810p' BRT.txt; echo \"=== xsnu\"; grep -n -E 'xinav-|x§nav|xsnav|xSnav|xsnu-|zufriedenstell' BRT.txt | head -10",
 "description": "Bartholomae haošyaŋha and xšnav"
}
```


### [2026-09-14T03:11:57.348Z] TOOL RESULT

```
=== haosyanha
•  j,  *haoyö.t»mäi "  Adv.  'zu  äusserst links  von  — '  (Gen.):  'mäi  dansman  paiü. barsil  .  .  *dasinl!.fym3i  .  .  N.  70,
DS.  aus  "AatySMima..  —  Pü.:  häylum.  —  1)  Hd», haBUm',  t.  aber  Pü.
j.  haoyi  Y.  ti.   I :  s.  hava-.
•  j.  haosafnaena-  Adj.  (fem.  °nr-)  'stäh- lern,   atis    Stahl':    hatanrsm    cakulanqm •naitiqm  (GP.)  Yt  JO.  130;   —  ytn  a> zannärmi  (sd.)  ,  .  'nalnif  (NSf.)    V.  j. 74i.
KorapA.  —  Ableil.  aus  •iowa/na-»).  —  P pSlätacU/n  'itählem'  (s.  daiu  Hbil  AGr. 231).  —  ')  S.  das  folg.  Wort,
•  j.  haosafnaenö.saepa-  Adj.  'wo(rin) Stählernes,  Stahl  geschweisst  wuxl':  pisrat kaca  'fäl  V.  *.  90.
fi.:  filäwai  *3leH(f)iar.  —  >)  Man  verlangt«
•  ').  haosrao-gaona-  Adj.  'von  der  Art des  Haosravah' ^):    'nS  hudagrtS  Yt.^.  9.
Statt  'srau5.g',  %  a68.  36.     Garn  unsicher.
•  j.  haosravaDha-  n.  'guter  Leumund, Ruf;  Ruhm' :  da%di  ahmäksm  . .  havanhum asavaslftnca  °nhtm  hurutitmca  Yt;o.  33 —  havanhe  asavastäica  'vatiht  (DS.) iurunyaua  "V.OS.t;  —  tanvaica  *'^h»m uruiMlca  darr/im  havanh»m  F.  ^  h ; aheca  anhius  dariyäi'vaAhai  manahyeheca arahsu^  dar?yai  havaiihai  VyL_j2;  — mürvrrt .  .yeAhe  vohu  °nA)m  vatvuAi  ktrsß Yl/o.  60;  —  tiitrlm  ..  ''yahmai  kaca b>r>zät  •nfutn  apqm  naf^rat  haca  ct&nm "T. ..,  von  dem  her,  dem  erhabenen,  der Ruhm  stammt,  .  ."  YL  8. 4;  —  *'va^Ae'> F.  24.
Ableit.  —  Ableit  au*  *hustaoiik;  %  100  a.  3 ; ai.  Tgl.  sauhavasi-  n.  —  Pn.:  hustavlh.  —  •>  S. /rada%a-  No.  1.  —  ')  Hds.  haau.tr'.
•  j,  haosravaahan-  Adj.'dergutenRuf  hat, berühmt':  yim  (näml.  v»r?hrayn>m)  vasanie ahuratjks  .  .  ahairyaTphS  .  .  •i»Aam  (NP.)
Yt.  14- 39-
Ableit.  aas  kaostavanho'.  —  Npfi.;  täin^ai.
•  j.  haosravaahana-"  patr.  Adj.   'von
haoSyanha-
1738
ffaosravah  stammend,  dessen  Nachkomme' : axrürahe  'nahe  Yty.  137.
AbleiL  aat  ^hamravah:    —    1)   I^sung  nicht
sicher.     F  i  o.  a. :  'vaahaki.
•  j.  'haosravah-  m.  Name  einer  Bucht des  VourukaSa*^:  aSa  hau  apayzärS  bvai srayanhö  vouru.kafahe  vairis'yS  'vä  nqma Yt.  15.  56;  —  vairim  'varthsm  S.a.  9;  — vardis  'vanhahe'^  Ny.5.  5.
*)  Nach  Bd.  33.  S  ist  sie  50  Porasangen  vom See  CowoiW  (id.)  enlfemt;  s.  «her  »ST.  ZA. 3.  631.
Ableit.  Bui  hva-aeak-'i  Oder  für  *httoi^ra- vak-i  —  Vgl.  *haosraoah:  —  ')  Them.
•  j.  'haosravah-  m.  EN.  eines  irani- schen Königs  aus  der  A'uz'aj'dyiiastie:  arsa airyanqm  dahyunam  xJdhrai  hanktr^mH (sd.)  'va  (NS.)  Yt.5.49.  a)  sonst  mit kavay-:  ayaslam  amahrkim  bavdhi  ydkia kava  *'va  Az.7'>;  *Vyt.2'';  —  haomS .  . him  ja^yal . .  dazdi  mL.ya'ia  aam  banda- yeni  . ,  läirTm  fraarasyämm  . .  uta  bastftn upanayeni  bastsm  kavSi^  'vanhahe^  janäi t>m  kava  'va  .  .  pu%rü  iama  (sd.)  syä- var/anäi  Yti).  i7f.;  /p.77,  93,  ^5.32;  — ahurS  kava  'va  Ytig.yj;  —  uynm  ia- valm  i^amiS  .  .  yat  upa^hacat  kavaltn •vanhitn  Yt /p.  73f.;  S. /.  9;  —  yc^a  as>m uzayeni  ha^a  iavlfis 'vamkahe'^  Yt.  15.  2^ ; Ny.  J.  S ;  —  kavsis  kaosravatihs  ai'aonS  Yt J.?-i3a-
Ableit.  —  Vgl.  'ha/!sravnh-.  —  mp.  hesrmi, np.  xuirav;  HORN  GIrPh.  /  b.  30.  (Das  arm. icsi-av  weist    auf  «j'ojr').    —    ■)  Hier   Hds.
•  j.,  g.  haozaS-wa-  n.  'Wohlvcrtrautheit, Wissendheit'  in  Glaubenssachen:  sraoäm .. yeiihe  amaca  vsr3%ra-jnala  'waia  va^yäla avain  atmsa  spttda  Y.57.  33.  a)  mit Gen.  obj.:  tsta  nS  vohB  mat  manai^Aä iixsnu^  (sd.)  .  ,  varshSu!  ajä  'wät  a manaKhS  ".  .  für  unsere  durch  Asa  (er- langte) Wo  hl  Vertrautheit  mit  dem  guten Sinn"  V,  45. 9  ■>,
Ableit,  aus  laaanlav;  Auzinloii:  —  Pü.;  hu- zandaüh;  s.  daiu  HbM.  SBayrAW.  7^/3.655 No.  3  und  DsT.  ZA.  /.  298  No,  30.  —  ')  VgL iSt.  Y.  ^  5.
•  j.  baoS-  V.  'exarescere',  Praes.  3 kaos:  —  PPfP.  husata-  (sbes.).
'austrocknen,  verdorren';  :fai^ai%e  nd daiiMui'  nih/Ual(Sf.  Jxa  o.ya  haoiätaila Yty.  66;  —  •haoSfmna-.
zEL  %.  nnler  anhaalimna:
j.  haoäyasha- m,  EN.  zweier  Gläubiger;
=== xsnu
6226:•  j.  *a^va.xSnav-  Adj.  'den,  die  Gläu- bigen zufrieden  stellend':  ahurahe  ,  .  yai am  *'Xfnu/'*  YtJJ.63.
7119:nicht  am  FUlz. •  j.  ä-xsnav-'>  Adj.  'bis  zum  Knie  reichend, so  gross  dass  es  bis  zum  Knie  reicht'
10904:Zum  V,  xsnav:  —  Vgl.  xinümaine  mil  JScHMIDT Krit.  103.  —  rap.  inöm;  %.  dizu  Hbm.  AGr.  /. 214.  —  Pü,:  inäyünlh,  erl-i  .,  rämUnlar  iarl
10906:•  ).,  g.  'xänav-  V.  'Genüge  haben  an  — , leisten  in  — '.  Praes.  i  xs'nu-,  5  kuxsnu-, 16  (Des.)  cixsfiusa-,  17  (Fut.)  xsnaolya-, 30  (Iter.)  xinävaya-;  J-Aor.  i  xsnaos-, 2  x/tovis:  —  PPfP.  xskuta-'^;  PFP.  xsnao- %wa';  Inf  x/nümaine,  xsnao^räi.  S. noch  ax/nus/a  und  kuxsnBsa.
10927:KompE.  —  Zum  V.  xinav-.  —  VgL  smit-,  — Pü.  (lu  Y.  60) :  tnäycmtJrU ;  (sonst] :  inäxiänh  ■), ?A.:  fri^dhak.  —  >)  Es  wird  btäyl&rth  lu lesen  sein,  vgL  lu  'xinaa%ra-.
10930:KompE.  —  Zum  V.  xinav-,  —  Pü, :    Inäyäii. I       lärJA.
11266:Mit  Int.-Red.  gebildet,  S  i02  II.  4-  Et.?  — ')  Oder  auch  läxinav-,  iJxinafs  nach  J  10;  s. No.  2.  —  »)  Nach  JusTi  NB.  152  (und  And.) identisch  mit  dem  Bd.  jz.  t  genannten  Ur- ahnen Zara%r/stras  Caxinui.
11288:•  g.  cixsnuäa-  Adj.,  PPA.:  s.  ^xinav-.
15769:—  Adhä  atgAsus  vaAistaAyH  'rvlm  käi^S (sd.)  sUidyai  Y.44.1.  3)  'zum  ersten Mal':  taha  ayac/ (sd.)  yäha  'rlm  vTr>m avi  yä  bavaiti  YtÄi4;  14^;  —  'fjm  .. 5«/  mayun  avaJtanaym  . .  bitJtn  . .  %ritlm V.Ä'.37ff,;  7.37.  4)  'erstens':  io  'rJm imam  tarn  mazista  xsnaoma  xsnavayeiti V.>.i,;'i,  7.
19047:—  atat  dim  «•  räsaymte  Yt/0.21;  —  jAw.;  zu  I);  yS  «°  pashUa  hus^afa aß  narym  n°  jainti  V. 5.  8;  9;  —  jvascil\yat  .  .  Y. 57.  17;  N. 24;  —  yS  «•  kahmai tr  bvat  asava  (Sp.  253  o.)  mfsascit  «• '  (Sp.  426  u.)  mikrB.druJqm  ..  ae/S  daÖaiti baxlaiti  vahistahe  argkSus  V.5.  61;  Y\.io.n'  xävarp  Yt /O.  6a;  62';  —  yS  n'  jv5 3o3;  —  mit  Ellipse  der  Kopula:  vlspa*  sraosyqm  tavirgzyeiti  V.  f^.  3;  p.  47,  18.') duivarstä  n'  baote.varsta  FrW.  J.  i ;  — ;  (s.  2),  P.  48;  —  yS  n'  narvm  asavan»m  . . vtrahrarjnS ..n'  narS{y<iV.) yesnyS  vahmy5\xSnaolta  vä  xsnavayeUe  va  P.45;  —  ^'"«
```


## [2026-09-14T03:11:59.293Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT Ufratu\"; grep -n -i -E 'ufratu|Euphrates' KNT_full.txt | head -20; echo \"=== BRT p9r9tu\"; grep -n -E \"p3r3tu-|parstu-|'Furt'|Furt,\" BRT.txt | head -10",
 "description": "Kent on Ufrātu / Euphrates"
}
```


### [2026-09-14T03:11:59.387Z] TOOL RESULT

```
=== KNT Ufratu
4872:Ufrütu- ‘Euphrates’, Nadifaba?ra ‘Nidintu-Bel’, 
5016:(Elamite), Nadztabaira (Semitic), Ufratu- 'Eu- 
6015:e.g. Абита ‘Assyria’, Атафауа ‘Arabia’, Ufratu- 
6018:"Euphrates", Armina ‘Armenia’, Karka ‘Carians’, 
8549:with well-known rivers (Ufrätuš ‘Euphrates’; 
8612:Ufratus, Tigra. 
12118:amu» Ufrātwã ‘a town beside the Euphrates’; 
14342:Euphrates"), and then a resumptive adverb. The . E 
16886:Foy’s [abiyiyam. *? Ufratuvà KT. % [-- Jie[4- 3- -]a. RL; 
17098:Euphrates—there this Nidintu-Bel who called 
22635:at Zazana on the Euphrates, X 2 ($19); he pursued 
24577:Ufrütu- sb. ‘Euphrates’, river of Babylonia: 
29379:Euphrates above Babylon: Elam. 2a-12-2a-an, АКК. 
=== BRT p9r9tu
16069:•j.,g.p»r9tav-ra.,f.'*i) 'Durchgang,  Gang*: "tui  F.  JO;  —  frabm?m  daiähsus  nava '%ioS  (AP.)  k»r?nai'a  "in  der  grössten  Ab- teilung des  Bezirks  mach  neun  Gänge ((L  i.  Abteile)"  V.  2. 30";  —  fraUtmm °^wd  (AP,)  Aazavnm  narqm  näirinanua taoxma  upa.bara  "in  die  Gänge  der  grSssten Abteilung  bring.. "■V.2.3o'>,  2)'^gang, Pforte',  mit  z^mS  'Pforte  des  Winters',  Name einer  Örtlichkeit:  ndt^  tä  im  xsnäus  vaipyS (sd.).,V?(LS.)  t?mB\.5i.  1 2.  3)  'Durch- gang durch  — ,  Übergang  über  das  Wasser, Furt,  Brücke':  afqmca  -/«/(AP.)  Y.42.1; —  apqm  .  .  nOvayanqm  patti  °tül  Yt. II.  4.  a)    mit    GS.    Smiatö  (sd.)    'die
```


## [2026-09-14T03:12:15.486Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT lexicon Ufratu\"; sed -n '24570,24585p' KNT_full.txt; echo; sed -n '8540,8555p' KNT_full.txt; echo \"=== BRT haosyanha entry\"; sed -n '28810,28840p' BRT.txt",
 "description": "Kent Ufrātu lexicon and BRT haošyaŋha"
}
```


### [2026-09-14T03:12:15.574Z] TOOL RESULT

```
=== KNT lexicon Ufratu
slà- (6140.1, $142), ef. Gm. Bei-stand for meaning. 
upastém asf. AmH 10; DB 1.25, 55, 87, 94; 2.24f, 
34, 40, 45, 54, 60, 68, 86, 97°; 3.6, 17, 37, 45, 62, 
67, 87; 4.60f, 62; DPd 13; DNa 50; DSf 19°; DSk 
5; XPh 32, 45. 


Ufrütu- sb. ‘Euphrates’, river of Babylonia: 


OLD PERSIAN 


Elam. t-ip-ra-tu-i8, Akk. purattu, Gk. Еўфрат 




of less-known place names the generic word is 

regularly given; but it is given with names of 
provinces only when there is a list of all or several, 
and is omitted with some larger districts (Kar- 
тала, Varkàna), with cities (Pársa, if = ‘Persepo- 
пе’; Passiyduvdda ‘Pasargadae’; Hagmatana 'Ecba- 
tana’; Arbatra ‘Arbela’; Babirus ‘Babylon’), and 
with well-known rivers (Ufrätuš ‘Euphrates’; 

Тита ‘Tigris’). The place names may be geo- 

graphically, and to a certain extent linguistically, 

grouped together as follows? 
=== BRT haosyanha entry
j.  haoäyasha- m,  EN.  zweier  Gläubiger;
dby  Google
1 739  hao$yanta-  -
i)  des  Stammvaters  und  ersten  Königs der  Iranier*':  tqm  yasata  'nhö  parahals (sd.)  upa  iipaMi  karayk  Ytj.ii;  is-l, 77.  z6;  —  ttjrtm  kavaün  3?armd  .  . yat  upanhalat  'rah^m  parmäUm  Yt  ig. 26.  3)    'fihahe    taxmahe    aS'aonS    Yt.
*)  Vgl.  Bd.  31.  1,  WasT  SEE.  34.  57,  Tusti  ' NB.  391.
Eig.  B«<].7  Versuch  einer  EL  bei  JusTi  WB. 126.
•  j.  haoäyanta-  Adj.  'der  ausgepresst werden  soll,  wird',  vom  Haoma:  ysi  lanti^ haoma  .  .  afaya  htKvana  (sd.)  asaya  hao- syanta  (NP.)  Vr.nj.s.  |
PFP.  zam  V.  i*ai-.;  am  dem  Praes.  17  (Fat.) gebildet;  %30g.\^.  —  Vi.:  ke ..kunil  täk  nun . .  hunVifl  hac  nünfräl  "bis  jetzt  ausgepreist . . voQ  jetzt  an  ferner  la  pressen".
•  yvlspa^a  antar»  as>m  tt/ii'°'hau§tuaya'^ P.jo.
PQ, :  o').  —  ■)  DST.  ZA,  66  vermutet  iujlu- tayä.  —    '}  Bei   Blochzt  Lex.   ist   das  Wort
•  j.,  g.  'hak-  V.  'sequi*.  Fracs.  1  Äai-, si;  2  haca-,  5  *his.hak-\  hisk-,  15  haxsa-, 16  (Des.)  hixia'^,  2  +  24  hacaya-,  30 (Her.)  häcaya:  —  PPfP.  'haxta-;  Inf. haxtSit.
i)  mit  Akk.;  a)  'begleiten,  sich  an- schliessen  an  — ,  sich  gesellen  zu  — ':  yim halaite  aiis  vanuhi  Yt.  10. 66;  —  asi ää%re  .  .  :^ariJi5  aiiqm  naram  yöi  (als Akk.)  haMAi  Yt.i/.ö;*;';  —  lim  hacat  aÜl Yt.  /p.  S4;  Vyt.  8{hacatu) ;  —  a<fa..dar>santa %wä  pairi  If^wä  jamyama  hamsm  harä Aaxma  "o  A.,  wir  wollen  deines  Anblicks teilhaftig  werden,  wir  möchten  zu  dir  ge- langen, wir  wollen  ganz  dir  zugesellt  wer- den" Y.  ßb.  u'';  —  ärmaiii  hacimnö XI  änm  (Sp.  1 83  m.)  V.  43. 10.  b)  'nach- gehen, sich  umtun,  bemühen  um  —  :  yS.. ahyS  iaoling ..Tarfn}ng{sA.)  hacaitg  "-viei seinen  (eigenen)  Neigungen  . .  nachgeht" Y.  48. 4;  —  yöi  xinam  (sd.)  .  .  hacanti "die  sich  bemUhen  um  .  ."  Y,  41?.  12;  — alcä  kBi  s^antä  (3PIA.)3>  .  .  xMUm  (sd.) Y.5J.  2,  c)  'hinter—  her  sein,  drängen,
dringen  in  — ,  antreiben  zu  — ';  mit  o)  Dat oderdatlnf.,  3)  Injunktiv  (s.  3  b  ß);  zua): yqslä  haxsäi  xsmSvatam  i-ahmäi  ä  "und die  ich  antreiben  will  zu  eurer  Anbetung" Y.  46.  10;  —  yezi^a  *ditn  hacayat  . yasnaica  .  .    Yyt4j;    4j  {iixia%a);    —
'hak- 2  b
1740
Jtä  litis  syaaianäi  (sd.)  matifil  yaHa  *v3 *haxtnV^  (n'ämL  syao'hanäi)  ".  .  wie  ich euch  dränge  (zu  tun)"  Y._j4.s**;  — *kixsalsa  .  .  kfmcit  ar»hSuS  .  .  affaiA-a daxmaliva  vTkantle  iiA.)  V.  7.  50;  F.  24 {hixial)^^; — Aaxsaya{i%0^.)azfmcit../ra- i>mq  . .  aitihä  damaya  anuniatayai(sd.ya "soll  ich  die  Obersten  antreiben  .  ,?"  Y, S.  j-j—yaka  atim  käcayene  ..  zara^ttitrtm anumatie  (_sA.)  dainayäi  YLj,  18;  105, g.  »6.  zu  ß);  *hixsäne  nanm..  *hixsäne nairikam  .  .  *hixsäru  drt'aiqm  .  .  sqm  .  . nrp3rayan/a  (sd.)  "soll  ich  ,  .  antrei- ben, dass  sie  . .  sich  aneignen''  V.  79. 26.  d)  'Jemandem  zu  teil,  zu  eigen werden,  eignen':  kacaiti  dim  aspahe  aojö Yt  ig.  68;  68I;  —  ttm  kacät  V)ri>r»m  . . aat  ana  vsrihra  hatmnS  (s.  2b)..  Yt J5- S4i — >^i  ttasTm  ..  sig(Sp.  1607  m.) , .  masyä  hacaite  . .  xratui yaira  mthr^mat . .  hacaite  . .  xratus  "es  gibt  keinen  Men- schen .  .,  dem  grösserer  Verstand  zu eigen  ist  als  .."Yt/o.io;.  e) 'in  Be-
sitz einer  Sache  kommen,  teilhaftig  werden; teilhaftig  sein':  fi-masays  alöis  baelaza (APn.)  haHmna  Y.  60,  4;—  haomaiiqm ..  assis  baisaza  (APn.)  haHmnanqm Vr.p,  I ;  1',  2;  —  Uta  buyS  . .  dSus.sranä (sd.)  haHmnS  Y.  77.  i.  2)  mit  Instr.;
a)  'begleiten,  gehen  mit  — ;  verbunden, vereint  sein  mit  — ':  hacanulia  .  .  *ana  .  . *  ana ..  AaxtUiJ  (sd.)  N.p; —  a^J  *kax3mqm (sd.)  Syatyais  kUcamaid^'*  Y.  40. 4 ;  —  tarn dainqm  .  .  yä  mdi  gafhä  asä  fradöit hacsmnä  "die  Religion  .  .,  die  im  Verein mit  Asa  was  mein  ist  fördern  möge"  Y. ^^.  lo;  —  ya%rä  asä  hacait!  ärmattis "wo  mit  A.  Arm.  vereint  ist"  Y.  46.  16; — yehyä  uruä  asä  hacaitl  "des  Seele  mit Asa  eins  ist"  Y.^4-2;  —  suraosi  aii taqta.raya  (sd.)  hacimnö  Y.^^y.  12;  — sraoSö  yS  '"asahe  (lies  asi)  hacaite  *mq- täraya  (sd.)  Y.  27.  6;  Yt  10.  ii7{?);  — mazdä  .  ,  hac'imnS  *mihra  rainuca  ,ir- maitica  .  .  "M.,  zusammen  mit  Mi.  und X.  undÄrm."  Yt  13.  3;  FrW.  7. 1 ;  —  *anye *maoa»h^  (sd )  alima  haanie  .  .  äal  .  . haomahe  ma^  asa  hacaite  urvasmatta Y.  70.  8;  Yt/7.  5'.  b)  'in  Besiu  einer
Sache  kommen,  teilhaftig  werden,  sein,  zu eigen  haben':  t>m  hacat  (s.  i  d)  v^i^nm .  .  äat  ana  v)ri%ra  hacimnS  vanät  .  . Yt7p.  54J  — ya%a  aam  avata   v^n^ra
aby  Google
174»
■hak-  mit  a
hah«r9t
1743
Hacäne  Yt.5. 69;  —  a/arö  (sA.)  vfrf%\ hacaite  Yt, /4-44;  —  vsr^^rava  zaina hacimnS  hulasta  .  .  ^anna  kaHmnS Vt.  10. 141  i  67,  Y.  ig.  17  (?).  3)  absoL; Med.;  a) 'zusammenstimmen,  harmoniren': nöit  nä  mann  . .  naSlä  varanä  (sd.)  . .  tUSit uri'qnS  hacainti  Y.  45.  % ;  —  ayä  *aröi hikur3n»n  (sd.)  yayh  haHntl  urvqnS  Y. ,?.?■  9-  b)  'sich  zusammentun,  vereinigen'
um  etwas  zu  tun;  mit  «)  Inf.,  p)  Inj.  (s. 1  c  3);  zu  a):  dväciiia  /lä*  (sd.)  ha cimna  (NDm.)    Yt.  70.84.  zu  ?):>«/
me  slärS  .  .  halante  paraca  mi  twr^iyS i^arynS  *baxsprUa  yaesi  .  .  ".  .  dass  sich die  Sterne  mir  zusammentun  und  voran der  Mond,  um  den  Kriegern  Herrlichkeit zu  schenken,  will  ich  , ."  Yt  <S'.  i.  [ha- (imna  V.  44-  13:  lies  Aa^na;  —  kaxiaitt N.p:  lies  hä  xsayete.
mit  ä  'sich  heften,  haften  an  — '  (Aklc): ä  diiit  ä* hil.haxti''l  yava&a  .  .  "an  den heftet  er  sich  .  ."  V.5. 34.
mit  upa  1)  mit  Akk.;  a)  "begleiten,  sich anschliessen  an  -,  sich  gesellen  zu  -'  (s. Simpl.  I  a):  ulta  bn  yim  hacahi  uta upatfhaöaAiYt.  ij."} ;  — yat  dim  upaiahalat yd  . .  hqm.var?itis  Yt  ig.  39;  39;  — pairi- kam  .  .  yä  upanhacat  kinsäspim  V.  7. 9.  b)  'Jemandem  zu  eigen  werden, sein'  (s.  SimpL  1  d):  li'arms  .  .  yai  upan- hacal Äaofyarfh)mYi. ig.  26;  66  {'caiii);  — upa  ^ws  haxiöii  ghd  vq%wa  upa  .  . *fouruJas  . .  upa  %wa  f>r}svatca  matts  . . Aaxidit  \.  62.10;  —  upa  %wä  hixial^a N\i.45{7).  2)  mit  Instr.  'einer  Sache teilhaftig  werden'  (s.  Simpl.  3  b):  daHat ahmai  . .  ya%a  13  upanha^ai  "  .  dass  er des  teilhaftig  wurde"  Yi.  i^. '^raynS  .  .  upa.haxIS voll  Ungestüms  .  ."  Yt  iQ.  71.  3)  mit
Dat.  der  Person  und  fin.  Dat.  'Jemandem willfährig  sein  zu  —  (dass  er  ,  .)':  kahmai .  .  upanhacayeni  .  .  fraranhai  haomana- tihäica  "y/em  .  .  soll  ich  willfahren,  dass er  munter  und  wohlgemut  sei?"  Yt.  5. 8.  4)  absol.  'vorhanden  sein':    vJspim
a  ahmai  yal  alsa  *gainH!  upavAaÜaili ". .  solang  der  Gestank  (davon,  näml.  der Leichenstätte)  noch  wahrnehmbar  ist"  V. 7-56.
```


## [2026-09-14T03:12:18.026Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in 'hunar' 'hučihr' 'hucihr' 'hunyāg' 'huniyāg' 'hunyag' 'hujastag' 'huǰastag' 'hurust' 'husraw' 'humāy' 'humay' 'xūb' 'xwašnūd' 'hušnūd' 'xurram' 'huram'; do echo \"--- $w\"; grep -n -- \"$w\" PHD.txt PHD_mackenzie.txt 2>/dev/null | head -4; done",
 "description": "Grep MacKenzie Pahlavi dictionary"
}
```


### [2026-09-14T03:12:19.467Z] TOOL RESULT

```
--- hunar
PHD.txt:398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
PHD.txt:692:ability čāraggarīb, hunar, šāyendag- ih, tuwānīgih; extent of ones — tuwān-sāmān.
PHD.txt:3682:skill abzar, hunar, hunarāwandīh, kārāgāhih, kirrēgih, nēzūmānīh.
PHD.txt:3683:skilled ` abzarómand, frahixtag, hunarāwand, hunarómand, kār- āgāh, kirrēg.
--- hučihr
--- hucihr
PHD.txt:953:beautiful hucihr, nëk(óg).
--- hunyāg
--- huniyāg
PHD.txt:1546:delight huniyāgīh, urwahm(an)ih.
PHD.txt:1776:entertainer huniyāgar.
PHD.txt:1777:entertainment huniyāgih.
--- hunyag
--- hujastag
--- huǰastag
--- hurust
PHD.txt:4301:well-born pad-góhr(ag). well-grown hurust. well-known nāmčišt.
PHD_mackenzie.txt:7961:well-grown hurust.                     woe way.
--- husraw
PHD.txt:400:huniyāģar [hwayd’kl | N xunyágar] entertainer, musician. hu-niyox$ [hwnydwhs] attentive. hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~ih : happiness, content. hunušak [hwnsk' = Av. hunu§] offspring (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic drink, *koumiss. huram [hwlm | N xurram !] happy. ««īh: happiness. hurām [л?т] blissful. hu-|-ramag [hwlmk'] having good flocks. ~-rust [-/wst'] well-grown. ---Süzagih [-s’ckyh] agreement. ~-8рӣз [-s5?s] grateful. ^ husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good керше у m ~ih: fame, good repute. Ms hušk [kwšśk! | = M, N xušk] dry. —-kün [-S TE] impotent. hu-škūh [kwškwh] dignified, splendid. ^h: dignity. hu&nüd(ag) [лото (А)! | M hwinwd, N xusniid] contented, happy. ~th: contentment, happiness. hu-tuxš [kwtwhš] artisan. huwaršt [hwwlst! = Av. hwarfta-] virtue, good deed. hu-xém [hwhym] of good character, good-natured. ^h: good character. hüxt [kwht' = Av. hüxta-] good speech.
PHD.txt:1877:fame husrawih, nàm.
PHD.txt:1879:famous husraw, nāmčištīg, nāmīg.
PHD.txt:2126:good (a.) huda(ha)g, nēk(ēg), new, weh, xūb, hu-, P naxšag; ~ char- acter huxémih; — deed huwatršt, kirbag; — repute husrawih; — rule hupādixšāyīh; ~ ruler hupádix- šā(y); ~ speech hüxt; ~ spirit spenag mēnēg; ~ thought humat; of ~ behaviour hukunišn; of ~ character huxém; of — religion hudén; of — repute husraw; of — speech hu-éwaz, hu-gówisn; of ~ stock pad-góhr(ag); of ~ thought humenišn.
--- humāy
PHD.txt:398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
PHD.txt:999:bird murw, way, wayendag; little ~ murwizag ; ~ of good omen humāy; ~ of prey škarag.
PHD.txt:1720:eagle āluh, dalman, humāy.
--- humay
PHD_mackenzie.txt:2951:humay [hwm)y IN ......] a bird of good omen; eagle.
PHD_mackenzie.txt:6464:eagle aluh, dalman, humay.                   endure burdan, pattiidan, widar-
PHD_mackenzie.txt:11950:humay                       JoM6V"            xwarwariin              \~~~
--- xūb
PHD.txt:2126:good (a.) huda(ha)g, nēk(ēg), new, weh, xūb, hu-, P naxšag; ~ char- acter huxémih; — deed huwatršt, kirbag; — repute husrawih; — rule hupādixšāyīh; ~ ruler hupádix- šā(y); ~ speech hüxt; ~ spirit spenag mēnēg; ~ thought humat; of ~ behaviour hukunišn; of ~ character huxém; of — religion hudén; of — repute husraw; of — speech hu-éwaz, hu-gówisn; of ~ stock pad-góhr(ag); of ~ thought humenišn.
--- xwašnūd
--- hušnūd
PHD.txt:1373:content(ment) hunsandih, hušnūdīh, Énómag, šnēhr, wīdwarīh.
PHD.txt:2200:happiness farroxīh, huramih, hun- sandih, hušnūdih, šādih, šnāyēn- išn, urwāzišn, xwa(h)rih.
--- xurram
PHD.txt:400:huniyāģar [hwayd’kl | N xunyágar] entertainer, musician. hu-niyox$ [hwnydwhs] attentive. hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~ih : happiness, content. hunušak [hwnsk' = Av. hunu§] offspring (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic drink, *koumiss. huram [hwlm | N xurram !] happy. ««īh: happiness. hurām [л?т] blissful. hu-|-ramag [hwlmk'] having good flocks. ~-rust [-/wst'] well-grown. ---Süzagih [-s’ckyh] agreement. ~-8рӣз [-s5?s] grateful. ^ husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good керше у m ~ih: fame, good repute. Ms hušk [kwšśk! | = M, N xušk] dry. —-kün [-S TE] impotent. hu-škūh [kwškwh] dignified, splendid. ^h: dignity. hu&nüd(ag) [лото (А)! | M hwinwd, N xusniid] contented, happy. ~th: contentment, happiness. hu-tuxš [kwtwhš] artisan. huwaršt [hwwlst! = Av. hwarfta-] virtue, good deed. hu-xém [hwhym] of good character, good-natured. ^h: good character. hüxt [kwht' = Av. hüxta-] good speech.
PHD_mackenzie.txt:2974:huram [hwlm I N xurram !] happy.
--- huram
PHD.txt:400:huniyāģar [hwayd’kl | N xunyágar] entertainer, musician. hu-niyox$ [hwnydwhs] attentive. hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~ih : happiness, content. hunušak [hwnsk' = Av. hunu§] offspring (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic drink, *koumiss. huram [hwlm | N xurram !] happy. ««īh: happiness. hurām [л?т] blissful. hu-|-ramag [hwlmk'] having good flocks. ~-rust [-/wst'] well-grown. ---Süzagih [-s’ckyh] agreement. ~-8рӣз [-s5?s] grateful. ^ husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good керше у m ~ih: fame, good repute. Ms hušk [kwšśk! | = M, N xušk] dry. —-kün [-S TE] impotent. hu-škūh [kwškwh] dignified, splendid. ^h: dignity. hu&nüd(ag) [лото (А)! | M hwinwd, N xusniid] contented, happy. ~th: contentment, happiness. hu-tuxš [kwtwhš] artisan. huwaršt [hwwlst! = Av. hwarfta-] virtue, good deed. hu-xém [hwhym] of good character, good-natured. ^h: good character. hüxt [kwht' = Av. hüxta-] good speech.
PHD.txt:760:Ahuramazda Ohrmazd.
PHD.txt:2200:happiness farroxīh, huramih, hun- sandih, hušnūdih, šādih, šnāyēn- išn, urwāzišn, xwa(h)rih.
PHD.txt:2201:happy farrox, huram, hušnüd, Sad, xunak.
```


## [2026-09-14T03:12:37.223Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"##### HRN p.111 (leaf 132)\"; awk 'BEGIN{RS=\"\\f\"} NR==133' HRN.txt; echo \"##### HRN p.108 (leaf 129)\"; awk 'BEGIN{RS=\"\\f\"} NR==130' HRN.txt",
 "description": "Print Horn pages 111 and 108"
}
```


### [2026-09-14T03:12:38.252Z] TOOL RESULT

```
##### HRN p.111 (leaf 132)
— 111 —
500. ^fyalTden *f?chmeckon' , /^al 'Speise', /^älger, /^älf,
X^'ältger.
aw. x^arezista-; phlv. /^list (vd. 2 (77))'); arm.
l^alcr 'süss (sehr unsicher, H. No. 287).
501. polier \Sch wester, /ö/j.
g. yohr; Käs. /üh, yöh,
SiW. /^afihar- Schwester; phlv, /^'ühar, ytlk {PPGl.);
ai. svasar-; arm. ^^oir (H. No. 294).
kurd. xöh, ;c^A^» ^^^^ (H.-Sch.), af}'. yöt' ; oss. d. /ore,
t. ;ro; bei. gvahär, n. gvähar, göhär, gvär (131) 2); wa/.
;^m/, sar. ya;^, minj. yayvd, sangl. i/vd.
502. x^**^^*» /^^^^ 'Wohlgeschmack'.
skr. sräda- * Wohlgeschmack*.
kurd. x^ *Salz ; bei. väd, n. väd, vad\ vü:: (411)
'Salz.
In diesem Worte hat sich die ursprüngliche Be-
deutung der [/"svad- im Neupersischon allein noch
erhalten; vergl. /^'dfiten (No. 497).
503. y(nb gut, schön , /hIü.
Ka§. /ßh, /öb^ /eb.
aw. hväpah' 'wohltätig; phlv. /rap bezw. /üp,
Xüpih; ai. svdpas-'^),
504. lud, ^eS (AM.) 'selbst'.
Käs. x^d.
ap. vergl. wrö- ; aw. yyatö 'selbst'; phlv. ;^^a^, j^^'a/^Ä ;
ai. svdtas,
kurd. ;^i2 ; af/. ;t'/>'<^ ; oss. d. x'^^^^^9i t. /ädäg (298) ;
bei. i?a^, n. viixt^ vas; äiyn. ^w, sar. /w, wa;^. ;frti, gen.
505. x'*^* 'Sonne', hur, hör (reimt auf .<??^^ör; Sahn. 111,1105
Vers 693), Xurasan,
*) So korrigirt D armesteter, 6t. ir. I, 136.
') Yergl. Bartholomae ZDMG. 44, 552, Hübschmann ebenda
557, Geiger, Lautlehre d. Bei. § 15, 3. Uraprachliche Dialekt-
Verschiedenheit.
«) Ebenso Fr. Müller, WZKM. 5, r>7.
##### HRN p.108 (leaf 129)
— 108
486. yi^usur 'Schwiegervater.
aw. /asitru' 'Schwiegervater ; ai. imruru-; arm.
skesr]ah\ d. i. 'Mann der Scliwiegermutter (Hübsch-
mann, Xo. 253).
kuvd. /a2ur, xozJ)\ /aur 'Schwiegervater ; afy. s^or;
bei. n. vasarik 'Schwiegervater, vasar\2ä/t *Schwager
(405); wa;K'. yjtrs, sar. (LW.) Xasur.
•Vergl. /Hsrä (No. 487).
487. xusrfi, zesä^ /jisü^ /'es etc. 'Schwiegermutter.
Käs. /asrii',
ai. <;DarrU' 'Schwiegermutter'; arm. akesnr (H. No. 253) ;
lat. socru-s; ksl. soekry.
kuvd. /ost, /esü, yasrü 'Schwiegermutter; af/. ;K''ö4fa ;
bei. V((8sö, vasl, vase (406) ; wa;^. /as, si/n. /as, sar. /,e/.
Vergl. ytisur (No. 486).
488. x^Ht 'Ziegel, Backstein'.
aw. istya- 'Ziegel, Backstein' ; phlv. /ist ; skr. isfakOr-
'Backstein'.
afy. LW. /ßta; bei. ist (168).
489. ^usk 'trocken', /ös« ') 'Ähre', yös, yöslden, yösdniden
(AM. 236 Zeile 3 v. u.), /mkUm,
Kä§. tisk (jendn, husküdSn.
ap. Msia- trocken'; aw. huskd- 'trocken*, aflluiosemnu'
'nicht vertrocknend'; phlv. /<*^Ä;, /usklh^ /ösTnUän
(Bund.)-); ;rösaA; 'Ähre' (Bund.); ai. güska-, güsyati,
skr. gösa-.
kurd. LW. hüsk; afy. vud; oss. /tisk, ba/ussin (311
und Seite 141); bei. husay 'trocknen, austrocknen (160)
(LW?); wa/. vesk,
np, /uskar {/usk ärd, Vullers, 756, vergl. dial. ör,
oben No. 13), arab. LW. x^iskar 'Mehl', phlv. /nsk[a]r
V
(vd. 6 (9) Gl., Say. näsäy. 2, 35). Vergl. de Lagarde,
Semitica 1,41, Nöldeke, ZDMG. 32, 408; de Lagarde
*J Phlv. ;(Osak (Sternbild, Bund.); kurd. t*st, vasi^ krisl; afy. vazai;
bei LW. hösay, d. hösay (100).
2) Vd. 5 (43) (44) steht zwei Mal xösinUan,
```


## [2026-09-14T03:12:53.847Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"##### HUB p.57 (leaf 67)\"; awk 'BEGIN{RS=\"\\f\"} NR==68' HUB.txt",
 "description": "Print Hübschmann p.57"
}
```


### [2026-09-14T03:12:54.804Z] TOOL RESULT

```
##### HUB p.57 (leaf 67)
- 57 —
498. Zd. x^aini" wird von der Phi. tTbersetzung durch
xup *schon* wiedergegeben, das vollkomnien passt. Die
Zusammenstellung ist also falsch.
501. Np. x^ahar Schwester aus ^jf'ahar, vgl. skr. ace.
soctsaram, Ahnlich ware np. bahar 'Friihling' = phi.
vahar aus *vahar entstanden, wenn es zu ap. d^uravo-
hara- geh5rt.
502. Dazu np. nctnx^ah 'Ammi' u. s. w. als *Brot-wurze',
afgh. x^and 'Geschmack, Wohlgeschmack, Vergniigen
(Geiger) , kurd. xevS *Salz* ZDMG. 38, 64. Falsch ist
wohl die Aussprache x4/va, fiir die man x^a nach alien
Analogien erwarten muss. Vullers ftihrt x^ai neben
xiva an. Auch nach N 5 Id eke ist das Wort einsilbig.
503. Nach dieser Etymologic sollte man im Neup. *ipwi,
*a;''ai oder *x^ab statt xUb erwarten. Ich setze xub
(paz. xUb Shk. 254, afgh. LW. xilb 'schon) = skr.
suvapus' N. pr. (von m gut* und vapus- 'Gestalt, Schon-
heit').
505. Np. xor = x^ar 'Sonne* ist = zd. *x^'are, gen. x^mg-,
dagegen hdr 'Sonne* = zd. hvare^ gen. Awr5, skr. suaVj
gen. sfAras. Also geht xorsBd (Nr. 506) = x^arsed
*Sonne = paz. x^arsSd Shk. 255 auf zd. "^x^are-
xsaetem^ die Nebenformen von hvarexsa^tem zurtick.
507. Arm. xortik^K plur. *Speise* = zd. x^areti-, phi. x^ar-
iik^ np. x^ard% 'Speise*. Das afgh. Verbum schreibt
Geiger x^arql *essen, geniessen, trinken*. Arm.
*xortak findet sich nur im Denom. xoriakem 'schlage
in Stiicke*. Das zugehdrige np. xurda *klein, kleines
Stiick' kann mit lat. curitis (— gr. ^agxig geschoren'
nach Brugmann, Grdr. I, 238, zu ksl. hrattiku nach
Fick, Wb.'* I, p. 385), dem ein np. *A:»rrf oder *Aarrf
entsprechen wiirde, nicht vermittelt werden. Horn's
Bemerkungen tiber das anl. x aus k sind verfehlt.
Vgl. Fr. Mtiller, WZKM. 7, 373.
508. Np. x^aS gut, schon, angenehm' = zd. "^hvasi- (skr.
sval^Or-) sch5naugig? Moglich, aber nicht sicher.
Vgl. bal. vas 'siiss, angenehm, gut, glucklich, fr5hlich*.
```


## [2026-09-14T03:12:56.320Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 'hovaid' 'huvaid' 'hoveid' 'paidä' 'hu-vaeda' 'hunivak' 'yunyä' 'xunyä' 'yunj'; do echo \"--- $p\"; grep -n -i -- \"$p\" HRN.txt HUB.txt | head -5; done",
 "description": "Grep Horn/Hübschmann for hovaydā and xonyā"
}
```


### [2026-09-14T03:12:57.424Z] TOOL RESULT

```
--- hovaid
--- huvaid
HUB.txt:6196:apam; huvaida 'deutlich*, aus hu + paidd; vdrUn 'inversus,
HUB.txt:7646:und in Humdi (§ 105) sowie in huvaida oflfenbar , hamana
--- hoveid
--- paidä
HRN.txt:3311:LW. kurd. peidä; sdy, paidä; bei. peda^ P^dag^
HRN.txt:19946:paidä 349.
--- hu-vaeda
--- hunivak
--- yunyä
--- xunyä
--- yunj
```


## [2026-09-14T03:13:21.429Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'hu-va' BRT.txt | head -20; echo \"=== hu-vaed / suveda\"; grep -n -E 'hu-vaeda|huvaeda|hu-vaSda|hu-vaida' BRT.txt | head",
 "description": "Grep Bartholomae hu-va compounds"
}
```


### [2026-09-14T03:13:21.492Z] TOOL RESULT

```
30628:AvOiStaefva\  1      Slalt  hu-vaP  geschr.,  S  268.  H.  —  ai.  suvacas-
=== hu-vaed / suveda
```


## [2026-09-14T03:13:22.451Z] TOOL CALL #28: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py; echo ===; ls data/verification/sources/refs/incoming/BQT/",
 "description": "Inspect ref_page tool and BQT incoming"
}
```


### [2026-09-14T03:13:22.515Z] TOOL RESULT

```
Exit code 1
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
(eval):1: == not found
```


## [2026-09-14T03:13:36.623Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for f in BQT_v3_pages.txt BQT_v4_pages.txt BQT_v5_pages.txt; do echo \"=== $f\"; ls -la $f; head -3 $f; grep -c 'pdf page' $f; done",
 "description": "Inspect BQT vol3-5 page files"
}
```


### [2026-09-14T03:13:37.702Z] TOOL RESULT

```
=== BQT_v3_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2499427 Sep  4 14:06 BQT_v3_pages.txt
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
721
=== BQT_v4_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2055176 Sep  4 14:06 BQT_v4_pages.txt
[pdf page 1]
[pdf page 2]
ه
553
=== BQT_v5_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 723928 Sep  4 14:06 BQT_v5_pages.txt
[pdf page 1]
5
[pdf page 2]
293
```


## [2026-09-14T03:13:38.737Z] TOOL CALL #30: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));b=d['BQT'];print(json.dumps(b.get('scans'),ensure_ascii=False,indent=1)[:2000]);print(b.get('page_offset'));print(b.get('lookup_hint'))\n\"; ls data/verification/sources/refs/ocr/ 2>/dev/null; ls data/verification/sources/refs/ocr/BQT 2>/dev/null | head -30",
 "description": "BQT scan config and OCR cache"
}
```


### [2026-09-14T03:13:39.991Z] TOOL RESULT

```
[
 {
  "volume": "3",
  "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "first_printed": 1208,
  "last_printed": 1925,
  "pdf_offset": -1205,
  "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json",
  "lang": "fas",
  "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"
 },
 {
  "volume": "4",
  "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "first_printed": 1920,
  "last_printed": 2475,
  "pdf_offset": -1917,
  "lang": "fas",
  "offset_note": "printed = pdf+1917, checked at pdf 150 and 500",
  "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"
 },
 {
  "volume": "5",
  "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "first_printed": 1,
  "last_printed": 290,
  "pdf_offset": 5,
  "lang": "fas",
  "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.",
  "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "requires_volume": true
 }
]
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
AFM
ARY
BLY
BOOK
BQT
FFD
HRN
IRN
PLA
SNS
SOD
TAD
0001.png
0001.txt
0049.png
0049.txt
1024.png
1024.vision.txt
103.vision.txt
1074.vision.txt
1085.png
1085.vision.txt
1092.jpg
1092.vision.txt
1187.png
1187.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1230.png
1230.txt
1237.png
1237.txt
1237.vision.txt
1261.png
```


## [2026-09-14T03:13:52.855Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for pdfp in 257 380 448 484; do echo \"########## v4 pdf page $pdfp (printed $((pdfp+1917)))\"; awk -v p=\"[pdf page $pdfp]\" 'BEGIN{RS=\"\\f\"} index($0,p)==1' BQT_v4_pages.txt | head -60; done",
 "description": "Extract BQT vol4 pages 2174,2297,2365,2401"
}
```


### [2026-09-14T03:13:53.830Z] TOOL RESULT

```
########## v4 pdf page 257 (printed 2174)
[pdf page 257]
بو ۱۷
اول هم درست است - و دلیر و پپلوادرا نیز فو! « بروزن هوا . چند معنی دارد :
کنتهاید ۱ - وبمعتی ناله کردن وزاری هم‌آمده ۱ هرنقمه وآهنگه و آواز وداله راگوبند۴
است ۴ - و اهر باین معنی هم هست بمنی ناله | عموما خواه از اسان باشد و خواه ازمرغان 8 .
و زار ی کن ۴ - و حرکت وجنبش ولرزه را نیز | ۲-نام مقامی‌است ازجمل‌دوازده مقام موسیقی۹ +
کوبند؟۴ - وامربلرزیدن وجنبانیدن هم‌مت ۴ | ۳ - جممیت و سامان و سرانجام و کترت مال
بمنی بلرز ویجنب وبلرزان وبجنیان + و توانگری و نیکوبی حال و رولق‌کار باشد ۷

- رشیدی کوبد: «* و پهلوان ودلیر که نیو نی ز کوبند . فردوسی گوید:
اکر چند بیژن جواست ولو ر بهن کار دارد خرد پیش رو
وله : جهاندار کاوی شان پیش رو زلشکر بی رزم سازان نو . >
(و رك : جهانگیری ایاً) اما «نو» درین آشمار بمعنی جوان است ولورسیده (رك : فهرست ولف)
ولی‌ممکن است « نو »> بکسراول مخذف «نیو» (ه.م.) باشد ولی‌نه در اشمار مذ کور.
۲ - ريشة « نوبدن » (ه.م.) ۴ - رد4 : وین .
۴ - پهلوی 210816 [ 81۷2۳ - 1۵1 خوش نوا ] « اوتوالا ۲۰۵ > +
8 -قی : ارمنی 2028 ( آهنگه » نغمه , سرود ) » 8188612 ( من مینوازم )

« هوبشمان ۱۶۸۹ :

ففان ازین غراب بین و وای او که در نوا فکندمان نوای او.
منوچهری دامغانی ص۷۹ .۰

نوا بازی کنان در پردة تنگه غزل کیس و کشان در دامن چنکه.
نظامی کنجوی «کنجینه س ۱۵۹ *.
. نوا یکی از اصطلاحات موسیقی‌است و چنان مینماید که بمعنی‌پردة موسیقی ومقام باشد ,چنانکه
در الحان قدیم نام « نوای چکاوك > , * نوای خارکن > ۰ * نوای خسرواتی» آمده ( رك : عريك
از کلمات مذ کور). «نواگر» و «نوا زن» نیز بمعنی زندة‌آهنگک موسیقی است. «نفیسی. تعلیقات
تاریخ بیهقی ج ‎٩‏ ی ۸۹۱ . رك : نواختن . ۹- * نام مقامی است از جملهٌ دوازده

مقام موسیقی , چنانکه شاعر در مقامات شعبه‌هایی بنظم‌آورده :

نوا آمد مقام و هست مشهور زوی نوروز خارا هست وماهور...» « جهالگیری >
« هنوز یکی از آهنگهای موسیقی کنوی بنام « نوا > معروفت ... عبدالقادر بغدادی در « لغفت

شهنامه » (چاپ پطرزبو رکه ۱۸۹۵ ص ۲۱۹) تسریح میکند که نوا نام نغمه‌ای در پردءصفاهان»

است و مانند ۶ حسینی » در پردهٌ صفاهان زده میشود > رك : نفیسی . تعلیقات تاریخ بیهقی چ

۷ ص ۰.۸۹۱ نوا یکی ازهفت دستگاه ابرانی‌است. فواصل درجات «گام»آن مانند شور است ولی

«تنیث» ( پم اول ) ( مبداً ) آن درجهٌ چهارم کام شور میباشد ( از افادات استاد ابوالحن‌سبا ).

۷ - «اسلا نوا بمنی وسایل زندکی و آنچه زند کی را درخور است , چنانکه امروز
« بنوا رمیدن » رسنی‌در زند کی کشایش بافتن » و*بی‌نوا» بمنی کسی که تنکه دستست ودرزند کی
او کشایشی لیست ... اما ۶ جمعیت وسامان وسرانجام وتوانگری » معانی نزديك و با معانی‌مججازی
مان کشاد کی‌وفراخی درزند کی است » چنانکه این کلمه را با « بر که »که اسلا بمعنی‌استطاعت
مادی وئوانایی مادی است مرادف می‌آورند و« بر که ونوا > می کوبند؛ ودرفرهنگه اسدی (چاپ
آقای اقبال س ۸ ) * توانگری وساز کار وشغل مردم» معنی کرده‌اند. > « فیسی . تعلیقات تاریخ

بقیه در حاشیةٌ صفحةٌ بمد

########## v4 pdf page 380 (printed 2297)
[pdf page 380]
۷۷۹۷ ویضا
باشد وخواء صد بر که ؛ وبکسرثالك‌هم کفته‌اند. ٍ ممانی پفتح اول هم‌آمده است - و بکسراولوئانی
وید - بکر اول وسکون ثانی و دال» | مجهول نام کنابی است آسمانی باعتقاد کفرء
بمعنی کم باش د که درمقابل بسیاراست ۱ سویمعنی | هند ۲ . :
کم در برابر بیدا همست ‎٩‏ - واهر چیز عقص ویف! - بکسراول بروزن بیجا » بمعنی
را نی زکوبند مانند مازو وپوست اناروامثال آن- وید اس تک هگم و ناپیدا و باپدید کشت۳ -وکم
و بستی چام وعلاج همکنته‌اند جنانکه کرین | وب انداخته باشد۴ - و بسی بدا
«چه ویدکنم ؟» بمنی چه چاره کنم ؛ و باین و ناص و دور 0 و بمعمی ۸
۹ - امد ی کوید : « وید ,گم باشد » وید! نیز گوبند . رود کی (سمرقندی) گوید:
ای غافل از شمار چه پنداری کت خالق آفریده بهرکاری (له‌برکاری؟دهشدا)
عمری که هر تراست سرمایه وید است وکارهات بدین زاری .>
« لغت فری ص *۱۱ ۰
و هم آسدی‌آرد : ۸ وید! گم شده باشد چون وید » « لغت فری ص ۵ > [ رك : ویدا ]ظ. کله
مصحف «* ولد ؟ ومعنی‌آن «کم» ( بفتح‌کاف تازی ) است بمنی اند . ابن‌الندیم درالفهرست(چاپ
مسرص۳۳۸) درداستان گردانیدن دفاتر دیوانی‌ازفارسی بمربی‌آرد: « فقال‌له ( لسالح‌ین‌عبدالرحمن)»
مردانشاه‌پن زادانفروخ : کیف تصنم , «دهویه» و «ششویه ( ظ: پنجوبه )»۲ فال : اکتب«عشرا» و
« صف عفر». قال : فکیف نع , « وید ‎٩»‏ قال : اکتب « وایضاً > قال [ فکیف تسنح , *وند»1
قال : اکتب « اللیف »] ( سوال وجواب اخیر دراصل نیامده و ظ. لازم است ) و ا[ « وید » ( ا
« وند » ظ. ) النیف.» دیف بروزن کیس درعربی بمعنی افزونی وزیادت چیزی است«منتهی‌الارب»
و «وفد »۳ اند ( ۸ اند , شمار مجهول هم‌هست ازسه تا نه » وآئرا بعربی لیف و بطم خوانند.»
برهان ). رك : اند . ۴ ۷۵42۳ از ربشه ۷16 بممنی داستن است «وبلیامز 2۲:۹۹۳
وخود «ودا» بمعنی معرفت و داش است وآن مجموعهٌ کتابهای مقدس هندوان و متملق به آریین
برهمائی‌است‌بز بان ماسکریت و شامل چغار کتاب است : ۷648 818 ۷۵۵8 #ناژة ۰
8-۷8 54. ۸108۲۷8-۷۵۵۵ .هرهودا» عبارتست ازمجموعه‌ایاز رودها که باوزانمختلف
و در بارة خدابان متمدد سروده شده است . ۴ - « ویدا :کم شده باشد چون‌وید . دقیقی
(طوسی )گفت +
آمیرا ! جان شیرین‌برفهاام اگروید! شود پیکارعمرم(ن‌ل:ا گرویداشوديك‌با رکی‌همر)».
ورك : وید (ح۱ )۰ « لفت فری ص ۵ >.
و در تخد صحاح‌الفری آمده : « وبداکم باشد بفتح‌کاف . دقیقی گفت :
امیرا ! جان شیرین برفغام اگر وید! شود یکبار کی‌عمر.» ‏ «طاعتی».
ودر خةٌ دیگر صحاح‌الفری : « وبدا یمتی کم و ناقص . دقیقی گفت :
امیرا ۱ از برای مدحت تو شده همر عزیزم زود وبدا .>
« فرهنگه نظام > .
این لفت درجهانگیری وسروری نیز «گم‌شده » معنی شده . چنانکه درمتن لغت قری (ص ۵ ).
ولی مملوم لیست فی‌الحقیقه این جملةٌ «کم شده > دراین کتابها باید با قتح‌کاف خوانده شود با با
شمگاف ! در دخهٌ « منتخب فری » میرزا ابراهیم هم این لغت چنین معنی شده : « وید -کم
شده ». با توجه بضبط صحاح‌الفرس » نوان گفت این جمله دراسل همان «کم‌شده > بفتح‌کاف برده»
سپس فتحةکاق را شاخ دوم کاف پارسی کمان کردهآنرا «کم» بنم کاف خواندماند. « طامتی ».

########## v4 pdf page 448 (printed 2365)
[pdf page 448]
- ۳۹۰ رب هللا
هماویز ۱ « بروزن بلاغیز . بسنی ِ اسقتدیار است که ارجاسب اورا اسیر کرد درقلمهٌ
هماورد است که هم کوشش وهمتا باشد وعربان | روبین دز نگاه داشته بود۴ - و نام دختر بهمن
کقو میگویند . که در حبالةٌ نکاح پدر خود بود۴ - ولام پادشاء
همای ۲ - بنم اول واثانی بالف زاده ای که بپمایون عاغق بود و قسةٌ « همای
کشیده وبتختانی‌زده. نام مرغیست مشهوروممروی | وهمایون» مشهور است9 - و نام دختر قیصر روم
که استخوان خورد - و نام یکی از خواهران | هم هست و او زن بهرام گاور بوده ‎٩‏ - و علم
۱ - از : هم ( پیشوند اشتراك ) ۳ آویز ( آويزنده ) :
بهرهز نعره ای برز د که مگرین با کامد بمیدات هم آویز -
بزاری قهستانی « فرهنگه‌نظام».
۴ عهما (هم.) . قن : همایون . همای لفظاً بمنی فرخنده و خجته . م/(81-78
و 110-1222 بهمین معنی بیار دراوستا بکار رفته « فاب ص۳۱4 » پپلوی ۵122۴ «تاوادیا
۴ . اصلا این کلمه صفت عقاب است « قاب۱ ص ۳۱۶». ولف در فهرست شاهنامه همای را
به ۸0167 (عقاب) ترجمه و بدین ابیات فردوسی آشاره کرده است :
یکی جای دارد سر اندر محاب بچاره بر آورده از قعر آبء
نهاده ز هر چیز کنجی بجای فکنده برو سایه پر همای .
« شاهنامهٌ بخ ج ۱ص ۴۱۱۹
یکی سينةٌ شیر پاخدش جای یکی کر کس و دیگریرا همای.

۰ عاهنامةٌ بخ ج ۳ ۹۵۱ ۰۹
ور: ح۱صفحی‌بعد. اما غالباً دُرادییات فارسی‌همای‌راپرنده‌ای‌داسته‌اند فرخنده وخجسته که خوراك
او استخوان است و در افانه‌ها گونند در کشورهای قدیم هرکاه پادشاهی میمرد وجاشین نداشت
همای را بیرواز در می‌آوردند » برسر هرکس می‌نشت او را پادشاء میکردند ( غالباً اين‌وظیقه با
شاهین و باز محول شده ):

ملکا ! در ملکی فر همایست ترا نا بجاست جهان » ملك بجاست‌ترا +
« منوچهری دامغانی . دیوان صس ۱۵۹
همای بر همه مرغان ازآن شرف دارد که استخوان خوید و جانور یازاره--
« کلتان مص ۰.۳۳
کس یاید بزبر سایةٌ بوم ور ۸ءای از آجهان شود معدوم .
و رك : داثرةالمعارف اسلام : 11082 . « کلستان ص ۹۷۰ .
۴ - در فروردینبشت اوستا دختر کی گشتاسپ (خواهراسفندیار) 111-17282 خوانده
شده است «فاب۱ ص۳۱۶ » «پورداود » بشتها۱ ص۲۸۹ ۰ ۱۳۹۱ ورك : مزدیناس۳۵۹ و۳۹۳.
ی #خمانی (ه.م ) ر4 : شاهنامهٌ بخ ج ‎٩‏ مس ۱۷۹۵ بیمد » و ر4 : همای آزاه .
* - منظومه‌ای از خسهٌ خواجوی کرمانی بنام «همای و همایون» است درشرح داستان
عاشقانهٌ آدو » وآن مثنویی است در بحر منقارب که بال ۷۳۲ در بفداد بنظم آورده است. ر4 :
دکنر شفق . تاریخ ادبیات مس ۰۳۱۳
۹ - دختر قیسر همآیون رای هم همایون و هم بنام «همای».
نظامی کنجوی « هفت پیکر چاپ آرمغان صس ۷۸ *.

########## v4 pdf page 484 (printed 2401)
[pdf page 484]
-۲1۱- حوبدك
ناح یکمرد میباشند و هريك مر دیگریرا هوو | وکسر ثالی است وآن کلیمی باشد یشم آ کندم
خواشد . پمنی‌پرپشم کهآبرا بردور کوهان‌شترد رآوزند؟ .

هوی يم اول وسکون ثالی‌وتحتالی» هوید)۲ يم اول بر وزن سوبداء
بمعنی ترس وبیم باشد۹ . بمعنی ظاهر و روشن و بین باشد بعتی در تهایت
هوید < بم اول وفتح ثالی وسکون | ظهورد-
تحتالی ودال» جهاز شتر را کوبند وآن بمنزله همویدل4؟ -« بنم‌اولرفتح نای‌وسکون
پالان اوست ؛ و بح ی گوبند این لغت بفتح اول | نحتالی ودال بی‌قطةٌ مفتوح بکاف زده »یکی از
۹ - هوی (80,88)کلمهٌ افضوس است :
همه چشم پرآب ودل پر از هوی به طوی سپهید لمودند رزوی .
فردوسی طوسی«فرهتگه نظلم».
وکلمهٌ تنبیه است :
هان‌مردا هوی وهان جوانمردا هوی مردی کنی و نگاه داری سر کوی.
منسوب بابوسمید ابوالغیر «فرهنگه نظام».
۴ - برآوردم زمامش(شتر) تا بناگوش . فرو هشتم هویدش با یکاهل -
«منوچهری دامفانی. دیوان ص*۴۵.
۴ - از: « (* قا۵] اوستایی بمعنی خوب )۳ ویدا (* پیدا ) مرحوم بهار در حواشی

مخطوط خود برلغت فرسی اسدی چاپ مرحوم‌اقبال صه عمین گونه آظهار عقیده کرده‌اند . قی +

کردی 3818 (ظاهر» بدیهی) «ژابا ص۱۹۷*. #هوبداء سخت پیدا بود , چنانکه عنصری (بلشی)

گوید :

درشتی دل شاه وارمی دلش ندانی هویدا کنی حاصلش .»
«لفت قری ی٩۹».‏
ور4:صعاح الفری نسغهٌ طاعتی . ارچ جهانگیری «هوبديك» آورده کوید: « نام یکی از

پیخوایان ملحدان بوده که حکم خاقالی فرماید +

او کیست که با روان تاريك باشد ‏ بمثات هویديك .>

بوستی این نام را 110۳2116 ضبط کرده باستناد فولرسی 1 ۰ 8۱۶۷۰ و بکتاب ,57016861

2۰ .410 ول[ ۲۳01۳۵0۸۵۶ ارجاع کرده «یوستی . نام نامه مس *۱۸* اشپیگل درکتاب

مزبور («مان صفحه) دربحث از كلمهٌ اوستابی 80813542 (که طبقه‌ای ازدروجان [ ده غیرستان»

پیروان کیش باطل] هستند. رك: پوستی. فرهنگه اومتا ص۳۲۸) کوید: من اکنون ارجیح‌میدهم

که کلمهٌ مز بورعنوانی‌باشد برای انگره میئو (اهریمن). اسپند,ارجی مقدم, این کلمه را «زبانار»

(مضر) تعبیر میکند واسپندبارجی موخر آیرا 1108068 با ۵۵۷1086 (رك: فرلری . هویدك)

میداند که شانه‌است برای تشخیص بی دینان . » همکن امت احتمال داد ۶ عوبد4 » من

مسحف « بوند که » «لع33۷2848 پهلوی ( در ارءنی 0۷28426 ) بمعنی کامل * بوندی

8 -* بوند, * بوندباشد, نام یکی‌ازمالويهٌ روم که با کیش رسمی مانویه مخالفت کرد و او

پیشرو مزدك بود. رك: کربتنن. ساسان ص۳۳۷ ببعد؛ ترجمةٌ آن طبع دوم یس۳۹۲ بیعد؛ ایا

کربستنسن . ترجمهٌ تاریخ سلطنت قباد وظهور مزدك ص۲۰۲ بیمد. درهرحال خاقانی این اسم وا
بقیه درحاشيةٌ صفحةٌ بمد
```


## [2026-09-14T03:14:16.742Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for lf in 174 194 205; do echo \"########## v2 leaf $lf (printed ~$((lf+543)))\"; awk -v n=$((lf+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -45; done",
 "description": "Extract BQT vol2 leaves for pages 717,737,748"
}
```


### [2026-09-14T03:14:17.887Z] TOOL RESULT

```
########## v2 leaf 174 (printed ~717)
   ‫‪۷۱۹‬‬                                                                                ‫تنس‬

‫شاخ آن مرغ‌است وازآن زهگیر تراشند ودستةٌ‬        ‫از آنجاآورند ‪ -‬ویمعنی فریبنده همبنظر آمده‬
‫‪.‬ویند خاصیتش آست که اکر‬    ‫کارد لیزسازند گ‬                                            ‫است ‪#.‬‬
‫در جابی چیزی مسموم با طعامی بزهر آغشته‬          ‫ختثیر = بابای ابجد بر وزن فلندر ‪۰‬‬
‫بیاورند اآزن شاخ علامتی ظاهرمیشود » و بسنی‬      ‫مقلی راکوبند که لاف توانگری زند وخود را‬
‫گفته اند شاخ ماراست و هر گاه ازعمر مارهزار‬       ‫ورعکس هم بنظر آمده است‬
                                                                      ‫مالدار وانماید » ب‬
‫سال بگذردشاخ برمی‌آورد » وبعضی گوبند شاخ‬              ‫یعتی توانگری که شکوء مفلی کند ‪# .‬‬
‫افعی است وبسضی دبگر کویند شاخ‌ماهی‌وال (‪)۱‬‬      ‫خقو د منم اول و الی بواو رسیده »‬
‫است * وسمتی دیگرگفته‌اند دندان جانوری‌است‪:‬‬
                                                 ‫وسنی‬
                                                    ‫شاخ گاوی است که درملك چین‌مساشد *‬
                              ‫اله (‪ )۲‬اعلم‪. ۱‬‬     ‫هگ‌راند‬
                                                        ‫گجفمتدی‬
                                                              ‫کوبند شراکخدکن‌است ‪ ۰‬و‬
‫‏‪ a‬بروزن بروانه‪ .‬حامه ولسای‬   ‫حتوانه‬
                                                ‫که در مابین ملك چین و زنگبار ملکی است‬
              ‫پشمينة دروبتان وفقیران باشد ‪.‬‬     ‫خراب ودرا نجامرغی میشود بغایت بزر که واین‬

                              ‫() چك‪ .‬چش ‪ :‬وال ‪.‬‬            ‫(‪ )۱‬چك » چش ‪ :‬زال ‪.‬‬
 ‫‪ ۱‬بیرونی در « زکرالختو » آرد ‪ :‬ک«نت سالت‌الرسل‌الواردین من قتای‌خان عنه فلم‬
  ‫نفی‌الکتب‬
          ‫اجد عندهم سبباللرغبة فيه غیرالعرق من‌السم و اله عظم جبهة شور » و هکذا کر‬
  ‫بزبادة ان هذا الثور کون بارش خرخیز » و فحن‌تری له من‌الفلظالزائد علی‌عرض‌الاصبعین مابکاد‬
  ‫یستحیل معه‌ان‌بکون عظم جبهة مع‌صفرجثة ثبران التركك وسیرالفرن اولی به‌ولوسدق ماقیللعان‬
 ‫جلبهالی الاوعال من خرخیز اولی‪,‬هلانهم اليه‌اقرب ولم بجلب من‌العراق وخرامان وقدقبل‌فیه ایض‬
  ‫مائی وسمی فلا مائاً ‪« ۰...‬الجماهر ‪ ۹۰۲۲ - ۸۰۲‬ونظراین مطالب درصيدنة‬          ‫ن‬
                                                                              ‫کهةدکر‬
                                                                                   ‫انه جب‬
  ‫بیروتی آمده ‪ .‬ارلكج‪:‬ماهر ‪ ۸۰۲‬ح ‪ . ۲‬دانشمندان قول اخیر را صحیح دانته اند » چه‬
 ‫مکنوع‌ماهیی است که بفراسوی ‪ 12۷722‬و بانگلیی ‪ 12517721‬و بلمآانی ‪ 13۷۲4‬کوبند‬
  ‫که از اسکاندیناوی مأخوذست و در اصطلاح علمی آنرا ‪ 8000201۷1 50۲6608021‬کوبند‬
  ‫واز نوع فطاس ‪ ( 5602060‬وابته بنوع وال [ رجوع به وال شود ]یابال) است‪ .‬ربن آندرفك‬
  ‫اعلی دارای دودندان است که بطور افقی درازشدموطول دندان‌چپ نا ‪ ۲‬متر و *‪ ۵‬سالتیمتر میر‪-‬د‬
  ‫ودیگری کوتاه‌میمالد ‪ .‬دندان دراز مزبورشبیه بشاخ است ‪ .‬این‌ماهی‪,‬وال قطب شمالی است وندرة‬
   ‫بقبه در صفحهُ ‪۷۱۷‬‬
                 ‫‪ #‬خجتن ‪ -‬شم اول و فتح دوم » رك ‪:‬ص پانزده از مقدمة کتاب حاضر ‪.‬‬
  ‫‪ #‬خحتنی ‪ -‬منسوب به «ختن؟ ‪ -‬زبان ختن ‪ .‬رك‪ :‬ص پانزده ‪ -‬هفده کتاب حاضر‪ .‬برای‬
                  ‫بوشتن زبان ختنی «خط کوپتای ‪ 46110‬آسیای م رکزی» بکار میرفت ‪ .‬رك ‪:‬‬
           ‫‪David Diringer ‘The Alphabet. London. 1947 .p. 350.‬‬

                                                                          ‫قه اصزفحهٌ ‪۵۱۷‬‬
   ‫‪« - ۵‬ختلان ناحیتی‌است (ازحدود ماوراوالنهر) اندرمیان کوههای بزر گت بواآدان‌وبسیار‬
   ‫کشت وبسیارمردم وهمت‌های‌فراخ و پادشای وی ازملو که‌اطراف‌است ومردمان این ناحیت مردمان‬
########## v2 leaf 194 (printed ~737)
    ‫‪۷۳۹‬‬
‫را‬    ‫مدور‬    ‫بز رگ‬    ‫زا کوب شوم ارا‬                   ‫ومع‬    ‫کرمان بیز ند وبخورند وارد نیزسازند ونان هم‬
                                               ‫خت ‪۲‬‬                                                 ‫يزنك ‪.‬‬
‫‪۰‬‬     ‫دوم‬     ‫بم خای‬     ‫=‬   ‫خر گاه خصر‬
                                                               ‫خرك = بر وزن فلك » مخفف خارك‬
                                ‫کنانه ازآسمان است‬              ‫است» وان نوعی ازخرهای خشك باشد » وبعضی‬
‫سیز سرخرگاه‌سزگاو پشت‬                      ‫گراه‬
                                              ‫خ‬                ‫مور رما تت که خرمای نارسده باشد‬                ‫و‬
          ‫بمعنی خر گاه خضراست که آسمان باشد ‪.‬‬                  ‫= ومصفر خر‬       ‫رخوانند‬
                                                                                      ‫ببسان‬
                                                                                          ‫وآترابعضی از عر‬

‫خگراه قمر ‪ -‬کنابه از هالهباشد‪.‬‬                                  ‫هم‌هت ‪ -‬وچوبکی باشد که برروی طنبوروعود‬
    ‫وآن دایرهء‌ایست که‌بعضی اوقات ازبخار بهم هرسف‬
                                                               ‫و کمانسه(‪ )۱‬وامثال آن کذارند وتارها رایرهالای‬

              ‫زآندایره منگردد ‪.‬‬
                              ‫چنانسه ماهمرک‬
                                                               ‫آن کشند ‪ -‬و ام دهی استت از ولات فاری در‬
                                                                ‫ییراز ‪ -‬و تخته‌ای ناشد که‬
                                                                                        ‫ش‬                  ‫خر‬
                                                                                                            ‫س ف‬
                                                                                                              ‫هشت‬
                                                               ‫وناه کاران را برآن خوابانند و درهٌ‬
                                                                                                ‫مجرمان گ‬
‫اول را‬       ‫و آسمان‬     ‫است که خرمن ماه باشفد —‬
                                                               ‫و چوییرا نز گویند که استادان‬          ‫تادیب زتند ‪-‬‬
‫نکیوزیند ‪ -‬وکنابه از خط عذار مهوشان هم‬                         ‫هیمه در زر آن‬         ‫‪CA‬‏‬       ‫کنده شکن در وت‬
                                                    ‫‪۰‬‬     ‫هت‬
                                                               ‫کذار دوش کنند ‪ -‬وسه چوبه‌ای باشد که بربای‬
‫از | مات‬         ‫کنابه‬       ‫خر گاه میا ‪-‬‬                       ‫اطفال دهند‬     ‫هر کدام غلطکی صت کدف و اٹ‬
                                                               ‫ای باشد که هر‬ ‫‌مه‬‫هو‬‫ی‪-‬‬  ‫اند‬
                                                                                        ‫یموز‬
                                                                                           ‫تن بیا‬ ‫فاه‬
                                                                                                    ‫ترار‬
    ‫خر گر = بروزن زگر»بمعنی خرمن‪-‬‬                               ‫دوسرکار گاهرا بربالای گآذنارند ونةش دوزی‬
                                         ‫وهالةٌ ماه باشد ‪.‬‬      ‫گولایتون دوزی کنند ‪ -‬ومه‌یایه‌ای که زر گران‬
    ‫وسکون‬      ‫فتح اول وحم کاف‬
                             ‫‪.‬بف‬     ‫۔‬    ‫کس‬    ‫خر‬
                                                                ‫بش خود گذارند وچیزها را بربالای‌آن سوهان‬
    ‫از مردم بیعقل وابله‬                  ‫ثانی وسین بی‌نقطه‬      ‫کاری کنند و حمچنین بنابان در زیر پای خود‬
                                            ‫واحمق باشد ‪۰‬‬        ‫گذاشته کچ کاری و کچ بری سقف ودیوار خانه‬
                                                                ‫"نند ‪ -‬و چزیکه بدان دیوار رخنه کنندن ‪-‬‬
                                                                                                     ‫ک‬
    ‫خر کش = بطم کاف و سکن شین‬
########## v2 leaf 205 (printed ~748)
  ‫خس‌در دهان گرقتن‬                                                                              ‫‪1‬ع‬
                                                                                                 ‫‪۷‬‬


 ‫لباسی باشد که درویشان وفران پوشند وازآن‬              ‫جست ه بفتح اول بروزن مست» ماضی‬
 ‫یشمها وموبها اوبزان باشد‪ - ۷‬وخرقه ایرا لیز‬           ‫حستن و آزرده ساختن باشد بعنی مجروح کرد‬
 ‫کونند که از بارچپای الوان دوخته شده باشد ؛‬            ‫ویند‬ ‫وآزرده ساخت ‪ - ۱‬ورنگ ولون را نکیز‬
                       ‫وفتح اول هم آمده اس‬            ‫ویمعتی تفع وفایده هم‌هست ‪ -‬وبضم اول بمعتی‬
                                                      ‫حامه را لیز‬    ‫و آستن‬        ‫فرار و ارام باشد ‪-‬‬
 ‫خستو نه بضم اول بر وکزلنگونه ‪.‬‬
                                                                                               ‫گفتها ند‬

                                            ‫باشد‬       ‫خستر؟ ‪ -‬برورن کفتر‪,‬حثرات‌الارض‌را‬
 ‫وزن دسته ‪.‬‬   ‫اول بر‬    ‫حسته ‪ -‬بفتح‬
                                                           ‫کوند همچو مورو مار وموش وامثال آن‬
 ‫ثال آن باشدھ ‪-‬‬
              ‫ووزاردم]‬     ‫استخوان‌خرما وش‬
                     ‫لفتوالو‬                          ‫خستی ‪ = ۲‬بپروزن بستن بمعنی‌ مجر وج‬
 ‫ومجروح وزخم خورده وسماررا لیزکو ند ‪ 6‬ہے‬                              ‫کردن ‪ -‬ومجروح شدن باشد ‪.‬‬
    ‫مندخ‪-‬فوف‬
           ‫زومینی که آنرا شریکارده باش‬                ‫حستو ت بفتح اول بروزن بدخو » دانۀ‬
 ‫‪ -‬ونم اول بمعنیهی‬     ‫خاسته وبرخاسته هم هت‬
                                                      ‫میوهارا کوبند همچودانةٌ زآرلدو وشفتالو وخرما‬
                           ‫وبنورة دیوار باشد ‪.‬‬
                                                      ‫و مانند آن ‪ - ۴‬و م اول ناممکی از اکابر‬
 ‫حسته نك = بابای ابجد بروزن هرزه‬                      ‫وبزرکان چن است ‪ -‬واقرار واعتراف کننده را‬
‫لیزگفته‌اند(‪ -)۱‬وبمعنی‌جانورخز ندحهمبذظر آ مده خند ‪ .‬پارچه‌ای کروایند کهچون دستی بایایی‬
 ‫شکته باشد بدان بندند ‪ -‬و کی را تیز گوبند‬                                                      ‫است ® ‪.‬‬
 ‫که زخم را و(‪ )۲‬دست ویای شکستهرا می‌بندد‪-‬‬             ‫خستوان‪ = 1‬یبنرماووزلن‌استخوان »‬
 ‫وهرچیز که انرابرزخ‌بندند خواه پلرچه باشد‬              ‫افرار و اعتراف کنندکان و معترف شکدانرا‬
                                     ‫خواه هر هم‪.‬‬                                     ‫گویند ‪.‬‬
  ‫ان گر فتی‪ -‬بسنی‌خس‬
                   ‫خدسهدر‬                              ‫حستو انه = پم اول‌بروزن خرواله»‬

                            ‫‪ -:‬را و‬     ‫(‪)۲‬چك‪ .‬چش‬                   ‫)‪ (۱‬چك ‪,‬چش‪ :‬کونند ‪۳‬‬


                ‫«خراستر» (ه‪.‬م‪ = . ).‬خرفتر‪.‬‬            ‫مخفف‬
                                                         ‫‪۴‬‬               ‫رك ‪ :‬خستن ‪.‬‬      ‫‪۱‬‬
   ‫‪ - ۴‬هلوی ‪ 08152۷5‬ک(وفتن ‪.‬كتك زدن) «ناوادیا ‪ ۷۹۱2‬ورگ ‪ :‬اسفا! ‪:‬ص‪. ۲۸۱‬‬
    ‫هه بهلوی ‪6-4۵1‬‬               ‫‪.‬‬    ‫ورك ‪ 1‬استخوان‬    ‫هته(ه‪.‬م‪.).‬‬    ‫چ‬   ‫(ھ‪.‬م‪(.‬‬     ‫و‬     ‫‪۴‬‬

                                                            ‫‪۲ : ۱‬ص‪٩۸۱٥‬‏ رك ‪ :‬خستوان ‪:‬‬            ‫«اسفا‬

               ‫کرچه کوا تخواهندازختو‪.‬‬                      ‫بقرنل اوکوا کنراند دل‬
```


## [2026-09-14T03:14:31.888Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    for w in ['خجسته','خرم','خسرو','خسر']:\n        if w in p:\n            print(i, i+545, w, p.count(w))\nEOF",
 "description": "Locate خجسته/خرم/خسرو in BQT vol2"
}
```


### [2026-09-14T03:14:33.023Z] TOOL RESULT

```
11 556 خرم 1
22 567 خرم 1
23 568 خرم 2
24 569 خرم 2
29 574 خسرو 2
29 574 خسر 2
31 576 خرم 1
32 577 خسر 1
36 581 خرم 1
37 582 خسرو 1
37 582 خسر 1
41 586 خرم 4
43 588 خرم 1
44 589 خسرو 2
44 589 خسر 2
56 601 خرم 1
57 602 خسرو 1
57 602 خسر 1
60 605 خرم 1
63 608 خرم 1
64 609 خرم 1
84 629 خرم 1
84 629 خسرو 1
84 629 خسر 1
92 637 خرم 3
108 653 خسرو 1
108 653 خسر 1
117 662 خرم 1
118 663 خرم 2
125 670 خسرو 1
125 670 خسر 1
127 672 خسرو 1
127 672 خسر 1
141 686 خرم 1
149 694 خرم 1
151 696 خرم 1
152 697 خرم 1
156 701 خرم 1
162 707 خسرو 1
162 707 خسر 1
169 714 خسرو 1
169 714 خسر 1
170 715 خرم 1
179 724 خرم 1
182 727 خسرو 2
182 727 خسر 2
185 730 خرم 2
187 732 خسرو 1
187 732 خسر 1
188 733 خرم 1
190 735 خرم 1
191 736 خسر 1
192 737 خرم 1
194 739 خرم 3
195 740 خرم 3
196 741 خرم 14
197 742 خرم 8
198 743 خسرو 1
198 743 خسر 1
200 745 خرم 1
201 746 خرم 2
201 746 خسرو 1
201 746 خسر 1
205 750 خرم 2
206 751 خسرو 8
206 751 خسر 11
207 752 خسرو 6
207 752 خسر 7
213 758 خجسته 1
214 759 خرم 2
217 762 خسرو 1
217 762 خسر 1
221 766 خرم 1
226 771 خسرو 1
226 771 خسر 1
227 772 خرم 1
241 786 خسر 1
245 790 خسرو 1
245 790 خسر 1
252 797 خسرو 1
252 797 خسر 1
253 798 خسرو 1
253 798 خسر 1
257 802 خسرو 1
257 802 خسر 1
258 803 خرم 1
269 814 خسرو 1
269 814 خسر 1
270 815 خسرو 1
270 815 خسر 1
283 828 خرم 1
298 843 خرم 3
327 872 خرم 1
332 877 خرم 2
335 880 خرم 2
337 882 خسرو 1
337 882 خسر 1
362 907 خرم 1
369 914 خسر 1
376 921 خرم 1
388 933 خسرو 1
388 933 خسر 1
389 934 خرم 1
391 936 خرم 1
394 939 خسرو 1
394 939 خسر 1
404 949 خرم 1
405 950 خرم 1
411 956 خرم 1
427 972 خرم 1
444 989 خرم 1
449 994 خسرو 1
449 994 خسر 1
458 1003 خرم 1
473 1018 خسرو 1
473 1018 خسر 1
477 1022 خسرو 1
477 1022 خسر 1
478 1023 خسرو 1
478 1023 خسر 1
482 1027 خرم 1
503 1048 خرم 1
523 1068 خسرو 1
523 1068 خسر 1
528 1073 خرم 1
537 1082 خسرو 1
537 1082 خسر 1
545 1090 خرم 1
555 1100 خسرو 1
555 1100 خسر 1
556 1101 خسرو 1
556 1101 خسر 1
559 1104 خسرو 1
559 1104 خسر 1
565 1110 خرم 1
572 1117 خسرو 1
572 1117 خسر 1
573 1118 خرم 1
575 1120 خرم 1
588 1133 خسرو 1
588 1133 خسر 1
589 1134 خسرو 1
589 1134 خسر 1
591 1136 خسرو 1
591 1136 خسر 1
593 1138 خجسته 1
609 1154 خسرو 1
609 1154 خسر 1
611 1156 خرم 1
612 1157 خرم 1
617 1162 خسرو 1
617 1162 خسر 1
618 1163 خرم 1
627 1172 خرم 1
636 1181 خسرو 1
636 1181 خسر 1
639 1184 خرم 1
648 1193 خسرو 1
648 1193 خسر 1
671 1216 خرم 1
672 1217 خسرو 8
672 1217 خسر 8
678 1223 خسرو 1
678 1223 خسر 1
```


## [2026-09-14T03:14:42.719Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for lf in 196 206 207; do echo \"########## leaf $lf\"; awk -v n=$((lf+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -12; echo \"...FOOTNOTES...\"; awk -v n=$((lf+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | tail -18; done",
 "description": "Print BQT leaves 196,206,207"
}
```


### [2026-09-14T03:14:44.388Z] TOOL RESULT

```
########## leaf 196
   ‫و‪۳۷‬‬                                                                                            ‫خرمای ابوجهل‬

 ‫خرم روز ‪ - ۴‬نام روزهشتم است‌از‬                        ‫است که ماه دهم‌باشد ازسال شمی وبودن فت|اب‬
 ‫هرماه شمسی‪ .‬کوبند ملوك عجم درین روزلیکن‬              ‫در برح جدی ‪ - ۱‬ونام روز هشتم است ازهرماه‬
                                ‫درماه د‬
 ‫کیه‌ان ماه دهم است از سالهای شمی‬                     ‫شمسی » و بنا برقاعدهکلیه که نزد فارسان مقرر‬
 ‫جشن کردندی‌وجامپای سفید پوشیدندی وبرفرش‬              ‫است که (‪ )۱‬نام ماه وروز (‪ )۲‬موافق آبد عید‬
 ‫نشتندی ودربانر! ءنع کردندی وبار عام دادندی‬           ‫باید کرد دراین روز عید کنندوجشن سازند ‪٩‬‏ ‪-‬‬
 ‫ویامور رعیت مشفول شدندی وامرزعان ودهقانان‬            ‫نام مرغزاری‬                ‫رضم اول وسکون انی بی‌تشدید ‏‬
  ‫بمالوك بر سر يت خوان نشتندی وچیزی‬                  ‫مطلبی که‬             ‫است» در آ نجاکوهی‌هم هست که هر‬

‫خوردندی وبمدازآن هر عرضی )‪(٩‬‏ ومدعایی که‬              ‫عرض کنند جواب آبد ‪ .‬کویند چون سکندر‬
...FOOTNOTES...
                                                                       ‫تت ب‬
                                                                          ‫ف اس‬
                                                                             ‫گنن‬
                                                                               ‫« چ‬
                                                                                 ‫‪۴‬‬
                       ‫چونکه بستندخرمکت بگلو بر ‪.‬‬             ‫‪ - ۴‬ترسم چشمت رسد که مخت خطیری‬
                       ‫»‪.‬‬   ‫‪۷‬رع‪۵‬‬
                               ‫‪۲‬ت ف‬
                                  ‫منجيك‌ترمذی‪« .‬لغ‬
                        ‫‪#‬خرها ‪-‬بنم‌اول‪ .‬پهلوی ‪ « ۷207۲2‬ناوادیام‪ < > ۵۱:۲‬اونوالا‪»۷۳۵‬‬
                        ‫(‪« ۷)20۳]21‬تاوادبا ‪ ۷۹۱‬پازند ‪ . 801۲11۳‬ارمنی ‪« ۷20۳۳2‬اسفاا ‪۲ :‬ص‬
                         ‫‪۷‬‏ ‪ Phoenix 276110021‬کل کلاب‪« »۱۹۲‬نابتی ‪« ۰۸۱‬ستوده ‪۵4‬‬
                       ‫ميو درخت خرمابن » درختی از طابقهٌ نخیلات از محصولات گرمیری که‬
                       ‫دارای‌میوه است‌شیرین ولذیذ موسوم بخرما ودرجنوب ابران فراوان بعمل آید‪.‬‬
                                     ‫ببعد ‪.‬‬   ‫رك‪ :‬کل کلاب ‪ ۱۹۲۷‬وفرهنك درخت خرما روستانی ص ‪۹۲۵‬‬

   ‫درخت خرما‬                              ‫‪ #‬خرمدان ‪ -‬بش اول و فتح دوم رك ‪ :‬چرمدان ‪.‬‬

########## leaf 206
  ‫با]س‬
     ‫ی‬


‫»ابه از‬
      ‫خسرو اقلیم چهادم کن‬                      ‫بدهن گرفتن است ککنهایه ازعاجزشدن وزیشهار‬
                      ‫آفتاب عالمتاب است ‪.‬‬                     ‫‪۱‬‬                    ‫خواستن باشد ‪.‬‬
‫حسرو انحم = بمعنی خرو اقلم‬                     ‫حسره بفتح اول و انی بر وزن شرر »‬
     ‫چهارم است که خورشید عالم|راست (‪.)۱‬‬        ‫و آن آیی است که در زمستان‬             ‫شخد‬
                                                                                       ‫اب‬‫بعنی‬
                                                                                            ‫بم‬
 ‫تا روزن ‪:‬کهادنی‪:.‬‬        ‫خسروانی‬              ‫مانندشیه‌بندد ‪ - ۱‬ویم اول و انی » پدر زن‬
...FOOTNOTES...
                                                      ‫چوآفتاب توبی‌برهمه جهان تانان‪.‬‬

                                                  ‫«هعزی نیشابوری ‪:۸۳۵‬‬
                                               ‫از دساتدر‬   ‫‪ -. ۴‬به‌عنی آخیر ما‬
                                               ‫مراد‬    ‫®‬              ‫‪.‬‬   ‫>‬   ‫دانر‪۳‬؟‪۲‬‬   ‫‪ ۵‬فرهنك‬


                                                      ‫ارك خسرر ‪:‬‬                     ‫کیطسروست‪.‬‬
                                                 ‫از‪ :‬خرو ان (جمع) ‪-‬ی(نبت) ‪.‬‬                   ‫*‬
                                               ‫خسروانی گرد‬        ‫‏‪ _ A‬همه نا چو دره‌های‬
                                                 ‫کنب وار‬
                                                       ‫ارم تابد غر و‬
                                                 ‫فرخی سیستانی ‪« .‬رشددی»*‪.‬‬
                                                   ‫‪ #‬خسرواول رك ‪ :‬انوشروان ‪.‬‬
                                                ‫‪ #‬خسرو دوم حرو هرو هر ‪-‬پس‬
                                                ‫عرمز وچپارم ونوادة انوشروان» شاهنشاه ساسانی‬
       ‫خسر وروز درشکارگاه‬                             ‫‪(e.1‬‬        ‫(‏ ‪- ۰۵‬‬

########## leaf 207
  ‫جسوردن‬                                                                                                       ‫نله‬
 ‫خساث ‪ -‬بفتح اول وانی وسکون‌کافی»‬                                              ‫همجو خم خسروانی وامثالآن ‪.‬‬
 ‫خس وخاشاك وخاری‌باشد سه گوشه ‪-‬وخارهای‌سه‬                      ‫خسرو چهارم سریر ‪ -‬کناب‬
 ‫کوشهرانیز گوبند که انزدآهون‌دسرازسررامدشمن‬                                    ‫افزتآاب است باعتبار فلك چهارم‬
‫گذارند ودراطراف وجوالب حصار وقلعه ریزتلد‬                     ‫یه است از‬       ‫خسرو خکاونرا‪-‬‬
 ‫وبضم اول مطلق وقت رکاوبند اعم ازصبح وشام‬
                                                                ‫خورشید ‪ -‬ویادشاه مغرب را نیز گوبند ‪. ۱‬‬
‫زته‌اند ‪ -‬وبکر‬
             ‫وغیره ‪ -‬وتأخیرودرنگه رائیگزف‬
                                                               ‫حسر و داد وه رستنی وداروبی باشد‬
  ‫تکرهاکل‬
        ‫آشد‬
...FOOTNOTES...
                                     ‫وغله باشّف ‪۰۱‬‬                                                             ‫خوانند ‪.‬‬


                                                                            ‫(‪ )۱‬چك » چش ‪:‬کافشه ‪.‬‬

   ‫‪ ۳‬ك مراد (اختمارات‪,‬دیعی) است ‪ .‬رك‪ :‬ص‌هشتاد وشش‌مقدمه‪.‬‬                            ‫‪۰‬‬   ‫خاور‬     ‫رك‪:‬‬   ‫_‬   ‫‪۱‬‬



           ‫صح نختن‌نمود روی بنظار کان‬                              ‫‪- ۴‬آمد بانگه‌خروس‌موذن میخوارگان‬
  ‫روی_بمشرق نهادخسروسا رگان‪...‬‬                  ‫که بکتف برفکندچادر (ب رگرفت‌جامة) بازارگان‬
      ‫‪ ۵‬منوچپری دامقالی ‪٩ ۵6۱‬‏ ‪.‬‬
                            ‫دانه ‪.‬‬    ‫‪ :‬خك‬    ‫رك‬    ‫_‬    ‫®‬                 ‫بیت‬
                                                                             ‫د‪+‬‬‫(رو‬
                                                                                 ‫‪ ۴‬از ‪:‬خ‬
  ‫‪ _ ۸‬لغتی‌درخز نده (ھ‪.‬م‪(.‬‬             ‫‪.‬‬   ‫_ رك ‪:‬خك‬            ‫‪۷‬‬        ‫‪ - ۱‬مصحف «خدکامار» («‪.‬م‪.).‬‬
                                            ‫خسودن‬       ‫رك ‪:‬‬        ‫‪۶‬‬              ‫‪ ,‬خنوره ‪.‬‬       ‫رك ‪ :‬خر‬        ‫‪-‬‬   ‫©‬
```


## [2026-09-14T03:14:55.780Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"#### leaf 176 (printed 717)\"; awk 'BEGIN{RS=\"\\f\"} NR==177' BQT_v2_pages.txt | head -50",
 "description": "BQT leaf 176 = printed 717"
}
```


### [2026-09-14T03:14:56.987Z] TOOL RESULT

```
#### leaf 176 (printed 717)
 ‫ضا‬
  ‫با سوختن و راه رفتن در دست وایعاو‬                            ‫خجنك = نماول وفتح ثانی سوکون‬
                                                              ‫نون ودال ابجد ‪ 0‬نام قصبه‌ایت درماوراءالنهر که‬
                                         ‫‪.‬‬   ‫بهم رسد‬
                                                          ‫‪۲‬‬                              ‫مولد کمال است ‪٩‬‏ ‪:‬‬
‫اول و انی بتحتانی‬
  ‫»|‬    ‫=‬    ‫‪۷۳1‬‬
                            ‫حجیر "‪۰‬یکر‬
                                  ‫‪۴‬‬          ‫‪2‬‬


                                                               ‫_ بن اول و ثالی» در نذه است‬        ‫خجی؟‬

                                                              ‫گویند‪.‬‬   ‫که لآرا چکاو کے خوانند و بعربی قبره‬
‫وجمیل وخوش صورت وصاحب حسن راگویند ؛‬
                          ‫ویضم اول هم آمده است ‪1‬‬              ‫خجو له بکر اول و فتح ثانی و لام‬
                                                              ‫وسکون واو »آبله گروانندکه ببب کارکردن‬


                                                   ‫بیان ششم‬
            ‫درخای نقطه دار ‪ ۳‬دال بی نقطه مشممل بر شانزده لغت و کنات‬

 ‫‪-‬دوای؟ جم اول ‪ ۰‬نام ذات | وصاحب ومالك را نگیوزبند ؛ وبا ذال نقطه‌دار‬
                                                                    ‫خداً خ‬
                                      ‫بارتمالی است همچو الهواله ‪ -‬و مخقف خود؟" | هم خوانده‌اند ‪.‬‬
                                                                                              ‫‪1‬‬




                                                   ‫(‪ )۷‬چك‪ .‬چش‪ :‬جوئی‪.‬‬               ‫(‪ )۱‬خم‪ -: ۱‬و‪.‬‬
  ‫روزه راه‬         ‫ده‬   ‫‪ ۰‬من آن و ‪-‬مرقند‬         ‫‪ - ۱‬شهری مشپور بماوراء النهر بر ساحل سبحون‬
  ‫در ‪ ۱4‬درجه و ‪ ۳۲‬دققهة‬               ‫ت‬
                                      ‫س)‬‫اوس‬
                                          ‫است « ممجم‌البلدان ‪ :‬خجندة » و اکنون در ترکستان (ر‬
      ‫‪ - ۴‬ظ‪ .‬مصحف«چفو»‬          ‫عرض شمالی و ‪۸٩‬‏ درجه و‪ ۲4‬دققة طول‌شرفیه ضمیمهةٌ معجم البلدان»‪.‬‬
  ‫بهلوی ‪rhic‬‏ ‪( uh -‬از ‪ :‬هو (خوب ) ‪٣‬‏ چهر(اصل نژاد ) ‪.‬‬                            ‫هرژ=ر‬
                                                                                      ‫هج‬          ‫(«‪.‬م ) ‪= ۴‬‬
   ‫اوستا_‪-»3601)1‬ل‪0‬ا«بارتولمه ‪۱۲۸۱٩‬‏ نبیر گے ‪»۹۰۱‬طبری ‪( ۲1[06‬خوش» خوب‪ .‬زیدا) «واژه‌نامه‬
  ‫‪ .‬دامفالی نیز ×‪٣[0‬‏ ‪ ,‬شهمیرزادی ‪7[1205‬؛ لفة نيك نژاد ‪ .‬خوب اصل و مجازاً بمعانی‬                            ‫‪۳‬‬
  ‫‪ ۴‬ب۔هلوی متأخر ‪: . ۷2۸۵۷۲‬هلوی اشکانی‬                                    ‫مکقور در متن آمده ‪ .‬رك‪ :‬هزیر ‪.‬‬
  ‫بازند ‪« 102۷‬هوبشمانس ‪4۵‬ج » « مسینا ‪. » ۲ : ۹۳۱‬بعضی ابن کلمه را از‬                                 ‫‪007‬‬
   ‫اوستابی_‪ )# 212210(, 6 ۵۷5 3/2010-‬مشتق دانسته اند ونولد که بحق دراين وجه اشتقاق‬
  ‫شکكرده » چون خدای فارسی و خواتای بهلوی بکلمةٌ ‪_ayÃtaWX‬‏ ‪ °‬با ‪o 2002802۷01‬‏‬
   ‫‪+ 142‬‬      ‫رت‬    ‫کبا‬
                      ‫سده )‬
                          ‫اد زن‬
                              ‫مزخو‬‫اقرب است و آنهم بسادسکریت_‪( 5802۷5 + 1018‬ا‬
  ‫‪ ( 52‬ازخود آغاز کرده) رابطه دارد ‪ .‬برای اطلاع از عقابد مختلف رك ‪ :‬بارتولمه ‪۰ ۲۹۸۱‬‬
      ‫استق ‪ , ۱۲۷‬هوشمان ‪.۱۷4‬تبعات ادرالی‪ .‬دارمستتر ‪ ۱‬ص‪ ۷۰‬بشتها ‪ ۲6۰ : ۱‬خرده اوستاه‪.۵۲‬‬
```


## [2026-09-14T03:15:17.571Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor lf in (175,195,196,206,207):\n    p=t[lf]\n    print('#### leaf',lf,'printed',lf+541)\n    for ln in p.split('\\n'):\n        if 'پهلوی' in ln or 'اوستا' in ln or 'خجسته' in ln or 'بارتولمه' in ln:\n            print('   ',ln.strip())\nEOF",
 "description": "Extract etymological footnotes from BQT leaves"
}
```


### [2026-09-14T03:15:18.678Z] TOOL RESULT

```
#### leaf 175 printed 716
    ‫جته؛ اوستا ‪uh - [2052‬‏ « اسفاا ‪ :‬ص ‪۷٩.‬‏ از ربشه اوستابی‪ ( )[028(02‬خواهش‪.‬‬
    ‫ه« بارتولمه ‪ .»۷۸4‬خجته لفة بمعتی تك‌خواسته ‪ .‬متبرك » مبارك؛ ضد «گسسته»‬                                    ‫‪0‬‬
#### leaf 195 printed 736
    ‫‏* جالوری از بتانداران خانده ‪.‬‬                          ‫‪ - ۴‬پهلوی ‪ « 1508721‬اونوالا ‪. ۵۸۲‬‬
#### leaf 196 printed 737
    ‫خرم‪.‬‬    ‫رك‪:‬‬       ‫‪-‬‬   ‫‪۳‬‬                ‫اوستا ‪ 4۰۲‬رك‪:‬خرم روز‪.‬‬
    ‫‪#‬خرها ‪-‬بنم‌اول‪ .‬پهلوی ‪ « ۷207۲2‬ناوادیام‪ < > ۵۱:۲‬اونوالا‪»۷۳۵‬‬
#### leaf 206 printed 747
    ‫يدر ر‬          ‫‪_ ۴‬اوستا_‪.4۲184۷۸-‬هندی باستان ‪4‬‬         ‫‪ ۱‬ظ؛مصحففرده“(ھ‪.‬م‪).‬‬
    ‫‪ ۴‬بهلوی ‪:( ۷0۲5۱21‬يك شهرت) «منای‪ ۷2۲5-110 ۷۷۲‬اوستا ‪uh _ 012۷2۲5‬‏‬
#### leaf 207 printed 748
```


## [2026-09-14T03:15:40.060Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ hur\"; grep -n -E 'حور|Ḥūr|hūr|Houri|houri' FVQ.txt | head -20",
 "description": "Grep Jeffery FVQ for ḥūr"
}
```


### [2026-09-14T03:15:40.119Z] TOOL RESULT

```
=== FVQ hur
7515:The Houries, or Maidens of Paradise. 
7602:Houries of Paradise is one borrowed from outside sources, and the 
8110:of Paradise, where we are told that the Houries are fLAll ^ Cj lj
```


## [2026-09-14T03:15:42.157Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins su/wesu\"; grep -n -E '^\\s*(su-|wesu-|esu-)|\\bwesu-\\b|\\besu-\\b' AHD_watkins1985.txt | head -20; echo \"=== AHD cushy/khush\"; grep -n -i -E 'cushy|khush' AHD_watkins1985.txt | head",
 "description": "Grep Watkins AHD for su-/wesu-"
}
```


### [2026-09-14T03:15:42.239Z] TOOL RESULT

```
=== AHD watkins su/wesu
462:esu-. Good. Extension of es-. Greek ews, good, combining form eu-, well: EU-. [Pok. esu-s 342.]
1033:su-. Well, good. 1. Sanskrit su-, well-being, good luck: SWASTIKA. 2. Compound *su-gia-es-, “living in good condition” (see g"ei-). [Pok. su- 1037.]
=== AHD cushy/khush
```


## [2026-09-14T03:15:46.694Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7500,7620p' FVQ.txt",
 "description": "Read Jeffery FVQ ḥūr discussion"
}
```


### [2026-09-14T03:15:46.755Z] TOOL RESULT

```
Arabic equivalent of these forms, however, is <^\i. to fail, to be dis- 
appointed (BDB, 295), and cj>^>. or <^> *>., as Bevan notes, 1 is to 

be taken as a loan-word from Aramaic, and the verb _>L!>- as a 

denominative. The probabilities are in favour of the borrowing being 
from Syriac rather than from Jewish Aram., 2 for (30**, especially 
in the plu., is used precisely in the Qur'anic sense (PSm, 1214). 



(Hur). 

xliv, 51 ; Hi, 20 ; Iv, 72 ; Ivi, 22. 
The Houries, or Maidens of Paradise. 

Except in Iv, 72, it is used always in the phrase /*-,_ j >- The 
occurrences are all in early Suras describing the delights of Paradise, 

where the ^ J^p- are ^ nc beauteous maidens whom the faithful 
will have as spouses in the next life. 

The Grammarians are agreed that j *> is a plu. of Jj > and 
derived from j>-> a form of U., and would thus mean " the 



white ones". /~- is a plu. of <V.P| meaning "wide eyed" (LA, 
xvii, 177). It thus becomes possible to take SJ*G, J9*" as ^ wo objectives 
used as nouns meaning " white skinned, large eyed damsels ". The 



1 Daniel, 62 n. 

2 Mingana, Syriac Influence, 86. 



118 FOREIGN VOCABULARY OF THE QUR ? AN 

Lexicons insist that the peculiar sense of j *>- is that it means the 

contrast of the black and white in the eye, particularly in the eye of 
a gazelle or a cow (cf. LA, v, 298 ; and TA, iii, 160). Some, however, 
insist equally on the whiteness of the body being the reference of the 

word, eg. al-Azharl in TA, "a woman is not called t\jj>- unless 

along with the whiteness of the eye there is whiteness of body." One 
gathers from the discussion of the Lexicographers that they were 
somewhat uncertain as to the actual meaning of the word, and in 
fact both LA. and TA. quote the statement of so great an authority 

as al-Asma'I that he did not know what was the meaning of j^>- as 
connected with the eye. 

The Commentators give us no help with the word as they merely 
set forth the same material as we find in the Lexicons. They prefer 
the meaning which refers it to the eye as more suited to the Qur'anic 
passages, and their general opinion is well summarized in as-Sijistanl, 
117. 

Fortunately, the use of the word can be illustrated from the old 
poetry, for it was apparently in quite common use in pre-Islamic 
Arabia. Thus in 'Abid b. al-Abras, vii, 24 (ed. Lyall) wo find the verse 



" And maidens like ivory statues, 1 white of eyes, did we capture " 
and again in 'Adi b. Zaid. 



" They have touched your heart, these tender white maidens, beside 

the river bank." 
and so in a verse of Qa'nab in the Mukhtardt, viii, 7, we read 



" And in the women's chamber when the house is full, are white 
maidens with charming voices." 
In all these cases we are dealing with human women, and except 

in the verse of 'Abld the word j >- could quite well mean white- 



1 So in al-A'sha we find ^jJl Jl^Kj^*-, cf. Geyer, Zwei Gedichte, i, 196 = 
Diwan, xxxiii, 11. 



FOREIGN VOCABULARY OF THE QUR ? AN 119 

skinned, and even in the verse of 'Abid, the comparison with ivory 
statues would seem to lend point to al-Azhari's statement that it is 
only used of the eyes when connected with whiteness of the skin. 

Western scholars are in general agreed that the conception of the 
Houries of Paradise is one borrowed from outside sources, and the 
prevalent opinion is that the borrowing was from Persia. Sale suggested 
this in lu's Preliminary Discourse, but his reference to the Sadder 
Bundahishn was rather unfortunate, as Dozy pointed out, 1 owing to 
the lateness of this work. Berthels, however, in his article " Die 
paradiesischen Jungfrauen im Islam", in Islamica, i, 263 ff., has 
argued convincingly that though Sale's Hurdn-i-Bihisht may not be 



called in as evidence, yet the characteristic features of the j^>- of the 
Qur'anic Paradise closely correspond with Zoroastrian teaching about 
the Daena. The question, however, is whether the name j^p- is of 
Iranian origin. Berthels thinks not. 2 Hang, however, suggested its 
equivalence with the Zoroastrian y-Gy* humat, good thought (cf. Av. 
A^JJG>O> ; Skt. *p*l) ; ftyy* huxt, good speech (cf. Av. iipoffttf > 

Skt. *W), and ^Xr^ *' 7 *r*fa, good deed (cf. Av. ^J^-tt))^) 3
```


## [2026-09-14T03:15:49.885Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7620,7700p' FVQ.txt",
 "description": "Continue FVQ ḥūr"
}
```


### [2026-09-14T03:15:49.939Z] TOOL RESULT

```
but the equivalences are difficult, and as Horovitz, Parodies, 13, points 

out, they in no way fit in with the pre-Islamic use of j^>-. Tisdall, 
Sources, 237 ff., claims that j^>- is connected with the modern Pers. 
jj. sun from Phlv. J^o X var 4 and Av. gYut) havarz, 5 but this 

comes no nearer to explaining the Qur'anic word. 

It is much more likely that the word comes from the Phlv. ft)}yf* 
hurust, meaning beautiful, and used in the Pahlavi books of the 
beauteous damsels of Paradise, e.g. in Arda Viraf, iv, 18, and in 



1 Het Islamisme, 3 cd., 1880, p. 101. 

2 " Das Wort Hur durfen wir naturlich ebensowenig in den iranischen Sprachen 
suchen." 

3 The three words occur together in Pand-namak, xx, 12, 13. Cf. Nyberg, Glossar, 
109, 110. 

4 Horn, Grundriss, pp. Ill, 112; Shikand, Glossary, 255. 

6 Bartholomae, AIW, 1847 ; Reichelt, Awestisches Elementarbuch, 512 ; cf. Skt. 



120 FOREIGN VOCABULARY OF THE QUR*AN 

Hadoyt Nasfc, ii, 23, 1 where we have the picture of a graceful damsel, 
white-armed, strong, with dazzling face and prominent breasts. Now 

5V)u is a good Iranian word, the equivalent of Av. 



TmraoSa, 2 and though these Pahlavi works are late the conceptions 
in them are early and there can be no question of borrowing from 
the Semitic. 

To this Iranian conception we may now add the influence of the 
Aram. "Tin. Sprengcr was doubtless right in his conjecture 3 that 

the root &~ to be white came to the Arabs from Aramaic. The Heb. 



"IT! occurs in Is. xxix, 22, in the sense of becoming pale through 
shame, and Syr. ]>CU* is commonly used to translate XCVKOV, and 
is thus used for the white garments of the Saints in Rev. iii, 4. Carra 
do Vaux, 4 indeed, has suggested that Muhammad's picture of the 
youths and maidens of Paradise was due to a misunderstanding of the 
angels in Christian miniatures or mosaics representing Paradise. This 

may or may not be so, but it does seem certain that the word j^>- in 

its sense of whiteness, and used of fair-skinned damsels, came into use 
among the Northern Arabs as a borrowing from the Christian com- 
munities, and then Muhammad, under the influence of the Iranian 

V)*>, used it of the maidens of Paradise. 



/%.v->- (Khdtam). 

xxxiii, 40. 

A seal. 

The passage is late Madinan and the word is used in the technical 



phrase 

17 **. 

On the surface it would seem to be a genuine derivative from
```


## [2026-09-14T03:16:06.669Z] TOOL CALL #41: Bash

```json
{
 "command": "sed -n '1,40p' /home/sfmqrb/git/rishe/tools/fetch_source.py",
 "description": "Inspect fetch_source tool"
}
```


### [2026-09-14T03:16:06.832Z] TOOL RESULT

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


## [2026-09-14T03:16:11.020Z] TOOL CALL #42: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/Euphrates\" \"https://www.etymonline.com/word/cushy\" \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A8\" \"https://en.wiktionary.org/wiki/%D8%AD%D9%88%D8%B1\"; do python3 tools/fetch_source.py \"$u\" --note \"page 484, root Su 1 Esu Wesu: Euphrates/cushy/xub/hur\" 2>&1 | tail -2; done",
 "description": "Archive web sources batch 1"
}
```


### [2026-09-14T03:16:19.924Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/86c962b0c4d92252.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2be697a887572ed3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1bdf23869ed832b0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0422a99755c9a7d1.txt
```


## [2026-09-14T03:16:22.647Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== Euphrates\"; grep -n -i -A14 'Etymology' 86c962b0c4d92252.txt | head -50",
 "description": "Read Euphrates wiktionary"
}
```


### [2026-09-14T03:16:22.701Z] TOOL RESULT

```
=== Euphrates
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
69-
70- 1.3.1 
71- Related terms 
72-
73- 1.3.2 
74- Translations 
75-
76- 1.4 
--
91: Etymology 
92-
93- 2.3 
94- Pronunciation 
95-
96- 2.4 
97- Proper noun 
98-
99- 2.4.1 
100- Declension 
101-
102- 2.5 
103- Noun 
104-
105- 2.5.1 
--
227: Etymology
228- [ edit ] 
229-
230- From Latin Euphrātēs , from Ancient Greek Εὐφράτης ( Euphrátēs ) , from Old Persian 𐎢𐎳𐎼𐎠𐎬𐎢 ( u-f-r-a-tu-u /⁠ h Ufrātuš⁠/ ) , from Akkadian 𒀀𒇉𒌓𒄒𒉣 ( ÍD Purattu ) , from Sumerian 𒀀𒇉𒌓𒄒𒉣 ( ÍD Buranun ) (compare Elamite 𒌑𒅁𒊏𒌅𒅖 ( ú-ip-ra-du-iš ) , Classical Syriac ܦܪܬ ( P(ə)rāṯ ) ). The Elamite, Akkadian, and possibly Sumerian forms are either from an unrecorded substrate language, or from Proto-Sumerian * 𒁍𒍏 burudu "copper" (Sumerian 𒍏 ( urudu ) ) with an explanation that Euphrates was the river by which the copper ore was transported in rafts, since Mesopotamia was the center of copper metallurgy at the period.
231-
232- Pronunciation
233- [ edit ] 
234-
235- IPA ( key ) : /juːˈfɹeɪtiːz/ 
236-
237- Audio ( US ) : ( file ) 
238-
239- Rhymes: -eɪtiz 
240-
241- Proper noun
--
424: Etymology
425- [ edit ]
```


## [2026-09-14T03:16:24.124Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== cushy\"; grep -n -i -B2 -A12 'cushy' 2be697a887572ed3.txt | head -40; echo \"=== xub\"; grep -n -A12 'Etymology' 1bdf23869ed832b0.txt | head -40",
 "description": "Read cushy and khub"
}
```


### [2026-09-14T03:16:24.198Z] TOOL RESULT

```
=== cushy
1:URL: https://www.etymonline.com/word/cushy
2-FETCHED: 2026-09-14T03:16:15Z
3-STATUS: 200
4:TITLE: Cushy - Etymology, Origin & Meaning
5-
6:Cushy - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
13- Apps 
14- Premium 
15-
16- Log in 
17-
18- Advertisement Remove Ads 
19- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
20-
21: Origin and history of cushy 
22-
23: cushy (adj.) 
24-
25- "easy," 1915, Anglo-Indian slang, from Hindi khush "pleasant, healthy, happy" + -y (2). Wright's "English Dialect Dictionary" (1898) has cush "a soft, useless person," identified as Scottish and Northumberland and explained as "A common term of reproach, used of one who allows others to beat him, either in self-defence or at work," hence cushie "soft, flabby." 
26- also from 1915 
27-
28: Entries linking to cushy 
29-
30- -y (2) 
31-
32- very common adjective suffix, "full of, covered with, or characterized by" the thing expressed by the noun, Middle English -i , from Old English -ig , from Proto-Germanic *-iga- , from PIE -(i)ko- , adjectival suffix, cognate with elements in Greek -ikos , Latin -icus (see -ic ). Germanic cognates include Dutch, Danish, German -ig , Gothic -egs .
33-
34- It was used from 13c. with verbs ( drowsy , clingy ), and by 15c. with other adjectives ( crispy ). Chiefly with monosyllables; with more than two the effect tends to become comedic.
35-
36- *
37-
38- Variant forms in -y for short, common adjectives ( vasty , hugy ) helped poets after the loss of grammatically empty but metrically useful -e in late Middle English. Verse-writers adapted to -y forms, often artfully, as in Sackville's "The wide waste places, and the hugy plain" ( and the huge plain would have been a metrical balk).
39-
40- After Coleridge's criticism of it as archaic artifice, poets gave up stilly (Moore probably was last to make it work, with "Oft in the Stilly Night"), paly (which Keats and Coleridge himself had used) and the rest.
=== xub
62: Etymology 
63-
64- 1.2 
65- Adjective 
66-
67- 2 
68- Pashto 
69-
70- Toggle Pashto subsection 
71-
72- 2.1 
73: Etymology 
74-
75- 2.2 
76- Pronunciation 
77-
78- 2.3 
79- Noun 
80-
81- 3 
82- Persian 
83-
84- Toggle Persian subsection 
85-
--
87: Etymology 
88-
89- 3.2 
90- Pronunciation 
91-
92- 3.3 
93- Adjective 
94-
95- 3.3.1 
96- Usage notes 
97-
98- 3.3.2 
99- Inflection 
--
131: Etymology
```


## [2026-09-14T03:16:34.827Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '125,175p' 1bdf23869ed832b0.txt; echo \"=== HUR arabic\"; grep -n -A10 'Etymology' 0422a99755c9a7d1.txt | sed -n '1,80p'",
 "description": "Read Persian خوب and Arabic حور etymologies"
}
```


### [2026-09-14T03:16:34.899Z] TOOL RESULT

```
 4 
 Urdu 

 Toggle Urdu subsection 

 4.1 
 Etymology 

 4.2 
 Pronunciation 

 4.3 
 Adjective 

 4.3.1 
 Derived terms 

 4.4 
 Adverb 

 4.5 
 Phrase 

 4.6 
 References 

 4.7 
 Further reading 

 Toggle the table of contents 

 خوب 

 21 languages 

 العربية 
 Deutsch 
 فارسی 
 Français 
 Magyar 
 Bahasa Indonesia 
 한국어 
 Kurdî 
 Lietuvių 
 Malagasy 
 ဘာသာမန် 
 Nederlands 
 Occitan 
 Polski 
 پښتو 
 Português 
=== HUR arabic
62: Etymology 
63-
64- 1.2 
65- Verb 
66-
67- 1.2.1 
68- Conjugation 
69-
70- 1.3 
71- Verb 
72-
--
121: Etymology 
122-
123- 2.2 
124- Pronunciation 
125-
126- 2.3 
127- Noun 
128-
129- 2.3.1 
130- Declension 
131-
--
141: Etymology 
142-
143- 3.2 
144- Pronunciation 
145-
146- 3.3 
147- Noun 
148-
149- 3.3.1 
150- Declension 
151-
--
161: Etymology 
162-
163- 4.2 
164- Pronunciation 
165-
166- 4.3 
167- Noun 
168-
169- 4.3.1 
170- Declension 
171-
--
254: Etymology
255- [ edit ] 
256-
257- Root 
258-
259- ح و ر ( ḥ w r ) 
260-
261- 14 terms 
262-
263- The Arabic term for the poplar is probably borrowed from Classical Syriac ܚܘܪܐ ( ḥawwərā ) , considering that
264- the range of distribution of the white poplar is outside Arabia, but inside the Aramaic language area
--
1570: Etymology
1571- [ edit ] 
1572-
1573- Borrowed from Arabic حُور ( ḥūr ) .
1574-
1575- Pronunciation
1576- [ edit ] 
1577-
1578- ( Standard Punjabi ) IPA ( key ) : /ɦuːɾ/ 
1579-
1580- Noun
--
1644: Etymology
1645- [ edit ] 
1646-
1647- Borrowed from Classical Persian حُور ( hūr ) , from Arabic حُور ( ḥūr ) .
1648-
1649- Pronunciation
1650- [ edit ] 
1651-
```


## [2026-09-14T03:16:40.966Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i -E 'Proto-Iranian|Middle Persian|hu-|Hapah|vapu' 1bdf23869ed832b0.txt | head -20",
 "description": "Find Persian khub etymology lines"
}
```


### [2026-09-14T03:16:41.022Z] TOOL RESULT

```
259: Inherited from Proto-Iranian *hwápati , from Proto-Indo-Iranian *swápati , from Proto-Indo-European *swép-e-ti , from *swep- ( “ to sleep ” ) .
283: Proto-Iranian *HhuHā́pah 
286: From Middle Persian 𐭧𐭥𐭡 ( xūb ) , from Old Persian *huvāpah , from Proto-Iranian *HhuHā́pah , from Proto-Indo-Iranian *HsuHápas , from Proto-Indo-European *h₁su- ( “ good ” ) +‎ *h₃épos ( “ work ” ) . Compare Sogdian [script needed] ( xwp ) .
475: Proto-Iranian *HhuHā́pah 
549: Pashto terms inherited from Proto-Iranian 
550: Pashto terms derived from Proto-Iranian 
559: Persian terms inherited from Proto-Iranian 
563: Persian terms derived from Proto-Iranian 
565: Persian terms inherited from Middle Persian 
566: Persian terms derived from Middle Persian 
576: Urdu terms derived from Proto-Iranian 
599: Middle Persian terms with non-redundant manual transliterations
```


## [2026-09-14T03:16:55.912Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport urllib.parse, subprocess\nwords=['هژیر','خنیا','هویدا','خجسته','خرم','خسرو','هما','هنر','خشنود','هوشنگ','خسر']\nfor w in words:\n    u='https://en.wiktionary.org/wiki/'+urllib.parse.quote(w)\n    r=subprocess.run(['python3','tools/fetch_source.py',u,'--note','page 484 root Su 1/Esu/Wesu: Persian derivative '+w],capture_output=True,text=True)\n    print(w, r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[:100])\nEOF",
 "description": "Archive Wiktionary pages for Persian derivatives"
}
```


### [2026-09-14T03:17:09.704Z] TOOL RESULT

```
هژیر /home/sfmqrb/git/rishe/data/verification/sources/web/cc972195b129aed2.txt
خنیا /home/sfmqrb/git/rishe/data/verification/sources/web/71579ebefc1889fc.txt
هویدا /home/sfmqrb/git/rishe/data/verification/sources/web/27c7d441b030957f.txt
خجسته /home/sfmqrb/git/rishe/data/verification/sources/web/65131a5fa342e274.txt
خرم /home/sfmqrb/git/rishe/data/verification/sources/web/4d82e3a553ca26df.txt
خسرو /home/sfmqrb/git/rishe/data/verification/sources/web/4db6a10667d14516.txt
هما /home/sfmqrb/git/rishe/data/verification/sources/web/b34c24d0037a22da.txt
هنر /home/sfmqrb/git/rishe/data/verification/sources/web/e97d90088de80132.txt
خشنود /home/sfmqrb/git/rishe/data/verification/sources/web/df4e52e22771427c.txt
هوشنگ /home/sfmqrb/git/rishe/data/verification/sources/web/024a112f77d4d59a.txt
خسر /home/sfmqrb/git/rishe/data/verification/sources/web/70609fc23fb15eb4.txt
```


## [2026-09-14T03:17:14.200Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in cc972195b129aed2:هژیر 71579ebefc1889fc:خنیا 27c7d441b030957f:هویدا 65131a5fa342e274:خجسته 4d82e3a553ca26df:خرم 4db6a10667d14516:خسرو b34c24d0037a22da:هما e97d90088de80132:هنر df4e52e22771427c:خشنود 024a112f77d4d59a:هوشنگ 70609fc23fb15eb4:خسر; do id=${f%%:*}; w=${f##*:}; echo \"######## $w\"; grep -n -E 'From Middle Persian|Middle Persian|Proto-Iranian|Avestan|Inherited|Borrowed' $id.txt | grep -v -E 'terms (derived|inherited|with)|Category|categor' | head -6; done",
 "description": "Extract etymology lines from archived Wiktionary pages"
}
```


### [2026-09-14T03:17:15.316Z] TOOL RESULT

```
######## هژیر
######## خنیا
141: Inherited from Middle Persian [Book Pahlavi needed] ( hwnydʾk' /⁠huniyāg⁠/ , “ joyful ” ) , from Proto-Iranian *xwan-iyā-ka- , from the same root as خواندن ( xândan , “ to sing ” ) , ultimately from Proto-Indo-European *swenh₂- ( “ to sound ” ) .
######## هویدا
######## خجسته
######## خرم
751: Inherited from Arabic خَرَمَ ( ḵarama ) .
1031: Inherited from Arabic خُرْم ( ḵurm ) .
1051: From Persian خرم ( xorram ) , from Middle Persian [script needed] ( hwlm /⁠huram⁠/ ) .
1089: From Middle Persian [script needed] ( hwlm /⁠huram⁠/ ) .
1208: Requests for native script for Middle Persian terms 
######## خسرو
237: Borrowed from Classical Persian خُسْرَو ( xusraw ) .
257: Borrowed from Classical Persian خُسْرَو ( xusraw ) .
291: Inherited from Middle Persian 𐭧𐭥𐭮𐭫𐭥𐭣𐭩 ( hwslwdy /⁠Husrōy⁠/ ) , 𐮰𐮵𐮽𐮹𐮵𐮱𐮵 ( hwslwb' /⁠Husrav⁠/ ) , from Old Median *Husravah , from Proto-Iranian *Hhucráwāh ( “ renowned, famous ” ) , from Proto-Indo-Iranian *Hsućráwās . Cognate with Avestan 𐬵𐬀𐬊𐬯𐬭𐬀𐬎𐬎𐬀𐬵 ( haosrauuah , mythical figure ) (from an unattested *𐬵𐬎𐬯𐬭𐬀𐬎𐬎𐬀𐬵 ( *husrauuah ) ), Ancient Greek εὐκλεής ( eukleḗs ) , Εὐκλῆς ( Euklês ) , Vedic Sanskrit सु॒श्रव॑स् ( suśrávas ) .
349: a male given name , Khosrow , Khusro , Khosrau , Khusrau , Khosro , Khusraw , Chosroes , and Osroes , from Middle Persian 
403: Borrowed from Classical Persian خُسْرَو ( xusraw ) .
453: Persian male given names from Middle Persian 
######## هما
362: From earlier همای ( homây ) , from Middle Persian hwmʾy ( humāy ) .
######## هنر
182: Borrowed from Classical Persian هُنَر ( hunar , “ art; craft, ability ” ) , from Middle Persian 𐫍𐫇𐫗𐫡 ( hwnr /⁠hunar⁠/ , “ virtue, ability, skill ” ) , ultimately from Old Persian 𐎢𐎺𐎴𐎼 ( ʰuvnara , “ talent, capability ” ) .
245: Inherited from Middle Persian [Book Pahlavi needed] ( hwnl ) , 𐫍𐫇𐫗𐫡 ( hwnr /⁠hunar⁠/ , “ virtue, ability, skill ” ) , from Old Persian 𐎢𐎺𐎴𐎼 ( ʰuvnara , “ talent, capability ” ) , from Proto-Iranian *hu-nara , from Proto-Indo-European *h₁su- ( “ good ” ) + *h₂nḗr ( “ man; power, force, vital energy ” ) . Cognate with Old Armenian հնար ( hnar , “ means, way ” ) (from Iranian), Avestan 𐬵𐬎𐬥𐬀𐬭𐬀   m ( hunara , “ skill, strength ” ) , Sanskrit सूनर ( sū-nára , “ possessing vital strength, mighty, prosperous, beautiful ” ) and सुन्दर ( sundara , “ beautiful, charming ” ) .
378: Boyce, Mary ( 1977 ), “hwnr”, in A word-list of Manichaean Middle Persian and Parthian (Acta Iranica 9a, Série 3 – “Textes et mémoires”, vol. 2-supplément)‎ [6] , with a reverse index by Ronald Zwanziger, Leiden, Tehran-Liège: E.J. Brill, Bibliothèque Pahlavi, page 49 
424: Requests for Book Pahlavi script for Middle Persian terms 
######## خشنود
176: Borrowed from Classical Persian خشنود ( xušnūd , “ content, satisfied ” ) , from Middle Persian [script needed] ( hwšnwt' /⁠hušnūd⁠/ , “ contented, happy ” ) .
231: Inherited from Middle Persian [script needed] ( hwšnwt' /⁠hušnūd⁠/ , “ contented, happy ” ) .
######## هوشنگ
161: From Middle Persian hwšng ( Hōšang ) , from Old Iranian . Akin to Avestan 𐬵𐬀𐬊𐬱𐬌𐬌𐬀𐬢𐬵𐬀 ( haošiiaŋha , “ Haoshyangha ” ) .
206: a male given name , Hushang , Houshang , Hooshang , and Hoshang , from Middle Persian 
237: Persian male given names from Middle Persian 
######## خسر
2032: Inherited from Arabic خَسِرَ ( ḵasira ) .
2240: Inherited from Arabic خَسِرَ ( ḵasira ) .
```


## [2026-09-14T03:17:47.236Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 esu-s\"; grep -n -E 'esu-s|esus' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"=== WLD Bd1 uesu\"; grep -n -E 'u̯esu|uesu-|vesu-' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Grep Walde-Pokorny for esu-s and wesu-"
}
```


### [2026-09-14T03:17:47.313Z] TOOL RESULT

```
=== WLD Bd1 esu-s
7710:159 in es, est, esse, esus Dehnung von e nach der sog. Lachmannschen 
7734:fressen lassen'; £o-Ptc. lat. esus (zum U s. o.s, lit. cstas „gegessen“, subst. 
7805:ruhen 'arm. utem enthielte die Praefixablautstufe o-), so daB z. B. lat. esus, 
10471:wenn aus *esus, so zuniichst vergleichbar mit gall. Esus, Esu-nertas, 
19671:320 nicht zu dt. TI7c.ce); gall, in Eigennamen vie Bello-, Sigo-vesus, V<‘*u- 
=== WLD Bd1 uesu
19498:Uber das wahrscheinlich verwandte idg. 'uesu- ,,gut‘‘ s. d. — Urspriing- 
19531:ues- „yerweilen“ s. d., wo aueh iiber lat. Vesta. S. ferner *uesu- ,,gut“. 
19649:uesu- — ues-r, ues-(e'n- 
19664:uesu- ,,gut" (voller tuts-, s. u.). 
19673:trefflichkeit" aus *uesu-d, fehus ..Yortreffliehkeit", *fehtu, gen. fehtad gl. 
19692:riickzugehn scheint, dagegen uesu- wegen got. iusiza auf *curs- ; Mittelbegriff
```


## [2026-09-14T03:17:50.187Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC esus/su-\"; grep -n -E '^esu|esus|^su-, |sū-s' IEC.txt | head -10; echo \"=== SYN good\"; grep -n -i -E 'Av\\. hu-|OPers\\. u-' SYN.txt | head -6; echo \"=== BRT ja8 erbitten\"; grep -n -E \"ja5-|jaS-|'erbitten'|jad-\" BRT.txt | head -8",
 "description": "Grep Mann, Buck, Bartholomae jaδ-"
}
```


### [2026-09-14T03:17:50.285Z] TOOL RESULT

```
=== IEC esus/su-
348:aksios (2) “like, equivalent, due, true, valid, right’. WP I, 36. Cf. aksulos Skt. aCChab; Av. a$0; Tokh. cf. asan; Kanic (name of a king at Kültepe) Kunut-ahsu- (cf. $nótos below); Arm. a£; Gk. áxios; MIr. aice, adj. ‘worth’; R cf. -oSij (in xor-ošij *good^). For OCS oxolü see aksulos, and for OCS oxvy see esus
3433:eds-, edsmn- “eating; food’. See ëd- and de- rivatives Per. aš ‘pap’; Lat. cf. sem-esus 'half-eaten'; OLat. cēsnās, pl., Lat. cena ‘mealtime’; Umb. cersnåf “food, supply’ (if fr. *ko-edsno-, -eds- na-); MHG as ‘carrion’; Du. aas ‘pasture’; OE æs, n. “food, bait, carrion’; Li. cf. ésena “fod- der”
3722:esros “good, fine, noble, grand'. Cf. es-mi, esulos, esus Lat. *ebrus (in in-ebrae aves 'inauspicious birds”); Ir. earr ‘noble, grand"
3731:esulos (1) ‘noble’. Cf. esros, esus, etc. Skt. ásurab; Av. ahuro; Hitt. assul, assulas “favour, greeting’; Dor. cf. eslós ‘noble, kind” beside Gk. esthlós, id. (cons. obscure); Lat. erulus “lord; Olr. éola “expert, wise’; Br. héal, hael ‘noble, generous’; OHG, OS er ‘man’; OE eorl “chief, noble, earl; ON jarl, id. jarl- (cpds. *noble-"). Cf. Srb. ohol ‘proud’?
3732:esulos (2) living, dwelling'. Cf. és-, esmi Skt. ásurah, adj. id.; Arm. heyk, hiyK & hiwy, i-st. “hut, inn”
3733:esus (əsus, su-) (1) ‘good, true’. Cf. su-, uesus. Cf. WP II 512; I, 161 Skt. cf. su-, px.; Av. hu-, id.; Arm. ge ‘rich, powerful; Oss. äx-, px. ‘good-; Myc. Gk. eu-, px.; Hom. ēü-; eüs, gs eéos; cf. also eós; áotos (*osu- + Gk. -atos); Hitt. assus; Umb. (?) eruhu (suitable. A wd. of ambig. spg. and mng.); Ligurian (?) Esu- (in Esu- biani, an Alpine tribe); Mir eo (2) ‘goog’;
3745:esus (esos, esi-) (2) “animal, breath, being”. Cf. es-mi, etc. Skt. ásuh (Ð “breath, life; Av. àhus (2) ‘world, place’; cf. áha ‘mind’; áhva “self, being’; Per. ahü deer": Arm. cf. ir, -i, -av, a-st. ‘thing, fact’; irav ‘rightly’; iravi, adj. ‘true’ from a type *esiiə)
3746:esus (és-) (3) “god, demon’. Cf. esulos, etc. Skt. ásuh, id.; Av. áhus ‘lord’; Hitt. hassus ‘king’ beside eshas (‘master’. The u-st. with umlaut is functional; the a-st., IE o-st. is non- functional); Lat. erus, herus ‘master’; era, OLat. esa ‘mistress’; Gaul. Esus ‘God’; ON ass, i-st. “heathen god'
3859:9SUS, See esus, su-, uesus. Additional forms: Av. anhu- queried ‘good’ beside báhus, váhus ‘perfect; OW hy ‘bold’; Lüneburg Wend. wachwy 'robust
4557:ghaisos ‘lance, pole’. WP I, 528 Av. cf. gaesus ‘lancer’; Gk. khaios *shepherd's crook’; Hes. gaiós (Thrac. or Maced. (?) «lance, pole); Celt. LW in Gk. gaisos ‘javelin’; Olr. gaí, gáe, Ir. gai, gaoi ‘spear’; Gallo-Lat. gae- sum; Br. goaó, goaf, gwat; Cor. gew; W gwaew lance, javelin’, w. induced labialism; OHG gër, MHG geér(e); OE gàr; Du. geer “bias, crosscut, gore’; ON geirr ‘spear’, geiri ‘gore, gusset
=== SYN good
7698:1. Grk. iyujs (also dSyunpds > NG yepés), hence dyiea, NG syela ‘health’ (hence the pop. greeting yeé cov), fr. *su-g"iyes, cpd. of IB *su- ‘well’ (Skt. su-, Av. hu-, etc.) and deriv. of IE *9"e7- ‘live’ in Grk. {@ ete. (4.74). Walde-P. 1.669.
29628:Skt. su-, Av. hu-; Grk. b- in dyes ‘in
=== BRT ja8 erbitten
```


## [2026-09-14T03:18:01.785Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT erbitten\"; grep -n -E 'erbitt' BRT.txt | head -8; echo; echo \"=== KLN eu- prefix\"; grep -n -E \"^eu-|eu-, pref|'well', from Gk\" KLN_1966.txt | head -10; echo \"=== KLN Euphrates\"; grep -n -i 'Euphrates' KLN_1966.txt KLN_1971.txt | head -6",
 "description": "Grep Bartholomae erbitten and Klein eu-"
}
```


### [2026-09-14T03:18:01.899Z] TOOL RESULT

```
=== BRT erbitten
21603:•  p.  a/Ctf*  adam  yä-a**m  jaäiyämiy  t^ur^- mazdäm  "das  erbitte  ich  mir  als  Gunst von  AhM."  D.^.3.
21657:-  a,uM^  äräjIzrt-M^I  -jiy.e.,,  i^i^„,^^  (dem)  erbitte  ich  den  Preis 'l^S';--  >'!  *'  •Ji!iuätl<;ä^fa,a  j„  Gerechtigkeit"  Y.j4.i;  -  J'a««»*' V- V«. 43; -»,»,«„  (sd.)V"'_Vj.36;3,„„.j„,.5,»   N.IOjf?).         a)   mit  M

=== KLN eu- prefix
13764:eu-,  combining  form  meaning  ‘good,  well’.  —  Fr. Gk.  eu,  ‘well’,  prop.  neut.  of  £64,  ‘good’,  which is  cogn.  either  with  Hitt,  ashshush,  ‘good’,  or — more  probably — with  OI.  vasuh,  Avestic  vohu-, ‘good’,  Ir.  feb  (fr.  I.-E.  *wesw-a),  ‘excellence’. Eu-  is  the  opposite  of  dys-. eucaine,  n.,  name  of  two  synthetic  alkaloids called  alpha-eucaine  and  beta-eucaine. —  Coined fr.  eu-  and  the  second  and  third  syllable  of cocaine.
=== KLN Euphrates
KLN_1971.txt:91983:the Euphrates-Tigris valley to the Persian Gulf 
KLN_1971.txt:132363:town on the Euphrates. 
KLN_1971.txt:149756:between the Euphrates and Tigris rivers. — Gk. 
KLN_1966.txt:14605:Fertile  Crescent,  a  semicircle  of  fertile  land  ex¬ tending  from  Palestine  and  Phoenicia  around the  Euphrates-Tigris  valley  to  the  Persian  Gulf {Ancient  hist.)  —  Coined  by  the  American  ar¬ chaeologist  and  historian  James  H.  Breasted (1865-1935).
KLN_1966.txt:20883:suff.  -fc  fr.  Kufa  (fr.  Arab.  al-K&fa"),  name  of  a town  on  the  Euphrates.
KLN_1966.txt:23636:mesoblast,  n.,  the  mesoderm.  —  Compounded  of  between  the  Euphrates  and  Tigris  rivers.  —  Gk.
```


## [2026-09-14T03:18:15.429Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB\"; grep -n -E 'hurust|hunar|husraw|hunyāg|huniyāg|hučihr|hujastag|humāy|hušnūd|hurram|huram' NYB_vol2_glossary.txt | head -12; echo \"=== HRN hunar/xunya/xujasta\"; grep -n -E 'hunar|/unar|yunyä|xunyä|/ugasta|yugasta|/urram|yurram|hu\\+|haosravanh' HRN.txt | head -12",
 "description": "Grep Nyberg and Horn"
}
```


### [2026-09-14T03:18:15.505Z] TOOL RESULT

```
=== NYB
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
2057:hunar [hwnl] skill 3?5, 158-9-20, 694, 845, — Av. (1831) hunara-; MPrth hwnr ‘manli- ness, ability’; Paz. xunar; NP hunar. *hūnēh: read *höneh q. v.
2070:hu-ram [hwlm] cheerful, glad 67%; bliss- ful, of Paradise, comp. ~-tar 66’. — Paz. cüram; NP xurram; in some way or other to be connected with Av. (1511) ram- ‘to rest, to repose’. Cf the next w. and huraméh.
2072:hu-ramak [hwlmk'] having good herds of cattle 5076, with the gl. ku ramak 4 apdrik veh dānēt dästan ‘that is: it knows how to breed other cattle [than sheep, ete.] in the best way’. — V. ramak. Paz. hurama; translates Av. (1857) hvq0wa-.
2073:huramēh abstr. of hu-ram (g.v.): ~ kartan to enjoy oneself 4?5.
2799:Ohurmazd [’whrmzd] 1. the name of the Supreme God, OP Ahuramazdah, passim ;
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
4039:vat-hunar [wthwnl] of bad skill, unskil- ful, comp. ~-tar 15$.
4101:Dhabhar vētvar, without etymology, in the sense of ‘contented, contentment, forbearance, patient, consoling oneself (‘consoling’ already West), resigned to the will of God’ (~ dätan ‘to console’); Hormazdyar with the same etymology as Bailey, but giving the same senses as Dhabhar (‘one who endures grief, en- during, patient, consoling, persevering’). Both lay stress on the close parallelism with a%ansand (x"arsand), of which it sometimes seems to be a mere synonym. However, the original idea underlying it must be looked for from another angle. I read it, with Dhabhar, vēt-var and derive it from OTr *vaiti-bara- ‘the willow- bringer [Av. (1314) vaéti-, NP bed, ’willow’] originally an epithet of Airyaman, the god of healing, and going back to the myth told in Vd. 22: Ahuramazdah, badly wounded and struck with 99999 maladies by Ahriman on his first on- slaught on the heavenly creation, pro- mised 1000 horses, 1000 camels, 1000 heads of cattle, 1000 sheep and “the beautiful Benediction of the Righteous" (dahma äfriti) to the god who could heal him. All declined except Airyama tišyē *Airyaman the desired(?)": he brought (barat) hair from 9 horse stallions, hair from 9 camel stallions, hair from 9 bulls, hair from 9 rams, and brought 9 willow twigs (nava vačtayo barat) and drew 9 furrows — the Phl v. adds: “and made a nirang (g. v.)”, a magic spell intended ‘to heal the wounds and stop the maladies. Apparently the willow twigs played the chief part in this nirang (of whose parti- culars we know of course nothing), thus it was quite natural to form out of it the epithet *vea$-bara- of Airyaman in his quality of the healing and relieving god. Later, Airyaman having faded away, the usage took a wider range and developed secondary nuances, but the original meaning ‘healing’ is still fairly transpar- ent in many passages, e.g. DD 36? (quoted both by Dhabhar and Hormazd-
5197:haxay-: *hamāxakēh (vi-)häy-: višatan haya-, hya-: xóm hazanra-: hazar hazanré.zyam-: hazan- grö-zim hšm, ham: hamak hindu-, hondu-: Hind hixra-: hihréh hizü, hizva: uzvàn hudah-: hu-dahak, véh-dak hü-: ?xuar hu frāšmē.dāti-: frašm hüxta-: hüxt humata-: humat humäyä-: Hamak hunara-: hunar hunivixta-: *hu-vaxm hunu-: hunusk h(u)vira-: dür-huviréh hurà: hur huska-: husk Hutaosā-: Hutös hutāšta-: hu-taštak hvaro-darosa-: xUar-cašm hvaro-xšačta-: xUar-xščt hvaršta-: huvaršt hyaona-: xičn
5638:hwnr: hunar
6654:hurama: huramak
=== HRN hunar/xunya/xujasta
4346:hur am), yurramth.
9559:V)<;v.^l aw. hunara- 'Hoheit (Geldner, y. 48, 5, vergl. KZ.
9570:'schön*: phlv. hunar, arm. LW. hnar.
9571:LW. kurd. huner; af;'. bei. (95) hunar.
```


## [2026-09-14T03:18:43.985Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB/AID khush\"; grep -n -i -E 'khush|khoosh' HJB.txt AID.txt GPL.txt | head -8; echo \"=== KLN cushy/houri\"; grep -n -i -E '^cushy|cushy,|houri' KLN_1966.txt KLN_1971.txt | head -8; echo \"=== LKT huri\"; grep -n -i -E 'Huri|houri' LKT.txt | head -6",
 "description": "Grep Hobson-Jobson, Klein, Lokotsch"
}
```


### [2026-09-14T03:18:44.096Z] TOOL RESULT

```
=== HJB/AID khush
GPL.txt:168:b. Conjunct >. The letter ¢ in conjunction with و‎ (>) occurs at the beginning of some Persian words, most of them words of common occurrence; but »> is regarded by Persians as a simple sound, the و‎ being neglected in pronunciation ; e.g. حود‎ khud or khad ‘self’ (pronounced as though written aS or JS, the latter, however, only in poetry or rhyming prose) ; خوش‎ khush or khash ‘happy’; خوردن‎ khurdan ‘to eat’; خواستن‎ khastan ‘to wish’ (not to be confounded with خاستن‎ khastan ‘to rise’); خوان‎ khan ‘table’ (but yb 0 ‘ prince’); خواهر‎ khahar ‘sister’; خویش‎ khish (archaic khésh) ‘ one’s own’; حوی‎ khai ‘sweat’. y> in such words is originally a conjunct, appearing in Phl. as ۳ Av; and in Zend as hva (S. swa); e.g. خود‎ = Phi. hvat = Z. hwato- (S. swa-tas). Persian grammarians appear to have lost cognizance of this fact. They regard the é and و‎ as separate and independent letters and term the اشمام ضمع  و‎ gly vaiv-t-eshmam- i-zamma ‘the vav that has a soupgon of zamma "or according to some grammarians واو معد وله‎ vav-i-ma‘dila ‘the deflected or removed va’, which latter term is, however, more correctly given to the 3 of the words رتو ردو‎ and y=. This letter is to be omitted in trans- literation except in the last-mentioned words in which it appears as u, e.g. du, tu, and chu.
GPL.txt:2845:.. bhashidan 4 حخشای‎ khashay- or رن‎ khushidan P khushay du + prefix uz زدودن‎ zidudan ‘to clean’, ۰ زدای‎ 20000 - stu ستودن‎ situdan ‘to praise’ ستای‎ sitdy-
GPL.txt:3297:talkhi uw khushi wu zisht w 2006 biguzasht‏ تلخی و خوشش و زشت و زیبا one “3G ‘bitterness and happiness, the ugly‏ and the beautiful passed away ’.‏ stl baghcha va hauz va mahtabi'st ‘there‏ و حوض و مهتابی است is a garden and a reservoir and a‏ terrace’.‏
GPL.txt:3458:se chi khush gufé an ‘how well did that man say ۳‏ وشن لفت آن
HJB.txt:16963:PAWNEE,  s.  Hind,  pdnt,  'water.' The  word  is  used  extensively  in Anglo-Indian  compound  names,  such as  bilayntee  pawnee,  'soda-water,' brandy-pawnee,  Khush-bo  pawnee  (for European  scents),  &c,  &c.  An  old friend.  Gen.  J.  T.  Boileau,  RE. (Bengal),  contributes  from  memory the  following  Hindi  ode  to  Water,  on the  Pindaric  theme  dpun-op  fUv  CSwp, or  the  Thaletic  one  dpx^  ^  TQy  Tdnn-wv HSwp !
=== KLN cushy/houri
KLN_1971.txt:62200:cushy, adj., easy, pleasant (slang). — Hind, khashi, 
KLN_1971.txt:116237:houri, n., a nymph of the Moslem Paradise; (fig.) 
KLN_1966.txt:10008:cushy,  adj.,  easy,  pleasant  (slang).  —  Hind,  khashi, ‘pleasant’,  fr.  Pers.  khush,  ‘pleasant’, cusp,  n.,  a  sharp  point.  —  L.  cuspis,  ‘point, pointed  end’,  of  uncertain  origin.  Cp.  cuspid, bicuspid,  tricuspid.
KLN_1966.txt:18149:Derivatives:  hour-ly,  adj.  and  adv. houri,  n.,  a  nymph  of  the  Moslem  Paradise;  (fig.) a  seductive  woman.  —  F.,  fr.  Pers.  hurt,  fr. Arab,  hur,  pi.  of  ahwar,  fern,  haurd ’,  ‘having beautiful  black  eyes’,  fr.  fiawira,  ‘had  black eyes’,  which  is  rel.  to  Heb.  hawar,  Aram.-Syr. hdwdr,  ‘was  white’,  Heb.  hur,  ‘white  stuff’,  hori, ‘white  bread’.  The  -i  in  Pers.  hurt  is  a  formative element  serving  to  denote  the  singular, house,  n.  —  ME.  hus,  hous,  fr.  OE.  hits,  rel.  to OS.,  ON.,  OFris.,  OHG.  MHG,  Ads,  Du.Au/s,G. Haus,  Goth.  -Aur(in  the  compound^MdAnj.'temp- le\  lit.  ‘the  house  of  God’);  orig.  ‘shelter’,  fr. I.-E.  *qeus-,  -s-enlargement  of  base  *qeu-,  ‘to cover,  hide’.  See  hide,  v.  and  cp.  hoard,  hose, hut.  Cp.  also  husk,  the  first  element  in  husband, husting  and  the  second  element  in  caboose, house,  tr.  and  intr.  v.  —  OE.  husian,  ‘to  take  into a  house’,  fr.  hus,  ‘house’.  See  house,  n. housecarl,  n.,  member  of  the  bodyguard  of  a Danish  or  early  English  king  or  nobleman (hist.)  —  OE.  huscarl,  fr.  ON.  huskarl,  which  is compounded  of  ON.  hus,  ‘house’,  and  karl, ‘man’.  See  house  and  churl, housel,  n.,  the  Eucharist  (obsol.)  —  ME.  husel, fr.  OE.  husel,  ‘the  Eucharist’,  rel.  to  ON.  husl, of  s.m.,  Goth,  hunsl,  ‘sacrifice’,  and  prob.  cogn. with  Lith.  svehtas.  OSlav.  svetu,  OPruss.  swints, ‘holy’,  Lett,  svinet,  ‘to  hallow,  celebrate’, Avestic  splnta-,  ‘holy’.
=== LKT huri
2055:einer  reizenden  Frau  sp.  hitrl,  frz.  houri, ndl.  engl,  houri,  dtsch.  Huri.  [DE  ;287. Devic  DEt  141.
4430:1962  a.  Tk.  tabak: 'Sohle'  [vom  Stamme  tap  'unten,  Grund, Sohle',  Vämbery  TktEtWb  S.  156,  Nr. 1721;  Kelekian  Kämüs  787  a];  hieraus mit  Verlust  des  Endkonsonanten  sp.  taba 'Art  Würfel  zum  Taba-  oder  Knöchel- spiel'. Man  beachte,  daß  bereits  im Mandschurischen  taba  ein  technischer Ausdruck  im  Knöchelspiel  ist:  'Die flachste  Seite  des  Spielkuochens';  eben-
4700:'JÜ96.  Mal.  trlpaiig: 'Seewalze,  Holothuria  edulis'  [Pijn  6^  b]; liieraus  en^l.  tripnng  ;aucli  swallow  aus mal.  suwälä  'dass.'  Pijn  143  b],  ndl. tfipang,  dtsch.  Trepaiif/;  trz.  trijjan,  tre- pang.  —  Der  Trepan;:  wird  in  den  in- dischen Gewässern  in  großen  Mengen getischt,  dann  abgekocht,  gedörrt  und nach  China  verkauft;  die  Chinesen  halten ihn  für  einen  Leckerbissen.  [Devic  DEt t>i>±    JAOS  XVIII,  110/111.
5008:Guttapercha  712 jffafcö  792 ifa^M»  GiVai  800 i/am  1157 Harakiri  818 Harmelraute  829 Harün  ar-Rasid  605 Hasan  ibn  Sabäh  839 Haschisch  839 Hedschra  863 Hildegard  v.  Bingen  795 Hobson-Jobson  835 Holothuria  edulis  2096 ifw^fta  655
7622:horde  1594 houri  848
```


## [2026-09-14T03:18:53.158Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2045,2058p' LKT.txt; echo \"=== MON hur\"; grep -n 'حور' MON_part1.txt MON_part2.txt | head -8",
 "description": "Lokotsch Huri entry and Mo'in حور"
}
```


### [2026-09-14T03:18:53.245Z] TOOL RESULT

```
845.  Hebr.  hattä':
'Sünder'  [Ave-L  IV,  529];  in  der  süd- fränkischen Händlersprache  sagt  man von  einem  Kaufmann,  dessen  Geschäft schlecht  steht,  er  gehöre  zur  Firma Katesberger  &  Co.
846.  Ar.  haud: 'Wasserbecken,  Teich';  hieraus  mit  ar. Art.  sp.  pg.  alfoz,  sp.  alhoz  'dass.'.  Über das  tk.  hatvtiz  wurde  rum.  havuz  'Wasser- becken, Zisterne',  bulg.  hawuz.  [DE 116.    Eguilaz  173.    ML  4085.
847.  Ar.  Jiaudagr:
'Tragkorb  auf  einem  Kamele,  Kamel- sänfle',  ebenso  bind,  hauda  'Silz  auf einem  Elefanten' ;  hieraus  angloind, hotvdah,  howder  'ein  großer  Sitz  auf einem  Elefanten',  für  zwei  und  mehr Personen  eingerichtet,  gewöhnlich  noch mit  einem  Schutzdach  versehen.  [Hob- son-Jobson  4!27/428.
848.  Ar.  liaurä':
Fem.  zu  ahu  'ar  'schwarzäugig'  besonders von  einer  Gazelle,  einem  Jünglinge  oder einer  Jungfrau  gesagt;  dazu  plur.  hür. Dieses  Wort  betrachteten  die  Perser  [und gelegentlich  auch  schon  die  Araber,  s. BSGW  Leipzig  ph.-hist.  Kl.  1881 .  XXXIII, 31]  als  sglr.  und  fügten  ein  *  der  Ein- heit an :  hüri ;  darunter  versteht  man die  Paradiesesjungfrauen,  die  man  nach Muhammads  Verheißung  im  Paradiese vorfinden  soll ;  hieraus  zur  Bezeichnung
5*
Ar.  hauz.]
68
einer  reizenden  Frau  sp.  hitrl,  frz.  houri, ndl.  engl,  houri,  dtsch.  Huri.  [DE  ;287. Devic  DEt  141.
849.  Ar.  liauz:
'Bezirk,  Umgebung';  hieraus  mit  ar. Art.  sp.  pg.  alfoz  'Landschaft,  Feldflur', im  MA  der  Bezirk,  der  seine  eigene Jurisdiktion  hatte  und  nach  einem  be- sonderen fuero  regiert  wurde,  meistens nur  eine  Pfarrei  oder  ein  Schloßgebiet umfassend.    [DE  116/117.
850.  Pers.  hänagä:
=== MON hur
MON_part2.txt:1233:دور محوری گردد و بر محیط آن شیاری به 
MON_part2.txt:1463:بحور مستحدث و آن را بجر جدید نیز 
MON_part2.txt:2223:کر که مرها حور سا 
MON_part2.txt:4351:کننده نیست؛ به درد من نمی حور د. 
MON_part2.txt:4490:بحور شعر؛ مرکب از یکك وتد مجموع و 
MON_part2.txt:5525:برحور» تما 
MON_part2.txt:7533:موسم سال. ضح.- (جغ.) چون محور زمین 
MON_part2.txt:7537:محور زمین نسبت به سطح مداری ٩۲‏ درجه
```


## [2026-09-14T03:19:03.399Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Persian$/{f=1} f{print NR\": \"$0}' 0422a99755c9a7d1.txt | sed -n '1,40p'",
 "description": "Persian section of حور Wiktionary"
}
```


### [2026-09-14T03:19:04.448Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:19:07.342Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -E 'Persian|Arabic حُور|from Arabic' 0422a99755c9a7d1.txt | sed -n '1,30p'",
 "description": "Find Persian entry in حور page"
}
```


### [2026-09-14T03:19:07.396Z] TOOL RESULT

```
1537: → Classical Persian: حور ( hur ) 
1573: Borrowed from Arabic حُور ( ḥūr ) .
1647: Borrowed from Classical Persian حُور ( hūr ) , from Arabic حُور ( ḥūr ) .
1707: Borrowed from Classical Persian حُور ( hūr , “ houri ” ) , from Arabic حُور ( ḥūr ) .
1807: Punjabi terms borrowed from Arabic 
1808: Punjabi terms derived from Arabic 
1817: Sindhi terms borrowed from Classical Persian 
1818: Sindhi terms derived from Classical Persian 
1819: Sindhi terms derived from Arabic 
1827: Urdu terms borrowed from Classical Persian 
1828: Urdu terms derived from Classical Persian 
1829: Urdu terms derived from Arabic 
1844: Persian terms with non-redundant manual transliterations
```


## [2026-09-14T03:19:48.182Z] TOOL CALL #57: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-14T03:19:48.231Z] TOOL RESULT

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
```


## [2026-09-14T03:19:53.206Z] TOOL CALL #58: Bash

```json
{
 "command": "grep -rl '\"Kes 2\"' data/extracted/batch/ | head -3; grep -rh -o '\"name\": \"Kes 2\"[^}]*}' data/extracted/batch/*.json | head -3; python3 - <<'EOF'\nimport json,glob\nfor f in glob.glob('data/extracted/batch/page-*.json'):\n    d=json.load(open(f))\n    for e in d['entries']:\n        if e['root']['name'].startswith('Kes'):\n            print(f, e['root'])\nEOF",
 "description": "Find Nourai's root Kes 2"
}
```


### [2026-09-14T03:19:54.374Z] TOOL RESULT

```
data/extracted/batch/page-484.json
data/extracted/batch/page-412.json
data/extracted/batch/page-261.json {'name': 'Kes 1, Kas 1', 'lang': 'Indo-European', 'refs': 'POK:586', 'gloss': 'to cut'}
data/extracted/batch/page-261.json {'name': 'Kes 2, Qseu', 'lang': 'Indo-European', 'refs': 'POK:585; WLD1:449', 'gloss': 'to scratch'}
```


## [2026-09-14T03:20:02.597Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E 'xšnau|xšnaw|XŠNAU|hušnūd|xšnu' CHEUNG.txt | head -12",
 "description": "Cheung on xšnau"
}
```


### [2026-09-14T03:20:02.663Z] TOOL RESULT

```
29536:*AVESTAN: xšnu- ‘to entertain, welcome, take care of (a guest)’, OAv. xSanmanai 
29542:ОРТ. 2sg. med. YAv. "kuxsnuuisa (FrW 7.2); Aor. s-: 3sg. INJ. OAv. xšnauš (Y 46.13, Y 51.12), med. 
29589:*xšnauš ‘to sneeze’ 
57805:*ti(n)f , *xšnau!
```


## [2026-09-14T03:20:05.050Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29525,29590p' CHEUNG.txt",
 "description": "Read Cheung xšnau entry"
}
```


### [2026-09-14T03:20:05.108Z] TOOL RESULT

```
«PIE *ksneu- ‘to sharpen’ = LIV: 373 | Pok.: 585 

*REFERENCES: Horn 1893: 177; Zhukovskij I: 20, 156; КРЕТ: 81a f., 140a f., 207b, 247a; Ivanow 1926: 
422; KPF II: 205; Christensen, Contributions I: 69, 167, 261; Christensen, Contributions II: 59, 116, 160; 
Abrahamian 1936: 113; Lambton 1938: 42b, 78a; MacKenzie 1966: 89; Nyberg II: 34b; WIM I: 68; WIM 
Ш: 104; Vahman — Asatrian 1991: 77; Werba 1997: 174; Paul 1998: 291; Steblin-Kamenskij 1999: 212; 
Lecoq 2002: 120, 122, 131, 133 (passim) 


*xÉnau^ ? ‘to exchange gifts (between host and guest) (whence: ‘to entertain, 
welcome (a guest), to thank, praise, etc.’)’ 
*AVESTAN: xšnu- ‘to entertain, welcome, take care of (a guest)’, OAv. xSanmanai 


"instead" (Y 29.9) = Liste: 17 

Pres. {1} athem.: OPT. 2sg. YAv. xsnuiiá (Y 68.9), med. OAv. xsnouuisà (Y 28.1); Pres. {2} athem. red.: 
ОРТ. 2sg. med. YAv. "kuxsnuuisa (FrW 7.2); Aor. s-: 3sg. INJ. OAv. xšnauš (Y 46.13, Y 51.12), med. 
3sg. YAv. xsnaosta (P 49), SUBJ. 15р. med. OAv. xSnaosai (Y 46.1), 3р1. OAv. xšnaošən (Y 30.5); 
Partic.: pres. (2) kuxsnuuana- (Yt 8.49, H 2.13), aor. OAv. xsnaosomna- (Y 46.18), perf. pass. xSnüta- (Y 
31.3, Y 51.9, Y 60.2); Caus.: pres. IND. 3sg. YAv. xsnauuaiieiti; Desid.: pres. IND. 15р. OAv. cixsnusa 
(49.1) 

*OLD PERSIAN: хёпи- ‘to be satisfied, glad’ > Kent: 182 

Partic.: perf. pass. xSnuta- <x-S-nu-u-t> (DNb 26) 

*MIDDLE PERSIAN: MMP ‘snwm- (denomin.) “о propitiate’ || BMP sn’dyn- /snayen-/ 
(sec. caus.) ‘to praise, propitiate’, BMP hwsnwtk /hosnud/ /husnüd/, BMP hwsnwtk 
/hosnudag/ /husnudag/ ? ‘satisfied, content > DMMPP: 94 

Pres.: IND. 3sg. MMP ‘snwmyd {hapax} || Caus.: pres. IND. 3sg. BMP sn'dynyt /Snayénéd/; Inf.: caus. 
BMP Ssn’dynytn /Snayénidan/; Partic.: perf. pass. BMP sn’dynyt /Snayénid/ 

*SOGDIAN: SSogd. ’xSnyBnt ‘hospitable, dienerfreundlich’ 

*CHORESMIAN: m/XNwry- (denomin.) ‘to thank’, bxnwr’wc (+ neg.) ‘ingratitude’ 
c» Samadi: 138 

*NWIR: NP xusnüd ‘content, pleased, happy’ 

*NEIR: Oss. æxsæn (postp.) ‘in the middle of, between’, axszeny ‘public, general’, 
æxsæny lag ‘mediator, go-between’ (with archaic meaning ?) 

9 On the etymology see Schwartz, Fs H.P. Schmidt: 213 f.; Schwartz 1990: 203. 
This root and its IE provenance postulated by Schwartz, l.c. is problematic, as one 


458 *x&naus 


needs to make several assumptions about their semantic development: it 1s a rather 
tall order to reconcile notably the meanings of Av. and Oss. through an unproven 
series of semantic shifts. 

«PIE *ksenu- ‘to exchange gifts (between guest and host)’ ? = LIV: — | Pok.: 

*IE COGNATES: Gr. &évoc, (Ion.) &etvog 'strange(r); guest, host’, Olrish son ‘in 


exchange' 
*REFERENCES: Abaev, Slovar’ IV: 227 


*xšnauš ‘to sneeze’
```


## [2026-09-14T03:20:31.450Z] TOOL CALL #61: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg484.png data/verification/sources/refs/ocr/BOOK/484.png && ls -la data/verification/sources/refs/ocr/BOOK/484.png\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81su-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81wesus\"; do python3 tools/fetch_source.py \"$u\" --note \"page 484 root Su 1/Esu/Wesu: PIE reconstruction\" 2>&1 | tail -1; done",
 "description": "Copy page image and fetch PIE reconstructions"
}
```


### [2026-09-14T03:20:32.941Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 100595 Sep 13 23:20 data/verification/sources/refs/ocr/BOOK/484.png
/home/sfmqrb/git/rishe/data/verification/sources/web/0796cdb8411b4cf9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/da3fbce2bb66881b.txt
```


## [2026-09-14T03:20:35.762Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 0796cdb8411b4cf9 da3fbce2bb66881b; do echo \"#### $f\"; head -5 $f.txt; grep -n -E 'Root|Adverb|Adjective|Descendants|good' $f.txt | sed -n '1,12p'; done",
 "description": "Check PIE reconstruction pages fetched"
}
```


### [2026-09-14T03:20:36.839Z] TOOL RESULT

```
#### 0796cdb8411b4cf9
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81su-
FETCHED: 2026-09-14T03:17:31Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₁su- - Wiktionary, the free dictionary

71: Descendants 
143: Possible metathesis of *h₁wes- ( “ good ” ) , or perhaps related to *h₁es- ( “ to be ” ) . [ 1 ] 
145: Hittite 𒀀𒀸𒋗𒍑 ( āššuš , “ good ” ) and possibly Epic Greek ἠΰς ( ēǘs , id. ) provide strong evidence for a u -stem adjective *h₁óh₁s-u-s , gen.sg. *h₁h₁s-éw-s , [ 2 ] which would point to a reduplicated root *h₁es- . Since Proto-Indo-European apparently did not allow geminate clusters, the weak stem would have simplified to *h₁s-éw- ; this could be the source of the combining form * h₁su- , with which it would be identical in the zero-grade.
152: good 
172: Descendants
#### da3fbce2bb66881b
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81wesus
FETCHED: 2026-09-14T03:20:32Z
STATUS: -1
TITLE:
```


## [2026-09-14T03:21:49.188Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && tail -18 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['status'], d['url'])\n\"",
 "description": "List archived URLs"
}
```


### [2026-09-14T03:21:50.132Z] TOOL RESULT

```
200 https://abadis.ir/fatofa/%D8%B3%D8%B1%D9%88/
200 https://abadis.ir/fatofa/%D8%B3%D9%85%D8%A7%D9%82/
200 https://abadis.ir/fatofa/%D8%B3%DA%AF%D8%B1/
200 https://fa.wikipedia.org/wiki/%D9%87%D9%88%D9%88%D8%AE%D8%B4%D8%AA%D8%B1%D9%87
200 https://en.wiktionary.org/wiki/%D8%AA%D8%A8%D8%A7%D9%87
200 https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D8%AE%D8%AA%D9%86
200 https://en.wiktionary.org/wiki/%D8%AA%D9%88%D9%BE
200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/top
200 https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%82%E0%A4%AA
200 https://en.wiktionary.org/wiki/%E0%A4%A4%E0%A5%81%E0%A4%9C%E0%A5%8D
200 https://www.etymonline.com/word/stop
200 https://www.etymonline.com/word/stuff
200 https://www.etymonline.com/word/stucco
200 https://www.etymonline.com/word/study
200 https://www.wisdomlib.org/definition/tup
-1 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81wesus
200 https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=MW&page=1086
200 https://abadis.ir/fatofa/%D8%AA%D8%A8%D8%A7%D9%87/
```


## [2026-09-14T03:21:53.410Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -h 'page 484' index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['status'], d['url'])\n\"",
 "description": "List my archived URLs for page 484"
}
```


### [2026-09-14T03:21:54.402Z] TOOL RESULT

```
200 https://en.wiktionary.org/wiki/Euphrates
200 https://www.etymonline.com/word/cushy
200 https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A8
200 https://en.wiktionary.org/wiki/%D8%AD%D9%88%D8%B1
200 https://en.wiktionary.org/wiki/%D8%AE%D9%86%DB%8C%D8%A7
200 https://en.wiktionary.org/wiki/%D9%87%D9%88%DB%8C%D8%AF%D8%A7
200 https://en.wiktionary.org/wiki/%D8%AE%D8%AC%D8%B3%D8%AA%D9%87
200 https://en.wiktionary.org/wiki/%D8%AE%D8%B3%D8%B1%D9%88
200 https://en.wiktionary.org/wiki/%D9%87%D9%85%D8%A7
200 https://en.wiktionary.org/wiki/%D9%87%D9%86%D8%B1
200 https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D9%86%D9%88%D8%AF
200 https://en.wiktionary.org/wiki/%D9%87%D9%88%D8%B4%D9%86%DA%AF
200 https://en.wiktionary.org/wiki/%D8%AE%D8%B3%D8%B1
-1 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81wesus
```


## [2026-09-14T03:22:02.814Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for u in '%D9%87%DA%98%DB%8C%D8%B1' '%D8%AE%D8%B1%D9%85' 'h%E2%82%81su'; do echo \"-- $u\"; grep -c \"$u\" index.jsonl; grep -o \"\\\"url\\\": \\\"[^\\\"]*$u[^\\\"]*\\\"\" index.jsonl | head -2; done",
 "description": "Verify missing URLs are archived"
}
```


### [2026-09-14T03:22:03.814Z] TOOL RESULT

```
-- %D9%87%DA%98%DB%8C%D8%B1
1
(eval):1: bad math expression: operand expected at `^\"'
-- %D8%AE%D8%B1%D9%85
1
(eval):1: bad math expression: operand expected at `^\"'
-- h%E2%82%81su
1
(eval):1: bad math expression: operand expected at `^\"'
```


## [2026-09-14T03:29:32.280Z] TOOL CALL #66: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-484.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nSRC_XUB = W + \"%D8%AE%D9%88%D8%A8\"\nSRC_HUR = W + \"%D8%AD%D9%88%D8%B1\"\nSRC_XONYA = W + \"%D8%AE%D9%86%DB%8C%D8%A7\"\nSRC_HOVAYDA = W + \"%D9%87%D9%88%DB%8C%D8%AF%D8%A7\"\nSRC_XOJASTE = W + \"%D8%AE%D8%AC%D8%B3%D8%AA%D9%87\"\nSRC_XOSROW = W + \"%D8%AE%D8%B3%D8%B1%D9%88\"\nSRC_HOMA = W + \"%D9%87%D9%85%D8%A7\"\nSRC_HONAR = W + \"%D9%87%D9%86%D8%B1\"\nSRC_XOSNUD = W + \"%D8%AE%D8%B4%D9%86%D9%88%D8%AF\"\nSRC_HUSANG = W + \"%D9%87%D9%88%D8%B4%D9%86%DA%AF\"\nSRC_XOSOR = W + \"%D8%AE%D8%B3%D8%B1\"\nSRC_HAZIR = W + \"%D9%87%DA%98%DB%8C%D8%B1\"\nSRC_XORRAM = W + \"%D8%AE%D8%B1%D9%85\"\nSRC_EUPH = \"https://en.wiktionary.org/wiki/Euphrates\"\nSRC_CUSHY = \"https://www.etymonline.com/word/cushy\"\nSRC_PIE = W + \"Reconstruction:Proto-Indo-European/h%E2%82%81su-\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"hu 1\", \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan hu- 'good, well' is not an independent word but the inherited first member of compounds (Bartholomae's AiW devotes cols. ~1817-1850 to hu-/hv- compounds). It continues PIE *h1su- through Proto-Indo-Iranian *su- (Sanskrit su-), Proto-Iranian s- > h- before a vowel being the regular Iranian change; Old Persian shows the further reduced u- (u-frašta-, Ufrātu-). Pokorny p.1037 states the equation outright: 'Old Indic su-, Avestan hu-, Old pers. u-'. The language label and the gloss in the box are exactly right.\",\n \"derivation_fa\": \"«hu-» اوستایی واژهٔ مستقل نیست بلکه پیشوند و جزء نخست ترکیب‌هاست (بارتولمه در فرهنگ ایرانی باستان حدود سی ستون را به ترکیب‌های hu-/hv- اختصاص داده است). این پیشوند از هندواروپایی آغازین *h₁su- می‌آید؛ س آغازین ایرانی باستان پیش از واکه به ه‍ بدل شده است (سنسکریت su- در برابر اوستایی hu-)، و در پارسی باستان یک گام فروتر رفته و به u- رسیده است (مانند Ufrātu-). پوکورنی در ص۱۰۳۷ همین برابری را آورده است؛ برچسب زبانی و معنای جعبه درست است.\",\n \"sources\": [SRC_PIE],\n \"ref_check\": [{\"ref\": \"POK:1037\", \"status\": \"supports\", \"note\": \"POK_full.txt line 83240 ff., 'Root / lemma: su-, su- ... Meaning: well, good. Material: Old Indic su-, Avestan hu-, Old pers. u-' (Page(s): 1037-1038) — exactly the node.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 1037-1038 s.v. su-, sū-\", \"stance\": \"supports\", \"note\": \"'Old Indic su-, Avestan hu-, Old pers. u-, e.g. ... Avestan hu-baya- \\\"good Eheglück granting\\\"'\"},\n   {\"src\": \"BRT\", \"where\": \"cols. 1817-1850 (hu-/hv- compounds)\", \"stance\": \"supports\", \"note\": \"the whole hu- section of the Altiranisches Wörterbuch (hu-ciθra-, hu-manah-, hu-māyā-, hu-raoδa-, hu-sravah- ...) shows hu- only as a compound-initial 'gut-'\"},\n   {\"src\": \"PHD\", \"where\": \"p. 45 s.v. hu-\", \"stance\": \"supports\", \"note\": \"'hu- [hw- | = M] good-, well-. ~ih: good, goodness' — the same prefix in Middle Persian\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins, s.v. su-\", \"stance\": \"supports\", \"note\": \"'su-. Well, good. 1. Sanskrit su-, well-being, good luck: SWASTIKA. [Pok. su- 1037.]'\"}]})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Avestan\", \"words\": \"hu-apah; hu-čitra; hu-nara; hu-vaeda\", \"verdict\": \"plausible\",\n \"derivation\": \"Three of the four are attested exactly as drawn. Av. hv-apah- n. 'gutes Werk, Wirken', adj. 'gute, schöne Werke verrichtend' (Bartholomae, AiW s.v. hv-apah-) = hu- + apah- 'work' (Skt. ápas-, Lat. opus); Pokorny p.780 s.v. op-1 'to work' cites 'Avestan hv-apah- \\\"good work (verrichtend)\\\"' — i.e. Nourai's POK:780 is exactly on target. Av. hu-ciθra- adj. 'von guter Abstammung, Herkunft; des Anblick gut ist, schön' (AiW col. 1821) and hunara- m. 'Können, Kunst; Tüchtigkeit' (AiW cols. 1831-32, with 'mp. (Pü.), np. hunar') are both real, and the referrals to 'Op' (*h3ep- 'work'), 'Skai' (čiθra- 'appearance, seed') and 'Ner 1' (*h2ner- 'man, force') are right. The fourth, hu-vaeda- 'well known', is not in Bartholomae and is Nourai's back-formation from New Persian hovaydā; Hübschmann and Mo'in analyse that word as hu + paydā (see node #3), so only three of the four members of this box are secured.\",\n \"derivation_fa\": \"از چهار واژهٔ این جعبه سه تا بی‌گمان اوستایی‌اند: hv-apah- «کارِ نیک» (بارتولمه ذیل hv-apah-) از hu- + apah- «کار» (سنسکریت ápas-، لاتین opus)؛ پوکورنی در ص۷۸۰ ذیل ریشهٔ op- «کار کردن» خودِ همین صورت اوستایی را آورده، پس ارجاع نورایی درست است. hu-čiθra- «نیک‌نژاد، خوب‌روی» (بارتولمه ستون ۱۸۲۱) و hunara- «هنر، توانایی» (ستون ۱۸۳۱) نیز واقعی‌اند و اشاره‌های او به ریشه‌های Op و Skai و Ner 1 پذیرفتنی است. اما *hu-vaēda- «نیک‌شناخته» در اوستا گواهی نشده و ساختهٔ قیاسی نورایی از «هویدا»ی فارسی است؛ هوبشمان و معین آن واژه را hu + پیدا می‌دانند (نگاه کنید به گرهٔ ۳). بنابراین ادعای جعبه با احتیاط پذیرفتنی است.\",\n \"sources\": [SRC_XUB, SRC_HONAR],\n \"ref_check\": [\n   {\"ref\": \"POK:780\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Root / lemma: op-1 ... Material: Old Indic apas-, Avestan hv-apah- \\\"good work (verrichtend)\\\"' (Page(s): 780) — supports hu-apah\"},\n   {\"ref\": \"POK:1037\", \"status\": \"supports\", \"note\": \"s.v. su-, sū- 'well, good', the first member\"},\n   {\"ref\": \"HRN:111\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.111 no.503: 'xūb gut, schön ... aw. hvāpah- \\\"wohltätig\\\"; phlv. xwap bezw. xūp; ai. svápas-'\"},\n   {\"ref\": \"HUB:57\", \"status\": \"partial\", \"note\": \"Hübschmann, Pers. Studien p.57 ad 503: 'Nach dieser Etymologie sollte man im Neup. *xwāi, *xwāb ... statt xūb erwarten. Ich setze xūb = skr. suvapus-' — he keeps hu- 'good' but rejects hvāpah-\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.v. hv-apah-, hu-ciθra- (col. 1821), hunara- (cols. 1831-32)\", \"stance\": \"supports\", \"note\": \"'hv-apah- (im gĀw.) n. \\\"gutes Werk, Wirken\\\"'; 'hu-ciθra- Adj. \\\"von guter Abstammung, Herkunft; des Anblick gut ist, schön\\\"'; 'hunara- m. \\\"Können, Kunst\\\" ... mp. (Pü.), np. hunar \\\"Fertigkeit\\\"'; no *hu-vaeδa- entry\"},\n   {\"src\": \"PHD\", \"where\": \"pp. 45-46\", \"stance\": \"supports\", \"note\": \"'hu-čihr [hwcyhl | M hwcyhr, (N xujir)] fair, beautiful'; 'hunar [hwnl | M hwnr, N ~] virtue, ability, skill'\"},\n   {\"src\": \"POK\", \"where\": \"p. 780 s.v. op-1\", \"stance\": \"supports\", \"note\": \"Avestan hv-apah- listed under the 'work' root, as the chart's ☞Op implies\"},\n   {\"src\": \"HUB\", \"where\": \"p. 57 (ad Horn 503)\", \"stance\": \"partial\", \"note\": \"prefers *hu-vapuš- 'of good form' for xūb\"}]})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"xūb «خوب»; hožîr «هژیر»; honar «هنر»; hovaydâ «هویدا»\", \"verdict\": \"plausible\",\n \"derivation\": \"خوب xūb: MP xūb/xūp < Old Persian *huvāpah < Proto-Iranian *Hhu-Hāpah 'of good works' = *h1su- + *h3épos (Wiktionary, following Horn no. 503 'aw. hvāpah-; phlv. xwap bezw. xūp'); the Avestan a-vowel is lost in the Middle Persian contraction hwāp > xūp — Hübschmann's objection (he expects *xwāb and prefers *hu-vapuš- 'of good shape') is the minority view. هژیر/خجیر: MP hu-čihr 'fair, beautiful' (MacKenzie p.45, 'N xujir') < Av. hu-ciθra-, with MP č > NP ž/j and the h-/x- doublet خجیر ~ هژیر; Mo'in's footnote in Borhān p.717 gives precisely 'پهلوی hučihr (از: هو «خوب» + چهر «اصل، نژاد»)، اوستا hu-ciθra- «بارتولمه ۱۸۲۱»'. هنر honar: MP hunar 'virtue, ability, skill' < OP huvnara- < *hu-nara- (Av. hunara-), PIE *h1su- + *h2nḗr. هویدا hovaydā 'evident': Hübschmann (Pers. Studien) analyses 'huvaida \\\"deutlich\\\", aus hu + paidā', and Mo'in's footnote on Borhān p.2401 says the same ('از: *hu اوستایی بمعنی خوب + ویدا (=پیدا)'), i.e. hu- + MP paydāg 'manifest', not a compound of the 'know' root as the chart's ☞Weid implies — hence the node is only plausible.\",\n \"derivation_fa\": \"«خوب» از فارسی میانهٔ xūb/xūp، از پارسی باستان *huvāpah، از ایرانی آغازین *hu-Hāpah «نیک‌کردار» (هو «خوب» + آپه «کار»)؛ هرن (ش۵۰۳) و ویکی‌واژه همین را می‌گویند، هرچند هوبشمان بر آن خرده گرفته و *hu-vapuš- «نیک‌پیکر» را پیشنهاد کرده است. «هژیر/خجیر» از پهلوی hučihr «زیبا» (مکنزی: N xujir) از اوستایی hu-čiθra-؛ حاشیهٔ معین بر برهان قاطع ص۷۱۷ دقیقاً همین را می‌آورد: «پهلوی hučihr (از: هو خوب + چهر اصل، نژاد)، اوستا hu-čiθra-». «هنر» از پهلوی hunar، از پارسی باستان huvnara-، هم‌ریشه با اوستایی hunara-. اما «هویدا» را هوبشمان و معین «هو + پیدا» می‌دانند (حاشیهٔ برهان ص۲۴۰۱)، نه ترکیبی از ریشهٔ «دانستن»؛ پس این جعبه در مجموع با احتیاط پذیرفتنی است.\",\n \"sources\": [SRC_XUB, SRC_HONAR, SRC_HAZIR, SRC_HOVAYDA],\n \"ref_check\": [\n   {\"ref\": \"BQT:2174\", \"status\": \"not_found\", \"note\": \"vol. 4 leaf 257 = printed 2174 is the entry نوا (music, melody), not a word of this box; it belongs rather to خنیا in node #7\"},\n   {\"ref\": \"BQT:2297\", \"status\": \"partial\", \"note\": \"printed 2297 (vol.4 leaf 380) is وید/ویدا 'lacking, lost' — only tangentially the ویدا element of هویدا\"},\n   {\"ref\": \"BQT:2401\", \"status\": \"supports\", \"note\": \"printed 2401 (vol.4 leaf 484), s.v. هویدا, Mo'in's note 4: 'از: (*hu اوستایی بمعنی خوب) + ویدا (*پیدا) ... قس کردی dyar'\"}],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"p. 111 no. 503\", \"stance\": \"supports\", \"note\": \"'xūb gut, schön, xūbī ... aw. hvāpah- \\\"wohltätig\\\"; phlv. xwap bezw. xūp, xūpīh; ai. svápas-'\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 2 p. 717 s.v. خجیر (Mo'in's footnote 3)\", \"stance\": \"supports\", \"note\": \"'پهلوی hučihr (از: هو (خوب) + چهر (اصل نژاد)) ... اوستا hu-ciθra- «بارتولمه ۱۸۲۱» ... رك: هژیر'\"},\n   {\"src\": \"PHD\", \"where\": \"pp. 45-46\", \"stance\": \"supports\", \"note\": \"'hu-čihr ... (N xujir) fair, beautiful'; 'hunar ... N ~ virtue, ability, skill'\"},\n   {\"src\": \"HUB\", \"where\": \"Pers. Studien (index s.v. huvaida)\", \"stance\": \"partial\", \"note\": \"'huvaida \\\"deutlich\\\", aus hu + paidā' — second element paydā, not *vaeδa-\"},\n   {\"src\": \"HRN\", \"where\": \"no. 349 (paidā)\", \"stance\": \"partial\", \"note\": \"Horn treats paydā as its own headword, the base of huvaidā\"}]})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Hindustani\", \"words\": \"xuši\", \"verdict\": \"plausible\",\n \"derivation\": \"Hindi-Urdu खुशी / خوشی khušī 'pleasure, happiness' is indeed a Persian loan of the Sultanate/Mughal period, but its Persian etymon is خوش xoš 'pleasant' (+ the abstract suffix -ī), not خوب xūb as the arrow from node #3 says. Klein s.v. cushy: 'Hind. khushī \\\"pleasant\\\", fr. Pers. khush \\\"pleasant\\\"'. Persian خوش itself belongs to the same family (Hübschmann p.57 ad 508 equates it with Av. *hvaši-/hu-, cf. Baluchi vas 'sweet, pleasant'), so the ultimate ancestry in *h1su- stands; only the immediate Persian source inside the chart is misdrawn.\",\n \"derivation_fa\": \"«خوشی» هندی‌اردو وام‌واژه‌ای فارسی است از دورهٔ سلطنت دهلی و گورکانیان، اما اصل آن «خوش» است نه «خوب»؛ کلاین ذیل cushy می‌نویسد: «هندی khushī «خوشایند» از فارسی khush». خودِ «خوش» نیز به همان خانوادهٔ hu- «خوب» بازمی‌گردد (هوبشمان ص۵۷ ذیل ش۵۰۸ آن را با *hvaši- اوستایی می‌سنجد)، پس ریشهٔ نهایی درست است و تنها پیوندِ درون‌نمودار (از «خوب») نادقیق است.\",\n \"sources\": [SRC_CUSHY],\n \"ref_check\": [{\"ref\": \"AHD:328\", \"status\": \"not_checked\", \"note\": \"the local AHD file is only Watkins's Indo-European appendix (no entry 'cushy'); p.328 of the 1975 New College edition is in the c- range, so the citation is plausibly the main-dictionary entry for cushy, and Klein gives the same etymology\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. cushy\", \"stance\": \"partial\", \"note\": \"'cushy, adj., easy, pleasant (slang). — Hind. khushī \\\"pleasant\\\", fr. Pers. khush, \\\"pleasant\\\"' — source is خوش, not خوب\"},\n   {\"src\": \"HJB\", \"where\": \"grep 'khush' — only Khush-bo pawnee s.v. PAWNEE\", \"stance\": \"silent\", \"note\": \"Hobson-Jobson has no separate khushi entry\"},\n   {\"src\": \"GPL\", \"where\": \"Platts-Ranking § on conjunct xw\", \"stance\": \"partial\", \"note\": \"lists خوش khush 'happy' among the xw- words whose w goes back to Av. hv-\"}]})\n\nnodes.append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"cushy\", \"verdict\": \"confirmed\",\n \"derivation\": \"English cushy 'easy, comfortable' is 1915 Anglo-Indian army slang (World-War-I soldiers' 'a cushy job', 'a cushy wound'), from Hindi khush/khushī 'pleasant, healthy, happy' (Etymonline; Klein s.v. cushy), the Persian loan of the previous node. The spelling with -y assimilated the word to the English adjective suffix -y; Wright's English Dialect Dictionary (1898) cush/cushie 'soft, flabby' may have helped it along.\",\n \"derivation_fa\": \"cushy انگلیسی به معنی «راحت، آسان» از ۱۹۱۵م و از زبان سربازان انگلیسی در هند برمی‌آید («کارِ راحت»، «زخم بی‌خطر») و از هندی khush/khushī «خوشایند» گرفته شده که خود وام‌واژه‌ای فارسی است (اتیمانلاین، کلاین). پایانهٔ ‑y آن به پسوند صفت‌ساز انگلیسی همانند شده است. زنجیرهٔ فارسی ← هندی ← انگلیسی درست است.\",\n \"sources\": [SRC_CUSHY],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. cushy\", \"stance\": \"supports\", \"note\": \"'cushy, adj., easy, pleasant (slang). — Hind. khushī ... fr. Pers. khush'\"},\n   {\"src\": \"WEB\", \"where\": \"grep 'cushy'\", \"stance\": \"silent\", \"note\": \"not found in the available Webster volume\"}]})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Avestan\", \"words\": \"hu-nivâk; hu-šnūta\", \"verdict\": \"plausible\",\n \"derivation\": \"Neither form is attested in Avestan in the shape and sense printed. (a) *hu-ni-vāka- 'of good voice' is reconstructed backwards from MP huniyāg 'delightful', huniyāgar 'musician' (MacKenzie p.46); the analysis hu- + *ni-vāka- to vak- 'to speak, sound' (PIE *wekʷ-, Nourai's ☞Wekw) is the traditional one, but Wiktionary (after Hasandust's alternative) derives خنیا rather from Proto-Iranian *xwan-iyā-ka-, to *xwan- 'to sing' (NP خواندن), PIE *swenh2-. (b) Bartholomae does have hu-xšnuta-, but glossed 'gutgeschärft, scharfgespitzt' (to xšnu- 'wetzen'); the 'well satisfied' word is a parallel *hu-xšnūta- built on xšnav- 'Genüge haben an', whose past participle xšnūta- is attested (AiW s.v.; OP xšnuta- 'satisfied', Kent 182). Nourai's referral ☞Kes 2 (= POK 585 *ksneu- 'to whet') is the etymology Cheung assigns to the homonym *xšnau1 'to sharpen'; for *xšnau2 'to entertain, satisfy' he explicitly declines that root.\",\n \"derivation_fa\": \"هیچ‌یک از این دو صورت دقیقاً به همین شکل در اوستا گواهی نشده است. *hu-ni-vāka- «خوش‌آوا» بازسازی قیاسی از پهلوی huniyāg «دل‌انگیز» و huniyāgar «رامشگر» است (مکنزی ص۴۶)؛ تحلیل سنتی آن را hu- + *ni-vāka- از ریشهٔ vak- «گفتن، آوا» می‌داند (همان ریشهٔ Wekw نورایی)، ولی ویکی‌واژه «خنیا» را از ایرانی آغازین *xwan-iyā-ka- از ریشهٔ *xwan- «خواندن، سرودن» می‌گیرد. دربارهٔ hu-šnūta نیز باید گفت بارتولمه hu-xšnuta- را «خوب‌تیزشده» معنی کرده (از xšnu- «تیز کردن»)، و واژهٔ «خشنود» به ستاکِ دیگری یعنی xšnav- «خرسند شدن» بازمی‌گردد که صفت مفعولی آن xšnūta- در اوستا و پارسی باستان هست. ارجاع نورایی به ریشهٔ Kes 2 (تیز کردن) بنابر چونگ به آن ریشهٔ هم‌آواست نه به این یکی؛ پس جعبه با احتیاط پذیرفتنی است.\",\n \"sources\": [SRC_XONYA, SRC_XOSNUD],\n \"ref_check\": [\n   {\"ref\": \"POK:780\", \"status\": \"not_found\", \"note\": \"POK p.780 is op-1 'to work' — nothing to do with these two words (the page was carried over from node #2)\"},\n   {\"ref\": \"POK:1037\", \"status\": \"supports\", \"note\": \"s.v. su-, sū- 'well, good' — covers the hu- of both compounds\"},\n   {\"ref\": \"HRN:111\", \"status\": \"not_found\", \"note\": \"Horn p.111 contains nos. 500-505 (xwāstan, xwāhar, xwāš, xūb, xud, xwar); neither خنیا nor خشنود\"},\n   {\"ref\": \"HUB:57\", \"status\": \"partial\", \"note\": \"Hübschmann p.57 ad 508 discusses خوش (= zd. *hvaši-), i.e. the family but not these two words\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.v. hu-xšnuta- and ʹxšnav-\", \"stance\": \"partial\", \"note\": \"'hu-xšnuta- Adj. \\\"gutgeschärft, scharfgespitzt\\\"'; but 'xšnav- V. \\\"Genüge haben an—\\\" ... PPfP. xšnūta-' gives the 'satisfied' participle\"},\n   {\"src\": \"PHD\", \"where\": \"p. 46\", \"stance\": \"supports\", \"note\": \"'huniyāg [hwnydʼkʼ | N xunyā] delightful'; 'huniyāgar ... [N xunyāgar] entertainer, musician'; 'hušnūd(ag) [M hwšnwd, N xušnūd] contented, happy'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *xšnau1 / *xšnau2 (pp. 457-458)\", \"stance\": \"partial\", \"note\": \"keeps *xšnau 'to sharpen' (PIE *ksneu-, Pok. 585) apart from *xšnau 'to entertain/satisfy' (Av. xšnu-, OP xšnuta-, BMP hwšnwtk /hušnūd/, NP xušnūd)\"}]})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"xonyâ «خُنیا (خنیاگر)»; xošnūd «خشنود (خوش)»\", \"verdict\": \"plausible\",\n \"derivation\": \"خنیا/خنیاگر: MP huniyāg 'delightful', huniyāgīh 'delight, entertainment', huniyāgar 'entertainer, musician' (MacKenzie p.46, who gives NP xunyā, xunyāgar); the change hu- > xu- > NP xu/xo- is the regular Middle-to-New-Persian treatment of the prefix (cf. hušnūd > xšnūd, huram > xurram), and Ferdowsī's verse quoted in the box uses خنیاگران in exactly the Pahlavi sense 'musicians'. Whether the second element is *ni-vāka- 'voicing' (☞Wekw) or *xwan- 'to sing' is open (see node #6), so the arrow's root assignment is only plausible. خشنود (and خوش): MP hušnūd(ag) 'contented, happy' (MacKenzie; Manichaean MP hwšnwd), OP xšnuta- 'satisfied' — this half of the box is solid.\",\n \"derivation_fa\": \"«خنیا» و «خنیاگر» از فارسی میانهٔ huniyāg «دل‌انگیز» و huniyāgar «رامشگر» است (مکنزی ص۴۶ که برابر فارسی نو را xunyā و xunyāgar می‌آورد)؛ تبدیل hu- ← خُ/خو در فارسی نو قاعده‌مند است (hušnūd ← خشنود، huram ← خرم) و بیت فردوسی در همین جعبه «خنیاگران» را به همان معنای پهلوی به کار برده است. اینکه جزء دوم *ni-vāka- «آوا» باشد یا *xwan- «خواندن»، هنوز محل گفتگوست. «خشنود» از پهلوی hušnūd(ag) «خرسند» و پارسی باستان xšnuta- «خشنود» است و این نیمهٔ جعبه استوار است.\",\n \"sources\": [SRC_XONYA, SRC_XOSNUD],\n \"ref_check\": [\n   {\"ref\": \"BQT:2174\", \"status\": \"partial\", \"note\": \"vol. 4 leaf 257 = printed 2174 is the entry نوا 'melody, sound' with Mo'in's footnote 'پهلوی nywʼk [niwāg] خوش نوا' and the Armenian comparison from Hübschmann — i.e. the second element of hu-nivāk, not خنیا itself\"},\n   {\"ref\": \"BQT:2297\", \"status\": \"not_found\", \"note\": \"printed 2297 is وید/ویدا, unrelated to this box\"},\n   {\"ref\": \"BQT:2401\", \"status\": \"not_found\", \"note\": \"printed 2401 is هویدا, unrelated to this box\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 46\", \"stance\": \"supports\", \"note\": \"'huniyāg ... | N xunyā'; 'huniyāgar ... | N xunyāgar'; 'hušnūd(ag) ... | N xušnūd'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *xšnau 'to entertain/satisfy'\", \"stance\": \"supports\", \"note\": \"'BMP hwšnwtk /hušnūd/ ... NP xušnūd \\\"content, pleased, happy\\\"'\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 4 p. 2174 s.v. نوا\", \"stance\": \"partial\", \"note\": \"Mo'in's note gives Pahlavi niwāg 'good-sounding' and Armenian nuag — the element in hu-nivāk\"}]})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Avestan\", \"words\": \"hu-jasta; hu-parathwa; hu-rama; hu-srav; hu-mâyâ\", \"verdict\": \"disputed\",\n \"derivation\": \"Four of the five are sound. hu-jasta- 'well-wished, blessed' (Mo'in's footnote in Borhān p.716 s.v. خجسته: 'اوستا hu-jasta ... از ریشهٔ اوستایی jaδ- (خواهش) «بارتولمه ۷۸۴»'), from jaδ-/jad- 'to ask, pray' = PIE *gʷʰedʰ- (☞Gwhedh). hu-rāma- 'well rested' to Av. ram- 'to rest' (AiW 1511; Nyberg II s.v. hu-ram). hu-sravah- adj. 'der einen guten Ruf hat; berühmt' (AiW col. 1837), whose vṛddhi derivative Haosravah- is the name of the Kavi king (AiW: 'mp. husrōy, np. xusrav'). hu-māyā- adj. 'segensreich; gesegnet' and the woman's name Humāyā- (AiW cols. 1833-34, 'mp. humāy, np. humāi'). The fifth, *hu-pərəθβa- 'good to cross', is NOT an Avestan word: it is the nineteenth-century folk-etymological reading of Old Persian Ufrātu- 'Euphrates' (Kent, Old Persian, lexicon s.v.: 'Ufrātu- sb. \\\"Euphrates\\\", river of Babylonia: Elam. ú-ip-ra-tu-iš, Akk. purattu, Gk. Εὐφράτης'), and the river name is Sumerian Buranun > Akkadian Purattu — the Iranian form only reinterprets it (see nodes #9, #10). Because that one member is wrong, the box as drawn is disputed.\",\n \"derivation_fa\": \"چهار عضو از پنج عضو این جعبه درست است: hu-jasta- «نیک‌خواسته، خجسته» از ریشهٔ jaδ- «خواستن، طلبیدن» (حاشیهٔ معین بر برهان ص۷۱۶ و بارتولمه ستون ۷۸۴)؛ hu-rāma- «نیک‌آرام» از ram- «آرمیدن»؛ hu-sravah- «نیک‌نام، نامور» (بارتولمه ستون ۱۸۳۷) که صورت وریدی آن Haosravah- نام کی‌خسرو است؛ و hu-māyā- «فرخنده، خجسته» و نام زن Humāyā (بارتولمه ستون ۱۸۳۳: «پهلوی humāy، فارسی نو همای»). اما *hu-pərəθβa- «نیکْ‌گذر» واژه‌ای اوستایی نیست؛ این تنها خوانشِ ریشه‌شناسی عامیانهٔ نام پارسی باستان Ufrātu- «فرات» است و کنت آن را وام‌گرفته از اکدی purattu (و در نهایت سومری Buranun) می‌داند. به سبب همین یک عضو، ادعای جعبه رد می‌شود.\",\n \"sources\": [SRC_XOSROW, SRC_HOMA, SRC_EUPH],\n \"ref_check\": [\n   {\"ref\": \"BQT:717\", \"status\": \"partial\", \"note\": \"in the Mo'in/Amir Kabir pagination of the scan the خجسته entry with its footnote 'اوستا hu-jasta ... بارتولمه ۷۸۴' stands on p.716 (vol. 2 leaf 175); p.717 (leaf 176) is the facing page with خجیر — one page off, but the claim is there\"},\n   {\"ref\": \"BQT:737\", \"status\": \"supports\", \"note\": \"vol. 2 leaf 196 = printed 737, the خرم entry\"},\n   {\"ref\": \"BQT:748\", \"status\": \"supports\", \"note\": \"vol. 2 leaf 207 = printed 748, the خسرو compounds; the facing p.747 carries خسر 'father-in-law' with the footnote 'اوستا x̃asura-, هندی باستان śváśura-' and خسرو with 'پهلوی husraw ... اوستا haosravah-'\"},\n   {\"ref\": \"BQT:2365\", \"status\": \"supports\", \"note\": \"vol. 4 leaf 448 = printed 2365 s.v. همای, Mo'in's note: 'هما ... قس همایون. همای لفظاً بمعنی فرخنده و خجسته. humāya- و hu-māya- بهمین معنی بسیار در اوستا بکار رفته «یشت‌ها ص۳۱۶» پهلوی humāy «تاوادیا»'\"},\n   {\"ref\": \"HRN:108\", \"status\": \"contradicts\", \"note\": \"Horn p.108 no.486: 'xusur \\\"Schwiegervater\\\". aw. x̃asuru-; ai. çváçura-; arm. skesrayr' — the page Nourai cites derives the in-law word from *swéḱuros, not from hu-srav\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. 1833-34, 1837, and s.v. pərətav-\", \"stance\": \"partial\", \"note\": \"'hu-māyā- Adj. \\\"segensreich; gesegnet\\\"'; 'hu-sravah- Adj. \\\"der einen guten Ruf hat; berühmt\\\"'; 'pərətav- \\\"Übergang über das Wasser, Furt, Brücke\\\"' — but no *hu-pərəθβa- compound\"},\n   {\"src\": \"KNT\", \"where\": \"Old Persian, lexicon s.v. Ufrātu-\", \"stance\": \"contradicts\", \"note\": \"'Ufrātu- sb. \\\"Euphrates\\\" ... Elam. ú-ip-ra-tu-iš, Akk. purattu, Gk. Εὐφράτης' — a Babylonian name, not an Iranian compound\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary s.v. hu-ram\", \"stance\": \"supports\", \"note\": \"'hu-ram [hwlm] cheerful, glad ... NP xurram; to be connected with Av. (1511) ram- \\\"to rest, to repose\\\"'\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 2 p. 716 (Mo'in's footnote to خجسته)\", \"stance\": \"supports\", \"note\": \"'خجسته؛ اوستا hu-jasta «اسفار ص۷۹» از ریشهٔ اوستایی jaδ- (خواهش) «بارتولمه ۷۸۴». خجسته لغةً بمعنی نیک‌خواسته، متبرک، مبارک'\"}]})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Persian\",\n \"words\": \"xojasteh «خجسته»; Forât «فُرات»; xorram «خرّم»; xosor «خسرو (کسری)»; xosrow «خُسر (خسور،خسوره)»; homâ «هما (همای ، همایون)»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"خجسته < MP huǳastag < Av. *hu-jasta- (Borhān p.716, footnote) — confirmed. خرم < MP huram 'happy' (MacKenzie p.46; Nyberg: 'NP xurram ... Av. ram-') — confirmed. خسرو < MP Husraw/Husrōy < Old Median *Husravah < PIr *Hhu-čráwāh 'renowned', cognate with Av. haosrauuah-, Greek εὐκλεής/Εὐκλῆς and Vedic suśrávas- — confirmed (the Arabic form کسری is the Arabicised Kisrā). هما/همای/همایون < MP humāy < Av. hu-māya- 'blessed' — confirmed (Borhān p.2365). TWO words are wrong. (a) فرات is not 'the crossable river': NP/Arabic al-Furāt continues Akkadian Purattu (< Sumerian Buranun); the Old Persian Ufrātu- is itself an adaptation of the Babylonian name, and NP فرات is a straight Arabic loan. (b) خسر (خسور، خسوره) 'father-in-law' has nothing to do with hu-srav 'famous': it is Av. x̃asura-, Skt śváśura-, Lat. socer, from PIE *swéḱuros — stated on the very page of Horn (p.108 no. 486) that Nourai cites for node #8, and in Mo'in's footnote on Borhān p.747. In addition the printed page swaps the two transliterations: it prints 'xosor' beside خسرو (کسری) and 'xosrow' beside خُسر (خسور، خسوره), whereas خسرو = xosrow and خسر = xosor; the JSON reproduces the page faithfully, so this is the book's own slip.\",\n \"derivation_fa\": \"«خجسته» از پهلوی huǳastag و اوستایی *hu-jasta- (حاشیهٔ معین بر برهان ص۷۱۶) درست است؛ «خرم» از پهلوی huram (مکنزی، نیبرگ)؛ «خسرو» از پهلوی Husraw/Husrōy و مادی باستان *Husravah «نامور»، هم‌ریشه با اوستایی haosravah- و یونانی εὐκλεής و سنسکریت suśrávas- (صورت معرّب آن «کسری» است)؛ «هما/همای/همایون» از پهلوی humāy و اوستایی hu-māya- «فرخنده». اما دو واژه نادرست است: «فرات» ایرانی نیست، بلکه از اکدی purattu (و در نهایت سومری Buranun) است و به عربی الفرات و از آنجا به فارسی رسیده؛ و «خسر/خسور» به معنی پدرزن هیچ پیوندی با hu-srav ندارد و از اوستایی x̃asura-، سنسکریت śváśura-، لاتین socer و هندواروپایی *swéḱuros است — همان چیزی که هرن در ص۱۰۸ (شمارهٔ ۴۸۶) و حاشیهٔ معین بر برهان ص۷۴۷ می‌گویند. افزون بر این، خودِ کتاب آوانگاری دو واژه را جابه‌جا چاپ کرده است: در برابر «خسرو» xosor و در برابر «خُسر» xosrow نوشته، حال آنکه باید وارونه باشد؛ استخراج داده‌ها وفادار است و خطا از چاپ کتاب است.\",\n \"sources\": [SRC_XOSROW, SRC_HOMA, SRC_XORRAM, SRC_XOJASTE, SRC_XOSOR, SRC_EUPH],\n \"error_in\": \"book\",\n \"book_prints\": \"xosor : \\\"well known\\\" king «خسرو (کسری)» / xosrow : \\\"famous\\\" in-law «خُسر (خسور،خسوره)»\",\n \"correct_form\": \"xosrow = خسرو (the king), xosor = خسر (the in-law) — the two Latin transliterations are interchanged on the printed page\",\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"partial\", \"note\": \"the box cites Borhān without a page; the relevant pages are 716 (خجسته, Av. hu-jasta), 737 (خرم), 747 (خسر < Av. x̃asura- — which contradicts the chart), 748 (خسرو < MP husraw < Av. haosravah-), 2365 (همای < Av. hu-māya-). Four support the chart, the خسر entry contradicts it, and Borhān has no Iranian etymology for فرات\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"pp. 45-46\", \"stance\": \"supports\", \"note\": \"'huram [hwlm | N xurram] happy'; 'husraw [hwslwbʼ | N xusraw] famous, of good repute'; 'humāy [hwmʼy | N ~] a bird of good omen; eagle'\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 2 p. 747 (Mo'in's footnotes to خسر and خسرو)\", \"stance\": \"partial\", \"note\": \"'اوستا x̃asura-، هندی باستان śváśura- ... پدر زن' for خسر, and 'پهلوی husraw ... اوستا haosravah-' for خسرو — the first contradicts the chart, the second supports it\"},\n   {\"src\": \"HRN\", \"where\": \"p. 108 no. 486\", \"stance\": \"contradicts\", \"note\": \"'xusur \\\"Schwiegervater\\\". aw. x̃asuru-; ai. çváçura-; arm. skesrayr' — خسر is not from hu-srav\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary s.v. hu-ram\", \"stance\": \"supports\", \"note\": \"'NP xurram; ... Av. (1511) ram-'\"}]})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Greek\", \"words\": \"Euphrates\", \"verdict\": \"disputed\",\n \"derivation\": \"Greek Εὐφράτης does come to the Greeks through Old Persian — Herodotus and Xenophon use the form the Achaemenid administration used — but the Old Persian name Ufrātuš is itself a loan: Sumerian Buranun > Akkadian Purattu > (Elamite ú-ip-ra-tu-iš) Old Persian Ufrātuš > Greek Euphrátēs, Latin Euphrātēs (Wiktionary; Kent, Old Persian, lexicon s.v.). The Iranian and Greek forms owe their eu-/u- to a folk-etymological reinterpretation as the prefix 'good' (and Greek reshaped the ending after -ατης names), which is exactly why the older handbooks Nourai follows explained it as *hu-pərəθβā 'good to cross'; modern Iranistics does not accept that as the source of the name.\",\n \"derivation_fa\": \"یونانی Εὐφράτης راستی از راه پارسی باستان به یونانیان رسیده است (هرودوت و گزنفون صورت دیوانی هخامنشی را به کار برده‌اند)، اما خودِ نام پارسی باستان Ufrātuš وام‌واژه است: سومری Buranun ← اکدی Purattu ← (عیلامی ú-ip-ra-tu-iš) ← پارسی باستان Ufrātuš ← یونانی Euphrátēs ← لاتین Euphrātēs (کنت، ویکی‌واژه). آغازِ u-/eu- آن حاصل ریشه‌شناسی عامیانه و همانندسازی با پیشوند «هو/نیک» است و همین سبب شده کتاب‌های قدیمی آن را *hu-pərəθβā «نیکْ‌گذر» بخوانند؛ ایران‌شناسی امروز این تفسیر را نمی‌پذیرد.\",\n \"sources\": [SRC_EUPH],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"not_found\", \"note\": \"the local AHD file is Watkins's IE-root appendix only; it has no Euphrates entry, and the appendix does not list the river under su-/esu-\"}],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Old Persian, lexicon s.v. Ufrātu-; also § on place names\", \"stance\": \"contradicts\", \"note\": \"'Ufrātu- sb. \\\"Euphrates\\\", river of Babylonia: Elam. ú-ip-ra-tu-iš, Akk. purattu, Gk. Εὐφράτης'\"},\n   {\"src\": \"KLN\", \"where\": \"grep 'Euphrates' in the 1966/1971 editions\", \"stance\": \"silent\", \"note\": \"Klein has no headword Euphrates (only incidental mentions s.v. Fertile Crescent, Kufic, Mesopotamia)\"},\n   {\"src\": \"BRT\", \"where\": \"s.v. pərətav-\", \"stance\": \"silent\", \"note\": \"'Durchgang über das Wasser, Furt, Brücke' exists, but no compound with hu- and no river name\"}]})\n\nnodes.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"Euphrates\", \"verdict\": \"confirmed\",\n \"derivation\": \"English Euphrates is the learned Latin form Euphrātēs taken over from Ancient Greek Εὐφράτης, reaching English through the Vulgate and the medieval Bible translations (Old English already has Eufrate). The step drawn here (Greek > English, through Latin) is uncontroversial; only the further ancestry claimed in nodes #8 and #10 is at issue.\",\n \"derivation_fa\": \"«Euphrates» انگلیسی همان صورت لاتینی Euphrātēs است که از یونانی Εὐφράτης گرفته شده و از راه ترجمهٔ لاتینی کتاب مقدس (ولگات) و ترجمه‌های سده‌های میانه به انگلیسی رسیده است. این حلقه از زنجیره (یونانی ← لاتین ← انگلیسی) بی‌چون‌وچراست؛ آنچه محل ایراد است تبارِ پیشین این نام است (گره‌های ۸ و ۱۰).\",\n \"sources\": [SRC_EUPH],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"grep 'Euphrates'\", \"stance\": \"silent\", \"note\": \"no headword; Klein only mentions the river s.v. Mesopotamia 'between the Euphrates and Tigris rivers'\"},\n   {\"src\": \"FSD\", \"where\": \"grep 'Euphrates'\", \"stance\": \"silent\", \"note\": \"no etymological entry found in the available volumes\"}]})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Avestan\", \"words\": \"hu-mana; hav-sivanga, hao-šyangh\", \"verdict\": \"plausible\",\n \"derivation\": \"Av. hu-manah- adj. 'des Denken gut ist' and, in Younger Avestan, 'gutes Muts, wohlgemut' is well attested (AiW col. 1834; Skt. sumánas-; Pahlavi gloss huminišn) — the referral ☞Men 1 (*men- 'to think') is right. Haošiiaŋha- is likewise real, the name of 'des Stammvaters und ersten Königs der Iranier' with the epithet Paraδāta- (AiW cols. 1738-39), but its analysis is not: Bartholomae writes flatly 'Eig. Bed.? Versuch einer Et. bei Justi NB. 126'. The reading as *hau-šyah- 'of good dwellings' (to šay-/ši- 'to dwell', hence Nourai's 'with good household') is one guess among several, and the first variant printed in the box, 'hav-sivanga', is not a citable Avestan form.\",\n \"derivation_fa\": \"hu-manah- «نیک‌اندیش» در اوستا گواهی شده است (بارتولمه ستون ۱۸۳۴؛ سنسکریت sumánas-؛ ترجمهٔ پهلوی huminišn) و ارجاع نورایی به ریشهٔ Men 1 «اندیشیدن» درست است. Haošiiaŋha- نیز نام نخستین شهریار ایرانیان با لقب پرادات است (بارتولمه ستون ۱۷۳۸)، ولی تحلیل معنایی آن قطعی نیست؛ بارتولمه صریحاً می‌نویسد «معنای اصلی؟» و به کوشش یوستی ارجاع می‌دهد. خوانش *hau-šyah- «دارندهٔ خانمان نیک» (از ریشهٔ šay- «زیستن، مسکن گزیدن») تنها یکی از حدس‌هاست و صورت «hav-sivanga» که در متن آمده صورت اوستاییِ قابل استنادی نیست؛ پس با احتیاط پذیرفتنی است.\",\n \"sources\": [SRC_HUSANG],\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"not_checked\", \"note\": \"no page given in the box; Borhān's هوشنگ entry (vol. 4, ه section) was not pinpointed\"},\n   {\"ref\": \"FAF:708\", \"status\": \"not_checked\", \"note\": \"Danešgar, Farhang-e A'lām-e Fārsi — not digitised anywhere (refs_online.json: 'Not found')\"},\n   {\"ref\": \"ZMA:48\", \"status\": \"not_checked\", \"note\": \"Jonaydi, Zendegi va Mohājerat-e Āryāiān — purchase only, no open copy (refs_online.json)\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1834 s.v. hu-manah-; cols. 1738-39 s.v. haošyaŋha-\", \"stance\": \"partial\", \"note\": \"'hu-manah- Adj. \\\"des Denken gut ist\\\" ... 2) \\\"gutes Muts, wohlgemut\\\"'; for the king: 'EN. ... des Stammvaters und ersten Königs der Iranier ... Eig. Bed.? Versuch einer Et. bei Justi NB. 126'\"},\n   {\"src\": \"PHD\", \"where\": \"p. 45\", \"stance\": \"partial\", \"note\": \"'hu-menīšn [hwmynšnʼ] of good thought'; '~-mānīh good-mindedness' — the Middle Persian continuations of hu-manah-\"}]})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"Hūman «هومن»; Hūšang «هوشنگ»\", \"verdict\": \"plausible\",\n \"derivation\": \"هوشنگ is beyond doubt: NP Hūšang < MP Hōšang < Av. Haošiiaŋha- (Wiktionary; the Pahlavi books' Hōšang paraдāt = Av. Haošyaŋha Paraδāta), with the regular loss of the final syllable and šy > š. هومن is the Shahnameh name of the Turanian warrior and also the modern given name; its base Av. hu-manah- 'good-minded' is attested, and the parallel Middle Persian Wahman/Bahman (< Vohu Manah) shows the same compound type — but no continuous Old–Middle–New Persian line for *Hūman is documented in the dictionaries, so this half rests on the transparency of the compound rather than on attestation. The glosses ('well mannered', 'good builder') are Nourai's own renderings; 'good builder' in particular reproduces one disputed reading of Haošiiaŋha-.\",\n \"derivation_fa\": \"«هوشنگ» بی‌گمان از فارسی میانهٔ Hōšang و اوستایی Haošiiaŋha- است (در کتاب‌های پهلوی «هوشنگ پرادات» برابر «هَئوشیَنگهَ پَرَذاتَ»)، با افتادن هجای پایانی و تحول šy ← š. «هومن» نام پهلوان تورانی در شاهنامه و نیز نام امروزی است؛ پایهٔ آن یعنی اوستایی hu-manah- «نیک‌اندیش» گواهی شده و ساختِ همانندِ «وهومن/بهمن» (از Vohu Manah) همین الگو را نشان می‌دهد، اما سلسلهٔ پیوستهٔ پارسی باستان ← پهلوی ← فارسی نو برای *Hūman در فرهنگ‌ها ثبت نشده است. معنی‌هایی که نورایی به دست داده («نیک‌خو»، «نیک‌سازنده») برداشت خود اوست؛ پس این جعبه با احتیاط پذیرفتنی است.\",\n \"sources\": [SRC_HUSANG],\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"not_checked\", \"note\": \"no page given in the box\"},\n   {\"ref\": \"FAF:708\", \"status\": \"not_checked\", \"note\": \"not digitised (refs_online.json: 'Not found')\"},\n   {\"ref\": \"ZMA:48\", \"status\": \"not_checked\", \"note\": \"purchase only, no open copy\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. 1738-39, 1834\", \"stance\": \"partial\", \"note\": \"Haošyaŋha- attested with Paraδāta-; hu-manah- attested; no etymology given for the king's name\"},\n   {\"src\": \"PHD\", \"where\": \"p. 45\", \"stance\": \"partial\", \"note\": \"'hu-menīšn of good thought', 'humat = Av. humata- good thought' — the MP type behind هومن\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary, Avestan-Pahlavi index (humāyā-, humata-, hunara-)\", \"stance\": \"silent\", \"note\": \"no Hūman/Hōšang headword in the Manual's glossary\"}]})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Avestan\", \"words\": \"hava-rd\", \"verdict\": \"transcription_suspect\",\n \"derivation\": \"'hava-rd' is not a possible Avestan form, and the printed page (pdf 484 / book 454) really does show 'hava-rd : well grown, well-built ☞Leudh', so the extraction is faithful and the slip is the book's. The word meant is Av. hu-raoδa- adj. 'von gutem äusseren Ansehen, von schönen Formen' (Bartholomae col. 1836), with the variants hu-raoδah- and the abstract *hu-raoδay- 'gutes äusseres Ansehen'; Bartholomae expressly derives it 'zum V. raod-' — the verb 'to grow' that is Nourai's ☞Leudh (PIE *h1leudʰ-) — and gives the Pahlavi rendering of the word as hurust, which is precisely the next node. Jeffery, whose page Nourai cites at second hand through VDQ, writes the same: 'Phlv. hurust ... the equivalent of Av. huraoda'.\",\n \"derivation_fa\": \"«hava-rd» صورتی است که در اوستا ممکن نیست، و تصویر صفحهٔ چاپی (ص۴۵۴ کتاب) نشان می‌دهد که خودِ کتاب همین را چاپ کرده است؛ پس خطای خوانشِ اسکن نیست، خطای چاپ کتاب است. واژهٔ مورد نظر اوستایی hu-raoδa- «خوش‌سیما، خوش‌اندام» است (بارتولمه ستون ۱۸۳۶) با گونه‌های hu-raoδah- و *hu-raoδay-؛ بارتولمه آن را به ریشهٔ raod- «رُستن، بالیدن» بازمی‌گرداند — همان ریشه‌ای که نورایی با نشانهٔ Leudh به آن ارجاع داده — و برابر پهلوی آن را hurust می‌آورد که دقیقاً گرهٔ بعدی است. جفری نیز (که نورایی از رهگذر ترجمهٔ فارسی‌اش «واژه‌های دخیل در قرآن» به او ارجاع می‌دهد) همین را می‌نویسد.\",\n \"sources\": [],\n \"error_in\": \"book\",\n \"book_prints\": \"hava-rd : well grown, well-built ☞Leudh\",\n \"correct_form\": \"hu-raoδa- (also hu-raoδah-) 'of fine growth, beautiful'\",\n \"ref_check\": [\n   {\"ref\": \"VDQ:39\", \"status\": \"partial\", \"note\": \"VDQ is Badre'i's Persian translation of Jeffery's Foreign Vocabulary; the corresponding English text (FVQ pp. 119-120) has 'Phlv. hurust ... the equivalent of Av. huraoda' — the substance is there, but with the correct Avestan form, not 'hava-rd'\"},\n   {\"ref\": \"MAG:186\", \"status\": \"not_checked\", \"note\": \"Widengren, Muhammad the Apostle of God (1955), ch. VIII — archive.org lending only, HathiTrust search-only (refs_online.json)\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1836 s.v. hu-raoδa-, *hu-raoδay-, hu-raoδah-\", \"stance\": \"partial\", \"note\": \"'hu-raoδa- Adj. \\\"von gutem äusseren Ansehen, von schönen Formen\\\" ... Pü.: hurust(ak)'; '*hu-raoδay- f. \\\"gutes äusseres Ansehen\\\" ... Zum V. raod-'\"},\n   {\"src\": \"FVQ\", \"where\": \"pp. 119-120\", \"stance\": \"partial\", \"note\": \"'It is much more likely that the word comes from the Phlv. hurust, meaning beautiful ... hurust is a good Iranian word, the equivalent of Av. huraoda'\"}]})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Pahlavi\", \"words\": \"hu-rust\", \"verdict\": \"confirmed\",\n \"derivation\": \"MP hu-rust 'well-grown' is a real Book-Pahlavi word: MacKenzie p.46 lists 'hu-|-rust [-lwstʼ] well-grown' among the hu- compounds (and his English index has 'well-grown hurust'). It is hu- + rust, the past stem of rōyistan/rustan 'to grow' (< Old Iranian *raud-/*ruθ-), and it is exactly the word the Pahlavi translators use to render Av. hu-raoδa-/hu-raoδah- (Bartholomae col. 1836: 'Pü.: hurust'). It describes the radiant maiden of the Pahlavi apocalypses (Ardā Wīrāz 4.18, Hadoxt Nask 2.23), which is why it entered the discussion of the Qur'anic ḥūr.\",\n \"derivation_fa\": \"«hurust» واژه‌ای اصیل در پهلویِ کتابی است: مکنزی در ص۴۶ ذیل ترکیب‌های hu- آن را «hu-rust نیک‌رُسته» آورده است. ساخت آن hu- + rust (ستاک گذشتهٔ rōyistan/rustan «روییدن»، از ایرانی باستان *raud-) است و مترجمان پهلوی همین واژه را برابر اوستایی hu-raoδa-/hu-raoδah- به کار برده‌اند (بارتولمه ستون ۱۸۳۶: «پهلوی: hurust»). این واژه وصفِ دوشیزهٔ زیبای متن‌های پهلوی (ارداویراف‌نامه ۴/۱۸ و هادخت‌نسک ۲/۲۳) است و از همین‌رو به بحث دربارهٔ «حور» قرآنی راه یافته است. ادعای نورایی در این گره درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"MAG:186\", \"status\": \"not_checked\", \"note\": \"Widengren 1955 not accessible (lending/search-only); the Pahlavi form itself was verified in MacKenzie and Bartholomae\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 46 (s.v. hu-rust) and English index 'well-grown'\", \"stance\": \"supports\", \"note\": \"'~-rust [-lwstʼ] well-grown'; index: 'well-grown hurust'\"},\n   {\"src\": \"BRT\", \"where\": \"col. 1836\", \"stance\": \"supports\", \"note\": \"the Pahlavi gloss of hu-raoδa- is 'hurust(ak)', erl. 'χūpīh pa gōšt' — beauty as to the flesh\"},\n   {\"src\": \"FVQ\", \"where\": \"p. 119\", \"stance\": \"supports\", \"note\": \"'the Phlv. hurust, meaning beautiful, and used in the Pahlavi books of the beauteous damsels of Paradise, e.g. in Arda Viraf, iv, 18, and in Hadoyt Nask, ii, 23'\"}]})\n\nnodes.append({\n \"id\": 16, \"lang\": \"Arabic\", \"words\": \"hūr\", \"verdict\": \"disputed\",\n \"derivation\": \"Arabic حور ḥūr (Q 44:54, 52:20, 55:72, 56:22) is morphologically a native plural of أحور aḥwar / حوراء ḥawrāʾ 'having the white of the eye strongly contrasted with the black', from the root ḥ-w-r 'to be white' (Klein s.v. houri; Lokotsch no. 848; Wiktionary root حور), and it is used of human women in pre-Islamic poetry ('Abīd b. al-Abraṣ, 'Adī b. Zayd) long before any Qur'anic paradise context. Jeffery — the author of the very book Nourai cites through its Persian translation VDQ — reaches a carefully split conclusion: the sense of whiteness 'came into use among the Northern Arabs as a borrowing from the Christian communities' (Aram./Syr. ḥwr 'to be white'), 'and then Muhammad, under the influence of the Iranian hurust, used it of the maidens of Paradise'. In other words the CONCEPT may be Iranian, the WORD is Semitic; the straight arrow Pahlavi hu-rust > Arabic ḥūr drawn here is Widengren's maximal position (MAG:186) and is not the view of modern scholarship.\",\n \"derivation_fa\": \"«حور» عربی (قرآن، ۴۴/۵۴، ۵۲/۲۰، ۵۵/۷۲، ۵۶/۲۲) از نظر ساخت جمعِ «أحور/حوراء» است از ریشهٔ عربی ح‑و‑ر «سپید بودن، سیاهی و سپیدی چشم را در تقابل داشتن» (کلاین ذیل houri، لوکوچ ش۸۴۸، ویکی‌واژه)، و در شعر جاهلی (عبید بن الأبرص، عدی بن زید) دربارهٔ زنان آدمی به کار رفته است، یعنی پیش از هر زمینهٔ بهشتی. جفری — همان کسی که نورایی از راه ترجمهٔ فارسی کتابش (واژه‌های دخیل، ص۳۹) به او ارجاع می‌دهد — نتیجه‌ای دوپاره می‌گیرد: معنای سپیدی از آرامی/سریانی به عربیِ شمال راه یافته و سپس «تحت تأثیر hurust ایرانی» دربارهٔ دوشیزگان بهشتی به کار رفته است. یعنی مفهوم ممکن است ایرانی باشد اما واژه سامی است؛ پیکانِ مستقیمِ «پهلوی hurust ← عربی حور» دیدگاه بیشینه‌گرای ویدنگرن است و پژوهش امروزی آن را نمی‌پذیرد.\",\n \"sources\": [SRC_HUR],\n \"ref_check\": [\n   {\"ref\": \"VDQ:39\", \"status\": \"partial\", \"note\": \"= Jeffery, FVQ 118-120: he grants the Iranian influence on the conception ('under the influence of the Iranian hurust') but derives the word itself from the Semitic root ('the word ḥūr in its sense of whiteness ... came into use among the Northern Arabs as a borrowing from the Christian communities'); Berthels, whom Jeffery quotes, is blunter: 'Das Wort Hūr dürfen wir natürlich ebensowenig in den iranischen Sprachen suchen'\"},\n   {\"ref\": \"MAG:186\", \"status\": \"not_checked\", \"note\": \"Widengren 1955 (lending only) is the source of the strong Iranian claim; not verifiable here\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. houri\", \"stance\": \"contradicts\", \"note\": \"'F., fr. Pers. hūrī, fr. Arab. ḥūr, pl. of aḥwar, fem. ḥawrāʾ \\\"having beautiful black eyes\\\", fr. ḥawira \\\"had black eyes\\\", which is rel. to Heb. ḥāwar, Aram.-Syr. ḥāwār \\\"was white\\\"'\"},\n   {\"src\": \"LKT\", \"where\": \"no. 848 (Ar. ḥaurāʾ)\", \"stance\": \"contradicts\", \"note\": \"'Fem. zu aḥwar \\\"schwarzäugig\\\" ... dazu plur. ḥūr. Dieses Wort betrachteten die Perser als sglr. und fügten ein ī der Einheit an: ḥūrī'\"},\n   {\"src\": \"FVQ\", \"where\": \"pp. 118-120\", \"stance\": \"partial\", \"note\": \"full discussion, quoted above; pre-Islamic attestations of ḥūr of human women\"}]})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Persian\", \"words\": \"hūr 1 «حور» (extra: حوری ، حوروش)\", \"verdict\": \"confirmed\",\n \"derivation\": \"Whatever the ultimate history of the Arabic word, this last step is certain and runs the other way from the Pahlavi one: New Persian حور hūr (and the singulative حوری hūrī, the compound حور‌وش 'houri-like') is a Qur'anic Arabic loan taken over with the Islamic paradise vocabulary (Wiktionary: Arabic حور → Classical Persian حور, whence Urdu, Punjabi, Sindhi). Persian speakers reinterpreted the Arabic plural as a singular and added the unit-ī, ḥūrī, which is the form that went on to Turkish, French houri and English houri (Lokotsch 848; Klein s.v. houri). So the chart is right that حور reached Persian from Arabic; what it claims is a round trip is a round trip only on Widengren's disputed premise.\",\n \"derivation_fa\": \"هر تاریخی که برای واژهٔ عربی بپذیریم، این حلقهٔ پایانی قطعی است: «حور» فارسی (و صورت واحدسازِ «حوری» و ترکیب «حوروش») وام‌واژه‌ای عربی و قرآنی است که همراه با واژگان بهشت اسلامی وارد فارسی شده است (ویکی‌واژه: عربی حور ← فارسی کلاسیک حور، و از آنجا اردو و پنجابی و سندی). فارسی‌زبانان جمعِ عربی را مفرد پنداشتند و «یاءِ وحدت» بر آن افزودند و «حوری» ساختند که از فارسی به ترکی و فرانسه (houri) و انگلیسی رفت (لوکوچ ش۸۴۸، کلاین). پس این گره درست است؛ اما «رفت و برگشتِ» ادعایی نمودار تنها بر پایهٔ فرضِ مورد مناقشهٔ ویدنگرن رفت و برگشت است.\",\n \"sources\": [SRC_HUR],\n \"ref_check\": [{\"ref\": \"MON:1378\", \"status\": \"not_checked\", \"note\": \"the local Mo'in OCR (MON_part1/part2) does not contain the حور entry (grep 'حور' returns only محور/بحور etc.), and the vajehyab/abadis route was not used; the Arabic origin was checked in Klein, Lokotsch and Wiktionary instead\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. houri\", \"stance\": \"supports\", \"note\": \"'fr. Pers. hūrī, fr. Arab. ḥūr ... The -ī in Pers. hūrī is a formative element serving to denote the singular'\"},\n   {\"src\": \"LKT\", \"where\": \"no. 848\", \"stance\": \"supports\", \"note\": \"'Dieses Wort betrachteten die Perser ... als sglr. und fügten ein ī der Einheit an: ḥūrī ... hieraus ... sp. hurí, frz. houri, engl. houri, dtsch. Huri'\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1/part2 grep 'حور'\", \"stance\": \"silent\", \"note\": \"the cited entry (vol. 1 p. 1378) is not in the available OCR\"}]})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Su 1, Esu, Wesu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h1su- 'good, well' (prefix; Skt su-, Av. hu-, OP u-, Gk. eu-), beside the u-stem adjective *h1wesu- 'good' (Skt vásu-, Av. vohu-/vaŋhu-, Gaul. Vesu-)\",\n \"note\": \"Nourai's triple heading reproduces Pokorny exactly: 'esu-s (: su-)' p.342, 'su-, sū- Meaning: well, good' pp.1037-38, and 'u̥esu- Meaning: good' pp.1174-75, with Pokorny himself cross-referring esu-s to su-. Watkins/AHD has both ('esu-. Good. Extension of es- ... [Pok. esu-s 342]'; 'su-. Well, good ... [Pok. su- 1037]'), Mann's IEC prints 'esus (əsus, su-) (1) \\\"good, true\\\". Cf. su-, uesus', and Klein's eu- entry (the cited KLN:548) connects Greek eu-/ἠύς with 'OI. vasuh, Avestic vohu-, \\\"good\\\"'. So the language label (Indo-European) and the gloss ('well, good') are right and the three shapes are the standard ones. The one caveat is that current handbooks keep *h1su- (prefix/adverb) and *h1wesu- (adjective) apart as two formations — Wiktionary calls *h1su- a 'possible metathesis of *h1wes-' or a zero grade of a reduplicated *h1es- — so the box merges what is today usually presented as a probable but unproven relationship. Every Avestan and Persian derivative on this page belongs to the hu- (*h1su-) side, not to the vohu- (*h1wesu-) side.\",\n \"note_fa\": \"سه‌گانهٔ نورایی («Su 1، Esu، Wesu») دقیقاً بازتاب پوکورنی است: «esu-s (: su-)» در ص۳۴۲، «su-, sū- «خوب، نیک»» در ص۱۰۳۷ و «u̯esu- «خوب»» در ص۱۱۷۴؛ خودِ پوکورنی نیز esu-s را به su- ارجاع می‌دهد. واتکینز (پیوست ریشه‌های هندواروپایی) هر دو را دارد، مان در فرهنگ تطبیقی خود «esus (əsus, su-) «خوب، راستین»؛ قس su-, uesus» می‌نویسد، و کلاین در ص۵۴۸ ذیل پیشوند eu- یونانی آن را با vasu- سنسکریت و vohu- اوستایی می‌سنجد. پس برچسب زبانی و معنای جعبه درست است. تنها نکته این است که پژوهش امروزی *h₁su- (پیشوند) و *h₁wesu- (صفت) را دو ساختِ جداگانه می‌داند که پیوندشان محتمل ولی اثبات‌نشده است؛ نورایی این دو را یکی گرفته است. همهٔ مشتقات اوستایی و فارسی این صفحه به شاخهٔ hu- بازمی‌گردند نه به شاخهٔ vohu-.\",\n \"sources\": [SRC_PIE],\n \"ref_check\": [\n   {\"ref\": \"POK:342\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: esu-s (: su-) Meaning: good ... Gr. ἠύς, εὖ ... Hittite a-as-su-us ... See also: es- Page(s): 342'\"},\n   {\"ref\": \"POK:1037\", \"status\": \"supports\", \"note\": \"'Root / lemma: su-, sū- Meaning: well, good. Material: Old Indic su-, Avestan hu-, Old pers. u- ... Page(s): 1037-1038'\"},\n   {\"ref\": \"POK:1174\", \"status\": \"supports\", \"note\": \"'Root / lemma: u̥esu- Meaning: good. Material: Old Indic vasu- \\\"good\\\" ... Avestan vaŋhu-, vohu- ... Page(s): 1174-1175'\"},\n   {\"ref\": \"KLN:548\", \"status\": \"supports\", \"note\": \"Klein s.v. eu-: 'combining form meaning \\\"good, well\\\". — Fr. Gk. eu, \\\"well\\\", prop. neut. of ἠύς, \\\"good\\\", which is cogn. either with Hitt. ashshush, \\\"good\\\", or — more probably — with OI. vasuh, Avestic vohu-, \\\"good\\\", Ir. feb (fr. I.-E. *wesw-a)' — exactly the Esu/Wesu equation of the box\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 161 (esu-s) and Bd. I 311 (u̥esu-)\", \"stance\": \"supports\", \"note\": \"the two headings Pokorny cites as 'WP. I 161' and 'WP. 1311'; Bd. I p.311 'uesu- \\\"gut\\\" (voller ǵuesu-)' with Gaul. Bello-, Sigo-vesus, OIr. feib\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. esu-, su-\", \"stance\": \"supports\", \"note\": \"'esu-. Good. Extension of es-. Greek eus, good, combining form eu-, well: EU-. [Pok. esu-s 342.]'; 'su-. Well, good ... [Pok. su- 1037.]'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. esus (1)\", \"stance\": \"supports\", \"note\": \"'esus (əsus, su-) (1) \\\"good, true\\\". Cf. su-, uesus. Cf. WP II 512; I, 161. Skt. cf. su-, px.; Av. hu-, id.; ... Myc. Gk. eu-, px.; Hom. ēü-; ... Hitt. assus'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §16.71 'good' and §4.83\", \"stance\": \"supports\", \"note\": \"'fr. *su-gʷiyes, cpd. of IE *su- \\\"well\\\" (Skt. su-, Av. hu-, etc.)'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. eu-\", \"stance\": \"supports\", \"note\": \"quoted above\"}],\n \"nodes\": nodes,\n}\n\nout = {\n \"pdf_page\": 484,\n \"book_page\": 454,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-484.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", len(nodes), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-484.py",
 "description": "Write verification JSON for page 484"
}
```


### [2026-09-14T03:29:35.159Z] TOOL RESULT

```
written 17 nodes
```


## [2026-09-14T03:29:39.563Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-484.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 484",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T03:29:40.785Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'confirmed': 5, 'plausible': 7, 'disputed': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'partial': 8, 'not_found': 6, 'not_checked': 13, 'contradicts': 1}
books consulted: {'supports': 23, 'partial': 17, 'silent': 8, 'contradicts': 5} | by book: {'BRT': 9, 'PHD': 9, 'KLN': 6, 'BQT': 4, 'HRN': 3, 'NYB': 3, 'FVQ': 3, 'POK': 2, 'HUB': 2, 'CHEUNG': 2, 'KNT': 2, 'LKT': 2, 'AHD': 1, 'HJB': 1, 'GPL': 1, 'WEB': 1, 'FSD': 1, 'MON': 1}
```


## [2026-09-14T03:29:59.951Z] AGENT

Page 484 done — `data/verification/page-484.json`, `verify_check.py 484` reports 0 PROBLEM lines.

**Counts** (1 entry, root `Su 1, Esu, Wesu` = confirmed; 17 nodes): confirmed 5, plausible 7, disputed 4, transcription_suspect 1. Ref checks: 9 supports, 8 partial, 1 contradicts, 6 not_found, 13 not_checked (FAF, ZMA, MAG/Widengren, MON:1378 not accessible).

**disputed**
- #8 Av. box `hu-parathwa "good to be crossed"` — no such Avestan word; it is the old folk-etymology of OP *Ufrātu-*, which Kent and Wiktionary derive from Akkadian *Purattu* < Sumerian *Buranun*. (The other four members — hu-jasta, hu-rama, hu-srav, hu-māyā — are all attested; the node takes the worst verdict.)
- #9 Persian box — two bad words: **فرات** (an Arabic loan of the Akkadian name, not "the crossable river") and **خسر/خسور** "father-in-law" (Av. x̌asura-, PIE *swéḱuros — said on the very Horn page, p.108 no.486, that Nourai cites, and in Mo'in's footnote to Borhān p.747). خجسته، خرم، خسرو، هما all confirmed.
- #10 Greek *Euphrates* — transmitted via Old Persian, yes, but not from an Iranian compound.
- #16 Arabic **ḥūr** — native plural of aḥwar/ḥawrāʾ (root ḥ-w-r "white"), pre-Islamic; Jeffery (= Nourai's own VDQ:39) grants Iranian influence only on the *concept*, not the word. The direct Pahlavi > Arabic arrow is Widengren's maximal position.

**transcription_suspect**
- #14 `hava-rd` — impossible Avestan form; the printed page really prints it (`error_in: book`), correct form Av. **hu-raoδa-** (Bartholomae col.1836, Pahlavi gloss *hurust* = node #15).

**Extraction errors for the owner:** none — the JSON is faithful to the page everywhere I checked. But note the book itself swaps two transliterations in node #9: it prints "xosor" beside خسرو (کسری) and "xosrow" beside خُسر (خسور، خسوره); recorded via `error_in`/`book_prints`/`correct_form`. Also, the reference sets are loose: BQT:2174/2297 in node #3 are the pages for نوا and وید (2174 actually belongs to خنیا in node #7), and BQT:717 is one page off from the خجسته footnote (p.716).

Page image archived at `data/verification/sources/refs/ocr/BOOK/484.png`; 16 web pages archived via `fetch_source.py`. Nothing committed.
