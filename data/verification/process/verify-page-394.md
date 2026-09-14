# Verification process log — verify-page-394


## [2026-09-14T00:49:41.207Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 394 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-394.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-394.json. Write /home/sfmqrb/git/rishe/data/verification/page-394.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 394` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:49:42.484Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:49:43.379Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:49:43.393Z] TOOL RESULT

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


## [2026-09-14T00:49:43.952Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-394.txt"
}
```


### [2026-09-14T00:49:43.970Z] TOOL RESULT

```
1	=== PDF page 394 (book page 364) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Per 1 : around, forward. Also see roots "Per 2", "Per 3" and "Per 4".  (refs POK:810)  PART 2
4	#1 (parent #0) [Old Persian] refs=POK:813; KNT:198,200 | fra : forward ; frava, fravata : forward, downward ; fra-bar : offer, grant ☞Bher 1
5	  #2 (parent #1) [Pahlavi] refs=KNT:198 | frôt : downward
6	    #3 (parent #2) [Persian] refs=KNT:198; BQT:1473; HRN:183 | forŭ «فرو» : down ; forŭtan «فروتن» : down to earth | extra: فرود
7	#4 (parent #0) [Avestan] refs=POK:810,813,815; HRN:61; AEF:376 | paurva, parô, para 4, parâ 4 : former, earlier ; parô-ayare : last day ☞Ayer
8	  #5 (parent #4) [Persian] refs=BQT:349,397; AEF:331,368,376; ZMA:55 |  | extra: پار ، پارسال ، پارینه ، پَرَن ، پَرَندوش ، پَریر ، پریروز ، پیرار ، پیرارسال
9	#6 (parent #0) [Old Persian] refs=KNT:195,196 | paruva : early ; pariy : around ; para : later, beyond ; parâ : along
10	#7 (parent #0) [Sanskrit] refs=POK:813 | pra-jan : with perception, one who understands beforehand ☞Gnô
11	  #8 (parent #7) [Pahlavi] refs=BQT | farzânak : smart
12	    #9 (parent #8) [Persian] refs=BQT:1459; HRN:181 | Farzâneh «فرزانه» | extra: فرزین
13	#10 (parent #0) [Germanic] refs=AHD | fer, fruma, furista
14	  #11 (parent #10) [English] refs=AHD | far, for, former, first
15	#12 (parent #0) [Latin] refs=AHD | per, pro : first, forward, along ; prô-tahere : to draw forward ; primo-capus : first in rank, prince ; para-meter : measure along
16	  #13 (parent #12) [French] refs=AHD | 
17	    #14 (parent #13) [Persian] refs=MON |  | extra: پارامتر ، پُرتره ، پرنسس
18	    #15 (parent #13) [English] refs=AHD | per, perimeter, parameter, portrait, prince
19	#16 (parent #0) [Greek] refs=AHD | proto- : first ; para : along with ; para-bolâre : to throw (talk) around ☞Gwel 1 ; proto-inin : of prime value ; proto-kolla : the first attached (page) ; para-sitos : (uninvited guest) along for food
20	  #17 (parent #16) [French] refs=AHD | 
21	    #18 (parent #17) [Persian] refs=MON |  | extra: پارازیت ، پروتکل ، پارلمان ، پروتئین
22	    #19 (parent #17) [English] refs=AHD | parasite, parallel, protein, parabola, parliament, protocol, paragraph
23	#20 (parent #0) [Indo-European] refs=POK:810,811; IEC:927 | Per-per-os : flighty, giddy
24	  #21 (parent #20) [Persian] refs=IEC:927; MON:2521 | farfar «فَرفَر» : in hurry
25	  #22 (parent #20) [Latin] refs=IEC:927; POK:811 | perperus : rashly
26	
```


## [2026-09-14T00:49:45.253Z] AGENT

I'll start by looking at the source JSON and the reference infrastructure.


## [2026-09-14T00:49:47.147Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-394.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:8000])\n\"",
 "description": "Dump source JSON for page 394"
}
```


## [2026-09-14T00:49:48.238Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat data/verification/sources/SOURCE_MATRIX.md | head -80",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-14T00:49:48.368Z] TOOL RESULT

```
{
 "pdf_page": 394,
 "book_page": 364,
 "entries": [
  {
   "part": 2,
   "root": {
    "name": "Per 1",
    "lang": "Indo-European",
    "refs": "POK:810",
    "gloss": "around, forward. Also see roots \"Per 2\", \"Per 3\" and \"Per 4\"."
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Old Persian",
     "refs": "POK:813; KNT:198,200",
     "words": [
      {
       "translit": "fra",
       "gloss": "forward",
       "script": null
      },
      {
       "translit": "frava, fravata",
       "gloss": "forward, downward",
       "script": null
      },
      {
       "translit": "fra-bar",
       "gloss": "offer, grant",
       "script": null,
       "see": [
        "Bher 1"
       ]
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Pahlavi",
     "refs": "KNT:198",
     "words": [
      {
       "translit": "frôt",
       "gloss": "downward",
       "script": null
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
     "refs": "KNT:198; BQT:1473; HRN:183",
     "words": [
      {
       "translit": "forŭ",
       "gloss": "down",
       "script": "فرو"
      },
      {
       "translit": "forŭtan",
       "gloss": "down to earth",
       "script": "فروتن"
      }
     ],
     "script_extra": "فرود",
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:810,813,815; HRN:61; AEF:376",
     "words": [
      {
       "translit": "paurva, parô, para 4, parâ 4",
       "gloss": "former, earlier",
       "script": null
      },
      {
       "translit": "parô-ayare",
       "gloss": "last day",
       "script": null,
       "see": [
        "Ayer"
       ]
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "Persian",
     "refs": "BQT:349,397; AEF:331,368,376; ZMA:55",
     "words": [],
     "script_extra": "پار ، پارسال ، پارینه ، پَرَن ، پَرَندوش ، پَریر ، پریروز ، پیرار ، پیرارسال",
     "note": null,
     "quote": {
      "text": "چنین داد پاسخ که بر کوه و دشت - سواری پرندوش بر من گذشت",
      "poet": "Ferdowsî"
     }
    },
    {
     "id": 6,
     "parent": 0,
     "lang": "Old Persian",
     "refs": "KNT:195,196",
     "words": [
      {
       "translit": "paruva",
       "gloss": "early",
       "script": null
      },
      {
       "translit": "pariy",
       "gloss": "around",
       "script": null
      },
      {
       "translit": "para",
       "gloss": "later, beyond",
       "script": null
      },
      {
       "translit": "parâ",
       "gloss": "along",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 0,
     "lang": "Sanskrit",
     "refs": "POK:813",
     "words": [
      {
       "translit": "pra-jan",
       "gloss": "with perception, one who understands beforehand",
       "script": null,
       "see": [
        "Gnô"
       ]
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 8,
     "parent": 7,
     "lang": "Pahlavi",
     "refs": "BQT",
     "words": [
      {
       "translit": "farzânak",
       "gloss": "smart",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 9,
     "parent": 8,
     "lang": "Persian",
     "refs": "BQT:1459; HRN:181",
     "words": [
      {
       "translit": "Farzâneh",
       "gloss": null,
       "script": "فرزانه"
      }
     ],
     "script_extra": "فرزین",
     "note": null,
     "quote": null
    },
    {
     "id": 10,
     "parent": 0,
     "lang": "Germanic",
     "refs": "AHD",
     "words": [
      {
       "translit": "fer, fruma, furista",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 11,
     "parent": 10,
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "far, for, former, first",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 12,
     "parent": 0,
     "lang": "Latin",
     "refs": "AHD",
     "words": [
      {
       "translit": "per, pro",
       "gloss": "first, forward, along",
       "script": null
      },
      {
       "translit": "prô-tahere",
       "gloss": "to draw forward",
       "script": null
      },
      {
       "translit": "primo-capus",
       "gloss": "first in rank, prince",
       "script": null
      },
      {
       "translit": "para-meter",
       "gloss": "measure along",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 13,
     "parent": 12,
     "lang": "French",
     "refs": "AHD",
     "words": [],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 14,
     "parent": 13,
     "lang": "Persian",
     "refs": "MON",
     "words": [],
     "script_extra": "پارامتر ، پُرتره ، پرنسس",
     "note": null,
     "quote": null
    },
    {
     "id": 15,
     "parent": 13,
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "per, perimeter, parameter, portrait, prince",
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
     "parent": 0,
     "lang": "Greek",
     "refs": "AHD",
     "words": [
      {
       "translit": "proto-",
       "gloss": "first",
       "script": null
      },
      {
       "translit": "para",
       "gloss": "along with",
       "script": null
      },
      {
       "translit": "para-bolâre",
       "gloss": "to throw (talk) around",
       "script": null,
       "see": [
        "Gwel 1"
       ]
      },
      {
       "translit": "proto-inin",
       "gloss": "of prime value",
       "script": null
      },
      {
       "translit": "proto-kolla",
       "gloss": "the first attached (page)",
       "script": null
      },
      {
       "translit": "para-sitos",
       "gloss": "(uninvited guest) along for food",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 17,
     "parent": 16,
     "lang": "French",
     "refs": "AHD",
     "words": [],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 18,
     "parent": 17,
     "lang": "Persian",
     "refs": "MON",
     "words": [],
     "script_extra": "پارازیت ، پروتکل ، پارلمان ، پروتئین",
     "note": null,
     "quote": null
    },
    {
     "id": 19,
     "parent": 17,
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "parasite, parallel, protein, parabola, parliament, protocol, paragraph",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 20,
     "parent": 0,
     "lang": "Indo-European",
     "refs": "POK:810,811; IEC:927",
     "words": [
      {
       "translit": "Per-per-os",
       "gloss": "flighty, giddy",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 21,
     "parent": 20,
     "lang": "Persian",
     "refs": "IEC:927; MON:2521",
     "words": [
      {
       "translit": "farfar",
       "gloss": "in hurry",
       "script": "فَرفَر"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": {
      "text": "برداشت کلک و کاغذ و فَرفَر نوشت - فی الفور این قصیدهٔ مطبوعِ آبدار",
      "poet": "Anvarî"
     }
    },
    {
     "id": 22,
     "par
```


### [2026-09-14T00:49:48.410Z] TOOL RESULT

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
----
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
```


## [2026-09-14T00:49:53.104Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-394.json'))\nprint(json.dumps(d['entries'][0]['nodes'][-1],ensure_ascii=False,indent=1))\nprint('n entries',len(d['entries']))\nprint(json.dumps(d.get('redirects'),ensure_ascii=False)[:500])\nprint(list(d.keys()))\n\"",
 "description": "Show last node and top-level keys"
}
```


### [2026-09-14T00:49:54.177Z] TOOL RESULT

```
{
 "id": 22,
 "parent": 20,
 "lang": "Latin",
 "refs": "IEC:927; POK:811",
 "words": [
  {
   "translit": "perperus",
   "gloss": "rashly",
   "script": null
  }
 ],
 "script_extra": null,
 "note": null,
 "quote": null
}
n entries 1
null
['pdf_page', 'book_page', 'entries']
```


## [2026-09-14T00:49:55.374Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nr=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','BQT','HRN','AEF','ZMA','IEC','MON','AHD','PHD','BRT','WLD','SYN','ARY','NYB','HUB']:\n    v=r.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400])\n    print()\n\"",
 "description": "Show ref metadata"
}
```


### [2026-09-14T00:49:56.481Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه

ZMA {"title": "Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian, Bonyad-e Neyshabur 1374/1995", "kind": "purchase", "url": "https://www.gisoom.com / iketab.com listings (Balkh / Bonyad-e Neyshabur, in print)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only; no open

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
```


## [2026-09-14T00:50:01.360Z] TOOL CALL #7: Bash

```json
{
 "command": "ls data/verification/ | grep -E 'page-39[0-9]' ; echo ----; ls data/verification/page-385.json && python3 -c \"\nimport json;d=json.load(open('data/verification/page-385.json'));e=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1))\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1))\n\"",
 "description": "Check neighboring pages and template"
}
```


## [2026-09-14T00:50:02.091Z] TOOL CALL #8: Bash

```json
{
 "command": "cat tools/verify_check.py | head -80",
 "description": "Read verify_check script"
}
```


### [2026-09-14T00:50:02.495Z] TOOL RESULT

```
----
data/verification/page-385.json
{
 "entry": 0,
 "root": "Peg",
 "verdict": "plausible",
 "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
 "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
 "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
  "https://en.wiktionary.org/wiki/pectus"
 ],
 "ref_check": [
  {
   "ref": "POK:792",
   "status": "partial",
   "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. peg-",
   "stance": "supports",
   "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."
  },
  {
   "src": "WLD",
   "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)",
   "stance": "partial",
   "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'breast'."
  },
  {
   "src": "IEC",
   "where": "Mann, alphabetical",
   "stance": "silent",
   "note": "grep of IEC.txt for 'peg-', 'pokso-', 'pektos' returns no headword for this root."
  }
 ]
}
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "pakša",
 "verdict": "plausible",
 "derivation": "Sanskrit पक्ष (pakṣá-) m. is real and old (RV), but its meanings are 'wing, feather; side, flank; half (of a month); party, faction' — not 'breast'. Monier-Williams and Wiktionary give no 'breast' sense; the chart's 'breast' is imported from Nourai's root gloss. Formally pakṣa- goes back to Proto-Indo-Iranian *pakšás 'side, flank' < PIE *peg-/*pok-s-, with the regular Indo-Aryan treatment of *-ks- > -kṣ-; the Iranian cognate is Ossetic fæxs 'side'. So the arrow root -> Sanskrit is sound; only the gloss 'breast' is wrong.",
 "derivation_fa": "واژهٔ سنسکریت pakṣá- «بال، پر؛ پهلو، سو؛ نیمه (ماه)؛ دسته» از ریگ‌ودا به‌بعد گواهی شده است، اما معنای «سینه» برای آن ثبت نشده و نورایی آن را از معنای ریشه به این گره تسری داده است. از دید آوایی pakṣá- بازماندهٔ هندوایرانی آغازین *pakšás «پهلو، سو» است (خوشهٔ *-ks- در هندوآریایی به -kṣ- بدل می‌شود) و هم‌ریشهٔ آن در ایرانی، fæxs آسی به معنی «پهلو» است. بنابراین پیکان «ریشه ← سنسکریت» درست است و تنها معنای «سینه» نادرست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7"
 ],
 "ref_check": [
  {
   "ref": "AHD",
   "status": "partial",
   "note": "Watkins 1985 s.v. peg-: '2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA.' Watkins glosses the Sanskrit word 'wing' only, and marks the connection 'possibly'."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "IEW 792 (POK_03 leaf 25)",
   "stance": "partial",
   "note": "'Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"' — shoulder/wing/side, not breast."
  },
  {
   "src": "KLN",
   "where": "1966 ed. p.1272 s.v. punka (leaf 678)",
   "stance": "partial",
   "note": "'fr. OI. pakṣaḥ, pákṣas, \"wing, side, half\", which is possibly cogn. with Lett. paksis, \"corner of a house\", Russ. pach, \"flank\".' Klein too has no 'breast'."
  },
  {
   "src": "WLD",
   "where": "WP II 3-4",
   "stance": "partial",
   "note": "lists ai. pajasyá- 'Bauchgegend, Weichen' beside the pakṣa- family; gloss 'flank'."
  }
 ]
}
```


### [2026-09-14T00:50:02.534Z] TOOL RESULT

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


## [2026-09-14T00:50:12.900Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nr=json.load(open('refs_online.json'))\nfor k in ['POK','KNT','HRN','IEC','AHD','BQT','MON','BRT','PHD','SYN','WLD','ARY','NYB','HUB','AEF','ZMA','KLN','SKT','LEW','LAT','CHEUNG']:\n  v=r.get(k) or {}\n  print('==',k, '| kind:',v.get('kind'),'| offset:',v.get('page_offset'))\n  print('   local:',v.get('local_file'))\n  print('   hint:',(v.get('lookup_hint') or '')[:300])\n\"",
 "description": "Print page offsets for refs"
}
```


### [2026-09-14T00:50:13.973Z] TOOL RESULT

```
== POK | kind: archive_djvu | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== KNT | kind: archive_djvu | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
   hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== HRN | kind: archive_djvu | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== IEC | kind: archive_djvu | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
   hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== AHD | kind: archive_djvu+website+archive_restricted | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== BQT | kind: archive_djvu+local_scan_ocr | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
   hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== MON | kind: website+archive_djvu | offset: None
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
   hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== BRT | kind: archive_djvu | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
   hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== PHD | kind: archive_djvu | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
   hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== SYN | kind: archive_djvu | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== WLD | kind: archive_djvu | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt']
   hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== ARY | kind: local_scan_ocr | offset: printed page = pdf page + 1
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
   hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== NYB | kind: archive_djvu | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
   hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== HUB | kind: archive_djvu | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
   hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== AEF | kind: catalog | offset: None
   local: None
   hint: Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015
== ZMA | kind: purchase | offset: None
   local: None
   hint: Searched archive.org, ketabnak, noorlib, web: not found.
== KLN | kind: archive_djvu | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== SKT | kind: archive_djvu | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
   hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== LEW | kind: archive_djvu | offset: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt
   hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
== LAT | kind: archive_djvu | offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt
   hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
== CHEUNG | kind: None | offset: None
   local: None
   hint:
```


## [2026-09-14T00:50:18.113Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 46 47 48 49; do echo \"=== POK_03 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((n+1))\"'' POK_03.txt | head -60; done",
 "description": "Print Pokorny leaves around p.810"
}
```


### [2026-09-14T00:50:19.150Z] TOOL RESULT

```
=== POK_03 leaf 46 ===
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
=== POK_03 leaf 47 ===
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
=== POK_03 leaf 48 ===
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
=== POK_03 leaf 49 ===
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


## [2026-09-14T00:50:24.244Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 43 44 45; do echo \"=== POK_03 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((n+1))\"'' POK_03.txt | head -45; done",
 "description": "Print Pokorny leaves 43-45"
}
```


### [2026-09-14T00:50:25.313Z] TOOL RESULT

```
=== POK_03 leaf 43 ===
ch,  streben,  gehen,  eilen'  =  ags. fundian  ds.,  ahd.  funden  ds.,  aisl.  füss  ,geneigt,  willig',  as.  ags.  füs ,schnell,  eifrig,  willig',  ahd.  funs  , bereit,  willig'  (^*fund-sa-)  norw.  füsa ,schnell  laufen';
aksl.  pgtb  usw.  m.  ,Weg'  (^pontis),  tiefstuf.  apr.  pintis  ds.
WP.  II  26  f.,  WH.  II  336  f.,  Trautmann  205  f.;  Wackernagel  KZ  55, 104 ff.,  Ai.  Gr.  3,  1,  306 f.
I.  per-f  pero-  :  pre-,   preu-   , sprühen,   spritzen,   prusten,   schnauben' ;   das- selbe wie  sper-  ,sprühen  usw.'.
A.  perQ-  :pre:  gv.  nl(,i-TtQrj-f.ii,  *7rQrj^(jü  (Ttgifjao),  mor^aa)  ,(fache  an  =) zünde  an,  verbrenne;  blase;  spritze  aus',  Ttgr^öibv,  -ovog  i.  , entzündliche Geschwulst',  7tQ7]i.iaiv(ü  ,blase  heftig',  TCQrnioväu)  ,tobe',  ^Qr^arrjQ  ,Blitzstrahl, Sturmwind,  reißender  Strom';  slav.  *preieti  in  polu.  przec  ,sich  erhitzen, schmoren',  russ.  prejety  preth  , schwitzen,  sieden',  aksl.  para  , Rauch,  Dampft, (apr. ^ore  ,Brodem'  aus  poln.  para);  hitt.  paräi-  ,anfachen,  blasen,  wehen';
mit  t-Formans  aschwed.  fradha  , Schaum,  Geifer',  mnd.  vradem,  vratem , Dunst,  Hauch';  mit  s-Formans  aisl.  fi-cSs  f.  ,das  Blasen,  Zischen',  reduk- tionsstufig norw.  frasa  ,knistern' ;  ö-stufig  (?)  norw.  fresa  , sprudeln,  schnau- ben, fauchen'  (vielleicht  kontaminiert  aus  frysa  und  fnesa).
B.  pr-eu-  :  unerweitert  vielleicht  in  ai.  vi-pru-  ,nach  allen  Seiten  hin sprühen'  (aber  vgl.  pravate  , springt  auf,  eig.  , auseinanderspringen') ;
preus- :  ai.  prusnöti  ,spritzt  aus',  Intrans.  prüsyati  ,spritzt',  aisl.  frysa ,prusten,  schnauben',  schwed.  frusta  ds.,  früsa  , spritzen' ;  lautmalend  mnd. 3Lh.d. prusten]  baltoslav.  *prausiö  ,spritze'  in  lit.  praüsti  ,^3iS  Gesicht  waschen', lett.  prausldt  ,leise  lachen',  prüsfuot  ,prusten',   lit.  prusnos,  lett.  prusnas
810  f
^Lippen,   Mund',    apr.    Akk.    Sg.  prusnan   ^Gesicht^;    aksl.  prysngti,  russ. pryskath  ,spritzen^ ;  aus  baltoslav.  *prüsa-  ( :  schwed.  früsa)  slav.  *prychati[ in  ksl.  prychanije  n.   ^fremitus'^   usw. ;    dazu  vielleicht   als   ven.-illyr.  Elg. ment   im    Gallischen    die   PN   Pruso,  Prusonius  und   der  VN  Prausi  (Iq^; *ProiLSi) ;
preu-t(b)-  :  ai.  pröthati  .prustet,  schnaubt  (vom  Rosse)',  av.  fradd-au aspa-  ,mit  schnaubenden  Rossen',  ai.  apa-pröthati  .schnaubt  weg,  bläst  weg'^ pra-pröthati  ,aufpusten,  aufblasen';  aisl.  fraud  n.,  froda  f.  ,Schaum',  ags. ä-freodan  ,schäumen';
hierher  einige  germ.  Worte  für  ,Frosch',  als  ,der  Geiferige':  aisl. /rat((fr1 (vgl.  fraud  ,Geifer'),  mengl.  früde  ,Kröte'.
C.  Kons.  Erweiterungen  von  per-  s.  noch  miier  perk',prek-  .gesprenkelt^^ pers-  ,sprühen,  spritzen,  gesprenkelt'.
WP.  II  27  f.,  Trautmann  230  f.
2.  per  ,das  Hinausführen  übe
=== POK_03 leaf 44 ===
r'.
A.  Dient  als  Präposition,  Präverb  und  Adverb:
a.  per,  peri  (Lokative  des  Wurzelnomens)  , vorwärts,  im  Hinausgehen,- Hinübergehen  über,  im  Durchdringen,  im  Übermaß',  woraus  ,über  —  hinaus,' durch  —  hin';
ai.  pari,  av.  pairi,  apers.  pariy,  gr.  tvsql,  tcbq,  alb.  per  (z.  T.  auch  = idg.  *pr6),  pej,  pe-,  daneben  per  {*periy  mit  wiederhergestelltem  r;  lat. per  (-^per  oder  *peri):  osk.-umbr.  per-  und  per t  {*per-ti)]  gall.  eri-,  air.  iV, er-  (analogisch  *ero-)]  cymr.  com.  bret.  er;  got.  fair-,  ags.  fyr-,  ahd. /r- ,ver-',  ahd.  as.  firi-  ds.;  apr.  per,  lit.  per,  per-]  slav.  per-  'm  aksl.  pr^- usw. ;  aus  ,vorwärts'  entwickelte  sich  schon  idg.  die  Bedeutung  ,sehr^  (ai. pari-pri-  ,sehr  lieb',  gr.  Ttsgi-y.allrjg  ,sehr  schon',  lat.  per-magnus  ,sehr groß';  lit.  per-didis  ,zu  groß',  aksl.  prä-hlag^  ,sehr  gut'),  dann  die  der Überlegenheit  {2i\.  pari — as-,pdri — bhü-  ,übertreffen',  gr.  negi-eZvai  ds.),  des Übermaßes  oder  hohen  Grades  (ai.  pdri-vid-,  gr.  Ttegl-oida,  lat.  per-videre ,genau  wissen');  besonders  ai.  und  gr.  ist  die  Bedeutung  ,ringsum,  um- herum'  (ai.  pari  i-  ,umhergehen',  gr.  negi-ievai]  gr.  TC£Qi-L,(bvvviii  =  lit. per-jousti  ,umgürten*) ;
Ableitungen  sind:
Got.  fairra  Adv.  ,fern',  als  Präp.  ,fern  von',  aisl.  fjar{ri)  Adv.  ,fern' (davon  Kompar.  firr,  Superl.  first),  ags.  feor(r),  engl,  far,  as.  ferr,  ahd. ferro  Adv.  ,fern,  sehr',  Kompar.  f error  (♦/er-ro- aus  *fer-ero-)]  aksl.  ^r^c?^ ,vor;  voran;  das  Vordere'  (wie  na-d.^),  prez-h  ,über  —  hin';  -Ä:o-Adj. :  prlk^ ,quer',  cech.  pH^{kd)  ,Querholz'  =  umbr.  percam  ,virgam',  osk.  perk\ais\ ,perticis*;
in  zeitlicher  Verwendung:  ai.  par-üt,  gr.  -rtigvoL  usw.  (s.  unter  uet-  ,Jahr') und   die  Ableitungen  lit.  pernai  ,im  vorigen  Jahre',   lett.  perns  Adj.   ,vor-
k
811
iährig;  firn'^,  mhd.  verne  ^vorjährig^,  vern  ,im  vorigen  Jabre^,  got.  nur  in (if  fairnin  jera  ,yom  Vorjahre^,  as.  fernun  gei-e,  fernun  iära  ,\m  Vorjahre^, ^.ivon  mit  lo-Formans  got.  fairneis  ^itakaio^^  aisl.  fymd  i.  ,Alter',  ahd. jlrni  ,alt;  weise^,  nhd.  Firn  ^alter  Schnee^;  ebenso  zum  tiefstufigen  got. faur  das  aisl.  forn  ^alf^^,  neben  dem  i-St.  as.  an  furndagun^  ags.  fyrn^ ßrn  ^alt^;  vgl.  ai.  puränd-  ,vormalig^  zu  purä,  ap.  paranam  ,vormals^  zu parä]  lat.  perendie  ^übermorgen'  aus  *peren-die?
auf  per-  in  anderer  Verwendung  weist  '^per-u-2'ln-  in  bora.  neigag  (Find. itstgagjf  TTslgarog,  att.  Ttsgag,  -aTog  ,Ausgang^  Ende'^  bom.  dcTreiQwv  ,unend- licb^  =  (att.)  djtSQOva '  rvegag  ^ij  e'xovra  Hes.,  bom.  neiQaivcjjj  att.  nsgalvu) ^voUende^;  —  daneben  im  Ai.  eine  gleicblautende  Sippe  der  Bedeutung ^Knoten^:  ai.  parva-  Nom.  Akk.  PI.  n.  _,Knoten^  Gelenke'  (statt  *2?arüf), pdrii'  m.  , Knoten,  Gelenk,  Glied  (Ozean,  Him
=== POK_03 leaf 45 ===
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
```


