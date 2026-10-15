# Verification process log — verify-page-503


## [2026-10-15T02:44:16.201Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 503 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-503.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-503.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-503.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 503` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.241Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.468Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.590Z] TOOL RESULT

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


## [2026-10-15T02:44:21.722Z] TOOL CALL #2: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-503.txt; cat /home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md | head -80; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ | head -100"
}
```


### [2026-10-15T02:44:22.354Z] TOOL RESULT

```
=== PDF page 503 (book page 473) ===
--- entry 0 ---
ROOT Tengh -> redirect to Ten 1
--- entry 1 ---
ROOT [Indo-European] Tenk : to become firm and thick  (refs POK:1068)
#1 (parent #0) [Avestan] refs=POK:1068; KLN:1617; MON5:405; BQT:511 | tanj-išta : most pulled together, strongest ☞Isto ; taxma : pulled together, strong ; taxma-tanu : (with) strong body ☞Ten 1 ; taxma-urupa : (with) strong dogs ☞Wel 2 ; raodha-taxma : grown strong ☞Leudh
  #2 (parent #1) [Persian] refs=BQT:491,519,538; POK:1068 | tang «تَنگ» : tight ; tanjîdan «تَنجیدن ( تَرَنجید )» : to squeeze, pull ; tahamtan «تهمتن» : "with strong body" ; Tahmŭras «تهمورث» : "with strong dogs" ; Rostam «رُستم» : "grown strong"
#3 (parent #0) [Germanic] refs=AHD | thinhatz : tight ; thangul : thick mass
  #4 (parent #3) [English] refs=None | tight, thick, tangle
--- entry 2 ---
ROOT Tenu -> redirect to Ten 1
--- entry 3 ---
ROOT [Indo-European] Tep : to be warm  (refs POK:1069)
#1 (parent #0) [Avestan] refs=POK:1069; KLN:1589 | tap 2, tab : warm
  #2 (parent #1) [Persian] refs=BQT; HRN; FFD:46 | tab «تب ( تاب ، تابه )» : fever ; tâbîdan «تابیدن ۲ ( تابش ، تابان )» : shine ; tapîdan «تپیدن ( تپش )» : beat | extra: تافتن ۲ ، تفتن ، تفسیدن ، تفت
#3 (parent #0) [Avestan] refs=BQT:49,453,1252,1958 | tab-stana : place (time) of heat, summer ☞Stâ ; ap-tab : heat emitting glitter, sun ☞Ab 1 ; mâh-tab : moonshine ☞Me ; para-tab : shine forward, light ray ☞Per 1 ; aiwiš-tap : in heat, in hurry ☞Ambhi
  #4 (parent #3) [Persian] refs=BQT; HRN | tâbestân «تابستان» : summer ; âftâb «آفتاب» : sun ; mahtâb «مهتاب» : moonshine ; parto «پرتو» : light rays ; šetâftan «شتافتن ( شتاب )» : to hurry
#5 (parent #0) [Sogdian] refs=SOD:11 | âtp`k : heat
#6 (parent #0) [Latin] refs=KLN:1589 | tepěre : to be warm
  #7 (parent #6) [English] refs=None | tepid
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
```


## [2026-10-15T02:44:24.927Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 80,200p data/verification/sources/SOURCE_MATRIX.md; ls data/verification/page-49*.json data/verification/page-50*.json 2>/dev/null; cat tools/verify_check.py | head -150"
}
```


## [2026-10-15T02:44:26.234Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json\nfor k in ['POK','KLN','BQT','MON5','MON','HRN','FFD','SOD','AHD','WLD','ARY']:\n  d=json.load(open('data/verification/sources/refs_online.json')).get(k); print(k, json.dumps(d,ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-10-15T02:44:26.603Z] TOOL RESULT

```
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


### [2026-10-15T02:44:26.706Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 34

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON5 null

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verifi

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-10-15T02:44:29.387Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'));e=d['entries'][1] if len(d['entries'])>1 else d['entries'][0]\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'}));print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3500])\"; python3 -c \"\nimport json;print(json.dumps(json.load(open('data/verification/sources/refs_online.json'))['POK']['page_offset']))\""
}
```


### [2026-10-15T02:44:29.835Z] TOOL RESULT

```
{"pdf_page": 499, "book_page": 469, "verified_by": "claude-opus-5", "verified_on": "2026-10-14"}
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
   "note": "Mann: 'tl- (1) ... lift, raise, bear, suffer'. WP I, 701 & 738-9' with Tocharian, Greek tlēmi, Latin tuli, Gothic þulan — Sanskrit tulā is not quoted under this head."
  }
 ]
}
"POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
```


## [2026-10-15T02:44:31.518Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Root /lemma: tenk\\|Root /lemma: tep\" POK_full.txt"
}
```


### [2026-10-15T02:44:31.916Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:44:33.580Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^Root\\|lemma\" POK_full.txt | grep -i \"tenk\\|tep-\\|tep\\b\" | head; grep -n \"1068\\|1069\" POK_full.txt | head"
}
```


### [2026-10-15T02:44:34.045Z] TOOL RESULT

```
81374:Root / lemma: steb(hj- and steb(h)-. stdo"^-, nasalized stemb(h)-, step- {a\so step-?), 
85569:Root / lemma: tenk-1 
85591:Root / lemma: tenk-2 
85826:Root / lemma: tep- 
28890:be vacant, be without, not to contain ' (besides voco, -are EM^ 1069); Umbrian vagetum, 
85785:Page(s): 1068-1069 
85865:Page(s): 1069-1070
```


## [2026-10-15T02:44:35.339Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 85569,85870p POK_full.txt"
}
```


### [2026-10-15T02:44:35.672Z] TOOL RESULT

```
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
```


## [2026-10-15T02:44:40.413Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^tenk\\|^tep-\\|^tegu\\|tenk-\" AHD_watkins1985.txt | head; "
}
```


### [2026-10-15T02:44:40.748Z] TOOL RESULT

```
1072:tegu-. Thick. Germanic *thiku- in Old English thicce, thick: THICK. [Pok. tegu- 1057.]
1080:warp threads are stretched on the loom): TAFFETA; b. Iranian *tap-, “carpet,” in Greek tapés, carpet: TAPES- TRY. [Pok. temp- 1064.] ten-. To stretch. I. Derivatives with the basic meaning. 1. Suffixed form “ten-do- in: a. Latin tendere, to stretch, extend: TEND!, TENDER?, TENDON, TENSE!, TENT!; AT- TEND, CONTEND, DETENT, DISTEND, EXTEND, INTEND, OSTENSIBLE, PRETEND, SUBTEND; b. Latin portendere, “to stretch out before” (por-, variant of pro-, before; see per’), a technical term in augury, “to indicate, presage, foretell”: PORTEND. 2. Suffixed form *ten-yo- in Greek teinein, to stretch: TENESMUS; BRONCHIECTASIS, EPITA- SIS, HYPOTENUSE, PERITONEUM, PROTASIS, TELANGIEC- TASIA. 3. Suffixed zero-grade form *tn-nu- in Sanskrit tandéti, he stretches or weaves, with suffixed (instrumen- tal) derivative *ten-tro- in tantam, loom: TANTRA. 4. Suf- fixed form *ten-tro- in Persian ¢tdr, string: SITAR. 5. Basic form (with stative suffix) *ten-é- in Latin ten��re, to hold, keep, maintain (< “to cause to endure or con- tinue, hold on to”): TENABLE, TENACIOUS, TENACULUM, TENANT, TENEMENT, TENET, TENON, TENOR, TENURE, TENUTO; ABSTAIN, CONTAIN, CONTINUE, DETAIN, ENTER- TAIN, LIEUTENANT, MAINTAIN, OBTAIN, PERTAIN, PERTI- NACIOUS, RETAIN, (RETINACULUM), SUSTAIN. II. Derivatives meaning ‘‘stretched,” hence “thin.” 1. Suffixed zero-grade form *tn-u- in Germanic *thunw-, whence *thunniz in Old English thynne, thin: THIN. 2. Suffixed full-grade form *ten-u- in Latin tenuis, thin, rare, fine: TENUOUS; ATTENUATE, EXTENUATE. 3. Suf- fixed full-grade form *ten-ero- in Latin tener, tender, delicate: TENDER!, TENDRIL. III. Derivatives meaning “something stretched or capable of being stretched, a string.” 1. Suffixed form *ten-dn- in Greek tenén, ten- don: TENO-. 2. Suffixed o-grade form *ton-o- in Greek tonos, string, hence sound, pitch: TONE; TONOPLAST. 3. Suffixed zero-grade form *tn-ya- in Greek tainia, band, ribbon: TAENIA; POLYTENE. [Pok. 1. ten- 1065.] teng-. To soak. 1. Latin tingere, to moisten, soak, dye: TAINT, TINCT, TINGE, TINT; INTINCTION, STAIN. 2. Zero-grade form *tng- in Germanic *thunk- in Old High German thunk6n, dunk6n, to soak: punk. [Pok. 1. teng- 1067.] tenk-'. To stretch. Extension of ten-. Perhaps Germanic *thingam in: a. Old English thing, assembly, (legal) case, thing: THING; b. Old Norse thing, assembly: HUSTINGS; c. Old High German thing, ding (> German Ding), thing: DINGUS. [Pok. 1. tenk- 1067.] tenk-2, To become firm, curdle, thicken. 1. Suffixed form *tenk-to-, thickened, in Germanic *thinhtaz in Old Norse théttr, dense, watertight, akin to the Scandinavian source of Middle English thight, dense: TIGHT. 2. Possibly suffixed o-grade form *tonk-lo- in Germanic *thangul- in Old Norse théngull, seaweed (? < “thick mass”), akin to the source of TANGLE?. [Pok. 2. tenk- 1068.] tens-. To stretch, draw. Extension of ten-. Suffixed zero-grade form *tns-ero- in Sanskrit tasaram, shuttle: TussAH. [Pok. tens- 1068.] tep-. To be warm. Suffixed (stative) form *tep-é- in Latin tepére, to be warm: TEPID. [Pok. tep- 1069.] ter-. Base of derivatives meaning peg, post, boundary marker, goal. 1. Suffixed form *ter-men-, boundary marker, in Latin terminus, boundary, limit: TERM, TER- MINATE, TERMINUS; DETERMINE, EXTERMINATE. 2. Suf- fixed zero-grade form *tr-m- in Germanic *thrum- in Old English thrum, broken-off end (attested only in tungeth- rum, the ligament of the tongue): THRUM2. [Pok. 4. ter- 1074.] tera-1, To rub, turn; with some derivatives referring to twisting, boring, drilling, and piercing; and others refer- ring to the rubbing of cereal grain to remove the husks, and thence to the process of threshing either by the trampling of oxen or by flailing with flails. Variant *tré-, contracted from “*trea-. I. Full-grade form *ter@)-. 1. a. Latin terere (past participle tritus), to rub away,
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
2336:TaaL del-2 TABES ta- TACET tak-1 TACHE dek-? TACHISM deik- TACHYLYTE leu-! TACHYPNEA pneu- TACIT tak-1 Tack! dek-2 TACT tag- TACTICS tag- TACTORECEPTOR tag- TAEL tele- TAENIA ten- TAFFETA temp- TAG! dek-2 TAHSILDAR dher-2 TAIL! dek-2 TAINT teng- Tad (s)teg- TAKE tak-2 TALE del-2 TALENT tela- TALES to- TALION tele- TALISMAN kWel-1 TALK del-2 TALLOW del-4 TAME deme-2 TAMPON tap- TANDEM to- TANG! denk- TANGENT tag- TANGIBLE tag- TANGLE? tenk-2 TANGORECEPTOR tag- TANSY dhwene- TANTALIZE tele- TANTALUS tele- TANTAMOUNT to- TANTRA ten- Tap! tap-
2380:THING §tenk-1 THINK tong-
2389:THYME dheu-! -THYMIA dheu-1 THYROID dhwer- TICK? deigh- TICK3 dhé-1 TICKET steig- TIDE! da- TIDE2 da- TIDINGS da- TIE deuk- TIERCE trei- TIFFANY bha-1 TIGER steig- TIGHT tenk-2 TILE (s)teg- TILLER? teks- TILLERS del-3 TILT? del-3 TIMBER deme-1 TIME da- TIMOCRACY kWeig-1 TINCT teng- TINGE teng- TINSEL skeei- TINT teng-
```


## [2026-10-15T02:45:02.176Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^\\*tap\\|^\\*tanč\\|^\\*tanc\\|tanj\\|šitāf\\|sitaf\\|šetāf\\|tapīdan\\|tapidan\" CHEUNG.txt | head -30"
}
```


### [2026-10-15T02:45:02.598Z] TOOL RESULT

```
3298:*tap ‘to seize, attach, stick, strike’ 
23719:*NWIR: NP sitaftan/sitab- ‘to hurry’ 
24631:*NWIR: NP tanjidan/tanj- ‘to squeeze; to twist, roll together; to draw tight; to be 
24669:*tap ‘to warm up, heat’ 
24686:*tap 379 
24728:result of wound, pox, etc.)’ || (+ *us-) Sh. (Baj.) sitafc-/situvd, Bart. sitafs-/situvd ‘to 
25332:*tap ‘to twist, wind’ 
41589:tanjidan/tanj-, 378 
48293:sitafc-/sitüvd, 379 
48426:sitafs-/sitüvd, 379 
55127:*tap (s.v.), *zarH' (s.v.) 
56143:*tanc
```


## [2026-10-15T02:45:04.151Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23700,23730p CHEUNG.txt; echo ----; sed -n 24600,24760p CHEUNG.txt"
}
```


### [2026-10-15T02:45:04.541Z] TOOL RESULT

```
*IE COGNATES: Lith. sterübti, stémbti ‘to oppose’, Gr. &oteugng ‘unshakable’, Toch. 
A stäm-, B stäm- ‘to stand’, A sänm- (caus.) ‘to attach, bind? 

*REFERENCES: EVP: 70; DKS: 434b; K.T. Schmidt 1992: 106 ff.; Werba 1997: 383; NEVP: 11 


*stap ‘to hasten, (op)press’ 

*MIDDLE PERSIAN: (+ *abi-) MMP ’wyst’b-, BMP ’wst’p- /awistab-/ ‘to (op)press; 
hasten [tr.]’, MMP ’wyst’bysn ‘oppression’ || (+ *ni-) MMP “nyst’pt (ppp.) ‘fallen 
headlong, away’ {hapax} > DMMPP: 76b, 254b 

Pres.: IND. 3sg. MMP ’wyst’byd: Partic.: perf. pass. MMP ’wst’ft, ’wyst’pt, "wystptg; Pass.: pres. IND. 
3sg. MMP ’wst’byhyd 

*PARTHIAN: (+ *abi-) ’wyst’bysn ‘oppression’ || (+ *ni-) “nst’ft (ppp.) ‘fallen 
headlong, away’ {hapax} = Ghilain: 72 | DMMPP: 76b, 254b 

*NWIR: NP sitaftan/sitab- ‘to hurry’ 

*MISC: Arm. (LW) stapem ‘I oppress’, štap ‘haste, trouble’ 

© The root may be a "variant" of *stambH (?). The Armenian borrowings Stapem and 
Stap rather favour original *-p-. No doubt, *stap is influenced by *stambH. 

«PIE *step- ‘to press, step’ = LIV: — | Pok.: 1013 

*IE COGNATES: OCS stopiti ‘to tread’, OCS stopa ‘foot-step’, OFr. steppa, stapa, OE 


----

*SANSKRIT: tan ‘to stretch, to extend’ (RV+) = EWAia I: 618 

«PIE *ten- ‘to draw, stretch’ = LIV: 626 f. | Pok.: 1065 f. 

ТЕ COGNATES: Gr. teivo ‘I draw, pull tight’, OHG den(n)en ‘to stretch’, МНС 


dehnen ‘to stretch’, etc. 

*REFERENCES: Horn 1893: 89; IIFL II: 545b, 262a; Edel’man 1971: 263; MacKenzie, Pahlavi: 81; EVS: 
80b; WIM I: 73; WIM ПЛ!. 84; Abaev, Slovar’ III: 301 ff; Werba 1997: 348; Cabolov 1997: 73; 
Steblin-Kamenskij 1999: 367 f., 457 


*tanó ‘to twist (together), become narrow, dense, constrict’ 
*MIDDLE PERSIAN: MMP tnz- ‘to strain, press’, BMP tng /tang/ ‘narrow’ 


c DMMPP: 325b 
Partic.: pres. MMP tnz’g’n (pl.) 


378 *tand 


*PARTHIAN: tncysn ‘prohibition’, tng ‘1. suffering, distress; 2. narrow; distressing’ 
c DMMPP: 324b f. 

*KHOTANESE: (+ *ш-) byamjsa-, bätamjsa- ‘astringent’ 

*NWIR: NP tanjidan/tanj- ‘to squeeze; to twist, roll together; to draw tight; to be 
distressed, sad’, Bal. tancit/tanc- ‘to fasten strongly, roll strongly, squeeze’, ? tajén- 
‘to stretch’, NP tang, Bal. tank ‘narrow’ 

*NEIR: Wa. tanz-/tanzd-, tanz-/tanzd- ‘to fortify the warp [of textiles]; to draw a web 
[of spiders]’, Sh. taZ-/tiZd, Sariq. toZ-/tiZd ‘to pull, draw, haul, drag, stretch’, Pash. 
tat ‘close, thick’, ? Sh. (Baj.) taxc-/tixt, Rosh. taxs-/taxst ‘to puff, smoke’. Ф Wa. 
tanz-/tanzd-, tanz-/tanzd- are unconnected with YAv. 0anj- ‘to pull, draw’, etc. 
(ant), 

*SANSKRIT: ѓайс ‘to pull together, coagulate, solidify’ (YV+) = EWAia I: 614 

*PIE *tenk- (*temk- ?) ‘to twist together, pull oneself together, condense’ = LIV: 
625 | Pok.: 1068 

*IE COGNATES: Lith. tenkü (tekti) ‘I stretch, reach, attain’, Olrish -téici ‘solidifies, 
coagulates’, (ppp.) Olrish técht ‘solidified’, ON péttr ‘close, thick’, Lith. tánkus 
‘dense, thick; frequent’ 


*REFERENCES: Horn1893: 88 f.; Fraenkel II: 1077; EVS: 82a; DKS: 282a; Abaev, Slovar’ III: 285; Werba 
1997: 189 f.; Steblin-Kamenskij 1999: 354; Shahbakhsh: s.v. tané-; Korn 2005: 168 f., 365 


*tand ‘to languish, faint’ 

*PARTHIAN: tnd ‘faint, languishing’. 0 The Parthian form cannot be analysed as the 
past participle of *tamH, which would rather be *taHta- > *täta-. > DMMPP: 324b 
*SANSKRIT: fand ‘to become tired, paralysed’ = EWAia I: 623 

© The evidence for the corresponding Ir. root *tand of Skt. tand is confined to 
Parthian. 

«PIE *ten-d- ‘to tire’ = LIV: 627 f. | Pok.: (1066) 

*IE COGNATES: Lith. (dial.) tandus ‘lazy, sloppy’, Lat. tendo ‘I stretch’ 


*tap ‘to warm up, heat’ 

*AVESTAN: YAv. tap- “о be(come) hot’ || (+ *4-) ‘to warm’ || (+ *ham-) ‘to 
be(come) hot’ — Liste: 24 

Pres. inch.: INJ. 3sg. YAv. tafsat- (Y 9.11, rep.), SUBJ. 3pl. YAv. tafsan (V 3.32); Caus.: pres. IND. 3sg. 
YAv. täpaiieiti (Yt 6.1, Yt 7.4, Yt 17.20, etc.), ? YAv. "a.tapaiieiti (V 9.41); Partic.: perf. pass. YAv. 
ham.tapta- (V 4.46) 

*MIDDLE PERSIAN: MMP t’b- ‘to shine’ ?, BMP t’p- /tab-/ ‘to heat, burn (up); shine’. 
© No certain attestations in MMP, DMMPP: ibid. > DMMPP: 321a 

Pres.: IND. 3sg. BMP t’pyt /tabéd /, SUBJ. 35р. ? MMP t’b’d {rather Pth. 7}, OPT. 3sg. ? MMP ®t’byy, 
ІМРУ. 2sg. BMP t^p /tab/; Inf.: BMP t’ptn /taftan/; Partic.: perf. pass. BMP грі /tafi/; Pass.: pres. IND. 
35р. BMP t’pyhyt /tabihed/ 


*tap 379 


*PARTHIAN: t’b- ‘to shine, burn’ || (+ *abi-) *bd’b ‘sunshine’ || (+ *pati-) pt’b- ‘to 
burn into’ || (+ *ui-) wyt’b- ‘to shine’ (young formation) = Ghilain: 72 | DMMPP: 
321a f., 9, 360a 

Pres.: IND. 259. t’byh, 35р. t’byd, t'byd, 3р1. t'bynd, SUBJ. 3sg. t’b’h; Partic: perf. pass. П t^b'd, t’b’d || 
(+ *pati-) Pres.: IND. 3sg. pt'byd, IMPV. 2pl. pt’byd || (+ *ui-) Pres.: IND. 3sg. wyt'byd, SUBJ. 2sg. 
wyt’b’h; Partic.: perf. pass. II wyt’b’d 

*KHOTANESE: ttav- (ttau(s)-) ‘to be(come) hot’ || (+ *a) LKh. ауу- ‘to heat’ || (+ 
*nis-) nastau-/nistau-, (inch.) OKh. nastos- ‘to be consumed’ || (+ *pati-) 
pattav-/pattau- ‘to burn up; illuminate’ || (+ *ui-) LKh. byav- ‘to be hot’ || (+ *ham-) 
OKh. handau- ‘to become hot’, LKh. hamdev- (caus.) ‘to ripen’ = SGS: 38, 9, 67, 
50 £., 104, 140 f. 

*SOGDIAN: SSogd. t’p (denomin.) ‘to seal’ || (+ *a-) CSogd. "tpn ‘furnace’ || (+ 
*pati-) MSogd. ptp- ‘to burn’ (perhaps p- < *upa- ?) || (+ *ui-) BSogd. wyt’’p- ‘to 
shine, radiate’, CSogd. wyt’p ‘to shine forth’ || (+ ham-) BSogd. ’ntph ‘fever’ 

Pres.: ОРТ. 2sg. SSogd. t’py; Pass.: pret. intr. IND. 3sg. SSogd. tpty; Partic.: perf. pass. SSogd. tpt || (+ 
*pati-) Impf.: IND. 3sg. MSogd. ptyt’p; Partic.: perf. pass. ptßtyy ‘hot’ (BBB: 43); Pass.: perf. intr. IND. 
1р1. MSogd. ptBtyt "ym ‘we are burned’ || (+ *ui-) Pres.: IND. 35р. BSogd. wyt’’pt, BSogd. wyt’pt, 3pl. 
BSogd. wyt’p’nt, SUBJ. 3sg. BSogd. wyt’’p’t, Impf.: IND. 35р. CSogd. wyt’p 

*CHORESMIAN: t’BY- ‘to heat’, (denomin.) ‘to punctuate, put a diacritic; to hit the 
target’ || (+ *upa-) bdfs- ‘to become hot’ => Samadi: 203 f., 15 

*BACTRIAN: Taß- ‘to impress (a seal); to seal’ = S-W, Bact.: 225a 

*NWIR: NP taftan/tab- ‘to shine, burn’, NP tafsidan/tafs- (inch.) ‘to become hot’, Bal. 
tapt/tap- ‘to heat’, Gz. to(u)-/to(w)a ‘to shine, light up’, NP tab ‘fever’, tab ‘heat, 
burning; heated iron; affliction, pain, torment’, tabah, tavah ‘frying-pan; burnt brick, 
tile’, Kurd. taw ‘sun’ || (+ *abi-) NP айар ‘sun(shine)’ || (+ *ш-) Gur. (Kand.) yaw 
‘fever’ 

*NEIR: Oss. I. tæfsyn/tæfst, D. tefsun/tzfst (inch.) ‘to become hot’, I. tavyn/tavd, D. 
tavun/tavd (caus.) ‘to warm up’, also Oss. I. texsyn/taxst ‘to itch; to be feverishly 
ill’ (contaminated with inch. *daxsa- < *daj ?), Yzgh. tifs-/tüvd ‘to be (over)heated’, 
Oss. tæf ‘steam, spirit, scent’, I. taevd, D. taevde ‘heat, hot’, Pash. tod ‘hot’, Sh. tofc 
‘pox’, Ishk. tofë ‘burnt, scorched’, Sariq. tufë ‘faded away; stain’, Wa. tofc ‘scar (as 
result of wound, pox, etc.)’ || (+ *us-) Sh. (Baj.) sitafc-/situvd, Bart. sitafs-/situvd ‘to 
be fried’, Sh. (Baj.) sitäb-/sitäpt, Rosh. sitéb-/sitob-, Bart. sitöb-/sitöbt, Sariq. 
stob-/stipt (caus.) ‘to fry, stir (during roasting)’ || (+ *fra-) Sariq. radabon-/radabond 
‘to be roasted’ || (+ *ui-) Sh. widob, (Baj.) xür-widob, Sariq. wadub ‘the time after 
sunrise, early forenoon’ || (+ *ham-) Oss. I. andavyn/eendevd, D. aendavun/aendavd, 
M. dif-/dift- ‘to catch fire’ (or < *ham- + *diHp?), Wa. dsıp-/dopt ‘to warm (up), 
become warm’, Pash. döbay, (Wan.) doba ‘summer’, Yi. idou, Wa. andáv ‘fever’ 
*SANSKRIT: tap ‘to burn, be hot, to make hot; to hurt, torment’ (RV+) = EWAia I: 
623 


380 *taré (*tark) ? 


o CSogd. frtyp- ‘to shine’, cited by Gershevitch (GMS: $49, 8318) and 
Morgenstierne (GMS: l.c.), does not belong here: s.v. *diHp. 
*PIE *tep- ‘to be warm, hot’ = LIV: 629 f. | Pok.: 109 


*IE COGNATES: Lat. tepere ‘to be warm’, Olrish té ‘hot’, OCS teplosts (f.) ‘warmth’ 
*REFERENCES: Horn 1893: 83; EVP: 80; IIFL II: 205a; Abaev, Slovar' I: 153 f.; EVS: 80a, 76a, 87b, 66b; 
Nyberg II: 189a; Abaev, Slovar’ III: 249 f., 236 f., 246 f., 283, 285; DKS: 20a; WIM II/1: 84; Werba 
1997: 190; Steblin-Kamenskij 1999: 83, 158, 357; Korn 2005: 313, 363 


*taré (*tark) ? ‘to turn, to move to and fro ?’ 

*KHOTANESE: (+ *fra-) OKh. hatäljs- ‘to flutter’? = SGS: 145 

*NWIR: ? NP tarkand(ah) ‘ruse’ 

*SANSKRIT: ? tark ‘to turn, move to and fro’ (KS+) = EWAia I: 633
```


## [2026-10-15T02:45:07.618Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25332,25370p CHEUNG.txt; grep -n \"tapidan\\|tapīdan\\|tapid\" CHEUNG.txt | head"
}
```


### [2026-10-15T02:45:07.996Z] TOOL RESULT

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

*REFERENCES: Horn 1893: 83; EVP: 84; Andreev — PeSéereva: 337b; EVS: 80a; Abaev, Slovar’ III: 336 
f., 244; Steblin-Kamenskij 1999: 358 f.; Lecoq 2002: 638b, 684b 


*ti(n)f! ‘to sharpen’ 

*MIDDLE PERSIAN: MMP Dt, MMP tyz, tyz, ВМР tyc /téz/ ‘sharp? = DMMPP: 
332a, 333a 

*KHOTANESE: (+ *fra-) OKh. hatiys- ‘to shine’ = SGS: 145
```


## [2026-10-15T02:45:11.352Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"tahm\\|šitāft\\|sitaft\\|sitäft\\|partav\\|partau\\|äftäb\\|āftāb\\|aftab\\|tapīdan\\|tapidan\\|tanjid\\|tañg\\b\\|tang \\|tabistan\\|täbistän\\|tābistān\\|tāftan\\|taftan\" HRN.txt | head -40"
}
```


### [2026-10-15T02:45:11.731Z] TOOL RESULT

```
3486:tahan, tabistan 'Sommev\ (jNnozxn, Jer. 40, 10; niwNP,
6285:phlv. stahmak^ sfahmaklh bezw. sta/mak^ Rtaxtnakih
6761:phlv. östaftan ') (vd. 7 (27) GL, 18 (98), Meii.) eilen,
```


## [2026-10-15T02:45:13.515Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3470,3500p HRN.txt; echo ----; sed -n 6270,6295p HRN.txt; echo ---; sed -n 6750,6775p HRN.txt"
}
```


### [2026-10-15T02:45:13.963Z] TOOL RESULT

