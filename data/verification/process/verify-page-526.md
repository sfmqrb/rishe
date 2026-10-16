# Verification process log — verify-page-526


## [2026-10-16T05:13:01.698Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 526 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-526.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-526.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-526.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 526` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.792Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:07.306Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:07.371Z] TOOL RESULT

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


## [2026-10-16T05:13:07.860Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-526.txt"
}
```


### [2026-10-16T05:13:07.903Z] TOOL RESULT

```
1	=== PDF page 526 (book page 496) ===
2	--- entry 0 ---
3	ROOT Waq -> redirect to Wegh
4	--- entry 1 ---
5	ROOT Wâs -> redirect to Wes 1
6	--- entry 2 ---
7	ROOT [Indo-European] Wě 1, Aŭe 1 : to blow  (refs POK:81)
8	#1 (parent #0) [Avestan] refs=POK:81; KLN:1745; BQT:170 | vâta : wind ; vâiti : blows ; vât-âs : wind mill ☞Ak ; antara-vâyu : in the wind, wandering, poor ☞En
9	  #2 (parent #1) [Persian] refs=BQT:170,205 | bâd «باد ۱» : wind ; bâdâs «بادآس» : wind mill ; andarvâ «اندروا» : wandering, poor | extra: بادبان ، بادبادک ، بادخَن / اندرواژ ، اندروای
10	#3 (parent #0) [Sanskrit] refs=KLN:1049 | nir-vanah : blowing out, extinction ☞Nis
11	  #4 (parent #3) [Persian] refs=MON:4882 | nîrvânâ «نیروانا» : extinction of soul by absorption into the Supreme Being
12	  #5 (parent #3) [English] refs=AHD:889 | Nirvana : extinction of soul by absorption into the Supreme Being
13	#6 (parent #0) [Germanic] refs=AHD | windaz, wedram : wind ; vind-auga : wind eye (window) ☞Okw ; wě-ingia : wing
14	  #7 (parent #6) [English] refs=None | wind, weather ; window ; wing
15	#8 (parent #0) [Latin] refs=AHD | ventus : wind
16	  #9 (parent #8) [English] refs=AHD | vent, fan
17	#10 (parent #0) [Greek] refs=AHD | atmo : air
18	  #11 (parent #10) [Latin] refs=None | 
19	    #12 (parent #11) [French] refs=None | 
20	      #13 (parent #12) [Persian] refs=MON:32 | âtmosfer «آتمسفر» : atmosphere
21	    #14 (parent #11) [English] refs=None | atmosphere
22	#15 (parent #0) [Greek] refs=AHD | aěr : air
23	  #16 (parent #15) [English] refs=None | air
24	  #17 (parent #15) [Latin] refs=None | mal-aria : bad (sick) air ☞Mel 2
25	    #18 (parent #17) [Italian] refs=None | 
26	      #19 (parent #18) [French] refs=MON:3709 | 
27	        #20 (parent #19) [Persian] refs=MON:3709 | mâlârîyâ «مالاریا» : malaria
28	      #21 (parent #18) [English] refs=AHD | malaria
29	--- entry 3 ---
30	ROOT We 2 -> redirect to Au 2
31	
```


## [2026-10-16T05:13:08.641Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-526.json"
}
```


### [2026-10-16T05:13:08.676Z] TOOL RESULT

```
1	{
2	  "pdf_page": 526,
3	  "book_page": 496,
4	  "entries": [
5	    {
6	      "root": {"name": "Waq", "redirect": "Wegh"},
7	      "nodes": []
8	    },
9	    {
10	      "root": {"name": "Wâs", "redirect": "Wes 1"},
11	      "nodes": []
12	    },
13	    {
14	      "root": {
15	        "name": "Wě 1, Aŭe 1",
16	        "lang": "Indo-European",
17	        "refs": "POK:81",
18	        "gloss": "to blow"
19	      },
20	      "nodes": [
21	        {
22	          "id": 1,
23	          "parent": 0,
24	          "lang": "Avestan",
25	          "refs": "POK:81; KLN:1745; BQT:170",
26	          "words": [
27	            {"translit": "vâta", "gloss": "wind", "script": null},
28	            {"translit": "vâiti", "gloss": "blows", "script": null},
29	            {"translit": "vât-âs", "gloss": "wind mill", "script": null, "see": ["Ak"]},
30	            {"translit": "antara-vâyu", "gloss": "in the wind, wandering, poor", "script": null, "see": ["En"]}
31	          ],
32	          "note": null,
33	          "quote": null
34	        },
35	        {
36	          "id": 2,
37	          "parent": 1,
38	          "lang": "Persian",
39	          "refs": "BQT:170,205",
40	          "words": [
41	            {"translit": "bâd", "gloss": "wind", "script": "باد ۱"},
42	            {"translit": "bâdâs", "gloss": "wind mill", "script": "بادآس"},
43	            {"translit": "andarvâ", "gloss": "wandering, poor", "script": "اندروا"}
44	          ],
45	          "script_extra": "بادبان ، بادبادک ، بادخَن / اندرواژ ، اندروای",
46	          "note": null,
47	          "quote": null
48	        },
49	        {
50	          "id": 3,
51	          "parent": 0,
52	          "lang": "Sanskrit",
53	          "refs": "KLN:1049",
54	          "words": [
55	            {"translit": "nir-vanah", "gloss": "blowing out, extinction", "script": null, "see": ["Nis"]}
56	          ],
57	          "note": null,
58	          "quote": null
59	        },
60	        {
61	          "id": 4,
62	          "parent": 3,
63	          "lang": "Persian",
64	          "refs": "MON:4882",
65	          "words": [
66	            {"translit": "nîrvânâ", "gloss": "extinction of soul by absorption into the Supreme Being", "script": "نیروانا"}
67	          ],
68	          "note": null,
69	          "quote": null
70	        },
71	        {
72	          "id": 5,
73	          "parent": 3,
74	          "lang": "English",
75	          "refs": "AHD:889",
76	          "words": [
77	            {"translit": "Nirvana", "gloss": "extinction of soul by absorption into the Supreme Being", "script": null}
78	          ],
79	          "note": null,
80	          "quote": null
81	        },
82	        {
83	          "id": 6,
84	          "parent": 0,
85	          "lang": "Germanic",
86	          "refs": "AHD",
87	          "words": [
88	            {"translit": "windaz, wedram", "gloss": "wind", "script": null},
89	            {"translit": "vind-auga", "gloss": "wind eye (window)", "script": null, "see": ["Okw"]},
90	            {"translit": "wě-ingia", "gloss": "wing", "script": null}
91	          ],
92	          "note": null,
93	          "quote": null
94	        },
95	        {
96	          "id": 7,
97	          "parent": 6,
98	          "lang": "English",
99	          "refs": null,
100	          "words": [
101	            {"translit": "wind, weather", "gloss": null, "script": null},
102	            {"translit": "window", "gloss": null, "script": null},
103	            {"translit": "wing", "gloss": null, "script": null}
104	          ],
105	          "note": null,
106	          "quote": null
107	        },
108	        {
109	          "id": 8,
110	          "parent": 0,
111	          "lang": "Latin",
112	          "refs": "AHD",
113	          "words": [
114	            {"translit": "ventus", "gloss": "wind", "script": null}
115	          ],
116	          "note": null,
117	          "quote": null
118	        },
119	        {
120	          "id": 9,
121	          "parent": 8,
122	          "lang": "English",
123	          "refs": "AHD",
124	          "words": [
125	            {"translit": "vent, fan", "gloss": null, "script": null}
126	          ],
127	          "note": null,
128	          "quote": null
129	        },
130	        {
131	          "id": 10,
132	          "parent": 0,
133	          "lang": "Greek",
134	          "refs": "AHD",
135	          "words": [
136	            {"translit": "atmo", "gloss": "air", "script": null}
137	          ],
138	          "note": null,
139	          "quote": null
140	        },
141	        {
142	          "id": 11,
143	          "parent": 10,
144	          "lang": "Latin",
145	          "refs": null,
146	          "words": [],
147	          "note": null,
148	          "quote": null
149	        },
150	        {
151	          "id": 12,
152	          "parent": 11,
153	          "lang": "French",
154	          "refs": null,
155	          "words": [],
156	          "note": null,
157	          "quote": null
158	        },
159	        {
160	          "id": 13,
161	          "parent": 12,
162	          "lang": "Persian",
163	          "refs": "MON:32",
164	          "words": [
165	            {"translit": "âtmosfer", "gloss": "atmosphere", "script": "آتمسفر"}
166	          ],
167	          "note": null,
168	          "quote": null
169	        },
170	        {
171	          "id": 14,
172	          "parent": 11,
173	          "lang": "English",
174	          "refs": null,
175	          "words": [
176	            {"translit": "atmosphere", "gloss": null, "script": null}
177	          ],
178	          "note": null,
179	          "quote": null
180	        },
181	        {
182	          "id": 15,
183	          "parent": 0,
184	          "lang": "Greek",
185	          "refs": "AHD",
186	          "words": [
187	            {"translit": "aěr", "gloss": "air", "script": null}
188	          ],
189	          "note": null,
190	          "quote": null
191	        },
192	        {
193	          "id": 16,
194	          "parent": 15,
195	          "lang": "English",
196	          "refs": null,
197	          "words": [
198	            {"translit": "air", "gloss": null, "script": null}
199	          ],
200	          "note": null,
201	          "quote": null
202	        },
203	        {
204	          "id": 17,
205	          "parent": 15,
206	          "lang": "Latin",
207	          "refs": null,
208	          "words": [
209	            {"translit": "mal-aria", "gloss": "bad (sick) air", "script": null, "see": ["Mel 2"]}
210	          ],
211	          "note": null,
212	          "quote": null
213	        },
214	        {
215	          "id": 18,
216	          "parent": 17,
217	          "lang": "Italian",
218	          "refs": null,
219	          "words": [],
220	          "note": null,
221	          "quote": null
222	        },
223	        {
224	          "id": 19,
225	          "parent": 18,
226	          "lang": "French",
227	          "refs": "MON:3709",
228	          "words": [],
229	          "note": null,
230	          "quote": null
231	        },
232	        {
233	          "id": 20,
234	          "parent": 19,
235	          "lang": "Persian",
236	          "refs": "MON:3709",
237	          "words": [
238	            {"translit": "mâlârîyâ", "gloss": "malaria", "script": "مالاریا"}
239	          ],
240	          "note": null,
241	          "quote": null
242	        },
243	        {
244	          "id": 21,
245	          "parent": 18,
246	          "lang": "English",
247	          "refs": "AHD",
248	          "words": [
249	            {"translit": "malaria", "gloss": null, "script": null}
250	          ],
251	          "note": null,
252	          "quote": null
253	        }
254	      ]
255	    },
256	    {
257	      "root": {"name": "We 2", "redirect": "Au 2"},
258	      "nodes": []
259	    }
260	  ]
261	}
262	
```


## [2026-10-16T05:13:12.565Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; cat tools/verify_check.py | head -150"
}
```


### [2026-10-16T05:13:12.899Z] TOOL RESULT

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


## [2026-10-16T05:13:39.904Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-511.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2500]);print(json.dumps(e['nodes'][1],ensure_ascii=False,indent=1)[:3000])\"; python3 -c \"\nimport json;r=json.load(open('data/verification/sources/refs_online.json'));\nfor k in ['POK','KLN','BQT','MON','AHD']: print(k, json.dumps(r[k],ensure_ascii=False)[:600])\""
}
```


### [2026-10-16T05:13:40.305Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Tôkei, Tôgei",
 "verdict": "plausible",
 "modern_form": "Tamil tōkai (தோகை) 'peacock's tail; peacock' - a proposed, not proven, eastern source of Greek ταώς",
 "note": "Tamil tōkai 'tail of a peacock; peacock' is a real word (Wiktionary தோகை), and Klein (KLN:1143) and Skeat (SKT:378) both name 'Tamil tokei, tōgei' as the ultimate source of the peacock words, so Nourai's root box faithfully reports his references; Wiktionary today calls Greek ταώς 'of Pre-Greek origin; possibly ... perhaps from Dravidian (compare Tamil tōkai)', i.e. only a possibility. The internal chart, however, is wrong in its routing: (1) there is no Sanskrit intermediary (Sanskrit has mayūra-, śikhin-); (2) Arabic ṭāwūs comes from Aramaic ṭawsā, which comes from Greek ταώς, not from Sanskrit; (3) Greek ταώς (5th c. BCE) and Latin pāvō cannot derive from medieval Persian ṭāvūs - the arrows from the Persian box to Greek and Latin reproduce Skeat's 1911 chain and are reversed. Persian ṭāvūs < Arabic, OE pēa < Latin pāvō and English peacock are correct. The book's root note prints 'Tanil' for Tamil (misprint in the book, faithfully extracted). No extraction errors: JSON matches the printed page.",
 "note_fa": "تامیلی tōkai «دم طاووس؛ طاووس» واژه‌ای واقعی است و کلاین (۱۱۴۳) و اسکیت (۳۷۸) هر دو «tokei/tōgei» تامیلی را سرچشمهٔ نهایی نام طاووس در زبان‌های اروپایی دانسته‌اند؛ ویکی‌واژهٔ امروز یونانی ταώς را پیش‌یونانی و تنها «شاید» از دراویدی می‌داند. پس ریشه با احتیاط پذیرفتنی است. اما مسیرهای درون نمودار نادرست است: گذر از سنسکریت گواهی ندارد؛ «طاووس» عربی از آرامی ṭawsā و آن از یونانی ταώς است؛ و یونانی ταώς و لاتین pāvō که بسیار کهن‌ترند نمی‌توانند از «طاووس» فارسی (که خود معرّب است) آمده باشند - پیکان‌ها وارونه‌اند و از اسکیت (۱۹۱۱) گرفته شده‌اند. «طاووس» فارسی از عربی، pēa انگلیسی کهن از لاتین و peacock انگلیسی درست است. «Tanil» در یادداشت کتاب خطای چاپی به جای Tamil است؛ خطای استخراج دیده نشد.",
 "sources": [
  "https://en.wiktionary.org/wiki/தோகை",
  "https://en.wiktionary.org/wiki/ταώς",
  "https://en.wiktionary.org/wiki/طاووس",
  "https://en.wiktionary.org/wiki/pavo",
  "https://en.wiktionary.org/wiki/peacock"
 ],
 "ref_check": [
  {
   "ref": "KLN:1143",
   "status": "partial",
   "note": "Klein 1966 s.v. peacock (KLN_1966.txt line 27770): 'OE. pāwa, pēa ... fr. L. pāvo, gen. pāvonis, 'peacock' ... which, together with Gk. ταώς, prob. comes ult. fr. Tamil tokei, tōgei (whence also Heb. tukkiyyim, 'peacocks'). The initial p- in L. pavo is due to imitative infl
{
 "id": 2,
 "lang": "Arabic",
 "words": "tawoos",
 "verdict": "disputed",
 "derivation": "Arabic ṭāwūs (طاووس, also طاؤوس) 'peacock' is real, but it is not taken from Sanskrit: it is borrowed from Aramaic ṭawsā (טַוסָא), itself borrowed from Greek ταώς (Wiktionary s.v. طاووس: 'Borrowed from Aramaic ṭawsā, borrowed from Ancient Greek ταώς, borrowed from Pre-Greek'). The emphatic ṭ- reflects the Aramaic spelling of Greek t-, and the long ū the Greek long ō. Arab lexicographers (Ibn Durayd in al-Jawālīqī's al-Mu'arrab) already call it a foreign word (أعجمي).",
 "derivation_fa": "«طاووس» عربی (طاؤوس) به معنای طاووس واژه‌ای واقعی است، اما از سنسکریت گرفته نشده است؛ ویکی‌واژه آن را وام‌واژه از آرامی ṭawsā و آن را از یونانی ταώς می‌داند. ط عربی برابر t یونانی در نوشتار آرامی است و ū بلند برابر ō بلند یونانی. ابن درید (در المعرّب جوالیقی) نیز آن را «أعجمی» شمرده است. پس اصل واژه درست است ولی مسیر «سنسکریت ← عربی» را پژوهش امروزی نمی‌پذیرد.",
 "sources": [
  "https://en.wiktionary.org/wiki/طاووس",
  "https://en.wiktionary.org/wiki/ταώς"
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
   "src": "ARB",
   "where": "al-Mu'arrab (ARB_mo3rb.txt lines 16707-16712)",
   "stance": "partial",
   "note": "'(م) «طاؤوس» بالهمزة وأصلها الواو ... وقال [ابن دريد]: وطاؤوس أعجمي ... وقد تكلمت به العرب' - the Arab philologists already treated ṭāwūs as a foreign word, without naming the source."
  },
  {
   "src": "BQT",
   "where": "p.1346, Mo'in fn. s.v. طاوس (ocr/BQT/1346.vision.txt)",
   "stance": "partial",
   "note": "'(عر) معرب آن طویس، یونانی Taôs، آرامی طاوسا tausâ ... اصل کلمه از زبان دراویدی وارد سانسکریت شده و از آنجا بزبانهای دیگر رفته' (after Pourdavoud)."
  },
  {
   "src": "KLN",
   "where": "1966 s.v. peacock (KLN_1966.txt line 27770)",
   "stance": "partial",
   "note": "'L. pavo ... which, together with Gk. ταώς, prob. comes ult. fr. Tamil tokei, tōgei (whence also Heb. tukkiyyim) ... initial p- in L. pavo is due to imitative influence; cp. L. paupulo, 'the natural sound of the peacock''."
  }
 ]
}
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 34
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
```


## [2026-10-16T05:13:43.700Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;r=json.load(open('refs_online.json'));\nfor k in ['POK','KLN','BQT','MON','AHD','WLD','BRT','PHD','NYB','HRN','HUB','ARY','IEC','SYN','SKT']: print(k, r[k].get('page_offset'), '|', r[k].get('lookup_hint','')[:400]);print()\""
}
```


### [2026-10-16T05:13:44.033Z] TOOL RESULT

```
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-d

KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada

MON None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab

AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.

WLD Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.

BRT Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.

PHD leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).

NYB Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

HUB leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.

ARY printed page = pdf page + 1 | Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image

IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.

SYN leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.

SKT leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
```


## [2026-10-16T05:13:46.657Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'lemma: au̯e-\\|lemma: \\(1\\. \\)\\?au̯ē\\|lemma: 1. au̯e\\|lemma: u̯ē-' POK_full.txt | head; grep -n -i 'lemma:.*au.e' POK_full.txt | head"
}
```


### [2026-10-16T05:13:47.082Z] TOOL RESULT

```
1743:Root/ lemma: au(e)-9, aued-, auer-\ "to flow, to wet; water, etc' 
3840:Root/ lemma: au(e)-9, aued-, auer-\ "to flow, to wet; water, etc' 
7339:Root / lemma: au-2, au-es-, au-s- 
7697:Root/ lemma: aus-\ "to draw (water), ladle' derived from the stem: au/e/-, auent-:a\ Root/ 
7699:lemma: au(e)-9, aued-, auer-\ "to flow, to wet; water, etc.'. 
7848:Root / lemma: au(e)-10, aue(o)-, ue- 
7998:Root / lemma: au(e)-9, aued-, auer- {*h2ahiue > aue-) 
9356:Root/ lemma: at(e)r-\ "fire, *blow the fire' derived from a suffixed Root/ lemma: au(e)-10, 
9661:band- {* bhend-): "drop' derived from a zero grade of Root/ lemma: au(e)-9, aued-, auer- 
18379:Anatolian languages Root/ lemma: ghesor-1, ghesr-: "hand' because of the common alb.
```


## [2026-10-16T05:13:49.686Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7848,7997p POK_full.txt | cut -c1-300"
}
```


### [2026-10-16T05:13:49.973Z] TOOL RESULT

```
Root / lemma: au(e)-10, aue(o)-, ue- 

Meaning: to blow 

Grammatical information: participle ue-nt- 

Note: in Slavic languages often from the " throw dice ', i.e. to the cleaning of the grain of 

the chaff by throwing of the grains against the wind. 

Material: I. belong to light root form au(e)- 

a. Gr. aoc, (if not late neologism), -ox\c, (see below II a). 

b. Mcymr. awyd^ violent gust of wind ', acorn, awit^ air ' ( *aueido-)\ 



c. i/e-d'^ro- presumably in Old Norse vedrv\. "wind, air, weather'. Old Saxon wedam. " 
weather, bad weather ', Old High German wetar^ weather, scent, free air, wind (of 
animals)' and Old Church Slavic vedro " cheerful weather ', vedrb " jovial, merry (from the 
weather) '; 

£/e-£/- perhaps in gr. £5av6c; " fragrant '; in t/e-d'^- correlates Persson Beitr. 664 doubting 
still £0|jn ai\x6c„ Kanv6(; Kzuioc,, ai\xx\ Hes.). 

d. r-, A derivatives: gr. aupa ' aerial breath, draft ' (places light root form Sij/e-ahead, as 
asAAa, a£T|j6v, Wetter, see below); but app. Gen. n£po(; " smoke, fog, air ' stays away, see 
below uer-^ bind, hang up '. 

Also Albanian ajer: Furlan ajar: Latvian arija: Maltese arja: Sardinian Campidanesu airi; 
aria 'air'. 

Gr. asAAa, Aeolic ausAAa ' storm ' (*aF£A-ja); cymr. awen^ inspiration ', awelt " wind, 
breath ', acorn, auhe/'aura, heaven, breeze ', mcorn. awe/' weather', brit. loanword 
Middle Irish a/7e/(/7 hiatus sign), a/a/' wind, breath '. According to Thurneysen Grammar 
125 Old Irish oa/' mouth ' from *aue/a. 

e. au-et-vc\ gr. qstijov to nvsupa Hes., a£T|ja cpAo^ Et. M., arpoc; (contracted from 
a£Tpi6(;) ' vapour, smoke, smoke ', with zero grade, but analogical absorption of a-: aurpn " 
breath, draft of the bellows, the wind, smell, hot aura of the fire ', aurtjriv ds. 

II. belong to heavy root form: 

a. ue-, ua-:0\(i Indie vat/, Avestan va/t/' blows ', gr. anai ds., Cypriot ^asi (read ^an with 
Z, from *dp} Hes. (that a in anai perhaps prothetic; from light root form come gr. aoc; 
nveupia Hes.; 

maybe alb. {**ue-nts) Kes/7 'strike, blow, hit'. 

cxKpan(; " sharp blowing ', 5uaanc; " adverse blowing ', unspanq ' excessive blowing ' with 
stretch in compound); besides the participle *ue-nt-' blowing ' (Old Indie vant-, gr. Akk. 
aevTo) stand *ue-nto-s' wind ' in Latin ventus, Gothic etc w/nds. Old High German w/nt, 
cymr. gwynt' wind ', wherefore Latin ven t//a re '{* expose to a draught, brandish, fan), 
oscillate, vibrate', vent//abrum " throw shovel ', Gothic d/sw/n^jan " separate the grain (the 
wheat) from the chaff ', w/nt^/s/<aurd " throw shovel ' (Germanic /=>, next to which with 
gramm. variation d\v\:) Old High German w/nton^ winnow, fan ', w/nta, w/ntscOva/a^ 
winnowing shovel ', Old English windwian^ to expose to the hoist, winnow, fan ' (engl. 



winnov\/); Tocharian A want, B yente " wind '. (under the influence of common Celtic -ns-, - 
nt- > -nn-). 

About Hittite hu-u-wa-an-te-es {h(u)uantes) " hoist ' (?) see Forrer by Feist 565, places the 
word as ' (hurrying) clouds ' to hu-wa-a-r runs, flees ', which also belongs here; see 
CouvreurH 119f., SchwyzerGr. Gr. I 6804. 

n- present: gr. aivu) from *aFa-v-iaj (compare to the formation Schwyzer Gr. Gr. I 694) 
and qvecjo from *aFav£U) ' clean the grains by shaking up of the chaff, sieves ', Favai 
TTspinTiaai Hes. (delivers yavai nspinTuoai; see also Bechtel KZ. 46, 374); is based on 
such zero grade n- present, but in meaning "blow', thus Old Prussian w/ns^a\r', Akk. 
m'nnen' weather'? (under the influence of common Celtic -ns-, -nt- > -nn-). 

Jo-present (or from root form *uef- ?): Old Indie vayat/" blows ', Avestan fravaye/t/" goes 
out' ', Gothic wa/an waiwo. Old English wawan. Old High German wajan, waen' blow ', 
Old Church Slavic vejq, vejeti^ "blow' and " winnow, fan ' (therefrom russ. vejalo, sloven. 
vevnica, poln. wiejaczka^ winnowing shovel, a winnowing-fan '); nominal: Lithuanian vejas 
" blow '; Old Indie vay'u-h, Avestan vayus' blow, wind, air '. 

For root-like value of -/■ leads the sound grade *uT-to the following words in which give 
space, however, partly to other views: Old Church Slavic v/ja/b, vijalica^ storm, weather', 
russ. vbjalica " snow flurry ' (also vejalica\), vbjuga " blizzard, snowstorm ', zavbjatb " snow- 
covered, covered with snow ', Czech vati{ *vbjati) " blow ' (only Slavic developments from 
vortonigem ve}-l)\ 

r. -Church Slavic vichbrb ( *ueisuro-) " whirlwind ' (in any case, at first to russ. vichatb " 
shake, move ', vichljatb " toss, fling ', s. Brugmann Grundr. IP 1049, Pedersen IF. 5, 70, 
and probably as " whirl, swing in the circle ' to *ueis-' turn '); 

Lithuanian vydra, vidras' gale ' (see Leskien Bild. 438; in Lithuanian very rare forms -dra- 
compare really Lithuanian vetra " storm ' - urges to caution); 

hom. aiov pTop, Oupiov aiaOs, aiaOwv from breathing out or letting out the vitality (to last 
meaning Bechtel Lexil 21 f.), gr. root dFia-; mcymr. awyds. 82 above. 

b. aue-d-:0\6 High German wazan, wiaz. Middle High German wazen^ blow, exhale, 
inflate ', waz^ gust of wind ', Lithuanian vedinti^ ventilate, cool '; at most gr. aa^u) " 
breathes ' from *aFa5-iu) (rather, however, gr. neologism of after other verbs in -a^w); 



presumably also (from *au9-d-ro-) Lithuanian audraxw. " storm ', n. " thunderstorm ', Old 
Prussian wydra^ blow '. About Old Indie u(i!^arv\. " chillness, cold ', Avestan aodara, aota 
ds. compare Persson Beitr. 1 1 . 

c. j[/e-A?- perhaps in Latin evelatus^ scattered, dissipated, fan away, winnow thoroughly', 
whence i/e/Sit'/'a "something winnowing the grain' (Paul. Fest. 68, 3) and in Old High 
German wala m. n. ' fans ' (if not from *we-t^la, see below)? 

d. ue-s-:0\6 Indie vasa-h, vasaka-h^ fragrance ', vasayat/" fills with fragrance ', 
samvasita-h " makes stinking '; isl. vas " frigid aura ', vaesa " exhale, blow, breathe ', Dutch 
waas^ white frost, ripe, smell, fragrance ', Lithuanian vestu, vesti^ cool off, become chill or 
become aerial ', vesa^ chill air, coolness ', vesus' chilly, aerial '. 

e. /-further formations: Old Indie vata-h, Avestan vato^ blow'. Old Indie vatula-h {see 
below), gr. anTr|<; " blowing, wind ', ar|aupO(; " windy, aerial ' = Old Indie vatula^ windy ' 
(also " mad; crack-brained; demented; mind-boggling; insane; crazy; unbalanced '; in 
addition also perhaps gr. arjauAoq ' sacrilegious, outrageous, wanton, wicked ' after 
Brugmann BSGW. 1901, 94; in spite of aiauAo(; ds. not after Bechtel Lexil. 15 to Old Indie 
yatu-h^ spook, ghost '); 

Latin vannus^ winnowing-fan ' (from *uat-n6-s, compare the Demin. i/a////i//77 originally " a 
small winnowing shovel '; from Latin comes Old High German wanna. Old English fann^ 
winnowing-fan ', also Modern High German Wanne); (under the influence of common 
Celtic -/7s^, -nt- > -nn-). 

Old Norse vel, velT whisk, tail ' (about syncopated VeA'/a-from *val=>ila-). Old High 
German wediMs.; Old High German wadaF tail, fan ', Adj. ' wandering, fickle, beggar', 
wadalon^ sweep in a curve, rove ' (proto Germanic *waNa-, Indo Germanic *u9-tlo-). Old 
English wat^or wandering ', waedla' beggar, poor', wsedr poverty', waedlian^ beg, be 
poor ' (proto Germanic *weNa-), next to which Old High German wallon " wander, gad 
about, pilgrimages ', Old English M/e5///5/7' wander; roam; travel; journey; drift; float; 
rove; stray; migrate; hike; walk; ramble; tramp ' (from * wadl6-ja-n)\ Old High German 
wala^ fans ' (from *we-Na-ox *we-la-, see above); Lithuanian vetra^ storm', thunder- 
storm'. Old Church Slavic i/e//^"air, blow'. Old Prussian wetro^b\o^'\ Lithuanian vetyti 
"winnow, fan'. 

About Old Indie upa-vajayat/" make (fire / embers) blaze by blowing air onto (it / them)' 
(composed from Panini as Kaus. to va-) see Waekernagel KZ. 43, 292. 



Maybe alb. vatra, i/a/e^'hearth, (place where one blows the fire)' 

Maybe here gr. azQKoc, (see aue-1V strive oneself ') as ' gasp, pant, wheeze '? 

References: WP. I 220 f.. Feist 565 a, Trautmann 345, Schwyzer Gr. Gr. I 680. 
Page(s): 81-84
```


