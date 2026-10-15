# Verification process log — verify-page-505


## [2026-10-15T02:44:16.251Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 505 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-505.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-505.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-505.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 505` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.294Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.557Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.633Z] TOOL RESULT

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


## [2026-10-15T02:44:21.501Z] TOOL CALL #2: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/agent/charts/page-505.txt; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; ls data/verification/page-50*.json"
}
```


### [2026-10-15T02:44:21.886Z] TOOL RESULT

```
=== PDF page 505 (book page 475) ===
--- entry 0 ---
ROOT [Indo-European] Ter 3, Tar : a kinship term, a suffix indicating someone who performs the action indicated by the root verb  (refs PRT:863; KAS:10; POK:369; AHD:1500)
#1 (parent #0) [Indo-European] refs=POK; SYN:103-107 | Mâ-ter : feeder (of the family) ☞Mâ ; Pa-ter : protector/ feeder (of the family) ☞Pa ; Dhugh-tar : milker (of the family) ☞Dheugh ; Bhra-ter : load carrier (of the family) ☞Bher 1 ; Geme-tar : married (to the family) ☞Geme
  #2 (parent #1) [Avestan] refs=KLN; SYN:103-107 | mâ-tar : mother ; pi-tar : father ; duğ-dâr : daughter ; brâ-tar : brother ; zâmâ-tar : son-in-law
    #3 (parent #2) [Persian] refs=BQT | mâdar «مادر» : "feeder", mother ; pedar «پدر» : "protector", father ; doxtar «دختر» : "milker", sister ; barâdar «برادر» : "load carrier" brother ; dâmâd «داماد» : "married", in-law
  #4 (parent #1) [Germanic] refs=AHD | môthar, fadar, dohter, brôthar
    #5 (parent #4) [English] refs=AHD | mother, father, daughter, brother
--- entry 1 ---
ROOT [Indo-European] Terp, Trep 2, Trp : to satisfy  (refs POK:1077; KLN:1592)
#1 (parent #0) [Avestan] refs=POK:1077; KLN:1592 | thrafza, thrafda : satisfied ; tarep : to steal
  #2 (parent #1) [Persian] refs=POK:1077 | tulf «تولف» : fully satisfied (obsolete)
  #3 (parent #1) [Pahlavi] refs=POK:1077 | tirft : theft
#4 (parent #0) [Sogdian] refs=POK:1077; SOD:125 | cft, cf : to steal ; cftu : stolen
#5 (parent #0) [Sanskrit] refs=POK:1077 | trpti : satisfied
#6 (parent #0) [Greek] refs=POK:1077; AHD | terpo : to fill, satisfy
  #7 (parent #6) [Latin] refs=POK:1077 | terpsi-chorě : satisfaction from dancing
    #8 (parent #7) [English] refs=AHD; KLN:1592 | terpsichore, euterp
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
Permissions Size User   Date Modified Name
.rw-r--r--   69k sfmqrb 14 Oct 22:14  data/verification/page-50.json
```


## [2026-10-15T02:44:23.681Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls data/verification/ | grep page-49 ; sed -n 1,200p tools/verify_check.py; cat data/extracted/batch/page-505.json | head -c 3000"
}
```


### [2026-10-15T02:44:24.156Z] TOOL RESULT

```
.rw-r--r--   68k sfmqrb 14 Oct 22:14  page-49.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-490.json
.rw-r--r--   55k sfmqrb 14 Oct 22:14  page-491.json
.rw-r--r--   70k sfmqrb 14 Oct 22:14  page-492.json
.rw-r--r--   68k sfmqrb 14 Oct 22:14  page-493.json
.rw-r--r--   62k sfmqrb 14 Oct 22:14  page-494.json
.rw-r--r--   60k sfmqrb 14 Oct 22:14  page-495.json
.rw-r--r--   66k sfmqrb 14 Oct 22:14  page-496.json
.rw-r--r--   35k sfmqrb 14 Oct 22:14  page-497.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-498.json
.rw-r--r--   49k sfmqrb 14 Oct 22:33  page-499.json
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
{
  "pdf_page": 505,
  "book_page": 475,
  "entries": [
    {
      "root": {
        "name": "Ter 3, Tar",
        "lang": "Indo-European",
        "refs": "PRT:863; KAS:10; POK:369; AHD:1500",
        "gloss": "a kinship term, a suffix indicating someone who performs the action indicated by the root verb"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK; SYN:103-107",
          "words": [
            {"translit": "Mâ-ter", "gloss": "feeder (of the family)", "script": null, "see": ["Mâ"]},
            {"translit": "Pa-ter", "gloss": "protector/ feeder (of the family)", "script": null, "see": ["Pa"]},
            {"translit": "Dhugh-tar", "gloss": "milker (of the family)", "script": null, "see": ["Dheugh"]},
            {"translit": "Bhra-ter", "gloss": "load carrier (of the family)", "script": null, "see": ["Bher 1"]},
            {"translit": "Geme-tar", "gloss": "married (to the family)", "script": null, "see": ["Geme"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "KLN; SYN:103-107",
          "words": [
            {"translit": "mâ-tar", "gloss": "mother", "script": null},
            {"translit": "pi-tar", "gloss": "father", "script": null},
            {"translit": "duğ-dâr", "gloss": "daughter", "script": null},
            {"translit": "brâ-tar", "gloss": "brother", "script": null},
            {"translit": "zâmâ-tar", "gloss": "son-in-law", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT",
          "words": [
            {"translit": "mâdar", "gloss": "\"feeder\", mother", "script": "مادر"},
            {"translit": "pedar", "gloss": "\"protector\", father", "script": "پدر"},
            {"translit": "doxtar", "gloss": "\"milker\", sister", "script": "دختر"},
            {"translit": "barâdar", "gloss": "\"load carrier\" brother", "script": "برادر"},
            {"translit": "dâmâd", "gloss": "\"married\", in-law", "script": "داماد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "môthar, fadar, dohter, brôthar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "mother, father, daughter, brother", "gloss": null, "script": null}
          ],
```


## [2026-10-15T02:44:33.393Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/505.jpg; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2500]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-10-15T02:44:33.798Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   66k sfmqrb 14 Oct 22:15  site/pages/505.jpg
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
   "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'glei
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


## [2026-10-15T02:44:34.940Z] TOOL CALL #5: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/505.jpg"
}
```


### [2026-10-15T02:44:34.993Z] TOOL RESULT

```

```


## [2026-10-15T02:44:38.041Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Root /lemma: terp\\|Root /lemma: ter-4\\|Root /lemma: ter-3\\|Root /lemma: ter-\\b\" POK_full.txt | head; grep -n \"1077\" POK_full.txt | head"
}
```


### [2026-10-15T02:44:38.484Z] TOOL RESULT

```
85996:Root /lemma: ter-3, tera-and ten-, tn- 
85935:Page(s):1077 
86335:Page(s): 1077-1078 
87074:from d^eragh-, dh/-eig^-with terk- and trek- {above S. 1077) originated?
```


## [2026-10-15T02:44:40.382Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 86320,86380p POK_full.txt; grep -n \"Root /lemma: .*ter\\b\\|Page(s): 369\\|Page(s):369\" POK_full.txt|head"
}
```


### [2026-10-15T02:44:40.802Z] TOOL RESULT

```
benefit'. Old English dearf^ necessary, benefit'. Old High German o''a/'i6'5"Entbehrung, 
lack', Gothic t^aurftsi. " necessary' (= Old Indie trpti-). Old Icelandic t^urft. Old High 
German durftds.7; die meaning- development could gewesen sein " whereof satisfaction 
finden - bediJrfen' (compare above S. 173 Latin ;h/o/'(ge)brauche); 

Lithuanian tarpa' prospering; flourishing, growth ', tarpstu, tarpt/'thme, zunehmen', 
Latvian tarpa'was gute Hoffnung gives, prospering; flourishing, growth ', terpinat 
"verbessern'. Old Prussian e/7/e/'yOC»"nutzt', enterpon, enterpen^ useful '; 

Tocharian AB /sa/w-"sich freuen' (Pedersen Tocharian Sprachgesch. 19). 

References: WP. I 736 f., Trautmann 314, Vasmer 3, 125 f., 134, Mayrhofer 1, 523 f. 



Page(s): 1077-1078 



Root / lemma: ters- 

Meaning: dry; thirst 

Material: Old Indie //•sya// "durstet, lechzt' (= Gothic l=>aursjan), tarsayat/" aWows dursten, 

languish ' (= Latin torreo. Old High German derren), tarsa-m. " thirst ', trsta- 'arid, rough, 

jolting, hoarse', trsu- " greedy, lechzend' = Avestan tarsu-'6ry, that is to say not fluid' (= 

apart from pronunciation of Gothic Paursus, Old Latin /o/TY/s'torridus'); Old Indie frsna' 

thirst, yearning', Avestan tarsna-m. ' thirst '; Old Indie trsna-j- " thirsty '; 

Armenian t'aramim, f'arsam/m '\Ne\ke' , far' shaft, pole zum Trocknen from Trauben ' 
{* trsa or * trs/a: gr. rpaaia); 

