# Verification process log — verify-page-521


## [2026-10-16T05:13:01.578Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 521 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-521.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-521.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-521.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 521` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.614Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:07.384Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:07.403Z] TOOL RESULT

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


## [2026-10-16T05:13:07.890Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-521.txt"
}
```


### [2026-10-16T05:13:07.910Z] TOOL RESULT

```
1	=== PDF page 521 (book page 491) ===
2	--- entry 0 ---
3	ROOT [Mongolian] Urmak : to strike  (refs KLN:742)
4	#1 (parent #0) [Mongolian] refs=KLN:742 | Urdu : camp of strikers, army camp
5	#2 (parent #0) [Turkish] refs=KLN:742,1861 | ordu : camp
6	  #3 (parent #2) [Persian] refs=KLN:1861; MON:197; NAT:14 | ordŭ «اردو» : camp, army, also a "camp language" that was originally spoken by an Indian army of Hindi, Persian, Turkish and Arab soldiers. | extra: اردوگاه ، اردوکشی ، اردوبیگ
7	    #4 (parent #3) [Hindustani] refs=KLN:1681 | urdu : Hindustani language
8	      #5 (parent #4) [English] refs=KLN:1681 | Urdu : an Indian language
9	#6 (parent #0) [French] refs=KLN:742; AHD | 
10	  #7 (parent #6) [English] refs=AHD:634; KLN | hoard : a wandering tribe, group, camp
11	--- entry 1 ---
12	ROOT [Indo-European] Uroiks, Loik : twist, twine, wicker, beard  (refs IEC:704,1593)
13	#1 (parent #0) [Avestan] refs=HRN:142; IEC:104,1593 | raeša : hair, beard
14	  #2 (parent #1) [Pahlavi] refs=BQT:988; SOD:348 | rěš : beard ; rěšak : (hairy) root
15	    #3 (parent #2) [Persian] refs=BQT:988,989; HRN:142; IEC:704,1593 | rîš 2 «ریش٢» : beard ; rîšeh «ریشه» : root
16	  #4 (parent #1) [Sogdian] refs=SOD:348 | ryš`kk : beard
17	#5 (parent #0) [Latin] refs=IEC:704 | lîcium : woof, yarn
18	--- entry 2 ---
19	ROOT [Avestan] Urvan : spirit, soul  (refs SYN:1088; BQT:967)
20	#1 (parent #0) [Pahlavi] refs=BQT:967 | ruvân : spirit
21	  #2 (parent #1) [Persian] refs=BQT:967 | ravân «روان٢» : spirit | extra: روانکاو ، روانپزشک
22	#3 (parent #0) [Sogdian] refs=SOD:59 | `rw`n : spirit | NOTE: This may be a cognate rather than a derivative of Avestan "urvan".
23	
```


## [2026-10-16T05:13:08.510Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-521.json"
}
```


### [2026-10-16T05:13:08.538Z] TOOL RESULT

```
1	{
2	  "pdf_page": 521,
3	  "book_page": 491,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Urmak",
8	        "lang": "Mongolian",
9	        "refs": "KLN:742",
10	        "gloss": "to strike"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Mongolian",
17	          "refs": "KLN:742",
18	          "words": [
19	            {
20	              "translit": "Urdu",
21	              "gloss": "camp of strikers, army camp",
22	              "script": null
23	            }
24	          ],
25	          "note": null,
26	          "quote": null
27	        },
28	        {
29	          "id": 2,
30	          "parent": 0,
31	          "lang": "Turkish",
32	          "refs": "KLN:742,1861",
33	          "words": [
34	            {
35	              "translit": "ordu",
36	              "gloss": "camp",
37	              "script": null
38	            }
39	          ],
40	          "note": null,
41	          "quote": null
42	        },
43	        {
44	          "id": 3,
45	          "parent": 2,
46	          "lang": "Persian",
47	          "refs": "KLN:1861; MON:197; NAT:14",
48	          "words": [
49	            {
50	              "translit": "ordŭ",
51	              "gloss": "camp, army, also a \"camp language\" that was originally spoken by an Indian army of Hindi, Persian, Turkish and Arab soldiers.",
52	              "script": "اردو"
53	            }
54	          ],
55	          "script_extra": "اردوگاه ، اردوکشی ، اردوبیگ",
56	          "note": null,
57	          "quote": null
58	        },
59	        {
60	          "id": 4,
61	          "parent": 3,
62	          "lang": "Hindustani",
63	          "refs": "KLN:1681",
64	          "words": [
65	            {
66	              "translit": "urdu",
67	              "gloss": "Hindustani language",
68	              "script": null
69	            }
70	          ],
71	          "note": null,
72	          "quote": null
73	        },
74	        {
75	          "id": 5,
76	          "parent": 4,
77	          "lang": "English",
78	          "refs": "KLN:1681",
79	          "words": [
80	            {
81	              "translit": "Urdu",
82	              "gloss": "an Indian language",
83	              "script": null
84	            }
85	          ],
86	          "note": null,
87	          "quote": null
88	        },
89	        {
90	          "id": 6,
91	          "parent": 0,
92	          "lang": "French",
93	          "refs": "KLN:742; AHD",
94	          "words": [],
95	          "note": null,
96	          "quote": null
97	        },
98	        {
99	          "id": 7,
100	          "parent": 6,
101	          "lang": "English",
102	          "refs": "AHD:634; KLN",
103	          "words": [
104	            {
105	              "translit": "hoard",
106	              "gloss": "a wandering tribe, group, camp",
107	              "script": null
108	            }
109	          ],
110	          "note": null,
111	          "quote": null
112	        }
113	      ]
114	    },
115	    {
116	      "root": {
117	        "name": "Uroiks, Loik",
118	        "lang": "Indo-European",
119	        "refs": "IEC:704,1593",
120	        "gloss": "twist, twine, wicker, beard"
121	      },
122	      "nodes": [
123	        {
124	          "id": 1,
125	          "parent": 0,
126	          "lang": "Avestan",
127	          "refs": "HRN:142; IEC:104,1593",
128	          "words": [
129	            {
130	              "translit": "raeša",
131	              "gloss": "hair, beard",
132	              "script": null
133	            }
134	          ],
135	          "note": null,
136	          "quote": null
137	        },
138	        {
139	          "id": 2,
140	          "parent": 1,
141	          "lang": "Pahlavi",
142	          "refs": "BQT:988; SOD:348",
143	          "words": [
144	            {
145	              "translit": "rěš",
146	              "gloss": "beard",
147	              "script": null
148	            },
149	            {
150	              "translit": "rěšak",
151	              "gloss": "(hairy) root",
152	              "script": null
153	            }
154	          ],
155	          "note": null,
156	          "quote": null
157	        },
158	        {
159	          "id": 3,
160	          "parent": 2,
161	          "lang": "Persian",
162	          "refs": "BQT:988,989; HRN:142; IEC:704,1593",
163	          "words": [
164	            {
165	              "translit": "rîš 2",
166	              "gloss": "beard",
167	              "script": "ریش٢"
168	            },
169	            {
170	              "translit": "rîšeh",
171	              "gloss": "root",
172	              "script": "ریشه"
173	            }
174	          ],
175	          "note": null,
176	          "quote": null
177	        },
178	        {
179	          "id": 4,
180	          "parent": 1,
181	          "lang": "Sogdian",
182	          "refs": "SOD:348",
183	          "words": [
184	            {
185	              "translit": "ryš`kk",
186	              "gloss": "beard",
187	              "script": null
188	            }
189	          ],
190	          "note": null,
191	          "quote": null
192	        },
193	        {
194	          "id": 5,
195	          "parent": 0,
196	          "lang": "Latin",
197	          "refs": "IEC:704",
198	          "words": [
199	            {
200	              "translit": "lîcium",
201	              "gloss": "woof, yarn",
202	              "script": null
203	            }
204	          ],
205	          "note": null,
206	          "quote": null
207	        }
208	      ]
209	    },
210	    {
211	      "root": {
212	        "name": "Urvan",
213	        "lang": "Avestan",
214	        "refs": "SYN:1088; BQT:967",
215	        "gloss": "spirit, soul"
216	      },
217	      "nodes": [
218	        {
219	          "id": 1,
220	          "parent": 0,
221	          "lang": "Pahlavi",
222	          "refs": "BQT:967",
223	          "words": [
224	            {
225	              "translit": "ruvân",
226	              "gloss": "spirit",
227	              "script": null
228	            }
229	          ],
230	          "note": null,
231	          "quote": null
232	        },
233	        {
234	          "id": 2,
235	          "parent": 1,
236	          "lang": "Persian",
237	          "refs": "BQT:967",
238	          "words": [
239	            {
240	              "translit": "ravân",
241	              "gloss": "spirit",
242	              "script": "روان٢"
243	            }
244	          ],
245	          "script_extra": "روانکاو ، روانپزشک",
246	          "note": null,
247	          "quote": {
248	            "text": "همان جویبار است و آب روان ١ - که از دیدنش تازه گردد روان ٢",
249	            "poet": "Ferdowsî"
250	          }
251	        },
252	        {
253	          "id": 3,
254	          "parent": 0,
255	          "lang": "Sogdian",
256	          "refs": "SOD:59",
257	          "words": [
258	            {
259	              "translit": "`rw`n",
260	              "gloss": "spirit",
261	              "script": null
262	            }
263	          ],
264	          "note": "This may be a cognate rather than a derivative of Avestan \"urvan\".",
265	          "quote": null
266	        }
267	      ]
268	    }
269	  ]
270	}
```


## [2026-10-16T05:13:15.500Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; ls sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['KLN','MON','NAT','AHD','IEC','HRN','BQT','SOD','SYN','POK','WLD','PHD','NYB','BRT','HUB','ARY','TTS','LKT','SKT','HJB','CHEUNG','WEB','FSD']:\n  v=d.get(k);print(k, v and {x:v.get(x) for x in ['local_file','page_offset','lookup_hint','scans']})\n\""
}
```


### [2026-10-16T05:13:15.969Z] TOOL RESULT

```
<persisted-output>
Output too large (31.8KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/b1o00klwt.txt

Preview (first 2KB):
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
...
</persisted-output>
```


## [2026-10-16T05:13:18.706Z] TOOL CALL #5: Bash