## [2026-10-16T05:13:54.618Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^wē-\\|^we-\\.\\|^wē\\b\\|^we- ' AHD_watkins1985.txt | head; grep -n -i 'nirvana\\|ATMOSPHERE\\|MALARIA\\|WINDOW\\|WEATHER' AHD_watkins1985.txt | head -20"
}
```


### [2026-10-16T05:13:54.923Z] TOOL RESULT

```
1124:we-. We. For oblique cases of the pronoun see nes-2, Suffixed variant form *wei-es in Germanic *wiz in Old English wé, we, we: we. [Pok. ué- 1114.]
128:Man and His Physical Environment. A large number of terms relating to time, weather, seasons, and natural surroundings can be reconstructed from the daughter lan- guages, some of which permit certain infer- ences about the homeland of the Indo-European-speaking people before the period of migrations took them to the differ- ent localities where they historically appear.
796:Oku-. Swift. Zero-grade form *aku- in compound *oku-petro-, “swift-flying,” in Latin accipiter, hawk (*pet-ro-, flying; see pet-): ACCIPITER. [Pok. 6ku-s 775.] okv-, To see. 1. Germanic *augén- (with taboo deforma- tion) in: a. Old English éage, eye: EYE; DAISY; b. Old Norse auge, eye: WALLEYED, WINDOW; Cc. Low German 00g, eye: OGLE. 2. Suffixed form *ok-olo- in: a. Latin oculus, eye: EYELET, OCELLUS, OCULAR, OCULIST, UL- LAGE; INOCULATE, MONOCLE, OCULOMETER, OCULOMO- TOR; b. Gallo-Latin compound *ab-oculus, blind, modeled on Gaulish ex-ops, blind, in French aveugle, blind: INVEIGLE. 3. Form *okv-s in Greek dps, eye (and stem *op-, to see): METOPIC, MYOPIA, NYCTALOPIA, PEL- OPS, PHLOGOPITE, PYROPE. 4. Suffixed form *ok-ti- in Greek opsis, sight, appearance: OPSIN, -OPSIS, -OPSY; AUTOPSY, (IODOPSIN), (RHODOPSIN), SYNOPSIS. 5. Suf-
814:fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
955:5. Suffixed form *lag-no- in Greek lagnos, lustful, lasciv- ious (> lagneia, lust, lasciviousness): ALGOLAGNIA. 6. Variant form */ég- in Greek légein, to leave off: CATALECTIC. [Pok. (s)lég- 959.] sleidh-. To slip, slide. 1. Germanic *s/idan, to slip, slide, in Old English s/idan, to slide: SLIDE. 2. Germanic *slid- in: a. Middle Low German sledde, a sled, sledge: SLED; b. Middle Dutch s/éde, a sled: SLEIGH; C. Middle Dutch sleedse, sleigh: SLEDGE. sleng”h-. To slide, make slide, sling, throw. 1. Germanic strong verb *slingwan and derived suffixed noun form *slingw-6- in Old Frisian slinge, sling, akin to the possi- ble source of Middle English sling, sling: SLING}; (SLING- SHOT). 2. Germanic variant strong verb *slinkan in Old English slincan, to creep: SLINK. 3. Suffixed o-grade form *slongh-ri-ko- in Latin lumbricus, intestinal worm, earthworm: LUMBRICOID. [In Pok. (sjleidh- 960, slenk- 961.] sleu-. Hypothetical base of a group of distantly related Germanic derivatives with various suffixes. 1. Germanic *slii-m- in Old English slima, sleep: SLUMBER. 2. Prob- ably Germanic *slautjan- in Old English “s/léte, sleet: SLEET. 3. Germanic *slus- in Norwegian slusk, sloppy weather, probably akin to the possible Scandinavian source of SLUSH. 4. Germanic *sleura- in Middle High German slier, mud, slime: SCHLIEREN. 5. Extended form *sleug- in Germanic ‘*sluk-, *slug- in: a. Norwegian dialectal slugg and Swedish dialectal slagga, slow-mov- ing animal or person, probably akin to the source of Middle English slugge, a sluggard, and sluggen, to be idle: SLUG?, SLUGGARD; b. Dutch /og, lazy, slack: LOGY. [Pok. (s)leu- 962.] sleubh-. To slide, slip. I. Basic form *sleubh-. 1. Ger- manic *slewb- in Old English s/éf, siif, slief, sleeve (into which the arm slips): SLEEVE. 2. Suffixed form *sleubh- ro- in Latin Jibricus, slippery: LUBRICATE, LUBRICITY, LUBRICIOUS. II. Variant Germanic form *sleup-. 1. Ger- manic *slup- in: a. Old English slypa, slyppe, slipa, slime, slimy substance: SLIP’; COWSLIP, OXLIP; b. Old English *sloppe, liquid food (perhaps > Middle English sloppe, a muddy place): sLoP!; c. Old English (ofer)slop, surplice (perhaps > Middle English sloppe, a kind of garment): SLOP?. 2. Germanic *s/aup- in Dutch sloep, sloop (< “gliding boat”): sLoop. [Pok. sleub(h)- 963.] sli-. Bluish. Contracted from *s/is-. 1. O-grade form *sloi- in Germanic *slaihw6n in Old English s/ah, sla, sloe (< “bluish fruit”): SLOE. 2. Suffixed form *sli-wo- in Latin livére, to be bluish: Livip. 3. Suffixed form *s/i-wd- in Serbo-Croatian sijiva, plum: sLivovitz. [Pok. (s)li- 965.] sloug-. Help, service. Celtic and Balto-Slavic. Suffixed form *sloug-o- in Old Irish slag, slog, army, host, whence Gaelic sluagh, army, host: SLEW!, SLOGAN. [Pok. slougo- 965.] smé-. To smear. Contracted from *smeo-. 1. Extended root *smeid- (< *smea-id-) in Germanic *smitan in Old English smitan, to daub, smear, pollute: SMITE. (2. At- tributed by some to this root, but more likely to be of unknown origin, is the Germanic root *mas-, spot, speck, in: a. Middle Dutch masel, pustule, spot, akin to the source of Middle English masel, measles-spot: MEASLES; b. Old French masere, mazre, knot in wood: MAZER.) 3. Attributed by some to this root, but perhaps distinct, is root *smik-, small, in: a. Latin mica, crumb, small piece, grain: MICA; b. Greek (s)mikros, small: MICRO-, MICRON; CHYLOMICRON, OMICRON. [Pok. smé- 966.] smeg-. To taste. Germanic *smak- in: a. Old English smzxc, flavor, taste: SMACK?; b. Middle Dutch and Mid- dle Low German smacken, to taste, make a sound with the lips while tasting food, akin to the source of SMACK!. [Pok. smeg(h)- 967.] smei-. To laugh, smile. 1. Germanic reshaped forms *smer-, *smar- in Old English smercian (with -k- forma- tive), to smile: SMIRK. 2. Germanic extended form *smil- in Swedish smila, to smile, probably akin to the Scandi-
1125:wé-. To blow. Contracted from “*wea-; oldest basic form *gwé- (< *owea-). 1. Suffixed irregular shortened form *we-dhro- in Germanic *wedram, wind, weather, in Old English weder, weather, storm, wind: WEATHER. 2. Suf- fixed (participial) form *wé-nt-o-, blowing, in: a. Ger- manic *windaz in (i) Old English wind, wind: wIND! (ii) Old Norse vindr, wind: wInpow; b. Latin ventus, wind: VENT, VENTAIL, VENTILATE. 3. Suffixed Germanic form *wé-ingjaz in Old Norse vengr, wing, akin to the Scandi- navian source of Middle English wenge, wing: WING. 4. Basic form *wé- in Sanskrit vdti (stem *vd-), he blows: NIRVANA. [Pok. 10. aw/é)- 81.]
1144:*wn-to- in Germanic *wundaz in Old English wund, a wound: WOUND!. 2. Suffixed o-grade form *won-yo- in Germanic *wanja-, a swelling, in Old English wen(n), wen{n), wen: WENI. [In Pok. 1. ué- 1108.] wendh-. To turn, wind, weave. 1. Germanic *windan, to wind, in: a. Old English windan, to wind: WIND2; b. Old Norse vinda, to wind: WINDLASS. 2. Germanic causative *wandjan in: a. Old English wendan, to turn to: WEND; b. Dutch wenden, to turn: WENTLETRAP. 3. Germanic *wandr6n, to roam about, in: a. Old English wandrian, to wander: WANDER; b. German wandern, to wander: WANDERLUST. 4. Germanic *wanduz in Old Norse véndr, a supple twig: WAND. 5. Germanic *wandljaz, “wan- derer,” perhaps in Latin Vandalus, a Vandal: VANDAL. [Pok. 1. uwendh- 1148.] weng-. To bend, curve. 1. Germanic *wink- in Old Eng- lish wincian, to close the eyes (< “to bend down the eyelids”): WINK. 2. Germanic *winkja in Old English wince, a reel, roller: WINCH. 3. Germanic *winkil- in Old English -wincel, spiral shell: PERIWINKLE!. 4, Germanic *wankil-, *wankul- in: a. Old English wencel, youth, maid (< “inconstant one’): WENCH; b. Old English wancol, inconstant, unsteady: wonky. 5. Germanic *wankj- in: a. Old French gauchir, to turn aside: GAUCHE; b. Anglo-Norman *wencir, to turn aside, avoid (> Middle English wincen, to kick): w1NcE. [Pok. we-n-g- 1148.] wep-. Bad, evil. From earlier *awep-. Suffixed zero-grade form *up-elo- in Germanic *ubilaz, evil, in Old English yfel, evil: EVIL. [wépnam. Weapon. Germanic root. 1. Old English wé- P(e)n, weapon: WEAPON. 2. Old Norse vapn (plural vdpn), weapon: WAPENTAKE.] wer-', High raised spot. 1. Suffixed form *wer-d- in Germanic *wartén- in Old English wearte, wart: WART. 2. Possibly Germanic *war- in obsolete Swedish var- bulde, “pus swelling” (bulde, swelling; see bhel-2), akin to the source of WARBLE2. 3. Latin varius (genitive plural variérum), spotty, speckled, changeable: (VAIR), VARIE- GATE, (VARIETY), VARIOLA, VARIORUM, VARIOUS, VARY; (MINIVER). 4. Latin varix, varicose vein: VARIX. 5. Suf- fixed and extended zero-grade form *wrsu-ko- in Latin verriica, a wart: VERRUCA. [Pok. 2. wer- 1151, 2. ud- 1108.] wer-2. To raise, lift, hold suspended. Earlier form *ower-. 1. Basic form *awer- in Greek aeirein, to raise, and Greek artéria, windpipe, artery: AORTA, ARSIS, ARTERIO-, ARTERIOLE, ARTERY. 2. Possibly referred to this root (obscure basic form *dwer-) is Greek aér (> Latin aer > Italian aria), air: AERIAL AERO-, AIR, ARIA, MALARIA. 3. Related to Greek aér, air, is Greek aura (< zero-grade form *aur-), breath, vapor: AURA. [Pok. 1. wer- 1151.] wer-3, Conventional base of various Indo-European roots; to turn, bend. I. Root *wert-, to turn, wind. 1. Germanic *werth- in: a. Germanic variant *warth- in (i) Old Eng- lish -weard, toward (< “turned toward”): -WARD (ii) Germanic *inwarth, inward (*in, in; see en), in Old English inweard, inward: INWARD; b. perhaps Germanic derivative *werthaz, “toward, opposite,” hence “equiv- alent, worth,” in Old English weorth, worth, valuable, and derivative noun weorth, wierth, value: WORTH}; STALWART. 2. Germanic *werthan, to become (< “to turn into”), in Old English weorthan, to befall: worTH?. 3. Zero-grade form *wrt- in Germanic *wurth- in Old English wyrd, fate, destiny (< “that which befalls one”): WEIRD. 4, Latin vertere, to turn, with its frequentative versare, to turn, and passive versari, to stay, behave (< “to move around a place, frequent”): VERSATILE, VERSE}, VERSION, VERSUS, VERTEBRA, VERTEX, VERTIGO, VOR- TEX; ADVERSE, ANNIVERSARY, AVERT, BOULEVERSE- MENT, CONTROVERSY, (CONVERSE!), CONVERT, DEXTRORSE, DIVERT, EVERT, (EXTROVERSION), EXTRO- VERT, INTRORSE, INTROVERT, INVERT, MALVERSATION, OBVERT, PERVERT, PROSE, RETRORSE, REVERT, SINIS-
1165:wet-'. To blow, inspire, spiritually arouse. Related to wé-. 1. Lengthened-grade form *w6t- in Germanic suffixed form *wéd-eno-, *wéd-ono-, “raging,” “mad,” “inspired,” hence “spirit,” name of the chief Teutonic god, in: a. Old English Woéden, Woden: WoDEn; b. Old English Wod- nesdxg, ““Woden’s day”: WEDNESDAY; Cc. Old Norse Odhinn, Odin: Opin; d. Old High German Wuotan (> German Wotan), Wotan: WoTAN. 2. Lengthened variant form *wdt- in Latin vdtés, prophet, poet: vaTic. 3. Suf- fixed variant form *wat-no- in Latin vannus, a winnow- ing fan: FAN!, vAN3. 4, Oldest basic form *awet- becoming *awet- in suffixed form *awet-mo- in Greek atmos (< *aetmos), breath, vapor: ATMOSPHERE. [Pok. udé- 1113.]
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
1803:MAL- mel-5 MALACHITE malakhé MALACOLOGY mel-1 MALADY mel-5 MALARIA wer-2
1923:NIPPLE nabja- NIRVANA we-
```


## [2026-10-16T05:14:01.820Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,60p tools/fetch_source.py"
}
```


### [2026-10-16T05:14:02.129Z] TOOL RESULT

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


## [2026-10-16T05:14:12.876Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; mkdir -p $S; : > $S/urls-526.txt\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂weh₁-\" \"https://en.wiktionary.org/wiki/vāta\" \"https://en.wiktionary.org/wiki/باد\" \"https://en.wiktionary.org/wiki/اندروای\" \"https://en.wiktionary.org/wiki/निर्वाण\" \"https://en.wiktionary.org/wiki/nirvana\" \"https://en.wiktionary.org/wiki/wind\" \"https://en.wiktionary.org/wiki/weather\" \"https://en.wiktionary.org/wiki/window\" \"https://en.wiktionary.org/wiki/wing\" \"https://en.wiktionary.org/wiki/ventus\" \"https://en.wiktionary.org/wiki/vent\" \"https://en.wiktionary.org/wiki/fan\" \"https://en.wiktionary.org/wiki/ἀτμός\" \"https://en.wiktionary.org/wiki/atmosphere\" \"https://en.wiktionary.org/wiki/ἀήρ\" \"https://en.wiktionary.org/wiki/air\" \"https://en.wiktionary.org/wiki/malaria\" \"https://en.wiktionary.org/wiki/vannus\" \"https://en.wiktionary.org/wiki/vāyu\" \"https://www.etymonline.com/word/vent\" \"https://www.etymonline.com/word/air\" \"https://www.etymonline.com/word/malaria\" \"https://www.etymonline.com/word/atmosphere\" \"https://www.etymonline.com/word/nirvana\" \"https://www.etymonline.com/word/window\" \"https://www.etymonline.com/word/wing\" \"https://www.etymonline.com/word/fan\"; do p=$(python3 tools/fetch_source.py \"$u\" --note \"page 526, root We 1 (PIE *h2weh1- 'blow'): etymology check\" 2>&1 | tail -1); echo \"$u $p\" >> $S/urls-526.txt; echo \"$u -> $p $(wc -c < $p 2>/dev/null)\"; done",
 "timeout": 600000
}
```


### [2026-10-16T05:14:25.330Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂weh₁- -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/208c74743847ad4c.txt 7761
https://en.wiktionary.org/wiki/vāta -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/19110d5e4ace13e5.txt 3476
https://en.wiktionary.org/wiki/باد -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/fa5aca5687e59d7e.txt 23512
https://en.wiktionary.org/wiki/اندروای -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/4f05c3bb60ea7047.txt 140
https://en.wiktionary.org/wiki/निर्वाण -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/4a1263f9c12f549e.txt 15419
https://en.wiktionary.org/wiki/nirvana -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/5da585b195df37a2.txt 23797
https://en.wiktionary.org/wiki/wind -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/dd8b45b8174956ae.txt 38287
https://en.wiktionary.org/wiki/weather -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/b4e6a62d999564e6.txt 33543
https://en.wiktionary.org/wiki/window -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/cc15bb57c26a563d.txt 46803
https://en.wiktionary.org/wiki/wing -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/4a3552cbf8ec3dee.txt 49641
https://en.wiktionary.org/wiki/ventus -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/169d7e0177f26d8e.txt 11708
https://en.wiktionary.org/wiki/vent -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/0a26bcaab38fd1de.txt 36432
https://en.wiktionary.org/wiki/fan -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/504951ddb6f88669.txt 100733
https://en.wiktionary.org/wiki/ἀτμός -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/43cc7b03b5eeff3b.txt 6498
https://en.wiktionary.org/wiki/atmosphere -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/def0da40ecd94485.txt 25260
https://en.wiktionary.org/wiki/ἀήρ -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/0337404108fe1c00.txt 9842
https://en.wiktionary.org/wiki/air -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/c87ce7e176ebcf1c.txt 70964
https://en.wiktionary.org/wiki/malaria -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/c9f38fb2d03b8d85.txt 33252
https://en.wiktionary.org/wiki/vannus -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/46db96d682e26fe8.txt 5167
https://en.wiktionary.org/wiki/vāyu -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/5d92cd5f9b146eec.txt 131
https://www.etymonline.com/word/vent -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/9d0547fd7df96e83.txt 131
https://www.etymonline.com/word/air -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/bdb15e3796d7eba9.txt 130
https://www.etymonline.com/word/malaria -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/9a09c1735289a8c0.txt 134
https://www.etymonline.com/word/atmosphere -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/61462814d47f9e5d.txt 137
https://www.etymonline.com/word/nirvana -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/6dd0844070b0f011.txt 134
https://www.etymonline.com/word/window -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/7fb551f5851722a4.txt 133
https://www.etymonline.com/word/wing -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/cceb1e9fd03f31be.txt 131
https://www.etymonline.com/word/fan -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/32092a4bb11217f1.txt 130
```


## [2026-10-16T05:14:27.792Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 208c74743847ad4c 19110d5e4ace13e5; do echo \"=== $f\"; sed -n '1,200p' $f.txt | grep -v '^\\s*$' | cut -c1-400 | head -90; done"
}
```


### [2026-10-16T05:14:28.266Z] TOOL RESULT

```
=== 208c74743847ad4c
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂weh₁-
FETCHED: 2026-10-16T05:14:13Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₂weh₁- - Wiktionary, the free dictionary
Reconstruction:Proto-Indo-European/h₂weh₁- - Wiktionary, the free dictionary 
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
 Proto-Indo-European 
 Toggle Proto-Indo-European subsection 
 1.1 
 Root 
 1.1.1 
 Derived terms 
 1.1.2 
 Descendants 
 1.2 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ h₂weh₁- 
 Add languages 
 Reconstruction 
 Discussion 
 English 
 Read 
 Edit 
 View history 
 Tools 
 Tools
 move to sidebar 
 hide 
 Actions
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
 See also: Reconstruction:Proto-Indo-European/h₁weh₂- 
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Root
 [ edit ] 
 *h₂weh₁- ( imperfective ) [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] 
 to blow ( of wind ) 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *h₂weh₁- (100 c, 0 e) 
 *h₂wḗh₁-ti ~ *h₂wéh₁-n̥ti ( athematic Narten root present ) [ 5 ] 
 *h₂wéh₁-n̥ts ( “ wind ” , active participle ) [ 5 ] [ 7 ] 
=== 19110d5e4ace13e5
URL: https://en.wiktionary.org/wiki/vāta
FETCHED: 2026-10-16T05:14:14Z
STATUS: 200
TITLE: vāta - Wiktionary, the free dictionary
vāta - Wiktionary, the free dictionary 
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
 Pali 
 Toggle Pali subsection 
 1.1 
 Alternative forms 
 1.2 
 Etymology 
 1.3 
 Noun 
 1.3.1 
 Declension 
 1.4 
 References 
 Toggle the table of contents 
 vāta 
 15 languages 
 አማርኛ 
 العربية 
 فارسی 
 Bahasa Indonesia 
 Kurdî 
 Lietuvių 
 Malagasy 
 Polski 
 Русский 
 Soomaaliga 
 Kiswahili 
 Тоҷикӣ 
 Türkçe 
 Татарча / tatarça 
 Oʻzbekcha / ўзбекча 
 Entry 
 Discussion 
 English 
 Read 
 Edit 
 View history 
 Tools 
 Tools
 move to sidebar 
 hide 
 Actions
 Read 
 Edit 
 View history 
 General
 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 
 Print/export
 Create a book 
 Download as PDF
```


## [2026-10-16T05:14:35.104Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; ety(){ python3 - \"$1\" \"$2\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1]).read()\nlang=sys.argv[2]\nlines=[l.strip() for l in t.split('\\n') if l.strip()]\nout=[]\nfor i,l in enumerate(lines):\n    if re.match(r'^Etymology( \\d)?$',l) or l.startswith('Etymology '):\n        out.append(' '.join(lines[i:i+12])[:900])\nfor o in out[:6]: print('*',o)\nEOF\n}; for f in 208c74743847ad4c; do sed -n '/Derived terms/,/References/p' $f.txt | grep -v '^\\s*$' | tr '\\n' ' ' | cut -c1-3500; echo; done; for f in fa5aca5687e59d7e 4a1263f9c12f549e 5da585b195df37a2 43cc7b03b5eeff3b 0337404108fe1c00 46db96d682e26fe8; do echo \"=== $f\"; ety $f.txt; done"
}
```


### [2026-10-16T05:14:36.112Z] TOOL RESULT

```
 Derived terms   1.1.2   Descendants   1.2   References   Derived terms  [ edit ]   Terms derived from the Proto-Indo-European root *h₂weh₁- (100 c, 0 e)   *h₂wḗh₁-ti ~ *h₂wéh₁-n̥ti ( athematic Narten root present ) [ 5 ]   *h₂wéh₁-n̥ts ( “ wind ” , active participle ) [ 5 ] [ 7 ]   *h₂weh₁-tr-o- [ 8 ]   Proto-Balto-Slavic: *wēˀtrāˀ ( see there for further descendants )  *h₂weh₁-yú-s ( “ wind ” ) [ 9 ] [ 10 ]   Proto-Balto-Slavic:   Lithuanian: vė́jas ( “ wind ” ) ( or formed synchronically )   Latvian: vējš ( “ wind ” )   Proto-Indo-Iranian: *HwaHyúš ( see there for further descendants )  *h₂ew(h₁)-dʰ-   Proto-Armenian:   Old Armenian: աւդ ( awd ) , օդ ( ōd )   Armenian: օդ ( ōd )   *h₂ewh₁eleh₂   Proto-Celtic: *awelā ( see there for further descendants )  *h₂uh₁d-o- [ 11 ]   Proto-Anatolian:   Hittite: [script needed] ( ḫūda- , “ readiness, ability to act swiftly ” )   *h₂uh₁-nt-r-ie/o- [ 12 ]   Proto-Anatolian:   Hittite: [script needed] ( ḫuntarii̯a(i)- , “ to break wind ” )   *h₂uh₁-oy-ey ~ h₂uh₁-i-enti [ 13 ]   Proto-Anatolian:   Hittite: [script needed] ( ḫuu̯ai- ) , [script needed] ( ḫui- , “ to run, hurry ” )   *h₂uh₁-dʰlo-   Proto-Hellenic: *awetʰlon   Ancient Greek: ἄεθλον ( áethlon )   *h₂uh₁-l-yeh₂   Proto-Hellenic: *awel͏̌l͏̌ā   Ancient Greek: αὔελλα ( aúella ) , ἀέλλη ( aéllē ) , ἄελλα ( áella )   Unsorted formations   Albanian:  Proto-Albanian:   Albanian: vetëtin ( “ it thunders ” )   > ? Proto-Albanian: *awuòr   Albanian: fjur ( “ aloft ” )   Proto-Balto-Slavic:   Lithuanian: vėsùs ( “ fresh, cool ” )   Latvian: vȩ̄ss ( “ fresh, cool ” )   Hellenic:  Ancient Greek: ἀτμός ( atmós ) , ἀϋτμή ( aütmḗ ) , ἀίσθω ( aísthō )   Germanic:  Old Norse: vængr ( see there for further descendants )  Indo-Iranian:  Indic:  Sanskrit: वीज् ( vīj )   Iranian:  Persian: وز ( vaz )   Italic:  Latin: vannus (for *vatnus ), vatillum   Descendants  [ edit ]   Proto-Indo-Iranian: *HwaH-   Proto-Indo-Aryan: *HwaH-   Sanskrit: वा ( vā )   References 

=== fa5aca5687e59d7e
* Etymology 1 1.1.1 Pronunciation 1.1.2 Verb 1.1.2.1 Conjugation 1.2 Etymology 2 1.2.1 Pronunciation 1.2.2
* Etymology 2 1.2.1 Pronunciation 1.2.2 Adjective 1.2.2.1 Declension 2 Gawar-Bati Toggle Gawar-Bati subsection 2.1 Etymology
* Etymology 2.2 Noun 3 Ottoman Turkish Toggle Ottoman Turkish subsection 3.1 Etymology 3.2 Noun 3.2.1 Derived terms
* Etymology 3.2 Noun 3.2.1 Derived terms 3.2.2 Descendants 3.3 Further reading 4 Pashto Toggle Pashto subsection
* Etymology 4.2 Pronunciation 4.3 Noun 4.4 Further reading 5 Persian Toggle Persian subsection 5.1 Pronunciation
* Etymology 1 5.2.1 Noun 5.2.1.1 Derived terms 5.2.1.2 Descendants 5.3 Etymology 2 5.3.1 Verb 5.3.1.1
=== 4a1263f9c12f549e
* Etymology 1.2 Adjective 1.3 Noun 1.3.1 Declension 2 Sanskrit Toggle Sanskrit subsection 2.1 Alternative forms
* Etymology 2.3 Pronunciation 2.4 Noun 2.4.1 Declension 2.4.2 Descendants 2.5 Adjective 2.5.1
* Etymology [ edit ] Borrowed from Sanskrit निर्वाण ( nirvāṇa , “ blown or put out, extinguished ” ) . Adjective [ edit ] निर्वाण • ( nirvāṇ ) ( indeclinable ) extinguished , blown out Noun [ edit ] निर्वाण • ( nirvāṇ )  m ( Buddhism , Jainism ) nirvana Declension
* Etymology [ edit ] From निस्- ( nis- , “ out ” ) + वान ( vāna , “ blown ” ) . Pronunciation [ edit ] ( Classical Sanskrit ) IPA ( key ) : /n̪iɾ.ʋɑː.ɳɐ/ Noun [ edit ] निर्वाण • ( nirvāṇa ) stem ,  n ( Classical Sanskrit ) blowing out, extinction , cessation , setting, vanishing, disappearance निर्वाणं कृ ― nirvāṇaṃ kṛ ― to blow out, extinguish ( Hinduism ) extinction of the flame of life , dissolution , death or final emancipation from matter and re-union with the Supreme Spirit
=== 5da585b195df37a2
* Etymology 1.2 Pronunciation 1.3 Noun 1.3.1 Derived terms 1.3.2 Translations 1.4 Further reading 1.5
* Etymology 2.2 Pronunciation 2.3 Noun 2.3.1 Declension 2.4 Further reading 3 French Toggle French subsection
* Etymology 4.2 Pronunciation 4.3 Noun 4.3.1 Related terms 5 Portuguese Toggle Portuguese subsection 5.1 Etymology
* Etymology 5.2 Pronunciation 5.3 Noun 5.4 Further reading 6 Romanian Toggle Romanian subsection 6.1 Etymology
* Etymology 6.2 Noun 6.2.1 Declension 7 Serbo-Croatian Toggle Serbo-Croatian subsection 7.1 Etymology 7.2 Pronunciation
* Etymology 7.2 Pronunciation 7.3 Noun 7.3.1 Declension 7.4 References 8 Spanish Toggle Spanish subsection
=== 43cc7b03b5eeff3b
* Etymology 1.2 Pronunciation 1.3 Noun 1.3.1 Inflection 1.3.2 Descendants 1.4 References 1.5
* Etymology [ edit ] From *ἀετμός ( *aetmós ) (only attested in an inflected gloss ἀετμόν ( aetmón , “ wind ” ) ), of uncertain origin. Traditionally derived from Proto-Indo-European *h₂weh₁- ( “ to blow ” ) , and connected with ἄημι ( áēmi , “ to breathe, blow ” ) (as well as ἀϋτμή ( aütmḗ , “ breath, scent ” ) , which is now considered unrelated); however, this leaves the vocalism unexplained. Despite superficially similar semantics and phonetics, not from Proto-Indo-European *h₁eh₁t- ( “ to breathe ” ) (whence German Atem ( “ breath ” ) , Sanskrit आत्मन् ( ātmán , “ breath; soul ” ) ). [ 1 ] Pronunciation [ edit ] IPA ( key ) : /aːt.mós/ → /atˈmos/ → /atˈmos/ ( 5 th BCE Attic ) IPA ( key ) : /aːt.mós/ ( 1 st CE Egyptian ) IPA ( key ) : /atˈmos/ ( 4 th CE Koine ) IPA ( key ) : /atˈmos/ ( 10 th CE Medieval ) IPA ( key ) : /atˈmos/ ( 15 th CE Constantinopolitan ) IPA ( key ) : /atˈmos/ Nou
=== 0337404108fe1c00
* Etymology 1.3 Pronunciation 1.4 Noun 1.4.1 Usage notes 1.4.2 Declension 1.4.3 Derived terms 1.4.4
* Etymology [ edit ] Beekes gives Proto-Hellenic *auhḗr ( “ morning mist ” ) , from Proto-Indo-European *h₂ewsér , from *h₂ews- ( “ dawn; east ” ) . Cognate with αὔρᾱ ( aúrā ) (< *h₂éwsreh₂ ), Latin aurōra . [ 1 ] The a was lengthened to ā by compensatory lengthening . Sihler gives Proto-Hellenic *āwḗr ( “ morning mist ” ) but provides no further etymology. [ 2 ] See Albanian fjur . Pronunciation [ edit ] IPA ( key ) : /aː.ɛ̌ːr/ → /aˈir/ → /aˈir/ ( 5 th BCE Attic ) IPA ( key ) : /aː.ɛ̌ːr/ ( 1 st CE Egyptian ) IPA ( key ) : /aˈe̝r/ ( 4 th CE Koine ) IPA ( key ) : /aˈir/ ( 10 th CE Medieval ) IPA ( key ) : /aˈir/ ( 15 th CE Constantinopolitan ) IPA ( key ) : /aˈir/
=== 46db96d682e26fe8
* Etymology 1.2 Pronunciation 1.3 Noun 1.3.1 Declension 1.3.2 Derived terms 1.3.3 Descendants 1.4
* Etymology [ edit ] Etymology tree Proto-Indo-European *h₂weh₁- der. Proto-Italic *watnos der. ? Latin vannus Traditionally derived from Proto-Italic *watnos , from Proto-Indo-European *h₂weh₁- ( “ to blow ” ) ; compare the diminutive vatillum , as well as Latin ventus , Ancient Greek ἄημι ( áēmi ) , Middle High German winden ( “ to winnow ” ) , Icelandic vinsa ( “ to pick out, weed ” ) , English winnow . However, De Vaan is skeptical of the semantics, and leaves the origin open. [ 1 ] Pronunciation [ edit ] ( Classical Latin ) IPA ( key ) : [ˈwan.nʊs] ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈvan.nus] Noun
* Etymology tree Proto-Indo-European *h₂weh₁- der. Proto-Italic *watnos der. ? Latin vannus Traditionally derived from Proto-Italic *watnos , from Proto-Indo-European *h₂weh₁- ( “ to blow ” ) ; compare the diminutive vatillum , as well as Latin ventus , Ancient Greek ἄημι ( áēmi ) , Middle High German winden ( “ to winnow ” ) , Icelandic vinsa ( “ to pick out, weed ” ) , English winnow . However, De Vaan is skeptical of the semantics, and leaves the origin open. [ 1 ] Pronunciation [ edit ] ( Classical Latin ) IPA ( key ) : [ˈwan.nʊs] ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈvan.nus] Noun [ edit ] vannus   f ( genitive vannī ) ; second declension
```


## [2026-10-16T05:14:42.291Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; ety(){ python3 - \"$1\" \"$2\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1]).read()\nlines=[l.strip() for l in t.split('\\n') if l.strip()]\nj=' \\n '.join(lines)\n# split by language headers roughly: find \"Etymology [ edit ]\" occurrences\nfor m in re.finditer(r'Etymology( \\d)? \\n \\[ edit \\]',j):\n    s=j[m.start():m.start()+700].replace(' \\n ',' ')\n    if sys.argv[2] in j[max(0,m.start()-8000):m.start()] or True: print('*',s);print()\nEOF\n}; ety fa5aca5687e59d7e.txt x | sed -n '1,40p' | grep -A1 -i 'persian\\|Middle Persian' | head -20"
}
```


### [2026-10-16T05:14:42.858Z] TOOL RESULT

```
* Etymology [ edit ] Borrowed from Pashto باد , from Persian باد . Noun [ edit ] باد ( bād ) suffering from chronic joint , bone pain Ottoman Turkish [ edit ] Etymology [ edit ] Etymology tree Proto-Indo-European *h₂weh₁- Proto-Indo-European *-ti Proto-Indo-European *h₂wḗh₁ti Proto-Indo-European *h₂wéh₁n̥ts Proto-Indo-Iranian *HwáHatas Proto-Iranian *HwáHatah Persian باد ( bâd ) bor. Ottoman Turkish باد Borrowed from Persian باد ( bâd , “ wind; air ” ) , from Proto-Iranian *HwáHatah ( “ wind ” ) . Noun [ edit ] باد • ( bâd ) ( definite accusative بادی ( bâdı ) , plural بادلر ( bâdlar ) ) wind , the real or perceived movement of atmospheric air us

* Etymology [ edit ] Etymology tree Proto-Indo-European *h₂weh₁- Proto-Indo-European *-ti Proto-Indo-European *h₂wḗh₁ti Proto-Indo-European *h₂wéh₁n̥ts Proto-Indo-Iranian *HwáHatas Proto-Iranian *HwáHatah Persian باد ( bâd ) bor. Ottoman Turkish باد Borrowed from Persian باد ( bâd , “ wind; air ” ) , from Proto-Iranian *HwáHatah ( “ wind ” ) . Noun [ edit ] باد • ( bâd ) ( definite accusative بادی ( bâdı ) , plural بادلر ( bâdlar ) ) wind , the real or perceived movement of atmospheric air usually caused by convection or differences in air pressure Synonyms: روزكار ( rüzgâr ) , ریح ( rih ) , یل ( yel ) air , the substance constituting Earth 's atmosphere , a g