gr. T£pao|jai (£T£par|v) 'werde dry', Tspaaivu) "make dry', rpaaia, rapaia "Darre', lapooq, 
rappoc; 'Darre, Dorr- or Trockenvorrichtung'; dubious rpauAoc; (*TpaauA6(;?) 'lisping'; 

alb. /eA'trockne (trans.) an the air'; 

Latin torreo, -ere, -ui, tostum 'dehydrate, desiccate, fry, rosten, singe' {tostus= Old Indie 
trsta-). Old Latin torrus, extended /o/r/io'^s 'ausgetrocknet, arid', /o/r/is 'blaze, burning piece 
of wood', torrens' burning, sengend, erhitzt; violent, roaring, rapid in the current', Subst. 
"Wildbach' ('in summer austrocknend'?); 

here also Latin terrai. 'earth' (: eA-Zo/r/is 'verba nnt' = tellus: meditullium), Oscan 
teei{um], /em/77 'territorium', /eras 'terra e' from Italian *terso-, *tersa, Indo Germanic *ters-, 
to Old Irish //?n. es-stem ' region, area', corn. bret. acymr. //r'tellus'. Old Irish *//?, tirim 
'dry'; also basic form *teros-, *teres-, Latin terres-tris, terrenus aiter terra; Old Irish tart' 
thirst '(tz-s/o-); 

Italian terrene : Spanish tierra : French terrain : Furlan teren : Portuguese terrene ; terra : 
Romagnolo tiren : Sardinian Campidanesu (*terranea) tanca ; terra : Albanian (*tanca) toka 
' soil ; ground '; 

Gothic gaf^a/rsan stem V. ' wilt' (= gr. Tspaopai); gat^aursnan ds. = Old Icelandic t^orna 
ds.; Old High German dorren ds.; Old High German derren' dry make, dehydrate, 
desiccate'. Old Icelandic tierra' dry' (= Old Indie tarsayati, Latin torreo); Gothic t^aursjan 
'diJrsten', Old Icelandic Ay/'s//' (Gothic *t^aursiPs) ' thirsty ', whereof Gothic t^aursteii.. Old 
Icelandic t^orstirw.. Old English t^urst. Old High German durst' thirst '; Gothic t^aursus{s 
35026:Page(s): 369 
35055:Page(s): 369-370 
73586:Root /lemma: seni-, senu- {Sgni-), sp-ter- 
85996:Root /lemma: ter-3, tera-and ten-, tn-
```


## [2026-10-15T02:44:42.209Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 86290,86320p POK_full.txt; echo ----; sed -n 35000,35060p POK_full.txt"
}
```


### [2026-10-15T02:44:42.570Z] TOOL RESULT

```
an ostem %rmos or %ramo-s)\ cymr. cynrhonyn 'termes, lendix', PI. cynrhawn, corn. 

confronen^c'wnex', Middle Breton controunenn, nbret. contronenn'ver 6e viande' {*kon- 

trono); cymr. i{o)rog-en, abr. toroc, bret. teurok^vnWe' {*tdr-ako-). 

References: WP. I 735, WH. II 649. 

Page(s): 1 076 

Root / lemma: ter-Z, tera-, te/b^- terd- terg- terp- 
See also: see above S. 1022 ff., 1031 f. under ster-. 
Page(s): 1 076 

Root / lemma: terp- trep- 
Meaning: to be satiated, satisfied 

Material: Old Indie tfpyati, trpnoti, trmpati, /a/'/caZ/'sattigt sich, wird befriedigt', Kaus. 
tarpayati^ sdXW^i, befriedigt', trptf-, trpti-i. " satiation, satisfaction', Avestan ^rqfda- 
"befriedigt, ausreichend versehen' {*tramptha-: 0\6 Indie trmpati), &r^fs-v\. " 
contentedness '; npers. /i//rUbersattigung'(*//#a-); perhaps also Old Indie -trp- "stealing', 
Avestan ta rep- ^s\.ea\\ Middle Persian tirft^ theft ', sogd. cf- "steal' ("sich of Besitzes 
erfreuen'?); gr. TEpiru) "sattige, erfreue', T£pno|jai "freue myself; TspijjK; "satisfaction'; 

perhaps Gothic l=>rafstjan^ comfort, ermahnen', anal=>rafstjan^ refresh, zur Ruhe come 
let' (to *t^rafsta-, Indo Germanic *trop-sto-l)\ also die group Gothic t^aurban {t^arf, 
l=>aurbum, preterit t^aurfta) "bediJrfen', Old Icelandic t^urfa {t^arf, t^urfum). Old High 
German durfan {darf, durfum) ds., Gothic A'a/'ifc>5"bedurftig, notig'. Old Icelandic t^arfr^ 
useful ', t^arfi^v\6WQ\ Gothic t^arba^\acK DiJrftigkeit', Old Icelandic t^grfi. " necessity, 
benefit'. Old English dearf^ necessary, benefit'. Old High German o''a/'i6'5"Entbehrung, 
----

z^bQ, z^bst/" tear'; 

Old Indicya/77i6'/7a-/7m. 'tooth, PI. teeth ' (Jambhya-h^ incisor tooth or molar'), gr. y6|j(po(; 
"tooth', also 'peg, plug, nail'; yo|j(pio(; soil. 65ou(; ' incisor tooth ', alb. dhemb, Geg dam 
'tooth'. Old Church Slavic zgbii 'tooth', Latvian z^Oit's 'tooth', Lithuanian zambas^ sharp 
edge'; zs/ttZj/s 'wooden plow'; 

Old High German kamb. Old English cc»/77i7'comb' ('dentated'). Old Norse kambr^ Q,orr\\i , 
jagged edge (: Lithuanian zambas), jagged ridge ', Modern High German ' ridge, mountain 
range ' (but about ndd. kimmesee above ur\6er gem-). Old English cemban. Old High 
German kemben ' comb' , Swiss chambe^ Kamm bei Hahnen '; in addition Bavarian sich 
kampe/n \quarre\ =) tear, rend, fight, squabble', with expressive p; 

Tocharian A kam, B /re/77e 'tooth'. 

Under a meaning mediation 'tooth' - ' like a small tooth of protrudent plant shoot ' one 
lines up the family of Lithuanian zembu, zembet/" gerrr\\nate' , Old Church S\a\/\c pro-zgbat/, 
pro-zgbngt/6s., Latin gemma {*gerrb^na) ' eye or bud in the grapevine or in trees; 
gemstone, precious stone ', Old High German champ ' the stalk of a cluster of grapes and 
similar plants; a bunch of berries, cluster of grapes ', Modern High German Kamm 
('dentated device '); the Lithuanian glottal stop is explainable through a lengthened grade 
present formation like sergmi, gelbmi, gelbu. 

References: WP. I 575 f., WH. I 588, Trautmann 369, Specht Dekl. 86 f. 
See also: see also under gep(h)-, geb^-. 
Page(s): 369 

Root / lemma: gem(e)- 

Meaning: to marry 

Material: Old Indie yaAa-/?' suitor, lover' {*gm-r6-s?)\ Old \r\(X\c jamatar-, Avestan zamatar- 

' man's daughter ', created after other relationship names in -/sa- extension, with a the 

second syllable after matar-; the basic root has been abbreviated *Jama-, compare 

Avestan zamaoya-^ brother of son-in-law ', also Old Indicya/r?/-/?' connected, related by 



blood ', fern, nachved. " feminine relatives, esp. daughter-in-law ', ved. vf-Jami-h) " relative 
by marriage \jama^ daughter-in-law '; 

gr YOM^w " marry ' (Akt. of man, husband, Med. from the wife, woman), eyriMCi (Doric 
£yc(|ja), y£yapr|-MC('; YC(M£Tr|<; " husband ', yapeTn, yapsiK;, -xboo, "wife", yapr|AiO(; " nuptial ', 
yapo(; m. " wedding '; yappp6(; {*gem-ro-) 'son-in-law'; 

Maybe alb. o'as/77e "wedding': gr. Ya(JO(; m. "wedding' common alb. gh- > o'-phoentic 
mutation. 

Latin gener-, /"ds. (for *gemer aiter genus, gens). 

References: WP. I 574 f., WH. I 590 f. 
Page(s): 369-370 

Root / lemma: gen-1, gene- gne- gno- 

Meaning: to bear
```


## [2026-10-15T02:44:49.823Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in 'terp' ; do grep -n \"^terp\\|terp-\" AHD_watkins1985.txt | head; done; grep -n \"^mater\\|^pəter\\|^peter\\|^dhughəter\\|^bhrāter\\|^bhrater\\|^gem\" AHD_watkins1985.txt | head -20; grep -n -i \"Terpsichore\\|Euterpe\" KLN_1966.txt | head; grep -n \"terp\" IEC.txt | head"
}
```


### [2026-10-15T02:44:50.292Z] TOOL RESULT

```
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
2354:TENTH dekm TENUOUS ten- TENURE ten- TENUTO ten- TEPID tep- TERATOCARCINOMA kWer-1 TERATOGEN kWer-1 TERATOID kWer-1 TERATOMA kWer-1 TERCEL trei- TERCET trei- TEREDO tera-! TERETE tere-1 TERGIVERSATE wer-3 TERM ter- TERMINATE ter- TERMINUS _ter- TERN? trei- TERPOLYMER trei- TERPSICHORE gher-!, terp-
234:gemination” (doubling of the final conso- nant), written solid.
7550:Derivatives:  chorolog-ical,  adj.,  chorolog-ist,  n. chortle,  intr.  and  tr.  v.  and  n.  —  A  blend  of chuckle  and  snort;  coined  by  Lewis  Carroll, chorus,  n.  —  L.,  fr.  Gk.  yopoi;,  ‘dance  in  a  ring, festive  dance,  dance;  band  of  dancers;  chorus, choir;  troop,  band;  place  for  dancing’.  The  first meaning  was  prob.  ‘an  enclosed  place  for  danc¬ ing’,  from  I.-E.  base  *gher -,  ‘to  seize,  take,  hold, close,  envelop’,  whence  also  Gk.  yap,  ‘hand’, yop-o ‘feeding  place,  courtyard’.  See  chiro- and  cp.  words  there  referred  to.  Cp.  also  choir, quire,  chorea,  choreus,  the  first  element  in  carol and  in  choragus  and  the  second  element  in Terpsichore.
13853:Euterpe,  n.,  the  Muse  of  music  (Greek  mythology). —  L.,  fr.  Gk.  EuT£p7rr),  lit.  ‘pleasing  well’,  fr s5  (see  eu-)  and  T^pTteiv,  ‘to  delight,  please’. See  Terpsichore.
38687:Terpsichore,  n.,  the  Muse  of  the  dance  (Creek  and
38692:Roman  mythol.)  —  L.  Terpsichore,  fr.  Gk.  Tsp- lit.  ‘enjoyment  of  dance’,  a  name  com¬ pounded  of  T£<p4^,  ‘enjoyment,  gladness,  de¬ light’,  and  x°po?,  ‘dance’.  The  first  element  is  a derivative  of  Teptretv,  ‘to  delight,  please ,  fr. I.-E.  base  *terp-,  ‘to  satisfy’,  whence  also  OI. trpyati,  trpnoti,  tarpati ,  ‘takes  one  s  fill ,  Avestic &rafda-,  ‘satiated,  satisfied’,  Toch.  AB  tsdrw-,  ‘to rejoice",  tsarwo,  ‘joy’,  Lith.  tarpstii,  tafpti !,
38693:‘to  thrive,  prosper’,  tarpa,  ‘thriving,  prosperity  , Lett,  tarpa,  of  s.m.,  OPruss.  en-terpo,  ‘it  is  use¬ ful’,  en-terpen,  en-terpon ,  ‘useful .  Cp.  Euterpe. For  the  second  element  see  chorus.
38694:Derivative:  Terpsichore-art,  adj.,  pertaining  to Terpsichore;  hence,  pertaining  to  dance, terra,  n.,  earth.  —  L.,  prob.  for  *tersa-  and  lit. meaning  ‘dry  land’  and  rel.  to  OL.  torrus  (for *torsus),  ‘dry’,  L.  torrere,  ‘to  parch,  roast’,  and cogn.  with  OIr.  Ur  (for  *teros),  ‘land’,  fr.  I.-E. base  *ters-,  *trs-,  ‘to  be  dry’,  whence  also  OI. tar$dvati,  ‘dries  up’,  tr?yati,  ‘thirsts’,  tfftah, ‘hoarse',  trsuh,  ‘greedy,  desirous’,  Avestic tarshu-,  ‘dry,  solid’,  Arm.  Tafamim,  ‘I  wither, dry  up',  erasht,  metathesized  fr.  *trast  (for  I.-E. *trsti),  ‘dryness, drought’,  Gk.TspnenHat,  ‘to  be or  become  dry,  dry  up',  Tspaodvciv,  ‘to  make dry,  to  dry',  xapoo;,  ‘wickerwork;  flat  of  the foot;  ankle’,  xpama,  Ion.  xapai r„  ‘a  crate  for drying  figs'.  Alb.  ter,  ‘I  lay  out’,  Goth.  p aursus, ‘dry,  barren',  OHG.  thurri ,  durri,  MHG.  durre, diirre,  G.  diirr,  Du.  dor,  OS.  thurri,  ON.  purr,  OE. pyrre,  'dry',  OHG.  darra,  MHG.,  G.  darre,  'kiln drying'.  Cp.  inter, ‘to  bury’,  mediterranean,  par¬ terre,  subterranean,  tarsus,  terrace,  terra  cotta, terrain,  terramara,terramycin,  terrane,terrestrial, terrier  (in  both  senses),  terrine,  territory,  thirst, toast,  torrid,  trass,  traulism,  tureen  and  the  sec¬ ond  element  in  verditer.  Cp.  also  torsk. terrace,  n.  —  MF.  terrasse,  terrace,  ‘pile  of  earth, terrasse'  (whence  F.  terrasse),  fr.  O  Pro  vent,',  ter¬ ras  su,  fr.  VL.  *terrdcea,  a  derivative  of  L.  terra, ‘earth-.  See  prec.  word  and  cp.  terrazzo. Derivatives:  terrace ,  tr.  v.,  terrac-er,  n., terrac-ette,  n.,  terrac-ing,  n. terra  cotta,  hard  pottery,  compounded  of  fineclay and  fine  sand.  — ■  It.,  lit.  ‘cooked  earth  ,  fr.  terra , ‘earth'  (fr.  L.  terra),  and  cotta,  fern.  pp.  of  cuo- cere,  ‘to  cook'  (fr.  L.  coquere).  For  the  first  word see  terra,  for  the  second  see  cook  and  cp.  coc- tion.
51:My thanks are due to all previous lexicographers (“harmless drudges”) and etymologists who have unknowingly contributed to the material of this Dictionary, and who have served as a necessary corrective to a work whose only aim is to present a common denominator rather than a lost primitive speech. As an independent study, Indo-European linguistics can claim to be an exact, albeit empirical science, since it fulfils the three requisites of science, viz. collection, classification and interpretation. For such a science, absolute and final proof is probably unattainable, but if a relationship can, in terms of Euclid, be “de- monstrated" by an adequate amount of analogy, the result can be both probable and con- vincing. Historical linguistics is unique in being probably the only exact science that is linked exclusively to human behaviour. It stands or falls by the logic inherent within it, and does not depend op the dicta of any one scholar, dead or alive. In bringing this work to a close after 55 years of intense and unremitting labour, the author has tried to avoid the German fault of overloading etymologies with irrelevancies, the French fault of trim- ming the evidence to achieve a neat pattern, and the Anglo-Saxon fault of being content with approximations.
1292:bhi- (radical) ‘be’. WP II, 143 Per. bid (2pl. imperative "bel: Gk. cf. phi- tuo “produce, propagate'; OLat. fi! fite! (*be- .come'! Plaut.) (Lat. fio usually interpreted as if fr. *bhui-); OIr. bíu “am”; Ir. cf. bí-odh Tet him be"; OBr. bi! id.; MW bit! W bid! id.; OCS bimí, bi, bi (condit. ‘should be); OLi. bit, biti (3s. "was
2007:bhutios, om “container, cask’ Gk. (fr. Maced.? Thrac.? Phryg.?) cf. bütinë, beside Mod. Gk. bution ‘cask’; LWs in Alb. buti, gs butini, id. beside but, id. (perh. via LL buttis, id.); Per. (?) büte ‘crucible’; ON cf. boðn “vessel, pot Li. bücias, bücius *fish- trap, lobsterpot'. (A *wanderword' in Rom- ance and Gmc.)
6222:cf. khés-imon “self-easement'; pés-imon “act of falling'; pega-imós 'act of departure'; Alb. het-im (inquiry): Li. skait-ymas reading); Ir. maoidh-eamh, gs -imh ‘telling’; áir-eamh, gs -imh ‘counting’; OCS pisimo “letter, writing; jarímü (fyoke', cf. Pol. ko-jarzyé "mont: Li. pie3-imas, ar-imas, grub-imas, &j-imas *design- ing, plowing, roughening, going’ beside grüd- ymas ‘hardening’; sür-ymas ‘saltwater’, etc. -inā, a generalizing extn. See next Gk. khoir-inë (‘musseľ: khoiros); dotiné (Hes: dos); (melíné ‘millet? in relation to *mel- ‘grind’, q. v. may belong here); Alb. lug- inë ((valley': lug 'trough); rreth-inë ('sur- roundings': rreth 'circle"); Lat. farina (:far); rüpina (:rüpes); haed-ina ('goatsflesh': hae- dus); OS cf. stulina ‘stealing’; lugina ‘lying’; OCS ozina ('anguish': ozükü, cf. Lat. angina); globina (‘depth’: globokü); dolina ('valley': dolü *ditch"). A variant occurs in Li. avíena “mutton”, cf. LLat. ovina, id. As an indicator of a female with a male counterpart, cf. Gk. héroiné (*heroine": héros); Lat. reg-ina (:rex); MHG cf. vühsinne (vixen': vuhs). A truncat- ed formula occurs in Go. managei, obl. -ein- ‘multitude’ and OHG hohi, obl. -1n-. See next -Inos, om (-Inios, om), an adjectival formant > a noun-derivative. Skt. a$v-in (:Lat. equinus); Av. peronin *wing- ed'; hámin- ‘summer’; Per. Sirin (sweet: Sir *milk); éübin (^wooden': éüb); pūstīn (‘fur coat: pūst "pelt: Oss. zàr-in ( golden": zàr); Arm. verf-in (final: verð); het-in, id. (fr. *en-pedinos, cf. Li. j-pedin “close behind”; Í-pédinis *successor"); Gk. pheg-inós (*oaken": phégós, cf. Lat. fàgínus of beech’); earinós (‘of spring": éar, cf. Lat. vernus); Lat. marinus, fibr-inus beside nüc-Ínus, màter-nus, ver-nus, etc.; W derw- in, lledr-in, hef-in ('oaken, leath- ern, summer: derw, lledr, haf); Go. fill-eins (‘of skin": fill, cf. Lat. pell-inus); fadr-ein (“pa- ternity, cf. Lat. paternus); OHG bibir-in, fuhs-in; MHG buech-in; ON gull-inn, OE medr-en, etc. “of beaver, fox, beech, gold, mother’; OCS materinü, materiní ‘maternal’; sestrinü, sestrini ‘sisterly’; krův-ínů (“of blood': krúvi, cf. Li. krùvinas ‘bloody’:kraŭjas “blood”). The variant -inios, where it occurs,
7061:kerpó, ið (2) ‘be fit, be strong, thrive’. Cf. kroip-. WP I, 486 and II, 595. (Evidence am- big.) Skt. (o-gde) kálpe “be fit, succeed'; z-gde in klptáh “arranged, fit, ready’; Tokh. AB kilp-, B (also) käll «reach, obtain’; OCS cf. krépü, adj. ‘strong’; krépljo, krépiti ‘strengthen’; OCz. cf. stfépné, f. “responsibility”; Li. kerpiü, "ti join, mate’ (Various interpretations of Lat. corpus in EM:DELL & WH:LEW)
8136:(ks-. The identity of this initial is difficult, esp. when an alternative *qus- is possible. The equivalence of Skt. ks- and Gk. kt- is pro- bably to be interpreted as *kst-, cf. *rkstos ‘bear’, and Skt. ks-: Gk. khth- as *ksth-, but firm evidence is lacking. Cf. the author's “The Reduced Prefixes Ks- and do/d- and Metathe- sis in Greek’, Transactions of the Philological Society, 1942, 11-14, in need of revision, and "Initial x/š in the Slavonic Languages’, Slavo- nic and East European Review, 88, Dec. 1958, 131-140)
8262:kübo ‘lie’. Cf. kumbó (1) Lat. cubo, åre, pf. cübi, id.; Ir. cúbaim ‘crouch, lie down’; ON (?) hopa, v. ‘recoil’; OE cf. (?) hop-scyte ‘counterpane’
14160:quolos, -es- “turning, turn, wheel, axis, centre, community'. WP I, 515 and cf. I, 464. Cf. quol- extns. and queló Arm. cf. olor, Let, (twist, curl", fr. *quolesi-); Myc. -qoro-; Gk. pólos, m. 'axis, globe, dial, round chaplet’; cf. oneiro-pólos ‘interpreter of dreams; Alb. cf. kalla- in kalla-tumba *head- over-heels'; Thrac. cf. kól-abros ‘a dance’ be- side koléa, id. (if fr. *quoleso. Hes.); Lat. colus gs: -1, and -üs, f. 'spinning-wheeP" beside in-
15012:sap- (1) 'stick, rod, penis, pipe, spout. Vowel uncertain, cf. sopos, io(n). Skt. sápah, m. ‘penis’; Gk. cf. pri-ápos, -épos (Cerected', vulg. Osthoff); (Srb. sopa, LW = ‘stick, cudgel’); Blg. sop, m. *waterpipe, spout’; (sòpa, LW = ‘stick, crosspiece of loom’); cf. sopot, m. ‘drainpipe’; Pol. cf. sopel, m. ‘icicle, pintle of lock’. (The vowel -o- is explicit in Lat. song, m. ‘penis’, see sop-). Cf. also OCS sopli, m. ‘flute’; sopuxü, m. ‘reed’ and sopotü, m. ‘pipe’ (all w. ambig. vocalism). ON sef, Sw. säv, n. “reed” appears to be distinct, in view of Dan. siv, id. (NB. Blg. Srb. sopa is fr. Tk.)
16039:skhaul- “cover, casing, sheath' Skt. kholah, m. ‘waterproof hat; helmet’; kho-
```


## [2026-10-15T02:44:53.840Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"rafəδa\\|rafada\\|rafəda\\|raf[əe]d\\|θrafs\\|rafah\" BRT.txt | head; grep -n \"^tarəp\\|tarap-\\|tarəp-\\|tarep-\" BRT.txt | head; grep -n \"zāmātar\\|zamatar\\|dugədar\\|duγdar\\|dugadar\\|dug[əe]dar\" BRT.txt | head; grep -n \"brātar\\|bratar\" BRT.txt | head -5"
}
```


### [2026-10-15T02:44:54.279Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:44:56.449Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 1500 BRT.txt; echo; grep -n -i \"stehlen\" BRT.txt | head; grep -n -i \"befriedigt\\|Sättigung\\|sättig\" BRT.txt | head"
}
```


### [2026-10-15T02:44:57.067Z] TOOL RESULT

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
12102:•  j.  tanp-  V.  'stehlen',  Praes.  27  trpjya-'\
12106:Vgl.  ai-  'Irt-  Adj.  'stehlend'  (KZ.  35.  311). mp.  lirß*)  'DiebsUhl';  alles  übrige  (Horn NpEt.  86,  Hbm.  PSt  185)  ist  unsicher.  — Pü.:  HrflFnUan').  —  ')  Statt  bn/y',  %  368. 39.  —  ")  Vgl.  zu  taya-  und  l^vis:  Wie  zu lesen?  Wl.  Iri/t°,  Analogiebildung  nach^r^* (IF.  II.  ia6),  wenn  man  annehmeD  darf,  dass air.  *lffjati  zu  mp.  'Grcl  führte,  wie  "g^iiaii zu  gira  (IF.  12.  107).
12187:Aus  einer  Buii  »/iv-  (iBild-  s.  Bthu  AT.  3. 53);  E.  np.  iiiädan  'stehlen',  ksl.  lajiH  'bergen' usw.;  Bau.  IF.  //.  105.  —  Vgl.  laya-,  läya-, läyav:  —  Pü.;i/«£[/Bpdark'),  ert.:  apdaark')- ei  (K)  etSn  vinäskär  ^göti  duid.  —  >)  Nicht ganz  sicher.  Hds.  /äyiäs/a;  »gl.  S  s6S.  14.  — ')  Welche  der  beiden  Schreibungen  ist  die lichllge?  Ein  apt  apdaariin  (bei  DsT.  ZA.  I. loi:aßäiisn  'presser')  steht  in  Pu.  zu  Y.  27.  7.
12675:ai.  daihnoä  'er  tauscht,  schädigt'^,  difisah, daihyaH:;  daidhäh;  otsss.  .^a:»» 'stehlen',  PDw. lUt^deiusam  'ich  mache  Profit''(GIrPh.y  b.  321); ann.  [LW.?)9>  dmii  ■hintergehen'.  VgL  noch lÜHBi-  und  Pü,  EU  diavay-.  —  Pü.:  fre/lan;  s. noch  No.  6,  7.  —  «)  iSchr.  s.  S  2&J.  37.  — •)  Ar.  *i^hana%-\  vgl.  Bthl.  IF. /.  78,  wo weitre  Litt.  —  i1  Bthl.  IF.7.  87  No.  und  lu q/7a-.  —  4)  Ohne  Desiderat! vbedentung,  — S)  %S3  n.  1.  — 6)  Pg.:/fl  fl„/r^.  -  7)P6.r hin  . .  ie  pa  freflarlh  fugend.  —  •)  Zum  angebl. ai.  Praes.  a  däbhaü  s.  Bthi_  IF.  7.  83.  — «  Hbm.  AGr.  /.  438.
3326:•  j.  a-dbi§ta-'>,  a-tbiäta-'>  Adj.  (fem. °/p-)  'nicht  angefeindet,  gekränkt':  iitar/.. xsnStä  °tö  \.62.^;  Yt  lO.iio,  V.(j.39,  Yt. '3-^5'  —  xsnataheat  'tahe  mi>ra  manS yaozayeiti  "(aber)  auch  des  befriedigten, ungekränkten  Sinn  bringt  er  durch  M.  in Aufruhr"  Yt  /o.  1 1 1 ;  —  xsnUth  ainili  °t^ ..  fravaiayö  Yt/y.si;  34i  63;  —  "'"^ (VS.)  Yt/2.8.
5308:•  j.  a-ratu'fri-  Adj.  'der  nicht  r.  ist,  die Ratav  nicht  befriedigt,  es  ihnen  nicht  zu Dank  macht,  gegen  ihren  Willen  ver- stösst':  äahms  zaota  dahmS  upa.sraolärü vispe  ratu/ryö  tanupirii^ö  zaota  tarnt- p>r3%5  upü.sraotltrS  vupe  '/ryüti.^i);  — yai  ig  däiti  dalätH  ^rafufrÜ . .  yesi  aal hSnDit  däiti  daoäiti  '/ris'ü.io^;  wo,  loi'^, S03, 104,55,  *55  ■';  — yi  ^ri/*Aa>räricS yätayeinle  ratufryS  yai  Hat  (ä-ri/)  nSii *Aa>r.'rtci>  yataytinti  'fryO  N.  S8;  gj,  gi, 9-',  93>  95;  —  y^i  •  ■  »o  ratu/ryö  yezi *aai  .  .  uva  -/ryJ  (ND.)  ü.$4;  —  yai arastnm  (sd.)  .  .  pairi.iioa  .  .  °/rya  pasca vä  pars  vä  pairi.ä6a  °/ryS  ii.32;  —  yä yastam  *yazfnti..  nva  *ratu/rya  Aam.srul.- väcayala  (sd.)  ^yax^nti  *«va  *'fiya  (ND.)'' N.  24',  — yö  aiwyänhayäiti  kar>tSsca  °/ryS pasca  aiitiySstim  nitaohydti  ratufrys  N. tV^.  a)  mit  Gen.  dessen,  wodurch  (und wofür)  man  ar.  ist  oder  wird:  yasnahe advakt  (sd.)  ratu/ris  'frii gä'iianqm  N.22; —  kaithqm  ml  gä'^anqm  srutanqm  °/rii3 yä  ^maizö  vä  . .  *srävayeiti  aetaesqm  vacqm "fris  "mit  welchen  aufgesagten  G.  verstbsst
13258:ai.  vgl.  dhi„öii  'er  sättigt'.  —  VgL  däyah-, ■^a'däyav;  ixaoüya-.  —  Pfi.  (zu  Y.  Sp):  te  pa 1  an  i  har  3  dahän  dahel  Öhnurlärän,  (zu  Y.  Jj) : däniinSi.  —  >)  NamL  mi  urvä  gitäeä  atyi  V. Y.  29,  s-  —  ')  S.  iiida/.gav-  mit  No.  —  3)  Also
14575:gesegnet':  saokqmia  baral-avantam  barat.- aya^qm . .  'Zqm  Yt  ij.  41.       2)  'befriedigt, zufrieden  gestellt':  ytiiAi  nm3naya  sraoSs .  .  'Zs  asti  faili.zanlö  Y.57. 14,         a)  'zu- frieden, wohlzufrieden':  ya%a  aüfir  amavh °%S  fraxslane  z>mä  paiti  Y, 9.  ao;  F.  2^'', Aus  ar,  'tramptha-,  S  24  aE.  —  Vgl,  %ri^fs'.  — ai,  vgl.  ,!r«/(iA'er  wird  Salt', —  Pii.:  ptdannJ), Sü, :  samidäka^.    S.  noch  No,  1.  —  ')  So  in NA.  nur  Yt.  13.  loo;   s.  aber  Pt4  lu  Y.  57, K5  lo  Y.  fl.  —  •)  Pü.  (ßlschlich):  ptdanrt. —  J)  Nach  Ki.fatlx'  la  lesen,  s.  Yt.  /.  az, Mx.  3.  1  (usw.);   aber  SWienAW,  67.  841.  5 »lebt  fiidix  :  xus7.     Wohl    lu  fifav-  (sd.),   also fil  dar  lu   lesen?,   vgl,  np,  baxlyir  nsw,     S. noch  lU  %rima-,  /rap^wa-  und  äyapla-.
14642:•  j.  Srima-  m.  'Nahrung,  Sättigung; Stäilcung,  Stärke':  gaohamm  (sd.)  .  .  yat asti  puhraAe  'mS  Y.2i,j;  —  am>mla *'mimla ''  aojasca  Yt, I.ti;  —  amäica 'tnäica  yat  fouru.baoxsnahe  (sd.)  Y.^,  27; —  °mahe  . .  baliazyeke  Yt  t^.  50.
29681:voD  iveien  (die  Gä^as)  aufsagt,  ist  nicht r.,  wer  sie  für  eine  Veisammlung  von  dreien au&agt,  ist  r.    Wie  gross  muss  eine  Ver- sammlung  mindestens  sein,    damit   man die  Ji.  befriedigt?    Eine  Versammlung  von dreien."  N.jj. KompE.  —  Zum  V.  'Ani;  eig.  'Siuung'.    — u.  tiUb-d.  n.  'Feier,  Feit';   s.  daia  IFAni.  Ä 15.    —    Pü.:  haHJaman.    —     ')  Der  folgende Text   iit    Dicht   in  OTdnone.    Auch    die   Pü. nicht.     Abweichend  überielit  DsT.  ZA.  3.  99. S.   noch   No.   3  ff.    —    1)   Liei   aratu/f.    — J)  Erginze  rahtfr'.  —  *)  Liei  %Tii.hattnm ;  td.  '
30179:•  j.  'hu-xsnaoOra-  Adj.  'leicht  befriedigt, leicht  zufrieden  zu  stellen*:  •rj(NSm,,  näml. ist  der  Hund)  yc^a  ahrava  AväzSrd  (sd.) yaha  ährazia  V.  J_J.  45.
```