## [2026-09-14T00:50:42.205Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 195 196 198 200; do n=$((p+15)); echo \"=== KNT printed p.$p (leaf $n) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((n+1))\"'' KNT.txt | head -70; done",
 "description": "Print Kent lexicon pages 195,196,198,200"
}
```


### [2026-09-14T00:50:43.258Z] TOOL RESULT

```
=== KNT printed p.195 (leaf 210) ===
1) XPh 23.
tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) AmH 5; AsH 13°. tyà npf. DB 1.13, 18; 2.6; 4.33; DPe 9, 14f; DSf 45. tyaiy as npf. (§258.1V) = XPh 31. рё apf. DPe 7; DNa 17, 40; DSe 16. . tyaišām gpf. DSm 6°; XPh 15.
tya nsn. (M0) DB 1.27, 61, 67; 2.91; 3.10, 20, 58, 76; 4.1f, 42, 49°, 53; DNa 48; DNb 2, 11, 29, 54, 56; DSe 31, 43; DSf 36; DS} 5^; D8n 2^; DZe 9, 10; XPa 19; XPb 23; ХРЇ 26, 37, 46; XPg 4; XPh 42; XV 19; AjPa 26. tya-sém DB 1.19; DNa 20; DSe 19°; XPh 17. tya-maiy DNb 48; DSe 52°; DSf 19°; DSs 7^; XPa 19f; XPb 24, 30; XPe 13 bis; XPd 19; XPf 38, 47; X8e 5°; XV 27°; A!Pa 24°; A?He 20. tya-taiy DNb 58. tya-patiy XPa 15. (ya asn. DB 1.44, 72; 4.3, 40, 59, 75, 79; 5.2; DPh 4; DNb 22, 24; DSa 4; DSf 20f, 22°; рө) 2°, 4; DSI 3; DH 3; XPa 14, 15; XPf 41; XPh 43, 49, 52; A’Sa 5^; А4 3; А?На 7. [tya]- ат DNa 36f. tya-maiy DPh 8; DH 6. tya-patiy XPf 40f. {уала isn. DSf 42. {уй npn. in tyã- maiy DNb 13. tyä apn. DB 1.64; DNb 46, 49. tyā-diš DB 1.65.
(2) Def. art., ‘the’: ат asm. DB 1.50, 54, 57, . T8, 89, 95; 2.21, 25f, 35, 41, 46, 55, 61, 69, 87, 97^; 3.7, 18, 38, 46, 625, 67f; 481; DSe 39. tyam- iim DB 5.12".
іуйт asf. DB 1.69, 71; 4.87; DNa 59. tya as asf. ($56. V) AsH 9, A’Sc 6. tyaisám gpf. DPe 3f.
tya nsn. DNa 21; DSe 20°, 38; XPh 19. tya asn. DB 1.81; DSf 11 his; DSm 4° bis; DSp 2°, 8°; DZc 4 bis. tyanā isn. DB 1.23.
(3) Demonst. pron., ‘this’: буй ndm. DSf 14. шай apm. DB 3.73.
уа. conj. ‘that’, nt. sg. of preceding; cf.
similar uses of Gk. öre, Lt. quod, NEng. that, NGm. dass. In various uses ($299):
(1) ‘that’, introducing clause of fact as object, DSf 28 bis, 29.
(2) ‘that’, introducing clause of volition, with opt., DNb 8, 10, 19.
(3) ‘that’, introdueing indirect or direct quota- tion, DD 1.32, 52; DNa asf.
(+) ‘because’, introducing causal clause, DNb 38 (tya-maty).
(5) ‘so that’, introducing result clause, DB 4.34; DNb 7.
187
(6) ma-tya “п order that . . . not, lest, not, DB 4.43, 48, 71, and in md-fya-mdém DB 1.52.
(7) yada-tya ‘where’ XPh 35, cf. yadéya ‘where’ XPh 39.
(8) yafü tya ‘when’ XPh 29.
Odigarct- adj. ‘Thaigarci’, third month, May- June: Elam. sákurrisi$, АКК. simannu (S30, §72, §87, $126, $1521, §165); an etymology as ‘Garlic-Collecting Month’, involving normaliza- tion @digraci-, is given by Justi, ZDMG 51.243 (cf. Bthl. AiW 786). Oäigarcaiš gsm. DB 2.46f.
akata- pte. adj. ‘completed’: Av. sak- ‘(of time) pass’, pIE *keg-; fut. pte. pass. (8244) like Av. yazata- ‘worthy of worship’ (Bv. BSLP 30.1.68-70), passing into past meaning, like Skt. pacalá- ‘cooked’, Gk. dpi-delx-e7os ‘much pointed out, famous’ (Schwyzer, Griech, Gram. 501-2); rather than pres. act. pte. daka"t- made thematic (cf. Bthl. АКМ 22.79-80). @akatam nsn. DB 3.8. 6akalá npn. DB 1.38, 42, 56, 90, 96; 2.26f, 36, 42, 47, 56, 70, 98; 3.19, 39f, 47, 63, 68, 89.
Oalagu- sb. ‘Sattagydia’, a province of the ` Persian Empire: Elam. sa-ad-da-ku-13, Akk. sa- al-ta-qu-u, Gk. Zarrayudia ($07, §87, $120, $158.1, $161.ITa, $204.V). From éata- ‘hundred’, Av. sala-, Skt. Satdém, Gk. ё-катоу, Lt. centum, NEng. hundred, pIE *kmto-m, + gav- ‘cattle’: ‘having hundreds of cattle’ (hardly ‘(Land of] Seven Streams’, with Hz. AMI 1.99n, 3.100-2, 8.78, König Rul D 63). Seealso @ataguzya-. — 8alagu& пэт. DB 1.17; 2.7; DPe 17; DNa 24; DSe 28°; DSm 10°; XPh 22.
Gataguiya- adj. ‘Sattagydian’: adj. to preced- ing (5144.11, $167). G@ataguiya nsm. А?Р 11; for -guoiybi, unless -gudaya is to be read (854.T, $167), ef. Gk. Zarrayidat, in which case the etymology given under @atagu- must be revised.
да"4- vb. ‘seem’: Av. sand-, Skt. chand- (887, $215). @adaydlary subj. mid. ($222.II) DB 4.49; DSa 5; 08) 6 (for text, see under frasa-; cf. 554.1). ðadaya inj. ($224, 5228.11, §237) DNa 58; рМ 53.
додада,
=== KNT printed p.196 (leaf 211) ===
 word of uncertain meaning, Sb 3.
Sanuvaniya- sb. ‘bowman’: deriv. ($144.IV) of stem in Av. Üanvar/n- ‘bow’, ef. Skt. dhanvan- ‘bow’ (583.11, $114, §155.1V) and Hz. ApI 339.
See also wlanwaniya-.  Ganwaniya.nsm. DNb 42.
188
*
bard- sb. ‘year’: Av. sarad- ‘year’, NPers. säl, Skt. Sardd- ‘autumn’ (§31, 587, $142). For the chronology of the rebellions against Darius, see Hist. App. IV. &ardam asf. DB 5.3. barda gsf. DB 4.4f, 41, 45, 52, 60.
barmi- sb. ‘timber’ (86, 529, $34, $15217): no probable etymology, despite Kónig, Burgbau 52-4; Hz. AMI 3.58; Gray, AJP 53.67-8. barmiš р? 30.
баћ- vb. ‘declare, say’: Ау. sqh-, pres. sanha-, Skt. édsati, Lt. censet, рТЕ *kens- (§87); perhaps lacking the nasal in the OP present ($108.n1; MB Gr. $134, ef. Wackernagel, IF 45.321-7; dubious theories on the pronunciation, Hz. AMI 3.83-6). 6atiy (8131, $213, 5228.1; JAOS 35.332-4) AmH 4, 9; AsH 5; CMb 3; DB 1.3, 6, 8f, 11, 121, 17, 20, 24, 26f, 35, 43, 48, 61, 71, 72, 81, 83, 90; 2.1, 5°, 8, 11, 13, 18, 29, 37, 42, 49, 57, 64, 70, 78, 91, 92; 3.1, 9, 10, 19, 21, 28f, 40, 49, 521, 54, 64, 69, 75, 76, 83; 4.1, 2, 31, 33, 36, 40, 43, 45, 50, 52f, 57, 59, 61, 67, 69, 72, 76, 80, 86, 88; 5.1, 14, 18, 20, 30, 33f; DBa 4, 9, 13f; DPd 5, 12; DPe 5, 18; DPh 3; DNa 15, 30, 47; DNb 5, 22; DSa 3; рва 2f°; DSe 14, 30°, 41, 49°; DSf 8, 55; DSg 2f; DSi 2f; DS} 2, 4°; DSk 3; DSI 1; DSm 3; DSo 2°; DSt 6f; DZc 7; DH 3; XPa 11, 17; XPb 21; ХРе 9; XPd
^ 15; ХРЇ 15, 27, 43; XPg 1; XPh 13, 28, 56; ХР);
XSa 1; X8e 2f°; XV 16; А:Ра 17; D'Sb 3°; Аа 1; A’Sc 1°; A’Sd 2; А?На 1; A?He 7, 15; A?Pa 8, 21, 23. |
аваћат Ist sg. imf. (5181, $132.23, 8213) DB 2.20, 30, 50, 83; 3.14. 85; DNa 37. alaha imf. DB 1.75; 2.10°, 15, 80; 3.25, 57£; 4.8, 11, 13, 16, 19, 21, 24, 21°, 29; DBb 4; DBe 5; DBd 3; DBe 5; DBf 3; DBg 4f; DBh 4; рв: 4; ОВ) 3. éahya- mahy 1st pl. pass. (5220, $280.Г) DB 1.7; DBa 10f. aðahya imf. pass. ($220) DB 1.20, 231; РМа 20; DSe 19°; abahiya (827) XPh 18. " баћу 2d sg. subj. ($181, $222.11, $227.I) DB 4.55, 58. 6aslanaiy inf. ($132.23) DB 1.58f.
bikä- sb. ‘gravel, rubble, broken stone’ ‘(wrongly Konig, Burgbau 50, cf. Kent, JAOS 53.14): probably pIE *higd- (887, $143.IV), ef. Skt. sikata- ‘sand, gravel’ (with Prakrit s for Skt. §, or borrowed from an Iranian dialect, Ву. BSLP 30.1.60-1), and perhaps OP Sikayawatis (with Med. s-), fem. to *$ikayas-vant- (ef. Bv. BSLP 30.1.61; Hz. AMI 3.55-6; Kent, JAOS 51.203). Ка nsf. DSf 25, 28. бат asf. DSi 27.
OLD PERSIAN
Өшта- sb. "Thukhra', father of Otanes (8163.Ib, §164 JIT): Elam. du-uk-kur-ra, Akk. su- uh-ra-’. Perhaps same as Av. suzra- ‘red’, NPers, surz, Skt. $ukrd- "bright ($87, 5108.1, §148.1; ef, Foy, KZ 35.20).  Guzrah|yli gsm. DB 4.83.
Oüravühara- adj. “Thuravahara’, second month, April-May: Elam. turmar, Akk. айайги.
Cpd. of @йга- ‘vigorous’, Av. süra-, Skt. $ra-, Gk. —
kvpos ‘valid’, pIE *hiro- (887), + vàáhara- ‘spring time’, Skt. vdsard- ‘bright’, NPers. bahar ‘spring’, Lith. vásara ‘summer’ (§1181, $126, $148, 5148.1, §154.1; ef. Bv. Origines 16): ‘(Month) of Strong Spring’ ($161.ITa, §165). Guravüharahya gsm. DB 2.36, 41, 61; 3.39. .
çay- vb. ‘lean’: Av. sray-, Skt. Sri-, Gk. кою, Lt. in-clinat, NEng. lean, pIE *flei- (§94). ni- + gay-, causative (8129, $215) ‘restore’; form influenced by ddraya- in Av. and OP (Ware, JAOS 44.285-7): niyacürayam 1st sg. imf. DB 1.64.
çita- adj. ‘third’: Gk. rpizos, pIE *tritos (§204.- IIT). See also cztiya-. Фат) asf. DB 5.3 (JNES 2.109-10).
citiya- adj. ‘third’: Av. 6ritya-, Sks. trtiya-, Lt. tertius, pIE *trifizo- (878, 414111, $204TIT); see also cita-. сат asn. as adv. DB 243.
(asa- sb. ‘Susa’, a capital city of Darius, in . |
Elam: Elam. šu-ša-an, Akk. Su-Sa-an, Gk. Loven (878, 17). Саќауа Isf. DSf 22, 34, 56; DSo 3f.
Idà- vb. ‘give’: Av. Skt. dà-, Gk. бош, Lt. dai ‘gives’, dónum ‘gift’, pIE *dó- (862, 576.11). dadátus іту. (§209, $237.II) DPd 28; DNa 55; XPh 60.
*dà- vb. ‘put, make, create’: Av. dá-, Skt.
dhà-, Gk. ri
=== KNT printed p.198 (leaf 213) ===
5-6).
Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 522-486 ».c.; IT, son of Artaxerxes I, king 426-04 в.с.): Elam da-ri-a-ma-u-ts, Akk. da-ri- ja-mus, Gk. Дарєюѕ (by haplology for *Aapetaios; Keiper, Acta Sem. Phil. Erlangen, 1.253). From pAr. *dháragat-, pic. to root in OP dar- (§162, §240), + pAr. *yasu asn. ‘the good’ (5158.1), see OP vau-: ‘He who holds firm the good’ (Hz. Arch. Hist. Iran 40, ApI 255, 267, takes as hypocoris- tie of *ddraya-vahu-manah- ‘Holder of Good Thought’; this is rejected by Nyberg, Rel. 361).
Dérayavaus nsm. (8118.IV, 5124.2) DB 1.1, 4, 6,9, 11, 13, 171, 201, 24, 27, 35, 44, 48, 61, 71, 73, 81, 83, 90; 2.1, 5, 8, 11, 13f, 18, 29, 37, 42f, 49, 57, 64, 70, 78, 91, 92; 3.1, 9, 10f, 19f, 21, 29, 40, 49, 53, 54, 64, 69, 75, 76, 83; 4.1, 2f, 31, 33, 36, 40, 43, 45, 50, 58, 57, 59, 611, 67, 69f, 72, 76; 80, 86, 88; 5.1, 14, 18, 20, 30, 34^; DBa 1, 41,9, 14; DPa 1;
190 OLD PERSIAN
DPb; DPd 4f, 5, 12; DPe 1, 5f, 19; DPh 1, 3f; DNa 8, 15, 30f, 40, 47t; DNb 5; DSa 1, 3; DSb 1f°; DSc; рва 1°, 3°; DSe 8, 14, 30f°, 41^, 49f; DSf 5f, 8, 55; DSg 1, 3; DSi 1, 3; DSj 1, 2, 5; DSk 1, 3f; DSI 1; DSm 1, 3°; DSn 1°; DSo 2f; D8q 2; DSt 7°, DSy 1; DZa; DZb 1; DZe 4, 7; DE 12; DH 1, 8; XPc 11; XPf 16f, 30, 38; XPg 6; XSa 2; XV 17; D*Sa 2; D'Sb 1°, 3°; Аа 3; Wa 21; Wb 1; We 2; Wd 2; SDa; SDb. Dérayavahaus as nsm. XPf 25 (851; Lg. 9.39).
Dérayavaum asm. DPd 2; DNa 5; ОХЬ 4; DSe 5^; DSf 3f; DSn 2; DSp 1f°; DSt 5°; DZe 3; DE 7; XPf 221; D'Sa 2f.
Dérayavahaus gsm. (8118.1V, 5124.2) DB 3.58f; DPe; DPd 10; DPi; DNe 1f; DNd 1; DZc 3; XPa 9f; XPb 19; XPe 8f, 14; XPd 13; XPe3; XPf 13f, 17; XPh 11; ХР}; XPk; X8e 2°; XE 19; XV Mf; A!Pa 16. Dérayavaus as gsm. XPf 28 (851; Lg. 9.39); (8313.11) A’Sb, A'Sd 2, A?Hb, A?Pa 13f, 14, 17, 18. Dérayavausahya gsm. (557) АЧ, A’Sa 1, 1f, 2f, 3; A?8c 0 bis; A?He 9f, 10 (as nom., 8813.1), 18, 14 (as nom.). Dàrayavasahyà gsm. (852.VI, $57) А?На 2, 2°, 4, 4°.
daru- sb. ‘wood’: Av. déuru-, Skt. dáru-, ef. Gk. доро ‘spear’. düruv (§181) nsn. DSf 41, in phrase asd атир ‘ebony’, lit. ‘stone wood’ (§308.- nl), so called because of its hardness; but also probably аз@ because of the assonance translated Akk. aban ‘stone’, ef. Hebr. eben ‘ebony’, Gk. Веро, from Egyptian hbnj ‘ebony’ (J. Duchesne- Guillemin, BSOS 10.925-7 [1942], noting that acc. to Hdt. 3.97 the Egyptians paid a tribute of ebony logs to the Persian King). Not to be normalized dārwa to root !dar- and the phrase taken as ‘copper’ (Scheil 21.30; Kent JAOS 51.208, 53.18- 9), or as ‘iron’ (Ву. BSLP 30.1.60; who also sug- gests that dáruva may be an adj. referring to some kind of tree); not asé + instr. déruv ‘window frames of wood’ (König, Burgbau 64-5); not asd süruva ‘lead’ (Hz. Ар] 299), to Av. srva- ‘lead’ (Bthl. AIW 1649), for the slight traces do not con- firm initial s". — [dár|uv asn. DSf 51 (so Hinz, Orientalia, soon to appear; not {23mal}uv, see Lex. S.V.).
darga- adj. ‘long’: GAv. daraga-, LAv. daroya-, NPers. dër, Skt. dirghd-, pIE *dlgho-, ef. Ck. dodexés, Lt. longus (881, $68, $101, $148.11, VI). dargam asn. as adv. ‘for a long time’ DB 4.56, 15.
dartana- (or perhaps zarlana-, with Med. 2) sb. ‘anger’: Av. zarafa- ‘enraged’, Skt. hrnité ‘ig angry’ (§34, §147.V, $238). [dalrtanaya lsn. DNb 13f (conj. of Kent, JNES 446-7; ef. §238.n1).
darš- vb. ‘dare’: GAv. dora&- ‘deed of vio- lence’, Skt. dhrs-noti ‘dares’, NEng. dare (570.11, $117). See also Dädarši-, darfam. adaršnauš imf. $80, §84, §210.1, $228.11) DB 1.53.
darsam adv. ‘mightily’: asn. to adj. darsa- ($143.1), to root dar§- (against this, Hz. Apī
135-6). DB 1.50 (MB Gr. $366; wrongly Kent, ·
JAOS 35.336-42); 4.37; DNb 14, 15, 50.
dasta- sb. ‘hand’: Av. zasta-, N Pers. 0051, Skt. hdsta-, pIE *ghosto- (§88, $116, $145). See also dastakarta-. даѕіауа ism. DR 4.35. dastaibiya idm. (§189) DNb 41.
dastakarta- adj. ‘handmade’: dasta- + pte. .
karta- (5160.10), to kar- ‘make’. [dasta|kartam (restored after the Elam., Wb. ZDMG 91.85, 
=== KNT printed p.200 (leaf 215) ===
rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $136).
duradasa adv. ‘from afar’, with preceding hacá: dūra- + adv. -dä asin отада + abl. -ša asin avada&a (§135, 5191.1; ЈАО 54.37).  DSf 23.
duruj- vb. ‘lie, deceive’: Av. druj- ‘le’ (draog-, Bthl. AYW 767), pres. druZasti, sb. druzé ‘principle of evil, devil’, Skt. drúhyatí ‘deceives’, Gm. trügen, pIE *dhrugh- (876.111). See alsodrauga-. adu- rujiya imf. (§101, $103.IV, $113, 5128, 4132.1, 2, 3, $214, 5228.11) DB 1.39, 78; 3.80; 4.8, 10f, 13, 16, 18, 21, 24, 261, 29; DBb 2; DBc 2; DBd 2; DBe 3f; DBf 1; DBg 2; DBh 2f; ОВ! 2f; DB} 2f. adurujiyasa" 3d pl. imf. ($214, §218.1, $232.III) DB 4.34f. duruxiam nsn. past pte. pass. ($103.IV, $122, $128, 8132.1, 3, $242.I) DNb 52, 5f; asn. DB 4.44f, 49f.
duruva- adj. ‘firm, secure’: Av. drva-, Skt. dhruvd-; deriv. to root in OP ‘dar- ($122, $128, $150). durwä nsf. DB 4.39.
duvatsta- adj. ‘very long, very far’: superl. to dūra- ($156.IIL, §190.11 $191.0; МВ Gr. $275), ef. Skt. davisthd- with slightly different formation.
192 OLD PERSIAN
duvais[ta]m asn. as adv. ‘for a long time’ DPe 23 (cf. remarks s.v. hyà).
duvara- sb. ‘door’: Av. dvar-, Skt. dhvar-, Gk. дора, Lt. forés, NEng. door, Lith. dvéras ‘court- yard’, pIE *dhuor- dhur- and its extended forms *dhyoro- etc.; see also duvarfi-. duvarayd-maiy lsn. ($186) DB 2.75; 89f.
duvari- sb. ‘portico, colonnade’: duvar- ‘door’ + varði- ‘cover, protection’, to root var- ‘cover’, with haplology ($34, $129, $152.IV, §160.Ia; ВЫ. AIW 766). duvarfim asm. XPa 12.
duvitdparanam adv. ‘one after the other, in succession’, a meaning agreeing with Elam. Samak- mar ‘ex ordine’: duvità ($191.11, $204.IT), MPers. dit ‘one or other of two’ (Bthl., quoted by Tm. Lex. 102), ef. OP duviliyam ‘a second time’, Skt. 0015 ‘twice’, Lt. bis, + paranam ‘before, previ- ously’ (Tm. 1.е., and Vdt. Stud. 1.8). This is better than Tm.’s "long aforetime', adv. duvità ong’, GAv. дайа, Skt. dvità (cf. OP duvaistam), + paranam (as above); also than KT's duvità- parnam ‘in two lines’, contaming the cognate of Skt. parnd- ‘wing’ (supported by Wb. ZDMG 61.724-5, KIA 10-1, and by Hz. AMI 1.112n). DB1.10; DBa 17.
duvitiya- adj. ‘second’: GAv. daibitya-, LAv. bitya-, Skt. dvitiya-, pLE *dyitiio- (676.11, 51441, 5204.1). See also duwilàáparanam. дилат, asn, as adv. ‘a second time’, DB 2.87f, 57, 3.77; as inner obj., ‘a second (uprising), DB 3.24 (not duvitiya-ma udapalalà ‘was second to rise up from me’, as Bthl. AiW 964 takes it, since udapatatà nowhere else takes an expression of the person against whom uprising is made).
duš- insep. prefix ʻi: Av. dui-, Skt. dus-, Gk. dve- ($76.Ш); in dušiyāra-, duskarta-.
dusiyara- sb. ‘evil year, bad harvest, famine’: duš- + yar- ‘year’ made thematic, Av. ydr-, Gk. ёра ‘season’, NGm. Jahr ($140.VIT, $143.IT). dušiyāram nsn. DPd 19. dudiyard absn. DPd 17.
| du$karia- ad). ‘ill-done’, opposite of naiba- (Hz. ApI 1434): duš- + karta- ‘done, made’, past pte. pass. tokar-. duskartam nsn. DSe 31f; XPh 42. draug- vb., see duruj- and draujiya-.
drauga- sb. *the Lie", the evil force opposed to Ahuramazda, Ávestan Druj: Av. draoga-, NPers.
dury, Skt. drógha- droha- ‘(malicious) injury’, pIE *dhrougho-, cf. NGm. Trug ‘deceit’, and OP duruj-, draujana-, draujiya- (870, 576.11, $101, $108.IV, $106, $122, $128, 5132.2, 3, $143.I, V). drauga nsm. DB 1.34, 434; DPd 20. draugà absm. DB 437; DPd 17f.
draujana- adj. ‘deceitful’, i.e. ‘adherent of the Lie’: deriv. of drauga- (§101, 5132.2, 5147.1), cf. GAv. drogvant- ‘adherent of the Dru? (Hz. Apl 140-1). draujana nsm. DB 4.38, 63, 68. drauja- nam asm. DNb 12.
draujiya- vb. ‘regard as a lie’, denom. to drauga- (S217). [Отау уау 2d sg. subj. (§222.11, §227.1) DB 4.43.
drayah- sb. ‘sea’: Av. zrayah-, NPers. dáryà, ·
Skt. jrdyas- ‘expanse’, pIE *órejos- (§88, $113, $128, $156.II). Decl, §185.1. See also para- draya. draya asn. DB 5.23; DP
```


## [2026-09-14T00:50:52.101Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 218 219 221 223; do echo \"=== KNT leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((n+1))\"'' KNT.txt | head -80; echo; done",
 "description": "Print Kent leaves 218,219,221,223"
}
```


### [2026-09-14T00:50:53.090Z] TOOL RESULT

```
=== KNT leaf 218 ===
with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $142, §166, 5160.1): ‘Home of the Archives and Sacred Writings’ (on Pasargadae, ef. also Kónig, RuID 66; but Hz. ApI 275-6, modifying his view ш AMI 1.86n, takes prior element to be pati-, pati- becoming pa&-, with epenthesis; Bthl. AiW 907-8 normal- izes Piši- after the Akk., but gives no etymology). Paisiydwddim asf. DB 3.42. Parsilydluvadayd absf. DB 1.36f.
pa|camàm] adj. ‘fifth’, asf.: wrong restoration of Wb. at DB 5.8 (ef. Kent, JNES 2.109).
pal- vb. ‘fly’: Av. pat-aiti, Skt. pát-ati, Gk. vérerat, Lt. рені ‘seeks’, pIE *pet-.
ud- + pat- ‘rise up, rebel’ (cf. Ву. TPS 1945.64-
66): udapalatà imf. mid. (§84, 8213, 5285.П) DB 1.36, 38, 74, 78; 2.10, 14f; 3.24, 79.
patiy adv., prep., prefix ($140.I, $1911): Av. рай, Gk. (dial.) rori, pIE *poti, cf. pIE *proti in Skt. prát, Gk. Hom. троті, classical rpés (cf. Lg. 20.9-10).
(1) Adv. ‘thereto, again’: DB 2.37, 48, 57; 3.04, 71. pati-maty ($186) DNb 32f.  nai-pati-mà ($133, 5186) DNb 20. yadi-patiy (8136) DNa 38. (ya-patiy XPa 15; XPf 40f.
(2) Prep. (8271) with ace.: DB 52 ‘during’; DNb 22 ‘against? (Hz. ApI 273 reads par[slaiy ‘in court’, sb. to root fraé-); postposed DB 2.62 ‘on’. Encl., with ace. ‘during’ DB 1.20 (8133, $136); with inst. ‘near, at’ DB 2.16°, 3.26; with loc. ‘on, upon’ DB 2.76, 91; 3.52, 92. Ву. BSLP 42.2.70 takes all these as adverbs except DB 2.62, DNb 22.
(3) Prefix with verbs avahya-, ay-, ziay-, jan-, рӣ-, fraf-, d-bar-, zbü-; prior element in nouns palikara-, Patigraband-, perhaps Pátisuvari- and
"* 2 - -
also patiš, patisam.
patikara- sb. ‘picture, (sculptured) likeness’: .
РМ. patkar-, NPers. pátkür-;.pati- + kara- to root
as sata jeu iit И ЗАК
pores agent iain ee Seeman Re NE SS a cet ras ЧЕК ЧАС ve NEMPE
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
par- vb. ‘communicate’: Av. *par- ‘hindureh-, hintibergehen’ (ВЕ. AYW 851), Gk. weipw 

=== KNT leaf 219 ===
‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- іаїу| nsn. past pte. pass. ($242.1) DNb 54 (dubious con]. of Kent, Lg. 15.167, 178-4).
ipara- adj. ‘later’, possibly in hyáparam (q.v.) : Av. para- ‘farther’, Skt. pára- ‘distant’, Gk. qépav ‘beyond’.
nara prep. with acc. ‘beyond’ (§32, $63.1): Av. pard ‘before’, Skt. purds ‘before’, Gk. таро ‘before’; DPe 15; DPh 5; DH 4, See also para- dayadàm, paradraya.
parü postpos. with acc. ‘along’, and verbal prefix ‘forth’ ($132.3): Av. ?pará ‘before’, Skt. purá ‘before, formerly’, Gk. rapá ‘alongside’: in avapard and with ay-, ar-, gam-, bar-.
parauvaty lsn. as sb. ‘in the east’: руи] "Ре 15, a misreading for pr? : d*r^ ye (uninseribed space between r* and y*) = para : dra ya; seeunder paradraya.
paradayadám sb. asf., perhaps ‘pleasant re- treat’ ($55.II, §148.1V): Аа 3. Possibly mis- written руат“ for p'rud*iljme = paridai- dam, Av. patridaéza- ‘Umwallung, Ummauerung' (Bthl. AiW 865), borrowed in Gk. тарабено ‘park’, cf. JAOS 51.229; or for p'r*d'id^am* = paradidam, from ?para ‘beyond’ + didá- ‘wall’ (q.v.), as ‘that which is beyond or behind the wall’ (ef. Scheil 21.93; Bv. BSLP 30.1.67 j'vadiy paradayadám ‘paradis de vie’).
paradraya phrasal adv. ‘across the sea’ ($44, $191.[V): рата ‘beyond’ + acc. draya ‘sea’. DNa 28f; DSe 29°; XPh 24. paradraiya (848) A?P 24 (Hz. ApI 142). As two words, para draya DPe 15 (Cameron, JNES 2.307-8).
parana- adj. ‘former’: deriv. ($147.11) of stem in OP ?para, para (cf. ВЕШ. AiW 854), Av. рагі, рагб, Skt. рига ‘formerly’ (hardly to be normal- ized parna-, with MB Gr. $267, to Gt. faírneis ‘old’). See also dumlaparanam. — paranam asn. as adv. ‘formerly’ DB 1.51, D'Sb 3.
pariy prep. and prefix ‘around, about’: Av. pairi, Skt. pári, Gk. тері, Lt. per ‘through’, pIE *peri ($64, §75.1, $113, §140.1). Prep. with aec. ‘about’ DB 1.54. Prefix-with ay-, bar-; ef. also pariyana-.
196 OLD PERSIAN
pariyana- sb. ‘superiority’: deriv. ($147.IT) of pariy, in meaning seen in Ау. pairi ‘vorne, über ... hin’, Skt. pári as prefix ‘much, excessively’, cf. Gk. meptoads ‘excessive’ (otherwise Hz. ApI 273, Sen 250). pariyanam nsn. DNb 52.
paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; Азра 6, 7.
paruva- adj. ‘being before in time or place’ (§35.1[): Av. paurva-, Skt. pürva-, pIE *pruos (868, $150), ef. Gk. Ion. трохоѕ ‘early’. See also paruviyata, paruviyaüd. parwā npm. ‘former’ DB 4.51. parwam asn. as adv. ‘formerly’ DB 1.9; DBa 15f; DSe 43°, 47; XPh 36, 39; paruvam- ciy DB 1.63, 67, 69.
parwnyata, adv. with preceding hacd, ‘from long ago’: *paruviya- (ie. *parvya-, deriv. of paruva-), Av. paouruya-, Skt. pürvyd-, + adv. suffix -la^, Av. -£ó, Skt. -tas, Gk. -ros, Lt. -tus asin funditus, pIE *-los ($191.11). C£. also paruviyatà. DB 1.7, 8, 45; DBa 11, 12.
[paruv|iyafà adv. ‘at first attempt’: *paruviya- (see paruviyala) + adv. suffix -0à, Av. -fa, Skt. -ihà ($191.ID). DSj 3 (conj. of Brandenstein, WZKM 39.49-51; ef. note ad loc.).
paruzana- adj. ‘having many men, or many kinds of men’ (‘having men of all tongues’, Wb. ZfA 44.165, after the Akk.): paru- ‘many’ + zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. poruvzandndm (523.1) XPb 15f; XPd 11. раги zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; XPh 9; XV 12.
Parga- sb. ‘Parga’, a mountain in Persia: Elam. par-rak-qa, NPers. Purg ($30). Parga лет. DB 3.44. |
partara- sb. ‘battle’ (as in Elam. and АКК. versions): extension of -r/n- s

=== KNT leaf 221 ===
r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1, $154.II); see also hamapilar-. pita пет. ($86.П, $124.5, $186.1T) DB 1.4 bis, 5 bis, 6; 2.93; DBa 5, 6, 6f, 7, 8; DSf 12, 58; XPa 15; ХРе 12; XPf 16, 17, 19, 23, 31, 33, 42; XPg 7; X8a 2; XV 18; А!Ра 20f; D?Sb 4°. pica gsm. ($78, $124.5, $186.If) XPa 20; ХРе 14; XPf 35, 38, 47.
Pirdva- sb. ‘Nile’ (§75.V, $124.II, §166.V]): Pirdva пзш. DZc 9, in naming phrase, anacolu- thic for abl. after Ласа; either ‘Ivory River’, as deriv. adj. to piru- ‘ivory’, or possibly plural ‘The Tusks’ (JAOS 51.209).
miru- sb. ‘ivory’ (§75.V, 5153.1): Elam. pi- ru-§, Akk. pilu-, with cognates (or borrowings) in Eastern Asiatic languages (Przyluski, BSLP
197
27.3.220-2; Scheil, Rev. d’Assyr. 24.120; Bv. BSLP 30.1.62; König, Burgbau 66; Hz. AMI 3.67-8).  piruf пет. DSf 48.
pi-, vb., see paid-.
pisa- sb. ‘raft’: perhaps originally ‘cut mate- rial’, from root pazd- (8143.1II). різ ism. or isn., with collective meaning (§255), DB 5.24.
pisa- or paisa-, vb. stem, see paið-.
Putéya- adj. ‘man of Put, Libyan’ (§75.V, $/6.V, §144.HI); pl., ‘Libya’, a province of the Persian Empire (Cameron, JN ES 2.308-9) : Elam. pu-á-ti-ja-ap, Akk. pu-u-ta (Lg. 18.299, 15.165). Pulüya пет. A?P 27. Putāyā npm. DNa 29f; DSe 29°; XPh 28,
puça- sb. ‘son’: Av. puéra-, Ars. РЬ. рим, N Pers. pus, Skt. pulrá-, Ose. puclo-, рї *putlo- ($64, §75.1,§78,§148.1II). pucansm. AmH 3; AsH 4; CMb 2°; DB 1.8, 28, 39, 53, 74, 78, 79; 2.9; 3.25, 79, 81; 4.9, 14, 28, 30, 83, 84° bis, 85 bis, 86; DBa 3; DBb 6; DBd 6; DBh 7; DBi 8f; DPa 5; DPb; DPe 5; DPh 2; DNa 18, 14; DSa 2; DSb 10; DSe; DSd 2; DSe 12, 13; DSf 7; DSg 2°; DSi 2°; DS} 2°; DSk 3; DSm 2°; DSy 3; DZb 5f; DZec 6; DE 20; DH 2; XPa 10; XPb 20; XPe 9; XPd 14; XPe 4; XPf 14; XPh 11, 12; XPj; XPk; Х5е 2; XE 20; XV 15; A!Pa 15f; АЧ bis; D'Sb 2°; Аба 1, 2 bis, 3 bis; Ab; A?Sc 0° bis; А4 2; A?Ha 2°, 8, 3°, 4, 4°; А?Не 10, 11, 12, 13f, 15; A3Pa 18, 14, 15, 16, 18, 19, 20; Wa 7; Wb 8; We 9; Wd 9; Sa 8°, pucä npm. XPf 28; as nsm. А?НЬ (853; with -a after парӣ, acc. to Brd. WZKM 39.92).
farnah- sb., see Vidafarnah-.
fra- prefix ‘before, forth’ (as prep., not found in OP): Av. fra, Skt. pra, Gk. тро, Lt. prü-fessus, Gt. fra-, pIE *pro ($33, $01, $75.II, $106, $132.3). Found with verbs а1$-, jan-, nay-, var-, má-, sá-, haj-; in nouns framdtar-, framānä-, Fravarti-; in phrasal adv. fraharavam; with suffixes and exten- sions, in fratama-, fratara-, fratara-, fravata, fraxa-.
fratama- adj. ‘foremost’: fra- + superl. suf- fix -lama-, Av. fratama-, Skt. -tama- (4190.11). fratama npm. DB 1.57; 2.77; 3.48f, 51, 74, 90°, 91.
fratara- ad). ‘prior, further’: fra- + comp. suf- fix -tara-, Av. fratara-, Skt. adv. pratardm, Gk. mpotepos (§106, 5190.11). " fratara ism. DNb 38 (Sen 249 needlessly takes as error» for frataram).
198
frataram asn. XPg 11; adv. ‘previously’ DB 3.26, A!Pa 21.
fratarta DB 3.26, incorrect reading for fra- taram (Cameron).
fral- vb. ‘ask, examine, investigate, punish’: Av. fras-, Skt. pra-, Lt. precor, pIE *prek-, with inchoative present, *prk-ske-, OP parsa-, Av. poro- saiti, NPers. pursdd, Skt. precháti, Lt. poscit. Cf. also ufrasta- ufrasta-. parsdémiy 1st sg. (830, $97, $130, $212, 5226.1) ОМ 19. aparsam Ist sg. imf. ($122, 5182.3, $212. $226.П) DB 1.22; 4.67, parsü 2d sg. imv. (8212, 5237.1) DB 4.38, 69. . frabiyaiš opt. pass. ($220, $228.П, $228.11) DNb 21 (not desid. fut. pass., as taken by Hz. Арі 167). pati- + parsa- ‘examine, read’ (on meaning, Bv. DSLP 31.2.71-2): patiparsühy 2d sg. subj. (§222.- II, $227.I) DB 442.  patiparsátiy subj. ($222.11) DB 4.48.
frafara- adj. ‘superior’: fra- + variant com- par. suffix -thara- seen in Av. fraéara- ($1491, 6190.11; Wb. ЖА 41.319; Bv. 33.2.150-1, 34.1.33-4, Hz. AMI 4.126-7, 8.3940, ApI 166-7), cf. superl. -thama- in Skt. prathamd- ‘first’. Cf. also uradara