```
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
----
bei. istür (167); yidg. üstür.
716. setei*veH, suturven^ esterven 'unfruchtbar' (Schefer,
ehrest, persane II, 188 Zeile 2).
Gehört wohl zu ai. start- 'unfruchtbar ; arm. sferj
(II. No. 258); gr. otttga; lat. sterilis; got. sfairö
(Hörn, KZ. 32, 583 No. 12).
Die neuper?ische Volksetymologie 'Maulesel ähnlich*
ist unwahrscheinlich, zumal es ein Suffix -ve72 'ähnlich*
sonst gar nicht giebt. Oder ist jüd.-pers. H^mriDN
(Is. 54, I) die ursprüngliche Form?
'J Im Satzsandlii entstanden nach Bartholomae, Studien II, 42;
aber verf^l. nhd. stern,. sterben u. v. a. ni. (Hörn, KZ. 32, 588 No. 24).
-) Arm. LW. sioivar.
8J Syr. LAV. ^n^P.DX» <lc Lagnrdo, Oor. Abli. 13.— 159 —
717. ffitem 'unrecht, Gewalt'.
phlv. stahmak^ sfahmaklh bezw. sta/mak^ Rtaxtnakih
gewaltthätig, Gewaltthat'.
Also aus aw. '*8ta/ma-^ vergl. staxlra- (zu dem
Suffixwechsel vergl. oben unter No. 479). Vergl.
N. pr. Gustehm aus '^Vista/^na-,
718. Htetnbe') 'gewaltthätig, streitsüchtig, kampflustig
(Vfs und Kämtn, Seite 7»^ Vers 9), istembe ').
ap. "^stambaka-y vergl. ai. stambha- 'Aufgeblasenheit,
anspruchsvolles Wesen'; arm. LVV. sfambak {nvavrjoo^).
719. ftitTiden, sutä(fe7i 'loben, preisen*, Praes. sitäy-ew,
sifäyis,
---
(Geiger* s Etymologie *sa — Praeüx — und |/^pö*- ist
falsch).
777. Htäften 'eilen', Praes. sitäb-em^ sitab, DNDl^iN (Jer.
48, 16).
*J E. Drouin*s Lesung suhanum uut* Münzen (Kevuc niumiä-
matique, 1890, S. 361) ist ebenso verfehlt, wie seine Qemmenentzifferungeii
(vergl. ZDMG. 45, 429 folgg.).
') Vergl. oben No. 179 Anm. _
5) IV^u/^ijufQoy, H. 8. Jarret, Aln-i Akbari-Transl. Vol. II, 13
Anm. 2.
*) Ilübsohmann, ZDMG. 44, 5ß0.— 172 -
phlv. östaftan ') (vd. 7 (27) GL, 18 (98), Meii.) eilen,
arm. LW. staij, davon Denomin. stapim 'eilen.
aw. *aiwis + l^tap-, täpaj/eiti *iri Wärme, Hitze
bringen', dann tropisch-).
Zu aiwis vergl. oben np. hes- (No. 221).
778. sHden gehen; sein, werden', Praes. sev-em.
ap. \/^siya€', aslt/avam, asiyuva 'gehen, marschiren';
aw. {/sav-, suvaite'^) gehen'; ai. [/^cyav-, Ci/dvate 'fort-
gehen ; arm. cit 'Aufbruch', ciiem 'aufbrechen' (H.
No. 242).
kurd. eleu 'gehen', dicm; sify, soal 'werden, gehen';
oss. d. t. cäün 'gehen, schreiten, spazieren, fahren'
(319) ; bei. suta, siit, n. suöa, iud^a (322) ; wa;^. cduam,
si/n. oi\zafcam, sar. va]zevsam.
779. siirrän, serrün 'unablässig lliessend', slrän Kegen' (y),
```


## [2026-10-15T02:45:18.605Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"teng\\b\\|teng \\|tengiden\\|tenjiden\\|tenciden\\|tenjlden\\|tahm\\|rustem\\|rustam\\|tahmüra\\|tehmtcn\\|tehemten\\|pertev\\|perteu\\|tepiden\\|tejpiden\\|ap-täb\\|äftäb\\|aftäb\" HRN.txt | head -30"
}
```


### [2026-10-15T02:45:19.086Z] TOOL RESULT

```
407:aus G. zu nehmen ist: ^Dem Rustem gab zehn Ammen der Löwe (d. L
408:Zäl), dass jener edle Löwe (d. i. Rustemj satt wurde (Mohl's Über-^— XVI —
3696:394. tenjlden zusammenziehen ; trinken' (jüd.-pers., z. B.
3729:398. teng 'en^Q,
6285:phlv. stahmak^ sfahmaklh bezw. sta/mak^ Rtaxtnakih
11428:aftäb 3, 37, 372.
```


## [2026-10-15T02:45:21.147Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3690,3745p HRN.txt; grep -n \"^3\\. \\|^37\\. \" HRN.txt | head; grep -n \"^3\\. äb\\|^3\\. \\?ab\" HRN.txt"
}
```


### [2026-10-15T02:45:21.659Z] TOOL RESULT

```
fannaz ^).
aw. tanü' *Körper, Leib'; phlv. tan; ai. tanä^,
af/. tan; wa/. tan, si/n. tand.
Dazu tenha allein', phlv. tamhä (SpiegeTs Lesung
tanhäk, vd. 5 (134) 61., ist falsch. Hier wie vd. 6
(9) 61. — ZDM6. 43, 43 — ist tuhtk zu lesen).
394. tenjlden zusammenziehen ; trinken' (jüd.-pers., z. B.
Is. 63, 6), }T:Nj:n.
aw. i^danj' ziehen' u. s. w. (6 eidner, Drei Yasht,
95). ^ .
oss..t. tlinfin, d. iünjun 'ausdehnen' (249); bei. tajenag
'spannen, dehnen (375).
Der Übergang von der Bedeutung 'ziehen* zu 'trinken
findet sich auch bei np. ähenjiden und kestden.
Da magidüta kein Abstractum auf üiu («', d) sein kann, muss es für
magidäta stehen. Im Neubabyl. wiederholt -ü^w für -äti Endung des
Plurals fem. gen. Agidtu *ßinde* bezeugt (von "I^IX)« Davon könnte
magidtu eine Form MafUlatu sein. Ev. aber auch magidtu : agidlu
= JISi^niD • Ärahsamna, Taka- also höchst wahrscheinlich irgend eine
*Binde' als Kopfbedeckung. Nähme man mit Recht an, dass täj =
*Krone* elamitischen Ursprungs wäre, ebenso wie taka- in takabarä, so
stände der Verknüpfung beider Wörter, soweit wir dies beurteilen können,
nichts im Wege. Die beiden Wörter könnten zu verschiedenen Zeiten
und aus verschiedenen Dialccten entlehnt sein".
Ehe ich Jensen 's Erklärung kannte, hatte ich an siyn. tdki
'Pelzmütze' gedacht, ß e z o 1 d , Achaemenideninschriften 72, hält übrigens
magidüta für den xgwßvXog (Thycyd. I, 6).
*) Aus tan + näz^ de Lagarde, Ges. Abh., 51 Note 4.— 89 —
395. tund schnell, heftig, stark'.
aw. Hvant" (= Hnvant-), [/'tav-, vergl. tuvan (No. 401).
396. tunder, tundur ^Donner .
Vergl. ai. i/^tan-, tdnyati erschallen, laut tönen,
rauschen', tanayitnü- 'donnernd', tanyatii' 'Donner';
lat. tonare, tonitnis; ags. pnnjan, punor, nhd. Donner^
engl, thufider,
397. tenuk *düun, zart, fein'.
ai. tanu-, tdnuka- *dünn, fein\
kurd. tenik; oss. f(wäg (248); bei. tanak, n. fana/,
fanaU (377); sar. tanük,
398. teng 'en^Q,
aw. tahcista- (Superl. von ta/tna- 'kräftig'); phlv. tanf/
eng', tmigih 'Enge'; arm. fanjr 'dicht' (H. No. 110).
kurd. tenk *enge; bei. tank, n. tanJc, tahanH (378);
af/. tangat/l; wsi/, t^mg, sar. tong,
Vergl. auch Bartholomae, Studien II, 44, 51.
399. tenlden 'drehen, spinnen', tede 'Spinnengewebe*, tane
'Zettel, Aufzug (am Webstuhl)'.
aw. [/^tan-; phly, tatak, vd. 7 (36) (für aw. täfdaena-):
ai. |/"^aw-, tanoti, 'dehnen, spannen'.
400. tHj tu, tö (FirdüsT)^) 'du, vergl. -et 'dein', -tan 'euer'.
ap. iuvam 'du'; aw. tum, tväm, tu, tava; päz. tö {tu);
ai. tvdm, tdva; arm. du 'du' (H. No. 85).
kurd. ttr, af/. ta (obliqu. tä, di); oss. d. du, t. di
(112).
401. tuvan 'vermögend, mächtig', tuvanä, tuvanisten.
aw. i/^taV' 'können, vermögen', tavä[cä; phl. tuvän
464:3. ä& *Glanz , (Sahn. I S. 14 Vers 7), vergl. ab[rö, ah[tah,
752:37. äftäh *Sonne, ixDS'X (jüd.-pers.).
2608:37. bei ^Grabscheit* ^).
10021:3. äfräH 'Mitteilung, Belehrung (Men.).
10185:37. iiiväklh 'Hilfe, Beistand' (AV.), vergl. awäklnitan
21496:3. ^«ce 545.
21500:3. <Jö i)75.
```


## [2026-10-15T02:45:24.906Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 752,765p HRN.txt; grep -n \"pertev\\|pertew\\|partav\\|partau\\|parta\" HRN.txt HUB.txt | head"
}
```


### [2026-10-15T02:45:25.258Z] TOOL RESULT

```
37. äftäh *Sonne, ixDS'X (jüd.-pers.).
skr. "^ahha + tapa- (vergl. No. 3).
kurd. LW. a^taw (Houtum-Schindler), ätätv etc.
(Jaba-Justi).
38. äfdutn 'letzter', nur im Mujmil ettevärT;^ (ed. Mohl,
Journ. asiat. 1841, S. 178)^), vergl. hafdum zuletzt*^).
«) Hübschmann, ZDMG. 38, 431.
') Bartholomae, Arische Forsch ungren II, 102.
*) Dazu wohl auch äyisten, z. B. AM. 14 Zeile 16, 193 Zeile 11.
do Lagarde, Ges. Abh. 290 ist natürlich unmöglich.
*) Vergl. Spiegel, Grammatik der- Huzväresch-Sprache, 76.
^) Für bäfdum (d. i. be äfdum) haben die Wörterbücher folgende
Belegstellen: SF (S. 95 Vers 53), Metrum Remel:
kär-i dänä nek^ gerded bäf^dum
HUB.txt:1293:296. Np. partav 'Licht, Strahl* (auch afgh. LW.) mit auf-
HUB.txt:6673:neben kafiar *Taube' (H. 842). Ueber partav *Glanz, Strahl
HUB.txt:7415:LW. partam *reich*?
HUB.txt:10632:partav 38.
HRN.txt:909:INIX 'Verwüstung*, vergl. äpar^ apar(i)sn *Raub*, apartan^
HRN.txt:1573:phlv. avpartan bezw. öpärtan 'verschlingen' (Men., AV.).
HRN.txt:2082:apartar, apartum; ai. upäri.
HRN.txt:2880:296. pertew 'Glanz*.
HRN.txt:6217:aw. Sparta- Veiss*; phlv. spSt, arm. LW. spitak; ai.
HRN.txt:13312:pertew 296.
```


## [2026-10-15T02:45:27.340Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2878,2890p HRN.txt; sed -n 1290,1300p HUB.txt; sed -n 6670,6680p HUB.txt; grep -n \"tang\\b\\|tahm\\|tabistän\\|täbistän\\|tep\\b\" HUB.txt | head"
}
```


### [2026-10-15T02:45:27.681Z] TOOL RESULT

```
ap. "^para -\~ y/kan- (?). Der Bedeutungswechsel ist
allerdings sehr auffällig. Vergl. efgenden (No. 103).
296. pertew 'Glanz*.
para j- ^fap-^ vergl. np. fäßen (No. 372).
297. perdayten 'ausführen, ausleeren; streben, sich be-
mühen* ; Praes. ,perdazem.
phlv. parda/tan (AV.).
aw. *para + l^tac-; Bedeutungswechsel wie bei
end (Ixten (No. 117). Die np. Bedeutung 'ausleeren'
lässt sich aus 'weglaufen lassen' erklären.
von Stackeiberg (briefl. Mitteilung) vergleicht
oss. t. fäldä/jn 'wenden' (ZDMG. 41, 574 Anm. 3),
dessen Bedeutung sich mit der von V^tac- {-\- pard)
Wrzl. kan graben'. Es gab ja wohl auch noch andere
Wurzeln kan oder gan. Vgl. Nr. 41 : agandan VoU-
stopfen'.
296. Np. partav 'Licht, Strahl* (auch afgh. LW.) mit auf-
falligem t fiir d, Anlehnung an tab, taftan etc.?
297. Np. pardaxtan hat bei Vullers 12 Bedeutungen,
es ist schwer zu entscheiden, auf welche man die
Etymologie bauen soil. Die gewohnliche Bedeutung:
VoUenden, beendigen, sich mit etwas beschaftigen'
(vgl. afgh. LW. pardaxt performance, relinquishment,
*) paSira = phi. patirdh gehort zu zd. paiti + ar^ wovon pat-
Min. Gl. 22; firotan (aus firod-fan) 'humilis', paz. ertan- 189 -
*humble* Min. Gl. 72, die noch als Komp. mit tan (vgl. x"^stan
selbst', abistan *schwanger ) gefuhlt wurden ; kabutar 'Taube'
neben kafiar *Taube' (H. 842). Ueber partav *Glanz, Strahl
H. 296 s. oben p. 38. Die Etymologie von kutah kurz' (s.
oben p. 89) ist noch nicht gefunden. Aber die Frage bleibt
noch oflfen, wie die nach Vokalen im Persischen iiberhaupt
vorkommenden t (wie z. B. in kutah) zu erklaren sind, da
urspr. t nach Vokal der Kegel nach zu d werden musste.
§ 84. Ap. t wird nach Vokalen und tonenden Kon-
sonanten (r, n) im Np. zu d:
1655:398. Np. tang enge, bedrangt' geh5rt zu tanjldan zusammen-
1657:und taiij (Nr. 394) u. s. w. Vgl. tang u bandt obli-
1658:gation' JRAS. 1894, 452. — Dazu auch tang *Sattel-
1660:tang *Sattelgurt' (Dames p. 60) kurd. taiig 'Gurt',
1664:dumStbng *Schwaiizriemen*, afgh. ta-tang *Sattelgurt',
1665:tang ^Sattelgurt*.
2471:*) Zur Bedeatang vgl. Horn Nr. 676.
4658:*nayna' ? ? ; . Bistam aus Bistahm = Gustahm (N Q 1 d e k e ,
5562:tahm neben Gustahm = phi. Vistaxm Tab. 96; Bindoi =
5598:(Sebeos 30 u. s. w.) = np. Binddi und Bistahm, arab.
```