## [2026-10-15T02:44:58.658Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 12100,12107p BRT.txt; sed -n 14570,14575p BRT.txt | cut -c1-600"
}
```


### [2026-10-15T02:44:59.141Z] TOOL RESULT

```
•  j.  tauruna-  Adj.  'jung'  von  Menschen und  Tieren:  yS  yaiia  pu'hnm  "mm  hao- mam  vanäalta  masyS  "wer  den  H.  wie einen  jungen  Sohn  lobt"  Y.  10. 8;  —  spä 'äj  "ein  junger  Hund"  V, 5. 30";  —  spämm .  .  yim  »ffw»  V.  13. 1  $,  23,  27».  a)  m. 'Knabe':  ma  apinnHyu  'na  mS  kainina anupaitä  (sd.)  mafyänqm  "nicht  unmündige Knaben,  nicht ..  Mädchen"  Yt,/7. 54;  55.
ai.  tdruffa-  Adj. ;  np.  vgl.  lar.  —  Wegen  np. eh  'jniiEer  Hund'  s.  IFAni.  10.  22.  —-  Pü.! faranai,  Sfi.:  JiSuA.  —  >)  ifiä  'no  bezeichnet nach  meiner  Ansicht  den  un ausgewachsenen Hund  jeder  beliebigen  Basse  (vgl.  V.  /j.  10  fT.), '. der  eben  wegen  seiner  Jugend  noch  nicht  in  1 bestimmter  Richtung  Tervrendet  werden  kann.  | DST.  ZA.  3.  197  meint  mit  Andern,  ea  sei  . der  Jagdhund  darunter  lu  verliehen,  vgl, draxlB-kunara-,  s.  aber  die  Riv.- Stelle  bei  Sp. Ober*.  2.  :uxui  No.  z ,  wo  fürüi  (für  mp.  I laranak;  s.  V.  /j.  27]  gleich  baia  gesetzt wird.     Bd.  14.  19  hat  larSi  in  Aw.-Buchat.
•  j.  tanp-  V.  'stehlen',  Praes.  27  trpjya-'\
mit  Akk.  der  Person  und  der  Sache:  yH
mam    tal   draenS  zinät  (sd.)  va  tnjyäl^''
vä  apa  vä  yäsaiii  Y.  11. 5.
Vgl.  ai-  'Irt-  Adj.  'stehlend'  (KZ.  35.  311). mp.  lirß*)  'DiebsUhl';  alles  übrige  (Horn NpEt.  86,  Hbm.  PSt  185)  ist  unsicher.  — Pü.:  HrflFnUan').  —  ')  Statt  bn/y',  %  368. 39.  —  ")  Vgl.  zu  taya-  und  l^vis:  Wie  zu lesen?  Wl.  Iri/t°,  Analogiebildung  nach^r^* (IF.  II.  ia6),  wenn  man  annehmeD  darf,  dass air.  *lffjati  zu  mp.  'Grcl  führte,  wie  "g^iiaii zu  gira  (IF.  12.  107).
•  ]■  "gaZwa  MurS  kurs  (sd.)  tamvani . ." FrW.2.2.
Ableit,  —  Komp.  wie  iiirS.taa%r3-;  zum  Praes. 26  des  V.  %rä:  —  Pii. :  sriycnTlir  i  driiötSn. -  ')  VgL  Y.  j*  S-
•  j.  fl-räyö.drijTi'tama-  Adj,  'der  die Annen  am  besten  beschirmt,  am  besten versorgt':  marsdikavastima  'ma  (als  AP,) A.J.4-
Pü. !  drijSsiin  träythitirlMni. ].  %r»m>ot  Yt,  T.  2Z:  lies  %rim: j.  %r3sar>m  P.  99;  lies  %ris'. j.  %r>tl?mim?ai  N,  J/j  \ie%%rUaslim}mHl(i).
•  j.  SrtjfBÄa-,  9T^f8a-'>  Adj.  (fem.  "oä-) 'satt'  sva,  i)  'ausreichend,  reichlich  ver- sehen mit  — '  (Gen.):  nT  Alm  (näml.  dal- nqm)  dasta  . .  birni.räsim  . .  °lam  giusca västraheca  frihqm  gSusca  vSslraAeca  Yty, 100.       a)  ohne  nähere  Bestimmung  'reich
ÖTi.gamya-  806
gesegnet':  saokqmia  baral-avantam  barat.- aya^qm . .  'Zqm  Yt  ij.  41.       2)  'befriedigt, zufrieden  gestellt':  ytiiAi  nm3naya  sraoSs .  .  'Zs  asti  faili.zanlö  Y.57. 14,         a)  'zu- frieden, wohlzufrieden':  ya%a  aüfir  amavh °%S  fraxslane  z>mä  paiti  Y, 9.  ao;  F.  2^'', Aus  ar,  'tramptha-,  S  24  aE.  —  Vgl,  %ri^fs'.  — ai,  vgl.  ,!r«/(iA'er  wird  Salt', —  Pii.:  ptdannJ), Sü, :  samidäka^.    S.  noch  No,  1.  —  ')  So  in NA.  nur  Yt.  13.  loo;   s.  aber  Pt4  lu  Y.  57, K5  lo  Y.  fl.  —  •)  Pü.  (ßlschlich):  ptdanrt. —  J)  Nach  Ki.fatlx'  la
```


## [2026-10-15T02:45:05.466Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=12080 && NR<=12110' BRT.txt | grep -o \"^[^ ]* *[0-9]\\{3,4\\}$\\|[0-9]\\{3,4\\}  *[A-Za-z.°-]*$\" | head; grep -n \"^[0-9]\\{3\\}\\b\\|  64[0-9]$\" BRT.txt | awk -F: '$1>12050 && $1<12120' | head"
}
```


### [2026-10-15T02:45:05.887Z] TOOL RESULT

```
643
644
12051:641  tar9-äat-
12071:taro.pifrwa-  643
12082:643
12085:644
```


## [2026-10-15T02:45:08.779Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"'Tochter'\\|'Schwiegersohn'\\|'Bruder'\\|'Mutter'\\|'Vater'\" BRT.txt | cut -c1-200 | head -30"
}
```


### [2026-10-15T02:45:09.192Z] TOOL RESULT

```
16365:•  U  E-.  P-  pitar-,  j.,  g,  *ptar-,  patar-", g.  tar-'':j.,  %.ß>r-,  p./jV-,  j.,  %.filr-ä m.  'Vater' :  fita  pukrasca  Y.g. 5 ;  — /«' & re va  Jru^räi  Yt.  14.  46;  —  ks  usitnSm 
17427:•  ]■>  g'\  P-  br^tar-  :  iräir-  m.  'Bruder': li  kä'büjiyahyä  'tä  bardiyJ'  nätni^  SAa* Bh./.io;  11;  —  'ta  .  .  ^attha  vä  V. 12.  s;  Yt.  J7. 16;  —  'ta  haca  sfaahartm :^a»ha
17479:•  j.  "faSri  'Vater'«:  F.y.
28086:AbleiL  aus  "säma-  m.,  svl.  ajmälat-;  afy. lümt).  iSulT.  (ar.  ?I3.)  und  iKed.  s.  tüitya-, itülmya-  und  WH.'Or.'  %  2228c.  —  I'ö.: äämät  'Schwiegersohn'.  —  ■)  D.  i.  'zäniai
```


## [2026-10-15T02:45:12.206Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28080,28086p BRT.txt | cut -c1-500; grep -n \"dug[ae9]dar\\|du%d[aä]r\\|dug>dar\\|dugsdar\\|'Tochter\\|Tochter'\" BRT.txt | cut -c1-300 | head; grep -n \"mätar-\\|mStar-\\|matar-.*Mutter\\|'Mutter\" BRT.txt | cut -c1-200 | head"
}
```


### [2026-10-15T02:45:12.702Z] TOOL RESULT

```
—  narqmca  'tanqmca  sqhyamnanqnt^a (sd.)  Y,  4-  S'i  —  ^^annatiuhaslimS  °tanqm Y.g.  4.  2)  'jetzt  vorhanden,  jetzig';  ya/ asti  airyanqm  dahyunqm  'tanqm  (GPf.) aziitanamca  (sd.)  Yt  ig.  56.
KompA.  —  ri'fP.  iura  V.  -.an-.  —  ai./i/a- Atlj.,    nip.  Siit;    rp.    vgl.  :.i</a.    —     Pü.;    :ä/,
•  j.  nsil  hväzaiö  nöii  "zäniti  FrD.  7.
•  j.  zänu.dräl|ah-  Adj.  (auch  fem.)  'im Vorstrecken  des  Kinns  bestehend':  aEvahe zl  .  .  anasaonS  v'l  (NSf.)  .  .  ü/riti^  (ßAy V.  16.  II.
*:iinav-  f.  'Kinn'');  vgl.  %\.  hänav-  f.,  np. zaiiiix.  —  Pii.;  züiiak  drahnäk.  —  ')  Vor- strecken des  Kinns  bei  gleichzeitigem  Streifen des  llandiückens  vom  Ilats  her  nach  dem Kinn  tu  drückt  in  Italien  Geringschätzung aus.  —  >)  Das  ä  ist  aufrälÜg;  man  hat  das Wort  dirtim  mit  'Knie'  übersetit  —  lulelil Gdn.  SPreussAW,  ig.  414:  'Kniestoss' -  und zu  ai.  j'iinit  n.,  np.  zitiii  gestellt  Aber  Pü. spricht  nicht  dafür  j  'Knie'  wäre  zänüi.
•  j.  *zämaoya-"  m.  'Bruder  des  Schwieger- sohns': 'yö  F.  20.
AbleiL  aus  "säma-  m.,  svl.  ajmälat-;  afy. lümt).  iSulT.  (ar.  ?I3.)  und  iKed.  s.  tüitya-, itülmya-  und  WH.'Or.'  %  2228c.  —  I'ö.: äämät  'Schwiegersohn'.  —  ■)  D.  i.  'zäniai/ya; %  36S.  13.  Die  Hdss.  haben  i  statt  y.  — ')  Das  nicht  mit  Ggr.  ABayrAW.  20.  t.  194 gleich  j.  ämälar-,  np.  dämäd  gesetzt  werden kann;    dafür  wäre  *:ümör  zu  erwarten,    vgl.
6915:•  ].,  g.  ahuräni-  fem,  patr.  Adj,  'von Akura  stammend,  Ahs  Tochter',  als  Bei- wort des  Wassers;  mit  GS.  aAuraAyä, °rahe:  aps  at yazamaidl tna^aintls'ä  (sd.) .  .  'ränis  akura/iyä  Y.jÄ  3'';  —  yd  vö sps  vanuhis  yazäiie  ..  'ränls  ahurahe  Y. 68. 10.  A)  als  Gotthei
13645:^"fdtnäni  N   ,ro-  lies  ,arSJ.nä^  "  S-   dug»dM-,  j.   do^^r-  C  Tochter':
10253:•  j.   gaMWa-   m.    l)   'Mutterleib,   Uterus':  I         i-  Sanmü.vataahim  A.  J,  ?;  lies  a^arim-,
14146:•  j.  driwray-  f.  'Flecken,  Mal'  (nur Komp.).  a)  bes. 'Muttermal' :  mä  dhra .  .  °wil  . .  mSia.am  anyqm  daxstanqm  ,  . atarahe  mainySuiV.2.3^.  a)  aXsGasva: 'wii'  daevB  V.  ig
14793:•  j.  'pacman-  n.  'Muttermilch';  yU  (nätnl. aridvt)  vupanqm  hütriünqm  däitlm  ra- %wTtn  'ma  ava.daraiti  Y.Ö^.z;  Vyt  50; —  Aä  (näml.  andvt)  .  .  yaeiäa%äiti  .  . ar^qm  xhtdrä 
16972:•  '].  baradrl-  f.  Tntgeiin,  Erhalterin; Mutter':  zqm  pgrikviXm  . . ya  '%ri  paraoi srJrahe  y3  vupsm  aAüm  .  .  baraiti  Yt y.  9;  *F,  2f.**,  *7ff'*;  —  tarn  ptn%wim  .. ■ärr«  
17725:•  p.  fi^-mätar-  m.  'Gebieter,  Befehls- haber': a''ur<^matdä  .  .  hyJ'  xsayärsäm xs3yai:iyam  akunaul  aivatn  parUnäm  xsä- yaiiyam  aivam  parünäm  °ttlram  X. /.  i, 6".  I,  ♦D.6:i'>,
20278:ai.  miTnile;  mitik;  np.  patmäyad  'er  misit', »üBiöj'flrf'er  teiel'.  ätiaöj'.irf 'er erptobt';  ows. amain  'erbaoen.  —  PO.  (in  V./,  F.  S):  ezmä- yün,  Hmüli^ai),  (zu  Vr.  //):  
20291:•  j.  'mätar-  m.  'der  misst,  Messer':   Vöi
20293:•  ].,  g.  (,  p.)  'mätar-  f.  'Mutter*:  yai  pits .  .  'ta  vä  paradrUyäti  hat  a^qm  upa.- manaytn  (sd.)  pukrS  haia  pilarvm  duyta^ haca  Uanm  V.  12. 1 ;  3,  F.  2,  6;  —  pita 
28087:•  j.  zämätar-  m.  'Eidam,  Schwiegersohn': aäai>iiva  (,rä.m\.  asti  mihrB)  antan  'tara (AD.)  :^asura  ".  .  zwischen  Eidam  und Schwäher  Ytio.  116.
```


## [2026-10-15T02:45:16.899Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28087,28090p BRT.txt | cut -c1-600; sed -n 13645,13648p BRT.txt | cut -c1-500; sed -n 20293,20296p BRT.txt | cut -c1-200"
}
```


### [2026-10-15T02:45:17.987Z] TOOL RESULT

```
•  j.  zämätar-  m.  'Eidam,  Schwiegersohn': aäai>iiva  (,rä.m\.  asti  mihrB)  antan  'tara (AD.)  :^asura  ".  .  zwischen  Eidam  und Schwäher  Ytio.  116.
a\.jii>Mä/ar-  m.,  np.  Jämäd'1.  —  Vgl.  iJi?ia&ya; —  ■)  Ein  et.  Versuch  bei  vünISradke  IF. 4.  SS.
•  j.  zävar-  n.  '(physische)  Krafl,  Stärke': 'var»  aojaiia  Yt  13.  i ;  10.  62,  F.  20\  —  : aojas'a  zavanca"^  Y.  72.  6;  7J.  8,  Yt. i,sz.  a)  insbes.  a)  der  Ftlsse^;  yat kl  da'i^at  .  .  patave  'vars  YL  16.  7 ;  Y.  ^. a8;  —  apa  pälayä  "var>  (näml.  barahi) Yt  ro.  23.  b)  der  Rosse:  'van  dayä' hitaiibyö  Y.  57.  26;  Yt  iO.  1 1 ;  —  yS  mqm
z«mana-  1690
^"fdtnäni  N   ,ro-  lies  ,arSJ.nä^  "  S-   dug»dM-,  j.   do^^r-  C  Tochter':
...       _  ,    ,      .,  ,    .  /"»'*  *7''J  ^'i^  "^-'S.  3;  (,  4:  —  j^atfha
•  j.  Oim  Part  1)  der  Hervorhebung:  /.in  ,,j  .  -     ^.jy         ,c-F  ■■£-   ,0/  'firam
f  «'«>"^£«''"^  ■-."'■■  "d^n  sollst  'k^(s^'^f,:^]^XA_2',-asim..'TL;^m du  einen  Pnester  oennen.  .  .  der  . ."  \ .  „^^^^^^  ^^j  y^  _  _  ^  ^„^'  ^^ iÄ6;  -  <7/^r^  (^)  .  .  m  d'a2-a>a  f„^^  sr»,«/i,7)  -y«»  <»>l«r<7^  »,«,/J  V. /«/,««  fsd.)  y.75.48;  -  yat  hanö  -  .,,^.,3.  _  ^^  ^^^  .nämL  maUh)  'g^ä bm-äl  aojjst^mca  d-  pascaaa  mazdayama  ^^^„„^^„3  s„naitis  Y.J3.4;  —  Pm.ru- tanast,mca    .  .  pastö.fra^a»,h^   (sd.)    h!    .^^^.  .^,^   ,^^^^    far^i^^^  
•  ].,  g.  (,  p.)  'mätar-  f.  'Mutter*:  yai  pits .  .  'ta  vä  paradrUyäti  hat  a^qm  upa.- manaytn  (sd.)  pukrS  haia  pilarvm  duyta^ haca  Uanm  V.  12. 1 ;  3,  F.  2,  6;  —  pita  tl (n
KompE.  —  ai.  mätär-  f.,  np,  mädar.  —  Pii, : niälar;  s.  noch  No.  I.  —  •)  Zu  Y.  jS.  5 werden  die  Worte  von  Pii.  als  EN.  genommen und  traniskribirl  1  dabei  zu  mäOrqi  die  E
•  p.  mä-tya'*  neg.  Konjn.  mit  Konjv.; 1)  hinter  einem  regierenden  Satz  mit  ava- hyarädiy  'dass  nicht,  damit  nicht':  ava- hyarädiy  naiy  nipistam  tn'  hyi^  . .  avahyH paruv  *%aday
j.  "«DO-gm  Vyt.  JO;  %.  "aita.in'.
```


## [2026-10-15T02:45:23.311Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"theft\\|thief\" PHD.txt | head; grep -n \"mādar\\|pidar\\|duxt\\|brād\\|dāmād\" PHD.txt | head -20"
}
```


### [2026-10-15T02:45:23.647Z] TOOL RESULT

