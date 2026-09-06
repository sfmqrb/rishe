# Verification process log — verify-page-242


## [2026-09-06T15:48:16.034Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 242 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-242.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-242.json. Write /home/sfmqrb/git/rishe/data/verification/page-242.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 242` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:48:17.519Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:48:18.237Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:48:18.252Z] TOOL RESULT

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
226	```json
227	{
228	  "pdf_page": 126,
229	  "book_page": 96,
230	  "verified_by": "claude-opus-5",
231	  "verified_on": "2026-09-05",
232	  "entries": [
233	    {
234	      "entry": 0,
235	      "root": "Dheigh, Dhigha",
236	      "verdict": "confirmed",
237	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
238	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
239	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
240	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
241	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
242	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
243	      "nodes": [
244	        {
245	          "id": 6,
246	          "lang": "Avestan",
247	          "words": "pairi-daeza",
248	          "verdict": "confirmed",
249	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
250	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
251	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
252	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
253	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
254	        }
255	      ]
256	    }
257	  ]
258	}
259	```
260	
261	Rules:
262	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
263	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
264	- `words` = the transliterations of the node joined by "; " (copy from the chart).
265	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
266	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
267	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
268	- If a node lists several words, cover each word; if they differ in verdict, use the worst
269	  verdict for the node and explain per word in `derivation`.
270	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
271	  scholarship takes.
272	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
273	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
274	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
275	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
276	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
277	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
278	  any extraction errors (JSON differs from the printed page) the owner must fix.
279	  Do not paste the JSON back into your reply.
280	
```


## [2026-09-06T15:48:18.426Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-242.txt"
}
```


### [2026-09-06T15:48:18.443Z] TOOL RESULT

```
1	=== PDF page 242 (book page 212) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kar 1, Qar 1, Quseros, Qhar; Karkar, Kongar : hard; hardened or fortified, armor, fort  (refs POK:531; IEC:1056,1632)
4	#1 (parent #0) [Avestan] refs=POK:531; SYN:1201 | xratu : mental strength, intelligent work
5	  #2 (parent #1) [Pahlavi] refs=None | xrat : intelligence
6	    #3 (parent #2) [Persian] refs=BQT:729 | xerad «خرد» : intelligence
7	#4 (parent #0) [Sanskrit] refs=POK:531; KLN:703 | xara : hard, rough ; karkarah : hard ; karkatah : crab (hard body)
8	  #5 (parent #4) [Pahlavi] refs=BQT:697; WLD:355; SYN:173 | xâr : hard, rough ; kar-cang : crab
9	    #6 (parent #5) [Persian] refs=BQT; HRN | xâr 2 «خار» : thorn ; xârâ «خارا» : a hard stone ; xarčang «خرچنگ» : crab
10	#7 (parent #0) [Avestan] refs=SOD:166 | xara : a harsh voiced animal, donkey
11	  #8 (parent #7) [Pahlavi] refs=WLD:355; SYN:173 | xar : donkey, harsh ; xar-bâra : donkey load ☞Bher 1 ; xar-buz : harsh melon or cucumber
12	    #9 (parent #8) [Persian] refs=BQT; HRN; FVF:190 | xar «خر» : donkey, symbol of harshness | extra: خروار، خربزه، خرگوش، خرمگس، خرمهره
13	  #10 (parent #7) [Sogdian] refs=SOD:166 | xr : donkey ; xr-tr`k, xara-tara : related to a donkey, mule
14	    #11 (parent #10) [Persian] refs=MON:2615 | qâter «قاطر» : mule | extra: قاطر
15	#12 (parent #0) [Sanskrit] refs=POK:531; IEC:1632 | kankarta, kankatih : fortified, armor
16	  #13 (parent #12) [Persian] refs=IEC:1632; MON:3102 | kongareh «کنگره ۱» : battlement on a castle wall
17	#14 (parent #0) [Germanic] refs=KLN:703; AHD | harduz : hard
18	  #15 (parent #14) [Old French] refs=AHD:1257 | estandard : standing firm, a flag or rule that stands firm ☞Stâ
19	    #16 (parent #15) [Persian] refs=MON:239 | estândârd «استاندارد» : standard
20	    #17 (parent #15) [English] refs=None | standard
21	  #18 (parent #14) [English] refs=None | hard, Richard, Bernard, Leonard, Gerard
22	#19 (parent #0) [Greek] refs=AHD:351 | keratos : strength, government ; děmos-keratos : people's government ☞Dâ ; karkanos : crab
23	  #20 (parent #19) [French] refs=AHD | 
24	    #21 (parent #20) [Persian] refs=MON:1561 | demokrâsî «دموکراسی» : democracy
25	    #22 (parent #20) [English] refs=None | democracy
26	  #23 (parent #19) [English] refs=None | carcinogen
27	#24 (parent #0) [Latin] refs=KLN:230 | carcro : hard ; cancer : hard bodied animal, crab
28	  #25 (parent #24) [English] refs=None | cancer
29	#26 (parent #0) [Indo-European] refs=IEC:1056 | Qusěro : scrape, scratch
30	  #27 (parent #26) [Persian] refs=IEC:1056 | xârîdan «خاریدن» : to scratch, itch | extra: خارش
31	
```


## [2026-09-06T15:48:22.068Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-242.json",
 "description": "Read source JSON for page 242"
}
```


## [2026-09-06T15:48:22.097Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:48:22.112Z] TOOL RESULT