* Etymology [ edit ] Borrowed from Classical Persian باد ( bād ) . Doublet of وو ( wō ) . Pronunciation [ edit ] IPA ( key ) : /bɑd/ Noun [ edit ] باد • ( bād )  m wind Further reading [ edit ] Raverty, H. G. ( 1867 ), “ باد ”, in A dictionary of the Puk'hto, Pus'hto, or language of the Afghans: with remarks on the originality of the language, and its affinity to other oriental tongues , London: Williams & Nortgate Persian [ edit ] Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ˈbaːd/ ( Dari, formal ) IPA ( key ) : [bɑːd̪] ( Dari, formal ) IPA ( key ) : [bɑːd̪] ( Kabuli ) IPA ( key ) : [bɑːd̪] ( Hazaragi ) IPA ( key ) : [bɔːd̪̥] ( Iran, 

* Etymology 1 [ edit ] From Middle Persian wād , from Old Persian *vātah , from Proto-Iranian *HwáHatah , from Proto-Indo-Iranian *HwáHatas , from Proto-Indo-European *h₂wéh₁n̥ts ( “ wind ” ) . [ 1 ] Noun [ edit ] Dari باد Iranian Persian Tajik бод باد • ( bād / bâd ) ( Tajik spelling бод ) wind باد شرق ― bâd -e šarq ― east wind باد تند ― bâd -e tond ― harsh wind سرو در باد ارتعاش داشت. ― sarv dar bâd erte'âš dâšt. ― The cypress trembled in the wind . air Synonym: هوا ( havâ ) ( medicine ) inflammation ; swelling ( medicine ) windiness ( colloquial ) pride Synonym: غرور ( ġorur ) با باد و فیس ― bâ bâd o fis ― with pride and haughtiness Derived terms 

* Etymology 2 [ edit ] Shortened form of بواد ( bovâd ) , from Middle Persian [Book Pahlavi needed] ( bawād ) , an old inherited optative form. Verb [ edit ] باد • ( bâd ) ( poetic , literary ) Third-person singular present optative of بودن ( budan ) . شرم بر شما باد ― šarm bar šomâ bâd! ― Shame be upon you! Synonyms [ edit ] باشد ( bâšad ) ( subjunctive form that has some overlap in meaning) Descendants [ edit ] → Urdu: بَاد ( bād ) References [ edit ] ^ Nourai, Ali ( 2011 ), An Etymological Dictionary of Persian, English and other Indo-European Languages , page 496 Urdu [ edit ] Etymology 1 [ edit ] Borrowed from Classical Persian باد ( bād , “ wind;

* Etymology 1 [ edit ] Borrowed from Classical Persian باد ( bād , “ wind; air ” ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /bɑːd̪/ Noun [ edit ] باد • ( bād )  f air wind ; breeze ; gale Derived terms [ edit ] بادِ بَہار ( bād-e-bahār , “ spring breeze ” ) بادِ عِیسیٰ ( bād-e-'īsa , “ skillful physician ” , literally “ breath of Jesus ” ) بادِ ہَوائی ( bād-e-havāī , “ meaningless, useless ” , literally “ wind of wind ” ) Etymology 2 [ edit ] Borrowed from Classical Persian بَاد ( bād ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /bɑːd̪/ Verb [ edit ] بَاد • ( bād ) ( Hindi spelling बाद ) Let it be , may it be 195

* Etymology 2 [ edit ] Borrowed from Classical Persian بَاد ( bād ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /bɑːd̪/ Verb [ edit ] بَاد • ( bād ) ( Hindi spelling बाद ) Let it be , may it be 1952 , “ Qaumi Taranah ”, Hafeez Jalandhari (lyrics), Ahmed Ghulam Ali Chagla (music): پاک سرزمین شاد باد کشورِ حسین شاد باد تُو نشانِ عزمِ عالی شان ارضِ پاکستان! مرکزِ یقین شاد باد Pāk sar zamīn śād bād Kiśvar-e-hasīn śād bād Tū niśān-e-azm-e-ālī śān Arz-e-Pākistān! Markaz-e-yaqīn śād bād Blessed be the sacred land, Happy be the bounteous realm. Thou symbol of high resolve, O Land of Pakistan! Blessed be the citadel of faith. References [ edi
```


## [2026-10-16T05:14:47.929Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; first(){ python3 - \"$1\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1]).read()\nlines=[l.strip() for l in t.split('\\n') if l.strip()]\nj=' '.join(lines)\nms=[m.start() for m in re.finditer(r'Etymology( \\d)? \\[ edit \\]',j)]\nfor s in ms[:2]: print('*',j[s:s+650]);\nEOF\n}; for f in dd8b45b8174956ae b4e6a62d999564e6 cc15bb57c26a563d 4a3552cbf8ec3dee 0a26bcaab38fd1de 504951ddb6f88669 c87ce7e176ebcf1c c9f38fb2d03b8d85 def0da40ecd94485 5da585b195df37a2 169d7e0177f26d8e; do echo \"=== $f $(sed -n 1p $f.txt)\"; first $f.txt; done"
}
```


### [2026-10-16T05:14:48.918Z] TOOL RESULT

```
=== dd8b45b8174956ae URL: https://en.wiktionary.org/wiki/wind
* Etymology 1 [ edit ] From Middle English wynd , wind , from Old English wind ( “ wind ” ) , from Proto-West Germanic *wind , from Proto-Germanic *windaz , from Proto-Indo-European *h₂wéh₁n̥tos ( “ wind ” ) , from earlier *h₂wéh₁n̥ts ( “ wind ” ) , derived from the present participle of *h₂weh₁- ( “ to blow ” ) . Cognates Cognate with Yola weend , wyeene ( “ wind ” ) , North Frisian win , winj ( “ wind ” ) , Saterland Frisian Wíend ( “ wind ” ) , West Frisian wyn ( “ wind ” ) , Alemannic German wend , wind , winn , wénn ( “ wind ” ) , Bavarian bint , Wind ( “ wind ” ) , Cimbrian and Mòcheno bint ( “ wind ” ) , Dutch wind ( “ wind ” ) , German 
* Etymology 2 [ edit ] From Middle English wynden , from Old English windan , from Proto-Germanic *windaną . Compare West Frisian wine , Low German winden , Dutch winden , German winden , Danish vinde , Walloon windea . See also the related term wend . Pronunciation [ edit ] enPR : wīnd , IPA ( key ) : /waɪnd/ ( Standard Southern British ) IPA ( key ) : /wɑjnd/ Audio ( US ) : ( file ) Rhymes: -aɪnd Homophones : wined , whined ( wine – whine merger ) Verb [ edit ] wind ( third-person singular simple present winds , present participle winding , simple past and past participle wound or winded ) ( transitive ) To turn coils (of a cord or something 
=== b4e6a62d999564e6 URL: https://en.wiktionary.org/wiki/weather
* Etymology [ edit ] From Middle English weder , wedir , from Old English weder , from Proto-West Germanic *wedr , from Proto-Germanic *wedrą , from Proto-Indo-European *wedʰrom (= *we-dʰrom ), from *h₂weh₁- ( “ to blow ” ) . Cognates Cognate with Scots wather ( “ weather ” ) , Saterland Frisian Weeder ( “ weather ” ) , Cimbrian bèttar ( “ weather ” ) , Dutch weder , weer ( “ weather ” ) , German Wetter ( “ weather ” ) , Low German Weder ( “ weather ” ) , Luxembourgish Wieder ( “ weather ” ) , Yiddish וועטער ( veter , “ weather ” ) , Danish vejr ( “ weather ” ) , Faroese , Icelandic veður ( “ weather ” ) , Norwegian Bokmål vær ( “ weather ” ) ,
=== cc15bb57c26a563d URL: https://en.wiktionary.org/wiki/window
* Etymology [ edit ] Etymology tree Proto-Indo-European *h₂weh₁- Proto-Indo-European *-ti Proto-Indo-European *h₂wḗh₁ti Proto-Indo-European *h₂wéh₁n̥ts Proto-Germanic *windaz Old Norse vindr Proto-Indo-European *h₃ekʷ- der. Proto-Germanic *augô Proto-Norse *ᚨᚢᚷᚨ ( *auga ) Old Norse auga Old Norse vindauga bor. Middle English wyndowe English window From Middle English wyndowe , wyndown , from Old Norse vindauga ( “ window ” , literally “ wind-eye; wind-hole ” ) , equivalent to wind +‎ eye . Cognate with Scots windae and windock , Faroese vindeyga , Norwegian Bokmål vindu , Norwegian Nynorsk vindauge , Danish vindue , archaic Swedish vindöga , El
=== 4a3552cbf8ec3dee URL: https://en.wiktionary.org/wiki/wing
* Etymology [ edit ] Etymology tree Old Norse vængr bor. Middle English winge English wing From Middle English winge , wenge , from Old Norse vængr ( "wing of a flying animal, wing of a building"; compare vængi ( “ ship's cabin ” ) ) , from Proto-Germanic *wēingijaz , from Proto-Indo-European *h₂weh₁- ( “ to blow ” ) , thus related to wind . Cognate with Danish , Norwegian Bokmål , and Swedish vinge ( “ wing ” ) , Elfdalian waingg ( “ wing ” ) , Faroese vongur ( “ wing ” ) , Icelandic vængur ( “ wing ” ) , Norwegian Nynorsk veng ( “ wing ” ) . Replaced native Middle English fither (from Old English fiþre , from Proto-Germanic *fiþriją ), which 
* Etymology [ edit ] (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . Particularly: “Onomatopoeic?”) Pronunciation [ edit ] Cantonese ( Jyutping ) : wing 1 Cantonese ( Standard Cantonese , Guangzhou – Hong Kong ) + Jyutping : wing 1 Yale : w ī ng Cantonese Pinyin : wing 1 Guangdong Romanization : wing 1 Sinological IPA ( key ) : /wɪŋ ⁵⁵ / Adjective [ edit ] wing ( Hong Kong Cantonese , slang , of person ) intoxicated ; tipsy Synonyms [ edit ] stone Middle English [ edit ] Noun [ edit ] wing alternative form of winge Tok Pisin [ edit ] Etymology [ edit ] From English wing . Noun [ edit ] wi
=== 0a26bcaab38fd1de URL: https://en.wiktionary.org/wiki/vent
* Etymology 1 [ edit ] Partly from Middle French vent , from Latin ventus and partly from French éventer . Cognate with French vent and Spanish viento ( “ wind ” ) and ventana ( “ window ” ) . Doublet of wind . Noun [ edit ] vent ( plural vents ) A vent (opening) in the wall of a house. An opening through which gases , especially air , can pass. Synonym: outlet the vent of a cask; the vent of a mould 2014 , Elizabeth Kolbert , The Sixth Extinction: An Unnatural History , Picador, →ISBN , page 122 : According to geologists who work in the area, the vents at Castello Aragonese have been spewing carbon dioxide for at least several hundred years, m
* Etymology 2 [ edit ] Clipping of ventriloquism . Noun [ edit ] vent ( plural vents ) Ventriloquism . Derived terms [ edit ] vent puppet Etymology 3 [ edit ] From French vente , from Latin vendere ( “ to sell ” ) . Verb [ edit ] vent ( third-person singular simple present vents , present participle venting , simple past and past participle vented ) To sell ; to vend . 1614 , Walter Ralegh [ i.e. , Walter Raleigh ], The Historie of the World   [ … ] , London: [ … ] William Stansby for Walter Burre ,   [ … ] , →OCLC , (please specify |book=1 to 5) : Therefore did those nations [ … ] vent such spice. Etymology 4 [ edit ] From Spanish venta ( “ a 
=== 504951ddb6f88669 URL: https://en.wiktionary.org/wiki/fan
* Etymology [ edit ] Clipping of English Fan g . Symbol [ edit ] fan ( international standards ) ISO 639-2 & ISO 639-3 language code for Fang (Bantu) . See also [ edit ] Wiktionary’s coverage of Fang (Bantu) terms English [ edit ] English Wikipedia has an article on: fan Wikipedia Pronunciation [ edit ] ( Received Pronunciation , General American without /æ/ raising ) IPA ( key ) : /fæn/ Audio ( Northwestern US ) : ( file ) ( Standard Southern British ) IPA ( key ) : /fan/ , /faːn/ Audio ( Southern England ) : ( file ) ( Northern England , Scotland , Wales ) IPA ( key ) : /fan/ ( Australia ) IPA ( key ) : /fæːn/ ( General American , /æ/ raising
* Etymology 1 [ edit ] Handheld fans . An electrical fan . A ceiling fan . Inherited from Middle English fan , inherited from Old English fann ( “ a winnowing, fan ” ) , derived from Latin vannus ( “ fan for winnowing grain ” ) , derived from Proto-Indo-European *h₂weh₁- ( “ to blow ” ) . Cognates Latin ventus ( “ wind ” ) Dutch wan ( “ winnowing basket ” ) German Wanne ( “ winnowing basket ” ) Swedish vanna ( “ a fan for winnowing ” ) Old English windwian ( “ to fan, winnow ” ) . More at winnow . Noun [ edit ] fan ( plural fans ) A hand-held device consisting of concertinaed material, or slats of material, gathered together at one end, that ma
=== c87ce7e176ebcf1c URL: https://en.wiktionary.org/wiki/air
* Etymology [ edit ] Clipping of English Air oran . Symbol [ edit ] air ( international standards ) ISO 639-3 language code for Airoran . See also [ edit ] Wiktionary’s coverage of Airoran terms English [ edit ] English Wikipedia has an article on: air (disambiguation) Wikipedia A hot air balloon partially inflated with air. The composition of air. Alternative forms [ edit ] aire , ayre , eyr ( obsolete ) ayr ( especially music ) Pronunciation [ edit ] ( non-rhotic ) ( Received Pronunciation ) IPA ( key ) : /ɛə̯/ Audio ( UK ) : ( file ) ( Standard Southern British , General South African ) IPA ( key ) : /ɛː/ ( Lancashire , fair – fur merger ) I
* Etymology 1 [ edit ] Etymology tree Proto-Indo-European *h₂ews- Proto-Indo-European *-r Proto-Indo-European *h₂ewsér Proto-Hellenic *auhḗr Ancient Greek ᾱ̓ήρ ( āḗr ) bor. Latin āēr Old French air bor. Middle English aire English air From Middle English aire , from Old French air , from Latin āēr , from Ancient Greek ἀήρ ( aḗr ) . Displaced native Old English lyft . More at lift , loft . Noun [ edit ] Wikidata has a Lexeme related to: air (L1038) air ( countable and uncountable , plural airs ) ( uncountable ) The substance constituting Earth 's atmosphere : a gaseous mixture of nitrogen , oxygen , and various trace gases. This drill runs on co
=== c9f38fb2d03b8d85 URL: https://en.wiktionary.org/wiki/malaria
* Etymology [ edit ] Borrowed from Italian malaria , formed from mal- ( “ bad ” ) and aria ( “ air ” ) . Introduced into English by the Scottish geologist John MacCulloch (1773–1835). Displaced native Old English unlyft ( literally “ bad air ” ) . Pronunciation [ edit ] IPA ( key ) : /məˈlɛəɹi.ə/ Audio ( US ) : ( file ) Audio ( Southern England ) : ( file ) Rhymes: -ɛəɹi.ə Noun [ edit ] malaria ( countable and uncountable , plural malarias ) ( pathology ) A disease spread by mosquito , in which a protozoan , Plasmodium , multiplies in blood every few days. Synonyms: ague , ( archaic ) paludism ( archaic ) Supposed poisonous air arising from mar
* Etymology [ edit ] Inherited from Spanish malaria ( “ malaria ” ) . Pronunciation [ edit ] Hyphenation: ma‧la‧ria Noun [ edit ] malaria malaria Danish [ edit ] Etymology [ edit ] From Italian malaria . Noun [ edit ] malaria   c ( singular definite malariaen , not used in plural form ) ( pathology ) malaria Dutch [ edit ] Pronunciation [ edit ] Audio : ( file ) Hyphenation: ma‧la‧ria Noun [ edit ] malaria   f ( uncountable , no diminutive ) malaria Descendants [ edit ] → Caribbean Hindustani: maláriyá Finnish [ edit ] Finnish Wikipedia has an article on: malaria Wikipedia fi Etymology [ edit ] Borrowed from Italian malaria . Pronunciation [ ed
=== def0da40ecd94485 URL: https://en.wiktionary.org/wiki/atmosphere
* Etymology [ edit ] Etymology tree Ancient Greek ἀτμός ( atmós ) der. French atmo- Ancient Greek σφαῖρᾰ ( sphaîră ) bor. Latin sphaera Late Latin sphēra French -sphère French atmosphère bor. English atmosphere Borrowed from French atmosphère , from New Latin atmosphaera , from Ancient Greek ἀτμός ( atmós , “ steam ” ) + σφαῖρα ( sphaîra , “ sphere ” ) ; corresponding to atmo- +‎ -sphere . Pronunciation [ edit ] ( Received Pronunciation , Australia ) IPA ( key ) : /ˈætməsˌfɪə/ ( Standard Southern British ) IPA ( key ) : /ˈatməsˌfɪː/ , /ˈatməsˌfɪj.ə/ Audio ( UK ) ; /ˈatməsˌfɪː/ : ( file ) ( US ) IPA ( key ) : /ˈætməsˌfɪɹ/ Audio ( US ) : ( file )
=== 5da585b195df37a2 URL: https://en.wiktionary.org/wiki/nirvana
* Etymology [ edit ] Borrowed from Sanskrit निर्वाण ( nirvāṇa , “ blown or put out, extinguished ” ) , from निस् ( nis , “ out ” ) +‎ वा ( vā , “ to blow ” ) , the second part cognate with Russian ве́тер ( véter , “ wind ” ) , weather , vent and wind . Pronunciation [ edit ] ( India ) IPA ( key ) : /nɪrˈvɑːn(ɑː)/ ( Received Pronunciation , Australia ) IPA ( key ) : /nɪəˈvɑː.nə/ , /nəˈvɑː.nə/ Audio ( Australia ) : ( file ) ( General American ) IPA ( key ) : /nɪɹˈvɑ.nə/ , /nəɹˈvɑ.nə/ , /nəɹˈvæn.ə/ Audio ( US ) : ( file ) Rhymes: -ɑːnə , -ɑːn Noun [ edit ] nirvana ( countable and uncountable , plural nirvanas ) English Wikipedia has an article on:
* Etymology [ edit ] Borrowed from Sanskrit निर्वाण ( nirvāṇa , “ blown or put out, extinguished ” ) , from निस् ( nis , “ out ” ) +‎ वा ( vā , “ to blow ” ) . Pronunciation [ edit ] IPA ( key ) : /ˈnirʋɑnɑ/ , [ˈnirʋɑ̝nɑ̝] Rhymes: -irʋɑnɑ Syllabification ( key ) : nir‧va‧na Hyphenation ( key ) : nir‧va‧na Noun [ edit ] nirvana nirvana Declension [ edit ] Inflection of nirvana ( Kotus type 12/ kulkija , no gradation) nominative nirvana nirvanat genitive nirvanan nirvanoiden nirvanoitten partitive nirvanaa nirvanoita illative nirvanaan nirvanoihin singular plural nominative nirvana nirvanat accusative nom. nirvana nirvanat gen. nirvanan genitive 
=== 169d7e0177f26d8e URL: https://en.wiktionary.org/wiki/ventus
* Etymology 1 [ edit ] Inherited from Proto-Italic *wē̆ntos , from Proto-Indo-European *h₂wéh₁n̥ts ( “ blowing ” ) , present participle of *h₂weh₁- ( “ to blow ” ) . Etymology issues The term is often cited as an example of Osthoff's law, which predicts shortening of long vowels when followed by a resonant and then a consonant. Thus, the thematicized pre-form *h₂weh₁n̥tos could have yielded *wēntos , [ 1 ] which would have eventually shortened into *wentos . [ 2 ] However, the existence of Osthoff's law in Latin is disputed, and one alternative proposal suggests that *h₂weh₁n̥tos would have instead directly yielded *wentos . According to this t
* Etymology 2 [ edit ] Inherited from Proto-Italic *gʷemtus , from Proto-Indo-European *gʷém-tu-s , from *gʷem- ( “ to come ” ) . The -n- was, according to De Vaan, potentially adopted from the verb veniō ( “ to come ” ) . By surface analysis , veniō +‎ -tus ( forming action nouns ) . Noun [ edit ] ventus   m ( genitive ventūs ) ; fourth declension ( Old Latin , dubious hapax legomenon ) a coming ; an arrival 116 BCE – 27 BCE , Marcus Terentius Varro , De Lingua Latina 5.72 (quoting Plautus, Cistellaria 14-15): Venilia a veniendo, ac ventu illo, quem Plautus dicit: Quod ille dixit, qui secundo vento vectus est tranquillo mari, ventum gaudeo. [
```


## [2026-10-16T05:14:54.770Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'vāta-\\|vata- \\|\"wehen\"\\|wehen' BRT.txt | head -20; grep -n -i 'antar.*vā\\|antar.*vay\\|antarə' BRT.txt | head -20"
}
```


## [2026-10-16T05:14:55.779Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^wind,\\|^window,\\|^wing,\\|^nirvana,\\|^weather,\\|^atmosphere,\\|^malaria,\\|^air,\\|^vent,\\|^fan,' KLN_1966.txt | head -20"
}
```


### [2026-10-16T05:14:56.124Z] TOOL RESULT

```
2051:air,  n.,  atmosphere.  —  ME.  aire,  fr.  OF.  (—  F.) air,  fr.  L.  aer  (whence  also  Rum.  aer,  OProveng., Catal.,  Sp.  aire.  Port,  air,  ‘air’),  which  derives fr.  Gk.  df)p,  gen.  l)tpoQ,  Att.  gen.  aepop,  ‘air’ (from  the  Att.  acc.  a£pa  is  borrowed  It.  aria, ‘air’).  Gk.  dr,p  (cp.  the  parallel  forms  Aeol. otuTjp,  Dor.  dfWjp)  and  the  rel.  aopx,  ‘air  in motion,  breeze’,  are  of  uncertain  origin.  They are  possibly  rel.  to  deipciv,  ‘to  lift  up,  raise’, and  lit.  mean  ‘that  which  rises’.  See  aorta,  and cp.  aerate,  aerial,  aero-,  the  first  element  in aerostat,  and  the  second  element  in  malaria. Derivatives:  air,  v.,  air-able,  adj.,  air-er,  n.,  air¬ ing,  n.,  air-less,  adj.,  air-y,  adj.,  air-i-ly,  adv., air-i-ness ,  n.
2052:air,  n.,  melody,  tune.  —  F.,  fr.  It.  aria,  of  s.m., fr.  L.  aerea,  fern,  of  the  adjective  aereus,  ‘per¬ taining  to  the  air’,  fr.  aer,  ‘air’.  See  prec.  word
14355:fan,  n.,  an  enthusiastic  supporter  of  any  sport, esp.  of  base-ball  (U.S.  Slang).  —  Shortened  fr. fanatic.
28684:wind,  bubble’,  from  the  imitative  base  *pu-, *phu-,  ‘to  blow,  swell’,  whence  also  L.  pustula, ‘blister,  pimple,  pustule’.  See  pustule  and  -ia  and cp.  the  next  two  words.  Cp.  also  emphysema. Physalis,  n.,  a  genus  of  plants,  the  ground-cherry (bot.)  —  ModL.,  fr.  Gk.  9U3aX (X)i;,  ‘bladder; a  plant  with  a  bladderlike  calyx’.  See  prec. word.
41230:vent,  n.,  1)  the  act  of  selling;  2)  market  for  sale. —  MF.  (=  F.)  venfe, ‘sale’.fr.VL.  vendita,' sale’, prop.  fern.  pp.  of  L.  vendere,  ‘to  sell’,  used  as  a noun.  Cp.  It.  vendita,  Sp.  venta,  which  also  de¬ rive  fr.  VL.  vendita,  and  see  vend.  Cp.  also  next word.
```


### [2026-10-16T05:14:56.133Z] TOOL RESULT

```
2964:vgl-  evata-  Adj.  'inferior'  (wozu  aera-  wie  Ht.  |  ^  püZ.^';  —  yahmat  haca  naicU  bunjayät
4013:•  j.  a-fraka'8avata-  Adj,  (fem.  'vai(i-)'^ 'nicht  vorwärts,  fort,  von  der  Stelle  zu rütteln,  unverrückbar' :  «r  Aim  (näml. dngnam)  dasta  ..  -vaitim  Yt.  ij.  100.
16912:•heftig  wehen,  stürmen':  vännü  v3  sna!- zinü  (sd.)  vs  barfftti  (LS.)  vä  .  .  ayan V.Ä4.
18306:•  j.  frOT«ntay-  f.  'Heranlcommen,  (vom Wind)  -wehen',  mit  Akk.  der  Richtung: aäkä  dim  vatayA  °r>nta  (LS.)'*  satayäti yä  hava  daeaa  "indem  sie  (die  Seele)  dieser Wind  anweht,  wird  das  eigene  Ich  sicht- bar" H,  2.  9.
22204:Rede:  at  J  (Sp.  11  m.)  vaocat  ahurS  .  ..■ nüif  .  .  Y.  2(J.  6;  —  yezica  vaocät  alsa  yä kaine:  faä:r»m  isd.)  alm  ..varsta  V.75. 13; 13.  a)  mit  Dat.  der  Person:  sat  vao- iät  ratul . .  mazJayasnagibyS:  maadayaina (Vok.)  ..  V.tf.  II.  3)  mit  Objektsakk.: ya'hä  iü  T  *ahuramazää  mSnghaca  vaocasifl däscä  varfscä  ya  vohu  aha  .  .  V.  J^.  4; —  /a(  0/  vainmaidi . .  hyat  I  mainimadicä vaocdimäcS  vsnzimäiä  yä  .  .  vakisiä  Y. JJ.  3;  —  tarahuslrahe  .  .  paoiryai  vohu mamnanai  .  .  vaokuSe  .  .  vävinzuh  Yl 13. 87  f. ;  —  ySi  nsii  ih3  mqhnm  vanssnti (sd.)  ya%S  Tm  mSnai^a  vai>ea(K.onj.)£ä Y.45.  3i  —  ai  sl  i"Ä(ADn.)  vaxs'ya  (iS.) mazdä,  vidull  zT  na  mruyai  (Sp.  1193  u.) Y.5/.8.  a)  zugleich  mit  o)  Akk.  der Person:  at  tä  vaxsya  üints  (Sp.  29  o.)  . . mazda^a  Y.  ?o.  t.  ß)  Dat  der  Person: y7  mlH  viäva  vaocäl  haihim  mähnm  .  , ampnitaias{sd.)ca  Y.^1.6;  —  *>'?*'  '''^' vTdvä  mazdä  vaocat  Y.  1^5. 3;  —  masda at  mSi  vahilta  sraväslä  .  .  vaocä  (Imp.) tä  .  .  asacä  iiudfm  (sd.)  Y,  j4. 15;  —  mit finalem  Inf. :  tat  nS  mazdä  vldvanöi  (sd.) vaola  hizvä  %'waAya  araks  Y.31. 3 ;  5 ;  —  in pass.  Wendung  :_)'as'4vö  mazdä  %wSi  va^äl daena  Y,  44. 11;  —  »n/  mdi  tneBcam  ^  vata- hJuI  va/u/(sd.)  manarahs  Y.  48. 9.  3)  mit wie?-Adv.slattObj.:  (is  mainyü  mamanäiti , .  vaocätari . .  vävjnzätarS  Y.  ly.  4 ;  —  *yal neit  yava  mihS  mamne  .  .  vavaü  .  .  va- variza  P.  iS;  —  tat  hwä  pinsa  (sd.)  fnS
22765:niVi  paiti    'umstürzen,   zu  Grunde  rieh-;  —  visptm  a  ahmäl  yal  alte  narB  "'rt/^iHt ten,  vernichten';    mi^rtm  ..yd    doi^Afus .(LP.)''  anh^n  V.2.28. raxryaihyS  paiti  s^armä  värayäti  "..der       Zum  V.  "for-.    —    ai.  vgl.  vata-  m.  'Raum';
23196:ai.  vihati,  ukyäte  (Praet.  37,  Fass.]^  uhl,  vaksai; ; udhäh,  vähadhyai;  mp.  voiSlan  'dahin fahren', , rp.  i'.ijrH'fl« 'wehen',  afj.  po/ii/ 'fliegen' (Praes.  I vuzt],  sbal,  gvcaag,  ZDg.  vailmün  'laufen'.  — Pü. !  vaätan,  vazemlan;  s.  noch  No.  6  ff-  —  ' I)  Nur  im  Abiol.  —  '>  S  W  H;  »■  dagegen  • ai.  üijh^.  —  »  S  /a/  g.  Wertlos  Wilhelm  | Mus.  3.  600.  —  4)  Stall  vaänii,  lu  S  325  No.  ■ S.  hindav-  No.  I.  —  s)  Them.  —  &)  Pü. : vastnit;  s.  zu  vaou  Inf.  —  7)  Es  handelt  sich  | Dm  einen  Kamof,  bei  dem  die  Entscheidung nicht  fallen  will.  Anders  Gdn.  sYI.Si,  Dst. ZA.  3.  572.  Npü.  (fOc  vailiakS):  ml gardadA —  S)  Pü.:  nap  an  (Mills  iivawfn),  Sü.:  svämi-^ iämitü.  —  9>  Unsicher;  vlL  haplol,  für *avcaa>:  —  ")  Fehlt  in  Pü.  —  ")  Pü.  erL; buland  e  sar  .  .  fröt  ö  bun.
23407:•  j.  'vä-  V.  'wehen'  vom  Wind.  Praes.  i
23409:'wehen':  kudaiarm  vatö  vaiti  ytm  . . "woher  weht  hier  der  Wind,  den  . ."  H. 2.  (?,  26;  —  vaa  vänti  dunmS.frutS  (sd.) Yty.14.
23410:mit  aiwi  'herzuwehen':  aiwi^a  vUta  vänlt *yaoxstivantS  Yt.  Ä  8.
23411:mit  antan  und  fra  'herzuwehen  hinein unter  — '  (Akk.):  yat  Al/  antan  väts  fra- väiti  "wenn  unter  sie  hinein  der  Wind heranweht"  Yt  13. 46.
23412:mit  a  und  upa  'herzuwehen  an  -  (Akt), anwehen':  a  dim  vatö  tipa.vavS()iSm.)'^ sahayeiti  <sd.)  H.2.7,  35.
23437:vata-  1408
25591:•  g.  'urvata-  n.  'Bestimmung':  kyaf  °t»m lasdinifki'adibyS  "was  die  Bestimmung  für die  Verständigen  (ist)"  Y.jr.  3".
25595:•  j.  'urvata-  Adj.  -  ?  -,  bezeichnet  eine gute  Eigenschaft  des   Kameb:   uitramim •«{statt  GP.)'>  samiJiao/anqm    \.22'.y, —  ttstmhe . .  aiwijaanahe  'tu  (statt  GS.) frasparanahe  \\.14.\\.
27477:•  j.  surunvata-  Adj.  'hörbar,  laut*:  hm yasai  °ta  yasna  sraoSifn  .  .  taokräiyU  Y. 57-3;  Vt.^.i8,  s.<).
29217:•  j.  hadra-vata-  n.  'auf  einmal,  auf  einen Schlag  erfolgender  Sieg  über  — '  (Gen.): •tahela  paiti    hamtnä^anqm    Yt  13.  133,
7140:—  yat  titarat  (sd.)  attrö  tnaittyus  duhjm alahe  . .  antar)  pairi.avsilim  vohula  tnanö "tarsca  ta  hc  taurvayattm  tba!sa  Yt.  13. 7 7 f.*';  —  asim  vahütim  'tnmca  Y.2.4; 7.4,  A.  4.2,  S.  7. 7,  2.7;  —  xmümaine  ahu- rahe mazdä  am»sanqm  spintaiiqm  sraosahe afyehe  °^riJ  Y.  22. 4;  —  mana/a  yastum yat  ahurahe  mazdä  'hrascd  "S.^ff;  — haurvata  anitrstätä  ,  .  gjui  tarne  gfus itrwie  ..    "'hre  Y.JO.2;    7.2,  Vr.p-S;  —
15582:i  si'afranqm  . .  daüanqm  . .  *siß-a- nqm  (Tjanqmca  'Aaaqm  Vt  13. 104;  — •kam  yqm  *xnqiaiH  (sd.)  yä  upartha^at ksnsasfim  V.  /.  9;  ig.  5.  a)  von  Tistryt bekämpft**':  aam  da^qm  .  .  tiltnm  . ODaiiihäi  'kayäi  paitistätayaica  .  .  yi duzyäirya  Yt  &  50  f.;  —  'ka  yä  duiyäirya . .  parsit  pairikiWH  (sd.)  aaki'qm  ava.- kisiayai  .  .  tislryO  . .  avqm  'kqm  ädan- tayäti  YL&S4f,;  —  tiärim  .  .  yJ  'ki tat/rvayeiti  yö  *kä  titärayeiti  yä  stärS ktrsmh  (sd)  patanti  antar7  sqm  asma- n»Mca  Yt  8. 8  ">.  A)  sonst  in  Verbin- dung natyätav-  (sd.,  auch  fdSt):  ya^  mqm nalAs  taurvayJl  . .  nSit  yätavS  naiöa  *ka Yt/. 6;  usw.;  —  paiti.ptnm  ..  vlspe yStavö  'käsca  vispa  *janayä  yä  drvaitis  V. 20.  jo;  usw.;  —  paitistälse  yätunqm  °ka- nqmia  Yt  6.  4;  usw.;  —  Aaia  "yäiai  haca *käi  Yt4-3; — yätulcä  ystumalqm  'iäsöi pairikavatqm  Yt  11. 6.
28639:asti  ap»ntii  kal  hl  asti  yaoidä'knml . .  nava  he  asti  aha  nava  hl  asti  äpiritii^ nBit  hl  asti  yaozdähnm  V.^,38f.;  36,! tf.  107'.  Z)  auf  ein  Nomen  voraus- weisend: nöit  he  aosö  pairi.vam3mi\ zarahustrai  V.lff.s;  —  ^J  .  .  uia  hl' itsnpfn  xratßm  ava.baraiti  .  ,  uta  hl  .  .\ ziayantsi  jasaiti  avanhe  Yt.  J7.  2 ;  —  para  ' hl  iris)nts  ralsim  Hkayat  V.  7.  38;  —  ■ pairi  /?(Plur.)  hs parit3.tanunam  starshaiti ; N.42;  — yS  hl  *ap}rm?mnai  (Sp.  869  o.) nsil  visäiti  *framrüite  N.  y;  —  zugleich zurückweisend:  yat  litaral  anrö  main- yu} . .  antar?  pairi  avätüm  vohuca  manS älarsca;  tä  hl  taurvayaigm  lialsä  atsraht mainyiul  Yt,  iS-77('<  —  pasvö  staoräca .  ,  ottaAmai  naire  frabäraym;  yezi  nöit tavqn  .  .  anyqm  hl  avantqm  altahmäi naire  frabäraytn    V.  g.  39.  Anhang
```


## [2026-10-16T05:15:00.163Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o '.\\{0,20\\}\\(wind,  n\\|window,  n\\|wing,  n\\|nirvana,  n\\|Nirvana,  n\\|weather,  n\\|atmosphere,  n\\|malaria,  n\\|vent,  n\\|fan,  n\\).\\{0,600\\}' KLN_1966.txt | cut -c1-800 | head -20"
}
```


### [2026-10-16T05:15:07.164Z] TOOL RESULT

```
1742:advent,  n.  —  L.  adventus,  ‘arrival’,  fr.  advent- ( um ),  pp.  stem  of  advenire.  See  prec.  word, adventitious,  adj.,  casual.  —  L.  adventicius, ‘coming  from  abroad,  extraneous,  foreign’,  fr. advent-(um),  pp.  stem  of  advenire.  See  advent and  -itious.
2760: 'qzosti,  ‘a  narrowing,  nar¬ rowness’,  qziiku,  ‘narrow’,  Lith.  ahkstas,  ‘nar¬ row’,  fr.  I.-E.  base  *angh-,  ‘to  narrow,  com¬ press’  ;  the  corresponding  Celtic  base  is  *engh-, *%gh-,  whence  Bret,  enk ,  ‘narrow’,  Ir.  cumung, ‘narrow’,  Ir.,  W.  ing,  ‘distress’.  Cp.  agnail,  an¬ gina,  anguish,  anxious,  and  the  second  element in  cynanche,  quinsy,  squinancy,  Orobanche. Derivatives:  angr-y,  adj.,  angr-i-ly,  adv.
3859:.,  atmometr-y,  n. atmosphere,  n.  —  Compounded  of  Gk.  dxpop, ‘steam,  vapor’,  and  cnpoupa,  ‘ball,  sphere’;  see atmo-  and  sphere.  The  word  atmosphere  was  first used  by  the  English  bishop  and  scientist  John Wilkins  (1614-72)  in  1638  with  reference  to  the moon  (which  in  reality  has  no  atmosphere). Derivatives :  atmospher-ic,  atmospher-ic-al,  adjs., atmospher-ic-al-ly,  adv.,  atmospher-ics,  n.pl. atocia,  n.,  sterility  of  the  female  (med.)  —  Medi¬ cal  L.,  fr.  Gk.  axoxla,  ‘sterility’,  fr.  6x0x04, having  never  yet  brought  forth’,  fr.  4-  (see  priv. pref.  a-)  and  XOX
4642:iti, ‘blows’;  see  wind,  n.  For  the  second  element see  rose.
9045:convent,  n.  —  L.  conventus,  ‘meeting,  assembly’, lit.  ‘a  coming  together’,  fr.  conventus,  pp.  of  con¬ vent re\  see  convene.  Cp.  AF.  covent  (whence  ME. covenl),  OF.,  F.  couvent,  OProveni;.  coven,  ‘con¬ vent’,  fr.  Eccles.  L.  co(n)ventus,  of  s.m.,  fr.  L. conventus.  Cp.  also  covenant,  covin.
13883:ning’,  and  song, event,  n.  —  OF.  event,  fr.  L.  eventus,  ‘occurrence, event’,  fr.  event-(um),  pp.  stem  of  evenire,  ‘to come  forth,  happen,  occur’,  fr.  e-  and  venire, ‘to  come’.  See  come  and  cp.  venue,  ‘arrival’, eventful,  adj.  —  Compounded  of  event  and  -fill; first  used  by  Shakespeare.
14353:ant’.  See  family, fan,  n.,  an  instrument  for  winnowing.  —  ME.,  fr. OE.  fann,  fr.  L.  vannus,  ‘winnowing  fan’.  See van,  ‘winnowing  fan’.
14355:fan,  n.,  an  enthusiastic  supporter  of  any  sport, esp.  of  base-ball  (U.S.  Slang).  —  Shortened  fr. fanatic.
21145:lapwing,  n.,  a  bird  of  the  plover  family.  —  ME. lappewinke,  fr.  OE.  hleapewince,  lit.  ‘leaper- waverer’,  fr.  hleapan,  ‘to  leap’,  and  wincian,  ‘to blink,  wink’  (the  original  meaning  of  this  latter was  ‘to  move  rapidly,  to  waver’) ;  influenced  in form  by  a  folk-etymological  association  with wing.  See  leap  and  wink, larboard,  n.,  left-hand  side  of  a  ship  to  a  person on  board  looking  from  the  stern  toward  the bow.  —  ME.  ladeborde,  lit.  ‘the  loading  side’. The  first  -r-  in  E.  larboard  is  due  to  the  analogy of  starboard.  See  lade  
22639:r,  n.,  cheekbone, malaria,  n.  —  Lit.  ‘bad  air’,  fr.  It.  mar aria,  con-
25465: nip,  ‘to  pinch’, nirvana,  n.,  extinction  of  the  individual  soul  by absorption  into  the  supreme  spirit  (Hinduism) —  OI.  nirvanah,  lit.  ‘a  blowing  out  (of  a  light), extinction,  disappearance’,  which  is  formed  fr. nis-,  nir-,  ‘out,  forth,  away’  (which  is  rel.  to Avestic  nish-,  of  s.m.,  and  prob.  cogn.  with OSlav.  nisti,  ‘poor’),  and  vati,  ‘it  blows’,  for whose  etymology  see  wind,  n.
37741:ink. Derivatives:  swing,  n.,  swing-er,  n.,  swing-ing-ly, adv.,  swing-y,  adj.
41148:  ‘to  blow’.  See  wind,  n.,  and  cp.  words there  referred  to.
41190:the  valley’.  See  wind,  n.,  and  avale.
41227:,  venous-ness,  n. vent,  n..  a  slit,  opening  in  a  coat.  —  ME.  vente,  a var.  of  fente,  fent,  fr.  MF.  (=  1. )  feme,  ‘cleft, slit’,  fr.  fendre,  ‘to  cleave,  split’,  fr.  L.  finder e (pp.  fissus );  see  fissile.  The  spelling  of  ME. vente  is  due  to  a  confusion  with  F.  vent,  ‘wind’. See  next  word.
41228:out  at  a  vent  . vent,  n.,  1)  outlet  for  air,  gas  or  liquid;  2)  ex¬ pression.  —  Partly  fr.  F.  vent,  ‘wind’,  fr.  L.  ven- tus ;  partly  fr.  F.  event,  ‘a  breaking  forth’,  fr. eventer,  ‘to  break  forth’,  which  is  formed  fr.  pref. i-  (=  OF.  es-,  L.  ex-),  and  vent,  ‘wind’.  See wind,  ‘air’,  and  cp.  ventilate.
41230:vent,  n.,  1)  the  act  of  selling;  2)  market  for  sale. —  MF.  (=  F.)  venfe, ‘sale’.fr.VL.  vendita,' sale’, prop.  fern.  pp.  of  L.  vendere,  ‘to  sell’,  used  as  a noun.  Cp.  It.  vendita,  Sp.  venta,  which  also  de¬ rive  fr.  VL.  vendita,  and  see  vend.  Cp.  also  next word.
```


## [2026-10-16T05:15:13.342Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o '.\\{0,300\\}Avestic  va.\\{0,500\\}' KLN_1966.txt | cut -c1-900 | head; grep -n -o 'malaria,  n.  —.\\{0,500\\}' KLN_1966.txt; sed -n 22640p KLN_1966.txt | cut -c1-500; grep -n -o 'window,  n.\\{0,400\\}\\|wing,  n.\\{0,400\\}' KLN_1966.txt | head -4"
}
```