=== KNT leaf 223 ===
1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 1; XPh 1; XE 1; XV 1; A!Pa 1^; A*He 1; A®Pa 1, 25. bagaha npm. ($10, $119, $172) DB 4.61, 63. bagünám gpm. AsH 7; DPd 1f; DPh 9; D8f 9; DSp 1°; DH 7; XE 2; XV 2; A’He 2. bagaibiš ipm. DPd 14f, 22, 24; DSe 50f°; DSt 8; XPb 28f; XPe 12f, 15; XPd 18; XPg 13f; XSc 5°; XV 26; A'Pa 23°. Вот ($42) ipm. D’8a 3. |
Bagábigna- sb. ‘Bagabigna’, a Persian, father of Hydarnes: Elam. ba-qa-pi-ig-na; from baga- ‘sod’ + d-bigna-, pte. in -na- of an unidentified verbal root, cf. perhaps Skt. bija-m ‘seed’ (575.1, $103.IV, $160.Ie, $243). Baglalbignah{ya} gsm. DB 4.84f.
Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
Bagayddi- adj. ‘Bagayadi’, seventh month, Sept.-Oct.: Elam. байцай$, АКК. tasritu. From baga- ‘god’, with vriddhi (8126, §165), + yad- ‘worship’, with lengthened vowel ($126, $165) and formative -2- (8152.1): ‘God-Worship Month’ (8159, $161.Ia), probably referring to Mithras, since Phl. and NPers. call this month Mihr
‘(Month of) Mithras’ (Justi, ZDMG 51.247; Bthl. AiW 952-3). Bágayádait gsm. DB 1.55.
bàji- sb. ‘tribute’: NPers. Баг; deriv. (§152.1, $165) of root seen in Skt. bhdga- ‘portion, dis- penser’, OP baga- ‘god’, the verb being Skt. bhájatt ‘apportions’, Av. bag-, РЫ. bäztän (§101, $122, $128, $126). Балт asf. DB 1.19; DPe 9; DNa 19; DSe 18; XPh 17.
batugara- sb. ‘drinking cup, saucer’: if genu- ine ($55.11; JAOS 56.215; Schaeder, БРАМ 1935. 489-96), from batu- ‘wine’ ($153.1; etymology un- certain, but Hz. ApI 114 quotes Bariaxy from Athenaeus, bk. xi, page 784a, as the Persian word for ‘phiale, cup’) + -gara- (8143.1) ‘devouring, drinking’ ($160.Ia), cf. Av. aspé.gard ‘horse-de- vouring’, Skt. aja-gará- ‘goat-swallower, boa con- strictor’, Gk. dnuo-Bédpos ‘people-devouring’, Lt. carni-vorus ‘flesh-eating’, from root in Av. gar- ‘devour’, Skt. girdit, Lt. vorat, plE *g*er-. Bv. J As. 228.233-4 suggests, and На. AMI 8.9-17, Ap! 118—5, accepts cognation rather with Skt. galati ‘drips’, gdlayat ‘pours’, as ‘wine-pourer’, cf. Lt. рате ‘pour (as an offering to the gods)’, and NPers. piyàüla ‘drinking cup’, from *pati-gdra-. bülugara пет. ($56.V) АЧ.
ba*d- vb. ‘hind’: Av. band-, Skt. bandh-, Gt. bindan, pIE *bhendh-. See also badaka-. basta (NPers. bäst) nsm. past pte. pass. (867, $85, 5120, $122, 5182.1, 52421) DB. 1.82; 2.75, 90; 5.26. basta apm. DB 3.88".
ba"daka- sb. ‘subject, servant’ (cf. König, Кыр 64): Phi. bandak, NPers. bändäh; deriv. (§146.1T) of OP *ba"da- ‘bond, fetter’, Av. banda-, Skt. bandhd-, to pIE root *bhendh- (OP ba"d-; $39, $75.11, $111, §122, 8132.1). badaka пет. DB 2.20, 30, 49f, 82; 3.13, 31, 56, 85; 5.8. badakā npf. DB 1.19.
Bábiru- sb. (Babairu- because of Pali Báveru-, MB Gr. $80) ‘Babylon’, a city (S56.III, $166); ‘Babylonia’, a province of the Persian Empire; by transfer, ‘Babylonian’: Elam. ba-pi-li, Akk. bab-ilu, bab-ilàni ‘gate of the god(s)’, Gk. Вав (§75.V, $107). See also Babirwiya-. Bahrus пет. DB 1.14, 80; DPe 10f; РМа 26; DSe 25; DSm 7°; XPh 22; as ethnic ($56.11), DN xvi, A?P 16. Babirum asm. DB 1.83f, 91 bis; 2.2, 3, 3f; 3.82, 84, 87; 4115, 30. \Babiraus absm. ($168, 6182.1) DB 2.65. Варта lsm. DB 1.78, 81;
200 OLD PERSIAN
2.5, 6; 3.79, 88, 92; 4.2; DBd 7f; DBi 11 (written Bab*raw, $22); DSf 33 as loc. with усій, 33 as abl. with Ласа (hardly a real abl., corresponding to Av. -aut despite Hz. AMI 3.55n, Kent ЈАО 53.16).
Bābirwiya- adj. ‘Babylonian’: deriv. ($144.- ПТ) to preceding. — Bábiruviya nsm. DB 1.77, 79; 8.81; 4.13; DSf 20. Babiruviyam asm. DB 3.86. Babiruviyé npm. DB 3.78; DSf 53f. Bäbiruviyä apm. DB 3.88.
bar- vb. ‘bear, lift up, esteem’: present stem bara-, Av. батат, N Pers. bard, Skt. bhárati, Gk. dpa, Lt. fert, Gt. batrip, pIE *bhere/o- (8213). See also ubarta-, uSabdri-, Gaubaruva-, bara-. bara^tiy 3d pl. ($122, 5232.1) DB 5.22f (written berety, 522); DNa 42. abaram Ist sg. imf. ($61, $75.III, 5226.1) DB 1.2
```


## [2026-09-14T00:51:07.680Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==223' KNT.txt | head -60",
 "description": "Print KNT leaf 222"
}
```


### [2026-09-14T00:51:08.700Z] TOOL RESULT

```
-. — fra&aram asn. XPf 26f, 37.
Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-ra-da, АКК. pa-ra-da-’ ; perhaps thematic noun- stem (§141) to fra- + *dà-, with vriddhi ($126), cf. Av. früd- ‘to further, increase’ (ТИМ. AiW 1012), but more probably hypocoristie to a com- pound name ($164.П1; Bthl. AiW 1018) of which the prior part was the participial stem to the same compound verb (§162), ef. Av. adj. fradat.qaéa- ‘prospering the household’, sb. frddaj.fsav- ‘Pro- moter of flocks’ (name of a divinity; Bthl. AiW 1013-4). Not with Sen 52 (fra- + OP *ad- ‘drive’, Av. azaiti, Skt. djati, Lt. agit), nor with Justi, INB 101 (fra- + had- ‘sit’, with loss of intervocalic -h-). Fraéda nsm. DB 3.12; 4.23; ОВ] 1.
framatar- sb. ‘master, lord’ (‘giver of judicial decisions’, ace. to Hz. ApI 150-4): fra- + root mā- + agent suffix -tar- (5154.1). framatéram asm. (§124.VI, $1861) DNa 7f; DSe 7; DSf 5; DE 11; XPa 5; XPb 11; XPe 5; XPd 8; ХР? 7f; XPh 6; XE 11; XV 9; A'Pa 8°; A?He 7. frama- ібгат (852.111) A?Pa 8.
framána- sb. ‘command’ (judgment, deci- sion’, acc. to Hz. ApI 144-50): РЫ. framán, NPers.
OLD PERSIAN
fürmán; fra- + mä- + suffix -nà- ($128, $1471), ef. Skt. pramána-m ‘measure, standard’. — framánà nsf. DNa 57; DNb 28; DSj 3°, framánáyà isf. DNb 37.
fravata adv. ‘forward, downward’: Phl. frót, NPers. fáród јато; from *frava-, extension of fra- as in Gk. rpõros ‘first’ from *proya-, + -tos as in amata (§191.1I; JAOS 51.204, 53.15; Bv. BSLP 30.1.59; hardly with Kénig, Burgbau 51; not identical with Skt. isf. pravátà ‘downhill’). DSf 23f, 28.
Frovartz- sb. ‘Phraortes’, a Median rebel: Elam. pir-ru-mar-t-18, Akk. pa-ar-ti-mar-ti-1§ Gk. Ppadprys: identical either with Av. frava&i- ‘guar- dian angel, soul’, from fra- + var- ‘protect’ + -ti- (S31, 8152.11) as ‘Protection’, or with Av. fraoroti- "Siehbekennen zu’, from fra- + var- ‘choose (re- ligiously)’ + -й- (Bthl. AIW 991, 992, 976; Nyberg Rel. 334-5, prefers second view); as man’s name, probably liypocoristic of a longer compound ($164.1). — Fravarti$ пата. DB 2.14, 66, 71, 73; 4.18; DBe 1f. Fravartim asm. DB 2.17. Fravar- tas gsm. DB 2.69, 93.
fras- vb., see јтаб-.
fraša- adj. ‘excellent’ (‘tauglich’, König Burg- bau 48, Brd. АКМ 39.87): Av. frasa- ‘directed toward, useful’, formed on adv. fraša to frünk-, Skt. adv. praca to ртайс-, from pra- + añe- (Bthl. AiW 1006-7); the irregular -3- for -s- of Sy- may be a contamination of *frasa- and *frasya- (otherwise ВБ. IF 2,266-7; borrowed from Aves- tan aec. to Hz. ApI 162). Hz. ApI 156-65 (recant- ing derivation from fra- + záy- ‘shine’, ‘brilliant’, AMI 3.1-11) takes as deriv. of pra-, through an idiom of racing or fighting, as 'extra (certamen), hors (concours)’, and therefore "incomparable, su- preme’. Cf. also Hz. RHRel. 113.26; Bailey, BSOS 6.595-7; Kent, Lg. 15.169. — frasam nsn. DSa 5, DS] 6 (see frasta-, for reading). frasam asn. DNb 2; DSf 56, 56f; DSo 4^; DSs 1°.
frašta DSa 5, DS] 6: discussed by Bv. ВІР 30.1.63-4, Gr. $103, Gray AJP 53.67, Brd. WZKM 39.20-1; but fra$am @adaydlary and not frašta ðadayämaiy ($54.11) should be read in both pas- sages (Hz. AMI 3.9-10, ApI 156-8). See under frasa-.
(mu. em lere Am ee шшш. ште у. mi ease e +
LEXICON 199
fraharavam, phrasal adverb ($191.]II), ‘in all’: fra- ($1401) + asn. haravam with variant orthography ($22, $26), to haruva-. DB 1.17.
. baug- vb. ‘free’: Av. baog-, NPers. boxtén; in Attydbausna-, Bagabuxsa-.
Düxtri- sb. ‘Bactria’, a province of the Persian Empire: Elam. ba-ak-&-18, ba-ik-tur-ri-i$, Akk. ba-ah-tar, Gk. (nt. pl) Béxrpa (§9.1, $79, 6103.111). OP %-stem, for older 7-stem (8152.II), seen in Av. báxói. — Büziri$ nsf. DB 1.16; DPe 16; DNa 23; DSe 22°; D8m 9°; XPh 21. Ваг- triyd \sf. DB 3.13f, 21. Baztriya absf. DSf 36.
bag- vb., see under baga-, bàji-.
baga- sb. ‘god’: Av. baga- ‘lot, good fortune’, Skt. bhdga- ‘dispenser (of good fortune)’, Gk. -paryos ‘eater’, OCS bogi ‘god’, pIE *bhago- ($101, $122, 5143.1, V, VI); ef. Hz. ApI 105-10. See also Bagábigna-, Bagabuxsa-, Bagayddi-, bà. рада nsm. AmH 6; AsH 6; DNa 1; DNb
```


## [2026-09-14T00:51:21.775Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"frābara\\|frabara\\|fräbara\\|frābar\" KNT.txt | head -20; echo ---; awk 'BEGIN{RS=\"\\f\"} NR==224' KNT.txt | head -20",
 "description": "Find frabara in Kent"
}
```


### [2026-09-14T00:51:22.696Z] TOOL RESULT

```
1056:OP maub-, Adiyabausna-, gaibà-, frabara-, mitah-,
3062:DZe ЗЕ hya Dàrayavahau$ X. Syd xsacam frabara 4
3072:I. The enclitic pronouns are attached to the first word of their sentence or clause or phrase, even though this be шй ‘and’: DB 1.25 Aura- mazdü-maty upastém frabara ‘Ahuramazda bore me aid’; РР} 8 tya-mary Auramazdà frübara ‘(the kingdom) which Ahuramazda conferred upon me’; DPh 9f тат Auramazdà pütuy utä-maiy ийат ‘me may Ahuramazda protect, and my royal house’. But the phrase vašnā Auramazdaha does not count in fixing the position of an enclitic: DB 1.13f vaina Auramazdàha адат-&ат х$йуабтуа Gham ‘by the favor of Ahuramazda I was king of them’; except in two partly restored passages, see under IIT. An enclitic in a dependent clause is sometimes attached to wd preceding a conjunc- tion or relative: DB 4.781 utd-tazy yàvà tauma ahatiy ‘and as long as strength shall be unto thee’; XPa 15 ша-тату tya рий akunaus ‘and what my father built’, but also XPa 19f шй tya-maiy pica kartam ‘and what was built by my father’; DNb 28f yabd-maiy tya kartam vatnühy ‘when thou shalt see what was built by me’. An attributive en- clitic genitive normally precedes the word which it modifies (cf. §309); but the meaning sometimes governs the position, as in Аа 3 apan?yüka-ma ‘my grandfather’s grandfather’, A*Sa 4 [n*yd|kama (for -am-ma, §138.1) ‘my grandfather’, both with am for -miy = -maiy (852.D. The abl. -ma is found only in hacd-ma ‘from me’, standing any- where in its clause. These formulations are vio- lated in three heavily restored passages, but the available space and the other versions favor these restorations: DSf 20 [ava исйтатату ( = -am-maty) akunaus} ‘that he made successful for me’; DSf 28 [hacd-cily ditradasa [arjanam-sary abariya) from afar its ornamentation was brought’; DNb 54f tya partalm-taty as]fiy ‘what is eommunicated to thee’ (this restoration is highly conjectural).
3471:12 dha : adam : хддёуайуа : amiy : Auramazdā :xšaçam : mana: frabara : 6
4098:8 тй: tyamaiy : Auramazda : frabara 9 : һуа : mafista : bagindm : mam : Au 10 ramazda : pituv : utamaty : vidam
4369:6 kunautiy : mand : haudis : frabara : mam : Ай 7 ramazdà : pdtw : uta : tyamaiy : kartam :
---
1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 1; XPh 1; XE 1; XV 1; A!Pa 1^; A*He 1; A®Pa 1, 25. bagaha npm. ($10, $119, $172) DB 4.61, 63. bagünám gpm. AsH 7; DPd 1f; DPh 9; D8f 9; DSp 1°; DH 7; XE 2; XV 2; A’He 2. bagaibiš ipm. DPd 14f, 22, 24; DSe 50f°; DSt 8; XPb 28f; XPe 12f, 15; XPd 18; XPg 13f; XSc 5°; XV 26; A'Pa 23°. Вот ($42) ipm. D’8a 3. |
Bagábigna- sb. ‘Bagabigna’, a Persian, father of Hydarnes: Elam. ba-qa-pi-ig-na; from baga- ‘sod’ + d-bigna-, pte. in -na- of an unidentified verbal root, cf. perhaps Skt. bija-m ‘seed’ (575.1, $103.IV, $160.Ie, $243). Baglalbignah{ya} gsm. DB 4.84f.
Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
Bagayddi- adj. ‘Bagayadi’, seventh month, Sept.-Oct.: Elam. байцай$, АКК. tasritu. From baga- ‘god’, with vriddhi (8126, §165), + yad- ‘worship’, with lengthened vowel ($126, $165) and formative -2- (8152.1): ‘God-Worship Month’ (8159, $161.Ia), probably referring to Mithras, since Phl. and NPers. call this month Mihr
‘(Month of) Mithras’ (Justi, ZDMG 51.247; Bthl. AiW 952-3). Bágayádait gsm. DB 1.55.
bàji- sb. ‘tribute’: NPers. Баг; deriv. (§152.1, $165) of root seen in Skt. bhdga- ‘portion, dis- penser’, OP baga- ‘god’, the verb being Skt. bhájatt ‘apportions’, Av. bag-, РЫ. bäztän (§101, $122, $128, $126). Балт asf. DB 1.19; DPe 9; DNa 19; DSe 18; XPh 17.
batugara- sb. ‘drinking cup, saucer’: if genu- ine ($55.11; JAOS 56.215; Schaeder, БРАМ 1935. 489-96), from batu- ‘wine’ ($153.1; etymology un- certain, but Hz. ApI 114 quotes Bariaxy from Athenaeus, bk. xi, page 784a, as the Persian word for ‘phiale, cup’) + -gara- (8143.1) ‘devouring, drinking’ ($160.Ia), cf. Av. aspé.gard ‘horse-de- vouring’, Skt. aja-gará- ‘goat-swallower, boa con- strictor’, Gk. dnuo-Bédpos ‘people-devouring’, Lt. carni-vorus ‘flesh-eating’, from root in Av. gar- ‘devour’, Skt. girdit, Lt. vorat, plE *g*er-. Bv. J As. 228.233-4 suggests, and На. AMI 8.9-17, Ap! 118—5, accepts cognation rather with Skt. galati ‘drips’, gdlayat ‘pours’, as ‘wine-pourer’, cf. Lt. рате ‘pour (as an offering to the gods)’, and NPers. piyàüla ‘drinking cup’, from *pati-gdra-. bülugara пет. ($56.V) АЧ.
ba*d- vb. ‘hind’: Av. band-, Skt. bandh-, Gt. bindan, pIE *bhendh-. See also badaka-. basta (NPers. bäst) nsm. past pte. pass. (867, $85, 5120, $122, 5182.1, 52421) DB. 1.82; 2.75, 90; 5.26. basta apm. DB 3.88".
ba"daka- sb. ‘subject, servant’ (cf. König, Кыр 64): Phi. bandak, NPers. bändäh; deriv. (§146.1T) of OP *ba"da- ‘bond, fetter’, Av. banda-, Skt. bandhd-, to pIE root *bhendh- (OP ba"d-; $39, $75.11, $111, §122, 8132.1). badaka пет. DB 2.20, 30, 49f, 82; 3.13, 31, 56, 85; 5.8. badakā npf. DB 1.19.
Bábiru- sb. (Babairu- because of Pali Báveru-, MB Gr. $80) ‘Babylon’, a city (S56.III, $166); ‘Babylonia’, a province of the Persian Empire; by transfer, ‘Babylonian’: Elam. ba-pi-li, Akk. bab-ilu, bab-ilàni ‘gate of the god(s)’, Gk. Вав (§75.V, $107). See also Babirwiya-. Bahrus пет. DB 1.14, 80; DPe 10f; РМа 26; DSe 25; DSm 7°; XPh 22; as ethnic ($56.11), DN xvi, A?P 16. Babirum asm. DB 1.83f, 91 bis; 2.2, 3, 3f; 3.82, 84, 87; 4115, 30. \Babiraus absm. ($168, 6182.1) DB 2.65. Варта lsm. DB 1.78, 81;
200 OLD PERSIAN
2.5, 6; 3.79, 88, 92; 4.2; DBd 7f; DBi 11 (written Bab*raw, $22); DSf 33 as loc. with усій, 33 as abl. with Ласа (hardly a real abl., corresponding to Av. -aut despite Hz. AMI 3.55n, Kent ЈАО 53.16).
Bābirwiya- adj. ‘Babylonian’: deriv. ($144.- ПТ) to preceding. — Bábiruviya nsm. DB 1.77, 79; 8.81; 4.13; DSf 20. Babiruviyam asm. DB 3.86. Babiruviyé npm. DB 3.78; DSf 53f. Bäbiruviyä apm. DB 3.88.
bar- vb. ‘bear, lift up, esteem’: present stem bara-, Av. батат, N Pers. bard, Skt. bhárati, Gk. dpa, Lt. fert, Gt. batrip, pIE *bhere/o- (8213). See also ubarta-, uSabdri-, Gaubaruva-, bara-. bara^tiy 3d pl. ($122, 5232.1) DB 5.22f (written berety, 522); DNa 42. abaram Ist sg. imf. ($61, $75.III, 5226.1) DB 1.2
```


## [2026-09-14T00:51:30.825Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bear, lift up, esteem\" KNT.txt; awk 'NR>=3200 && NR<=3210' KNT.txt | head -5; echo ===; grep -n \"esteem\" KNT.txt | head",
 "description": "Locate Kent bar- entry line"
}
```


### [2026-09-14T00:51:31.855Z] TOOL RESULT

```
Exit code 1
5730:bar- vb. ‘bear, lift up, esteem’: present stem bara-, Av. батат, N Pers. bard, Skt. bhárati, Gk. dpa, Lt. fert, Gt. batrip, pIE *bhere/o- (8213). See also ubarta-, uSabdri-, Gaubaruva-, bara-. bara^tiy 3d pl. ($122, 5232.1) DB 5.22f (written berety, 522); DNa 42. abaram Ist sg. imf. ($61, $75.III, 5226.1) DB 1.22; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54, 60, 68, 86, 97^; 3.6, 17, 37, 45, 62, 67 (written ar?r^, 854.11), 87; 4.61, 62; DNa 50f; DSf 19°, 32; XPh 33, 45. abara” 3d pl. imf. ($10, $40, $84, $106, 8232.1) DPe 10; DSe 18°; DSf 34. aba- raha” 3d pl. imf. ($10, $218, $282.11) DNa 19f; XPh 17 (written орт, §54.1). abara"tà 3d pl. imf. mid. ($10, $236.II) DB 1.19. abariya imf. pass. (535.1, $220, $228.IT) DSf 23°, 31f, 35, 36, 38f, 40, 48, 45. abariya" 3d pl. imf. pass. ($220, 8232.11) DSf 41, 47.  baratuv imv. (5237.П) AmH 11^; DPd 14; DSk 5. аталаш inf. ($238) DNb 41.
49: 249D bis; 249E; 261.11
50:26111; 271; 279.11; 283; 288; 3014; 310.IV; 311.IV
51: 261.1; 279.1IIb; 302b
52: 278.1IId; 279.IITb; 292b; 302b; 305e; 311 bis; 311.V
52f: 249C; 302e
(eval):1: == not found
```


## [2026-09-14T00:51:34.182Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5731,5740p' KNT.txt",
 "description": "Print lines after Kent bar- entry"
}
```


### [2026-09-14T00:51:34.226Z] TOOL RESULT

```
à + bar- ‘perform’: dbaratiy ($218, $228.1) DNb 25. Cf. also Hz. Ар] 110-1, who refers to à-bar- certain other forms listed above as augmented forms of uncompounded bar-.
pati- + à + bar- ‘bring back, restore’: райуй- baram Ist sg. imf. DB 1.68 (but -à- perhaps only by influence of pardbartam, JAOS 62.275; 558, $206c).
para + bar- ‘bear away, take-away’: pardbara imf. DB 1.71, 96. pardbartam nsn. past pte. pass. (§242.1) DB 1.62, 67f.
pari- + bar- ‘protect, preserve’ (cf. Hz. Ар 112-3): paribarümiy Ist sg. (8226.]) DNb 17. paribarühy 2d sg. subj. ($27, $136, §222.IT, 4227.1) DB 4.78; paribaráh*-di$ (827, etc.) DB 4.74. pari- barā 2d sg. imv. (5237.1) DB 4.72, 88.
fra- + bar- ‘proffer, grant’: frábara imf. AmH 7; AsH 9; DB 1.12, 25, 60; DPd 3f, 7f; DPh 8; DNa 33; DSf 11; DSm 3°; DSp 2°; D8s 6; DZc 4; DH 7; A’He 18f, 20.
bara- sb. ‘bearmg, bearer’: Av. -bara-, Skt. -bhara-, Gk. -фороѕ, pIE "bhoros ($32, $122, $1431, ҮТ), to root bar- ‘bear’, in aritibara-, takabara-, vacabara-; also bāra- ‘borne by, rider of’, with vriddhi (8122, $126, 5148.1), in asabdra-, ef, usabüri-. See Hz. Ар] 95.
bard- vb. ‘be high’: Ау, baraz- ‘high’, baraz- ant- ‘lofty’, NPers. burz ‘high’, Skt. brhánt- ‘lofty’, OHG berg ‘mountain’, pIE *bhergh-; in Bardiya-, barsan-, probably in brazman-.
Bardiya- sb. Smerdis’, brother of Cambyses ($16411): Elam. bir-h-ia, АКК. bar-zi-ia, Gk. Урёрӧ ($29.02, $30). Репу. (§144.1V) of OP bard- ‘be high’ (575.11): ‘The Exalted’. Bardiya пет. DB 1.30, 32, 39, 52f; 3.25, 35, 54; 4.9, 27, 82; DBb 4f; DBh 5. Bardiyam asm. DB 1.31 bis, 51.
barSan- sb. ‘height, depth’ (S81): Av. barazan- .
(ВМ. AiW 950); deriv. of OP bard- (575.1, $155.1; Scheil 21.26; Konig, Burgbau 51; Hz. AMI 3.57; Bv. Gr. $812; Kent, JAOS 51.204, 99.15). bar$nà ism. (806, $120) DSf 26, 26f.
```


## [2026-09-14T00:51:43.726Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 202 203 204 205; do echo \"=== HRN leaf $n (printed ~$((n-21))) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((n+1))\"'' HRN.txt | head -40; done",
 "description": "Print Horn leaves 202-205"
}
```


### [2026-09-14T00:51:44.753Z] TOOL RESULT

```
=== HRN leaf 202 (printed ~181) ===
— 181 —
811. ferüx Vorwärts, aufwärts; offen' etcJ).
aw. frq^ Vorwärts' (schw. St. ^frac-^ vergl. N. pr.
FrOdi/a-); phlv. fräd- (päz. fräz^ frfl^); ai. pränc-
(schw. St. präC') ^vorwärts*.
oss. räzäi Von vorn* etc. (210).
812. feramöS Vergessend; Vergessenheit', ferämus^ fera-
muSt^ fer(a)mösiden (Vis und RämTn, S. 50 V. 13).
ai. pra + |/';/?«rs-, ////ifya^c Vergessen' ; y\\]w , framös
bezw. farmös^ framöst^).
bei. samusag, samDsay, n. samusay^ Samösay Ver-
gessen (361), mit anderem Pracfix.
813. ferbih, ferheh^ ferhl (d. i. "^ferhiQi)) 'fett'. Vergl. np.
pih (No. 365).
aw. frapi^wa- 'Voizug, first-rate' (Geldner, Ve-
dische Studien 11, 17iJ)'^); phlv. frapili hi^zw. farpfh;
ai. prapitüd' (vergl. Geldner a. a. (). 155 folg.).
LW. wa;^. farhl^ sar. farhe,
Jüd.-pers. HO*!^ (Is. 17, 4) geht auf ein ap. *//(/-
2)itU' zurück.
814. ferjätn *Ende\
ap. ^frajäma- {{^gani- 'gehen*); \)\\\v, frajäm bezw.
farjam 'Ende', frajämtnltany vergl. fraj(a)ftan (AV.,
jung in Kolophonen. Siehe No. 113).
815. ferxane V^eise, gelehrt*, ferzanegl.
ai. pra + [/^./aw- , jafiäti- 'erkennen , verstehen' ;
phlv. frazänak bezw. farzänak,
Vergl. dänisten (ar. l/iaw-), No. 534.
816. ferzend 'Spross'. sowohl *Sohn* als auch 'Tochter (N'is
und Kämln, S. 22 V. 4, 5 v. u.).
aw. frazainti' 'Nachkonimenschalt*; phlv. farc^attd
bezw. frazand.
*) Vergl. Dar mestcter, Et. ir. IT, 112 foli^g.
*J Nach den arm. LW. hraman^ hrasak, hrahany zu sclilicsson,
scheint im Pehlevi noch /ra-, nicht schon far- gesprochen zu sein.
Das Päzend lässt beide Möglichkeiten offen.
'j Justi' Thema /raj9J/M- *Füllc' rauss also fallen.
=== HRN leaf 203 (printed ~182) ===
- 182 -
817. fiv'i stallen 'schicken*.
ap. *fra + [^sta-, vergl. a.i. pra -\- l^stho- (Causat.)
'entsenden, entlassen'.
vergl. Sit'/, (ififcwul 'senden'; bei. sastay ^ n. sastay
(363).
818. ferseng 'Parasange', arab. LW. farsax»
ap. 7Taf)f((r(iyy7j; phl. frasang bezw. farsany (Men.,
Bund.).
819. firisfe 'Bote.
phlv. firisfak (Dat. d. 3, 15); chald. LVV. vXpnonp
(das de Lagarde fälschlich = np. pereste setzt) und
NOPIDI.?« (Ezra 4, 9), Hoffmann, Zeitschr. f. Assy-
riologie II, 55 (danach Ezra 5, 6 und 7, 6 zu emen-
diren).
Zu np. ßristäden (No. 817), vergl. skr. prasthita-
aufgebrochen, der sich aufgemacht hat'. Ein aw.
^frcfsfa- (aus ar. *prasth'td', vergl. KZ. 25, 56) ist
etwa als Grundform anzunehmen ^).
^[()bi. ffriste, firzste (AM., d. l ßreste) 'Bote; Engel*.
skr. presita- {pra + |/es-, Causat.) 'gesandt', vergl.
ap. fräisayam, fräisaya ; arm. LW. hresfak 'Engel'.
bei. LW. piristay (202).
Die Etymologie stammt von de Lagarde, zuletzt
Semitica I, 67.
820. fermän 'Befehl'.
ap. framana- 'Befehl'; phlv. farman bezw. framm,
arm. LW. hramcm (davon hramanem), talm. }0*)n.
Allgemein entlehnt.
821. f ermüden 'befehlen', Praes. fermäy-em^ fermayis,
fra -f [/^ma-y vergl. ap. framätar- 'Gebieter ; phlv.
farmütan bezw. framiitan^ framät, framäy(i)sn,
822. fernüs 'töricht, nachlässig, verschlafen; Thorheit'.
ai. pra -f [/^nag- 'verloren gehen, verschwinden'.
*) Justi (Glossay 8. v. asta-) hat die Etymologie fra -|- astO' auf-
gestellt, doch giebt es ein aw. asta- 'Gesandter' nicht, und l/^as- (ai.
ag-, agnöti) heisst nicht 'senden*.
=== HRN leaf 204 (printed ~183) ===
- lS:i -
skr. pranä^U' Mas Ausgohün, Aufliören, Verschwinden'
(Nüldeko, mündliche Mitteilung).
\. fervar 'Soninierhaus, Veranda.
aw. *fravärana-^ vergl. fravüra- (?) ; phlv. fravär
(de Lagard e, Beitr. z. altb. Lex. 55).
Die Bedeutung von aw. fravara- ist unsicher (wie
de Lagarde übersetzen will, sagt er nicht). ^^, fervar
setzt ein ^fravarana- mit gleicher oder ähnlicher Be-
deutung wie *up(nrivara7ia- (No. 210) voraus. Übrigens
kann fervar auch die arabisirte Form von bervür und
phlv. fravar nur Transscription sein (vergl. S. 68
Anm. 1).
L furöyteu, firöyten^) Verkaufen', Praes. furös-em,
firöslden.
Semn. behlr\üsliin; Kas. Z. Impt. hefrös.
aw. '*fra + 1/ oa/s- (Erweiterung von oac- wie ha/s-
von haC') 'ausrufen, ausbieten*; phlv. frö/tan,
kurd. LW. frütm, difrüsim 'verkaufen'; af/. prölal,
prövul; bei. savaskay, söskay 'verkaufen', p. p. §ava/fa
(364).
Die Etymologie stammt von Justi, Kurdische
Grammatik, 190; bei. sdjva/fa ist eine der durch-
sichtigsten Formen. Durch häufige Verbindung mit
np. /enden ('kaufen und verkaufen*) entstanden die
dialektischen: g. herCLtmün {heridmün 'kaufen*), /urusteti,
Käs. K. /orölmün,
K firöd, fiiröd^ firö^furö 'hinunter, unten', furööTn 'unterer*
(AM. S. 265 Zeile 7).
phlv. fröt,
ai. pravät- abschüssige Bahn', pracdtä 'beigab, ab-
wärts*; firöd setzt ein "^praufd (schw. St.) voraus
(Barthol omae, briefl. Mitteilung)'').
') Sähu. IIT, 1662 V. 2904 reimt ftiröxt auf uedöxt
^) Darmesteter (At. ir. II, 154) hatte an aw. dnnma.fraotö
13, 14) '(Iriving down the clouds* gedaclit; die Neuausj^abe hat
ma.frutö* Eine andere, ebenso unwahrsclieinlicho liltymologie stammt
Goldiger, KZ. 25, S. 515 Note 12 (np. furöd ^ aw. fraonf).
=== HRN leaf 205 (printed ~184) ===
— \Si -
826. ftHh viel, mehr.
aw. vergl. fräyäo, fraesta-; phlv. fr ah, f rahist
(Päz. freh^ frehest), ursprünglich freh^ vergl. freh[dätär
(AV.).
Die Aussprache ßrih (nicht fireh) bezeugen die
Keime der beiden bei Vullers s. v. mitgeteilten
Verse {bih und girih). Ich stelle das Wort zu den
von Andreas erklärten bih, kih, mih (No. 241).
827. ferl *lieb, schön .
aw. frya- geliebt, Freund*; ai. pnyä-,
828. feryäd *Hilfe; Hilferuf, Klage.
aw. fraöäia- ^Gedeihen, Förderung' (yt. 13, 68);
phlv. frayät bezw. fradät 'Hilfe*.
Die mittelpersische Bedeutung *Hilfe* findet sich
auch noch im Neupersischen, z. ß. AM. 43 Zeile 6, 82
Zeile 1 V. u., Öähn. I, 126 Vers Uli (NB. wohl un-
echter Vers).
LW. kurd. af/. feryad-, bei. paryat 'Geschrei* (199).
Anders Fr. Müller, WZKM. 5, 353.
829. fireften 'betrügen*, Praes. fireb-em , ßreb 'Betrug*,
ßreftär, JTJKSnE^ (Jer. 20, 7).
ai. pra + [/"rep- 'anschmieren, betrügen', vergl. rip^
'Betrug, ripü' 'Betrüger ; phlv. freftan^ frepet^ f^^P^
frep(i)sn, freftär.
oss. d. fälewun, t. fäliwin 'betrügen* (271). Sar.
rof-am hat noch die Bedeutung 'beschmieren' bewahrt.
830. fe^, fuy 'Götterbild (Geliebter, Geliebte)', fuyistün
V
'Harem* (Sahn. II, 532 V. 198), fuyäk 'töricht', fuyvare
sprachlos, vergl. Fayfür (Seite 71 Note 1).
ap. baga- 'Gott*; aw. baya-; phlv. bag]baxt (ge-
schrieben baW) ; ai. bhdgha-.
Die echt persische Form hat sich im Np. nur in
Ba/däd erhalten, das / ist eine Arabisirung.
```