```
{
  "pdf_page": 242,
  "book_page": 212,
  "entries": [
    {
      "root": {
        "name": "Kar 1, Qar 1, Quseros, Qhar; Karkar, Kongar",
        "lang": "Indo-European",
        "refs": "POK:531; IEC:1056,1632",
        "gloss": "hard; hardened or fortified, armor, fort"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:531; SYN:1201",
          "words": [
            {"translit": "xratu", "gloss": "mental strength, intelligent work", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "xrat", "gloss": "intelligence", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:729",
          "words": [
            {"translit": "xerad", "gloss": "intelligence", "script": "خرد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:531; KLN:703",
          "words": [
            {"translit": "xara", "gloss": "hard, rough", "script": null},
            {"translit": "karkarah", "gloss": "hard", "script": null},
            {"translit": "karkatah", "gloss": "crab (hard body)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "BQT:697; WLD:355; SYN:173",
          "words": [
            {"translit": "xâr", "gloss": "hard, rough", "script": null},
            {"translit": "kar-cang", "gloss": "crab", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT; HRN",
          "words": [
            {"translit": "xâr 2", "gloss": "thorn", "script": "خار"},
            {"translit": "xârâ", "gloss": "a hard stone", "script": "خارا"},
            {"translit": "xarčang", "gloss": "crab", "script": "خرچنگ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SOD:166",
          "words": [
            {"translit": "xara", "gloss": "a harsh voiced animal, donkey", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Pahlavi",
          "refs": "WLD:355; SYN:173",
          "words": [
            {"translit": "xar", "gloss": "donkey, harsh", "script": null},
            {"translit": "xar-bâra", "gloss": "donkey load", "script": null, "see": ["Bher 1"]},
            {"translit": "xar-buz", "gloss": "harsh melon or cucumber", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "BQT; HRN; FVF:190",
          "words": [
            {"translit": "xar", "gloss": "donkey, symbol of harshness", "script": "خر"}
          ],
          "script_extra": "خروار، خربزه، خرگوش، خرمگس، خرمهره",
          "note": null,
          "quote": {
            "text": "خر عیسی گرش به مکه برند - چون بیاید هنوز خر باشد",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 10,
          "parent": 7,
          "lang": "Sogdian",
          "refs": "SOD:166",
          "words": [
            {"translit": "xr", "gloss": "donkey", "script": null},
            {"translit": "xr-tr`k, xara-tara", "gloss": "related to a donkey, mule", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON:2615",
          "words": [
            {"translit": "qâter", "gloss": "mule", "script": "قاطر"}
          ],
          "script_extra": "قاطر",
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:531; IEC:1632",
          "words": [
            {"translit": "kankarta, kankatih", "gloss": "fortified, armor", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "IEC:1632; MON:3102",
          "words": [
            {"translit": "kongareh", "gloss": "battlement on a castle wall", "script": "کنگره ۱"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "کنگره ویران کنید از منجنیق - تا رود فرق از میان این فریق",
            "poet": "Molavî"
          }
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:703; AHD",
          "words": [
            {"translit": "harduz", "gloss": "hard", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Old French",
          "refs": "AHD:1257",
          "words": [
            {"translit": "estandard", "gloss": "standing firm, a flag or rule that stands firm", "script": null, "see": ["Stâ"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:239",
          "words": [
            {"translit": "estândârd", "gloss": "standard", "script": "استاندارد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 15,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "standard", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 14,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "hard, Richard, Bernard, Leonard, Gerard", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:351",
          "words": [
            {"translit": "keratos", "gloss": "strength, government", "script": null},
            {"translit": "děmos-keratos", "gloss": "people's government", "script": null, "see": ["Dâ"]},
            {"translit": "karkanos", "gloss": "crab", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "French",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "Persian",
          "refs": "MON:1561",
          "words": [
            {"translit": "demokrâsî", "gloss": "democracy", "script": "دموکراسی"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 20,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "democracy", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 23,
          "parent": 19,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "carcinogen", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 24,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:230",
          "words": [
            {"translit": "carcro", "gloss": "hard", "script": null},
            {"translit": "cancer", "gloss": "hard bodied animal, crab", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 25,
          "parent": 24,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cancer", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 26,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "IEC:1056",
          "words": [
            {"translit": "Qusěro", "gloss": "scrape, scratch", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 27,
          "parent": 26,
          "lang": "Persian",
          "refs": "IEC:1056",
          "words": [
            {"translit": "xârîdan", "gloss": "to scratch, itch", "script": "خاریدن"}
          ],
          "script_extra": "خارش",
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


### [2026-09-06T15:48:22.131Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
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


## [2026-09-06T15:49:09.827Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo --- && sed -n '1,60p' tools/verify_check.py",
 "description": "List verification dir and check tool"
}
```


### [2026-09-06T15:49:09.882Z] TOOL RESULT

```
agent
page-100.json
page-101.json
page-102.json
page-103.json
page-104.json
page-105.json
page-106.json
page-107.json
page-108.json
page-109.json
page-110.json
page-111.json
page-112.json
page-113.json
page-114.json
page-115.json
page-116.json
page-117.json
page-118.json
page-119.json
page-120.json
page-121.json
page-123.json
page-124.json
page-125.json
page-126.json
page-127.json
page-128.json
page-129.json
---
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


## [2026-09-06T15:49:12.482Z] TOOL CALL #6: Bash

```json
{
 "command": "pdftoppm -f 242 -l 242 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg242 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render page 242 to PNG"
}
```


### [2026-09-06T15:49:15.384Z] TOOL RESULT

```
total 6632
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 11:49 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     880 Sep  6 11:48 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb   77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47928 Sep  6 11:38 mk224.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53093 Sep  6 11:40 mk226.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51303 Sep  6 11:39 mk228.py
-rw-rw-r-- 1 sfmqrb sfmqrb   29152 Sep  6 11:37 mk229.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:47 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   17907 Sep  6 11:25 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb  194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb  147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb  118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb   90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:49:19.991Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg242.png"
}
```


### [2026-09-06T15:49:20.794Z] TOOL RESULT

```

```


## [2026-09-06T15:49:20.791Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T15:49:36.470Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 531 area: grep kar- hart ===\"\ngrep -n -i \"kar-1\\|hart, stark\\|karkaros\" POK_full.txt | head -30\necho \"=== POK xratu ===\"\ngrep -n \"xratu\\|kratús\\|κράτος\" POK_full.txt | head -20",
 "description": "grep Pokorny for kar- root"
}
```


### [2026-09-06T15:49:36.528Z] TOOL RESULT

```
=== POK 531 area: grep kar- hart ===
43826:Root / lemma: kar-1 
48107:compare also above kar-1S. 530, where Balto Slavic examples can also belong here. 
=== POK xratu ===
43928:remains far off Old Indie kratu-, Avestan xratus^ spiritual power '.
```


## [2026-09-06T15:49:38.890Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC 1056 / 1632 headwords ===\"\ngrep -n -i \"quseros\\|qusero\\|kankarta\\|kankati\\|kongar\" IEC.txt | head -30\necho \"=== SOD 166 xr donkey ===\"\ngrep -n \"xr-tr\\|xartar\\|xrtr\\|donkey\" SOD.txt | head -30",
 "description": "grep IEC and SOD"
}
```


### [2026-09-06T15:49:38.961Z] TOOL RESULT

```
=== IEC 1056 / 1632 headwords ===
8165:kseros (2) (quseros ?) “sharp, harsh'. (Same as (1)? The alternative initial is suggested by Gk. psorós (rough?) Skt. khárah, kharuh 'rough, harsh'; Oss. cf. áxsálí ‘Juniper’; Tokh. A tsår, B Scire trough, hard’; R cf. Sero-xovatyj ‘rough, rugged’; Ukr. Sory, pl. ‘barbs’. Long-gde in R o-šaràšiť ‘dumbfound’
14304:qusaros (1), variant of type quseros, q. v.
14330:qusero, ið ‘scrape, scratch, itch. Cf. qusoros and next. Per. (ambig. *-ē- or *-0-) xaram, v. ‘scratch, itch’; Alb. cf. shore, f. trash, eruption on skin’; R šàrju, inf: Sàrit, v. Árummage'
14331:quseros ‘rough, harsh’. (Variant: qusóros). Cf. kseros, and WP I, 355 Skt. kharah (frough, sharp, hard’. Phonol. ambig.); Gk. cf. (o-gde) psorós 'rough, un- even'; Tokh. A tsår, id.; Pol. cf. szor-stki, adj. as Skt.
14332:quséros (qusáros? Initial and vocalism pro- blematic) ‘motley’. Variant initial consonant- ism in Indo-Iranian. Cf. WP II, 666 Skt. cf. Caráh, Sàrab, id.; Per. sar, sarak, s. "star. ling’; Gk. psàrós, adj. ‘motley’; pser, gs: -ós, beside psar, m. ‘starling’; Alb. cf. shore ( rash, eruption’, but see quseros above); OCS Sarü, šara, mf. ‘colour’; Sar&jo se, v. “be variegated'; Srb. Sar, adj. ‘motley’; Blg. Sar, m. ‘dye’ be- side šaren, adj. ‘motley’. (The initial conso- nantism of Lat. varius, adj. ‘motley, change- able’ and vārī, mpl. ‘rash, pockmarks? is of uncertain background)
=== SOD 166 xr donkey ===
6001:Ixarl  Yr-  donkey      Av.  xara- 
35163:donkey 
35167:A-10,  4;  GMS  1177;  Yr'crm,  "donkeys  skin", 
35839:xartare   ©<*xara-tara-,  Turk.   =*xrtry 
79948:donkey 
79992:xrtry 
80007:10629  xrtry   S(M)  ^<>IS 
80008:xartare  ^yrt^k 
88959:donkey     4169,  10622
```


## [2026-09-06T15:49:44.983Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '43820,43960p' POK_full.txt",
 "description": "Print Pokorny kar-1 entry"
}
```


### [2026-09-06T15:49:45.032Z] TOOL RESULT

```
among the reflexes of PT *Klp- (usually confused with *Klp- 'spark') and the TM derivative 
*kapta- (usually confused with *kapta- 'flat'). Cf. also *k'ap'V. 

References: WP. I 342 ff., WH. I 159 f., 169. 
Page(s): 527-528 

Root / lemma: kar-1 

Meaning: to scold, punish 

Material: Gr. Kopvp l,x\\x\cx, auT6Kapvo(; auT0^npi0(; Hes.; 

Latin carino, -are^ scoff, mock ' (probably a); 

Old Irish cairei. "reprimand', acymr. cared^ wickedness; idleness', cymr. caredd^iauW., 
error', corn. cara^xeb\Ae\ Middle Breton ca/iez" reprimand' {*l<ria)\ 

Old High German harawen. Middle High German herwen^ deride ', Old English hierwan 
" deride ', Old Norse herfiligr' contemptible, degrading'. Middle High German here, herwer 
" sharp, tangy', Finnish loanword karvas' bitter| bracl<isli| pungent; liarsli| slirill;sad| calamitous; 
ill-naturedl caustic'; zero grade Old English gehornian^ affront, offend'; 

Latvian /ra/7/7a/' banter, stir, tease, irritate'; ablaut. East Lithuanian kirinti6s:. 

Old Church Slavic kerb, u-korb^ indignityl affront| abuse/insult', u-koriti^vMy, scold', po 
koriti^ subject, subdue', Czech yOC»-/rc»/'5 'humility', yOC»-/rc»/77y" humble, humiliated', ablaut. 
Serb. -Church Slavic karat 'fight', Czech kara' reproach, accusation, punishment', etc.; 

Maybe alb. kor/t'make ashamed' a Slavic loanword. 

perhaps here Tocharian A karn-, B karn- "torment, smite'. 

References: WP. I 353, WH. I 168 f.; Trautmann 118 places Balto Slavic words to Indo 
Germanic kor/o- see there. 
Page(s): 530 

Root / lemma: kar-2, kara- 
Meaning: to praise, glorify 



Note: also (still) more in general onomatopoeic words as many other, the connection from 
kand /■included roots 



Material: Old Indie carkarti^ erwahnt ruhmend ' (Aor. akant), carkrtf-lavne, praise, 
laudation', karkarf-, karkarT a kind of sound ', kTrtf- f. "fame, knowledge' (thereafter with /" 
also kTrf-, /r/?/>7- 'singer'); karii- 'singer, bard' (: Kripu^); 

gr. KapKoipw ' thunder out, roar, rumble ', Kripu^, Doric KOpO^ ' herald '; 

Old Norse herma {*harmjan) ' apprise, notify ', hrodrxw. 'fame, laudation ', Old English 
hrodorm. 'pleasure, joy', hred {* hrot^i-) 'fame'. Old High German {h)rdd-, (h)ruod-6s. (in 
EN), Gothic hro^eigs' glorious ', Old Norse hrosa^ vaunt ' {* hrdt^s-dn)\ Old High German 
(h)ruom. Old Saxon hromlame, laudation, honour', in addition Old English breme 
'illustrious' {* bihromi-); 

Maybe alb. mbrembje ' even\ng, dark' common alb. b > mb 

perhaps as i>-extension: Gothic ^rops 'clamor'. Old High German ruofshoxA, call'. Old 
Saxon Old English hropan. Old High German (b) ruo fan ^caW, shout, cry'. Old High German 
(h)ruoft. Middle High German geruefte, geruofteu. 'shout, call, scream ', Middle Low 
German ruchte, rochteu. 'shout, call, scream, rumor'. Modern High German (from Ndd.) 
Gerucht . ' rumbling, rumor, hearsay '; 

Lithuanian kafdas^ echo ', Old Lithuanian ap-kerdziu^\ announce ', Old Prussian kirdJt 
'hear'. 

References: WP. I 353 f. 
Page(s): 530-531 

Root / lemma: kar-3, redupl. kartiar- 

Meaning: hard 

Material: Old Indie /ra/'/ra/'a- 'rough, hard' = gr. KopKopoi Tpax£T<; Hes., Old Indie karkasa- 

'rough, hard' (also karaka-xx\., 'hail'?); presumably gr. Kpava[F]6(; 'hard, rough, rocky'. 

In addition probably die words for ' Cancer, 4th sign of the zodiac': Old Indie karkata-m. 
' Cancer, 4th sign of the zodiac' {karkin- ' Cancer, 4th sign of the zodiac as constellation', 
loanword from gr. KapKivo(;), karka-hm. 'crab'; 

gr. KapKivo(; ds., Latin cancer, -crT6s. (dissim. from *carcro-, perhaps already Indo 
Germanic, compare Old Indie karjkata-xw. 'armor, coat of mail, garment made of linked 
metal rings ' from *karikrta-)\ 



Old Church Slavic rakt " Cancer, 4th sign of the zodiac' from *kraki, dissim. sei, is 
possible; die Ahnlichkeit with Norwegian (etc.) rseke^caucev squilla, prawn, shrimp' places 
borrowing of Norwegian words ahead; 

further words for hard shell, nut, dry fruit contained in a shell: gr. Kopuov ' nut, dry fruit 
contained in a shell', Kopua f. " walnut'; Latin cannai. " nutshell, the keel of a ship, ship' 
(maybe from Gr. after Keller Volkset. 279, in which case Kapuivoq is the origin); cymr. ceri 
{*carTso-) "kernel '. 

With /-suffixes: Gothic hardus' hard, stern'. Old Norse hardr' hard', Old English heard 
"hard, strong, valiant'. Old Saxon hard. Old High German hart, herti^hard, tight, firm, heavy 
', Adv. Old Norse harda. Old English hearde. Old High German harto. Middle Low German 
harde^yevj, particularly, specially, especially, particular: in particular, peculiarly, 
separately, extra, notably ' (compare gr. Kopra), proto Germanic *hardu- from Indo 
Germanic *kar-t'u-; due to an Indo Germanic extension *kre-t-, *krt- Aeolic (Gramm.) 
Kp£TO(;, next to which with the vocalism of Adj. Attic KpaTO(;, ep. Ionian Kaproc; " strength, 
power', hom. KpaTU(; "strong' Komparat. Ionian Kpsaaajv, Attic KpeiTTwv, Superl. KpaTiaTO(;, 
ep. KapTiaTO(;, Adv. Kapra "strong', K^aiz^oc,, KapT£p6(; "strong, tight, firm, violent' (etc.); 
remains far off Old Indie kratu-, Avestan xratus^ spiritual power '. 

Old Indie kathina-, kathora-' hard, tight, firm, stiff ' could also belong to Indo Germanic / 
to cymr. ca/ed. Middle Irish ca/ad'hard', gall, -ca/etos {see ka/- "hard'). 

Because of the existence of a widespread iber.-mediterr. *carra 'stor\e, cairn, pile of 
stones set up as a memorial or mark of some kind ' (v. Wartburg FEW. s. v.) the affiliation 
of the following words is dubious, they could partly belong here or to (sjker-'cut, clip': 

Old Irish carraci. (nir. carraig) "rocks, cliff and creci. ds.. Gen. craice, creice. Middle 
Irish also Nom. craic {r\\r. craig) f. ds.. Gen. creca, derive all from Brit., also Middle Irish 
crach^ouqh' (= scabbed); to acymr. carrecc, cymr. carregi. "stone, rocks' {*karrika), bret. 
karreg, corn, carrek ds., compare cymr. cam?^ "stream, brook' {*karraka), actually " rock 
brook ' = Middle Irish carrach^ scabbed ' and gallo-rom. *cracos ^s\.or\e' (v. Wartburg FEW. 
s. v), acymr. creik, cymr. craigi. {*krakT} "rocks', bret. krag^ sandstone ', cymr. crach 
"scurf' = bret. (Vannes) krah^ small hill, cusp, peak' {*krak-, *krakk-, perhaps through 
metathesis from *kar-k-) etc. basic forms are Proto Indo Germanic "/ra/r- or Indo Germanic 
YSy/Zr-s- (ergabe Celtic carr-), respectively *kar-k-, also zweidentig Italian-venezian. 
(Venetic) scaranto, caranto^ stony mountain brook ' and Venetic PN Scarantia> Scharnitz 
(Tirol), Ca/'a/7/a/7/5"Carinthia, region in southern Austria', etc.; 



likewise Germanic *har(u)gaz^ cairn, pile of stones set up as a memorial or mark of 
some kind, sacrificial altar ' in Old Norse hgrgr^ cairn, pile of stones set up as a memorial 
or mark of some kind ', Old English heargm. " heathenish temple'. Old High German harg 
' grove, temple' (Finnish loanword karko^ woodpile, pile, stack ', /7a/'/r/rc» 'clump, heap'), 
perhaps also to Old Irish cymr. bret. co/77 'stone hill, stone grave ', and Old High German 
hart^ mountain forest ', Old English harad, -edds.; barely here as 'woodlander, forest- 
dweller ' the Old Germanic VN Xapou5£c;, Harudes, Old English Hseredas, Old Icelandic 
Hgrdar, rather to Old Irish caur, cur' hero ' ( *karut-s). 

References: WP. I 30f., 345f., WH. I 8, 151, 166, 168, Loth RC 43, 401 f., Thurneysen KZ.
```


## [2026-09-06T15:49:46.649Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5995,6010p' SOD.txt; echo ---; sed -n '35830,35850p' SOD.txt; echo === ; grep -n -i \"kankar\\|kankat\\|konger\\|kangura\\|kangar\" IEC.txt | head -20",
 "description": "SOD context and IEC kankarta"
}
```


### [2026-09-06T15:49:46.724Z] TOOL RESULT

```
Exit code 1

/xep8/        Yyp8\  own  Av.  xvaepai&ya- 

xypS;  xypO 

3)  Ixl  Voiceless  velar  spirant  <  *x  and  *  h 
Ixarl  Yr-  donkey      Av.  xara- 

/max/  m>x  moon         Av.  mah 

/farnxunde/  prnYwnS^k  fortunate  Av.xywarnahwant 

IV)  The  voiced  stops  [*,  d,  /,  g]  are  predictable;  they 
are  conditioned  by  their  phonological  environment 
such  as  nasal  and  voiced  sibilants.  They  behave  as 
ailophonic  variants  of  voiceless  stops.  The  picture  is 
---
xartc   (yrty,  yrtk)  ©pp.  pi.  -/;  ace.  -w  =»xrtyh 
past,  gone 

TSP  2.831,  7.84,  10.7,  11.9;  BSTBL,  Dhy.  358; 
MDii;  Doc.  10.16.;  Yrtw,  MDii  p200,  A-14,12 

4269  yrtk  =>  yrt)k 

4270  yrtr'k    B  j& 
xartare   ©<*xara-tara-,  Turk.   =*xrtry 

mule 

TSP  2.771n  pl79;  Hen.  Texts.  723 

4271  yrty  =»  yrt>k 

4272  yrwy    B  (Jf^<J&.)*Jjli~<JU-li43jar 
xarwe   ©<*xwaraka;  Pahl.  xwarg 

ember 
(eval):2: == not found
```


## [2026-09-06T15:50:15.879Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['POK','IEC','SYN','SOD','WLD','KLN','AHD','BQT','MON','HRN','FVF','FVQ']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-06T15:50:18.575Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."}
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt;
```


## [2026-09-06T15:50:24.043Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 173 (donkey?) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==197' SYN.txt | head -60",
 "description": "Buck p.173"
}
```


## [2026-09-06T15:50:24.766Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 1201 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==1225' SYN.txt | head -50",
 "description": "Buck p.1201"
}
```


### [2026-09-06T15:50:26.145Z] TOOL RESULT

```
=== SYN 173 (donkey?) ===
�� (3.27). WaldeP. 1.628f. Falk-Torp 298. Hellquist 269, NED s.v. gilt, sb.?.
Dan. orne ‘boar’, Sw. dial. orne ‘boar’ or ‘barrow’: Lat. verrés ‘boar’, ete. (above, 3) Falk-Torp 867. Hellquist 737.
OE bar, ME bore, NE boar, Du. beer, OHG, MHG ber, NHG dial. bar, etym.?
6. Lith. kuilys, Lett. kuilis : Lith. kiaulé ‘swine’ (3.31).
7. SCr. nerast, epd. of neg. ne and rasti ‘grow’, lit. ‘one that does not grow’, applied to a tree that will not grow and to the ‘boar’ as the swine that will not fatten, in contrast to the castrated hog. Rjetnik Akad. 8.46.
Boh. kanec, fr. Hung. kan ‘male ani- mal’. Berneker 479.
Pol. kiernoz = ORuss., Ukr. knoroz : ChSl. kriini ‘mutilated’, perh. com- pounded with a word for testicle cognate with Grk. dpxis, the whole meaning orig. ‘castrated’, with shift to ‘boar’. Ber- neker 663f. Briickner 229.
Russ. kaban, fr. Turk. Berneker 464, Lokotsch 975. :
8. Skt. varaha-, Av. varaza- (but both only ‘wild boar’) etym.?
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
| | | | /
1 terms for the ‘barrow’ - unfamiliar, the gen- nly used in ref-
; ‘castrated’ (cf. teow’; or With added ‘cas : aaah E castrated hog, Fr. pore chatré,
4), as N : ed verschnittenes schwein, NG pouvouxt-
te. tyo youpout, © ; al Grk. roulas ‘castrated animal’
3.14) was the technical term, just as for ‘wether’ (3.27), but usually simply
éponv (as in Hom., Od. a 13h, where the 360 hogs used for eating, contrasted with the 600 sows, were, of course, castrated males).
NG povvovxexorpos, epd. of xotpos ‘hog’ with pouvodxos ‘castrated’ (3.19).
9. Lat. maidlis (Varro, RR 2.4.21 castrantur verres—quo facto nomen mu- tant aique e verribus dicuntur maiales), hence It maiale, perh fr. Maia (or only pop. etym.?), in any case prob. in- fluenced by maior ‘larger’, with refer- ence to the greater growth of the cas- trated animal. Walde-H. 2.13. Er- nout-M. 582.
In Fr., Sp., Rum. only the generic words in common use, though the words for ‘castrated’ may be added.
3. In Celtic, only the generic words or with the addition of the words for castrated (3.14).
4. ON borgr, OF bearg, ME baru, barowe, NE barrow, Du. barg, OHG barug, barh, NHG barch (borch, barg, borg); prob. fr. the root of ON berja strike’, Lat. fertre ‘strike, cut’, etc., here in the sense of ‘castrate’. Walde-P. 2,160. aie ue galt ‘male swine’, both also
: ae or Ee , See 3.32.
(3.31), - pargas: Lat. porcus, etc.
Lett. vepris, Boh. vep¥, Pol. wieprz : ChSi. veprt, Lat. aper ‘wild ) (3.31), + Gper boar’, etc.
$s or avs with 6 or
Digitized by Arya Samaj Foundation Chennai and eGangotri
ANIMALS 163
6. SCr. brav (also ‘sheep’), Russ.
borov, etc., with various applications in Slavic (Boh. brav ‘small cattle, sheep, swine’) prob. from the root of Chsl. brati ‘fight’, orig. ‘strike’, Lat. ferire ‘strike, cut’, etc., here as ‘castrate’. Cf. ON borgr, etc. (above
```


### [2026-09-06T15:50:27.685Z] TOOL RESULT

```
=== SYN 1201 ===
ormation parallel 8 replacing the older zawisé. Britckn 646, 656. 2 ie
7. Skt. irsyd-, Av. arasi-, aras a Skt. ars- ‘be jealous, envy’, AV- ann ‘envious’, OS irri, OE trre ‘angry 1 (16.42). Walde-P. 1.150.
a, u~
greizsirdigs
gm oTION: TE
Digitized by Arya Samaj Foundation Chennai and eGangotri
MPERAMENTAL, MORAL, AESTHETIC NOTIONS 1141
16.45 SHAME (sb.)
; Goth. gariudez (aiwiski, Lith. géda y, alba aloxuvn skanda) Lett. kauns Gt: (erp0™ ON kinnrodt ChSl. studi, sramit wpm] 5 Dan. skam SCr. __stid, sram . pudor, ver éoundia Sw.  skam Boh. stud It vergogna OE sceamu Pol. wstyd, wslydliwos¢ a honte ji ME _ shame Russ. styd, stydlivost’ Sp. el NE poke Skt. lajja-, hri-, vrida- um. Tut ire Du. _ schaamte Av. _—_ fiarama- i ane ae OHG coe sake Rite ockel d- MHG _scham(e), scham(e)de W. ane et NHG  scham
Br. mez
Most of the words listed ae used not oily for the subj. sense of ‘shame’, but also or even more commonly for the obj. shame, dishonor, disgrace’ (note the econdary differentiation in NHG scham ys, schande).
In some an earlier sense of ‘respect, reverence or modesty’ led to ‘shame’ in a good sense. In others, as shown by usage or etymology or both, ‘shame’ in a bad sense was the primary notion. Thus, for example, Grk. aldws and alcxtvy are contrasted in origin and in their prevail- ing usage. Several are connected with words for ‘red’ through ‘blushing’ as a sign of shame.
1. Grk. aléés, mostly ‘shame’ in good ny ee ipa modesty’, iG te Hat, eS be ashamed, a mee) respect’, prob. : Goth.
m Tevere’, Skt. id- ‘praise, suppli-
) ° ho ft. *ais-d-, extension of *ais- in Meco: NHG ehre ‘honor’, etc.
. I ee Boisacq 22. Feist 27 f. bona” na mx vn, beside aloxivw ‘dis- ; an pate dishonored, feel shame’, ‘ithe shame, disgrace’, prob. fr. race! aa ot - Mwiski ‘a shame, dis- Coe Bwisc ‘dishonor, offense’, Piz Ugly, Tepulsive’, etc. Walde- Gk. ae 30. Feist 30, tet : ne 7 in a Grk. Tespect, ‘ N ea, umiliation , NT OUP, algo ¢ ame’: &rpémw ‘turn
0 Put to shame’ (NT, etc.),
used mostly in mid. ‘hesitate’ and ‘give heed to, respect, reverence’ (Hom.+), later ‘feel shame’ (Polyb., NT), as reg. in NG.
2. Lat. pudor (also ‘modesty’ as most- ly the borrowed Romance words, It. pudore, Fr. pudeur, etc.), with vb. im- pers. pudet ‘feels ashamed’, prob. as orig. ‘feel repulsed or cast down’ : repudium ‘divorce, repudiation’, tri-pudiwm ‘a cer- tain dance’, etc., those fr. the root of’ pavire ‘beat, stamp’ (or: pés, pedis
‘foot’?). Walde-P. 2.12. Ernout-M. 761, 820. Lat. verécundia, also ‘bashfulness,
modesty’ (> It. vergogna, Sp. verguenza; Fr. vergogne obs.), beside verécundus ‘ashamed, bashful, modest’, fr. veréri ‘feel awe of, be afraid (religious sense)’ : OE wer ‘careful’, warian ‘preserve, pro- tect’, etc. Walde-P. 1.284. Ernout-M. 1089.
Fr. honie, fr. the Gmce., Frank. *hau- nipa fr. vb. *haunjan (> Fr. honnir) : OHG hénen ‘despise, dishonor’, Goth. haunjan ‘debase’, hauns ‘humble’, etc. REW 4080. Feist 249. Weigand-H. 1.881.
Rum. rusine, fr. rugt, rogi (now in-rogi) ‘redden, make red’, refl. ‘b
```


## [2026-09-06T15:50:37.168Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN NR=207 (printed 173) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==207' SYN.txt | head -40\necho \"############ SYN NR=1235 (printed 1201)\"\nawk 'BEGIN{RS=\"\\f\"} NR==1235' SYN.txt | head -40",
 "description": "Buck pages 173 and 1201"
}
```


### [2026-09-06T15:50:39.087Z] TOOL RESULT

```
=== SYN NR=207 (printed 173) ===
h. kilpet ‘womb’, OE cild ‘child’, etc. Walde-P. 1.614. Falk-Torp 593, 430. Cf. ON hiann ‘block’ and ‘young bear’, NE cub: Norw. kubbe ‘block, stump’.
5. Lith. kumelys, Lett. kumelg, see 3.41, under ChSl. konji.
6. ChSl. Zrébe, etc., the general Slavic word : Grk. Bpédos ‘fetus, babe, young of an animal’. Walde-P. 1.689. Briick- ner 666.
7. Skt. kigora-, etym.?
CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
172 SELECTED INDO-EUROPEAN SYNONYMS
3.46 ASS, DONKEY
Grk. —bvos -Goth. asilus Lith. asilas NG = yatdapos, yatdotpl ON asni Lett. ezelis youdpt Dan. assel ChSl.  osilit Lat.  asinus Sw. dsna SCr. osao, magarac Tt. asino, somaro OE assa, esol , Boh.  osel Fr. ane ME asse Pol. osiot Sp. asno, burro NE donkey, ass Russ. osel Rum. asin, mdgar Du. ezel Skt. gardabha-, rdsabha- iin asan OHG  esil Av. xara-, ka9wa- Nir. asal MHG sel W. asyn NHG esel Br. azen
The majority of the European words for ‘ass, donkey’ are derived, mostly through Latin, from some Asiatic name for this animal, the appearance of which in Europe was relatively late. Other words reflect the function of the ass as ‘beast of burden’, or sometimes other characteristics such as ‘lascivious’ or ‘harsh braying’. Schrader, Reallex. 1.271.
1. Grk. dvos (prob., see below), Lat. asinus, loanwords fr. some Asiatic source, ultimately prob. the same word as Su- merian ansu ‘ass’. Schrader lic. Er- nout-M. 79. Walde-H. 1.72 ff.
Lat. asinus, or in part dim. asellus, is the source of the common European words, the Romance, Celtic, Gme. (ON asni, Sw. asna fr. OF r. asne; Dan. esel fr. LG or HG; OE assa perh. fr. Ir. asan) and, through Gmc., the Balto- Slavic.
2. Grk. évos is prob. fr. the same source as Lat. asinus, though the precise phonetic relation is obscure. The old view that it belongs with Lat. onus ‘load, burden’ (cf. NG youapt, It. soma- ro, below) has recently been revived by Grégoire, Byzantion 13.288 ff.
NG yatdapos, yaidépu, yatdotpr, fr. yatdapioy occurring in pap. of the 6th to 8th cent. a.p., parallel to a gaydor in a 4th cent. Talmudic text, with somewhat
similar forms in other Semitic writings, doubtless a word of Asiatic origin, pre- cise source uncertain. Hatzidakis Mec. 2.560 with references.
NG yopép., fr. neut. of adj. youdprs, deriv. (suffix fr. Lat. -drius) of class. Grk. youos ‘load’. Cf. It. samaro (below, 3), NG dial. Bacrayé(s), Bacrayovp, and goprixe ‘donkey’, fr. adjs. Bacrayés (: Bao- Taf ‘carry’) and ¢oprixds (: dopriov ‘load’). G. Meyer, Alb. Etym. Wtb. 127. D. Georgacas, ’A@nva 51.71 ff.
3. It. somaro (usual word for ‘donkey’ in parts of Italy; cf. R. A. Hall, Jr., Lan- guage 19.136), like Fr. sommier, OE séamere, OHG saumari ‘pack horse’ or ‘mule’), fr. late Lat. sagma
############ SYN NR=1235 (printed 1201)
s, drqsus ayabbs ON djarfr, hraustr Lett.  dii8igs, druoks NG dvrpetos, -yevvatos Dan. tapper,modig . ChSl. — driizti, chrabiirt, Lat. fortis, animdsus, au- Sw. tapper, modig SCr. _hrabar, odvaan daz OE beald, céne, médig, Boh. udatny, staletny It. bravo, coraggioso dyrstig Pol. odwazny, waleczny, Fr. brave, courageux ME bold, keene, modi, meiny Sp. bravo, valiente corageus Russ. chrabryj Rum. viteaz, brav, curagios NE brave, courageous Skt. ¢tira-, vira- Ir. dana, essamin (gal Du. dapper, moedig, koen Av. Girya-, dar&i-, dar’yu- sb.) OHG  kuoni, bald Nir. _calma, crodha MHG kriene, balt, ° tiirstic, W. dewr, gwrol muotec Br. kalonek, kadarn NHG tapfer, mutig, kiihn
Some of the words listed are used only in the good sense, as terms of approval, like NE brave, while others are used also, or some of them more usually, in the bad sense, with feeling of reproof, ‘bold, rash’
Several are in origin ‘daring’, cognate with verbs for ‘dare’. Others are de- rived from words for ‘spirit, soul’, ‘mood’, or ‘heart’ through the notion of ‘cour- age’; or as originally ‘manly’ from words for ‘man’; or as ‘fearless’ from ‘fear’. Still others are words for ‘strong, mighty’, ‘firm, steadfast’, ‘skilful’, ‘good’ etc., either used also as common expres- sions for ‘brave’ or definitely specialized in this sense. A few are connected with words for ‘war’, ‘anger’, or ‘blood? (through ‘cruel’).
1. Grk. @pacts (most often in bad sense ‘bold, rash’, but also in good sense ‘brave, bold’ as of Hector and others in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Hom.) : dapcéw ‘dare’, Odpoos ‘courage’, ete. (16.51).
Grk. rodunpéds (poet. also roApjes), deriv. ‘of 76\ua ‘courage, daring’ : roAuaw ‘dare’ (16.51).
Grk. ayafés ‘good’ (16.71) used also for ‘brave’ (Hom.+), as conversely xaxés ‘bad’ for ‘cowardly’ (16.55).
Grk. davépetos ‘manly’ (fr. avqp, avbpés ‘man’) in NG reg. ‘brave’, with avdpela ‘bravery, courage’.
Grk. yevvatos ‘high-born, noble, ¢x- cellent’ (fr. yévva ‘birth, descent’), NG ‘noble’ but esp. ‘brave’.
2. Lat. fortis ‘strong’ (4.81), and esp., as mentally strong, ‘brave’. oo
Lat. animosus, fr. animus ‘soul, spirit, mind, etc.’ (16.11), and hence ‘spirit, courage’. F
Lat audax (more often ‘bold’ in bad sense) : audére ‘dare’ (16.51).
Sp. bravo, ‘wild’ in OSp., later
‘brave’
sense > It. bravo > Fr. prav), fr. Lat. barbarus orig. ‘foreign, a foreigner’, id. REW 945. Gamill-
1080 teal coraggio (fr. Prov. corat-
ge ‘courage’, derivs. of Fr. tc. ‘heart’. REW 2217. j i Iso It.
nie (and in this sense a 4 a yaillant > ME vailant, NE
yaliant), PP qloir) ‘be wor be good for’. REW 9130.
Rum. viteaz, as sb. ‘hero’, fr. th
```


## [2026-09-06T15:50:51.584Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN xratu ===\"; grep -n \"xratu\\|xratu-\" SYN.txt | head\necho \"=== SYN xara ===\"; grep -n \"xara-\" SYN.txt | head\necho \"=== which leaf has xratu ===\"; awk 'BEGIN{RS=\"\\f\"} /xratu/{print NR\": \"substr($0,1,200)}' SYN.txt | head",
 "description": "grep Buck for xratu/xara"
}
```


## [2026-09-06T15:50:53.336Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 hard ===\"; grep -n \"hardus\\|OE. heard\" KLN_1966.txt | head -20\necho \"=== KLN cancer ===\"; grep -n -i \"cancer, n\\.\\|carcro\\|karkinos\" KLN_1966.txt | head -20",
 "description": "grep Klein for hard and cancer"
}
```


### [2026-09-06T15:50:53.529Z] TOOL RESULT

```
=== SYN xratu ===
=== SYN xara ===
4639:Grk. —bvos -Goth. asilus Lith. asilas NG = yatdapos, yatdotpl ON asni Lett. ezelis youdpt Dan. assel ChSl.  osilit Lat.  asinus Sw. dsna SCr. osao, magarac Tt. asino, somaro OE assa, esol , Boh.  osel Fr. ane ME asse Pol. osiot Sp. asno, burro NE donkey, ass Russ. osel Rum. asin, mdgar Du. ezel Skt. gardabha-, rdsabha- iin asan OHG  esil Av. xara-, ka9wa- Nir. asal MHG sel W. asyn NHG esel Br. azen
17085:Grk. — (xara-)5tw (a, b, mid. Goth. siggan (b), saggjan Lith. grimsti (b), gramz- a
=== which leaf has xratu ===
```


### [2026-09-06T15:50:53.609Z] TOOL RESULT

```
=== KLN 1966 hard ===
1494:acratia,  n.,  weakness  (med.)  —  Medical  L.,  fr. Gk.  4xpaxsia,  ‘want  of  power’,  fr.  a-  (see priv.  pref.  a-)  and  xp4xop,  ‘strength,  power, rule’,  which  is  cogn.  with  Goth,  hardus,  OE. heard,  ‘hard’.  See  hard  and  cp.  -cracy,  -crat.  For the  ending  see  suff.  -ia.
5679:Derivatives:  Brobdingnag-ian,  adj.  and  n. brocade,  n.,  a  rich  figured,  woven  fabric.  —  Sp. brocado,  fr.  broca,  fr.  ML.  broccare,  ‘to  prick, emboss’,  fr.  L.  broccus,  ‘projecting’  (said  esp. of  teeth).  Cp.  It.  broccato,  F.  brocart,  and  see broach,  n.  For  the  ending  see  suff.  -ade. Derivatives:  brocade,  tr.  v.,  brocad-ed,  adj. brocard,  n.,  a  law  maxim.  —  F.  brocard,  fr.  ML. brocardus,  of  s.m.,  fr.  Brocardus,  fr.  Burchardus, G  Burckard,  bishop  of  Worms,  who  in  the  1st half  of  the  nth  cent,  compiled  an  ecclesiastical canon.
6333:cancer,  n.,  a  malignant  growth.  —  L.,  ‘crab,  ul¬ cer,  cancer’,  dissimilated  fr.  *carcro-  and  cogn. with  Gk.  xxpxlvos,  ‘crab’,  lit.  ‘the  animal  with the  hard  shell’,  fr.  I.-E.  base  *qarq-,  *qraq-,  ‘to be  hard’,  whence  also  OI.  karkatakt,  karkah, ‘crab’,  karkarah ,  ‘hard’.  Cp.  OSlav.  rakii,  ‘cray¬ fish’,  OPruss.  rakis,  of  s.m.,  which  were  prob. dissimilated  fr.  *krak-  \  cp.  also  W.  crach,  ‘crust’, craig,  ‘rock’,  Mir.  crach ,  ‘hard’,  fr.  *qraq-.  Cp. also  I.-E.  base  *< jar-tu-,  ‘hard,  strong’,  whence Gk.  xpaT'ic,  ‘strong’,  Goth,  hardus,  OE.  heard, ‘hard’.  See  hard  and  cp.  canker,  carcinoma, chancre.  Cp.  also  kunkur.
9522:xpaxoi;,  ‘strength,  might,  power,  rule,  sway,  do¬ minion’  (whence  xpaxsxv,  ‘to  be  strong,  rule over’,  xpxxup,  ‘strong,  mighty’),  which  is  cogn. with  Goth,  hardus,  ‘hard’,  OE.  heard,  ‘hard, brave’.  See  hard  and  cp.  acrasia,  acratia  and  the first  element  in  Crataegus, cradge,  n.,  a  small  bank  raised  to  prevent  over¬ flow  of  water.  —  F.  creche,  ‘crib,  cradle’,  fr. Frankish  *kripja ,  which  is  rel.  to  OHG.  krippa, OE.  cribb,  ‘crib’.  See  crib  and  cp.  cratch,  creche. Derivative:  cradge,  tr.  and  intr.  v. cradle,  n.  —  ME.  cradel,  fr.  OE.  cradel,  cradol, rel.  to  OE.  creel,  ‘cart’,  and  to  OHG.  kratto, ‘basket’,  OHG.  chrezzo,  MHG.  krezze,  of  s.m., G.  Krdtze,  ‘basket  carried  on  the  back’,  and cogn.  with  OI.  grathndti,  granthdyati,  ‘twists, ties’,  granthah,  ‘knot’.  Cp.  cart.
9573:‘member’  of  a  certain  type  of  government,  as  in democrat.  —  F.  -crate,  fr.  Gk.  -xpdrr t]z,  fr. xpxxcx;,  ‘strength,  power,  rule’.  See  -cracy. Crataegus,  n.,  a  genus  of  plants  of  the  apple  family (bot.)  —  ModL.,  fr.  Gk.  xpaxaiy °?>  ‘thorn’, which  is  compounded  of  xpa-ni?,  ‘strong’,  and -aiyo?,  ‘tree,  oak’.  The  first  element  is  cogn. with  Goth,  hardus,  OE.  heard;  see  hard.  The second  element  is  cogn.  with  L.  aesculus,  ‘the Italian  oak’,  OE.  ac,  ‘oak’;  see  oak  and  cp. Aesculus.
17197:Derivatives :  harbo{u)r-er,  n. bard,  adj.  —  ME.  hard,  fr.  OE.  heard,  rel.  to hearde  (adv.),  ‘extremely’,  OS.,  Du.  hard,  ON. hardr  (adj.),  ‘hard’,  ON.  harda  (adv.),  ‘very’, Dan.  hoard,  Swed.  hdrd,  ‘hard’,  OHG.  harto (adv.),  ‘extremely,  very’,  hard,  herd  (adj.), ‘hard’,  MHG.  harte  (adv.),  ‘very’,  herte  (adj.), ‘hard’,  G.  hart,  Goth,  hardus,  ‘hard’,  fr.  I.-E. base  *qar-,  ‘hard’.  Fr.  I.-E.  *qret-,  *qpt-,  a -/-enlargement  of  base  *qar-,  derive  Gk.  xpa- -05,  Ion.  xapTo?,  Aeol.  xpsToc,  ‘strength’,  Gk. xpa-nii;,  ‘strong’.  Cp.  hardy,  -ard,  arditi,  and  the second  element  in  Bernard,  Everard,  Gerard, Gunther,  Leonard,  Reynard.  Cp.  also  acratia, -cracy,  the  first  element  in  Epicrates,  pancratium. Cp.  I.-E.  *quar-q-,  whence  OI.  karkafah,  ‘crab’, karkarah,  ‘rough,  hard’,  Gk.  xapxlvo;,  ‘crab’, L.  cancer  (dissimilated  fr.  *carcro-),  ‘crab,  ulcer, cancer’.  See  cancer  and  cp.  words  there  referred to.
17198:Derivatives:  hard,  adv.  (q.v.),  hard,  n.,  harden (q.v.),  hardly  (q.v.),  hardship  (q.v.),  hardy  (q.v.) hard,  adv.  —  ME.  harde,  fr.  OE.  hearde,  ‘ex¬ tremely’,  rel.  to  ON.  harda  (adv.),  ‘very’,  OE. heard,  adj.,  ‘hard’.  See  hard,  adj. harden,  tr.  and  intr.  v.  —  ME.  hardnen,  fr.  hard. See  hard,  adj.,  and  verbal  suff.  -en.
17205:make  bold’,  fr.  Frankish  *hardjan ,  ‘to  harden’, which  is  rel.  to  OHG.  herten,  OFris.  he-da, O.N.  herda,  O.S.  herdian,  OE.  hierdan,  Goth. ga-hardjan,  ‘to  harden’,  OHG.  hard,  herd,  OE. heard,  ‘hard’.  See  hard,  adj.,  and  cp.  foolhardy. Derivative:  hardy,  tr.  v.,  to  make  hardy  f  intr.  v., to  become  hardy.
23523:Mercator  Gerhardus,  Flemish  geographer  (1512- 94), _ Latinized  from  his  original  name  Ger¬
=== KLN cancer ===
6333:cancer,  n.,  a  malignant  growth.  —  L.,  ‘crab,  ul¬ cer,  cancer’,  dissimilated  fr.  *carcro-  and  cogn. with  Gk.  xxpxlvos,  ‘crab’,  lit.  ‘the  animal  with the  hard  shell’,  fr.  I.-E.  base  *qarq-,  *qraq-,  ‘to be  hard’,  whence  also  OI.  karkatakt,  karkah, ‘crab’,  karkarah ,  ‘hard’.  Cp.  OSlav.  rakii,  ‘cray¬ fish’,  OPruss.  rakis,  of  s.m.,  which  were  prob. dissimilated  fr.  *krak-  \  cp.  also  W.  crach,  ‘crust’, craig,  ‘rock’,  Mir.  crach ,  ‘hard’,  fr.  *qraq-.  Cp. also  I.-E.  base  *< jar-tu-,  ‘hard,  strong’,  whence Gk.  xpaT'ic,  ‘strong’,  Goth,  hardus,  OE.  heard, ‘hard’.  See  hard  and  cp.  canker,  carcinoma, chancre.  Cp.  also  kunkur.
17197:Derivatives :  harbo{u)r-er,  n. bard,  adj.  —  ME.  hard,  fr.  OE.  heard,  rel.  to hearde  (adv.),  ‘extremely’,  OS.,  Du.  hard,  ON. hardr  (adj.),  ‘hard’,  ON.  harda  (adv.),  ‘very’, Dan.  hoard,  Swed.  hdrd,  ‘hard’,  OHG.  harto (adv.),  ‘extremely,  very’,  hard,  herd  (adj.), ‘hard’,  MHG.  harte  (adv.),  ‘very’,  herte  (adj.), ‘hard’,  G.  hart,  Goth,  hardus,  ‘hard’,  fr.  I.-E. base  *qar-,  ‘hard’.  Fr.  I.-E.  *qret-,  *qpt-,  a -/-enlargement  of  base  *qar-,  derive  Gk.  xpa- -05,  Ion.  xapTo?,  Aeol.  xpsToc,  ‘strength’,  Gk. xpa-nii;,  ‘strong’.  Cp.  hardy,  -ard,  arditi,  and  the second  element  in  Bernard,  Everard,  Gerard, Gunther,  Leonard,  Reynard.  Cp.  also  acratia, -cracy,  the  first  element  in  Epicrates,  pancratium. Cp.  I.-E.  *quar-q-,  whence  OI.  karkafah,  ‘crab’, karkarah,  ‘rough,  hard’,  Gk.  xapxlvo;,  ‘crab’, L.  cancer  (dissimilated  fr.  *carcro-),  ‘crab,  ulcer, cancer’.  See  cancer  and  cp.  words  there  referred to.
```


## [2026-09-06T15:51:11.453Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins kar-1 ===\"; grep -n -A12 \"^kar-1\\|^kar-\\b\" AHD_watkins1985.txt | head -40\necho \"=== AHD watkins kret ===\"; grep -n \"krat\\|kret-\\|hardus\" AHD_watkins1985.txt | head -20",
 "description": "grep Watkins AHD"
}
```


### [2026-09-06T15:51:11.522Z] TOOL RESULT

```
=== AHD watkins kar-1 ===
584:kar-2, To praise loudly, extol. Hypothetical base form. 1. Perhaps Germanic *hrém- in Dutch roemen, to praise: RUMMER. 2. Lengthened-grade form *kdru- in Greek (Doric) karux, (Attic) kérux, herald: capucEvs. [Pok. 2. kar- 530.]
585-[karlaz. Man. Germanic root. 1. Old English ceor/, man, churl: CHURL. 2. Old Norse karl, man, freeman: CARL, CARLING. [In Pok. ger- 390.]]
586-kars-. To card. 1. Latin cdrere, carrere, to card wool (> carmen, a card for wool): CARMINATIVE. 2. Perhaps Latin carduus, thistle, artichoke: CARD?, CARDOON, (CHARD). [Pok. kars- 532.]
587-kas-. Gray. 1. Germanic *has6én-, *hazdn- in Old English hara, hare: HARE. 2. Suffixed form *kas-no- in Latin cdnus, white, gray, grayed hair: CANESCENT. [Pok. kas- 533.]
588-kat-1. Something thrown down; offspring. 1. Possibly Greek kata, down: CATA-; CATHEPSIN. 2. Suffixed form *kat-olo- in Latin catulus, young puppy, young of ani- mals: CADELLE. [Pok. 2. kat- 534.]
589-kat-2. To fight. Suffixed form *kat-u- in Old Irish cath, battle: KERN!. [Pok. kat- 534.]
590-kau-'. To howl (imitative). 1. Reduplicated suffixed form *ka-kau-ro- in Sanskrit cakorah, partridge: CHUKAR. 2. Reduplicated form *k6-kii-o- in Greek kdkuein, to wail, lament: Cocytus. [Pok. kau- 535.]
591-kau-2, To hew, strike. 1. Germanic *hawwan in: a. Old English héawan, to hew: HEW; b. Old Norse héggva, to cut: HAGGLE; c. Old ‘French hove, a hoe: HOE. 2. Ger- manic *hawwé6 in Old Norse hégg, a gap, a cutting blow, akin to the source of HAG?. 3. Germanic *haujam in Old English hieg, hay, cut grass: HAY. 4. Suffixed form *kau-do- in Latin ciidere (< *caudere), to strike, beat: incus. [Pok. kdu-, 535.]
592-kaul-. Stalk, stem. Latin caulis, stalk, stem, cab- bage-stalk, cabbage: CAULICLE, CAULINE, COLE, KALE; AMPLEXICAUL, CAULESCENT, CAULIFLOWER, COLCAN- NON, COLESLAW, KAILYARD SCHOOL, KOHLRABI. [Pok. kau-l- 537.)
593-ked-. To go, yield. 1. Lengthened-grade form *kéd- in Latin cédere, to go, withdraw, yield: CEASE, CEDE, CES- SION; ABSCESS, ACCEDE, ACCESS, ANCESTOR, ANTECEDE, CONCEDE, CONCESSION, DECEASE, EXCEED, INTERCEDE, PRECEDE, PREDECESSOR, PROCEED, RECEDE, RETRO- CEDE, SECEDE, SUCCEED. 2. Prefixed and suffixed form *ne-ked-ti-, “from which one cannot draw back” (*ne-, not; see ne), in Latin necesse, inevitable, unavoidable: NECESSARY. [In Pok. sed- 884.]
594-keg-. Hook, tooth. 1. Germanic *hakan- in: a. Old Norse haki, hook, akin to Old English haca, hook: HAKE; b. Middle Low German hake, hook: HARQUEBUS. 2. Ger- manic lengthened form *Adka- in: a. Old English héc, hook: HOOK; b. Middle Dutch hok, hoec, hook: HOOKER}. 3. Germanic *hakila- in Middle Dutch hekel, hatchel, a flax comb with long metal hooklike teeth: HECKLE. 4. Germanic *hakkijan in Old English -haccian, to hack to pieces as with a hooked instrument: Hack!. [Pok. keg- 537.]
595-kei-'. To lie; bed, couch; beloved, dear. I. Basic form *kei-. 1. Suffixed form *kei-wo- in: a. Germanic *hiwa- in Old English hiwan, members of a household: HIND?;
596-kei-?
=== AHD watkins kret ===
532:[grat-. Also krat-. To scratch. Germanic root. 1. Ger- manic *krattén in Middle Dutch cratsen, to scrape: SCRATCH. 2. Germanic *grat- in Old French grater, to scrape: GRATE}; REGRATE. [Pok. gred- 405.]]
583:heard, hard: HARD; b. Frankish *hard, hard, perhaps the source of Old French estandard, rallying place: STAN- DARD; Cc. Old French hardir, to make hard: HARDY}. 2. Extended zero-grade form *krt-es- in Greek kratos, strength, might, power: -cracy. II. Basic form *kar- in derivatives referring to things with hard shells. 1. Possi- bly Latin carina, keel of a ship, nutshell: CAREEN, CARINA. 2. Possibly Greek karuon, nut: KARYO-; EU- CARYOTE, GILLYFLOWER, SYNKARYON. 3. Reduplicated form *kar-kr-o dissimilated to Latin cancer, crab: CAN- CER, CANKER, CHANCRE. 4. Suffixed form *kar-k-ino- in Greek karkinos, cancer, crab: CARCINO-, CARCINOMA; (CARCINOGEN). [Pok. 3. kar- 531.]
644:Latin cinctari, to delay: cuNCTATION. [Pok. kenk- 566, konk- 614.] konk(h)o-. Mussel, shellfish. 1. Greek konkhé, konkhos, mussel, conch: COCKLE!, CONCH, CONCHA, CONCHO-. 2. Greek kokhilos, land snail: cocHLEa. [Pok. konkho- 614.] kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ormo- 615.] koro-. War; also war-band, host, army. I. Germanic *harjaz, army. 1. Old English here, army: HERIOT. 2. Old French herban, a summoning to military service: ARRI- ERE-BAN. 3. Compound *haryja-bergaz, “army hill,” hill- fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-?), in: a. Old English herebeorg (> Middle English herberwe), lodging: HARBOR; b. Old French herberge, lodging: HARBINGER. 4. Compound *harja- waldaz, “‘army commander” (*wald-, rule, power; see wal-), in Anglo-Norman herald, herald: HERALD. II. Ger- manic denominative *harjén in Old English hergian, to ravage, plunder, raid: HARRY. III. Germanic compound *harihring, assembly, “host-ring” (*hringaz, ring; see sker-3), in Medieval Latin harenga, harangue: HA- RANGUE. [Pok. koro-s 615.] koselo-. Hazel. Germanic *haselaz in Old English hesel, hazel: HAZEL. [Pok. kos(e)lo- 616.] kost-. Bone. Probably related to ost-. Latin costa, rib, side: COAST, COSTA, COSTARD, COSTREL, CUESTA, CUTLET; ACCOST, INTERCOSTAL, STERNOCOSTAL. [Pok. kost- 616.] krau-. Also kru-. To conceal, hide. Suffixed extended form *krup-yo- in Greek kruptein, to hide: CRYPT, CRYP- TIC, CRYPTO-, KRYPTON; APOCRYPHA. [Pok. krd(u)- 616.] kred-. Framework, timberwork. Possible root. Germanic *hr6(d)-st- in Old English hrést, roost: Roost. [Pok. kred- 617.] krei-. To sieve, discriminate, distinguish. 1. Basic form with variant instrumental suffixes in: a. suffixed form *krei-tro- in Germanic *hridra-, a sieve, in Old English hridder, hriddel, sieve: RIDDLE}; b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GAR- BLE. 2. Suffixed form *krei-men- in (i) Latin crimen, judgment, crime: CRIME; RECRIMINATE (ii) Latin discri- men, distinction (dis-, apart): DISCRIMINATE. 3. Suffixed zero-grade form *kri-no- (participial form *kri-to-) in Latin cernere (past participle certus), to sift, separate, decide: CERTAIN; CONCERN, DECREE, DISCERN, EXCRE- MENT, INCERTITUDE, RECREMENT, SECERN, SECRET. 4. Suffixed zero-grade form *kri-n-yo- in Greek krinein, to separate, decide, judge (> krinesthai, to explain): CRISIS, CRITIC, CRITERION; APOCRINE, DIACRITICAL, EC- CRINE, ENDOCRINE, EPICRITIC, EXOCRINE, HEMATOCRIT, HyYPrROCcRISY. [Pok. 4. sker-, Section II. 945.] krek-1. To weave, beat. 1. Germanic *hreh-ulaz in Old English hréol, reel, spool for winding cord: REEL. 2. Suf- fixed o-grade form *krok-u- in Greek krokus, nap of cloth: CROCIDOLITE. [Pok. 1. krek- 618.] krek-2. Frog spawn, fish eggs. Germanic *hrog- in Middle English row, roe: ROE}. [Pok. 2. krek- 619.] krem-. Wild garlic, onion. O-grade form *krom- in Ger- manic *hram- in Old English hramsan, onion, garlic: RAMSON. [Pok. kerem- 580.] kret-'. To shake. O-grade form *krot- in Germanic *hra- thaz, swift, nimble, in Old English hreth(e), nimble, quick, prompt, ready: RATHE, (RATHER). [Pok. 1. kret- 20.
645:kret-2. To beat. O-grade form *krot- in Greek krotein, to strike, beat: DICROTISM, TRICROTIC. [Pok. 2. kret- 621.] kreue='. Raw flesh. 1. Lengthened-grade form *kréw- in Germanic *hréwaz in Old English hréaw, raw: RAW. 2. Suffixed form *krewo-s- in Greek kreas, flesh: CRE- ATINE, CREODONT, CREOSOTE, PANCREAS. 3. Suffixed zero-grade form *krii-do- (< *krua-do-) in: a. Latin cridus, bloody, raw: CRUDE; ECRU, RECRUDESCE; b. Lat- in cridélis, cruel: CRUEL. [Pok. 1. A. kreu- 621.]
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
2162:RATHE kret-1 RATHER kret-1 RATHSKELLER  at-, kel-2 RATIO af-
2361:TERRESTRIAL ters- THRESH tera-! TORTICOLLIS kWel-1, terkw- TRICERATOPS ker-1 TERRE-VERTE ters-, virére THRESHOLD tere-1 TORTUOUS terkw- TRICHINA  thrix TERRIBLE tres- THRICE trei- Tory ret- TRICHO-  thrix TERRICOLOUS ters- THRILL tere-2 TOTAL teuta- TRICHOME _ thrix TERRIER ters- THRONE dher-2 TOUGH denk- TRICHOTOMY _ trei- TERRIFIC tres- THROSTLE trozdo- TOUPEE tap- -TRICHOUS _ thrix TERRIGENOUS §ters- THROUGH tere-2 Tow! deuk- TRICHURIASIS ors- TERRITORY ters- THROW tere-1 Tow? taw- TRICLINIUM klei-, trei- TERROR tres- THRUM?2 ter- TOWN dhino- TRICORN ker-1 TERTIAN trei- THRUSH! trozdo- TOXIC tekw- TRICROTIC  kret-2, trei-
```


## [2026-09-06T15:51:12.413Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN xar donkey ===\"; grep -n \"Esel\" HRN.txt | head -20\necho \"=== HRN Dorn ===\"; grep -n \"Dorn'\" HRN.txt | head -20",
 "description": "grep Horn for Esel/Dorn"
}
```


### [2026-09-06T15:51:12.474Z] TOOL RESULT

```
=== HRN xar donkey ===
2266:*Eselsziege' nach einem gr. ^ovorqayo^ gebildet.
4298:47o. y/fi' 'Esel*, yj^ryö^ *Hase' (^^ *Eselsohr K /ercür, /«fr^^fAr«?
4300:aw. /ara- 'Esel : phlv. /ar: skr. khara- 'Esel'.
4306:. y^erbuze, /erbtu^) *Melone' (wörtl. *Eselsgurke').
7417:'Eselswurm'.
=== HRN Dorn ===
```


## [2026-09-06T15:51:19.633Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '580,584p' AHD_watkins1985.txt",
 "description": "Print Watkins kar-1 full"
}
```


### [2026-09-06T15:51:19.674Z] TOOL RESULT

```
kan-
BIT), GAMBOL, (GAMBREL), (GAMMON3), (JAMB). 2. Suf- fixed form *kamp-ulo- in Greek kampulos, bent: CAMPYLOTROPOUS. [Pok. kam-p- 525.] kan-. To sing. 1. Germanic *han(e)ni in Old English hen(n), hen: HEN. 2. Latin canere, to sing (> cantdre, to sing): CANOROUS, CANT?, CANTABILE, CANTICLE, CANTIL- LATE, (CANTO), CANTOR, CANZONE, CHANT; ACCENT, DESCANT, ENCHANT, (INCANTATION), INCENTIVE, PRE- CENTOR, RECANT. 3. Latin oscen, a singing bird used in divination (< *obs-cen, “one that sings before the au- gurs”; ob-, before; see epi): OSCINE. 4. Suffixed form *kan-men- in Latin carmen, song, poem: CHARM}. [Pok. kan- 525.] kand-. To shine. 1. Suffixed (stative) form *kand-é- in Latin candére, to shine: CANDENT, CANDID, (CANDIDA), (CANDIDATE), CANDLE, CANDOR; INCANDESCE. 2. Latin transitive *candere, to kindle, in compound incendere, to set fire to, kindle (in-, in; see en): (INCENDIARY), IN- CENSE. [Pok. kand- 526.] kannabis. Hemp. Late Indo-European word borrowed from an unknown source. 1. Germanic *hanipiz in Old English henep, henep, hemp: HEMP. 2. Greek kannabis, hemp: CANNABIS, (CANVAS). kanto-. A corner, a bending. Celtic *cantos, rim, border, in Latin cantus, canthus, iron ring around a carriage wheel, a wheel, rim (> Italian canto, corner): CANTEEN, CANTON; DECANT. [Pok. kan-tho- 526.] kap-. To grasp. I. Basic form *kap-. 1. Germanic *haf- in Old English hefeld, thread used for weaving, heddle (a device which grasps the thread): HEDDLE. 2. Germanic *haftjam in Old English heft, handle: Harr. 3. Form *kap-o- in Germanic *habai-, *habén in Old English habban, to have, hold: HAVE. 4. Germanic hafigaz, “containing something,” having weight, in Old English hefig, heavy: HEAVY. 5. Germanic *hafnd-, perhaps “place that holds ships,” in Old English hefen, a haven: HAVEN. 6. Germanic habukaz in Old English h(e)afoc, hawk: HAWK}, 7, Latin combining form -ceps (< *kap-s), “taker.” II. Suffixed form *kap-yo-. 1. Germanic *hafjan in Old English hebban, to lift: HEAVE. 2. Latin capere, to take, seize, catch: CABLE, CAPABLE, CAPACIOUS, CAPIAS, CAPSTAN, CAPTION, CAPTIOUS, CAPTIVATE, CAPTIVE, CAP- TOR, CAPTURE, CATCH, (CHASE!); ACCEPT, ANTICIPATE, CONCEIVE, DECEIVE, EXCEPT, INCEPTION, (INCIPIENT), INTERCEPT, INTUSSUSCEPTION, MUNICIPAL, NUNCUPA- TIVE, OCCUPY, PARTICIPATE, PERCEIVE, PRECEPT, RE- CEIVE, (RECOVER), RECUPERATE, (RX), SUSCEPTIBLE. III. Suffixed form *kap-s- in Latin capsa, repository, case: CAISSON, CAPSICUM, CAPSID, CAPSULE, CASE2, CHASE?, CHASES, CHASSIS, CHESS?; ENCHASE. IV. Length- ened-grade variant form *kdép-. 1. Germanic *hof- in compound *bi-hdf, “that which binds,” requirement, obligation (*bi-, intensive prefix; see ambhi), in: a. Old English behdf, use, profit, need: BEHOOF; b. Old English behéfian, to have need of: BEHOOVE. 2. Greek k6pé, oar, handle: copePpop. Compare ghabh-. [Pok. kap- 527.] kap(h)o-. Hoof. Lengthened-grade form kdp(h)-o- in Germanic *héfaz in Old English Adf, hoof: Hoor. [Pok. kapho- 530.] kapro-. He-goat, buck. Latin caper, he-goat (> capra, she-goat): CABRILLA, CABRIOLET, CAPELLA, CAPRIOLE, CHEVRON; CAPRIC ACID, CAPRICORN, CAPRIFIG, CAPROIC ACID. [Pok. kapro- 529.] kaput. Head. 1. Germanic *haubidam, *haubudam, in Old English héafod, head: HEAD. 2. Latin caput, head (> Italian capo, head): CABEZON, CADET, CAPE?, CAPITAL, CAPITAL, CAPITATE, CAPITATION, CAPITELLUM, CAPITU- LATE, CAPITULUM, CAPO!, CAPRICE, CAPTAIN, CATTLE, CAUDILLO, CHAPITER, CHAPTER, CHIEF, CHIEFTAIN; BI- CEPS, CHAMFRON, DECAPITATE, KERCHIEF, MISCHIEF, OCCIPUT, PRECIPITATE, RECAPITULATE, SINCIPUT, TRI- ceps. [Pok. kap-ut- 529.] kar-', Hard. I. Variant form ker-. 1. Suffixed o-grade form *kor-tu- in Germanic *harduz in: a. Old English hard,
kei-'
heard, hard: HARD; b. Frankish *hard, hard, perhaps the source of Old French estandard, rallying place: STAN- DARD; Cc. Old French hardir, to make hard: HARDY}. 2. Extended zero-grade form *krt-es- in Greek kratos, strength, might, power: -cracy. II. Basic form *kar- in derivatives referring to things with hard shells. 1. Possi- bly Latin carina, keel of a ship, nutshell: CAREEN, CARINA. 2. Possibly Greek karuon, nut: KARYO-; EU- CARYOTE, GILLYFLOWER, SYNKARYON. 3. Reduplicated form *kar-kr-o dissimilated to Latin cancer, crab: CAN- CER, CANKER, CHANCRE. 4. Suffixed form *kar-k-ino- in Greek karkinos, cancer, crab: CARCINO-, CARCINOMA; (CARCINOGEN). [Pok. 3. kar- 531.]
kar-2, To praise loudly, extol. Hypothetical base form. 1. Perhaps Germanic *hrém- in Dutch roemen, to praise: RUMMER. 2. Lengthened-grade form *kdru- in Greek (Doric) karux, (Attic) kérux, herald: capucEvs. [Pok. 2. kar- 530.]
```


## [2026-09-06T15:51:21.056Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4290,4320p' HRN.txt\necho \"=== HRN xara/xar entries around ===\"\ngrep -n \"yär\\|yara\\|/ara-\\|yärä\" HRN.txt | head -30",
 "description": "Horn context"
}
```


### [2026-09-06T15:51:21.111Z] TOOL RESULT

```
schon an .>icii wenig Überzeugendes, ganz abgesehe
von der falschen awesti:?chen Xominativbildung.
47:i. yJrätnJden 'schreiten, ^ehen".
ai. l h'ntut'. knlwftfi. hrt'n/Uitr 'gehen, schreiten'.
In der Bedeutung angenehm, erfreuend* etc. ist,
wie schon Vullers gesehen hat. /jrüm ursprünglich
yu/rem. eine Ansicht, der auch Xöldeke beipflichtet
(mündliche Mitteilung».
47o. y/fi' 'Esel*, yj^ryö^ *Hase' (^^ *Eselsohr K /ercür, /«fr^^fAr«?
u. a. m.
aw. /ara- 'Esel : phlv. /ar: skr. khara- 'Esel'.
kurd. ier, liar (GuränT): SLfy./ar: oss. /ßräg, x^*'^9
(2i)7); bei. n. ffar, /ar, LW. har^) (192); wa/. ;rwr,
«ar. cer, üer, sangl. //tr, minj. xara.
*j Vcrgl. Ilorn, ZDMG. 44, 675, No. 134.
•; Vcrgl. Barthol oniao, ZDMG. 44, 550.— 105 —
. y^erbuze, /erbtu^) *Melone' (wörtl. *Eselsgurke').
phlv. /arböjhia, kharbuzak (PP61.), vergl. höjlna =
/iyär (ebendas.) und bujpa (BQ.) d. i. bäjinä, htijina
V
(FS); die letzteren beiden neupersischen Worte sind
nur Fehle vlumschriften, noch mit aramäischem -a.
Vergl. NT2il2, de Lagarde, Semitica 56.
Weit gewandert, vergl. türk. qarpuz etc.
>. y^ereeuf/ *Krebs', vergl. kilinjar, kulenöek (Wo Ilaston:
karanjäl, kalanjär).
skr. vergl. karkiffa- 'Krebs, Krebs im Tierkreise'
(karkä- etc. sind bedenklich) ; phlv. karcany 'Krebs im
Tierkreise (Bund.); gr. -^nQy.lvo^ 'Krebs', vergl. md^j/ar
yjumi'oi 2itY.t\oi , Hesych.; lat. Cancer wird ebenfalls
dazu gehören (vergl. Brugmann, Grundriss, I, § 282
=== HRN xara/xar entries around ===
517:afsöi^ra-^ a/stacin-^ awMäta-, awzdäna-^ äfsbyäriyti'^
744:36. üyärden, ayäriden Verschlingen*.
1444:') Das Pehlevi hat auch schon andarün (für aw. aw/ara-).- 28 -
1995:np. but in dieselbe Kategorie wie gStl^ ätes, petyäre
2277:217. hes Viel, genug, vergl. bisyär.
2791:284. petyäre 'Unglück' etc. (Vis und Rämin, Seite 81,
2793:aw. paitt/ara- 'Gegenschöpfung'; phlv. patyardk,
2794:püyärak (Men., K 43).
3319:aw. '^para,yär' (+ säl),
3379:358. peiyäre 'Tadel' (Sahn. III, 1763, V. 95; 1803, V. 383)^).
4300:aw. /ara- 'Esel : phlv. /ar: skr. khara- 'Esel'.
4308:/iyär (ebendas.) und bujpa (BQ.) d. i. bäjinä, htijina
4467:aw. hareöis; phlv. havak bezw. yarah^ vd. 2 (89).
4577:t. yärin (308); bei. varag, n. varay (404); si/n. minj.
5852:Urverwandt mit afy. zyara * Kettenpanzer', oss. zyär
6088:man sonst seryär erwarten müsste.
6643:kurd. dausCf slzdeh (LW.); afy. dyärlas.
6978:798. sehryär 'Herrscher*.
7701:Vers 852), Praes. yär-em (unbelegt) ^) ; gesten, Praes.
7934:kurd. girin weinen ; oss. d. yär, t. qär 'Geschrei,
8049:kurd. gerü 'Kehle'; af}'. yäre; oss. gm' (166; un-
8083:kurd. gilt 'Klage', gire 'Streit'; oss. d. yärziin, t.
8143:LW. kurd. gör; afy. yyara; bei. gör 'Wildesel' (80).
9628:aw. yär-, ap. -yära-.
9660:Wl21. yär 'Freund', yärl-, yärwer (Sahn. I, 126 Vers 1117).
9664:phlv. äyär (die Lesung scheint durch haniäyär, z. B.
9678:41H Note 2) nur auf einer falschen Päzendlesung? Aber np. yärer?\
9680:aber ohne Erfolg, da er np. yärwer nicht kennt.
9684:Suffixes -yär - vergl. beytyür 'glücklich* , hösyär
9685:Verständig', däwyär * Jäger , sehrydr 'Herrscher u.
```


## [2026-09-06T15:51:32.468Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN Dorn ===\"; grep -n \"Dorn\" HRN.txt | head -20\necho \"=== HRN Granit/harter Stein ===\"; grep -n -i \"granit\\|harter Stein\" HRN.txt | head -10",
 "description": "Horn thorn"
}
```


### [2026-09-06T15:51:32.527Z] TOOL RESULT

```
=== HRN Dorn ===
4213:461. y^ar, x^^^ 'Fels; Dorn 2), x^*'^ (Häliz 16, 3), ;fä£?e?r
=== HRN Granit/harter Stein ===
```


## [2026-09-06T15:51:33.944Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 page tags near 697/729 ===\"; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -5\necho \"=== grep خرد ===\"; grep -c \"خرد\" BQT_v2_pages.txt; echo \"=== grep خارا ===\"; grep -c \"خارا\" BQT_v2_pages.txt",
 "description": "Inspect BQT v2"
}
```


### [2026-09-06T15:51:34.043Z] TOOL RESULT

```
=== BQT v2 page tags near 697/729 ===
=== grep خرد ===
137
=== grep خارا ===
25
```


## [2026-09-06T15:51:38.894Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4205,4235p' HRN.txt",
 "description": "Horn no. 461"
}
```


### [2026-09-06T15:51:38.936Z] TOOL RESULT

```
aw. /an-, Nom. /äo 'Quelle*, vergl. np. xäm (No. 466)
und die folgende Nummer.
460. {2)%ä 'Schulter .
aw. /äo, yt. 10, 71 ; 14, 29 'Schultern'.
Geld n er, Studien I, 173. Doch sind beide Worte
im Neupersischen durchaus unbelegt, und die Über-
setzung von aw. /äo durch 'Schultern (man erwartet
einen Dual) nicht sicher^).
461. y^ar, x^^^ 'Fels; Dorn 2), x^*'^ (Häliz 16, 3), ;fä£?e?r
(aus *;^6Zr^^r ?) 3), x^^P^^^ Igel-
skr. khara- 'hart, rauh; scharf; phlv. /ßr, /drpust
Igel* (Bund.); arm. fear 'Stein*.
462. '^Kitsten 'aufstehen*, Praes.;^e2-e/w (AM. 84 Zeile 2 v. u.),
yeztden [x^ztden).
aw. pairi]./aezayiuha^) erhebe dich'; phlv./ös^ (vd. 16
*) Bartholomae (briefl. MitteiluDg) nimmt nach dem Glieder-
parallelismus (s. Neuausgabe)
erezöis x^o
bäzväo aojö
tnnvö vazdvare
für yäo eine mit aojö und vazdvare ungefähr synonyme Bedeutung an.
*) In der Bedeutung Tenis* in alb. Tcär^ kars (G. Meyer,
Alban. Wörterbuch, 176); auch arm. xw (S. Bu gge, KZ. 32, 9).
») Vergl. Rückert, ZDMG. 10, 166, 167 und dann Vullers zu
V ^^
Sahn. I, 196 Vers 1211 (der Rückert, wie gewöhnlich, nicht nennt).
*) D armestet er, 6t. ir. I, 201 weicht hier von Vullers,
Institutiones, ab und macht die Sache nur schlimmer, indem er mi^
dem Pehlevl-Commcntator auf aw. ^'^Isat *er fing an zu schwitzen* (!)
verfällt.— 103 —
(7) Gl.), rTstjayee, ä/ezJt (Phlv.-Vend. für aw. [^ha/s-;
```


## [2026-09-06T15:51:40.453Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 600 BQT_v2_pages.txt; echo; echo \"=== formfeeds:\"; python3 -c \"\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint(len(d.split(chr(12))))\nimport re\nprint([m for m in re.findall(r'\\[.{0,30}\\]',d)[:10]])\n\"",
 "description": "Inspect BQT_v2_pages structure"
}
```


### [2026-09-06T15:51:42.415Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬‬
‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان‬

                      ‫‪۴2 ۱‬‬

                  ‫رک یمن‬
                  ‫م سارو کی و ررك‬


                 ‫جلررومدا‬
             ‫چاپ د
=== formfeeds:
684
['[ برای پرندکانماهی و غیرہ ]', '[از\u202a:\u202cجنب اش (پوند اسم\u200cمصدر) ]', '[ر \u202a :\u202cح\u202a.]', '[یکرکاف ]', '[ك \u202a:\u202cگاه ]', '[رك \u202a :\u202cخامالا و خامالیون ]', '[ رجوع به وال شود ]', '[ک]', '[که ابن\u200cدوم را آذرخراد کفته\u200cاند]', '[ رك \u202a :\u202cخریز ]']
```


## [2026-09-06T15:51:51.507Z] TOOL CALL #26: Bash

```json
{
 "command": "sed -n '1,50p' tools/ref_page.py",
 "description": "Inspect ref_page tool"
}
```


### [2026-09-06T15:51:51.551Z] TOOL RESULT

```
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
```


## [2026-09-06T15:52:00.416Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))['BQT']\nprint(json.dumps(d.get('scans'),ensure_ascii=False,indent=1))\nprint('local_file',d.get('local_file'))\nprint('page_offset',d.get('page_offset'))\n\"",
 "description": "BQT scans config"
}
```


### [2026-09-06T15:52:02.277Z] TOOL RESULT

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
local_file ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
page_offset vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-09-06T15:52:06.937Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 153 154 155 156; do echo \"########## leaf $n (printed ~$((n+543)))\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -c 1200; echo; done",
 "description": "BQT v2 leaves around printed 697"
}
```


### [2026-09-06T15:52:08.887Z] TOOL RESULT

```
########## leaf 153 (printed ~696)
                                ‫گفتار هشم‬

 ‫تبجی‬      ‫از "کاب بردان قاطع در حرف ای هطه دار باروف‬

        ‫دیتفی بر دست بان و محتوی بر بصد و بيست و دو‬
                                 ‫و کنات‬         ‫لت‬




                                     ‫بیان اول‬


‫خاتهر ‪ « ۴‬بنتح میمبروزن تاجور ؛‬                    ‫هک‬
                                                 ‫اهی‬      ‫را‬
                                                       ‫آگوی‬
                                                     ‫بند‬              ‫وہے‬
                                                                      ‫ی‬   ‫‪۶#‬‬
                                                                        ‫کخا‬
‫کثرف همچو آب مطبخ وزیر آب حمام بدانجا | بلغت زند و پازند (‪ )۱‬بمعنی خواهر است ؛‬
‫و یک میم هم درست است ؛ و بجای رای‬                                                  ‫رود ‪.‬‬

          
########## leaf 154 (printed ~697)
      ‫‪-61‬‬                                                                                                 ‫خاتم کوبا‬
                                                                  ‫خاتم گویاد بمعنی خانمسهیل شان‬
‫را لز‬      ‫)‪۰‬‬    ‫‪ 9‬فاطمه علهااللام‬               ‫است‬    ‫معظمه‬     ‫و شاهد‬    ‫ومعشوق‬       ‫است که کنابه از دهان محوب‬

                                                 ‫گفته اند ‪.‬‬                                               ‫وساقی باشد ‪.‬‬
                                                                  ‫خائو له بروزن تاتوله » مکر وحیله‬
                                                                  ‫ودغا کردن ‪ -‬ودو بیتی ‪ -‬و دو دل بودن است ‪۰‬‬