### [2026-10-16T05:15:17.034Z] TOOL RESULT

```
ugrep: error: error at position 89
x80-\xbf][\x80-\xbf]*){0,500}
exceeds complexity limits___/


22639:malaria,  n.  —  Lit.  ‘bad  air’,  fr.  It.  mar aria,  con-
927
2760:wing,  nar¬ rowness’,  qziiku,  ‘narrow’,  Lith.  ahkstas,  ‘nar¬ row’,  fr.  I.-E.  base  *angh-,  ‘to  narrow,  com¬ press’  ;  the  corresponding  Celtic  base  is  *engh-, *%gh-,  whence  Bret,  enk ,  ‘narrow’,  Ir.  cumung, ‘narrow’,  Ir.,  W.  ing,  ‘distress’.  Cp.  agnail,  an¬ gina,  anguish,  anxious,  and  the  second  element in  cynanche,  quinsy,  squinancy,  Orobanche. Derivatives:  angr-y
21145:wing,  n.,  a  bird  of  the  plover  family.  —  ME. lappewinke,  fr.  OE.  hleapewince,  lit.  ‘leaper- waverer’,  fr.  hleapan,  ‘to  leap’,  and  wincian,  ‘to blink,  wink’  (the  original  meaning  of  this  latter was  ‘to  move  rapidly,  to  waver’) ;  influenced  in form  by  a  folk-etymological  association  with wing.  See  leap  and  wink, larboard,  n.,  left-hand  side  of  a  ship  to  a 
37741:wing,  n.,  swing-er,  n.,  swing-ing-ly, adv.,  swing-y,  adj.
```


## [2026-10-16T05:15:20.352Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22639,22642p KLN_1966.txt | cut -c1-600; grep -n 'Avestic  vat\\|Avestic  vä\\|Avestic vat' KLN_1966.txt | cut -c1-200 | head; grep -n '^wind,\\|wind,  n.,  air' KLN_1966.txt | cut -c1-200"
}
```


### [2026-10-16T05:15:20.794Z] TOOL RESULT

```
Derivative;  malar,  n.,  cheekbone, malaria,  n.  —  Lit.  ‘bad  air’,  fr.  It.  mar aria,  con-
927
traction  of  mala  aria,  ‘bad  air’,  fr.  mala,  fern,  of malo  (fr.  L.  malus),  ‘bad’,  and  aria,  ‘air’.  See mal-  and  air,  ‘atmosphere’.  The  term  malaria was  prob.  used  first  by  the  Italian  physician Francisco  Torti  (1658-1741).
Derivatives:  malari-al,  malari-an,  malari-ous, adjs.
4642:bedeck,  tr.  v.  —  Formed  fr.  be-  and  deck,  v. bedeguar,  bedegar,  n.,  a  mossy  growth  on  rose¬ bushes.  —  F.  bedeguar,  bedegar,  fr.  Pers.  bada- ward,  lit.  ‘wind  rose’,  fr. 
28684:wind,  bubble’,  from  the  imitative  base  *pu-, *phu-,  ‘to  blow,  swell’,  whence  also  L.  pustula, ‘blister,  pimple,  pustule’.  See  pustule  and  -ia  and cp.  the  next  two  words.
```


## [2026-10-16T05:15:26.345Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=883 && NR<=887 {print \"=== leaf \" NR-1; print}' KLN_1966.txt | grep -n -i 'wind\\|vata\\|vaiti' | cut -c1-400 | head -30"
}
```


### [2026-10-16T05:15:26.828Z] TOOL RESULT

```
9:Turbellaria,  n.,  a  class  of  flatworms  ( helminthol .) —  ModL.,  formed  with  suff.  -aria  fr.  L.  turbel- lae  (pi.),  ‘bustle,  stir’,  dimin.  of  turba,  ‘crowd’ (see  turbid  and  -ella);  so  called  from  the  little currents  caused  in  the  water  by  their  cilia), turbid,  adj.  —  L.  turbidus,  ‘confused,  disordered, muddy’,  fr.  turbare,  ‘to  confuse,  bewilder’,  fr. 
122:Derivative:  twilight-y,  adj. twill,  n.,  a  cloth  woven  in  parallel  diagonal  lines. —  ME.  twylle,  twyll,  fr.  OE.  twili,  rel.  to  OE. twilic,  ‘woven  double',  OHG.  zwilih,  MHG. zwilich,  G.  Zwillich,  ‘of  two  threads’,  and  prop, loan  translation  of  L.  bilix ,  ‘of  two  threads’,  fr. bi-  and  licium,  ‘thread’,  which  is  of  uncertain origin.  See  twi-  and  cp
162:Derivative:  typhoid-al,  adj. typhomania,  n.,  delirium  characteristic  of  typhus (med.)  —  Medical  L.,  compounded  of  typho- and  Gk.  jxavla,  ‘madness,  frenzy’.  See  mania, typhonic,  adj.,  pertaining  to,  or  resembling,  a  ty¬ phoon.  —  Gk.  TU9ttmx6?,  fr.  -rupoiv,  which  is rel.  to  TU90?,  ‘smoke,  mist’.  See  typhus  and  -ic. typhoon,  n.,  a  cyclone  in  the  west
163:Typhula,  n.,  a  genus  of  fungi  (hot.)  —  A  ModL. hybrid  coined  fr.  Gk.  ruipoe,  ‘vapor’  (see  next word),  and  L.  dimin.  suff.  -ula.  The  correct  form would  be  Typhidium  (fr.  Gk.  TU90?  and  suff. -idium,  fr.  Gk.  dimin.  suff.  -iStov). typhus,  n.  —  Medical  L.,  fr.  Gk.  TU90?,  ‘smoke, mist,  cloud,  fever  accompanied  by  stupor’, which  is  rel.  to  T09EIV,
```


## [2026-10-16T05:15:29.444Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'Gothic  winds\\|Goth.  winds' KLN_1966.txt | cut -c1-100; "
}
```


### [2026-10-16T05:15:29.765Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:15:32.688Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'winds,  ‘wind\\|vindr,  ‘wind\\|vindr' KLN_1966.txt | cut -c1-120 | head; tail -c 600 KLN_1966.txt; grep -c $'\\f' KLN_1966.txt"
}
```


### [2026-10-16T05:15:32.994Z] TOOL RESULT

```
11911:Derivative:  dividual-ly,  adv. divination,  n.  —  OF.  (=  F.),  fr.  L.  divinationem, acc.  of  divindtio,  ‘t
11914:divine,  tr.  and  intr.  v.  —  ME.  divinen,  devinen, fr.  OF.  (—  F.)  deviner,  fr.  VL.  *  divindre,  dis¬
11915:Derivatives:  diviner  (q.v.),  divin-ing,  n. diviner,  n.  —  ME.  devinour,  fr.  OF.  devineor,  fr. L.  divin
n,  n.,  an  amorphous  al¬ kaloid  obtained  from  sabadilla  seeds, C36H61OnN  (chem.)  —  Coined  fr.  L.  verdtrum, ‘hellebore’  (see  next  word),  and  the  chem. suffixes  -ide  and  -ine  (resp.  -in), veratrine,  n.,  also  veratrin,  veratrina,  veratria,  a poisonous  mixture  of  alkaloids  obtained  from sabadilla  seeds,  used  in  medicine  in  the  treat¬ ment  of  rheumatism,  neuralgia,  etc.  —  F.  vera¬ trine,  fr.  ModL.  veratrina,  fr.  L.  verdtrum,  ‘helle¬ bore’,  fr.  verare ,  ‘to  tell  the  truth’,  fr.  verus, ‘true’;  so  called  because902
```


## [2026-10-16T05:15:35.463Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'wind,  n.,  air\\|^wind, n\\|wind, n., air\\|wind,  n.' KLN_1971.txt | cut -c1-150 | head"
}
```


### [2026-10-16T05:15:35.766Z] TOOL RESULT

```
267376:wind, n., air in motion. — ME. wind, fr. OE.
```


## [2026-10-16T05:15:38.083Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 267376,267420p KLN_1971.txt | tr '\\n' ' '; echo; grep -n '^window, n\\|^wing, n\\|^weather, n' KLN_1971.txt | head; "
}
```


### [2026-10-16T05:15:38.397Z] TOOL RESULT

```
wind, n., air in motion. — ME. wind, fr. OE.  wind, rel. to OS., OFris., Du. wind, ON. vindr,  Dan., Swed. vind, OHG. wind, MHG. wint, G.  Wind, Goth, winds, and cogn. with OI. vdtafi,  Avestic vata-, Toch. A want, want, B yente, Hitt.  huwantis, L, vent us, OSlav. vetru, OPruss. wetro ,  Lith. vejas, ‘wind’, Lith. vetra, ‘tempest’, OIr.  feth, ‘air’, W. gwynt, Bret, gwent , ‘wind’. Adi  these words are derivatives of I.-E. base * we-, ‘to  blow’, whence also OI. vdti, vayati, Avestic  vditi, ‘blows’, Goth, waian, OE. wawan, OHG.  wdjan, MHG. weien, G. wehen , OSlav. vdjati, ‘to  blow’, Gk. <5 c7]|jU (for *1 blow’,   (for *<if7jTrjc), ‘wind’. Cp. weather, window,  wing, winnow, winze, wither. Cp. also van, ‘win-  nowing fan’, and fan. Cp. also Aello, atmo-,  bedeguar, nirvana, Vayu, vent, ‘outlet’, ventail,  ventiduct, ventilate, ventilation, Ventose, vol-au-  vent.   Derivatives: wind, tr. v., to scent, wind-less ,  wind-y , adjs., wind-i-ly, adv., wind-i-ness, n.   wind, tr. and intr. v., to turn. — ME. winden, fr.  OE. windan, ‘to wind, twist’, rel. to OS. windan ,  ON., Swed. vinda, Dan. vinde, OFris. winda, Du.  winden, OHG. wintan, MHG., G. winden, Goth.  windan, ‘to wind’, fr. I.-E. base *wendh-, *w$dh-,  ‘to turn, twist’, whence also OI. vandhurap , ‘a  hamper (made of wickerwork)’, Gk. £&poc<; [for  *F6l (vj&paf;], ‘chariot’. For the causatives of  the above mentioned verbs see wend. OF. guin -  der , It. ghindare , ‘to hoist’, are Teut. loan words.  Cp. wand, wander, wynd, gauntlet, ‘glove’, and  the first element in wentletrap and in windle-  straw. Cp. also Atragene.   Derivatives: wind, n., the act of winding, wind-  ing, n. and adj., wind-ing-ly , adv.   windlass, n., a device for raising weights by wind-  ing a rope round a cylinder. — ME. windelas,  windlas, fr. Ieel. vindilass, fr. ON. vindass  (whence also MDu., Du. windas ), which is  
265607:weather, n. — ME. weder , ‘storm’, fr. OE. weder y 
265623:weather, n.), with -ing, suff. forming verbal nouns, 
267446:window, n. — ME. windoge, windowe , fr. ON. 
267477:wing, n. — ME. wenge , winge, of Scand. origin.
```


## [2026-10-16T05:15:44.861Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 265607 267446 267477; do sed -n \"${l},$((l+10))p\" KLN_1971.txt | tr '\\n' ' ' | cut -c1-700; echo; done; grep -n '^Vayu, n' KLN_1971.txt; l=$(grep -n '^Vayu, n' KLN_1971.txt | cut -d: -f1); sed -n \"${l},$((l+5))p\" KLN_1971.txt | tr '\\n' ' '"
}
```


### [2026-10-16T05:15:45.406Z] TOOL RESULT

```
weather, n. — ME. weder , ‘storm’, fr. OE. weder y  rel. to OS. wedar, ON. vedr, Swed. vdder , Dan.  veir, OFris., MDu., Du, weder, OHG. wetar,  MHG. we ter, G. Wetter , ‘storm, wind, weather’,  and cogn. with OSlav. vitru , OPruss. wetro ,  ‘wind’, Lith. vetra, ‘storm’, OSlav. vedro , ‘good  weather’, vedru , ‘serene’ (said of the weather),  and prob. also with OI. vatab, ‘wind’. See wind,  ‘air in motion’, and cp. wither.   Derivatives: weather , tr. and intr. v., weather ,  

window, n. — ME. windoge, windowe , fr. ON.  vindauga , lit. ‘windeye’. See wind, ‘air in motion 7 ,  and eye.   Derivatives: window , tr. v., windo w-ed, adj.,  window-less, adj.   Windsor, n., 1) the Windsor bean; 2) a Windsor  chair; 3) Windsor soap. — Named after Wind-  sor, a town in Berkshire, England,  wine, n. — ME. win , fr. OE. win , fr. L. vinvm ,  

wing, n. — ME. wenge , winge, of Scand. origin.  Cp. ON. vsengr , Dan., Swed. vinge, ‘wing 7 ,  which are rel. to Du. waaien , ‘to blow; to flutter  in the wind, to fly’, OE. wawan, ‘to blow’. See  wind, ‘air in motion’.   Derivatives: wing, tr. and intr. v., wing-ed, wing-  less, adjs., wing-let, n.   wink, intr. and tr. v. — ME. winken , fr. OE.  wincian , ‘to nod, wink’, rel. to Du. wenken,  

259702:Vayu, n., the god of wind in Hindu mythology. 
Vayu, n., the god of wind in Hindu mythology.  — OI. vdyun, ‘wind*, rel. to vati, vayati , ‘it  blows’, and cogn. with L. ventus, ‘wind’, Goth.  waian, ‘to blow’, Lith. veyas, ‘wind’, OSlav.  vijati, ‘to blow’. See wind, n., and cp. words  there referred to.
```


## [2026-10-16T05:15:46.727Z] AGENT

Now Iranian sources.


## [2026-10-16T05:15:48.629Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *[0-9]*\\. *bād\\b\\|^ *[0-9]*\\. bäd\\|bād 'Wind\\|bäd .Wind\" HRN.txt | head; grep -n -i \"Wind'\" HRN.txt | head; grep -n \"bād\\b.*Wind\\|bäd.*Wind\\|andarvä\\|andarwä\\|andarvāy\\|andarwāy\" HUB.txt HRN.txt | head"
}
```


### [2026-10-16T05:15:48.987Z] TOOL RESULT

```
1728:151. {i)bäd 'Wind*,
1746:154. bädefräh 'Vergeltung, Strafe'.
6818:schnaufend*, skr. cvkä?- 'Wind' 2).
11132:aw. vayU' 'Luft'; ai. vayti- Luft, Wind'.
HRN.txt:1728:151. {i)bäd 'Wind*,
```


## [2026-10-16T05:15:51.808Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1728,1745p HRN.txt; sed -n 11125,11135p HRN.txt; grep -n \"151\\b\\|bäd\\b\\|bād\\b\" HUB.txt | head"
}
```


### [2026-10-16T05:15:52.245Z] TOOL RESULT

```
151. {i)bäd 'Wind*,
g. vad; Käs. vöd, vöi; mäz. va.
aw. väta- 'Wind*; phlv. vüt; ai. väta-,
kurd. ha, wäi; afy. vö; oss. t. wäd, vad (69); bei.
gvät, n. gvä&, gväs (148).
152. {lyhäd '-geschützt* (Comp.),
aw. pata- geschützt; phlv. -patx skr. patd-.
153. hädreng 'Citrone*.
mäz. vdreng.
phlv. vatrang (PPGl., Bund.), vatreng (Bund.), vatreg
(verschrieben (?), vd. 2 (77) GL).
*) Die verschiedene Art der Orientirung erklärt Bartholomae,
ZDMG. 42, 154. Zu apcf^s (Nom. sing.) vergl. KZ. 29, 501.
*) Ein aw. üö^«- *Kraft' (Justi) giebt es nicht, vergl. Geldner ,
KZ. 30, 524, Bartholomae, Indog. Forsch. I, 191 Anm.
3*— 86 —
arm. patrinc (de Lagarde, No. 1848: patriny)
gehört kaum hierher.
sicher)*; lit. udrä; abulg. vydra 'Otter; mhd. otter,
ahd. ottar, an. otr 'Fischotter' 3).
206. vaydän (auch vaytdn geschrieben^)) 'Haupt* (von
guten Wesen), AW.-Komm., Hn.
aw. vaydana' 'Haupt*.
207. vai 1) 'Luft', häufig; vergl. val veh und out mttar
(Men. 2, 115)^), oUyitan 'wehen' (AV.).
aw. vayU' 'Luft'; ai. vayti- Luft, Wind'.
*) Im AW.-Komm. wird H geschrieben, z. B. vd. 19 (5b).
*) L 4 hat vd. 14 (2) udrak,
') In gr. vS^ u. a. hat sich die Bedeutung *Otter* verschoben.
1276:291. Np. padtra 'entgegen = paz. padtra Min. Gl. 151,
5287:(oben p. 13 J.— 151 ~
5410:yasamin, ycivar, yOz, yoy (s. p. 151). Wo sonst y im Np.
6807:Shk. 261-262, Min. Gl. 151—152, patkar 'dispute* Shk.
6842:arm. Atrpatakan\ padospan Tab. 151 — 152 st,uS' ^padgOspdn
7337:Min. Gl. 151, phi. patasx^drgar Phi. Vd. p. 6, Z.3-2 v. u.,
7675:auch N. pr. (syr. nOD 6. Jhd. ZDMG. 44, 403; Tab. 151),
7687:u. 8. w., vgl. Horn Nr. 110-127; unten § 151. Doch er-
8175:p. 143—151. Daher zud H. 673 mit z in den Dialekten
8580:Geschwunden ist k in padospdn Tab. 151 — 152 = arm,
```


## [2026-10-16T05:15:57.051Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *151[\\.\\ ]\\|bäd 'Wind\\|bäd  \\|bäd,\\|,bäd\" HUB.txt | head; grep -n \"^wād\\|^wad \\|^andarwāy\\|^andarwāz\\|andarwāy\" PHD.txt PHD_mackenzie.txt | head; grep -n \"^vāt\\|^vät\\|^vāt \\|andarvāy\\|andarvāk\\|^vāy\" NYB_vol2_glossary.txt | head"
}
```


### [2026-10-16T05:15:57.576Z] TOOL RESULT

```
PHD.txt:761:air andarwāy, way; of the ~ andar- wayig.
PHD.txt:880:atmosphere andarwāy, way, spas.
PHD_mackenzie.txt:5114:wad [SL Y A < A sry'; wtl I M wd, N bad] bad, evil.
PHD_mackenzie.txt:9884:wad                        \tDl    wadxcm                     -6'\.)J ,0 \
PHD_mackenzie.txt:10267:wad                                         1-2wazidan
4058:vāyēndak [w'yndk'] flying creature, pl. cas. obl. —-än, enumerated after murvān 802. — Pres. pt. of Av. (1356) Wvay- ‘to fly’.
```


## [2026-10-16T05:16:01.154Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"wind\\b\" PHD.txt | head; grep -n \"^wād\\|^wāt\\|wād \\[\\|andarwāy\\|andarwa\" PHD_mackenzie.txt | head; grep -n \"^vāt\\|^vād\\|andarvāi\\|andarvāy\\|andarvāk\\|andar-v\" NYB_vol2_glossary.txt | head"
}
```


### [2026-10-16T05:16:01.555Z] TOOL RESULT

```
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
603:wābar [w’Al | M wbr, (N bāwar)] truth; belief. wābarīģān [w?/yk?n' | M wbryg’n) true, trustworthy. “Аһ: trustworthiness. wabz [wpc, wpz] wasp. wačast [wcst! = Av. vwacas-tasti-] strophe (of the Gathas). watéag [wck!, (bck!) | N bacca] child, baby, cub. wad [SL Y.ÀA < A sry’; wt! | M wd, N bad] bad, evil. ^ Áh : badness, evil. маа [w?t! | M wd, N bad] wind, breath, spirit; cal. 22nd day. wadag [wtk'] evil, vile, wicked. ~ih: evil, vileness. wādām [w’t?m | N bádám] almond. wādbān [w°tp’n' | N bādbān] sail.
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
653:~agig [-yk!] movable; intercalary (year). wihir- [whyl- | (M whwr-)] change. —išn: change. wimand [wymnd | = M] boundary, frontier, limit. ~ig, —6mand [-yk', 2wmnd] bounded, limited. *wiméhgén [wmyhkn! | M wymyh-] *shapely. wimustan [uwymwstn! | M wymrz- (< P)] spoil, destroy. win [wn'] vina, lute. wināh [zs | М zoyz)h, N gunàh] sin, crime. winahgar [wsk] | M wwhg’r, (N gunahhar)] sinner. ~ih: sinfulness. wināhīdan, wināh- [wn’s-ytn' | M wyn’h-] spoil, damage, destroy. ~išn: damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N gunjišk, binjišk] sparrow. win(n)ārdan, win(n)àr- [wyx?7-tn' | M wyn’r-dn] order, fix, arrange. ~išn: arrangement. win(n)irdan [wynltn' | M wynyrdn) be arranged, established; stay. iwir [wyl | M wyyr] man, hero. *wir [wyl | M wyr-, N bir] memory, mind. *wir [wyl | N bir] thunderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guréy] flight, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis [wys | = M] village. wisandan, wisān- [ws’n-dn'] separate. —išn(ih): separation. wisay- (ws'd- | M wys’y-] rest. wisbed [wyspt! | M wysbyd] village headman. wisé [wsydy | (P wsyd), N gusë] despatch. ~ kardan: send, despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
718:acquire ayāftan, handóxtan, wind- ādan, xwāstan.
1029:blow (v.) daftan, (damīdan); (wind) wāyīdan, wazīdan; — flute pazd-.
1937:find windādan.
2961:obtain ayāftan, windādan.
4306:which čē, kadam, kadār, ke. whichever kadām-iz-ē(w). whip aštar, tāzānag. whirlwind wād-girdag. white spēd, arus; (n.) spēdag. who kē, kadār.
1091:andarway ['ndlw'd I (P 'ndrw'z)] air, atmosphere.
5923:air andarway, way; of the,...., andar-    apart from fraz az, Jud az.
6002:atmosphere andarway, way, spas.          banquet sur, xwaran.
6003:atmospheric andarwayig.                  barbarity anerih.
12065:andarway                   .-.~~             uwcnidan                   , \ \'f.) '" t'"
12066:andarwayig           \~~~~                   owon                             \\,.~
448:andar-vāi [’ndlw’y] the atmosphere 8919. 9318, — Paz. andar-waé; SW form < *an- dar-vàd, MPrth ’ndrw’z (S; v. Sogd. 50). From andar + vaz-, v. vazitan.
557:urvar har cé ne ~ (se. hösitan) à nē hošet 9612-13, 9810-11; — apāyet būtan it is bound to happen, of predestination, explains jäyisn 271, brihenisn 16°; used itself as a nominal expression of Predestination: apäyet-bütan rād 16!!; — b) taking a v. n. as its complement: -šān ... gošt z"arisneh ne — it is not allowed for them to eat meat 10420-21; — e) governing a subordinate clause introduced by kū 8!. 1181-14 by ka 56?? (gl); without an introductory particle, with the governed vb. in ind. or in Subju.: ~ stdyé thou shalt profess 596; bē ~ apesihät 4419-19, v.s. v. apa- sistan. — MPrs ’b’yd with inf. (A-H II); Paz. āwāyastan āwāyad; āwāyastaa ‘re- quisite, desire’ (SGV); NP bäyistan, bā- yad; andar-vdi ‘desire, need (cf above no. 3; to be distinguished from andarvāt ‘atmosphere’, g. v.). Den. of OIr *updya- < *upa-aya- ‘that which comes upon, is imposed upon, affects a p.' = 1. need, 2. duty, cf Av. (150) upa-ay-, v. HP II, 17 sg.; Verbum 168; Ghilain 48. apāyišnīk ['p'dányk] proper, fit, fitting, handsome, nice, exquisite, comp. ~-tar, 33-5. 422, etc. passim; pl. cas. obl. ~-dn the qualified ones 1052,
5545:’hy’ng: äyiyän ’jdh’k: Aži-dahāk ’mb’g: ham-bäi ’mStn: āmušt ’mwjd: ämurzitan ^mwzdyft: āmuržītan ’n’bys: 'bēš ’ndrw’z: andar-vài "ngd(g): hangateh ’rd’w: ahlav
```


## [2026-10-16T05:16:15.534Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"vayu-\\|väyu-\\|vayav-\\|vayu\\b\" BRT.txt | cut -c1-250 | head -20; grep -n -i \"antara\\.vay\\|antarvay\\|antar.\\{0,3\\}vay\" BRT.txt | cut -c1-250 | head"
}
```