## [2026-09-14T00:51:55.727Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 81 82 83; do echo \"=== HRN leaf $n (printed ~$((n-21))) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((n+1))\"'' HRN.txt | head -45; done",
 "description": "Print Horn leaves 81-83"
}
```


### [2026-09-14T00:51:57.325Z] TOOL RESULT

```
=== HRN leaf 81 (printed ~60) ===
— 60 —
261. Mm 'Nase.
Semn. vlm; mäz. v^it,
aw. va^nä' Nase' (Y. 9, 11 (35), Darmesteter, Et.
ir. I 57); phlv. venik (Bund., AV.), bEmk (AV.).
kurd. hen *Nase, Geruch' (H.-Sch.); bei. gin *Atem,
Leben (109) (?).
Fr. Müller (WZKM. 5, 260) stellt dazu phlv. mi,
(ZP61. 8, 3) 'Hauch* und nimmt als dessen Grundform
*vayana' an.
262. bever 'tausend'.
äw. ba^vare 'tausend'; phlv. bevar.
oss. d. beurä, t. birä Viel, sehr, lange (61).
263. beve Wittwe'.
Käs. vJgd^ vU (neben bivä^ bwe),
ai. vidhdvä' *Wittwe'; phlv. vepak d. i. vBvak; lat.
oidiia; got. viduvö,
oss. t. idäj *Wittwe' (aus *vidüä'j), von Stackel-
be rg (briefliche Mitteilung).
264. beyoj^beyök 'Braut*, :V2 (Jer. 16, 9).
ai. <^ergl. vadhü- 'Braut' ; kurd. buk.
P.
265. />flcZ 'Schützer, gewaltig ^).
27äd setzt ein ap. ^päta- (Suffix ta- wird bekannt-
lich auch gelegentlich zur Bildung von Nom. ag. ver-
wandt) Schützer voraus; ap. "^pätar- (aw. pätar-, ai.
jmtdr-) müsste im Np. als pädar erscheinen 2).
§i/n. päda 'Hirte*.
*) In den Wörterbüchern finde ich keinen Beleg; aber Sadi hat
in seinem Commentar zu Häfiz, Ghazel No. 11, Beit 2 einen Vers
Enveri's (ed. Brockhaus, S. 56). Er erklärt das Wort durch türk.
ulu 'gross*.
*) Bartholomae wiU nach brieflicher Mitteilung *pcUas 'schützend*
lieber als neuen Nominativ zu päJtam d. i. pät-am (Brugmann, Grund-
riss II, 367) auffassen.
=== HRN leaf 82 (printed ~61) ===
- 61 -
265^" pädäs, pädes (Vis und Rämin) 'Vergeltung', padast,
pädosn,
phlv. pätdah(i)sn {paiti -f dah(i)sn), päz. pädaisn^
pädaän 'Vergeltung'.
Aus dem Pärsismus übernommenes Wort. Vergl.
np. dasen (No. 528).
266. pädiSäh *König'.
ap. "^pati/Säyadiya-; phlv. päta/sä^ bezw. päta/sah
(übersetzt im Kommentar aw. x^<^y(^^^<^' Vermögend,
erlaubt ; Herrscher) ^).
267. päde 'Heerde'^), padehan.
ap. aw. skr. päta- 'beschützt, bewahrt'.
268. pädyäb, pädyaw rituelle Waschung.
aw. paüyäpa- ; phlv. pätt/äp, pOtyapih,
Rituelles Pärsenwort.
269. pädyävend (i:ixnx5?, Is. 1, 31) 'kräftig'.
phlv. pätyavand 'kräftig'.
paiti + l/^««?-, aw. *paityavanU (Part. Praes.).
270. pär 'das vergangene Jahr', pärsal^ parm.
skr. vergl. panit 'im vergangenen Jahre' ; arm. heru
Vergangenes Jahr' (H. No. 167).
kurd. (LW.) par\ af/. parös-; oss. d. fdi% t/aron
'im vorigen Jahre' (277) ; bei. pari, n. pän (293) ; wa;^.
pardy sar. parvus (vergl. gr. nigvöi).
Ap. paruva- 'früher (aw. paurva-) ist schon im
Pehlevi aufgegeben worden; np. pärav alte Frau' ist
nicht belegt.
*) Zu phlv. pata^sa, np. padisäh als t. t. beim Ehesohluss vergl.
West, Pahlavi Texts» 142 Note 10.
2) FR und F J haben als Beleg folgenden Vers des Ferälädl
(so nach Eth6, Morgenländisohe Forschungen, während FR und die
Strassburger Handschrift des FJ Ferälävl, Salemann, SF Feräläri
schreiben), Metrum: Xeflfi
mäde-gävän-t päde-es her yeh
mh^perver huved cn hirmäyün
=== HRN leaf 83 (printed ~62) ===
— 62 ~
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
bei. LW. palayag^ pälenay 'seihen, worfeln, reinigen'
(292).
^j Vergl. Geldner, Studien I, 16. Bartholomae (briefliche
Mitteilung) verweist mich aber auf aw. parendi- (Indog. Forsch. I, 184)
mit der Grundbedeutung 'Füllser.
```


## [2026-09-14T00:52:19.131Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v1_pages.txt | head -3; echo ---; grep -n \"پارسال\\|پارينه\\|پارینه\" BQT_v1_pages.txt | head -20; echo \"=== parir ===\"; grep -n \"پرير\\|پریر\" BQT_v1_pages.txt | head -20",
 "description": "Grep Borhan vol1 for parsal, parina, parir"
}
```


### [2026-09-14T00:52:19.216Z] TOOL RESULT

```
---
3115:میخورد وچرا میکند» بهمین‌طریق تاچپارسال. بعدازآن برمی‌آید ومیگربزد وحکمت درین‌آفث
23088:۹ مح ۱*. ۱ رك : لت‌نامه ویازیر. .  .‏ ۷ 2 در: پارسال» پارینء قس مانسکربت
=== parir ===
```


## [2026-09-14T00:52:23.208Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=23090{if(/\\f/) c++} END{print \"leaf idx:\",c}' BQT_v1_pages.txt; sed -n '23070,23110p' BQT_v1_pages.txt",
 "description": "Locate BQT v1 line 23088 context"
}
```


### [2026-09-14T00:52:24.274Z] TOOL RESULT

```
leaf idx: 564
اف بر وزن خار ۰ بمعنی سال گذشته
و پیش ازین باشد ۷ - و «خفف پاره هم هسنت -
و چرم دبافت کرده دا نیز کویند - و بمعنی
پرواز و پرش هم‌آمده است؛ چه پاریدن بمعای
بر بدن باشد 3
پار او - بارای بالف کشیده وبواو زده .
زت بر و مرژال را گونند - و نام بلو کیت از
پار د۸- بضم دال وسکون‌هيم» رانگی‌را
چاروا دوزند وبریس ران چارو! اندازند » وی
کوبند چرمی باشد که بریس زین اسب بندند
وبرزیر دم‌اسب اندازند. واين اسح است .
پار س - بسکون الث بروزن و حعنی
۳ هس یابه ۹ ۳ ۰
۴ رك : یادیاو .
۶ با 2202۷ . وآن مثل وضوست تزد مسلمانان. زرتفتب ی که میخواهد پادباب کند نضت
بك «خشنوتره اهورهه مزداو» (بخشنودی اهور مزدا) م‌خواند ویس از آن یکبار « اشم وهو...»
میسراید . آنگاه روی.ودستها وپاهای خودرا میشومد» از آن پسکشتی نو مبکند و بترئیب عقرد
کمربند خود می کتاید ودعای مخصوصآرا میخواند وباردیگر پدورکمر می‌بندد. «خرده اوسنا
۹ مح ۱*. ۱ رك : لت‌نامه ویازیر. .  .‏ ۷ 2 در: پارسال» پارینء قس مانسکربت
۸ ( در سال گذشته ) ؛ ارمتی 0۵ ( سال گذشته ) , کردی ۵ . افنانی ۳۵۲۵5 ,
استی 18۲8 ۰ 18808 ( در مال پیش ) » وخی ۳8۳0 ۰ سریکلی 2۳۷۷15 ( قس بونانی
61 ) بارسی باستان2 ۳8۲۷۷ (سابقا), اوستا 8211۲۷2 « اسشق ۲۷۰ *. ۸ - در
پارسی باستان (کتیبه‌های هضامنشی) 2752 : ام مکی از اقوام ابرانی مقیم جذوب ایران که نام
بقبه درصفحةً ۳۰
۵ پارت - پارسی‌باستان ۳۵۲4118۷2 مقر قوم پارت ( خراسان قدیم )- خود قوم پارت
ازاقوام ابرانی؛ کلم بهلو وهلوی (ه .م) ازین دام مشتق است.
۵ پارتی - منسوب بپارت , ازفوم پارت- زبان پارتی زبان پهلوی اشکانی را گونند .
رك : پهلوی ورد : مقدمهٌ آقای پورداود برهمین کتاب .۳9
۱ با نگ - بسکون الت بی وزن
آپرنگ » به‌نی امک ات و آن چیزی
باشد که در يك که ترازو نهند نا با کفهٌ دمگر
برایر شود .
وصفاهان و کرمان و بزد را نیز گفته‌اند و نام
جانورست شکاری کوچکتر ازپلاک واورا بوزهم
منگویند- ونام پس پهلوبن سام‌هم هست. گویند
که اصطخر بناکرد؛ اوست . ۱
یدسا «بارابع بالف کنیده. پرهیز کار
و دور از معاصی و ذمايم را کویند ٩‏ -
و بمعنی پارسی هم آمده است وجمع آن‌پارسیان
بار سه بقتح رابم‌بروزن دلوچه. بمعنی
کدابی باشد . ۶
```


## [2026-09-14T00:52:41.779Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پيرار\\|پیرار\\|پرندوش\\|پرندوشين\\|پرندوشین\" BQT_v1_pages.txt | head -20; echo \"=== farzane v3 ===\"; grep -n \"فرزانه\\|فرزانك\\|فرزانک\" incoming/BQT/BQT_v3_pages.txt | head -20",
 "description": "Grep BQT for pirar, parandush, farzane"
}
```


### [2026-09-14T00:52:41.858Z] TOOL RESULT

```
=== farzane v3 ===
776:‏کتابی است از تصنیفات فرزانه بهرام که ‎DE‏
811:‏*- «شارستان داش و گلتان بینش» ‎adi‏ «فرزانه ‎de‏ بن‌فرهاد» از پیروان‌آنر کیوای (هم.)
18148:۱ فرزانه (هم) :
18183:ورك : فرزانگی ی « فرزان حکمت ‎ol‏ و حکیم فرزانه »« لفت فرس ۰۳۷۹« فرزانسزاوار
18186:نباشد میل‌فرزانه بفرزند وبزن ‎Sp‏
18205:«منای ‎٩۲۷6‏ از: فرزانك )= فرزانه) ‎(ge)‏ + یه( سای ببت) ؛ علم. داتابی» حکت. فشل .
36303:‏۱ - همی تا داب کنج وکام کردش پدر فرزانه هرمز نام کردش .
42620:بهم در به پبوست فرزانه سنگه درآنجا نبود از گرچ بوی ورنگه.
```


## [2026-09-14T00:52:44.524Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18140,18215p' incoming/BQT/BQT_v3_pages.txt; echo \"=== leaf idx ===\"; awk 'NR<=18190{if(/\\f/) c++} END{print c}' incoming/BQT/BQT_v3_pages.txt",
 "description": "Print BQT v3 farzane context"
}
```


### [2026-09-14T00:52:45.572Z] TOOL RESULT

```
بروزنگرم‌سود » پمعنی حکمت باشد که آن در
یافتن افضل معلومات است بافنل علم .
قردد ‎٩‏ - بضم اول و ثالی و سکون
الث و دال ابجد . سبزمایت در نپات سبزی
و تازکی و تری ‎Ts‏ فریز نیز گوبند ؛وبعضی
گوشد سبزم‌ای باشدکه در روی آبهای ابستادء
(۷) چك: پا زا .

۱ فرزانه (هم) :
مخالفان‌تو ‎og‏ فره‌اند 2 ‎Kas‏

۴ فرزین » ورك : فرز .

فرزدد شاد

بهم میرسد و در تابستان و زستان سبز و خرم
عیباشد ‎He‏

فرز ‎wT‏ - بکردال ‎deel‏ .کنابه
از حیوانات آبی باشد - و حباب را ‎ja‏ گویند
وآن ‎ats‏ ماندی است که بوقت باربدن باران
بر روی آب بهم میرسد +

فرر ند ‎LST‏ » بکردال .کنایهاز
لمل و ‎ol‏ و جواهر کانی باشد .

فرز ند خاود » کنابه از ‎wT‏
‏جهانتاب است .

فررند شا ۷ - بنتح اول و ‎AU‏
‏و سکون ثانی ورابع و شین نقطم‌دار بالف کشیده
و بدال بی ‎Me‏ زده » بمعنی مراقبه است که‌سر
جیب فرود بردن ‎Yay»‏ صاحب حال باشد.

. Ody : ‏چك‎ (0

| معادیان تو تافرخند و تافرزان .
بهرامی‌سرخی« لغت فرس ۳۷۹ *.

۴ - فرزان («.م.) . پپلوی 1822026 «مناس

۳ : ۲ > « اونوالا ‎٩۱۲‏ * هندی ‎OL‏ ۳۳2 ( پیشوند بمعنی پیش ) + ‎JAndti . jan‏
( شناختن , فهمیدن ) , قس : دانستن ( ارمنی - 080[ ) « اسشق ۸۱۵ » ورك : فاب \ ص۸۵
ورك : فرزانگی ی « فرزان حکمت ‎ol‏ و حکیم فرزانه »« لفت فرس ۰۳۷۹« فرزانسزاوار
بود ‎Kee (ipa)‏ حکیم راکونند ‎GLO.‏ (مروزی) گوید :

نباشد میل‌فرزانه بفرزند وبزن ‎Sp‏

» ‏این هردو تبرد دل قرزانه.‎ JH oye
. ٩ ۸٩۳ ‏«لت فری‎

۴ - برساختة ‎sho‏ > فرهنگه دماتیر ‎۷0٩‏ » « فاب ۱ : 4۷ .
5 - فربز < فرز < فرس * پریز. «قرزد » سبزم‌ای باشد درآب‌ومدام سب باشد.درتازی

آنرا ثیل(ه.م.) خوانند . بوشکور ( بلخی) گوبد :

فروتر زکیوان ترا ‎spol‏

برخشانی لاله اندر فرزد. »

0 ‏فری‎ cal?

۱ = فرزشاد ‎dsl,‏ دساتیر « فرهنگ دساتیر ۲۵۷ ۰.

‎POU ©‏ -بفتح ‎pind wees pads!‏ کزی بکرپنجم). پهلوی1722808161
«منای ‎٩۲۷6‏ از: فرزانك )= فرزانه) ‎(ge)‏ + یه( سای ببت) ؛ علم. داتابی» حکت. فشل .

‏۵ فرز ند - بقتح‌اولوسوم ؛ پهلوی ‎frazand‏ . ایرانی باستان - 4 ۲82210]دبارتولمه
۶ « یی رکه ۷۵ * اسشق ‎۸۱٩‏ ۲ ؛ ولد . زاده ‎WE.‏ پسر وگاء بدختراطلاق شده«اسشق

‎۰ ‏ورامین‎ we 0G ANN
[pdf page 253]
۱ ws

فزدو ۱ ‎peo‏ اول و سکون نالی
‎gly city‏ کشیده. بمعنی‌فرزبود اس تکهحکمت
=== leaf idx ===
251
```


## [2026-09-14T00:53:00.477Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"perperos\\|perper\\|perperus\" IEC.txt | head -20",
 "description": "Grep Mann IEC for perper"
}
```


### [2026-09-14T00:53:00.533Z] TOOL RESULT

```
12771:perperos ‘flighty, giddy’. Cf. peros (2) Gk. pærperos, adj. ‘fickle, rash, vain’; Lat. per- perus, id. cf. also perperam, adv. 'rashly, vain- ly’; Per. farfar, s. “hurry”
```


## [2026-09-14T00:53:01.846Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^per-\\|^per‑\\|^1\\. per-\\|^per\\b\" AHD_watkins1985.txt | head -30",
 "description": "Grep AHD Watkins for per roots"
}
```


### [2026-09-14T00:53:01.918Z] TOOL RESULT

```
836:per’
838:per-?
840:per-3. The young of an animal (< “a bringing forth,” “offspring”), Derivative root belonging to the group of per'. Suffixed o-grade form *por-si- in Germanic *farzi-, young cow, in Old English fearr, calf, and compound heahfore, calf (first element obscure): HEIFER. [In Pok. 2. D. per 818.]
841:per-‘. To try, risk (< “to lead over,” “press forward”). A verbal root belonging to the group of per’. 1. Lengthened grade *pér- in Germanic *féraz, danger, in Old English
```


## [2026-09-14T00:53:07.401Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=12771{if(/\\f/) c++} END{print \"IEC leaf:\",c}' IEC.txt; sed -n '12760,12775p' IEC.txt; echo \"=== AHD ===\"; sed -n '835,845p' AHD_watkins1985.txt",
 "description": "IEC leaf + AHD per entries"
}
```


### [2026-09-14T00:53:08.549Z] TOOL RESULT

```
IEC leaf: 511
the night; MHG ver-nahten, v. id.; OCS pré- noStujo, -evati, v. id.; Li. per-nàkt, adv. “through the night’; cf. per-nakvoti, inf. ‘spend the night; Latv. cf. par-naktim, parnaktis ‘night after night’; pàrnakSot, inf. ‘spend the night
pern- (pernt-) ‘beyond, away, far’. Cf. pe- rəm-. (Some forms ambig.) OPer. cf. parana-, adj. ‘former’; Tokh. A pärne, B parna, prp. ‘outside’; Arm. cf. heri, adj. ‘distant’; heru, adv. ‘far’; Hitt. peran, parranta, adv. ‘forth, away’; Gk. pérà, péran, prp. “be- yond’; péras, gs: pératos, s.n. ‘limit; Lat. cf. peren-die ‘the day after tomorrow’; OHG fër- rana, MHG vërren “far”; OE feorr, adj. & adv. id.; ON fjarri, adv. “far”
perð (1), see perið “pass through”, etc.
peró, io (2) ‘beat, flog? OCS pero, inf: prati, v. id. (and ‘wash - clothes"); Li. periü, perti, v. “flog” (pf: periau); Latv. peru, pert, id. (Z-gde in OCS prja, f. ‘quarrel’. Of indeterminate grade in Hitt. parh- mi, v. "drive
pero, io (3) breed (Variant: por-) Lat. cf. puer-pera, adj. f. ‘in childbirth’; -pe- rium, n. ‘parturition’; cf. also jüni-perus, gs: 1, f. Cjuniper,, if fr. *jeuni-per- ‘barren’, cf. for the sense Cz. jalovec ‘juniper’, jalový *barren?); (z-gde in) Lat. pario, ére, pf: peperi, v. ‘beget; Li. periü, pereti, v. ‘brood; hatch out; Latv. peru, et, v. id.; cf. pere, f. 'broody hen’; peri, mpl. ‘brood’?
peros, om, iom (1) ‘feather, wing’. WP II, 3]. Cf. peront- Skt. parnám, n. id.; Romani por, m. “feather”; Per. par, s. as Skt.; OCS & com. Sl. pero, n. ‘feather’; perije, n. (feathers, coll.)
peros (2) “swift, swiftness'. Lat. cf. pro-perus, adj. ‘rapid’; W er, m. ‘dash, impetus"; cf. erydd, pl. -on, m. Ceagle fr. *pe- riios? or fr. *ariio-? cf. Go. ara, OHG aro, id.); OCS cf. pero, inf. prati, v. (3) “jump, fly”
péros, à, om (pelor-?) (1) ‘side, end Skt. pàrah, am. m. n. ‘further bank, end, goal'; Av. paro, m. “end, edge, shore’; Per. cf. pār “over, across’; par- cpds.; Oss. cf. fale, falje, falä, adv. ‘beyond’; Pamph. pería, f. ‘site, plot'; cf. Gk. peirar, gs: peíratos, n. ‘end, limit
927
beside a-peíron, adj. “endless: farther’; Ir. íriu, gs: írenn, f. “land, field’; Ir. íre, gs: íreann, f. id.; Go. cf. fera, f. ‘side, region, limb’; OHG fera, fiara, f. ‘side, part; ON fjara, f. *fore- shore’. (Gmc. forms apparently fr. *peiora in view of OHG etc.)
peros (2) (?) Av. paro, m. (2) eut: OHG fara, fari, f. “danger; temptation; MHG vare, sf. ‘guile; rancour; danger beside vår, sm. & sf. id.; OS far, m. ‘ambush’; cf. far-ungo, adv. ‘suddenly’; OE fær, m. “danger, disaster ON fár, n. “harm; fraud?
perperos ‘flighty, giddy’. Cf. peros (2) Gk. pærperos, adj. ‘fickle, rash, vain’; Lat. per- perus, id. cf. also perperam, adv. 'rashly, vain- ly’; Per. farfar, s. “hurry”
perquo ‘thwart, oppose’ Arm. herkem, v. ‘refute, deny’; Go. cf. wai- faírhwjan, v. ‘wail; ON cf. firra, i-st. ‘defend; deprive’; firrast, refl. ‘shur’; OCS prëcæo se, inf. prěčiti se, v. ‘oppose; rebel; R perèčiť, inf. ‘thwart’; cf. po-prek-at, out, inf. ‘reprove’; (isophonic: Li. peřku, piřkti, v. ‘buy’; Latv. pērku, perkt, id. Cf. the semantics of Lat. pretium ‘price’ and Pol. preciw, prp. ‘against. Cf. also R poperëk ‘across’; Ukr. v-po-perek *athwart")
perquon- (?) “tree-top (?), striker of tree- tops (?), thunder-god (?Y. WP II, 43. See next Lat. cf. quernus, adj. ‘oaker’ (?); Go. cf. fair- guni, n. ‘mountain’; OE firgen-, cpds. id.; ON fjarg, m. “heathen god’; Li. perkūnas ‘Thor’; Latv. pērkons, pérküns ‘thunder’. (Semantics and phonol. obscure)
perquos, à, üs (a tree). Cf. prquo-. WP II, 47 Lat. quercus, gs: -üs, f. 'oak'; Lombardic fe- reha, f. “fir”; (z-gde in) OHG foraha, f. id.; (o- gde in G Fahre, f. ‘Scotch fir beside Fóhre (z-gde) as also ON fura, cpds: furu-, f. id; S w. furu, n. id.
pers- (1) ‘athwart, counter-, crosswise’. Cf. perquo OE feorsian, v. ‘pass, excel’; OCS cf. présovü, OR peresov ‘beam, rafter’ cf. also R prjàsio *crosspiece'; Cz. přes over, across’; cf. also OCS présme, n. ‘interruption, pause’; Hitt.
=== AHD ===
49
per’
“around.” I. Basic form *per and extended form *peri. 1. Germanic *fer-, *far-, used chiefly as an intensive prefix denoting destruction, reversal, or completion, in: a. Old High German far-, in German vereinen, to unite: TURNVEREIN; b. Middle Dutch vieren, to let out, slacken: VEER; C. compound “*fer-getan, “‘to lose one’s hold,” forget (see ghend-). 2. Suffixed (comparative) form *per-ero-, farther away, in Germanic *fer(e)ra’in Old English feor(r), far: FAR. 3. Compound “per-n-yo-, of last year (*-n-, year; see en-), in Germanic *fernja- in Old High German firni, old: FmRN. 4. Latin per, through, for, by: PER, PER-; PARAMOUNT, PARAMOUR, PARGET, PAR- VENU. 5. Greek peri, around, near, beyond: PERI-; PERIS- SODACTYL. 6. Sanskrit pari, through, around: PALANQUIN. 7. Avestan pairi, around: PARADISE. II. Zero-grade form *pr-. 1.Germanic *fur, before, in: a. Old English for, before, instead of, on account of: FOR; b. Old English for-, prefix denoting destruction, pejora- tion, exclusion, or completion: For-. 2. Extended form *prt- in Germanic *furth-, forward, in Old English forth, forth: FORTH; AFFORD. 3. Suffixed (comparative) form *pr-tero- in Germanic *furthera- in Old English furthra, furthor, farther away: FURTHER. 4. Compound *pr-st-i- (or *por-st-i-, with o-grade form *por-), “that which stands before,” stake, post (see sta-). III. Extended zero-grade form “pro-. 1. Suffixed (superlative) form *pro-mo- in: a. Germanic *fruma-, *furma- in Old Eng- lish forma, first, foremost: FOREMOST, FORMER?; b. Latin compound prandium, “first meal,” late breakfast, lunch (probably < *pram-d-ium < *pram-(e)d-yo-; second ele- ment *-(e)d-, to eat; see ed-). 2. Suffixed (superlative) form *pro-isto- in Germanic *furista-, foremost, in Old English fyrst, fyrest, first: FIRST. 3. Suffixed form *pre-wo- in Greek *prowo-, first, foremost, in: a. analogi- cally suffixed Greek form *préw-arya in Greek prdira, forward part of a ship: PROw; b. suffixed (superlative) Greek form *préw-ato- in Greek prétos, first, foremost: PROTEIN, PROTIST, PROTO-, PROTON. 4. Suffixed form *pro-i in Celtic *(p)ari, *are in Gaulish ari (combining form are-), before, in Latin arepennis, half-acre (second element obscure): ARPENT. IV. Extended form “prod. 1. Germanic *fura, before, in: a. Old English fore, for (> Middle English fore-), before: FORE, FORE-; FOREFA- THER; b. Old High German fora (> German vor), before: VORLAGE; Cc. Germanic prefixed and suffixed form *bi-fora-na, in the front (*bi-, at, by; see ambhi), in Old English beforan, before: BEFORE. 2. Greek para, beside, alongside of, beyond: PARA-); PALFREY. V. Extended form *pré. 1. a. Germanic *fra, forward, away from, in Old Norse *frd (> Middle English fro), from: FRO; FROWARD; b. Germanic *fra-, completely (see ed-, éik-). 2. Suffixed form *pro-mo- in: a. Germanic *fram, from, in Old English from, from: FROM; b. Germanic *frum, forward, hence derivative verb *frumjan, to further, in Old French f(ojurnir, to supply, provide: FURNISH, VE- NEER; C. Czech pram, raft: PRAAM. 3. Suffixed form *pr6é-wo- in Germanic *frdw6-, lady, in: a. Old High German frouwa, lady: FRAU, (FRAULEIN); b. Middle Dutch vrouwe, woman: vRouw. 4. Latin pré, pro-, be- fore, for, instead of: PRO!, PRO-!; PURCHASE. 5. Suffixed form *pr6-no- in Latin prénus, leaning forward: PRONE. 6. Possible suffixed form *pro-ko- in Latin compound reciprocus, alternating, ‘‘backward and forward” (*re-ko-, backward; see re-): RECIPROCAL. 7. Suffixed adverb *pro-kve in: a. Latin prope, near: APPROACH, RAPPROCHEMENT, REPROACH; b. suffixed form *prok- ink“o- in Latin propinquus, near: PROPINQUITY; Cc. suf- fixed (superlative) form *prok’-samo- in Latin proximus, nearest: PROXIMATE; APPROXIMATE. 8. Compound *pro-bhw-o-, growing well or straightforward (*bhw-o-, to grow; see bheue-), in Latin probus, upright, good, virtuous: (PROBABLE), PROBE, PROBITY, (PROOF), PROVE; APPROVE, IMPROBITY, (IMPROVE), (REPROVE). 9. Greek pro, before, in front, forward: PRO-2. 10. Suffixed (com-
per-?
parative) form *pro-tero- in Greek proteros, before, former: HYSTERON PROTERON, PROTEROZOIC. VI. Exten- ded forms *prai-, *prei-. 1. Latin prae, before: PRE-; PRETERIT. 2. Suffixed (comparative) form *prei-yos- in Latin prior, former, higher, superior: PRIOR2. 3. Suffixed form *prei-wo- in: a. Latin privus, single, alone (< “standing in front,” “isolated from others”): PRIVATE, PRIVILEGE, PRIVITY, PRIVY; DEPRIVE; b. Latin proprius, one’s own, particular (< pré priv6, in particular, from the ablative of privus, single): PROPER, PROPERTY; APPRO- PRIATE, PROPRIOCEPTION, PROPRIOCEPTOR. 4. Extended form *preis- in: a. suffixed (superlative) form *preis-mo in (i) Latin primus (< *prismus; ablative plural primis), first, foremost: PREMIER, PRIMAL, PRIMARY, PRIMATE, PRIME, PRIMITIVE, PRIMO, PRIMUS; IMPRIMIS, PRIMA FACIE, PRIMAVERA, PRIMEVAL, PRIMIPARA, PRIMOGENI- TOR, PRIMOGENITURE, PRIMORDIAL (ii) Latin compound princeps, “he who takes first place” (-ceps, “-taker”; see kap-), leader, chief, emperor: PRINCE, PRINCIPAL, PRIN- CIPLE; b. suffixed form *preis-tano- in Latin pristinus, former, earlier, original: PRISTINE. VII. Extended form *pres- in compound “*pres-g“u-, “going before” (*gvu-, to go; see gWa-), in Greek presbus, old, old man, elder: PRESBYTER, (PRIEST); PRESBYOPIA. VIII. Extended form *proti in Greek pros, against, toward, near, at: PROS-; PROSOPOPEIA. Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-’. [Pok. 2. A. per 810.] per-?. To lead, pass over. A verbal root belonging to the group of per’. I. Full-grade form *per-. 1. Suffixed form *per-tu-s in Germanic “*ferthuz, place for crossing over, ford, in Old Norse fjérdhr, an inlet, estuary: FIRTH, FJORD. 2. Suffixed form *per-ond in Greek peroné, pin of a brooch, buckle (< “that which pierces through”): PERONEAL. II. O-grade form *por-. 1. Germanic *faran, to go, in: a. Old English faran (> Middle English faren), to go on a journey, get along: FARE; WAYFARER, WAY- FARING, (WELFARE); b. Old High German faran, to go, travel: GABERDINE. 2. Suffixed form *por-o-, passage, journey, in Greek poros, journey, passage: PORE”; EMPO- RIUM, POROMERIC. 3. Suffixed (causative) form *por- eyo-, to cause to go, lead, conduct, in Germanic *farjan, to ferry, in Old English ferian, to transport: FERRY. 4. Lengthened-grade form *pdér- in: a. Germanic suffixed form *f6r-ja- in Old English (ge)féra, “fellow-traveler,” companion (ge-, together, with; see kom): FERE; b. Ger- manic suffixed (causative) form *fér-jan in Old High German fuoren, to lead: FUHRER. 5. Possibly suffixed form *por-no-, feather, wing (< “that which carries a bird in flight”), in: a. Germanic *farnd, feather, leaf, in Old English fearn, fern (having feathery fronds): FERN; b. Sanskrit parnam, leaf, feather: PAN2. III. Zero-grade form pr-. 1. Suffixed form *pr-tu-, passage, in: a. Ger- manic *furdu- in Old English ford, shallow place where one may cross a river: FORD; b. Latin portus, harbor (< “passage”): PORT!; IMPORTUNE, OPPORTUNE. 2. Suffixed form *pr-té in Latin porta, gate (> Old French porte, door): PORCH, PORT’, PORTAL, PORTCULLIS, PORTE-CO- CHERE, PORTER®, PORTICO, PORTIERE, PORTULACA. 3. Suffixed (denominative) form *pr-to- in Latin portdre, to carry: PORTS, PORTABLE, PORTAGE, PORTAMENTO, PORTATIVE, PORTER}; COMPORT, DEPORT, EXPORT, IM- PORT, (IMPORTANT), PORTFOLIO, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT. [Pok. 2. B. per 816.]
per-3. The young of an animal (< “a bringing forth,” “offspring”), Derivative root belonging to the group of per'. Suffixed o-grade form *por-si- in Germanic *farzi-, young cow, in Old English fearr, calf, and compound heahfore, calf (first element obscure): HEIFER. [In Pok. 2. D. per 818.]
per-‘. To try, risk (< “to lead over,” “press forward”). A verbal root belonging to the group of per’. 1. Lengthened grade *pér- in Germanic *féraz, danger, in Old English
50
pet-
fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
pete-
```


## [2026-09-14T00:53:40.984Z] TOOL CALL #27: Bash

```json
{
 "command": "pdftoppm -f 394 -l 394 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg394 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg394.png",
 "description": "Render PDF page 394"
}
```


## [2026-09-14T00:53:42.516Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"فرفر\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -20",
 "description": "Grep Mo'in for farfar"
}
```


### [2026-09-14T00:53:42.719Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 96039 Sep 13 20:53 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg394.png
```


### [2026-09-14T00:53:42.774Z] TOOL RESULT

```
MON_part2.txt:6403:فرفر: ۲ ا(ق.) به تندی» به شتات. 
MON_part2.txt:6404:فرفر: ۸-۲ [- فر فر ه] (اصت.) چرمی مدور 
MON_part2.txt:6406:کشاکش آورند تا از آن صدای فرفر ظاهر 
MON_part2.txt:6409:فرفره: (اص.) کاغذ پاره‌ای که بر سر 
MON_part2.txt:6412:فرفری: آ-6۲]6۲] (ص نس..) (عم.) مجعد 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:6403:فرفر: ۲ ا(ق.) به تندی» به شتات. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:6404:فرفر: ۸-۲ [- فر فر ه] (اصت.) چرمی مدور 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:6406:کشاکش آورند تا از آن صدای فرفر ظاهر 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:6409:فرفره: (اص.) کاغذ پاره‌ای که بر سر 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:6412:فرفری: آ-6۲]6۲] (ص نس..) (عم.) مجعد
```


