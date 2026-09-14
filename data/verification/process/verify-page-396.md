# Verification process log — verify-page-396


## [2026-09-14T00:49:46.683Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 396 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-396.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-396.json. Write /home/sfmqrb/git/rishe/data/verification/page-396.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 396` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:49:47.713Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:49:48.528Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:49:48.543Z] TOOL RESULT

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


## [2026-09-14T00:49:48.990Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-396.txt"
}
```


### [2026-09-14T00:49:49.032Z] TOOL RESULT

```
1	=== PDF page 396 (book page 366) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Per 3 : opposite, against, in front of, strike. Related to the Indo-European root "Per 1".  (refs POK:815-818)  PART 1
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:815 | paiti 2, paitî 3, pati, patiy : opposite, in front of, against
5	  #2 (parent #1) [Pahlavi] refs=BQT:440 | paitiš, pat, pěš : in front of, before, leader
6	    #3 (parent #2) [Persian] refs=BQT:242,440,2405 | pîš «پیش (پیشینه)» : front, ahead ; bod, bad 2 «-بد» : (suffix) leadership | extra: پیشانی ، پیشوا ، پیشرفت ، پیشخدمت
7	سپهبد ، هیربد ، موبد
8	  #4 (parent #1) [Pahlavi] refs=HRN:33; AEF:190 | pad, pa : to, toward | NOTE: HRN:33 claims these prefixes are combinations of Avestan "upa" and "paiti". See root "Upo".
9	    #5 (parent #4) [Persian] refs=AEF:190,191 | be[h] «به (په ۲)» : to, toward | NOTE: The "b-" and "p-" prefixes have lost their original meaning.
10	#6 (parent #0) [Avestan] refs=HRN:68-88; BQT:400-445 | paiti-kan : front digger ☞Gwhen 1 ; paiti-gar : say against someone, blame ☞Gwer 2 ; paiti-gama : bring forward (a message) ☞Gwa ; paiti-kâra : do (fight) against ☞Kwer
11	  #7 (parent #6) [Persian] refs=BQT; HRN | paykân «پیکان» : arrow tip ; payğâreh «پیغاره» : blame ; payğâm «پیغام (پیغمبر ، پیام ، پیامبر)» : message ; paykâr «پیکار» : fight
12	#8 (parent #0) [Avestan] refs=HRN:68-88; BQT:400-445 | paiti-band : to bond against/with ☞Bhendh ; paiti-man : to think against, regret ☞Men 1
13	  #9 (parent #8) [Persian] refs=BQT; HRN | payvastan «پیوستن (پیوند)» : join ; pažmân «پژمان (پشیمان)» : regretting
14	#10 (parent #0) [Avestan] refs=HRN:68-88; BQT:354,400-434; FSF:99; POK:243 | paiti-ma : to measure against ☞Me ; paiti-raeč : to leave, avoid ☞Leigh 2 ; paiti-dâhišn : given back, reward ☞Dô 2 ; paiti-sahva : answer to speech ☞Kâs 2 ; paiti-râman : well arranged, pleasant ☞Rem
15	  #11 (parent #10) [Persian] refs=BQT; HRN | paymǔdan «پیمودن» : to walk, measure ; parhîxtan «پرهیختن (پرهیز)» : to avoid ; pâdâš «پاداش (پاداشن)» : reward ; pâsox «پاسخ» : answer ; Pedrâm «پدرام» : "pleasant" | extra: پیمانه، پیمان
16	#12 (parent #0) [Avestan] refs=POK:818 | peret : fight against ; ni-part : fight down ☞Nî 1 ; â-part : battle ☞Apo
17	  #13 (parent #12) [Persian] refs=BQT:2115; HRN:230 | nabard «نبرد» : battle ; âvard «آورد (آوردگاه)» : battle
18	
```


## [2026-09-14T00:49:52.131Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-396.json | head -200",
 "description": "Read page 396 source JSON"
}
```


## [2026-09-14T00:49:52.836Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T00:49:53.232Z] TOOL RESULT

```
{
    "pdf_page": 396,
    "book_page": 366,
    "entries": [
        {
            "root": {
                "name": "Per 3",
                "lang": "Indo-European",
                "refs": "POK:815-818",
                "gloss": "opposite, against, in front of, strike. Related to the Indo-European root \"Per 1\"."
            },
            "part": 1,
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "POK:815",
                    "words": [
                        {
                            "translit": "paiti 2, pait\u00ee 3, pati, patiy",
                            "gloss": "opposite, in front of, against",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Pahlavi",
                    "refs": "BQT:440",
                    "words": [
                        {
                            "translit": "paiti\u0161, pat, p\u011b\u0161",
                            "gloss": "in front of, before, leader",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "BQT:242,440,2405",
                    "words": [
                        {
                            "translit": "p\u00ee\u0161",
                            "gloss": "front, ahead",
                            "script": "\u067e\u06cc\u0634 (\u067e\u06cc\u0634\u06cc\u0646\u0647)"
                        },
                        {
                            "translit": "bod, bad 2",
                            "gloss": "(suffix) leadership",
                            "script": "-\u0628\u062f"
                        }
                    ],
                    "script_extra": "\u067e\u06cc\u0634\u0627\u0646\u06cc \u060c \u067e\u06cc\u0634\u0648\u0627 \u060c \u067e\u06cc\u0634\u0631\u0641\u062a \u060c \u067e\u06cc\u0634\u062e\u062f\u0645\u062a\n\u0633\u067e\u0647\u0628\u062f \u060c \u0647\u06cc\u0631\u0628\u062f \u060c \u0645\u0648\u0628\u062f",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 1,
                    "lang": "Pahlavi",
                    "refs": "HRN:33; AEF:190",
                    "words": [
                        {
                            "translit": "pad, pa",
                            "gloss": "to, toward",
                            "script": null
                        }
                    ],
                    "note": "HRN:33 claims these prefixes are combinations of Avestan \"upa\" and \"paiti\". See root \"Upo\".",
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Persian",
                    "refs": "AEF:190,191",
                    "words": [
                        {
                            "translit": "be[h]",
                            "gloss": "to, toward",
                            "script": "\u0628\u0647 (\u067e\u0647 \u06f2)"
                        }
                    ],
                    "note": "The \"b-\" and \"p-\" prefixes have lost their original meaning.",
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "HRN:68-88; BQT:400-445",
                    "words": [
                        {
                            "translit": "paiti-kan",
                            "gloss": "front digger",
                            "script": null,
                            "see": [
                                "Gwhen 1"
                            ]
                        },
                        {
                            "translit": "paiti-gar",
                            "gloss": "say against someone, blame",
                            "script": null,
                            "see": [
                                "Gwer 2"
                            ]
                        },
                        {
                            "translit": "paiti-gama",
                            "gloss": "bring forward (a message)",
                            "script": null,
                            "see": [
                                "Gwa"
                            ]
                        },
                        {
                            "translit": "paiti-k\u00e2ra",
                            "gloss": "do (fight) against",
                            "script": null,
                            "see": [
                                "Kwer"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "Persian",
                    "refs": "BQT; HRN",
                    "words": [
                        {
                            "translit": "payk\u00e2n",
                            "gloss": "arrow tip",
                            "script": "\u067e\u06cc\u06a9\u0627\u0646"
                        },
                        {
                            "translit": "pay\u011f\u00e2reh",
                            "gloss": "blame",
                            "script": "\u067e\u06cc\u063a\u0627\u0631\u0647"
                        },
                        {
                            "translit": "pay\u011f\u00e2m",
                            "gloss": "message",
                            "script": "\u067e\u06cc\u063a\u0627\u0645 (\u067e\u06cc\u063a\u0645\u0628\u0631 \u060c \u067e\u06cc\u0627\u0645 \u060c \u067e\u06cc\u0627\u0645\u0628\u0631)"
                        },
                        {
                            "translit": "payk\u00e2r",
                            "gloss": "fight",
                            "script": "\u067e\u06cc\u06a9\u0627\u0631"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "HRN:68-88; BQT:400-445",
                    "words": [
                        {
                            "translit": "paiti-band",
                            "gloss": "to bond against/with",
                            "script": null,
                            "see": [
                                "Bhendh"
                            ]
                        },
                        {
                            "translit": "paiti-man",
                            "gloss": "to think against, regret",
                            "script": null,
                            "see": [
                                "Men 1"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "Persian",
                    "refs": "BQT; HRN",
                    "words": [
                        {
                            "translit": "payvastan",
```


### [2026-09-14T00:49:53.272Z] TOOL RESULT

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


## [2026-09-14T00:50:07.425Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-396.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-14T00:50:08.577Z] TOOL RESULT

```
                            "translit": "payvastan",
                            "gloss": "join",
                            "script": "\u067e\u06cc\u0648\u0633\u062a\u0646 (\u067e\u06cc\u0648\u0646\u062f)"
                        },
                        {
                            "translit": "pa\u017em\u00e2n",
                            "gloss": "regretting",
                            "script": "\u067e\u0698\u0645\u0627\u0646 (\u067e\u0634\u06cc\u0645\u0627\u0646)"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u062e\u062f\u0627\u0648\u0646\u062f \u0632\u06cc\u0628\u0627\u06cc \u0628\u0631\u062a\u0631 \u0645\u0646\u0634 - \u0627\u0632 \u0627\u0648 \u062f\u0648\u0631 \u067e\u06cc\u063a\u0627\u0631\u0647 \u0648 \u0633\u0631\u0632\u0646\u0634",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 10,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "HRN:68-88; BQT:354,400-434; FSF:99; POK:243",
                    "words": [
                        {
                            "translit": "paiti-ma",
                            "gloss": "to measure against",
                            "script": null,
                            "see": [
                                "Me"
                            ]
                        },
                        {
                            "translit": "paiti-rae\u010d",
                            "gloss": "to leave, avoid",
                            "script": null,
                            "see": [
                                "Leigh 2"
                            ]
                        },
                        {
                            "translit": "paiti-d\u00e2hi\u0161n",
                            "gloss": "given back, reward",
                            "script": null,
                            "see": [
                                "D\u00f4 2"
                            ]
                        },
                        {
                            "translit": "paiti-sahva",
                            "gloss": "answer to speech",
                            "script": null,
                            "see": [
                                "K\u00e2s 2"
                            ]
                        },
                        {
                            "translit": "paiti-r\u00e2man",
                            "gloss": "well arranged, pleasant",
                            "script": null,
                            "see": [
                                "Rem"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 10,
                    "lang": "Persian",
                    "refs": "BQT; HRN",
                    "words": [
                        {
                            "translit": "paym\u01d4dan",
                            "gloss": "to walk, measure",
                            "script": "\u067e\u06cc\u0645\u0648\u062f\u0646"
                        },
                        {
                            "translit": "parh\u00eextan",
                            "gloss": "to avoid",
                            "script": "\u067e\u0631\u0647\u06cc\u062e\u062a\u0646 (\u067e\u0631\u0647\u06cc\u0632)"
                        },
                        {
                            "translit": "p\u00e2d\u00e2\u0161",
                            "gloss": "reward",
                            "script": "\u067e\u0627\u062f\u0627\u0634 (\u067e\u0627\u062f\u0627\u0634\u0646)"
                        },
                        {
                            "translit": "p\u00e2sox",
                            "gloss": "answer",
                            "script": "\u067e\u0627\u0633\u062e"
                        },
                        {
                            "translit": "Pedr\u00e2m",
                            "gloss": "\"pleasant\"",
                            "script": "\u067e\u062f\u0631\u0627\u0645"
                        }
                    ],
                    "script_extra": "\u067e\u06cc\u0645\u0627\u0646\u0647\u060c \u067e\u06cc\u0645\u0627\u0646",
                    "note": null,
                    "quote": {
                        "text": "\u0628\u062f \u0648 \u0646\u06cc\u06a9 \u0631\u0627 \u0647\u0631 \u062f\u0648 \u067e\u0627\u062f\u0627\u0634\u0646 \u0627\u0633\u062a - \u062e\u064f\u0646\u06a9 \u0622\u0646\u06a9 \u062c\u0627\u0646\u0634 \u0627\u0632 \u062e\u0631\u062f \u0631\u0648\u0634\u0646 \u0627\u0633\u062a",
                        "poet": "Asad\u00ee T\u00fbs\u00ee"
                    }
                },
                {
                    "id": 12,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:818",
                    "words": [
                        {
                            "translit": "peret",
                            "gloss": "fight against",
                            "script": null
                        },
                        {
                            "translit": "ni-part",
                            "gloss": "fight down",
                            "script": null,
                            "see": [
                                "N\u00ee 1"
                            ]
                        },
                        {
                            "translit": "\u00e2-part",
                            "gloss": "battle",
                            "script": null,
                            "see": [
                                "Apo"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 12,
                    "lang": "Persian",
                    "refs": "BQT:2115; HRN:230",
                    "words": [
                        {
                            "translit": "nabard",
                            "gloss": "battle",
                            "script": "\u0646\u0628\u0631\u062f"
                        },
                        {
                            "translit": "\u00e2vard",
                            "gloss": "battle",
                            "script": "\u0622\u0648\u0631\u062f (\u0622\u0648\u0631\u062f\u06af\u0627\u0647)"
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        }
    ]
}
```


## [2026-09-14T00:50:09.487Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','HRN','AEF','FSF','MON','ARY','PHD','BRT','KNT','NYB','HUB','CHEUNG','IRN']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700])\n\"",
 "description": "Ref metadata"
}
```


### [2026-09-14T00:50:10.605Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, ver
== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page 
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== CHEUNG null
== IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "/home/sfmqrb/git/rishe/data/verific
```


## [2026-09-14T00:50:15.886Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 50 51 52 53 54 55 56 57; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_03.txt | head -60; done 2>&1 | head -250",
 "description": "Print Pokorny leaves around p.815"
}
```


### [2026-09-14T00:50:16.928Z] TOOL RESULT

```
=== leaf 50 ===
  oder  -kommen,  übersetzen durchdringen,  fliegen^;  poro-s  ,Zugang^,  por-mo-s  , Fähre',  per-fu-s^ por-tu-s  ,Zugang';  nicht  sicher  von  C.  zu  trennen.
Ai.  piparti  ,führt  hinüber,  geleitet,  fördert,  übertrifft^,  Kausat.  pärdyati ,setzt  über^  (=  pälayati  ,schützt^),  av.  par-  (mit  Präfixen)  ,hindurch- hinübergehen',  Kaus.  -pärayeite,  ai.  pära-  ,hinüberbringend,  übersetzend', m.  n.  ,jenseitiges  Ufer,  Ziel,  äußerste  Grenze^  (dazu  pärya-  ,wirksam'), av.  pära-  m.  ,Ufer;  Grenze,  Ende^;
arm.  hord  , begangen,  betreten^,  hordan  ,fortgehen',  hordantam  ,lasse fortgehen',  und  heriun  ,Pfrieme';  thrak.  -Ttögog^  -naga  in  Ortsnamen  = gr.  TtÖQog  ,Furt';  '
gr.  Ttegdcü  , dringe  durch',  tcsiqü)  {rtS7iaQi.ievoq)  , durchdringe,  durchbohre* (=  ksl.  na-perJQ)y  diau-TteQrjg  ,durchbohrend',  Ttegövr]  ,Spitze,  Stachel, Spange';  Ttögog  ,Durchgang,  Zugang,  Übergang,  Furt;  Ausweg;  PI.  Ein- künfte', hom.  TVOQstv  ,verschaffen',  Aor.  enoQOv^  nsTtgayTai  ,ist,  war  vom Schicksal  bestimmt'  {*pf-),  ^ogevio  , führe,  verschaffe',  Med.  ,reise',  nogll^u) , gewähre  Durchgang;  verschaffe',  nogd-^ög  ,Überfahrt,  Meerenge';
alb.  pruva,  prura  , brachte,  führte',  sh-poroj  ,durchbohre,  durchsteche' (dis--^*perä-iö),  sh-poj,  tsh-poj,  sh-puay  ,ds.,  durchbreche  eine  Mauer,  breche ein'  (dis-  +  *pereiö),  sh-pie  ,f ühre  hin'  (*sem-  +  *perö) ;  pirr{e)  f.  ,Dorn' (^-p^r-nä)  usw. ;
lat.  portöj  -äre  ,tragen,  führen,  fahren,  bringen,  darbringen',  umbr.  por- tatu  ,portato',  portust  ,portaverit'  (*poritö,  zu  einem  Iterativ  *poreiö)]
got.  faran,  för  ,wandern,  ziehen',  farjan  ,fahren,  schiffen',  st.  V.  ahd. ags.  faran,  aisl.  fara  ,fahren',  schw.  V.  as.  ferian,  ahd.  ferien,  ferren, äisl. /er/tt  ,fahren,  schiffen'  (Jarjan  =  *poreiö)]  aisl. /or  f.  ,Reise,  Fahrt', ags. /artt  f.  ,Fahrt,  Reise,  Zug',  mhd.  vai  t  ,Fahrt^,  Weg,  Art,  Weise' (fem.  zu  gr.  Ttögog)]  aisl. /armr,  ags./earm  m.  ^Schiffsladung',  ahd. /am ,Nachen'  (=  russ.  porom)-,  dehnstuf.  Kaus.  as.  förian,  ahd.  fuoren,  nhd. führen,  aisl.  fera  ds.,  ags.  (als  Iter.)  feran  ,gehn,  ziehen'  (=  av.  pärdyati, aksl.  pariti)',  ahd. /wom  ,Fuhre,  Fahrt  usw.',  ags. /ör  f.  ,Fahrt,  Wagen';
i
817
aisl.  /^^^'   ;fahrbar^    geeignet^,   ahd.  gi-fuori   ,passend,   bequem^   nützlich'; ^fgi-balabstr.  aisl. /ercT^  Sigs.  ßerd,  ahd.  mhd. ; /ar^  ^Fahrt'  (*por-ti-)',
russ.-ksL  na-'perJ2  (=  rceiQü)),  -perüi  ^durchbohren';  perg,  pirati  , fliegen'; Iter.  pariti  ^fliegen,  schweben'  (=  ai.  pärayati,  germ.  *-förjan)'^  pero  ^Feder'; russ.  poröm,  skr.  präm  ,Fähre'  (=  aisl.  farmr) ;  vermutlich  hierher  auch aksl.  porjq,  prati  ^zerschneiden';  über  nhd.  Farn  usw.  s.  Nachtrag  S.  850.
per-tu-,  por-tu-f  Gen.  pr-teus  ^Durchgang,  Furt':  av.  pdvdtu-s  m.  f. (urar.  *prtü-s)  und  pdsu-s  m.  (urar.  *pftu-s)  ^D
=== leaf 51 ===
urchgang^  Furt,  Brücke' niu-pdrdd-wa-  ,gut  zu  überschreiten'- =  ^Euphrat') ;  lat.  portus,  -üs  ,Haus- türe^(XII  tab.); , Hafen',  angi-portus  ,enge  Fassage,  Nebengäßchen';  daneben ä-St.  porta  , Stadttor,  Tor'  =  osk.  \jp']urtam\  illyr.  ON  Nau-portus]  gall. ritu-  ,Furt'  in  Ritumagus,  Äugustoriturrij  acymr.  ri7,  ucymr.  rhyd,  corn. rit  ,Furt';  ahd.  fürt,  ags.  ford  ,Furt'  (hochstufig  aisl.  fjordr  ,enger  Meer- busen' aus  ^^per-tu-s)]  daneben  f.  i-St.  ira  nhd.  ON  Fürth  (^furti-).
WP.  II  39  f.,  WH.  II  344,  Trautmann  206,  215  f.
C.  pQT-,  pero-  , verkaufen  (eig.  zum  Verkauf  hinüberbringen'),  , hinüber- handeln, zuteilen';  aus  dem  Wert  und  Gegenwert  ira  Handel  auch Wörter  für  ,gleich,  vergleichen,  begleichen';  pr-ti-  ,Lohn'.
a.  Gr.  7t€QV7]f.iL  (Präs.  und  Impf.),  Ttegdco,  -w  (formal  =  neqdü)  , dringe durch'),  e7tsQa(j{a)(x,  und  7tL7tQ&a'/.a)j  negdaa)  (att.  nsgß),  eneQaaa,  7iinQäy.a ,verkaufe',  (gr.  St.  ^^pei-a-),  tcoqvtj  ,meretrix';  air.  ren(d)id  ,verkauft'  (*pr-?i9-: gr.  TiBQva-),  Konj.  3.  Sg.  -ria-  {*riä-  nach  Indik.  *[jp]ri-na-  für  *[p]erä-  ein- getreten), Perf.  3.  Sg.  -rir  {*ri'r-e)'^  Verbalnomen  reicc  (Dat.)  ,Verkaufen' (im  Auslaut  nach  icc  , Heilung,  Bezahlung'  gerichtet) ;  vgl.  mit  einer  alten Gutt.-Erw.  lit.  perkü  pirkti  ,kaufe'.
ß.  Av.  pairyante  ,sie  werden  verglichen',  aipi-par-  ,(seine  Schuld)  be- gleichen, Buße  tun',  a-pdrdti-s  ,Sübne',  pdrdSa-  n.  , Ausgleichung  (einer Schuld),  Sühne,  Strafe',  pära-  m.  ,Schuld'  (dazu  wohl  auch  par-  ,verur- teilen');  lat.  pär  (Dehnstufe),  päris  ,gleichkommend,  gleich.  Paar',  davon paröj  -äre  ,gleichschätzen',  comparare  ,vergleichen'  (umbr.  parsest  ,par  est' hat  das  s  von  mers  est),
y.  Ai.  pürtd-  n.,  pürti-  f.  ,Lohn'  =  lat.  pars,  -tis  ,Teil'  (*p^reti-),  portiö  ^Teil, Anteil'  (nachklass.;  klass.  nur  pro  portiöne,  assim.  aus  *prö  partiöne)]  air. rann,  cymr.  rhan,  mcorn.  ran,  abret.  PL  rannou  ,Teil'  (*perd-sna)]  air. ern{a)id  , gewährt',  Konj.  r-a-cera  ,er  möge  es  gewähren',  Prät.  ro-ir  ,er hat  gewährt'  (*per-e),  Fut.  *ehraid  (*pi-prä-s-e-ti)]  ro-rath  ,ist  gewährt worden'  (*pr9-^o-?);  hitt.  pars-  ,zerbrechen,  zerteilen'.
WP.  II  40  f.,  WH.  II  250  f.,  256  f.,  257  ff.
52
818
D.  per-  ^gebären,  liervorbringen^  (wie/erö  :  ^gebäre^  in  einstiger  Beziehi zu  C.  per-  .zuteilen'),  davon  Worte  für  , Tierjunges' :  pr-tu-ko~^
a.    Lat.    pariö,    -ere,   peperl,    partum,   paritürus   ^gebären',   repen'ö,   .j^ repperi,   repertum   .wiederfinden,    finden,   erfahren^,    partus,    -üs    ,gebärei Geburt;    Leibesfrucht'.   Parca   (*parica)   ursprüngl.   , Geburtsgöttin', pertius  eig.  .der  Frühgeborene'  ==  um
=== leaf 52 ===
br.  Propartie  .Propertii'.  parö, .bereite,    erwerbe,    kaufe',    comparö    .kaufe'    (.sich    etwas    besorgen,   ^i schaffen');  imperäre  .anschaffen  ==  befehlen';
lit.  periiij  pereti  .brüte'.  peraX  Nom.  PL  .Bienenlarven'.
p.   Ai.  -frthuka-   m.   .Rind.   Kalb.   Tierjunges',  arm.   ort\   -u  .Kalb   di Rindes   oder   Hirsches'   (mit   Formans   -thu-);    gr.    TtÖQLg,    nöqza^^    nt .Kalb,  junge  Kuh';   cymr.   erthyl  .abortus';   ahd.  far,  farro,  nhd.  Fa% ags.  fearr,   aisl.  farri   {*farz-)   .Stier',   mit   gramm.  Wechsel   mhd.   v^nt^ nhd.  Färse  junge    Kuh'  (germ.  "^fdrsl,  Gen.   ^fdrsjös)^  zu  ags.   heah-fore engl,  heifer]  ursprüngl.  von  jungen  Tieren,  vgl.  engl,  farrow  .nicht  trächtier* wfries.  fear   ,gelt';    dehnstufig   ags.  /ör.    mnd.    vor  .Schweinchen';    aksl. za-pr^t^k^  .Wind-Ei',   cech.  s-pratek  .früh  geborenes  Kalb',  klr.   vy-portok .Frühgeburt'.
WP.  II  41  f.,  WH.  II  255  f.,  Trautmann  215.
E.  per-  .versuchen,  probieren,  riskieren.  Gefahr'  (=  per-  .hinüberführen durchdringen').  ^
Arm.  p'orj  .Versuch'  (express.  p-) ;   gr.  nelQa  f.  .Erfahrung.  Versuch',  M äol.   neoqa   {*7tSQia),    Ttsigdo),    -atw    .versuche',    ^insL^og   .erfahren,   klug, '^ gewandt';  lat.  experior,  -iri  .versuche,  prüfe',  experimentum  .Versuch.  Prü- ^ fung'.   comperiö,    -Ire   .erfahre   genau',   opperior,   -tri,  -itus   (und  -tus)  sum  ^ .warte,   erwarte',  peritus  .erfahren',  periculum  .Versuch.  Probe;    Gefahr;  7 Prozeß ;  Anklage' ;  das  l  von  peri-tus,  -culum  stammt  aus  den  Kompositis mit  -perior-^  air.  a{i)re  .Wachen.  Aufmerksamkeit',  mv.  faire ^  wegen  gallo- brit.    areänl   PL    .Kundschafter'   aus    *pdreiä]    germ.    *firina-  .das    Außer- gewöhnliche'  in  got.  fairina  f.  .Schuld',  ahd.  firina   .Verbrechen'   usw.; germ.  *fera-  .Gefahr'  in  aisl.  fär  n.  .Gefahr.  Unglück',  ags.  f^r  m..  ahd. fär{a)  .Nachstellung.  Gefahr',  zu  got.  f 67 ja  m.  .Aufpasser',  ahd.fären  .auf- lauern' usw. ;    vielleicht  dazu  mit  Abtönung  gr.  ralal-ncügog  ;geplagt'  als .Gefahren  erduldend'.
WP.  II  28  f..  WH.  II  288  f.   •
3'  P^r-f  Per-g'  .schlagen'.
Arisch  nur   mit  if-Formans:   ai.  pft-,  pftanä  .Kampf.  Streit',  av.  pdrdt-,     ■ pysanä  .Kampf.  Schlacht'.  pdr9tamna  .die  miteinander  Kämpfenden',  vaiti- pai^tata  .bekämpft';
819
arm.  ^i<^^^  ^ich  schlugt  (Aor.  zum  Präs.  Jiarkanem,  s.  u.);  harac  ^vulnus^; ^rot  ;,Doiiner^,  orotam  , donnere';
alb.  fres  ^haue  ab^  nieder;  schneide',  Aor.  'preva,  me  pret  ,es  kümmert 0iich;  ist  mir  angelegen',  pritem  ,werde  geschnitten;  zerkratze  mic
=== leaf 53 ===
h; kümmere  mich  um  etwas';
lat.  premö,  -erej  pressi,  pressum  , drücke',  prelum  ,Presse,  Kelter'  (*pres- lom) ;  Wurzel  pr-em-  (mit  durativem  -em-)  und  pr-es-  wie  gr.  tq^iü)  , zittere  : tQ£co'  {*tresö)  ds.;
lit.  periü,  perti  ,mit  dem  Badequast  schlagen,  jemanden  baden;  schlagen', lett.  perUj  pert  ds. ;  lit.  jpirtiSj  lett.  jplrts  ,Badestube';
aksl.  perqj  ptrati  ,schlagen,  bes.  mit  dem  Bläuel  schlagen,  waschen', skr.  perem,  präti  , waschen' ;  ablaut.  aksl.  phrjq,  *phräti  ,contendere',  sg-ptrjaj n-porz  , Streit',  öech.  pru,  priti  se  ,streiten'  und  aksl.  *phrq,  *perti  in  russ. priL,  prathy  pereth  ,drücken,  drängen',  napoTb  ,Stoß'  usw.,  aruss.  phrth ,Badestube';
perg-:  arm.  harkanem  {pvg-)  ,schlage,  zerhaue  (Holz),  fälle  (Bäume), erschlage,  kämpfe';  air.  orcaid,  mir.  oirggid  ,erschlägt,  tötet,  verwüstet'; mir.  cymr.  orn  ,Morden,  Zerstören'  {^[p']org-no-  od.  -wä);  abret.  treorgam ,perforö',  orgiat  ,caesar'  (=  caesor),  gall.  orge  ,occide',  PN  Orgeto-rlx] anders  über  kelt.  org-  s.  Lewis-Pedersen  387  (zu  hitt.  harganu-  , zerstören* ; vgl.  das  air.  Verbalnomen  orcun  aus  *orgena)]  vielleicht  hierher  ai.  Parjd- nya-  Regen-  und  Gewittergott;  s.  unter  jperk^u-s.
WP.  II  42  f.,  WH.  II  288,  Trautmann  215;  weiter  zu  1.  perg-.
perd-  ,laut  furzen';  prdi-s  ,Fürz'.
Ai.  pdrdate  ,furzt'  (Gramm.),  av.  pdrdöaiti  , furzt';  gr.  TTegdw,  nigdof^av (meist  Med.  wie  im  Ai.)  ds.,  eTiaqdov,  7ie7tOQÖa\  Ttoqdr)  ,Furz';  vielleicht  hier- her nsQÖi^  m.  f.  ,Rebhuhn'  (vom  schwirrenden  Fluge);  alb.  pjerth  ,pedo' (Aor.  pordha),  pordhe  ,Furz'  (*perdä)]  ahd.  ferzan,  ags.  feortarij  aisl. freta  , furzen',  ahd.  firz,  /wrz,  aisl.  fretr  ,Furz';  lit.  perdzUj  persti,  lett. pirdu,  pirst  ds.,  lit.  pirdis  (=  nhd.  ,Furz') ;  sloven.  prd§ti,  russ.  perdäth ,furzen';  cymr.  rhech  ,Furz'  {^rikhä  aus  *prd-kä)'^  für  schallmalenden Ursprung  der  Wz.  spräche  schwed.  dial.  prutta  ,furzen  (bes.  von  Pferden)'.
WP.  II  49,  Trautmann  219 f.;  vgl.  pezd-.
I.  perg-  , Stange,  Stamm'  (ursprüngl.  , abgehauener  Stamm?').
Aisl.  fork?^  m.  , Stange,  Stock';  (ags.  feorcol^  3iS.fercal  , Riegel,  Verschluß' aus  lat.  veruculum) ;
lit.  pergas  ,Fischerkahn'  (*Einbaum);
aksl.  pragz  , Schwell
=== leaf 54 ===
e',  porög-b  ds.,  poln.  prög  ,Schwene,  Haus,  Wohnung', progi  PI.  , Dielen,  Bänke';
62*
820
9
vielleicht    hierher  lat.    pergula    , Vorsprung,  Vorbau    an    einem   Haus©. Vorraum,  Weinlaube'  als  Demin.  eines  ^pergä  , Gebälk'. WP.  II  48,  WH.  II  288;  vgl.  oben  S.  819  Mitte.
2.  perg-  , Furcht,  sich  fürchten'?
Got.  faurhrtei,  Sigs.  fyrhtu  f.  , Furcht*;  got.  faurhts,  ahd.  as.  for(a)hi^
ags.  forht    ,furchtsam';    ahd.    as.  forhta   ,Furcht';    got.  faurhtjan,    ahd.
furhten,  for{a)hten  ,fürchten';   vielleicht  zu  toch.   A  B  'pärsk-,  A  prask-^-
B  präsk-  , fürchten',  A  praski,  B  proskoj  proskye  ,Furcht'  {-sk-  aus  -k-sk^y
WP.  II  48,  Holthausen  Altengl.  etym.  Wb.  112.
1.  perk-,  prek-  ,füllen,  auffüllen'?   Nur  indisch  und  irisch.
Ai.  prndkti  {prücati,  piparkü)  ^füllt,  gibt  reichlich;  mengt,  mischt*/ Partiz.  prkta-  ,gemischt,  erfüllt,  voll  von',  Aor.  apräk]  upala-prak^ii^. ,die  Handmühle  drehend',  sam-pfc  ,in  Berührung  stehend';  pracura-  ,viel,' reichlich';  mir.  ercaim  ,fülle'.
WP.  II  47,  Kuiper  Nasalpräs.  81.
2.  (perk-) :  prk-  ,glühende  Asche,  Kohle'.
Lit.  pirkänys  f.  PI.  , Asche  mit  glühenden  Funken',  lett.  pirkstis,  pirkstes PI.  ds. ;  air.  riches  f.  ,glühende  Kohle',  bret.  regez  ,Kohlenglut'  {^prki-stä^ vgl.  das  lett.  Formans);  unklar  cymr.  rhys-yn,  PL  rJiys-od  ,glühende Asche',  mit  anderem  Formans  acorn.  regihterij  KoUekt.  regyth  ds. ;  ob  als jSprühend'  zu  *sp(h)er-  , streuen,  sprühen'?  vgl.  lett.  spirgsti  , glühende Kohlen  unter  der  Asche'  unter  sp{h)er{e)g-  ,zucken,  sprühen'.
WP.  II  47,  Mühlenbach-Endzelin  III  223.
1.  perk-  , Rippe;  Rippengegend,  Brust'.
Ai.  pdrsu-  f.  jRippe,  gebogenes  Messer',  pärsvd-,  -m  ,Kippengegend, Seite',  av.  par^su-  f.  ,Rippe',  pdi-Qsu-  m.  ,Rippe,  Seite',  osset.  fars  ,Seite, Strich,  Gegend';  aksl.  pr^si  ,Brüste',  f.  PI.  wohl  aus  ,Rippengegend' ;  vgl. lit.  zem.  p\r§ys  f.  PI.  ,Brust  des  Pferdes'.
WP.  II  44  f.,  Trautmann  220.
2.  perk-,    prek-    ,gesprenkelt,    bunt',    oft    zur  Bezeichnung  gesprenkelter,
farbig  getupfter  Tiere;  perko-,  porko-,  perk-no-,  prk-no-  ds. Mit  22-Formantien :    Ai.  pfäni-  ,gefleckt,    bunt',   gr.   rtsQxvög,   ursprüngl. ,7roixtAos',    dann    ,dunkelfleckig,    dunkel,    blauschwarz',    nsQ%alvsi    ,wird dunkel';  ngaTivöv'  ^leXava  Hes. ;   TIqöuvtj  ,die  Schwalbe';  ohne  -n-  mir.  erc
821
crefleckt,  dunkelrot',  auch  , Lachs,  Forelle,  Kuh,  Eidechse',  cymr.  erch  ,ge- fleckt'  (==  n£Qy(.og)',  ahd.  forhana,  mhd.  forhe(n),  forhel 
=== leaf 55 ===
 ,Forelle',  as. fiirnia,  ags.  forn(e)  ds.  (*pr]c-nä)j  ablaut.  schwed.  färna  ,Weißfisch* (^perk-nä) ;
mit  -uo:  ahd. /aro,  mhd.  vare,  flekt.  varit-er  , farbig',  substantiviert  ahd. farawa  , Farbe'  {*pork'u6-)]  lat.-germ. /arzö  ,Lachsforelle'  (germ.  *farhjön-^ älter  *farhwjön-)-
andere  Bildungen:  gr.  nsoxog  m.  , Sperber'  (Aristot.),  nsQ-KÖ-Ttrsgog  ,weiß- köpfige  Geierart',  Tteoxd^eL  ,wird  dunkel,  schwarz';  Ttgö^,  -KÖg  f.  und ^QOTidgj  -ddog  ,Hirschkalb',  TtQcb^j  -y,ög  , Tautropfen' ;  neQy.7]  (lat.  perca  Lw.) , Barsch',  lat.  porcus  ,ein  Fisch  mit  Stachelflossen',  ligur.  FIN  Porco-bera (,Forellen  führend');  mir.  orc  (und  erc,  s.  oben)  , Lachs' ;  aisl.  fjgrsimgi' ,trachinus  draco'  (*perks-nkö-)  ]  redupl.  vielleicht  Ttartga^  ein  thrak.  See- fisch GForelle?');
vielleicht  hierher  durch  Diss.  eines  *perk-ro-s  zu  *pelcro-j  *polcrO':  lat. pulc{h)ery  alat.  polcher  , schön'  (=  ,bunt').
WP.  II  45  f.,  WH.  II  384;  Erweiterung  von  1.  per-.
5.  perk-,  prk-  ,auf reißen,  aufwühlen,  aufkratzen':  , Furche,  und  die  daneben aufgewühlte  Erde';  p^kä  , Furche'.
Ai.  pdHäna-  m.  ,Kluft,  Abgrund,  Einsenkung*;
lat.  porca  , Furche  im  Acker',  , Wasserabzugsrinne  im  Acker'  (porcu- letum  , Ackerbeet'  mars.  umbr.  jporculeta^)  ]  cymr.  rhych  ,Furche'  (mit expressivem  -kk)  vielleicht  =  bret.-rec'Ä  , Kummer*,  dagegen  mit  k  abret. 7'ec,  gl.  ,sulco',  ro-ricse[n]ti  ,sulcavissent' ;  gall.  rica  ,Furche*,  frz.  raie , Streifen';  Sihd.  furuh,  sigs.  furJi  f.  ,Furche',  aisl. /or  f.  , Abzugsgraben, Kanal'  (*p2'k-)j  hochstufig  norw. /ere  m.  , Ackerbeet';  nach  F.  R.  Schröder, Festgabe  K.  Helm  25  ff.  hierher  aisl.  Fjgrgyn  f.  als  , Göttin  der  Acker- furche';
lit.  pra-persis  , Blanke  im  Eis',  pra-par§as  , Graben',  peHeti  ,brennend schmerzen'  (von  Wunden) ;
dazu  *porkös  , Schwein'  (, Wühler').
WP.  II  46,  47,  WH.  II  340  f.
4.  perk-,  prek-,  prk-  ,f ragen,  bitten';  prk-skä-  ,Frage'.
1.  s£o-Präs.  *prk-sköj  woraus  *prskö :  Sii.  prcchdti  ^ira.gt\  av.  pdresaiti , fragt,  begehrt'  (Partiz.  parHa-\  ap.  aparsam  ,ich  frug';  arm.  e-harc  ,er hat  gefragt'  (:  ai.  d-pxcchat\  davon  das  Präs.  harcanem]  lat.  poscö  , fordere, verlange,  er  bitte';  ir.  arco  ,ich  bitte',  cymr.  arcTiaf,  corn.  arghaf  ds., mbret.  archas  ,il  commanda'  (air.  imm-chom-arc  ,gegenseitiges  Fragen, Begrüßen'  usw.)  mit  ar  aus  f  vor  dem  s  der  Grundf.  *prskö  (aus  *pxk-skö)',
822  f
lit.  per^Ä,  pirUi  ,für  jemanden  freien*  {pirslys  ^Freiwerber*),  wenn  mit analogischem  Präs.-Ablaut  e  statt  i;  dazu  a.1  prcchä  »Frage,  Erkundigung* =  arm.  harc  ds. ;  ahd.forsca  »Forschung,  Frage*  ist  Postverbale  znforscön »fragen,  forschen*;  lat.  postulö  ,fordere*  (Deminutiv  vom  Fartiz.  *posctoi zu  poscö))  im  Osk.-Ümbr.  ist  *porscö  zu  *perscö  umgebildet:  umbr.  per«- nivm  Imper.  Med.  ,precätorS  dazu  mit  (Formans  -(e)Zo-)  umbr.  persklu^ pesklu  ,supplicätiöneS  ferner  mars.  pesco  ,sacrificu
=== leaf 56 ===
mS  und  vom  Partiz. *pes[c]to-  aus:  osk.  pestlürriy  peeslüm  ,templum*,  woraus  messap.  nevayX^ , Bethaus*.
2.  Ai.  präS'  , (gerichtliche)  Befragung*,  av.  frasä  f.  ,Frage*,  ai.  prstha- (=  av.  parUa-)  ,Gerichtsf rage*,  prasnä-,  av.  frasna-  m.  ,Befragung,  Frage* (=  ahd. /ra^an  , Specht^  KZ  62,  31,  2),  arm.  harsn  ,Braut,  Neuvermählte, Schwiegertochter*  (vgl.  got.  fraihnan) ;  lat.  procus  ,Freier',  prex  f.  ,Bitte', precoTy  -äri  »bitten*,  umbr.  pepurkurent  3.  PL  Fut.  ,poposcerint* ;  got. fraihnan  ,f ragen*,  aisl.  fregna,  ags.  frignan  (und  to-Präs./ricnaw)  ds.,  as. Prät.  fragn]  ags.  friccea  ,Herold*;  germ.  *frehii-  in  aisl.  frUt  f.  Frage, Erforschung*,  ags.  frtht  f.  , Wahrsagung* ;  ahd.  fräga  ,Frage*  i^fräg-on^ -en,  frohen  ,fragen*),  aisl.  frägr,  ags.  gefrcege,  as.  gifrägi  ,berühmt*; ablaut.  ahd.  fergön  ,bitten* ;  aisl.  prositi,  bitten ;  lit.  Iterat.  praSaü^  -yti »fordern,  bitten*;  toch.  A  prak-j  B  prek-  , fragen*.
WP.  II  44,  WH.  II  346  f.
perk"u-s  , Eiche*,  daraus  vielleicht  , Stärke,  Kraft,  Leben,  Weltenbaum'  und ,Baum  des  Donnergottes  Perknuno-s'. Ai.  parkatl-  ,heiliger  Feigenbaum*,  nind.  pargäi  , Steineiche* ;  ven.  VN Quarqueni  , Eichenmänner*  (lat.  Relikt?);  NympMs  Percernibus  vielleicht  "^  " ligurisch  (Yaucluse);  lat.  quercus  f.  ,Eiche';  ital.-trent.  porca  ,Föhre* (rät.  *porca)]  kelt.  Hercynia  Silva  ,das  deutsche  Mittelgebirge*  (aus  *Per- kunia,  älter  *Perk'i^unia)j  cymr.  perth  L  ,Busch,  Hecke*  (*k^erkl/^-t-  ?) ;  kelt. VN  Querquerni  (goidel.)  in  Hispania  Tarrac. ;  aus  *Perkuniä  wohl  entlehnt germ.  *ferguniö,  ahd.  Fergunna  , Erzgebirge*,  mhd.  Virgunt  f.  _, Waldgebirge westlich  Böhmens*,  got.  fairguni  n.  , Gebirge*,  Sigs.firgen  ,Waldhöhe';  ahd. fereheihj  langoh.  f er eha  ,Speiseeiche*,  aisl.  ^'prr  m.  , Baum,  Mann*;  ablaut. ahd.  forha  ,Kiefer*,  ags. /wrÄ;  aisl. /wra  f.  »Föhre*, /^ri  n.  ,Föhrenwald*; aus  ahd.  *forh-ist  »Föhrenwald*  :  nhd.  Forst;  aus  ahd.  kien-forha  (kien- zu  ags.  cen  »Kienfackel*,  ablaut.  zu  ags.  cinan,  oben  S.  355)  wird  nhd. Kiefer;  unsicher  ob  nach  Vendryes  RC  44,  313 ff.  hierher  auch  got.  fairhus ,Welt*,  ags.  feorhy  ahd.  ferah  ,Leben*,  westgerm.  Alaferhuiae  (=  *Ala- ferhwiös),  zu  aisl.  flrär  {*firhw-jöR),  ags.  firas  PI.  ,Männer*  usw. ;  alit. perkünas  Donnergott,  lit.  perkünas  , Donner*,  perkünija  f.  , Gewitter*,  lett. p^rkuons   ,Donner,    Donnergott*,    apr.    percunis    , Donner';    aruss.    Perum

=== leaf 57 ===
823
Donnergott',  russ.  perün  ,Donnerkeil,  Blitz*  sind  volksetymol.  nach  slav. *perö  , schlage'  umgestaltet;  unklar  ist  ai.  Parjdnya-  , Gewittergott'  (s.  oben unter  3.  per-,  perg-).
WP.  II  42  f.,  47  f.,  WH.  II  402  f.,  Specht  KZ.  64,  10  f.,  68,  193 ff., Thieme,  Untersuchungen  zur  Wortkunde  des  Rigveda  71.
perS'  ^sprühen,  stieben,  spritzen  (bespritzt  =  gesprenkelt),  prusten^ ;  prso-s , Staub,  Asche'.
Ai.  pfsat,  pj-satd-m  n.  ,Tropfen';  pfsant-^  L  pfsa^l , gesprenkelt,  scheckig, bunt',  prsati  , scheckige  Kuh,  gefleckte  Antilope^;  av.  parhiya-  ,vom Wasser',  n.,  vielleicht  , Schneewasser' ;  aisl.  fors^  foss  m.  ,Wasserfall' ;
lit.  purslaSj  pursla  , Schaumspeichel',  pufkUi  ,wie  eine  Katze  prusten, schnarchen';  lett.  ^örsZa  , Flocke'  (von  Schnee,  Asche,  Wolle)  ablaut.  p^rsla ds. ;  (vgl.  lett.  sjpurslät  , prusten');  slav.  *parsa-  m.  ,Staub'  >  *porcJn  in aksl.  pi-achz  ds. ;  slav.  ptrsth  in  aksl.  prbstb  „^oUg",  (*p,rs-),  neben  sloven. prh  m.  ,Staub,  Asche'  (=  aisl.  fors),  pr^hati  ,streuen,  stieben',  öech.  prseti ds.  usw.;  toch.  AB  pars-  ,besprengen' ;  Partiz.  Akt.  papärs,  hit.  papparS- ,spritzen,  sprengen'.
WP.  II  50;  Trautmann  206  f.,  Erweiterung  von  1.  per-  ,spirühen'.
■persnä,  -sni-,  -sno-  , Ferse'.
Ai.  pärsni-  t,  av.  päSna-  n.  , Ferse';  gr.  rttegvi]  f.;  lat.  perna  f.  {^persnd) ,Hinterkeule,  Schweineschinken,  Schenkel,  Bein',  pernls  , schnell'  (mit  der Ferse);  got.  fairsna,  a.s.  f er sna,  ahd.fersana  , Ferse'  {*persna)j  Sigs.fiersin f.  ds.  (*persni-)]  hitt.  parsina  (leg.  parsna)  , Oberschenkel,  Lende',  par§- (a)näi-  ,hocken'  (auf  den  Oberschenkeln).
WP.  II  50  f.,  WH.  II  289  f.,  Pedersen  Hitt.  258.
pertb-  jStange,  Schößling'?
Arm.  ort""  (o-St.)  ,Weinstock,  Rebe';  gr.  TCtood-oq  m.  ,Schößling'  (vgl. -rtTÖlsfiog  :  rtöXefxog  usw.);  vielleicht  lat.  pertica  , Stange',  falls  nicht  aus per-ti-ca  zu  osk.  jpert  ,bis  zu'  aus  *jper-tij  also  ursprüngl.  ,Querholz';  vgl. cech.  jpHska  ds.,  S.  810.
WP.  II  49,  WH.  II  292  f.
I.  pes-  ,blasen,  wehen'  (s.  auch  2.  pes-  ,Staub,  Sand').
Aisl.  fQnn  f.  ,Schneewehe,  Schneehaufe'  (*faznö),  -fenni  n.  ds. ;  als  ,im  Win- de wehender  Faden':  ah d. /aso  m.,fasa  f.  ^Faser,  Franse,  Saum',  sgs.fces(ri) n.  ,Franse',  engl,  feaze  ,Fasern';  aisl.  fqsull  m.  ,B^iid',  mnd.  vese{n),  Spreu, Faser,  Franse',  ndl.  vezel  ,Faden',  ahd.  fesa  ,Spreu,  Spelze',  nhd.  Fehse, dän.  ßcBser^  älter  f{j)es  ,Fasern',  ahd.  fasön  ^untersuchen'  (*zerfasern) ;
824
aksl.  'p^chyrh  ,bulla,  Blase',  'pachati  ,ventilare,  agitare',  russ.  pacÄnui^,
```


## [2026-09-14T00:50:26.700Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 45 46 47 48 49; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_03.txt; done 2>&1 | head -120",
 "description": "Pokorny leaves 45-49 (pp ~810-815)"
}
```


### [2026-09-14T00:50:27.779Z] TOOL RESULT

```
=== leaf 45 ===
mel)',  paru§-  n.  ^Knoten, Gelenk,  Glied' ;  gr.  TtsiQag  , Knoten^  ist  unsicber  (G.  Björck  Mel.  Boisacq 1,  143  ff.).
b.  Adj.  pero-s  , ferner':  ai.  pdra-h  ,ferner,  jenseitig,  Feind;  früber; später',  Superl.  paramd-h  ,fernster,  letzter,  bester',  av.  ap.  para-  ,ulterior, der  andere,  spätere,  künftige',  jpara-iara-  ,Feind';  ai.^rt?*«^  (Nom.  Sg.  m.  mit adv.  Endbetonung)  Präp.  m.  Akk.  ,über : —  binaus',  mit  Abi.  ,fern  von',  mit Instr.  ,jenseits  von',  selten  adverbal  =  av.  parö  Präp.  m.  Akk.  ,außer  — abgesehen  von';  ai.  pdräj  av.  para  (Instr.  Sg.)  adverbal  ,fort,  weg,  zur Seite';  ai.  pari  (Lok.  Sg.)  ,darauf,  fernerbin';  ai.  param  (Nom.  Akk.  Sg. u.  =  osk.  perum)  , binaus  über,  jenseits,  nach',  Präp.  mit  Abi.;
arm.  Jiei-i  ,entfernt,  fern';
gr.  7t£Qa(v),  ion.  7t€Qr]v  (Akk.  Sg.  f.)  , darüber  binaus,  jenseits',  Adv., Präp.  m.  Abi.  (Gen.);  lat.  per-peram  , verkehrt',  per-perus  , falsch',  woraus gr.  TtegrrsQog  ,Geck';  gr.  negä  , darüber  binaus,  jenseits'  (Instr.  Sg.  f.  vom St.  *pero-  =^  ai.  pdrä  ,weg,  fort^) ;  davon  uegaZog  ,jenseitig'  (itegalTegog), Tcegad-ev  ,von  jenseits  her',  tfi  Ttsgariß  (yfj)  ,gegen  Westen' ;
aus  einer  schwundstufigen  Nebenform  von  nsga  durch  -Jco-  erweitert  ist delph.  TcgäY.og  ,mit  e.  Geldstrafe  belegt',  ion.  Tigrjaaoj  att.  ng&TTO)  , durch- fahre, vollstrecke,  vollführe,  verrichte,  tue' ;
osk.  perum  (=  ai.  param)  ,sine';
air.  ¥re  ,weiter,  länger'  (^perio-,  das  l  nach  s'ir  ,lang') ;
bitt.  parä  (=  gr.  rtega)  ,vorwärts,  weiter,  ferner^,  Postpos.  ,aus  —  heraus'; periia{n)  , darüber  hinaus',  Postpos.  , über  —  hinaus', ^«rra72c?a  ds.  (*=  gr. negav  +  -de).
c.  prai,  perai  (Richtungsdativ  des  St.  per),  auch  prei,  priy  pe^i. Ai.  parB  ,daraufhin'  (Lok.  Sg.) ;
gr.   Tvagai    ,7vagd\    außerhalb    des   bom.    (ion.  att.)    nur   in   Kompositis,
812
•  .^
wie  kyren.  HagaL-ßara]   ttqlv  (bom.   auch  Ttgtr)   .vorher;  vor^;  wohl  um-^ gebildet   aus  *fCQlg   {"^pri-is,    zu   lat.  prior,  prlscus)    vgl.    kret.    ngetv  aus  _^
^Ttgeig ;
alb.  pa  ,bevorS  wenn  aus  *par{-  (im  Vokal  nach  pare  .erster^  umgebildet?);
lat.  prae  Präf.  ,voran,  voraus,  überaus',  Präp.  ,vor,  wegen^  osk.  prat, prae-,  umbr.  pre  ,prae',  Präf.  und  Präp.,  pre-pa  ,priusquam^  Kompar.  lat, praeter    ,vorbei    an   =   außer,    ausgenommen'   {*prai-tero-),    umbr.    pretra
,priöres' ;
alat.  prl  (*prei)  ,prae'  {prehendö  ,ergreife*  aus  *praehendö),  Kompar. *pri-iös,  *pri-is  (woraus  ^rls)  in  prior  ,der  frühere',  prlmus  (aus  *pr-is~7nos\  * päl.  prismu  ,prima',  vermutlich  auch  prldem  ,vor  längerer  Zeit,  längst'; pris-cus  .altertümlich'  i^preis-lzo-,  vgl.  arm.  erec,  Gen.  ericu  ,Ältester,  Priester', *preis-]cu) ;  pristinus  ,vorig,  vormalig,  alt',  pälign.  pn-trom-e  ,prötinus',  prl s^a/aZacmcc  ,*praes
=== leaf 46 ===
tibulätrix' ;  hierher  wohl  auch  lat.  jprwws  {*prei-uo8)  ,für sich  bestehend,  einzeln;  eigentümlich;  einer  Sache  beraubt',  prlvö,  äre  ,einer Sache  berauben',  prlvätus  , beraubt;  jemandem  als  Sondereigentum  gehö- rig', umbr.  prever  ,singulis',  preve  ,singuläriter',  osk.  preiuatud  Abi. ,privätö,  reo';
PcTi-  =  kelt.  [p'lari-  in  gall.  ai^e-  [Are-morica,  Are-brigium,  abrit.  Are- clütä  usw.)  ,bei,  vor,  bes.  östlich  von'  (vgl.  ir.  an-air  ,von  Osten^);
ahd.  as.  furi  ,vor,  für,  vorbei',  aisl.  fyr  (und  mit  Komparativendung fyrir)  ,vor,  für';  Kompar.  ahd.  furiro  ,der  frühere,  vordere'.  Superl. furist,  mhd.  vürst  ,erster,  vornehmster',  3ls.  furisty  ags.  fyr (e) st,  engl.ßrst, aisl.  fy7'r  adv.  , früher,  vorher',  fyrri  ,der  frühere',  fyrstr  ,der  erste',  ags. fyrsta,  as.  ahd.  furisto  ,Fürst';  got.  fri-sahts  ,Bild,  Beispiel,  Rätsel'  ent- hält schwundstufiges  *pin-,  wie  auch  ahd.  fri-liez  ziehen  fir-,  fai^-^fra-liez.
prei-  in  \h.  prie,  zem.  pry  ,bei,  an',  Nominalpräf.  prie-,  prie-,  prie-,  pi^- (auch  prei-kälas  m.  .Amboß),  Präverb  pri- ;  Präpos.  prie^  ,gegen',  pries ,vov^]  lett.  prie{k)8a  ,das  Vordere' (*preiiiä) ;  lett.  ^zere  , Stirn.  Vorderseite' (*^nere?);  apr.  prei  .zu.  bei',  als  Präf.  ,auch,  vor,  an',  preisiks  m.  ,Feind'; aksl.  pri  Präp.  und  Präf.  ,bei,  an,  zu';
aus  einem  dem  lat.  pri[s]mus  ähnlichem  '^prisjni-,  -ei:  air.  rem-  Präf. (lenierend)  ,vor,  voran'  {rlam  ,vor  ihm',  remi  .vor  ihr'),  remi-  als  Präverb, Präpos.  re  (nas.).
d.  Peres,  peros  (und  als  1.  Kompositionsglied  pres-  ,vor'.  Gen.- Abi. des  St.  per-) :
Ai.  puräk  Adv.  und  Präf.  .voran,  vorn'.  Präp.  .vor',  av.  parö  Adv. .vorn,  vor',  Präp.  ,vor',  gr.  ndcgog  Adv.  ,f ruber ;  voran,  vorn'.  Präp.  .vor'; prcs-  in  gr.  ngea-ßvg,  -yvg  .alt'  (,*im  Alter  vorangehend',  vgl.  ai.  purö- gavd'  .Führer'  (*Leitstier),  s.  unter  g^ou-  .Rind';  zu  kret.  itgeTayog  s.  oben);
813
^liS-ffist  m.  n.,  as.  frist  n.^  Sigs.ßrst  m.  ,Frist^  aus  *pres-sti-,  a,is\,  fr  est  n. eis.  lins'^pres-sto-j  vgl.  3i\.  pur  ah- sthita-  ^bevorstehend^ ;  aus  ^p^ros-stäti-s  ,im Alter  voran  seiend'^  wohl  air.  arsaid,  arsid  ,vetus^  (ai.  purdstät  ^yov,  voran^ vorn,  vorher'  ist  freilich  purah  +  Abl.-^J^).
e.  pr-  ^hervor^,  etwa  Nom.  Sg.  n.  des  St.  ^e?'- :  gr.  tt«^  in  Eigennamen ^vie  TlaQ'f-iBVLO'AOq,  in  el.  icaQ-ßaiva)  u.  dgl.,  /rao  Tor  vöfxov  u.  dgl,;  lat. por-tendö    (:  got.  faura^janjan),    -rigö,  pol-liceor    u.  a.,    umbr.   pur-douitu
porricito^,  falisk.  por-ded  ^brachte  dar,  widmete';  got.  faür,  as.  for,  für präp.  ,vor,  ^ür'^  ags.  for  ds.,  aisl.  for-  ,yoy%  mit  steigender  Bed.  aisl. for-ljötr  ,sehr  häßlich',  ags.  for-manig  ,gar  viele,  allzu  viele';
germ.  Ableitungen :  aisl.  forr  , hastig,  voreilig'  (*furha-,  vgl.  von  *pro : <rr.  Ttgö-aa  unten  S.  815);  as.  dlvies.  forth,  ford,  ag
=== leaf 47 ===
s.  for d  ,fort,  vorwärts' ; mild,  vort  ^vorwärts,  weiter,  fort',  norw.  fort  , schnell,  bald',  3iis\.  forda,  ags. ge-forpian  , fortbringen' ;  Kompar.  *furpera-  in  a.s.  furpor,  für dor  Adv., ags.  furdor  Adv.  ,weiter',  furdra  Adj.  , größer,  höher',  ahd.  furdir,  -ar Adv.  Adj.  ,vorder,  vorzüglicher,  früher,  vormalig'.
Komposita  mit  Formen  von  stä-  ,stehen'  in  ai.  pv-stA-  f.  ,Rippe',  pf-sthä-m ,hervorstehender  Rücken,  Gipfel',  av.  par-Ua-  m.  , Rücken',  ^ar-s^i-  f.  (Du.) , Rücken',  mnd.  vorst-  f.  , Dachfirst'  aus  *for-stö,  a.gs.  fyrst  ds.  aus  *fur-sti-'^ daneben  mit  hochstuf.  Präfix  ahd.  first  m.,  ags.  fierst  f.  ,First'  aus  *ßr-sti- : wahrscheinlich  ebenso  lat.  postis  , Pfosten,  Türpfosten'  (*por-sti-s  ,hervor- stehendes');  gr.  naardg  (neben  naqaatdg)  ,Pfosten,  Pfeiler,  Türpfeiler', TtaoTcideq'  äfiTtsloi  Hes.  {*7taq-aTag),  lit.  pirHas,  aksl.  pr^si^  ,Finger' (,hervorstehend') ;
f.  perä  Instr.  Sg.  des  St.  *per:  ai.  purä  Adv.  ,vormals,  früher;  ehe, bevor',  Präp.  ,(zum  Schutze)  vor,  ohne,  außer',  av.  para,  ap.  parä  Adv. ,zuvor',  Präp.  ,vor',  davon  ai.  puränd-  ,vormalig,  früher,  alt',  ap.  paranam Adv.  ,vormals';  gr.  Ttagd,  Ttdga  Verbalpräf.  ,vor  —  hin,  dar-',  Präp.  ,an etwas  hin,  entlang,  neben;  während';  ,bei,  aus  der  Nähe  weg,  von  Seiten'; got.  faüra,  ahd.  as.  foi-a  Adv.  ,vorn,  vorher',  Verbalpräf.  ,vorher,  voraus, vor',  Präp.  ,vor',  ags.  fore  Präp.  ,vor'.
g.  pro,  pro  , vorwärts,  vorn,  voran',  Bildung  wie  *apo,  *upo]  pro  mit Auslauts  dehnun  g .
Ai.  prd-  Präf.  ,vor,  vorwärts,  fort'  (vor  Subst.  und  Verben),  ,sehr'  (vor Adj.),  2,Y.  frä,  fra-,  2i^.  fra-  Präf.  ,vorwärts,  voran;  fort,  weg';  gr.  ttqö Präverb  ,vor',  Präp.  ,vor',  TCQw-neqvoi  (rhythm.  Dehnung)  ,im  vorvorigen Jahr';  lat.  pro-,  pro-  in  Kompositis,  pro  Präp.  ,vor,  für';  prönus  ,vorwärts geneigt'  (von  *pröne,  vgl.  pöne  ,hinten'  aus  *post-ne)]  üher  prödest  s.  WH. II  365 ;  osk.-umbr.  Präverb,  pro-,  pru- ;
814
air-  ro-,  cymr.  ry-,  abret.  rf»-,  ru-,  mbret.  nbret.  ra-,  Präverb  und  \^:\ tensivpräfix,  z.  B.  air.  vo-mdr  ,zu  groß^  gall.  GN  f.  Ro-smerta;
got.  /ra-,  ahd.  /r-,  nhd.  ver-  Präverb  (letztere  z.  T.  auch  ==  got.  fair. ' s.  oben  A.);
apr.  pra,  pro  ,durch^,  als  Präverb  ,ver-',  lit.  pra,  pro  ,vorbei^  als  Prä, verb  ,vorbei-,  durch-,  ver-^  vgl.  prä-garas  , Vielfraß'  =  lett.  pra-garis  ds.;S^ lett.  prud-jäm  ,weg,  fort' ;  aksl.  Präverb  pro-  ,durch-,    ver-',  Präpos.  russ. öech.  pro  ,wegen',  ablaut.  russ.  prd-däd,  serb.  prä-djed  ,Urgroßvater' ;
gedoppelt:  ai.  prd
=== leaf 48 ===
pra,  gr.  ttqöttqo  ,immer  vorwärts'.
pru-  (Reim  auf  *pW;  s.  *apo?)  liegt  zugrunde  in  gr.  öia-TVQv-aiög  ,durch.^ gehend',  Ttgv^vög  ,das  äußerste  Ende  von  etwa  bildend'  {fiQvuvr]  , Hinter- schiff' usw.).
pro-  ,früh,  morgens'  in  ai.  prä-tdr  ,früh,  morgens',  gr.  ngwi  (att.  nq(^) ,früh,  morgens',  ngmog  ,morgendlich',  dor.  nqoyäv,  nq&v  {*nQ(joäv),  att. 7tQ(^riv  [*n:Q(jüJ^Lav  seil,  -fj^gav)  ,kürzlich,  vorgestern',  ahä.fruo  ,in  der  Frühe', fruoi,  mhd.  vrüeje  (=  Ttgtülog)  Adj.  ,früh'  (idg.  *prö);  lit.  pro  ,vorbei', slav.  pra-  s.  oben.
Ableitungen  von  pro-:
prO'tero-  in  ai.  pratardm,  -am  Adv.  ,weiter,  künftig',  av.  fratara-  ,der vordere,  frühere',  gr.  Ttgövegog  ,der  vordere,  vorige';  osk.  pruter  pan ,priusquam'  ist  einzelsprachlich  zu  *prö-  gebildet,  ebenso  ai.  prätdr  ,früh, morgens'  s.  oben;
dazu  mit  Superlativsuffix  -temo-:  ai.  pratamäm  ,vorzugsweise',  av. fratdma-,  ap.  fratama-  ,der  vorderste,  vornehmste,  erste'  (daneben  ai. prathamd-  , erster'  und  einzelne  iran.  Formen  mit  th) ;  gr.  ^ngö-atog  (aus TTQÖzaTog?)  vielleicht  in  dor.  Ttgazog  , erster';  aber  gr.  TtgOJrog  ds.  aus *pf-to-  (umgebildet  aus  *pf-mo-  ds.);  dazu  rrgrjrrjv  m.  ,einjähriges  Lamm' (s.  oben  S.  314) ;
pro-zno- :  gr.  rrgöfiog  , Vorderster,  Vorkämpfer,  Führer',  umbr.  promom Adv.  ,prlmum',  got.  fram  Adv.  , weiter',  Präp.  ,von  —  her',  aisl.  fram  Adv. , vorwärts',  fra  (*fram)  Präp.  ,weg  von',  ahd.  fram  Adv.  ,vorwärts,  fort, weiter,  sogleich',  Präp.  ,fort  von,  von  —  her',  Sigs.  from  Adv.  , fort',  Präp. ,weg  von';  aisl.  framr  ,voranstehend,  vorwärtsstrebend,  ausgezeichnet', ags. /?'am  ,tüchtig  keck';
pTc-znO'  in  gr.  jigd^og  ,Führer'  (eher  korrupt  für  Ttgöfxog  ds.?),  got. fruma  ,erster'  (Su^.frumists),  mhd./rww,  vrom  ,tüchtig,  brav'  (nhd.  fromm] ahd.  as.  fruma  f.  Nutzen',  nhd.  Frommen) ;  ähnlich  lat.  probus  ,gut,  tüchtig, brav',  umbr.  profe  ,probe'  aus  *pro-bhuo-s  :  ai.  pra-bhü-  ,hervorragend  an Macht  und   Fülle',  sowie  in  abg.  pro-st^  ,rechtscha£fen,  einfach,  schlicht',
815
und  (aus  *pf-mo-)  as.  formo,  SLgs.  forma  .erster'  (Superl.  fyrmest),  lit. pirTuas  apr.  pirmas  .erster',  wahrscheinlich  lat.  prandium  .Frühmahlzeit' aus  *präm-ediom  (*pfm-).
prü-ko-  .voran  seiend' :  gT.  itgöy-a  (Nom.  Akk.  PL  n.)  Adv.  .sofort',  lat. reci-procus  eig.  .rückwärts  und  vorwärts  gerichtet',  alat.  procum  Gen.  PL. procerum'.  nach  pauperes  umgebildet  zu  proceres,-um  .die  Vornehmsten;  die aus  der  Wand  herausragenden  Balkenköpfe';  procul  .fern'  (vgl.  simul)-^
lat.  prope  .nahe  bei'.  Superl.  proximus,  eigeutl.  *pro-h'^.e  .und  vorwärts (an  etwas  heran)',  mit  Assimil.  p  —  k^  im  p — p;  dazu  propier  .daneben' (*propiter)  und  propinquus  .benachbart,  verwandt'  (vgl.  ai.  praty-dnd-  .zu- o-e wandt');  vgl.  oben  S.  813  germ.  *furha)
aksl.  prok^  .ü
=== leaf 49 ===
brig',  pro^e  Adv.  .^oi/roV.  igitur^  {^prokiom) ;
auf  ein  *prö-ko-  geht  zurück  bret.  a-raok  ,vorwärts.  voran,  früher', cjmr.  (y)rhawg  ,auf  lange',  mit  Proklisenkürzung:  bret.  7^ak,  corn.  rag, cymr.  rhag  .vor'.
pro-uo-:  in  ai.  pravanä-  .(vorwärts)  geneigt,  abschüssig',  n.  .Abhang. Halde';  über  lat.  prönus  s.  oben;  gr.  TTQßvrig^  hom.  TCQT]vrjg  .vorwärts  ge- neigt' nach  Leumann  Homer.  Wörter  77  f.  aus  *TiQO-avrjg  .Gesicht  voraus'; mit  anderer  Bedeutung  ahd. /rö.  sls.  frao,  ags.  /rea  .Herr'  {*frawan-), got.  frauja  .Herr'  (aisl.  Freyr  GN  zum  o-St.  geworden),  as.  fröio  ds.. a.is\.  fr eyja  .Herrin;  Name  der  Göttin',  'dhä.  frouiua  .Frau';  daneben  as. früaj  mnd.  früwe  .Frau'  aus  *fröwön,  idg  *prö-uo-,  das  auch  in  att.  frQ(öQa (lat.  Lw.  pröra)  .Schiffsvorderteil'  (ngcüJ^aiga-,  -(^Qk^  idg.  ^pröu-fia) ;  viel- leicht lat.  prövinciaj  wenn  auf  einem  *pröuiön  .Herr.  Herrschaft'  beruhend; abg.  prav^  .recht,  richtig'  (.*gradaus');
mit  demselben  Formans,  aber  wie  lit.  pir-mas  .erster'  von  *per9-  .ge- bildet', idg.  pcr9-uo-  in :  ai.  purva-,  av.  paurva-,  pourva-,  ap.  paruva-  .der vordere,  frühere'  (ai.  pürvyd-,  av.  paouruya-  paoirya-,  ap.  paruviya  .prior', dann  .primus').  alb.  pare  .erster',  para  .vor';  aksL  pr^v^  prbü^  .der  erste'; wohl  auch  die  Grundlage  von  2igs.  foricost,  forwest  .der  erste'.
h.  pretiy  proti  .gegenüber,  entgegen,  gegen',  z.  T.  im  Sinne  des  Ent- gelts ;  preti-os  .gleichwertig  an'.
Ai.  prdti  (im  Iran,  durch  paiti  verdrängt)  Präf.  ,gegen,  zurück  usw.' Präp.  ,gegen'  usw.;  gr.  hom.  ttqotL  (kret.  tcoqtL  umgestellt),  ion.  att.  lesb. iTQÖq  (vgl.  7tQÖa(a)a)  ,vorwärs'  aus  *jprotiö^  7Tq6o-!^E{v)  ,von  vorn'),  pamphyl. neQxl  (umgestellt  aus  '^TtQeTi)^  äol.  Tcqeg,  Adv.  ,noch  dazu,  überdies',  Präf.^ Präp.  ,gegen — hin,  zu,  gegen',  ,an',  ,nach  einem  Bereich  hin;  bei  (in Schwüren)',  ,von  —  her,  von';  lat.  pretium  ,Wert,  Preis  einer  Sache' (Neutr.  eines  Adj.  *pretios),  vgl.  ai.  prati-as-  ,gleichkommen',  apratä  (St. *pratay-)  ,ohne  Entgelt,  umsonst',  av.  pdrdskä  (*pj't'Ska)  ,Preis  oder  Wert*,
816      •
i
aksl.  protiv^J  protivg  ,entgegen*,  kaschub.  prociw;  wruss.  preci,  polu.  przeciV ,gegen*  (auch  im  Sinn  des  Tauschverhältnisses);  lett.  pret  usw.
i.  porsö(d):  arm.  ar  ,bei,  an,  neben',  Verbalpräf.  und  Präp. ;  ^^^ araj  ,Vorderseite,  Anfang',  afajin  ,erster';  ^r.  rtÖQQcx),  itOQGü)  (Find.)  ,vor. wärts*  =  lat.  porrö  »vorwärts,  fürder';  durch  ihren  o -Vokalismus  auf. fällige  Bildung.
WP.  II  29ff.,  EM.2  754f.,  801,  808 ff.,  811  f.,  WH.  II  283 ff.,  351,  364ff.^ Trautmann  214f.,  220,  229f.,  230ff.,  Schwyzer  Gr.  Gr.  2,  491ff.,  499ff*| 505ff.,  508ff.,  541f.,  ö43ff.,  654ff.
B.  per-,  pers-  ^hinüberführen  oder  -bringen
```


## [2026-09-14T00:51:35.877Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"######## PHD pēš/pad/bed\"\ngrep -n -E \"^(pēš|pad|bed|paywand|paywastan|pahrēz|pādāšn|passox|pāsox|paygām|paykān|paykār|pašēmān|padrām|nibard|āward)\" PHD.txt | head -40\necho \"######## PHD grep loose\"\ngrep -n -E \"pē(š|s)\\b\" PHD.txt | head -20",
 "description": "Grep MacKenzie Pahlavi dictionary"
}
```


### [2026-09-14T00:51:35.938Z] TOOL RESULT

```
######## PHD pēš/pad/bed
959:bed gah, baléngah.
960:bedding wistar(ag).
2627:pēšār, pēšōbāy,
4603:padišxwar
4625:padēxēn-
4626:padēxēnīdan
4627:padēx, [error for
4629:padir- padiragih padirag padiriftan padirign 12радіѕаг padist- padista(g) padistadan padistán -bed pid paywasag paywiz- paywazag paywāzišn paywand
4630:paywand-
4706:padnigerišn
4707:padwizēn
4708:padzyān purs- pursīdan pursišnīg pursišn padpānag pa(č)čībāy- pa(č)čībāgīh frazand
4722:pēšār
4723:pēšārwār
4724:pēšgāh pēšēnīg pēšēmāl pēšēmālīh pēšūbāy pēšūbāyīh
4725:pēškār, pēšyār
4726:padám payádag 1-2pay, pīh pas, "pay pés
4742:padyabib, ALI 00 t€» о) pādāšn VA My o padirán- ` - My yey a pādīrānēn- -p ry yey a pādīrānēnīdan W3 y ry We pādīrānīdan WS wy veyo pādīrān wey yey os paymar Ne теу o pādēz 23 voy o lpādan Y rero) pādofrāh ау\һе» 0) padzahr NS ve» o» pāygūs ISYA padrozag 15 cP rere pāyram » rey’ о
4743:padrazm sò rey о) pādifrāh © teras arzan!, gāwars! 5o)
4756:padyawandih “> (ry ve» o
######## PHD grep loose
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
732:adorn ārāstan, azrāy-, payrāstan, pēsīdan.
964:before handēmān, pēš.
1424:cover (v.) nihuftan, (nihumbidan), pēšīdan.
1678:don paymēxtan, pēšīdan.
2001:forehead anig, pēšānīg.
2003:foremost pāhlom, pēšēnīg; ~ seat pëšgah.
2013:former pēšēnīg.
2175:guide (n.) parwānag, pēšār, rāhnimāy.
2178:guilty, be — of pēšār būdan.
2581:leadership parwānagīh, pēšēbāyīh.
2602:leper, leprous pēs.
2627:pēšār, pēšōbāy,
2855:mottled pēs.
2926:noble abarmanig, āsnūd(ag), (āsnī- dag), āzād, āznāwar, ēr, pēšēnīg.
3139:plaintiff pēšēmāl.
3260:prosecution pēšēmālīh.
3300:put nihādan; ~ on pēšīdan, paymóx- tan.
```


## [2026-09-14T00:51:37.468Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### HRN leaf for p.33 (leaf=printed+21 => 54)\"\nawk 'BEGIN{RS=\"\\f\"} NR==55' HRN.txt\necho \"### HRN p.230 => leaf 251\"\nawk 'BEGIN{RS=\"\\f\"} NR==252' HRN.txt",
 "description": "Horn pages 33 and 230"
}
```


### [2026-09-14T00:51:38.511Z] TOOL RESULT

```
### HRN leaf for p.33 (leaf=printed+21 => 54)
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
### HRN p.230 => leaf 251
230 —
V
1025. neberd "Kampf, newerd, neberde 'tapfer (Sahn. I, 93
Vers 586).
aw. *ni -r l/^parU^ peretente sie kämpfen'; phlv.
n{i)part "Kampf (AV.).
Vergl. np. äwerd "Kampf (Sahn. I, 218 Vers 1506),
äwerdgäh (häufig), äweriden,
1025*»*« nebld, nebtd 'Fruchtsaft, Wein »).
ap. ^nipita- 'Trank', vergl. ai. pltd- etc. (Nöldeke,
mündliche Mitteilung) 2).
nehire "Enkel' siehe unter newade (No. 1047).
1026. ner, nerr (AM.) "Mann; männlich', nere [nerre), nenne
"männlich*.
aw. naV' "Mann ; phlv. war; ai. när-,
kurd. ner 'männlich'; afy. nar\ oss. d. nale, t. nal
'Männchen von Tieren' (197) ; bei. nar 'männlich'
(258); sangl. narak.
1027. nirx, nerx "Preis, Wert' (z. B. Schefer, Chresto-
mathie persane I, 99)^).
kurd. ni/ir, nir/ "Wert, Taxe'.
Nöldeke (mündliche Mitteilung) stellt das Wort
zu np. /erlden "kaufen .
1028. nerm "weich, sanft', nerml,
ai. namrd' "sich biegend, unterwürfig, ehrfurchts-
voll ergeben; aw. namra.vä/ä (7jPQI,)?; phlv. narm
'weich, sanft*.
LW. kurd. nertn, zaza nemr "weich, sanft*; afy.
bei. (178) wa;^. narm.
1029. ne^^d "nahe', nezdik^ nezdiki,
aw. nazda- "nahe ; phlv. nazdik, nazdist; ai. nedl-
yas-, nedisfha-.
kurd. nizüky nezTk "nahe*; af/. nizde, nizde; bei.
nazlk, n. nazl/, nazi (256) ; sar. nizd.
*) Reimt auf niskerid, Öähn. I, 166 Vers 675.
2) Rücke rt hatte ZDMG. 8, 286 an ai. pidr (d. i. *pizd') ^drücken,
pressen' gedacht.
^) Die BelegstcUe vordanke ich Herrn Prof. Nöldeke.
```


## [2026-09-14T00:51:50.804Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD bed\"\ngrep -n -o -E \".{200}\\bbed \\[.{200}\" PHD.txt | head -5\necho \"=== PHD pad [\"\ngrep -n -o -E \".{250}[^a-zā-ž]pad \\[.{250}\" PHD.txt | head -5\necho \"=== PHD paywastan/paywand\"\ngrep -n -o -E \".{150}paywastan.{250}\" PHD.txt | head -5\necho \"=== PHD pašēmān\"\ngrep -n -o -E \".{150}pašēm.{250}\" PHD.txt | head -5",
 "description": "MacKenzie entries bed, pad, paywastan, pašēmān"
}
```


### [2026-09-14T00:51:50.966Z] TOOL RESULT

```
=== PHD bed
256:anapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince.
566:sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [s
=== PHD pad [
=== PHD paywastan/paywand
547:Рак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāza
=== PHD pašēmān
545:tion. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudatio
```


## [2026-09-14T00:51:58.748Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"pādāšn\" \"paymūdan\" \"paymā\" \"pahrēz\" \"paygām\" \"paykān\" \"paykār\" \"padrām\" \"nibard\" \"āward\"; do echo \"=== $w\"; grep -n -o -E \".{120}$w.{200}\" PHD.txt | head -3; done",
 "description": "MacKenzie further entries"
}
```


### [2026-09-14T00:51:59.839Z] TOOL RESULT

```
=== pādāšn
536:N-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N p
=== paymūdan
=== paymā
212: [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag P
547:! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN 
547:xtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya]
=== pahrēz
540:lence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] def
=== paygām
4718:10303 paydāgīh- = 95747 №0 paydagihistan 1152294 3” е 0 paydāgēn- = 527310500 paydāgēnīdan ММ 8” 5 05 paydag 15? ye» о) paygām -È ve os paygāmbar Sye Yeso petitigih A3 4) M 4290) petītīg 14) 95 1050) petit 12d уез 0› **pid we es panāh ^U? 103 panāhīh AY 10) "oul PITT puhlén- = "yes 10) puhlénidan ure rne 19у frāz erie pēhišn
=== paykān
=== paykār
=== padrām
=== nibard
392:ng. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-rán
512:ammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M 
=== āward
```


## [2026-09-14T00:52:00.967Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT paiti\"\ngrep -n -o -E \".{100}paiti-kan.{150}\" BRT.txt | head -3\ngrep -n -o -E \".{120}paitiš.{150}\" BRT.txt | head -5\necho \"=== BRT pərət\"\ngrep -n -o -E \".{100}p.r.t-.{200}\" BRT.txt | head -8",
 "description": "Bartholomae greps"
}
```


### [2026-09-14T00:52:02.996Z] TOOL RESULT

```
=== BRT paiti
=== BRT pərət
```


## [2026-09-14T00:52:11.964Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT count paiti\"; grep -c \"paiti\" BRT.txt\ngrep -n -o -E \".{80}paiti\\.kan.{120}\" BRT.txt | head -3\ngrep -n -o -E \".{60}paiti\\.gam.{150}\" BRT.txt | head -3\ngrep -n -o -E \".{60}paiti\\.mn?a.{120}\" BRT.txt | head -3\necho \"=== BRT Herr\"; grep -n -o -E \".{60}paiti-\\s*,?\\s*m\\..{150}\" BRT.txt | head -5",
 "description": "Bartholomae paiti compounds"
}
```


### [2026-09-14T00:52:13.222Z] TOOL RESULT

```
=== BRT count paiti
1061
=== BRT Herr
```


## [2026-09-14T00:52:14.586Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG raič\"; grep -n -o -E \".{100}parh[eē]x.{250}\" CHEUNG.txt | head -5\necho \"--- raic entry\"; grep -n -E \"^\\*?raiH?č\" CHEUNG.txt | head -10\necho \"=== CHEUNG mā measure\"; grep -n -o -E \".{80}paym[uū]dan.{200}\" CHEUNG.txt | head -5",
 "description": "Cheung EDIV greps"
}
```


### [2026-09-14T00:52:14.675Z] TOOL RESULT

```
=== CHEUNG raič
--- raic entry
=== CHEUNG mā measure
```


## [2026-09-14T00:52:18.139Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la CHEUNG.txt BRT.txt; echo \"---\"; head -c 600 CHEUNG.txt; echo; echo \"=== grep parhez variants\"; grep -n -i -o -E \".{80}parh[eéē]z.{150}\" CHEUNG.txt | head -5; echo \"=== raic\"; grep -n -i -o -E \".{60}\\bRAIC\\b.{200}\" CHEUNG.txt | head -5",
 "description": "Inspect Cheung file"
}
```


### [2026-09-14T00:52:18.326Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4803500 Sep  4 14:06 BRT.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1769485 Sep  4 14:06 CHEUNG.txt
---
Etymological 
Dictionary 


of the Iranian Verb 


Johnny Cheung 


Etymological Dictionary of the Iranian Verb 


Leiden Indo-European 
Etymological Dictionary Series 


Edited by 
Alexander Lubotsky 


VOLUME 2 


Etymological Dictionary 
of the 


Iranian Verb 


By 


ohnny Cheun 
y g 


LEIDEN : BOSTON 
2007 


This publication has been made possible by the financial support of the 
Netherlands Organization for Scientific Research (NWO), and Leiden Unwersity. 


This book is printed on acid-free paper. 


Library of Congress Cataloging-in-Publication Data 


A СІР. record for this book
=== grep parhez variants
=== raic
```


## [2026-09-14T00:52:21.513Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor p in \"parhextan\" \"parhéxtan\" \"pahréxtan\" \"pahrextan\" \"RAIC\" \"raik\" \"raic\" \"pati-raic\"; do echo \"=== $p\"; grep -n -o -E \".{80}$p.{220}\" CHEUNG.txt | head -3; done",
 "description": "Cheung parhextan / raic"
}
```


### [2026-09-14T00:52:22.608Z] TOOL RESULT

```
=== parhextan
=== parhéxtan
=== pahréxtan
=== pahrextan
=== RAIC
=== raik
=== raic
=== pati-raic
```


## [2026-09-14T00:52:26.628Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor p in \"hrez\" \"hréz\" \"hrez-\" \"pahr\" \"REK\" \"raek\" \"riz-\" \"Verlassen\"; do echo \"=== $p\"; grep -n -o -E \".{60}$p.{160}\" CHEUNG.txt | head -4; done",
 "description": "Cheung fuzzy"
}
```


### [2026-09-14T00:52:27.715Z] TOOL RESULT

```
=== hrez
=== hréz
=== hrez-
=== pahr
=== REK
=== raek
=== riz-
=== Verlassen
```


## [2026-09-14T00:52:30.374Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -l CHEUNG.txt; sed -n '20000,20060p' CHEUNG.txt",
 "description": "Sample Cheung middle"
}
```


### [2026-09-14T00:52:30.431Z] TOOL RESULT

```
58427 CHEUNG.txt

*PIE ingress. *pek"-s/,- > LIV: 468 | Pok.: 798 

*IE COGNATES: Toch. B paks- ‘to cook; [med.] to ripen’ (Hackstein: 89) 

*REFERENCES: WIM II/1: 81; WIM III: 114; Paul 1998: 308b; Lecoq 2002: 133 


*pazd! *to blow, smoke' 

*MIDDLE PERSIAN: BMP pzd- /pazd-/ ‘to blow (the flute)’, MMP n'y pzd’’n (pl.) 
‘flute-players’ = DMMPP: 238b 

Pres.: IND. 3pl. BMP pzdynd /pazdénd/ 

*PARTHIAN: pzd- ‘to blow, play (flute), play a tune’ = Ghilain: 53 | DMMPP: 291b 
Pres.: IND. 3sg. pzdyd (Sundermann 1992: §14) 

*SOGDIAN: BSogd. pzt- ‘smoke’ 

*NWIR: Abz. pözowa/pöz- ‘to sneeze’ 

*NEIR: Oss. fæzdæg, Yghn. payst ‘smoke’ 

© On account of the semantic differences, it is advisable to postulate two separate 
roots of *pazd, cf. Nyberg II: 160a. The often cited preform given for *pazd from 
*pa-zd ‘absitzen’, with prefix *pa-, by Fischer 1979: 224, is unlikely, on which see 
Cheung 2002: 109 f. and Henning, BSOAS 28: 246, fn. 29. This apparently 
exclusively Ir. root may in fact reflect a causative da-present stem (cf. Kellens 1984: 
155 ad 6.2.) of IE *pes- ‘to blow’ (Pokorny: 823 f.), similar to MMP rwzd- ‘to 
desire’ (*rauf?), CSogd. sxwrd- ‘to shout’ (*hyar’). See also *pazd’. 


*PIE— > LIV: – | Pok.: 
*REFERENCES: Abaev, Slovar’ I: 467; Andreev — PeSéereva: 304b; DKS: 43a f., 145a, 177b; Cheung 
2002: 109, fn. 56; Lecoq 2002: 125 


*pazd2 ‘to cause to thread, go’ 

*AVESTAN: Y Av. pazd- ‘to chase, pursue’ = Liste: 34 

Caus.: pres. IND. 3sg. YAv. pazdaiieiti (V 15.5), INJ. med. 3pl. YAv. pazdaiianta (Yt 17.55 £.) 
*PARTHIAN: pzd- ‘to scare, frighten’, pzdgr ‘chaser, hunter? = Ghilain: 53 | 
DMMPP: 291b 

Pres.: IND. 3sg. pzdyd, 3pl. "pzdynd, IMPV. 2pl. pzdyd 

*KHOTANESE: (+ *ati-) LKh. tvasd- ‘to transfer’ || (+ us-) LKh. uspasd- ‘to produce, 
cause’ || (+ *niš-) LKh. naspasd- ‘to remove’ = SGS: 41, 18, 51 

9 All previous attempts to find an etymology for notably Av. pazd- and Pth. pzd- are 
set with problems: the reconstruction posited by Fischer (1979: 224) is 


*rag ? 305 


morphologically impossible (*pa-zd- ‘absitzen’, from *had), on which see *pazd'. 
The connection with IE *pesd- ‘to break wind (softly)’ (Pokorny: 829; LIV: 477), 
recently suggested in Cheung 2002: 109, fn. 56 is actually not compelling
```


## [2026-09-14T00:52:36.057Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"raik\" CHEUNG.txt | head -20; echo \"=== mah/ma measure\"; grep -n -E \"^\\*ma[h1-3]? \" CHEUNG.txt | head; echo \"=== hrez\"; grep -n \"hréz\\|hrez\\|hrêz\\|hryz\" CHEUNG.txt | head",
 "description": "Cheung raik and mā"
}
```


### [2026-09-14T00:52:36.155Z] TOOL RESULT

```
=== mah/ma measure
=== hrez
12781:phryz- ‘to flow’ = DMMPP: 304a 
12785:phryzyd, 3р1. MMP *phryzynd 
20208:*MIDDLE PERSIAN: (+ *pati-) MMP phryz- ‘to keep away from, abstain, avoid’ || (+ 
20210:© On the interpretation of MMP phryz- see Humbach — Skjarve 1983 II: 86 ff. 
20213:(+ *pati-) Pres.: IND. 3sg. MMP phryzyd, 3pl. MMP "phryzynd || (+ *ui-) Pres.: IND. 3pl. BMP wlycynd 
34538:phryz-, 187, 307
```


## [2026-09-14T00:52:39.805Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '20180,20245p' CHEUNG.txt; echo \"#### 12770-12800\"; sed -n '12770,12800p' CHEUNG.txt",
 "description": "Cheung root entry for parhēz"
}
```


### [2026-09-14T00:52:39.869Z] TOOL RESULT

```
cautiously from *ra- ‘to howl’ + z-enlargement. The z-enlargement from ysär- ‘to 
sing’ ? = SGS: 115 

*BACTRIAN: paC- ‘to call, name’, (раѕѕ.) pi- ‘to be called, be named’ = S-W, Bact.: 
220b 

*NEIR: ? M. raZdn ‘language’ (Gauthiot) 

© The Ir. root may be connected to Gr. Ado«w. The *-z of the Ir. root *raHz would 
have to be explained though: contamination with semantically similar roots ?, cf. 
SGS: l.c. 

«PIE ? *leH5K- ‘to call’ = LIV: 402 | Pok.: 650 


*IE COGNATES: Gr. А&ско “I call’, €AaKov (aor.) ‘I called’ 
*REFERENCES: JIFL II: 245a; Chantraine: 622; DKS: 361b 


*raié ‘to leave, let, abandon’ 

*AVESTAN: Y Av. raec- ‘to leave, let’ || (+ *pati-) ‘to desert’ — Liste: 58 

Pres. n-: IND. 35р. YAv. irinaxti (Yt 10.68); Aor. s-: OPT. med. 25р. YAv. paiti raexsisa (P 40); Caus.: 
pres. IND. 35р. YAv. рай raécaiieiti (V 5.8, Yt 10.41), 3pl. YAv. raecaiieinti (Yt 10.41), INJ. 3sg. ҮАУ. 
raécaiiat (Yt 5.78), SUBJ. 3sg. Y Av. “paiti. raecaiiat (ViD 2), IMPV. 25р. YAv. raécaiia (Yt 5.77); 
Intens.: pres. IND. med. 3sg. ? Y Av. iririxsaite (Y 65.7) 

*MIDDLE PERSIAN: (+ *pati-) MMP phryz- ‘to keep away from, abstain, avoid’ || (+ 
*ш-) MMP wryxt- (pret. stem), BMP wlyc- (‘LYKWN-) /wiréz-/ ‘to flee, run away’. 
© On the interpretation of MMP phryz- see Humbach — Skjarve 1983 II: 86 ff. 
c DMMPP: 346a, 274b 

(+ *pati-) Pres.: IND. 3sg. MMP phryzyd, 3pl. MMP "phryzynd || (+ *ui-) Pres.: IND. 3pl. BMP wlycynd 
/ wirezend/; Partic.: perf. pass. MMP wryxt 

*PARTHIAN: (+ *ш-) wryxs- (orig. inch.) ‘to flee? = Ghilain: 94 | DMMPP: 346a 
Pres.: IMPV. 2р1. “wryxsyd; Partic.: perf. pass. wryxt 

*KHOTANESE: (+ *pari-) OKh. pars- (pars-) ‘to escape’, OKh. parrij- (caus./tr.) ‘to 
deliver, rescue’ || (+ *fra-) hars- ‘to be left, remain’ — SGS: 76, 74, 150 

*SOGDIAN: BSogd. rxm’k, MSogd. rxmyh ‘remains’ (BBB: 34) || (+ *apa-) BSogd. 
prys-, CSogd. prxs- (intr./inch.) ‘to remain, be left || (+ *pari-) BSogd. pr’yc, 
CSogd. pryc, MSogd. pryc (caus.) ‘to leave behind, desert’ 

(+ *apa-) Pres.: IND. 3sg. BSogd. prxsty, MSogd. prxst, MSogd. prxstyy, SUBJ. 3sg. BSogd. prxs't, etc. 
|| (+ *pari-) Widely attested: Pres.: IND. 2sg. SSogd. prycy, BSogd. pr’yc’y, 3sg. BSogd. pr’yct, etc. 
*CHORESMIAN: rycy- ‘to spread out’ || (+ *apa-) pryX- ‘to leave behind’ = Samadi: 
160 

*BACTRIAN: pnyo ‘remains, what is left’ = S-W, Bact.: 221a 

*NWIR: NP ristan ‘to set at liberty, absolve’ || (+ *ui-) NP guréxtan/guréz-, Fariz. 
-wret-/-wrej-, Yar. -wret-/-wrej-, Jow. ba-urut-/a-urud3-, Meim. ba-rveft-/a-iru:ds-, 


308 *raip ? 


Nn. virite/viriss- ‘to run away from, flee’, Sang. -urít-/-uriZaen-, Sorkh. -owrut-/ 
owriZ- ‘to flee’ 

*NEIR: Oss. I. lizyn/lygd, D. lezun/ligd ‘to run away; to abandon a settlement; to 
move to another place, resettle’, Pash. raZedol ‘to cast off, shed, to fall (as leaves)’, 
Sh. (Baj.) ris-/réd, Rosh. rays-/rayd, Bart. ra(y)s-/rid, Sariq. ris-/reyd, Yzgh. raxs-/ 
#### 12770-12800
*IE COGNATES: Olrish -ráidi ‘deliberates, says’, Goth. ga-redan ‘to take precautions’, 
Goth. rodjan, NHG reden ‘to talk, speak’ (« *‘to deliberate, premeditate"), ORuss. 


raditi ‘to care for’, OCS ne-raditi ‘to neglect’ 
*REFERENCES: DKS: 143b f.; Werba 1997: 396 f. 


*Hraié ‘to pour, flow’ 

*MIDDLE PERSIAN: MMP ryc- (sic), BMP lyc- /réz-/ ‘to flow; pour’ || (+ *pati-) MMP 
phryz- ‘to flow’ = DMMPP: 304a 

Pres.: IND. 3sg. BMP lycyt /rézéd/, 3pl. MMP rycynd, BMP lycynd /rézénd/; Partic.: perf. pass. MMP 
“ryxt ‘cast (of gold)’, BMP Iyht /réxt/; Inf.: BMP Iyhtn /réxtan/ || (+ *pati-) Pres.: IND. 3sg. MMP 
phryzyd, 3р1. MMP *phryzynd 

*PARTHIAN: ryz- ‘to pour’. On ryz- ‘to fall (of leaves)’ see *raiz’. > Ghilain: 94 | 


DMMPP: 304a, 274b 

Partic.: perf. pass. ryxt 

*SOGDIAN: BSogd. ryz ‘to flow’ || (+ *apa-) SSogd. p’ryc (caus.) ‘to pour (out) 
(SDGM III: 34) || (+ *ui-) CSogd. wyrxs- (inch./pass.) ‘to be poured’ 

Pres.: OPT. 3sg. BSogd. ryz’y (+ *apa-) Caus.: impf. IND. 3sg. SSogd. p’ryc (+ *ui-) Pret.: tr. IND. 3pl. 
CSogd. wry’rnt, Partic.: perf. pass. CSogd. wyrxc’ (Ё) ‘poured’
```


## [2026-09-14T00:52:50.999Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor p in \"paymüdan\" \"paymudan\" \"paymäy\" \"pym’d\" \"to measure\" ; do echo \"=== $p\"; grep -n -o -E \".{80}$p.{160}\" CHEUNG.txt | head -4; done",
 "description": "Cheung measure root"
}
```


### [2026-09-14T00:52:52.183Z] TOOL RESULT

```
=== paymüdan
=== paymudan
=== paymäy
=== pym’d
=== to measure
```


## [2026-09-14T00:52:54.654Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"measure\" CHEUNG.txt | head -20",
 "description": "Cheung measure"
}
```


### [2026-09-14T00:52:54.702Z] TOOL RESULT

```
1848:*NEIR: Oss. I. baryn/barst, D. barun/barst ‘to contemplate, measure’; to forgive’, 
9758:"prothetic" ?) || (+ *ham-) NP hamar ‘number, quantity; measure’ 
9761:‘measure of dry substances, chiefly of grain’, Pash. dö-mra ‘so much’, cö-mra ‘how 
16225:*CHORESMIAN: ? kcy- ‘to throw (away), put on, to; to dictate’, knd- ‘to measure, 
16226:measure off (before cutting off the leather)’ || (+ *upa-) bkrzy- ‘to attack’. > It is 
16898:*maH! ‘to measure’ 
16900:*AVESTAN: mä- (mi-) ‘to measure’ || (+ *ä-) ‘to be ready’ || (+ *fra-) ‘to allow, 
16922:stem), BMP ptm’d- /paymäy-/ ‘to measure’ || (+ *pari-) ? MMP prm’y- ‘to 
16933:*PARTHIAN: (+ *pati-) pdm'd- (pret. stem) ‘to measure (against)’ || (+ *pari-) prm’y- 
16945:*KHOTANESE: (+ *apa- ?) LKh. pim- ‘to measure’ (SVK I: 72 f.) = SGS: 83 f. 
16949:ptm’ky, CSogd. ptm’q ‘measure’, BSogd. ptm’t’y ‘measured, frugal’ || (+ *pari-) 
16972:*CHORESMIAN: (+ *pati-) рсту- “о weigh, measure’ || (+ *fra-) sm’- ‘to order, turn 
16984:(Sor.) péw-, Awrom. pimay/pim-, Gz. pääm-/päämä, Khuns. p&im- ‘to measure, 
16994:|| (+ *pati-) Pash. pyamal ‘to measure (as liquids, grain, etc.)’ = pem-/pem(d) (cf. 
16995:Sims-Williams, apud NEVP: 63), Wa. patm(a)y-/patmat- ‘to measure’ || (+ *fra-) 
17005:*SANSKRIT: та ‘to measure’ (RV+) = EWAia П: 341 
17007:«PIE *meH_- ‘to measure’ => LIV: 424 f. | Pok.: 703 f. 
17013:*IE COGNATES: Lat. metior ‘I measure (out), Toch. A me-, B mai- ‘to measure’, 
17016:Goth. mel ‘time, hour’, OHG mal ‘moment’, Russ. méra ‘measure’, etc. 
18037:Derived from *maH! ‘to measure’.
```


## [2026-09-14T00:53:06.326Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==252' POK_01.txt | head -40; echo \"#### NP paymudan cheung\"; sed -n '16975,17000p' CHEUNG.txt",
 "description": "Pokorny p.243 and Cheung NP forms"
}
```


### [2026-09-14T00:53:07.665Z] TOOL RESULT

```
srri-xtm mit  demselben  Konsonantenverhältnis  wie  zwischen  nvvda^ :  ai.  budh-nd-\
WP.  I  850  f.,  Kuiper  Nasalpräs.  147,  Schwyzer  Gr.  Gr.  I  333.
dheg^h-  ^brennen';  Nominalbildungen  dti6g^ho-s,  dheg^h-ro-s.
Ai.  ddhati,  av.  dazaiti  , brennt'  (=  lit.  degü^  aksl.  zegg,  alb.  djek)^  Partiz. ai.  dagdhd-h  (=  lit.  degtas),  Kaus.  dähdyati]  däha-h  ,Brand,  Hitze',  nidagha-]^ , Hitze,  Sommer',  npers.  däy  , Brandmal'  (dazu  spätgr.  ödyalog,  -ig  ,rot- braunes  Pferd'?);  av.  daxsa-  m.  ,Brand';
gr.  d-emavog'  ä7tTÖ{,isvog  Hes.  (,angezündet';  =  lit.  degtinas  ,wer  oder was  zu  verbrennen  ist'),  tscpqä  , Asche'  (*dheguhra)]
alb.  djek  ,verbrenne,  brenne  an',  Kaus.  dhez,  n-dez  .zünde  an'  (Gdt *dhoguheiö  =  lat.  foveö)]
lat.  foveö,  -ere  ,wärraen,  hegen,  pflegen',  föculum  ,Feuerpfanne'  {^'foue- clom),  fömentum  ,ein  erwärmender  Umschlag'  {*fouementom)j  fömes,  -itis , Zunder'  (*fouemet-j  Bedeut.  wie  lett.  daglis),  favilla  , Asche,  bes.  noch glühende'  (wahrscheinlich  aus  *dhogi^h-lo-lä):  favöniiis  ,der  laue  Westwind' (aus  ^-fovönios)'^  febris  ,Fieber'  C^dheguhro-;  nach  Leumann  Gnom.  9,  226 ff. die  i-Flexion  nach  sitis).
Mir.  daig  (Gen.  dega)  ,Feuer,  Schmerz'  (aus  *degi-)]  über  mbret.  deuijf, nbret.  devi,  cjmr.  deißo  ,brennen'  s.  unter  *<^äw-, brennen';  cymr.  de ,brennend'; go-ddaith  ,Brand'  (aus  "^-dekto-)]  aber  air.  ded-öl  ,Morgengrauen'  nach Mai-strander  Dict.  Ir.  Lang.  I  213  eigentlich  .Abschiedstrunk,  letzter  Trunk'; nir.  dogha  ,Klette'  (:lit.  dagys  s.  unten);
über  got.  dags  ,Tag'  usw.  s.  unter  '^'ügher-  S.  7:
241
.  lit.  degu,  degt'i  .brennen'  (trans.  und  intrans.);  degtas  .gebrannt',  degtinas xras  25U  verbrennen  ist',  degüne  f.  .Branntwein',  ablautend  dagys,  dägis 'oistel'  (lett.  dadzis);  dägas  .das  Brennen;  Sonamerbitze;  Ernte',  dagä  .Ernte', ipr.  dagis  .Sommer';  lit.  däglas,  .brandfarben',  deglas^  .schwarzscbeckig-; lott.  daglas  f.  PI.  .Brandfleck',  daglis  .Zunder';  lit.  nuodegulis  .Feuer- brand'; degis  »Brandwunde';  ablaut.  atüo-dogiai(?)  m.  PI.  .Sommerweizen';
sloven.  djgniti  .brennen,  wärmen',  cech.  alt  dehna  .Teufel',  ablaut. Jahneti  .brennen';  russ.  degoth  .Teer'  (aus  .*harzreicbes  Holz'),  wie  lit. degtitas  .Birkenteer';  mit  Assimil.(?)  von  *degg  zu  "^gego:  aksl.  zegg,  zesti ^brennen',  ablaut.  >uss.  iz-gdga  .Sodbrennen'  (s.  Meillet  MSL.  14.  334  f., anders  Brugmann  II ^  3.  120).
Tocb.  B  teki  .Krankheit'  (=  ir.  daig)'^  A  tsäk-,  B  tsak-  .brennen',  das i8  nach  dem  ablaut.  tsäk-  {*dheguh-)  .glänzen,  glühen';  AB  cok  , Lampe' (aus  .Kienfackel')  :  bsl.  *degut-  .Teer'  (s.  oben).
WP  I  849  f.,  WH.  I  466  f..  469.  471  f..  864.  Trautmann  49.  Pedersen Tech.  Sprachg.  23.
äbS(i)'  (daneben  dh-ei-  ?)  .saugen,  säugen'  ( :  c?Äai-.  dJvt-  und  dhe-j  dhd-)  s
#### NP paymudan cheung
because an intervocalic *h has regularly disappeared in Chor., but also because the 
appearance of -h- in the subj. seems to be intrusive in origin, viz. probably from the 
subj. (3sg.) y’h’c of y- ‘to be’ (s.v. *Hah). = Samadi: 142, 153, 195 

*BACTRIAN: (+ *fra-) ọpopa- ‘to order, command’ = S-W, Bact.: 230b 

*NWIR: (+ *4-) NP ämädan/amäy- ‘to prepare’ || (+ *a- + *uz-) NP azmüdan/azmay- 
‘to try, test, prove, tempt’, NP 4zmudan/azmay-, Gz. uzn-/uznä ‘to try, test, prove, 
tempt’ || (+ *pati-) NP paymüdan/paymäy-, Kurd. (Kurm.) pivin/piv-, payvin, pivan, 
(Sor.) péw-, Awrom. pimay/pim-, Gz. pääm-/päämä, Khuns. p&im- ‘to measure, 
traverse’ || (+ *pari-) NP parmäsidan ‘to know’ || (+ *fra-) NP farmudan/farmay- ‘to 
order, command; [in polite address] to say’, Awrom. farmaway/farmaw- ‘to order, 
deign’, Fariz. bäfärmä ‘order !’, Gil. (Rsht.) farmoestoen/farmaj-, Ham. färmayän/ 
färmon-, Jow. ba-farma:niya, Sang. -farmij-/farmoen-, Shamerz. -farmim-/farmam-, 
Sorkh. -farm-/farma- ‘to order’, NP farman ‘order, command, decree’, Tal. hamue 
‘to order, command’ || (+ *ni-) NP nimäy-/nimüdan ‘to appear, show’, Kurd. (Sor.) 
niwen-, Awrom. nimana, (sec. caus.) Gz. numn-/numnä ‘to show’ 

*NEIR: (+ *a-) Oss. I. amajyn/amad, D. amajun/amad ‘to build up (a wall, logs, etc.) 
|| (+ *pati-) Pash. pyamal ‘to measure (as liquids, grain, etc.)’ = pem-/pem(d) (cf. 
Sims-Williams, apud NEVP: 63), Wa. patm(a)y-/patmat- ‘to measure’ || (+ *fra-) 
Yghn. farmóy-/farmóyta ‘to order, command, wish’, Ishk. ferma(y)-, Sangl. farmé-, 
Sh. (Baj.) rimi(y)-/rimöd, Rosh. rimay-/rimüd, Bart. rimiy-, rimay-/rimöd, Sarig. 
rimey-/rimud, Yzgh. Xamay-, Wa. ram(a)y-/ramat- ‘to command, order; to send’ || (+ 
*ni-) Oss. I. nymajyn/nymad, D. nimajun/nimad ‘to count, value, esteem; to read’, 
Sh. (Baj.) rimi(y)-/rimöd, Rosh. rimay-/rimüd, Bart. rimiy-, rimay-/rimöd, Sarig.
```


## [2026-09-14T00:53:17.813Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==253' POK_01.txt | head -45",
 "description": "Pokorny leaf 253"
}
```


### [2026-09-14T00:53:18.812Z] TOOL RESULT

```
. bes.  Schulze  KZ.  27.  425  =  Kl.  Sehr.  363.  Nominalbildungen:  dhe-lä .Mutterbrust',  dhi-lo-  , Zitze',  dbe-lu-  .säugend'.  dbQi-l-  ds.,  dhei-nä .trächtig',  dhe-nä  .Fruchtertrag',  dhedhn-  .(saure)  Milch'. Ai.  dhäya-h  .ernährend,  pflegend',  dhäyas-  n.  .das  Saugen',  dhäyü-  .durstig'. dhätave    .zu    saugen',    Fut.  dhäsyati,    i^or.    ddhät   ,er    sog',    su-dhä    .Saft, Nektar',  dhätrl  .x4mme.  Mutter',  dhenü-  f.  .milchend'  =  av.  daenu-  .Weib- chen von  vierfüßigen  Tieren',  ai.  dJiBnä  .Milchkuh',  ablaut.  dhud-  .gesogen*^, Perf.  Plur.  1.  3.  da-dhi-md  (i  =  »),    da-dh-üh]   redupl.   Nomen    da-dh-an-j Nom.  dd-dh-ij  Gen.  dadhnds  .saure  Milch'  (:  apr.  dadaUj  alb.  djathej'j
vom  Stamme  dhoi-:  dhdyati  .saugt'  (*dh^ieti  :  Kaus.  *dhoi-4ie-ti  in slav.  dojiti,  got.  daddjan)  und  dhinöti  .nährt';
arm.  diem  .sauge'  (^  =  idg.  e  oder  eher  l,  so  daß  =  anord.  dia),  stn-di ,(Brust  saugend  ==)  Säugling',  dal  aus  dail  ,Biestmilcli'  (dhdi-li-)^  dayeak ,Amme'  (von  *dayi-  =  idg.  dhd-ti-)]
gr.  d-TjoaTo  .er  sog',  d^rja^at  .melken',  ^rjVLOv  ,Milch',  TL&rjvrj  ,Amme' (Kurzform  zlrd-rj  u.  dgl.,  worüber  anders  Falk-Torp  u.  taute),  yaXad-rjvög .Milch  saugend'.  n-d-aGÖg  ,zahm,  kultiviert';
alb.  djathe  .Käse'  ursprüngl.  ,aus  saurer  Milcb  gemachter  Quark'  (:ai. dddJii),  gr.-alb.  dithe  ,Käse';
lat.  femina  .Frau'  (,*die  säugende');  über  felix,  fecundus  s.  unten; air.  dinu   ,Lamm',    dlth   ,suxit'   {}  =  idg.  e   oder  i),    denaid   ,er   saugt' {*di-na-ti),  bret.  denaff  ,sauge',  cjmr.  dynu  .saugen';
16
242
got.  daddjan  =  8isc\iwed.  dceggja  ,säugen'  (urgerm.  *dajjan,  vgl.  ai.  dhdyat aksl.  dojo]  das  germ.  *dajj-  ist  regulär  aus  *dhoi-eie-  entstanden),  aschw« dla,   d'ä.n,  norw.  die  , saugen',   mhd.   dien,   tlen  ,säugen;    die  Brust   gebe^ (vgl.  0.  arm.  diem),  hochstufig  ahd.  täen,  Präs.  täju  (=  lett.  deju  ,sauge' Avestfäl.  däierrn  ,ein  Kalb  mit  Milch  auffüttern'  (Holthausen);
lett.  deju,  det  ,saugen',  at-diene,  at-diemte  ,eine  Kuh,  welche  im  zweite] Jahr  kalbt',  lit.  dieni  f.  ,trächtig'  (=  ai.  dhenü-),  dienä  ds.  (=  ai.  dhenä  ,Kuh*3 apr.  dadan  , Milch'  (=  ai.  dadJian-)]  aksl.  dojg  ,säuge'  (ai.  dhdyati),  doilicQ ,Amme',  mit  e  (=  idg.  e  oder  9i)  däth  f.  ,Kinder',  deva,  devica  ,Määchen Jungfrau'  (verschoben   aus   ,*Weib'  =  ,die  säugende',    s.  Berneker  197);
Mit  i-Formantien:   Ai.    dhärü-  ,saugend'  =  gr.  ^fjXvg  ,nährend  {isQSijJl säugend,    weiblich'    (fem.    d^r^leia    und    d-^lvg)^    ^^Xw,    -d^rjXa^tbv   ,Aminef d-r^laCo}  ,säuge,  sauge',  d^rilrj  ,Mutterbrust',  alb.  dele  , Schaf  {*dhdil-n-),  dek ds.,  dhalle  , saure   Milch',   illyr.  dalm-  , Schaf  in  ON  JdX^iov,  Jelixivio^ VN  Dalmatae,  Delmatae,  messap.  PN  Gen.  m.  dalmaihi,  fem.  PN  dalmad-oa' lat.  felö,  -äre   ,säugen',  fllius   ,Sohn'   (,*Säugling',   aus    *felios)  =  umbr^ fel
```


## [2026-09-14T00:53:31.768Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==254' POK_01.txt | head -25",
 "description": "Pokorny leaf 254"
}
```


### [2026-09-14T00:53:32.882Z] TOOL RESULT

```
iuf,  filiu  ,lactantes';   mir.  del  , Zitze'  (*dhi-lo-),  delech  ,Milchkuh',  danT dcel  , Milchdrüsen  oder  Euter  bei  der  Sau',  schwed.  mdartl.  del  m.  jZitze*^ ahd.  tila  f.  ,weibliche  Brust',  ags.  delu  f.  ,Brustwarze,  Zitze',  anord.  dilkrl ,Lamm,   Junges';   lett.   dels   ,Sohn',  dele    ,Blutegel',    lit.  dele    ds.,  pirmdell '^ ,die  zum  ersten  Male  geboren  hat',  pirmdelys  ,was  gerade  geboren  worden ist';  lett.  dile  ,saugendes  Kalb',  dllit  ,säugen'.
Ob  gr.  d^tjad-ai  {^d^wisad-ai) , schmausen',  d^oivi]  ,Schmaus'  (aus  *d-(x}L-vG?) mit  Abtönung  hierher  gehöre,  ist  fraglich;  ob  d-Co^ai  und  (dor.)  d-a^ai ^lied-vaai^  als  ^d^oia'/.-(Jai  auf  eine  leichte  Wz.  *dhÖi-  (ebenso  dann  d^oirt]] auch  d'üJa-d'aL  kann  d-oia-od-ai  sein)  weisen?
Lat.  felix  , fruchtbar,  glücklich'  zu  feläre  geht  auf  ein  fem.  Subst. *fell-c-  ,die  säugende  =  fruchtbare'  zurück,,  nach  Specht  (KZ.  62,  237) aus  '^felui-k-s,  Femin.  zu  ai.  dhäru-,  gr.  d-fjXvg',  lat.  fecundus  ,fruchtbar^, fetus,  -üs  ,das  Zeugen,  Gebären',  feta  , schwanger,  trächtig',  auch  ,was geboren  hat',  effeta  , durch  vieles  Gebären  geschwächt',  fenus,  -oris  , Er- trag, Zinsen,  Wucher',  vielleicht  auch  fenum  ,Heu'  (als  , Ertrag')  erklären sich  aus   einer  Sonderanwendung  von   dhei-  , säugen'  für  , fruchtbar  sein';
dazu  aber  nicht  *dhönä-  , Getreide'  :  ai.  dhänäh  f.  PL  , Getreidekörner', dhänyd-  n.  , Getreide',  np.  däna  ,Korn',  av.  dänö-karsa-  ,eine  Ameisenart', d.  i.  , Körner  (=  Ameiseneier)  schleppend',  toch.  B  tano  ,Getreide'  und lit.  ddona,  lett.  duona  f.  ,Brot'  (ursprüngl.  , Getreide',  alit.  , Ausgedinge'); dor. -illyr.  (kret.)  ÖTjal  .  .  .  ai  KQid^ai  EM.,  örjTTcci'  al  inTLGf.i€vaL  xQi&ai (*c?Äe-Ä;-ia-)  Hes.;  anders  Jokl  bei  WH.  I  475;
s.  auch  oben  1.  dhe-,  dhe-dhe-.
WP.  I  829  ff.,  WH.  I  474  ff.,  864,  Trautmann  51.
245
.  rihiä-  :  dhi-  .sehen,  schauend -     *Ai.    ddldhet   ,Qr    schaute',    PL    dldUmah,    Med.   didhye,    ddldkUa,    Konj. thdhayat  (vielleicht  zum  Präs.  umgewandeltes  Perf.,  vgl.  Perf.  dldliaya)'^ jf^ya-th  dhyä-ya-ti  (lO-Präs.)  ^schaut  im  Geiste,  d.  i.  denkt,  sinnt',  Partiz. »j^yj.^rt-und  dhi-tä-,  dhyä  ,das  Denken,  Sinnen',  dhyä-tar- , Denker^,  dJiyä-na- „    ,das   Sinnen,   Nachdenken',   dhyäman-  n
```


## [2026-09-14T00:53:42.902Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"peikän\" \"peikan\" \"peyām\" \"peigäm\" \"peikär\" \"peiwesten\" \"pesīmān\" \"peimūden\" \"perhīzīden\" \"pädäš\" \"päsux\" \"pedrām\" \"āwerd\" \"pēš\" \"pīš\"; do echo \"=== $w\"; grep -n -o -E \".{60}$w.{200}\" HRN.txt | head -3; done",
 "description": "Horn headwords"
}
```


### [2026-09-14T00:53:44.076Z] TOOL RESULT

```
=== peikän
=== peikan
=== peyām
=== peigäm
=== peikär
=== peiwesten
=== pesīmān
=== peimūden
=== perhīzīden
=== pädäš
=== päsux
=== pedrām
=== āwerd
=== pēš
=== pīš
```


## [2026-09-14T00:53:51.176Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o -E \".{50}(pekan|pekän|pegam|pegäm|pekar|pekär|pewesten|pesman|pesiman|pemuden|perhezden|perhez|padas|pasux|pasox|pedram|awerd|pes 'vor|pes ‘vor)\" HRN.txt | head -20\necho \"###### HRN leaves 89-96 (pp 68-75)\"\nfor n in 89 90 91; do echo \"--- leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' HRN.txt | head -50; done",
 "description": "Horn pages 68-70"
}
```


### [2026-09-14T00:53:52.246Z] TOOL RESULT

```
###### HRN leaves 89-96 (pp 68-75)
--- leaf 89
— 68 —
kurd, per e; af}'. parün; oss. vergl. /ar- (274, 1);
bei. paran- 'darüber hinaus gehend' (284).*
304. pervär *Stair^).
aw. *2)airivära?ia-, vergl. pairi.vära- 'Wall*, 'Stall'
(vd. 2, 26 vielleicht, Bartholomae); phlv. {pä-amün-)
parvär,
eS05. perväi^ 'Flug .
aw. pairi (oder para) — V^vciz-, 'herum- bezw. weg-
fliegen , vergl. vazaiti er fliegt*.
306. jyerwerden ernähren, erziehen*, periveris, perwer'tden,
pari -f- y^hhar-; phlv. partoarfan, partvar(i)sn,
307. pervez 'siegreich*.
phlv. aparvej 'siegreich'; wohl zu «r^i, be.ze (No. 253)?
Dann perwez.
308. pervfn 'Plejaden*.
aw. paoiryaeinyas\ca (yt. 8, 12), de Lagarde, Beitr.
z. altb. Lex. 56.
af/. peröne; bei. panvar 'Plejaden (Dam es, 54).
309. perhey(ten 'sich enthalten ; sich hüten', Praes. perliez-etn^
perhez, perheztden^).
aw. palti + [/ra^c- 'verlassen'; phlv. pahre/tan
'sich enthalten', pahrej, pahrej(i)sn.
kurd. pärlstin, dispärise 'ist enthaltsam, enthält sich*.
^) Die persischen Original Wörterbücher geben für hervär (No. 210)
und pervär (die de Lagarde schon geschieden hat) zusammen die
folgenden Formen an : pervär^ perräre, perbär, perbärff perbäl, perbcUe^
fervür^ ferväre (vergl. No. 82S)^ fet'väl^ ferväle . von denen die mit/
beginnenden in dieser Bedeutung gewiss falsch sind. Als Beleg für
die Bedeutung *Stall* dient ein Vers des Xäqänl (Metrum: Munsarih).
röz^ beperrär^ büd^ färbe ez an sude cünin
seb tSn-t himär^ däst läylr ez an sude dun an
^) Die Annahme , dass np. pärsä 'enthaltsam , fromm*, aus
*perhezä (eine solche Form construirt sich Darmesteter, Et. ir. I,
115, NB. ohne Stern) contrahirt sei, ist durchaus unstatthaft. Pärsä
bedeutet überhaupt nicht 'enthaltsam', sondern ursprünglich nur *brav*
(vergl. Sahn. I, 35 Vers 15, 70 Vers 158 u. o.), es bezeichnet gewiss
eigentlich den Pärsen.
--- leaf 90
— 69 — '
810. perl 'Perl, guter Genius*.
aw. pairlkä' *Hure'; phlv. parlk, arm. LW. parik,
LW. af/. parT.
Nach Bartholomae, BB. 15, 9 ist die SiW. pairikä-
ursprünglich *die Fremde'.
811. perer Vorgestern, perejröz, pere\seb.
Kilo, perc; pere]sdl, pe7^i]söUf per]sew^ pörijsd.
aw. '^parö.ayare; phlv. parer.
kurd. picne (Houtum-Schindler), per; oss. vergl.
fal'iväre 'im vorvorigen Jahre' (274, 2); bei. parerl^
paireri^ n. paln (285).
812. piSmanj pemän^ ptizmän (8ähn. I, 359 Note 2, Calc.)
'bereuend', pesiman,
ap. patü r *wawc/- ; phlv. pasTmän (paz. pasemän) ;
ai. /)ra^^ -i- y/'yw^w- 'erwiedern, entgegenhalten'.
Die Entstehung der Form pesJmän ist ganz unklar ;
piz'' scheint aber sicher auf patis hinzuweisen. Der
Wechsel von z und s findet sich auch sonst dialectisch.
313. pi^fnurden, pezmurden 'erschlaffen, verblühein', pilOTi:!
(Is. 16, 8 u. ö.), plzmertden (Vis und Rämin, S. 47
V
Vers 16), pizmeranlden (Sahn. 85 Vers 433).
ap. paus bezw. aw. aiwis j- \^mar-,
piZ' Scheint wegen jüd.-pers. V\^ ein alter Fehler
für biZ" zu sein, (de Lagarde, Persische Studien,
75), doch findet sich piz- auch in pizöhiden und Ab-
leitungen (No. 314) und in pizmän (No. 312). Jeden-
falls spricht man heute p" (W o 1 1 a s t o n) ; das b
des Gazophylacium's (s. v. infracidirsi) kann
nichts beweisen. — Im Wesentlichen übereinstimmend
ist die Auffassung Nöldeke's, ZDMG. 45, 106
Anm. 3, welche ich erst nachträglich zu Gesicht
bekommen habe.
814. pizohlden 'erforschen, nachfragen*, pizöh, pizöhis^).
Reime z. B. Sahn I, 73 Vers 215, Sälin. I, 140 Vers 198. Die
Wörterbücher wissea nichts mehr voa einem Majhülvooal.
--- leaf 91
70 ~
phlv. ^patv(i)hltan , vergl. u^v(i)hTtan^ vd. 19 (16),
nv(i)himtan ^).
aw. *paitis + 1 [/'va^d-^ caeday^mi] ai. prati +
i/^ved'.
Np. h aus altem d zwischen Vokalen z. B. auch in
/'ähem aus ^svädämL Die gleiche Behandlung von d
und d (bei letzterem häufige Fälle des Übergangs in h)
zeigt, dass das d zwischen Vokalen im Persischen
ebenfalls spirantisch gesprochen wurde, daher auch
keine Scheidung im Altpersischen durch besondere
Buchstaben ; vergl. auch die allgemein durchgeführte
Spirans d bei AM., also im älteren Neupersisch, über
die Behandlung im Reim siehe Rückert, ZDM6. 8,
285, 286, 10, 263.
315. pes 'hinter, nachher, pesin 'letzter.
Käs. peCj pdc]es, pes.
ap. pasa, 'hinter', pasäva 'nachher ; aw. pasda 'nach',
paskät nachher, hinter , pasne 'hinter' ; phlv. paSj pasTn
'letzter ; ai. pagdd *hinter, nachher , pagcdt Von hinten,
hernach*.
kurd. püstve, pfisl; af/. LW. pas; oss. d. fastäge, t.
fästäg 'hinterer, nachher, zuletzt, am Ende' (280) ; bei.
pas^ Comp, pastara (287).
316. pest 'niedrig, nnoilN (Is. 2, 9; 11, 17).
ai. vergl. üpastiä, upastis 'Untergebener .
Bartholomae (briefliche Mitteilung).
LW. wa/. past, siyn. pist,
317. pistän 'Brust (der Frau)'.
a.w./stana' *Brust'; phlv. p(i)stan (vd. 9 (71)), pistän
(vd. 15 (26) 61.); ai. stdna-; arm. stin (H. No. 259).
LW. af/. pistän.
Vergl. Bartholomae, Indog. Forsch. I, 187 Anm. 2.
318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
1517 Vers 358 2), 1523 Vers 473).
*) So lese ich statt nvedlnltan.
*) An den beiden ersten SteUen vielleicht für puser zu emendireD,
doch kann bei puser wie bei pider die Izäfe fehlen, vergl. Landauer
zu S. 1517 Note 4.
```


## [2026-09-14T00:54:05.347Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor g in \"Pfeilspitze\" \"Botschaft\" \"Vorwurf\" \"verbinden\" \"'messen\" \"Lohn'\" \"Antwort\" \"ruhig, froh\" \"'vorn\" ; do echo \"=== $g\"; grep -n -o -E \".{200}$g.{120}\" HRN.txt | head -4; done",
 "description": "Horn by German gloss"
}
```


### [2026-09-14T00:54:06.460Z] TOOL RESULT

```
=== Pfeilspitze
=== Botschaft
=== Vorwurf
=== verbinden
=== 'messen
=== Lohn'
=== Antwort
=== ruhig, froh
=== 'vorn
```


## [2026-09-14T00:54:09.304Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor g in \"Pfeilspitze\" \"Botschaft\" \"Vorwurf\" \"Lohn\" \"Antwort\"; do echo \"=== $g\"; grep -n \"$g\" HRN.txt | head -6; done",
 "description": "Horn plain grep German glosses"
}
```


### [2026-09-14T00:54:10.359Z] TOOL RESULT

```
=== Pfeilspitze
3401:362. peikän 'Pfeilspitze, Pfeil'.
=== Botschaft
3291:348. peyam ^Botschaft', peiyäm'^)^ peiyätnber , peyämber^
9125:1053. uuved *frolie Botschaft.
=== Vorwurf
10980:vergl. säst 'Schelten, Vorwurf, Drohung, Unwille,
=== Lohn
5086:(zu z aus z vergl. np. miizd^ ^mizd 'Lohn gegen aw.
8507:978. muzd, muzd 'Lohn, Preis', muzde {mizde) 'frohe Bot-
8509:aw. mUda- 'Lohn'; phlv. m(i)zd (paz. mozd), mtizd
8511:'Lohn'.
8512:oss. d. mizd, t. m^izd 'Bezahlung, Vergeltung, Lohn,
9808:agrn --- 'Lohn', sondern von ^agru 'Mietling* abzu-
=== Antwort
2724:275. päsu% 'Antwort'.
2727:patas/ani 'Antwort*.
```


## [2026-09-14T00:54:13.035Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2700,2740p' HRN.txt; echo \"#### 3285,3300\"; sed -n '3285,3305p' HRN.txt; echo \"#### 3395,3420\"; sed -n '3395,3425p' HRN.txt",
 "description": "Horn pāsux, peyām, peikān entries"
}
```


### [2026-09-14T00:54:13.113Z] TOOL RESULT

```
*) Zu phlv. pata^sa, np. padisäh als t. t. beim Ehesohluss vergl.
West, Pahlavi Texts» 142 Note 10.
2) FR und F J haben als Beleg folgenden Vers des Ferälädl
(so nach Eth6, Morgenländisohe Forschungen, während FR und die
Strassburger Handschrift des FJ Ferälävl, Salemann, SF Feräläri
schreiben), Metrum: Xeflfi
mäde-gävän-t päde-es her yeh
mh^perver huved cn hirmäyün— 62 ~
271. päre ^ück, Teil'.
ai. pärd- *das Letzte' ; (^w, para- SchulaX?) ^) ; phlv.
pärak 'Stück; Geschenk (behufs Bestechung)', AV.
272. päzen *Bergziege*, päzen,
phlv. pacm (Bund.) ; bei. pädin, n. päsin 'Ziegenbock,
männliche wilde Ziege* (290).
273. päzehr 'Gegengift, Bezoar.
paiti + zehr (s. zehr No. 678).
274. päs 'Schutz*, pasban^ päsTden,
aw. pädra- 'Schutz'; phlv. pas (Bund.), pOspäti, vd.
13 (77); ai. pätra-.
274*»^* päsäyt 'bereit'.
paiti + sagten (s. No. 688) ; phlv. pasa/tan^ pasaxtak
(AV.).
phlv. palsäytan könnte auf die Praeposition pa (tipa)
deuten, doch vergl. phlv. j^^^^X (No. 275).
275. päsu% 'Antwort'.
aw. ^paitisahva- [paiti + [/'safih- hat zwar im Awesta
nur die Bedeutung 'beschwören') ; phlv. pasu/ ; arm.
patas/ani 'Antwort*.
276. päSne 'Ferse'.
aw. päsna- 'Ferse'; phlv. päsnak*^ ai. pdrsni-,
kurd. päsüne, päm, päme (ZDMG. 38, 55), päm (JJ.);
af/. pünda ; bei. pünzig, ptnz, n. pTz, pid (306) ; wa/.
päsna, sar. pu/nä 'Ferse'.
syr. LW. j^li/^B 'der Bimstein, mit welchem man
sich im Bade die Fersen reibt', de Lagarde, Ges.
Abh. 73.
277. päk 'rein', paktze,
ai. pavakd- 'rein, klar ; phlv. pak, päkih,
278. pälüden 'reinigen', Praes. pälay-em, päläyiden,
paiti + alüden (s. älüden^ No. 42) ; phlv. pälüt (Bund.),
päz. pälJdan, pälaidan (West, Sik. gum.-Gl.).
#### 3285,3300
erkannt. Die PehlevTform (PPGl.) kann man p(i)däz
padäz oder p(i)yäz, payäz lesen.
Danach wäre Geiger, Lautlehre des BalüöT, § 19, 2
zu berichtigen. Ich halte die sämmtlichen bei Geiger,
Etymologie des BalüöT No. 299, angeführten Formen
für persische Lehnworte*).
348. peyam ^Botschaft', peiyäm'^)^ peiyätnber , peyämber^
pelyember.
aw. ^paltigama- ; phlv. petäm^ pUcimbar (AV. ; y. 60
(11) Gl.), arm. LW. patgam, pntgamavor, mand. LW.
XDNn:n5, paz. peyam (PPGL).
*) Ein anderer Pilanzenname, in welchem d und y nebeneinander
stehen , ist püdene *Minze*, arab. LW. füdenej und füyenej (AM. 65
Zeile 3, 184 Zeile 8). Das ausserdem bei AM. 184 und anderweitig
überlieferte füfenej beruht nur auf falscher Punctation statt füyenejj.
*) Peiyäm und peyäm stehen unmittelbar nebeneinander Sahn.
I, 141 A^ers 223, 224.- 78 -
LW. kurd. peyamher; af;'. paiyämhar\ oss. t.
pa/umpar, d, pexompar; hei, paiyam^ paiyambar (207).
Ich möchte phlv. petäm für eine Verschreibung aus
patgätn ansehen.
#### 3395,3420
phlv. patkär 'Kampf (z. B. vd. 5 (33) GL), patkäritan
'Köcher, (z. B. vd. 4 (137)), patkärok (AV.).
arm. LW. payUar *Kampf' .
361. peiker *Bild'.
Sii^. patikara- 'Bild'; iphlv, patkar (Bund.), arm. LW.
pafker.
362. peikän 'Pfeilspitze, Pfeil'.
aw. paiti -\- [/kan- (?); arm. LW. paikan\daran
de Lagarde, No. 1834.
vergl. serb. LW. pHk 'Pfeilzeichen der fahrenden
Leute (Miklosich, Denkschr. WAW. Band 38, 11);
während peik 'Bote, Laufbursche' (ib. Band 35, 144
und 38, 11) zu np. peik (No. 359) gehört.
363. pei/imiden'mQ^^Gn\ zeigen', Prsies. peimäy-emj peimäny
peimäne^).
*) An der letzten Stelle wie auch sonst (z. B. IIT, 1642, Vers 2,
Calc, 1708, V. 3765) ist in der VuUers-Landauer'schen Ausgabe
h^ in p^ zu ändern.
«) Eine *Masft' (HohlmassJ, z. B. Jnnn ZKM. V, 302.— 81 —
aw. *paiti' -p l/^mö- ; phlv. patmay^d (AV.), patman,
patmänih^ patmänak 'Mass'.
kurd. piwdn messen; wa/. piHmiHam 'nachahmen,
nachmachen' (?).
)4. peiwesten ^vorbinden', Praes. peitvend-em, peiwend,
aw. "^paiti- 4- \/hnfid' (s. No. 219) ; phlv. patwastan,
patwand Band*.
kurd. pevandn *kleben .
55. plh *Talg, Fett', ^S (Is. 1, 11); vergl. ferhih (No. 813).
ap. ^pi^u-; aw. pitu- 'Speise*; phlv. pxh bezw. pih;
ai. pitü'. Vergl. np. ferbih (No. 813).
aw. pjvah' ^) 'Fett'; ai. pfvas- *Fett, Speck'; kurd. ptü
```


## [2026-09-14T00:54:24.818Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"^[0-9]+\\. (p|ä)\" HRN.txt | sed -n '1,200p' | grep -n -E \"2[6-9][0-9]\\.|3[0-9][0-9]\\.\" | head -60",
 "description": "Horn entry list p section"
}
```


### [2026-09-14T00:54:24.883Z] TOOL RESULT

```
44:2679:266. pädiSäh *König'.
45:2683:267. päde 'Heerde'^), padehan.
46:2685:268. pädyäb, pädyaw rituelle Waschung.
47:2688:269. pädyävend (i:ixnx5?, Is. 1, 31) 'kräftig'.
48:2691:270. pär 'das vergangene Jahr', pärsal^ parm.
49:2708:271. päre ^ück, Teil'.
50:2711:272. päzen *Bergziege*, päzen,
51:2714:273. päzehr 'Gegengift, Bezoar.
52:2716:274. päs 'Schutz*, pasban^ päsTden,
53:2724:275. päsu% 'Antwort'.
54:2728:276. päSne 'Ferse'.
55:2736:277. päk 'rein', paktze,
56:2738:278. pälüden 'reinigen', Praes. pälay-em, päläyiden,
57:2746:279. pälez 'Garten (Sahn. I, 73 Vers 207) ^), palezhan, arab.
58:2750:280. panzde 'fünfzehn , vergl. pänsed 'fünfhundert'.
59:2755:281. päl^ pä Tuss ; vergl. paye 'Stufe', päym.
60:2761:282. päyisten 'fest stellen , dauern ; erwarten ; vergl.
61:2785:283. päyi;^ 'Herbst*.
62:2791:284. petyäre 'Unglück' etc. (Vis und Rämin, Seite 81,
63:2795:285. pulten 'kochen, Praes. pez-em^ pezamden,
64:2804:286. pider (peder) 'Vater'.
65:2824:287. pidräm 'schön, fröhlich' (Sahn. III, 1803, V. 372).
66:2826:288. pedrad 'Heil, Lebewohl*.
67:2829:289. pedJd 'sichtbar.
68:2832:290. peölruften 'empfangen, annehmen', jüd.-pers. J nenne,
69:2839:291. peöfre entgegen*.
70:2843:292. per-, Praefix.
71:2850:293. perr Teder, Flügel*; pemden^ penden^ perend 'Vogel'^),
72:2876:295. perfuf enden zerstreuen; erschrecken, pergenden,
73:2880:296. pertew 'Glanz*.
74:2882:297. perdayten 'ausführen, ausleeren; streben, sich be-
75:2892:298. perest 'Verehrer , verehrend*, perestTde7i , perestür^
76:2897:299. pursTden 'fragen', pursis^).
77:2907:300. perrisiym^uS, perrisiyCLvesän ^) , 'Frauenhaar (Pflanze),
78:2912:301. pers 'Bach, Quell'.
79:2920:302. pergene 'Provinz, Distrikt'.
80:2923:303. peren 'gestern', perendös 'gestern Nacht'.
81:2934:304. pervär *Stair^).
82:2943:307. pervez 'siegreich*.
83:2946:308. pervfn 'Plejaden*.
84:2950:309. perhey(ten 'sich enthalten ; sich hüten', Praes. perliez-etn^
88:2987:313. pi^fnurden, pezmurden 'erschlaffen, verblühein', pilOTi:!
90:3019:315. pes 'hinter, nachher, pesin 'letzter.
91:3028:316. pest 'niedrig, nnoilN (Is. 2, 9; 11, 17).
92:3032:317. pistän 'Brust (der Frau)'.
93:3037:318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
94:3050:319. pesend zufrieden, angenehm', pesendlden.
95:3058:320. pist 'Mehr.
96:3068:322. pusek, pösek *Katze' ('Dialekt von Transoxanien' BQ.)^).
97:3086:323. peSenjTden, pisenjidefi ^besprengt werden ^), j)^^^^j^
98:3094:324. pegäh *Frühlicht, früher Morgen .
99:3096:325. pul^) 'Brücke.
100:3103:326. peleng 'Leopard'^).
101:3107:327. penUh 'Zuflucht, Schutz', penahlden 'Schutz suchen'.
102:3121:328. penj 'fünf*, penjum 'fünfter , peNje Taust'.
103:3128:329. penjäh 'fünfzig'.
104:3131:330. pend *Rat\
106:3140:332. penhän, pinhän Verborgen'.
107:3167:334. püde *faul, verfault', päsiden (Inchoat.) *faulen .
108:3172:335. poz 'Partie um die Nase* 2).
```


## [2026-09-14T00:54:32.064Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2824,2835p' HRN.txt\necho \"#### search padas\"; grep -n -i \"padas\\|pädas\\|pädäs\\|pätas\" HRN.txt | head\necho \"#### entries 336-372\"; grep -n -E \"^3[3-7][0-9]\\. \" HRN.txt | head -40\necho \"#### peyare\"; grep -n -i \"peyare\\|peyäre\\|pegäre\\|peiyäre\\|Schelte\" HRN.txt | head",
 "description": "Horn pidrām, pādāš, peyγāre"
}
```


### [2026-09-14T00:54:32.172Z] TOOL RESULT

```
287. pidräm 'schön, fröhlich' (Sahn. III, 1803, V. 372).
aw. *2)aiti.raman' ; vergl. np. räm (No. (504).
288. pedrad 'Heil, Lebewohl*.
phlv. pa i]^t) + drüt (Nöldeke, Kam. 65).
Vergl. np. durüd (No. 555).
289. pedJd 'sichtbar.
phlv. pa du {^\y\rr^^\ ps), Nöldeke, Karn. 40; also
aw. Sipa.dHi-,
290. peölruften 'empfangen, annehmen', jüd.-pers. J nenne,
Praes. peöJr-em, peSlr,
ap. *patit/ -f- i/^grufj-; phlv. patgriffan bezw.
«
#### search padas
2673:265^" pädäs, pädes (Vis und Rämin) 'Vergeltung', padast,
13212:pädäsf 265*>i'*.
#### entries 336-372
3131:330. pend *Rat\
3140:332. penhän, pinhän Verborgen'.
3158:333. inipü, püpe, püpek 'Wiedehopf; auch hühü etc.
3167:334. püde *faul, verfault', päsiden (Inchoat.) *faulen .
3172:335. poz 'Partie um die Nase* 2).
3180:336. pöziS 'Reue, Entschuldigung', pöztden (Vis und Kämm, ^
3192:337. pü^e Pfote .
3195:338. po8t 'Fell, Haut', pöstln,
3199:339. j>iifc, pwA: das Blasen (um Feuer anzufachen), Blase-
3210:340. puläd 'Stahl'.
3233:341. pehre *Wache\
3238:342. 2>ehlü 'Seite'; Stadt' (Sahn. 1, 104 Vers 793, 105
3248:343. peJilev, pehletan 'Held'^).
3251:344. peh/Ti' 'weit, breit', pehnä.
3257:345. {i)pei-, Praefix.
3265:346. {^)pei 'Fussspur, Fusstapfen*.
3274:347. piyäde Tussgänger, Fusssoldat*.
3291:348. peyam ^Botschaft', peiyäm'^)^ peiyätnber , peyämber^
3306:349. peiää^ offenbar, jüd.-pers. NT^5.
3313:350. plr alt, Greis', pTre,
3318:351. pfrär, pirar[sal *das vor vergangene Jahr.
3320:352. pmrästen schmücken, anordnen , Praes. peiray-em.
3323:353. perähen 'Hemd*.
3328:354. perö^, arab. LW. ß:rüz 'siegreich' ; j^frö^e 'Türkis,
3341:355. pes *Aussatz', pest leprös', pesl, pese Schecke*.
3377:357. 2^^'*^^ ^Handwerk, Gewerbe'.
3379:358. peiyäre 'Tadel' (Sahn. III, 1763, V. 95; 1803, V. 383)^).
3388:359. peig (peik) Tussgänger, Häscher, Bote', arab. faij,
3393:360. peikär, peigär *Kampf'.
3398:361. peiker *Bild'.
3401:362. peikän 'Pfeilspitze, Pfeil'.
3408:363. pei/imiden'mQ^^Gn\ zeigen', Prsies. peimäy-emj peimäny
3454:368. täyten *laufen; laufen machen (z.B. ab)\ Praes. täz-em,
3468:369. {i)tär 'Faden.
3471:370. {2)tär 'finster', tarik, I^nDDnND (Is. 50, 10).
3480:371. täze 'frisch'.
3484:372. täften 'brennen, wärmen, leuchten', Praes. täb-em,
3524:373. tal *Zweig, Stück\
3534:374. teber, tewer 'Beil', arab. LW. tabar,
3542:375. tejer 'Winterhaus mit Heizvorrichtung; Magazin*,
#### peyare
3379:358. peiyäre 'Tadel' (Sahn. III, 1763, V. 95; 1803, V. 383)^).
3579:*schmähen , tadeln , verachten*, tiraskära- 'Schelten,
9286:guväze 'Schmähung*, gtwäSzden, schelten' (unbelegt).
10980:vergl. säst 'Schelten, Vorwurf, Drohung, Unwille,
10981:Strenge', sastem schelten, drohen, einschärfen', sastik
```


## [2026-09-14T00:54:35.832Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2673,2680p' HRN.txt; echo \"---358\"; sed -n '3379,3393p' HRN.txt; echo \"---345 pei prefix\"; sed -n '3257,3266p' HRN.txt",
 "description": "Horn pādāš, peiyāre, pei- prefix"
}
```


### [2026-09-14T00:54:36.090Z] TOOL RESULT

```
265^" pädäs, pädes (Vis und Rämin) 'Vergeltung', padast,
pädosn,
phlv. pätdah(i)sn {paiti -f dah(i)sn), päz. pädaisn^
pädaän 'Vergeltung'.
Aus dem Pärsismus übernommenes Wort. Vergl.
np. dasen (No. 528).
266. pädiSäh *König'.
ap. "^pati/Säyadiya-; phlv. päta/sä^ bezw. päta/sah
---358
358. peiyäre 'Tadel' (Sahn. III, 1763, V. 95; 1803, V. 383)^).
aw. "^paiti + 2 [/"gar' (ai. praii + gar- bedeutet auch
nur 'anrufen, begrüssen, antworten).
Spiegel, Ar. Periode, 229.
Bartholomae meint, man könne auch an Ableitung
von ai. prati + [^har- denken (vergl. pratihdrana- und
die Bedeutung von lat. ohjicere), Ai. h entspricht ja
sowohl indogermanischem gji wie g2h,
peiyäni s. peyäm (No. 348).
359. peig (peik) Tussgänger, Häscher, Bote', arab. faij,
aw. "^padika-,
de Lagarde, Ges. Abh. 74; Nöldeke, Tabari-
Übers. 448, Note 2, vergl. auch Denkschr. WAW.
Band 38, 14.
360. peikär, peigär *Kampf'.
---345 pei prefix
345. {i)pei-, Praefix.
ap. patli/ 'zu, gegen etc.'; aw. paiti; phlv. pat-^ pät-
etc.; ai. präti.
Im Neupersischen erscheint das Praelix pati- als
pät\ pa\ pid% peö\ pei" {pe^),
*) Gehört hierher t. LW. balabän (statt *palabän) *gro88* (s. auch
Miklosich, Denksohr. WAW. Band 35, 255; 37, 10)? Für bala-
(*pala-) vergl. mäz. päli^ gel. pälü, kurd. päl (No. 342).- 77 -
346. {^)pei 'Fussspur, Fusstapfen*.
ap. vergl. ni\padiy *auf dem Fusse (nachfolgen)*;
```


## [2026-09-14T00:54:46.868Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== Horn mobed/herbed/sipehbed\"; grep -n -i \"möbed\\|mobed\\|herbed\\|herbud\\|sipehbed\\|spähbed\\|-bed\\b\" HRN.txt | head -12\necho \"=== Horn pes vor\"; grep -n -E \"^3?[0-9]*\\.? ?pes \" HRN.txt | head\ngrep -n \"'vor'\\|'vorn'\\|vorn,\\|voran\" HRN.txt | head -12",
 "description": "Horn -bed and pēš"
}
```


### [2026-09-14T00:54:46.940Z] TOOL RESULT

```
=== Horn mobed/herbed/sipehbed
2062:188. {2)-bed, -bud 'Herr* (Comp.), z. B. sipehbed, möbed,
8553:984. muy, möy 'Magier, Feueranbeter*^), möbed,
=== Horn pes vor
3019:315. pes 'hinter, nachher, pesin 'letzter.
3341:355. pes *Aussatz', pest leprös', pesl, pese Schecke*.
```


## [2026-09-14T00:54:49.321Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2062,2080p' HRN.txt; echo \"=== search 'pes' front around 356\"; sed -n '3360,3380p' HRN.txt",
 "description": "Horn 188 -bed and entry 356"
}
```


### [2026-09-14T00:54:49.377Z] TOOL RESULT

```
188. {2)-bed, -bud 'Herr* (Comp.), z. B. sipehbed, möbed,
hBrbud.
aw. paiti-, -paiti^ 'Herr ; phlv. pat, ^pat, arm. LW.
pet, -pet; ai. päti-, -pati-,
oss. LW. fätäg Tührer' (v. Stackeiberg ZDMG.
43, 672).
189. hidest, gidest 'Spanne'.
aw. vltasti- 'Spanne'; phlv. v(i)tast; skr. vitasti-
'Spanne*.
Das unbelegte np. audes, audest setzt ein aw.
*avatasti' voraus.
190. (\)ber 'Brust', vergl. ber a ber,
mäz. var; Käs. ver, ver ö vir.
aw. varah- (ZPGl.) 'Brust'; phlv. var,
kurd. LW.(?) ier; bei. gvar (135).
191. {2)ber, eber, auf, über, nahe bei' etc.; "ibN Is. 1, 1;
vergl. berm 'höchster 2).
*) Mohl übersetzt falsch durcli *mieux*.
2) Phlv. barin 'höchster*.— 45 —
=== search 'pes' front around 356
vd. 16 (17) GL; vd. 5 (48) Gl. unklar). Vergl. auch
piz-,
Joh. Schmidt, Pluralbildungen S. 359 flf., sieht in
ap. patis neben patiy, abis neben abii/j gr. djucplc; neben
dfLKpl 'ein neutrales Stammbildungssuffix s, welches
in der Ursprache mehrfach an vokalische daneben
erhaltene Stämme angefügt ist*. Anders Bartho-
lomae, Studien I. 75 Anmerk. 2.
^) Barth olomae macht mich darauf aufmerksam, dass aw. paitis
ganz unsicher sei: yt. 12, 3 habe Geldner paitisa gedruckt, yt. 5, 62
sei mit Fl Pt 1 P 13 ebenfalls paitisa zu lesen (die überschüssige
Silbe besagt nichts); es bleibe also nur yt. 3, 4. Er fasst paitisa als
einen adverbiell gebrauchten Instr. Sing., wie frasa^ apasa (s. LDMG.
43, 670).
*) Wa;^. petSy §i/n. pits *Angesicht, Miene' (S. 780) sind wohl nur
verdruckt statt pets^ pits; oder liegt eine durch den Bedeutungswechsel
verursachte Differenzierung vor?— 80 -
357. 2^^'*^^ ^Handwerk, Gewerbe'.
aw. vergl. pistro- 'Gewerbe*; phlv. pesak.
358. peiyäre 'Tadel' (Sahn. III, 1763, V. 95; 1803, V. 383)^).
aw. "^paiti + 2 [/"gar' (ai. praii + gar- bedeutet auch
```


## [2026-09-14T00:55:06.532Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3341,3362p' HRN.txt",
 "description": "Horn entry 356 pēš"
}
```


### [2026-09-14T00:55:06.578Z] TOOL RESULT

```
355. pes *Aussatz', pest leprös', pesl, pese Schecke*.
g. pTsk,
ap. madyaq = o Xengog (Ktesias bei Photius), niaadyai
corr. aus maoärai (Hesych); aw. paesa- aussätzig*
{zaranyö.pis-^ paesah- [pa^sa-) 'Schmuck', pacsa- *bunt
(Rind)', Bund.); phlv.^eS(/Ä*Aussatz', ^;^7.<?f^ geschmückt';
ai. pe^aS' 'Schmuck, Zierrat'.
kurd. pis^ pisa; af}'. pes, pesai 'Aussatz.
Vergl. de Lagarde, Ges. Abh. 75, 217, Hübsch-
mann ZDMG. 38, 426.
856. 2}es 'zuerst, zuvor, pester ^ j)Psin^ pesäm 'Stirn'.
ap. patis 'gegen'; aw. paitis^); phlv. pat(i)s-, pes,
pHäntk 'Stirn, arm. LW. patS\gam n()oardg fJfJ^^a.
wa/. pat^', pitS"^), sar. pac 'entgegen*.
LW. kurd. pU; bei. pes, n. pes^ pesa (302).
de Lagarde, Beitr. z. altb. Lex. 50; Pers. Studien,
74.
Als Praefix findet sich pes z. B. in peskär, peskes^ pes-
gäh, pes/^er (phlv. pat(i)sxur^ bezw. -/rar 'Tischtuch*,
vd. 16 (17) GL; vd. 5 (48) Gl. unklar). Vergl. auch
piz-,
Joh. Schmidt, Pluralbildungen S. 359 flf., sieht in
```


## [2026-09-14T00:55:11.825Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o -E \".{60}patiy.{200}\" KNT.txt | head -6\necho \"=== patis\"; grep -n -o -E \".{40}patiš.{150}\" KNT.txt | head -4",
 "description": "Kent Old Persian patiy"
}
```


### [2026-09-14T00:55:11.909Z] TOOL RESULT

```
1638:nating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48,
2404: imv. *o*hn-le, OP jata, and 3d sg. imf. mid. *egthn-lo, OP patiy-ajalà| imf. *eg*hen-m, OP ajanam, Skt. áhanam (with antevocalic de- velopment of m, $07.11), whence with the- matic vowel 3d рі. OP -ajana" in avajana* and perhaps the restored subjunctive 3d pl. i-J
2688:h the verb ‘to rule’ probably belongs here: DNa 18f adamSdm patiyarSayaty ‘I ruled over them; DNb 15 uvaipašiyahyā xšayamna ‘ruling over my own (impulses)'. D. Partitive, expressing the whole: DB 1.37f 1 The disappearance of dative forms in OP and the as- sumption 
3076:а, only in ava-parā; rādiy, in avahya-rddiy and separately; patiy, as enclitic postposition, as separate post- position, and also as preposition; -à, as formative of the locative case; kacã once (DB 1.50), separ- ately, governing a preceding enclitic. Position in t
3551: Kent, JAOS 62.274. 6 тагал KT, with omission of the d*. 55 patiydeahyaty Jn., KT. % Sika- lya]uvati$ KT. 6% abrieris RI, WB, Jn., KT. 606. {ү Ja., KT, for Rl's eéibeis[e]a; ef. Lex. for lit. on various normalizations and interpretations. ® Ву. MSLP 23.182-3 finds 
3586: à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : v
=== patis
3586:va : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara :
3586:itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā 
3747:àparam : hamiciya : hagmatà : paraità : patiš : Vivanam : hamaranam : cartana 66 iy : Gadutava : nàmà& : dahyáus : avadd : hamaranam : akunava : Auramazdima 67 iy : upastam : abara : vasnà : Aura
5641:atisam adv. ‘in addition’: extension of patiš, ef. for formation Ose. per-um ‘without’ to (Lt.) per, and for meaning Gk. трд ё ‘and besides’, Lit. atque from *ad-que ‘and thereto’ (OP patiy, Gk.
```


## [2026-09-14T00:55:16.839Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o -E \".{0,60}patiy (prep|adv|postpos|'|\\().{250}\" KNT.txt | head -5\necho \"---\"; sed -n '5636,5650p' KNT.txt",
 "description": "Kent lexicon patiy"
}
```


### [2026-09-14T00:55:21.206Z] TOOL RESULT

```
ugrep: error: error at position 104
pos|'|\()(?:[^\n\x80-\xbf][\x80-\xbf]*){250}
               exceeds complexity limits___/


---
LEXICON 195
kar- ($143.V). patikaram asm. DSn 1°. palikara apm. DB 4.71, 78, 77; DNa 41.
Patigraband- sb. ‘Patigrabana’, a town in Parthia: Elam. pat-t-ig-rdb-ba-na; from pati- + root grab- + suffix (833, $103.IV, §147.1). Pati- graband nsf. DB 3.4f.
Я patipadam phrasal adv. ($191.17) ‘on its base, in its own place’: pati- ($186, $1401) + aec. padam (see pada-; 76.111, $122). DB 1.62.
palis prep. with acc. ‘against’: pati- + adv. -s, ef. Lt. ex, abs, ops- in os-lendó, sups- in sus-tined, Skt. nt and nis, Gk. ато iy, audi audis. See also patisam. DB 1.93; 2.33, 38, 43f, 52f, 58, 67; 3.36, 43, 65.
patisam adv. ‘in addition’: extension of patiš, ef. for formation Ose. per-um ‘without’ to (Lt.) per, and for meaning Gk. трд ё ‘and besides’, Lit. atque from *ad-que ‘and thereto’ (OP patiy, Gk. тро, Lt. ad agree in marking something as an ad- dition). patišam DB 4.89 (p* probable but not certain KT); (раат DB 4.90 (restoration of Konig, Klotho 4.45; see also Kent, JAOS 62.267- 8).
Pàtiwvari- adj. ‘Patischorian’ ($167): Elam. ba-ul-ti-i$-mar-ri4$, АКК. pa-id-di-if-hu-ri-i$, Gk. (рі) llaracxopes. Perhaps pAr. *pati-, with vriddhi ($126), + *suára- ‘(of the plain) before the Hvara Mts.’ ($117), with combination (8$140.VI) of sandhi forms (so Hz. ApI 183-4, who however disregards the d in the penult of the OP). Ран паті nsm. DNe 1.
. раві- sb. ‘path, way’ (676.1, §152.1, $179. III): Av. pab- patá-, Skt. panthan- path-. райт asf. DNa 58.
pad- sb. ‘foot’: Av. Skt. pad-, Gk. roô-, Lt. ped- ($142); in mipadiy, cf. also pada-, páda-, pasti-.
pada- sb. 'footing, step, station': Av. paóa- ‘foot (as measure)’, Skt. padd- ‘step, footstep, place’, Gk. aé&ov ‘ground’; extension of pad- ($143.- П). In Garmapada-, patipadam; see also pad-, рӣйо-.
рӣйа- sb. ‘foot’: LAv. páóa- ‘step, pace’, Skt. pida- ‘foot’, Gt. fotu-, extension of stem in pIE nom. *pdd-s, acc. *pod-m, seen in Gk. Dor. тах ($76.11, §122, $126, $148.П). Cf. also pad-, pada-. püdaibiyà idm. ($189) DNb 41.
par- vb. ‘communicate’: Av. *par- ‘hindureh-, hintibergehen’ (ВЕ. AYW 851), Gk. weipw ‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- іаїу| nsn. past pte. pass. ($242.1) DNb 54 (dubious con]. of Kent, Lg. 15.167, 178-4).
ipara- adj. ‘later’, possibly in hyáparam (q.v.) : Av. para- ‘farther’, Skt. pára- ‘distant’, Gk. qépav ‘beyond’.
nara prep. with acc. ‘beyond’ (§32, $63.1): Av. pard ‘before’, Skt. purds ‘before’, Gk. таро ‘before’; DPe 15; DPh 5; DH 4, See also para- dayadàm, paradraya.
parü postpos. with acc. ‘along’, and verbal prefix ‘forth’ ($132.3): Av. ?pará ‘before’, Skt. purá ‘before, formerly’, Gk. rapá ‘alongside’: in avapard and with ay-, ar-, gam-, bar-.
```


## [2026-09-14T00:55:27.574Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"paiti\" BRT.txt | grep -n -i \"Herr\\|Präp\\|Praep\\|gegen\" | head -20",
 "description": "Bartholomae paiti main entries"
}
```


### [2026-09-14T00:55:27.629Z] TOOL RESULT

```
38:3003:—  at  ..  dr?grai5  akäU  ^arihäii  (sd.)  •  j-  aka'tara-  Adj.  '(der  bösere,)  beson- paitiurvanöpaityeintl\.40-i\.  a)mitjders,  überaus  böse  (in  Wille  und  Tat) DaL  'Jmdm.  (gegenüber)  böse  (in  Wille  gegenüber-'  (Gen.)":  mtirim  ..  kam}- und  Tat)"':  tum  -kö  rahislasla  mi^ra  rs'.ö.jamm  daevanam  'nm  sraosyanqm ahi  masyJkaHbyS  "du  bist  (je  nachdem)  "■  ■  der  denen  überaus  böse  ist,  die  sich böse  und  (auch)  sehr  gut  gegenüber  den ,  strafbar  machen  .  ."  Yt.  10. 26. Menschen,  a  M»  Yt. /o.agijg;  — oiS«/«|  "  ^e'-  '"*"■  «■  F»Isch  KZ.  jo.  517. klil  {hd.)  aahat  ..  -kb  dngväitl  Y.47.  •  j-  aka'tas-  m.  Name  emes  Daiva: A)   in    religiös-moralischem    Sinn:  °tahm  daium  Y. 10.13,  '5  43-
86:4653:vorausg.  nagclm  und  la-  'nicht  irgend  ein anderer';  naSclm  tsm  'nySm  yOsmat  vasdä asa  "ich  kenne  nicht  irgend  einen  andern als  euch,  0  Asä"  Y.  j^7">.  II  a)  mit AbL  des  Verglichenen:  ttsit  mSi  vaiiä(sd.) x/mai  *nyS  Y.  2g.  1 ;  ^0. 1 ;  —  h3m  tta mavaitl  payBm  dadat  'nyJm  %wahmat a^rasciJ  ..Y.46.J;  34.7.  ni)  'alienus', a)  im  Gegensatz  zu  'eigen':  nsii  hl  'iiys ttrva  kaom  urvantm  paiti  irista  bqzaiti V.  y,  9'";  — jahikayai  ya  aom  pu>^r»m baraiti  'nyahmai  arsänai  varit»m  pai'^e apa.baraiti(sd.)Ytij.s8.  b), lim  Gegen- satz zu  'heimisch',  sva.  'hostis':  yadiy  ava'ia *maniyähay  hacä  'niyaria  (iS.)  ma  tarsam ".  ,  vor  keinem  Feind  will  ich  mich  zu fürchten  haben"  D.5,3;  D.4.2;  —  karam tyam  ..ajanam  vasiy  'iiiyJ'  apiy3*ahyaiä (sd)  Bh.  j.  19.  IV)  In  ungenauer  Aus- drucksweise; das  mit  a'  Bezeichnete  ist dem  Vorausgehenden,  dem  es  gegenüber- gestellt wird,  nicht  gleichartig'J':  daat {taeta)  -nyatsam  rähwqm  paiti.maydi^i^d^
87:4691:•  j.  a-mainlinna-  Adj.  'der  nicht  (daran) denkt',  mit  mananhö  'im  Sinn"':  kakmsi asim  uyr»m  x/a^rpm  ,  .  'nahe  (statt  DS.) mananho  paitiJa^äni  "wem  soll  ich  eine starke  Herrschaft  zuweisen,  ohne  dass  et in  seinem  Sinn  daran  denkt?"  Yt.ro.  119.
91:4797:mit  aoi  und  paiti  'zurückkehren,  sich zurückwenden  gegen  -  (Akk.)':  yö  tayui ..  tsm  aoi  ibaiSa  pattyantv  ..  t'hyeja yatitu yS  t  daoa  "wer..,  gegen  den  zurück  sollen sich  die  Feindseligkeiten  wenden,  . .  sollen sich  die  Gefahren  wenden  (gegen  den,) der  sie  hervorgerufen  hat"  Y.  65. 8.
106:4965:aJs dessen  Konelat:  avam  käram..  °vaAya ksrahyä  .  .  tyam  z-ohyazdaiJ*  /räilayi^ Bh.5.  lof.;  —  nadi'tahaire^  .  .  udafiatata .  .  fasäve^  adam  .  .  asiyavam  abiy  "vam nadi'tabairam  kyi^  nabitkadrai'ari^  agau- batä  Bh. /. i6- 1 8;_j.  3, g,  14, 2. 4. 1  b) sub- stantivisch, auch  im  Sinn  unsres  schwach- tonigen  'er':  t3m  lafmeii . .  yatata  ahurö maxda , ,  aom  Jai'iyat  Yt  ^5. 1  —  3 ;  —  I  gau- mat^  . .  hauv  udapaiata  . .  pasäv<^  ATru* aHy..'vam  asiyav^  Bh.;.ii;  —  *utilmaiy amyaiiiy  vasiy  astiy  kartam  °v<^  .  .  naiy nifistam  Bh.  4.8;  —  tuvam  ks  hyc^ imäm  dipim  vainahy  .  .  imatvä  patikarä . .  yävä  (sd.)  *taumä  *ahatiy  *äva  °vaiy pariiarä  Bh.4-i5;  — ya'^a  «J  snaihi^. paiti.vaiaMt  'vat  paiti.päpayamnS  "..eine Waffe  .  ^  sich  dagegen  zu  decken  suchend' P.  2/;  —  afavatum  mahrka'^ni  aon äinrnta  strmca(sd.)\t ip.12.  a)l'insbes. ein  Nomen,  das  —  zum  selben  Satz  gc- höiig  —  sammt  Zubehör  unmittelbar Toraosgeht:  kSram  tyam  hamii'iyam  kyeT
114:5259:mit  paili  'sich  feindlich  wenden,  auf- treten gegen  — '  (Akk.) :  yS  mä  dr»gvä  %viä savä  (sd.)  paitianti  \.  44.12  '";  —  'paiii.- inta-,  s.  ap°;  —  s.  noch  Inf.
139:5982:i)  'treiben,  wegtreiben,  wegschleppen' (Vieh   und  Gefangene   als   Kriegsbeute): jvU  gqm  *vani(rm  (sd.)  aznUe'W.  S-Zl ', —   ' ya  {gäu^  varÄa  (sd.)  azimna  (Pass.)  Yt.  . ;o.86;    —    kaoa    nS  fraourvaesayälti  . drujö  vaismmda  a z;/ mn a m  (APm.)  "wann wird  er  uns,   die  zur  Wohnung  der  Dr.  ,  j.^  g,  azan-  :  asn-'^  n.  'Tag',  im  Gegens. hinweggetriebenen  (Rinder)  . ."  Yt/o.86;,2ur  Nacht:  pat/i  'sai paiti  xsa/ne  Yt./.g,
151:6271:—  '/äum  spitama  Yt.5.89,  91,  72.2,  77. 21.  aa)  auch  kät'  i^.  (ohne  Nennung des  Namens,  s.  i  a  a):  paiti  dim  psr»sat 'hva  asäum  afiura  masda  .  .  äat  mraot ahurS  mazdä  axtm  bä  tl  tat  fratnraväni ,  .  asäum  spitama  Yt  72.  i  f.  ß)  Sing. koU.  sva.  die  gläubige  Gemeinde  im  Gegen- satz zum  amtirenden  Zaotar^^:  ya^ä  ahU vairyS  saota  (sd.)  fra  ml  mrüti  .  .  a^ä ratus  .  .  fra  °lava  vütva  mraotu  Y.j. 25.  f)  GP-  mit  fravasay-  (sd.,  auch fdSt):  'laonqm  {'launqm)  JravalayS  Y. 2.6,  Yt  7^.1,  usw.  0)  insbes.  mit  nar-'>> m.  und  näirl-'^^,  näirikä-'>'>  t  'der,  die Gläubige',  von  den  erwachsenen  Mitglie- dern der  zara^ustnscAitn  Religionsgemein- schaft; Sing,  und  Plur.:  narsm  'savatum ys  anhat .  .  mqhr^m  p}r>sS  'sava  V.5.2;
167:6706:mit  pai/i*i>  1 ) 'sich  gegenüber  befinden', mit  Dat.:  paitica  As  anya  dva  vä  nara atsAm  .  .  "und  (wenn)  sich  ihnen  gegen- über zwei  andre  Männer  befinden  oder  .  ." ¥.5.27.  2)  'entgegenkommen' (?)  r  jaä-a astis  (sd.)  pailyaAmi  F.  4  a.
173:6963:ausgehendem) cä:  ahmäkSiig  .  .  urunS pasukanqmcä  .  .  yalibyascä  tut  S  yas^ä agibyö  ä  at3k?n  ".  .  fiir  welche  diese  und welche  für  diese  dasind"  Y._jp.i.  a)  zu- gleich gegenüberstellend  'atque  tarnen': yß  .  .  paiti.hincaiti  a  dim  (sd.)  nBit  api- vatäitt  daStiaya  ..  V.g.^z.  II)  Praen.*'* i)  mitAkk.;  a)  räumlich,  a)  'hin  zu  — ,  hin gegen  — ':  ia'^a  drupin  nls  ahmat  3  rtis rtäsämä  (sd.)  tSng  3  avä  yöi  . .  Y,  44. 1 3 ; 11;  —  iaoa  riS  tba  . .  agats  i^yejankatal haca  atjhagt  atiyajafthim  ahUm  3  V,  ir). 31;  7.52,  Yt/.i7; — apänS  (%A.)  t
184:7223:—  V3r>-ir(^imn  . .  ya  . .  aca  paraca  pirs- saite  Yt.  j^.47.  2)  anschliessead  'dazu, dazu  auch,  und  auch';  aStS  sl  vSxs  .  . */ramrvqriö  ä  vacS  aAuriS  vairyö  fraoxtS .  ,  spanvaitti  H,7,4;  —  hil  hama  pairi- süite  fräpaya  (sd.)  datikus  ä  upaosatih- väsca  Yt  /p.  1 ;  —  yi  ä  axti/  ahinäi  ySm axfSyöi  (sd.)  dSn/ig  Y.jÖ.i;  —  >wsi  as *ärmaitis  "^wS  ä  gPui  tasäi^i.)  as  Y.^i. 9,  a)  wiederholt  'et  .  ,  et',  nach- gestellt: ahunm  masdqm  ämruyi  (sd.) nmänahe  mitandpatSis  ratum  ä  vXsS  vTspa- töil  ratßm  ä'  .  .  daitihupatöis  ratüm  a Y.  13. 1.  a)  in  Verbindung  mit  (vor- ausgehendem) cä:  ahmClkSng  ,  .  urunö pasukanqincä  ,  .  yaHbyascä  tsi  ä  yascii aHbyö  ä  arfh)n  ".  .  für  welche  diese  und welche  für  diese  da  sind"  Y.  J5.  i.  a)  zu- gleich gegenüberstellend  'atque  tarnen': yS  .  .  paiti.hincaiti  ä  dim  (sd,)  mit  api- vatäite  daSnaya  ..  V.p.52.  II)  Praen.** i)  mitAkk.;  a)  räumlich,  o)  'hin  zu  ~,  hin gegen  — ':  ka'i:il  drupm  nls  ahmat  ä  nts näiiimä  (sd.)  fff^  ii  avä  yöi  . .  Y.44.13; 11;  —  iaoa  nö  ioa  . .  agats  iäiycjatjhatat haca  anhaot  aikyajaiiksin  ahüm  3  V.  iq.
191:7361:—  upa.barat  "tim  Vyt.jiV;  —  ix^a/imi dam  . .  aire  . .  ^ahmi  't.m  yat  ahurahe mazäii  Vr.  14. 2  (?).  2)  Plur."  'GlUcks- güter,  Herrlichkeiten,  Wonnen,  fehcitates': tiltrlm  .  .  isänim  hataaräi  °tanqm  yO daoäiti  ..  'lä  jairiyantiJi  Yt.  Ä  49;  —  vts- panqmca  paiti  'tanqm  Yty,  t35;  — yat da'iat    'ta    Vyt  25;    —    viT.H>rpm    dtm
201:8055:•  j.  iSHe  Inf.  'Herr  zu  sein  über  — Besitz  zu  kommen  von  — ':  jamyqn  i^ra . .  /ravalayö  . .  i°  *vari/ianAqm  paitistaiSe ätaranqm  frala.vax^Si  rayqmca  »farma- »kqmca  "her  (ins  Haus)'>  soUen  sie  kom-
209:8471:'  'um  "ranqm  uzuxfyenlinam  srlranqm zairi^aoiianqm  vaxsA  (sd.)  apayasaite  V. /Ä63;  Yt. /Ä6;  —  at  aRyäi  (näml.  dem Rind)  mazdä.  'rä  vaxiaj  (sd.)  Y.4S.6;  — avi  racynyq/H  varauhmt  azuitlmca  'ranam Yt.  ^2.3;  —  nima  'vaire  (VS.)  varMhi masdaöäte  asaone'V.  ig.ii;  Vyt.22,  N.7/, f)7.  a)  Plut.,  im  Gegens.  zu  alxa-  Plur., 'pflanzenbewachsener Boden';  ahond  una 'rlhuca  paiti  *baooisca  vTdtnanmnS  saoa- yäti  . .  ärvatS  urva  *aexahuea  (sd.) . .  "der Seele  des  Gläubigen  ist  es  so,  als  ob  sie auf  Wiesengiund  (stehe)  und  Wohlgerüche empfinde,  .."H.  2. 7— 25.  b)  sva, 'Baum', a)  im  Gegens.  zu  var^ä-.  pairi  van>'>iJ- byasca  'räbyas^a  atsmaiibyS  (sd.)  V.  16. s.  ß)  sonst:  v3r»ynahe  . .  yS  .  .  sainif marisat  'ranqm  ". .  der ..  im  Flug  der  Bäume Wipfel  streift'"  Yt./.4.2i''.  c)  'Pflanzen- Stengel,  Reis':  yavat  akmUi  paitinqm •ranqm  aetavat . .  "so  viel  es  ihm  einzelne Reiser  gibt,  (als  ob)  er  so  viel  .  ."  V.  iV. 86,  a)  bes.    der   zum  Barisman    ge-
235:9484:•  g.  kä^e  Inf,  mit  asii  'er  erweist  leisten,  aufkommen  für  — '  (Akk.):  yas:t Liebes',  mit  Dat.:  kasJuscii  nä  asäunS  tat  .  .  tsyus  vä  v»hrks  vä  haca  gae^sbyS k°  anhat  isi-ilcft{s(i.)  hqs  paraol  akö  dr?g-  para.baraiti  dasa  (sd.)  üö;?/  paiti  afis väitt  "man  soll  dem  .^j-iianhänger  Liebes  cikayat'l  ".  .  so  soll  er  dann  für  den erweisen,  aber  böse  sein  gegen  den  ZJ«/^-  Schaden  aufkommen"  V,  ;j.  lo. genossen"  V.  47. 4.  mit  para   dnwS.     i)  para    hg*iriilr:tB
238:9547:('Leichnam':  nDrfjtm  ..  upa  tarn  'ptm ' fratauharaitl  yqm  iristake  maiyeheV.^.x; ' — pqslö./ra'^a?»h»m  (sd.)  Al  kam?r?}.»m Ivinä^ay^n  ..  as.:^arft3maEiby3  ..*k3r»ß.- ifarqm  '/s  (als  Akk.)*'  paiti  nisirinuyJl \va\)qm  .  ,'^. 3.20;  —  yd  nar!  asaonö 1  iriri>usö  z»m  -pa  (statt  AS.)  nikainti  V. j.  40  PüZ.;  —  ma:dayasrta  aStsm  'pim hvarp-dansim  (sd.)  k?rjiiavqn  V.  5.  13; 14;  —  s.  noch  KompA.  a)  im  Gegen- satz zu  urvan-,  matiah-,  ifvTsl-:  ahurahe mazda  . .  yeähe  urfa  . .  "pas.'a  (NP.)  y3 ral^wayeiti  (sd.)  .  .  Yt  13.  81;  —  yö aSnatthaiti  nö  maiiS ,  .  nB  'p?m  Y.  9.  ag; —  frä  tS  'p»mca  imulmca  yao'zda'^äni V.3i,6;  —  ima  'pasca  tn-lsls:a  Vr.j/,3; Y.  55.  1.  3)    von   Tieren:  yal  barata
247:9980:mit  paiti,  patiy  i)  '(eine  Schlagwaffe) schlagen  gegen  — ,  auf—'  (Akk.):  paiti azöii  .  .  k)hrp>m  .  .  i<adar?  (sd.)  jat-it  Y. ^■30;    30-32*.  i)    'zurückschlagen':
248:9981:nSmSni  aeSam  drujinqm  .  .  paiti.janaiti*'' Yt.4. 7.  3)  Med.  a)  II  'sich  wehren gegen  --,  bekämpfen',  mit  Akk.:  pärst^ martiy^  ^duraiyapiy  kacä  pitrsil^  hama- ram  (sd.)  patiyajatä  (3SPrM.)"  D.  ti. 4.  b)  'sich  wehren  um  — ,  kämpfen um  — ',  mit  kala  und  Abt.:  ya'ia  nä taxmö  . .  kus.kqm.bfr?tal  kam  laität  (sd.) . .  paiti.ynita  (3SOM.)  Yt.  13. 67.
253:10044:Tmtpaiti  i)  'entgegengehen,  sich  wen- den gegen  — ';  a)  mit  Akk.:  vTsp»m  paiti usanhim  ..hazaaraja  (.y&ssA.dqma)  *ar?rö.~ mainyus{W.)  paiti.Jasaiti  V./ j.i.  b)mit Dat.;  miitvm  .  .  yet^he  hazar»nm  vaFja- nqm  paiti  katmrg'^äi  jasaiti  Yt  W.  69 ;  —  s. noch  Inf.  c)  absolut  'dagegen  angehen, als  Ausgleich  (einer  Schuld)  dienen':  aiia zaokra  palti.jamyat  Y.6S.1.  2)  'zurück- kommen, -kehren  zu  — '  (Dat):  iala  nS abmai  asanbalca  .  .  paiti.jasatö  (3DK.) isaca  ozuitiica  V.^.  54;  55,  57.  a)  ab-
259:10052:mit  paiti  und  kam  Med.  'sich  gegen einander  aufsammeln,  aufsummiren,  gegen einander  zur  Abrechnung  kommen':  kva tu  daira  paiti  *hsnjas?iite  V,  ig.  27.
```


## [2026-09-14T00:55:34.536Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"paiti\" BRT.txt | grep -E \"Herr\" | head -10\necho \"=== paiti.kan / paiti.gam\"\ngrep -n \"paiti\\.kan\\|paiti\\.gam\\|paitigam\\|paiti\\.man\\|paiti\\.mrav\\|paiti\\.rae\\|paitiraec\" BRT.txt | head -10\necho \"=== p.r.t Kampf\"\ngrep -n \"Kampf\" BRT.txt | head -20",
 "description": "Bartholomae targeted"
}
```


### [2026-09-14T00:55:34.616Z] TOOL RESULT

```
4691:•  j.  a-mainlinna-  Adj.  'der  nicht  (daran) denkt',  mit  mananhö  'im  Sinn"':  kakmsi asim  uyr»m  x/a^rpm  ,  .  'nahe  (statt  DS.) mananho  paitiJa^äni  "wem  soll  ich  eine starke  Herrschaft  zuweisen,  ohne  dass  et in  seinem  Sinn  daran  denkt?"  Yt.ro.  119.
7361:—  upa.barat  "tim  Vyt.jiV;  —  ix^a/imi dam  . .  aire  . .  ^ahmi  't.m  yat  ahurahe mazäii  Vr.  14. 2  (?).  2)  Plur."  'GlUcks- güter,  Herrlichkeiten,  Wonnen,  fehcitates': tiltrlm  .  .  isänim  hataaräi  °tanqm  yO daoäiti  ..  'lä  jairiyantiJi  Yt.  Ä  49;  —  vts- panqmca  paiti  'tanqm  Yty,  t35;  — yat da'iat    'ta    Vyt  25;    —    viT.H>rpm    dtm
8055:•  j.  iSHe  Inf.  'Herr  zu  sein  über  — Besitz  zu  kommen  von  — ':  jamyqn  i^ra . .  /ravalayö  . .  i°  *vari/ianAqm  paitistaiSe ätaranqm  frala.vax^Si  rayqmca  »farma- »kqmca  "her  (ins  Haus)'>  soUen  sie  kom-
10711:j.,  g.  xäaSra-,  p.  xSsO-'a-  n.  'imperium, regnum,  Herrschaft,  Reich';  uzw.  im  Sinn von  1)  "Herrschgewalt,  Obergewalt,  Herr- schermacht'"; i)  I  im  Ap.:  c^ur^mazdä h'am  mann  fmbara''  Bh./.s,i3;  9,  'D.4. 1,17. 1 ;  —  °^^am  iyt^  bäbirauv  hauv  agar- blyaiiJ  Bh.7.  16;  11';  —  vasnä  a^urO^- mazdäA^  imJ'  °h''am  därayämiy  Bh.  /. 9;  9;  —  °'ii''amiim  adam  adlnant  Bh./. 13;  i3i  —  "''"*  "ä'^'»'«  fy<^  gaumätc^ ty^  maguS  üdin^  ia''bBßyam  aitJ'  ''i'aiii ha'ä  paruviyata''  amäxam  taumäya  aha Bh./.i2;  —  '^'am  tyJ" ..paräbarfam  aha^ .  .patipadam  akunavam  Bh.  /.  1 4.  ||  2)  im jAw.T  uparäi  amäi  .  .  v»r?'hrSi  ..  °%räi A.  /.  8;  —  '%rakela  paiti  bäiiumais  dan- yayasca  paiti  darr^S.jXtSiS  Yt  y.  135; —  ''%r)mca  paiti.astlmca  darrfö.xsa^rfin "'hrahe  darr^5.j.ttJm  ustanahe  A.  /.  8;  — yim3  asti  hr.?>e(s6.}  '^rayä  (GD,)  V.  2. -  ^ahmi  '>re  Vr. /^_2(P);  P.  2^; — yimahe  °&re  nSit  aotftn  SnHa  .  .  yavata xsaySit  (sd.)  . ,  "unter  Ks  Herrschaft  .  ," Y.^.j;  V.2.S; — yim?m  . .  ye/'jhe  ''^rula .  .  nöit  aottm  fff»ha  . .  para  ahmSl  yat . . Yt.  IQ.  33 ;  —  yimS  . .  yat  kirmaot  aiähe '"ifräha  *amarsanta  pasu  vira  Y.g.  4;  Yt 15. 16; — Auxsa'hrS.ttmaiät  al  ""kmin  äfyai A.J.6;  —  zard^ustrim  ..ya^  as  ..*%rfm huxsa^rJ.ümS  (sd.)  \t  1^.79;  A.^.4,  Vs. 5^_j; —  'ir.lt  xsayamiia  VytJ5;  — yal^a anyhsBt  ""^räl  xlayamnä  hatnö-xiahrS.- xiayamnS  Yt.  J5.  54;  —  As  araHwya  '"^ra nsit  xiayeti  Vyt  47;  —  us  nü  atühäi  vJse jamyäl  asimea  "'hrsmca  savasca  .  .  Y.  60. 2;  —  zaraiiultrahe  ,  ,  paoiryai  hanhanuse gqrnifa  ahmla  .  .  uxüahyäca  (sd.)  i
10833:yavata  xiayöiliz^ViA.)  ..yimS  "so  lang  Y, die  Herrschaft  führte"  Y.p.  5;  —  mi^nm ..  xsayant^m  xsayamnem  Yt /O.  35; 5.49,  Vyt2;(?);  —  ahurahe  xsayatö (GS.)  Ytrj.  63;  78;  —  xHyammm ('gebietend')  asnvamm  däyata  *axsyamn3m (sd.)  drtanlsmY.8.$; — yd>a  Almjanama xsayamnö{^^.)^1  *axsyamnqm  Y,6j.s;Yt 10. 101,  F.  5;  —  xsayamna  *apaitijr)ta F.jh;  —  xiayanlascä  *ax^yantasca{%^) Y-,3'5-4;  —  cvqs  främraoi  /ravakunf vaMstB  xsayamnd  Y.  1^.10;  —  xsayqs mazda  aAurS  Y. Si.iT,  —  xsayäa  Vyt. 47  (?)■  a)  in  Verbindung  mit  xsa>ra- : t^narS  xsa'hra  (AP.)  xs'ayen/eYt  ly.T, — Aäu  ara^wya  x/aira  nSit  xsayett  Vyt 47(^)1 — xsa^raj  xsayamna  Vyt_j5;  — yaia  anyasai  x/airSJ  x/ayamni  hamS.- xsa'i^rS.xiayamna  Yt.  75.  54(?).
11082:(yascd),  V,?.  70,  ij.4  (ymca);  —  iäsca imä  nämSnJs  "so  lauten  die  Namen" Vt  /.  15;  75.  49;  —  Hsca  caraitis  ahi yqm  ..  H.2.  io(?).  Anhang.  Ellipse ist  anzunehmen  für  gAw.:  vaidä  tat  ya ahmT  .  ,  anales  (sd)  tna  kamnafsva  (sd.) hyatlä  iamnänä  (sd.)  ahmT  "ich  weiss  das, weshalb  ich  , .  nichts  vermag;  nur  wenig Herden  sind  mein,  (deshalb  ist  es  so) und  weil  ich  nur  wenig  Leute  habe"  Y. 46. 2.  C)  In  der  Bedeutung  unsres 'auch';  ca  folgt  dem  angeknüpften  Satz- teil, bz.  dessen  erstem  Wort.  B)im  Aw.; 'auch'  hat  den  Sinn  von  i)  'ebenso,  eben- falls, nicht  minder' :  ^<«ji  mi^r>m..yazai vasram  .  .  yasäi  Aojoörpmi^a  yat  attt  . . Yt  6'.  5;  —  mai  vi  padäis{si.)  . .  paiti- fasai  .  ■  al  va  aridrahyala  n>manha  at vi  ..  AunarptatäY-SO.S;  —  tara^uänm ..hyathei  Im  caratasca{Sf.$(>$M.)aodiir?f^ä sSiS?na  vazä  V.jr.ia.  a)  Ellipse  liegt  vor in  gAw.:  vahiSta  tstii' {sA)  , .  tara%usttake .  .  yezT  hsi  dat  ayaptä  . .  ahurö . .  hvaivhf- vlm  (sd)  yaZcä  hsi  dabm  .  .  ". .  des  Z.: dass  ihm  nämlich  AA. ..  die  Herrlichkeiten verleihen  wird  . .  (So)  auch  denen,  die . ." Y,  $3.  I.  a)    'überdies,    ausserdem':
12701:•  j.  daÜhu-patay-')  m-  'Herr,  Gebieter einer  Provioz,  eines  Landes,  Landesherr'; i)  im  eig.  Sinn:  a!%rapatay3  .  .  *°tayS Aog.59;  —  va%ayanö  'paitts  V.  ig.  6 Yt.  15.  31;  —  yim  yazmte  "tayö  arjzahe ttva.jaspras  Yl  JO.  8;  —  ahurö  ^sästrfnqm •paiHl  Yt.  J^  37;  —  akuranhS  'tayS pu%ränhs  'paitinqm  Yt,  5. 8  5 ;  —  ä/rlitami tava  nara  ••paiti(VS.)Az.i;  A.i.8.  a)  mit Gen.  aus  ^Xyav,  daiAAav-.  nmanaAe  va KMätuspaitil  .  .  daijihfui  va  "paitis  Yt 10.18;  83,  l6.\%  VyL46';  —  dai^hsus yatffiM  Vr.J.  3,  V.  7.41,5.37;  —  daiMiuf •mVV.iO.S,  Y.y.  I,  Vyl-iö;  —  liairihSus 'tSe  Yt  /o.  17;  —  da/ryunam  'pattil (AP.)  Yt  /O.  18;  —  äaiAhyui  'painm*> nSirikqm  "die  Frau  ebes  Landesherrn" V.  7,  4a.  2)    von   Göttern;    a)    von
16484:•  j.  baevar9.patay-  ni.  'Herr  Über  Zehn- tausend": pu%rar»hs  'tayd  Yt.  r^.  59;  — ää'iunqm  'paitinqm ''  Yt.  13. 38.
19342:•  j.  lunänö-padni-,  d^m^ö-paSni-'*  f. 'Herrin,  Gebieterin  eines  Hauses,  Haus- herrin'; nmänS paitil .  .  'm  vä  V.  72.  7;  F. 2  f.;  —  d»mqn5pa%ttiY.2i.  a)  mit  Gen. aus  nmäna- :  nmänahe  "nTm  Vr.  J.  3 ;  —  nmä- nahe '^nyä  Yyt.1-;.
24419:•  j,  vis-patay-''  m.  'Herr,  Gebieter  eines Dorfes,  einer  Gemeine;  Gemeindeherr'; a)  im  eig.  Sinn,  mit  Gen.  von  vis-''' :  nmanahe va  nmanö.paitii  vTsB  vä  'paitis  zantSu^  vä zantupaitis  daiähSui  vü  daitihupaiti/  Yt. io.  18;  84;  —  vTsö  •paitim  Vr.j.  2,  V. 7- 41, 9-ZT,  —  viss  'isi/  V. !o.  5,  Y.  13.  i, Vyt/o;  —  vTsU'tJe  Yt/0. 17;  —  visqm 'paitis  {KV.)  Yl/0.  18;  —  vujs 'pttihm ftilirikqm  V.  7.  42  3'.  b)  von  Göttern : kaoma  nmStUS.paitt  'patte  .  .  Y.p.27;  — mihnm  ..  taxnam  'pattlm^'  YLJO.112.
=== paiti.kan / paiti.gam
14775:•  j.  tbaeäö.par^ta-  Adj.  'aus  Feindschaft, in  feindseliger  Absicht  gefragt':  uia  hl fraiha  (sd.)  paiti.mravSne  navaca  navai- tXmla  xruidranqm  °tanqm  yat  mqtn  p»r>- sai ..  "..  auf  die  99  schwierigen,  in  feind- seliger Absicht  gefragten  (Fragen),  wenn  . ." Ytj.  82'';  —  iard^uströ  asaritS  aka manatgka  xrüzdya  'tanqm  ",  .  durch  die Schwierigkeit  der  in  feindseliger  Absicht gefragten  (Fragen)"  V.  ig.  4.
15037:•  j.  paiti.rae9-wa-  n,  'indirekte  Ansteckung (durch  die  Drttg  JVasav)"^:  iuia  harn.- ralhw?m  kuha  *iti3m  iu%a  natu/  apa- yasUne  haca  *avaAhai  visaf  V.ig.ii;  10.6, 11.9.
20660:..  Uta  ki/rama  (sd.)  paiti.mravane  Ytj. 82,
21224:Au.irixt^m(sd.)..trinaxtiYt.io.6B.  a)init' vorhergehendem  vTspum  S  aAm3J  'donec, bis':  näa  difyäi  aäa  ^rityäi  vJsp^m  ä ahmst  y'  hl  han/asaitt  yaia  iahrutiim *yär?  N.42;  43,  Vd..#.  3)  mit  dem Konj.  (oder  Inj.)  in  fiiCuiischem  Sinn:  yai (s.  V)  .  .frasna  (sd.)  paiti.mravSm  y  mgm ftrpsai  axtys  Yt  j.  8z;  —  y  irista  paiti us»hiltqn  ..  äa%aite  fras>m  vasna  anhui Yt  Jp.  1 1 ;  —  y  astvatjTTls  fraxHäite  .  . avaaa  drujpm  nilbarat  Yt  jg.  92  f.;  —  y yavs  dqyät  aal  daeva  :^um  (sd.)  y^  ■  ■ äayap  äaO  ..  V.,;.  32;  —  asti  zT  ana avavai  uxäata  (sd.)  ya'äsa  y  dim  vJsp5 ar»huf  äsaxiat  (sd.)  . .  pairi  irtkyqstätat (sd.)  haraite  Y.ig.  10.  /)  im  Sinn  des lat  Fut  II:  aSaha  hr  tanüm  . .  »idaihyqn vTsppm  3  ahmat  .  .  yat  (s.  c.)  frä  vayS patqn  ,  .  äat  y°  ('wenn')  ht^  frä  vayS patqn  fra  urvara  ux^qn  nysttiä  apa.- tacin  .  .  ariala  .  .  kahrptm  kvanJansJm kmnaot  V.  5.  i  a  £ ;  —  *fra  *ma  . .  *gara- yffi/ (sdj)  y  raful  fritsil  *a/asäi  N.  ip;  — y  dim  iatäj..paia  *avaMääiV.S.too(t); io3(?); — yai  nSiriAa  voAunls  atwi.vamäl y  (nachdem')  Al  'kray3  xlafiia  sacatüe V.  16. 8;  — y  ('nachdem')  kl  tanul  hilkvi Mymii  pqsnu  bavat  pascaSa  .  .  jasBtt  V. p.  31.  a)  mit  vorhei^ehendem  pasca 'postquam':  aem  ai^he  asti  utvanam  yal (s.  V)  nä  pasla  y  usthtÜäi^^  .  .  änV aÄOT  ■  upajtuyät  V.  18.  43;  s.  V.  18.  49 (unter    4).  b)    mit    vorhergehendem
24731:mit  paili  i)  'zuriicklassen':  äfs  uxz-a- zaiti  (sd.)  ä//  nivazaiti  äfs  paiti.raecayää ",  .  das  Wasser  lässt  (ihn)  zurück"  V.  j. 8'\  2)  'überlassen,  als  Erbgut  iiber- weisen'(?)3':  yezi  . .  pairijrihyät  cz-at  . . paUi.raicyat  (statt  "raj"")  Vd.  2.  3)  'im
=== p.r.t Kampf
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
5346:•  j.  a-rÄna-  Adj.  'keinen  Kampf  führend, nicht  kämpfend':  'na  F.  7.
5511:•  j.  arflnav-  m. 'Kampf,  Wettkampf':  _>'i'( .  .  /lita  taxAriii  'nStitn  (AS.)  "die  .  .  ihr Gespann  zum  Wettkampf  entsenden"  Y,
5512:l>.  2  2. KompA.  (?).    —   Vgl.  ahd,  frniisl,  ags.  eorniisl 'Kampf').  —  Pü.i  fehlt;  unrichtig  Det,  ZA. /.  93.    —    O  Gnindbed.   vIL   'Gewinn',    vgl.
5514:I'iaes.  irinav-  zum  V,  'ar-,  Uk  Bedeutungen ■Gewinn,  (Kampfpreis)'  und  'Kampf  sind  öfter TeieiDiet;  s.  ai.  dhina-,  klrä-  (GoN.VSt.  /.  I  ig)
5592:/0.136;  —  ai  vs  yaoja  zwlstyTng  (sd.J ,  -^^^^  ^^,- , ,  -. .  «enn  sie  in  den  Kampf •vatS  .  .  p>r>>üs  Y.  $0-  V,  -  mä  buyä  ^^^^i^hen  gegen  . .«  Yt  /o.  S;  -  ^J  . 'vatqmyOMa  (sd.)  .  .  »f«/?«  «r^i/a^/a . .  1  ,^^^^  ^^_y,  Yt./p.42.
5609:•  y  ar>za-  m.  'Kampf,  Schlacht':  miir^m]     Bfm^  if  jq  j^j
5858:Komp.:   aspii-+ä'j/aoia-  m.  'KampP,    zum  V. yaaii'X  at.  vgl.  äyadhatia-  n.  'Kampf.  —  0  An- ders JusTi  NB.  46  a. j.  asp>n'  i  s.  unter  aipaii:
7155:+1  Vgl.  JN.  GIrPh.  z.  641.  Clier  das  feuer im  Kult  s.  N.  /^  ff. ;  ferner  Sp.  Av.  2.  LXv,  DsT. ZA.  7.  LX^  In  dei  Mythologie  tritt  Alur  her- vor 1)  durch  seinen  Kampf  mit  AiayDaliJka um  das  i^'tirjiiah,  s.  Vi.  Ig-  \6f(. ;  2)  dmch  seinen Sieg  in  Gemeinschaft  mit  VehuManah  über  den angreifenden  AuraMainyat;  s.  Yt.  13.  77  f.,  Y. 46.  7.  —  ")  Der  TeuerbebSlter'  (d/«i  liia)  hat seinen  riati  auf  dem  'Feuersland'  {iitusi  od« äHU)7\  an  der  'Feuerslätte'  iftia's  i^ä6),  d.  i.  in der  Südhälfte  des  'OpferhauEes'  {j-azisH  xJn,ii); vom  Za^/ar  (Oberpriester)  aus  gesehen,  der  an der  Nordwand  der  'Opferstälte'  {ya::Jii  gilli),  d.  i. der  Nordhälfte  des  'Opferhaoses'  silit,  jenseits ■  des  Gerilctisches  (s.  araiiar-'),  auf  dem  auch I  das  Bai/iman  sich  befindet.  S.  oben  1  b.  — I  •")  Vgl.  dazu  oyah-  A  und  inlay-*') ;  ferner  lu
7933:*)  Dessen  Tätigkeit  Bd.  iS.  8  beschrieben wird.  S-  noch  West  SEE.  s/.  i8a.  Blocket RHR.  31.  113.  Bd.  so.  29  und  PöErl.  lu  Y. 4S.  1  wird  er  als  spezieller  Gegnti  Aial'aAii'tas '    :im  letzten  Kampf  bezeichnet.
8625:•  j.  iizgastay-  f.  'Auszug'  (zum  Kampf): aurvanUm  .  .  yö  äsits  anhat  'td  (LS.)  Yt.
10015:—  nanm  asavamnt  hväkva  ähäAva(sd.)  Leben)  davon  kommen':  yat  paoirTm  .. jasäntam  *'  ^-49;  —  ylf  janat  .  .  gatS  kfrmiät  apa  he  jasat  "wenn  er  einen arytahe  ". .  wenn  er  in  den  Kampf  ge- '  ersten  operirt  (und)  der  kommt  davon" zogen  ist"  Vt/5.42"'';  —  ii  ahmt  »«(7w|  V.  7.  39;  39';  —  ä/rsafro  (sd.)  ioa,.g}iis /amyärpfyii  afapnqm  xsnQtasia  .  .  Y.  60. 1  apa.jasat  V,  2.  23,
14733:deule  meist  ^J/oj/J»,  aber  au  eh  dälavmt.  —  ' '  "^f  ■"*  " '  ^f?'^  ,  *  ■  'l"  ' '  ^  ^ '  "'"Tratte . . »  irfoÄa- (und  ebenso  "/*nAV,  sd.)  gehört  also  !>'«/  3«"*  dtdvXsma  Y.Öff.i;  —  i?  Ja/a/« wie  'daiira-  (sd.  *)),  wn|f-  usw.  zu  den  Schlag-  ^yim  afturnn  .  .  masUta  tbalsanha  ibaisa- und  Kampfwörtem   der  jn^aSüi/nschen  Zeil.  \ yäti  V.  18.  6jJ  —  tbistahtlit  axsnustahe
15609:Kampfe.— Komp.-.pam+'Awa-, —  tä.-.viiarai- emaiidiM,  Sü.i  parikramariTyah.  —  '>  Falsch Wilhelm  ZDMG.  4^-  96.  vgl.  apairüaya-.
16066:•  j.  ■•■parat-"  f.  "Kampf,  Streit*:  OxStlm ham.vmniim  'tasüa  mrvayasca  Aamaistara Yti/,is.
16073:Bed.?  —  GnN.  vermutet /oraf/A*.  Eher  vll, mit  Mf3 /^jilft/af',  d.  L  'p^r^tiflS. ;  vgL ai.ifij'tü-  'Nebenbuhler;  Kampf,  got.  ipaun/s ■Rennbahn';  %  S3.  a)  +  *daya-  (rgL  paiü,- liaya-),  also  eig.  'der  auf  den  Nebenbuhler Acht  hat'  oder  'der  achtsam  ist  im  'Wettkampf.
16161:•  j.  paranävayam-  f.  'vollkommene  Ab-  •  ]■  'paäana-  n-,  p«äaiüi-  f.  'Kampf, Wendung,  Abbitte':  -^J  (NS.)  F./o.  Schlachf:  nivanäat(sd.)  apaydH  [..]  "«a
17237:•  j.  boiwrra-  m.  'Kampf,  Streit':  'ranqm dmitanamca  ..  %wa^sh  (sd.)  Yt/y.  so.
17238:Mit  Int. -Red.  gebildet,  S  103  n.  6.  —  ai.  vgl. bhira-  m.  'Kampf;  Bthl.  IF.  IO.  aoo.
18210:■  j.  frl'yaoda-  m.  EN.  eines  Gläubigen: ;  'oaAg  karsnayanaAe  asaonff  Yt  jj.  108. Eig.  'der   vom   im  Kampf  ist,   vpifiaipt'.  — "yaiia-  m.,  inm  ^.  yaed-;  vi.  yadhä-  m. \.Jriyal^i&'  Yl,  /j.  108;    lies /rflnya/.r".
```


## [2026-09-14T00:55:46.553Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null\necho \"=== tags sample\"; grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -5; grep -c \"\\[pdf page\" BQT_v1_pages.txt",
 "description": "BQT files structure"
}
```


### [2026-09-14T00:55:46.617Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2499427 Sep  4 14:06 incoming/BQT/BQT_v3_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2055176 Sep  4 14:06 incoming/BQT/BQT_v4_pages.txt
=== tags sample
0
```


## [2026-09-14T00:55:50.153Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 400 BQT_v1_pages.txt; echo; echo \"=== formfeeds\"; python3 -c \"\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint('pages',d.count('\\f'))\n\"\npython3 -c \"\nimport json,sys\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\"",
 "description": "BQT page offsets"
}
```


### [2026-09-14T00:55:51.427Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس

=== formfeeds
pages 776
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
 "scans": [
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
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
```


## [2026-09-14T00:55:57.994Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(660,672):\n    t=d[i]\n    print('===== leaf',i,'len',len(t))\n    print(t[:900])\nEOF",
 "description": "BQT v1 leaves around p.440"
}
```


### [2026-09-14T00:55:59.154Z] TOOL RESULT

```
===== leaf 660 len 2153
یاب
وبکر او عخفف یه بات دکه درچراغ سوزند
- وشمم تیز سلزند ۷ -
یمیت بروزن سراب. بمعنی پاباباست
که ین‌حوض وته جربا باشد وبعربی قمع رکوبند -
وتهات عرچیز را تز کفتهاعد - و بمعنی تاب
لبادم بر وزن زباده . هعروف است
که قض سواره باشد ۴ - ونام مکی‌از مپرهای
شطرنح عم حست - و نم کلی است ممروف -
از عردم یی سواد باشد یمنی علم و فنلی کسب
تکروه بلشد .
یباده نهادن-کنابه از زبون داتن
وعلجز اتکلشتن باشد . 9۶
ار دشتی- بکسر .اول و زای هوز ۰
دوآنی است که *ن را جربی صل‌الفار خوانند .
کوبنه اکر حوش بخورد میمیرد , و از خواص
او اتت که اک رک رکه بای بربر که آن ,گذارد
حمین که مزدارد لنگه شده باشد وگن سای
توقف کند الیته بفتد وبمیرد .
هیا لش یا کاف . تسیر پیاز است -
مه
وکیاهی را لیز کون دکه ازآن بوربا بافند -
و نوعی از کرز باشدکه سر. آن را با زنجیر
چو کن خوانند ۴ - ونام قربه‌ایت دردامن کوه
معدن لمل ۵ .
یا کیی- املیباشد قیمتی۷ ومنسوب
بقربه مازك را نیز گویند.
فاد یز « بکس لام و سکون تحتالی
و زای نقطه دار . نوعی از از 
===== leaf 661 len 1485
و۳ ««
پیاهو - با های هوز بر وزن ترازو .
هم عده است کهخالة شش بهلو 7
اری ماشد ٩‏ ۰
فیتا۵؟ - بانای قرشت؛ زد زن و معنی
ت بلغت زند و بازند (۱).
لیترسب؟ - بدر اول و سکون ثانی
و .فوفانی و رای می نقعله مفتوح بسن مي نقمله
وبای فارسی زده , نام بدر پورشسپ اسث که جد
یفام است
برست ات .
شقات- با تای قرشت بر وزن مخك »
کرمیست که جامهای ایرشمی را خورد وضایع
و ۵
له بروزن هیج . بمعتی تاب و حلقه
و خم باشف ب و کنابه از رشك و حند هم
هست .
پیچبا * - با بای فارسی بسر وزن
پیشوا . خرچنکه را کویند که بمربی سرطان
خوانند .
پیچاگ - بای مجهول بروزن قیجك ۰
(۱) چك: ژد و پاژند :
۱ ‌- ره 5 آهویای.
۶ اسشق+ ۳4عرك : بیام.
و مربی آن دا عشقه و لبلاب خوانند ۷ -
و کرو ابرشم و رسمانب و سربند زن را
دا
لین » بروزن ربوند . عصانه ویتانی
بند زنان را گومند .
لیچه » با نانی مجهول بوزن رشه .
و عذقه کویندشی  .۷‏ و زلف عملی دا نیز
گویند- و طر؛ زلف و کا کل را حم کقتماند که
پیچند و برمکدیگر گرء زتند - وموی بلف وا
نیز گفنه‌اند و بعربی عفاص خ
===== leaf 662 len 1227
تشن
ولای‌هرچیز وضله حرشیتی را کوشد ازحیوانات
پیتتن" -بروزن ربختن,بممنی پیچیدن
باشف . ۱
یتخس" بروزن ک رکس . بممنی کمان
بردن واز روی گمان فهمیدن وراه بچیزی بردن
باشد .
سای ارل و تاك پر مك
- و چیزی که 9 فرم شده باشد -
و درمانده و عاجز شده را نیز کویند - و بمعئی
هی بست 4 دبوار ی که بیخ
ومحبری ومتحصن و کرفتاروبندی رانیز گفته‌اند
و بد بو و متعفن و گندیده شده را ه مگویند »
وبضم الث یز آمده است .
پیخسته ح بر وزن برجنه » بمعنی
زیر بای نرم شدم و عاجز ودرمانده - و محبوی
و گرفتار - و بد بو و متعفن - وکمان بردن را
- و در
زر کوسد ری ی رس اسر میتی
ره
بزور باشد ۰
بمعنی ترت ومرت وتار وعار و بفایده - وهرچه
از تف آش زرد وضایع شده باشد ِ#
ید اد بر وزن شداد ؛ بمعني بیدا
وظاهر باشد .
فيك او سی» بنتح واو و سین بی نفطه
بتحنانی کشیده . درمی که در زمان کیان رایج
بوده و هردرمی به‌ینج دینار خرج میشد, وبکسر
واو هم بنظر آمده ات :۷
پیر ؟ بروزن وه‌متی پدر |
اب گوند ۵ ۰
یر ا ۲ - با انی مجهول بروزن گیرا »
و سر تراش که مو
===== leaf 663 len 2160
خافهای زیادن را عرد نی قلاف. ماهه 2
وبمعنی‌ساخدن ویرداختن ومنقح کردن- وچیزی‌را
از عیب خالی نمودن هم هست .
ثیر استو۱ « کم کردن چیزی باشد
بواسطه زبابی و خوش آیند کی همچو بربدن
ذاخهای زبادئی آزدرخت وموی زبادنی از بدن.
کوبند شبی اباز بامر سلطان محمود در حالت
مستی زلف خویش را بربد. روز دیگر سلطان
از آن حالت پریتان خاطر گفت. عنصری باین
رباعی سلطان را از کدورت بسرون آورد :
ر باعی
هنن زلف بت‌از کاسنن است
چه جای بفم نشتن و خاستن است
جای طرب ونثاط ومی خواستن است
کاراستن سرو ز پیراستن است.
سو دیاغت دادن چرم را نیز گویشد.
۳
بر استه؟ بروزن بی‌خواسته » به‌عتی
مرتب گردانیده و ساخته و پرداخته باشد -
و باغی که شاخهای زبادنی درختان آن را بریده
وعلفهای زبادنی آن‌را چده و صفا داده باشند -
و درخت ی که آن را پر کاوش کرده باشند » بعنی
شاخهای زیادتی آن را بریده باشند - ودهی را
معتی بابای ابجدهم بنظر آمده است.
نون و دال ابجد , ماضی متفرق ساختن
وافشاندن باشد بعنی متفرق ساخت ویریشان کرد
و افشانید ۰
یر آهن» با انی 
===== leaf 664 len 1681
پیراهن فبا کردن
پیراستن وزینت دادن راگویند مطلقا- و دبافت
کردن پوست را ه مکفته‌اند ‌#
پیر آهی قبا کردن - کنابه از چا
زدن و پاره کردن پیراهن باشد.
پر اهی کاغدی- کنابه از داد -
خواهی‌باشد٩‏ . وروشنابی صبح وشعاع آقتاب را
نیز کویند .
لیر ای ؟ه بروزن سیمای» زشت دهنده
باشد "که سرتراش و بافبان است . چه کی که
شاخهای زبادتی درخت دا سرد او را بشان
پیراکوبند - و پرداختن و مستعد کردن را لیز
کفته‌اند .
یر آیش- بابای حطی» بروزن و ععنی
بیراهش است که پبراستن وزشت دادن ودباخت
کردن بوست باشد. وساختن و پرداختن. وهستمد
کردن ومهیا نمودنرا نیز گویند.
ثبر اینده » مر وزن ژیباینده » زیت
دهنده را گویند که چیزی را از چیزی بجپت
خوش آبند کی کم کند همچو سرتراش و باغبان,
برخلاف مشاطه .
پیر ایه۴ ه بر وزن بی خابه . آرایش
و زیور باشد ازطرف تقصان همچو سر ترائشیدن
واصلاح کردن وشاخهای زبادتی درخت دابربدن.
و کنایه ازساختن رپرداختن هم هست؛ ودرجمیع
بفتح اول‌هم پنظی آمده است ۴ .
هیر بر فا آن» بکسراول وتح بایابجده
۱ ره کاغذی حجا
===== leaf 665 len 2357
پیر فلا کنابه از کوکب زحل
پیر كاخ - بکسر اول و سکون ثالی
و فتح رای قرشت و نون ساکن و دا بی تفطه
بالف کشیده و بخای نقطه دار زده » نیماج
و سختیان را گویند ۷ .
ثبر وج - بائانی مجهول و جیم بر وزن
فووژ ۰عرغی است که س و کردن او ساده
وبی پر میباشد و حرساعت برنگی مینم‌اید و از
بالای منقار اوپوستی مانند خرطوم فیل آوبخته
است» وفبل مرغ همان است
فیر ود - بر وزن و معنی فیروز است
که غاب شدن و غاب آمدن بر اعدا باشد
و عرب مظفر خوانند , و فیروز معرب آست -
و بمعنی مبارك هم هست - و تام مبارزی بوده
ابرانی
ثیر ود دام با رای بی نقطه بالف
کشیده و بمیم زده ۰ نام شهری بوده در زمان
۱ ره ؛پرنداخ وس‌تداق , ۲
قدم ۴ ۰ *
یر 9 ۴۵ « بروزن‌وممنی فیروزماست؛
وآن جوهری باشد معروف ونشایوری آن هش
است ..گوند نگاه کردن بر آن روشنابی چم
آورده و فیروزه عمرب آست .
ثبر وزه‌جادد. کنایه ار آسمان
وفلك است .
ثبر ودی ِ بروزن و معنی فبروزی
است که ظفر وصرت یافتن براعدا باشد .
مر ۵ - بروزن خیرء » خلیفه و جاشن
مشایخ واریاب طریقت وخانقاه نشی
===== leaf 666 len 2291
علت برص وجذام داشته باشده ۴.
ودنه باثانی مجهول و دال بررزن
بی سوزن » عبل نمودن و اراده کردن بطرفی
باشد .
لیسه ۴ » با ثانی مجهول بروزن کیسه »
بمعتی سیاه و سفید بهم آمشته باشد - و فیژ
هی رنگ ی که بفید آمیخته بود» و بعربی ابلق
کوشد ۴«
فیش۰ بروزن ریش ۰ ممروف است که
نقیض پی باشد ۴ - و شاخ درخت خرما
و خرمای ابوجهل را تیز گوبند ۵ و مافل
و خرمای ابوجهل را نیز گویند ,و آن ببانی
کب وت ور بو که
ازمردم خسیس و رذل هم هست - وسفد را حم
حیکوین د که یش سیاه باشد:
ی سیاز « بابای فارسی بروزن زرنگار,
رونده و راهرو را گوشد- ویمعنی‌پی‌سیر هم‌آهده
س که لکد کوب ویایمال باشد.. :
یی سیر بابای فارسی مر وزن دردسر »
او 0 9
شفه باخدت ویمعتی رونده نیز آعده است ۰
فسست» بروزن کیست » شخصی است که
اک تن و ع ‏
۴ -درپارسی باستان 085 و در اوستا ۳265 بمعنی دگاشتن و نگادیدن و شش کردن
است. ازهمن بنیاد است ۵۸51216 که درپهلوی بمعنی نقش ونگار بسته وزشت شده است و دد
پارسی پیسه شده بمعنی ابلق و دورنک : سفید وسیاه. پیسی که در نازی بر 
===== leaf 667 len 2013
تن پش باز
و مواجه ویرابر و مقابل را یز کویند وکنابه
ازدو لت م هست.
لیشا نی ۵اد - بارال ابجد بالف کشیده
و برای قرشت زده ۰ کي را گونندکه کاربرا
بشکفتگی از پیش برد - و کنابه از دولتمند
ئم حست .4
پیش آهنگ بش رر فافله
ولشکر را کوینده - وچاروای یکه پیش‌پیش‌رود.
رهرحیوانی که س رکروه وییشرو توع خود باشد
اورا هم مهن( ۳ :
و خردمند راهم کفته‌اند - و بمعنی مقدمه هم
هست چنانکه کونند « اين پیش را داستی >
اراده آن باشد که این مقنیسه را دانستی و بمعنی
فیشاذست » با تانی مجهول و ثالث
بالف کشیده وقتح دال وسکون سين سعفص وتای
قرخت» اجرت ییشی را گویند. وبمعنی مشدستی .
هم آهده اسعات و نقد را نی زگفنه‌اند که در مقابل
لسیه است ۴ .
پیش اد ه- بابای فارسی بروزن شیر
خوارهء نوعی ازحلوا باتد بیار نرم ونازكوآ نرا
از آرد وروغن و دوشاب پزند» وبعربی شفارج ٩‏
خوانند ۷ .
پیش بار- بانانی مجهول,بروزن وممنی
پیشان بائانی مجهول بررزن پیجان ؛
بیش پرش را گونند که از آن پیشتر چیزی‌دیگر
تباشد بعنی اهپا ؟ .
فیشالی ۴ - با انی مجهول حع
===== leaf 668 len 2058
پیشواز است که بعربی استفبال گوبند و نوعی
ازجامة پرشیدنی هم هست .
پیش خاه - بسنی رواق است که
بیشگاه خانه باشد - و ایوانی که در مرتبهٌ دویم
ساخته باشند ‏
پیش خورد بر وژن لیم خورد »
و پیمنی پیشکی و سلم فروخته هم هست» یعنی
فلة نارسیده و مو# نايخته وامثال آ که بیشتر
فروشند .
یشد۵اذ ۱ - با انی مجهول و دال
اسجد بروزن پیش باد ؛ بمعنی عادل اول است -
و اول کی را نیز کویند که نظلم برحاکمی
کند . وحا کمی که‌اول‌یفور مظلوم برسد- واول
پیشدادیان را هم گویند که هوشتکه باشد واو را
فارسان بشداد میگفته‌اند یعتی عادل اول و بعد
ازر طهمورث و پعد ازو جمشید و معد ازو
ضحاك و فربدون و منوچهر که شش تن باشند
. و بضی بازده تن را گفته‌اندکه ابثان دو زار
و چپار صد و ینجاه سال یادشاهی کردند : اول
هک ‏ رت حا
6۲ سه
جمشید. پنجم‌ضحاك, ششم فریدون: هفتم‌عنوچهر»
هشتم نوذر» نهم افراسیاب تركك. دهم زو پس
طهماسب‌ین منوچهر» بازدهم گرشاسب- وزری را
نیز کوین دکه مش‌از کار بمزدور و کار گر دهند
و آلرا بعربی تقدمه خوانند ۴ .
پیش‌داد بر و
===== leaf 669 len 1528
۳و
فیشگاه « باکاف فارسی بروزن ثیرماه»
بیتی صدر- و صدر مجلس هردو آهده است -
وفرشی‌را نیز گوبند که‌درپیش افکنند. وفرش یکه
درپیش ابوان وصدر مجلس اندازند - و محرابب
مسجیرایز کوش ویادشاه وصاحب تخت ومسندوا
هم کنته‌انه ِ
پیشگاه نشور - کنابه از قيامت
باشد .
پیشگر - با کاف فارسی بروزن بیشتر »
خادم وخدمنکار ت ومددکار باشد 2
پیشگو- باکاف فارسی بر وزن نیکشو »
۴۹۳۳ را کونندکه در مجلس سلاطین و امرا
و اک بر صدارت شخصی کند 2 بایشان بشناسانف
و آن شخص رابعربی معرف خوانشد. و شخصي را
نیز کونند که مطاب مردم دا مرش سلاطین
میرساند» واو رادر هندوستان میرعرض ودر دکن
بخبردار گویند .
پیشگوی بروزن نیکخوی:» بمعتی
یو است که معرف باشد و شخصی که مطالب
کسی‌را بمرض سلاطین رساند .
)۱ چش : پازاح
پِشة آش
بشگه بروزت لیهژه » مضفف بیشگاه
است که هم صدر- وهم صدر مجلس- وهممحواب
مسجد باشد و فرشی‌را نیز گویند که دد پیش
آبوان وسدر مجلی اندازند-
شین خنح الث بروزن سجن , لیف
خرما را گوبند که ازآن رسن بتابند.
پیشن ه بر وزن ربونف » بمعلی
===== leaf 670 len 2248
شطالی باشد .3
ی اد بایای حطی» بروزن وععنی
بیشکار است ت که خادم و خدستکار اک رد
ومزدور وش دست‌باشد ویمصی بیشاب و شاش
هم هست که بمربی بول گویند- و قاروره پیماررا
نیز گفته‌اند وآن شیشه‌ای باشد که بول بیمار را
درآن کنند و پیش طبیب برند » و بممنی آخر
بجای حرف آخر نون هم آمده است
پیشیاده - با ثالی مجپول بر وزن‌هیج
کاره؛ خواتجه وطبقی را گوبند که تعلات 4
در آن کنند و بمجلی آورند ٩‏ .#
بیفاد ه- باغن نقطه‌دار بروزن مخوارد:
طعنه وسرزنش وبهتان را گویند ۴ .
بغا له بر وزن بنگاله» قدح و کاسةٌ
را
هرزه هم آمده اس ۴ ۰
0 غلوش ه
کلی است‌از جنس سوسن و آنرا سوسن آسمان
کون خوانند و بر کنارهای آن خالهای سیاه
وچینهای کوچك افتاده است
دغله- ار وزن زنگله
چ‌
« بالام بروزن نیم جوش »
1 بمعنی کنج
و کوشةٌ خانه باشد - و کنج و كوشة چشم را لیز
گویند. وبمعنی براحه : دز آمده اسن که قض
راه باشد ٩‏ #
لماگنس بروزن هدن , سداب را گونند:
و آنگیاهی باشد دوابی مانند بودنه» و خوردن
11 ِِ_ قوت باه و یت ها و ی آن
۲ اول و ضم ثالث» بروزن
===== leaf 671 len 2072
وشرط را گونند ۳
لیتا- بکسر اول بر وزن جیفه » چوبی
باشد بوسده در ولابت خوزسنان و آن را دای
ی ۲ بکاربرند بمنی باستگه و چشماق آش
درآن زننه 2
ییگاد ۴ - بنتح اول وکاف فارسی‌بروزن
نی‌زار , جنک وجدال را کویند - و بمعنی قصد
واراده هم هست ۳0
کار بر ستان - کنابه از مردمان
جنگجو باشد . 4
٩‏ بیغو (مرکی), مرغ شکاری‌شبیه بشاهین. «جفتابی۱۸۷. ۴ - همریشة بیفوله. ۴ - رك:
بیغان‌وبیمان . ۴ - بیکار ویرگار » ازاوستابی 0۵016278 ۵» پهلوی024۵ (جنگ),
ارحنی اسف (جنگه) «اسدق ۰۳۹۰ دیب رکه۱ ۰*۱۸ . ۵ ومجازآبممنی جدلوسخن‌بهوده:
بهستیش بابد که خستو شوی ز گفتار پیکار _مکسوشوی. فردوسی طوسی.
«تاحیت سپاهان ومردم‌آن جهانیان را عبرتی تمام‌است» باب که جوایی جزم فاطم دهیدنه
عشوه و یبکار.» تیف ۶ب ٩۲۱‏ ۰
۵ پيك بفتح اول وکاف فارسی باکاف تازی, ازاوستابی ۳20112 ۵ لفة بمعنی پیادم
۱ معرب آن‌فیج .سشق ۳۵۹.
‌ یکان - بفتح اول . اوستایی (9) 0هع + 02161 (180 کندن). ارمنی [مه‌اعم
0 « استق ۲ ۶ , پهلوی 0 « اونوالا ۲ده » ؛ توكك تيز تس و دیزه ح
```


## [2026-09-14T00:56:21.401Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in list(range(664,672)):\n    print('===== leaf',i)\n    print(d[i][-700:])\nEOF",
 "description": "BQT v1 footnotes leaves 664-671"
}
```


### [2026-09-14T00:56:22.774Z] TOOL RESULT

```
===== leaf 664
 باشد چنانجه در نمام
بدن او موی میاه نماندهباشد.
ثیر بنیه» نم بای ابجد و فتحع یبای
هنوز جوان باشد لیکن موی بدن او قمام سفید
شده باشد .
یر جهل سا له کنابه ازعفل است-
و فرشته را نز گویند و کنابه از آدم صفی ۶
عم مت و فیروزه دا نیز گونند که نوعی از
جواهر باشد .
ثیر ذو هو یه کنابه ازدنیا باشدباعتبار
شب وروز .
یر ۵هقان» معروف است_وشرابکهنة
انگوری را تبز گویند 5
لیر ده بفتح اول و ثانی و زای هوز ,
چیزی که درلنگی و دستمال کرده کره بندتدواز
جابی بجابی برند .
پیر سالخودده- بسن پر دهفان
است که شراب کهنة انگوری باشد.
بر سر اند بب ه کتابه از آدم
صفی؟ است .
یر صنتعا - مراد از شيخ صنمان است
واو زاهدی بوده مشپور ۵ ‌
اسناد هنینگه) -- پیرایش.
عروس مجلس ماخود همیشه دل میبرد
علی‌الخصوص که پیرابه‌ای پراوستند. ٩۱‏
===== leaf 665
 بهلوی 208462 دیب رگه 6 مر کب از: بسن ی (حاصل مصنر).
٩‏ - بیره خلیفه وولعهد. «فرهنگه‌دساتیر ۲۳۹. ۷ - تلفظی ازیراهن(ه.م).
۸ اوستا 2۵52 (ایر ۳ ؛یپلوی 6( ص). هندی‌باستان 0۵29(آراش زشت)»پارسن
باستانبنقل بو نانیان81384 1 , کردی ۳۵581:0۳15 افتانی 65 ۳0981 (برسص) «اسشق۵ ۳۵ کلمه
. 2 وراوستا دوممنی دارد: نخست بمعنی زینت ونقش » دوم نام مرش معررف ‏ بارتولمه در
فرحنگ» خود ( ۸۱۸) و بشبع اوهرن« اسثق ۳۵۵ > ممنی دوم این واژه را جذام 2اعفتاخ
ترجه کرده است وآن مرضی است ماری که در ایلم قدبم بیشتر ازعصی حاضر شیوع داشته ولی.
در آن (برخلاف پسه) خالهای سفید در بدن ظاهر نمیشود. بتابرین مانند فوبسند گان اسلامی
متاسب‌تر است آتراما (برص>» نطبی قکنیم . در بسرالجواهر درمادءٌ 2 «البری»] هنه: «یان عظهررفی
بقبه درصفسةٌ 440
===== leaf 666
شت بند۲ » وندیداد پند۲۹. این بیماری | کرچه ساری
نست, معپذا ملل قدم را مسیار شوم مبدانستند . از همن‌رو درآ بان به شت و ونددداد (ندعهای
و۳ آمد هکه پبسی را بانداز ما کر . هردوتی همین موضوع را در کاب اول ند
۳۸ آورده : اک کسی درمیان ابرانیان بمرض برص میتلاگردد نباید درشهر بماند ودرانجمن
درآید . ایرانبان کمان میکنند که مبتلابان بان مر ضگناهی دسبت بخورشید مرتکب شده‌اند ,
اک بیگانه‌ای (خارجی) دچار این ناخوشی گردد اورا از کشور ببرون میکنند. » ازروایت طبری
و بلعمی نیز برمیآید که نزد بنی اسرائیل هم اين مرض موم بود ومبتلابان بدانرا اخراج
میکردند 1 رلك: قاموی ۰قدسر: فذبل: اردو ] . «مزدبسناصی ۱۱۰ - ۱۱۲ رلد: فسه .
۵ پروزگر - مرکب از : پیروز ۳+ گر ( پسوند فاعلی ) [ رث : پیروز ] ؛
عالب فاتح ( بر ها قاطع )٩۰‏
===== leaf 667

اشکاشمی و مشگلجی ۳6۵۵01 » بورغا ۳15102001 «کربرسن ۰۰۹۲ کينكي 201تاهام.
۵ - نشاید ,رد سعدی حان از امن کار مسافر شته و جلاب مسموم
چو آهن تاب آتش هی نیارد چرا بابد که پیشال ی کند موم.
سعدی شبرازی.
دل ز او چشمت کوش داشتم لیکن ابروی کماندارت میبرد به‌یشانی.
حافظ شبرازی. «دیوان حافط فزونی ص ۳۳۵».
۵ ۷ با خیمگی‌خیمه فروهل که پیش آهنگه بیرون شد ز عنزل.
ِ ( منوچهری دافانی44 *.
۰ فشفارج‎ ٩ وتیز‎ ٩
سخن باید که پیش آری خوش ابرال سخن خوشتر بسی از پیشیاره.‎ - ۷۲
تس «ناصر خسرد بلخی۳۹۵) دردیوان مزبور ییث‌باره!‎
پیشاو ند و پیشو ند -امروز درمقابل پساوند وب‌وند.بحرف (باحروفی) اطلاق‌شو د که‎ ۵
درآغاز کلمه قرار گیرد وتفییری درممنی آن‌دهد مانند: «باز» در بازآمدن. «فرا» درفراهم.«1* در-‎
آراستن» #یر>* در بر‌داشتی.‎
===== leaf 668

پوشند .
پیشکار ه با کاف بر وژن رش دار »
خدمتکار وشا کرد و مزدور باشد - و بمعنی همد
ومماون و مددکار هم هست . #
ککه درپیش قالون وضع کرد و داد گری نمود بالضتین واضم . حمز؛ اصفهانی نیز این‌کمهرا
درست معنی کرده نود : فیشداد اول حا کم باشد چه اوشهنج اول حاکم ممالك بشمار است.
«یشتها اص ۱۷۹؛ بشتها اس 40 و۲۱۵». ۸ موف زغور اخبار ملوك الفرس دردیادشاهی حوشنگه»
کوید: ... ووضم قوانین ورسوم وبرقراری عدل بدومنسوب است وبهمین مناسبت به پیشداد ملقب
شده که بفارسی نختین واضم عبانی عدالت است.
۴۳ ح ‏ فش + راد» بعنی بیش داده :
ز بی حرص بخششی نکرده سژال بىایل دهد جود او پیش داد.
عجدی مروزی. «جپانگیری».
پشکش - بکر چهارم (در اهج؛ حر کزی) ازربشة پارسی باستان۵:5.ظ5 ۵2
(جل وکشیدن) ؛ حدیبه‌ای که بشخصی بزر کتر ندیم کنند .
===== leaf 669
 سجن , لیف
خرما را گوبند که ازآن رسن بتابند.
پیشن ه بر وزن ربونف » بمعلی پیشن
است که لیف خرما باشد واز آن رسن تابند.
پیش شیی - بکس نون پازاج (۱)را
کوبند که دابه و ماماچه باشد , و بعربی فابله
خوانند- وامر به‌پیش شستن هم هست.*
پیش | - با واو بالف کشیده » سر کرده
و پیش‌رو مردمان باشد و بعربی مقتدا گوشب -
ولوعی ازجامه هم هس ت که زنان بوشند .3
یاه بی وزن رشه » رسنی باشد که
آن را از لیف خرما تابند ‏ و با ثالی مجهول »
شفل وکار وعمل و کسب را گوند وبمربی حرفه
خوانند ۱ - و فسمی از نی ۲ باشد که شبانان
عم نوازند و آنرا توتك خوانند.
بشه آ تش کنابه از کارهای
(نی + چه) « از افادات علامه دهشدا» .
۴ - ظ . تشه
پیشنهاد خاطرم ابنکه هلا او شوم
تشنهٌ جام می روم شاید اکر سبو شوم .
باشرابط عمین ۲ گاهی میدهد. عرضه .
===== leaf 670
فر ( که اغلب
بقلط بیغو وپیغونوتثه و خوانده میشود) بحکام خلخ اطلاق شده. ابن خردادبه (س ۱5) کوب د که
ملاطین ترك و تبت وخزر « حافان » خوانده میشوند « باستثنای پادشاه خرلخ که جبفوبه نامیده
میشود .» بقول کاشفری ]11 . ۲۵ یففو عنوانی بود دو درجه یابین‌تر از خاقان . عنوان ,بفو
0 ( کاغنری]]] .2]800:۳6از ۷2۳۵00) را بامد از نام قبلهباغو 72028۳00
تمیزداد. قببلهة اخبر درسمت شرقی‌ثر بن قای وتانار جا داشته‌اند (کاشفری آ .۲۸». برای اطلاعات
بیشتر" رك : : میلورسکی . حور العالم ص ۰۳۸۸
‌ پیشی - از: پیش اد ی (حصدری)؛ سبقت. . نقدم: : بیی گرفتن سیقت جستن؛ میتی
ریسی تقدم و تأخر: «پیدا کردن حال منقدمی ومتأخری که پیشی وپسی بود: پیشی ویسی ۳
بود بابطبع بود بابشرف بود...» «دانشنامه ص ۹۸».
۲ مصحف : یب انه.
بقه درصفحً 140
===== leaf 671
رین خوانند وعلم پیشین
وعلم آفچه سیبر, طبیمت است خوانند...» « دانشنامه ص ٩٩‏ .
۵ پیغام - بفتح اول. هم‌ریشه وهم محنی پیام «اسشق ص ۸۰ ر: پیلم وپیتام. درزبا کی
00 «کربرسن ۰۹۰ ,کیلکی صفاو(26 .
۵ یغامیر وعخفف آن یغمبر ار بات اب ام بیغام ۳ بر (مخنف
برنده)" دراستی ۳6610171۳26 با 02011۳0۳6۲ « . است ۱۲ » »گیلکی ۳۹
رسول . کبکه پیفام می‌برد یامی‌آورد-. کس یکه ازجاب خدا مأمور هدابت خلق است : «ازهر
اين همی عیراث ماند علم پیغمبر بوصی و از وصی بامام و از اما بحجت » «کنف سپ ۱
سجتاای ص 1۱۵؟.
۵ یخامیری و پیخمبری - م رکب از: ییفامبر (پیغمبر) ۳+ ی ( مصدري )؛ رسالت ؛
یفام بردن- نبوت: «بسیاری پیغمبران‌بمین برشریمت پیغمیزان پیشین بودند وغدتی برآن شریمت
همی کار کردند ؛ وبه پیذامبری رسیدند.» < کشف المحجوب سجسانی ص۷*.
```


## [2026-09-14T00:56:34.966Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [463,464,465,466]:\n    print('===== leaf',i); print(d[i][:300]); print('...TAIL...'); print(d[i][-600:])\nEOF",
 "description": "BQT v1 around p.242 (-bad suffix)"
}
```


### [2026-09-14T00:56:36.176Z] TOOL RESULT

```
===== leaf 463
- ۷۳
است مابن هندوستان و خراسان ۰ کوبند معدن
لءل و طلا در آنجا هست و گوسفند آنجا را از
غابت. بزر کی و قوت سوارشوند و باهای‌تر دك
تردد نمایشد » وبسنی کویندکان لمل آنجانیست
و چون از مدن بدانجا آدرند و فررشند بدان
شبب سوب مبدخشان شده است.
بدخش مذاب ه کنابه از امن
بدخشانو شراب لعل باشد .
بفدل « با دال ا
...TAIL...
هل جپت اعانت وازدیاد عمل‌آن تدرجاً وشد - معتمد - و شکیبا
و صابر دنانمآلاطباء» » مبذرق » در عربی بمعنی دلیل و دیدبان است .
9 ماء کنعانی هن اهستف مصرآن توشد وفت آتست که بدرود کنیزندان وا. تحانط شیرازییه»
۲ - رك: پدرود - .
۵ بدر 8 محبت ‏ ورقمراسلة دوستانه «نلظم‌الاطباه».
بقه از مشحهً؟ ۷4"
با بلخش 0212:0510 است و آن نوعی است از باقوت که کویند جز دربدخشان » در ساحل نهر
ککجدت»0 بات نشود.» اماکاملایحتملاست که کلم باخش 021850( که‌کت فان کنعلعط
و انگلیسی کقاق(] از آن مأخوذ است) در آغاز نام ناحیت هورد بحث بوده و بسدها بلملی که حر
آن ناحت بافت شود اطلاق شده باشد . «بارتولد . دائرتالمعارف اسلام : بدخشان».
===== leaf 464
بلیست - بکسر اول و ثالی و سکون
سین بی نقطه و فوقانی» وجب را گوبند و بسربی‌شبر
خوانند ۱ .و فتح اول و ثانی هم آمدم است َ
سو قوی زا تفت وا تن عکی
بدست لو ذدن « کنایبه از باخبر بودن
و آ گاه و هشیار بودن باشد .
بدست چب شمر دن - کنابه از
بسیار باشد» چه درحسابقد انامل آحادوهشراث
بانامل دست چپ اختصاص دارد 1
...TAIL...
وهر بمعنی اصل ونراد عم آهده است.
بل گر < مخفف بدکوهر اس تکه بد
اصل و بدزات باشد .
بل گام « ممروف اس تکه اسپ‌بدلجام
باشد یی هیچ دهته را قبول نکند  -‏ وکنایه از
مخالفتر خلاف کننده باشدیعنی کسیکهسرباطاعت
و اقیاد فرو نبارد .
بك لو ن! < بابایحعی‌بروزن‌سرنگون»
بلفت سریانی صمفی‌باشه سیامزنگه» بسرخی‌ماٍدل
مشهور بمقل ازرق . اکربخود ب رکیرند با بخور
کنند بواسیر را تافع است .
بدمموم با دو هیم بروزن‌سرنگون »
بلفت زند و پازند (۱) بممنی ترسیدن و رمیدن
بد نام با نون بروزن سرسام , شهرت
کردن ببدی باشد - ومرشی است که اسب‌واستر
و خر را بهم میرسد و آثرا - اجه گومتد .
۴ رکب از
بتقص نوکفتن نیابد مجال . سعدی شیرازی.
===== leaf 465
مودن باشث .
بد ندان‌خوش هدن « کنابماز
لذت بافتن و محظوظ شدن باشد .
بو » بنتم اول و ثانی و سکون واو »
اسب تندرو را گویند .
بدواد - بر وزن پرواز » بال کشودن
طیور را گوند ‏ و یمن و قرارگاه و آرام
جای باز و شاهی و امثال آبرا نیز گفته اند ۷ .
یدو ره بروزن‌تنوره » طعلمیرا گویند
باشند - و بروزن مسخره عم کن
...TAIL...
ه بودسوآن
دواست قاض . 3
ید سه - بروزن حرسه . چرم و چوبی
باشد مدور که درکلوی دول کنند - و نختهمیان
سوراخی‌رانپز گویند که برسرچوب‌خیمه گذارید .
4 ع بکسر اول بروزن میه » بمعنی
آرژومندی باشد ۵ .
بد له پروز نطله ۰ سخیمرغوبدلکش
باشد ٩‏ - وخواندن شعر را ی زکوند باآهنگه .
یوت « بروزن آفیون» قماش نفیی‌را
بر س بفتح اول و سکون ثانی ؛ بمعنی
۱ - ر : تواز .
۵ .ظ , مصحف » بپوبه . رگ : پوبه .
بلندی هرچیز و استملا هم هست - و بار درخت
د امثال آن ۸ - وتن‌وبدن- و سینه وتان 4-
۴ رك : بده . ۴ .. رگ : ط .
بکر اول ؛ جامةٌ باد روزه < منتهی‌الارب ٩‏ .
۶ منای ۲۱۹ > ۰ ره : بار .
وخ اف ۶ ۸ - بهلوی 026
4۵ شیث _ رك : ندید .
===== leaf 466
و مردمی را نز گویند که در عروسی همرامداهان
بخانة عروی روند .
بر اذا ند - مختف برادراندر اس تکه
پس پدر باشد از زن دیگر » با پر مادرازشوهی
دیگر #
پر اد ۲ ه بروزن تماز » بمعنی‌برازند گین
و زسایی و تیدویی و آوانتتگ باشد ‏ و اهر
باینممنی هیهمت سعتی آراعته کنو نیکو ییاور _"
و چوبکی رانب ز گوبند که کنش گرا
...TAIL...
جهی دهد و آنرا پپروات جمع بشدند » و آن عربی است ودراصل
(برامة) بوده است به‌عنی بری‌الذمه گردیدن از دین, و صواب درجمم آن برامات با براوات است
«قزویتی . تعلبقات چهار مقالا ی *۱۷* . ه برادر - بفتح آول وچهارم» پهلوی 2۲26
و 08۳۵12۴ هوست ۷۸»"اوستا ۲22 «حرن. اسفاا:ص ۰۱۰۲ طبری 932726 «واژه‌نامه۱۰۵»
کلکی 02408۵۲ . نطتری 926۲2 «۵. ۲۸4۱ , سمتانی [08۳26 ؛ منگری 96۲36۲
سرخه ولاسگردی ۰۳6۲ شهمبرزادي 8۲2۲ «4. ۷ ص۱۸۸ » اورامانی ۵8۲2 .«. اورامان
۰ ».۰ اشکاشمی ۷۲۵۵ , زیاکی ۷۵۲۵۵4 ۰ وخی ۷۲۱ . سریکلی ۷۲۵ منگلچی۷۷۳4
منجی ۷6۲21 ۰ بودفا ۷۳۵1 « گربرسن ۰۷۱۰۱ ؛ اخ » پسر که با شخص از مك پدر و مادو
ما ازمکی از آغدو ماشد ‏
```


## [2026-09-14T00:56:48.318Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,t in enumerate(d):\n    if 'پاداش' in t or 'پاسخ' in t:\n        print('leaf',i, [w for w in ['پاداش','پاسخ'] if w in t])\nEOF",
 "description": "Find pādāš/pāsox leaves in BQT v1"
}
```


### [2026-09-14T00:56:49.398Z] TOOL RESULT

```
leaf 39 ['پاسخ']
leaf 163 ['پاسخ']
leaf 228 ['پاسخ']
leaf 229 ['پاداش']
leaf 426 ['پاداش']
leaf 561 ['پاسخ']
leaf 567 ['پاداش']
leaf 576 ['پاسخ']
```


## [2026-09-14T00:56:52.326Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [567,576,577]:\n    print('===== leaf',i); print(d[i][:500]); print('...TAIL...'); print(d[i][-800:])\nEOF",
 "description": "BQT pādāš / pāsox pages"
}
```


### [2026-09-14T00:56:53.410Z] TOOL RESULT

```
===== leaf 567
او
نیز گویند . ۱
پاچیله » بر وزن پانیله . کنش و پا
افزار باشد .
پاخره ‏ بفتح خای نقطه دار و رای
بی نفطه : صفه و نشیدتی را گویند که در پیش
در خانه باژند» ویکسرخای نفطه‌دار نیز گفته‌اند
و بسکون آن هم آحده است .
پاخیره - بر وزن کاجیره , بنای دیوار
و خانه و امثا آن باشد و آنرا بعربی رهص
خواند . ۱
پاخیره دن ‏ بنتح زای هوزوسکون
تون, بنا و گل کار و دبوار کر را گوبند. وسربی
رحاص خوانند .
پاث ۱ بر وزن شاد.بمعنی‌ای ویاسبان
و نگهبان و پاییدن باشد که از دوام و بات ودد
تظر داشتن است - و مامان و دارندگی دا لی
...TAIL...
۰
بمعنی ۳ ست که جزا و مکافاث یکی
باشد . ۱
باداشی * ‌ شتح شین نقطه‌داروسکون
نون» بمعتی پاداشت باشد که جزای نیکی است
چ هکفتاند ,
یت ؛
بگانه‌ای که دودستش کهعطا بدهد
حزار فابده با صد هزار پاداشن ۷ .
پادام ‏ بر وزن آرام , حلقةٌ موی را
کویند. وآن دامیست که ازدم اسب ساند و در
راه جانوران برنده گذارند - و پرنده‌ای‌دا نیز
کفته‌اند که ترديك بدام بندند تا جانوران دیگر
بهوای اوآیند ودردام افتند, واو را بعربی ملواح
خوانند .
پادرر کایه بننتی_موار و مواری :
سفر باشد و کنابه از مهیا بودن و مستمد شدن .
اسباب سفر است - ودم تزع را نیز کفته‌اند که
ابتدای سفر آخرت است- و هرچیز یکه تزديك
بضایم‌شدن باشد عموماً و شراب ی که مادل بشرشی
شده باشد خصوصا . 4
پادسکه -بنتح اك بر وزن پات »
شغنی 8202 (شبان) «اسشق۲1۵».
۴ - بهلوی 02۳15۳0 224
۴ - نگر نيك‌وبد تاچه کردی ز پیش
رد پاداشن ۳
۹ ی ره ": پادای
رك :آي و خرده اوستا ۰.۹۹
===== leaf 576
بر ون دلدگار » بیعتی سار است که فگد
باشد؟ _ ولگد کوب راه مگفتماند - و بضم ثالت
درآب و درخشکی میکنند .
پاسبان ۴ - با بای ابجدبروزنآسمان,
شب زنده دار و محافظت کنندء ۴ باشد؟ .
پاسبان طار م نهم- کابه‌از کر کب
زحل باشد .
پاسبان قلاث - بنمنی پامبان طارم
نهم ات که کوک رحل باشد .
پاسخ؟ -
دار ؛ ۳ در مقابل سوال است .9
پاسره - بنتح ثاك بر وزن تاسره »
زه‌عنی راکه ء بند که‌صاحب زراعت دروجه‌اخراجات
صرف اخراجات دبواای و غيره کنئد .
پاساث - منم ثاكت بروزن نازك. خمیازه
و دهان دره باشد . و بفتح الث یز آمده
ات ۷۸ 
...TAIL...
و بفتح الث یز آمده
ات ۷۸ .
: پاستگه - بر وزن آهنگه, آنچه ند
۱ - رك . یاسار.
بان ( پوند اصاف ) «اسشق ۲۷4».
زر ۱
دیگ ۷
پاسواد -_بممنی سوار پاست که پبادة
و چايك باشد .
پاسه - بی وزن 8 بمعشی تاسه
و تلواسه است که عیل کردن هر چیز -. و غم
واندوه ‏ و فشردن کلو باشد » دباین حعنی بجای
#9 9
پاش بر وزن ماش » بمعشی پربشان
است منی پربشان کن و از هم جدا ساز و بر
افعان .
با شات ۷" فتح الث‌بروزن ناولگ. نمعئی
خمازه باشد۷۷.
باشنا با فون بروژن آشناء یاشنة بارا
کوبند ۷۴- وخیار ثر خربزه و هندوانه و کدو
وامثال آ نرائیز کفته‌اند که‌بجهت نخم نگاهدار بر۴٩۰‏
+ کلتان ۵۱ *.
بارستگه .
ارمنی ۳80285201 < اسخق ۷۵ > جمماً
* را : باشك ۸ ی
. لت نامه». ٩‏ مرک از
نتارکان » « الفهيم بنقل لفت نامه» .
6۰ خاکرا نذمکی ده ی که باش
0 رله : باسكث . ۴ رل : باشنه.
۵ پاسدار - نگاهبان, مراقب :
بزد تیغ بر کردن پاسدار
۴ ره : پاششگه ویاشنگه.
===== leaf 577
۳66 77
و همال پاش ۷ - . .
باشنك - بروزنآونگ , خوشه کوچكث
انگور را کویند - و خیار و خریزه و هندوانه
کدو و امثاآنر" نیز کفته اندکه بجهت نخم
نگاهدارند , و با باهنگك و یاچ جنگ مترادف
لت ۲ :
اس بان فرچندوا
و
انگوریرا نیز کفته اند که برتال خشك شده
باشد ۴ . «د
پاشیب « بر وزنآسیب, نردبان وزیته
یابه را گویند #
هاغر - بر وزن لاغر, ستوئی راکویند
که مقف خانه بدان. قرارگیرد .
پاغره - منم غبن له دار و فتح رای
بی نقطه ؛ مرضی است که پای آ دمی‌مقابل بخیکی
یود وآنرا عربی داء الفیل ۴ خوانند ؛ وبعضی
گویند زحمتی و آ
...TAIL...
کون نون ودال
ابجد . کلولهٌ نب حلاجی کرده را گویند
پاغنده - بنم تالت و فتح دال ابجد .
بمعنی باغند است که كلولة پثبةٌ حلاجی کردم :
رید ثالك هم کفته‌اد که بر وزن
پاغوش - باواو مجهوذبر وزن آغوشی,
ب‌منی غوطه باشد بعنی سرباآب فرو بردن ۷.
بافز اد - مخنف با افزار است که
کنش باشد ۷.
پالك ۵« بر وزن خاك . بدشی صاف
ویی‌غش و پاکیزه باشد - و بمعنی همه وتمام
و باقی هم آمده است ت چنانکه کوبند «حساب‌ا
با شد * ممنی‌تمام‌شدو چیزی نماندو *پابردند»
عنی همه با بردند و چیزینگذاشتند 2
پا کار باکاف بروزن‌نلچار ؛ کسی‌را
گونن دکه چون تحصیل داری بجابی یابد او زد
آزمردم تحصیل کند وبتحصل‌داردهدوشضصی‌رالیز
کویند که‌ستراح‌و ادبخانعراجاروب کند وپا کیزه
اوه وا دای کتای عو اننعت ومنللن خدستر)
لز کفته‌اند ۳
پاکان خط اول کید زاب
و کروبیان و حاملان عرش مملی باشد .
. «لخت نامه >.
« . ۱ ص ۲۹۲
6 وخ 51202 ۳8. سر یکلی 0۷6112 «اره
ی
```


## [2026-09-14T00:57:09.216Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nd=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('pages',len(d))\nfor i,t in enumerate(d):\n    if 'نبرد' in t and i<230 and i>180:\n        print('--- idx',i, t[:80].replace('\\n',' '))\nEOF",
 "description": "BQT v4 nabard"
}
```


### [2026-09-14T00:57:10.327Z] TOOL RESULT

```
pages 553
--- idx 193 [pdf page 194] -۹۱۱۱- : ناروی باشد .3 بجای نون بای حهای نیز بنظرآه«ده است . ناور
--- idx 197 [pdf page 198] بیان دویم در نون با بای ابحد مشتمل بر شانزده لت نباج ۱ « بر وزن ر
--- idx 209 [pdf page 210] ۲۱۷۷ رجل ترجل - بفتح اول و ثالی و ض جیم معروف از مخترعات بوزرجمهر
```


## [2026-09-14T00:57:12.905Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nd=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nt=d[197]\nprint(t[:200]);print('...TAIL...');print(t[-1400:])\nEOF",
 "description": "BQT v4 p.2115 nabard"
}
```


### [2026-09-14T00:57:14.105Z] TOOL RESULT

```
[pdf page 198]
بیان دویم
در نون با بای ابحد مشتمل بر شانزده لت
نباج ۱ « بر وزن رواج , بمعنی ابباغ | وکارزار باشد ۴ چه‌نبردگاه جنکه گاه راکویند
است و آن دو زن باشد که در نکاح که هرد | - ومردم شجاع ودلی
...TAIL...
 کفته‌اند .
با ۴ « با غین ضله‌دار بروزن‌طلاق, فیسه ۸ - بننح اول وئانی وثالث, بمعنی
بممنی نباج است وآن دوژن باشد که درنکاح يك نبی‌است که دخترزاده باشد ؛ و بعضی کویند پر
مردلد - ودختر پر است که لبیره خوانند ؛ وبعضی‌دیگر
نپرد- بفتح اول وثانی‌وسکون را ودال | دختر دختر راکوبند نه پردختررا ؛ وبا تشدید
بی لقطه » بمعنی کوشش وجنکه و حدال و رزم تالی هم کنته‌اند .48
۱-ر4: بباغ («م.) * انباغ (هم.) ۴ - انجمن‌آرا وجه تمبه‌ای برای‌آن آورده
است . بدانجا رجچوع شود ۰ ۴ *انباغ (م.) ورل4: نباج ‏ ۴ < ورد (هم.) وقید
آورد « اسشق ۰۱۶۲۵ پپلوی 81021 ( جنکه . نزاع ) » ایرانی‌باستان 02۳91۳1 (مبارزه
کردن ) « بارتولمه ۸۹۸ * ۰ ورك : لیب رک اس ۱۵۹ ؛ اسشق ۱۹۲۵ ؛ ورك : لبرده ۰ * لیرد »
کارزار باشد . فردومی (طومی )گفت :
فرامرز پیش پدر شد چو کرد به پیروزی روزکار نبرد .۶ « لغت فری ص۹۸ 2 +
8 - باین معنی « نبرده > (ه.م.) و نبردی ( رك :جح ‎٩‏ ) است .
‎٩‏ - از: برد (ه.م.) + ۰ ( پسوند بت و اتصاف ) : * رده ؛ مبارز بود . عنجدی
( مروزی ) گوید :
شاه ابوالقاسم پن تاصن دین آن ببردی ( نبرده . دهشدا ) ملك » لبرده سوار .>
« لغت فری سس ۸۷۹ .۰
۷ "یه (وم.) * نواسه (ه.م.) س نواسی ۳ یه « سيك شناسی ج ۲ص ۷۹+
رك : نواده .
صفت ذات او همین نه بس است که رسول خدای رایس امت .
امیرخرو دهلوی درمنقبت امام ین . * فرهنگه نظام * .
۸ یی (هم.) اه نواسه 38۷282 ( در خراسان متعمل امت ) ( فرزند وه )
« فرهنگه نظام »۳ نواسی ۳ لیسه . رك : نواده ‏
ای بتن تیره‌گر شریفی وکر دون نب کردولی و نبیر کردون ‏
۱ امیرخسرو دهلوی * فرهنگه نظام > -
لبشتی - ر4 : لوشتن .
```


## [2026-09-14T00:57:21.778Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nd=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [486,487,488]:\n    t=d[i]; print('===== idx',i); print(t[:250]); print('...TAIL...'); print(t[-900:])\nEOF",
 "description": "BQT v4 p.2405"
}
```


### [2026-09-14T00:57:22.878Z] TOOL RESULT

```
===== idx 486
[pdf page 487]
هد <<
وجیم فارسی » برطرف شده و معدوم گردیده - هیدخ؟ - بفتح اوز بروزن‌برزخ» اسب
ولاغی‌را کوبند۱ - وکنایه ازاندك وقلیل و کم | تند وتیز وجهنده راکوبند وبعربی طمرخوانند؛
هم آمده ات ده وبجای خای نقطه دار جم هم(۳) آمده است .
هید؟ « بنم | زن 
...TAIL...
 آتش .
(فارسی) هیر .» (رك: هیرید). هرن‌لوید (اسدق‌س۷۸4۹) : « دراوستا وپپلوی -261078 ,5۷
بمعنی آش نیامده » . جهانگیری "هیر کده» را بمعنی آنشکده آورده باستناد این پیت معزی :
درهیر کده گر زمدیح تو بخوانند بیزار شود عیرید از زند وز پازند -
ولی مصراع اول در دبوان معزی مسحح اقبال ص۱۷۹ چنین آهده : در بتکده گر دفتر مدح تو
بخوانند. . رشیدی «هیرمند» (۸.م.) را بهعنی آتش پرست آورده, بدون شاهد . درفغرست ولف
این کلمه بهمین هعنی. آهده وبدین بیت استشهاد شده +
دگر هر کجا رسم آتشکده سث که بی‌هبرمند است وویران شدست.
ولی ولف خود نوشته که درسخهٌ ۷ «هیرید» آبده ودرشاهنامةٌ بخ جه ۱۳۲۹ چنین آهده :
دکر هر کجا رسم آنشکده ست که بی هیربد جای ویران شده ست.
و بنا برین استمال کلمةٌ مزبور در فارسی مسلم نیست, او کوبا فرهنکه لوبسان از وجه اشتقاق
«برید» (ه.م.) با گهجه‌های محلی این معنی را نوشته اند ( در پدتو «هیر» بمعنی‌آتش آمده)
در اوستا 2610۳8 (که برابر ۶ هیر » در «هیرید»] است ) فقط بمعنی آموزش و لیم آمده
(ر4: هیرید) .

===== idx 487
[pdf page 488]
)۲ هیرسا
وعبادت‌هم آمده است۱ - وبزبان علمی اهل‌هند | کویند - وقاضی ومفتی کبران را نیز کفته اند؛
طلا راآکونند. و بسنی خداوند و بزرکه و حاکم آنشکده را

هیراد؟ » بکر اول بر وزن بیداد , | میگوبند - وبمعنی آتش پرست‌هم آهده است-
خودرا بمردم 
...TAIL...
 بلکه رئیس آنشگاه است ,:
معادل 1870106-0811 ( ۳ #598130108-0811. تحت لفظ بممنی « رئیس هیزم قربالی». دو
عنوان مزبور بهم نزدیکند ( بعت 217 ۰ ). از ط1 معتق است : هیر 87ظ
که نمابندء معمولیآ نت *بعنوان مترادف‌آتش بکاررفته. وهی ر کد. 671208 مترادف آتشکده
باد شده است.» اما دراوستا- 26110۳2 ودرپهلوی 812۳ بمعنی آش نیامده ۵ اسشق‌ش۹۸۹ ۱۳ >
ور4: بارتولمه ۲۱۰۲۰؛ پپلوی+613۳202 (در کتیبه‌ها). ۰1367081 1387۳08128188 (هیربدستان)
«اسعق ۰۹۱۱۱۵

«هیربد. قاضی گبران باشد . فردوسی (طوسی) گفت.:

چو برداشت پرده ز در هیربد سیاوش همی بود ترسان ز بد .>

«لغت‌قری م۶۱۰۸ ورك: هین -

۴ - معنی اخیر از دساتیر است «فرهنکه دساتیر ص۳۷۷ .

.8 - #هیرسا بای مجهول وسین مهمله درپرهان بممنی پارساکفته . مولف کوید ظاهرآً
«پیرسا» امالهٌ «پارسا» است که صاحب برهان چنین‌خوانده. آزاینجاست که در کتب معتبرءٌ این فن
دیده شد..» سراج اللغات بنقل « فرهنکه نظام جه سمب > . بایدداست‌این‌کلمه برساختهٌ فرقةٌ
آذرکیوان است . رك: فرهنگه دساتیر ص۲۷۷.

===== idx 488
[pdf page 489]
هیر -۲4۹-
که درتمام عمر با زنان نزدیکی نکرده است . هیرون؟ بکسراول وضم ثالث‌بروزن
هیر ۱4 « بر وزن زبرك . بچة بز را | بیرون» لوعی آزنی‌است وبمربی آفرا قسب‌خوانند
گویند که بزغاله باشد ؛ و پسنی کفته اند که | وآن محکم ومیان پرمیباشد. کوبند 
...TAIL...
یت 1361۵77:280 «بارتولمه ۰۹۹-۱۷۲۸ دربونانی 8۸82820708 «داثرة -
الممارف اسلام . فرادسوی ج ۱۵*۱ ستون ۱ > حوضةٌ رود هامون که شامل قسمتی از ابران
وافغاستان وبلوچستان است قریب 0۰۰۲۰۰۰ کیاومتر مربع مساحت دارد طول رود هیرمند قرب
۰ کیلومتر وطویل ترین رود واقع بین سند و فرات محوب میشود. وی در*۹ کیلومتری
غربی‌کابل در کوه باباسرچشمه میگیرد وراه تاربخی بامیان وپیشاوربفاصله *۲ کیلومتر ازسرچشمة
هیرمند ازروی آن عبورمیکند. این‌رود درقمت علیا بسیارپرآب ودرزمین داور عرض آن‌به۹۰۰٩‏
متر میرسد ودرتایتان از۳*۰ مت ر کمتر لمیشود. شمبهٌ مهم‌آن «ارغنداب» (۸.م.) است که‌م رکب
ازچهارشعبة مختلف میباشد. ر: کیهان. جغرافیای‌طبیمی ۹۹-۹۳. رشیدی کوید: «ساحب قاموس
«دندمند» صحیح کرده و وجهی ندارد.» ۴ - «هیرون, نوعی ازخرماست وکوبند مراد
آزو قسب‌است.» «تحقة حکیم‌موژمن( «وقسب, خرمای‌خشك که دردهان ریز کردد.» «منتهی‌الارب»
ورك: دزی ج» ص۷۷4: هیرونی. فرهنگه نوبسان «قسب» را قسب خوانده بممنی نی کرفته‌اند ۱

۵ - خیری (۸.م.) «رشیدی» .
```


## [2026-09-14T00:57:36.156Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,60p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-14T00:57:36.202Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-14T00:57:42.391Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/preti\" \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B4#Persian\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%B3tis\" \"https://en.wiktionary.org/wiki/%D8%A8%D9%87#Persian\" \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%A7%D8%B1#Persian\" \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%BA%D8%A7%D9%85#Persian\"; do\npython3 tools/fetch_source.py \"$u\" --note \"page 396, root Per 3 (paiti), node verification\" ; done",
 "description": "Archive Wiktionary pages batch 1"
}
```


### [2026-09-14T00:57:47.514Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/edfed86a6f8e7c60.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/34265b212b4ade35.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5cc57d5c414bf99b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bab1c606c00a46a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/69a46a6010475666.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5fcfff4fa55d6792.txt
```


## [2026-09-14T00:57:50.288Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in edfed86a6f8e7c60 34265b212b4ade35 5cc57d5c414bf99b; do echo \"######## $f\"; grep -n -A4 -i \"Etymology\" $f.txt | head -50; done",
 "description": "Read archived pages 1"
}
```


### [2026-09-14T00:57:51.398Z] TOOL RESULT

```
######## edfed86a6f8e7c60
######## 34265b212b4ade35
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
97: Etymology 
98-
99- 2.2 
100- Pronunciation 
101-
--
185: Etymology
186- [ edit ] 
187-
188- Inherited from Middle Persian [Book Pahlavi needed] ( pyš /⁠pēš⁠/ , “ before, pre-, past, beside ” ) , [ 1 ] of unclear further origin. Multiple theories have been proposed: [ 2 ] 
189-
--
369: Etymology
370- [ edit ] 
371-
372- Borrowed from Classical Persian پیش ( pēš ) .
373-
######## 5cc57d5c414bf99b
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
--
140: Etymology
141- [ edit ] 
142-
143- Derksen writes: “It is often assumed that the meaning ‘lord, husband’ derives from an even older meaning ‘self’, as found in pàts” (see Lithuanian pàts ( “ ( singular masculine ) self ” ) ).
144-
```


## [2026-09-14T00:57:55.339Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### preti file head\"; head -40 edfed86a6f8e7c60.txt\necho \"########## pēš theories\"; sed -n '185,225p' 34265b212b4ade35.txt",
 "description": "Read preti + pēš"
}
```


### [2026-09-14T00:57:55.406Z] TOOL RESULT

```
### preti file head
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/preti
FETCHED: 2026-09-14T00:57:44Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found########## pēš theories
 Etymology
 [ edit ] 

 Inherited from Middle Persian [Book Pahlavi needed] ( pyš /⁠pēš⁠/ , “ before, pre-, past, beside ” ) , [ 1 ] of unclear further origin. Multiple theories have been proposed: [ 2 ] 

 proposed etymologies

 Horn takes the word as a derivative of Old Persian [script needed] ( patiš , “ against ” ) , from Proto-Iranian *pati- ( “ against ” ) , itself from Proto-Indo-European *per- ( “ in front; first ” ) ; this is rejected by Hubschmann.

 Nyberg considers the word as a southwestern dialectal form of Old Persian [script needed] ( paišiyā , “ in front, before ” ) ; however, he does not elaborate further. [ 3 ] 

 Gershevitch derives the word from Proto-Iranian *pasya- , from Proto-Iranian *pas- ( “ to observe, look ” ) (with phonetic assimilation of *sy- to š- , à la the shift from Proto-Iranian *kacyápah ( “ tortoise, turtle ” ) to Persian کشف ( kašaf , “ tortoise, turtle ” ) ), from Proto-Indo-European *speḱ- ( “ to see, look, observe ” ) .

 Most likely, according to Edelman, is a derivation from an earlier Proto-Iranian *pati-aši- ( “ before or against one's eyes ” ) , from Proto-Iranian *pati- ( “ against ” ) + *Háši ( “ eye ” ) , the latter from Proto-Indo-Iranian *Hákši ( “ eye ” ) . This would make the word an exact cognate with Sanskrit प्रत्यक्ष ( pratyakṣa , “ present before the eyes, obvious, clear ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈpeːʃ/ 

 ( Dari, formal ) IPA ( key ) : [pʰeːʃ] 

 ( Dari, formal ) IPA ( key ) : [pʰeːʃ] 
 ( Kabuli ) IPA ( key ) : [pʰeːʃ] 

 ( Hazaragi ) IPA ( key ) : [pʰeːʃ] 

 ( Iran, formal ) IPA ( key ) : [pʰiːʃ] 

 ( Tajik, formal ) IPA ( key ) : [pʰeʃ] 

 Rhymes: -eːʃ 

 Readings

 Classical reading ? 

 pēš

 Dari reading ?
```


## [2026-09-14T00:58:11.948Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in bab1c606c00a46a0 69a46a6010475666 5fcfff4fa55d6792; do echo \"######## $f\"; grep -n \"Etymology\" -A8 $f.txt | grep -i -E \"Middle Persian|Proto-Iranian|Avestan|Old Persian|Inherited|From\" | head -12; done",
 "description": "Read be, paykār, payγām"
}
```


### [2026-09-14T00:58:13.089Z] TOOL RESULT

```
######## bab1c606c00a46a0
313- From Middle Persian 𐭯𐭥𐭭 ( pʿn ) / PWN ( pad , “ to, at, in, on ” ) , from Old Persian 𐎱𐎫𐎡𐎹 ( p-t-i-y /⁠patiy⁠/ ) , from Proto-Iranian *pati- . Northern Luri ڤە ( ve ) .
562- From Middle Persian [Term?] ŠPYL / wyh ( weh , “ better, good ” ) , from Old Persian *vahuš ( “ good ” ) , from Proto-Iranian *Hwáhuš , from Proto-Indo-Iranian *Hwásuš , ultimately from Proto-Indo-European *h₁wésus ( “ good ” ) . Northern Luri بێ ( bı ) . Related to Old Armenian վեհ ( veh , “ sublime ” ) , an Iranian borrowing.
650- From Sanskrit अपि ( api , “ close by; also ” ) .
######## 69a46a6010475666
161- From Middle Persian ptkʾl ( “ struggle, battle, dispute ” ) . [ 1 ] Compare Manichaean Middle Persian [script needed] ( phykʾʾr , “ strife, battle ” ) , Avestan 𐬞𐬀𐬌𐬙𐬌𐬀𐬐𐬆𐬭𐬆𐬥𐬀𐬊𐬝 ( pa i tiakər ə naot̰ , “ he fought against ” ) . [ 2 ] The preverb is from Old Persian 𐎱𐎫𐎡𐏁 ( p-t-i-š , “ against, to, towards ” ) , itself from Proto-Iranian *pati- ( “ towards, to, against ” ) , ultimately from Proto-Indo-European *próti , and the root is from Proto-Iranian *kar- ( “ to do, make ” ) , ultimately a derivative of Proto-Indo-European *kʷer- ( “ to do, make, construct ” ) . [ 3 ] [ 4 ] Old Armenian պայքար ( paykʻar ) and Georgian პაექრობა ( ṗaekroba ) are Iranian borrowings. [ 3 ] The preverb is also found in پرهیز ( parhēz , “ abstinence , diet ” ) and پیکر ( paykar , “ form , figure , body ” ) .
######## 5fcfff4fa55d6792
176- Inherited from Middle Persian pgtʾm , compare Manichaean Middle Persian pygʾm , Sogdian [script needed] ( patγām ) , Northern Kurdish pêxemet ( “ sake, in the name of ” ) , pêxem ( “ barrier, obstacle; from the sense of "come against" ” ) , Central Kurdish پێخەم ( pêxem , “ barrier, hindrance; answer ” ) . Ultimately from Old Iranian , from Proto-Iranian *pati- ( “ against ” ) + a formation derived from Proto-Iranian *gam- ( “ to come ” ) , the latter from Proto-Indo-Iranian *gam- , from Proto-Indo-European *gʷem- ( “ to come, step ” ) . Compare also Iranian borrowings: Old Armenian պատգամ ( patgam ) , Aramaic פִּתְגָמָא ( piṯḡāmā ) , Classical Syriac ܦܬܓܡܐ ( peṯəḡāmāʾ ) , Classical Mandaic ࡐࡅࡂࡃࡀࡌࡀ ( pugdāmā ) , Hebrew פִּתְגָּם ( piṯgām ) .
255- Borrowed from Classical Persian پَیْغَام ( payġām ) .
```


## [2026-09-14T00:58:27.884Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pr%C3%B3ti\" \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D9%88%D8%B3%D8%AA%D9%86#Persian\" \"https://en.wiktionary.org/wiki/%D9%BE%D8%B4%DB%8C%D9%85%D8%A7%D9%86#Persian\" \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D9%85%D9%88%D8%AF%D9%86#Persian\" \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D9%87%DB%8C%D8%B2#Persian\" \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%A7%D8%B4#Persian\" \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B3%D8%AE#Persian\" \"https://en.wiktionary.org/wiki/%D9%86%D8%A8%D8%B1%D8%AF#Persian\" \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%A7%D9%86#Persian\" \"https://en.wiktionary.org/wiki/-%D8%A8%D8%AF#Persian\"; do\npython3 tools/fetch_source.py \"$u\" --note \"page 396, root Per 3 (paiti) node verification\" ; done",
 "description": "Archive Wiktionary batch 2"
}
```


### [2026-09-14T00:58:33.950Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/1ab3e70755301a3c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3dd0cdeb2c3d564b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7ad449102377ade8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ff1ec7e37714e55.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/12e5e521ad649169.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1b6e7ec05507d991.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f31f1db613906b88.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/df400ab0b6d930e2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cba6666b233dd9bf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a9324e3531d19b56.txt
```


## [2026-09-14T00:58:38.051Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 1ab3e70755301a3c 3dd0cdeb2c3d564b 7ad449102377ade8 6ff1ec7e37714e55 12e5e521ad649169 1b6e7ec05507d991 f31f1db613906b88 df400ab0b6d930e2 cba6666b233dd9bf a9324e3531d19b56; do echo \"######## $f\"; head -5 $f.txt | sed -n '1,4p'; grep -n -m3 -E \"Inherited from|From Middle Persian|From Proto-Iranian|from Proto-Iranian|Borrowed from\" $f.txt | head -4; done",
 "description": "Read archived batch 2"
}
```


### [2026-09-14T00:58:39.212Z] TOOL RESULT

```
######## 1ab3e70755301a3c
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pr%C3%B3ti
FETCHED: 2026-09-14T00:58:29Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/próti - Wiktionary, the free dictionary
######## 3dd0cdeb2c3d564b
URL: https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D9%88%D8%B3%D8%AA%D9%86#Persian
FETCHED: 2026-09-14T00:58:29Z
STATUS: 200
TITLE: پیوستن - Wiktionary, the free dictionary
148: From Middle Persian [Book Pahlavi needed] ( ptwstn' /⁠paywastan⁠/ ) , [Book Pahlavi needed] ( ptwnd- /⁠paywand-⁠/ , “ to join, to connect ” ) , from Proto-Iranian *pati- + *bándati ( “ to bind ” ) ; see بستن ( bastan ) for the latter element.
615: Persian terms inherited from Proto-Iranian 
616: Persian terms derived from Proto-Iranian 
######## 7ad449102377ade8
URL: https://en.wiktionary.org/wiki/%D9%BE%D8%B4%DB%8C%D9%85%D8%A7%D9%86#Persian
FETCHED: 2026-09-14T00:58:30Z
STATUS: 200
TITLE: پشیمان - Wiktionary, the free dictionary
202: Borrowed from Classical Persian پَشِیمَان ( pašīmān ) .
265: Inherited from Middle Persian [Book Pahlavi needed] ( pšymʾn' /⁠pašēmān⁠/ , “ penitent, repentant ” ) , Northern Luri پںشیمۆ ( pəşimø ) . Akin to Old Armenian փաշաման ( pʻašaman ) , a Middle Iranian borrowing.
367: Borrowed from Classical Persian پَشیمان ۔
######## 6ff1ec7e37714e55
URL: https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D9%85%D9%88%D8%AF%D9%86#Persian
FETCHED: 2026-09-14T00:58:30Z
STATUS: 200
TITLE: پیمودن - Wiktionary, the free dictionary
147: From Middle Persian [script needed] ( ptmwtn', ptmʾd- /⁠paymūdan, paymāy-⁠/ , “ to measure ” ) , ultimately from *pati- and *maH- ( “ to measure ” ) , the latter from Proto-Indo-Iranian *maH- , from Proto-Indo-European *meh₁- ( “ to measure ” ) . 
######## 12e5e521ad649169
URL: https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D9%87%DB%8C%D8%B2#Persian
FETCHED: 2026-09-14T00:58:31Z
STATUS: 200
TITLE: پرهیز - Wiktionary, the free dictionary
179: Borrowed from Classical Persian پَرْهیزْ ( parhēz , “ abstinence, avoiding; diet, fasting ” ) , from Middle Persian [script needed] ( pʾhlyc /⁠pahrēz⁠/ , “ defence; care ” ) .
244: From Middle Persian [script needed] ( pʾhlyc /⁠pahrēz⁠/ , “ defence; care ” ) . Compare Semnani پهریز ( pahriz ) . [ 1 ] 
######## 1b6e7ec05507d991
URL: https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%A7%D8%B4#Persian
FETCHED: 2026-09-14T00:58:31Z
STATUS: 200
TITLE: پاداش - Wiktionary, the free dictionary
156: From Middle Persian pʾtdʾšn' ( pādāšn , “ reward, retribution ” ) . Equivalent to پادـ ( pād-  / pâd- , “ counter-, re- ” ) +‎ دهش ( dahiš  / daheš , “ giving ” ) .
######## f31f1db613906b88
URL: https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B3%D8%AE#Persian
FETCHED: 2026-09-14T00:58:32Z
STATUS: 200
TITLE: پاسخ - Wiktionary, the free dictionary
153: From Middle Persian [script needed] ( pshw' /⁠passox⁠/ ) , [script needed] ( pʾshw' /⁠pāsox⁠/ ) , 𐫛𐫘𐫇𐫟 ( pswx /⁠passox⁠/ ) , from Proto-Iranian *paticahwaH , derived from Proto-Iranian *cánhati , ultimately from Proto-Indo-European *ḱens- . Cognate to Sanskrit शंसति ( śaṃsati ) , Latin cēnseō .
234: Persian terms inherited from Proto-Iranian 
235: Persian terms derived from Proto-Iranian 
######## df400ab0b6d930e2
URL: https://en.wiktionary.org/wiki/%D9%86%D8%A8%D8%B1%D8%AF#Persian
FETCHED: 2026-09-14T00:58:32Z
STATUS: 200
TITLE: نبرد - Wiktionary, the free dictionary
193: Inherited from Middle Persian [Book Pahlavi needed] ( nplt' /⁠nipart⁠/ ) , derived via well-known prefix ni- from the stem of the verb which is in Neo-Persian بردن ( burdan ) .
######## cba6666b233dd9bf
URL: https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%A7%D9%86#Persian
FETCHED: 2026-09-14T00:58:33Z
STATUS: 200
TITLE: پیکان - Wiktionary, the free dictionary
######## a9324e3531d19b56
URL: https://en.wiktionary.org/wiki/-%D8%A8%D8%AF#Persian
FETCHED: 2026-09-14T00:58:33Z
STATUS: -1
TITLE:
```


## [2026-09-14T00:58:59.340Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -i -B2 -A6 \"Etymology\" cba6666b233dd9bf.txt | head -40\necho \"#### proti\"; grep -n -i -A6 \"Iranian\\|Descendants\\|Etymology\" 1ab3e70755301a3c.txt | head -40",
 "description": "Read paykān + próti"
}
```


### [2026-09-14T00:58:59.405Z] TOOL RESULT

```
#### proti
62: Etymology 
63-
64- 1.2 
65- Adverb 
66-
67- 1.2.1 
68- Reconstruction notes 
--
74: Descendants 
75-
76- 1.3 
77- References 
78-
79- Toggle the table of contents 
80-
--
140: Etymology
141- [ edit ] 
142-
143- Possibly from *pró +‎ *-ti . [ 1 ] 
144-
145- Adverb
146- [ edit ] 
--
157: Proto-Iranian *pati and Proto-Hellenic *poti seem to come from *poti , [ 3 ] but they are probably r -less forms of *próti , originating when combined with words containing r . [ 1 ] A similar development probably happened in Latvian pìe from earlier * prie . [ 4 ] 
158-
159- Derived terms
160- [ edit ] 
161-
162- *preti-om 
163- Proto-Italic: *pretjom 
164: Latin: pretium ( see there for further descendants )
165-
166- *próti- h₃kʷ -o-m ( with *h₃ekʷ- ( “ to see ” ) ) 
167-
168: Descendants
169- [ edit ] 
170-
171- Proto-Balto-Slavic: *preti , *prati 
172- Latgalian: pret , pretim , preteims
```


## [2026-09-14T00:59:10.499Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%A8%D8%AF#Persian\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/pati\" \"https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D9%87%D8%A8%D8%AF#Persian\" \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%BA%D8%A7%D8%B1%D9%87#Persian\" \"https://en.wiktionary.org/wiki/%D8%A2%D9%88%D8%B1%D8%AF#Persian\" \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B4%D8%A7%D9%86%DB%8C#Persian\"; do python3 tools/fetch_source.py \"$u\" --note \"page 396, root Per 3 (paiti) node verification\"; done 2>&1 | tail -8",
 "description": "Archive Wiktionary batch 3"
}
```


### [2026-09-14T00:59:14.770Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/16a8715fb6b16e82.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f9823ba1c3b7587b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/37d0e420a6716fef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2f50cf462a90fe12.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/42a1a340c276d032.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/081fa138a8862ae2.txt
```


## [2026-09-14T00:59:18.576Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 16a8715fb6b16e82 f9823ba1c3b7587b 37d0e420a6716fef 2f50cf462a90fe12 42a1a340c276d032 081fa138a8862ae2; do echo \"######## $f\"; sed -n '4p' $f.txt; grep -n -m3 -E \"Inherited from|From Middle Persian|from Proto-Iranian|From Proto-Indo|Borrowed from|Compound of|univerbation\" $f.txt | head -4; done",
 "description": "Read batch 3"
}
```


### [2026-09-14T00:59:19.749Z] TOOL RESULT

```
######## 16a8715fb6b16e82
TITLE: موبد - Wiktionary, the free dictionary
177: Borrowed from Persian موبد ( mowbed, mubed , “ mobad ” ) .
205: Borrowed from Arabic مُؤَبَّد ( muʔabbad , “ everlasting ” ) .
######## f9823ba1c3b7587b
TITLE: 
######## 37d0e420a6716fef
TITLE: سپهبد - Wiktionary, the free dictionary
147: From Middle Persian 𐭮𐭯𐭠𐭧𐭯𐭲𐭩 ( spāhbed ) , from Old Persian *spādapatiš , from Proto-Iranian *cwaHdapatiš ( “ commander of the army ” ) . By surface analysis , سپاه ( sepâh , “ army ” ) +‎ ـبد ( -bod , “ lord, master ” ) .
200: Persian terms inherited from Proto-Iranian 
201: Persian terms derived from Proto-Iranian 
######## 2f50cf462a90fe12
TITLE: 
######## 42a1a340c276d032
TITLE: آورد - Wiktionary, the free dictionary
177: Inherited from Proto-Turkic *aḏurt ( “ cheek pouch ” ) ; cognate with Azerbaijani ovurd .
######## 081fa138a8862ae2
TITLE: پیشانی - Wiktionary, the free dictionary
176: Borrowed from Persian پیشانی ( pišâni , “ forehead ” ) .
277: Borrowed from Classical Persian پیشانی .
```


## [2026-09-14T00:59:26.520Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -i \"battle\\|combat\\|āvard\\|âvard\" 42a1a340c276d032.txt | head -10",
 "description": "Check āvard battle"
}
```


### [2026-09-14T00:59:26.567Z] TOOL RESULT

```
296: âvard
305: آورد • ( âvard )
```


## [2026-09-14T00:59:28.503Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '285,330p' 42a1a340c276d032.txt",
 "description": "āvard Persian section"
}
```


### [2026-09-14T00:59:28.539Z] TOOL RESULT

```
 Classical reading ? 

 āward

 Dari reading ? 

 āward

 Iranian reading ? 

 âvard

 Tajik reading ? 

 ovard

 Verb
 [ edit ] 

 آورد • ( âvard ) 

 third-person singular past indicative of آوردن ( âvordan ) 

 Pronunciation 3
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔaː.ˈwurd/ 

 ( Dari, formal ) IPA ( key ) : [ʔɑː.wʊ́ɹd̪] 

 ( Dari, formal ) IPA ( key ) : [ʔɑː.wʊ́ɹd̪] 
 ( Kabuli ) IPA ( key ) : [ʔɑː.wʊ́ɹd̪] 

 ( Hazaragi ) IPA ( key ) : [ʔɔː.wúɹd̪̥] 

 ( Iran, formal ) IPA ( key ) : [ʔɒː.vóɹd̪̥] 

 ( Tajik, formal ) IPA ( key ) : [ʔɔ.vúɹd̪] 

 Rhymes: -urd 

 Readings

 Classical reading ?
```


## [2026-09-14T00:59:39.697Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"پدرام\\|پادافره\\|پاداش\\|آوردگاه\" FSF_pages.txt | head -10\necho \"=== pages count\"; python3 -c \"print(open('FSF_pages.txt',encoding='utf-8',errors='replace').read().count(chr(12)))\"",
 "description": "FSF Shahnameh glossary"
}
```


### [2026-09-14T00:59:40.906Z] TOOL RESULT

```
1592: ‫آوردگاه‬
1630:                            ‫آوردگاه آ=وردکه‬            ‫بپرسش‪ ,‬بدو گفت ز انباز خویش‬
1641:                                  ‫کن‬                         ‫بسندست با او به آوردگاه‬
1690: ‫(‪)۵-۲۷۲۰-۹۲۶‬‬                                     ‫جز آویختن نیست پاداش این‬
2840: ‫بر پاداشتن» از جای جنباندن و جهانیدن‪.‬‬           ‫ازینسان که هستی بپنداشتم‬
3357:             ‫بازخواست‪ .‬سزای گناه پاداش‪:‬‬                 ‫(‪)۵-۳۲-۹۴۲‬‬
3371:                       ‫رسستم پس از‬                           ‫بحر و ابرست روز پاداشن‬
3381: ‫(‪)۸۸۱-۷۱۸-‬‬                                     ‫چه پاداش و چه بادافره نمودم‬
6264:‫که پاداش این آنکه بسی‌جان شود‬           ‫نماندی که پایش برفتی ز جای‬
6268:                                                                ‫باداش = پاداشن =‬
=== pages count
484
```


## [2026-09-14T00:59:45.805Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,t in enumerate(d):\n    if 'پاداشن' in t:\n        print('leaf',i)\n        print(t[:1200])\n        print('---')\n        break\nEOF",
 "description": "FSF pādāšn leaf"
}
```


### [2026-09-14T00:59:46.942Z] TOOL RESULT

```
leaf 75
 ‫شدن سهراب‬          ‫کشته‬
                       ‫رسستم پس از‬                           ‫بحر و ابرست روز پاداشن‬
                           ‫(‪:)۲-۰۴۲-۹۳4‬‬         ‫وهرست گاه بادافراه‬
                                                                 ‫چرخ د‬

         ‫گورد‬
            ‫نشست از بر رخش رستم چ‬                 ‫از فخر گرگانی (‪۵۶۱-۵۴‬و ‪:)۱۶۲-۶۳۱‬‬
‫پراز خون رخ و لب پر از باد سرد‬                              ‫راگفت شاهاکامگارا‬          ‫مرو‬
        ‫گشت لرزان و رخ لاژورد‬        ‫تش‬         ‫تهرسانی به پادافراه مارا‬
                                                                       ‫چ‬
‫پراز حون جگر دل پر از باد سرد‬                            ‫ترازین پیش بسیار آزمودم‬
 ‫(‪)۸۸۱-۷۱۸-‬‬                                     ‫چه پاداش و چه بادافره نمودم‬
         ‫اگزرفخگرانی (ویس ‪:)۴۷۳-۱۷۴‬‬                                                ‫بادپا‬
       ‫برآرم سرد بادی زین دل ریش‬                             ‫تیزتگ‪:‬‬      ‫ار»‬
                                                                           ‫وسب‬
                                                                             ‫هزا‬
                                                                   
---
```


## [2026-09-14T01:00:00.959Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor w in ['آوردگاه','پرهیز','پیمودن','پاسخ']:\n    ls=[i for i,t in enumerate(d) if w in t]\n    print(w, ls[:6])\nEOF",
 "description": "FSF leaf positions"
}
```


### [2026-09-14T01:00:02.200Z] TOOL RESULT

```
آوردگاه [40, 41, 131, 151, 402]
پرهیز [13, 30, 132, 148, 149, 174]
پیمودن [87, 106, 162, 163, 294, 394]
پاسخ [11, 16, 18, 25, 26, 40]
```


## [2026-09-14T01:00:20.731Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB\"; for w in \"pēš\" \"pad \" \"-bed\" \"pādāšn\" \"paywastan\" \"nibard\" \"passox\" \"paymūdan\" \"pahrēz\" \"patkār\" \"paygām\" \"pašēmān\"; do printf \"%-12s\" \"$w\"; grep -c \"$w\" NYB_vol2_glossary.txt; done\necho \"=== NYB pat\"; grep -n -o -E \".{80}p(a|ē)š(ēmān|)[^a-z].{120}\" NYB_vol2_glossary.txt | head -3",
 "description": "Nyberg glossary greps"
}
```


### [2026-09-14T01:00:21.831Z] TOOL RESULT

```
=== NYB
pēš         26
pad         11
-bed        4177
pādāšn      0
paywastan   0
nibard      0
passox      0
paymūdan    0
pahrēz      0
patkār      2
paygām      0
pašēmān     3
=== NYB pat
ugrep: error: error at position 26
(?m).{80}p(a|ē)š(ēmān|)[^a-z].{120}
                      \___empty (sub)expression
```


## [2026-09-14T01:00:26.559Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"patkār\" \"pašēmān\" \"pēš\" \"patmān\" \"patwand\" \"pātaxšāh\"; do echo \"=== $w\"; grep -n -o -E \".{100}${w}.{180}\" NYB_vol2_glossary.txt | head -2; done",
 "description": "Nyberg entries"
}
```


### [2026-09-14T01:00:27.766Z] TOOL RESULT

```
=== patkār
=== pašēmān
2996:mānēh [pšym'nyh] repentance 10?!. 128, 6822. — MPrs pšym'n(yg) ‘repentant’ (S); Paz. pašēmg, abstr. pašēmānī; NP pasimän, pišmān, pizman, abstr. pašī- mani, pišmānī. Of NW origin: paše the NW form corresponding to SW pasé (q. v.) + *mdna- ‘measure’, ‘repentance’ being understood as an '
=== pēš
817:lt!], opt. pass. 3d p.sg. ävurt he [HWH-d] 218: to bring a th. to a p. (6) 218 (avis, g. v.). 6% (6 pēš i); 1576 (6 en giyāk to this place here); 76°. 10915, 113; 6 ē giyak ~ to put together, to compose 1192-21; to fetch down 40?!; to inflict (a punishment) 9°; to acquire (a name, 
2874:on the tracks of, on the heels of 71%. — An ad- verbial formation, on the pattern of fräceh, pasēh, pēšēh, ulēh etc., from pad-, the weak st. of pdd- (v.s. v. pad), cf OP Loc. ni-padiy adv. ‘in pursuit’, prep. with acc. ‘in pursuit of’; Bal p'adā ‘after, behind’ (Gilbertson and Long
=== patmān
=== patwand
=== pātaxšāh
```


## [2026-09-14T01:00:40.615Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 188 312 315 345 356 362 363 364 265; do echo \"=== HUB no $n\"; grep -n -A12 \"^ *$n\\.\" HUB.txt | head -16; done 2>&1 | head -120",
 "description": "Hübschmann entries by Horn number"
}
```


### [2026-09-14T01:00:41.766Z] TOOL RESULT

```
=== HUB no 188
=== HUB no 312
1371:312. Die Form piSman u. s. w. ist verkiirzt aus paslman, das
1372-auch ins Afgh. {pa§Tmcin Veuig') iibergegangen ist. Vgl.
1373-paz. poSetnan repentant', paSSmam 'penitence' Shk. 263,
1374-Min. Gl. 157, phi. paSSmdnlh 'Reue* Phi. Min. p. 5, Z. X5,— 41 —
1375-Die Sanskritubersetzung giebt das paz. Wort durch
1376-pagdnttdpin- Veuig* wieder. Es wird irgendwie zu zd.
1377-pasda nachher und Wrzl. man *denken* gehOren und
1378-urspriinglich *nachher-bedenkend* bedeutet haben.
1379-313. Die von Noldeke und Horn erwahnte Form gu^s-
1380-murdan des Judenpersischen zeigt, dass piSmurdan
1381-'verwelken iiber alteres bizmurdan (Noldeke, ZDMG.
1382-45, 106) auf *vizmurdan zuriickgeht. Damit fallt
1383-Horn's Etymologic, insbesondere piz- aus patis.
=== HUB no 315
=== HUB no 345
1494:345. Ap. patiy als 1. Glied von Comp. ist neup. zu paS
1495-(vor Vocalen), pa (vor c, s, 5), pai (vor den ubrigen
1496-Consopanten) geworden, ap. *patiy' zu pad-, pa-,
1497-tJber das selbstandige patiy vgl. Nr. 144.
1498-346. Fiige hinzu 2) pai *Sehne* = afgh. pala *Sehne*
1499-(Geiger, Etym. und Lautl. des Afgh. Nr. 158) aus
1500-iran. *padd,
1501-347 ^*^ Anm. Vgl. sTvend pTdm 'marjolaine' = np. pudana
1502-(Journ. asiat. 1893, 258).
1503-349. Bei der Erklarung von paidd 'sichtbar, oflfenbar, klar
1504-kommt alles darauf an, ob es zu dem phi. patyak der
1505-Hajlabad-Inschrift gehSrt oder nicht. Im ersten Falle
1506-ware patyak durch Epenthese zu phi. paitak = u^.paida
=== HUB no 356
1540:356. Np. pes Vor' = paz. phi. pSs (61. and Ind. 113—114)
1541-^= bal. pSs = arm. pBS- (in Lehnwortern) ist jeden-
1542-falls nicht = ap. pati§, Dass auch kein Grund vor-
1543-handen ist, np. piS- auf ap. patis zuriickzufuhren, ist
1544-oben Nr. 312—314 gezeigt. Nach np. paskam = arm.
1545-patskamh = zd. ^paiti'skemba- (oben Nr. 314) soUte
1546-man np. pas- fiir ap. patis- (in Comp.) erwarten. —
1547-Np. pi^x^ar hat seiner Bedeutung nach nichts mit
1548-dem angefiihrten phi. pati§x^ar zu thun.
1549-359. Np. paig Tussganger = syr. N3^£> Noldeke,
1550-Alexanderroman p. 14, arab. /ai/, phi. paik West,
1551-Pahl. Texts II, 280, plur. paikan Yatk. i. Zar. p. 50,
1552-*) *A long robe, a shirt or shift*.— 46 —
=== HUB no 362
=== HUB no 363
=== HUB no 364
=== HUB no 265
1158:265. Nach den Bemerkungen der pers. Lex. bei Vullers zu
1159-urtheilen, existiert ein np. pad 'Schiitzer iiberhaupt
1160-nicht. Siehe unter Nr. 273, Sonst hatte pad = ap.
1161-nom. sg. *p<it€L gesetzt werden miissen, wie dGst Treund'
1162-=- ap. dausta ist. Vgl. ZDMG. 38, 426; WZKM. 1,
1163-249; 8, 92.
1164-265 ^^^ Np. paddS Tergeltung, Belohnung bei Fird. I, 437,
1165-Z. 1. Vgl. g. padas 'Belohnung, Rache* ZDMG. 36, 76,
1166-afgh. LW. podcis 'retaliation*. Daneben np. padds
1167-JRAS. 1894, 450.
1168-266. Zu pad' vgl. Nr. 275.
1169-268. Wie passt der Sinn von pddyab rituelle Waschung'
1170-zu zd. paityapem 'stromauf ?
```


## [2026-09-14T01:00:56.303Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o -E \".{0,80}\\bpreti\\b.{200}\" AHD_watkins1985.txt | head -5\necho \"=== per1\"; grep -n -o -E \".{0,40}per-?1.{400}\" AHD_watkins1985.txt | head -3\necho \"=== per5 strike\"; grep -n -o -E \".{0,60}To strike.{200}\" AHD_watkins1985.txt | head -5",
 "description": "Watkins AHD per"
}
```


### [2026-09-14T01:01:05.746Z] TOOL RESULT

```
=== per1
ugrep: error: error at position 81
bf][\x80-\xbf]*){400}
                     \___exceeds complexity limits


=== per5 strike
ugrep: error: error at position 84
-\xbf][\x80-\xbf]*){200}
                        \___exceeds complexity limits
```


## [2026-09-14T01:01:09.282Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"preti\" AHD_watkins1985.txt | head -5\necho \"=== per. heads\"; grep -n -E \"^per-?[0-9]?\\.|^ *per-[0-9]\" AHD_watkins1985.txt | head -20\necho \"=== 'To strike'\"; grep -n \"To strike\" AHD_watkins1985.txt | head -10",
 "description": "Watkins AHD greps 2"
}
```


### [2026-09-14T01:01:09.362Z] TOOL RESULT

```
844:fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
=== per. heads
840:per-3. The young of an animal (< “a bringing forth,” “offspring”), Derivative root belonging to the group of per'. Suffixed o-grade form *por-si- in Germanic *farzi-, young cow, in Old English fearr, calf, and compound heahfore, calf (first element obscure): HEIFER. [In Pok. 2. D. per 818.]
=== 'To strike'
325:English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source of English BANG!; b. Swedish dia- lectal bangla, to work inefficiently, akin to the possible Scandinavian source of English BUNGLE. 2. Possibly Germanic nasalized forms *bankiz and *bank6én-, bank of earth (possibly < “feature where the contour of the ground is broken,” escarpment, riverbank, possibly also associated with “manmade earthwork’’), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank, akin to the Scandinavian source of BANK}; c. Old High German banc, bank, bench, moneychanger’s table (> Italian banca): BANK?, BANT- LING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic suffixed form *bidn- in Old English 6é0, a bee: BEE}. [Pok. bhei- 116.] bhei-2. To strike. 1. Germanic suffixed form *bili- in Old English bile, bird’s beak: BILL?. 2. Germanic suffixed form *bilja- in Old English bil), sharp weapon: BILL’. [Pok. bhei(a)- 117.] bheid-. To split; with Germanic derivatives referring to biting (hence also to eating and to hunting) and wood- working. 1. Germanic *bitan in Old English *bitan, to bite: BEETLE!, BITE. 2. Zero-grade form *bhid- in: a. Ger- manic *bitiz in Old English bite, a bite, sting: B1T?; b. Germanic *bitén- in Old English bita, a piece bitten off, morsel: BIT!; c. Suffixed form *bhid-ro- in Old English bit(tjer, ‘‘biting,’’ sharp, bitter: BITTER. 3. O-grade form *bhoid- in Germanic *baitjan in: a. Old Norse beita (verb), to hunt with dogs, and beita (noun), pasture, food: BAIT!; b. Old French beter, to harass with dogs: ABET. 4. Germanic *bait-, a boat (< “dugout
340:bheue-. Also bheu-. To be, exist, grow. I. Extended forms *bhwiy(o)-, *bhwi-. 1. Germanic *biju in Old Eng- lish béon, to be: BE. 2. Latin fieri, to become (third person singular present subjunctive fiat): FIAT. 3. Possi- bly suffixed form *bhwi-lyo- in Latin filius, son; but this is possibly from dhé(i)-. II. Lengthened o-grade form *bhéw- in Germanic *béwan in: a. Old Norse bia, to live, prepare (present participle bondi); BONDAGE, BOUND‘; HUSBAND; b. Middle Dutch bouwen, to cultivate: BOW- ERY; C. Old Danish bdth, dwelling, stall, akin to the Scandinavian source of Middle English bothe, market stall: BooTH. III. Zero-grade form *bhu-. 1. Germanic *buthia in: a. Old English bold, dwelling, house, hence byldan, to build: BUILD; b. alternate Germanic form *béthla in Middle Dutch bédel, riches, property: BOoo- DLE. 2. Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE, PHYTO-, PHYTON; DIAPHYSIS, DIPHY- ODONT, EPIPHYSIS, HYPOPHYSIS, IMP, MONOPHYSITE, NEOPHYTE, PERIPHYTON, SYMPHYSIS, TRACHEOPHYTE. 3. Suffixed form *bhu-td- in Welsh bod, to be: EISTEDD- FOD. 4, Suffixed form *bhu-tu- in Latin futirus, “that is to be,” future: FUTURE. IV. Zero-grade form *bhii- (< *bhua-). 1. Germanic *biiram, dweller, especially farmer, in: a. Old English bir, “dwelling space,” bower, room: BOWER}; b. Old English gebir, dweller (ge-, collective prefix; see kom): NEIGHBOR; Cc. Middle Dutch gheboer, ghebuer, peasant: BorR, Boor. 2. Germanic *birjam, dwelling, in Old English byre, stall, hut: BYRE. 3. Suf- fixed form *bhi-lo- in Greek phulon, tribe, class, race, and phulé, tribe, clan: PHYLE, PHYLETIC, PHYLUM; PHY- LOGENY. V. Suffixal forms in Latin. 1. *du-bhw-io-, “being two,” in Latin dubius, doubtful, and dubitdre, to doubt (see dwo-). 2. *pro-bhw-o-, “growing well or straightforward” (see per'). 3. *super-bhw-o-, “being above,” in Latin superbus, superior, proud (see uper). VI. Possibly Germanic *baumaz (and *bagmaz), tree (? < “growing thing”), in: a. Old English béam, tree, beam: uel b. Middle Dutch boom, tree: BooMm?. [Pok. bheu- 146. bheug-'. To flee. 1. Zero-grade form *bhug- in Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE. 2. Extended form *bhuga in: a. Latin fuga, flight (> fugdre, to drive away): -FUGE, FUGUE; FEBRIFUGE; b. Greek phugé, flight: APOPHYGE. [Pok. 1. bheug- 152.] bheug-2. To enjoy. Nasalized zero-grade form *bhu-n-g- in Latin fungi, to discharge, perform: FUNCTION, FUNGI- BLE; DEFUNCT, PERFUNCTORY. [Pok. 4. bheug- 153.] bheug-*. To bend; with derivatives referring to bent, pliable, or curved objects. 1. Germanic *baugaz in: a. Old English béag, a ring: BEE?; b. Old High German boug, a ring: BAGEL. 2. Germanic *bugon- in: a. Old English boga, a bow, arch: Bow’; b. compound *alino- bugén-, “bend of the forearm,” elbow (*alino-, forearm; see el-'), 3. Germanic biégan in Old English bigan, to bend: Bow?, BUXxOM. 4. Germanic causative form *baug- Jan in Old Norse beyla, a swelling, akin to the probable Scandinavian source of Middle English baile, baill, a handle: Barn’. 5. Germanic *buhtiz in Old English byht, a bend, angle: BIGHT. 6. Celtic *buggo-, “flexible, mallea- ble,” in Scottish and Irish Gaelic bog, soft: BoG. [Pok. 3. bheug- 152.] bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153,] bhiad-. To worship. Suffixed form *bhildd-(s)men- in Latin flamen, priest (of a particular deity): FLAMEN. [In Pok. bhlag-men- 154.] bhlag-. To strike. 1. Germanic *blak-, perhaps in the probable Scandinavian source of Middle English bakke, bat: BAT?. 2. Latin flagrum, a whip (> flagellum, little whip): FLAGELLATE, FLAGELLUM, FLAIL, FLOG. 3. Latin
342:flagitdre, to demand importunately: FLacitious. [Pok. bhlag- 154.] bhlagh-men-. Form, ritual form. Sanskrit brahmd, brah- man-, priest, and brahma, bréhman-, prayer: BRAHMA!, BRAHMAN, (BRAHMIN). [Pok. bhlagh-men- 154.] bhlé-1. To howl. Probably imitative. 1. Germanic suffixed form *blé-t- in Old English b/gtan, to bleat: BLEAT. 2. Germanic suffixed form *b/é-r- in Middle English bleren, to roar: BLARE. 3. Latin flére, to weep: FEEBLE. [Pok. bAlé- 154.] bhié-2, Also bhla-. To blow. 1. Germanic suffixed form *blé-w- in Old English blawan, to blow: BLow!. 2. Ger- manic suffixed form *blé-dram, “something blown up,” in: a. Old English blZdre, blister, bladder: BLADDER; b. Old Norse bladhra (noun), bladder, and bladhra (verb), to prattle: BLATHER. 3. Germanic extended form *blés- in: a. Old English b/ést, a blowing, blast: BLAST; b. Middle Dutch blas(e), a bladder: stncLass. 4. Variant form *bhid- in Latin flare, to blow (> flabellum, fan): FLABELLUM, FLATUS, FLAVOR; AFFLATUS, CONFLATE, (DEFLATE), INFLATE, SOUFFLE. [In Pok. 3. bhel- 120.] bhlei-. To blow, swell. Extension of bhel-2. 1. Germanic *blajjinén-, a swelling, in Old English blegen, a boil, blister: BLAIN. 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhiei- 156.] bhleu-. To swell, well up, overflow. Extension of bhel-?. 1. Possibly Germanic *b/aut- in Old Norse blautr, soft, wet: BLOAT. 2. Extended form bhleug~- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (IN- FLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS. 3. Zero-grade form *bhlu- in Greek phluein, phluzein, to boil over: PHLYCTENA. 4. Possibly Greek phloos, phioios, tree bark (< “swelling with growth”): PHLOEM. [Pok. bhileu- 158.] bhlig-. To strike. Latin fligere, to strike: AFFLICT, CON- FLICT, INFLICT, PROFLIGATE. [Pok. bhlig- 160.] bhoso-. Naked. Germanic *bazaz in: a. Old English bzr, bare: BARE!; b. Old Swedish and Old Danish bar, bare: BALLAST. [Pok. bhoso-s 163.] bhrag-. To smell. 1. Germanic *brak- in Old High Ger- man bracc(h)o, dog that hunts game by scent: BRACH. 2. Suffixed form *bhrag-ro- in Latin fragrdre, to smell: FLAIR, FRAGRANT. [Pok. bhrag- 163.] bhrater-. Brother, male agnate. 1. Germanic *brdthar- in Old English bréthor, brother: BROTHER. 2. Latin frdter, brother: FRA, FRATERNAL, FRIAR; CONFRERE, FRATRI- CIDE. 3. Greek phratér, fellow member of a clan: PHRATRY. 4, Sanskrit bhratd, bhrdatar-, brother: PAL. [Pok. bhrdater- 163.] bhreg-. To break. 1. Germanic *brekan in: a. Old English brecan, to break: BREAK; b. Old English bréc, a break- ing: BREACH; c. Old High German brehhan, to break, akin to the Germanic source of Italian breccia, breccia: BRECCIA; d. Old French breier, to break: BRAY?; e. Old French brier (dialectal) and broyer, to knead: BRIOCHE. 2. Germanic *brak-, bushes (< “that which impedes motion”), in Old Norse *brakni, undergrowth, akin to the probable Scandinavian source of Middle English brake(n), bracken: BRACKEN, BRAKE’, BRAKE‘, 3. Nasal- ized zero-grade form *bhr-n-g- in Latin frangere, to break: (FRACTED), FRACTION, (FRACTIOUS), FRACTURE, FRAGILE, FRAGMENT, FRAIL!, FRANGIBLE; ANFRACTU- OUS, CHAMFER, DIFFRACTION, (INFRACT), INFRANGIBLE, INFRINGE, OSSIFRAGE, REFRACT, (REFRAIN?), (REFRIN- GENT), SAXIFRAGE, SEPTIFRAGAL. 4, Latin suffrdgdri, to vote for (? < “to use a broken piece of tile as a ballot”), hence suffrdgium, the right to vote: SUFFRAGAN, SUF- FRAGE. [Pok. 1. bhreg- 165.] bhréi-. Also bhri-. To cut, break. 1. Possibly Latin fricdre (> French frotier), to rub: FRAY?, FRICATIVE, FRICTION, FROTTAGE; AFFRICATE, DENTIFRICE. 2. Possi-
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
566:kae-id-. To strike. 1. Latin caedere, to cut, strike: CAE- SURA, CEMENT, CESTUS2, CHISEL, -CIDE, SCISSORS; AB- SCISE, CIRCUMCISE, CONCISE, DECIDE, EXCISE2, INCISE, PRECISE, RECISION. 2. Latin caelum (? < *caedum), sculptor’s chisel: CAELUM. [Pok. (s)k(h)ai- 917.] kagh-. To catch, seize; wickerwork, fence. 1. Germanic *hag- in: a. Old French hagard, wild, wild hawk (< “raptor”): HAGGARD; b. Germanic *hagén- in Old Eng- lish haga, hedge, hawthorn: HAW?; c. Germanic *hagj6é in Old English hecg, hedge: HEDGE. 2. Suffixed unaspirated form *kag-yon- in Gaulish caio, rampart, retaining wall (> Old French quai, quay): (CAY), KEY?, QUAY. 3. Possi- ble variant *kogh- in: a. Latin cohum, strap from yoke to harness: INCHOATE; b. possibly Latin cdlum, sieve (< wickerwork), and its derivative céldre, to filter: COLAN- DER, COULEE, (COULOIR), CULLIS; PERCOLATE. [Pok. kagh- 518.]
602:kel-1, To strike, cut. Hypothetical base of derivatives referring to something broken or cut off; twig, piece of wood. I. Basic form *kel- in suffixed o-grade form *kol-o- in Greek kolos, docked, kolobos, maimed: COLOBOMA. II. Extended form *keld-. 1.Germanic *helt- in Old English hilt: HILT. 2. Zero-grade extended form *kid- in a. Germanic *hulta- in Old English holt, wood: HOLT; b. Greek klados, branch, shoot: CLADOCERAN, CLADODE, CLADOGENESIS, CLADOPHYLL, PHYLLOCLADE. 3. Variant Celtic zero-grade extended form *klad- in: a. suffixed form *klad-yo-, Celtic source of Latin gladius, sword: GLADIATE, GLADIATOR, GLAIVE; b. suffixed form *klad- ibo- in Gaelic claidheamh, sword: CLAYMORE. 4. O-grade extended form *kold- in: a. Germanic *haltaz, “with a broken leg,” in Old English compound lemphealt, limp- ing, halting (lemp-, hanging loosely; see leb-'), probable source of obsolete limphalt, lame: LIMP; b. Germanic derivative verb *haltén in Old English healtian, to limp: HALT’, III. Extended form *keb-. 1. Zero-grade form *klo- in: a. Greek kia- in (i) Greek klan, to break: CLAST, CLASTIC; CLASMATOCYTE, OSTEOCLAST, PLAGIOCLASE (ii) Greek klén (< *kla-6n), twig: CLONE; b. suffixed form *klo-ro- in Greek kléros, lot, allotment (< “that which is cut off”): CLERK; C. suffixed form *kb-mn in Greek kléma, twig: CLEMATIS; d. suffixed form *kb-mo- in Latin calamitds, injury, damage, loss: CALAMITY. 2. O-grade form *kob- in suffixed form *kols-bho- in Greek kolaphos, a blow: coPE!, coup. See extension kleg-. [Pok. 3 kel- 545.]
844:fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
859:plak-2. To strike. 1. Nasalized variant forms *pla-n-k-, *pla-n-g- in: a. Germanic *flang- in Old Norse flengja, to flog, whip, akin to the Scandinavian source of Middle English flingen, to fling: FLING; b. Latin plangere, to strike (one’s own breast), lament: PLAINT, PLANGENT; COMPLAIN. C. suffixed form *plang-yo- in Greek plazein, to drive away, turn aside: PLANKTON. 2. Variant form *plag- in Latin plaga, a blow, stroke: PLAGUE. 3. Suf- fixed form *pldk-yo- in Greek pléssein, to beat, strike: PLECTRUM, -PLEGIA, PLEXOR; APOPLEXY, CATAPLEXY, PARAPLEGIA. [Pok. 2. pldk- 832.]
951:slak-. To strike. 1.Germanic *slahan in Old English sléan, to strike, kill: sLay. 2. Germanic suffixed form *slag-j6- in Old English slecg, hammer: SLEDGEHAMMER. 3. Germanic suffixed form *slah-tram in Old Norse sidtr, butchery, “striking,” probably akin to the Scandinavian source of Middle English slaughter, killing: SLAUGHTER. 4. Germanic *slag- in: a. Old High German slag (> German Schlag), a blow: scHLOocK; b. Middle Dutch slag, a blow: ONSLAUGHT; C. probably Middle Low Ger- man slagge, metal dross (< “that which falls off in the process of striking”): SLAG. 5. Germanic suffixed length- ened-grade form *slégiz in Old Norse sl@gr, clever, cunning (< “able to strike”): SLEIGHT, SLY. [Pok. slak- 959.]
1142:HELMINTH; ANTHELMINTIC, PLATYHELMINTH. [Pok. 7. uel- 1140.] wel-‘, To tear, pull. 1. Suffixed form *wel-do- in Latin vellere, to tear, pull: AVULSE, CONVULSE, DIVULSION, EVULSION, REVULSION, SVELTE. 2. Suffixed form *wel-no- in Latin vullis, shaggy hair, wool: VELOURS, VELVET, VILLUS [Pok. 8. wel- 1144.] wele-'. Wool. Probably related to wel-‘. 1. Suffixed extended zero-grade form “*wi-nd- in: a. Germanic *wullé in Old English wul(l), wool: woot; b. Italic *wland in Latin lana (> French laine), wool, and its derivative laénig6, down: LANATE; DELAINE, LANIFER- OUS, LANOLIN, LANUGO; ¢. Celtic *wland in Welsh gwlan, wool (> Middle English flannel, woolen cloth): FLANNEL. 2. Possible suffixed o-grade form *wol(o)-no- in Greek oulos, wooly, curly: ULoTRICHOUs. [Pok. 4. uel- 1139.] wela-2. To strike, wound. 1. Suffixed o-grade form *wol()-o- in Germanic *walaz in Old Norse valr, the slain in battle in: a. Old Norse Valhdéll, Valhalla: VAL- HALLA; b. Old Norse Valkyrja, “chooser of the slain,” name of one of the twelve war goddesses (-kyrja, chooser; see geus-): VALKYRIE. 2. Suffixed basic form *welo-nes- in Latin vudnus (stem vulner-), a wound: VULNERABLE. [In Pok. 8. wel- 1144.] welg-. Wet. Germanic *welk- in: a. Old English wolc(e)n, cloud, sky: WELKIN; b. Middle English welken, to wilt: wILT!. [Pok. 2. welk-, uelg-, 1145.] welt-. Woods; wild. 1. Suffixed form *wolt-u- in Germanic *walthuz in: a. Old English weald, wald, a forest: WEALD, WOLD!; b. Old Norse vdllr, field: VOLE!. 2. Ger- manic *walthdn- in Middle English welde, a plant yield- ing a yellow dye, weld: WELD2. 3. Germanic *wilthigaz in: a. Old English wilde, wild: wip; b. Old English wildéor, wilddéor, wild beast (déor, animal; see dheu-'): WILDERNESS; C. Dutch wild, wild: WILDEBEEST. [In Pok. 4. uel- 1139.] weme-. To vomit. 1. Germanic *wam- in Old Norse vamla, qualm, and Danish vamle, to become sick, prob- ably akin to the Scandinavian source of Middle English wam(ejlen, to feel nausea, stagger: WAMBLE. 2. Latin vomere, to vomit: NUX VOMICA, VOMIT. 3. Greek emein, to vomit: EMESIS, EMETIC. [Pok. wem- 1146.] wen-', To desire, strive for. 1. Suffixed form *wen-w- in Germanic *winn(w)an, to seek to gain, in Old English winnan, to win: WIN}. 2. Suffixed zero-grade form *wn-ydé in Germanic *wunjé in Old English wynn, wen, pleasure, joy: WEN2, WINSOME. 3. Suffixed (stative) zero-grade form *wn-é-, to be contented, in Germanic *wunén in Old English wunian, to become accustomed to, dwell: won!, (wont). 4. Suffixed (causative) o-grade form *won-eyo- in Germanic *wanjan in Old English wenian, to accustom, train, wean: WEAN}. 5. Germanic *wéniz, hope, with denominative *wénjan, to hope, in Old English wénan, to expect, imagine, think: WEEN. 6. Suffixed zero-grade form *wn-sko- in Germanic *wunsk- in Old English wyscan, to desire, wish: WISH. 7. O-grade *won- perhaps in Germanic *wani- in: a. Old Norse Vanir, the Vanir: VANIR; b. Old Norse vana- in Vanadis, name of the goddess Freya: VANADIUM 8. Suf- fixed form *wen-es- in: a. Latin venus, love (> venerari, to worship): VENERATE, VENEREAL, VENERY!, VENUS; b. suffixed form *wen-es-no- in Latin venénum, love potion, poison: VENOM. 9. Suffixed form *wen-eto-, “be- loved,” possibly in Germanic *Weneda-, a Slavic people, in Old High German Winida, the Wends: WEND. 10, Suffixed form “wen-yd@ in Latin venia, favor, forgive- ness: VENIAL. 11. Lengthened-grade form *wén-d- in Latin véndri, to hunt: VENATIC, VENERY2, VENISON. 12. Suffixed basic form *wen-o- in Sanskrit vanam, forest: WANDEROO. 13. Possibly zero-grade suffixed form *wn-ig- in Sanskrit vanik, vdnijah, merchant (? < “seek- ing to gain”): BANIAN. [Pok. 1. ven- 1146.] wen-2. To beat, wound. 1. Suffixed zero-grade form
```


## [2026-09-14T01:01:19.963Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"proti\\|PROSTHESIS\\|per-'\\.\" AHD_watkins1985.txt | head -8\necho \"---\"; grep -n -o \"per-1[^.]\\{0,900\\}\" AHD_watkins1985.txt | head -2",
 "description": "Watkins per-1"
}
```


### [2026-09-14T01:01:21.217Z] TOOL RESULT

```
375:mild, gentle: DAFT. 2. Probably suffixed form *dhabh-ro- in Latin faber, artisan (< “he who fits together”): FABRIC, (FABRICATE), FORGE}. [Pok. 2. dhabh- 233.] dhal-. To bloom. Suffixed form *dhal-yo- in Greek thal- lein, to flourish, bloom, sprout (> thallos, a shoot): THALIA, THALLUS; PROTHALLUS. [Pok. dhail- 234.] dhé-', To set, put. Contracted from *dheo-. 1. O-grade form *dhé- in Germanic *don in Old English dén, to do: Dol; FORDO. 2. Suffixed form *dhé-ti-, “thing laid down or done, law, deed,” in Germanic *dédiz in Old English déd, doing, deed: DEED. 3. Suffixed o-grade form *dho-mo- in Germanic *démaz in: a. Old English dom, judgment (< “thing set or put down”): Doom; b. Old English -d6m, abstract suffix indicating state, condition, or power: -DOM; c. Old Norse -démr, condition (see ka-); d. Gothic déms, judgment, akin to the Germanic source of Russian Duma, Duma: Duma; e. Germanic denomina- tive *“ddmjan in Old English déman, to judge: DEEM. 4. Suffixed o-grade form *dhé-t- in Latin agential suffix -dés in Latin sacerdés, priest, “(performer of sacred rites” (see sak-). 5. Zero-grade form “dha- in: a. prefixed form *kom-dha- in Latin condere, to put together, establish, preserve (*kom, together; see kom): CONDIMENT; AB- SCOND, INCONDITE, RECONDITE, SCONCE?; b. compound *kred-dha- (see kerd-'). 6. Suffixed zero-grade form *dha-k- in: a. Latin facere (< *fak-yo-), to do, make (> French faire, to do), and Latin combining form -fex (< *.fak-s), “maker”: -FACIENT, FACT, FACTION, FACTITIOUS, FACTOR, FASHION, FEASIBLE, FEAT!, FEATURE, (FETISH), -FIC, (-FY); AFFAIR, AFFECT!, (AFFECT2), (AFFECTION), AMPLIFY, ARTIFACT, ARTIFICE, BEATIFIC, BENEFACTION, BENEFIC, (BENEFICE), (BENEFICENCE), BENEFIT, CHAFE, COMFIT, CONFECT, (CONFETTI), COUNTERFEIT, (DEFEA- SANCE), DEFEAT, DEFECT, (DEFICIENT), (DISCOMFIT), EDIFICE, (EDIFY), EFFECT, (EFFICACIOUS), (EFFICIENT), FACSIMILE, FACTOTUM, FORFEIT, HACIENDA, INFECT, JUSTIFY, MALEFACTOR, MALFEASANCE, MANUFACTURE, MISFEASANCE, MODIFY, MOLLIFY, NIDIFY, NOTIFY, NUL- LIFY, OFFICINAL, PERFECT, PETRIFY, (PLUPERFECT), PON- TIFEX, PREFECT, (PROFICIENT), PROFIT, PUTREFY, QUALIFY, RAREFY, RECTIFY, REFECT, (REFECTORY), RU- BEFACIENT, SACRIFICE, SCIRE FACIAS, SPINIFEX, SUF- FICE, (SUFFICIENT), SURFEIT, TUBIFEX, TUMEFACIENT, viviry; b. Latin derivative faciés, shape, face (< “form imposed on something”): FACADE, FACE, (FACET), (FA- CIAL), FACIES; (DEFACE), EFFACE, PRIMA FACIE, (SUR- FACE); c. Latin compound officium (< *opi-fici-om), service, duty, business, performance of work (*opi-, work; see op-'): OFFICE; d. further suffixed form *dha-k-li- in Latin facilis (< Old Latin facul), feasible, easy: FACILE, (FACILITY), FACULTY; DIFFICULTY. 7. Suffixed zero-grade form *dha-s- in Latin fds, divine law, right: NEFARIOUS. 8. Possibly Latin -farius, -doing: MULTIFARIOUS, OMNI- FARIOUS. 9. Reduplicated form *dhi-dhé- in Greek tithe- nai, to put: THESIS, THETIC; ANATHEMA, ANTITHESIS, APOTHECARY, (APOTHECIUM), BODEGA, BOUTIQUE, DI- ATHESIS, EPENTHESIS, EPITHET, HYPOTHESIS, METATHE- SIS, PARENTHESIS, PROSTHESIS, PROTHESIS. 10. Suffixed form *dhé-k- in Greek théké, receptacle: THECA, TICK?; AMPHITHECIUM, BIBLIOTHECA, CLEISTOTHECIUM, ENDO- THECIUM, PERITHECIUM. 11. Suffixed zero-grade form *dha-mn in Greek thema, “thing placed,” proposition: (THEMATIC), THEME. 12. Reduplicated form *dhe-dhé- in Sanskrit dadhdti, he places: SANDHI. 13. Reduced form *dh- (see aw-2). [Pok. 2. dhé- 235.] dhé-2. To vanish. Contracted from *dhea-. 1. Possibly Old Norse d%sa, to languish, decay: DASTARD. 2. Possibly Old Norse *dasa, to tire out (attested only in reflexive form dasask, to become exhausted), akin to the Scandi- navian source of Middle English dasen, to stun: DAZE. [Pok. 3. dhé- 239.] dheb-. Dense, firm, compressed. Germanic suffixed form *dap-ra- in Middle Dutch and Middle Low German
839:parative) form *pro-tero- in Greek proteros, before, former: HYSTERON PROTERON, PROTEROZOIC. VI. Exten- ded forms *prai-, *prei-. 1. Latin prae, before: PRE-; PRETERIT. 2. Suffixed (comparative) form *prei-yos- in Latin prior, former, higher, superior: PRIOR2. 3. Suffixed form *prei-wo- in: a. Latin privus, single, alone (< “standing in front,” “isolated from others”): PRIVATE, PRIVILEGE, PRIVITY, PRIVY; DEPRIVE; b. Latin proprius, one’s own, particular (< pré priv6, in particular, from the ablative of privus, single): PROPER, PROPERTY; APPRO- PRIATE, PROPRIOCEPTION, PROPRIOCEPTOR. 4. Extended form *preis- in: a. suffixed (superlative) form *preis-mo in (i) Latin primus (< *prismus; ablative plural primis), first, foremost: PREMIER, PRIMAL, PRIMARY, PRIMATE, PRIME, PRIMITIVE, PRIMO, PRIMUS; IMPRIMIS, PRIMA FACIE, PRIMAVERA, PRIMEVAL, PRIMIPARA, PRIMOGENI- TOR, PRIMOGENITURE, PRIMORDIAL (ii) Latin compound princeps, “he who takes first place” (-ceps, “-taker”; see kap-), leader, chief, emperor: PRINCE, PRINCIPAL, PRIN- CIPLE; b. suffixed form *preis-tano- in Latin pristinus, former, earlier, original: PRISTINE. VII. Extended form *pres- in compound “*pres-g“u-, “going before” (*gvu-, to go; see gWa-), in Greek presbus, old, old man, elder: PRESBYTER, (PRIEST); PRESBYOPIA. VIII. Extended form *proti in Greek pros, against, toward, near, at: PROS-; PROSOPOPEIA. Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-’. [Pok. 2. A. per 810.] per-?. To lead, pass over. A verbal root belonging to the group of per’. I. Full-grade form *per-. 1. Suffixed form *per-tu-s in Germanic “*ferthuz, place for crossing over, ford, in Old Norse fjérdhr, an inlet, estuary: FIRTH, FJORD. 2. Suffixed form *per-ond in Greek peroné, pin of a brooch, buckle (< “that which pierces through”): PERONEAL. II. O-grade form *por-. 1. Germanic *faran, to go, in: a. Old English faran (> Middle English faren), to go on a journey, get along: FARE; WAYFARER, WAY- FARING, (WELFARE); b. Old High German faran, to go, travel: GABERDINE. 2. Suffixed form *por-o-, passage, journey, in Greek poros, journey, passage: PORE”; EMPO- RIUM, POROMERIC. 3. Suffixed (causative) form *por- eyo-, to cause to go, lead, conduct, in Germanic *farjan, to ferry, in Old English ferian, to transport: FERRY. 4. Lengthened-grade form *pdér- in: a. Germanic suffixed form *f6r-ja- in Old English (ge)féra, “fellow-traveler,” companion (ge-, together, with; see kom): FERE; b. Ger- manic suffixed (causative) form *fér-jan in Old High German fuoren, to lead: FUHRER. 5. Possibly suffixed form *por-no-, feather, wing (< “that which carries a bird in flight”), in: a. Germanic *farnd, feather, leaf, in Old English fearn, fern (having feathery fronds): FERN; b. Sanskrit parnam, leaf, feather: PAN2. III. Zero-grade form pr-. 1. Suffixed form *pr-tu-, passage, in: a. Ger- manic *furdu- in Old English ford, shallow place where one may cross a river: FORD; b. Latin portus, harbor (< “passage”): PORT!; IMPORTUNE, OPPORTUNE. 2. Suffixed form *pr-té in Latin porta, gate (> Old French porte, door): PORCH, PORT’, PORTAL, PORTCULLIS, PORTE-CO- CHERE, PORTER®, PORTICO, PORTIERE, PORTULACA. 3. Suffixed (denominative) form *pr-to- in Latin portdre, to carry: PORTS, PORTABLE, PORTAGE, PORTAMENTO, PORTATIVE, PORTER}; COMPORT, DEPORT, EXPORT, IM- PORT, (IMPORTANT), PORTFOLIO, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT. [Pok. 2. B. per 816.]
981:ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
---
2278:per-1 SPARGE (s)preg- SPARLING spei- SPARROW sper-? SPARSE (S)preg- SPATHE spé-2 SPATHIC spé-2 SPATULA spé-2 SPAY spé-2 SPEAK spreg- SPEAR sper-! SPECIES spek- SPECIMEN spek-
```


## [2026-09-14T01:01:31.017Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"pṛtanā\\|prtana\\|pftana\\|pytana\\|pṛt-\" WLD_Bd2_pages.txt | head -8\necho \"=== schlagen per\"; grep -n -o -E \".{0,80}per-, perg-.{200}\" WLD_Bd2_pages.txt | head -4\necho \"=== proti\"; grep -n \"proti\" WLD_Bd2_pages.txt | head -6",
 "description": "Walde-Pokorny Bd II"
}
```


### [2026-09-14T01:01:34.530Z] TOOL RESULT

```
=== schlagen per
ugrep: error: error at position 86
80-\xbf][\x80-\xbf]*){200}
                          \___exceeds complexity limits


=== proti
2225:bildet?), palign. pri-trom-e „inprius, protinus^, pri-stafalacirix „*praestibu-
2575:     H. pretij proti „gegeniiber, entgegen, gegen“, z. T. im Sinne des Entgelts:
2590:BrugmannIP2, 877 f.; Hermann IF. 34, 357 (Kreuzung von *proti und "^pos);
2600:     Abg.        protivhy   protivq „entgegen“,kaschub. procim; wruss. preci, poln.
42105:7xovn^\proti „Anschwellung“, ags. drutian „Yor Hochmut oder Zorn schwellen'^;
44535:spritzen^^; aisl. sproti m, ,,junger SchoBling an einem Baum, Stecken“,
```


## [2026-09-14T01:01:38.461Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '2575,2605p' WLD_Bd2_pages.txt\necho \"#### per schlagen\"; grep -n \"schlagen\" WLD_Bd2_pages.txt | sed -n '1,40p' | grep -n \"per\" | head\ngrep -n \"pdrdtamna\\|paretamna\\|pesana\\|p9r9t\" WLD_Bd2_pages.txt | head",
 "description": "WLD preti/proti + per schlagen"
}
```


### [2026-09-14T01:01:38.542Z] TOOL RESULT

```
     H. pretij proti „gegeniiber, entgegen, gegen“, z. T. im Sinne des Entgelts:
ai. prdii        (im Iran, durch pati verdrangt) Praef. „gegen, zuriick usw.“ Praep.
m. Acc. „gegen usw."^ (mit Gen. prdtivdstoJi „gegen Morgen hin*0 gr- horn. ttootI          ;


(kret. TzoQTt umgestellt wieLI^^o^d/ra) jon. att. lesb. Tzgog, pamphyl.      (umge-
stellt aus *7iQarl s. Kretschmer KZ. 33, 266), aol.      Adv. „noch dazu, iiberdies^,
Praef., Praep. m. Acc. „gegen            —
                                     hin, zu, gegen“, mit Loc. („Dativ“)„an“, m.
Gen. „nach einem Bereich bin; bei (in Schwuren)'S mit Abl. („Gen,“) „von“
her, von die Entstehung der Form jigog ist strittig, vgl. Kretschmer Gl. 1, 53 ff.;
             ;


3, 322ff. (gegen Jacobsohn KZ. 42, 282); 6, 293 (zu Ehrlich Unt. 29fF.);
BrugmannIP2, 877 f.; Hermann IF. 34, 357 (Kreuzung von *proti und "^pos);
nicht zur Entscheidung verwendbar ist stgoo^eiv), da auch in Mdarten
iiblich, die nur norl und nog kennen (vielleicht unmittelbar zu ngo nach
omo^evj wenn dies nicht umgekehrt sein a von ngoo^ev empfangen hat,
8. ^epi,   oier 7tq6o&sv iTZQooooo — omod-ev djiioooj ; ngdooco aus ^ngorico mit dem
                                                       :



Formans -t-io- wie ai. apa-t-ya-, got. ni-p-jis, s. Brugmann ll^ 2, 729 m. Lit.).
     Abg.        protivhy   protivq „entgegen“,kaschub. procim; wruss. preci, poln.
przeckc „entgegen“              (auch im Sinn des Tauschverhaltnisses).  Lett, pret
{pret€; pretty prete usw., s. Bielenstein Lett. Spr. 2, 319, Zubaty lA. 22, 60)
Praep. m. Acc. und Gen. „gegen'^ (auch in Vergleichungen), pretiba „Gegen-
stiick. Pendant^, pretmeks „Gegner, Widersacher, gleichen Schlages oder
AYertes“.   Hierher auch lat. pretium „Wert, Preis einer Sache“ (Keutr.
#### per schlagen
14:2847:8.     per-, per-g-,   per-q- „schlagen'',          auch   vom     Donnerschlag.       S. bes.
15:2864:  Lit. periu, periau, perti „mit dem Badequast schlagen, jmdn baden auch               :
16:2869:iiberhaupt schlagen“, lett. peru. pe'rt „mit dem Blatterquast (belaubtem
18:2871:   Abg. pereij pbvati „schlagen, bes. mit dem Bleuel schlagen, waschen“,
19:2882:diese Gruppe oder die ganze Wz. per- ..schlagen^* nur als einen Ableger
24:3262:aisl.    Fiqrggn,   lit.   Perkitnas s. u. per-, perg-, perq- „schlagen“.    — Dt. Forst
```


## [2026-09-14T01:01:41.827Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '2847,2866p' WLD_Bd2_pages.txt",
 "description": "WLD per- schlagen"
}
```


### [2026-09-14T01:01:41.894Z] TOOL RESULT

```
8.     per-, per-g-,   per-q- „schlagen'',          auch   vom     Donnerschlag.       S. bes.
       Liden Arm. St. 85 ff. m.     Lit.

     Arisch nur mit mhaft gewordenem ^-Formans: ai. prt-, pHana „Kampf,
Streit“, ay. pdVdU,  pdsanci „Kampf, Schlacht”, pdrdiamna „die miteinander
Kampfenden*', paiti-parotata „bekampft“ (Bugge KZ. 32, 36; nicht besser
ware   ein mit ^pre-ti^ ^pro-tl ablautendes         zugrunde zu legen: noch
anders Persson Beitr. 473 al).
   Ann. }iar% e-har „schlug“ (Aor. zum Praes. harkanem, s. u,), Jiarac „vulnus‘'
(usw., s. Liden); orot .,DonneP', orotam ,,donnere“; alb. (G. Meyer Wb. 352)
pres „haue ab, nieder schneide^', Aor. preva. me pret „es kummert mich,
                          ;


ist mir angelegen“, pritem „werde geschnitten; zerkratze mich; kiimmere

mich um etwas“.
  Lit. periu, periau, perti „mit dem Badequast schlagen, jmdn baden auch               :
```


## [2026-09-14T01:01:52.196Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nd=open('ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor w in ['پیکار','پیمودن','پاسخ','نبرد','پیش']:\n    ls=[i for i,t in enumerate(d) if w in t]\n    print(w, ls[:8])\nEOF",
 "description": "Aryanpur leaves"
}
```


### [2026-09-14T01:01:53.387Z] TOOL RESULT

```
leaves 545
پیکار []
پیمودن []
پاسخ [9, 351]
نبرد [32, 56, 394, 514]
پیش [1, 5, 6, 7, 9, 10, 11, 12]
```


## [2026-09-14T01:01:56.251Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nd=open('ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [351,394]:\n    print('==== leaf',i); print(d[i][:1500])\nEOF",
 "description": "Aryanpur pāsox / nabard pages"
}
```


### [2026-09-14T01:01:57.364Z] TOOL RESULT

```
==== leaf 351
[pdf page 352]
تمه
ا . ست
ایسلندی کهن (۵ 901۸۷۷ صا0): لینوانی (4] هنال 7/):
. لد نم تآهلد5 ,ت52 ,5۸۳1
ساکسونی کهن (540/0 010): 88001۸01 ایرلندی کهن (8/30/ ص01): 13
فریزی کهن (/۶7/540 صا0): ه502 گالی (4ل3/الام0): دا
آلمانی کهن ((087۸44 05 (ا0): ولزی (4اکا): 8 58 ,88
ردان آلبانی (الفاامفقتم: 70
آلمانی (44/۷ل052): 5
انگلیسی کهن (4ل5لق2:0 ص۰0 8800۸1 پسگشت‌ها اسرد
انگلیسی (5ل870): هی 397 ین
دانمارکی (0۸0/184): 508 1 (8۸) ی مین اس
سوئدی (31720/50): ۵6۸ 9 (0188) ما۸5
ملدی (ثن۵07: 2860680 ,8860801 4 (8۳8503) ات دی هم
اسلاری کهن (۲10با5 )نان 0ا0): ناش تلا
1 هن 2 (8۸9) :0/05
لهستانی (۳03): ه6ا050 6 (8۸9) 37
روسی (551۸1): هد برهان قاطع : 11:۶
یادداشت: :
۱ واژه‌ی فارسی "پاسخ" از واجربشه‌های "پاد" و "سخن" تشکیل شده است» (پهلری آن: ۳۸880 ,(۳80
کردی: 315881۷ ارمنی:۳۸7۸87۸۷1).
۲- چم این واژه در لانین: به ترتیب گفتن.
۳- 03110188 معتقد است که واژه‌های این فهرست با واژه‌های ایرانی - هندی این فهرست رابطه‌ای ندارد. سایر
۱ پسگشت‌ها هم واژه‌های ایرانی - هندی این فهرست را مورد بررسی قرار نداده‌اند» لذا جلو واجریشه‌ی هند و اروپایی
(شاید) آورده‌ام.
دا ۹ 8
اوستایی (۸887/04): -لف 5۸ بلورچی (/للاءل8۸): 3
پهلری (1/شاللم): 3 افغانی (پشتو) (/470[2): 3
اوستی (0598712): 3 سانسکر یت (7ل54(/۶8۶): 21313۸8 ,518۸۹
کردی (00820/37): 82806 ب587 بال8۸ ارمنی (0/8011۸7): 3

==== leaf 394
[pdf page 395]
۶ | کار (به چم *ارتش * و "جنگ" کارزار
بادداشت:
۱ بازگشت به‌زگوهگوی ی
۲- چم این واژه در زبان‌های غیراز فارسی: اتانکد» خوکك دونی» غار» کلبه» تفای ی و
چم اين واژه در زبان‌های انگلیسی نوین: خلیج کوچکه ی
۳ واژه‌های " کوژ" و "قوز" نیز از همین ریشه‌اند.
اوستایی (415574/۷): 1۵7۸۷۸11 بفالق سوئدی (ل550[15): 16
پارسی باستان (۳8781۸ 010): هم نروژی (077801۸0/): 6
پهلری (1ها(م«): 3 هلندی (7لع007): از ۱۹۸
کردی (۸(8(137)+ ۸ لبترانی (4142لهلالل7).
افغانی (پشتو) (/4۳0/۸۷): 3اه ,5۸3۸8 ,کفش
سانسکریت (7ل8۸(/587): ۸ نونی (لتی) (ق7۲ها): اند ۱
یونانی 07/6870): 05 پروسی کهن ۳8-۹۹۸0 010): 1۸3018
گرتیک (0077/0): 11۸87۸ ,73۸815 ایرلندی کهن (4لولع[ صرا0): 3
ایسلندی کهن (7+۸۷۵(۷طنته صام).
قددان پسگشت‌ها 1/5
ساکسوی کهن ((54:0 طا0): دنا 6 ۶00800
فریزی کهن (الفاول۶۶ ضام). دا دنا #4 هام0
آلمانی کهن (/687/40 بزه ]با صزم): و ۱ شا
41 ,فا 311 0۴۵ ۸0
آلمانی (0284490): ان برهان قاطع + ۱۵۸
انگلیسی کهن 8۱/0/0 0۱2: 11888 فرهنگ معین : ۳۸۹
دانمارکی (0۸(/18[7): 6
یادداشت: ۹
۱- امروزه پیشتر دانشمندان معتقدند که واژه‌های انگلیسی 4 ور فرانسه‌ی 811123838 از این واجريیشه مشتق
نشده‌اند بلکه از واجریشه‌ی هند و اروپایی ۷۷338* هستند.
۲- در فارسی واژه‌ی " کارزار" بعنی "محل نبرد؟: "کار" * نبرد و پا جنگ و آزار"< محل (مانند "گلزار").
۳ البته ان واژه در فارسی امروز به چم "عمل" و "پیشه" و "کردار" بکار می‌رود.
چ
```


## [2026-09-14T01:02:04.079Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py",
 "description": "Inspect verify_check.py"
}
```


### [2026-09-14T01:02:04.134Z] TOOL RESULT

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


## [2026-09-14T01:02:29.630Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:12:13.244Z] TOOL CALL #79: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-396.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n \"entry\": 0,\n \"root\": \"Per 3\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"two distinct PIE etyma: (a) *próti / *preti 'against, opposite, towards' (Pokorny 815-816, under 1. per- section A.h; Iranian replaced it by the r-less variant *poti > *pati), and (b) *per- / *perg- 'to strike, fight' (Pokorny 818, 3. per-)\",\n \"note\": \"The two halves of Nourai's gloss belong to two roots that Pokorny, Walde-Pokorny and Watkins all keep apart. 'Opposite, against, in front of' = Pokorny 815f. 'h. preti, proti ‚gegenüber, entgegen, gegen‘', where Pokorny notes expressly 'Ai. práti (im Iran. durch paiti verdrängt)'; 'strike' = Pokorny 818 '3. per-, perg- ‚schlagen‘', whose only Indo-Iranian reflexes are the t-stems Skt. pṛt-/pṛtanā and Av. pərət-/pəšanā 'Kampf' (that is node #12). Nourai's page-range POK:815-818 is therefore exact for both, but the box merges them into one root. His own remark 'Related to the Indo-European root Per 1' is what Watkins says: *proti is listed as extension VIII of per-1 and per-5 'to strike' is said to be 'possibly related'. The Iranian preverb paiti- itself is not straightforwardly *preti: Iranian *pati (like Doric Greek poti) points to *poti, usually explained as an r-less doublet of *próti. Verdict: plausible - the material is real and correctly grouped by ancient usage, but as a reconstructed 'root' the box conflates *próti with *per- 'strike'.\",\n \"note_fa\": \"ریشهٔ یگانه‌ای به نام Per 3 با معنای ازدوج «روبه‌رو، دربرابر» و «زدن» در پژوهش امروزی وجود ندارد؛ پوکورنی دو مدخل جداگانه دارد: در صفحهٔ ۸۱۵–۸۱۶ صورت قیدی/حرف‌اضافه‌ای *preti / *proti «دربرابر، پیش» و در صفحهٔ ۸۱۸ ریشهٔ فعلی *per- / *perg- «زدن، جنگیدن». نکتهٔ مهم آنکه خود پوکورنی می‌نویسد سنسکریت prati در ایرانی جای خود را به paiti داده است؛ صورت ایرانی *pati (همانند poti در یونانی دوری) را امروزه گونهٔ بی‌«r» ی از *próti می‌دانند. پس ارجاع نورایی به POK:815-818 درست است اما دو ریشهٔ جدا را در یک جعبه یکی کرده است؛ ادعای او با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/pr%C3%B3ti\"],\n \"ref_check\": [\n   {\"ref\": \"POK:815-818\", \"status\": \"partial\",\n    \"note\": \"Checked POK_03.txt leaves 49 and 51-52 (pp. 815-818). p.815f: 'h. preti, proti ‚gegenüber, entgegen, gegen‘, z.T. im Sinne des Entgelts; preti-os ‚gleichwertig an‘. Ai. práti (im Iran. durch paiti verdrängt) ... gr. hom. προτί ... lat. pretium'. p.818: '3. per-, perg- ‚schlagen‘. Arisch nur mit t-Formans: ai. pṛt-, pṛtanā ‚Kampf, Streit‘, av. pərət-, pəšanā ‚Kampf, Schlacht‘, pərətamna ‚die miteinander Kämpfenden‘, vaiti-parətata ‚bekämpft‘'. Both claims of the box stand on those pages, but they are two different Pokorny lemmas, not one root.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II, '8. per-, per-g-, per-q- ‚schlagen‘' and 'H. preti, proti'\", \"stance\": \"partial\",\n    \"note\": \"WLD_Bd2_pages.txt l.2847: 'Arisch nur mit t-haft gewordenem t-Formans: ai. pṛt-, pṛtanā ‚Kampf, Streit‘, av. pərət-, pəšanā ‚Kampf, Schlacht‘ ... paiti-parətata ‚bekämpft‘' and expressly rejects basing these on an ablauting *pre-ti/*pro-ti; l.2575: 'H. preti, proti ‚gegenüber, entgegen, gegen‘ ... ai. práti (im Iran. durch pati verdrängt)'. So Walde-Pokorny too keeps 'against' and 'strike' apart.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. per-1 (VIII) and per-5\", \"stance\": \"partial\",\n    \"note\": \"'per-1 ... VIII. Extended form *proti in Greek pros, against, toward, near, at ... Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-6. [Pok. 2. A. per 810.]' and separately 'per-5. To strike ... [Pok. 3. per- 818.]'. Watkins therefore allows the two to be 'possibly related' - Nourai's 'Related to Per 1' - but still numbers them apart.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/próti\", \"stance\": \"supports\",\n    \"note\": \"'Possibly from *pró + *-ti' and, on the reconstruction notes, 'Proto-Iranian *pati and Proto-Hellenic *poti seem to come from *poti, but they are probably r-less forms of *próti, originating when combined with words containing r.'\"}\n ],\n \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\ndef node(i, lang, words, verdict, der, der_fa, sources, refs, cons):\n    N.append({\"id\": i, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n              \"derivation\": der, \"derivation_fa\": der_fa,\n              \"sources\": sources, \"ref_check\": refs, \"consulted\": cons})\n\n# ---------------- node 1 ----------------\nnode(1, \"Avestan / Old Persian\", \"paiti 2, paitî 3, pati, patiy\", \"confirmed\",\n \"Av. paiti (also the adverbial/compositional paiti-) and OP patiy are the regular Old Iranian continuants of the Indo-Iranian preverb-preposition that Sanskrit shows as prati. Kent's lexicon has patiy both as enclitic postposition and as preposition/preverb, and the -š extension patiš 'against' (DB 1.93; 2.33 etc., 'paraitā patiš Dādaršim' = 'they marched against Dādaršiš'); Bartholomae has Av. paiti throughout with exactly the senses 'gegen, entgegen, zu, auf' plus dozens of paiti-compounds. The only correction to the chart is formal, not factual: the Iranian form is *pati, not *prati, i.e. it continues the r-less *poti variant of PIE *próti, and Pokorny/Walde-Pokorny state that Iranian pati 'displaced' prati. Nourai's numbering 'paiti 2 / paitî 3' is his own homonym-numbering, not a source form.\",\n \"صورت‌های paiti اوستایی و patiy پارسی باستان به معنای «دربرابر، به‌سوی، پیش» هر دو مسلم‌اند: کنت در واژه‌نامهٔ پارسی باستان هم patiy را و هم صورت گستردهٔ patiš «برضد» را از سنگ‌نوشتهٔ بیستون می‌آورد و بارتولومه ده‌ها ترکیب با paiti ثبت کرده است. تنها اصلاح لازم صوری است: صورت ایرانی *pati است نه *prati، یعنی دنبالهٔ گونهٔ بی‌«r»ی هندواروپایی *próti (مقایسه با poti یونانی دوری). شماره‌های «۲» و «۳» از آنِ خود نورایی و برای تمایز هم‌نگاشت‌هاست. ادعای نورایی درست است.\",\n [W + \"Reconstruction:Proto-Indo-European/pr%C3%B3ti\"],\n [{\"ref\": \"POK:815\", \"status\": \"supports\",\n   \"note\": \"POK_03.txt leaf 49 (p.815f): 'h. preti, proti ‚gegenüber, entgegen, gegen‘ ... Ai. práti (im Iran. durch paiti verdrängt) Präf. ‚gegen, zurück usw.‘'. The page names the Iranian paiti explicitly, so it does support the arrow root->paiti, while showing the Iranian form is *pati not *prati.\"}],\n [{\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.195 s.v. patiš / patiy\", \"stance\": \"supports\",\n   \"note\": \"KNT.txt: 'patiš prep. with acc. ‚against‘: pati- + adv. -s, cf. Lt. ex, abs ... DB 1.93; 2.33, 38, 43f...' and, in the grammar, 'Postpositions: ā, patiy; both also as separate words before or after their nouns'.\"},\n  {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW, s.v. paiti and the paiti-compounds\", \"stance\": \"supports\",\n   \"note\": \"BRT.txt has 1061 hits for 'paiti'; e.g. 'mit paiti ‚sich feindlich wenden, auftreten gegen —‘ (Akk.)', 'mit paiti 1) ‚entgegengehen, sich wenden gegen —‘', 'paiti.raēθwa- n. ‚indirekte Ansteckung‘' - the preposition and the preverb in exactly the chart's sense.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn no. 345, p.76\", \"stance\": \"supports\",\n   \"note\": \"'345. (1)pei-, Praefix. ap. pati[y] ‚zu, gegen etc.‘; aw. paiti; phlv. pat-, pāt- etc.; ai. práti. Im Neupersischen erscheint das Praefix pati- als pāt-, pa-, pid-, peδ-, pei- (pe-).'\"}])\n\n# ---------------- node 2 ----------------\nnode(2, \"Pahlavi\", \"paitiš, pat, pěš\", \"plausible\",\n \"The Pahlavi material is right, the etymology of one member is contested. MP pad (Book Pahlavi PWN / p'n) 'at, in, to, by' and the compositional pat-/pāt- are the regular continuants of OIr. *pati (Horn 345; MacKenzie s.v. pad). MP pēš [LOYN' < Aram. l-'yn; pyš] 'before, in front' is well attested (MacKenzie p.68), and Horn no. 356 derives it from OP patiš / Av. paitiš - but Horn's own footnote already records Bartholomae's warning that Av. paitiš 'ganz unsicher sei' (Yt 12.3 and 5.62 are to be read paitiša, leaving only Yt 3.4), and Hübschmann, Pers. Studien no. 356, rejects the derivation outright: 'Np. pēš ‚vor‘ = pāz. phl. pēš ... ist jedenfalls nicht = ap. patiš'. Modern opinion (Edelman, via Wiktionary) keeps *pati- but as the first member of *pati-aši- 'before one's eyes' (= Skt pratyakṣa); Gershevitch derives it instead from *pasya- 'observing'. The third gloss of this node, 'leader', belongs not here but to the homonym OIr. *pati- 'lord' - see node #3.\",\n \"مادهٔ پهلوی درست است ولی ریشهٔ یکی از سه صورت محل اختلاف است. pad و پیشوند pat-/pāt- در فارسی میانه بازماندهٔ مستقیم *pati ایرانی باستان‌اند (هرن، شمارهٔ ۳۴۵؛ مکنزی). صورت pēš پهلوی هم مسلم است، اما اینکه از patiš پارسی باستان آمده باشد مورد انکار هوبشمان (پژوهش‌های فارسی، شمارهٔ ۳۵۶) است؛ بارتولومه نیز پدیدهٔ اوستایی paitiš را سخت مشکوک می‌داند. دیدگاه امروزی (ادلمان) پیش را از *pati-aši- «دربرابر چشم» می‌گیرد که باز هم پایهٔ pati- دارد. معنای سوم «سرور» متعلق به هم‌نگاشت دیگری است (نگاه کنید به گره ۳). ادعای نورایی با احتیاط پذیرفتنی است.\",\n [W + \"%D9%BE%DB%8C%D8%B4#Persian\"],\n [{\"ref\": \"BQT:440\", \"status\": \"supports\",\n   \"note\": \"BQT_v1_pages.txt leaf ~666-667 (printed p.440-442; offset checked against the 'baqiye dar safhe-ye 440' catch-line on leaf 665) carries the پیش / پیشانی / پیشوا / پیشآهنگ cluster, i.e. exactly the page Nourai cites for pēš. Mo'in's footnotes in this stretch cite Horn's numbers («اشتق ۳۵۶ ...»).\"}],\n [{\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.68 s.v. pēš; p.65 s.v. pad\", \"stance\": \"supports\",\n   \"note\": \"'pēš [LOYN! < A l-‘yn; pyš | = M, N ~] before'; also 'pēšānig [pyš\\\"nyk! | N pēšānī] forehead', 'pēšōbāy ... leader, vanguard'.\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, no. 356\", \"stance\": \"contradicts\",\n   \"note\": \"'356. Np. pēš ‚vor‘ = paz. phl. pēš ... = arm. pēš- (in Lehnwörtern) ist jedenfalls nicht = ap. patiš. Dass auch kein Grund vorhanden ist, np. piš- auf ap. patiš zurückzuführen, ist oben Nr. 312-314 gezeigt.'\"},\n  {\"src\": \"HRN\", \"where\": \"Horn no. 356, p.80 with footnote\", \"stance\": \"partial\",\n   \"note\": \"'356. pēš ‚zuerst, zuvor‘, pēšīn, pēšānī ‚Stirn‘. ap. patiš ‚gegen‘; aw. paitiš; phlv. pat(i)š-, pēš' - but the footnote: 'Bartholomae macht mich darauf aufmerksam, dass aw. paitiš ganz unsicher sei ... es bleibe also nur yt. 3,4.'\"}])\n\n# ---------------- node 3 ----------------\nnode(3, \"Persian\", \"pîš; bod, bad 2\", \"disputed\",\n \"پیش pīš 'front, ahead' (and its family پیشانی, پیشوا, پیشرفت, پیشخدمت) is the regular NP continuation of MP pēš, with MP ē > NP ī in the modern standard; its ultimate source is contested but every current proposal except Gershevitch's contains *pati- (see node #2), so for پیش the chart is at worst imprecise. The second word is a different matter. The suffix -بد (-bad/-bod) of سپهبد, موبد, هیربد goes back to MP -bed [-pt'], from OIr. *pati- 'lord, master' = Av. paiti- m. 'Herr', Skt páti-, from PIE *pótis (cf. Gk πόσις/δεσπότης, Lat. potis, Goth. -faþos) - a homonym of, not the same word as, the preposition paiti < *próti. Horn himself separates them (no. 188 '-bed, -bud ‚Herr‘ ... aw. paiti-, -paiti ‚Herr‘; ai. pāti-, -pati-' vs. no. 345 the prefix pei- < ap. patiy), and Wiktionary derives سپهبد from OP *spādapatiš 'commander of the army', PIr. *cwaHdapatiš, by surface analysis سپاه + ـبد 'lord, master'. Because the chart hangs -بد on the 'opposite, in front of' root, this node is disputed; the worst verdict of its two words governs.\",\n \"واژهٔ «پیش» بازماندهٔ pēš فارسی میانه است («ای کشیدهٔ فارسی میانه در فارسی نو به ی بدل شده») و ریشهٔ بازپسین آن هرچند محل بحث است، در بیشتر تحلیل‌ها عنصر *pati- دارد. اما پسوند «ـبد» در سپهبد، موبد، هیربد از این ریشه نیست: آن از -bed فارسی میانه و از *pati- ایرانی باستان به معنای «سرور، خداوند» (اوستایی paiti- «Herr»، سنسکریت páti-، هندواروپایی *pótis) می‌آید که فقط هم‌نگاشتِ حرف‌اضافهٔ paiti است. خودِ هرن این دو را در دو مدخل جدا (۱۸۸ و ۳۴۵) آورده است. پس پژوهش امروزی پیوند «بد» را با ریشهٔ «دربرابر» رد می‌کند.\",\n [W + \"%D8%B3%D9%BE%D9%87%D8%A8%D8%AF#Persian\", W + \"%D9%BE%DB%8C%D8%B4#Persian\",\n  W + \"Reconstruction:Proto-Indo-European/p%C3%B3tis\"],\n [{\"ref\": \"BQT:242,440,2405\", \"status\": \"partial\",\n   \"note\": \"p.440 (BQT_v1_pages.txt leaves 666-667) is the پیش page - supports. p.2405 = BQT vol.4 pdf page 488 (printed = pdf+1917), the هیربد entry, whose Mo'in footnote reads 'در اوستا aēθrapaiti- و در پهلوی hērbad ... «اشتق ۱۱۱۵» ... بارتولمه ۲۱۰-۲۰؛ پهلوی aēhrpat (در کتیبه‌ها)' - i.e. Mo'in derives the -bad of هیربد from Av. aēθra-paiti- 'master of learning', the 'lord' word, not from the preposition. So the reference supports the FORM but not the arrow drawn from 'opposite, in front of'. p.242 could not be pinned down: BQT_v1_pages.txt leaves 463-466 cover بدخشان ... برادر (printed ~239-242) and no بد suffix entry with an etymological footnote was legible in the OCR.\"}],\n [{\"src\": \"HRN\", \"where\": \"Horn no. 188, p.44\", \"stance\": \"contradicts\",\n   \"note\": \"'188. (2)-bed, -bud ‚Herr‘ (Comp.), z. B. sipehbed, mōbed, hērbud. aw. paiti-, -paiti ‚Herr‘; phlv. pat, -pat, arm. LW. pet, -pet; ai. pāti-, -pati-.' Horn puts the suffix under the 'lord' word, separate from his no. 345 prefix pei- < ap. patiy.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.18 s.v. -bed; p.77 s.v. spāh-bed\", \"stance\": \"contradicts\",\n   \"note\": \"'-bed [-pt' | M -byd, N -bad/bud] suffix, -lord, -master'; 'spāh ... ~bed [-pt! | N -bud] general, commander'. Glossed 'lord, master', never 'in front of'.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"سپهبد\", \"stance\": \"contradicts\",\n   \"note\": \"'From Middle Persian spāhbed, from Old Persian *spādapatiš, from Proto-Iranian *cwaHdapatiš (“commander of the army”). By surface analysis, سپاه + ـبد (-bod, “lord, master”).'\"}])\n\n# ---------------- node 4 ----------------\nnode(4, \"Pahlavi\", \"pad, pa\", \"confirmed\",\n \"MP pad (written with the Aramaeogram PWN, phonetically p'n/pd) 'at, in, on, to, by' is the direct continuant of OP patiy / Av. paiti used adverbally and prepositionally; the final -ti of *pati gives MP -d after the vowel, and in proclisis the word is further reduced to pa- before consonant clusters. The NOTE reports Horn p.33 correctly: Horn no. 144 lists 'be, beδ (vor Vokalen), Praeposition ‚zu, bei, mit, an, auf‘. ap. patiy bezw. upā; aw. paiti bezw. upa; phlv. pat[aš], pat- bezw. pāz. pa; ai. práti bezw. úpa ... In der Form be sind die beiden Praepositionen upa und (irregulär) pati zusammengefallen, ein Vorgang, der scharf beachtet werden muss.' So Horn's claim is about the NP outcome be, not about Pahlavi pad, which he derives from patiy alone.\",\n \"حرف‌اضافهٔ pad در فارسی میانه (به خط پهلوی با هزوارش PWN) به معنای «به، در، بر، با» دنبالهٔ مستقیم patiy پارسی باستان است؛ تِ پایانی در میان دو واکه به d نرم شده و در جایگاه بی‌تأکید به pa کوتاه شده است. یادداشت نورایی دربارهٔ هرن دقیق است: هرن در بند ۱۴۴ می‌گوید در صورت «به» دو حرف‌اضافهٔ upa و (به‌صورت بی‌قاعده) pati در هم ادغام شده‌اند. ادعای نورایی درست است.\",\n [W + \"%D8%A8%D9%87#Persian\"],\n [{\"ref\": \"HRN:33\", \"status\": \"supports\",\n   \"note\": \"HRN.txt leaf 54 (printed p.33): '144. be, beδ (vor Vokalen), Praeposition, ‚zu, bei, mit, an, auf‘. ap. patiy bezw. upā; aw. paiti bezw. upa; phlv. pat[aš], pat- bezw. pāz. pa (JIS); ai. práti bezw. úpa ... In der Form be sind die beiden Praepositionen upa und (irregulär) pati zusammengefallen.' Exactly the NOTE in the chart.\"},\n  {\"ref\": \"AEF:190\", \"status\": \"not_checked\",\n   \"note\": \"Khaleqi Motlaq's Asas-e Eshteqaq-e Farsi is not online (refs_online.json: 'Not online (searched archive.org, ketabnak, noorlib, web)'). Since it is the Persian translation of Horn+Hübschmann, Horn no. 144 (checked above) is the same text.\"}],\n [{\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.64 s.v. pad\", \"stance\": \"supports\",\n   \"note\": \"MacKenzie lists pad (PWN) 'at, in, on, to, for, by' as the ordinary MP preposition, and its compounds pad-pānag, pa(č)čībāy- etc. appear in PHD.txt's index block.\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, no. 345\", \"stance\": \"supports\",\n   \"note\": \"'345. Ap. patiy als 1. Glied von Comp. ist neup. zu paδ (vor Vocalen), pa (vor c, s, š), pai (vor den übrigen Consonanten) geworden, ap. *patiy zu pad-, pa-. Über das selbständige patiy vgl. Nr. 144.'\"}])\n\n# ---------------- node 5 ----------------\nnode(5, \"Persian\", \"be[h]\", \"confirmed\",\n \"NP به be/ba 'to, at, in, by' continues MP pad directly: initial p- is voiced to b-, and the final -d is lost in the proclitic form (be-, ba-), while the older beδ survives before vowels in early NP and in Judaeo-Persian. Wiktionary states the chain without hesitation: 'From Middle Persian PWN (pad, “to, at, in, on”), from Old Persian patiy, from Proto-Iranian *pati-'. The NOTE that the b-/p- prefixes have lost their original meaning is right and is exactly why Horn (no. 144) warns that in NP be the reflexes of upa and pati have fallen together, so that a given be- cannot always be assigned to one or the other; the doublet په (pa) of the chart's script field is the unvoiced variant preserved in compounds.\",\n \"حرف‌اضافهٔ «به» در فارسی نو مستقیماً از pad فارسی میانه است: پِ آغازین به ب واک‌دار شده و دِ پایانی در جایگاه پیوسته افتاده است؛ صورت کهن‌تر «بهـد» پیش از واکه در فارسی دری و متون یهودی‌فارسی باقی مانده است. یادداشت کتاب دربارهٔ ازدست‌رفتن معنای اصلی پیشوند درست است، زیرا بنا بر هرن در «به» بازماندهٔ upa و pati یکی شده‌اند. ادعای نورایی درست است.\",\n [W + \"%D8%A8%D9%87#Persian\"],\n [{\"ref\": \"AEF:190,191\", \"status\": \"not_checked\",\n   \"note\": \"AEF (Khaleqi Motlaq's Persian version of Horn/Hübschmann) has no online copy; the corresponding German original, Horn no. 144 (p.33) and Hübschmann no. 345, were read instead and say what the node claims.\"}],\n [{\"src\": \"Wiktionary\", \"where\": \"به, Persian, Etymology 1\", \"stance\": \"supports\",\n   \"note\": \"'From Middle Persian 𐣯𐣥𐣭 (pʿn) / PWN (pad, “to, at, in, on”), from Old Persian 𐎱𐎫𐎡𐎹 (patiy), from Proto-Iranian *pati-.'\"},\n  {\"src\": \"HRN\", \"where\": \"Horn no. 144, p.33\", \"stance\": \"supports\",\n   \"note\": \"Same entry as for node #4; Horn's headword IS the NP word ('be, beδ ... Praeposition') derived from ap. patiy / upa.\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, no. 345\", \"stance\": \"supports\",\n   \"note\": \"'Ap. patiy als 1. Glied von Comp. ist neup. zu paδ ..., pa ..., pai ... geworden' - Hübschmann accepts the pati > paδ/pa/pai development even though he rejects Horn's pēš etymology.\"}])\n\n# ---------------- node 6 ----------------\nnode(6, \"Avestan\", \"paiti-kan; paiti-gar; paiti-gama; paiti-kâra\", \"plausible\",\n \"All four are preverb-plus-root compounds of paiti- with an Avestan verbal root, and all four are the standard etymologies of the NP words in node #7 - but three of them are reconstructions (Horn stars them) and one carries Horn's own question mark. (a) paiti + √kan- 'to dig' > *paiti-kāna- 'that which digs in': Horn no. 362 'peikān ‚Pfeilspitze, Pfeil‘. aw. paiti + √kan- (?)' - the question mark is his. (b) paiti + 2√gar- 'to raise the voice, call out' > 'reproach': Horn no. 358, who notes that Skt prati + gar- means only 'anrufen, begrüssen, antworten' and that Bartholomae would rather think of prati + har-. (c) *paiti-gama- 'that which comes toward (one)' = message: Horn no. 348, and Wiktionary's PIr. *pati- + a formation of *gam- 'to come'. (d) paiti-kāra- 'acting against' from √kar- 'do': here Avestan actually attests the verb - Wiktionary cites Av. paitiakərənaoṯ 'he fought against' - and MP patkār 'battle' is attested (Horn no. 360). So: sound in substance, loose in labelling starred forms 'Avestan'.\",\n \"هر چهار صورت ترکیب پیشوند paiti- با ستاک‌های فعلی اوستایی‌اند و همان ریشه‌هایی اند که هرن و معین برای پیکان، پیغاره، پیغام و پیکار می‌آورند؛ اما سه صورت از آن‌ها بازساخته‌اند (هرن پیش از آن‌ها ستاره می‌گذارد) و ریشهٔ پیکان (paiti + kan «کندن») نزد خود هرن با علامت پرسش همراه است. در مقابل، برای paiti-kāra- فعل اوستایی paitiakərənaot «دربرابر او جنگید» گواهی مستقیم است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n [W + \"%D9%BE%DB%8C%DA%A9%D8%A7%D8%B1#Persian\", W + \"%D9%BE%DB%8C%D8%BA%D8%A7%D9%85#Persian\"],\n [{\"ref\": \"HRN:68-88\", \"status\": \"supports\",\n   \"note\": \"Horn's entries in that page range are exactly these compounds: p.78 '348. peyam ‚Botschaft‘ ... aw. *paiti-gama-; phlv. patgām'; p.80 '358. peiyāre ‚Tadel‘ ... aw. *paiti + 2√gar-'; p.80 '360. peikār, peigār ‚Kampf‘ ... phlv. patkār ‚Kampf‘'; p.81 '362. peikān ‚Pfeilspitze, Pfeil‘. aw. paiti + √kan- (?)'.\"},\n  {\"ref\": \"BQT:400-445\", \"status\": \"supports\",\n   \"note\": \"BQT_v1_pages.txt leaf 671 (printed ~p.445) carries Mo'in's footnotes: 'پیکار و پرگار، از اوستایی paiti+kāra، پهلوی patkār (جنگ) ... «اشتق ۳۹۰»' and 'پیکان - بفتح اول. اوستایی (؟) paiti + kan (بمعنی کندن) ... «اشتق ۳۶۲»' and 'پیغام ... هم‌ریشه و هم‌معنی پیام «اشتق ص ۸۰»'. Mo'in's '؟' after 'اوستایی' for پیکان is the same reservation as Horn's.\"}],\n [{\"src\": \"BRT\", \"where\": \"Bartholomae, AiW, s.v. paiti (preverb) and the paiti.*-compounds\", \"stance\": \"partial\",\n   \"note\": \"BRT.txt gives many real paiti-compounds (paiti.raēθwa-, paiti.mrav-, paiti.jan- 'zurückschlagen', paiti.jasaiti 'entgegengehen') but none of the four starred forms of this node as headwords - they are reconstructions, as Horn's asterisks say.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"پیکار and پیغام\", \"stance\": \"supports\",\n   \"note\": \"پیکار: 'From Middle Persian ptkʾal ... Compare ... Avestan paitiakərənaoṯ (“he fought against”). The preverb is from Old Persian patiš ... ultimately from PIE *próti, and the root is from Proto-Iranian *kar-'. پیغام: 'Ultimately from Old Iranian, from Proto-Iranian *pati- (“against”) + a formation derived from Proto-Iranian *gam- (“to come”).'\"}])\n\n# ---------------- node 7 ----------------\nnode(7, \"Persian\", \"paykân; payğâreh; payğâm; paykâr\", \"plausible\",\n \"The four NP words all show the regular NP outcome pay-/pey- of the Old Iranian preverb pati- before a consonant (Hübschmann no. 345: 'ap. patiy als 1. Glied von Comp. ist neup. zu paδ vor Vokalen, pa vor c/s/š, pai vor den übrigen Consonanten geworden'). پیغام payġām < MP patgām/paygām (MacKenzie 'paygām [pyg'm | N pay(y)ām] message; ~bar messenger, apostle'), whence the doublet پیام with loss of the fricative and the compound پیغمبر/پیامبر = payġām + bar 'carrier'; the same MP word was borrowed into Armenian patgam and into Aramaic/Syriac pitġāmā and Hebrew pitġām. پیکار paykār < MP patkār 'battle' (Horn 360; Arm. loan paykʿar). پیغاره payġāre 'reproach' < *paiti-gara- (Horn 358, with Shahnameh attestations; the chart's Ferdowsi line 'خداوند زیبای برتر منش - از او دور پیغاره و سرزنش' belongs to node #9 in the JSON but is a paygāre verse). پیکان paykān 'arrowhead' is the weak link: Horn and Mo'in both mark the paiti+kan analysis with a question mark, and Wiktionary's entry gives no etymology at all.\",\n \"هر چهار واژه بازتاب قاعدهٔ آوایی معروف‌اند: پیشوند pati- ایرانی باستان پیش از همخوان در فارسی نو به «پیـ» بدل شده است (هوبشمان، شمارهٔ ۳۴۵). «پیغام» از patgām فارسی میانه است که دوگانهٔ «پیام» را هم پدید آورده و در ارمنی patgam و در آرامی/سریانی pitġāmā وام گرفته شده است؛ «پیغمبر» مرکب از پیغام + بر است. «پیکار» از patkār پهلوی و «پیغاره» از *paiti-gara- است. تنها «پیکان» است که هرن و معین هر دو ریشهٔ آن را با علامت پرسش آورده‌اند؛ پس حکم کلی «با احتیاط پذیرفتنی» است.\",\n [W + \"%D9%BE%DB%8C%DA%A9%D8%A7%D8%B1#Persian\", W + \"%D9%BE%DB%8C%D8%BA%D8%A7%D9%85#Persian\",\n  W + \"%D9%BE%DB%8C%DA%A9%D8%A7%D9%86#Persian\"],\n [{\"ref\": \"HRN\", \"status\": \"supports\",\n   \"note\": \"Horn nos. 348 (peyam), 358 (peiyāre), 360 (peikār, peigār), 362 (peikān) - all four NP headwords are there, with the Pahlavi and Avestan antecedents the chart draws.\"},\n  {\"ref\": \"BQT\", \"status\": \"supports\",\n   \"note\": \"BQT_v1_pages.txt leaf 671 (printed ~445) has Mo'in's footnotes on پیکار, پیکان, پیک and پیغام/پیغمبر, each keyed to Horn's numbers ('اشتق ۳۹۰', 'اشتق ۳۶۲', 'اشتق ص ۸۰').\"}],\n [{\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.66 s.v. paygām\", \"stance\": \"supports\",\n   \"note\": \"'paygām [pyg’m | M pygʾam, N pay(y)ām] message. ~bar [-b’r | N -bar] messenger, apostle.'\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, no. 345\", \"stance\": \"supports\",\n   \"note\": \"'ap. patiy als 1. Glied von Comp. ist neup. zu paδ (vor Vocalen), pa (vor c, s, š), pai (vor den übrigen Consonanten) geworden' - the phonetic rule behind pay-kān, pay-ġām, pay-kār.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"پیکان (Persian)\", \"stance\": \"silent\",\n   \"note\": \"The entry gives the senses ('arrowhead') and the Paykan car but carries no Etymology section at all - i.e. no independent modern confirmation of paiti+kan.\"}])\n\n# ---------------- node 8 ----------------\nnode(8, \"Avestan\", \"paiti-band; paiti-man\", \"plausible\",\n \"paiti + √band- 'to bind' is solid: Horn no. 364 'peiwesten ‚verbinden‘ ... aw. *paiti- + √band-; phlv. patwastan, patwand ‚Band‘', and Wiktionary reconstructs PIr. *pati- + *bándati for the same word. paiti + √man- 'to think (back)' is the contested one. Horn no. 312 does say what the chart says ('pižmān, pemān, pižmān ‚bereuend‘, pesīmān. ap. pati + √mand-; phlv. pasīmān; ai. práti + √man- ‚erwiedern, entgegenhalten‘') but immediately admits 'Die Entstehung der Form pešīmān ist ganz unklar'. Hübschmann no. 312 and Nyberg both take the first element to be pas- 'after' instead, giving 'after-thinking' > 'regret', which fits the semantics better. So the node's first compound is confirmed and the second is a live dispute.\",\n \"ترکیب paiti + √band «بستن، پیوستن» مسلم است و هرن (شمارهٔ ۳۶۴) و ویکی‌واژه هر دو آن را پشتیبانی می‌کنند. اما paiti + √man «دربرابر اندیشیدن، پشیمان شدن» محل اختلاف است: هرن همین را می‌گوید ولی خود اعتراف می‌کند پیدایش صورت pešīmān ناروشن است؛ هوبشمان و نیبرگ عنصر نخست را pas- «پس، پس از» می‌دانند یعنی «پس‌اندیش». پس ادعای نورایی در نیمهٔ نخست درست و در نیمهٔ دوم با احتیاط پذیرفتنی است.\",\n [W + \"%D9%BE%DB%8C%D9%88%D8%B3%D8%AA%D9%86#Persian\", W + \"%D9%BE%D8%B4%DB%8C%D9%85%D8%A7%D9%86#Persian\"],\n [{\"ref\": \"HRN:68-88\", \"status\": \"partial\",\n   \"note\": \"Horn no. 364 (p.81) 'peiwesten ‚verbinden‘ ... aw. *paiti- + √band- (s. No. 219); phlv. patwastan, patwand ‚Band‘' - supports. Horn no. 312 (p.69) 'pižmān ... ‚bereuend‘, pesīmān. ap. pati + √mand-; phlv. pasīmān ... ai. práti + √man-' supports the chart, but with Horn's own caveat 'Die Entstehung der Form pešīmān ist ganz unklar'. Both are within pp.68-88.\"},\n  {\"ref\": \"BQT:400-445\", \"status\": \"not_found\",\n   \"note\": \"The پیوستن and پژمان/پشیمان entries fall on BQT pages a little outside the leaves checked (the پیچ/پیش/پیک stretch, leaves 660-671 = pp. ~436-446, was read); no etymological footnote for these two words was legible in the OCR of that stretch.\"}],\n [{\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, no. 312\", \"stance\": \"contradicts\",\n   \"note\": \"'312. Die Form pišman u.s.w. ist verkürzt aus pasīman ... Es wird irgendwie zu zd. pasča ‚nachher‘ und Wrzl. man ‚denken‘ gehören und ursprünglich ‚nachher-bedenkend‘ bedeutet haben.'\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. pašēmānēh\", \"stance\": \"contradicts\",\n   \"note\": \"'pašēmānēh [pšymʾ nyh] repentance ... Of NW origin: paše the NW form corresponding to SW pasē (q.v.) + *māna- ‚measure‘, ‚repentance‘ being understood as ...' - i.e. pas 'after', not paiti.\"},\n  {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW, paiti + band-\", \"stance\": \"supports\",\n   \"note\": \"Bartholomae lists paiti with band- among the preverb constructions ('mit paiti ‚sich gegenüber befinden‘ etc.); the Pahlavi continuation patwastan/patwand is in MacKenzie, see 'consulted' on node #9.\"}])\n\n# ---------------- node 9 ----------------\nnode(9, \"Persian\", \"payvastan; pažmân\", \"plausible\",\n \"پیوستن payvastan 'to join' (present stem پیوند- paywand-) continues MP paywastan/paywand- [ptwstn', ptwnd-] exactly; the preverb pati- appears as pay- before a consonant and the root is *band- 'to bind' (NP بستن bastan), with the noun پیوند 'bond, tie, lineage' beside it - Wiktionary: 'from Proto-Iranian *pati- + *bándati (“to bind”)'. پژمان pažmān (and the ordinary form پشیمان pašīmān) continues MP pašēmān 'penitent, repentant' [pšm'n'], borrowed into Armenian pʿašaman; Horn derives the first element from pati-, Hübschmann and Nyberg from pas 'after', and Wiktionary gives no pre-Middle-Persian analysis at all. The z/ž ~ š alternation of پژمان/پشیمان is dialectal (Horn no. 312 notes 'Der Wechsel von z und s findet sich auch sonst dialectisch'). Because one of the two words rests on a contested first element, the node is plausible rather than confirmed.\",\n \"«پیوستن» (ستاک حال: پیوند-) دقیقاً دنبالهٔ paywastan/paywand- فارسی میانه است، از پیشوند pati- و ستاک *band- «بستن»؛ اسم «پیوند» نیز از همین ساخت است. «پژمان/پشیمان» از pašēmān فارسی میانه است (وام‌واژهٔ ارمنی pʿašaman گواه آن است) و ابدال ژ/ز و ش در آن گویشی است؛ اما دربارهٔ عنصر نخست اختلاف هست: هرن paiti- و هوبشمان و نیبرگ pas- می‌گویند. بنابراین ادعای نورایی با احتیاط پذیرفتنی است.\",\n [W + \"%D9%BE%DB%8C%D9%88%D8%B3%D8%AA%D9%86#Persian\", W + \"%D9%BE%D8%B4%DB%8C%D9%85%D8%A7%D9%86#Persian\"],\n [{\"ref\": \"HRN\", \"status\": \"partial\",\n   \"note\": \"Horn no. 364 for peiwesten fully supports; Horn no. 312 for pižmān/pesīmān supports the chart but with his own reservation, and is explicitly overturned by Hübschmann's note on the same number.\"},\n  {\"ref\": \"BQT\", \"status\": \"not_checked\",\n   \"note\": \"Nourai gives BQT without a page for this node; the پیوستن / پشیمان pages of BQT vol. 1 were not identified in the OCR (only the پیچ-پیک stretch, leaves 660-671, was read).\"}],\n [{\"src\": \"PHD\", \"where\": \"MacKenzie 1971 pp.66, 65\", \"stance\": \"supports\",\n   \"note\": \"'paywastan, paywand- [ptwstn!, ptwnd- | M pywst, N ~] join, connect'; 'paywand [ptwnd | N ~] connection; offspring'; 'pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance.'\"},\n  {\"src\": \"Wiktionary\", \"where\": \"پیوستن and پشیمان\", \"stance\": \"partial\",\n   \"note\": \"پیوستن: 'From Middle Persian ptwstnʹ (paywastan), ptwnd- (paywand-, “to join, to connect”), from Proto-Iranian *pati- + *bándati (“to bind”)' - supports. پشیمان: 'Inherited from Middle Persian pšymʾniy (pašēmān) ... Akin to Old Armenian pʿašaman, a Middle Iranian borrowing' - stops at Middle Persian, offering no support for paiti-man.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. pašēmānēh\", \"stance\": \"contradicts\",\n   \"note\": \"Derives it from NW paše (= SW pasē 'after') + *māna-, not from paiti.\"}])\n\n# ---------------- node 10 ----------------\nnode(10, \"Avestan\", \"paiti-ma; paiti-raeč; paiti-dâhišn; paiti-sahva; paiti-râman\", \"confirmed\",\n \"Every one of the five is the accepted analysis of the corresponding NP word. (a) paiti + √mā- 'to measure': Cheung's EDIV s.v. *maH1 'to measure' lists Av. mā- and MP '(+ *pati-) ptm'd- /paymāy-/ ‚to measure‘'; PIE *meh1- (Pok. 703f.). (b) paiti + √raēč- 'to leave': Cheung s.v. *raič 'to leave, let, abandon' gives 'Y Av. raēc- ... (+ *pati-) “to desert”' with the attested forms paiti raēxšiša and paiti raēcaiieiti, and 'MMP (+ *pati-) phryz- ‚to keep away from, abstain, avoid‘'. (c) *paiti-dāhišn 'given back' > MP pāt-dahišn: Mo'in's footnote in Borhan spells the Pahlavi pātdah(i)šn (paiti + dah(i)šn) explicitly. (d) *paiti-sahva- from √saŋh- 'to speak, proclaim': Horn no. 275, and Wiktionary reconstructs PIr. *paticahwaH from *cánhati < PIE *ḱens- (Skt śaṃsati, Lat. cēnseo). (e) *paiti-rāman- 'well-arranged, pleasant' from rāman- 'peace, joy': Horn no. 287. The label 'Avestan' is again generous - (a), (c), (d), (e) are starred reconstructions - but (b) is genuinely attested in the Avesta.\",\n \"هر پنج ترکیب همان تحلیلی است که امروز هم پذیرفته است: paiti + mā «پیمودن» (چونگ، ذیل *maH1)؛ paiti + raēč «واگذاشتن، پرهیختن» که در خود اوستا با صورت‌های paiti raēcaiieiti گواهی شده است؛ *paiti-dāhišn > pātdahišn پهلوی «پاداشن»؛ *paiti-sahva- از ستاک saŋh «گفتن» که ویکی‌واژه آن را *paticahwaH ایرانی آغازین می‌نویسد؛ و *paiti-rāman- «خوش و آرام». تنها نکته آنکه چهار صورت از پنج بازساخته‌اند و برچسب «اوستایی» برایشان مسامحه‌آمیز است. ادعای نورایی درست است.\",\n [W + \"%D9%BE%DB%8C%D9%85%D9%88%D8%AF%D9%86#Persian\", W + \"%D9%BE%D8%A7%D8%B3%D8%AE#Persian\",\n  W + \"%D9%BE%D8%A7%D8%AF%D8%A7%D8%B4#Persian\"],\n [{\"ref\": \"HRN:68-88\", \"status\": \"supports\",\n   \"note\": \"Horn no. 363 (p.81): 'peiṃūden ‚messen‘ ... aw. *paiti- + √mā-; phlv. patmāyēd, patmān'; no. 309 (p.68): 'perhezīden ‚sich enthalten‘ ... aw. paiti + √raēc- ‚verlassen‘; phlv. pahreχtan'. Both lie in the cited range.\"},\n  {\"ref\": \"BQT:354\", \"status\": \"supports\",\n   \"note\": \"BQT_v1_pages.txt leaf 576 (printed ~p.352-354) is the پاسخ page; its footnote quotes the Armenian loan patasχan and Horn's number ('اشتق ۲۷۵'). The پاداشن entry two leaves earlier (leaf 567) carries a Pahlavi form in Mo'in's footnote.\"},\n  {\"ref\": \"POK:243\", \"status\": \"not_found\",\n   \"note\": \"Pokorny pp. 242-245 (POK_01.txt leaves 252-254) are dhē(i)- ‚saugen‘ and dheiə- ‚sehen‘ - nothing to do with any of the five compounds. The relevant Pokorny pages would be 703f. (mē- ‚messen‘), 669 (leikʷ-), 223f. (dō-), 566 (ḱens-) and 864 (rem-). Probably a misprint in the book.\"},\n  {\"ref\": \"FSF:99\", \"status\": \"not_found\",\n   \"note\": \"FSF_pages.txt has no printed-page tags and no verified offset; the پاداشن/بادافره discussion is on leaf 75 and gives Shahnameh citations and glosses only, no etymology. Could not confirm that this is printed p.99.\"}],\n [{\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *maH1 'to measure' and *raič 'to leave, let, abandon'\", \"stance\": \"supports\",\n   \"note\": \"*maH1: 'BMP ptmʾid- /paymāy-/ “to measure”' under '(+ *pati-)', PIE *meH1- (LIV 424f., Pok. 703f.). *raič: 'Y Av. raēc- “to leave, let” || (+ *pati-) “to desert” ... Aor. s-: OPT. med. 2sg. YAv. paiti raēxšiša (P 40); Caus.: pres. IND. 3sg. YAv. paiti raēcaiieiti (V 5.8, Yt 10.41) ... MIDDLE PERSIAN: (+ *pati-) MMP phryz- “to keep away from, abstain, avoid”'.\"},\n  {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. paiti + raēk-, paiti.raēθwa-\", \"stance\": \"supports\",\n   \"note\": \"BRT.txt: 'mit paiti 1) ‚zurücklassen‘: āfš ... āfš paiti.raēcayāt „.. das Wasser lässt (ihn) zurück‘ V. 5.8' and the lemma 'paiti.raēθwa- n. ‚indirekte Ansteckung‘'.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"پاسخ, پیمودن, پاداش\", \"stance\": \"supports\",\n   \"note\": \"پاسخ: 'from Proto-Iranian *paticahwaH, derived from Proto-Iranian *cánhati, ultimately from Proto-Indo-European *ḱens-. Cognate to Sanskrit śaṃsati, Latin cēnseō.' پیمودن: 'ultimately from *pati- and *maH- (“to measure”) ... from PIE *meh₁-'. پاداش: 'From Middle Persian pʾatdʾāšnʹ (pādāšn) ... Equivalent to پاد- (pād-, “counter-, re-”) + دهش (daheš, “giving”).'\"}])\n\n# ---------------- node 11 ----------------\nnode(11, \"Persian\", \"paymǔdan; parhîxtan; pâdâš; pâsox; Pedrâm\", \"confirmed\",\n \"پیمودن paymūdan (pres. پیمای- paymāy-) 'to measure, traverse' < MP paymūdan/paymāy- < *pati-mā-, with the derivatives پیمانه and پیمان (MP paymān 'measure; treaty'). پرهیختن parhīxtan / پرهیز parhēz < MP pahrēxtan/pahrēz with the regular NP metathesis of -hr- (pahrēz > parhēz), from *pati-raič- 'to leave off'. پاداش pādāš (older پاداشن) < MP pādāšn 'reward, retribution' = pād- 'back, counter-' + dahišn 'giving'; the -ن of پاداشن is still in Asadi's verse quoted on the chart. پاسخ pāsox < MP passōx/pāsox < *pati-sahva- 'speech in return'; Armenian borrowed it as patasχani. پدرام Pedrām 'pleasant, happy' (a personal name today) < *paiti-rāman-; Horn no. 287 'pidrām ‚schön, fröhlich‘ (Šāhn. III, 1803) ... aw. *paiti.rāman-; vergl. np. rām'. All five are standard.\",\n \"«پیمودن» (ستاک حال: پیمای-) از paymūdan فارسی میانه و در نهایت از *pati-mā- است و «پیمانه» و «پیمان» هم از همین خانواده‌اند. «پرهیختن/پرهیز» از pahrēxtan پهلوی است که در فارسی نو قلب (متاتز)ی هـر > رهـ یافته است، از *pati-raič-. «پاداش» صورت کوتاه‌شدهٔ «پاداشن» = pādāšn پهلوی (پاد + دهشن) است و نون پایانی آن در بیت اسدی توسی هنوز هست. «پاسخ» از *paiti-sahva- «سخنِ دربرابر» و «پدرام» از *paiti-rāman-. ادعای نورایی درست است.\",\n [W + \"%D9%BE%DB%8C%D9%85%D9%88%D8%AF%D9%86#Persian\", W + \"%D9%BE%D8%B1%D9%87%DB%8C%D8%B2#Persian\",\n  W + \"%D9%BE%D8%A7%D8%AF%D8%A7%D8%B4#Persian\", W + \"%D9%BE%D8%A7%D8%B3%D8%AE#Persian\"],\n [{\"ref\": \"HRN\", \"status\": \"supports\",\n   \"note\": \"Horn no. 265bis (p.62) 'pādās, pādēs ‚Vergeltung‘, pādāst, pādošn. phlv. pātdah(i)šn (paiti + dah(i)šn)'; no. 275 'pāsuχ ‚Antwort‘. aw. *paitisahva- (paiti + √saŋh-); phlv. pasuχ; arm. patasχani'; no. 287 'pidrām ‚schön, fröhlich‘ ... aw. *paiti.rāman-'; no. 309 perhezīden; no. 363 peiṃūden. Every word of the node has its Horn entry.\"},\n  {\"ref\": \"BQT\", \"status\": \"supports\",\n   \"note\": \"BQT_v1_pages.txt leaf 567 (پاداش/پاداشن, with a Pahlavi form in Mo'in's footnote) and leaf 576 (پاسخ, footnote citing the Armenian patasχan and Horn no. 275).\"}],\n [{\"src\": \"PHD\", \"where\": \"MacKenzie 1971 pp. 64-67\", \"stance\": \"supports\",\n   \"note\": \"'pādāšn [pʾatdʾāšnʹ | M pʾidʾāšyn, N pādāš] reward, retribution'; 'paymūdan, paymāy- [ptmwtnʹ, ptmʾid- | N ~] measure'; '1pahrextan, pahrēz- [phlyhtnʹ, pʾihlyc- | M phryz-, N parhēxtan, parhēz-] abstain, refrain, avoid'; 'passox [pshw! | M pswx, N pāsux] answer'.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, leaf 351 (پاسخ)\", \"stance\": \"supports\",\n   \"note\": \"'واژهٔ فارسی پاسخ از واج‌ریشه‌های پاد و سخن تشکیل شده است، (پهلوی آن: pāsox/pasox، کردی: ...، ارمنی: patasxani)' - the same pād + saxvan analysis.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"پرهیز\", \"stance\": \"partial\",\n   \"note\": \"'From Middle Persian pʾihlyc (pahrēz, “defence; care”)' - confirms the MP antecedent and the -hr- > -rh- metathesis but stops there; the *pati-raič- analysis comes from Cheung (node #10).\"}])\n\n# ---------------- node 12 ----------------\nnode(12, \"Avestan\", \"peret; ni-part; â-part\", \"confirmed\",\n \"Av. pərət- f. 'Kampf, Streit' is a real Avestan noun (Bartholomae's AiW has the lemma '*pərət- f. ‚Kampf, Streit‘', alongside pəšana- 'Kampf, Schlacht' and pərətamna 'die miteinander Kämpfenden'), and it is the Iranian half of Pokorny's 3. per- 'schlagen' - Indo-Iranian shows the root only with the t-suffix (Skt pṛt-, pṛtanā). The two prefixed forms are Old Iranian compounds reconstructed from their Middle/New Persian outcomes: *ni-pṛta- 'fought down' > MP nibard [nplt'] 'fight, battle', and *ā-pṛta- > NP āvard 'combat'. Mo'in's footnote in Borhan spells it out: 'آورد ... پهلوی nipart (جنگ، نزاع)، ایرانی باستان ni+pərət (مبارزه کردن) «بارتولمه ۸۹۸»'. Nourai's 'peret' is simply his transliteration of pərət-.\",\n \"اسم اوستایی pərət- «نبرد، ستیز» واقعی است و بارتولومه آن را در فرهنگ ایرانی باستان آورده است؛ در زبان‌های هندوایرانی این ریشه فقط با پسوند -t دیده می‌شود (سنسکریت pṛt-، pṛtanā). دو صورت پیشونددار بازساخته‌اند: *ni-pṛta- که در پهلوی nibard شده و *ā-pṛta- که به «آورد» رسیده است. حاشیهٔ معین بر برهان قاطع همین را با ارجاع به بارتولومه و هرن می‌گوید. ادعای نورایی درست است.\",\n [],\n [{\"ref\": \"POK:818\", \"status\": \"supports\",\n   \"note\": \"POK_03.txt leaf 52 (p.818): '3. per-, perg- ‚schlagen‘. Arisch nur mit t-Formans: ai. pṛt-, pṛtanā ‚Kampf, Streit‘, av. pərət-, pəšanā ‚Kampf, Schlacht‘, pərətamna ‚die miteinander Kämpfenden‘, vaiti-parətata ‚bekämpft‘'. Precisely the node's claim.\"}],\n [{\"src\": \"BRT\", \"where\": \"Bartholomae, AiW, s.v. *pərət- and pəšana-\", \"stance\": \"supports\",\n   \"note\": \"BRT.txt: '• j. *pərət- f. ‚Kampf, Streit‘: χštēm ham.vainišm ‘tasča mərəvayasča hamaēstarə Yt 11.15' and '• j. pəšana- n., pəšanā- f. ‚Kampf, Schlacht‘'. Mo'in's Borhan footnote cites Bartholomae col. 898 for ni+pərət.\"},\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II, '8. per-, per-g-, per-q- ‚schlagen‘'\", \"stance\": \"supports\",\n   \"note\": \"'Arisch nur mit t-Formans: ai. pṛt-, pṛtanā ‚Kampf, Streit‘, av. pərət-, pəšanā ‚Kampf, Schlacht‘, pərətamna ‚die miteinander Kämpfenden‘, paiti-parətata ‚bekämpft‘ (Bugge KZ 32,36)'. Note that WLD's last example is itself a paiti-compound of this root.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. per-5\", \"stance\": \"supports\",\n   \"note\": \"'per-5. To strike. Extended forms *prem-, pres- in Latin premere ... [Pok. 3. per- 818.]' - the same Pokorny page Nourai cites, though Watkins numbers it as a root separate from per-1.\"}])\n\n# ---------------- node 13 ----------------\nnode(13, \"Persian\", \"nabard; âvard\", \"confirmed\",\n \"نبرد nabard 'battle' continues MP nibard [nplt'] 'fight, struggle, battle' (MacKenzie p.58, with the denominative nibardīdan 'to do battle' and the compound ham-nibardīh 'single combat'), from OIr. *ni-pṛta- 'struck down, fought down'; the NP forms نبرده 'valiant' and نبردیدن belong with it. آورد āvard 'combat' (and the common آوردگاه 'battlefield', آوردیدن) is the same formation with *ā-. Horn no. 1025 states both: 'nebeرd ‚Kampf‘ ... aw. *ni + √parət-, pərətənte ‚sie kämpfen‘; phlv. n(i)part ‚Kampf‘ (AV.). Vergl. np. āwerd ‚Kampf‘ (Šāhn. I,218 V.1506), āwerdgāh (häufig), āwerīden.' Mo'in repeats it in Borhan with references to Horn 1025 and Bartholomae 898. The only dissent found is the unsourced remark in the English Wiktionary entry that MP nipart is 'derived via well-known prefix ni- from the stem of the verb which is in Neo-Persian بردن' - i.e. from bar- 'to carry'; that is a folk analysis of the homophony with برد and is contradicted by the Pahlavi spelling nplt' with p, which excludes *bar-.\",\n \"«نبرد» دنبالهٔ nibard فارسی میانه (به خط پهلوی npltʹ) از *ni-pṛta- ایرانی باستان است و «آورد/آوردگاه» همان ساخت با پیشوند *ā-. هرن (شمارهٔ ۱۰۲۵) و حاشیهٔ معین بر برهان قاطع هر دو همین را می‌گویند و به بارتولومه ارجاع می‌دهند. یک دیدگاه مخالف در ویکی‌واژهٔ انگلیسی آمده که آن را از ستاک «بردن» می‌گیرد؛ این ریشه‌شناسی عامیانه است و نگاشت پهلوی با «p» آن را رد می‌کند. ادعای نورایی درست است.\",\n [W + \"%D9%86%D8%A8%D8%B1%D8%AF#Persian\"],\n [{\"ref\": \"HRN:230\", \"status\": \"supports\",\n   \"note\": \"HRN.txt leaf 251 (printed p.230): '1025. neberd ‚Kampf‘, newerd, neberde ‚tapfer‘ (Šāhn. I, 93 Vers 586). aw. *ni + √parət, pərətənte ‚sie kämpfen‘; phlv. n(i)part ‚Kampf‘ (AV.). Vergl. np. āwerd ‚Kampf‘ (Šāhn. I, 218 Vers 1506), āwerdgāh (häufig), āwerīden.' Exactly the node.\"},\n  {\"ref\": \"BQT:2115\", \"status\": \"supports\",\n   \"note\": \"BQT vol.4, pdf page 198 = printed 2115 (printed = pdf + 1917). The نبرد entry ('بمعنی کوشش و جنگ و جدال و رزم') with Mo'in's footnote: 'آورد «اشتق ۱۰۲۵» پهلوی nipart (جنگ، نزاع)، ایرانی باستان ni+pərət (مبارزه کردن) «بارتولمه ۸۹۸»'.\"}],\n [{\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.58 s.v. nibard\", \"stance\": \"supports\",\n   \"note\": \"'nibard [npltʹ | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [nplt-ytn! | P nbrdʹd] fight, do battle.' Also 'ham-nibardīh [hmnpltyh] (single) combat.'\"},\n  {\"src\": \"Wiktionary\", \"where\": \"نبرد (Persian)\", \"stance\": \"contradicts\",\n   \"note\": \"'Inherited from Middle Persian npltʹ (nipart), derived via well-known prefix ni- from the stem of the verb which is in Neo-Persian بردن (burdan).' No source is given, and the Pahlavi p of npltʹ tells against a *bar- etymology; Horn, Bartholomae and Mo'in all have ni- + pərət-.\"},\n  {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.4 p.2115 (Mo'in's footnote)\", \"stance\": \"supports\",\n   \"note\": \"Same footnote as in ref_check: it derives both نبرد and آورد from ni/ā + pərət, citing Horn 1025 and Bartholomae 898.\"}])\n\nout = {\n \"pdf_page\": 396,\n \"book_page\": 366,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-396.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-396.py",
 "description": "Write page-396.json"
}
```


### [2026-09-14T01:12:14.601Z] TOOL RESULT

```
written
```


## [2026-09-14T01:12:22.228Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,io\np='data/verification/page-396.json'\nd=json.load(open(p,encoding='utf-8'))\nn13=[n for n in d['entries'][0]['nodes'] if n['id']==13][0]\nn13['derivation']=n13['derivation'].replace(\"nebeرd\",\"neberd\")\njson.dump(d,io.open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)\nopen(p,'a',encoding='utf-8').write(\"\\n\")\nprint('ok', 'nebeرd' in json.dumps(d,ensure_ascii=False))\nEOF\npython3 -m json.tool data/verification/page-396.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 396",
 "description": "Fix typo and run verify_check"
}
```


### [2026-09-14T01:12:23.573Z] TOOL RESULT

```
ok False
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 7, 'plausible': 5, 'disputed': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 14, 'partial': 3, 'not_checked': 3, 'not_found': 3}
books consulted: {'supports': 24, 'contradicts': 8, 'partial': 4, 'silent': 1} | by book: {'Wiktionary': 8, 'PHD': 7, 'BRT': 5, 'HUB': 5, 'HRN': 4, 'NYB': 2, 'KNT': 1, 'CHEUNG': 1, 'ARY': 1, 'WLD': 1, 'AHD': 1, 'BQT': 1}
```


## [2026-09-14T01:12:43.605Z] AGENT

Verification of PDF page 396 (book page 366) is complete and `verify_check.py 396` reports **0 PROBLEM lines**.

**Page 396 — root "Per 3" (Indo-European, "opposite, against, in front of, strike"), 1 entry, 13 nodes**

- Node verdicts: confirmed 7, plausible 5, disputed 1. Root verdict: plausible.
- Ref checks: supports 14, partial 3, not_found 3, not_checked 3. Books consulted: POK, WLD, AHD, BRT, KNT, PHD, NYB, HRN, HUB, CHEUNG, BQT (vols 1 and 4), ARY, Wiktionary.

Flagged items:

- **ROOT "Per 3" (plausible)** — the box merges two roots Pokorny, Walde-Pokorny and Watkins all keep apart: *próti/*preti "against" (POK 815-816, under 1. per- A.h) and *per-/*perg- "to strike" (POK 818, 3. per-). Nourai's page range is exact for both, so the citation is right but the root is a conflation. Also, Iranian *pati is the r-less *poti variant, not *preti (Pokorny himself: "ai. práti, im Iran. durch paiti verdrängt").
- **#3 Persian bod/bad 2 «-بد» (disputed)** — the suffix of سپهبد/موبد/هیربد goes back to OIr. *pati- "lord, master" (Av. paiti- m. 'Herr', Skt páti-, PIE *pótis), a homonym of the preposition paiti, not a derivative of "in front of". Horn keeps them in separate entries (no. 188 vs no. 345); Mo'in's own footnote at the cited BQT:2405 derives هیربد from Av. aēθra-paiti- "master of learning". پیش in the same node is fine; the node takes the worse verdict.
- Contested but not disputed overall: #2 پیش (Hübschmann no. 356 rejects Horn's pēš < OP patiš; modern preference is Edelman's *pati-aši-), and #8/#9 پژمان/پشیمان (Horn = Nourai's paiti-man, but Hübschmann no. 312 and Nyberg derive it from pas "after" + man).

Book/reference problems the owner may want to note (no extraction errors found — the JSON matches the chart everywhere):

- **POK:243 in node #10 is a misprint in the book.** Pokorny pp. 242-245 are dhē(i)- "saugen" / dheiə- "sehen"; the roots actually needed are at POK 703f., 669, 223f., 566 and 864.
- **FSF:99 (node #10) could not be located**: FSF_pages.txt has no page tags and no verified offset; the پاداشن material sits on leaf 75 and carries no etymology anyway.
- **AEF:190-191 (nodes #4, #5) is not online**; since AEF is the Persian translation of Horn/Hübschmann, Horn no. 144 (p.33) was read instead and confirms the NOTE verbatim.

All web pages used were archived via `tools/fetch_source.py` (16 Wiktionary URLs).