```json
{
 "command": "cat /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/b1o00klwt.txt | grep -v '^  `' | head -150; cat /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/memory/checkout-setup.md"
}
```


### [2026-10-16T05:13:19.193Z] TOOL RESULT

```
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
- **CHEUNG** — CHEUNG
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
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
KLN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", 'scans': None}
MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", 'scans': None}
NAT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NAT_2005.txt', 'page_offset': '2005 reprint: leaf = printed + 15 (e.g. leaf 17 = p.2); reprint pagination may differ slightly from 1982. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': 'Popular book, prose chapters; grep the word.', 'scans': None}
AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).", 'scans': None}
IEC {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", 'scans': None}
HRN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", 'scans': None}
BQT {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", 'scans': [{'volume': '3', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]}
SOD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'], 'page_offset': 'printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)', 'lookup_hint': "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", 'scans': None}
SYN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.", 'scans': None}
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", 'scans': None}
WLD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.", 'scans': None}
PHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).", 'scans': None}
NYB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", 'scans': None}
BRT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.", 'scans': None}
HUB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", 'scans': None}
ARY {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", 'scans': [{'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt'}]}
TTS {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt'], 'page_offset': 'TTS_pages.txt: 253 leaves; printed page N = leaf N+30.', 'lookup_hint': "Not searched exhaustively (3 citations); the 1878 original is public domain - try IA query 'vambery etymologisches wörterbuch turko-tatarischen' or Google Books.", 'scans': None}
LKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt', 'page_offset': 'leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", 'scans': None}
SKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", 'scans': None}
---
name: checkout-setup
description: "How the rishe-private checkout was wired up on 2026-10-14 (remotes, worktree, ref library, hook)"
metadata:
  node_type: memory
  type: project
  originSessionId: 7c41a241-7571-4c3b-8e91-929d2c62eed6
  modified: 2026-10-15T02:20:15.267Z
---

The repo now lives at /home/sfmqrb/git/rishe-private (it used to be /home/sfmqrb/git/rishe). On 2026-10-14 it was set up to match COORDINATOR.md:
- `origin` = public sfmqrb/rishe, `private` = sfmqrb/rishe-private. Working branch is `verified`.
- `../rishe-backup` is a worktree on `verified-with-sources`. The reference library (`sources/refs/`) was rsynced from there into the main tree, where it is gitignored.
- `.git/hooks/pre-push` blocks pushes of `sources/refs/` to any remote except `private`. The hook is not versioned.
- Subagent transcripts are at `~/.claude-work/projects/-home-sfmqrb-git-rishe-private/<session>/subagents/`.
- Known gaps: `refs/tessdata` (Persian OCR traineddata; the system only has eng), the `incoming/*_faseng.txt` files and the Bailey PDF were never in the backup.

**Why:** the docs and scripts assumed the old path and remote layout.
**How to apply:** if the checkout is re-cloned, redo these steps before launching verification agents.
```


## [2026-10-16T05:13:22.527Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls data/verification/ | tail -5; python3 -c \"\nimport json;d=json.load(open('data/verification/page-511.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in d.items() if k!='entries'}));n=e['nodes'][0];print(json.dumps(n,ensure_ascii=False,indent=1)[:3000])\"; grep -n 'PROBLEM' tools/verify_check.py | head -40"
}
```


### [2026-10-16T05:13:23.077Z] TOOL RESULT

```
.rw-r--r--   40k sfmqrb 14 Oct 22:50  page-514.json
.rw-r--r--   22k sfmqrb 14 Oct 22:47  page-515.json
.rw-r--r--   36k sfmqrb 14 Oct 22:51  page-516.json
.rw-r--r--   32k sfmqrb 14 Oct 22:48  page-517.json
.rw-r--r--   20k sfmqrb 14 Oct 22:48  page-518.json
{"pdf_page": 511, "book_page": 481, "verified_by": "claude-opus-5", "verified_on": "2026-10-14"}
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "",
 "verdict": "disputed",
 "derivation": "Empty pass-through box: Nourai (following Pourdavoud via Mo'in's Borhan footnote) routes the Tamil word through Sanskrit before it reaches Aramaic and Arabic. No Sanskrit form of the tōkai/ṭāwūs type is attested: the Sanskrit words for 'peacock' are mayūra-, śikhin-, barhin-, kalāpin-. Modern scholarship (Wiktionary s.v. ταώς, Klein s.v. peacock) derives the Mediterranean/Semitic words either from Pre-Greek ταώς or directly from a Dravidian (Tamil tōkai) or other eastern source by sea trade, with no Sanskrit intermediary.",
 "derivation_fa": "این خانهٔ خالی «سنسکریت» را نورایی به پیروی از پورداوود (در حاشیهٔ معین بر برهان قاطع) میان تامیلی و آرامی/عربی گذاشته است. اما در سنسکریت واژه‌ای از گونهٔ tōkai یا ṭāwūs برای طاووس دیده نمی‌شود؛ نام‌های سنسکریت طاووس mayūra، śikhin و barhin است. پژوهش امروزی (کلاین، ویکی‌واژه) واژهٔ یونانی ταώς را پیش‌یونانی می‌داند یا آن را مستقیم به منبعی شرقی مانند تامیلی tōkai می‌رساند، و گذر از سنسکریت را تأیید نمی‌کند.",
 "sources": [
  "https://en.wiktionary.org/wiki/ταώς",
  "https://en.wiktionary.org/wiki/தோகை"
 ],
 "ref_check": [
  {
   "ref": "BQT:1346",
   "status": "partial",
   "note": "Borhan-e Qate' p.1346 (BQT_v3_picofile.pdf page 139; the tool's default offset lands on pdf 141, use --pdf-page 139; transcription saved in ocr/BQT/1346.vision.txt), Mo'in's footnote s.v. طاوس: '(عر) معرب آن طویس، یونانی Taôs، آرامی طاوسا tausâ «تسیمرن. لغات دخیل اکدی ص۵۲» طبق تحقیق استاد پور داود اصل کلمه از زبان دراویدی وارد سانسکریت شده و از آنجا بزبانهای دیگر رفته'. Source of Nourai's Dravidian > Sanskrit > Arabic/Aramaic chart (after Pourdavoud); Mo'in himself lists the Greek and Aramaic forms side by side without making Greek a daughter of Persian."
  }
 ],
 "consulted": [
  {
   "src": "KLN",
   "where": "1966 s.v. peacock (KLN_1966.txt line 27770)",
   "stance": "partial",
   "note": "'L. pavo ... which, together with Gk. ταώς, prob. comes ult. fr. Tamil tokei, tōgei (whence also Heb. tukkiyyim) ... initial p- in L. pavo is due to imitative influence; cp. L. paupulo, 'the natural sound of the peacock''."
  },
  {
   "src": "SKT",
   "where": "s.v. Peacock (SKT_dli_revised.txt line 55507)",
   "stance": "contradicts",
   "note": "Skeat's chain is 'Pers. tāwus ... - Tamil tōkei' with no Sanskrit stage."
  },
  {
   "src": "MON",
   "where": "vol.2 s.v. طاوس (MON_part1.txt line 91933)",
   "stance": "partial",
   "note": "Only the tag '[دراویدی هندی]' - Dravidian/Indian, no Sanskrit form given."
  }
 ]
}
90:        print("PROBLEM:", p)
```


## [2026-10-16T05:13:24.732Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,95p tools/verify_check.py"
}
```


### [2026-10-16T05:13:25.179Z] TOOL RESULT

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
```


## [2026-10-16T05:13:33.362Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^horde|^Urdu' KLN_1966.txt | head; grep -n -i -E '^(horde|urdu|ordu)' SKT_dli_revised.txt SKT.txt | head; grep -n -i 'ordu' LKT.txt | head; grep -n -i -E 'ordu|urdu' HJB.txt | head -20"
}
```


### [2026-10-16T05:13:33.853Z] TOOL RESULT

```
18067:horde,  n.,  1)  a  wandering  tribe;  2)  a  multitude.  — F„  fr.  Turk,  ordit,  ‘camp,  army’,  fr.  Tatar  urdu, ‘camp’  (lit.  ‘something  pitched  up’),  fr.  urmak, ‘to  strike’.  Cp.  Urdu.
18070:Hordeum,  n.,  a  genus  of  grasses,  the  barley  (bot.)
40860:Urdu,  n.,  Hindustani.  —  Hind,  urdii,  fr.  Pers.  Ur¬ du,  ‘camp’,  which  is  cogn.  with  Turk,  ordu, ‘horde’  (see  horde) ;  used  in  the  sense  of  zaban- i-urdu,  ‘(language  of)  the  camp".
SKT_dli_revised.txt:8892:hordeure (Span, bordaaurd), an edging. — 
SKT_dli_revised.txt:37247:horde, Icel. hur6, G. hurde, M. H. G. 
SKT_dli_revised.txt:68559:ordure. +A. S. scearn, dung. 
SKT_dli_revised.txt:94926:horde. 
2023:dazu  demin.  Husain  ebenfalls  als  häu- figer Name  gebraucht.  Jä  Hasan  jä Husain  'o  Hasan,  o  Husain!'  ist  der Klageruf  der  Schiiten  ata  10.  Muharram zum  Andenken  an  die  Ermordung  der beiden  Söhne  'Alis.  Diese  Wehklage ist  angloind.  zu  hobson-jobson  verball- hornt worden  und  ein  für  das  Anglo- indische  geradezu  typischer  Ausdruck geworden;  daher  gaben  YüLE  und BURNELL  ihrem  Glossary  of  Anglo- Indian  Colloquial  Words  den Namen  HOBSON-JOBSON.  Übrigens nennt  Chamb  AllJap  43,  Anm.  1)  dieses Werk  mit  Recht  ,das  entzückendste aller  Wörterbücher",  und  auch  ENNO LITTMANN  nennt  es  in  MWiD  IX  ,das eigenartige  englische  Werk  H.-J."  [Hob- son-Jobson  419/420.
3654:1594.  Tk.  ordu:
170:It  is  curious  to  note  that  several  of  our  most  common  adoptions  are  due  to what  may  be  most  especially  called  the  Oordoo  (Urdu)  or  *Camp'  language, being  terms  which  the  hosts  of  Chinghiz  brought  from  the  steppes  of  North Eastern  Asia — e.g.  "The  old  Bukshee  is  an  awful  haliadur,  but  he  keeps  a first-rate  bdbachee"  That  is  a  sentence  which  might  easily  have  passed without  remark  at  an  Anglo-Indian  mess-table  thirty  years  ago — perhaps might  be  heard  still.  Each  of  the  outlandish  terms  embraced  in  it  came  from the  depths  of  Mongolia  in  the  thirteenth  century.  Chick  (in  the  sense  of  a cane-bUnd),  daroga,  oordoo  itself,  are  other  examples.
1130:[Platte,  J.  T.  A  Dictionary  of  Urdu,  Classi- cal Hindi,  and  English.    London,  1884.]
1228:Sanang  Sotion.  Oeschichto  dor  Ost-Mon- goien  .  .  .  von  Ssanang  Ssetzen  Chung- taidschi  der  Ordus.  aus  dem  Mongol .  .  . ▼on  Isaac  Jacob  Schmidt.  4to.  St. Petersburg,  1829.
4044:BBANDTPAWK^EE,  s.  Brandy and  water ;  a  specimen  of  genuine Urdu,  i.e.  Gamp  jargon,  which  hardly needs  interpretation.  H.  panl,  *  water.' Williamson  (1810)  has  hrandy-tkravh- l»i*ny(r.Af.  ii.  123).
6627:1615. — P&rson  Terry  well  describes  the thing,  but  names  it  not :  "  The  ordinary  sort of  people  eat  bread  made  of  a  coarse  grain, but  both  toothsome  and  wholesome  and hearty.  They  make  it  up  in  broad  cakes, thick  like  our  oaten  cakes ;  and  then  bake  it upon  small  round  iron  hearths  which  they carry  with  them." — In  Furduu,  ii.  1468.
7853:1590.— "One  Crocodile  was  so  huge  and l^reedy  that  he  devoured  an  Alibamiia,  that IS  a  chained  company  of  eight  or  nine  slaves ; but  the  indigestible  Iron  paid  him  his  wages, and  raurthered  the  murtherer." — Anarew BaUel  (West  Africa),  in  Purduu,  ii.  965.
9375:c.  1616.— "The  20th  day  (August),  the ni^ht  past  fell  a  storme  of  rame  oalled  the Ouphant,  Tsnall  at  going  out  of  the  raines." —Sir  r.  /2oe,  in  Purduu,  i.  549 ;  [Hak.  Soo. i.247].  .
11118:HIND08TA1IEE,  a.  HindOttdnl, properly  an  adjective,  but  used  sub- stantivdv  in  two  senses,  viz.  (a)  a native  of  Hindustan,  and  (b)  (Hindu- stdni  zabdn)  Hhe  language  of  that counti^,'  but  in  fact  the  langu^  of the  liukhommedans  of  Upper  India, and  eventually  of  the  Manommedans of  the  Deccan,  developed  out  of  the Hindi  dialect  of  the  Doab  chieflv,  and of  tlie  territory,  round  Agra  and  Delhi, with  a  mixture  of  Persian  vocables and  phrases,  and  a  readiness  to  adopt other  foreign  words.  It  is  also  called Oordoo,  i.e.  the  language  of  the  Urdu (*  Horde  *)  or  Camp.  This  lanmiage was  for  a  long  time  a  kind  of  Manom- medan  lingua  franca  over  all  India, and  still  possesses  that  character  over a  lar^  part  of  the  country,  and  among certain  classes.  Even  in  Madras, where  it  least  prevails,  it  is  still  re- cognised in  native  re^ments  as  the language  of  intercourse  between  officers ana  men.  Old-fashioned  Anglo-Indians used  to  call  it  the  Moors  (q.v.).
12997:c.  1560.— "These  Laos  came  to  Camboia, downe  a  River  many  dales  loumie,  which they  say  to  have  his  beginning  in  China  as many  others  which  ninne  into  the  Sea  of India ;  it  hath  eight,  fifteeno,  and  twentie f athome  water,  as  myselfe  saw  by  experience in  a  great  part  of  it;  it  paaseth  through manie  vnknowne  and  desart  Countries  of great  Woods  and  Forests  where  there  are innumerable  Elephants,  and  many  Buffes .  .  .  and  certayne  beastes  which  in  that Ck>untrie  they  call  Badat  (see  ABABA)."— Oatpar  da  CrvZt  in  PurduUy  iii.  169.
13474:1585.— "They  came  to  Amaeao,  in  July, 1585.  At  the  same  time  it  seasonably hapned  that  Linsilan,  was  commanded  from the  ooort  to  procure  of  the  Strangers  at /^TwanftAj^  certaine  goodly  feathers  for  the King."  —  From  the  Jesuit  Aceourds,  in J*urduu^  iii.  330.
13747:1602.—*'  We  came  to  anchor  in  the  Roade of  Achen  .  .  .  where  we  found  sixteene  or eighteene  saile  of  ahippes  of  diuera  Nations, some  OosercUty  some  of  Bengala,  some  of GaleciU,  called  Malabares,  some  Pegws, and  some  Paianyes." — Sir  J.  Lancaster ^  in Purduu,  i.  153.
14612:MOONSHEE.  8.  At.  munM,  but written  in  Hina.  munshi.  The  verb inshOj  of  which  the  Ar.  word  is  the participle,  means  *  to  educate '  a  youth, as  well  as  *  to  compose  *  a  written  docu- ment. Hence  *a  secretary,  a  reader, an  interpreter,  a  writer.*  It  is  com- monly applied  by  Europeans  specifi- cally to  a  native  teacher  of  languages, especially  of  Arabic,  Persian,  and  Urdu, though  the  application  to  a  native amanuensis  in  those  tongues,  and  to any  respectable,  well-educated  native gentleman  is  also  common.  The  word probably  became  tolerably  famiHar  in Europe  through  a  book  of  instruction in  Persian  bearing  the  name  (viz.  **  Th€ Persian  Moonshee,  htf  F,  Gladioyn"  Ist ed.  s.a.,  but  pubbshed  in  Calcutta about  1790-1800).
14688:MOOBS,  TBS,  s.  The  Hindustani language  was  in  the  18  th  century commonly  thus  styled.  The  idiom is  a  curious  old  English  one  for  the denomination  of  a  language,  of  which *  broad  Scots'  is  perhap  a  type,  and which  we  find  exemplified  in  *Mala- bars'  (see  MALABAB)  for  Tamil, whilst  we  have  also  met  with  Bengals for  Bengali,  with  Indostans  for  Urdu, and  with  Turks  for  Turkish.  The term  Moors  is  probably  now  entirely obsolete,  but  down  to  1830,  at  least, some  old  officers  of  the  Royal  army and  some  old  Madras  civilians  woiild occasionally  use  the  term  as  synony- mous with  what  the  former  would  also call  *  the  black  language.'  [Moors  for Urdu  was  certainly  in  use  among  the old  European  pensioners  at  Chunar  as late  as  1892.]
15662:1626.— "After  death  they  (the  Talapoys) beleeye  three  Places,  one  of  Pleasure  Scuuih (perhaps  sukham)  fike  the  Mahumitane  Para- dise ;  another  of  Torment  Naxac  (read  Na- roc);  the  third  of  Annihilation  which  they call  mhtL."—PurdUu,  Pilffrimage,  606.
15929:OOBDOO,  s.  The  Hindustani language.  The  (Turki)  word  urdu means  properly  the  camp  of  a  Tartar Khan,  ana  is,  in  another  direction, the  original  of  our  word  horde  (Russian orda),  [which,  according  to  Schuyler (Turki^n,  i.  30,  note),  "is  now  com- monly used  by  the  Bussian  soldiers and  Cossacks  in  a  very  amusing manner  as  a  contemptuous  term  for  an Asiatic  "1  The  *  Golden  Horde '  upon the  Volga  was  not  jjroperly  (pace Littre)  the  name  of  a  tribe  of  Tartars, as  is  often  supposed,  but  was  the  style of  the  Royal  Camp,  eventually  Palace, of  the  Khans  of  the  House  of  Batu  at
15933:Sarai.  Horde  is  said  by  Pihan,  quoted by  Dozy  {OotterU  43")  to  have  been introduced  into  Frencn  by  Voltaire  in his  Orphelin  de  la  Chine,  But  Littr^ quotes  it  as  used  in  the  16th  century. urda  is  now  used  in  Turkistan,  e,g, at  Tashkend,  Khokhand,  &c.,  for  a *  citadel'  (Schuyler,  loc.  dt.  i.  30).  The word  urau,  in  the  sense  of  a  royal camp,  came  into  India  probably  with Baber,  and  the  royal  residence  at  Delhi was  styled  urdu-i-mu'cUld,  *the  Sublime Camp.*  The  mixt  language  which  grew up  in  the  court  and  camp  was  called zabdn-i-urdUf  *the  Camp  Language,' and  hence  we  have  elliptically  Urdu. On  the  Peshawar  frontier  the  word nrdu  is  still  in  frequent  use  as  applied to  the  camp  of  a  field-force.
15942:[1763.-"  That  part  of  the  camp  called  in Turkish  the  Ordubaiar  or  camp-market^ begins  at  the  end  of  the  square  fronting  the guard-rooms.  .  .  ."— iTaiiway,  Hitt.  Account, I  247.]
18900:1610.— "This  armie  consisted  of  100,000 horse  at  the  least,  with  infinite  number  of Camels  and  Elephants:  so  that  with  the whole  baggage  there  could  not  bee  lesse than  fiue  or  sixe  hundred  thousand  persons, insomuch  that  the  waters  were  not  suf- ficient for  them ;  a  MoBSOCke  (see  MX78- SnCK)  of  water  being  sold  for  a  Rupia, and  yet  not  enough  to  be  had"— ffawkiru^ in  Purduut  i.  427.
19467:Prior  to  1419.  — "Et  debent  ad  dictum Wardemotum  per  Aldermannum  et  probos Wardae,  necnon  per  juratores,  eligi  Con- -stabnlarii,  Scayegeonn,  Aleconners,  Be- delle,  et  alii  Officiarii."— Zi6«r  AUnu,  p.  38. „  ''Sbrbmbnt  db  Soawageonn. Vona  jurrez  qe  vous  surverrez  diligientie- ment  qe  lez  pavimentz  danz  vostre  Garde «oient  bien  et  droiturelement  reparaillez  et nyent  enhanasez  a  nosance  dez  veysyns  ;  et <\Q  lez  chemyna,  ruwes,  et  yenelles  soient nettez  dez  nens  et  de  toutz  roaners  dez ordures,  pur  honestee  de  la  citee ;  et  qe tonts  les  chymyneys,  foumes,  terrailles soient  de  piere,  et  suffiaantement  defens- ■ables  encontre  peril  de  few ;  et  si  vous troYez  rien  a  oontraire  yous  monstrez  al Alderman,  issint  qe  I'Alderman  ordeigne pur  amendement  de  celle.  Et  ces  ne lerree— si  Dieu  vous  eyde  et  lez  Saintz."— Ihid.  p.  818.
21451:1611.— "That  wood  which  we  out  for -firewood  did  all  han^  trased  with  cods  of greene  fruit  (as  big  as  a  Bean-cod  in England)  called  Tamerim ;  it  hath  a  very score  tast,  and  by  the  Apothecaries  is  held good  against  the  Scurvie. ' — N,  Dountoriy  in FurduUf  i.  277.
```


## [2026-10-16T05:13:53.332Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'roik|wroik|u̯roik|uroik' IEC.txt | head -20; grep -n -i -E 'rēš|rēsh|rês|rīš|rîš' HRN.txt | head -20; grep -n -i -E 'lemma: .*reik|lemma: .*u̯reik|licium' POK_full.txt | head"
}
```


### [2026-10-16T05:13:53.677Z] TOOL RESULT

```
13493:proikos (prik-) “facing, front, opposite, op- posing, opponent. Cf. WP II, 89 Lat. cf. (?) a-pricus (for *ad-proik- “facing the sun” Fest. Cf. praecia, pl. “heralds of a holi- day”; Br. cf. raok, a-raok, s. “face, front; ON freegr, adj. ‘famous’; OCS prékü, adj. “obli- que’; préky ‘against’; Slovak priek, m. 'de- Dance: crossing’; priekom ‘crosswise’; Cz. pfik, m. “opposition; wrong; slope’; Li. priekis, gs. -jo, m. ‘front’; Latv. cf. priekš, prp. 'be- fore’; prieks, m. “joy”. (The R forms po-perék, adv. “across”, Ukr. v-po-perek, id. and perecy- tysja, with anaptyxis, derive from a form of type perquo, q.v., but the Sl. forms above are ambig.). See next
13494:proiKos, variant of proikos above. Arm. Lat. ambig. Cf. preK-, prekt- Lat. (Fest) cf. praecia ‘heralds declaring a holiday”; praeco, gs. -onis m. (“herald”, if not a synthetic cpd.); Br. (ambig.) raok, s. “face, front'; Arm. eres & eresk 'face, appearance' beside eresem, v. ‘appear’; MIr. cf. airec, s. “shield” beside airechas, m. (sovranty', if fr. *prikost-); Cz. cf. přes, prp. (2) “despite”; Li. prieš, prp. “against'; priešas, m. ‘opponent; priešůs, adj. fopposing?
14698:roikseio ‘loosen, free; clarify; decide. (Balto-Slav only?) OCS ré&o, rěšiti, v. 'undo'; Cz. řešit, inf. *de- cide’; Li. raisküs, adj. “clear, explicit’; raiška, f. fexpression'; cf. (e-gde) reiSkiu, reikšti *ex- plain, express, declare, publish’; reiSküs, adj. (var. of raiSküs)
14706:roikseió — romb- (rombos, à)
15843:skrau- — skreikos (skroik-)
15858:skreikos (skroik-) “cry, shriek, scream' Ir. scr��achaim, v. id.; scréach, pl. a f. id.; MHG schri, beside schrei, sm. id.; schrien, sv., beside schreien, tr. ‘shriek; make scream’;
18883:(treik- ‘force, crush’. Cf. trenk- and trik-. Ambig. in Li. tréikiu, -ti ‘rage’ Go. breihan, v. ‘press, squeeze’; Latv. triecu, triekt, v. ‘batter, crush’. For Go. faíhu-praibns *riches' see trika-. Latv. ambig. cf. troik-)
18960:trik- (or treik-) «twist, tangle, whirligig, gad- ged, plot'. (Vowel ambig.) Lat. tricae, fpl. ‘gadgets’; cf. in-tricare, inf. *entangle'; LLat. cf. also expressive variant *tricca, *triccare in Fr. tricher ‘to trick; MHG drihe, wf. “plot, intricacy’; Srb. trice. f. ‘gad- get, toy? (LW?); Li. cf. trinkü, trikti, v. “err, be confused’. (Isophones: Go. preihan, v. ‘press’; Latv. trice, f. ‘tremor’; triece, f. *pile- driver?) (*-1- : -ei-). See troikó
18973:triped-, tripüd- — troiko, eio
18986:troikō, eið ‘oppress, squeeze, strain’. Cf. treik-, trīk-. Ir. traochaim, v. ‘drain; weary’; OS thrēgian, Du. dreigen, v. ‘threaten, menace’; Li. cf. traiškau, yti, v. ‘cramp, strangle, squeeze,
20036:(uereiKa ‘heather’, see uroiK-)
48306:Root / lemma: krei-2, kreig-, kreik- 
69919:Root / lemma: reik- 
93355:Root / lemma: ureik-, uereik- {*hauerk^
```


## [2026-10-16T05:13:56.332Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^uroi|uroiK|uroik' IEC.txt | head; sed -n 93355,93400p POK_full.txt; grep -n -E 'lemma: (u̯lei|ulei|lei-?k|leik)' POK_full.txt|head"
}
```


### [2026-10-16T05:13:56.920Z] TOOL RESULT

```
20036:(uereiKa ‘heather’, see uroiK-)
Root / lemma: ureik-, uereik- {*hauerk^ 

Meaning: " heath, heather, any of a number of low evergreen shrubs bearing clusters of 

purple flowers ' 

See also: see above S. 1 155 under uergh-. 

Page(s):1182 

Root / lemma: urek- {*hauei1(-) 

Meaning: ' talk, shout ' 

References: WP. I 318, II 343, 362, Trautmann 243, Vasmer 2, 508 f. 

See also: s. ober under uer-6. 

Page(s):1182 

Root / lemma: uren- {*hauer-en-) 

Meaning: to sprinkle 

Material: Gr. paivoj {*urnjd) 'bespritze, besprenge (with water or dust, powder)', pavit;, - 

'\boc,i. "drip"; with -d^- extension paGapiy^f. "drip, Staubkornchen' {*urn-6'^-), paGaivw 

"besprenge, streue from'; secondary -5- in sppaSarai, sppaSaro, paaaaTS Perf. Pass, and 

Aor. to paivu); paivw could indeed also to Old Church Slavic izroniti {above S. 329) belong; 

about Old Saxon Old High German wrennio, (under the influence of common Celtic -ns-, 
-nt- > -nn-). Old Saxon wrenio. Old High German reineo, Ae/zX/?)*? "stallion' (to Old English 
wraene. Old Saxon ty/'(9/7/sc "horny, lustful', Norwegian vrTna^cry, neigh ') see above S. 81 
and under i/e/-- J respectively urei-\ 

after Szemerenyi (KZ. 73, 74) here Hittite hurna'h "sprinkle' {*urn-), further perhaps to 
Indo Germanic auer- above S. 80 f. 

References: WP. I 277, 320, Specht Indo Germanic Dekl. 156. 
Page(s):1182 

Root/ lemma: iureth-.) uroth-ox urath-{*hauerth-) 
Meaning: to support
```


## [2026-10-16T05:14:00.512Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'licium|rae[sš]a|raesa|\\briš\\b|rēš|resh' IEC.txt | head -20; grep -n -E '^(u?roiK|uroiK|uroik|loik)' IEC.txt"
}
```


### [2026-10-16T05:14:00.839Z] TOOL RESULT

```
961:bloskos “bang, dash, etc? Cf. blosko. Cf. WP II, 218 Mir blosc; E plash; Li. bláskas ‘threshing of corn'
1174:bhaus- “violent, dashing, boisterous; bang, beat, din’ Arm. cf. (variant) z-bawsank ‘amusement’, z-bawsnum (‘amuse os, fr. *bhauK-); Fris. boas "lively, eager; (of weather) bad: OHG bosi ‘paltry, bad'; bosa ‘badness’; Du. boos “angry, malignant, evil’; Nynorsk (archaic Nor- wegian) baus ‘stalwart’; Cz. cf. vý-buch, Ukr. vy-bux ‘explosion’. Verbal types include: Arm. (variant) z-bawsnum ‘amuse oneself; MHG besen ‘do evil; Cz. bušiti ‘hammer’; Big. bùša ‘punch’ beside bùxam ‘flog’. Cf. also ON beysta ‘thresh’; Big. buxtjà ‘dash, roar’
1408:bhlóros ‘flushed, pale, dim? Alb. blerë ‘green’; OLat. florus ‘flourishing, fresh; Gael. blár ^white-blazed'; W blawr ‘grey, hoary’; ME bere EME blear 'dim- sighted, clouded’; Icel: blórar, fpi. ‘secrets’, blóra ‘secretly’ :
1622:Alb. breshté, i — ‘wild, savage; MHG brésten ‘break, burst’; ON bresta, id.; Sw. brista, id. (MHG, ON & Sw. also lack); Olr. bress “din”; Slovene cf. brecati “din, clatter'. Variant (*bhre$t-) in OE breahtm ‘din’
2471:dromos ‘course, way’. WP I, 796 Skt. cf. dram- ‘to run’; Gk. drómos; LG tram ‘rung of ladder’; OE. trem ‘footstep’; Norw. tram ‘threshold’
2593:dupso, ið ‘trample, beat, thresh’ Arm. tpem “beat; scutch'; Sw. tofsa, tufsa ‘lug, touse’; OCz. & Cz. depsati ‘tread, trample, plod’; OCz. cf. also deptati, Isg depcu: Pol. deptać, id.
2654:duinos, à (2) (duisnos?) ‘turn, spin’. Cf. WP I, 820 Gk. dinos, dinë *'eddy; giddiness; lathe; threshing-floor'; cf. kor-dinéma *head-spin- ning; vertigo’; én-dina (pl. *entrails"); dinéo, v. “spin” (but Aeolic dinna ‘eddy’ suggests a type *duisnà, q. v.); OE twin ‘twine’; Du. twijn, id.; Sw. cf. tvinna 'twine, spin'; Nor. tvinne, id. cf. tvist ( yarn, twist’, fr. *duistós). See duisnos
2784:dhémn- “setting, fixture, form, shape, sub- stance’. WP I, 828. Cf. dheio (2) *dhemen-, *dhemn- in Gk. thé- ma, cf. also thémis: Myc. temi- “Justice? and Hes. thémeros “firm, stationary'; Lat. femen, gs -inis & femur, gs femoris & feminoris (*thigh': Cz. dymé, gs demene ‘groin’, beside Lat. femin-àlia *drawers"); Ir. damhna 'substan- ce; cause’; W defn ‘substance, material’ beside defnydd, pl. iau (elemen? fr. *dhemniio-); MHG tinne (‘forehead’; pl. ‘temples’); Swiss Tenn ‘main room in hut’; G Tenne ‘threshing- floor’; *dhemn-, *dhēmō(n) in Skt. dhàman ‘fixed abode, reaim, place, common-law, rule, pleasure’; Av. dama, obl. daman- ‘creature’; Gk. théma ‘tomb’, themón ‘heap’; Li. démé “mark, note’; demuó, eps “item, theme, com- ponent, datum’. Cf. further dhomn-. (Av. dax- məm ‘repository for bones’ seems to represent a type *dhesmom. Cf. dhesno-. For Ir. deimh- in ‘certainty’ see above: dhémen-)
3449:edhros (odhros) ‘construction, end-beam, crutch, gable-end'. WP I, 121 Arm. erd, o-st. ‘roof, house’; erdik, pl. form ‘dormer window’; Lat. cf. cer-ebrum, lit. "bead structure: OHG &tar, MHG éter; MLG éder ‘boundary’; G Etter ‘portcullis, grille, fence, frontier; OS ëder ‘fence’; OE eodor (2) “house, dwelling’; EME edder 'tierod on fence’; ON jaðar ‘edge, selvedge’ beside erói ‘beam’; OCS jadro (2) ‘mast, rudder’ beside Blg. odăr ‘bedstead; porch’; Cz. odry, pl. ‘scaf- folding’; Slovak vôdor ‘dutch barn, drying- shed, threshing-floor. Cf. the variant *ordh- in Li. ardas (drying-rack', ardai, pl. *scaffold- ing’; Latv. ards 'drying-rack, cross-timbers'. See ordh- and rdh-
4712:ghlaues, ghlauuos “bright; brilliance’. Cf. WP I, 624 W (ambig.) glaw ‘brightness’; OHG glao, glawes gs. beside glou, gs glouwer “clever”; OS glau, id.; OE gléaw ‘keen; wise’; LG glau ‘gay’; G glau ‘fresh, bright’; Icel. glöggur (1) ‘clear, visible’. (The isophones Go. glaggwō ‘carefully, exactly’; Icel. glöggur ‘stingy’ & G glau, also glauch ‘barren, non-ore-bearing' are of uncertain etym. Hes. glausós ‘bright, bold' appears to be a variant of glaukós ‘bluish’, a LW in Lat. glaucus, of type *glauk-)
4992:ghrudos, is, io (1) (coarse; coarse meal, groats’. Cf. ghrudos (2) & ghrüdos Lat. rudis “new, fresh, rude, boorish'; OLat. rodus ‘rude, crude, unshapen'; Ir. gruid “lees of malt; Du. grut ‘porridge, grits’; OE grot ‘meal; particle’; pl. grotan ‘coarse meal’; grytt ‘dust, meal”; grytta ‘coarse meal, chaff, bran’; OHG gruzzi ‘bran’; MHG cf. grüsch, id. Cf. also ghrusd- and WP I, 649. (FK: EWDS: Grütze)
4993:ghrudos (2) ‘broken, breakable, fragile; trun- cated’. Same as (1)? Mir grod ‘short’; Ir. grod ‘quick, prompt’; Lat. cf. rudis (in sense of ‘new, fresh’); OE cf. grot (2) “earth, soil beside grut, m. ‘rock; chasm’; Swiss Grotz ‘polled fir; Li. grudùs ‘fragile, sensitive’. Ir. groidhe, adj. ‘sturdy, spirited’ is semantically to ghrudos (1). Cf. E grotty “nas- ty’; G grotzig ‘dirty’
5199:guou- (gu-) “ox; filth’. See guóu- and cpds. R- and z-gde forms in Skt. eu beside -gaváb, cpds.; OBr. bu- in bu-es ‘stable’; OW bu- in bu-al *drinking-horn'; ON kýr, as, ds kú; R cf. gumnó, Cz. humno *threshing-floor, barn’, fr. *guou- or *gueu-mn, lit. *ox-press' beside Cz. hov-ézí, adj. ‘beef, hov-ado ‘beast’; hov- no, R gov-no “dung”
5228:guisoros (guisros) “fresh, green’. Cf. guis, and WP I, 666 Per. (?) zahàr ‘belly’; Arm. cf. ner-kur ('skill- ed”, if for *entro-?); Gk. dierós ‘moist, fresh, lively’; Lat. cf. viridis ‘green’; Fris. kwier, adv. ‘nicely, neatly’; OCS Zirü ‘pasture’. (Uncertain if guis- forms part of Per. zahar “abdomen”, and of Lat. viscera. See next). For Per. zahr, cf. guhesl-
5350:guðus “head of cattle, ox, cow. WP I, 696. (Z-gde variant: gii-) Skt. gauh, pl. gāvah “head of cattle’; gávam ‘bull’; gavah ‘ox’; gavih ‘cow’; Av. gáus; Per. gàu, gàv; Oss, qug, gog ‘cow’; Arm. kov, u-st. ‘cow’; Tokh. ko, pl. kowi; B keu ‘cow’; Hitt. .. us ‘head of cattle’; Hiero-Hitt. wawas, id. (for *hwawas); Myc. qou-; Gk. boüs; Lat. bos, gp boum; Umb. bum, acc.; Olr. Ir. bó, pl. ba; W bu, buw; Cor. bow- cpds. ‘cow’; OBr. cf. bou-tig *'cow-house'; OHG kuo, pl. kuo, kuoi, gp kuo; OE cü, pl. cy; LG kau; Fris. kou, pl. kij; Du. koe; OCS cf. gu-mno 'cow-tread', i. e. *threshing-floor', and com. Sl. Cf. min-; Cz. hav-éd' ‘vermin’ beside hov-ézí ‘beef; Latv. govs, gs id., gp govju ‘cow’. Z-gde variants in-
5540:guhrendho, ið “crush, grind, tread down, gnash (the teeth)'. Variant: ghrendh-, q. v. WP L 656. (For the isophone, cf. guhremdh- ‘growl’, etc) Alb. grind 'torment'; Lat. frendo, Gre, and frendeo, ere ‘grind; crush; break; gnash the teeth’; cf. fressus, adj. ‘crushed’; MIr. grean- naim ‘carve, engrave’; con-grennim ‘scrape to- gether’; cf. grinneall “lake-bed'; Go. grinda-, cpds. ‘grind-; MHG grint, sm. ‘scurf?; OE grindan ‘grind, rub, scrape, gnash the teeth’; Li. gréndžiu, gresti ‘scour, scrape; raze skin; pave, lay down, press; cf. also Li. gréndimas *threshing-floor'; o-gde in Li. grándau, -yti ‘scour’. Variant in Du. grint (gravel, fr. *guh- rend-). Of uncertain connexions are Alb. grí, gs grini ‘whetstone’; er, aor. grina, v. ‘whet’; OE grind ‘crash’, grinde ‘shingle’; Br. brenn *bran', fr. either *gurendh- or *bhrendh-
6490:iðr- (2) “fresh, clean, clear, pure’. Cf. WP I, 3, 208, 775 and next
6501:Romani (ambig.) jalo “fresh, raw’; Gk. zorós “pure; neat, of wine’; Cz. jary “fresh, youth- ful, highspirited’; R cf. jarkij “clear, serene, bright"
6651:kak- (4) ‘strike’ (Phonol. ambig.) Skt. ka$àmi “strike, kil; Arm. kasum, aor. kasi ‘thresh’; OCS cf. pri-kosno -noti “touch?
6667:kal- (5) ‘thrust’. (Same as (4) and (6)?). Cf. WP I, 437, but cf. kol- Skt. kalāmi, kalayāmi (2) ‘thrust, drive’; Arm. cf. kal, o-st. ‘threshing floor” (fr. *kalios); Alb. kall (2) ‘thrust, insert, bung’; Lat. cf. inter- calo, are (1) “insert”; OCS (here or under (6)) koljọ, klati ‘stab’; Li. kalù, kálti ‘drive in; forge’; Latv. kaļu, -t, id.
9972:loiksos, a ‘stroke, mark’. Cf. loisa & WP II, 344 Skt. lekhah, m., Aa f. ‘stroke, line, streak, fur- row; drawing, writing'; z-gde in likh-, rikh-, vbl. root ('scratch', etc.); Av. raeka "line"; (Li. láiSkas & laiskas “leaf: letter, message’; lai$kuüs "bitter, tar & OCS léxa 'garden-plot, bed, bor- der" are potential isophones only); Blg. cf. lèša, v. ‘scrape — hideg’
9980:loik- (1) ‘twist, twine, wicker, matting, bas- ketry’. Av. rae50, m. (2) ‘beard’; Per. rís (2), id.; Lat. licium ‘woof, yaro’; Blg. OCS lësa ‘hurdle, frame, rack, mat’; Pol. lasa ‘sieve’
9981:loik- (2) ‘fragment, droplet, grain’ Skt. lesah “atom, particle, drop’; Per. rize “frag- ment’; Hes. *loikos, written: loikor ‘millet; Li. laišis, gs. -10, m. "lenti
```


## [2026-10-16T05:14:05.625Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==164' HRN.txt | grep -n -i -B2 -A8 -E 'r[eēi]s|Bart|beard'; echo ====; grep -n -i -E 'rae[sš]a|raēša|raesa' BRT.txt | head"
}
```


### [2026-10-16T05:14:05.943Z] TOOL RESULT

```
Exit code 1
6-kurd. rltin *kacken'; oss. d. liyun, t. Hin (168); bei.
7-rii/ay (315).
8:610. vis (*m) *Bart', rese *Haai'\
9-aw. ra^sa- zweifelhaft (Hörn, ZDMG. 43, 33,
10-Jackson, Amer. Journ. of Philology, Vol. XI, 88);
11:phlv. res *Bart' (AV.), resak *Haar (vd. 7 (28) Gl).
12:kurd. ruh, ri *Bart'; afy. ^Ira (aus *riSa) bezw.
13-^ire; oss. d. re/e, t. rt/T (213); wa/. reyis, i^itr. ri/is,
14-rikis, minj. yarzd,
15:Vergl. Bartholomae, Studien II, 54, 55.
16:641. veH') 'Wunde, Geschwür, rese, resTde,
17-aw. ra^sah' 'Wunde', [/^rars-, ra^ayat 'verwunden ;
18:phlv. res, resiian ; ai. l^reS-, resat^ reHyati *versehrt
19-werden ; beschädigen'.
20:LW. kurd. m; bei. res 'Wunde' (225).
21-642. reg \Sand' (AM. 242 Zeile 9), rez (Käs. Z. ryz).
22-LW. (?) kurd. rik^ rig; afy. reg; bei. rek^ n.
23-re/ (317).
24:Bartholomae (ZDMG. 46, 301 No. XIX) stellt die
25-iranischen Worte zu ai. sikata- 'Sand', während sie
26-Geiger an aw. l/^rafx- (No. 638) anschliessen wollte.
27-643. rew 'Betrug, List* (Sahn. II, 735 Vers 939), rewäs,
28:reimen, rlmen 'betrügerisch'^).
29-ai. rip' 'Betrug* (l/"rep-, lep- 'anschmieren').
30-Vergl. fireften (No. 829).
31-») *liem', LW. kurd. afy. rim *Eiter*, bei rgm 'Eiter* (224), wa/.
32-rim *Schmutz\
33-2) Der Mftihülvokul ist bezeichnet AM. 231 Zeile 3.
34-*) *Repmetiy vergl. * Verlorenes Sprachgut* No. 83. Die Volks-
35-otyraologie macht das Wort zu einer Verkürzung von Ahrlmen. Da die
36-Bedeutung 'sclimutzig, unrein* dem Worte nach der Überlieferung nicht
(eval):1: === not found
```


## [2026-10-16T05:14:10.962Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"ra[eē]i?[sš]a|raes\" BRT.txt | head -20; grep -n -E \"Bart[’'‘]\" BRT.txt | head"
}
```