## [2026-09-14T00:53:48.050Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6398,6415p' MON_part2.txt",
 "description": "Print Mo'in farfar context"
}
```


### [2026-09-14T00:53:48.096Z] TOOL RESULT

```
درنگ. غفلت.. 


فرغیش: 5(ص.) کهنه و فر سوده. 
موی‌ها و ریشه‌های پوستین کهنه که آویزان 
فرفر: ۲ ا(ق.) به تندی» به شتات. 
فرفر: ۸-۲ [- فر فر ه] (اصت.) چرمی مدور 
که کودکان ریسمانی در آن گذارند و در 
کشاکش آورند تا از آن صدای فرفر ظاهر 
شو د؛ بادفر. 

فرفره: (اص.) کاغذ پاره‌ای که بر سر 
چوبی تعبیه کنند و کودکان بدست گرفته رو 
به باد ایستند تا باد آن را به گردش در آورد. 
فرفری: آ-6۲]6۲] (ص نس..) (عم.) مجعد 
(موی). 

فرفور: ۲ ([م_عر - فر فیر ] (.) (جان.)
```


## [2026-09-14T00:53:48.748Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg394.png"
}
```


### [2026-09-14T00:53:49.262Z] TOOL RESULT

```

```


## [2026-09-14T00:53:49.260Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T00:54:06.834Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 394 -l 394 -r 450 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg394hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg394hi.png'); print(im.size)\nw,h=im.size\n# node18 persian box approx x 1000-1200/1545, y 1190-1270/2000 scaled\nim.crop((int(0.62*w),int(0.575*h),int(0.80*w),int(0.65*h))).save('crop18-394.png')\nim.crop((int(0.60*w),int(0.49*h),int(0.80*w),int(0.55*h))).save('crop14-394.png')\n\"; ls",
 "description": "Crop Persian boxes at high res"
}
```


### [2026-09-14T00:54:09.832Z] TOOL RESULT

```
(3825, 4950)
agents.txt
bqt390_436_foot.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
crop14-394.png
crop18-394.png
pg390.png
pg394hi.png
pg394.png
queue.txt
```


## [2026-09-14T00:54:12.055Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop18-394.png"
}
```


### [2026-09-14T00:54:12.068Z] TOOL RESULT

```

```


## [2026-09-14T00:54:20.487Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop14-394.png"
}
```


### [2026-09-14T00:54:20.527Z] TOOL RESULT

```

```


## [2026-09-14T00:54:22.039Z] TOOL CALL #34: Bash

```json
{
 "command": "pdftotext -f 394 -l 394 -layout EtymologicalDictionary-persian-english.pdf - 2>/dev/null | cat -A | head -5; echo \"=== plain ===\"; pdftotext -f 394 -l 394 EtymologicalDictionary-persian-english.pdf - 2>/dev/null | head -60",
 "description": "Extract PDF text layer page 394"
}
```


### [2026-09-14T00:54:23.133Z] TOOL RESULT

```
^L=== plain ===
```


## [2026-09-14T00:54:33.035Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD frod/frazanag ===\"; grep -n \"^frōd\\|^frod\\|^frazānag\\|^frazanag\\|^frāz\\|^frōt\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== PHD grep loose ===\"; grep -n \"frazān\\|frazan\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== NYB ===\"; grep -n \"frōt\\|frōd\\|frazān\" NYB_vol2_glossary.txt | head -10",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-14T00:54:33.134Z] TOOL RESULT

```
=== PHD frod/frazanag ===
PHD.txt:4661:frazānagīh ^3» > O° frazanag 13 d o frazām $ à o frazám- -S à оу
PHD_mackenzie.txt:2372:frazanag [plc)nk I P frz)ng, N farzana] wise, intelligent.
PHD_mackenzie.txt:2398:frod [plwt' I M pTwd, N juro(d)] down.
PHD_mackenzie.txt:8635:frazanagih          AU~~~eu                fragan, pillagan          \,.,..~v
PHD_mackenzie.txt:8636:frazanag              \9""~eu              parrag                      ,~eu
=== PHD grep loose ===
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD.txt:354:frazānaģ [plc”nk! | P frzng, N farzána] wise, intelligent.
PHD.txt:356:frazand [prznd | M frzynd, N farzand] child, son, offspring.
PHD.txt:965:beget (frazand) warzīdan.
PHD.txt:1223:child aburnüy(ag), frazand, waččag, zadag, zahag.
PHD.txt:2458:intelligence frazanagih, ēš(īh).
PHD.txt:2459:intelligent frazānag.
PHD.txt:2967:offspring frazand, paywand, zahag; (daevic) hunušak,
PHD.txt:3730:son frazand, pus(ar).
PHD.txt:3733:sonship frazandih.
=== NYB ===
6560:farzanaa: frazānak
```


## [2026-09-14T00:54:40.415Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^frōd\\|^frod \\|frōd \\[\" PHD.txt | head; echo ---; awk 'NR<=354{if(/\\f/) c++} END{print \"PHD leaf for frazanag:\",c}' PHD.txt; grep -n \"frōd\\|furō\" PHD.txt | head -10",
 "description": "Find frod in PHD.txt and page"
}
```


### [2026-09-14T00:54:41.544Z] TOOL RESULT

```
---
PHD leaf for frazanag: 51
```


## [2026-09-14T00:54:46.130Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '350,362p' PHD.txt; echo \"=== search frod ===\"; grep -n \"plwt\\|prwd\" PHD.txt PHD_mackenzie.txt | head; echo === ; sed -n '2394,2400p' PHD_mackenzie.txt",
 "description": "PHD context for frazanag and frod"
}
```


### [2026-09-14T00:54:46.214Z] TOOL RESULT

```
Exit code 1
~išn: completion.
frazám [plem | (N farjām)] end, conclusion.
frazāmēnīdan, frazāmēn- [plc*myn-ytn!] = frazāftan.
frazām-pērēzīh [p/c”*m pylwcyh] final victory.
frazānaģ [plc”nk! | P frzng, N farzána] wise, intelligent.
~ih: wisdom, intelligence.
frazand [prznd | M frzynd, N farzand] child, son, offspring.
~ih: sonship.
frazën [plcyn' | N farzin] (chess) queen (lit. ‘guard’).
frēb [plyp | N firéb] deceit, deception.
fréftan, frēb- [plyp-in' | N fir~] deceive.
C 6684 D
fréftár 34 gal
=== search frod ===
PHD.txt:370:frdd [plwt' | M prud, N furd(d)] down. -mànd [-m?nd] deficiency, shortcoming.
PHD_mackenzie.txt:983: AUldan, illy- plwtn', 'l'd- I (M 'rwd), N .....,] defile, pollute.
PHD_mackenzie.txt:2398:frod [plwt' I M pTwd, N juro(d)] down.
(eval):1: == not found
```


## [2026-09-14T00:55:02.039Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT paurva ===\"; grep -n \"paurva\\|pouruua\\|pourva\" BRT.txt | head -15; echo \"=== BRT paro.ayara ===\"; grep -n \"parö\\.ayara\\|paro\\.ayara\\|ayara\" BRT.txt | head -10",
 "description": "Grep Bartholomae"
}
```


### [2026-09-14T00:55:02.102Z] TOOL RESULT

```
=== BRT paurva ===
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
3480:mit  avi  'einholen':  yest  ahi  paurva.- nafmät  aal  "lam  avi  nmänaya  (sd.)  yezt paskät  aai  ma'm  avi  apaya^sS.)  Yt.i&.a.
3583:—  ma%rym  spmttm  . .  pmrumca  . .  'r^mca V.  4.45;  45;  —  ahun?m  vairJm  . .  Tim sraoidyehya  (^^  frasrüiti  Y.  5. 14;  — apanmta  tiais^mi&A.)  G.3.T, —  'raheca yamahe  haplanhatdis  Vr.2/.o;  0,4^;  — ranuhlsla  a'A  .  .  hupaurva  (sd.)  vahehiS Ti/"  räsaintü  ¥.52.3;  —  aiwiea  'rim patiia  'rym  apsca  paurvalibya  "und  (man soll)  einen  zweiten  (Rüden)  und  dann noch  einen  weiteren  (zulassen)  und  zwar (soll  man  ihn)  gesondert  von  den  beiden ersten  (halten)"  V.  i^.  48.  3)  '>  der  Zeit nach 'der  spätere,  kUnftige'rja^a  mä  'racil (NPm.)  saoiyanis  stavqn  V.9.  2;  — yastä datrSMg  °rö  .  .  tarS.mqstä  "wer  darum künftighin  (eig.  posterior)^  den  D.  ..  auf- sagen wird"  V.  4:5. 11;  —  huzantSus  paiti •raya  YL  13. 134.  a)  mit  ayan-  n.  'der spätere  Teil  des  Tags,  Nachmittag':  */ra- \aire  ayqn  bavaiiii^A.)  hubar,rS  ..  a',a  "re ayqrt  duWirjm  ". .  dann  am  Nachmittag (kommt)  das  Unglück"  Aog.jJ.  A)  ASn. 'r?m,  'ram  und  IS.  °ra  als  Adv.  'postea, später,  künftig' :  yezi  nairyS  aukat  pasca hl  pourum  (sd.)  paiti.hin£öi^  paitisa  "r^m V.ÄSS;  v,%;  —  \mätyi^hy(r'ramimam dipim  patiparsiltiy  .  ,  BL4.8;6,  15,  ^.y,
3777:gaikaAü  tanusi^ä  Y.^J.  7-       2)  Praev.  (mit 'ak;gam-,  'bar;y/th-,  valn-  usw.).        a)  bei Ellipse  des  Verbums:   "wi?a  aparpm  (sd.) paiica    aparam    apnca  paurvaäbya    V.  75, 48;  —  asäaüä  haiä  van/iSus^il  mananhs vankyuscS   xla>rilt  staotäis  '^Tnifl  ahum staotSibyö  °bT  ux'o/l    '^wüt  uxüSibyS  yasnH %wät  yasnsibyd  "und  um  des  ASa  willen und  des    VM.  und  des   guten  XS.:    Lob- gesänge (häufen  wir)  nunmehr,  o  Ah.^  auf Lobgesänge  und  Sprüche  auf  Sprüche  und Gebete  auf  Gebete"  V.^j,.  10";  —  huxsa- %rSJ»m!li  (sd.)    .  .    xsa'inm    ahmai   hya^ 'bii^  dadsmahica  .  .  Y._Jv5. KompA-i  Ableit. —  aLiiM/,  mp..rai*,  np.a/". —  Vgl.  laii,  aei.  —  Pü. :  afar;  (in Komp.  auch): d/f  und  wepgelassen.  —  ')  S.  lu  aiiaiwülay- No.  I.   —    ')  Man  kann  aus   dem   vorherg. Ahsatzdad3maideetgiaT.Ka.  Gdn.n  Übersetzung GlrPb.   3.  32    ist    mir   unverständlich.     Pä.: släyisn  i  IS  öhrmatd  am  haf  släyi'snän  apar,  Sü. : ilulih    te    a-ämin    slulibhya^    utirflalarä.      — ))  Man  erwartete  die  selbe  Redensart  wie  V.
4190:•  '].  a-ohvä-,  g.  a-hvä-"  f.  i)  'Antrieb des  Willens,  Schaffensdrang,  Lebenskraft' : pairika  yä  duzyäirya  vlspahe  atiksui  .  . ' faröit pairi'in^misA.)  anhvqm  avaAisiiyät\ (sd.)  Yt.Ä54;  —  ava  m!  3zis  .  .  par5it\ fairrbnpm  (sd.)  arihvqm  ava.d}nnqn  sada- 1 yäfi  (sd.)  V.  i5. 19.  2)  'Antrieb  derl Seele,  innerlicher  — ,  Gemütsdrang,  Ge-j müt'"':  kal..*manS  asti  vT/aymii'tfm{s±) anhvqm  vjmar3zist?m  (sd.)  VL  /.  2 ;  —  ' virtzvatca  (sd.)  mat^  vansvatica  attuAa  j 'W.  62,10;  —  ye  kvam  ankvam  yaozdaite\ humatsilia  .  .  V.  ^.2i^>;  si  *PÜZ.,  lO.  19  I PüZ.;  —  dusx'arpnä  . .  asH5  asti  auuhaya  \ (LS.)  ".  .  ist  unfroh  in  seinem  Gemüt"  j YLJO.105;  —  aibl  ahväha  daxst^m  dilvOi\ (sd.)  Y.5/,9;  —  yatära  vä  dim  paurva frayasäiti  fraor^t  fraxsni  avi  manö  (sd.) zrazdälöii  ar^huyal*^  (oder  avuhyat)  i>  haca ". .  gern  in  sorglichem  Sinn  aus  gläubigem Gemüt"  Yt  /o.  9;  —  fora  vi  räki  am?sä spmtn  yasmmcä  rahmtmcä  firä  mana»hä ..  vaiaahä  ..  syat>^anä  ..  dw^iy«  (IS.) » Y.7/.18.
4698:\)amm  Y.$4.2,  G,  j.6; — yä  {ar?ävi) 'vaiti fratalaili  Y.  Ö5. 3 ;  Yt.  5. 1 5 ;  —  a^tn  vatau- hlm  .  .  hrpsailTm  'vattTm  Y.  3. 14;  Yt /J. I,  7;  —  drvaspqm  . .  'vaitlm  YL9.2;  — fravaiayö  .  .  yä  'vaifli  Yt  13.  29;  —  at töi  atrjm  . .  *asXsttin  'vanhm  Y.j^4;  — tiiirim  .  .  'vant?m  YtÄ4;  —  vatianttm 'vant»m  Yt  21.  i;  —  °vatS  amai  'vatÖ virp^raynäi  'vat^yO.  »rütyi  'vai'iya aiöii  'vai^ya  astdil  'vaüyä  paurvatälo 'vai'i'yB  uparatälö  'va^byä  yazatoAbyö  Vr. g.i,.  b)  sonst;  uströ . ,  b)r?zB  "vä  Yt i.^.  1 2 ;  —  srlra  urusta  'vaiti  (VSf.)  .  . UfTaireY.it^.iB,Vyt22; — srayarfhö  vouru- ka?ahe  'vatö  Yt.<S.46;  —  vasnm..  zaröil ayanhö  frahixt»m  'vatö  \L  10.96;  —  'vat iimäfum  Y.  57. 10;  —  ptiüm . .  yim  aiwatö 'vantim  Vyt.^;  —  'vaitlm  sitiqin  dävöi (sd.)  dr»gvasa  Y.  44. 14.  —  IstJm  . .  pouru.- sarioam  'vaitlm  Y.  65. 1 1 ;  —  hazö  "vat  Y. jj^.  iz;  —  yahmi  maza  'va  (NSn.l')J' '  iiiäälpm  Yt  10. 64  (?) ;  —  *°vata  vaca  F.3  e. AbleiL  —  ai.  dmm-ant-  Adj.;  vgl.  mp.  (PS.) amäz-nnd.  —  ')  %  jg4.  —  •)  Zur  Zusammen- Stellung  von  amai'aaf-  mit  ^'/ri^ravan ,  viri- %rasan-  s.  'amn-  2.-3)  Wenn  richtig,  wohl Neubildung  lum  NSm.  'va  nach  der  n-Dekt.
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.aspahe  Yt.  10. 1 3.  A)  ins- bes.  von  den  dem  AhuraMazdäh  nächst- stehenden Gottheiten*':  yaia  vahm>m 'iaiibyS  Y.  21.2;  —  -saHi  . .  avarshe  ismti masyäkänAs  Aog.  41.  a)  sonst  in  Ver- bindung mit  spitUa-  Adj.  'heilig',  das  in GHapL'vor-,  sonst  nachsteht:  *vyäX3mca kanjamanimca  (sd.)  yat  as  'sanqm  sp?nta- nqm  banlnvS  *avarihe  as/0  y?mat^m  (sd.)
7023:ll  aim  iaraili  aesmfm  .  .  5  h/  pascalta frJnaiti  ätari  . .  ".  .  wenn  er  ihm  drauf Brennholz  bringt,  alsdann  segnet  ihn  Ä." V.  62. 8f.  1  a)  'seit  dem':  äai  {s.i)  ^ws . .  tmrrja  vlbann  . .  ä'  äkva  paurvalähva des  Satzes  stehend'*;  1)  zimi  Ausdruck  | .  .  vTraoXahe  Y.  10. 1 1  f.;  —  frö.  K  mazdh zeitlicher  Folge 'darauf,  dann,  alsdann,  da':  ,^11^0/  .  .  aiwyhnkaram  .  .  a°  aiAhe  ahi pinsal  tara'>:ustrS  ahurim  mazdqm  .  .  iT'aiwysstö  Y.p.  26.  2)   zur  Anknüpfung
7038:satz'so,  dann;  da.' -.yezi ('wenn') aAipaurva.- naem3l  3'  mqm  avi.rimilnaya  (sd.)  Yt.16. 2;  a.  3-3,  Y.2.43,  ^'.36,  103,  /ö'.ii,Nik. 3,  Vd.  13';  —  yat  ('wenn')  yave  dayat ä'  datva  y^ism  (sd.)  V.J. 32;  321,  H.  2". 13,  N.  IJ2;  —  3at  (s.  8)  yat  apö  uzbargnte .  .  a°  fraiasinti  . .  fravasayö  Yt.  13.65; V.  Ä40,  i7.4;  —  yat  ("als')  mqm  tura pazdayatita  .  .  3'  az3m  tanüm  aguze  .  . \3at  (s.  3)  mqm  fraguzayanta  ..Yt  i7.  55^'; — yas}  tat  nmäfum  äk^rstmn  .  .  «7°  mqm tnairyö  akasat  dai  (s.  2)  .  .  fräksrmaot V.  22.  i£;  —  3at  (s.  8)  yat  miirtm  .  . /radaöqm   .  .   a°  dim  danqm  ,  .  Yt.  10.  i ;
7251:zu  *  myaso-ä. Sarana-  und  ♦i^nira-.  —  '«  In  |  Nachsatz  r  cim  Aoxa  . .  ^baraiU  .Ja'  ym Pü.  scheint  *aoM*tD  entsprechen, —  w)  Wennjj'^  glm  baraifi  agsttum  ..  ä  kl  pascalta nicht  -  mp.  äk;  s.  »u  J™.  -  •')  Geschr.  f^^atti  aiar/  .  .  ".  .  wenn  er  ihm  drauf Brennholz  bringt,  alsdann  segnet  ihn  Ä." Y.62.8f.  I  A)  'seit  dem':  äal  (s.i)  ^aiä •  j.,  g,'>  aat  Adv,,  meist  an  der  Spitze  ..  varrfa  viiar^n . .  a-  ahva  paurvatähi-a des  Satzes  stehend'*;  1)  zum  Ausdruck  ,.  vTraö^ahe  Y.io.iii.;  — frä  il  mazdä zeitlicher  Folge 'darauf,  dann,  alsdann,  da' :  i  Mm/  ,.  atmyatahajam  ..  ä°  aiiike  ahi pfnsal  zard^ultrS  ahumn  mazdqm  .  ,  3° .  aiwyäslö  V.p.  26,  2)   zur  Anknüpfung
7957:1 1 ;  —  D  °mä  dahyävc^  tyil  kacärnJ'  hami- ' ^'^/^'J  abaia":  p^rsa^..'Bh.2.2;  1.6,  D.5.2, 6.3;  —  'm?m  Hwam  xstäm  yju>m  .  . jairiyemi  ..:  paurva  tiiyüm  . .  bütriyBimatoe Y.5.21.  a)  auf  eine  erläuternde  oder ergänzende  nominale  Beifügung,  a)  sut>- Stativisch;  dassmü  yat  ahmt  ,  .  i'a^rvdasS imat:  vIiivaestv3{sA.)  YtJ.8;  —  in  Kon- gruenz mit  dem  Praedikat:  'tnftn  'hwqm paoirlin  yiin?m  .  .  jatoyemi  .  .:  vahishm aküm  Y.5.19.  b) adjektivisch, bei rela- tivischem  Anschluss:  'mat  äama  yat  ahu- rahe  V.  ig.  14,  17,  34,  Vyt.  20;  —  avi °mqnt  tanUm  yqm  masylnqm  V.  20.  3, 5.  3)  auf  ein  Relativum  als  dessen Korrelat,  a)  adjektivisch :  'ine  vaca  framrva yöi  hmti  gä^ilkva  bisämrüta  V.  10.  2;  2;
8751:Lebenskraft'^':  hyat  astvant»m  (sd.)  dada 'tatum  y.j/.  ij;  —  tal  ii  .  .  vairim  ast- rwV?  (sd.)  'tänäi''''  data  Y.^j.,^.  14;  —  at rätqm  zara'^uÜrö  tanvascti  x^ahya  'tattpm dadaiti  paurvatätpm\.33.i^;  —  f^ra  vS rahl  .  .  tanvasclt  c^'ahyS  'tatum  V.  //.  18; /_9.4;  — darsyö.xia'irpm  xsa'^raAe  dury/ö.- jUim  'tilnahe  A.  1.8]  Y.  17. 19;  —  m-^irpswa slün'i  gayehe  mprpzu^a (sd.)  xa  'tänahe  Yt. JO.  7 1 ;  —  avai  he  astt  masyö  ar^i^pm  yat \  'tatum  bttnjayüt  (sd.)  V.  7.  7 1 ;  —  ava \  apamm  (sd.)  gayehe  *frasatu>m  'tanahe  Yt.
10507:1  paurva.nalmäX  (sd.)  ahe  gravahe  V.  ,  Yt  /j.  2.         A)  Int  'hin-  und  herfliessen, €f.  14.  '  auf  und  ab  wallen':  ti  kist.uiti  (sd.)  yzan.-
10715:gAw. :  ahya  '"kräXa  maziiiäcä  *hvapa- nhäisca  (sd.)  tsm  at  ,  .  yasamaidl  Y.^J/. a;  —  kudä  (sd.)  asim  vohuca  maus '%r)m^ä  Y.  25.  1 1 ;  —  yüism  aäbyS  .  . aogü  data  .  .  '%nmc3  .  .  yl  kuhitts  rä- mqmcS  (sd-)  däl  Y.  2p.  10;  —  isasä  (sd.) . .  maibyö  '"^nm  aojönahvat  yehy3  vfndä (sd.)  vanalmS  *drujim  Y.J/.  4;  benutzt V.ao.  8;  —  tat  mazdä  tava  '>rfm  yä  .. düAf  drigaov!\sA.)  vaiyj  Y.ß^.g;  — yJ vahyJ  varihSuS  dagdi..ahurö  '"S^rä  mazdä Y.5J.  6;  —  tici  '^rä  mazdä  dqmis  (sd.) ahurS  'V.4$.T,  9;  —  maibyS  masds  tavä rafinS  JräxStuiam  (sd.)  kyat  ^wä  °&rJ a/Jt  hacä  frqifa  Y.  4!?.  1 4 ;  34. 15;  —  y} dfmanahyä  'hnm  M^rahya  vä  daSySu:" va ../radahäi{sA.)  aspinzatä  Y.Ji,  16;  — yastJm  °ärJ/  mazäJ  mSÜai  (sd.)  jyätSul Vä  Y.  46.  4;  —  at  ratqm  zara'iuitrS  .  . dadäiij  paurvatätim  . .  mazdiU . .  ux^aHyäcß (sd.)  ifraespm  '"irimcä  "..  den  Gehorsam und  die  Herrschgewall"  \.33.i4;  benutzt Yt  IJ.  88 ;  —  vauhstts  dazd,l{%ü.)  manau/iS lyaöhananqm  a»fiSus  mazdäi  ''knmca ahuräi  a  X.2-j.iy,  —  hux^a^rSJimäi (sd.)  .  .  '"ir^m  .  .  äad)mahicä  cismahicä *hvqnmakicä  Y.^5. 5;  —  yS  dngvSUi '"^nm  hunüiiJ  {?,d.)  Y.j/,  15;  —  yais *ffrMm3{sd.)  asäivaratä..°'^r3mca  lianqm *dnfim  Y. 32.13;  —  '>rais  yujin  (sd.) karapanU  .  .  akäis  syaohanäis  .  .  Y.  46. II.  a)  mit  Gen.  'über  — '  (s.  2  a);  tarn
11060:5700.);  —  ave  aipi  dai',yants  ave  aipi  hu- marmtö  yüi  . .  avasiqmca  pä^S phntB yim  .. Ytro.4S.  b)  sie  sind  getrennt:  3r>sat>tn zaranim  ..  vasfräsca  Yt/7. 14»';  —  yais "grskma  (sd.)  asat  varalä  karapa  xsa- lirjmca  Y.32.  12;  —  akmaicä  (zu  B) xsa^ra  jasal  (sd.)  manarshä  vohB  asaca Y._;o.  7;  — paurvatätim  .  .  ssraosim  xsa- %nm^a  Y.33.14.  a)  mit  Tmesis:  vT- Hdyäi  . .  vtduyi . .  tfisnca  daidyai  Y.  31. 5.  ß)  in  Verbindung  mit  ula:  :^ar»tiS
=== BRT paro.ayara ===
2801:Irrlehrer,  der  . ."  \.g,$i{.;  —  yavat  °fa *gaintii  upankacaili  (sd.)  V.  7.  56;  — yavat  'sa  ilß  bySrixfi  (sd.)  .  ,  frabavai \.i4.\y,  — yavat  -lö  spä  anya{sA.) )asö V./5.48,  a)mitrelativischemAnschIuss: "jS  zT  asti  baslazyö.t3mö  .  .yal  *mahnm.- sppni»m.baei'azyd  (sd.)  V.  7.44;  —  '/a  bi~ paitisiana  (sd.)  y3  kaine  V.  75. 19;  19;  — vXsp»m  ä  ahmst.,  yat  -ia  yö  apsntinyBkB uxjasnf  (sd.)  "bis  es,  das  Kind  . ,"  V.  75. 15;  —  'sa  yS  *ar?mBiidd'a.W3.  2)  auf ein  Relativum  als  dessen  Korrelat,  sub- stantivisch: ci'at  dra)ö  avaMUlüt  '^a  yö näirikaya  . .  !^ar>^3tn  frabamt  V.  /J.  4 1 ; —  °sö  .  .  aitayä  vihrkayh  (sd.)  Jq'^-wS.' tarö  *at3kat  . .  ya^a  spä  vtkrkake  k»r?- naoiti  V.  y .  4 1 ;  — "/?  ratufris  *yö  jayara N.if};  24,  60;  —  'sa  yetjhe  apirinSyükö ^•9i  7;  —  °^'''  zaoiranqm  tnaziltaca  . . yiJ  *naire  asaone  *daste  N.^4.  III)  In
4885:•  j.  ayara-  m.  Plur.  Name  der  Gottheiten der  Tage :  ra'iwqm  'ranqmca  '*  asnya- nqmca  mlhyanamfa  yätryanqmca  Y.l.iy;
5901:•  j.  asnya-  Adj.  'auf  den  Tag  bezüglich': °yehe  pascaSa  anyehe  ra'^ivü  "im  nächst- folgenden Tagesabschnitt"  V.  7.4,  A)  m. Name  der  Gottheiten  der  fünf  Tagesab- teilungen**  und  derentsprechendenGebete: •ya  asavana  asake  ratavS  Y.  2.3;  17;  — 'yaeibyS  aiahe  ratubyS  Y.  /.  3 ;  —  ra'iivqm ayaranqmca  'yanqmca  Y.  r.  17.
8585:j.  usayara  V.  2/.  J :  s.  '<rr-.
8586:•  j.  uzayara-  n.  'Nachmittagszeit,  Nach- mittag* :  haca  rapthwayät  ^matäyni  -räi N.4t);  ^7;  —  Äaca  maiiyäj  *'räj'*  An */rasm0.äätJe^.^o;*^o'^; — ya'iia  *°rpm'^ yat  ya>a  xiapartm  N.  .i7(?);  —  yche sa'^aii'a  vaxiai'a  'r^m  dd^at  ahurS  V.  2/. 1*6  (?).
8589:•  j.  'tizayeirina-  Adj.  'nachmittägig': */rayar?ne  vä  'ne  vä  *ayqn  "sivc  ante- meridiano  sive  pomeridiano  die"  N. p.  A)  m,  Gotdieit  der  dritten  der  fünf^ {priesterüchen)  Tagesabteilimgen" :  'tum aimamm  asahe  ratäm  Y.2.5;  G.J.5;  — 'ttäi  Y.  i.  5,  G.  j.  I ;  —  °na  .  ,  ralvö  Y.  i. zo;  —  ^räyS  ayara  °yarna  Vd./7*'.
8590:•>  Genannt  uzayara- {%&,)  und  nach  N.  50  vom halbea  Nachmittag  bis  Sonnenuntergang  während. Vgl.  noch  Bd.  2J.  9  (wo  efiärai'))  und  zu  aiHya-, Ableit.  —  Ableit.  aus  uiayara-.  —  Pü. :  utayarin, Sü.:  aparShnaksamdkyah,  —  1)  Pü.:  roc  i  Jum fa  gät  i  Ungarin,  —  »)  S.  dawi  GIrPb.  /. 372  p).
10176:avi  imitt  karh-arf  yat  x^anira%3m  ..  'tum ' .  .  mi^r^  .  .  ädmäiti  Yt.  lo.  15, '  •  j.  gav-a'äitay-  f.  'Wohnstätte  der  Rin- der': avi  imai  karrvar>  yat  x''anira>:>m.. gavasayaramisA.)  'lliiica  bassatyqm  mi^rö . .  ädi'jiiiti  Yt  10. 15.
10985:•  j.,  g.  xSvid-  m.  'Milch';  im  Gegensatz zu  axBtay-  (sd.)  überhaupt  'flüssige  Nah- rung' im  Gegensatz  zu  fester:  pars  °isca (NS.)  äsaitisca'^  gsui  mal  "hervor  (geholt werde)  Milch  und  Fett  samrat  Fleisch" V.13.2%;  —  ■ilaica  (DS.)  azStayalFa''> Y.ßS.ii  —  am  äiStBis(sd.)  aAurB mohnm tasat  .  .  gavSi  'lihmlä'''  * AvS urusalibyS V.  25,  7;  —  *mmdäidyäi  (sd.)  «ftfem^)  Y. 1/.9.  a)  Du.  in  Verbindung  mit  äsütay- Du.:  "röa  (AD.)  äzuiti  yazamaiäeY.iG.Z; zit.  *F,5.  a)  pasca  xsavaidlm  ayara- namca  (soll  heissen)  "nach  sechs*'  Tagen" Vd.5.
11148:—  'tanrö  (Af.)  p>rmä  vf<>ärayvU  Yt.  z^. 44;  N.  6j,  /02;  —  '"iiwan  ayaranqmea Vd.//.  a)  -^tpJrff  als  a)Nfs':^ä/^J ^rafJ  .  .  "'^wärB . ,  pania  xsafha  saüänie V.  j6.8;  8.  ß)  An.S':  •%iiiärSsata  Stn.- saokanqm  "vierhundert  .."  V.  Ä 84;  6.21'.
```


## [2026-09-14T00:55:13.670Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN vorgestern ===\"; grep -n \"vorgestern\\|vorletzten Jahre\\|parlr\\|perlr\" HRN.txt | head -10; echo \"=== HUB ===\"; grep -n \"vorgestern\" HUB.txt | head -10",
 "description": "Grep Horn/Hübschmann for 'vorgestern'"
}
```


### [2026-09-14T00:55:13.735Z] TOOL RESULT

```
=== HRN vorgestern ===
=== HUB ===
```


## [2026-09-14T00:55:18.287Z] TOOL CALL #40: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T00:55:18.291Z] TOOL RESULT

```


```


## [2026-09-14T00:55:21.773Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C%D8%B1",
 "prompt": "Give the full Persian etymology section for پریر (parīr) 'the day before yesterday' — Middle Persian and Avestan/Old Iranian antecedents, and any cited authorities."
}
```


### [2026-09-14T00:55:23.086Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T00:55:23.544Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B2%D8%A7%D9%86%D9%87",
 "prompt": "Give the full Persian etymology section for فرزانه (farzāne) — Middle Persian form, Old Iranian reconstruction, and cited authorities. Also any note on فرزین farzin."
}
```


### [2026-09-14T00:55:28.954Z] TOOL RESULT

```
# Persian Etymology for فرزانه

Based on the Wiktionary entry provided:

