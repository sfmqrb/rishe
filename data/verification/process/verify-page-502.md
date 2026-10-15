# Verification process log — verify-page-502


## [2026-10-15T02:44:16.175Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 502 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-502.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-502.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-502.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 502` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.216Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.273Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.293Z] TOOL RESULT

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


## [2026-10-15T02:44:19.964Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-502.txt"
}
```


### [2026-10-15T02:44:19.987Z] TOOL RESULT

```
1	=== PDF page 502 (book page 472) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ten 1, Tengh, Temp : to stretch, pull  (refs POK:1064,1067)  PART 2
4	#1 (parent #0) [Latin] refs=AHD; POK | tendere : to stretch ; tenere : to hold, keep ; ana-tempa : stretched sail, antenna
5	  #2 (parent #1) [French] refs=KLN:1587 | 
6	    #3 (parent #2) [Persian] refs=None | ânten «آنتن» : "stretched out (sail)" ; tenîs «تنیس»
7	  #4 (parent #1) [English] refs=None | tent, contain, tennis, antenna, temperature, tension
8	#5 (parent #0) [Indo-European] refs=AHD; POK | Tenu : thin
9	  #6 (parent #5) [Avestan] refs=POK:1069; BQT:411,515 | tanu : body ; a-puthra-tanu : with child in body ☞Pôu ; taxma-tanu : with strong body ☞Tenk ; pešô-tanu : with condemned body
10	    #7 (parent #6) [Persian] refs=HRN:88; BQT:524; VSF:16 | tanîdan «تَنیدن ( تَنِش )» : to stretch, pull ; tan «تَن» : "stretched" body ; âbestan «آبستن» : "holding child in body" ; Tahamtan «تهمتن» : "with strong body" ; Pašŭtan «پشوتن» : "with condemned body"
11	  #8 (parent #5) [Sanskrit] refs=POK:1069 | tanuka : thin, soft
12	    #9 (parent #8) [Persian] refs=HRN:89; BQT:519; MON:1154 | tonok «تُنُک» : thin, little ; tonekeh «تُنکه» : underwear from thin soft cloth | NOTE: See root "Kitu" for another possible root of "tonekeh"
13	  #10 (parent #5) [Greek] refs=AHD | tonos : string
14	    #11 (parent #10) [French] refs=AHD | 
15	      #12 (parent #11) [Persian] refs=MON:1145 | ton «تُن» : tone
16	      #13 (parent #11) [English] refs=AHD | tone
17	  #14 (parent #5) [Germanic] refs=AHD | thunw : stretched, thin
18	    #15 (parent #14) [English] refs=AHD | thin
19	--- entry 1 ---
20	ROOT [Indo-European] Ten 2, Stena : to thunder  (refs POK:1021)
21	#1 (parent #0) [Parthian] refs=POK:1021 | tndwr : thunder
22	  #2 (parent #1) [Persian] refs=BQT:517; KLN:1613 | tondar «تُندر» : thunder
23	#3 (parent #0) [Germanic] refs=AHD | thunaraz
24	  #4 (parent #3) [English] refs=AHD | thunder
25	#5 (parent #0) [Latin] refs=AHD | tonâre : to thunder
26	  #6 (parent #5) [English] refs=AHD | tornado, detonate, astonish
27	
```


## [2026-10-15T02:44:21.127Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-502.json"
}
```


### [2026-10-15T02:44:21.173Z] TOOL RESULT

```
1	{
2	  "pdf_page": 502,
3	  "book_page": 472,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Ten 1, Tengh, Temp",
8	        "lang": "Indo-European",
9	        "refs": "POK:1064,1067",
10	        "gloss": "to stretch, pull"
11	      },
12	      "part": 2,
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Latin",
18	          "refs": "AHD; POK",
19	          "words": [
20	            {"translit": "tendere", "gloss": "to stretch", "script": null},
21	            {"translit": "tenere", "gloss": "to hold, keep", "script": null},
22	            {"translit": "ana-tempa", "gloss": "stretched sail, antenna", "script": null}
23	          ],
24	          "script_extra": null,
25	          "note": null,
26	          "quote": null
27	        },
28	        {
29	          "id": 2,
30	          "parent": 1,
31	          "lang": "French",
32	          "refs": "KLN:1587",
33	          "words": [],
34	          "script_extra": null,
35	          "note": null,
36	          "quote": null
37	        },
38	        {
39	          "id": 3,
40	          "parent": 2,
41	          "lang": "Persian",
42	          "refs": null,
43	          "words": [
44	            {"translit": "ânten", "gloss": "\"stretched out (sail)\"", "script": "آنتن"},
45	            {"translit": "tenîs", "gloss": null, "script": "تنیس"}
46	          ],
47	          "script_extra": null,
48	          "note": null,
49	          "quote": null
50	        },
51	        {
52	          "id": 4,
53	          "parent": 1,
54	          "lang": "English",
55	          "refs": null,
56	          "words": [
57	            {"translit": "tent, contain, tennis, antenna, temperature, tension", "gloss": null, "script": null}
58	          ],
59	          "script_extra": null,
60	          "note": null,
61	          "quote": null
62	        },
63	        {
64	          "id": 5,
65	          "parent": 0,
66	          "lang": "Indo-European",
67	          "refs": "AHD; POK",
68	          "words": [
69	            {"translit": "Tenu", "gloss": "thin", "script": null}
70	          ],
71	          "script_extra": null,
72	          "note": null,
73	          "quote": null
74	        },
75	        {
76	          "id": 6,
77	          "parent": 5,
78	          "lang": "Avestan",
79	          "refs": "POK:1069; BQT:411,515",
80	          "words": [
81	            {"translit": "tanu", "gloss": "body", "script": null},
82	            {"translit": "a-puthra-tanu", "gloss": "with child in body", "script": null, "see": ["Pôu"]},
83	            {"translit": "taxma-tanu", "gloss": "with strong body", "script": null, "see": ["Tenk"]},
84	            {"translit": "pešô-tanu", "gloss": "with condemned body", "script": null}
85	          ],
86	          "script_extra": null,
87	          "note": null,
88	          "quote": null
89	        },
90	        {
91	          "id": 7,
92	          "parent": 6,
93	          "lang": "Persian",
94	          "refs": "HRN:88; BQT:524; VSF:16",
95	          "words": [
96	            {"translit": "tanîdan", "gloss": "to stretch, pull", "script": "تَنیدن ( تَنِش )"},
97	            {"translit": "tan", "gloss": "\"stretched\" body", "script": "تَن"},
98	            {"translit": "âbestan", "gloss": "\"holding child in body\"", "script": "آبستن"},
99	            {"translit": "Tahamtan", "gloss": "\"with strong body\"", "script": "تهمتن"},
100	            {"translit": "Pašŭtan", "gloss": "\"with condemned body\"", "script": "پشوتن"}
101	          ],
102	          "script_extra": null,
103	          "note": null,
104	          "quote": {"text": "کای خرد و نیروی تو زال و تهمتن - پیکر و رایت سفندیار و پشوتن", "poet": "Qâânî"}
105	        },
106	        {
107	          "id": 8,
108	          "parent": 5,
109	          "lang": "Sanskrit",
110	          "refs": "POK:1069",
111	          "words": [
112	            {"translit": "tanuka", "gloss": "thin, soft", "script": null}
113	          ],
114	          "script_extra": null,
115	          "note": null,
116	          "quote": null
117	        },
118	        {
119	          "id": 9,
120	          "parent": 8,
121	          "lang": "Persian",
122	          "refs": "HRN:89; BQT:519; MON:1154",
123	          "words": [
124	            {"translit": "tonok", "gloss": "thin, little", "script": "تُنُک"},
125	            {"translit": "tonekeh", "gloss": "underwear from thin soft cloth", "script": "تُنکه"}
126	          ],
127	          "script_extra": null,
128	          "note": "See root \"Kitu\" for another possible root of \"tonekeh\"",
129	          "quote": null
130	        },
131	        {
132	          "id": 10,
133	          "parent": 5,
134	          "lang": "Greek",
135	          "refs": "AHD",
136	          "words": [
137	            {"translit": "tonos", "gloss": "string", "script": null}
138	          ],
139	          "script_extra": null,
140	          "note": null,
141	          "quote": null
142	        },
143	        {
144	          "id": 11,
145	          "parent": 10,
146	          "lang": "French",
147	          "refs": "AHD",
148	          "words": [],
149	          "script_extra": null,
150	          "note": null,
151	          "quote": null
152	        },
153	        {
154	          "id": 12,
155	          "parent": 11,
156	          "lang": "Persian",
157	          "refs": "MON:1145",
158	          "words": [
159	            {"translit": "ton", "gloss": "tone", "script": "تُن"}
160	          ],
161	          "script_extra": null,
162	          "note": null,
163	          "quote": null
164	        },
165	        {
166	          "id": 13,
167	          "parent": 11,
168	          "lang": "English",
169	          "refs": "AHD",
170	          "words": [
171	            {"translit": "tone", "gloss": null, "script": null}
172	          ],
173	          "script_extra": null,
174	          "note": null,
175	          "quote": null
176	        },
177	        {
178	          "id": 14,
179	          "parent": 5,
180	          "lang": "Germanic",
181	          "refs": "AHD",
182	          "words": [
183	            {"translit": "thunw", "gloss": "stretched, thin", "script": null}
184	          ],
185	          "script_extra": null,
186	          "note": null,
187	          "quote": null
188	        },
189	        {
190	          "id": 15,
191	          "parent": 14,
192	          "lang": "English",
193	          "refs": "AHD",
194	          "words": [
195	            {"translit": "thin", "gloss": null, "script": null}
196	          ],
197	          "script_extra": null,
198	          "note": null,
199	          "quote": null
200	        }
201	      ]
202	    },
203	    {
204	      "root": {
205	        "name": "Ten 2, Stena",
206	        "lang": "Indo-European",
207	        "refs": "POK:1021",
208	        "gloss": "to thunder"
209	      },
210	      "nodes": [
211	        {
212	          "id": 1,
213	          "parent": 0,
214	          "lang": "Parthian",
215	          "refs": "POK:1021",
216	          "words": [
217	            {"translit": "tndwr", "gloss": "thunder", "script": null}
218	          ],
219	          "script_extra": null,
220	          "note": null,
221	          "quote": null
222	        },
223	        {
224	          "id": 2,
225	          "parent": 1,
226	          "lang": "Persian",
227	          "refs": "BQT:517; KLN:1613",
228	          "words": [
229	            {"translit": "tondar", "gloss": "thunder", "script": "تُندر"}
230	          ],
231	          "script_extra": null,
232	          "note": null,
233	          "quote": null
234	        },
235	        {
236	          "id": 3,
237	          "parent": 0,
238	          "lang": "Germanic",
239	          "refs": "AHD",
240	          "words": [
241	            {"translit": "thunaraz", "gloss": null, "script": null}
242	          ],
243	          "script_extra": null,
244	          "note": null,
245	          "quote": null
246	        },
247	        {
248	          "id": 4,
249	          "parent": 3,
250	          "lang": "English",
251	          "refs": "AHD",
252	          "words": [
253	            {"translit": "thunder", "gloss": null, "script": null}
254	          ],
255	          "script_extra": null,
256	          "note": null,
257	          "quote": null
258	        },
259	        {
260	          "id": 5,
261	          "parent": 0,
262	          "lang": "Latin",
263	          "refs": "AHD",
264	          "words": [
265	            {"translit": "tonâre", "gloss": "to thunder", "script": null}
266	          ],
267	          "script_extra": null,
268	          "note": null,
269	          "quote": null
270	        },
271	        {
272	          "id": 6,
273	          "parent": 5,
274	          "lang": "English",
275	          "refs": "AHD",
276	          "words": [
277	            {"translit": "tornado, detonate, astonish", "gloss": null, "script": null}
278	          ],
279	          "script_extra": null,
280	          "note": null,
281	          "quote": null
282	        }
283	      ]
284	    }
285	  ]
286	}
287	
```


## [2026-10-15T02:44:24.830Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; ls sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','HRN','BQT','MON','VSF','WLD','IEC','SYN','BRT','PHD','NYB','HUB','ARY','SKT','CHEUNG']:\n  v=d.get(k);print(k, v and {x:v.get(x) for x in ['local_file','page_offset','lookup_hint']})\n\""
}
```


### [2026-10-15T02:44:25.386Z] TOOL RESULT

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
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
KLN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
HRN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
BQT {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
VSF {'local_file': None, 'page_offset': None, 'lookup_hint': 'Not found.'}
WLD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
IEC {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
SYN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
BRT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
PHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
NYB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
HUB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
ARY {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
SKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
CHEUNG None
```


## [2026-10-15T02:44:28.119Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:5000])\"; wc -l tools/verify_check.py; grep -n \"PROBLEM\" tools/verify_check.py | head -40"
}
```


### [2026-10-15T02:44:28.572Z] TOOL RESULT

```
{
 "pdf_page": 499,
 "book_page": 469,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-10-14",
 "entries": [
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
     "note": "Klein 1966 (KLN_1966.txt leaf 75 = c. pp.122-127 by the two-pages-per-leaf offset; the Atlas entry is the one Nourai means) s.v. Atlas: 'Gk. τλῆναι derives fr. *tl-, zero degree of I.-E. base *tel-, *tal-, *tol-, 'to bear, lift, suffer', whence τάλας ... τάλαντον, ... L. tollere 'to lift up, raise', tolerare 'to bear, support''."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I pp.738-740 s.v. 1. tel-",
     "stance": "supports",
     "note": "Walde-Pokorny Bd. I pp.738-740 (local WLD_Bd1_pages.txt leaves 747-749) '1. tel- „aufheben, z. T. wägend, z. T. sich aufladend; tragen; ertragen, dulden“: Ai. tulā „Waage, Waagbalken“, tulayati „hebt auf, wägt“' ... 'τάλαντον ... eig. „die beiden Waagschalen“', 'Ἄτλας, -αντος', 'lat. tollo ... tolero ... lātus'."
    },
    {
     "src": "AHD",
     "where": "Watkins s.v. telə-",
     "stance": "supports",
     "note": "Watkins AHD Roots (local AHD_watkins1985.txt line 1078) s.v. telə-: 'To lift, support, weigh; with derivatives referring to measured weights and thence to money and payment' — 2a 'Greek telos, tax, charge: TOLL1'; 2b 'Latin tolerare ... TOLERATE'; 4 '*tala-nt- in Greek talanton, balance, weight ... TALENT'; 6 'Perhaps zero-grade form *tla- in Greek Atlas ... ATLANTIC, ATLAS'; 8 '*tl-to- in Latin lātus ... RELATE ... TRANSLATE'; 9 '*tl-ā- in Sanskrit tulā, scales, balance, weight'; 10 '*tl-n-a- in Latin tollere'. [Pok. 1. tel- 1060.]"
    },
    {
     "src": "IEC",
     "where": "s.v. tl- (1) (line 18624)",
     "stance": "supports",
     "note": "'tl- (1) (tlō, tolō, iō) 'lift, raise, bear, suffer'. WP I, 701 & 738-9 ... Tokh. A B tal-, v. 'lift, carry'; Gk. tlēmi, aor. etlēn 'bear, support, suffer'; Lat. perf. (te)tulī; Go. þulan'."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Sanskrit",
     "words": "tulâ, tulya",
     "verdict": "confirmed",
     "derivation": "Sanskrit tulā́ f. 'balance, scales; weight' continues the zero grade *tl̥h₂-éh₂ of PIE *telh₂- 'to lift, weigh, bear': syllabic *l̥ before the laryngeal gives Indo-Aryan ul (the l is the dialectal Indo
98 tools/verify_check.py
90:        print("PROBLEM:", p)
```


## [2026-10-15T02:44:29.862Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat tools/verify_check.py"
}
```


### [2026-10-15T02:44:30.202Z] TOOL RESULT

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


## [2026-10-15T02:44:32.979Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/502.jpg && python3 -c \"\nfrom PIL import Image; im=Image.open('site/pages/502.jpg'); print(im.size)\""
}
```


### [2026-10-15T02:44:33.681Z] TOOL RESULT

```
Exit code 1
Permissions Size User   Date Modified Name
.rw-r--r--   78k sfmqrb 14 Oct 22:15  site/pages/502.jpg
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image; im=Image.open('site/pages/502.jpg'); print(im.size)
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-15T02:44:36.839Z] TOOL CALL #8: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && pdftoppm -f 502 -l 502 -r 200 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf pg502 && ls -la pg502.png"
}
```


### [2026-10-15T02:44:37.732Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   82k sfmqrb 14 Oct 22:44  pg502.png
```


## [2026-10-15T02:44:39.492Z] TOOL CALL #9: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg502.png"
}
```


### [2026-10-15T02:44:39.847Z] TOOL RESULT

```

```


## [2026-10-15T02:44:39.843Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-15T02:45:11.314Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"lemma: ten-\\|lemma: (s)ten\\|lemma: temp\\|lemma: tengh\\|lemma: stene\\|lemma: \\(s\\)\\?ten\" POK_full.txt | head; grep -n \"^ten-\\|^tenə-\\|^temp-\\|^\\(s\\)ten\\|^stenə\\|^tengh\" AHD_watkins1985.txt | head"
}
```


### [2026-10-15T02:45:11.672Z] TOOL RESULT

```
81943:Root / lemma: (s)ten-1 
81980:Root / lemma: sten-2 
85453:Root / lemma: temp- 
85500:Root / lemma: tend- 
85506:Root / lemma: tenagos, tenagos 
85516:Root / lemma: tengh- 
85550:Root / lemma: teng-1 
85563:Root / lemma: teng-2 
85569:Root / lemma: tenk-1 
85591:Root / lemma: tenk-2 
1077:temp-
1079:ten-
```


## [2026-10-15T02:45:13.734Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 81943,81980p POK_full.txt; sed -n 85453,85550p POK_full.txt | cut -c1-600; grep -n \"lemma: ten-\\|lemma: ten\\b\\|lemma: tenu\" POK_full.txt"
}
```


### [2026-10-15T02:45:14.367Z] TOOL RESULT

```
Root / lemma: (s)ten-1 

Meaning: to groan, etc.. 

Material: Old Indie stanati{= gr. gtevu). Old English stenan, Lithuanian stenu), staniti, 

stanayaf/ "donnert, drohnt, bellow, roar, braust', stanay/tnu-m. "thunder', tanayitnu- 

"drohnend, donnernd', /^/7y5//(= Aeolic tevvei) " soughs, sounds, donnert', tanyu-' 

soughing, thundering '; afghan. /a/7a "thunder', np. fundards.; Old \nd\c abh/'-stana- m. " 

din, noise '; 



gr. otevcjo "drohne, achze, lament', Ionian arsivu) (= Old Church Slavic stenjg) ds., 
aiEva^u) ds., aT£vaY|j6(; 'das sigh ', arsvaxu) ds., arovoc; m. " the groaning ', cxsa-aiovoo, 
"very stohnend' (Old Indie abh/-stana-'6as Tosen, shout', russ. ston's\g\r\'), Itevtojp; 
Lesbian tevvei otsvsi, ppuxsTOi Hes.; 

Latin tono, -are " thunder; also from other lauten Schalleindrucken', to-nitru, tonitrus 
"thunder'; Celtic FIN Tanaros{: Old High German donar); 

Old English stenan siem V. "groan, moan'; Middle Low German stenensdcm. V. ds. 
{*stanjan= Old Indie stanayati); Old Icelandic stynja ds. = Middle Low German stonen 
(Modern High German stohnen); Old Icelandic sfynrm. "Gestohne', Old English gestunn. 
"din, fuss, noise, whirlwind'; Old Icelandic stanka'groan, moan'. Old English stenecian 
"pant, gasp'; Old High German o'c»/75/'" thunder'. Old English f^unords., Old Icelandic f^orr' 
Thunder God ', Old English dun/an^ thunder, roar, bellow, sigh'; 

Lithuanian stenu, -etT groan, groan, moan'. Old Church Slavic stenjg, stenatids.; russ. 
s/d/7" the groaning '; Old Prussian *stint, s//77c»/7s participle Perf. Akt. "gelitten'. 

References: WP. II 626 f., WH. II 690 f., Trautmann 286.; VasmerS, 10, 19. 
Page(s):1021 

Root / lemma: sten-2 
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
85648:Root / lemma: ten-1, tend- 
85662:Root/ lemma: ten-1, tend-: "to extend, stretch, span' derived from the extended Root/ 
85748:Root / lemma: ten-2 
85789:Root / lemma: tenu-s, tenu-s
```


## [2026-10-15T02:45:17.493Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 85648,85830p POK_full.txt | grep -n -i \"tanu\\|tenu\\|tonos\\|tend\\|teneo\\|tan-\\|Page\\|thin\\|þunn\\|np\\.\\|npers\\|Avest\\|tanuka\\|tunuk\" | head -60"
}
```


### [2026-10-15T02:45:18.577Z] TOOL RESULT

```
1:Root / lemma: ten-1, tend- 
3:Meaning: to extend, stretch, span 
9:with -e^-extension (ved. tanoti, tanute, gr. hom. Tavurai) or vie/o-suffix shaped (gr. Tsivoj); 
11:compare /e/7i/-5"thin' and die extensions tengh-, tenk-, temp-, tens-. 
15:Root/ lemma: ten-1, tend-: "to extend, stretch, span' derived from the extended Root/ 
19:Material: Old Indie /a/7d7/"dehnt, spannt, erstreckt sich, dauert', Avestan pairi-tanava 1 . Sg. 
21:Konj. Akt. "I will fernhalten', pairi-tanuya \ . Sg. Opt. Med.; Old Indie ut-tana- "ausgestreckf 
23:= Avestan ustana- ds. ( *tnn6-, compare Old Indie tani-man- n. "Dunne', also Lithuanian 
25:t'inti, Latin tene-re); np. tamdan^iuru, spinnen'; as o^-present (as Latin tendd) Old Indie 
32:tan- "Ausbreitung, Fortdauer, Fortpflanzung, progeny ', Instr. /a/75 "continue', tana- m. " 
33:descendant ', tana-m, tana, tanas- n. " progeny '; tantra-m 'Zette\, Aufzug am loom' = np. 
34:/^/'(Avestan *t^&ra-) ds., afghan. /©/""net'; Old Indie tana- m. "clay, filament ' (compare gr. 
35:t6vo(;); perhaps here tanu-i. "body, person, Selbst' = Avestan tanu-i. ds. (Mayrhofer 475); 
37:gr. TavuTQi "streckt sich' (= Old Indie tanute), ravucjo (sravuaa etc.) "streeke, dehne'; 
40:"sinew, straff angezogenes Band' (= Latin tenus, -oris, compare also Old Indie tanas-v\.), 
44:{*tnt/s); about tovu- "sich ausbreitend' see below tenus, 
53:Latin tendo, -ere, tetendi, tentum, newer M/75i//77'spannen, distend, ausstrecken' 
54:(originally o'-present) = Umbrian an-, e/7-/e/7/^"intendito', i/s/e/7/^"ostendito' etc., Latin 
55:tentus, (in-)tentia, teneo, -ere, tenui{0\6 Latin tetinT= Old Indie tatan§), tentum^\\o\6, stop 
60:tenus, -or/'sn. "cord with loop, noose, snare ' (= gr. itvoq), tenor, -dr/src\. 
67:Maybe alb. tendos' strech ' a Latin loanword. 
74:Gothic uf-l=>anjan ^s\c\\ distend, sich ausstrecken'. Old Icelandic A'e/7/5"ausspannen, 
80:Middle High German donen ' s'\c\r\ distend, to swell, strotzen'; oto/? "ausgespannf. Middle 
82:branch, tendril ', Modern High German Dohne, Old English ^/Adc»/7e"Albranke, Solanum 
86:Lithuanian tinstu, t/nt/'to swell', /a/75S "swelling, lump, growth' ("*sich distend ', also of 
99:Page(s): 1065-1066 
105:Page(s): 1 067 
109:Meaning: to extend, stretch, span 
115:tasat^puW, with Gewalt set in motion ', /asa/a-zr? 'Weberschiffchen', v/tast/'-m.; Avestan 
125:Gothic 5/A'//75a/7'heranziehen', anid. thinsan^ z\e\\en, rend ', Old High German dinsan 
138:Page(s): 1068-1069 
142:Root / lemma: tenu-s, tenu-s 
144:Meaning: thin 
146:Grammatical information: fern. tenuT 
150:Material: Old Indie tanu-, fern. /5/71/rthin, tender, fragile, flimsy, insignificant ' {tanuka-6s. 
152:= Slavic tbnbkb); substantivized Old Indie tanu- f., tanus- n., Avestan tanO- f., tanus- n., np. 
159:Latin tenuis ^\h\v\, fine, tender' (from fem. *tenuT= Old Indie tanvT); gr. lavaFoq kann from 
162:Old Irish tan{a)e{W\\h secondary -e), corn, tanow, bret. tanao, /5/7c»"thin' (proto Celtic 
163:*tanauo-\ cymr. /e'/7e^verdankt sein edem influence of Latin tenuis); 
174:Old Church Slavic tbnbl<b "thin' (assimil. *tbnbl<b, russ. t6nl<ij). 
177:Page(s): 1 069
```


## [2026-10-15T02:45:21.192Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 85789,85825p POK_full.txt; sed -n 1077,1095p AHD_watkins1985.txt; grep -n \"^(s)tenə\\|^stenə\\|^\\(s\\)\\?tenə-\\|thunraz\\|thunaraz\" AHD_watkins1985.txt|head"
}
```


### [2026-10-15T02:45:21.693Z] TOOL RESULT

```
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