### [2026-10-16T05:14:11.267Z] TOOL RESULT

```
2335:P.  (in  3SPM.  usw.):  Praesens. P.  (in  NPt  AP.  usw.  nnd  in  3PPfA.  usw. :  Flu
2356:FFA.:  Part.  Praes.  Akt.
2357:PPtP. :  Part.  Ferf.  Pass. ,FFM.:  Part.  Praes.  Med.
2360:Praes.:  Praesens.
2361:praes.:  praesentisch.
2411:Die  ZilTem  hinter  Praes.,  Ferf.,  j-Aor.  gehen  anf  meine  ZähUinfr  der  Praesens(DSw.)formationen in  GIrPh.  /.  49  f.     Die  nnter  V.  (Verbslsiamm)  eingeslellten  Partizipien  sind  mit  Sperrdruck
2631:•  j.,  g.  aen-'' V.  'vergewaltigen'.   Praes.
2633:'vergewaltigen,  kränken':  ks'iwqmyim akurim  mazdam  "mazislayanti  isA.)  tnaotü V./i-.öi. aL  inMi,  'initak.  —  Pü. ;  tetümtan.  —  '5  Das  ^ n  ist  im  letzten  Grunde  praesentisch.  —
2635:Vgl.  lainai-,  —  Pü. :  iiiili,  erl.;  vinäsiär. •  j.    aenah'ya-  den.  Praes.  31  'zu  ver- gewaltigen'.
2702:aes-V. 'Herr  sein  Über —'.  Praes." —  Inf.  Wie.
2731:Zum  V.  äs-;  s.  unter  ana-,  —  aL  ihm-  n.  — )  VgL  iKoDstT.  Dbr.  AiS.  185. j-,  g.  'aeä-  V.  'suchen'.  Praes.  3  isa-, a  isa-,  *»Ja-'',  14  b  tfasa-,  aisasa-", 17  (Fut)  aifya-,  30  (Iter.)  aSsaya-;  Perf. iyals-^,  yals-i\  —  PPfP.  isla-,  PFP.  k><7-;
2748:Zum  V.  äi-i),  Praes.  i^a-'X  —  ai.  f-ia-OAdj.  l^r)m  aojöngkvat  "so  erstrebe,  O  VM.,   für
2776:afiar;  damit  wird  aber  auch /^W  übersetit.  |,  j_  ,g^^^^,  ^  .pg^g..  _j,^^/„„  zayan^m •  j.,  g.  =ae5-,  p.  ais-  V.  '(sich)  in  eilige  Be-  ysstryehe  fhiyantö  'la  CND.)  >'»yA«»»(sd.) weguQg  setzen'.  Praes.  3  iSa-,  27  isya-,  30  ■  v_  j^^  ^^
2805:aedasa-  Adj.  'suchend,  ausgehend -',  mit  Akk.:  töi  narjpi/  *an>ßs  'sa einen  Sau,  substantivisch  in  Kongruenz  |  (pjpm.)  äijit.arpm  p»sö4anv5  ka  asavä mit  dem  Praedikat:  astuyi  damam  {^^Mahurö\tA.)  yi  Ts' . .  Ä3mihyäJ (sd.)  "sie,  die '/J  as/i  dainnya  . .  äsiailir  (sö.)  Y.  J2. 9 ;  i  darauf  ausgehen  die  Würdigen"  herabzu- —  yat  hl  nr'tp  fr9dvo.st?hamm (sd.)  ..'^^ setzen,  die  Missächter  des  heiligen  Rechts, zi  asti  äiiiya  kata  (statt  NS.)  aetake  yat:  djg  jjjren  Leib  verwirkt  haben  -;  wo  ist irisiahe  ".  .  so  (wie  beschrieben)  ist  die  der  .  ."  V.  \J.  9". vorschriftsmässige  Kammer  für  den  Leich- '     Zum  Praes.  14  des  V.  'a?/-.  —  Vgl.  üaia-,  —
2869:•  ]*.,  g.  aog-  V.  'praedicare'.  Praes. laog-  [,  22  flö/ffa]').—  PPfP.aox/a-,  PFP. aejya-.
2947:•  j.  aobg-  V,  'niederhalten,  -drücken'. Praes.  27  (Pass.)  ubjya-,
2966:•  g.  aoz-  V.  'achten'.     Praes.  i  uz-.       \     näml.  Kavay  Vi,,»-,  vgl.  Dst.  ZA.  j.  39. 'achten  für  -',  mit  dopp.  Aklc. :  ki  kvö  ,  j.  ao§ö.tara-  Adj.  'der  verderblichere,
2979:•  j.   aos-  V.    sagen.      Praes.   2   aosa-.       \      Kindern),    die    als   -/«rHsches  Zeichen  ange- Nur  Med.  'sagen,    sprechen';    es  folgt  i     sehen  wurde.    S.  noch  No.  2.  —  D  rt..%  ,/«•
3047:Nom.   act.  itus  aicya-,  den.  Praes.  31   aus  ata- (flC  für  ay,  %  2g8.l,  oder  statt  i>,  S  268.  1 1  c)j».
3126:Stall  aiinmi'  geschr.;  S  ^^S.  57").  —  PPM., Praes.  lo  7;itiri^;  vgl.  gr.  ^äs»;  (nach  Prrll- wn7,  Wb.  344  eiß.  'Verkleinenuig').  —  Pü.; fa  onbär  vindüiüh,  erL  i  kui  päHxsäkih  i  apit amoArasfandän    slawr.    —     >)  NA.    ai!a^mi' ;
```