**Middle Persian Form:** The entry states the word derives "From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") \[script needed\] (plcʾnk' /⁠frazānag⁠/, 'wise, intelligent')."

**Old Iranian Reconstruction:** The Parthian cognate is listed as /⁠frazānag⁠/, with the same meaning of "wise, clever."

**Morphological Analysis:** The word is presented as equivalent to فرزان (farzân) plus the suffix ـه (e).

**Cited Authority:** MacKenzie, D. N. (1971), *A concise Pahlavi dictionary*, Oxford University Press, page 33, is referenced for historical validation.

**Additional Note:** The entry mentions a "Perhaps related to Sanskrit प्रज्ञान (knowledgeful)" connection, though this is marked as speculative rather than established etymological fact.

**Regarding فرزین (farzin):** The provided content contains no information about this variant or related term.
```


## [2026-09-14T00:55:35.984Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B2%DB%8C%D9%86",
 "prompt": "Give the full Persian etymology for فرزین (farzin) 'queen in chess', including Middle Persian forms and any cited authorities; also mention Arabic فرزان/firzān if present."
}
```


## [2026-09-14T00:55:36.811Z] TOOL CALL #44: WebSearch

```json
{
 "query": "Persian پریر parīr \"day before yesterday\" etymology Middle Persian *parēr Avestan para ayar"
}
```


### [2026-09-14T00:55:40.680Z] TOOL RESULT

```
# Persian Etymology of فرزین (farzin)

According to the Wiktionary entry, the word derives "From Middle Persian [Book Pahlavi needed] (plcyn' /⁠frazēn⁠/, 'guard, (chess) queen')."

The documentation indicates the Middle Persian form was *frazēn*, which carried meanings relating to both a guardian figure and the chess piece. This etymological lineage shows the term's evolution from Middle Persian into Classical Persian and subsequently into modern dialects including Dari, Iranian Persian, and Tajik variants.

The entry does not mention Arabic فرزان/firzān or cite specific authorities beyond the reference to Hayyim's 1934 New Persian-English Dictionary. The earliest attested usage provided is from Rumi's Masnavi (c. 1260s), where the word appears in its chess context.
```


### [2026-09-14T00:55:42.706Z] TOOL RESULT

```
Web search results for query: "Persian پریر parīr "day before yesterday" etymology Middle Persian *parēr Avestan para ayar"

Links: [{"title":"پری - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C"},{"title":"A concise review of the Iranian calendar","url":"https://arxiv.org/pdf/astro-ph/0409620"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"},{"title":"Category:Middle Persian terms derived from Avestan - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Middle_Persian_terms_derived_from_Avestan"},{"title":"Introduction to Old Iranian - The Linguistics Research Center","url":"https://lrc.la.utexas.edu/eieol/aveol/0"},{"title":"Aban","url":"https://en.wikipedia.org/wiki/Aban"},{"title":"Zoroastrian Global Glossary | FEZANA","url":"https://fezana.org/glossary/"},{"title":"Persians - Wikipedia","url":"https://en.wikipedia.org/wiki/Persians"},{"title":"Persian Online – Grammar & Resources » Time List","url":"https://sites.la.utexas.edu/persian_online_resources/vocabulary-lists/time/"},{"title":"CHAPTER THREE OLD IRANIAN Prods Oktor Skjarv@ 1 INTRODUCTION *","url":"https://theswissbay.ch/pdf/Books/Linguistics/Mega%20linguistics%20pack/Indo-European/Iranian/Avestan%20&%20Old%20Persian;%20Old%20Iranian%20(Skj%C3%A6rv%C3%B8).pdf"}]

Based on the search results, I found detailed etymological information about the Persian word parīr (پریر) meaning "day before yesterday":

The word parīr (day before yesterday) comes from Middle Persian parīr/parēr, which derives from Proto-Iranian *parāyarah, composed of *para- combined with *ayarah (day). The *ayarah component compares with Avestan ayarə̄ (day), which ultimately traces back to Proto-Indo-European *h₂eyer- (day, morning).

This etymology shows a clear line of descent from Proto-Indo-European through Old Avestan to Middle Persian and into Modern Persian, with the word essentially meaning "the day before" (*para-) + "day" (*ayarah).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T00:55:50.046Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/portrait",
 "prompt": "Give the etymology chain for portrait and portray: Latin protrahere, Old French portraire, English. Quote the key sentences."
}
```


## [2026-09-14T00:55:50.877Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/prince",
 "prompt": "Give the etymology of prince: Latin princeps, its analysis (primus + capere), Old French prince, English. Quote key sentences."
}
```


### [2026-09-14T00:55:54.840Z] TOOL RESULT

```
# Etymology Chain: Portrait and Portray

## Latin to English Path

**Latin Origin:** The chain begins with Latin *protrahere*, meaning "to draw forth."

**Old French Intermediate:** This evolved into Old French *portraire*, defined as "to draw, to paint, portray."

**English Adoption:** Both terms entered English through French sources—*portray* in the mid-13c. and *portrait* in the 1560s.

## Key Quotes

On the Latin-to-French transition:
> "literally 'trace, draw forth,' from por- 'forth' (from Latin pro-; see pro-) + traire 'trace, draw,' from Latin trahere 'to drag, draw'"

On *portrait* specifically:
> "a back formation from portraiture or directly from French portrait, from Old French portret (13c.), noun use of past participle of portraire 'to paint, depict'"

The semantic thread remains consistent: all three forms relate to the act of drawing, painting, or creating a visual representation.
```


### [2026-09-14T00:55:56.492Z] TOOL RESULT

```
# Etymology of Prince

**Latin Origin:**
The word traces back to Latin *princeps* (genitive *principis*), meaning "first person, chief leader; ruler, sovereign." As the source explains: "noun use of adjective meaning 'that takes first,' from *primus* 'first'...+ root of *capere* 'to take.'"

**Component Analysis:**
The Latin term combines two elements:
- *primus* = "first"
- *capere* = "to take"

Together, they literally mean "one who takes first" or "the foremost."

**Old French Evolution:**
The word passed into Old French as *prince*, meaning "prince, noble lord," around the 12c., before entering Middle English around 1200.

**Semantic Development:**
Initially, *prince* designated "governor, overseer, magistrate; leader; great man, chief." By the mid-14th century, it narrowed to mean "heir apparent to a throne," and by the mid-15th century specifically denoted "king's son, scion of a royal family."

**German Cognate:**
Notably, the German word *Fürst* appears to be "apparently an imitation of the Latin formation."
```


## [2026-09-14T00:56:00.576Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/protein",
 "prompt": "Give the etymology of protein: who coined it, from French protéine, Greek prōteios, and the meaning 'of the first quality'. Quote key sentences."
}
```


## [2026-09-14T00:56:01.596Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/parameter",
 "prompt": "Give the etymology of parameter, and also of perimeter if mentioned: Modern Latin, Greek para + metron. Quote key sentences."
}
```


### [2026-09-14T00:56:05.171Z] TOOL RESULT

```
# Etymology of Protein

**Coiner:** Dutch chemist Gerhard Johan Mulder (1802-1880) coined the term in 1838, possibly on the suggestion of Berzelius.

**Etymology:** The word derives from French *protéine*, which comes from Greek *prōteios* meaning "the first quality," combining *prōtos* ("first") with the suffix *-ine*.

**Key Quote:**
"Originally a theoretical substance thought to be a constituent of food essential to life, further studies of the substances he was working with overthrew this, but the words protein and proteid continued to be used."

**Modern Definition:** A 1907 committee standardized terminology, establishing protein's current meaning as a "class of organic compounds forming an important part of all living organisms," while the older term *proteid* was abandoned.
```


### [2026-09-14T00:56:06.622Z] TOOL RESULT

```
# Etymology of Parameter and Perimeter

**Parameter** comes from Modern Latin *parameter* (1630s), derived from Greek *para-* meaning "beside, subsidiary" plus *metron* meaning "measure." As the source notes: "from Modern Latin *parameter* (1630s), from Greek *para-* 'beside, subsidiary'...+ *metron* 'measure.'"

Originally a geometry term from the 1650s, it expanded in meaning during the late 1920s to describe "measurable factor which helps to define a particular system," eventually becoming common by the 1950s.

**Perimeter** shares the same Greek root *metron*. It derives from Latin *perimetros*, combining Greek *peri* (around) with *metron* (measure). The etymology states: "from peri 'around, about'...+ *metron* 'measure.'" This term, dating to the early 15c., refers to "circumference, outer boundary, or border."

Both words illustrate how the Greek measuring root *metron* was combined with different prefixes to create distinct mathematical concepts.
```


## [2026-09-14T00:56:13.281Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/parliament",
 "prompt": "Give the etymology of parliament: Old French parlement, parler, Late Latin parabolare, Latin parabola, Greek parabole. Quote key sentences."
}
```


## [2026-09-14T00:56:15.596Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B1%D8%B3%D8%A7%D9%84",
 "prompt": "Give the Persian etymology of پارسال (pārsāl) 'last year' and of پار (pār), including any Proto-Iranian reconstruction and cognates (Sanskrit parut, Greek perusi)."
}
```


### [2026-09-14T00:56:18.020Z] TOOL RESULT

```
# Etymology of Parliament

The word "parliament" traces back through several linguistic layers:

**Old French Origin:**
"parliament" derives from Old French *parlement* (11c.), which originally meant "a speaking, talk," from the verb *parler* "to speak."

**Latin Development:**
The term evolved through Late Latin *parabolare* "to speak (in parables)," which came from Latin *parabola* meaning "speech, discourse."

**Key Quote:**
"consultation; formal conference, assembly," from Old French *parlement* (11c.), originally "a speaking, talk," from *parler* "to speak"

**Semantic Shift:**
By the mid-14c., the specific sense emerged referring to "representative assembly of England or Ireland," broadening from its original meaning of "a conference of the secular and/or ecclesiastical aristocracy summoned by a monarch."

The ultimate root connects to the concept of speaking and discourse, with the institutional meaning developing later as the word became associated with formal governmental assemblies in England.
```


### [2026-09-14T00:56:20.278Z] TOOL RESULT

```
# Persian Etymology of پارسال and پار

**پارسال (pārsāl) 'last year'** is "a compound of پار (pâr, 'last') +‎ سال (sâl, 'year')."

**پار (pār)** derives from Old Persian, tracing back to "Proto-Iranian *pr̥Hwo-, ultimately from Proto-Indo-European *per-" The entry notes that "cognates include English before."

The second component سال (sâl, 'year') comes from Middle Persian through Old Persian θard-/θarad-, reconstructed as "Proto-Iranian *carHdáh," ultimately from "Proto-Indo-Iranian *ćarHáts."

The Wiktionary entry does not provide Sanskrit or Greek cognate information beyond the English parallel to the PIE root *per-.
```


## [2026-09-14T00:56:32.326Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"فرزانه\\|فرود\\|پارسال\\|پریر\" ARY_pages.txt | head -20",
 "description": "Grep Aryanpur for relevant headwords"
}
```


### [2026-09-14T00:56:32.376Z] TOOL RESULT

```
13466:آلمانی فرودین میانه 05714۸00 10 قطان [ 63 نم
13468:آلمانی فرودین (05294407 0۷.): 1.01680 2 (736) :010/5
13474:چم این واژه در زبان آلمانی فرودین و لنونی: جست و خیز
```


## [2026-09-14T00:56:34.566Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"perperam\\|perperus\" LEW_1910.txt LAT.txt KLN_1966.txt 2>/dev/null | head -10; echo \"=== SYN before/first ===\"; grep -n \"perusi\\|parut\" SYN.txt POK_full.txt 2>/dev/null | head -10",
 "description": "Grep Latin dictionaries for perperus"
}
```


### [2026-09-14T00:56:34.641Z] TOOL RESULT

```
KLN_1966.txt:14378:Derivative:  fantasy,  tr.  and  intr.  v. fantoccini,  n.  pi.,  puppets;  a  puppet  show.  — It.,  pi.,  dimin.  of  fantocdo,  ‘puppet’,  dimin.  of fante,  ‘child’.  See  infant  and  cp.  fantassin. far,  adv.  and  adj.  —  ME.  fer,  feor,  fr.  OE.  feorr, adv.  and  adj.,  rel.  to  OS.  ferr,  fer ,  ON.  fjarre, OFris.  fer,  fir,  Du.  ver,  OHG.  ferro,  MHG. verre,  adv.,  OHG.  ferrana,  MHG.  verrene, verne,  ‘from  afar’,  G.  fern,  adj.  and  adv.,  Goth. fairra,  adv.,  fr.  I.-E.  base  *per-,  ‘through, across,  beyond’,  whence  also  OI.  parah,  ‘farth¬ er,  remoter,  ulterior’,  parah,  ‘beyond’  (adv.), Toch.  A  parne,  parnamhe,  ‘outer,  exterior’, Hitt,  para  (a  postpos.),  ‘outside  of’,  Arm.  heri, ‘far,  remote’,  Gk.  rrepa,  ‘across,  beyond’, trepaio?,  ‘being  or  dwelling  beyond’,  L.  per, ‘through’,  OIr.  ire,  ‘farther,  that  is  beyond’, and  prob.  L.  perperam,  ‘wrongly,  falsely’  (for *per-peram,  ‘beyond’).  See  fare,  ‘to  prosper’, and  cp.  fore,  adv.  Cp.  also  para-,  ‘beside’,  per, Perean,  peri-,  pro-.
LAT.txt:46632:(c£ osq. pertemust "peremerit "), peruerto, perperus, perfidus, periurus,
LAT.txt:46658:de ddviation qai est celai de perimS, de- pereo, perd 5 , perperus,
LAT.txt:46831:perperus, -a, rum: de trayera; et perperam adr. L’adjectif est
LAT.txt:49946:dans perei, perperus , etc., qui est ancien (v. per). Le suffixe aerait
LAT.txt:49949:marche pour le sens avec perperus. Le difficile est d' expliquer prd- ;
LAT.txt:50501:La formation rappelle celle de perperus. Dans un cas comme dans
=== SYN before/first ===
```


## [2026-09-14T00:56:40.611Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '46828,46845p' LAT.txt; echo \"=== leaf ===\"; awk 'NR<=46831{if(/\\f/) c++} END{print c}' LAT.txt",
 "description": "Read Ernout-Meillet perperus"
}
```


### [2026-09-14T00:56:41.712Z] TOOL RESULT

```
p 9 ro, -Snis m.: sorte de bottine, f aite de cuir crfi, et garnie de
poils, surtout en usage dans l'arn 4 e. Non attestS arant Vg. (Ae.7,690).
Ddrird: peronatus. Sana doute en rapport arec pera.
perperus, -a, rum: de trayera; et perperam adr. L’adjectif est
trfes rare (un ex. d'Accius ap.Non.150,11); 1'adverbe, qui est du
type clam, palam, protinam, aaaez frdquent, est ancien et appartient
plutot 4 la 1 . fanilifere. De per- et d'un second dldnent peu clair,
cf. properus. Pour le sena, cf .perdd, pereS et peut-etre prduus, aoua
per-. Ddrirds: perperitadG (Acc.), perpera, -as (ital.).Le grec a dga-
1 enent Ttepreepoc naia seulenent i basse dpoque (Polybe, Sextus, Arrien;
7tep7tepeta C 14 «u, 7 tep 7 iepOTnS Chrys.). Enprunt?
perpes, -etis; perpetuus, -a, -um; qui a'aranee d'une nani fere
continue; ininterroupu; perpdtuel. Perpes de per-pet-s (cf.impes,
praepes, et pete) 'a. dtd renplac 4 par perpetuus que farorisait 1'exis-
tence des synonynes assiduus, continuus, et ne ae troure que ehez
Pl.,Pac.Tr. R 3 188 et yhez lea archaasants de l*dpoq. inp. De perpetuus
ddrirent perpetualis (cr £4 par Quint. pour traduire xafioXucoC, cf.
Inst.Or.4,13,14); perpetuarius, perpetuitas (presque uniquenent cic 4 -
=== leaf ===
902
```


## [2026-09-14T00:57:38.700Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== parandush BQTv1 ===\"; grep -n \"رندوش\\|پرن \" BQT_v1_pages.txt | head -10; echo \"=== MON paran/parandush ===\"; grep -n \"پرندوش\\|پَرَن\\b\\|پرن:\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep for parandush/paran"
}
```


### [2026-09-14T00:57:38.784Z] TOOL RESULT

```
=== parandush BQTv1 ===
24957:چون سسنگه دیگیابه هقعه برجوزا کنار چون شرار دمگیایه یش‌او خیل‌پرن .
24994:. رل: پرن وپروین‎ - ٩
=== MON paran/parandush ===
```


## [2026-09-14T00:57:41.304Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24940,25000p' BQT_v1_pages.txt",
 "description": "Read BQT v1 context for paran"
}
```


### [2026-09-14T00:57:41.362Z] TOOL RESULT

```
ری نم اول و سکون تالی وکسن
اك و سکون تدتانی » نوعی از انگور باشد
و بعربی انگور را عتب گویند. .
بر هیو - بفتح اول وسکون نانی و فتح
ثالث و سکون تحتانی مجهول و واو. مرضی‌باشد
کهآ نرا عوام سوزالخوانند چه بوفت بول کردن
مجری‌بول بسوزش درآ بد وبعربی‌حرقةالبول گویند.
رت - ی وزن چمن ۰ پروین را گویند
و ند مش ات یا منم ات هر کروان
ور و بمربی ثربا خوانندش 4 - و نام حتزلی از
زبهر جهان برپدر کینه ور. ابوشکور بلخي.
که عمی داشت سالها برع ۰
عب‌عود سعد همدانی ۷اهوری ۰
این صورت رافرهنگه شموری بنقل ازمجمع آورده و بت فوق رامثال زده است تاسل
مت‌جر دبوان چابی طهران بدینگونه است:... که همی بودش ازفلك برتر: «لفت نامه».
۴ ر: پرمور  .‏ ۴ -رل: پرمو و پرموز ویرموزه. ۵ ركه: پزموویرمود.
۲۷ - رگ : پرماه . ۸۵ - رك : پروین :
چون سسنگه دیگیابه هقعه برجوزا کنار چون شرار دمگیایه یش‌او خیل‌پرن .
«منوچهری دامفالی۸».- و۳ -
منازل قمرحم هت۱ سویمعتی دیروز عم گفته‌اند
که روز گذخته باشد ار ؟ر ۴ ۰
پر نا بر وزن رعنا, دبای منقش لطیف
و تازكگ را گویند -
پر فالك ه بنم اول وسکون ثانی و نون
بالف کشیده ویکاف زده ءآدم جوان و اول مرا
کوننده - ونام‌طایفه ای حم‌هست از ترکان ۰۷
ر فج - ختح اول و ثانی ۷وسکون‌نون
وجیم . غلهای: باشد شبیه بگندم لیکن از کندم
باریکتر وضعیف تراشت.:
پر فف - بر وزن کمند.» بافتٌ ابربشمی
وحریر ساده را کونند ۵و پرتبان منفش‌رائیز
کفته اند و بمعتی زین پوش هم آهده
است - و بمعنی پروین هم حست که ناره های
پر داد
کوهان ئور باشد ٩‏ - .و ایغ وشمشیر و" جوهر
تیغ وشمشیر وامثالآنرا یز کویند*۱ - وبمعنی
خیار صحرابی هم هست - و مرغ و فربز را حم
کفته‌اند وآن سبزء نورسته باشد که دواب آنرا
برغبت تمام خورند۱9 .
پر نداخ ه ختح اول و انی وسکون
؟الث و دال بی نقطه بالف کشیده و بضای‌شطه‌دار
بر نداور ۱۴ « بفتح اول و واو بروزن
حسن ساغی » تيغ وشمشیر جوهودار را گونند.
ی
پر ند بفتح اولوئانی ورابم‌وسکون
تالث وکاف » يشته و کوه کوچك را گویند که دد
میان صحرا وافم شده باشد .
مرز ضبط کرده است.»
ار کس عازه چو چاء ذقنی شد بمثل
چونکه زرن قدحی در کف حسمین صنمی
۵ رک : ابر .
گر بود چاه ز دینار وز نقره ذفنا
با درخشنده چراغی ممبان برنا .
«منوچهریدامغانی۳؟.
. رل: پرن وپروین‎ - ٩
مبارزان فدر قدرت قنا قوت‎ ۰
ات او مت جک
ازرقی هر وی. «لفت نامه».
بامن هححنی ممرب آن «فر ند» (بکسراود ودوم) وأفر ندنیز آهله. دتشس؟. ۱-نیزه
سد دستی. ركك : برن (حاشیه) . ۴ رك : پراداخ و برنداق . ۴- از : بر ند
( جر شمشیر ).۲+ آور ( پسوید اصلف ) .پرعدوار
```


## [2026-09-14T00:57:55.938Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C%D8%B1%D9%88%D8%B2",
 "prompt": "Give the Persian etymology of پریروز and of پریر if mentioned: Middle Persian parēr, Proto-Iranian *para-ayarah, Avestan ayarə̄ 'day'."
}
```


### [2026-09-14T00:58:00.090Z] TOOL RESULT

```
# Persian Etymology of پریروز

Based on the Wiktionary entry provided, **پریروز** (pariruz) derives from a compound of two Persian words:

- **پری** (pari/parê) meaning "day before yesterday"
- **روز** (ruz) meaning "day"

The etymology tree traces پری back through Proto-Iranian *ráwčah and ultimately to Proto-Indo-European *léwk-os (related to concepts of light/day).

**Note:** The entry does not mention پریر or provide the Middle Persian, Proto-Iranian, and Avestan etymologies you referenced. Those details are not present in the source document provided.
```


## [2026-09-14T00:58:02.789Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C",
 "prompt": "Give the Persian etymology of پری (parê) 'the day before yesterday' — Middle Persian, Proto-Iranian *para-, Avestan ayarə̄. Quote the etymology section."
}
```


### [2026-09-14T00:58:09.433Z] TOOL RESULT

```
# Persian Etymology of پری (parê)

Based on the Etymology 3 section, the word پری meaning "the day before yesterday" derives from Middle Persian *parīr* through Proto-Iranian roots.

**Etymology Quote:**
"from [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[𐬞𐬭𐬌𐬭](/w/index.php?title=%F0%90%AC%9E%F0%90%AC%AD%F0%90%AC%8C%F0%90%AC%AD&action=edit&redlink=1 "𐬞𐬭𐬌𐬭 (page does not exist)")_ (prir /⁠parīr⁠/), from [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") _[\*parāyarah](/w/index.php?title=Reconstruction:Proto-Iranian/par%C4%81yarah&action=edit&redlink=1)_, from _[\*para-](/w/index.php?title=Reconstruction:Proto-Iranian/para-&action=edit&redlink=1)_ +‎ _[\*ayarah](/w/index.php?title=Reconstruction:Proto-Iranian/ayarah&action=edit&redlink=1)_ ("day")"

The compound structure combines the prefix *para-* with *ayarah* (day), which connects to Avestan *ayarə̄* sharing the same meaning. This ancient linguistic lineage traces the modern Persian temporal expression back through multiple historical language stages.
```


## [2026-09-14T00:58:16.942Z] TOOL CALL #58: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B2%D8%A7%D9%86%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B2%DB%8C%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B1%D8%B3%D8%A7%D9%84' \\\n 'https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C' \\\n 'https://www.etymonline.com/word/portrait' \\\n 'https://www.etymonline.com/word/prince' \\\n 'https://www.etymonline.com/word/protein' \\\n 'https://www.etymonline.com/word/parameter' \\\n 'https://www.etymonline.com/word/parliament' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 394, root Per 1 part 2, verification of Persian/English derivations' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


## [2026-09-14T00:58:19.588Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg394.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/394.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/394.png",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-14T00:58:20.991Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5440d437fbd4d540.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/97d4572f87fbba43.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b36319569ac0e8e6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ab7c5d4990c9e20.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf0f5a9ee3ee06a5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/096b092785a27b5d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/79be80f167a3fceb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d069427fe838dbd5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f70a5a05955383a6.txt
```


### [2026-09-14T00:58:21.052Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 96039 Sep 13 20:58 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/394.png
```