## [2026-10-15T02:45:30.075Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1650,1666p HUB.txt; sed -n 5555,5566p HUB.txt; grep -n -i \"rustahm\\|rotstahm\\|rödstahm\\|rostam\\|rustam\" HUB.txt NYB_vol2_glossary.txt PHD_mackenzie.txt | head"
}
```


### [2026-10-15T02:45:30.502Z] TOOL RESULT

```
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
naftafig *Mitte des Leibes' (beim Pferd, eigentl. *Nabel-
gurt') Socin, kurd. Samml. II, 294 (die Seiten 293—294— 49 —
kommen doppelt vor!), 339, osset. dxtong 'Bauchgurt*,
dumStbng *Schwaiizriemen*, afgh. ta-tang *Sattelgurt',
tang ^Sattelgurt*.
399. Dazu np. tanasta 'tela araneae', afgh. LW. tanista
v(i)skdfak Bdh. Gl. 263; bisgard *Jagd* aus phi. *viskart
(oben p. 30), vgl. np. sikar *Jagd*, sikardan jagen , phi. v(i)skar
Bdh. 61. 263?; binjisk 'Sperling = gunjisk^), phi. v(i)nc(i)sk
Gl. and Ind. 248, sivend. bunjis, binjis Journ. asiat. 1893,
252 ; pizmurdan statt bihmtrdan Verwelken, verfallen Gazo-
phyl. p. 167, jiid. pers. mit gu anlautend {gmmurdan\ also
aus mp. ^'viSnmrdan (oben p. 41); arab. Bistdm aus np. Bis-
tahm neben Gustahm = phi. Vistaxm Tab. 96; Bindoi =
arm. Vndoy, zu ap. Vindafarnah- u. s. w. Vgl. baskarl
oben p. 30.
§ 50. Ap. V im Anlaut vor r wird im Np. zu gii-
oder bi'i
HUB.txt:8367:zwar noch auf der HajjTabad- und Naksh i Rustam-Inschrift,
HUB.txt:8998:Rustam, arm. Rostom Mos. Chor. 79, syr. Rustam --= phi.
HUB.txt:8999:Rustahm aus *Rdtastahm^)? (Gl. and Ind. 140, Yatk. i. Zar.
NYB_vol2_glossary.txt:2124:but we are here in a part of Iran where Greeks reigned for about 200 years after Alexander (v. Tarn, The Greeks in Bactria & India, 1951). There is every reason to believe that their kings and magnates erected monumental buildings over their tombs, with which the Yvy1 of the de- ceased was in some way connected. The Greek Yvx1 could, however, only be ren- dered in Iranian by jän, as the ruvān belonged to a quite different sphere. Prob- ably these seven jdnakdns were built in the seven cities which Alexander founded in Bactriana and Sogdiana (Justin XII, 5, 8). The later attribution of such ancient monuments to the primordial heroes of East Iranian antiquity is a phenomenon too well known to need comment, cf Taxt + Jamsid, Nags 1 Rustam and the like. — Strictly speaking the reading HY?-d’n' = jän-dän 're- captacle of the jan’ would be admissible (cf uvnuciov Ļvxījg of the cinerary urn Sophocles, Electra 1126-1127), but this interpretation is perhaps too hazardous. — jānakān has a parallel in MPrs rw’ng’n, MPrth ’rw’ng’n ‘belonging to, serving the ruvan’, of pious works.
NYB_vol2_glossary.txt:3349:Rötastahm [lwtsthm] n. pr. 1162. — NP Rustam; Old Sogd rwstmy, Reichelt, Sogd. Handschr.- R. II, 63.
NYB_vol2_glossary.txt:3635:*Sif(a)rg [Splg] of doubtful meaning, per- haps: swift arrow, ~ % Rotastahm swift Rustam-arrows, arrows swift as those shot by R. 20%, — The form is to
NYB_vol2_glossary.txt:4528:its capital was Ghazna; it was the native country of Rustam. Cat. 88; Bailey, BSOS VI, 1931, 590; Gnoli, Ricerche storiche sul Sīstān antico, Roma 1967, v. Index.
NYB_vol2_glossary.txt:4683:DNa = Dareios, Nagš i Rustam inscription a, according to Kent’s edition (q. v.).
NYB_vol2_glossary.txt:7372:Rustam: Rötastahm
```


## [2026-10-15T02:45:34.585Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 8995,9003p HUB.txt; grep -n -i \"^tahm\\|^tang\\b\\|^tang \\|^tab\\b\\|^tab \\|^tāb\\|^tābistān\\|^tabistan\\|^taftan\\|^tābīdan\\|^tabidan\\|^stahm\\|^partaw\\|^ōstāf\\|^ostaft\\|^Tahm\\|ʾštʾp\\|^tafsīdan\" PHD_mackenzie.txt | head -30"
}
```


### [2026-10-15T02:45:34.993Z] TOOL RESULT

```
in Taxmaspada- (*mit starkem Heer , ein Meder), arm. tarn in
Tam-Xosrov Stark-Chosrau' = gr. Ta^i/o(jp6fjc, vgl. Tamsapor
bei Ammian u. s.w. Tab. 443, ZDMG. 35, 178; pers. tarn in
Rustam, arm. Rostom Mos. Chor. 79, syr. Rustam --= phi.
Rustahm aus *Rdtastahm^)? (Gl. and Ind. 140, Yatk. i. Zar.
51, West, PT. I, 140); sitam Unrecht, Bedrtickung = paz.
stahtn violence', phi. stahm oder staxm Phi. Min. p. 13, 2 ;
LW. diram, arm. dram (5. Jhd.) = arab. dirham, gr. dpaxiar}.
Ob np. paz. phi. sdmdn 'Grenze* = arm. sahman hierher
4663:stahm [st/zm I N sitam] power, oppression.
4864:tab [tp IN .....] fever.
4865:tab-, .....isn, v. taftan.
4866:tAb-, --iln, v. tMtan.
4911:tang [tng 1 = M, N --] narrow, tight.
8175:tab                             cut"    targ                         ~~
8176:tab-                          -cuP      tars
8187:taftan
```


## [2026-10-15T02:45:37.347Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 8985,8996p HUB.txt; grep -n -i \"tahm\\|taftan\\|tAbistAn\\|tabistan\\|abtab\\|Aftab\\|partaw\\|ostaftan\\|ostAftan\\|tAftan\" PHD_mackenzie.txt | head -20"
}
```


### [2026-10-15T02:45:37.711Z] TOOL RESULT

```
p. 194) = ap. Baxtris; auch mit hi: syr. ^r\2 N5ldeke,
Alexanderroman 14, 15, arm. Bahl Mos. Chor. 148 u. s.w.
c) xm = idg. km: daxm, daxma 'Dakhma' (Parsen-
wort!) = zd. daxma- H. 543; tuxm Same, Geschlecht' =
zd. taoxman-, pSz. tuxm, arm. tohm (aber ap. tauma-l);
haufiger wird xm schon zur Sassanidenzeit zu hm und mit Aus-
fall des h zu m: Gustahm = Bistahm, anf Miinzen Vistahm
(ZDMG. 19, 482), arm. Vstam Sebeos 30, 39, arab. Bistam,
SLf*Vi8taxnfa'; tahm — taham *stark* (auch in Tahamtan Von
starkem KSrper, Rus tern's Beiname) zd. taxma-, ap. taxma-
in Taxmaspada- (*mit starkem Heer , ein Meder), arm. tarn in
Tam-Xosrov Stark-Chosrau' = gr. Ta^i/o(jp6fjc, vgl. Tamsapor
623:add tahm !thm I =M, N "'] strong, brave.
4663:stahm [st/zm I N sitam] power, oppression.
4666:stambag [sthmbh l (-/z- < stahm) I M <stmbg, N sitamba] oppressive;
4865:tab-, .....isn, v. taftan.
4875: tAbidan [t)pytn l IN .....] = tAftan.
4878: taftan, tab- [tp-tn l ] grow hot; shine.
4880: tAftan, tAb- [t)p-tn l I P t)b-, N .....] heat, burn; shine.
6113:brassard bazabanag.                    burn (vt.) dazidan, soxtan, taftan,
6758:hang (up) agustan.                       heat (v.) taftan, (tabidan).
6797:hide (v.) nihuftan, (nihumbidan).              hot garm; grow""'" taftan.
7187:nourishment parwiil(isn), parwarisn.   oppress awistaftan.
7190:number mareag), sag.                       pazd, stahm, stahrn(ag)ih, starn-
7192:nurse, (wet·) dayag.                   oppressive stahmag, starnbag.
7307:   stahm, tuwiin, zor.                         produce (n.) bar.
7707:   wand, saxt, stabr, stahmag, sur,        supplication liibag, liibakkarih.
8187:taftan
8298:Tistar              "tb\Y\l'         taftan
8899:sturg              ~\lU'              stahm                      <~
8902:storbiin         \~~,teV              stahmih                  ~te»
8903:stard                 ,~,tUJ          stahmagih               A(J~te.»
```


## [2026-10-15T02:45:41.871Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"wistAf\\|wistaf\\|stAb\\|tAbistAn\\|tabestan\\|hAmin\\|summer\\|sunshine\\|partaw\\|ray\\b\" PHD_mackenzie.txt | head -20"
}
```


### [2026-10-15T02:45:42.362Z] TOOL RESULT

```
295:scarcely to merit the name. The establishment of the original
300:phonetic Manichaean script it has become possible to establish
1135:·apedag [>j',ytk I P )pyd(g)] lost, stray.
1137: --dAr [-d)l] custodian of stray animals.
1159:arastan, aray- [)l'stn', 'l'd- IN....,] prepare, arrange, adorn.
1356: axwarr ['hwll N axur] manger, stable•
1438:azray- [)zr)d-] adorn.
1460:bahra~ [b)hlk'], (az) an,.", rAy: on that account.
1717:    ""'-sray [-sPd] harpist.
1754:  - ray: for what, why.
1787: . . . . (rAy) : why?
1797:BrAy                                 23                             dahlbed
1798:elrAy [cl'" I P cr'g, N ,...,] lamp.
1883:P daray [dl'g I J --, N daray] bell.
2051:dray-, .....,isn, ' v. drayidan.
2057:drayidan / drayistan, dray- [d1'd-ytn , -stn' I M dr'yst, dr'y-, N
2091:drustabed [drwystpt l ] chief physician.
2189:  -- ray ~e [ef. N z-e-ra] because, since.
2351:fray [pl)y I M pr)y] more, much.
2388:freh [plyh IN Jirih] more, much, = fray.
```


## [2026-10-15T02:45:45.988Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"taxma\\|tancišta\\|tančišta\\|tąsyah\\|urupay\\|urupi\\|tafnah\\|tafnu\" BRT.txt | head -30"
}
```


### [2026-10-15T02:45:46.719Z] TOOL RESULT

```
190:Die  angeführten  Texte  bringen  ausserordentlich  zahlreiche  Wiederholungen. Und  zwar  sind  entweder  zwei  oder  mehr  Stellen  einander  völlig  gleich  oder  sie unterscheiden  sich  nur  in  untergeordneten  —  d.  h.  für  das  Wörterbuch  wenigstens untei^e ordneten  —  Stücken.  Als  Beispiel  für  die  erste  Art  von  Wiederholungen mögen  dienen:  Y.  65.  2-5  —  Yt.  3.  2-5;  Yt.  5.  10  =  12,  14,  16,  20  (usw.);  Yt. 5. 19  =  23,  27,  35,  39  (usw.);  Yt.  JO.  98  =  135;  Yt.  j^.  15  (von  hü  bis  taxmahe')  ^ Yt.  10.  70,  127;  Y.  57.  25  (von  akeca  an)  —  Yt.  10.  93  usw.  —  Die  Wiederholungen der  zweiten  Art  zerfallen  in  verschiedene  Gruppen:  Yt io.  103  wiederholt  sich  von yS  hantaia  an  wörtlich  in  Y.57.  isfl,  nur  dass  hier  das  ca  hinter  har>ta  fehlt; irgend  ein  Grund  für  die  Abweichung  ist  nicht  vorhanden.  Yt. /o.  94  (^=  114I und  Y.57. 26  stimmen  völlig  lusammen,  nur  dass  auf  die  Eingangsworte  aäa  nS tum  dort  der  Vokativ  mikira  vouru.gaoyaoite,  hier  aber  traosa  afya  huraöha  folgt; die  Gebetsformel  ist  die  selbe,  aber  die  Adresse  ist  verschieden.  Ähnlich  steht es  mit  den  vier  in  Yljo.  igof.  enthaltenen  Stücken,  die  von  vier  Waffenarten Mihras  durchaus  das  Gleiche  aussagen;  nur  eben  die  Namen  der  Waffe,  sowie deren  Beiwörter  machen  die  Verschiedenheit  der  Stücke  aus.  Besonders  zahlreich findet  sich  diese  Art  der  Wiederholung  im  Viälvdäi  {Vendidad);  z.B.  unterscheiden sich  in  dem  Kapitel  über  die  Verträge  (V.  4)  die  Abschnitte  6  bis  10  und  ander- seits II  bis  16  nur  durch  den  Namen  des  Vertrags  und  der  Zahl  in  der  Buss- bestimmung. Femer  haben  V.p,  53,  54,  55  und  S7  '^'on  üäca  an  den  gleichen Wortlaut,  nur  dass  das  dreimalige  para  von  53  in  54  durch  kaha,  in  55  durch nöü,  in  57  durch  pascalta  ersetzt  ist  In  den  liturgischen  Teilen  des  Yasna  wieder sind  grosse  Stücke  bis  auf  die  Eingangs-  oder  Schlussformel  gleichlautend.  So decken  sich  Y,  i.  3  ff.  und  5.  5  ff.,  4. 8  ff.,  7.  5  ff.  vollständig  bis  auf  die  Eingangs- worte, die  zu  Y.  1:  nivaiöayemi  hankärayemi,  zu  Y.^:  äyese yeSH,  zu  Y.  4:  Hat  dis äva^ayamahl,  zu  Y.  7:  alaya  daöami  lauten,  während  anderseits  Y.  2.  äff.  und 6.\S.  nur  darin  auseinandergehen,  dass  hier  (Y.  6)  jeder  Abschnitt  mit  yatamatde endet,  dort  (Y.  4)  jeder  mit  ahmya  zaohre  bar>smanaica  eingeleitet  und  mit  äyese yeiti  geschlossen  wird.
2798:auf  ein  relativisch  angeschlossenes  Nomen vorausweisend:  >o/<iW:4a/  sp3  urupis  fuai -so  spl  yS  urupis  .  ,  V.5.33;  —  ufa  vä nasus  raz'iwst  .  .  'sa  Jruxi  yä  ttasus  V. J.14;  5.27,  28,  7.1—4,  *.i6,  41',  9.40, 48;  —  ä^ravaium  yaoida^o  ,  .  'so  nä yö  yaoid.1>ryS  V.<).  37— 39;  40,  42,  If). 21,  Vd.iV.  10.  b)  substantivisch;  aStacTva daxmaisva . .  "sö  zl  asH  äaivanam  rapakö V.  7.55f.;  —  daxme  .  .  yat  °/a  pqsnu ra^'>a'.J/(sd-)  V.  7,49f.;  —  aisa  y5..aiwi.- >r}lti^ätus  (sd.)  *aivayaHi  -io  barfsmö.- sbrfiti  ratufris  N.  /Oj;  —  slaotaca  (sd.) yasnäica  . ,  yat  °sa  ahurake  mazda  "Pre is- lieder  .  .:  das  des  AAM."  Vr.if.ö;  6;  — jtal  ..  kmntiit  ava  hö  mirysüe  anJmltÖ si  'SÖ  , .  "wenn  er  . .  operiit  (und)  der foperirte)  stirbt,  dann  ist  er  disqualifizirt.." ^'■7-37;  —  iD  Kongraenz  mit  dem  Prae- diltkt;  cit  ai-at  vacö  äs  ,  J  baya  °h  3s ahunahe  vairyehe  "Was  war  das  für  ein Sprach  .  .?  Das  war  das  Stück  A/iV." 'W  i<).  I  —3,  o)  öfters  zugleich  auf  ein
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
4754:—  yal:iä  ro  data  °/il  (VP.)  spsntä  a^iä na  >räzäa?n  Y.5#.  5;  II.  iZ,  14.  i,  42.1, • — ■  mai^amnt  . .  yat  ksrmlun  "la  (NS.) sp>nta  vispe  hazaesaYLio.$i;  7.3',  /0.92, y.ga,  Y. 57.^23,  60.6;  —  /ml  '/ä  (NP.) spmtä  gaiia  giurvain  Y.2S.0;  Ny.l.i, VyL^o;- —  spmtsttg  °s3ng  yava^yff  yavaSsvB Y.,J.')-3;  4-A\  —  °^^  sptrüa  huxiäi:ra hmfmhs  (Stverz.)  Vr. ;/.  12;  usw.;  —  -sS spints  vatihali  srlräi^  namqn  äebaya  Y. /  5. 1 ;  Vr.  6.1;  —  vlspqscä  'iq  spintq  yasa- maidsY.42.()\  —  °h  spinlS alaonam  yasa- maideY.yi.2,  G.  2. 6  (wo  'sJtca);''*  — 'sanqm  sp)ntanqm  xialtanqm  vinzidsi- %ranqm  Ötnzatqm  aiwyämanqm  taxmanqm ähuiryanqm  ySi  aihy^anhs  alwvanB  ysi hapta  iam^.manavAö.. Yt  lj.82f.;Y.j. 4, 20,3;  — y3i  hapta  'sä  spmta  Yt.2.3;  — ape  °ianam  spmtanqm  dähXtn  Y./9.8;  Yt. ;^.  8 1 ' ;  —  vankubyS  yazataiibyS  yat  'laii- byS  spmtaHbys  Vr. 8.\;  ff. 4, 13. \,Yt.4.y,
5485:•  j.,  g.  aradra-  Adj,  (fem.  'rJ-)  'getreu, 'verlässig':  'rS  '^wävqs(sd.)  ÄitzSntuü  sfmtö mazdä  Y. 4:_j.3;  46.^;  — fravasayB..  °rä taxmä  *at>javuAai/i/ \l.  ij.  $2;  75;  — mihrgm  . .  y5  äsunqtn  äsus  yS  'ranqm  °rö y3  taxmanqm  taxmS  Yt.  70. 65.  a)  mit DaL:  kuirä  tsi  °rä  masdä  ysi..  caxrayö' (sd.)  "ob  sie  wohl  dir  getreu  sind,  die  . ," Y._j4-7-  A)  insbes. 'dem  Glauben  treu, gläubig,  fromm':  firasaosträ  air3  tu  'r.lis idi  hvB^S  täis  yitig  . .  "o  Fr.Hv.,  dahin geh  mit  diesen  Frommen,  denen  . ."  Y. 4'j^i6;  —  kä  iw'ffi  a/a  äk,i  (sd.)  'ring isyl  Y.  4S.  8;  S*}.  4;  —  fatrijasai  .  .  at vä  aia  "rahyacä  mmankä  "..und  vor  euch, o  Asa,  auch  mit  dem  Gebet  des  Frommen" Y.50.8;  —  da^at  ahrnili  tat..  arfdvJ . . 'räi  yavmiini  jatoyantäi  da^ris  ayaphm Ytj.ig;  13a,  /5.1,  21.
5555:•)    Über   die   Bedeutung   des  Gotls   ist   den    t'isjie  °va   Vlspe  taxma   .  .  kave  HK.1Q.1z; ,i'j5i sehen  Teilen  nichu  Klnies  lu  entnehmen;   —    'v3  as.vancS   kava    usa  Yt5.45;   —
5713:idn^taxma^  näma"  °tiyi^    Bh.^.  i  /p.g,  Yt  /_y.  28;  —  öarjimrS  ^avaühe  'htS
5799:•  j.  asta'va-  Adj.  'mit  einem  Knochen Teisehcn';  °v3  vä  taxmahe  mirr/ake pars- nai'SvS..  "wer  einen  Knochen  des  starken Vogels  oder  eine  Feder  (als  Amulet)  trägt .." YL/4.3(S.
7136:[  da^at  . .  '"krasca  . .  paitHarat  N.  ■j4;  — j  iävanänS  (sd.)  dilityS  gätus  fralarqn  barts- ,  mqn  aparqm  ''i<ri)  N.79;  79 ; — '"ai^a  yff  dim *frähincin  (sd.)  *antarp  'tartmca  barsmaca \  ". .  zwischen  dem  Feuer  und  dem  B.  (an ■  der  Opferstätte)"  N.  08''\  c)  GS.  mit I  ta/nav-  m.  Flur.  'Feuergluten'  sva.  'Fieber- lanfälle':  kö pagiryS..'%rS  tafnus  därayat tanaot  haca    masyehe  V.  20.  i.  d)    Es
7470:•  j.  äsu.aspya-  n.  'Besitz  schneller  Rosse, Reichtum  an  schnellen  Rossen':  'pTm da'jiiiti  mi%rU  Ytjo.3; —  '^wqm  naracit yöi  taxma  Jat'iyhnte  -ptm  YL5.86;  98.
8304:—  mihnm  .  .  yetike  valnn  Aangrgwnäiti asii vamihi ..yat  dim  dätnBis  °ns  AuÄrixtim (sd.)  .  ,  irinaxH  YL/O.  68;  —  dahmaya vaakuyi  a/ritöii' uyrni  dümsis  '■näi  \.fi.t, S. /.30; —  uyraAe^a  taxmaAe  dämsii "nahe yazatahe  Y.  /.  1 5 ;  —  uyr^m  taxmem  dämeis 'n?m  Y.2.1S,  7.26,  77.23.
8334:•  j.  upara'tSt-  f.  'Superiorität,  Über- lefenheif:  ^wam  nara^it  ysi  taxma jai'jyhrtte  .  .  sfarfttanAasca  'tätS  (AP.) YL5.86.  a)  sonst  mit  vananl-  Adj.: dasdi  .  .  tai  äyafUm  .  .  V9r9%rar}n}mea aAurdoat?m  vanaintimla  *t3t>m  Yt  ro. 33;  5-86.  y-34.  A'i,  X-57-33;  —  vin- liraynaAeca  . ,  vanaintySsca  paiti  'täto  Yt. 8.11.  A)  als  Gottheit:  avistayalca  .  . amavaihya  faurvatäis  amavaihyä  Häts (GS.)  Vr.(f,4.  a)  sonst  mit  vanani-  Adj.: v^ry^rayramca  ..vanaintimca  '/aftw  Y.2.6; Vr.2.8;  —  vfhhraynahe  .  .  vanainiyäsca 'tätö  Y./.6,  Vr./.6,  Vt.J4.o.
10879:•  j.  xStävay-  Adj.  'zur  Familie  der Xstavay  gehörig,  Xstavi-^a.nvi^ -.  ysi  taxma 'vayS  dänubyö  azm  pilana  Yt  13. 37 ;  38.
11331:•  p,  tSi&'a°'taxma-  m.  EN.  eines  Sagar- tiers,  der  sich  gegen  Darius  I.  empörte,
11356:paitis  , .  zbayeiti  . .  yim  *driyBsat  . .  sba- yäti  Yt  10.  84;  —  %wqm  yazSnte  .  .  dai- AAu.paiays  . .  '^wqm  naraHt  ySi  taxma Jai'jyhnte  Yt  5.  85  f;  —  haraiti  bars  .  . kä  Aama  päirisSite  frSpayä  (sd.)  . ,  M3r?- fiaaS  gairis  . .  AämS  hasHt  päirisaile  .  . "das  jy.-Gebirg  . ,  umlagert  . . ;  . .  das  Z.- Gebii^,  auch  das  umlagert  . ."  Yt  ig.  i; y- 69;  —  Vlspe  ,.  tirKtnti  pfnmne  {%äj) avaia  mävayaiit.-tprisantu  Yt  14.38;  — *daSinqtn..Äaoyqm  h! paiayqm ..  dumtnüit Af  upa.%w^r^saym'V.i3.ai.;^vlsfe  haoma . . yaicit . .*upa  *dintäku{sA.)  V./0.17J  — Aazaignrn  maoirinqm  d3nS.karSanqm  ava.- jartyat  duye  hazanre  anyalsamat'-'^  V.  18. 73i  73i  —  ^y^  *gr}Amö  ä.ASi^Si  (sd.) «r  ksvayas^l  xratül  «r  dadat  ".  .  Gr., de^leichen  (sva,  und)  die  K.  richten  .." Y.  J2.  14; —  aSavatca  alsasät  ästärayeite (sd.)  N.72; — nava..anaiwyasHi  kunämi; hinti  (Sp.  370  o.)  .  .  mävayacit  ca^warS arsäna  V.lS.^j;  —  ksnti  anyäsät'^  (Sp. 137  in.)  asäs^a  /äi^ris^a  srIras/a..Y.l.2o; —  aam^i  akyS  . .  %wam  tUSökj  , .  vai- <hm  (sd.)  Y.  ig.  10;  —  mainya  .  .  yS  ä narSm(,sd.)ät.,Aäi>0  Y.^i.y  i — in  auffälliger Stellung:  mUca  paslaSa  mazdayasna  vXmä- oasHt*^  vTmSoayanta  "nicht  sollen  sie  dann auch  bei  M.  als  Ärzte  praktiziren"  V.  7, 38;  38,  40;  —  hinter  ula^^:  iavaj  aiwi.- vanyä  .  .  ta^ryävanttm  , .  ptiatamca  .  . Uta  anyäscit'^  ..  kyaon&tgkB  Wtig.ST, 89;  —  hasannm  aspä  uta  äsitqmHt /rastUntim  Yt  18.  5 ».  a)  Bei  hypotak- tischer Saufiigung  steht  das  mit  /■■  hervor- gehobene Wort  jeweils  an  zweiter  Stelle*', U2W.  a)  des  Hauptsatzes;  b)  im  Aw.: Sfit  MOra^uslrS  da^äU  sanm  vyämrvUä .  .  flS-a  *aspm^  .  .  vlinruyg  Y.  12.  6\  — ya'ha    . .    kvarsxiatä^m    .  .  fraca    Siti  .  .
11819:taxma-  62Ö
11841:*  j-i  g-  (.  P-)  taxma-  Adj.  (fem.  °mä-) 'fortis,  tapfer,  tüchtig,  energisch,  helden- haft'; a)  von  a)  Menschen  und  ß)  Göttern: a)  masyänqm  .  .  'manqm  V.  20.  i ;  —  nä •Mö  Yt  jj.  67,  Aog.Ä^;  Vyt.  2j;  —  narU 'ma  (NPm.)  Yty.  27;  5.86,  iS-Hn^^h
11843:627  taxman-
11845:•  j.  taxman-  n. 'Lauf  fliessenden  Wassers: %risum  apqm  '^raotö.stäcqm  °manqm  pairi- itayeiii  "ein  Drittel  der  im  Flussbett  fliessen- den Wasser  hindert  er  an  ihrem  Lauf V.  7*63.
11847:•  p,  taxma-späda-  m,  EN.  eines  Heer- führers Darius  I, :  'dc^  näma'  madei'  Bh. 2.14;  14.
11851:•  j.  taxmö.Mma-"'  Adj.  'der  tapferste, energischste,  heldenhafteste' :  taxms. .  "tsma (stattNSna.)  n^ffia  ahmt  Yt  73.46;  —  vamt ('den  Vayav^)  taxmanqm  'tsm^m  Yt  75.  57.
11894:'damit,  auf  dass'  vorher:  yat  yavo  (sd.) pourus  baväf  aha  ma'hnm  *t'  ^  mairyat ^•3-a-  3)  'damals,  da',  ini  Wechsel mit  ta6a  (sd.)*':  tala  dim  akurS  mazdä avqn  (Sp.  1 1 2  m.)  . .  t°  apu  urvaras<a  YL 8."];  —  fravasayS  .  .  yä  .  .  laoa  nijasm (Sp.  500  m.)  xÜiviwyS  *pi^  yöi  taxma xstävayB  dänubyS  az>n  pthnh  Yt.  13. 37.  4)  'dann,  alsdann':  yas>  t  *api- vataiti  (sd.)  parmtarim  (sd.)  issil  N. 12.  a)    zusammen    mit    aaf:    US  patti
11926:•  j.  tafnah-  n.  i)  'Hitze,  Glut'  (nur  Ab- leit.).  2)  'Fieberhitze,  -glut':  yaiÖa  hi hqm  °nS  jasat  (Sp,  501  u.)  avi  tanuye  zsis- nuye  V.  7. 70.
11931:•  j.  tafnah'vant-  Adj.  'Gluthitze  enthal- tend':  mäaA^m  ..  *'natfhuntfm'1  Ytj.S-
11988:•  j.  tan£iita-  Adj.  (fem.  'li-)  'der  tapferste, energischste,  heldenhafteste';  i)von  a)Men- schen  und  ß)  Göttern:  a)  tBtn  xara^u/tra .  .  yö  aojists  .  .  °ts .,  %waxiWs . .  abaval mainivä  dämqn  Y.p,  15;  —  'timca  darae- ^at»«  YL3.73;  —  häuca  ii:ra..taxmanam
12283:•  j.  tizi.daä-  Adj.  (mask.  'ta-)  'mit scharfem  Gebiss':   urupii  (sd.)   'iahe  V,
12511:•  j.''daevö.tbiä-"m.EN.  eines  Gläubigen: 'ibsii  taxmaht  aiwns  Yt  y.  98.
13393:•  j.  'dänav-  Adj.,  bezeichnet  einen  den  Ira- niern  feindlichen  i'Srischen  Volksstamm: tala  yöi  taxma  xstüvayS  'nubyS  az)n  p?sana yüz»tn  (näml.  /ravasayj)  tdm  taurvayata v>r?^r?m  'nunqtn  türanqm..t6al^3  'nunam türanqm  .  .  xrBma  asSbis  frasinta  (sd.) "nunqm  baivari.pailinqm  Yt-/J.  37f.;  — yat  baväma  aiwi.vanya  °nav3  (als  AP.) tära  vyäxana  Yt.  J.  73.
15708:•  j,  parana'va-  Adj,  'mit  einer  Feder  ver- sehen': aslavff  (sd.)  vä..  'vH  vä  taxmaAe mirr/ahe  Yt.  14.  36.
18506:•  j.  'naeza-  m.  Name  einer  Krankheit: aüalfva  daxmalha  kamiavamU  axtiica gannusla  tafnusca  'zasca  sSrastisYaV.j.SJ ; —  paiHstätSe  gamiSusca  tafttaolca  'sahe^a sarastSisca  Yt/J.  131.
```


## [2026-10-15T02:45:51.163Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"j\\.  urupay\\|urupay-\\|urupi-\\|•  j.  taxma\" BRT.txt | head; grep -n \"j.  urupay\\|urupay-  m\" BRT.txt|head -3"
}
```


### [2026-10-15T02:45:51.544Z] TOOL RESULT

```
11845:•  j.  taxman-  n. 'Lauf  fliessenden  Wassers: %risum  apqm  '^raotö.stäcqm  °manqm  pairi- itayeiii  "ein  Drittel  der  im  Flussbett  fliessen- den Wasser  hindert  er  an  ihrem  Lauf V.  7*63.
25526:•  j.  urupay-m.EN.  des  zweiten  iranischen Königs,  eines  altem  Bruders  Yimas,  der ihm  nachfolgt"':  taxmO  °/a  (NS.)  asinavä Yt.75,11;  —  kavann  x'ar»nB  . .  yat  upa- nhaca^  taximm  'pi  (alsAS.)*'  azinavantam .  .  yat  barata  anrim  mainyBm  framittm (sd.)  aspahe  kihrpa  %risattm  aiwi^äma- nam  Yt.  jp.  28f.;  —  ^zainanuhanttm  .  . ya%a  taxmS  °pa  Az.  2.
25526:•  j.  urupay-m.EN.  des  zweiten  iranischen Königs,  eines  altem  Bruders  Yimas,  der ihm  nachfolgt"':  taxmO  °/a  (NS.)  asinavä Yt.75,11;  —  kavann  x'ar»nB  . .  yat  upa- nhaca^  taximm  'pi  (alsAS.)*'  azinavantam .  .  yat  barata  anrim  mainyBm  framittm (sd.)  aspahe  kihrpa  %risattm  aiwi^äma- nam  Yt.  jp.  28f.;  —  ^zainanuhanttm  .  . ya%a  taxmS  °pa  Az.  2.
```


## [2026-10-15T02:45:53.400Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25520,25535p BRT.txt | cut -c1-900"
}
```


### [2026-10-15T02:45:53.948Z] TOOL RESULT

```
AbleiL  aus  uru%may-').  —  P&.;  StSii!aSmani/. —  >>  Vgl.  zEild.  ai,  hrinya-  Adj.  'wogend'  ; ürmiy-  m.  "Woge'.
•  j.  umd'wan-,  'iwar-  n.  'Eingeweide, Bauch':  'wan  F._?g;  —  yB  gSus  'wart hqmpnfraiti  (sd.)  V.  4.48;  —  auch  Plur. : astila  gaonala  ^dimohaca  *''wqmca  pah- yasca  fraväxlas^a  YL  /_J.  1 1 ;  —  yB  nars aiaonB  kaca  "wqn  bt/asyät  "der  bei  einem Gläubigen  die  Eingeweide  kurirt"  V.  7. 44(?);  —  alte  äaxma  (sd.)  upanAanzalta an/aräj  naiMät  barp%ri/va  'WBJiva  "die Leicheostätten  soll  sie  (damit)  besprengen innen  im  Mutterleib,   im  Eingeweide"  V.
5. 5 1 .  a)  in  Ubertr.  Sinn  'Kern  (,  Quint- essenz)'": kai  asti  damayh  mazdayas^il ry  "was  ist  der  Kern  der  masd.  Keli- gion?"  V.^.30.
VgL  np.  rüda,  nbal.  rS%  'Eingeweide';  Bthl. IF.  5.  »28.  —  Pü.  (ru  F.):  itamb,  (in  V.  /): an  ddprn  ad,  (sonst):  tranaakr.—  '>S.  *»ra!rya-.
•  j.  umpay-  m.  (auch  mit  ^span-  m.) Name  einer  Art  des  Hundegeschlechts: hau  'pü  (statt  GS.)  HU.äatahe  . .  hau vispanam  .  .  spaci^ranqm  V.  13. 16;  — spä  •pii'V.S.ss'.
El?  FaIschFlCKVglWb.«.5s6.  — PD.:rpnk, nach  DsT.  ZA.  i.  77  für  rddpnk  (s.  lU  na- sujfafya-),  das  er  raipük  liest  und  mit  np. räsü  'WieEcl'  identiliilrt  Diese  Bedeutnng will  auch  GQ.
•  j.  urupay-m.EN.  des  zweiten  iranischen Königs,  eines  altem  Bruders  Yimas,  der ihm  nachfolgt"':  taxmO  °/a  (NS.)  asinavä Yt.75,11;  —  kavann  x'ar»nB  . .  yat  upa- nhaca^  taximm  'pi  (alsAS.)*'  azinavantam .  .  yat  barata  anrim  mainyBm  framittm (sd.)  aspahe  kihrpa  %risattm  aiwi^äma- nam  Yt.  jp.  28f.;  —  ^zainanuhanttm  .  . ya%a  taxmS  °pa  Az.  2.
Eig.  Bed.?  Falsch  DsT.  ZA.  2.  583,  FlCK  BB. 34.  314.  —  •)  Spälcr  Taxmürq/,  Tahtnüras  ge- nannt. —  ')  Man  verlangte  'pim,
•  g.  urüpa'ya-  den.  Praes.  31  '(Schein- bilder,  falsche  Vorstellungen  hervorrufen sva.)  täuschen,  betrügen' "':  *maäaAya  (sd.) yä  angrayä  karapanB  uropayäntl  yäiä xrata  äus»xsa%ra  dahyunqm  ". .  Rausch- Iranks  . .,  durch  den  böslich  die  Karapan und  durch  den  mit  Absicht  die  üblen Herrscher  der  Länder  betrügen"  \.48. 10.
*uripa-  n.  'Scheinbild' ;  ai.  rüpö-  n.  (woto Bgm.  Grdr.» /.  a6o),  räj^yaCj 'imiutur".  — Pü.: rätüitend  pinakXh,  erL :  pänakXh  i  liämän  tu kunind.  Mau  lerlegle  urü-^pay.  —  1)  Anders Gdn.  KZ.  30.  534,  bei  dessen  Fassang  ich jedoch  ein  Objekt  verlangte.
•  j.  urunya-  m,  'Gefäss';  i)  für  den Myazda,  'Schale,  Schüssel':  yailam  taya- nqm  aiaurune  . .  °ya  rai^wis.6ajina  , . V./4.8.  2)  Du.  die  beiden  Gefässe, 'Eimer'  od.  dgl.,  in  denen  den  Rossen Wasser  und  Futter  gereicht  wicd(?):  äpe urvaire  yazamaide  aourvatqm  •/w(AD.)" asavantm     asahe     ratum    yazamaide    G.
KompA.(?l.  —  EI.7  —  Aus  ar.  *{t)ninia-.  — PiL  (zu  V.):  myacd  dän,  (lu  Y.):  tttnärämand. —  0  Statt  -Bfo,  S  3ÖÄ  32. j.,  g.  urun'z  1,  unmn:
dby  Google
1533
uninyö.vSiSimidlrä-
»534
```


## [2026-10-15T02:45:58.481Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-10-15T02:45:58.884Z] TOOL RESULT

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


## [2026-10-15T02:46:05.376Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://en.wiktionary.org/wiki/تنگ\" \"https://en.wiktionary.org/wiki/تنجیدن\" \"https://en.wiktionary.org/wiki/تهمتن\" \"https://en.wiktionary.org/wiki/تهمورث\" \"https://en.wiktionary.org/wiki/رستم\" \"https://en.wiktionary.org/wiki/تب\" \"https://en.wiktionary.org/wiki/تابیدن\" \"https://en.wiktionary.org/wiki/تپیدن\" \"https://en.wiktionary.org/wiki/تابستان\" \"https://en.wiktionary.org/wiki/آفتاب\" \"https://en.wiktionary.org/wiki/مهتاب\" \"https://en.wiktionary.org/wiki/پرتو\" \"https://en.wiktionary.org/wiki/شتافتن\" \"https://en.wiktionary.org/wiki/tight\" \"https://en.wiktionary.org/wiki/tangle\" \"https://en.wiktionary.org/wiki/thick\" \"https://en.wiktionary.org/wiki/tepid\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tenk-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tep-\" \"https://en.wiktionary.org/wiki/taxma\" \"https://www.etymonline.com/word/tight\" \"https://www.etymonline.com/word/tangle\" \"https://www.etymonline.com/word/thick\" \"https://www.etymonline.com/word/tepid\" \"https://www.iranicaonline.org/articles/rostam-1\" \"https://www.iranicaonline.org/articles/tahmuras\"; do echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 503, roots Tenk/Tep: etymology check\" 2>&1 | tail -1; done"
}
```


### [2026-10-15T02:46:28.863Z] TOOL RESULT

```
== https://en.wiktionary.org/wiki/تنگ
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3c0babba0e34bb38.txt
== https://en.wiktionary.org/wiki/تنجیدن
/home/sfmqrb/git/rishe-private/data/verification/sources/web/39c05482f6c025c8.txt
== https://en.wiktionary.org/wiki/تهمتن
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2a47e565f5f908db.txt
== https://en.wiktionary.org/wiki/تهمورث
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ff869a5c1356b51d.txt
== https://en.wiktionary.org/wiki/رستم
/home/sfmqrb/git/rishe-private/data/verification/sources/web/350dd9b8a87fe440.txt
== https://en.wiktionary.org/wiki/تب
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5fafb5208b258fdd.txt
== https://en.wiktionary.org/wiki/تابیدن
/home/sfmqrb/git/rishe-private/data/verification/sources/web/24b0a25c595f14af.txt
== https://en.wiktionary.org/wiki/تپیدن
/home/sfmqrb/git/rishe-private/data/verification/sources/web/211789acf15b5b32.txt
== https://en.wiktionary.org/wiki/تابستان
/home/sfmqrb/git/rishe-private/data/verification/sources/web/60073a2e2cc08773.txt
== https://en.wiktionary.org/wiki/آفتاب
/home/sfmqrb/git/rishe-private/data/verification/sources/web/948d2d1ce1d3354a.txt
== https://en.wiktionary.org/wiki/مهتاب
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1543ee2dfdd393e7.txt
== https://en.wiktionary.org/wiki/پرتو
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ebed09d603c2b47a.txt
== https://en.wiktionary.org/wiki/شتافتن
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d73bf394998a3735.txt
== https://en.wiktionary.org/wiki/tight
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3a54efe485515277.txt
== https://en.wiktionary.org/wiki/tangle
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6c3c6c21eb6f12d2.txt
== https://en.wiktionary.org/wiki/thick
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e9f1a3676752016d.txt
== https://en.wiktionary.org/wiki/tepid
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3a8e70a3b9ca6c60.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tenk-
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f1292d129a579357.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tep-
/home/sfmqrb/git/rishe-private/data/verification/sources/web/66888b0a62be5831.txt
== https://en.wiktionary.org/wiki/taxma
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e8bd2defa3d0e716.txt
== https://www.etymonline.com/word/tight
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e433c94b0a7a1899.txt
== https://www.etymonline.com/word/tangle
/home/sfmqrb/git/rishe-private/data/verification/sources/web/834fab871b95838e.txt
== https://www.etymonline.com/word/thick
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4c340697ef7d78ca.txt
== https://www.etymonline.com/word/tepid
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7ec6fec08384222f.txt
== https://www.iranicaonline.org/articles/rostam-1
/home/sfmqrb/git/rishe-private/data/verification/sources/web/aa8a19425de336a5.txt
== https://www.iranicaonline.org/articles/tahmuras
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f508f16256c72792.txt
```


## [2026-10-15T02:46:32.084Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 3c0babba0e34bb38 39c05482f6c025c8 2a47e565f5f908db ff869a5c1356b51d 350dd9b8a87fe440 5fafb5208b258fdd 24b0a25c595f14af 211789acf15b5b32 60073a2e2cc08773 948d2d1ce1d3354a 1543ee2dfdd393e7 ebed09d603c2b47a d73bf394998a3735 e8bd2defa3d0e716; do echo \"=== $f $(wc -c <$f.txt)\"; grep -A4 -m3 \"^ *Etymology\" $f.txt | grep -v \"^--$\" | cut -c1-700; done"
}
```


### [2026-10-15T02:46:32.682Z] TOOL RESULT

```
=== 3c0babba0e34bb38 9533
 Etymology 

 1.2 
 Adjective 

 Etymology 1 

 2.1.1 
 Pronunciation 

 Etymology 2 

 2.2.1 
 Pronunciation 

=== 39c05482f6c025c8 17366
 Etymology 

 1.2 
 Pronunciation 

 Etymology
 [ edit ] 

 Borrowed from a Northwestern Iranian cognate of Manichaean Middle Persian 𐫤𐫗𐫉- ( tnz- /⁠tanz-⁠/ , “ to strain, press ” ) , from Proto-Iranian *tanč- ( “ to twist (together), become narrow, dense, constrict ” ) , from Proto-Indo-European *tenk- ( “ to compact ” ) . Akin to Ossetian тындзын ( tynʒyn ) , Old Armenian տանջեմ ( tanǰem ) , Old Georgian ტანჯვა ( ṭanǯva ) , as well as Sanskrit तञ्च् ( tañc , “ to contract, coagulate ” ) ; see the Sanskrit for more cognates. [ 1 ] 

=== 2a47e565f5f908db 136
=== ff869a5c1356b51d 138
=== 350dd9b8a87fe440 7842
 Etymology 

 1.2 
 Pronunciation 

 Etymology 

 2.2 
 Pronunciation 

 Etymology 

 3.2 
 Pronunciation 

=== 5fafb5208b258fdd 11232
 Etymology 1 

 1.1.1 
 Pronunciation 

 Etymology 2 

 1.2.1 
 Noun 

 Etymology 3 

 1.3.1 
 Verb 

=== 24b0a25c595f14af 3083
=== 211789acf15b5b32 9085
 Etymology 

 1.3 
 Pronunciation 

 Etymology
 [ edit ] 

 (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . Particularly: “Onomatopoeia?”) 

=== 60073a2e2cc08773 5633
 Etymology 

 2.3 
 Pronunciation 

 Etymology
 [ edit ] 

 Inherited from Middle Persian 𐭲𐭠𐭯𐭮𐭲𐭠𐭭 ( tʾpstʾn /⁠tābestān⁠/ ) . By surface analysis , تاب ( tāb  / tâb , “ heat ” ) + ـستان ( -istān  / -estân ) .