‫خاج " = بر وزن تاج » بمعتی چلیپا‬                                 ‫وژن صابون » بزر که‬          ‫=ر‬
                                                                                              
########## leaf 155 (printed ~698)
‫جار خار‬                                                                                                            ‫‪-۷-‬‬
‫خار بست د آنجه بردور (‪ )۳‬زرات‬                                          ‫چوبی که راست رسته باشد وچویی که دارسازند‬
   ‫وسر‌های دیوار باغ از خار و خلاشه بندند ‪.‬‬                                                 ‫بجهت (‪ )۱‬قصاص دزدان ‪.‬‬
‫= جاتورست معروف ‪٩‬‏ ‪۰‬‬           ‫خار يشت‬                               ‫خار = پروزن مار ‪,‬معروف است ‪- ۷‬‬
                                         ‫کو‪:‬ندمارافعی‌را‬            ‫و نام قصبه‌ای باشد ازمضافاتری ‪ - ۴‬وماه بدررا‬
                                 ‫میگیرد وسر بخود‬                   ‫هگموبند که ماه‌شب چهازده‌باشد‪ -‬ونازو کرشمهٌ‬
                                ‫فرو میکشد و مار‬                   ‫معشوق را نز گفته اند ‪ -
########## leaf 156 (printed ~699)
    ‫ره‬                                                                                        ‫خارخك‬
             ‫راکش منوب بدوست ‪.‬‬
                             ‫که سرود خ‬                                                        ‫گفته اند ‪.‬‬
‫خار کن‪ -‬بروزن بادزن» معروف امست‬                   ‫‪ 4‬وآن‬    ‫است‬    ‫ممروف‬   ‫ت‬   ‫‪۱‬‬   ‫خك‬          ‫جار‬


 ‫وآندخصی باشد که ببوسته خاراززمن بکند ‪۹‬‬           ‫خاری باشد سه پهلو ‪ .‬بهترین آن بتالی بود‬
‫و ام نوایی وصوتی است از موسیقی ‪ - ۷‬و نام‬           ‫وآنرا مفرییان (‪ )۱‬حمص‌الامیر خوانند گ‪.‬ویند‬
 ‫تدوصتب‬
                           ‫‪۰‬‬
            ‫است که سرود خار کن منوب‬        ‫شخصی‬
                                                  ‫كك بهار‬
                                                        ‫است وعصارة آ را درجامی �
```


## [2026-09-06T15:52:16.856Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"######## leaf 155 full (printed 698)\"; awk 'BEGIN{RS=\"\\f\"} NR==156' BQT_v2_pages.txt | tail -c 1400\necho; echo \"######## leaves 185-187\"\nfor n in 185 186 187; do echo \"--- leaf $n (printed ~$((n+543)))\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -c 900; echo; done",
 "description": "BQT leaves for خار footnote and خرد"
}
```


### [2026-09-06T15:52:18.450Z] TOOL RESULT

```
######## leaf 155 full (printed 698)
      ‫فری ‪۳‬‬

  ‫_ از ‪ :‬خار (ه‪.‬م‪)٠‬‏ ی‪+‬شت «هویشمان‪»۱11‬‬                                         ‫رك ‪ :‬اشترخار » خارشتر‪.‬‬        ‫‪_ ۵‬‬

  ‫پهلوی ‪ :‬خار پوشت* بوستی ‪ .‬بندهش‪ .۲۲۱‬لغة بمعنی(جانوری) که‌پشت او خار دارد» دلدل(عی)‪:‬‬
      ‫بپوست او نکند طيغ پوستین پبرای‪.‬‬                                    ‫بخار پشت نگه کن که از درشتی موی‬
   ‫کایی مروزی «لغت فریه ‪5‬‬
 ‫خارخار » خلحان وتعاق خاطر و اندشه که صمر آدمی برطلب و کنجکاوی دارد‬                                          ‫‪- ۷‬‬

 ‫‪ :‬در آدمی عشفی و دردی و خارخاری و قاضابی‬                          ‫‪۳۸۲‬‬         ‫» تعلیقات فيه مافه مصحح فروزان‌فر ص‬
            ‫هست که کارصدهزارعالم ملك اوشود که نیاساید وآرام نیابد ‪« »...‬فیه‌مافیه مولوی‪.»4‬‬
                         ‫بقتح شم ‪ ,‬متعدی خاریدن (ه‪.‬م‪ .).‬خارش دادن ‪.‬‬                                ‫* خاراندن‬


######## leaves 185-187
--- leaf 185 (printed ~728)
  ‫خر حه‬                                                                                              ‫‪۳-۷ ۲۷‬‬



  ‫باعد و آرن بکیزی‬        ‫ان‬
                           ‫لشیر‬
                              ‫کز»‬
                                ‫معنی سا‬               ‫باشد وانکررایکوبند وبر گوشت‌پاشند وبگرك‬
‫غلیواج میشود و پیوسته خود را سرنکون از‬                    ‫دهند تا بخورد بعد از ساعتی بمیرد وبدان سبب‬
 ‫درخت آویزد (‪ )4‬؛ و با بای فارسی هم‬                                      ‫خانق الذئب وقاتل‌الذئب خوانندش ‪.‬‬
                                   ‫کفته اند ‪٩‬‏‬
                                              
--- leaf 186 (printed ~729)
           ‫‪۱‬‬
                                                                                                      ‫خرچکول‬
                       ‫‪2‬‬     ‫‪.‬‬   ‫ماه باشد ‪۹‬‬   ‫وخانه‬   ‫چهارم‬


‫خر ححجیون‪ -‬سض اول و سکون ثانی‬                                      ‫اعت را سادات خرجته وخر در کله خواتند‪.‬‬

‫وخای مضموم وجیم بتحتانی مجهول رسیده وواو‬                           ‫ک = بفتح اول و سکون‬
                                                                          ‫چرکو‬   ‫خ‬
‫تانی وجیم فارسی‌مفتوح وکاف مضموم بواو وکاف ؛ مفتوح‌بنون زده " بلغت سربانی‌کابوس وعبدالجنه‬
‫راکوند ‪ ,‬
--- leaf 187 (printed ~730)
 ‫خرداد‬                                                                                        ‫‪-‬‬
                                                                                              ‫‪۲۷‬‬‫‪-‬‬

‫ازختاو ختن کهمشك خوب در آنجا میشود ‪ | -‬و بی‌تشدید ثانی همدرست امت ‪ -‬و بکسر اول‬
‫وفتح ثانی‌بمعنی عفل باشد؟ ‪ -‬وم اول وسکون‬            ‫و نوعی از جامةً آبریشمی هم از آنجا آورند ؛‬
‫»بمعنی کوچك باشد که در مقابل‬        ‫لث‬
                                     ‫ثیاو‬
                                        ‫ان‬          ‫و بجای زای هوز رای قرشت همگفته اندکه بر‬
                               ‫بزر کب امت ‪
```