temp-
a. Latin téla, web, net, warp of a fabric, also weaver’s beam (to which the warp threads are tied): TILLER?, ToiL2; b. Latin subtilis, thin, fine, precise, subtle (< *sub-téla, “thread passing under the warp,” the finest thread; sub, under; see upo): SUBTLE. 3. Suffixed form *teks-On, weaver, maker of wattle for house walls, builder (possibly contaminated with *teks-tdr, builder), in Greek tekton, carpenter, builder: TECTONIC; ARCHITECT. 4. Suf- fixed form *teks-nd-, craft (of weaving or fabricating), in Greek tekhné, art, craft, skill: TECHNICAL, POLYTECHNIC, TECHNOLOGY. 5. Possibly Germanic *thahsu-, badger (“the animal that builds,” referring to its burrowing skill), in Old High German dahs (> German Dachs), badger but more likely borrowed from the same pre- Indo-European source as the Celtic totemic name Tazgo-, Gaelic Tadhg, “‘badger’”): DACHSHUND. [Pok. tekth- 1058.] tekv-. To run, flee. Suffixed o-grade form *tokv-so- in Iranian *taxsa-, bow, borrowed into Greek toxon, bow, also (in the plural) bow and arrow (< “that which flies’): Toxic. [Pok. tekz- 1059.] tel-. Ground, floor, board. 1. Germanic *thil-j6- in Middle Low German and Middle Dutch dele, plank: DEAL?. 2. Suffixed form *tel-n- in Latin telliis (stem telliir-), earth, the earth: (TELLURIAN), (TELLURIC), (TELLURION), (TELLURIUM), TELLURO-. 3. Possibly reduplicated form *ti-tel- in Latin titulus, placard, label, superscription, title: TITLE. [Pok. 2. tel- 1061.] tela-. To lift, support, weigh; with derivatives referring to measured weights and thence to money and payment. 1. Suffixed form *telo-mon- in Greek telamén, supporter, bearer: TELAMON. 2. Suffixed form *tel/a)-es- in: a. Greek telos, tax, charge: TOLL!; PHILATELY; b. Latin tolerdre, to bear, endure: TOLERATE. 3. Suffixed zero-grade form *th-i-, becoming *tali- (influenced by ¢dlis, such), in Latin ¢alid, reciprocal punishment in kind, “something paid out”: TALION; RETALIATE. 4. Suffixed variant zero-grade form *tala-nt- in Greek talanton, balance, weight, any of several specific weights of gold or silver, hence the sum of money represented by such a weight: TALENT. 5. Perhaps intensive reduplicated form *tantal- in Greek Tantalos, name of a legendary king, “the sufferer’: (TANTALIZE), TANTALUS. 6. Perhaps zero-grade form *tla- in Greek Atlas (stem Atlant-), name of the Titan supporting the world: ATLANTIC, ATLAS. 7. Suffixed zero-grade form *tl-é- in Germanic *thulén in Old English tholian, to suffer, endure: THOLE. 8. Suf- fixed zero-grade form *tl-to- in Latin ldtus, “carried, borne,” used as the suppletive past participle of ferre, to bear (see bher-'), with its compounds: ABLATION, COL- LATE, DILATORY, ELATE, ILLATION, LEGISLATOR, OB- LATE], PRELATE, PROLATE, RELATE, SUPERLATIVE, TRANSLATE. 9. Suffixed zero-grade form *tl-d- in San- skrit tuld, scales, balance, weight: TAEL, TOLA. 10. Nasal- ized zero-grade form *tl-n-a- in Latin tollere, to lift: EXTOL. [Pok. 1. éel- 1060.] tem-. Also teme-. To cut. I. Form *tema-. Nasalized form *t(e)m-n-a- in Greek temnein, to cut: TMESIS, TOME, -TOME, -TOMY; ANATOMY, ATOM, DIATOM, DICHOTOMY, ENTOMO-, EPITOME. II. Form *tem-. 1. Suffixed form *tem-lo- in Latin templum, temple, shrine, open place for observation (augury term < “place reserved or cut out”), small piece of timber: TEMPLE!, TEMPLE’; CONTEMPLATE. 2. Extended root *tem-d- becoming *tend- in o-grade suffixed (iterative) form *tond-eyo- in Latin tondére, to shear, shave: TONSURE. [Pok. 1. tem-, tend- 1062.] teme-. Dark. Suffixed form *tema-s-. 1. Latin temere, blindly, rashly: TEMERARIOUS, TEMERITY. 2. Suffixed form *temas-rd- in Latin tenebrae (plural), darkness: TENEBRAE, TENEBRIONID. [Pok. tem()- 1063.] temp-. To stretch. Extension of ten-. 1. Possibly Latin tempus, temple of the head (? where the skin is stretched from behind the eye to the ear): TEMPLE?. 2. Zero-grade form *tmp- perhaps in: a. Persian taftan, to weave (the
ten-
warp threads are stretched on the loom): TAFFETA; b. Iranian *tap-, “carpet,” in Greek tapés, carpet: TAPES- TRY. [Pok. temp- 1064.] ten-. To stretch. I. Derivatives with the basic meaning. 1. Suffixed form “ten-do- in: a. Latin tendere, to stretch, extend: TEND!, TENDER?, TENDON, TENSE!, TENT!; AT- TEND, CONTEND, DETENT, DISTEND, EXTEND, INTEND, OSTENSIBLE, PRETEND, SUBTEND; b. Latin portendere, “to stretch out before” (por-, variant of pro-, before; see per’), a technical term in augury, “to indicate, presage, foretell”: PORTEND. 2. Suffixed form *ten-yo- in Greek teinein, to stretch: TENESMUS; BRONCHIECTASIS, EPITA- SIS, HYPOTENUSE, PERITONEUM, PROTASIS, TELANGIEC- TASIA. 3. Suffixed zero-grade form *tn-nu- in Sanskrit tandéti, he stretches or weaves, with suffixed (instrumen- tal) derivative *ten-tro- in tantam, loom: TANTRA. 4. Suf- fixed form *ten-tro- in Persian ¢tdr, string: SITAR. 5. Basic form (with stative suffix) *ten-é- in Latin ten��re, to hold, keep, maintain (< “to cause to endure or con- tinue, hold on to”): TENABLE, TENACIOUS, TENACULUM, TENANT, TENEMENT, TENET, TENON, TENOR, TENURE, TENUTO; ABSTAIN, CONTAIN, CONTINUE, DETAIN, ENTER- TAIN, LIEUTENANT, MAINTAIN, OBTAIN, PERTAIN, PERTI- NACIOUS, RETAIN, (RETINACULUM), SUSTAIN. II. Derivatives meaning ‘‘stretched,” hence “thin.” 1. Suffixed zero-grade form *tn-u- in Germanic *thunw-, whence *thunniz in Old English thynne, thin: THIN. 2. Suffixed full-grade form *ten-u- in Latin tenuis, thin, rare, fine: TENUOUS; ATTENUATE, EXTENUATE. 3. Suf- fixed full-grade form *ten-ero- in Latin tener, tender, delicate: TENDER!, TENDRIL. III. Derivatives meaning “something stretched or capable of being stretched, a string.” 1. Suffixed form *ten-dn- in Greek tenén, ten- don: TENO-. 2. Suffixed o-grade form *ton-o- in Greek tonos, string, hence sound, pitch: TONE; TONOPLAST. 3. Suffixed zero-grade form *tn-ya- in Greek tainia, band, ribbon: TAENIA; POLYTENE. [Pok. 1. ten- 1065.] teng-. To soak. 1. Latin tingere, to moisten, soak, dye: TAINT, TINCT, TINGE, TINT; INTINCTION, STAIN. 2. Zero-grade form *tng- in Germanic *thunk- in Old High German thunk6n, dunk6n, to soak: punk. [Pok. 1. teng- 1067.] tenk-'. To stretch. Extension of ten-. Perhaps Germanic *thingam in: a. Old English thing, assembly, (legal) case, thing: THING; b. Old Norse thing, assembly: HUSTINGS; c. Old High German thing, ding (> German Ding), thing: DINGUS. [Pok. 1. tenk- 1067.] tenk-2, To become firm, curdle, thicken. 1. Suffixed form *tenk-to-, thickened, in Germanic *thinhtaz in Old Norse théttr, dense, watertight, akin to the Scandinavian source of Middle English thight, dense: TIGHT. 2. Possibly suffixed o-grade form *tonk-lo- in Germanic *thangul- in Old Norse théngull, seaweed (? < “thick mass”), akin to the source of TANGLE?. [Pok. 2. tenk- 1068.] tens-. To stretch, draw. Extension of ten-. Suffixed zero-grade form *tns-ero- in Sanskrit tasaram, shuttle: TussAH. [Pok. tens- 1068.] tep-. To be warm. Suffixed (stative) form *tep-é- in Latin tepére, to be warm: TEPID. [Pok. tep- 1069.] ter-. Base of derivatives meaning peg, post, boundary marker, goal. 1. Suffixed form *ter-men-, boundary marker, in Latin terminus, boundary, limit: TERM, TER- MINATE, TERMINUS; DETERMINE, EXTERMINATE. 2. Suf- fixed zero-grade form *tr-m- in Germanic *thrum- in Old English thrum, broken-off end (attested only in tungeth- rum, the ligament of the tongue): THRUM2. [Pok. 4. ter- 1074.] tera-1, To rub, turn; with some derivatives referring to twisting, boring, drilling, and piercing; and others refer- ring to the rubbing of cereal grain to remove the husks, and thence to the process of threshing either by the trampling of oxen or by flailing with flails. Variant *tré-, contracted from “*trea-. I. Full-grade form *ter@)-. 1. a. Latin terere (past participle tritus), to rub away,
70
ters-
thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
teu-
LOUS, TERRIGENOUS, VERDITER. 3. Suffixed o-grade form *tors-eyo- in Latin torrére, to dry, parch, burn: TOAST!, TORRENT, TORRID. 4. Suffixed zero-grade form *trs-o- in Greek tarsos, frame of wickerwork (originally for drying cheese), hence a flat surface, sole of the foot, ankle: TaRSUS. [Pok. ters- 1078.]
teu-. To pay attention to, turn to. 1. O-grade form *tou- in Germanic *thau- in Old English théaw, usage, custom (< “observance”): THEW. 2. Suffixed zero-grade form *tu-é- in Latin tuéri, to look at, watch, protect: TUITION, TUTOR; INTUITION. [Pok. 2. teu- 1079.]
teue-. Also teu-. To swell. 1. Extended form *teuk- in Germanic *theuham, “the swollen or fat part of the leg,” thigh, in Old English théoh, thigh: THIGH. 2. Extended form *tis- in Germanic compound *thiis-hundi-, “swollen hundred,” thousand (*hundi-, hundred; see dekm), in Old English thisend, thousand: THOUSAND. 3. Suffixed zero-grade form *tu-l- probably in Germanic *thul- in Old English thol(l), oar pin, oarlock (< “a swelling”): THOLE PIN. 4. Extended zero-grade form *tiim- in: a. Germanic *thimoén- in Old English thima, thumb (< “the thick finger”): THIMBLE, THUMB; b. suffixed (stative) form *tum-é- in Latin tumére, to swell, be swollen, be proud: TUMESCENT, TUMID, TUMOR; DETUMESCENCE, INTU- MESCE, TUMEFACIENT, TUMEFY; C. suffixed form *tum- olo- in Latin tumulus, raised heap of earth, mound: TUMULUS. 5. Extended lengthened zero-grade form *tibh- in Latin tiber, lump, swelling: TRUFFLE, TUBER; PROTUBERATE. 6. Suffixed zero-grade form *tu-r-yo- in Greek turos, cheese (< ‘“‘a swelling,” “coagulating”’): BUTTER, TYROSINE, TYROTHRICIN. 7. Suffixed variant form *tw6-ro- in Greek sdros, heap, pile: SORITES, SORUS. 8. Suffixed variant form *twd-mn, in Greek sdma, body (< “a swelling,” “stocky form”): SOMA, SOMATO-, -SOME?; PROSOMA. 9. Suffixed zero-grade form *twa-wo- in Greek saos, sds, safe, healthy (< “swollen,” “strong”), with derivative verb sdzein, to save, rescue: CREOSOTE, SOTE- RIOLOGY. 10. Perhaps nasalized extended form *tu-m-b(h)- (or extended zero-grade form *tum-) in Greek tumbos, barrow, tomb: TOMB. [Pok. téu- 1080.]
teuta-. Tribe. 1. Germanic *theudd-, people, with deriva- tive *theudiskaz, of the people, in Middle Dutch duutsch, German, of the Germans or Teutons: DuTcH; PLaATT- DEUTSCH. 2. Suffixed form ‘*teut-onds, “they of the tribe,” in Germanic tribal name *theudanéz, borrowed via Celtic into Latin as Teuténi, the Teutons: TEUTON. 3. Possibly Latin tétus, all, whole (? < “of the whole tribe”): TOTAL, TUTTI; FACTOTUM, TEETOTUM. [In Pok. téu- 1080.]
[threph-. To cause to grow, develop. Greek root (stem form treph-). 1. Greek trephein, to feed, nourish, and trophé, nourishment: (TROPHIC-), TROPHO-, -TROPHY; ATROPHY, CHEMOTROPHY, EUTROPHIC, PHOTOTROPH, (POLYTROPHIC). 2. Suffixed form *threph-ma in Greek thremma, creature (< “nursling”): THREMMATOLOGY. [In Pok. dherebh- 257.]]
[thrix. Hair. Greek word of unknown origin (stem form trikh-). TRICHINA, TRICHO-, TRICHOME, -TRICHOUS; PERI- TRICH, STREPTOTHRICIN, TYROTHRICIN, ULOTRICHOUS. [In Pok. dhrigh- 276.]]
tit-. Also tik-, kit-. To tickle. Expressive root. 1. Germanic *kit- in Old Norse kitla, to tickle, akin to the probable source of Middle English kytyllen, to tickle: KITTLE. 2. Latin fitilldre, to tickle, titillate: TITILLATE. [In Pok. geid- 356.]
tké-. To gain control of, gain power over. 1. Possibly in Indo-Iranian suffixed form *ksa-tram in: a. Sanskrit ksatram, rule, power, and ksayati, he rules: KSHATRIYA; b. Old Persian khshathra-, kingdom, province, in com- pound khshathra-pava, protector of the province (see pa-): SATRAP. 2. Possibly in Indo-Iranian *ksayati, has power over, rules, in Old Persian khshayathiya-, king, whence Persian shah, king: CHECK, SHAH; CHECKMATE. [Pok. Rthé(i)- 626.]
trei-
tkei-. To settle, dwell, be home. 1. Suffixed o-grade form *()koi-mo- in Germanic *haimaz, home, in: a. Old Eng- lish hdm, home: HOME; b. Old Norse heimr, home: NIFLHEIM; C. Middle Dutch hame, hame (< “covering”): HAME; d. Old French ham, village, home: HAMLET; e. Germanic *haimatjan, to go or bring home, in Old French hanter, to frequent, haunt: HAUNT. 2. Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHYCTYONY. 3. Probable zero-grade form *tki- in Latin si- in suffixed form *si-tu- in situs, location: SITUATE, SITUS. [Pok. 1. hei- 589, Athei- 539.] to-. Demonstrative pronoun. For the nominative singular see so-. 1. Germanic *thé- in: a. Old English thé, thy (instrumental case), by the: THE!, THE?; NATHELESS; b. Middle Dutch de, the: pEcoy. 2. Germanic *thauh, “for all that,” in Old Norse thd, though, akin to the Scandinavian source of Middle English though, though: THOUGH. 3. Germanic *thasi- in Old English thes, this, this: (THESE), THIS. 4. Germanic *thana- in Old English thanne, thenne, thenne, than, then: THAN, THEN. 5. Ger- manic *thanana- in Old English thanon, thence: THENCE. 6. Germanic *thér in Old English ther, thér, there: THERE. 7. Germanic *thathro in Old English theder, thider, thither: THITHER. 8. Germanic nomina- tive plural *thai in Old English tha and Old Norse their, they: THEY. 9. Germanic genitive plural *thaira in Old Norse their(r)a, theirs: THEIR. 10. Germanic dative plural *thaimiz in Old Norse theim and Old English thém, them: THEM. 11. Extended neuter form *tod- in: a. Ger- manic *that in Old English thet, that: THAT, (THOSE); b. Greek to, the: TAUTO-. 12. Germanic *thus- in Old English thus, thus: THUS. 13. Adverbial (originally accu- sative) form *tam in Latin tandem, at last, so much (> Anglo-Norman tant): TANDEM, TANTAMOUNT. 14. Suf- fixed reduced form *t-dli- in Latin tdlis (plural tdlés), such: TALES. [Pok. 1. to- 1086.] tolky-. To speak. Metathesized form *tlokv- in Latin loqui, to speak: LOCUTION, LOQUACIOUS; ALLOCUTION, CIRCUMLOCUTION, COLLOQUIUM, (COLLOQUY), ELOCU- TION, GRANDILOQUENCE, INTERLOCUTION, MAGNIL- OQUENT, OBLOQUY, PROLOCUTOR, SOLILOQUY, VENTRILOQUISM. [Pok. tolk¥- 1088.] tong-. To think, feel. 1. Germanic *thank6n in: a. Old English thancian, to thank: THANK; b. Old English thencan, to think: THINK. 2. Germanic *(ga)thauht- (*ga-, collective prefix; see kom) in Old English (ge)- thoht, thought: THOUGHT. 3. Germanic factitive *thunk- Jan in Old English thyncan (third person singular present indicative thyncth), to seem: METHINKS. [Pok. 1. tong- 1088.] tragh-. To draw, drag, move. Rhyming variant dhragh-. Latin trahere, to pull, draw: TRACT!, TRACTABLE, TRAC- TION, TRAIL, TRAIN, (TRAIT), TREAT; ABSTRACT, AT- TRACT, CONTRACT, DETRACT, DISTRACT, EXTRACT, PORTRAY, PROTRACT, RETRACT, SUBTRACT. [Pok. tragh- 1089.] treb-. Dwelling. 1. Zero-grade form *trb- in Germanic *thurp- in Old English thorp, village, hamlet: THORP. 2. Latin trabs, beam, timber: TRABEATED, TRABECULA, TRAVE; ARCHITRAVE. [Pok. treb- 1090.] trei-. Three. I. Nominative plural form *treyes. 1. Ger- manic *thrijiz in Old English thrie, thréo, thri, three, with its derivatives thriga, thriwa, thrice, and thritig, thirty, and thréotine, thirteen: THREE, THRICE, THIRTY, THIRTEEN. 2. Latin trés (> Italian tre and French trois), three: TREY, TRIO; TRAMMEL, TRECENTO, TREPHINE, TRIUMVIR, TROCAR. II. Zero-grade form *tri-. 1. Suffixed form *tri-tyo- in: a. Germanic *thridjaz, third, in (i) Old English thrid(d)a, thirdda, third: THIRD (ii) Old Norse thrithi, third: RIDING?; b. Latin tertius (neuter tertium), third: TERCEL, TERCET, TERTIAN, TERTIARY, TIERCE; SESTERCE. 2. Latin évi-, three: TRI-, TRIPLE. 3. Greek t7i-, three: TRI-; TRICLINIUM, TRICROTIC, TRIDACTYL, TRI- GLYPH, TRITONE. 4. Sanskrit tri, three: TRIMURTI.
trem-
1013:STICKLE. 3. Suffixed form *stigh-o- in Greek stikhos, row, line, line of verse: STICH; ACROSTIC, CADASTER, DISTICH, HEMISTICH, ORTHOSTICHOUS, STICHOMETRY, STICHO- MYTHIA. III. O-grade form *stoigh-. 1. Suffixed form *stoigh-ri- in Germanic *staigri in Old English stéger, stair, step: STAIR. 2. Greek stoikheion, shadow line, element: STOICHIOMETRY. [Pok. steigh- 1017.] steip-. To stick, compress. 1. Germanic *séifaz in: a. Old English séff, rigid, stiff: stirF; b. Dutch stip, tip, point: STIPPLE. 2. Latin stipes, post, tree trunk: STIPE, STIPES. 3. Suffixed form *steip-d- in Latin stipdre, to compress, stuff, pack: STEEVE!, STEVEDORE; CONSTIPATE. [Pok. stéib(h)- 1015.] stel-. To put, stand; with derivatives referring to a standing object or place. I. Basic form *stel-. 1. Suffixed form *stel-ni- in Germanic “*stilli- in Old English stile, quiet, fixed: sTILL’. 2. Suffixed form “stel-yo- in Greek stellein, to put in order, prepare, send, make compact (with o-grade and zero-grade forms sfol- and stal-): APOSTLE, DIASTOLE, EPISTLE, PERISTALSIS, SYSTALTIC. II. O-grade form *stol-. 1. Suffixed form *sfol-no- in Germanic *stalla- in: a. Old English steall, standing place, stable: STALL; FORESTALL; b. Old French estal, place: INSTALLMENT!; Cc. Old French estalon, stallion: STALLION; d. Old Italian stallo, stall: PEDESTAL; e. Me- dieval Latin stallum, stall: INSTALL; f. Germanic denomi- native *stalljan in Old High German stellen, to set, place: GESTALT. 2. Suffixed form stol-6n- in Latin stolé, branch, shoot: STOLON. 3. Suffixed form *stol-ido- in Latin stoli- dus, “firm-standing,” stupid: sTOLID. 4. Suffixed form *stol-d- in Greek stolé, garment, array, equipment: STOLE}, III. Zero-grade form “*stj-. 1. Suffixed form *stl-to- in Latin stultus, foolish (< “unmovable, unedu- cated”): STULTIFY. 2. Suffixed zero-grade form “st/-no- in Germanic *stullén- in Old High German stollo, post, support (> German Stolle, Stollen, stollen): sTOLLEN. 3. Suffixed zero-grade form *stal-nd- in Greek stélé, pillar: STELE. IV. Extended form “stelg- in Germanic *stalk- in Norwegian dialectal stalk, stalk, akin to the source of Middle English stalk(e), stalk: sTALK’. V. Ex- tended form *steld- in: a. Germanic *stiltjon- in Low German and Flemish sfilte, stick, akin to the source of Middle English stilte, crutch, stilt: sTILT; b. zero-grade form “*stld- in Germanic *stult-, “walking on stilts,” strutting, in Old French estout, stout: stout. [Pok. 3. stel- 1019.] stele-. To extend. Zero-grade form “*sélo-. 1. Suffixed form *stlo-to- in Latin /atus, broad, wide: LATITUDE; DILATE. 2. Attributed by some to this root (but more likely of obscure origin) is Latin /aémina, place, layer: LAMELLA, OMELET. [Pok. 2. stel- 1018.] sten-. Narrow. Suffixed form *sten-wo- in Greek stenos, narrow: STENO-, STENOSIS. [Pok. 2. sten- 1021.] (s)tene-. To thunder. 1. Zero-grade form *stno- in Ger- manic *thunaraz in: a. Old English thunor (genitive thunres), thunder, Thor: THUNDER; THURSDAY; b. Middle Dutch doner, donder (> Dutch donder), thun- der: BLUNDERBUSS, DUNDERHEAD; C. Old Norse Thorr (older form Thunarr), “thunder,” thunder god: THOR. 2. O-grade form *tona- in Latin tondre, to thunder: TORNADO; ASTONISH, DETONATE, STUN. [Pok. 1. (s)ten- 1021.] ster-'. Stiff. I. O-grade form *stor-. 1. Suffixed form *stor-é- in Germanic *staren in Old English sfarian, to stare: STARE. 2. Suffixed form *stor-g- in: a. Germanic *starkaz in Old English stearc, hard, severe: STARK; b. Germanic denominative *starkjan in Old English *stercan (> Middle English starchen), to stiffen: STARCH. II. Full-grade form *ster-. 1. Germanic *sternjaz in Old English stierne, styrne, firm: STERN}. 2. Suffixed form *ster-ewo- in Greek stereos, solid: STERE, STEREO-; CHOLESTEROL. 3. Lengthened-grade form *s¢ér- in Greek stérizein, to support: STERIGMA. III. Zero-grade form *str-. 1. Extended form *strg- in Germanic *sturkaz in
```


## [2026-10-15T02:45:29.093Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"tanîdan\\|tanidan\\|tanīdan\\|tunuk\\|tunük\\|tundar\\|äbus\\|abistan\\|äbistan\\|ābistan\\|tahamtan\" HRN.txt | head -20; echo ---HUB; grep -n -i \"tanidan\\|tanīdan\\|tunuk\\|tundar\\|äbistan\\|ābistan\\|abistan\\|tahamtan\\|pašōtan\\|pešōtan\" HUB.txt | head"
}
```


### [2026-10-15T02:45:29.398Z] TOOL RESULT

```
3486:tahan, tabistan 'Sommev\ (jNnozxn, Jer. 40, 10; niwNP,
---HUB
1653:396. Zu tundar 'Donner JRAS. 1894, 452 gehort afgh.
6672:selbst', abistan *schwanger ) gefuhlt wurden ; kabutar 'Taube'
8993:SLf*Vi8taxnfa'; tahm — taham *stark* (auch in Tahamtan Von
10230:abistan 5.
```