=== 948d2d1ce1d3354a 11126
 Etymology 

 1.3 
 Noun 

 Etymology 

 2.3 
 Pronunciation 

 Etymology 

 3.2 
 Noun 

=== 1543ee2dfdd393e7 5116
 Etymology 

 1.3 
 Pronunciation 

 Etymology
 [ edit ] 

 From مه ( mah ) + تاب ( tâb ) . Compare Northern Kurdish taveheyv .

=== ebed09d603c2b47a 4944
 Etymology 

 1.2 
 Noun 

 Etymology 

 2.3 
 Pronunciation 

 Etymology
 [ edit ] 

 Borrowed from Classical Persian پرتو ( partaw ) .

=== d73bf394998a3735 3248
 Etymology 

 1.3 
 Pronunciation 

 Etymology
 [ edit ] 

 Inherited from Middle Persian awištāftan > ōštāftan .

=== e8bd2defa3d0e716 131
```


## [2026-10-15T02:46:36.120Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 3c0babba0e34bb38 350dd9b8a87fe440 5fafb5208b258fdd 948d2d1ce1d3354a ebed09d603c2b47a 24b0a25c595f14af; do echo \"=== $f\"; grep -A3 \"^ *Etymology.*$\" $f.txt | grep -v \"^ *\\[ edit\\|^--\\|^ *$\\|^ *Etymology\\|Pronunciation\\|^ *[0-9.]* *$\\|Noun\\|Adjective\\|Verb\" | cut -c1-600 | head -8; done; head -c 300 2a47e565f5f908db.txt"
}
```


### [2026-10-15T02:46:36.766Z] TOOL RESULT

```
=== 3c0babba0e34bb38
 Alternative forms 
 Borrowed from Pashto تنگ or Urdu تنگ , from Persian تنگ .
 Inherited from Middle Persian [script needed] ( tng /⁠tang⁠/ , “ narrow, tight ” ) , in turn inherited from Proto-Indo-European *tenk- ( “ to compact ” ) , [ 1 ] perhaps from *ten- ( “ to stretch ” ) . Cognate with تنجیدن ( tanjīdan , “ to squeeze ” ) , as well as Old Armenian թանկ ( tʻank ) , an Iranian borrowing.
 Via Chagatai from Chinese 桶 ( MC thuwngX | duwngX , “tub, keg”)
 Via Chagatai from Chinese 等 ( MC tojX | tongX , “equal; sort, type, etc. ”), or specifically 戥 (“small steelyard for weighing money and similar items”).
 From Sanskrit [Term?] .
 Borrowed from Classical Persian تنگ ( tang ) .
=== 350dd9b8a87fe440
 Borrowed from Classical Persian رستم ( rustam ) .
 Proto-Indo-European *ser- ? 
 Proto-Indo-European *srew- der. 
 Borrowed from Classical Persian رُسْتَم ( rustam ) , from Middle Persian lwtsthm ( /⁠rōdstahm⁠/ ) , from lwd ( /⁠rōd⁠/ , “ river ” ) + stʾhmb ( /⁠stahm⁠/ , “ force, power ” ) .
=== 5fafb5208b258fdd
 Root 
 From Middle Persian [Book Pahlavi needed] ( tp /⁠tab⁠/ , “ fever ” ) , ultimately from Proto-Indo-European *tépos ( “ heat, warmth ” ) . Related to Sanskrit तपस् ( tapas ) , and Old Armenian տապ ( tap , “ heat ” ) , an Iranian borrowing.
 From Sanskrit त ( ta , “ this ; that ” ) + एवम् एव ( evam eva , “ just so ” ) .
=== 948d2d1ce1d3354a
 Borrowed from Classical Persian آفْتَاب ( āftāb ) 
 Borrowed from Classical Persian آفْتَاب ( āftāb ) .
 Borrowed from Classical Persian آفتاب ( āftāb ) .
 From Middle Persian 𐭠𐭯𐭲𐭠𐭡 ( ʾptʾb /⁠āftāb⁠/ , “ sunshine ” ) (compare 𐮀𐮎𐮃𐮀𐮁 ( ʾpdʾb /⁠ābdāb⁠/ ) ), from Proto-Iranian *abi-tāpáh [ 1 ] Equivalent to آف ( âf ) +‎ تاب ( tâb ) .
 Borrowed from Classical Persian آفْتَاب ( āftāb ) . First attested in c. 1635 as Middle Hindi آفتاب ( āftab /⁠ãftāb⁠/ ) . [ 1 ] 
=== ebed09d603c2b47a
 Borrowed from Classical Persian پرتو ( partaw ) .
 The second part is ultimately from Proto-Indo-European *tep- . Related to Persian تفت ( “ heat, warmth ” ) , Persian آفتاب ( “ sun, sunshine ” ) , etc.
=== 24b0a25c595f14af
URL: https://en.wiktionary.org/wiki/تهمتن
FETCHED: 2026-10-12T18:40:53Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-10-15T02:46:40.188Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -o -i \".\\{300\\}staxma.\\{300\\}\\|.\\{300\\}rōdastahm.\\{200\\}\\|.\\{200\\}Raoda.\\{300\\}\" aa8a19425de336a5.txt | head -4; echo; grep -o -i \".\\{300\\}urupi.\\{300\\}\" f508f16256c72792.txt | head -3; head -c 400 f508f16256c72792.txt"
}
```


### [2026-10-15T02:46:40.747Z] TOOL RESULT

```
URL: https://www.iranicaonline.org/articles/tahmuras
FETCHED: 2026-10-15T02:46:28Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-10-15T02:46:42.642Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; head -c 300 aa8a19425de336a5.txt; grep -o -i \".\\{200\\}etymolog.\\{300\\}\\|.\\{200\\}name .\\{300\\}\" aa8a19425de336a5.txt | head -3"
}
```


### [2026-10-15T02:46:43.030Z] TOOL RESULT

```
URL: https://www.iranicaonline.org/articles/rostam-1
FETCHED: 2026-10-15T02:46:25Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-10-15T02:46:46.589Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://www.iranicaonline.org/articles/rostam-legendary-hero\" \"https://www.iranicaonline.org/articles/tahmurat\" \"https://en.wikipedia.org/wiki/Tahmuras\" \"https://en.wikipedia.org/wiki/Rostam\" \"https://en.wiktionary.org/wiki/تهمتن\"; do echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 503, Tenk: Tahmuras/Rostam names\" 2>&1|tail -1; done"
}
```


### [2026-10-15T02:46:53.711Z] TOOL RESULT

```
== https://www.iranicaonline.org/articles/rostam-legendary-hero
/home/sfmqrb/git/rishe-private/data/verification/sources/web/eb7e9712e6937cd3.txt
== https://www.iranicaonline.org/articles/tahmurat
/home/sfmqrb/git/rishe-private/data/verification/sources/web/70d637db2c570b60.txt
== https://en.wikipedia.org/wiki/Tahmuras
/home/sfmqrb/git/rishe-private/data/verification/sources/web/39c83e2ab7a227c7.txt
== https://en.wikipedia.org/wiki/Rostam
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6f59c16e0f15c692.txt
== https://en.wiktionary.org/wiki/تهمتن
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2a47e565f5f908db.txt
```


## [2026-10-15T02:46:56.102Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in eb7e9712e6937cd3 70d637db2c570b60 39c83e2ab7a227c7 6f59c16e0f15c692; do echo \"== $f\"; sed -n 3p $f.txt; grep -o -i \".\\{250\\}\\(staxm\\|taxma\\|urupi\\|Raod\\|Rōd\\).\\{300\\}\" $f.txt | head -3; done"
}
```


### [2026-10-15T02:46:56.629Z] TOOL RESULT

```
== eb7e9712e6937cd3
STATUS: -1
== 70d637db2c570b60
STATUS: -1
== 39c83e2ab7a227c7
STATUS: 200
sode is set by the account in the Avesta of the reign of Taxma Urupi, which relates that this sovereign of the world subdued not only demons and sorcerers, but also the archfiend Angra Mainyu himself, thanks to the help of the wind god Vayu and his (Taxma Urupi's) possession of the khvarenah or mystic 'kingly glory'. Thus empowered, the valiant king is able to ride Angra Mainyu, like a horse, 'from one end of the earth to the other', every day for thirty years. (At this point the Avesta falls silent and the Parsi rivayât takes up the story). Ahriman
== 6f59c16e0f15c692
STATUS: 200
```


## [2026-10-15T02:46:59.037Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -o -i \".\\{100\\}\\(etymolog\\|name\\b\\).\\{400\\}\" 39c83e2ab7a227c7.txt | head -3; echo ===; grep -o -i \".\\{100\\}\\(etymolog\\|stahm\\|Rōd\\|Rotastahm\\).\\{400\\}\" 6f59c16e0f15c692.txt | head -4"
}
```


### [2026-10-15T02:46:59.401Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-10-15T02:47:01.287Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -o -i \".\\{100\\}etymolog.\\{400\\}\" 39c83e2ab7a227c7.txt | head -3; echo \"-----\"; grep -o -i \".\\{100\\}\\(etymolog\\|stahm\\|Rotastahm\\).\\{400\\}\" 6f59c16e0f15c692.txt | head -4"
}
```


### [2026-10-15T02:47:02.064Z] TOOL RESULT

```
-----
```


## [2026-10-15T02:47:04.327Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -o -i \".\\{200\\}\\(Taxma\\|Tahm\\).\\{200\\}\" 39c83e2ab7a227c7.txt | head -3; echo \"-----\"; grep -o -i \".\\{200\\}\\(Avest\\|Middle Persian\\|name\\).\\{250\\}\" 6f59c16e0f15c692.txt | head -5"
}
```


### [2026-10-15T02:47:04.795Z] TOOL RESULT

```
e div s (demons) of Ahriman . On the advice of his vizier Shahrasp , Tahmures used magic to subdue Ahriman and made him his slave, even riding upon his back as on a horse. The demons rebelled against Tahmuras, and he made war against them with both magic and force. By magic he bound two-thirds of the demons; the remaining third he crushed with his mace. The div s now became Tahmuras's slaves and they 
ign of Taxma Urupi, which relates that this sovereign of the world subdued not only demons and sorcerers, but also the archfiend Angra Mainyu himself, thanks to the help of the wind god Vayu and his (Taxma Urupi's) possession of the khvarenah or mystic 'kingly glory'. Thus empowered, the valiant king is able to ride Angra Mainyu, like a horse, 'from one end of the earth to the other', every day for thi
e founder of the Sabian religion, "Boudasf" lived during Tahmuras's reign, [ 6 ] while Al-Tabari reports that Tahmuras reigned for 40 years, and was obedient to Allah , who had given so much power to Tahmuras that Iblis was submissive to him, and that he was the first ruler of Babylon . He also reports that Tahmuras jumped on Iblis's back and rode him around the world, and that "Bewarasb" (better know
-----
 otherwise leave blank -->"},"alt":{"wt":"<!-- descriptive text for use by speech synthesis (text-to-speech) software -->"},"caption":{"wt":"Rostam killing the [[White Div]] from the [[Baysunghur Shahnameh]] (1430 AD)"},"native_name":{"wt":"رستم"},"native_name_lang":{"wt":"fa"},"pronunciation":{"wt":""},"birth_name":{"wt":"<!-- only use if different from name -->"},"birth_date":{"wt":"<!-- {{Birth date and age|YYYY|MM|DD}} for living people supply on
ve died, use {{Birth date|YYYY|MM|DD}}. -->"},"birth_place":{"wt":"[[Zabulistan]] (present-day [[Zabul province|Zabul]], [[Afghanistan]])<ref>{{Cite web|url=https://www.bl.uk/learning/cult/inside/shahnamestories/storyfour/birthofrostam.html|title=Rostam life story explained based on Shahname Book|access-date=10 January 2023|archive-date=26 March 2023|archive-url=https://web.archive.org/web/20230326024530/https://www.bl.uk/learning/cult/inside/shahnam
lace_coordinates (displays \"Burial place\" as label) -->"},"burial_coordinates":{"wt":"<!-- {{coord|LAT|LONG|type:landmark|display=inline}} -->"},"monuments":{"wt":""},"nationality":{"wt":""},"other_names":{"wt":"Rustam<br>Rustem"},"siglum":{"wt":""},"citizenship":{"wt":""},"education":{"wt":""},"alma_mater":{"wt":""},"occupation":{"wt":""},"years_active":{"wt":""},"era":{"wt":""},"employer":{"wt":""},"organization":{"wt":""},"agent":{"wt":"<!-- Dis
"},"notable_works":{"wt":"<!-- produces label \"Notable work\"; may be overridden by |credits=, which produces label \"Notable credit(s)\"; or by |works=, which produces label \"Works\"; or by |label_name=, which produces label \"Label(s)\" -->"},"style":{"wt":""},"net_worth":{"wt":"<!-- Net worth should be supported with a citation from a reliable source -->"},"height":{"wt":"<!-- \"X cm\", \"X m\" or \"X ft Y in\" plus optional reference (conversio
":"<!-- Criminality parameters should be supported with citations from reliable sources -->"},"criminal_penalty":{"wt":""},"criminal_status":{"wt":""},"spouse":{"wt":"<!-- Use article title or common name -->[[Tahmina]]"},"partner":{"wt":"<!-- (unmarried long-term partner) -->"},"children":{"wt":"[[Sohrab]]<br>[[Faramarz]]<br>[[Siyâvash]] (adopted son)<br>[[Banu Goshasp]] (In [[Banu Goshasp Nama]])"},"parents":{"wt":"<!-- overrides mother and father
```


## [2026-10-15T02:47:12.013Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in e433c94b0a7a1899 834fab871b95838e 4c340697ef7d78ca 7ec6fec08384222f; do echo \"== $f\"; sed -n 3p $f.txt; grep -o -i \".\\{0\\}\\(from Old Norse\\|Proto-Germanic\\|from Latin\\|PIE root\\).\\{300\\}\" $f.txt | head -3; done; for f in f1292d129a579357 66888b0a62be5831; do echo \"== $f\"; grep -i -A30 \"Derived terms\\|Descendants\" $f.txt | grep -i \"iranian\\|germanic\\|latin\\|tepid\\|tang\\|tight\\|tahm\\|tax\" | head -15; done"
}
```


### [2026-10-15T02:47:12.503Z] TOOL RESULT

```
== e433c94b0a7a1899
STATUS: -1
== 834fab871b95838e
STATUS: -1
== 4c340697ef7d78ca
STATUS: -1
== 7ec6fec08384222f
STATUS: -1
== f1292d129a579357
== 66888b0a62be5831
 Proto-Indo-Iranian: *tápati ( see there for further descendants )
 Proto-Germanic: *þebōną ( see there for further descendants )
 *tep-sḱé-ti ( inchoative ) [ 1 ] ( or created in Proto-Iranian ) 
 Proto-Indo-Iranian: *tapsćáti 
 Proto-Iranian: *tafšáti 
 Proto-Indo-Iranian: *Hátāpst 
 Proto-Indo-Iranian: *taptás ( “ warmed, heated, hot ” ) ( see there for further descendants )
 ↑ 2.0 2.1 2.2 De Vaan, Michiel ( 2008 ), “ tepeō ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 614
```


## [2026-10-15T02:47:15.947Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 3p f1292d129a579357.txt; for f in 3a54efe485515277 6c3c6c21eb6f12d2 e9f1a3676752016d 3a8e70a3b9ca6c60; do echo \"== $f\"; grep -A3 \"^ *Etymology\" $f.txt | grep -v \"^ *\\[ edit\\|^--\\|^ *$\\|^ *Etymology\\|Pronunciation\\|^ *[0-9.]* *$\\|Noun\\|Adjective\\|Verb\" | cut -c1-500 | head -3; done"
}
```


### [2026-10-15T02:47:16.329Z] TOOL RESULT

```
STATUS: -1
== 3a54efe485515277
 From Middle English tight , tyght , tyȝt , tiht , variants of thight , thiht , from Old English *þiht , *þīht (attested in meteþiht ), from Proto-West Germanic *þį̄ht(ī) , from Proto-Germanic *þinhtaz , from Proto-Indo-European *tenkt- ( “ dense, thick, tight ” ) , from Proto-Indo-European *ten- ( “ to stretch, pull ” ) .
 From Middle English tighten , thyhten ( “ to make tight ” ) ; see tighten .
 From English tight . Doublet of tæt .
== 6c3c6c21eb6f12d2
 From Middle English tanglen , probably of North Germanic origin, compare Swedish taggla ( “ to disorder ” ) , Old Norse þǫngull , þang ( “ tangle; seaweed ” ) , see Etymology 2 below.
 Of North Germanic origin, such as Danish tang or Swedish tång , from Old Norse þongull, þang . See also Norwegian tongul , Faroese tongul , Icelandic þöngull .
== e9f1a3676752016d
 From Middle English thikke , from Old English þicce ( “ thick, dense ” ) , from Proto-West Germanic *þikkwī , from Proto-Germanic *þekuz ( “ thick ” ) , from Proto-Indo-European *tégus ( “ thick ” ) .
== 3a8e70a3b9ca6c60
 Proto-Indo-European *tep-
```


## [2026-10-15T02:47:18.888Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -o \"From Middle English tepide.\\{0,300\\}\\|from Latin tepidus.\\{0,200\\}\\|From Latin tepidus.\\{0,200\\}\" 3a8e70a3b9ca6c60.txt | head -2; grep -o \".\\{0,40\\}Sogdian.\\{0,200\\}\" 66888b0a62be5831.txt 5fafb5208b258fdd.txt | head"
}
```


### [2026-10-15T02:47:23.132Z] TOOL RESULT

```
from Latin tepidus . Cognate with Sanskrit तप् ( tap ) , Proto-Slavic *teplъ .
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,200}
                        \___exceeds complexity limits
```


## [2026-10-15T02:47:25.850Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"'tp'k\\|’tp’k\\|ʾtpʾk\\|'tp\\\"k\\|^ *1[0-9][0-9] '\\|'tpk\" SOD_pages.txt | head; grep -n -i \"heat\" SOD_pages.txt | head -20"
}
```


### [2026-10-15T02:47:27.009Z] TOOL RESULT

```
4604:     279 »s,m-     B                                                    heat ?
15566:                                                                              wheat
15876:         heat
28190:                                                                          BSTi 259;heathen
38519:heat 291, 4263                        high in rank      1547                  horse covering   1623
38520:heathen 8497                          him     1792, 1845, 2030, 3373, 9146,   horse killing  1670
39844:virtuous    9438                        water     190, 207, 215, 450, 1247      wheat    4162
```


## [2026-10-15T02:47:28.893Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *291 \\|  291 \" SOD_pages.txt | head; grep -n \"^ *4263 \\| 4263 \" SOD_pages.txt | head -3"
}
```


### [2026-10-15T02:47:30.047Z] TOOL RESULT

```
4601:          TSP 7.143, 14.ii, n p214; BSTBL, Padm. 56; GMS           291 »tp>k    B                                          u/
45241:291      atpak                   atapak                                                           -                           3243
15874: 4263 yrmyh       B                                     u/     4275 yryn-1 C                                       j.u>
38519:heat 291, 4263                        high in rank      1547                  horse covering   1623
```


## [2026-10-15T02:47:32.083Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4590,4615p SOD_pages.txt; awk 'NR<4601 && /\\[pdf page/ {p=$0} END{}; NR==4601{print p}' SOD_pages.txt; grep -n \"pdf page\" SOD_pages.txt | awk -F: '$1<4601' | tail -1"
}
```


### [2026-10-15T02:47:32.817Z] TOOL RESULT

```
         burned
                                                                        may be
          Hen. LW      103
                                                                        SCE 186; GMS 767
     275 »Swk ** *s»wk>                                            289 »t*r => n»rh
     276 "swr =» 's'wr
                                                                   290 »t*rh                             (J>>>^jj)j^<>-7
     277 "swr'n =» "s'wr                                                atar (Hr, "t'r, Mrh) ©ob. -y      =^tr
     278 »S»k(w) B                                       j^S^           fire
         ase ('s'y) ©Av. atrya <*a0raka                                 GMS 4, 943; TSP; SCE 78, 168; BSTBL; BBB;
         ashes                                                            MSP; STii 4.27
          TSP 7.143, 14.ii, n p214; BSTBL, Padm. 56; GMS           291 »tp>k    B                                          u/
            299
                                                                        atpak ©<*a-tdpaka-, Av. a-tapaite        =»>ntp
     279 »s,m-     B                                                    heat ?
                                                 &jijj <oJ*>&i
         asam     ©Av. sam~                                             S W, IIJ 1976, 69, Frag. 24.1; C2 pl77.18
          (to)drink, (ro)swallow
                                                                   292 »tr =» 't'rh
          TSP 2.461 pi 75
                                                                   293 »tr »wst- M                (o*U j^ h Jz1)qjXx jS\
     280 »s,m,kk S                                         eXjJL       atar ost
         asame/ak
          swallowing                                                    (rc)extinguish, (fo)lay a fire
          Sund. MHC     p25                                            Sund. Man. Lett. 305.23, 313
```


## [2026-10-15T02:47:36.829Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;print(json.dumps(json.load(open('refs_online.json'))['BQT'],ensure_ascii=False)[:3000])\""
}
```


### [2026-10-15T02:47:38.089Z] TOOL RESULT

```
{"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt", "/home/sfmqrb/git/rishe-pr
```


## [2026-10-15T02:47:40.619Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 511 491 519 538; do echo \"######## BQT:$p\"; timeout 300 python3 tools/ref_page.py BQT:$p 2>&1 | head -c 2500; echo; done"
}
```


### [2026-10-15T02:47:41.220Z] TOOL RESULT

```
######## BQT:511
no scan of BQT covers printed page 511 (see 'scans' in refs_online.json)

######## BQT:491
no scan of BQT covers printed page 491 (see 'scans' in refs_online.json)

######## BQT:519
no scan of BQT covers printed page 519 (see 'scans' in refs_online.json)

######## BQT:538
no scan of BQT covers printed page 538 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:47:44.211Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"pdf page\" BQT_v1_pages.txt | head -3; for w in \"تنجیدن\" \"تهمتن\" \"تهمورث\" \"تهمورس\" \"تب \" \"تپیدن\" \"تابستان\" \"تابیدن\" \"آفتاب\" \"پرتو\"; do echo \"== $w\"; grep -n \"$w\" BQT_v1_pages.txt | head -4 | cut -c1-200; done"
}
```


### [2026-10-15T02:47:44.848Z] TOOL RESULT

```
== تنجیدن
17505:اعر است به‌بتنجیدن » نی درهم بیج و بفثار
30956:۵ رگ : تسین . ۹ - تنجیدن بمعنی کشیدن و بسن و آشامیدن , اوستا
30958:*- اسم مفعول از تنجیدن.
31095:وخی ۷28 .سریکلی 008) « اسشق ۳۹۸ * «صینا .4۲:۱4٩‏ بمنی آنرا ازرشة تنجیدن(«.م)ه
== تهمتن
31994:عدیل و نظیر نداشته باشد ۰ و تهمتن مر کب
31997:تهمتن* » با ای فرشت بر وزن
32015:۴ - تهمتن بخندید کورا بدید
32016:٩‏ -کنون ای‌تهمتن تو در کار من
== تهمورث
32031:که او وا تهمورث دیو ند می خوانند؟ ت ورنفی
32059:۵ تهمورث - رك : نهمورسی .
== تهمورس
== تب 
345:آثار فراوان سانسکریت از کتب دینی و داستانی و دانگی پشتیبان
384:سبب دیگری که از ذخرء هنگفت کتب پهلوی روز گار ساسانیان‌بی بهپره
550:چند نام و چند کلمه از زبان مادی بوسیلهٌ کتب یونانی و یره بما
898:ز بان ازحیطة ز بانهای ایرانی‌خارج‌است. ولی گاه در کتب اسلامی نامز بان
== تپیدن
28827:از تپیدن . رکه: ثابا که .
28873:مصدد از. تپیدن. هتفرن از
== تابستان
11799:کلسنان » بوستان » کوهستان ء بلوچنان » هندوستان وصررت بوند زمان درتابستان و زمستان
16359:تابستانی باشد ۸ .
24373:است که خابهٌ تابستانی باشد .
28716:درحجه حرارت تابستانی‌در امردادهاه ۷ وحدافل درزستان ۱۵ درجه است. رك: جفرافای سباسی.
== تابیدن
28033:ه تابان اسم فاعل‌از تابیدن, درخشان» منور. معرب آن‌نیزتابان." «دزیج ۱ص ۱۳*.وجام و شیلةٌ آلوان کنند وگاهی خالی گذارند .
== آفتاب
1205:«چون لغت عبری وسریانی وپهلوی تا بایام طلوع آفتاب دین عر ی
1422:سیوندی نیزاز نظار علم اصوات منفرد است ( 0۲] (خورء آفتاب) »
4164:آت شگردان ۰ آرواره » آفتاب گردان ۰ آفتا به» آقا.ابزار» از گیل
6084:بیمنی ابریق و آفتابه و مطهرء ومانند آن
== پرتو
317:در اینجا باید بیفز اييم از پرتو سانسکر بت کمتر لفت
9351:که پرتو ماه باشد -
24007:ومخف پرتو حم ی 6۵ .
24285:وشماع و پرتو را هم کنته‌اند؟ - و دامن و کناره
```


## [2026-10-15T02:47:46.382Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 30940,30962p BQT_v1_pages.txt; echo ----; sed -n 31985,32065p BQT_v1_pages.txt"
}
```


### [2026-10-15T02:47:46.830Z] TOOL RESULT

```
قنج۸ ه بفتم اول بر وزن رنج » سنعنی
درهم پیچیدن و فراهم فشردن باشد - و بمعنی
از پی درآمدن و فراهم نشاندن هم هست. و هر
فاعل را نیز گویند که بحسنده و فشارنده واز ی
درآ ینده باشد - و امر ببایئمعنی هم هست یمنی
در یچ و بفثر واز پی‌دزآری - و ی گوبند
تنج بمعنی از پی در آمده وترئج بممئی فشارنده
باشد » ویکسر اول نیز گفته‌انث .
نان «٩‏ بر وزن رنبیدن " بسنی
ببحیدن ر نس فشر دن باشد .
لنحید ه* احه بر وزن سنجیده » بمعنی
ترنجیده است که درهم کشیده شده و فشارده
کردیده وپیچیده باشد.
۱رد : تملیت  .‏ ۴ - طنبور معرب از اسپایابی 30۲اتقاند , 2۳000۲)
(فرانه ۳0۱۳۵۵۷0۲ه۱) «دزی؛ ص۱۵۳*. .۰ ۴ -رگ: تبول.. ‏ #رکه: تنبك. ۵ رکه:
نیو که . ٩‏ -- رکه تنمك‌و :نیو کك. ۷ جزو اول آن‌تن (نبدن). ره: تنسته.
۵ رگ : تسین . ۹ - تنجیدن بمعنی کشیدن و بسن و آشامیدن , اوستا
رت اب
*- اسم مفعول از تنجیدن.
تر تجید وار گن ننگه تنگه .
«لفت فرس ۹٩۹‏ ور که ۰*۵زند ۱ - چم اول و سکون انی و دال
سوق نت کا مرلین مامت ردر چم
که از جای برجهد و جهنده باشد . و خشم -
----
فه غربالی -کنابه از دانهای کوچك
وتخالهٌ هرچیز باشد .
تهاث - بر وزن نمك » خاك راگویند
و بعربی نراب خوانند - و بمعنی‌تهی‌وخالی ۷ -
وبرهته و عربان هم هت .
تهم ۴ بفتح اول و ثانی وسکون‌هيم,
شخصی را گویند که در بزرکی جله و ت کیب
وقد وقامت وشجاعت ومردی و دلیری و دلاوری
۳ای ح
عدیل و نظیر نداشته باشد ۰ و تهمتن مر کب
ازین است » وبسکون ثانی هم باين معنی‌آمده
است .
تهمتن* » با ای فرشت بر وزن
فلمزن , یکی از القاب رستم زال ۴ و بهمن ۵
است - و مردم فوی جثه و شجاع بی نظیر را
نیز کوبند » چه‌معنی تر کیبی این‌لفت بی‌همتاتن
است ۱ ععنی‌ننی که عدیل ونظیر نداشته باشد
و بم‌نی سپهدار ولشکر کش وخداوند سیاه هم
هست - وبند کی و فرمان برداری کردنرا نیز
و
ای زهر مردمی تهی ونهك
مردمان تزد توچرا پابد(باد. دحخدا).
بوشکور بلخی, «لفت فری ۲۵۷*.
«اسشق ۶۰۵ :
کرا بخت وشمیشر ودینار باشد
وبالا وتن نهم ونسبت کیانی. دقیفی‌طوسی.
«لت فری۳۳۸».
هم همست در بهلوانی زبان
بمردی فزرن ز اژدهای دمان .
«یشنها ۲ ص۱۳۹ ».
۴ - تهمتن بخندید کورا بدید
٩‏ -کنون ای‌تهمتن تو در کار من
یکی تیغ تیز ازه‌یان بر کشد .
فردوسی طوسی. *لغت‌فرس ۳۳۸*.
نگه کن بآزار و کردار من.
فردوسی طوسی» گفتار رستم باسفندیار .
و کوبروارمفرب بقزوین وساوهطول آن ازهشرق‌بمغزب (غر قآ باد تا فدروژ کوه) ۲۹۰ وعرض‌ازشمال
بجنوب (ا زگردنة کندوان تا درباچهُ ق) *۱۲ کیلومتر و صساحت آن فربب ۳۱۰۰۰ کیلو متر
مربع است. شهرتهران پابئخت ابران دربن ابالت است. درفدیم نهران عکیاز فربه‌ه‌ای کوچكری
بوده» اصطخری وابن‌حوفل ومسمودی نام‌تهران را در کتب خود ذ کر کرده‌اند. «جقرافای سیاسی .
کیهان ۳۱۱- ۳۹۹. درسال ۱۲۱۰ آغا محمدخال قاجار آنرا باشخت ابران فرارداد . جمیت
نپران قوب ۱۰۰۰۰۰۰ نن است. راجم‌بوجه اشتفاق نهران وسور مختلف تلفظ و کتابت آن» رك:
بقبه درصفحةٌ ۰۳۹تهمك - بر وزن لك لك , مصفر تهم
اسق بت و بمعنی دویم تهك ‌‌ حست که برهنه
وعربان - وتهی وخالی باشدا .<
بهمو درس - بنتح اول نامشخصی است
که او وا تهمورث دیو ند می خوانند؟ ت ورنفی
تهمیشه » بر وزن اندیشه . نام
پشته است در دارالم‌رز نزديك‌به بشه نارون؟ .
هو - منم اول و نانی » بروزنوهعنی
تفواست که آب دهن - وآب دهن انداخثن باشد
ویک اول مخمقف تسهواست ۹ وآن برنده‌است
خبیه بکيك. ایک نکوچکتراست از کیال
4 و بالا » بیمنی زیر و زبرباشد که
تحت و فوق است - و کنابه از اضطراب
و وف تپك رتپيك (ذیل: نهی).
وبیتراری هم ست وحصول مطلس دو سرامرد
باق فزکلاسک وا
ی - بکسر اول و نانی و سکون
تحتانی نام شپری و مدینه است* - و یمعنی
خالی۷ هم‌هست که در مقابل پراست۸ » و باین
معنی بفتح اول وضم اول هم گفنه‌اند .
بهیته - بر وزن همشه , نام شهری
است که فربدرن پوسنه و دام جر آنجا
می بوده . ۱
نهیگاه - ما ین شکم وپهلو را کویند.
تهی و تهاكث ۰ با ای فرشت و ها
بروزن زمی و فلكث» این‌لفت ازاتباع است بمعنی
برهنه و عربان - وتهی وخالی ۰
۴ در اوستا ۱۲۷۳2 31100[ ؛ جزو
سفق نمعدی يك فسم -ت.
زب
۵ سرله: نهو.
ا ورف *سشق ۰ ۰
۵ تهمورث - رك : نهمورسی .
شه ارصفحه ۵۳۸
نامهای شپرها ودبه‌های ابران. احمد
(بدون‌نام نوسن ») .مجلهٌکاوه دور جدید سالدوم شمارء۷ صی۱۱-۸؛ طهران.عسمد قزوشی.مجلةً
کاوه دور جدید. سال‌دوم شمار #ص۱۵-۱4؛ طهران با تهران؟ سمید نفیسی. محله آشده سال
دوم شمارء 4۰۷۰۱قی ۱ ع یکسر اول و سکون ثالی :
مخفف تهی است که خالی باشد .
```


## [2026-10-15T02:47:51.926Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 30956 31997 32059; do head -n $n BQT_v1_pages.txt | tr -cd '\\f' | wc -c; done; grep -n \"تنگ\" BQT_v1_pages.txt | sed -n 1,400p | grep -n \"^[0-9]*:تنگ\\|تنگ -\\|تنگ۱\\|تنگ ۱\" | head"
}
```


### [2026-10-15T02:47:52.293Z] TOOL RESULT

```
744
766
767
39:31119:تنگا » بااف بر وزن اغیار. داروبی
40:31128:تنگ پاز » بر وذن زنگبار » نامی
42:31159:تنگه ر کان - نام مونمی است از
43:31161:تنگ چشم - کنابه از مردم بخیل
44:31165:تنگ دست » با دال ابجد بو رزن
45:31181:تنگ دوی» نم ثانی » کنابه از شهرت . دی
47:31190:تنگ‌سار ؟ » بر وزت منگه مار »
57:31265:تنگه » بفتم اول و ثالث و سکون
58:31268:تنگه بقراه کنابه از بر کهفراست
59:31269:تنگ یاب ب با بای حطی بر وزن
```


## [2026-10-15T02:47:57.828Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 745 767 768; do echo \"== leaf $((n-1))\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -4; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -o \"[۰-۹]\\{3\\}\" | head -5 | tr '\\n' ' '; echo; done"
}
```


### [2026-10-15T02:47:58.631Z] TOOL RESULT

```
== leaf 744
تنیلیت۱ عبا تای فرشت درآخر بر وزن
عندلیب , بارکوچکی را گویند که بربار بز رکه
بندند و گاه بربالای چاروا نهند و بر بالای آن
موار شوند - ویك لنکه بار را نیز کنته‌اند.
۱۳۵ ۱۵۳ 
== leaf 766
بر وزن نرسا . شبره گرفتن از انگور را
کوند . *
فه غربالی -کنابه از دانهای کوچك
وتخالهٌ هرچیز باشد .
۲۵۷ ۶۰۵ ۳۳۸ ۱۳۹ ۳۳۸ 
== leaf 767
تهمك - بر وزن لك لك , مصفر تهم
اسق بت و بمعنی دویم تهك ‌‌ حست که برهنه
وعربان - وتهی وخالی باشدا .<
بهمو درس - بنتح اول نامشخصی است
۱۲۷ ۵۳۸ ۰۷۰
```


## [2026-10-15T02:48:00.979Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))['BQT'];print({k:v for k,v in d.items() if k not in('title','url','lookup_hint','local_file')})\" | head -c 2500"
}
```