## [2026-09-06T15:52:27.221Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==188' BQT_v2_pages.txt | tail -c 1500",
 "description": "BQT leaf 187 footnotes (khirad)"
}
```


### [2026-09-06T15:52:29.053Z] TOOL RESULT

```
��ابورسمان دارلآباارقیه (س‬
  ‫‏‪ («٥‬گو بد ‪« :‬معنى هذا الاسم (خرداد) ثدات الخلق» وی نام ابزدی از ایزدان دین‌زرشتی‌است‪.‬‬
  ‫نگهبانی سومین ماه سال وششمین روز ماه (شمسی) با اوست ‪ .‬در اوستاو کتب دینی پهلوی خرداد‬
  ‫وامرداد غالبا باهمباد شده‌اند ‪.‬خرداد مظهر کمال اهورمزدا درین جهان و درجهان مینوی‌بخشایش‬
 ‫ابزدی جزای اعمال لیکوکاران است ‪ .‬در عالم مادی‌نگهبانی آب با خردادست‪ .‬بیرونی(آ ارالباقه‬
  ‫كويد ‪« :‬هروذا (خرداد) هوالملك المو کل بتربية الخلق والاشجاروالنبات و ازالقالتجانات‬               ‫‪۰‬‬
  ‫بقیه در صفحةً ‪۰۳۷‬‬

                                                                               ‫بقبه از صفحهٌ ‪۸۲۷‬‬
                              ‫چو گودرز آن سو گت شپزاده (سیاوش در هر کف مادر ) دید‬

   ‫دژم شد چوآن سرو آزاده دید‬
             ‫شنو پند وازلومکن سوك یاد‪.‬‬                   ‫بخرجید گوفتش که ای شاهزاد!‬
   ‫«شاهنامةٌ بخ ‪ ۳ +‬ص‪۱۳۵‬‬
```


## [2026-09-06T15:52:43.066Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD xrad ===\"; grep -n \"xrad\\|xrat\" PHD_mackenzie.txt PHD.txt | head -20\necho \"=== PHD xar donkey ===\"; grep -n \"^xar\\| xar \\|xarbuz\\|xarbūz\\|karzang\\|karčang\" PHD_mackenzie.txt PHD.txt | head -20\necho \"=== PHD xār ===\"; grep -n \"xār\" PHD_mackenzie.txt | head -20",
 "description": "MacKenzie lookups"
}
```


### [2026-09-06T15:52:43.143Z] TOOL RESULT

```
=== PHD xrad ===
PHD.txt:219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:3333:reason čim, wihān(ag); xrad ; without — abēčim.
PHD.txt:4323:wisdom danagih, frazānagīh, xrad; innate ~ àsn-xrad.
PHD.txt:4324:wise dānāg, frazānag, xradēmand, zīrak.
PHD.txt:4359:xradīg,
PHD_mackenzie.txt:1219:asn ['sn l ], ..... xrad: innate wisdom.
PHD_mackenzie.txt:5567:xrad [hit I I M xrd, N xirad] wisdom, reaSOn.
PHD_mackenzie.txt:7377:  (asnidag), pak(izag), yoJdahr.               reason tim, wihiin(ag); xrad; without
PHD_mackenzie.txt:7950: 'weed zaz.                            'wisdom danagih, frazanagih, xrad;
PHD_mackenzie.txt:7951: week haftag.                               innate ....... asn-xrad.
PHD_mackenzie.txt:7952: weep bram-, griyistan.                 wise      danag,        frazanag,    xradig,
PHD_mackenzie.txt:7953: weeping bramag.                            xradomand, zirak.
PHD_mackenzie.txt:11653:amar, hamahl, hamill         ~         xradumallll               "'f4~&
PHD_mackenzie.txt:11655:amargar                   ~~           ardIg. xradIg               \~~
PHD_mackenzie.txt:11661:hamban                     \~          Ard, xrad                     \,v.,..
=== PHD xar donkey ===
PHD.txt:426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:1431:crab karzang.
PHD.txt:3005:oryx xarbuz,
PHD.txt:4996:kulang kirrdg sett kargās karkēhan kark karm, kirm karmīr karb, kirb karafs karbunag karzang kardār
PHD_mackenzie.txt:3249:·karzang [klcng I M kyrzng, (N xarcang)] crab; astr. Cancer.
PHD_mackenzie.txt:5540:xar [HMRA < A lJ,mr); hll N.......,] donkey, ass.
PHD_mackenzie.txt:5541:xar [h)ll M x)r, N .......,] thorn.
PHD_mackenzie.txt:5542:xar- buz [hlbwc I M xrbwz] oryx.
PHD_mackenzie.txt:5543:xar.g6A [hlgws IN.......,] rabbit, hare.
PHD_mackenzie.txt:5544:xaroIYland [h)[>wm1zd] thorny.
PHD_mackenzie.txt:5545:xar-puAt [h)lpwst IN.......,] porcupine, hedgehog.
PHD_mackenzie.txt:6296:crab karzang.                              cypress sarw.
PHD_mackenzie.txt:7205:oryx xarbuz.                           passing sazisn, widerisn(ih).
PHD_mackenzie.txt:9546:kabig                   '!.lQ)~       karzang              .:;\~~
PHD_mackenzie.txt:11621:xar   I                                hambawisn       I
PHD_mackenzie.txt:11759:xarbuz                                -ag                                 \~-
PHD_mackenzie.txt:11800:                                      haT, xar                        ~
PHD_mackenzie.txt:12323:                        '~16'U'     ahr, xar                   ~
=== PHD xār ===
```


## [2026-09-06T15:52:43.854Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT xara ===\"; grep -n \"xara-\\|xratu\" BRT.txt | head -30",
 "description": "Bartholomae xara/xratu"
}
```


### [2026-09-06T15:52:43.926Z] TOOL RESULT

```
=== BRT xara ===
2582:ai.  »el-  "«'=''™'-,Adj.  —  Pü.  (iu  V.6./): /«>,   (Priester-)Schule,    Lehrer,    (priested icher) '7  i^,i/A^^''il?^;/'''„' v''5  i'"™^;,'L^ '"^  Lehnncister":    hat   m    *--paiHm   upt'islll ylrpjirJ/ö;  %risar>maem  (sd.)  xratum  a
2768:mit  paiti  i)  'streben  nach  — ,  begeh- ren': a)  mit  Akk,:  tafca  yä  kasu.xratul ,  masyöjcrdkwqm  (sd.)  nöit  paitiSaiti  V.  7, I  59.  b)  mit  Gen.:  s.  AbsoL  a)  'sich befleissigen,  betätigen',  mit  Akk.'>:  paiti- sata  (2P.)  mazdayasna  sraoiahe  a/yeke '  yasmm  Y.  37. 13;  —  staota  yesnya  yaza- maide  .  .  dadräna  paitHäna  paitiima- .  r^mna  Y.  55. 6 ;  —  six/anlfm  sa/ayaitt^m paitisant^m  Vyt52,  *P- /?  (wo  °Ä«- ,ljm)'i^.  3)  'erfahren,  erleben':  iaia lUli  (sd.)  *paitUäma  '*>  frya  paiti  tanvi ,  Yt.  i7, 10.  a)  bes. 'zur  Vergeltung,  zum Dank  erfahren,  empfangen':  kä>:ä..kä%3 .  (sd.)  saidyäi  yS  I  paitisift  Y.44.2 ; — ya^a ahmya  amtsa  spmta  sraoläoa  aiyäoa paitisqn  . .  yasnqsca  vahmqsca  Y.  öb.6.
3607:•  j.  apairi.gaed'ä-  Adj.  -?-:  dusxratum ''^am  *asravayai^a%qm  Aog. AD.
6752:•  ).  a-ham.baoS^mna-  Adj,  'nicht  wahr-  Oberherm  und  Richter  und  als  den nehmend'  sva,  'der  seine  Sinne  nicht  zu  ersten  Lehrer  der  Menschheit"  Yt. /_J.  1 5  a ; brauchen  weiss'  (vom  Hund):  yat  ..  sfä\ —  ya^a  fr3  loa  (sd.)  ämraot  yat  dim •n<s  Tä  haiat  aoäitySjxratus  "wenn . .  ander- '  ahümca  ratutn^a  ääadat  "'ya^a'  sagt  aus, seits  ein  Hund  seine  Sinne  nicht  zu '  dass  sie  ihn  (näml.  Zar^  als  A.  und  R. brauchen  weiss,  der  (weil  er)  nicht  recht  eingesetzt  haben"  Y.Jfj.u;  Yt  7^.92;  — bei  Verstand  ist"  V.  /_J,  35;  —  yesi  nnl<yailqm  ns  ahurS  maeäh  .  .  vatsks  valaa spS  'nS  mafye  v3  .  .pai'jyäite  aAmai(sA.)\{sA.)  atiqm  zaraiustr5  ankuca  (NS.)'' heüa  irisylt  "sonst  könnte  der  Hund,  der  ratu^ca  Vi.iö.i;  Yt./j.gi;  —  allai  dim seine  Sinne  nicht  recht  zu  brauchen  weiss,  lUsfanam  maziit?m  dazäyli  (sd.)  ahümca in  eine  Grube  ..  geraten"  V.  j_j.  37.  .^ratämca  yim    ahunm    mazdqm    Y.  27.  i;
6860:'rS  maaiä y7  mazistJ yjzatanqm yJ  vaAi^^  yt,i^.  ^T  \t%v.;  —  cattt  alte  mi^ra  tava  yit yazatanqm  Yt.J7.16; —  °r>m  tnazäqm  ..'.°ra  ma3äaV.4-3;  —  ahm  äuyoarfm 'rahe hudanfam  mazishm  yjzalim  yim  sjvisi?iH  \  mazdii  3^ai>karpm  ain>sanqm  spmtanam /rädat^ali:}m  dätänmvohunam  damanqm\'^K.i-j.z;  16,  V.  79.  13;  —  us  mg  fita \,  16.  i;  —  nh'afiayemi..daiusj(StvcTZ.)iAaomäi  draond  frSnnaoi  °rS  mazdh  ..  V. °rahe  mazdä  ralvatS  c^annarmAalS  (Sl-  /j,  4;  —  astvatintä  .  .  asts  mazda  °rahe verz.)  mazistahe'a  vahistahe^a  sralHahecaYlx.ig.f)-i;  I3.\\f>,  V./(7.34;  —  buyama xraoMistake'a  xraiwistaheÜa  kukinpttma- ,  'rahe  mazda  frya  väsiita  astayJ  (sd.)  V, he'a  aSät  apanSJtmahe'a  hwiHmanS  vouru.- 1  70. 4;  —  haomö  . .  zaota  °räi  (statt  Gen.) ra/na»/i^  y7  nS  daöa  yd  lata^aylltu^ruy?\mazdai  Vty.88f.;  —  ySs^a  t!  y?na  'ra yj  mainyus  ipmtSJimB  V.  /.  i ;  usw. ;  —  mazda  Vr.  7.  4 ;  —  fravasTm  avqm  yqm pQuru^ar)na)3ha  'ra  mazda  VyL  2^^;  —  °raAe  mazdä  Y.  26.  2;V. 1^.14;  —  vXsp»mca °raki  mazdh  ..  STvUtah!  \.  56.  1;  — ^k^rs/s  'rahe  mazdä  Y.ji,^; —  ««  'rahe ax^aßis  ahi  abai>hJ!  tum  yS  °rD  maxdä  1  mazda  yazamaide  dar?ir3i  (sd.)  mq^rahtr V,  jp.  20;  —  'rät  mazält  .  .  vpr/irayne ■  sp^ntaAe  xralüm  'rahe  masdi  ..  marjirrüi frädat^aliai  yat  huxla'iräi  .  .  ratu-l..  hievam  ° rahe  matdä  . .  fravSkäi  .  .  Yt. xla%rai  Vr.ll.i;  —  huxsa'irSJ^mli.'if  1.2%;  —  gayehe  marP^nS  .  .  yS  paoiryd at  xsa'ir?m  eiyJt  yat  'rät  masdäi  A.^.  °räi  (stitt  Gen.)  mazdJi  manlscä  *git/ta 6;  s.  Y.J5.5;  —  'rät  masdäi  fanhavl  säsnasca  Yt./_J.87;  Y.jp.14;  —  nazdys vohumaill  Y.  I2.\;  "V,  tg.  11;  —  vaAists\ahmi  az>m  (Stverz.,  unter  3)  yö  'rS 'ra  mazda  Y.  /p.  1 5 ;  —  xsayat?  "rahe  I  mazda  vispahe  aukSul .  .  ya^a  .  .  P.  2(.?; mazda  YX.13.-jZ;  —  ise  ^wqm  'ra  mazda ..\  usw.;  Vyt.j^';  —  pascasta  azim  ya  'rS aoaoyf  ahi  a'iaoyS.xratul ..vTsps.viwS  Yi.'mazdil  aoi  urune  urväsma  (sd.)  dassayeni /2,  i;  70.  III,  V.  ig.  20,  a6,  Vr.jp.  i;  — Ivahi/ipmea  ahüm  .  .  V.38;  Y.ig.6,  7;  — °rJ  mazda  hvapis  Yt  5.  85;  Y.  7/.  10  (wo  vasas^a  tu  'ra  mazda  . .  x/ag/a  havanqm ab  Vok.) ;  —  'ra  mazda  mainyl  spinUta  1  däinanqm  Y.  Ä*.  5 ;  —  imat  dqma  yat  "rahe dätar?  gai^anqm  astvaitinqm  asäum  {^\.-\  mazdh  V.jy.14,  17,  34;  Vyt  20,  Vd.  i, verz.,  unter  I  2  a.);  usw.;  —  tsm  bay?m\YX.i(f.iZ,\.22.Z;  —  irrj/^/^-rJ (statt Vok.) t)m  ratüm  ,  .yim  'ram  mazdqm  daovätih?m  \  mazdä  vanuhti  dämqn  .  .  yazamaide  yäü i^t^vcz)  rapant3mtarh'a»h?mt'üpa*voh[i^dadä'ia  pouruca  vanhuia  Y.  7;.  10;  ;.  1, Y.70.1;  usw.;  fo.  9;  —  'rim  mazdqm\  12.  7, Yt  ig.  10,  58,V.  21. 4;  —  azmi  daoqm mainyaem  mainyavanqm  dämanqm  main-...tistrim..ya'ia  mqmcit  yim  'nm  mazdam yaoyä  stSts  ahUm;a  ratümca  Vr.  2.  4;  7,IVlÄ'.5o;  —  ttstrlm  .  .  yahmäi  hazaitnm ^'■57-4j  —  allat  dim  vlspanqm  mazih?m\yaoxstinqm  fradd^at  °rS  mazda  Yt^.45; dazdyäi  (sd.)  ahUm^a  ratUmca  yim  °r}m\iQ.Z%; —  tistrim  ..yim  ratüm  frada'hat masdqm  Y.  27.  i;  Vr.  /;.  21;  —  imimca'  'ro  mazdä  YL<?.  44;  5-  89,  70.103,^5.35; isi"^ rahe paitim ..yim  'rsm  mazdqmY.2.i6;\  —  arpdvjm  . . yeiihe  ca'^wärB  arSäna  ham.- 13.1,  ^.I03{?);  —  ySvaram  °rS  mazdä ..^tlsaX  'rJ  mazdä  Yt. 5.120;  —  ya'ia  vs tä  varmScä  .  .  ahmi  Y.12.  7;  —  mi^rpm  '  'rS  mazdä  fradaiim  haxsat  F.  ^Ib;  —  tä ..yim  yazata  'rS  mazdä  raoxsnlt  paiti  (frava^ayS)  ii3..'ä^rayente  ..aomna  'ra{lS^ gars  nmänlt  Yt.  10.12s;  5- '7!    —    avi\  mazda  Yt  13. 146;  S.7,  $&;  —  äyaptj/r.
6889:—  tistrlm  ..yim  'raca  xratugBlS ..*hispö.- ttuti  Yt  iV  36 ;  —  fravasayö  .  ,  yil  °rahe xiayatö  doBnqm  upa  yüi%yänti  Yt/_J.  63;
7499:•  j.  'ä-sna-  Adj.  'angeboren,  natürlich', von  xratav-  m.  'Weisheit'  (im  Gegensatz zu  gmiSsräta-,  sd.):  «J»V  mailm..  s/g(s±) masyä  kacaiie  °nS  xrahts  yaüa  mi'inmni .  .  ha<aiu  'nasHt  xratus  "es  gibt  keinen Menschen,  dem  grössere  natürliche  Weis- heit zu  eigen  ist,  als  , ."  Yt.ro.107;  — "rum  xraiBm  tnasdaoättm  .  .  gaosS-srütim xratüm  tnazda'Mit^m  Y.  25.6;  —  'nahe xraiwö\.  22.2%;  —  Uta  kg  "fum  xratäm avaiaraiti  vSrjma  (sd.)  Yt/j.a,
7753:•  g.  araSva-  Adj.  i)  'recht  handelnd,  ge- recht': västryö  syaoianäis  °vs  hqs  huxratus namaakä  (sd.)  Y.5i'.  s;  —  ks  7'ä  vaiAsus manav/iö  aästä  magäi  'vd  "oder  wer  wird, rechthandelnd,  sich  auf  den  Bund  des  VM. bedacht  zeigen?"  Y,  57. 1 1 ;  —  yS  savaitl ädriiig  (sd.)  'ViwAöY.S^.^.  2)  "wahr, sicher':  ''i'j(APn.)  x/a^nl . .  asTstfs'{sd.)  Y. 44.g;~däidi*asä*dä(sd.)  dar^JyFi  'vifis tli  ux'iilis  mazdä  zarairvstr^t  aojSnghvat rafonS  akmaibyäLä  aAura  "schenk  du, o  M.,  durch  Aia  .  .  dem  Zar.  gemäss deinen  sichern  Worten  langdauernde  kräf- tige Unterstützung,  und  uns  . ."  Y.  2rV.  6.
10546:•  j,  xara-  m.;  xara-  f.  'Esel'*;  Esel- stute': täirya  payä  (sd.)  bavät  aspayaat'a ^'•rayäatla  ''>  N.  6y.  a)  m.  ein  mythischer Esel,  der  im  Weltozean  steht*':  'nm:J yim  a^avatum  .  .  yS  hUtaiU  inavAm  zra- yanhs  vouruka^ahi  Y,  ^2.4.  [S,  noch "xra.uru.b'^
10597:xratu.käta-
10613:j.  xratu.kata-  Adj.  '(um  Weisheit  ange-
10617:xratugrut-
10621:•  j.  xratu-gÜt-  Adj.  '(Weisheit  sva.)  Be- lehrung, Rat  erteilend':  ahuraca  'giitSi,^?.)
10623:•  j.  xratu.^inah-  Adj.  '(Weisheit,  d,  i.)  Be- lehrung (in  religiösen  Dingen)  heischend' "' ; yai  -nanks  (PP.)  jasqtt  upa  vä  ma^nm spinfim  marasta  "wenn  sie  kommen  Be- lehrung zu  heischen,  soll  man  ihnen  das heilige  Wort  vorsagen"  V.4.4S;  44-
10625:•  j.  xratu'mant-  Adj.  'einsichts-,  weisheits- voll': xitvS  yal  ahmi  xralu^  hapta'hd  °ma yt.l.j;  ¥.6.
11072:asaotie ..aiwica  Aa/ft(Sp.  277  u.)  *cai3näica pailica  *p>r?smanäi  xratum  asavamm  N. 84.  ß)  in  Verbindung  mit  der  Nega- tion: nöit  astaca  nSif  us'tänjmca  nöit  bao- 'lasca  y.iff.j.  f)  mit  unregelmässiger Stellung  des  cä:  ahurB  masdascä  'J'  ärmai- tis^ä  aümaJ  /rä^aigai^pm  raaaasciJ  voka xsa'hnimcJ  Y.jj,  11;  —  fravaSlm  avqm .  .  xra'iwHtqmca  hukir^pUmamca  a/ät apanSJimqmia  Y.2Ö.  2  '*'.  b)  sie  sind  ge-
11359:—  ahe  zl  nä  ..  aframannti  (sd.)  ästrydte yaha  gä^anqmat  N.22 ;  —  daivayasnoHbyS paurvS  ämayayanta  yaha  mazdayasnaH- byasät  V.  7. 37;  —  Aamah a  iStverz.) ya'ha paraat  Yt.  S- 65  usw.;  —  bei  negirtem Hauptsatz:  »Sij  masyS  ..  ao/if  {sd.)  maiti- yäe  duimat^m  ya'ha  mihrasHt  ..mainyäe kumatim  Yt  m,  106;  106';  —  nSit  mallm ..masya  /ia^aite(sd.)  äsnö  xratu/ya^a  mi- ^r»mät..Aacaite..Yl.io.iOT.  a)  wieder- holt 'sowohl  , .  als  auch,  nicht  nur  . . sondern  auch,  et  ..et.,  et ..,  cum.,  tum': vatjharsStascit  maytt}niasä( srSvaySi^Y.  12; zit  *N.  log^^i  —  raixtnä  aspSnili  sädrä- Ht  /axrq)i5(sd.)  Y.34.J ; — savAimat  *anu.- sasträi  sa^himHi  *anu.mainyäi  Yt  10. 137;  P.2Ö(?);  — fratar?mHt  ti  havamm vaüa   upa,staomi  . .  upanmcit  .  .  Y.  10.  3;
11443:•  j.,  g.  '(Sistay-  f.  'Denken;  Erkenntnis, Einsicht':  °ff''  ui§täis  syaokanä  ahm  spsn- vaiiaA.)  Y.5/.  ai;  —  isn^  ä  vanhSul ;imaS  manauhs  'tis  "wer  fsind)  die,  bei denen  die  Erkenntnis  des  guten  Sinns  sich einfinden  wird?"  '^.48.11;  — Sya  Hl  hv8 *ptä  asahya  mazdä  "in  (Folge)  dieser  Er- kenntnis: er,  M.,  ist  der  Vater  des  A" Y,  4-].  2 ;  —  hyat  ka^rä  fsA)  manS  bavat yahrä  'H/  atshat  mafkä  Y.jo.g;  —  mana xrdhwäca  °Hca  "durch  meine  Geisteskraft und  Einsicht"  Yt-/.a6; — xi'tvS yat  ahmi xratus  .  .  aitims  .  .  •tif  YL  /,  7;  F.  ig;  — prp'^yä  . .  a/ffi/  . .  a/navaihyä  -ISis'  Vr.  q. 4.  A)  als  Gottheit:  haomanqm  .  .  assis .  .  °isis  baiSaza  kaämnanqm  Vr.  fj.  i;  — ■ sonst  mit  vattula-.  aiim  ..  °tlm  vanuhTm Yi.4.1;  —  a^öil..-'t5is  vankuya  "jwiJ.. Y.7.14;  V.ip.39,  Yt//.i6.
12524:•  j,  *daevö.tät-"  f.  '.öt/ft/aschaft':  xara- ,  srirä  pa'iö  daesayänti  Vty.53;  — ./*»- '^usiraie  .  .  yS  vispqm  'lät^m'^  vavaca  vasayS  .  .  yä  stram  mhnhö  hürS  ..  pähB aytsnyqm  avähmyqm  Yt  y.  90.  XdaisaytnXX.i^.^'};  —  a^qm  ratui . .  aSahe
13435:g>rpbqm  (sd.)  huxratus. .  spmtqmlä  ärmaitim °iinm  (ASf.)  ".  .  und  an  der  heiligen  Arm., der  schaffenden"  Y.34.  10;   —   'mim  ..
14361:%w}  (NSm.)  a  gsui  taSa  (sd.)  as  *xratui Y.^i.g.  3)  'der  deinige  sva.  dir  er- geben, dein  Anhänger':  ysi  .  .  ärmattim 'wahyä  mazdä  hrixhqm  (sd.)  vTäusö  .  . ovajsata^  Y,  J4. 9.        [Y.  44. 10:  lies  äwJ.-
16760:bavam  aiwi-sasis  aiwiJmantB  "wenn  ich in  Worten  und  Gedanken  verwünscht werde"  Yt74. 34;  —  iS«  frikiä  paiti.- zantä  buyata  "hier  sollt  ihr  geliebt  und gern  aufgenommen  werden  (sein)"  Yt 13.  147;  —  altallva  daxma^a  .  .  yöi paiti  äya  zima  bavainti  vzda^a  usdista "in  diesen  Z>.,  die  auf  der  Erde  aufge- schüttet werden  (sind)"  V.  7.  54;  —  aat hl  im  za  bvat  psrme  .  .  "drauf  ward ihm  die  Erde  voll  .  ."  V.  2.  8;  —  ana buyä  savanS.sasta(sd.)  ana  buyä  huyaita- tara  (sd.)  Yt  5.  9;  — yif  bavaiti  xratu.- käts  (sd.)  Yt  13.  16;  —  yai  */ranata bun^^  N.  65(?);  —  liu'ha  nmäwm  yaoe- da%ani  iuäa  bun^^  (näml.  nmana)  yaos- data  "wie  kann  ich  das  Haus  purifizi- ren?  wie  können  (die  Häuser)  purifizirt werden?"  V,  72.  2;  77.  a,  72.  3,  75.  33*, 20.  a)  negirt:  yai  St  bavainti  *ana-
18957:furchtsvoll bittend,  betend' :  yi  mq%ra  (sd.) *vaam  .  .  baraitT  urvahu  aia  *nAa  (NS-) Y.50.  6;  —  vastryS  yyaoHanats  fnfys  Aas Auxratus  -»Aä  yS  . .  "der  Bauer,  der  in seinem  Tun  gerecht  ist,  der  einsichtsvolle, wenn  er  (zu  dem)  betet,  der  . ."  Y.  5/. 5  j  —  yH^i  'nAa  (NS.)  vaHm  baraili  yal gaosXsAyit  Yt  10.  85 ''.
19779:vahiita—,  yaT  tat/  a%a  hatä.maräta  (sd.) vahista  vdiitä  •naaha  Y.J2.6>';  —  *df nS  maiJa  . .  vatthtul/radaxüa  (sd.)  °tuwhs Y.  J/.  17*';  —  king  a  vanA^ii/ ßmaj •naaAS  ^istü  {sA.)  Y.^.ii«;  44- 16*'; —  ya%a  ns  a  vohü  jimai  (sd.)  •naaha (als  Subj.)«  Y.  44.1«;  —  axsß  {n^) vanhJui  alä  ÜtTm  'navhB  Y.  46.  3^>; 32.  9*);  —  vatafOus  °nai»Jü5  syao%ana vaolai  ginhqm  (sd.)  huxratui  Y.34.  io*>; ^o.  io^>;  —  t^g  zhayä  (sd.)  vanhSus uxlaii  •nanhs  Y.46. 14**;  —  mat  vä  . . pairi/asai  .  .  vaiakfui  •nat)AS  ktmantäta (sd.)  Y.50.8'';  —  vanhSus..  kaotq%wat (sd.)  ä  'nanhsY.45.'i^''>  —  ahurim  aia- vafom  vanhTui  ßiT^hfm  (sd.)  'naaks  Y. J/.  lO^J;  —  'naahö  VawAj«/*'  i/ft/J  (sd.) Y.57. 18*';  —  yBi . .  ärmaitim  . .  duL^ao- %anä  avatazat  va»Afui  2vistT  (sd.)  •naahs Y.^4.9«;  —  yöi  ziahiitäi  *aiaonö  .  . rar7^an(s±)  'na»h6Y.32.  ii»;  —  doTvö.- tu/tä  (sd.)  vaisAfuI  sfSdyamna  (sd.)  °naahs matdä  .  .  xraiJus  nasyanio  (sd.)  aSaatca Y.^2.4*>; —  kuda  (sd.)  a/»m  vohuia  'n3 x/a^fvmia  Y,  2().  II*';  —  ySHg  a/aat^ä vSistä  vanfOufcit  . .  'naiaAff  »n%w9ng  (sd.) Y.  28. 10»;  —  y!  aii  as>m  nipätihl  (sd) 'nas^a  vohü  Y.aÄiis);  —  tat^a  %wahmt *a  *dqm  (Sp.  684  o.)  nipätshl  'nS  vohü urunasca  asäunqm  Y.^p.  10*';  verwendet 42.4;  —  inYHapL:  vohü  ^ma  •nat3ha voha  "kwa  asa  .  .  pairijas3maidl  Y.  36. 4'°*-  «)  im  Gegensatz  zu  Sprechen und  Handeln:  vahÜtaca  'naaha  aiä£(Sp. 231  m.)  ha/a  fyao%anäSt  vatanhai'a  Y. 47.1"*;  —  paurvatatim  (sd.)   'nanhasiä
19888:nüiiya  (sd.)  xinstjm  Y.31. 3";  —  ts  (näml. s^ä^rä)  matdä  'inya  uxlyS  (sd.)  yl  ä nürSm^  . .  hämS  Y.31.  7'';  —  ahyä  *°in- ySuS  tvSm  ahl  tä  (Sp.  905  m.)  sf>nt^  ys ahmäi  gqm  .  .  hJmJa/at  Y.47.  3;  —  at tBi  mazds  tPm  'inysm  asaox^ayantyä  *ta- r^idyayä  (sd.)  .  .  Y.  J5.9;  —  äw?  ä  giul tala  (sd.)  as  *xratui  °inySus  masda  ahurä Y.31. 9  '^.  b)  der  Geist  des  Bösen  heisst angra-,  aka-  oder  dngvant-'.  mainya  (Sp. 1125  m.)  . .  yayä  spanyä  Biff  mravai  y^'" angr»m  Y.  45-  2 ;  —  hyat  vä  aka  manatahä ying  äafvSng  akascä  °inyul .  .  Jyaeharum fraSnas  ..  */«>■;»  (sd.)  Y.^2.s«;  — aya  *Mainivä(Sp.ii25m.)z'aratä y? drugvä acists  vfntys  Y.30.%.  b)  im  jAw.: ihä  'inyB  mamanaiti . .  vaoiatar!  . .  z/3- v>r>zätarS  Y.  ij.  4;  —  paslaäa  .  .  yat 'inyB  dSmqn  daSiltgin  Y.57. 17;  Yt.  TJ.yß ^'inyu);  —  yüthistB  'iniv&  damqn  V.  ig. 42;  Y.ip.is,  Yt.  13.  T  6  {'nivä);'^  ya%a apimim  'nivä  anhat  nivaiti/  Y.  10. 16; '9-9'>  —  "^'i  ■  •  ^hmi  paiti  nairi  dva *'inyu  rSnaisA.)  ava.stsvhat  ■V.7.52;  — rar  antarp  eam  asmammca  druja  (Sp.  781 m.)  °nivä  vaonyät  Yt.i3.iy,\^.  a)der Geist  des  Guten*'  heisst  spmta-,  spanyak-x ..yatmainyB  dqman  daCoTtfm yasia  spmtd 'inyul  yasca  attrö  Y.J7.r7;  Ytjy.76, 75.43,  Vyt.  47;  —  dqma  .  .  yi  hinti spfntahe  'inySus  Yttf.i;  Y.j.16,  Ä  6, 27.2,  Vr,/2.4,  Yt.Ä48,  70.142,  i^.^, V.5.33.  yi.  aS,  Vyt,5/;  —  yat  sp^ntS 'inyus  vitärayal  asmamm  Yt.  ij,  a8;  39, V./p.  9;  —  yS  dc&vä  Spante  »inyui  Yt 10.  r43;  —  avanayeni  spantim  'inyBm hala  . .  garS  nmSna  uspatayeni  anram 'inyBm  .  ,  haea  duiaaha;  tl  ml  vaifm 'kanjaysnte  spmtatla  'inyus  araras&i  Yt. ig,  44;    —    sfaranS  yahmi  paiti  "para-
20143:j.  masyah-  Adj.  (fem.  'yehJ-Y^  'der grössere':  Ä  üsti  '_>'?(NSn.)  vatghs  srayS (sd.)  aittm  dättm . .  upairi  anyäi^..  V.5. 22 ; avai  hl  asti  'yS  ari^»n  (sd.)  V, 7.71; tisit  maslm  gag%Jm  ff?(sd.)  'ya  hacaiU (sd.)  3snS  xratui  YL/0. 107;  —  ''kaya h»nH  •yaaho  (NP.)  a^  (sd.)  .  ■  *ltaya kasyanhö  F.  j  c ;  —  ^a^  'yS  attahmäi barfsma  N.  70;  —  ^aSa  tJ'ays  (NSf.)" J/^  kasyanhqm  apqm  *avi./rädavaiie  (sd.) V.  5. 24;  —  ya%a  yayi  (NSf.)''  vana kasyanhqm  vanqm  aiwi.vfrjnvaiH  (sd.)  V. 5.  24;  —  yimö  . .  tqm  vXSävayai  (sd.)  atva 'kriha  ahm3l  'yehim  ya'^a  . .  V.3.11;  — fravasayS  .  .  yä  'yehll  ahmät  .  .  yaäsa vaca  /ramraväire  (sd.)  Yl  13.  64;  —  °yd va  ahmätäi  "oder  noch  grösseres  (ärgeres, näml.  soll  als  Strafe  ihm  geschehen)"  V. 4.  50.  a)  'von  grösserem  Wert,   wert-
20457:mäsdayasneis  . .  staotanam  yesnyanqm  Vr. 5.  7  j  —  gSuI  .  .  gayehe  .  .  'rahe  spmtake asaonS  vgntyarfuAaAe  Yt.21.3;  —  xara- 'hustnm  .  .  'nm  spnlwt  .  .  g^l  urvätam yazamaide  G.  4-  6  i  —  fravaiayS .  .  yqm^a ahrS  .  .  sraosahe  . ,  mi%raAe  . .  °rtiÄe  spenr tahe  YL/_y,86;  /J.  17;  —  äal  mqm  tum bi/azyöi^  'rö  (alsVok.)  iptnts  ys  aij^arma V.  22.  2 ;  —  ^aiti  ahmSi  avafata  °rö  spmts yH  asjfarmä  V.  22. 6.  a)  *rahe  spfTitahe (näml,  ayars)  heisst  der  39,  Monatstag: 'rahe  spmtahe  alaotüS  v^r»tyar?uhahe  S. /.  29;  vgl.  2.39,  ¥./().  7.  Undeutlich:
21124:2  a):  mit  tnaslm  ,  .  masyä  hacaite  J^fnJJ  möglich  oder  denkbar  hingestellt;  nur  c)  im xratu^ y  mtir»mcii  ..  halatie  äinasHl\\Pi.vt.\  a)  mit  Opt:  hö  mqm  ava'ha xratusYt  10.107.  zuzb):  hsuca  ..vohu^VTrmqm  nijaintHsÄ.)  y  v»Arkd..barf%ryät manB jiig)r)bustarU  anhai yS ..y  häti y5 ..  \^/iaca pui:r»m  midafy.dairyat(sd.)'V.iff.3S V.4.48;  F._yf,  V. /_J.  42,  43;  — ■  staotärpm' — y  .,  nmänS.paitim  paiti  tard.pikwtm vaf9hat?h>m  , .  aoxta  ahurS..y°  aäm  yat  .dai^yät  aha  astryäti  V.y.20;  A-^J.?; vaAist?mY.i0.g;  —  nazdyS akmi ..vTspahe\ —  th  yüioyänti  .,  mqnaytn  ake  y  .. ar?hsui*'maiiihca .  .y  Stsha  haca  *gaosalibya  \  ra%ailta  . .  haca  saäst  (sd.)  .  .  paiti.yntta y  vä  gaosa  haca  *%rar»hibya  (sd.)  P.  26';  I  Yt /J.  67;  —  tä  he  stiai^iifia  var^'äjosca
21236:—  aAyH  *griAmB  ä.ASihBi  (sd.)  ta  kava- yasclt  xratul . .  dadat . .  Ay  ('weil')  vTsjutä
21770:pasla  hl  peurum  (sd.)  paitiMncSiS  V.  8. 58;  58;  —  y  näirika  vohunU  aiwi.- vaiMt  . .  airimt  gatüm  kl  nühilaäa  V. J&8;  Vd./7;  —  y  ait^m  iristtm  upa.- b9r?%wSJanm  (sd.)  avajsanqn  ava  ait/m irist>m  baraym  V.8.a;  3,  7.13.  i4f-'> 74  f.*;  —  y  xratu.iinar)hB  Jasqn  upa
```


## [2026-09-06T15:52:58.996Z] TOOL CALL #33: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:52:59.004Z] TOOL RESULT

```


```


## [2026-09-06T15:53:02.188Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B1",
 "prompt": "Persian خر (xar) 'donkey': give the full etymology section — Middle Persian, Proto-Iranian, Avestan, Sanskrit forms, and any PIE root cited."
}
```


## [2026-09-06T15:53:03.846Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D8%A7%D8%B7%D8%B1",
 "prompt": "Give the etymology of Persian/Arabic قاطر 'mule' — all language sections (Persian, Arabic, Turkish). Is a Sogdian *xara-tara origin mentioned?"
}
```


### [2026-09-06T15:53:08.999Z] TOOL RESULT

```
# Persian خر (xar) Etymology

Based on the Wiktionary entry, here's the complete etymological chain:

**Proto-Indo-Iranian:** *[kʰáras](https://wiki/Reconstruction:Proto-Indo-Iranian/k%CA%B0%C3%A1ras)*

**Proto-Iranian:** *[xárah](https://w/index.php?title=Reconstruction:Proto-Iranian/x%C3%A1rah&action=edit&redlink=1)* (reconstructed form)

**Middle Persian:** HMRA (/xar/, "donkey, ass") - inherited from Proto-Iranian

**Persian:** خر (xar) - inherited from Middle Persian

**Sanskrit cognate:** खर (khara, "donkey")

The entry notes that "the meaning of something large is presumed to be from the weight-measure خروار (xar-vâr), originally a donkey-load but later even too heavy for a donkey to carry." This semantic extension reflects how the animal's name became applied to measurements and size descriptors in Persian compounds.

The etymological tree indicates the term may derive from "the BMAC substrate," suggesting ancient Central Asian linguistic influence alongside the Indo-Iranian heritage.
```


### [2026-09-06T15:53:12.006Z] TOOL RESULT

```
# Etymology of قاطر (Mule)

Based on the Wiktionary entry provided, the Persian word قاطر (qâter) meaning "mule" has the following etymology:

**Origin:** The term was "Borrowed from Turkic" languages. The entry provides cognates including Azerbaijani *qatır*, Turkish *katır*, Kazakh *қашыр* (qašır), Uzbek *xachir*, and Uyghur *خېچىر* (xëchir).

**Related Forms:** The entry also notes a connection to Tajik *хачир* (xačir), which similarly derives from "the same Proto-Turkic etymon through the borrowing of Mongolian into a Turkic language."

**Regarding Sogdian:** The provided content does **not mention** any Sogdian origin (*xara-tara* or otherwise). The etymology focuses exclusively on Turkic language sources and Proto-Turkic roots, with a secondary connection through Mongolian borrowing into Turkic languages.
```


## [2026-09-06T15:53:22.408Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/kat%C4%B1r",
 "prompt": "Etymology of Turkish katır 'mule' — Old Turkic forms, dates, and any Iranian/Sogdian connection."
}
```


## [2026-09-06T15:53:23.736Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%AF",
 "prompt": "Persian خرد (xerad) 'wisdom, intellect': give the etymology — Middle Persian, Old Iranian/Avestan xratu-, Proto-Indo-Iranian and PIE root cited."
}
```


### [2026-09-06T15:53:27.121Z] TOOL RESULT

```
# Etymology of Turkish katır 'mule'

Based on the web page content provided, I cannot offer detailed etymological information about the Turkish word "katır" (mule). The page shown appears to be from Nişanyan Sözlük (Nişanyan Dictionary), a Turkish etymology dictionary, but only the site's header, navigation, and footer are visible in the excerpt—the actual dictionary entry content is not included.

To obtain the etymology you're seeking, including information about Old Turkic forms, historical dates, and potential Iranian or Sogdian connections, you would need to access the full dictionary entry on the Nişanyan Sözlük website directly.
```


### [2026-09-06T15:53:29.772Z] TOOL RESULT

```
# Etymology of Persian خرد (xirad) - "Wisdom, Intellect"

Based on the Wiktionary entry, here's the etymological path:

**Persian خرد (xirad)** derives from "Middle Persian (hlt /xrat, xrad/, 'wisdom, understanding, intelligence')," which traces back to Proto-Indo-Iranian *krátuš meaning "intelligence, mental power."

The ultimate source is the Proto-Indo-European root *krét-us, which carries the sense of mental capability and understanding across ancient language families.

The entry notes a cognate connection to Old Armenian խրատ (xrat), identified as an Iranian loanword, demonstrating how this root spread across related language groups.

This etymological chain illustrates the deep linguistic ancestry of the concept of wisdom across Indo-European languages, originating from roots emphasizing intellectual capacity rather than physical characteristics.
```


## [2026-09-06T15:53:40.259Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CC%81ret-",
 "prompt": "Which PIE root page is this? List the meaning and the descendants (Greek kratos, Sanskrit kratu, Avestan xratu, Proto-Germanic harduz?) and whether Germanic *harduz is derived from this root."
}
```


## [2026-09-06T15:53:41.646Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/harduz",
 "prompt": "Proto-Germanic *harduz 'hard': give the etymology — which PIE root, and which cognates (Greek kratos, Sanskrit) are cited."
}
```


### [2026-09-06T15:53:42.357Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:53:47.437Z] TOOL RESULT

```
# Etymology of Proto-Germanic *harduz

## PIE Root
The traditional etymology derives from Proto-Indo-European **\*kort-ús**, formed from an o-grade of **\*kret-** meaning "strong, powerful."

## Cited Cognates
The article mentions Greek cognates:
- Ancient Greek **κρατύς** (kratús, "strong")
- Ancient Greek **κράτος** (krátos, "strength, power, dominion")

Notably, the document does not cite Sanskrit cognates, though it does reference comparisons with other Indo-European languages including Lithuanian **kartùs** ("bitter") and Proto-Slavic **\*kortъ̀kъ** ("short").

## Alternative Etymology
Some scholars (Strunk, Heidermanns, Kroonen) propose an alternative derivation from **\*(s)ker-** ("to cut"), though this remains less established as the primary theory.
```


## [2026-09-06T15:53:55.600Z] TOOL CALL #40: WebSearch

```json
{
 "query": "کنگره ریشه‌شناسی فارسی حسن‌دوست kongereh battlement etymology Sanskrit kaṅkaṭa"
}
```


## [2026-09-06T15:53:57.170Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D8%B1%DB%8C%D8%AF%D9%86",
 "prompt": "Persian خاریدن (xâridan) 'to scratch, itch': give the etymology — Middle Persian, Proto-Iranian, PIE root if given."
}
```


### [2026-09-06T15:53:59.177Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:54:03.361Z] TOOL RESULT

```
Web search results for query: "کنگره ریشه‌شناسی فارسی حسن‌دوست kongereh battlement etymology Sanskrit kaṅkaṭa"

Links: [{"title":"فرهنگ ریشه‌شناسی فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%B3%DB%8C_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"فرهنگ ریشه‌شناختی فارسی، محمد حسن‌دوست، 1393 تهران، فرهنگستان زبان و ادب فارسی، دورۀ پنج جلدی","url":"https://lsi-linguistics.ihcs.ac.ir/article_1976.html"},{"title":"محمد حسن‌دوست - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86%E2%80%8C%D8%AF%D9%88%D8%B3%D8%AA"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی | راهک","url":"https://raahak.com/?p=942"},{"title":"محمد حسن دوست نویسنده کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) | ایران کتاب","url":"https://www.iranketab.ir/profile/23034-mohammad-hasandust"},{"title":"کتاب فرهنگ ریشه‌شناختی زبان فارسی (جلد 5)","url":"https://fanuus.org/library/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AC%D9%84%D8%AF-5/"}]

The search results provide information about the Etymological Dictionary of Persian Language (Farhang-e Risheh-Shenasi-ye Zabaan-e Farsi), a specialized lexicon for Persian etymology authored by Mohammad Hasan Doust, published in 2014 in five volumes by the Academy of Persian Language and Literature.

This work won the 33rd edition of the Book of the Year Award in the "Ancient Languages" category in 2015. Doust previously published the first volume of this dictionary in 2004, containing letters "A-T".

However, the search results do not contain specific information about the etymology of "کنگره" (kongereh/battlement), its connection to Sanskrit kaṅkaṭa, or specific etymological entries from Doust's work. To find information about the specific word etymology you're asking about, I would need to search more specifically for that term's etymological analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:54:09.991Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG xar scratch ===\"; grep -n -i \"scratch\" CHEUNG.txt | head -20\necho \"=== CHEUNG xār- ===\"; grep -n \"x̌ār\\|\\*xar-\\|xāridan\\|xārīdan\" CHEUNG.txt | head -20",
 "description": "Cheung for scratch"
}
```


### [2026-09-06T15:54:10.052Z] TOOL RESULT

```
=== CHEUNG xar scratch ===
6103:*draub ? ‘to scratch, peel off ?' 
6119:dropt ‘to tear, scratch; to comb’. > If Oss. reduvyn, etc. does contain *draub, we 
6124:off’, Russ. drapat’ (obs.) ‘to scratch’ Gr. ópémo ‘to cut off’, etc. See *drap. 
6129:«PIE ? *d’reub"- ‘to scratch (off) > LIV: 156 | Pok.: 275 
6131:*IE COGNATES: Gr. ópónco ‘I scratch the cheeks (as a sign of mourning)’, Өролто ‘I 
10489:*huar ‘to have a sore, scratch, itch’ 
10494:(Sina) xuriän, Zaz. vurnäyis/vurnen- ‘to scratch’, Awrom. wuriäy/wuria- ‘to itch’, 
10496:xanahe/xan-, Gz. yam-/yarna, Nn. xärnäye/xärn-, Tr. xornaya/xorn- ‘to scratch’ 
10497:(contaminated with *xrau ‘to tear, break, scratch’ ?) || (+ *a-) ? Bal. (EHB) awali0/ 
10501:scratch (oneself), Yzgh. X"er (in X"er К. ‘to be scratched), (caus.) xértin- ‘to cause 
10502:to itch, scratch’, Sangl. xür-/xorió ‘to scratch (oneself), ? Pash. xriyal/xriy- ‘to 
10503:shave’, ? M. xréd-/xrést-, Y1. xird-/xirst ‘to shave, scratch’ (diff. root ?, contamin. ?), 
15320:*NWIR: Bal. kudit/kud- ‘to scratch, wound, injure’, Tt. (Tak.) akun/akund, (Cha.) 
15755:*IE COGNATES: always with initial *s-: Gr. скблто ‘to dig’, Lat. scabö ‘I scratch, 
16185:*IE COGNATES: Hitt. /gulsanzi/ ‘they scratch into’, Gr. téAoov (n.) ‘last furrow of the 
20544:*MIDDLE PERSIAN: ВМР Ind- /rand-/ ‘to scratch, grate, abrade, rake’ 
20551:*KHOTANESE: LKh. ran- ‘to scrape’ || (+ *aua-) OKh. varras- (varri-) ‘to scratch’ || (+ 
20563:< Ir. *-d- ?) || (+ *uz-) Wa. zrand-/z(a)rast-, z(o)rond- ‘to scratch, scrape’ 
22674:*IE COGNATES: Olrish sceirtid ‘shaves, scratches off’, Lith. skerdZiü (skefsti) ‘I 
22723:*CHORESMIAN: k’w- ‘to scratch, rub’; m/kw- ‘to pluck’ || (+ *pari-) prk’w- ‘to curry’ 
=== CHEUNG xār- ===
```


## [2026-09-06T15:54:12.519Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC leaf for kongar/kankarta (1632) ===\"\ngrep -n \"kongar\\|konkar\\|kankar\\|kankat\" IEC.txt | head -20\necho \"=== IEC around 'karkr' 'kar-' hard ===\"\ngrep -n \"^karkaros\\|karkaros\\|kartus\\|kartos\" IEC.txt | head -20",
 "description": "IEC kongar"
}
```


### [2026-09-06T15:54:12.579Z] TOOL RESULT

```
=== IEC leaf for kongar/kankarta (1632) ===
6735:kankər- (kanker-) (?) “hook, bend, curl’ Lat. cancer ‘crab’; Cz. kucera ‘curl’. (Isopho- nic: Latv. kankars, m. 'tatter)
=== IEC around 'karkr' 'kar-' hard ===
6842:kartus ‘hard, harsh, bitter’. Cf. WP I, 354 & II, 578. Cf. kratus Gk. *kartüs ('strong', cf. kártos ‘strength’ be- side krátos, id.); Go. hardus (‘hard, cruel, and com. Gmc.); Li. kartüs “bitter”
```


## [2026-09-06T15:54:19.387Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10485,10512p' CHEUNG.txt",
 "description": "Cheung *huar/xar scratch"
}
```


### [2026-09-06T15:54:19.432Z] TOOL RESULT

```
*REFERENCES: Abaev, Slovar’ I: 225; DKS: 188a f. 


*huar ‘to have a sore, scratch, itch’ 

*AVESTAN: Y Av. x"ara- (n.) ‘wound, sore’ (Y 57.10, V 4.30, V 4.33, etc.) 

*NWIR: Kurd. (Kurm.) xurin/xuré- ‘to itch’, (Sor.) xurandin/xuren-, (Sul.) xurin, 
(Sina) xuriän, Zaz. vurnäyis/vurnen- ‘to scratch’, Awrom. wuriäy/wuria- ‘to itch’, 
(caus.) NP xärändan/xärän-, Awrom. wurnäy/wurn-, Abyan. xürnoya/xürn-, Ard. 
xanahe/xan-, Gz. yam-/yarna, Nn. xärnäye/xärn-, Tr. xornaya/xorn- ‘to scratch’ 
(contaminated with *xrau ‘to tear, break, scratch’ ?) || (+ *a-) ? Bal. (EHB) awali0/ 
äwal- ‘to blister (of hand and feet)’ (with unexpl. -/-) 

*NEIR: Oss. І. xaryn/xord, D. xwarun/xward, Sh. xir-/xird, Rosh. xirt ‘to itch, 
scratch (oneself), Yzgh. X"er (in X"er К. ‘to be scratched), (caus.) xértin- ‘to cause 
to itch, scratch’, Sangl. xür-/xorió ‘to scratch (oneself), ? Pash. xriyal/xriy- ‘to 
shave’, ? M. xréd-/xrést-, Y1. xird-/xirst ‘to shave, scratch’ (diff. root ?, contamin. ?), 
also Pash. xwar (m.) ‘skin, bark, peel, scurf’, Sangl. xurüs, M. xuri ‘itching’ 

9 This root appears to have solely Germanic cognates. 

«PIE *suer- ‘to have a sore’ = LIV: 613 | Pok.: 1050 


*IE COGNATES: OHG sweran ‘to have a sore, hurt’, OHG swero, Engl. sore 
*REFERENCES: EVP: 97 f.; IIFL II: 422a f., 267a f.; EVS: 98a; MacKenzie 1966: 112, 111; Abaev, Slovar’
```


## [2026-09-06T15:54:22.506Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport io\nd=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=d.split('\\f')\nprint('nleaves',len(leaves))\n# find leaf containing 'qusero,'\nfor i,l in enumerate(leaves):\n    if 'qusero, i' in l or 'quseros ‘rough' in l:\n        print('qusero leaf',i)\n    if 'kongro' in l or 'konkro' in l or 'kankarta' in l:\n        print('kank leaf',i, [w for w in l.split('\\n') if 'kank' in w][:3])\nEOF",
 "description": "Locate IEC leaves"
}
```


### [2026-09-06T15:54:24.445Z] TOOL RESULT

```
nleaves 858
qusero leaf 585
```


## [2026-09-06T15:54:41.754Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (542,543,544,830,831,832):\n    t=d[leaf]\n    print('==== leaf',leaf,'~ printed p',2*(leaf-15),'-',2*(leaf-15)+1)\n    print(t[:700].replace('\\n',' | '))\n    print()\nEOF",
 "description": "IEC leaves 543 and 831"
}
```