## [2026-09-14T00:58:23.456Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:10:36.940Z] TOOL CALL #60: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-394.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nE = \"https://www.etymonline.com/word/\"\n\nnodes = []\n\ndef N(**kw):\n    nodes.append(kw)\n\nN(\n id=1, lang=\"Old Persian\", words=\"fra; frava, fravata; fra-bar\",\n verdict=\"confirmed\",\n derivation=\"All three are genuine Old Persian. (a) fra- is the OP preverb/prefix 'before, forth' < PIE *pro, the o-grade/lengthened extension of *per- (Pokorny IEW 813-814 'g. pro, prō ... ai. prá-, av. frā, fra-, ap. fra- Präf. ‚vorwärts, voran; fort, weg‘'); Iranian regularly turns PIE *p before *r into f (*pro > fra), so OP fra- : Skt. prá- : Gk. pró : Lat. pro-. (b) fravata is the OP adverb 'forward, downward', attested at DSf 23f, 28; Kent analyses it as *frava- (an extension of fra- exactly like Gk. prōtos < *prowo-) plus the adverbial suffix -ta as in amata; Nourai's bare 'frava' is that extracted stem, not a separately attested word. (c) fra-bar is the compound fra- + bar- 'bear' > frābara 'he proffered, granted', the formula of the royal inscriptions (Auramazdā-maiy xšaçam frābara 'Ahuramazda granted me the kingship', DB 1.12, 25, 60 etc.); Nourai's cross-reference to root Bher 1 (PIE *bher- 'carry') is correct.\",\n derivation_fa=\"پیشوند fra- در پارسی باستان به معنی «پیش، به جلو» از هندواروپایی آغازین *pro می‌آید؛ در ایرانی پ؛ پیش از r به f بدل می‌شود (*pra- > fra-)، از این‌رو fra- هم‌ریشهٔ pra- سانسکریت، pró یونانی و pro- لاتین است (پوکورنی صفحهٔ ۸۱۳–۸۱۴). قید fravata «رو به جلو، رو به پایین» در سنگ‌نبشتهٔ داریوش در شوش (DSf) آمده و کنت آن را *frava- (گستردهٔ fra-) + پسوند قیدی -ta می‌داند. فعل مرکّب fra-bar ، یعنی frābara «بخشید، ارزانی داشت»، فرمول همیشگی کتیبه‌هاست. ادعای نورایی درست است.\",\n sources=[],\n ref_check=[\n   {\"ref\":\"POK:813\",\"status\":\"supports\",\"note\":\"Pokorny IEW 813 (local POK_03.txt, form-feed leaf 47) 'g. pro, prō ‚vorwärts, vorn, voran‘ ... Ai. prá- Präf. ‚vor, vorwärts, fort‘ ..., av. frā, fra-, ap. fra- Präf. ‚vorwärts, voran; fort, weg‘'.\"},\n   {\"ref\":\"KNT:198\",\"status\":\"supports\",\"note\":\"Kent, Old Persian, Lexicon p.198 (KNT.txt leaf 222): 'fravata adv. ‘forward, downward’: Phl. frōt, NPers. fārōd; from *frava-, extension of fra- as in Gk. πρῶτος ‘first’ from *prowos, + -tos as in amata ... DSf 23f, 28.' The prefix fra- itself is treated one page earlier (p.197).\"},\n   {\"ref\":\"KNT:200\",\"status\":\"supports\",\"note\":\"Kent, Lexicon p.200 s.v. bar-: 'fra- + bar- ‘proffer, grant’: frābara imf. AmH 7; AsH 9; DB 1.12, 25, 60; DPd 3f, 7f; DNa 33; DSf 11 ...' — exactly Nourai's fra-bar 'offer, grant'.\"}],\n consulted=[\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. per¹, section V\",\"stance\":\"supports\",\"note\":\"'V. Extended form *prē ... 4. Latin prē, pro-, before, for, instead of' and I.7 'Avestan pairi, around'; the AHD treats Iranian fra-/pairi- as part of the same root [Pok. 2. A. per 810].\"},\n   {\"src\":\"BRT\",\"where\":\"Altiranisches Wörterbuch, cols. 974 ff. (fra-)\",\"stance\":\"silent\",\"note\":\"BRT.txt OCR of the Avestan transliteration is too corrupt to quote the fra- article; grep of 'fra-bar', 'fravata' returned only garbled fragments.\"},\n   {\"src\":\"PHD\",\"where\":\"MacKenzie 1971 s.v. frōd\",\"stance\":\"supports\",\"note\":\"'frōd [plwt’ | M prwd, N furō(d)] down' (PHD_mackenzie.txt line 2398) — the Middle Persian continuation of OP fravata, confirming the OP form is the ancestor of the Persian branch.\"}])\n\nN(\n id=2, lang=\"Pahlavi\", words=\"frôt\",\n verdict=\"confirmed\",\n derivation=\"Middle Persian frōd / frōt 'down, downward', written <plwt'> in Book Pahlavi and <prwd> in Manichaean Middle Persian, continues OP fravata: the OP adverbial ending -ta is lost, and the sequence *frava- contracts to frō- (regular MP monophthongisation of *-awa- > -ō-). Kent states the equation outright at Lexicon p.198 ('fravata ... Phl. frōt, NPers. fārōd'); MacKenzie prints the voiced reading frōd (Book Pahlavi <t'> is ambiguous for final -d), so Nourai's 'frôt' is simply Kent's 1950 transliteration, not an error.\",\n derivation_fa=\"صورت فارسی میانهٔ frōd/frōt «فرو، پایین» (پهلوی کتابی <plwt'>، مانوی <prwd>) دنبالهٔ fravata ی پارسی باستان است؛ پسوند قیدی -ta افتاده و خوشهٔ *-awa- به واکهٔ کشیدهٔ ō بدل شده است. کنت خود همین زنجیره را می‌آورد و مکنزی صورت frōd را می‌نویسد؛ پس «frôt» نورایی همان آوانگاری کنت است و خطا نیست. ادعای نورایی درست است.\",\n sources=[],\n ref_check=[{\"ref\":\"KNT:198\",\"status\":\"supports\",\"note\":\"Kent p.198 s.v. fravata: 'Phl. frōt, NPers. fārōd' — the Pahlavi form and the arrow OP > Pahlavi are Kent's own (KNT.txt leaf 222).\"}],\n consulted=[\n   {\"src\":\"PHD\",\"where\":\"MacKenzie 1971 p.33-34 s.v. frōd (PHD_mackenzie.txt line 2398 / PHD.txt line 370)\",\"stance\":\"supports\",\"note\":\"'frōd [plwt’ | M prwd, N furō(d)] down. -mānd [-m?nd] deficiency, shortcoming.'\"},\n   {\"src\":\"HRN\",\"where\":\"Horn, Grundriss p.183 no. 825 (HRN.txt leaf 204)\",\"stance\":\"supports\",\"note\":\"'firōd, furōd, firō, furō ‚hinunter, unten‘, furōdīn ‚unterer‘ ... phlv. frōt.'\"},\n   {\"src\":\"NYB\",\"where\":\"Nyberg, Manual II (glossary)\",\"stance\":\"silent\",\"note\":\"grep of NYB_vol2_glossary.txt for 'frōt'/'frōd' returns nothing usable (OCR only yields 'farzanaa: frazānak' at line 6560).\"}])\n\nN(\n id=3, lang=\"Persian\", words=\"forŭ «فرو»; forŭtan «فروتن» (+ فرود)\",\n verdict=\"confirmed\",\n derivation=\"New Persian فرود furūd / فرو furū 'down, below' is the direct continuation of MP frōd: MP ō > NP ū, and the anaptyctic vowel of the initial cluster gives fu-rōd > furūd, with the final -d lost in the shortened adverb/preverb فرو. Horn (Grundriss p.183 no. 825) lists exactly the set 'firōd, furōd, firō, furō' and adds furōdīn 'lower' (whence the month-name فروردین is NOT derived — that is Av. fravaši-). فروتن furūtan 'humble, down-to-earth' is a transparent NP compound فرو 'down' + تن 'body' ('with body lowered'), first common in classical NP prose and poetry, so it is a New Persian formation on the inherited adverb rather than an inherited word itself.\",\n derivation_fa=\"«فرود» و صورت کوتاه‌شدهٔ آن «فرو» بازماندهٔ فارسی میانهٔ frōd است؛ ō ی فارسی میانه در فارسی نو به ū بدل شده و برای شکستن خوشهٔ آغازین واکه‌ای میانجی افزوده شده است (fr- > fu-r-). هرن در صفحهٔ ۱۸۳ همین زنجیره را می‌آورد. «فروتن» نیز ترکیبی است فارسی‌نو از «فرو» + «تن» یعنی «تن‌فروآورده، افتاده‌حال». ادعای نورایی درست است.\",\n sources=[],\n ref_check=[\n   {\"ref\":\"HRN:183\",\"status\":\"supports\",\"note\":\"Horn p.183 no. 825 (HRN.txt leaf 204): 'firōd, furōd, firō, furō ‚hinunter, unten‘, furōdīn ‚unterer‘ ... phlv. frōt. ai. pravát- ‚abschüssige Bahn‘, pravátā ‚bergab, abwärts‘; firōd setzt ein *pravát (schw. St.) voraus (Bartholomae, brieflich).' Exactly Nourai's arrow.\"},\n   {\"ref\":\"KNT:198\",\"status\":\"supports\",\"note\":\"Kent p.198: 'fravata ... Phl. frōt, NPers. fārōd' — the NP form is named in the same entry.\"},\n   {\"ref\":\"BQT:1473\",\"status\":\"not_checked\",\"note\":\"Borhan-e Qate’ p.1473 falls in vol. 3; the entry فرو/فرود was not located in the rough OCR of incoming/BQT/BQT_v3_pages.txt (greps for فرود return only unrelated verse lines). The neighbouring page 1459 (فرزانه) was found and checked, so the page range Nourai cites is the right part of the book.\"}],\n consulted=[\n   {\"src\":\"PHD\",\"where\":\"MacKenzie 1971 s.v. frōd\",\"stance\":\"supports\",\"note\":\"'frōd ... N furō(d)] down' — MacKenzie himself gives the New Persian outcome furō(d).\"},\n   {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien\",\"stance\":\"silent\",\"note\":\"grep of HUB.txt for 'furōd'/'firōd'/'vorgestern' finds no separate article; Hübschmann follows Horn's numbering and adds nothing here.\"},\n   {\"src\":\"ARY\",\"where\":\"Aryanpur, Farhang-e rishe-hā\",\"stance\":\"silent\",\"note\":\"grep of incoming/ARY/ARY_pages.txt for فرود returns only German-glossary lines (13466-13474), no headword.\"}])\n\nN(\n id=4, lang=\"Avestan\", words=\"paurva, parô, para 4, parâ 4; parô-ayare\",\n verdict=\"confirmed\",\n derivation=\"All four are genuine Avestan words of this root, and Nourai's 'para 4 / parâ 4' are Bartholomae's numbered homonyms. (a) paurva- (also pourva-) 'former, first' < PIE *perə-uo- (Pokorny 815: 'idg. perə-uo- in: ai. pūrva-, av. paurva-, pourva-, ap. paruva- ‚der vordere, frühere‘'). (b) parō 'before, in front of; except' is the ablative-genitive form of the stem *per- (Pokorny 813: 'av. parō Adv. ‚vorn, vor‘, Präp. ‚vor‘', beside Skt. puráḥ and Gk. páros). (c) para- 'ulterior, later, further' and the instrumental adverb parā 'before, forth' (Pokorny 814: 'av. para, ap. parā Adv. ‚zuvor‘, Präp. ‚vor‘'). (d) parō.ayara- 'the preceding day' is parō + ayar-/ayan- 'day' (PIE *h₂ey-er-), the exact Old Iranian prototype of Persian پریر (see node 5); Nourai's cross-reference to root Ayer is right, though 'last day' is better rendered 'the day before'.\",\n derivation_fa=\"هر چهار صورت اوستایی اند. paurva-/pourva- «پیشین، نخستین» از *perə-uo- هندواروپایی و هم‌ریشهٔ pūrva- سانسکریت و paruva- پارسی باستان است (پوکورنی صفحهٔ ۸۱۵). parō «پیش، جلو» برابر puráḥ سانسکریت و páros یونانی است (پوکورنی ۸۱۳)، و para-/parā «بعدی، پیش‌از» (پوکورنی ۸۱۴). ترکیب parō.ayara- یعنی «روز پیش» (parō + ayar- «روز») همان سرچشمهٔ «پریر» فارسی است. ادعای نورایی درست است.\",\n sources=[\"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C\"],\n ref_check=[\n   {\"ref\":\"POK:815\",\"status\":\"supports\",\"note\":\"Pokorny IEW 815 (POK_03.txt leaf 49): 'idg. perə-uo- in: ai. pūrva-, av. paurva-, pourva-, ap. paruva- ‚der vordere, frühere‘ (ai. pūrvyá-, av. paouruya- paoirya-, ap. paruviya ‚prior‘, dann ‚primus‘).'\"},\n   {\"ref\":\"POK:813\",\"status\":\"supports\",\"note\":\"Pokorny 813 (leaf 46): 'd. Peres, peros ... Ai. puráḥ Adv. und Präf. ‚voran, vorn‘, Präp. ‚vor‘, av. parō Adv. ‚vorn, vor‘, Präp. ‚vor‘, gr. πάρος.'\"},\n   {\"ref\":\"POK:810\",\"status\":\"supports\",\"note\":\"Pokorny 810 is where the article '2. per ‚das Hinausführen über‘' begins (leaf 43/44) — the root box itself.\"},\n   {\"ref\":\"HRN:61\",\"status\":\"partial\",\"note\":\"Horn p.61 no. 270 (HRN.txt leaf 82) is about NP pār, not about the Avestan words, and it warns: 'Ap. paruva- ‚früher‘ (aw. paurva-) ist schon im Pehlevi aufgegeben worden' — i.e. Horn denies that paurva- survived into Persian (see node 5).\"},\n   {\"ref\":\"AEF:376\",\"status\":\"not_checked\",\"note\":\"Khaleqi-Motlaq's Asās-e Eshteqāq-e Fārsi is not available online (refs_online.json: 'Not online'); it is the Persian rendering of Horn, whose corresponding article (no. 270, p.61) was checked instead.\"}],\n consulted=[\n   {\"src\":\"BRT\",\"where\":\"Altiranisches Wörterbuch, cols. 846-870 (para-, parō, paurva-)\",\"stance\":\"silent\",\"note\":\"BRT.txt OCR is unusable for these headwords; searches for 'paurva' return only running text fragments ('āhva paurvaṭāhva', 'paurva.naēmāṭ') which at least attest the stem in the Avesta but give no article text.\"},\n   {\"src\":\"WLD\",\"where\":\"Walde-Pokorny II 29 ff. (per-)\",\"stance\":\"supports\",\"note\":\"Pokorny's own closing reference for this article is 'WP. II 29ff.' (POK_03.txt leaf 49), i.e. Walde-Pokorny treats the same Avestan material under the same root.\"},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. per¹ I.7\",\"stance\":\"supports\",\"note\":\"'7. Avestan pairi, around: PARADISE.' The AHD assigns the Avestan preverbs of this family to per¹ [Pok. 2. A. per 810].\"}])\n\nN(\n id=5, lang=\"Persian\", words=\"(script only) پار ، پارسال ، پارینه ، پَرَن ، پَرَندوش ، پَریر ، پریروز ، پیرار ، پیرارسال\",\n verdict=\"plausible\",\n derivation=\"The set is genuine and all of it belongs to PIE *per-, but it has two different Old Iranian sources and Nourai hangs all of it on paurva-. (i) The parā/parō- compounds are exactly as charted: پریر parīr 'the day before yesterday' < MP parīr < Proto-Iranian *parā-yarah = *para- + *ayarah 'day' (= Av. parō.ayara-), with پریروز = پری(ر) + روز; پیرار pīrār 'two years ago' and پیرارسال are the parallel formation with *yār-/sāl 'year'; پَرَندوش 'the night before last' is para- + دوش 'last night'; پَرَن, which Borhan-e Qate’ glosses 'و به معنی دیروز هم گفته‌اند که روز گذشته باشد', belongs here too. (ii) پار pār 'last year' (with پارسال, پارینه) is contested: Horn (p.61 no.270) compares Skt. parút, Gk. πέρυσι, Kurd. par, Oss. faru, i.e. *par-ut = per- + *wet- 'year' (Pokorny 811 puts these 'in zeitlicher Verwendung' under per-), and expressly says OP paruva-/Av. paurva- 'was already given up in Pahlavi'; Wiktionary and Mo'in's own footnote in Borhan, on the other hand, do derive پار from Proto-Iranian *pṛHwo- (= paurva-), listing both sets of cognates. So Nourai follows one of two live opinions for پار, and is unambiguously right for the rest.\",\n derivation_fa=\"این خوشه همگی از ریشهٔ *per- است ولی دو سرچشمهٔ ایرانی باستان دارد. «پریر» از فارسی میانهٔ parīr و آن از ایرانی آغازین *parā-yarah (یعنی *para- «پیش» + *ayarah «روز»، برابر parō.ayara- ی اوستایی)؛ «پریروز»، «پیرار»، «پیرارسال» و «پرندوش» (para- + دوش) همان ساختارند و «پَرَن» را نیز برهان قاطع به معنی «دیروز» آورده است. امّا دربارهٔ «پار، پارسال، پارینه» دو نظر هست: هرن (ص ۶۱) آن را با parút سانسکریت و πέρυσι یونانی (یعنی *par-ut «در سال پیش») می‌سنجد و تصریح می‌کند که paruva- در پهلوی از میان رفته بوده؛ معین (حاشیهٔ برهان) و ویکی‌واژه آن را از *pṛHwa- (همان paurva-) می‌گیرند. پس نمودار نورایی با احتیاط پذیرفتنی است.\",\n sources=[\"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C\",\n          \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B1%D8%B3%D8%A7%D9%84\"],\n ref_check=[\n   {\"ref\":\"BQT:349\",\"status\":\"supports\",\"note\":\"Borhan-e Qate’ vol. 1, s.v. پار (BQT_v1_pages.txt leaf ≈564, printed ≈p.345-349; the footnote itself says بقیه در صفحهٔ ۳۵۰): Mo’in's note 7 reads 'در: پارسال، پارینه؛ قس سانسکریت parūt (در سال گذشته)؛ ارمنی heru (سال گذشته)، کردی par، افغانی parōs، آسی faru/farun، وخی pəray، سریکلی parwis (قس یونانی πέρυσι) پارسی باستان paruva (سابقاً)، اوستا paurva'. So BQT does connect پار with Av. paurva-, as Nourai's arrow requires — while also listing the parūt-type cognates.\"},\n   {\"ref\":\"BQT:397\",\"status\":\"not_found\",\"note\":\"The page-397 entry (presumably پریر/پرندوش) could not be isolated: greps of BQT_v1_pages.txt for پریر, پرندوش, پیرار return nothing (the OCR of this volume drops many headwords). The entry پَرَن was found (leaf ≈593) with the gloss 'و به معنی دیروز هم گفته‌اند که روز گذشته باشد'.\"},\n   {\"ref\":\"AEF:331,368,376\",\"status\":\"not_checked\",\"note\":\"Asās-e Eshteqāq-e Fārsi is not available online or on disk (refs_online.json).\"},\n   {\"ref\":\"ZMA:55\",\"status\":\"not_checked\",\"note\":\"Jonaydi, Zendegi va Mohājerat-e Āryāiān: refs_online.json records 'purchase only; no open copy found'.\"}],\n consulted=[\n   {\"src\":\"HRN\",\"where\":\"Horn p.61 no. 270 (HRN.txt leaf 82)\",\"stance\":\"contradicts\",\"note\":\"'pār ‚das vergangene Jahr‘, pārsāl, pārīn. skr. vergl. parút ‚im vergangenen Jahre‘ ... Ap. paruva- ‚früher‘ (aw. paurva-) ist schon im Pehlevi aufgegeben worden.' Horn derives پار from *par-ut, not from paurva-.\"},\n   {\"src\":\"POK\",\"where\":\"IEW 811 (POK_03.txt leaf 44)\",\"stance\":\"partial\",\"note\":\"'in zeitlicher Verwendung: ai. par-ūt, gr. πέρυσι usw. (s. unter uet- ‚Jahr‘)' — Pokorny places the 'last year' words under per- but as a compound with *wet- 'year', a different formation from perə-uo-.\"},\n   {\"src\":\"BQT\",\"where\":\"Borhan-e Qate’ vol. 1, s.v. پَرَن (BQT_v1_pages.txt line 24957 ff.)\",\"stance\":\"supports\",\"note\":\"'پرن – بر وزن چمن، پروین را گویند ... و به معنی دیروز هم گفته‌اند که روز گذشته باشد' — confirms the temporal sense of پَرَن that the chart presupposes.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann, IECD p.927 s.v. pēros (1)\",\"stance\":\"partial\",\"note\":\"'pēros, ā, om (1) ‚side, end‘ ... Av. parō, m. ‚end, edge, shore‘; Per. cf. pār ‚over, across‘' — Mann attaches Persian pār to the parō-family, but with the spatial, not the temporal, meaning.\"}])\n\nN(\n id=6, lang=\"Old Persian\", words=\"paruva; pariy; para; parâ\",\n verdict=\"confirmed\",\n derivation=\"All four are Kent's Old Persian lexicon headwords and both cited pages are exact. p.195: 'para prep. with acc. “beyond” (Av. parā “before”, Skt. purás, Gk. παρά)'; '²parā postpos. with acc. “along”, and verbal prefix “forth”'; 'pariy prep. and prefix “around, about”: Av. pairi, Skt. pári, Gk. περί, Lt. per, pIE *peri'. p.196: 'paruva- adj. “being before in time or place”: Av. paurva-, Skt. pūrva-, pIE *pruos', attested paruvā 'former' DB 4.51 and paruvam 'formerly' DB 1.9. Nourai's glosses ('early', 'around', 'later, beyond', 'along') reproduce Kent's almost word for word; only 'later' for para is Kent's separate entry '¹para- adj. “later”'.\",\n derivation_fa=\"هر چهار واژه سرواژهٔ فرهنگ پارسی باستان کنت اند و هر دو صفحهٔ مورد استناد نورایی درست است: در ص ۱۹۵ para «فراتر از»، parā «الونگ، به سوی جلو» و pariy «پیرامون» (هم‌ریشهٔ pairi اوستایی، pári سانسکریت، περί یونانی)؛ در ص ۱۹۶ paruva- «پیشین، نخستین» که در کتیبهٔ بیستون (paruvam «پیش‌از این») آمده است. ادعای نورایی درست است.\",\n sources=[],\n ref_check=[\n   {\"ref\":\"KNT:195\",\"status\":\"supports\",\"note\":\"Kent, Lexicon p.195 (KNT.txt leaves 218-219): '¹para- adj. “later” ... Av. para- “farther”, Skt. pára- “distant”, Gk. πέραν “beyond”'; '²para prep. with acc. “beyond”'; '²parā postpos. with acc. “along”, and verbal prefix “forth”'; 'pariy prep. and prefix “around, about”: Av. pairi, Skt. pári, Gk. περί, Lt. per, pIE *peri'.\"},\n   {\"ref\":\"KNT:196\",\"status\":\"supports\",\"note\":\"Kent p.196 (KNT.txt leaf 219): 'paruva- adj. “being before in time or place”: Av. paurva-, Skt. pūrva-, pIE *pruos ... paruvā npm. “former” DB 4.51. paruvam asn. as adv. “formerly” DB 1.9.'\"}],\n consulted=[\n   {\"src\":\"POK\",\"where\":\"IEW 810-815\",\"stance\":\"supports\",\"note\":\"p.810-811 'a. per, peri ... ai. pari, av. pairi, apers. pariy'; p.815 'ap. paruva- ‚der vordere, frühere‘'; p.814 'av. para, ap. parā Adv. ‚zuvor‘'.\"},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. per¹ I\",\"stance\":\"supports\",\"note\":\"'I. Basic form *per and extended form *peri ... 5. Greek peri, around, near, beyond ... 6. Sanskrit pari ... 7. Avestan pairi, around.'\"},\n   {\"src\":\"IEC\",\"where\":\"Mann, IECD p.927 s.v. pern-\",\"stance\":\"partial\",\"note\":\"'pern- (pernt-) ‚beyond, away, far‘ ... OPer. cf. parana-, adj. ‚former‘' — Mann lists the related OP adverb parana-, which Kent also derives from ²para/parā.\"}])\n\nN(\n id=7, lang=\"Sanskrit\", words=\"pra-jan\",\n verdict=\"plausible\",\n derivation=\"The underlying word is real: Sanskrit pra-jñā- (prajānāti 'discerns, understands beforehand', prajñā f. 'discernment, wisdom', prajñāna- n. 'knowledge'), from pra- 'fore-' (< PIE *pro, this root) + jñā- 'to know' (< PIE *ǵneh₃-, whence Nourai's cross-reference to root Gnô). The printed form 'pra-jan' is the book's own shorthand for the verb stem (Horn writes 'ai. pra + √jñā-, jānāti'), not an attested Sanskrit citation form; and Pokorny p.813, which Nourai cites, does not contain this word at all — p.813-814 is where av./ap. fra- and Skt. prá- are treated, so the citation supports only the pra- element.\",\n derivation_fa=\"واژهٔ واقعی سانسکریت prajñā- / prajānāti «پیشاپیش دانستن، دریافتن» است، مرکّب از پیشوند pra- (از همین ریشهٔ *per-/*pro) و ستاک jñā- «دانستن» (از *ǵneh₃- هندواروپایی، همان ریشهٔ Gnô که نورایی ارجاع می‌دهد). صورت «pra-jan» که در کتاب چاپ شده صورتی استنادی سانسکریت نیست بلکه کوتاه‌نوشتی نورایی از pra + √jñā است (هرن نیز همین را می‌نویسد). افزون بر آن صفحهٔ ۸۱۳ پوکورنی فقط پیشوند pra- را پوشش می‌دهد. پس ادعا با احتیاط پذیرفتنی است.\",\n sources=[\"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B2%D8%A7%D9%86%D9%87\"],\n ref_check=[{\"ref\":\"POK:813\",\"status\":\"partial\",\"note\":\"Pokorny 813-814 (POK_03.txt leaf 47) has 'g. pro, prō ... Ai. prá- Präf. ‚vor, vorwärts, fort‘ (vor Subst. und Verben)' but no compound with jñā-; the jñā- element is under Pokorny's ǵenə- (IEW 376 ff.).\"}],\n consulted=[\n   {\"src\":\"HRN\",\"where\":\"Horn p.181 no. 815 (HRN.txt leaf 202)\",\"stance\":\"supports\",\"note\":\"'ferzāne ‚weise, gelehrt‘, ferzānegī. ai. pra + √jñā-, jānāti- ‚erkennen, verstehen‘; phlv. frazānak bezw. farzānak.' Horn uses the same pra + jñā analysis Nourai charts.\"},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. gnō-\",\"stance\":\"supports\",\"note\":\"the AHD appendix root gnō- 'to know' supplies the second element; Watkins lists Sanskrit jānāti under it.\"},\n   {\"src\":\"BQT\",\"where\":\"Borhan-e Qate’ vol.3 p.≈1459, Mo’in's footnote 3 to فرزانه\",\"stance\":\"supports\",\"note\":\"'پهلوی frazānak ... هندی/سانسکریت pra (پیشوند بمعنی پیش) + jñā/jānāti (شناختن، فهمیدن)، قس: دانستن، اسشق ۸۱۵' (i.e. Horn no. 815).\"}])\n\nN(\n id=8, lang=\"Pahlavi\", words=\"farzânak\",\n verdict=\"plausible\",\n derivation=\"Middle Persian frazānag (Book Pahlavi <plc’nk’>, Parthian frz’ng) 'wise, intelligent' is real and is indeed *fra-jñā-na-ka-, the Iranian match of the Sanskrit formation: Iranian *fra- for Indic pra-, Iranian *zan-/*zān- for Indic jñā-/jān- (Proto-Indo-Iranian *ǵ(h)nā- > Indic jñā-, Iranian zān-), plus the participial -āna- and the adjectival -ak/-ag. What the chart draws as descent (Sanskrit → Pahlavi) is in fact cognacy: Middle Persian did not borrow from Sanskrit but inherited the same Indo-Iranian compound. Wiktionary flags the Sanskrit link accordingly as 'perhaps related to Sanskrit प्रज्ञान'. Nourai's gloss 'smart' and the reading 'farzānak' (the later, an-anaptyctic pronunciation) are both defensible.\",\n derivation_fa=\"فارسی میانهٔ frazānag (پهلوی کتابی plc’nk’، پارتی frz’ng) «دانا، خردمند» بازماندهٔ *fra-jñā-na-ka- است: در ایرانی *fra- برابر pra- ی هندی و ستاک zān-/zan- برابر jñā- ی هندی است (هندوایرانی *ǵnā- در هندی j و در ایرانی z می‌دهد). نکتهٔ مهم آنکه پیکان نورایی (سانسکریت ← پهلوی) وام‌گیری نیست بلکه هم‌ریشگی است؛ فارسی میانه این واژه را از سانسکریت نگرفته بلکه هر دو از هندوایرانی آغازین به ارث برده‌اند. پس با احتیاط پذیرفتنی است.\",\n sources=[\"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B2%D8%A7%D9%86%D9%87\"],\n ref_check=[{\"ref\":\"BQT\",\"status\":\"supports\",\"note\":\"Borhan-e Qate’ (Mo’in ed.) vol. 3, footnote 3 on the page carrying فرزانه (incoming/BQT/BQT_v3_pages.txt line 18205 area, pdf leaf 252 ≈ printed p.1459): 'پهلوی frazānak ... از: فرزانک (= فرزانه)'. Nourai's bare 'BQT' citation is therefore accurate.\"}],\n consulted=[\n   {\"src\":\"PHD\",\"where\":\"MacKenzie 1971 p.33 s.v. frazānag (PHD.txt line 354)\",\"stance\":\"supports\",\"note\":\"'frazānag [plc’nk’ | P frz’ng, N farzāna] wise, intelligent. ~īh: wisdom, intelligence.'\"},\n   {\"src\":\"NYB\",\"where\":\"Nyberg, Manual II glossary (NYB_vol2_glossary.txt line 6560)\",\"stance\":\"supports\",\"note\":\"'farzanaa: frazānak' — the OCR preserves the headword equation MP frazānak = NP farzāna.\"},\n   {\"src\":\"HRN\",\"where\":\"Horn p.181 no. 815\",\"stance\":\"supports\",\"note\":\"'phlv. frazānak bezw. farzānak' — Horn gives both readings, which is exactly Nourai's 'farzânak'.\"}])\n\nN(\n id=9, lang=\"Persian\", words=\"Farzâneh «فرزانه» (+ فرزین)\",\n verdict=\"plausible\",\n derivation=\"فرزانه farzāna 'wise, sage' is the straightforward New Persian continuation of MP frazānag: intervocalic -g is lost and the final vowel written -h/-e appears (MP -ag > NP -a), and the initial cluster fr- is broken by anaptyxis (fra- > far-). Wiktionary derives it from MP frazānag citing MacKenzie 1971 p.33; Horn no. 815 and Mo’in's footnote in Borhan (p.≈1459) give the same chain. The bracketed extra فرزین farzīn 'queen (chess piece)' is another matter: MacKenzie lists it as a separate headword, 'frazēn [plcyn’ | N farzīn] (chess) queen (lit. “guard”)', and Wiktionary follows him — so its link to farzāna/pra-jñā- is folk-etymological rather than established, even though Persian tradition has long associated the chess 'counsellor' with the 'wise man'.\",\n derivation_fa=\"«فرزانه» بی‌هیچ واسطه‌ای دنبالهٔ frazānag ی فارسی میانه است: پسوند -ag در فارسی نو به -a (هٔ بیان) بدل شده و خوشهٔ آغازین fr- با واکهٔ میانجی شکسته شده است (fra- > far-). مکنزی (ص ۳۳)، هرن (شمارهٔ ۸۱۵) و حاشیهٔ معین بر برهان قاطع همین زنجیره را می‌آورند. امّا افزودن «فرزین» به این خوشه پذیرفتنی نیست: مکنزی آن را سرواژه‌ای جداگانه می‌آورد: frazēn «نگهبان؛ (در شطرنج) وزیر»، و پیوند آن با «فرزانه» بیشتر ریشه‌شناسی عامیانه است.\",\n sources=[\"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B2%D8%A7%D9%86%D9%87\",\n          \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B2%DB%8C%D9%86\"],\n ref_check=[\n   {\"ref\":\"BQT:1459\",\"status\":\"supports\",\"note\":\"Borhan-e Qate’ vol. 3, printed p.≈1459 (incoming/BQT/BQT_v3_pages.txt, pdf leaf 252, tag [pdf page 253] follows): footnote 3 'فرزان (ه.م.). پهلوی frazānak ... هندی pra (پیشوند بمعنی پیش) + jñā/jānāti (شناختن، فهمیدن) ... اسشق ۸۱۵'. With the volume-3 offset (printed = pdf + ≈1207) the page Nourai cites is exact.\"},\n   {\"ref\":\"HRN:181\",\"status\":\"supports\",\"note\":\"Horn p.181 no. 815 (HRN.txt leaf 202): 'ferzāne ‚weise, gelehrt‘, ferzānegī. ai. pra + √jñā-, jānāti- ‚erkennen, verstehen‘; phlv. frazānak bezw. farzānak.'\"}],\n consulted=[\n   {\"src\":\"PHD\",\"where\":\"MacKenzie 1971 p.33 (PHD.txt lines 354, 358)\",\"stance\":\"partial\",\"note\":\"'frazānag ... N farzāna] wise, intelligent' supports فرزانه; but two lines later 'frazēn [plcyn’ | N farzīn] (chess) queen (lit. “guard”)' keeps فرزین apart from it.\"},\n   {\"src\":\"MON\",\"where\":\"Mo’in's footnote in BQT (above) and Farhang-e Fārsi s.v. فرزانه\",\"stance\":\"supports\",\"note\":\"Mo’in's Borhan note is the same text used in the Farhang; the entry فرزین is cross-referenced there only as 'ورک: فرز' — not to فرزانه.\"},\n   {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien\",\"stance\":\"silent\",\"note\":\"no separate article; Hübschmann's Part I follows Horn's numbering and adds nothing to no. 815.\"}])\n\nN(\n id=10, lang=\"Germanic\", words=\"fer, fruma, furista\",\n verdict=\"confirmed\",\n derivation=\"Three genuine Proto-Germanic stems of this root, exactly as Watkins sets them out: *fer(e)ra- (from the suffixed comparative *per-ero- 'farther away'), *fruma-/*furma- 'first, foremost' (from the superlative *pro-mo- / *pr-mo-), and *furista- 'foremost' (from *pro-isto-). Germanic f- for PIE *p- is Grimm's Law; the zero-grade *pr- gives *fur- (Old English for, forth, further), the e-grade *per- gives *fer- (Old English feor(r)). Nourai's citation is AHD without a page, and the AHD appendix entry per¹ contains all three.\",\n derivation_fa=\"هر سه ستاک ژرمنی آغازین‌اند: *fer(e)ra- «دورتر» (از صورت برتری *per-ero-)، *fruma-/*furma- «نخستین» (از *pro-mo-/*pr-mo-) و *furista- «نخستین، پیشاپیش» (از *pro-isto-). تبدیل p ی هندواروپایی به f در ژرمنی همان قانون گریم است. ادعای نورایی درست است.\",\n sources=[],\n ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. per¹ (AHD_watkins1985.txt line 836): 'I.2. Suffixed (comparative) form *per-ero-, farther away, in Germanic *fer(e)ra- in Old English feor(r), far: FAR'; 'III.1.a. Germanic *fruma-, *furma- in Old English forma, first, foremost: FOREMOST, FORMER²'; 'III.2. Suffixed (superlative) form *pro-isto- in Germanic *furista-, foremost, in Old English fyrst, fyrest, first: FIRST.'\"}],\n consulted=[\n   {\"src\":\"POK\",\"where\":\"IEW 813-815\",\"stance\":\"supports\",\"note\":\"p.813 'ahd. as. furi ‚vor, für, vorbei‘ ... Superl. furist, mhd. vürst ‚erster, vornehmster‘, as. furist, ags. fyr(e)st, engl. first'; p.815 'got. fruma ‚erster‘ (Sup. frumists)' and 'as. formo, ags. forma ‚erster‘'.\"},\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. far (KLN_1966.txt line 14378)\",\"stance\":\"supports\",\"note\":\"'far ... fr. OE. feorr ... Goth. fairra, adv., fr. I.-E. base *per-, ‚through, across, beyond‘ ... Cp. also para-, ‚beside‘, per, Perean, peri-, pro-.'\"},\n   {\"src\":\"WLD\",\"where\":\"Walde-Pokorny II 29 ff.\",\"stance\":\"supports\",\"note\":\"Pokorny's article closes 'WP. II 29ff.' — the same Germanic material is gathered under per- there.\"}])\n\nN(\n id=11, lang=\"English\", words=\"far, for, former, first\",\n verdict=\"confirmed\",\n derivation=\"All four come down from the Germanic stems of node 10 with no complication: OE feor(r) > ME fer > far; OE for (preposition, and the pejorative prefix for-) from zero-grade *fur; OE forma 'first' + the comparative -er (a double comparative) > former; OE fyrst/fyrest > first. Watkins's per¹ entry names each English outcome in capitals (FAR; FOR, FOR-; FOREMOST, FORMER²; FIRST), so Nourai's node is a direct transcription of the AHD appendix.\",\n derivation_fa=\"هر چهار واژهٔ انگلیسی بی‌هیچ پیچیدگی از همان ستاک‌های ژرمنی می‌آیند: feor(r) ی انگلیسی کهن > far؛ for از صورت صفرمرتبهٔ *fur؛ former از forma «نخستین» + پسوند برتری -er؛ و first از fyrst/fyrest. واتکینز در پیوست AHD همین چهار را ذیل per¹ می‌آورد. ادعای نورایی درست است.\",\n sources=[],\n ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. per¹: 'FAR' (I.2), 'II.1.a. Old English for, before, instead of, on account of: FOR; b. Old English for-, prefix ...: FOR-', 'FOREMOST, FORMER²' (III.1.a), 'FIRST' (III.2).\"}],\n consulted=[\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. far\",\"stance\":\"supports\",\"note\":\"'far ... fr. I.-E. base *per- ‚through, across, beyond‘ ... See fare, ‚to prosper‘, and cp. fore, adv.'\"},\n   {\"src\":\"SKT\",\"where\":\"Skeat, Concise Etym. Dict.\",\"stance\":\"silent\",\"note\":\"grep of SKT.txt for the headwords returns the entries but with no root-level statement beyond 'AS. feor'; nothing that bears on the arrow.\"}])\n\nN(\n id=12, lang=\"Latin\", words=\"per, pro; prô-tahere; primo-capus; para-meter\",\n verdict=\"transcription_suspect\",\n derivation=\"per and pro are impeccable (Pokorny 810-811 'lat. per (*per oder *peri)', 814 'lat. pro-, prō- in Kompositis, prō Präp.'), although Nourai's gloss 'first, forward, along' conflates the senses of per, pro and the superlative prīmus. The other three items are problems. (a) 'prô-tahere' is not a Latin word: the source of portrait is prō-trahere 'to draw forth' (> Old French portraire 'to draw, paint' > Middle English portraien, and the noun portrait 1560s). The -r- is simply missing; the printed page (pdf 394) shows the same 'prô-tahere', so this is Nourai's own misprint and the extraction is faithful. (b) 'primo-capus' is Nourai's rendering of the standard analysis of princeps < *prīmo-caps '(he) who takes first place', prīmus + the root of capere — the sense is right, the reconstructed shape is not a form any dictionary prints. (c) para-meter is placed under Latin, but it is a 1630s Modern Latin coinage from Greek para- 'beside' + metron 'measure', not an inherited Latin word.\",\n derivation_fa=\"per و pro ی لاتین کاملاً درست‌اند (پوکورنی ۸۱۰–۸۱۴). امّا صورت «prô-tahere» واژه‌ای لاتین نیست؛ درست آن prō-trahere «پیش کشیدن، نگاریدن» است که از راه portraire ی فرانسوی کهن به portrait رسیده است؛ حرف r افتاده و چون همین صورت در صفحهٔ چاپی کتاب هم هست، خطای چاپی کتاب است نه خطای خوانش اسکن. «primo-capus» نیز بازسازی شخصی نورایی از princeps < *prīmo-caps («آنکه جایگاه نخست را می‌گیرد») است؛ معنا درست و صورت نادرست است. سرانجام para-meter واژه‌ای لاتینی نو (سدهٔ ۱۷م) از یونانی para + metron است و جایاش شاخهٔ یونانی است.\",\n error_in=\"book\",\n book_prints=\"prô-tahere : to draw forward ; primo-capus : first in rank, prince\",\n correct_form=\"prō-trahere 'to draw forth'; princeps < *prīmo-caps\",\n sources=[E+\"portrait\", E+\"prince\", E+\"parameter\"],\n ref_check=[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 s.v. per¹ has 'I.4. Latin per, through, for, by: PER, PER-' and 'V.4. Latin prē, pro-, before, for, instead of: PRO¹, PRO-¹' and 'VI.4.a.ii Latin compound princeps, “he who takes first place” (-ceps, “-taker”; see kap-), leader, chief, emperor: PRINCE' — but the AHD nowhere prints 'prōtahere', 'primo-capus' or 'para-meter' as Latin forms.\"}],\n consulted=[\n   {\"src\":\"POK\",\"where\":\"IEW 810-811, 814\",\"stance\":\"supports\",\"note\":\"p.811 'lat. per (*per oder *peri)'; p.814 'lat. pro-, prō- in Kompositis, prō Präp. ‚vor, für‘'; p.815-816 'lat. prīmus (aus *pr-is-mos)' and 'Latin compound princeps' material under *preis-mo-.\"},\n   {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. per, prō\",\"stance\":\"supports\",\"note\":\"LAT.txt carries the per/prō articles with the same IE analysis; the file also confirms that no lemma 'protahere' exists (grep returns nothing).\"},\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. portrait, prince\",\"stance\":\"supports\",\"note\":\"Klein derives portrait from OF portraire < VL *protrahere and prince from L. princeps < *prīmo-caps — i.e. the corrected forms.\"}])\n\nN(\n id=13, lang=\"French\", words=\"(no words given)\",\n verdict=\"confirmed\",\n derivation=\"An empty pass-through box: the Latin words of node 12 reached English (node 15) and modern Persian (node 14) through French. That is historically right for portrait (OF portret, noun use of the past participle of portraire, 13c.) and prince (OF prince 'prince, noble lord', 12c., into Middle English c.1200); per, perimeter and parameter came into English more from Latin/Modern Latin than from French, and the modern Persian words of node 14 are 19th-20th c. French loans.\",\n derivation_fa=\"این جعبه تهی است و تنها نقش واسطه دارد: واژه‌های لاتین از راه فرانسه به انگلیسی و به فارسی نو رسیده‌اند. این مسیر برای portrait (از portret ی فرانسوی کهن، سدهٔ ۱۳م) و prince (سدهٔ ۱۲م) کاملاً درست است؛ امّا per و perimeter و parameter بیشتر از لاتین (و لاتینی نو) به انگلیسی راه یافته‌اند.\",\n sources=[E+\"portrait\", E+\"prince\"],\n ref_check=[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins marks the English outcomes but not the French intermediary; the AHD appendix never states the route, so this box rests on Nourai's own arrangement.\"}],\n consulted=[\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. portrait, prince\",\"stance\":\"supports\",\"note\":\"Klein: 'portrait, n. — F., prop. pp. of portraire, “to portray”'; 'prince, n. — F., fr. L. princeps'.\"},\n   {\"src\":\"FSD\",\"where\":\"Funk & Wagnalls Standard Dictionary\",\"stance\":\"silent\",\"note\":\"not consulted separately; Klein and Etymonline agree and the chain is uncontroversial.\"}])\n\nN(\n id=14, lang=\"Persian\", words=\"(script only) پارامتر ، پُرتره ، پرنسس\",\n verdict=\"confirmed\",\n derivation=\"Three modern French loans in Persian, all borrowed in the late Qajar/Pahlavi period through French as the language of Iranian higher education: پارامتر < paramètre, پُرتره < portrait (the Persian spelling with final ه reflects the French pronunciation [pɔʁtʁɛ], not the English), پرنسس < princesse. The chart's route French → Persian is right; the words did not come through Arabic or English. Mo’in marks such items with the tag [فر.] 'French' in the Farhang-e Fārsi, which is what Nourai's bare 'MON' citation refers to.\",\n derivation_fa=\"هر سه وام‌واژهٔ فرانسوی اند که در دورهٔ قاجار و پهلوی، از رهگذر آموزش عالی فرانسه‌زبان، وارد فارسی شده‌اند: «پارامتر» از paramètre، «پُرتره» از portrait (هٔ پایانی نشانهٔ تلفّظ فرانسوی است نه انگلیسی) و «پرنسس» از princesse. معین این‌گونه واژه‌ها را با نشانهٔ [فر.] می‌آورد. ادعای نورایی درست است.\",\n sources=[E+\"portrait\", E+\"prince\", E+\"parameter\"],\n ref_check=[{\"ref\":\"MON\",\"status\":\"partial\",\"note\":\"Mo’in's Farhang-e Fārsi vol. 4 collects the foreign words; the local OCR (MON_part1/2.txt) covers the lexicon volumes and does not carry پارامتر/پرنسس as headwords, so the citation could only be checked for the style of tagging ([فر.]) and not for these three items.\"}],\n consulted=[\n   {\"src\":\"MON\",\"where\":\"Farhang-e Fārsi (vajehyab text, MON_part2.txt)\",\"stance\":\"silent\",\"note\":\"grep for پارامتر / پرنسس / پرتره in the local Mo’in OCR returns nothing — these belong to the separate volume of foreign compounds.\"},\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. princess, portrait, parameter\",\"stance\":\"supports\",\"note\":\"Klein confirms the French forms princesse and portrait and the Modern Latin parameter that Persian borrowed.\"}])\n\nN(\n id=15, lang=\"English\", words=\"per, perimeter, parameter, portrait, prince\",\n verdict=\"plausible\",\n derivation=\"portrait (1560s, from French portrait, noun use of the past participle of portraire < VL *protraire < Lat. prōtrahere) and prince (c.1200, OF prince < Lat. princeps 'first person, chief') are exactly as charted; per is the Latin preposition taken over directly. But perimeter (early 15c.) is Latin perimetros from Greek περίμετρος = peri 'around' + metron 'measure', and parameter (Modern Latin, 1630s) is Greek para- + metron: both belong under the Greek node 16, not under the Latin → French chain, and neither reached English through French. The root is the same throughout, so the verdict is 'plausible' only because of the misrouting.\",\n derivation_fa=\"portrait (سدهٔ ۱۶م، از فرانسه، و آن از prōtrahere ی لاتین) و prince (حدود ۱۲۰۰ م.، از princeps ی لاتین) دقیقاً همان‌اند که نمودار می‌گوید. امّا perimeter از περίμετρος ی یونانی (peri + metron) و parameter از para + metron ی یونانی (از راه لاتینی نو، سدهٔ ۱۷م) است و هیچ‌کدام از راه فرانسه نیامده‌اند؛ جایای درستشان شاخهٔ یونانی است. پس ادعا در کلیّات درست و در مسیر نادقیق است.\",\n sources=[E+\"portrait\", E+\"prince\", E+\"parameter\"],\n ref_check=[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins per¹ has 'I.4 Latin per ...: PER, PER-' and 'VI.4.a.ii ... PRINCE', but lists PERIMETER/PARAMETER under the Greek sections (I.5 'Greek peri, around, near, beyond: PERI-') rather than under Latin.\"}],\n consulted=[\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. perimeter, parameter, portrait, prince\",\"stance\":\"partial\",\"note\":\"Klein sends perimeter to Gk. περίμετρος and parameter to Gk. παρά + μέτρον, confirming the misrouting; portrait and prince agree with the chart.\"},\n   {\"src\":\"SKT\",\"where\":\"Skeat\",\"stance\":\"silent\",\"note\":\"Skeat's entries add nothing beyond the Latin/French chain.\"}])\n\nN(\n id=16, lang=\"Greek\", words=\"proto-; para; para-bolâre; proto-inin; proto-kolla; para-sitos\",\n verdict=\"transcription_suspect\",\n derivation=\"para (παρά 'beside, along with', Pokorny 814 'gr. παρά, πάρα'), proto- (πρῶτος 'first' < *prōw-ato-, Pokorny 815), πρωτόκολλον 'the first sheet glued to a papyrus roll' (prōtos + kolla 'glue') and παράσιτος 'one who eats at another's table' (para + sitos 'grain, food') are all genuine and correctly glossed. Two entries are not Greek as printed: (a) 'para-bolâre' is Late/Vulgar Latin parabolāre 'to speak (in parables)', built on Latin parabola < Greek παραβολή (para + bállein 'to throw'); it is the ancestor of French parler and so of parliament, and Nourai's cross-reference to root Gwel 1 (*gʷelԥ- 'to throw') is right, but the form belongs to Latin. (b) 'proto-inin' is not a Greek word at all: protein was coined in 1838 by G. J. Mulder (on Berzelius's suggestion) as French protéine from Greek πρωτεῖος prōteios 'of the first quality' + the chemical suffix -ine. The printed page (pdf 394) shows 'proto-inin' exactly as the JSON has it, so the fault is the book's.\",\n derivation_fa=\"παρά، πρῶτος، πρωτόκολλον («نخستین برگ چسبانده‌شده») و παράσιτος («هم‌خوراک، مهمان ناخوانده») همگی واژه‌های راستین یونانی‌اند. امّا دو مورد نادرست چاپ شده‌اند: «para-bolâre» لاتینی پسین است (parabolāre «سخن گفتن»، از parabola و آن از παραβολή ی یونانی)، نه یونانی؛ و «proto-inin» هیچ صورت یونانی نیست، بلکه protein در ۱۸۳۸ توسط مولدر از فرانسهٔ protéine و آن از πρωτεῖος «از مرتبهٔ نخست» ساخته شده است. چون همین صورت‌ها در صفحهٔ چاپی کتاب هم هست، خطای چاپی کتاب است نه خطای خوانش اسکن.\",\n error_in=\"book\",\n book_prints=\"para-bolâre : to throw (talk) around ; proto-inin : of prime value\",\n correct_form=\"Late Latin parabolāre (< Gk. παραβολή); Gk. πρωτεῖος prōteios 'of the first quality'\",\n sources=[E+\"protein\", E+\"parliament\"],\n ref_check=[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 s.v. per¹: 'III.3.b suffixed (superlative) Greek form *prōw-ato- in Greek prōtos, first, foremost: PROTEIN, PROTIST, PROTO-, PROTON' and 'IV.2. Greek para, beside, alongside of, beyond: PARA-¹; PALFREY' — so the AHD supplies prōtos and para but prints neither 'proto-inin' nor 'para-bolâre'.\"}],\n consulted=[\n   {\"src\":\"POK\",\"where\":\"IEW 814-815 (POK_03.txt leaves 47-48)\",\"stance\":\"supports\",\"note\":\"p.814 'gr. παρά, πάρα Verbalpräf. ... Präp. ‚an etwas hin, entlang, neben‘'; p.815 'aber gr. πρῶτος ds. aus *pṛ-to- (umgebildet aus *pṛ-mo- ds.)'.\"},\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. protein, protocol, parasite, parabola\",\"stance\":\"supports\",\"note\":\"Klein derives protein from Gk. πρωτεῖος 'of the first quality', protocol from πρωτόκολλον 'first leaf glued to a manuscript', parasite from παράσιτος 'eating at the table of another'.\"},\n   {\"src\":\"SYN\",\"where\":\"Buck, Dict. of Selected Synonyms\",\"stance\":\"silent\",\"note\":\"grep of SYN.txt for these items returns nothing relevant; Buck treats concepts, not these technical loans.\"}])\n\nN(\n id=17, lang=\"French\", words=\"(no words given)\",\n verdict=\"confirmed\",\n derivation=\"Another empty transit box. It is historically accurate for parliament (OF parlement 11c., from parler < Late Latin parabolāre), for protocol (French protocole, 16c., from Medieval Latin protocollum), for protein (French protéine, 1838) and for the Persian loans of node 18, all of which are French-mediated. parasite, parabola, paragraph and parallel came into English at least as much from Latin as from French, so the box is a simplification rather than an error.\",\n derivation_fa=\"این نیز جعبه‌ای تهی و واسطه است. مسیر فرانسه برای parliament (از parlement ی فرانسوی کهن، سدهٔ ۱۱م)، protocol، protein (protéine، ۱۸۳۸) و همهٔ وام‌واژه‌های فارسی گره ۱۸ درست است؛ ولی parasite و parabola و paragraph بیشتر از لاتین به انگلیسی راه یافته‌اند؛ پس این جعبه ساده‌سازی است نه خطا.\",\n sources=[E+\"parliament\", E+\"protein\"],\n ref_check=[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"The AHD appendix lists the English words but never names French as the intermediary, so the box reflects Nourai's own arrangement.\"}],\n consulted=[\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. parliament, protocol\",\"stance\":\"supports\",\"note\":\"Klein: 'parliament ... fr. OF. parlement, fr. parler, “to speak”'; 'protocol ... fr. F. protocole, fr. ML. protocollum'.\"},\n   {\"src\":\"SKT\",\"where\":\"Skeat s.v. parliament\",\"stance\":\"supports\",\"note\":\"Skeat marks parliament '(F.-L.-Gk.)', the same three-stage route.\"}])\n\nN(\n id=18, lang=\"Persian\", words=\"(script only) پارازیت ، پُرتُکل ، پارلمان ، پرتئین (JSON: پروتکل ، پروتئین)\",\n verdict=\"confirmed\",\n derivation=\"Four French loanwords of the Constitutional/Pahlavi era: پارازیت < parasite (in Persian mainly in the radio sense 'interference', a French technical use), پروتکل < protocole, پارلمان < parlement (used beside the native-Arabic مجلس), پروتئین < protéine. All four go back through French to the Greek forms of node 16, so the chain drawn is right. Note a discrepancy between page and data: the printed page prints پُرتُکل and پرتئین (without و), while the JSON gives the standard modern spellings پروتکل and پروتئین — the extraction has silently normalised Nourai's spelling.\",\n derivation_fa=\"هر چهار وام‌واژهٔ فرانسوی عصر مشروطه و پهلوی اند: «پارازیت» از parasite (در فارسی بیشتر به معنی پارازیت رادیویی)، «پروتکل» از protocole، «پارلمان» از parlement و «پروتئین» از protéine. مسیر یونانی ← لاتین/فرانسه ← فارسی درست است. یک نکته: در صفحهٔ چاپی «پُرتُکل» و «پرتئین» (بی‌واو) آمده، در حالی که دادهٔ استخراج‌شده صورت معیار امروزی را آورده است — یعنی خطای خوانش اسکن (نه خطای کتاب).\",\n sources=[E+\"protein\", E+\"parliament\"],\n ref_check=[{\"ref\":\"MON\",\"status\":\"partial\",\"note\":\"Mo’in tags such items [فر.] in the Farhang; the four words are in vol. 4 (foreign compounds), which is not in the local OCR, so the specific entries could not be read.\"}],\n consulted=[\n   {\"src\":\"MON\",\"where\":\"MON_part2.txt (lexicon volumes)\",\"stance\":\"silent\",\"note\":\"grep for پارازیت / پروتکل / پارلمان / پروتئین returns nothing — these are in the separate foreign-words volume.\"},\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. protein, protocol, parliament, parasite\",\"stance\":\"supports\",\"note\":\"Klein gives the French forms protéine, protocole, parlement, parasite that Persian borrowed.\"}])\n\nN(\n id=19, lang=\"English\", words=\"parasite, parallel, protein, parabola, parliament, protocol, paragraph\",\n verdict=\"confirmed\",\n derivation=\"All seven are Greek-based and all contain para-/pro-/prōtos of this root: parasite (παράσιτος), parallel (παράλληλος 'beside one another'), parabola (παραβολή), paragraph (παράγραφος 'a mark written alongside'), protocol (πρωτόκολλον), protein (πρωτεῖος + -ine, Mulder 1838) and parliament (OF parlement < parler < Late Latin parabolāre < parabola < παραβολή) — a doublet chain in which parabola and parliament go back to the same Greek word by learned and popular routes respectively. Watkins lists PARA-¹ and PROTEIN, PROTO- under per¹.\",\n derivation_fa=\"هر هفت واژه یونانی‌تبارند و پیشوند para-/pro-/prōtos را در خود دارند. نکتهٔ جالب آنکه parabola و parliament دوگانهٔ (doublet) یک واژه‌اند: اوّلی راه عالمانه و دومی راه مردمی را از παραβολή به لاتینی پسین parabolāre و از آنجا به parler و parlement پیموده است. ادعای نورایی درست است.\",\n sources=[E+\"parliament\", E+\"protein\"],\n ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. per¹: 'IV.2. Greek para, beside, alongside of, beyond: PARA-¹; PALFREY' and 'III.3.b ... Greek prōtos, first, foremost: PROTEIN, PROTIST, PROTO-, PROTON.'\"}],\n consulted=[\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. parallel, paragraph, parabola, parliament\",\"stance\":\"supports\",\"note\":\"Klein derives all of them from παρά compounds and notes parliament's chain OF parlement < parler < VL. *paraulāre/parabolāre.\"},\n   {\"src\":\"SKT\",\"where\":\"Skeat s.v. parable, parliament, parasite\",\"stance\":\"supports\",\"note\":\"Skeat tags parable '(F.-L.-Gk.)' and parliament '(F.-L.-Gk.)', i.e. the doublet relationship the chart implies.\"}])\n\nN(\n id=20, lang=\"Indo-European\", words=\"Per-per-os\",\n verdict=\"plausible\",\n derivation=\"The form is taken verbatim from Mann's Indo-European Comparative Dictionary p.927, where it is a headword: 'perperos ‚flighty, giddy‘. Cf. peros (2) Gk. pærperos, adj. ‚fickle, rash, vain‘; Lat. perperus, id., cf. also perperam, adv. ‚rashly, vainly‘; Per. farfar, s. “hurry”' — so gloss, language label and even the Persian attachment are Mann's, not Nourai's invention. Pokorny, however, sets up no such Indo-European lexeme: at IEW 811 he merely lists 'lat. per-peram ‚verkehrt‘, per-perus ‚falsch‘, woraus gr. πέρπερος ‚Geck‘' under the adjective *peros, i.e. he treats the Greek word as a loan from Latin. Ernout-Meillet go further: for them the second element of perperus is 'peu clair' and the late attestation of πέρπερος (Polybius, Sextus, Arrian) makes it probably a borrowing. A reduplicated PIE *per-per-os is therefore a reconstruction only Mann defends.\",\n derivation_fa=\"این سرواژه عیناً از فرهنگ تطبیقی من (Mann) صفحهٔ ۹۲۷ گرفته شده است، که همانجا فارسی «فرفر» را هم ذیل آن می‌آورد. امّا پوکورنی چنین واژهٔ هندواروپایی‌ای بازنمی‌سازد و در صفحهٔ ۸۱۱ تنها می‌نویسد که πέρπερος ی یونانی از perperus ی لاتین گرفته شده است؛ ارنو-میه‌یه نیز جزء دوم perperus را «ناروشن» می‌خواند. پس بازسازی *per-per-os را تنها من می‌پذیرد و ادعای نورایی با احتیاط پذیرفتنی است.\",\n sources=[],\n ref_check=[\n   {\"ref\":\"IEC:927\",\"status\":\"supports\",\"note\":\"Mann, IECD p.927 (IEC.txt line 12771, form-feed leaf 511, on which the printed number '927' appears): 'perperos ‚flighty, giddy‘. Cf. peros (2) Gk. pærperos, adj. ‚fickle, rash, vain‘; Lat. perperus, id. cf. also perperam, adv. ‚rashly, vainly‘; Per. farfar, s. “hurry”'. The page number is exact.\"},\n   {\"ref\":\"POK:811\",\"status\":\"partial\",\"note\":\"Pokorny 811 (POK_03.txt leaf 45) has 'lat. per-peram ‚verkehrt‘, per-perus ‚falsch‘, woraus gr. πέρπερος ‚Geck‘' but no IE headword *per-per-os.\"},\n   {\"ref\":\"POK:810\",\"status\":\"supports\",\"note\":\"p.810 is where the article '2. per' opens — the Latin/Greek perper- words are treated inside it.\"}],\n consulted=[\n   {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. perperus (LAT.txt line 46831, leaf 902)\",\"stance\":\"contradicts\",\"note\":\"'perperus, -a, -um: de travers; et perperam adv. ... De per- et d’un second élément peu clair, cf. properus ... Le grec a également πέρπερος mais seulement à basse époque (Polybe, Sextus, Arrien) ... Emprunt?' — i.e. no inherited IE *perperos.\"},\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. far\",\"stance\":\"partial\",\"note\":\"'and prob. L. perperam, ‚wrongly, falsely‘ (for *per-peram, ‚beyond‘)' — Klein accepts the root but analyses per-peram as per- + a second element, not as a reduplication.\"},\n   {\"src\":\"WLD\",\"where\":\"Walde-Pokorny II 29 ff.\",\"stance\":\"silent\",\"note\":\"Pokorny's 'WP. II 29ff.' reference covers the per- article; no separate *perperos lemma is set up there either.\"}])\n\nN(\n id=21, lang=\"Persian\", words=\"farfar «فَرفَر»\",\n verdict=\"disputed\",\n derivation=\"The word is real — Mo’in's Farhang-e Fārsi has 'فرفر: (ق.) به تندی، به شتاب' (adverb 'quickly, in haste'), which is exactly Nourai's 'in hurry', and the Anvari verse quoted on the chart is genuine — but the derivation is not. Mo’in supplies no etymology and no bracketed origin tag; the immediately following entries فرفره 'a leather disc whirled on a string by children, so that a فرفر sound comes from it; بادفر' and فرفره 'paper whirligig' show the family to be echoic — the whirring noise itself is called فرفر. A reduplicated onomatopoeia of this shape is productive in Persian (جلز و ولز, تلو تلو, زرزر) and needs no PIE ancestor; there is also no Middle Persian antecedent. The only authority for the arrow is Mann (IECD 927), whose Persian comparanda are notoriously freehand. Modern scholarship would call فرفر onomatopoeic, not an inherited reflex of *per-per-os.\",\n derivation_fa=\"واژه واقعی است و معین آن را چنین آورده: «فرفر: (ق.) به تندی، به شتاب» — یعنی همان معنایی که نورایی می‌دهد. امّا معین هیچ ریشه‌ای برای آن نمی‌آورد و هیچ نشانهٔ خاستگاه نمی‌گذارد؛ مدخل‌های پس از آن («فرفره» چرمی مدوّر که کودکان می‌چرخانند تا «صدای فرفر» برآید) نشان می‌دهد که این خانواده نام‌آوایی (محاکات صدا) است و مانند «تلوتلو» و «زرزر» ساختهٔ خود فارسی است؛ صورت فارسی میانه‌ای هم برای آن گواهی نشده است. تنها منبع این پیکان، من (Mann) است. پژوهش امروزی آن را رد می‌کند و فرفر را نام‌آوا می‌داند.\",\n sources=[],\n ref_check=[\n   {\"ref\":\"IEC:927\",\"status\":\"supports\",\"note\":\"Mann p.927 s.v. perperos ends 'Per. farfar, s. “hurry”' — Nourai's arrow is Mann's, verbatim.\"},\n   {\"ref\":\"MON:2521\",\"status\":\"partial\",\"note\":\"Mo’in, Farhang-e Fārsi (MON_part2.txt line 6403): 'فرفر: (ق.) به تندی، به شتاب.' The word and gloss are confirmed; but Mo’in gives no etymology at all, so the reference supports the meaning, not the descent from an IE root.\"}],\n consulted=[\n   {\"src\":\"MON\",\"where\":\"MON_part2.txt lines 6403-6412\",\"stance\":\"contradicts\",\"note\":\"The neighbouring entries make the family echoic: 'فرفر: [= فرفره] (اسم.) چرمی مدور که کودکان ریسمانی در آن گذارند و در کشاکش آورند تا از آن صدای فرفر ظاهر شود؛ بادفر' and 'فرفره: (اس.) کاغذ پاره‌ای که بر سر چوبی تعبیه کنند ... تا باد آن را به گردش در آورد'.\"},\n   {\"src\":\"PHD\",\"where\":\"MacKenzie 1971\",\"stance\":\"silent\",\"note\":\"no Middle Persian *farfar / *frafr; grep of PHD.txt and PHD_mackenzie.txt returns nothing.\"},\n   {\"src\":\"HRN\",\"where\":\"Horn, Grundriss\",\"stance\":\"silent\",\"note\":\"no entry; grep of HRN.txt for 'ferfer'/'farfar' finds nothing — Horn did not regard it as an inherited word.\"}])\n\nN(\n id=22, lang=\"Latin\", words=\"perperus\",\n verdict=\"confirmed\",\n derivation=\"Latin perperus is genuine but very rare (one attestation, Accius ap. Nonius 150,11); the common word of the family is the adverb perperam 'wrongly, amiss', which is old and colloquial. Pokorny prints both on the page Nourai cites (811) and glosses perperus 'falsch' (false, wrong), perperam 'verkehrt'; Nourai's gloss 'rashly' is Mann's rendering of perperam ('rashly, vainly'), so both glosses are defensible but they are not the same sense. The first element is per- 'through, beyond' with pejorative force (cf. perdō, pereō); Ernout-Meillet leave the second element unexplained.\",\n derivation_fa=\"واژهٔ لاتین perperus واقعی ولی بسیار کمیاب است (تنها یک شاهد از آکیوس)؛ صورت رایج‌تر قید perperam «نادرست، واژگونه» است. پوکورنی در همان صفحهٔ ۸۱۱ که نورایی یاد کرده هر دو را می‌آورد، امّا معنای «نادرست» می‌دهد نه «شتابزده»؛ معنای نورایی از من گرفته شده است. جزء نخست per- با بار معنایی منفی است (مانند perdō، pereō)، و جزء دوم ناروشن است. ادعای نورایی درست است.\",\n sources=[],\n ref_check=[\n   {\"ref\":\"POK:811\",\"status\":\"supports\",\"note\":\"Pokorny IEW 811 (POK_03.txt leaf 45): 'lat. per-peram ‚verkehrt‘, per-perus ‚falsch‘, woraus gr. πέρπερος ‚Geck‘'. Page number exact; gloss 'falsch', not 'rashly'.\"},\n   {\"ref\":\"IEC:927\",\"status\":\"supports\",\"note\":\"Mann p.927: 'Lat. perperus, id. cf. also perperam, adv. ‚rashly, vainly‘' — the source of Nourai's gloss.\"}],\n consulted=[\n   {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. perperus (LAT.txt line 46831)\",\"stance\":\"partial\",\"note\":\"'perperus, -a, -um: de travers ... L’adjectif est très rare (un ex. d’Accius ap. Non.150,11); l’adverbe ... est ancien et appartient plutôt à la l. familière. De per- et d’un second élément peu clair.' Confirms the word and the per- element, doubts the analysis.\"},\n   {\"src\":\"LEW\",\"where\":\"Walde, Lateinisches etym. Wörterbuch\",\"stance\":\"silent\",\"note\":\"grep of LEW_1910.txt for 'perperus'/'perperam' returns no hit in the OCR.\"},\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. far\",\"stance\":\"partial\",\"note\":\"'prob. L. perperam, ‚wrongly, falsely‘ (for *per-peram, ‚beyond‘)' — Klein attaches it to *per-, hedged with 'prob.'\"}])\n\nentry = {\n \"entry\": 0,\n \"root\": \"Per 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *per- / *peri, *pro, *prē, *prai- 'forward, through, around, before' (Pokorny IEW 810-816, '2. per: das Hinausführen über'; Watkins/AHD per¹ 'around')\",\n \"note\": \"The root box is accurate. Pokorny's article '2. per' runs pp.810-816 and opens exactly on the page Nourai cites; its sections cover per/peri 'around, through' (a), peros 'farther' (b), prai/prei (c), peres/peros (d), pr- (e), perā (f), pro/prō (g) and preti/proti (h) — i.e. precisely the double gloss 'around, forward'. Watkins's AHD appendix prints 'per¹. “Around.” ... [Pok. 2. A. per 810]' and closes with 'Other possibly related forms are grouped under per-², per-³, per-⁴, per-⁵, and per-⁶', which is the source of Nourai's cross-references to 'Per 2', 'Per 3' and 'Per 4'. PART 2 of the chart carries the Iranian, Germanic, Latin, Greek and modern-loan branches. Two nodes print forms that do not exist in that shape (node 12 'prô-tahere' for Latin prōtrahere; node 16 'proto-inin' for Greek prōteios) — both are on the printed page, so they are the author's misprints, not extraction errors. One real extraction discrepancy: node 18 prints پُرتُکل and پرتئین on the page but the JSON has the normalised پروتکل and پروتئین. The one substantive etymological objection on the page is node 21 (Persian فرفر), which rests on Mann alone and is almost certainly onomatopoeic.\",\n \"note_fa\": \"جعبهٔ ریشه درست است. مقالهٔ «2. per» در فرهنگ پوکورنی از صفحهٔ ۸۱۰ تا ۸۱۶ امتداد دارد و دقیقاً از همان صفحه‌ای آغاز می‌شود که نورایی آورده است؛ بخش‌های آن (per/peri، peros، prai/prei، parā، pro/prō، preti) همان دو معنای «پیرامون، به پیش» را پوشش می‌دهد. واتکینز در پیوست AHD می‌نویسد «per¹. Around ... [Pok. 2. A. per 810]» و همانجا به per² تا per⁶ ارجاع می‌دهد، که منبع ارجاعات نورایی به «Per 2» تا «Per 4» است. دو گره صورت‌های ناموجود چاپ کرده‌اند (prô-tahere به جای prōtrahere و proto-inin به جای prōteios) که هر دو خطای چاپی خود کتاب است. تنها ایراد جدی ریشه‌شناختی این صفحه، گره ۲۱ («فرفر») است که تنها بر گفتهٔ من تکیه دارد و به حتم نام‌آواست.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C\"],\n \"ref_check\": [\n   {\"ref\":\"POK:810\",\"status\":\"supports\",\"note\":\"Pokorny IEW 810 (POK_03.txt leaf 43 end / leaf 44 start): the article opens '2. per ‚das Hinausführen über‘. A. Dient als Präposition, Präverb und Adverb: a. per, peri (Lokative des Wurzelnomens) ‚vorwärts, im Hinausgehen, Hinübergehen über, im Durchdringen, im Übermaß‘ ...' and runs to p.816 ('WP. II 29ff., EM.² 754f. ...').\"}],\n \"consulted\": [\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 pp.49-50 s.v. per¹ (AHD_watkins1985.txt line 836)\",\"stance\":\"supports\",\"note\":\"'per¹. “Around.” I. Basic form *per and extended form *peri ... [Pok. 2. A. per 810.]' plus the closing 'Other possibly related forms are grouped under per-², per-³, per-⁴, per-⁵, and per-⁶' — the exact source of the chart's cross-references.\"},\n   {\"src\":\"WLD\",\"where\":\"Walde-Pokorny II 29 ff.\",\"stance\":\"supports\",\"note\":\"Pokorny's own closing reference for the article is 'WP. II 29ff.' (POK_03.txt leaf 49); WLD_band3 (the index volume) is all that is on disk, and it confirms the volume/page assignment.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann, IECD pp.925-930 (per-, pern-, pēros, perperos)\",\"stance\":\"supports\",\"note\":\"Mann has a dense series of per- headwords on these pages ('pern- ‚beyond, away, far‘', 'pēros (1) ‚side, end‘', 'perperos ‚flighty, giddy‘'), confirming the root's existence and shape.\"},\n   {\"src\":\"SYN\",\"where\":\"Buck, Dict. of Selected Synonyms\",\"stance\":\"silent\",\"note\":\"grep of SYN.txt for 'perusi', 'parut' and the per- prepositions returns nothing usable; Buck's concept sections do not treat prepositions.\"}],\n \"nodes\": nodes,\n}\n\nout = {\n \"pdf_page\": 394,\n \"book_page\": 364,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry],\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-394.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(out,f,ensure_ascii=False,indent=1)\nprint(\"written\", len(nodes), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-394.py",
 "description": "Build page-394.json"
}
```


### [2026-09-14T01:10:38.485Z] TOOL RESULT

```
written 22 nodes
```


## [2026-09-14T01:10:42.554Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-394.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 394",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-14T01:10:43.760Z] TOOL RESULT

```
JSON OK
nodes verified: 22/22
node verdicts: {'confirmed': 13, 'plausible': 6, 'transcription_suspect': 2, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 23, 'not_checked': 4, 'partial': 11, 'not_found': 1}
books consulted: {'supports': 33, 'silent': 16, 'contradicts': 3, 'partial': 8} | by book: {'KLN': 12, 'PHD': 6, 'HRN': 5, 'POK': 5, 'AHD': 4, 'MON': 4, 'SKT': 4, 'WLD': 3, 'LAT': 3, 'BRT': 2, 'NYB': 2, 'HUB': 2, 'BQT': 2, 'IEC': 2, 'ARY': 1, 'FSD': 1, 'SYN': 1, 'LEW': 1}
```


## [2026-09-14T01:10:50.424Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\np=\"data/verification/page-394.json\"\nd=json.load(open(p,encoding=\"utf-8\"))\nns=d[\"entries\"][0][\"nodes\"]\nn13=[n for n in ns if n[\"id\"]==13][0]\nn13[\"consulted\"]=[c for c in n13[\"consulted\"] if c[\"src\"]!=\"FSD\"]\nn13[\"consulted\"].append({\"src\":\"SKT\",\"where\":\"Skeat s.v. portrait, prince\",\"stance\":\"supports\",\"note\":\"Skeat tags both '(F.-L.)', i.e. French from Latin — the route this box draws.\"})\njson.dump(d,open(p,\"w\",encoding=\"utf-8\"),ensure_ascii=False,indent=1)\nprint(\"ok\")\nPYEOF\npython3 tools/verify_check.py 394",
 "description": "Fix FSD entry and re-check"
}
```