### [2026-10-15T02:48:01.417Z] TOOL RESULT

```
{'kind': 'archive_djvu+local_scan_ocr', 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'covers_etymology': True, 'notes': "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N
```


## [2026-10-15T02:48:05.667Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 31119 31265; do head -n $n BQT_v1_pages.txt | tr -cd '\\f' | wc -c; done; for L in 719 739 747; do echo \"== leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -E \"^.{2,14} [-»*،]|بفتح|بر وزن\" | head -8 | cut -c1-80; done"
}
```


### [2026-10-15T02:48:06.226Z] TOOL RESULT

```
748
751
== leaf 719
تر نحان » جْم اول . معرب ترنگان
تر نج مه ر گان - ببعنی ترج زد
فر فيك » بروزن‌غرابید»ماضی نرنجیدن
تر نحیدن؟ جنم اول وئالی بر وزن
غرنسدن » بمعنی مخت درهم کشیده و کوفته
شدن - و چن بهم رسانیدن و درشت گردبدن
باشد » و بفتح اول و ثانی همآمده است .
فر نجیده ز بر وزن غرنبیده» بمعنی
== leaf 739
قم ع بفتح اول دسکون ثانی ۰ آفنی
تماجح نم اول بر وزن اعاج ۰
تماخره - بتح اول وخای نقطه‌دار
و ظرافت باشد - و بسکون خای نقطه دار هم
تهساشا؟ - با دار اف کنیده
آمام شدن - بسی باهبا رسیدن
کاری باشد - و کنابه از مردن و فوت شدن‌هم
بندند؟ - و یکسر هردو فوقانی بحربی سماقی را
== leaf 747
کننه - ودوالی که بدان‌بار بر پشت باربردار(۱)
محکم سازند - ودره اکویراهم گفته‌اند۴ - ونایاب
بدخشان - و تلم مقامی باشد از تر کستان که
لی‌شوی » نم شین شقطه دار بروزن
کونند عموماً - و تخته ای که میت را بر بالای
تنقظاد -_بنم اول وفاف و طای‌حلی
بالف کشیده بر وزن پرخمار » پاسبان‌را گویند -
تا صباح بسوزد , وبر وزن توالفقار و بردبار حم
```


## [2026-10-15T02:48:10.244Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==720' BQT_v1_pages.txt | grep -n \"اوستا\\|پهلوی\\|[a-z]\\{3,\\}\\|ترنج\\|رك\" | head -20; echo =====; awk 'BEGIN{RS=\"\\f\"} NR==749' BQT_v1_pages.txt | grep -n \"تنگ\\|اوستا\\|پهلوی\\|[a-z]\\{3,\\}\" | head -20"
}
```


### [2026-10-15T02:48:10.810Z] TOOL RESULT

```
Exit code 1
20:کوچك و کم پرواز و متحرك و خوانشده که اور
28:۱ -رک: ترنجیدن.
34:هم‌آمده است - و فوقاب را نی زگفتهامد - وتاركد
48:و ترنجان ممرب آست » و آترا بعربی حفرح
62:۲ - درگیلکی ۵۲۵98 , رك: نذرو.
(eval):1: ==== not found
```


## [2026-10-15T02:48:13.995Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"ترنجیدن\\|تر نجیدن\" BQT_v1_pages.txt | head; grep -n \"تنگ ۱\\|تنگ - \\|تنگ » \\|تنگ؟\\|^تنگ\" BQT_v1_pages.txt | head"
}
```


### [2026-10-15T02:48:14.354Z] TOOL RESULT

```
29804:۱ -رک: ترنجیدن.
31119:تنگا » بااف بر وزن اغیار. داروبی
31128:تنگ پاز » بر وذن زنگبار » نامی
31159:تنگه ر کان - نام مونمی است از
31161:تنگ چشم - کنابه از مردم بخیل
31165:تنگ دست » با دال ابجد بو رزن
31181:تنگ دوی» نم ثانی » کنابه از شهرت . دی
31190:تنگ‌سار ؟ » بر وزت منگه مار »
31265:تنگه » بفتم اول و ثالث و سکون
31268:تنگه بقراه کنابه از بر کهفراست
31269:تنگ یاب ب با بای حطی بر وزن
```


## [2026-10-15T02:48:16.331Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 31060,31118p BQT_v1_pages.txt | grep -n \"تنگ\\|اوستا\\|پهلو\\|tang\\|tanc\" | head; sed -n 31080,31100p BQT_v1_pages.txt"
}
```


### [2026-10-15T02:48:16.777Z] TOOL RESULT

```
34:۱ - اوستاه)نأکفی(20)8) (سفت عالی‌از 140۳08 بمعنی‌نمم وببر ومند)» پپلوی 808
38:کردی 208 ,061208 (مبان کمربند وتنگ)؛ استی 8750088 (شک‌بند) .افنانی 18-۵08
40:۴ در این بلاد فزون دارد از هزار کلات بهريك ادر دبنار تنگها برتشگه .
42:۴ ر4: ارتنگه : ۱
45:9 رکفث: تنگه ت رکان.
58:کوز؛ سرتنگه کرد ن کوتاءه راکگویند - و بکس
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
۴ در این بلاد فزون دارد از هزار کلات بهريك ادر دبنار تنگها برتشگه .
فرخی سیستالی . *لغت‌فری ۶۲۷۹ .
```


## [2026-10-15T02:48:21.422Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 1252 1958; do echo \"######## BQT:$p\"; timeout 600 python3 tools/ref_page.py BQT:$p 2>&1 | head -c 4000; echo; done"
}
```


### [2026-10-15T02:48:22.224Z] TOOL RESULT

```
######## BQT:1252
[transcription from the page image; OCR text in data/verification/sources/refs/ocr/BQT/1252.txt]
[BQT p.1252 (vol 3), Mo'in's footnote on شتافتن — read from 1252.png by page-503 verifier]
* شتافتن - بکسر اول و فتح پنجم (در لهجهٔ مرکزی)، پهلوی ôshtâftan (عجله کردن)
رك : اسشق - هوبشمان ۷۷۷ ؛ در اوراق مانوی تورفان - 'wysht'b = avishtâb ،
ایرانی باستان * abi-shtâpayati ، ارمنی ع shtap (شتاب ؛ عجله) از * ushtâp- از
* us-stâp- «نیبرگ ۱۶۶» ؛ عجله کردن ، بسرعت انجام دادن ، شتاب کردن - بسرعت
رفتن - حمله و هجوم کردن .


######## BQT:1958
(no exact page map; using offset -1917 -> pdf page 41; check the printed number and re-run with --pdf-page if off)
REF: BQT:1958  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 41  OCR-lang: fas

هاه بر کوهان -۱۹۱۸-
و خوش صورت باشد .3 از طلا و نقره و برنج و مانندآ ن که زلان برض
ماه بر کوهان - نام لحنی باشد از | وگریبان فروبرند و آترا سنجق هم میگوبند -
مصنفات باربد وآن لحن بیست ویکم است ازسمی و يك حصه از دوازده حصهٌ تولجه را نیز گفته‌اند
لحن بارید .8 که هشت‌حبه باشد وتولچه دومثقال ونیم‌است؟۴ .
ماه پیکردرفش - کنایه از شب ماه خر گهی - باهیرا کویند که
است و بعربی لیل خوانند . درهاله باشد چه عاله را تیزخر گاه کوبند؟ (۱)
ماهتاب ۱ پرتوماه را کوبند- وماه - وکنایه از شاهد مهوش هم هست. .
را نیز گفته‌اند «مچوآفتاب - و چیزی که آتش ماهر - بروزن‌ظاهر بلفت‌زند ویاز ند(۲)
بازان از شوره وکو کرد و غیره سازند . بممنی فردا باشد که بعربی غد میگویند 8 -
ماه جو شاخ گوزن * کنایه از | ودرعربی بمعنی اوستاد باشد ‎٩‏ .
هاه باربك و خمیده است که ماه شب اول وشب ماه دمه - بسکون ثاك وفتح رای بی
دویم و سیم باشد . نقطه و میم » برماه راکویند* و آن‌آلتی باش د که
ماهچه - بروزن باغجه , سرعلمی را | درودکران بدان چوب‌وتخته سوراخ کنند وپزیان
کوبند که بصورت ماه ساخته باشند بعنی کرد | عربی مثقب خوانند ۷ .**
و هدور و صیقل زده از طلا ونقره و اغیره ۴ - ماهر وزه ۸ < بسکون ثاك بروزن
وسوزئیرالیز کویندکه‌بريك سرآن کلوله‌ای‌باشد ] چارروزه » بمعنی سال مه باشد که بمریی تاریخ
() خم۱: میباشد . (۲) چك : ژد ویاژند .
۱ مهتاب ( مخفف ) از : ماه (ه.م )+ تاب ( گرمی . نور ) لغة بمعنی لور ماء
و مجازاً جرم هاه :
از کوتهی بخت ندارم امد که بوبرانة من پرتومهتاب افتد . صائب‌تبریزی «فرهنکه نظام» .
۴ - ماهجچه , شکل علالی بود که بر سر علمها و چترهای پادشاهان سلجوقی و امرای
دیگر ترك بعد ازایشان منصوب بوده . ذکر ماه علم وماهچهٌ چتر در اشعار شعرای معاصرسلاجقه
و ,خوارزمشاهیان بسیار دیده میشود. خافانی در مدح علاءالدین تکش خوارزمشاه گوید :
ماهچهٌ چتر او قامةٌ کردون کشاد مورچهةٌ تیغ او ملك ملیمان کرفت.
رك : مجلهٌ ابران امروز ۱۶:۲ , چند فایدء ادبی بقلم آقای عبای اقبال ؛ ورك : مهچه .
۴ عماعه (ومم.) <ماهه (ه.م.) #۴ ماه خرکاهی « بپاز عجم *. 8 -اهز .
7۳( . پپلوی* ۶۳2182 ( فردا ) ۶« بوتکرس۱۱۹* - ‎۹٩‏ - (عر ) «ماهر . استاد
هرفن - وزبرك ورسا در هرامن - و ليك شناور » مهرة محر كة جمع » « منتهی‌الارب > .
۷ - رشیدی‌این معنی را نقل کرده گوید : «لیکن‌این‌لغت شاهد میخواهد» . رك : ماهه,
برماهه » برماه » برمه » پرمه» پرماه » پرمهه - ۸ << مهروز * روزماه * روزمه (ه.م.)
0 ماه پاره - رك : ماه پا ؛ ونیز مخفف آن « مهپاره » است .
0 ماه پروی
```


## [2026-10-15T02:48:29.789Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^آفتاب\\|^آفتاب ‌\\|آفتاب -\\|آفتاب ۱\\|^تابستان\\|تابستان ۱\\|تابستان -\\|^تابیدن\\|^تب \\|^تب -\\|^تپیدن\\|تپیدن ۱\\|^پرتو\" BQT_v1_pages.txt | head -20"
}
```


### [2026-10-15T02:48:30.214Z] TOOL RESULT

```
4078:تب طر یق نقطه گذاری شده: لفت( که باحروف ۸سیاه
6339:تب گر ك فاه ه بکس ثالث » کنابه
7583:تب که ۲۸ », « منای ۲۹۹ »؛ از ره 28۳
8232:آفتاب اه بروزن ماعتاب. پصب لت
12049:آفتاب را گویند - و بضی کقته‌اند جام جهان نما
12631:آفتاب چندان سایندکه منمقد شود » و طبیعت
14708:تب ۱۵۰ ,
16359:تابستانی باشد ۸ .
17669:آفتاب - و روزروشن - و آتش - و لملتییاقوت
19572:آفتاب‌پرست را کویند » و آن‌جانورست ازجنی
19775:تب و هواللحم بالعريبة » کتبو با بای عارسی نیز درست است -
23310:تب رکه ۱۷۲ *. ۵ - پاسا رکردن »
25701:تب رکف ۱۹۹ ( ذیل : 6۳۵5020 ) ۰ کلکی ۳85 , رني ۳25 , نطنزی 0251 « .۱ ص
26452:تب باشد و «عرب
26635:آفتاب بسمت الرای رسد بشکند و آن را گل
28047:آفتاب وماء وشمحع ویرت و آتش راگوشد 4
28278:تب وی 6 سس
28403:آفتاب و ماء و ستاره و چراغ و آش و امشال
28662:تب زکنته‌اند ٩٩‏ ؛ و نبرژد بجهت آن گویند که
28728:تب بفتح اول و کر تالی بروزن
```


## [2026-10-15T02:48:32.539Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 8225,8240p BQT_v1_pages.txt; grep -n \"آفتاب\\b.*پهلوی\\|پهلوی.*آفتاب\\|aftab\\|âftâb\" BQT_v1_pages.txt | head -5; sed -n 28720,28740p BQT_v1_pages.txt"
}
```


### [2026-10-15T02:48:33.025Z] TOOL RESULT

```
) غول - نم ثالث وسکون واومجپول
و لام » نگاه کردن و نگرستن بگوشة چشم‌باشد
از روی خشم ۴ -
یل هب رذن فاییل ».جسنی آغول
است که نگرستن بگوشهُ چشم باشد از روی
خثم ؟ .
]له - بروزن کاف. بمعنی مهراست
آفتاب اه بروزن ماعتاب. پصب لت
تایش و روشنی و برتو عهر است همحو ماحتاب
ترکیبی آن آفت آب است - و جصب احطلاح
شمی‌دا گویند - و بمعنی روز عم آمده است -
و کتابه ازشراب انگوری هم همت - ونزد ازیاب
سلوك از آفتابت دوح مراد است و از ماهتاب
نف ؛ و کوبند روح دریدن یمنرَلهٌ آفتاب است
غلامان ویندکان ترژك :
ای خواجهٌ ارسلان و آغوش
1205:«چون لغت عبری وسریانی وپهلوی تا بایام طلوع آفتاب دین عر ی
ساسکرت (دخیل) 2۷8722 «اونوالا ۰۵۵۳ .
۶ وآن سیب چومخروط یکی کوی تبرزد در معصفری آب زده باری سبصد.
«منوچهری دأمفانی۲۰ ۰*۱
۱ - باول هرن پس از ذ کر این‌وجه اشنقاق نوبد: اشتقاق عامیانه(!) «اسذق ۳۷4*.
۴ رك: تسرزد .تیسیدن! ه بر وزن و معنی نفسیدن
۱ ست که کرم شدن‌باشد .
تسیل ی ۲
بسیف ۵ " » بروژن فهمیده. » بمعثی گرم
تب بفتح اول و کر تالی بروزن
کثش » گرما و کرمی را کویند - ومخنف‌تایش
هم حست که فروغ وپرتو باشد.
یشی؟ طبقی باشد ند گرولن از
مس و نقره و طلا هم سازند ؛ و طبشی معرب
۳
ثیقود " ه با فا بروزن سر دوز ۰ مردم
و چاروا را ببرامون و کردا کرد دهان» ومرغان‌را
منفار باشد ؛ و بجای فا فافی هم بنظر آمده
است. .
بل «یفتح اول وانی بروزن اجل»چین
و شکنج و آجیده را گویند مانند چین وشکنج
و ناهمواری بوست یدام .
```


## [2026-10-15T02:48:35.606Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -n 8232 BQT_v1_pages.txt | tr -cd '\\f' | wc -c; awk 'BEGIN{RS=\"\\f\"} NR==258' BQT_v1_pages.txt | grep -n \"آفتاب\\|اوستا\\|پهلوی\\|tâb\\|tap\" | head"
}
```


### [2026-10-15T02:48:36.054Z] TOOL RESULT

```
259
```


## [2026-10-15T02:48:38.032Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==260' BQT_v1_pages.txt | grep -n \"^۱\\|^۲\\|^۳\\|آفتاب\\|اوستا\\|پهلوی\" | head -20"
}
```


### [2026-10-15T02:48:38.425Z] TOOL RESULT

```
8:۲ و شیدان - بمنی دریفل گرفتن‌ودر
17:آفتاب اه بروزن ماعتاب. پصب لت
22:سلوك از آفتابت دوح مراد است و از ماهتاب
23:نف ؛ و کوبند روح دریدن یمنرَلهٌ آفتاب است
43:۲ فتاب بر کوه‌ر قتن بمعتی کاب
46:۲ فتاب بگل اندودن - کنایه از
49:۲ فتاب‌درد بِ بضم‌دال‌اول, شبکه‌ای
50:باشد که طفلان از پوربا سازد و در آفتاب
```


## [2026-10-15T02:48:39.983Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==260' BQT_v1_pages.txt | tail -25"
}
```


### [2026-10-15T02:48:40.376Z] TOOL RESULT

```
« حرذون » کوشد من
و کل یکه بر هر طرف
آ فتاب‌میل کند بر گهای
آن رو بدان جاب
کند ۷- واهل‌هند بر
ح رکل کبود عموماً -
وطایفهای پیز باشند از
گبران و مش رکان و افلا کیان ۸ ۰
۲ فتاب بر کوه‌ر قتن بمعتی کاب
بر دیواز رفئن است که کنابه از انتهای عمر
و زندکانی و دولت و کامرانی باشد .
۲ فتاب بگل اندودن - کنایه از
خی‌پوشکردن و پنپان ساختن امری بود که در
تهات کهور باشد .
۲ فتاب‌درد بِ بضم‌دال‌اول, شبکه‌ای
باشد که طفلان از پوربا سازد و در آفتاب
۴ - در حقیقت نامی است ازدامهاي
هر گاه «لفت نامه؟ .
۴ - بهلوی 26128 «منای۲:۲۹4*:
کلکینا۵؟2 (یز2609) . فریز دی #فا2 و202۳. برنی 2003۷۷ نطنزی 00۵۷
۰ .. ۱ ص۲۸۵ . سمنانی 3610۷۷, سرخه 26۷8۷ . لاسکردی 21101۷ , شهمیرزادی 26120
« 4 ۷ ص ۱۸۰ مرکب ازآفی - آبط تاب. آق درایتجا بمعنی روشنی و درخشندگی است
و تاب از تاییدن بسعنی گرم کردن است ؛ پس‌کلمةً م کب آقتاب بمعنی (جرم ) روش نکرما بخش
است . ایکه در فرهنگها ممنی ترکیبی آبرا< آفت‌آب » نودته اند مبتنی برفقه اللغة عامیانه
است . « یشتها اس ۳۰۵ . ۷ - 26110070۳6. ۸ مراد برستن دگان مهر ۷110۳۵ است .
```


## [2026-10-15T02:48:43.687Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^tight\\b\\|^tight,\\|^tepid\\|^tangle\\|^thick\\b\\|^thick,\" KLN_1966.txt | head"
}
```


### [2026-10-15T02:48:43.968Z] TOOL RESULT

```
38141:tangle,  tr.  v.,  to  hamper,  ensnare;  intr.  v.,  to  be¬ come  tangled.  —  ME.  tangilen,  formed  with freq.  suff.  -le  fr.  Dan.  tang,  ‘seaweed’  (see  tang, ‘seaweed’).  The  orig.  meaning  of  the  verb tangle  was  ‘to  form  a  mass  comparable  to seaweed’.  Cp.  entangle.  Cp.  also  toggle. Derivatives :  tangle,  n.,  mass,  confusion,  tangle- some,  adj.,  tangl-y,  adj.
38621:tepid,  adj.,  moderately  warm,  lukewarm.  —  L. tepidus,  fr.  tepere,  ‘to  be  warm  or  lukewarm’, which  is  cogn.  with  OI.  tdpati,  ‘makes  warm, heats,  burns',  tdpu-,  ‘burning’,  tdpafi,  ‘heat’.
38625:tepidarium,  n.,  intermediate  room  in  the  Roman bath,  situated  between  the  caldarium  and  frigi- darium.  —  L.,  ‘a  moderately  warm  room’,  prop, neut.  of  the  adjective  tepidarius,  ‘pertaining  to  a lukewarm  bath’,  used  as  a  noun.  Tepidarius  de¬ rives  fr.  tepidus,  ‘warm,  lukewarm’.  See  tepid and  -arium.
39242:tight,  adj.  —  ME.  thight,  tight,  of  Scand.  origin, cp.  ON.  pettr,  Dan.  t;et,  Swed.  tat,  which  are rel.  to  MHG.  dihte,  G.  and  Du.  dicht,  ‘dense, tight’,  and  to  OE.  gedthan,  gedeon,  OS.  thihan.
```


## [2026-10-15T02:48:46.090Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 38622,38624p KLN_1966.txt | cut -c1-600; sed -n 39243,39246p KLN_1966.txt | cut -c1-800; grep -n \"^thick,\\|^thick \" KLN_1966.txt | head -2"
}
```


### [2026-10-15T02:48:46.439Z] TOOL RESULT

```
teratology
Avestic  tafnush,  ‘fever’,  Toch.  B.  tsdp-,  ‘to  make lukewarm’,  an-tdpee,  ‘fire,  conflagration’  (an-  in antapee  is  a  prefix  of  intensity),  OSlav.  topiti,  ‘to warm’,  tepid,  ‘warm’,  teplosti,  ‘heat;  warmth’, OIr.  tene,  gen.  tened  (for  *tepnet-),  ten,  ‘fire’,  te (for  *tepent-),  ‘hot’,  W.  tes,  ‘heat’,  Alb.  Gheg ftof,  Tosk  ftoh  (for  *ve-tep-sk-),  ‘to  deprive  of heat’  (seeN.  Joklin  Indogermanische  Forschun- gen,  37,  103).  Cp.  tapas,  topaz  and  the  second element  in  Beltane  and  in  pardao.  For  the  ending of  tepid  see  1st  suff.  -id.
Derivatives:  tepid-ity,  n.,  tepid-ly,  adv.,  tepid¬ ness,  n.
OFris.  thigia,  MDu.  ghedien,  Du.  gedijen,  OHG. gidihan,  MHG.  gedihen,  G.  gedeihen,  Goth. (ga)peihan,  ‘to  thrive,  grow,  prosper,  flourish’, OHG.  gidigan,  MHG.  gedigen,  ‘grown  up,  firm, genuine’,  G.  gediegen,  ‘genuine,  solid,  worthy’ (prop.  pp.  of  OHG.  gidihan,  MHG.  gedihen, resp.  former  pp.  of  G.  gedeihen),  and  cogn.  with Ir.  techt,  ‘curdled,  coagulated’,  Lith.  tankus, ‘close,  tight’,  Pers.  tang,  ‘tight’,  OI.  tanakti, ‘draws  together,  contracts’,  fr.  I.-E.  base  *tenq-, ‘to  be  thick  or  strong’.  The  initial  t  (for  th)  in ME.  and  E.  tight  is  due  to  the  influence  of  Swed. tat,  Dan.  test.
Derivatives:  tight,  adv.  and  tr.  v.,  tight-en,  tr.  v., tighten-er,  n.,  tight-er,  n.,  tight-ish,  adj.,  tight-ly, adv.,  tight-ness,  n.,  adv.,  tight-s,  n.  pi. tiglic,  also  tiglinic,  adj.,  pertaining  to  a  crystalline acid  (C4H,C02H,  obtained  fr.  croton  oil  (chem.) —  ModL.  tiglium,  in  Croton  tiglium,  ‘the  croton oil  plant’,  fr.  Gk.  tiXoi;,  ‘a  thin  stool',  so  called in  allusion  to  its  purgative  properties.  Gk.  tiXo? is  prob.  cogn.  with  OSlav.  tilja,  ‘decomposition, putrefaction’,  tiled,  ‘to  rot,  putrefy’.  Arm. t'rem,  ‘I  knead’  (prop.  ‘I  moisten  the  dough’), t'rik\  ‘dung’,  OSlav.  tina,  ‘mud,  mire’,  Lith. tyras,  tyre,  ‘pap’,  W.  tail,  ‘dung’,  OE.  pinan,  ‘to become  moist’ ;  fr.  I.-E.  base  */(-,  *tli-,  ‘to 
tigrine,  adj.,  tigerlike.  —  L.  tigrinus,  fr.  tigris.  See tiger  and  adj.  suff.  -ine  (representing  L.  -inus). tigroid,  adj.,  resembling  a  tiger.  —  Compounded of  Gk.  Tiyptc,  ‘tiger’,  and  -oetSyji;,  ‘like’,  fr. sISoig,  ‘form,  shape'.  See  tiger  and  -oid. tike,  n.  —  See  tyke.
til,  n.,  a  mark  ( ~ )  placed  over  a  vowel  or  the  first vowel  of  a  diphthong  in  Portuguese  to  indicate nasalization  as  in  13,  grdo.  —  Port.,  fr.  L.  titulus. See  tilde.
```