### [2026-09-06T15:54:43.257Z] TOOL RESULT

```
==== leaf 542 ~ printed p 1054 - 1055
 LW ?). (Isophonic: OCS podü, m. *food") | pondheió (pondhio) ‘press, probe, attack’. (Vocalism ambig.) MHG vanten, G venden, wv. “try, probe, find out’; OFris. fandia, wv. ‘visit’; OE fandian, v. “probe, explore, experience, visit"; cf. fandung ‘probe, search, temptation’; OS fandon, v. 'ransack; probe’; OCS poZdo, poditi, v. drive: Pol. pędzić, v. ‘drive’; Cz. pudit, inf. ‘impel’; Srb. puditi, inf. ‘scare off; cf. Pol. ped, m. ‘rush, dash; shoot, bud’; Cz. pud, m. "instinct". Here also EM. vanden, v. ‘visit’ | poluos — pordhimos, pordhmos | 20 | 25 | 30 | 35 | 40 | 45 | 976 | ponguos ‘whole, sole; total, Jot" (?). (Evi- dence ambig. Cf. panghus & bhngh-) Hitt. pankus, gs: pangawas, adj. “whole, all’; Mir óg, 

==== leaf 543 ~ printed p 1056 - 1057
 Cz. prach, m. ‘dust’, and com. Sl. beside R poròxa, f. ‘early snowfall’) | pork- (porKs-) (?) ‘surrounding, edge, rim’. Cf. perkus & WP II, 45 Ober. parsa- ‘court’; Gk. pórkes, m. “loop, ring, snath’; Lat. porca, f. (fridge, baulk’, but cf. porKos ‘pig’ and semantic note); W cf. variant: orch, pl. -au, f. ‘border, limit’ | porKos, à ‘hog; sow'. WP II, 78 Arm. (?) cf. mkn-harsnuk ('weaseP', lit. *mouse-pig'?); Lat. porcus, gs. -1 m. ‘pig’; (LW in) Gk. pórkos ‘hog, boar’; Umb. purka, porca, acc. pl. f. ‘sows’; Ir. orc, m. ‘pig, boar’; OHG farah, farh, n., MHG varch, gs: varhes, sn. id.; OE fearh, m. id.; OCS (dim. type) prasę, n. id.; Li. parSas, m. id. (LW in) Finn. porsas, s. ‘piglet’. (Lat. po

==== leaf 544 ~ printed p 1058 - 1059
 pòr- titi, v. (spoil, damage’, fr. *prt-) | portüno ‘be forthcoming, be welcome’. Cf. por-, tu-, tu-bhālos Gk. porsüno, v. “offer, provide, prepare, cher- ish’; Lat. cf. op-portünus, adj. ‘convenient, useful, apt, self-committed'; im-portūnus, adj. out of place; fretful; troublesome; absurd; urgent; cruel; shrewd'. (Li. pratünoju, -oti, v. lie hidden’ seems to be of independent ori- gin) | pos, variant of type post (posti), q.v. and cf. posteros. WP II, 79-9 Ober cf. pasa “behind, after’; Per. pas, id.; Oss. fás- & fäste, id.; Gk. pos- (in pos-ágo); Cyp. Arc. pós, prp. ‘toward, at, from’; LLat. po-ne, adv. “afterwards” beside LLat. pos, prp. ‘after’; Alb. (Tosk) pa ‘then’; Li. pas, prp. ‘near, 

==== leaf 830 ~ printed p 1630 - 1631
 ‘desired’; vairyo *desir- able’; varom & varo, gs: varáh-, n. ‘gift; Tokh. cf. A wäl, B wel, s. ( ‘king’, to ual- (2), q.v.); Gk. defect. vb. eilon, aor. ‘I chose’; Lat. (*-e- or *-o-) volo, inf: velle, defect. vb. ‘wish; OLat. cf. velim, v. ‘may wish’; Osc. cf. vellia-, f. ‘will: It. voglia, id. beside Rumansh veglia, id.; cf. also lat. volup, volupe, defect, adj. (pleasant, fr. *uel-/uol- + *op- in opes ‘wealth, power, help’; and volup-tàas, cf. Umb. gs. opeter “of the best’: Skt. aptas, n. “act of sacrifice’. See op- (2) and (3) and opoetom. Not as WH); Ir. feillim, v. ‘suit, please’; Go. wiljan, wv. ‘wish’; wilja, f. id.; MHG wëllen, wv. anomal. vb. ‘wish’; Du. willen; OE willan, id. be

==== leaf 831 ~ printed p 1632 - 1633
 ‘better’; OE cf. we- lig, adj. ‘rich, prosperous, abundant, fertile, luxurious’; Du. welig, id.; LG welig “bright, gay, luxuriant’; Go. cf. ga-wiljis, adj. “willing, agreeable’; Scots walie, adj. ‘ample, large; jol- ly’; ON cf. vilgi, adv. “very, at al’; OCS velij, adj. ‘big’; OCz. velí, Srb. velji, id.; Li. vély, adv. ‘rather’. Compounding forms in Per. bali- *up- beside bali (“indeed, certainly, yes’: Li. vély “rather?); Ir. feile- ‘very’; Go. waila-, px. *well2; OE, Du. wel, wel- ‘very, fully’; OCS, Cz. Slovene vele-, px. "great" Verbal forms: Per. balidan, inf. ‘grow’; Tokh. A. cf. wäl, B | uel- — uelik- (uelk-) | 20 | 25 | 30 | 35 | 40 | 45 | 1510 | walo ‘king’; OE wealian, v. "be defiant’; Sw. vilja, v

==== leaf 832 ~ printed p 1634 - 1635
�mina, pl., vellemina & vellimina, n. s. & pl. id. | (uelnó, possible reconstruction of Lat. vello, see uel- (4) & cf. ueluó) | (uelquóo, possible reconstruction of OCS vlékg & Li. velkü, Latv. velku, see uelk- above, and cf. suelk-) | (uelsó, possible reconstruction for Lat. vel- lo, ére ‘tug’, but cf. uel- (4) & uelno. Ambig. also in Lat. vellus, gs: -eris, n. ‘fleece; foliage’, but cf. OCS (o-gde) vlasü, m. ‘hair’, and com. SL) | (uelumn-, see uelmn- and uelumn- (1) and Ou | uelutrom “wrap, cover. Cf. uel- (2), but ambig. in Skt. | Skt. varutram, n. ‘cloak’; Gk. élutron, n. ‘wrap, sheath, veil; shell | ueluel-, redup. of type uel- (2) in Gk. elelízo, v. ‘whirl’; Lat. volvulus, m. "feld. roller. The rad
```


## [2026-09-06T15:54:56.301Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,l in enumerate(d):\n    for pat in ('kankər-','kartus ‘hard','karkaros','kongar','kankarta','kseros (2)','quseros ‘rough'):\n        if pat in l:\n            print(pat,'-> leaf',i,'printed p',2*(i-15),'/',2*(i-15)+1)\nEOF",
 "description": "Locate IEC entries by leaf"
}
```


### [2026-09-06T15:54:57.889Z] TOOL RESULT

```
kankər- -> leaf 269 printed p 508 / 509
kartus ‘hard -> leaf 274 printed p 518 / 519
kseros (2) -> leaf 325 printed p 620 / 621
quseros ‘rough -> leaf 585 printed p 1140 / 1141
```


## [2026-09-06T15:55:10.412Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%86%DA%AF%D8%B1%D9%87",
 "prompt": "Persian کنگره: give any etymology given (Persian section), meanings (battlement, congress?), and any Middle Persian/Sanskrit source."
}
```


## [2026-09-06T15:55:11.534Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"کنگره\" \"قاطر\" \"استاندارد\" \"دموکراسی\"; do echo \"=== $w ===\"; grep -o -m3 \".\\{0,160\\}$w.\\{0,160\\}\" MON_part1.txt MON_part2.txt 2>/dev/null | head -4; done",
 "description": "grep Mo'in text for words"
}
```


### [2026-09-06T15:55:16.399Z] TOOL RESULT

```
# کنگره (Kongre/Kongore)

## Etymology

The word has two distinct etymologies:

**Etymology 1** lacks detailed explanation, marked as incomplete in the dictionary entry.

**Etymology 2** is clearly documented: "Borrowed from French _congrès_, from Latin _congressus_." As a proper noun referring to the US legislative body, it functions as "a calque of English _Congress_."

## Meanings

The term carries multiple definitions depending on context:

1. **Architectural**: "merlon, battlement" and "pinnacle, turret"
2. **Tool-related**: "notch, tooth (of a tool)"
3. **Modern/Political**: "congress; conference" and "Congress" (the US legislative body)

## Linguistic Origins

No Middle Persian or Sanskrit sources are mentioned in this entry. The document indicates the architectural sense represents the original Persian usage, while the modern political meaning derives from European language borrowing through French and English pathways.
```


### [2026-09-06T15:55:29.140Z] TOOL RESULT

```
=== کنگره ===
=== قاطر ===
=== استاندارد ===
=== دموکراسی ===
```


## [2026-09-06T15:55:34.164Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la MON_part1.txt MON_part2.txt; head -c 400 MON_part1.txt; echo; echo ---; head -c 400 incoming/MON/MON_2vol_Adena_v2_djvu.txt",
 "description": "Inspect MON files"
}
```


### [2026-09-06T15:55:34.218Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم �
---
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


۰ 
۳ 


فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ 


۲ج 
(دوره) :964-7252-51-2 :158 
(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] 
فهر ستنویسی بر اساس اطلاعات فیپا. 
۱. فارسی -- واژه‌نامه‌ها. الف. عنوان. 
۴۵ف ۲۹۵۴/۸
```


## [2026-09-06T15:55:38.759Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON\nfor w in \"کنگره\" \"قاطر\" \"استاندارد\" \"دموکراسی\" \"خرچنگ\" \"خارا\"; do echo \"=== $w ===\"; grep -h -o \".\\{0,140\\}$w.\\{0,180\\}\" MON_2vol_Adena_v1_djvu.txt MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -3; done",
 "description": "grep Mo'in Adena for words"
}
```


### [2026-09-06T15:55:55.756Z] TOOL RESULT

```
=== کنگره ===
=== قاطر ===
=== استاندارد ===
=== دموکراسی ===
=== خرچنگ ===
=== خارا ===
```


## [2026-09-06T15:56:00.455Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%82%D8%A7%D8%B7%D8%B1/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for قاطر verbatim, including any bracketed origin tag such as [ع.] or [تر.] or [سغد.]. Also quote the لغت‌نامه دهخدا etymology note if present."
}
```


## [2026-09-06T15:56:02.161Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%86%DA%AF%D8%B1%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for کنگره verbatim, including any bracketed origin tag. Distinguish کنگره ۱ (battlement) from کنگره ۲ (congress, French)."
}
```


### [2026-09-06T15:56:07.919Z] TOOL RESULT

```
# قاطر - Dictionary Entry

## From فرهنگ معین (Mo'in Dictionary):

**(طِ) [تر.] (اِ.) استر، حیوانی که از جفت گیری خر نر و اسب ماده بوجود آید.**

The bracketed tag **[تر.]** indicates the source is marked as Turkish (Turkic).

## From لغت‌نامه دهخدا (Dehkhoda Lexicon):

The etymology note states that while some scholars attribute this to Turkish origin, the entry notes: **"ظاهراً این لفظ به تای فوقانی بوده و متأخرین به طاء بدل کرده اند"** (apparently this word originally had an upper ta and later scholars changed it to ط).

The Dehkhoda entry describes the animal as one produced from the union of a male donkey and mare, stronger than a donkey but smaller than a horse, with remarkable endurance in difficult mountain terrain.
```


### [2026-09-06T15:56:08.654Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for کنگره

The dictionary provides two distinct definitions:

**کنگره ۱ (Architectural):**
"(کُ گِ رِ) (اِ.) شرفه، دندانه، دندانه های بالای دیوارها و بلندی های هرچیزی"
[Battlement, indentation, notches atop walls and heights of things]

**کنگره ۲ (Assembly):**
"(کُ گْ یا گِ رِ) [فر.] (اِ.) مجلسی متشکل از نمایندگان چند دولت یا عده ای دانشمند برای بحث و گفتگو، همایش"
[An assembly comprising representatives of multiple governments or scholars for discussion, a convention]

The bracketed origin tag [فر.] indicates the French etymological source for the second definition. The dictionary clearly distinguishes the architectural sense (fortification elements) from the political/academic gathering sense borrowed from French.
```


## [2026-09-06T15:56:23.556Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD leaf for 4270 xartare ===\"\npython3 - <<'EOF'\nd=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(d):\n    if 'xartare' in l or 'yrtr' in l:\n        print('leaf',i,'printed ~',i-66)\n        print([x for x in l.split('\\n') if 'xartare' in x or 'yrtr' in x][:4])\nEOF",
 "description": "SOD page for xartare"
}
```


### [2026-09-06T15:56:25.244Z] TOOL RESULT

```
=== SOD leaf for 4270 xartare ===
leaf 235 printed ~ 169
["4270 yrtr'k B                                           j&          stinking", '     xartare ©<*xara-tara-, Turk.      =*xrtry']
leaf 246 printed ~ 180
['      VJ 1030                                                    4537 yyrtr                                     j^cj^', "4528 yyp6      B, S     j->)(^bj' jT jl «y JU <ju <->>- <o^     4538 yyrtrcyq     S                                */ j>*", "     yi/er ? (yyr) =*yyrtr                                      4542 yyscn'k *» yysc'n'k"]
leaf 499 printed ~ 433
['       xartare ^yrt^k']
leaf 512 printed ~ 446
["      reproach ?                                            10947 yy'rtr <* yyrtr"]
leaf 513 printed ~ 447
['10953 yyrtr     B                                             10964 yyws- B                                 ^^T']
leaf 539 printed ~ 473
["         gold-coloured                                            11584 zyrtr'p'k B                            J*jl*&jjJ*s"]
```


## [2026-09-06T15:56:27.076Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB xrad/xar ===\"; grep -n \"xrat\\|xrad\" NYB_vol2_glossary.txt | head -10\necho \"=== NYB xar ===\"; grep -n \"^xar\\b\\|xar |xar,\" NYB_vol2_glossary.txt | head -10\necho \"=== HUB xar ===\"; grep -n -i \"Esel\\|xar\" HUB.txt | head -15\necho \"=== TTS katir ===\"; grep -n -i \"katir\\|qatyr\\|Maulesel\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -10\necho \"=== LKT katir ===\"; grep -n -i \"katir\\|qatir\\|Maulesel\" LKT.txt | head -10",
 "description": "Nyberg, Hübschmann, Vambery, Lokotsch"
}
```


### [2026-09-06T15:56:27.174Z] TOOL RESULT

```
=== NYB xrad/xar ===
693:isn ['sn'] innate, inherent, primordial: ~ xrat (q.v.); ~ vir 3922. — Borrowed from Av. (341) lāsna-; Paz. den, Skr. v. naisargika.
873:azateh ['e'tyh] 1. feudal benefice, fief 1173; xrat ~ the wealth of his Wisdom 917; generosity 70%. — 2. sg. cas. obl. of āzāt (2), q.v. — 1. From àzàt (1); Paz. āzādī, Skr. v. prabhutva ‘dominion, wealth', ažadi, Skr v. rddhatva, sampatti ‘prosperity, abundance’ (SGV); MPrs »zdyy, ’z’dyy ‘inheritance’ (thus Péri- khanian, l. c. s. v. āzāt, p. 16; the passages from A-H II).— 2. MPrth "z'dyft ‘free- dom’; NP āzādī ‘liberty, freedom from worldly cares’.
909:band [bnd] tie, band, bond; fetters 919. 34! (81? probably mistaken for bry<n> = brin, cf Mx ch. 279; Paz. is wanting); ~ + zēndān imprisonment, captivity 9°; ~ the snare of Death 6514-18; ca rād ka menčyan u gētīkān dänisn u kār-ākāhēh har 2 band 6 tč [i.e. xrat] patvast why are knowledge and skill of both the heavenly and the earthly beings (so) closely tied up with (dependent on) thee [the Wisdom]? 8811-12; the Skr. v. joins band with the preceding har 2: dvdvapi bandhau, but this is contradicted by 12017-18; cigön martömäan i andar gété band 6 mēnēyān patvast estet as men in this world are closely tied up with the heavenly beings. — Av. (926 sq.) banda- ; MPrth. bnd; bndys?n ‘prison’ (MHC); MPrs bnd (A-H II), bn = bann (S, A-H I), bnyst’n = bannistän < band- (A-H I); Paz. NP band. V. bastan.
1044:burtan [bwltn'; YBLWN-, YDLWN-tn'; forms v. I, 178] bar-, to carry, to bring, to bear, to wear, to procure; to take away, to remove (6 or pat ‘to’); arišk ~ to bear envy 691. 8419; !a&, bes, dast, dašn, gobišn, nam, namāc, nipart, paitäk, srav, stēžak, vāng, pat xrat ~: v. these ws.; bahr ~ v. barišneh; — to place on the top of (apar) 444; to lay a p. on (6) 4720-21; — andar 6 tan ~ to bring into corporeal existence 92t; — andarg ~, v. göbisn; — apar ~ to send out against 3711; to bring 6016; dmdcisn apar ~ to give instruction, to teach 80%; v. also apar-barisneh and apar-burtäreh ; — frac ~ to bring, to present 411; to bring forth, to light (a fire) 44°; — fröt ~ to bring down, to shed (water) 417°; v. also fröt- barišneh; — 6 ham ~ to collect, to amass 4815; pret. construed as an act. 187% Common Iranian; Av. OP (933 sqq.) also — (act. and middle) ‘to ride’, cf barak and asvār; cf also apar-barišneh from bar- ‘to move’.
1188:~ kē that 397?; with obj.: passim; with inf. to know how to, to manage to 5026.27, 511-2, — Av. (1659) zan-, OP dan-; MPrth z’n’dn z’n-; MPrs d'nystn d’n-; Paz. dä- nastan, dänestan dan-, NP dänistan. danišn [d'nšn'] knowledge 661, 803-5; ~ u kār-ākāhēh 881.23; m <u> xrat 4 martömän 10414; akahéh u ~ 1095, ~ u ākāhēh 111’. — MPrs d’nysn; NP dans. dānišnēh det. v. n.: uspurrikiha (q. v.) ~ 10615-16.
1856:ham-pursakik adj.: magūnē ~ xrat the wisdom (understanding) of the Magi won through consultation (of the gods) 112}.
2131:jāyišn [y?dšn'], 70!? jahišn [yhšn'] For- tune, luck, dispensation 2?!. 145; ~ u zaman <i> brihenišn rād 14'?, v. zaman; murvāk ~ i névak augury (and) good Fortune (i.e., good Fortune revealed through augury) 18!; pat névak ~ <u> yazdän hayyārēh with good fortune and the help of the gods 121-4; 121°; pat ~ hayyārēh i pat martömän xrat veh For- tune (giving aid to =) favouring men, wisdom is the best thing [she gives] 7012-13, Skr. v. siddheh sahāyatāyai ma- nusyanam buddhih uttamā; cf ke [for ka] ~ hayyär pat martömän cis + xrat veh when Fortune (is a helper to =) favours men, wisdom is the best of things PT 675-5, with the explanation cé hakar par- kast xvāstak be šavēt aivāp cahārpād be mirét xrat bē mānēt for if wealth dwindles and is lost or animals die wisdom remains; pātixšāi han névaktar i... xrat u dānišn nēvak api-$ ~ hayyäreh apāk that ruler
2535:mčnči [mdnwd: thus the FrP] A. adj. heavenly, celestial, immaterial, ideal (in the Platonic sense), always placed before the subst.: ~ ästisneh 3871, ~ kamakéh 4022, ~ venišneh 1105, v. these ws.; ~ astéh heavenly peace 561%; ~ tag 4 den 561°, v. tag; — often with the ending -€ before the headw.: ~-é xrat the Heav- enly Wisdom (personified) 68~77, passim ; 7-6 asn-xrat 76144; ~-é€ + a long series of abstract virtues 8514-18 ‘heavenly, of heavenly origin’; ~-é dätistän 171%, — B. subst. 1. pers.: immaterial, spiritual be- ing: apazönik ~ Ohurmazd 3985; ganäk (v. this w.) ~ the Evil Spirit, Ahriman;
2539:spannäk ~ 659, spenäk (-nāt) ~ 10215-17, 10312, 106% = Av. Spanta-Mainyu-; 3 ~ 654; ~ i véh a good spirit, opp. ~ % vattar an evil spirit 651; pl. the celestial gods, pl. cas. obl. ~-dn 40%. 578, 5924, 7218, 7416, 8917.25, with the app. yazdan 7413-18; opp. gétikan, v. getik, 34". 2. the heavenly world, the beyond, opp. geteh, getah 3612, 629.1", 6819-20, 723; har 4 m opp. hir i getäh 6814, 798-11-12, 8023.25; šahr t ~ the realm of Heaven 667; mizd i ~ the reward of Heaven 62°. 658. — Av. (1136) mainyaoya-, adj. of mainyu- (v. s. v. dušmen); Paz. mainyč, minč etc.; NP minč ‘heaven’. The spelling mdnwd of FrP 1 (glossed by mynwy) is constant throughout the whole of BP, and must not be emended to mynwg or mynwk. An adj. mēnēk < *mainyava-ka- is so far only attested in MPrs: mynwg $h ‘the Heavenly King‘ (List 85), and the abstr. mynwgyh ‘the quality of possessing an animal spirit (menög)’, of the body, as opposed to gy’n and rw’n ‘the soul’, a purely Manichean terminology quite for- eign to Zoroastrianism. The Zoroastrians have always understood mönöi as an adj., rendering it in Skr by paralokiya, paralokacara, Sünyacärin (‘existing in the air-space', e.g. 7712. 8514-18), adrsya ‘in- visible’ (SGV), only in the sense of B 2 by a subst.: pat mēnči 723 Skr. v. paraloke. The construction of this adj.: optional addition of the ending -č and position before its head w., is taken over from the NW area, and known from Bal., where the adj. is regularly placed before its headw. and may, or may not, take the ending -e (thus Gilbertson) or -e, -en (thus Longworth Dames; traces of this ending in BP v.s. v. harvistén harvén, névakén). When this construction was borrowed by the SW language the ending -€ was mistaken for the izäfat; hence the translations of the Dasturs: paralokīyā yà buddhih for menöye xrat, ete.
2580:miyānjīkihā mediately: ~ pat rah i xrat through the medium of Reason 6215,
=== NYB xar ===
4274:xar [HMR] donkey 2415. 303. — Av. (532) zara-; NP zar.
6890:xar(a)nidan: kirrenikan
=== HUB xar ===
933:213. Das in der Anmerkung erwahnte phi. xarbuz (Bdh.
934:57, 8, West, PT. I, 48) = 'Esel-ziege, das Noldeke
936:vor: xarbuz eine Ziegenart, oqv^ Deuter. 14, 5 und
950:215. Zu ba^m *Gesellschaft, Gastmahl, Gelage' (Fird. I,
1784:LW. Caxr *Drehung , 6axr-em 'kreise', Saxarak 'Dreh-
1835:afgh. LW. xar *Dorn' = arm. xar^ xar *Dorn (Galen);
1836:np. xWra^ xara *harte Stein, Fels' = arm. xarak harte
1838:urverwandt) und xari *penis' (der Worterbiicher) hierher
1870:474. Vgl. ZDMG. 46, 234. Dazu arm. xarbzak 'Melone' (nur
1872:475. Np. xarSang *Krebs' aus phi. karcang mit volksety-
1873:mologischer Anlehnung an die Composita mit xar Esel
1874:(vgl. Vullers s. v. xar 2), so dass nun das Wort
1875:aus xar 'Esel' und cang *Kralle' zusammengesetzt er-
1877:476. Lies arm. xrat (fur xart),
1911:482. Zu xartdan *kaufen — skr. krz 'kaufen' gehSrt gr. ngi
=== TTS katir ===
5406:trocknen;  Ä"a^a^  =  Feuerstahl  (vgl.  ^•aja  =  Fels);  katiriJc^^ 
=== LKT katir ===
339:[Kelekian  Kämas  32]  'Sattel-  od.  I'ack- pferd,  Wallach'.  Hieraus  russ.  losad' 'Pferd'  u.  viele  Ableitungen,  klruss.  losa 'Pferd',  losak  'Maulesel',  poln.  loszak 'Pferd,  kleines  Tataren pferd'.  [Gorjajew 192.    Bern  SlEtWb  734.
1430:'Esel',  kas.  tat.  isak  [nach  PEDERSEN ZDMG  LVIl,  561  (nicht  567,  wie  Bern SlELWb  438  steht)  auf  armen,  es  'Esel' zurückzuführen ;  vgl.  weiteres  in  IF  XXII, 198];  hieraus  russ.  «Äafc 'Maulesel',  serb. esek  'Esel'.    [Gorjajew  125.
2664:'Maultier';  hieraus  rum.  cat'ir  'dass.', catirä  'Mauleselin';  bulg.  katzr,  serb. katura,  russ.  (dial.)  katjer  'Maultier'. [Sain48.  Gorjajewl36.  Bern  SlEtWb  495.
3870:'Zug  von  Reisenden  auf  Lasttieren'; hieraus  kat.  sp.  ricua,  pg.  recova  'Koppel Lasttiere',  pg.  recovar  'Tiere  treiben', recoveiro  'Mauleseltreiber'  [Constancio Dicc  833  a].  [DE  329.  Eguilaz  480. ML  7191.
```


## [2026-09-06T15:56:44.422Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT context ===\"; sed -n '2655,2670p' LKT.txt\necho \"=== SOD entry 4169 / donkey ===\"\npython3 - <<'EOF'\nd=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(d):\n    if '4169' in l and ('yr' in l or 'donkey' in l):\n        print('leaf',i,'printed ~',i-66)\n        for x in l.split('\\n'):\n            if '4169' in x or '4168' in x or '4170' in x: print('   ',x)\nEOF",
 "description": "Lokotsch katir and SOD donkey entry"
}
```


### [2026-09-06T15:56:46.365Z] TOOL RESULT

```
=== LKT context ===
1126.  Hebr.  kätön:
'Klein' ;  dieses  Wort  kommt  in  dem ndl.  Ausdruck  houd  je  maar  katoen 'halte  dich  mal  ruhig  oder  stille!'  vor.
1227.  Ar.  katrä: 'Stück  (Fleisch,  Fisch  oder  ähnl.)' ;  hier- aus mit  ar.  Art.  pg.  alcatra  'Hinterviertel
eines  Ochsen'.  Ar.  plr.  katrät;  hieraus pg.  alcatraie  'Kielpflock  (ein  Teil  des Kiels  am  Schiffe)'  [Constancio  Dicc  45c; DE  88/89].
1128.  Ar.  katrä  :
'Teer'  [vom  Vb.  katara  'tropfenweise fließen',  vgl.  dazu  aram.  'atränä  'Teer' <  ass.  etränu  'dass.'  ZAkkFW  60] ;  hier- aus z.  T.  über  tk.  katran  'dass.':  rum. catran  'Teer,  Gift  und  Galle',  cäträni 'teeren',  it.  catrame  'Schiffsteer',  afrz. cotran,  nfrz.  guitran,  goudi-on,  prov. catran,  sp.  alqtiiträn,  pg.  alcaträo  'Schiffs- teer'; bulg.  serb.  katran,  serb.  katram 'Schiffspech',  russ.  katran  'Erdpech'. [DE  186.  Eguilaz  251.  ML  6902.  Bern SlEtWb  494.
1129.  Zigeuu.  katsTiua: 'Wirtshaus,  Schenke'  [Fink,  Lehrbuch des  Dialekts  der  dtsch.  Zigeuner.  Mar- burg 1903.  Glossar  s.  v.  Vgl.  auch Jesina,  Romäüi  Gib.  ^.  Leipzig  1886. S.  84  b:  Iröma  <  öech.,  s.  MSISI  278] ; hieraus  gaunerdtsch.  Kaschemme  'ge- wöhnliche Kneipe',  katschänme  [Ave-L IV,  554].
1130.  Ar.  kattära: 'Destillierkolben'  [vom  Vb.  kattara 'destillieren',  II.  Form  von  katara  s.  hier Nr.  1128];  hieraus  mit  ar.  Art.  sp.  alqui- tara  'Destilliergefäß'  [=  alatnbiqne,  s.  hier Nr.  79.    Dicc  Gast  137  a.    DE  186].
1131.  Tk.  katyr:
'Maultier';  hieraus  rum.  cat'ir  'dass.', catirä  'Mauleselin';  bulg.  katzr,  serb. katura,  russ.  (dial.)  katjer  'Maultier'. [Sain48.  Gorjajewl36.  Bern  SlEtWb  495.
1132.  Ar.  kaukab:
'Stern',  eigentlich  k.  simäli  'Nordstern', d.  h.  Polarstern.  Der  Name  wurde  durch Verwechselung  auf  den  Stern  ß  über- tragen, der  jetzt  Kochab  heißt.  [Ideler Stern  n  14.
1133.  Hind.  kauri:
Od.  kaiidl  [aus  sskr.  kaparda]  'eine kleine  weiße  Muschel  Cypraea  moneta', die  in  einem  großen  Teil  Asiens  und Afrikas  als  Geld  in  Umlauf  ist.  Ihr Wert  ist  Schwankungen  unterworfen, z.  B.  werden  bei  den  Haussa  11  bis  18, an  der  Togoküste  40  und  an  der  Gold- küste 20  Stück  gleich  einem  Pfennige gerechnet  [vgl.  Globus  LXIX,  374  Anm.  2]. Hieraus  engl.cowry,  dtsch.  Kaurimuschel, frz.  cauris,  sp.  cauris,  pg.  cauril,  caiirim, coril  [Constancio  Dicc  237  c].  [Hobson- Jobson  269/271.  John  E.  Hertz,  Über Verwendung  und  Verbreitung  der  Kau- rimuschel. In  Mitteilungen  der  Geo- graphischen Gesellschaft  in  Hamburg 1880/81.
91
[Tk.  kawaV.
=== SOD entry 4169 / donkey ===
leaf 231 printed ~ 165
    4169 yr-3 B, S                                   >                          gadfly
     4170 yr»n     B => yrln
leaf 551 printed ~ 485
    dismounting      1895                  donkey        4169, 10622               dry land   1753, 9240, 10225
leaf 642 printed ~ 576
    986          andeslk                 andesek                     2853                                 ©*fra-trya-             4169        +
```


## [2026-09-06T15:57:04.024Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT standard ===\"; grep -n -i \"^Standard\\|Standard, a flag\\|estandart\" SKT.txt | head -5\necho \"=== SKT hard ===\"; grep -n \"Hard, firm\\|^Hard\\.\" SKT.txt | head -5\necho \"=== SKT cancer ===\"; grep -n -i \"Cancer, a crab\\|^Cancer\" SKT.txt | head -5\necho \"=== SKT democracy ===\"; grep -n -i \"Democracy\" SKT.txt | head -5\necho \"=== SKT carcinoma ===\"; grep -n -i \"carcino\" SKT.txt | head -5",
 "description": "Skeat lookups"
}
```


### [2026-09-06T15:57:04.113Z] TOOL RESULT

```
=== SKT standard ===
18358:Standard,  (F,  -  O.  H.  G.)  O.  K esfanJati,  a  Uandani  or  ensign,  a  standard mcosarc.  'I he  flag  was  a  lajge  (nc,  0x1  a fixed  (standing)  polc.-'O.  U.  G.  sfatui an, lo  stand  ;  with  suffix  -art  (  -O.  H.  G.  /lar/, a  siifTix,  orig,  the  i>ame  as  ^d/-/,  adj.,  hard) ^  Cr  Span,  tstau.iarte,  a  stand.ird  ;  O.  Du stofttfairt,  'a  standarO  or  a  ereat  trophic, a  pillar,  column,  mill-post  ^Hexham), evidently  from  the  verb  stand.  The  O.  I*'. esUH*itini,  Ital.  stemianh  are  modified  forms, as  if  ffotn  L  ext^uUrt.  to  siprcad  out.
=== SKT hard ===
=== SKT cancer ===
2718:CANCER.
22902:cancer— canker.
=== SKT democracy ===
944:democracy.  (F.— Gk.)  Formerly  *ir- miH'Oiy  (MU(on).  — Q.  F.jgmiMtafu ,  Cot.
=== SKT carcinoma ===
```


## [2026-09-06T15:57:04.998Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/standard",
 "prompt": "Give the full etymology of English 'standard' — Old French estandart, Frankish *standhard, and any alternative derivation from Latin extendere. Also note the date of first attestation."
}
```


### [2026-09-06T15:57:11.195Z] TOOL RESULT

```
# Etymology of English "Standard"

**First Attestation:** Mid-12th century

**Primary Derivation Path:**
The word originated from Old French *estandart* (Anglo-French *estandard*) and Medieval Latin *standardum*. According to etymologists Barnhart and Watkins, these likely derive from Frankish *\*standhard*, meaning "stand fast or firm"—a compound combining words cognate with "stand" and "hard."

**Original Sense:**
"Distinctive flag or other conspicuous object displayed from a position in battle to serve as a rallying point for a military force." The flag received this name because it was "fixed to a pole or spear and stuck in the ground to stand upright."

**Alternative Theory:**
The Oxford English Dictionary proposes folk-etymology, instead connecting the Old French term to *estendre* ("to stretch out"), derived from Latin *extendere*.

**Secondary Development:**
By the late 14th century, "standard" acquired a second meaning: "weight, measure, or instrument by which the accuracy of others is determined." This likely emerged from royal ordinance establishing official weights and measures as *the king's standard*, eventually metaphorically representing authoritative measures of quality and correctness.
```


## [2026-09-06T15:57:45.128Z] TOOL CALL #59: WebSearch

```json
{
 "query": "\"کنگره\" ریشه واژه دندانه دیوار \"کنگر\" اتیمولوژی فارسی باستان"
}
```


## [2026-09-06T15:57:47.738Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg242.png data/verification/sources/refs/ocr/BOOK/242.png\nls -la data/verification/sources/refs/ocr/BOOK/ | tail -5",
 "description": "Copy page image for audit"
}
```


### [2026-09-06T15:57:55.647Z] TOOL RESULT

```
Web search results for query: ""کنگره" ریشه واژه دندانه دیوار "کنگر" اتیمولوژی فارسی باستان"

Links: [{"title":"کنگره - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%DA%A9%D9%86%DA%AF%D8%B1%D9%87/"},{"title":"معنی کنگره | واژه یاب","url":"https://vajehyab.com/?q=%DA%A9%D9%86%DA%AF%D8%B1%D9%87"},{"title":"کنگره (معماری) - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%DA%A9%D9%86%DA%AF%D8%B1%D9%87_(%D9%85%D8%B9%D9%85%D8%A7%D8%B1%DB%8C)"},{"title":"کنگره - ویکی‌واژه","url":"https://fa.wiktionary.org/wiki/%DA%A9%D9%86%DA%AF%D8%B1%D9%87"},{"title":"ریشه‌شناسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%B3%DB%8C"},{"title":"کنگره | در فرهنگ لغات ها (دهخدا،معین و ... ) + سایر منابع اطلاعاتی | جدول یاب","url":"https://jadvalyab.ir/moein/%DA%A9%D9%86%DA%AF%D8%B1%D9%87+"},{"title":"ادبی.مسائل روز | تیر ۱۳۹۹","url":"https://1350javad.blogfa.com/1399/04"},{"title":"معنی کنگره چیست | لغت یاب","url":"https://logatyab.ir/word/144443/%DA%A9%D9%86%DA%AF%D8%B1%D9%87"},{"title":"معنی کنگره - فرهنگ فارسی معین","url":"https://lamtakam.com/dictionaries/moen/26058/%DA%A9%D9%86%DA%AF%D8%B1%D9%87"}]

بر اساس نتایج جستجو، این اطلاعات درباره واژه «کنگره» و ریشه‌شناسی آن یافت شد:

## معنی کنگره

کنگره بلندی‌های سرِ دیوار، حصار، قلعه و دیوارها است. دندانه‌های مثلث یا نیم‌دایره که از گل، سنگ، یا آجر بر بالای دیوار، برج، و بارو می‌سازند.

## اتیمولوژی (ریشه‌شناسی)

درباره ریشه‌شناسی این واژه، ریشه و خاستگاه این واژه روشن نیست (برای دکتر کزازی). 

تک تفسیری دیگری وجود دارد که کنگره یک کلمه ترکیبی متشکل از دو کلمه است: کُن که برگرفته از کلمه کُوْن و مکان می‌باشد و گِره نیز یعنی به هم رسیدن و به هم آمیختن.

## ارتباط با کنگر

منابع اشاره می‌کنند که می‌توان به کنگر و کنگری مراجعه کرد برای اطلاعات بیشتر.

## استفاده در معماری باستان

کنگره در اغلبِ ساختمان‌های باستانی ایران، به‌خصوص در تخت جمشید، فراوان یافت می‌شود.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-06T15:57:57.166Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T15:58:06.990Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D9%82%D8%A7%D8%B7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/harduz\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%86%DA%AF%D8%B1%D9%87\" \\\n \"https://abadis.ir/fatofa/%D9%82%D8%A7%D8%B7%D8%B1/\" \\\n \"https://abadis.ir/fatofa/%DA%A9%D9%86%DA%AF%D8%B1%D9%87/\" \\\n \"https://www.etymonline.com/word/standard\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 242, root Kar 1 (Qar 1/Quseros/Qhar): xar, qater, xerad, harduz, kongareh, standard\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-06T15:58:14.378Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4267cf945b377290.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a28fb25d3d429f9c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c7bfbbf0ba43ddbd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1a8da24f08b41b89.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0581b10ced922645.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ac32a91de40453fa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f88a48b04940cec4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c7450309af77f4c4.txt
```


## [2026-09-06T15:58:21.316Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=d.split('\\f')\nprint('nleaves',len(leaves))\nfor i,l in enumerate(leaves):\n    if \"dissimilated  fr.  *carcro-  and  cogn\" in l: print('cancer leaf',i)\n    if \"Cp.  hardy,  -ard,  arditi\" in l: print('hard leaf',i)\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['KLN']\nprint(d['page_offset'])\"",
 "description": "Find Klein leaves and offset"
}
```


### [2026-09-06T15:58:22.951Z] TOOL RESULT

```
nleaves 903
cancer leaf 132
hard leaf 379
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-06T15:58:51.528Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nimport re\np='WLD_Bd1_pages.txt'\nd=open(p,encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor i,l in enumerate(d):\n    if 'khara' in l or 'kharás' in l or 'karkara' in l:\n        print('--- leaf',i, [x for x in l.split('\\n') if 'khara' in x or 'karkara' in x][:6])\nEOF",
 "description": "Walde-Pokorny Bd I for khara"
}
```


### [2026-09-06T15:58:53.060Z] TOOL RESULT

```
leaves 895
--- leaf 362 ['  Ai. karkara- „rauh, hart" = gr. xagxaooi  xoaycig Hcs., ai. karkaga-']
--- leaf 363 ['  Ai. khara- „hart, rauh, scharf“, np. xar, xdra „Fels,                               Dorn"', 'Z. B. Horn Np. Et. 102, Uhlenbeck Ai. Wb. 74 (ai. khara- m. av. xaro „Esel“', 'Substantivierung von khara- „hart“), Boisacq u. y.dgyagog.']
--- leaf 463 ['kamm, Flamme", cikhara- „spitzig, 2 ackig“, cekhara- n. „Scheitel, Gipfel,']
```


## [2026-09-06T15:59:00.691Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nd=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (362,363):\n    print('==== leaf',i)\n    print(d[i][:1800])\nEOF",
 "description": "WLD leaves 362-363 full"
}
```


### [2026-09-06T15:59:02.659Z] TOOL RESULT

```
==== leaf 362
354                                                  qar-, qarqar-



zweifelhaft(Thumb GGA. 1915, 24)                            und keine ausreickende   Stiitze    fiir

einen Ansatz qaro- (statt yard-).


3, qar-, redupl.          qarqar- u. dgl. „hart“.
  Ai. karkara- „rauh, hart" = gr. xagxaooi  xoaycig Hcs., ai. karkaga-
                                                                     ‘




„rauh, hart" (auch karaka- m. „Hagel“? Uhlenbeck Ai. Wb. 44); vermut-
lich gr. x.gava\j ]og „hart, rauh, felsig" (s. Boisacq s. v. ; aber xgdvog „Helm“
                      -