### [2026-10-16T05:16:15.880Z] TOOL RESULT

```
3570:•  j.  "apayate"  nqma  ahmi  (näial.  vayu^
8528:•  j.  uskSt  Adv.  '(von  oben  her;)  oben, hoch':  kainTnö  .  .  u°  yästayh  (sd.)  Vt  5. 64;  —  vayu^  *«•  yilstö'^  Yt,  15.  54.
13559:•  j.  d«r9zi.yaoxaSra-  Adj,  'des  Angriff  1 stark  ist"':  vayu!  .  .  -rö  Yt  15.  54.  I
22690:•j. 'vayav-, 'vaya- ''m. 'Luft,  Atmosphäre', als  Gottheit'*':  'yus  bä  nqma  ahmt . .  avat •yus  .  .yat  «va  dqma  vayemi  yasca  äa%al sp»nts  mainyui yasca  da'^at  anrS  matnyus Yt.  1$.  43 ;  —  'yusys  upar5.kairy5  Yl  75. 4, 2 1 
22693:*)  Die  S.  /.  21  mit  Ramait  in  Beziehung  ge- setzt wird»).  V. /p.  13  steht  der  Name  hinter &Jiij!a  und  Zrvan  und,  durch  eine  Anrufungs- Tormel  getrennt,  vor  Väla.  Der  Gottheil  ist das  junge  Machwerk  Yt  1$  gewidmet
22696:•  j.  'vayav-,  'vaya-  m.  Name  eines Daeva*':  *asls.vlhstui  dim  (näml.  nanm) bandayäti  °yö  dim  bastim  nayätt  V.5.  8; —  pairihwS  panta  yim  . .  hü  dit  atvö apairi%wS  yO  °yaos  anawtanidikahe  Aog.
22709:ZoDi  V.  •i'ü-.  —  Vgl.  'vayav-.  —  PB. :  väy  (/
22713:und;  s.  daiu  tvayav-*\  —  j  her  den  schßnen  Wagen  lenkend"  YL/o. Fi  u»w.  JJJ4.
24453:Komp.:  vüfia"\-äyav-.  —  ai.  visvayav-  Adj. ■für  alle  Lebenden  beMimmt'(?J.  —  Pü.(dKn.); hai-visp  elön,  hamäi  invadai,
```


## [2026-10-16T05:16:20.149Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /بادآس|باد آس/ {print \"LEAF\",NR-1; print}' BQT_v1_pages.txt | grep -n 'LEAF\\|بادآس\\|باد آس\\|vât\\|vāt\\|vata' | head -20"
}
```


### [2026-10-16T05:16:20.551Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:16:22.930Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:170 2>&1 | head -80",
 "timeout": 300000
}
```


### [2026-10-16T05:16:23.408Z] TOOL RESULT

```
no scan of BQT covers printed page 170 (see 'scans' in refs_online.json)
```


## [2026-10-16T05:16:28.489Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in $(seq 380 396); do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt526-$n.txt; echo \"leaf $n: $(head -c 300 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt526-$n.txt | tr '\\n' ' ')\"; done"
}
```


### [2026-10-16T05:16:29.729Z] TOOL RESULT

```
leaf 380: که زر بائد! .۷ امی‌صادق - بنم اول , اشاره (۱) به حضرت رسالت ناه صلوات‌اله علیه باشد . امیله ه بروزن دلیله » بمعی‌آمله‌است وان وهای باشد درهندوستان که درشکرپرورده ۲۳ وخ�
leaf 381: یوتانی۱ وممنیآن‌بفارسی « سنگه زاییدن آمان کن » باشد . وآن دانه ایست ساهرنگه بمقداو جوژبوا. بغایت املی‌وصلب ودشوارشکن: وچون بجنبانند مفز آن در درون وی صدا کند وآنرا ب
leaf 382: اتبارش که پر کرده باشد - و بمعنی پرنسمت و با نعست هم اجه ات ۵ نبادش! -بروزن‌افزایش. پر کردنی‌را کوبند . و آن چیزی باشد که جوف درون چیزبرا بان پر کنند. وأنرا بعربی حشوخوا�
leaf 383: سب ی ٩5‏ | بودن بروزن افزودن, بربالای حم چیدن باشد . اثبوذن س با زال قطه‌دار بروزن‌اندودن, بمعنی اسل‌کاینات و آفرینش باشد . ایوس » بروزن اضوی , تخمی باشد بنظر آحده است �
leaf 384: انج - بفتح اول وسکون ثانی و جیم» اطراف 2 روی و رخار ( ۱ ) باشد - «بمعنی بیرون رفتن وبیرون کشیدن‌هم آمدم‌است - وامر بان معنی هم حست بمنی بیرون بکش . انحام ۱ و آخر هرکار و هو�
leaf 385: - بو - ) فحل س بفتم اول وکسر ثالث و سکون نانی ولام» رسثنی باشد که آیرا خطمی خوانند ۳ عالمتاب است . انجمن! - ینم اك و قح میم وسکون نون ۰ مجلس و مجمم را کویشد - بمعنیکروه انحوج
leaf 386: انجین از توابم بزد - و ناوچهٌ مقمد و سوراخ کون را نیز گویند ٩‏ . # | نجین۲ بروزن‌دنگین» بمعنی ریز مر بزه باشد و ربزه کننده را نیز گویشد - و امر باین ممنی هم هست عئی ریزه و 
leaf 387: -۱۹۹ - )اد « بروزن پرواژ ؛ ممنی شسد - و میل نمودن - و حمله کردن باشد - و امر باين معنی هم هست عنی فص دکن ومیل تمای - است. واندازمومقیای‌ومقذار چیزی‌رانی زکویند ۱ و بممنی مص
leaf 388: اندر خور ا ندز خو در - بنمخای نفطه‌داروسکون واو ممدو له و رای می‌نقعله 4 ممحنی اج وسزاوار وزیبا باشد . بمشی اندرخور است که لابق و مزاوار و زیبا باشد . آثدر خو دك هه بنکو�
leaf 389: اف او رفتی . بکشب بای شد و آتش را بکشت راندروی درمیان دربا کم کردید .. سین می‌نقطه , نام یکی از حکمای بونان است گوند درطبابت اعجاز مکاربردی ۴ نلم مکی از مبلوزان تورانیی �
leaf 390: انسجان که کرفتگی دل ودلگیری باشد . اندهان بروزن مردمان ؛ جمم انده باشد چنانکه جانور را جانوران ومردمرا عردمان کویند . واین جمم بخلاف‌قیای است چه‌بنیراز جاتور را بال�
leaf 391: رن ار ه- باازای فارسی بر وزن غمزه ؛ مرجماث باشد و آثرا ببربی عد ی گویند . انسته - بفتم اول و کسرثانی و سکون سین بی‌قطه و فتح فوفالی 4 مقصورآ دته است» وان بیخ کیاهی باشد خو
leaf 392: اگارده است که افسانه و سر گذشت باشد . انگاده ۱ ه بروزن عموارء ."هر چیز "که افانه وس گذشت داشد - وباد گذشتها کردن رانیز کوبند - و ازسر گرفتن سر گذشت وافانه را عم گفته اند بط
leaf 393: مردم فررنگ «م هست ٩‏ ۰ الث و زای قطه‌دار ساکن » سلی باشد که بآن زمن را هموار ساز ند ۹ انگز ح بفت اول و خم نالث: و کت تابی و زای فارسی» آهنی باشد سر کج که فیلرا بدان بهرطر�
leaf 394: انگشت ب حرف‌نهادن - کنابه ازعیب کر فتن ودکته گیری کردن باشد . ) نگشت بر دهان گد اشتن- کنابه از<سرت واضوی - وتعجب وتحیرباشد - واشاره کردن بخاموشی هم هست . بضم بای ابجد وفتح
leaf 395: یاف چنکالی ومالیده 3۳ وان یش کی با روغن وشیرینی بهم‌بمالند . انگشتو) ۰ بکس الك و داد بالف کشیده . نی باشد که آنرا برروی آعل زغال وغیره بز ند. انگشته - بنم الث بر وزن خریشت
leaf 396: انگوز زیتونی . . وبعربی اصابع‌المذاری گوبند . ) نگوژه؟ - با زای فارسی بر وزن سنبوصه ؛ صمغ درخت انکدان باشد و به_بی حلثیت و صمن‌المحروث خوانند . و تخم آنرا بذرالانجره وقر
```


## [2026-10-16T05:16:39.110Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /اندروا|اندرواى|اندروای/ {print \"LEAF\",NR-1}' BQT_v1_pages.txt; awk 'BEGIN{RS=\"\\f\"} /۱۷۰ -|- ۱۷۰|-۱۷۰-|۲۰۵ -|-۲۰۵|- ۲۰۵/ {print \"LEAF\",NR-1}' BQT_v1_pages.txt"
}
```


### [2026-10-16T05:16:39.697Z] TOOL RESULT

```
LEAF 387
LEAF 388
```


## [2026-10-16T05:16:44.333Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==389' BQT_v1_pages.txt | grep -n -B2 -A6 'اندروا' | head -60"
}
```


### [2026-10-16T05:16:44.715Z] TOOL RESULT

```
30-باشد .
31-اند واه ۲ ع بروزن لشگ ی گاء»‌بمعنی
32:اندرواژ اس تکه س رکشته رحیران - واحتیاج -
33-وسرنگون آوبخته باشد . .
34-| ندد و ای" بروزن‌سندل‌سای,یمعنی
35:اندرواه است که صر گشته وحیران و احتیاج (۱)
36-وسرتگون آویخثه باشد .
37-| نددوالی " - بروزنک پروایی: بمحنی
38-ب کشتگی وحیرانی - و آرزو و حلجتمندی -
39-وسر‌دگونی باشف .
40-ندر وب س بفتح اول وضم ثالث‌پروزن
41-کند کرب . نام نوعی از جوشش باشد که پوست
```


## [2026-10-16T05:16:48.425Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==389' BQT_v1_pages.txt | grep -n -i '[a-z]\\{3,\\}\\|^ *(۱)\\|۲۰' | head -30; awk 'BEGIN{RS=\"\\f\"} NR==389' BQT_v1_pages.txt | head -5"
}
```


### [2026-10-16T05:16:48.869Z] TOOL RESULT

```
اندر خور
ا ندز خو در - بنمخای نفطه‌داروسکون
واو ممدو له و رای می‌نقعله 4 ممحنی اج وسزاوار
وزیبا باشد .
بمشی اندرخور است که لابق و مزاوار و زیبا
```


## [2026-10-16T05:16:53.484Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/pageimg | head; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT | head -30"
}
```


### [2026-10-16T05:16:53.948Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   60k sfmqrb 14 Oct 22:19  bqt_v3_p150-150.png
.rw-r--r--   51k sfmqrb 14 Oct 22:19  bqt_v3_p600-600.png
.rw-r--r--   75k sfmqrb 14 Oct 22:19  bqt_v4_p150-150.png
.rw-r--r--   41k sfmqrb 14 Oct 22:19  bqt_v4_p500-500.png
.rw-r--r--   55k sfmqrb 14 Oct 22:19  bqt_v5_p8-008.png
.rw-r--r--   42k sfmqrb 14 Oct 22:19  bqt_v5_p30-030.png
.rw-r--r--   49k sfmqrb 14 Oct 22:19  bqt_v5_p150-150.png
.rw-r--r--   44k sfmqrb 14 Oct 22:19  bqt_v5_p250-250.png
.rw-r--r--   79k sfmqrb 14 Oct 22:19  irn_p100-100.png
Permissions Size User   Date Modified Name
.rw-r--r--  368k sfmqrb 14 Oct 22:19  0001.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  0001.txt
.rw-r--r--  534k sfmqrb 14 Oct 22:19  0049.png
.rw-r--r--  2.7k sfmqrb 14 Oct 22:19  0049.txt
.rw-r--r--  190k sfmqrb 14 Oct 22:30  0143.jpg
.rw-r--r--   576 sfmqrb 14 Oct 22:30  0143.vision.txt
.rw-r--r--  472k sfmqrb 14 Oct 22:45  0339.jpg
.rw-r--r--   849 sfmqrb 14 Oct 22:45  0339.vision.txt
.rw-r--r--  221k sfmqrb 16 Oct 01:15  0342.jpg
.rw-r--r--   700 sfmqrb 16 Oct 01:15  0342.vision.txt
.rw-r--r--  522k sfmqrb 14 Oct 22:46  0456.jpg
.rw-r--r--  1.0k sfmqrb 14 Oct 22:46  0456.vision.txt
.rw-r--r--  202k sfmqrb 14 Oct 22:30  0479.jpg
.rw-r--r--   444 sfmqrb 14 Oct 22:30  0479.vision.txt
.rw-r--r--  205k sfmqrb 14 Oct 22:30  0480.jpg
.rw-r--r--   849 sfmqrb 14 Oct 22:30  0480.vision.txt
.rw-r--r--  481k sfmqrb 14 Oct 22:46  0511.jpg
.rw-r--r--   799 sfmqrb 14 Oct 22:46  0511.vision.txt
.rw-r--r--  490k sfmqrb 14 Oct 22:46  0544.jpg
.rw-r--r--   644 sfmqrb 14 Oct 22:46  0544.vision.txt
.rw-r--r--  2.6k sfmqrb 14 Oct 22:19  31.vision.txt
.rw-r--r--  1.5k sfmqrb 14 Oct 22:19  58.vision.txt
.rw-r--r--  1.9k sfmqrb 14 Oct 22:19  70.vision.txt
.rw-r--r--  257k sfmqrb 14 Oct 22:19  71.png
.rw-r--r--  1.5k sfmqrb 14 Oct 22:19  71.vision.txt
.rw-r--r--  1.6k sfmqrb 14 Oct 22:19  72.vision.txt
.rw-r--r--  1.1k sfmqrb 14 Oct 22:19  103.vision.txt
.rw-r--r--  521k sfmqrb 14 Oct 22:19  171.png
.rw-r--r--   806 sfmqrb 14 Oct 22:19  171.vision.txt
```


## [2026-10-16T05:16:56.650Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; ls | grep -E '^(0?1[67][0-9]|0?20[0-9]|0?19[0-9]|0?23[0-9]|0?24[0-9])\\.'; cat 171.vision.txt; cat 0143.vision.txt"
}
```


### [2026-10-16T05:16:57.007Z] TOOL RESULT

```
[Borhan-e Qate', ed. Mo'in, vol. 1, printed p. 171 — read from the archive.org scan
 borhan-ghate-v1 leaf n389 (https://archive.org/download/borhan-ghate-v1/page/n389.jpg).
 Page identified by the footnote catch-line «بقیه در صفحهٔ ۱۷۲».]

Headword (col. 2):
اندوختن* — بروزن افروختن، بمعنی جمع کردن و فراهم آوردن باشد — بمعنی قرض و وام دادن ...

Footnote 5 (bottom of p. 171):
۵ ـ پهلوی handôxtan (از handôzh «اندوز»، بمعنی جمع کردن)، مرکب
بقیه در صفحهٔ ۱۷۲

[Other footnotes on the same page, for neighbouring headwords:
 ۳ ـ پهلوی handak (کم، کمی) «مناس ۲۷۶»، رك: اند.
 ۴ ـ از اسپانیولی Andalucia ...
 ... Vandarəmainish ...]
[BQT vol.1 printed p.143 = archive.org borhan-ghate-v1 leaf n359; read from the page image]
Mo'in's added entry (marked ☼) in the footnote zone:
☼ اطلس - از تازی، از یونانی Atlas (نام ربّ‌النوع حامل کرهٔ زمین) «نفس». کتاب شامل نقشه‌های جغرافی - جامهٔ ابریشمی پرز دار.
(Column text above, for context: اصطرلاب - معروف است و آن آلتی باشد از برنج ... و این لغت یونانی است بمعنی ترازوی آفتاب چه اصطر ترازو ...)
```


## [2026-10-16T05:17:04.041Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in $(seq 418 432); do echo \"leaf $n: $(awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -c 200 | tr '\\n' ' ')\"; done; awk 'BEGIN{RS=\"\\f\"} /بادآس|باد آس|بادا س|بادآ س/ {print \"LEAF\",NR-1}' BQT_v1_pages.txt"
}
```


### [2026-10-16T05:17:05.313Z] TOOL RESULT

```
leaf 418: ابلا ومردمان و جماعت را نیز گویند - وهیل را هم مبگوبند که له صفارباشد - و بکر اولوفتح انی مشدد گا و کوهی باشد . گو�
leaf 419: دنق و نام ییت النفدس هم‌هست - وبسینی کوبند تام عبت ان رت رادم کر از فتحهایعبرخطاب. ومعنی آن‌سدیق اکبرباشد. ایم 
leaf 420: ایولز ایو اد « بانانی مجهول بر وزن شیرازه بمعتی آراسته و بیراسته باشه ۱ . بسعنی ابواز است که آراسته و پیراسته با
leaf 421: و شش لت و نات بیان اول با - , دمعم مع است که‌بجهت عصاحت باشد - ویمعنی به بفتح بای ابجد - و مضاف به اسامی آشها مانند 
leaf 422: ۱ بابادشاه دست زدن ۱ متشه د< است؛ و این صفیر بجهت تعظیم است . پا یل » یکر الك بر وزن قابل , بلفت بونانی نام ستار هش�
leaf 423: بت ۷۲۰۳ ح- قلعهٌ آن شهر بوده چاهی است عمیق . گویندحاروث و ماروت در اتحاه محبوی آند» و جضم الث حم هقلح آنتتته. : یا 
leaf 424: ودریجة کوچك را گوند» وظاهراً ابن لفت‌باجهك است که مصفر باجه باشده و باجه مخفف بادجه و پادجه بمعنی باد گیر و با�
leaf 425: ی ۷۰ ‌- پاخر و بنتحالت وسکون رای‌بی‌هطه و زای نقطه‌دار , نام فصبهابست در خراسان ونم کوشه‌نی باشد از چهل و حشت 
leaf 426: نکن مم ینظر آعده است ٩‏ ادا فنجیر - نومی از درخت انجیراست که یش از هم درختان موه دهد و انجیر آن کاواك و پرباد میب
leaf 427: سب ۰ ۷ -- و او آنرامتصرف شد وباین تام موسوم کشت ٩‏ - و نام بوتهٌ خاری است سفید و دراز بقدر بكنرع در هایت خفت و سبکی
leaf 428:  هریداب‎ باك بره » بنتح بای ابجد و رای‌فرخت. نام روز یست و دوم )۱( همن حاه باشف. کو بند عفت سال درابران باد نیامد�
leaf 429: نت و ۵ ٩‏ حه باددر هشت ه بسنی باد در کف است که بی‌ماحصل و نهی‌دست و مفلس باشد . باددر فام ۱- بک دابع و سکون‌زای ف
leaf 430: باد وح که جربی بادروج گویند ؛ د بسی کوبند بادرو تره‌ایست که بر کش بسپرغم میماند و بوی ترنج میدهد پاددوج - بسکون 
leaf 431: است که عوام یازهر کوبند و بعربی حجرالئیس خوانند - وبسنی مهر# مار رانیز بادزهر کفته‌اند باد ز هر د- فتح رای قرشت �
leaf 432: مار از اعمال هرات و اصل آن بادخیز بوده است که معل هبوب ریاح باشد ۷ . باثقر « با فایروزن‌داد کر ؛ جزاومکافات بدیر
```


## [2026-10-16T05:17:11.460Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for n in 388 427 428; do curl -sL -o bqt526-n$n.jpg \"https://archive.org/download/borhan-ghate-v1/page/n$n.jpg\"; file bqt526-n$n.jpg; done",
 "timeout": 180000
}
```


### [2026-10-16T05:17:16.420Z] TOOL RESULT

```
bqt526-n388.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
bqt526-n427.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
bqt526-n428.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
```


## [2026-10-16T05:17:22.260Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 -c \"\nfrom PIL import Image\nfor n in [388,428]:\n    im=Image.open(f'bqt526-n{n}.jpg'); w,h=im.size\n    im.crop((0,0,w,int(h*0.55))).resize((w//2,int(h*0.55)//2)).save(f'bqt526-n{n}-top.png')\n    im.crop((0,int(h*0.5),w,h)).resize((w//2,int(h*0.5)//2)).save(f'bqt526-n{n}-bot.png')\n\""
}
```


### [2026-10-16T05:17:22.661Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-16T05:17:37.995Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; which magick convert vips 2>/dev/null; for n in 388 428; do magick bqt526-n$n.jpg -crop 100%x55%+0+0 -resize 50% bqt526-n$n-top.png; magick bqt526-n$n.jpg -gravity south -crop 100%x50%+0+0 -resize 50% bqt526-n$n-bot.png; done; ls"
}
```


### [2026-10-16T05:17:40.649Z] TOOL RESULT

```
/usr/bin/magick
/usr/bin/convert
/usr/bin/vips
```


## [2026-10-16T05:17:44.599Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt526-n388-bot.png"
}
```


### [2026-10-16T05:17:44.632Z] TOOL RESULT

```

```


## [2026-10-16T05:17:50.536Z] TOOL CALL #45: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt526-n388-top.png"
}
```


### [2026-10-16T05:17:50.596Z] TOOL RESULT

```

```


## [2026-10-16T05:17:52.983Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt526-n428-bot.png"
}
```


### [2026-10-16T05:17:53.010Z] TOOL RESULT

```

```


## [2026-10-16T05:17:56.606Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; n=427; magick bqt526-n$n.jpg -crop 100%x55%+0+0 -resize 50% bqt526-n$n-top.png; magick bqt526-n$n.jpg -gravity south -crop 100%x50%+0+0 -resize 50% bqt526-n$n-bot.png"
}
```


## [2026-10-16T05:17:57.904Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt526-n427-top.png"
}
```


## [2026-10-16T05:17:58.758Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt526-n427-bot.png"
}
```


### [2026-10-16T05:17:59.934Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-16T05:17:59.952Z] TOOL RESULT

```

```


### [2026-10-16T05:17:59.962Z] TOOL RESULT

```

```


## [2026-10-16T05:18:04.106Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for n in 425 426; do curl -sL -o bqt526-n$n.jpg \"https://archive.org/download/borhan-ghate-v1/page/n$n.jpg\"; magick bqt526-n$n.jpg -crop 100%x55%+0+0 -resize 50% bqt526-n$n-top.png; magick bqt526-n$n.jpg -gravity south -crop 100%x50%+0+0 -resize 50% bqt526-n$n-bot.png; done; ls bqt526*",
 "timeout": 180000
}
```


## [2026-10-16T05:18:05.497Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt526-n425-top.png"
}
```


## [2026-10-16T05:18:06.433Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt526-n425-bot.png"
}
```


### [2026-10-16T05:18:11.423Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--  2.2k sfmqrb 16 Oct 01:16  bqt526-380.txt
.rw-r--r--  3.7k sfmqrb 16 Oct 01:16  bqt526-381.txt
.rw-r--r--  2.7k sfmqrb 16 Oct 01:16  bqt526-382.txt
.rw-r--r--  3.1k sfmqrb 16 Oct 01:16  bqt526-383.txt
.rw-r--r--  2.7k sfmqrb 16 Oct 01:16  bqt526-384.txt
.rw-r--r--  3.0k sfmqrb 16 Oct 01:16  bqt526-385.txt
.rw-r--r--  2.4k sfmqrb 16 Oct 01:16  bqt526-386.txt
.rw-r--r--  3.5k sfmqrb 16 Oct 01:16  bqt526-387.txt
.rw-r--r--  2.6k sfmqrb 16 Oct 01:16  bqt526-388.txt
.rw-r--r--  2.6k sfmqrb 16 Oct 01:16  bqt526-389.txt
.rw-r--r--  2.7k sfmqrb 16 Oct 01:16  bqt526-390.txt
.rw-r--r--  3.7k sfmqrb 16 Oct 01:16  bqt526-391.txt
.rw-r--r--  2.5k sfmqrb 16 Oct 01:16  bqt526-392.txt
.rw-r--r--  2.9k sfmqrb 16 Oct 01:16  bqt526-393.txt
.rw-r--r--  2.6k sfmqrb 16 Oct 01:16  bqt526-394.txt
.rw-r--r--  2.9k sfmqrb 16 Oct 01:16  bqt526-395.txt
.rw-r--r--  3.0k sfmqrb 16 Oct 01:16  bqt526-396.txt
.rw-r--r--  266k sfmqrb 16 Oct 01:17  bqt526-n388-bot.png
.rw-r--r--  269k sfmqrb 16 Oct 01:17  bqt526-n388-top.png
.rw-r--r--  530k sfmqrb 16 Oct 01:17  bqt526-n388.jpg
.rw-r--r--  242k sfmqrb 16 Oct 01:18  bqt526-n425-bot.png
.rw-r--r--  283k sfmqrb 16 Oct 01:18  bqt526-n425-top.png
.rw-r--r--  533k sfmqrb 16 Oct 01:18  bqt526-n425.jpg
.rw-r--r--  218k sfmqrb 16 Oct 01:18  bqt526-n426-bot.png
.rw-r--r--  275k sfmqrb 16 Oct 01:18  bqt526-n426-top.png
.rw-r--r--  504k sfmqrb 16 Oct 01:18  bqt526-n426.jpg
.rw-r--r--  232k sfmqrb 16 Oct 01:17  bqt526-n427-bot.png
.rw-r--r--  293k sfmqrb 16 Oct 01:17  bqt526-n427-top.png
.rw-r--r--  541k sfmqrb 16 Oct 01:17  bqt526-n427.jpg
.rw-r--r--  237k sfmqrb 16 Oct 01:17  bqt526-n428-bot.png
.rw-r--r--  289k sfmqrb 16 Oct 01:17  bqt526-n428-top.png
.rw-r--r--  536k sfmqrb 16 Oct 01:17  bqt526-n428.jpg
```


### [2026-10-16T05:18:11.442Z] TOOL RESULT

```

```


### [2026-10-16T05:18:11.450Z] TOOL RESULT

```

```


## [2026-10-16T05:18:15.720Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt526-n426-top.png"
}
```


### [2026-10-16T05:18:15.739Z] TOOL RESULT

```

```


## [2026-10-16T05:18:22.099Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for w in بادآس اندروا آتمسفر مالاریا نیروانا; do for u in \"https://vajehyab.com/moein/$w\" \"https://abadis.ir/fatofa/$w/\"; do p=$(python3 tools/fetch_source.py \"$u\" --note \"page 526, root We 1: Mo'in/dictionary entry for $w\" 2>&1 | tail -1); echo \"$u $p $(wc -c < $p)\"; done; done",
 "timeout": 300000
}
```


### [2026-10-16T05:18:33.191Z] TOOL RESULT

```
https://vajehyab.com/moein/بادآس /home/sfmqrb/git/rishe-private/data/verification/sources/web/f627ad32fb7101e9.txt 854
https://abadis.ir/fatofa/بادآس/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/f276ec3dfe12e13e.txt 2760
https://vajehyab.com/moein/اندروا /home/sfmqrb/git/rishe-private/data/verification/sources/web/ffd8799832ba5eca.txt 134
https://abadis.ir/fatofa/اندروا/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/42590a21ae25674f.txt 6723
https://vajehyab.com/moein/آتمسفر /home/sfmqrb/git/rishe-private/data/verification/sources/web/1798047445ff7623.txt 1042
https://abadis.ir/fatofa/آتمسفر/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/728f731370565647.txt 10829
https://vajehyab.com/moein/مالاریا /home/sfmqrb/git/rishe-private/data/verification/sources/web/1a2b33a9f2f0e9b4.txt 1137
https://abadis.ir/fatofa/مالاریا/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/22a14f8306237399.txt 17456
https://vajehyab.com/moein/نیروانا /home/sfmqrb/git/rishe-private/data/verification/sources/web/9b4723e0d409b6df.txt 136
https://abadis.ir/fatofa/نیروانا/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/790b7986b027eab1.txt 21769
```


## [2026-10-16T05:18:35.999Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in f627ad32fb7101e9 f276ec3dfe12e13e 1798047445ff7623 1a2b33a9f2f0e9b4; do echo \"== $f\"; sed -n '5,$p' $f.txt | grep -v '^\\s*$' | tr '\\n' ' ' | cut -c1-900; echo; done; for f in 42590a21ae25674f 790b7986b027eab1 728f731370565647 22a14f8306237399; do echo \"== $f\"; grep -n 'معین\\|فر\\.\\|سنس\\|انگ\\|هوا' $f.txt | head -8 | cut -c1-300; done"
}
```


### [2026-10-16T05:18:36.341Z] TOOL RESULT