```
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
3970:theft appar(išn), duz(d)ih.
3976:thief duz(d), gég.
275:*brādarod [bPtlwt!'] relative, rival, counterpart. “АҺ: relationship, rivalry.
308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
439:~ith: femininity. *madag [mtk' | (M myg, N māya)] essence, substance. ~ig [-yÀ!] essential. ~war [-w/] essential, especial, principal. madan [mtn! | M mdn] come. madār [т comer. mādar [AMYtl < А т-у; mtl | M mdr, N ~] mother. imādayān [m!tgd?n! | М m'dy'n] book. *mādayān [m tyd?n'] essence, basis, core; essential, chief. mādayār [m tgd’l] steward; (chess) rook, castle. mādišt [m’tyst'] *matter, protoplasm. mādīyān [m’tyg?n | N ~] mare. may [my | N ~] hole, pit. magas [mks | P mgs, N ~] fly. ~ i angubén: honey-bee. magind [mkn'd | M mgyn(d)] shield, protection.
549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
1494:daughter duxt(ar).
3370:relationship brādarēdih.
3458:rival brādarēd.
3459:rivalry brādarēdīh.
4885:mādayār mādišt mādagīh mādagīg 1*mādag mādagwar mādar Abt, mex ābgēnag! mēhan mēzd may, meh Sahrestan! ‘mahist men- moymard! menidan mënög
5468:gūhragdānāg gohrag dwāzdahān dwāzdah duxt, Just 1-*dūxtun duxtar ldaw-, gūw- gūwāg 12а} dwàr- dwārīdan dwiristan dwārišn jy)
5550:dāmādīh
5551:dāmād
```


## [2026-10-15T02:45:27.286Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{80\\}tlpt.\\{120\\}\\|.\\{80\\}trift.\\{120\\}\\|.\\{80\\}tirift.\\{120\\}\" PHD.txt NYB_vol2_glossary.txt | head; grep -n -o \"brād \\[.\\{150\\}\\|brādar \\[.\\{150\\}\" PHD.txt | head -3; grep -n -o \".\\{20\\}brātar.\\{150\\}\\|.\\{20\\}brāt .\\{150\\}\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-10-15T02:45:27.767Z] TOOL RESULT

```
NYB_vol2_glossary.txt:3799:nifications, the former must be regarded as borrowed from Av., and consequently tlpt is best interpreted as trift, not as tirft as Bthl has it. This is confirmed by the parallel form tlwpt = truft with -r
NYB_vol2_glossary.txt:3799: to me: 1. inf. tlwptn! = truftan DkM 364U (+ bwrtan, cf 11214 just quoted); 2. tlpt'l = triftär Phl. Y 291: 3. tlwptk = truftak BAA p. 2418; 4. tlptkyh = triftakéh, v. above; 5. tlp- tynytn' = trifténita
1021:2"; — sg. cas. obl. brātar [bl”tl] in compounds (v. below); in the sense of a pl. after nume- rals: har 2 brdtar 9%, hàn 4 brätar 9!? (both dir. obj.); — pl. cas. obl. brätarän
```


## [2026-10-15T02:45:30.390Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3795,3799p NYB_vol2_glossary.txt | cut -c1-2500; grep -n -o \"brād.\\{100\\}\" PHD.txt | head -5; grep -n -o \".\\{10\\}pidar.\\{100\\}\\|.\\{10\\}mātar.\\{80\\}\\|.\\{10\\}duxtar.\\{80\\}\\|.\\{10\\}dāmāt.\\{80\\}\" NYB_vol2_glossary.txt | head"
}
```


### [2026-10-15T02:45:30.818Z] TOOL RESULT

```
triftak&h
195
Türän
triftakéh [tlptkyh] stealing: apāc kuntš- [ Tür [twl] the name of the hereditary
neh u burtäreh u ~ 11214. — Av. (643) tarop- ‘to steal’. subju. trofyāt (Y.115; a hapax) < *trpydt with secondary develop- ment of -r- to -ra- (tr- is only secondary in Olr) Cf NP tarb, tarfand ‘deceit, fraud, lie’. As the BP derivatives of this root semantically agree with Av., whereas the derivatives outside this group have other, non-technical significations, the former must be regarded as borrowed from Av., and consequently tlpt is best interpreted as trift, not as tirft as Bthl has it. This is confirmed by the parallel form tlwpt = truft with -ri- > -ru- be- cause of the labial. I give here the BP forms known to me: 1. inf. tlwptn! = truftan DkM 364U (+ bwrtan, cf 11214 just quoted); 2. tlpt'l = triftär Phl. Y 291: 3. tlwptk = truftak BAA p. 2418; 4. tlptkyh = triftakéh, v. above; 5. tlp- tynytn' = trifténitan "to commit theft’ Phl Y. 115 (translation of trofyāt); 6. tlpt = trift ‘theft’ explaining Av. (638) taya-.
1064:thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have su
1413:cas. obl. duxtar [dwhtl] 152°; 6 duxt [BRTH] 957; hac pus tài ~ both sons and daughters 24?3, Av
4522: man hac mātar nē zat hom 2111-12. Artaxsér haciš zāt 27°; haciš pus . . . zāt 1075; — the pre
```


## [2026-10-15T02:45:33.865Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"\\[pdf page\" SOD_pages.txt | head -3; grep -n -i \"to steal\\|stolen\" SOD_pages.txt | head -20"
}
```


### [2026-10-15T02:45:34.485Z] TOOL RESULT

```
12772:        stolen                  r                                        grasped
39550: stolen 3170                               stupidity    4651, 10070                supplies 7471, 7475
```


## [2026-10-15T02:45:36.314Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 12740,12790p SOD_pages.txt; grep -n \"^ *3170\\b\\|3170 \" SOD_pages.txt | head"
}
```


### [2026-10-15T02:45:36.690Z] TOOL RESULT

```
                                                                                                              J aiOS— <<Ua>*J>-




                                                                      BSTii 849.16, 851.3; C2 gloss, n p55
3154 c'r6»p'6w B                          U^oL*-
     car0a-pa8u ^cyrSp^w, crfip'Syh                              3165 *cVnty =» c'wnc
     quadruped                                                   3166 cNvysn B                                          LtsTjl
     VJ 1178; GMS 111, 440; Gersh. Sogd. Cpds. 139,                   cawes(a)n   =»c}-, wysn
       149                                                            of them
3155 cV C                                                             TSP 2.89
     casa ©<caSarsar ©adv. -^c's'r                               3167 cp- B
     downwards
                                                                      cof ©<*rr/?; Khwar. ycfy ©inf. -y,
     BSTii 826.8; C2, 94R8
                                                           j±\        (/^Osteal                               -y =*cf-
 125                                                                                                                     ckkr

        GMS 150, 277, 508, 610; TSP 526, 79; SCE 156,                3180 cyr-  B, S                             <^><£>r
          159, 161; AVS 108                                               caxr ©ace. -w; nom., ob. -y(h) =>cxr-, ckkr
 3168 cpt- B                                              jjbi>           wheel, circle
      capd ©pt, st.                                                       TSP 2.144, 216, 924; Frag. Len. 93.17: O2 17
      GcOsteal                                                       3181 cyrh =* syrh
      TSP 5.112,7.138
                                                                     3182 cys- S                              j*f<&fsSj>
 3169 cptVmyk B                                            fJl^           caxs ©pt. cYsty ? ^'c'xs-, ptexs-
      caftarmik ? ^ctP'rmyk                                               0o)take, (to)grasp
      fourth                                                              MDii pl27npl28, 8
      GMS 442; TSP 2.326                                             3183 cysty S                                     •jzSj*
 3170 cptw      B                                         .jojji          caxste ©pp. =»cxsty
        ca(3du, caftu ©pp. =*cpt-
        stolen                  r                                        grasped
                                                                         MDii pl27 n pl28; cYsty m'tym, lsg. perf. B16.8
        TSP 5.112,7.138                                             3184 cywty B                      (^<a*i;jL^.>)ju^
                                                                         cayut
 3171 c6-(\v)      B    L jfji JjjjT uX )ljjljl* JL-^^^-^U
                                                                          owl
                                            \oJj>~ ij->b- *_S-^-<
                                                                          SCE 148; Hen. LW 96
        j/ca5(u) ©Khot. jaya\ Turk, yada <*yatu ?
        magic                                                       3185 cyz-    B                    (>^ .-J^^^y
        TSP 3.123 n pl95; Bailey. BSOAS 15, 533
                                                                          cayz ©Yaghn. caYz ©ace. -w; abl. ->
 3172 c8y k>ry B                                ^,/^U                     frog, toad
      ca6y-kare, ja5e-kare                                                TSP 3.250; SCE 178; Hen. L W 96
      magician                                                      3186 cyz r'yh S                        («Ljy"cJ.j)Jv
      TSP 3.231, 240; Hen. Sogdica. 5                                    cayz- ray ^r'y
                                                                         marsh land
3173 cf-     M,S                                         j±>p
       C3f   ->Cp-                                                        Gersh. Melanges Benv. 196ff; MDii B16, 8
12770: 3170 cptw      B                                         .jojji          caxste ©pp. =»cxsty
39550: stolen 3170                               stupidity    4651, 10070                supplies 7471, 7475
```


## [2026-10-15T02:45:41.179Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for f in BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt MON_part1.txt MON_part2.txt incoming/ARY/ARY_pages.txt; do echo \"== $f\"; grep -n -o \".\\{60\\}تولف.\\{120\\}\" $f | head -5; done; grep -n \"tulf\" HRN.txt HUB.txt | head"
}
```


### [2026-10-15T02:45:41.693Z] TOOL RESULT

```
== BQT_v1_pages.txt
== incoming/BQT/BQT_v3_pages.txt
== incoming/BQT/BQT_v4_pages.txt
== incoming/BQT/BQT_v5_pages.txt
== MON_part1.txt
== MON_part2.txt
== incoming/ARY/ARY_pages.txt
```


## [2026-10-15T02:45:45.739Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"sättigung\\|übersatt\\|ubersatt\\|tulf\\|tolf\" HRN.txt HUB.txt WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt | head; grep -n \"تولف\\|تُلف\\|تلف \" BQT_v1_pages.txt BQT_v2_pages.txt | head -5"
}
```


### [2026-10-15T02:45:46.241Z] TOOL RESULT

```
incoming/WLD/WLD_Bd1_pages.txt:30870:„Hitze gebend", kaitulf/s 1. „aufbrausender Mensch", 2. ..Drehkrankheit
BQT_v1_pages.txt:664:است.قابل توجه است در یتخصوص باد آور شویم که سه نام مختلف بر ای‌ملخ
BQT_v1_pages.txt:744:ملحق میشودواین‌دسته خطوطموجب پیدایشاشکال مختلف پپلویومخصوصا
BQT_v1_pages.txt:1090:مز بوردر فرن‌های درم وسوم هجری غالبا ازانحاء ابران و لهجه‌های مختلف این کشور و زبان عای
BQT_v1_pages.txt:1440:« وزبان های ایشان؟ مختلف است . اما ز بان نیشابور فصیح و مقبوم
BQT_v1_pages.txt:1478:نز ديككاست زبان روستاهای بخار ا. و انز بان سبی مختلف و نزدمر دم بخارا|
```


## [2026-10-15T02:45:50.473Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"terp-\\|terp\\b\" incoming/WLD/WLD_Bd1_pages.txt | head; grep -n \"māter\\|mäter-\\|pəter-\\|bhräter\\|dhughəter\\|dhug(h)əter\\|dhughэter\" incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt | head"
}
```


### [2026-10-15T02:45:50.991Z] TOOL RESULT

```
69194:         terp-, trap- (nur bsl.):                            lett. iar/is            ,(\Yurm ',       £
69197: Liieke. Ivluft", tarp. terp ,,zwischen £ :                                          lit.   fra pus ,,sprode, leicht                             brechend \   £
69503:736                                                                                         terg"                              terp-
69658:    terp-      .,sich siittigen,                         genieBen 14                        .
69701:                                       *tnp- zu bestimmen oder ptafsfjau aus                         :   terp-,
80783: ster-, sterp- „starren“), gcd 'orf  deorf n. „Arbeit, Miihsal“, lit. d'nbii. d'trbfi
```


## [2026-10-15T02:45:52.843Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 69655,69700p incoming/WLD/WLD_Bd1_pages.txt | tr -s ' ' | head -60"
}
```


### [2026-10-15T02:45:53.477Z] TOOL RESULT

```
 terp- .,sich siittigen, genieBen 14 .


 44
 Ai. trpijati, trpnoti , trmpdti , turpati , siittigt sich. wird befriedigt ,
 Kaus.
 tarpuyati ., siittigt, lobt, befriedigt 44
 , trpti-li trpfi-h .,Sattigung, Geniige, Be-
 h :




 --'
friedigung, UberdruB ; av. Qrafdu- ,,befriedigt, zufriedengestellt, ausreiehend
womit verseken” {ptramptha- ai. trmpdti), Dr/tfs- n. ,,Zufriedenheit gr. : ‘
 ;

 --
zigmo ..siittige, erfreue zegno/tai ,,freue mich '; lit. tarpa ..Gedeihen,
Wachstum --
 tarpsiu tarpau tnfpti .gedeihen, zunehmen (von Menschen,
 . , ,

 lett tarpa „was gute Hoffnung gibt, Gedeihen, Wachs-
 --
Tieren, Pflanzen) ,

 :<
tum”, tErpiudt „verbessern'\ pr. enterpo ,,nutzt ,
 mterpon ,
 enterpen ,,niitz-

lich ‘. Z. B. Trautmann Wb. 314 (verfehlt iibeL‘ vermeintl. Anlautsdoubletten
Lewy KZ. 40, 420). — Aus dem Germ, vielleielit got. prafstjan .,trosten,
ermahnen' -
 ', anuprafstjan welchen- .erquicken, zur Rube kommen lassen --
 .




falls die Wz. als *terep-
```


## [2026-10-15T02:45:56.895Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"milk.\\{0,40\\}daughter\\|daughter.\\{0,80\\}milk\\|-ter-\\|-ter, \\|suffix -ter\" SYN.txt | head -20"
}
```


### [2026-10-15T02:45:57.403Z] TOOL RESULT

```
2558:In the inherited group the suffix -ter- or in some cases -er-, -or-, is conspicuous (cf. Skt. pitar-, matar-, bhratar-, duhitar-, jamatar-, yatar-; devar-, svasar-). Owing to the well-known use of this suffix in agent-nouns, these words of relationship were also formerly interpreted as agent- nouns from certain roots, e.g. ‘father’ as ‘protector’, ‘mother’ as ‘measurer, thoughtful one’, or the like, ‘brother’ as ‘supporter’, ‘daughter’ as ‘milker’, either the ‘suckling’ or the ‘milkmaid’, etc. Most of these derivations now seem fan- ciful and pointless and are generally given up. The use of the suffix is not to be connected directly with its use in agent-nouns, but rather with the use of -tero- (-ero) in words of contrasted rela- tionship, like Lat. dexter vs. sinister, nos- ter vs. vester, etc., that is, it was used in words for ‘father’ and ‘mother’, etc. as contrasted terms. Cf. Streitberg, IF 35.196.
25251:Several of the words for ‘again’ have such obvious semantic sources as ‘an- a time, a second time’, or ‘anew’. a the most striking development is ie the notion of ‘back’ or ‘against’, ee ‘back again, returning’. » Gtk. raw, in early use ‘backwards’, a 8g. of a *rddts ‘turn’ : rédos ig Walde-P. 1.515. Boisacq 748. org ee fr, the freq. prefix fava-, i denoting repetition. ae i ret, fr. *i-tero-, pron. stem relation a Suffix -tero- of contrasting tout exter, ete.) Walde-P. 1.100. oe £99. Walde-H. 1.723 f. ue™0 “anew’ and so freq. ‘again’,
25279:Du. weer, OHG widar, MHG wider, also and orig. ‘against’, like OF wiper : Goth. wipra ‘opposite, in the presence of’, Skt. witaram ‘further’, fr. *vi- ‘apart’, in Skt. vi-, etc., with suffix -tero- in words of contrasting relations. NHG wieder, wiederum, with differentiated spelling for sense ‘again’ vs. wider ‘against’. Walde-P. 1.312f. Feist 570. Weigand-H. 1255.
```


## [2026-10-15T02:46:08.072Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o \"māter-\\..\\{300\\}\\|mater-\\. .\\{300\\}\\|pəter-\\..\\{300\\}\\|pater-\\. .\\{200\\}\\|dhugh[əa]ter-\\..\\{300\\}\\|bhrāter-\\..\\{300\\}\\|bhrater-\\. .\\{300\\}\\|gem[əa]-\\..\\{200\\}\" AHD_watkins1985.txt | head"
}
```


### [2026-10-15T02:46:08.468Z] TOOL RESULT

```
mater-. These terms are ultimately derived from the baby-talk sylla- bles pa(pa) and ma(ma), but they had a socio- logical significance in the Indo-European family over and above this, which is marked by the kinship-term suffix -ter-. Related terms are found for the grandfather (awo-) and the maternal uncle
bhrater-. Brother, male agnate. 1. Germanic *brdthar- in Old English bréthor, brother: BROTHER. 2. Latin frdter, brother: FRA, FRATERNAL, FRIAR; CONFRERE, FRATRI- CIDE. 3. Greek phratér, fellow member of a clan: PHRATRY. 4, Sanskrit bhratd, bhrdatar-, brother: PAL. [Pok. bhrdater- 163.] bhreg-. To break. 1. G
mater-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -fer-. 1. Germanic *méthar- in Old English mddor, mother: MOTHER}. 2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRI- MONY. 3. Greek métér, mother: METRO-; METROPOLIS.
```


## [2026-10-15T02:46:11.441Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o \"dhug.\\{0,3\\}ter-\\..\\{400\\}\\|p.ter-\\. Father.\\{400\\}\\|gem.-\\. .\\{150\\}\" AHD_watkins1985.txt | head -4; grep -n -i \"^.\\{0,5\\}mātēr\\|māter\\b\\|pəter\\b\\|dhughəter\\|bhrāter\\|gem[əe]-\" IEC.txt | head"
}
```


### [2026-10-15T02:46:12.734Z] TOOL RESULT

```
geme-. To marry. Suffixed zero-grade form “gmoa-o- in Greek gamos, marriage: GAMETE, GAMO-, -GAMOUS, -GAMY; GAMOSEPALOUS. [Pok. gem/(e)- 369.] gen-. To compr
10369:mātēr (màter-, mātr) (1) ‘mother’. Cf. maté and mati. WP II, 229 Skt. matt; Ober matar; Per. madar; Oss. cf. mad, madà; Tokh. macar, B macer; Arm. majr, gs mawr, ab. s. marb; Myc. matere(i), ds; Gk. méter, gs métrós; Doric mater; Phryg. māte- res, pl.; Alb. motër 'sister'!; Lat. mater, gs matris; Osc. maatreís, gs; Umb. matrer, gs; (?) Faliscan materei, ds; Olr. máthir, Ir. má- thair, gs máithre; Gaul. matre-bo, dpl.; W cf. modr-yb (“aunt', fr. *màtriqua); OHG muoter; OE moóor, ds meóer; ON móðir, gs móður & moeór; OCS materi beside mati, gs matere; Slovak mat, mati & mater; R mat, gs materi; Li. móte, gs móters & móteris, f. ‘woman’; cf. móčia ‘mother; Latv. (isophone) materes, pl. Cmotherwort', bot.)
10382:māter- (3) (?) ‘pad, coating MHG muoder, müeder, m. n. ‘corselet (mod. Mieder); OFris. mother, n. id.; if related to mäter (1), cf. Lat. måtrix, Gk. métrà and G Perl-mutter, E mother-of-pearl. (In sense of “lees, dregs’ cf. E mother, Du. moer (2) and Fr. mère de vinaigre, Moravian z-matetely *mouldy'. The semantic link is obscure)
```