nicht „der Harte", sondern zu her- „Haupt“).
  Dazu wohl die Worte fiir Krebs: ai. karkata- m. „Krebs“ (karkin „Krebs
als Sternbild" L\v.             aus gr. xagxlvog)
  gr. y.agxivog ds.,            lat.   cancer, -cri ds. (diss. aus *carcro-, vielleicht schon
idg.,   vgl.   ai.      m. ,,Panzer“ aus *kav>krta-', s. Yf. LEWb. 2 s. v.
                     kchakata-
Umstellung aus * qarqno -, Ilavet Msl. 3, 196, Solmsen KZ. 34, 21 Anm., ist
nicht wahrscheinlicher).

  DaB aksl. roki           ,,   Krebs" aus *krakz diss. sei, ist sehr unwahrscheinlich
die Ahnlichkeit mit norw. (usw.) rake ,, cancer squilla, Garnele" (urn. rakion;
kaum *hrukion, als *qrcqn- zu unserm St., s. Falk-Torp u. rake) ist kaum
trugerisch, setzt aber             Entlehnung auf einer der beiden Seiten voraus.
  Ferner Worte fiir liarte Schale, NuB: ai. karaka- m. „KokosnuB, daraus
bereiteter Wasserkrug", knrwaka- m. „Schadel“ s. Scheftelowitz BB. 28,
145; kaum besser nach Uhlenbeck Ai. Wb. 44 mit idg. g“- zu got .hairnei
„Hirnschale“, anord. hvtrna „Schiissel“ usw.); gr. y.agvo    „NuS", xagva
„NuBbaum“: lat. cartna „NuBschale, Schiffskiel, Schiff“ (vielleicht aus dem
Gr. nach Keller Yolkset. 279, welchenfalls xagvivog die Qu
==== leaf 363
                                                  qar-   — qars-                                             355

„Verstand“ (Pedersen KZ. 39, 368, wo aueh nicht iiberzeugend arm. xorh-
hn „denke“ als Ableitung eines *qhor-tu- angereiht wird). Anord. herstr
„barsch“, mhd. harsten „hart werden" und mnd. Itarsch „hart, rauh“. nhd.
harsch (von Persson Beitr. 337 als st-, sk-Bildungen neben hart aufgefaBt),
bleiben bei ai. kasati „kratzt", aksl. krasta „Kratze“ usw. (s. Falk-Torp
u. harsh, Berneker 575); s. qars- „kratzen“.

  Uber mit bar-             (qar-) anl.   Steinbezeichnungen            s.   u.   *ak- „scharf“.


qar- „Wachs“.
   Gr. y.ygog „Wachs“, y.rjgtov „Wabe, Wabenhonig" kann, obwohl dor.
xagog (Fick I 4 378) nach OsthofF Par. I 1 8 f., Herwerden Lex. gr. suppl.
nicbt geniigend gesichert ist, auBerhalb des Ion.-Att. Lehnform aus dieser
Dialektgruppe sein, welchenfalls lat. cera als griech. Lw. (Fick BB. II 196)
gesichert und gegeniiber dem a der flgdn. balt.-slav. "Worte kein Ablaut
a:e (Kretschmer KZ. 31, 411) anzunehmen ware (s. Yf. LEWb. 2 s. v„
Giintert IF. 37, 85 f.). Lit. kort/s „Wabenhonig, Honigscheibe der Bienen",
                                                  5
lett. karites „Bienenzellen mit Honig" (Curtius     149), poln. skarsyk „der
YorstoB im Bienenstock“ (Zubaty AfslPh. 16,411).
  Unnatiirlich ist Osthoffs Trennung des lat.-gr. Wortes, das zu creo, cresco
mit der Ablautstufe von procerus , sincerits gehore, von den balt.-slav., die
entweder zu lit. karti „hangen“ oder zu lit. kiirti „bauen“ zu stellen seien.


qhar- „scharf,           spitz".

  Ai. khara- „hart, rauh, scharf“, np. xar, xdra „Fels,                               Dorn"
  redupl. gr. y.dgyagog „spitz, gescharft, beiBend", y.agyag-odcov „mit scharfen
Zahnen", y.agyaoeog „bissig
```


## [2026-09-06T15:59:19.431Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 -c \"\nd=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[362][1800:3600])\"",
 "description": "WLD leaf 362 tail (kratu section)"
}
```


### [2026-09-06T15:59:21.185Z] TOOL RESULT

```
elle ist).
   Fern bleiben air. e urar, mir. culardn ,,Gurke, ErdnuB", gall. (Yendryes
Msl. 13, 387 f.) Cnlaro „Grenoble“ („*Gurkenstadt“, wie Zixvtbv), cymr.
cylor, mbret. coloren, nbret. kclcr „ErdnuB" (Stokes BB. 23, 45 f.)    eine                 ;


Grundform *kahiro~ aus *kartdo- kann nicht angesetzt werden, da die
brit. Formen den Wz.-Vokal u erfordern.

  Mit t Suffixen: got. hcirdns „hart, streng", anord. hardr „hart“, ags. heard
„hart, stark, tapfer", as. hard, ahd. hart , herti „hart, fest, schwer", Adv. anord.
harda, ags. hcardc, ahd. harto mnd. harde „sehr, besonders" (vgl. gr. xdgxa)
                                             ,


urgerm. huntu- aus idg. * qar-tu   Auf Grand einer idg. Erw. qre-
                                                      .


iiol.   (Gramm.) x.gtxog, woneben mit dem Yokalismus des Adj.                        att.   xgaxog,
ep. jon. xaoxog „Stiirke, Kraft' 1 , horn, xgaxvg „stark“                 Komp. jon. dor. xgea-
oaav, att. y.oelxxcov, Sup. xoaxiaxog, ep. xdgziazog, Adv. xugxa „stark“ (zu

*xagxvg in xagxvvm „verstiirke“), xoaxegog, xagxsgog „stark, kriiftig, fest,
heftig" (usw., s. Boisacq 510 f., 514).
   Mit germ, hardu- hat trotz Meillet Et. 325, Zupitza Gutt. 109 (Lit.) nichts
                                         £
zu tun   lit. kartiis „bitter (  xdgo> usw.), aksl. cnstm „fest' £ (: xdgxaAog
                                                 :




usw.), arm. kurcr ,,hart, fest‘‘ (: yog-yog); auch Yereinigung mit qert- „zu-
8aminendrehen, kompakt‘ (Wood a x Nr. 427) ist nicht annehmbar.
   Ygl.   z.   B. Curtius 3 143, 144, Fick I 4 20, 377, III 4 78.
  Ai. knthind-, kdthora- „hart, fest, steif" kann auch mit idg. I zu cymr.
cahd, mir. calad .hart", gall, -calctos gehoren (s. qal- „hart“). Der Bed.
halber gewiii fer
```


## [2026-09-06T15:59:45.405Z] AGENT

Now I'll write the verification file.