```
== f627ad32fb7101e9
معنی بادآس | فرهنگ انتشارات معین | واژه یاب   26 فرهنگ   همه دیکشنری مترادف طیفی آزاد +   همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه   بادآس  فرهنگ انتشارات معین  (اِمر.) آسیاب بادی .  بادآس در فرهنگ‌های دیگر  معنی بادآس در لغت‌نامه دهخدا   معنی بادآس در دیکشنری فارسی به انگلیسی   واژه‌های مشابه  بااستخوان   باداباد   خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره   نسخه جدید 

== f276ec3dfe12e13e
باداس - معنی در دیکشنری آبادیس   دیکشنری مترجم بپرس   باداس  /bAdAs/  دنبال کنید   لغت نامه دهخدا  ( بادآس ) بادآس. ( اِ مرکب ) آس بمعنی آسیا که با باد گردد. آسیای بادی. مرکب از دو کلمه آس و باد. رجوع به این دو کلمه شود.   فرهنگ فارسی  ( باد آس ) ( اسم ) آس بادی آسیایی که با باد گردد   فرهنگ معین  ( بادآس ) (اِمر. ) آسیاب بادی .   پیشنهاد کاربران  درود برشما  آس به معنای اسیاب داس به معنای درو  اسیاب به وسیله باد  + عکس و لینک   دیکشنری آبادیس  آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشن

== 1798047445ff7623
معنی آتمسفر | فرهنگ انتشارات معین | واژه یاب   26 فرهنگ   همه دیکشنری مترادف طیفی آزاد +   همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه   آتمسفر  فرهنگ انتشارات معین  (مُ فِ) [ فر. ] (اِ.) 1 - تودة هوایی که اطراف کرة زمین را فرا گرفته ، جو. 2 - کنایه از: اوضاع و احوال .  آتمسفر در فرهنگ‌های دیگر  معنی آتمسفر در فرهنگ فارسی عمید / قربان‌زاده   معنی آتمسفر در فرهنگ مترادف و متضاد   معنی آتمسفر در فرهنگ سره   واژه‌های مشابه  اتمسفر   خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره   نسخه جدید 

== 1a2b33a9f2f0e9b4
معنی مالاریا | فرهنگ انتشارات معین | واژه یاب   26 فرهنگ   همه دیکشنری مترادف طیفی آزاد +   همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه   مالاریا  فرهنگ انتشارات معین  (اِ.) تب نوبه ؛ بیماری گرمسیری که بر اثر گزش پشة آنوفل در بدن انسان پدید می آید و با تب و لرز و عرق شدید و متناوب همراه است .  مالاریا در فرهنگ‌های دیگر  معنی مالاریا در لغت‌نامه دهخدا   معنی مالاریا در فرهنگ فارسی عمید / قربان‌زاده   معنی مالاریا در فرهنگ مترادف و متضاد   معنی مالاریا در فرهنگ فارسی طیفی   خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره   نسخه جدید 

== 42590a21ae25674f
13: معنی انگلیسی : hanging 
19: اندروا. [ اَ دَ ] ( ص مرکب ) سرنگون آویخته و واژگون. ( برهان قاطع ) ( هفت قلزم ). آویخته و نگونسار. ( غیاث اللغات ). سرنگون و آویخته و باژگونه. ( مؤید الفضلاء ). معلق. آویخته. ( از فرهنگ رشیدی ) ( فرهنگ فارسی معین ). نگون آویخته. ( فرهنگ سروری ). سرنگون و سر فروافکنده و واژگون و معلق. ( ناظم ال
33: || در هوا. ( فرهنگ فارسی معین ). آنکه میان زمین و آسمان یعنی در فضاست بی اتکاء بجایی و تعلیق از جایی. ( یادداشت مؤلف ) : 
40:بحر که مایه ده هر سرمایه دار است در حوالی ولایتش ( مازندران ) کناره نشینی ، ابر خفتان پوش که در دفع ضرر آفتاب از آن ریاض اندرواست.... ( عنایت نامه ملک الکلام جلال الدین دهستانی نقل از جنگ خطی مورخ به 651 ). || سرگشته و حیران. ( برهان قاطع ) ( غیاث اللغات ) ( هفت قلزم ). سرگشته و حیران و سرگردان. 
45:( صفت ) ۱ - در هوا . ۲ - معلق آویخته 
47: فرهنگ معین
73: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده
== 790b7986b027eab1
17: اسم: نیروانا (دختر) (سانسکریت) (مذهبی و قرآنی) (تلفظ: nirvānā) (فارسی: نيروانا) (انگلیسی: nirvana) 
18: معنی: آخرین مرحله سلوک در نزد بودا، انسان کامل، ( سنسکریت ) آخرین مرحله سلوک در نزد « بودا » که مرحله ی محو شدن جنبه ی حیوانی وجود و رسیدن به کمال است، ( سنسکریت ) آخرین مرحله سلوک در نزد ' بودا ' که مرحله ی محو شدن جنبه ی حیوانی وجود و رسیدن به کمال است، آخرین مرحله سلوک در نزد
27: نیروانا (آلبوم). «نیروانا» ( به انگلیسی: Nirvana ) آلبومی از نیروانا است که در سال ۲۰۰۲ میلادی منتشر شد. 
48: نیروانا (ئی پی). نیروانا اولین آلبوم چندآهنگه ( ای پی ) از خواننده انگلیسی سم اسمیت. آلبوم در ۴ اکتبر ۲۰۱۳ در بریتانیا به عنوان دانلود موسیقی منتشر شد. ای پی شامل یک نسخه صوتی از ترانه دیسکلوژر است. نیروانا در اکتبر ۲۰۱۳ در رتبه ۸۲ جدول تک آهنگ های بریتانیا قرار گرفت. [ ۱] 
55: نیروانا (فیلم). نیروانا ( انگلیسی: Nirvana ) فیلمی در ژانر علمی–تخیلی به کارگردانی گابریله سالواتورس است که در سال ۱۹۹۷ منتشر شد. از بازیگران آن می توان به کریستوفر لمبرت، امانوئل سنیه و پائولو روسی اشاره کرد. 
58: نیروانا (گروه موسیقی). نیروانا ( به انگلیسی: Nirvana ) یک گروه راک آمریکایی بود که در سال ۱۹۸۷ توسط کرت کوبین ( گیتاریست و خواننده ) و کریست ناواسلیک ( گیتار بیس ) بنیان نهاده شد. نیروانا چند نوازندهٔ درامز مختلف را به خود دید که هر کدام مدت کوتاهی در گروه عضویت داشتند، اما بالاخره دیو گرول که د
80: - بودا، �نیروانا� را به صورت های متعددی تعریف کرده است به صورت شادی عظیم، صلح و آرامش، فناناپذیری، بدون شکل و قالب، آنسوی زمین، آنسوی آب، آنسوی آتش، آنسوی هوا، آنسوی خورشید و ماه، پایان ناپذیر و بیکران و همچنین رهایی از درگیری و منی و ریشه کن کردن حرص و طمع، کینه و دشمنی و فریب و تمامی خصوصیات ن
102: اسم شیک ایرانی و سنسکریت ، ، برارنده نامهای فرزندان ایرانی است، ، فراوانی بسیار کم دارد ، ، ، به معنای الهه شور و شوق زندگی ، ، به معنای بهشت جاویدان، ، کمال مطلق و آرامش مطلق، به معنای آنسوی هوا، آسمان 
== 728f731370565647
13: مترادف اتمسفر : ( آتمسفر ) جو، فضا، هوا، محیط، شرایط، وضعیت
14: برابر پارسی : ( آتمسفر ) هوابار، پناد | هواسپهر، هوابار، پناد
15: معنی انگلیسی : atmosphere 
21: ( آتمسفر ) ۱ - تود. هوایی که اطراف کر. زمین را فرا گرفته جو.این توده از گازهای مختلفی تشکیل شده : ۷۸ ازت ۲۱ اکسیژن ٠۳ اسید کربنیک ۹۴ آرگون ٠۱ ئیدرژن و گازهای دیگر مانند نئون هلیوم و غیره میباشد . ۲ - ( در فارسی ) محیط فضا وضع محیط . اتمسفر:طبقه بخاریاجو، طبقه هوا، واحدفشارهوا
24: فرهنگ معین
26: ( آتمسفر ) (مُ فِ ) [ فر. ] (اِ. ) ۱ - تودة هوایی که اطراف کرة زمین را فرا گرفته ، جو. ۲ - کنایه از: اوضاع و احوال . (اَ مُ فِ ) (اِ. ) نک آتمسفر. 
30: ( آتمسفر ) = اتمسفر ۱. طبقۀ هوا که گرداگرد کرۀ زمین را فراگرفته و از گازهای مختلف مانند ازت، اکسیژن، اسیدکربنیک، آرگن، هیدروژن، و غیره تشکیل شده، طبقۀ بخار یا جو.
39: اَتمُسفِر ( از یونانی باستان، راه یافته به تمام زبان های اروپایی و بسیاری زبان های دیگر ) یا جَوّ[ ۱] ( وام واژه از زبان عربی ) یا هواسپهر ( معادل فارسی ) یا پناد و همچنین ویو ( پپارسی میانه ) یک یا چند لایه از گاز است که دور یک جسم آسمانی مانند یک سیاره، ستاره، یا قمر را احاطه کرده است. جوّ به 
== 22a14f8306237399
15: معنی انگلیسی : malaria 
21: مالاریا. ( فرانسوی ، اِ ) تب لرز. تب لرزه. نوبه. تب آجامی. ( یادداشت به خط مرحوم دهخدا ). مرضی عفونی که حاملش نوعی میکرب از راسته جانوران یک سلولی و جزو هاگ داران است. میکرب این مرض بوسیله نیش پشه ٔمخصوصی بنام آنوفل که دراماکن باتلاقی و مردابها بفراوانی موجود است وارد خون بدن انسان می شود. میکرب
28: فرهنگ معین
38: مالاریا ( به انگلیسی: Malaria ) یک بیماری انگلی است. دسته ای از انگل های تک یاخته به نام پلاسمودیوم به وسیله نیش پشهٔ آنوفل ماده عامل انتقال بیماری به انسان هستند. نخست، تصور می شد که عامل مالاریا پشه آنوفل است؛ اما پشه آنوفل تنها ناقل است و عامل را منتقل می کند. 
39:این بیماری به صورت عفونت حاد در بیشتر موارد وخیم و گاهی طولانی و با ویژگی های تب متناوب و لرز، کم خونی و بزرگی طحال و گاه با ویژگی های ساده یا کشنده دیگر خودنمایی می کند. اهمیت این بیماری به خاطر شیوع زیاد و مرگ ومیر قابل توجه است. انگل مالاریا توسط یک تیره از پشه به نام آنوفل به انسان منتقل می ش
40:کلمه مالاریا یک کلمه ایتالیایی و به معنای هوای بد ( Mal - Aria ) است و منظور از آن تعریف بیماری با ویژگی های تب متناوب است که ایتالیایی ها در گذشته وجود آن را ناشی از هوای بد و مناطق باتلاقی می دانستند. همواره با گرم شدن زمین، شیوع این بیماری افزایش می یابد. 
42:علائم بیماری مالاریا در نوشته های چین باستان توضیح داده شده است. ۲۷۰۰ سال پیش از میلاد چند علامت مشخص مالاریا که بعداً به نام بیماری مالاریا نام گرفت در نایجینگ ( انگلیسی:Nei ching ) ( قانون پزشکی ) توضیح داده شد. قانون نای چینگ توسط امپراتور هوانگ تای ( انگلیسی: Huang Ti ) ویرایش شد. بیماری مالا
43:سوشروتا ( انگلیسی:Susruta ) فیلسوف هندی سده ۷ پیش از میلاد در مقاله پزشکی نوشته شده به زبان سانسکریت به علایم تب مالاریا و نیش زدن حشره معینی در ایجاد تب اشاره کرده است. تعدادی از نویسندگان رومی باتلاق را در ایجاد بیماری دخیل می دانستند. در کشور چین در سده دوم پیش از میلاد به گیاه گندواش ( به انگ
```


## [2026-10-16T05:18:41.284Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo WLD; awk 'BEGIN{RS=\"\\f\"} NR>=228 && NR<=232 {print \"=== leaf \" NR; print}' incoming/WLD/WLD_Bd1_pages.txt | grep -n 'au̯e\\|aue\\|wehen\\|ventus\\|vāta\\|väta\\|aör\\|ἀήρ\\|atmos\\|ἀτμ' | cut -c1-250 | head -20"
}
```


### [2026-10-16T05:18:41.647Z] TOOL RESULT

```
WLD
149:                                „wehen, blasen, hauchen“, in den europ. Sprachen
157:also nicht vorgr. a-; uxgatjg „scharf wehend“, dvoa/j ? „widrig wehend“, vn eg-
158:<xt)i „ubermal.iig wehend“ mit Zsdehnung); neben dem Ptc. *ue-nt- „wehend“
160:tai. cant-, gr. Acc. der r«) stand ue-ntds „Wind      in lat. ventus got. usw.
181:ahd. wajan warn „wehen“, aksl. vijq, vijati „wehen“ und „worfeln“ (davon
192:„Schneesturm ‘, zavbjdtb „verschreien“, cech. rati ( *njati „wehen“ (erst
235:«-Praes., aber in der Bed. „wehen“, auch apr. wins „Luft", Acc. winnen
241:Nebel, Luft“ (a- wohl erst nach *afd>g, ecog, kaum Dehnstufe flu- zu aue-\
305:mhd. sicadem „Rauehschwaden, Dunst‘ ags. uvadal „Rauck, Dampt”'.'.
336:    *uc-d   ahd. waym, wiaj mhd. waryn „wehen, blasen“, ivas „Windstot:V
431:  ohnedies etwas diinne Yergleichbarkeit mit a uc- „wehen“ recht unsicher
440:  heitiem Wasser kann man zweifeln. ob zu uijiiii- „wehen“ oder zu
454:                                        ue- (aue-? ue-d(li)- ?)   — uei-                                                 223
459:2.    ue- (aue-? ue-d(h)-?) „sich miihen, anstrengen“?
470:„Anstrengung“, fedil „ausdauernd“, air. ni fcdligedar „non manet“, co fedlignu r
476:uU- .,wehen“     anord. vedr, dt. Wetter vergleiclibar waren), wozu Pedersen
```


## [2026-10-16T05:18:43.654Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=228 && NR<=232 {print \"=== leaf \" NR; print}' incoming/WLD/WLD_Bd1_pages.txt | sed -n '140,165p;225,245p;280,300p' | cut -c1-200"
}
```


### [2026-10-16T05:18:44.107Z] TOOL RESULT

```
worin jedenfalls nicht ein      der Bed. „z\vei“ igegen ein idg. *ui dieser
Bed. s. *ui „auseinander“), sondern wohl Verbindung des Acc. vd> mit einem
Nom. du. *ft vorliegt, daB der St. idg. uei-, ui- gewesen sei und die bsl.
Formen mit e auf Umbildung beruhten. Urspriinglich bloB dualische Bed.
,.ich und du“ ist trotz Brugmann nicht anzunehmen,



1,     lie-       (vereinzelt ane-
                                „wehen, blasen, hauchen“, in den europ. Sprachen
         vielfacli                           dem Reinigen des Getreides von der
                                   votu „Windigen“, d. h.
         Spreu durch Werfen der Korner gegen den Wind. (Ausfiihrlich Solmsen
         Enters. 270 ft’., Persson, Wtf. 7.)
       Ai.       villi, „weht“ = gr. uym ds. (gr. a- kann Yorschlagsvokal
                                 av.   ca'ti
sein; dot;' nvev/ta Hes. ist wohl erst auf Grand von drjut gebildet, erweist
also nicht vorgr. a-; uxgatjg „scharf wehend“, dvoa/j ? „widrig wehend“, vn eg-
<xt)i „ubermal.iig wehend“ mit Zsdehnung); neben dem Ptc. *ue-nt- „wehend“

tai. cant-, gr. Acc. der r«) stand ue-ntds „Wind      in lat. ventus got. usw.
                                                                                         :
                                                                                             ‘
                                                                                                                   ,

winds ahd. ivint. cymr. gwynt „Wind“, wozu lat. ventilure „(*worfeln)

      n-Praesens:                 gr. aivco           aus *^a-v-no (vgl. zur Bildung cpaivco               :       ai.   hhali)
und aveco avecof) aus *a-faveco „reinige       Korner durch Aufriitteln vondie
der Spreu, beutle“, parai nsginxlaai Hes. (iiberliefert yavar Tteginxiaar.
                                                       '




s. auch Bechtel KZ. 46, 374); beruht     auf einem solchen schwachstufigen
«-Praes., aber in der Bed. „wehen“, auch apr. wins „Luft", Acc. winnen
„ Wetter"?
   /•-, Z-Ableitungen: gr. avga „Lufthauch, Luftzug" tsetzt eine leichte Wzf.
uue- voraus, wie askXa, aex/uov. Wetter , edavog s. u.), drjo, g. yeoog „Dunst.   ,


Nebel, Luft“ (a- wohl erst nach *afd>g, ecog, kaum Dehnstufe flu- zu aue-\
lit. urns „Luft, das Freie, Wetter", von Persson auf *a\n\ros zuriickgefiihrt,

ist       keine irgend wahrscheinliche Stiitze fur eine solche Dehnstufe).
      Gr. de/j.a, aol. aveXXa „Sturm !< (*ci£eX-ia; nicht                      Umbildung eines *afed-
germanisch wnpht-, idg. up-tlo-), ags. wapol ,,wandernd“, wcedla „Bettler.
arm", tccedl „Armut“, wiedlinn „betteln, arm sein“ (urgermanisch *wepln - >.
woneben ahd. icallon „wandern, umherzielien. wallfahrten", ags ueallian
„wandern" (aus *wudlo-ja-n; Sievers IF. 4, 337, Brugmann IF. IS. 436:
anders stellt Falk-Torp 1345 dies Yerbum als *waln- zu *ud- „walzen‘\
Kluge Wb. zu wallen „sieden“); ahd. wain „Fiicher" (aus *wr-plo oder we-lr,
s.o.); lit. vetra „Sturm, Uuwetter", aksl. v'tn ,,Luft. Wind"; auf Grund
der leichten Wzf. *mie- envachsenes *uet- vgl. uhgov ai. mil-tra vielleicht                            :




in        gr.   dsxyov" to m’Ev/ua                ,
                                                      aex/ua   '
                                                                   <pXo^ lies., axuog       kontrahiert aus asxuog,
„Dampf, Dunst, Rauch", mit Tiefstufe, aber analogischer tlbernahme des
u-Yorschlags aus den vorigen avryi) „Atem, Luftzug des Blasebalgs, des
Windes, Duft, heiBer Anhaucli des Feuers", uvr/u/jr „Atem, Windzug"

=== leaf 231
                                                                              Be
```


## [2026-10-16T05:18:48.717Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo IEC; grep -n \"^wēntos\\|^wēt-\\|^wē-\\|^wēi̯\\|^wē̆ntos\\|^wentos\\|^we̅\\|'wind'\" IEC.txt | head -15 | cut -c1-250; echo SYN; grep -n \"WIND\\b\" SYN.txt | head -5; "
}
```


### [2026-10-16T05:18:49.067Z] TOOL RESULT

```
IEC
SYN
1904:1.72 WIND Grk. — &veyos Goth. winds Lith. véjas NG Gvepos ON vindr Lett. v@78 Lat ventus Dan. vind ChSl.  véirtt It. vento Sw. vind SCr. —_ vjetar Fr. vent OE wind Boh. vftr Sp. viento ME wind Pol. = wiair Rum. vint NE wind Russ.  veter I. gaith Du. wind Skt.  vdta-, vayu-, anila- Nir. = gaoth OHG wint Av. vala- W. gwynt, awel MHG wint Br. avel, gwent NHG wind
6995:4.64 BREAK WIND, FART (vb.)
16694:5 TURN (vb.) TURN AROUND (vb) WIND, WRAP (vb) ROLL (yp)
28742:. ‘oq 1026f. Barth. 50f. 1,999. Boisacd ih Glcretostbo Grk. fndorumia, WIND aaa solous’, fr. qos (Dor. Gos) sometimes ee but more often In a good a ‘emulation, rivalry, zeal’ (-ruzla : ios form’), whence NG Siheva ; etym. dub, Walde-P. 1.775. Boisaeq 309.
```


## [2026-10-16T05:18:51.381Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1905,1925p SYN.txt | tr '\\n' ' ' | cut -c1-1800; echo; echo IEC; grep -n \"wēnt\\|wēt\\b\\|wē-\\|wē̆-\" IEC.txt | head -10 | cut -c1-250; grep -n \"\\bAIR\\b\" SYN.txt | head -3"
}
```


### [2026-10-16T05:18:51.741Z] TOOL RESULT

```
Most of the words for ‘wind’ belong to an inherited group connected with (less widespread) verbs for ‘blow’. 1. From IE *wé- ‘blow’ in Skt. va-, Grk. anu, etc. Walde-P. 1.220 ff. Ernout-M. 1086. Pedersen. 1.37, 60. Lat. ventus (> Romance words); W. gwynt, Br. gwent, W. awel, Br. avel (cf. Grk. ada ‘whirlwind’); Goth. winds, ete., general Gme. ; Lith. véjas, ChSI. vétrii, ete., general Balto-Slavic; Skt., Av. vata-, Skt. vayu-; Toch. A want, B yante. 2. Grk. aveuos : Lat. anima ‘breath’, animus ‘soul’, Skt. ana- ‘breath’, anila- ‘breath, wind’, vb. an- ‘breathe’, etc. (4.51). Walde-P. 1.56 ff. Boisacq 61. Ernout-M. 53 f. 3. Ir. gazth, NIr. gaoth, etym.? Stokes 104, 4. Skt. (beside vata-, anila-, above, 1, 2) pavana-, fr. pu- ‘cleanse, purify’; samirana-, fr. sam-r- ‘come together’, r- ‘move’. CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar others. Digitized by Arya Samaj Foundation Chennai and eGangotri THE PHYSICAL WORLD IN ITS LARGER ASPECTS 65 1.73 CLOUD : P Goth. milhma Lith.  debesis é oe ea ON sky Lett. i eat padebesis Lat nibes, nibila (pl.) Dan. sky Ghee om e : uvola, nube Sw. moln, sky SCr.  oblu List ere OE _ wolcen Boh. oblak, mrak si eit ME sky, cloud Pol. chmura, obtok Sas Sal ad NE cloud Russ, oblako Daas oy Du. wolk Skt. megha-, abhra-, ei eal OHG wolkan ghana-, etc. W. cumul MHG wolken Av. = maéya-, awra-, snao- Br. koabrenn, koumou- NHG_ wolke éa-, dvanman- lenn The relation of ‘cloud’ and ‘mist’ is such that cognate words may mean ‘cloud’? in some languages, ‘mist’ in For the frequent relationship between ‘cloud’ and ‘sky’, see 1.51. Words for ‘cloud’ are connected with words for ‘moisture’, ‘covering’, and ‘mass’. 1. IE *nebh-, *embh-, *yrbh-, in words for ‘cloud’ (> ‘sky’), ‘mist’, ‘shower’. Walde-P. 1.131. Ernout-M. 660 f. Grk. védos, ve

IEC
19624:uábio “shout, call’. WP I, 217 Hitt. wapiyami, v. ‘bark’; Go. wopjan, v. ‘shout; OHG wuoffan, sv. 7., MHG wuofen, sv. 7 and wüefen, wv. ‘howl, weep’; OE wē- pan, sv. 7. ‘weep’; ON cepa, wv. ‘shout, cry’; Óp, n. ‘shouting; weeping’, cf. ómun, f.
694:AIR
1887:AIR Lith. oras Lett. gaiss ChSl.  viizduchit SCr.  uzduh, vazduh, zrak Boh. vzduch Pol. powretrze Russ. vozduch Skt. vata-, vayu- Ay. vayu-, vayah-
```


## [2026-10-16T05:18:55.019Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1887,1903p SYN.txt | tr '\\n' ' ' | cut -c1-1500; echo; echo IEC; grep -n \"^ *u̯ē\\|^uē\\|^uēntos\\|^uēnt\\|^uētr\\|^uēi̯\\|^uē̆\\|^ue̅\" IEC.txt | head -10 | cut -c1-250; grep -n \"‘wind’\\|'wind'\" IEC.txt | head -10 | cut -c1-200"
}
```


### [2026-10-16T05:18:55.495Z] TOOL RESULT

```
AIR Lith. oras Lett. gaiss ChSl.  viizduchit SCr.  uzduh, vazduh, zrak Boh. vzduch Pol. powretrze Russ. vozduch Skt. vata-, vayu- Ay. vayu-, vayah- vayah- ‘air’ (personified), Lat. véntus ‘wind’, OE wind, etc. (1.72). Walde-P. 1.221. Hence Lat. aér, Olt. aire, It. aria, Fr. air (> ME, NE az), Sp. aire, Rum. aer, Ir. ar, NIr. aer, W. awyr, Br. aer. REW 240. Pedersen 1.203. (Grk. aiéjp, in Homer ‘sky, heavens, the upper air, ether’, above the ajp : aid ‘burn’, ai@pis ‘clear, bright’, etc. Hence Lat. aether, NE ether, etc.). 2. The Gme. group, Goth. lufius, ON lopt, OF lyft, ME lft (NE lift rare and only for ‘sky’, but the vb. lift ‘raise’ is fr. CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar airing rem Tee eis Sat Limes) aaa Digitized by Arya Samaj Foundation Chennai and eGangotri 64 SELECTED INDO-EUROPEAN SYNONYMS same source), OHG-NHG luft (> Dan., Sw. luft), is in origin the same as ON lopt ‘oft, attic, etc.’ (> ME, NE loft; OE loft ‘sky’). Development from ‘ceiling, loft’? to ‘sky, air’. Further connection prob. (but less certain and immaterial for the immediate source of ‘air’) with OHG louft ‘bark’, louba ‘roof, attic, etc.’, loub, Goth. laufs, OF léaf ‘leaf’, Lith. lupti ‘peal’, etc., with development from ‘bark’ to ‘(bark) roof, ceiling’. Walde-P. 2.418. Falk-Torp 652. 3. Lith. oras : Lett. dra ‘open field, the outdoors, the outside’, prob. fr. the the root of Lith. arti, Lett. art ‘plow’, with development indicated by the Lett. uses. Walde-P. 1.79. Mihl.-