## [2026-10-15T02:45:31.600Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=109 && NR<=111' HRN.txt | grep -n -i -B2 -A8 \"tan\\b\\|tan \\|tun\\|tund\" | head -120"
}
```


### [2026-10-15T02:45:32.512Z] TOOL RESULT

```
2-387. tes'Axt\
3-ap. vergl. us^tasana- *Bau; aw. tasa- *Axt*; phlv.
4:täsltan, tOsUar bezw. taxs° (vergl. aw. 'tmta-), syr.
5-LW. :it^NlO"nü *Zimmermannsaxt' (de Lagarde, Ges.
6-Abb. 49); ai. [/^taks^.
7-V
8-388. tis *Durst\ tisne {tesne Sahn. I, 59, 481), tisnegl, tesnegi
9-(AM. 40 Zeile 10), INDOnJl^^^D 'Wüste (Is. 13, 21).
10-g. tasne,
11-aw. tarsna- 'Durst*; phlv. tisn , tisnak, tisncfklh;
12-ai. tfsna-; arm. vergl. farsamim welken', anfarsam
--
43-phlv. tag [steht statt tak *stark, Held* (z. B. vd. 3
44-(113) 61.), takik^ taktkth, takikömand (für aw. ta/ma-)]
45:ist im Neupersischen in dieser Bedeutung aufgegeben.
46-Nicht hierher gehört das von Andreas 2tO gelesene
47-tag des PP61. (vergl. Hörn, Mitteilungen, Heft IV,
48-S. 29).
49-392. tem 'Staar (der Augen)' (AM.), ^Oin Finsterniss' (Is.
50-19, 3).
51-aw. temah' *Finsterniss' ; phlv. tum (Phlv.-Vend.),
52-tumtk\ ai. tämas- Tinsterniss*.
53-af/. tör\tam Tinsterniss' (zwei Synonyma componirt).
54-393. ten 'Körper, Leib*, tenömend, vergl. arab. LW.
55-fannaz ^).
56:aw. tanü' *Körper, Leib'; phlv. tan; ai. tanä^,
57:af/. tan; wa/. tan, si/n. tand.
58-Dazu tenha allein', phlv. tamhä (SpiegeTs Lesung
59-tanhäk, vd. 5 (134) 61., ist falsch. Hier wie vd. 6
60-(9) 61. — ZDM6. 43, 43 — ist tuhtk zu lesen).
61-394. tenjlden zusammenziehen ; trinken' (jüd.-pers., z. B.
62-Is. 63, 6), }T:Nj:n.
63-aw. i^danj' ziehen' u. s. w. (6 eidner, Drei Yasht,
64-95). ^ .
65-oss..t. tlinfin, d. iünjun 'ausdehnen' (249); bei. tajenag
66-'spannen, dehnen (375).
67:Der Übergang von der Bedeutung 'ziehen* zu 'trinken
68-findet sich auch bei np. ähenjiden und kestden.
69-Da magidüta kein Abstractum auf üiu («', d) sein kann, muss es für
70-magidäta stehen. Im Neubabyl. wiederholt -ü^w für -äti Endung des
71-Plurals fem. gen. Agidtu *ßinde* bezeugt (von "I^IX)« Davon könnte
72-magidtu eine Form MafUlatu sein. Ev. aber auch magidtu : agidlu
73-= JISi^niD • Ärahsamna, Taka- also höchst wahrscheinlich irgend eine
74-*Binde' als Kopfbedeckung. Nähme man mit Recht an, dass täj =
75-*Krone* elamitischen Ursprungs wäre, ebenso wie taka- in takabarä, so
--
80-'Pelzmütze' gedacht, ß e z o 1 d , Achaemenideninschriften 72, hält übrigens
81-magidüta für den xgwßvXog (Thycyd. I, 6).
82:*) Aus tan + näz^ de Lagarde, Ges. Abh., 51 Note 4.
83-— 89 —
84:395. tund schnell, heftig, stark'.
85-aw. Hvant" (= Hnvant-), [/'tav-, vergl. tuvan (No. 401).
86:396. tunder, tundur ^Donner .
87:Vergl. ai. i/^tan-, tdnyati erschallen, laut tönen,
88-rauschen', tanayitnü- 'donnernd', tanyatii' 'Donner';
89-lat. tonare, tonitnis; ags. pnnjan, punor, nhd. Donner^
90-engl, thufider,
91-397. tenuk *düun, zart, fein'.
92-ai. tanu-, tdnuka- *dünn, fein\
93-kurd. tenik; oss. f(wäg (248); bei. tanak, n. fana/,
94:fanaU (377); sar. tanük,
95-398. teng 'en^Q,
96-aw. tahcista- (Superl. von ta/tna- 'kräftig'); phlv. tanf/
97-eng', tmigih 'Enge'; arm. fanjr 'dicht' (H. No. 110).
98-kurd. tenk *enge; bei. tank, n. tanJc, tahanH (378);
99-af/. tangat/l; wsi/, t^mg, sar. tong,
100-Vergl. auch Bartholomae, Studien II, 44, 51.
101-399. tenlden 'drehen, spinnen', tede 'Spinnengewebe*, tane
102-'Zettel, Aufzug (am Webstuhl)'.
103:aw. [/^tan-; phly, tatak, vd. 7 (36) (für aw. täfdaena-):
104-ai. |/"^aw-, tanoti, 'dehnen, spannen'.
105:400. tHj tu, tö (FirdüsT)^) 'du, vergl. -et 'dein', -tan 'euer'.
106-ap. iuvam 'du'; aw. tum, tväm, tu, tava; päz. tö {tu);
107-ai. tvdm, tdva; arm. du 'du' (H. No. 85).
108-kurd. ttr, af/. ta (obliqu. tä, di); oss. d. du, t. di
109-(112).
110-401. tuvan 'vermögend, mächtig', tuvanä, tuvanisten.
111-aw. i/^taV' 'können, vermögen', tavä[cä; phl. tuvän
112:(geschrieben J^D-n), tuvämk, tuvän(i)stan; ai. l^tav-,
113-tavlti; arm. tevem 'bleiben, dauern, aushalten, Stand
114-halten (H. No. 273).
115-402. töften 'sammeln; ausgeben, zahlen', Praes. töz-em;
116:'k^Tin-TND 'Vergeltung' (Is. 34, 11; 35, 4).
117-*) Die Aussprache tö ist zwar nicht überliefert, sie ist aber wohl
118-bei FirdQsi in den Fällen anzunehmen , wo das WorMhetrisch lang
119-gemessen wird, z. B. Öflhn. I, 189 Vers 1080 und sehr oft. Vergl. dö
120-*zwei'.
```


## [2026-10-15T02:45:37.166Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1648,1660p HUB.txt; sed -n 6668,6674p HUB.txt; sed -n 8990,8996p HUB.txt; echo ---PHD; grep -n \"^tan \\|^tanūk\\|^tanuk\\|^tunuk\\|^tundar\\|^ābus\\|^ābustan\\|^ābistan\\|^tanīdan\\|^tanīdan\\|^pēšōtan\\|^pišyōtan\\|^tahm\\|^tah\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-10-15T02:45:37.578Z] TOOL RESULT

```
394. Ich stelle np. tanjtdan zusammenziehen' zu skr. tafiCf
faflj, pr. tanakti 'zusammenziehen*.
395. Dass tund *schnell, heftig, scharf, spitz' (Fird. Ill,
1703, 3642) (aus *tuvant-?) nahe verwandt mit tuvdn
VermSgend, fahig' sei, glaube ich nicht.
396. Zu tundar 'Donner JRAS. 1894, 452 gehort afgh.
LW. tandar *Donner , echt afgh. ^aw^'Donner (Geiger).
398. Np. tang enge, bedrangt' geh5rt zu tanjldan zusammen-
ziehen', auch angusto et aegro esse animo', skr. tanc
und taiij (Nr. 394) u. s. w. Vgl. tang u bandt obli-
gation' JRAS. 1894, 452. — Dazu auch tang *Sattel-
gurt' (Shah. Ill, 1537, 728 - Noldeke), bal LW.
tang *Sattelgurt' (Dames p. 60) kurd. taiig 'Gurt',
vordere* u. s. w. ; in -tan als 2. Glied von Komp. wie hartan
*hochmiithig, arm. aparfan-er, paz. awartanl 'haughtiness
Min. Gl. 22; firotan (aus firod-fan) 'humilis', paz. ertan- 189 -
*humble* Min. Gl. 72, die noch als Komp. mit tan (vgl. x"^stan
selbst', abistan *schwanger ) gefuhlt wurden ; kabutar 'Taube'
neben kafiar *Taube' (H. 842). Ueber partav *Glanz, Strahl
H. 296 s. oben p. 38. Die Etymologie von kutah kurz' (s.
haufiger wird xm schon zur Sassanidenzeit zu hm und mit Aus-
fall des h zu m: Gustahm = Bistahm, anf Miinzen Vistahm
(ZDMG. 19, 482), arm. Vstam Sebeos 30, 39, arab. Bistam,
SLf*Vi8taxnfa'; tahm — taham *stark* (auch in Tahamtan Von
starkem KSrper, Rus tern's Beiname) zd. taxma-, ap. taxma-
in Taxmaspada- (*mit starkem Heer , ein Meder), arm. tarn in
Tam-Xosrov Stark-Chosrau' = gr. Ta^i/o(jp6fjc, vgl. Tamsapor
---PHD
PHD.txt:148:tahm [thm | =M, N ~] strong, brave. tak [t^k' | N ~ 'vine'] branch. tohm(ag) [twhm(k') | M twhm, -g, N tuxm, -a] ... wanigar [wnykl) prodigal.
PHD_mackenzie.txt:4920:tanuk [tnwk ' I N --] thin, shallow.
PHD_mackenzie.txt:8224:tanuk.                    , ~"to        tuwlinlig
PHD_mackenzie.txt:8352:tah                            NlO       sab                                 Q.)-o'\)
```


## [2026-10-15T02:45:42.305Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^tan \\|^tan\\b\\|^tan(\\|^tanīh\\|ābus\\|^tundar\\|^tondar\\|^tanīdan\\|^tanūr\\|thunder\\|pregnant\\|^Pišyōtan\\|Pišyōtan\\|Pešōtan\" PHD_mackenzie.txt | head -20; echo --NYB; grep -n \"^tan\\b\\|^tan \\|ābus\\|apus\\|^tanūk\\|thunder\\|pēšōtan\\|Pišyōtan\\|pēšak tan\\|pēšōtan\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-10-15T02:45:42.773Z] TOOL RESULT

```
833:Abus, -tan ['pws, -tnl I M 'bwws, v. Abestan] pregnant.
2477:yarranag [gPn)k l I M grn)g ?] thunder.
2478:yarranidan, yarran- [gPn-ytn l I (N yurridan)] roar, thunder.
4905:tan-bahr [tn1b)hl] physique.
4908:tan-drust [tn'drw(y)st 1 N --] healthy, whole.
4918:tan-tOhmag [tn'twhmk ] (sap) of plants.
5401:3wir [wyll N bir] thunderbolt.
5735:zahag6mand [zhk)wmnd] pregnant, gravid.
6698:   maiden.                                    gravid zahagomand; v. pregnant.
7327:pregnant abestan, abus(tan), zahag-            proper, be""" saz-; seem""'" sahistan.
7780:testicle gund.                            thunder (n.) yarranag.
7781:testimony gugiiyih; false ,... ziir-      thunder (v.) yarriinidan.
7782:    gugayih.                              thunderbolt wir.
8302:tan-                                 tasidan
--NYB
604:apustan
611:apustan [’pwstn'] pregnant 222, 1012.15, 16%. — < OP *à-puca-tanu-, SW form of
613:apustan
3711:tan [tn'] body, passim, stalk of a plant 9524; ~ u jan body and vital spirit 1523. 6422 (the constituents of human physical nature); ~ u jan u hir u xvāstak 4%; kanišn 4 jan u višopišn i ~ the destruc- tion of the vital spirit and the decom- position of the body (= the physical death) 64191; ~o as opposed to the immortal soul, ruvān 6625. 6820, 6927, 7615-17-18; — — also refers to the human individual as a whole, with all its physical and spiritual qualities, cf 65? sqq. 6611. 8414. 8671; har —-E rad hamgöhr fravahr et 4 x"eš paitak it is revealed that every human individual has its own fravahr (g. v.) of the same substance as itself 88°; xueš.— and ~ 4, avēš v. aueš; — ~ i pasen the ultimate form of existence the Universe will be given after the now running eycle of millenia has elapsed, the next world, Eternity; very often ristaxéz (q. v.) u ~ + pasen: 12%, 6411-13, 7118-19, 7610, 8326, 8821, 919; ~ 4 pasén alone 5212-13, 66°. 677. 934. 104%. — Av. (633 sqq.) tanū-; common Ir.
3716:tan ... paristém adak-tān dahém ... vas zarr ... 193-4; u api-tin ... kar framā- yēm 198; täi-tän man zīvišn + gētē pat miyān kunom 67-5; agent: ka-tän pursīt hat 214; kū-tān... dit ...? 39%; vinäs t-tān kart éstét 67°; referred to by a follow- ing prep.-adv.: āfrīn-tān + xvatāi apāk the benediction of the Lord (be) with you 1281-19; — independent form atän 451,
3717:tanäpuhrak [tn’pwhlk'] guilty of a tanä- puhr sin, 1.e. of a deadly sin which can only be atoned for by hard flogging or (later) by a very high fine, and which involves the excommunication of the eulprit until he has suffered his punish- ment; applied to Hésm, the demon of Wrath: the originator of deadly sin 61, — Adj. of tanäpuhr, the Milr. adaption of Av. (636 sq.) tanu.parada- ‘whose body is forfeited’, thus an adj. whereas BP tanüpuhr is used as a subst. for the sin itself. f
3725:tanük [tnwk'] scarce, rare 971923, — NP tanuk ‘slender, thin’; Skr tanu-, Lat tenuts.
7249:tan
```


## [2026-10-15T02:45:45.799Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 611,613p NYB_vol2_glossary.txt; sed -n 3711p NYB_vol2_glossary.txt | grep -o \"Av. (633.\\{0,200\\}\"; sed -n 4900,4925p PHD_mackenzie.txt; grep -n \"pēšō\\|pesotan\\|pešotan\\|Pišyōtan\" PHD_mackenzie.txt NYB_vol2_glossary.txt | head"
}
```


### [2026-10-15T02:45:46.593Z] TOOL RESULT

```
apustan [’pwstn'] pregnant 222, 1012.15, 16%. — < OP *à-puca-tanu-, SW form of
www.parsianjoman.org | ool wok
apustan
Av. (633 sqq.) tanū-; common Ir.
 tan [tn' I = M, N .....] body, person.
 tan-, v. tadan .
  • tanapuhl [tn)pwhl = Av. tanu.pmJ8a- I (N tanafur)] a degree of sin.
  e 6684                            G
tan-bahr                                                                taxi
tan-bahr [tn1b)hl] physique.
tand [tnd I = P] faint, languishing.
  --ih: faintness, langour.
tan-drust [tn'drw(y)st 1 N --] healthy, whole.
                                   '
  --ih: health.
tang [tng 1 = M, N --] narrow, tight.
  --ih: narrowness; distress.
tanig [tn'yk l 1 N tani] bodily, corporal.
tanigard(ig) [tnykrt(yk) I 1 M tnygyrd] corporeal.
taniha [tn'yh) I M tnyh), N tanha] alone.
tanOmand [tnPwmnd 1 N --] corporeal.
  --ih: corporeality.
tan-tOhmag [tn'twhmk ] (sap) of plants.
                                     '
tanuk [tnwk ' I N --] thin, shallow.
taniir [tnwll M tnwr, N --] oven.
tar [LCDr l < A l-~d; tll M tr] over, through, across.
 ,ow    kardan, -- menidan: abuse, despise.
-tar [-tll (M -dr), N --] suffix forming comparative adjectives.
tar [t)ll M t)r] darkness.
```


## [2026-10-15T02:45:51.224Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^tadan\\|^ tadan\" PHD_mackenzie.txt; grep -n -i \"pəsō\\|pesö.tanu\\|pdsö\\|peso.tanu\\|pəšō\\|pesotanu\\|ps5.tanu\" BRT.txt | head; grep -n -i \"Körper, Leib\\|Leib, Körper\" BRT.txt | head; grep -n \"^\\*tanH\\|^\\*tan\\b\\|^\\*tan-\\|^\\*tan \" CHEUNG.txt | head"
}
```


### [2026-10-15T02:45:51.667Z] TOOL RESULT

```
4876: tadan, tan- [ttn', tn- I N tan-] spin (thread).
24557:*tané 377 
24582:*tan ‘to extend, stretch’ 
24615:*tanó ‘to twist (together), become narrow, dense, constrict’ 
55658:*tané
```


## [2026-10-15T02:45:53.994Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 24582,24614p CHEUNG.txt | cut -c1-400; grep -n \"tanu-\\|tanü-\\|tanü\\b\" BRT.txt | head -30"
}
```


### [2026-10-15T02:45:54.515Z] TOOL RESULT

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


3658:•  j.  ap«m9n),  g.  ap3ni9m  Adv.:  s.  apma-, ■  j.  a-p9r9tö.tanü-  Adj.  'auf  des  Leib kein  Makel  haftet,  makellosen  Leibes"*: Aagat^rnt  gavam  axsaenanqm  'nunqnt  V. 22.4.
3659:Bed.  Dach  K.  Vgl.  pariiö.tanü:  —  Pü.:  man- ftkr,  erL:  vinäikärik  . .  ?  .  .  lü  mal  esiil,  — ■)  Anders  Gdn.  KZ.  30.  517.
10543:•  j.  puirS  zayante  tanu-kihrpa  kikrpa "xay^us'*  Vyt,  /,
11941:•  j.,  g.  tanü-  f.,  m.'*,  g.  tanuS-'*  n.  Xeib' 1)  der  Menschen  (und  menschenähnlich gedachten  Götter);  auch  sva.  'Person', wobei  die  obliquen  Ka^us  auch  im  Sinn von  ihn'  usw.,  sowie  -  mit  oder  ohne  Ava-, hava-  —  in  reflexiver  Bedeutung^*  im  Sinn von  'sich,  mich'  usw.  gebraucht  werden: ya  anrS  mainyui  frak?rfntat  avi  imqm 'nüm  yam  masyänqm  V.  20.3;  5;  s.  noch lu  aj  —  ks , .  a%r3  tafitus  äärayat  'naot haca  maiyehe  V.  20. 1 ;  —  yasca  .  .  dax- manam  avavantim  mazS  vXkänayat  yaha hl  'nui  anhal  V.  7. 5 1 ;  —  {yai)  *may'iain 'nUm**  aiwyästam  (sd.)  "irlris  .  .  N.  p5; *95^>  —  '*'"'  panna  (sd)  °nBm  aiwi.- si/ais  YX.  14. ^5 i  —  yaf  kl  'nus  hiskvi Aiynvi  (sd.)  pqsnu  bavai  V.5.31;  —  &«.- ayarpm..  'nüm  frasnayayania  Yt/0.  laz; 133;  —  US  'nüm  snayaita  us  *vasirä  V. J.  54;  —  "^ris  frasnaiti  •nunqm  . .  vastra- nam  V. /2.  a;  —  hakmt  aps  hvqm  'nüm pairi yaozdai^ita  V.  (),3i;  31",  ä  36,  37, 39,  Vd./5,  ig*,  20; —  Ja/  vlspam  kvam 'nüm  ayaozdata  k>r>naoiti  V,  ■¥.40;  — yal fU  zasta  nöie  frasnäta  aai  vJspam  hvqm 'nüm  ayaozdata  ik?n>»aoiti  Y.S.40; — yffi Aqm.nasüm  paitiäristfm  °nüm  yaozdai%yqn V.g.i;  —  iia  iristahe  'nüm  avaMsta  .. isaaa  (sd.)  ml  yaoldaitim  V,  Ä  100;   —
11942:tanu-  I  634
11975:'tanu-mazah-  n.  'Grösse  des  Leibes':
12500:namca  'nanam  adaivayasnanqmca  tanu.- p3r3%anani  atanu-pinhanatiua  V.iS.öz*^.
13075:—  yS  anyehe  'mähe  bansma  ^/rashrMti (sd.)/ra/asaitiN.io4; — "" apanS,t)m»m  'rtiftn N.  r2;  —  saota  asava  .  .  "mö  tanu-tnair!) Yt  /O-  137  (vgl.  I  j8);  —  'mB  ahmi  äfrl.- :-aca  Az.  / ;  *Vyt  / ;  —  °mS  niurusds  ümityü.- draonh  N.  77;  —  jaki  ..yö  xsitdrä  hqm.- raliwayeiti  'iiianqm  adakmanqmca  V.  18. 62.         a)   bes.    im   Gegensatz   zu  tanu.-
15226:'cäca  vTsatii'a  "25"  V.  12.  9;  —  °^aca (akwar»sal>mfa  "45"  A.  _^.  7;  —  °^3ca ÄaptaitTm"T%"  A..3.1),  u.  a)  substanL mit   Gen.-'';    °ta    dahmanqm    dasa  tanu-
16186:•  J->  %■  'piiSö.tanü-  Adj,  'des  Leib  ver- wirkt,   dem    Gericht    verfallen    ist':     töi
22042:—  yäha  drvä  gaom  *visie  (3SPM.)*'  .  . *viile'  Aog.  S2;  F.  Ä*>;  —  vispä  ta  p?nsqs ya'ha  diät  haSi  gam  vtdat  västryS  "nach all  dem  frag  idi,  ob  durch  A!a  der  Kuh teilhaftig  werden  wird  der  Bauer  . ,"  V. 5'-  S*''j  —  ""^  ^^  ""^  ät^ham  zadhranam (Gen,  ab  Obj.)  vindita  '(3SOM.)»  Yt ^7-  S4i  —  '^it  *^  ^^  asraoyanam  tanu- nqm  alahe  (Gen.  als  Obj.)  .  ,  *vthaiti^'> P.  75;  —  yim  dim  va^tät  *tvistaiha  (sd) *vindän?m  ndit  *'ava  yä  *vistas!va  (sva. 'gegen  Entgelt")  N.  t6;  —  s.  noch  i'ldat.', vKat."  a)  mit  Gen.  (statt  Abi.)  der Person  'von  .  .' :  asanS  sasta  draiimnS  .  . vindimnS  dahufs  akuräi  mazdäi  „Steine .  .  von  dem  Schöpfer  AhM.  (sie)  be- kommend" V./5.4.  3)  'Jemandem  (Dat) etwas  erwirken,  verschaffen,  verleihen':  at.. taibyB  xidhnm  vohB  mananha  (als  Subj.) *»S(i'riÄJjÄ(3SKA.)9'  a^byö  jaj«(sd.)  yBi . . Y.J0.8;  —  s.  noch  vindat.-.  4)  'fertig, zu  Stand  bringen,  bereiten':  aAyä  vohs aosO  vida  (sS.)  mananhä  "ihm  bereite, o  VM.,  den  Untergang"  Y.4g.  i;  —  kva ht  aols  vindäma  V.  ig.  46.
24015:•  j.  vi'turatö.tanü-  Adj.  'wobei  der  Leib, die  Person  (an  einen  besonderen  Ort) weggebracht,  isolirt  werden  muss':  patss (sd.)^J  •«w/V.2.29;  Yt.5.9z.
24497:•  j.  vispo.tanü-  Adj.  'auf  den  ganzen Leib  sich  erstreckend':  aojs  °näM  *>  (ASn.)
25488:•  j.  irista-tanü-  f.  'Leib  des  Gestorbenen, Leichnam':  paslaili  avi  ht  °nüm  tipa daxma  frabaröil  Vd.  12.  Wertlos.
25623:Menschen;  a)  im  gAvr.:  spiniahyacä n?ni  . .  yehyä  'vä  afö  kahitl  (sd.)  Y. 34.2; — yi  'vqn>m'^  »iÄ(^fl»>?(Sp.5i4m.) voAs  dadi  Aa%ra  (sd.)  manaiaha  V.  28.  4; —  iat  möi  °va  isl  (Sp.  26  o.)  caAyl avanh^  Y.50. 1 ;  —  aläunqm  Ja/  'unsyasa- maide  kudsaUaniim^t  narqm/ä  ttsirinqmeä Y.jp.  z;,;^.  i(s.bei3).  B)imjAw.:«ÄV cahmi  »awa  (sd.)  yS  rfit  °une  tatva  FrD.j; *j'';  —  ävsya  ^druzantt  .  .yS  fraurvatxH (Sp.  996  u.)  kavahe  'um  druiaite  N.  Ärf; *84^'i  —  SvBya  . .  dahäiti  .  .yaihe  d/l%rahe daiti  *ndit  *AavS  'va  ^vauräta  (Sp.  1544 u.)  N.*,^;  F.p; —  vJspfm  amm paiH sruä- mm  astanm  °va  käSayat  (sd.)  P.  J7;  — hazaiarim  .  .  datnunqm  .  .  asaya  vankuya 'uru  paraJaihyV  Ä.J.J;  V.  r^.  3;  —  /ä nS  A>nti  'une  »valm  sfari^itnca  vastnm^a Y.  55.  3;  2,  Vyt.  J2;  —  AaemS  . .  ydha kannte  vakütö  'unalia  pii%mainys.hmlf Y.g.  16;  —  havahe  °unö  haomq  ävaeaa- yamahl  Vr.  ri.  1 ;  —  xsnamaine  havakeca \°unS  Y.J. 4;  —  %at3  (sd.)  buye  vatshäu^a \miide  ..  'unai'a  darr/e  havanhe  A. 7. 11; iY.7j.11; — fravaHbyS  yä  nS  isla  'vSibyS Y.  55.  a;  —  yU  yazaite  hvan  . ,  yazaite 1  haom  °vämm  Yt.  6.  4;  —  kake  VB  'va  frä- ,yetyat  YL  /j.  50;  —  nava.»apiyai(sd.)^ij  hl I  'vätam para.itar9ncaiU  V.  13.%.  a) neben oder  im  Gegensatz  zu  tanü-  und  zu  anderen .menschlichen  Kräften  usw.:  tanval?a  *hao- sravankitn  'unalca  darrfim  havanA>m F.jh;  —  cim  .  .  qstjm  isatti  tanva  Hm °una  Aog.4S{?);  —  havaj)häi  °une  frada- 5j«  galhanqm  Y.6S.4;  —  amaheca  vin- %ra-fnahtca  'unala  damaca  spanvanti  (sd.) H.I.4; — (ha  alaonqm  a^aoninqtnca  ahümca damqmca  iaotasca  °vän?m'a  frai-ailmca yatamaidt  Y-sd.  4;  —  vUpa  gafisisca tanvasla  azdihxi^a  ustänqsia  kikrpas^a t/vlMca  baooasia  'vansmia  fravaiimh pairica  dad>mahJ. .  Y.55.  i ;  —  aläunqmca 'unasca  /ravasisca  yazamaide^.']0,Y.63.%; — aläunamia  fravaHbyS  ailwiqmi'a  'vöibyS Y.4.2;  —  vlspanqmia  ankam  O'aonqm alaoninqmla  .  .  yat/qm  *yasii%waca  'vqnö taoySsla  /ravai'ayS  Yty.  148;  ~  Aaom 'vänim  .  .  kavqm  fravalsm  yazamaide  V. 7/.  i8j  —  havahe  °und  fravalse  Y, /. 1 8.  3)  von  der  Seele  nach  dem  Tode  des Menschen;  a)  imgAw.:  kä  me  *vä  vshu *urvaxidt  *Sg?maUJ  (Sp.  497  m.)  Y.  44. 8 ;  —  a>mr>tnitT  *a!aon5  'va  alsS  (sd.)  Uta-
27227:•  j.  srao-tanü-  Adj.  (nur  fem.)  'tüchtigen Leibes':  katnlnS  k?hrpa  ..  'nv5  (GS.)  H. 2.9;  —  aäam  kaininS  arahmie  ..  'nv3 (NP.)  Yt. /7.'ii;  —  fravaSayü  .  .  yh  .. 'm'if  itiP.)  YL/J.40.
27255:—  mi^rB ..'iasca  afys sBrS  nairyü.satakasla Yt./0.52;  j^.  85,  Vyt^lO;  —  daütam  hl\ (nämL  mi^rahe)  upa  ar^»m  vazaite  ys\ vanhus  *sS  afys  vairyaMSnm  .  .  rasnus  1 Yt  10.  100;  41;  —  imal  vS . .  jaioyemi mi^ra  .  .  '/a  asya  .  .  rainvS  Y.  6^5.  1 70.3;  —  '^ahe  asyeke  asBiSca  vankuyä naitythela  satikake  Vr.  u.  16;  7.1;  — brUta  U  (näml,  aSsif)  y5  vaahui  °ls  asyS Yt.  //.  16;  —  'sähe  asyehe  taxmahe  tanu- mq%rahe  darH.draoi  ähüiryehe  aoxtö,- nämanU yazatoAe  Y.  3.  so;  4.23,  Y.iS.  14;
```


## [2026-10-15T02:45:58.666Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 16180,16190p BRT.txt | cut -c1-500; grep -n -i \"sohnlos\\|kinderlos\" BRT.txt | head -5; grep -n \"taxma-  Adj\\|ta%ma-\\|taxma- \\\"\\|'tapfer\" BRT.txt | head -5"
}
```


### [2026-10-15T02:45:59.163Z] TOOL RESULT

```
(nur  Komp.).  >
KorapA.    —    Zum   V.  \pai-,  %  272.   —   Vgl.
p>titav  und  Osthoff  IF.  *.  33.  —  Pü.;  puhl.
•  j.  p3§5-cingha-  Adj.  'mit  weit  auseinander- gezogenen, gespreizten  Klauen'  ",von  einem Daivayasntt:   'ksm  .  .  humayahm  (sd.)
Yt5-ii3.
Aus  ir.  ^lattga-  m.,  mit  i  nach  S  25A  4  und mit  agh  statt  b^,  vgl.  lu  *haifha:  —  np.  iang. —  I)  Zum  Angriff  oder  lur  Abwehr.
•  J->  %■  'piiSö.tanü-  Adj,  'des  Leib  ver- wirkt,   dem    Gericht    verfallen    ist':     töi
nar>fils  *anj[i  aeSasü  (sd.)  dijU.antä  'nvö (NP.)  Y.5_J.9.  A.)]\vi.sva..ianu.f?r^%a- (sd.)*':  -nustanUm  *piryeteF.2jh;  lO;  — aäahe  paiti  'nuye  duye  satte  upäzananqm (sd.)  upäzSil  aspake  aStraya  .  .  V.4.io; —  aMÄaJ  hala  * fyaohnäv3r>za  (sd,)  aia ; bavainti  'nvS  (NP.)  V,  13.  38,  15.  i  (wo  j 'irva) ;  —  yS  gidä  asrävayS  .  .  tat  /"'''  j *ainim  dahnam  gäiianqm  *srao%rät  pai-  \ ristayeiti  .  .  *°nu/  N.  44;  —  vTspS  arikui' astvä  .  .  xraodat-urv
")  Die  .Sünden,  durch  die  man  p'  wird,  sind
genannt;  V.  ^.  20  f.,  24  f.,  28  f.,  3i  f.,  35  f.,  38[.,
41  f.,  5-  43.  *■  4.  8,  18,  47.  /■  71.  /5-  24,  37, 1
3723:.  y  aipi-paramna-  Ad,.,  PPM.;  s.  l^i^.    ,  ^^^^.  „^j^^  p^^,_  ^jj^  j^g^  kinderlos  ist"
3725::  ^^  °?,'f 'iT^  /  t  °\  -^lü^'l"  .''  '/ramraomi)ya>,a  'nli  "einem  mit  Kindern keine  M,lch  m  der  Brust  hai^  nicht  säugf:  (^  ^^^^  ich  einen  höheren  Wert  zu)  als nätnkqm  ■  ■  ^0^^m  vlH^d.)  '/p'Bs'fmj'n  <  ^^^^  kinderlosen"  V.4-47;  -  yat  M V.i5.$;  —  hSinsinqm  ..  'pyBstnqm  Vyt  „^^^  ,„^/^  ,^^,-  ^„^^,  «„e„„  ^er  Mann 5*';         _..,,,..,,.  I  bei  seinem  Tod  kinderlos  ist"  Vd,  21;  —
3729:,.  at^mi,  VI.  10.  a?^   i^yh  1  ^.^^  kinderlos  ist,  unfruchtbar':  faoiryam
4060:•  j.  a-frazantay-   Adj.  'kinderlos':    uia
11841:*  j-i  g-  (.  P-)  taxma-  Adj.  (fem.  °mä-) 'fortis,  tapfer,  tüchtig,  energisch,  helden- haft'; a)  von  a)  Menschen  und  ß)  Göttern: a)  masyänqm  .  .  'manqm  V.  20.  i ;  —  nä •Mö  Yt  jj.  67,  Aog.Ä^;  Vyt.  2j;  —  narU 'ma  (NPm.)  Yty.  27;  5.86,  iS-Hn^^h
```


## [2026-10-15T02:46:03.490Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=16100 && NR<=16200 && /^ *[0-9]{3,4} *$/' BRT.txt; awk 'NR>=11900 && NR<=11950 && /[0-9]{3}/' BRT.txt | grep -o \"tanu-  I  634\"; awk 'NR>=11830 && NR<=11845' BRT.txt | grep -o \"^[^a-z]*[0-9]\\{3\\}[^a-z]*$\""
}
```


### [2026-10-15T02:46:04.073Z] TOOL RESULT

```
897
tanu-  I  634
```


## [2026-10-15T02:46:09.965Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"تندر\" \"تنک\" \"تنیدن\" \"پشوتن\" \"تهمتن\" \"آبستن\"; do echo \"== $w\"; awk -v w=\"$w\" 'BEGIN{RS=\"\\f\"} index($0,w){print NR-1}' BQT_v1_pages.txt | tr '\\n' ' '; echo; done"
}
```


### [2026-10-15T02:46:11.161Z] TOOL RESULT

```
== تندر
81 427 465 473 722 742 745 
== تنک
31 127 132 169 198 256 278 299 399 414 512 542 671 723 750 
== تنیدن
751 752 
== پشوتن
145 
== تهمتن
766 
== آبستن
216 233 251 355 371 422 685
```


## [2026-10-15T02:46:14.454Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR-1==745' BQT_v1_pages.txt | grep -n -A3 \"تندر\\|tundar\\|tondar\\|tanyatu\\|Donner\" | head -40"
}
```


### [2026-10-15T02:46:14.942Z] TOOL RESULT

```
42:نه چرخ است واجزای ار چون ستاره نه ابر است وآوای آن حمجو تندر.
43-«فرخی سیسالی۵ه .۶
44-۴۳ رك: تور . 0 از فن - دس (مخنف دس). رلك: تندس .
45-۵ ند ر ست -بفتح اول وضم‌سوم‌وچهارم‌از:نن ۳ درست («.م). کیلکیو نطنزی)10400۲05:
--
48:لندر ستی -بفتح اول وض‌سوموچپارم.از: تندرست(ه.م) - ی(مصدری) رجوع به‌درستی‌شود ؛
49-پهلوی )۲105 0210-41«ار نوالا ۶ سلاهت: #رسو لگفت علیه‌السللام: این‌طایفه را (مسلمانان را
50-طریفی حست که نااشتها غالب شود خورند ونوزاشتهابافی باشد که دست‌ازطمام بدارند. حکیم گفت:
51:این است موحب تندرستی.٩‏ «کلتان ۷ و۸ -لیز نندرسی اسمی است که به‌بسنا *داده شده
52-#ستا۱ ص۳۲۷ >.
```


## [2026-10-15T02:46:17.253Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 744 745; do awk -v L=$L 'BEGIN{RS=\"\\f\"} NR-1==L' BQT_v1_pages.txt | head -40; echo =========; done"
}
```


### [2026-10-15T02:46:17.727Z] TOOL RESULT

```
Exit code 1
تنیلیت۱ عبا تای فرشت درآخر بر وزن
عندلیب , بارکوچکی را گویند که بربار بز رکه
بندند و گاه بربالای چاروا نهند و بر بالای آن
موار شوند - ویك لنکه بار را نیز کنته‌اند.
لثبوو » بر وزن زنبور ۰ سازست
مشهور , و ععرب‌ان طنبور ۴
تنبو لك بر وزنمقلو 2
بععث ی کیاده باشد ء و آن کمالی
است‌بسیار کم زور و بمعنی
جناغ زین هم آمده است که
دامنزین وتسمهرکاب باشد ؟-
و طاق زین را یز کوبند ۴ .
تتبول «بروزن مقبول
برگی باشد که دره‌ندوستان‌پان
کویند وبا هك وفوفل خور ند
و کیاده را ی زگوند . و آن
کمالی باشد کم زور 6 وفام
قلمه‌است درهندومتان . تنبور (طنبور)
آنیه س بر وزن انبه » چوبی کنده
وبزر گه باشپ که در پس در نهند تا در کشوده
نگردد .
لنسدن بروزن‌خندیدن» بمعنی‌لرژیدن
ات
و طییدن و حر کت کردن باشد - و بمعنی کمین
کردن هم حست .
تنبياگ سب بشم اول وسکون ثانی‌وکاف ؛
بىمنی تتبك است و آن دهلی باشد دم دار که
مسر ؟ان‌وبازمگران درزیر بغل گیرند ولواز نش
وجناغ زین اسبرا نیز گوبند٩‏ * و با بای‌فلرسی
مده است .
ناگ ه با نای فرشت بر وزن غناقد .
نم پادشاهی بوده است - و نام مردی هم‌هست.
تنته ۷ < بفتح اول و فوقانی و سکون
تالی» تنیده و پرد؛ عنکبوت راگونتد وضم‌اول
و فتح ثالث زلبورسرخ باشد .
قنج۸ ه بفتم اول بر وزن رنج » سنعنی
درهم پیچیدن و فراهم فشردن باشد - و بمعنی
از پی درآمدن و فراهم نشاندن هم هست. و هر
فاعل را نیز گویند که بحسنده و فشارنده واز ی
درآ ینده باشد - و امر ببایئمعنی هم هست یمنی
(eval):1: ======== not found
```


## [2026-10-15T02:46:22.998Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 743 744 745 746 747 748 749 750 751 752; do echo \"#### leaf $L\"; awk -v L=$L 'BEGIN{RS=\"\\f\"} NR-1==L' BQT_v1_pages.txt | grep -n \"^ *تن\\|^ *ثن\\|^ *لن\\|tan\\|tun\\|Av\\.\\|اوستا\\|پهلوی\\|سنس\" | head -25; done 2>&1 | cut -c1-200"
}
```


### [2026-10-15T02:46:23.990Z] TOOL RESULT

```
#### leaf 743
14:لنیسه ‏ بر وزن مدرسه؛ قالی را گویند
17:تنبك بشم اول بر وزن اردك باانگشت
33:تنساث. ۶ درگیلکی وفربزندی و برنی ونطنزی ۱81081 کد. ۱ص ۰۲۲۹6 سنگسری
#### leaf 744
1:تنیلیت۱ عبا تای فرشت درآخر بر وزن
7:تنبو لك بر وزنمقلو 2
22:لنسدن بروزن‌خندیدن» بمعنی‌لرژیدن
26:تنبياگ سب بشم اول وسکون ثانی‌وکاف ؛
33:تنته ۷ < بفتح اول و فوقانی و سکون
42:تنج بمعنی از پی در آمده وترئج بممئی فشارنده
46:لنحید ه* احه بر وزن سنجیده » بمعنی
52:۵ رگ : تسین . ۹ - تنجیدن بمعنی کشیدن و بسن و آشامیدن , اوستا
#### leaf 745
8:تنل بار آه تند معلوم بابای ابجد بالف
17:تنلیر 5 عه بضم اول وفتح ثالك وسکون
18:۱ -اوستا ۷2۵۸ ه (ه . 2)۷29۵6) ,از ربشة 4۵۷, فس: توان (تواستن) «اسفة
31:لنفد و - بروزن تندخوه بخیل ومسك
38:لندسه » بنتع تالث بر وزن مدرسه ه
48:لندر ستی -بفتح اول وض‌سوموچپارم.از: تندرست(ه.م) - ی(مصدری) رجوع به‌درستی‌شود ؛
49:پهلوی )۲105 0210-41«ار نوالا ۶ سلاهت: #رسو لگفت علیه‌السللام: این‌طایفه را (مسلمانان را
#### leaf 746
3:تند و خند» ح اول وخای قطددار »
7:تندور بنم‌اول وثالث بروزن پرزور *
16:تند ید۴ س سم اول بروزن جتبید »
26:لندیسی * » بر وزن تسدیس » بمعلی
27:تن مانند است چه دیس بمعنی مالند باشد -
35:تندس است که تمثال و صورت - و مالئد
51:تنستخج(4) بنم سین بر وزن عه رخ ۰
#### leaf 747
17:تنقظاد -_بنم اول وفاف و طای‌حلی
25:۱ - اوستاه)نأکفی(20)8) (سفت عالی‌از 140۳08 بمعنی‌نمم وببر ومند)» پپلوی 808
42:تنكك دل چو باران بمنزل رسید نضبد که واماند کان از ند .
#### leaf 748
6:تنگا » بااف بر وزن اغیار. داروبی
15:تنگ پاز » بر وذن زنگبار » نامی
46:تنگه ر کان - نام مونمی است از
48:تنگ چشم - کنابه از مردم بخیل
52:تنگ دست » با دال ابجد بو رزن
#### leaf 749
4:تنگ دوی» نم ثانی » کنابه از شهرت . دی
13:تنگ‌سار ؟ » بر وزت منگه مار »
36:بونالی بوده که ظاهراً درعهد انوشروان ازبونانی بهپلوی و کمی بمد از پهلوی بزبان آرامی ترجمه
38:کتاب که ظاحراً درفرن دوم‌هجری اززبان پهلوی حربی ترجمه‌شده» دربن منجمان اسلام محروف
#### leaf 750
9:نیمهٌدوم قرن‌اول مسیسی کتاب خود را یونانی نوشته, و بعدها بپهلوی ترجمه شده بوده وحتی در
10:کناب «بزبدح»(ویز ید که) پهلوی (رش: شماری م۱۹ ۳۱۷) آزآن کتاب منقولافی بوده است.
11:درموفع ترجمهٌ کتاب نو کروی‌ازپهلوی بعربی که‌به « کتاب‌الوجوه والحدود» معررف‌شده»
12:بملت اغتشاش خطپهلوی که ذابل همه کونه صحیف است.اسم ملف که دریپلوی مي,و(یم
22:کهسنسوب‌به «تنطوشا» وترجمهٌ اين وحشیه است واکنون بعض نسخه‌های نادر ازآن موجود است
27:کتاب اسلی -یعنی ترجمةٌ عربیاز پهلوی.- خبری نیست و ظاهراً ازمیان رفته است. «گلمشمساری
#### leaf 751
1:تنگنای۱ - تنگی - و جای تنگه .
7:تنگه » بفتم اول و ثالث و سکون
10:تنگه بقراه کنابه از بر کهفراست
11:تنگ یاب ب با بای حطی بر وزن
16:تنندوه - بر ورن -دن بوه بمعلی‌تنند
#### leaf 752
9:وكوي که در پهلویآسیا سازند تا آب ازسوراخ
15:تنومند ۴ ۳ بفتح اول ومیم و سکون
36:تنیدن* بر وزن رمیدن » معررف
40:٩‏ -ازاوستا -5480 ؛بهلوی
47:عری «نور» (بتشد ید دوم) فد فرردکل گوید لفت آرامی خورازمنعاً ابراتی‌است. دراوستا کلمةٌ
```


## [2026-10-15T02:46:27.434Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR-1==746' BQT_v1_pages.txt | sed -n 1,20p; echo; awk 'BEGIN{RS=\"\\f\"} NR-1==746' BQT_v1_pages.txt | grep -n \"^ *[۰-۹]* *-\" | head; echo; awk 'BEGIN{RS=\"\\f\"} NR-1==752' BQT_v1_pages.txt | sed -n 30,50p; awk 'BEGIN{RS=\"\\f\"} NR-1==747' BQT_v1_pages.txt | sed -n 1,30p"
}
```


### [2026-10-15T02:46:28.150Z] TOOL RESULT

```
نی ۱ مس بر وزن بدرو . کبوت را
گویند.
تند و خند» ح اول وخای قطددار »
اين لفت ازانباع است بمعنی (۱) تار و ما رکه
زیروزیر شده(۲) واز هم پاشیده باشد » و باین
ححشفی بفتح اول وخای نقطمدار هم آمده است .
تندور بنم‌اول وثالث بروزن پرزور *
بمعنی رعد باشد » و بختح ثالث هم باین حعنی
آمده است ۴ -وبللرانر گویند کهءرب‌عندلیب
خوانند ؟ .
نف « بنم اوذیر وزن عمده , چیزی
باشد که مانند غنجه مرتبهٌ اول از درخت‌سرزند
وبمد ازآن ب رکه از مبان‌آن‌بر آبد۴ -و زبود
سرخ رالیز کوبند , و بمعنی اول بجای‌دال ایجد
زای حوزعم آمده‌است ۰
تند ید۴ س سم اول بروزن جتبید »
ماضی تندشدن ودرخشم‌رفتن باشدیمنی تند گردید
ودر خشم شد وغنچهوب رکه وشکوفه برآوردن
درخت را نیز کوبند " چه ه رگامدرخت شروع
در ب رک وشخوفه برآوردن کند کویند «نندید»


نا - معروف است که از مفرد بودن
باشد - و بمعنی اجسام نیز آعده است ۷ چه‌نن
بدهنی جیم‌است .
آفی۷ » بر وزن غنی » بمعنی‌جمالی
فئیان» - نتم اول و کر تالی
و تحتانی بالف کشیده و بنون زده » بمعنی
تنیدن* بر وزن رمیدن » معررف
۴ از : تن ۳ اومند (یود
۵ از: تن (تندن)
۷ -بپلوی
٩‏ -ازاوستا -5480 ؛بهلوی
«اسشق ۰۳۹۹ .
قه ازصفحهٌ ۰۲۳
ففه‌اللغه (۳۱۷) آنر! در زمر کلمات مشتراه فارسی و عربی آرد . درزبان | کدی 100111 آعده
(۰ 32 ,۳۲۵۵۵۵ ,۸۲2, 2۸1۳0026۳8) چون رش لغت‌مززبور درهيحجيك اززبانهای سامی
اصالی تیست. ممکن‌است متوجه فرطية لفوبان مسلمان راجم بابرانی بودن اسل لفت‌شد. فرانکل
[26۵ برآست که لفت عربی « تنور » ازآرامی بعاربت گرفته شده. در آرامی «تنورا» ودر
عری «نور» (بتشد ید دوم) فد فرردکل گوید لفت آرامی خورازمنعاً ابراتی‌است. دراوستا کلمةٌ
8 آمده ( رك : وندیداد , 1 ,۲۵4 ) , ودریهلوی صورت 2100 بمعنی احاق طت
(65),)21065311,121 ۷۷ ). با این حال لغتمز بورینظیمی رسد نه‌ابرانی‌باشدونه‌سامی؛ولیابران‌شناسان
آنرااز مأخشسامی دانستهاند. آنجه‌قویب بحتیفت بنظرمیرسد آنت که کلمة مزبور مثعلق است به
و کنابه . از دهان خویان هم هست - و بمعنی
فروبردن و نایدید کردن همآمده است - و هر
صضحه با نشته ای باشد که نفاشان ومسوران‌اظپار
صثمت خود ی آن‌کنند عموماً - و نگار ایا
مانیرا وین خصوصاً وباین ممنی با ثای مثأثه
هم آمده‌است؟ وتوار ی که برژین اسب مضوط
کننه - ودوالی که بدان‌بار بر پشت باربردار(۱)
محکم سازند - ودره اکویراهم گفته‌اند۴ - ونایاب
وعدیمالمشال را نیز کویند - و بمسنی‌ملول‌وستوه
وآزرده هم آمده است - و ام ولایتی اسث از
بدخشان - و تلم مقامی باشد از تر کستان که
ترکان‌ننگی با ن‌منسوب بخوش‌صورتی‌مشهوراند9 -
لی‌شوی » نم شین شقطه دار بروزن
بدخوی, حوض وجوي آب و چشمه و امتالآبرا
کونند عموماً - و تخته ای که میت را بر بالای
آن شود خصوصا .
تنقظاد -_بنم اول وفاف و طای‌حلی
بالف کشیده بر وزن پرخمار » پاسبان‌را گویند -
وشمم باريك بلئدی را نیز کفته‌اند که ازسرشب
تا صباح بسوزد , وبر وزن توالفقار و بردبار حم
گفتهاید .#9
قنگه س بفتح اوز وسکون ثانی وکاف
فارسی : ممروف است که هی فراخ باشدا -
وبك انگه بار و خروار شکر را یز کویند؟ -
۱ - اوستاه)نأکفی(20)8) (سفت عالی‌از 140۳08 بمعنی‌نمم وببر ومند)» پپلوی 808
(ضیق) , ارمنی 12017 ( سفت» ححکم ) , کردی 668 ,بلوچی ۱27 اففاني اقهتها .
وخی ۷28 .سریکلی 008) « اسشق ۳۹۸ * «صینا .4۲:۱4٩‏ بمنی آنرا ازرشة تنجیدن(«.م)ه
ازساس کرت 4206 و420 داسته‌اندرننگ بمعنی دوال زین مر کوب (در بلوچی 00۰808ه,
کردی 208 ,061208 (مبان کمربند وتنگ)؛ استی 8750088 (شک‌بند) .افنانی 18-۵08
( ننک زین ) و 1808 (ننکه زین) <هوبشمان ۳۹۸*.
```


## [2026-10-15T02:46:34.050Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 746 747; do awk -v L=$L 'BEGIN{RS=\"\\f\"} NR-1==L' BQT_v1_pages.txt | grep -n -A4 \"^ *تنك\\|^ *تنکه\\|^ *تنكه\\|^ *تنک\\|تنو\\b\" ; done | head -40; awk 'BEGIN{RS=\"\\f\"} NR-1==745' BQT_v1_pages.txt | sed -n 14,22p"
}
```


## [2026-10-15T02:46:35.526Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 746 747; do awk -v L=$L 'BEGIN{RS=\"\\f\"} NR-1==L' BQT_v1_pages.txt | grep -n \"تنك\\|تنک\" ; done | head; grep -n \"tanuka\\|tanuk\\|تنکه\\|تنك\" ../../sources/web/*502* 2>/dev/null | head -2"
}
```


### [2026-10-15T02:46:36.303Z] TOOL RESULT

```
42:تنكك دل چو باران بمنزل رسید نضبد که واماند کان از ند .
43-«بوستان‌سمدی. چاپ‌فر وغیص۳۸*.
44-کوبا مرادش رقیق القلب وحساس باشد. « از بادداشتهای علامه قزوننی» - نیز بمعنی کم
45-واندك -در دزفولی0001) بمعتی‌رفیق وآبکی و کم‌آهدد. درچپارمقال(ص۳۲-۳۱) آمده: «لزآن
46-( انگورهرات ) دونوع‌است: ... دومکلنجری‌تناه پوست‌خردنکس بسیارآب. * بمنی پوست‌ناز که.
واو مجهول و رای فرشت » جستن و برجتن رآ
گونند» و باین معنی بجای بای ابجد بای حطی
اههد سح
تنلیر 5 عه بضم اول وفتح ثالك وسکون
۱ -اوستا ۷2۵۸ ه (ه . 2)۷29۵6) ,از ربشة 4۵۷, فس: توان (تواستن) «اسفة
۵ هرب انرابطةٌ *نند»رابا «نوان» ممتقدنیست «هوبشمان ۳۹۵ اورامانی00) «ل . اورامان
۷ سننانی 00 ۰ منکری و سرخه و لاسکردی 10۳0 , شهمیرزادی لا « ۵ . ۲
ص۱۹۹ .گیلکی ۱94 . ۴ فرهنگ دساتیر ۷4۰ .
۴ - قس: ریش هشدی‌باستان 20], 180201 ( صدا پیجیدن , صدا: صدادادن ).
```


### [2026-10-15T02:46:36.583Z] TOOL RESULT

```
39:طبری ۹۵8 (روان. ضدغلیظ) «واژه‌نامه 6۷۳۳؛ بارىك» رقیق؛ نازك. لطیف. دان‌تنكث» درعرمی
42:تنكك دل چو باران بمنزل رسید نضبد که واماند کان از ند .
```


## [2026-10-15T02:46:38.685Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR-1==747' BQT_v1_pages.txt | sed -n 31,41p"
}
```


### [2026-10-15T02:46:39.284Z] TOOL RESULT

```
۴ در این بلاد فزون دارد از هزار کلات بهريك ادر دبنار تنگها برتشگه .
فرخی سیستالی . *لغت‌فری ۶۲۷۹ .
۴ ر4: ارتنگه : ۱
۴ -دشت چوندیبای سوزن کرد وآحو جوق‌جوق استاده آمده بیرون صحراها زشکه .
منجيك ترمذی. هلت فرس ۲۷۹+
9 رکفث: تنگه ت رکان.
۵ قك -بشم اول ودوم» حندی باستانی ها , - هتلاحشا (نلزك , لطیف) « کردی
عطاهعا . استی اقا . بلوچی عطقعها , <هتقا . سربکلی لاله « اسشق ۳۹۷ > .
طبری ۹۵8 (روان. ضدغلیظ) «واژه‌نامه 6۷۳۳؛ بارىك» رقیق؛ نازك. لطیف. دان‌تنكث» درعرمی
رفاق. سلائق «السامی» «منتهی‌الارب» وان توع‌نانرا اکنون درایران «نان لواش» گویند ودر بهار
عجم «لواشی» و«لباش» (کلحة اخبر بنفل‌از جهادگیری) نیز نوشته (در:لواش):
```


## [2026-10-15T02:46:46.916Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"پشو\" \"پشوت\" \"بشوتن\" \"آبست\"; do echo \"== $w\"; awk -v w=\"$w\" 'BEGIN{RS=\"\\f\"} index($0,w){print NR-1}' BQT_v1_pages.txt | tr '\\n' ' '; echo; done; awk 'BEGIN{RS=\"\\f\"} NR-1==752' BQT_v1_pages.txt | sed -n 18,36p"
}
```


### [2026-10-15T02:46:47.942Z] TOOL RESULT

```
== پشو
145 255 331 598 611 637 
== پشوت
145 
== بشوتن

== آبست
216 233 251 355 371 422 685 
انصاف ومالکیت),
-ه (یوند مدید آ ور ند اسماز ضل) .
اقا »از: بن ۳-ی (سبت).
اي ده
نون و دال ابجد (۱) +توانا و تدرست - وبلند
بالا - و عریض 7 وصلحب فوت - و فربه را
ات وشاد وخرم دارند تن را نیز کفته‌اند
که نن پرور باشد .
قنه ۴ « بنتح اول و الی» توت کیب
و جثه را کوند - و ننیده عنکبوت دا نیز
گفته اند 9 - و بعسی قبول و رشا هم هست
چه ننه شدن فبول کردن وراضی شدن باشد.
نا - معروف است که از مفرد بودن
باشد - و بمعنی اجسام نیز آعده است ۷ چه‌نن
بدهنی جیم‌است .
آفی۷ » بر وزن غنی » بمعنی‌جمالی
فئیان» - نتم اول و کر تالی
و تحتانی بالف کشیده و بنون زده » بمعنی
تنیدن* بر وزن رمیدن » معررف
```


## [2026-10-15T02:46:50.299Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR-1==637' BQT_v1_pages.txt | grep -n -B2 -A6 \"پشو\" | head -40"
}
```


### [2026-10-15T02:46:51.051Z] TOOL RESULT

```
14-و دعای بد راگویند ؛ ویاسین بی‌قطه هم آمده
15-است ۲
16:پشول » بر وزن اصول ۰ بمعنی پشور
17-است که نفرین ودعای بد باشد ۴ .
18-بو لیده باواو مجهول ولام بروزن
19-نکوهیده" » پرشان و ژولیده و پراکنده را
20-(۱) چب ۱ چش: هجرالبق .
21-٩‏ - شنجر همه تش انجدماند
22-.۰ رك : بشنجیدن ویشنجد.
--
43-لمیبی . «لفت نامه».
44-بت ۴ رك : یشور .
45:طرة دوست پشولیده خوش است ۰
46-شرف شفروه. «لغت نامه».
47-دوم هردو آهثبه :
48-. پشه‌کی داند که عمرش تاکی است
49-۲ ره : بشمدار -
50-دربهاران زاد ومر کش در دی است.
51-مثنوی‌مولوی‌بلخی.
```


## [2026-10-15T02:46:55.009Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR-1==636' BQT_v1_pages.txt | grep -n \"^ *پ\\|^ *ب\\|تن\\b\\|tanu\\|اوستا\" | head -30; awk 'BEGIN{RS=\"\\f\"} NR-1==145' BQT_v1_pages.txt | grep -n -B2 -A3 \"پشوت\""
}
```


### [2026-10-15T02:46:55.479Z] TOOL RESULT

```
2:باشد ۰ 3
3:بشکله ‌‌ بفتح لام بمعنی شکل است
6:پشکلید » بکر اول و لام بروزن دل
8:پشکم ه بکر اول بر وزت اشکم »
11:بشل -
18:بشلنگ - نم اول و فثح لام بر وذت
23:پشما گنف* م بنخ اول و سکون انی
29:بين پشت‌ستود و تنگک بار گذارند وپالان الاغ‌را
34:باشد «هنی صاحب نفس و صاحب غیرت نباشد .
35:بشم‌شدن » بمعنی پراگنده شدن -
36:وپرا گنده ساختن باشد - و جدابی کردن را نیز
38:پشمات » بروزن چنمك, سا
46:پشنجد- بکر اول وفتح ثانی وسکون
10-خودکار ایران. ۱۳۲۶شمسی. (<- حماسه سرایی). .
11-۴هخر ده اوستا. غیروتالیف ابر اهیم پورداود. .از سلسله | نتشارات
12:|نجمن‌زرتشتیان ایرانی بمبتی وایران لیک (از نفقةٌ پشوتن مارکر). ۱۳۱۰
13-هه دارو نامه. دکتر احمد پارسا. از نشریات موز علوم طبیعی .
14-تپران. چاپغا * داتش (بدون ثاریخ).
15-"هم دانش (مجله). کتا خروشی دانش. دو دوره. تهر ان.از ۱۳۲۸
```


## [2026-10-15T02:46:59.223Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR-1==637' BQT_v1_pages.txt | sed -n 1,13p; awk 'BEGIN{RS=\"\\f\"} NR-1==637' BQT_v1_pages.txt | sed -n 23,42p"
}
```


### [2026-10-15T02:47:00.332Z] TOOL RESULT

```
۳
لشنجیده - بر وزن ستمد‌یده ؛ یعئی
باشد ۷ . .
بشنگ بروزن پلنگه, نام‌پدرافراسیاب
است - و نام پس او که شیده میگفتند- و نام
مبارزی از ابرانسونام پدرمنوچهر شام ومیل آهنیی‌را
گوینددرازوسر تیز که‌تابان‌بدانبوارسوراخ کنند
- و بمعنی زتبر هم آمده است هو آن کلیمی
نا نخته‌ای باشدکه بردو سرآن دو چوب تبیه
کنند وبدان خشت و گل وخالك وامثال آ نکشند
- و جفا وستم وجور و محنت را نیز گفته‌اند -
وترشحآب وفیر آنرا نیز گوبند ۴» وباین معنی
متکتی. ول وثالی‌هم درست است .3
۵ دل دروش سراسمه به است
گونند ۵ .
لشه - بفتح اول
۴1 ثانی هشن ء حانوری
است ممروف گونند چهل
روزعمر کند وبعضی گویند
بته خانه. با خای نقطه دار بالف
کشبده وفتح نون» نام‌درخت صده است که سربی
شجرقالیق (۱) خوانند ۷ .
بشه جورد » بفتح خای نفطه دار
و سکون واو ممدوله و را ودال بی‌تقطه » ریشی
و جراحتی باشد که بیشتر در ملك بلخ بهم رسد
و دیر خوب شود و کمان مردم اينکه از گزیدن
پثه بهم میرسد و آن را بعربی فرحة بلخی
گونند .
بشه‌ذاد ۸ ۰ بادال ابجد بالف کشیده
و برای قرشت زده . پثه خانه را گویند و آن
درختی است که بعربی شجرتالیق خوانند .
پشه‌غال » با ین نله دار و لام :
بر آن خاك و خوش پشنجید‌اند .
```


## [2026-10-15T02:47:04.069Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^tennis,\\|^antenna,\\|^thunder,\\|^tone,\\|^temperature,\\|^tent,\\|^thin,\\|^tornado,\\|^astonish,\\|^detonate,\" KLN_1966.txt | head -20"
}
```


### [2026-10-15T02:47:04.609Z] TOOL RESULT

```
38494:temperature,  n.  —  L.  temperdtura,  ‘due  measure, proportion,  composition,  temper,  tempera¬ ment’,  fr.  temperdtus,  pp.  of  temperare.  See temperate  and  -ure.  In  its  physical  sense,  L. temperdtura  was  first  used  by  the  Italian  physi¬ cist  and  astronomer  Galileo  Galilei  (1564-1642).
38548:tennis,  n.  —  ME.  teneis,  fr.  AF.  tenetz,  fr.  OF.
38577:tent,  n.,  attention  (now  Scot,  and  dial.  English).
38579:tent,  tr.  v.,  to  attend  to  (now  Scot,  and  dial. English).  —  Prob.  short  for  take  tent.  See prec.  word.
38580:tent,  n.,  a  sweet  Spanish  wine.  —  Sp.  Unto,  ‘red (wine)’,  lit.  ‘dyed,  tinged’,  fr.  L.  tinctus,  pp.  of tingere,  ‘to  soak  in  color,  dye’ ;  See  tinge  and  cp. taint,  tint,  tincture.
39038:thin,  adj.  —  ME.  thinne,  fr.  OE.  pynne,  rel.  to  OS. thunni,  ON.  punnr,  Swed.  tunn,  Norw.  tunn, tynn,  Dan.  tynd,  MDu.  dunne,  Du.  dun,  OFris. thenne,  OHG.  thunni,  dunni,  MHG.  diinne,  G. dtinn,  ‘thin’,  orig.  ‘stretched  out’,  and  to  OE. penian,  ON.  penja,  OHG.,  MHG.  dennen,  de- nen,  G.  dehnen,  Goth,  uf-panjan ,  ‘to  stretch,  ex¬ tend’,  fr.  I.-E.  base  *ten-,  ‘to  stretch,  extend’, whence  also  OI.  tanuh  (fern,  tanvi),  tanukah, ‘thin,  tender’,  lit.  ‘stretched  out’,  Homeric  Gk. xavao?,  ‘stretched  out,  long’,  Gk.  xavu-, ‘stretched  out,  long'  (as  in  xavdyXoiaao;,  ‘long- tongued’),  L.  tenuis,  ‘thin,  slender’,  tenus,  ‘cord, snare’,  OSlav.  tinukO,  tinikii,  ‘thin’,  dial.  Lith. tenvas,  Lett,  tiews,  ‘slender’,  OIr.  tan(a)e,  Co. tanow,  W.  teneu,  MBret.  tanau,  ‘thin’.  See  tend, ‘to  move  in  a  certain  direction’,  and  cp.  tenuis. Derivatives:  thin,  tr.  and  intr.  v.,  thin-ly,  adv., thin-ness,  n.
39175:thunder,  n.  —  ME.  thuner,  later  thunder,  fr.  OE. punor,  rel.  to  ON.  porr,  OFris.  thuner,  MDu. donre,  donder,  Du.  dander,  OHG.  donar,  MHG. doner,  donre,  toner,  G.  Donner,  from  the  I.-E. imitative  base  *ten-,  whence  also  OI.  tanayitnuh, ‘thundering’,  tanyati,  ‘it  thunders',  Pers.  tundar, ‘thunder’,  Aeol.  Gk.  revvet  (Hesychius),  ‘moans, sighs,  groans',  L.  tonare,  ‘to  thunder’,  tonitrus, ‘thunder’.  The  same  base,  enlarged  with  initial s,  appears  in  OI.  stdnati,  stdniti,  standyati,  ‘it
```


## [2026-10-15T02:47:07.772Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 38548,38552p KLN_1966.txt; grep -n \"^antenna\\|^tent,  n\\|^tone,\\|^tornado\\|^astonish\\|^tenuous\\|^tension\" KLN_1966.txt | head; grep -n \"^antenn\\|^antemn\" KLN_1966.txt SKT.txt LAT.txt | head"
}
```


### [2026-10-15T02:47:08.269Z] TOOL RESULT

```
tennis,  n.  —  ME.  teneis,  fr.  AF.  tenetz,  fr.  OF.
(=  F.)  tenez,  ‘hold!’,  pi.  imper.  of  tenir,  ‘to hold’;  see  tenable.  The  game  was  so  called  from the  w'ord  used  by  the  server  when  throwing  the ball.
teno-,  before  a  vowel  ten-,  combining  form  de¬ noting  the  tendon  (anat.)  —  Gk.  tevo-,  tsv-,  fr. t£vcov,  ‘sinew,  tendon’;  see  tendon  and  cp. tenonto-.
tenon,  n.,  a  projection  inserted  to  make  a  joint.
—  ME.,  fr.  OF.  (=  F.),  fr.  tenir,  ‘to  hold’. See  tenable.
38577:tent,  n.,  attention  (now  Scot,  and  dial.  English).
38580:tent,  n.,  a  sweet  Spanish  wine.  —  Sp.  Unto,  ‘red (wine)’,  lit.  ‘dyed,  tinged’,  fr.  L.  tinctus,  pp.  of tingere,  ‘to  soak  in  color,  dye’ ;  See  tinge  and  cp. taint,  tint,  tincture.
38608:tenuous,  adj.,  thin.  —  Formed  with  suff.  -ous  fr. L.  tenuis.  See  prec.  word.
LAT.txt:4199:antenna, -ae f.(surtout an plnriel, parce que la vergue est souvent
LAT.txt:4201:antenna doit noter une prononciation tardive, avec assimilation dn
LAT.txt:60783:antemnas ad mallos destinabant, et destina: appui, support (Vitr.).
```


## [2026-10-15T02:47:10.598Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4195,4210p LAT.txt; grep -n -i \"^antenna\\|^ANTENNA\" KLN_1966.txt KLN_1971.txt SKT.txt | head -3"
}
```


### [2026-10-15T02:47:10.856Z] TOOL RESULT

```
comae dans skr. nicd, v.sl. nict, sons forae de derive thematique; cf.
praeceps, sons caput.
antegerio ( anti -): - antiqui pro ualde dixerunt, P.F.7,33. Mot de
glossaire, sans donte de ante et gero.
antenna, -ae f.(surtout an plnriel, parce que la vergue est souvent
formee de deux pifeces de sapin liees enseable, cf. Rich. s.u.; la graphie
antenna doit noter une prononciation tardive, avec assimilation dn
gronpe -nn-): vergue(s); correspond i gr.e71ucpl.ov. Deja dans Piante;
techniqne. M.L.498. Mot sans donte eaprunt 4 , comae la plupart des termes
nautiqnes dn latin.
antistes: v. sto.
antrum, -I n. : caverne, antre. Eaprunt d'abord poetiqne et litt 4 -
raire (Vg., 4 poq. d'Aug.) an gr. avTpov, passe ensnite dans la prose
(P6tr., Plin.) et chez les antenrs chr6tiens.
D6riv6 tardif: antrdlis.
anus, -us f.: vieille femae; joint k senex, oppos6 k puer. Sert
KLN_1971.txt:16099:antenna, n. — ModL., feeler or horn of an in- 
KLN_1971.txt:16107:Antennaria, n., a genus of herbs, plants of the 
KLN_1971.txt:218871:antennae {zool.) — ModL., lit. ‘having sawlike
```


## [2026-10-15T02:47:13.139Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 16099,16106p KLN_1971.txt; grep -n \"^ANTENNA\\|^TENNIS\\|^TONE\\b\\|^TORNADO\\|^ASTONISH\\|^THUNDER\" SKT.txt | head"
}
```


### [2026-10-15T02:47:13.614Z] TOOL RESULT

```
antenna, n. — ModL., feeler or horn of an in- 
sect’, fr. L. antemna , antenna , ‘sail yard’, which is 
of uncertain origin. It is perh. a contraction of 
*an(a)tempna , ‘that which is stretched, extend- 
ed’, fr. I.-E. base *temp-, ‘to stretch, extend’. See 
temple, ‘place of worship’, and cp. next word. 
Derivative: antenn-al, adj.
```


## [2026-10-15T02:47:17.543Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^Thunder\\|^Tornado\\|^Astonish\\|^Tennis\\|^Tone\\b\\|^Thin\\b\\|^Antenna\\|^ANTENNA\\|^THUNDER\" SKT.txt | head; grep -n \"tornado\\b\" SKT.txt | head -3"
}
```


### [2026-10-15T02:47:17.993Z] TOOL RESULT

```
19584:Thin.  lE,)    M.E.  |>mii^    A. +  Du.  dun^    IccL  ^mmr,  Dan. tynn'),  bwed.  twm,  G.diiMM.  + Gael  Iriih  tana,  Ross,  itnkii, Gk.   rafaut,  Skt.  fmmu.      lit. out.*     (V  T.\N.)
19662:Thunder,  sb.  (E.)  For  thuntr;  the  d is  excrescent.  M.K.  Jw/«r.  A.S.  putiar. »A.  S.  ^um'an,  to  rattle,  thunder;  cf.  ^- !>««,  a  loud  noisc.+Du.  dffttdcr;  Icel.  JiJrr (for  JwMr),  Thor,  god  of  thunder  ;  G. dfinner.'^h.  tonare,  lo  thunder,  Skt  tan, to  sound,  p.  We  further  find  A.  S.  tonian, to  thunder,  which  points  to  loss  of  initial X,  3p|>caring  in  Skt.  r/<irf,  to  sound,  thunder, sigh,  sfanita,  thunder,  and  in  K.  stun. VSTAN.)
19916:Tornado  ;  sec  Turn.
20321:-  F.  «-  (  =  L.  rf),  back  ;  taurner,  lu  in tornado,    a    horricauc.    (Spatj.  •  1
23456:real  (a\  renegade  (rcncgado^,  salver.  ■hcrTy, ■tcvrdore.  tent  V3),  tornado,  ultramarine, vanilla,  venndnh.
```


## [2026-10-15T02:47:26.902Z] TOOL CALL #40: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/w502 && cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/w502 && for t in \"آبستن\" \"تندر\" \"تنک\" \"تنکه\" \"پشوتن\" \"تهمتن\" \"تن\" \"تنیدن\" \"antenna\" \"tornado\" \"Reconstruction:Proto-Indo-European/(s)tenh₂-\" \"Reconstruction:Proto-Indo-European/ténh₂us\" \"Reconstruction:Proto-Indo-European/ten-\" \"Reconstruction:Proto-Iranian/tanHúš\" \"آنتن\" \"تنیس\" \"تن\"; do f=$(echo -n \"$t\" | md5sum | cut -c1-8); curl -s \"https://en.wiktionary.org/w/index.php?title=$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" \"$t\")&action=raw\" -o \"$f.txt\"; echo \"$t $f $(wc -c < $f.txt)\"; done"
}
```


### [2026-10-15T02:47:30.467Z] TOOL RESULT

```
آبستن 0e3cb66e 995
تندر 25a0865c 1541
تنک 13cd6d59 1178
تنکه ec54d0ca 456
پشوتن 464bb443 1928
تهمتن f982273b 1928
تن 352de520 2774
تنیدن 22186434 662
antenna f212100e 15953
tornado 99bdf8d9 13440
Reconstruction:Proto-Indo-European/(s)tenh₂- 02f8ff74 2172
Reconstruction:Proto-Indo-European/ténh₂us 98b414cd 2172
Reconstruction:Proto-Indo-European/ten- ad97e5b3 2172
Reconstruction:Proto-Iranian/tanHúš 2caa2554 2172
آنتن b9938551 2172
تنیس dd8b22a5 2172
تن 352de520 2774
```


## [2026-10-15T02:47:34.557Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/w502; for f in 0e3cb66e 25a0865c 13cd6d59 ec54d0ca 464bb443 352de520 22186434; do echo \"#### $f\"; grep -v \"^\\s*$\" $f.txt | head -30; done; head -c 400 02f8ff74.txt; grep -n -A6 \"===Etymology\\|==Latin==\" f212100e.txt | head -40; grep -n -A4 \"Etymology\" 99bdf8d9.txt | head -12"
}
```


### [2026-10-15T02:47:35.032Z] TOOL RESULT

```
#### 0e3cb66e
==Khalaj==
===Adjective===
{{head|klj|adjective|head=آبِستَن|tr=âbistən}}
# {{spelling of|klj|Arabic|âbistən|t=[[pregnant]]}}
==Persian==
{{wp|fa:}}
===Alternative forms===
* {{alt|fa|اوسن|tr=owsan||dialectal|Khesht|Konartakhteh}}
===Etymology===
From {{inh|fa|pal||tr=ʾpwstn'|ts=ābustan, ābistan}}, from {{m|pal||tr=ʾpws|ts=ābus|t=pregnant}}, from {{der|fa|ira-pro|*āpuθra-|t=pregnant}}, from {{m|ira-pro|*puθráh|t=son}}, from {{der|fa|iir-pro|*putrás|t=boy; son}}, from {{der|fa|ine-pro|*putlós}}.
===Pronunciation===
{{fa-IPA|ābistan}}
===Adjective===
{{fa-regional|آبستن|آبستن|обистан}}
{{fa-adj|tr=âbestan}}
# {{lb|fa|formal}} [[pregnant]]
#: {{syn|fa|حامله|q1=colloquial|tr1=hâmele|باردار|tr2=bârdâr}}
====Inflection====
{{fa-adj-pred-c|âbestan}}
====Derived terms====
* {{l|fa|آبستنی|tr=âbestani}}
====Descendants====
* {{desc|gu|આબિસ્તા|bor=1}}
* {{desc|klj|âbistən|bor=1}}
{{C|fa|Pregnancy}}
#### 25a0865c
{{also|تنذر|بندر}}
==Arabic==
===Etymology 1===
====Verb====
{{ar-verb|V.pass}}
# {{rfdef|ar}}
=====Conjugation=====
{{ar-conj|V.pass}}
===Etymology 2===
====Verb====
{{ar-verb form|+أندر<IV>}}
==Persian==
===Etymology===
{{root|fa|ine-pro|*(s)tenh₂-}}
From {{inh|fa|ira-pro|*tánHtā}}, from {{inh|fa|iir-pro|*tánHtā|*tánHtar-}}, from {{inh|fa|ine-pro||*ténh₂-tōr}} or {{m|ine-pro||*tónh₂-tōr}}, whence {{cog|la|tonitrus}} may also be derived; ultimately from {{m+|ine-pro|*(s)tenh₂-||to thunder, resound}}. Compare similarly {{m|ine-pro||*tónh₂-r̥}}, whence {{cog|gem|-}} and {{cog|cel|-}} cognates.
Cognate with {{cog|xpr|𐫤𐫗𐫅𐫇𐫡|ts=tandur}}, {{cog|sog|𐼚𐼇𐼎𐼚𐼘|ts=tundar}}, {{cog|sa|स्तनति||to resound; to thunder}}, {{cog|ga|torann||thunder, loud noise}}, {{cog|en|thunder}}.
===Pronunciation===
{{fa-IPA|tun`dar,tun`dur}}
* {{audio|fa|Tondar (Iranian Persian).wav|a=Iran}}
===Noun===
{{fa-regional|تندر|تندر|тундар}}
{{fa-noun|cls=تُنْدَر|cls2=تُنْدُر}}
# [[thunder]]
#: {{syn|fa|رعد|tr=ra'd}}
# [[roaring]]
# a [[nightingale]]
====Descendants====
* {{desc|ur|تندر|tr=tundar|bor=1}}
===References===
* {{R:STEIN}}
#### 13cd6d59
{{also|بنك|تنك|بنگ|تنگ}}
==Persian==
===Etymology===
{{inh+|fa|pal||sc=Phlv|tr=tnwk'|ts=tanuk|t=thin, shallow}}, from {{inh|fa|ira-pro||*tanúkakah}}, from {{der|fa|ine-pro|*ténh₂us|*tn̥h₂ukos ~ ténh₂ukos|t=thin}}.
===Pronunciation===
{{fa-IPA|cls=tanuk,tunuk|tunuk}}
===Adjective===
{{fa-adj|tr=tonok}}
# [[thin]]
# [[sparse]], [[porous]] (not-[[dense]])
====Derived terms====
* {{l|fa|تنکه|tr=toneke|t=underwear}}
* {{l|fa|تنک‌بیز|tr=tanuk-bēz}}, also {{l|fa|تنگ‌بیز|tr=tang-bēz|t=sieve}}
* {{l|fa|تنک‌ظرف|tr=tanuk-zarf|t=dimwit; tattler}}
====Related terms====
* {{l|fa|تنگ|tr=tang|t=narrow}}
'''Antonym'''
* [[چگال]] (dense)
* [[ستبر]] (thick)
===References===
* {{cite-book|year=2009|title=Exegisti Monumenta. Festschrift in Honour of Nicholas Sims-Williams|chapter=On the History of Middle Persian Nominal Inflection|page=19|pageurl=https://www.google.de/books/edition/Exegisti_Monumenta/b3gOdaiXNKkC?hl=de&gbpv=1&dq=%22tnwk%22+%22Middle+persian%22&pg=PA19&printsec=frontcover|publisher=Otto Harrassowitz|location=Wiesbaden|last=Cantera|first=Alberto|isbn=9783447059374}}
* {{R:fa:Steingass|page=329b}}
#### ec54d0ca
==Persian==
===Etymology===
From {{af|fa|تنک<tr:tonok><t:thin, flimsy>|ـه<tr:-e>}}.
===Pronunciation===
{{fa-IPA|tunuˈka}}
===Noun===
{{fa-noun|tr=tonoke}}
# [[wrestler]]'s [[shorts]]
# {{lb|fa|dated}} [[underwear]], [[underclothing]]
# {{lb|fa|dated}} [[thin]] [[sheet]] of [[metal]]
====Descendants====
* {{desc|chg|تنکه|ts=tunukä|bor=1}}
** {{desc|uz|tunuka}}
* {{desctree|ota|bor=1|تنكه|tr=teneke}}
===Further reading===
* {{NPED}}
#### 464bb443
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
#### 352de520
{{also|بن|ثن|پ.ن}}
==Arabic==
===Etymology 1===
{{wp|ar:}}
{{etymon|ar|:bor|la:thunnus|text=:grc}}
====Pronunciation====
{{ar-pr|تُنّ}}
====Noun====
{{ar-noun|تُنّ|m}}
# [[tuna]]
=====Declension=====
{{ar-decl-noun|تُنّ}}
=====Descendants=====
* {{desc|id|tuna|bor=1}}
* {{desc|roa-opt|bor=1}}
** {{desc|gl|atún}}
** {{desc|pt|atum}}
* {{desctree|osp|atun|bor=1}}
===Etymology 2===
====Verb====
{{ar-verb form|+ونى<I>}}
{{C|ar|Scombroids}}
==Burushaski==
===Etymology===
{{rfe|bsk}}
===Pronunciation===
* {{IPA|bsk|[tin]}}
===Noun===
{{head|bsk|noun|tr=tin}}
# {{lb|bsk|anatomy}} [[bone]]
#### 22186434
==Persian==
===Etymology===
From {{inh|fa|pal|tr=tn-|ts=tan-}}, present stem of {{m|pal|tr=ttn'|ts=tadan|t=to weave}}; the verb was regularized according to the present stem. Ultimately from {{inh|fa|iir-pro|*tanáwti}}, from {{inh|fa|ine-pro|*tn̥néwti}}, from {{m|ine-pro|*ten-||to stretch, draw}}.
===Pronunciation===
{{fa-IPA|tanīˈdan}}
===Verb===
{{fa-verb|tr=tanidan|prstem=تن|tr2=tan}}
# to [[spin]] (a thread, a web, a cocoon, etc.)
#: {{coa|fa|در هم '''تنیده'''|tr=dar ham '''tanide'''|t=inter'''twine'''d}}
# to [[weave]]
# to [[twist]]
# {{lb|fa|archaic}} to [[pay attention]]
====Conjugation====
{{fa-conj|تنید|tanid|تن|tan}}
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #5:===Etymology===
6-{{root|en|ine-pro|*h₂ent-|*ten-}}
7-{{bor+|en|la|antenna|antenna, antemna|yard, sailyard; pole}}.  First used in this sense as a Latin word in the 15th century<ref name="NED">{{R:New English Dictionary|volume=I|page=357|column=2}}</ref> and as an English word by the end of the 17th century.
8-
9-===Pronunciation===
10-* {{IPA|en|/ænˈtɛn.ə/}}
11-* {{audio|en|en-us-antenna.ogg|a=US}}
--
189:===Etymology===
190-{{inh+|it|la|antenna}}, the scientific senses were borrowed later.
191-
192-===Pronunciation===
193-{{it-pr|anténna}}
194-* {{audio|it|LL-Q652 (ita)-LangPao-antenna.wav}}
195-
--
204:==Latin==
205-
206:===Etymology===
207-{{root|la|ine-pro|*h₂ent-|*ten-}}
208-May be from {{inh|la|itc-pro|*antitempnā}}, from {{der|la|ine-pro|*ten-|*temp-|to stretch, extend}}.
209-
210-===Pronunciation===
211-* {{la-IPA|antenna}}
212-
5:===Etymology===
6-From earlier English {{m|en|ternado}}, attested since the 1550s as a nautical term for a windy thunderstorm.<ref>{{R:Dictionary.com}}</ref> From {{der|en|es|tronada|t=thunderstorm}}, from {{m|es|tronar|t=to [[thunder]]}}, from {{der|en|la|tonō|t=to [[thunder]]}}, from {{der|en|ine-pro|*(s)tenh₂-|t=to [[thunder]]}}. The ''o'' and ''r'' were reversed in English ({{metathesis|en}}) under influence of {{noncog|es|tornar|t=to twist, to turn}}, from {{noncog|la|tornō|t=to turn}}.
7-
8-===Pronunciation===
9-* {{enPR|tô(r)-nā'dō|a=UK}}, {{IPA|en|/tɔː(ɹ)ˈneɪ.dəʊ/}}
--
217:===Etymology===
218-From {{der|da|en|tornado}}.
219-
220-===Noun===
221-{{da-noun|en|er}}
--
```


## [2026-10-15T02:47:43.952Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/w502; for t in \"پشوتن\" \"تهمتن\" \"Reconstruction:Proto-Indo-European/(s)tenh₂-\" \"Reconstruction:Proto-Indo-European/ténh₂us\" \"Reconstruction:Proto-Iranian/tanHúš\" \"tennis\" \"آنتن\"; do f=$(echo -n \"$t\" | md5sum | cut -c1-8); curl -s -A \"rishe-verify/1.0 (research)\" \"https://en.wiktionary.org/w/index.php?title=$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" \"$t\")&action=raw\" -o \"$f.txt\"; echo \"$t $f $(wc -c < $f.txt) $(head -c 30 $f.txt)\"; done"
}
```


### [2026-10-15T02:47:45.919Z] TOOL RESULT

```
پشوتن 464bb443 1928 <!DOCTYPE html>
<html lang="en
تهمتن f982273b 1928 <!DOCTYPE html>
<html lang="en
Reconstruction:Proto-Indo-European/(s)tenh₂- 02f8ff74 2651 {{reconstructed}}
==Proto-Indo
Reconstruction:Proto-Indo-European/ténh₂us 98b414cd 1653 {{reconstructed}}
==Proto-Indo
Reconstruction:Proto-Iranian/tanHúš 2caa2554 1928 <!DOCTYPE html>
<html lang="en
tennis 1fbfb233 14540 {{also|Tennis}}
==English==
{{
آنتن b9938551 1928 <!DOCTYPE html>
<html lang="en
```


## [2026-10-15T02:47:49.434Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/w502; cat 02f8ff74.txt | head -40; cat 98b414cd.txt | head -30; grep -n -A3 \"===Etymology\" 1fbfb233.txt | head -6; head -5 464bb443.txt | grep -i \"404\\|not\\|error\" "
}
```


### [2026-10-15T02:47:49.627Z] TOOL RESULT

```
{{reconstructed}}
==Proto-Indo-European==

===Etymology===
{{ety|ine-pro|pos=root|:from<unc>|*sten-}}
Possibly extended from {{m|ine-pro|*sten-|t=to groan}}.<ref>{{R:inc:IAIL|stan⁽ⁱ⁾|pages=472-473}}</ref>

===Root===
{{ine-root}} <ref name="LIV">{{R:ine:LIV|head=*(s)tenh₂-|page=597}}</ref><ref>{{R:inc:EWAia|vol=2|head=STAN¹|page=752|passage=Idg. *(s)tenh₂}}</ref>

# to [[thunder]]

====Derived terms====
* {{?}} {{l|ine-pro||*(s)ténh₂-e-ti|pos=thematic root present}}
** {{desc|itc-pro|*tenō}}<ref name="EDL">{{R:itc:EDL|tonō, -āre|623|PIt. *tena- [pr./aor.], *tonaje- [pr.]; PIE *(s)tenh₂- [aor.] ‘to thunder’, *(s)tonh₂-eie/o- [pr.]}}</ref>
*** {{desc|la|tonō|t=to thunder}} {{q|readjusted to iterative<ref name="EDL" />}} {{see desc}}
* {{l|ine-pro||*(s)ténh₂-t ~ (s)tn̥h₂-ént|pos=athematic root aorist}}<ref name="LIV"/>
** {{desc|iir-pro|*HástanHt}}
*** {{desc|inc-pro|*HástanHt}}
**** {{desc|sa|*अस्तनीत्|tr=*ástanīt}}<ref name="LIV"/>
***** {{desc|sa|स्तन्|pos=3sg.inj.act|der=1|स्तनिहि|pos2=2sg.impv.act.|t2=to thunder}}
* {{l|ine-pro||*(s)tén-ye-ti|pos=ye-present}}<ref name="LIV"/> {{q|< {{l|ine-pro||*(s)ténh₂-ye-ti}}<ref name="LIV"/> with Pinault's law}}
** {{desc|iir-pro|*tányati}}
*** {{desc|inc-pro|*tányati}}
**** {{desc|sa|तन्यति|t=to thunder}}
* {{l|ine-pro||*(s)tonh₂-éye-ti|pos=iterative}}<ref name="LIV"/><ref name="EDL" />
** {{desc|iir-pro|*stanHáyati}}
*** {{desc|inc-pro|*stanHáyati}}
**** {{desc|sa|स्तनयति|tr=stanáyati|t=to thunder}}
** {{desc|itc-pro|*tonaō}}<ref name="EDL" />
*** {{desc|la|tonō|t=to thunder}} {{see desc}}
* {{desc|ine-pro|alt=*(s)ténh₂-tr̥ ~ *(s)tn̥h₂-tén-s|nolang=1}}
** {{desc|iir-pro|*tánHtā|t=thunder}} {{see desc}}
** {{desc|itc-pro|*tenatrus}}
*** {{desc|la|tonitrus|t=thunder}} {{q|readjusted to iterative}} {{see desc}}
* {{l|ine-pro||*(s)tónh₂-r̥ ~ *(s)ténh₂-n̥s, *(s)ténh₂-r̥ ~ *(s)tn̥h₂-éns}}
** {{desc|cel-pro|*toranos|t=thunder}} {{q|< {{l|cel-pro||*tonaros}} < {{l|ine-pro||*(s)tónh₂r-os}}<ref name="EDPC" />}} {{see desc}}
** {{desc|gem-pro|*þunraz|alt=*þun(a)raz|t=thunder}} {{q|< {{l|ine-pro||*(s)tn̥h₂r-os}}<ref name="EDPC">{{R:cel:EDPC|head=*torano-|page=384|passage=PIE *(s)tonHr- / *stnHr-os}}</ref>}}  {{see desc}}

====Descendants====
{{reconstructed}}
==Proto-Indo-European==

===Etymology===
{{ety|ine-pro|:af|*tenh₂-<t:to stretch>|*-us<pos:Caland system suffix>}}
From {{af|ine-pro|*tenh₂-<t:to stretch>|*-us<pos:Caland system suffix>}}.

===Adjective===
{{ine-adj}}<ref name="LIN *tenh₂-">{{R:ine:LIN|pages=694-698}}</ref>

# [[thin]]

====Inflection====
{{ine-decl-adj|ac=proterokinetic|ténh₂u|tn̥h₂éw|tn̥h₂éwih₂|tn̥h₂uyéh₂}}
Later pattern:
{{ine-decl-adj|tn̥h₂ú|tn̥h₂éw|tn̥h₂éwih₂|tn̥h₂uyéh₂}}

====Derived terms====
* {{l|ine-pro||*tenh₂-w-ó/éh₂-}} / {{l|ine-pro||*tn̥h₂-ew-ó/éh₂-}}<ref name="LIN *tenh₂-"/><ref name="D tęvas">{{R:bat:EDBIL|pages=464–465}}</ref>
** {{desc|ine-bsl-pro|*tenˀwas}} {{see desc}}
** {{desc|grk-pro|*tanawós}}
*** {{desc|grc|τᾰνᾰός}}
*** {{desc|gmy|𐀲𐀙𐀷}}, {{l|gmy|𐀲𐀙𐀺}}
* {{l|ine-pro||*tn̥h₂-ew-yó/yéh₂-}}<ref name="LIN *tenh₂-"/>
** {{desc|cel-pro|*tanauyos}} {{see desc}}
* {{l|ine-pro||*tn̥h₂-u-kos ~ ténh₂-u-kos}}<ref name="LIN *tenh₂-"/><ref name="D tęvas"/><ref>{{R:sla:EDSIL|head=*tьnъkъ|505}}</ref>
** {{desc|ine-bsl-pro|*tinˀukas}}
*** {{desc|sla-pro|*tьnъkъ|alt=*tь̏nъkъ}} {{see desc}}
** {{desc|iir-pro|*tánukas}}
*** {{desc|inc-pro|*tánukas}}
7:===Etymology===
8-{{ety|en|tree=1|:inh|enm:tennys//teneys//tenis<ety:der<fro:tenir<alt:tenir, ~nez>>>}}
9-From {{inh|en|enm|tennys,teneys,tenis}}, from {{der|en|fro|tenez|pos={{lg|second person|second-person}} {{lg|plural number|plural}} {{lg|imperative mood|imperative}} of {{m|fro|tenir|t=to hold}}}}.
10-
--
228:===Etymology===
<title>Wikimedia Error</title>
```


## [2026-10-15T02:47:58.295Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/w502; for t in \"پشوتن\" \"تهمتن\"; do f=$(echo -n \"$t\" | md5sum | cut -c1-8); curl -s -A \"rishe-verify/1.0 (research; contact eslaminavid0@gmail.com)\" \"https://en.wiktionary.org/w/index.php?title=$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" \"$t\")&action=raw\" -o \"$f.txt\"; echo \"$t $(head -c 300 $f.txt)\"; done; curl -sL \"https://www.iranicaonline.org/articles/pesotan\" | sed 's/<[^>]*>//g' | grep -i -m5 \"pešōtan\\|Pəšō\\|Pišōtan\\|body\""
}
```


### [2026-10-15T02:47:59.301Z] TOOL RESULT

```
پشوتن <!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; fle
تهمتن <!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; fle
Just a moment...*{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width Enable JavaScript and cookies to continue(function(){window._cf_chl_opt = {cFPWv: 'g',cH: 'X40XkLmRM20z9TNZYjXZ.VcswguQt69JKKSHad0hdt0-1792032479-1.2.1.1-KZqQ_bgEbFhLrCWtY_QWzJtbWZyNge.F0M_fQjPzhQER7RyMk7aQ_UMZNUZ0sEaW',cITimeS: '1792032479',cN: 'Ce8ZIhPTr5Xb5Ifj7JiFWz',cRay: 'a4ab80937af3eff9',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/articles/pesotan?__cf_chl_tk=NmfNTFZj9mMNCvXS7xHoO4fEXwnXAmvjN.GxoL0tqZM-1792032479-1.0.1.1-KTJnT_VM8OyWfkh3vI9DcreDcwllg6DqiKTXH7zIFsQ",cvId: '3',cZone: 'www.iranicaonline.org',fa:"/articles/pesotan?__cf_chl_f_tk=NmfNTFZj9mMNCvXS7xHoO4fEXwnXAmvjN.GxoL0tqZM-1792032479-1.0.1.1-KTJnT_VM8OyWfkh3vI9DcreDcwllg6DqiKTXH7zIFsQ",md: 'bU4oh4qtQ668JvqADI94r5rp63aZriq5Ws5HDLqwH3s-1792032479-1.2.1.1-zg3KdguMFjZqpzQvhcFat8vn1.xVGAlA4YJMUbAKDYKUK2CRZDSRIErDx2Pwkq0s8hql2FxRk3_AQOmtG6rgl2RRJi5270u9H5st5S8e9XsZdPo40csomUTXxE9w5OLYwKNVtypcsgQLAVqPXWBkVvQwyAZAtYH5dWj25Lb8k38JHQ7E8.M7EJ5OKixm7wWkTuwZ7PN_PgdGtmiEU87ia1SrhHZxYyBhCG0zdwZo2Hyj4YyNI8FxcnVWsDzEXpWC9UDN8p01MpzlE7ST4D.hE4rd2z9YEi6rrFu6Dcvnhq8.PL0PIOZ6fNB1hsp.8gxp7O.O9XfLGf2.675_u2lMlBS5VV4IJ2zYXZ8WSCOGVnKH9OJja50I87IgOurwtpyzs3.vPC_y1JP_0sHlB5krVF4BAdb_JDjsEASqGs3EmDCdpGIX59n3h_6OJY3pXAHlLGfMW_42CwxFCdJTzLa443.RmkpyA5fX2GDtaKR7q18NC_TOuop8xU2Do2umboKufJgEJVLrazumvowFoH3.J5prwBHHEFJ8MNH7Ppr2M6Ejsj70WBws1wkY9ObQkLUWAd.tFfuBEld07ytgQ1SB6.jWiHzZzHNFpfU1ypBukU5ljF_zEmm1mpDlxkljFB2uvRdi7V4LS6EHLSTQFw.k0qJDmhCeDZeM1fOXu19.Bo5fwW2xaWNHdrJzm.uFStTL5X0CIRe37_pb7byz3xMOY5LR0Th8r.lZHwT7iWeG59dYLFVd6o93zJz_ZKbTEvZdR8WB_aW8VE6j40gJnrZH5oQqyU4BZl_VeLqrg7G5erQidJLEBGp1pxEUzhMAPo8.3hXVDGgQrl1D8azdwU7q2U3wGHtCN1WiDlKcLGap09q1Upms7J_NPdrZ6X5ssFSlIOmzH5UyZVgckBkcGrkJrsJIeSnkLvcLBii1TA3XdtfjCFL7vzCMuskDr_X5LnWANHDR7_ZfyHh.mBl.FhS.qCu44p2J0Gy0DccM4NHa4tk2C0KiYxmHIGQmYEg6upsDn7SVnhzbmtZtPGBY7EbVFQ2iPk1iuVPQZTVrOR0DKYRwisHhSBivacAAbLlBj2jM',mdrd: 'TW7UgNncrRpJDfzzdbUpkN_6BTin7bQU5x9Q_FkDIXo-1792032479-1.2.1.1-ydyHbnKfqD8njTlXPm5qlP5qNCcpDBuA4hXySQIOyNex6HgMlhfVi5aaHmzL.34n5w7iuMutSZFQepMWH.3sOlUpLo3k23Z.oCC8jinYlQ6MnVVP_cyoJXxEN53CakdRXHNJPFXTQibujqD3p.V7gJ2fsPQy2rGAQn1ygA9MsagL_3wK1oRv91L_1sO3Buh8tnhPLaRSiEpOy6NbYk_XCjL22FV0h6vmmoo0fy.fW3s',};var a = document.createElement('script');a.nonce = 'Ce8ZIhPTr5Xb5Ifj7JiFWz';a.src = '/cdn-cgi/challenge-platform/h/g/orchestrate/chl_page/v1?ray=a4ab80937af3eff9';window._cf_chl_opt.cOgUHash = location.hash === '' && location.href.indexOf('#') !== -1 ? '#' : location.hash;window._cf_chl_opt.cOgUQuery = location.search === '' && location.href.slice(0, location.href.length - window._cf_chl_opt.cOgUHash.length).indexOf('?') !== -1 ? '?' : location.search;if (window.history && window.history.replaceState) {var ogU = location.pathname + window._cf_chl_opt.cOgUQuery + window._cf_chl_opt.cOgUHash;history.replaceState(null, null,"/articles/pesotan?__cf_chl_rt_tk=NmfNTFZj9mMNCvXS7xHoO4fEXwnXAmvjN.GxoL0tqZM-1792032479-1.0.1.1-KTJnT_VM8OyWfkh3vI9DcreDcwllg6DqiKTXH7zIFsQ"+ window._cf_chl_opt.cOgUHash);a.onload = function() {history.replaceState(null, null, ogU);}}document.getElementsByTagName('head')[0].appendChild(a);}());
```


## [2026-10-15T02:48:05.943Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py --help 2>&1 | head -15"
}
```


### [2026-10-15T02:48:06.476Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-10-15T02:48:14.937Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; \npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/آبستن' --note 'page 502, root Ten 1/Tenu: abestan etymology (MP ābustan < *āpuθra-)'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/تندر' --note 'page 502, root Ten 2: Persian tondar < PIr *tánHtā; Parthian tandur cognate'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/تنک' --note 'page 502, root Tenu: tonok < MP tanuk < *tanúkakah'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/تنکه' --note 'page 502, root Tenu: tonekeh = tonok + -e'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/تنیدن' --note 'page 502, root Ten 1: tanidan < MP tadan/tan- < PIE *ten-'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/antenna' --note 'page 502, root Ten 1: Latin antenna maybe < *antitempnā'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/tornado' --note 'page 502, root Ten 2: tornado < Sp. tronada < tonare'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/tennis' --note 'page 502, root Ten 1: tennis < OF tenez'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)tenh₂-' --note 'page 502, root Ten 2: PIE *(s)tenh2- to thunder'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ténh₂us' --note 'page 502, root Tenu: PIE *tenh2us thin'\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/temperature' --note 'page 502, root Ten 1: temperature < temperare (tempus?)'\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/astonish' --note 'page 502, root Ten 2: astonish < OF estoner < VL *extonare'\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/tone' --note 'page 502, root Tenu: tone < OF ton < L tonus < Gk tonos'\n"
}
```


### [2026-10-15T02:48:16.710Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/02d1cf0e24276467.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c8d33c0f34fe8573.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fd55177f33f8a313.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e597cec3df66ba3a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6c293e5058c7785c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9714aa9548c7f440.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d06e90878a6fcb3e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/aa819baf85271b89.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4e56d3a682d71b1e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/14e7bc4d3cb1a9f5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bcdbf0086321ac9b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/69e231f11ad18f9a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/74647dfbfd4cb554.txt
```


## [2026-10-15T02:48:19.173Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in bcdbf0086321ac9b 69e231f11ad18f9a 74647dfbfd4cb554; do wc -c $f.txt; grep -o -i \"temperature (n.).\\{0,400\\}\\|astonish (v.).\\{0,400\\}\\|tone (n.).\\{0,400\\}\" $f.txt | head -1; done"
}
```


### [2026-10-15T02:48:19.630Z] TOOL RESULT

```
138 bcdbf0086321ac9b.txt
135 69e231f11ad18f9a.txt
131 74647dfbfd4cb554.txt
```


## [2026-10-15T02:48:23.109Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; wc -c 02d1cf0e24276467.txt c8d33c0f34fe8573.txt fd55177f33f8a313.txt e597cec3df66ba3a.txt 6c293e5058c7785c.txt 9714aa9548c7f440.txt d06e90878a6fcb3e.txt aa819baf85271b89.txt 4e56d3a682d71b1e.txt 14e7bc4d3cb1a9f5.txt; cat bcdbf0086321ac9b.txt"
}
```


### [2026-10-15T02:48:23.588Z] TOOL RESULT

```
  4801 02d1cf0e24276467.txt
 14443 c8d33c0f34fe8573.txt
  4030 fd55177f33f8a313.txt
  3323 e597cec3df66ba3a.txt
  9597 6c293e5058c7785c.txt
 22835 9714aa9548c7f440.txt
 33877 d06e90878a6fcb3e.txt
 36441 aa819baf85271b89.txt
  6648 4e56d3a682d71b1e.txt
  8957 14e7bc4d3cb1a9f5.txt
144952 total
URL: https://www.etymonline.com/word/temperature
FETCHED: 2026-10-12T18:40:33Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
```


## [2026-10-15T02:48:28.741Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^tenus\\|^ten- \\|^ten-\\b\\|^tenu\\|^ton-\\|^stenō\\|^(s)ten\\|^sten-\\|^tnnus\\|^tṇnus\" IEC.txt | head; grep -n \"THUNDER\\|^12.64\\|THIN\\b\" SYN.txt | head -8; grep -n \"1\\. ten-\\|ten- „dehnen\\|ten- \\\"dehnen\\|tenu- „dünn\\|1\\. sten-\\|sten- „stöhnen\\|(s)ten-\" incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt | head"
}
```


### [2026-10-15T02:48:29.220Z] TOOL RESULT

```
17188:sten-agio ‘groan’. Cf. stend E stenos (2), ston- Gk. stenágo, id.; OE stenecian, id.
18350:ten- (1) “hither, here; thither, there'. Cf. te-, -tenos Tokh. B tane, tne “here, there’; Lat. cf. tenus “as far as’; quà-tenus, adv. “how far; so far”: Hes. cf. tënës ‘until; ON pinig ‘hither’; Li. teñ, tenai, tenais ‘there’; long-gde in Dor. tenei, id.
18351:ten- (2) radical: ‘stretch; spread; thin’. Cf. teneuos, tend (1), ton-, tnu- Long-gde in Skt. tànah, m. ‘fibre’; tanavam, n. ‘thinness’; Srb. tjena, f. ‘membrane’; Latv. tena, f. id.; Latv. cf. also tievs ((thin', cf. tnui-)
18352:ten- (3) ‘stiff, hard; harden, grip’. See tend (2)
18356:ten- — tenk-
18761:ton-, see tonos
692:Moon STAR LIGHTNING THUNDER
1746:1.56 THUNDER Grk. Boor Goth. peihwo Lith. perkiinas, griausmas NG Bpovr7 ON retdar, bruma Lett. pérkuons Lat. tonitrus Dan. torden ChSl. gromi It. tuono Sw. dska (tordén) SCr.  grom, grmljavina Fr, tonnerre OE = punor Boh. hrom Sp. trueno, tronido ME _ thunder Pol. — grzmot, grom, piorun Aunts tunet NE thunder Russ. grom De torainn Du. donder Skt. stanita- NIr. — tdirneach OHG donar Ay. Sater W. —taran MHG doner Br. kurun, kudurun, ta- NHG donner ran oe
1773:1.57 LIGHTNING (AS STRIKING), THUNDERBOLT
9844:cLOTHIN
10513:ING; PERSONAL ADORNMENT AND CARE 421 cLOTHIN™: 6.44 SHIRT ¢ Lith.  margkiniai ON serkr, skyrta 5 rm) Dak, skjorte Lett. krekls wi £5
11047:ING; PERSONAL ADORNMENT AND CARE 439 cLOTHIN™: 6.63 PIN : dalkr, nestt Lith. spilka by, FOP™M pa oN. naal Lett. kniepe “i trans P77) Sw. nal ¥ SCr. Gioda : us; fioula OE alc, préon Boh.  Spendltk illo ME preen, pynn Pol. szpilka ‘pingle NE pin Russ. bulavka Skt stici- [filer : Du. speld : a (cu gamalie) OHG = spinula f * delg, st! MHG  spenel, stecknolde bioran, dealg NHG _ stecknadel
22662:12.64 THICK? (In Density)
22696:12.65 THIN!
incoming/WLD/WLD_Bd2_pages.txt:1203:zu ten- „dehnen“ ; die Gleichsetzung mit acymr. edit, ncymr. eiddyl „tenuis“,
incoming/WLD/WLD_Bd2_pages.txt:41583:1. sten-, ten- von lauten Gerauschen;               „donnerD, rauschen, brausen, drohnen,
incoming/WLD/WLD_Bd2_pages.txt:43797:        *ten- „dehnen, spannen'* fiir „spinnen, flechten^'. {s)pen- spe(i)- „ziehen“  :
incoming/WLD/WLD_Bd1_pages.txt:68183:ten- „dehnen. ziehen, spannen" (z. T. auch von der Weberei, Spinnen, Netz,
incoming/WLD/WLD_Bd1_pages.txt:68224:Ton“ (wie              gr. x ovog;     wohl ohne Aufsaugung eines zur Schallwz. -(s)ten-
incoming/WLD/WLD_Bd1_pages.txt:68520:ware tenq- Wzerw. von ten- „dehnen“.
```


## [2026-10-15T02:48:33.639Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 41583,41600p incoming/WLD/WLD_Bd2_pages.txt | grep -n -i \"tund\\|np\\.\\|Page\\|^\\[pdf\" ; awk 'NR<41583 && /\\[pdf page/ {p=$0} END{}; NR==41583{print p}' incoming/WLD/WLD_Bd2_pages.txt; sed -n 68183,68200p incoming/WLD/WLD_Bd1_pages.txt | grep -n \"tanu\\|np\\.\\|tan\" ; awk 'NR<=68183 && /\\[pdf page/ {p=$0} NR==68183{print p}' incoming/WLD/WLD_Bd1_pages.txt; grep -n \"tenu-\\|tenus-\\|tanu-\" incoming/WLD/WLD_Bd1_pages.txt | sed -n 1,8p; sed -n 22696,22712p SYN.txt | cut -c1-600"
}
```


### [2026-10-15T02:48:34.196Z] TOOL RESULT

```
6:tosend“;  afghan. tana „Donner'‘, np. tundar ds.;

6: rarv-iiai ,       ravvco und das Adj. tpm-s „tenuis“), av. pairi-tanava 1 sg. Konj.                          .
10: Act. ,.ich will fernhalten", palri-tanuya 1. sg. Opt. Med.; ai. PPfP. ut-tana-h
13:                              = av. ustana- ds. (*tpid-n6                          -,   Set-Form,   vgl. ai. tani-man- n.
14: ,Dfinne“, auch                   lit.   fniti,      lat.       tcnc-re ,   z.    B. Persson Beitr. 648); np. tanldan
16: r7-Praesens (wie      lat. tcndo ) tandatc „laBt nach, ormattet" ( tundra „Mattig-

12.65 THIN!
(In Dimension) Grk.  dexrés Goth. Lith. plonas NG exrds, prevds ON = funnr Lett. tievs, plans lat. tenuis Dan. tynd ChSl. tiniiki It. _soltile (tenwe) Sw. tunn SCr.  tanak Fr, mince OE pynne Boh.  tenky 8p. delgado (tenue) ME thinne Pol. _—cienki Rum. subjire NE thin Russ. tonkij I, tana, séim Du. dun Skt.  fanu- Nir, tana OHG dunni Ay. W. — teneu MHG diinne Br. tano NHG  diinn
tievs; (Lith. dial. tenvas, Leskien, Bil- dung d. Nom. 344; Mithl.-Endz. 4.215 f); ChSl. tintiki, ete., general Slavic; Skt. tanu-; but Grk. ravaés ‘slender, long’, ravu- in epds. ‘long’.
2. Grk. derrés, lit. ‘peeled’ (of grains) hence ‘fine, thin’: \érw ‘peel, husk’, Néros ‘rind, husk’, etc. Walde-P. 2.424. Boisacq 569.
Byz. mrevés (Const. Porph.), NG pop. grevos, perh. fr. wrnvés ‘flying, winged’ (Eust. 855.42, Koraes, “Araxra 1.123), despite the difficulty in form (€ fr. mrepov?) and sense (‘thin’ as what easily flies?).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
890 SELECTED INDO-EUROPEAN SYNONYMS
3. It. sottile, Rum. subtire fr. Lat. sub- filis ‘fine, delicate’ (of thread, Lucr.), prob. orig. a weavers’ term ‘finely wov- en’ with the last part related to déla ‘web, loom’, terere ‘weave’. Ernout-M. 995. REW 8399.
Fr. mince, deriv. of OFr. mincier ‘make small’ fr. VLat. *mindtiare, fr. minitia ‘particle, trifle’. REW 5598.
Sp. delgado, fr. Lat. delicatus ‘charm- ing, tender, delicate’. REW 2538.
4, Ir. séim ‘thin, slender’, of liquor
‘mild, thin’, perh. fr. *spei-mi- - Grk omt-vos ‘lean’, fr. the root *spéi- in Grk. ora ‘draw out, pull, pluck out’, OHG spannan ‘stretch, span’, etc. Walde-P. 2.656. Stokes 295.
5. Lith. plonas, Lett. plans, the latter also ‘flat? and ‘weak’ : Lat, planus ‘flat’, etc. (12.71), with meanings ‘flat? and ‘thin’ fr. ‘spread out’, common to the large group of cognates, Walde-P, 2.61. Miihl.-Endz. 3.330.
12.66 THIN? (In Density)
Grk. pavés, dpatds Goth. Lith.  retas, ‘skystas NG = dpatés, dvaptos ON = punnr Lett. ets, 3k’idrs Lat.  rdrus Dan. tynd ChSl.  rédiikit It. rado, non fiito Sw. tunn, gles SCr. rijedak Fr. rare, clair, clairsemé OE pynne Boh. fidky Sp. ralo, claro ME _ thinne Pol. = rzadki Rum. rar NE thin Russ. redkij, Zidkij Ir. tana Du. dun Skt. virala- Nir. tana OHG dunni Av. W. teneu MHG dtinne Br. tano NHG diinn
‘Thin’ in density is expressed by the old words for ‘thin’ in dimension in Celt- ic and Germanic, but elsewhere mostly by different words based on such notions as ‘clear, bright’ (what one can see through, hence ‘thin’) or ‘loose, sepa- rated’. Many of these come to be used also or mostly for ‘rare, scarce’.
```


## [2026-10-15T02:48:39.575Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} {n=split($0,a,\"\\n\"); c+=n-1; if(!f && c>=41583){print \"Bd2 leaf\",NR; f=1}}' WLD_Bd2_pages.txt; awk 'BEGIN{RS=\"\\f\"} {n=split($0,a,\"\\n\"); c+=n-1; if(!f && c>=68183){print \"Bd1 leaf\",NR; f=1}}' WLD_Bd1_pages.txt; grep -n \"\\[pdf page\" WLD_Bd2_pages.txt | head -2"
}
```


### [2026-10-15T02:48:40.277Z] TOOL RESULT

```
Bd2 leaf 631
Bd1 leaf 731
```


## [2026-10-15T02:48:45.015Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"تنکه\\|تُنُکه\\|تنكه\" MON_part1.txt MON_part2.txt | head -5; grep -n \"تُن\\b\\|تن (فر\\|ton\\b\" MON_part1.txt | head -5; grep -n \"^تندر\\|تُندُر\\|تندر\" incoming/ARY/ARY_pages.txt | head -5; grep -n \"TONDAR\\|TONOK\\|TAN\\b\\|ABESTAN\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-15T02:48:45.383Z] TOOL RESULT

```
MON_part1.txt:19587:(جف.) تنکه میان دو خشکی. تمام» به تمام) 
MON_part1.txt:28179:فوق و تحت و میان هر دو تنکهٌ افقی بکار 
MON_part1.txt:44296:تنکه: (۵-)۱0۱۵۲۸ (.) تنان چرمی که تا سر 
MON_part1.txt:44301:تنکه: (۵-)0۲۵ه) [آهنن سشبد] (.) قر ص 
MON_part1.txt:44615:تنکه. شلوار کو تاه کشت یگیران. 
1356:APE (OLD PRUSSIAN) AS 3. ‘AP, APAM AVESTAN) gles)
1366:_ ATER ATARSH —(AVESTAN) gus)
1382:» UGNUS * (LATVIAN) (33) 93) ATHRAVAN, ADAR, :(AVESTAN) gl!
1397:RATAN ARADH, -RADH —«(AVESTAN) pl 3\
1398:RATEN H(GERMAN) aT ARASTAN (PAHLAVI) 5 shy
1423:RIM ENGLISH) (1\2) gulSib RAMYEITI, RAMAN,(AVESTAN) gl)
1425:RAMTIS, RIMTI, :(LITHUANIAN) gl) ARAMITAN, PAHLAVD ($3,
1426:RAMDITI RAMISHN, RAM, RAMENITAN
1451:LAK- ARETHNA A AVESTAN) leu 9)
1482:AULYS (LITHUANIAN) gy.) HANUHARENA —{AVESTAN) gs)
```


## [2026-10-15T02:48:47.786Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 44294,44303p MON_part1.txt; sed -n 44613,44616p MON_part1.txt; grep -n \"TANU\\b\\|TANU,\\|TUNDAR\\|TONDAR\\|TANDUR\" incoming/ARY/ARY_latin_index_pages.txt | head -5"
}
```


### [2026-10-15T02:48:48.266Z] TOOL RESULT

```
ج. تتکرات. 

تنکه: (۵-)۱0۱۵۲۸ (.) تنان چرمی که تا سر 
زانو باشد و کشتی‌گیران وقت کشتی گرفتن 
بوشند. شلوار کو تاه زنانه. زیر شلواری کو تاه 
مر دانه. 

تنکه: (۵-)0۲۵ه) [آهنن سشبد] (.) قر ص 
رایج از زر و سیم و مس. 

تئنبه توام. دو همزاد. دو همراه» دو قر بن. 
توبان: مت [- تتبان ‏ تمان] (.) شلوار. 
تنکه. شلوار کو تاه کشت یگیران. 

5767:BUCK: 198-199| ©  TANU SANSKRIT) ep Sail
13393:‘TANU., (TANU-TER) MANIYA — (OLD PERSIAN) dul gos),
```


## [2026-10-15T02:48:50.491Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /TANU SANSKRIT/ {print \"leaf\",NR-1; print substr($0,1,1500)}' incoming/ARY/ARY_latin_index_pages.txt | head -40"
}
```


### [2026-10-15T02:48:50.941Z] TOOL RESULT

```
leaf 199
[pdf page 200]
Wh ge ‘
[Ra PERSLAN et |

: TAND AVESTAN) gle 3\

j REFERENCES Benth TAN PAHLAVI) «53h
POKORNY SOS*~*~*~*~*~«SCD DGAN ARURDISH) 53,5
MACKENZIE: (BODY) 104 TAN AFGHAND) (4) it
BUCK: 198-199| ©  TANU SANSKRIT) ep Sail
AMINDAROV: (BODY) 192 TEINO (GREEK) gli,
or} rgb iby

Jeeta
sce ayy gaat 5 pa SE gu fly “A
ASE y Ti
Slat ely gal hI en" 298 oF "ota ate a tl olan jly of
(sch ou pid ans g"Gasmas gh p94) ge Gane PERSIAN) ya dlb
TANJIDAN
CONTORT, COMPRESS ng gld 50 3Iy a1 gual ie
AVESTAN) gies!
‘REFERENCES ecethag ‘TASHYAH., TANCHISHTA
POKORNY ——=S*«~S*«w BND TINJIN, ITINJUN —(OSSETIC) zo)
ow ebb oby TAJENAG © ABALUCHI) gz sh
TANI, TANC: (SANSKRIT) cy Sail
seatloay #°°%
the ae ojNy 395 a)
STANATI, (SANSKRIT) 2 Soil AFGHAN) (4) silts)
STANITI, TANYATI, TANAYITU ‘TTANDAR, TANA, TALANDA
```


## [2026-10-15T02:49:12.617Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^تن: \\|^تن :\\|^تن(\\|^تُن\" MON_part1.txt | head; grep -n \"^تنک: \\|^تنک:\" MON_part1.txt | head -3"
}
```


### [2026-10-15T02:49:12.981Z] TOOL RESULT

```
36900:تن : 
43759:تن: ۱20 (افا.) در بعضی کلمات م رکب به 
43762:تن: ۱20 (پس. مصدری) یکی از علامات 
43767:تن: ۱0۰ (1.) مقباس وزن که آن را معمولا با 
43772:تن: «۱0 (.) درجة بلندی و پستی صدا و
```


## [2026-10-15T02:49:14.752Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 43772,43776p MON_part1.txt; grep -n \"^تنک\" MON_part1.txt | head -4"
}
```


### [2026-10-15T02:49:15.133Z] TOOL RESULT

```
تن: «۱0 (.) درجة بلندی و پستی صدا و 
آواز؛ مابه. 

تن آسان: 0 [- تناسان] (حامص.) 
آسوده» مرفه. تندرست» سالم. . تن بروره 
41645:تنکک گر فتن. . خللاف ورزیدن) ج. تعسیرات. 
44286:تنکبیز: ۱۵۱۵-2 [- تنکک‌سزنده] (ص‌فا. 
44296:تنکه: (۵-)۱0۱۵۲۸ (.) تنان چرمی که تا سر 
44301:تنکه: (۵-)0۲۵ه) [آهنن سشبد] (.) قر ص
```


## [2026-10-15T02:52:32.757Z] TOOL CALL #57: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-502.json",
 "content": "{\n  \"pdf_page\": 502,\n  \"book_page\": 472,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-10-14\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ten 1, Tengh, Temp\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ten- (*tenh₂-) 'to stretch' (Pokorny 1. ten-, tend- 1065-1066), with extensions *temp- (1064-1065) and *tengh- (1067); adjective *ténh₂us 'thin' (Pokorny tenu-s 1069)\",\n      \"note\": \"Root, label and gloss are correct: Pokorny heads 'ten-1, tend-' 'to extend, stretch, span' (pp.1065-1066), and lists temp- 'to extend, stretch, span. Note: extension from *ten-' (1064-1065) and tengh- 'yet probably nevertheless extension from ten-1' (1067); Nourai's POK:1064,1067 point to those two extensions. Watkins (AHD) ten- 'To stretch' covers tendere, tenere, tonos, Germanic *thunw- 'thin'. Problems are local: (1) 'ana-tempa' is not attested Latin but Klein's/Pokorny's tentative reconstruction *an(a)-temp-na behind Latin antemna/antenna, whose origin Ernout-Meillet consider unknown (probably a loan); (2) temperature belongs to temperare, connected with *temp- only tentatively; (3) the Persian box hangs tanīdan 'to spin' (a verb from *ten- itself, Cheung *tan-) under Avestan tanū- 'body', and âbestan's analysis as *ā-puθra-tanu- (Nyberg, Hübschmann) is not the one Wiktionary gives (*āpuθra-); (4) Persian tonok is inherited (MP tanuk), a cognate of Sanskrit tanuka-, not a derivative of it. No extraction errors: the JSON matches the printed page (checked against the page image).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ten- (*tenh₂-) «کشیدن، گستردن» است و پوکورنی (ص۱۰۶۵–۱۰۶۶) آن را با همین معنا آورده و temp- (ص۱۰۶۴) و tengh- (ص۱۰۶۷) را گسترش‌یافتهٔ همان ریشه می‌داند؛ صفت *ténh₂us «نازک» (پوکورنی ۱۰۶۹) نیز از همین ریشه است. پس ریشه، برچسب و معنای نورایی درست است. اشکال‌ها جزئی‌اند: «ana-tempa» واژهٔ لاتین گواهی‌شده نیست بلکه بازسازی گمانیِ کلاین و پوکورنی برای antemna (دکل بادبان) است؛ «تنیدن» فعلی مستقیم از ریشهٔ *tan- است نه از «تن»؛ و «تُنُک» هم‌ریشهٔ سنسکریت tanuka- است نه برگرفته از آن. خطای استخراج دیده نشد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ténh₂us\",\n        \"https://en.wiktionary.org/wiki/antenna\",\n        \"https://en.wiktionary.org/wiki/تنیدن\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1064\", \"status\": \"supports\", \"note\": \"POK_full.txt line 85453 'Root / lemma: temp-' 'Meaning: to extend, stretch, span' 'Note: extension from *ten- ds.'; includes 'Latin tempus ... temperare' and 'perhaps antemna f. \\\"sprit\\\" (\\\"die Aufgespannte\\\") from *an(a)-temp-na'; Page(s): 1064-1065.\"},\n        {\"ref\": \"POK:1067\", \"status\": \"supports\", \"note\": \"POK_full.txt line 85516 'Root / lemma: tengh-' 'Meaning: to extend, stretch, span' 'Note: ... probably nevertheless extension from ten-1'; Page(s): 1067. Same page has 'tend-: see below tem-1'. The main root '1. ten-, tend-' is on pp.1065-1066 (line 85648).\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ten- (line 1079)\", \"stance\": \"supports\", \"note\": \"'ten-. To stretch. ... Latin tendere ... TENT1 ... Latin tenere, to hold, keep ... CONTAIN ... II. Derivatives meaning \\\"stretched,\\\" hence \\\"thin.\\\" 1. ... *tn-u- in Germanic *thunw- ... THIN ... III. ... *ton-o- in Greek tonos, string, hence sound, pitch: TONE. [Pok. 1. ten- 1065.]'\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I p.722 (WLD_Bd1_pages.txt leaf 731)\", \"stance\": \"supports\", \"note\": \"'ten- „dehnen, ziehen, spannen“ (z. T. auch von der Weberei, Spinnen ...)' with 'av. pairi-tanava', 'np. tanīdan', 'lat. tene-re'.\"},\n        {\"src\": \"IEC\", \"where\": \"line 18351 s.v. ten- (2)\", \"stance\": \"supports\", \"note\": \"'ten- (2) radical: ‘stretch; spread; thin’. Cf. teneuos, tend (1), ton-, tnu-'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Latin\",\n          \"words\": \"tendere; tenere; ana-tempa\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin tendere 'to stretch' continues an o-grade-less *ten-d- present (Pokorny 'Latin tendo ... originally d-present'), and tenēre 'to hold' the stative *ten-ē- ('to cause to endure, hold on to', Watkins) — both confirmed. 'ana-tempa' is not a Latin word: the attested word is antemna/antenna 'sail-yard', which Klein and Pokorny tentatively analyse as *an(a)-temp-na 'the stretched-up (yard)' from *temp-, with *-mpn- > -mn-; Wiktionary repeats this as 'may be from Proto-Italic *antitempnā', while Ernout-Meillet regard antemna as an unexplained (probably borrowed) nautical term. Nourai has dropped both the asterisk and the -n- of the reconstruction.\",\n          \"derivation_fa\": \"لاتین tendere «کشیدن» و tenēre «نگه داشتن» هر دو از ریشهٔ *ten- «کشیدن»اند و این بخش درست است. اما «ana-tempa» واژهٔ لاتین نیست: واژهٔ گواهی‌شده antemna/antenna «چوب افقی بادبان» است که کلاین و پوکورنی آن را با تردید از *an(a)-temp-na «آنچه بالا کشیده شده» از ریشهٔ گسترش‌یافتهٔ *temp- دانسته‌اند؛ ارنو و میه آن را وام‌واژه‌ای دریانوردی با ریشهٔ نامعلوم می‌شمارند. نورایی ستارهٔ بازسازی و -n- آن را انداخته است؛ پس این خانه با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/antenna\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins s.v. ten-: 'Latin tendere, to stretch, extend' and 'Latin tenere, to hold, keep, maintain' — supported; antenna is not listed under ten- or temp- (temp- gives only tempus 'temple' and Persian taftan).\"},\n            {\"ref\": \"POK\", \"status\": \"supports\", \"note\": \"POK_full.txt temp- (pp.1064-1065): 'perhaps antemna f. \\\"sprit\\\" (\\\"die Aufgespannte\\\") from *an(a)-temp-na'; ten- (1065-1066): 'Latin tendo, -ere ... teneo, -ere'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1971.txt line 16099 s.v. antenna\", \"stance\": \"supports\", \"note\": \"'fr. L. antemna, antenna, ‘sail yard’, which is of uncertain origin. It is perh. a contraction of *an(a)tempna, ‘that which is stretched, extended’, fr. I.-E. base *temp-'.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. antenna (line 4199)\", \"stance\": \"contradicts\", \"note\": \"'antenna, -ae f. ... vergue(s) ... Mot sans doute emprunt, comme la plupart des termes nautiques du latin.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.722\", \"stance\": \"supports\", \"note\": \"'ten- „dehnen, ziehen, spannen“' with 'lat. tene-re'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pass-through French box: French antenne (from Latin antenna, in the 'aerial' sense from the 1900s after the insect 'feeler' sense) and tennis (English game name built on Old/Anglo-French tenez 'hold!', imperative of tenir < Latin tenēre, re-borrowed into French as tennis in the 19th c.) are the forms Persian took over.\",\n          \"derivation_fa\": \"خانهٔ فرانسوی خالی است و فقط گذرگاه است: فرانسوی antenne (از لاتین antenna) و tennis (از تعبیر tenez «بگیر!»، امرِ tenir از لاتین tenēre، که از راه انگلیسی دوباره به فرانسه بازگشت) واژه‌هایی‌اند که فارسی وام گرفته است. این مسیر درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/tennis\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1587\", \"status\": \"supports\", \"note\": \"Klein 1966 (KLN_1966.txt line 38548) s.v. tennis, on the cited page range: 'ME. teneis, fr. AF. tenetz, fr. OF. (= F.) tenez, ‘hold!’, pl. imper. of tenir, ‘to hold’ ... so called from the word used by the server'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1971.txt line 16099 s.v. antenna\", \"stance\": \"supports\", \"note\": \"'antenna ... fr. L. antemna, antenna, ‘sail yard’'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt (grep 'Tennis', 'Antenna')\", \"stance\": \"silent\", \"note\": \"No separate entries found in the OCR.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"ânten; tenîs\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian ânten آنتن 'aerial' is a 20th-century loan of French antenne (Latin antenna 'sail-yard'); the gloss 'stretched out (sail)' is Nourai's etymological gloss of the Latin, not a Persian meaning. tenis تنیس is the game name borrowed (via French tennis / English tennis) in the Pahlavi era, ultimately from Anglo-French tenetz 'hold!' < tenir < Latin tenēre.\",\n          \"derivation_fa\": \"«آنتن» وام‌واژهٔ سدهٔ بیستمی از فرانسوی antenne است که خود از لاتین antenna «چوب بادبان» آمده؛ معنای «(بادبانِ) کشیده‌شده» توضیح ریشه‌شناختی نورایی است نه معنای فارسی. «تنیس» نام بازی است که از فرانسوی/انگلیسی tennis وام گرفته شده و آن از tenez «بگیر!» از فعل tenir (لاتین tenēre «نگه داشتن») است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/tennis\", \"https://en.wiktionary.org/wiki/antenna\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The Persian box carries no reference of its own; the French parent cites KLN:1587 (tennis), which supports the Romance chain.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt (grep آنتن / تنیس)\", \"stance\": \"silent\", \"note\": \"The 2-vol Mo'in abridgement OCR gave no clean hit for either loanword.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 38548 s.v. tennis\", \"stance\": \"supports\", \"note\": \"'fr. OF. (= F.) tenez, ‘hold!’, pl. imper. of tenir'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"tent, contain, tennis, antenna, temperature, tension\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"tent < Old French tente < Late Latin tenta 'stretched (cloth)', pp. of tendere; contain < Old French contenir < Latin continēre (con- + tenēre); tennis < Anglo-French tenetz 'hold!' (tenir < tenēre); tension < Latin tensio < tendere — all secure (Watkins lists TENT, CONTAIN, TENSE under ten-). antenna < Latin antemna (only tentatively *an(a)-temp-na, see #1). temperature < Latin temperātūra < temperāre 'to mix in due measure', which Pokorny attaches to tempus 'stretch of time' < *temp- with a 'perhaps', and Watkins does not list under ten-/temp-; so the last two are only plausible.\",\n          \"derivation_fa\": \"tent (چادر، از لاتین tenta «کشیده‌شده» از tendere)، contain (از continēre)، tennis (از tenir/tenēre) و tension (از tendere) بی‌گمان از ریشهٔ *ten- «کشیدن»اند. اما antenna تنها به گمان از *temp- است (ر.ک. خانهٔ ۱) و temperature از temperāre «به‌اندازه آمیختن» است که پیوندش با tempus و *temp- «کشیدن» را پوکورنی با «شاید» آورده است؛ پس این خانه در مجموع پذیرفتنی ولی نه قطعی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/tennis\", \"https://en.wiktionary.org/wiki/antenna\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed on this box; checked against AHD/Klein instead (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. ten-\", \"stance\": \"partial\", \"note\": \"'Latin tendere ... TENSE1, TENT1 ... Latin tenere ... CONTAIN' — tent, contain, tension supported; antenna and temperature not listed under ten- or temp-.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 38494 s.v. temperature\", \"stance\": \"partial\", \"note\": \"'L. temperātūra, ‘due measure, proportion ...’, fr. temperātus, pp. of temperāre. See temperate' — no direct link to *ten-.\"},\n            {\"src\": \"POK\", \"where\": \"temp- pp.1064-1065\", \"stance\": \"partial\", \"note\": \"'Latin tempus \\\"Zeitspanne\\\", in addition temperare \\\"measure halten\\\" ... perhaps antemna'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Indo-European\",\n          \"words\": \"Tenu\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"PIE *ténh₂-u-s 'thin' (Pokorny tenu-s 1069, 'to ten-1 \\\"dehnen\\\"'), a u-adjective of *tenh₂- 'stretch': literally 'stretched out', hence 'thin'. Reflexes: Sanskrit tanú-, Latin tenuis, Old English þynne, Old Church Slavonic tĭnŭkŭ.\",\n          \"derivation_fa\": \"هندواروپایی آغازین *ténh₂us «نازک» صفتی با پسوند -u از ریشهٔ *tenh₂- «کشیدن» است، یعنی «کشیده‌شده»، و از آن سنسکریت tanú-، لاتین tenuis، انگلیسی thin و اسلاوی کهن tĭnŭkŭ آمده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ténh₂us\"],\n          \"ref_check\": [\n            {\"ref\": \"POK\", \"status\": \"supports\", \"note\": \"POK_full.txt line 85789 'Root / lemma: tenu-s' 'Meaning: thin' 'Note: to ten-1 \\\"dehnen\\\"' ... 'Page(s): 1069'.\"},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. ten- II: 'Derivatives meaning \\\"stretched,\\\" hence \\\"thin.\\\" 1. ... *tn-u- in Germanic *thunw- ... 2. ... *ten-u- in Latin tenuis'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SYN\", \"where\": \"12.65 THIN (line 22696)\", \"stance\": \"supports\", \"note\": \"Buck: 'Lat. tenuis ... OE þynne ... Skt. tanu-' — 'Skt. tanu-; but Grk. ταναός ‘slender, long’'.\"},\n            {\"src\": \"IEC\", \"where\": \"line 18351 ten- (2)\", \"stance\": \"supports\", \"note\": \"'stretch; spread; thin'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.722 ff.\", \"stance\": \"supports\", \"note\": \"ten- entry with 'das Adj. tenu-s „tenuis“'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Avestan\",\n          \"words\": \"tanu; a-puthra-tanu; taxma-tanu; pešô-tanu\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan tanū- f. 'body, person, self' is real (Bartholomae col. 634 'Leib'); Pokorny lists it both as 'substantivized' tanū- under tenu-s 1069 and as 'perhaps here tanū- \\\"body\\\"' under ten- (after Mayrhofer), so the 'stretched' body is an accepted but uncertain etymology. pəšō.tanu- 'whose body is forfeit, liable to punishment' is attested (Bartholomae col. c.897 'des Leib verwirkt, dem Gericht verfallen ist'). taxma- 'brave, strong' is attested (Bartholomae), but a compound *taxma-tanu- is not; it is the reconstructed source of NP tahamtan. 'a-puthra-tanu' is not attested: Avestan a-puθra- would mean 'sonless'; Nyberg reconstructs OP *ā-puça-tanu- 'having a son in the body' for MP ābustan, so the hyphenated form is a misleading reconstruction.\",\n          \"derivation_fa\": \"اوستایی tanū- «تن، پیکر، خود» گواهی شده است (بارتولومه، ستون ۶۳۴) و پیوندش با *ten- «کشیدن» را پوکورنی و مایرهوفر با احتیاط پذیرفته‌اند. pəšō.tanu- «کسی که تنش (به سبب گناه) در گرو است» نیز در اوستا هست. اما taxma-tanu «تهمتن» ترکیبی بازسازی‌شده است و در اوستا نیامده، و «a-puthra-tanu» هم گواهی نشده است؛ نیبرگ برای آبستن صورت پارسی باستان *ā-puça-tanu- «پسر در تن دارنده» را بازسازی می‌کند، حال آنکه a-puθra- در اوستایی «بی‌پسر» معنی می‌دهد. پس این خانه پذیرفتنی است ولی دو صورتش بازسازی است نه واژهٔ اوستایی.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/آبستن\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1069\", \"status\": \"supports\", \"note\": \"POK_full.txt tenu-s (p.1069): 'substantivized Old Indie tanū- f., tanūs- n., Avestan tanū- f., tanus- n., np. tan \\\"body\\\"'.\"},\n            {\"ref\": \"BQT:411\", \"status\": \"not_found\", \"note\": \"BQT_v1_pages.txt leaves 636-637 (≈ pp.410-411, entries پشکم ... پشول): no headword پشوتن in the OCR; the neighbouring entries are there, so the name is apparently not a Borhan headword.\"},\n            {\"ref\": \"BQT:515\", \"status\": \"partial\", \"note\": \"BQT_v1_pages.txt leaf 752 (≈ p.515-524 region): headword 'تن - معروف است ... و بمعنی اجسام نیز آمده است' with footnote '۷ - پهلوی' — confirms tan but the OCR footnote does not show the Avestan form.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 634 s.v. tanū- (BRT.txt line 11941); col. c.897 s.v. pəšō.tanu- (line 16186); s.v. taxma- (line 11841)\", \"stance\": \"partial\", \"note\": \"'tanū- f. ... „Leib“ 1) der Menschen ... auch sva. „Person“'; 'pəšō.tanū- Adj. „des Leib verwirkt, dem Gericht verfallen ist“'; 'taxma- Adj. „fortis, tapfer, tüchtig“' — no compound taxma.tanu- or a-puθra-tanu-.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. āpustan (line 611)\", \"stance\": \"partial\", \"note\": \"'āpustan [ʾpwstn'] pregnant ... — < OP *ā-puça-tanu-, SW form of' — Nyberg's OP reconstruction, not an Avestan word.\"},\n            {\"src\": \"KNT\", \"where\": \"KNT_full.txt (grep taxma)\", \"stance\": \"silent\", \"note\": \"Old Persian taxma- appears only in the name Taxmaspāda-; no tanu compound.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"tanîdan; tan; âbestan; Tahamtan; Pašŭtan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"tan تن 'body' < MP tan < Av./OIr. tanū- — confirmed (Horn no. 393). tanīdan تنیدن 'to spin, weave' < MP tadan, pres. tan- 'to spin (thread)' < PIr. *tan- 'to stretch' (Cheung) < PIE *ten-: right root, but it is a verb from the root, not a derivative of Avestan tanū- 'body' as the arrow implies. âbestan آبستن 'pregnant' < MP ābus/ābustan [ʾpwstn']; Nyberg derives it from OP *ā-puça-tanu- 'with a son in the body' and Hübschmann notes it was felt as a compound with tan, but Wiktionary gives *āpuθra- 'pregnant' (< *puθra- 'son') without tanu, so the tan element is disputed. Tahamtan تهمتن, Rostam's epithet, = tahm/taham 'strong' (MP tahm < Av. taxma-) + tan 'body' — confirmed by Hübschmann. Pašūtan پشوتن (Pahlavi Pišyōtan), son of Goštāsp, is generally analysed as Av. pəšō.tanu- 'whose body is forfeit' (here as an epithet of the immortal); the Qāʾānī verse quoted on the page names Zāl, Tahamtan, Esfandiyār and Pašūtan.\",\n          \"derivation_fa\": \"«تن» از فارسی میانهٔ tan و اوستایی tanū- است و درست است. «تنیدن» از فارسی میانهٔ tadan/tan- «رشتن» و ایرانی باستان *tan- «کشیدن» (چونگ) است؛ ریشه یکی است ولی این فعل مستقیماً از ریشه آمده نه از «تن». «آبستن» از فارسی میانهٔ ābus/ābustan است؛ نیبرگ آن را از پارسی باستان *ā-puça-tanu- «پسر در تن» و هوبشمان آن را ترکیبی با «تن» دانسته‌اند، ولی ویکی‌واژه آن را از *āpuθra- «باردار» (از *puθra- «پسر») و بی‌جزء «تن» می‌داند. «تهمتن» لقب رستم از «تهم» (اوستایی taxma- «دلیر، نیرومند») + «تن» است و درست است. «پشوتن» (پهلوی Pišyōtan) پسر گشتاسپ را معمولاً با اوستایی pəšō.tanu- یکی می‌دانند. در مجموع با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/تنیدن\", \"https://en.wiktionary.org/wiki/آبستن\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:88\", \"status\": \"supports\", \"note\": \"Horn p.88 no. 393 (HRN.txt leaf ~109): 'ten „Körper, Leib“ ... aw. tanū- „Körper, Leib“; phlv. tan; ai. tanū-'; p.89 no. 399 'tenīden „drehen, spinnen“ ... aw. √tan-; ai. √tan-, tanoti „dehnen, spannen“' (Horn keeps the verb under the root, not under tanū-).\"},\n            {\"ref\": \"BQT:524\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 752: 'تنیدن بر وزن رمیدن، معروف' with Mo'in's footnote '٩ - از اوستا [tan] ؛ پهلوی ...' (Latin letters lost in OCR).\"},\n            {\"ref\": \"VSF:16\", \"status\": \"not_checked\", \"note\": \"VSF not identified / no copy available (refs_online.json: 'Not found').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"HUB.txt lines 6668-6672 and 8993\", \"stance\": \"supports\", \"note\": \"'-tan als 2. Glied von Komp. ... die noch als Komp. mit tan (vgl. xᵛēštan „selbst“, ābistan „schwanger“) gefühlt wurden'; 'tahm — taham „stark“ (auch in Tahamtan „von starkem Körper“, Rustem's Beiname) zd. taxma-'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *tan 'to extend, stretch' (CHEUNG.txt line 24582)\", \"stance\": \"partial\", \"note\": \"'MIDDLE PERSIAN: BMP tn- /tan-/, (pret. stem) tt- /tad-/ ‘to spin (thread)’ ... NP tanidan/tan- ‘to turn, spin’ ... PIE *ten- ‘to draw, stretch’' — the verb is from the root, not from tanū-.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt lines 833, 4876, 4900\", \"stance\": \"supports\", \"note\": \"'ābus, -tan [ʾpws, -tn' | M ʾbwws, v. ābestan] pregnant'; 'tadan, tan- [ttn', tn- | N tan-] spin (thread)'; 'tan [tn' | = M, N ~] body, person'.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. tan (line 3711), āpustan (611)\", \"stance\": \"supports\", \"note\": \"'tan [tn'] body ... — Av. tanū-'; 'āpustan ... < OP *ā-puça-tanu-'.\"},\n            {\"src\": \"ARY\", \"where\": \"pdf page 200 (printed 201), Latin index\", \"stance\": \"supports\", \"note\": \"تن entry: 'TANŪ (AVESTAN) ... TAN (PAHLAVI) ... TANU (SANSKRIT) ... TEINŌ (GREEK)', refs Pokorny, MacKenzie 'tan (body) 104', Buck 198-199.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"tanuka\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit tanuka- 'thin, small' is the -ka- extension of tanú- 'thin' < PIE *tn̥h₂-ú- / *tn̥h₂-u-kos (Wiktionary *tn̥h₂ukos ~ ténh₂ukos, the same formation as Old Church Slavonic tĭnŭkŭ). Pokorny 1069 cites 'tanuka- ds. = Slavic tĭnŭkŭ'.\",\n          \"derivation_fa\": \"سنسکریت tanuka- «نازک، کوچک» گونهٔ پسونددار tanú- «نازک» است و به هندواروپایی *tn̥h₂u-kos بازمی‌گردد، همان ساختی که در اسلاوی کهن tĭnŭkŭ هست. پوکورنی (ص۱۰۶۹) آن را آورده است؛ ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ténh₂us\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1069\", \"status\": \"supports\", \"note\": \"POK_full.txt tenu-s: 'Old Indie tanu-, fem. tanvī \\\"thin, tender, fragile, flimsy, insignificant\\\" (tanuka- ds. = Slavic tĭnŭkŭ)'; Page(s): 1069.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 39038 s.v. thin\", \"stance\": \"supports\", \"note\": \"'whence also OI. tanuh (fem. tanvi), tanukah, ‘thin, tender’, lit. ‘stretched out’'.\"},\n            {\"src\": \"SYN\", \"where\": \"12.65 THIN\", \"stance\": \"supports\", \"note\": \"'Skt. tanu-'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"tonok; tonekeh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"tonok تُنُک 'thin, sparse' < MP tanuk [tnwk'] 'thin, shallow' < PIr. *tanuka- (Wiktionary *tanúkakah) < PIE *tn̥h₂u-kos; it is inherited, a cognate of Sanskrit tanuka-, not derived from it as the arrow suggests (the vowel u of the first syllable is a later NP assimilation tanuk > tunuk). tonekeh تنکه 'wrestler's shorts, short drawers' is tonok + -e (Wiktionary), i.e. a garment of thin cloth; the chart's NOTE pointing to root 'Kitu' (Semitic kittān 'linen' / Greek chitōn) is not supported by any source consulted. (A homonymous تنکه 'coin' in Mo'in is Turkic tanga/tenge, unrelated.)\",\n          \"derivation_fa\": \"«تُنُک» از فارسی میانهٔ tanuk «نازک، کم‌عمق» و ایرانی باستان *tanuka- است؛ یعنی واژه‌ای موروثی و هم‌ریشهٔ سنسکریت tanuka- است، نه برگرفته از سنسکریت (فلش نورایی را باید به معنای هم‌ریشگی گرفت). «تُنُکه» (شلوارک کشتی‌گیران، زیرپوش) از «تنک» + «ـه» است، یعنی جامه‌ای از پارچهٔ نازک؛ پیوند احتمالی آن با ریشهٔ «Kitu» (کتان/خیتون) که در یادداشت کتاب آمده در منابع امروزی تأیید نمی‌شود. در مجموع پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/تنک\", \"https://en.wiktionary.org/wiki/تنکه\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:89\", \"status\": \"supports\", \"note\": \"Horn p.89 no. 397: 'tenuk „dünn, zart, fein“. ai. tanu-, tánuka- „dünn, fein“; kurd. tenik; oss. ...; bal. tanak'.\"},\n            {\"ref\": \"BQT:519\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 747, Mo'in's footnote: 'بضم اول و دوم، هندی باستان [tanu], [tanuka] (نازک، لطیف)، کردی ... بلوچی ... «اسشق ۳۹۷»؛ طبری ... (روان، ضد غلیظ)'.\"},\n            {\"ref\": \"MON:1154\", \"status\": \"partial\", \"note\": \"Only the 2-vol abridgement is on disk (MON_part1.txt line 44296): 'تنکه: ... تنبان چرمی که تا سر زانو باشد و کشتی‌گیران وقت کشتی گرفتن پوشند. شلوار کوتاه زنانه. زیرشلواری کوتاه مردانه' — meaning confirmed; page 1154 of the 6-vol edition cannot be mapped.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 4920\", \"stance\": \"supports\", \"note\": \"'tanuk [tnwk' | N ~] thin, shallow.'\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary line 3725\", \"stance\": \"supports\", \"note\": \"'tanūk [tnwk'] scarce, rare — NP tanuk ‘slender, thin’; Skr tanu-, Lat tenuis.'\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt (grep tunuk)\", \"stance\": \"silent\", \"note\": \"No remark on Horn no. 397.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Greek\",\n          \"words\": \"tonos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek tónos 'cord, rope; tension; pitch, tone' is the o-grade action noun *ton-o- of teínō 'stretch' (< *ten-yō): 'that which is stretched', hence a stretched string and the pitch it produces. 'string' is the base meaning given by Watkins.\",\n          \"derivation_fa\": \"یونانی tónos «ریسمان، کشش، زیر و بمی صدا» اسمِ با درجهٔ o از فعل teínō «کشیدن» است: «آنچه کشیده شده»، یعنی زه، و سپس صدای آن. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ténh₂us\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. ten- III.2: 'Suffixed o-grade form *ton-o- in Greek tonos, string, hence sound, pitch: TONE'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"1. ten- pp.1065-1066\", \"stance\": \"supports\", \"note\": \"'Old Indie tāna- m. \\\"clay, filament\\\" (compare gr. τόνος)'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.722 ff. (line 68224)\", \"stance\": \"supports\", \"note\": \"'„Ton“ (wie gr. τόνος ...)' under ten- „dehnen“.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pass-through box: Greek tónos > Latin tonus 'sound, tone' > Old French ton (12th c.), the source of both Persian ton and Middle English tone.\",\n          \"derivation_fa\": \"خانهٔ گذرگاه: یونانی tónos به لاتین tonus و از آنجا به فرانسوی ton رسید که هم منشأ «تُن» فارسی است و هم tone انگلیسی. درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins lists TONE under Greek tonos (ten- III.2); the French step is the standard route of the English word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt (grep '^Tone')\", \"stance\": \"silent\", \"note\": \"Entry not found by grep in the OCR.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt (grep '^tone,')\", \"stance\": \"silent\", \"note\": \"Entry not located by grep (OCR line start differs).\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Persian\",\n          \"words\": \"ton\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian ton تُن 'pitch of a sound, tone' is a modern loan of French ton (< Latin tonus < Greek tónos); Mo'in records it with the French tag.\",\n          \"derivation_fa\": \"«تُن» به معنای «درجهٔ زیر و بمی صدا» وام‌واژهٔ نو از فرانسوی ton است که از لاتین tonus و یونانی tónos آمده؛ معین آن را با همین معنا آورده است. درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"MON:1145\", \"status\": \"partial\", \"note\": \"2-vol abridgement MON_part1.txt line 43772: 'تن: [ton] (اِ.) درجهٔ بلندی و پستی صدا و آواز؛ مایه' — meaning confirmed; 6-vol page 1145 cannot be mapped.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 43772\", \"stance\": \"supports\", \"note\": \"'درجهٔ بلندی و پستی صدا و آواز؛ مایه.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. ten- III.2\", \"stance\": \"supports\", \"note\": \"'Greek tonos, string, hence sound, pitch: TONE'.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"tone\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English tone (ME ton, tone, 14th c.) < Old French ton / Latin tonus < Greek tónos 'stretching, pitch' (from teínō 'stretch').\",\n          \"derivation_fa\": \"انگلیسی tone (انگلیسی میانه ton) از فرانسوی کهن ton و لاتین tonus از یونانی tónos «کشش، زیر و بمی» است. درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. ten- III.2: '... Greek tonos, string, hence sound, pitch: TONE'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.722 ff.\", \"stance\": \"supports\", \"note\": \"τόνος under ten- „dehnen“.\"},\n            {\"src\": \"POK\", \"where\": \"1. ten- 1065-1066\", \"stance\": \"supports\", \"note\": \"Greek τόνος cited under ten-.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Germanic\",\n          \"words\": \"thunw\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *þunnuz (Watkins *thunw-, whence *thunniz) < zero-grade *tn̥h₂-ú-: syllabic *n̥ > Germanic un, *t > þ (Grimm's law), *-nw- > -nn-. Continued in OHG dunni, ON þunnr, OE þynne.\",\n          \"derivation_fa\": \"ژرمنی آغازین *þunnuz (به نگارش واتکینز *thunw-) از درجهٔ صفرِ *tn̥h₂ú- است: n هجایی به un، t به þ (قانون گریم) و -nw- به -nn- بدل شده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ténh₂us\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. ten- II.1: 'Suffixed zero-grade form *tn-u- in Germanic *thunw-, whence *thunniz in Old English thynne, thin: THIN'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"tenu-s 1069\", \"stance\": \"supports\", \"note\": \"'Old High German dunni, Old Saxon thunni, Old Icelandic þunnr \\\"thin\\\" (nn from nu)'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 39038 s.v. thin\", \"stance\": \"supports\", \"note\": \"'OE. þynne, rel. to OS. thunni, ON. þunnr ... orig. ‘stretched out’ ... fr. I.-E. base *ten-'.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"English\",\n          \"words\": \"thin\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English thin < ME thinne < OE þynne < PGmc *þunnuz (i-umlaut of u > y > i in the ja-/i-stem *þunniz) < PIE *tn̥h₂ú- 'stretched, thin'.\",\n          \"derivation_fa\": \"انگلیسی thin از انگلیسی کهن þynne و ژرمنی *þunnuz است که از *tn̥h₂ú- «کشیده، نازک» آمده است. درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. ten-: '*thunniz in Old English thynne, thin: THIN'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"line 39038\", \"stance\": \"supports\", \"note\": \"'thin ... ME. thinne, fr. OE. þynne ... fr. I.-E. base *ten-, ‘to stretch, extend’'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 19584 s.v. Thin\", \"stance\": \"supports\", \"note\": \"'Thin. (E.) M.E. thinne, A.S. þynne ... Skt. tanu ... lit. stretched out (√TAN)'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Ten 2, Stena\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *(s)tenh₂- 'to thunder' (Pokorny 1. (s)ten- 1021; Watkins (s)tenə-; LIV² 597)\",\n      \"note\": \"Pokorny 1021 heads '(s)ten-1' with the meaning 'to groan, etc.' but the material is largely 'thunder' (Skt. stanayati 'donnert', tanyatu- 'thunder', 'np. tundar', Latin tonō, OE þunor); Watkins gives '(s)tenə-. To thunder'; modern *(s)tenh₂-. Nourai's root, label and gloss are correct. Note that Pokorny does not cite a Parthian form; the Parthian tndwr (Manichaean /tandur/) is real (Wiktionary lists it as a cognate of tondar). Persian tondar is inherited from PIr. *tánHtā, a cognate of the Parthian word, not a derivative of it. No extraction errors.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *(s)tenh₂- «غریدن (تندر)» است؛ پوکورنی (ص۱۰۲۱) آن را با سنسکریت stanayati «می‌غرد»، tanyatu «تندر»، فارسی «تندر»، لاتین tonāre و انگلیسی کهن þunor آورده و واتکینز نیز «(s)tenə- غریدن» نوشته است. پس ریشه و معنای نورایی درست است. واژهٔ پارتی tndwr (تَندور) واقعی است، ولی «تندر» فارسی از ایرانی باستان *tánHtā به ارث رسیده و هم‌ریشهٔ واژهٔ پارتی است نه برگرفته از آن. خطای استخراج دیده نشد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)tenh₂-\",\n        \"https://en.wiktionary.org/wiki/تندر\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1021\", \"status\": \"supports\", \"note\": \"POK_full.txt line 81943 'Root / lemma: (s)ten-1' 'Meaning: to groan, etc.' ... 'stanayati \\\"donnert, dröhnt ...\\\", tanayitnú- \\\"dröhnend, donnernd\\\" ... tanyatú- \\\"thunder\\\"; afghan. tana \\\"thunder\\\"; np. tundar ds.' ... 'Latin tono, -are \\\"thunder\\\"' ... 'Old English þunor'; Page(s): 1021.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins s.v. (s)tenə-\", \"stance\": \"supports\", \"note\": \"'(s)tenə-. To thunder. 1. Zero-grade form *stnə- in Germanic *thunaraz in: a. Old English thunor ... THUNDER ... 2. O-grade form *tonə- in Latin tonāre, to thunder: TORNADO; ASTONISH, DETONATE, STUN. [Pok. 1. (s)ten- 1021.]'\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II p.626 (WLD_Bd2_pages.txt leaf 631)\", \"stance\": \"supports\", \"note\": \"'1. sten-, ten- von lauten Geräuschen; „donnern, rauschen, brausen, dröhnen“ ... afghan. tana „Donner“, np. tundar ds.'\"},\n        {\"src\": \"SYN\", \"where\": \"1.56 THUNDER (line 1746)\", \"stance\": \"supports\", \"note\": \"'Lat. tonitrus ... OE þunor ... Skt. stanita-'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Parthian\",\n          \"words\": \"tndwr\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Manichaean Parthian tndwr /tandur/ 'thunder' is attested (Wiktionary lists it, with Sogdian tundar, as a cognate of Persian tondar); it continues PIr. *tánHtā / *tanHtar- 'thunderer', an agent noun of *(s)tenh₂- (cf. Sanskrit tanyatú-, Latin tonitrus from *(s)ténh₂-tr̥).\",\n          \"derivation_fa\": \"پارتی مانوی tndwr (خوانش tandur) «تندر» گواهی شده است و ویکی‌واژه آن را همراه سغدی tundar هم‌ریشهٔ «تندر» فارسی می‌آورد. هر دو از ایرانی باستان *tánHtā «غرّنده» از ریشهٔ *(s)tenh₂- «غریدن» آمده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/تندر\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1021\", \"status\": \"partial\", \"note\": \"Pokorny 1021 has the root and 'np. tundar' but no Parthian form.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt (grep thunder)\", \"stance\": \"silent\", \"note\": \"MacKenzie's Pahlavi gives only γarrānag 'thunder'; Parthian is outside its scope.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary (grep thunder/tndwr)\", \"stance\": \"silent\", \"note\": \"No entry.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"tondar\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian tondar/tondor تندر 'thunder' (also تندور in Borhan) < PIr. *tánHtā (Wiktionary: inherited, from PIE *ténh₂-tōr or *tónh₂-tōr), with the vowel later rounded (tandar > tundar, cf. Afghan tandar). The word and root are certain, but it is inherited in Persian alongside the Parthian form, not taken from Parthian as the arrow suggests (unless one assumes a Parthian loan, which no source claims).\",\n          \"derivation_fa\": \"«تُندر» (در برهان «تندور» نیز) از ایرانی باستان *tánHtā «غرّنده» است و با پارتی tandur، سغدی tundar، سنسکریت tanyatú- و لاتین tonitrus هم‌ریشه است. خود واژه و ریشه قطعی است، ولی در فارسی واژه‌ای موروثی است و منبعی آن را وام از پارتی ندانسته است؛ پس فلش پارتی ← فارسی را باید هم‌ریشگی خواند و ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/تندر\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:517\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 746 (≈ p.517): 'تندور بضم اول و ثالث بروزن پرزور، بمعنی رعد باشد، و بفتح ثالث هم باین معنی آمده است'; leaf 745 footnote '۴ - قس: ریشهٔ هندی باستان [stan], [tan] (صدا پیچیدن، صدا دادن)'.\"},\n            {\"ref\": \"KLN:1613\", \"status\": \"supports\", \"note\": \"Klein 1966 line 39175 s.v. thunder: 'from the I.-E. imitative base *ten-, whence also OI. tanayitnuh, ‘thundering’, tanyati, ‘it thunders’, Pers. tundar, ‘thunder’ ... L. tonare'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"p.89 no. 396\", \"stance\": \"supports\", \"note\": \"'tunder, tundur „Donner“. Vergl. ai. √tan-, tányati „erschallen, laut tönen, rauschen“, tanayitnú- „donnernd“, tanyatú- „Donner“; lat. tonare, tonitrus; ags. þunor'.\"},\n            {\"src\": \"HUB\", \"where\": \"no. 396 (HUB.txt line 1653)\", \"stance\": \"supports\", \"note\": \"'Zu tundar „Donner“ ... gehört afgh. LW. tandar „Donner“, echt afgh. tana „Donner“ (Geiger).'\"},\n            {\"src\": \"ARY\", \"where\": \"pdf page 200 (Latin index)\", \"stance\": \"supports\", \"note\": \"'STANATI, STANITI, TANYATI, TANAYITU (SANSKRIT) ... TANDAR, TANA, TALANDA (AFGHAN)' under تندر.\"},\n            {\"src\": \"PHD\", \"where\": \"English index 'thunder'\", \"stance\": \"silent\", \"note\": \"Only 'thunder (n.) γarrānag'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"thunaraz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *þunraz / *þun(a)raz 'thunder, thunder-god' < zero-grade *(s)tn̥h₂-r-ós (Wiktionary after Matasović), *t > þ by Grimm's law; Watkins writes *thunaraz. Continued in OE þunor, OHG donar, ON Þórr (older Þunarr).\",\n          \"derivation_fa\": \"ژرمنی آغازین *þunraz / *þunaraz «تندر، خدای تندر» از درجهٔ صفرِ *(s)tn̥h₂-r-ós است و t طبق قانون گریم به þ بدل شده است؛ از آن انگلیسی کهن þunor، آلمانی کهن donar و نام خدای نورس Þórr آمده‌اند. درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)tenh₂-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. (s)tenə- 1: 'Zero-grade form *stnə- in Germanic *thunaraz in: a. Old English thunor ... c. Old Norse Thorr (older form Thunarr)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"(s)ten-1 p.1021\", \"stance\": \"supports\", \"note\": \"'Old High German donar ... Old English þunor, Old Icelandic Þórr \\\"Thunder God\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"line 39175 s.v. thunder\", \"stance\": \"supports\", \"note\": \"'OE. þunor, rel. to ON. Þórr, OFris. thuner ... OHG. donar'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"thunder\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English thunder < ME thuner, later thunder (with excrescent d between n and r, 13th c.) < OE þunor < PGmc *þunraz.\",\n          \"derivation_fa\": \"انگلیسی thunder از انگلیسی میانه thuner (با d افزوده میان n و r) و انگلیسی کهن þunor از ژرمنی *þunraz است. درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins: 'Old English thunor (genitive thunres), thunder, Thor: THUNDER; THURSDAY'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"line 39175\", \"stance\": \"supports\", \"note\": \"'thunder, n. — ME. thuner, later thunder, fr. OE. þunor'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 19662 s.v. Thunder\", \"stance\": \"supports\", \"note\": \"'Thunder, sb. (E.) For thuner; the d is excrescent. M.E. thoner. A.S. þunor ... L. tonare, to thunder, Skt. tan, to sound'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"tonâre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin tonāre 'to thunder' < Proto-Italic *tonāō, from the o-grade iterative *(s)tonh₂-éye- (de Vaan; Wiktionary), cf. Sanskrit stanáyati; tonitrus 'thunder' belongs to the same root.\",\n          \"derivation_fa\": \"لاتین tonāre «غریدن، تندر زدن» از ایتالیک آغازین *tonāō و صورت تکراریِ با درجهٔ o *(s)tonh₂-éye- است و با سنسکریت stanáyati هم‌ریشه است. درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)tenh₂-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. (s)tenə- 2: 'O-grade form *tonə- in Latin tonāre, to thunder'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p.1021\", \"stance\": \"supports\", \"note\": \"'Latin tono, -are \\\"thunder; also from other lauten Schalleindrücken\\\", tonitru, tonitrus \\\"thunder\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p.626\", \"stance\": \"supports\", \"note\": \"sten-, ten- „donnern“ with Latin tonāre.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"tornado, detonate, astonish\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"detonate < Latin dētonāre 'to thunder down/out' (18th c.); astonish < ME astonien / OF estoner < Vulgar Latin *extonāre 'to strike with thunder, stun' (with -ish from verbs like abolish); tornado (1550s ternado, a nautical word for a thunderstorm) < Spanish tronada 'thunderstorm' < tronar 'to thunder' < Latin tonāre, with metathesis tron- > torn- under the influence of Spanish tornar 'to turn'. Watkins and Wiktionary derive tornado this way; Skeat instead put it under turn (tornar), but the thunderstorm sense of the earliest English uses favours tronada.\",\n          \"derivation_fa\": \"detonate از لاتین dētonāre «غرّیدن»، astonish از فرانسوی کهن estoner و لاتین عامیانهٔ *extonāre «با تندر گیج کردن»، و tornado (نخست ternado، اصطلاح دریانوردی برای طوفان تندری) از اسپانیایی tronada «طوفان تندری» از tronar (لاتین tonāre) است که زیر تأثیر tornar «چرخیدن» جابه‌جایی (قلب) حروف یافته است. اسکیت آن را از tornar می‌دانست، ولی واتکینز و ویکی‌واژه همان دیدگاه نورایی را دارند. درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/tornado\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. (s)tenə- 2: 'Latin tonāre, to thunder: TORNADO; ASTONISH, DETONATE, STUN'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 19916 'Tornado; see Turn'\", \"stance\": \"partial\", \"note\": \"Skeat derives tornado from Spanish tornar 'turn' (under Turn), not from tronada.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt (grep '^tornado', '^astonish')\", \"stance\": \"silent\", \"note\": \"Entries not located by grep in the OCR.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-15T02:52:32.822Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-502.json (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:52:36.007Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"taxma\" KNT_full.txt | head -5; cd /home/sfmqrb/git/rishe-private && python3 -m json.tool data/verification/page-502.json >/dev/null && python3 tools/verify_check.py 502"
}
```


### [2026-10-15T02:52:36.912Z] TOOL RESULT

```
1821:taxma- ‘brave’, with x retained before m, in the 
5072:Thus the ç of Cica*taxma- is represented by š 
6354:sp in späda- ‘army’, in Taxmaspdda- (name of a 
7750:and Varka-zana-, Saka-, späda- in Taxma-spáda-, 
8418:taxma-. 
nodes verified: 21/21
node verdicts: {'plausible': 6, 'confirmed': 15}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 5, 'supports': 21, 'not_checked': 3, 'not_found': 1}
books consulted: {'supports': 34, 'contradicts': 1, 'silent': 10, 'partial': 7} | by book: {'KLN': 11, 'POK': 6, 'WLD': 5, 'SKT': 5, 'NYB': 4, 'PHD': 4, 'HUB': 3, 'MON': 2, 'AHD': 2, 'SYN': 2, 'ARY': 2, 'LAT': 1, 'IEC': 1, 'BRT': 1, 'KNT': 1, 'CHEUNG': 1, 'HRN': 1}
```


## [2026-10-15T02:52:40.386Z] TOOL CALL #59: Edit

```json
{
 "replace_all": false,
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-502.json",
 "old_string": "\"note\": \"Old Persian taxma- appears only in the name Taxmaspāda-; no tanu compound.\"}",
 "new_string": "\"note\": \"KNT_full.txt line 1821 'taxma- ‘brave’, with x retained before m'; OP taxma- occurs in the names Taxmaspāda- and Čiçantaxma- (lines 5072, 6354); no tanu compound.\"}"
}
```


## [2026-10-15T02:52:41.172Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-502.json >/dev/null && python3 tools/verify_check.py 502 | grep -c PROBLEM"
}
```


### [2026-10-15T02:52:41.705Z] TOOL RESULT

```
The file /home/sfmqrb/git/rishe-private/data/verification/page-502.json has been updated successfully. (file state is current in your context — no need to Read it back)
```


### [2026-10-15T02:52:41.936Z] TOOL RESULT

```
0
```


## [2026-10-15T02:52:51.015Z] TOOL CALL #61: SubagentHandback

```json
{
 "message": "Page 502 (book page 472) is verified. I wrote /home/sfmqrb/git/rishe-private/data/verification/page-502.json, and `verify_check.py 502` reports 0 PROBLEM lines.\n\n**Counts:**\n- **Nodes (21 of 21 verified):** 15 confirmed, 6 plausible, none disputed, none transcription_suspect.\n- **Roots:** 2 confirmed.\n  - Ten 1, Tengh, Temp is PIE *ten- 'to stretch' (Pokorny 1064–1067).\n  - Ten 2, Stena is *(s)tenh₂- 'to thunder' (Pokorny 1021).\n- **Nourai's own references:** 21 support, 5 partial, 1 not found (BQT:411), 3 not checked (VSF has no copy, and two boxes print no reference).\n\n**Plausible nodes (none are disputed):**\n- **Ten 1 #1, Latin \"ana-tempa\":** not an attested Latin word. It is Klein's and Pokorny's starred reconstruction *an(a)-temp-na behind antemna/antenna, printed without the asterisk or the -n-. Ernout-Meillet treat antemna as a loan of unknown origin.\n- **Ten 1 #4, English list:** temperature and antenna connect to *temp- only tentatively. The other words in the box are secure.\n- **Ten 1 #6, Avestan:** \"a-puthra-tanu\" and \"taxma-tanu\" are reconstructions, not attested Avestan words. tanū- and pəšō.tanu- are real (Bartholomae).\n- **Ten 1 #7, Persian:**\n  - tanīdan comes straight from the verb root *tan- (Cheung), not from tanū- 'body'.\n  - The tan- element in âbestan is contested: Nyberg and Hübschmann read *ā-puça-tanu-, but Wiktionary gives *āpuθra- 'pregnant' with no tan-.\n- **Ten 1 #9, tonok:** inherited through Middle Persian tanuk, so it is a cognate of Sanskrit tanuka-, not a derivative. tonekeh is simply tonok + -e; nothing supports the book's note pointing to root \"Kitu\".\n- **Ten 2 #2, tondar:** inherited from Proto-Iranian *tánHtā, a cognate of Parthian tndwr. No source treats it as borrowed from Parthian.\n\n**Extraction errors:** none. The JSON matches the printed page.\n\nEtymonline pages could not be fetched (403) and are not cited."
}
```


### [2026-10-15T02:52:51.429Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