## [2026-09-06T16:08:53.032Z] TOOL CALL #66: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk242.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nnodes = []\n\ndef N(**kw):\n    nodes.append(kw)\n\nN(id=1, lang=\"Avestan\", words=\"xratu\",\n  verdict=\"plausible\",\n  derivation=\"Avestan xratu- m. 'mental power, intellect, resolve' is well attested (Y. 25.6 asnahe xratus 'innate wisdom', Yt. 10.107, Yt. 1.7 xratu-mant-); Bartholomae, AiW col. 535 ff. Its Indo-Iranian match is Skt. krátu- 'power, resolve, insight', and the reconstruction is PIE *krét-us, a u-stem of the root *kret- 'strong'. Whether that root is the same as the *kar-/*ker- 'hard' of Nourai's box is exactly the point on which the sources disagree: Walde-Pokorny I 355 still filed Skt. krátu-/Av. xratu- 'Verstand' under qar- 'hart' (with the t-extension *qre-t- that gives Gk. kratos), but Pokorny's own 1959 revision at the page Nourai cites reverses this and says of Gk. kratos that 'remains far off Old Indic kratu-, Avestan xratus \\\"spiritual power\\\"'. Modern handbooks (Wiktionary/Cheung, following LIV *kret-) keep xratu- with Gk. kratos and Germanic *harduz (< o-grade *kort-us) but treat the crab/hard-shell words (*kar-kr-o-) as a separate family. So the node is right that xratu belongs with Gk. kratos and Engl. hard, and wrong only in that the reference it cites (POK:531) explicitly denies it.\",\n  derivation_fa=\"«خرد» در اوستایی xratu- «نیروی اندیشه، خردِ مینوی» (یسنا ۲۵٫۶، یشت ۱۰٫۱۰۷) آمده و بارتولومه در فرهنگ ایرانی باستان ستون ۵۳۵ به بعد آن را ثبت کرده است. هم‌ریشهٔ سنسکریت آن krátu- است و صورت بازسازی‌شدهٔ هندواروپایی آغازین *krét-us از ریشهٔ *kret- «نیرومند» است. والده-پوکورنی (جلد یکم ص ۳۵۵) این واژه را هنوز زیر ریشهٔ qar- «سخت» می‌آورد، اما پوکورنی در چاپ ۱۹۵۹ در همان صفحهٔ ۵۳۱ که نورایی به آن ارجاع می‌دهد صریحاً می‌گوید krátu- سنسکریت و xratu- اوستایی «از این ریشه دور می‌مانند». پس پیوند خرد با krátos یونانی و hard انگلیسی درست است، ولی نه از راه معنای «سختی»؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[W+\"%D8%AE%D8%B1%D8%AF\", W+\"Reconstruction:Proto-Germanic/harduz\"],\n  ref_check=[\n    {\"ref\":\"POK:531\",\"status\":\"contradicts\",\"note\":\"POK_full.txt (root kar-3, redupl. karkar-, Pages 530-531): after listing Gk. kratos/kartos/kratys it says 'remains far off Old Indie kratu-, Avestan xratus \\\"spiritual power\\\"' — i.e. Pokorny at the very page cited excludes xratu- from this root.\"},\n    {\"ref\":\"SYN:1201\",\"status\":\"not_found\",\"note\":\"Buck p.1201 in SYN.txt is section 16.53 'BRAVE' (Av. aurva-, dars(i)-); grep -n 'xratu' SYN.txt returns nothing at all, so Buck nowhere cites Av. xratu-. The 'mental strength' sections of Buck (17.11 ff.) are ~pp.1198-1210 but give Av. xratu- no entry.\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"AiW col. ~535 ff. (BRT.txt lines 7499, 10617-10625: 'ā-sna- Adj. \\\"angeboren, natürlich\\\", von xratav- m. \\\"Weisheit\\\"'; 'xratu-mant- Adj. \\\"einsichts-, weisheitsvoll\\\"')\",\"stance\":\"supports\",\"note\":\"Bartholomae has Av. xratu- 'Weisheit, Einsicht' exactly with Nourai's gloss 'mental strength'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. I 354-355 (WLD_Bd1_pages.txt leaves 362-363, s.v. 'qar-, redupl. qarqar- \\\"hart\\\"')\",\"stance\":\"supports\",\"note\":\"'Auf Grund einer idg. Erw. qre-t-: äol. krétos, att. krátos ... hom. kratýs \\\"stark\\\"' followed on p.355 by '\\\"Verstand\\\" (Pedersen KZ. 39, 368 ...)' — the older Walde-Pokorny did file the 'Verstand' word here, which is where Nourai's arrow comes from.\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. kar-1 'Hard'\",\"stance\":\"partial\",\"note\":\"'2. Extended zero-grade form *krt-es- in Greek kratos, strength, might, power: -cracy' — Watkins keeps kratos under kar-1 but says nothing about Avestan xratu-.\"}])\n\nN(id=2, lang=\"Pahlavi\", words=\"xrat\",\n  verdict=\"confirmed\",\n  derivation=\"Middle Persian xrad (Book Pahlavi hlt', Manichaean xrd) 'wisdom, reason' continues Old Iranian xratu- directly: the u-stem is remade as a consonant stem and final -u is lost, Av. xratu- > MP xrat/xrad, with the usual Middle Persian devoicing/voicing alternation in final position (xrat in absolute, xrad before vowels). Nyberg's Manual glossary shows the word all through the Dēnkard/Mēnōy-ī Xrad material ('mēnōy-ē xrat, the Heavenly Wisdom (personified)'), and the compound āsn-xrad 'innate wisdom' is a direct calque of Av. āsna- xratu-.\",\n  derivation_fa=\"فارسی میانه (پهلوی) xrat/xrad، به خط پهلوی کتابی hlt' و در پهلوی مانوی xrd، دنبالهٔ مستقیم xratu- ایرانی باستان است؛ ستاکِ -u به ستاک صامتی بدل شده و -u پایانی افتاده است. مکنزی در فرهنگ کوتاه پهلوی می‌آورد: «xrad [hlt' | M xrd, N xirad] wisdom, reason». ترکیب āsn-xrad «خردِ غریزی» نیز گرته‌برداری مستقیم از āsna- xratu- اوستایی است. ادعای نورایی درست است.\",\n  sources=[W+\"%D8%AE%D8%B1%D8%AF\"],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference of its own in the book.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie p.94 s.v. xrad (PHD.txt line 661; PHD_mackenzie.txt line 5567)\",\"stance\":\"supports\",\"note\":\"'xrad [hlt' | M xrd, N xirad] wisdom, reason. ~ig, ~omand [N -mand] wise' — MP xrad, New Persian xirad, exactly the arrow drawn.\"},\n    {\"src\":\"NYB\",\"where\":\"Nyberg, Manual II glossary s.vv. āsn, mēnōy (NYB_vol2_glossary.txt lines 693, 2535)\",\"stance\":\"supports\",\"note\":\"'āsn [ʼsnʼ] innate, inherent, primordial: ~ xrat (q.v.)'; 'mēnōy-ē xrat the Heavenly Wisdom (personified)' — Nyberg reads the word xrat and derives āsn from Av. āsna-.\"}])\n\nN(id=3, lang=\"Persian\", words=\"xerad «خرد»\",\n  verdict=\"confirmed\",\n  derivation=\"New Persian خرد xerad/xirad 'intelligence, wisdom' is the regular reflex of MP xrad: the Middle Persian initial cluster xr- is broken by an anaptyctic vowel (xrad > xirad/xerad), the same development as MP frāz > NP farāz. The word is continuous from the Šāhnāme ('تُوانا بُوَد هر که دانا بُوَد') onward, and it was also borrowed early into Armenian as xrat 'counsel, admonition' — an Iranian loan noted by Hübschmann (Persische Studien no. 476, 'Lies arm. xrat (für xart)'), which independently fixes the Middle Iranian form.\",\n  derivation_fa=\"«خِرَد» فارسی نو بازماندهٔ منظمِ xrad فارسی میانه است؛ خوشهٔ آغازینِ xr- در فارسی نو با واکهٔ میانجی شکسته شده (xrad > xirad/xerad)، درست مانند frāz > فراز. واژه از شاهنامه تا امروز پیوسته به‌کار رفته است. وام‌واژهٔ ارمنی xrat «اندرز» نیز — که هوبشمان در «مطالعات فارسی» شمارهٔ ۴۷۶ به آن اشاره می‌کند — صورت ایرانی میانه را مستقل تأیید می‌کند. ادعای نورایی درست است.\",\n  sources=[W+\"%D8%AE%D8%B1%D8%AF\"],\n  ref_check=[{\"ref\":\"BQT:729\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 186 (identified as printed p.729 by its own footers 'بقیه از صفحهٔ ۷۲۸ / بقیه در صفحهٔ ۷۳۰'): the entry خرد reads '... و بکسر اول وفتح ثانی بمعنی عقل باشد' — Borhān-e Qāṭeʿ glosses خِرَد as عقل 'intelligence', Nourai's gloss exactly. (Moʿin's footnote on that page is on خرداد, not on خرد.)\"}],\n  consulted=[\n    {\"src\":\"HUB\",\"where\":\"Persische Studien no. 476 (HUB.txt line 1876)\",\"stance\":\"supports\",\"note\":\"'Lies arm. xrat (für xart)' — Hübschmann's list of Iranian loanwords in Armenian has xrat from Middle Persian xrat.\"},\n    {\"src\":\"PHD\",\"where\":\"MacKenzie s.v. xrad\",\"stance\":\"supports\",\"note\":\"'[hlt' | M xrd, N xirad]' — MacKenzie himself gives the New Persian outcome xirad.\"}])\n\nN(id=4, lang=\"Sanskrit\", words=\"xara; karkarah; karkatah\",\n  verdict=\"confirmed\",\n  derivation=\"All three are real Sanskrit words and all three sit in the sources Nourai cites. khára- (Nourai writes x- for kh- throughout) 'hard, rough, sharp, pungent' is the adjective; karkara- 'hard, rough' equals Gk. kárkaros 'rough' (Hesych.); karkaṭa- m. 'crab; the zodiac sign Cancer' (also karka- m. 'crab'). Walde-Pokorny I 354 sets up 'qar-, redupl. qarqar- \\\"hart\\\"' with precisely 'Ai. karkara- \\\"rauh, hart\\\" = gr. karkaros ... ai. karkaṭa- m. \\\"Krebs\\\"', and treats khára- separately on p.355 as 'qhar- \\\"scharf, spitz\\\"' — which is why Nourai's root box carries the two names 'Karkar' and 'Qhar' side by side.\",\n  derivation_fa=\"هر سه واژه سنسکریتِ اصیل‌اند (نورایی به‌جای kh پیوسته x می‌نویسد): khára- «سخت، زبر، تند»، karkara- «زبر، سخت» (برابر با kárkaros یونانی) و karkaṭa- «خرچنگ؛ برج سرطان». والده-پوکورنی در جلد یکم ص ۳۵۴ ریشهٔ qar- و صورت مضاعفِ qarqar- «سخت» را با همین شواهد می‌آورد و khára- را در ص ۳۵۵ زیر qhar- «تیز، نوک‌تیز» جدا می‌کند؛ همین دو نام «Karkar» و «Qhar» در جعبهٔ ریشهٔ نورایی دیده می‌شود. ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[\n    {\"ref\":\"POK:531\",\"status\":\"supports\",\"note\":\"POK_full.txt, root kar-3 (Pages 530-531): 'Old Indie karkara- \\\"rough, hard\\\" = gr. karkaroi ... Old Indie karkasa- \\\"rough, hard\\\" ... Old Indie karkata- m. \\\"Cancer, 4th sign of the zodiac\\\" ..., karka- m. \\\"crab\\\"'.\"},\n    {\"ref\":\"KLN:703\",\"status\":\"supports\",\"note\":\"Klein s.v. hard (KLN_1966.txt line 17197, leaf 379): 'Cp. I.-E. *quar-q-, whence OI. karkatah, \\\"crab\\\", karkarah, \\\"rough, hard\\\", Gk. karkinos, \\\"crab\\\", L. cancer (dissimilated fr. *carcro-)'. (In this 1966 two-volume scan the entry falls at ~p.735; Nourai's 703 is presumably the one-volume reprint's pagination.)\"}],\n  consulted=[\n    {\"src\":\"WLD\",\"where\":\"Bd. I 354 and 355 (leaves 362-363)\",\"stance\":\"supports\",\"note\":\"p.354 '3. qar-, redupl. qarqar- u. dgl. \\\"hart\\\". Ai. karkara- \\\"rauh, hart\\\" = gr. karkaroi ... ai. karkata- m. \\\"Krebs\\\"'; p.355 'qhar- \\\"scharf, spitz\\\". Ai. khara- \\\"hart, rauh, scharf\\\"'.\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. kar-1\",\"stance\":\"supports\",\"note\":\"'II. Basic form *kar- in derivatives referring to things with hard shells ... 3. Reduplicated form *kar-kr-o dissimilated to Latin cancer, crab ... 4. Suffixed form *kar-k-ino- in Greek karkinos'.\"}])\n\nN(id=5, lang=\"Pahlavi\", words=\"xâr; kar-cang\",\n  verdict=\"plausible\",\n  derivation=\"Middle Persian xār 'thorn' is real (MacKenzie: 'xār [hʼl | M xʼr, N ~] thorn', with the derivatives xārōmand 'thorny' and xār-pušt 'porcupine'), and its equation with Skt. khára- 'hard, rough, sharp' is exactly Walde-Pokorny I 355, which lists 'np. xār, xārā \\\"Fels, Dorn\\\"' under qhar-. Nourai's gloss 'hard, rough' for the Pahlavi word is the etymological, not the attested, sense: in Pahlavi the word already means 'thorn'. The second word is a misspelling of the Pahlavi form: MacKenzie has karzang [klcng | M kyrzng] 'crab; astr. Cancer', Horn (no. 472) reads it karčang, and Nourai's hyphenated 'kar-cang' reflects Horn's spelling but suggests a compound that does not exist. Also, karzang does not descend from Skt. khára- 'hard' (Nourai's parent) but from the karkaṭa-/karkinos reduplicated family of node 4's third word.\",\n  derivation_fa=\"xār فارسی میانه به معنی «خار» واقعی است؛ مکنزی می‌آورد «xār [hʼl | M xʼr, N ~] thorn» با مشتقاتِ xārōmand «خاردار» و xār-pušt «خارپشت». برابرنهادن آن با khára- سنسکریت «سخت، زبر، تیز» همان چیزی است که والده-پوکورنی جلد یکم ص ۳۵۵ زیر qhar- می‌گوید: «np. xār, xārā \\\"Fels, Dorn\\\"». معنای «سخت، زبر» که نورایی برای صورت پهلوی می‌دهد معنای ریشه‌شناختی است نه معنای گواهی‌شده. واژهٔ دوم اما درست نوشته نشده: صورت پهلوی karzang است (مکنزی: «karzang [klcng | M kyrzng, (N xarčang)] crab»)، و هرن آن را karčang می‌خواند؛ نگارش «kar-cang» ترکیبی می‌نماید که وجود ندارد. افزون بر این، karzang از khára- «سخت» نمی‌آید، بلکه از خانوادهٔ مضاعفِ karkaṭa-/karkinos است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[],\n  ref_check=[\n    {\"ref\":\"BQT:697\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 154/155 (printed 697-698): the headword 'خار = بروزن مار، معروف است' with the sub-entries خاربست، خارپشت، خارخسک — the Borhān entry for خار that Nourai is pointing at.\"},\n    {\"ref\":\"WLD:355\",\"status\":\"supports\",\"note\":\"Walde-Pokorny Bd. I 355 (leaf 363): 'qhar- \\\"scharf, spitz\\\". Ai. khara- \\\"hart, rauh, scharf\\\", np. xar, xāra \\\"Fels, Dorn\\\"' — precisely the Sanskrit-to-Persian arrow Nourai draws.\"},\n    {\"ref\":\"SYN:173\",\"status\":\"partial\",\"note\":\"Buck p.172-173 (SYN.txt leaf 207) is section 3.46 'ASS, DONKEY' with 'Av. xara-, kaθwa-'; it is relevant to the donkey branch (node 8), not to xār 'thorn' or to the crab.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie pp.94, 50 (PHD.txt lines 661, 426)\",\"stance\":\"partial\",\"note\":\"'xār [hʼl | M xʼr, N ~] thorn' supports the first word; but for the crab MacKenzie writes 'karzang [klcng | M kyrzng, (N xarčang)] crab; astr. Cancer', not kar-cang.\"},\n    {\"src\":\"HRN\",\"where\":\"Horn no. 461 (HRN.txt line 4213, printed p.102) and no. 472 (line 4310)\",\"stance\":\"supports\",\"note\":\"no.461 'xār, xārā \\\"Fels; Dorn\\\" ... skr. khara- \\\"hart, rauh; scharf\\\"; phlv. xār, xārpust \\\"Igel\\\" (Bund.); arm. kʿar \\\"Stein\\\"'; no.472 'xarčang \\\"Krebs\\\" ... phlv. karčang \\\"Krebs im Tierkreise\\\" (Bund.)'.\"}])\n\nN(id=6, lang=\"Persian\", words=\"xâr 2 «خار»; xârâ «خارا»; xarčang «خرچنگ»\",\n  verdict=\"confirmed\",\n  derivation=\"خار xār 'thorn' and خارا xārā 'granite, hard rock' continue MP xār directly (Horn no. 461: 'xār, xārā \\\"Fels; Dorn\\\" ... skr. khara- \\\"hart, rauh; scharf\\\"; phlv. xār'); Armenian kʿar 'stone' and xarak 'hard rock' are the Iranian loans that confirm the Middle Iranian shape (Hübschmann). خرچنگ xarčang 'crab' is the regular outcome of MP karčang/karzang, but with a secondary k- > x- that is folk-etymological: Hübschmann, Persische Studien no. 475, states it outright — 'Np. xaršang \\\"Krebs\\\" aus phlv. karčang mit volksetymologischer Anlehnung an die Composita mit xar \\\"Esel\\\" ..., so dass nun das Wort aus xar \\\"Esel\\\" und čang \\\"Kralle\\\" zusammengesetzt erscheint'. That is, the modern speaker's 'donkey-claw' reading is false, and the chart is right to put xarčang under the 'hard' branch rather than under the donkey branch.\",\n  derivation_fa=\"«خار» و «خارا» (سنگ سخت، گرانیت) دنبالهٔ مستقیم xār فارسی میانه‌اند؛ هرن در شمارهٔ ۴۶۱ می‌نویسد: «xār, xārā \\\"Fels; Dorn\\\" ... skr. khara- ...؛ phlv. xār؛ arm. kʿar \\\"Stein\\\"». وام‌واژه‌های ارمنی kʿar «سنگ» و xarak «صخرهٔ سخت» صورت ایرانی میانه را استوار می‌کنند. «خرچنگ» بازماندهٔ منظمِ karčang/karzang پهلوی است، اما x- آغازین آن ثانوی و زادهٔ ریشه‌شناسی عامیانه است؛ هوبشمان در «مطالعات فارسی» شمارهٔ ۴۷۵ صریح می‌گوید: «xaršang فارسی نو از karčang پهلوی، با تکیهٔ ریشه‌شناسی عامیانه بر ترکیب‌های دارای xar \\\"خر\\\"، چنان‌که اکنون واژه مرکب از xar \\\"خر\\\" و čang \\\"چنگ\\\" می‌نماید». پس جای‌دادنِ خرچنگ در شاخهٔ «سختی» — نه شاخهٔ «خر» — درست است. ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[\n    {\"ref\":\"BQT\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaves 154-156 (printed 697-699) carry خار، خاربست، خارپشت، خارخسک and (leaf 156 footnote) Moʿin's note 'پهلوی: خارپوشت ... بندهش' — i.e. Borhān+Moʿin give the Pahlavi antecedent of the خار family.\"},\n    {\"ref\":\"HRN\",\"status\":\"supports\",\"note\":\"Horn, Grundriss no. 461 (p.102) for xār/xārā and no. 472 (p.105) for xarčang: 'skr. vergl. karkaṭa- \\\"Krebs, Krebs im Tierkreise\\\"; phlv. karčang \\\"Krebs im Tierkreise\\\" (Bund.); gr. karkinos \\\"Krebs\\\" ...; lat. cancer wird ebenfalls dazu gehören'.\"}],\n  consulted=[\n    {\"src\":\"HUB\",\"where\":\"Persische Studien nos. 473-475 (HUB.txt lines 1835-1876)\",\"stance\":\"supports\",\"note\":\"'afgh. LW. xar \\\"Dorn\\\" = arm. xar \\\"Dorn\\\" (Galen); np. xʷāra, xārā \\\"harte Stein, Fels\\\" = arm. xarak \\\"harte ...\\\"'; and no.475 on xarčang < phlv. karčang 'mit volksetymologischer Anlehnung'.\"},\n    {\"src\":\"PHD\",\"where\":\"MacKenzie s.vv. xār, karzang\",\"stance\":\"supports\",\"note\":\"'xār ... thorn'; 'karzang ... (N xarčang) crab; astr. Cancer' — MacKenzie explicitly names New Persian xarčang as the outcome.\"}])\n\nN(id=7, lang=\"Avestan\", words=\"xara\",\n  verdict=\"plausible\",\n  derivation=\"Avestan xara- m. 'donkey' (and f. 'she-ass') is securely attested — Bartholomae, AiW col. 532: 'xara- m.; xara- f. \\\"Esel\\\"; \\\"Eselstute\\\"', including the mythical three-legged ass standing in Vourukaša (Y. 42.4) — so the word and the language label are right. Nourai's gloss 'a harsh voiced animal' is not a lexical meaning but the etymological story: the derivation from 'hard, rough' is Uhlenbeck's, quoted approvingly in Walde-Pokorny I 355 ('ai. khara- m., av. xaro \\\"Esel\\\", Substantivierung von khara- \\\"hart\\\"'). Modern Indo-Iranian work is more sceptical: Wiktionary (after EWAia) reconstructs Proto-Indo-Iranian *kʰáras 'donkey' as a lexical item of its own, with a possible BMAC-substrate source, and does not connect it to the 'hard' adjective. The node's reference (SOD:166) is a Sogdian dictionary, an odd citation for an Avestan form, though Gharib does gloss Sogdian γr- 'donkey' with 'Av. xara-'.\",\n  derivation_fa=\"xara- اوستایی «خر» (و مؤنث «ماده‌خر») گواهی استواری دارد؛ بارتولومه در ستون ۵۳۲ می‌آورد: «xara- m.; xara- f. \\\"Esel\\\"، \\\"Eselstute\\\"»، از جمله خرِ اسطوره‌ای سه‌پایِ ایستاده در دریای فراخ‌کرت (یسنا ۴۲٫۴). پس واژه و برچسب زبانی درست است. اما معنای «جانورِ درشت‌آواز» که نورایی می‌دهد معنای واژگانی نیست، بلکه روایتِ ریشه‌شناختی اوست: این گرفتنِ «خر» از صفتِ «سخت/زبر» از اولنبک است که والده-پوکورنی جلد یکم ص ۳۵۵ آن را نقل می‌کند («khara- سنسکریت و xara- اوستایی، اسم‌شده از khara- \\\"سخت\\\"»). ریشه‌شناسی امروزی محتاط‌تر است: ویکی‌واژه بر پایهٔ مایرهوفر *kʰáras هندوایرانی آغازین را واژه‌ای مستقل و احتمالاً وام از زیرلایهٔ بلخ-مرو (BMAC) می‌داند. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[W+\"%D8%AE%D8%B1\"],\n  ref_check=[{\"ref\":\"SOD:166\",\"status\":\"partial\",\"note\":\"SOD_pages.txt leaf 231 (printed ~165) has entry '4169 γr- ... donkey' and the phonology table (SOD.txt line 6001) '/xar/ γr- donkey — Av. xara-'; Gharib does cite the Avestan form, but a Sogdian dictionary is not the natural authority for an Avestan headword.\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"AiW col. 532 (BRT.txt line 10546)\",\"stance\":\"supports\",\"note\":\"'j. xara- m.; xara- f. \\\"Esel\\\"; \\\"Eselstute\\\" ... a) m. ein mythischer Esel, der im Weltozean steht: Y. 42.4'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. I 355 (leaf 363)\",\"stance\":\"supports\",\"note\":\"'Uhlenbeck Ai. Wb. 74 (ai. khara- m., av. xaro \\\"Esel\\\", Substantivierung von khara- \\\"hart\\\")' — the exact claim of Nourai's arrow, though presented by WP as one scholar's view.\"},\n    {\"src\":\"SYN\",\"where\":\"Buck 3.46 'ASS, DONKEY', p.172-173 (SYN.txt leaf 207)\",\"stance\":\"partial\",\"note\":\"Buck lists 'Av. xara-, kaθwa-' among the words for donkey but offers no etymology for the Iranian word; he notes the European words are loans 'fr. some Asiatic source'.\"}])\n\nN(id=8, lang=\"Pahlavi\", words=\"xar; xar-bâra; xar-buz\",\n  verdict=\"confirmed\",\n  derivation=\"MP xar 'donkey' (Book Pahlavi with the Aramaic ideogram HMRA, from Aramaic ḥmr', beside the phonetic spelling hl) is the regular reflex of Av./Old Iranian xara-: intervocalic *-a- stem loss gives a bare xar. Nyberg's glossary states the descent directly: 'xar [HMR] donkey ... — Av. (532) xara-; NP xar'. xar-bār 'a donkey-load' is xar + bār 'load' (< OIr. *bāra-, root bar- 'carry'), Nourai's cross-reference to Bher 1 being correct. xar-buz is attested twice over: MacKenzie glosses MP xar-buz [hlbwc] as 'oryx' (literally 'donkey-goat', as Hübschmann no. 213 explains, 'phlv. xarbuz = Esel-Ziege ... eine Ziegenart'), while Horn no. 471 has 'phlv. xarbōjhīna, kharbuzak' behind NP xarbuza 'melon', literally 'donkey-cucumber'. So the element xar- 'donkey, hence coarse/big' is right, and the melon sense is the New Persian development.\",\n  derivation_fa=\"xar فارسی میانه «خر» (در پهلوی کتابی با هزوارش آرامی HMRA و نگارش آوایی hl) بازماندهٔ منظمِ xara- ایرانی باستان است. نیبرگ در واژه‌نامهٔ خود صریح می‌گوید: «xar [HMR] donkey ... — Av. (532) xara-؛ NP xar». xar-bār «بارِ خر» از xar + bār «بار» (از *bāra- ایرانی باستان، ریشهٔ bar- «بردن») ساخته شده و ارجاع نورایی به Bher ۱ درست است. xar-buz دو گواه دارد: مکنزی آن را «oryx» (تحت‌اللفظ «خر-بز») می‌داند و هوبشمان در شمارهٔ ۲۱۳ آن را «بزی از گونه‌ای» می‌خواند؛ هرن در شمارهٔ ۴۷۱ صورت پهلویِ xarbōjhīna/kharbuzak را پشتِ «خربزه» فارسی نو می‌گذارد، تحت‌اللفظ «خیارِ خری». ادعای نورایی درست است.\",\n  sources=[W+\"%D8%AE%D8%B1\"],\n  ref_check=[\n    {\"ref\":\"WLD:355\",\"status\":\"supports\",\"note\":\"Walde-Pokorny Bd. I 355: 'Uhlenbeck Ai. Wb. 74 (ai. khara- m., av. xaro \\\"Esel\\\", Substantivierung von khara- \\\"hart\\\")' — the page cited does connect the donkey word with khara- 'hard'.\"},\n    {\"ref\":\"SYN:173\",\"status\":\"supports\",\"note\":\"Buck, Dict. of Selected Synonyms, section 3.46 'ASS, DONKEY' (printed pp.172-173, SYN.txt leaf 207): the comparative table lists 'Av. xara-, kaθwa-'.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie p.93 (PHD.txt line 661)\",\"stance\":\"supports\",\"note\":\"'xar [HMRA < A ḥmrʼ; hl | N ~] donkey, ass'; 'xar-buz [hlbwc | M xrbwz] oryx'; 'xar-gōš [hlgws | N ~] rabbit, hare'.\"},\n    {\"src\":\"NYB\",\"where\":\"Nyberg, Manual II glossary s.v. xar (NYB_vol2_glossary.txt line 4274)\",\"stance\":\"supports\",\"note\":\"'xar [HMR] donkey 24¹⁵. 30³. — Av. (532) xara-; NP xar' — the whole Av. > MP > NP chain in one line, with Bartholomae's column number.\"},\n    {\"src\":\"HRN\",\"where\":\"Horn no. 470-471 (HRN.txt lines 4298-4310, printed pp.104-105)\",\"stance\":\"supports\",\"note\":\"'470. xar \\\"Esel\\\", xargōš \\\"Hase\\\" ... aw. xara- \\\"Esel\\\": phlv. xar: skr. khara- \\\"Esel\\\"'; '471. xarbuze, xarbuza \\\"Melone\\\" (wörtl. \\\"Eselsgurke\\\"). phlv. xarbōjhīna, kharbuzak'.\"}])\n\nN(id=9, lang=\"Persian\", words=\"xar «خر»\",\n  verdict=\"confirmed\",\n  derivation=\"New Persian خر xar 'donkey' inherits MP xar unchanged; the transferred sense 'coarse, stupid; huge' is the source of the whole productive series the chart lists in the margin: خروار xarvār 'a donkey-load' (a weight of ca. 300 kg, therefore 'huge'), خربزه xarboze 'melon' (Horn no. 471, lit. 'donkey-cucumber'), خرگوش xargūš 'hare' (lit. 'donkey-ear', MP xar-gōš), خرمگس xarmagas 'horsefly' (lit. 'donkey-fly'), خرمهره xarmohre 'a large coarse bead'. The Saʿdī line quoted on the page ('خر عیسی گرش به مکه برند / چون بیاید هنوز خر باشد') is genuine and turns on exactly this metaphorical sense.\",\n  derivation_fa=\"«خر» فارسی نو بی‌هیچ دگرگونی از xar فارسی میانه به ارث رسیده است؛ معنای مجازیِ «درشت، کودن، بزرگ» سرچشمهٔ همان زنجیرهٔ زایایی است که در حاشیهٔ نمودار آمده: «خروار» (بارِ یک خر، وزنی نزدیک به ۳۰۰ کیلوگرم و از این‌رو «بسیار بزرگ»)، «خربزه» (به گفتهٔ هرن، شمارهٔ ۴۷۱، تحت‌اللفظ «خیارِ خری»)، «خرگوش» (xar-gōš پهلوی، «گوش‌درازِ خری»)، «خرمگس» و «خرمهره». بیت سعدی که در صفحه آمده («خر عیسی گرش به مکه برند / چون بیاید هنوز خر باشد») اصیل است و بر همین معنای مجازی می‌چرخد. ادعای نورایی درست است.\",\n  sources=[W+\"%D8%AE%D8%B1\"],\n  ref_check=[\n    {\"ref\":\"BQT\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaves 185-187 (printed 728-730) carry the خر- compounds (خرچکول، خرچنگ، خرجه ...) immediately before خرداد; the Borhān has خر and its compound series as Nourai says.\"},\n    {\"ref\":\"HRN\",\"status\":\"supports\",\"note\":\"Horn nos. 470-471 (printed pp.104-105): 'xar \\\"Esel\\\", xargōš \\\"Hase\\\" (= \\\"Eselsohr\\\") ... aw. xara- \\\"Esel\\\": phlv. xar: skr. khara- \\\"Esel\\\"' and 'xarbuze ... \\\"Melone\\\" (wörtl. \\\"Eselsgurke\\\")' — covers خر، خرگوش، خربزه of the margin list.\"},\n    {\"ref\":\"FVF:190\",\"status\":\"not_checked\",\"note\":\"FVF = Emām Šuštarī, Farhang-e vāžehā-ye fārsi dar zabān-e ʿarabi (Tehran 1347); refs_online.json records no local copy and no fetchable scan (noorlib/ketabnak need a login), so p.190 could not be read.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie s.vv. xar, xar-gōš\",\"stance\":\"supports\",\"note\":\"'xar [HMRA ...| N ~] donkey, ass'; 'xar-gōš [hlgws | N ~] rabbit, hare' — the New Persian equivalences are MacKenzie's own.\"},\n    {\"src\":\"HUB\",\"where\":\"Persische Studien no. 213-215 (HUB.txt lines 933-950) and no. 474 (line 1870)\",\"stance\":\"supports\",\"note\":\"'Das in der Anmerkung erwähnte phl. xarbuz (Bdh. 57,8 ...) = \\\"Esel-ziege\\\"'; 'Dazu arm. xarbzak \\\"Melone\\\"' — Armenian xarbzak is the loan that fixes the Middle Iranian melon word.\"}])\n\nN(id=10, lang=\"Sogdian\", words=\"xr; xr-tr`k, xara-tara\",\n  verdict=\"confirmed\",\n  derivation=\"Both Sogdian forms are in Gharib's dictionary exactly as drawn. Buddhist/Manichaean Sogdian γr- /xar/ 'donkey' (entry 4169) continues Old Iranian xara- like Middle Persian xar; γrtrʼk /xartarē/ 'mule' (entry 4270) is a comparative formation, *xara-tara- 'the more donkey-like one', with the Indo-Iranian comparative suffix *-tara- (Av. -tara-, Skt. -tara-, Gk. -teros) and the Sogdian ending -ē of the animate declension. Gharib herself reconstructs '<*xara-tara-' and cross-refers to Turkic. The semantics ('more of a donkey than a horse') is transparent for the hybrid animal.\",\n  derivation_fa=\"هر دو صورت سغدی درست همان‌گونه که در نمودار آمده در فرهنگ سغدی بدرالزمان قریب هست: γr- /xar/ «خر» (مدخل ۴۱۶۹) که مانند xar فارسی میانه دنبالهٔ xara- ایرانی باستان است، و γrtrʼk /xartarē/ «قاطر» (مدخل ۴۲۷۰) که ساختِ تفضیلیِ *xara-tara- «خرمانندتر» است، با پسوند تفضیلی هندوایرانی -tara- (اوستایی -tara-، سنسکریت -tara-، یونانی -teros) و پایانهٔ -ē سغدی. خودِ قریب صورت «<*xara-tara-» را بازسازی می‌کند. معنا برای جانورِ دورگه روشن است: «بیشتر خر تا اسب». ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"SOD:166\",\"status\":\"supports\",\"note\":\"SOD_pages.txt leaf 231 (printed ~165) entry '4169 γr-3 B, S ... donkey' and leaf 235 (printed ~169) entry '4270 γrtrʼk B / xartare © <*xara-tara-, Turk. ... mule / TSP 2.771n p179; Hen. Texts 723'. The index leaf 551 confirms 'donkey 4169, 10622'. Both are within a few pages of Nourai's 166.\"}],\n  consulted=[\n    {\"src\":\"SOD\",\"where\":\"Gharib entries 4169 and 4270\",\"stance\":\"supports\",\"note\":\"as quoted; Gharib's own reconstruction '<*xara-tara-' is the whole of Nourai's claim for the Sogdian node.\"},\n    {\"src\":\"BRT\",\"where\":\"AiW col. 532\",\"stance\":\"supports\",\"note\":\"'xara- m. \\\"Esel\\\"' supplies the Old Iranian base of the Sogdian comparative.\"}])\n\nN(id=11, lang=\"Persian\", words=\"qâter «قاطر»\",\n  verdict=\"disputed\",\n  derivation=\"The Sogdian word γrtrʼk xartarē 'mule' is real, but no independent authority derives Persian قاطر qāter from it, and the reference Nourai cites for this arrow says the opposite. Moʿin's own dictionary tags قاطر '[تر.]' — Turkic — and glosses it 'استر، حیوانی که از جفت‌گیری خر نر و اسب ماده به وجود آید'. The standard view is a loan from Turkic katır (Az. qatır, Turkish katır, Kazakh qašır, Uzbek xachir, Uyghur xëchir < Proto-Turkic), which entered Arabic and Persian as قاطر and spread thence into the Balkans (Lokotsch no. 1131: 'Tk. katyr \\\"Maultier\\\"; hieraus rum. catîr, bulg. katır, serb. katura, russ. (dial.) katjer'). Dehḵodā notes only that the word was originally written with ت and later respelt with ط, i.e. a foreign word accommodated to Arabic orthography. Gharib's laconic 'Turk.' beside xartarē may even mean the Turkic word is her comparandum rather than her derivative; in any case the Sogdian-to-New-Persian route Nourai draws is not attested anywhere.\",\n  derivation_fa=\"واژهٔ سغدیِ γrtrʼk /xartarē/ «قاطر» واقعی است، اما هیچ مرجع مستقلی «قاطر» فارسی را از آن نمی‌گیرد، و مأخذی که خودِ نورایی برای این پیکان آورده خلاف آن را می‌گوید: معین در ذیل «قاطر» انگ «[تر.]» (ترکی) می‌گذارد و آن را «استر، حیوانی که از جفت‌گیری خر نر و اسب مادّه به وجود آید» معنی می‌کند. دیدگاه پذیرفته این است که واژه وام‌واژه‌ای است از ترکی katır (آذری qatır، ترکی استانبولی katır، قزاقی qašır، ازبکی xachir) که به عربی و فارسی راه یافته و از آنجا به زبان‌های بالکان رفته است؛ لوکوچ در شمارهٔ ۱۱۳۱ می‌نویسد: «ترکی katyr \\\"استر\\\"؛ از آن رومانیایی catîr، بلغاری katır، صربی katura، روسی (گویشی) katjer». دهخدا نیز تنها یادآور می‌شود که این لفظ در اصل با «ت» بوده و متأخران به «ط» بدل کرده‌اند — نشانهٔ واژه‌ای بیگانه که به املای عربی درآمده است. پژوهش امروزی مسیر سغدی → فارسی نو را رد می‌کند.\",\n  sources=[W+\"%D9%82%D8%A7%D8%B7%D8%B1\",\"https://abadis.ir/fatofa/%D9%82%D8%A7%D8%B7%D8%B1/\"],\n  ref_check=[{\"ref\":\"MON:2615\",\"status\":\"contradicts\",\"note\":\"Moʿin's entry for قاطر (read via abadis.ir, section فرهنگ معین): '(طِ) [تر.] (اِ.) استر، حیوانی که از جفت گیری خر نر و اسب ماده بوجود آید' — the origin tag [تر.] marks it Turkic, not Sogdian.\"}],\n  consulted=[\n    {\"src\":\"LKT\",\"where\":\"Lokotsch no. 1131 (LKT.txt line 2664)\",\"stance\":\"contradicts\",\"note\":\"'1131. Tk. katyr: \\\"Maultier\\\"; hieraus rum. catîr \\\"dass.\\\", catirǎ \\\"Mauleselin\\\"; bulg. katır, serb. katura, russ. (dial.) katjer \\\"Maultier\\\"' — Lokotsch files the word as Turkish, with no Iranian antecedent.\"},\n    {\"src\":\"SOD\",\"where\":\"Gharib entry 4270\",\"stance\":\"partial\",\"note\":\"'xartare © <*xara-tara-, Turk. =*γrtry / mule' — Gharib gives the Sogdian word and its Iranian make-up but does not claim Persian قاطر descends from it.\"},\n    {\"src\":\"TTS\",\"where\":\"Vámbéry (TTS_vambery1878_uoft_djvu.txt)\",\"stance\":\"silent\",\"note\":\"grep -i 'katir|qatyr|Maulesel' returns only 'katirik' at line 5406 under kata- 'trocknen'; Vámbéry has no entry for katır 'mule'.\"}])\n\nN(id=12, lang=\"Sanskrit\", words=\"kankarta, kankatih\",\n  verdict=\"plausible\",\n  derivation=\"The Sanskrit word is kaṅkaṭa- m./n. 'armour, coat of mail' (Nourai's 'kankatih' is the nominative kaṅkaṭaḥ); 'kankarta' is not an attested word but the reconstructed pre-form *kaṅkr̥ta-, which is exactly how Pokorny cites it: Latin cancer is dissimilated from *carcro-, 'perhaps already Indo-Germanic, compare Old Indic kaṅkata- m. \\\"armor, coat of mail, garment made of linked metal rings\\\" from *kaṅkr̥ta-'. So the node is well founded in the source, except that the second gloss 'fortified' has no lexical warrant (kaṅkaṭa- is a noun 'mail-coat', not an adjective), and the node's own reference, Mann IEC, does not support it: Mann's nearest headword, kankǝr- (p.508-509), is glossed 'hook, bend, curl' and cites only Latin cancer and Czech kučera.\",\n  derivation_fa=\"واژهٔ سنسکریت kaṅkaṭa- «زره، جوشن» است («kankatih» نورایی همان صورت فاعلی kaṅkaṭaḥ است)؛ اما «kankarta» واژه‌ای گواهی‌شده نیست، بلکه صورت بازسازی‌شدهٔ *kaṅkr̥ta- است — و پوکورنی نیز دقیقاً همین‌گونه می‌آورد: cancer لاتین از *carcro- با ناهمگونی پدید آمده، «شاید همان‌گونه در هندواروپایی، سنجیده شود با kaṅkata- سنسکریت \\\"زره، جوشن\\\" از *kaṅkr̥ta-». پس گره در مأخذ پایه دارد، جز آنکه معنای دوم «استوارشده/دژوار» پشتوانهٔ واژگانی ندارد (kaṅkaṭa- اسم است نه صفت)، و مأخذی که خودِ گره به آن ارجاع می‌دهد (مان، IEC) آن را تأیید نمی‌کند: نزدیک‌ترین مدخل مان، kankǝr- در ص ۵۰۸–۵۰۹، «قلاب، خم، پیچه» معنی شده است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[],\n  ref_check=[\n    {\"ref\":\"POK:531\",\"status\":\"supports\",\"note\":\"POK_full.txt root kar-3: 'Latin cancer, -crī (dissim. from *carcro-, perhaps already Indo Germanic, compare Old Indie kaṅkata- m. \\\"armor, coat of mail, garment made of linked metal rings\\\" from *kaṅkr̥ta-)'.\"},\n    {\"ref\":\"IEC:1632\",\"status\":\"not_found\",\"note\":\"IEC.txt leaf 831 = printed pp.1632-33, which is inside the uel- 'wish/will' article; Mann has no headword 'Kongar' anywhere (grep 'kongar|kankarta' finds nothing), and his kankǝr- at leaf 269 = pp.508-09 reads 'kankǝr- (kanker-) (?) \\\"hook, bend, curl\\\" Lat. cancer \\\"crab\\\"; Cz. kučera \\\"curl\\\"' — different meaning, no Sanskrit.\"}],\n  consulted=[\n    {\"src\":\"WLD\",\"where\":\"Bd. I 354 (leaf 362)\",\"stance\":\"supports\",\"note\":\"'lat. cancer, -cri ds. (diss. aus *carcro-, vielleicht schon idg., vgl. ai. kaṅkata- m. \\\"Panzer\\\" aus *kaṅkr̥ta-)' — Walde-Pokorny's wording, which Pokorny 1959 repeats.\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. kar-1\",\"stance\":\"silent\",\"note\":\"Watkins gives 'Reduplicated form *kar-kr-o dissimilated to Latin cancer' but does not mention the Sanskrit armour word.\"}])\n\nN(id=13, lang=\"Persian\", words=\"kongareh «کنگره ۱»\",\n  verdict=\"unverified\",\n  derivation=\"کنگره kongare 'merlon, battlement; the toothed cresting of a wall or tower' is a genuine and old Persian word (it is the standard term for the crenellations of Persepolis, and the Molavī line quoted on the page is authentic), but no source consulted derives it from Sanskrit kaṅkaṭa- 'armour'. Moʿin's dictionary gives کنگره ۱ 'شرفه، دندانه، دندانه‌های بالای دیوارها' with no origin tag at all (he tags only کنگره ۲ 'congress' as [فر.], from French congrès), and Persian etymological discussion (e.g. Kazzāzi) states plainly that the origin of the word is unclear; a link to کنگر 'thistle, cardoon' (from the spiky outline) is sometimes suggested but not demonstrated. Mann's IEC, the other reference cited, has no such entry. A semantic bridge from 'coat of mail' to 'crenellation' would in any case need argument, since the shared idea is 'row of overlapping plates' rather than 'fortification'.\",\n  derivation_fa=\"«کنگره» به معنی «شُرفه، دندانه‌های سرِ دیوار و برج» واژه‌ای اصیل و کهن فارسی است (اصطلاح متعارف برای دندانه‌های تخت‌جمشید؛ بیت مولوی نقل‌شده در صفحه نیز اصیل است)، اما هیچ‌یک از مأخذهای بررسی‌شده آن را از kaṅkaṭa- سنسکریت «زره» نمی‌گیرد. معین برای «کنگره ۱» هیچ انگ ریشه‌ای نمی‌گذارد («شرفه، دندانه، دندانه‌های بالای دیوارها») و تنها «کنگره ۲» را [فر.] (از congrès فرانسوی) می‌داند. در بحث‌های ریشه‌شناسی فارسی (از جمله نزد کزّازی) صریحاً آمده که «ریشه و خاستگاه این واژه روشن نیست»؛ پیوند احتمالی با «کنگر» (از شکل دندانه‌دار گیاه) پیشنهاد شده اما اثبات نشده است. مان نیز چنین مدخلی ندارد. بنابراین ادعای نورایی نه تأیید و نه رد شد؛ سندی برای آن نیافتم.\",\n  sources=[W+\"%DA%A9%D9%86%DA%AF%D8%B1%D9%87\",\"https://abadis.ir/fatofa/%DA%A9%D9%86%DA%AF%D8%B1%D9%87/\"],\n  ref_check=[\n    {\"ref\":\"IEC:1632\",\"status\":\"not_found\",\"note\":\"as for node 12: IEC printed pp.1632-33 (leaf 831) is the uel- article; Mann has no 'Kongar' headword and his kankǝr- (pp.508-09) means 'hook, bend, curl'.\"},\n    {\"ref\":\"MON:3102\",\"status\":\"partial\",\"note\":\"Moʿin's entry, read via abadis.ir: 'کنگره ۱ (کُ گِ رِ) (اِ.) شرفه، دندانه، دندانه‌های بالای دیوارها و بلندی‌های هرچیزی' — headword and gloss are exactly Nourai's, but Moʿin supplies no etymology; he tags only کنگره ۲ as [فر.].\"}],\n  consulted=[\n    {\"src\":\"MON\",\"where\":\"Farhang-e Moʿin s.v. کنگره (via abadis.ir)\",\"stance\":\"silent\",\"note\":\"no origin tag on کنگره ۱; '[فر.]' only on کنگره ۲ 'congress'.\"},\n    {\"src\":\"POK\",\"where\":\"POK_full.txt root kar-3 (pp.530-531)\",\"stance\":\"silent\",\"note\":\"Pokorny's kar- 'hard' article mentions Skt. kaṅkata- 'armour' but no Iranian or New Persian continuant of it.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann, leaf 269 = pp.508-509\",\"stance\":\"contradicts\",\"note\":\"'kankǝr- (kanker-) (?) \\\"hook, bend, curl\\\"' — Mann's only near-matching headword, glossed quite differently, with no Persian material.\"}])\n\nN(id=14, lang=\"Germanic\", words=\"harduz\",\n  verdict=\"confirmed\",\n  derivation=\"Proto-Germanic *harduz 'hard' (Gothic hardus, ON harðr, OE heard, OS hard, OHG hart/herti) is the standard reconstruction and is derived from PIE *kort-ús, an o-grade tu-stem, in every handbook consulted. Pokorny states it in so many words: 'proto Germanic *hardu- from Indo Germanic *kar-t-u-'; Klein: 'G. hart, Goth. hardus, \\\"hard\\\", fr. I.-E. base *qar-, \\\"hard\\\"'; Watkins: 'Suffixed o-grade form *kor-tu- in Germanic *harduz'. The only live disagreement is Kroonen's/Heidermanns' minority proposal to take it from *(s)ker- 'to cut' instead — noted on Wiktionary as the less established option — which does not affect the shape of the reconstruction.\",\n  derivation_fa=\"ژرمنی آغازین *harduz «سخت» (گوتی hardus، نورس کهن harðr، انگلیسی کهن heard، آلمانی علیای کهن hart/herti) بازسازی متعارف است و در همهٔ مأخذهای بررسی‌شده از *kort-ús هندواروپایی — ستاکِ tu- با درجهٔ آوایی o — گرفته می‌شود. پوکورنی می‌نویسد: «ژرمنی آغازین *hardu- از *kar-t-u- هندواروپایی»؛ کلاین: «آلمانی hart، گوتی hardus \\\"سخت\\\"، از پایهٔ هندواروپایی *qar- \\\"سخت\\\"»؛ واتکینز: «صورتِ پسوندداری با درجهٔ o، *kor-tu-، در ژرمنی *harduz». تنها اختلافِ زنده پیشنهاد اقلیتِ کرونن و هایدرمانس است که آن را از *(s)ker- «بریدن» می‌گیرند. ادعای نورایی درست است.\",\n  sources=[\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/harduz\"],\n  ref_check=[\n    {\"ref\":\"KLN:703\",\"status\":\"supports\",\"note\":\"Klein s.v. hard, adj. (KLN_1966.txt line 17197): 'ME. hard, fr. OE. heard, rel. to ... G. hart, Goth. hardus, \\\"hard\\\", fr. I.-E. base *qar-, \\\"hard\\\". Fr. I.-E. *qret-, *qr̥t-, a -t-enlargement of base *qar-, derive Gk. kratos, Ion. kartos, Aeol. kretos, \\\"strength\\\", Gk. kratys, \\\"strong\\\".'\"},\n    {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. kar-1 'Hard': 'I. Variant form ker-. 1. Suffixed o-grade form *kor-tu- in Germanic *harduz in: a. Old English heard, hard: HARD ...'\"}],\n  consulted=[\n    {\"src\":\"POK\",\"where\":\"POK_full.txt root kar-3, Pages 530-531\",\"stance\":\"supports\",\"note\":\"'With t-suffixes: Gothic hardus \\\"hard, stern\\\", Old Norse harðr ... proto Germanic *hardu- from Indo Germanic *kar-tʼu-'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. I 354 (leaf 362)\",\"stance\":\"supports\",\"note\":\"'Mit t-Suffixen: got. hardus \\\"hart, streng\\\", anord. harðr \\\"hart\\\", ags. heard ... urgerm. hardu- aus idg. *qar-tu-'.\"}])\n\nN(id=15, lang=\"Old French\", words=\"estandard\",\n  verdict=\"plausible\",\n  derivation=\"Old French estandart / Anglo-Norman estandard 'rallying flag' (mid-12th c.), whence Medieval Latin standardum and Middle English standard, is normally explained as a borrowing of Frankish *standhard 'stand firm', a compound of the verb 'to stand' with the adjective *hard — so only the SECOND element belongs to this root, which the chart's single arrow from Germanic harduz obscures (Nourai's own cross-reference '☞Stâ' acknowledges the first element). Watkins states it exactly so under kar-1: 'Frankish *hard, hard, perhaps the source of Old French estandard, rallying place: STANDARD', and Skeat s.v. Standard has 'O.H.G. standan, to stand; with suffix -art (= O.H.G. hart, a suffix, orig. the same as hart, adj., hard)'. The competing derivation, favoured by the OED, takes the Old French word from estendre 'to stretch out' (Latin extendere) with the -ard ending by folk etymology; Skeat already notes 'The O.F. estendard, Ital. stendardo are modified forms, as if from L. extendere'. Hence 'plausible' rather than 'confirmed'.\",\n  derivation_fa=\"فرانسوی کهن estandart / انگلیسی-نورمنِ estandard «درفشِ گردآمدن» (نیمهٔ سدهٔ دوازدهم میلادی) — که لاتینِ میانهٔ standardum و انگلیسی میانهٔ standard از آن است — معمولاً وام‌واژه‌ای از فرانکیِ *standhard «استوار ایستادن» دانسته می‌شود، ترکیبی از فعلِ «ایستادن» و صفتِ *hard؛ پس تنها جزء دوم به این ریشه می‌رسد و پیکانِ یگانهٔ نمودار از harduz این نکته را می‌پوشاند (هرچند ارجاعِ خودِ نورایی به «Stâ» به جزء نخست اشاره دارد). واتکینز زیر kar-1 می‌نویسد: «فرانکی *hard \\\"سخت\\\"، شاید سرچشمهٔ estandard فرانسوی کهن»، و اسکیت در ذیل Standard می‌آورد: «standan آلمانی علیای کهن \\\"ایستادن\\\"، با پسوندِ -art (= hart، در اصل همان صفتِ hard)». دیدگاه رقیب که فرهنگ آکسفورد می‌پسندد واژه را از estendre «کشیدن» (لاتین extendere) می‌گیرد. از این‌رو ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[\"https://www.etymonline.com/word/standard\"],\n  ref_check=[{\"ref\":\"AHD:1257\",\"status\":\"supports\",\"note\":\"Nourai's AHD:1257 is the main-dictionary page of the American Heritage New College Edition for STANDARD; the corresponding root article, Watkins 1985 s.v. kar-1, reads 'b. Frankish *hard, hard, perhaps the source of Old French estandard, rallying place: STANDARD' — the arrow as drawn, with Watkins's own 'perhaps'.\"}],\n  consulted=[\n    {\"src\":\"SKT\",\"where\":\"Skeat s.v. Standard (SKT.txt line 18358)\",\"stance\":\"supports\",\"note\":\"'O.F. estandart, a standard or ensign ... The flag was a large one, on a fixed (standing) pole. — O.H.G. standan, to stand; with suffix -art (= O.H.G. hart, a suffix, orig. the same as hart, adj., hard). ... The O.F. estendard, Ital. stendardo are modified forms, as if from L. extendere, to spread out.'\"},\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. hard\",\"stance\":\"silent\",\"note\":\"Klein's hard article lists the -ard names (Bernard, Everard, Gerard, Leonard, Reynard) but does not mention standard among them.\"}])\n\nN(id=16, lang=\"Persian\", words=\"estândârd «استاندارد»\",\n  verdict=\"confirmed\",\n  derivation=\"Persian استاندارد estāndārd is a twentieth-century European loan — from French standard / English standard, taken in with the metric and industrial vocabulary (the Iranian standards institute, مؤسسهٔ استاندارد و تحقیقات صنعتی ایران, was founded in 1339/1960). The Persian shape shows the regular prothetic e- that Persian gives to word-initial st- clusters (as in استکان, اسکناس, استخر), i.e. st- > es-t-. It has nothing to do with the inherited Iranian branch of this chart; it is a re-entry of the Germanic word by way of modern Europe.\",\n  derivation_fa=\"«استاندارد» وام‌واژه‌ای اروپایی از سدهٔ بیستم است، از standard فرانسوی/انگلیسی، که همراه با واژگان صنعتی و اندازه‌گیری به فارسی درآمد (مؤسسهٔ استاندارد و تحقیقات صنعتی ایران در ۱۳۳۹ بنیاد گرفت). صورت فارسی، واکهٔ آغازینِ افزودهٔ e- را نشان می‌دهد که فارسی همیشه پیش از خوشهٔ آغازینِ st- می‌آورد (مانند استکان، اسکناس، استخر). این واژه هیچ پیوندی با شاخهٔ موروثیِ ایرانیِ این نمودار ندارد و بازگشتِ واژه‌ای ژرمنی از راه اروپای امروزی است. ادعای نورایی درست است.\",\n  sources=[\"https://www.etymonline.com/word/standard\"],\n  ref_check=[{\"ref\":\"MON:239\",\"status\":\"not_checked\",\"note\":\"Moʿin's foreign-compounds volume (vol. 4) is not online with page numbers and the local MON OCR (MON_part1/2.txt, MON_2vol_Adena_*_djvu.txt) is too corrupt to grep Persian script — 'استاندارد' returns no hits in any of them. abadis/vajehyab carry the Moʿin lexicon volumes only.\"}],\n  consulted=[\n    {\"src\":\"MON\",\"where\":\"Farhang-e Moʿin (vol. 4, foreign words)\",\"stance\":\"silent\",\"note\":\"could not be read; see ref_check.\"},\n    {\"src\":\"SKT\",\"where\":\"Skeat s.v. Standard\",\"stance\":\"supports\",\"note\":\"establishes the Western word that Persian borrowed; the Persian form is transparently the French/English one.\"}])\n\nN(id=17, lang=\"English\", words=\"standard\",\n  verdict=\"confirmed\",\n  derivation=\"Middle English standard (mid-12th c. in Anglo-Latin/Anglo-French contexts, of the flag at the Battle of the Standard, 1138) is straight from Anglo-Norman estandard with the usual loss of the French prosthetic e- in English (cf. estat > state, escarlate > scarlet). The 'measure of quality' sense is later, late 14th c., from 'the king's standard' of weights and measures.\",\n  derivation_fa=\"انگلیسی میانهٔ standard (از نیمهٔ سدهٔ دوازدهم میلادی، در پیوند با «نبرد استاندارد» ۱۱۳۸) یکراست از estandard انگلیسی-نورمن گرفته شده، با افتادنِ معمولِ e- آغازینِ فرانسوی در انگلیسی (مانند estat > state و escarlate > scarlet). معنای «معیار سنجش» دیرتر، در اواخر سدهٔ چهاردهم، از «استانداردِ شاه» در اوزان و مقادیر پدید آمده است. ادعای نورایی درست است.\",\n  sources=[\"https://www.etymonline.com/word/standard\"],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference in the book.\"}],\n  consulted=[\n    {\"src\":\"SKT\",\"where\":\"Skeat s.v. Standard (SKT.txt line 18358)\",\"stance\":\"supports\",\"note\":\"'Standard, (F, - O.H.G.) O.F. estandart, a standard or ensign ...'\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. kar-1\",\"stance\":\"supports\",\"note\":\"'... Old French estandard, rallying place: STANDARD'.\"}])\n\nN(id=18, lang=\"English\", words=\"hard, Richard, Bernard, Leonard, Gerard\",\n  verdict=\"confirmed\",\n  derivation=\"English hard continues OE heard < PGmc *harduz directly. The four names are Continental Germanic dithematic personal names whose second element is the same *hard 'hard, brave', brought into English chiefly by the Normans: Richard < Frankish *Rīk-hard 'rule-hard' (OHG Rīhhart), Bernard < *Bern-hard 'bear-hard', Leonard < *Lewin-hard/Leon-hard 'lion-hard', Gerard < *Gair-hard 'spear-hard'. Klein lists exactly this set of names at the end of his hard article; the -ard of French/English words like drunkard, sluggard is the same suffixed element.\",\n  derivation_fa=\"hard انگلیسی دنبالهٔ مستقیمِ heard انگلیسی کهن از *harduz ژرمنی آغازین است. آن چهار نام، نام‌های خاصِ دوجزئیِ ژرمنیِ قاره‌ای‌اند که جزء دومشان همان *hard «سخت، دلیر» است و بیشتر با نورمن‌ها به انگلیسی راه یافته‌اند: Richard از *Rīk-hard «سخت‌فرمان»، Bernard از *Bern-hard «خرس‌سخت»، Leonard از *Leon-hard «شیرسخت»، Gerard از *Gair-hard «نیزه‌سخت». کلاین در پایان مقالهٔ hard دقیقاً همین فهرست را می‌آورد؛ پسوندِ -ard در واژه‌هایی چون drunkard و sluggard نیز همین جزء است. ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference in the book.\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. hard, adj. (KLN_1966.txt line 17197)\",\"stance\":\"supports\",\"note\":\"'Cp. hardy, -ard, arditi, and the second element in Bernard, Everard, Gerard, Gunther, Leonard, Reynard.' (Klein's list has Everard and Reynard where Nourai has Richard; Richard's second element is the same -hard.)\"},\n    {\"src\":\"SKT\",\"where\":\"Skeat s.v. Standard\",\"stance\":\"supports\",\"note\":\"'with suffix -art (= O.H.G. hart, a suffix, orig. the same as hart, adj., hard)' — the same name-forming element.\"}])\n\nN(id=19, lang=\"Greek\", words=\"keratos; děmos-keratos; karkanos\",\n  verdict=\"transcription_suspect\",\n  derivation=\"All three Greek forms are wrong as printed, and the printed page shows them exactly as the JSON has them, so these are the author's misprints, not extraction errors. (1) 'keratos' should be κράτος krátos 'strength, power, rule' (Attic; Ionic κάρτος kártos, Aeolic κρέτος krétos); κέρατος keratos is in fact the genitive of κέρας 'horn', an unrelated word from *ḱer-. (2) 'děmos-keratos' should be δημοκρατία dēmokratía 'rule of the people' (δῆμος + κράτος), the form actually behind French démocratie. (3) 'karkanos' should be καρκίνος karkínos 'crab' (PIE suffixed *kar-k-ino-), the source of carcino-/carcinogen. Klein at the page Nourai cites for 'hard' gives the correct forms — 'Gk. kratos, Ion. kartos, Aeol. kretos, \\\"strength\\\", Gk. kratys, \\\"strong\\\"' and 'Gk. karkinos, \\\"crab\\\"' — so the misprints are Nourai's own transliteration slips. With the forms corrected, the derivations themselves are sound.\",\n  derivation_fa=\"هر سه صورتِ یونانی نادرست چاپ شده‌اند و تصویر صفحهٔ چاپی نیز همان‌ها را نشان می‌دهد؛ پس خطای چاپیِ کتاب است، نه خطای خوانشِ اسکن. یکم: «keratos» باید κράτος krátos «نیرو، توان، فرمانروایی» باشد (آتیک؛ یونیایی κάρτος، آیولی κρέτος)؛ κέρατος در حقیقت حالتِ اضافیِ κέρας «شاخ» است و از ریشهٔ دیگری (*ḱer-) می‌آید. دوم: «děmos-keratos» باید δημοκρατία dēmokratía «مردم‌سالاری» باشد (δῆμος + κράτος)، همان صورتی که پشتِ démocratie فرانسوی است. سوم: «karkanos» باید καρκίνος karkínos «خرچنگ» باشد (از *kar-k-ino-)، سرچشمهٔ carcino-/carcinogen. کلاین در همان صفحه‌ای که نورایی برای «hard» ارجاع می‌دهد صورت‌های درست را می‌آورد. با تصحیحِ صورت‌ها، خودِ ریشه‌شناسی‌ها درست است.\",\n  error_in=\"book\",\n  book_prints=\"keratos : strength, government / děmos-keratos : people's government / karkanos : crab\",\n  correct_form=\"krátos (κράτος) / dēmokratía (δημοκρατία) / karkínos (καρκίνος)\",\n  sources=[],\n  ref_check=[{\"ref\":\"AHD:351\",\"status\":\"partial\",\"note\":\"AHD:351 is the New College Edition dictionary page for DEMOCRACY; the corresponding root article, Watkins 1985 s.v. kar-1, gives '2. Extended zero-grade form *krt-es- in Greek kratos, strength, might, power: -cracy' and '4. Suffixed form *kar-k-ino- in Greek karkinos, cancer, crab: CARCINO-, CARCINOMA; (CARCINOGEN)' — the derivations are supported, but with the correct Greek forms kratos and karkinos, not keratos/karkanos.\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.vv. hard, cancer, -cracy, -crat (KLN_1966.txt lines 17197, 6333, 9522, 9573)\",\"stance\":\"partial\",\"note\":\"'Gk. kratos, \\\"strength, might, power, rule, sway, dominion\\\" ... cogn. with Goth. hardus'; '-crate, fr. Gk. -kratēs, fr. kratos, \\\"strength, power, rule\\\"'; 'Gk. karkinos, \\\"crab\\\"' — Klein has the correct spellings throughout.\"},\n    {\"src\":\"POK\",\"where\":\"POK_full.txt root kar-3, p.531\",\"stance\":\"partial\",\"note\":\"'Aeolic kretos, next to which ... Attic kratos, ep. Ionian kartos \\\"strength, power\\\", hom. kratys \\\"strong\\\"' and 'gr. karkinos ds.' — again the correct forms.\"}])\n\nN(id=20, lang=\"French\", words=\"\",\n  verdict=\"confirmed\",\n  derivation=\"An empty pass-through box standing for French démocratie (attested 1370s in Oresme's translation of Aristotle's Politics, re-popularised in the 1789 Revolution), the intermediary through which Greek dēmokratía reached both English democracy and Persian دموکراسی. The chart leaves the word unwritten but the two children make it unambiguous.\",\n  derivation_fa=\"جعبه‌ای گذرا و تهی که نمایندهٔ démocratie فرانسوی است (نخستین گواه در دههٔ ۱۳۷۰ میلادی در ترجمهٔ اورم از «سیاست» ارسطو، و رواج دوباره در انقلاب ۱۷۸۹)، همان میانجی که dēmokratía یونانی از راه آن هم به democracy انگلیسی و هم به «دموکراسی» فارسی رسیده است. واژه در نمودار نوشته نشده، اما دو فرزندِ آن جای هیچ ابهامی نمی‌گذارد. ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 s.v. kar-1 ends the Greek branch with '-cracy' and does not name the French intermediary; the AHD main-dictionary entry DEMOCRACY (p.351, the page Nourai cites for the parent node) is where 'French démocratie' stands.\"}],\n  consulted=[\n    {\"src\":\"SKT\",\"where\":\"Skeat s.v. democracy (SKT.txt line 944)\",\"stance\":\"supports\",\"note\":\"'democracy. (F.— Gk.) Formerly democratie (Milton). — O.F. democratie' — Skeat routes the word through French exactly as this box does.\"},\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. -cracy / -crat (KLN_1966.txt line 9573)\",\"stance\":\"supports\",\"note\":\"'-crate, fr. Gk. -kratēs, fr. kratos' — the French suffix is Klein's stated intermediary.\"}])\n\nN(id=21, lang=\"Persian\", words=\"demokrâsî «دموکراسی»\",\n  verdict=\"confirmed\",\n  derivation=\"Persian دموکراسی demokrāsi is a direct loan of French démocratie, taken in during the Constitutional period (mašruṭe, 1905-11) along with the rest of the modern political vocabulary (پارلمان, کنستیتوسیون, ملیت); the Persian shape -krāsi rather than -krasī reflects the French stress and vowel, and the spelling with و rather than a long ā in the first syllable follows the French [demɔ-]. It is a European loan, not an inherited Iranian form.\",\n  derivation_fa=\"«دموکراسی» وام‌واژه‌ای مستقیم از démocratie فرانسوی است که در دورهٔ مشروطه (۱۲۸۴–۱۲۹۰ خورشیدی) همراه با دیگر واژگان سیاسی نو (پارلمان، کنستیتوسیون، ملّیت) به فارسی درآمد؛ صورتِ -کراسی به‌جای -کراتیا، تکیه و واکهٔ فرانسوی را بازمی‌تاباند. این واژه وام‌واژه‌ای اروپایی است، نه صورتی موروثی از ایرانی. ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"MON:1561\",\"status\":\"not_checked\",\"note\":\"Moʿin's foreign-words volume is not paginated online and the local MON OCR files return no hits for 'دموکراسی'; the entry could not be read.\"}],\n  consulted=[\n    {\"src\":\"MON\",\"where\":\"Farhang-e Moʿin\",\"stance\":\"silent\",\"note\":\"could not be read (see ref_check); Moʿin's practice is to tag such words [فر.], as he does for کنگره ۲ 'congress'.\"},\n    {\"src\":\"SKT\",\"where\":\"Skeat s.v. democracy\",\"stance\":\"supports\",\"note\":\"'(F.— Gk.) ... — O.F. democratie' — establishes the French form that Persian borrowed.\"}])\n\nN(id=22, lang=\"English\", words=\"democracy\",\n  verdict=\"confirmed\",\n  derivation=\"English democracy (1570s, earlier democratie in Milton) is from Middle French démocratie, from Late Latin dēmocratia, from Greek dēmokratía 'popular government', δῆμος 'people, deme' + -κρατία 'rule' (κράτος). Watkins files -cracy under kar-1 via the extended zero-grade *kr̥t-es-.\",\n  derivation_fa=\"democracy انگلیسی (از دههٔ ۱۵۷۰، و پیش‌تر به صورت democratie نزد میلتون) از démocratie فرانسوی میانه، از dēmocratia لاتینِ پسین، از dēmokratía یونانی «فرمانروایی مردم» است: δῆμος «مردم، دِه» + -κρατία «فرمانروایی» (از κράτος). واتکینز پسوندِ -cracy را زیر ریشهٔ kar-1 و از راهِ صورتِ گستردهٔ *kr̥t-es- می‌آورد. ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference in the book.\"}],\n  consulted=[\n    {\"src\":\"SKT\",\"where\":\"Skeat s.v. democracy (SKT.txt line 944)\",\"stance\":\"supports\",\"note\":\"'democracy. (F.— Gk.) Formerly democratie (Milton). — O.F. democratie'.\"},\n    {\"src\":\"KLN\",\"where\":\"Klein s.vv. -cracy, -crat\",\"stance\":\"supports\",\"note\":\"'-crate, fr. F. -crate, fr. Gk. -kratēs, fr. kratos, \\\"strength, power, rule\\\". See -cracy.'\"}])\n\nN(id=23, lang=\"English\", words=\"carcinogen\",\n  verdict=\"confirmed\",\n  derivation=\"carcinogen (1853 in the sense 'cancer-producing agent'; common from the 1930s) is a modern scientific compound of Greek καρκίνος karkínos 'crab, cancer' + -γενής -genēs 'producing' (root *ǵenh₁-). Watkins lists CARCINOGEN, in parentheses as a secondary derivative, under 'Suffixed form *kar-k-ino- in Greek karkinos'. The chart is right that this is the Greek, not the Latin, member of the crab family — English keeps both, carcino- from Greek and cancer from Latin, as a doublet.\",\n  derivation_fa=\"carcinogen (از ۱۸۵۳ به معنای «سرطان‌زا»، و رایج از دههٔ ۱۹۳۰) ترکیبی علمی و نوساخته است از καρκίνος یونانی «خرچنگ، سرطان» به‌علاوهٔ -γενής «زاینده» (از ریشهٔ *ǵenh₁-). واتکینز واژهٔ CARCINOGEN را — در پرانتز و به‌عنوان مشتق ثانوی — زیر «صورت پسونددارِ *kar-k-ino- در karkinos یونانی» می‌آورد. نمودار درست تشخیص داده که این عضو یونانیِ خانوادهٔ «خرچنگ» است، نه لاتینیِ آن؛ انگلیسی هر دو را نگه داشته است: carcino- از یونانی و cancer از لاتین، همچون دوگانه (doublet). ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference in the book.\"}],\n  consulted=[\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. kar-1\",\"stance\":\"supports\",\"note\":\"'4. Suffixed form *kar-k-ino- in Greek karkinos, cancer, crab: CARCINO-, CARCINOMA; (CARCINOGEN).'\"},\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. cancer (KLN_1966.txt line 6333)\",\"stance\":\"supports\",\"note\":\"'cogn. with Gk. karkinos, \\\"crab\\\" ... See hard and cp. canker, carcinoma, chancre.'\"}])\n\nN(id=24, lang=\"Latin\", words=\"carcro; cancer\",\n  verdict=\"plausible\",\n  derivation=\"Latin cancer, gen. cancrī, 'crab; the zodiac sign; ulcer, cancer' is certainly from this root, and 'carcro' is not a Latin word but the reconstructed pre-form *carcro- (< reduplicated *kar-kr-o-) from which cancer is dissimilated — the very wording of Klein at the page cited ('L., \\\"crab, ulcer, cancer\\\", dissimilated fr. *carcro-') and of Pokorny ('Latin cancer, -crī ... dissim. from *carcro-, perhaps already Indo Germanic'). So the box is faithful to its source; what is misleading is that it prints the asterisked reconstruction as if it were an attested Latin word, and glosses it 'hard' rather than 'crab'. Watkins likewise: 'Reduplicated form *kar-kr-o dissimilated to Latin cancer, crab'.\",\n  derivation_fa=\"cancer لاتین، اضافیِ cancrī، «خرچنگ؛ برج سرطان؛ زخمِ خوره، سرطان» بی‌گمان از همین ریشه است، اما «carcro» واژه‌ای لاتین نیست بلکه صورت بازسازی‌شدهٔ *carcro- (از *kar-kr-o- مضاعف) است که cancer با ناهمگونی (dissimilation) از آن پدید آمده — همان تعبیری که کلاین در صفحهٔ مورد ارجاع به‌کار می‌برد («لاتین، \\\"خرچنگ، زخم، سرطان\\\"، ناهمگون‌شده از *carcro-») و پوکورنی نیز («cancer لاتین ... با ناهمگونی از *carcro-، شاید همان‌گونه در هندواروپایی»). پس جعبه به مأخذش وفادار است؛ آنچه گمراه‌کننده است این است که صورتِ ستاره‌دارِ بازسازی‌شده را چون واژه‌ای گواهی‌شده و با معنای «سخت» (به‌جای «خرچنگ») چاپ کرده است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"KLN:230\",\"status\":\"supports\",\"note\":\"Klein s.v. cancer (KLN_1966.txt line 6333, leaf 132): 'cancer, n., a malignant growth. — L., \\\"crab, ulcer, cancer\\\", dissimilated fr. *carcro- and cogn. with Gk. karkinos, \\\"crab\\\", lit. \\\"the animal with the hard shell\\\", fr. I.-E. base *qarq-, *qraq-, \\\"to be hard\\\", whence also OI. karkatakah, karkah, \\\"crab\\\", karkarah, \\\"hard\\\".' Both of Nourai's Latin words come from this one entry.\"}],\n  consulted=[\n    {\"src\":\"POK\",\"where\":\"POK_full.txt root kar-3, p.531\",\"stance\":\"supports\",\"note\":\"'gr. karkinos ds., Latin cancer, -crī ds. (dissim. from *carcro-, perhaps already Indo Germanic ...)'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. I 354 (leaf 362)\",\"stance\":\"supports\",\"note\":\"'lat. cancer, -cri ds. (diss. aus *carcro-, vielleicht schon idg. ...)' — note that Walde-Pokorny explicitly rejects Havet's and Solmsen's alternative metathesis from *qarqno-.\"}])\n\nN(id=25, lang=\"English\", words=\"cancer\",\n  verdict=\"confirmed\",\n  derivation=\"English cancer is a straight learned borrowing of Latin cancer, in Old English already as cancer 'spreading sore' (a very early Latin loan), re-borrowed in the medical sense c.1600; the popular Old French development of the same Latin word gave chancre and canker, so English holds a triplet cancer / canker / chancre from one Latin etymon.\",\n  derivation_fa=\"cancer انگلیسی وام‌واژه‌ای دانشورانه و مستقیم از cancer لاتین است؛ در انگلیسی کهن نیز به‌صورت cancer «زخمِ گسترنده» (وامی بسیار کهن از لاتین) دیده می‌شود و در معنای پزشکی امروزی نزدیک ۱۶۰۰ میلادی دوباره وام گرفته شده است. تحولِ عامیانهٔ همان واژهٔ لاتین در فرانسوی کهن chancre و canker را داده است؛ پس انگلیسی از یک ریشهٔ لاتینِ واحد سه‌گانهٔ cancer / canker / chancre را دارد. ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference in the book.\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. cancer (KLN_1966.txt line 6333)\",\"stance\":\"supports\",\"note\":\"'See hard and cp. canker, carcinoma, chancre' — Klein's own cross-references for the English triplet.\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. kar-1\",\"stance\":\"supports\",\"note\":\"'... dissimilated to Latin cancer, crab: CANCER, CANKER, CHANCRE.'\"}])\n\nN(id=26, lang=\"Indo-European\", words=\"Qusěro\",\n  verdict=\"plausible\",\n  derivation=\"This is a headword of S. E. Mann's Indo-European Comparative Dictionary, quoted almost verbatim: 'qusero, id \\\"scrape, scratch, itch\\\". Cf. qusoros and next. Per. (ambig. *-ē- or *-o-) xaram, v. \\\"scratch, itch\\\"; Alb. cf. shorë, f. \\\"rash, eruption on skin\\\"; R šarju, inf. šarit, v. \\\"rummage\\\"'. So the reconstruction and the gloss are Mann's, and the Persian verb is Mann's own witness. But it is a private reconstruction: Mann himself flags the neighbouring quseros 'rough, harsh' as 'Phonol. ambig.', the root is not in Pokorny or Watkins under any comparable shape, and it is in any case a different etymon from the *kar- 'hard' of the rest of the chart — Nourai has simply appended it to the root box because both begin with a velar. Note also that Mann's entry stands at printed pp.1140-41, not at the p.1056 the chart cites.\",\n  derivation_fa=\"این سرواژه از «فرهنگ تطبیقی هندواروپایی» استوارت مان است و تقریباً واژه‌به‌واژه نقل شده: «qusero، \\\"خراشیدن، خاراندن، خارش\\\". Per. xaram \\\"خاریدن\\\"؛ آلبانیایی shorë \\\"جوش پوستی\\\"؛ روسی šarit \\\"جست‌وجو کردن\\\"». پس بازسازی و معنا از مان است و فعل فارسی نیز گواهِ خودِ اوست. اما این بازسازی شخصی است: مان دربارهٔ مدخل همسایهٔ quseros خود می‌نویسد «از نظر آواشناسی مبهم»، چنین ریشه‌ای نه در پوکورنی هست و نه در واتکینز، و به هر روی ریشه‌ای جداست از *kar- «سخت» که بقیهٔ نمودار بر آن استوار است؛ نورایی تنها به سببِ آغازِ کامی مشترک آن را به جعبهٔ ریشه چسبانده است. افزون بر این، مدخل مان در صفحه‌های ۱۱۴۰–۱۱۴۱ است، نه ۱۰۵۶ که نمودار ارجاع می‌دهد. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"IEC:1056\",\"status\":\"not_found\",\"note\":\"IEC.txt leaf 543 = printed pp.1056-57 is the pork-/porKos article ('surrounding, edge, rim' / 'hog; sow'). The entries Nourai means are on leaf 585 = printed pp.1140-41: 'qusero, id \\\"scrape, scratch, itch\\\" ... Per. xaram, v. \\\"scratch, itch\\\"' and 'quseros \\\"rough, harsh\\\". (Variant: qusóros). Cf. kseros, and WP I, 355 Skt. kharah (\\\"rough, sharp, hard\\\". Phonol. ambig.)'. The reference supports the content but the page number is wrong.\"}],\n  consulted=[\n    {\"src\":\"POK\",\"where\":\"POK_full.txt\",\"stance\":\"silent\",\"note\":\"Pokorny has no root of the shape *kus-er-/*kʷes-er- 'scratch'; the nearest, kars- 'to card' (p.532) and (s)ker- 'cut', are different.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. I 355 (leaf 363), s.v. qars- 'kratzen'\",\"stance\":\"partial\",\"note\":\"'... bleiben bei ai. kasati \\\"kratzt\\\", aksl. krasta \\\"Krätze\\\" usw. (s. Falk-Torp u. harsh, Berneker 575); s. qars- \\\"kratzen\\\"' — Walde-Pokorny do have a 'scratch' root next to qar- 'hard', which is presumably what Mann's qusero- reworks, but they do not cite the Persian verb.\"}])\n\nN(id=27, lang=\"Persian\", words=\"xârîdan «خاریدن»\",\n  verdict=\"disputed\",\n  derivation=\"خاریدن xāridan 'to scratch, itch' (with خارش xāreš 'itch' and the causative خاراندن xārāndan) is a real Persian verb, and Mann's IEC entry does cite it ('Per. xaram, v. \\\"scratch, itch\\\"'), so Nourai's arrow reproduces his source. But the modern standard treatment of Iranian verbs, Cheung's Etymological Dictionary of the Iranian Verb (2007), files it under a quite different root: *huar 'to have a sore, scratch, itch', with Young Avestan xʷara- (n.) 'wound, sore' (Y 57.10, V 4.30, 4.33), Kurdish xurîn 'to itch', Ossetic xæryn/xward, Shughni xir-, Yazghulami xʷer 'to itch, scratch' and 'NP xārāndan/xārān-' — the Persian causative — and derives the whole set from PIE *swer- 'to have a sore' (LIV 613, Pokorny 1050). On that account the initial x- is from Iranian *hu̯- (*sw-), not from a velar, and Persian خاریدن has nothing to do with either 'hard' or Mann's *qusero-. There is also a real risk of contamination with خار 'thorn' (whence 'to prick') in the Persian word's history, which Cheung flags for the neighbouring *xrau family.\",\n  derivation_fa=\"«خاریدن» (با «خارش» و سببیِ «خاراندن») فعلی اصیل در فارسی است و مان نیز آن را در مدخل خود گواه آورده («Per. xaram \\\"خاریدن\\\"»)، پس پیکان نورایی مأخذش را بازمی‌گوید. اما مرجع استاندارد امروزی برای فعل‌های ایرانی، یعنی «فرهنگ ریشه‌شناختی فعل ایرانی» چونگ (۲۰۰۷)، آن را زیر ریشه‌ای یکسره دیگر می‌آورد: *huar «زخم داشتن، خاراندن، خارش داشتن»، با اوستاییِ نو xʷara- «زخم» (یسنا ۵۷٫۱۰، وندیداد ۴٫۳۰ و ۴٫۳۳)، کردی xurîn، آسی xæryn/xward، شغنی xir-، یزغلامی xʷer «خاریدن» و «NP xārāndan/xārān-»، و همهٔ این‌ها را از *swer- هندواروپایی «زخم داشتن» می‌گیرد (LIV ۶۱۳، پوکورنی ۱۰۵۰). بر این پایه، x- آغازین از *hu̯- (*sw-) ایرانی است نه از یک واکِ کامی، و «خاریدن» نه با «سختی» پیوند دارد و نه با *qusero- مان. پژوهش امروزی ادعای نورایی را رد می‌کند و به‌جای آن ریشهٔ *huar را می‌نهد.\",\n  sources=[],\n  ref_check=[{\"ref\":\"IEC:1056\",\"status\":\"not_found\",\"note\":\"the qusero entry with 'Per. xaram' is on IEC leaf 585 = printed pp.1140-41, not on p.1056 (leaf 543 = pork-/porKos). Content-wise Mann does support the arrow; the page number does not.\"}],\n  consulted=[\n    {\"src\":\"CHEUNG\",\"where\":\"Cheung 2007 s.v. *huar (CHEUNG.txt lines 10489-10505)\",\"stance\":\"contradicts\",\"note\":\"'*huar \\\"to have a sore, scratch, itch\\\" ... Y Av. xʷara- (n.) \\\"wound, sore\\\" ... (caus.) NP xārāndan/xārān- ... Oss. I. xæryn/xward ... «PIE *suer- \\\"to have a sore\\\" = LIV: 613 | Pok.: 1050»'.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann, leaf 585 = pp.1140-41\",\"stance\":\"supports\",\"note\":\"'qusero, id \\\"scrape, scratch, itch\\\". Cf. qusoros and next. Per. (ambig. *-ē- or *-o-) xaram, v. \\\"scratch, itch\\\"'.\"},\n    {\"src\":\"HRN\",\"where\":\"Horn, Grundriss (HRN.txt)\",\"stance\":\"silent\",\"note\":\"Horn's numbered entries 461-476 cover xār, xārā, xar, xarbuze, xarčang, xaridan 'to buy' (no. 482, from Skt. krī-) but he gives no entry for xāridan 'to scratch'.\"}])\n\nentry = {\n \"entry\": 0,\n \"root\": \"Kar 1, Qar 1, Quseros, Qhar; Karkar, Kongar\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *kar-/*ker- 'hard' (Pok. 3. kar-, 531), with the t-extension *kret-/*kort-ú- 'strong, firm' and the reduplicated *kar-kr-o- 'hard-shelled animal, crab'\",\n \"note\": \"The root box is a bundle of at least three of Walde-Pokorny's headwords plus one of Mann's, which is why it carries four names. 'Kar 1 / Qar 1 / Karkar' = WP I 354 = Pokorny 531 'kar-3, redupl. karkar- \\\"hart\\\"' (Skt. karkara-, karkaṭa-, Gk. karkaros/karkinos, Lat. cancer < *carcro-, Goth. hardus < *kar-tu-, and by the extension *kre-t- Gk. kratos/kartos). 'Qhar' = WP I 355 'qhar- \\\"scharf, spitz\\\"' (Skt. khara- 'hard, rough, sharp', NP xār, xārā), which is where the thorn/donkey branch comes from. 'Kongar' answers to Skt. kaṅkaṭa- 'coat of mail' < *kaṅkr̥ta-, cited by both WP and Pokorny under kar-. 'Quseros' is Mann's own headword qusero/quseros 'scrape, scratch; rough' (IEC pp.1140-41), a separate and shakier etymon. The gloss 'hard' is right; 'hardened or fortified, armor, fort' over-reads the Sanskrit mail-coat word. The two real weaknesses are (a) Avestan xratu-, which Pokorny at the cited page expressly removes from this root, and (b) the donkey word, which modern Indo-Iranian scholarship treats as an independent (possibly substrate) lexeme rather than a substantivised 'hard'.\",\n \"note_fa\": \"جعبهٔ ریشه در واقع دست‌کم سه سرواژهٔ والده-پوکورنی به‌علاوهٔ یک سرواژهٔ مان است، و از همین‌روست که چهار نام دارد. «Kar 1 / Qar 1 / Karkar» همان WP جلد یکم ص ۳۵۴ و پوکورنی ص ۵۳۱ است: «kar-3، با صورت مضاعف karkar- \\\"سخت\\\"» (karkara- و karkaṭa- سنسکریت، karkaros و karkinos یونانی، cancer لاتین از *carcro-، hardus گوتی از *kar-tu-، و با گسترشِ *kre-t- واژهٔ kratos یونانی). «Qhar» همان WP ص ۳۵۵ است: «qhar- \\\"تیز، نوک‌تیز\\\"» (khara- سنسکریت «سخت، زبر، تیز»، و xār و xārā فارسی) که شاخهٔ خار و خر از آن می‌آید. «Kongar» به kaṅkaṭa- سنسکریت «زره» از *kaṅkr̥ta- بازمی‌گردد که هم WP و هم پوکورنی زیر kar- می‌آورند. «Quseros» اما سرواژهٔ شخصیِ مان است (qusero/quseros «خراشیدن؛ زبر»، صفحه‌های ۱۱۴۰–۱۱۴۱) و ریشه‌ای جدا و سست‌تر. معنای «سخت» درست است، ولی «استوارشده یا دژوار، زره، دژ» بیش از اندازه از واژهٔ سنسکریتِ «زره» نتیجه گرفته شده است. دو نقطهٔ ضعف واقعی: نخست xratu- اوستایی که پوکورنی در همان صفحهٔ مورد ارجاع صریحاً از این ریشه بیرون می‌گذارد، و دوم واژهٔ «خر» که ایران‌شناسی امروزی آن را واژه‌ای مستقل (و شاید وام از زیرلایه) می‌داند نه صفتِ «سخت» که اسم شده باشد.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/harduz\", W+\"%D8%AE%D8%B1\"],\n \"ref_check\": [\n   {\"ref\":\"POK:531\",\"status\":\"partial\",\"note\":\"POK_full.txt 'Root / lemma: kar-3, redupl. karkar-; Meaning: hard; Pages: 530-531' — supports the 'hard' root, the crab words, the Sanskrit mail-coat and Germanic *hardu-, but at the same page states 'remains far off Old Indie kratu-, Avestan xratus \\\"spiritual power\\\"', contradicting the chart's first branch; and Pokorny's kar-3 contains no donkey and no 'scratch' material.\"},\n   {\"ref\":\"IEC:1056\",\"status\":\"not_found\",\"note\":\"IEC.txt leaf 543 = printed pp.1056-57 is the pork-/porKos article. Mann's qusero/quseros entries are at leaf 585 = pp.1140-41.\"},\n   {\"ref\":\"IEC:1632\",\"status\":\"not_found\",\"note\":\"IEC.txt leaf 831 = printed pp.1632-33 is inside the uel- 'wish' article. Mann's kankǝr- 'hook, bend, curl' is at leaf 269 = pp.508-09 and his kartus 'hard, harsh, bitter' at leaf 274 = pp.518-19; there is no 'Kongar' headword in IEC.\"}],\n \"consulted\": [\n   {\"src\":\"WLD\",\"where\":\"Bd. I 354-355 (WLD_Bd1_pages.txt leaves 362-363)\",\"stance\":\"supports\",\"note\":\"'3. qar-, redupl. qarqar- u. dgl. \\\"hart\\\"' on p.354 and 'qhar- \\\"scharf, spitz\\\"' on p.355 — the two names of Nourai's root box, with the Sanskrit, Greek, Latin, Germanic and New Persian material he uses; p.355 also still files the 'Verstand' word (xratu-) here, which Pokorny 1959 removed.\"},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. kar-1 'Hard'\",\"stance\":\"supports\",\"note\":\"'kar-1. Hard. I. Variant form ker-. 1. Suffixed o-grade form *kor-tu- in Germanic *harduz ... 2. Extended zero-grade form *krt-es- in Greek kratos ... II. Basic form *kar- in derivatives referring to things with hard shells ... [Pok. 3. kar- 531.]' — the same bundle, minus the Iranian branch.\"},\n   {\"src\":\"KLN\",\"where\":\"Klein s.vv. hard and cancer (KLN_1966.txt lines 17197, 6333)\",\"stance\":\"supports\",\"note\":\"'fr. I.-E. base *qar-, \\\"hard\\\". Fr. I.-E. *qret-, *qr̥t-, a -t-enlargement of base *qar-, derive Gk. kratos ... Cp. I.-E. *quar-q-, whence OI. karkatah, \\\"crab\\\" ... L. cancer (dissimilated fr. *carcro-)' — Klein unites the same two sub-families.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann, leaves 274 and 585 (pp.518-19, 1140-41)\",\"stance\":\"partial\",\"note\":\"'kartus \\\"hard, harsh, bitter\\\". Cf. WP I, 354 & II, 578. Cf. kratus Gk. *kartus ... Go. hardus' supports the hard/strong side; 'quseros \\\"rough, harsh\\\" ... Cf. kseros, and WP I, 355 Skt. kharah (\\\"rough, sharp, hard\\\". Phonol. ambig.)' shows Mann himself hedging the qus- root.\"}],\n \"nodes\": nodes,\n}\n\ndoc = {\n \"pdf_page\": 242,\n \"book_page\": 212,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [entry],\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-242.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('ok', len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk242.py",
 "description": "Generate page-242.json"
}
```


### [2026-09-06T16:08:55.289Z] TOOL RESULT

```
ok 27
```


## [2026-09-06T16:08:59.877Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-242.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 242",
 "description": "Validate and run verify_check"
}
```