IEC
19798:uēd- (2) (uedios) ‘wet, damp’. (Arm. type *uedio-) Oss. wdain, Dig. wodajun, inf. ‘wet; Arm. gec, gs: giči, ab. s. -av, adj. ‘wet; OE w&t, adj. ‘damp, wet; waeta, wm. “moisture, fluid"; ON vátr, adj. *wet; mod. also væta, f. *wet- ness’; cf. wæ
531:“homo” and Oscan -Umbrian ner- ‘magistrate, prince’. Cf. Skt. anilah ‘wind’ (?)
3472:eila, io ‘going, gait;, gang, troop; file, line’. Cf. ei-mi. Cf. WP I, 70, 104 Skt. ela “sport beside Irah, -am ‘wind’; ilā 'flow"; ir-te, mp. ‘go’ (ei-: i-); Gk. ale ile “gang, troop; W wyl “flo
4795:ghoit-os, à, us (1) ‘movement; going; goer. Cf. ghois-, etc. Skt. hetúh “motive, cause*; hetíh ‘missile’; Arm. get, o-st. (river, but related to Av. vaiðis ‘irrigation’: Phryg. bedu (vedu) ‘water
6214:1ló, ið ‘come, go, rush’. Cf. eilà Skt. dëm ‘come’, cf. íla ‘flow’; Irah ‘wind’; Gk. cf. hom-iléo ‘consort’; Myc. cf. om-irijo- (‘of an assembly’: homilou); OS (an, MHG (en *be eager, hurry'
15199:senouos, à (senouuo-) “twist, gut, sinew'. Cf. sneuàa, sneuor-, sinuos, ambig. Hitt. senahhas, sinahhas ‘snare, ambush’; Lat. sinus, gs: -üs, m. (2) ‘ringlet; bow of net'; cf. sinuosus, adj. ‘wi
17903:suatmos, is, à, iiə ‘vapour, smoke’ Arm. cf. kami, s. ‘wind’; Gk. atmós, m., atmë & atmís, f. ‘smoke, vapour, steam, air’; cf. atéo, v. (‘rave’, if fr. *suatejo); OLat. CH suasus, for *suassus, 
19909:ueios, à, us ‘wind, air, draught’. WP I, 220. Cf. ueio (uemi) Skt. vayüh, m. id.; Av. (short vowel) vayus, vayo, m., vayu, n. id.; Oss. cf. wájág, adj. ‘swift’; Tokh. A (?) wiyu, adj. (queried:
19990:uendh- (1) ‘turn’. WP I, 261. Cf. uondh-, undh- Skt. cf. vandhürabh, m. *chariot-seat'; Arm. cf. gind, gs: gndi, ab. s. -av, also gint, gs: gnti, s. (ring; gndak, dim. ‘tendri’; Tokh. AB wánt-, 
20182:uésmn- (uésmos, à) “breath, breeze, air, va- pour’. Cf. ues- (2). WP I, 222 Skt. vasanam, n. ‘fumigation, scenting'; Gk. cf. á-ëma, n. ‘wind’; Du. wasem, m. ‘vapour’; Latv. vēsma, f. ‘breeze’; 
20223:uëturos (uëtr-, *uétur-) “windy; wind’. Cf. uëtos, uēið | Skt. vatulah, vatalah, adj. ‘windy, airy’; Gk. cf. a-ésuros, adj. fairy, flimsy, agile’; OCS větrů (and com. SL.) ‘wind’; Li. cf. vētra
```


## [2026-10-16T05:18:59.296Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *uētos\\|^uētos\\|^uēntos\\|^uentos\\|^uēnt-\\|^uetrom\\|^uedhrom\\|uēdhrom\\|^uēio\\|^uēi̯ō\\|^ueio\" IEC.txt | cut -c1-400 | head; sed -n 17903p IEC.txt | cut -c1-500"
}
```


### [2026-10-16T05:18:59.695Z] TOOL RESULT

```
19893:ueiolos, à, is ‘twist’. Sce next ON vél, f. ‘ruse’, cf. vælindi, npl. ‘tricks’; Li. vielà, f. ‘wire’. Var. uiiolos, q.v.
19906:ueio, uiieið (3) ‘wither, droop, languish’. Cf. uaio. WP I, 227 Lat. cf. viétus, adj. (^withered', vbl. form ab- sent); Latv. viju, vit, v. intr. ‘wither’. (For Skt. váyàmi, v. ‘languish’, see uāið)
19908:ueios, à, us “twist, creeper’. Cf. ueið (1) Myc. (uncertain) wejewe, pl. ‘creepers, vines’? (also *tyres'?); Hes. cf. huié-, f. ‘vine’; Slo- vene veja, f. “branch?
19909:ueios, à, us ‘wind, air, draught’. WP I, 220. Cf. ueio (uemi) Skt. vayüh, m. id.; Av. (short vowel) vayus, vayo, m., vayu, n. id.; Oss. cf. wájág, adj. ‘swift’; Tokh. A (?) wiyu, adj. (queried: 'sur- prised’? *flattered?); G Wehe, f. “drift of sand or snow’; ON vé, npl. ‘standard’; Pol. wieja, f. “breeze; snowdrift; Cz. cf. zá-v&je, f. 'snow- drift; Li. v&jas, m. ‘wind’; Latv. vējš, m. id.
suatmos, is, à, iiə ‘vapour, smoke’ Arm. cf. kami, s. ‘wind’; Gk. atmós, m., atmë & atmís, f. ‘smoke, vapour, steam, air’; cf. atéo, v. (‘rave’, if fr. *suatejo); OLat. CH suasus, for *suassus, cpd. in-? ((smoky, dun’, if fx. *suatso-); W cf. chwad, m. ‘gust’; MHG swadem, sm. “thick vapour; G Schwadem, id. (Kluge 17 untenable). (NB. For Skt. atman, OE &pm “breath, soul”, etc. see étmn-)
```


## [2026-10-16T05:19:02.855Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in WINDOW WING FAN VENT AIR MALARIA ATMOSPHERE NIRVANA WEATHER; do grep -n \"^$w[ ,.(]\" SKT.txt | head -2 | while IFS=: read l rest; do sed -n \"${l},$((l+3))p\" SKT.txt | tr '\\n' ' ' | cut -c1-350; echo; done; done"
}
```


### [2026-10-16T05:19:03.328Z] TOOL RESULT

```
(eval):1: invalid subscript
(eval):1: invalid subscript
(eval):1: invalid subscript
(eval):1: invalid subscript
(eval):1: invalid subscript
(eval):1: invalid subscript
(eval):1: invalid subscript
(eval):1: invalid subscript
(eval):1: invalid subscript
```


## [2026-10-16T05:19:05.359Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in WINDOW WING FAN VENT AIR MALARIA ATMOSPHERE NIRVANA; do grep -n -m2 \"^${w}[ ,.(]\" SKT.txt | cut -c1-300; done"
}
```


### [2026-10-16T05:19:05.764Z] TOOL RESULT

```
21505:WINDOW.
20665:VENT.
```


## [2026-10-16T05:19:08.333Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 21505,21512p SKT.txt | tr '\\n' ' '; echo; sed -n 20665,20672p SKT.txt | tr '\\n' ' '; echo; grep -n -m3 \"^WING\\|^MALARIA\\|^AIR\\b\\|^FAN\\b\\|^ATMOSPHERE\" SKT.txt SKT_dli_revised.txt | cut -c1-300"
}
```


### [2026-10-16T05:19:08.664Z] TOOL RESULT

```
WINDOW. WINK. 565 ftn,  led.  vemfa,  Dan.  vfnJi,  Swed. }da,  Goth,  watufjan,  G.  wenJcn,  to |i;  all  can&aJ  forms. Uront.  (E.)  See  above. Rrindlass  (i),  a  machine  with  a  turning b.  (Scand.)  A  corruption  (due  to  con- no  with  the  word  below)  of  M.  £■ fdtUt  a  windlass  ;  Chaucer,  C.  T.  10408, b  ••  Iccl.  vindAu,  a  windlass.  »  Icel. \d'^  to  wind  ;  6ss,  a  pole,  ronnded  beam. t)n.  wimiiu,  O.  Du.  windtus,  a  windUss. Here  O.  Du.  aes,  Icel.  dss^  is  cognate fa  Goth.  OH/,  a  beam  (.distinct  from  Da. iO.  Do.  asit^  an  axis). NrlndlAAB  (j).  a  circuit.  (Hybrid;  £. ; i^  F.  *»!*)  Formerly  •win,ilaiu\  Ham- I  ii.  I.  65:  &c.  I*ut  for  xuinJ-ia£c,  a Iduig  course;  from  triW,  vb.,  and  iaa, koitre.  twisted  stiing,  twi!>t,  the  same M  as  rood.  £.  late ;  see  Laoe. Nronder,  sb.  (E.)  A.S.  tt'Mn(/*r,  a nent,  wonder.  Orig.  a  thing  from  which \  turns  a&ide  in  awe ;  allied  to  A.  S. ^uiiam,  to  turn  aside  from,  to  respect, icre,  M,E.  wondtn,  to  conceal  through r.  flatter,  turn  from. •A.  S.  wundcn, b  of  A.  S.  windan,  to  wind ;  the  verb \ndian  being  from  the  pL  t.  wamd, irondrous,  wonderful.  (EL)  A  cor* ^lion  of  the  old  word  wonders^  won- bos.  orig.  an  adv.,  but  also  an  adj. YmiHert^txz*  —  wondrously  dear  ;  '  v.*on- men  *  «=  wonderful  men.  Wondtrs formed  by  adding  the  adv.  Kufiix  -/ A  ecn.  ca5»e)  to  the  M.  £.  wonder, raonerful,  Chaucer,  C.T.  4^5.  This is  short  for  wonderiy,  adj.  —  A.  S. •fU,  wonderful,  the  ly  being  dronjicd Luae  it  seemed  Uke  an  advexbul  ending. KTlndow  ;  see  'Wind  (1). RTlno  (L.5  A.  S.  win,  wine ;  borrowed )fm  L.  uittym,  wine  (whence  al&o  G. ttiv,  Slc),  -^  Gk.  oTcoT,  wine ;  i^t^,  a  vine, le  Gk.  041^  is  from  V  ^h  to  wind, ibt,  twine  (sec  Withy) ;  from  the  twining >wth.  Cf.  Lilh.  a/*uynys^  hop-tendriH I.  ttJftu,  a  braid  of  hair. vignette,  a  &matl  engraving  with  oma* mied  bonier.  iF.  — L.)  Fir^t  applied  to rders  in  which  wine-leaves  ana  tendrils we  introduce*! ;  XVII  cent  —  F.  vignette, little  vine ;  pi.  vignettes,  '  branchlike trishea ; '  CoL  Dimin.  of  F.  vipu,  a vln«  (below), (F.  — L,)     F,  vi^ru.^L.,  uima,  a ;  in  late  L.  fapparemJy)  a  vine. F/,  MxwMf,  «//,  from  ai»H$im,  wine 4 
VENT. 539 fundtrt,  to  sell ;  short  for  u/nuntiart.  lit. to  give  or  ofTer  for  sale,  also  written  u^tium i/dA^.  —  L.  utMum,  sale:  dare,  to  give. vent    {2),    sale,    utterance.    \F.  — Formerly  common  ^Y.v^tUe,  sale,  selli —  F.  venJre.^'L.  tun,iere  (above). Veneer;  we  Furnish. Venerable ;  see  below. Venereal.  (L.)   Coined  from  L.  ttentrf Hs,  utneti-us,  jierlaining  lo  Venus  or  love. —  L.  Hentri-,  crude  form  of  itfntu,  love. Allied  to  Ski.  ccx/i,  to  love,  honour. venerable.    (F.— L.)    F.  vewrahU.* L.    ucjurai'iiis,    to    be    reverenced. utn-cra-ri,  to  reverence.*!*  iwHrr-,  stem of  uent4j,    love.     Der.  vetunU-ian,   from pp.  of  utturan, 
SKT_dli_revised.txt:88216:WING
```


## [2026-10-16T05:19:12.602Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 88216,88222p SKT_dli_revised.txt | tr '\\n' ' ' | cut -c1-500; echo; for w in MALARIA ATMOSPHERE 'FAN,' 'VENT,' 'WINDOW' 'NIRVANA' 'AIR,'; do l=$(grep -n -m1 \"^$w\" SKT_dli_revised.txt | cut -d: -f1); [ -n \"$l\" ] && { echo \"--$w $l\"; sed -n \"${l},$((l+5))p\" SKT_dli_revised.txt | tr '\\n' ' ' | cut -c1-400; echo; }; done"
}
```


### [2026-10-16T05:19:12.904Z] TOOL RESULT

```
Exit code 1
WING    WISTFUL    twist, twine (see Withy) ; from the twining
```


## [2026-10-16T05:19:16.756Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"bäd\\b\\|bād\\b\" HUB.txt | head -8 | cut -c1-200; grep -n \"BAD\\b\\|BĀD\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -5 | cut -c1-200; grep -n \"^باد\\b\\|باد :\" incoming/ARY/ARY_pages.txt | head -5 | cut -c1-200"
}
```


### [2026-10-16T05:19:17.070Z] TOOL RESULT

```
336:BAD 9979 ST Sod AS Anais ULE od ota glee ob ssl ye Ghdk; 52S ged
2872:OLD SCANDINAVIAN) 598 gL! BAD ABALUCHI) gx gh
2873:VINDR BAD 4AFGHAND) (p44) gait
3200:REFERENCES eh BAD ~ (ARMENIAN) ga)
3248:BARNHART. (BAD) 71 FOEDARE, (41) LATIN) ga)
1462:بادداشت:
1536:بادداشت:
1586:بادداشت:
1612:بادداشت, ۹
1683:بادداشت. 1
```


## [2026-10-16T05:19:19.783Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /VINDR/ {print \"PDFPAGE\",NR; print}' incoming/ARY/ARY_latin_index_pages.txt | head -5; grep -n \"pdf page\" incoming/ARY/ARY_latin_index_pages.txt | head -3; sed -n 2860,2880p incoming/ARY/ARY_latin_index_pages.txt | cut -c1-200"
}
```


### [2026-10-16T05:19:20.146Z] TOOL RESULT

```
PDFPAGE 101
[pdf page 101]
Cosy’ 4 SS soil LL | UT
letloak
sore tle Wigs st ste Ghd) Be Hel ol ow
1:[pdf page 1]
9:[pdf page 2]
37:[pdf page 3]
letloak
sore tle Wigs st ste Ghd) Be Hel ol ow
TATO POLISH) glen ABA (KURDISH) 52,5
TATA ASZECLL) Sop PAPPA AGREEK) gli
‘REFERENCES ocntKany PAPA, PAPPA LATIN) ops
POKORNY: SOSO*~*~*~*~*~«S PAPA (FRENCH) Wi
AMINDAROV: (FATHER) 123 PAPA SPANISH) glitoet
reer sbi aby PAL PORTUGUESE) Js y
VENTO A(ITALIAN) piste! HAVESTAN) glu
, viNT (RUMANIAN) clay, VARA, VATO, VAITI, VATA
VENTO (PORTUGUESE) Js WAD VAT (PAHLAVI) 5 shy
wivps GOTHIC) SF BA (KURDISH) 53,5
OLD SCANDINAVIAN) 598 gL! BAD ABALUCHI) gx gh
VINDR BAD 4AFGHAND) (p44) gait
VINDR (OLD NORSE) oS 7395 WANT, WANT :(TOKHARIAN A) A 5,155
‘WIND HOLD SAXON) pS gi p-S YENTE :(TOKHARIAN B) B g ,\os
WIND (OLD FRISIAN) 4S 53.5 VATA, VATAS, (SANSKRIT) ey Suite
WIND, (OLD HIGH GERMAN) nS glST ATI
WINT AENTES, ABSI, (GREEK) 36 y
WIND (GERMAN) git VATMOS, DES!
WIND — (OLD ENGLISH) 4 god VENTUS, VENTILARE (LATIN) 33
```


## [2026-10-16T05:20:12.868Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; cp $S/bqt526-n388.jpg 170.jpg; cp $S/bqt526-n425.jpg 205.jpg\ncat > 170.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, vol. 1, printed p. 170 (running head «- ۱۷۰ -», catchword اندرخور) — read from the archive.org scan\n borhan-ghate-v1 leaf n388 (https://archive.org/download/borhan-ghate-v1/page/n388.jpg). Read for Nourai p.496 (pdf 526), root We 1.]\n\nHeadwords (col. 2):\nاندرواژ - با زای فارسی بر وزن چنبرباز، بمعنی اندرواست که سرگشته وحیران - و آرزو و حاجتمندی - و سرنگون آویخته باشد.\nاندرواه ۲ - بروزن لنگرگاه، بمعنی اندرواژ است که سرگشته وحیران - واحتیاج - وسرنگون آویخته باشد.\nاندروای ۳ - بروزن صندل‌سای، بمعنی اندرواه است که سرگشته وحیران و احتیاج (۱) وسرنگون آویخته باشد.\nاندروایی ۴ - بروزن کم‌پروایی، بمعنی سرگشتگی وحیرانی - و آرزو و حاجتمندی - وسرنگونی باشد.\n(col. 1) اندروا ۲ - با واو بروزن اندرزا، بمعنی سرگشته‌وحیران‌باشد - وبمعنی آرزوو حاجتمندی هم هست - و سرنگون آویخته و واژگونرا نیز گویند.\n\nFootnote 3 (Mo'in):\n۳ - پهلوی andarvây «مناس ۲۶۶» مرکب از اندر: حرف اضافه + وای، دراوستا vayu در پهلوی وای بمعنی باد، جمعاً یعنی در هوا. ویو در اوستا نام فرشتهٔ پاسبان هواست، درسانسکریت Vâyu در پهلوی وای یا اندروای خوانده شده. در فرهنگهای فارسی درواي یا اندروای بمعنی معلق و آویخته دانسته شده ولغةً درست نیست. گویندگان پیشین‌گاه آنرا درست بکار برده بمعنی هوا گرفته‌اند. اندروای ناگزیر از واژهٔ مرکب antara vâyu آمده است. «قاب ۱: ۲۴۶».\n۴ - مرکب از: اندروای + ی (علامت حاصل مصدر)\nEOF\ncat > 205.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, vol. 1, printed p. 205 (running head «- ۲۰۵ -», catchword بادافره) — read from the archive.org scan\n borhan-ghate-v1 leaf n425 (https://archive.org/download/borhan-ghate-v1/page/n425.jpg). Read for Nourai p.496 (pdf 526), root We 1.]\n\nHeadword (col. 2, bottom):\nباد ۲ - بر وزن شاد، معروف است که یکی از چهار عنصر باشد - و نام فرشته ایست موکل برتزویج ونکاح - ونام روز بیست‌ودوم (۱) از هرماه شمسی باشد ...\n\nFootnote 2 (Mo'in):\n۲ - دراوستا vâta «بارتولمه ۱۴۰۸»، پهلوی vât «نیبرگ ۲۳۷»، «تاوادیا ۱۶۶ :۲»، گیلکی bâd، فریزندی و یرنی و نطنزی vâj «دك . ۱ ص۲۸۵»، سمنانی bâ ، bâd، سرخهٔ vâ ، شهمیرزادی bâd «دك . ۲ ص ۱۸۰». واته در اوستا مانند ودا بمعنی باد وگاه اسم خاص ایزد باد است. در یشتها سه‌بار واته بمعنی فرشته آمده. محافظت روز بیست ودوم هر ماه شمسی با اوست. ابوریحان در فهرست روزهای ایرانی این‌روز را «باد» و در سغدی و خوارزمی «واذ» یاد کرده، زرتشتیان امروز نیز ... بقیه درصفحهٔ ۲۰۶\n(بادآس is not on pp. 205-207; Mo'in's Farhang (vajehyab) has: بادآس (اِمر.) آسیاب بادی.)\nEOF\nls"
}
```


### [2026-10-16T05:22:14.117Z] TOOL RESULT

```
Command did not complete within its 120s timeout and was moved to the background (ID: bxoq027lt). Output is being written to: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tasks/bxoq027lt.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/sfmqrb/git/rishe-private; directory changes made by the backgrounded command do not apply to subsequent commands.
```


## [2026-10-16T05:22:16.319Z] TOOL CALL #69: Bash

```json
{
 "command": "wc -c /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/170.* /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/205.*"
}
```


### [2026-10-16T05:22:16.719Z] TOOL RESULT

```
 529778 /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/170.jpg
   2057 /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/170.vision.txt
 532793 /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/205.jpg
   1471 /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/205.vision.txt
1066099 total
```


## [2026-10-16T05:25:11.095Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-526.py <<'PYEOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nPIE=W+\"Reconstruction:Proto-Indo-European/h₂weh₁-\"\nPOKc={\"src\":\"POK\",\"where\":\"pp. 81-84, 10. au̯(e)-, au̯e(o)-, u̯ē- 'to blow' (POK_full.txt l.7848 ff.)\",\"stance\":\"supports\",\"note\":\"'II a. ue-, uā-: Old Indie vāti, Avestan vāiti blows ... participle *ue-nt- ... *ue-nto-s wind in Latin ventus, Gothic etc winds'; 'e. t-further formations: Old Indie vāta-h, Avestan vātō blow[=wind]'; 'Old Indie vāyu-h, Avestan vayuš blow, wind, air'.\"}\nWLDc={\"src\":\"WLD\",\"where\":\"Bd. I pp. 220-222, 1. u̯ē- (vereinzelt au̯e-) (WLD_Bd1_pages.txt leaves 229-230)\",\"stance\":\"supports\",\"note\":\"'u̯ē- „wehen, blasen, hauchen“ ... Ai. vāti „weht“ = gr. ἄησι ... av. vāiti ... neben dem Ptc. *u̯ē-nt- „wehend“ stand u̯ē-ntós „Wind“ in lat. ventus got. winds ahd. wint'.\"}\nAHDc={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wē- (AHD_watkins1985.txt l.1125)\",\"stance\":\"supports\",\"note\":\"'wē-. To blow. ... *we-dhro- in Germanic *wedram ... WEATHER. ... *wē-nt-o- ... Germanic *windaz ... WIND, WINDOW; Latin ventus: VENT, VENTAIL, VENTILATE. ... Germanic *wē-ingjaz in Old Norse vengr: WING. ... Sanskrit vāti, he blows: NIRVANA. [Pok. 10. aw(e)- 81.]'\"}\nKLNwind={\"src\":\"KLN\",\"where\":\"1971 one-vol. ed. s.v. wind, n. (KLN_1971.txt l.267376; the 1966 local text ends at 'veratrine', so p.1745 itself is not on disk)\",\"stance\":\"supports\",\"note\":\"'cogn. with OI. vātaḥ, Avestic vāta-, ... L. ventus ... All these words are derivatives of I.-E. base *wē-, to blow, whence also OI. vāti, vāyati, Avestic vāiti, blows ... Cp. weather, window, wing, winnow ... van, fan ... atmo-, bedeguar, nirvana, Vayu, vent'.\"}\nnodes=[]\ndef N(i,lang,words,verdict,der,derfa,sources,rc,cons,**kw):\n    d={\"id\":i,\"lang\":lang,\"words\":words,\"verdict\":verdict,\"derivation\":der,\"derivation_fa\":derfa,\"sources\":sources,\"ref_check\":rc,\"consulted\":cons}\n    d.update(kw); nodes.append(d)\n\nN(1,\"Avestan\",\"vâta; vâiti; vât-âs; antara-vâyu\",\"disputed\",\n \"Two of the four forms are real Avestan words: vāta- m. 'wind' (Bartholomae col. 1408, Pokorny 81-84) < Proto-Iranian *HwāHata- < PIE *h₂wéh₁n̥t-o-, the old participle 'blowing', and vāiti 'blows' (Bartholomae s.v. 2vā- 'wehen': kudat̰ vātō vāiti 'whence the wind blows', H. 2.7), the athematic Narten present *h₂wéh₁-ti, = Sanskrit vāti. The other two are not attested Avestan: 'vât-âs' 'windmill' is New Persian bād-ās (bād 'wind' + ās 'mill', MP ās) projected back into Avestan (Avestan has no word for a windmill, a Sistani invention of the Islamic period); 'antara-vâyu' is not found in Bartholomae (who has only antarə 'between' and vayu-/vaiiu- 'air, atmosphere; the god Vayu'), but is Mo'in's reconstruction in his BQT p.170 footnote ('اندروای ناگزیر از واژهٔ مرکب antara vâyu آمده است') to explain MP andarwāy 'air, atmosphere'. Vayu- itself is generally taken from *h₂weh₁-yu- (Wiktionary, Pokorny 83, Klein s.v. Vayu), so the elements are of this root, but the compound is a reconstruction and Nyberg derives MP andar-vāy instead from *andar-vāz (Parthian ʼndrwʼz, verb vaz- 'move, blow').\",\n \"«واتَ» (vāta-) اوستایی به معنای «باد» و «وایتی» (vāiti) «می‌وزد» واژه‌های واقعی اوستایی‌اند (بارتولومه، ستون ۱۴۰۸) و از ریشهٔ هندواروپایی آغازین *h₂weh₁- «وزیدن» آمده‌اند؛ vāta- در اصل صفت فاعلی «وزنده» است. اما «vât-âs» (آسیای بادی) واژه‌ای اوستایی نیست، بلکه همان «بادآس» فارسی است که به اوستا بازتابانده شده؛ «antara-vâyu» هم در واژه‌نامهٔ بارتولومه نیست و بازسازی معین در حاشیهٔ برهان قاطع (ص ۱۷۰) برای توضیح پهلوی andarwāy است. پس دو صورت نخست درست است و دو صورت دیگر ساختگی یا بازسازی‌اند و در اوستا گواهی ندارند.\",\n [PIE,W+\"باد\"],\n [{\"ref\":\"POK:81\",\"status\":\"supports\",\"note\":\"Pokorny pp. 81-84 (POK_full.txt l.7848 ff.): 'Old Indie vāti, Avestan vāiti blows'; 'Old Indie vāta-h, Avestan vātō blow[wind]'; 'Old Indie vāyu-h, Avestan vayuš blow, wind, air'. Nothing on vât-âs or a compound antara-vāyu.\"},\n  {\"ref\":\"KLN:1745\",\"status\":\"partial\",\"note\":\"p.1745 (s.v. wind) is beyond the end of the local 1966 text; the same entry in the 1971 edition (KLN_1971.txt l.267376): 'Avestic vāta- ... Avestic vāiti, blows'. Supports vāta/vāiti only.\"},\n  {\"ref\":\"BQT:170\",\"status\":\"supports\",\"note\":\"BQT vol.1 p.170 (archive.org borhan-ghate-v1 n388; transcribed in ocr/BQT/170.vision.txt), Mo'in fn.3 s.v. اندروای: 'پهلوی andarvây ... مرکب از اندر + وای، دراوستا vayu ... اندروای ناگزیر از واژهٔ مرکب antara vâyu آمده است' - Nourai's antara-vâyu is Mo'in's inferred compound, not a quoted Avestan text form.\"}],\n [{\"src\":\"BRT\",\"where\":\"col. 1408 s.v. vāta- and s.v. 2vā- 'wehen' (BRT.txt l.23407-23412, 23437)\",\"stance\":\"supports\",\"note\":\"''vā- V. 'wehen' vom Wind ... kudat̰ vātō vāiti yim ... \\\"woher weht hier der Wind\\\" H.2.' ; index line 'vāta- 1408'.\"},\n  {\"src\":\"BRT\",\"where\":\"s.v. vayav-/vaya- (BRT.txt l.22690)\",\"stance\":\"partial\",\"note\":\"''vayav-, 'vaya- m. 'Luft, Atmosphäre', als Gottheit' - vayu- exists; no compound antara-vayu- found (grep 'antar.*vay' empty).\"},\n  {\"src\":\"NYB\",\"where\":\"Part II p.? s.v. andar-vāi (NYB_vol2_glossary.txt l.448)\",\"stance\":\"contradicts\",\"note\":\"'andar-vāi [ʼndlwʼy] the atmosphere ... SW form < *andar-vāz, MPrth ʼndrwʼz ... From andar + vaz-, v. vazitan' - Nyberg derives MP andarwāy from andar + vaz-, not from a compound with vayu-.\"},\n  POKc]\n)\nN(2,\"Persian\",\"bâd; bâdâs; andarvâ\",\"plausible\",\n \"bād 'wind' < MP wād (MacKenzie 'wād [wʼt] wind, breath, spirit') < OIr. *wāta- (Av. vāta-): Old Iranian intervocalic -t- voiced to -d- in Middle Persian, and initial w- became b- in New Persian (as wahār > bahār, wafr > barf) - confirmed (Horn no.151, Wiktionary, Mo'in fn. BQT p.205). bādās 'windmill' is a New Persian compound bād + ās 'mill' (MP ās; Mo'in, Dehkhoda: 'آس بمعنی آسیا که با باد گردد') - confirmed as a Persian formation, not an inheritance from Avestan. andarvā (with اندرواژ، اندروای) continues MP andarwāy 'air, atmosphere' (MacKenzie; Nyberg andar-vāi), originally 'in the air' > 'suspended, hanging upside down' > 'bewildered, needy'; Borhan's glosses 'سرگشته و حیران، احتیاج' are the ones Nourai renders 'wandering, poor', which Mo'in calls lexically unjustified ('لغةً درست نیست'). The analysis andar + wāy (= Av. vayu- 'air') is Mo'in's and MacKenzie's; Nyberg prefers andar + vāz 'blow, move' (Parthian ʼndrwʼz), so the exact second element is debated. Extras بادبان (sail, MP wādbān), بادبادک (kite), بادخن are transparent bād-compounds.\",\n \"«باد» از فارسی میانهٔ wād و آن از ایرانی باستان *wāta- (اوستایی vāta-) است: «ت» میان دو واکه در فارسی میانه به «د» نرم شده و «و» آغازین در فارسی نو به «ب» بدل شده (چنان‌که در wahār > بهار)؛ این بخش بی‌گمان درست است (هرن شمارهٔ ۱۵۱، معین در حاشیهٔ برهان ص ۲۰۵). «بادآس» ترکیبی فارسی از «باد» + «آس» (آسیا) است، نه بازماندهٔ واژه‌ای اوستایی. «اندروا/اندروای/اندرواژ» از پهلوی andarwāy «هوا، فضا» است، یعنی «در هوا» ← «معلق، سرنگون آویخته» ← «سرگشته و نیازمند»؛ معین معنای «سرگشته» را لغةً نادرست می‌داند. معین و مکنزی جزء دوم را «وای» (= اوستایی vayu «هوا») می‌دانند، ولی نیبرگ آن را از andar + vāz «وزیدن، جنبیدن» (پارتی ʼndrwʼz) می‌گیرد؛ پس این بخش با احتیاط پذیرفتنی است.\",\n [W+\"باد\",\"https://vajehyab.com/moein/بادآس\",\"https://abadis.ir/fatofa/بادآس/\",\"https://abadis.ir/fatofa/اندروا/\"],\n [{\"ref\":\"BQT:205\",\"status\":\"supports\",\"note\":\"BQT vol.1 p.205 (borhan-ghate-v1 n425; ocr/BQT/205.vision.txt), Mo'in fn.2 s.v. باد: 'دراوستا vâta «بارتولمه ۱۴۰۸»، پهلوی vât «نیبرگ ۲۳۷» ... گیلکی bâd ... سمنانی bâ، bâd'. بادآس itself is not on pp.205-207.\"},\n  {\"ref\":\"BQT:170\",\"status\":\"supports\",\"note\":\"p.170 (n388): headwords اندروا/اندرواژ/اندرواه/اندروای 'سرگشته وحیران - و آرزو و حاجتمندی - و سرنگون آویخته'; Mo'in fn.3: 'پهلوی andarvây ... مرکب از اندر + وای ... جمعاً یعنی در هوا ... در فرهنگهای فارسی ... بمعنی معلق و آویخته دانسته شده ولغةً درست نیست'.\"}],\n [{\"src\":\"HRN\",\"where\":\"no. 151, p. 39 (HRN.txt l.1728)\",\"stance\":\"supports\",\"note\":\"'151. bād 'Wind', ... aw. vāta- 'Wind'; phlv. vāt; ai. vāta-, kurd. ba, wā; afɣ. wō; oss. wad'.\"},\n  {\"src\":\"PHD\",\"where\":\"s.v. wād (PHD.txt l.603) and andarwāy (English index l.761, 880; PHD_mackenzie.txt l.1091)\",\"stance\":\"supports\",\"note\":\"'wād [wʼt | M wd, N bād] wind, breath, spirit'; 'wādbān [... N bādbān] sail'; 'andarwāy [ʼndlwʼd | (P ʼndrwʼz)] air, atmosphere'; '*way [wd = Av. wayu-] air, atmosphere'.\"},\n  {\"src\":\"NYB\",\"where\":\"Part II s.v. andar-vāi (NYB_vol2_glossary.txt l.448)\",\"stance\":\"partial\",\"note\":\"'andar-vāi the atmosphere ... SW form < *andar-vāz, MPrth ʼndrwʼz ... From andar + vaz-' - same MP word, different analysis of the second element.\"},\n  {\"src\":\"ARY\",\"where\":\"pdf page 101 (printed p.102), entry باد (ARY_latin_index_pages.txt l.2860-2880)\",\"stance\":\"supports\",\"note\":\"Latin-script cognate list under باد: 'VATA, VATO, VAITI (AVESTAN); WAD, VAT (PAHLAVI); VATA, VATAS (SANSKRIT); VENTUS, VENTILARE (LATIN); VINDR (OLD NORSE)'.\"},\n  {\"src\":\"MON\",\"where\":\"vajehyab moein/بادآس; abadis (Dehkhoda) بادآس, اندروا\",\"stance\":\"supports\",\"note\":\"Mo'in: 'بادآس (اِمر.) آسیاب بادی'; Dehkhoda: 'آس بمعنی آسیا که با باد گردد. آسیای بادی. مرکب از دو کلمه آس و باد'; Dehkhoda s.v. اندروا: 'سرنگون آویخته ... معلق ... در هوا (فرهنگ فارسی معین)'.\"}]\n)\nN(3,\"Sanskrit\",\"nir-vanah\",\"confirmed\",\n \"Sanskrit nirvāṇa- n. 'blowing out, extinction (of a flame); final emancipation' = nis-/nir- 'out' + vāna- 'blown', past participle of vā- 'to blow' (vāti 'blows' < *h₂wéh₁-ti); the n of -vāna- becomes retroflex ṇ after the r of nir-. The book's 'nirvanah' copies Klein's 'OI. nirvanah' (a nominative -aḥ form); the standard citation form is nirvāṇa. Derivation from the root and gloss are correct (Wiktionary, Klein, AHD).\",\n \"واژهٔ سنسکریت nirvāṇa «خاموش شدن (شعله) با دمیدن، فرونشستن؛ رهایی نهایی» از پیشوند nis-/nir- «بیرون» و vāna- «دمیده»، صفت مفعولی از ریشهٔ vā- «وزیدن، دمیدن» ساخته شده که هم‌ریشهٔ «باد» فارسی است؛ n پس از r به ṇ برگشتی بدل شده است. صورت «nirvanah» کتاب از کلاین گرفته شده و صورت معیار nirvāṇa است. ادعای نورایی درست است.\",\n [W+\"निर्वाण\",W+\"nirvana\"],\n [{\"ref\":\"KLN:1049\",\"status\":\"supports\",\"note\":\"Klein 1966 s.v. nirvana (KLN_1966.txt l.25465): 'OI. nirvanah, lit. a blowing out (of a light), extinction, disappearance, which is formed fr. nis-, nir-, out, forth, away ... and vāti, it blows, for whose etymology see wind, n.'\"}],\n [AHDc,{\"src\":\"POK\",\"where\":\"p. 82 (POK_full.txt l.7848 ff.)\",\"stance\":\"supports\",\"note\":\"'Old Indie vāti ... blows' under 10. au̯(e)- 'to blow' (base of vāna-).\"},\n  {\"src\":\"KLN\",\"where\":\"1971 s.v. wind, n. (KLN_1971.txt l.267376)\",\"stance\":\"supports\",\"note\":\"'Cp. also ... nirvana, Vayu, vent'.\"}]\n)\nN(4,\"Persian\",\"nîrvânâ\",\"plausible\",\n \"Persian نیروانا nirvānā is a modern learned loan of Sanskrit nirvāṇa, entering Persian in the 20th c. through Indological and European writing on Buddhism (cf. English/French nirvana); the final long -ā reflects the European/Hindi pronunciation rather than a direct Sanskrit -a. The chart's direct Sanskrit → Persian arrow is acceptable in substance (the word is ultimately Sanskrit and dictionaries tag it 'سنسکریت'), but the immediate route of transmission is not documented.\",\n \"«نیروانا» وام‌واژه‌ای نو و دانشورانه از سنسکریت nirvāṇa است که در سدهٔ بیستم از راه نوشته‌های هندشناسی و اروپایی دربارهٔ آیین بودا به فارسی آمده؛ «ا»ی پایانی بلند نشان تلفظ اروپایی یا هندی است. اصل سنسکریت واژه درست است، اما مسیر مستقیم «سنسکریت ← فارسی» گواهی روشنی ندارد؛ پس با احتیاط پذیرفتنی است.\",\n [W+\"nirvana\",\"https://abadis.ir/fatofa/نیروانا/\"],\n [{\"ref\":\"MON:4882\",\"status\":\"not_checked\",\"note\":\"Mo'in vol. page cannot be mapped online; vajehyab moein/نیروانا returned no entry (archived, 136 bytes). Abadis (archived) gives 'نیروانا (سنسکریت) ... آخرین مرحله سلوک در نزد بودا'.\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. nirvana (l.25465)\",\"stance\":\"supports\",\"note\":\"'nirvana, n., extinction of the individual soul by absorption into the supreme spirit (Hinduism) - OI. nirvanah' (source of Nourai's gloss).\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wē-\",\"stance\":\"supports\",\"note\":\"'Sanskrit vāti, he blows: NIRVANA'.\"},\n  {\"src\":\"MON\",\"where\":\"abadis.ir/fatofa/نیروانا (name dictionary section)\",\"stance\":\"partial\",\"note\":\"'نیروانا (سانسکریت) ... (تلفظ: nirvānā) (انگلیسی: nirvana)' - Sanskrit origin, transmission route not stated.\"}]\n)\nN(5,\"English\",\"Nirvana\",\"confirmed\",\n \"English nirvana (first recorded 1836 in Orientalist writing on Buddhism) is borrowed from Sanskrit nirvāṇa 'blown out, extinguished' (nis 'out' + vā 'to blow'); Klein's gloss 'extinction of the individual soul by absorption into the supreme spirit' is Nourai's.\",\n \"نیروانای انگلیسی (نخستین‌بار ۱۸۳۶ در نوشته‌های خاورشناسان دربارهٔ آیین بودا) وام‌واژه از سنسکریت nirvāṇa «خاموش‌شده با دمیدن» است. معنایی که نورایی آورده همان تعریف کلاین است. ادعای نورایی درست است.\",\n [W+\"nirvana\"],\n [{\"ref\":\"AHD:889\",\"status\":\"supports\",\"note\":\"1976 page 889 not accessible; Watkins 1985 s.v. wē- (AHD_watkins1985.txt l.1125): '4. Basic form *wē- in Sanskrit vāti (stem *vā-), he blows: NIRVANA'; index 'NIRVANA wē-'.\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. nirvana (l.25465)\",\"stance\":\"supports\",\"note\":\"'nirvana ... OI. nirvanah, lit. a blowing out (of a light)'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 index (l.1923)\",\"stance\":\"supports\",\"note\":\"'NIRVANA wē-'.\"}]\n)\nN(6,\"Germanic\",\"windaz, wedram; vind-auga; wě-ingia\",\"confirmed\",\n \"Proto-Germanic *windaz 'wind' < PIE *h₂wéh₁n̥t-o-, the thematized participle 'blowing' (Grimm's law does not touch w; *-ēnt- > *-int- by Osthoff shortening and raising), cognate with Latin ventus. *wedrą 'weather' < *wedʰrom, a shortened *h₂weh₁-dʰro- 'blowing' (AHD *we-dhro-, Wiktionary; Pokorny 81 'u̯e-dʰro- presumably in Old Norse veðr'). Old Norse vindauga 'window', literally 'wind-eye', is a North Germanic compound of vindr 'wind' + auga 'eye' (PIE *h₃ekʷ-), not common Germanic. Old Norse vængr 'wing' < PGmc *wēingijaz, a derivative of *wē- 'blow' (AHD, Wiktionary, Klein 'rel. to Du. waaien, to blow').\",\n \"ژرمنی آغازین *windaz «باد» از *h₂wéh₁n̥t-o- هندواروپایی، صفت فاعلی «وزنده»، است و با ventus لاتین هم‌ریشه است؛ *wedrą «هوا، آب‌وهوا» از *wedʰrom با پسوند ابزار از همین ریشه است. vindauga «پنجره» ترکیبی نورس کهن از vindr «باد» + auga «چشم» (= «چشمِ باد») است. vængr «بال» نورس کهن از *wēingijaz ژرمنی و باز از ریشهٔ «وزیدن» است. همهٔ این وابستگی‌ها را پژوهش امروزی (واتکینز، ویکی‌واژه، کلاین) تأیید می‌کند.\",\n [W+\"wind\",W+\"weather\",W+\"window\",W+\"wing\",PIE],\n [{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. wē- (l.1125): '*we-dhro- in Germanic *wedram ... WEATHER'; '*wē-nt-o- ... Germanic *windaz in (i) Old English wind ... (ii) Old Norse vindr: WINDOW'; 'Suffixed Germanic form *wē-ingjaz in Old Norse vengr, wing'.\"}],\n [AHDc,POKc,WLDc,\n  {\"src\":\"KLN\",\"where\":\"1971 s.v. weather, window, wing (KLN_1971.txt l.265607, 267446, 267477)\",\"stance\":\"supports\",\"note\":\"weather: 'OE. weder ... ON. veðr ... and cogn. with OSlav. vĕtrŭ ... and prob. also with OI. vātaḥ, wind'; window: 'fr. ON. vindauga, lit. windeye'; wing: 'ON. vængr ... rel. to Du. waaien, to blow ... OE. wāwan, to blow'.\"},\n  {\"src\":\"SYN\",\"where\":\"1.72 WIND (SYN.txt l.1904-1910)\",\"stance\":\"supports\",\"note\":\"'From IE *wē- blow in Skt. vā-, Grk. ἄημι ... Lat. ventus ... Goth. winds, etc., general Gmc.; ... Skt., Av. vāta-, Skt. vāyu-'.\"}]\n)\nN(7,\"English\",\"wind, weather; window; wing\",\"confirmed\",\n \"English wind < Old English wind < PGmc *windaz; weather < OE weder 'storm, weather' < PGmc *wedrą; window < Middle English wyndowe, borrowed (13th c.) from Old Norse vindauga 'wind-eye', displacing OE ēagþyrel 'eye-hole'; wing < ME wenge (12th c.) from Old Norse vængr, replacing OE fiþere. All four ultimately from *h₂weh₁- 'blow' (Wiktionary, Klein, AHD).\",\n \"wind انگلیسی از انگلیسی کهن wind و آن از ژرمنی *windaz است؛ weather از انگلیسی کهن weder «توفان، هوا»؛ window در انگلیسی میانه (سدهٔ ۱۳) از نورس کهن vindauga «چشم باد» وام گرفته شد؛ wing نیز در سدهٔ ۱۲ از نورس کهن vængr وام گرفته شد. هر چهار به ریشهٔ «وزیدن» می‌رسند. ادعای نورایی درست است.\",\n [W+\"wind\",W+\"weather\",W+\"window\",W+\"wing\"],\n [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"Nourai cites no reference for this node; checked against AHD/Klein below.\"}],\n [AHDc,{\"src\":\"KLN\",\"where\":\"1971 s.v. wind, weather, window, wing\",\"stance\":\"supports\",\"note\":\"'wind, n., air in motion. - ME. wind, fr. OE. wind'; 'weather, n. - ME. weder, storm, fr. OE. weder'; 'window, n. - ME. windoge, windowe, fr. ON. vindauga'; 'wing, n. - ME. wenge, winge, of Scand. origin'.\"}]\n)\nN(8,\"Latin\",\"ventus\",\"confirmed\",\n \"Latin ventus 'wind' < Proto-Italic *wēntos < PIE *h₂wéh₁n̥t-o-s, the participle 'blowing' of *h₂weh₁- (Osthoff's law shortening *ē before -nt-); exact cognate of Germanic *windaz and Welsh gwynt (Wiktionary, Pokorny 82, Walde-Pokorny I 220).\",\n \"لاتین ventus «باد» از ایتالیک آغازین *wēntos و آن از *h₂wéh₁n̥tos هندواروپایی، صفت فاعلی «وزنده» از ریشهٔ *h₂weh₁- است و دقیقاً هم‌ریشهٔ wind ژرمنی و gwynt ولزی است. ادعای نورایی درست است.\",\n [W+\"ventus\",PIE],\n [{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. wē-: 'b. Latin ventus, wind: VENT, VENTAIL, VENTILATE'.\"}],\n [POKc,WLDc,{\"src\":\"SYN\",\"where\":\"1.72 WIND\",\"stance\":\"supports\",\"note\":\"'From IE *wē- blow ... Lat. ventus (> Romance words)'.\"}]\n)\nN(9,\"English\",\"vent, fan\",\"plausible\",\n \"vent 'outlet for air' comes partly from French vent 'wind' < Latin ventus and partly from French éventer 'to expose to air' (é- + vent); a separate vent 'slit in a coat' is from French fente (fendre), merged in spelling (Klein, Wiktionary) - the air sense is correctly from ventus. fan, however, is not from ventus: Old English fann 'winnowing fan' was borrowed from Latin vannus 'winnowing-basket', usually derived from *wat-no- of the same root (Pokorny 84 'Latin vannus from *uat-nó-s'; AHD puts it under the related root wet-1), though de Vaan doubts the connection. Same root, but a different Latin word than the arrow implies.\",\n \"vent انگلیسی (روزنهٔ هوا) بخشی از فرانسوی vent «باد» < لاتین ventus و بخشی از فرانسوی éventer است، پس این بخش درست است. اما fan «بادبزن» از ventus نیست: انگلیسی کهن fann از لاتین vannus «غربال بادافشان» وام گرفته شده که آن را معمولاً از *wat-no- از همین ریشهٔ «وزیدن» می‌دانند (پوکورنی ۸۴؛ واتکینز آن را زیر ریشهٔ خویشاوند wet- آورده)، و دی‌واان در آن تردید دارد. پس ریشه یکی است، ولی واژهٔ میانجی لاتین دیگری است؛ با احتیاط پذیرفتنی.\",\n [W+\"vent\",W+\"fan\",W+\"vannus\"],\n [{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985: VENT under wē- ('Latin ventus, wind: VENT'); FAN under wet-1 'Related to wē-': '3. Suffixed variant form *wat-no- in Latin vannus, a winnowing fan: FAN, VAN'.\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. vent (l.41227-41228), fan (l.14353)\",\"stance\":\"partial\",\"note\":\"'vent, n., 1) outlet for air ... Partly fr. F. vent, wind, fr. L. ventus; partly fr. F. évent'; 'fan, n., an instrument for winnowing. - ME., fr. OE. fann, fr. L. vannus, winnowing fan'.\"},\n  {\"src\":\"POK\",\"where\":\"p. 84\",\"stance\":\"supports\",\"note\":\"'Latin vannus winnowing-fan (from *uat-nó-s ...; from Latin comes ... Old English fann)'.\"}]\n)\nN(10,\"Greek\",\"atmo\",\"plausible\",\n \"Greek ἀτμός 'steam, vapour, smoke' (not primarily 'air') is contracted from *ἀετμός (Hesychius ἀετμόν 'wind'), traditionally from *h₂weh₁- (cf. ἄημι 'blow'): Walde-Pokorny I 221 and Pokorny 83 'ἀτμός contracted from ἀετμός', AHD under wet-1 '*awet-mo- in Greek atmos'. Wiktionary calls the origin uncertain because the vocalism is unexplained, and Mann (IEC) sets up a different *swatmos. The connection is the standard but not a secure one.\",\n \"یونانی ἀτμός به معنای «بخار، دود» (و نه دقیقاً «هوا») از صورت کهن‌تر *ἀετμός است و به‌طور سنتی از ریشهٔ *h₂weh₁- «وزیدن» (هم‌ریشه با ἄημι «می‌وزم») دانسته می‌شود (والده-پوکورنی، پوکورنی ۸۳، واتکینز). ویکی‌واژه به سبب ناسازگاری واکه‌ها آن را نامطمئن می‌داند و مان ریشهٔ دیگری (*swatmos) پیشنهاد کرده است. پس با احتیاط پذیرفتنی است.\",\n [W+\"ἀτμός\",PIE],\n [{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 s.v. wet-1 (l.1165), not wē-: 'Related to wē-. ... Oldest basic form *awet- ... in suffixed form *awet-mo- in Greek atmos (< *aetmos), breath, vapor: ATMOSPHERE'.\"}],\n [{\"src\":\"POK\",\"where\":\"p. 81 I.e (POK_full.txt l.7848 ff.)\",\"stance\":\"supports\",\"note\":\"'e. au-et-: gr. ἀετμόν τὸ πνεῦμα Hes. ... ἀτμός (contracted from ἀετμός) vapour, smoke'.\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I p. 221\",\"stance\":\"supports\",\"note\":\"'ἀτμός kontrahiert aus ἀετμός „Dampf, Dunst, Rauch“, mit Tiefstufe'.\"},\n  {\"src\":\"IEC\",\"where\":\"s.v. suatmos (IEC.txt l.17903)\",\"stance\":\"contradicts\",\"note\":\"'suatmos ... vapour, smoke ... Gk. atmós ... smoke, vapour, steam, air' - Mann derives it from a different root *swat-.\"}]\n)\nN(11,\"Latin\",\"\",\"confirmed\",\n \"Pass-through node: New Latin atmosphaera, a 17th-century scholarly coinage from Greek ἀτμός 'vapour' + σφαῖρα 'sphere' (Latin sphaera), first applied to the vapour envelope supposed around the Moon; Wilkins used English atmosphere in 1638.\",\n \"گرهٔ میانجی: لاتین نو atmosphaera، واژه‌ای دانشورانه از سدهٔ هفدهم، از یونانی ἀτμός «بخار» + σφαῖρα «کره»، نخست برای پوستهٔ بخاری که گرد ماه گمان می‌کردند. ادعای نورایی درست است.\",\n [W+\"atmosphere\"],\n [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference cited for this node.\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. atmosphere (l.3859)\",\"stance\":\"supports\",\"note\":\"'Compounded of Gk. ἀτμός, steam, vapor, and σφαῖρα, ball, sphere ... first used by the English bishop and scientist John Wilkins (1614-72) in 1638 with reference to the moon'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wet-1\",\"stance\":\"supports\",\"note\":\"'Greek atmos ... ATMOSPHERE'.\"}]\n)\nN(12,\"French\",\"\",\"confirmed\",\n \"Pass-through node: French atmosphère (17th c.), from New Latin atmosphaera; it is the immediate source of the Persian word (Mo'in tags آتمسفر [فر.]) and, per Wiktionary, of English atmosphere as well.\",\n \"گرهٔ میانجی: فرانسوی atmosphère (سدهٔ هفدهم) از لاتین نو atmosphaera؛ همین واژهٔ فرانسوی سرچشمهٔ مستقیم «آتمسفر» فارسی است (معین: [فر.]). ادعای نورایی درست است.\",\n [W+\"atmosphere\",\"https://vajehyab.com/moein/آتمسفر\"],\n [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference cited for this node.\"}],\n [{\"src\":\"MON\",\"where\":\"vajehyab moein/آتمسفر\",\"stance\":\"supports\",\"note\":\"'آتمسفر (مُ فِ) [ فر. ] (اِ.) ۱ - تودهٔ هوایی که اطراف کرهٔ زمین را فرا گرفته، جو'.\"},\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. atmosphere\",\"stance\":\"supports\",\"note\":\"Gk. ἀτμός + σφαῖρα, 17th-c. coinage.\"}]\n)\nN(13,\"Persian\",\"âtmosfer\",\"confirmed\",\n \"Persian آتمسفر / اتمسفر ātmosfer 'atmosphere; (fig.) ambience' is a 19th-20th c. loan from French atmosphère (Mo'in [فر.]); French final -ère is rendered -er. The native equivalents are جو (Arabic) and the coinage هواسپهر.\",\n \"«آتمسفر» (اتمسفر) در سده‌های نوزدهم و بیستم از فرانسوی atmosphère وام گرفته شده (معین: [فر.])؛ پایانهٔ -ère فرانسوی در فارسی -er شده است. برابرهای آن «جوّ» (عربی) و «هواسپهر» است. ادعای نورایی درست است.\",\n [\"https://vajehyab.com/moein/آتمسفر\",\"https://abadis.ir/fatofa/آتمسفر/\"],\n [{\"ref\":\"MON:32\",\"status\":\"supports\",\"note\":\"Print page not mappable online; Mo'in's entry on vajehyab (archived): 'آتمسفر (مُ فِ) [ فر. ] (اِ.) ۱ - تودهٔ هوایی که اطراف کرهٔ زمین را فرا گرفته، جو. ۲ - کنایه از: اوضاع و احوال'.\"}],\n [{\"src\":\"MON\",\"where\":\"abadis.ir/fatofa/آتمسفر (Mo'in section)\",\"stance\":\"supports\",\"note\":\"'(آتمسفر) (مُ فِ ) [ فر. ] (اِ. )'.\"},\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. atmosphere\",\"stance\":\"supports\",\"note\":\"Source word Gk. ἀτμός + σφαῖρα (European coinage, so Persian can only have it via a European language).\"},\n  {\"src\":\"ARY\",\"where\":\"pdf page 101, entry باد (ARY_latin_index_pages.txt)\",\"stance\":\"partial\",\"note\":\"Aryanpur lists Greek '(A)ATMOS' among the cognates of باد, i.e. treats atmos as of the 'blow' root; no entry for the loan آتمسفر.\"}]\n)\nN(14,\"English\",\"atmosphere\",\"confirmed\",\n \"English atmosphere (1638, John Wilkins) from New Latin atmosphaera (Wiktionary: via French atmosphère), from Greek ἀτμός 'vapour' + σφαῖρα 'sphere'.\",\n \"atmosphere انگلیسی (۱۶۳۸، جان ویلکینز) از لاتین نو atmosphaera (به گفتهٔ ویکی‌واژه از راه فرانسوی atmosphère)، از یونانی ἀτμός «بخار» + σφαῖρα «کره» است. ادعای نورایی درست است.\",\n [W+\"atmosphere\"],\n [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference cited for this node.\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. atmosphere (l.3859)\",\"stance\":\"supports\",\"note\":\"'first used by ... John Wilkins ... in 1638'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 index (l.1266)\",\"stance\":\"supports\",\"note\":\"'ATMOSPHERE wet-1'.\"}]\n)\nN(15,\"Greek\",\"aěr\",\"disputed\",\n \"Greek ἀήρ (Ionic ἠήρ, gen. ἠέρος) meant 'mist, haze' in Homer and later 'air'. Older handbooks put it under *u̯ē- 'blow' (Walde-Pokorny I 221; Buck 1.71 follows WP), but Pokorny 1959 explicitly removes it ('ἀήρ ... stays away, see u̯er- bind, hang up'), Watkins/AHD places it 'possibly' under *wer-2 'raise, hold suspended' (with ἀείρω), Klein calls it of uncertain origin, possibly 'that which rises' (ἀείρω), and Beekes (cited on Wiktionary) reconstructs *h₂ews-ér 'morning mist' from *h₂ews- 'dawn' (cf. αὔρα, Latin aurōra). Modern scholarship thus does not derive ἀήρ from *h₂weh₁-.\",\n \"یونانی ἀήρ در هومر به معنای «مه، تیرگی» و سپس «هوا» است. واژه‌نامه‌های کهن‌تر (والده-پوکورنی، باک) آن را از ریشهٔ «وزیدن» می‌دانستند، اما پوکورنی (۱۹۵۹) آن را صریحاً از این ریشه بیرون گذاشته و به *u̯er- «آویختن، بلند کردن» می‌برد، واتکینز آن را «شاید» زیر *wer- «بلند کردن» آورده، کلاین آن را نامعلوم می‌داند و بیکس آن را از *h₂ewsér «مه بامدادی» از ریشهٔ *h₂ews- «سپیده‌دم» می‌گیرد. پس پژوهش امروزی پیوند ἀήر با ریشهٔ «وزیدن» را نمی‌پذیرد.\",\n [W+\"ἀήρ\",W+\"air\"],\n [{\"ref\":\"AHD\",\"status\":\"contradicts\",\"note\":\"Watkins 1985 s.v. wer-2 'To raise, lift, hold suspended' (l.1125 block): 'Possibly referred to this root (obscure basic form *awer-) is Greek aēr (> Latin aer > Italian aria), air: AERIAL, AERO-, AIR, ARIA, MALARIA'; index 'MALARIA wer-2'.\"}],\n [{\"src\":\"POK\",\"where\":\"p. 81 I.d (POK_full.txt l.7848 ff.)\",\"stance\":\"contradicts\",\"note\":\"'gr. αὔρα aerial breath ... but app. Gen. ἠέρος smoke, fog, air stays away, see below u̯er- bind, hang up'.\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I p. 221\",\"stance\":\"supports\",\"note\":\"r-derivatives: 'gr. αὔρα „Lufthauch, Luftzug“ ... ἀήρ, g. ἠέρος „Dunst, Nebel, Luft“' listed under u̯ē- (the older view Nourai follows).\"},\n  {\"src\":\"SYN\",\"where\":\"1.71 AIR (SYN.txt l.1887 ff.)\",\"stance\":\"partial\",\"note\":\"Buck groups Skt./Av. vāyu- 'air' with ventus, wind 'Walde-P. 1.221. Hence Lat. aēr, OIt. aire, It. aria, Fr. air (> ME, NE air)', following WP.\"},\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. air (l.2051)\",\"stance\":\"contradicts\",\"note\":\"'Gk. ἀήρ ... and the rel. αὔρα ... are of uncertain origin. They are possibly rel. to ἀείρειν, to lift up, raise, and lit. mean that which rises'.\"}]\n)\nN(16,\"English\",\"air\",\"confirmed\",\n \"English air < Middle English aire < Old French air < Latin āēr < Greek ἀήρ; the chart's direct Greek → English arrow skips the Latin and Old French stages, but the chain itself is undisputed (Klein, Wiktionary). It displaced Old English lyft. Its ultimate link to *h₂weh₁- depends on node #15, which is disputed.\",\n \"air انگلیسی از انگلیسی میانه aire، از فرانسوی کهن air، از لاتین āēr و آن از یونانی ἀήρ است؛ نمودار میانجی‌های لاتین و فرانسوی را انداخته، ولی زنجیره بی‌گمان درست است. پیوند نهایی آن با ریشهٔ «وزیدن» به گرهٔ ۱۵ بستگی دارد که مورد تردید است.\",\n [W+\"air\"],\n [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference cited for this node.\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. air (l.2051)\",\"stance\":\"supports\",\"note\":\"'air, n., atmosphere. - ME. aire, fr. OF. (= F.) air, fr. L. aer ... which derives fr. Gk. ἀήρ'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wer-2\",\"stance\":\"partial\",\"note\":\"'Greek aēr (> Latin aer ...), air: ... AIR' - same Greek > Latin > English chain, root assigned to wer-2.\"}]\n)\nN(17,\"Latin\",\"mal-aria\",\"plausible\",\n \"'mal-aria' is not a Latin word: malaria is Italian mal'aria, a contraction of mala aria 'bad air', from mala (Latin malus 'bad') + aria 'air', which comes from Latin āēr through the Greek accusative ἀέρα / Latin āera > Vulgar Latin *aria. The meaning 'bad (sick) air' is correct and the Latin ancestry of both elements is correct, but the form belongs to the Italian box (#18), so the node is mislabelled rather than wrong in substance.\",\n \"«mal-aria» واژه‌ای لاتین نیست؛ «مالاریا» ایتالیایی mal'aria، کوتاه‌شدهٔ mala aria «هوای بد» است، از mala (لاتین malus «بد») + aria «هوا» که از لاتین āēr (حالت مفعولی āera) و لاتین عامیانهٔ *aria آمده است. معنا و تبار لاتین هر دو جزء درست است، ولی برچسب «لاتین» نادرست است؛ با احتیاط پذیرفتنی.\",\n [W+\"malaria\"],\n [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference cited for this node.\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. malaria (l.22639-22641)\",\"stance\":\"partial\",\"note\":\"'Lit. bad air, fr. It. mal' aria, contraction of mala aria, bad air, fr. mala, fem. of malo (fr. L. malus), bad, and aria, air' - Italian, not Latin.\"},\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. air (l.2051-2052)\",\"stance\":\"supports\",\"note\":\"'from the Att. acc. ἀέρα is borrowed It. aria, air'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wer-2\",\"stance\":\"partial\",\"note\":\"'Greek aēr (> Latin aer > Italian aria), air: ... ARIA, MALARIA'.\"}]\n)\nN(18,\"Italian\",\"\",\"confirmed\",\n \"Pass-through node: Italian malaria (mal'aria 'bad air'), used for the marsh fevers of the Roman Campagna and popularized as a medical term by Francesco Torti (1712); the Italian word is the source of the English and French terms.\",\n \"گرهٔ میانجی: ایتالیایی malaria (mal'aria «هوای بد»)، نام تب‌های مرداب‌های پیرامون رم که فرانچسکو تورتی (۱۷۱۲) آن را اصطلاح پزشکی کرد؛ سرچشمهٔ واژهٔ انگلیسی و فرانسوی همین است. ادعای نورایی درست است.\",\n [W+\"malaria\"],\n [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference cited for this node.\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. malaria\",\"stance\":\"supports\",\"note\":\"'The term malaria was prob. used first by the Italian physician Francisco Torti (1658-1741)'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wer-2\",\"stance\":\"supports\",\"note\":\"'Italian aria ... MALARIA'.\"}]\n)\nN(19,\"French\",\"\",\"confirmed\",\n \"Pass-through node: French malaria (19th c.), borrowed from Italian; Dehkhoda labels the Persian word 'فرانسوی', which supports French as the immediate source for Persian.\",\n \"گرهٔ میانجی: فرانسوی malaria (سدهٔ نوزدهم) از ایتالیایی وام گرفته شده؛ دهخدا «مالاریا» را «فرانسوی» دانسته که فرانسه را میانجی فارسی نشان می‌دهد. ادعای نورایی درست است.\",\n [W+\"malaria\",\"https://abadis.ir/fatofa/مالاریا/\"],\n [{\"ref\":\"MON:3709\",\"status\":\"partial\",\"note\":\"Print page not mappable online; Mo'in's online entry (vajehyab, archived) gives only the definition 'تب نوبه؛ بیماری گرمسیری ...' without an origin tag; Dehkhoda on abadis: 'مالاریا. ( فرانسوی ، اِ ) تب لرز'.\"}],\n [{\"src\":\"MON\",\"where\":\"vajehyab moein/مالاریا; abadis (Dehkhoda)\",\"stance\":\"supports\",\"note\":\"Dehkhoda: '( فرانسوی ، اِ )'.\"},\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. malaria\",\"stance\":\"supports\",\"note\":\"Italian source of the European word.\"}]\n)\nN(20,\"Persian\",\"mâlârîyâ\",\"confirmed\",\n \"Persian مالاریا mālāriyā 'malaria' is a 20th-c. loan from French malaria (Dehkhoda 'فرانسوی'), the pronunciation -iyā matching French/Italian -ia; native terms are تب نوبه, تب لرز.\",\n \"«مالاریا» در سدهٔ بیستم از فرانسوی malaria وام گرفته شده (دهخدا: «فرانسوی») و برابرهای فارسی آن «تب نوبه» و «تب لرز» است. ادعای نورایی درست است.\",\n [\"https://vajehyab.com/moein/مالاریا\",\"https://abadis.ir/fatofa/مالاریا/\"],\n [{\"ref\":\"MON:3709\",\"status\":\"partial\",\"note\":\"Mo'in online entry: 'مالاریا (اِ.) تب نوبه؛ بیماری گرمسیری که بر اثر گزش پشهٔ آنوفل ...' - word attested, no origin tag online; page not mappable.\"}],\n [{\"src\":\"MON\",\"where\":\"abadis.ir/fatofa/مالاریا (Dehkhoda)\",\"stance\":\"supports\",\"note\":\"'مالاریا. ( فرانسوی ، اِ ) تب لرز. تب لرزه. نوبه'; also 'کلمه مالاریا یک کلمه ایتالیایی و به معنای هوای بد (Mal-Aria) است'.\"},\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. malaria\",\"stance\":\"supports\",\"note\":\"'fr. It. mal' aria'.\"}]\n)\nN(21,\"English\",\"malaria\",\"confirmed\",\n \"English malaria (mid-18th c.; Wiktionary credits its introduction to John MacCulloch) is borrowed from Italian mal'aria 'bad air', the miasma once blamed for the fever; it displaced the native ague.\",\n \"malaria انگلیسی (میانهٔ سدهٔ هجدهم) از ایتالیایی mal'aria «هوای بد» وام گرفته شده، یعنی بخار مرداب که پیشینیان آن را علت تب می‌پنداشتند. ادعای نورایی درست است.\",\n [W+\"malaria\"],\n [{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 s.v. wer-2: 'Greek aēr (> Latin aer > Italian aria), air: ... MALARIA' - Italian route confirmed; root given as wer-2, not wē-.\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. malaria (l.22639)\",\"stance\":\"supports\",\"note\":\"'Lit. bad air, fr. It. mal' aria'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 index (l.1803)\",\"stance\":\"partial\",\"note\":\"'MALARIA wer-2'.\"}]\n)\n\nentry={\"entry\":2,\"root\":\"Wě 1, Aŭe 1\",\"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *h₂weh₁- 'to blow (of wind)' (Pokorny 81-84 10. au̯(e)-, u̯ē-; AHD wē-)\",\n \"note\":\"Root, label and gloss are correct: Pokorny pp. 81-84 (10. au̯(e)-, au̯e(o)-, u̯ē- 'to blow'), Walde-Pokorny I 220 ff., Watkins/AHD wē- and Wiktionary *h₂weh₁- all agree, and the Iranian (vāta-, vāiti, bād), Sanskrit (vāti, nirvāṇa), Germanic (wind, weather, wing, window) and Latin (ventus) branches are standard. Problems in the chart: (1) Avestan 'vât-âs' and 'antara-vâyu' are not attested Avestan - the first is the NP compound bād-ās projected back, the second Mo'in's reconstruction (BQT p.170 fn.); (2) English 'fan' comes from Latin vannus, not ventus; (3) Greek ἀήρ (air, malaria) is no longer derived from this root: Pokorny 1959 excludes it, AHD puts it under *wer-2, Beekes derives it from *h₂ews- 'dawn'; (4) Greek ἀτμός is only traditionally assigned here (AHD under the related *wet-1); (5) 'mal-aria' is Italian, not Latin. Nourai's Avestan/Persian side follows Mo'in's footnotes in Borhan-e Qate' (pp.170, 205). No extraction errors noticed (JSON matches the chart text).\",\n \"note_fa\":\"ریشهٔ هندواروپایی آغازین *h₂weh₁- «وزیدن (باد)» و معنای آن درست است (پوکورنی ۸۱-۸۴، والده-پوکورنی ۱: ۲۲۰، واتکینز، ویکی‌واژه) و شاخه‌های ایرانی (vāta-، vāiti، «باد»)، سنسکریت (vāti، nirvāṇa)، ژرمنی (wind، weather، wing، window) و لاتین (ventus) پذیرفته‌اند. اما در نمودار چند لغزش هست: «vât-âs» و «antara-vâyu» در اوستا گواهی ندارند (اولی همان «بادآس» فارسی است و دومی بازسازی معین در حاشیهٔ برهان)؛ fan انگلیسی از لاتین vannus است نه ventus؛ یونانی ἀήρ (و از این رو air و malaria) را پژوهش امروزی از این ریشه نمی‌داند؛ ἀτμός تنها به‌طور سنتی به این ریشه بسته می‌شود؛ و «mal-aria» ایتالیایی است نه لاتین. ادعای نورایی دربارهٔ خود ریشه درست است.\",\n \"sources\":[PIE,W+\"wind\",W+\"ventus\",W+\"باد\"],\n \"ref_check\":[{\"ref\":\"POK:81\",\"status\":\"supports\",\"note\":\"Pokorny pp. 81-84 (POK_full.txt l.7848, 'Page(s): 81-84'): 'Root / lemma: au(e)-10, aue(o)-, ue- ; Meaning: to blow ; participle ue-nt-'.\"}],\n \"consulted\":[WLDc,AHDc,\n  {\"src\":\"IEC\",\"where\":\"s.v. ueios 'wind, air' (IEC.txt l.19909)\",\"stance\":\"supports\",\"note\":\"'ueios ... wind, air, draught. WP I, 220. Cf. ueio (uemi) Skt. vāyúḥ ... Av. vayuš ... Li. vėjas'.\"},\n  {\"src\":\"SYN\",\"where\":\"1.72 WIND\",\"stance\":\"supports\",\"note\":\"'Most of the words for wind belong to an inherited group ... From IE *wē- blow in Skt. vā-, Grk. ἄημι ... Walde-P. 1.220 ff.'.\"},\n  KLNwind],\n \"nodes\":nodes}\nout={\"pdf_page\":526,\"book_page\":496,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":[entry]}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-526.json\",\"w\"),ensure_ascii=False,indent=1)\nPYEOF\ncd /home/sfmqrb/git/rishe-private && python3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-526.py && python3 -m json.tool data/verification/page-526.json > /dev/null && echo OK && python3 tools/verify_check.py 526"
}
```


### [2026-10-16T05:25:11.709Z] TOOL RESULT

```
OK
nodes verified: 21/21
node verdicts: {'disputed': 2, 'plausible': 5, 'confirmed': 14}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'partial': 6, 'not_checked': 8, 'contradicts': 1}
books consulted: {'supports': 44, 'partial': 10, 'contradicts': 4} | by book: {'KLN': 18, 'AHD': 11, 'POK': 7, 'MON': 6, 'WLD': 4, 'SYN': 3, 'BRT': 2, 'NYB': 2, 'ARY': 2, 'HRN': 1, 'PHD': 1, 'IEC': 1}
```


## [2026-10-16T05:25:17.322Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-526.py; sed -i 's/ἀήر/ἀήρ/g; s/Part II p.? s.v. andar-vāi/Part II s.v. andar-vāi/; s/(l.1125 block)/(AHD_watkins1985.txt l.1144)/' $F && python3 $F && grep -c 'ἀήر\\|p\\.?' data/verification/page-526.json; python3 tools/verify_check.py 526 | grep -c PROBLEM"
}
```


### [2026-10-16T05:25:17.876Z] TOOL RESULT

```
0
0
```


## [2026-10-16T05:25:26.970Z] TOOL CALL #72: SubagentHandback

```json
{
 "message": "I wrote the verification file for PDF page 526 (book page 496): /home/sfmqrb/git/rishe-private/data/verification/page-526.json. `verify_check.py 526` reports 21/21 nodes and 0 PROBLEM lines.\n\nThe page has one real entry, entry 2: the root \"Wě 1, Aŭe 1\", PIE *h₂weh₁- \"to blow\". The three redirect entries (Waq, Wâs, We 2) were skipped.\n\n- **Root:** confirmed. Pokorny pp. 81–84, Walde-Pokorny I 220, Watkins/AHD wē- and Wiktionary all agree.\n- **Nodes:** 14 confirmed, 5 plausible, 2 disputed, 0 transcription_suspect, 0 unverified.\n\n**Disputed:**\n- **#1 Avestan \"vât-âs; antara-vâyu\":** vāta- and vāiti are real (Bartholomae col. 1408). Neither of the other two forms is attested in Avestan:\n  - \"vât-âs\" is the New Persian compound bād-ās projected back into Avestan.\n  - \"antara-vâyu\" is Mo'in's own reconstruction in his footnote on Borhan-e Qate' p. 170 (\"اندروای ناگزیر از واژهٔ مرکب antara vâyu آمده است\"). Nyberg instead derives Middle Persian andarvāy from *andar-vāz.\n- **#15 Greek \"aěr\" (ἀήρ):** modern sources no longer put it under this root. Pokorny 1959 explicitly excludes it, AHD files it under *wer-2, Klein calls it of uncertain origin, and Beekes derives it from *h₂ews- \"dawn\". Only the older Walde-Pokorny and Buck include it here. This also weakens the root link for \"air\" and \"malaria\".\n\n**Plausible:**\n- **#2 andarvâ:** the analysis of its second element is debated.\n- **#4 Persian nirvânâ:** how it reached Persian is undocumented.\n- **#9 fan:** it comes from Latin vannus, not ventus.\n- **#10 atmos:** assigned to this root only by tradition.\n- **#17 \"mal-aria\":** labelled Latin, but the word is Italian.\n\n**Extraction errors:** none. The JSON matches the chart text. The book's \"nir-vanah\" copies Klein's form \"nirvanah\" rather than being a scan misread.\n\n**Other notes:**\n- I checked Borhan-e Qate' pp. 170 and 205 against the archive.org scans (leaves n388 and n425). Transcriptions and images are saved under data/verification/sources/refs/ocr/BQT/ as 170.vision.txt, 170.jpg, 205.vision.txt and 205.jpg.\n- Klein p. 1745 (the \"wind\" entry) is past the end of the local 1966 text, so I checked that entry in the 1971 edition instead.\n- The Etymonline fetches failed, so none of those pages are cited."
}
```


### [2026-10-16T05:25:27.297Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
