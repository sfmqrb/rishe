# Verification process log — verify-page-215


## [2026-09-06T14:52:36.985Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 215 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-215.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-215.json. Write /home/sfmqrb/git/rishe/data/verification/page-215.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 215` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:52:38.472Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T14:52:39.184Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:52:39.197Z] TOOL RESULT

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


## [2026-09-06T14:52:39.426Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-215.txt"
}
```


### [2026-09-06T14:52:39.448Z] TOOL RESULT

```
1	=== PDF page 215 (book page 185) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwhen 2 : to strike, hurt  (refs POK:492)
4	#1 (parent #0) [Avestan] refs=POK:492; HRN:204; BQT:324; FFD:25 | žata 2, jan, gan 2, gaz,gaš : to hit, harm, bite ; â-ža-ta 2 : harmed ; vî-jainti : to sting, harm ☞Wi ; varathra-ğam : demon killer ☞Wer 3
5	  #2 (parent #1) [Persian] refs=HRN:204; BQT:324,1007,1812; FSF:26 | zadan «زدن» : to hit, strike ; âzdan «آزدن» : to poke ; gazîdan «گزیدن ٢ ( گزیدن ، گشتن ٢ ، گزند )» : to sting ; Bahrâm «بهرام» : "demon killer", a male name | extra: آژدن ، آژندن ، آژیدن ، آجدن ، آجیدن
6	#3 (parent #0) [Old Persian] refs=KNT:184,185 | jan : to strike
7	  #4 (parent #3) [Old Persian] refs=HRN:231 | ni-jan : to strike down, to put (somebody) down ☞Nî 1
8	    #5 (parent #4) [Persian] refs=BQT:2134; HRN:231; MON:4713 | nažand «نژند» : put down, feeling sad
9	  #6 (parent #3) [Old Persian] refs=KNT:184 | ava-jan, apa-jan : to strike down, kill
10	    #7 (parent #6) [Persian] refs=BQT:184; FSF:55 | owžandan «اوژندن ( اوژدن ، ـ اوژن )» : to strike down | extra: اوژنیدن ، شیراوژن ، گرداوژن
11	  #8 (parent #3) [Old Persian] refs=POK:1170; BQT:1669 | vâra-ğna : lamb killer (falcon, crow) ☞Weren
12	    #9 (parent #8) [Sogdian] refs=SOD:398 | w`rğn`k : falcon
13	    #10 (parent #8) [Persian] refs=BQT:1669; SOD:398 | varğeneh «ورغنه» : falcon ; kalâğ «کلاغ» : crow
14	  #11 (parent #3) [Old Persian] refs=KNT:184,185; HRN:231 | pati-jan : fight against ☞Per 3 ; fra-jan : cut off ☞Per 1 ; vi-jan : strike apart, shatter ☞Wi
15	#12 (parent #0) [Avestan / Old Persian] refs=AHD:1520; AEF:335 | jatara : resin (obtained by striking a tree trunk) ; jathra : poison ; paiti-jathra : anti-poison ☞Per 3 | NOTE: Derivation of "jatara: resin" is not certain
16	  #13 (parent #12) [Persian] refs=MON:1776; BQT:175,1776 | žad «ژد ( ژه ، زه ٣ )» : resin ; angžeh «انگژه» : sweet resin ☞Embhi | extra: انگژد ، انگورژد ، انغوزه
17	  #14 (parent #12) [Persian] refs=BQT:1047 | zahr «زهر» : poison ; pâdzahr «پادزهر ( پازهر ، پای زهر )» : antitoxin | NOTE: KLN:168 derives this from Avestan "zahr: bile", See "Ghel".
18	    #15 (parent #14) [Arabic] refs=FVF:50 | bâdzahr
19	      #16 (parent #15) [English] refs=AHD | bezoar
20	#17 (parent #0) [Germanic] refs=AHD:1520 | guthjô : war
21	  #18 (parent #17) [English] refs=None | gun
22	#19 (parent #0) [Latin] refs=AHD | fendere, off-endere, de-fendere : to strike off, attack
23	  #20 (parent #19) [English] refs=None | fender, fence, offense, defense
24	
```


## [2026-09-06T14:52:43.895Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-215.json | head -200",
 "description": "Read source JSON"
}
```


### [2026-09-06T14:52:43.941Z] TOOL RESULT

```
{
  "pdf_page": 215,
  "book_page": 185,
  "entries": [
    {
      "root": {
        "name": "Gwhen 2",
        "lang": "Indo-European",
        "refs": "POK:492",
        "gloss": "to strike, hurt"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:492; HRN:204; BQT:324; FFD:25",
          "words": [
            {"translit": "žata 2, jan, gan 2, gaz,gaš", "gloss": "to hit, harm, bite", "script": null},
            {"translit": "â-ža-ta 2", "gloss": "harmed", "script": null},
            {"translit": "vî-jainti", "gloss": "to sting, harm", "script": null, "see": ["Wi"]},
            {"translit": "varathra-ğam", "gloss": "demon killer", "script": null, "see": ["Wer 3"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:204; BQT:324,1007,1812; FSF:26",
          "words": [
            {"translit": "zadan", "gloss": "to hit, strike", "script": "زدن"},
            {"translit": "âzdan", "gloss": "to poke", "script": "آزدن"},
            {"translit": "gazîdan", "gloss": "to sting", "script": "گزیدن ٢ ( گزیدن ، گشتن ٢ ، گزند )"},
            {"translit": "Bahrâm", "gloss": "\"demon killer\", a male name", "script": "بهرام"}
          ],
          "script_extra": "آژدن ، آژندن ، آژیدن ، آجدن ، آجیدن",
          "note": null,
          "quote": {"text": "به داغی جگرشان کنی آژده - که بخشایش آرد بر ایشان دده", "poet": "Ferdowsî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:184,185",
          "words": [
            {"translit": "jan", "gloss": "to strike", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Old Persian",
          "refs": "HRN:231",
          "words": [
            {"translit": "ni-jan", "gloss": "to strike down, to put (somebody) down", "script": null, "see": ["Nî 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:2134; HRN:231; MON:4713",
          "words": [
            {"translit": "nažand", "gloss": "put down, feeling sad", "script": "نژند"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "چنین داد پاسخ که چرخ بلند - دلم کرد پر درد و جانم نژند", "poet": "Ferdowsî"}
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "Old Persian",
          "refs": "KNT:184",
          "words": [
            {"translit": "ava-jan, apa-jan", "gloss": "to strike down, kill", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:184; FSF:55",
          "words": [
            {"translit": "owžandan", "gloss": "to strike down", "script": "اوژندن ( اوژدن ، ـ اوژن )"}
          ],
          "script_extra": "اوژنیدن ، شیراوژن ، گرداوژن",
          "note": null,
          "quote": {"text": "گرفتند هرسه ورا در کنار - بپرسید شیراوژن از شهریار", "poet": "Ferdowsî"}
        },
        {
          "id": 8,
          "parent": 3,
          "lang": "Old Persian",
          "refs": "POK:1170; BQT:1669",
          "words": [
            {"translit": "vâra-ğna", "gloss": "lamb killer (falcon, crow)", "script": null, "see": ["Weren"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Sogdian",
          "refs": "SOD:398",
          "words": [
            {"translit": "w`rğn`k", "gloss": "falcon", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "Persian",
          "refs": "BQT:1669; SOD:398",
          "words": [
            {"translit": "varğeneh", "gloss": "falcon", "script": "ورغنه"},
            {"translit": "kalâğ", "gloss": "crow", "script": "کلاغ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 3,
          "lang": "Old Persian",
          "refs": "KNT:184,185; HRN:231",
          "words": [
            {"translit": "pati-jan", "gloss": "fight against", "script": null, "see": ["Per 3"]},
            {"translit": "fra-jan", "gloss": "cut off", "script": null, "see": ["Per 1"]},
            {"translit": "vi-jan", "gloss": "strike apart, shatter", "script": null, "see": ["Wi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "AHD:1520; AEF:335",
          "words": [
            {"translit": "jatara", "gloss": "resin (obtained by striking a tree trunk)", "script": null},
            {"translit": "jathra", "gloss": "poison", "script": null},
            {"translit": "paiti-jathra", "gloss": "anti-poison", "script": null, "see": ["Per 3"]}
          ],
          "script_extra": null,
          "note": "Derivation of \"jatara: resin\" is not certain",
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:1776; BQT:175,1776",
          "words": [
            {"translit": "žad", "gloss": "resin", "script": "ژد ( ژه ، زه ٣ )"},
            {"translit": "angžeh", "gloss": "sweet resin", "script": "انگژه", "see": ["Embhi"]}
          ],
          "script_extra": "انگژد ، انگورژد ، انغوزه",
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "Persian",
          "refs": "BQT:1047",
          "words": [
            {"translit": "zahr", "gloss": "poison", "script": "زهر"},
            {"translit": "pâdzahr", "gloss": "antitoxin", "script": "پادزهر ( پازهر ، پای زهر )"}
          ],
          "script_extra": null,
          "note": "KLN:168 derives this from Avestan \"zahr: bile\", See \"Ghel\".",
          "quote": {"text": "مبادا که گستاخ باشی به دهر - یکی زهر یابد یکی پای زهر", "poet": "Ferdowsî"}
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Arabic",
          "refs": "FVF:50",
          "words": [
            {"translit": "bâdzahr", "gloss": null, "script": null}
```


## [2026-09-06T14:52:44.444Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-06T14:52:44.509Z] TOOL RESULT

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
page-130.json
page-131.json
page-132.json
page-133.json
page-134.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-149.json
---
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


## [2026-09-06T14:52:48.525Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-215.json'))\nprint(json.dumps(d['entries'][0]['nodes'][14:], ensure_ascii=False, indent=1))\nprint('num entries', len(d['entries']))\n\"",
 "description": "Read tail of JSON"
}
```


## [2026-09-06T14:52:48.775Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py",
 "description": "Read verify_check"
}
```


### [2026-09-06T14:52:50.936Z] TOOL RESULT

```
[
 {
  "id": 15,
  "parent": 14,
  "lang": "Arabic",
  "refs": "FVF:50",
  "words": [
   {
    "translit": "bâdzahr",
    "gloss": null,
    "script": null
   }
  ],
  "script_extra": null,
  "note": null,
  "quote": null
 },
 {
  "id": 16,
  "parent": 15,
  "lang": "English",
  "refs": "AHD",
  "words": [
   {
    "translit": "bezoar",
    "gloss": null,
    "script": null
   }
  ],
  "script_extra": null,
  "note": null,
  "quote": null
 },
 {
  "id": 17,
  "parent": 0,
  "lang": "Germanic",
  "refs": "AHD:1520",
  "words": [
   {
    "translit": "guthjô",
    "gloss": "war",
    "script": null
   }
  ],
  "script_extra": null,
  "note": null,
  "quote": null
 },
 {
  "id": 18,
  "parent": 17,
  "lang": "English",
  "refs": null,
  "words": [
   {
    "translit": "gun",
    "gloss": null,
    "script": null
   }
  ],
  "script_extra": null,
  "note": null,
  "quote": null
 },
 {
  "id": 19,
  "parent": 0,
  "lang": "Latin",
  "refs": "AHD",
  "words": [
   {
    "translit": "fendere, off-endere, de-fendere",
    "gloss": "to strike off, attack",
    "script": null
   }
  ],
  "script_extra": null,
  "note": null,
  "quote": null
 },
 {
  "id": 20,
  "parent": 19,
  "lang": "English",
  "refs": null,
  "words": [
   {
    "translit": "fender, fence, offense, defense",
    "gloss": null,
    "script": null
   }
  ],
  "script_extra": null,
  "note": null,
  "quote": null
 }
]
num entries 1
```


### [2026-09-06T14:52:50.969Z] TOOL RESULT

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
```


## [2026-09-06T14:52:53.648Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 80,160p tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-06T14:52:53.686Z] TOOL RESULT

```
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


## [2026-09-06T14:52:56.879Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BQT','FFD','KNT','SOD','MON','FSF','AHD','AEF','FVQ','FVF','KLN','BRT','CHEUNG','PHD','NYB','WLD','ARY','IEC','SYN','SKT','LKT','PLA','AFM']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print(k, v.get('kind'), '|', str(v.get('title'))[:60], '| local:', v.get('local_file'), '| off:', v.get('page_offset'), '| hint:', str(v.get('lookup_hint'))[:80])\n\"",
 "description": "Read refs_online keys"
}
```


### [2026-09-06T14:52:59.156Z] TOOL RESULT

```
POK archive_djvu | J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | off: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry 
HRN archive_djvu | P. Horn, Grundriss der neupersischen Etymologie, Strassburg  | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | off: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep 
BQT archive_djvu+local_scan_ocr | Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymo | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | off: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f;
FFD local_scan_ocr | Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] | off: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general 
KNT archive_djvu | R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1 | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | off: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line st
SOD archive_djvu | Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictio | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] | off: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may b
MON website+archive_djvu | Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/198 | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | off: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in'
FSF archive_djvu | Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Dosh | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt'] | off: 484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking | hint: grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php searc
AHD archive_djvu+website+archive_restricted | W. Morris (ed.), The American Heritage Dictionary of the Eng | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | off: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor
AEF catalog | Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), | local: None | off: None | hint: Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings
FVQ archive_djvu | Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwa | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | off: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; pri
FVF website | S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban- | local: None | off: None | hint: Alphabetical by Persian headword; noorlib page number N is the scan page — brows
KLN archive_djvu | E. Klein, A Comprehensive Etymological Dictionary of the Eng | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | off: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evad
BRT archive_djvu | C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (r | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | off: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP 
CHEUNG MISSING
PHD archive_djvu | D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971 | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | off: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script 
NYB archive_djvu | H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part I | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | off: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in tr
WLD archive_djvu | A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indoger | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | off: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' 
ARY local_scan_ocr | Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Oru | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | off: printed page = pdf page + 1 | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by lan
IEC archive_djvu | S. E. Mann, An Indo-European Comparative Dictionary, Hamburg | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | off: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456'
SYN archive_djvu | C. D. Buck, A Dictionary of Selected Synonyms in the Princip | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | off: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words
SKT archive_djvu | W. W. Skeat, A Concise Etymological Dictionary of the Englis | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | off: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse 
LKT archive_djvu | K. Lokotsch, Etymologisches Wörterbuch der europäischen Wört | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | off: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by
PLA archive_djvu | A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 19 | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | off: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only 
AFM archive_djvu | Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arra | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | off: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pa
```


## [2026-09-06T14:53:03.357Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-202.json'))\nprint({k:v for k,v in d.items() if k!='entries'})\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'}, ensure_ascii=False, indent=1)[:2500])\nprint(json.dumps(e['nodes'][0], ensure_ascii=False, indent=1)[:2500])\n\"",
 "description": "Sample existing verification file"
}
```


### [2026-09-06T14:53:05.096Z] TOOL RESULT

```
{'pdf_page': 202, 'book_page': 172, 'verified_by': 'claude-opus-5', 'verified_on': '2026-09-05'}
{
 "entry": 0,
 "root": "Gwa, Gwâ, Gwen 2",
 "verdict": "confirmed",
 "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
 "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
 "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-"
 ],
 "ref_check": [
  {
   "ref": "POK:463",
   "status": "supports",
   "note": "POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; z
{
 "id": 1,
 "lang": "Avestan / Old Persian",
 "words": "gam : to come, step; jam, jantu : to go",
 "verdict": "confirmed",
 "derivation": "Indo-Iranian inherits PIE *gʷem- as the root gam- (Skt. gam-, Av. gam-, OP gam-). In Avestan the root appears in two guises that Nourai lists side by side: (a) gam- proper, in the perfect and in nominal derivatives (gāman-, gata-), and (b) jam-, the regular Avestan outcome of the full-grade *gʷem- (PIE labiovelar *gʷ- > Indo-Iranian *ǰ before front vowel of the thematic/subjunctive stems: *gʷem-e-ti > Av. jamaiti 'goes'), beside the inchoative present jasaiti < *gʷm̥-sk̑e-ti. jantu- is the tu-stem *gʷem-tu- 'a going, coming' (= Skt. gántu-, Lat. adventus), which Pokorny prints on the same page. Old Persian has the root only in compounds (ā-gam-, ham-gam-, parā-gam-), and there too the reflexes with j- (ājamiyā 'may he come') alternate with the g- of the participles (paragmatā, hangmatā). Nourai's glosses 'to come, step' / 'to go' are correct.",
 "derivation_fa": "ریشهٔ هندواروپایی *gʷem- در هندوایرانی به‌صورت gam- بازمانده است (سنسکریت gam-، اوستایی gam-، پارسی باستان gam-). در اوستایی دو گونه در کنار هم دیده می‌شود که نورایی هر دو را آورده است: نخست gam- که در ستاک‌های اسمی و کامل می‌ماند (gāman-، gata-)، و دوم jam- که پیامد آوایی قانونمند *gʷ- در ایرانی است (واک‌گونهٔ لبی‌کامی هندواروپایی پیش از واکهٔ پیشین به ǰ بدل می‌شود: *gʷem-e-ti > اوستایی jamaiti «می‌رود»)؛ ستاک حال آغازی نیز jasaiti < *gʷm̥-sk̑e-ti است. jantu- همان ستاک tu-دار *gʷem-tu- «رفت، آمد» است (هم‌ریشه با gántu- سنسکریت و adventus لاتین) که پوکورنی در همان صفحهٔ ۴۶۵ آورده. در پارسی باستان این ریشه تنها با پیشوند به‌کار رفته (ā-gam-، ham-gam-، parā-gam-). ادعای نورایی در این گره درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-",
  "https://en.wiktionary.org/wiki/آمدن"
 ],
 "ref_check": [
  {
   "ref": "POK:463",
   "status": "supports",
   "note": "POK_02.txt p.464-465 (the continuation of the entry that begins on 463): 'thematisch: hochstufig ai. gámati, av. jamaiti „geht“', 'sk̑o-Präsens *gʷm̥-sk̑ō: ai. gácchati, av. jasaiti „er geht“', and 'nach Schwyzer … könnte das n auch von Formen wie av. jantu (*gʷem-tu-) … bezogen sein'. All three of Nourai's forms are there."
  },
  {
   "ref": "KLN:318",
   "status": "supports",
   "note": "KLN_1966.txt line 8320, s.v. 'come' (page number 318 printed at the foot of the block): 'fr. I.-E. base *gʷem-, “to go; to come”, whence also OI. gámati, gacchati, “he go
```


## [2026-09-06T14:53:44.517Z] AGENT

Now let me start the source work. First the PIE root.


## [2026-09-06T14:53:46.837Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; grep -n \"g\\^ʷhen\\|gʷhen\\|gʷhen\\|ghen-\\|gu̯hen\" $f | head -20; done",
 "description": "Grep Pokorny for gwhen"
}
```


## [2026-09-06T14:53:48.248Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"gwhen\\|gʷhen\\|g\\*hen\" AHD_watkins1985.txt | head -20; echo \"---KLN bezoar/gun\"; grep -n \"^bezoar\\|^gun,\\|^gun \" KLN_1966.txt | head",
 "description": "Grep AHD and Klein"
}
```


### [2026-09-06T14:53:50.349Z] TOOL RESULT

```
== POK_01.txt
98:agher-,  nghen-,  Eghes-  (oder  ogher  usw.)  ^Tag'.  Heteroklit.  Neutrum.
596:anghen-  ,Duft,  Gei'uch,  Persona
== POK_02.txt
1380:ghen-  »zernagen»  zerrdben,  kratzen*»  auch  »Kleines,  Bißchen*.
1408:vielleicht  hierher   (als   mit   cymr.  genni  bildungsverwandtes  ^ghend-nö). got.  du-ginnan,  ags.  on-,  bi-ginnan,  as.  ahd.  biginnan  ,in-cipere,   beginnen'! (andere   Deutungsversuche    s.  bei  Feist  ^  s.  v. ;    davon   beachtenswert  dei von  Wiedemann  BB.  27,  193  als  *ghen-uö  zu  alb.  ze,  geg.  zä  ,berühre,  fang« fange  an,  empfange  [vom  Weibe],  miete'  aus  uralb.  "^zeno) ;
4194:gr.  xoWg,  -löoq  f.  (*knid-s),  wohl  an  ^/.öviq  , Staub'  angeglichen; mir.  sned  f.  ,Nisse',  kymr.  PI.  nedd,  nkorn.  ned,  bret.  nez  ds.  (*s(k)nida); ags.  hnitu  f.,  ahd.  (h)niz,  nhd.  Nisse  ,Ei  der  Laus'  (*knidä). Könnte  zu  (s)ken-  ,kratzen'  gehören,  wie  ghnldä  zu  ghen-  ds. WP.  I  461,  WH.  I  783  f.,  Specht  Idg.  Dekl.  44,    Trautmann  93.
== POK_03.txt
```


### [2026-09-06T14:53:50.414Z] TOOL RESULT

```
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
---KLN bezoar/gun
4878:bezoar,  n.,  orig.  a  term  for  antidote-,  later  used for  concoctions  found  in  the  stomach  or  in¬ testines  of  certain  animals  and  thought  to  have antidotal  properties.  —  F.  bezoard,  fr.  Sp.  be¬ zoar  (cp.  Port,  bezuar),  fr.  Arab,  badizdhr,  often shortened  into  bazahr  (see  Freytag,  Lexicon
```


## [2026-09-06T14:53:59.489Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=147 && NR<=150 {print \"===LEAF \" NR-1 \"===\"; print}' POK_02.txt | head -120",
 "description": "Print Pokorny leaves around p.491"
}
```


## [2026-09-06T14:54:00.184Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"g\\*hen\" AHD_watkins1985.txt | head -20; echo \"=== klein bezoar ctx\"; sed -n '4874,4890p' KLN_1966.txt",
 "description": "AHD gwhen and Klein bezoar context"
}
```


### [2026-09-06T14:54:01.936Z] TOOL RESULT

```
===LEAF 146===
bgierig,  geizig',  godziüoi^ godetis  ,begehren,  wonach  dürsten,  wünschen,  begierig  sein';
im  Slav.  mit  durchgeführter  Nasalierung :  aksl.  z^zdq^  ^^dati,  acech.  Mdatil ,begehren,  wonach  dürsten',  z^zdg,  zedeti  ,cupere',  z^^da  , Durst',  poln/ zqdza  ,Begehren,  Gier,  Sehnsucht,  Wunsch';
unsicher  wegen  des  Anlautes  anord.  ged  n.  (*gadia-)   ,Sinn,  Charakter," Verlangen,   Lust',   gedlauss   , charakterlos'   vielleicht  =  ahd.  getilös,  mhd.  | getlös  ,zügellos,  mutwillig';
man  beachte  die  übereinstimmende  Gruppierung  d^eaaaad^ai  ;  Ttod^sw  = ir.  gess-am  (*guhedh-s-o-mos)  :  guidiu  (*g'^liodh-eiö).
WP.  I  673,  Trautmann  84£.,  Endzelin  Lett.  Gr.  577.
(*^Mi2ei-0  g'^hgi-,  g^bgi-d- :  g^hid-  ,hell,  leuchtend';  g^hoi-d-ro-s  ds.
Gr.  (patÖQÖg  ,klar,  hellglänzend,  leuchtend;  heiter,  vergnügt'  (=  lit. giedras),  woneben  cpaidi-  im  cpaidL(j,og  ,glänzend,  stattlich';  q)aLÖg  ,schum- merig,  dämmerig,  bräunlich,  grau'  (Gdf.  *(p(xL-J^ög  oder  -oög)'^  cparAÖg' XafiTtQÖg  Hes. ;
lit.    giedrasj    gaidrüs    ,heiter,    klar'    (davon    giedrä,    gaidrä   f.    ,schönes Wetter'),  lett.  dziedrs  ,azurblau',  ablautend  dzidrums  ,Klarheit';  lit.  gaisas  ■- i^g^hdid-so-s),  gaisa  , Lichtschein  am  Himmel',  lett.  gäiss  m.  ,Luft,  Wetter', gaiss  (*gaisus)   ,klar',   gäisma   f.  ,Licht',   lit.   gaXsras   m.   ,Lichtschein   am
489
Uimmel,    Feuersbrunst;    Zorn^,    gaXzdras    m.    , Lichtschein    am    Himmel'; ■tvohl  auch  apr.  gaylis  ,weiß*. WP.  I  665,  Trautmann  75.
g^beio-  :  g^hl-  , Ader,  Sehne,  Band' ;  gHbi-slo-  ds. Cymr.  gi-au  PL  ,Nerven,  Sehnen';
lit.  gijä  , Faden  im  Aufzug  eines  Gewebes',  lett.  dzija  , Faden,  PL Garn';
aksL  H-ca  , Sehne',  russ.  diaL  Mca  ,Kammgarn',  skr.  zica  ,Faden,  Draht, Schnur,  Saite';  die  bsl7-Formen  könnten  auch  zu  gVin9-  gehören.
g'ihislO'',
Arm.  jil  , Sehne,  Schnur';
lat.  fllum  , Faden';
lit.  gysla  ,Ader,  Sehne,  Blattrippe',  lett.  dztsla^  dztksla  ,Ader'  (die Nasalierung  in  zemait.  ginsla  ist  sekundär),  apr.  pettegislo  , Rückenader' ; aber  aksl.  züa^  russ.  i2?a,  skr.  zila  usw.  ,Ader,  Sehne'  sind  Neubildun- gen zu  zi-ca,  s.  oben.
WP.  I  670,  694,  WH.  I  497  f.,  Trautmann  87,  90.
g^bel-
===LEAF 147===
  ,wollen'.
Gr.  d-slü)j  i-&€lo)  (zum  Präfix  s.  W-,  ö-Part.)  ,will,  wünsche',  ablautend (pakiC^ei '  d'eXei  Hes. ;  ijiL^dg)sXog  ,heftig' ;
anord.  gildra  f. ;  gildri  n.  , Falle',  gilja  ,verlocken',  aschwed.  gicel- skaper  , Unzucht';
aksL  zeleti,  ^elatij  iter.  russ.-ksl.  zalati  ,wünschen',  aksl.  zelja  , Wunsch, Sehnsucht'  (auch  ,trauern'  und  ,Trauer'  durch  Anlehnung  an  ^aU  , Schmerz' von  *^"eZ-  ,stechen').
WP.  I  692.
gbuel-  ,sich  krümmen,  von  der  geraden  Richtung  abbiegen  (auch  geistig und  sittlich)  u.  dgl.';  ghuelo-s  ,gekrümmt'.
Ai.  hvdrate  ,biegt  von  der  geraden  Richtung  ab,  macht  krumme  Wege', hvdlati  ,gerät  auf  Abwege,  strauchelt,  irrt',  juhuränd-h  , mißglückend', vihriUa-h  , schadhaft,  krank',  hrunäti  ,geht  irre',  Partiz.  hrutd-y  geneuert hvftd-',  hürchati  ,geht  schief,  gleitet,  schwankt,  fällt';  hvdras-  n.  ,Krüm- mung',  hvard-  m.  , Schlange',  vihrüt-  f.  ,Art  Schlange  oder  Wurm' ;
av.  zbardmna-  ,krumm  gehend',  zharad-a-  n.  ,Fuß  daevischer  Wesen', zharah-  n.  ,Hügel',   zürah-  n.  ,Unrecht,  Trug',   npers.  zur  , falsch;  Lüge';
gr.  q)aXl7tT€L'  uwqaivei  Hes.,  (paXög  , stammelnd,  töricht'  Hes.  und  wahr- scheinlich (pdXoQ  m.  ,hornartiger  Vorsprung  am  Helm',  vermutlich  g)oAxdg, Beiwort  des  Thersites  B.  217,  etwa  , krummbeinig' ;   vielleicht  auch  dTto-
L
490  •
(fcblLog   ,trügerisch'    (ö-stufig),    q)fjlog    ^betrügerisch^,    q)rjXi^T7jg    ;Betrüger',  v? cprjXötJ  (dor.  cpaXöcü)  betrüge';  ^^';
lat.  fallö,  -ere  ^täuschen,  betrügen;  unwirksam  machen;  sich  entziehen-  ^'-^ unbemerkt  bleiben'  (,*krumme  Wege  machen;   ausbiegen';    *ghujnö,  vgl.  - ai.  hrunäti)'j  '4-  -
lit.  nuozvelnüs  ,abschüssig'j  zvalüs  ^geschickt;  flink,  behend'  (,*sich leicht  biegend');  ablaut.  i^vünas  ,schräg,  schief  {*g'hul-),  pa^il-ti,  -au ,sich  neigen',  ir^/^wo^t  , schaukeln,  schwanken';  prazulnas  (*ghul-)  ,schräge, schief,  paMnus  ds. ;  atiülas,  -us  ,schroff,  hart,  unhöflich,  unbarmherzig' u.  dgl. ;
lett.  zveVu,  zveVu,  zvelt  ,wälzen,  fortbewegen,  umwerfen ;  schlagen',  refl. ,sich  schwerfällig  fortbewegen,  sich  wälzen,  umfallen',  zvalstities  ,wanken, schwanken',  zvatns  ,sch wankend';
aksl.  z^l^  ,böse,  schlimm',  skr.  zäo  (f.  zlä)^  russ.  zoi  (f.  zia)  ds. ;
vielleicht  *ghu-el-  aus  einem  gheu-  ,schief'  erweitert;  vgl.  ^ghu-er-  in lit,  ziirU  ,eine  Rankenpflanze'  (*g^ur-lo-),  gv.  ^egfiog  m.  ,Feigenbohne^ (*guher-mo-).
WP.  I  643 f.,  WH.  I  448,   Trautmann  372  f.
•'^^ ' ghuelg-  ,anblicken'?  ^-^'<
Gr.  d-sXyo}   ,bezaubere,   umschmeichle'   (unwahrscheinlich   oben  S.  247);
lit.  ^velgiüj  zvelgti  ^anblicken',  Iterat.  zvalgaUj  zvalgyti  und  zvilgis  m. , Blick',  ^vUgiu,  ^vilgUi  ,kurz  hinblicken'.
WP.  I  644,  Trautmann  374,  Schwyzer  Gr.  Gr.  I  302.  .v4.^-
^hemh-  , lustig  springen,  hüpfen'??  "^
Gr.  äd-sixßovaa '  äy.oXaaraivovaa  (,ausgelassen')  Hes. ;
mhd.  gampen,  gumpen  , springen',  gampel,  gumpel  , lustiges  mutwilliges Springen,  PossenspieF,  gümpelj  nhd.  Gimpel]  mit  oberdeutscher  Lautver- schiebung mhd.  gampf  m.  
===LEAF 148===
,das  Schwanken';  norw.  dial.  gimpa  , wippen, schaukeln',  gamp  m.  ,großer  schwerfälliger  Kerl,  plumpes  Pferd'.
Eine  kürzere  Wzf.  guhem-  vielleicht  in  aisl.  gaman  n.  ,Freude,  Lustig- keit, Wollust',  ahd.  gaman  n.  ds.,  usw.  "       ^
WP.  I  678  f.  ^^
ghuen-    ,tönen',    ghupno-s    ,Ton':    Erweiterung    von    ghau-,     s.   Persson Beitr.  191. kxm.  jain  (ghuon-ii-),  i-St.  , Stimme'  (mit  t- Epenthese) ; alb.  tosk.  Z6  , Stimme',  geg.  zd  (<  *ghuono-s)'j
russ.-ksl.  zvbnjuj  zvhnki  ,klingen,  tönen',  russ.  zvenith,  acech.  zvnieti, öech.  zniti,  altpoln.  tozniec  ds.,  ablaut.  aksl.  zvom  ,Ton',  sl.  zvqn  , Glocke',
491
hnlg'  zv^n^  ,Klang,  Schall',  zvznecb  , Glocke',  skr.  zvono,  russ.  cech.  zvon, poln.  dzwon  , Schall,  Glocke^
Baltoslav.  Wurzelerweiterung  gbueng-:
lit.  zvengiu,  zvengti  ^wiehern',  su-zvihgu,  -zvingti  ,in  Wiehern  ausbrechen^, zvangüs  ,laut,  schallend',  svdngu,  zvangeti  ,rasseln,  klingen,  klirren',  lett. zviegt  , wiehern';
aksl.  zv^go  ,verkünde',  russ.-ksl.  zvjagu  ,singe,  schwatze',  russ.  dial. zvjagü,  zvjach  ,bellen'.
Slav.  Wurzelerweiterung  gbuenk-:
aksl.  zv^kz  m.  ,Klang',  zveknqti  , tönen',  zvecati  , rufen',  skr.  zvek  ,Klang'^ poln.  zwi^k,  diwiek  , Klang,  Schall';  mit  Ablaut  aksl.  zvok^  ,Klang',  russ. zvuk,  cech.  zvuk  ,Ton,  Laut,  Schall';
Slav.  Wurzelerweiterung  gbuent-:
bulg.  zv^ntja  ,schallen,  klingen'.
WP.  I  642,  Trautmann  374.
f.  g^hen-  ,schwellen,  strotzen.  Fülle';  g^hono-s  ,üppig,  reichlich'.
Ai.  a-hand'  , schwellend,  strotzend,  üppig',  ghand-  , dicht,  dick',  m. ,kompakte  Masse';
npers.  ä-gandan  , anfüllen',  äganis  ,voll';
arm.  yogn  ,multum'  (Präp.  i  +  *o-g^hon-  oder  *o-g^hno-,  im  Präfix  o- dem  ar.  ä-  nächststehend) ;
gr.  sid-svi^g  ,reichlich,  in  Fülle',  Hes.,  edd^svsoj  ,gedeihe',  eid-iveia  , Fülle, blühender  Zustand',  dehnstufig  ion.  svdr]vi^g  , reichlich,  in  Fülle',  ion.  att. sid-rivso)  ,gedeihe,  bin  in  Blüte  und  Kraft',  svd-rjvla  f.  ,Fülle';  o-stufig IloKvcpövrrjg  =  noXvKTT^TTjg;  KXsocpövrrjg^  usw.,  red. -stufig  q)aväv '  d^eksiv Hes.,  wohl  eigentlich  ,geil  sein' ;
lit.  ganä  ,genug',  ganeti  ,genügen',  gandeti  ,genug  haben',  lett.  gana ,genug';
aksl.  gonejetb,  goneti  ,genügen',  Denomin.  von  "^gona  =  lit.  ganä]
ob  hierher  gr.  ^cpavog,  lücpvog  n.  ,reichlicher  Vorrat,  Reichtum',  äcpvsiog , begütert'  {cp  und  der  Vokalvorschlag  aus  der  vokallosen  Form  {a)(fv- oder  *sm-g^h(e)n-'>),  auch  Ttao-divog  , Jungfrau'  (leibliche  Fülle?)?
WP.  I  679,  WH.  I  479 ;  Trautmann  77  f.
2.g^hen-(p)-  ,schlagen'.
Nominalbildungen:  g^höno-s  , Schlagen',  g^hn-to-s  ^geschlagen', g^hn-ti-s  und  g^hn-tia  (?)  , Schlagen',  g"hen-tel-
===LEAF 149===
  .Schläger',  g'ihen-tuo-s ,occidendus'.
Ai.  hdn-ti  (jünger  thematisch  hanati)  , schlägt,  trifft,  erschlägt,  tötet', 3.  PL  ghn-dnti,  Im^.  ja- hi,  Opt.  Jian-yät,  ghnlta,  VerL  jaghdna]  jaghanväs.
492
Gen.  jaghn-us-ah,  Pass.  hanyäte,  Partiz.  hatd-  ^geschlagen,  getötet'  (==  ay.*^ jata-j  gr.  -cpatog),  hdntva-h  ;Zu  schlagen,  zu  töten'  ( :  av.  jq^iva-^  aksl  .^ 0gtva)j  vrtra-hdn-,  Gen.  -ghTi-dh  (=  av.  vdrd^ra-jan-,  Gen.  -y-no)  ,<ien  Wider-  S stand  niederschlagend',  ghand-  ^erschlagend,  m.  Knüttel,  Keule'  (==  g^^  „- ävÖQO-q)6vogj  lett.  gans),  sam-hd-t  ,Schicht',  hati-h  ,das  Schlagen,  Schlag^ ^ Multiplikation'  (:  gr.  ÖLcpaai-og,  av.  -jaüi-,  anord.  gudr,  gunnr),  hatyä  (spät) ,Tötung'  (:  ahd.  gundea,  lit.  dial.  ginciä),  hantdr-  ,wer  einen  schlägt  od( tötet'  (=aksl.  z§teljb)',  von  der  schweren  Basis  ai.  hanitum  (spät!)  und^fÄö^ ,tötend',  m.  ,Schlag,  Tötung,  Vernichtung',  ghätayati  ,tötet';
aiv,jain-ti  (=  ai.  hdnti-)  ,er  schlägt,  trifft,  tötet',  Imp.  Jaidi,  1-  Sg.  Met m'-ywe  ,ich  schlage  nieder',  Opt.  paiti-ynUa  (=  ai.  ghnlta)  ,er  möchte^ kämpfen  um',  Partiz.  jata-  (=  ai.  hatd-,  s.  oben),  jqd-wa-  ,occidendu8'J Partiz.  Perf.  Akt.  jaynvä,  npers.  ajanam  ,ich  erschlug  =  besiegte',  3.  SgJ aja^""^'^  av.  Jana-  ,schlagend',  jantar-  ,der  schlägt,  tötet',  Jan^i-  f.  ^( Schlagen,  Erschlagen',  -jaiti-  (als  2.  Kompos.-Glied)  ,das  Schlagen'  (=  affl Äa^i-);    Vdrd&rajan-    ,den  Widerstand   niederschlagend'  =  ai.  Vrtra-hani^^^
arm.  ^an,  Gen.  gani  {*g^he-n)  ,Schläge,  Prügel',  ganem  ,schlage,  prügle'^ jin  ,Stock'  (*gyihen-),  jnem  ,ich  schlage'  (über  *jinem  aus  ^g^henö  =  hdnai lit.   genilj  aksl.   ieng),   jnjem  ,vernichte,    reinige'    (aus   ^g^heniö  =  ^stVöjS lit.  geniü)]
gr.   -^ftVw    (*gVien-iö  =  arm.  Jnjßm  ,töte',   alb.   gjanj   ,jage',   lit.   genii ,ästle  ab')  ,schlage',  d-evu),  e-d-eiva-,  redupl.  i/rfi^yo)' , tötete',  necparaLi  -<p(xr6g\ in   hom.  dcQr]l-q)arog   (=  ai.  hatd-h),   auch   in  dlcparov  öiq)daLOv  Hes.  d. , doppelt'  (,Mal'  =  ,Schlag',  ebenso:)  ÖL-cpaai-og  (:  ai.  hati-  s.  oben);  q)6vog'^ ,Mord'    (=  russ.   gon),    cpovr]    ds.,    g)ovsvg    , Mörder',    dvdgocfövog    ,Männer mordend'  (s.  auch  Boisacq  unter  q)0iv6g)]
alb.  gjanj  ,jage,  verfolge'  (*guhen{o)]
lat.  defendö,  -ere  , abwehren,  verteidigen',  offendere  ,anstoßen,  beleidigen', infensus  (Partiz.  eines  *infendö)  , feindlich';
air.  gonim  ,verwunde,  töte',  Perf.  1.  Sg.  gegon,  3.  Sg.  geguhi]  guin ,Wunde' ;
anord.  gudr,  gunnr  f.  (=  ai.  hati-),  as.  güdea,  ags.  güp  (*gunpjö  =  ai. hatyä  bis  auf  den  Akzent)  , Kampf,  Schlacht',  ahd.  gund-fano  ,Kriegs- fahne';  anord.  gandr
```


### [2026-09-06T14:54:01.991Z] TOOL RESULT

```
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
=== klein bezoar ctx
bewray,  tr.  v.,  to  reveal,  divulge  ( archaic )  — ME.  bewreien,  bewreyen,  ‘to  reveal’,  fr.  be-  and OE.  wregan,  ‘to  accuse’,  which  is  rel.  to  OS. wrogian,  OFris.  wrogia,  OHG.  ruogen,  MHG. riiegen,  ‘to  accuse’,  G.  riigen,  ‘to  censure’,  Goth, wrohjan,  ‘to  accuse’,  ON.  rcegja,  ‘to  slander,  de¬ fame’,  Du.  wroegen,  ‘to  prick’  (said  of  con¬ science),  OE.,  OS.  wrdht,  OFris.  wrogie,  MHG. ruoge,  riiege,  Goth,  wrohs,  ‘accusation’,  G.  Riige, ‘censure’,  ON.  rog,  ‘quarrel,  slander’, bey,  n.,  1)  governor  of  a  district  in  Turkey;  2)  a Turkish  title  of  honor.  —  Osmanli  equivalent of  Turk.  beg.  Cp.  beg,  ‘bey’,  begum, beylic,  beylik,  n.  —  Turk.,  formed  fr.  bey  and -lik,  a  suff.  expressing  quality.  Cp.  pashalik. beyond,  adv.  and  prep.  —  ME.  biyeonde,  biyonde, fr.  OE.  begeondan,  ‘beyond’,  fr.  be-  and  geond, ‘yond,  yonder’.  See  yon,  yond,  yonder. Derivative:  beyond,  n.
bezant,  n.,  a  gold  coin.  —  Orig.  ‘coin  of  Byzan¬ tium’,  fr.  OF.  besan,  besant,  fr.  L.  byzantius. short  for  Byzantius  nummus,  ‘Byzantine  coin’. See  Byzantine.
bezel,  n.,  a  sloping  edge.  —  OF.  bezel  (F.  biseau ), ‘a  sloping  edge,  bevel,  prob.  orig.  meaning  "a stone  with  two  angles’;  fr.  VL.  *bis-alus,  ‘hav¬ ing  two  angles’,  fr.  L.  bis,  ‘twice’,  and  ala,  ‘wing, side’.  See  bis-  and  ala.
bezesteen,  n.,  a  bazaar.  —  Pers.  bezestan,  formed fr.  bez  (whence  Arab,  bazz),  ‘flax,  linen  clothes’, and  -stan,  a  suff.  denoting  place,  which  is  rel, to  Avestic  stana-  (in  compounds),  ‘place’,  lit. ‘a  place  where  to  stand’.  See  Hindustani, bezetta,  bezette,  n.,  a  dyeing  material  made  by dipping  linen  rags  into  certain  coloring  matters. —  It.  pezzetta,  dimin.  of  pezza,  ‘piece  of  cloth’, a  word  of  Gaulish  origin.  See  piece  and  -ette. bezique,  n.,  a  card  game.  —  F.  besigue,  of  un¬ known  origin.
bezoar,  n.,  orig.  a  term  for  antidote-,  later  used for  concoctions  found  in  the  stomach  or  in¬ testines  of  certain  animals  and  thought  to  have antidotal  properties.  —  F.  bezoard,  fr.  Sp.  be¬ zoar  (cp.  Port,  bezuar),  fr.  Arab,  badizdhr,  often shortened  into  bazahr  (see  Freytag,  Lexicon
I
Arabico-Latinum,  I,  79a  and  b),  ult.  fr.  Pers. badzahr,  padzahr,  ‘counterpoison,  bezoar  stone’, lit.  ‘protecting  (against)  poison’,  fr.  pad,  ‘pro¬ tecting,  guarding;  guardian,  lord,  master’,  and zahr,  ‘poison’.  For  the  first  element  see  padi- shah.  The  second  element  is  rel.  to  Pers.  zehre, ‘gall,  bile’,  Pahlavi  zahr,  ‘poison’,  Avestic  zara-, ‘gall,  bile’,  and  cogn.  with  Gk.  yoXf],  ‘gall,  bile’. See  choler.
bezonian,  n.,  knave,  rascal.  —  Formed  with  suff. -ian,  fr.  It.  bisogno,  ‘want,  need’,  which  is  rel.  to F.  besogne,  ‘work,  task,  job’,  besoin,  ‘want, need’,  OProveng.  bezonh,  ‘want’,  bezonha,  ‘want, work,  task’.  These  words  prob.  derive  fr.  Fran¬ kish  *bisunnia,  which  is  formed  fr.  hi-,  ‘by’,  be¬ side’  (see  be-),  and  *sunnia  (rel.  to  OS.  sunned), ‘care’,  whence  Olt.  sogna,  F.  soin,  OProveng. sonh,  sonha,  ‘care’.  See  Dauzat,  DELF.,  p.85 s.v.  besogne.
bezzle,  tr.  v.,  to  plunder,  consume;  intr.  v.,  to revel  (dial.  English).  — -  OF.  besillier,  ‘to  tor¬ ment’,  freq.  of  beser,  ‘to  be  scared,  be  startled’ (said  of  cows  stung  by  gadflies),  fr.  OHG.  615- 3an,  ‘to  bite,  sting’;  see  bite  and  cp.  embezzle. See  R.  Grandsaignes  d'Hauterive,  Dictionnaire d’ancien  frangais,  Paris,  1947,  p.62  s.v.  besillier.
bezzo,  n.,  name  of  a  small  Venetian  silver  coin.  — It.,  fr.  G.  Batz,  Batzen,  name  of  a  small  Swiss coin,  orig.  meaning  ‘a  thick  piece’,  and  rel.  to the  verb  batzen,  ‘to  be  sticky,  be  adhesive’.  See batz.
Bhaga,  n.,  a  god  of  wealth  (Vedic  mythol.)  — OI.  Bhagah,  lit.  ‘allotter,  distributer,  master, lord’,  fr.  bhdjati,  ‘assigns,  allots,  apportions,  en¬ joys,  loves’,  rel.  to  Avestic  haya,  OPers.  baga, ‘master,  lord,  god’.  See  baksheesh  and  cp.  next word.  Cp.  also  pagoda.
Bhagavad-Gita,  the  celebrated  dialogue  between Krishna  and  Arjuna  inserted  in  the  Maha- bharata.  —  OI.  Bhdgavadgita,  ‘the  song  of  the Sublime  One’,  compounded  of  Bhaga,  suff. -vant  (corresponding  to  Gk.  -Fevr-,  -evt-)  and gi-td,  ‘song’,  prop.  fern.  pp.  of  gdyale,  ‘sings, calls',  from  the  I.-E.  imitative  base  *ga-,  *gi-, whence  also  Avestic  ga&a,  Pers.  gah,  ‘song’, Lith.  giedoti,  'to  sing’,  giesme,  ‘song’,  Lett. diesma,  ‘song’.
bhang,  n.,  the  Indian  hemp.  —  Hind,  bhang,  fr. OI.  bhahga,  ‘hemp’,  which  is  cogn.  with  Russ. penika  (whence  Pol.  pienka ),  ‘hemp’.
bhat,  n.,  1)  a  bard;  2)  a  title  of  respect.  —  Hind. bhat,  fr.  OI.  bhat  (ah,  a  title,  prob.  rel.  to  bhart- rih,  ‘bearer,  supporter,  master’,  from  the  stem of  bharati,  ‘he  bears’,  fr.  I.-E.  base  *bher-,  ‘to bear,  carry’.  See  bear,  to  carry’.
bhava,  n.,  becoming,  birth,  origin,  world,  health. —  OI.  bhavah,  rel.  to  bhavitram,  ‘world",  hhitnuh , bhdman-,  ‘earth,  world',  from  the  stem  of  hhd- vati,  ‘becomes,  happens’,  fr.  I.-E.  base  *bheu-, *bhu-,  ‘to  be,  exist’,  whence  also  Gk.  jeiv,  ‘to make  to  grow’,  g>ucTi<;,  ‘nature’,  L.  fid,  ‘I  be¬ come’,  fui,  ‘I  have  been’,  OE.  beon,  ‘to  be’.  See
be  and  words  there  referred  to  and  cp.  esp.
Bhumi  Devi,  bhut.
```


## [2026-09-06T14:54:14.804Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"gunthjo\\|gunth\\|gundjo\\|Gunnhild\\|gundea\" AHD_watkins1985.txt KLN_1966.txt SKT.txt | head -20",
 "description": "Grep for Germanic gunthjo"
}
```


### [2026-09-06T14:54:14.868Z] TOOL RESULT

```
AHD_watkins1985.txt:362:DECENT. 2. Suffixed (causative) o-grade form *dok-eye- in: a. Latin docére, to teach (< “to cause to accept”): DOCENT, DOCILE, DOCTOR, DOCTRINE, DOCUMENT; b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX. 3. Suf- fixed form *dek-es- in: a. Latin decus, grace, ornament: (DECOR), DECORATE; b. Latin decor, seemliness, elegance, beauty: DECOROUS. 4. Suffixed form *dek-no- in Latin dignus, worthy, deserving, fitting: DAINTY, DEIGN, DIG- NITY; CONDIGN, DIGNIFY, DISDAIN, INDIGN, INDIGNANT, INDIGNATION. 5. Reduplicated form *di-dk-ske- in Latin discere, to learn: DISCIPLE, (DISCIPLINE). 6. Greek dekh- esthai, to accept: PANDECT, SYNECDOCHE. 7. Greek dok- os, beam, support: DIPLODOCUS. [Pok. 1. dek- 189.] dek-2. Referring to such things as a fringe, lock of hair, horsetail. 1. Suffixed o-grade form *dok-lo- in Germanic *taglaz in Old English teg(e)l, tail: TAIL!. 2. Perhaps Germanic *tag- in: a. Swedish tagg, prickle, akin to the Scandinavian source of Middle English tagge, pendent piece: TAG!; b. Middle High German zacke, nail (> German Zacken, point): SHAKO; Cc. Old French tache, fastening, nail: TACHE, TACK!. [Pok. 2. dek- 191.] dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN; b. Old Norse an, ten (see oktd(u)). 2. Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECI- MAL, OCTODECIMO, SEXTODECIMO. 3. Irregular Latin distributive dani, by tens, ten each (formed by analogy with néni, nine each): (DENARIUS), DENARY, (DENIER?). 4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON. II. Extended form *“dekmt- in Germanic *-tig in Old English -tg, ten (see dwo-). III. Ordinal number *dekmto- in Germanic *te- guntha- in Old English teogotha, téotha, tenth: TENTH, (TITHE). IV. Suffixed zero-grade form *-dkm-ta, reduced to -kmtd, and lengthened o-grade form *-dk6m-ta, re- duced to *-kontd. 1. Latin -gintd, ten times: NONAGE- NARIAN, OCTOGENARIAN, SEPTUAGINT, SEXAGENARY. 2. Greek *-konta, ten times: PENTECOST. V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom. 1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED. 2. Germanic *thiis-hundi, “swollen hundred,” thousand (see teue-). 3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CEN- TESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CEN- TURY; CENTENNIAL, PER CENT, QUATROCENTO, SEICENTO, (SEN!), (SEN2), (SENITI), SEXCENTENARY, TRE- CENTO. 4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-'): HECATOMB, HECTO-. 5. Avestan satam, hundred: SATEM. See also compound root wikmti. [Pok. dekm 191.] deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side: DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. Compare ner-'. [In Pok. 1. dek- 189.] del-'. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1.Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LoNG!; b. Old High German lang (> German Jang), long: LANGLAUF; C. Old English denominative langian, to grow longer, yearn for: LONG?; d. Latin compound Lon- gobardus, Langobardus (with Germanic ethnic name *Bardi): LOMBARD. 2. Germanic abstract noun */lang- ithé in: a. Old English lengthu, length: LENGTH; b. West Germanic */angitinaz, lengthening of day, in Old English lengten, lencten, spring, Lent: Lent; ¢. Dutch lenghe, linghe, “long one,” akin to the Low German source of Middle English lenge, ling, ling: LING}. 3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PUR-
AHD_watkins1985.txt:1195:yeu-. Vital force, youthful vigor. Earliest form *ayeu-; variant of aiw-. Suffixed zero-grade form *yuwen- (< *yu-sen-), “possessing youthful vigor,” young. 1. Further suffixed form *yuwn-ti- in Germanic *jugunthi-, *jugun- tha- in Old English geoguth, youth: YOUTH. 2. Further suffixed form *yuwn-ko- in: a. Germanic *juwungaz becoming *jungaz in (i) Old English geong, young: YOUNG (ii) Old High German jung, young: JUNKER (iii) compound *jung-fréw6-, young lady (see per’); b. Old Irish 6ac, Irish Gaelic 6g, in oglach, soldier: GALLOW- GLASS. 3. Latin iuvenis, young: JUNIOR, JUVENILE; JUVE- NOCRACY, REJUVENATE. [Pok. 3. ieu- 510.]
```


## [2026-09-06T14:54:16.072Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=150 && NR<=151 {print \"===LEAF \" NR-1 \"===\"; print}' POK_02.txt | head -60",
 "description": "Pokorny leaf 149-150"
}
```


### [2026-09-06T14:54:17.704Z] TOOL RESULT

```
===LEAF 149===
  .Schläger',  g'ihen-tuo-s ,occidendus'.
Ai.  hdn-ti  (jünger  thematisch  hanati)  , schlägt,  trifft,  erschlägt,  tötet', 3.  PL  ghn-dnti,  Im^.  ja- hi,  Opt.  Jian-yät,  ghnlta,  VerL  jaghdna]  jaghanväs.
492
Gen.  jaghn-us-ah,  Pass.  hanyäte,  Partiz.  hatd-  ^geschlagen,  getötet'  (==  ay.*^ jata-j  gr.  -cpatog),  hdntva-h  ;Zu  schlagen,  zu  töten'  ( :  av.  jq^iva-^  aksl  .^ 0gtva)j  vrtra-hdn-,  Gen.  -ghTi-dh  (=  av.  vdrd^ra-jan-,  Gen.  -y-no)  ,<ien  Wider-  S stand  niederschlagend',  ghand-  ^erschlagend,  m.  Knüttel,  Keule'  (==  g^^  „- ävÖQO-q)6vogj  lett.  gans),  sam-hd-t  ,Schicht',  hati-h  ,das  Schlagen,  Schlag^ ^ Multiplikation'  (:  gr.  ÖLcpaai-og,  av.  -jaüi-,  anord.  gudr,  gunnr),  hatyä  (spät) ,Tötung'  (:  ahd.  gundea,  lit.  dial.  ginciä),  hantdr-  ,wer  einen  schlägt  od( tötet'  (=aksl.  z§teljb)',  von  der  schweren  Basis  ai.  hanitum  (spät!)  und^fÄö^ ,tötend',  m.  ,Schlag,  Tötung,  Vernichtung',  ghätayati  ,tötet';
aiv,jain-ti  (=  ai.  hdnti-)  ,er  schlägt,  trifft,  tötet',  Imp.  Jaidi,  1-  Sg.  Met m'-ywe  ,ich  schlage  nieder',  Opt.  paiti-ynUa  (=  ai.  ghnlta)  ,er  möchte^ kämpfen  um',  Partiz.  jata-  (=  ai.  hatd-,  s.  oben),  jqd-wa-  ,occidendu8'J Partiz.  Perf.  Akt.  jaynvä,  npers.  ajanam  ,ich  erschlug  =  besiegte',  3.  SgJ aja^""^'^  av.  Jana-  ,schlagend',  jantar-  ,der  schlägt,  tötet',  Jan^i-  f.  ^( Schlagen,  Erschlagen',  -jaiti-  (als  2.  Kompos.-Glied)  ,das  Schlagen'  (=  affl Äa^i-);    Vdrd&rajan-    ,den  Widerstand   niederschlagend'  =  ai.  Vrtra-hani^^^
arm.  ^an,  Gen.  gani  {*g^he-n)  ,Schläge,  Prügel',  ganem  ,schlage,  prügle'^ jin  ,Stock'  (*gyihen-),  jnem  ,ich  schlage'  (über  *jinem  aus  ^g^henö  =  hdnai lit.   genilj  aksl.   ieng),   jnjem  ,vernichte,    reinige'    (aus   ^g^heniö  =  ^stVöjS lit.  geniü)]
gr.   -^ftVw    (*gVien-iö  =  arm.  Jnjßm  ,töte',   alb.   gjanj   ,jage',   lit.   genii ,ästle  ab')  ,schlage',  d-evu),  e-d-eiva-,  redupl.  i/rfi^yo)' , tötete',  necparaLi  -<p(xr6g\ in   hom.  dcQr]l-q)arog   (=  ai.  hatd-h),   auch   in  dlcparov  öiq)daLOv  Hes.  d. , doppelt'  (,Mal'  =  ,Schlag',  ebenso:)  ÖL-cpaai-og  (:  ai.  hati-  s.  oben);  q)6vog'^ ,Mord'    (=  russ.   gon),    cpovr]    ds.,    g)ovsvg    , Mörder',    dvdgocfövog    ,Männer mordend'  (s.  auch  Boisacq  unter  q)0iv6g)]
alb.  gjanj  ,jage,  verfolge'  (*guhen{o)]
lat.  defendö,  -ere  , abwehren,  verteidigen',  offendere  ,anstoßen,  beleidigen', infensus  (Partiz.  eines  *infendö)  , feindlich';
air.  gonim  ,verwunde,  töte',  Perf.  1.  Sg.  gegon,  3.  Sg.  geguhi]  guin ,Wunde' ;
anord.  gudr,  gunnr  f.  (=  ai.  hati-),  as.  güdea,  ags.  güp  (*gunpjö  =  ai. hatyä  bis  auf  den  Akzent)  , Kampf,  Schlacht',  ahd.  gund-fano  ,Kriegs- fahne';  anord.  gandr  
===LEAF 150===
, Stock',  Schweiz,  gunten  ,eine  Art  Keil';  norw.  dial. gana  ,die  Äste  an  Bäumen  abhauen'  wie  lit.  geneti]
lit.  genü  (=  aksl.  zeng,  ai.  hdnati,  arm.  jnem)  giftti  ,treibe  (Vieh  auf die  Weide)',  lett.  dzenu-,  dzit  ds.,  schwere  Basis:  geniü  (==  d-eivo))  gene-ti ,abästeln'  und  ginü,  ginti  ,wehren,  schützen'  (ginti :  gmti,  giütas :  gintas =  ai..  hatd :  ghätd-) ;  zu  genü  Iterat.  ganyti  ,Vieh  (treiben  =)  hüten, weiden';  lit.  gänas,  let.  gans  ,Hirt'  (=  ai.  ghand-),  gani  m.  PI.  ,Weide', dehnstufig   lit.   naktl-gonis   m.   ,Nachtschwärmer' ;    lit.   genys,    lett.   dzenis
493
Specht^,  lit.  dial.  ginöiä  (=  ai.  hatyä),  gificas  , Streit'^  giilklas  m.  , Waffe' {*qintlaSj  vgl.  aksl.  ^lo  aus  *gindla')j  üganüs  ^heilbringend'  (lit.  gdinioti ist  Iterativum  zu  ginti ;  lett.  dzenis  ,das  in  der  Gabel  der  Pflugschar  einge- klemmte Holz',  dzenulis  , Stachel'  (vgl.  zur  Bed.  unten  aksl.  ^^lo  , Stachel') ;
aksl.  zeng,  g^nati  ^treiben'  (wie  lit.  genü),  Iter.  gonjq,  goniti  ^treiben, iao'en',  wovon  wieder  poganjati  ^verfolgen' ;  russ.  usw.  gon  ^Treiben,  Jagd' (=s  q)6vog),  cech.  uhona  , Verletzung,  Schaden',  serb.  prijegon  ,Kampf' (dazu  vielleicht  klr.  honöba  ,Belästigung,  Plage',  sloven.  gonöba  , Schaden, Verderben',  ugonoha  , Vernichtung,  Untergang');
aksl.  ^hnjg,  S^ti  (serb.  zeti,  also  schwere  Basis)  ,ernten',  z§tva  (serb. Btva)  f.  ,Ernte'  ( :  ai.  hdntva-) ;  auch  zdo  (*z§dlo)  n.  ,StacheP,  poln.  zqdio ds.,  russ.  zäh  , Stachel,  Schneide  eines  Messers,  einer  Axt' ;  slav.  *gen-tel- m.  , Schnitter'  in  aksl.  ^eteljh  (=  ai.  han-tdr  ,wer  schlägt,  tötet');
hitt.  ku-en-zi  , tötet'  (=  ai.  hdnti),  3.  PI.  ku-na-an-zi  (kunanzi) ;  vgl.  ai. ghndnti  (*g1thn-enti).
WP.  I  679  ff.,  WH.  I  332  f.,  Trautmann  85  f.
gbuer-  , wildes  Tier'.
Gr.  d^T^Q,  -dg,  m.  spät  f.  (^fJQsg,  &rjQCüv  =  ostlit.  ^veres,  zvery,,  Schwyzer
Gr.  Gr.  I  424),  lesb.  gpij^,  hom.  OfjQSQj  thess.  qjeig  {TiecpeLQ&y.orveg  =  xeS^r]-
gaycöreg,  OiXöcpsiQog)  ,Tier'; lat.  ferus,  -a,  -um  ,wild,  wildwachsend,  -lebend'  {*ghuero-s)\ mit  Überführung  in  die  z-Deklination  (nach  dem  Akk.  Sg.  PL  -t»,  -i  =  m,
J,  -^s)  lit.  Iverxs  m.  f.,  lett.  zmrs  m. ;  apr.  Akk.  PL  siolrins ; aksl.  zv^rb  ,wildes  Tier',  sloven.  zvp,  acech.  zvef  m.  f.,  russ.  zverh; i      Substantiv.  Adjektiv  lit.  Sverienä  f.,  russ.  zverina  , Wildbret',  zu  lat.  carö ferina  ds. WP.  I  642  f.,  WH.  I  487  f.,  Trautmann  374  f.
g^her-    ,heiß,    warm';    Adjektiv    g^hermo-
```


## [2026-09-06T14:54:25.081Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"g\\*hen-[^.]\\{0,900\\}\" AHD_watkins1985.txt | head -5",
 "description": "Extract AHD gwhen entry"
}
```


### [2026-09-06T14:54:27.111Z] TOOL RESULT

```
g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
```


## [2026-09-06T14:54:30.380Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Gunnhildr\\|GUN\\b\\|OFFEND\\|DEFEND\" AHD_watkins1985.txt | head -10",
 "description": "Find AHD gun entry"
}
```


### [2026-09-06T14:54:30.430Z] TOOL RESULT

```
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1572:GUN gWhen-1 GURGITATION gWere-4 GURU gWera-2 GUSH gheu- Gust! gheu- GusT2 geus- GUSTO geus-
1962:OFFEND g¥hen-! OFFENSE gWhen-1 OFFER bher-1 OFFICE dhé-1 OFFICINAL dhé-1, op-1 OFT upo
```


## [2026-09-06T14:54:40.946Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb && ls site/pages/215.jpg 2>/dev/null; pdftoppm -f 215 -l 215 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg215 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render page 215"
}
```


### [2026-09-06T14:54:42.387Z] TOOL RESULT

```
Exit code 1
I/O Error: Couldn't open file 'EtymologicalDictionary-persian-english.pdf': No such file or directory.
```


## [2026-09-06T14:54:44.663Z] TOOL CALL #19: Bash

```json
{
 "command": "ls *.pdf; ls site/pages/ 2>/dev/null | head -3",
 "description": "Locate the PDF"
}
```


### [2026-09-06T14:54:44.714Z] TOOL RESULT

```
EtymologicalDictionary-persian-english.pdf
100.jpg
101.jpg
102.jpg
```


## [2026-09-06T14:54:49.418Z] TOOL CALL #20: Bash

```json
{
 "command": "SP=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 215 -l 215 -r 220 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf $SP/pg215 && ls -la $SP",
 "description": "Render page 215 to PNG"
}
```


### [2026-09-06T14:54:52.431Z] TOOL RESULT

```
total 408
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 10:54 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    264 Sep  6 10:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
```


## [2026-09-06T14:54:54.665Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg215.png"
}
```


### [2026-09-06T14:54:55.308Z] TOOL RESULT

```

```


## [2026-09-06T14:54:55.303Z] INPUT

[Image: original 1870x2420, displayed at 1545x2000. Multiply coordinates by 1.21 to map to original image.]


## [2026-09-06T14:55:13.391Z] AGENT

The printed page confirms the extraction. Now the Iranian sources.


## [2026-09-06T14:55:16.892Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT vārəγna\"; grep -n \"vārəγna\\|varonna\\|vārəngan\\|vJrJgna\\|vär9gna\\|varegna\" BRT.txt | head -10\necho \"=== BRT jan-\"; grep -n \"^jan-\\|^ jan-\\|jan- \\[\" BRT.txt | head -10\necho \"=== BRT gaz\"; grep -n \"^gaz\\|gaZ-\\|ga^z\" BRT.txt | head -10",
 "description": "Grep Bartholomae"
}
```


### [2026-09-06T14:55:16.981Z] TOOL RESULT

```
=== BRT vārəγna
=== BRT jan-
=== BRT gaz
```


## [2026-09-06T14:55:17.636Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT jan\"; grep -n \"^jan\\|jan-.*strike\\|avajan\\|vijan\\|patijan\\|nijan\" KNT.txt | head -20",
 "description": "Grep Kent for jan"
}
```


### [2026-09-06T14:55:17.696Z] TOOL RESULT

```
=== KNT jan
769:avdjaniya DB 1.51, 52, perhaps for avajaniyd; cf. `
2379:(c) Double prefixes are perhaps found in two forms: pait-à- in patiydbaram DB 1.68, ava-à-in avajaniya DB 1.51, 52; but there are some dubi- ous features even about these, сї. JAOS 62.274-5.
2404:„ рту. *g*hn-dhi, OP jadiy, Skt. jaht; so alko 2d pi, imv. *o*hn-le, OP jata, and 3d sg. imf. mid. *egthn-lo, OP patiy-ajalà| imf. *eg*hen-m, OP ajanam, Skt. áhanam (with antevocalic de- velopment of m, $07.11), whence with the- matic vowel 3d рі. OP -ajana" in avajana* and perhaps the restored subjunctive 3d pl. i-Janá"tty.
2545:janä”tiy, cf. Av. 3d sg. Јалан.
2582:bhdvanti, OP bava"tiy; Skt. dhardyant, OP dáraya. - ; tiy; OP larsa"tiy; (restored) subjunctives with -6., : OP vináfayá^tiy, vijaná"tiy (cf. $222.11). When = attached to an unaccented non-thematic stem, the E -nti was of necessity accented, and took the form pIE -énti: pIE *s-énti ‘they are’, Osc. sent, Gk. * Dor. (enclitic) &ri, Skt. sánti, ОР ha"tiy. It is to - be noted that the OP script does not permit the _. writing of the nasal in the ending ($111).
2916:(b) Volitional uses: affirmative commands bavatiy DNa 43, 45f, vaindiaiy DNb 35; negative commands with mä or matya, draujiyáhy DB 443, wkanàhy DB 471, kunavdtaiy DNb 56, bavdtiy DNb 59. Negative wishes possibly in (restored) vijanātiy, vināðayātiy A?Sa 5, A?Ha 7 (though optative or injunc- tive or imperative forms are equally pos- sible in these passages).
3513:59 mi : dahyàus : Mādaiy : avadasim : avajanam : xSacamsim : adam : adinam : va 60 sna : Auramazdiha : adam : xSayaéiya : abavam : Auramazdà : xsagam : manā : fr
3533:88 m :adumsim : avijanam
3551:S! avajaniyd, ef. Kent, JAOS 62.274. 6 тагал KT, with omission of the d*. 55 patiydeahyaty Jn., KT. % Sika- lya]uvati$ KT. 6% abrieris RI, WB, Jn., KT. 606. {ү Ja., KT, for Rl's eéibeis[e]a; ef. Lex. for lit. on various normalizations and interpretations. ® Ву. MSLP 23.182-3 finds an haplography and would read adiná : adam |: patiyübaram : adam] : kāram. ™ Upadar- mahyà RI., Wb. KIA; Upadara*mahya Opp. Méd., Hüsing, KT, Tm.; U"padara^mahyà HK.
4691:5 nah*ta : uid : M'bra : тат: pdtw : hacá : vispā : дазїй : Ша : imam : tya : akundm : má : vijanátu : mà : vinàttayátiy
4705:A’Ha = Artaxerxes IT, HAMADAN A. 1 Gatiy : Artax&agà : XS : vazraka : XS : XSyanim : XS : DHyünàm : XŠ : ah 2 yaya : BUyà : Dárayavasahy& : XShya : puça : Dérayavasahyd : ArtaxSatra 3 hyà : XShy& : puça : Artaxšaðrahyā : Xšayāršahyā : XShya : puça : XSayar 4 šahyā : Darayavagahya : XShya : puça : Dérayavasahyd : V?Stáspahyà : puça 5 : Haxàmanisiya : imam : apadàna : vašnā : AM : Anah*la : иа : Mitra : adam : akun 6 ат : AM : Anah'ta : uta : Mitra : mam : püluv : ћасӣ : vispd : gaslá : ut Т & : imam : tya : akunà : mà : vijanátiy : mà : vinátayàtuy Notes то А?На: *? ArtazXatrahyá, acc. to Tm. Lex. 54, and not -cahyd. * [hacd : gastá] WB; [utàmaiy : zsagam] Tm.; [ћасӣ : vispé : gasta] Kent, after A°Sd. " akuna for akundm, and ma with following lost verb, as in A'Sa;
5399:jan- vb. ‘strike; smite, defeat (enemy ш. battle); mould (brick)’: Av. Jan- (gan-, Bthl. AW
5408:vi- + jan- ‘shatter’: vijaná"tiy 3d pl. subj. ($208, $222.111, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent).
```


## [2026-09-06T14:55:23.279Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5390,5420p' KNT.txt; echo \"=== leaf number for line 5399\"; awk 'NR<=5399{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before:\", n}' KNT.txt",
 "description": "Kent jan- lexicon entry"
}
```


## [2026-09-06T14:55:23.844Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 1500 BRT.txt; echo; echo \"=== size\"; wc -l BRT.txt",
 "description": "Inspect BRT OCR quality"
}
```


### [2026-09-06T14:55:25.423Z] TOOL RESULT

```
rebel: Elam. şi-iš-ša-an-tak-ma, Akk. -it-ra-an. — | lah-ma, Gk. Tpravraixuns. From ciga-(§9.n1) + | lazma- ‘brave’ ($9.11): ‘Brave-by-Lineage’ (§160,- Ie); the -zm- is Median ($163.II; Jacobsohn, KZ 54.261; Bv. BSLP 31.2.79). For the nasal end-
ing the prior element, see $159.n1. Cicatazma
пет. DB 2.79; 4.20; DBg 1f. Ciçatarmam asm, DB 2.871. Cicalaxmà ism. DB 2.86.
сіла] emphasizing adv. after neg., ‘at all’: , :
Av. cină ‘also, likewise’; perhaps isn. of ci-, cf.. 4 JAOS 58.116-7, 324, and Harl, KZ 63.2 (not ! eità], with Sen 134). DSe 36.
ciyăkara- (§53) adj. ‘how great’; nt. аз sb., ‘how great a thing’: *ciya(n)t-, cf. Skt. kiyat nsn. ‘how much, how many’, + kara- to root kar- ‘make’ ($160.19; Bthl. AiW 597; hardly to kara- ‘time’, cf. hakaram, as taken by MB Gr $293, Hz. ApI 101-3). ciyakaram nsn. (§259) DNa 39; ciyükaram DNb 50; ciyakaram-ca-maiy (written — : -"m*m*eur; $41, $51, $132, $138.I; Lg. 15.178, — | against Hz. ApI 240) DNb 51, 51f. 1
CiSpi- (so Schaeder, SbPAW 1931.641.n4; i Catišpi- acc. to Justi, INB 152, on the evidence of certain spellings in Greek) sb. "Teispes', King of Elam about 610 в.с., ancestor of Cyrus and Darius: Elam. $1-13-рї-1$, АКК. $-4f-pi-i$, Gk. Téergs (S117, 8124.3, §164.V). Стр nsm. (824, §179.IV) DB 1.5°; DBa 8. Cišpãiš gsm. (824, 8179.IV) DB 1.5f; Cišpaiš ($24, S170.IV) AmH 3; DBa 8.
ja*tar- sb. ‘smiter, slayer’: Av. Jantar-, Skt. hantdr-; pIE *g*hen-tor-, agent noun to OP root jan- ($154.11). Jat пзш. ($186.1) DB 4.58, 78.
jad- vb. ‘pray, ask’, with acc. of person and асс. of thing: Av. Jad- (gad-, Bthl. AIW 487), pres. faiya- (§214), Gk. aor. inf. mid. Өёосасдо:, pIE *g*hedh-. — jadiyümiy lst sg. ($226.1) DPd 21; DNa 54; XPh 59; XSc 4.
jan- vb. ‘strike; smite, defeat (enemy ш. battle); mould (brick)’: Av. Jan- (gan-, Bthl. AW
490), Skt. han-, Gk. бере ‘strikes’, dóvos ‘murder’, - |
Lt. dé-fendit ‘wards off’, pIE *g*hen- ($101, $110, 6208); see also jatar-.
јачу (Skt. hánii; 3208, $228.1) DSe 36, 40. ajanam Ist sg. imf. ($110, $122, $208) DB 1.89, 95; 2.69; 4.61; 5.25; XPh 34. аја" imf. (8101, $208) DB 2.26, 36, 41, 46, 55, 61, 87, 98°; 3.7, 18, 39,46,63, 68;.88; 6011) 05634. | ajaniya imf. pass.
LEXICON
(8220) DSf 29, jadiy (Skt. jaht; $101, $122, 8208, 6237.1) 2d sg. шу. DB 2331, 51; 3.15. ја 2d pl. imv. ($208, 5231) DB 2.21, 84; 3.58, 86.
ava- + jan- and ava- + à + jan- ‘smite down, slay’ (apparently ava- in avajata, ара-й- in avàjan- iyà, others ambiguous; cf. §206c, JAOS 62.274): avàjanam 1st sg. imf. ($226.IT) DB 1.57, 59, 73, 83; 2.5; 481; 5.13, 27°. арфа" imf, ($228.IT) DB 1.31 bis; 3.75.  avàjana" За pl. imf. ($208, $232. П) DB 2.13. avájantyü opt. (§206c, $2281, §228.1I) DB 1.51, 52 (858, JAOS 62.274; hardly with Foy, KZ 35.34). avajata nsm. past pte. pass. (8122, §242.1) DB 1.32 (error for avdjata, ace. to Gray AJP 21.13, Bthl. AW 491).
pali- + jan- ‘fight against’: patzyajatà imf. mid. ($140.П1, $208, $235.II) РМа 47.
fra- + jan- ‘cut off’: frájanam lst sg. imf. (§226.11) DB 2.74, 89.
vi- + jan- ‘shatter’: vijaná"tiy 3d pl. subj. ($208, $222.111, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent).
Jav- vb. ‘press forward’: Skt. jū- ‘press for- ward, impel quickly, excite, promote’, pres. jdvate ‘hastens’, caus. javayati. Cf. Ву. BSLP 332.152; Hz. AMI 4.127, 8.37-8, 65-6, ApI 366-7; Wb. МА 41.8320; Bailey, BSOS 7.292-4; Schaeder SbPAW 1935.502; Kent, Lg. 9.43, 231.
abi- + jav- caus. ‘promote, increase, add to’: abiyajüvayam 1st sg. imf. ($215) XPg 9; abijáva- yam (§23.1, $140.IIT) XPf 40.
jtyamna- pte. as adj. ‘growing old’, nt. as sb. ‘end’ ($109, $241): Av. Jyamna-, pte. to root }уй- ‘grow weak’, Skt. jinåti ‘grows old’. jiyamnam asn. DB 2.62.
ji- vb. ‘live’: Av. fait: (gay-, Bthl. AiW 502), Skt. Джай, Lt. vivit, pIE *g*īųeti (§216); see also gaiéd-, jiva-. ajivatam 3d du. imf. ($229) DSf 14; XPf 21. jwà 2d sg. imv. ($2371) DB 4.56, 75.
jiva- ad). ‘living’: Av. fva-, Skt. jivd-, Lt. vivos, pIE *g*iuo-, cf. *g*iuo- in Gk. Blos "life", *g*ig*o- in OEng. cwicu "living, NEng. quick (8101, $114, $150). See also 7й-. Jiva nsm. XPh 48, 54. jva-diy Аза 3 (dubious $22, 555.1; ef. JAOS 51.229, Scheil 21.93, Wb. AfOF 7.45). jivahya gsm. DB 5.19f, 35.
jü- vb., see jav-.
-{а- encl, demonst. pron. ‘this, it’: Av. Skt. ta-, ef. OP tya-. Only -tā apm., referring to patikarā,
185
in avabasa-a DB 4.72 (8133, $196; JAOS 62.272- 3).
{аита- sb. ‘family’ (8149.1): Av. taoxman-, NPers. tuzm, Skt. tokd-m ‘offspring’, tókman- tokma-s ‘young blade of barley’; -zm- became OP -hm- (5103.1, 5118.1), but remained in Med. (Ву. BSLP 31.2.76-9, Gr. $188; wrongly Mt. Gr. §75, Kent JAOS 35.329-31). taumd nsf. DB 1.8; 4.56, 58f, 64, 75, 79; DBa 13. іаитат asf. DB 488. іаитӣуӣ gsf. ($119) DB 1.9, 28f, 45, 49; 2.16, 81; 4.19f, 22; DBa 15; DBe 8; DBg 11f. taumaya absf. DB 1.61f.
tauman- sb. ‘power, strength’: deriv. of root tav- ‘be strong’, with suffix -man- as in Skt. nama ‘name’, Lt. nomen (§122, $155.11). For separa- tion from taumd- ‘family’, see Tm. Lex. 91, and Kent, JAOS 35.329-31. See also tawiyah-. taumā nsn. ($187) DB 4.74, 78; 5.19°, 35. tau- тату (= taumanis-Saiy; §41, §130, $138, $187) ipn. DNb 25f (Lg. 15.171-2, 176; not gen. sg. with Hz. Api 327; hardly loc. sg. with Sen 247; possibly aee. du., ‘two powers lof mind and of body|’, with Pisani, Riv. Stud. Or. 19.88-9).
lauviyah- adj. ‘stronger’: comp. to *tauma-, adj. to tauman- ‘power’; for formation ($48, $122, $156.IIT, $190.1-1), ef. Skt. sthürd- ‘strong’ and comp. sthdviyas-, Av. stūra- and comp. staoyah-, tarma- ‘brave’ and comp. tqsyah-: JAOS 58.324. іашлуй nsm. (§185.1V) DSe 39 (not to pres. pte. tavya-nt-, as taken by Hz. ApI 328).
=== leaf number for line 5399
formfeeds before: 207
```


### [2026-09-06T14:55:25.473Z] TOOL RESULT

```
Google
This  is  a  digital  copy  of  a  book  that  was  prcscrvod  for  gcncrations  on  library  shclvcs  bcforc  it  was  carcfully  scannod  by  Google  as  pari  of  a  projcct
to  make  the  world's  books  discoverablc  online.
It  has  survived  long  enough  for  the  Copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject
to  Copyright  or  whose  legal  Copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books
are  our  gateways  to  the  past,  representing  a  wealth  of  history,  cultuie  and  knowledge  that's  often  difficult  to  discover.
Marks,  notations  and  other  maiginalia  present  in  the  original  volume  will  appear  in  this  flle  -  a  reminder  of  this  book's  long  journcy  from  the
publisher  to  a  library  and  finally  to  you.
Usage  guidelines
Google  is  proud  to  partner  with  libraries  to  digitize  public  domain  materials  and  make  them  widely  accessible.  Public  domain  books  belong  to  the public  and  we  are  merely  their  custodians.  Nevertheless,  this  work  is  expensive,  so  in  order  to  keep  providing  this  resource,  we  have  taken  Steps  to prcvcnt  abuse  by  commercial  parties,  including  placing  lechnical  restrictions  on  automated  querying. We  also  ask  that  you:
+  Make  non-commercial  use  ofthefiles  We  designed  Google  Bo
=== size
30724 BRT.txt
```


## [2026-09-06T14:55:37.170Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"vär.gna\\|varegan\\|vārəg\\|v[aä]r[9əe][gğγn]na\\|vraghna\\|Vərəθraγna\\|v.r.thraghna\" BRT.txt | head\necho \"=== try 'Falke'\"; grep -c \"Falke\" BRT.txt; grep -n \"Falke\" BRT.txt | head -20",
 "description": "Search Bartholomae for varəγna/Falke"
}
```


### [2026-09-06T14:55:37.281Z] TOOL RESULT

```
=== try 'Falke'
1
25787:KompE.  —  VgL  'saina-  EN,  —  mp.  sinmun; np.  (Npü.)  änmur^;  ai.  vgL  lyeni-  m.  'Adler, Falke'  (S  po.  1);  s.  dazu  Hbm.  AGt.  /.  499,
```


## [2026-09-06T14:55:44.508Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ragna\\|raghna\\|rayna\\|ra^na\" BRT.txt | head -10\necho \"=== column 490 area\"; grep -n \"^490\\|  490$\\| 490 \" BRT.txt | head\necho \"=== leaves\"; awk 'BEGIN{RS=\"\\f\"} END{print NR \" leaves\"}' BRT.txt",
 "description": "Probe BRT structure"
}
```


### [2026-09-06T14:55:46.522Z] TOOL RESULT

```
4700:•  j,  amavas't^ma-  Adj,  'der  stärkste, mächtigste,  gewaltigste',  neben  v)rj%ra- rast?ma-'-'>:  äaj  ahmäi  'mo  atiia  ahmt  'mö vsrüra  ahmt  viri^ravasttmö^^A^  (sprach) zu  ihm  der  stärkste  {Vsrürayna):  'Der stärkste  bin  ich  an  Stärke..'"  Yt/4^3; —  vazrjm.,  'm»m  zaSnqm  viri^ravastsiiDm zalitqmYtlo.gö;  132; — hat  asti  tnqürahe spmtahe  °num  hat  v3n'i'ravast»m»mYX,l.\.
6896:^raynaca  °ta  Yt/0, 67.  b)  von  der Erde:   sam  piraiwint  'tarn  Yt /J.  9  usw.
7235:ahüm  fraparayeni  .  .  3  vakistat  atfhaot  a . .  as3t  a  . .  raocSby3  '^.ig.6. '  b)  zeit- lich :  fravasayS  . .  ya  kaca  gayät  marp^nat 3  saosyaHtät  vfrsiiraynat  Y.  s6. 10;  — pu^rS . .  apara.itCbintS  *3  d3tai'*^  vii3taot (sd.)  Yl/^.  II,  22,  28; —  apam  ..fratiS .. kaca  hü  vaxi'at  ä  ^An'^'  frasml!.datsit pairisafaiH  '^.48;  Yt5.9r,  V.  y.i;  — a  tnaiiyat  xlapat  N.  50, 46;  —  a  darr/at :^3Miry3l  (sd.)  Y.O'0.6;  —  vTsp^m  3 ahmai  sbes.  c)    'in,    bei',   räumlich:
8334:•  j.  upara'tSt-  f.  'Superiorität,  Über- lefenheif:  ^wam  nara^it  ysi  taxma jai'jyhrtte  .  .  sfarfttanAasca  'tätS  (AP.) YL5.86.  a)  sonst  mit  vananl-  Adj.: dasdi  .  .  tai  äyafUm  .  .  V9r9%rar}n}mea aAurdoat?m  vanaintimla  *t3t>m  Yt  ro. 33;  5-86.  y-34.  A'i,  X-57-33;  —  vin- liraynaAeca  . ,  vanaintySsca  paiti  'täto  Yt. 8.11.  A)  als  Gottheit:  avistayalca  .  . amavaihya  faurvatäis  amavaihyä  Häts (GS.)  Vr.(f,4.  a)  sonst  mit  vanani-  Adj.: v^ry^rayramca  ..vanaintimca  '/aftw  Y.2.6; Vr.2.8;  —  vfhhraynahe  .  .  vanainiyäsca 'tätö  Y./.6,  Vr./.6,  Vt.J4.o.
8380:•  j,  upa.8tütay-  f.  'Preisen,  Preis':  kva . .  v>ri''>:raynake  . .  iiqma.azbäiti^  {sA.)  ki'a 'staiHi  Yt.  14-^2;  —  'stüiei/ri  VyL  2t),
10042:'aufziehen,  grossziehen':  bis  hapta  pui^rqm ga'iwqm  «i/(7MJ/V"'""zweimalsiebcn junge Hunde  soll  er  gross  ziehen"  V.  14. 16.  2)  'heraufkommen  zu —,  erstehend sich  einstellen  bei  -';  a)  mit  Lok.:  Aya^ US  asa  naptyassu  naßuca  türahya  uzjSn (jSPr.^.)  '**  fryanahya  aoJyaisR  "wenn sich  das  Asa  bei  den  preislichen  Enkeln und  Nachkommen  des  Tlsrers  Fryana  ein- stellen wird"  Y..rf6".  12.  b)  mit  Dat.: US  na  aMbai  vTse  Jamyal  ahnica  xsa- ^mm^a..  Y.60.  2;  —  ta  iiö  ama  tä  v)r»- %rayna  ,  .  usjamyqn  ya  staota  yesnya  Y. i5-  3-  3)  'ausschlagen,  gereichen  zu  — '
11286:•  j.  *dixra-"  m.  'Tatkraft,  Energie':  mi- 'ämm  .  .  yö  .  .  fravazaite  . .  rd^wya  °ra kaamns  :^ar3nar3kaca  . .  viri^raynaca  Yt /0.67,
12470:—  sraohm  ..yd..yBityeiti..Aata  'vaeibys Y-57-IT, — paiti-pirme  vannya  'z/fffAP."') V.  70. 14;  —  yat  baväni  aiwi.vanyä  vTspe •va  Ytp.  4,  /5.2g;  —  imi  alte  vaca  yoi fanti  vjspanam  'vanqm  snahim  V.io. 16;  16,  Y.27.1',  Y.ig.46';  —  snaihi/.. hvS.vafjim  kam^rihe  patti  "vanqm  Y.  57. 31;  31,  YtÖ-s,  jo.aß,  129,  V.79.15;  — pas^a  jainti  'vanqm  . .  fravaxaiU  mihrS Yt  70. 133;  3. 10,' 4-  2,  5-  2^.  V.J.  32;  — hasat^rayna  paiä./asaiit  aiars  .  .  'vanam mainyavanqm  ..  drvatam  Y.S.So;  Y.io. 6,  YL  13. 4S;  —  asfi»  ,  .  taurvayeintim vTspä  tbalsa  'vanqm  maSyänqmca  Y.52. if.;  5.18,  Yl/.i',  S,  6;  —yat  mqm nalcis  taurcayät  nsit  °vS  na^a  masyS  nöii yäiaz'B »a^a pairikä  YtJ.6;  J5.56,2.n(?); — paitiltätse  'vaheca  tbaiiatahs  ma^eheca Y.6S.S;  5S.3,  VLy.'"i42;  ~y8..ä>,r)m urvaaayata  °väatia  haotäti^A.)  mafyäatca Vt  13.  89;  —  'vanqm  parö  draomBku  Yt. ^3-57!  57-  S.  noch  Y.J5.  2  (Sp.  667 u.).  a)  klassifizirt:  mürym  . .  yahmal haca  frabr^SMii  vTspe  mainyava  (Stverz.) •va  yaica  varsnya  (Stverz.)  drvants  Yl /o.  97;  usw.;  —  paiti^tätJe  mäzanyanqm (Stverz.)  'vanam  varmyanqmca  Yt.  13,1  ^T, usw.  b)  namentlich  bezeichnet:  °vö  ao^O V. /j.  i;  —  akataam  dasum'^'^  V. 79.43  (statt  Nom.);  —  °vasca  yS  apaoSs \X.8.ii;  XI,  22,  28  (daiam^'i),  18.2,  6;  — inärS  °vS  V,  ig.  43;  —  kasvjS  'vS  V.  ig. 43;  —  daium  kund»n  V,  75.41;  —  daiwil 'vS  V.  79. 43;  —  driieis  °vS  V.  iq.  43 bßiti  'vS  Y.ig.  i,  2,  43;  —  paitisJ  °vS 'Z'onqm  da!v3JfmS  V,  7^,43;  — "^jm  dalum  V./0.9;  75.43; —  vätJm  'vö (statt  Akk.)  V.  70. 14;  —  vTzansd  °vS nama  .  .  urvän^m  bast>m  vataydti  V.  ig. 39;  —  saouru  'vS  V.  7_9. 43;  —  ar^rff mainyus   .  .  'vanqm  'vs  Y.ig.  1,  43;  44;
14890:yaoiädhd  dakmayStparS  ä/ritstt.,  dairihu. paitlm yaozdd^ö  ustraAe'ti  arsnSV.Q.^T'^; 37  f.*.  a)  bes.  beim  V._>'a«-:  vanani^m .  .  yazamaide  amaheca  °ii  kuiastahe  Yt. Ä  I2J  12',  U- 133-135 '^  JJi;  —  yaf^a- maide  ^a/am  malfi^anahe  (sA)  °//*'  .  . drvaßaoi  Y.  7Ö'.  10;  —  ft«  yazata  . .  zara- %uitrS  v^fhraynaAe  'ti  manahi  Yt/^^aS; 78';  —  yqm  yasata  zard^uilrS  .  .  ava- he^a  'ti  yqnahe  yat  hi  da^a/  .  .  Yt.  16, 6f.  b)  aSahe  paiti  (Sp.  14  m.,  u.)  '(als
16478:•  j.  baevara-yna-  n,,  Plur.  'loooo Schläge':  pancascrinsi  .  .  Aazanraynai 'ynäisca  baluarj-jttäi  *aAqxsicrfnäisca  (sd.) V.  7.  S3-         DS.  °ynai  als  Inf.  sbes.
=== column 490 area
9938:490
13784:mp.  drismhi.  —  PQ.:  dusman,  dusmFitisii.  — ')  Zweimal  ha.t  NA.  duim'.  —  »)  S^P^Nachtr. —  3)  S  407.—  1)  Them.;  s.  S  407  Nlr.  Vgl. auch  die  Var.  lu  Y.  5/.  26,  A.  /.  9.  —  S)  Ent- sprechend der  Lesung  von  F  l  usw. j.  duimainyü.jayanlam  hx.7:  \it%  dmmatttyü jananUm-,  s.  Sp.  490  u.
=== leaves
1041 leaves
```


## [2026-09-06T14:55:52.406Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9925,9975p' BRT.txt",
 "description": "BRT column 490 jan-"
}
```


### [2026-09-06T14:55:52.449Z] TOOL RESULT

```
KompE  —  ai.  gada-  m,  'Krankheit'?  —  Pü. : da  da.
•  j,  gaSa-vara-  Adj.  'der  die  Wurfkeule ftihrt',  yaa.K3r»säspa:  itnsaspasca  ..yavü gaisus  'rS  Y.g.xo;  —  hrisäspahe  . . *gae^Su!f  *rahe  Ytij.Si,  136.
Komp.:  gaiä-\-*iara-,  S  26S.  37').  —  Pü.: gaimar  {Sü. :  gaifäi/iaraA)-,  erl.:  tu!  iSr  fa gai  vis  katt.  —  ■)  Vgl.  ai.  vajra-bkft-.
•  j.  ga8ä-  f.  "Wiuflteule"*:  he  . .  °oqtn nijairtti  aspalca  puiti  vlral^a  "er  schmet- tert die  Keule  nieder  auf  Ross  und  Mami" Yt.  jo.  101;  —  hazannm  °oanqm  Ytio,
131-
KompA.  —  fli.  gada-  f.,  mp.  gas  (geschr.  dt); s.  noch  Osthoff  Par.  143.  —  ")  Im  Gegens. va  vazra-,  womit  gehauen  wuide.  Vgl.  Vt 10.  131  f.,  wonach  sich  in  ;1/f%ras  Wagen  1000 gaiä-  belinden,  aber  nur  ^in  zaim-.  Anders Galt,  OK,  445 ,  der  auf  die  Grundbedealnng von  saina.  lu  viel  Gewicht  legi.
•  p.  ga^dära-  m.  Name  eines  Lands, Gandarilis :  imä  dahyavJ^  tya  adam  *adar- s'iy  .  .  he'dus  -/-a*  saka  D.5.  2;  ff.  3,  Bh. /.  6.
•  j.  gaSö.karSta-  Ad},  'von  Räubern, Banditen  bewirkt,  veranlasst':  paüÜtätSe Hake  tbaisaahB  Yt  13.  1 36,
•  j.  gaiö.tay-  m.  'Räuber,  Bandit':  äal *aite  *ySi  fracarinli  kfrpsqsca  -hsülsäi  dal- visca  *Aandramana  ufa.mraodStca  vups.- xlaps  ".  .  die  welche  jede  Nacht  zu  (in die  Gesellschaft  von)  Wegelagerern  und Banditen  und  (Iü^tdschen  Rotten  und Hurenjägem  gehen"  ^-SS',  —  paiHi.- :fairu  (sd.)     rat^anhs    vä    kpnsqm    va
dby  Google
489
gadötüt-
'gan-  I  a
490
*'tinqm^^  {va)  ". .  oder  durch  Wegelagerer
oder  Banditen"  N.  26.
Ableil.  aus  tgoia-;  vgl,  dazu  ai.  Vfia-  und vftälay:  —  Pü.  (lu  N.  S3)'-  galakaseähtA'), (zQ  N.  36):  gaiajläni),  dazu  die  Eil.:  väng kai  äula:^  Syel.  —  ')  Hds.  laiSJ'  (oder  mit dem  zweit enf -Zeichen  znAnfang).  — >)Geschi. daddddf.  —  3)  Gescbr.  dddf.
•  j.*gadötGt-f,'Räubertu[n,  Räuberbande': yat  äjasät  ''ktrisasca  *°tstai'l  dasvllca handramana  Yt.  u.  6.
zSuK  5.  BtH!_  WklPh.  18^8.  1052.  Vgl. mp.  gaiui^w  Bd.  j/.  6;  Justi  NB.  107.  — Pii.:  gaiakaitinA.  —  «  So  F  I ;  NA.  ^-oJi" mUa.  —  '>  Nach  DST.  Jaiar/fln,  5.,(-oJfl- Nu,  s
•  p.  ga''dutava-'>  m.  Name  einer  Land- schaft in  Arachosien"':  'vc^  näm^  dah- yaui  Bh.  j.  10.
■>  Die  Lesung  des  vorletzten  Buchstabens  {f* oder  m'?)  ist  unsicher;  s.  KZ.  J/.  518. Übrigens  kann  Juetis  Deutung  des  Namens als  'Weiienland'  (GIrPh.  a.  430,  ZDMG,  51. i\o),  die  auf  . ,  m"  .  .  fusst  -  gifduma'va-  - nur  unter  der  VoiaussetzuDg  aufrecht  erhalten werden,  dass  in  jener  Landschaft  der  Ober- gang dei  Tenues  in  Mediae  nach  Nasal  um vieles  früher  stat^efunden  habe  als  sonst;  s. xantunia:  —  ')  Wie  aus  Bh.  J.    12  folgt.
•  j,  "gaJwra  iurS  (sd.)  . .  &ux/ä  maki' FrW.  2.  2.
■  j.  gaSwa-  m.,  gaSwä-  f.  'Hund,  Hün- din''' i)xa.:di^e  navaiti 'wqm{CiY,) pairi.- yaoidaikUa  stiptibyas£a{^^..'S.i4-  I7;  — bis  hapta  puhrqm  'wqm  (AP.)  uzjämöit (sd.)  V.  r4.  i6;  17;  —'  fra  mi  'wa  (NP. als  AP.)  sasayqn  mzbjnta  (sd.)  V,  8. 37.  2)  f.:  aiia  (näml.  hätrist)  ca%wan.- failißäna ya  'Tva'W .i^.iqGl.; — yaica  aisa toa  uÜrS-itänaisva /rajasät{sA.)  V.  15.23; — yS  °wqm  yqm  apu%Tqm  {sd.) /anaiä  vs ,.pasdaya/i{sd.)  vä  yaica  alsa  "wa  magye .  .  pai'jyäite  V.  Jj.  S ;  —  °wqm  yqm  apu- irqm  "^rayqm  *baesdri  "eine  Hündin,  die kürzlich  geworfen  hat,  . ,"  V.  15.49.
Et,?  — Pü.:  jttt.  — ')  Wohl  besonderer  Rasse,
im  Gegensaiz  zu  '^span:
•  g-  ■'"gatte",  ^gattöi'J  Inf.  i)  'her  zu konunen  zu—'  (Dat):  matbyS  zi>ay:i  ahm vtttski^  ah  'te  "zu  mir  her  rufe  ich Asa,  her  zu  kommen  mit  dem  guten  Lose" Y.5/.  10.  2)  'hin  zu  gelangen  zu  -  (Akk.), ZD  erlangen':  u3ä  aAmsi yaAmäi  u^ä  {sd.) koAmäi^  . .  dayäi  . .  uiayüitl  trulilm  'isi vattmi  "nach  seinem  Wunsch  wünsche  ich einem  Jeden  .  -  die  Krafl  sammt  dem Bestand  zu  erlangen"  Y..^j.i.
Zum  V.  gam-,  Bthl,  KZ.  28.  21").  —  Pü. (dRn.):  riu  iS  {?<}i.:  ftäpnomi  U),  pa  rasiin  hac tS.  —  ')  NA.  getrennt,  gt^-f  steht  für  gat', S  268.  4g.  —  ")  So  trotz  Gdn.  KZ.  jo.  322, Mills  G.  509,  599,  Dict  161  und  JusTI  PrJ. 88.  74.  214.    Lauüehre!
•  i-  gafya-  n.:  -?-. KompE.  (inoflvö^*,  *iäHg',  EN.j  NA.  trennt).
•  j-«  S-i  P-  'gäm-  V.  'schlagen'.  Praes.  i jan-''':  (yn-,^  Ja-,     5    Jayn-,     tj     (Pass,)
\janya-,   PiT.'jaini;    Perf.   i  /ajn-,    PfPr.
\/ayna-.  —  PPfP./a/a-,  PFP. /q^wa-;  Inf.
'Jaidyäi,    'jaiti,     ytnqm,     'ynai,     'ynyäi;
■  Absol.  'jatim,
\  i)  'schlagen,  treffen,  verletzen;  er- schlagen, töten':  a0a  he  6ä%a  kanar^am jaynvä  paiHjfanhayäti  '^•Sl- 10;  —  y^ gaüwqm  . .  Janaiti'^  v3  vayelH  va  .  . pazdayäti  (si)  va  V.  75.  5;  —  jaritu  a.- aitySmäA^S  vup?m  yask»mca  ..  V.20. 12;
—  anyii  akmäi  yd  Janaiti'''  frala  kusaiti (näml.  hlm)  V.5.34;  Yt.<^8(?); — jainti mqm  ahuna  vairya  avavata  snaiiiia yäha  ..    Yt. /?.  20;  j.  lo-is'»    {jaiiitt),
14— 16'5  {fanät)'");  — yS  aSa!sqm  sünqm (als  Obj.)  >(«/(■  V.y.8;  w.  i,' FrB.;  '— /anaiii'*  vispa^qm  anrB  mainyu/Yt.3.5; Y.1S.2  PüZ.; — 'vjspa  druxs  jattaiti'^  Yt 2. 1 1 ;  12;  —  ya'ha  ya^  . .  janyät  *n)r^ V./1V.T2;  —  janät'*  t?m  . .  haosrava "töten  soll  ihn  .  .  H."  Yt.g.iS,  i5.32; ig,  44';  —  yat  janatii  /litüsppm  raüe ^paiti.vazaityäi  (sd.)  Yt.  J5.  28;  —  na?^a manyete  (sd.)  jaynvä  na^a.äm  y?nqm sadayeiti  (sd.)  Yt  /o.  7 1 ;  —  taha  hunavS  . . jata  pai^yänU  Mt.iO.iiy,  80;  — yasca dilti  janat  .  .  vikrhm  V.  7.  51  PüZ.;  52 PüZ.,  y.'s.  4,  Yt.^.  2*;  —  jata  (2P.?) karapanS  cT^rJm  Y1.4.T,  — fanäni  äqma daev3.dat2m  V.  ip.  5;  $',  Yt.  4.  $;'  — rasm5.jat>m  va  dim  jainti  amff.jabm  (sd.) va  Yt  70.52;  74. 36f.4;  —  ka'^a  (sd.) nisMäiamal  ya'^a    hltri  jatiüma  Y.61.  $;
—  iamdha  airyabyü  dai^AubyS (sta.ttiiP.?) janyAntH^ass.'i)..Yt.8.6i;—*/anaaAssai^in
(sd.)  ttsit  janm^  Yt  i4-  S6;  — yS  janat''> dva  %rifva..dagvanqm  Yt/p.26;  41— 43*, _;.  10;  —  dusmaitryä  *janant?m3'>  bavahi yaha  v)r3%raymm  Az.  7;  —  aß  nanm jainti  väf  .,  afl  nar?m  nSit  jainti  V.5.  8; .  9';  —  ynat'^,  ynai''>  F.  22.  a)  'schlagen' i  in  militärischem  Sinn,  'besiegen':  ipasavt^ adam  karam  tyam  nadi''tabairahya  adam \ajanam  vasiy  Bh.J.18;  19,2.13,  4.1;  —
dby  Google
491
'gan-
'gan-  mit  nr  2  a
491
liara*  kyJ'   mann    avam     karam  .  .  aj<^ (3SPrA.)    vasiy    Bh.  2.  7-iiS,  ^.3,  9,  10; /,  6,  7,  2.6;    —  paraidiy    avam    käram jadiy/iyt^..  Bh.^.  3;  2.7,  10; — paraita avam  karam  .  .  jatä  (2P.)*'  hyJ'  .  .   Bh. t;  II  —  %ragtaonS  yö  Janat''> Y.9.  8;  11;  —  vaSam'.  . ^ra^aonS  yat  azis  äahukd 93"-  a)  'Jnidm.  (einen
ide)  schlagen,  (eine  Ver- ;en';  a)  mit  Dat.  und  Akk.; jainti  V.  jj.io.  ß)  mit yö  narim  andusa  snd^a 30.  7)  mit  dopp.Akk.:
jainti  ar?dus  vii  . .  maza- •»  (sd.)  N.  45;  — ylf  nanm siia'hsm  Jainti  V.  4-  40, 4  2 ; . 39.5-37, y-"-  5)mit
nstr.  {'mittelst') :  yö  adniim "iiila  vlxrBmmtim  x'arim 2)  '(den  Vertrag)  ver- ' :  mi'hnm  mä  janya  Yt. 'das  Wasser)  treffen'  sva. iniessbar  machen' :yV^  ap>m t/rävayeiti  V.5.37. chlagenauf— ,  erschlagen': aipi.janyh  mi^ra  Yt  10. i:  lies  aipi.jaiti,  Inf.] lieder-,  erschlagen,  töten'; upäk?m  janaita'''  ava  kl ; — yS  frasiiim  usayanqm 't  y,  105;  ~  sraoiö  asyö anyät  'V.iff.41; —  masda- ■ivanaHbil  (sd.)  avajamm udrahe  avayiulnS  ha!c5 51.  a)  bes.  vom  Töten ■e;  ban'arg  aiinqm  ..  ava.- Sf.';  —  xraßlnm  ava.- Im  .  .  V.  16.12;  —  Äakyä- vanijm  xra/stranqm  ava.- ;  JÄ73J.  2)  'anfallen,
rim  pasüm  avayniV'^  paoi- 'yätV. 13.^2.         [Bh.;.io;
a  'töten'^:  kära^Hm  haca a*  (sd.)  karam  vasiy  ava- ■arädiy  (sd.)  käram    avj/a-
". .  deshalb  möchte  er  die ih.7. 13; — ya'kä  ka"bsjiyj' 1"  (sSPrA.)  küraAyS  naiy *  /ya*  bardiya''  *avi}jatc^i''
getötet  hatte,  . .,  dass  B. Ii.  /.  10;  10;   —    Uta  mar-
```


## [2026-09-06T14:56:08.220Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG gaz\"; grep -n \"\\*gaz\\|gaz-\\b\" CHEUNG.txt | head -20\necho; echo \"=== CHEUNG jan\"; grep -n \"^\\*jan\\|\\*jan \" CHEUNG.txt | head -10",
 "description": "Grep Cheung for gaz and jan"
}
```


### [2026-09-06T14:56:08.295Z] TOOL RESULT

```
=== CHEUNG gaz
581:pass (time ?)’ and *gaz ‘to receive, accept’. 
8432:*gaz ? 117 
8490:*gaz ? ‘to bite, sting’ 
8498:118 *gaz 
55768:*dans, *gaz, *xsau (s.v.) 
57992:*gaz 

=== CHEUNG jan
7593:*jan. This derivative is often used in impersonal constructions. In the Zazaki dialects 
15043:224 *jan 
15100:*jan 225 
15686:*jan), Abyan. katan/e-k-, Anar. ikeft/ek-, Ard. kat/ k-, Fariz. kát/-k-, Yar. kat-/-k-, 
55615:*daH’, *jan (s.v.), *ka(H)ud 
56010:*man8H, *jan (s.v.), *kaup' 
56946:*jan, *kaus’ 
57840:*jan, *uadH
```


## [2026-09-06T14:56:11.048Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8485,8530p' CHEUNG.txt",
 "description": "Cheung *gaz entry"
}
```


### [2026-09-06T14:56:11.103Z] TOOL RESULT

```
*REFERENCES: EVP: 10; IFL П: 534b, 189b; Andreev — PeSéereva: 234a; Abaev, Slovar’ I: 160 Ё; EVS: 
38a; Abaev, Slovar’ II: 336 f.; Werba 1997: 178; Steblin-Kamenskij 1999: 276; Cabolov 2001: 409 f.; 
NEVP: 8 


*gaz ? ‘to bite, sting’ 

*MIDDLE PERSIAN: BMP gc- /gaz-/ ‘to sting’ (LW) 

Pres.: IND. 3sg. BMP асу! /gazéd/, SUBJ. 3sg. BMP gc't/gazad/; Partic.: perf. pass. BMP gcyt /gazid/ 
*PARTHIAN: “gst (pret. stem) ‘to bite” = Ghilain: 96 | DMMPP: 170b 


118 *gaz 


*NWIR: NP gazidan, Kurd. gastin, gazin/gaz-, Nn. gisa/giz-, Siv. gäz-/gäze ‘to bite; 
sting’, Bal. gassit, gast/gass- (inch.) ‘to bite, sting, wear out’, NP -gaz ‘biting, 
pungent’, саха ‘a biting serpent’, Zaz. gaz (f.), Abz. 207, Varz. gize ‘bite, sting’ 
*NEIR: (+ *4-) ? Pash. ayzai ‘thorn’ = ayzäy, azyáy (m.) || (+ *ham-, *abi- ?) ? Oss. I. 
enqevzyn/engevzt, D. evgezun/evgazt ‘to gurgle, run out [of water]’ (with irreg. 
metathesis ?, sec. pref. ?) 

9 The root is exclusively Iranian. The suggestions of Korn 2005: 80, fn. 27 (deriva- 
tion from IE *geg"- ‘to enter, seep in’, Skt. gäh-) and Bailey, DKS: 349a (IE *geg"”- 
“prick, sting’) are either semantically (Korn) or formally (Bailey) unconvincing. 


“PIE LIV: — | Pok.: 
*REFERENCES: KPF I: 146a; EVP: 10; Abaev, Slovar’ I: 164; WIM III: 106; Paul 1998: 298a; Cabolov 
2001: 372; Lecoq 2002: 594a, 678b; NEVP: 8; Shahbakhsh: s.v. gass-; Korn 2005: 80, 316, 397 


* 947 ‘to accept, receive’ 

*KHOTANESE: (+ *pati-) pajays- ‘to enjoy; accept’. © On the Khot. form pajays- see 
Emmerick, Fs Humbach: 77. — SGS: 64 

*SOGDIAN: (+ *pati-) 1. SSogd. pcy’z ‘to promise ?’, BSogd. pcy’z, CSogd. pcy’z 
‘to receive, take, accept’, || 2. secondary ? CSogd. pcx$- ‘to take, hold, receive’ (cf. 
Sims-Williams 1984: 54, no. 29), MSogd. ptcxs- ‘to take, hold, receive’ || (+ *para-) 
SSogd. pry’s-, BSogd. pry’s-, CSogd. pryyZ ‘to deprive’ || (+ *fra-) MSogd. Bry’z 
“grasping, extending (of hands), [Tk. transl.] sunup’ (Sogdica: 64 ad 11) 

Widely attested: 1. Pres.: IND. 35р. dur. CSogd. pcy’ztq, OPT. 3sg. BSogd. pcy’z’y, 3pl. SSogd. 
pey’zy’nt, IMPV. 2sg. BSogd. pcy’zCSogd. pcy z, 2pl. BSogd. pcy’zö, CSogd. pcy’z0’, etc. || Widely
```


## [2026-09-06T14:56:11.531Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15040,15115p' CHEUNG.txt",
 "description": "Cheung *jan entry"
}
```


### [2026-09-06T14:56:11.576Z] TOOL RESULT

```
*REFERENCES: DKS: 110b; Werba 1997: 404 f.; Vahman — Asatrian 1991: 107; Lecoq 2002: 617 


224 *jan 


Han ‘to kill, slay, strike’ 

*AVESTAN: jan- (yn-) ‘to kill, slay’ || (+ *aua-) ‘to kill’ || (+ *upa-) ‘to nudge, touch 
upon’ || (+ *pati-) ‘to strike, hit (with a weapon) against’ || (+ *ni-) ‘to strike down’ 
= Liste: 23 

Pres. {1} athem.: IND. 1sg. med. YAv. niyne (Yt 4.5), 3sg. YAv. jainti (V 13.8, Yt 17.20, Yt 3.10 ff., 
etc.), med. YAv. niyne (Y 10.2, Y 57.29, Yt 10.104), 3pl. YAv. "niyninti (Yt 10.133), 3р1. med. *niynaire 
(Yt 10.40), SUBJ. 1sg. ҮАУ. janani (V 19.5, Yt 4.5, Yt 15.28), 3sg. ҮАУ. janat (Yt 19.26, Yt 19.41 ff), 
Ipl. YAv. janama (Y 61.5), OPT. 2sg. YAv. janiià (Yt 10.2), 3sg. YAv. janiiat (V 18.12), YAv. 
auua.janiiat (V 14.5 f., V 16.12, V 18.73, V 19.41), Y Av. upa.janiiät (V 5.11), med. Y Av. paiti.ynita (Yt 
13.67), 3р1. med. ? Y Av. "jan(a)iianta (Vn 112), IMPV. 25р. ҮАУ. jaiói (Y 9.30 ff.), 3sg. YAv. jantu (V); 
Pres. (2) them.: IND. 3sg. YAv. janaiti (V 5.2, V 5.34, V 15.5), INJ. 3pl. YAv. janon (Yt 14.56), SUBJ. 
3sg. Y Av. janaiti (Yt 2.11), Y Av. janat (Y 9.24, Yt 3.14 ff., 9.18, etc.), 3sg. med. Y Av. nijanaite (V 9.56), 
ОРТ. 3sg. med. YAv. auua.janaöta (V 16.12), 3pl. YAv. айпа janaiion (V 8.74); Partic.: pres. ҮАУ. 
ynant- (Yt 10.71), med. YAv. ynäna- (V 15.14), Y Av. auuaynäna- (V 13.51), perf. YAv. jaynuuäh- (Y 
57.10, Yt 10.71), fut. pass. YAv. ja0uua- (V 13.40 £, V 18.65), perf. pass. YAv. -jata- (Yt 10.110), YAv. 
nijata- (Yt 5.77); Inf. pres. OAv. jaidiiäi (Y 32.14); Pass.: pres. SUBJ. 3pl. YAv. janiianti (Yt 8.61, ? Yt 
14.43); Intens.: pres. IND. 3р1. med. YAv. nijaynonte (Yt 13.48), INJ. 35р. YAv. auua.jaynat (Yt 13.105), 
SUBJ. 3sg. ? YAv. “auuajaynat (V 13.32 ff.) 

*OLD PERSIAN: Ja(n)- ‘to strike; smite, defeat (enemy in battle); mould (brick)’ || (+ 
*aua-) ‘to smite down, slay’ || (+ *pati-) ‘to fight against’ || (+ *fra-) ‘to cut off 
= Kent: 184b f. 

Pres. athem.: IND. 3sg. ja"tiy <j-t-i-y> (DSe 36, DSe 40), impf. 1sg. ajanam <a-j-n-m> (DB 1.89, DB 
1.95, DB 2.69, DB 5.25, XPh 34), <a-j-n-m> (DB 4.6), 3sg. aja" <a-j> (DB 2.26, DB 2.36, DB 2.41, DB 
2.55, 2.61, DB 2.87, etc.), <[a]-j-> (DB 2.46), 3sg. med. patiyajata <p-t-i-y-j-t-a> (DNa 47), 3р1. avajana" 
<[a]-[v]-a-j-n> (DB 2.13), OPT. 3sg. avajaniya <a-v-a-j-n-i-y-a> (DB 1.51), IMPV. 25р. jadiy 
<[j}-[di]-i-y> (DB 2.31), <j-di-i-y> DB 2.51, DB 3.15), 2р1. jatä <j-t-a> (DB 2.21, DB 2.84, DB 3.58, DB 
3.86); Partic.: perf. pass. avajata- < a-v-j-t> (DB 1.32) 

*MIDDLE PERSIAN: MMP zn-, BMP zn- /zan-/ ‘to beat, strike, smite; to play an 
instrument’ || (+ *aua-) MMP ’wzn-, BMP ’we- /öz-/ ‘to kill’ || (+ *ui-) IMP wz'd- 
(denomin.) ‘to destroy = DMMPP: 383b f., 77b. 

Pres.: IND. 3sg. MMP jnyd, BMP znyt /zanéd/, 2р1. MMP znyd, SUBJ. 1sg. MMP zn’n, 3pl. MMP 
zn'nd; Partic.: pres. MMP zn’n, perf. pass. MMP zd || (+ *aua-) Pres.: IND. Leg, MMP ’wznym, 35р. 
MMP ’wznyd, 3р1. MMP ’wznynd, SUBJ. 152. MMP ’wzn’n, 3р1. MMP ’wzn’nd; Partic.: pres. MMP 
"wzn'g, perf. pass. MMP ’wzd; Inf.: MMP ’wzdn || (+ *ui-) Inf.: IMP wz'dtny 

*PARTHIAN: jn- ‘to beat, strike, smite; to make with a die; to play an instrument’ || (+ 
*aua-) 'wjn- ‘to kill’ || + *ш-) IPth. wyz’d- (denomin.) ‘to harm’ = Ghilain: 55 | 
DMMPP: 199a, 68b 

Pres.: IND. 3sg. jnyd, 3pl. jnynd, SUBJ. 3sg. jn’h; Partic.: perf. pass. jd; Inf.: jdn || (+ *aua-) Pres.: IND. 
2sg. *’winyh, "wjnyy, 35р. "wjnyd, 3р1. *’wjnynd, SUBJ. 15р. ’wjn’n, 25р. ’wjn’, ’wjn’h; Partic.: perf. 
pass. ’wjd || (+ *ui-) Inf.: IPth. wyz’dytn 

*KHOTANESE: jsan- ‘to strike; slay’, jsafi- (pass.) ‘to be struck, slain’ || (+ *pati-) 
OKh. pajs(afi)- ‘to be struck, beaten’ || (+ *ni-) nijsa- ‘to befall, be struck with’ 
> SGS: 37, 65 


*jan 225 


*SOGDIAN: MSogd. jn- ‘to strike’ || (+ *aua-) BSogd. ’wzy’n ‘killing, slaughter’ || (J 
*pati-) CSogd. ptyny’ (loc. sg. f.) ‘in the manner of (Schwartz 1967: 151) || С 
*fra-) MSogd. frjn- ‘to cut off. 0 On MSogd. frjn- cf. Henning 1965: 32, fn. 4: "The 
close agreement in meaning with Old Persian frajan- is noteworthy.": OP naham uta 
gausa uta hazanam frajanam ‘I cut off his nose and ears and tongue’ vs. MSogd. bd 
b’d gws frjnynd ‘time and again they cut off his ears’. 

Inf.: pres. MSogd. jnyy (Sogd.Tales: 467), pret. MSogd. jtyy (Sogd.Tales: 467) || (+ *fra-) Pres.: IND. 
3pl. MSogd. frjnynd 

*CHORESMIAN: y- (< *yn- ?) ‘to hit, strike’ = Samadi: 74 f. 

*BACTRIAN: С1- ‘to strike’ || (+ *ui-) о1оубо-уоро ‘injurious, able to cause injury’
```


## [2026-09-06T14:56:21.561Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15115,15190p' CHEUNG.txt",
 "description": "Cheung *jan continuation"
}
```


### [2026-09-06T14:56:21.614Z] TOOL RESULT

```
*BACTRIAN: С1- ‘to strike’ || (+ *ui-) о1оубо-уоро ‘injurious, able to cause injury’ 
c» S-W, Bact.: 192a f., 212b 

*NWIR: Widely attested: NP zadan/zan-, Zaz. jinayis/jinen-, Gz. Zen-/Zent ‘to beat, 
hit; to play (music)’, Bal. jat/jan- ‘to strike, hit’, Awrom. Zanay/(-)Zan- ‘to shut (the 
door, etc.); to churn’, Fariz. -jaj/-jan-, Yar. -Zà/-Zan-, Natan. Jäj/jän- ‘to play (a string 
instrument), Fariz. -gan-/-gan- (denomin. ?), Yar. gon-/gon- (denomin. ?), Ard. jiye/ 
jin-, Gil. (Rsht.) zecen/zaen-, Ham. jiyän/jon-, Khuns. zin-, Anar., Lasg. -jas/-joen-, 
Nn. zeye/zin-, Qohr. jida/jin-, Sang. -Ze&Zenan-, Shamerz. -zi(n)-/-zänäm-, Soi zat, 
Sorkh. -jahan/-jan-, Varz. jinde/jin- ‘to hit, strike’, Gur. (Kand.) -Zinyan- (pass.) 
/-Zan- ‘to close the door’ || (+ *а-) Delij. адепт ‘to strike, beat (on the ground)’ (Safari 
1373: 68, 229) || (+ *ui-) NP gazand ‘damage, injury’ 

*NEIR: Pash. -Zan-/-Zal ‘to chop, mince’, Oss. I. дап, D. бапа ‘wound, fracture; 
shortcoming; [also D.] guilt, transgression’, (NP >) Sh. zin-/zıd, Khf. zaen-/zöd, 
Rosh. zan-/zod, Sariq. zon-/zed, Yzgh. Zan-/Zud ‘to beat, kill’ || (+ *abi-) Yzgh. 
vajan-/vajad ‘to throw down, overcome, vanquish, conquer’ || (+ *upa-) Sh. bizin-/ 
bizid, Khf. bizoen-/bizod, Rosh. bizin-/bizod, Bart. bizan-/bizód ‘to drive into, 
enclose cattle in cowhouse/pen’, Sariq. bizis-/bizeyd, bizis-/bizeyd (inch.) ‘to touch, 
brush against, attack, attain’ || (+ *ni- ?) Pash. nayand (m.) ‘harm, damage, injury’ 
*MISC: Par. jan-/j6, Orm. zan-/zök ‘to beat, strike’= zan-/jök, zók, jan-/jök, zók || (+ 
*аџа-) Orm. uZnaw-/uZnawok, wazn-/wazyok ‘to kill’ 

*SANSKRIT: han ‘to strike, to slay, to kill’ (RV) = EWAia II: 800 

9 This root has impeccable IE credentials. 

«PIE *g""en- ‘to slay, kill’ > LIV: 218 f. | Pok.: 491 ff. 

sit COGNATES: Hitt. ku-(e-)en-zi ‘he kills’, Gr. Өғіуо ‘I kill’, Gr. @dvocg (m.) 
‘murder’, Olrish gonim ‘I hurt, kill’, etc. 

*REFERENCES: KPF I: 82a, 246b; IIFL I: 262a, 414a, 388b; EVP: 105; KPF II: 184; Christensen, 
Contributions I: 67, 165, 159, 260; Christensen, Contributions П: 50, 52 f., 115, 118, 159 Ё; Abrahamian 
1936: 116; MacKenzie 1966: 114; Gignoux 1972: 36b, 67b; EVS: 108a, 117a, 22b; Lecoq 1974: 63; 
Nyberg II: 230a f., 146b f., WIM I: 68, 74; WIM IV/1: 87; DKS: 114a f., 115a; Abaev, Slovar’ П: 290 Ё; 


Werba 1997: 268 f.; Paul 1998: 299a, 302b; Steblin-Kamenskij 1999: 329, s.v. Say-/sit-; Jusupova 2000: 
84; Lecoq 2002: 121, 130; 132 (passim); NEVP: 56; Kiefer 2003: 210; Korn 2005: 313, 368 (passim) 


226 *jiauH 


*fiauH ‘to chew’ 

*MIDDLE PERSIAN: MMP jw- ‘to chew’, BMP ywd- /joy-/ ‘to chew; devour (daevic)’ 
с DMMPP: 199 

Pres.: IND. 3р1. MMP jwynd, BMP ywdynd /joyend/; Partic.: perf. pass. MMP jwwd, BMP ywt /jud/ 
*PARTHIAN: J ’w- ‘to chew (?)” = DMMPP: 197b 

Pres.: IND. 35р. j’wyd 

*KHOTANESE: (+ *ham-) LKh. hamjvame = SGS: 138 f. 

*SOGDIAN: BSogd. zyB, MSogd. jB’ ‘to bite’, CSogd. (zb'qy) *Zyb’mnty ‘the biting 
(of their tongues)’. © Sogd. -B- (CSogd. -b-) is perhaps due to the influence of zB’k 
(CSogd. zb'q) ‘tongue, language’. 

Impf.: IND. 35р. BSogd. ZyB’’; Pass.: pret. IND. 1sg. MSogd. jB’ty "ktym ‘I have been bitten’ (BBB: 43) 
*NWIR: NP javidan/jav-, Bal. ja0-//a-, Kurd. (Kurm.) jun, jutin/ju-, (Sor.) jun/ju-, 
Jawin/jaw-, Zaz. jawitiS//awen-, (LW) Siv. gav-/Zavi, Tal. jüye ‘to chew’, Abz. 
Jovida/jov- ‘to gnaw’ 

*NEIR: Pash. Zowul, Zoyol/Zoy- ‘to chew’, (LW ?) Yghn. Zav-/Zafta ‘to eat (liquid 
food), drink, slurp’ (why -v-/-f- ?), Rosh. yiyaw-/yiyud, Bart. yiyaw-/yiyud, Khf. 
yiyaw-/yiyud, Orosh. yiyaw-/yiyud ‘to gnaw, nibble’, Sariq. Z(i)yew-/Zyod ‘to 
masticate, munch, to fight together [of dogs, etc.]’, ? Ishk. Saw-/Sawod ‘to chew’ (S- 
< ?), ? Yi. Zaf-/Zaft- ‘to chew, masticate; to light a fire’ (why -f ?) 

*MISC: Orm. zay-ék ‘to chew, mastigate’ = zay-/zayók 

© On the development of initial *gi- > Ir. *ji- see Rasmussen 1989: 114, no. 5. This 
development suggested by Rasmussen may also account for the doublet roots *JiaH
```


## [2026-09-06T14:56:35.406Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== nazand\"; grep -n \"nazand\\|naiand\\|na^and\\|nizand\" HRN.txt | head\necho \"=== azadan/azdan\"; grep -n \"äzadan\\|azadan\\|äzdan\\|äzudan\" HRN.txt | head\necho \"=== zadan\"; grep -n \"^[0-9]*\\. *zadan\\|zadan \" HRN.txt | head",
 "description": "Grep Horn"
}
```


### [2026-09-06T14:56:35.480Z] TOOL RESULT

```
=== nazand
=== azadan/azdan
1583:päz. awazadan.
=== zadan
```


## [2026-09-06T14:56:39.980Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==226{print}' HRN.txt",
 "description": "Horn leaf 225 (page 204)"
}
```


### [2026-09-06T14:56:41.889Z] TOOL RESULT

```
— 204 —
b ehren kann (ee ö biigrEzeö)\ Wenn man hier von
'fliehen* ausgehen wollte, so würde die Erklärung sehr
gezwungen sein.
915. giristen, giristen *klagen, weinen', Impt. girl ^) girye,
giryjden (Sahn. I, 107 Vers 837).
aw. [/^gar-, gerente 'anrufen*; phlv. grlstan 'weinen,
klagen (AV.), g(i)rt/TnUan (AV.) ; ai. [/^gar-, gpidti 'an-
rufen'.
kurd. girin weinen ; oss. d. yär, t. qär 'Geschrei,
Ton, Laut, Stimme* (88); bei. greag, n. girey 'lärmen,
schreien, heulen, weinen*, Impt. bigri (117)^).
916. fße^endj guzend (AM. S. 38 Zeile 7) 'Schade Leid',
bezendT 'Elend'.
aw. "^mjainti-, vergl. ai. vi -i- iXAa«-, vihanti- ; phlv.
agajand bezw. agazand (AV.).
917. gu^ärden 'auseinander setzen, darlegen, bezahlen ;
gtizäris, güzärisn (Wörterbücher)^), guzäre; vergl. vecer
(vejer) 'richterliche Entscheidung (unbelegt).
skr. vi + [/"car-, Caus. 'erwägen, in Betracht ziehen,
prüfen ; phlv. v(i)cartan (AV.), v(i)car(i)sn^)j v(i)cartar
'verständig (für aw. cazdönkvaM-, arm. LW. vcar 'Be-
zahlung*.
918. guziden 'aussuchen, erwählen*, Praes. giizm-em, guzin
'erwählt'.
aw. vi H- [/^öay- 'aussuchen* ; phlv. v{i)öUany v{i)cwet
(AV.), arm. LW. vöit 'rein, lauter*; skr. vi-^ i^cay-
'auslesen, aussuchen'.
bei. gicinag, n. gisainay auswählen, aussuchen* (104).
*) Im Reim bei Eth6, Morgenländische Forschungen, S. 59,
Zeile 5 v. u. (Dies Citat verdanke ich Herrn Prof. Nöldeke).
2) Hübsohmann, ZDMG. 44, 557.
3) Vu 11 er 8 8. V. menisn hat falsch gttSärisn; beide Stämme
sind nicht zu verwechseln, doch werden sie in den Wörterbüchern
immer zusammen geworfen.
*) Phlv. *v%närisn^ vltiärfan* ist wohl auch r{i)c" zu lesen (ein aw.
c ist eingedrungen, wie öfter); die Bezeichnung des i in der Praepo-
sition vi wäre sehr aufiPäUig.
```


## [2026-09-06T14:56:48.814Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==253{print}' HRN.txt",
 "description": "Horn leaf 252 (page 231)"
}
```


### [2026-09-06T14:56:50.711Z] TOOL RESULT

```
MI
— 231 -
WSO, niiad 'Geschlecht, Abstammung, Adel' *), nizade 'von
adeliger Abstammung 2).
aw. ^nizäti", vergl. skr. Jati-.
1031. uiS&iidy nezend niedergeschlagen (trop.); elend,
niedrig*.
ap. *ni -h l/yaw- niederschlagen*, also etwa ein ap.
*/ii/a«/M- 'niederschlagbar voraussetzend, vergl. indische
Bildungen auf -tti- bei B. Lind n er, Altindische Nomi-
nalbildung, 8 54, Ib (S. 80).
Unsicher.
1032. niSästen 'sich setzen lassen', Praos. uisän-em,
nisänden.
Causativ zu nisesten (No. 1083); phlv. n(i)sastan (vd.
16 (17) ÖL), n(i)sanet (M6n.).
1033. nisesten 'sitzen*, Praes. nisln-em,
g. senastmün 'sich setzen'.
ap. m + [/^had-, Caus. niyasädayam; aw. ni -\-
l^had-, mshiSaiti 'sitzen, sich setzen', Caus. niSädayöis;
phlv. n(i)sastan, n(i)$fnet (vd. 16 (1)) ; ai. ni + [/^sad-,
stdati,
kurd. LW. nisin 'sich setzen'; bei. nindag^ n. nin-
day^ Causat. nistainay (264).
Der Nasal der Wurzelsilbe in np. nism-em ist auf-
fallig (er findet sich auch in bei. nindag, ksl. sedq
(sösti), apr. midMs, ist also wohl alt), ebenso das
lange f. Vergl. Bartholomae, Studien II, 97, 98,
der eine Erklärung für die iranischen Formen allein
versucht. Np. nisäxten 'sich setzen lassen* (z. B. Vis
und Rämin, Seite 24 Vers 7) ist eine Analogiebildung.
1034. niseb Unteres; unten'.
aw. *mxsvaepa-, vergl. x^^^W^' (No. 799) ; phlv.
n(i)Sep (AV.), n(i)sepitan^ n(i)sepmd 'sie gehen unter*
(Salemaifn, Mel. asiat. IX, 238), vergl. v(i)seft, 'Ver-
lorenes Sprachgut*, No. 229.
>) VergL Rückert, ZDMa. 10, 138.
2J Vergl. besonders äähn. II, 765 Vers 11 ; auch II, 611 Vers 1601.
```


## [2026-09-06T14:57:03.707Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD zadan/zan\"; grep -n \"^zadan\\|^zan-\\|^zahr\\|^ozadan\\|^ōzadan\\|ozan\\|^wardag\\|^wārēn\\|nizand\\|^nizār\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD gaz\"; grep -n \"^gazidan\\|^gaz-\\|^gazand\" PHD.txt PHD_mackenzie.txt | head",
 "description": "Grep MacKenzie"
}
```


### [2026-09-06T14:57:03.786Z] TOOL RESULT

```
=== PHD zadan/zan
PHD.txt:515:nizārīh 61 0$
PHD.txt:4602:paymānag paui paymog paymoz- paymozan paymüdan padisay padist padiš
PHD.txt:4919:lawzēnag rūzīg rozwürag rozan ranjwar rozward rozgar ranjag, rozag rozbinag roz-Saban rosnih rēšn rūšnag rūšngar rodbar rodigan rodig 12го rüdan abàg! rūstūg
PHD.txt:5103:zahrag Kä: zāmyād YU g S zāmēn- - e$ zāmēnīdan Wes PAS zadan US zādag \зтеҳЅ zibāl NS S 1-1, zay- -aS zih AUS zi(w)- _ GAR zēnhār Sao «S
PHD.txt:5378:muy! Cst-! éstádant jagar ozan-t ózadant -gar dar, gar yal darr- draya dravābār dravāb draxt darāy
PHD_mackenzie.txt:2082:drozan [dlwcn l 1M, J drwzn] lying, liar.
PHD_mackenzie.txt:3882:ozadan,ozan- [YKTLWN-, YKTLWN-tn l < A 'yq#wn, ..J qtl; 'wetn' l
PHD_mackenzie.txt:4158:paymozan [ptmwcn l 1M pymwcn] garment, dress.
PHD_mackenzie.txt:4434:rozan [lwen ' IN,....,] window.
PHD_mackenzie.txt:5717:zadan, zan- [MHYTWN-tn < A.y mfz); ztn', zn- I M zdn, zn-, N ......]
PHD_mackenzie.txt:5721:zadan, zay- [YL YDWN-tn' < A "1/ yld; z)tn l I M z)d, z)Y-, N -] bear
PHD_mackenzie.txt:5738:zahr [z)hll M zhr, N ......] poison, venom.
PHD_mackenzie.txt:5739:zahrag [ze)hlk I N "'a] bile, gall.
PHD_mackenzie.txt:5759:zan-, -isn, v. zadan.
PHD_mackenzie.txt:6436:disquiet anastih.                       dress paymozan; v. garment.
PHD_mackenzie.txt:6545:excellence pAhlomih.                               falsehood drozanih, mihoxt.
PHD_mackenzie.txt:6664:fourth tasum.                                  paymozan, warr, wastar(ag).
PHD_mackenzie.txt:6965:lark cakok.                               liar drozan.
PHD_mackenzie.txt:7000:lineage gohr(ag).                        lying drozan; (prostrate) nibem.
PHD_mackenzie.txt:7142:mountain gar, kOf.                             needle sozan.
=== PHD gaz
PHD_mackenzie.txt:2496:gaz-, -isn, v. gazidan.
PHD_mackenzie.txt:2501:gazidan, gaz- [gc-, gz-ytn l I N -] bite, sting.
```


## [2026-09-06T14:57:14.640Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5735,5745p;3878,3890p;2495,2505p' PHD_mackenzie.txt\necho \"=== page markers near\"; awk 'NR>=5700 && NR<=5760 && /^[0-9]+$/ {print NR\": \"$0}' PHD_mackenzie.txt | head\ngrep -n \"^9[0-9]$\\|^10[0-9]$\" PHD_mackenzie.txt | sed -n '1,20p'",
 "description": "MacKenzie entries with context"
}
```


### [2026-09-06T14:57:16.179Z] TOOL RESULT

```
gaz [gc IN ......] tamarisk.
gaz-, -isn, v. gazidan.
gazag [gc'k ' ] biting.
gazar [g)cll N gazur] fuller, washerman.
gazdum [gcdwm I N kazdum!] scorpion; astr. Scorpio.
gazidag [gzytk ' I N gazid] poll-tax.
gazidan, gaz- [gc-, gz-ytn l I N -] bite, sting.
 -isn: biting.
geg [gdk I M gyyg] thief.
         '
gehan [gyh)n ' I = M, N gihiin, Jahan] world.
llwon ['wgwn' I M ))wn] as, so.
oy [OLE < A (l-h I M 'wy, N -] he, she, that; (pi. awesan).
·oyrist ['w(k)ylSt l = Av. awaoirifta-] a degree of sin.
oz ['we] strength, power.
ozadan,ozan- [YKTLWN-, YKTLWN-tn l < A 'yq#wn, ..J qtl; 'wetn' l
  M 'wzdn, 'wzn-] kill.       -
ozarak ['we'lk I M hwz'rk] little, small, few.
               '
ozomand ['we'wmnd] strong, powerful.



                                  p
zahag6mand [zhk)wmnd] pregnant, gravid.
zahar [zh)ll N ......] womb.
·zahih [zhyh] = zaha.
zahr [z)hll M zhr, N ......] poison, venom.
zahrag [ze)hlk I N "'a] bile, gall.
                        '
zaUig [ztwk I N zalU] leech.
                  "
zam [zm I P zmg] winter.
  C 6684                          H
zamAn                                                       zAylstan
=== page markers near
```


## [2026-09-06T14:57:24.667Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD w'rgn\"; grep -n \"w'r.n'k\\|w’r.n’k\\|wrgn\\|w'ryn'k\\|varghn\\|falcon\" SOD.txt | head -20\necho \"=== SOD_pages\"; grep -n \"w'r.n'k\\|w’r.n’k\" SOD_pages.txt | head",
 "description": "Grep Gharib Sogdian"
}
```


### [2026-09-06T14:57:24.744Z] TOOL RESULT

```
=== SOD w'rgn
49129:falcon 
57561:liking  hunting  with  falcon 
74533:9848  wVyn'y  =*  w'ryn'k 
74572:9855  w'ryn'k   B  <^jj0^j=*^ 
74577:falcon 
74610:9858  w'rpn'k  S 
86167:falcon 
89412:falcon    6154,9855,11501 
91315:liking  hunting  with  falcon     7406 
=== SOD_pages
32116:                                                               9848 wVyn'y =* w'ryn'k
32152:9843 w'pryt =* w>Pr>y5                                         9855 w'ryn'k     B                         <^jj0^j=*^
32175:9858 w'rpn'k S
```


## [2026-09-06T14:57:28.333Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '74565,74620p' SOD.txt\necho \"=== leaf of 9855 in SOD_pages\"; awk 'BEGIN{RS=\"\\f\"} /9855 w.r.n.k/ {print \"leaf(1-based)=\"NR}' SOD_pages.txt",
 "description": "Gharib entry 9855"
}
```


### [2026-09-06T14:57:29.952Z] TOOL RESULT

```
9854  w>r8-/t  ?   B  jji\>f<j*fid±*/ 
war6/t-  ? 

GcOturn 

Frag.  Len.  93,  8 

9855  w'ryn'k   B  <^jj0^j=*^ 
warayne  (w^yn'y)  ©Av.  vardYna-, 

Khwar.wVrnwib;  Oss.  uari\  Pahl.  varisak/varis 

falcon 

TSP  I3ii  14  n  p228;  SCE  359;  Ben  v.  Vxtra  et 


399 


wHmyc 


JVf-" 


•LP ji 


OJiyLS  tjjj  iQ^Jt'  <<j-*i  Jj 


VrOagna,  1934,  34;  Bailey.  Garutmant.  10 

9856  wVms-   M,  C  J^fljT 
warams  ©impf.  ^wrms- 

(to)become  quiet 
GMS  828;  C2,  12V28 

9857  w'rnmpy   C  ^ 
war-nampe   ©ace.  -nmpw 
rainwater 
C2,  94V22  pl77  n22 

9858  w'rpn'k  S 
fat,  heavy 
MDii  B-6  11R6  B-61,  3,  4$  MDii  pl30 

9859  w>ry    B,  C  ^  w>r>k 

9860  w,ry(,k)  S  ^ 
warik  ? 

chosen,  selected 
Mfiii  p214  n  p72 
=== leaf of 9855 in SOD_pages
leaf(1-based)=466
```


## [2026-09-06T14:57:44.995Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"1170\" POK_03.txt | head -5; echo \"---\"; grep -n \"Lamm'\\|,Lamm\\|Widder\" POK_03.txt | head -20",
 "description": "Find Pokorny 1170"
}
```


### [2026-09-06T14:57:45.059Z] TOOL RESULT

```
5882:1170  #
---
218:Ai.  dvi-  m.  f.  jSchaf,  avika-  m.  ds.,  avikä  ,weibliches  Schaf  (=  abg.  ovhcaY dvya-  ,vom  Schaf,  vgl.  gr.  ota;  arm.  hov-iio  (*oui-pa-)  , Schäfer';  gr.  5'tg,  olg (argiv.  Akk.  PI.  ofivg)  , Schaf ,  oXeog  ,vom  Schafe*,  ola,  Ba  , Schaffell',  dehn- stufig ^a  , Schaf  feil,  Saum'  (wie  ai.  ävika-  n.) ;  lat.  ovis^  umbr.  oui^  uvef  Akk. PI.  ,oves'  {au-huhulcus  ,pastor  bovum',  auch  avillus  ,Lamm',  s.  u.  ag^hnos)-, air.  öi  ,Schaf;  cymr.  ewig,  acorn.  eiihic  ,cerva'  {*oulkd)',  aisl.  «r,  ags. eowu,  eowe,  as.  ewi,  ahd.  ouioi,  o«  , Schaf  {^awl,  Gen.  *awjöz),  got.  awistr jSchafstall',  ags.  eowestre  ds.,  ahd.  awist,  ewist  (mit  zu  stä-  , stehen'  ge- hörigem 2.  Gliede  -sto-,  -s^[9]<ro-),  got.  atoepi,  ags.  eowde,  ahd.  ewü  ,Schaf- herde*;  lit.  avts,  lett.  avs  f.  ,Schaf*;  lit.  ävinas,  lett.  avins,  äuns,  apr. awins  , Widder'  =  abg.  ovh-m  ds.;  abg.  ovb-ca  , Schaf.
595:dazu  mit  Superlativsuffix  -temo-:  ai.  pratamäm  ,vorzugsweise',  av. fratdma-,  ap.  fratama-  ,der  vorderste,  vornehmste,  erste'  (daneben  ai. prathamd-  , erster'  und  einzelne  iran.  Formen  mit  th) ;  gr.  ^ngö-atog  (aus TTQÖzaTog?)  vielleicht  in  dor.  Ttgazog  , erster';  aber  gr.  TtgOJrog  ds.  aus *pf-to-  (umgebildet  aus  *pf-mo-  ds.);  dazu  rrgrjrrjv  m.  ,einjähriges  Lamm' (s.  oben  S.  314) ;
3772:alb.  shtjerre  ,junge  Kuh,  Lamm';
3774:•  got.  stairö  f.  ,unfruchtbar*,  ahd.  stero  , Widder';  mit  k-  erweitert  mndd.
4856:gr.  att.  ö-arrtü,  ion.  adaaio  {eaa^a,  ion.  saaaa]  iasadxccTo)  ,au8rütteiL bewaffnen ;  anfüllen,  feststopfen'  (*tuakiö),  uaycTÖg  ,vollgestopft',  mit  gr;  y (Entgleisung)  adyr]  , Rüstung,  Geschirr,  Sattel,  Kleidung',  ady^a  ,Deckt| Saumsattel;  Kleidung,  Überzug*  (>  lat.  sagma  >  ahd.  soumj  nhd.  SaumiUii^ Gayr^rr]  ,Fischernetz^,  GdyovQOV  yvgyd&iov  PoU.,  aayig'  nrjqa  Hes.,  und  thebaa. (TaxTög  ,Arzt*  und  das  dem  lat.  sa^ana  , Zauberin' zugrunde  liegende  *<Ta)i!ih«| arjy,ög,  dor.  Gaxög  , Hürde,  Stall,  heiliger  Ort' ;  orj-i^d^o)  ,pferche  ein,  sperrt ein',  dor.  oäviräg  ,in  der  Schäferei  aufgezogenes  Lamm',  cijx/g,  -Idog  »S^U* vin^;  auch  wohl  gtjköo)  , wiege',  Gri%wf.La  , Gewicht;  Gegenwert,  Belohnaii|'| mit  Abtönung  ö  wohl  hom.  Gajytog  ,kräftig,  stark*,  awxsa)  ,bin  stark,  DAbt Kraft';  schwundstufig  ovxvog  ,gedrängt,  zahlreich'  (*i;v'K-Gvog),  -^^  '
5886:Ueren-  ,Widder,  Schaf,  Lamm^
5887:Ai.   *uran-  (aus  *vuran-),  Akk.  *uranam,  Nom.  urä,  woraus  urana-  rn ,Lamm,  Widder',  urä  f.  , Schaf*,  dazu  urahhra-  m.  ,Widder'  für  *ura'bha' (wie  vrsabha-  zu  vrsan-);  vgl.  npers.  barra  (*varnak)  ,Lamm''  pehl.  varak ,Widder*;   iran.   värdn-jar-y    vär9-yna-    , Lämmerschläger'  (Humbach  DLZ 78,  299 f.);
5888:arm.  garn,  Gen.  garin  ,Lamm*;
5889:gr.  hom. X'F)ccQi^y,  Gen.  agvög  ,Lamm*,  kret.  J^agrjv]  auch  in  tsakon.  vanna aus  lakon.  J^aqviov  ,Lamm',  dazu  -J^qtjv  in  hom.  noXvQQrjv  ,schafreich*  daraus spät  qrjv)j  mit  Ablaut.  äqvsLÖg  ,Widder',  falls  nicht  eher  aus  *äQ0vEi6q  (*aQijy^ rjfoq)  zu  Ixqariv  , männlich'  (oben  S.  336);
5891:unklar  als  Ableitung  lat.  vervex^  -ecis  (-Ix,  -Icis)  , Hammel*;  unklar  ut auch  das  Verhältnis  zu  den  auf  *enio(s)-, Wolle'  rückführbaren  gr.  Worten slqoq  n.  , Wollfließ',  abgeleitet  eYqlov,  att.  eqlov  , Wolle',  att.  e^eqog^  st%^^ ,schönwollig',  äol.  en-eqog  ,Widder'  (, worauf  Wolle  ist*),  ion.  elgtrsogf  att. iQlveog  ,von  Wolle';  anlautendes  /  lässt  sich  nicht  nachweisen.
5967:got.  wiprus  jjähriges  Lamm*,  aisl.  vedr,  ahd.  widar  ^Widder'  (vgl.  oben ai.  sa-vätdräu)]
```


## [2026-09-06T14:58:25.274Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v1 leaf for p.324 (بهرام)\"; awk 'BEGIN{RS=\"\\f\"} /بهرام/ {print \"leaf1b=\"NR}' BQT_v1_pages.txt | head -20\necho \"=== v1 اوژدن\"; awk 'BEGIN{RS=\"\\f\"} /اوژدن|اوژنیدن|اوژندن/ {print \"leaf1b=\"NR}' BQT_v1_pages.txt | head\necho \"=== v1 انگژه\"; awk 'BEGIN{RS=\"\\f\"} /انگژه|انگژد/ {print \"leaf1b=\"NR}' BQT_v1_pages.txt | head",
 "description": "Locate BQT vol1 headwords"
}
```


### [2026-09-06T14:58:27.007Z] TOOL RESULT

```
=== v1 leaf for p.324 (بهرام)
leaf1b=19
leaf1b=40
leaf1b=114
leaf1b=218
leaf1b=223
leaf1b=224
leaf1b=232
leaf1b=266
leaf1b=417
leaf1b=439
leaf1b=469
leaf1b=538
leaf1b=545
leaf1b=546
leaf1b=567
leaf1b=601
leaf1b=618
leaf1b=653
leaf1b=685
=== v1 اوژدن
=== v1 انگژه
leaf1b=394
```


## [2026-09-06T14:58:32.207Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## LEAF 394 (p.175?)\"; awk 'BEGIN{RS=\"\\f\"} NR==394{print}' BQT_v1_pages.txt | head -60",
 "description": "BQT v1 p.175 angžeh"
}
```


### [2026-09-06T14:58:33.912Z] TOOL RESULT

```
########## LEAF 394 (p.175?)
مردم فررنگ «م هست ٩‏ ۰
الث و زای قطه‌دار ساکن » سلی باشد که بآن
زمن را هموار ساز ند ۹
انگز ح بفت اول و خم نالث: و کت
تابی و زای فارسی» آهنی باشد سر کج که فیلرا
بدان بهرطرف که خواهند بي‌ند .
انگژ د ۴ ختح اول دضم ثالث‌وسکون
انی و فتح زای فارسی ودال ابجد -اکن مطلق
صعفها را گویندعموعاً و صمفی باشد بغایت‌بدبوی
و آترا پعربی حلتیت خوانندو آنرا انگژدیسب
آن گون که سمغ درحت انگدان است و ال
آن انگدان ژد باشد بفتح زای فارسی چه ژد
بلفت فرس بمعنی صمغ است و آن گرم و خشكت
است در درجه سیم .
انگز لك . بازای هوز بروزن مرجمك ,
کجك فل را گونند و آن آلی باشد سر کج از
آهن که فیلبانان فیل رابدان بپرطرف که‌خواهند
برند . و بازای فارسی هم بنظر آهده است :
اآلگژ واه بکس نات و سکون زای
فارسی و واو بالف کشپده‌بروزن »نزل‌ها. جابی‌را
کودت که شنها گوتفندان زا چر ادا تک
دارند - و کوسفندانرا نیز گفته‌اند - ویمعنی‌دانه
و ختَهةٌ میوه ها هم آهده است .
انگشت برچشم نفادن
۱ نگژه ‌ ح با زای فارسی مفتوح‌بروزن
خربزه , مخفف انگوژه است که صمغ درخت
انکدان باشد و آلرا عربان حلنیت و شیرازبان
انگثت گنده ( ۱ ) کوند. و با زای هوز نیز
ال اسگ:
ا نگسبه بفتح اول والت و سکون‌انی
و سین بی قطه و فتح بای ابجد » برزیگربرا
گویند که صاحب سامان بود وکار کنان وزراعت
کاران ببار داشته باشد .
انگشبه - با شین نقطه دار . بر وزن
و معنی انکته کت که مرن وا اسان
باشد - و سودا کر صاحب مابه را نیز گفه‌اند.
انگشت؟ - بنم اك , ممروضت که
عربك از انگشتان دست و بای باشد - و بکس
ثالت زغال را گوند که اخگر کشنه شده است.
انگشتال * ه یکی تاك , فوفانی بالف
کشبده و لام سکن , مردم‌شمیف و نحیف وعلیل
ویارنا وصاحب تقاهت راگونند .<
انگشت بد ندان گز بدن - کناه
ازنه‌جب کردن و نحیر نمودن باشد - و حسرت
و اقوی خوردن را نیز گوبند .
انگشت بر چشم نهادن د کاب
ازقبول کردن ومسلم‌داشتن باشد, وانگثث بر دیده
۳ ۳۳ رلك؛ انگود.
```


## [2026-09-06T14:58:49.005Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v2 زهر / زدن leaves\"; awk 'BEGIN{RS=\"\\f\"} /پادزهر|پازهر/ {print \"leaf1b=\"NR}' BQT_v2_pages.txt | head\necho \"--- زدن\"; awk 'BEGIN{RS=\"\\f\"} /^.*زدن/ {c++} END{}' BQT_v2_pages.txt\nawk 'BEGIN{RS=\"\\f\"} NR>=460 && NR<=468 {print \"==LEAF \"NR\"==\"; print substr($0,1,300)}' BQT_v2_pages.txt",
 "description": "BQT vol2 around p.1007"
}
```


### [2026-09-06T14:58:50.711Z] TOOL RESULT

```
=== v2 زهر / زدن leaves
leaf1b=450
leaf1b=462
leaf1b=511
--- زدن
==LEAF 460==
 ‫زاغ یا‬                                                                                                                   ‫‪66‬‬      ‫ی‬

‫رارال ه با زای هوز بورزن آغال »‬                                   ‫کوبند ‪ , ۱‬و آن بار �
==LEAF 461==
 ‫پر هه‬
                                                                           ‫کنایه ازطعنه وسرزش باشد ‪.‬‬

 ‫ز‬
 ‫یر‬‫چ ه‬
     ‫» بچ‬         ‫ق‬
                  ‫ازن‬
                    ‫راق ‪ - ۴‬بسر �
==LEAF 462==
 ‫زامیاد‬                                                                                                     ‫تس‬

‫رال مستحاضه ‪ - ۴‬بعنی زالعفيم‬                                       ‫رال ابرو = کنابه از آسمان است‬
         
==LEAF 463==
 ‫—‬           ‫‪۵ ۵ 6‬‬




     ‫مخفف زدآوتر امت که انزاطرف ترباشد‪#*.‬‬                              ‫نام روز ست‬         ‫کشده و بدال ایرد زده )‪۰ (۱‬‬

‫زانو رصد اه کردن = کنابه‬     
==LEAF 464==
‫زاولایه‬                                                                                     ‫ات‬   ‫او‬




‫زاور فتراش * ‪ -‬بنتح ف واسکون‬                             ‫بارچه و لیم‬   ‫وهبمعتی خشت‬   ‫کوه را نی
==LEAF 465==
   ‫و ‪ ۵‬ات‬
                                                                                                      ‫زاووش‬

  ‫راهد حخك د کنابه از زاهدی‬                           ‫است که‌برپای‌ستوران و بکزپرابان گذار�
==LEAF 466==
   ‫زنباکنسكت‬                                                                            ‫و و ات‬    ‫تم‬




                                                   ‫زان ‪ ۱‬ب»فتم اول معروف است ‪۴‬‬
‫و سخن گوی باشد ‪ -‬و شخ
==LEAF 467==
    ‫ات‬                                                                                                            ‫ِ‬
‫ر بر جد ‪ - ۴‬لوعی اززمرد باشد‪ .‬وآن‬
‫از جملهٌ جواهراست وطسمش سرد وخشك است‬
                     
==LEAF 468==
                                                                                           ‫و‬   ‫ی‬




‫بیز کوبند ‪ -‬ویضم اولخریداری باشدکه چیزها‬          ‫کاف فارسی » بروزن ومعتی زبغر است که زبلغ‬
 ‫شتر�
```


## [2026-09-06T14:59:04.578Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=468 && NR<=476 {n=split($0,a,\"\\n\"); print \"==LEAF \"NR\" (p.\"NR+543\")==\"; print substr($0,1,700)}' BQT_v2_pages.txt",
 "description": "BQT vol2 leaves 468-476"
}
```


### [2026-09-06T14:59:06.182Z] TOOL RESULT

```
==LEAF 468 (p.1011)==
                                                                                           ‫و‬   ‫ی‬




‫بیز کوبند ‪ -‬ویضم اولخریداری باشدکه چیزها‬          ‫کاف فارسی » بروزن ومعتی زبغر است که زبلغ‬
 ‫شتربراکوبند‬     ‫ی‬
                 ‫بدر‬
                   ‫‪-‬و‬‫عردر‬
                        ‫را برغبت نمام بخ‬          ‫باشد آونرا آیوق نکیوزبند (‪)۱‬؛ وبکر اول‬
                                                  ‫وفتح‌ انی و ضم‌کاف تازی دز کفته‌اند ؛ و ماکاف�
==LEAF 469 (p.1012)==
                                                 ‫بیان سوم‬
                     ‫در زای نقطه دار باجیم مشتمل بر چپار لغت‬

                     ‫عنکبوت را گویند ‪۱‬‬       ‫مال‬        ‫* رج ‪ -‬بضم اووسلکون انی » تیر‬
                                                                        ‫پرتاب‌باشدکه پیکانآ براازاستخوان‬
‫رجمول ‪ -‬با میم بر وزن معقول ‪.‬‬
                                                                        ‫فیل وشاخ‌قوج کواومیش وامثال آن‬
‫حبی امت دوابی و 
==LEAF 470 (p.1013)==
 ‫زدن‬                                                                                ‫و ‪—| ۵ ۵‬‬




‫چویکی باشد که سنادزهابدان سازنوازند ویعربی‬                                  ‫درخت رگاوند ‪۶.‬‬
                              ‫مراب خوانند ‪.‬‬      ‫زخم بریان س بمعنی دم پفت است‪.‬‬
‫رخناره ‪ = ۴‬بانون پروزن انگاره »‬                                      ‫‪۱‬‬   ‫وآن طعامی باشد معروف‬

      ‫بمعنی زخاره است که شاخ درخت باشد ‪۰‬‬         ‫زخم ناخ د بمنی �
==LEAF 471 (p.1014)==
‫—‬        ‫‪۵۵‬‬
                                                                                                      ‫زدوار‬

‫ردو نتن ‪» ۴‬با نون و تای قرشت مر‬                          ‫وجماغ باشد‪ -.‬و چون مرکب شود معنی بیار‬
‫وزن سبوشکن » بلغت زند و یازند (‪ )۱‬بمعنی‬                                                       ‫اهل‬         ‫دارو‬
                                       ‫خریدن باشث ‪.‬‬
                                                          ‫= بر وزن ومعنی‌جدواراست‬         ‫ردوار‪
==LEAF 472 (p.1015)==
 ‫زراوند‬                                                                                                       ‫ت‬
                                                                                                              ‫اهن ‪۵‬‬‫‪-‬‬



          ‫و نام مبارزی از اران بوده ‪.‬‬            ‫نود ‪7‬‬        ‫رراتشت ‪ ۱‬س نم فوفالی ‪ ۰‬زردشت‬
‫رراعش؟ = باغین قطه‌دار(‪ )۲‬بروان‬                              ‫راکوبند ‪ .‬وکیشآتش پرستی را او بهم‌رسانید؛‬
‫را‬   ‫زمین سخت‬    ‫و‬    ‫ي�
==LEAF 473 (p.1016)==
    ‫—‬        ‫)‪0‬‬
                                                                                                                       ‫زراوه‬

 ‫ونفس ناطفه ‪ -‬و عقل فلك عطارد ‪ -‬ونورمجرد‪-‬‬                                 ‫تام خوای ابت که آن دونوع میباشد ‪ :‬یکی‬
        ‫وعفل فعال ‪ -‬ورب‌النوع انان وراست کوی‬
                                                                          ‫را زراوند طوبل میگوبند یمتی‌دراز وآترا شجرة‬
‫رالیز گوبن دکه‬               ‫ورردشت‬        
==LEAF 474 (p.1017)==
       ‫زردشت‬                                                                        ‫‪۱‬‬

                            ‫ابتاده عبادت کرد ‪۰.‬‬                             ‫وغش راکونند ‪#. ۱‬‬
  ‫زرد خی بفتح اول وخای نقطه‌دار بر‬                ‫ازرداب ‪ - ۲‬بارالابجدبروزن غرقاب»‬
  ‫وزن مردرو » دام کیاعی است که بشتر در باغات‬      ‫نخالمطی است که بعربی صفرا کوبند ‪ -‬و آبی‬
                ‫روید و کلی زرد وخوشبوی دارد ‪.‬‬     ‫ککهااجزکیلره بوقت
==LEAF 475 (p.1018)==
 ‫ات‬                                                                                     ‫زردشت‬

‫زردشت بز رگ ‪ -‬بازن‌پهلوی دام‬                     ‫دين تش برستی رایهم رالد واحوال او درلغت‬
                                                 ‫زارتشت ييتهفصب لهذ کورشد‪ .‬وبعضی گویند رردشت‬


                           ‫بزبان سربانی ‪*. ۴‬‬     ‫بزبان سریانی نام‌ابراهیم علیه‌اللام است وبعضی‬
‫رردك ‪ = ۴‬بفتح اول وثالث وسکون‬                    ‫ویرزین هر دو ام�
==LEAF 476 (p.1019)==
   ‫تی‬
    ‫ده‬‫رش‬
       ‫ح‬ ‫ز‬                                                                                                ‫‪-۱۰۱۳-‬‬
‫زر دهشت * ‪ -‬سم اك و سکون‬                               ‫و معرب آن جزراست‪ - ۱‬و مصفر زرد همهت‬
‫و هاو شین و تایقرشت» همان زرتشت آتش‬                   ‫وآن رنگی باشد معروف ‪ -‬و آب زعفرانرا نیز‬
                                                      ‫‪ -‬و ممعنی زرتك همآ مده است که‌آب‬                           ‫کو ند‬
```


## [2026-09-06T14:59:20.081Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==470{print}' BQT_v2_pages.txt | tail -40",
 "description": "BQT vol2 leaf 470 full"
}
```


### [2026-09-06T14:59:21.607Z] TOOL RESULT

```
                                                       ‫در زای نقطه دار با دال بی‬
‫بکر اول بر وزن جگر »‬          ‫ردر ‪= ۴‬‬            ‫ردای‪ = ۴‬بکر اول بر وزن فزای »‬
             ‫زدابنده و پاکیزه کننده را گویند ‪ -‬وامر | بمعنی درخور راق وسزاور باشد ‪.‬‬
‫رشن * = بروزن‌بدن‪.‬عمروف است ‪١-‬‏‬                  ‫بابن معنی هم هت بعنی بزدای وپاکیزه ساز‬
‫وکنابه از چیزی خوردن ‪ - ۷‬و مباشرت کردن‬           ‫و زدایدن وصان کردن وبا کیزه ساختن باشد ‪.‬‬

                                              ‫‪۰‬سوند اسم آلت) ‪:‬‬
                                                             ‫‪ -‬از ‪ :‬زخم (پ‬
    ‫رکه بدر آوازش‪.‬‬
                 ‫ناخوشتر از آواز‪ :‬م‬               ‫کفتی رکه جان میگلد زخمه‌ناسازش‬
  ‫«کلتان ‪۲۷‬‬
               ‫رك ‪ :‬از در ‪.‬‬    ‫‪۴‬‬        ‫رك ‪ :‬زدودن ‪.‬‬     ‫‪۴‬‬        ‫‏‪e‬‬
 ‫‪-‬هلوی ‪ 12122‬و ‪ 02682‬از رة ابرانیقدیم ‪. 2421 . [02 -‬ار ‪nag‬‏‬        ‫پ‬
 ‫که ‪ ۸۵۲‬بارسی‌باستان ر‪٫‬عةٌ‏ ‪ 0712032 ۰ [12-‬ک(شتن)‪ .‬هندی‌باستان‬
                                                             ‫د بارتولمه ‪ ۰۹4‬نربب‬
  ‫رثة ‪ ( 4261 . 022 -‬مضروب کردن‪ .‬کشتن ) قس‪ :‬ارمنی ‪( 028‬ضرب ‪ .‬تادب) و‪۳۳6088‬‬
 ‫(مضروب کردن ‪ ,‬كتك زدن) » کردی ‪( 8106012‬زدن (آش)‪ .‬تیر الداختن)» افقانی‪۵۷ |۳202-‬‬
 ‫‪ ..4‬بلوچی ‪ [8202‬و ‪. [18202‬ع ‪ 82022‬ر ‪ . 0821022‬شغنى ‪"1Z - 0۳2‬‏ ‪,‬سریکلی‬
 ‫[‪ « 1۷‬اسنق ‪ ۳۹۰۰‬طبری ‪ ( 20- 72112‬زدن ) « ساب طبری‬                  ‫‪0-102‬‬
                                                                        ‫و ‪12‬‬       ‫‏‪0-2am‬‬
                                                                                      ‫‪2‬‬
  ‫‪ -‬کوفتن» وارد آوردن‌صدمه‪,‬‬             ‫)‪( 2022-80 .‬بزند) ‪.‬‬        ‫ن‬
                                                                   ‫د(‬‫ز‪06‬‬
                                                                       ‫‪» ۶‬گیلکی ‪62‬‬
   ‫‪۳‬ه*‪.‬‬
      ‫ات»ن«‬
          ‫سراتکف‬
               ‫ل‌چ‬
                 ‫ضرب ‪ « :‬ملك فرمود بنزدش (شیاد را ) وفی کنند تا چندین دکرهم‬
                                    ‫‪ -‬اکنونکوبند ‪ :‬کیلاسی( مشروب ) بزیم ‪.‬‬
 ‫‪.‬هلوی ‪ 01522‬ب‪2‬ا‪. 01012‬کردی واففانی ‪ ۰ 0122‬بلوچی‬
                                               ‫اول پ‬                     ‫فمت‪-‬ح‬
                                                                             ‫بزخ‬
                                                                               ‫‪#‬‬
‫‪ 0‬و ‪( 7182‬شمشیر) «استق ‪ ۲04‬ورك ‪ :‬هوبشمان ابضاً ‏ گیلکی ‪ 00122‬؛ جراحتی که‬
                                ‫بوسیلةٌ آلات جارحه با ناخن ودتدان ومافند آن بهم رسد » رش‪:‬‬
         ‫‪.‬‬   ‫که تماید بچشم همردم دوست‬                        ‫ر خم دادان دشمتی شرت‬
 ‫«کلتان ‪۰۲۱٩‬‏ ‪.‬‬
                                               ‫‪ -‬ضرب ‪ ۰‬صدحه ‪ -‬شکستگی ‪ ۰‬کسر‬
```


## [2026-09-06T14:59:40.555Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=502 && NR<=512 {print \"==LEAF \"NR\"==\"; print substr($0,1,200)}' BQT_v2_pages.txt",
 "description": "BQT vol2 zahr region"
}
```


### [2026-09-06T14:59:42.038Z] TOOL RESULT

```
==LEAF 502==
                                                                                                  ‫‪ ۳۵‬پات‬
 ‫زن‌فعل‌سبز چادر » کنابه ادزیا‬               
==LEAF 503==
   ‫‪ ۵‬اس‬   ‫و‬




 ‫زگله * ‪ -‬بفتح اولوآخ رکهلام باشد‪.‬‬
                                 ‫ن‬                          ‫واکفرا‬
==LEAF 504==
                                                                                                 ‫—‬    ‫‪64 ۱‬‬   ‫س‬




‫و دیات را همگفته‌اند ‪ -‬وبم�
==LEAF 505==
                   ‫وبفتح اول نام داروبی است که‬                  ‫خادم راکوبند عموماً وخادم بیماران وزنداتیانر‬
                  
==LEAF 506==
  ‫زورق‬                                                                                                    ‫ت‬
                                                                           
==LEAF 507==
 ‫‪٩۰ 6‬‬                                                                                              ‫زور زرین‬
 ‫وغرورباشد واین‌لفت‌را درفرهنگه 
==LEAF 508==
  ‫زوترگ‬
                                                                                                               ‫ات‬   ‫ی و ه‬




 ‫و صندوق‬        ‫زور�
==LEAF 509==
‫—‬        ‫‪4 6٩‬‬
                                                                                                               ‫زو‬
‫دیگر وعربان کربه خوان�
==LEAF 510==
  ‫زحراوی‬                                                                                               ‫پات‬
 ‫زهدآن * ‪ -‬بچهدان و قرارکله نطنه‬
    
==LEAF 511==
  ‫‪— ۱‬‬   ‫‪4‬‬    ‫س‬
                                                                                                                    ‫زحرنار‬
‫رهرة می
==LEAF 512==
                                                                                              ‫ات‬     ‫‪0‬‬


‫ودرا دجاگنجی است و من برآن اعتماد دکردم�
```


## [2026-09-06T14:59:44.713Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==511{print}' BQT_v2_pages.txt | head -60",
 "description": "BQT zahr page"
}
```


### [2026-09-06T14:59:47.094Z] TOOL RESULT

```
  ‫‪— ۱‬‬   ‫‪4‬‬    ‫س‬
                                                                                                                    ‫زحرنار‬
‫رهرة میق = کنابه از قطرات باران‬                                     ‫هر باد = بفتح اول وسکون‌الیوثاكت‬
                                                   ‫است ‪.‬‬           ‫و بای ایجد (‪ )۱‬بالف کشیده وبدال زده »یمعتی‬
                                                                   ‫بزاهدر است ‪٩‬‏ ‪ ۰‬و آن مرضی باشد که بعربی‬
 ‫و واو بالف کشیده » خوش خوان و خوش‌الحان‬                                                              ‫خناق گوبندش ‪.‬‬
                                           ‫‪.‬‬     ‫را گوینه‬          ‫ر هر حند = خنده‌ای رگاویند که از‬
 ‫رهز اك * ‪ .‬بروزن بهزاد‪ .‬به‌عنی نسل‬                                                   ‫روی قهر وعضب وخعالت کنند‪.‬‬

                                           ‫وفرزند باشد ‪.‬‬           ‫ز هر خود بکسی ر بختن ‪ -‬کنابه‬
 ‫مگمن اول و ثانی وسکون‬        ‫=‬
                                                                    ‫قهروغضب خودرا تمام‌صرف‬           ‫کتسکه‬
                                                                                                     ‫ی‬   ‫از امن اس‬
 ‫ززههواب و چشمه‬                            ‫شین نقطه‌دار ‪.‬‬
 ‫مدن آب از چشمهباشد‬
                  ‫ودءوضع جوشیدن وآبر‬                               ‫رهر دادو ‏ زهر معلوم است » با‬
                        ‫‪.‬‬   ‫هم هت‬          ‫ولسسن‬         ‫وصفت‬      ‫دال ابجد بالف کشیده و رای قرشت بواو‬
 ‫دم وفقس ر‬       ‫هشت ‪ -‬بروزن بهشت ‪.‬‬
                                  ‫ر‬                                 ‫فاد زهر‬     ‫ومریی‬
                                                                                    ‫رسیده ‏‪ ١‬پازهر را گونند ‪:‬‬
                                                         ‫کو‬
                                                                                                                      ‫خواندد‬

‫رهك ‪ = ۲‬بفتح اول‌وسکون‌نانیو کاف؛‬                                  ‫رهر کر دن ‪ -‬کنابه از تلخ کردن‬
‫شیر زنان وشیر حیوانات نوزابیده باشد و آهرا‬                                                    ‫عیش است‬
 ‫آغوز وفله بگیوزبند وعربان لباء خوانند بکسر‬                         ‫رهر گا = یکرکاف فارسی ‪ ۰‬گیاهی‬
‫کشیده ‪ -‬و در عربی‬           ‫لام و بای ابجد بالف‬                     ‫ت که هر کس اندکی از آن بخورد فی‌الحال‬
 ‫جستن باد سخت باشد ‪ ۰ ۸‬وبکر اول‌هم‌درست‬                                                                        ‫«لاگ گردد ‪.‬‬
                                                     ‫‪.‬‬    ‫است‬
                                                                    ‫ر هر مهر ه = مهره‌ای باشد که بدان‬
 ‫که‬         ‫آلس»ت‬
                ‫‪-‬کر ار‬
                     ‫رهکو نی ‪,‬‬                                                        ‫دفع زهر افعی وغیزه کنند‬
 ‫پشت بای خودرا بضرب وزورهرچه تمام "ر‬                                ‫بفتح اول بروزن بهره؛پوستی‬         ‫زرهره =‬
                        ‫‪.‬‬   ‫رنف‬                ‫ا‬
                                               ‫‪۰‬‬
                                                                   ‫آدمی و حدوانات دیگر‬            ‫ناد پرآب که ‪3‬‬

 ‫فص وف‬       ‫= بروزن د لک‬         ‫‏‪٩‬‬       ‫زهگر‬                     ‫چسیده امت ‪ - ۴‬و کنابه از دلبری و شداعت‬
 ‫انت‪ :‬وآن انگشترمانندی باشف ازشاخ‌واستخوان‬                           ‫بود ‪ -‬وبمعنی شکوفه عربی است ‪ -‬و چامول‬
 ‫و کنابه‌ازفرح‬    ‫وغره که در انگشت ابهام کنند ت‬                        ‫ستاره امت معروف که آ را زاهد خواند ‪۴‬‬
                                  ‫‪. ۶۲‬‬         ‫زنان هم هت‬
                                                                    ‫زهرة تست بفتح‌اول‪ ,‬کنایه آازروشنی‬
 ‫نم اول وسکون ثانی و هیم '‬             ‫=‬       ‫رھم‬                                                                  ‫شب باشد‪.‬‬
                                                                                                ‫(‪ )۱‬چك ‪- :‬‬
   ‫‪ 8‬طایفةٌحکمامتفق شدند که‌مر ین دردرا دوابی‌یست مگر‬                      ‫‪۲۳‬‬            ‫‪.‬‬   ‫رك‪ :‬بادزهره‬   ‫‪-‬‬    ‫‪۱‬‬


   ‫‪( - ۴‬عر) «زهره بم اولرفتح الی وهمچنن سکون دوم ‪۰‬‬                                       ‫زهرةآدمی‪« € .‬گلستان» ‪.4‬‬

        ‫چه ستارگزهره ربةالنوع خنیا کرت‬                     ‫‪۴‬‬          ‫ستارةآسمان‌سوم_وشکوفه» « منتهی الارب» ‪.‬‬
      ‫‪ - ۱‬اسم مصدر از «زهیدن»‪ .‬ورك نزهاب‬                             ‫ژه (‪.‬م‪ ):‬ا زارد (زادن) ‪۰‬‬          ‫ار‬
   ‫‪ « _- ۸‬زهکت الریح الارض » برد‬                                ‫‪ - ۷‬از ‪ :‬زه (ه‪.‬م‪( ۲-2 ).‬پوند سیت) ‪.‬‬
      ‫‪ - 4‬افتانی]‪ « 18012‬هوبشمان ‪ .)¥۷۷0‬رك‪ :‬زه‬                                ‫* ‪.‬‬   ‫ویرانبد باد خاك را » «منتهی‌الارب‬


                                                                   ‫از‪ :‬زه (ه‪.‬م‪ + ).‬کیر(گیرنده)‪.‬‬            ‫‪- ۶۰‬‬
```


## [2026-09-06T14:59:56.176Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==510{print}' BQT_v2_pages.txt | tail -35",
 "description": "BQT p.1047 zahr"
}
```


### [2026-09-06T14:59:57.946Z] TOOL RESULT

```
                                                                                      ‫کرر‬
                                                                                        ‫زه ب‬
                                      ‫از اطباست ‪. ۸‬‬                                                          ‫باشد ‪.‬‬


                                               ‫(‪ )۲‬چك ‪ :‬ها ‪.‬‬              ‫(‪ )۱‬چك ‪ - :‬قطه دار ‪.‬‬

                                                                                     ‫‪ ۱‬رك ‪ :‬زهشس‬
               ‫زه‌آبی بدون آندرون سهمگن‪.‬‬                               ‫‪ - ۴‬سوی رود بکااروالیگشن‬
       ‫دلخت فرص ‪٤‬‏‪.¥‬‬    ‫ابوشکوربلخی‪.‬‬


                                                 ‫بلگد ناف وزهارهمه (انگور) از من ربد‬
   ‫‪.‬‬      ‫‪۱‬‬   ‫دامغالی‬    ‫«مسوچهری‬       ‫بردش غشبی‪.‬‬     ‫اندرشده‬        ‫که از اشان س‬

   ‫شهنشاهعالم زحازه گرفت‪.‬‬           ‫بشادی مکی‌الجمن‌برشگفت‬             ‫‪( ۱‬واسطه) ‪ +‬زه‪:‬‬      ‫‪ ۴‬از‪:‬زە‬

       ‫«لخت فرص ‪۹*۵‬‬     ‫فردوسی‌طوسی‪.‬‬


           ‫‪ - ۱‬درزبان کنوبی«زه زدن»‪.‬‬               ‫_ از ‪ :‬زه (ه‪.‬م‪٣+ ).‬‏ دان (بوددمان) ‪.‬‬
   ‫‪ - ۲‬پپلوی ‪ . 7022‬ارمنی ع ‪ 7013012‬ازابرالی باستان ‪ * 2۳048 -‬از ‪( 8‬زدن»‬
                                          ‫‪7۲‬‬    ‫‪, ۳12012 ,‬‬    ‫کردی ‪۲0۳4۳2‬‬      ‫‪۰ ۲‬‬    ‫) « نیبرکه ‪۰۵۲‬‬        ‫کشتن‬
   ‫‪.‬‬    ‫‪ ,‬افنانی » بلوچی ع ‪7022‬‬

   ‫رك‪ :‬اسشق » هویشمان ‪ ۰ ۸۷۱‬گیلکی یز ‪ « : 70122‬وییماربهای‌باريك را منفمت دهد (شیر)‪...‬‬
                                     ‫ی‬                                      ‫یا‬

  ‫‪ -‬ایوالقاسم زهراوی خلف‌بن عبای قرطبی " درتاریخطب بزر کتررین نماینده وممرف‬
   ‫‪ .‬مولداو زهرا محلی درجوار قرطبه است و اودرفرن پنجم ميزسته‪ ..‬وی‌همهٌ‬                       ‫است‬           ‫ی‬

   ‫آثار خودرا درمجموعه‌ای شامل سی کتاب ينام » التصریف‌لمن عحز عن‌التالیف» گرد آودده است ‪.‬‬

                                                                             ‫ابوالقاسم زهراوی‬      ‫نامه‪:‬‬   ‫لب‬   ‫رك‪:‬‬
```


## [2026-09-06T15:00:20.048Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=136 && NR<=137{print \"==LEAF \"NR-1\"==\"; print}' POK_02.txt | grep -n -A6 -B2 \"jatu\\|Lack\\|Harz\" | head -40",
 "description": "Pokorny 480 gwet- resin"
}
```


### [2026-09-06T15:00:21.474Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:00:24.684Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"jatu\\|Lack,\\|bitümen\\|bitumen\" POK_02.txt | head -10; echo \"---\"; grep -n \"^  480\\|^480\" POK_02.txt | head",
 "description": "Find Pokorny gwet- resin"
}
```


### [2026-09-06T15:00:24.738Z] TOOL RESULT

```
2077:lat.  hitümen  .Erdharz.  Erdpech'  (osk.-umbr.  oder  kelt.  Lw.);  hetulla] .Birke'  (gall.  Lw.).  mir.  be(i)the  (*betu{a)  .buxus'.  cymr.  bediv  (*het'Uäy .betula'.  corn.  bedeiven  .populus'.  bret.  beziien  .betula'  (benannt,  weil  .bitumen] ex  ea  Galli  excoquunt'.  Plinius  NH.  XVI  75);
---
2062:480  9
```


## [2026-09-06T15:00:27.384Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2062,2085p' POK_02.txt",
 "description": "Pokorny p.480 context"
}
```


### [2026-09-06T15:00:27.423Z] TOOL RESULT

```
480  9
vorliegt  (Pedersen  IF.  5,  47 ;  vielleicht  als  ""ged-s-os  zum  allerdings  nag Herten  lit.  gaüdinu-,  -inti  ^schrecken^,  üsi-gq,stü,  -gandaü  'gq.sti  ,erschreckei intrans/,  Ugqstis  .Schrecken',  Scheftelowitz  IF.  33,  155).  Ob  hierher  kelj Häs-  .sterben'?  (s.  unter  g'^em-,  g'^ä-  .gehen,  kommen');
unsicher  ist  Verwandtschaft  von  ahd.  quist  L  .Verderben.  Vernichtuii« als  *g^es-ti-s  .*Erlöschen'.  wovon  got.  qistjan,  fragistjan  .verderben,  trans/, fraqistnan  .verderben,  intrans.'.  ahd.  ßrquisten  .verderben,  trans.'.
WP.  I  693.  Trautmann  86.  Feist  388  f.
gues-,  guos-,  gus-,  erweitert  guoz-do-  .Gezweig.  Laubwerk'. Norw.  dän.  kvas  .kleine,  abgehauene  Zweige';
1.  mit  -d-Er Weiterung:  '* alb.  gQ^.  ghethi  .Blatt',  tosk.  gjethe  .Laub.  Zweig'  (kollekt.  PI.  zu  einem
Sg.  *gath  aus  *guozd-)]
ahd.  questa  f.,  mhd.  queste,  koste,  haste,  quast  m.  f..  .Laubbüschel, Sprengwedel.  Besen',  nhd.  Quaste  f..  asächs.  quest  .Laubbüschel',  aschwed. kvaster,   koster,   schwed.   qvast,  norw.  dän.  kost  .Laubbüschel.  Reisbesen*;
aserb.  gvozd  m.  .Wald',  apoln.  gicozd  .Bergwald',  gozd  .dichter  Wald',  usir.;
2.  mit  -f-Erweiterung:
gr.  ßöaTQvxog  .Haarlocke.  Geringel';
3.  mit  -p-Erweiterung: ai.  guspitd-  .verflochten,  verschlungen'; lat.  vespices  PL  .dichtes  Gesträuch';
mndl.  quispel,  quespel,  mnd.  md.  quispel  .Quast.  Wedel'. WP.  I  644  f..  Berneker  365.
1.  g^et-  .Harz'.
Ai.  jdtu  n.  .Lack.  Gummi' ;
lat.  hitümen  .Erdharz.  Erdpech'  (osk.-umbr.  oder  kelt.  Lw.);  hetulla] .Birke'  (gall.  Lw.).  mir.  be(i)the  (*betu{a)  .buxus'.  cymr.  bediv  (*het'Uäy .betula'.  corn.  bedeiven  .populus'.  bret.  beziien  .betula'  (benannt,  weil  .bitumen] ex  ea  Galli  excoquunt'.  Plinius  NH.  XVI  75);
ags.  hwit  cuidu,  cweodo,  civudu  .mastix'.  ahd.  cuti  .gluten'.  mhd.  kiitef] küt,  nhd.  kütt,  kitt  .Kitt';  ablautend  anord.  kväda  t  .Harz',  adän.  kvadej\ norw.  dial.  kvcede  .Birkensaft',  norw.  koda,  kvceda  .Biestmilch'.
WP.  I  672.  WH.  I  112.
2.  g^et-  .reden,  sprechen'.
Ai.  gadati  .sagt'  (falls  durch  analog.  Einfluß  aus  *gdtati)? sogd.  zäydm,  zam  .ich  sage',  zut  .er  sagt'  (uriran.  *jut-ati)\
*
481
arm.  kocem  (*g'^ot-{-)  ,rufe,  nenne,  lade  ein^,  ko^  ,Einladung^  (wahr- scheinlich nomen  postverbale);  got.  qipan  ,sagen,  sprechen,  nennen^, anord.  kveda  ds.  und  ,singen,  dichten^,  ags.  civedan  ^sprechen,  sagen, nennen,  befehlen,  erklären^,  afries.  quetha  ,sagen,  sprechen,  bedeuten', as.  quedan^  ahd.  quedan  ds.;  aisl.  kvidr  ,Spruch,  Gerede',  as.  quidi  st. m.  ,Rede,  Wort';  Kausat.  aisl.  kvedja  ,begrüßen,  anreden,  fordern,  auf- bieten', as.  queddiauy  ahd.  chetten  ,begrüßen' (d.  h.  ,zum  Reden  bringen'); anord.  kvgp  ,Forderung,  Vorladung,  Verpflichtung'  ist  zu  kveda  retograd o-ebildet;  got.  un-qeps  , unaussprechlich'  (vgl.  anord.  sam-kväsdr  ,überein- stimmend'),  sama-qiss  f.  ,Ubereinstimmung'  (*g^ct-ti-)y  zu  ags.  ge-cwiss  f. ^Verschwörung'.
WP.  I  672,   Feist  389,  G.  Morgenstierne  NTS.  7,  116  ff.
```


## [2026-09-06T15:00:49.616Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=555 && NR<=575 {print \"==LEAF \"NR\" (p.\"NR+537\")==\"; print substr($0,1,160)}' BQT_v2_pages.txt",
 "description": "BQT vol2 zhe section"
}
```


### [2026-09-06T15:00:51.131Z] TOOL RESULT

```
==LEAF 555 (p.1092)==
‫که درجنگه دوازده رخ بردست حجیری نگودرز‬             ‫سیهید ‪ = ۱‬بکر اول‌وضم بای ابجد‪.‬�
==LEAF 556 (p.1093)==
  ‫سییفه‌داز‬                                                                                                ‫‪۱۱۳‬‬
                  
==LEAF 557 (p.1094)==
 ‫—‬      ‫‪۰5 6‬‬



‫بهنای‬     ‫‪۰‬‬    ‫سفده‬     ‫ورن‬           ‫اش‬
                               
==LEAF 558 (p.1095)==
                                                   ‫يان چهارم‬
           ‫درسین بی‌نقطه بانای‌قرشت مشتمل برهفت�
==LEAF 559 (p.1096)==
 ‫‪۱۰۵۹‬‬                                                                                                                     ‫ستار‬
‫تک
==LEAF 560 (p.1097)==
                                                                                           ‫‪ ۷4۰‬ات‬
‫‪ -‬وبضی مطلق شاخ درخت �
==LEAF 561 (p.1098)==
‫هه اس‬                                                                                                ‫ستاله‬


‫گفتن‬   ‫لمیدح
==LEAF 562 (p.1099)==
                                                                                                                          ‫نز شا او‬

            ‫�
==LEAF 563 (p.1100)==
  ‫‪۵‬ات‬       ‫‪4‬‬
                                                                                              ‫سثروك‬
 ‫اس
==LEAF 564 (p.1101)==
                                                                                                      ‫=‬

‫آن قره بطالا باشد‬       ‫و
==LEAF 565 (p.1102)==
 ‫==‬                                                                                              ‫سوه‬

‫وزن کبوتر » هوابی باشد
==LEAF 566 (p.1103)==
                                                                                                 ‫‪î‬‬     ‫‪۱ ۵۳‬‬




  ‫الوث‬
   
==LEAF 567 (p.1104)==
   ‫‪۷‬‬   ‫‪4‬‬                                                                                                  ‫سنیز‬


 ‫یابگ
==LEAF 568 (p.1105)==
  ‫سجلاط‬                                                                                       ‫==‬

 ‫ونافرمالی نمودن‪ -‬وف
==LEAF 569 (p.1106)==
  ‫—‬       ‫‪۵‬‬                                                                           ‫نجن‬


‫سچیدن ‪ = ۲‬بروزن د
==LEAF 570 (p.1107)==
                                                                                                            ‫‪¬ ۱‬‬      ‫وه‬




 ‫سج = ب�
==LEAF 571 (p.1108)==
    ‫==‬                                                                            ‫وش‬
                                                             
==LEAF 572 (p.1109)==
 ‫سدوم‬                                                                                          ‫یت‬‫‪-‬‬

‫گوبند صمخ درخت 
==LEAF 573 (p.1110)==
  ‫تس رز —‬

‫برامن آن است کهیومرث را صد فرزدد از‬                 ‫قاضی شهر لوط است و او فتوی �
==LEAF 574 (p.1111)==
                                                                                                  ‫=‬            ‫‪-‬‬

‫وا خلال‬
      �
==LEAF 575 (p.1112)==
  ‫‪“NNN‬‬                                                                                                 ‫سراب‬


   ‫نی‬
    ‫‪-�
```


## [2026-09-06T15:00:58.589Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=515 && NR<=545 && /صمغ/ {print \"==LEAF \"NR\" (p.\"NR+537\")==\"}' BQT_v2_pages.txt\necho \"--- headers\"; awk 'BEGIN{RS=\"\\f\"} NR>=515 && NR<=555 {gsub(/\\n/,\" \"); print NR\" (p.\"NR+537\"): \"substr($0,1,110)}' BQT_v2_pages.txt | sed -n '1,45p'",
 "description": "Find zhe section in BQT vol2"
}
```


### [2026-09-06T15:01:00.362Z] TOOL RESULT

```
==LEAF 516 (p.1053)==
==LEAF 521 (p.1058)==
==LEAF 535 (p.1072)==
--- headers
515 (p.1052):  ‫ات‬        ‫او‬                                                                              ‫
516 (p.1053):                                                                                                       ‫سا�
517 (p.1054):   ‫==‬                                                                                                 ‫
518 (p.1055):   ‫زين‬                                                                                              �
519 (p.1056):                                           ‫کفتار دو آزدهم‬           ‫از کناب برها
520 (p.1057):                                                                                                ‫وی ‪— 
521 (p.1058):                                           ‫بیان دوم‬                  ‫در زای فارسی ب�
522 (p.1059):  ‫ژغاله‬                                                                                       ‫ه�
523 (p.1060):   ‫اف‬    ‫د‬                                                                                      
524 (p.1061):                                              ‫بیان هفتم‬                        ‫در زای ف�
525 (p.1062):                                              ‫بیان هشتم‬                       ‫در رای فا
526 (p.1063):  ‫زون‬                                                                                                 
527 (p.1064):   ‫—‬        ‫=‬                                                                                    
528 (p.1065):                                 ‫از کناب پرهان قاطمگفتار سیردهم‬   ‫در حر�
529 (p.1066):        ‫ها‬                                                                                             
530 (p.1067):     ‫ساده‬                                                                                            
531 (p.1068):   ‫‪¬1‬‬    ‫>‪° A‬‬                                                                        
532 (p.1069):                                                                                                    ‫اس‬ 
533 (p.1070):  ‫=‬    ‫‪o‬‬                                                                                     
534 (p.1071):                                                                                                   ‫= —‬ 
535 (p.1072):     ‫= —‬                                                                                       ‫سا�
536 (p.1073):   ‫سالار‬                                                                                         ‫
537 (p.1074):  ‫‪۱ ۰‬‬     ‫‪6‬‬     ‫سال خورد = بسکونلام ؛بمعنی‌بیار‬     
538 (p.1075):  ‫ساما کسه‬                                                                                   ‫ت
539 (p.1076):    ‫اس‬      ‫‪۷۵‬‬                                                                           
540 (p.1077):   ‫ساو‬                                                                                                
541 (p.1078):        ‫ه‬        ‫جاه‬          ‫ا ب‬            ‫و‬                                  
542 (p.1079):   ‫سابه خوش‬                                                                         ‫‪ ۷۱0�
543 (p.1080):      ‫‪«۹‬‬                                                                                    ‫س
544 (p.1081):                                                                                          ‫—‬   ‫‪0�
545 (p.1082):   ‫‪ ۷‬با ‪— ۵‬‬   ‫گ بروزن نفزك‪ .‬مصفر سبز باشد‬             
546 (p.1083):                                                                                         ‫ره باس‬  ‫
547 (p.1084):      ‫زا‬                                                                                        ‫سب
548 (p.1085):  ‫سڀار‬                                                                                          ‫س
549 (p.1086):   ‫رک ها‬  ‫گوبند « سپای دارم»‬                   ‫که‬‫نست‬           
550 (p.1087):                                                                                         ‫==‬              
551 (p.1088):      ‫س‪۵‬‬       ‫ایز‬                                                                      
552 (p.1089):                                                                                          ‫ها‬   ‫رس�
553 (p.1090):    ‫‪¬ 40‬‬   ‫تس‬                                                                             
554 (p.1091):  ‫سپوز کار‬                                                                                        
555 (p.1092): ‫که درجنگه دوازده رخ بردست حجیری نگودرز‬             ‫سیهید ‪ = �
```


## [2026-09-06T15:01:06.765Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==521{print}' BQT_v2_pages.txt | head -40",
 "description": "BQT p.1058 zhad"
}
```


### [2026-09-06T15:01:08.513Z] TOOL RESULT

```
                                          ‫بیان دوم‬

                ‫در زای فارسی باخای لقطه دار مشتمل بر دو لفت‬
                  ‫‪.‬‬   ‫ند‬
                       ‫ینیز‬
                          ‫گلهورا‬
                               ‫زاری و نا‬               ‫رخ = بفتح اول و سکون انی ‪ .‬مخفف‬
  ‫زخار ؟ = یکسر اول بر وزن شکار‬                         ‫آزخ است؛ وآن‌دانه ای باشد سخت وبی ددرکه‬
‫دراعضای آدمی بهم میرسد و آنرا بعربی تولول | بان و لعره را گوبند ‪ -‬و بممنی سختی لیز‬
                               ‫‪-‬صدای | آمده است ‪.‬‬
                                                ‫خوالنند ‪ - ۱‬وآواز حزین وآهته ؟ و‬



                                          ‫بیان سوم‬


 ‫معرب‬    ‫ار‬
          ‫وو‬‫داند‬
               ‫جته‌‬
                  ‫زو ‪ ۴‬ت شنح اول وسکون انی‪ .‬مطلق | مشهور؛ و سم اول نیز گف‬
                                   ‫‪۰‬‬     ‫ات‬      ‫‪۱‬‬     ‫را گونند‪ ,‬وآن چیزی است چبند هکه از‬              ‫صمغ‬


‫بکر اول و فتحایی» مخفف‬                        ‫‪"...‬ده‬                                               ‫‪a‬‬
 ‫زدوار ت بفتح اولبروزن و معنی‌جدوار‪ | ‎‬آژده‌است ‪ ۲‬که‌سوزن زدن وآژننه بنگه‌آسا‬
                                 ‫زدن باشد ‪۰‬‬            ‫باشد وآن دوایبی است‪‎‬‬      ‫‪ e‬که ماه بروین‬        ‫اش‪‎‬‬




                                         ‫بیان چهارم‬

              ‫زای فارسی بارای می نقطه مشتمل بر چهار لفت‬                               ‫در‬


                          ‫باشد ‪¥‬‬   ‫‪۱‬وبرخوری‬             ‫بمعنی بسبارخوردن‬     ‫بروزن زرد‬         ‫زرد‬


                           ‫ت‬                                          ‫‪.‬‬    ‫آزخ‬   ‫آزخ ‪۰‬‬   ‫رك‪:‬‬   ‫‪-‬‬   ‫‪۱‬‬
```


## [2026-09-06T15:01:20.156Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nfor n in 459 460 461 462 567 568 569 570 603 604 605 606; do echo \"== pdf $n ==\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N{gsub(/\\n/,\" \"); print substr($0,1,180)}' BQT_v3_pages.txt; done",
 "description": "BQT vol3 target pages"
}
```


### [2026-09-06T15:01:22.075Z] TOOL RESULT

```
== pdf 459 ==
[pdf page 459] و  و ده وروستا را ‎gt‏ گفته‌اند ‎Bare‏ دهی‌وروستابی باشد ۱ - وبمعتن کوناء وناقص همآمدماست؟ .
== pdf 460 ==
[pdf page 460] وت  کلات ۱ © ‎pele‏ اول بروزن حیات» للم شپری ‎col‏ از تر ‎SOLS‏ فرودیسر سیاوش(۱) با مادرتی آتجا 
== pdf 461 ==
[pdf page 461] کلانه  قهوه خوری +  کالاذه ۱ - ‎Jal pce‏ وذال قطمدار , کاج واحول راکوید .  ‎IT‏ » بر وزن ‎Ses dp‏ و و
== pdf 462 ==
[pdf page 462] -۱114- کلافه لام جایی ومقامی است.  کلاغ = بفتم اول. ممر‌واست وآنرا  کالاش ه بر وزن لواش : عشکبوت 
== pdf 567 ==
[pdf page 567] گازشیر  ‎pe?‏ ۰ باشین ‎aes‏ دار بر وزن ‎fees Sb‏ درختی ‎Seal‏ ساق آن کوتاه ‎Ky,‏ آن شبیه به ‎Fp‏ �
== pdf 568 ==
[pdf page 568] ۱۷۷۱ ‎OPIVP‏ ه با زای ‎abs‏ دار بر وزن ایدن,زهرة کار راکویند. چیزی با مد سنکه وآن‌از زهره کاوب
== pdf 569 ==
[pdf page 569] گاهنبارها ماحتابهاء ر گاهنبار هابررزن ‎OT‏ ابارها . اين دولئت يك معنی دارده و آن شش روری اس�
== pdf 570 ==
[pdf page 570] oS -۱۷۷۳<  آدم علبه‌اللام کرده ومبادی‌این ایام بر تقدیری است که ‎Lis‏ مترقه را در آخر بهمن ما
== pdf 603 ==
[pdf page 603] ee:  NAc  gs BE ‏بنم اول و‎ - os Miley ‏تالار‎ gan » Oe ‏بجیم‎ ot ‏کوچك و کنج و گوشه و بیفوله (۱) ونفب زیر
== pdf 604 ==
[pdf page 604] ۷۲ اس  کشیده و بنین نقطهدار زده 1 بمعنی کریز است که از کریختن باشد .  گر یفن ۱ ‎ble‏ بر وزن و مع�
== pdf 605 ==
[pdf page 605] بیان دهم  در ‎GE‏ فارسی با زای نقطه دار مشتمل بر پنجاه ودو لغت و کنابت  گز - بفتح اول و سکون ‎G
== pdf 606 ==
[pdf page 606] رات  کزار (۱) و ادا کننده سخن راکوبند ‎٩‏ . گزاددن ۴ - نم اول وف‌دالابد. بمعنی ادا کردن باشد چ
```


## [2026-09-06T15:01:30.690Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} NR==462{print}' BQT_v3_pages.txt | head -50",
 "description": "BQT kalagh page"
}
```


### [2026-09-06T15:01:32.310Z] TOOL RESULT

```
[pdf page 462]
-۱114- کلافه
لام جایی ومقامی است.

کلاغ = بفتم اول. ممر‌واست وآنرا

کالاش ه بر وزن لواش : عشکبوت را | زاغ‌دشتی‌هممیگویند۷
‎SaaS‏ - وصاحب ‎Waddle fa‏

‎ay‏ کلاغ بالشم و
بات کر
باش د که آنرا کرد بر
کرد قبور بزرکان
میدارند وآن از ‎Ke‏ وچوب نیز یود . #
‎bd FEW‏ - کنابه از استهرا
وتسخر و ربشخند کردن باشدکسیرا -
‎OWT‏ ۵ - بر وزن و ممنی کلابه
باشد و آن ‎Glos‏ است خام که ازدوكبرچرخه

‏کلاش خانه۲ = ‎get‏ ویافتضکبوت
راکویند و ‎lige‏ ایکا کیا خوانند ۴ - ‎bie,‏
‏عنکبوت را هم کفته‌اند که درآن تخم نهد وبچه
برآرد .
کلاشك ۴ = بفتح اول ورابع وسکون
‎GE‏ » بمعنی کلاسنگ است که فلاخن باشد.
کالاشکن * - بنتح اول ‎ing GS,‏
‎gals‏ نام یکی از حلواها باشد .
کلاشکه ۱ ‎che‏ اول ‎ele‏ وکاف:
قلاییرا گوبند که چیزها ‎HOR‏ چاه برآرند.

‎aN ia 0‏ لنگر ۰
‎٩‏ ره : جپانگیری ‎oe: dy‏ خانه . ۴ - از : کلاش ‎Cpe)‏ + خاله.
۴ رگ ‎Weyl:‏ ۴ - مسحف «کلاسنگ» ( هم ) =
‎٩‏ مخفف «6الاشکن» (هم. ) :
طفل برلج بی ن که چه خوش درکنار خوان لوح کلاشکن بکنارش نهاده اند .
«یسحاق اطعمه چاپ قطنطنیه‌س»۱۰*.
۱ - رك : کلاژ که . ۲ - ‎kulagh . kalagh‏ , هرن با ‎Lyles‏ ازرشة
اوستابی - ۷2۲881108 ( شاهین ) ‎syle i ey‏ ۷2۲28 ۰ ۷2۲۵ میداند « اسشق۸+۲»
ورك : هوبشمان ‎۸٩۷‏ , قس :کردی ‎kala‏ (کلاغ), زازا اژ92120 (کلاغ ) « ژاباس۳۳۹,
سمنانی ‎kala‏ )1( ,کاشانی 16116 ‎kargha ust.‏ (زا اغ) « وقس: بونالی ‎Agus kborax‏
‎corvus -3Y‏ ( کلاغ) . ‎Cormix‏ (زاغ) < هوبتمان ۸۱۷ © بلوچی ‎guragh‏ « اسفا ۱:
‎ony ۲‏ « طبری ‎۵٩۱ ales, > kalaj‏ © تهرانی و دزفولی ‎qalagh‏ کیلکی ۵180
پرنده ایست از ‎ees‏ سبك بالان بزر که با منفار درازفوی که از حشرات وجوند ان تغذيهميکند.
‎Cpe) am ۸‏ = کلاوه (هم) .
‎BUFO‏ پیسه - بفتح‌اول , از: کلاغ ‎(p.m)‏ -پیسه ‎(pam)‏ (مخفف آن : کلایسه) لفة
بمعنی کلاغ‌دورنگگ (سياه وسیید) ‎OE?‏ ص۱۱4 ‎GIT aed .٩‏ کلازاره (هدم.). ورلك: کلايیسه.

‏فد .

‎۱99۸ Gaie inthe ‏بقیه از‎
```


## [2026-09-06T15:01:47.552Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nfor n in 607 608 609; do echo \"===== pdf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N{print}' BQT_v3_pages.txt | grep -n \"گزیدن\\|گزند\\|گشتن\\|۱۸۱\" ; done",
 "description": "Find gazidan in BQT vol3"
}
```


### [2026-09-06T15:01:49.216Z] TOOL RESULT

```
Exit code 1
===== pdf 607
44:‎Gos‏ زده » بمعنی گزند و گزند رساننده
46:وگزند ‎Nol,‏
===== pdf 608
===== pdf 609
```


## [2026-09-06T15:01:51.935Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} NR==608{print}' BQT_v3_pages.txt | head -60",
 "description": "BQT vol3 pdf 608"
}
```


### [2026-09-06T15:01:53.587Z] TOOL RESULT

```
[pdf page 608]
ae © =VAN\—
۰ ‏رساننده وکزد وآزار کنان هم‌آهده‌است۱‎

wale ‏بتتح اول بر وزن‎ FW
‏مشتق از کزیدن ۴ است یعنی بگزد و کرد‎
oly ita ‏به یش‎ Ad ates

گزایش '- ‎em‏ اول بروزن ‎lS‏
‏بسنی در خور ‎BN‏ بشد ‎٩‏ - و بت اول عم
‎oth‏ هعنی و هم بمعنی چویی باشدکه خرو ‎IS‏
‏را بدان ‎Vast‏ ؛ و پکسر اول نبز کفته‌الد -
و بمعنی پبچش هم هت ۷ .

گزر - بفتح اول و ثالی و سکون رای
قرشت » زرد را گوند ومعرب آن‌جزراست۸
- و بضم اول وکسر ثانی, مخفف کزیر است که
چاره وعلاج باشد ‎٩‏ - و بضم اول وفتح ثالی +
خرجین ‎Pa ST LS‏ و بمعنی دویم که چاره

- از :کزای (گزاییدن ) ‎ot‏ ( پسود فاعلی ):
حقا که شکر زهر شود تلغ و گزایان کرام خلافش بنگاری بشکر بر .
عنصری بلخی « ریدی ۰ .
۴ رك :گزایدن . ۴ - از «گزایبدن» . ۴ - از ‎(ol TVs Fs‏
‎gt‏ ( اسم مصدر ) + * رك :کزاش. ۱ - رد :کزاش .
۷ - ظ.مسحف «کرایش»(«.م.) ‎A‏ - سانسکربت 8887 محتماازبارسی ناشی‌شده.
زرا ‎Sos‏ از ماخذ طبی مناخرآمده . رك : ‎O-Béhtlingk, Sanskrit.‏
‎Wirterbuch, abridged ed . ( St . Petersburg, 1879 - 89 )‏
و ‎esbir‏ با 85101۲ در ‎Lend‏ قرء ‎ged‏ ( روسیه ) یز باغعب احتمال از همین
‎cad‏ فارسی ‎R. N. Frye Su. :4) col‏ درمعرفی ‎Karl 13. Menges,‏
‎Qaraqalpaq Grammar‏ درمجلةٌ ‎Harvard Journal of Asiatic‏
‎Studies, Vol . 10. No ۰ 3.4, p-438‏ دریعتو 842812 و درکیلکی
‎ae 24-48 . (45,5) gazer‏ ۰ ۳ مصدرص‌خم ازد اکزردن»
(هم) ‎w‏ - صحیح ‎i‏ دوم است . ۴ از :گزر )= ‎GS‏
‎Gob‏ (پوند مصدری). ۳ ‎Ay‏ :کزارنامه < کزارش نامه .
۴- رك : ح ۱۵ صفحام ‎dy ۵ Nat‏ : سرزیره. گزر
‎Ud -0‏ بعنی کز(واحد مقیای) ‎Gale‏ (ملکی) ‏ کزملك ‎Com)‏ . رك :کزء شایگان.
»گرا ییدن - بفتح ‎Jal‏ وشنم شم کزبدن ؛ آفت رسالیدن » آسیب رسالدن,سنمهزدن:
کیت کش وصل کر زد سود کیست کش فرقت و نگزاید .
دقیقی طوسی > فرهنگه نظام».

‎Ee,‏ باشد بفتح دوم هم آمده است.

‏گرگ ۱۲ -ضراول وفتح ثابی(۱وسکون
را و دال بی‌نقطه « بمعنی علاج وچاره باشد چه
ناگزرد بمعنی لاعلاج باشد.

‏95.9 ؟۱- بنم‌اول وفتح‌دالابجد۱۱,
بمعنی علاج کردن وچاره نمودن باشد .

‏گزر نامه ‎-f‏ کاب تعبیر خواب را
کوند چه کزر ‎gee‏ خواب هم آمده ‎Med‏

‏گژره - بنتح اول وئالت و ضم ثالی»
گیاهی است که آن را سرزیره خوانند ‎NO‏

‎we FS MOLES‏ به ما
‎Gt th‏ و نیم آدمی که ستوی الخلقه باشد
و ‎gam‏ کویند ازيك ارش ولیم چیزی کمتراست»
```


## [2026-09-06T15:01:58.360Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} NR==609{print}' BQT_v3_pages.txt | head -70",
 "description": "BQT p.1812 gazidan"
}
```


### [2026-09-06T15:01:59.980Z] TOOL RESULT

```
[pdf page 609]
oF

. ‏در ولات خراسان رواج دارد‎ Sols

hy gilt ‏ینتح اول و سکون‎ ۱ sy
PS ‏است‌سیاه کب‎ fae ‏بمعنی فیرباشد وآن‎
‏وجپازمالند وسیم سوخته را نیز گویند- وسواد‎
‏زرگربراهم کفته‌اند؛ وبضم اول نیز بنظ رآمده‌است‎
. ‏وبا زای فارسی هم هست‎

‎DP‏ بر وزن نمکه ,هر چیز که
بدان تفیدر ذائقه کنند ۴ - و سرما زده را یز
گوند ۳ .

‎OP‏ - بکس اول و لام وسکونثانی
‎SE,‏ :کارد کوچك دسته درازرا گویند؟ -ونوعی
از قلم تراش را هم گفته‌اند که سر آن بر کشته
و داباله‌اش باريك ‎ath‏ و بیشتر از جاب مسر

‏آورند .
گزم - بفتح اول وسکون ثالی و میم +
(۱) چش ‎aS:‏ .

‏۲ را

‏درخت کز را کوبند وبسبی طرفا خوانند 9 .

‎VILE‏ - بنتح اول وسکون‌نالی
و میم بالف کشیده و زای قطفدار مفتوح بکاف
‎pag sh 005‏ درخت کزرا ‎aa See‏ (۱)ومعرب
‎OT‏ جزمازج است و بعریی ثمرة الطرفا خوانند
وحب‌الائل همان است با ای مثلثه .

‏گزمارو ۲ - بر وزن شنتالو , بمعنی
کزمازك است که ‎tye‏ درخت کز باشد .

‎He FF‏ = بکسرتانی وض‌تالت‌وسکون
لام وکاف » بمعنی گزشایکان است ۸ و آن‌مقدار
بك ارش ولیم است بچی زک ی کم .

‎AP‏ بروزن کمند » بمعن یآسیب
وافت و رنج و چشم زخم باشد .

‎AS‏ - با دون بروزن فرزند . جوال
پرکاء ‎Ae an Sl,‏

‎٩‏ رف :کزف ‎GI‏ , کشف ؛ و رك : کرف . ۴ ‎sie‏ که ‎jae‏ شراب
خورند از ‎Jad‏ میوه وآجبل و جز ‎AGT‏ قل ‎Kin prays‏ نظام» . سراج کوید : «ک که
بوزن نك , هر چه برآن تفییر ذائقه کنند در شراب » و در برهان تفییر ذائقه مطلقاً ,و ‎OT‏
‏خطاست.» (سراج‌اللغات بنقل فرهنگه نظام ج ه س لط) . ۴ - مرضی عشپو رکه بعربی
‎Se,‏ «رشیدی » «کزك زدن زخم . تشنج و بدی زخم ازآب برداتتن یا بو بردن.میرالهی
همدالی (گوید ) :
دل خون کرفته است که دشمن هم از غیش در هم کشیده روی چر زخم ‎IS‏ زدء .»

‏« بهار عجم .

‎US  ).م.«(‎ US = ¢‏ و رك : دزی ج ۷ ص43۳ :

‏پنما بمن که منکر حسن رخ ت وکیست تا دیده‌اش بگزلك غیرت برآورم .
«حافظ شیرازی . دبوان ص ۲۲>.

‏9 رك : ‎us Saye‏ ورك :کز. ‎(pa) wml‏ = جزمازج(معرب) ع
جزمازق ( معرب ) < کزمازك ( معرب) ]= جزمازك] ‎fruit du tamaris‏ « دزی ج ۱ س
۳ س ‎Galle du tamarix‏ » عقار ۷۰۰ ق >. ۷ سس کزمازك ‎(pa)‏

‏4,4 :گز خایگان . ‎٩‏ پهلوی ۷12200 ‎ine)‏ نصه . غم ) , پارسی
جدید ‎gazand , guzand‏ ( شکل چنوب غربی ) ۰ ‎JC: ( bazhand?‏ شمال غربی ) .
‎YL!‏ باستان - 2۳1 - ‎vi‏ ۵ از - ‎Ban‏ ( زدن ) « بارتولمه ‎4٩۰‏ » « تیب رکه ص ۷45 >
```


## [2026-09-06T15:02:10.663Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 402 403 404; do echo \"===== leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N{print}' BQT_v1_pages.txt | head -45; done",
 "description": "BQT vol1 p.184 owzhandan"
}
```


### [2026-09-06T15:02:12.361Z] TOOL RESULT

```
===== leaf 402
ای ۸ اه
نیز خواشد ره ۳
اورمز ۱ نم اول و میم و سکون
وین ثالث و زای قطمدار . دام متارة
ی باشد - و فام روز اول است از هر صله
نيك است در این روز نو پوشیدن‌وسفر
کردن" و مهر بر کاغذ نهادن » و بد است قرض
و وام دادن - و نام فرشته ایست که تدییر لمور
اسفندیار هم هستِ که بسر بهمن باشد .
اودهز ۵ ۱ » پروزن روز دزد » بمعنی
اورمز است که نام روز اول از حرمله شمسی -
و نم ستار؟ مشتری -.و لام فرشته ای که موکل
ات تلم بسرزاده اسفندبار
اورمك « پروزن اوزيك , کلاموطاقی
پهمین‌را گویند,وسنی‌این‌لفت ران رکی‌میدانند ۴ .
آود نج - تال وثالك و سکون‌نالی
و نون و جیم » سکه الگور را کویشد و آرا
و جم ال و سکون انی مجهول » چوب خوشة
انگور باش که انگور آرا خورده بلشند ؛ وباین
معانی بچای حرف ثالث لام هم بنظرآمده است .
آورنگن
آود فحین - بر وزن فروروین » بمعنی
اورنجن امت و آن میلی باشد از طلا ونقره که
زنان بر (۱) دست و با یکنند .
اود فك ۲ ۰ بر وزن سوکند » مکر
وقریب و دفا وخدعه باشد - و + وی
حست که تخت پادشاهان است - و بممنی شأن
و شوکت و فر و شکوه و عظمت و ژیبایی وبها
لیز آمده است- و هم یکی از پسرا نکی‌پشین‌بن
و طالم و زیدگانی را هم گفتها ند - و رودخانةً
عظیم و بر رکه را یز کویندمطلقاً همچو رودئیل
ودجلةٌ بفداد واثالآ نپا ۵ - وبمعنی درباهم‌پشظار
آمده اس تکه بعربی جحر خوانند - و سیاهی‌را
یز کن‌ماند که در مقابل سفیدست .
اور فدیدن » بر وزن بر هم چیدن »
مصدر اورند. است یمعنی قریب. دادن و مکر
وحیله نبودن ۰
اود نگ - بر وزن فرهنکه . تخت
پادشاعان باشد - و بمنی عقل و داش - و فر
هست - و هکر وفرب و حیله را ی 5
و نام شخصی‌است که‌اوماشق کلچهره نامی‌بوده ۱ -
آوو فک - ینتم اول بروزن وبت زن» | وئم جانور کی هم‌هست که عربان‌ارضه‌خوانند ۷ .
باشد از طلا و نقره و امثال آ نکه ز 0
0 تِ 9 7 ۲ اور نگی بر وزن فرزندي » دمم
دست اورنجن و آنسه در با ی کنند پای آورنجن پرده ابست از موسیقی - و نام لحن می‌اماست‌از
===== leaf 403
آوروختن
آود و ختن ه بروزن و معنی افروخئن
است. که روشن کردن: آنشس و چراغ باشد ۷ .:
آوده » بفتح اول و ثاكك وسکون‌انی »
بمعنی ابره است که روی فبا و کلاه و امثال ان
باشد, چه درفارسی با و واو بهم نبد بل‌می با بند ‌-
اور یا ۴ ه بر وزن بوربا» نام شخصی
است که داود علیه‌السلام او را بجنك فرستاد واو
۳ جنک کته شد و داود زن او را خواست
سلیتان عله‌الملام از ان زن بهم دسید ؛ ویسنی
گوند جد مادری سلیمان است و جمعی گویند
برادز داود عله‌السلام بود .
۱ اور لت هن اول و خفای نانی و کسر
الث و سکون تحتانی و بای ابجد» آنست که در
عربی محرف و بت رکی قیقاح گویند . *
"او رف هت یک ثات و سکون واو ؛
بروزن و معنی اوربباست که‌بتر کی‌قیقاج‌وبعربی
ایو < بانندید ثانی بر وزن هوزء نوعی
از مرغایی بزر که باشد - و مفتح اول و کمرثانی
و بکسر اول و انی هم آعده است؛ گوشد عربی
ی 9
اورار بروزن و ممنی افزار است که
بادبان کشتی - و دست افزارپيشه وران - و کفش
و با افر ار سوداروی کرم‌باشد مثل فلفل‌ودارچینی
. رك :افروختن . ۴ رد : اپره‎ ٩
یت
و زیره و غیره که در ذیگه طمام ریز تر6 ۰
اورایش بررزن ومعنی افزایش‌است
ععنی زباده شدن .
اون ك با زای فارسی بروژندوزن»
بمعنی انداز باشد که از انداختن و افکندن‌است.
و بمعنی فاعل حم صت که اندازنده وافکننده
باشدب وامرباین معنی‌هم آعده است یعنی بینداز
و بیقکن و قتل و کثش را نیز کونند که از
کشگن ماشد .
ماضی افکندن و انداختن باشد , ۱
۵ ۰
آوز ندیدن ۲ بر وزن بر هم‌چیدن ؛
بمعتی افکندن و الداختن باشد .
۵ ۰
اوز نید۲ پر وزن برمزید » بمعنی
افکند وانداخت باشد که ماضی‌افکندن وانداختن
است  .‏
اه ژ ی
ودول ع« بر وزن مقبول » سعنی
===== leaf 404
ی و ای
ع ‏ به ۷ ج جم حممي یه ۶" چا + ف ( ۲[ ج هو مه
۳ 2
۳
۱۲
۳ 5
۴ اه
۵اه
کدی نع
1 پدیم‌ر(ید._ | هرز | ع۴غطع | اصونل خدا ۳
۲ تس( ]ار ۱ 3
ری رکراه) رسد ایدا 2۶ | اعا ۹
ری و 4 پلاس ۳ -72] ]| جزه, فره ۹
او ص دویسم ای اوسعَة ید | اشم.خم ب
او رگشبه) وود اه | جرف ۳ 1
| زد رس طکه 6 یر فا ول دس ت نمسندا سین .حانه 9 اد
! دگرنای )ان (رش 8۱۳24 راست ,دست له 0۶ ) 5
یه 66 ند جرد جر نت اصعبعوق | رانا رورشد (ممدا) ع
ز وراه ورتم دملد او ارو 29۳۵ تعارز 0
ز (اراه ویر ات 4
آ و رکشده) [ید<6 ره وت و (وساة
او نهد (س تراد مهم | دم »بر _
ان ترسیری مس () نتم وحصگ» اند + صأنه
] (دیچن) ری زد خن ۱ ی 6
۹ 5 مند 6 مب کاعٌه هت ۳ ,کامه ۷
5 اعد اغق اماب | ج
خر ج ند ۵۵ ازیه خزفنه 9 ۷ چا
گر سید اه | ]۳۰۲ , 8
3 1 عو سع‌ندت ,یت )
ٍآ تسوا یسدنه اه هی ]| رایس | عم 5
۳ و 9 5 کر
م‌ ۲سدیج چش یم پسیدده 4
ح نسم لام نزو | ررف. گس ّ
۱ ۵۰ اد ۹
زد اک أوب؟ 4 ۰
رُ نل(د رنر 3 راو ۱
۱ یا (نید جد ت۳۳( سراه‌سگه قلة ره یام ](۸۵ه)1
```


## [2026-09-06T15:02:25.489Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nfor n in 216 217 218; do echo \"===== pdf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N{print}' BQT_v4_pages.txt | grep -n \"نژند\\|۲۱۳\\|نژ\" | head -10; done",
 "description": "BQT vol4 nazhand"
}
```


### [2026-09-06T15:02:27.540Z] TOOL RESULT

```
===== pdf 216
===== pdf 217
8:و - بفنتح اول و سکون ثانی , بیرون | کوهری کنه اصیل باشد » و نژاده تفسیر اصیل
15:بعنی نژاذ است که اصل وب و اصیل ونجیب | ضباب خوانند .
17:۱ رد : نژ تژه (؛). ۲ - این‌کلمه صوره تربدن »۰ « تزیدن » و «نژیدن»
18:دری ن کناب آهده است (۱) رك : نژ » تژبدن - ۴ -رك : نویدن .
23:۷ - باین معتی* نژاده» (ه.م.) ضبح است . ۸ از : نژاد (۶.م.) ۰۳ (پوند
28:*- کمین دولت و در هرتبت کرفته مکان ملك نژاده و اسر مکان ملك مکین .
===== pdf 218
2:-و۲۱۳-< س‌
17:۱ - هربرکی از اوكونة رخار نژفدیست ‏ هوشاخی ازوزصورت انگفت نگارست ۰ :
21:۴ - در جهاتگیری « نژنگه > بفتح اول و اسکون دوم آهده ‏
23:و ورق زرنثار - وتیر سقف ) برای « نژه> نوشته که تصحیف خوانی« تژه > است و درشعر شاهد
35:بقیه در حاشية صفحةٌ ۲۱۳۹
```


## [2026-09-06T15:02:30.386Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} NR==218{print}' BQT_v4_pages.txt | head -45",
 "description": "BQT vol4 pdf218 nazhand"
}
```


### [2026-09-06T15:02:31.970Z] TOOL RESULT

```
[pdf page 218]
-و۲۱۳-< س‌
ون و دال ایجد » بمعتی اندوهگین و غمناکه قژه - بفتح اول و ثانی وظهور ها» خاخ
وفرومانده و افمرده و سرفرود افکنده و پژمرده | درختی راکوبند که بسیار نازك و لطیف برآمده
باشد ‎٩‏ - و بمعنی‌سر گشته وخشمکین وفهرآلود | باشد ۴ - و ورق طلا و نقره رانیز کوبند که
هم هست - وپست و حضرض را نیز کوبند که در | بهیأت بر که کل بریده باشند و برسر پادشاهان
مقابل بلند واوج باشد ۴ ؛ وبفتح اول هم آمده | و نودامادان نثارکنند ۴ - ونام ستاره‌ای هم‌هست
است . از ثوابت * - و چوبی که بدان سقف خانه را
نک ۴ - بفتح اول و دون بر وزن پوشند ۴ .
نغزك , دام و تله راکوبند که حیوانات را بدان فژیدان ‎٩‏ » بروزنومعنی کشیدن باشد.
گیرند.
بیان یاز دهم
در نون با سین بی‌نقطه مشتمل بر سی وهشت لغت و کنایت
: پوز باشد که گردا کرد لب و دهان امت ازجا
سس - بنم اول و سکون ثانی » بممنی درون و بیرون ۷ - و بمعنی هو وشمور وعقل
() چك : ژد ویاژند .
۱ - هربرکی از اوكونة رخار نژفدیست ‏ هوشاخی ازوزصورت انگفت نگارست ۰ :
« فرخی سیستالی ص ۲۶ *.
- بغاك اسر افکند خوار وتژند فرودآمد ودست کردش ببند +
فردوسی طوسی « شاهنامة پخ اج ۳ص ۰۸۹۵
۴ - در جهاتگیری « نژنگه > بفتح اول و اسکون دوم آهده ‏
۴ - موّلف فرهنگه نظام نویسد : « جهانگیری مه معنی دیگرهم ( شاخهٌ نازك درخت-
و ورق زرنثار - وتیر سقف ) برای « نژه> نوشته که تصحیف خوانی« تژه > است و درشعر شاهد
از سیف اسفرنگی برای معنی شاخه وزرورق هم باتاء‌است . شعر این آمت :
پنجةٌ سرو از طرب بر دست گیرد جام مل طرء بید آزتژه بر کلشن‌افمانده(افعاند) تژه .>
و رك : تژه » لزه- 8 - باین معنی در جهانگیری بدون شاهد آمده .
۹ - این کلمه صوره نزیدن »۰ « تریدن > و۸ تربدن > درین کناب آمده , و رك : ات .
۷ - در نخ متعدد لغت قری « لس » بهمین معنی آمده و این بیت رود کی (سمرقندی)
شاهدآورده شده :
کیرآلوده بیاری و هی د رکی‌من بوسه‌ای چند پتزویر دهی بر نی هن.
رك : لغت فرسی ص ۱۹۹ -
در رود کی مسحح نفیسی ج ۳ص ۱۳۹۹ :۱ بونه‌ای چند بتیرو پزلی بر نی هن -
وسوزنی سمرقندی کوید :
خرخر بنده بد لنچ ونی را پز بازی کر استا د کردم . « فرهنگه نظام >.
بقیه در حاشية صفحةٌ ۲۱۳۹
```


## [2026-09-06T15:02:43.300Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} NR==217{print}' BQT_v4_pages.txt | tail -25",
 "description": "BQT p.2134 footnotes"
}
```


### [2026-09-06T15:02:45.214Z] TOOL RESULT

```
کتته‌اند ۴ . وغار ۱۱ باغین تقطه‌داربروزن رفتاره
نزاد * < بکراول بروزن نخاط , اسل | بانگه و فرباد وتعره راکویند .
و نب را گوبند ‎٩‏ - و بمعنی اسیل و نجیب رم ۱۳- بکر اول وسکون ثانی ومیم»
وخداوند اصل ودب هم‌آمده است ۷ . بمعتی‌میغ‌است وآن بخاری باعد تاربك وملاصق
فزاده * - یک اول بر وزن فتاده . | زمین ؛ وبم اول هم بنظر آمده است که عربان
بعنی نژاذ است که اصل وب و اصیل ونجیب | ضباب خوانند .
باشد ‎٩‏ ؛ و بفتح اول هم آمده است - و پمعتی | قوف ۱۴سیکراول وفتح ثانی وسکون
۱ رد : نژ تژه (؛). ۲ - این‌کلمه صوره تربدن »۰ « تزیدن » و «نژیدن»
دری ن کناب آهده است (۱) رك : نژ » تژبدن - ۴ -رك : نویدن .
۴ - در لفت فری (ص 4۶۲ ) « تزه > با شاهد بدین معتی‌آهده » ورك: قره » تژه -
6 - اوستا )08122 . قی : سانسکریت 111 ۶ اسدق ۰۹۱۰۳۰
‎٩‏ - من تناکوی توام زیرا تژادم لیست بد خود تکوگوی ترا هرکزنبوده بد تژاد.
متائی غزنوی صس ۵۵۳ >
۷ - باین معتی* نژاده» (ه.م.) ضبح است . ۸ از : نژاد (۶.م.) ۰۳ (پوند
سبت و اصاف ) رك : اسشق ۳۰
‎٩‏ - آزرده این وآن بحذر از من کوبی که از تزادة تلینم .
* ناصر خرو بلخی ص ۰۶۲۷۰
و رك : تاریخ سیستان ص ۸۷ متن واح ۳
*- کمین دولت و در هرتبت کرفته مکان ملك نژاده و اسر مکان ملك مکین .
* فرخی سیستانی صس ۰۲۹۵
۱ مصحف « زغار » (م.) ۳ زغار (م.)
۴۳ بترم (وم.) ۴ پارسی‌باستان -270[ 981-۳ (بزمین انداختن؛فروشاسن).
همچنین در پارسی باستان -011128110 ( خوارکردنی » فروافکندنی ) مقروض است. ر4: اسشق
۹۱ ؛ و رك : نیب رگه س ۱۵۸ (52۳ - 6 هون ).
```


## [2026-09-06T15:03:01.776Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF leaves with اوژن\"; awk 'BEGIN{RS=\"\\f\"} /اوژن|آژده|آژدن/ {print \"leaf=\"NR}' FSF_pages.txt | head\necho \"=== FSF grep\"; grep -n \"اوژن\\|آژده\\|شیراوژن\" FSF.txt | head",
 "description": "Grep Noushin Shahnameh glossary"
}
```


## [2026-09-06T15:03:03.374Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON نژند\"; grep -c \"نژند\" MON_part1.txt MON_part2.txt 2>/dev/null; grep -n \"نژند\" MON_part2.txt | head -3\necho \"=== MON ژد\"; grep -n \"انگژد\\|انگژه\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Grep Mo'in"
}
```


### [2026-09-06T15:03:03.609Z] TOOL RESULT

```
=== FSF leaves with اوژن
leaf=10
leaf=27
leaf=30
leaf=54
leaf=69
leaf=70
leaf=73
leaf=181
leaf=273
leaf=274
=== FSF grep
119:اوژن بریور, «در اعماق» از ماکسیم گورگی» «مستنطق» نوشته پریستلی» «یوری ناگی 
1280:لگامی به زر آژده بر سرش 
1282:در بیت زیر «آژده» به معنی رنگین است: 
1284:رخان مسعصفر به زر آژده 
1287:به داغی جگرشان کنی آژده 
1291:دلی کو نباشد به درد آژده 
1294:ز بس در چرم ایشان آژده تیر 
2935:آژدها 
2941:آژدها 
4044:اوژن
```


### [2026-09-06T15:03:03.692Z] TOOL RESULT

```
=== MON نژند
MON_part2.txt:0
MON_part1.txt:0
=== MON ژد
```


## [2026-09-06T15:03:09.052Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1275,1300p' FSF.txt; echo \"==== owzhan ====\"; sed -n '4040,4070p' FSF.txt",
 "description": "FSF azhdan and owzhan entries"
}
```


### [2026-09-06T15:03:09.119Z] TOOL RESULT

```
«چين و شکن» (جهانگیری) ابه معنی 


رنگ کردن هم امده است» (پرهان4 
یکی اسب رهوار زیر اندرش 
لگامی به زر آژده بر سرش 
(۲۸۷-۱۴۵-۲) 
در بیت زیر «آژده» به معنی رنگین است: 
سوی خانه شد دختر دلشده 
رخان مسعصفر به زر آژده 
(۸۶۲-۱۹۱-۱) 
۲-معنی دیگر آژدن خلانیدن و خلیدن است: 
به داغی جگرشان کنی آژده 
که بخشایش آرد برایشان دده 
(۴۵۹-۱۰۶-۱) 
ز مردم شمر ار ز دام و دده 
دلی کو نباشد به درد آژده 
(۶۹۷-۲۷۷-۵) 
از فخر گرگانی (ویس و رامین ۵-۳۴۰): 
ز بس در چرم ایشان آژده تیر 
تو گفتی پر ور بودند نخچیر 
آژنګک 
چین و شکن و چروک: 
پرآژنگ شد روی پور پشنگ 
ز گفتار اغریرٹ آمدش ننگ 
(۱۵۲-۱۵-۲) 
==== owzhan ====

1۵ 


اوژن 


جهان خرم از فر و اورند اوی 
هم از میر محمود فرزند اوی 
*اورند 
فریب» نیرنگ: 
چو آن نامه برخواند خورسند گشت 
دلش سوی نیرنگ و اورند گشت 
(ج ۴-ص ۱۶۹۳) 
اورنک 
۱-تخت. گاه: 
چو کاوس را دید دستان سام 
نشسته بر اورنگ بر شادکام 
(۱۰۱-۸۱-۲) 
از فخر گرگانی (ویس و رامین ۸-۲۹۵): 
جوانی داری و اورنگ شاهی 
چو این هر دو بود دیگر چه خواهی؟ 
از ناصر خحسرو (دیوان ۲۰-۲۳۷): 
بسر کد هرشن نی هرا تست از 
گاه بخشدش و مسند و اورنگ 
۲-فر و زیبایی خرد و دانش (رشیدی - 
برهان) «زیبایی» (لغت فرس): 
گر ایدونک آید ز مینو سروش 
نباشد بدان فر و اورنگ و هوش 
(۱۷۸۵-۱۱۶-۳) 
از فخر گرگانی (ویس و رامین ۶۶-۱۵۹):
```


## [2026-09-06T15:03:25.309Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"اوژد\\|اوژَ\\|شیر اوژن\\|گرد اوژن\\|اوژنیدن\" FSF.txt | head -20; echo \"---\"; sed -n '4075,4130p' FSF.txt",
 "description": "FSF owzhan entry"
}
```


### [2026-09-06T15:03:25.376Z] TOOL RESULT

```
4074:اسم فاعل مرخم از اوژنیدن به معنی 
4078:در واه مرکب. شیر اوژن = شیرافکن؛ 
4090:بپر سید شیر اوژن از شهریار 
4093:منم گفت گرد اوژن رزمخواه 
4264:که‌ای باب شیر اوژن تیز چنگ 
---
افکندن. زدن. کشتن: 


در واه مرکب. شیر اوژن = شیرافکن؛ 


اومید 


گرداوژن گردانکن... پهلوی ۵20: 
شاهنشاه به ریدک گفت که شو [ رو برو ] 
شیران را باوژن [: بیفکن. بزن» بکش ]و 
ریدک شد. و شیران را باوژت (خسرو و 
ریدک ۱۱۹-۴۱): 
گرفتند هر سه ورا در کنار 
بپر سید شیر اوژن از شهریار 
(fr-11-۴)‏ 
بغرید شنگل ز پیش سپاه 
منم گفت گرد اوژن رزمخواه 
(۵۲۶-۲۴۲-۴) 
به هومان سپرد آن زمان قلبگاه 
سپاهی هژبر اوژن و رزمخواه 
(۵ ۲-۱۰۴ 
اومید 
امید: 
ور اومیدداری که خسرو به مهر 
گشاید برین گفته‌ها بر تو چهر 
(۱۲۶۵-۱۵۷-۵) 
از فخر گرگانی (ویس و رامین ۷-۴۱۰): 
چو کشت تشنه بر اومید باران 
ویابیمار بر اومید درمان 
اهتوخوشی 
به گفتار دربارۀ پیشه‌های چهارگانه در 
شاهنامه نگاه کنید. 
ایدر 
اینجا: 
دل و جانم ایدر بماند همی 
مژه خون دل بر فشاند همی 
(۲۴۳۹-۱۵۲-۱) 


که دو پهلوان آمد ایدر به‌جنگ 
ز ترکان سپاهی چو دشتی پلنگ 
(۳۷۴-۳۱-۲) 
از اسدی ( گر شاسب‌نامه ۲۲-۱۱): 
ببین و بدان کز کجا آمدی 
کجارفت باید چو ز ایدر شدی 
از ناصر خسرو (دیوان ۱۶-۴۸): 
نیست چیزی هیچ ازین گنبد برون 
هرچه هست و نیست یکسر ایدرست 
ایدون 
چنین داد پاسخ که ایدون کنم 
که کین از دل شاه بیرون کنم 
(۴۶-۱۹۸-۱) 
که گیتی ز آغاز چون داشتند 
که ایدون به ما خوار بگذاشتند
```


## [2026-09-06T15:03:35.261Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb && sed -n '1,40p' tools/fetch_source.py",
 "description": "Check fetch_source usage"
}
```


### [2026-09-06T15:03:36.924Z] TOOL RESULT

```
Exit code 2
sed: can't read tools/fetch_source.py: No such file or directory
```


## [2026-09-06T15:03:39.749Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n '1,45p' /home/sfmqrb/git/rishe/tools/fetch_source.py",
 "description": "Read fetch_source.py"
}
```


### [2026-09-06T15:03:39.797Z] TOOL RESULT

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
```


## [2026-09-06T15:03:46.174Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D8%B2%DB%8C%D8%AF%D9%86\" \\\n \"https://www.etymonline.com/word/bezoar\" \\\n \"https://www.etymonline.com/word/gun\" ; do\n echo \"##### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 215, root Gwhen 2, verifying nodes\"; done",
 "description": "Archive web sources batch 1"
}
```


### [2026-09-06T15:03:51.582Z] TOOL RESULT

```
##### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-
/home/sfmqrb/git/rishe/data/verification/sources/web/8f4a4c4d0f4d87ee.txt
##### https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/cdc38016c37eaee5.txt
##### https://en.wiktionary.org/wiki/%D8%B2%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/470f5036ec28b2dd.txt
##### https://en.wiktionary.org/wiki/%DA%AF%D8%B2%DB%8C%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/02d46431ba6c893c.txt
##### https://www.etymonline.com/word/bezoar
/home/sfmqrb/git/rishe/data/verification/sources/web/6d735b18286ee472.txt
##### https://www.etymonline.com/word/gun
/home/sfmqrb/git/rishe/data/verification/sources/web/1c3471c70f712a24.txt
```


## [2026-09-06T15:03:54.847Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"########## PIE gwhen\"; grep -n -i -A25 \"Proto-Indo-European root\" 8f4a4c4d0f4d87ee.txt | head -50",
 "description": "Read PIE gwhen wiktionary"
}
```


### [2026-09-06T15:03:54.912Z] TOOL RESULT

```
########## PIE gwhen
145: Terms derived from the Proto-Indo-European root *gʷʰen- (74 c, 0 e) 
146-
147- *gʷʰén-dʰe-ti ( dʰ-present ) 
148- Proto-Italic: *fendō ( or < *gʷʰn̥dʰi ( “ strike! ” , pr.ipv.sg. ) ) [ 4 ] 
149- Latin: *fendō [ 5 ] ( see there for further descendants )
150-
151- *gʷʰén-ti ~ *gʷʰn-énti ( athematic root present ) 
152-
153- *gʷʰén-ye-ti ( ye-present ) [ 6 ] [ 5 ] 
154- > ? Proto-Albanian: *gānja 
155- Albanian: gjuaj ( “ to hunt ” ) [ 2 ] ( or < *h₁eyǵʰ- or *seh₂ǵ- ) 
156-
157- Proto-Armenian: 
158- Old Armenian: ջնջեմ ( ǰnǰem ) ( see there for further descendants )
159-
160- Proto-Balto-Slavic: *genˀtei ( see there for further descendants )
161-
162- Proto-Hellenic: *kʷʰéňňō [ 7 ] 
163- > ? Ancient Greek: θείνω ( theínō , “ to strike ” ) ( or secondarily formed from a thematic root present ) 
164-
165- *gʷʰe-gʷʰón-e ~ gʷʰe-gʷʰn-ḗr ( reduplicated stative ) 
166-
167- *gʷʰn̥-sḱé-ti ( sḱe-present ) [ 2 ] 
168-
169- *gʷʰé-gʷʰn-e-t ( reduplicated thematic aorist ) [ 2 ] 
170- Proto-Hellenic: *kʷʰékʷʰnon 
--
246: Proto-Indo-European roots 
247- Proto-Indo-European CeR-shaped roots 
248- Proto-Indo-European imperfective roots 
249-
250- Hidden categories: Pages with etymon 
251- Proto-Indo-European entries with etymon 
252- Pages with entries 
253- Pages with 1 entry 
254-
255- This page was last edited on 23 August 2026, at 21:54.
256-
257- Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
258-
259- Privacy policy 
260-
261- About Wiktionary 
262-
263- Disclaimers 
264-
265- Legal & safety contacts 
266-
267- Code of Conduct 
268-
```


## [2026-09-06T15:03:59.145Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '100,145p' 8f4a4c4d0f4d87ee.txt\necho \"############## zahr\"; grep -n -B4 -A18 \"Middle Persian\" cdc38016c37eaee5.txt | head -60",
 "description": "PIE gwhen head + zahr etymology"
}
```


### [2026-09-06T15:03:59.209Z] TOOL RESULT

```
 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *gʷʰen- ( imperfective ) [ 1 ] [ 2 ] [ 3 ] 

 to strike , slay , kill 
 Synonyms: *bʰerH- , *bʰeyh₂- , *dʰebʰ- ( See also Thesaurus:gʷʰen- ) 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *gʷʰen- (74 c, 0 e) 
############## zahr
1030-
1031- Etymology
1032- [ edit ] 
1033-
1034: From Middle Persian zʾhl ( zahr , “ poison, venom ” ) .
1035-
1036- Pronunciation
1037- [ edit ] 
1038-
1039- ( Classical Persian ) IPA ( key ) : /ˈzahr/ 
1040-
1041- ( Dari, formal ) IPA ( key ) : [zäɦɾ] 
1042-
1043- ( Dari, formal ) IPA ( key ) : [zäɦɾ] 
1044- ( Kabuli ) IPA ( key ) : [zɑːɾ] 
1045-
1046- ( Hazaragi ) IPA ( key ) : [zɔːɾ] 
1047-
1048- ( Iran, formal ) IPA ( key ) : [zæɦɹ] 
1049-
1050- ( Iran, formal ) IPA ( key ) : [zæɦɹ] 
1051- ( Tehrani ) IPA ( key ) : [zæːɹ] 
1052-
--
1231- Ottoman Turkish terms derived from Persian 
1232- Ottoman Turkish lemmas 
1233- Ottoman Turkish nouns 
1234- ota:Poisons 
1235: Persian terms inherited from Middle Persian 
1236: Persian terms derived from Middle Persian 
1237- Persian terms with IPA pronunciation 
1238- Rhymes:Persian/ahr 
1239- Rhymes:Persian/ahr/1 syllable 
1240- Persian lemmas 
1241- Persian nouns 
1242- South Levantine Arabic terms belonging to the root ز ه ر 
1243- South Levantine Arabic terms inherited from Arabic 
1244- South Levantine Arabic terms derived from Arabic 
1245- South Levantine Arabic terms with IPA pronunciation 
1246- South Levantine Arabic terms with audio pronunciation 
1247- South Levantine Arabic lemmas 
1248- South Levantine Arabic nouns 
1249- South Levantine Arabic collective nouns 
1250- South Levantine Arabic masculine nouns 
1251- South Levantine Arabic uncountable nouns 
1252- South Levantine Arabic adjectives 
1253- ajp:Flowers 
1254- ajp:Vegetables
```


## [2026-09-06T15:04:04.877Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"##### zadan\"; grep -n -A12 \"^ Etymology\" 470f5036ec28b2dd.txt | head -40\necho; echo \"##### gazidan\"; grep -n -A12 \"^ Etymology\" 02d46431ba6c893c.txt | head -40",
 "description": "Wiktionary zadan/gazidan etymologies"
}
```


### [2026-09-06T15:04:04.934Z] TOOL RESULT

```
##### zadan
70: Etymology 
71-
72- 2.2 
73- Pronunciation 
74-
75- 2.3 
76- Verb 
77-
78- 2.3.1 
79- Conjugation 
80-
81- 2.3.2 
82- Derived terms 
--
182: Etymology
183- [ edit ] 
184-
185- From Middle Persian [script needed] ( MHYTWN-n /⁠zadan⁠/ ) (root [script needed] ( zn- /⁠zan-⁠/ ) ), from Old Persian 𐎩𐎫𐎡𐎹 ( j-t-i-y /⁠jaⁿtiy⁠/ , “ to strike , defeat ” ) (root [Term?] ( /⁠ja(n)-⁠/ ) ), from Proto-Iranian *ǰánti , from Proto-Indo-Iranian *ǰʰánti ( “ to slay , strike ” ) . [ 1 ] Cognate with Younger Avestan 𐬘𐬀𐬌𐬧𐬙𐬌 ( ja i ṇti ) , Sanskrit हन्ति ( hánti ) , English bane .
186-
187- Pronunciation
188- [ edit ] 
189-
190- ( Classical Persian ) IPA ( key ) : /za.ˈdan/ 
191-
192- ( Dari, formal ) IPA ( key ) : [zä.d̪án] 
193-
194- ( Dari, formal ) IPA ( key ) : [zä.d̪án] 

##### gazidan
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Verb 
69-
70- 1.1.2.1 
71- Derived terms 
72-
73- 1.2 
74: Etymology 2 
75-
76- 1.2.1 
77- Pronunciation 
78-
79- 1.2.2 
80- Verb 
81-
82- 1.2.2.1 
83- Derived terms 
84-
85- 1.3 
86- References 
--
156: Etymology 1
157- [ edit ] 
158-
159- From Middle Persian [Book Pahlavi needed] ( gzytn' /⁠gazīdan⁠/ ) . Cognate with Gilaki گشتن ( gaštən ) (present stem: گز ( gaz ) ), Central Kurdish گەستن ( gestin ) and Northern Kurdish gestin . Compare Old Armenian գազան ( gazan ) , an Iranian borrowing.
160-
161- Pronunciation
162- [ edit ] 
163-
164- Dari
165-
166- گزیدن 
167-
168- Iranian Persian
--
```


## [2026-09-06T15:04:13.919Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"##### bezoar\"; grep -n -i \"bezoar\" 6d735b18286ee472.txt | head -6; sed -n \"$(grep -n 'bezoar(n' 6d735b18286ee472.txt | head -1 | cut -d: -f1),+12p\" 6d735b18286ee472.txt 2>/dev/null | head -20\necho; echo \"##### gun\"; sed -n \"$(grep -n 'gun(n' 1c3471c70f712a24.txt | head -1 | cut -d: -f1),+14p\" 1c3471c70f712a24.txt 2>/dev/null | head -20",
 "description": "Etymonline bezoar and gun"
}
```


### [2026-09-06T15:04:15.706Z] TOOL RESULT

```
##### bezoar
1:URL: https://www.etymonline.com/word/bezoar
4:TITLE: Bezoar - Etymology, Origin & Meaning
6:Bezoar - Etymology, Origin & Meaning 
21: Origin and history of bezoar 
23: bezoar (n.) 
27: The name is attested later in reference to a concoction from solid matter found in the stomachs and intestines of ruminants, which was held to have antidotal qualities (1570s). Related: Bezoardic .

##### gun
```


## [2026-09-06T15:04:18.258Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '21,32p' 6d735b18286ee472.txt; echo \"=========== GUN\"; sed -n '18,42p' 1c3471c70f712a24.txt",
 "description": "Etymonline entries"
}
```


### [2026-09-06T15:04:18.309Z] TOOL RESULT

```
 Origin and history of bezoar 

 bezoar (n.) 

 1540s, "stone used as an antidote against poison," via Medieval Latin, from Arabic bazahr , from Persian pad-zahr "counter-poison," from pad "protecting, guardian, master" (from Iranian *patar- , source also of Avestan patar- , from PIE *pa-tor- , from root *pa- "to feed, protect") + zahr "poison" (from Old Iranian *jathra , from PIE *gwhn-tro- , from root *gwhen- "to strike, kill;" see bane ).

 The name is attested later in reference to a concoction from solid matter found in the stomachs and intestines of ruminants, which was held to have antidotal qualities (1570s). Related: Bezoardic .
 also from 1540s 

 Entries linking to bezoar 

 bane (n.) 
=========== GUN
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.

 About
 Who Did This 
 Sources 
 Introduction 
 Links 

 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 

 Apps

Get Chrome Extension 

Get iOS App 

Get Android App 

 Dark
```


## [2026-09-06T15:04:23.625Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n \"Gunnhildr\\|Lady Gunilda\\|gunne\\|Old Norse\" 1c3471c70f712a24.txt | head -10",
 "description": "Find gun etymology text"
}
```


### [2026-09-06T15:04:23.673Z] TOOL RESULT

```
58: mid-14c., gunne "an engine of war that throws rocks, arrows or other missiles from a tube by the force of explosive powder or other substance," apparently a shortening of woman's name Gunilda , found in Middle English gonnilde "cannon" and in an Anglo-Latin reference to a specific gun from a 1330 munitions inventory of Windsor Castle ( "... una magna balista de cornu quae Domina Gunilda ..." ). Also compare gonnilde gnoste "spark or flame used to fire a cannon" (early 14c.).
60: The woman's name is from Old Norse Gunnhildr , a compound of gunnr and hildr , both meaning "war, battle." First element from PIE *gwhen- "to strike, kill" (see bane ); for second, see Hilda .
64: Or perhaps gun is directly from Old Norse gunnr "battle." The word also was perhaps influenced by or confirmed by (or possibly from) Old French engon , dialectal variant of engin "engine."
82: Middle English bane , from Old English bana "killer, slayer, murderer, a worker of death" (human, animal, or object), also "the devil," from Proto-Germanic *banon , cognate with *banja- "wound" (source also of Old Frisian bona "murderer," Old Norse bani "death; that which causes death," Old High German bana "death, destruction," Old English benn "wound," Gothic banja "stroke, wound"), a word of no certain IE etymology. The sense of "that which causes ruin or woe" is attested from 1570s. Related: Baneful .
97: gunner 
98: gunnery 
114: "male child in relation to either or both parents," Old English sunu "son, male child," also broadly "male descendant;" also "second person of the Trinity," from Proto-Germanic *sunus (source also of Old Saxon and Old Frisian sunu, Old Norse sonr, Danish søn, Swedish son, Middle
```


## [2026-09-06T15:04:34.651Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://www.etymonline.com/word/fence\" \"https://www.etymonline.com/word/fender\" \"https://www.etymonline.com/word/defend\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%B1%D8%A7%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%84%D8%A7%D8%BA\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%DA%98%D9%86%D8%AF\" ; do\n echo \"##### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 215, Gwhen 2, nodes 2/5/10/19/20\"; done",
 "description": "Archive web sources batch 2"
}
```


### [2026-09-06T15:04:39.504Z] TOOL RESULT

```
Exit code 1
##### https://www.etymonline.com/word/fence
/home/sfmqrb/git/rishe/data/verification/sources/web/763fe0d2a2c59aaa.txt
##### https://www.etymonline.com/word/fender
/home/sfmqrb/git/rishe/data/verification/sources/web/33faff7c05b1e79c.txt
##### https://www.etymonline.com/word/defend
/home/sfmqrb/git/rishe/data/verification/sources/web/e83f66dc161c9229.txt
##### https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%B1%D8%A7%D9%85
/home/sfmqrb/git/rishe/data/verification/sources/web/3aad50020e9ed641.txt
##### https://en.wiktionary.org/wiki/%DA%A9%D9%84%D8%A7%D8%BA
/home/sfmqrb/git/rishe/data/verification/sources/web/1e2aa0d836d062be.txt
##### https://en.wiktionary.org/wiki/%D9%86%DA%98%D9%86%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/1e1dde7ff515d65f.txt
```


## [2026-09-06T15:04:42.732Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 763fe0d2a2c59aaa 33faff7c05b1e79c e83f66dc161c9229; do echo \"##### $f\"; sed -n '20,32p' $f.txt; done",
 "description": "Etymonline fence/fender/defend"
}
```


### [2026-09-06T15:04:44.763Z] TOOL RESULT

```
##### 763fe0d2a2c59aaa

 Origin and history of fence 

 fence (n.) 

 early 14c., "action of defending, resistance; means of protection, fortification," shortening of defens (see defense ). The same pattern also yielded fend , fender ; and obsolete fensive "defensive" (late 16c.). Spelling alternated between -c- and -s- in Middle English. Sense of "enclosure" is first recorded mid-15c. on notion of "that which serves as a defense." Sense of "dealer in stolen goods" is thieves' slang, first attested c. 1700, from notion of such transactions taking place under defense of secrecy.

 To be figuratively on the fence "uncommitted" is from 1828, perhaps from the notion of spectators at a fight, or a simple literal image: "A man sitting on the top of a fence, can jump down on either side with equal facility." [Bartlett, "Dictionary of Americanisms," 1848].
 also from early 14c. 

 fence (v.) 

 early 15c., "defend" (oneself); mid-15c. as "protect with a hedge or fence;" from fence (n.). From 1590s as "fight with swords," from the noun in this sense (1530s); see fencing . From 1610s as "knowingly buy or sell stolen goods." Related: Fenced .
##### 33faff7c05b1e79c

 Origin and history of fender 

 fender (n.) 

 late 13c., shortening of defender . Originally something hung over the side to protect the hull of a ship at a wharf, pier, etc. Of fireplaces since 1680s; of automobiles from 1919. Fender-bender "minor automobile accident" is from 1958.
 also from late 13c. 

 Entries linking to fender 

 defender (n.) 

 c. 1300, defendour, "one who protects from injury a champion" (early 13c. as a surname), via Anglo-French from Old French defendeor , agent noun from defendre (see defend ). The Latin word in this sense was defensor .
##### e83f66dc161c9229

 Origin and history of defend 

 defend (v.) 

 mid-13c., defenden , "to shield from attack, guard against assault or injury," from Old French defendre (12c.) "defend, resist," and directly from Latin defendere "ward off, protect, guard, allege in defense," from de "from, away" (see de- ) + -fendere "to strike, hit, push," attested only in compounds (such as offendere "to strike against; encounter;" infensus "aggressive, hostile"), from PIE root *gwhend- "to strike, kill" (source also of Hittite kue(n)zi "to kill," Sanskrit ghnanti "to kill; Greek theino "to slay, to kill;" Armenian jnem "to strike;" Lithuanian ginti "to protect, defend;" Old Irish gonaid "wounds, kills;" Welsh gwan "to thrust, hit;" Old Breton goanaff "to punish, sting").

 It is attested from c. 1300 as "fight in defense of" (someone or something). From mid-14c. as "defend with words, speak in support of, vindicate, uphold, maintain." In Middle English it also could mean "forbid, prohibit; restrain, prevent." In the Mercian hymns, Latin defendet is glossed by Old English gescildeð . Related: Defended ; defending .

 also from mid-13c. 

 Entries linking to defend
```


## [2026-09-06T15:04:51.407Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"##### bahram\"; grep -n -A6 \"Etymology\" 3aad50020e9ed641.txt | sed -n '1,40p'\necho; echo \"##### kalagh\"; grep -n -A8 \"^ Etymology\" 1e2aa0d836d062be.txt | sed -n '1,40p'",
 "description": "Wiktionary Bahram and kalagh"
}
```


### [2026-09-06T15:04:51.471Z] TOOL RESULT

```
##### bahram
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
--
151: Etymology
152- [ edit ] 
153-
154- From Middle Iranian (see Parthian 𐭅𐭓𐭉𐭇𐭓𐭌 ( wryḥrm /⁠Wahrām⁠/ , “ war god, god of victory ” ) and Middle Persian 𐭥𐭫𐭧𐭫𐭠𐭭 / 𐭥𐭠𐭧𐭫𐭠𐭬 ( ʿlḥlʾn / ʿʾḥlʾm /⁠Wahrām⁠/ ) ), from Avestan 𐬬𐬆𐬭𐬆𐬚𐬭𐬀𐬖𐬥𐬀 ( vər ə θraγna , “ smiting of resistance, victorious ” ) , from Proto-Iranian *Wr̥tragnáh , from Proto-Indo-Iranian *Wr̥tragʰnás .
155-
156- Related to Sanskrit वृत्रहन् ( vṛtrá-hán , “ smiter of vṛtra , i.e. smiting the cause of covering/hiding ” ) . In pre-Islamic Iran mythologically conflated with the Persian Gulf narrows (which oral tradition considered to be a remnant of the "obstruction" that was overcome by Verethragna), hence in Iranian folk etymology incorrectly identified with the toponym "Bahrain."
157-

##### kalagh
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- Toggle the table of contents 
--
152: Etymology
153- [ edit ] 
154-
155- From a Proto-Iranian root not attested in Middle Persian. Cognate with Baluchi کلاگ ( kalág ) , Mazanderani کلاج ( kalāǰ ) , Gilaki کلاچ ( kəlāč ) , Southwestern Fars قلاغ ( qalâğ ) , قلا ( qalâ ) , Northern Luri قلا ( qelā ) , Ossetian халон ( xalon ) . Probably ultimately onomatopoeic, but perhaps from Proto-Indo-European *ḱer- ( “ crow ” ) ; compare Latin corvus , Ancient Greek κόρᾰξ ( kórăx ) , Proto-Germanic *hrabnaz .
156-
157- Pronunciation
158- [ edit ] 
159-
160- ( Classical Persian ) IPA ( key ) : /ka.ˈlaːɣ/
```


## [2026-09-06T15:05:02.944Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -A8 \"^ Etymology$\" 1e1dde7ff515d65f.txt | head -20; echo \"--- any\"; grep -n -i \"nižand\\|Middle Persian\\|Etymology\" 1e1dde7ff515d65f.txt | head -10",
 "description": "Wiktionary nazhand"
}
```


### [2026-09-06T15:05:04.638Z] TOOL RESULT

```
--- any
```


## [2026-09-06T15:05:07.249Z] TOOL CALL #81: Bash

```json
{
 "command": "SP=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 215 -l 215 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf $SP/pg215hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('$SP/pg215hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(0.20*w),int(0.155*h),int(0.48*w),int(0.20*h))).save('$SP/crop_node1.png')\nim.crop((int(0.20*w),int(0.555*h),int(0.55*w),int(0.63*h))).save('$SP/crop_node12.png')\nim.crop((int(0.20*w),int(0.70*h),int(0.75*w),int(0.78*h))).save('$SP/crop_germ.png')\n\"",
 "description": "Crop page regions at 600dpi"
}
```


### [2026-09-06T15:05:12.283Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-06T15:05:14.745Z] TOOL CALL #82: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_node1.png"
}
```


### [2026-09-06T15:05:14.769Z] TOOL RESULT

```

```


## [2026-09-06T15:05:18.425Z] TOOL CALL #83: Bash

```json
{
 "command": "SP=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('$SP/pg215hi.png'); w,h=im.size\nim.crop((int(0.20*w),int(0.195*h),int(0.50*w),int(0.235*h))).save('$SP/crop_varathra.png')\nim.crop((int(0.24*w),int(0.735*h),int(0.45*w),int(0.775*h))).save('$SP/crop_guthjo.png')\n\"",
 "description": "Crop varathra and guthjo lines"
}
```


### [2026-09-06T15:05:20.984Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:05:23.732Z] TOOL CALL #84: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_varathra.png"
}
```


### [2026-09-06T15:05:23.746Z] TOOL RESULT

```

```


## [2026-09-06T15:05:28.139Z] TOOL CALL #85: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_guthjo.png"
}
```


### [2026-09-06T15:05:28.151Z] TOOL RESULT

```

```


## [2026-09-06T15:05:40.308Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### NYB zahr/ozadan/zadan\"; grep -n \"zahr\\|ozadan\\|ōzadan\\|'wzdn\\|zatan\" NYB_vol2_glossary.txt | head -12\necho \"### HUB 871 zahr\"; awk 'BEGIN{RS=\"\\f\"} /zahr/ {print \"leaf=\"NR\": \"substr($0,1,0)}' HUB.txt | head -5\ngrep -n \"zahr\" HUB.txt | head -8",
 "description": "Grep Nyberg and Hübschmann"
}
```


### [2026-09-06T15:05:42.211Z] TOOL RESULT

```
### NYB zahr/ozadan/zadan
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
809:aviš [?wbš] adv. l. used instead of the prep. 6 if it refers back to an encl. pron. in the beginning of the sentence: zahr i-š ~ fréstit the poison that was sent to her 918; kū-t... ~ ne rasét lest ... shall come upon thee 688-?; api-§ ... ~ barét bring for him! 7489 = bé-§ ~ barét 76’; puhr i-Š ... ~ mat the punishment that has come upon him 741^; cigón ka-šan... ~ hilénd as if one poured ... upon them 101291, — 2. as a substitute for the prep. 6 + the encl. pron. 3d p. sg. -&: 14-16, 413.15, 727, ete. passim; taking up the rel. pron. 4226, 7213 v.s. v. ke. — Ps. ’wbsy; MPrs ’wys, from an OP adv. *abišā or *abisah derived from Av. (87 sg.) adbi, aiwi = OP abiy, as patiš (q. v.) from pati (cf also haciš : hac). I maintain my opinion expressed in HP II, 212; a
1287:distak [dystk'] *treated, manipulated, or the like: pat Hēšm zahr ~ "treated with (the demon) Wrath's poison 2516-17 = 2814, — In the edition the first letter is a marked d, hence the reading dystk' is cogent. Because of -ist- this must be a SW form corresponding to a NW form with -i$t-, but its meaning in this context make it impossible to combine it with NW dištan (v. next w.): a weapon is not “built” or “‘formed’’. It would be tempt- ing to connect it with Skr dih- ‘to daub, to smear', but the corresponding Av. (673) dačz- has other significations (cf diz), and the Phl. renderings of it (Vd 39.13.18, 733. 1536) have run wild and are no more recognizable (they can scarcely be brought together with dés-, v. the next w.).
1451:age DkM 6989; tat pat dātistān(ūman>- deh či veh tuvän zatan u éraxtan cigón ka-š pat davreh u drusteh apäk gēbāh through righteousness thou art better able to defeat him and make him lose the case than if thou speakest to him coarsely and roughly (cf s. v. davr) PR 573; — pres. pass. 3d p. sg. éraxtét he is pronounc- ed guilty, opp. buxtet he is acquitted, v. Bthl, ZsR IV, 8; Paz. buxted ... érexted SGV III, 26; kē rāstēh rad pat xudstak eraxtet, ah veh cigon kē družeh rād pat ruvān éraxtét he who suffers loss of prop- erty because of his righteousness is better than the one who suffers the loss of his soul (forfeits his soul) because of his falsity PR 26$-9.] — Two vbs. seem to have coalesced here: 1) črtatan ērēc-, cf Paz. érexted and the caus. érezinidan ‘to condemn’ SGV XI, 257, most probably < abi- + Av. (1479 sq.) raék- ‘to leave in the lurch, to abandon to destruction’ (Bthl IF XII, 112sqq.); 2. éraxtan érang-, most probably a denom. of érang, črangčh 'trouble, delusion' (Paz. ŠGV X, 58 ete.) < *abi-ranga-, cf. an-črang, ranj, ranjak; MPrs ‘yrat, “yrnz- ‘to combat’, Verbum 199. (Bthl, l.c. adopted the reading érazt).
1616:ganak [gn'-’k, gn'k], ganài [gn’y], gana [gn'-] 1. murderer, of a human being 5414, — 2. ~ menči the Evil Spirit, designa- tion of Ahriman 46%’, 642-7. 659. 6626. 67 7.14. 1526. 105. 1021-2.16.1 7, 1034-29-21, 10512; without ménói: gizistak ~i druvand 8012. 9025, — From gan- ‘to slay’, v. zatan; cf BdA p. 4811-12; ganäkeh<i)> hast zatäreh. — ~ mēnēt is the Milr. translation of Angra- mainyu-, Ayra-m., v. Ahriman, and ~ corresponds to angra-, ayra-, which is rendered in the Skr. vs. by hantar. Paz. gana; the Skr. vs. only transliterate. Widely differing readings and interpre- tations of ~ have been proposed, v. Bthl, MirM I, 18-28; Bailey, BSOS VII, 1935, 755-759. The above interpretation, which restores the Paz. reading and respects the tradition, is due to Bailey (l.c.; ZP 20-21) I now give up my
1975:hazar [LP, with a P resembling the OAram. and Palmyr. forms of it; for Aram ’LP] thousand, — Av. (1796) hazagra- < *ha- zahra-, Skr sahasra-.
2126:janišn [ynšn'] the act of slaying 1018 (correct initial g- to y- with one dot be- low). — The NW form of zantšn, v. zatan. The passage is not quite clear. The text of the MSS: MNW-8?n' ynšn' MN-#’n' = kē-šān janišn hac-isän is ambiguous: ‘those from whom slaughter had arisen’? (but haci$ would have been the correct construction), ‘those of them (hac-ısän partitive, seems rather superfluous) by whom slaughter is done’ ? My emendation MRK*-n' = MLK?-’n' = $ähän: ‘those kings from whom slaughter had arisen’ implies the difficulty that MRK’ for MLK” is so far only attested in the in- scriptions, and only in royal titles. Cf, on the other hand, BdA p. 22418-16; čišan kē-šān xvat-*āyēn [for -divén 1] dāmēh rād
2220:kārēcār [k'lyc'l] battle, combat 1198, with: ~ % 8?9, 4 apäk 108%; pat ~ bē dzatan to kill in battle 9722; ~ xtinrécisnéh (q.v.) 1312-13, kéasisn u kārēcār 901; ~ kartan to fight 25-29, passim. 511. 95!1; vas ~ u ozanišn apāk ... kart 138-4; ~ dästan to keep contending, wrestling 329-19; be 0 m~ ìi... šutan to engage in battle with 9617-18 ete. — MPrs kryer, krer (S); Paz. kārīžār, NP kürzür; käre- cas. obl. of kar < OP kära- ‘army’, + cär from Av. (449) 5kar- ‘to move’, cf NP caridan ‘to graze’ and vicar-.
2844:Ozatan
2853:özatan [?wetn'; YKTLWN-tn'] özan- (YKTLWN-x, for ózanet 29%) to kill; cond. 3d p. sg. hakar-im . . . nē dzat hah 3221, 3d pl. hakar-im ... ne ozat hand 335; — pt. pass. dzatak killed: hunuskan ozatak gurg a bitch wolf whose cubs had been killed 4927; hunuskän özatak dit saw the cubs killed 50!; — v. n. dzanisn 1. pred. : be ozanišn is to be killed 108; 2. as a subst. : kārēcār u ozanišn 134; pat ozanišn āivēnak 1032, v. divénak. — Av. (491) ava-gan-, pres. -jan-, pt. -jata-; MPrth
2855:Ozatan
2857:^wjdn "wjn- (MHC); MPrs 'wzdn "wzn-; Paz. awazadan awazan-. V. also janišn, ganäk and apa-Zand.
### HUB 871 zahr
leaf=47: 
leaf=82: 
leaf=144: 
leaf=204: 
leaf=207: 
1194:273. Die altere Form pddzahr siehe bei Vullers s. v.
1195:pazahr, Polak, Persien II, 375, paz. 'pad{a)zah(a)r
1196:*Gegengift' Shk. 261. Auf dieses padzahr (das aber
1210:pddzahr *6egengift'; np. padas 'Vergeltung' = phi. pa^-
2485:in deraselben Dialect auch zu zahr, zahra werden
2490:zahr 'Gift' = kurd. mhr, iar (ZDM6. 38, 72, 107), zah'r
2492:(wie ohne Weiteres fiir zahr gelesen werden kann) auf
2494:leite zahra *6alle* (bal. LW. zahrak *Gallenblase') mittelst
```


## [2026-09-06T15:05:49.126Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2480,2510p' HUB.txt; echo \"=== pazahr ===\"; sed -n '1190,1215p' HUB.txt",
 "description": "Hübschmann zahr"
}
```


### [2026-09-06T15:05:49.206Z] TOOL RESULT

```
678. Gegen Noldeke's Deutung ist einzuwenden, dass ap.
^zarta- und *zartaka- im Neup. zu zard und zarda
werden mussten und auch geworden sind, vgl. Nr. 656:
zard gelb', zarda *6alle' (bal. LW. zard gelb*, zardd
*Eidotter , zarddi *6alle*), dass sie mithin nicht zugleich
in deraselben Dialect auch zu zahr, zahra werden
konnten. Der Ubergang von ap. ri m np. rd ist laut-
gesetzlich, derjenige von rt in hr findet sich nur in
gewissen rituellen WSrtern, die nicht neupersisch sind,
wie ich im zweiten Theile zeigen werde. Ich fiihre daher
zahr 'Gift' = kurd. mhr, iar (ZDM6. 38, 72, 107), zah'r
Socin, kurd. Samml. II, p. 311, arm. LW. iahr, phi. mhr
(wie ohne Weiteres fiir zahr gelesen werden kann) auf
*ja&ra- = skr. ^hatra- 'Mittel zum TOdten zuriick und
leite zahra *6alle* (bal. LW. zahrak *Gallenblase') mittelst
des Suffixes a (= phi. ak) davon ab, was doch das
natiirlichste ist, wahrend NOldeke dem Worte zahr^
das sich nur in der Bedeutung 'Gift' nachweisen lasst,
als urspriingliche Bedeutung 'Galle' zuschreiben muss,
um zahr = zahra auf ap. "^zartor- = "^zartaka- gelb'
zuriickfiihren zu k5nnen. Eine Neubildung ist zahra
'Galle' so wie so fiir nicht mehr vorhandenes ''^zdr =
zd. zaras(6a) = x^^^^^ X^^Vf d. GaUe etc.
680. In den Nachtragen bemerkt Horn sehr richtig, dass
np. ztr 'hoch, hohe Stimme, hellste Saite' (= arm. zU
Sopran") mit f (nicht B) zu sprechen und also von
zer 'unter' zu trennen ist. Vgl. die LW. afgh. zBr
'under gegeniiber zir {jlr) 'the fine or highest note of
a lute, the treble in music*.
681. Zu zirak 'scharfsinnig, schlau = phi. zTrak (oder Strak)— 72 -
Ganj. 61. p. 10 gehSren als LW. kurd. zlr^ zlrek ge-
=== pazahr ===
para^ *das Letzte, Ausserste, Ende* noch zu zd. para-
'Schuld' (ZPGl.). Horn stellt es jetzt zu lat. j>ar« =
*^«- KZ. 33, 443.
3*— 36 —
273. Die altere Form pddzahr siehe bei Vullers s. v.
pazahr, Polak, Persien II, 375, paz. 'pad{a)zah(a)r
*Gegengift' Shk. 261. Auf dieses padzahr (das aber
*6egen-gift' bedeutet) sowie auf padsdh *Konig' stiitzen
die pers. Lex. falscblich ihr pad 'Schiitzer (s. Nr. 265).
274. Zu pas *Wache, Nachtwache' vgl. Nr. 341: pahra^
Skr. pdtra- (Rgv. 1, 121, 1 nach Say. = pdtar 'Be-
schiitzer !) bleibt besser weg.
274 bis jfp pasaoct im Uiiterschied von paz. phi. pasaxt
Shk. 262 - 263, Gl. and Ind. 103 etc. miisste aus ^patsaxf
entstanden sein, wie pasCtxt aus patsCixt,
275. Neben dem gewohnlichen phi. pasaxv (61. and Ind.
p. 103) ist nach np. und paz. pasux (Shk. 263, Min.
haufig) ein phi. *pasaxv anzusetzen, jenes aus *patsaxv,
dieses aus *patsaQcv (vgl. Sirm, patasxani 'Antwort').
Dieses pdt (aus ap. *pCitiy) liegt noch vor in np. paz.
pddzahr *6egengift'; np. padas 'Vergeltung' = phi. pa^-
ddhisn ; np. bddafrah, lies padafrah Tergeltung, Strafe',
paz. padafrah, phi. patafrds; phi. patrazm Yatk. i.
Zar. 66, Anm. 61 = arm. paterazm *Krieg, Kampf,
Schlacht' (vgl. np. razm *Kampf ') , entsprechend im
Avesta paiti in paitivaka- = *Gegen-rede, Erwiederung
```


## [2026-09-06T15:06:03.977Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### LKT bezoar\"; grep -n -i \"bezoar\\|badzahr\\|bāzahr\\|pādzahr\" LKT.txt | head -6\necho \"### PLA bazahr\"; grep -n -i \"bazahr\\|bādzahr\\|zahr\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -8\necho \"### AFM bazahr\"; grep -n \"بازهر\\|بادزهر\" AFM_pages.txt | head -5\necho \"### KLN gun\"; grep -n \"^gun,\\|^gun (\" KLN_1966.txt | head -3",
 "description": "Grep Lokotsch, Asbaghi, Addi Shir, Klein"
}
```


### [2026-09-06T15:06:04.070Z] TOOL RESULT

```
### LKT bezoar
3674:160.5.  Pers.  pädzähr: 'Gegengift,  Bezoar'  [päzähr  Horn  NpEt
3677:S.  62,  Nr.  273  oder  'Gift  antreibend'  aus päd,  s.  hier  Nr.  1604,  und  zähr  'Gift', ebenda  S.  150,  Nr.  678];  man  versteht darunter  hauptsächlich  gewisse  harte Abscheidungen  aus  tierischen  Körpern, denen  die  Wiriiung  von  Gegengiften  zu- geschrieben wird,  insbesondere  aus  dem Magen  einer  Wildziege  in  der  pers.  Pro- vinz Lar.  Hieraus  ar.  bädizahr,  bäzahr und  nach  magribinischer  Aussprache  mit Imäla  [a  >  e]  bezahr,  woraus  die  Ärzte des  MA.  die  ihre  Kunst  den  Westarabern verdankten,  mlat.  bezoar  machten:  sp. bezaar,  sj).  pg.  kat.  bezoar,  frz.  bezoar, it.  bezzoar,  bezzoarre,  belzuar;  engl,  be- zonr,  ndl.  bezoar  'Ziegenstein  im  Magen der  Wiederkäuer',  dtsch.£f2;oar'Gemsen- kugel'.  Im  Russ.  wurde  bezar,  bezuj sowie  daraus  abgeleitet  zaberzat  Bezeich- nung eines  Edelsteins  [vgl.  Zapiski  der Oriental.  Sektion  der  Kais.  Russ.  Ar- chäol.  Ges.  XIV.  1.  Lieferung:  K.  Ino- strantzew,  Über  zwei  allrussische  Be- zeichnungen für  Edelstein].  [DE  239/240. Dozy  Oost  25/26.  Eguilaz  345.  Devic DEt  68/69.    Hobson-Jobson  40/41.
5765:besehein  j.  2210 Beteigetize  St.  695 Betel  2149 betucht  j.  267 Betuchter  j.  267 Betuecliter  j.  267 Bezoar  1605 Bisam  293 ii/Mse  1647 Boback  181 ß��c/i^r  j.  180 Bombasin  16 17 Bonze  331 Borax  356 Boretsch  13 Borretsch  13 £os  j.  184  a Bronze  1657 Burnus  365 Burrich  13 5?<sa  376 Buxkin  324
7425:halascius  151 balsatnum  293 bambagium  1617 Barabbas  220 ftarca  2148 harracanus  250 basilica  (vena)  262 bezoar  1605 birrus  365 bisamutn  293 bombacium  1617 borrago  13 bronzium  1657 brundisinum  Caes)  1657 brunitius  1657 buccina  347 burgns  362 burrus  365
7492:bezoar  1605
8067:bezoar  1605
### PLA bazahr
3422:badähan 33 bädzahr 
3462:Br - bädzahr: "Bezoarstein" pers. ı1 aus dem pers. „w>h pädzahr mp. 
3465:Ye oo padzah ® m. pät "gegen, anti" + zahr "Gift", frz. bezoard, 
3695:e;l - bäzahr = bädzahr s. bädzahr . 
6528:„eis\e - Yäwzah : "Orogen" aus dem pers. ‚o,,1/gäwzahr Tmp.\gyp gozihr. 
6531:er" - $äwzahraß = bäwzahr s. bäwzahr . 
7840:Yauzbüyä 99 auzahr 
7882:2/2 - $auzahr: "Drogen" aus pers. „+, Züzahr 7 mp. )9r gözihr 8, 
### AFM bazahr
4156:بادزهر ١‏
### KLN gun
```


## [2026-09-06T15:06:12.524Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Gunnhildr\\|Gunilda\\|gunnr\" KLN_1966.txt SKT.txt | head -6\necho \"### KLN fence/defend\"; grep -o \"fence,  n\\..\\{0,400\\}\" KLN_1966.txt | head -2; grep -o \"defend,  tr\\..\\{0,500\\}\" KLN_1966.txt | head -2",
 "description": "Klein gun/fence/defend"
}
```


### [2026-09-06T15:06:14.191Z] TOOL RESULT

```
KLN_1966.txt:10609:beat,  strike’,  Gk.  Oetvetv  (for  *ghwen-yein), ‘to  strike’,  cpAvot;  (for  *ghwonos),  ‘murder’.  Alb. gan,  ‘I  hunt’,  OSlav.  zenQ,  gunati,  ‘to  drive’, Lith.  genu ,  gihti,  ‘to  drive’,  geniu,  geneti,  ‘to  cut off  branches’,  OIr.  gonim,  ‘I  strike,  kill’,  gain, ‘a  wound’,  ON.  gunnr,  gudr,  OE.  gud,  ‘war, battle’,  gudfana,  ‘banner’.  Cp.  defense,  fend,  of¬ fend,  offense.  Cp.  also  phoenix,  the  first  element in  gonfanon,  Gunther,  and  the  second  element in  Bellerophon,  Tisiphone,  Triphasia  and Edith.  Derivatives :  defendant  (q.v.),  defend-er,  n. defendant,  adj.,  defending;  n.,  the  accused  party (law).  —  F.  defendant,  pres.  part,  of  defendre, fr.  L.  defendere.  See  defend  and  -ant. defenestration,  n.,  the  act  of  throwing  out  of  a window.  —  Formed  fr.  pref.  de-,  L.  fenestra, ‘window’  (see  fenestra)  and  suff.  -ation.  Cp. fenestration.
KLN_1966.txt:12645:edit,  tr.  v.  —  Back  formation  fr.  editor  (q.v.) Edith,  fern.  PN.  —  OE.  Eadgyth,  compounded of  ead,  ‘wealth,  prosperity,  happiness’,  and  giid, ‘war’.  For  the  first  element  see  Edgar  and  cp. words  there  referred  to.  OE.  giid  is  rel.  to  OHG. gund-,  ON.  gunnr,  gudr,  ‘war’,  and  cogn.  with Gk.  8-etveiv,  ‘to  strike’,  <povo;,  ‘murder’,  L. -fendere,  ‘to  thrust,  strike’.  See  defend  and  cp. the  words  there  referred  to. edition,  n.  —  F.  edition,  fr.  L.  editidnem,  acc.  of editio,  ‘a  bringing  forth,  publishing’,  fr.  edere, ‘to  give  out,  bring  forth,  publish’,  formed  fr.  e-
KLN_1966.txt:16421:gonfalon,  n.,  an  ensign.  —  OF.  (=  F.),  formed with  dissimilation  from  gonfanon  (q.v.) gonfalonier,  n.,  one  who  bears  the  gonfalon.  — F.,  fr.  gonfalon.  See  prec.  word  and  -ier. gonfanon,  n.,  a  gonfalon.  —  F.,  fr.  OHG.  gundfano (cp.  OE.  gupfana,  ON.  gunnfani),  lit.  ‘banner  of war’,  fr.  gund,  gunt,  ‘war’,  and  fano,  ‘flag,  ban¬ ner’.  The  first  element  is  rel.  to  OE.  gud,  ON. gudr,  gunnr,  ‘war’,  fr.  I.-E.  base  *gwhen-,  ‘to strike’,  whence  also  Gk.  Helvsiv,  ‘to  strike’,  L. de-fendere,  ‘to  ward  off,  keep  away,  defend, guard,  protect’ ;  see  defend  and  cp.  the  first  ele¬ ment  in  Gunther.  The  second  element  is  rel.  to OE.,  Goth,  fana,  ‘cloth’,  and  cogn.  with  L.  pan- nus,  ‘piece  of  cloth’ ;  see  pane,  ‘sheet  of  glass', and  cp.  fanon.  Cp.  also  gonfalon, gong,  n.  —  Malay  gong,  of  imitative  origin.  Cp. gum-gum.
### KLN fence/defend
fence,  n.  —  The  British  spelling  of  defense, defend,  tr.  and  intr.  v.  —  ME.  defenden,  fr.  OF. defendre  (F.  defendre),  fr.  L.  defendere,  ‘to  ward off,  keep  away,  defend,  guard,  protect’,  fr.  de- and  -fendere  (found  only  in  compounds),  ‘to thrust,  strike’,  fr.  I.-E.  base  *g" hen-,  ‘to  strike’, whence  also  OI.  hdnti,  ‘he  strikes,  kills',  pi. ghnanti,  ‘they  st
fence,  n.  —  ME.  defense,  defence,  fr. OF.  defense  (F.  defense),  fr.  VL.  defensa  (cor¬ responding  in  sense  to  L.  defensio),  ‘defense’, prop.  fem.  pp.  of  L.  defendere,  used  as  a  noun. See  defend  and  -ce.
defend,  tr.  and  intr.  v.  —  ME.  defenden,  fr.  OF. defendre  (F.  defendre),  fr.  L.  defendere,  ‘to  ward off,  keep  away,  defend,  guard,  protect’,  fr.  de- and  -fendere  (found  only  in  compounds),  ‘to thrust,  strike’,  fr.  I.-E.  base  *g" hen-,  ‘to  strike’, whence  also  OI.  hdnti,  ‘he  strikes,  kills',  pi. ghnanti,  ‘they  strike,  kill',  Hitt,  kuenzi,  ‘he strikes,  kills’,  kunanzi,  ‘they  strike,  kill’.  Arm. gan,  gen.  gani,  ‘a  beating,  thrashing’,  jnem,  ‘I,
```


## [2026-09-06T15:06:28.045Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=4878{n+=gsub(/\\f/,\"\")} END{print \"KLN leaf for bezoar line:\", n}' KLN_1966.txt\ngrep -o \"gun,  n\\.,  a  firearm.\\{0,600\\}\" KLN_1966.txt | head -2\necho \"### SKT gun\"; grep -o \"^GUN.\\{0,400\\}\" SKT.txt | head -2",
 "description": "Klein leaf + gun; Skeat gun"
}
```


### [2026-09-06T15:06:30.314Z] TOOL RESULT

```
KLN leaf for bezoar line: 100
### SKT gun
GUN.
```


## [2026-09-06T15:06:35.066Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^GUN\\.\" -A6 SKT.txt | head -12\necho \"### KLN gun\"; grep -n \"gun,  n\" KLN_1966.txt | head -3",
 "description": "Skeat GUN and Klein gun"
}
```


### [2026-09-06T15:06:35.136Z] TOOL RESULT

```
8119:GUN.
8120-Guillotine.  (F.;  Vsm«d  aSttt  a  plqrii- cian,y.  /.  CtiiUotm,  died  a.  d.  1814.  Flal used,  1793
8121-Guilt,  crime.    (E.)     M.  E.  gilt.     AS. gyli,  orig.  a  fine  for  a  trespass;  hence, Uc«pa«.      Allied  lo  AS.  gtldan  (pi,  t-  pl» gji/ihrn),  to  pay,  yield ;  see  TSeld.
8122-Guinea.  (African,^  First  coined  (4 African  gold  from  the  Guimea  coast,  aa 1 66 J.  Der.  piinea/tnt)/.  ^  Thtgninet' pig  is  from  ^.  America;  so  that  it  my mean  Guiana  fig.
8123-Guise  ;  see  Wiae»  sb.
8124-Guitar ;  see  CMthem.
8125-Gules ;  see  Gullet.
### KLN gun
16875:gummous,  adj.,  pertaining  to,  or  resembling,  gum, gummy.  —  L.  gummosus,  ‘gummy’,  fr.  gummi. See  gum,  ‘a  viscid  substance’,  and  -ous. gumption,  n.,  shrewdness,  common  sense  {col- —  Orig.  Scot.;  of  uncertain  origin, gun,  n_  —  ME.  gunne,  gonne,  prob.  from  the  fern. PN.  Gunne,  shortened  from  the  name  Gunhild, which  was  applied  to  a  war  engine  (in  I33»30- For  sense  development  cp.  the  gun  names Mons  Meg,  Big  Bertha,  etc.
25447:nine,  adj.  —  ME.  nigen,  nine,  fr.  OE.  nigon,  nigan, rel.  to  OS.  nigun,  OFris.  niugun,  nigun,  ON .  niu, Dan.  ni,  Swed.  nio,  dial.  Norw.  nio,  nie,  MLG., Du.  negen,  OHG.,  MHG.  niun,  G.  neun,  Goth. niun,  ‘nine’,  and  cogn.  with  OI.  nava,  Avestic nava,  Toch.  hu,  Arm.  inn  (for  *envan),  Gk.  i'J'du. (for  *evve"x),  Alb.  mnde,  L.  novem  (for  *  no¬ yen  ;  the  change  of  -n  to  -m  is  due  to  the  analogy of  L.  septem,  ‘seven’,  decern,  ‘ten’),  Lith.  devyni, Lett,  dewihi,  OSlav.  dev?ti  (the  change  of  the initial  n-  to  d-  in  the  Balto-Siavonic  languages is  due  to  dissimilation,  n-n  having  become  d-n), OIr.  noi  n-,  W.,  Co.  naw,  ‘nine’.  All  these  words derive  fr.  I.-E.  *enewen,  *enwn,  *newn,  ‘nine’, and  are  prob.  cogn.  with  OI.  navalt,  Gk.  v£oq (for  *v£fo? ),  L.  novus,  etc.  ‘new’,  a  supposition corroborated  by  the  fact  that  I.-E.  *oktou,  eight ,
35020:shogun,  n.,  title  of  the  military  governors  of  Japan until  1868.  —  Jap.  shogun,  lit.  ‘leader  of  an army’,  fr.  Chin  chiang-chiin,  ‘leader  of  an  ar¬ my’.
```


## [2026-09-06T15:06:43.777Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### IEC gwhen\"; grep -n \"g^hen\\|guhen\\|gṷhen\\|ghen-ō\\|hen- 'strike\" IEC.txt | head -5\ngrep -o \"g.hen-.\\{0,200\\}\" IEC.txt | head -8\necho \"### WLD Bd1 679\"; awk 'BEGIN{RS=\"\\f\"} NR==688{print substr($0,1,900)}' incoming/WLD/WLD_Bd1_pages.txt",
 "description": "Mann and Walde-Pokorny"
}
```


### [2026-09-06T15:06:47.569Z] TOOL RESULT

```
### IEC gwhen
2105:de-guhenio (d-guhen-), see de-, guhen- (a form of doubtful composition) Skt. cf. ksanómi, ksanumi *wound, kill; Gk. kteínó ‘kill’; Arm. cf. (?) čgank ‘effort’, Cgnim "Lol
4652:ghend-, see ghed-, ghnd-. (The evidence is ambig.) Gk. cf. kheísomai ‘will contain’; Alb. gjej (?) “find; guess? beside gjíndem “am found, oc- cur’; Lat. cf. prae-hendo; Pol. cf. Zadac dest. re’; Li. cf. pa-si-gendu, inf. -gesti, pf. -gedau *keep watch, observe'
4653:ghendh- (ghondh-, ghndh-) ‘smell, stink’? Li. gendu, gesti ‘rot, turn bad’; (o-gde in) Skt. gandháh ‘smell’; Per. gand, id.; gande ‘stinking’; gandana ‘leek’; Arm. (?) gon£ (i- st. adj. *mangy"); (z-gde in) Go. gund ‘canker’; OHG gunt, OE gund ‘pus’
5473:guheguhon-, redup. theme of guhen-, q.v. Vedic. 3s pres. subj. jaghánat; MIr. geoguin, aor. 3s; Hom. cf. épephnon, aor. isg.
5477:guhen- radical of general sense: “drive, beat, kil. WP I, 679. Cf. guhn- Verbal forms: Skt. hánmi: Av. jainmi; OPer. -janam; Per. zanam, inf. zadan; Arm. $Énem (thematic: ‘beat: gin ‘whip, rod); fanam ‘strive’: athematic; beside ğan, Let, ‘effort’; Hitt. kwemi (for *kwenmi, 3pl. kunanci: Skt. ghnanti);; Gk. (thematic) théno, iotacized:
guhen-), see de-, guhen- (a form of doubtful composition) Skt. cf. ksanómi, ksanumi *wound, kill; Gk. kteínó ‘kill’; Arm. cf. (?) čgank ‘effort’, Cgnim "Lol
guhen-, q.v. Vedic. 3s pres. subj. jaghánat; MIr. geoguin, aor. 3s; Hom. cf. épephnon, aor. isg.
guhen- radical of general sense: “drive, beat, kil. WP I, 679. Cf. guhn- Verbal forms: Skt. hánmi: Av. jainmi; OPer. -janam; Per. zanam, inf. zadan; Arm. $Énem (thematic: ‘beat: gin ‘whip, rod); fanam ‘stri
guhen- Vedic hántvà “to be slain’; OCS Zetva Char. vest”, lit. cutting")
guhen-, q. v. Cf. Gk. phtháno ‘forestall’, a synthetic cpd.; Alb. për- zàj, T pér-zé ‘chase’; OCS Zinjo Zeti ‘mow’)
guhen-, q. v. Av. yno, ynyo, adj. ‘striking, lethal; Gk. cf. phtháno ‘forestall’; Go. wunns “pain? (f. i-st.); MHG wünne ‘pasture’; OCS cf. Ze-tva, f. "har, vest" beside günati, gnati, inf. ‘drive’; cf. als
guhen- & WP I, 680 Skt. hatih; Av. jaitis; Go. cf. wunds, OHG wunt ‘wounded’; cf. OHG wunta ‘wound’; ON und, f. i-st., id.; OCS cf. Zetva ‘harvest’; Li.
guhen- Skt. batáh; Av. jato; Oss. cf. qád-gom, cpd. *wound'; Hom. Gk. cf. Areiphatos 'slain by Mars’; Alb. (ambig.) gând ‘slight, offence’; Ir. gunta, pp. ‘wounded’ beside LOIr. gat ‘rob- bery’ (cf. -tis ab
### WLD Bd1 679
                                              gjheu-                                                    679

ahd. gaman n. „Spiel, SpaB, Lust" u. dgl.     kaum mit Recht aber in aisl.
                                                            ;


ijumarr „Widder“ u. dgl., die wegen mit gr. yipaiga verwandten Worten
wie norw. gimber (aisl. gymbr) f. ,.junges weibliches Schaf" eher um- als
Ablautneubildung zu -im- enthalten. Ygl. aber oben S. 548.
   Wiedemann BB. 27, 202 vergleicht die germ. Worte unter idg. gliem(b)-
abweichend mit alb. zemere. zembere „Herz, Wille, Leib", zemerdk, zem-
beralc „jahzornig", doch ist dei' Yergleich mit d&epfiovon in der Bed. viel
treffender.


1.    gKlien- „schwellen, strotzen, Fiille".
     Ai. O-hands „schwellend, strotzend, xippig, geil", ghand- „kompakt, dicht,
dick",      m. „kompakte Masse" (nicht als „fest zusammengesehlagen" =
```


## [2026-09-06T15:06:55.483Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==688{print}' incoming/WLD/WLD_Bd1_pages.txt | sed -n '12,60p'",
 "description": "WLD Bd1 p.679 gwhen strike"
}
```


### [2026-09-06T15:06:57.403Z] TOOL RESULT

```
beralc „jahzornig", doch ist dei' Yergleich mit d&epfiovon in der Bed. viel
treffender.


1.    gKlien- „schwellen, strotzen, Fiille".
     Ai. O-hands „schwellend, strotzend, xippig, geil", ghand- „kompakt, dicht,
dick",      m. „kompakte Masse" (nicht als „fest zusammengesehlagen" = ghand-
„erschlagend, m. Keule", Uhlenbeck Ai. Wb. 84; s. *cfihen- „schlagen“)
  npers. u-gandan „anfiillen“, Ciganis „voll“; gr. evftevyg evrcaftovou, loyvgd
                                                                                                        2
Hes., ev&eveco „gedeihe, bin in Bliite              und Kraft", evdeveta           ,,   Fiille.   blxihen-
der Zustand", dehnstnfig jon. svdgvgg „reichlich, in Fxille", jon. att. ev'&y-
veco „gedeihe, bin in Bliite und Kraft", evdgvia „Fiille“ {-!h:v- kaum nach
Sommer Gr. Ltst. 66 aus -dyv- nacli o&evog), o-stufig KQe\*T\a-cp6vTyg eig.
„kraftschwellend", HoXvcp6vzr\g = IIoXvYzijzrjg, KXeocfdvzrjg, vielleicht zpovog
aipazog II. 16, 162 wenn „Hasse“ (doch eher nach Niedermann IA. 29, 33
fur al/ua <povov „das Blut des getbteten Hirsches"), red.-stufig rpavav &e-
Xelv Hes., wohl eigentlich ,,geil sein". Lit. guild „genug“, aksl. goncti „ge-
niigen" (gegen Entlehnung aus got. ganah s. Solmsen Beitr. I 167 Anm. 2.
Berneker 327).
   Arm. yogn „multum" (Praep. i               +
                                         *o-g’ihon- oder *o-cfihno    im Praelix
o- dem ar. a- nachststehend, Liden Arm. St. 76 f.)
  Bezzenberger-Fick BB. 6. 337, Fick BB. 8, 330; 16. 289, Horn Kp. Et.
10, Grdr. d. iran. Phil. I 2, 62, 130, Johansson IF. 3, 241, Ehrlich KZ. 39, 561.
     Kaum hierher gr. agevog, azpvo; n. „reichlicher Yorrat, Reichtum",                                 dcp-
veiog „begiitert"          (z.   B. wieder Bechtel Lexil. 7Sf. nach Fick, wobei                    <p   und
der Yokalvorsclilag aus der vokallosen Form ( a)cpv hergeleitet wird; auch
             wurde erwogen; andere, doch auch nicht einleuchtende Deu-
*s//t -</“/« (e)w-

tungen bei Johansson IF. 3, 241, Liden Stud. 72, s. auch Yf. LEWb. u.
omnis ); n agfievog (Brugmann BSGW. 58, 172 ff.) fern bleibt o&svog „Kraft“
                                                                    ;


(Siebs KZ. 37, 281, Charpentier KZ. 40, 476). Lat. fenus (Froehde BB. 21,
326) trotz des an eir&yvyg erinnernden c wohl vielmehr zufc-lix fe-cundus                  ,                  ,


Wz. *dhei~. Mindestens ganz fraglich lat. pracgnas, pracgndns ,,schwanger,
triichtig, voll, strotzend" (Ehrlich KZ. 39, 561, BPhW. 1911, 1573, Brug-
mann IP’. 34, 400, der ein Adj. *prac-gn-os „liervorstrotzend“ voraussetzt,
woraus ein Yerbum *pmegnarl und als -ti- und -wANomen dazu -gnd{ti)s,
-   gnan(t)s     doch      s.   auch Yf. LEWb. 2   s. v.,       wonach vielleicht zu *gcn- „er-
zeugen", nutio, niittl).


2.    gShen- „schlagen“, auch als set -Basis g^hene-.
```


## [2026-09-06T15:07:03.817Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### FFD pdf 30 (p.25)\"; awk 'BEGIN{RS=\"\\f\"} NR==30{print}' incoming/FFD/FFD_pages.txt | head -30",
 "description": "FFD p.25"
}
```


### [2026-09-06T15:07:05.460Z] TOOL RESULT

```
### FFD pdf 30 (p.25)
[pdf page 30]
ماده‌های ماضی و مضارع فارسی دری - ا اس ۲۵
8 صورت بالانلرهٌ ريشهٌ 7210 است. ريشةٌ 730 «استراحت کردن» معنی می‌دهد. از
ريشهٌ 1318 «آرمیدن» و «رامیدن» هم آمده‌اند.
۱ آزاردن
آزارد + فارسی میانه 22374 < ایرانی باستان 3-227-12*. 8 پیشوند فعلی است >
آراست. 237 ريشه است به معنی «تحریک کردن» و 12 پسوند است. برای 12 > آراست.
آزار« فارسی میانه 2227 < ایرانی باستان 3-237-0*. برای 2 -> آرای.
«آرّرد»» که امروزه به ضم ز تلفظ می‌شودء» مخفف «آزار» است.
آزدن, آژدن
آزد « ایرانی باستان ۴2-70-18 برای 18 -> آراست. 2 پیشوند فعلی است. 8[ صورت
ضعیف ريشةٌ 8/180 است. 8/188 به معنی «ازدن» است. «آژد» از پهلوی اشکانی وارد
فارسی دری شده است.[ ایرانی باستان در پهلوی اشکانی #ودر فارسی میانه 7 شده
است.
آزن « ایرانی باستان 20[-3*. آژن < پهلوی اشکانی 0ه37* < ایرانی باستان 80[-3*.
آزمودن
آزمود < فارسی میانه ۰320084 02130. صورت اصلی 02804 است از پیشوند فعلی
2 که به فارسی میانه نرسیده و 134 . 8 به قیاس با 8739 8730 به جای 30 آمده
است. صورت ایرانی باستان این ماده 1 - ۳3 - 2* بوده است. ريشه (133)7 به معنی
«اندازه گرفتن» است. برای 1۵ آراست.
آزمای + فارسی میانه 2203 23 < ایرانی باستان 2-ر2-3*. برای 2-> آرای.
آسودن
آسود + فارسی میانه 3800.
آسای + فارسی میانه 3837.
```


## [2026-09-06T15:07:18.815Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### DKS varegna\"; grep -n \"vārəgna\\|vārəγna\\|varəgna\\|wārəγna\\|vārgan\\|Falcon\\|w'rγn\" ISS_alt_DKS.txt | head -8\necho \"### ARY زهر/زدن\"; grep -n \"زهر\\b\" incoming/ARY/ARY_pages.txt | head -5\necho \"### ARY latin\"; grep -n -i \"ZAHR\\|ZADAN\\|GAZIDAN\" incoming/ARY/ARY_latin_index_pages.txt | head -8",
 "description": "Bailey and Aryanpur"
}
```


### [2026-09-06T15:07:18.921Z] TOOL RESULT

```
### DKS varegna
### ARY زهر/زدن
228:آنها اخذ کردند و یا اینکه چون مارهای فلات ایران و هند مهلکه‌اند (و مارهای اروپای شمالی زهرین
4283:۸ | پاده پٌد (به چم "مخالف» *ضد* مثلاً در واژه‌ی *پادزهر*)
4318:یونانی (078870): 7 207 فرهنگ معین + ۷ (پادزهر) ۶۴۸
9815:"پادزهر"88102۸77) نیز از واژه‌ی فارسی "پادزهر گرفته شده است (5168۸7 :53-59)
12054:۳ واژه‌ی "کشت" با واژه‌های "زدن" و آزهر" همريشه است.
### ARY latin
9118:NASCOR, GIGNERE, (LATIN) gs ZADAN, ZAY- PAHLAVI) 5 sg,
9266:JHENTH, ZHENO ZADAN, ZATAN, (PAHLAVI) 65 |
9620:POKORNY, = SSs~*~*~*«OD ZAHR PAHLAVI) (53h
9623:OF THE ENGLISH LANGUAGE: ZAHR HBALUCHI) ge gh
9624:(GWHEN) 2031 ZAHR HAFGHAND) (4) ls!
9630:(58-59: SKEAT) cast ot och £" 24" go ofl 5 53 BADZAHR’ a 3h"
```


## [2026-09-06T15:07:22.416Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12045,12060p' incoming/ARY/ARY_pages.txt; echo \"---- ARY 9805-9830 latin\"; sed -n '9610,9640p' incoming/ARY/ARY_latin_index_pages.txt; echo \"--- pages ctx 9805\"; sed -n '9805,9825p' incoming/ARY/ARY_pages.txt",
 "description": "Aryanpur zahr entry"
}
```


### [2026-09-06T15:07:22.497Z] TOOL RESULT

```
[pdf page 405]
۶ / کشتن کاشتن
پسگشت‌ها گر در 0 (آنآل) شا
9 000 54 080 7
0 وق ۸/28 برهان قاطع : . ۹ ۱۶۴۸۹
امن
یادداشت:
۱ 80 اصل این واژه‌ی هند و ایرانی را "ناشناخته" می‌داند. (
۱ ۲ چم این واژه در زبان سانسکریت: کشیدن» دریدن
۳ واژه‌ی "کشت" با واژه‌های "زدن" و آزهر" همريشه است.
| لکیس سروازای فارش ‏ سا ما3 ۲0۷3338
ارستایی (۸7887۸07): اددید ۹ پرتغالی (008701895: ۲0137۷۸
۱ پهلری (۲7مابقده): ۸ انگلیسی (/۸)5۸70/57(از فراننه)
بلرچی (تقتتامقهه): ان انیا دبای ای
افغانی (پشتو) (4۳0۸71): :
باهش ملعم پسگشت‌ها کی
---- ARY 9805-9830 latin
REFERENCES : nthe ZHI KURDISH) «53,5
POKORNY, = SSS*S~«SBSCS JicH NBALUCHD) ge Sy
DELAMARRE: ZHAL AFGHAND (52%) glist
(CORDE D’ARC) 115 SYA (SANSKRIT) Sy Soils
(MACKENZIE: (BOW-STRING) 105 BIOs GREEK) gli
MALLORY & ADAMS: GW (DIEH- (OLD CHURCH SLAVIC) 455 set
vere sbi day ZHICA
setlaal
STK eel Sy popu oy go! 54 >
REFERENCES boy JATHRA — (OLD PERSIAN) Skul,
POKORNY, = SSs~*~*~*«OD ZAHR PAHLAVI) (53h
MACKENZIE: (POISON) 127 KURDISH) 53,5
THE AMERICAN HERITAGE DICTIONARY JEHR, ZHAHR, ZHAHR, ZHAIR
OF THE ENGLISH LANGUAGE: ZAHR HBALUCHI) ge gh
(GWHEN) 2031 ZAHR HAFGHAND) (4) ls!
AMINDAROY: (POISON) 269 ‘ZHAHR, ZHAHUR (ARMENIAN) ¢s,!
1eVF seb sky ZATRUC (4U(POLISH) slug)
lethal
ae BEZAR 3 p\lu! BEZOAR +3 4 BEZDARD :.i13) BEZOAR 18:1 5051)
[pdf page 332]
(58-59: SKEAT) cast ot och £" 24" go ofl 5 53 BADZAHR’ a 3h"
[em a 9 8
BIAO (GREEK) gi ZYANA, ZYANI-—:(AVESTAN) (pln)
ZIYAN, ZYAN PAHLAVI) 5 ay
‘REFERENCES eer ZIAN, ZHIAN OSSETIC) gi \
POKORNY. SSOS~*~S~S~«SD ZIYAN KURDISH) «53,
MACKENZIE: ZIYANI HBALUCHI) gz gh
(DAMAGE) 109, (LOSS) 122 ZIYAN HAPGHAND) (4) ih
BUCK: 160-762 (SANSKRIT) cy Sui
AMINDAROV: (DAMAGE) 208 JAYATI, SYANA, JYA-
Vode igbG ob, ZEAN ARMENIAN) |
--- pages ctx 9805

بلو چی (71لع( ال 8۸): 72۸78 :0 ما تذل اماط 778 0۶
افغانی (پشتو) (/70/۸۸): 72۸1 1 (0۷553)
ار نی ((/(8(/5): 2۸71۳ ,2۸37۴ 9 (80150) 0
لهستانی (5/-۳0)(شاید) شا ۷ 2 برهان قاطع + ۱.۷۴

یادداشت,

واژه‌ی انگلیسی 81520۸4 (فرانسه: (81220۸147) پرتغالی:؛ چ8152.0۸؛ اسپانیایی: ۹1224۸18 عربی
[pdf page 332]
"پادزهر"88102۸77) نیز از واژه‌ی فارسی "پادزهر گرفته شده است (5168۸7 :53-59)
اوستایی (ر۸۲2۹: -20۸0۷1 بقلل2 2۷ یونانی (06526): 311۸0
پهلری (1۸7ل(۳۸): ۸۷ ,و71۷۸
اوستی (05355776): 7 ,ما2 پسگشت‌ها 5
کردی ([00-7015: 72۸0 را 1 نا
بلوچی (للتامله8): ال ۱ :۸/۸۲2/215
افغانی (پشتو) (//4۳0۸): 2۸ 2 (1059) ,109 (0۸31۸65)
سانسکر بت (854(/570/7)+ 70742 8
۰ مشاله ال ,1۸۷۸7 8 (0۸/۸05) ۸۸4/۷۵۸۵۰
ارمنی (۸8۸18(42): 72۸ برهان قاطع ۱.۵۰
| چم‌انگلیس سرواژای نار ۱۳۳۴۹
```


## [2026-09-06T15:07:35.648Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### BRT Harz\"; grep -n \"Harz\" BRT.txt | head -5\necho \"### BQT v4 ورغنه\"; grep -n \"ورغنه\\|ورغن\" incoming/BQT/BQT_v4_pages.txt | head -5\necho \"### v3 ورغنه\"; grep -n \"ورغنه\" incoming/BQT/BQT_v3_pages.txt | head -3\necho \"### MON adena varghaneh\"; grep -n \"ورغنه\" incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -3",
 "description": "Look for varghaneh and Avestan resin"
}
```


### [2026-09-06T15:07:35.757Z] TOOL RESULT

```
### BRT Harz
21517:(auf  welchem,    näml.  Berg)  das  Han  -  oder der  Asphalt  -  (wächst)'.  —  VgL  «L  jälaii-  n. 'Gammi',    np.  iad  'Gummi',   angu-iad  'Harz', —  ■)  So,  ohne  Trennung,  alle  guten  Hds, j.  "yakva  Yt.  10.   2S:  s.  ya-,  Sp.   1304  O.
### BQT v4 ورغنه
### v3 ورغنه
### MON adena varghaneh
```


## [2026-09-06T15:07:40.617Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21495,21525p' BRT.txt",
 "description": "Bartholomae resin entry context"
}
```


### [2026-09-06T15:07:40.666Z] TOOL RESULT

```
-S.)  Yt  1$.  56.')        IS.  ytM  als  In£  sbes. Zum  V.  yai:  —  ai.  Tgl.  v/ay-  f.  —    i)  Gant unsichere  Stelle;  vgl,  liar-  mit  No.  10. j.  yaätar-  m.  'Anbeter':  staota.  , .  -tä amfianqm    spmtanqm    Y.  J2.  i ;    —    vuai V! . .  zbatä  'ta  fra'martta  Y. z^. i,  Vr. 5. 1 (wo  'ta);  —  'tars^a  äfrjtanca  Yt  J.  1. Zum  V.  yat:    —   ai.  yäilar-,  yofldr-  m.,   mp, yahär.  -  Pü.  (in  Y.  13):  yaümi  (lu  Y.  14): fata-fm  . .  /ayatunTA,
•  j.  yasaSwa-  (,  *yasdhwa-)  Adj.  'vene- randus'j  vTspanqmca  .  .^avaslm  .  .yas'am
''^waca'^  urvans  zaoyäs^a  JravasayS  Yt 13'  148.
KompE.  — PFP.iumV.^'a»-;  statt  «j-n/Au^  unter
Uiflitized  by  VjOOQ  IC
yata
383
dem  Einlluss  der  I'FP.  mit  regelrechtem  ^wa- {S  30p-  13).  Ähnlich  yai^  Äri-ä  (— '  a,\.  yäs tvä)  statt  *yas  ttj.  —  ')  Hda.  ■in/o/Za.
•  j.  yah-  V.  'sieden'  (intrans.).  Praes.  6 jraesa-'\  2^  jyagsya-.  —  FP[P.  yaäa-i?)».
'sieden,  sich  in  Siedehitze  befinden': yaihnia  (3?.)^'  fatmta  "(die  Wasser) siedeten,  flössen  über"  F.  4f-;  —  ffqs (sd.)  ayanhsjrasparat  yais'yantim  äptm *paraiihät  "..dassiedendeWasser schüttete er  um"  Y.p.ii;  —  *ya!s?ntim*'  äp>m F-^f.;  —  niioyäti  (sd.)  il . ,  ätari . .  kala yastibys  (DPf.)"  aiwyiJ  ".  .  vor  den siedenden"  Wassern"  P.  2/.
a\.ydsyaH,  yf^ati;  yas/äi;  np. jasian  (?,  GlrPh. /b.  139),  PDw.  yaiin  {?,  GlrPh.  /  b.  Z98).  — PQ.!  »da«  ßaa,  •eitUait,  Sä.  {lu  Y.p):  mala- vatT  'schmutzig'  (,  weil  man  hixr°  Im)*}.  — ')  Nicht  ganz  sicher,  da  'l>ni°  fiir  'siitf  ge- schrieben sein  kann;  s.  hindav-  No.  I.  — ">  /  müEste  vom  redupl.  Praeseos  stammen. Statt  yaihliiyS  im  Text  schreibt  DST,  in  der Note  yokiH'.  VII.  ist  beide»  falsch.  Ob yaihnübyöt  —  J)  Vgl,  No.  i.  —  4)  M  hat aestnüm,  K  yaisinlim;  s.  noch  No.  I.  — S)  Und  deshalb  überwallenden.  —  «)  Vgl.  Dst. ZA,  3.  II.  Jamaspji  Gloss,  475-  476  bat aySrRjn^d  'surpasses', j.  yahi  Yt.  10.  64:  lies  yalimi;  5.  ya-  mit No.  17.
•  j.  yahmat  haca  adv.-artige  Verb,  'wes- halb, quam  ob  rem',  an  den  Inhalt  des vorausgehenden  Satzes  anknüpfend:  avt tfÄBm  . .  *x»mS  jauhsntu  y  h°  staxrS , .  xyä . .  y  h'  .  .  snaoilf  (sd.)  vafra  snaHäi  V. 2,2a;  — pairi  ig  hs  *pant5Janunqm  iti- Aaiti  y  h'  tsm  ava.rae%>nti  (sd.)  N.  42.
AblSn.  aus  ja-.—  Pü.:  k!  hac  an,  ka  kal in,
•  j.  yahmäi  Konjn.  'bis  (dahin)  dass'; es  folgt  Konj. :  janäni  dqma  dagvS.dät»m .  .  y"  *ussayäiti  sac^qs  V.ip,^.
DSn,  aus  ya-.  —  Pii.!  läk  ka.
•  j.  yahmya  Adv.  'wo,  ubi' :  yai  bä  paiti fraishm  daxma  (NPm.)  uzdaSza  (sd.)  kir- yeinie  y  narS  irtsta  moayeinteV.3.');i2, 7.  54i  —  tl  narB  xsd^ra  (APn.)  xsqymte ,,  y  stariiatca  gätus  .  .  Yt/7.  7;  — arpdvJm  (ASf.)  , ,  y  ('ubi'  statt  'in  qua') ahurS  masdh  ..  niva^ayal  Yt.5.  85.
KompA.  —  I^n,  aus^i-,  —  Pü. ;  ku  andat  an,
•  j.  vispaca  däma  .  .  a/aoni  alavabyS . yahmyEiSi''  aiavabys  ^.-^i.b:  -?-,
Pü, :  harvispca  däm  .  .  Si  i  akrav  kl  andar ahrtcuän  fa  ahrSkih  älnäi.  —  ')  VII.  alte  Ver- derbnis aas  yisnyäla  vahmyäla-
•  j   *yahmya-Jatara- ''  m,  Name  eines
Bergs  oder  Gebirgs:  ahmal  haca  garayS fraoxiyqn  . .  °rasla  Yt  ig.  6,
Komp.*   mit  LS.   im    1.  Glied.    Eig,  vU.  'wo
(auf  welchem,    näml.  Berg)  das  Han  -  oder der  Asphalt  -  (wächst)'.  —  VgL  «L  jälaii-  n. 'Gammi',    np.  iad  'Gummi',   angu-iad  'Harz', —  ■)  So,  ohne  Trennung,  alle  guten  Hds, j.  "yakva  Yt.  10.   2S:  s.  ya-,  Sp.   1304  O.
•  j.  'yä-  V.  'gehen';  nur  mit  Praev.   Praes.
1  yä:
mit  apa  i )  "weggehen  von  — '  (Abi,) :  apa aiat  frabirita  altäibyS  xaoi^rabyS  yäiti (Konj.)  yanhqm  .  .  N.  ?/(?).  2)    'ent-
gehen', mit  Abi.;  kaomsm  yim  nivUatH riivandäi  {sd.)  apayeiti  Yt.  1^,57,
mit  upa  'herzugehen,  -kommen':  3a/  tat dunmqn  fi-asäupayäü  (d.  '\.fi-ala  -(-  upay")  ■' marye^ara  "und  dann  kommen  die  wolken- bildenden Nebel  herangezogen"  YL1S33, Vgl. '<?>'-;  die  Formen  der  beiden  Basen  sind nicht  immer  sicher  lu  scheiden.    S.  auch  zn frayäi.  —    ai.  yäli  'er  geht".    —   Pii.  (lu  N.): ap^  ^tatoil.  —  ')  S  J04  IT-  31.  ^*-  33-
•  j.  *yä-  Adj.  (auch  fem.)  'gehend'. KorapE.  —  ai.  'ya-  Adj.  —  VgL  za  frayäi.
•  g.  *yäat''  Adv.  'seit  (dem  dass  — )';  es folgt  Perf.;  y  yusta  framXmaha  (sd.)  ya marya . ,  vaxs?nU  daevSsuUa  (sd.)  Y.  J2.  4.
AblSn.  (nominaler  Bildung)  aus  ya- ;  eig,  'ex qno'.  —  aL  yaf  Konjn.  'seit'.  —  PB.:  :*i"  haf an.  —  O  So  richtig  Mf  1  usw.;  s.  auch  Pt4. Vgl.  äal  No.  6.
```


## [2026-09-06T15:07:57.920Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ja%ra\\|ja&ra\\|jaüra\\|ja^ra\\|paiti.ja\\|Gegengift\\|'Gift'\" BRT.txt | head -12",
 "description": "Bartholomae jathra"
}
```


### [2026-09-06T15:07:57.973Z] TOOL RESULT

```
2790:Kaus.  '(Truppen,  einen  Truppenführer)  U  .  .  *dqnmahi  'sa  zao^ra  paiti.jam- entsenden,  marschiren  lassen':  pasäviJ'  yät  tava  .  .  Y.C^.i;  —  '/a  dacna  N.  j; adam     käram    /raisayam     Bh.  2.  6;    14,  ,*j'(?).  2)    substantivisch:     °/ü    aibi.-
4117:•  j.  aBr5.mainyav-  Adj,  'dem  bösen Geist  entstammt,  zur  Schöpfung  des  bösen Geists  gehörig' :  iaAe  vaca  vanai  . .  kana zaya  mana  dqma  'yus  (IP,  als  APn.) ''  V. /»).8;  —  -ffl/  tat  dqma  spmfs.matnyava ailauhqm  dämanam  .  .  Aazatpraja  "yus (nämb  dama;  IP.  als  APn.)''  paiti.jasaiti V.13.1.  '
5737:•  j.  asah-  n.  'Ort,  Stätte,  Platz,  Raum': y8  anyeAe  *'saAya  (LS.)  bansma  */ra- stff^ie^.ioi; — äaire  "saAi  razaaiam(sd.) V.Ä97;  —  atfffi  daoam  °s/f  rämsMäitTm (sd.)  ndil  kuäalJäiim'V.i.i;  iPUZ.,  Vyt. 2'j(?);  —  xrüma  'sl6rs{3is  Subj.)  frasinia danunam  YL  13.  ^S;  —yatca  aakat  %wyqs- brnalrva  'sauham  V.2.23;  —  yäi^a  °sS mai^animca  atmisilSe  äaiära  (sd.)  Yt.  13. 67.  a)  sonst  neben  sSihra-.  paoirlm •sanham^a  Sstiranamca  vakishm  frii' "iwtnspm  .  .  airyatDtn  vaSjB  "als  die  erst- beste der  Stätten  undWohnplätze.."  V.  I.a; Y.  /.  lÖ;  —  hpnti  atiyäscii  °s3sca  sSi^rSsca irirasla..  V.J.  20;  Y.  3.16,  S.  7.28,  2.28; —  äat . .  vazaite  väiS . .  avi  'sä  avi  /gi'irS ai-i  karh'ä  yäis  hapta  Yt  Ä  3  3 ;  —  para  nU ahntät  h<üa  'sarihal^a  ^t^räatca  axslat .,  iia/a  äzätliscaY.g.^y,  —  Adoa..  aktnai •saaAalia  sUrbraläi  paiti.jasata  iii V.  ß.  5  4 ;  55,  57;  —  tä  yai'.yeinti  p>sanahu kavc  'tahi  säi^rafai  Yt.  IJ.  27.
7024:ff(rai>/(Stverz.)  «^«röMasi/J  V.2, 1  f.,  usw.;'eines  koordiniiten  Satzes  an  das  Voraus- Y.p.z.s,  16,  7J.2,  V.j&ai,  H.  2.ii,Nik.  2, 1  gehende 'und';  die  zeitliche  Folge  tritt  min- yyt.8,22;  —  ä3tar3..kd  avalia..vl.l>arat..}'  dest  sehr  zurück;  a)  eines  Hauptsatzes:  tarn a°  aoxta  ahurö  mazdä  V.  2.42;  40,  Yt  5.  ^yatata  haofyauA^  .  ,  ä'  Alm  jaloyal  Yt. 9°>  95!  —  ahmäi  fradaisaSm  dainqm  .  .  ij.2^{.;  5.18,  5.17,  /j.40;  —  vagiipmnsm ä°  hl  mraont  .  .  visanha  mg  yima  .  .  ä'\  *apa  karsayjn  Jainis  .  .  ä°  tä  .  .  hazö ml  alm  paityaoxta  yimS  .  ,  ä"  h!  mraom  '  nivamay?n  (sd.)  Yt.  /5.80;  —  J  tat  han- .  .  ä'  mE  aem  paityaoxta  .  .  ä"  kl  saya  [jamarum  paiti.jasat .  .  ahurö  mazdä  .  .  ä° "       ■    "    "  ahurff  riazdfv.  2.21  f.;—  ,iat{s.  8}
9029:?:t.?0.  —  Pü.:  fehlt;  Kyo.:  kF«ü.  ei\.:  n.i kiMii  li.iti  ,/,ijl  kitnad.  —  ')  Man  setit  wegen np.  kiihijsl  'Koloquinle'  die  Bedeutung  'Gift' oder  'plante  vüni'neuse'  an,  was  mir  nicht  lu passen  scheint.  Eber  ka-/<a'Uiy-  (s.  unter t,-nu,A„-y,  vgl.  lat.  A^/«.
9916:mitpai/i  'Jmdn.  (Akk.)  um  etwas  (Akk.) befragen':  bae\asca  urvän^m^a  yät?m(sA.) ga^'hanqm  paiti.jaihycinti  V.  ig,  29.
9981:nSmSni  aeSam  drujinqm  .  .  paiti.janaiti*'' Yt.4. 7.  3)  Med.  a)  II  'sich  wehren gegen  --,  bekämpfen',  mit  Akk.:  pärst^ martiy^  ^duraiyapiy  kacä  pitrsil^  hama- ram  (sd.)  patiyajatä  (3SPrM.)"  D.  ti. 4.  b)  'sich  wehren  um  — ,  kämpfen um  — ',  mit  kala  und  Abt.:  ya'ia  nä taxmö  . .  kus.kqm.bfr?tal  kam  laität  (sd.) . .  paiti.ynita  (3SOM.)  Yt.  13. 67.
10036:mit  ii  und  J>aili  'hinzukommen  zu  — ' (AkL):  n  tat  hanjamamm  paiti.jasat  yö . . akurs  V.2.  ai;  zi  (wo  -jasat  als  Praet).
10044:Tmtpaiti  i)  'entgegengehen,  sich  wen- den gegen  — ';  a)  mit  Akk.:  vTsp»m  paiti usanhim  ..hazaaraja  (.y&ssA.dqma)  *ar?rö.~ mainyus{W.)  paiti.Jasaiti  V./ j.i.  b)mit Dat.;  miitvm  .  .  yet^he  hazar»nm  vaFja- nqm  paiti  katmrg'^äi  jasaiti  Yt  W.  69 ;  —  s. noch  Inf.  c)  absolut  'dagegen  angehen, als  Ausgleich  (einer  Schuld)  dienen':  aiia zaokra  palti.jamyat  Y.6S.1.  2)  'zurück- kommen, -kehren  zu  — '  (Dat):  iala  nS abmai  asanbalca  .  .  paiti.jasatö  (3DK.) isaca  ozuitiica  V.^.  54;  55,  57.  a)  ab-
10049:wenden,  begeben  zu  — ';  a)  mit  Akk.: yezua  äpS  vaauAls  hansnüm  vayoanifm pourum  paitiJasaitiY.S.^i;  —  nqmistahyä mmatikä  iiS  mazi^täi  yär>Aqm  failljamyä Y.36.2  (zit  Y.5d'.7);  a;  —  asaya  tie*paill.- Jamylt  Y.  7.  24;  —  käu  .,*nx'iB.vaht9hqm uxoB.vaiashmö  paiü.jasat  *dritümla  dri- vtmla  T.26;  2.V»  b)'niit  Dat.:  xM- aaScii  azütaya^ca  mSvayaca  zaoire  paiti.- jamyä  Y.flS.a;  —  akmät  iaAmSiät  {&d.) naimanqm  .  .  paiti.jasaiti  ütarf  V.  8. 80,  c)  mit  Akk,  und  Dat;  taota{sA) *syaoi/iSJäitya  *häva7taHbya  faitt.ja»- hsit''i>  *iavaiian3  gatüm  ".  .  soll  sich zum  Mörser  begeben  auf  den  Platz  . ." N.A'/.
10300:hvialia  V.O.33,  /tf.8;  —  hiku  pqsitu  (sd.) °tu  (IS.)  tihayaaa  Y.16.2;  —  nsit  Alm  'tvd (GS.)  vindm  pasvasca  . .  "es  fanden  nicht mehr  Platz  .."  V.2.8;  9.  a)  mit  misvan- Adj,  (sd.,  auch  fdSt.):  misvärum  'tarn  S. 2.^0;  — misvänahe  'tvaie(GS.)^>  S./.30; usw.  2)  sva.  'festbestimmter,  vorge- schriebener, richtiger  Ort  (usw.)';  iva aHahe  nars  'tu^  anhat  ya£  irisis.kasahe ^■,?-^5i  —  y^S  "^'''^  zaota  (sd.)  /r3ya- zititi ..zaotars  "lai-a^  (IS.) .. syae^nöJätfya .  .  paiti.jatfkdit  hävanänö  -taiii'  .  .  N.  Si;
13101:paiti.jasätB  ii3ca  Ozüitisca  ..yat..  aäaahs °iA^/..'V.g.$${.; — räma  i^ästr?m  *aöhä 'i^hsul  afrlnami  V.6S.i$;  —  at  tsi  at?h^i saofyantS  (sd.)  'Jiptnam  \.  i0.  12;  70.4, Vr./J.i3;  — ä^ravanS  'hyunqm  Yt/J.147; — ySi  *iyefqm  .  .  alB.lsS  (sd.)  'hyunqm  Y. 42.(>\  —  mihfpm  ..  vJspanqm  'hyunqm daitihufaitim  Yt  70.145,  ^P-3S)  Y,  2. 11; J.  1 1 ;  —  fravasayS  .  .  vJspä  vtspanqm 'hyunqm  Vty.  ai;  21,  5.  22,  98; — bäna joff  ä/rasane  -ahuiyU  V.^.  27;  —  ^^agpai'ie nö  'iähuif  nibätal^a(Sp.j2i  o.)  haosiitalca YtJj.66;  68;  —  tis/rim  . .  yhn  . ,  *kisp5.- smti  huyairyUta  "i'ähavt  uzjaimt^m  äui- yairyäea  Yt.  Ä  36;  V.  4.2;  —  huyairyJ avi  'iähu/\LS.g;  —  usia  a.bav,it  'iii/iavö (P.)  US  vB  apqm  alavS  .  .  jasanti  Yt Ä  29;  —  ilbyd  'iiihubyö  snislB  ydi,a alm  (näml.  iistryö)  bavaitt  yallB  Yt  8. 47 ; '^■34j  —  m»rm(aite  vtspqm  'iühaom mairyS  mPbrB.änixs  Yt,  10.2;  —  tBm  akB vahistasla  mii:ra  ahi  'irihubyB  Yt. /o,  29J
```


## [2026-09-06T15:08:16.426Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -rn \"ورغ\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null | head -5\necho \"--- v3 page 462 raw again for varghaneh\"; awk 'BEGIN{RS=\"\\f\"} NR==461{print}' incoming/BQT/BQT_v3_pages.txt | grep -n \"ورغ\\|کلاغ\" | head",
 "description": "Search for varghaneh in Borhan"
}
```


### [2026-09-06T15:08:18.398Z] TOOL RESULT

```
incoming/BQT/BQT_v4_pages.txt:2835:بله کرد ازآن سوکه بود آب و مرغ پیت از بر دامن ربگه ورغ .
incoming/BQT/BQT_v4_pages.txt:9097:برآورده وخابيدة شتران وامثال آن باشد ۴ . ماشد نمد کرم خورده وآ ترا بعربی‌هرشفه ورغوة
incoming/BQT/BQT_v4_pages.txt:13267:۷ «ورغ (.م.) * برغ («م.) ۸ -ر4 : رشیدی , در موْبدالفضلا وازع بزاء
incoming/BQT/BQT_v4_pages.txt:13968:نامه ۷۸۲ *. 8 رك : ورارود . ۹ ورغ (وم.)
incoming/BQT/BQT_v4_pages.txt:14409:ورغست ؟ - باغین نقطهدار بر وزن | و معشوق باشد.
--- v3 page 462 raw again for varghaneh
13:وسفید ‎KET SEW pie il‏ و کلاغ ‎cary‏
32:که لوچوکاج واحول ۷ - وکلاغ یسه باشد که
47:‏کیذکی ۵186 (کلاغ) « فارس یکلاغ . قلاغ , کلاژاره . قلازاره .
```


## [2026-09-06T15:09:18.293Z] TOOL CALL #101: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg215.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/215.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-06T15:09:18.370Z] TOOL RESULT

```
total 8476
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 11:09 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-06T15:09:41.364Z] TOOL CALL #102: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==545{print}' BQT_v1_pages.txt | tail -22",
 "description": "BQT vol1 p.324 Bahram footnote"
}
```


### [2026-09-06T15:09:44.601Z] TOOL RESULT

```
- -انسکریت 0180754 «اسفا ۱ : ۲ ص۲۳» همرشةٌ 03۲2 (سهم . حصه)» ورپارسی باستان
۵ اوستا 02۷۵00۳2 «اسفا ۱ :۲ س ۸۱> : بهلوی ۲ط08 . 0891 «امفا ۱ : ۲
س ٩۵‏ ازرشة طوعو «ثی رگد 6۹ * منای ۲5۹۹ » ۶ بارتولمد۹۲۳ . ۳ در اوستا
۷۵/۵۵/2۵ ۰ پهلری ۷۵۲۳۵۵ , ۷2۳۵۲۵۲ ۰ ۷۵۵۲۵۵ آمده < تب رکه ۲۳۳ >
بمحنی پیروز هند . اصلا مر کب است ار دو جزو : ۷۵۲۵013۳2 اوستابی و ۷۴۱0۶۵ ساسکریت
بمنی اادهایی که بادان دا محبوی میدادد و آرباییان آنرا بز رکترین دشمن خود محصوب
حیداشتند , جزو دوم 81087 اوستابی و 288 ساسکربت از حصمر 88[ ابرانی باستان و 2
اوستا , بهء‌عنی زدن و کشئن . ورثرغنه اوستا و ۷۲۸/۲22810 ساسکرت لفة بمعنی ورنرا کش ۰
فانل دشمن. این نام بزرکترین و محترم نرین لقبی است که بخدابانی که بورنره حمله میکردند
متوضا 8 (رب‌النوع رعد) داده میشد. «مزدبسنا ص ۳۵*- همین عفپوم دردین قدیم آرمنی
بنام ۷2188315 ( خدای اژوها کش ) آمده است . نیز در ارمنی ۷۵1810 و مردم گرجستان
0 کومند. ریییکی از ایزوان‌بساریز که مزدبسناست ودرهمام همیاية سروش است_درمهربشت
آمده که بهرام بار و همراء مهر ( فرشتة رزم ) و پاسبان عهد
و پیبان است - پشت چهلردهم اوشا بنام«بهرام بشت * است.
آش ورهرام ( بهرام ) که بجای 6824۳607916 عسوبانت "
راب مخصوص باایزد پیروزی» بهرام دارد - نگهبانی روز بیستم
هرهاه شمسی بدین فرشته سیرده شده و دد ادببات‌ها بهرام گاه
اسم ایزد پیروزی . گاه روز بیسم ماه , کاه ستار هریخ » گاه
اسم کیاء ( منسوب ببهرام ) و گاه نلم یکی از ناهن بثلم
ای رو ی کور آهده . « روژ شماری 4۸ -
- بهرام نام پنج پادشاه ساسانی است: بیرام. اول ( ۷۷۳
ید گرد اول.. ۴ -ره؛ ۶ تربتنن. ساسان. ص۳ یمد ۰0۰۵۸4۷۱ ۲ بعد.
```


## [2026-09-06T15:10:11.579Z] AGENT

Now I'll write the verification file.


## [2026-09-06T15:19:52.703Z] TOOL CALL #103: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/gen215.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE = W + \"Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-\"\nZAHR = W + \"%D8%B2%D9%87%D8%B1\"\nZADAN = W + \"%D8%B2%D8%AF%D9%86\"\nGAZIDAN = W + \"%DA%AF%D8%B2%DB%8C%D8%AF%D9%86\"\nBAHRAM = W + \"%D8%A8%D9%87%D8%B1%D8%A7%D9%85\"\nKALAGH = W + \"%DA%A9%D9%84%D8%A7%D8%BA\"\nE = \"https://www.etymonline.com/word/\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"žata 2, jan, gan 2, gaz,gaš; â-ža-ta 2; vî-jainti; varathra-ğam\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Four of the six items are correct and standard. (a) Av. jan- / gan- 'to strike, slay' is the regular Iranian continuation of PIE *gʷhen-: Bartholomae files the verb under the headword 'gan-' with the present stem jan- (AiW col. 490 f.), the palatalisation *gʷh > ǰ before a front vowel giving jainti 'he strikes' beside the g-forms of the perfect and of nominal derivatives (jaγnvå, -γna-). (b) The past participle jata- (= Skt. hatá-, Gk. -φατος) is Pokorny's own example on p. 492; Nourai's 'žata' with ž- is not the Avestan shape but the Parthian/Middle-Iranian reflex (*ǰata- > Parth. žad), and he uses it because he needs it for NP āžadan in the daughter node. (c) â-ža-ta = Old Iranian *ā-ǰata-, the prefixed participle behind NP āzdan/āždan; Abolghasemi (FFD p. 25) sets up exactly *ā-ǰa-ta- with ǰa the weak grade of the root ǰan. (d) vî-jainti = Av. *vi-jainti- 'striking apart, injuring', Horn's reconstruction (Grundriss no. 916) behind NP gazand. (e) varathra-ğam is a misprint: the word is Av. vərəθra-γna- / vərəθra-jan- 'smiting resistance' (Yt 14), the second element being the very root of this chart; Borhan-e Qāte' p. 324 spells the components 'vərəθra + γna' and the printed page here clearly reads -ğam with a final m. (f) 'gaz, gaš' do NOT belong here and are not Avestan at all: there is no Avestan gaz-. Cheung (Etymological Dictionary of the Iranian Verb, s.v. *gaz, pp. 117-118) sets up *gaz 'to bite, sting' from Middle Persian gaz- and Parthian gst onwards only, states flatly 'The root is exclusively Iranian', leaves the PIE/LIV/Pokorny slots empty, and rejects both Bailey's and Korn's attempts to give it an IE source.\",\n \"derivation_fa\": \"چهار صورت از شش صورتِ این گره درست است. ریشهٔ اوستایی gan-/jan- «زدن، کشتن» بازماندهٔ قانونمند *gʷhen- هندواروپایی است؛ بارتولمه (فرهنگ ایرانی باستان، ستون ۴۹۰) مدخل را «gan-» گذاشته و ستاک حال را jan- آورده، زیرا واک لبی‌کامی *gʷh پیش از واکهٔ پیشین در ایرانی به ǰ بدل شده است. صفت مفعولی jata- (هم‌ریشه با hatá- سنسکریت) را خودِ پوکورنی در صفحهٔ ۴۹۲ آورده؛ صورت «žata» که نورایی نوشته اوستایی نیست بلکه بازتاب پهلوی اشکانی (žad) است و او آن را برای رسیدن به «آژدن» فارسی به کار برده. â-ža-ta همان *ā-ǰata- ایرانی باستان است که ابوالقاسمی در «فعل‌های فارسی دری» ص۲۵ عیناً بازسازی کرده. vî-jainti بازسازی هرن (بند ۹۱۶) برای «گزند» است. اما «varathra-ğam» غلط چاپی است: صورت درست vərəθra-γna «ورثره‌کُش» است و حاشیهٔ معین بر برهان قاطع (ص۳۲۴) نیز جزء دوم را γna می‌نویسد. سرانجام «gaz, gaš» اصلاً اوستایی نیست: چونگ (ذیل *gaz، ص۱۱۷–۱۱۸) این ریشه را «منحصراً ایرانی» می‌داند، خانهٔ هندواروپایی و پوکورنیِ آن را خالی می‌گذارد و کوشش‌های بیلی و کورن برای دادن ریشهٔ هندواروپایی به آن را رد می‌کند. پس ادعای نورایی در این گره جز دربارهٔ gaz/gaš درست است.\",\n \"error_in\": \"book\",\n \"book_prints\": \"varathra-ğam\",\n \"correct_form\": \"varathra-ğna (Av. vərəθraγna-)\",\n \"sources\": [PIE, BAHRAM],\n \"ref_check\": [\n  {\"ref\": \"POK:492\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 149 (printed p. 492), under '2. gʷhen-(ə)- ,schlagen'': 'av. jain-ti (= ai. hánti-) ,er schlägt, trifft, tötet', Imp. jaiδi … Partiz. jata- (= ai. hatá-) … av. jana- ,schlagend', jantar- ,der schlägt, tötet' … Vərəθrajan- ,den Widerstand niederschlagend' = ai. Vrtra-hán-'. Nothing about gaz/gaš.\"},\n  {\"ref\": \"HRN:204\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 226 (printed p. 204), no. 916: 'gezend, guzend (AM. S. 38 Zeile 7) ,Schade Leid' … aw. *vi-jainti-, vergl. ai. vi + han-, vihanti-; phlv. agajand bezw. agazand'. This is exactly Nourai's vî-jainti.\"},\n  {\"ref\": \"BQT:324\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 545 (printed p. 324), Mo'in's footnote to بهرام: «در اوستا Vərəθraγna … اصلاً مرکب است از دو جزو: vərəθra اوستایی و vṛtra سانسکریت … جزو دوم γna اوستایی و ghna سانسکریت از مصدر jan ایرانی باستان و gan اوستا، به معنی زدن و کشتن». Confirms the arrow and shows the printed '-ğam' is an error for -ğna.\"},\n  {\"ref\": \"FFD:25\", \"status\": \"supports\", \"note\": \"FFD_pages.txt pdf 30 (printed p. 25), s.v. «آزدن، آژدن»: «آزد < ایرانی باستان *ā-ǰa-ta … ǰa صورت ضعیف ریشهٔ ǰan است. ǰan به معنی زدن است». Nourai's â-ža-ta 2 verbatim.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"AiW col. 490-491 s.v. gan- (BRT.txt lines 9925-9975)\", \"stance\": \"supports\", \"note\": \"'j., g., p. gan- V. ,schlagen'. Praes. 1 jan- … PPfP. jata-, PFP. jaθwa- … 1) ,schlagen, treffen, verletzen; erschlagen, töten''; the article cites the Old Persian Behistun forms ajanam, avajanam under the same root.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *jan pp. 224-225 and s.v. *gaz pp. 117-118\", \"stance\": \"partial\", \"note\": \"*jan 'to kill, slay, strike' — 'AVESTAN: jan- (γn-) … (+ *aua-) … (+ *ni-) …', 'This root has impeccable IE credentials. PIE *gʷhen- > LIV: 218 f. | Pok.: 491 ff.' But *gaz 'to bite, sting': 'The root is exclusively Iranian … PIE LIV: — | Pok.: —'. So the jan-material is confirmed and the gaz-material contradicted.\"},\n  {\"src\": \"POK\", \"where\": \"IEW 492\", \"stance\": \"supports\", \"note\": \"See ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"zadan «زدن»; âzdan «آزدن»; gazîdan «گزیدن ٢ ( گزیدن ، گشتن ٢ ، گزند )»; Bahrâm «بهرام»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"زدن zadan is textbook: OIran. *ǰan- > MP zadan / zan- (Book Pahlavi MHYTWN-tn', Manichaean zdn, zn-), NP zadan; Iranian ǰ- regularly becomes z- in South-Western (Persian) territory, while the North-Western dialects keep ž-/j- (Parth. jan-, Bal. jan-). Mo'in's footnote in Borhan (p. 1007) gives the whole ladder — پهلوی zatan/zadan, اوستایی jan/gan, پارسی باستان jan-, هندی باستان han — citing Bartholomae col. 490. آزدن/آژدن âzdan 'to prick, to quilt, to stud' is *ā-ǰata- (node 1): Abolghasemi shows both spellings arise from one form by two routes, آژد through Parthian (*ǰ > ž) and آزد through Middle Persian (*ǰ > z); Noushin (Vazhe-namak p. 26) glosses آژدن 'خلانیدن و خلیدن' with the very Ferdowsi couplet Nourai prints. بهرام Bahrām is Av. Vərəθraγna- 'smiting of resistance' > Parth. Wahrām / MP Wahrām > NP Bahrām, a straight continuation of the root, so 'demon killer' is a loose but defensible gloss of 'slayer of Vərəθra/the obstruction'. گزند gazand is also right, but for a reason the chart obscures: Cheung derives NP gazand from *ui-jan (i.e. node 11's vi-jan), and Mo'in's footnote on Borhan p. 1812 says the same — «ایرانی باستان *vi-janti- از jan (زدن)، بارتولمه ۴۹۰». What is wrong is گزیدن gazīdan / گشتن gaštan: Wiktionary and Cheung take these from MP gazīdan, gaz- of the separate root *gaz (Kurd. gestin, Gilaki gaštən, Bal. gast) that has no Indo-European etymology at all. Nourai has fused two different words that merely look alike in New Persian.\",\n \"derivation_fa\": \"«زدن» بی‌هیچ تردید از این ریشه است: ایرانی باستان *ǰan- > فارسی میانه zadan/zan- > فارسی نو زدن؛ ǰ ایرانی در حوزهٔ جنوب‌غربی (فارسی) به z و در حوزهٔ شمال‌غربی (پارتی، بلوچی) به ž/j بدل می‌شود. حاشیهٔ معین بر برهان قاطع (ص۱۰۰۷) همین زنجیره را می‌آورد: «پهلوی zatan و zadan … اوستایی jan/gan، پارسی باستان jan-، هندی باستان han، بارتولمه ۴۹۰». «آژدن/آزدن» همان *ā-ǰata- است و ابوالقاسمی نشان می‌دهد که هر دو املا از یک صورت‌اند: آژد از راه پهلوی اشکانی و آزد از راه فارسی میانه؛ نوشین در «واژه‌نامک» ص۲۶ آژدن را «خلانیدن و خلیدن» معنی کرده و همان بیت فردوسی را شاهد آورده. «بهرام» نیز دنبالهٔ Vərəθraγna اوستایی است (پارتی و پهلوی Wahrām). «گزند» هم درست است اما نه از راهی که چارت نشان می‌دهد: چونگ و حاشیهٔ معین (برهان ص۱۸۱۲) آن را از *vi-janti- می‌گیرند، یعنی از گرهٔ ۱۱ نه از این گره. اما «گزیدن/گشتن» نادرست است: ویکی‌واژه و چونگ آن را از فارسی میانه gazīdan از ریشهٔ جداگانهٔ *gaz می‌دانند که هیچ ریشهٔ هندواروپایی ندارد. پس نورایی دو واژهٔ همانند اما بی‌ربط را یکی گرفته است.\",\n \"sources\": [ZADAN, GAZIDAN, BAHRAM],\n \"ref_check\": [\n  {\"ref\": \"HRN:204\", \"status\": \"partial\", \"note\": \"Horn no. 916 (p. 204) covers only gazand ('gezend, guzend … aw. *vi-jainti-'); he says nothing about gazīdan and does not treat zadan on that page.\"},\n  {\"ref\": \"BQT:1007\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 470 (printed p. 1007; the offset leaf+537 is fixed by انگژه on v1 p.175 and by زهر on v2 p.1047, both of which land exactly on Nourai's numbers). Mo'in's footnote to زدن: «پهلوی zatan و zadan از ریشهٔ ایرانی قدیم … اوستایی jan/gan … پارسی باستان jan- … هندی باستان han (کشتن). بارتولمه ۴۹۰» with the Kurdish, Afghan, Baluchi, Shughni, Tabari and Gilaki cognates.\"},\n  {\"ref\": \"BQT:324\", \"status\": \"supports\", \"note\": \"v1 leaf 545 = p. 324, the بهرام footnote quoted under node 1: Av. Vərəθraγna, second element γna from the root jan/gan 'زدن و کشتن'.\"},\n  {\"ref\": \"BQT:1812\", \"status\": \"partial\", \"note\": \"BQT_v3_pages.txt pdf 609 (running head shows -۱۸۱۱- on pdf 608, so pdf 609 = p. 1812). The footnote there is for گزند, not گزیدن: «پارسی جدید gazand, guzand (شکل جنوب غربی) … ایرانی باستان *vi-janti- از jan (زدن)، بارتولمه ۴۹۰، نیبرگ». It supports gazand but not the gazīdan of the headword line.\"},\n  {\"ref\": \"FSF:26\", \"status\": \"supports\", \"note\": \"FSF.txt, entry آژدن: «۲- معنی دیگر آژدن خلانیدن و خلیدن است: به داغی جگرشان کنی آژده / که بخشایش آرد برایشان دده» — Nourai's gloss 'to poke' and his Ferdowsi quotation come from here.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, s.v. zadan and s.v. gazidan\", \"stance\": \"partial\", \"note\": \"'zadan, zan- [MHYTWN-tn' … | M zdn, zn-, N زدن]' strike — supports zadan; but 'gazidan, gaz- [gc-, gz-ytn' | N -] bite, sting' is a separate Pahlavi lemma with no connection drawn to zadan.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *jan p. 226 (NWIR section) and s.v. *gaz p. 118\", \"stance\": \"partial\", \"note\": \"'*NWIR: Widely attested: NP zadan/zan- …' and '(+ *ui-) NP gazand ,damage, injury''; but gazīdan is filed under the unrelated *gaz, with 'Kurd. gastin, gazin/gaz-, … NP gazidan'.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. gʷhen-\", \"stance\": \"supports\", \"note\": \"'gʷhen- radical of general sense: \\\"drive, beat, kill\\\". WP I, 679 … Skt. hánmi: Av. jainmi; OPer. -janam; Per. zanam, inf. zadan'.\"},\n  {\"src\": \"FFD\", \"where\": \"p. 25 s.v. آزدن، آژدن\", \"stance\": \"supports\", \"note\": \"«آزد < ایرانی باستان *ā-ǰa-ta … ǰ ایرانی باستان در پهلوی اشکانی ž و در فارسی میانه z شده است» — explains both spellings of Nourai's âzdan.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Old Persian\", \"words\": \"jan : to strike\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian jan- is directly attested in the Achaemenid inscriptions: 3sg. present ja(n)tiy (DSe 36, 40), 1sg. imperfect ajanam (DB 1.89 etc.), imperative jadiy (DB 2.31), 2pl. jatā (DB 2.21). Kent's Lexicon (pp. 184-185) heads the entry 'jan- vb. \\\"strike; smite, defeat (enemy in battle); mould (brick)\\\"' and equates it with Av. jan-, Skt. han-, Gk. θείνει, Lat. dē-fendit, pIE *gʷhen-. The Old Persian outcome shows the same *gʷh > ǰ palatalisation as Avestan, and the writing system's inability to note a nasal before a consonant is why Kent prints ja(n)tiy. Nourai's gloss 'to strike' and his page reference are both exact.\",\n \"derivation_fa\": \"ستاک jan- در سنگ‌نبشته‌های هخامنشی به‌روشنی گواهی شده است: ja(n)tiy سوم‌شخص مفرد (DSe ۳۶، ۴۰)، ajanam «زدم» (بیستون ۱٫۸۹)، jadiy امر (بیستون ۲٫۳۱)، jatā امر جمع. کنت در واژه‌نامهٔ «پارسی باستان» صص۱۸۴–۱۸۵ مدخل را چنین آورده: «jan- فعل: زدن، شکست دادن (دشمن در نبرد)، خشت زدن؛ اوستایی jan-، سنسکریت han-، یونانی θείνει، لاتین dē-fendit، هندواروپایی *gʷhen-». دگرگونی *gʷh > ǰ در پارسی باستان همانند اوستایی است. ادعای نورایی و ارجاع او هر دو درست است.\",\n \"sources\": [PIE],\n \"ref_check\": [{\"ref\": \"KNT:184,185\", \"status\": \"supports\", \"note\": \"KNT.txt (leaf 207; the printed '185' page-break falls inside the article): 'jan- vb. \\\"strike; smite, defeat (enemy in battle); mould (brick)\\\": Av. jan- (gan-, Bthl. AiW 490), Skt. han-, Gk. θείνει \\\"strikes\\\", φόνος \\\"murder\\\", Lt. dē-fendit \\\"wards off\\\", pIE *gʷhen- … jaⁿtiy … ajanam 1st sg. imf. … jadiy 2d sg. imv. … jatā 2d pl. imv.'\"}],\n \"consulted\": [\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *jan, OLD PERSIAN section p. 224\", \"stance\": \"supports\", \"note\": \"'*OLD PERSIAN: ja(n)- \\\"to strike; smite, defeat (enemy in battle); mould (brick)\\\" || (+ *aua-) … (+ *pati-) … (+ *fra-) = Kent: 184b f.' — Cheung takes the entry over from exactly the pages Nourai cites.\"},\n  {\"src\": \"BRT\", \"where\": \"AiW col. 490 f. s.v. gan-\", \"stance\": \"supports\", \"note\": \"Bartholomae files the Old Persian forms (Bh. ajanam, avajanam, jadiy, jatā) inside the Avestan gan-/jan- article, i.e. one and the same root.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Old Persian\", \"words\": \"ni-jan : to strike down, to put (somebody) down\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The prefixed verb *ni-jan- 'to strike down' is securely Iranian: Avestan has ni-jan- (opt. ni.γnīta, part. nijata-, Vd 9.56 nijanaite) and Cheung lists it among the Avestan preverb combinations of *jan. In Old Persian, however, it is not attested; Horn (Grundriss no. 1031, p. 231) sets it up as a reconstruction precisely to explain nažand — 'ap. *ni + √jan- \\\"niederschlagen\\\", also etwa ein ap. *nijantu- \\\"niederschlagbar\\\" voraussetzend' — and Mo'in repeats the reconstruction in Borhan (p. 2134: «پارسی باستان *ni-jan-»). So the node is right in substance, but the label 'Old Persian' hides an asterisk: the form is inferred, not read off an inscription (Kent's lexicon has no ni-jan). Semantically the compound is transparent: ni- 'down' (PIE *ni-) + jan- 'strike'.\",\n \"derivation_fa\": \"فعل پیشوندی *ni-jan- «فروکوفتن» در ایرانی مسلم است: در اوستا ni-jan- گواهی دارد (ni.γnīta، nijata-، nijanaite در وندیداد ۹٫۵۶) و چونگ آن را در فهرست پیشوندهای *jan آورده است. اما در پارسی باستان گواهی نشده؛ هرن (بند ۱۰۳۱، ص۲۳۱) آن را تنها برای توضیح «نژند» بازسازی می‌کند: «پارسی باستان *ni + √jan- یعنی فروکوفتن، و بنابراین صورتی چون *nijantu- را باید فرض کرد» — و خودِ او می‌افزاید «نامطمئن». معین نیز در حاشیهٔ برهان (ص۲۱۳۴) همین بازسازی را تکرار کرده است. پس ادعای نورایی در جوهر درست است، ولی برچسب «پارسی باستان» صورتی ستاره‌دار را می‌پوشاند؛ در واژه‌نامهٔ کنت ni-jan نیست. از نظر معنایی ترکیب روشن است: ni- «فرود» + jan- «زدن».\",\n \"sources\": [PIE],\n \"ref_check\": [{\"ref\": \"HRN:231\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 253 (printed p. 231), no. 1031: 'nižand, nežand \\\"niedergeschlagen (trop.); elend, niedrig\\\". ap. *ni + √jan- \\\"niederschlagen\\\", also etwa ein ap. *nijantu- \\\"niederschlagbar\\\" voraussetzend … Unsicher.' Horn gives the arrow but marks it uncertain.\"}],\n \"consulted\": [\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *jan, Avestan section p. 224\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: jan- (γn-) … || (+ *ni-) \\\"to strike down\\\"', with OPT. 3sg. med. Y Av. paiti.γnita, IND. 3sg. med. Y Av. nijanaite (V 9.56) and perf. pass. Y Av. nijata- (Yt 5.77) — the compound exists, in Avestan.\"},\n  {\"src\": \"KNT\", \"where\": \"Lexicon pp. 184-185\", \"stance\": \"silent\", \"note\": \"Kent lists ava-, pati-, fra- and vi- + jan- but no ni- + jan-, i.e. the Old Persian label rests on Horn's reconstruction only.\"},\n  {\"src\": \"BQT\", \"where\": \"vol. 4, printed p. 2134, Mo'in's footnote\", \"stance\": \"supports\", \"note\": \"«پارسی باستان *ni-jan- (به زمین انداختن، فروشکستن). همچنین در پارسی باستان *ni-jantiya- (خوارکردنی، فروافکندنی) مفروض است … نیبرگ ص۱۵۸».\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"nažand «نژند» : put down, feeling sad\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Borhan-e Qāte' glosses نژند exactly as Nourai does — «اندوهگین و غمناک و فرومانده و افسرده و سرفرود افکنده و پژمرده … و پست و حضیض» ('sorrowful, dejected, with the head bowed down; low as opposed to high') — so the semantic step 'struck down' → 'cast down, low, sad' is documented inside Persian itself. The formal derivation is Horn's: an Old Iranian verbal adjective *ni-janti-/*ni-jantiya- 'to be struck down' gives Middle Persian *nižand and NP nižand/nažand, the -nd being the same suffix as in gazand < *vi-janti-, which is the strongest argument for the analysis (the two words are morphologically identical, only the preverb differs). Mo'in's footnote in Borhan repeats it and adds a reference to Nyberg. The reason this is 'plausible' rather than 'confirmed' is that Horn himself closes the paragraph with a bare 'Unsicher', and the form is nowhere attested in Middle Persian; there is no independent modern treatment that removes the doubt.\",\n \"derivation_fa\": \"برهان قاطع «نژند» را دقیقاً به همان معنایی می‌آورد که نورایی داده است: «اندوهگین و غمناک و فرومانده و افسرده و سرفرود افکنده و پژمرده … و پست و حضیض». پس تحول معنایی «فروکوفته‌شده» ← «سرافکنده، اندوهگین» در خودِ فارسی مستند است. ریشه‌شناسی از آنِ هرن است: صفت فعلی ایرانی باستان *ni-janti-/*ni-jantiya- «فروکوفتنی» که در فارسی میانه *nižand و در فارسی نو نژند/نژند شده است؛ قوی‌ترین دلیل آن است که «گزند» < *vi-janti- از نظر ساخت دقیقاً همین است و تنها پیشوندش فرق می‌کند. حاشیهٔ معین بر برهان (ص۲۱۳۴) همین را می‌گوید و به نیبرگ ارجاع می‌دهد. اما چون خودِ هرن پاراگراف را با واژهٔ «نامطمئن» می‌بندد و صورت میانه‌ای گواهی نشده، حکم را «با احتیاط پذیرفتنی» گذاشتیم نه «تأییدشده».\",\n \"sources\": [PIE],\n \"ref_check\": [\n  {\"ref\": \"HRN:231\", \"status\": \"supports\", \"note\": \"Grundriss no. 1031: 'nižand, nežand \\\"niedergeschlagen (trop.); elend, niedrig\\\". ap. *ni + √jan- … *nijantu- … Unsicher.'\"},\n  {\"ref\": \"BQT:2134\", \"status\": \"supports\", \"note\": \"BQT_v4_pages.txt pdf 217/218 (the running head '-۲۱۳۵-' on pdf 218 fixes printed = pdf + 1917). Headword نژند with the gloss «اندوهگین و غمناک و فرومانده و افسرده و سرفرود افکنده و پژمرده … و پست و حضیض» and Mo'in's footnote «پارسی باستان *ni-jan- … *ni-jantiya- … مفروض است … نیبرگ ص۱۵۸».\"},\n  {\"ref\": \"MON:4713\", \"status\": \"not_checked\", \"note\": \"The local Mo'in files (MON_part1/2.txt, MON_2vol_Adena_*_djvu.txt) contain no Persian text for نژند (grep returns nothing), and no page-4713 scan is on disk; Nourai's Mo'in volume is not the Adena two-volume reprint that is available here.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"vol. 4, printed p. 2134-2135\", \"stance\": \"supports\", \"note\": \"See ref_check; both the gloss and the *ni-jan- footnote.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 1031, p. 231\", \"stance\": \"partial\", \"note\": \"Gives Nourai's derivation but ends 'Unsicher.'\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, n- section\", \"stance\": \"silent\", \"note\": \"No Pahlavi *nižand is recorded; MacKenzie has nizārīh 'feebleness' but nothing from *ni-jan-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Old Persian\", \"words\": \"ava-jan, apa-jan : to strike down, kill\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Kent's lexicon (p. 184) has the compound as its own paragraph: 'ava- + jan- and ava- + ā + jan- \\\"smite down, slay\\\"', listing avājanam (DB 1.57 etc.), apājan (DB 1.31), avājanā (DB 2.13), avājaniyā (DB 1.51-52) and the participle avajata- (DB 1.32). Nourai's 'apa-jan' is Kent's apājan, the writing with ap- that Kent explains as ava- before ā (§206c). The compound survives straight through Middle Iranian: Manichaean MP 'wzn- / 'wzdn, Book Pahlavi ōzadan, ōzan- 'to kill', Parthian 'wjn-, all of which Nyberg files under Av. ava-gan- (AiW 491). Nourai's gloss 'to strike down, kill' is exactly Kent's.\",\n \"derivation_fa\": \"کنت در واژه‌نامهٔ خود (ص۱۸۴) این ترکیب را بندی جداگانه کرده است: «ava- + jan- و ava- + ā + jan- «فروکوفتن، کشتن»» با صورت‌های avājanam (بیستون ۱٫۵۷)، apājan (۱٫۳۱)، avājanā (۲٫۱۳)، avājaniyā (۱٫۵۱–۵۲) و صفت مفعولی avajata- (۱٫۳۲). صورت «apa-jan» نورایی همان apājan کنت است که او آن را ava- پیش از ā می‌داند. این ترکیب یکسره به ایرانی میانه رسیده است: فارسی میانهٔ مانوی 'wzn-/'wzdn، پهلوی کتابی ōzadan/ōzan- «کشتن»، پارتی 'wjn-؛ و نیبرگ همهٔ اینها را ذیل ava-gan- اوستایی (بارتولمه ۴۹۱) آورده است. معنایی که نورایی داده عیناً معنای کنت است.\",\n \"sources\": [PIE],\n \"ref_check\": [{\"ref\": \"KNT:184\", \"status\": \"supports\", \"note\": \"KNT.txt leaf 207 (printed p. 184): 'ava- + jan- and ava- + ā + jan- \\\"smite down, slay\\\" (apparently ava- in avajata, apa-ā- in avājaniyā …): avājanam 1st sg. imf. DB 1.57, 59, 73, 83 … apājan imf. DB 1.31 bis … avājanā 3d pl. imf. DB 2.13 … avajata nsm. past ptc. pass. DB 1.32'.\"}],\n \"consulted\": [\n  {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary), s.v. ōzatan\", \"stance\": \"supports\", \"note\": \"'ōzatan [ʾwctn'; YKTLWN-tn'] ōzan- to kill … — Av. (491) ava-gan-, pres. -jan-, pt. -jata-; MPrth 'wjdn 'wjn- (MHC); MPrs 'wzdn 'wzn-; Paz. awazadan awazan-.'\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *jan, MP and Parthian sections p. 225\", \"stance\": \"supports\", \"note\": \"'(+ *aua-) MMP 'wzn-, BMP 'wc- /ōz-/ \\\"to kill\\\"' and Parthian ''wjn- \\\"to kill\\\"'.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. ōzadan\", \"stance\": \"supports\", \"note\": \"'ōzadan, ōzan- [YKTLWN-, YKTLWN-tn' < A ... qtl; 'wctn' | M 'wzdn, 'wzn-] kill.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"owžandan «اوژندن ( اوژدن ، ـ اوژن )» : to strike down\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP اوژندن / اوژدن, present stem اوژن-, continues Middle Persian ōzadan, ōzan- 'to kill' < Old Iranian *aua-ǰan- (node 6). The -ž- rather than -z- shows the word came into New Persian through a north-western (Parthian) channel — Parthian 'wjdn / 'wjn- — the same ž that Abolghasemi invokes for آژدن. Noushin's Shāhnāme glossary (Vazhe-namak p. 55) gives 'اوژن: اسم فاعل مرخم از اوژنیدن به معنی افکندن، زدن، کشتن' and quotes the Pahlavi Xusraw ud rēdag passage «شیران را باوژن» beside the Ferdowsi couplet Nourai prints (شیراوژن), and the compounds شیراوژن 'lion-slayer' and گرداوژن 'hero-slayer' are exactly the -ōzan agent forms. Borhan p. 184 has the family اوژنیدن / اوژندیدن glossed «افکندن و انداختن».\",\n \"derivation_fa\": \"«اوژندن/اوژدن» با ستاک حال «اوژن-» دنبالهٔ فارسی میانهٔ ōzadan/ōzan- «کشتن» است، از ایرانی باستان *aua-ǰan- (گرهٔ ۶). وجود ž به‌جای z نشان می‌دهد که واژه از راه شمال‌غربی (پارتی 'wjdn/'wjn-) وارد فارسی دری شده است، همان ابدالی که ابوالقاسمی برای «آژدن» نیز یاد می‌کند. نوشین در «واژه‌نامک» ص۵۵ می‌نویسد: «اوژن: اسم فاعل مرخم از اوژنیدن به معنی افکندن، زدن، کشتن»، و هم متن پهلوی «خسرو و ریدک» («شیران را باوژن») و هم همان بیت فردوسی («بپرسید شیراوژن از شهریار») را شاهد می‌آورد. ترکیب‌های «شیراوژن» و «گرداوژن» نیز همین ستاک فاعلی‌اند. برهان قاطع در ص۱۸۴ «اوژنیدن/اوژندیدن» را «افکندن و انداختن» معنی کرده است. ادعای نورایی درست است.\",\n \"sources\": [PIE],\n \"ref_check\": [\n  {\"ref\": \"BQT:184\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 403 (printed p. 184, offset leaf−219 fixed by انگژه = p. 175): the entries «اوژنک»، «اوژندیدن»، «اوژنید» with the gloss «بمعنی افکندن و انداختن باشد» / «ماضی افکندن و انداختن باشد». Borhan has the family but glosses it 'cast down' rather than 'strike down'.\"},\n  {\"ref\": \"FSF:55\", \"status\": \"supports\", \"note\": \"FSF.txt s.v. اوژن: «اسم فاعل مرخم از اوژنیدن به معنی افکندن. زدن. کشتن … در واژه مرکب، شیر اوژن = شیرافکن؛ گرداوژن، گردان‌کن … پهلوی ōzan: شاهنشاه به ریدک گفت که شو، شیران را باوژن» plus Nourai's own Ferdowsi line «گرفتند هر سه ورا در کنار / بپرسید شیراوژن از شهریار».\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. ōzadan\", \"stance\": \"supports\", \"note\": \"'ōzadan, ōzan- … | M 'wzdn, 'wzn-] kill.'\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. ōzatan\", \"stance\": \"supports\", \"note\": \"'Av. (491) ava-gan-, pres. -jan-, pt. -jata-; MPrth 'wjdn 'wjn-; MPrs 'wzdn 'wzn-; Paz. awazadan awazan-.'\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *jan p. 225\", \"stance\": \"supports\", \"note\": \"The whole *aua-ǰan paradigm from Manichaean MP and Parthian down to Ormuri užnaw- 'to kill'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Old Persian\", \"words\": \"vâra-ğna : lamb killer (falcon, crow)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The word and the analysis are right; the language label is not. vārəγna- 'falcon' is an AVESTAN noun (Yt 14, the bird into which Vərəθraγna transforms); it is not attested in Old Persian. The analysis Nourai gives is Pokorny's own: under 'u̯erēn- \\\"Widder, Schaf, Lamm\\\"' on p. 1170 Pokorny writes 'vgl. npers. barra (*varnak) \\\"Lamm\\\", pehl. varak \\\"Widder\\\"; iran. vārən-jar-, vārə-γna- \\\"Lämmerschläger\\\" (Humbach DLZ 78, 299 f.)' — i.e. *wāran- 'lamb' + -γna- 'slayer', the zero-grade *gʷhn- of this very root, exactly parallel to vərəθra-γna-. So 'lamb killer' is not Nourai's invention but Humbach's etymology as adopted by Pokorny on the page cited. Gharib s.v. the Sogdian cognate likewise refers the word to 'Av. vārəγna-'.\",\n \"derivation_fa\": \"واژه و تحلیل درست است، اما برچسب زبانی نادرست: vārəγna- «شاهین» واژه‌ای اوستایی است (یشت ۱۴، پرنده‌ای که ورثرغنه به پیکر آن درمی‌آید) و در پارسی باستان گواهی نشده است. تحلیلی که نورایی می‌دهد از آنِ خودِ پوکورنی است: در صفحهٔ ۱۱۷۰ ذیل ریشهٔ u̯erēn- «قوچ، گوسفند، بره» می‌نویسد: «قس فارسی نو barra (*varnak) «بره»، پهلوی varak «قوچ»؛ ایرانی vārən-jar-، vārə-γna- «بره‌کوب» (هومباخ)». یعنی *wāran- «بره» + -γna- «کُشنده»، همان درجهٔ صفر *gʷhn- همین ریشه، درست به قیاس vərəθra-γna-. پس «بره‌کش» ساختهٔ نورایی نیست بلکه ریشه‌شناسی هومباخ است که پوکورنی در همان صفحهٔ مورد ارجاع پذیرفته. قریب نیز در فرهنگ سغدی همین واژه را به «اوستایی vārəγna-» بازمی‌گرداند.\",\n \"sources\": [PIE],\n \"ref_check\": [\n  {\"ref\": \"POK:1170\", \"status\": \"supports\", \"note\": \"POK_03.txt line 5887 (the '1170' page marker is at line 5882), s.v. u̯erēn- 'Widder, Schaf, Lamm': '… vgl. npers. barra (*varnak) \\\"Lamm\\\", pehl. varak \\\"Widder\\\"; iran. vārən-jar-, vārə-γna- \\\"Lämmerschläger\\\" (Humbach DLZ 78, 299 f.)'. Nourai's gloss 'lamb killer' is verbatim Pokorny's 'Lämmerschläger'.\"},\n  {\"ref\": \"BQT:1669\", \"status\": \"partial\", \"note\": \"BQT_v3_pages.txt pdf 462 = printed p. 1669 f. is the کلاغ article; its footnote quotes «از ریشهٔ اوستایی vārəγna (شاهین)» — it supports the Avestan etymon but calls it Avestan, not Old Persian, and is really the reference for node 10.\"}\n ],\n \"consulted\": [\n  {\"src\": \"SOD\", \"where\": \"Gharib no. 9855, printed p. 398 f.\", \"stance\": \"supports\", \"note\": \"'w'rγn'k /warəγnē/ … ©Av. vārəγna-, Khwar. w'rγnwk; Oss. wari; Pahl. wārišak/wāriš — falcon' — the etymon is labelled Avestan.\"},\n  {\"src\": \"BRT\", \"where\": \"AiW, v-section\", \"stance\": \"silent\", \"note\": \"The Google-scan OCR of Bartholomae in the repo is too corrupt in the v- columns for vārəγna- to be located by grep (searches on vārəγna, varegna, Falke, ragna all fail to hit the article).\"},\n  {\"src\": \"KNT\", \"where\": \"Lexicon\", \"stance\": \"silent\", \"note\": \"No vāra-γna or any *wāran- word in the Old Persian lexicon — confirming the language label is wrong.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Sogdian\", \"words\": \"w`rğn`k : falcon\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian w'rγn'k, read warəγnē, is the regular Sogdian continuation of Old Iranian *wāra-γna-: the -āka- suffix (Sogd. -'k) is added to the inherited stem and Sogdian keeps the intervocalic -γ- that Persian and Khotanese lose. Gharib's Sogdian-Persian-English Dictionary gives the entry with precisely this etymology and lists the sister forms (Khwarezmian w'rγnwk, Ossetic wari, Pahlavi wārišak/wāriš), citing Benveniste's Vṛtra et Vṛθragna (1934) and Bailey. Nourai's page reference is right: the entry stands at the foot of printed p. 398 / head of p. 399.\",\n \"derivation_fa\": \"صورت سغدی w'rγn'k که warəγnē خوانده می‌شود دنبالهٔ قانونمند *wāra-γna- ایرانی باستان است: پسوند -āka- (در سغدی -'k) بر ستاک موروثی افزوده شده و سغدی γ میان‌واکه‌ای را — برخلاف فارسی و ختنی — نگه داشته است. قریب در «فرهنگ سغدی» همین ریشه‌شناسی را می‌دهد و صورت‌های خواهر را برمی‌شمارد: خوارزمی w'rγnwk، آسی wari، پهلوی wārišak/wāriš، با ارجاع به بنونیست (ورثره و ورثرغنه، ۱۹۳۴) و بیلی. ارجاع صفحهٔ نورایی درست است: مدخل در پایان ص۳۹۸ و آغاز ص۳۹۹ چاپی است. ادعای نورایی درست است.\",\n \"sources\": [PIE],\n \"ref_check\": [{\"ref\": \"SOD:398\", \"status\": \"supports\", \"note\": \"SOD.txt / SOD_pages.txt leaf 466 (printed p. 398-399): '9855 w'rγn'k B — warəγnē (w'γyn'y) ©Av. vārəγna-, Khwar. w'rγnwk; Oss. wari; Pahl. wārišak/wāriš — falcon. TSP 13ii 14 n p228; SCE 359; Ben v. Vṛtra et Vṛθragna, 1934, 34; Bailey, Garuḍmant, 10'.\"}],\n \"consulted\": [\n  {\"src\": \"SOD\", \"where\": \"no. 9855\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n  {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka\", \"stance\": \"silent\", \"note\": \"Greps for vārəγna / vārgan / w'rγn in ISS_alt_DKS.txt return nothing, so no Khotanese control on the Sogdian form could be obtained from the local copy.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"varğeneh «ورغنه» : falcon ; kalâğ «کلاغ» : crow\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The two words have to be judged separately. ورغنه varγeneh 'falcon' is, if it exists as a Persian headword, the expected reflex of *wāra-γna-ka- through a dialect that kept -γ- (compare Sogd. warəγnē and Khwar. w'rγnwk); it could not be found in Borhan-e Qāte' (no «ورغ» headword in vols 1-4 of the scan), so the word itself is unverified here, but the chain Av. vārəγna- > Sogd. w'rγn'k > a Persian falcon-name is at least coherent. کلاغ kalāγ 'crow' is another matter. Mo'in's footnote in Borhan (p. 1669) does derive it from the Avestan vārəγna, which is plainly where Nourai got the arrow. Modern scholarship does not follow: Wiktionary, gathering Baluchi kalág, Mazanderani kalāǰ, Gilaki kəlāč, Fars qalâğ, Luri qelā and Ossetic xalon, says the word is 'from a Proto-Iranian root not attested in Middle Persian … probably ultimately onomatopoeic, but perhaps from PIE *ḱer- \\\"crow\\\"' — the same imitative family as Lat. corvus and Gk. kórax. Phonetically the derivation from vārəγna- is also hard: it would need an unexplained loss of the initial v- and a k- from nowhere. Verdict: the falcon word may stand, the crow does not.\",\n \"derivation_fa\": \"دو واژه را باید جدا سنجید. «ورغنه» اگر مدخلی فارسی باشد، بازتاب مورد انتظارِ *wāra-γna-ka- از گویشی است که γ را نگه داشته (قس سغدی warəγnē و خوارزمی w'rγnwk)؛ اما در اسکن چهار جلد برهان قاطع هیچ مدخل «ورغ...» یافت نشد، پس خودِ واژه در اینجا تأیید نشد، هرچند زنجیرهٔ اوستایی vārəγna > سغدی w'rγn'k > نام پرندهٔ فارسی سازگار است. اما «کلاغ» چیز دیگری است. حاشیهٔ معین بر برهان (ص۱۶۶۹) آن را «از ریشهٔ اوستایی vārəγna (شاهین)» می‌داند و بی‌گمان سرچشمهٔ پیکان نورایی همین است. پژوهش امروزی این را نمی‌پذیرد: ویکی‌واژه با گرد آوردن بلوچی kalág، مازندرانی kalāǰ، گیلکی kəlāč، فارسیِ فارس qalâğ، لری qelā و آسی xalon می‌نویسد که واژه «از ریشه‌ای ایرانی که در فارسی میانه گواهی نشده» است و «به احتمال زیاد آوایی/ نام‌آوا (onomatopoeic) است، شاید از *ḱer- هندواروپایی» — همان خانوادهٔ corvus لاتین و kórax یونانی. از نظر آوایی نیز گرفتن کلاغ از vārəγna دشوار است: افتادن v آغازین و پیدا شدن k توجیه ندارد. حکم: نام شاهین شاید بماند، اما کلاغ نه.\",\n \"sources\": [KALAGH],\n \"ref_check\": [\n  {\"ref\": \"BQT:1669\", \"status\": \"supports\", \"note\": \"BQT_v3_pages.txt pdf 462 (printed p. 1669), Mo'in's footnote 1 to کلاغ: «kalagh, kulagh … از ریشهٔ اوستایی vārəγna (شاهین) … ورک: هوبشمان ۸۹۷؛ قس کردی kala (کلاغ)، زازا …، سمنانی kala، … و قس یونانی korax، لاتین corvus (کلاغ)، cornix (زاغ)». The reference does say what Nourai's arrow says.\"},\n  {\"ref\": \"SOD:398\", \"status\": \"partial\", \"note\": \"Gharib no. 9855 supports the Avestan etymon and gives Pahlavi wārišak/wāriš as the Persian-side reflex — not ورغنه, and certainly not کلاغ.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"vol. 3, printed p. 1669, footnote to کلاغ\", \"stance\": \"supports\", \"note\": \"See ref_check; Mo'in is the source of Nourai's claim.\"},\n  {\"src\": \"SOD\", \"where\": \"no. 9855\", \"stance\": \"partial\", \"note\": \"Gives Pahl. wārišak/wāriš as the Middle Persian continuation, i.e. a -š- form, not a -γ- form such as ورغنه.\"},\n  {\"src\": \"MON\", \"where\": \"MON_part1/2.txt and the Adena reprint\", \"stance\": \"silent\", \"note\": \"Grep for ورغنه finds nothing in any local Mo'in file.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Old Persian\", \"words\": \"pati-jan : fight against ; fra-jan : cut off ; vi-jan : strike apart, shatter\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three compounds are in Kent's article on exactly the pages cited, each with its own sub-paragraph and its own inscriptional attestation: 'pati- + jan- \\\"fight against\\\": patiyajatā imf. mid. DNa 47'; 'fra- + jan- \\\"cut off\\\": frājanam 1st sg. imf. DB 2.74, 89'; 'vi- + jan- \\\"shatter\\\": vijanātiy 3d pl. subj. A²Sa 5, A²Ha 7'. The glosses in the chart are Kent's own words. Semantically the three show the normal Old Iranian preverb system: pati- 'against' (Av. paiti-, PIE *poti-) gives the reciprocal 'fight back', fra- 'forth, away' gives 'strike off, sever' (Darius' frājanam of the rebel's nose and ears, DB 2.74), vi- 'apart' gives 'shatter'. The last one is the ancestor of NP gazand < *vi-janti-.\",\n \"derivation_fa\": \"هر سه ترکیب در همان صفحه‌هایی که نورایی ارجاع داده در واژه‌نامهٔ کنت آمده‌اند، هرکدام با بندی جداگانه و گواه سنگ‌نبشته‌ای: «pati- + jan- «جنگیدن با»: patiyajatā در نقش رستم ۴۷»؛ «fra- + jan- «بریدن»: frājanam در بیستون ۲٫۷۴ و ۸۹»؛ «vi- + jan- «درهم شکستن»: vijanātiy در A²Sa ۵ و A²Ha ۷». معنی‌هایی که در چارت آمده عین واژه‌های کنت است. از نظر معنایی، دستگاه پیشوندی ایرانی باستان به‌روشنی کار می‌کند: pati- «در برابر» معنی متقابل می‌دهد، fra- «پیش، دور» معنی «بریدن و جدا کردن» (داریوش در بیستون ۲٫۷۴ بینی و گوش شورشی را frājanam می‌کند)، و vi- «جدا از هم» معنی «درهم شکستن». همین آخری نیای «گزند» فارسی است (< *vi-janti-). ادعای نورایی درست است.\",\n \"sources\": [PIE],\n \"ref_check\": [\n  {\"ref\": \"KNT:184,185\", \"status\": \"supports\", \"note\": \"KNT.txt leaf 207: 'pati- + jan- \\\"fight against\\\": patiyajatā imf. mid. (§140.III, §208, §235.II) DNa 47.' / 'fra- + jan- \\\"cut off\\\": frājanam 1st sg. imf. (§226.II) DB 2.74, 89.' / 'vi- + jan- \\\"shatter\\\": vijanātiy 3d pl. subj. (§208, §222.III, §232.I) A²Sa 5, A²Ha 7 (conj. Kent).'\"},\n  {\"ref\": \"HRN:231\", \"status\": \"not_found\", \"note\": \"Horn p. 231 (leaf 253) contains nos. 1030-1034 (nižād, nižand, nišāstan, nišastan, nišēb); none of pati-jan, fra-jan or vi-jan is discussed there. The vi-jan material is on Horn p. 204 (no. 916), not 231.\"}\n ],\n \"consulted\": [\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *jan pp. 224-225\", \"stance\": \"supports\", \"note\": \"'*OLD PERSIAN: ja(n)- … || (+ *aua-) … || (+ *pati-) \\\"to fight against\\\" || (+ *fra-) \\\"to cut off\\\" = Kent: 184b f.', and for Sogdian: '(+ *fra-) MSogd. frjn- \\\"to cut off\\\". © Henning 1965: 32 fn. 4: \\\"The close agreement in meaning with Old Persian frajan- is noteworthy.\\\"'\"},\n  {\"src\": \"BRT\", \"where\": \"AiW s.v. gan-, section paiti.jan-\", \"stance\": \"supports\", \"note\": \"'mit paiti … \\\"sich wehren gegen —, bekämpfen\\\", mit Akk.: … hamaram patiyajatā (3SPrM.) D. Na 4' — Bartholomae files the Old Persian form under the Avestan root article.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"jatara : resin (obtained by striking a tree trunk) ; jathra : poison ; paiti-jathra : anti-poison\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The 'poison' half is right and the 'resin' half is wrong. (1) *jaθra- 'poison' is the standard reconstruction behind MP/NP zahr: Hübschmann (Persische Studien no. 679) writes 'Ich führe daher zahr \\\"Gift\\\" … auf *jaθra- = skr. *hatra- \\\"Mittel zum Tödten\\\" zurück', and Watkins/AHD file the word under gʷhen-¹ as '4. Suffixed zero-grade form *gʷhn̥-tro- in Persian zahr, poison: BEZOAR'. Note that it is a reconstruction, not an attested Avestan or Old Persian word. (2) *paiti-jaθra- 'antidote' is a legitimate back-reconstruction of pād-zahr, whose pād- Hübschmann (no. 273) traces to OP patiy; again unattested. (3) 'jatara: resin' is a real Avestan element, but it does not belong to this root. Bartholomae has the mountain-name *yahmya-jatara- (Yt 19.6) and explains it as 'wo (auf welchem Berg) das Harz oder der Asphalt (wächst)', adding 'Vgl. ai. jātu- n. \\\"Gummi\\\", np. žad \\\"Gummi\\\", angu-žad \\\"Harz\\\"'. Sanskrit jātu- 'lac, gum' is Pokorny's own example under a completely different root, '1. gʷet- \\\"Harz\\\"' (IEW 480, with Lat. bitūmen, OE cwidu), which Watkins likewise heads 'gʷet-¹. Resin (?)'. So the resin word is *gʷetu-, not *gʷhen-tro-, and Nourai's gloss 'obtained by striking a tree trunk' is a rationalisation invented to attach it to this chart. The chart's own NOTE ('Derivation of \\\"jatara: resin\\\" is not certain') is therefore an understatement: modern scholarship assigns it elsewhere.\",\n \"derivation_fa\": \"نیمهٔ «زهر» درست است و نیمهٔ «صمغ» نادرست. (۱) *jaθra- «زهر» بازسازی معیار برای zahr پهلوی و فارسی است: هوبشمان در «پژوهش‌های فارسی» بند ۶۷۹ می‌نویسد: «من zahr «زهر» را … به *jaθra- = سنسکریت *hatra- «ابزار کشتن» بازمی‌گردانم»، و واتکینز در پیوست فرهنگ AHD همین را ذیل gʷhen-¹ می‌آورد: «صورت درجه‌صفرِ پسونددار *gʷhn̥-tro- در zahr فارسی». باید توجه داشت که این صورتی بازسازی‌شده است، نه واژه‌ای گواهی‌شده در اوستایی یا پارسی باستان. (۲) *paiti-jaθra- «پادزهر» نیز بازسازی پذیرفتنیِ «پادزهر» است که هوبشمان (بند ۲۷۳) جزء نخست آن را به patiy پارسی باستان می‌رساند. (۳) اما «jatara: صمغ» هرچند صورتی اوستایی است، به این ریشه تعلق ندارد. بارتولمه نام کوه *yahmya-jatara- (یشت ۱۹٫۶) را «جایی که صمغ یا قیر می‌روید» معنی می‌کند و می‌افزاید: «قس سنسکریت jātu- «صمغ»، فارسی نو žad «صمغ»، angu-žad «صمغ درخت»». و سنسکریت jātu- شاهدِ خودِ پوکورنی است ذیل ریشه‌ای یکسره دیگر: «۱. gʷet- «صمغ»» (ص۴۸۰، با bitūmen لاتین و cwidu انگلیسی کهن). پس واژهٔ صمغ از *gʷetu- است نه از *gʷhen-tro-، و توضیح «که با زدن بر تنهٔ درخت به دست می‌آید» توجیهی است که نورایی برای چسباندن آن به این چارت ساخته است. یادداشت خودِ کتاب («اشتقاق jatara نامطمئن است») کم‌گویی است: پژوهش امروزی آن را به ریشهٔ دیگری می‌دهد.\",\n \"sources\": [E + \"bezoar\", ZAHR],\n \"ref_check\": [\n  {\"ref\": \"AHD:1520\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt, s.v. gʷhen-¹: '4. Suffixed zero-grade form *gʷhn̥-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gʷhen-(ə)- 491, bhen- 126.]' — supports jathra 'poison' but says nothing about a resin word; Watkins puts resin under a separate root, 'gʷet-¹. Resin (?) … [Pok. 1. gʷet- 480]'.\"},\n  {\"ref\": \"AEF:335\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq, Asās-e Ešteqāq-e Fārsi vol. I, is not online and not on disk (refs_online.json: kind 'catalog', local_file null, 'Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings)').\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"AiW s.v. *yahmya-jatara- (BRT.txt line ~21517)\", \"stance\": \"contradicts\", \"note\": \"'j. *yahmya-jatara- m. Name eines Bergs oder Gebirgs … Eig. viell. \\\"wo (auf welchem, näml. Berg) das Harz - oder der Asphalt - (wächst)\\\". — Vgl. ai. jātu- n. \\\"Gummi\\\", np. žad \\\"Gummi\\\", angu-žad \\\"Harz\\\".' Bartholomae connects jatara- with Skt. jātu-, i.e. with the resin root, not with gan-/jan-.\"},\n  {\"src\": \"POK\", \"where\": \"IEW 480\", \"stance\": \"contradicts\", \"note\": \"'1. gʷet- \\\"Harz\\\". Ai. jātu n. \\\"Lack, Gummi\\\"; lat. bitūmen \\\"Erdharz, Erdpech\\\" … ags. hwīt cwidu … anord. kvāda f. \\\"Harz\\\".' The resin word has its own PIE root eleven pages before gʷhen-.\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien no. 679\", \"stance\": \"supports\", \"note\": \"For the poison word: 'Ich führe daher zahr \\\"Gift\\\" = kurd. zahr, … arm. LW. zahr, phl. zahr … auf *jaθra- = skr. *hatra- \\\"Mittel zum Tödten\\\" zurück und leite zahra \\\"Galle\\\" … davon ab.'\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, entry زهر (ARY_pages.txt pdf 331-332)\", \"stance\": \"supports\", \"note\": \"The entry heads 'JATHRA (OLD PERSIAN) / ZAHR (PAHLAVI)' and lists as references POKORNY 491 and 'THE AMERICAN HERITAGE DICTIONARY … (GWHEN)' — Aryanpur uses the same reconstruction and even the same spelling 'jathra' as Nourai.\"}\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"žad «ژد ( ژه ، زه ٣ )» : resin ; angžeh «انگژه» : sweet resin\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Persian facts are exactly as the chart gives them. Borhan-e Qāte' p. 1058 has «ژد … مطلق صمغ را گویند» ('žad: gum in general'), and p. 175 explains انگژد and انگژه: «آن را انگژد یعنی آن گون که صمغ درخت انگدان است و اصل آن انگدان‌ژد باشد … چه ژد بلغت فرس بمعنی صمغ است» ('angžad, i.e. the gum of the angudān plant; its original is angudān-žad, since žad in Persian means gum'), and «انگژه مخفف انگوژه است که صمغ درخت انگدان باشد» — hence also انغوزه, the Arabised asafoetida word. What is wrong is only the parent arrow. Bartholomae himself, in the article that supplies Nourai's Avestan jatara-, compares 'np. žad \\\"Gummi\\\", angu-žad \\\"Harz\\\"' with Sanskrit jātu- 'lac, gum', and jātu- is Pokorny's headword example under '1. gʷet- \\\"Harz\\\"' (IEW 480). NP žad from Old Iranian *ǰatu-/*ǰadu- is phonetically straightforward (initial *ǰ- > ž- as in Av. jafra- > NP žarf), so the word is well explained — just not from 'strike'. The cross-reference to 'Embhi' for angžeh (the angudān/anjudān element) is independent of this and unaffected.\",\n \"derivation_fa\": \"داده‌های فارسی درست همان است که چارت می‌گوید. برهان قاطع در ص۱۰۵۸ می‌آورد: «ژد … مطلق صمغ را گویند»، و در ص۱۷۵ دربارهٔ «انگژد» و «انگژه»: «آنرا انگژد یعنی آن گون که صمغ درخت انگدان است و اصل آن انگدان‌ژد باشد … چه ژد بلغت فرس بمعنی صمغ است»، و «انگژه مخفف انگوژه است که صمغ درخت انگدان باشد» — که «انغوزه» معرّبِ همان است. آنچه نادرست است تنها پیکانِ پدر است. خودِ بارتولمه در همان مدخلی که صورت jatara- را به نورایی داده، «فارسی نو žad «صمغ» و angu-žad «صمغ درخت»» را با jātu- سنسکریت «صمغ، لاک» می‌سنجد، و jātu- شاهد سرمدخلِ پوکورنی است ذیل «۱. gʷet- «صمغ»» (ص۴۸۰). تحول ایرانی باستان *ǰatu-/*ǰadu- به ژد فارسی نیز قانونمند است (ǰ آغازین > ž، چنانکه jafra- اوستایی > ژرف). پس واژه به‌خوبی توضیح‌پذیر است، اما نه از ریشهٔ «زدن». ارجاع «انگژه» به ریشهٔ Embhi (جزء انگدان/انجدان) مستقل است و از این ایراد آسیب نمی‌بیند.\",\n \"sources\": [PIE],\n \"ref_check\": [\n  {\"ref\": \"BQT:175\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 394 (printed p. 175): «انگژد … صمغی باشد بغایت بدبوی و آنرا بعربی حلتیت خوانند و آنرا انگژد یعنی آن گون که صمغ درخت انگدان است و اصل آن انگدان ژد باشد … چه ژد بلغت فرس بمعنی صمغ است» and «انگژه … مخفف انگوژه است که صمغ درخت انگدان باشد». Supports the internal analysis of angžeh and the meaning of žad.\"},\n  {\"ref\": \"BQT:1776\", \"status\": \"not_found\", \"note\": \"Printed p. 1776 falls in vol. 3 in the گ (gāf) section (pdf 573; pdf 568 carries the running head ۱۷۷۱ and pdf 570 shows -۱۷۷۳-), which has nothing to do with ژد. The ژد article is in vol. 2 at printed p. 1058 (BQT_v2_pages.txt leaf 521, «بیان دوم در زای فارسی با دال»: «ژد … مطلق صمغ را گویند»). The number 1776 looks copied over from the MON citation.\"},\n  {\"ref\": \"MON:1776\", \"status\": \"not_checked\", \"note\": \"No searchable copy of the six-volume Mo'in on disk (MON_part1/2.txt and the Adena two-volume djvu contain no hit for انگژه/انگژد), and Mo'in is not reachable page-by-page in this session.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"vol. 1 p. 175 and vol. 2 p. 1058\", \"stance\": \"supports\", \"note\": \"See ref_check; both articles support the meaning 'resin' and the compound analysis, neither offers an etymology from 'strike'.\"},\n  {\"src\": \"BRT\", \"where\": \"AiW s.v. *yahmya-jatara-\", \"stance\": \"contradicts\", \"note\": \"'Vgl. ai. jātu- n. \\\"Gummi\\\", np. žad \\\"Gummi\\\", angu-žad \\\"Harz\\\"' — Bartholomae ties NP žad to Skt. jātu-, i.e. to Pokorny's gʷet- 'Harz' (IEW 480).\"},\n  {\"src\": \"POK\", \"where\": \"IEW 480 s.v. 1. gʷet- 'Harz'\", \"stance\": \"contradicts\", \"note\": \"'Ai. jātu n. \\\"Lack, Gummi\\\"; lat. bitūmen …' — the resin family has its own root.\"}\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Persian\", \"words\": \"zahr «زهر» : poison ; pâdzahr «پادزهر ( پازهر ، پای زهر )» : antitoxin\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP زهر zahr < MP zahr (Book Pahlavi z'hl, Manichaean zhr) < Old Iranian *ǰaθra- 'means of killing' < PIE *gʷhn̥-tro-, a tro-instrument noun on the zero grade of this root, matching Skt. *hatra-. Hübschmann established this in Persische Studien no. 679, expressly against Nöldeke's derivation from *zarta- 'yellow', and pointed out that NP زهره zahra 'gall' is a later derivative of zahr and not the other way round; MacKenzie's dictionary keeps the two apart as separate lemmas ('zahr … poison, venom' vs 'zahrag … bile, gall'). پادزهر pādzahr is pād- (< OP patiy 'against') + zahr, Hübschmann no. 273; the variants پازهر and پای‌زهر are ordinary Persian reductions, the last a folk re-etymologisation with پای 'foot'. The chart's own NOTE that KLN:168 derives zahr from Avestan 'zahr: bile' is accurate (Klein s.v. bezoar: 'The second element is rel. to Pers. zehre, \\\"gall, bile\\\", Pahlavi zahr, \\\"poison\\\", Avestic zara-, \\\"gall, bile\\\", and cogn. with Gk. χολή'), and on this point modern scholarship sides with Nourai, not with Klein: Watkins/AHD, Etymonline and Hübschmann all put zahr under *gʷhen-.\",\n \"derivation_fa\": \"«زهر» از فارسی میانهٔ zahr (پهلوی کتابی z'hl، مانوی zhr) از ایرانی باستان *ǰaθra- «ابزار کشتن» از *gʷhn̥-tro- هندواروپایی است؛ یعنی اسم ابزارِ پسونددارِ -tro بر درجهٔ صفر همین ریشه، هم‌ساخت با *hatra- سنسکریت. هوبشمان این را در بند ۶۷۹ «پژوهش‌های فارسی» به‌صراحت در برابر نظر نولدکه (که آن را از *zarta- «زرد» می‌گرفت) نشان داد و افزود که «زهره» به معنی صفرا مشتق پسینِ «زهر» است نه برعکس؛ مکنزی نیز در فرهنگ پهلوی دو مدخل جدا دارد: zahr «زهر» و zahrag «زهره، صفرا». «پادزهر» از pād- (< patiy پارسی باستان «در برابر») + zahr است (هوبشمان بند ۲۷۳)؛ «پازهر» کوتاه‌شدهٔ آن و «پای‌زهر» ریشه‌شناسی عامیانه با «پای» است. یادداشت خودِ کتاب دربارهٔ کلاین (ص۱۶۸) درست نقل شده است — کلاین ذیل bezoar زهر را به «زهرهٔ» صفرا و χολή یونانی می‌بندد — اما در این نکته پژوهش امروزی جانب نورایی را می‌گیرد نه کلاین: واتکینز، اتیمانلاین و هوبشمان همگی zahr را ذیل *gʷhen- می‌آورند.\",\n \"sources\": [ZAHR, E + \"bezoar\"],\n \"ref_check\": [{\"ref\": \"BQT:1047\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 510 (printed p. 1047; the offset leaf+537 is confirmed by زدن landing on Nourai's p. 1007). Mo'in's footnote to زهر: «پهلوی zahr … از ایرانی باستان *ǰaθra- از ǰan (زدن، کشتن) … نیبرگ … کردی zahr … افغانی، بلوچی zahr». Exactly Nourai's arrow. The following page carries پادزهر / بادزهره with the cross-reference.\"}],\n \"consulted\": [\n  {\"src\": \"HUB\", \"where\": \"Persische Studien nos. 679 and 273\", \"stance\": \"supports\", \"note\": \"no. 679: 'Ich führe daher zahr \\\"Gift\\\" … auf *jaθra- = skr. *hatra- \\\"Mittel zum Tödten\\\" zurück und leite zahra \\\"Galle\\\" … mittelst des Suffixes a … davon ab'; no. 273: pādzahr's pād 'liegt noch vor in np. paz. pādzahr \\\"Gegengift\\\"' from OP patiy.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. zahr and zahrag\", \"stance\": \"supports\", \"note\": \"'zahr [z'hl | M zhr, N زهر] poison, venom.' and separately 'zahrag [zʾhlk | N زهره] bile, gall.' — the two are distinct lemmas, which is the formal argument against Klein's 'bile' etymology.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷhen-¹, section 4\", \"stance\": \"supports\", \"note\": \"'4. Suffixed zero-grade form *gʷhn̥-tro- in Persian zahr, poison: BEZOAR.'\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. bezoar (KLN_1966.txt leaf 100, printed p. ~168)\", \"stance\": \"contradicts\", \"note\": \"'The second element is rel. to Pers. zehre, \\\"gall, bile\\\", Pahlavi zahr, \\\"poison\\\", Avestic zara-, \\\"gall, bile\\\", and cogn. with Gk. χολή, \\\"gall, bile\\\". See choler.' This is the KLN:168 of the chart's NOTE — correctly cited, but superseded.\"}\n ]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Arabic\", \"words\": \"bâdzahr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic بادزهر bādizahr / bāzahr is a straight loan of Persian pādzahr; Arabic has no p, so p- is rendered b-, and the compound is not analysable in Arabic (it belongs to no triliteral root), which is itself the proof of borrowing. Asbaghi, Persische Lehnwörter im Arabischen, lists it as such: 'bādzahr: \\\"Bezoarstein\\\", aus dem pers. پادزهر pādzahr, mp. pātzahr, pāt \\\"gegen, anti\\\" + zahr \\\"Gift\\\"', with the by-form bāzahr cross-referenced to it. Addi Shir's Kitāb al-alfāẓ al-fārisiyya al-muʿarraba likewise has بادزهر among the Persianisms. The word travels with the drug trade of the Islamic pharmacopoeia (Ibn Sīnā, al-Bīrūnī), which is how it reaches the Latin West.\",\n \"derivation_fa\": \"«بادزهر / بازهر» عربی وام‌واژه‌ای است یکراست از «پادزهر» فارسی؛ چون در عربی p نیست، پ به ب بدل شده و ترکیب در عربی تحلیل‌ناپذیر است (به هیچ ریشهٔ سه‌حرفی نمی‌خورد) و همین خود دلیل معرّب بودن است. اصغری در «وام‌واژه‌های فارسی در عربی» می‌نویسد: «bādzahr: «سنگ پادزهر»، از پادزهرِ فارسی، فارسی میانه pātzahr، از pāt «در برابر» + zahr «زهر»»، و صورت bāzahr را به همان ارجاع می‌دهد. ادّی شیر نیز در «الالفاظ الفارسیة المعرّبة» بادزهر را در شمار معرّبات آورده است. واژه با داروشناسی اسلامی (ابن‌سینا، بیرونی) به مغرب‌زمین می‌رسد. ادعای نورایی درست است.\",\n \"sources\": [E + \"bezoar\"],\n \"ref_check\": [{\"ref\": \"FVF:50\", \"status\": \"not_checked\", \"note\": \"FVF = Emam Shushtari, Farhang-e Vāžehā-ye Fārsi dar Zabān-e ʿArabi; refs_online.json marks it kind 'website' with no local file and only a noorlib scan-page hint, and it could not be opened in this session.\"}],\n \"consulted\": [\n  {\"src\": \"PLA\", \"where\": \"Asbaghi 1988, s.v. bādzahr (PLA djvu lines 3462-3465, 3695)\", \"stance\": \"supports\", \"note\": \"'bādzahr: \\\"Bezoarstein\\\" … aus dem pers. پادزهر pādzahr, mp. pātzahr, m. pāt \\\"gegen, anti\\\" + zahr \\\"Gift\\\", frz. bezoard'; and 'bāzahr = bādzahr s. bādzahr.'\"},\n  {\"src\": \"AFM\", \"where\": \"Addi Shir, AFM_pages.txt line 4156\", \"stance\": \"supports\", \"note\": \"بادزهر appears as a headword in the list of Persian words Arabised.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. bezoar\", \"stance\": \"supports\", \"note\": \"'fr. Arab. bādizahr, often shortened into bāzahr (see Freytag, Lexicon Arabico-Latinum, I, 79a and b), ult. fr. Pers. bādzahr, pādzahr, \\\"counterpoison, bezoar stone\\\", lit. \\\"protecting (against) poison\\\".'\"}\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"English\", \"words\": \"bezoar\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic bāzahr, in the Maghribi pronunciation with imāla (a > e) bezahr, was taken over by the medical Latin of the physicians who learned their trade from the western Arabs as bezoar; thence Spanish/Portuguese/Catalan bezoar, French bézoard, Italian bezzoar, and English bezoar, first recorded in the 1540s in the original sense 'stone used as an antidote against poison'. The now-familiar sense, the concretion found in the stomach of ruminants (especially the wild goat of the Persian province of Lār), is a later transfer of the name of the drug to its source, attested from the 1570s. Lokotsch's entry 1605 gives this chain in full, and Watkins files BEZOAR under gʷhen-¹, so the whole line from PIE 'strike' to an English noun is unbroken.\",\n \"derivation_fa\": \"«بازهر» عربی، در تلفظ مغربی با اماله bezahr، در لاتینِ پزشکیِ اطبایی که فن خود را از عرب‌های غرب آموخته بودند به‌صورت bezoar درآمد؛ از آنجا اسپانیایی و پرتغالی و کاتالان bezoar، فرانسه bézoard، ایتالیایی bezzoar و انگلیسی bezoar که نخستین‌بار در دههٔ ۱۵۴۰ به همان معنی نخستین «سنگی که پادزهر است» ثبت شده. معنی امروزی، یعنی سنگی که در معدهٔ نشخوارکنندگان (به‌ویژه بز کوهی ولایت لار) پیدا می‌شود، انتقال پسینِ نام دارو به منبع آن است و از دههٔ ۱۵۷۰ گواهی دارد. لوکوچ در بند ۱۶۰۵ همین زنجیره را کامل می‌آورد و واتکینز نیز BEZOAR را ذیل gʷhen-¹ می‌گذارد؛ پس رشتهٔ پیوستهٔ «زدن» هندواروپایی تا واژه‌ای انگلیسی ناگسسته است. ادعای نورایی درست است.\",\n \"sources\": [E + \"bezoar\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. gʷhen-¹: '4. Suffixed zero-grade form *gʷhn̥-tro- in Persian zahr, poison: BEZOAR.' The small-cap headword BEZOAR is the English reflex Watkins hangs on this root, exactly as the chart does.\"}],\n \"consulted\": [\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1605 (LKT.txt line 3674 f.)\", \"stance\": \"supports\", \"note\": \"'160[5]. Pers. pādzähr: \\\"Gegengift, Bezoar\\\" … Hieraus ar. bādizahr, bāzahr und nach magribinischer Aussprache mit Imāla [a > e] bezahr, woraus die Ärzte des MA., die ihre Kunst den Westarabern verdankten, mlat. bezoar machten: sp. bezaar, sp. pg. kat. bezoar, frz. bézoar, it. bezzoar … engl. bezoar.'\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. bezoar, printed p. ~168\", \"stance\": \"supports\", \"note\": \"'F. bezoard, fr. Sp. bezoar (cp. Port. bezuar), fr. Arab. bādizahr, often shortened into bāzahr … ult. fr. Pers. bādzahr, pādzahr.'\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, entry زهر\", \"stance\": \"supports\", \"note\": \"«واژهٔ انگلیسی BEZOAR (فرانسه bézoard، پرتغالی bezuar، اسپانیایی bezoar، عربی بادزهر) نیز از واژهٔ فارسی پادزهر گرفته شده است (SKEAT: 58-59)».\"}\n ]\n})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Germanic\", \"words\": \"guthjô : war\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The Germanic word for 'battle' from this root is *gunþjō (Pokorny) or *gundjō (Watkins), with a nasal: OE gūþ, Old Saxon gūðea, Old Norse gunnr/guðr, OHG gund- in gundfano 'war-banner'. The -n- is not decorative: the form is *gʷhn̥-tyeh₂, the zero grade of the root with a *-tyā- suffix, and Pokorny equates it with Sanskrit hatyā 'killing' ('ags. gūþ (*gunþjō = ai. hatyā bis auf den Akzent)'). *guþjō with no nasal would not be derivable from *gʷhen- at all. The printed page (checked at 600 dpi) reads 'guthjô', so the JSON is faithful and the error is the book's: Nourai has dropped the n while copying the reconstruction out of the 1976 AHD appendix, where it stands as Germanic *gundjō. Everything else in the node — the Germanic language label, the gloss 'war', and the attachment to gʷhen- — is correct.\",\n \"derivation_fa\": \"صورت ژرمنی این ریشه به معنی «نبرد» *gunþjō (پوکورنی) یا *gundjō (واتکینز) است، با نون: انگلیسی کهن gūþ، ساکسون کهن gūðea، نورس کهن gunnr/guðr، آلمانی علیای کهن gund- در gundfano «درفش جنگ». آن n زینتی نیست: صورت اصلی *gʷhn̥-tyeh₂ است، یعنی درجهٔ صفر ریشه با پسوند *-tyā-، و پوکورنی آن را با hatyā سنسکریت «کشتار» برابر می‌نهد («ags. gūþ (*gunþjō = ai. hatyā»). صورت *guþjō بی‌نون اصلاً از *gʷhen- به دست نمی‌آید. تصویر صفحهٔ چاپی (با تفکیک ۶۰۰ نقطه بررسی شد) «guthjô» را نشان می‌دهد؛ پس خطای خوانش اسکن نیست، خطای چاپی خودِ کتاب است: نورایی هنگام رونویسی از پیوست AHD ۱۹۷۶ (که *gundjō دارد) نون را انداخته است. باقی گره — برچسب «ژرمنی»، معنی «جنگ» و پیوند با gʷhen- — درست است.\",\n \"error_in\": \"book\",\n \"book_prints\": \"guthjô\",\n \"correct_form\": \"gunthjô (PGmc *gunþjō / *gundjō)\",\n \"sources\": [PIE, E + \"gun\"],\n \"ref_check\": [{\"ref\": \"AHD:1520\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. gʷhen-¹: '2. Suffixed zero-grade form *gʷhn̥-tyā- in Germanic *gundjō, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanōn-, \\\"battle flag\\\" …: GONFALON.' The reference has the word, but with the nasal that the book's 'guthjô' lacks.\"}],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 492\", \"stance\": \"partial\", \"note\": \"'anord. guðr, gunnr f. (= ai. hati-), as. gūðea, ags. gūþ (*gunþjō = ai. hatyā bis auf den Akzent) \\\"Kampf, Schlacht\\\", ahd. gund-fano \\\"Kriegsfahne\\\"' — the reconstruction is *gunþjō.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. gonfanon and s.v. Edith\", \"stance\": \"partial\", \"note\": \"'OE. gūð is rel. to OHG. gund-, ON. gunnr, guðr, \\\"war\\\", and cogn. with Gk. θείνειν, \\\"to strike\\\", φόνος, \\\"murder\\\", L. -fendere' — again with the nasal throughout.\"}\n ]\n})\n\nnodes.append({\n \"id\": 18, \"lang\": \"English\", \"words\": \"gun\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The root connection is right but the chart's arrow is too short. English gun is not the direct phonetic descendant of a Germanic common noun: it is ME gunne, gonne (mid-14c.), an abbreviation of the woman's name Gunilda, which was applied to an engine of war — the Anglo-Latin munitions inventory of Windsor Castle of 1330 records 'una magna balista de cornu quae Domina Gunilda', and ME gonnilde 'cannon' and gonnilde gnoste 'touch-powder' are attested beside it. Gunilda is Old Norse Gunnhildr, a compound of gunnr and hildr, both meaning 'war, battle'; gunnr is the Old Norse reflex of the Germanic *gundjō/*gunþjō of node 17, so the ultimate source is indeed this root. Klein and Etymonline agree on this route; Watkins compresses it in the same way Nourai does ('Old Norse gunnr, war: GUN'), which is presumably where the chart's arrow comes from.\",\n \"derivation_fa\": \"پیوند ریشه‌ای درست است اما پیکان چارت کوتاه بریده شده. واژهٔ انگلیسی gun بازماندهٔ آواییِ مستقیم یک اسم عام ژرمنی نیست: صورت انگلیسی میانهٔ gunne/gonne (میانهٔ سدهٔ ۱۴) کوتاه‌شدهٔ نام زنانهٔ Gunilda است که بر منجنیقی نهاده شده بود — سیاههٔ سلاح‌های قلعهٔ ویندزور به سال ۱۳۳۰ از «una magna balista de cornu quae Domina Gunilda» یاد می‌کند، و در کنار آن gonnilde «توپ» و gonnilde gnoste «باروتِ آتش‌زنه» نیز گواهی دارد. Gunilda همان Gunnhildr نورس کهن است، مرکب از gunnr و hildr که هر دو «جنگ» معنی می‌دهند؛ و gunnr بازتاب نورسیِ همان *gundjō/*gunþjō ژرمنی گرهٔ ۱۷ است. پس سرچشمهٔ نهایی به‌راستی همین ریشه است. کلاین و اتیمانلاین بر همین راه هم‌داستان‌اند؛ واتکینز نیز آن را به همان کوتاهیِ نورایی می‌نویسد («نورس کهن gunnr «جنگ»: GUN») و پیکان چارت لابد از همان‌جا آمده است. حکم: با احتیاط پذیرفتنی، چون واسطهٔ نام خاص از قلم افتاده است.\",\n \"sources\": [E + \"gun\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Although the node carries no refs in the JSON, its parent's AHD:1520 covers it: 'Suffixed zero-grade form *gʷhn̥-tyā- in Germanic *gundjō, war, battle, in: a. Old Norse gunnr, war: GUN.' Watkins does list GUN under this root.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. gun (KLN_1966.txt line 16875)\", \"stance\": \"partial\", \"note\": \"'gun, n. — ME. gunne, gonne, prob. from the fem. PN. Gunne, shortened from the name Gunhild, which was applied to a war engine (in 1330). For sense development cp. the gun names Mons Meg, Big Bertha, etc.' — same root, but via a personal name.\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat, 'GUN.' at SKT.txt line 8119\", \"stance\": \"silent\", \"note\": \"The OCR of the concise Skeat breaks off after the headword 'GUN.' and the body of the entry is lost in the scan, so no reading could be taken.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷhen-¹\", \"stance\": \"supports\", \"note\": \"See ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 19, \"lang\": \"Latin\", \"words\": \"fendere, off-endere, de-fendere : to strike off, attack\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin -fendere 'to strike, thrust' exists only in compounds — dēfendere 'to ward off, defend', offendere 'to strike against, offend', īnfēnsus 'hostile' (participle of a lost *īnfendō) — and Pokorny prints all three in his gʷhen- article on p. 492: 'lat. defendō, -ere \\\"abwehren, verteidigen\\\", offendere \\\"anstoßen, beleidigen\\\", infensus (Partiz. eines *infendō) \\\"feindlich\\\"'. Formally it is a dhe-present, PIE *gʷhén-dʰe-ti, with the regular Italic *gʷh > f- word-initially and the *-dh- suffix showing up as -d-; Wiktionary reconstructs Proto-Italic *fendō for the same set. Kent quotes 'Lt. dē-fendit \\\"wards off\\\"' as the Latin cognate of Old Persian jan-, which puts the Latin and the Iranian branches of this chart side by side in one authority. Nourai's simple stem 'fendere' is a conventional citation form for the bound verb; his gloss 'to strike off, attack' fits offendere better than defendere but is not wrong.\",\n \"derivation_fa\": \"فعل لاتینی -fendere «زدن، کوفتن» تنها در ترکیب دیده می‌شود: dēfendere «دور کردن، دفاع کردن»، offendere «برخوردن، آزردن»، īnfēnsus «دشمن‌خو» (صفت مفعولی *īnfendō از میان رفته). پوکورنی هر سه را در همان مدخل gʷhen- صفحهٔ ۴۹۲ می‌آورد: «لاتین defendō, -ere «دور کردن، دفاع کردن»، offendere «برخوردن، آزردن»، infensus (صفت *infendō) «دشمنانه»». از نظر ساخت، این یک ستاک حالِ dhe-دار است، *gʷhén-dʰe-ti هندواروپایی، که در ایتالیک *gʷh در آغاز واژه f می‌شود و پسوند *-dh- به -d- بدل می‌گردد؛ ویکی‌واژه نیز *fendō ایتالیک آغازین را برای همین دسته بازسازی می‌کند. کنت «لاتین dē-fendit» را هم‌ریشهٔ jan- پارسی باستان می‌آورد و بدین‌سان دو شاخهٔ لاتینی و ایرانی این چارت را در یک مرجع کنار هم می‌گذارد. صورت «fendere» در چارت شکل استنادی مرسوم برای فعل مقیّد است. ادعای نورایی درست است.\",\n \"sources\": [E + \"defend\", PIE],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. gʷhen-¹: '3. Suffixed form *gʷhen-do- in: a. Latin dēfendere, to ward off (dē-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offendere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE).'\"}],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 492\", \"stance\": \"supports\", \"note\": \"'lat. defendō, -ere \\\"abwehren, verteidigen\\\", offendere \\\"anstoßen, beleidigen\\\", infensus (Partiz. eines *infendō) \\\"feindlich\\\".'\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. defend\", \"stance\": \"supports\", \"note\": \"'fr. L. defendere, \\\"to ward off, keep away, defend, guard, protect\\\", fr. de- and -fendere (found only in compounds), \\\"to thrust, strike\\\", fr. I.-E. base *gʷhen-, \\\"to strike\\\", whence also OI. hánti … Hitt. kuenzi …'\"},\n  {\"src\": \"KNT\", \"where\": \"Lexicon p. 184 s.v. jan-\", \"stance\": \"supports\", \"note\": \"'Lt. dē-fendit \\\"wards off\\\", pIE *gʷhen-' cited as the Latin member of the same root as OP jan-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 20, \"lang\": \"English\", \"words\": \"fender, fence, offense, defense\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are Latin -fendere words that reached English through Old French. defense < OF defense < Vulgar Latin *dēfēnsa, feminine past participle of dēfendere used as a noun; offense < OF offense < L. offēnsa, likewise. fence and fender are the two aphetic English shortenings of that pair: fence is recorded from the early 14c. as 'action of defending, resistance; means of protection', a clipped defens, and only takes on the sense 'enclosure' in the mid-15c. 'on notion of that which serves as a defense'; fender is a clipping of defender (late 13c.), first the mat or timber hung over a ship's side to protect the hull at a wharf, then the fireplace guard (1680s), then the car body-panel (1919). Watkins lists DEFEND, DEFENSE, FENCE, OFFEND, OFFENSE together under gʷhen-¹, so all four words are the same root at one remove; fender belongs with them through defender.\",\n \"derivation_fa\": \"هر چهار واژه از فعل لاتینی -fendere و از راه فرانسهٔ کهن به انگلیسی رسیده‌اند. defense از OF defense از لاتین عامیانهٔ *dēfēnsa، صفت مفعولی مؤنث dēfendere که اسم شده؛ offense نیز از OF offense از L. offēnsa. «fence» و «fender» دو صورت سرکوتاه‌شدهٔ (aphetic) همان جفت‌اند: fence از آغاز سدهٔ ۱۴ به معنی «دفاع، پایداری، وسیلهٔ حفاظت» گواهی دارد، یعنی دقیقاً defens با افتادن هجای نخست، و تنها در میانهٔ سدهٔ ۱۵ معنی «پرچین، حصار» می‌گیرد «بر پایهٔ مفهوم آنچه دفاع می‌کند». fender نیز کوتاه‌شدهٔ defender است (اواخر سدهٔ ۱۳)، نخست به معنی حائلی که از پهلوی کشتی می‌آویختند تا بدنه در بارانداز آسیب نبیند، سپس حفاظ بخاری (دههٔ ۱۶۸۰) و سرانجام گلگیر خودرو (۱۹۱۹). واتکینز DEFEND، DEFENSE، FENCE، OFFEND و OFFENSE را یکجا ذیل gʷhen-¹ می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [E + \"fence\", E + \"fender\", E + \"defend\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Node 19's AHD citation covers this node too: 'Latin dēfendere … DEFEND, (DEFENSE), (FENCE); b. Latin offendere … OFFEND, (OFFENSE).' The index page of AHD_watkins1985.txt confirms 'DEFEND gʷhen-1 DEFENSE gʷhen-1' and 'OFFEND gʷhen-1 OFFENSE gʷhen-1'.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. fence and s.v. defend\", \"stance\": \"supports\", \"note\": \"'fence, n. — ME. defense, defence, fr. OF. defense (F. défense), fr. VL. defensa … prop. fem. pp. of L. defendere, used as a noun', and 'fence, n. — The British spelling of defense.'\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷhen-¹ and the English index\", \"stance\": \"supports\", \"note\": \"See ref_check.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Gwhen 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *gʷhen- 'to strike, slay, kill' (Pokorny IEW 491-493, '2. gʷhen-(ə)- schlagen'; Watkins/AHD gʷhen-¹; LIV 218 f.)\",\n \"note\": \"The root box is right in every particular, including the number. Pokorny has two homophonous entries: '1. gʷhen- \\\"schwellen, strotzen, Fülle\\\"' (IEW 491, the root of NP āgandan) and '2. gʷhen-(ə)- \\\"schlagen\\\"' (IEW 491-493), and Nourai's 'Gwhen 2' reproduces Pokorny's own numbering, with POK:492 falling inside the second article. The language label 'Indo-European' and the gloss 'to strike, hurt' are accurate; Wiktionary heads the root '*gʷʰen- to strike, slay, kill', Watkins 'gʷhen-¹. To strike, kill', Mann 'gʷhen- radical of general sense: drive, beat, kill'. The Iranian, Latin and Germanic branches of the page are all present in Pokorny's own article on p. 492, and Kent's Old Persian lexicon entry for jan- (pp. 184-185, which Nourai cites four times) equates the Old Persian, Avestan, Sanskrit, Greek and Latin material in one line. Three things on the page do not belong to the root: Avestan 'gaz, gaš' and Persian gazīdan (node 1/2), which Cheung shows to be an exclusively Iranian root *gaz with no IE etymology; the resin words jatara / žad / angžeh (nodes 12-13), which Bartholomae himself refers to Skt. jātu- and hence to Pokorny's separate root gʷet- 'Harz' (IEW 480); and kalāγ 'crow' (node 10), which modern Iranian etymology treats as onomatopoeic. Two forms are misprints of the book itself: 'varathra-ğam' for varathra-ğna (node 1) and 'guthjô' for gunthjô (node 17). Against that, the zahr → pādzahr → Arabic bādzahr → English bezoar line is one of the best-supported chains on the whole page, endorsed by Hübschmann, Watkins, Etymonline, Lokotsch and Asbaghi alike, and the chart is right and Klein (cited in its own NOTE) is wrong about it.\",\n \"note_fa\": \"جعبهٔ ریشه از هر نظر درست است، حتی در شماره. پوکورنی دو مدخل هم‌آوا دارد: «۱. gʷhen- «آماسیدن، پر بودن»» (ص۴۹۱، ریشهٔ «آگندن» فارسی) و «۲. gʷhen-(ə)- «زدن»» (صص۴۹۱–۴۹۳)؛ و نام «Gwhen 2» نورایی همان شماره‌گذاری پوکورنی است و ارجاع POK:492 درون مدخل دوم می‌افتد. برچسب «هندواروپایی» و معنای «زدن، آسیب رساندن» درست است؛ ویکی‌واژه سرمدخل را «*gʷʰen- زدن، کشتن»، واتکینز «gʷhen-¹ زدن، کشتن» و مان «gʷhen- به معنی کلیِ راندن، زدن، کشتن» آورده‌اند. هر سه شاخهٔ ایرانی و لاتینی و ژرمنیِ این صفحه در همان مدخل پوکورنی در ص۴۹۲ حاضرند، و مدخل jan- در واژه‌نامهٔ پارسی باستانِ کنت (صص۱۸۴–۱۸۵ که نورایی چهار بار به آن ارجاع می‌دهد) صورت‌های پارسی باستان، اوستایی، سنسکریت، یونانی و لاتین را در یک سطر برابر می‌نهد. سه چیز در این صفحه به این ریشه تعلق ندارد: «gaz, gaš» اوستایی و «گزیدن» فارسی (گره‌های ۱ و ۲) که چونگ آن را ریشهٔ منحصراً ایرانی *gaz بی هیچ اشتقاق هندواروپایی می‌داند؛ واژه‌های صمغ یعنی jatara و ژد و انگژه (گره‌های ۱۲ و ۱۳) که خودِ بارتولمه آنها را به jātu- سنسکریت و در نتیجه به ریشهٔ جداگانهٔ gʷet- «صمغ» (پوکورنی ۴۸۰) بازمی‌گرداند؛ و «کلاغ» (گرهٔ ۱۰) که ریشه‌شناسی امروزی آن را نام‌آوا می‌شمارد. دو صورت هم غلط چاپی خودِ کتاب است: «varathra-ğam» به‌جای varathra-ğna و «guthjô» به‌جای gunthjô. در برابر اینها، زنجیرهٔ زهر ← پادزهر ← بادزهرِ عربی ← bezoar انگلیسی یکی از مستندترین رشته‌های کل صفحه است که هوبشمان و واتکینز و اتیمانلاین و لوکوچ و اصغری همگی آن را تأیید می‌کنند؛ و در این نکته حق با نورایی است نه با کلاین که خودِ چارت در یادداشتش از او یاد کرده است.\",\n \"sources\": [PIE],\n \"ref_check\": [{\"ref\": \"POK:492\", \"status\": \"supports\", \"note\": \"POK_02.txt: the entry '2. gʷhen-(ə)- ,schlagen'. Nominalbildungen: gʷhóno-s ,Schlagen', gʷhn̥-to-s ,geschlagen', gʷhn̥-ti-s und gʷhn̥-tiā (?) ,Schlagen', gʷhen-tel- ,Schläger', gʷhen-tuo-s ,occidendus'' opens at the foot of leaf 148 (printed p. 491) and runs across leaves 149-150 (pp. 492-493). Page 492 carries the Indo-Iranian, Armenian, Greek, Albanian, Latin, Celtic and Germanic material Nourai draws on; the article closes 'WP. I 679 ff., WH. I 332 f., Trautmann 85 f.'\"}],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 679-681 (WLD_Bd1_pages.txt leaf 688)\", \"stance\": \"supports\", \"note\": \"'2. gʷhen- \\\"schlagen\\\", auch als set-Basis gʷheneə-' — printed on the same page (679) that carries '1. gʷhen- \\\"schwellen, strotzen, Fülle\\\"', i.e. Pokorny's two-entry arrangement goes back to Walde-Pokorny.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷhen-¹\", \"stance\": \"supports\", \"note\": \"'gʷhen-¹. To strike, kill. 1. O-grade *gʷhon- in Germanic suffixed form *ban-ōn- … BANE … AUTOBAHN. 2. Suffixed zero-grade form *gʷhn̥-tyā- in Germanic *gundjō, war, battle … GUN … GONFALON. 3. Suffixed form *gʷhen-do- in Latin dēfendere … offendere … 4. Suffixed zero-grade form *gʷhn̥-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gʷhen-(ə)- 491, bhen- 126.]' — three of Nourai's four sub-branches, in the same order.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. gʷhen-\", \"stance\": \"supports\", \"note\": \"'gʷhen- radical of general sense: \\\"drive, beat, kill\\\". WP I, 679 … Skt. hánmi: Av. jainmi; OPer. -janam; Per. zanam, inf. zadan; Arm. jnem …; Hitt. kwemi …; Gk. (thematic) théno.'\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *jan, PIE line\", \"stance\": \"supports\", \"note\": \"'This root has impeccable IE credentials. «PIE *gʷhen- \\\"to slay, kill\\\" > LIV: 218 f. | Pok.: 491 ff.»'\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 215,\n \"book_page\": 185,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [entry]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-215.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/gen215.py",
 "description": "Generate page-215.json"
}
```


### [2026-09-06T15:19:55.505Z] TOOL RESULT

```
ok 20
```


## [2026-09-06T15:20:00.571Z] TOOL CALL #104: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-215.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 215",
 "description": "Validate and run verify_check"
}
```


### [2026-09-06T15:20:02.529Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'disputed': 5, 'confirmed': 10, 'plausible': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 24, 'partial': 6, 'not_checked': 4, 'not_found': 2}
books consulted: {'supports': 38, 'partial': 8, 'silent': 7, 'contradicts': 5} | by book: {'CHEUNG': 7, 'KLN': 7, 'BRT': 6, 'POK': 5, 'PHD': 5, 'BQT': 4, 'KNT': 3, 'SOD': 3, 'AHD': 3, 'NYB': 2, 'HUB': 2, 'ARY': 2, 'IEC': 1, 'FFD': 1, 'HRN': 1, 'ISS_alt_DKS': 1, 'MON': 1, 'PLA': 1, 'AFM': 1, 'LKT': 1, 'SKT': 1}
```


## [2026-09-06T15:20:23.365Z] AGENT

Done. `verify_check.py 215` reports **0 PROBLEM lines**, 20/20 nodes.

**Page 215 (book p. 185) — root Gwhen 2 (PIE \*gʷhen- "to strike, kill"), 1 entry, 20 nodes**

- Root: **confirmed** — Nourai's "Gwhen 2" reproduces Pokorny's own numbering (IEW 491: *1. gʷhen-* "swell" vs *2. gʷhen-(ə)-* "strike", 491–493); POK:492 lands inside the right article.
- Node verdicts: 10 confirmed, 4 plausible, 5 disputed, 1 transcription_suspect. Ref checks: 24 supports / 6 partial / 2 not_found / 4 not_checked. 21 different books consulted.

Disputed / flagged:
- **#1 Avestan "gaz, gaš"** — not Avestan and not from this root; Cheung s.v. *\*gaz* calls it "exclusively Iranian", PIE/LIV/Pokorny slots empty.
- **#2 Persian gazîdan / gaštan** — same problem; only *gazand* belongs here, and via *vi-jan* (Cheung; Mo'in's Borhan footnote p. 1812), not via gazīdan.
- **#10 kalâğ "crow"** — Mo'in's Borhan footnote (p. 1669) does derive it from Av. *vārəγna*, so Nourai is following his source, but Wiktionary/modern Iranian etymology treat it as onomatopoeic (or \*ḱer-). ورغنه could not be found in any local dictionary.
- **#12 "jatara: resin"** — Bartholomae (s.v. \*yahmya-jatara-) ties it to Skt. *jātu-*, i.e. Pokorny's separate root *gʷet-* "Harz" (IEW 480), not *gʷhen-*. The chart's own hedge understates it.
- **#13 žad / angžeh** — correct Persian data (Borhan p. 175, p. 1058) but hanging off the wrong parent, same reason.
- **#17 Germanic "guthjô"** — transcription_suspect; should be *gunthjô* (Pok. \*gunþjō, Watkins \*gundjō).

Book misprints (extraction is faithful — checked the printed page at 600 dpi, PNG saved to `data/verification/sources/refs/ocr/BOOK/215.png`): **"varathra-ğam"** for *varathra-ğna* (#1) and **"guthjô"** for *gunthjô* (#17). **No extraction errors found** — the JSON matches the printed page everywhere.

Notable positives: KNT:184–185 supports nodes 3/6/11 verbatim; POK:1170 gives *vārəγna-* as "Lämmerschläger" exactly as charted; FFD:25 gives \*ā-ǰa-ta- for âzdan; and the zahr → pâdzahr → Ar. bâdzahr → Eng. bezoar chain is confirmed by Hübschmann §679/§273, Watkins, Etymonline, Lokotsch 1605 and Asbaghi — the chart's own NOTE citing KLN:168 (bile) is correctly quoted but Klein is the one who is wrong.

Two bad citations by Nourai: **HRN:231** on node 11 (that page is *nižand*, not pati-/fra-/vi-jan) and **BQT:1776** on node 13 (p. 1776 is in the گ section; the ژد article is at p. 1058).