### [2026-09-06T16:09:01.750Z] TOOL RESULT

```
JSON OK
nodes verified: 27/27
node verdicts: {'plausible': 7, 'confirmed': 16, 'disputed': 2, 'unverified': 1, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'contradicts': 2, 'not_found': 5, 'not_checked': 9, 'supports': 17, 'partial': 5}
books consulted: {'supports': 41, 'partial': 7, 'contradicts': 3, 'silent': 9} | by book: {'WLD': 7, 'SKT': 7, 'KLN': 7, 'AHD': 6, 'PHD': 6, 'POK': 5, 'BRT': 3, 'HUB': 3, 'HRN': 3, 'MON': 3, 'NYB': 2, 'SOD': 2, 'IEC': 2, 'SYN': 1, 'LKT': 1, 'TTS': 1, 'CHEUNG': 1}
```


## [2026-09-06T16:09:18.257Z] AGENT

Page 242 (book p. 212) verified — one entry, root "Kar 1, Qar 1, Quseros, Qhar; Karkar, Kongar", all 27 nodes. `verify_check.py 242` reports 0 PROBLEM lines.

**Verdicts:** root plausible; nodes: 16 confirmed, 7 plausible, 2 disputed, 1 unverified, 1 transcription_suspect.
**Ref checks:** 17 supports, 5 partial, 5 not_found, 2 contradicts, 9 not_checked. 17 different books consulted.

**Flagged items**
- **disputed — قاطر qâter 'mule' (node 11):** Nourai derives it from Sogdian γrtrʼk *xara-tara-, but Moʿin — the very reference he cites (MON:2615) — tags it `[تر.]` Turkic; Lokotsch no. 1131 and Wiktionary agree (Turkic *katır). No source routes it through Sogdian.
- **disputed — خاریدن xârîdan 'to scratch' (node 27):** Cheung 2007 puts it under Iranian *huar 'to have a sore/itch' (Av. xʷara- 'wound', PIE *swer-, Pok. 1050), not under Mann's *quseros.
- **transcription_suspect — Greek node 19:** the book prints `keratos`, `děmos-keratos`, `karkanos`; correct forms are κράτος krátos, δημοκρατία dēmokratía, καρκίνος karkínos. `error_in: "book"` — the printed page (checked at 300 dpi, copied to `data/verification/sources/refs/ocr/BOOK/242.png`) shows exactly what the JSON has, so the extraction is faithful.
- **unverified — کنگره kongareh (node 13):** no source links it to Skt kaṅkaṭa-; Moʿin gives کنگره ۱ no etymology, and Persian scholarship calls its origin unclear.

**Notable ref problems (author's, not extraction):** POK:531 actually *contradicts* the xratu branch ("remains far off Old Indic kratu-, Avestan xratuš"); IEC:1056 and IEC:1632 are both wrong pages — Mann's `qusero/quseros` stands at pp. 1140-41 and his `kankǝr-` (glossed 'hook, bend, curl', not 'armor') at pp. 508-09; SYN:1201 is Buck's "BRAVE" section and nowhere cites xratu-. Conversely WLD:355 is exactly right (WP's `qhar-`, incl. Uhlenbeck's donkey-from-'hard' claim), as are BQT:697/729, SOD:166 and KLN:230.

**No extraction errors found** — the JSON matches the printed page throughout.