## [2026-10-15T02:48:50.028Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^thick,  adj\\|^thick, adj\" KLN_1966.txt | head -2; grep -n \"thick,  adj\" KLN_1966.txt | head -2 | cut -c1-500; grep -n -i \"teng\\b\\|tafnah\\|tepide\\|^tight\\b\" SKT.txt | head -5; grep -n \"^TIGHT\\|^TEPID\\|^TANGLE\" SKT.txt | head"
}
```


### [2026-10-15T02:48:50.466Z] TOOL RESULT

```
39030:thiazine,  thiazin,  n.,  any  of  a  class  of  ring  com¬ pounds  containing  one  sulfur  atom  and  one nitrogen  atom  and  four  atoms  of  carbon  (bio¬ chem.)  —  Compounded  of  thio-,  -az  and  -in(e). thiasus,  n.,  a  religious  brotherhood  ( Greek  antiq.) —  L.,  fr.  Gk.  (Kaooc,  ‘religious  guild,  confra¬ ternity’,  which  is  of  uncertain  origin, thiazole,  thiazol,  n.,  a  colorless  liquid  C3H3NS (chem.)  —  Compounded  of  thio-  and  azole, thick,  adj.  —  ME.
4165:Coatermonger.  (F.  anJ  E.)     Formerly  \ cciterd0tangtr  or  cMtard-mett^,  a  sdlcr  i of  iOitards  or  sjiplcs.    ['Ilie  sc^x  'iiteng^r U  H. ;   see  HonKer.l     M.  E.  ceitani,   an apple,  where   Ihe  suffix  -ani  is  F. ;  prob. from  O.  F.  <cjU.  F.  (dte,  a  rib;  c£  F.  /mii
19704:TIGHT.
19715:Tight  (Scand.)  Properly  tkigAt:  but. OS  both  Dan.  and  Swed.  put  /  for  tk.  it easily  became  tigkt.  Prov.  E.  tkite,  tit;ht, close,  compact ;  M.  E.  /ij/.  ako  Jwj/-  tkjkt.
21804:Young.  (E.)  M.  E  yong,  yteng.  A.  S. gt<*^S,  gi**rtg.  rung,  )oung.  +  Dn,  j^g, Icel.  ungr,  jungr.  Dan  Swed.  ung,  u. junt^,  Goth,  juggs  (written  for  jungs*\. p,  T htw  forms  answer  to  Lat  iuHttttus.  a young  animal,  heifer,  W.  iettanc^  yoang; ol  her  forms(withont  the  final  galluran occur in  L.  iuuenUt  Lith.  jaunas,  Skt.  yux>an, youn)^,  Uuss.  iunuH,  young.  "D^x.yQung- ting.  youngster :  also  youn-ker,  borrowed from  Vvi.  Jffnker^  Jonkheer,  i.e.  young  sir. compounded  of  Jong,  young,  and  A/rr,  sir^ a  lord.
19704:TIGHT.
```


## [2026-10-15T02:48:52.498Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 39030p KLN_1966.txt | grep -o \"thick,  adj.*\" | cut -c1-500; sed -n 19715,19722p SKT.txt; grep -n \"^Tangle\\|^Tepid\\|^Thick\" SKT.txt | head; "
}
```


### [2026-10-15T02:48:53.014Z] TOOL RESULT

```
thick,  adj.  —  ME.  thicke ,  thikke,  fr.  OE.  piece, rel.  to  OS.  thikki,  ON.  pykkr,  pjukkr,  piokkr, Dan.  tyk,  Swed.  tjock,  Norw.  tjukk,  OFris. thikke,  MDu.  dicke,  Du.  dik,  OHG.  dicki,  dichi, ‘thick’,  dicco,  ‘often’,  MHG.  dicke,  G.  dick, ‘thick’,  fr.  I.-E.  base  *tegu-,  whence  also  OIr. tiug,  ‘thick’,  W.,  Co.  tew,  Bret,  teo,  of  s.m. Derivatives:  thick,  n.,  adv.  and  v.,  thick-en,  tr. and  intr.  v.,  thick-en-er,  n.,  thick-en-ing,  n., thick-et
Tight  (Scand.)  Properly  tkigAt:  but. OS  both  Dan.  and  Swed.  put  /  for  tk.  it easily  became  tigkt.  Prov.  E.  tkite,  tit;ht, close,  compact ;  M.  E.  /ij/.  ako  Jwj/-  tkjkt.
—  Icel.  p/ttr,  tight,  e>p.  water  tight ;  Swed. tS/,  close,  tight,  solid,  compact  ;  Dan.  /.r/. tight,  close,  compact,  taut,  water-tight. M.  £.  /jV  shews  tlie  old  guttural ;  the Icel-  p^ttr  is  for  (v^/r»,  as  shewn  by  Du. digt,  G.  difkt,  tight :  orig.  '  thatched '  or •  covered  iu/  hence  *  water-tight.'  Cognate with  L.  ttctus,  Gk.  artxrvt  (.it)  o-ffvaimM), thatched,  co\eied  to.  Sn  Tlialoh. (ySlAG.)
5IO
TIKE.
taut.  (Dan.)  Dan.  tat,  tight,  clos«.  tsut (above).
Tike,  m  dog.  low  fellow.  (Scand,)  M.  E. tiki.^lcx^.  tlk,  Swed.  tiky  a  bitch.
Tile ;  see  Te^rument.
Till  (I),  to  cultivate.  (E.)  M.E.  tilitn. A.S.  tilian^  to  labour,  endeavoar,  stiire after,  to  tiU  land.  On^.  to  aim  at  excel- lence.—A.S.  tii,  good,  excellent,  prohlable; ///,  ah.  goodness.  +  Du.  ffUn,  to  breed, cultivate,  till  ;  G.  xt'flen,  to  aim  at,  from O.H.G.  siV,  a  mark.  Der.  /tV-M,  A.S. t/VS,  a  crop,  cultivatioo.
19157:Tangle,  to  knot  confuwdly.  ( Spelt  tangell  in  Palsgrave.  To  Uh^ 'to  keep  twisting  together  like  iMwee«i^ a  ftequentative  verb  from  North  t-  to* sea-weed.  -  Don.  tang^  .Swed.  thn^,  to \aHg^  kelp  or  bladder-wracJc,  a  tca-w (whence  the  idea  of  confused  heap) :  \ Icel.  \>ongHU.  sea-weed.  So  also  prov.  1 tmtgU,  sea-weed ;  Norman  K. kind  of  scfl-weed  {Fntw  Jlagei^trm M^tivier).  Dor.  en-tangU,  with  F.  prc( m-  ( =  L.  in).
19405:Tepid,    (L.)     L.    tefidm, tepere,  to  be  wann.+.Skt  /.t*.  to  \ Kuis  topittt  to  heat      '  v  \
```


## [2026-10-15T02:48:56.735Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; W=incoming/WLD/WLD_Bd1_pages.txt; grep -n \"tenk-\\|tep- \\|tep-\\.\" $W | head; grep -n \"tańč\\|tanc\\|tanakti\" $W | head -5; grep -n \"tapati\" $W | head -5"
}
```


### [2026-10-15T02:48:57.122Z] TOOL RESULT

```
67757:tep- .,\varm sein“.
70371:zu tep- „warm sein", ai. tdpyati „kasteit sich        zw. Fick III 4 1 80)
79507:von -demavoq als *tep-sra zu *tep- „warm, lau sein“, z. B. Prellwitz 2 s. v.
18311:statt -vin- hier                         wie           in    iuvencus richtig Juret Dominance et resistance 204)
62957:(einmal             belegt,           sonst)    giestrandeeg ,            giestranniht,             gyrstancefen          „gestern
68457:tiichtig, energisch, heldenhaft", Komp. tqsyah-. Sup. tanciita-; np. tan-
66540:     Ai.    vi-tapati       „driickt      auseinander“, sam-tapati „driickt zusammen“, np.
```


## [2026-10-15T02:48:59.388Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; W=incoming/WLD/WLD_Bd1_pages.txt; sed -n 68445,68465p $W; echo ----; sed -n 67757,67775p $W; for n in 68457 67757; do head -n $n $W | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1; done"
}
```


### [2026-10-15T02:48:59.806Z] TOOL RESULT

```
                                                                                                                gerinnen),       fest,
        dicht werden" (daraus aucb .gedeihen").                  ,



      Ai. tone-,              tandlcti     „zieht     zusammen", mit a „macht gerinnen", atdnga-
na-m „Mittel zura Gerinnen, Lab", tcikrd-m ,,Buttermilch zur Hiilfte mit
Wasser vermischt" [*tnj-l6-m * tenj-lo-m in isl. pel av. taxma- „tapfer,
                                                          :
                                                                                                 ,


tiichtig, energisch, heldenhaft", Komp. tqsyah-. Sup. tanciita-; np. tan-
jldan   zusammenziehen", arm. t'anjr „dicht, dick" (? s. u. tengh- .ziehen");
             ,,                                                                                                      ,


ir.       p'tcnqto- vgl. aisl. petty, Stokes BB. 25, 25S) ,,geronnen", te elite
       teeht
,,gehorig, recht", cymr. icifhi ^characteristics'  meymr. brenhin teithiawc          -

----
tep- .,\varm sein“.
      Ai. tdipati „gibt Warme von sich“, erwarmt, brennt"                   tdpati tdpyati auch
                                                                          (                                         ,

„kasteit       sich,      iibt    BuSe“,      s. Guntert Reimw. 44), ptc. taptd-h „erwarmt,
erhitzt“,      t&pah         n.   „IIitze,    Glut“ (vgl. lat. tepor und die kelt. u. o.-u. Ab-
leitungen),        tdpu-h          „gliihend,      heiti“,         Kaus.      tapd.ya.ti            „erwarmt, erhitzt“;
av. tapaiti        „ist      warm", Kaus. tdpayeiti „erwarmt,                                   erhitzt
                                                                                                          11
                                                                                                         Inkoh. tafsaiti
                                                                                                               ,

„wird hei[.>“, Ptc. tapta- ., erwarmt, heiB“, tafnu- m. „Fieberhitze, Fieber“,
tafnah- n. ,.Hitze, Glut; Fieber“; np. taftan „brennen, wiirmen. leuchten";
                                            tem-                                719

     alb. tosk. ftoh , geg. ftof „mache kalt, losehe aus, verletze mit Worten"
(
  *vetep-shd  G. Meyer Wb. 113, Pedersen KZ. 36, 325, Jokl IF. 37, 103);
```


## [2026-10-15T02:49:02.558Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^tep\\|^tenk\\|^tenq\\|^tenk\" IEC.txt | head; grep -n \"^tep- \\|tepō\\|^tepos\" IEC.txt | head -5"
}
```


## [2026-10-15T02:49:04.189Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"tepō\\|tepos\\|tepō\\|tep[eoōā]-\\|tenk\\|tnk\" IEC.txt | head -15; grep -n -i \"^tight\\|^TIGHT\\|tepid\\|lukewarm\" SYN.txt | head -5"
}
```


### [2026-10-15T02:49:04.718Z] TOOL RESULT

```
18367:tenk- (1) “press, squeeze, cram'. Cf. teng-, tuengh- and tonk- Skt. tanákmi, v. (contract; Av. cf. taficisto, superl. (“very strong’, var. of tafijisto, see teng- above); Arm. cf. ack tnkem, v. (fstare', fr. *oques- ^); Alb. cf. tingé, f. (^sultriness', but cf. teng- above); W teng, adj. (tough, tenacious’ (possibly fr. *teng-. Ambig.); MHG dingen, wv. (1) ‘assemble’; OE pingan, ON þinga, sv. 3. (1), id.; MHG cf. dihte, adj. ‘tight, close’; OE -piht, cpds. id.; Latv. tiecos, tiektis, v. ‘strive’
18368:tenk- (2) “fit, meet, coincide, agree’. Cf. tonk-, tnk- and tink-, tik- Tokh. A tsànk-, B Genk, v. “happen, arise’; OHG thingon, dingon, wv.; MHG dingen, wv. (2) “hope, trust, think’; dinge, wm. “hope, trust'; ON þinga, v. (2) ‘consult’; OHG also thingen, dingen ‘negotiate’; OCS cf. teklü, adj. "like, equal’; Srb. t&k, m. (1) “taste”; tečan, adj. ‘tasty’; Cz. cf. netecny, adj. ‘indifferent’; vy-teény, adj. ‘excellent’; Ukr. na-tjak, m. *il- lusion’; na-tjaknuty, v. ‘allude to’; Li. cf. man tenka, impers. “happen, chance to’; inf: tekti, see tek- (4); Latv. cf. tenka, f. “old wive's tale’; Li. also tenkinti, tr. ‘satisfy’; ? z-gde in man tinka (‘I like’, but cf. tink- below); (tinku, tikti, v. “agree, fit, suit, please’. Prob. a hybrid); (o-gde in) Br. tonki, tunki, pp: tonket, v. “agree to a bargain by striking hands’
18389:tep- (1) “be warm’; tepos, -es- ‘heat’. WP I, 719. Cf. tepmn-, tepont-, tepsK-, tept-, (top-), etc. Skt. tápami, v. "be warm, shine’; tr. ‘scorch’; tapyami, tapye, v. "be heated, burn, glow’; Av. tap-, v. “burn, glow, shine’; Per. tabidan, inf. ‘shine’ beside tafsidan, inf. (grow warm’, fr. *tepsK-); Hitt. cf. tapasas, s. (queried: fever); Lat. tepeo, Ere, v. be warm’; Alb. cf. f-tof, f-toh, v. (cool, chill’, fr. *apo-tepsKo); Mir cf. tenn, adj. “burning”; teine, f. (fire,
18392:tep- (2) (tepo, ið) “knock, tap, beat". Per. tapidan, inf. ‘palpitate’; Tokh. táüp-, v. ‘bang’; Oss. càf, s. with variant initial: “blow, wound’. Cf. táfsín beside cáfsín, inf. “feel warm’; OE pefian, ‘palpitate, pant’; o-gde in OHG bi-deppen (alleged), and in Icel. pefa, v. “scent out. Here?)
18393:tep- (3) (tepð) ‘smooth, smear, anoint’. See next Olr. cf. (?) téith, adj. (smooth, easy’, if fr. *teptis); Br. cf. (?) téon, tenv, m. 'sap'; Li. tepü, tépti, v. 'anoint, smear’; Latv. tepju, tept, id. (Isophonic: Li. tepi, éti, v. “sup, lap up?)
18394:tepolos ‘smear, lubricant W tail, m. ‘filth’; Li. tépalas, m. "lubricant, ointment'; (isophonic in Ir. teol, m. 'abun- dance; well-being)
18395:tepent- (tepnt-) (being) hot, (being) warm’. Cf. tep- (1) Skt. tapat, act. pt. mfn. id.; tapatih, f. ^warm- ing’; Arm. tend, tent, i-stem Clever": Skt. tapa- tih) beside tenğ (avidity, hunger”, fr. *tepntio-); Olr. té, pl. téit, adj. "bot" (an old nt-stem'. Thurneysen)
18396:tepn-, extn. of type tep- (1), q. v. Av. tafno, m. ‘heat’; tafnus, s. “fever”; Olr. tene, gs: tened; Ir. teine, gs: teineadh, f. ‘fire’; OBr. tan, Br. tân, pl. taniu, W tân, pl. -au, Cor. tān, pl. tanow, m. id.
18397:tepskö ‘grow warm, be warm’. Cf. tep- (1) and derivs. Av. tafs-, id.; Per. tafsīdan, inf. id.; Oss. täf- sín, cäfsín, id.; Alb. cf. f-tof, f-toh, v. (“grow cold’, fr. *apo-tepsK-)
18398:tepst- “heat, warmth'. See next and cf. tep- (1) with extns. Oss. tafst, id.; Arm. tawt, ost “heat; sultri- ness’; Olr. tess, Ir. teas, m. ‘heat; OW, W, Cor. tes, m. id.; Br. téz, m. (1) ‘sultriness’
18389:tep- (1) “be warm’; tepos, -es- ‘heat’. WP I, 719. Cf. tepmn-, tepont-, tepsK-, tept-, (top-), etc. Skt. tápami, v. "be warm, shine’; tr. ‘scorch’; tapyami, tapye, v. "be heated, burn, glow’; Av. tap-, v. “burn, glow, shine’; Per. tabidan, inf. ‘shine’ beside tafsidan, inf. (grow warm’, fr. *tepsK-); Hitt. cf. tapasas, s. (queried: fever); Lat. tepeo, Ere, v. be warm’; Alb. cf. f-tof, f-toh, v. (cool, chill’, fr. *apo-tepsKo); Mir cf. tenn, adj. “burning”; teine, f. (fire,
18392:tep- (2) (tepo, ið) “knock, tap, beat". Per. tapidan, inf. ‘palpitate’; Tokh. táüp-, v. ‘bang’; Oss. càf, s. with variant initial: “blow, wound’. Cf. táfsín beside cáfsín, inf. “feel warm’; OE pefian, ‘palpitate, pant’; o-gde in OHG bi-deppen (alleged), and in Icel. pefa, v. “scent out. Here?)
18393:tep- (3) (tepð) ‘smooth, smear, anoint’. See next Olr. cf. (?) téith, adj. (smooth, easy’, if fr. *teptis); Br. cf. (?) téon, tenv, m. 'sap'; Li. tepü, tépti, v. 'anoint, smear’; Latv. tepju, tept, id. (Isophonic: Li. tepi, éti, v. “sup, lap up?)
18399:tep- — teren- (terun-, tern-)
```


### [2026-10-15T02:49:04.726Z] TOOL RESULT

```
17664:sthnk- (stnk-), variant of type sthng- and sthngh-, q. v. Br. stank, adj. ‘compact; W (ambig.) sang, f. ‘tread’; Pol. (isophone?) cf. stek, m. ‘groan’?
18268:ték- (1) “pleasant; pleased; pleasure’. Cf. tekəlos (tekəros) & tenk- (2) Olr. tig, tich, adj. (seemly; pleasant’, fr. *te- kus); Ir. cf. teachta, adj. ‘suitable’; W teg, adj. ‘fair, beautiful’; Cor. tek, id.; cf. tegen, pl. tegennow, s. ‘jewel; ON pega, f. (Cgift', fr. *tekà) beside (long-gde) adj. pægr ‘agreeable, acceptable’; mod. bága, f. “advantage, inter- est’; ON paegja, tr. ‘make acceptable’; W cyn- nig, v. ‘propose’; mell-tigo, v. ((curse', fr. *meli-"); (variant w. doubling) OS thiggian, OE picgan, wv. “accept, receive’; Srb. cf. tëk, Slovene ték, m. ‘liking, appetite’; Srb. tečan, adj. ‘likable, tasty’; Cz. cf. vý-tečný *excellent'; netečný ‘indifferent’; Li. cf. tékit! “please! do accept"; impers. in man tenka, inf: tekti “it falls to my lot
18273:Tokh. B täk-, tek-, v. id.; Lat. cf. (?) per-tica, f. ‘pole’; Li. cf. man tenka, inf: tekti, v. “befalP
18275:tekolos, tekoros (1) ‘pleasant’. Cf. tek- (1) and tenk- Olr. & Ir. tacair, adj. ‘suitable’; Icel. ball ‘pleasant, docile’; MHG (variant) dere ('suit- able’, fr. *tekrios). O-grade radical in Ir. toich, gs: tocha, adj. ‘pleasing, acceptable
18354:teng- “hard, firm, strong”. Cf. tenk-, tuengh-. (W. Sl. ambig.) Av. cf. tañjistō, superl. “very strong’ beside 0afijayei(mi), v. (2) ‘tame’; OCS cf. tẹžọ, iti, v. (2) “weigh down'; R cf. tjagotà “burden; Cz. tíha f. d: cf. těhotná ‘enceinte’; (variant consonantism in) Slovene tezati, inf. “stretch. (For Per. tang ‘tight, narrow’, see tonk-; for W teng, adj. ‘tough, tenacious’, see tenk-, but possibly « teng- as here)
18356:ten- — tenk-
18366:ten£hóo, io (?) “seek, ask, beg’. Gmc. ambig. Cf. tenk- (2) OSw. biggja ask: OE pingian, wv. (1) “ask, beg; harangue’; ping, n. ‘cause, act, suit’; OCS tezo, tezati, v. “challenge, dispute, oppose’ beside variant tegati se, v. ‘quarreľ; OCz. Z- tieZu, z-tázati, v. ‘search for, seek’; tieZu, inf: tázati, v. ask; Cz. tázat se, inf. id.; do-taz, m. *questionnaire'
18367:tenk- (1) “press, squeeze, cram'. Cf. teng-, tuengh- and tonk- Skt. tanákmi, v. (contract; Av. cf. taficisto, superl. (“very strong’, var. of tafijisto, see teng- above); Arm. cf. ack tnkem, v. (fstare', fr. *oques- ^); Alb. cf. tingé, f. (^sultriness', but cf. teng- above); W teng, adj. (tough, tenacious’ (possibly fr. *teng-. Ambig.); MHG dingen, wv. (1) ‘assemble’; OE pingan, ON þinga, sv. 3. (1), id.; MHG cf. dihte, adj. ‘tight, close’; OE -piht, cpds. id.; Latv. tiecos, tiektis, v. ‘strive’
18368:tenk- (2) “fit, meet, coincide, agree’. Cf. tonk-, tnk- and tink-, tik- Tokh. A tsànk-, B Genk, v. “happen, arise’; OHG thingon, dingon, wv.; MHG dingen, wv. (2) “hope, trust, think’; dinge, wm. “hope, trust'; ON þinga, v. (2) ‘consult’; OHG also thingen, dingen ‘negotiate’; OCS cf. teklü, adj. "like, equal’; Srb. t&k, m. (1) “taste”; tečan, adj. ‘tasty’; Cz. cf. netecny, adj. ‘indifferent’; vy-teény, adj. ‘excellent’; Ukr. na-tjak, m. *il- lusion’; na-tjaknuty, v. ‘allude to’; Li. cf. man tenka, impers. “happen, chance to’; inf: tekti, see tek- (4); Latv. cf. tenka, f. “old wive's tale’; Li. also tenkinti, tr. ‘satisfy’; ? z-gde in man tinka (‘I like’, but cf. tink- below); (tinku, tikti, v. “agree, fit, suit, please’. Prob. a hybrid); (o-gde in) Br. tonki, tunki, pp: tonket, v. “agree to a bargain by striking hands’
18389:tep- (1) “be warm’; tepos, -es- ‘heat’. WP I, 719. Cf. tepmn-, tepont-, tepsK-, tept-, (top-), etc. Skt. tápami, v. "be warm, shine’; tr. ‘scorch’; tapyami, tapye, v. "be heated, burn, glow’; Av. tap-, v. “burn, glow, shine’; Per. tabidan, inf. ‘shine’ beside tafsidan, inf. (grow warm’, fr. *tepsK-); Hitt. cf. tapasas, s. (queried: fever); Lat. tepeo, Ere, v. be warm’; Alb. cf. f-tof, f-toh, v. (cool, chill’, fr. *apo-tepsKo); Mir cf. tenn, adj. “burning”; teine, f. (fire,
18572:(2) “sharp, crue?" (for Cor. tyn ‘tight’, see tig- (2); LLat. cf. tigalus, m. ‘snapdragon’. See next tigstlos, à ‘tip, point. Cf. tig- (1) and tigros Lat. cf. scin-tilla, f. ‘spark’; OHG distil, f.; Du. distel, f.; OE pistel, m.; ON pistill, m. ‘thistle’ tik- ‘reach, touch, suffice, satisfy’. Cf. tenk- (2), teik- and tink-. Ext. okt Gmc. forms ambig. W tygio, inf. “prosper, succeed'; Go. (ambig.)
18582:_ beihan, MHG dihen, sv. 1. id. (but cf. tenk-
18594:tink- *hit, meet, reach, suffice, suit, please'. Cf. tik-, tenk- & teik- W cf. tynged, pl. -ion, f. “luck? beside tygio, inf. succeed’. See tik-); MHG dinc, gs: din- ges, n. “affair, lawsuit; thing’; dingen, wv. ‘go to law’; OE ping, n. ‘matter, lawsuit; event: pingan, sv. 3. ‘prosper’; (for OE pingian, see tengh-); Li. tinka, 3s. impers. “it pleases’; inf: tikti, cf. also su-tinkü, -tikti, v. *meet; agree"; Latv. tiku, tikt, v. “please?
18671:(tnk- “fit, join, suit, arrange’. See Supt: T)
18672:tno, ið (ton-, títén-) ‘stretch, extend". Cf. tnuó, ten-, etc. WP I, 723 Skt. tan-, radical, id.; Av. tan-, v. id. (and *Jead^); tanyo, adj. ‘spread’; Per. tanam, Idan, v. ‘spin’; Oss. cf. tíndzín, Dig. tindzun, pp: tigd, v. (stretch, spread": fr. *ton-a$0, cf. Ir. tanuighim, v. ‘thin out, fr. *tonu-ag0); cf. also Oss. tonin, inf. ((pull', fr. *tonuo or *tnuo, q.V); Gk. cf. teíno (e-gde) beside redup: titaino, v. ‘stretch’; Alb. (e- or zero-gde): n- dëi. v. “extend, stretch"; MIr. tanaim, v. ‘thin’ beside Ir. tanuighim, v. id., W tanu, inf. "ex pand, spread"; Go. (and com. Gmc. o-gde) uf- panjan, tr. ('stretch', cf. tonos & ton-) beside (z-gde) MHG donen, intr. id. (Isophonic: Lat. teneo, ere ‘hold’. Here?); ON pynja, v. “thin beside penja, tr. ‘stretch’; G dünnen, v. be- side dehnen, as ON; OCS tínjo, tiniti, v. tr. ‘pull out, thin out beside *tünükü ‘thin’; Cz. tenky, R tónkij, 1d. (vocalism uncertain); cf. (*ton- or *ton- in) OCS tonoto, n. ‘net, snare’ beside OCz. teneto, id.; Li. cf. tinstu, tinti, v. ‘swell; Latv. tinu, tit, v. ‘wind, ravel out
8034:W. blin, cf. OBr. pl. blinion ‘inert’, Gael. blian ‘lean, insipid’ etym. dub., perh. (fr. IE *mléno- or *mlino-): Skt. mlana- ‘faded, withered, exhausted, languid’, pple. of mla- ‘fade, wither, grow weary’, SCr. mlitav ‘tepid, list- less’, etc. fr. extensions of IE *mel- ‘rub, grind’ (Walde-P. 2.284 ff.). G.S. Lane, Language 13.21 f.
8092:dub., perh. as Gme. *hluja- : *hlew-g. in Du. lauw, OHG lao, NHG lay ‘tepid? etc., fr. IE *fleu-, extension of *foj. cH Lat. calidus ‘warm’, etc. Franck-y. W. 400 f. (372). Walde-P. 2.709 (1.480), Otherwise Falk-Torp 680.
21248:Lat. conlocdre, collocare (> It, collo- care, Sp. colocar; VLat. development in Fr. coucher, Rum. culca ‘put to bed? Ss colgar ‘hang’, REW 2052), epd. of locas deriv. of locus ‘place’ (12.11). . It. matter; Fr. mettre, fr. Lat. mittere let go’ (whence the usual but Secondary ‘send’), ‘throw’ (hastam, lapides, etc.) ‘put forth’ (radices, florem, etc.), in late Lat. ‘put forth, putin, put’. Cf. manum autem nemo mittit ad tangendum (Pere- grinatio), [ova] ut in tepida acqua mit- tantur (Anthimi de observatione ciborum epistula), mittis et modicum sale (Oriba- sius), etc. Ernout-M. 621. REW 5616.
24796:Tight? (15.82).
27253:The distinction according to the de- 2 of heat, as in NE hot, warm, holds for the Gme. and Balto-Slavie words. Most of the other words listed are used without such distinction, though there may be special words for ‘lukewarm, tepid’, which are not included.
```


## [2026-10-15T02:49:24.625Z] TOOL CALL #68: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe-private/site/pages/503.* 2>/dev/null; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && pdftoppm -f 503 -l 503 -r 200 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf pg503 && ls -la pg503.png"
}
```


### [2026-10-15T02:49:25.781Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   70k sfmqrb 14 Oct 22:15  /home/sfmqrb/git/rishe-private/site/pages/503.jpg
Permissions Size User   Date Modified Name
.rw-r--r--   82k sfmqrb 14 Oct 22:49  pg503.png
```


## [2026-10-15T02:49:27.665Z] TOOL CALL #69: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg503.png"
}
```


### [2026-10-15T02:49:28.060Z] TOOL RESULT

```

```


## [2026-10-15T02:49:28.057Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-15T02:49:33.609Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-503.json'));print(json.dumps(d['entries'][1],ensure_ascii=False)[:2500])\"; mkdir -p data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg503.png data/verification/sources/refs/ocr/BOOK/503.png"
}
```


### [2026-10-15T02:49:34.010Z] TOOL RESULT