## [2026-10-16T05:14:17.777Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"r[a-zä^]{0,3}[sš]a[-h]?.{0,20}(Wunde|Verwund|Bart)\" BRT.txt | head; grep -n -E \"urvan|urvä|urva\" BRT.txt | head -5; grep -n -E '^(ruwān|ruwan|ruvān)' PHD.txt NYB_vol2_glossary.txt; grep -n -E '^r[eē]š' PHD.txt NYB_vol2_glossary.txt"
}
```


### [2026-10-16T05:14:18.143Z] TOOL RESULT

```
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2470:—  dgL:  al/s  giuS  urvä  raostä  .  .  yüzim aiibyO  (yiimX. gaobyd)'''*  ..  aogS  data  Y.sp. 10;  —  spintä  ma'myS  .  .  xia'irä  .  .  vohü mananha  .  .  aHbyö  (AbL)  .  .  Y.  4!j.  6 ;  — yastat  mtzäim  Aan>ntl  nöit  däitl  yS  it ahmüi  3r7zux'iä  (sd.)  nä  däiti  Y.44-J9', — -  'ia/aAyä  mahränO  . .  ahyä  . .  Y.^2.14; 43-9, 49-1,2,^6.3, 40.  s';  — -ahurSmazdt'
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2475:—  dr3gvä..ahya  fyao^anäis  akut  *3  fyqs  a^a^ara(sd.)  aya'^^  ra/u/risN.54;  — _>■« manatfhö  Y.47.5;  —  y^  •■  ^^yi^  zaohng  .tanup^rt^ah^  apa.rao^tmnaAe  (sd)  *a)a- usus  vann^ng {sd.)  Aa/aiteY.4S.4; — yimö\yaurva  *aya'^^'^'>  ralv/ris  Vi. $4.  b)  Das ..  yal  kirgnaot  airihe  x/a'iritoa  .,  Y.^.  4;  j  (subst)  Pron.  dem.  steht  an  Stelle  des  rel.
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
PHD.txt:559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
NYB_vol2_glossary.txt:3309:rēš [lyš] beard 267 32%. - = NP; Ps. lyšy.
NYB_vol2_glossary.txt:3310:rēšēnītan [lySynytn']todamage 56!9.—Den. of reš, Av. (1486 sg.) račša(h)- ‘injury, damage’, Paz. rēš = NP ‘a wound, sore’. V. also a-rēšītārihā, from résitan = ~.
NYB_vol2_glossary.txt:3311:rēš-galūtak [lyšglwtk'] the head of the exiles, the exilarch, title of the head of all Jews in the Sassanian empire, ac- credited at the Sassanian court, and responsible to the Great King. for the Jewry of the empire 116°. — Borrowed from Aram res gälütä.
NYB_vol2_glossary.txt:3343:rēšn [Iwšn'] 1. adj. light, bright, lumi- nous, splendent, brilliant, comp. ~-tar 3722, 668 etc. passim. — 2. subst. light: tai 50 roc ~ né bavét (pres. hist.) during 50 days it did not get light 2015; ~ bavandak 574; bun ~ primeval Light 1118-21, 11219; 965, — Av. (1488) raoxšna-; MPrthPrs rwšn; Paz. rös(a)n; NP rau- šan.
NYB_vol2_glossary.txt:7362:rēš: rēšēnītan
```


## [2026-10-16T05:14:24.766Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E '.{0,150}rēš \\[.{0,100}' PHD.txt | head; grep -n -o -E '.{0,30}ruw[aā]n.{0,150}' PHD.txt | head -5; grep -n -E '^ru[wv][aā]n' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-16T05:14:30.954Z] TOOL RESULT

```
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,100}
                          \___exceeds complexity limits


191:following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn,
212:immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd 
316: [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | 
561:wy-, N ~] grow. ~išn: growth. ruwān [lwbn'! | M rwn, N ~] soul. ~ig [-yk! | N ~7] spiritual. ruzd [lwzd | M rwzd, N таза] greedy. ~ih : greed.
1507:deceased anēšagruwān; v. blessed.
3356:ruvan [lwb?n'] soul, the immortal part of the human being: F:2. 9!4, 125, 1326 (v. s. v. vart). 31-34 passim. 72—76 passim, etc. passim; v. also anösak. — Av. (1537 sqq.) urvan-; KZŠPrth ^rwn; MPrth rwn, rwn (A-H. III, BBB); MPrs rwn; Ps lwb’n; Paz. rua; NP ravan.
```


## [2026-10-16T05:14:35.352Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 558,559p PHD.txt | grep -o -E 'r[eē][sš][^|]{0,20}\\|[^]]{0,40}\\][^.;]{0,40}' | head; grep -n -E \"rwʾn|'rw'n|ʾrwʾn|rw'n\" SOD_pages.txt | head -5; grep -n -E \"ry[sš]'?kk|ryškk|rysk\" SOD_pages.txt | head -5"
}
```


### [2026-10-16T05:14:36.112Z] TOOL RESULT

```
rēšaģ [/yšk! | N rēša] root, fibre
rēšīdan, rēš- [lysyin' | N ~] wound, hurt
8102:                                                                1513 'rw'n B, S, C                                       jljj
14008:     (o/)disciple                                                          Gurwan, Oruwan (Srw'n) ©ob. -y
14013:     5orzyawar, djyawar (5r)y,wr) ©ddzydwar-,                         3605 firw'n =» 5rw*n
14014:       <*drzya <*zrada\ - =»zy}wr, Srzy'wr                            3606 Srw'nc kn5        B    ^^    ^ lO^l^Ajy O'yOjj < 0'j>
14987: 3961 fryrw'n =* fryyrw'n                                               Hen. Cosm. 307.49
7863:      arsk ©<Av. araska; MP yrysk ©nom. -w
11645: 2752 prysky* B                                 ^i'^L^'v^              frapas ? ©impf. fir*p*s ^frp's-, P^p's-
11751:                                                                        Praxsakya ^prysky*
28634:                                                                8655 rysk S, M
28649:8647 ryncyk S                                    f *&?f         8657 rys'kk B
```


## [2026-10-16T05:14:39.451Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 8095,8115p SOD_pages.txt; echo ====; sed -n 28630,28670p SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} {if(index($0,\"1513 \\x27rw\\x27n\")) print NR-1}' SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} {if(index($0,\"8657 rys\")) print NR-1}' SOD_pages.txt"
}
```


### [2026-10-16T05:14:39.796Z] TOOL RESULT

```
Exit code 1
                                                                     Ardavan
      artxwost, artxust ©*artwahist ^Wwxwst rwc                      Anc. Lett. 3.13
      Ordibehesht, third day of the month
      MDiii p60; GMS 392; Hen. BSOAS 1965, 251,                 1510 >rtyh     M => 'rty1
        n 58
                                                                1511 Ytymw ^ 'rty1, mw
1498 >rtk    S                                           ,/     1512 Ytyy =* 'rty1
                                                                1513 'rw'n B, S, C                                       jljj
      arte (WkCw))      ©Av. as a =*}rt2, Jrty3
      flour                                                          (o)rwan, oruwan ©Av. urvan =»rw}n
                                                                     soul, spirit
      MDii, >rtkw; MDiii p30, }rtw                                     4,-y
                                                                     TSP; VJ 476, 537, 1188; STii 123; Frag. Len. 97a,
1499 Vtms => ms, 't1, rtyms
1500 >rtt rwc S            (^-V-W^r*              jJjOjjj^      1514 Wrt       M                                ^>^jU
     art-roc, as-roc =»*rt rwc, *s rwc(yy)
     ninth day of the month                                          orwart ©<Av. urvaOra =»rw'rtyh
     MDiii                                                           fine, delicate
                                                                     GMS 100; TSP 19.15; Hen. Texts. 713.5
1501 Vtw C                                •*i/<j*>«k,l          1515 Vw'st'k B                            <u^«u^U
     artaw ^rt'w
(eval):1: === not found
```


## [2026-10-16T05:14:45.824Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28645,28665p SOD_pages.txt | cut -c60-200"
}
```


### [2026-10-16T05:14:46.107Z] TOOL RESULT

```
           W-Lii 547.6; BBB pl34; GMS 464, 1241, 1288;
             Hen. Tales. 481.39; C2, 48 R25, 68V30 p224;

             STi; Sund. AoFviii 1981, 24V7 pl89
     8657 rys'kk B
          rese, resak ? ©Pahl. res

          beard

           VJ914

     8658 ryst> =* rst(h)
                                                               cri->
     8659 rysty'q C
           r(i)styak, rostyak   (rsty'q) =»rst(h)
           truth
                                                       iM>
          STi 40.5, 44.4, 53.5; GMS 517; Sund. AoFi 1974,

            224
```


## [2026-10-16T05:14:50.178Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 443 444 445 446 447; do echo \"== leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -3; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n -E 'ریش|rēš|res|Bart|beard' | head -12; done"
}
```


### [2026-10-16T05:14:51.303Z] TOOL RESULT

```
== leaf 443
  ‫رورشنه‬                                                                                            ‫”‪~A‬‬

                                                                ‫جو بنده‪ .‬کشت وزراعت پزرور و بالیده را‬
== leaf 444
 ‫‪۲‬‬
                                                                                                                        ‫ررین‬
‫پر افراسیاب هم هت که در جنگ دوازدمرخ‬                            ‫بروزن علی بند » بلغت زند وپازند (‪ )۱‬سپر را‬
== leaf 445
 ‫ره آورد‬                                                                                                     ‫ها‬    ‫سا‬

‫روبین خم است کهکوس و نقارة بزرکه باشد ‪.‬‬                       ‫روبین تن است که لقب اسفندبار ‪-‬‏ وکنابه از‬
== leaf 446
  ‫‪7‬‬                                                                                                          ‫رهاوی‬


== leaf 447
 ‫ری‬                                                                                  ‫هوت‬
                                                                                       ‫‪-‬‬
‫ه بررزن شهپر » مخفف رهوار‬      ‫ھور‬
```


## [2026-10-16T05:14:54.740Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /ریش/ && /res|rēš|rêš|Bart|ris/ {print NR-1}' BQT_v2_pages.txt | head; for L in 448 449 450 451 452; do echo \"== leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n -E 'ریش|r[eē]s|ris' | head -12; done"
}
```


### [2026-10-16T05:14:55.490Z] TOOL RESULT

```
101
== leaf 448
== leaf 449
== leaf 450
70:        ‫«اسشق ‪« : ۱8۹‬مصلحت ندبدم ازین بیش ریش دروش را بملامت‌خراشیدن » « کلستان ‪۰ ۹۳‬‬
== leaf 451
5:                                   ‫ابباریشم باش‬       ‫ریش خو ت‪۵2‬ه با ای مجهول ‪ ۰‬نام‬
13: ‫ریشیده ‪ ۲‬ه بر وزن پیچیده » ربغ‬                       ‫شودو کوشٌآن لته کراهآوشته وشراب "رشده‬
14: ‫دستار باشد ‪ -‬وبمعنی رنکگ بپشته و ریگ نهاره‬           ‫وقطره قطره‌شراب اآزن میچکیده باشد لیزریش‬
17: ‫ازیادشاهان هند حم بوده است‪ -‬ویمعنی رخشنده‬            ‫ریش گاو = با ثالی معروف ؛ مردم‬
19:                          ‫شده رگاوشد ‪.‬‬                ‫شخصی پرخود راگفت که «هرکز ریش کاو‬
26:                           ‫صحرا باشد ‪. ۷‬‬              ‫ب رکفت ‪ « :‬ای پدر ! من همه عمر ریش گاو‬
38: ‫کویند ‪٩‬‏ ‪ -‬وباکاف قارسی‌بروزن دیگه معروف‬                ‫ریشمالی ‪ - ۴‬بروزن‌نیك‌فالی‪.‬د‪,‬وی‬
== leaf 452
11: ‫جام لطیف بود و آنراکیمیا باکاف فارسی هم‬                              ‫بی‌نقطه بروزن بیجاده » بزبان اهل مروخاریشت‬
```


## [2026-10-16T05:14:57.975Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:988 --image 2>&1 | tail -60"
}
```


### [2026-10-16T05:14:58.453Z] TOOL RESULT

```
no scan of BQT covers printed page 988 (see 'scans' in refs_online.json)
```


## [2026-10-16T05:15:00.741Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==451' BQT_v2_pages.txt | head -80"
}
```


### [2026-10-16T05:15:01.187Z] TOOL RESULT

```
    ‫اس‬                                                                                                  ‫رىژك‬
             ‫ماضی ریدن و لجاست کردن باشد ‪.‬‬                          ‫وآرزو و هوا وهوس را بیز گفته‌اند ‪٩‬‏ ‪.‬‬
‫= بروزن زستن» فرورفتن بچاه‬              ‫ی‬‫ل‬                   ‫ریژ ك ‪ -‬بکر اول وفتح زای فارسی‬
 ‫باحوض وامثال أن باشد‪-‬ویمعنی موبیدن ونوحه‬                    ‫وکناه کردن و از جای‬         ‫»ن‬
                                                                                          ‫یكا‬
                                                                                            ‫سيش‬
                                                                                              ‫عن ش‬
                                                                                                 ‫بر وز‬
‫سفتن و کربه‬
          ‫یخف‬
            ‫کردن همهت ‪٩‬ک‏‪-‬روم‬                                                    ‫فرو لغزبدن باشد ‪.‬‬
‫وجاست کردارا نیز‬
               ‫کردن بود ‪ - ۷‬وریدن ت‬                          ‫ريز هةسیهیی ک=نابه از ستارگان‬
                                        ‫کوند ‪. ۸‬‬                                                        ‫باشفد ‪.‬‬

 ‫= با اول بثانی مجهول رسیده‬             ‫سی‬
                                         ‫ر‬                   ‫دیزی راز = بعنی رحمتی بکن ‪۰‬‬
                                                                   ‫هم مده است ‪۰ ۳‬‬          ‫چه رىز بمعدی رحمت‬

                                             ‫است ‪.‬‬         ‫ریس = بکر اول وسکون‌ثانی وسین‬
 ‫ر پسیدن ‪٩‬‏ س بروزن لسیدن » رشتن‬
                                                         ‫بی‌نقطه » غضب وقهر وخشم راگویند ‪ -‬وباثالی‬
    ‫پنبه و تافتن پشم وابرشم وامثال آن باشد ‪.‬‬
                                                         ‫مجهول ‪ .‬شوربای غلیظی کهبربالای شله پولاد‬
 ‫است‬       ‫رشو»ف‬
               ‫عنکی‬
                  ‫موز‬
                    ‫دش = بر‬                                  ‫و کشکك وامثالآن ریزند ‪ - ۴‬و هربه وحلیم‬
                                                             ‫را دز گفته‌اند لیکن قبل از آدکه پخته شود ‪۰‬‬
 ‫‪—-4۹‬‬    ‫جراحت‬   ‫‪۰‬‬   ‫با ثالی محجپول‬     ‫خوانند و‬                  ‫تم‬
                                                                   ‫هن ه‬
                                                                      ‫یهعننیوزآبکی باشد ‪ -‬و امربرشت‬
 ‫وشوربای‌هربه راکویند پیش ازکفجه زدن؟‪.۱‬‬                       ‫بعنی بربس ‪ ۴‬و‪-‬بفتح اول در عربی خرامیدرا‬
‫بیدشوع‌سفید کردن ‪ -‬کنابه‬        ‫ر‬                                                                    ‫کرننده ‪.‬‬
   ‫از مردم بیمقل و کسکه کم تجربه باشد ‪.۳۱‬‬                    ‫‪« ۰‬عنی رید که‬   ‫بروزن زست‬        ‫=‬    ‫زر لست‬


                                                                                       ‫)‪ (۱‬چك‪ :‬و ‪.‬‬


                 ‫‪ = ۱‬ریز (ه‪.‬م‪).‬ریرٌ» معمولا با «کام» اید و ریژکام با ریژوکام گویند ‪:‬‬
          ‫با ریدکان مطرب بودی بفر و ژب‪.‬‬                             ‫دیدی تو ریژو کام بدو آندرون بی‬
   ‫«لفت‌فری‪.*۹۷۱‬‬        ‫کی سمرفندی‬     ‫رود‬


   ‫سپولت شناخته میشود که همان سغدی ‪( 0128۲‬میل » شهوت) است ونیز درسفدی‌مصدر‬
                                                                             ‫‪ ) hzêr‬دوست داشتن) آمده‪. ‎‬‬
             ‫‪Henning,‬‬           ‫‪Sogdian‬‬      ‫‪‎ BSOS.,X, 1,p.99.‬و ‪loan _ words...‬‬
   ‫‪-‬ب ریس پمعتی آب‌چلومعمول‬
                          ‫‪ ۴‬آ‬                        ‫‪.‬‬       ‫اسبید‬
                                                                 ‫منا‬
                                                                   ‫ت) مت‬
                                                                       ‫رعر‬
                                                                         ‫‪-‬معنی فتض (‬
                                                                                   ‫‪ ۴‬ب‬
   ‫‪( -‬عر) قرس بفتح‬          ‫‪0‬‬            ‫رشنن ‪.‬‬   ‫رك‪ :‬رسدن ‏‬           ‫‪۴‬‬          ‫نامه ‪8‬‬    ‫‪ ۱‬لت‬   ‫‪ ۴‬رکه‬    ‫است‬


  ‫رسته بمعنی مرده «بشتها‬         ‫=‬    ‫در پهلوی رستك‬      ‫‪-‬‬    ‫‪۹‬‬          ‫اول‪ ,‬خرامیدن» « منتهی الارب» ‪.‬‬
                     ‫رك‪ :‬ريدن ‪.‬‬       ‫‪۸ 7‬‬         ‫کی‬                 ‫ر‬             ‫‪۲‬ص‪ ۳۳ ۲‬رك ‪ :‬رستاخیز‪.‬‬
  ‫‪ir‬‏‬       ‫بهلوی ‪hser‬‏ (لحه)» ‪kahsêr‬‏ (مو)‪ .‬کردی ‪۱‬‬                  ‫‪1‬‬           ‫رشتن ‪.‬‬      ‫‪ ۹‬رك‪:‬‬
   ‫(لحبه) ‪ .‬افنانی ‪( 871۳2‬از‪ 67102 .)* ۵۳21۲‬استی ‪ 153۲۰ ۰ 65۵۲‬وخی طکنطعع‪ .۲‬منجی‬
  ‫و کرباش ) ملاح (‬           ‫وراك‪ :‬هو شمان اسا »ورك‪ :‬رش‪ ۱ :‬چندانکه رش‬                   ‫«اسشق ‪۰‬‬         ‫‪82‬‬

   ‫‪ ۹‬اوستا‬          ‫بدست جوان در اوفتاد بخود کدشرید وبی محابا فرو کوفت» گ«لتان ‪. ۷۱۱۲‬‬
    ‫_‏ ‪ , çj ( 01211562۲‬جراحت) از رسَه‪tayhser . 9562۲ -‬‏ (مجروح کردن)‪ .‬بهلوی ‪,15۵۲‬‬
      ‫م)‬ ‫خ‪51‬‬
           ‫ز‪7‬‬ ‫(وچی‬
                 ‫_ هندی باستان ربشه ‪tahsêr , ۲5۵۲ -‬‏ (زخمی‌شدن)‪ ,‬کردی وبل‬        ‫‪0‬‬
        ‫«اسشق ‪« : ۱8۹‬مصلحت ندبدم ازین بیش ریش دروش را بملامت‌خراشیدن » « کلستان ‪۰ ۹۳‬‬
                 ‫‪ -۴‬مصدر است معنی عمر رابسفاعت کنرانیدن‬                       ‫(«‪.‬م‪).‬‬    ‫رس‬     ‫=‬   ‫‪۴۷‬‬
```


## [2026-10-16T05:15:07.520Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==452 || NR==453' BQT_v2_pages.txt | grep -n -E 'ریشه|rêš|resak|šak|ريشه' | head; grep -n -E 'روان' BQT_v2_pages.txt | head -0; awk 'BEGIN{RS=\"\\f\"} /urvan|urvân|ruvân|ruvan|ravân/ {print NR-1}' BQT_v2_pages.txt | head"
}
```


### [2026-10-16T05:15:08.511Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:15:11.876Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 422 423 424 425 426 427 428 429 430; do c=$(awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -c -E 'روان'); echo \"$n $c\"; done; awk 'BEGIN{RS=\"\\f\"} NR==452' BQT_v2_pages.txt | grep -n 'ریشه'"
}
```


### [2026-10-16T05:15:13.182Z] TOOL RESULT

```
422 0
423 0
424 1
425 0
426 0
427 6
428 7
429 0
430 0
```


## [2026-10-16T05:15:15.771Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==428 || NR==429' BQT_v2_pages.txt | grep -n -E 'روان|[a-zâêîû]{3,}' | head -40"
}
```


### [2026-10-16T05:15:16.188Z] TOOL RESULT

```
5:‫استاده روید و بمربی جرجیرالماء و کرفس‌الماء‬                         ‫ورواح وروان باشد ‪ -‬ویمعتی حصول‌کار هم‌هست‬
15:‫روان = بفتح اول و الیبالف کشیده‬                                     ‫وآب تیره رنگگ را نگیفزته‌اند » وبضم اول حم‬
26: ‫روان نفس اطقه است واز جان روح حیوالی*‪.۱‬‬                            ‫رواد ‪ = ۶‬بورزن نماز " بمعنی روار‬
27:‫روانان ‪ -‬جمع‌روان‌است که فوی‌باشد‬                                                        ‫است که خدمتکار زندایان باشد ‪.‬‬
39:  ‫د لك‪۲ ‎‬‬             ‫‪mul‬‬
52:  ‫‪ - ۶‬روان در مورد حیوان و جان در مورد انان ليز بکار رفته‬                                                    ‫› ‪.‬‬       ‫«اسشق ‪۵۲۱‬‬
54:         ‫روان کوسفند از وی بنالید ‪...‬‬                                           ‫لقشید‬
62:  ‫سره‬                                                                                    ‫روان آورد‬
64:                     ‫داشن را فيز گویند ‪٩‬‏‬        ‫سیفتح واو وسکون را‬         ‫روان ورد‬
73:           ‫عنبالملب خوانند در اختبارات ‪۰#‬‬        ‫روان بخش ‪ ۰ ۱‬فدرمخته‌ایت که‬
77:‫باشد )‪(٩‬‏ چه تربك بمعنی انگور باشد‪.‬و بعربی‬        ‫روان بد ‪ - ۲‬ینم بای ابجد ()‬
81:‫رو باه ترکی باهای مکور‪ .‬خار‬                      ‫روان خواه ‪ -‬با خای نقطه دار‬
87:                                                  ‫روان کرد ‪ = ۴‬بکرکاف وسکونرا‬
110:  ‫‪ ۴‬از دساتیر «روان گرد بکرکاف فارسی شهرروان که افلاك باشند و عالم ملکوت »‬
120:                     ‫مانوی(یارتی )‪elddiM 215۲6۳ ۷۷۳:,...0 9 5‬‏ ‪,gninneH( A tsil fo‬‬
123:                                                                                  ‫‪) Renard‬ر(‪. ‎‬‬
```


## [2026-10-16T05:15:18.392Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==428' BQT_v2_pages.txt | sed -n 36,60p"
}
```


### [2026-10-16T05:15:18.744Z] TOOL RESULT

```
  ‫ارونة‬    ‫‪٩‬‏‬   ‫که بدان بار بر شتر نداد‬           ‫ککاء » رسنی‌است‬           ‫(عر) «رواء‬        ‫‪-‬‬   ‫‪۴‬‬             ‫«منتهی‌الارب» ‪.‬‬
  ‫د لك‪۲ ‎‬‬             ‫‪mul‬‬
                        ‫‪=S‬‬‫‪٦‬‬                      ‫«روار» («‪.‬م‪۰ ).‬‬       ‫‪ ۵‬مصحف‬                         ‫‪« €‬منتهی‌الارب» ‪۰‬‬               ‫جمع‬

                                                                                                                       ‫‪۰‬‬        ‫‪۹۸۱‬‬    ‫ص‬
          ‫خکاهنه خالهةٌ قىت‪.‬‬
                           ‫|‬               ‫رماود‬
                                               ‫کورمف ل‬                ‫سرواق منظرچتم من آشیانهتنت‬                            ‫‪۲‬‬
  ‫«افظ شبرازی ‪۵۲٩‬‏ ‪.‬‬
                   ‫ح‬
  ‫‪0712۷021‬‬        ‫استی‬    ‫فاعلی) ویمعتی حال مکار روده‬            ‫آن ( يوند‬      ‫‪+‬‬    ‫)‬    ‫(رفتن‬        ‫از‪ :‬رو‬      ‫‪-‬‬        ‫‪۵‬‬

        ‫(بجربان افتادن) ‪ . ۰۵‬است ‪ ۱۳۱۰‬اشکاشمی ‪( ۲۵۷8۲‬متحرك "رونده) گ«ربرسن ‪۳٩٩‬‏ ‪.‬‬
  ‫٭ ‪ -‬پرلوی ‪( ۲۵۷۷۲‬روح) ‪ .‬اوستا ‪* 58۷۳11 -‬پارتولمه ‪ » ۷۳۵۱‬دلیبرگ ‪۸۹۱٩‬‏ ‪.‬‬
  ‫‪ - ۶‬روان در مورد حیوان و جان در مورد انان ليز بکار رفته‬                                                    ‫› ‪.‬‬       ‫«اسشق ‪۵۲۱‬‬
                                                                                                                ‫( رك ‪ :‬جان ) ‪:‬‬
         ‫روان کوسفند از وی بنالید ‪...‬‬                                           ‫لقشید‬
                                                                                    ‫احل‬
                                                                                      ‫بردمبر‬
                                                                                           ‫شبانگه کا‬
  ‫د کلتان ‪. ۲۸۰‬‬
          ‫کنم ‪۰‬‬       ‫بینم وتلیم وی‬        ‫رخش‬    ‫روزی‬                 ‫ابن جان عارت که حافظ سپرد دوست‬
  ‫«حافط شیرازی ‪۱۶۲٩‬‏ ‪.‬‬
```


## [2026-10-16T05:15:23.831Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py --help 2>&1 | head -20"
}
```


### [2026-10-16T05:15:24.253Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-10-16T05:15:33.169Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/horde' 'https://en.wiktionary.org/wiki/Urdu' 'https://en.wiktionary.org/wiki/ordu' 'https://en.wiktionary.org/wiki/اردو' 'https://www.etymonline.com/word/horde' 'https://www.etymonline.com/word/Urdu' 'https://en.wiktionary.org/wiki/ریش' 'https://en.wiktionary.org/wiki/ریشه' 'https://en.wiktionary.org/wiki/روان' 'https://en.wiktionary.org/wiki/urvan' 'https://en.wiktionary.org/wiki/licium' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/ordu'; do python3 tools/fetch_source.py \"$u\" --note \"page 521: etymology check\" 2>&1 | tail -1; done"
}
```


### [2026-10-16T05:15:40.066Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/72a7c8b1aff4dab9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2d1c1da2c1717f16.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/97e58ed857162fee.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8e5427d6757c8613.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/27dd97ebf21c3d33.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5fcdd1377532e99e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0d1d9b9739002132.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ab9ab5bb01a35117.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/719d6b0d42725c50.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8d8d52970b5e5982.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c4a7308a3a86b5f7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1f86b5ea18cd1950.txt
```


## [2026-10-16T05:15:43.278Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -12 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin: d=json.loads(l); print(d['url'],d.get('status'),d.get('bytes'))\"; for f in 72a7c8b1aff4dab9 97e58ed857162fee 8e5427d6757c8613 27dd97ebf21c3d33 1f86b5ea18cd1950; do echo \"=== $f\"; grep -n -i -A4 'Etymology' $f.txt | head -30; done"
}
```


### [2026-10-16T05:15:43.640Z] TOOL RESULT

```
https://www.etymonline.com/word/horde -1 39
https://www.etymonline.com/word/Urdu -1 39
https://en.wiktionary.org/wiki/Thomas 200 34455
https://en.wiktionary.org/wiki/توأم 200 6332
https://en.wiktionary.org/wiki/woe 200 17067
https://en.wiktionary.org/wiki/ژاژ 200 5498
https://en.wiktionary.org/wiki/ریش 200 10872
https://en.wiktionary.org/wiki/ریشه 200 4098
https://en.wiktionary.org/wiki/روان 200 8379
https://en.wiktionary.org/wiki/urvan 200 1914
https://en.wiktionary.org/wiki/licium 200 3479
https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/ordu 200 7197
=== 72a7c8b1aff4dab9
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
91: Etymology 
92-
93- 2.2 
94- Noun 
95-
--
108: Etymology 1 
109-
110- 3.2.1 
111- Noun 
112-
--
114: Etymology 2 
115-
116- 3.3.1 
117- Noun 
118-
--
162: Etymology 1 
163-
164- 6.1.1 
165- Noun 
166-
--
=== 97e58ed857162fee
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
--
76: Etymology 
77-
78- 2.2 
79- Noun 
80-
--
93: Etymology 
94-
95- 3.2 
96- Pronunciation 
97-
--
116: Etymology 
117-
118- 4.2 
119- Pronunciation 
120-
--
142: Etymology 
143-
144- 5.3 
145- Noun 
146-
--
=== 8e5427d6757c8613
65: Etymology 
66-
67- 1.3 
68- Noun 
69-
--
91: Etymology 
92-
93- 2.2 
94- Pronunciation 
95-
--
120: Etymology 1 
121-
122- 3.2.1 
123- Proper noun 
124-
--
126: Etymology 2 
127-
128- 3.3.1 
129- Noun 
130-
--
227: Etymology
228- [ edit ] 
229-
230- Inherited from Proto-Turkic *ordu ( “ army camp ” ) .
231-
--
=== 27dd97ebf21c3d33
=== 1f86b5ea18cd1950
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
--
137: Etymology
138- [ edit ] 
139-
140- Uncertain, however usually considered simplex . EDAL suggests a derivation from a hypothetical *or- verb suggesting *orun ( “ place ” ) and *ortu ( “ middle ” ) as cognates, however a derivation *or-du would have yielded *ortu not *ordu [ 1 ] . 
141-
```


## [2026-10-16T05:15:47.446Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 72a7c8b1aff4dab9 2d1c1da2c1717f16 97e58ed857162fee 8e5427d6757c8613 1f86b5ea18cd1950; do echo \"=== $f\"; grep -n -A3 -E '^\\s*(From|Borrowed|Inherited|Uncertain|Ultimately|Learned)' $f.txt | grep -v '^\\-\\-' | grep -v -E '^\\s*[0-9]+-\\s*$' | head -24; done"
}
```


### [2026-10-16T05:15:47.929Z] TOOL RESULT

```
=== 72a7c8b1aff4dab9
299: From Wiktionary, the free dictionary
301- See also: Horde , hörde , and hørde 
524: From German Horde .
526- Noun
527- [ edit ] 
590: Borrowed from German Horde ; attested from the early 17th century. 
592- Noun
593- [ edit ] 
604: From Middle Dutch horde , hurde , from Old Dutch *hurd , from Proto-West Germanic *hurdi , from Proto-Germanic *hurdiz ; cognate with German Hürde , and closely related to English hurdle (which is a diminutive of the same root). The sense "hurdle" is a semantic loan from English hurdle . 
606- Noun
607- [ edit ] 
716: From German Horde .
718- Noun
719- [ edit ] 
=== 2d1c1da2c1717f16
224: From Wiktionary, the free dictionary
226- See also: urdu , urdú , urðu , and úrdú 
241: Borrowed from Hindustani (see Urdu اُرْدُو ( urdū ) and Hindi उर्दू ( urdū ) ), from Classical Persian اُرْدُو ( urdū ) , from Proto-Turkic *ordu ( “ army, camp ” ) ( > Azerbaijani ordu , Turkish ordu , Turkmen oorda ). Doublet of horde and orda .
243- Pronunciation
244- [ edit ] 
478: Ultimately from Classical Persian اُرْدُو ( urdū ) , from Proto-Turkic *ordu ( “ army, camp ” ) . This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term. 
480- Pronunciation
481- [ edit ] 
528: From Classical Persian اُرْدُو ( urdū ) , from Proto-Turkic *ordu ( “ army, camp ” ) .
530- Pronunciation
531- [ edit ] 
=== 97e58ed857162fee
264: From Wiktionary, the free dictionary
266- See also: Ordu , ordú , and orðu 
274: From Classical Mongolian ᠣᠷᠳ᠋ᠤ ( ordu ) that came from Proto-Turkic "Ordu".
276- Noun
277- [ edit ] 
294: Ultimately from Latin ordō .
296- Noun
297- [ edit ] 
329: Inherited from Proto-Turkic *ordu , from Proto-Turkic *or- ( “ army, place of staying of the army, ruler etc. ” ) , whence also English horde .
331- Pronunciation
332- [ edit ] 
975: Inherited from Ottoman Turkish اردو ( ordu ) , Proto-Turkic *ordu .
977- Pronunciation
978- [ edit ] 
=== 8e5427d6757c8613
216: From Wiktionary, the free dictionary
218- Ottoman Turkish
219- [ edit ] 
230: Inherited from Proto-Turkic *ordu ( “ army camp ” ) .
232- Noun
233- [ edit ] 
449: Borrowed from Classical Persian اردو ( urdū ) , from Turkic .
451- Noun
452- [ edit ] 
=== 1f86b5ea18cd1950
130: From Wiktionary, the free dictionary
132- This Proto-Turkic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
140: Uncertain, however usually considered simplex . EDAL suggests a derivation from a hypothetical *or- verb suggesting *orun ( “ place ” ) and *ortu ( “ middle ” ) as cognates, however a derivation *or-du would have yielded *ortu not *ordu [ 1 ] . 
142- The rather uncommon consonant cluster *-rd- may also indicate a borrowing from an unknown source. Dybo suggests that the word is borrowed from Mongolic rather than the other way around [ 2 ] .
```


## [2026-10-16T05:15:52.710Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i -E 'polish|tatar|french' 72a7c8b1aff4dab9.txt | head -8; sed -n 140,160p 1f86b5ea18cd1950.txt; for f in 0d1d9b9739002132 ab9ab5bb01a35117 719d6b0d42725c50 8d8d52970b5e5982 c4a7308a3a86b5f7; do echo \"=== $f\"; grep -n -A2 -E '^\\s*(From|Borrowed|Inherited|Uncertain|Ultimately|Learned|Possibly|Perhaps|Of uncertain)' $f.txt | grep -v -E '^\\s*[0-9]+-\\s*(\\[ edit \\])?\\s*$' | head -14; done"
}
```


### [2026-10-16T05:15:53.203Z] TOOL RESULT

```
129: French 
131: Toggle French subsection 
311: Recorded in English since 1555. From Middle French horde , from German Horde , from Polish horda , from Russian орда́ ( ordá , “ horde, clan, troop ” ) , probably from Kipchak Turkic (compare Tatar урда ( urda , “ horde ” ) ), ultimately from Proto-Turkic *ordu ( “ place of staying of the army, ruler etc. ” ) . Cognates include Turkish ordu ( “ camp, army ” ) , Mongolian орд ( ord , “ court, castle, royal compound, camp, horde ” ) and Kalmyk орда ( orda ) . Doublet of orda and Urdu .
337: ( collective ) A wandering troop or gang ; especially, a clan or tribe of a nomadic people (originally Tatars) migrating from place to place for the sake of pasturage , plunder , etc.; a predatory multitude .
385: French: horde   (fr)   f 
421: Polish: horda   (pl)   f 
437: Tatar: урда   (tt) ( urda ) 
468: French: horde   (fr)   f 
 Uncertain, however usually considered simplex . EDAL suggests a derivation from a hypothetical *or- verb suggesting *orun ( “ place ” ) and *ortu ( “ middle ” ) as cognates, however a derivation *or-du would have yielded *ortu not *ordu [ 1 ] . 

 The rather uncommon consonant cluster *-rd- may also indicate a borrowing from an unknown source. Dybo suggests that the word is borrowed from Mongolic rather than the other way around [ 2 ] .

 Noun
 [ edit ] 

 *ordu 

 royal camp , palace 

 ( military ) army , camp 

 Declension
 [ edit ] 

 Declension of *ordu 

 singular 3) 

 nominative
=== 0d1d9b9739002132
238: From Wiktionary, the free dictionary
240- See also: ريش , رئس , and ریس 
--
248: Borrowed from Classical Persian ریش ( rīš ) .
250- Pronunciation
--
279: Borrowed from Persian ریش ( riš , “ beard ” ) .
281- Noun
--
292: Borrowed from Persian ریش ( riš , “ wound ” ) .
294- Noun
--
304: Borrowed from Arabic رِيش ( rīš , “ feathering, plumage ” ) .
306- Noun
=== ab9ab5bb01a35117
152: From Wiktionary, the free dictionary
154- See also: ريشة 
--
169: Inherited from Middle Persian [Book Pahlavi needed] ( lyšk' /⁠rēšag⁠/ ) , borrowed from Avestan 𐬭𐬀𐬉𐬱𐬀 ( raēša ) , ultimately from Proto-Indo-European *wréh₂ds ( “ root ” ) .
171- Cognate with Baluchi ریشَگ ( rīšag , “ root ” ) 
=== 719d6b0d42725c50
211: From Wiktionary, the free dictionary
213- See also: زوان and زؤان 
--
221: From French Rouen , q.v.
223- Proper noun
--
240: From رو ( rav ) +‎ ـان ( -ân ) ; the first part is the present stem of رفتن ( raftan ) .
242- Adjective
--
270: From Middle Persian [script needed] ( lwbʾn /⁠ruwān⁠/ ) , Manichaean Middle Persian 𐫡𐫇𐫀𐫗 ( rwʾn /⁠ruwān⁠/ , “ soul ” ) . Cognate with Parthian 𐫀𐫡𐫇𐫀𐫗 ( ʾrwʾn /⁠arwān⁠/ , “ soul ” ) , Avestan 𐬎𐬭𐬬𐬀𐬥- ( urvan- , “ soul; immortal part of a human being or an animal ” ) , Pashto: اروا , and perhaps Sanskrit रूप ( rūpa , “ shape, form ” ) . Ultimately perhaps from Proto-Iranian *urw-āna- ( literally “ what has created a wide room for itself ” ) ; compare Sanskrit उरु ( uru , “ space, wide scope, liberty ” ) . [ 1 ] Old Armenian ուրու ( uru , “ ghost ” ) is probably an Iranian loanword.
272- Pronunciation
--
414: From Classical Persian روان ( ravān , “ fluid, flowing ” ) , a compound of رو ( rav ) +‎ ـان ( -ân ) ; the former is the present stem of رفتن ( raftan ) .
416- Pronunciation
=== 8d8d52970b5e5982
125: From Wiktionary, the free dictionary
127- English
=== c4a7308a3a86b5f7
145: From Wiktionary, the free dictionary
147- Latin
--
153: Uncertain; could be a loan from a non-Indo-European language. [ 1 ] 
155- Noun
```


## [2026-10-16T05:15:57.921Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 240,300p 0d1d9b9739002132.txt | grep -v '^\\s*$' | head -50; sed -n 160,185p ab9ab5bb01a35117.txt | grep -v '^\\s*$'; sed -n 150,165p c4a7308a3a86b5f7.txt | grep -v '^\\s*$'"
}
```


### [2026-10-16T05:15:58.212Z] TOOL RESULT

```
 See also: ريش , رئس , and ریس 
 Kashmiri
 [ edit ] 
 Etymology
 [ edit ] 
 Borrowed from Classical Persian ریش ( rīš ) .
 Pronunciation
 [ edit ] 
 IPA ( key ) : [reːʃ] 
 Noun
 [ edit ] 
 ریش • ( rēś )  m ( Devanagari रेश ) 
 beard 
 Synonym: دٲر ( dạ̄r ) 
 Derived terms
 [ edit ] 
 ریشَل ( rēśal ) 
 References
 [ edit ] 
 S. K. Toshakhani; J. Lal Kaul; Mohiuddin Hajni ; Prithvi Nath Pushp; Akhtar Mohiuddin ( 1968-1980 ), Kashir Dictionary Vol 3 ‎ [1] (in Kashmiri), volume 3, Jammu and Kashmir Academy of Art, Culture and Languages , page 377 
 Ottoman Turkish
 [ edit ] 
 Etymology 1
 [ edit ] 
 Borrowed from Persian ریش ( riš , “ beard ” ) .
 Noun
 [ edit ] 
 ریش • ( riş ) 
 beard , facial hair on the chin , cheeks , jaw and neck 
 Synonym: صقال ( sakal ) 
 Etymology 2
 [ edit ] 
 Borrowed from Persian ریش ( riš , “ wound ” ) .
 Noun
 [ edit ] 
 ریش • ( riş ) 
 wound , sore 
 [ edit ] 
 Etymology tree
 Proto-Indo-European *wréh₂ds 
 Avestan 𐬭𐬀𐬉𐬱𐬀 ( raēša ) bor. 
 Middle Persian lyšk' 
 Persian ریشه 
 Inherited from Middle Persian [Book Pahlavi needed] ( lyšk' /⁠rēšag⁠/ ) , borrowed from Avestan 𐬭𐬀𐬉𐬱𐬀 ( raēša ) , ultimately from Proto-Indo-European *wréh₂ds ( “ root ” ) .
 Cognate with Baluchi ریشَگ ( rīšag , “ root ” ) 
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /reː.ˈʃa/ 
 ( Dari, formal ) IPA ( key ) : [reː.ʃá] 
 ( Dari, formal ) IPA ( key ) : [reː.ʃá] 
 ( Kabuli ) IPA ( key ) : [reː.ʃá] 
 ( Hazaragi ) IPA ( key ) : [reː.ʃá] 
 ( Iran, formal ) IPA ( key ) : [ɹiː.ʃé] 
 Etymology
 [ edit ] 
 Uncertain; could be a loan from a non-Indo-European language. [ 1 ] 
 Noun
 [ edit ] 
 līcium   n ( genitive līciī or līcī ) ; second declension 
 loop in the texture woven , through which the basic fabric is pulled
 thrum , leash 
 thread
```


## [2026-10-16T05:16:04.097Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'licium' POK_full.txt LEW_1910.txt LAT.txt WLD_band3.txt | head; grep -n -i -E 'urvan' SYN.txt | head -5; grep -n -E 'BEARD' SYN.txt | head -3; grep -n -i -E 'r[eē]š|resh' SYN.txt | head -5"
}
```


### [2026-10-16T05:16:04.451Z] TOOL RESULT

```
LAT.txt:4582:M.L.581 aquiducium; aquilex, -icis m.: sourcier; aquilicium,-i (aquae-
LAT.txt:4583:licium): sacrifice pour obtenir de la pluie; aquae manale (aquiminale,
LAT.txt:11829:cilicium, -I n.: 4 toffe grossibre en poil de chbvrej cilice. Ainai
LAT.txt:25809:gentiles, se revble par la conaunautd du noa, gentilicium nomen qui
LAT.txt:27427:D^riv^s: allecatus (Apicius); (h)al(l)eculay allicium.
LAT.txt:30420:licium Schrijnen, p.703 et suiv.
LAT.txt:32787:pones, exi stent aussi le non d’agent -lex, et le nom d’action - licium.
LAT.txt:32798:dabo) et delicium "seduction, perversion", cf. Plaute, M0.15 tu urbanus
LAT.txt:32811:cf. pias haut; inliciun, illicium’ appat, siduCtion, dans la 1. da
LAT.txt:32824:On considfere giniralement aquae licium comme sans rapport avec
2082:8. Av. atar-, NPers. ddar ‘fire’, Av. abravan-, abaurvan-, Skt. atharvan- ‘fire- priest’, root connection? Walde-P. 1.42.
17034:2. Lat. fervére, also fervere (> Sp. hervir, Rum. fierbe), Ir. berbaim, NIr. beirbhim, W. berwi, Br. birvi, also NIr. bruithim : Skt. bhurvani- ‘wild, restless’, Russ. bruja ‘streaming, current’, OHG briuwan, etc. ‘brew’, IE *bheru-. Walde-P. 2.167f. Ernout-M. 352f. Walde-H. 1.437.
17082:Br. bera ‘flow’ beside W. beru ‘drip’, prob. fr. *bher-in Ir. topur ‘spring, well’, Skt. bhur- ‘quiver’, bhurvan- ‘surging, etc. (Walde-P. 2.157f., without the
24378:Ay. zrvan-, cf. MPers. zarman ‘age, time’, prob. : Av. zaurvan- ‘old age, weakness of age’, Skt. jarant- ‘old, frail’,
24651:W. buan, cyflym, chwyrn, ras(ch), spoedig Av. dsu-, aurvant-, Owa- clau OHG  sniumi, (h)rad, snel, §a-, xSviwra-
5411:BOD or THE ARTS 4.142 BEARD Goth ote Lith. barzda everds e Lett. barda Grk. ete Tpeia oN ee ChSl. brada cq yevets Dan. g N barba Sw. skagg SCr. brada Ha barba OE beard Bee wre (brada) s barbe ME berd ol. roda oe barba NE beard Russ. boroda ia barbd Du. baard Skt. ¢macru- jr. —- e800 OHG bart AVn in gaat Nir. 7€a509 MHG bart W. we NHG bart Br. arv
823:Goth. land, etc., general Gme. : Ir. wh-land ‘threshing floor’ (epd. of ith ‘grain’), W. llan ‘inclosure, yard’, etc. Its earliest use was sense e, and in Goth- ic it is only so used, namely for ‘piece of land’ or ‘country’, airpa being used in all other senses, including ‘land’ in con- trast tosea. Walde-P. 2.438. Feist 321 f.
836:(also Hom. ovdés, Att. d5¢s ‘threshold’), perh. *wed- in Arm. getin ‘ground’. Walde-P. 1.254.
1086:OE denu, ME dene (NE dean, dene, -den, dial. or in local names; NED s.v. dean?.) : OK denn ‘den, lair’, OHG tenni ‘threshing floor’, Lith. denis ‘deck’, Grk. Gévap ‘palm of the hand’, ‘sole of the foot’, all having in common the notion of flat surface. Walde-P. 1.853.
1240:NG vepé fr. veapov (tdwp) ‘fresh water’, through vypdv (cf. Phrynichus vypdv dep ui) elrgs), with regular change of ir to er (Hatzidakis, Mec. 2.598).
1250:‘Sea’ is understood here as covering the most general terms applied to large bodies of water and used in such a phrase as ‘by land and sea’. But between ‘sea’ and ‘lake’ there is no rigid demarcation (either by size, or as salt vs. fresh water), and the same word or related group may serve for either or both, or shift its pre- vailing application with changed physi- cal conditions. This is notably the case in the Gmc. languages, with the diver- gent distribution of the groups repre- sented by NE sea and NHG meer.
```


## [2026-10-16T05:16:09.254Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 30405,30422p LAT.txt; echo ====; sed -n 5411,5440p SYN.txt | grep -n -i -E 'NPers|Av\\.|ri[sš]' ; echo ===; awk 'BEGIN{RS=\"\\f\"} NR==1113' SYN.txt | grep -n -i -E 'urvan|ravan|SOUL|NPers' | head"
}
```


### [2026-10-16T05:16:09.575Z] TOOL RESULT

```
Exit code 1
diligenrter uetera quaeque quasi in nouam speciem nutant. Plautus
Amphitryone (317):
illic homo me interpolabit meumque os finget denuo.
Non.34,1. Terme technique de la 1 . des foulons qui correspond pour
le sens au gr. e7U,yva7t'r(jo; il y a un adj .interpolus .(interpolis ) glos 4
e 7 H,yvacpoC et qui signifie "retape, remis a neuf": Si uest imenta inter¬
pola quis pro nouis emerit, Dig.18,1,43; (discernere) uestem interpolem
a sincera, Fronton, p. 161,3 N. De la "falsifier" et "falsifier en
introduisant dans un texte, interpoler" ( cf. Cic. Verr. 3,1,158).
Interpolo est-il le denominatif de interpolus, ou -polo est-il
a polio, comme duco,-as a. duco,-is? Dans ce cas, interpolus serait
reforme sur interpolo, comme inuidus sur inuideo. Les d 4 rives tardifs
de interpolo, interpolator,-tio, etc., n'ont que le sens figure. - An-
cien, usuel. Non roman.
Sur le rapport entre polio et interpolo, v. Vendryes, Donum nata¬
licium Schrijnen, p.703 et suiv.
interpres, -etis m. et f.: intermediaire, courtier, charge d'af-intersum
“ 573
(eval):1: === not found
```


## [2026-10-16T05:16:13.804Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^l[iīïl1]c[iī]um' LAT.txt LEW_1910.txt | head; grep -n -E 'l[īï]cium' LEW_1910.txt LAT.txt POK_full.txt | head; sed -n 5411,5460p SYN.txt | grep -n -i -E 'Pers|riš|ris' | head"
}
```


### [2026-10-16T05:16:14.143Z] TOOL RESULT

```
LAT.txt:4583:licium): sacrifice pour obtenir de la pluie; aquae manale (aquiminale,
LAT.txt:30420:licium Schrijnen, p.703 et suiv.
LAT.txt:33804:licium, -I n.: 1° li sse (gr. p,Cxos), cordon employ 4 dans le tissage
LAT.txt:33809:licium. Ancien (Loi des XII T.). Panroman, M.L.5030.
4:acaate with words for ‘bristle’, ‘point’, ete, Several of these are used also for mis ‘7 the Romance languages chin’, aS 10 : (REW 944) and Slavic (SCr., Boh. brada, Russ. boroda), and the inter- change between ‘beard’ and ‘chin’ is seen in several outside this group (below, 2 and 6).
6:1. IE *bhardha-, prob. fr. the same root as ON, OHG burst, OE byrst ‘bris- tle’, Skt. bhrsti- ‘point, edge’, etc. Walde-P. 2.185. Ernout-M. 103. Walde-H. 1.96. Berneker 72 f. es (> Romance forms and W.
36:Av. vohuni- (NPers. xin ‘blood’), etym.? Barth. 1434.
```


## [2026-10-16T05:16:16.816Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 33804,33812p LAT.txt; sed -n 5411,5430p SYN.txt | grep -n -i -E 'Iran|NPers|ris|reš' | head; grep -n -i -E 'NPers\\. r[iī][sš]' SYN.txt | head"
}
```


### [2026-10-16T05:16:17.141Z] TOOL RESULT

```
licium, -I n.: 1° li sse (gr. p,Cxos), cordon employ 4 dans le tissage
pour separer les fila de la chaine, de manibre a laisser passer la
navette et le fil de la trame: Vg.G. 1,385, licia telae I addere', puis
toute espbce de cordon, fil, ruban, etc., et meme "toile"; 3° sorte
de cale^on port 4 par le plaignant dans 1'enquete faite per lancem et
licium. Ancien (Loi des XII T.). Panroman, M.L.5030.
D 4 riv 4 s: liciatus "mis sur le metier", liciatorium "ensouple", llcid-
mentum "tissu", et sans doute licinium "filasse, charpie" et "meche"
(mais dans ce dernier sens, le mot semble etre une alt 4 ration de
4:acaate with words for ‘bristle’, ‘point’, ete, Several of these are used also for mis ‘7 the Romance languages chin’, aS 10 : (REW 944) and Slavic (SCr., Boh. brada, Russ. boroda), and the inter- change between ‘beard’ and ‘chin’ is seen in several outside this group (below, 2 and 6).
6:1. IE *bhardha-, prob. fr. the same root as ON, OHG burst, OE byrst ‘bris- tle’, Skt. bhrsti- ‘point, edge’, etc. Walde-P. 2.185. Ernout-M. 103. Walde-H. 1.96. Berneker 72 f. es (> Romance forms and W.
```


## [2026-10-16T05:16:19.504Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 33812,33820p LAT.txt; grep -n -E 'SOUL|SPIRIT' SYN.txt | head -5"
}
```


### [2026-10-16T05:16:19.795Z] TOOL RESULT

```
(mais dans ce dernier sens, le mot semble etre une alt 4 ration de
e l lychnium), M.L. 5018.
Licium semble etre le d 4 riv 4 d r un mot racine qui figure dans les
composta bilix "8i|ii,xoC", trilex ou trilix,-Icis (et trilicis ): k
triple fil, triplement tisse, Xpl<|ll,XOC, conservi dans les 1 . romanes
( fr. tre i 11 is), M.L. 8903, d'oii trillciarius.
A licium peut-etre faut-il encore rattacher licinnus: ouSoovapiv,
e|j,7ti,Ai,v CGL II 519,49, licinae, paxivoi, III 454,51, licinum : - uocatur
quod textura eius ligata sit in totum, Isid.19,33,97.
27531:16.11 SOUL, SPIRIT
```


## [2026-10-16T05:16:22.185Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27531,27600p SYN.txt | grep -n -i -E 'urvan|ravan|ruvan|Av\\.|NPers' | head"
}
```


### [2026-10-16T05:16:22.488Z] TOOL RESULT

```
2:yp Goth. saiwala, ahma Lith.  di%ia, dvasia pis O0H85 ™ RUE ON ond, sal(a), andi Lett.  dvésele, gars Yur ORS |. spiri- ‘Dan. sjael, aand ChSl. duSa, duchi qnima, antmus Sw.  sjal, ande SCr.  duSa, duh {us aes aD OE sdwel, gast Boh. duSe, duch anima, spirelo, Gree ME naules spirit, gost Pol. dusea, duch dime, esp “ty, animo NE soul, spirit (ghost) Russ. dua, duch alma, Co : Du. ziel, geest Skt. alman-, prana- _ suflet, oe, OHG _ séla, geist Av. urvan-, mainyu- anim, cad d MHG séle, geist ne ar d NHG .seele, geist € ? ene, spered Under ‘soul, spirit’ it is intended to | dub. (~i- with early transposition fr. n
23:Skt. heda- ‘anger, wrath’, Av. zdizdiiiq. most frightful’, fr. IE *Gheizd-, exten. sion of *§heis- in Goth. US-gaisjan ‘frighten’, Av. zaéSa- ‘horrible’, Walde- P. 1.554. Feist 531. NED sv. ghost.
31:Av. urvan-, the usual term for ‘soul, spirit’, etym.? Barth. 1537 ff. :
```


## [2026-10-16T05:16:29.885Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3650,3665p LKT.txt; grep -n -E '^اردو|اردو[ ]*\\[' MON_part1.txt | head -5; grep -n -i -E 'urdu|اردو' NAT_2005.txt | head -5; grep -n -i -E '\\bord[ui]\\b|ordu|urdu' incoming/TTS/TTS_pages.txt | head -5; grep -n -i -E '\\bur-?\\b.*(schlagen|strike)|vurmak|urmak' incoming/TTS/TTS_pages.txt LKT.txt | head"
}
```


### [2026-10-16T05:16:30.196Z] TOOL RESULT

```
'Palmblatt'.,  bes.  das  Blatt  der  Fahne Borassus  tlabellifornis,das  zum  Schreiben benutzt  wird;  hieraus  engl,  ollah,  frz. olle  Mass.'.    [Hobson-Jobson  636.
\'b\)±  Tk.  oluk: 'Kanal,  Rigole'  [fehlt  bei  Kelekian  Ka- mOs,  aber  bei  Hindoglu,  Dictionnaire Turc-FraiiQais.    Vienne  1838.   S.  86  a]; hieraus  rum.  uluc  'Falz,  Rinne'.
1593.  Mal.  öi'ang:
'Menscii'  [Pijn  19  a],  dazu  hütan,  ge- spro.'hen  ütan  'Wald,  wild'  [Pijii  232a]; örang-ütan,  also  wörtlich  'Waldmensch' [genau  dass.  wie  frz.  sauvage,  engl,  sa- vage  <^  lat.  silvaticus  sc.  homo],  ist  der Name  des  grotien  i\IenschenatTen  Simia satyrus  L.,  der  in  Sumatra  und  Borneo heimisch  ist  [die  Eingeborenen  bezeich- nen ihn  freilich  als  mias];  hieraus  engl. orang-uian  oder  kurz  orang,  ndl.  orang- oetang,  dt-ch.  Orang-Utang;  frz.  orang- oiitang,  sp.  orangutan,  pg.  ovang-otang. [MMM  37.  Devic  DEt  180.  Eguilaz  466. JAOS  XVIII,  86/89.
1594.  Tk.  ordu:
'Heerlager  und  -troß,  Schar';  hieraus angloind.  oordoo  'Urdti  oder  Hindustani- sprache'.  Ferner  bulg.  serb.  ordija 'Armee',  klruss.  russ.  orda  'Heerscharen'; engl,  horde,  ndl.  horde,  dtsch.  Horde; frz.  hoi-de  [angeblich  durch  Voltaire  ein- geführt, in  Wirklichkeit  älter],  it.  orda, sp.  horda,  ordo,  rum.  orda,  oarda,  ordie 'Heer,  Laujer'.  [Hobson-Jobson  639/640. Mikl  SlEtWb  225.  Kluge  210.  Dozy Oost  42/43.  Eguilaz  423  und  466.  Löbel EITAP  71.
1595.  Tk.  ormnn:
'Wald',  kas.-tat.  urman  'dass.';  hieraus bulg.  serb.  orman,  russ.  urman,  urema 'dass.'.
1596.  Pers.  Ormüz:
N.  pr.,  Name  einer  auf  einer  Insel  am Eingang  zum  pers.  Meerbusen  gelegenen blühenden  Handelsstadt  [bei  den  Alten (Ptolemaeus)  "ApiaouZa,  Hormozia;  vgl. auch  MP  99/104  und  504  sowie  v. Oppen- heim, Vom  Miltelmeer  zum  pers.  Golf II,  320  und  336];  nach  ihr  wurde  im MA  ein  satinartiger,  zu  Vorhängen, Fütterungen  usw.  dienender  Seidenstoff benannt:  it.  ormesino,  ermesino,  arme- sino,  mlat.  ermisinus  und  schließlich  frz. armoisin,  armoise,  armosin  'taftartig; dünner  Taft'  [jetzt  in  Lyon  vom  sog. armoiseur  hergestellt].  [ML  6102.  Kara- bacek.  Über  einige  Benennungen  mittel- alterlicher Gewebe.  Wien  1882.  S.  14. Anm.  61.
1597.  Tk.  orta:
'Milte;  Regiment'  [vom  Stamme  ar,  or 'zwischen,  gemeinsam,  Gesellschaft', Vämbery  TktEtWb  S.  18,  Nr.  19];  hieraus rum.  orla  'Regiment'.
1598.  Tk.  ortak:
'Kamerad,  Geführte'  [vom  gleichen Stamme  wie  Nr.  1597];  hieraus  rum. ortac  'dass.',  bulg.  serb.  ortak  'Handels- gesellschafter'.
1599.  Tk.  ota^:
Auch  ofak  'großes,  wohl  ausgestattetes Zell'  [Kelekian  Kämüs  172a;  vom  glei- chen Stamme  wie  hier  Nr.  1584];  hieraus rum.  otac  'Feldlager,  Viehhof,  poln.  otak 'Krämerbude'.  [Löbel  EITAP  71.  Mikl SlEtWb  228.
9801:اردو: ۱ [تر: مغ. ‏ اوردو] (ا.) (نظ.) 
9809:اردوگاه: .0 [تر. ف.] (امر.) محل 
9810:اردو» معسکر؛ لشکر گاه. 
25860:اردوگاه و فرستادن کمک خرج برای سر باز 
58642:اردوگاه؛ لشکرگاه. قبله ) طایفه؛ ج. اخبال» 
97:Chinese English Hindustani (the spoken form of Hindi and Urdu) Russian Spanish Japanese German Indonesian Portuguese French Arabic Bengali Malay Italian
129:Before India’s independence, Urdu and Hindi, now the chief languages of Pakistan and India respectively, were considered so similar that they were both referred to as Hindustani. The principal difference between them is that Hindi is written in the Sanskritic script Devanagari (‘writing of the gods’), and Urdu is written in Arabic script, the language of the Koran, the holy book of Islam. Hindi is more influenced by the ancient Sanskrit; Urdu contains many Turkish, Arabic, Persian, and Pushtu words dating from the time of Akbar, the great Mogul emperor of India. Akbar noticed that his army had adopted words used by different troop contingents to basic Hindustani so that the warriors could understand commands and each other, and decided to make this “‘army”’ language an official one. In fact he called the language Urdu, meaning ‘‘army.”’ The word “Urdu’”’ is linguistically related to our English word “horde,” indicating a wild and motley group—not necessarily an army.
423:Urdu: Mujge tumae mahabbat hai
610:In deference to some of the larger language groups, Indian rupee bills contain identification in India’s principal languages, including Hindi, English, Urdu, Bengali, Tamil, Gujerati, Marathi, Telegu, Bihari, Punjabi, Rajasthani, Kanarese, and Malayalam.
1070:GO! STOP! English Gee-up! Whoa! French Hue! Oh!Oh! Italian Arri! Fermo! Spanish jArre! jSo! German Hit! Brr! Russian T-t-t-t! Tproo! Hungarian Eloére! Hoh! Arabic Skee! Khef! Urdu Chull beta! Bus!
incoming/TTS/TTS_pages.txt:2234:       hurmak = fehlen.
incoming/TTS/TTS_pages.txt:3253:osni.   esmeTc   = wehen   ;     islemek       = pfeifen   ;       islih   — Pfeife        ;       osurmak,
incoming/TTS/TTS_pages.txt:3712:       olthan = Gott (der Verstehende, der Wissende) ohiurmak =                     ;
incoming/TTS/TTS_pages.txt:3977:cag. bolniah, olturmak (wie oben).
incoming/TTS/TTS_pages.txt:3994:       deutet. Im Osttürkischen heisst stehen ajali üere turmakl
incoming/TTS/TTS_pages.txt:5019:       malc, kovurmak=^&uih.ehen, erheben; ^ovanmak = sich er-
incoming/TTS/TTS_pages.txt:5036:                    Teaburmak                     ;
incoming/TTS/TTS_pages.txt:5543:osm. Ifavurmah (Ji:agurmak)                     ~ rösten     ,   sengen   ;   Ikiavurulmah   =
incoming/TTS/TTS_pages.txt:5734:osm. ^ajitnaJc,                kavusmak               (wie oben);         J{:avu8turmak :=^ ühexnin-
incoming/TTS/TTS_pages.txt:6240:           dörrt; Ä*«<?'ma7<;=hart werden; Jfatirmak, katurmak=^'ha,vi
```


## [2026-10-16T05:16:33.174Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 9801,9808p MON_part1.txt; grep -n -E 'NR?\\b' /dev/null; awk 'BEGIN{RS=\"\\f\"} /Urdu/ && /army/ {print NR-1}' NAT_2005.txt; grep -n -i -E 'ordu|orda' incoming/TTS/TTS_pages.txt | head"
}
```


### [2026-10-16T05:16:33.693Z] TOOL RESULT

```
اردو: ۱ [تر: مغ. ‏ اوردو] (ا.) (نظ.) 
مجمو عم سیاهیان ۳ تمام لوازم که به جانبی 
کر دارند» مجموغ قشون و لوازم او در 
سفر. . لشکرگاه» اردو گاه. (ور.) محلی که 
ورزشکاران یا پیشاهنگان برای تمرین یا 
تفریح گرد آیند. زبان معمولی در پا کستان و 
بخشی از هندوستان. 

29
30
8519:CUV.   sJorda^KeTze; sJot'im-bos = MorgenTÖthe.
8563:       tiordah    = zoYn\%; urutta^^?,ie\i erhitzen; urun =^\iell, klar,
```


## [2026-10-16T05:16:37.939Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://www.nisanyansozluk.com/kelime/ordu' --note 'page 521: Turkish ordu etymology' | tail -1; f=$(tail -1 data/verification/sources/web/index.jsonl | python3 -c \"import sys,json;d=json.loads(sys.stdin.read());print(d['file'],d['status'],d['bytes'])\"); echo $f"
}
```


### [2026-10-16T05:16:39.235Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5d79c352bf98b40a.txt
data/verification/sources/web/5d79c352bf98b40a.txt 200 219
```


## [2026-10-16T05:16:44.890Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/521.jpg 2>/dev/null; pdftoppm -f 521 -l 521 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg521 && echo ok"
}
```


### [2026-10-16T05:16:45.789Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   65k sfmqrb 14 Oct 22:15  site/pages/521.jpg
ok
```


## [2026-10-16T05:16:48.057Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg521.png"
}
```


### [2026-10-16T05:16:48.080Z] TOOL RESULT

```

```


## [2026-10-16T05:16:56.895Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; mkdir -p ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg521.png ocr/BOOK/521.png; awk 'BEGIN{RS=\"\\f\"} {n=split($0,a,\"\\n\"); c+=n-1; if(!h1 && c>=18067){print \"horde leaf\",NR-1; h1=1} if(!h2 && c>=40860){print \"urdu leaf\",NR-1; h2=1}}' KLN_1966.txt; grep -n -E '^(raeša|loik|beard)' AHD_watkins1985.txt | head; grep -n -i 'horde' AHD_watkins1985.txt | head -3"
}
```


### [2026-10-16T05:16:57.642Z] TOOL RESULT

```
horde leaf 400
urdu leaf 890
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
```


## [2026-10-16T05:17:04.323Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '\\b640\\b|r[eē][sš] .Bart|ravän|ravan|ruvan' HUB.txt | head; grep -n -i -E 'licium|loik|u̯loik' incoming/WLD/WLD_Bd2_pages.txt incoming/WLD/WLD_Bd1_pages.txt | head -5; grep -n -E 'ریش|ریشه' incoming/ARY/ARY_pages.txt | head -5; grep -n -E 'روان' incoming/ARY/ARY_pages.txt | head -3"
}
```


### [2026-10-16T05:17:04.764Z] TOOL RESULT

```
2377:640. Da zd. ra^a-, wie jetzt allgemein angenommen wird,
2426:phi. zruvan Gl. and Ind. 148, arm. LW. Zruan (=
2430:(d. i. zruvan-) *Zeit*. Np. zaman ist nicht aus zarman
3018:LW. karavan 'Earavane, Heerhaufen (bei Elise, Fau-
3019:stus etc.) im Phi. karavan oder karuran (geschrieben
5823:d^ *Damon H. 598; dtcar^ dXval *Mauer H. 599; ravan
5888:1894, 430) = phi. ruvan^ zd. urvan-.
5956:Jiinger ist ranam 'treibe aus *ravanam^ cans, zu ravam
6431:banda- ; paravand Fessel* u. s. w. ; mnvar *Sanfte', ap.*j'awi-
7362:= zd. yaozdad^ra- H. p. 301, asruk = zd. Hdravan- H.
incoming/WLD/WLD_Bd2_pages.txt:42916:stipum dblicium vel contra positum CGrlL. YII 9 nnd stipa ^^Strebe zur
incoming/WLD/WLD_Bd1_pages.txt:14593:94 L, licium „Eintragsfaden beim Weben, uberhaupt jeder Faden des Ge-
14:هدف این کتاب نشان دادن ریشه‌ی هند و اروپایی واژه‌های فارسی ناب است. این هدف موجب
17:۱- هیچ واژه‌ی فارسی که ریشه‌ی هند و اروپایی آن ناشناخته است آورده نشده است. صدها
18:واژه‌ی فارسی وجود دارد که ریشه‌پابی آنها تا حد پهلوی و اوستایی و حتی پارسی‌باستان پیگیری
19:شده است ولی ریشه‌ی هند و اروپایی آنها شناخته نیست. ممکن است برخی از آنها هند و اروپایی و
24:۰ ۳-هرجاکه توانسته‌ام واژه‌های همریشه‌ی کردی و بلوچی و افغانی و اوستی و سغدی و ختنی را
3569:روانی (/(44/4(): آل8۸ ,۲8165 9 (۲83) :0/05 ۱
4979:معنی اين واژه در زبان‌های ژرمنی: تبر زیر شیروانی؛ دیرکك.
```


## [2026-10-16T05:17:07.470Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2377,2385p HUB.txt; sed -n 5885,5889p HUB.txt; sed -n 14588,14600p incoming/WLD/WLD_Bd1_pages.txt; awk 'BEGIN{RS=\"\\f\"} {n=split($0,a,\"\\n\"); c+=n-1; if(c>=14593){print \"WLD leaf\",NR; exit}}' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-10-16T05:17:07.762Z] TOOL RESULT

```
640. Da zd. ra^a-, wie jetzt allgemein angenommen wird,
nicht *Bart* heisst (sondern etwa *Spalt' Riss?), so
bleibt die Etymologie dunkel. Nach den LW. bal. rfi,
afgh. ris *Bart' sowie nach echt afgh. ^Ira aus rJia
zu urtheilen, scheint ris die urspr. np. Form, rtso^ die
iranische gewesen zu sein.
642. Np. reg *Sand' = bal. rek = ap. ^rdika- gehOrt gewiss
nicht zu skr. sikata-. Die Form rez in der Bedeutung
*Sand' (Shukovski, Materialy I, p. 137) finde ich bei
arabisch QubaJ = phi. Kavdt^ zd. kavata- noben np. Kavad
(bei Hamza etc. Noldeke, Tab. 135), syr. Qavad, arm.
Kavat Einmal raban (oder ruban) fiir ravdn 'Seele* (JRAS.
1894, 430) = phi. ruvan^ zd. urvan-.
*) Die Nebenform np. bar, arm. LW. bar in bdrapan u. 8. w?




(reicht kaum aus, urn den ausl. Gutt als 5 “ sieherzustellen, s Persson Beitr.
94 L, licium „Eintragsfaden beim Weben, uberhaupt jeder Faden des Ge-
webes, dieses selbst; Gurt um den Unterleib („*Querfaden“, Breal-Bailly                         11


                                                                                                                                                               11
Diet.     el.   s.   y.\     lixulae „Kringeln“' iaber lie inns                                           „mit                   krummen       Ildrnern
trotz     Persson Beitr. 151                             aus Hecinus ,             \Vz. *lek-,             bei                   der auch hy.oiqk
/.   e/oios , Itxgoi        und       ley. got. '         oi d£oi            tojv elaqcetcov yeodraiv Hes.,                                    li}'£,     Hi'
WLD leaf 168
```


## [2026-10-16T05:17:15.799Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/vurmak' --note 'page 521: Turkish vurmak/urmak strike, root Urmak' | tail -1 | xargs -I{} sh -c \"grep -n -A2 -E '^\\s*(From|Inherited)' {} | head -8\""
}
```


### [2026-10-16T05:17:16.626Z] TOOL RESULT

```
157: From Wiktionary, the free dictionary
158-
159- Turkish
--
170: Inherited from Ottoman Turkish اورمق ( urmak, vurmak ) , from Old Anatolian Turkish اورمق ( urmaq ) , from Proto-Turkic *ur- . Cognate with Azerbaijani vurmaq , Old Turkic 𐰆𐰺 ( ur- ) , Kyrgyz уруу ( uruu ) , Uzbek urmak , Gagauz urmaa , Turkmen urmak .
171-
172- Pronunciation
```


## [2026-10-16T05:17:19.566Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' 8d8d52970b5e5982.txt | sed -n 1,40p | cut -c1-200"
}
```


### [2026-10-16T05:17:19.848Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/urvan
FETCHED: 2026-10-16T05:15:39Z
STATUS: 200
TITLE: urvan - Wiktionary, the free dictionary
urvan - Wiktionary, the free dictionary 
 Jump to content 
 Main menu 
 Main menu
 move to sidebar 
 hide 
 Navigation
 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 
 Search 
 Search 
 Appearance 
 Donations 
 Create account 
 Log in 
 Personal tools 
 Donations 
 Create account 
 Log in 
 Contents
 move to sidebar 
 hide 
 Beginning
 1 
 English 
 Toggle English subsection 
 1.1 
 Noun 
 1.2
```


## [2026-10-16T05:19:43.836Z] TOOL CALL #49: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-521.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nHORDE=W+\"horde\"; URDU=W+\"Urdu\"; ORDU=W+\"ordu\"; ORDU_FA=W+\"اردو\"; PT=W+\"Reconstruction:Proto-Turkic/ordu\"; VUR=W+\"vurmak\"\nRISH=W+\"ریش\"; RISHE=W+\"ریشه\"; RAVAN=W+\"روان\"; LIC=W+\"licium\"\nKLN_H={\"src\":\"KLN\",\"where\":\"1966 s.v. horde (KLN_1966.txt line 18067, leaf 400)\",\"stance\":\"supports\",\"note\":\"'horde ... F., fr. Turk. ordu, 'camp, army', fr. Tatar urdu, 'camp' (lit. 'something pitched up'), fr. urmak, 'to strike'. Cp. Urdu.' - the source of Nourai's whole chart.\"}\nKLN_U={\"src\":\"KLN\",\"where\":\"1966 s.v. Urdu (KLN_1966.txt line 40860, leaf 890)\",\"stance\":\"supports\",\"note\":\"'Urdu, n., Hindustani. - Hind. urdū, fr. Pers. Urdu, 'camp', which is cogn. with Turk. ordu, 'horde' (see horde); used in the sense of zabān-i-urdū, '(language of) the camp'.'\"}\nLKT={\"src\":\"LKT\",\"where\":\"no. 1594 (LKT.txt line 3654)\",\"stance\":\"supports\",\"note\":\"'1594. Tk. ordu: 'Heerlager und -troß, Schar'; hieraus angloind. oordoo 'Urdu oder Hindustanisprache'. Ferner ... russ. orda ...; engl. horde ... dtsch. Horde; frz. horde [angeblich durch Voltaire eingeführt, in Wirklichkeit älter]' - no etymon of ordu given, no urmak.\"}\nHJB={\"src\":\"HJB\",\"where\":\"s.v. OORDOO (HJB.txt line 15929)\",\"stance\":\"supports\",\"note\":\"'The (Turki) word urdu means properly the camp of a Tartar Khan, and is, in another direction, the original of our word horde (Russian orda) ... The word urdu, in the sense of a royal camp, came into India probably with Baber ... zabān-i-urdū, 'the Camp Language', and hence we have elliptically Urdu.'\"}\nMON={\"src\":\"MON\",\"where\":\"2-vol abridgement s.v. اردو (MON_part1.txt line 9801)\",\"stance\":\"supports\",\"note\":\"'اردو: [تر.-مغ. اوردو] ... مجموعهٔ سپاهیان ... لشکرگاه، اردوگاه ... زبان معمولی در پاکستان و بخشی از هندوستان' - Turkic-Mongolian origin, camp/army, and the language of Pakistan.\"}\nTTS={\"src\":\"TTS\",\"where\":\"TTS_pages.txt grep 'ordu|urdu|urmak'\",\"stance\":\"silent\",\"note\":\"no usable entry for ordu or ur- 'strike' found in the OCR.\"}\n\nentries=[]\n# ---------- entry 0\ne0={\"entry\":0,\"root\":\"Urmak\",\"verdict\":\"disputed\",\n\"modern_form\":\"Turkic *ur- 'to strike' (Old Turkic ur-, Turkish vurmak/urmak) is real, but Proto-Turkic *ordu 'royal camp, palace; army' is not derived from it (etymology uncertain; Mongolic ordu/ordo is a loan from or into Turkic).\",\n\"note\":\"The chart copies Klein s.v. horde ('fr. Tatar urdu, camp (lit. something pitched up), fr. urmak, to strike'). Two problems: (1) urmak is a Turkic verb (Ottoman/Old Anatolian Turkish urmaq, Turkish vurmak < Proto-Turkic *ur-), not Mongolian; (2) modern Turkology does not derive *ordu from *ur- 'strike': Wiktionary's Proto-Turkic *ordu calls the etymology uncertain, 'usually considered simplex', mentions EDAL's hypothetical *or- (cf. *orun 'place', *ortu 'middle') and Dybo's view that it may be a Mongolic loan; the vowel o- vs u- also speaks against ur-. In the printed book, 'Urmak: to strike' and 'Urdu: camp of strikers, army camp' share one Mongolian root box (the JSON split Urdu into node #1). Gloss 'to strike' is right for the verb, but the root as an etymon of ordu/horde/Urdu is rejected.\",\n\"note_fa\":\"نورایی به پیروی از کلاین، «اردو» و «horde» را از فعل urmak «زدن» می‌گیرد و آن را مغولی می‌نامد. urmak در واقع فعلی ترکی است (ترکی عثمانی urmak/vurmak، ترکی باستان ur- «زدن») و مغولی نیست؛ و پژوهش امروزی واژهٔ ترکی آغازین *ordu «اردوی شاهی، کاخ، لشکرگاه» را از این فعل نمی‌داند: ریشهٔ آن ناروشن است و برخی (دیبو) آن را وام‌واژه‌ای مغولی می‌دانند. پس این ریشه‌سازی پذیرفتنی نیست، هرچند پیوند «اردو» با horde و Urdu درست است.\",\n\"sources\":[PT,VUR,HORDE],\n\"ref_check\":[{\"ref\":\"KLN:742\",\"status\":\"supports\",\"note\":\"KLN_1966.txt line 18067 (leaf 400) s.v. horde: 'fr. Tatar urdu, 'camp' (lit. 'something pitched up'), fr. urmak, 'to strike''. Klein does say it - but he says Tatar, not Mongolian, and his derivation is not followed by modern sources.\"}],\n\"consulted\":[KLN_H,LKT,HJB,MON,TTS],\n\"nodes\":[]}\ne0[\"nodes\"].append({\"id\":1,\"lang\":\"Mongolian\",\"words\":\"Urdu\",\"verdict\":\"plausible\",\n\"derivation\":\"In the printed chart 'Urdu: camp of strikers, army camp' stands in the same Mongolian root box as 'Urmak' (the JSON made it a separate node). A Mongolic word does exist - Middle/Classical Mongolian ordu/ordo 'palace-tent, court, camp of a khan' (modern Mongolian ord) - and Mongol rule spread it (Golden Horde, Il-khanid Persia), but it is either a loan from Turkic *ordu or (Dybo) the source of it; the form 'urdu' is Klein's Tatar form (Tatar urda), and the gloss 'camp of strikers' rests only on the rejected link with urmak 'strike'.\",\n\"derivation_fa\":\"در کتاب «Urdu: اردوگاهِ زنندگان، لشکرگاه» در همان خانهٔ ریشه کنار Urmak آمده است. در مغولی میانه و کلاسیک واژهٔ ordu/ordo «خیمهٔ شاهی، اردوی خان» هست و با فرمانروایی مغولان (اردوی زرین، ایلخانان) پراکنده شد، اما یا وام از ترکی *ordu است یا به گفتهٔ دیبو سرچشمهٔ آن. معنای «اردوی زنندگان» تنها بر پیوند نادرست با urmak «زدن» استوار است؛ بنابراین واژه پذیرفتنی است ولی توضیح معنایی آن نه.\",\n\"sources\":[PT,HORDE],\n\"ref_check\":[{\"ref\":\"KLN:742\",\"status\":\"partial\",\"note\":\"KLN_1966.txt line 18067: 'fr. Tatar urdu, 'camp' (lit. 'something pitched up')' - Klein calls the form Tatar, not Mongolian, and glosses 'something pitched up', not 'camp of strikers'.\"}],\n\"consulted\":[KLN_H,MON,HJB]})\ne0[\"nodes\"].append({\"id\":2,\"lang\":\"Turkish\",\"words\":\"ordu\",\"verdict\":\"plausible\",\n\"derivation\":\"Turkish ordu 'army; camp' is inherited from Ottoman Turkish اردو ordu, Old Turkic ordu 'royal camp, palace, residence of the khagan' (Orkhon-era), Proto-Turkic *ordu. The word and meaning are right; what is not accepted is the arrow from 'urmak, to strike': *ordu has no agreed etymology (Wiktionary s.v. Proto-Turkic *ordu: 'uncertain, usually considered simplex').\",\n\"derivation_fa\":\"ترکی ordu «لشکر، اردوگاه» از ترکی عثمانی اردو و ترکی باستان ordu «اردوی شاهی، کاخ خاقان» و ترکی آغازین *ordu آمده است. واژه و معنا درست است، اما پیوند آن با urmak «زدن» را پژوهش امروزی نمی‌پذیرد و ریشهٔ *ordu را ناروشن می‌داند.\",\n\"sources\":[ORDU,PT],\n\"ref_check\":[{\"ref\":\"KLN:742\",\"status\":\"supports\",\"note\":\"KLN_1966.txt line 18067: 'Turk. ordu, 'camp, army', fr. Tatar urdu'.\"},{\"ref\":\"KLN:1861\",\"status\":\"not_found\",\"note\":\"Klein's 1966 two-volume pagination ends at p.1776; p.1861 does not exist - probably Nourai's slip for 1681 (Urdu).\"}],\n\"consulted\":[LKT,KLN_H,TTS]})\ne0[\"nodes\"].append({\"id\":3,\"lang\":\"Persian\",\"words\":\"ordŭ\",\"verdict\":\"confirmed\",\n\"derivation\":\"Persian اردو ordu/urdu 'army, army camp' is a Turkic loan of the Mongol and Timurid period (Mo'in: [تر.-مغ.]), from Turkic ordu 'royal camp'; derivatives اردوگاه 'camp', اردوکشی 'military expedition', اردوبیگ 'camp commander' are Persian formations. In Mughal India (from Babur) the royal camp at Delhi was urdū-yi muʿallā and its mixed speech zabān-i urdū 'language of the camp', whence the language name - Nourai's gloss on the Hindi-Persian-Turkish-Arabic camp language reflects this tradition (Natel-Khanlari/NAT p.14 likewise).\",\n\"derivation_fa\":\"«اردو» در فارسی وام‌واژه‌ای ترکی (به گفتهٔ معین ترکی-مغولی) از دورهٔ مغول و تیموری است به معنای «لشکر، لشکرگاه»؛ «اردوگاه»، «اردوکشی» و «اردوبیگ» ساخته‌های فارسی از آن‌اند. در هند گورکانی اردوی شاهی دهلی را «اردوی معلی» و زبان آمیختهٔ آن را «زبانِ اردو» می‌گفتند که نام زبان اردو از آن است. ادعای نورایی درست است.\",\n\"sources\":[ORDU_FA,URDU],\n\"ref_check\":[{\"ref\":\"MON:197\",\"status\":\"supports\",\"note\":\"Checked in the 2-vol abridgement (different pagination), MON_part1.txt line 9801: 'اردو: [تر.-مغ. اوردو] ... لشکرگاه، اردوگاه ... زبان معمولی در پاکستان و بخشی از هندوستان'.\"},{\"ref\":\"NAT:14\",\"status\":\"supports\",\"note\":\"NAT_2005.txt leaf 29 (= p.14): 'Akbar noticed that his army had adopted words used by different troop contingents ... he called the language Urdu, meaning 'army.' The word Urdu is linguistically related to our English word horde'.\"},{\"ref\":\"KLN:1861\",\"status\":\"not_found\",\"note\":\"page beyond the end of Klein 1966 (p.1776); the Urdu entry is at line 40860.\"}],\n\"consulted\":[MON,HJB,LKT]})\ne0[\"nodes\"].append({\"id\":4,\"lang\":\"Hindustani\",\"words\":\"urdu\",\"verdict\":\"confirmed\",\n\"derivation\":\"Hindustani/Urdu اُردو urdū (Hindi उर्दू) 'the Urdu language' is elliptical for Persian zabān-i urdū(-yi muʿallā) 'language of the (exalted) camp', the Persianised Hindustani of the Mughal court and army at Delhi; the word urdu came to India with Babur's Timurid army (Hobson-Jobson s.v. Oordoo).\",\n\"derivation_fa\":\"اردو (زبان) در هندوستانی کوتاه‌شدهٔ «زبانِ اردوی معلی» است، یعنی زبان هندوستانیِ آمیخته با فارسی در دربار و لشکر گورکانیان دهلی؛ واژهٔ اردو با لشکر بابر به هند رسید. درست است.\",\n\"sources\":[URDU],\n\"ref_check\":[{\"ref\":\"KLN:1681\",\"status\":\"supports\",\"note\":\"KLN_1966.txt line 40860 s.v. Urdu: 'Hind. urdū, fr. Pers. Urdu, 'camp' ... used in the sense of zabān-i-urdū, '(language of) the camp''.\"}],\n\"consulted\":[HJB,KLN_U,LKT]})\ne0[\"nodes\"].append({\"id\":5,\"lang\":\"English\",\"words\":\"Urdu\",\"verdict\":\"confirmed\",\n\"derivation\":\"English Urdu (earlier Oordoo, 18th c. Anglo-Indian) is borrowed from Hindustani urdū, from Persian urdū 'camp', from Turkic ordu; it is a doublet of horde (Wiktionary s.v. Urdu).\",\n\"derivation_fa\":\"انگلیسی Urdu (در انگلیسیِ هندی کهن Oordoo) از هندوستانی urdū و آن از فارسی «اردو» و ترکی ordu گرفته شده و با horde دوگانه است. درست است.\",\n\"sources\":[URDU],\n\"ref_check\":[{\"ref\":\"KLN:1681\",\"status\":\"supports\",\"note\":\"KLN_1966.txt line 40860: 'Urdu ... Hind. urdū, fr. Pers. Urdu, 'camp', which is cogn. with Turk. ordu, 'horde''.\"}],\n\"consulted\":[KLN_U,HJB,LKT]})\ne0[\"nodes\"].append({\"id\":6,\"lang\":\"French\",\"words\":\"\",\"verdict\":\"plausible\",\n\"derivation\":\"Empty pass-through French box (French horde). French horde (16th c., popularised by Voltaire per Lokotsch/Hobson-Jobson) did not come straight from Turkish: it came via German Horde < Polish horda < Russian/Ukrainian orda < Kipchak/Tatar urda 'camp of a khan' (the Golden Horde), ultimately Turkic *ordu; the chart's direct Turkic→French arrow skips the Slavic and German intermediaries.\",\n\"derivation_fa\":\"خانهٔ خالی فرانسوی (horde). فرانسوی horde مستقیم از ترکی نیامده، بلکه از آلمانی Horde و آن از لهستانی horda و روسی orda و تاتاری urda «اردوی خان» (اردوی زرین) گرفته شده که سرانجام به ترکی *ordu می‌رسد؛ نمودار نورایی حلقه‌های اسلاوی و آلمانی را انداخته است.\",\n\"sources\":[HORDE],\n\"ref_check\":[{\"ref\":\"KLN:742\",\"status\":\"partial\",\"note\":\"KLN_1966.txt line 18067: 'horde ... F., fr. Turk. ordu' - Klein also gives the shortened route; no Polish/German stage.\"},{\"ref\":\"AHD\",\"status\":\"not_checked\",\"note\":\"no page given; refers to the AHD main dictionary entry, not the IE appendix (Watkins 1985 text has no horde entry).\"}],\n\"consulted\":[LKT,HJB,KLN_H]})\ne0[\"nodes\"].append({\"id\":7,\"lang\":\"English\",\"words\":\"hoard\",\"verdict\":\"transcription_suspect\",\n\"derivation\":\"The book prints 'hoard : a wandering tribe, group, camp' - Nourai's misprint for horde (the gloss is that of horde; hoard 'treasure' is native Old English hord < Proto-Germanic *huzdą, unrelated). English horde (1555) is from Middle French horde < German Horde < Polish horda < Russian orda < Tatar/Kipchak urda, ultimately Turkic *ordu 'camp'; the extraction is faithful.\",\n\"derivation_fa\":\"کتاب «hoard» چاپ کرده که خطای چاپی کتاب به جای horde است (معنای «قبیلهٔ کوچ‌رو، گروه، اردو» از آنِ horde است؛ hoard «گنج» واژه‌ای بومی انگلیسی و بی‌پیوند است). انگلیسی horde از سال ۱۵۵۵ از فرانسوی horde، آلمانی Horde، لهستانی horda، روسی orda و تاتاری urda آمده و سرانجام به ترکی *ordu «اردو» می‌رسد. خوانش اسکن درست است.\",\n\"error_in\":\"book\",\"book_prints\":\"hoard\",\"correct_form\":\"horde\",\n\"sources\":[HORDE],\n\"ref_check\":[{\"ref\":\"AHD:634\",\"status\":\"not_checked\",\"note\":\"AHD main-dictionary page (1976), not available; the IE appendix (Watkins 1985) has no Turkic words.\"},{\"ref\":\"KLN\",\"status\":\"supports\",\"note\":\"KLN_1966.txt line 18067: 'horde, n., 1) a wandering tribe; 2) a multitude. - F., fr. Turk. ordu' - Nourai's gloss is Klein's definition of horde.\"}],\n\"consulted\":[KLN_H,LKT,HJB]})\nentries.append(e0)\n\n# ---------- entry 1\nIEC1={\"src\":\"IEC\",\"where\":\"s.v. loik- (1) (IEC.txt line 9980)\",\"stance\":\"supports\",\"note\":\"'loik- (1) 'twist, twine, wicker, matting, basketry'. Av. raeša, m. (2) 'beard'; Per. rīš (2), id.; Lat. licium 'woof, yarn'; Blg. OCS lěsa 'hurdle, frame, rack, mat'' - Nourai's chart is a copy of this entry.\"}\nHRN640={\"src\":\"HRN\",\"where\":\"no. 640, p.142 (HRN.txt leaf 163)\",\"stance\":\"partial\",\"note\":\"'640. rēš 'Bart', rēše 'Haar'; aw. raēša- zweifelhaft ... phlv. rēš 'Bart' (AV.), rēšak 'Haar' (vd. 7 (28) Gl). kurd. rīh, rī 'Bart'; afγ. žīra (aus *rīša)' - Pahlavi and Persian confirmed, the Avestan link called doubtful; no IE root.\"}\nHUB640={\"src\":\"HUB\",\"where\":\"no. 640 (HUB.txt line 2377)\",\"stance\":\"contradicts\",\"note\":\"'Da zd. raēša-, wie jetzt allgemein angenommen wird, nicht 'Bart' heisst (sondern etwa 'Spalt, Riss?'), so bleibt die Etymologie dunkel. Nach ... bal. rīš, afgh. ... sowie nach echt afgh. žīra aus *rīša zu urtheilen, scheint rīš die urspr. np. Form, *rīša die iranische gewesen zu sein.'\"}\nPHDr={\"src\":\"PHD\",\"where\":\"p.71 (PHD.txt line 559)\",\"stance\":\"supports\",\"note\":\"'rēšag [lyšk' | N rēša] root, fibre' and separately 'rēšīdan, rēš- [lyšyt'n | N ~] wound, hurt' - MacKenzie lists rēšag 'root' (no 'beard' entry captured on that line).\"}\nNYBr={\"src\":\"NYB\",\"where\":\"Glossary p.168 (NYB_vol2_glossary.txt line 3309)\",\"stance\":\"supports\",\"note\":\"'rēš [lyš] beard 267 32. - = NP' and next entry 'rēšēnītan to damage ... Den. of rēš, Av. (1486 sq.) raēša(h)- 'injury, damage'' - Nyberg ties Av. raēša- only to the 'wound' word.\"}\nBQTr={\"src\":\"BQT\",\"where\":\"vol. 2 s.v. ریش, BQT_v2_pages.txt leaf 450 (≈ p.988-993)\",\"stance\":\"partial\",\"note\":\"Mo'in's footnote (OCR, reversed): 'پهلوی rêš (لحیه)، rêšak (مو). کردی rîh (لحیه). افغانی žîra ...' for ریش 'beard', and separately for ریش 'wound': 'اوستا raêšah (جراحت)'. Mo'in gives no Avestan etymon for the beard word.\"}\nARYr={\"src\":\"ARY\",\"where\":\"ARY_pages.txt grep ریش/ریشه\",\"stance\":\"silent\",\"note\":\"only hits in the introduction; Aryanpur (who lists only words with a known IE root) has no entry for ریش 'beard' in the OCR.\"}\nPOKs={\"src\":\"POK\",\"where\":\"POK_full.txt grep 'licium', 'u̯reik', 'leik'\",\"stance\":\"silent\",\"note\":\"Pokorny has u̯reik- 'heath, heather' (p.1182) but no root grouping Iranian rēš 'beard' with Latin līcium; līcium not found.\"}\ne1={\"entry\":1,\"root\":\"Uroiks, Loik\",\"verdict\":\"disputed\",\n\"modern_form\":\"Mann's *loik- (1) 'twist, twine, wicker' (IEC) - not in Pokorny/Watkins; Persian rīš 'beard' and Latin līcium have no accepted common IE root.\",\n\"note\":\"The chart reproduces Mann IEC s.v. loik- (1) word for word (Av. raēša 'beard', Per. rīš (2), Lat. līcium). Mann's isolated equation is not accepted elsewhere: Pokorny and Watkins have no such root, the 'beard' meaning of Avestan raēša- was already rejected by Hübschmann (no. 640: raēša- means 'injury, split', so 'the etymology remains dark') and Horn (no. 640 'aw. raēša- zweifelhaft'), and Latin līcium is of uncertain origin (Ernout-Meillet: perhaps from a root noun seen in bilix/trilix; de Vaan via Wiktionary: possibly non-IE). The first form 'Uroiks' looks like Mann's *u̯roik- (heather) confused with loik-. Persian rēšag/rīša 'root' is moreover usually compared with PIE *wréh₂d- 'root' (Wiktionary), not with 'twist'.\",\n\"note_fa\":\"این ریشه از فرهنگ مان (loik- «تابیدن، بافتن، ترکه») برداشته شده که اوستایی raēša را «ریش» و فارسی «ریش» و لاتین licium «پود» را هم‌ریشه می‌داند. پوکورنی و واتکینز چنین ریشه‌ای ندارند؛ هوبشمان و هرن نشان داده‌اند که اوستایی raēša- به معنای «زخم» است نه «ریش»، و ریشه‌شناسی «ریش» را ناروشن دانسته‌اند؛ لاتین licium نیز ریشه‌ای ناروشن دارد. پس این ریشهٔ هندواروپایی را پژوهش امروزی نمی‌پذیرد.\",\n\"sources\":[RISH,RISHE,LIC],\n\"ref_check\":[{\"ref\":\"IEC:704\",\"status\":\"supports\",\"note\":\"IEC.txt line 9980 s.v. loik- (1): 'twist, twine, wicker, matting, basketry'. Av. raeša, m. (2) 'beard'; Per. rīš (2), id.; Lat. licium 'woof, yarn'' (two printed pages per leaf; entry in the l- section, consistent with p.704).\"},{\"ref\":\"IEC:1593\",\"status\":\"not_checked\",\"note\":\"p.1593 lies in the index/addenda part of IEC; not located in the OCR.\"}],\n\"consulted\":[IEC1,POKs,{\"src\":\"WLD\",\"where\":\"Bd. I p.159 (WLD_Bd1_pages.txt line 14593, leaf 168)\",\"stance\":\"contradicts\",\"note\":\"Walde-Pokorny treat 'L. licium „Eintragsfaden beim Weben ...“' under a root *lei-k-/*lek- 'bend' (with lixulae 'mit krummen Hörnern'), not with any Iranian 'beard' word.\"},{\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt grep '^loik|^leik'\",\"stance\":\"silent\",\"note\":\"no loik- root; no Persian rīš.\"},{\"src\":\"SYN\",\"where\":\"4.142 BEARD (SYN.txt line 5411)\",\"stance\":\"silent\",\"note\":\"Buck lists IE *bhardha- etc.; no IE etymology for NPers. rīš.\"}],\n\"nodes\":[]}\ne1[\"nodes\"].append({\"id\":1,\"lang\":\"Avestan\",\"words\":\"raeša\",\"verdict\":\"disputed\",\n\"derivation\":\"Avestan raēša- exists, but it means 'injury, wound' (Bartholomae col. 1486; Nyberg: 'Av. raēša(h)- injury, damage', source of Pahlavi rēšēnītan 'to damage' and NP rīš/rēš (1) 'wound'); it is the 'wound' word ریش1, not 'beard'. The 'beard' reading was an early 19th-c. guess that Hübschmann already reported as abandoned ('wie jetzt allgemein angenommen wird, nicht Bart'); Horn calls it 'zweifelhaft'. No Avestan word for 'beard' of this shape is attested, so the arrow root→Avestan 'hair, beard' is rejected (only Mann maintains it).\",\n\"derivation_fa\":\"در اوستایی raēša- هست، اما به معنای «زخم، آسیب» است (بارتولومه، نیبرگ) و نیای «ریش ۱» (زخم) و «ریشیدن» پهلوی است، نه «ریش» به معنای محاسن. هوبشمان می‌گوید اکنون همگان پذیرفته‌اند که raēša «ریش» نیست و هرن آن را «مشکوک» می‌خواند. بنابراین این بخش نمودار را پژوهش امروزی رد می‌کند و تنها مان از آن پیروی کرده است.\",\n\"sources\":[RISH],\n\"ref_check\":[{\"ref\":\"HRN:142\",\"status\":\"contradicts\",\"note\":\"HRN.txt leaf 163 (p.142) no. 640: 'rēš 'Bart' ... aw. raēša- zweifelhaft (Horn, ZDMG 43, 33; Jackson, AJPh XI, 88)' and no. 641 'rēš 'Wunde' ... aw. raēšah- 'Wunde''.\"},{\"ref\":\"IEC:104\",\"status\":\"not_checked\",\"note\":\"p.104 is in the b- section of Mann; probably Nourai's slip for 704. The loik- entry (line 9980) does say 'Av. raeša, m. (2) beard'.\"},{\"ref\":\"IEC:1593\",\"status\":\"not_checked\",\"note\":\"not located in the OCR.\"}],\n\"consulted\":[HUB640,HRN640,NYBr,{\"src\":\"BRT\",\"where\":\"BRT.txt grep raēša/Wunde\",\"stance\":\"silent\",\"note\":\"OCR of the column too noisy to locate raēša-; Nyberg's glossary cites it as 'Av. (1486 sq.) raēša(h)- injury, damage'.\"},IEC1]})\ne1[\"nodes\"].append({\"id\":2,\"lang\":\"Pahlavi\",\"words\":\"rěš; rěšak\",\"verdict\":\"plausible\",\n\"derivation\":\"Both words are real Middle Persian: rēš [lyš] 'beard' (Nyberg Glossary; Horn: phlv. rēš 'Bart') and rēšag [lyšk'] 'root, fibre' (MacKenzie; Horn: rēšak 'Haar' in the Vendidad gloss). The Pahlavi → Persian line is correct, but the descent from Avestan raēša 'beard' is not (see #1): rēš 'beard' has no known Old Iranian antecedent (Hübschmann reconstructs only Iranian *rīša-), and rēšag 'root' is either a -ag derivative of rēš 'hair, fibre' or (Wiktionary) a separate word compared with PIE *wréh₂d- 'root'.\",\n\"derivation_fa\":\"هر دو واژه در فارسی میانه هست: rēš «ریش» (نیبرگ، هرن) و rēšag «ریشه، رشته» (مکنزی؛ در گزارش وندیداد «مو»). گذر از پهلوی به فارسی درست است، ولی پیوند آن با اوستایی raēša «ریش» نادرست است؛ برای rēš «ریش» نیای ایرانی باستان شناخته‌ای نیست، و rēšag «ریشه» یا با پسوند -ag از rēš «مو، رشته» ساخته شده یا به گفتهٔ ویکی‌واژه با ریشهٔ هندواروپایی *wréh₂d- «ریشه» سنجیده می‌شود. با احتیاط پذیرفتنی است.\",\n\"sources\":[RISHE],\n\"ref_check\":[{\"ref\":\"BQT:988\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 450, Mo'in's footnote to ریش: 'پهلوی rêš (لحیه)، rêšak (مو)'.\"},{\"ref\":\"SOD:348\",\"status\":\"supports\",\"note\":\"SOD_pages.txt line 28649, entry 8657 'rys'kk B rēše, rēšak ? <Pahl. rēš beard' (page ≈ 348).\"}],\n\"consulted\":[NYBr,PHDr,HRN640]})\ne1[\"nodes\"].append({\"id\":3,\"lang\":\"Persian\",\"words\":\"rîš 2; rîšeh\",\"verdict\":\"plausible\",\n\"derivation\":\"NP ریش rīš (classical rēš, majhūl ē > Iranian Persian ī) 'beard' < MP rēš, and ریشه rīše (classical rēša) 'root' < MP rēšag with the regular loss of final -g (-ag > -a/-e). Both forms and the Pahlavi ancestry are confirmed (Horn 640, Hübschmann 640, Mo'in); the further IE etymology through Avestan raēša and *loik- 'twist' is not accepted (Hübschmann: 'die Etymologie bleibt dunkel'). The numeral '2' separates it from ریش1 'wound' (< Av. raēša-).\",\n\"derivation_fa\":\"«ریش» (در فارسی کلاسیک rēš با یای مجهول که در فارسی ایران به ī بدل شده) از فارسی میانه rēš، و «ریشه» (کلاسیک rēša) از فارسی میانه rēšag با افتادن -g پایانی آمده است. پیوند با پهلوی را هرن، هوبشمان و معین تأیید می‌کنند، اما ریشه‌شناسی هندواروپایی از راه اوستایی raēša و *loik- «تابیدن» پذیرفته نیست و هوبشمان ریشهٔ «ریش» را ناروشن می‌داند. «ریش ۲» از «ریش ۱» به معنای «زخم» (از اوستایی raēša-) جداست.\",\n\"sources\":[RISH,RISHE],\n\"ref_check\":[{\"ref\":\"BQT:988\",\"status\":\"partial\",\"note\":\"BQT_v2_pages.txt leaf 450: footnote to ریش (beard) gives only 'پهلوی rêš ... rêšak، کردی rîh، افغانی žîra'; the Avestan raêšah is given for ریش 'wound' only.\"},{\"ref\":\"HRN:142\",\"status\":\"partial\",\"note\":\"no. 640 'rēš 'Bart', rēše 'Haar'; aw. raēša- zweifelhaft; phlv. rēš 'Bart', rēšak 'Haar''.\"},{\"ref\":\"IEC:704\",\"status\":\"supports\",\"note\":\"line 9980: 'Per. rīš (2), id.' under loik- (1).\"},{\"ref\":\"BQT:989\",\"status\":\"not_checked\",\"note\":\"next page (ریشه) not legible in the OCR.\"}],\n\"consulted\":[HUB640,HRN640,BQTr,ARYr]})\ne1[\"nodes\"].append({\"id\":4,\"lang\":\"Sogdian\",\"words\":\"ryš`kk\",\"verdict\":\"plausible\",\n\"derivation\":\"Gharib lists Buddhist Sogdian rys'kk / ryš'kk (rēše, rēšak?) 'beard', comparing Pahlavi rēš; the form is a -k(k) derivative of the same Iranian *raiša-/*rīša- as MP rēš. The Sogdian word is real, but it is a cognate of the Middle Persian word, not a descendant of Avestan raēša (which means 'wound').\",\n\"derivation_fa\":\"قریب در فرهنگ سغدی rys'kk (rēše/rēšak) «ریش» را آورده و با پهلوی rēš سنجیده است. این واژه هم‌ریشهٔ واژهٔ فارسی میانه است و از اوستایی raēša («زخم») برنیامده؛ پس واژه درست است ولی پیکان نمودار نه.\",\n\"sources\":[],\n\"ref_check\":[{\"ref\":\"SOD:348\",\"status\":\"supports\",\"note\":\"SOD_pages.txt line 28649: '8657 rys'kk B / rēše, rēšak ? <Pahl. rēš / beard / VJ 914'.\"}],\n\"consulted\":[{\"src\":\"SOD\",\"where\":\"entry 8657 (SOD_pages.txt line 28649)\",\"stance\":\"supports\",\"note\":\"'rys'kk B rēše, rēšak ? <Pahl. rēš beard'.\"},HRN640]})\ne1[\"nodes\"].append({\"id\":5,\"lang\":\"Latin\",\"words\":\"lîcium\",\"verdict\":\"disputed\",\n\"derivation\":\"Latin līcium 'leash/heddle thread in weaving, thread, yarn' (Twelve Tables; panromance) is real, but its origin is uncertain: Ernout-Meillet derive it from a root noun seen in bilix, trilix 'two-/three-threaded'; Walde-Pokorny place it under *lei-k- 'bend'; Wiktionary (after de Vaan) suggests a non-IE loan. No source but Mann connects it with Iranian rēš 'beard'.\",\n\"derivation_fa\":\"لاتین līcium «نخ ورد در بافندگی، رشته، نخ» واژه‌ای کهن است، اما ریشهٔ آن ناروشن است: ارنو و میه آن را با bilix و trilix «دولا، سه‌لا» می‌سنجند، والده-پوکورنی آن را زیر ریشهٔ *lei-k- «خم کردن» می‌آورند و ویکی‌واژه احتمال وام از زبانی ناهندواروپایی را می‌دهد. پیوند آن با «ریش» فارسی را جز مان کسی نپذیرفته است.\",\n\"sources\":[LIC],\n\"ref_check\":[{\"ref\":\"IEC:704\",\"status\":\"supports\",\"note\":\"line 9980: 'Lat. licium 'woof, yaro'' under loik- (1).\"}],\n\"consulted\":[{\"src\":\"LAT\",\"where\":\"s.v. licium (LAT.txt line 33804)\",\"stance\":\"contradicts\",\"note\":\"'licium, -i n.: lisse ... cordon employé dans le tissage ... Licium semble être le dérivé d'un mot racine qui figure dans les composés bilix, trilix' - no IE etymology, no Iranian cognate.\"},{\"src\":\"WLD\",\"where\":\"Bd. I p.159 (WLD_Bd1_pages.txt line 14593)\",\"stance\":\"contradicts\",\"note\":\"'L. licium „Eintragsfaden beim Weben ...“' under *lei-k-/lek- 'bend'.\"},POKs]})\nentries.append(e1)\n\n# ---------- entry 2\nBRTu={\"src\":\"BRT\",\"where\":\"col. 1537 ff. (cited by Buck, Nyberg and Mo'in)\",\"stance\":\"supports\",\"note\":\"BRT.txt OCR too noisy to isolate the urvan- article; Buck: 'Av. urvan-, the usual term for soul, spirit, etym.? Barth. 1537 ff.'; Mo'in's footnote 'اوستا urvan- بارتولمه ۱۵۳۷'.\"}\nNYBu={\"src\":\"NYB\",\"where\":\"Glossary s.v. ruvan (NYB_vol2_glossary.txt line 3356)\",\"stance\":\"supports\",\"note\":\"'ruvan [lwb'n] soul, the immortal part of the human being ... - Av. (1537 sqq.) urvan-; KZ ŠPrth ʾrwn; MPrth rwn ... MPrs rwn; Paz. ruā; NP ravān.'\"}\nPHDu={\"src\":\"PHD\",\"where\":\"p.71 (PHD.txt line 561)\",\"stance\":\"supports\",\"note\":\"'ruwān [lwbʾn | M rwʾn, N ~] soul. ~ig spiritual.'\"}\nSYNu={\"src\":\"SYN\",\"where\":\"16.11 SOUL, SPIRIT (SYN.txt line 27531 ff.)\",\"stance\":\"supports\",\"note\":\"'Av. urvan-, the usual term for 'soul, spirit', etym.? Barth. 1537 ff.'\"}\nHUBu={\"src\":\"HUB\",\"where\":\"p.? (HUB.txt line 5886)\",\"stance\":\"supports\",\"note\":\"'Einmal raban (oder ruban) für ravān 'Seele' (JRAS 1894, 430) = phl. ruvan, zd. urvan-.'\"}\nBQTu={\"src\":\"BQT\",\"where\":\"vol. 2 s.v. روان, BQT_v2_pages.txt leaf 427\",\"stance\":\"supports\",\"note\":\"Mo'in's footnote (OCR reversed): 'پهلوی ruvân (روح). اوستا urvan-، بارتولمه ۱۵۳۷'; text: 'روان نفس ناطقه است و از جان روح حیوانی'.\"}\ne2={\"entry\":2,\"root\":\"Urvan\",\"verdict\":\"confirmed\",\n\"modern_form\":\"Avestan urvan- (n-stem; nom. urva) 'soul, spirit' (Bartholomae 1537); Proto-Iranian *Hurwan-, further etymology uncertain.\",\n\"note\":\"Root, language and gloss are correct: Avestan urvan- is the standard Zoroastrian term for the (immortal) soul, Bartholomae col. 1537 ff.; Buck 16.11 lists it with 'etym.?'. Wiktionary (s.v. روان) mentions a tentative Proto-Iranian *urw-āna- 'what has made wide room for itself' (cf. Skt. uru-). The Sogdian NOTE is evaluated at node #3.\",\n\"note_fa\":\"اوستایی urvan- «روان، روح جاودان آدمی» واژهٔ شناخته‌شدهٔ دین زرتشتی است (بارتولمه ۱۵۳۷، باک ۱۶.۱۱). ریشهٔ هندواروپایی آن روشن نیست و ویکی‌واژه با تردید ایرانی آغازین *urw-āna- را پیشنهاد می‌کند. ادعای نورایی دربارهٔ خود ریشه درست است.\",\n\"sources\":[RAVAN],\n\"ref_check\":[{\"ref\":\"SYN:1088\",\"status\":\"supports\",\"note\":\"SYN.txt 16.11 SOUL, SPIRIT (line 27531 ff., printed p.1087-1088): table 'Av. urvan-, mainyu-' and note 'Av. urvan-, the usual term for 'soul, spirit', etym.? Barth. 1537 ff.'\"},{\"ref\":\"BQT:967\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 427 (≈ p.967-970): footnote 'پهلوی ruvân (روح). اوستا urvan- بارتولمه ۱۵۳۷'.\"}],\n\"consulted\":[BRTu,NYBu,{\"src\":\"POK\",\"where\":\"POK_full.txt grep 'urvan'\",\"stance\":\"silent\",\"note\":\"Pokorny gives no IE root for Av. urvan-.\"}],\n\"nodes\":[]}\ne2[\"nodes\"].append({\"id\":1,\"lang\":\"Pahlavi\",\"words\":\"ruvân\",\"verdict\":\"confirmed\",\n\"derivation\":\"Middle Persian ruwān [lwbʾn], Manichaean MP rwʾn 'soul' continues Av./Old Iranian *urwān- (nom. urva, oblique stem urvān-) with metathesis/anaptyxis of the initial ur- cluster to ru- (cf. Parthian ʾrwʾn arwān with prothetic a-). The Zoroastrian Pahlavi texts use it for the immortal soul, beside gyān 'life'.\",\n\"derivation_fa\":\"فارسی میانه ruwān «روان» (در متون مانوی rwʾn) دنبالهٔ اوستایی/ایرانی باستان urvan- (ستاک urvān-) است که در آن آغازهٔ ur- با جابه‌جایی (قلب) به ru- بدل شده؛ پارتی آن ʾrwʾn (arwān) با واکهٔ افزوده در آغاز است. ادعای نورایی درست است.\",\n\"sources\":[RAVAN],\n\"ref_check\":[{\"ref\":\"BQT:967\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 427: 'پهلوی ruvân (روح). اوستا urvan-'.\"}],\n\"consulted\":[PHDu,NYBu,HUBu]})\ne2[\"nodes\"].append({\"id\":2,\"lang\":\"Persian\",\"words\":\"ravân\",\"verdict\":\"confirmed\",\n\"derivation\":\"NP روان ravān 'soul, spirit' < MP ruwān < Av. urvan-; early NP rawān with u > a before w (cf. Hübschmann's variant raban/ruban). It is a homonym of روان1 'flowing, running' (present stem rav- of raftan + -ān), the pun exploited in the Ferdowsi line quoted (آب روان ... تازه گردد روان). Modern derivatives روانکاو 'psychoanalyst', روانپزشک 'psychiatrist' are 20th-c. Academy coinages.\",\n\"derivation_fa\":\"«روان» به معنای جان و روح از فارسی میانه ruwān و اوستایی urvan- آمده است؛ در فارسی نو u پیش از w به a بدل شده است (ravān). این واژه با «روان ۱» (روان‌شونده، از ستاک «رو» + «ـان») هم‌آواست و فردوسی در بیت آورده‌شده از همین بازی استفاده کرده است. «روانکاو» و «روانپزشک» ساخته‌های فرهنگستان در سدهٔ بیستم‌اند. درست است.\",\n\"sources\":[RAVAN],\n\"ref_check\":[{\"ref\":\"BQT:967\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 427: headword 'روان ... نفس ناطقه است' with footnote 'پهلوی ruvân، اوستا urvan-'.\"}],\n\"consulted\":[BQTu,HUBu,{\"src\":\"ARY\",\"where\":\"ARY_pages.txt line 3569 (روانی)\",\"stance\":\"silent\",\"note\":\"OCR hit for روانی only; no legible entry for روان 'soul' (Aryanpur lists only words with a known IE root).\"},{\"src\":\"MON\",\"where\":\"MON_part1/2 grep روان\",\"stance\":\"silent\",\"note\":\"abridgement has the word but no etymological tag captured in the OCR.\"}]})\ne2[\"nodes\"].append({\"id\":3,\"lang\":\"Sogdian\",\"words\":\"`rw`n\",\"verdict\":\"confirmed\",\n\"derivation\":\"Sogdian ʾrwʾn (o)rwān, oruwān 'soul, spirit' (Buddhist, Sogdian-script and Christian texts; Gharib no. 1513) is the Sogdian outcome of Old Iranian *urwān-, with the initial ur- written ʾrw-. Nourai's NOTE is correct: it is a cognate (sister form) of Avestan urvan-, not a derivative of Avestan - Gharib's '< Av. urvan' is shorthand for the common Old Iranian form.\",\n\"derivation_fa\":\"سغدی ʾrwʾn (orwān، oruwān) «روان، روح» (قریب، شمارهٔ ۱۵۱۳) دنبالهٔ ایرانی باستان *urwān- است. یادداشت نورایی درست است: این واژه هم‌ریشهٔ اوستایی urvan- است، نه برگرفته از اوستایی؛ «از اوستایی» در فرهنگ قریب به معنای صورت ایرانی باستان مشترک است.\",\n\"sources\":[RAVAN],\n\"ref_check\":[{\"ref\":\"SOD:59\",\"status\":\"supports\",\"note\":\"SOD_pages.txt line 8102: '1513 'rw'n B, S, C / (o)rwan, oruwan <Av. urvan / soul, spirit / TSP; VJ 476 ...' (on the page ≈ p.59).\"}],\n\"consulted\":[{\"src\":\"SOD\",\"where\":\"entry 1513 (SOD_pages.txt line 8102)\",\"stance\":\"supports\",\"note\":\"''rw'n B, S, C (o)rwan, oruwan <Av. urvan soul, spirit'.\"},NYBu]})\nentries.append(e2)\n\nout={\"pdf_page\":521,\"book_page\":491,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":entries}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-521.json\",\"w\"),ensure_ascii=False,indent=1)\nEOF\ncd /home/sfmqrb/git/rishe-private && python3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-521.py && python3 -m json.tool data/verification/page-521.json >/dev/null && python3 tools/verify_check.py 521"
}
```


### [2026-10-16T05:19:44.655Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'plausible': 6, 'confirmed': 6, 'transcription_suspect': 1, 'disputed': 2}
root verdicts: {'disputed': 2, 'confirmed': 1}
ref checks: {'partial': 4, 'supports': 14, 'not_found': 2, 'not_checked': 5, 'contradicts': 1}
books consulted: {'supports': 32, 'silent': 6, 'contradicts': 4, 'partial': 5} | by book: {'KLN': 6, 'HJB': 6, 'LKT': 6, 'HUB': 4, 'HRN': 4, 'NYB': 4, 'MON': 3, 'PHD': 2, 'BQT': 2, 'ARY': 2, 'SOD': 2, 'TTS': 1, 'BRT': 1, 'IEC': 1, 'LAT': 1, 'WLD': 1, 'POK': 1}
```


## [2026-10-16T05:19:49.045Z] TOOL CALL #50: Bash

```json
{
 "command": "sed -i 's/\"p.71 (PHD.txt line 559)\"/\"s.v. rēšag (PHD.txt line 559)\"/; s/\"p.71 (PHD.txt line 561)\"/\"s.v. ruwān (PHD.txt line 561)\"/; s/\"Glossary p.168 (NYB_vol2_glossary.txt line 3309)\"/\"Glossary s.v. rēš (NYB_vol2_glossary.txt line 3309)\"/; s/\"p.? (HUB.txt line 5886)\"/\"Part II, HUB.txt line 5886\"/' data/verification/page-521.json && python3 -m json.tool data/verification/page-521.json >/dev/null && python3 tools/verify_check.py 521 | grep -c PROBLEM"
}
```


### [2026-10-16T05:19:49.537Z] TOOL RESULT

```
0
```


## [2026-10-16T05:19:57.335Z] TOOL CALL #51: SubagentHandback

```json
{
 "message": "I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-521.json` for page 521 (book page 491). `verify_check.py 521` reports 15/15 nodes verified and 0 PROBLEM lines.\n\n**Verdicts:**\n- **Roots (3):** 1 confirmed (Urvan), 2 disputed (Urmak; Uroiks/Loik).\n- **Nodes (15):** 6 confirmed, 6 plausible, 2 disputed, 1 transcription_suspect.\n\n**Disputed and transcription_suspect items:**\n- **ROOT Urmak (Mongolian, \"to strike\"):** urmak is a Turkic verb (Turkish vurmak < Proto-Turkic *ur-), not Mongolian. Modern sources do not derive *ordu \"camp\" from it; the chart copies Klein, who also calls it Tatar, not Mongolian.\n- **Urmak #7 \"hoard\":** the book prints \"hoard\" with the gloss of horde. This is Nourai's misprint for **horde** (error_in = book; the extraction is faithful). The page image is saved at `data/verification/sources/refs/ocr/BOOK/521.png`.\n- **ROOT Uroiks, Loik (IE \"twist, twine, beard\"):** this is Mann's isolated *loik- (1) entry, copied word for word. Pokorny and Watkins have no such root.\n- **Uroiks #1 Avestan raēša \"hair, beard\":** Avestan raēša- means \"injury, wound\" (the source of ریش \"wound\", not ریش \"beard\"). Hübschmann (no. 640) and Horn (no. 640) reject the \"beard\" meaning.\n- **Uroiks #5 Latin līcium:** its origin is uncertain (Ernout-Meillet: bilix/trilix; Walde-Pokorny: *lei-k- \"bend\"). Only Mann links it to rīš.\n\n**Extraction errors for the owner to fix:**\n- **Urmak root box:** on the printed page, \"Urdu: camp of strikers, army camp\" sits inside the same Mongolian box as \"Urmak\". The JSON splits it out as a separate node #1 (parent #0). I verified it as a node as given.\n\nNourai's ref numbers KLN:1861 (beyond Klein's last page, 1776) and IEC:104 look like his own slips (likely for 1681 and 704). I left them as not_found / not_checked."
}
```


### [2026-10-16T05:19:57.603Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