### [2026-09-14T01:10:51.591Z] TOOL RESULT

```
ok
nodes verified: 22/22
node verdicts: {'confirmed': 13, 'plausible': 6, 'transcription_suspect': 2, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 23, 'not_checked': 4, 'partial': 11, 'not_found': 1}
books consulted: {'supports': 34, 'silent': 15, 'contradicts': 3, 'partial': 8} | by book: {'KLN': 12, 'PHD': 6, 'HRN': 5, 'POK': 5, 'SKT': 5, 'AHD': 4, 'MON': 4, 'WLD': 3, 'LAT': 3, 'BRT': 2, 'NYB': 2, 'HUB': 2, 'BQT': 2, 'IEC': 2, 'ARY': 1, 'SYN': 1, 'LEW': 1}
```


## [2026-09-14T01:11:12.184Z] AGENT

Page 394 (book p. 364), root **Per 1** part 2 — 1 entry, 22 nodes, all covered. `verify_check.py 394` shows 0 PROBLEM lines.

**Verdicts:** root confirmed; nodes: 13 confirmed, 6 plausible, 2 transcription_suspect, 1 disputed.

**Disputed**
- #21 Persian فَرفَر *farfar* "in hurry" — real word (Mo'in: «به تندی، به شتاب») but Mo'in gives no etymology; neighbouring فرفره «صدای فرفر» shows the family is echoic, and there is no MP antecedent. The only authority for descent from IE *per-per-os is Mann (IECD 927). Modern view: onomatopoeic.

**Transcription_suspect (both `error_in: "book"` — printed page matches the JSON)**
- #12 Latin `prô-tahere` — no such Latin word; portrait goes back to **prōtrahere**. (Same node: `primo-capus` is Nourai's ad-hoc shape for *prīmo-caps* > *princeps*, and `para-meter` is Greek/Modern Latin, misfiled under Latin.)
- #16 Greek `proto-inin` — not Greek; protein < Fr. protéine < Gk. **prōteios** 'of first quality' (Mulder 1838). Same node: `para-bolâre` is Late Latin *parabolāre*, not Greek.

**Extraction error for the owner to fix**
- Node #18 `script_extra`: the page prints **پُرتُکل** and **پرتئین** (no و); the JSON has the normalised پروتکل / پروتئین.

**Other notable findings**
- Nourai's page citations are unusually accurate here: KNT 195/196 (para, parā, pariy, paruva-), KNT 198 (*fravata … Phl. frōt, NPers. fārōd*), KNT 200 (*fra- + bar- 'proffer, grant'*), POK 811/813/815, HRN 181 (ferzāne) and 183 (firōd), BQT 1459 (فرزانه, Mo'in's footnote citing Horn no. 815), IEC 927 (*perperos … Per. farfar*) all check out verbatim.
- #5: Horn p.61 **contradicts** the specific arrow Av. *paurva-* → NP پار ("Ap. paruva- … ist schon im Pehlevi aufgegeben worden"; he derives it from *par-ut, cf. Skt. parút, Gk. πέρυσι), while Mo'in's own Borhan footnote and Wiktionary support it — marked plausible with both views given. The parā-compounds (پریر، پیرار، پرندوش) are solid (PIr. *parā-yarah).
- #9: MacKenzie keeps **فرزین** apart — *frazēn* "guard, (chess) queen" — so its inclusion under farzāna/pra-jñā- is folk-etymological.
- #8: the Sanskrit → Pahlavi arrow is cognacy, not descent (MP *frazānag* inherited, not borrowed).

Page PNG archived at `data/verification/sources/refs/ocr/BOOK/394.png`; 9 web pages archived via `fetch_source.py`.