## [2026-10-15T02:46:15.911Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{5\\}Mutter.\\{200\\}\" HRN.txt | head -3; grep -n -o \".\\{5\\}Schwiegersohn.\\{250\\}\\|.\\{5\\}Eidam.\\{250\\}\" HRN.txt HUB.txt | head -4; grep -n -o \".\\{5\\}'Tochter'.\\{200\\}\\|.\\{5\\}„Tochter.\\{200\\}\" HRN.txt HUB.txt | head -4"
}
```


### [2026-10-15T02:46:16.755Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:46:19.328Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"mutter\\|tochter\\|schwiegers\\|bruder\" HRN.txt | cut -c1-250 | head -20; grep -n -i \"dämäd\\|dâmâd\\|dämäd\\|dāmād\\|duxtar\\|dukhtar\" HUB.txt | cut -c1-250| head"
}
```


### [2026-10-15T02:46:19.778Z] TOOL RESULT

```
2091:ü:^. hiräder *Bruder .
2092:a ap. hrätar^ *Bruder' ; aw. bratar^; phlv. brätar, brät ^);
2095:*Bruder, t. arwäd 'Verwandter* (30); bei. brät n.
4418:skesr]ah\ d. i. 'Mann der Scliwiegermutter (Hübsch-
4424:487. xusrfi, zesä^ /jisü^ /'es etc. 'Schwiegermutter.
4426:ai. <;DarrU' 'Schwiegermutter'; arm. akesnr (H. No. 253) ;
4428:kuvd. /ost, /esü, yasrü 'Schwiegermutter; af/. ;K''ö4fa ;
4774:532. dämäd 'Schwiegersohn; Bräutigam (Vis und Käniin,
4778:aw. zämätar- 'Schwiegersohn'; phlv. dämät; ai.
4825:kurd. da^ dl, diyä 'Mutter*, drUn Mutter, Amme*,
4844:54 L diiy^ter, du/t 'Tochter'.
4845:aw. diiydar- 'Tochter'; phlv. dtt/t^ vergl. arm.
7114:816. ferzend 'Spross'. sowohl *Sohn* als auch 'Tochter (N'is
8274:956. niädei; mrul (Patet's) 'Mutter, inäch, mfidlne 'weib-
8276:ap. ^mätar- in hamätil 'von der gleichen Mutter ;
8277:aw. rndtar-; phlv. inät, mätar 'Mutter, mätak Veib-
8280:kurd. mak {*mädk) 'Mutter, mOdek 'Büffelkuh'; af;'.
8282:n. mad-j was 'Mutter (234), LW. maday, n. maday
8322:963. mäm 'Mutter' (Öähn. I, 41 Vers 129 u. o.), mama^),
8324:cambr. corn. arem. mam 'Mutter; lit. mäma, momä
4099:ap. *duxtd neben duxtar -— ap. *diixtaram (vgl. auch pad-andar *Stief-
```


## [2026-10-15T02:46:22.807Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2088,2092p HRN.txt; sed -n 4774,4782p HRN.txt; grep -n -i \"'Vater\\|\\*Vater\" HRN.txt | head -5"
}
```


### [2026-10-15T02:46:23.335Z] TOOL RESULT

```
*Brust' gebildete nominale Praeposition und upari zu-
sammengeflossen sind. Np. her- kommt auch als Prae-
fix vor.
ü:^. hiräder *Bruder .
a ap. hrätar^ *Bruder' ; aw. bratar^; phlv. brätar, brät ^);
532. dämäd 'Schwiegersohn; Bräutigam (Vis und Käniin,
S. 46, Vers 4 v. u. folg.)'.
g. zümäd; gel. zamä, zemö Schwager'; Käs. zUmo,
zümod, zümoi,
aw. zämätar- 'Schwiegersohn'; phlv. dämät; ai.
jdwätar-,
kurd. zawä; af/. zäm, zümgai; bei. zämcLS^, n. Jan-
wa^ (420).- 118 —
533. ~dän 'Behälter , vergl. äbdän, nemekdän etc.
2347:vielmehr das arabische ebu% bu'l 'Vater des . . . .' ist,
2804:286. pider (peder) 'Vater'.
2806:ap. pitar- 'Vater'; aw. pitar-; phlv. pit, pitar (in
2808:pitar- ; arm. hair 'Vater* (H. No. 155).
2809:kurd. pier^) 'Vater'; af;'. plar\ oss. d. fidä, t. fid
```


## [2026-10-15T02:46:26.578Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2080,2087p HRN.txt; grep -n -o \".\\{30\\}Muse.\\{100\\}\" SKT.txt | head -3; grep -n -i \"^terpsichore\\|^euterpe\" SKT.txt FSD_vol4.txt | head"
}
```


### [2026-10-15T02:46:27.162Z] TOOL RESULT

```
2) Phlv. barin 'höchster*.— 45 —
ap. upariy 'über; aw. upairi; phlv. apar, päz. awar,
apartar, apartum; ai. upäri.
kurd. her; af/. pre- (LW. bar); oss. d. uol, t. 0/ *das
Obere*, välä Postpos. auf, über* (253) ; bei. par n. par
(283), resp. gvar (136); wa/. sar. war,
Geiger, Etymol. des Balü^i s. v. gvar (136), macht
darauf aufmerksam, dass in np. her eine von her
```


## [2026-10-15T02:46:31.644Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"dâmâd\\|dāmād\\|zâmâtar\\|zāmātar\\|zamatar\" BQT_v2_pages.txt | head -5; grep -n \"duxtar\\|dughdar\\|duγδar\\|dugh\" BQT_v2_pages.txt | head -5; grep -n \"pitar\\|brâtar\\|brātar\\|bratar\" BQT_v1_pages.txt | head -5"
}
```


### [2026-10-15T02:46:32.055Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:46:34.545Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^داماد\\|داماد ب\\|داماد -\\|داماد ‌\" BQT_v2_pages.txt | head -5; grep -n \"^دختر\\|دختر ب\" BQT_v2_pages.txt | head -5; grep -n \"^برادر\\|^پدر\\b\" BQT_v1_pages.txt | head"
}
```


### [2026-10-15T02:46:35.073Z] TOOL RESULT

```
18775:‫داماد بخانة عروس میفرمتد ‪ -‬و مهری را نیز‬                        ‫دست بنرحن ‪ = ۱‬دستینه ای باشد‬
37584:‫و بمعتی رشته مروارید و رشتةٌ سوزن باشدخصوصاً‬          ‫بمهیمرسد ‪ -‬و بکر اول یمعتی هم‌داماد باشد‬
2732:‫بود ‪-‬‬     ‫یمن فرستاده‬     ‫بخواستگاری دختر بادشاه‬
7742:‫دختر بپمن مادردار اب ناشلت و نام دخشس افراساب‬                ‫چهار منقو طه کنابه ازفلك کرسی‬
16825: ‫انگور ودانه انگورهم آمفه است که بعربی علب‬         ‫گاهی را‬        ‫دختر باشد ‪۴‬‬        ‫است که مخقف‬         ‫دخت‬
21276:                                                                                                 ‫دختر بکر را گونند ‪۰‬‬
26713:                                                                 ‫پبر هم هت که نقیض دختر باشد ‪ ۴‬و‬
188:پدرو نیا کان خو دراچنین پادمیکند: « بدر من و بشتاسب کشناسب) بوده پدرو یشتاسب
190:پدر چیش پیش هخامنش بود . از ایثررست که ما هخامنشی خوانده شدیم »
11095:برادر کوچك کاوس باشد .
12889:برادر اقراسیاب‌بن پشنگه‌ین ورین آفرربدون‌است
15829:پدرهم آمده اس تکه‌بمربی والد کویشد ؟ » وباین
22339:برادر و پهلوان و شجاع باشد- و بش کی يك را
24167:پدر پاشد؟ - و ختح اول درختی را گوبند که
27908:برادران را بوسف چو داد گندم وجو
29650:برادر پیاز است که بمربی وم وفوم‌خوانند
31886:برادر پیاز دا گوند » و بعربی نوم و فوم
```


## [2026-10-15T02:46:38.991Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -i \"MADAR\\|PEDAR\\|DOKHTAR\\|DOXTAR\\|BARADAR\\|DAMAD\" ARY_latin_index_pages.txt | head; grep -n \"\\[pdf page\" ARY_latin_index_pages.txt | head -2"
}
```


### [2026-10-15T02:46:39.425Z] TOOL RESULT

```
7589:GAM, GAMEO- GREEK) gb y DAMAD, DAMAT — (PAHLAVI) 5 shy
13276:MACER -(TOKHARIAN B) B 5 MADAR, MAD PAHLAVI) 5 shy
1:[pdf page 1]
9:[pdf page 2]
```


## [2026-10-15T02:46:42.329Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; awk 'NR<=7589 && /\\[pdf page/{p=$0} NR==7589{print p}' ARY_latin_index_pages.txt; awk 'NR<=13276 && /\\[pdf page/{p=$0} NR==13276{print p}' ARY_latin_index_pages.txt; sed -n 7580,7592p ARY_latin_index_pages.txt; grep -n \"داماد\\|مادر\" ARY_pages.txt | head"
}
```


### [2026-10-15T02:46:42.814Z] TOOL RESULT

```
[pdf page 262]
[pdf page 455]
SKEAT: (TAME) 628 ZAHM, ZAHMEN — (GERMAN) (jlJT
MALLORY & ADAMS: DEMH- HOLD ENGLISH) 4 gdSt
AW ebb olay ‘TAM, TEMIAN
: leadlaak
B27 8s 45 92 o5ls col
ae
|
|
JAMATAR SANSKRIT) ey Suite ZAMATAR HAVESTAN) ikea 3\ :
GAM, GAMEO- GREEK) gb y DAMAD, DAMAT — (PAHLAVI) 5 shy
GENER LATIN) ga) ZAWAT (KURDISH) 2,6 |
GENORE (FRENCH) 4318 JAMATH, JANWATH :(BALUCHI) gz sh '
YERNO (SPANISH) lily! ZOM, ZOMGALI (AFGHAND (5) lil
107:پوست هستند ولی زبان مادری بیشتر آنها یک زبان هند و اروپایی (یعنی اسپانیایی) است. :
302:همریشه» همگی دارای بک معنی نیستند. واژه‌های معدودی مانند «مادر» و دماه» و «گاو» در همه
412:۸ کهن مادر,زبانهای |سپانیایی و ایتالیایی و پرتغالی و غیره هم هست. بدین روش کم کم بیشتر زبانهای
1000:خانوادگی آنها بر پایه‌ی خانواده (پدر و مادر و فرزندان)» خانواده‌ی گسترده (پدر بزرگ‌ها و دایی‌ها
1022:بودندکه با تأید و تحت نظ رکاهتان انجام می‌شد. ضمناً ازدواج نوعی معامله هم بود: داماد یا ایل او به
1053:فرزندان و دوردازی دشمنان و پیماری‌ها هم بود. نیمه خدایی بودن شاه (معمولاً با مادرش الهه بود یا
1274:«مادر) یا «گاوه با «بوغ) معنی واژه‌های همریشه در زیانهای هند و اروپایی امروزی کاملدً یکی و
3778:۱ چم این وازه در لیتوانی: ولد» پدر پا مادر.
4628:پدر و مادر پدران (به چم / ۱۵۹
9336:چم این واژه در زبان اسلاوی کهن: شوهر دختر والدین؛ داماد,
```


## [2026-10-15T02:46:49.101Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/terp-' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-tḗr' 'https://en.wiktionary.org/wiki/داماد' 'https://en.wiktionary.org/wiki/دختر' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰugh₂tḗr' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰréh₂tēr' 'https://www.etymonline.com/word/Terpsichore' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ph₂tḗr'; do python3 tools/fetch_source.py \"$u\" --note \"page 505: Ter 3 / Terp verification\" 2>&1 | tail -2; done"
}
```


### [2026-10-15T02:46:53.853Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1688d03b703f37a3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cbaddd6e4969e015.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ce5ca6174cfa25b7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7106d17713cfc096.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8aabbd8a504d1590.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2a2c86ba905b5dd1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/721b0fe897c0e0ea.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1d93b84f15c32675.txt
```


## [2026-10-15T02:46:56.680Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 1688d03b703f37a3 cbaddd6e4969e015 ce5ca6174cfa25b7 7106d17713cfc096 8aabbd8a504d1590 2a2c86ba905b5dd1 721b0fe897c0e0ea 1d93b84f15c32675; do echo \"=== $f $(wc -c < $f.txt)\"; grep -i -m8 \"etymology\\|from \\|inherited\\|borrow\\|cognate\\|Iranian\\|Avestan\\|Persian\\|Sogdian\" $f.txt | cut -c1-300; done"
}
```


### [2026-10-15T02:46:57.059Z] TOOL RESULT

```
=== 1688d03b703f37a3 4891
 From Wiktionary, the free dictionary
 Terms derived from the Proto-Indo-European root *terp- (30 c, 0 e) 
 Proto-Indo-Iranian: 
 Proto-Indo-Iranian: 
 Proto-Indo-Iranian: *tr̥ptíš 
 Proto-Indo-Iranian: *tr̥ptás 
 ^ Ringe, Donald ( 2006 ), From Proto-Indo-European to Proto-Germanic (A Linguistic History of English; 1)‎ [1] , 1st edition, Oxford: University Press, →ISBN 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/terp-&oldid=92171665 "
=== cbaddd6e4969e015 4558
 From Wiktionary, the free dictionary
 Derives agent nouns from verb roots, denoting someone or something whose role or purpose it is to perform the root's action. 
 Proto-Indo-Iranian: *-tā́ ( partly merged with *-tōr ) 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/-tḗr&oldid=91828036 "
=== ce5ca6174cfa25b7 10844
 Persian 
 Toggle Persian subsection 
 Etymology 
 Etymology 
 From Wiktionary, the free dictionary
 Persian
 Persian Wikipedia has an article on: داماد 
 Etymology
=== 7106d17713cfc096 12361
 Persian 
 Toggle Persian subsection 
 Etymology 
 Etymology 
 From Wiktionary, the free dictionary
 Persian
 Etymology
 Etymology tree
=== 8aabbd8a504d1590 11396
 Etymology 
 From Wiktionary, the free dictionary
 Etymology
 Perhaps from *dʰewgʰ- ( “ to produce ” ) , originally meaning "the (potential) suckler, the one that draws milk" (compare Sanskrit दुहे ( duhé ) / दुग्धे ( dugdhé ) ), +‎ *-tḗr , the agentive nominal suffix common to other r-stem kinship terms.
 *dʰugh₂ter- on the basis of: PIIr. *dʰugHtar- (Sanskrit duhitár- , PIr. *dʰugʰtar- > *dʰugdʰar- > *dugdar- > Gathic Avestan dug ə dar- ), Ancient Greek thugátēr -, Tocharian A ckācer , Tocharian B tkācer 
 *dʰukter- on the basis of: Iranian *duxθrī (> Old Persian *duhçī ) and *duxtar- (> New Persian duxtar ) due to the absence of Bartholomae’s Law , possibly Gaulish duxtir , Gothic dáuhtar , Oscan fu-utreí (dative singular), Armenian dustr , Hieroglyphic Luwian t(u)watra/i- , Lycian kbatra- , Slavic 
 The nominative stem is also possibly also attested in the palatalization of the initial consonant of Tocharian A ckācar ( cf . Tocharian B tkācer ), which is usually explained as a distant assimilation to the palatal in the second syllable. After the split of the Anatolian (and possibly Tocharian) 
 Proto-Indo-Iranian: *diwás dʰúǰʰitā 
=== 2a2c86ba905b5dd1 8357
 Etymology 
 From Wiktionary, the free dictionary
 Etymology
 Etymology proposals
 Pinault proposed that the term reflects a noun *bʰréh₂ ( “ group of males borne to the same mother ” ) + *-tēr . The form *bʰréh₂ would itself derive from *bʰer- ( “ to carry ” ) +‎ *-éh₂ . [ 2 ] 
 Older scholars proposed a connection with Sanskrit भर्तृ ( bhártṛ , “ bearer, protector, husband ” ) , with a sense development from 'protector (of his sisters?)' > 'brother.' This etymology is now known to be phonologically impossible. [ 1 ] 
 This lexeme is widespread, [ 3 ] though absent from Albanian (where it was replaced with vëlla ), [ 1 ] [ 3 ] [ 4 ] and its existence in Anatolian is dubious (see 𐤡𐤭𐤠𐤱𐤭𐤳𐤦𐤳 ( prafršiš ) ).
 Both Sanskrit and Ancient Greek reflexes have a radical accent throughout the paradigm, which indicates that this accentuation was original, and that the PIE word for “ brother ” had an acrostatic inflection. Archaicity of the paradigm is furthermore indicated by the fact that the rest of the inher
=== 721b0fe897c0e0ea 138
=== 1d93b84f15c32675 5670
 Etymology 
 From Wiktionary, the free dictionary
 Etymology
 Often supposed to be from *peh₂- ( “ to protect, shepherd ” ) +‎ *-tḗr ( agentive nominal suffix ) . Alternatively, from a nursery form *pa . [ 1 ] It is possible that both semantic senses have contributed to the development of the term.
 Proto-Indo-Iranian: *pHtā́ ( see there for further descendants )
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/ph₂tḗr&oldid=92171580 "
```


## [2026-10-15T02:47:00.089Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -A3 \"^ *Etymology$\" ce5ca6174cfa25b7.txt | head -12; grep -A3 \"^ *Etymology$\" 7106d17713cfc096.txt | head -10; cat 1688d03b703f37a3.txt | sed -n 1,80p | grep -v \"^ *$\" | head -60"
}
```


### [2026-10-15T02:47:00.445Z] TOOL RESULT

```
 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( dʾmʾt' /⁠dāmād⁠/ ) , from Old Persian *𐎭𐎠𐎶𐎠𐎫𐎼 ( *d-a-m-a-t-r /⁠dāmātar-⁠/ ) , from Proto-Iranian *jā́mātā , from Proto-Indo-Iranian *ȷ́ā́mātā , from Proto-Indo-European *ǵem- ( “ to marry ” ) .
--
 Etymology
 [ edit ] 

 Borrowed from Classical Persian دَامَاد ( dāmād ) . Doublet of جَن٘وَائِی ( jãvāī ) . First attested in c. 1503 as Middle Hindi داماد ( damad /⁠dāmād⁠/ ) . [ 1 ] 
 Etymology
 [ edit ] 

 Etymology tree
--
 Etymology
 [ edit ] 

 PIE word 
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/terp-
FETCHED: 2026-10-15T02:46:50Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/terp- - Wiktionary, the free dictionary
Reconstruction:Proto-Indo-European/terp- - Wiktionary, the free dictionary 
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
 1.2 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ terp- 
 Add languages 
 Reconstruction 
 Discussion 
 English
```