```
{"root": {"name": "Tenk", "lang": "Indo-European", "refs": "POK:1068", "gloss": "to become firm and thick"}, "nodes": [{"id": 1, "parent": 0, "lang": "Avestan", "refs": "POK:1068; KLN:1617; MON5:405; BQT:511", "words": [{"translit": "tanj-išta", "gloss": "most pulled together, strongest", "script": null, "see": ["Isto"]}, {"translit": "taxma", "gloss": "pulled together, strong", "script": null}, {"translit": "taxma-tanu", "gloss": "(with) strong body", "script": null, "see": ["Ten 1"]}, {"translit": "taxma-urupa", "gloss": "(with) strong dogs", "script": null, "see": ["Wel 2"]}, {"translit": "raodha-taxma", "gloss": "grown strong", "script": null, "see": ["Leudh"]}], "script_extra": null, "note": null, "quote": null}, {"id": 2, "parent": 1, "lang": "Persian", "refs": "BQT:491,519,538; POK:1068", "words": [{"translit": "tang", "gloss": "tight", "script": "تَنگ"}, {"translit": "tanjîdan", "gloss": "to squeeze, pull", "script": "تَنجیدن ( تَرَنجید )"}, {"translit": "tahamtan", "gloss": "\"with strong body\"", "script": "تهمتن"}, {"translit": "Tahmŭras", "gloss": "\"with strong dogs\"", "script": "تهمورث"}, {"translit": "Rostam", "gloss": "\"grown strong\"", "script": "رُستم"}], "script_extra": null, "note": null, "quote": {"text": "بتنجید عذرا چو مردان جنگ - ترنجید بر بارگی تنگ تنگ", "poet": "Ferdowsî"}}, {"id": 3, "parent": 0, "lang": "Germanic", "refs": "AHD", "words": [{"translit": "thinhatz", "gloss": "tight", "script": null}, {"translit": "thangul", "gloss": "thick mass", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 4, "parent": 3, "lang": "English", "refs": null, "words": [{"translit": "tight, thick, tangle", "gloss": null, "script": null}], "script_extra": null, "note": null, "quote": null}]}
```