## [2026-10-15T02:47:02.546Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 60,200p 1688d03b703f37a3.txt | grep -v \"^ *$\" | head -60; sed -n '/Etymology tree/,+25p' 7106d17713cfc096.txt | grep -v \"^ *$\" | head -30"
}
```


### [2026-10-15T02:47:03.097Z] TOOL RESULT

```
 1.1 
 Root 
 1.1.1 
 Derived terms 
 1.2 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ terp- 
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
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Root
 [ edit ] 
 *terp- [ 1 ] [ 2 ] [ 3 ] 
 to satisfy 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *terp- (30 c, 0 e) 
 *térp-e-ti ( thematic root present ) 
 Proto-Hellenic: *térpō 
 Ancient Greek: τέρπω ( térpō ) ( see there for further descendants )
 *térp-t ~ *tr̥p-énti ( athematic root aorist ) 
 Proto-Hellenic: 
 Ancient Greek: ταρπώμεθα ( tarpṓmetha ) 
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: अतृपत् ( átṛpat ) 
 *tr̥-né-p-ti ~ *tr̥-n-p-énti ( nasal-infix present ) 
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Etymology tree
 Proto-Indo-European *dʰewgʰ- ? 
 Proto-Indo-European *-tḗr 
 Proto-Indo-European *dʰugh₂tḗr 
 Proto-Indo-Iranian *dʰúgʰHtā 
 Proto-Indo-Iranian *dʰúgdʰā 
 Proto-Iranian *dúgdā 
 Old Persian *duxçī- 
 Middle Persian [script needed] ( dwhtl ) 
 Persian دختر 
 From Middle Persian [Book Pahlavi needed] ( dwhtl /⁠duxtar⁠/ ) , oblique case of [Book Pahlavi needed] ( dwht' /⁠duxt⁠/ ) , from Old Persian *duxçī- , from Proto-Iranian *dúgdā . Cognate with Vedic Sanskrit दुहिता ( duhitā ) , Northern Kurdish dot , Pashto لور ( lur ) , Mazanderani دتر ( deter ) , Baluchi دہت ( duht ) , English daughter .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /dux.ˈtar/ 
 ( Dari, formal ) IPA ( key ) : [d̪ʊx.t̪ʰäɾ] 
 ( Dari, formal ) IPA ( key ) : [d̪ʊx.t̪ʰäɾ] 
 ( Kabuli ) IPA ( key ) : [d̪ʊx.t̪ʰäɾ]
```


## [2026-10-15T02:47:04.672Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 200,320p 1688d03b703f37a3.txt | grep -v \"^ *$\" | head -60"
}
```


### [2026-10-15T02:47:05.288Z] TOOL RESULT

```
 ↑ 2.0 2.1 Kroonen, Guus ( 2013 ), Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [2] , Leiden, Boston: Brill , →ISBN 
 ^ Rix, Helmut , editor ( 2001 ), “ 1. *terp- ”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 636 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/terp-&oldid=92171665 "
 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European roots 
 Proto-Indo-European CeRC-shaped roots 
 Hidden categories: Pages with etymon 
 Proto-Indo-European entries with etymon 
 Pages with entries 
 Pages with 1 entry 
 Sanskrit terms with non-redundant manual transliterations 
 This page was last edited on 24 August 2026, at 00:43.
 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
 Privacy policy 
 About Wiktionary 
 Disclaimers 
 Legal & safety contacts 
 Code of Conduct 
 Developers 
 Statistics 
 Cookie statement 
 Mobile view 
 Search 
 Search 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ terp- 
 Add languages 
 Add topic
```


## [2026-10-15T02:47:25.404Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"import json;d=json.load(open('data/verification/sources/refs_online.json'));print(d['MON'].get('lookup_hint'));print(d['BQT'].get('lookup_hint'))\"; for u in 'https://abadis.ir/fatofa/تولف/' 'https://vajehyab.com/?q=تولف'; do python3 tools/fetch_source.py \"$u\" --note \"page 505 Terp: Persian tulf lookup\" 2>&1 | tail -1; done"
}
```


### [2026-10-15T02:47:27.205Z] TOOL RESULT

```
Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d648565371b96f6c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/48056b14704d77ed.txt
```


## [2026-10-15T02:47:29.147Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in d648565371b96f6c 48056b14704d77ed; do echo \"== $f $(wc -c <$f.txt)\"; grep -n \"تولف\\|تُلف\" $f.txt | head -10 | cut -c1-400; done"
}
```


### [2026-10-15T02:47:29.577Z] TOOL RESULT

```
== d648565371b96f6c 124
1:URL: https://abadis.ir/fatofa/تولف/
== 48056b14704d77ed 3350
1:URL: https://vajehyab.com/?q=تولف
4:TITLE: معنی تولف | واژه یاب
6:معنی تولف | واژه یاب 
51: تولف Tofieldia
54: تولفرا داری
```


## [2026-10-15T02:47:34.278Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"stehlen\\|Diebstahl\" HRN.txt HUB.txt | head; grep -n -i \"tarəp\\|tarep\\|tarap\\|tarf\\b\\|tulf\\|sättig\\|satt\\b\" HRN.txt HUB.txt | head"
}
```


### [2026-10-15T02:47:34.641Z] TOOL RESULT

```
HUB.txt:1636:386. Dazu skr. paguti^p *Vieh stehlend' und KZ. 25, 311.
HRN.txt:3617:stehlen; phlv. tarftlnltan durch List wegnehmen*
HRN.txt:5083:LW. (?) kurd. diz *Dieb', dizhi 'stehlen'; bei. duz,
HRN.txt:6227:ai. skr. l/^sta-^) 'stehlen* in stäi/dt 'verstohlen', stäi/u-
HRN.txt:6229:aw. tayu- *Dieb', taya- 'Diebstahl*; vergl. ksl. fai/q,
HRN.txt:10382:'betrügen (oss. d. dawun, t. dawin 'stehlen*) vollständig
HUB.txt:2752:*satt* = zd. '^sairya-, gr. xo(>o^.
HUB.txt:4581:mana (als nom. sg.) ; 5gr 'satt' = *8arya- (p. 78). Unsicher
HUB.txt:5110:von ctturpat = ap. ^dt^pata-? (zd. atarepata-, gT!ATpondTjjc);
HUB.txt:6324:neben AdarbaSegan JKAS. 1894, 440, zu zd. atarepata-^ gr.
HRN.txt:408:Zäl), dass jener edle Löwe (d. i. Rustemj satt wurde (Mohl's Über-^— XVI —
HRN.txt:6248:(229) ; wa/. stär, si/n. starf^ stirj ^), sar. /turj^ minj.
HRN.txt:22463:taraparhak 341.
```


## [2026-10-15T02:47:36.196Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3608,3622p HRN.txt"
}
```


### [2026-10-15T02:47:36.540Z] TOOL RESULT

```
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
```


## [2026-10-15T02:47:41.298Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; mkdir -p $S data/verification/sources/refs/ocr/BOOK; pdftoppm -f 505 -l 505 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg505 && cp $S/pg505.png data/verification/sources/refs/ocr/BOOK/505.png && ls -la data/verification/sources/refs/ocr/BOOK/505.png"
}
```


### [2026-10-15T02:47:42.756Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   75k sfmqrb 14 Oct 22:47  data/verification/sources/refs/ocr/BOOK/505.png
```


## [2026-10-15T02:47:46.600Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['PRT','KAS','SYN','KLN','SOD']: print(k, {x:d.get(k,{}).get(x) for x in ['kind','local_file','page_offset','title']})\"; grep -n \"2.11\\b\\|^2.1[1-5] \\|FATHER\\|MOTHER\" data/verification/sources/refs/SYN.txt | head"
}
```


### [2026-10-15T02:47:47.059Z] TOOL RESULT

```
PRT {'kind': 'archive_restricted', 'local_file': None, 'page_offset': None, 'title': 'E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958'}
KAS {'kind': 'website', 'local_file': None, 'page_offset': None, 'title': "M.A. Hasani Da'i al-Eslam, Khod-amuz-e Zaban-e Sanskrit, Danesh 1361/1982"}
SYN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'title': 'C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949'}
KLN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'title': 'E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67'}
SOD {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'], 'page_offset': 'printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)', 'title': 'Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995'}
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
2524:Grk. ra:diov, dim. of zais ‘child’, is ‘young child’, in NT frequently ‘infant’ (Mt. 2.11, 18, etc. of the infant Jesus, in our version ‘the young child’).
2781:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 103 2.35 2.36 2.37 FATHER MOTHER PARENTS
2933:9.46 GRANDFATHER
2936:2.47 GRANDMOTHER
3377:2.61 FATHER-IN-LAW 2.62 MOTHER-IN-LAW
3615:128 SELECTED INDO-EUROPEAN SYNONYMS 2.71 2.72 2.73 2.74 STEP. STEPFATHER STEPMOTHER STEPSON DAUGHTER Grk.  (unrputés, rarpuiés) rout FESTOS f mpdyovos, Tpoydyn NG pytpuiés pnTpu Tporyoves, wrpoyore Tpoyorn, mpoydre Lat. _vitricus, patrasler noverca, matraster Gi eed Silidster es Me Sfiliastra | It. patrigno matrigno fightastro igliastra Fr. beau-ptre belle-mére (mardtre) beau-fils belle-fille Sp. padrastro madrastra hijastro hijastra Rum. até vitreg mamé vitregd fiu vitreg fatd vitregé Ir. lessathair lesmathair lesmac lessingen Nir. __leasathair leasmhathair leasmhac leasinghean W. llysdad llysfam llysfab Uysferch a ' lez-tad lez-vamm lez-vab lez-verc’h Obhas es otek Aas 2 Aiea a ee ee ane stjipr stjipdottir | an.  stiffader stifmoder slifson stifdatter Sw. styffar styfmoder styfson styfdoiter es Sie oe pee Se is | slepsone stepdou; te; NE stepfather stepmother stepson jenni Du. sliefvader stiefmoeder sttefzoon stiefdoehter OHG  stiuffater stiufmuotar sliufsun stiuftohter MHG stiefvater sliefmuoter sltiefsun stieftohter me a ies stiefsohn stieftochter ‘ pamote ostinis d Lett. patévs pamdate naaels ees ChSl.  oliéimii, oltéuchtt mastecha pastoriiku pastortika (pa- : : duiSz) See Le ; maceha pastorak pastorka oh.  nevlasint otec, olfim  nevlastnt matka, macecha nevlastni syn, pastorek nevlastnt dcera, : pastorkyné ec tte ard a aie i ; asyno. y Skt. _ (tata- yaviyan-) pee lai Av. pone
4922:2. Lat. piscis, Ir. tasc, NIr. zasg, Goth. fisk, etc., all the Gme. words, root connection? Walde-P. 2.11. Po- korny, KZ 54.307. Cuny, Mélanges Glotz, 268 f.
6716:3. Lat. spirdre (epd. respirare ‘breathe again, take breath, etc.’ > It. respirare, Fr. respirer, Sp. respirar), with sb. spiri- tus (It. respiro fr. respirare) prob. : ChSl. piskati ‘whistle’, SCr. pistatr ‘hiss’, ON fisa ‘pedere’ (4.64), ete., IE *(s)peis- (imitative). Walde-P. 2.11.
7028:6. ON fisa, Dan. fise, Sw. fisa, OE sb. fisting, ME vb. fyste (cf. NED s.v. fist, sb.?, vb.?), Du. veesten, MHG visten, visten, NHG fisten, of imitative orig., prob. through ‘blow’ (cf. also Lat. spirare ‘breathe’, ChSIl. piskati ‘whistle’). Walde-P. 2.11. Falk-Torp 220 f.
```


## [2026-10-15T02:47:50.598Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -n 2558 SYN.txt | tr -cd '\\f' | wc -c; head -n 2781 SYN.txt | tr -cd '\\f' | wc -c; sed -n 2781,2800p SYN.txt | grep -i -o \".\\{100\\}protector.\\{200\\}\\|.\\{100\\}nursery.\\{200\\}\\|.\\{50\\}baby.\\{200\\}\" | head"
}
```


### [2026-10-15T02:47:51.029Z] TOOL RESULT

```
122
134
```


## [2026-10-15T02:47:54.649Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2781,2860p SYN.txt | grep -i -o \".\\{0,200\\}\\(nursery\\|pa-\\|IE \\*pəter\\|pater\\|milk\\|daughter\\).\\{0,250\\}\" | head -8"
}
```


### [2026-10-15T02:47:58.149Z] TOOL RESULT

```
ugrep: error: error at position 137
(?:[^\n\x80-\xbf][\x80-\xbf]*){0,250}
        exceeds complexity limits___/
```


## [2026-10-15T02:48:00.226Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2781,2900p SYN.txt | grep -n -i \"nursery\\|Walde-P\\. 2.12\\|milk\\|IE \\*\" | cut -c1-400 | head -12"
}
```


### [2026-10-15T02:48:00.664Z] TOOL RESULT

```
33:2.36. ‘Mother’. 1. IE *mdter-, prob.
34:starting fr. a nursery word of the pa type (above, p. 94) orig. pd, reduced to pa before the accent. Walde-P. 2.4. Here belong the Grk., Lat., Ir., Gme., and Indo-Iranian words, also Arm. hair, and Toch, A pacar, B pacer. In Balto-Slavic it is completely replaced. 2. Nursery words that have become oe usual terms. Type baba (above, p. ) in It. babbo, now a serious rival of padre, nes atta, tata 
36:starting fr. a nursery word of the ma type. Walde-P. 2.229. Here belong the Grk., Lat., Ir., Gme. (except Goth aipei), Balto-Slavic, and Indo-Iranian forms, also Arm. mair, and Toch. A macar, B macer. But Lith. moté became ‘woman’, and as ‘mother’ was replaced by the deriv. motyna.
37:2. Nursery words that have become the usual terms. Type mama (above, p. 94, Walde-P. 2.221) in It. mamma a serious rival of madre, and W., Br. mam.
38:Goth. aipei, prob. new fem. formed fr. some nursery word similar to, though not identical with, atta ‘father’. Feist 28.
100:2. Lat. filius (> It. figlio, figholo, Fr. fils, Sp. hijo, Rum. fiu), together with fem. filia ‘daughter’ (> It. figha, figliola, Fr. fille, Sp. hija; Rum. fie arch., now dim. fitcd), orig. ‘suckling’, fr. the root of Lat. féldre ‘suck’ (cf. Umbr. sif filiu ‘suckling pigs’), Skt. dhayatz ‘sucks’, etc., IE *dh@i-. Cf. ChSl. déti ‘child’
110:2.42. ‘Daughter’. 1. IE *dhugh(a)ter, root connection obscure. The root agrees in form with that of Skt. duh- ‘milk’ and with that of Grk. rebxw ‘fash- ion, make’. But in neither case is there a convincing semantic explanation. Walde-P. 1.868. Here belong Grk. Qvyarnp; Goth. dauhtar, etc., all the Gme. words; Lith. dukté, OPruss. duckti, ChSI. disti, ete., all the Slavic words (partly with add
```


## [2026-10-15T02:48:07.323Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/τέρπω' 'https://en.wiktionary.org/wiki/Terpsichore' 'https://en.wiktionary.org/wiki/Euterpe' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/méh₂tēr' 'https://en.wiktionary.org/wiki/مادر' 'https://en.wiktionary.org/wiki/برادر' 'https://en.wiktionary.org/wiki/پدر'; do f=$(python3 tools/fetch_source.py \"$u\" --note \"page 505: Ter 3 / Terp verification\" 2>&1 | tail -1); echo \"== $u\"; grep -A4 \"^ *Etymology$\" $f | grep -v \"^ *$\\|edit\" | head -4 | cut -c1-400; done"
}
```


### [2026-10-15T02:48:19.922Z] TOOL RESULT

```
== https://en.wiktionary.org/wiki/τέρπω
 Etymology
 From Proto-Hellenic *térpō , from Proto-Indo-European *terp- ( “ to satisfy ” ) , cognate with German dürfen ( “ to need ” ) and obsolete and dialectal British English tharf ( “ to need ” ) . [ 1 ] 
--
 Etymology
== https://en.wiktionary.org/wiki/Terpsichore
 Etymology
 From Ancient Greek Τερψιχόρη ( Terpsikhórē , from τέρψις ( térpsis , “ enjoyment, delight ” ) +‎ χορός ( khorós , “ chorus ” ) ) .
== https://en.wiktionary.org/wiki/Euterpe
 Etymology
 From Ancient Greek Εὐτέρπη ( Eutérpē , “ muse of lyric poetry ” ) .
--
 Etymology
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/méh₂tēr
 Etymology
 The linguist Donald Ringe suggests that the term may be a nursery word or Lallwort , in which case he considers a reconstruction *mah₂tḗr to be most likely. [ 1 ] In older literature, the term was usually reconstructed de-laryngealized as *mātēr and explained as a combination of a nursery word *ma ( “ mother ” ) and the agentive nominal suffix *-tēr . However, Balto-Slavic forms have acute accent
== https://en.wiktionary.org/wiki/مادر
 Etymology
 Borrowed from Persian مادر ( mâdar ) .
--
 Etymology
== https://en.wiktionary.org/wiki/برادر
 Etymology
 Etymology tree
--
 Etymology
== https://en.wiktionary.org/wiki/پدر
 Etymology
 Etymology tree
--
 Etymology
```


## [2026-10-15T02:50:48.367Z] TOOL CALL #52: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-505.json",
 "content": "{\n  \"pdf_page\": 505,\n  \"book_page\": 475,\n  \"verified_by\": \"claude-opus-5-5\",\n  \"verified_on\": \"2026-10-14\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ter 3, Tar\",\n      \"verdict\": \"disputed\",\n      \"modern_form\": \"PIE kinship suffix *-ter- / *-h₂ter- (in *méh₂tēr, *ph₂tḗr, *dʰugh₂tḗr, *bʰréh₂tēr; Indo-Iranian *ǰā́mā-tar-); formally identical with the agent suffix *-tḗr, but its kinship use is not agentive\",\n      \"note\": \"The suffix -ter- in the IE kinship terms is real (Watkins/AHD s.v. pəter-/māter-: 'the kinship-term suffix -ter-'; Buck SYN). What the chart claims on top of that is outdated: that the suffix is the agent suffix and that the words mean 'feeder', 'protector', 'milker', 'load carrier', 'married one'. Buck (SYN, intro to ch. 2 family terms) says these agent-noun readings ('father' as 'protector', 'daughter' as 'milker', 'brother' as 'supporter') 'now seem fanciful and pointless and are generally given up'. Watkins and Wiktionary derive *māter-/*pəter- from the nursery words ma/pa plus the kinship suffix. Wiktionary calls the 'brother' = bhártṛ 'bearer, protector' idea 'phonologically impossible' and gives 'daughter' < *dʰewgʰ- only as 'perhaps'. Only geme-tar 'son-in-law' (Skt. jāmātar-, Av. zāmātar-) is still generally tied to a root, *ǵem- 'marry' (Pokorny 369). Pokorny p.369, which Nourai cites, is in fact the gem(e)- 'to marry' entry, not a -ter entry. The individual words and their descent (node chains Avestan→Persian, Germanic→English) are correct. Book problem: the Persian box glosses doxtar as 'sister' (should be 'daughter'); extraction faithful. Extraction matches the printed page (checked on site/pages/505.jpg and pdftoppm render).\",\n      \"note_fa\": \"پسوند -ter- در نام‌های خویشاوندی هندواروپایی (مادر، پدر، دختر، برادر، داماد) واقعی است و واتکینز و باک آن را «پسوند خویشاوندی» می‌نامند. اما ادعای نورایی که این پسوند همان پسوند فاعلی است و «مادر» یعنی «خوراک‌دهنده»، «پدر» یعنی «نگهبان»، «دختر» یعنی «دوشندهٔ شیر» و «برادر» یعنی «باربر» را پژوهش امروزی رد می‌کند. باک این تعبیرها را «خیال‌پردازانه و رهاشده» می‌داند، و واتکینز و ویکی‌واژه mā- و pa- را واژه‌های کودکانه شمرده‌اند. تنها «داماد» (*ǵem- «زناشویی کردن») هنوز به ریشه‌ای فعلی پیوند داده می‌شود. خودِ واژه‌ها و سیر تحول آنها درست است. معنای «خواهر» برای «دختر» در کتاب خطای چاپی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-tḗr\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/méh₂tēr\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ph₂tḗr\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰugh₂tḗr\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰréh₂tēr\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:369\", \"status\": \"partial\", \"note\": \"Pokorny p.369-370 (POK_full.txt line ~35030) is 'gem(e)- Meaning: to marry': 'Old Indic jāmātar-, Avestan zāmātar- ... created after other relationship names in -tar-, with ā in the second syllable after mātar-'. It supports Geme-tar and treats -tar- as a kinship-name pattern, but it is not an entry for a suffix meaning 'one who performs the action'.\"},\n        {\"ref\": \"AHD:1500\", \"status\": \"partial\", \"note\": \"Watkins AHD (AHD_watkins1985.txt) s.v. māter-: 'Based ultimately on the baby-talk form mā-, with the kinship term suffix -ter-'; s.v. pəter-: 'derived from the baby-talk syllables pa(pa) and ma(ma) ... marked by the kinship-term suffix -ter-'. The suffix is confirmed, the agentive reading is not. The page number 1500 refers to the 1975 appendix and was not checked.\"},\n        {\"ref\": \"PRT:863\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins is archive-restricted; no local copy.\"},\n        {\"ref\": \"KAS:10\", \"status\": \"not_checked\", \"note\": \"Hasani Da'i al-Eslam's Sanskrit primer: no page-level access.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"SYN\", \"where\": \"ch. 2 family relationship intro (SYN.txt line 2558, leaf 122)\", \"stance\": \"contradicts\", \"note\": \"'these words of relationship were also formerly interpreted as agent-nouns ... 'father' as 'protector', 'mother' as 'measurer' ..., 'brother' as 'supporter', 'daughter' as 'milker' ... Most of these derivations now seem fanciful and pointless and are generally given up.' The suffix is tied instead to -tero- of contrasting relationship.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins s.v. māter-, pəter-\", \"stance\": \"partial\", \"note\": \"'kinship-term suffix -ter-'; mā/pa baby-talk bases.\"},\n        {\"src\": \"IEC\", \"where\": \"s.v. mātēr (IEC.txt line 10369)\", \"stance\": \"silent\", \"note\": \"Mann lists 'mātēr ... mother' with Per. mādar, Av. mātar, no agentive etymology.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II 229 (cited by Buck/Mann for māter)\", \"stance\": \"silent\", \"note\": \"Not re-read; Buck quotes Walde-P. 2.229 for the nursery-word origin of *māter.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Indo-European\",\n          \"words\": \"Mâ-ter; Pa-ter; Dhugh-tar; Bhra-ter; Geme-tar\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The five PIE words are real (modern *méh₂tēr, *ph₂tḗr, *dʰugh₂tḗr, *bʰréh₂tēr; for 'son-in-law' only Indo-Iranian *ǰā́mātar- from *ǵem- 'marry'). The meanings Nourai gives them are discarded agent-noun etymologies. *méh₂tēr and *ph₂tḗr are the nursery words mā-/pa- plus the kinship suffix -ter (Watkins, Buck, Wiktionary; Ringe: Lallwort), though Wiktionary still mentions *peh₂- 'protect' as an 'often supposed' alternative for father. 'Daughter' from *dʰewgʰ- 'milk/produce' is only 'perhaps' (Wiktionary); Buck: 'root connection obscure ... in neither case is there a convincing semantic explanation'. 'Brother' as 'bearer' (bʰer-) is called phonologically impossible (Wiktionary, after Mallory-Adams). 'Geme-tar' from *ǵem(h₁)- 'marry' is accepted (Pokorny 369). So the forms are confirmed but the glosses 'feeder, protector, milker, load carrier' are rejected.\",\n          \"derivation_fa\": \"واژه‌های هندواروپایی آغازین *méh₂tēr «مادر»، *ph₂tḗr «پدر»، *dʰugh₂tḗr «دختر» و *bʰréh₂tēr «برادر» واقعی‌اند. واژهٔ هندوایرانی *ǰā́mātar- «داماد» هم از ریشهٔ *ǵem- «زناشویی کردن» آمده است. اما معناهایی که نورایی به آنها داده («خوراک‌دهنده»، «نگهبان»، «دوشنده»، «باربر») ریشه‌شناسی‌های کهنه‌ای است که باک و واتکینز و ویکی‌واژه کنار گذاشته‌اند. «مادر» و «پدر» از واژه‌های کودکانهٔ mā و pa با پسوند خویشاوندی -ter ساخته شده‌اند. پیوند «دختر» با «دوشیدن» فقط یک احتمال است، و پیوند «برادر» با *bʰer- «بردن» از نظر آوایی ناممکن است. تنها «داماد» با ریشهٔ «زناشویی» پذیرفته است (پوکورنی ۳۶۹).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/méh₂tēr\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ph₂tḗr\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰugh₂tḗr\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰréh₂tēr\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK\", \"status\": \"partial\", \"note\": \"Pokorny p.369 gem(e)- 'to marry' supports Geme-tar (jāmātar-/zāmātar-). Pokorny's entries for māter-/pəter-/bhrāter- (Pokorny 700, 829, 163) give no agent meanings. The bare 'POK' gives no page.\"},\n            {\"ref\": \"SYN:103-107\", \"status\": \"contradicts\", \"note\": \"Buck 2.35 'Father' 1. IE *pəter-, prob. starting fr. a nursery word of the pa type'; 2.36 'Mother' 'IE *māter-, prob. starting fr. a nursery word of the ma type'; 2.42 'Daughter' 'IE *dhugh(a)ter, root connection obscure ... in neither case is there a convincing semantic explanation' (SYN.txt lines 2814-2890).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. māter-, bhrāter-, geme-\", \"stance\": \"partial\", \"note\": \"'māter-. Mother. Based ultimately on the baby-talk form mā-, with the kinship term suffix -ter-'; 'bhrāter-. Brother, male agnate' (no root); 'geme-. To marry ... [Pok. gem(e)- 369]'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. mātēr (1) line 10369\", \"stance\": \"silent\", \"note\": \"'mātēr ... mother ... Skt. mātā; Av. mātar; Per. mādar' with no agentive gloss.\"},\n            {\"src\": \"SYN\", \"where\": \"ch. 2 intro (line 2558)\", \"stance\": \"contradicts\", \"note\": \"'daughter' as 'milker' etc. 'now seem fanciful and pointless and are generally given up'.\"},\n            {\"src\": \"POK\", \"where\": \"p.369-370 gem(e)-\", \"stance\": \"supports\", \"note\": \"jāmātar-/zāmātar- under gem(e)- 'to marry' (Geme-tar only).\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Avestan\",\n          \"words\": \"mâ-tar; pi-tar; duğ-dâr; brâ-tar; zâmâ-tar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All five are attested Avestan stems: mātar- f. 'mother', pitar- m. 'father' (nom. pita, also ptar-/fəδr-), dugədar- (Gathic) / duγδar- (YAv.) 'daughter', brātar- 'brother', zāmātar- 'son-in-law' (Bartholomae). They continue Proto-Iranian *mātā, *pitā, *dugdā, *brātā, *jāmātā. In the daughter word, PIIr. *dʰugʰ(H)tar- became *dugdʰar- by Bartholomae's law and then Av. dugədar-/duγδar-. The ā in Nourai's 'duğ-dâr' is a small slip for short -dar-. In zāmātar- the Av. z continues PIE *ǵ, and Old Persian has d there, which is the source of Persian dāmād (see node 3).\",\n          \"derivation_fa\": \"هر پنج واژه در اوستا آمده است: mātar- «مادر»، pitar- «پدر»، dugədar- (گاهانی) / duγδar- (اوستای نو) «دختر»، brātar- «برادر» و zāmātar- «داماد» (بارتولومه). صورت duγδar- با قانون بارتولومه از هندوایرانی *dʰugʰtar- ساخته شده است، و «dâr» با الف کشیده در کتاب لغزش کوچکی برای dar است. z اوستایی در zāmātar- برابر d پارسی باستان است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰugh₂tḗr\",\n            \"https://en.wiktionary.org/wiki/داماد\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN\", \"status\": \"not_checked\", \"note\": \"No page given. Klein lists Avestic cognates s.v. mother/father/brother/daughter, but these entries were not re-read for this node.\"},\n            {\"ref\": \"SYN:103-107\", \"status\": \"supports\", \"note\": \"Buck 2.35-2.44 tables list Av. pitar-, mātar-, dugədar-/duγδar-, brātar- among the inherited 'Indo-Iranian words'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt lines 16365, 17427, 20293, 13645, 28087\", \"stance\": \"supports\", \"note\": \"'pitar- ... m. 'Vater''; 'brātar- ... m. 'Bruder''; ''mātar- f. 'Mutter' ... ai. mātár- f., np. mādar'; 'dugədar-, j. duγδar- 'Tochter''; 'zāmātar- m. 'Eidam, Schwiegersohn' ... ai. jāmātar- m., np. dāmād'.\"},\n            {\"src\": \"HRN\", \"where\": \"nos. 286, 532, 541, 956\", \"stance\": \"supports\", \"note\": \"'aw. pitar-'; 'aw. zāmātar- 'Schwiegersohn'; phlv. dāmāt'; 'aw. duγdar- 'Tochter''; 'aw. mātar-'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"mâdar; pedar; doxtar; barâdar; dâmâd\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The words and their descent are right, but the route runs through Old Persian / Middle Persian, not Avestan. mādar < MP mādar < OIr. *mātar- (t > d after a vowel). pedar/pidar < MP pidar (oblique of pid) < *pitar-. duxtar < MP duxtar, oblique of duxt, < OP *duxçī-/*duxtar- (Wiktionary, MacKenzie). barādar < MP brād/brādar < OP brātar- (with an anaptyctic vowel). dāmād < MP dāmād < OP *dāmātar-. Its d- is the Southwest Iranian (Persian) reflex of PIE *ǵ, against Av. z in zāmātar-, so dāmād cannot come from the Avestan word directly (Wiktionary; Bartholomae). The book's glosses repeat the rejected agent meanings (see node 1). It also glosses doxtar as 'sister', which is wrong: doxtar means 'daughter, girl', and 'sister' is xᵛāhar. The book prints 'sister', so this is Nourai's misprint and the extraction is faithful.\",\n          \"derivation_fa\": \"«مادر» از فارسی میانهٔ mādar و ایرانی باستان *mātar- است (ت میان دو واکه به د بدل شده). «پدر» از فارسی میانهٔ pidar، «دختر» از فارسی میانهٔ duxtar (حالت غیرفاعلی duxt) و پارسی باستان *duxçī-، و «برادر» از فارسی میانهٔ brād/brādar و پارسی باستان brātar- آمده است. «داماد» از فارسی میانهٔ dāmād و پارسی باستان *dāmātar- است، و دال آغازینش ویژگی گویش جنوب‌غربی (پارسی) است در برابر z اوستایی. پس این واژه‌ها از پارسی باستان آمده‌اند و از اوستایی گرفته نشده‌اند، هرچند هم‌ریشه‌اند. معنای «خواهر» برای «دختر» خطای چاپی خود کتاب است (درست: دختر، دوشیزه). معناهای «خوراک‌دهنده، باربر …» هم پذیرفته نیست.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"doxtar «دختر» : \\\"milker\\\", sister\",\n          \"correct_form\": \"doxtar «دختر» : daughter\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/دختر\",\n            \"https://en.wiktionary.org/wiki/داماد\",\n            \"https://en.wiktionary.org/wiki/برادر\",\n            \"https://en.wiktionary.org/wiki/پدر\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT\", \"status\": \"not_checked\", \"note\": \"No page given. The BQT OCR (BQT_v1/v2_pages.txt) has the words only in running text, e.g. line 15829 'پدر هم آمده است که به عربی والد گویند'; the etymological footnote was not located.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"nos. 286 (p.~64), 532 (p.118), 541, 956; p.45 birāder\", \"stance\": \"supports\", \"note\": \"'286. pider (peder) 'Vater'. ap. pitar-; aw. pitar-; phlv. pit, pitar'; '532. dāmād 'Schwiegersohn; Bräutigam' ... aw. zāmātar-; phlv. dāmāt'; '541. duxter, duxt 'Tochter'. aw. duγdar-'; '956. mādar ... ap. *mātar- ... aw. mātar-; phlv. māt, mātar'; 'birāder 'Bruder'. ap. brātar; aw. brātar; phlv. brātar, brāt'.\"},\n            {\"src\": \"PHD\", \"where\": \"s.v. mādar, pidar, duxt/duxtar, dāmād\", \"stance\": \"supports\", \"note\": \"'mādar [AMYtl; mtl | M mdr, N ~] mother'; 'pidar [ABYtl; pyt | M pydr, N ~] father'; 'duxt ... daughter. ~ar [dwhtl | N ~] daughter'; 'dāmād [d’m’t' | M d’m’d, N ~] bridegroom, son-in-law'.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt line 4099\", \"stance\": \"supports\", \"note\": \"'ap. *duxtā neben duxtar — ap. *duxtaram' for np. duxtar.\"},\n            {\"src\": \"ARY\", \"where\": \"pdf p.262 (DĀMĀD), pdf p.455 (MĀDAR)\", \"stance\": \"supports\", \"note\": \"Latin index: 'JAMATAR (SANSKRIT) ... ZAMATAR (AVESTAN) ... GAM, GAMEO- (GREEK) ... DAMAD, DAMAT (PAHLAVI) ... GENER (LATIN) ... ZAWAT (KURDISH)'; 'MADAR, MAD (PAHLAVI)'.\"},\n            {\"src\": \"BRT\", \"where\": \"zāmātar- (line 28087)\", \"stance\": \"supports\", \"note\": \"'zāmātar- m. 'Eidam, Schwiegersohn' ... ai. jāmātar- m., np. dāmād'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"môthar, fadar, dohter, brôthar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"These are Proto-Germanic *mōdēr (Watkins' older notation *mōthar-), *fadēr, *duhtēr, *brōþēr. They come from PIE *méh₂tēr, *ph₂tḗr, *dʰugh₂tḗr, *bʰréh₂tēr by Grimm's law (*p > f, *t > þ, *bʰ > b, *dʰ > d, *gʰ > g/h before t). Verner's law gives the voiced d in *fadēr and *mōdēr, because the PIE accent fell after the dental; *brōþēr kept þ because it was accented on the root.\",\n          \"derivation_fa\": \"این‌ها صورت‌های ژرمنی آغازین *mōdēr «مادر»، *fadēr «پدر»، *duhtēr «دختر» و *brōþēr «برادر» هستند. با قانون گریم (p به f، t به þ، bʰ به b، dʰ به d) و قانون ورنر از صورت‌های هندواروپایی ساخته شده‌اند. ادعای نورایی درست است (واتکینز، باک).\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰréh₂tēr\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. bhrāter-: '1. Germanic *brōthar- in Old English brōthor, brother'; s.v. māter-: '1. Germanic *mōthar- in Old English mōdor, mother'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SYN\", \"where\": \"2.35-2.44\", \"stance\": \"supports\", \"note\": \"Buck lists Goth. fadar, brōþar, dauhtar and the Gmc. words among the inherited IE terms ('Here belong the Grk., Lat., Ir., Gme. ... words').\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. mātēr\", \"stance\": \"supports\", \"note\": \"'OHG muoter; OE mōdor ...; ON móðir'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"mother, father, daughter, brother\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English mōdor, fæder, dohtor, brōþor continue the Proto-Germanic forms of node 4. Middle English moder, fader changed to mother, father in the 15th-16th c., when -d- before -er became -th- (on the model of brother). The forms are standard (Watkins, Klein, Skeat).\",\n          \"derivation_fa\": \"انگلیسی mother، father، daughter و brother از انگلیسی کهن mōdor، fæder، dohtor و brōþor آمده‌اند و آنها از صورت‌های ژرمنی آغازین. d پیش از -er در سده‌های ۱۵ و ۱۶ در mother و father به th بدل شد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/méh₂tēr\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. māter-: 'Old English mōdor, mother: MOTHER'; s.v. bhrāter-: 'Old English brōthor, brother: BROTHER'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"IEC\", \"where\": \"s.v. mātēr\", \"stance\": \"supports\", \"note\": \"'OE mōdor, ds mēder'.\"},\n            {\"src\": \"SYN\", \"where\": \"2.35-2.44 tables\", \"stance\": \"supports\", \"note\": \"NE father, mother, daughter, brother listed with OE fæder, mōdor, dohtor, brōþor.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Terp, Trep 2, Trp\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *terp- 'to satisfy (oneself), enjoy' (Pokorny 1077 terp-, trep-; Watkins terp-; LIV² 636)\",\n      \"note\": \"Root, gloss and the Greek, Sanskrit and Avestan θrafəδa- branches are standard (Pokorny, Walde-Pokorny I 736, Watkins, Klein s.v. Terpsichore, Wiktionary). The 'steal' group (Av. tarəp-, MP trift, Sogd. cf-) is attached by Pokorny only with 'perhaps' ('sich des Besitzes erfreuen'?). Bartholomae and Nyberg treat Av. tarəp- 'steal' on its own. Persian tulf comes from Pokorny's 'npers. tulf 'Übersättigung'' and could not be found in Borhan/Mo'in, Horn or Hübschmann. Book problems: 'thrafza' is not an Avestan form (Bartholomae has θrafəδa-/θrafδa-), and the English 'euterp' is a truncation of Euterpe. The Pahlavi box points to an empty box, a blank in the book. Extraction faithful.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *terp- «سیر شدن، خرسند شدن، لذت بردن» است (پوکورنی ۱۰۷۷، واتکینز، کلاین). معنا و شاخه‌های یونانی (τέρπω)، سنسکریت (tṛpti-) و اوستایی (θrafəδa- «سیر، خرسند») درست است. پیوند گروه «دزدیدن» (اوستایی tarəp-، پهلوی trift، سغدی cf-) با این ریشه را پوکورنی تنها با «شاید» آورده است. «تولف» فارسی هم فقط در پوکورنی دیده می‌شود و در برهان و معین و هرن یافت نشد. «thrafza» در کتاب صورت درستی نیست (درست: θrafəδa-)، و «euterp» کوتاه‌شدهٔ Euterpe است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/terp-\",\n        \"https://en.wiktionary.org/wiki/τέρπω\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1077\", \"status\": \"supports\", \"note\": \"POK_full.txt line ~86297: 'Root / lemma: terp- trep- Meaning: to be satiated, satisfied. Material: Old Indic tṛpyati ... tṛpti- f. 'satiation, satisfaction', Avestan θrafəδa- 'befriedigt' ... θrafs- n. 'contentedness'; npers. tulf 'Übersättigung' (*tṛfa-); perhaps also Old Indic -tṛp- 'stealing', Avestan tarep- 'steal', Middle Persian tirft 'theft', sogd. cf- 'steal' ...; gr. τέρπω 'sättige, erfreue''.\"},\n        {\"ref\": \"KLN:1592\", \"status\": \"supports\", \"note\": \"Klein s.v. Terpsichore (KLN_1966.txt line 38692): 'fr. I.-E. base *terp-, 'to satisfy', whence also OI. tṛpyati ... 'takes one's fill', Avestic θrafda-, 'satiated, satisfied''.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p.736 (WLD_Bd1_pages.txt line 69658)\", \"stance\": \"supports\", \"note\": \"'terp- „sich sättigen, genießen“: Ai. tṛpyati ... av. θrafδa- „befriedigt, zufriedengestellt“ ... gr. τέρπω „sättige, erfreue“'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins s.v. terp-\", \"stance\": \"supports\", \"note\": \"'terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.]'\"},\n        {\"src\": \"IEC\", \"where\": \"grep 'terp'\", \"stance\": \"silent\", \"note\": \"No headword for terp- found in Mann's OCR.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"thrafza, thrafda; tarep\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"Av. θrafəδa-/θrafδa- 'satiated, satisfied, amply provided' (Yt 13.100, Y 57.14) is real. Bartholomae derives it from *tramptha- (cf. Skt. tṛmpáti), i.e. *trp- with Iranian *t > θ before r. The root vowel ə/zero shows the zero grade. The book's 'thrafza' is not attested; it is Nourai's misprint or mis-rendering of θrafəδa- (δ written z). Av. tarəp- 'to steal' (Y 11.5, pres. tərəfya-) is also real, but Bartholomae and Nyberg treat it on its own. Pokorny joins it to *terp- only with 'perhaps' ('to enjoy possession'?). The Avestan words are attested, but the spelling 'thrafza' is wrong and the 'steal' link is only plausible.\",\n          \"derivation_fa\": \"اوستایی θrafəδa- (یا θrafδa-) «سیر، خرسند، به‌قدر بسنده برخوردار» واقعی است. بارتولومه آن را از *tramptha- و از پایهٔ ضعیف ریشهٔ *terp- می‌داند، و t پیش از r در ایرانی به θ بدل شده است. صورت «thrafza» در کتاب در اوستا وجود ندارد و لغزش نورایی برای θrafəδa- است. فعل اوستایی tarəp- «دزدیدن» هم واقعی است، اما پیوندش با *terp- را تنها پوکورنی، آن هم با «شاید»، آورده است. بارتولومه و نیبرگ آن را جدا بررسی کرده‌اند.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"thrafza, thrafda\",\n          \"correct_form\": \"θrafəδa- (variant θrafδa-)\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/terp-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1077\", \"status\": \"supports\", \"note\": \"'Avestan θrafəδa- 'befriedigt, ausreichend versehen' (*tramptha-) ...; perhaps also ... Avestan tarep- 'steal''. Supports, with 'perhaps' for tarep.\"},\n            {\"ref\": \"KLN:1592\", \"status\": \"supports\", \"note\": \"'Avestic θrafda-, 'satiated, satisfied'' (s.v. Terpsichore).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 805-806 θrafəδa- (BRT.txt line ~14570); col. 644 tarəp- (line 12102)\", \"stance\": \"partial\", \"note\": \"θrafəδa-, θrafδa- Adj. 'satt' ... 'befriedigt, zufrieden gestellt' ... 'Aus ar. *tramptha-'; 'tarəp- V. 'stehlen', Praes. 27 tərəfya- ... Vgl. ai. -tṛp- Adj. 'stehlend'; mp. tirft 'Diebstahl'; alles übrige (Horn NpEt. 86, Hbm. PSt 185) ist unsicher'. No link between the two.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. 2 glossary p.195 s.v. triftakēh\", \"stance\": \"partial\", \"note\": \"'Av. (643) tarəp- 'to steal', subju. tərəfyāt (Y 11.5; a hapax)'. No connection with 'satisfy' mentioned.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"tulf\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"Pokorny 1077 lists 'npers. tulf 'Übersättigung' (*tṛfa-)'. That would be the zero grade *tr̥p- with Iranian *r̥ > ur/ul and *p > f, an expected development. The word could not be found in any Persian lexicon available: it is absent from the OCR of Borhan-e Qate' and Mo'in, from Horn and Hübschmann, and from vajehyab (which returns only تولفرا etc.). Nourai's '(obsolete)' admits it is not in current use. Plausible phonologically, but unconfirmed beyond Pokorny.\",\n          \"derivation_fa\": \"پوکورنی (ص۱۰۷۷) واژهٔ فارسی «tulf» را به معنای «سیری بیش از اندازه» از *tṛfa- آورده است. از نظر آوایی ممکن است: r هجایی در ایرانی به ur/ul و p به f بدل می‌شود. اما این واژه در برهان قاطع، فرهنگ معین، هرن، هوبشمان و واژه‌یاب یافت نشد. پس جز گواهی پوکورنی منبع دیگری برایش نیست و داوری درباره‌اش ممکن نیست.\",\n          \"sources\": [\"https://vajehyab.com/?q=تولف\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1077\", \"status\": \"supports\", \"note\": \"'npers. tulf 'Übersättigung' (*tṛfa-)' (POK_full.txt line ~86302). This is the source of Nourai's word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"grep تولف in BQT_v1/v2/v3/v4/v5_pages.txt\", \"stance\": \"silent\", \"note\": \"No hit.\"},\n            {\"src\": \"MON\", \"where\": \"grep تولف in MON_part1/2.txt; vajehyab.com/?q=تولف\", \"stance\": \"silent\", \"note\": \"No hit locally; vajehyab shows only unrelated تولفرا / Tofieldia.\"},\n            {\"src\": \"HRN\", \"where\": \"grep tulf/sättig\", \"stance\": \"silent\", \"note\": \"Horn has no tulf. No. 386 terfend 'Falschheit, Betrug' is tied to Av. tarəp- instead.\"},\n            {\"src\": \"ARY\", \"where\": \"grep تولف in ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"No hit.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"tirft\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Book Pahlavi <tlpt> 'theft' (with the verb <tlwptn'> truftan and triftār 'thief') is attested, mainly in the Pahlavi Yasna rendering Av. tarəp-/taya-. Bartholomae read it tirft. Nyberg argues for trift: as a technical Zoroastrian term it was borrowed from Avestan tarəp- (tərəfya-), and the parallel truft shows r-vowel colouring. The word is real and does descend from Av. tarəp-. Its tie to *terp- 'satisfy' is only Pokorny's 'perhaps', so plausible. The book's arrow to an empty box on the right is a blank in the printed chart.\",\n          \"derivation_fa\": \"پهلوی <tlpt> «دزدی» واقعی است و بیشتر در ترجمهٔ پهلوی یسنا در برابر اوستایی tarəp- آمده است. بارتولومه آن را tirft و نیبرگ trift می‌خواند. نیبرگ آن را وام‌واژه‌ای دینی از اوستایی می‌داند و فعل truftan و triftār «دزد» را هم از همین گروه می‌شمارد. پس پیوندش با tarəp- اوستایی درست است، اما پیوندش با ریشهٔ *terp- «سیر شدن» تنها یک احتمال است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/terp-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1077\", \"status\": \"partial\", \"note\": \"'perhaps also ... Middle Persian tirft 'theft''. The word is in Pokorny, but the root link is only 'perhaps'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"vol. 2 glossary p.195 s.v. triftakēh (NYB_vol2_glossary.txt line 3795-3799)\", \"stance\": \"supports\", \"note\": \"'the former must be regarded as borrowed from Av., and consequently tlpt is best interpreted as trift, not as tirft as Bthl has it ... 6. tlpt = trift 'theft' explaining Av. (638) taya-'.\"},\n            {\"src\": \"PHD\", \"where\": \"English index s.v. theft (PHD.txt line 3970)\", \"stance\": \"silent\", \"note\": \"MacKenzie gives only 'theft appar(išn), duz(d)īh'. No tlpt/trift entry.\"},\n            {\"src\": \"BRT\", \"where\": \"col. 644 tarəp-\", \"stance\": \"supports\", \"note\": \"'mp. tirft 'Diebstahl''.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"cft, cf; cftu\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Sogdian cp-/cf- (caf) 'to steal' (no. 3167, from *trf-, cf. Khwarezmian), past stem cpt- (capd/caft) 'stole', and past participle cptw (caftu) 'stolen' are attested (Gharib nos. 3167-3170, p.125). Sogdian č- < *tr- is regular (OIr. *tr- > Sogd. č-), so *tr̥p- > *čf- > cf-. Nourai's 'cft, cf' are the past and present stems. The forms are confirmed, but the tie to *terp- 'satisfy' is again only Pokorny's 'perhaps', so plausible.\",\n          \"derivation_fa\": \"سغدی cf- (caf) «دزدیدن»، ستاک گذشتهٔ cpt- (caft) و صفت مفعولی cptw (caftu) «دزدیده» در فرهنگ قریب (ص۱۲۵، ش۳۱۶۷ تا ۳۱۷۰) آمده‌اند. č سغدی برابر *tr- ایرانی باستان است، پس *tr̥p- به cf- رسیده است. خود واژه‌ها درست‌اند. پیوندشان با ریشهٔ *terp- «سیر شدن» را پوکورنی تنها با «شاید» آورده است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/terp-\"],\n          \"ref_check\": [\n            {\"ref\": \"SOD:125\", \"status\": \"supports\", \"note\": \"Gharib p.125 (SOD_pages.txt line ~12755-12775): '3167 cp- B caf ... <*trf-; Khwar. ... (to) steal'; '3168 cpt- capd pt. st. (to) steal'; '3170 cptw caβdu, caftu pp. stolen'.\"},\n            {\"ref\": \"POK:1077\", \"status\": \"partial\", \"note\": \"'sogd. cf- 'steal' („sich des Besitzes erfreuen“?)'. Only 'perhaps'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"p.125 nos. 3167-3170\", \"stance\": \"supports\", \"note\": \"'cp- caf ... steal'; 'cptw caftu pp. stolen'.\"},\n            {\"src\": \"BRT\", \"where\": \"col. 644 tarəp-\", \"stance\": \"silent\", \"note\": \"Lists ai./mp. cognates only, no Sogdian; 'alles übrige ... ist unsicher'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"trpti\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit tṛ́pti- f. 'satisfaction, satiety', with the adjective tṛptá- 'satisfied', is from the zero grade *tr̥p- plus the abstract suffix *-ti-. Syllabic *r̥ remains ṛ in Sanskrit. The verbs are tṛpyati, tṛpnoti 'is satisfied' and causative tarpayati 'satisfies' (Pokorny, Klein). Nourai's gloss 'satisfied' fits tṛptá-; tṛpti- strictly means 'satisfaction'.\",\n          \"derivation_fa\": \"سنسکریت tṛpti- «سیری، خرسندی» (و صفت tṛpta- «سیر، خرسند») از پایهٔ ضعیف *tr̥p- و پسوند اسم‌ساز *-ti- ساخته شده است. فعل‌های tṛpyati «سیر می‌شود» و tarpayati «سیر می‌کند» هم از همین ریشه‌اند. ادعای نورایی درست است، جز اینکه tṛpti در اصل «سیری» است و «سیر» نیست.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/terp-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1077\", \"status\": \"supports\", \"note\": \"'Old Indic tṛpyati, tṛpnoti, tṛmpati ... Kaus. tarpayati ..., tṛptá-, tṛpti- f. 'satiation, satisfaction''.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 736\", \"stance\": \"supports\", \"note\": \"'trpti-h „Sättigung, Genüge, Befriedigung, Überdruß“'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. Terpsichore\", \"stance\": \"supports\", \"note\": \"'OI. tṛpyati, tṛpnoti, tarpati, 'takes one's fill''.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"terpo\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek τέρπω 'to delight, gladden'; the middle τέρπομαι means 'enjoy oneself', and in Homer, with the genitive, 'have one's fill of' (food, weeping). It is the e-grade thematic present *térp-e-ti of *terp- (Wiktionary, Pokorny). Nourai's 'to fill, satisfy' reflects the old 'satiate' sense noted by Pokorny ('sättige, erfreue'); the usual classical meaning is 'delight'.\",\n          \"derivation_fa\": \"یونانی باستان τέρπω (terpō) «شاد کردن، خرسند کردن» است. حالت میانهٔ آن τέρπομαι در هومر «سیر شدن از چیزی، لذت بردن» معنا می‌دهد. این فعل صورت مضارع با بالاندِ e از ریشهٔ *terp- است. ادعای نورایی درست است، هرچند معنای رایج آن «شادمان کردن» است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/τέρπω\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/terp-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1077\", \"status\": \"supports\", \"note\": \"'gr. τέρπω 'sättige, erfreue', τέρπομαι 'freue mich'; τέρψις 'satisfaction''.\"},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 'terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 736\", \"stance\": \"supports\", \"note\": \"'gr. τέρπω „sättige, erfreue“, τέρπομαι „freue mich“'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. Terpsichore, Euterpe\", \"stance\": \"supports\", \"note\": \"'τέρπειν, 'to delight, please', fr. I.-E. base *terp-, 'to satisfy''.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"terpsi-chorě\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The name is Greek: Τερψιχόρη 'delight in the dance', from τέρψις 'enjoyment' (from τέρπω) + χορός 'dance, chorus'. Latin took it over as Terpsichorē, the Muse of dance, and English has it from there (Klein: 'L. Terpsichore, fr. Gk.'). Nourai's gloss 'satisfaction from dancing' fits. The Latin box is a borrowing step, not an inherited Latin word.\",\n          \"derivation_fa\": \"این نام یونانی است: Τερψιχόρη «لذت از رقص»، از τέρψις «لذت، خرسندی» (از τέρπω) و χορός «رقص گروهی، همسرایان». لاتین آن را به صورت Terpsichorē برای الههٔ رقص وام گرفت و انگلیسی از لاتین گرفت. پس در لاتین وام‌واژه است و از ریشه به ارث نرسیده. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Terpsichore\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1077\", \"status\": \"partial\", \"note\": \"Pokorny lists τέρψις under terp-. The Latin borrowing is not mentioned.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Terpsichore (KLN_1966.txt line 38687)\", \"stance\": \"supports\", \"note\": \"'Terpsichore, n., the Muse of the dance ... L. Terpsichore, fr. Gk. Τερψιχόρη, lit. 'enjoyment of dance', a name compounded of τέρψις, 'enjoyment, gladness, delight', and χορός, 'dance''.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins index TERPSICHORE gher-1, terp-\", \"stance\": \"supports\", \"note\": \"'TERPSICHORE gher-1, terp-'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"terpsichore, euterp\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"English Terpsichore 'Muse of the dance' (whence terpsichorean 'of dancing') comes from Latin < Greek Τερψιχόρη (node 7). The book's 'euterp' is a truncation of Euterpe, the Muse of music and lyric poetry: Latin Euterpē < Greek Εὐτέρπη 'well-pleasing', from εὖ 'well' + τέρπειν. It is a sister formation from τέρπω, not a descendant of Terpsichore. The printed page has 'euterp', so the error is in the book and the extraction is faithful.\",\n          \"derivation_fa\": \"انگلیسی Terpsichore «الههٔ رقص» از لاتین و آن از یونانی Τερψιχόρη آمده است. «euterp» در کتاب کوتاه‌شدهٔ Euterpe (الههٔ موسیقی) است، از یونانی Εὐτέρπη «بسیار خوشایند» (εὖ «خوب» + τέρπειν). این واژه از خود τέρπω ساخته شده و از Terpsichore نیامده است. ریشه‌شناسی درست است، اما صورت «euterp» خطای چاپی کتاب است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"terpsichore, euterp\",\n          \"correct_form\": \"Terpsichore, Euterpe\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Terpsichore\",\n            \"https://en.wiktionary.org/wiki/Euterpe\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1592\", \"status\": \"supports\", \"note\": \"Klein s.v. Terpsichore (above) and s.v. Euterpe (KLN_1966.txt line 13853): 'Euterpe, n., the Muse of music ... L., fr. Gk. Εὐτέρπη, lit. 'pleasing well', fr. εὖ and τέρπειν, 'to delight, please'. See Terpsichore.'\"},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. terp-: '... TERPSICHORE'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Euterpe, Terpsichore\", \"stance\": \"supports\", \"note\": \"As quoted in ref_check.\"},\n            {\"src\": \"AHD\", \"where\": \"terp- and index\", \"stance\": \"supports\", \"note\": \"'Greek terpein, to delight, cheer: TERPSICHORE'.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-15T02:50:48.440Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-505.json (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:50:54.152Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\nimport json\np='data/verification/page-505.json'\ns=open(p).read()\ns=s.replace(\" (Wiktionary, after Mallory-Adams)\",\" (Wiktionary)\")\nd=json.loads(s)\ne=d['entries'][0]\ne['consulted']=[c for c in e['consulted'] if c['src']!='WLD']+[{\"src\":\"POK\",\"where\":\"p.369-370 gem(e)-\",\"stance\":\"partial\",\"note\":\"'jāmātar-, Avestan zāmātar- ... created after other relationship names in -tar-' — treats -tar- as a kinship-name pattern, not an agentive meaning.\"}]\nopen(p,'w').write(json.dumps(d,ensure_ascii=False,indent=2)+\"\\n\")\nEOF\npython3 -m json.tool data/verification/page-505.json >/dev/null && python3 tools/verify_check.py 505"
}
```