## [2026-10-15T02:49:37.746Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming; grep -n \"تپیدن\\|تابیدن\\|تافتن\" FFD/FFD_pages.txt | head -8; echo ---; grep -n \"^تنگ\\|^تب\\b\\|^تپیدن\\|^تابیدن\\|^تابستان\\|^شتافتن\\|^تهمتن\\|^تنجیدن\\|^پرتو\\|^آفتاب\" ARY/ARY_pages.txt | head -20"
}
```


### [2026-10-15T02:49:38.425Z] TOOL RESULT

```
1276:تافتن
1698:شتافتن
1702:در فارسی میانه 55131127 به معنی «فشارآوردن» و «اشتافتن» است.
---
52:تبایل ترکك زبان (از حدود سده‌ی پنج میلادی به بعد) موجب از میان رفتن آن زبانهای محلی گردیده
373:تبدیل به کشو رگشایان کوچگر شدند!
5947:تنگ (در براپر / ۲۰۳ ۱
```


## [2026-10-15T02:49:40.946Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming; sed -n 1270,1290p FFD/FFD_pages.txt; echo ----; sed -n 1692,1706p FFD/FFD_pages.txt; echo; head -n 1276 FFD/FFD_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1; echo ---; sed -n 5940,5960p ARY/ARY_pages.txt; head -n 5947 ARY/ARY_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1"
}
```


### [2026-10-15T02:49:41.278Z] TOOL RESULT

```
اصلی 13 است» 1 پیش از 1 به بدل شده است. 13 صورت بالاندةٌ 18 است» ريشهٌ 18
به معنی «دویدنْ» است و 131 به معنی «دوانیدن».
در فارسی میانه 133122 به معنی «دواندن» است.
تاز < فارسی میانه 132 < ایرانی باستان 130-۵*.برای 2 -> آرای. #به‌جای ‏ آمده است.
[pdf page 51]
وا فعلهای فارسی دری
تافتن
تافت < فارسی میانه 1 گرم کردن < ایرانی باستان ۴13۳-12 برای 18 -> آراست.
۱ 0 صورت اصاٍ است. « پیش از ۲ به 1 بدل شده است. 150 صورت بالاندة 1۸0
است» 130 به معنم «گرم‌شدن» است و 130 به معن «گرم کردن». «تفتن) از 130 آمده
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
----
صورت 7 درآمده است.
شایسترد
شایست < فارسی میانه 19ر52. 1 مادهٌ ماضی جعلی و از مادهٌ مضارع ساخته
شده است.
شای < فارسی میانه 33 < ایرانی باستان 8-ر۹83*. برای 2 -> آرای. 529« صورت
بالاندة ريشهٌ وهکدو آن به معنی «توآنابودن» است.
شتافتن
شتافت < فارسی میانه 53130» صورت کهنتر 2۳15130 + ایرانی باستان ۵01-3110 *
برای 18 -> آراست. 201 پیشوند فعلی است. ۰8130 صورت بالاندةٌ ريشهٌ ۰۶127 صورت
اصلی 131 است. 0 پیش از 1به ؟بدل شده است. ريشهٌ به معنی «فشار آوردن» است.
در فارسی میانه 55131127 به معنی «فشارآوردن» و «اشتافتن» است.
شتاب + فارسی میانه 053180» صورت کهنتر 2۳8130 + ایرانی باستان 201-8130-8*.
برای ۵ سه آرای.
شدن
شد < فارسی میانه 504 + ایرانی باستان 50-1۵*. برای 1۵ > آراست. 80 صورت

[pdf page 51]
---
اوستی (0535776): 6اه7 لانین (770۷ا): 5 ,5 آتآ:7182
کردی (00157): و الن ای فرانسه (ح/۳52): ت71
بلوچی (1ع/انله8) 71۸3۸۳ ببل۸ات7۸ اسپانیایی (52۸۸/1577): لد زان با
سانسکریت (8۸(7577): 7۸1 گرتیک (0077710): 1۳۸07۸3 :۱
7 ش1۸7۷ ,7۸71 ,1۸3105 ایسلندی کهن (/۸70707/140 صا0):
[pdf page 202]
۹ لگ
تنگ (در براپر / ۲۰۳ ۱
أً
ا
7 اسلراکی 81.07470): ,18۸ أ
نورس کهن (۸0782 010): الول )۷0۰ لیترانی ([777۸/142/.ا): 7۸85
فریزی کهن (/3140ل۲8 010): ۰ 71738388 لتونی (لتی) (/77740): ۰ 11808 ,115
آلمانی کهن ((057۸ 4ا0آل 0]20): ایرلندی کهن (لدلها صان): ,7۸۸
انا ال با
آلمانی (/057440): نا گالی (للدلالام0): 71
انگلیسی کهن (5لا2070 ۵1): 711۷۵ ولزی (8ا75): راد ناد و۷
انگلیسی (#ل5لرا8/0): 71310 برتونی (/81670): 0 ,7۸۸0
دانمارکی (0۸(7]57). 770
سوئدی (817580137): ۷۱ پسگشت‌ها 5
نروژی (۷0778014۷): 70 09ات۶0
[pdf page 202]
```


## [2026-10-15T02:52:19.160Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-503.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nPOK_TENK={\"ref\":\"POK:1068\",\"status\":\"supports\",\"note\":\"POK_full.txt line 85591 'Root / lemma: tenk-2 ... Meaning: to clot, thicken; solid, thick': 'Old Indie tanc- tanakti zieht together ... Avestan taxma- valiant, proficient, energetic, heldenhaft, compounds tąsyah-. Sup. tančišta-, np. tanjīdan zusammenziehen' (Page(s): 1068).\"}\nWLD_TENK={\"src\":\"WLD\",\"where\":\"Bd. I p.725 s.v. 2. tenk- (WLD_Bd1_pages.txt line 68445ff.)\",\"stance\":\"supports\",\"note\":\"'Ai. tanc-, tanákti zieht zusammen ... av. taxma- „tapfer, tüchtig, energisch, heldenhaft“, Komp. tąsyah-, Sup. tančišta-; np. tanjīdan „zusammenziehen“, arm. t'anjr „dicht, dick“'.\"}\nAHD_TENK={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. tenk-2 (AHD_watkins1985.txt line 1080)\",\"stance\":\"supports\",\"note\":\"'tenk-2. To become firm, curdle, thicken. 1. Suffixed form *tenk-to-, thickened, in Germanic *thinhtaz in Old Norse théttr, dense, watertight ... TIGHT. 2. Possibly suffixed o-grade form *tonk-lo- in Germanic *thangul- in Old Norse thöngull, seaweed (? < \\\"thick mass\\\"), akin to the source of TANGLE. [Pok. 2. tenk- 1068.]'\"}\nIEC_TENK={\"src\":\"IEC\",\"where\":\"s.v. tenk- (1) (IEC.txt line 18367)\",\"stance\":\"partial\",\"note\":\"Mann: 'tenk- (1) press, squeeze, cram ... Skt. tanákmi (contract); Av. cf. tañcišto, superl. very strong ... MHG cf. dihte, adj. tight, close'; under teng- he refers 'For Per. tang tight, narrow, see tonk-' — same family, different root-labelling.\"}\nPOK_TEP={\"ref\":\"POK:1069\",\"status\":\"supports\",\"note\":\"POK_full.txt line 85826 'Root / lemma: tep- Meaning: warm': 'Avestan tapaiti is warm, Kaus. tāpayeiti ... Inchoh. tafsaiti ... tafnu- Fieberhitze, fever, tafnah- heat; fever; np. taftan burn, warm, gleam, shine'; 'Latin tepeo -ere lukewarm sein, tepidus warm' (Page(s): 1069-1070).\"}\nWLD_TEP={\"src\":\"WLD\",\"where\":\"Bd. I p.718 s.v. tep- (WLD_Bd1_pages.txt line 67757)\",\"stance\":\"supports\",\"note\":\"'tep- „warm sein“. Ai. tápati ... av. tapaiti „ist warm“, Kaus. tāpayeiti „erwärmt, erhitzt“, Inkoh. tafsaiti „wird heiß“ ... tafnu- m. „Fieberhitze, Fieber“ ... np. taftan „brennen, wärmen, leuchten“'.\"}\nAHD_TEP={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. tep- (AHD_watkins1985.txt line 1080)\",\"stance\":\"supports\",\"note\":\"'tep-. To be warm. Suffixed (stative) form *tep-ē- in Latin tepēre, to be warm: TEPID. [Pok. tep- 1069.]'\"}\nIEC_TEP={\"src\":\"IEC\",\"where\":\"s.v. tep- (1) (IEC.txt line 18389)\",\"stance\":\"supports\",\"note\":\"'tep- (1) be warm; tepos heat. WP I, 719 ... Av. tap-, v. burn, glow, shine; Per. tabidan, inf. shine beside tafsidan grow warm ... Lat. tepeo'.\"}\nCH_TAP={\"src\":\"CHEUNG\",\"where\":\"p.378-379 s.v. *tap 'to warm up, heat' (CHEUNG.txt line 24669)\",\"stance\":\"supports\",\"note\":\"'YAv. tap- to be(come) hot ... BMP tʾp- /tāb-/ to heat, burn (up); shine; Inf. BMP tʾptn /tāftan/ ... NP tāftan/tāb- to shine, burn, NP tafsīdan ... NP tab fever, tāb heat ... (+ *abi-) NP āftāb sun(shine) ... PIE *tep- to be warm, hot | Pok. 1069'.\"}\nHRN372={\"src\":\"HRN\",\"where\":\"no. 372, p.83 s.v. tāften\",\"stance\":\"supports\",\"note\":\"'tāften brennen, wärmen, leuchten, Praes. tāb-em (vergl. āftāb, mahtāb) ... tābistān Sommer ... teb Fieber ... aw. tap-, tāpayeiti warm machen, tafnu- Hitze, Fieber ... phlv. tāftan ... tap Fieber'.\"}\nentries=[]\n# ---------- entry 1 Tenk\ne1={\"entry\":1,\"root\":\"Tenk\",\"verdict\":\"confirmed\",\n\"modern_form\":\"PIE *tenk- (Pokorny's 2. tenk-) 'to become firm, curdle, thicken; to pull together'\",\n\"note\":\"Pokorny 1068 (2. tenk- 'gerinnen, fest, dicht werden'), Walde-Pokorny I 725, Watkins/AHD tenk-2 'to become firm, curdle, thicken', Cheung *tanč 'to twist (together), become narrow, dense, constrict' < PIE *tenk- (LIV 625). Root, label and gloss correct. Cross-cutting problems on this chart: the Avestan box mixes attested words (taxma-, tančišta-, Taxma Urupi) with compounds that are not attested in Avestan (taxma-tanu, raodha-taxma); Germanic 'thinhatz' is Nourai's misprint for AHD's *thinhtaz; English 'thick' does not belong here (it is from PIE *tegu-); Rostam's second element is MP -stahm (< *staxma-), not taxma- directly.\",\n\"note_fa\":\"ریشهٔ هندواروپایی آغازین *tenk- «سفت و دَلَمه شدن، فشرده و انبوه شدن، به هم کشیدن» (پوکورنی ۱۰۶۸، والده‌ـپوکورنی ۱:۷۲۵، واتکینز tenk-2) درست است و چونگ نیز ستاک ایرانی *tanč «پیچاندن، تنگ و فشرده شدن» را از همین ریشه می‌داند. ادعای نورایی دربارهٔ خودِ ریشه درست است؛ اما در نمودار چند لغزش هست: برخی واژه‌های «اوستایی» ساختگی‌اند، thinhatz خطای چاپی به جای *thinhtaz است، و thick انگلیسی از ریشهٔ دیگری (*tegu-) است.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/tep-\"] and [],\n\"ref_check\":[POK_TENK],\n\"consulted\":[WLD_TENK,AHD_TENK,IEC_TENK,\n {\"src\":\"CHEUNG\",\"where\":\"p.377-378 s.v. *tanč (CHEUNG.txt line 24600ff.)\",\"stance\":\"supports\",\"note\":\"'*tanč to twist (together), become narrow, dense, constrict ... BMP tng /tang/ narrow ... NP tanjīdan/tanj- to squeeze; to twist, roll together; to draw tight ... NP tang ... PIE *tenk- (*temk-?) to twist together, pull oneself together, condense = LIV 625 | Pok. 1068'.\"}],\n\"nodes\":[]}\ne1[\"sources\"]=[W+\"تنجیدن\"]\ne1[\"nodes\"].append({\"id\":1,\"lang\":\"Avestan\",\"words\":\"tanj-išta; taxma; taxma-tanu; taxma-urupa; raodha-taxma\",\"verdict\":\"plausible\",\n\"derivation\":\"Attested: YAv. taxma- 'brave, strong, valiant' (Bartholomae col.626 'fortis, tapfer, tüchtig, energisch, heldenhaft'), from *tank-ma- 'pulled together, firm' (PIE *tenk-), with comparative tąsyah- and superlative tančišta- 'strongest' (the book's 'tanj-išta' is a variant spelling; Mann cites tañjištō), whose -č- shows the unaspirated root final before -išta-. Taxma Urupi (Bartholomae urupay- m., 'Taxmō Urupa', Yt 15.11, 19.28) is the Avestan name of the king later called Tahmūras; urupay- is a canine species ('Hundegeschlecht', perhaps fox), so 'with strong dogs' is an interpretation of an unclear name (Bartholomae: 'Eig. Bed.?'). By contrast taxma-tanu 'strong-bodied' and raodha-taxma 'grown strong' are not attested Avestan words: they are Nourai's back-projections of the New Persian compound tahamtan (tahm + tan) and of MP Rōdastahm (Rostam), whose second element is -stahm < *staxma-, a different (though similar) word. Hence the node as a whole is only plausible.\",\n\"derivation_fa\":\"در اوستا taxma- «دلیر، نیرومند، پهلوان» (بارتولومه ستون ۶۲۶) و صفت عالی آن tančišta- «نیرومندترین» به‌راستی هست و از ریشهٔ *tenk- «به هم کشیده و سفت شدن» است؛ نام Taxma Urupi (= تهمورث بعدی) نیز در یشت‌ها آمده، هرچند معنای urupi- (گونه‌ای سگ یا روباه) روشن نیست. اما taxma-tanu و raodha-taxma در اوستا گواهی نشده‌اند و نورایی آن‌ها را از «تهمتن» و «رستم» فارسی بازسازی کرده است؛ جزء دوم نام رستم در پهلوی stahm (از *staxma-) است نه taxma. پس ادعای نورایی برای taxma و tančišta درست و برای دو ترکیب دیگر تنها با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"تنگ\",W+\"رستم\",\"https://en.wikipedia.org/wiki/Tahmuras\"],\n\"ref_check\":[POK_TENK,\n {\"ref\":\"KLN:1617\",\"status\":\"partial\",\"note\":\"Klein 1966 s.v. tight (KLN_1966.txt line 39242): '... cogn. with Ir. techt curdled, Lith. tankus close, tight, Pers. tang tight, OI. tanakti draws together, contracts, fr. I.-E. base *tenq- to be thick or strong' — supports the root, does not list the Avestan words.\"},\n {\"ref\":\"MON5:405\",\"status\":\"not_checked\",\"note\":\"Mo'in vol. 5 (proper names, presumably s.v. Tahmūras/Rostam) is not among the local files (MON_part1/2 are the lexicon) and the a'lam volume is not on vajehyab.\"},\n {\"ref\":\"BQT:511\",\"status\":\"partial\",\"note\":\"BQT vol.1 OCR around printed p.511-520 (BQT_v1_pages.txt line 31094ff., Mo'in's footnote to تنگ): 'اوستا tančišta (صفت عالی از taxma بمعنی تهم و برومند)، پهلوی tang (ضیق) ... «هوبشمان ۳۹۸»' — supports taxma/tančišta; the compounds are not there.\"}],\n\"consulted\":[\n {\"src\":\"BRT\",\"where\":\"col. 626-627 s.v. taxma-, taxmō.tma-; col. 1533 s.v. urupay-; s.v. tančišta- (BRT.txt lines 11841, 11851, 11988, 25526)\",\"stance\":\"partial\",\"note\":\"'taxma- Adj. fortis, tapfer, tüchtig, energisch, heldenhaft'; 'tančišta- Adj. der tapferste, energischste'; 'urupay- m. Name einer Art des Hundegeschlechts'; 'urupay- m. EN. des zweiten iranischen Königs ... taxmō urupa ... Eig. Bed.? — Später Taxmūraf, Tahmūras genannt'. No *taxma-tanu or *raoδa-taxma listed.\"},\n WLD_TENK,\n {\"src\":\"NYB\",\"where\":\"vol. II glossary (NYB_vol2_glossary.txt line 3349)\",\"stance\":\"partial\",\"note\":\"'Rōtastahm [lwtsthm] n. pr. — NP Rustam; Old Sogd rwstmy' — second element -stahm, not taxma-.\"},\n {\"src\":\"HUB\",\"where\":\"p.~170 §(xm) (HUB.txt line 8993)\",\"stance\":\"supports\",\"note\":\"'tahm — taham stark (auch in Tahamtan von starkem Körper, Rustem's Beiname) zd. taxma-, ap. taxma- in Taxmaspāda- ... pers. tam in Rustam ... = phl. Rustahm aus *Rōtastahm?'\"}]})\ne1[\"nodes\"].append({\"id\":2,\"lang\":\"Persian\",\"words\":\"tang; tanjîdan; tahamtan; Tahmŭras; Rostam\",\"verdict\":\"plausible\",\n\"derivation\":\"tang 'narrow, tight' < MP tang [tng] (MacKenzie 'narrow, tight') < OIr. *tanka-/*tanč- (Cheung *tanč) < PIE *tenk-; Horn 398 and Hübschmann 398 put it beside Av. tančišta-, so confirmed. tanjīdan 'to squeeze, contract, pull tight' (with variant taranjīdan) is from the same *tanč- (Cheung; Wiktionary: borrowed from a NW-Iranian cognate of Manichaean MP tnz- 'to strain, press'); Horn 394 had linked it to Av. θanj- 'to pull', which Cheung explicitly rejects. tahamtan 'strong-bodied', Rostam's epithet, = tahm/taham 'strong' (MP tahm 'strong, brave' < Av. taxma-, -xm- > -hm-) + tan 'body' (Av. tanū-): confirmed. Tahmūras/Tahmūrath < MP Tahmōraf < Av. Taxma Urupi; the Arabic-script ث reflects an Arabicised spelling; the gloss 'with strong dogs' is speculative. Rostam < MP Rōdastahm/Rōtastahm, usually analysed as rōd/raod- 'growth, stature' (or 'river', per Wiktionary) + stahm 'strength, force' < *staxma- (cf. Av. staxra-); Hübschmann already compared tahm, but the attested -stahm makes Nourai's 'raodha-taxma' only an approximation.\",\n\"derivation_fa\":\"«تنگ» از پهلوی tang «تنگ، فشرده» و ایرانی باستان *tanč- از ریشهٔ هندواروپایی *tenk- است (هرن، هوبشمان، مکنزی، چونگ) و «تنجیدن/ترنجیدن» «فشردن، درهم کشیدن» نیز از همین ستاک است؛ هرن آن را به اوستایی θanj- «کشیدن» پیوند داده بود که چونگ نمی‌پذیرد. «تهمتن» از «تَهم» (پهلوی tahm، اوستایی taxma- «دلیر») + «تن» ساخته شده و «تهمورث» صورت معرّب‌گونهٔ نام اوستایی Taxma Urupi است. «رستم» از پهلوی Rōdastahm است که جزء دومش stahm «زور، نیرو» (از *staxma-) است؛ پس پیوند آن با taxma تنها با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"تنگ\",W+\"تنجیدن\",W+\"رستم\",\"https://en.wikipedia.org/wiki/Tahmuras\"],\n\"ref_check\":[\n {\"ref\":\"BQT:519\",\"status\":\"supports\",\"note\":\"BQT vol.1 leaf 748 (≈ printed p.520), Mo'in's footnote to تنگ (BQT_v1_pages.txt line 31094): 'اوستا tančišta (صفت عالی از taxma بمعنی تهم و برومند)، پهلوی tang (ضیق) ... ارمنی ... کردی ... بلوچی ... «اسشق ۳۹۸» «هوبشمان ۳۹۸»'.\"},\n {\"ref\":\"BQT:538\",\"status\":\"supports\",\"note\":\"BQT vol.1 leaves 766-767 (≈ p.538-539, lines 31994-32059): 'تهم ... شخصی را گویند که در بزرگی جثه ... عدیل و نظیر نداشته باشد و تهمتن مرکب ازین است'; 'تهمتن ... یکی از القاب رستم زال'; Mo'in fn.: 'در اوستا taxma' (OCR garbled); 'تهمورث - رك: تهمورس'.\"},\n {\"ref\":\"BQT:491\",\"status\":\"partial\",\"note\":\"BQT vol.1 leaf 719 (≈ p.491) has the headword 'ترنجیدن ... بمعنی سخت درهم کشیده و کوفته شدن' (line ~29790); Mo'in's footnote to تنجیدن (line 30956) says 'تنجیدن بمعنی کشیدن و بستن و آشامیدن، اوستا θanj-' following Horn, not *tenk-.\"},\n POK_TENK],\n\"consulted\":[\n {\"src\":\"HRN\",\"where\":\"no. 398 p.89 (tang), no. 394 p.88 (tanjīdan)\",\"stance\":\"partial\",\"note\":\"'398. teng enge. aw. tančišta- (Superl. von taxma- kräftig); phlv. tang eng' — supports; '394. tenjīden zusammenziehen; trinken. aw. θanj- ziehen' — a different root for tanjīdan.\"},\n {\"src\":\"HUB\",\"where\":\"no. 398 p.48-49\",\"stance\":\"supports\",\"note\":\"'Np. tang enge, bedrängt gehört zu tanjīdan zusammenziehen, auch angusto et aegro esse animo, skr. tanc' — and §xm: 'tahm — taham stark (auch in Tahamtan ...) zd. taxma-'.\"},\n {\"src\":\"PHD\",\"where\":\"s.v. tang, tahm, stahm (PHD_mackenzie.txt lines 4911, 623, 4663)\",\"stance\":\"supports\",\"note\":\"'tang [tng] narrow, tight'; 'tahm [thm] strong, brave'; 'stahm [sthm, N sitam] power, oppression' (the second element of Rōdastahm).\"},\n {\"src\":\"CHEUNG\",\"where\":\"p.377-378 s.v. *tanč\",\"stance\":\"supports\",\"note\":\"'NP tanjīdan/tanj- to squeeze; to twist, roll together; to draw tight ... NP tang ... narrow ... PIE *tenk-'; Cheung adds that Wa. tanz- etc. 'are unconnected with YAv. θanj- to pull' (against Horn).\"},\n {\"src\":\"NYB\",\"where\":\"vol. II glossary line 3349\",\"stance\":\"partial\",\"note\":\"'Rōtastahm [lwtsthm] n. pr. — NP Rustam'.\"},\n {\"src\":\"ARY\",\"where\":\"pdf page 202 (printed 203) s.v. تنگ\",\"stance\":\"supports\",\"note\":\"Entry 'تنگ' with a cognate table (Old Norse, Old Frisian, Old English, Lithuanian, Old Irish ...) — the tight/þéttr family; Latin-script forms are illegible in OCR.\"}]})\ne1[\"nodes\"].append({\"id\":3,\"lang\":\"Germanic\",\"words\":\"thinhatz; thangul\",\"verdict\":\"transcription_suspect\",\n\"derivation\":\"Proto-Germanic *þinhtaz 'dense, tight' < *tenk-to- (Watkins), with the regular Germanic change *-nk-t- > *-nh-t- (Grimm's law k > h before t, later nasal loss with lengthening: ON þéttr, MHG dīhte, G dicht). The book prints 'thinhatz', an impossible form (an extra a): Nourai's misprint of AHD's *thinhtaz; the extraction copies the page faithfully. *thangul- (o-grade *tonk-lo-) underlies ON þöngull 'seaweed stalk' and þang 'seaweed'; AHD itself glosses it '? < thick mass' and calls the link 'possible', so thangul is plausible.\",\n\"derivation_fa\":\"ژرمنی آغازین *þinhtaz «فشرده، تنگ» از *tenk-to- است (k پیش از t در ژرمنی به h بدل شده)؛ از آن نورس کهن þéttr و آلمانی dicht آمده‌اند. کتاب «thinhatz» چاپ کرده که خطای چاپی نورایی به جای *thinhtaz واتکینز است و استخراج داده درست است. *thangul- (نورس کهن þöngull «جلبک دریایی») را واتکینز تنها با تردید به این ریشه می‌برد؛ پس این بخش با احتیاط پذیرفتنی است.\",\n\"error_in\":\"book\",\"book_prints\":\"thinhatz\",\"correct_form\":\"*thinhtaz (Proto-Germanic *þinhtaz)\",\n\"sources\":[W+\"tight\",W+\"tangle\"],\n\"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. tenk-2: 'Germanic *thinhtaz in Old Norse théttr, dense, watertight ... TIGHT. 2. Possibly suffixed o-grade form *tonk-lo- in Germanic *thangul- in Old Norse thöngull, seaweed (? < \\\"thick mass\\\")' — confirms both forms and shows 'thinhatz' is a misprint.\"}],\n\"consulted\":[POK_TENK and {\"src\":\"POK\",\"where\":\"p.1068 s.v. tenk-2 (POK_full.txt line 85591)\",\"stance\":\"supports\",\"note\":\"'Old Icelandic þéttr dicht, MHG dīhte, NHG dicht (proto Germanic *þenxtu-) ... Old Icelandic þang, MLG dank seaweed, Tang' — both Germanic words under 2. tenk-.\"},\n {\"src\":\"KLN\",\"where\":\"1966 s.v. tight, tangle (lines 39242, 38141)\",\"stance\":\"supports\",\"note\":\"tight: 'of Scand. origin, cp. ON. þéttr ... rel. to MHG. dihte, G. dicht ... fr. I.-E. base *tenq-'; tangle: 'ME. tangilen ... fr. Dan. tang seaweed'.\"},\n WLD_TENK]})\ne1[\"nodes\"].append({\"id\":4,\"lang\":\"English\",\"words\":\"tight, thick, tangle\",\"verdict\":\"disputed\",\n\"derivation\":\"tight: ME thight/tight from ON þéttr (and an OE *þīht), < PGmc *þinhtaz < *tenk-to-; the initial t- for th- under Scandinavian influence (Klein, Wiktionary) — confirmed. tangle: ME tanglen, frequentative of a Scandinavian word for seaweed (Dan. tang, ON þang/þöngull 'seaweed'), 'to form a mass like seaweed' — plausible as Watkins (\\\"possibly\\\") traces it to *tonk-lo-. thick: OE þicce < PGmc *þekuz < PIE *tegu- 'thick' (Pokorny 1057, Watkins tegu-, Klein, Wiktionary) — NOT from *tenk-; Nourai seems to have been led by AHD's gloss 'thick mass' for *thangul-. Node verdict: disputed because of 'thick'.\",\n\"derivation_fa\":\"tight انگلیسی از انگلیسی میانه thight و نورس کهن þéttr و ژرمنی *þinhtaz از ریشهٔ *tenk- است (درست). tangle «درهم پیچیدن» از واژه‌ای اسکاندیناویایی به معنی «جلبک دریایی» (þang) است و با احتیاط به همین ریشه می‌رسد. اما thick از انگلیسی کهن þicce و ژرمنی *þekuz و ریشهٔ هندواروپایی دیگری *tegu- «کلفت» است (پوکورنی ۱۰۵۷، واتکینز، کلاین)؛ پس پژوهش امروزی این بخش از ادعای نورایی را رد می‌کند.\",\n\"sources\":[W+\"tight\",W+\"tangle\",W+\"thick\"],\n\"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the English box carries no reference; checked via the Germanic node's AHD instead: Watkins lists TIGHT and TANGLE under tenk-2 but THICK under 'tegu-. Thick. Germanic *thiku- in Old English thicce' (AHD_watkins1985.txt line 1072).\"}],\n\"consulted\":[\n {\"src\":\"KLN\",\"where\":\"1966 s.v. thick (line 39030), tight (39242), tangle (38141)\",\"stance\":\"partial\",\"note\":\"thick: 'ME. thicke, fr. OE. þicce ... fr. I.-E. base *tegu-, whence also OIr. tiug' (contradicts); tight: '... Pers. tang tight ... fr. I.-E. base *tenq-' (supports); tangle: 'fr. Dan. tang seaweed' (supports).\"},\n {\"src\":\"SKT\",\"where\":\"s.v. Tight, Tangle (SKT.txt lines 19715, 19157)\",\"stance\":\"partial\",\"note\":\"Tight: 'Icel. þéttr, tight ... Du. digt, G. dicht ... Cognate with L. tectus' (Skeat's old thatch-etymology, now abandoned); Tangle: 'frequentative verb from North. tang, sea-weed ... Icel. þöngull sea-weed'.\"},\n AHD_TENK]})\nentries.append(e1)\n# ---------- entry 3 Tep\ne3={\"entry\":3,\"root\":\"Tep\",\"verdict\":\"confirmed\",\"modern_form\":\"PIE *tep- 'to be warm, hot'\",\n\"note\":\"Pokorny 1069, Walde-Pokorny I 718, Watkins tep-, LIV 629f., Cheung *tap 'to warm up, heat'. Root, label and gloss correct. Problems lie in the second Avestan box: its 'Avestan' compounds are reconstructions, and šetāftan/aiwiš-tap belongs (per Nyberg, Cheung, Mo'in's own note and Abolghasemi) to *stap 'to hasten, press', not to *tep-; tapīdan's attachment is also doubtful.\",\n\"note_fa\":\"ریشهٔ هندواروپایی آغازین *tep- «گرم بودن، گرم شدن» (پوکورنی ۱۰۶۹، واتکینز، چونگ *tap) درست است و ادعای نورایی دربارهٔ ریشه پذیرفته است. اما «شتافتن» را پژوهش امروزی (نیبرگ، چونگ، ابوالقاسمی و خود معین) از ریشهٔ دیگری (*stap «شتاباندن، فشار آوردن») می‌داند و پیوند «تپیدن» با این ریشه نیز قطعی نیست.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/tep-\"],\n\"ref_check\":[POK_TEP],\"consulted\":[WLD_TEP,AHD_TEP,IEC_TEP,CH_TAP],\"nodes\":[]}\ne3[\"nodes\"].append({\"id\":1,\"lang\":\"Avestan\",\"words\":\"tap 2, tab\",\"verdict\":\"confirmed\",\n\"derivation\":\"YAv. tap- 'to be(come) hot' (Cheung; Bartholomae), caus. tāpaiieiti 'warms', inchoative tafsaiti 'becomes hot', ppp. tapta-, nouns tafnu- 'fever-heat' and tafnah- 'heat, fever' — the regular Indo-Iranian continuation of PIE *tep- (PIE *e > Iranian a; *p kept, spirantised to f before n, s, t). 'tab' is the later (Middle/New Persian) shape of the same stem, with intervocalic/final -p- > -b-; as an Avestan citation it is loose but the identity is right.\",\n\"derivation_fa\":\"در اوستا ستاک tap- «گرم شدن»، سببی tāpaya- «گرم کردن»، آغازی tafs- «داغ شدن» و اسم tafnu- «تب، گرمای تب» هست که همه از ریشهٔ هندواروپایی *tep- اند (e به a بدل شده و p پیش از n و s و t به f). صورت «tab» در واقع صورت فارسی میانه/نو همین ستاک است. ادعای نورایی درست است (پوکورنی، بارتولومه، چونگ).\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/tep-\"],\n\"ref_check\":[POK_TEP,{\"ref\":\"KLN:1589\",\"status\":\"supports\",\"note\":\"Klein 1966 s.v. tepid (KLN_1966.txt lines 38621-38622): 'L. tepidus, fr. tepere ... cogn. with OI. tápati makes warm, heats, burns ... Avestic tafnush fever'.\"}],\n\"consulted\":[{\"src\":\"BRT\",\"where\":\"col. ~637 s.v. tafnah-, tafnav- (BRT.txt lines 11926, 7136)\",\"stance\":\"supports\",\"note\":\"'tafnah- n. 1) Hitze, Glut 2) Fieberhitze'; 'tafnav- m. Plur. Feuergluten sva. Fieberanfälle'.\"},CH_TAP,WLD_TEP]})\ne3[\"nodes\"].append({\"id\":2,\"lang\":\"Persian\",\"words\":\"tab; tâbîdan; tapîdan\",\"verdict\":\"plausible\",\n\"derivation\":\"tab 'fever' < MP tab [tp] 'fever' (MacKenzie) < OIr. *tapa-/*tafnu- < PIE *tep(os)- (Wiktionary; Horn 372) — confirmed; tāb/tābe 'heat, frying-pan' are the long-grade/causative derivatives. tābīdan 'to shine, heat' (= tāftan, tāb-) < MP tābīdan/tāftan 'heat, burn; shine' < caus. *tāpaya- (Av. tāpaiieiti), ā by causative vṛddhi, -p- > -b- (Cheung, MacKenzie, Abolghasemi) — confirmed; the extra list tāftan, taftan, tafsīdan, taft is also correct (tafsīdan < inchoative *tafsa-). tapīdan 'to throb, palpitate' is not secured: Mann puts it under a separate *tep- (2) 'knock, beat' with OE þefian 'pant', Wiktionary marks it as possibly onomatopoeic, and Cheung lists no tapīdan under *tap; the semantic bridge 'be agitated with heat' is possible but unproven.\",\n\"derivation_fa\":\"«تب» از پهلوی tab «تب» و ایرانی باستان *tapa- از ریشهٔ *tep- است، و «تابیدن/تافتن» «گرم کردن، درخشیدن» از ستاک سببی *tāpaya- (اوستایی tāpayeiti) با بلند شدن واکه و ابدال p به b آمده است؛ «تفتن، تفسیدن، تفت» نیز از همین ریشه‌اند (هرن، مکنزی، چونگ، ابوالقاسمی). اما «تپیدن» «لرزیدن و زدن دل» را مان از ریشهٔ جداگانهٔ *tep- «کوبیدن» می‌داند و ویکی‌واژه احتمال نام‌آوایی بودنش را می‌دهد؛ پس پیوند آن تنها با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"تب\",W+\"تپیدن\",W+\"تابیدن\"],\n\"ref_check\":[{\"ref\":\"FFD:46\",\"status\":\"supports\",\"note\":\"Abolghasemi FFD_pages.txt [pdf page 51] (≈ printed p.46) s.v. تافتن: 'تافت < فارسی میانه taft گرم کردن < ایرانی باستان *tap-ta- ... تفتن از tap آمده است -> تفتن، تفسیدن. تاب < فارسی میانه tāb < ایرانی باستان *tāpaya-' (Latin forms garbled in OCR).\"},\n {\"ref\":\"HRN\",\"status\":\"supports\",\"note\":\"Horn no. 372 p.83: 'tāften brennen, wärmen, leuchten, Praes. tāb-em ... teb Fieber ... aw. tap-, tāpayeiti, tafnu- Hitze, Fieber; phlv. tāftan ... tap Fieber' — tab and tābīdan; tapīdan not mentioned.\"},\n {\"ref\":\"BQT\",\"status\":\"partial\",\"note\":\"BQT vol.1 (BQT_v1_pages.txt line 28728ff.): 'تبش ... گرما و گرمی را گویند - و مخفف تابش هم هست که فروغ و پرتو باشد'; line 28827 'از تپیدن' — tapīdan listed without an etymology linking it to tab.\"}],\n\"consulted\":[CH_TAP,\n {\"src\":\"PHD\",\"where\":\"s.v. tab, tābīdan, tāftan (PHD_mackenzie.txt lines 4864-4880)\",\"stance\":\"supports\",\"note\":\"'tab [tp] fever'; 'tābīdan [tʾpytn] = tāftan'; 'tāftan, tāb- [tʾp-tn] heat, burn; shine'.\"},\n {\"src\":\"IEC\",\"where\":\"s.v. tep- (1) and tep- (2) (lines 18389, 18392)\",\"stance\":\"partial\",\"note\":\"'tep- (1) be warm ... Per. tabidan shine beside tafsidan grow warm' (supports tābīdan); 'tep- (2) knock, tap, beat. Per. tapidan, inf. palpitate ... OE þefian palpitate, pant' (contradicts placing tapīdan under 'be warm').\"},HRN372]})\ne3[\"nodes\"].append({\"id\":3,\"lang\":\"Avestan\",\"words\":\"tab-stana; ap-tab; mâh-tab; para-tab; aiwiš-tap\",\"verdict\":\"disputed\",\n\"derivation\":\"None of these is an attested Avestan word; they are Old Iranian reconstructions of Persian compounds. tab-stāna 'place/time of heat' > MP tābestān (Wiktionary) is a sound analysis (*tāpa- + -stāna-). ap-tab: MP āftāb, Parthian ʾbdʾb 'sunshine', from *abi-tāpa- (Cheung, Wiktionary), i.e. the preverb abi- 'towards' + tāp- 'shine', not Nourai's 'heat-emitting glitter' with āb 'brightness' (Horn's and Mo'in's view) — plausible as to the tap- element. māh-tāb is a purely New Persian compound (māh 'moon' + tāb), not Avestan. para-tab > partaw 'ray' (Horn 296 para + tap; Hübschmann notes the irregular t) — plausible. aiwiš-tap 'in heat, in hurry' for šitāftan follows Horn 777 (*aiwiš + tap, 'figurative'), but Nyberg, Cheung (*stap 'to hasten, oppress', MMP ʾwystʾb-, Arm. LW stapem) and Mo'in's own footnote derive it from *abi-štāp-; this item is therefore disputed.\",\n\"derivation_fa\":\"این ترکیب‌ها در متن اوستا گواهی نشده‌اند و بازسازی‌هایی ایرانی باستان برای واژه‌های فارسی‌اند. «تابستان» از *tāpa-stāna- و «پرتو» از *para-tāpa- (هرن) پذیرفتنی‌اند؛ «آفتاب» را چونگ و ویکی‌واژه از *abi-tāpa- (پیشوند abi- + تاب) می‌دانند، نه «آب = درخشش» + تاب؛ «مهتاب» ترکیبی فارسی نو است. اما *aiwiš-tap برای «شتافتن» از هرن است و نیبرگ، چونگ و معین آن را از ریشهٔ دیگر *stap «شتاباندن، فشار آوردن» (پهلوی awištāftan/ōštāftan) می‌دانند؛ پس این بخش را پژوهش امروزی رد می‌کند.\",\n\"sources\":[W+\"تابستان\",W+\"آفتاب\",W+\"پرتو\",W+\"شتافتن\"],\n\"ref_check\":[\n {\"ref\":\"BQT:49\",\"status\":\"partial\",\"note\":\"BQT vol.1 leaf 259 (≈ p.49), Mo'in's footnote to آفتاب: 'پهلوی āftāb ... مرکب از آف + تاب. آف در اینجا بمعنی روشنی و درخشندگی است و تاب از تابیدن بمعنی گرم کردن است ... اینکه در فرهنگها معنی ترکیبی آنرا «آفت آب» نوشته‌اند مبتنی بر فقه اللغهٔ عامیانه است' — supports tāb-, but not an Avestan *ap-tab.\"},\n {\"ref\":\"BQT:1252\",\"status\":\"contradicts\",\"note\":\"BQT p.1252 (vol.3) vision transcript ocr/BQT/1252: 'شتافتن ... پهلوی ôshtâftan (عجله کردن) رك: اسشق - هوبشمان ۷۷۷؛ در اوراق مانوی تورفان 'wysht'b = avishtâb، ایرانی باستان *abi-shtâpayati، ارمنی shtap ... «نیبرگ ۱۶۶»' — *stāp, not aiwiš-tap.\"},\n {\"ref\":\"BQT:1958\",\"status\":\"supports\",\"note\":\"BQT vol.4 pdf page 41 (≈ p.1958) via tools/ref_page.py: 'ماهتاب پرتو ماه را گویند' with footnote 'مهتاب (مخفف) از: ماه + تاب (گرمی، نور) لغة بمعنی نور ماه' — a Persian compound (no Avestan form).\"},\n {\"ref\":\"BQT:453\",\"status\":\"not_checked\",\"note\":\"vol.1 page ~453 (leaf ~675) not read; the tābestān/partaw entries were checked in Horn and Wiktionary instead.\"}],\n\"consulted\":[\n {\"src\":\"HRN\",\"where\":\"no. 37 p.11 (āftāb), no. 296 p.69 (pertew), no. 372 p.83 (tābistān, mahtāb), no. 777 p.171 (šitāften)\",\"stance\":\"partial\",\"note\":\"'37. āftāb Sonne ... skr. abhā + tapa-' ; '296. pertew Glanz. para + tap-'; '372 ... (vergl. āftāb, mahtāb) ... tābistān Sommer'; '777. šitāften eilen ... phlv. ōstaftan ... aw. *aiwiš + tap-, tāpayeiti in Wärme, Hitze bringen, dann tropisch' — Horn is the source of Nourai's aiwiš-tap.\"},\n {\"src\":\"CHEUNG\",\"where\":\"s.v. *tap (p.379) and *stap (CHEUNG.txt line 23705)\",\"stance\":\"contradicts\",\"note\":\"under *tap: '(+ *abi-) NP āftāb sun(shine)', Parthian '*bdʾb sunshine'; under *stap 'to hasten, (op)press': '(+ *abi-) MMP ʾwystʾb- ... to (op)press; hasten ... NWIR: NP šitāftan/šitāb- to hurry; Arm. (LW) stapem I oppress, štap haste'.\"},\n {\"src\":\"HUB\",\"where\":\"no. 296 p.38\",\"stance\":\"partial\",\"note\":\"'Np. partav Licht, Strahl ... mit auffälligem t für d, Anlehnung an tāb, tāftan etc.?'\"},\n {\"src\":\"FFD\",\"where\":\"pdf page ~74 s.v. شتافتن (FFD_pages.txt line 1698)\",\"stance\":\"contradicts\",\"note\":\"'شتافت < فارسی میانه ... صورت کهنتر ... < ایرانی باستان *...-stāp- ... ريشه به معنی «فشار آوردن» است. در فارسی میانه ... به معنی «فشار آوردن» و «اشتافتن» است'.\"}]})\ne3[\"nodes\"].append({\"id\":4,\"lang\":\"Persian\",\"words\":\"tâbestân; âftâb; mahtâb; parto; šetâftan\",\"verdict\":\"disputed\",\n\"derivation\":\"tābestān 'summer' < MP tābestān [tʾpstʾn] = tāb 'heat' + -estān 'place/time' (Wiktionary, Horn 372) — confirmed. āftāb 'sun' < MP āftāb [ʾptʾb] 'sunshine', Parthian ʾbdʾb, < *abi-tāpa- (Cheung, Wiktionary) — confirmed as a tap- derivative (the first element is the preverb, not āb). mahtāb 'moonlight' = māh 'moon' + tāb (Wiktionary; Mo'in) — confirmed. parto/partaw 'ray, light' < *para-/pari-tāpa- (Horn 296; Wiktionary: second element from *tep-) — confirmed, with Hübschmann's caveat on the unvoiced t. šetāftan/šitāb 'to hurry' < MP ōštāftan, older awištāftan, Manichaean ʾwyštʾb- 'to press, hasten' < *abi-štāpaya- from *stap 'to hasten, press' (Cheung, Nyberg, Mo'in, Abolghasemi; Wiktionary) — not from *tep-; disputed.\",\n\"derivation_fa\":\"«تابستان» از پهلوی tābestān (تاب «گرما» + پسوند -ستان) و «آفتاب» از پهلوی āftāb و ایرانی باستان *abi-tāpa- است؛ «مهتاب» از ماه + تاب و «پرتو» از *para-tāpa- است و همه به ریشهٔ *tep- می‌رسند (هرن، معین، چونگ، ویکی‌واژه). اما «شتافتن/شتاب» از پهلوی awištāftan > ōštāftan و ایرانی باستان *abi-štāpaya- از ریشهٔ *stap «شتاباندن، فشار آوردن» است (نیبرگ، چونگ، ابوالقاسمی و حاشیهٔ معین)؛ پس پژوهش امروزی این یک واژه را از این ریشه نمی‌داند.\",\n\"sources\":[W+\"تابستان\",W+\"آفتاب\",W+\"مهتاب\",W+\"پرتو\",W+\"شتافتن\"],\n\"ref_check\":[\n {\"ref\":\"HRN\",\"status\":\"partial\",\"note\":\"Horn no. 372 ('tābistān Sommer', 'vergl. āftāb, mahtāb'), no. 296 ('pertew Glanz. para + tap-'), no. 37 ('āftāb Sonne') support four words; no. 777 derives šitāften from '*aiwiš + tap-', the view now rejected.\"},\n {\"ref\":\"BQT\",\"status\":\"partial\",\"note\":\"Mo'in's footnotes: آفتاب (BQT p.49) 'آف + تاب ... تاب از تابیدن' supports; مهتاب (p.1958) 'ماه + تاب' supports; شتافتن (p.1252) 'پهلوی ôshtâftan ... ایرانی باستان *abi-shtâpayati' contradicts the tep- link.\"}],\n\"consulted\":[HRN372,\n {\"src\":\"CHEUNG\",\"where\":\"s.v. *tap and *stap\",\"stance\":\"partial\",\"note\":\"'(+ *abi-) NP āftāb sun(shine)' under *tap; 'NP šitāftan/šitāb- to hurry' under *stap 'to hasten, (op)press'.\"},\n {\"src\":\"PHD\",\"where\":\"English index 'oppress awistaftan' (PHD_mackenzie.txt line 7187)\",\"stance\":\"contradicts\",\"note\":\"MacKenzie's awištāftan 'oppress', the MP ancestor of šitāftan, belongs to *stap, not *tap.\"},\n {\"src\":\"HUB\",\"where\":\"no. 296 p.38\",\"stance\":\"partial\",\"note\":\"'Np. partav Licht, Strahl ... mit auffälligem t für d, Anlehnung an tāb, tāftan etc.?'\"},\n {\"src\":\"FFD\",\"where\":\"s.v. شتافتن (line 1698)\",\"stance\":\"contradicts\",\"note\":\"'ريشه به معنی «فشار آوردن» است' — *stap.\"}]})\ne3[\"nodes\"].append({\"id\":5,\"lang\":\"Sogdian\",\"words\":\"âtp`k\",\"verdict\":\"confirmed\",\n\"derivation\":\"Buddhist Sogdian ʾtpʾk /ātpak/ 'heat(?)' (Gharib no. 291), analysed by Gharib as < *ā-tāpaka-, cf. Av. ā-tāpaiti: the preverb ā- + the *tap- stem with the -aka- suffix; Cheung also lists CSogd. ʾʾtpn 'furnace' (+ *ā-) under *tap. The form and gloss match; Gharib marks the meaning with a query.\",\n\"derivation_fa\":\"سغدی بودایی ʾtpʾk (ātpak) «گرما» (قریب، شمارهٔ ۲۹۱) از *ā-tāpaka- (پیشوند ā- + ستاک tap- + پسوند -aka) است و با اوستایی ā-tāpaiti هم‌ریشه است؛ چونگ نیز ʾʾtpn «کوره» را از همین ریشه می‌آورد. ادعای نورایی درست است، هرچند قریب معنی را با نشان پرسش آورده است.\",\n\"sources\":[],\n\"ref_check\":[{\"ref\":\"SOD:11\",\"status\":\"supports\",\"note\":\"Gharib SOD_pages.txt line 4601-4604 (entry 291, early pages of the dictionary, consistent with p.11): '291 ʾtpʾk B ... atpak < *a-tāpaka-, Av. a-tapaite ... heat ?'.\"}],\n\"consulted\":[CH_TAP,{\"src\":\"SOD\",\"where\":\"English index 'heat 291, 4263' (SOD_pages.txt line 38519)\",\"stance\":\"supports\",\"note\":\"index lists entry 291 (ʾtpʾk) under 'heat'.\"}]})\ne3[\"nodes\"].append({\"id\":6,\"lang\":\"Latin\",\"words\":\"tepěre\",\"verdict\":\"confirmed\",\n\"derivation\":\"Latin tepēre 'to be (luke)warm' is the stative *tep-ē- of PIE *tep- (Watkins), with tepor 'warmth', tepidus 'lukewarm', inchoative tepēscere (= Av. tafs-); de Vaan s.v. tepeō (cited on Wiktionary).\",\n\"derivation_fa\":\"لاتین tepēre «ولرم بودن، گرم بودن» ستاک حالتی *tep-ē- از ریشهٔ هندواروپایی *tep- است و tepor «گرما» و tepidus «ولرم» از آن‌اند؛ هم‌ریشه با اوستایی tap- و فارسی تاب و تب. ادعای نورایی درست است.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/tep-\",W+\"tepid\"],\n\"ref_check\":[{\"ref\":\"KLN:1589\",\"status\":\"supports\",\"note\":\"Klein 1966 s.v. tepid (line 38621): 'L. tepidus, fr. tepere to be warm or lukewarm, which is cogn. with OI. tápati ...'.\"}],\n\"consulted\":[AHD_TEP,POK_TEP and {\"src\":\"POK\",\"where\":\"p.1069\",\"stance\":\"supports\",\"note\":\"'Latin tepeo -ere lukewarm sein, tepidus warm, tepor warmth'.\"},WLD_TEP]})\ne3[\"nodes\"].append({\"id\":7,\"lang\":\"English\",\"words\":\"tepid\",\"verdict\":\"confirmed\",\n\"derivation\":\"English tepid (late ME, c.1400) < Latin tepidus 'lukewarm', adjective in -idus from tepēre (Klein, Wiktionary, Watkins TEPID under tep-).\",\n\"derivation_fa\":\"انگلیسی tepid «ولرم» از لاتین tepidus، صفتی با پسوند -idus از tepēre «گرم بودن»، در اواخر انگلیسی میانه وام گرفته شده است. ادعای نورایی درست است.\",\n\"sources\":[W+\"tepid\"],\n\"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference on the English box; covered by KLN:1589 on the Latin node.\"}],\n\"consulted\":[{\"src\":\"KLN\",\"where\":\"1966 s.v. tepid\",\"stance\":\"supports\",\"note\":\"'tepid, adj., moderately warm, lukewarm. — L. tepidus, fr. tepere'.\"},\n {\"src\":\"SKT\",\"where\":\"s.v. Tepid (line 19405)\",\"stance\":\"supports\",\"note\":\"'Tepid. (L.) L. tepidus, ... tepere, to be warm'.\"}]})\nentries.append(e3)\nout={\"pdf_page\":503,\"book_page\":473,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-14\",\"entries\":entries}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-503.json\",\"w\"),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-503.py && cd /home/sfmqrb/git/rishe-private && python3 -m json.tool data/verification/page-503.json >/dev/null && python3 tools/verify_check.py 503"
}
```


### [2026-10-15T02:52:19.900Z] TOOL RESULT

```
nodes verified: 11/11
node verdicts: {'plausible': 3, 'transcription_suspect': 1, 'disputed': 3, 'confirmed': 4}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 12, 'partial': 7, 'not_checked': 4, 'contradicts': 1}
books consulted: {'partial': 11, 'supports': 24, 'contradicts': 4} | by book: {'CHEUNG': 6, 'WLD': 4, 'HUB': 4, 'HRN': 4, 'PHD': 3, 'KLN': 3, 'BRT': 2, 'NYB': 2, 'POK': 2, 'SKT': 2, 'AHD': 2, 'FFD': 2, 'ARY': 1, 'IEC': 1, 'SOD': 1}
```


## [2026-10-15T02:52:30.445Z] AGENT

I wrote the page 503 verification file and ran the checker: 0 PROBLEM lines, and all 11 nodes are covered (the two redirect entries, Tengh and Tenu, are skipped).

**Page 503 (book p. 473):** both roots, Tenk and Tep, are `confirmed`. Nodes: 4 confirmed, 3 plausible, 3 disputed, 1 transcription_suspect.

**Disputed:**
- **Tenk #4, English "tight, thick, tangle":** "thick" comes from a different root, PIE *tegu- (Pokorny 1057, Watkins, Klein). "tight" is confirmed and "tangle" is plausible.
- **Tep #3, Avestan "aiwiš-tap" (and the rest of that box):** the Avestan label is loose, since these are reconstructed compounds that don't appear in Avestan texts. The "aiwiš-tap" origin of šetāftan comes from Horn 777. Nyberg, Cheung, Abolghasemi and Mo'in's own footnote (BQT:1252) instead derive it from *abi-štāp-, root *stap 'to hasten, press'.
- **Tep #4, Persian "šetâftan":** same problem. It goes back to Middle Persian awištāftan/ōštāftan from *stap, not *tep-. The other four words in this box (tābestān, āftāb, mahtāb, parto) are confirmed.

**Transcription_suspect:**
- **Tenk #3, Germanic "thinhatz":** the printed book shows "thinhatz", which is Nourai's misprint for Watkins' *thinhtaz. The fault is in the book, not the extraction. I saved the page image as `data/verification/sources/refs/ocr/BOOK/503.png`.

**Plausible, worth knowing:**
- Tenk #1: "taxma-tanu" and "raodha-taxma" are not found in Avestan.
- Tenk #2: Rostam goes back to Middle Persian Rōdastahm, whose second part is -stahm (< *staxma-), not taxma- directly.
- Tep #2: tapīdan is doubtful. Mann puts it under a separate root, *tep- 'beat', and Wiktionary suggests it may be imitative.

**Extraction errors:** none. The JSON matches the printed page, including the Ferdowsi quote.

Three of Nourai's references could not be checked: MON5:405 (Mo'in's proper-names volume isn't available locally), BQT:453 (that page wasn't read), and the English boxes, which cite nothing. Four web fetches failed (the Etymonline pages and the Iranica articles), so I left them out of the `sources` lists.

Files are in /home/sfmqrb/git/rishe-private/data/verification:
- page-503.json
- sources/refs/ocr/BOOK/503.png


## [2026-10-15T02:52:30.480Z] INPUT

[handback-send-enforce] Your report has not been delivered. Call SubagentHandback({message: <your full report>}) now; the call ends your run.


## [2026-10-15T02:52:38.300Z] TOOL CALL #74: SubagentHandback

```json
{
 "message": "I wrote the page 503 verification file and ran the checker: 0 PROBLEM lines, and all 11 nodes are covered (the two redirect entries, Tengh and Tenu, are skipped).\n\n**Page 503 (book p. 473):** both roots, Tenk and Tep, are `confirmed`. Nodes: 4 confirmed, 3 plausible, 3 disputed, 1 transcription_suspect.\n\n**Disputed:**\n- **Tenk #4, English \"tight, thick, tangle\":** \"thick\" comes from a different root, PIE *tegu- (Pokorny 1057, Watkins, Klein). \"tight\" is confirmed and \"tangle\" is plausible.\n- **Tep #3, Avestan \"aiwiš-tap\" (and the rest of that box):** the Avestan label is loose, since these are reconstructed compounds that don't appear in Avestan texts. The \"aiwiš-tap\" origin of šetāftan comes from Horn 777. Nyberg, Cheung, Abolghasemi and Mo'in's own footnote (BQT:1252) instead derive it from *abi-štāp-, root *stap 'to hasten, press'.\n- **Tep #4, Persian \"šetâftan\":** same problem. It goes back to Middle Persian awištāftan/ōštāftan from *stap, not *tep-. The other four words in this box (tābestān, āftāb, mahtāb, parto) are confirmed.\n\n**Transcription_suspect:**\n- **Tenk #3, Germanic \"thinhatz\":** the printed book shows \"thinhatz\", which is Nourai's misprint for Watkins' *thinhtaz. The fault is in the book, not the extraction. I saved the page image as `data/verification/sources/refs/ocr/BOOK/503.png`.\n\n**Plausible, worth knowing:**\n- Tenk #1: \"taxma-tanu\" and \"raodha-taxma\" are not found in Avestan.\n- Tenk #2: Rostam goes back to Middle Persian Rōdastahm, whose second part is -stahm (< *staxma-), not taxma- directly.\n- Tep #2: tapīdan is doubtful. Mann puts it under a separate root, *tep- 'beat', and Wiktionary suggests it may be imitative.\n\n**Extraction errors:** none. The JSON matches the printed page, including the Ferdowsi quote.\n\nThree of Nourai's references could not be checked: MON5:405 (Mo'in's proper-names volume isn't available locally), BQT:453 (that page wasn't read), and the English boxes, which cite nothing. Four web fetches failed (the Etymonline pages and the Iranica articles), so I left them out of the `sources` lists.\n\nFiles are in /home/sfmqrb/git/rishe-private/data/verification:\n- page-503.json\n- sources/refs/ocr/BOOK/503.png"
}
```


### [2026-10-15T02:52:38.676Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