### [2026-10-15T02:50:54.919Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'disputed': 1, 'confirmed': 6, 'transcription_suspect': 3, 'unverified': 1, 'plausible': 2}
root verdicts: {'disputed': 1, 'confirmed': 1}
ref checks: {'partial': 4, 'contradicts': 1, 'not_checked': 2, 'supports': 12}
books consulted: {'partial': 3, 'silent': 7, 'contradicts': 1, 'supports': 23} | by book: {'BRT': 5, 'KLN': 4, 'AHD': 3, 'IEC': 3, 'SYN': 3, 'HRN': 3, 'PHD': 2, 'ARY': 2, 'NYB': 2, 'WLD': 2, 'POK': 1, 'HUB': 1, 'BQT': 1, 'MON': 1, 'SOD': 1}
```


## [2026-10-15T02:51:03.994Z] TOOL CALL #54: SubagentHandback

```json
{
 "message": "Page 505 (book page 475) is verified. I wrote /home/sfmqrb/git/rishe-private/data/verification/page-505.json, and `verify_check.py 505` shows 13/13 nodes and 0 PROBLEM lines.\n\n**Counts**\n- Roots (2): 1 disputed, 1 confirmed.\n- Nodes (13): 6 confirmed, 2 plausible, 1 disputed, 3 transcription_suspect, 1 unverified.\n\n**Disputed**\n- **ROOT Ter 3, Tar** and **#1 Mâ-ter / Pa-ter / Dhugh-tar / Bhra-ter / Geme-tar**: the kinship suffix -ter is real and so are the words. But the agent-noun meanings (\"feeder\", \"protector\", \"milker\", \"load carrier\") are rejected. Buck (SYN) calls them \"fanciful … generally given up\". Watkins and Wiktionary derive mother and father from the baby-talk words ma/pa, and Wiktionary says \"brother\" from *bʰer- \"carry\" is phonologically impossible. Only geme-tar → *ǵem- \"marry\" holds (Pokorny 369). Pokorny p.369, which Nourai cites for the root, is in fact the gem(e)- \"to marry\" entry.\n\n**Transcription suspects** (all are misprints in the book; the extraction matches the page)\n- **Ter 3, #3 Persian**: doxtar is glossed \"sister\"; it should be \"daughter\". Also, these Persian words come down through Old and Middle Persian, not from Avestan: dāmād has the Persian d-, where Avestan has z- in zāmātar-.\n- **Terp, #1 Avestan**: \"thrafza\" is not an Avestan form. Bartholomae has θrafəδa- / θrafδa- \"satiated\". The tarəp- \"steal\" link to *terp- is only Pokorny's \"perhaps\".\n- **Terp, #8 English**: \"euterp\" is cut short; the word is Euterpe.\n\n**Other findings**\n- **Unverified, Terp #2 Persian tulf تولف**: only Pokorny gives it (\"npers. tulf 'Übersättigung'\"). It is not in Borhan, Mo'in, Horn, Hübschmann, Aryanpur or vajehyab.\n- **Plausible, Terp #3 Pahlavi tirft and #4 Sogdian cf-/cftu**: both words are attested. Nyberg reads the Pahlavi word as trift, and Gharib p.125 has the Sogdian ones. Their link to *terp- \"satisfy\" is only Pokorny's \"perhaps\".\n- **Blank box**: the Pahlavi node in the Terp chart has an arrow pointing to an empty box. That box is empty in the printed book too.\n\n**Extraction errors for the owner to fix:** none. The JSON matches the printed page; the page render is saved at data/verification/sources/refs/ocr/BOOK/505.png."
}
```


### [2026-10-15T02:51:04.303Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
