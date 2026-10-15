# Verification process log — verify-page-516


## [2026-10-15T02:44:16.708Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 516 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-516.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-516.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-516.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 516` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.777Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.455Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.572Z] TOOL RESULT

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


## [2026-10-15T02:44:19.954Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-516.txt"
}
```


### [2026-10-15T02:44:19.981Z] TOOL RESULT

```
1	=== PDF page 516 (book page 486) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ud 1 : up, out, away  (refs POK:1103)
4	#1 (parent #0) [Avestan] refs=POK:1103; HRN:154; BQT:1049; DZA:57 | ud, us, uz : up, out ; us-tavah : out of power, tired ☞Tĕu 1 ; ni-us-tavah : not tired (of fighting) ☞Ne 1,Tĕu 1 ; us-spar : walk away, trust ☞Spher ; uz-ah, zâ 2 : push out of opening, give birth ☞Ôus 2 ; uz-ah-âp : where water comes out, spring ☞Ab 1
5	  #2 (parent #1) [Persian] refs=BQT:1049,1086,1102; IRN:108; MON:1763 | sotŭh «ستوه» : tired ; nastŭh «نستوه» : energetic in fighting ; sepârdan «سپاردن ۲ ، سپردن» : to entrust ; zeh 2 «زه ۲ (زاهیدن،زهیدن)» : to give birth ; zehdân «زهدان» : womb ☞Dhě 2 ; zahâb «زهاب ( زاب )» : spring, river ☞Ab 1
6	#3 (parent #0) [Avestan] refs=POK:1104 | us-tema : outmost, extreme ; usča : above, overhead, on top
7	#4 (parent #0) [Old Persian] refs=KNT:176 | ud : up ; ud-zma, uzma : grown up from ground ☞Ghdhem
8	#5 (parent #0) [Sanskrit] refs=POK:1104 | ucca, učča : high, top
9	  #6 (parent #5) [Arabic] refs=MON:399 | awja : tip, high top
10	    #7 (parent #6) [Persian] refs=MON:399 | owj «اوج» : top
11	    #8 (parent #6) [Spanish] refs=SKT:357 | auge : top
12	      #9 (parent #8) [French] refs=SKT:357 | ogive, ogee
13	        #10 (parent #9) [English] refs=SKT:357; TYL:568 | ogee, ogive : a pointed double-curved arch
14	#11 (parent #0) [Germanic] refs=AHD | ŭt : out
15	  #12 (parent #11) [English] refs=None | out, but, about
16	#13 (parent #0) [Greek] refs=AHD | hus-teros : later
17	  #14 (parent #13) [English] refs=None | hysteresis
18	--- entry 1 ---
19	ROOT Ud 2 -> redirect to Wed
20	
```


## [2026-10-15T02:44:20.740Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-516.json"
}
```


### [2026-10-15T02:44:20.763Z] TOOL RESULT

```
1	{
2	  "pdf_page": 516,
3	  "book_page": 486,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Ud 1",
8	        "lang": "Indo-European",
9	        "refs": "POK:1103",
10	        "gloss": "up, out, away"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1103; HRN:154; BQT:1049; DZA:57",
18	          "words": [
19	            {"translit": "ud, us, uz", "gloss": "up, out", "script": null},
20	            {"translit": "us-tavah", "gloss": "out of power, tired", "script": null, "see": ["Tĕu 1"]},
21	            {"translit": "ni-us-tavah", "gloss": "not tired (of fighting)", "script": null, "see": ["Ne 1", "Tĕu 1"]},
22	            {"translit": "us-spar", "gloss": "walk away, trust", "script": null, "see": ["Spher"]},
23	            {"translit": "uz-ah, zâ 2", "gloss": "push out of opening, give birth", "script": null, "see": ["Ôus 2"]},
24	            {"translit": "uz-ah-âp", "gloss": "where water comes out, spring", "script": null, "see": ["Ab 1"]}
25	          ],
26	          "note": null,
27	          "quote": null
28	        },
29	        {
30	          "id": 2,
31	          "parent": 1,
32	          "lang": "Persian",
33	          "refs": "BQT:1049,1086,1102; IRN:108; MON:1763",
34	          "words": [
35	            {"translit": "sotŭh", "gloss": "tired", "script": "ستوه"},
36	            {"translit": "nastŭh", "gloss": "energetic in fighting", "script": "نستوه"},
37	            {"translit": "sepârdan", "gloss": "to entrust", "script": "سپاردن ۲ ، سپردن"},
38	            {"translit": "zeh 2", "gloss": "to give birth", "script": "زه ۲ (زاهیدن،زهیدن)"},
39	            {"translit": "zehdân", "gloss": "womb", "script": "زهدان", "see": ["Dhě 2"]},
40	            {"translit": "zahâb", "gloss": "spring, river", "script": "زهاب ( زاب )", "see": ["Ab 1"]}
41	          ],
42	          "note": null,
43	          "quote": {
44	            "text": "بیازید هوشنگ چون شیر جنگ - جهان کرد بر دیو نستوه تنگ",
45	            "poet": "Ferdowsî"
46	          }
47	        },
48	        {
49	          "id": 3,
50	          "parent": 0,
51	          "lang": "Avestan",
52	          "refs": "POK:1104",
53	          "words": [
54	            {"translit": "us-tema", "gloss": "outmost, extreme", "script": null},
55	            {"translit": "usča", "gloss": "above, overhead, on top", "script": null}
56	          ],
57	          "note": null,
58	          "quote": null
59	        },
60	        {
61	          "id": 4,
62	          "parent": 0,
63	          "lang": "Old Persian",
64	          "refs": "KNT:176",
65	          "words": [
66	            {"translit": "ud", "gloss": "up", "script": null},
67	            {"translit": "ud-zma, uzma", "gloss": "grown up from ground", "script": null, "see": ["Ghdhem"]}
68	          ],
69	          "note": null,
70	          "quote": null
71	        },
72	        {
73	          "id": 5,
74	          "parent": 0,
75	          "lang": "Sanskrit",
76	          "refs": "POK:1104",
77	          "words": [
78	            {"translit": "ucca, učča", "gloss": "high, top", "script": null}
79	          ],
80	          "note": null,
81	          "quote": null
82	        },
83	        {
84	          "id": 6,
85	          "parent": 5,
86	          "lang": "Arabic",
87	          "refs": "MON:399",
88	          "words": [
89	            {"translit": "awja", "gloss": "tip, high top", "script": null}
90	          ],
91	          "note": null,
92	          "quote": null
93	        },
94	        {
95	          "id": 7,
96	          "parent": 6,
97	          "lang": "Persian",
98	          "refs": "MON:399",
99	          "words": [
100	            {"translit": "owj", "gloss": "top", "script": "اوج"}
101	          ],
102	          "note": null,
103	          "quote": null
104	        },
105	        {
106	          "id": 8,
107	          "parent": 6,
108	          "lang": "Spanish",
109	          "refs": "SKT:357",
110	          "words": [
111	            {"translit": "auge", "gloss": "top", "script": null}
112	          ],
113	          "note": null,
114	          "quote": null
115	        },
116	        {
117	          "id": 9,
118	          "parent": 8,
119	          "lang": "French",
120	          "refs": "SKT:357",
121	          "words": [
122	            {"translit": "ogive, ogee", "gloss": null, "script": null}
123	          ],
124	          "note": null,
125	          "quote": null
126	        },
127	        {
128	          "id": 10,
129	          "parent": 9,
130	          "lang": "English",
131	          "refs": "SKT:357; TYL:568",
132	          "words": [
133	            {"translit": "ogee, ogive", "gloss": "a pointed double-curved arch", "script": null}
134	          ],
135	          "note": null,
136	          "quote": null
137	        },
138	        {
139	          "id": 11,
140	          "parent": 0,
141	          "lang": "Germanic",
142	          "refs": "AHD",
143	          "words": [
144	            {"translit": "ŭt", "gloss": "out", "script": null}
145	          ],
146	          "note": null,
147	          "quote": null
148	        },
149	        {
150	          "id": 12,
151	          "parent": 11,
152	          "lang": "English",
153	          "refs": null,
154	          "words": [
155	            {"translit": "out, but, about", "gloss": null, "script": null}
156	          ],
157	          "note": null,
158	          "quote": null
159	        },
160	        {
161	          "id": 13,
162	          "parent": 0,
163	          "lang": "Greek",
164	          "refs": "AHD",
165	          "words": [
166	            {"translit": "hus-teros", "gloss": "later", "script": null}
167	          ],
168	          "note": null,
169	          "quote": null
170	        },
171	        {
172	          "id": 14,
173	          "parent": 13,
174	          "lang": "English",
175	          "refs": null,
176	          "words": [
177	            {"translit": "hysteresis", "gloss": null, "script": null}
178	          ],
179	          "note": null,
180	          "quote": null
181	        }
182	      ]
183	    },
184	    {
185	      "root": {
186	        "name": "Ud 2",
187	        "redirect": "Wed"
188	      },
189	      "nodes": []
190	    }
191	  ]
192	}
193	
```


## [2026-10-15T02:44:23.751Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -120; ls data/verification/sources/refs/ | head -100; sed -n 1,200p tools/verify_check.py",
 "description": "Read source matrix, refs list, check script"
}
```


### [2026-10-15T02:44:24.283Z] TOOL RESULT

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


## [2026-10-15T02:44:28.148Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BQT','DZA','IRN','MON','KNT','SKT','TYL','AHD','WLD','BRT','ARY','KLN','LKT','PHD','NYB','HUB','CHEUNG','DEV','PHN','DOZ']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:700]);print()\n\"; ls data/verification/sources/refs/ocr/; ls data/verification/sources/refs/ocr/BQT | head",
 "description": "Show reference metadata for cited abbreviations"
}
```


### [2026-10-15T02:44:28.629Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based lea

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or g

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

DZA {"title": "M.T. Rashed Mohassel, Daramadi bar Dastur-e Zaban-e Avestai, Khajeh 1364/1985", "kind": "purchase", "url": "taaghche.com (revised edition ebook)", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: the 1364 Khajeh edition is not digitised; a revised edition is sold as an ebook on Taaghche."}

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "/home/sfmqrb/git/rishe-priv

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https:

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/de

TYL {"title": "W. Taylor, Arabic Words in English (S.P.E. Tract XXXVIII), Oxford 1933", "edition_found": null, "kind": "hathitrust_fullview", "url": "https://babel.hathitrust.org/cgi/pt?id=uc1.b4089843 (S.P.E. Tracts nos. 31-40 bound volume incl. Tract XXXVIII, rightsCode pdus = full view in the US; record 000519279) ; mdp.39015005310308 (nos. 36-58) search-only", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_LeedsStudiesInEnglish_ArabicWordsInBenJonson_pp44-50.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TYL/TYL_Taylor1934_BenJonson_pages.txt"], "page_offset": null, "lookup_hint": "N

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f 

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe-

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966:

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cite

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/detail

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar 

CHEUNG null

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line star

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at lin

DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup

Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  AFM
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ARY
drwxr-xr-x     - sfmqrb 14 Oct 22:19  BLY
drwxr-xr-x     - sfmqrb 14 Oct 22:19  BOOK
drwxr-xr-x     - sfmqrb 14 Oct 22:30  BQT
drwxr-xr-x     - sfmqrb 14 Oct 22:19  FFD
drwxr-xr-x     - sfmqrb 14 Oct 22:19  HRN
drwxr-xr-x     - sfmqrb 14 Oct 22:19  IRN
drwxr-xr-x     - sfmqrb 14 Oct 22:27  PLA
drwxr-xr-x     - sfmqrb 14 Oct 22:19  SNS
drwxr-xr-x     - sfmqrb 14 Oct 22:19  SOD
drwxr-xr-x     - sfmqrb 14 Oct 22:19  TAD
Permissions Size User   Date Modified Name
.rw-r--r--  368k sfmqrb 14 Oct 22:19  0001.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  0001.txt
.rw-r--r--  534k sfmqrb 14 Oct 22:19  0049.png
.rw-r--r--  2.7k sfmqrb 14 Oct 22:19  0049.txt
.rw-r--r--  190k sfmqrb 14 Oct 22:30  0143.jpg
.rw-r--r--   576 sfmqrb 14 Oct 22:30  0143.vision.txt
.rw-r--r--  202k sfmqrb 14 Oct 22:30  0479.jpg
.rw-r--r--   444 sfmqrb 14 Oct 22:30  0479.vision.txt
.rw-r--r--  205k sfmqrb 14 Oct 22:30  0480.jpg
```


## [2026-10-15T02:44:31.427Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *ud-\\|^ud \" POK_03.txt | head; grep -n \"Ud-\\|ud- *'auf\" POK_full.txt | head -20",
 "description": "Find Pokorny ud- entry"
}
```


### [2026-10-15T02:44:31.770Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:44:33.907Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"1103\\|1104\" POK_full.txt | head -20; grep -n \"auf, empor\\|aufwärts, hinaus\" POK_03.txt POK_full.txt | head",
 "description": "Locate POK pages 1103-1104"
}
```


### [2026-10-15T02:44:34.316Z] TOOL RESULT

```
88038:Page(s):1103 
88070:Page(s): 1104-1105 
88101:Page(s):1103 
88105:Page(s):1103 
93567:Page(s): 1103-1104
```


## [2026-10-15T02:44:35.922Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 93520,93570p POK_full.txt",
 "description": "Print POK ud entry"
}
```


### [2026-10-15T02:44:36.238Z] TOOL RESULT

```
Material: 1 . Old Indie ud-, ut- "empor, out' proverb; Avestan us-, uz- {*uds-) ds., ap. ^s-ds. 

{ud- in ud-apatata^ex lehnte sich auf, fiel ab' is probably *uz-); 

gr. u- in u-ppiq (see below g'^er-^ heavy '), uarpi^ "porcupine', uanAr)^ "Startseil', Cypriot 
u-xnpo<; "Aufgeld' (Attic "ra £nix£ipa') and in this Mundart generally zum Ersatze from £ni 
has changed: adnominal with Lok. e.g. u-Tuxa "£ni Tuxp'; eine (an Gothic /i/pa besides 
*i/yC?c» gemahnende) full grade probably in Cypriot £UTp6aa£a0ai £niaTp£(p£a0ai. flacpioi and 
£uxou(; x^vn ("Trichter') laAafjivioi Hes.; (because of uoioo,, uaT£pa see below udero- 
"belly'); 

Latin us-que"\n a fort, ununterbrochen from - her or bis - toward '; 

Old Irish proverb uss-, 055- could also auf *^o^s- go back; see below upcr, 

Gothic J/ Adv. "out, heraus'. Old High German uz. Modern High German from. Old 
Saxon Old English uf6s.. West Germanic also preposition beim " dative ' Abl. (in addition 
Gothic uta. Old Icelandic ut/. Old English ute. Old High German uze'auQ>en, outside '; 
Gothic utana. Old High German uzana etc.. Modern High German auden. Old Icelandic 
utar. Old English uter. Old Saxon utar. Old High German Jza/'"besides', partly as 
preposition beim " dative ' and Akk.; Old High German uzero, uzaro. Old English uter-ra 
"the outer'); intrinsic auf *^o''5vor voiced Verschluftlauten based on Germanic l/z-"from, 
from - heraus, from - vor, vor - away' in Gothic us{uz-; vorr. ur-) prefix and preposition 
"from, from' ("Dat.' = Abl.), also Old Icelandic d^preposition, as prefix or-, or-, 0r-, Old 
English or-. Old Saxon ur-, or- prefix. Old High German ur, ar, /a preposition "from, from' 



(vor Jzzuruckweichend), ur-, ir-, ar-, er- prefix, Modern High German ur-, er-{e.g. Uriaub, 
er/auben \acat\on'); Middle Low German {ut)buten '{irom) exchange, erbeuterf irovc\ *bi- 
utian, compare Old Icelandic yta 'darreichen'; 

Lithuanian ^z-"auf-, hinauf-, to-' prefix (the meaning halber probably to divide from uz 
preposition ' behind, for', s. *ghdS. 451 f.; Trautmann, Bsl. Wb. 336 halt an the Einheit 
fest, also for die consecutive forms), Latvian uz, Jz prefix and preposition "auf (in addition 
also Old Prussian ^/7se/"hinauf, auf); 

Old Church Slavic: i/bz-(i/bs-) prefix, i/bz/^b^ preposition in the meaning "hinauf an 
etwas' (Akk.); 

2. Kompar. Old Indie Mara- "the hohere, obere, spatere, hintere' = gr. uaT£po(; "the 
spatere'; Sup. Old Indie ^//a/77a-"hochster, oberster, best', Avestan ^s/a/775- "aufterster, 
last', gr. uaraToq "last, spatester' (fur*uaTapiO(;); about Old Indie ucca-^hxqh' {*ud-k"e), 
ucca, Avestan uscaAdv. "above; after above' s. Wackernagel-Debrunner II, 2, 545 f. 

References: WP. I 189 f., WH. II 344, Schwyzer Gr. Gr. 2, 517 f., Vasmer 1, 214. 238 f., 
242, Mayrhofer 1 , 99, 101 f. 
Page(s): 1103-1104 

Root / lemma: ha/a
```


## [2026-10-15T02:44:39.591Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *2\\. *ud\\|ud- *.auf\\|ud-, ut-\\|uttara-\" incoming/WLD/WLD_Bd1_pages.txt | head; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3",
 "description": "Find ud- in Walde-Pokorny Bd I"
}
```


### [2026-10-15T02:44:40.088Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:44:42.240Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"uttara\\|ucc[aā]\\|usque\" incoming/WLD/WLD_Bd1_pages.txt | head; head -c 600 incoming/WLD/WLD_Bd1_pages.txt",
 "description": "Search WLD for ud- cognates"
}
```


### [2026-10-15T02:44:42.626Z] TOOL RESULT

```
162:flaccus,   lippus ,    siccus, pidlus ,    Lucca , guttur   ,
4138:vgl. die Lit. bei Yf. LEWb. 2 u. ad und usque , Berneker 454, Brtickner
6056:Acc. „usque ad“ bedeutungsgleich, was, selbst wenn nur junge Kreuzung
7025:nuB“, lett. r ieJest ,,YuB, HaselnuB“, apr. buccareisis „Bucbecker“ is. Traut-
17483:     Lat.    usque        „in           einein    fort,
17768:subs- (wie abs) in smtineo u dgl. und in susque cirque faro „aequo animo
19638:lat. rucca „Kub“, s. Curtius
49286:„utriusque‘     hapar aisl. huarr, ags. hwceper „wer von beiden“ (ahd.
67108:quibusdam                    ac macerata; et ideo toto anno durat“, tucca
67110:„xar dlvfxa Cco/ioii“, umbr. toco „tuccas“ (gall., siehe Biicheler Umbr. 40,
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

               CENTRAL
            ARCHEOLOGICAL
                LIBRARY
ACCESSION NO. jj03?7
CALL No. gJ3 Wafjpok
                 f_
D.G.A. 79
                      ALOIS WALDE


VERGLEICHENDES WftRTERBDCH
                                DER


     INDOGERM ANISCHEN SPRACHEN

                HERAUSGEGEBEN UND BEARBEITET
                                VON

                     JULIUS POKORNY


                           I.   BAND


VM   /




                   BERLIN UND LEIPZIG 1930

              WALTER DE GRUYTER & CO.
```


## [2026-10-15T02:44:44.524Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 17460,17520p incoming/WLD/WLD_Bd1_pages.txt",
 "description": "Print WLD ud- entry"
}
```


### [2026-10-15T02:44:44.899Z] TOOL RESULT

```
     nroEtj eottai. Ylaxfioi und evyovg yibri]. —a)ia/uviot Hcs. (s. zu dtn gr Formen
                                                                              '




     Bugge BB. 14. 03, Bgm. -Thumb GrGr. 4 51 Of. m. Lit., und wegen rarog.
     vortoa u. * tidi vo                         „Baucli‘").
                                                                      -




190                                                       udero-, uedero-


                                    ununtcrbrochen von — her oder bis — hin
                                                                                                                         - '

     Lat.    usque        „in           einein    fort,

(s. Yf. LEWb.  2
                 s. v.); [eher zu  upo (S. 193) air. (nur als Praefix: b-, u- (mit
Geminierung des folgenden Konsonanten, z. B. nccu „Wahl, Wunsch" aus
*ud-gus-T), o-, fta- (vor r, I, n), us, os (vorYok.        s. Thurneysen   Hdb. I      ;



474 ff. und bes. II 99 f., wo riehtiger *uks als Gdf. erwogen wird acymr. aper,                   ;


ncymr. aber „Miindung“ aus *acl-bhero-1 Fick II 4 54, Pedersen KG. I 4S0)];
  Got. fit Adv. „hinaus, heraus“, ahd. «j, nhd. aus as. ags. ut ds.. wgerm.            ,


auch Praep. beim „Dativ“ Abl. (dazu got. iite, aisl. Tdi, ags. Fite, ahd. dje
„auBen, drauBen"; got. fitana, ahd. Tirana usw., nhd. aufSen        aisl. fitar                       ;
                                                                                                                           ,


ags. liter, as. fitar ahd. Fi^ar „au8er“, z. T. als Praep. beim „Dativ‘ und
                                                                                                                 -

                                    ,

Acc.  ahd. Fiyo, ftyiro , ags. fiter-ra „der auBere"); wesentlich auf *uds
        ;



vor tbnenden YerschluBlauten (nach Osthoff MU. IY 202 freilich auf *ud-
vor Dentalen) beruht germ, uz- ,,aus, aus — heraus, aus    vor, vor — weg“                   —
in    got. us (uz-vor r ur~) Praef. und Praep. „von, aus“ („Dat.“
                           ;
                                                                          Abl.),                             =
ebenso aisl. or Praep., als Praef. or-, or-, gr-, ags. or-, as. ur-, or- Praef.,
ahd. ur, ar, ir Praep. „aus, von"                              („Dat.“    =Abl. ; sparlich, vor   zuriiek-
```


## [2026-10-15T02:44:47.194Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *ud-\\|ud- *Up\\|hysteresis\\|^ *ud\\b\" AHD_watkins1985.txt | head; ",
 "description": "Find ud- in AHD Watkins"
}
```


### [2026-10-15T02:44:47.568Z] TOOL RESULT

```
1102:ud-. Also Gd-. Up, out. 1. Germanic *it-, out, in: a. Old English at, ovuT; utmost; b. Old High German az (> German aus), out, in German garaus, “all out”: CA- ROUSE; AUSLANDER; C. Old Norse at, out: OUTLAW; d. Middle Dutch ute, uut, out: UITLANDER; e. Middle Dutch dteren, to drive away, speak out: UTTER}; f. Ger- manic suffixed (comparative) form *it-era- in Old Eng- lish dtera, outer: UTTER?; g. Germanic compound *bi-iitana (*bi-, by, at; see ambhi), “at the outside,” in Old English bitan, biite, outside (adverb): BUT; ABOUT. 2. Extended form *uds in Germanic *uz, out, and prefix *uz-, out, in: a. Old High German ir-, out, in irsezzan, to replace: ERSATZ; b. Middle Dutch oor-, out: ORT; c. Ger- manic *uz-dailjam, “a portioning out,” judgment (see dail-). 3. Suffixed (comparative) form *ud-tero- in Greek husteros, later, second, after: HYSTERESIS, HYSTERON PROTERON. 4. Greek hu- in compound hubris, violence, outrage, insolence (bri-, perhaps “heavy,” “violent”; see g”era-?): HUBRIS. [Pok. d- 1103.]
```


## [2026-10-15T02:44:49.871Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/516* 2>/dev/null; ls data/verification/sources/refs/ocr/BOOK | head -3",
 "description": "Check for page image"
}
```


### [2026-10-15T02:44:50.233Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   64k sfmqrb 14 Oct 22:15  site/pages/516.jpg
Permissions Size User   Date Modified Name
.rw-r--r--   96k sfmqrb 14 Oct 22:19  33.png
.rw-r--r--   99k sfmqrb 14 Oct 22:19  39.png
```


## [2026-10-15T02:44:53.924Z] TOOL CALL #14: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 516 -l 516 -r 200 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg516",
 "description": "Render PDF page 516 to PNG"
}
```


## [2026-10-15T02:44:54.335Z] TOOL CALL #15: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg516.png"
}
```


### [2026-10-15T02:44:55.063Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-15T02:44:55.476Z] TOOL RESULT

```

```


## [2026-10-15T02:44:55.467Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-15T02:45:13.401Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo ==CHEUNG; grep -n \"stōh\\|stoh\\|sepurdan\\|spurdan\\|sipurdan\\|zah-\\|zahīdan\\|zahidan\" CHEUNG.txt | head -30; echo ==HRN; grep -n \"^ *154\\.\\|^ *712\\.\\|^ *683\\.\\|^ *1023\\.\\|sitöh\\|sut[oö]h\\|ustavah\" HRN.txt | head",
 "description": "Grep Cheung and Horn for words"
}
```


### [2026-10-15T02:45:13.881Z] TOOL RESULT

```
Exit code 1
(eval):1: =CHEUNG not found
```


## [2026-10-15T02:45:16.637Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo \"-- CHEUNG\"; grep -n \"stōh\\|sepurdan\\|spurdan\\|sipurdan\\|zahīdan\\|zahidan\\|zah[iī]dan\" CHEUNG.txt | head -30; echo \"-- HRN\"; grep -n \"^ *154\\. \\|sitöh\\|sutöh\\|ustavah\\|zihidan\\|zahidan\\|sipurdan\\|sipardan\" HRN.txt | head",
 "description": "Grep Cheung and Horn for words"
}
```


### [2026-10-15T02:45:17.082Z] TOOL RESULT

```
-- CHEUNG
22984:*NWIR: NP sipär-/sipurdan, Bal. siparit/sipar- (< NP), Fariz. -spärd/-spär-, Yar. 
41476:sipar-/sipurdan, 351 
-- HRN
1746:154. bädefräh 'Vergeltung, Strafe'.
10844:154. pahlutn Vortreflflich, ausgezeichnet', pahlumih bozw.
```


## [2026-10-15T02:45:19.445Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22940,23000p CHEUNG.txt; echo ----; grep -n \"zah\\b\\|zah-\\|\\*Hah\\|\\*ah-\\b\" CHEUNG.txt | head -20; grep -n \"tauH\\|\\*tau-\\b\\|\\*stau\" CHEUNG.txt | head",
 "description": "Read Cheung spar- entry and grep other roots"
}
```


### [2026-10-15T02:45:19.828Z] TOOL RESULT

```
*spar 351 


*span(d)/sfan(d) (?) ‘to become agitated’ 

*KHOTANESE: OKh. sphan- ‘to agitate’ = SGS: 136 

*CHORESMIAN: (+ *fra-) ? špn- ‘to cough, groan, sigh’ = Samadi: 198 

*SANSKRIT: ? spand ‘to twitch, lash out (of animals)’ (RV) = EWAia II: 773 

© The existence of this root is uncertain, as the evidence is rather limited and 


ambiguous. 
*REFERENCES: DKS: 437b; Werba 1997: 384 f. 


*spar ‘to hand over, entrust’ 

*MIDDLE PERSIAN: BMP spwit /spurd/ (ppp.) ‘conducted (away)’ || (+ *upa-) BMP 
"psp ’I- /abespar-/ ‘to hand over, entrust [+ ’w 407], give up one's honour, life; to 
commit suicide, extradite someone (to be executed, tormented)’ = DMMPP: 17a 

(+ *upa-) Pres.: IND. 2sg. BMP ’psp’lyh /abesparéh/, 3sg. BMP ’psp’lyt /abespared/, 1р1. BMP 
"bsp'I(y)m /abesparem/, 3р1. BMP ’psp’lynd /abesparénd/; Partic.: pres. BMP ‘psp К /abesparag/, perf. 
pass. BMP ’bsp’It/abespard/, BMP "pswlt /abespurd/; Inf.: BMP ’psp’Itn /abespardan/ 

*PARTHIAN: (+ *upa-) "bysp'r- ‘to hand over" = Ghilain: 75 | DMMPP: 17a 

Pres.: IND. 3pl. ’bysp’rynd; Partic.: perf. pass. 'byspwrd 

*SOGDIAN: (+ *pati-) ? SSogd. pspr- ‘to fix, compose, level’, CSogd. pepr- ‘to alight, 
rest’, MSogd. ptspr(t)- (pass) ‘to be arranged’, ? SSogd. ptspr PN (UppInd.4, 
UppInd.71, UppInd.227, etc.) 

Pres.: IND. 35р. CSogd. pcprty; Impf.: IND. 3pl. CSogd. ptysprnt; Partic.: perf. pass. SSogd. ptsprtyy; 
Pass.: pres. IND. 3sg. MSogd. ptsprtyy ‘is arranged’ 


*CHORESMIAN: (+ *upa-) bsp’ry- ‘to hand over, entrust to” = Samadi: 26 

*NWIR: NP sipär-/sipurdan, Bal. siparit/sipar- (< NP), Fariz. -spärd/-spär-, Yar. 
-spard, Gz. ispär-/ispärt, Gil. (Rsht.) ispurdoen/ispur-, Ham. espartan/espar-, Isfah. 
espartän/separ-, Khuns. ispar-/ispart, Soi bé-spar ‘to hand over, entrust to’, Siv. 
isperd ‘to hand over; to say’, ? Gur. (Kand.) -spär- ‘to bury’ (rather *sparH ?) 

*NEIR: Sh. sipör-/sipört ‘to charge, commission’ (< Pers. ?), Yzgh. s(a)pard/s(a)par-, 
Wa. s(a)por-/s(a)pord/t- ‘to hand over’, Pash. spär- ‘to entrust, commission’ (< Pers. 
?) 

*MISC: Arm. (LW) apsparem ‘I hand over? 

*SANSKRIT: ? spar ‘to save, secure; deliver; gain” > EWAia II: 773 f. 

© This amply attested root may have an IE provenance, being connected to the 
Germanic spare forms. 

«PIE *sper- ‘to deliver, secure’ — LIV: 579 | Pok.: 992 
----
2315:*KHOTANESE: vä- (supplet. *Hah) ‘to be’ || (+ *pari-) LKh. parbav- ‘to overcome; 
5156:(LW), Tal. darz ‘sheaf? || (+ *pari-) NP padarzah ‘a wrapper in which clothes are 
5629:*AVESTAN: OAv. bazuuant- ‘thick, dense’ (Y 40.3), YAv. bazah- ‘thickness, 
5664:*AVESTAN: dobaz- (baz-) ‘to support’, OAv. dobazah- ‘support’ (Y 47.6). © The 
7470:*MISC: ? Par. zah-, Orm. záy-/zàk, jaw-/jök ‘to arrive’ = zey-/zäk || (+ *a-) Раг. aya 
7802:NP garzah (Rudaki). The -z- variants are derived from an unsupported base *garz ‘to 
10525:*Hahl 151 
10558:*Hah! ‘to be’ 
10581:152 *Hah2 
10633:*Hah? ‘to throw’ 
11823:*NWIR: ? NP javazah, Gz. yane ‘mortar’ || (+ *ni-) NP niyaz ‘need’ || (+ *ui-) Khuns. 
11827:Natan. -just/-juz-, Meim. bem-vi:ft/a-vi:z- ‘to discover; to find’. 0 NP javazah is 
11828:from *jaua-a(n)za-ka-, on which see Tafazzoli ("do vazah-i parti az diraxt-i аѕшӣ" [= 
16977:subj. (3sg.) y’h’c of y- ‘to be’ (s.v. *Hah). = Samadi: 142, 153, 195 
17031:BSogd. ’y-/’s- ‘to be’, s.v. *Hah!) 
21155:*AVESTAN: 9 The often cited YAv. razah- is unconnected, as it should rather mean 
26232:thesis: *u ... x > x... f/v/w), NP avazah ‘voice, sound, loud talk? || (+ *ni-) NP 
27977:*AVESTAN: Y Av. vaz- ‘to respect’, Y Av. asa.vazah- ‘respecting Aša’, vazista- ‘most 
30075:*NWIR: NP zäyad ‘is born’, Bal. za(y)-/zat, zah-/zahit, Kurd. zayin/zé- (also 
30246:cease’ and the suggested connection with the postulated Av. root zah- ‘to abandon’, 
23873:366 *stau 
23876:*stau ‘to praise’ 
23938:*staub/f ‘to sound, utter’ 
23945:apparently Пг. root has IE cognates: it is perhaps a blend of the ‘praise’ (*stau) and 
23953:*staup ‘to overcome, defeat’ 
23971:The root *tav- (i.e. *tauH ‘to be able, strong’) suggested by Ghilain (accepted in 
25124:386 *tauH 
25149:*tauH ‘to be able, strong’ 
55322:*tauH 
55612:*bar, *tauH (s.v.), *xsamH
```


## [2026-10-15T02:45:24.956Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 10633,10680p CHEUNG.txt; echo ----; sed -n 25149,25200p CHEUNG.txt; echo -----; sed -n 30050,30090p CHEUNG.txt",
 "description": "Read Cheung Hah2, tauH, zan entries"
}
```


### [2026-10-15T02:45:25.380Z] TOOL RESULT

```
*Hah? ‘to throw’ 

*AVESTAN: ah- ‘to throw’ || (+ *abi-) ‘to throw to’ || (+ *uz-) ‘to throw out on’ || (+ 
*para-) ‘to throw around’ = Liste: 11 

Pres. ja-: IND. 35р. YAv. aphiieiti (Yt 10.20), INJ. 35р. YAv. anhat (Yt 8.6), 3р1. YAv. anhon, SUBJ. 3sg. 
Y Av. anhät, Aor. athem.: INJ. 2sg. (?) OAv. as (Y 34.8), SUBJ. 3sg. OAv. aghat (Y 44.19); Perf.: SUBJ. 
3sg. YAv. uzänhat (Yt 8.39), ОРТ. 3sg. YAv. paranhat (Y 9.11); Partic.: pres. med. YAv. añhimna- (Y 
57.28), perf. pass. Y Av. huu-aiBiiasta- ‘thrown well’ (Yt 13.72) 

*OLD PERSIAN: ah- ‘to throw’ = Kent: 174a 

MED .; Pres. ja-: impf. IND. 3sg. "ähyatä <[a]-h-[y]-[t]-a> (DB 1.95) 


*HaHh 153 


*PARTHIAN: ? ’st’y ‘to throw, scatter’ (Sundermann apud Klimkeit 1989: 171, fn. 16) 
c DMMPP: 55b 

*CHORESMIAN: mjs- ‘to throw, shoot’ || (+ *apa-) ? b'h- ‘to shake off (leaves) 
(Mackenzie I: 546) || (+ *upa-) ? b'h- ‘to kick’. Ф The -s- in the Chor. forms perhaps 
points to an inch. formation. Alternatively, it may derive from older *-st- 
c» Samadi: 177, 11 f. 

*NWIR: ? Fariz. ár-has-, ár-ás-, Natan. ár-as- ‘to rise, stand up’ 

*MISC: (+ *abi-) ? Orm. awök, haw- (supplet.) histak ‘to read’ = aw-/awók ‘to read, 
sing’ 

*SANSKRIT: as ‘to throw, shoot’ (RV+) = EWAia: 144 

© This apparent Пг. root has no certain IE correspondences. The often cited Hitt. 
cognate /siie-/ ‘to throw, release’, may have a different etymology: *seH;I- ‘to 
release’, cf. LIV: l.c. 


«PIE? © LIV: 242 | Pok.: — 
*REFERENCES: IIFL I: 388a; Christensen, Contributions I: 152 f., 255; Oettinger 1979: 473 f.; Werba 
1997: 335 f.; ESIJa I: 94 f.; Kiefer 2003: 192 


*HaH(a)d ‘to speak, say’ 

*AVESTAN: äd- ‘to speak, say’ || (+ *pati-) ‘to reply’ = Liste: 11 

Pres. aja-: SUBJ. 3sg. ҮАУ. paiti.a.óaiiat (N 72 Ё), ОРТ. 35р. YAv. paiti ... aóaliot (V 9.12); Perf.: IND. 
----
*tauH ‘to be able, strong’ 

*AVESTAN: tauu- (tu-) ‘to be able, strong’ > Liste: 26 

Pres. athem.: IND. med. 3sg. YAv. tüite (V 13.8), SUBJ. Isg. OAv. tauuä (Y 28.4, Y 50.11), 3sg. YAv. 
frätauuat (Vyt 51), 3р1. ? YAv. (them.!) tauuan (V 6.51), OPT. 2sg. YAv. fratuiia (Y 9.29); Perf.: IND. 
3sg. Y Av. tütauua (V 6.32); Partic.: pres. YAv. tuuant- (V 3.33) 


*OLD PERSIAN: tav- ‘to be strong’ — Kent: 186a 

Partic.: pres. nu- (?) tunuvant- <tu-u-nu-v-t-> (DB 4.65), <tu-u-nu-v-t-> (DNb 9); Caus.: IND. 3sg. 
tavayatiy <t-a-v-y-t-[i]-y> (DNb 33), impf. 1sg. atavayam <a-t-a-v-y-m> (DNb 47) 

*MIDDLE PERSIAN: BMP twb'n- /tuwan-/ ‘to be able’, MMP tw’n, BMP twb’n 
/tuwan/ ‘might, power’ || (+ *pati-) MMP pt’y-, BMP pt’y- /pattay-/, BMP pt'dst- 
/pattayist-/ ‘to remain, continue; endure’. 0 MMP tw’n, BMP twb’n /tuwan/ are also 
frequently employed as (impers.) verbal aux. ‘to be able’, construed with an 
infinitive. || DMMPP: 330a, 285a 

Partic.: perf. pass. ВМР twb’nst /tuwanist/ || (+ *pati-) Pres.: IND. 2sg. MMP pt’yy, 35р. ? MMP “pt’yd, 
BMP pt’yyt /pattayéd/, SUBJ. 3sg. MMP “pt’y’d, IMPV. 2sg. MMP pt’y, BMP pt’y /pattay/; Partic.: 
MMP "рім 

*PARTHIAN: t’wg ‘strong’ || (+ *pati-) pt’w- ‘to bear, tolerate; (?) to remain, insist 
on’. © On pt’w- cf. Sundermann 1981: 169a: "Die Bedeutung bleiben" ist für mp. 
pattudan wohl bezeugt ..., für parth. pattudan, pattaw- ist m.W. jedoch ... nur ,,erdul- 
den, ertragen” belegt". = Ghilain: 76 f. | DMMPP: 322b, 285a 

(+ *pati-) Pres.: IND. 35р. pt’wyd, SUBJ. 35р. "pt’w’h; Inf.: рма 

*KHOTANESE: LKh. tvafi- (tvafi-) ‘to strengthen’ = SGS: 41 


*tauj2 387 


*SOGDIAN: BSogd. t’w’nty (SCE 10), MSogd. t’wndyy ‘strong, powerful’ || (+ 
*pati-) BSogd. pt’w, MSogd. pt’w ‘to endure’ 

(+ *pati-) Pres.: IND. 35р. CSogd. pt’wt, OPT. 3р1. dur. CSogd. pt^wyntqn; ’z-Impf.: IND. 35р. CSogd. 
pt’w’z ‘he endured’, dur. CSogd. pt’w’sq (GMS: §644); Partic.: pres. BSogd. pt’’wyn’k ‘patient’ 
*CHORESMIAN: t’w’n ‘compensation, fine’ (< NP) 

*BACTRIAN: TOOL, тоо ‘means, assets’, тооооуо, тоооуо ‘fine, Compensation’ 
=> S-W, Bact.: 226a 

*NWIR: NP tavänistan/tavän-, Kurd. tiwänin, Awrom. taway/taw-, Gil. (Rsht.) tan-, 
Gur. (Kand.) -tauw-/-tàü, Isfah. tunän (supplet. ša- < *x8aH), Khuns. tünis, Natan. 
-ton-est/ton-, Shamerz. -tün- (-ton-), Siv. tan-, ten-/tänis ‘to be able’ 

*NEIR: Oss. I. tyx, D. tux& ‘power, might’ 
-----
Pres.: IND. 3sg. z’yyd, z'yd ‘is born’, Ipl. z’y’m, 3pl. z’ynd ‘they bear’, SUBJ. 3sg. "z'y'h, OPT. 
z’yndyy; Partic.: perf. pass. z'd || (+ *4-) Pres.: IND. 3sg. "ууа, 3р1. ’jynd, "pd 

*KHOTANESE: уѕап- ‘to give birth to’, ysai- (pass.) ‘to be born’, ysyafi- (caus.) ‘to 
cause to be born’ = SGS: 112, 114 

*SOGDIAN: BSogd. zn-, CSogd. zn-, MSogd. zn- ‘to bring forth’ || (+ *abi-) BSogd. 
Bz’yn ‘offspring, son’ || (+ *a-) BSogd. ’’z’y, BSogd. ’’z’y ‘to be born, be produced, 
grow; [tr.] to beget, produce’, MSogd. "y ‘to be born’ || (+ *upa-) MSogd. рх? 
‘birth place’, MSogd. pz’tyk ‘homeland-’ || (+ *fra-) BSogd. Bs’nt’k, Bs’ntk ‘child’ 
(Sims-Williams 1983: 50; MacKenzie, SCE: 39) || (+ *ni-) nyz’tcw (f.) ‘born (in 
one’s own house)’ (Yoshida — Moriyasu 1989: 23) 

Pres.: IND. 3sg. (intr., med. ?) znty (v. Gharib 1965: 99), SUBJ. 3sg. CSogd. zn’t ‘she wants to give 
birth’, IMPV. 2pl. MSogd. znd’ bring forth’; Pret.: tr. IND. 3sg. CSogd. znd’rt, Partic.: pres. CSogd. 
zn'mnty ‘giving birth’ || (+ *a-) Well attested: Pres.: IND. 35р. BSogd. ’’z’yt, BSogd. "zyt, OPT. BSogd. 
тугу, etc. 

*CHORESMIAN: Z d (ppp.) ‘born’, z’dk ‘son’ 

*BACTRIAN: бобо, Cadyo, Cadayo ‘born, native’ || (+ *abi-) “aßlavavo (pl) 
‘descendants’ || (+ *а-) aCu- ‘to be born, be produced’ || (+ *fra-) робо, 
oopCivdo ‘descendant’ || (+ *ni-) viķaðayo ‘born (in one's own house)’ = S-W, 
Bact.: 177b, 173, 230a, 208b 

*NWIR: NP zäyad ‘is born’, Bal. za(y)-/zat, zah-/zahit, Kurd. zayin/zé- (also 
pass./intr.), Zaz. zayis/zén-, Abz. zowa/zon-, Anar. (pres. 35р.) ezoya, Awrom. 
zay/-z-, Tt. (Chal za/zas, (Ram.) zā/zāst ‘to give birth’, Gz. zén-/zint, zent, Gil. 
(Rsht.) zaan/zaj-, Gur. (Kand) za/-zi, Khuns. za-/za, Mah. zö-/zä ‘to bear, bring 


466 *zanH2 


forth’ || (+ *a-) NP azad, Kurd. аха ‘free’, (Sor.) ‘free; hero’, Gz. äzzä ‘free’ || (+ 
*fra-) NP farzand ‘child, son’ (< Pth.) 

*NEIR: Oss. I. zajyn/zad, D. zajun/zad ‘to bear, bring forth [usually of animals]; to be 
born, grow’, Pash. zöwul, zézédal ‘to be born’, Yghn. zan-/zänta ‘bear, give birth; to 
be born’, (orig. caus.) Sh. (Baj.) zi(y)-/zod, Rosh. zay-/zöd, Sariq. zey-/züd, zid ‘to 
bear’, Yi. ziy-/zuy- ‘to bear a child’, Yghn. Zuta ‘child, son’ || (+ *a-) ? Wa.
```


## [2026-10-15T02:45:28.753Z] TOOL CALL #20: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-15T02:45:28.762Z] TOOL RESULT

```

```


## [2026-10-15T02:45:30.781Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ستوه",
 "prompt": "Give the full Persian etymology section verbatim, with sources cited."
}
```


## [2026-10-15T02:45:31.407Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/سپردن",
 "prompt": "Give the full Persian etymology section(s) verbatim, with sources cited."
}
```


## [2026-10-15T02:45:32.067Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/زهیدن",
 "prompt": "Give the full Persian etymology section verbatim."
}
```


## [2026-10-15T02:45:32.540Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/أوج",
 "prompt": "Give the Arabic etymology of أوج (awj) verbatim, and the Persian section if present."
}
```


## [2026-10-15T02:45:33.236Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ogive",
 "prompt": "Give the etymology of ogive (and ogee if shown) verbatim."
}
```


## [2026-10-15T02:45:33.834Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/auge",
 "prompt": "Give the Spanish etymology section verbatim."
}
```


### [2026-10-15T02:45:34.474Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:45:34.513Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:45:36.281Z] TOOL RESULT

```
# Arabic Etymology of أوج (awj)

**Etymology (verbatim):** "From the Middle Persian equivalent of Persian اوگ (owg), ultimately from Proto-Indo-European *h₂ewg- ("related to increasement")."

**Persian Section:** There is no dedicated Persian section in this Wiktionary entry. However, Persian اوج (owj) is listed as a descendant of the Arabic term under the "Descendants" section.
```


### [2026-10-15T02:45:36.718Z] TOOL RESULT

```
# Persian Etymology Section

The etymology section for **ستوه** (sutōh / sotuh) is incomplete. According to the Wiktionary page:

"(This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium.)"

No sources are currently cited for the etymology of this Persian adjective. The page indicates that contributors are encouraged to expand this section.
```


### [2026-10-15T02:45:38.588Z] TOOL RESULT

```
# Spanish Etymology Section

From [Arabic](https://en.wikipedia.org/wiki/Arabic "w:Arabic") _[أَوْج](/wiki/%D8%A3%D9%88%D8%AC#Arabic "أوج")_ (ʔawj), from [Persian](https://en.wikipedia.org/wiki/Persian_language "w:Persian language") _[اوگ](/w/index.php?title=%D8%A7%D9%88%DA%AF&action=edit&redlink=1 "اوگ (page does not exist)")_ (owg). "Spelling with _g_ influenced by Latin _[augēre](/wiki/augeo#Latin "augeo")_ ("to wax, to increase")."
```


### [2026-10-15T02:45:41.205Z] TOOL RESULT

```
# Persian Etymology Sections for سپردن

## Etymology 1

From Middle Persian *spūrdan*, *spar-* meaning "to tread, trample."[\[1\]](#cite_note-1) The entry notes this etymology is incomplete and suggests possible Proto-Indo-European origins from *\*sperH-* ("to kick").

## Etymology 2

From Middle Persian *abespurdan*, *abespār-* meaning "to commit, entrust, consign,"[\[2\]](#cite_note-2) derived from Proto-Iranian *\*upa-* + *\*spar* ("to hand over, entrust"). According to Cheung, this traces to Proto-Indo-European *\*sper-* ("to deliver, secure"), though cognate Germanic forms may instead derive from *\*speh₁-* ("to succeed, prosper").[\[3\]](#cite_note-3)

## Sources

[1] MacKenzie, D. N. (1971). *A Concise Pahlavi Dictionary*. Oxford University Press, p. 76.

[2] MacKenzie, D. N. (1971). *A Concise Pahlavi Dictionary*. Oxford University Press, p. 3.

[3] Cheung, Johnny (2007). "Etymology entry" in *Etymological Dictionary of the Iranian Verb*. Brill, p. 351.
```


## [2026-10-15T02:45:44.648Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ogive",
 "prompt": "Give English and French etymology sections verbatim."
}
```


## [2026-10-15T02:45:45.205Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ogee",
 "prompt": "Give the English etymology section verbatim."
}
```


## [2026-10-15T02:45:45.788Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/نستوه",
 "prompt": "Give the Persian etymology section verbatim with sources."
}
```


## [2026-10-15T02:45:46.374Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/زهاب",
 "prompt": "Give the Persian etymology section verbatim with sources."
}
```


## [2026-10-15T02:45:46.951Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/hysteresis",
 "prompt": "Give the English etymology section verbatim."
}
```


## [2026-10-15T02:45:47.554Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/उच्च",
 "prompt": "Give the Sanskrit etymology section verbatim."
}
```


### [2026-10-15T02:45:48.094Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:45:50.469Z] TOOL RESULT

```
# English Etymology Section

Coined by Sir James Alfred Ewing from Ancient Greek ὑστέρησις (hustérēsis, "shortcoming"), from ὑστερέω (husteréō, "I am late, fall short"), from ὕστερος (hústeros, "later"). By surface analysis, hyster- ("higher, outer, latter, next") +‎ -esis.
```


### [2026-10-15T02:45:51.485Z] TOOL RESULT

```
# Persian Etymology

According to the Wiktionary entry, the etymology section states:

"By surface analysis, _نـ_ (na-, "un-") +‎ _ستوه_ (sutōh / sotuh, "defeated, beaten")"

The word is formed through morphological decomposition combining a negative prefix with an existing Persian term meaning "defeated" or "beaten."
```


### [2026-10-15T02:45:51.805Z] TOOL RESULT

```
# Etymology Section

From Middle English *ogeve*, *egeve*, *egeove*, from Old French *œgive*, *ogive*, *augive*, from Late Latin *augiva*, of uncertain origin; compare Late Latin *ogis* ("a support, prop"), Latin *augeō* ("to increase, strengthen"), Italian and Spanish *auge* ("highest point of power or fortune, apogee"). Doublet of *ogive*.
```


### [2026-10-15T02:45:51.959Z] TOOL RESULT

```
# Sanskrit Etymology Section

Back-formed from "उ॒च्चा (uccā́)" and "उ॒च्चैस्" (uccáis); ultimately derived from Proto-Indo-European "*úds-kʷeh₁".
```


### [2026-10-15T02:45:52.343Z] TOOL RESULT

```
# Etymology Sections

## English Etymology

"From late Middle English *ogif*, *egeve*, *egeove*, from Old French *ogive*, *œgive*, *augive*. Doublet of *ogee*."

## French Etymology

"From Vulgar Latin *augīvus*, from Latin *augēre*, as the ogive goes on increasing, and the arch it forms increases the strength of the vault. In Old French we find the phrase *arc ogif*, itself from Latin *arcus augivus*. The word was also written as *augive* in the 17th century."
```


## [2026-10-15T02:45:56.928Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo \"-- PHD\"; grep -n -i \"stōh\\|stoh\\b\\|abespār\\|abespurdan\\|spurdan\\|zahag\\|zahīg\\|\\bzah\\b\\|zahāb\\|ōg\\b\" PHD.txt | head -20; echo \"-- NYB\"; grep -n -i \"stōh\\|stoh\\b\\|apespār\\|abespār\\|spurtan\\|zahak\\|zahāk\\b\" NYB_vol2_glossary.txt | head",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-10-15T02:45:57.343Z] TOOL RESULT

```
-- PHD
166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
518:6 [OL < А Ч; ?w | M ’w] to, at; v. also 6h. ~ gird ámadan: gather, collect (intr.). — ham kardan: gather (tr.). ~ ham madan: gather (¿ntr.); come to an end. *óbad-, v. bastan, *óftadan. Obārdan, bär- Dwf?l-tn! | M ?wb’rd] swallow, devour. Obastan, *dbad- [NPLWN-stn! < A У npl; ^wpstn!, ^wpt- (if not Oft-, q.v.) | M ?wbyst, J ^wfst-] fall. *oftadan, Oft- Pwpt- | M *wpt'd, N uft~] fall. Gear Pwk’l] ebb. ogardan, ógàr- Pwk’l-tn'] remove, expel. *брга ['wgPy] declination, dip. Sh [KN < A kn | Mwh] so, thus; (with verbs, giving a sense of uncertainty) may, perhaps. Ohrmazd Pwhrmgd | M ^whrm(y)zd, N Hórmuzd] Ahura Mazda; astr. Jupiter; cal. 1st day of the month. -om [-wm | = M, N ~] suffix forming ordinal numbers from panjom onwards. -mand [-’wmnd | M -wmnd, N -mand] suffix forming adjectives of quality. *óréb(ih) [wlyp(yh)] disappointment. Dron ['cwlwn! | Mwrwn] hither. ад... ~: since. osán- Pws*n- | = M] throw down. óspurdan, ӧѕраг- [”zospl-tn!] tread, trample. 051°, v. awest^. Ost [220511] firm, reliable. ostigàn Pwstyk’n! | M Iwstyg^n, N ustuwàn?] firm, strong, sure, reliable. ~ih: reliability. lēš [wf | = M, N Ads] consciousness, intelligence. mih: = 68. 268 [wf | = M] death.
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
653:~agig [-yk!] movable; intercalary (year). wihir- [whyl- | (M whwr-)] change. —išn: change. wimand [wymnd | = M] boundary, frontier, limit. ~ig, —6mand [-yk', 2wmnd] bounded, limited. *wiméhgén [wmyhkn! | M wymyh-] *shapely. wimustan [uwymwstn! | M wymrz- (< P)] spoil, destroy. win [wn'] vina, lute. wināh [zs | М zoyz)h, N gunàh] sin, crime. winahgar [wsk] | M wwhg’r, (N gunahhar)] sinner. ~ih: sinfulness. wināhīdan, wināh- [wn’s-ytn' | M wyn’h-] spoil, damage, destroy. ~išn: damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N gunjišk, binjišk] sparrow. win(n)ārdan, win(n)àr- [wyx?7-tn' | M wyn’r-dn] order, fix, arrange. ~išn: arrangement. win(n)irdan [wynltn' | M wynyrdn) be arranged, established; stay. iwir [wyl | M wyyr] man, hero. *wir [wyl | M wyr-, N bir] memory, mind. *wir [wyl | N bir] thunderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guréy] flight, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis [wys | = M] village. wisandan, wisān- [ws’n-dn'] separate. —išn(ih): separation. wisay- (ws'd- | M wys’y-] rest. wisbed [wyspt! | M wysbyd] village headman. wisé [wsydy | (P wsyd), N gusë] despatch. ~ kardan: send, despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
673:zádag [2’tk' | М side, N zāda] born; child. тайап, zan- [MHYTWN-tn! < А У mh; ztn!, zn- | M zdn, zn-, N ~] hit, beat, strike, smite. ~išn: blow, smiting. zadan, zày- [YLYDWN-tn! < A Vyld; z?tn! | M zd, z'y-, N ~] bear (offspring); be born. ~išn: birth. ` ~iSnig : born, engendered, animal. zadār [2t?7] smiter; destructive. zadüg [ztwk! | (N Zad)] gum. zafar [zpl | N ~] mouth, maw (daevic). *zahā [zh?(k')] depth. zahabag [zAh'pk! | N zaháb] spring, source. 1zahag [zhk', (z^ hk!) | М zhg, N zah) child, offspring. *zAhag [2’hk'] element (water, fire, air, earth). zahagómand [zhk'wmnd] pregnant, gravid. zahār [2/7 | N ~] womb. *zahih [zhyh] = zahā, zahr [zh] | M zhr, N ~] poison, venom. zahrag [z()Alk! | N ~a] bile, gall. zalüg [zlwk' | N zali] leech. zam [zm | P zmg] winter.
1223:child aburnüy(ag), frazand, waččag, zadag, zahag.
1294:commit abespurdan.
1354:consign abespurdan.
1782:entrust abespurdan, gumārdan.
2142:gravid zahagómand; v. pregnant.
2967:offspring frazand, paywand, zahag; (daevic) hunušak,
3206:pregnant abestan, abus(tan), zahag- отапа.
3342:reckless gyānabespār.
3679:size wuzurgih, zahā, zahih.
3748:source bunxān, zahābag.
4045:trample spurdan, ēspurdan, wispur- dan, xwastan.
4335:womb a$kamb(ag), aškom(b), burdār, gabr, grāb, pusyān, uruspar, zahār.
4773:spéd spēdag spēdbāg spenāg spóxtan spandan Spandarmad sabuk spul spurrigih spurrig spurdan spūz spēz- spinjānagīh spozgar spūzišn sabz spazg spazgīh spar spar- sprahm sprahmag
-- NYB
1071:-e [-c], -ei [-cy] encl. particle; it precedes other enclitics : adak-ic-iš 8123; ka-c-it 1511: 1. coordinating conj. ‘and’: a) alone: Vahuman Zartuxst-ic 5712-13; 6 han karap mat apar-tc nē spurtan ... guft49!1.24—25; connecting a new section or a new
3109:must go back to *pati-yam- ‘to take hold of’, from Av. (1262sg.) yam-, chiefly with preverbs. I find *pāyam as a v. n. in two passages: 1. DkM 285 aköman ... menisn päyam ‘A. holding Mind in his grasp’; 2. ibd. 501? páyam hešm andar ménisn “Wrath taking Mind in his grasp’ (?). — Zsprm VIII, 4 has a somewhat divergent, perhaps more original version of the story 441-9: ^L ZLWN ‘L y’twk’n, MH-t L>? HWH-nd byšznyt'l, BR’ L'WHL ‘L h'nk' ZLWN, YDH BYN ml PWN "MŠH' ZY TWR’ ZY MDM thé YDLWN-t', hysme bwd wt'p' PWN NPSH-tn' zhk' MNW-t PWN 'škmb' = mà šav o yātūkān, cē-t nē hend bēšazanī- tar, bē apāc 6 xanak šav, dast andar mal pat rógn % gāv i apar ātaxš burt, hésm-ic bod vitāp pat x"ēš-tan zahak ké-t pat aš- kamb ‘do not go to the sorcerers, for they cannot heel thee, but go back home, rub thy hand with ox-tallow which has been. set on fire, and burn fragrant fuel for the benefit of thy offspring which is in thy womb’.
3506:spurtan [spwltn'] spar-, pres. pass. 3d p. sg. sparihét [splyhyt'], to trample (to death) 4876. 4911.14.25, — Av. (1613) spar-; NP sipurdan sipar-.
3544:stob [stwb'] powerless: ~ kartan to de- feat 3319. 858-12, 11574; ~ bütan to be defeated 912. — NW form: MPrth ‘stwb- ‘to enfeeble, to annihilate’ (A-H II, 302 n. 4), evidently a denom. of the adj. ‘stwb = estob (i. e., estöß), taken over by BP as stwb' (the original NW form ’stwb' is still found in FrP, Cod. P fol. 6%) and developed to *stēw > *stöi alternating as usual with stoh, which prevailed: Paz. stoh, stuh, NP sutüh. (The reading stwb' = "stav which I gave in HP was wrong, as shown by the MPrth form ; the spelling -wb- for -v- is unknown in MPrth). The authentic SW form is ‘stw = estav (also in Prth: MPrth ‘st’w- caus. ‘to annihilate’, W.-L. 112, II R 3b) attested in ‘stwy- gwn- ‘to overcome’, ‘stwy-bwdn ‘to be defeated’ (List 81, cf s. v. àkas?), also attested by FrP, Cod. P fol. 284, in the form stw' (erroneously read in Paz. stün, but glossed by sutüh, Anguetil Duperron ‘foible, pauvre’). I derive it from *us- tavah- ‘out of force, powerless’, from Av. (639) tavah-; MPrth estob may go back to *ustava(h)-bū- ‘being powerless’, cf SW ‘stwy-bwdn just mentioned.
5343:spar-: spurtan
7422:supurdan, sipar-: spurtan
```


## [2026-10-15T02:46:03.379Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/زه",
 "prompt": "Give all Persian etymology sections verbatim with sources, especially for meanings 'offspring/birth' or 'spring, oozing'."
}
```


## [2026-10-15T02:46:04.034Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/زهدان",
 "prompt": "Give the Persian etymology section verbatim with sources."
}
```


## [2026-10-15T02:46:05.237Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/úd",
 "prompt": "Summarize the reconstruction, meaning, and list Indo-Iranian (Avestan, Old Persian, Sanskrit, Persian), Greek and Germanic descendants verbatim."
}
```


### [2026-10-15T02:46:08.624Z] TOOL RESULT

```
# Persian Etymology

The etymology section states: "From _[زه](/wiki/%D8%B2%D9%87#Persian "زه")_ (zah, zih) +‎ _[ـدان](/wiki/%D9%80%D8%AF%D8%A7%D9%86#Persian "ـدان")_ (\-dân)."

This indicates the term combines the root element "zah/zih" with the suffix "-dân" to form the complete word.
```


### [2026-10-15T02:46:09.223Z] TOOL RESULT

```
# Proto-Indo-European *úd Reconstruction

## Reconstruction and Meaning
The Proto-Indo-European root **\*úd** is an adverb meaning "upwards, away, out, outward."

## Major Descendant Branches

**Indo-Iranian:** The root evolved into \*ud- prefix form, with descendants traceable through Sanskrit, Avestan, Old Persian, and modern Persian.

**Greek:** Descended through Proto-Hellenic as \*u, appearing in Ancient Greek as the prefix "ὑ-" (hu-) and preposition "ὑ" (hu).

**Germanic:** Evolved into Proto-Germanic \*ūt "out, outward," which generated the modern Germanic language family's directional terms.

The entry notes these forms derive from "comparative evidence" rather than direct attestation, representing scholarly reconstruction of this ancient root's evolution across Indo-European language families over millennia.
```


### [2026-10-15T02:46:11.504Z] TOOL RESULT

```
# Persian Etymology Sections for زه

## Etymology 2 (Birth/Offspring)

**Source text:** "Ultimately from Proto-Indo-European *ǵenh₁- ("to give birth"). Compare Avestan ząθa, "birth", Sanskrit ja, "son of, birth", Ancient Greek gónos, "procreation"."

The term derives from a Proto-Indo-European root meaning "to give birth," with cognates across multiple ancient languages denoting nativity concepts.

**Noun meanings:**
- "(archaic) childbirth" — synonymous with زایمان (zâymân)
- "(obsolete) offspring; child"

## Etymology 3 (Water Source)

**Source text:** "Inherited from Middle Persian *zah, attested in zahābag (/zahābag/, "spring, source"). Compare also zahā (/zahā/, "depth")."

This version comes through Middle Persian, connected to words meaning "spring" or "source" of water.

**Noun meaning:**
- "(archaic) spring of water; water source"

**Derived terms** include زهاب (zahâb, "spring, source") and زهکش (zahkeš, "drain").
```


## [2026-10-15T02:46:15.842Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^\\[pdf page\\|\\[pdf page\" BQT_v2_pages.txt | head -3; grep -n \"ستوه\" BQT_v2_pages.txt | head; grep -n \"سپردن\\|سپاردن\" BQT_v2_pages.txt | head",
 "description": "Grep Borhan vol 2 for words"
}
```


### [2026-10-15T02:46:16.356Z] TOOL RESULT

```
33781:‫ْم اول بروزن گروه «ممعنی‬      ‫ستوه ‪°‬‬
33799:   ‫پازید ‪ . 210005‬ایرای باستان ‪ 6 ۹۱ -۲۵۷۵-‬از‪‌۷‬ها ( نوانستن » فادر بودن ) » ستوه فارسی‬
33801:            ‫ور کے ‪ :‬استوه ‪٠‬‏ ضدآن ‪ :‬دتوه (خستگی ایذیر) مخفف آن «سته» («‪.‬م‪.).‬‬               ‫تبرکه ‪۸‬‬
33833: ‫ستا ‪ 4‬ب=فتح اول ثوالی وتحتالی‌بالف‬                         ‫ستوه است که بمعنی ملول و بتنگهآمده وعاجز‬
33853:                     ‫ستوه ‪.‬‬   ‫‪:‬‬   ‫رکه‬     ‫س‬    ‫‪۴‬‬         ‫‪ - ۱‬رک ‪ :‬استه » استخوان » هته ‪.‬‬
32593:          ‫فاعل سپردن ‪۷‬‬   ‫امر بپردن © _ و‬     ‫‪ -‬و‬
32613:      ‫‪ - ۱‬مراداسم فاعل است ‪ .‬رك ‪ :‬سیاردن » سپردن‪+‬‬                ‫‪ :‬سپاردن » سپردن‪.‬‬   ‫رك‬    ‫®‬
32680:       ‫‪ #‬سپاردن ‪ -‬بکر اول و فتح پنجم مخفف اسپاردن (ه‪.‬م‪ ).‬؛ پهلوی ‪021۳205208‬‬
32681:       ‫[رك ‪ :‬سپردن] و ‪ ۰ 8807110502‬قی‪:‬ارمنی ‪( ۲2۳5-۳2- 0006‬تسلیم کردم » واگذار کردم)‬
32715: ‫فشرد » ماضی‌سپردن است ‪ -‬وبمعنی کوشهشبنی‬
32740:                    ‫رك ‪ :‬سپردن‪. ‎‬‬      ‫‪۴‬‬          ‫حملة دشمن آنرا محافظ اعضاء بدن قرار مبدادند ‪.‬‬
32742:      ‫‪ _¥‬از‪:‬سیر(رك‪:‬سیار) ‪ +‬دن (یسوندمصدری) رك‪:‬سپاردن ‪ ۰‬اسیاردن»سبردن‪‎.‬‬             ‫‪ - ۷‬رکه‪:‬سیردن‪.‬‬
```


## [2026-10-15T02:46:18.966Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 33790,33805p BQT_v2_pages.txt; awk 'NR<33781 && /pdf page/ {l=$0} END{print l}' BQT_v2_pages.txt; awk 'NR<32680 && /pdf page/ {l=$0} END{print l}' BQT_v2_pages.txt; sed -n 32676,32684p BQT_v2_pages.txt",
 "description": "Read Borhan sotuh and separdan footnotes"
}
```


### [2026-10-15T02:46:19.471Z] TOOL RESULT

```
    ‫ججانور‪ ,‬چلریا » دواب)«هوشمان*‪۷ ۲‬؟‪.‬‬       ‫فی‪ :‬افغالی ‪۲‬‬
                                                        ‫حیوان خانگی عموما) «اسشقق ‪٩۲‬‏ ‪۰ ۷٩‬‬
    ‫کث‪ :‬مقدمه‌ص نودودو‪ = .‬اشنیجه = شهمیرزادی ‪asînhso‬‏‬        ‫‪)...‬ر‬     ‫‪ - ۴‬محف سلوسه» ‪E‬‏‬
   ‫[رك‪ :‬اعنوشه]‪.‬درلهج توش[ باکداشان‌چنانکه آ قایرضاتابش نوشته ند‪:‬هاشنشه» بمعنیعطهمتعمل‌است‬
    ‫نگلو‪-‬اکسن‬    ‫وااسهمرا‌ابصنکولتمهاست‪.‬قس‪:‬ا لگلیسی ‪.828808‬انگلیسی میانه‪5 06560‬و ‪1165604۰‬‬
   ‫‏‪ gfnêsan‬ر ‪« 02906۵0۲‬لغت بین‌المللی جدید وبسترسال ‪٤۲۹۱٩‬‏ ‪ .‬امادربارتمصراع‌رود کی(چنان‬
    ‫چون دردمندان را شنوشه» دراینجا همبمعنی عطسه امت چه درطب قدیم در امراض دماغی عطسه‬
     ‫‪ - ۴‬پهلوی ‪28005‬‬                 ‫ژدن رابرای تداوی امراش دماغی و زکام مفید مدانتند ‪.‬‬
   ‫بی‌زور) ‪.‬‬ ‫(‬ ‫‪۷‬‬ ‫‪2‬‬ ‫‪0‬‬ ‫‪5‬‬ ‫ی‬ ‫و‬ ‫ل‬ ‫ه‬ ‫پ‬ ‫‪-‬‬ ‫®‬      ‫ممحنی قله درخت است ی تاوادیا ‪ 9۹۰‬ور کف ‪3 :‬‬
   ‫پازید ‪ . 210005‬ایرای باستان ‪ 6 ۹۱ -۲۵۷۵-‬از‪‌۷‬ها ( نوانستن » فادر بودن ) » ستوه فارسی‬
   ‫مر کب امت از ‪ 2 82۳12۷20-۹۱ :‬قی ‪:‬کوناه ( ه‪.‬م‪ ( ).‬آنکه زورش کم است)‪ .‬‏ رکه ‪:‬‬
            ‫ور کے ‪ :‬استوه ‪٠‬‏ ضدآن ‪ :‬دتوه (خستگی ایذیر) مخفف آن «سته» («‪.‬م‪.).‬‬               ‫تبرکه ‪۸‬‬
                                                                    ‫‪ #‬ستون ‪-‬‬
                                    ‫اشومل و دوم » پهلوی ‪ » 00005‬اوستا‬
                                     ‫‪(8005-‬ستون )‪.‬هندی باستان ‪—anûhts‬‏ (ستون) ‪ ,‬کردی‬
                                                                          ‫‪. 20‬‬


   ‫سیاسیان پوارسیان که ابشان را ابرانیان نیز خوانند ‪ .‬گروهی هستند که ابشان را ایزدیان‬
       ‫ویزدانیانر آبادبان وسیاسیان ووشیان وانوشکان وآ ذرهوشنگیانو آذربانگویند» «دیستان‌المذاهب‬
   ‫‪.‬‬    ‫اسپناح‪‎‬‬   ‫‪:‬‬   ‫رك‬       ‫‪٩‬‬      ‫یمد ‪.‬‬    ‫‪٩ ۷‬‏ برای اطلاع ازعقاید نتسب باین‌فرفه » رك ‪ :‬دستان ص‪۷‬‬          ‫ص‬

       ‫‪ #‬سپاردن ‪ -‬بکر اول و فتح پنجم مخفف اسپاردن (ه‪.‬م‪ ).‬؛ پهلوی ‪021۳205208‬‬
       ‫[رك ‪ :‬سپردن] و ‪ ۰ 8807110502‬قی‪:‬ارمنی ‪( ۲2۳5-۳2- 0006‬تسلیم کردم » واگذار کردم)‬
        ‫از ‪‘ 52۳9۲ :‬رىش ابرالی ‪. 7203 -‬رك‪ :‬یبر گے ‪ ۰ ۵۱‬حوبشمان ‪۷٩۹‬‏ ورك ‪ :‬اسشق ‪۷۹۹‬‬
       ‫افتانی [‪(125205‬سلیم کردن)‪ .‬کردی ‪« 002419‬اسشق‌ایضا» ؛ تسلیم کردن "دادن » بامات دادن ‪.‬‬
   ‫( برهان قاطع ‪) ۱۳۱‬‬
```


## [2026-10-15T02:46:24.877Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"pdf page\" BQT_v2_pages.txt | awk -F: '$1<33781' | tail -1; grep -n \"pdf page\" BQT_v2_pages.txt | awk -F: '$1<32680' | tail -1; grep -n \"زهیدن\\|زاهیدن\\|زهدان\" BQT_v2_pages.txt | head; grep -n \"زهاب\" BQT_v2_pages.txt | head -5",
 "description": "Page tags and zah entries in Borhan"
}
```


### [2026-10-15T02:46:25.380Z] TOOL RESULT

```
16378:                                                     ‫بمعنی بدچهان » زهدان ) «بندهش ‪ ۶۹۰‬ک‪۰‬یلکی ‪. 081‬‬
27003:         ‫«اسشق ‪ , 0۵4۹‬رك‪ :‬زاج > زاچه ‪ .‬زاق » زاقدان » زاد » زه * زهدان » زابیدن « اسشق ‪64۹٩‬‏‬
30240:‫تراوبدن آب باشد اکنزار رودخانه وچشمه‌ونالاب‬                 ‫ولپذا فرزند را زمزاد و رحم و بچمدانرا زهدان‬
30396:      ‫‪ - ۱‬اسم مصدر از «زهیدن»‪ .‬ورك نزهاب‬                             ‫ژه (‪.‬م‪ ):‬ا زارد (زادن) ‪۰‬‬          ‫ار‬
39767: ‫استخر ودوم قلعةٌ شکته و سوم قلمه حتگوان‪:‬‬                       ‫پدر و تاریکی شکم و تاریکی زهدان مادراست‬
1274:             ‫‪:‬‬     ‫زهاب ) ‪ 2‬ساب طبری ‪۹e‬‏‬                 ‫کشدن‬        ‫ی‬‫اهر‬
25037:                                                                     ‫ریزهابی که ازتراشیدن‌چوب ومس وبرنج وامتال‬
25417:                           ‫‪ 3‬زهاب مار باشد ‪۰‬‬
27727:‫چویکی باشد که سنادزهابدان سازنوازند ویعربی‬                                  ‫درخت رگاوند ‪۶.‬‬
30396:      ‫‪ - ۱‬اسم مصدر از «زهیدن»‪ .‬ورك نزهاب‬                             ‫ژه (‪.‬م‪ ):‬ا زارد (زادن) ‪۰‬‬          ‫ار‬
```


## [2026-10-15T02:46:27.981Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 30225,30260p BQT_v2_pages.txt; echo ----; sed -n 30380,30410p BQT_v2_pages.txt",
 "description": "Read Borhan zah entries"
}
```


### [2026-10-15T02:46:28.406Z] TOOL RESULT

```
                  ‫تفه‬
                    ‫مه ص‬
                       ‫اوز‬
                         ‫ووض‬
                           ‫زگرهببان و زه ح‬
                                                            ‫تصین گوبند حمچو آفرین وباركالة ® ‪-‬وبمعنی‬
‫و بفتح اول وظهور ثانی‪ .‬مکان جوشیدن و بر‬                     ‫خوب وخوش هم هت ‪ -‬وزاییدنآ دمی‌وحیوانات‬
   ‫اتشد‪.‬‬  ‫‌ی»بآل‬
               ‫لال‬
                 ‫سی‌ت‬
                    ‫اخفا‬
                       ‫نولو‬
                          ‫آمدن آب ‪-‬ریفتح ت ا‬                ‫دیگر باشد‪٩‬‏ ؛ و باينمعنی بفتح‌اول همآمده‬
‫رهاب = بفتح اول بر وزن شهاب ‪۰‬‬                              ‫‪-‬به‌عنی نطفه وبجه و فرزند همگفته‌اند‬
                                                                                              ‫است و‬
‫تراوبدن آب باشد اکنزار رودخانه وچشمه‌ونالاب‬                 ‫ولپذا فرزند را زمزاد و رحم و بچمدانرا زهدان‬
 ‫‪-‬وضم چشمه را گیوزیند‬
                    ‫وامثال آن ‪٩‬‏ م‬                         ‫شگوته ‪٩‬‏ ؛ و باین معنی بفتح اول همآمده‬

                                ‫ها ‪.‬‬      ‫وكس‪:‬ک‪-‬ون‬
                                                 ‫(‪ )۷‬چ‬                  ‫(‪ )۱‬چك ‪:‬ژند ویاژند ‪.‬‬
                         ‫‪ - ۴‬رك‪ :‬زونگه » زوترك ‪.‬‬              ‫‪ - ۱‬رکه ‪ :‬زودگل ‪ .‬زور که ‪.‬‬
    ‫بممنی زالو » چنالکه در سنگری ‪« 60112‬ك ‪ ۲ .‬ص ‪.» ۹۸۱‬طبری‬                          ‫‪ - ۴‬لهجه ات‬

                           ‫؟ ‏ رك ‪ :‬زواج م رونج ‪۰‬‬                 ‫‪« 1۷‬ساب طبری ‪ › 4۰4‬و رك ‪ :‬زالو ‪.‬‬
                 ‫زه ‪.‬‬   ‫احسن ماك کفت‬      ‫فلك گت‬             ‫ده‬    ‫و قدرگفت‬   ‫کیر‬   ‫قضا کفت‬        ‫_‬    ‫®‬

    ‫‪.‬‬    ‫‪۰۵۹٩‬‏‬   ‫«شاهنامه بخ ج ‪ 4‬ص‬

        ‫‪ ۷‬اوسا ‪( 32۷1 ۳‬وتر کمان ‪ ۰‬رکے) ‪ ¢‬هندی‌باستان_‪[8/9-‬؛‬                   ‫‪.‬‬     ‫دن‬
                                                                                     ‫ی‪:‬‬‫زهرك‬
                                                                                          ‫‪۱‬‬
        ‫بازد از (رسمان»نج)‬       ‫کردی ‪( 1012‬زهکمان) ‪.‬اففانی ‪ : 202‬بلوچی ‪8‬ز «اسشق ‪۷۷۹6۰‬‬
                                                                                        ‫‪‎°‬نامشیوه ‪: ٩ ٩۷۷‬‬
                                                 ‫ساق چون بولاد ‪ .‬بی‌همجون کمان ‪ .‬رکه همجو زه‬

----
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
                                                                                              ‫ات‬     ‫‪0‬‬


‫ودرا دجاگنجی است و من برآن اعتماد دکردم‬                ‫دوابی است در عربی که بفارسی زرلباد گوشد‪.‬‬
‫زهی سلیم دل کهتوباشی ‪ .‬چون این بشنیدباز‬               ‫رهمت = بکر اول بروزن لعمت؛بوی‬
‫زمین میکند‬   ‫آمد ‪۳‬‬     ‫بخالة خود‬    ‫گردید و‬                            ‫شت وبوی ماهی‌خام باشد‪.‬‬
‫تا هاولی زرین بیافت بوزن سی من و از آن‬              ‫زهمن ‪ -‬بفتح اول بروزن بهمن » نام‬
                                   ‫توادگر کف‬
                                                     ‫صاحب آن‬     ‫‪ .‬وتف‬     ‫خانه‌ای بوده در شهر ری‬
```


## [2026-10-15T02:46:33.338Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 1049 1086 1102; do echo \"=== $p\"; timeout 120 python3 tools/ref_page.py BQT:$p 2>&1 | head -60; done",
 "description": "Fetch Borhan cited pages via ref_page tool",
 "timeout": 400000
}
```


### [2026-10-15T02:46:34.116Z] TOOL RESULT

```
=== 1049
no scan of BQT covers printed page 1049 (see 'scans' in refs_online.json)
=== 1086
no scan of BQT covers printed page 1086 (see 'scans' in refs_online.json)
=== 1102
no scan of BQT covers printed page 1102 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:46:37.500Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 32680 30240 30396 33781; do head -n $l BQT_v2_pages.txt | tr -cd '\\f' | wc -c; done; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False)[700:2500])\"",
 "description": "Compute page index of Borhan lines"
}
```


### [2026-10-15T02:46:37.932Z] TOOL RESULT

```
548
508
510
564
om (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/
```


## [2026-10-15T02:46:42.021Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==512' BQT_v2_pages.txt | grep -n \"زه\\|زاه\\|اوستا\\|uz\" | head -30",
 "description": "Print Borhan leaf 511 zah lines"
}
```


### [2026-10-15T02:46:42.553Z] TOOL RESULT

```
5:‫زهی سلیم دل کهتوباشی ‪ .‬چون این بشنیدباز‬               ‫رهمت = بکر اول بروزن لعمت؛بوی‬
7:‫تا هاولی زرین بیافت بوزن سی من و از آن‬              ‫زهمن ‪ -‬بفتح اول بروزن بهمن » نام‬
16:‫بکر اول وزای شله‬           ‫زه وراد‬                   ‫کجابی و دربن شهر سر کشته وحیران چرابی ؟‬
36:                                     ‫باشد ‪. ۴‬‬         ‫اندازه و حد باشد همچنانکه گویند « از زی‬
45:    ‫‪ - ۴‬از ‪ :‬زه (ه‪.‬م‪ ).‬بدن (یوك مصدری ) ‪ .‬لریب‬                    ‫زه ‪ ,‬زاد‪. ‎‬‬        ‫رك‬   ‫=‬   ‫‪١‬‬
```


## [2026-10-15T02:46:47.391Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 509 510 511; do echo \"== NR $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n \"^ *‫ *‪ *- *[۰-۹0-9]\\|زه\\b\\|زهاب\\|اوستا\\|پهلوی\" | head -20; done",
 "description": "Print footnotes of Borhan zah pages"
}
```


### [2026-10-15T02:46:48.167Z] TOOL RESULT

```
== NR 509
29:‫را ليز کوبند ‪ - ۷‬کونارة هرچیزهم‌هست همچو‬                   ‫باداش ندکی است ‪ -‬و کلمه‌ای باشد که در محل‬
35:                           ‫زگرهببان و زه ح‬
46:‫تراوبدن آب باشد اکنزار رودخانه وچشمه‌ونالاب‬                 ‫ولپذا فرزند را زمزاد و رحم و بچمدانرا زهدان‬
52:                         ‫‪ - ۴‬رك‪ :‬زونگه » زوترك ‪.‬‬              ‫‪ - ۱‬رکه ‪ :‬زودگل ‪ .‬زور که ‪.‬‬
56:                 ‫زه ‪.‬‬   ‫احسن ماك کفت‬      ‫فلك گت‬             ‫ده‬    ‫و قدرگفت‬   ‫کیر‬   ‫قضا کفت‬        ‫_‬    ‫®‬
61:                                                                                     ‫ی‪:‬‬‫زهرك‬
63:        ‫بازد از (رسمان»نج)‬       ‫کردی ‪( 1012‬زهکمان) ‪.‬اففانی ‪ : 202‬بلوچی ‪8‬ز «اسشق ‪۷۷۹6۰‬‬
65:                                                 ‫ساق چون بولاد ‪ .‬بی‌همجون کمان ‪ .‬رکه همجو زه‬
71:        ‫‪ ۹‬ت‌ رك‪:‬زهشزه‪.‬‬           ‫‪۱‬‬     ‫«منتهی‌الارب»‬   ‫زىق القمیص ‪ 4‬ره يراهن‬        ‫(‬   ‫‪٥۱‬‏‬    ‫‪۲‬‬       ‫سنون‬    ‫‪۸۱۷‬‬
== NR 510
2: ‫زهدآن * ‪ -‬بچهدان و قرارکله نطنه‬
22:                          ‫سوم کو‬                                  ‫زهار » بنتح اول بروزن نمبازا»نگ‬
42:                            ‫ه‬                             ‫از شیرازه بستن‬         ‫به‬
45:                                                                                        ‫زه ب‬
51:                                                                                     ‫‪ ۱‬رك ‪ :‬زهشس‬
52:               ‫زه‌آبی بدون آندرون سهمگن‪.‬‬                               ‫‪ - ۴‬سوی رود بکااروالیگشن‬
56:                                                 ‫بلگد ناف وزهارهمه (انگور) از من ربد‬
59:   ‫شهنشاهعالم زحازه گرفت‪.‬‬           ‫بشادی مکی‌الجمن‌برشگفت‬             ‫‪( ۱‬واسطه) ‪ +‬زه‪:‬‬      ‫‪ ۴‬از‪:‬زە‬
64:           ‫‪ - ۱‬درزبان کنوبی«زه زدن»‪.‬‬               ‫_ از ‪ :‬زه (ه‪.‬م‪٣+ ).‬‏ دان (بوددمان) ‪.‬‬
65:   ‫‪ - ۲‬پپلوی ‪ . 7022‬ارمنی ع ‪ 7013012‬ازابرالی باستان ‪ * 2۳048 -‬از ‪( 8‬زدن»‬
72:  ‫‪ -‬ایوالقاسم زهراوی خلف‌بن عبای قرطبی " درتاریخطب بزر کتررین نماینده وممرف‬
73:   ‫‪ .‬مولداو زهرا محلی درجوار قرطبه است و اودرفرن پنجم ميزسته‪ ..‬وی‌همهٌ‬                       ‫است‬           ‫ی‬
77:                                                                             ‫ابوالقاسم زهراوی‬      ‫نامه‪:‬‬   ‫لب‬   ‫رك‪:‬‬
== NR 511
14: ‫ززههواب و چشمه‬                            ‫شین نقطه‌دار ‪.‬‬
16:                  ‫ودءوضع جوشیدن وآبر‬                               ‫رهر دادو ‏ زهر معلوم است » با‬
19:                                  ‫ر‬                                 ‫فاد زهر‬     ‫ومریی‬
20:                                                                                    ‫رسیده ‏‪ ١‬پازهر را گونند ‪:‬‬
33:                     ‫رهکو نی ‪,‬‬                                                        ‫دفع زهر افعی وغیزه کنند‬
39: ‫فص وف‬       ‫= بروزن د لک‬         ‫‏‪٩‬‬       ‫زهگر‬                     ‫چسیده امت ‪ - ۴‬و کنابه از دلبری و شداعت‬
43:                                                                    ‫زهرة تست بفتح‌اول‪ ,‬کنایه آازروشنی‬
46:   ‫‪ 8‬طایفةٌحکمامتفق شدند که‌مر ین دردرا دوابی‌یست مگر‬                      ‫‪۲۳‬‬            ‫‪.‬‬   ‫رك‪ :‬بادزهره‬   ‫‪-‬‬    ‫‪۱‬‬
49:   ‫‪( - ۴‬عر) «زهره بم اولرفتح الی وهمچنن سکون دوم ‪۰‬‬                                       ‫زهرةآدمی‪« € .‬گلستان» ‪.4‬‬
51:        ‫چه ستارگزهره ربةالنوع خنیا کرت‬                     ‫‪۴‬‬          ‫ستارةآسمان‌سوم_وشکوفه» « منتهی الارب» ‪.‬‬
52:      ‫‪ - ۱‬اسم مصدر از «زهیدن»‪ .‬ورك نزهاب‬                             ‫ژه (‪.‬م‪ ):‬ا زارد (زادن) ‪۰‬‬          ‫ار‬
53:   ‫‪ « _- ۸‬زهکت الریح الارض » برد‬                                ‫‪ - ۷‬از ‪ :‬زه (ه‪.‬م‪( ۲-2 ).‬پوند سیت) ‪.‬‬
54:      ‫‪ - 4‬افتانی]‪ « 18012‬هوبشمان ‪ .)¥۷۷0‬رك‪ :‬زه‬                                ‫* ‪.‬‬   ‫ویرانبد باد خاك را » «منتهی‌الارب‬
57:                                                                   ‫از‪ :‬زه (ه‪.‬م‪ + ).‬کیر(گیرنده)‪.‬‬            ‫‪- ۶۰‬‬
```


## [2026-10-15T02:46:55.936Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo \"-- HRN\"; grep -n -i \"sut[uü]h\\|sit[uü]h\\|sipurdan\\|sipardan\\|^ *[0-9]*\\. *zah\\b\\|zahidan\\|zihdan\\|zahāb\\|zahdän\\|zahdan\" HRN.txt | head; echo \"-- HUB\"; grep -n -i \"sut[uüō]h\\|sipurdan\\|sipardan\\|zahidan\\|zah\\b\" HUB.txt | head; echo \"-- BRT\"; grep -n \"ustdma\\|ustəma\\|usca\\b\\|usča\\|uzah-\\|uz-ah\\|ustavah\\|^ *tavah-\" BRT.txt | head",
 "description": "Grep Horn, Hubschmann, Bartholomae"
}
```


### [2026-10-15T02:46:56.352Z] TOOL RESULT

```
-- HRN
-- HUB
1195:pazahr, Polak, Persien II, 375, paz. 'pad{a)zah(a)r
2490:zahr 'Gift' = kurd. mhr, iar (ZDM6. 38, 72, 107), zah'r
4612:ap. ^bardah" = zd. barezah^^) *H5he', phi. sup. balist, zd.
4670:gift*, paz. pad(a)zah(a)r Shk. 261 ; np. paz. pasux *Antwort*,
4994:'Edelstein* ; sutuh = Bui6h Mefatigatus, torpidus, tristis ; kuh
6292:sipardan *auf etwas treten' H. 701; supurz *Milz H. 702;
7859:'hoch' = phi. *bardak zu ap. *bardah- = zd. barezah-;
8238:duzah' 'Holle', daozarluha- 'holliseh'; drzem = dzrem *be-
9310:= zd. barezah- ; buland 'hoch' == ap. *brdanUy zd. berezant- ;
-- BRT
2959:j.  ai  aoyaiHii'  P.  2/1  lies:  aSaiy*,  amal. •  j,  g.  aora  Adv.  'nach  unten,  tünunter, hinab':  raocä  (sd.)  usca  usraocayeiti  . .  °ra äraocayäti  V,  2.40  PüZ.;  —  yai  äim  usüa
4248:anfangslosenLeuchten,  der  anC  Lichtraum":' vTspa  'ra  raocä-  usca  usraocayeitiY.2.^o\ PÜZ.;  —  "rd  raocä  x^aoJtä  V.  75.35;  J/.i, 2,  10,  P.j^,  Yt./2.35,  Y./6.6,  77.9, G.J.  6,  S.  2.30;  —  i/ram  mäuhe  hürS •ranqm  raocaukam  Y.  f.  i6|  Yt  ij.57;  — 'ralsra  raocShva  H.  2.  15.  a)  "ranqm
4391:•  j.  ana.x^ästa-  Adj.  'ungekocht':  ratufris *pitus  (sd.)  x'dsiilis  nöit  *'täis\ca\''''  .  . ratufril  mäk^isla  vlzusca  afästais^ca] nSil  "täis  N.57.
4777:ahmst  sISi  dqn  (sd.)  trvjh  utayüitl  Y.  4I5. 10;  57.7,  44.18,  47.1;  —  0,a  haurvaia "rstäta  ySi  slö  /nlzd»n  asaonqm  parSMsti jasmtqm  Yt.  1.25;  —  mazS  (sd.)  avaKyai .  .  daidl  Aaurväd  Titätä  (GD.)  V.  5Ä 7.  a)  als  Bezeichnung  fiir  die  Speise der  Seligen*;'*  at  löi  ubl  haurvassa 3^ar?%äi  3  'r^atasca  (NS.)**  "und  deine beiden  werden  zur  Nahrung  dienen,  der Wohlfahrtstrank  und  die  Unsterbltchkeits- speise"  Y.,?4.  n.  A)  als  Gottheit  {Amasa Spmtd),  der  die  Sorge  für  die  nützUchen Pflanzen  anvertraut  ist  (SüErL:  vanas- patipatiliySi  aya  damaya  fraonnta  akurd .  .  vohu  manu  .  .  a£>m  . .  xsa%rpm  .  . ärmaitil  frä  kaurvatas  fra  'r>tatils  Y.57. 24;  —  vanät  haurvasca  °rstas^a  (NS.)" •wa  sUMtttca  farsmmla  Yt  ig.  96 ;  96 ;  — armaitfm  ..  haurvaiat^m  ..  'rsiatatsm  yaza- maide  Y.16.%;  JI.12,  S,  2.6f.;  —  mazdii dadat  akurö  haurvatö  'riiatascä  .-.  sarS Y. 31.21;  —  data  vj  'rjtSscä (NS.  als VS.)i> utaySitT {%A.)  kaurvatas  draonsY.33.9,;  — iaurvatas^a  'r)tatasca\t.4.i(f)  a)bes. i  in  Dualverbindung  mit  Aaurvatät-:  aya I  damaya  fraornnta  ahurd  masdä  .  .  fra ,  sp^nta  *armaitis/ra  haurvaia  °rHäta  (ND.) Yt.  JO.92;  —  sarBi  bszdyai  (&d.)  haurräiä I  "niaia  (ND.) . .  j?.  .  Y.44.17;  —  upa.- ßm^ti  (sd.)  haurvatä  °r>talä  (AD.)  Y.  45, .  5;  —  sp)ntayai  ärmatSe  haurvalbya  -ntat- '  bya  Yt.  7. 2 ;  H.  i.  7 ;  —  yS  spsntaya  arma- töis  yä  haurvatä  'ntata  (GD.)  Y.  70. 3 ; .  —  kaurvatasca  nö  'ritats,'''^ gTusca  tasiiö.. I  Vr.  g.  5,  a)  amir>tät5  (näml.  ayar?) heisst  der  7.  Monatstag:  S.  7.7;  vgl, 2. 7, ,  V.  7tt.3,  A  1)  als  Bezeichnung  für  die
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
5835:KompA.    —    Vgl.    aHt-n-.    —    ai.  vgl.  asihaii- vänl;    asihima-l-    Adj.  S)     —    Pü. :    ailömaaii, laaSmai-d.  —  ■)  Hds.  aslir.i'.  —  »)  Them.  An 2.  St.  Hds.  ast.ahc.  —  J)  Slveri.  unter  aa/ia-.-. —  4)  Hds.  ';üi!i.  -^  s)   Eine  E^oi   verfehlte Deutung  von  as/za»t-  MSL-  7.  356. •  j.  f,  g.),  p.  aspa-  m.;  j.,  g.  'aapä-,  aspi-  (?) f.  'Ross'>;  Rossstute':   ^räyj  *hai>im.asa- vatiS  .  .  gäusca    "pasca   haomasca   Y.ii.i; 2;  —  II  aniyahyä  -pä  (.\Pm.)  patiyanayam "dem  andern  (Teil)  liess  ich  Rosse  herzu- bringen"    Bh.  /.  18;     —     'pahe     kihrpa aurasahe  Yt.  8.  1 8,  /4.  9 ;  —  -pake  kjhrpa sämaht   Yx.8.z\;    ig.z<)\   —    "pauhB  .. tisaz-ö  ravö.frao^jmanS  Yt/7.12; —  aur- vatiiö  'pa  (als  AP.)  Yt.  10. 42;  —  'pa  (NP.)    . Yt /o.  20,  Aog.  Ä^  Yyl.2f};  —  äsyanha (sd.)    'pafibya   Y.57.  28;  —  yö   mqm  .  . 'paisu  paiti  pantata  (sd.)  Ytj.  50;  ig. 77;  —  harisaesu  paiti  'panqm  Yt;o.  11;
6022:urvä  gsusca  'zya  "meine  (des  Stiers)  Seele
6052:•  j.  *azdya-'>  Adj.  'wohlgenährt,  fett': »^  pasusca  (statt  IS.)  ^nsii'a  «aV  irisla (sd.)  (sAV)  anatäya  ratu/ris  aianta  airista *°yii . .  N.  56;  —  ratufris  *paysbis  . .  *yaista an&idyäisia  .  .  *pitui . .  *'yäiil  nSit  *aitaz- ifas..SiUlJkSniscä  vitttsca,.*'yais  nSii  *anaz~ ijäU  N.57;  —  ratu/ris  ^anmanqmca  . . *'yanam  nSit  ^anazäyanam  (sd.)  N.5<?.
6092:—  masda  . .  ahurö  hyal  höi  °/a  vohucä cöist  (sd.)  manatihs  Y,  4^5. 10;  —  akurB mazdä  sar^mra  {^.)  vohä  manattha ..°sa hulAaxa  Y.j2.a;  —  at  hvö  'sahyä  anhat vatihsusca  vastrl  (sd.)  manauhS  Y.  33.  3 ;
6097:—  vohü  uxsya  (sd.)  matiauhä  xiahrä 'sä^ä  (Instr.)  usta  tatiäm  \. 33.10; —  in GHapt:  'säatcä  ha^a  vatihsusca  manatshs vantaus&i  xsa^rat  Y. 35.10.  e)  neben Ärmatay-:  vatihSus  xsd^ra  mananhä  'sä mal  armaitis  vaxH  (sd.)  Y.  34. 1 1 ;  48. 1 1 ;
```


## [2026-10-15T02:47:00.958Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{60\\}usca  *Adv.\\{150\\}\" BRT.txt | head -3; grep -n -o \".\\{30\\}ust[a-zə3]ma-  *Adj.\\{200\\}\" BRT.txt | head -3; grep -n -o \".\\{40\\}'werfen'.\\{150\\}\" BRT.txt | head -5; grep -n -o \".\\{40\\}us-, *uz-.\\{200\\}\" BRT.txt | head -3",
 "description": "Grep Bartholomae for usca, ustema, ah- werfen"
}
```


### [2026-10-15T02:47:01.736Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:47:04.553Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{30\\}usca  *Adv.\\{120\\}\\|.\\{30\\}ustama.\\{120\\}\\|.\\{30\\}us\\.tavah.\\{80\\}\\|.\\{30\\}werfen.\\{60\\}\" BRT.txt | head -12",
 "description": "Grep Bartholomae alternate spellings"
}
```


### [2026-10-15T02:47:05.126Z] TOOL RESULT

```
3492:.  äpa,  np.  af-gandan  ('wegwerfen',  Bthl. IF.  //.  il6)JJ.  —  Pü.:  ii;tf,  (Komp.  auch):
6722: F. 7.  2)  II  militärisch  'werfen'  sva.  'drängen in  — '  (Lok.):  aniy<^  äpiyä  *,lAyata^
15623: j.  pairi.spätay-  f.  'Herumwerfen,  Hin- werfen, Hin{ein)fanenlassen' :  nöil  attqm nöil  va
18806:m  *k^m  JanaOa    V.S.       werfend'?  VgL  die  SteDe  ait  pahis^^äiay..  ~ 74.  a)  vom  Fe
19176:niederzufegen,  zu Boden  zu  werfen':  ka'^ä  alai  drupm  dyqm sastayS  (sd.)  iiT  Alm  m'  %
19446:t  harn  'nieder-,  zu Boden  werfen,  unterdrücken'.  —  PPfP. °mtita-,  Inf.  "mistSe,  •mista
23255: gefallen  lassen und  ihn  abwerfen.  —  >)  Anders  jetit  lo.  54. I  Aber  l)  erwartete  ic
26751:it  aus  *siirii-  f.  'Niederwerfen',  »um  V. ^star-,  —  Pü. ;  visiarisnömand. j.    slirmli
26906:Yt. 19.  So- mit aipi  'zurückwerfen,  -schleudern  auf  -' {upa  mit  Akk.):  ustrahe..yd  kafi
29460:und) nieder-,  zu  Boden  zu  werfen,  zu  unter- drücken': frada^äi  vJspaya  asaonö  stsis •tS
29607:s  das  Mass   angebt,   hin- werfen,  soviel  als  .  .".    —    0  PQ.  hat  dafQr fräc,  was
```


## [2026-10-15T02:47:09.024Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 6700,6730p BRT.txt | cut -c1-600 | grep -n -i \"uz\\|werfen\\|ah-\" | head; grep -n -o \".\\{80\\}tavah-  *n\\..\\{150\\}\" BRT.txt | head -3",
 "description": "Read Bartholomae ah- werfen entry"
}
```


### [2026-10-15T02:47:10.140Z] TOOL RESULT

```
22:•  ].,  p.  "ah-  V.  'werfen'.  Praes.  26  ahya-, auhya-  (,  aäha-  '>,  ar^ia-'l).  PPf  P.  atta-; Absol.  'ashm,
23:1)  'werfen  (eine  Waffe),  schiessen':  arstii yqm  *an/iyeili'^  avi.>tiiiris  Yt  10.  ao;  *2i; —  tiyris" .  ,  yi'm  an/iaf  »rsxsö  (sd.)  Yt  8. 6;  —  äsyatjka  Avastayn  {sA.)  *arikima- nayäi^  (GD.)  Y.57.  28;  —  yalat  hvasttm (sd.)  *a»Ayeiti''>  Yt/0. 21;  —  asia  F. 7.  2)  II  militärisch  'werfen'  sva.  'drängen in  — '  (Lok.):  aniy<^  äpiyä  *,lAyata^'>  "der Feind  wurde  ins  Wasser  gedräng "" /.  19.
25:mit  ava  'herabwerfen':  * avanhynti^''  F. 23  a«^
26:mit  US  'hinaus-,  hinaufschicken':  pairikä .  .  ya  uzStihat  aurS  matnyus  Yt-Ä  39.
27:mit /am  'umwerfen,  umschütten':  yals- yanilm  (sd.)  rif>m  *j>arä!iMt  (als  Praet) » Y.5.11.
```


## [2026-10-15T02:47:14.545Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{20\\}tavah-.\\{120\\}\" BRT.txt | head -5; grep -n -o \".\\{20\\}ustsma-.\\{150\\}\\|.\\{20\\}ustima-.\\{150\\}\\|.\\{20\\}ust3ma-.\\{150\\}\" BRT.txt | head -4; grep -n -o \".\\{30\\}usca.\\{20\\}Adv.\\{120\\}\" BRT.txt | head -3",
 "description": "More Bartholomae greps"
}
```


### [2026-10-15T02:47:16.092Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:47:18.730Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \"tavah.\\{100\\}\" BRT.txt | head -5; grep -n -o \".\\{10\\}ust.ma.\\{100\\}\" BRT.txt | head -5; grep -n -o \"j\\.  *usca.\\{150\\}\" BRT.txt | head",
 "description": "Bartholomae loose greps"
}
```


### [2026-10-15T02:47:19.851Z] TOOL RESULT

```
3318:tavah-  m.  Name  eines  Bergs oder  Gebirgs:  ahma^  kam  garayB  fraoxs- yqn  . .  °vasca  Yt,  if).  6
14944:tavah-   Adj.  'seine  Kraft   da- gegen   einsetzend,  Widerstand  erhebend': nsit  'vä  iavaiti  (sd.) 
16468:tavah-  Adj.  'zweifinger- dick': as/?m  . .  'vatafum  (ASm.  als  n.)  vä bipTDSU.masargfDm  vS  V,  6'
```


## [2026-10-15T02:47:23.805Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{40\\}tavah-   Adj.  'seine.\\{250\\}\" BRT.txt; grep -n -o \"j\\.  *tavah-.\\{200\\}\" BRT.txt | head -3",
 "description": "Context for tavah in Bartholomae"
}
```


### [2026-10-15T02:47:24.164Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:47:26.594Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 14944p BRT.txt | cut -c1-400; sed -n 14943p BRT.txt | tail -c 200; grep -n -o \"tavah- n\\..\\{150\\}\\|tavah-  *n\\..\\{150\\}\" BRT.txt | head",
 "description": "Print Bartholomae line context"
}
```


### [2026-10-15T02:47:27.120Z] TOOL RESULT

```
/.  132  und  Pü.  —  Pü.  (lu  l):  patirak  raaiihük, (zu  a):  löäin,  erl.:  fa  ifästaij  i.  zu  A%d.. ■  j.   paiti.tavah-   Adj.  'seine  Kraft   da- gegen   einsetzend,  Widerstand  erhebend': nsit  'vä  iavaiti  (sd.)  Yt.  JO.  48.
830
```


## [2026-10-15T02:47:30.347Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"uzma\\|^ *ud-\\|ud- \\|ud-pat\" KNT.txt | head -20",
 "description": "Grep Kent for ud and uzma"
}
```


### [2026-10-15T02:47:30.695Z] TOOL RESULT

```
211:BSOS - Bulletin of the Sehool of Oriental Stud- ies, London. ;
1128:Final -d disappeared after 1, as in the enel. OP -cly, Skt. cid, pIE q*id; OP лаш ‘not’, Av. лб, from *ne + id. After и the final t seems to be retained as § in OP akunaus ‘he made’, adarsnaus ‘he dared’, Skt. ákrnot ddhysnot; but this § is better taken as an extension of the s of the aorist, after which -t would be lost. The prefix ud ‘up’, which appears unchanged before a vowel in ud- apatatā ‘he rose up (in rebellion)’, suffers com- plete assimilation of the d in uzma- ‘stake’ (from *ud-zma-), and became us- in us-taSand- ‘stair- case’ in the dental cluster (585).
1608:This shortening took place in most languages before and after consonants; OP example: uzma- ‘stake’ from *ud-zma-, §84.
2038:Loc. Sg. Parsaiy, Mädaiy, Mudrüyaiy, Ujaiy Unjaiy, Pardavaiy, Arminiyaiy, Asagartaty, Hagmatanaty; with added -à, duvarayd, dastayd, spaémardayd, probably kar Saya, {dalrtanayd; nt. uzmaya.
2599:II. The secondary ending was pIE -io, as in Gk. ёферєто, Skt. dbharata; this is seen in OP ud- араай (Gk. &érero, Skt. épatata), anayatà (Skt. dnayaia), amariyata, früámáyalà, agarbüyatà, agau- bata, ham-ataxsatd, dyasatd, |a|h[yat]à, adalrayat|a, [ат]аоаій, passive akunavayatd, perhaps aor. (h)amarmalà and perf. pass. cazr[zyala] or [claxr|iyata]; non-thematie remade to thematic, avarnavaté and aisiata; non-thematic aor. akula (Skt. dkria) and imf. patiy-ajatd (Skt. dhata).
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea’ (not ‘islanders’, since the term denotes the sa- trapy of which Dascylium was the capital, JNES 2.304). With ‘king’, singular nouns are in the loca- tive, as in DB 1.2 xSéyatiya Pérsary ‘king in Persia’, though plurals are in the genitive (§250.C); similarly DB 1.81 zšaçam tya Babtrauy ‘the kingship in Babylon’. It is a substitute for the genitive in DB 2.23f hya Madaisuvd тайа dha ‘who was chief among the Medes’ (cf. §250.D).
2705:B. Expressing place to which, with prep. уйй ‘as far as’, in DSf 32 abara yata Bābiraw ‘carried as far as Babylon’, 34 у010 Сй {уа ‘as far as Susa’; perhaps also, because of the idea of motion which seems to be in the verbs, in gátavà avástáyam (DB 1.62f), güfavü niyaSadayam (РМа 36), maškđuvā avükanam (DB 1.86), uzmayà-patiy (DB 2.76, etc.).
2864:(DB 2.16°, 3.26), ‘оп’ with locative in uzmayá-
3619:76 dra : avaina : pasivasim : Hagmatànaiy : uzmay&patiy : akunavam
3634:9] uzmayapatiy :akunavam p :8tly : Daravavaus : xšāyaðiya : ma : tya : ma
3646:Rl. has the following correct readings, in whieh he records as visible certain characters, here indicated by roman type, which were not visible to KT: * Naditabai- fram; *бай]у : Dárayavaus; *aham : i[mà; * Auri; з rhiyal6iya; * nama : var[danam; ” avais;  Dárayavaus : xéáya[frya; ? haeáma; * hya; * mahya : VI : ralucabes (VI is corrected to VIII by КІ. on page 218); * parazta : pat(is; 9 Armaniyaiy (RI. misread the third character); * vasiy; * ham[igrya; *! Uvaz[Stra]hyá; *! uzmayapat]iy.
3730:90 ауайуа : pasiva : adam : ava : Vahyazd&tam : uta : martiya : 51 tyaisaiy : fratamā : anuSyáà : Shata : Uvidaicaya : пата : var 92 danam : Parsaty : avadasiS : uzmayápatiy : akunavam : 64
3767:92 uXiyà : &hatà : Babirawv : uzmayāpatiy : akartyata
4956:Aéiydbausna- sb. ‘Athiyabaushna’, father of Arsaces ($168.11): cpd. of (Av.) ai- ‘destruction, misfortune’ + pass. pte. of d-baug- ‘to free’ ($248) with late -šn- from -aén- (Bv. BSLP 29.2.104, cf. Av. pouru-baozóna- ‘bringing abundant rescue, Bthl. AiW 901): ‘Freed from misfortune’ ($160.14; not active ‘bringing freedom from misfortune’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
4995:and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, pIE *apo. Used with vb. gaud- and in sbb. apaddna-, apa- niydka-; with suffix in apalara-, apara-.
5177:ud prep. and prefix ‘up’, becoming Iran. us- uz- before dentals ($85): Av. us- uz-, Skt. ud, pIE *ud (and *üd in NEng. out, NHG aus): ud with verbal root раф, us- in ustaxand-, u(z)- in uzma- (S84).
5226:uzma- adj. as sb. ‘that which is up from the earth, stake’: from ud- ‘up’ + zma- to zam- ‘earth’ ($84, $95, $120, $130, §142, 5148.11, VI): other- wise Wackernagel, KZ 61.208; Lommel, OLZ 37.180.n2; König, RuID 72. uzmayā-patiy lsn. DB 2.76, 91; 3.52, 92.
5341:gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
5372:gud- vb., see gaud-.
5624:ud- + pat- ‘rise up, rebel’ (cf. Ву. TPS 1945.64-
```


## [2026-10-15T02:47:35.647Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^ *ogee\\|^ *ogive\\|ogive\" SKT.txt | head; echo \"-- LKT\"; grep -n -i \"auge\\b\\|ogive\\|auǧ\\|awj\\|aug \" LKT.txt | head; echo \"-- DEV\"; grep -n -i \"OGIVE\\|^ *AUGE\" DEV.txt | head; echo \"-- KLN\"; grep -n -i \"^ *ogee\\|^ *ogive\" KLN_1966.txt | head",
 "description": "Grep Skeat, Lokotsch, Devic, Klein for ogive"
}
```


### [2026-10-15T02:47:36.142Z] TOOL RESULT

```
7611:tials.»A.  S.^V^M.  togive.+!oeL^y/i gift,  G.  -gift  I  in  mitgi/t^  a  dowry).     Der gif'itd. ttimard.  (F.-L.)    M.  V      -  -  "'-
12701:Ogee,  Ogive,  a  double  cunrc  (F.  «• Span.  —  Arab. )  *  An  ogiue  or  ogte,  a  wreath, circlet,  ot  round  band  in  architecture,' Minshcu.  An  ogee  arch  is  a  pointed  arch, with  doubly-curted  sides.  —  O.  F.  attgwtt off^vf,  an  ogive  or  ogee  (Cot.  V  —Span,  augr, highest  point;  from  the  pointed  top  of Moorish  .irches,  which  have  doubly-cuned sides.  — Arab,  ihtij,  summit.  Der.  ojpv^, adj.  (.also  wiitten  ogre-falH).  See  p.  579.
23699:French  from  Spanish  from  Arabic,  am* ber,  cotton  (i),  fonfnre,  galingale,  garble, garbage,  genet,  ;ennet  (genact),  lackey Jacquey).  mojJc  (masque),  masquerade, mosque,  ogee  (ogive),  racket  (1)  traquct), realgar,  ream,  »umach,  syrup  (sinip),  tabby, talc,  tare  (3),  tariff,  zenith,
-- LKT
304:'Auge',  plr.  a'jän  wörtlich  'Augen', übertragen  'Vornehme'.  Ebenso  tk. Hieraus  rum.  aian  'Vornehmer'.  Frz. ayan  'tk.  Beamter,  der  für  die  öffent- liche Sicherheit  zu  sorgen  hat'.  [Devic DEt  52.
525:'Höhe,  Kulmination,  Apogäum  [Erdferne als  Fachausdruck  der  Astronomie]'  als technischer  Ausdruck  und  in  verall- gemeinerter Bedeutung  [z.  B.  höchste Glückswonne]  ins  Romanische  über- gegangen: it.  sp.  kat.  pg.  anye,  frz. auge  'Apsiden'.  Ableitung  von  lat. awjerc,  wie  z.  B.  Constancio  Dicc  140  b, ist  aus  lautlichen  Gründen  abzulehnen. Das  ar.  Grundwort  ist  möglicherweise selbst  fremden  [persischen,  indischen oder  griechischen]  Ursprungs.  [DE  217. Devic  DEt  48.  Lammens  Rem  29/30. ML  782.
1084:^Quelle,  Springbrunnen'  [desselben  Ur- sprungs wie  5äsm  'Auge'  Horn  NpEt S.  98,  Nr.  440],  vgl.  ar.  'ain  'Auge'  und ^Quelle,  Brunnen',  ebenso  tk.  cesme; hieraus  rum.  cl§mea  'Brunnen,  künst- liche Quelle';  bulg.  cesma,  serb.  cesma, cesma  'dass.'.    [Bern  SlEtWb  151.
1825:'Weinende'  oder  'diejenige,  die  Schmerz in  den  Augen  hat'  [vom  Vb.  gamisa 'von  schmutzigem  Flusse  triefen'  (vom Auge  gesagt)].  Die  Araber  nannten Sirius  undProcyon'die  beiden  Schwestern des  Ganopus'.  Da  Procyon  sich  erst  über den  Horizont  erhebt,  wenn  der  Sirius verschwindet,  sagte  man,  Procyon  weine über  die  Entfernung  ihres  Bruders,  da- her der  Name  al-gimaisä'' ;  hieraus  der Sternname  Algomeiza  'Procyon'.  [Devic DEt  40.
2060:851.  Tk.  hawjar:
2558:Auch  karakol,  karawul,  karaul  'Wache' [vom  Stamme  kar  'Auge,  sehen',  z.  B. tk.  kara  'Augapfel',  Vämbery  TktElWb S.  78.  Nr.  831];  hieraus  rum.  caraulä 'Wächter,  Schildwache';  bulg.  karaul, karaimil,  karakol  'Wache',  serb.  kara- ula,  karawula  'Wachtturm,  Schilder- häuschen', klruss.  kalawur  'Wacht- mann',  russ.  karaul  'Wache',  karaulka 'Schilderhäuschen'.  [Gorjajew  134. Bern  SlEtWb  489.
2560:Die  lustige  Figur  des  tk.  Schattenspiels, etwa  'Kasperle'  [aus  tk.  kara  'schwarz' und  göz  'Auge'  vom  Stamme  kar,  kor, kör,  köz  'Auge,  blicken'  Vämbery  Tkt EtWb  S.  79,  Nr.  83 II];  hieraus  rum. caraghios  'Possenreißer,  närrisch',  ca- raghioslic  'Possenhaftigkeit,  Spaß' ;  frz. caragueiise  'Marionettenfigur'.  [Ausführ- liches über  die  Figur  des  Karagöz  s. Georg  Jacob ,  Türkische  Literaturge- schichte in  Einzeldarstellungen.  Heft  1. Das  tk.  Schattentheater.  Berlin  1900. S.  19  ff.,  sowie  G.  Jacob,  Die  tk.  Volks- lileratur.  Berlin  1901.  S.  33/34  ]
2832:'Blind',  vulg.  Aussprache  kjör;  hieraus rum.  chior  'einäugig';  bulg.  k'or  'blind', serb.  cor  'auf  einem  Auge  blind'  und Ableitungen.
3182:1375.  Hebr.  iiiakk^b^d: 'Hammer';  hieraus  Eiyenname  Macca- baeus  'Makkabäer'  und  mit  verschieden- artigem Bedeutungswandel  it.  (dial. Abruzzen)  maccabe  'Dmumkopf,  Tauge- nichts', frz.  machabee  im  Pariser  Argot : 'Jude;  Leiche  eines  Ertrunkenen'.  — ML  5253  [wo  auch  fälschlich  macabre hierauf  zurückgeführt,  s.  dagegen  hier Nr.  1372].
4260:1882.  Hebr.  s^lö  inö'il: 'Derjenige,  der  nichts  taugt;  Tauge- nichts'; hieraus  dtsch.  Schlemiel,  Schle- mihl  'Pechvogel',  bes.  bekannt  durch CH AMISSOS  ,  Peter  Schlemihl',  den Schattenlosen.  [Ablt.  von  TORCZYNER in  ZDMG  L,  557 ;  andere  Ableitungen : a)  Eigenname  Selümfel  Num.  1.  6;  II, 12,  ein  jüd.  Fürst,  so  Ave-L  IV,  470; denselben  Namen  soll  ein  Rabbinerschüler des  XIV.  Jahrhunderts  in  Ens  in  Öster-
-- DEV
653:Auge.  Terme  d'astronomie.  Nom  qu'on  donnait  autre- fois à  ce  qu'on  nomme  aujourd'hui  apsides,  c'est-à-dire  les points  où  une  planète  se  trouve  à  sa  plus  grande  ou  à  sa plus  petite  distance  du  soleil  ^.  Esp.  ange,  ital.  auge.  De ^^î  aouclj,  sommet,  point  culminant,  que  les  astronomes arabes  emploient  dans  le  même  sens.
2859:Auge.
-- KLN
26151:ogee,  n.,  1)  a  molding  having  an  S-shaped  curve;
```


## [2026-10-15T02:47:38.809Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 520,526p LKT.txt | cut -c1-500; sed -n 26151,26165p KLN_1966.txt; grep -n -i \"ogive\" DEV.txt PHN.txt | head",
 "description": "Read Lokotsch awj and Klein ogee"
}
```


### [2026-10-15T02:47:39.373Z] TOOL RESULT

```
Npr.  Ein  Urenkel  von  UMAIJJA,  dem Stammvater  der  Umaijjadendynastie, gab  einem  Stadtviertel  Bagdads  den Namen,  also  al-'aifäbija.  In  diesem Viertel  wurden  die  bunten  StolTe  aus Seide  und  Baumwolle  hergestellt,  die nach  dem  Ursprungsorte  einfach  'Attäbl- Stoffe  genannt  wurden.  Hieraus  mit W eglassung  des  ar.  Art.  it.  sp.  pg.  tabi, frz.  tabis  [wozu  das  Vb.  tabiser  'wäs-
sern, d.  h.  inoirieren'  gehört];  engl. tabby,  ndl.  tabijn,  dtsch.  Tabin  'schweres, glattes,  moiriertes  Seidenzeug'.  Poln. tabin,  tobin;  klruss.  polutabcnt  mit  An- gabe eines  weiteren  Herkunftortes. (DE  343/4.    Mikl  SlEtWb  346.
134.  Ar.  'attär:
'Verkäufer  von  Parfümen  und  Drogen [ar.  'är],  Drogist';  hieraus  mit  dem  ar. Art.  sp.  alatar  'Drogist'.    [DE  59.
135.  Ar.  au^:
'Höhe,  Kulmination,  Apogäum  [Erdferne als  Fachausdruck  der  Astronomie]'  als technischer  Ausdruck  und  in  verall- gemeinerter Bedeutung  [z.  B.  höchste Glückswonne]  ins  Romanische  über- gegangen: it.  sp.  kat.  pg.  anye,  frz. auge  'Apsiden'.  Ableitung  von  lat. awjerc,  wie  z.  B.  Constancio  Dicc  140  b, ist  aus  lautlichen  Gründen  abzulehnen. Das  ar.  Grundwort  ist  möglicherweise selbst  fremden  [persischen,  indischen oder  griechischen]  Ursprungs.  [DE  217. De
136.  Kas.  tat.  unl:
ogee,  n.,  1)  a  molding  having  an  S-shaped  curve;
2)  an  S-shaped  curve.  —  F.  ogive.  See  ogive, ogival,  adj.,  having  the  form  of  an  ogive.  —  See next  word  and  adj.  suff.  -al. ogive,  n.,  1)  the  diagonal  rib  of  a  Gothic  vault;  2) a  pointed  or  Gothic  arch.  —  F.  ogive,  earlier also  spelled  augive;  of  uncertain  origin.  Cp. ogee.
ogle,  intr.  v„  1)  to  keep  looking  amorously ;  2)  tr. v.,  to  look  at  amorously.  —  Of  LG.  origin.  Cp. LG.  oegetn,  freq.  of  oegen,  ‘to  look  at’,  rel.  to Du.  ogen,  ‘to  look  at’,  fr.  uog,  ‘eye’.  See  eye. Derivatives:  ogle,  n.,  ogl-er,  n.
Ogpu,  n.,  formerly,  the  secret  service  of  Soviet Russia.  —  Russ.,  formed  from  the  initials  of O bjedinionnoje  Gosudarstvennoje  Politicheskoje Vpravlenie  (United  Government  Political  Ad¬ ministration).
ogre,  n.,  1)  a  man-eating  giant;  a  hideous  or cruel  man.  —  F.,  first  used  by  Perrault  in  his fairy  stories,  1697;  in  English  it  appears  first (spelled  hogre )  in  a  translation  of  a  French version  of  the  Arabian  Nights;  fr.  Byzantine Ogur,  ‘Hungarian’.  The  sense  development  is due  to  a  confusion  of  the  Hungarians  with  the Huns  and  the  Tartars.  See  Wiener  in  Anglia, XXIII,  107,  and  Meyer-Liibke,  Romanisches etymologisches  Worterbuch,  p.  446,  No.  6048. Cp.  Ugrian.
Derivatives:  ogre-ish,  adj.,  ogr-ess,  n.
Ogygian,  adj.,  primeval,  prehistoric.  —  Lit.  ‘per¬ taining  to  Ogygius’,  fr.L.  Ogygius,  fr.  Gk.
’  Aydyio;,  fr.  fiyuyr,;,  name  of  a  mythical  king of  Attica.  For  the  ending  see  suff.  -ian. oh,  interj.  —  Of  imitative  origin.  Cp.  O. ohm,  n„  the  unit  of  electrical  resistance.  —  G. Ohm,  from  the  name  of  the  German  physicist Georg  Simon  Ohm  (1787-1854).
Derivatives:  ohmage  (q.v.),  ohm-ic,  adj. ohmage,  n.,  electrical  resistance  expressed  in ohms.  —  Formed  fr.  ohm  with  suff.  -age. ohmic,  adj.,  1)  of  an  ohm;  2)  measured  in  ohms.
—  Formed  fr.  ohm  with  adj.  suff.  -ic. ohm-meter,  n.,  an  instrument  for  measuring  elec¬ trical  resistance.  —  Formed  fr.  ohm  and  -meter, oho,  interj.  —  Compounded  of  the  interjections O  and  ho.
-oic,  a  -suff.  used  to  form  names  of  acid,  as  in caproic  (chem.)  —  From  the  ending  of  benzoic, -oid,  adj.  suff.  meaning  Tike,  resembling'.  The  ad¬ jectives  so  formed  are  often  used  substantively in  the  sense  ‘something  resembling  .  Gk. -oetS'/j?,  for  -o-eiStjc,  formed  fr.  -o-,  stem  vow¬
el  belonging  to  the  preceding  element,  and -eiSy]?,  Tike’  (cp.  e.g.  8axTuXo-EtS-/]q,  ‘finger¬ like’,  and  see  dactyloid),  lit.  ‘having  the  form  of’, fr.  eISoi;,  ‘form,  shape’,  which  stands  for*j-sT- 8op,  and  lit.  means  ‘that  which  is  seen",  fr.  I.-E. base  *weid-,  *woid-,  *wit-,  ‘to  see;  to  know’, whence  also  Gk.  tSetv  (for  */i8e1v},  to  see, oTSa  (for  *Fot8a),  ‘I  know’.  See  -o-  and  idea and  cp.  words  there  referred  to.  Cp.  also  -ode, ‘like’.  Cp.  also  the  second  element  in  collidine, iodine,  Ixodidae.
-oidal,  suff.  forming  adjectives  from  nouns  end¬ ing  in  -oid.  —  Compounded  of  the  prec.  suff. and  adj.  suff.  -al.
Oidium,  n.,  a  form  genus  of  imperfect  fungi  (hot  ) —  ModL.,  dimin.  formed  fr.  Gk.  oiov,  ‘egg’. See  oo-.
oil,  n.  —  ME.  olie,  oile,  fr.  OF.  oile  (F.  huile),  fr. L.  oleum,  fr.  Gk.  IXaiov  (fr.  *eXxtfov),  ‘olive tree’,  which,  together  with  Arm.  ewl,  is  prob. of  Aegean  (most  likely  Cretan)  origin.  OE.  trie, OS.  oli,  OFris.  and  Du.  olie,  OHG.  olei,  oli (whence  MHG.  ole,  ol,  G.  Oli,  oil ,  are  loan words  fr.  L.  oleum.  Cp.  ole,  oleagineous,  olive and  elaio-.  Cp.  also  the  second  element  in  anele, carbolic,  lanolin,  linoleum,  rhigolene.
```


## [2026-10-15T02:47:43.686Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; for w in ستوه نستوه سپردن سپاردن زهدان زهاب زاییدن اوج; do echo \"== $w\"; grep -n \"$w\" ARY_pages.txt | head -4; done; grep -n \"UD\\b\\|UD-\\|\\bUD \" ARY_latin_index_pages.txt | head",
 "description": "Grep Aryanpur for the Persian words"
}
```


### [2026-10-15T02:47:44.112Z] TOOL RESULT

```
== ستوه
== نستوه
== سپردن
10023:۰ | سپاردن» اسپاردن» سپردن
== سپاردن
10023:۰ | سپاردن» اسپاردن» سپردن
== زهدان
== زهاب
2465:آلمانی کهن (/027۵4۸ بزهابز صا0): صربی (۷ل5581۸4): 357۸۸
12163:آلمانی کهن (/0ف/نع05 تزهابز صام: 0رتهلا 6 (۲متته)) ای
13745:آلمانی کهن (0274۸(0 بزهابز صا0) :۸۸010 ق۶۲00
== زاییدن
== اوج
2993:8117313811۸ 6 ((811805) ,87 (5۸8ق) +7 راوجمه
795:cael a9 5d gaat Balad Glia (orks jl ote PUD U OYA) oj LLS
1413:| BUCK: 1285 AMRAUD (WELSH) «$5
1632:UD-+MATI SANSKRIT) 4 Sonile HOLD PERSIAN) Stoel go jh,
1641:lai S(UDTAMOS 4) UD -\ spy! y ta wataely 92 jt el Sp eesti onl ghey! sels
2129:MACKENZIE: (CLOUD) 167 AMBRIA, CELTIC) ( gS) gh
2149:BRAUD (OLD IRISH) pS 5) EYEBROW, BROW :(ENGLISH) Si
2726:Gajly eed dy ay Seat (UD y ott gta salle shy yg OT gat Gas Bh ya Sh yy!
3817:BOUTON ER, BUD
3890:BUNDRUS, —-(LITHUANIAN) =) BUD-, BAOTHI-, —{AVESTAN) ply!
5146:FOUL ENGLISH) gS -BUD HOSSETIC) «gi 3\
```


## [2026-10-15T02:47:46.329Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 10005,10035p ARY_pages.txt; grep -n \"pdf page\" ARY_pages.txt | awk -F: '$1<10023' | tail -1",
 "description": "Read Aryanpur separdan entry"
}
```


### [2026-10-15T02:47:46.761Z] TOOL RESULT

```
دانمارکی (7ل0۸(۷/5): 118 لفت‌نامه دهخدا : ۱۳۳۶۶
سوئدی (8/80/57): 1
یادداشست:
۱ چم این واژه در زبان یونانی: مخروط درخت کاج.
واژه‌های فارسی "ساییدن" و آسودن" و "بسودن" نیز از همین واجریشه‌اند (۳۵۳073790 :542)
اوستایی (4۲574۸): ۸۸۰ ,۸8522 3۸
پهلوی (بابلهه): 5۸ ساکونی کهن 54000۷0 ۰:00 5831۸8۷
ی با کردی (130/5): 4 باه فریزی گهن (/(۴۴/514 0ا0): 51۸
1۹ " بلرچی (اپل الم , 6 ,ل52 آلمانی کهن (08741۸0 107 01):
افغانی (پشتو) رس 81۷1۸۱۷ ۸رد
تخاری 8 (8 70827۸4۸): 30 آنمانی (08821۸۷): لد انا ان
سانسکربت (8/5877): ی انگلیی کهن (2(/050 ۰:0۵ 8213۸۷
یرنانی 078570): 541 انگلیسی (57/ا8/0): الا ادن
لاتین (712ها): 5۳1۸ دانمارکی (0۸/[574): لول رن
گریکه (00777/0): ادن سوئدی (817570150): 5.۸
ایسلندی کهن (504010704۵7 0ا0): نروژی (/0/0050140: لاهن
[pdf page 339]
اا ‏ اااااا ‏ )گگ گگ 1
۰ | سپاردن» اسپاردن» سپردن
هلندی (7ل[ع0077)+ ول ۱۸ ان
اسلاوی کهن (ع#1ما؟ 0710767 صا0): پسگشت‌ها کید دا
52 9918 1 و 2۵08۵0
لهستانی 10/870 لد 0 00018880 و
روسی (/4۸ا۸(85). داد :2/۸052
چکه (لل280)): 570 2 (00190فتا8 ,5(۸2)
صربی (8878140): در 6243 82
بوهمی (8071611۸2): لران 50۵1۸ :۸03 ۸ ۸/702
لتونی (لتی) (/(477/14): 58785 ,583۸ برهان قاطع : . ۱.۷۹
آلبانی (/(۸ا/(مقلام: 5 5[
یادداشت: ۱
۱ واژه‌های انگلیسی 8 و 817۸0017 و آلمانی 5211۸7788 از بکه واجریشه‌ی نزدیکه به ابن
10021:[pdf page 339]
```


## [2026-10-15T02:47:49.943Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/اوج",
 "prompt": "Quote verbatim the Mo'in entry for اوج, including origin tag (e.g. [ع.] or [معر.]) and any etymology."
}
```


## [2026-10-15T02:47:50.534Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/ستوه",
 "prompt": "Quote verbatim the Mo'in entry for ستوه including origin tag."
}
```


### [2026-10-15T02:47:52.562Z] TOOL RESULT

```
Based on the webpage content, here is the Mo'in dictionary entry for ستوه:

"(سُ) [ په . ] نک استوه ."

This entry indicates the word's pronunciation (sU), includes a reference marker (په), and notes "نک استوه" as related etymological information.
```


### [2026-10-15T02:47:53.144Z] TOOL RESULT

```
# Mo'in Dictionary Entry for اوج

According to the content provided, the Mo'in Dictionary entry for اوج reads:

"( اَ ) [ معر. ] (اِ.) 1 - بلندی . 2 - طرف بالای هر چیز. 3 - بالاترین درجة ستاره . 4 - بلندترین حد آواز."

**Translation of definitions:**
1. Height/elevation
2. The upper part of something
3. The highest degree of a star
4. The highest range of sound/voice

The origin tag [معر.] indicates this is a borrowed word (معرّب).
```


## [2026-10-15T02:48:04.910Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f(){ python3 tools/fetch_source.py \"$1\" --note \"$2\" 2>&1 | tail -1; }\nf 'https://en.wiktionary.org/wiki/سپردن' 'page 516, root Ud 1: sepordan etymologies (MP abespurdan < *upa-spar; spurdan tread)'\nf 'https://en.wiktionary.org/wiki/أوج' 'page 516, root Ud 1: Arabic awj from MP *awg'\nf 'https://en.wiktionary.org/wiki/ogive' 'page 516, root Ud 1: ogive from Latin augere (French etymology)'\nf 'https://en.wiktionary.org/wiki/ogee' 'page 516, root Ud 1: ogee uncertain origin, Late Latin augiva'\nf 'https://en.wiktionary.org/wiki/auge' 'page 516, root Ud 1: Spanish auge < Arabic awj'\nf 'https://en.wiktionary.org/wiki/نستوه' 'page 516, root Ud 1: nastuh = na- + sotuh'\nf 'https://en.wiktionary.org/wiki/hysteresis' 'page 516, root Ud 1: hysteresis coined by Ewing from Greek husteros'\nf 'https://en.wiktionary.org/wiki/उच्च' 'page 516, root Ud 1: Sanskrit ucca < PIE *uds-kweh1'\nf 'https://en.wiktionary.org/wiki/زه' 'page 516, root Ud 1: zah birth (< *zan-) and zah spring (MP zahabag)'\nf 'https://en.wiktionary.org/wiki/زهدان' 'page 516, root Ud 1: zahdan = zah + -dan'\nf 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/úd' 'page 516, root Ud 1: PIE *ud descendants'\nf 'https://vajehyab.com/moein/اوج' 'page 516, root Ud 1: Moin owj [moarrab]'\nf 'https://vajehyab.com/moein/ستوه' 'page 516, root Ud 1: Moin sotuh [Pahlavi], see ostuh'",
 "description": "Archive web sources used",
 "timeout": 300000
}
```


### [2026-10-15T02:48:08.183Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/898518140f8984ab.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b8d88d1dcd6648e7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/69974985becd14f7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/006d2f0d5ccdfedb.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/92d72c721f004801.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6afcfb22f4af3a87.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b512b55ca1fc1dc7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/89e017d05a8f4147.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2151778c9fa6745c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ec3584f18d955021.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/92101beedb8b858b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/905069ded0b09fb4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4406742805ec0820.txt
```


## [2026-10-15T02:48:12.998Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *ud\\b\\|^ud \\|^ *ud-\\|^ūd\" IEC.txt | head -5; grep -n -i \"^ *out, \\|^ *Out,\\|^ *But,\\|^ *About,\\|^ *Hysteresis\" SKT.txt | head; grep -n -i \"hysteresis\" KLN_1966.txt | head -2; grep -n \"ستوه\\|سپردن\\|زهدان\" ../../MON_part2.txt 2>/dev/null | head -3; grep -n -i \"aug\\b\\|auj\\b\\|ōj\\b\" HRN.txt | head -5",
 "description": "Grep Mann, Skeat, Klein, Horn"
}
```


### [2026-10-15T02:48:13.394Z] TOOL RESULT

```
19521:udór (udor, obl: udn-) ‘water’. Cf. üdros, à, uodór, uodor, uodn-. WP I, 252 Skt. cf. udan, n. “water, wave’; Oss. cf. wdain, v. ‘water, wet, urinate? beside wdásin, v. “get wet; Myc. cf. (queried) udo(r), oblique: udoro-(!) ‘water’; Gk. hüdor, gs: hüdatos, n. id.; Umb. utur, loc. sg: une, n. id.; Latv. ūdens, m. id. (Full-gde in Hitt. watar, gs: wetenas, see ued- (2) below, but the isophone of the above type, uttar, gs: uddanas = *rés, word, thing, legal action"). Cf. Skt. sam-udráb, m. *water's meet, catchment
19527:ūdhər (üdhen-) ‘udder, teat. (Gk. variant uüdhər-, -en- ?). WP I, 111 Skt. üdhar, n., ūdhas, n., udhan, n. ‘udder’; Av. udaro, m. ‘belly’; Gk. cf. oüthar, gs: oGthatos, n. id. perb. w def. article; Lat. über, gs: überis, n. as Skt.; OS üdar, sm. & n., MHG üter & iuter, id. w. def. art.?; LG üder, n. id.; Du. uier, m. ‘teat’; (LW in Finn. udar *udder and in Marian or Cheremis vádar, vodár, id. Mod. Eng. udder shortened fr. OE Oder. n. id. Cf. Li. adróta, adj. f. *milch-; in calf, in pig”, etc.)
12930:Out,  without,  abroad.  (E.^  M.E.  CTi/i-, uU,  adv.  A.  S.  W/f,  i//dn.  adv.,  out,  wiih> out ;  formed  (with  adv.  sufBx  -*  or  -an) frona  AS.  tit,  adv.  out,  from,+t>u-  <"A Icel.  1//,  Don.  »</.  Swcd.  ff/»  G.  aus,  Goth. «/  (-AS.  i//),  w/a  (-A.S.  tiU).  utana ( =  A.  S.  titan) ;  Skt.  uJ,  up.  out.  (Aryna IID.)  ^  Hence  nunicfous  compounds,  such OS  9ut baianctf  outbid,  outbnakt  present- ing no  difficulty.
17164:about,  skuita,  ikctta,  to  leap  about ;
20704:out,  result intervene,  to  come  I>et«reen   t'
24005:out,  away :    F.  rar/r  •  Low  L.  i-or/a,
18547:hysteresis,  n.,  the  lagging  in  the  magnetic  force behind  the  magnetizing  force  {magnetism).  — Gk.  uaxspTjCTu;,  ‘shortcoming,  deficiency’,  fr. oaxepetv,  ‘to  be  behind,  come  late,  lag’,  fr. uoxepov,  ‘later’.  See  hysteron  proteron. hysteria,  n.  —  Medical  L.,  fr.  Gk.  uaxipa,  ‘womb’, which  is  rel.  to  uaxpo?  (Hesychius),  ‘belly, womb’,  and  cogn.  with  Maced.  oSepo c,  (Hesy¬ chius),  of  s.m.,  OI.  udaram,  ‘belly’,  L.  uterus, ‘womb’;  see  uterus  and  -ia.  Hysteric  distur¬ bances,  which  most  frequently  occur  in  women, were  ascribed  erroneously  to  the  influence  of the  womb  and  were  for  this  reason  called  hys¬ teria,  ‘disease  of  the  womb’, hysteric,  more  frequently  hysterical,  adj.  —  L. hystericus,  fr,  Gk.  uaxepixo?,  ‘pertaining  to  the womb’,  fr.  uox£pa.  See  prec.  word  and  -ic,  resp. also  -al.
6013:nach Haug, aber gewiss nicht richtig].
6296:aw. i/^stav-y staomi preisen ; phlv. stätaUj stät/ttan,
7611:AUg. entlehnt; echt bei. köpak, n. ßöfay (211)
10378:ap. [/^drauj-^ adnrujiya 'er log'; aw. Vdraoj-,
14231:l/^drauj'j adurujlya 73.
```


## [2026-10-15T02:48:16.496Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4990,4996p HUB.txt; sed -n 6290,6293p HUB.txt; grep -n \"^ *ud-\\|\\bud-  *Adv\\|'ud'\" IEC.txt | head -3; grep -n -i \"^ud\\|^ ud\" IEC.txt | head -5",
 "description": "Read Hubschmann context, Mann ud"
}
```


### [2026-10-15T02:48:16.908Z] TOOL RESULT

```
phi. aatn (reap. a«g«) s. oben p. 10; mazldan *8augen, schmecken' s. § 17.
*) Dazu ciguna, can *wie*, zaryun etc.— 143 —
§ 313. Ap. au = phi. o kann (vor A, vor Doppelkon-
sonanten etc.) im Neup. verkurzt werden : guhar = gGhar
'Edelstein* ; sutuh = Bui6h Mefatigatus, torpidus, tristis ; kuh
= koh 'Berg'; anduh = andoh *Kummer : htiS = hds 'Ver-
stand'; bustdn = bdstan 'Garten'; tuxm 'Same' = paz. tuxm^
H. 696; supurdan 'anvertrauen H. 697; sipas Dank, Lob'
(Etym.?) H. 698; sipah 'Heer H. 699; sipar 'SchM H. 700;
sipardan *auf etwas treten' H. 701; supurz *Milz H. 702;
siparl Vollendet' H. 703, oben p. 73; sipanj *Ruheplatz'
19518:uderos, om ‘belly, stomach’. WP I, 190 Skt. udáram, m. ‘belly, stomach, womb’; Cy- priot óderos (‘stomach’, Cypr. -o- for Gk. -u-. WP). (Isophone: Fris. otter (2) “stack of cut peat")
19519:udor-, see udor
19520:udn (üd-ono) ‘out, outside’. Cf. od. ono Hitt. udne, udni, s. ‘countryside’; OE ütan(e) ‘from outside; MHG üsen, prp. & adv. out, side; ON útan, adv. ‘from outside, away’; OCS vünü, adv. and com. SL, Cz. ven, R von ‘outside, away
19521:udór (udor, obl: udn-) ‘water’. Cf. üdros, à, uodór, uodor, uodn-. WP I, 252 Skt. cf. udan, n. “water, wave’; Oss. cf. wdain, v. ‘water, wet, urinate? beside wdásin, v. “get wet; Myc. cf. (queried) udo(r), oblique: udoro-(!) ‘water’; Gk. hüdor, gs: hüdatos, n. id.; Umb. utur, loc. sg: une, n. id.; Latv. ūdens, m. id. (Full-gde in Hitt. watar, gs: wetenas, see ued- (2) below, but the isophone of the above type, uttar, gs: uddanas = *rés, word, thing, legal action"). Cf. Skt. sam-udráb, m. *water's meet, catchment
```


## [2026-10-15T02:48:19.796Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *697\\. \\|^ *701\\. \" HRN.txt; n=$(grep -n \"^ *697\\. \" HRN.txt | head -1 | cut -d: -f1); sed -n \"${n},$((n+8))p\" HRN.txt",
 "description": "Read Horn 697 supurdan"
}
```


### [2026-10-15T02:48:20.565Z] TOOL RESULT

```
6118:697. Hiipävden anvertrauen, übergeben*, jüd.-pers. p1N?10,
6149:701. seperden, siperden auf etwas treten*.
697. Hiipävden anvertrauen, übergeben*, jüd.-pers. p1N?10,
supiirden, sipäris (sifärls).
g. vaspartmün.
aw. tis-\- 2. l/'par-; phlv. avspärtan, avspurtan. (vd. 5
(77)), spiirtltan (AV.); ai. iid -{- "lA^par- 'hinüber-
führen', utpdrana- 'Übersetzen*; vergl. lat. portäre.
af/. späral übergeben'; kurd. sipärtin.
Die Etymologie stammt von de Lagarde, ist aber
sehr unsicher. Bei siperl (No. 703) passt die An-
```


## [2026-10-15T02:48:25.025Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==176' HRN.txt | head -60",
 "description": "Print Horn printed page 154"
}
```


### [2026-10-15T02:48:25.711Z] TOOL RESULT

```
— 154 -
694. (2)säii 'Teil, Stück; Art und Weise'; -$an gleich,
ähnlich, -sä.
Die Deutung von aw. sü^ia- (yt. 19, 44) als *Stück'
(Studien, I, 148) hat Geldner BB. XV, 254 wider-
rufon.
LW. kuid. säriy z. B. kH\sän *öü; wie?', va]suna auf
diese Weise'; afy. San; bei. sang (236).
Np. -sä^) hat das auslautende n verloren, wie äsuid,
a (No. 52), senrjso (Käs. Z. zu 1. süh) u. a. ni. Gehört
np. 'äsan 'äsä gleich, ähnlich* auch hierher?
695. säf/e 'Schatten, Schutz'.
ai. chayd' 'Schatten'; plilv. sayak,
kurd. se^ si\ bei. säig, n. saJ (340); wa;^. LW. sayd,
sar. suyä,
696. supär Tflug .
ai. phdla- Tflugscliar*, zu l^phal-, splial- *aufreissen'.
sar. spur 'Pflug .
697. Hiipävden anvertrauen, übergeben*, jüd.-pers. p1N?10,
supiirden, sipäris (sifärls).
g. vaspartmün.
aw. tis-\- 2. l/'par-; phlv. avspärtan, avspurtan. (vd. 5
(77)), spiirtltan (AV.); ai. iid -{- "lA^par- 'hinüber-
führen', utpdrana- 'Übersetzen*; vergl. lat. portäre.
af/. späral übergeben'; kurd. sipärtin.
Die Etymologie stammt von de Lagarde, ist aber
sehr unsicher. Bei siperl (No. 703) passt die An-
knüpfung an l^par- ausfüllen* besser.
698. »Ipäs 'Dank*.
phlv. späs, späsdär; arm. spas-em aufwarten, dienen',
spas 'Dienst'.
^) Np. sä *Tribut* ist dagegen au8 *sävaka- entstanden, vergl. die
Form säv (Nöldeko, Pers. Stud. II, 20 Anm. 4). In der Bedeutung
'kostbare Art Stoff* (Vis und Rämln 52 Vers 7 v. u.) wird es ebenfalls
hierher gehören.
```


## [2026-10-15T02:48:28.443Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 200 python3 tools/ref_page.py IRN:108 2>&1 | head -80",
 "description": "Fetch Iranvij page 108",
 "timeout": 250000
}
```


### [2026-10-15T02:48:28.929Z] TOOL RESULT

```
(no exact page map; using offset 11 -> pdf page 119; check the printed number and re-run with --pdf-page if off)
REF: IRN:108  PDF: data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf page 119  OCR-lang: fas

۱۸ ایرانویج
می گیرد و پس از آنکه بخش جنوب شرقی ترکیه را آییاری کرد وارد کشور عراق
می‌شود. در این سرزمین از تنگه‌های کوهستانی‌بسیار می گذرد و در ناحیةٌ کردستان
در پائین موصل» آبهای زاب بزرگك وزاب کوچک ك که ازکوههای غربی ایران
سرچشمه می‌گيرند به‌آن می‌پیوندند. این رود زا ب که در فرهنگها وکتابها ی
جغرافیای تاریخی کندن آن را به «زو» پادشاه داستانی ایران نسبت می‌دهند, در
اصل ترکیب شده است از واژه‌های «زه» و «آب» واین ترکیب همانست که در
واژهٌ «زهاب» در نام محل سرپل زهاب» دیده می‌شود. دراين ترکیب زه به
معنی زاینده است از ريشهٌ 22 به معنی زاییدن وزهاب یا زاب به‌معنی رود زاینده
است و بازاینده‌رود هم‌معنی‌است . نام های محلی اين دو زاب درکردستان‌به گویش
محلی «زی بج وکث» بدا 2:27 زاب کوچکه‌و«زی گور»80۷۳2 227 -زاب بزرگك
است .

اروندرود سپس بینْ سامره وبلد وارد دشت میانرودان می‌شود ورسوبات رود
دیاله آن‌را به‌سوی غرب می‌راند. رود دیاله از بهم آمیختن رودهای «سیروان»و
«زالم» و«تنجه‌رو» پدید می‌آید وجای پیوستن این رودها «دوآوان» نام دارد.
دیاله در همه مسیر خود در سرزمین عراق به‌نام یکی از رودهای تشکیل دهنده
آن» سیروان نامیده می‌شود ونزدیک «سلمان پا کك» درجنوب بغداد به دجله می‌ریزد
و دجله را به سوی غرب می‌راند و آن را به فرات نزديکك می‌سازد, رود دجله
پس از پیمودن مسافتی دوباره به‌سو ی کوههای زا گرس باز می گردد ونزدیک عماره
در اثر رسوبا تکرخه به سوی جنوب می‌گراید و در «الغرنه» در ء + کیلومتری
شمال بصره رود فرات به‌آن می‌پیوندد . سپس در شمال جزيره آبادان رود بزرگك
کارون به آن می‌ریزد واروند رود بزرك پس از پیمودن طول جزیرةٌ آبادان به
دریای پارس می‌ریزد. درازای این رود از سرچشمه تا دریای پارس نزديکك به
۰ کیلویتراست ودر سال . ه میلیون تن رسوب دارد که از مقدار رسوب رود
نیل بیشتر است .
```


## [2026-10-15T02:51:07.307Z] TOOL CALL #66: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-516.json",
 "content": "{\n  \"pdf_page\": 516,\n  \"book_page\": 486,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-10-14\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ud 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ud (*úd) adv./preverb 'up, out, away'; extended *uds-, comparative *ud-tero-\",\n      \"note\": \"Pokorny 1103-1104 ud- 'empor, hinauf, hinaus'; Walde-Pokorny I 189-190; Watkins/AHD ud- 'up, out'. Root, label and gloss are correct. The Old Iranian, Sanskrit, Greek and Germanic branches are standard. The problems are in the Iranian compounds Nourai builds on it: Persian sepârdan 'entrust' comes from *upa-spar- per MacKenzie and Cheung, not *us-spar- (Horn's etymology after de Lagarde, which Horn himself calls 'sehr unsicher'). Persian zah/zahidan 'give birth' is usually derived from *zan-/zā- 'bear', not from uz-ah- 'throw out'. French ogive/ogee is no longer derived from Spanish auge < Arabic awj; Klein says 'of uncertain origin' and Wiktionary gives Latin augere. Arabic awj is generally treated as a loan from Middle Persian *awg, so the Sanskrit ucca link is only a hypothesis. Sotuh/nastuh < *us-tavah- 'out of strength' is supported by Nyberg and Mo'in.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ud «بالا، بیرون، دور» (پوکورنی ۱۱۰۳–۱۱۰۴، والde-پوکورنی، واتکینز) درست است و پیشوندهای اوستایی us-/uz-، پارسی باستان ud-، سنسکریت ud-، یونانی hus-teros و ژرمنی *ūt همه از آن‌اند. «ستوه» و «نستوه» از ایرانی باستان *us-tavah- «بی‌توان» را نیبرگ و معین تأیید می‌کنند. اما «سپاردن» در پژوهش امروزی (مکنزی، چونگ) از *upa-spar- است، نه *us-spar-. «زه/زهیدن» به معنی زاییدن را هم بیشتر از ریشهٔ *zan- «زادن» می‌دانند. پیوند فرانسوی ogive با اسپانیایی auge و عربی «اوج» نیز امروز پذیرفته نیست. خودِ ریشه را نورایی درست آورده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/úd\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1103\", \"status\": \"supports\", \"note\": \"POK_full.txt l.93520ff (Page(s): 1103-1104): 'Old Indic ud-, ut- \\\"empor, out\\\" proverb; Avestan us-, uz- (*uds-) ds., ap. us-, ud-' ... 'Gothic ūt Adv.'; '2. Kompar. Old Indic uttara- ... = gr. hysteros \\\"the spätere\\\" ... Avestan ustəma- \\\"äußerster, last\\\" ... about Old Indic ucca- \\\"high\\\" (*ud-kʷe), ucca, Avestan usca Adv. \\\"above\\\"' — root, gloss and all IE branches on the chart are there.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I pp. 189-190 s.v. ud- (WLD_Bd1_pages.txt l.17460-17520)\", \"stance\": \"supports\", \"note\": \"'Got. ūt Adv. „hinaus, heraus“, ahd. ūʒ, nhd. aus, as. ags. ūt'; 'germ. uz- „aus, aus — heraus“' — same root ud- 'auf, hinauf, hinaus'.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.1102 s.v. ud-\", \"stance\": \"supports\", \"note\": \"'ud-. Also ūd-. Up, out. 1. Germanic *ūt, out ... BUT; ABOUT ... 3. Suffixed (comparative) form *ud-tero- in Greek husteros, later ... HYSTERESIS ... [Pok. ud- 1103.]'\"},\n        {\"src\": \"KNT\", \"where\": \"Lexicon p. 176 s.v. ud (KNT.txt l.5177)\", \"stance\": \"supports\", \"note\": \"'ud prep. and prefix \\\"up\\\", becoming Iran. us- uz- before dentals: Av. us- uz-, Skt. ud, pIE *ud (and *ūd in NEng. out, NHG aus)'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"ud, us, uz; us-tavah; ni-us-tavah; us-spar; uz-ah, zâ 2; uz-ah-âp\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Avestan has the preverb us-/uz- < PIE *ud(s)- (POK 1103; Kent p.176). The form ud- is Old Persian and Sanskrit, not Avestan. us-tavah- 'out of strength' (us- + tavah- 'power', cf. Av. paiti.tavah-) is not attested in Avestan but is Nyberg's reconstruction behind MP stōh/NP sotuh, so it is plausible as *us-tavah-. ni-us-tavah is Nourai's own construct; NP nastuh is simply na- + sotuh. uz-ah- is a real Avestan compound of ah- 'to throw' (Yt 8.39 uzāŋhat 'sent out'; Bartholomae, Cheung *Hah2), but it means 'throw/send out', not 'give birth'. Avestan zā- 'bear' belongs to *zan-, so equating uz-ah with zā is wrong. *uz-ah-āp 'spring' is unattested. us-spar is unattested, and the modern derivation of NP sipurdan 'entrust' is *upa-spar- (MP abespārdan), not *us-spar- (Cheung 351; MacKenzie p.3). The us-/uz- preverb and *us-tavah- stand; us-spar and the 'give birth' sense of uz-ah are disputed.\",\n          \"derivation_fa\": \"پیشوند اوستایی us-/uz- از هندواروپایی *ud(s)- است (پوکورنی، کنت). اما ud- صورت پارسی باستان و سنسکریت است، نه اوستایی. *us-tavah- «بی‌توان» در اوستا گواهی نشده ولی نیبرگ آن را ریشهٔ «ستوه» می‌داند و پذیرفتنی است. ni-us-tavah ساختهٔ خود نورایی است، چون «نستوه» همان نَ- + ستوه است. uz-ah- در اوستا هست (از ah- «انداختن»، بارتولومه، چونگ)، ولی معنای «بیرون افکندن» دارد نه «زاییدن». zā- «زادن» از ریشهٔ دیگر *zan- است. us-spar هم گواهی ندارد و پژوهش امروزی «سپردن» را از *upa-spar- می‌داند. پس این بخش از ادعای نورایی رد می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/úd\",\n            \"https://en.wiktionary.org/wiki/سپردن\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1103\", \"status\": \"supports\", \"note\": \"POK_full.txt l.93520: 'Avestan us-, uz- (*uds-) ds.' — supports the preverb only; Pokorny has none of the compounds.\"},\n            {\"ref\": \"HRN:154\", \"status\": \"partial\", \"note\": \"Horn p.154 (HRN.txt leaf 175) no. 697 'supārden \\\"anvertrauen, übergeben\\\" ... aw. us- + 2. √par-; phlv. avspārtan, avspurtan ... ai. ud + √par- \\\"hinüberführen\\\" ... Die Etymologie stammt von de Lagarde, ist aber sehr unsicher.' This is the source of Nourai's us-spar, and Horn calls it very uncertain.\"},\n            {\"ref\": \"BQT:1049\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaves 508-511 (printed ~1046-1049; offset leaf+538 inferred from sotuh/separdan): زه 'زاییدن آدمی و حیوانات ... بچه و فرزند'; footnote 'زهدان: از زه (ه.م.) + دان'; 'زهیدن: از زه + یدن (پسوند مصدری)'. OCR is rough and no uz-ah derivation is legible.\"},\n            {\"ref\": \"DZA:57\", \"status\": \"not_checked\", \"note\": \"Rashed Mohassel's Avestan grammar is not digitised (refs_online.json).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"s.v. ah- 'werfen' (BRT.txt l.6721); s.v. paiti.tavah- (l.14944)\", \"stance\": \"partial\", \"note\": \"'ah- V. \\\"werfen\\\" ... mit us \\\"hinaus-, hinaufschicken\\\": pairikā .. yā uzāŋhat aŋrō mainyuš Yt 8.39' — uz-ah exists but means 'send/throw out', not 'give birth'; 'paiti.tavah- Adj. \\\"seine Kraft dagegen einsetzend\\\"' shows the s-stem tavah- 'strength'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"pp. 152, 351 s.v. *Hah2, *spar\", \"stance\": \"contradicts\", \"note\": \"'*Hah2 \\\"to throw\\\" AVESTAN: ah- \\\"to throw\\\" || (+ *uz-) \\\"to throw out on\\\"'; '*spar \\\"to hand over, entrust\\\" ... (+ *upa-) BMP abespar- ... NWIR: NP sipār-/sipurdan' — entrust verb with *upa-, not *us-.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. stōh (NYB_vol2_glossary.txt l.3544)\", \"stance\": \"supports\", \"note\": \"'stoh, stuh, NP sutūh ... I derive it from *us-tavah- \\\"out of force, powerless\\\", from Av. tavah-' — supports us-tavah.\"},\n            {\"src\": \"KNT\", \"where\": \"p. 176 s.v. ud\", \"stance\": \"partial\", \"note\": \"'becoming Iran. us- uz- before dentals: Av. us- uz-' — Avestan has us-/uz-, not ud-.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"sotŭh; nastŭh; sepârdan; zeh 2; zehdân; zahâb\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"sotuh 'weary, exhausted' < MP stōh/stōb (Paz. stoh) < *us-tavah- 'out of strength' (Nyberg; Mo'in in BQT). The OIr. -avah- > MP -ōh, and the initial u- of us- is lost, as in stōr, stūn. Confirmed. nastuh 'untiring' = negative na- + sotuh (Ferdowsi: 'jahân kard bar div-e nastuh tang'). Confirmed. sepârdan/sepordan 'entrust' < MP abespārdan/abespurdan < *upa-spar- 'hand over' (MacKenzie p.3, Cheung 351, Mo'in: 'مخفف اسپاردن'), with no us- prefix. Disputed. zah/zahidan 'give birth' is better taken with zādan/zāy- < *zan- (Wiktionary; Farahvashi glosses zah 'زاینده'), not *uz-ah- 'throw out'. Disputed. zahdân 'womb' = zah + -dân (place suffix; Mo'in, Wiktionary): the formation is right but inherits the problem with zah. zahâb 'spring' < MP zahābag 'spring, source' (MacKenzie) = zah 'seepage, issue' + āb 'water'. The ultimate origin of zah 'spring' is open, so Nourai's uz- + ah- 'come out' is possible but unproven. Worst verdict: disputed (sepârdan, zeh 'give birth').\",\n          \"derivation_fa\": \"«ستوه» از فارسی میانهٔ stōh/stōb و از ایرانی باستان *us-tavah- «بیرون از توان» است. -avah- در فارسی میانه به -ōh رسیده و u- آغازی افتاده است (نیبرگ، معین). «نستوه» نَ- + ستوه است، چنانکه در بیت فردوسی آمده. این دو درست‌اند. «سپاردن/سپردن» به گفتهٔ مکنزی، چونگ و خودِ معین («مخفف اسپاردن») از فارسی میانهٔ abespārdan و ایرانی باستان *upa-spar- است، نه *us-spar-. «زه/زهیدن» به معنی زاییدن را امروز از ریشهٔ *zan- «زادن» می‌دانند. «زهدان» = زه + ـدان. «زهاب» از فارسی میانهٔ zahābag «چشمه» است (زه + آب) و ریشهٔ «زه» در آن روشن نیست. پس بخشی از ادعای نورایی درست و بخشی رد می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/سپردن\",\n            \"https://en.wiktionary.org/wiki/نستوه\",\n            \"https://en.wiktionary.org/wiki/زه\",\n            \"https://en.wiktionary.org/wiki/زهدان\",\n            \"https://vajehyab.com/moein/ستوه\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1102\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 564 (l.33781-33801), Mo'in's footnote to ستوه: 'پهلوی ... (بی‌زور) ... ایرانی باستان ... از tav- (توانستن، قادر بودن) ... ستوه فارسی مرکب است از ... (آنکه زورش کم است) ... ضد آن: نستوه (خستگی‌ناپذیر)' — the *us-tavah analysis.\"},\n            {\"ref\": \"BQT:1086\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaf 548 (l.32680): 'سپاردن - مخفف اسپاردن (ه.م.)؛ پهلوی ... [رك: سپردن] ... ارمنی ... (تسلیم کردم، واگذار کردم)' — Mo'in derives it from (a)spārdan, the *upa- form, not us-.\"},\n            {\"ref\": \"BQT:1049\", \"status\": \"partial\", \"note\": \"leaf 509-511: 'زهدان: از زه (ه.م.) + دان'; 'زهیدن: از زه + یدن'; no uz-ah etymology legible in the OCR.\"},\n            {\"ref\": \"IRN:108\", \"status\": \"partial\", \"note\": \"ref_page.py IRN:108 (pdf p.119): 'زاب ... در اصل ترکیب شده است از واژه‌های «زه» و «آب» ... زهاب ... زه به معنی زاینده است از ریشهٔ zā به معنی زاییدن' — supports zah+āb but derives zah from zā- 'bear', not uz-ah.\"},\n            {\"ref\": \"MON:1763\", \"status\": \"not_checked\", \"note\": \"Print page of Farhang-e Mo'in cannot be mapped; the online Mo'in (vajehyab) gives ستوه '[په.] نک استوه' (Pahlavi origin) only.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"p.154 no. 697 supārden\", \"stance\": \"partial\", \"note\": \"'aw. us- + 2. √par- ... Die Etymologie stammt von de Lagarde, ist aber sehr unsicher.'\"},\n            {\"src\": \"HUB\", \"where\": \"p.143 §313 (HUB.txt l.4994-6292)\", \"stance\": \"partial\", \"note\": \"'sutuh = sutōh \\\"fatigatus, torpidus, tristis\\\"'; 'supurdan \\\"anvertrauen\\\" H. 697' — confirms the forms; no etymology of sutuh given.\"},\n            {\"src\": \"PHD\", \"where\": \"pp. 3, 97 s.vv. abespurdan, zahābag, zahag\", \"stance\": \"contradicts\", \"note\": \"'abespurdan, abespār- ... N sipurdan, sipār- commit, entrust, consign' (*upa-spar); 'zahābag ... N zahāb spring, source'; 'zahag ... N zah child, offspring'.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. stōh\", \"stance\": \"supports\", \"note\": \"'Paz. stoh, stuh, NP sutūh ... I derive it from *us-tavah- \\\"out of force, powerless\\\"'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p.351 *spar\", \"stance\": \"contradicts\", \"note\": \"'NP sipār-/sipurdan ... \\\"to hand over, entrust to\\\"' listed under *spar (+ *upa- in MP abespar-), with no *us-/*uz-.\"},\n            {\"src\": \"ARY\", \"where\": \"pdf p.339 (printed 340) s.v. سپاردن، اسپاردن، سپردن\", \"stance\": \"contradicts\", \"note\": \"Aryanpur files سپاردن under the PIE root with English 'spare' (i.e. *sper-), citing Borhan; no ud-.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan\",\n          \"words\": \"us-tema; usča\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. ustəma- 'outermost, last' is the superlative of us- (*ud-tm̥mo-), matching Skt. uttama- 'highest' (POK 1104). Av. usča (uscā) 'upward, above' = us- + the directional suffix -ča (*ud-kʷe), the same formation as Skt. uccā 'aloft' (Wackernagel-Debrunner, cited by Pokorny). Both forms and glosses are correct.\",\n          \"derivation_fa\": \"اوستایی ustəma- «بیرونی‌ترین، واپسین» صفت عالی از us- است (*ud-tm̥mo-) و با سنسکریت uttama- «برترین» هم‌ریشه است. اوستایی usča «به سوی بالا، بالا» از us- + پسوند -ča (*ud-kʷe) ساخته شده، مانند سنسکریت uccā. پوکورنی هر دو را آورده و ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/úd\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1104\", \"status\": \"supports\", \"note\": \"POK_full.txt l.93560: 'Sup. Old Indic uttama- \\\"höchster\\\", Avestan ustəma- \\\"äußerster, last\\\" ... Old Indic ucca- \\\"high\\\" (*ud-kʷe), uccā, Avestan usca Adv. \\\"above\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"s.v. usca (BRT.txt l.2959, 4248)\", \"stance\": \"supports\", \"note\": \"Passages 'raocå usca usraocayeiti' (V 2.40) show adv. usca 'aufwärts' with the us- preverb. The ustəma- entry is not findable in the noisy OCR.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.190 ud-\", \"stance\": \"partial\", \"note\": \"Entry ud- is found, but the OCR section on the comparative/superlative (uttara-, ustəma-) is illegible (grep 'uttara' finds nothing).\"},\n            {\"src\": \"AHD\", \"where\": \"s.v. ud-\", \"stance\": \"silent\", \"note\": \"Watkins lists only Germanic and Greek derivatives.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old Persian\",\n          \"words\": \"ud; ud-zma, uzma\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OP ud- 'up' appears unchanged before a vowel in ud-apatatā 'rose up (in rebellion)' (DB). OP uzma- 'stake' (only in uzmayā-patiy kar- 'to impale', DB 2.76 etc.) is analysed by Kent as *ud-zma- 'that which is up from the earth', from ud- + zma-, the zero grade of zam- 'earth', with total assimilation of d. Nourai's gloss 'grown up from ground' paraphrases this. Kent notes rival analyses (Wackernagel, Lommel, König), but his is the standard one.\",\n          \"derivation_fa\": \"پارسی باستان ud- «بالا» در ud-apatatā «برخاست، شورید» دیده می‌شود. uzma- «تیرِ دار» (در uzmayā-patiy kar- «بر دار کردن») را کنت از *ud-zma- «آنچه از زمین برافراشته است» می‌داند: ud- + zma- (صورت ضعیف zam- «زمین»)، که در آن d همگون شده است. ادعای نورایی درست است، هرچند معنای دقیق واژه «دار، چوبهٔ دار» است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"KNT:176\", \"status\": \"supports\", \"note\": \"KNT.txt l.5177 (p.176): 'ud prep. and prefix \\\"up\\\" ... u(z)- in uzma- (§84)'; l.5226 (p.177): 'uzma- adj. as sb. \\\"that which is up from the earth, stake\\\": from ud- \\\"up\\\" + zma- to zam- \\\"earth\\\" ... otherwise Wackernagel ... uzmayā-patiy DB 2.76'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Grammar §84 (KNT.txt l.1128)\", \"stance\": \"supports\", \"note\": \"'The prefix ud \\\"up\\\" ... appears unchanged before a vowel in ud-apatatā ... suffers complete assimilation of the d in uzma- \\\"stake\\\" (from *ud-zma-)'.\"},\n            {\"src\": \"POK\", \"where\": \"p.1103\", \"stance\": \"supports\", \"note\": \"'ap. us-, ud-' ... 'ud- in ud-apatatā \\\"lehnte sich auf, fiel ab\\\"'.\"},\n            {\"src\": \"BRT\", \"where\": \"uzmayā-patiy\", \"stance\": \"silent\", \"note\": \"Not found in the OCR (grep 'uzma' finds nothing).\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"ucca, učča\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Skt. uccá- 'high, lofty', with adv. uccā́ 'aloft' and uccaís 'loudly, high'. It is back-formed from the adverb uccā́ < PIE *úd-kʷeh₁ 'upwards' (ud- + -kʷe), with assimilation -dc- > -cc-. It is a regular Indo-Aryan reflex of *ud.\",\n          \"derivation_fa\": \"سنسکریت uccá- «بلند، بالا» از قید uccā́ «در بالا» ساخته شده که از هندواروپایی *úd-kʷeh₁ است. d پیش از c همگون شده و cc پدید آمده. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/उच्च\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1104\", \"status\": \"supports\", \"note\": \"'about Old Indic ucca- \\\"high\\\" (*ud-kʷe), uccā, Avestan usca Adv. \\\"above\\\" s. Wackernagel-Debrunner II 2, 545 f.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 189-190\", \"stance\": \"partial\", \"note\": \"The ud- entry is present, but the ucca- passage is not legible in the OCR.\"},\n            {\"src\": \"AHD\", \"where\": \"s.v. ud-\", \"stance\": \"silent\", \"note\": \"Watkins gives no Sanskrit.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. ud-\", \"stance\": \"silent\", \"note\": \"grep finds only udn 'out, outside' (Hitt. udne, OE ūtan); no ucca.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Arabic\",\n          \"words\": \"awja\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic awj 'height, summit; apogee (astronomy)' is a technical term of the Abbasid astronomers. It is not native Arabic: Mo'in marks Persian owj [معر.] and Wiktionary derives Arabic awj from Middle Persian *awg (NP owg). That Pahlavi astronomical term is in turn often linked (Nallino) to Skt. ucca 'apex of a planet's orbit', taken over with Indian astronomy in Sasanian times. Lokotsch says only that the Arabic word is 'possibly itself of foreign (Persian, Indian or Greek) origin', and Wiktionary instead suggests PIE *h₂ewg-. The Skt. ucca → (Pahlavi) → Arabic route is a defensible hypothesis but not settled, and the chart skips the Persian intermediary.\",\n          \"derivation_fa\": \"عربی «أوج» «بلندی؛ دورترین نقطهٔ مدار سیاره» اصطلاح نجومی است و عربی اصیل نیست. معین آن را معرّب می‌داند و ویکی‌واژه از فارسی میانهٔ *awg (اوگ). بسیاری آن اصطلاح پهلوی را برگرفته از سنسکریت ucca، از اصطلاحات نجوم هندی در دورهٔ ساسانی، دانسته‌اند. ولی لوکوچ تنها می‌گوید ممکن است ریشهٔ پارسی، هندی یا یونانی داشته باشد. پس سخن نورایی با احتیاط پذیرفتنی است، و حلقهٔ میانی پهلوی در نمودار نیامده.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/أوج\",\n            \"https://vajehyab.com/moein/اوج\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:399\", \"status\": \"not_checked\", \"note\": \"Print page of Farhang-e Mo'in not mappable; online Mo'in: 'اوج (اَ) [معر.] (اِ.) ۱- بلندی ... ۳- بالاترین درجهٔ ستاره' — marks it as an Arabicised foreign word, consistent with a non-Arabic origin.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 135 (LKT.txt l.525)\", \"stance\": \"partial\", \"note\": \"'Ar. auǧ: Höhe, Kulmination, Apogäum ... ins Romanische übergegangen: it. sp. kat. pg. auge ... Das ar. Grundwort ist möglicherweise selbst fremden [persischen, indischen oder griechischen] Ursprungs.'\"},\n            {\"src\": \"DEV\", \"where\": \"s.v. Auge (DEV.txt l.653)\", \"stance\": \"partial\", \"note\": \"'Auge. Terme d'astronomie ... apsides ... Esp. auge, ital. auge. De أوج aoudj, sommet, point culminant, que les astronomes arabes emploient' — no source for the Arabic word.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"owj\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP owj 'height, peak, zenith' was borrowed from Arabic awj in the Islamic period, with Arabic aw > Persian ow. Mo'in tags it [معر.], 'Arabicised'. If Arabic awj itself comes from MP *awg (NP owg), this is a Persian → Arabic → Persian round trip: Pahlavi -g was rendered by Arabic -j, and Persian re-borrowed the Arabicised form.\",\n          \"derivation_fa\": \"«اوج» فارسی از عربی «أوج» به معنی بلندی و اوج وام گرفته شده. معین آن را «معرّب» نشان کرده است. اگر عربی خود از پهلوی *awg (اوگ) باشد، این واژه رفت‌وبرگشتی است: فارسی ← عربی (گ به ج) ← فارسی. وام‌گیری از عربی درست است.\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/اوج\",\n            \"https://en.wiktionary.org/wiki/أوج\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:399\", \"status\": \"not_checked\", \"note\": \"Page not mappable; online Mo'in: 'اوج [معر.] بلندی ... بالاترین درجهٔ ستاره ... بلندترین حد آواز'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab online s.v. اوج\", \"stance\": \"supports\", \"note\": \"'[معر.]' — an Arabicised loan, which fits the Arabic → Persian arrow.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 135\", \"stance\": \"partial\", \"note\": \"Treats auǧ as an Arabic word 'possibly of Persian, Indian or Greek origin'; says nothing on NP owj.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Spanish\",\n          \"words\": \"auge\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sp. auge 'apogee; peak, height of fortune' (medieval astronomical Spanish, e.g. Alfonsine tables) < Arabic awj. The spelling with g (Arabic ǧ) was influenced by Latin augēre (Wiktionary). Lokotsch rejects a direct derivation from augere on phonetic grounds.\",\n          \"derivation_fa\": \"اسپانیایی auge «اوج، نقطهٔ اوج» در نجوم سده‌های میانه (جدول‌های آلفونسی) از عربی «أوج» وام گرفته شده. نوشتن آن با g زیر تأثیر لاتین augēre بوده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/auge\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SKT:357\", \"status\": \"supports\", \"note\": \"SKT.txt l.12701 (p.357 s.v. Ogee): '— Span. auge, highest point ... — Arab. auj, summit.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 135\", \"stance\": \"supports\", \"note\": \"'ins Romanische übergegangen: it. sp. kat. pg. auge ... Ableitung von lat. augere ... ist aus lautlichen Gründen abzulehnen.'\"},\n            {\"src\": \"DEV\", \"where\": \"s.v. Auge\", \"stance\": \"supports\", \"note\": \"'Esp. auge ... De أوج aoudj, sommet, point culminant'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"French\",\n          \"words\": \"ogive, ogee\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Old French ogive/augive (arc ogif, 13th c., the diagonal rib of a Gothic vault) is no longer derived from Spanish auge < Arabic awj. Skeat's 1911 view, which Nourai follows, explained it 'from the pointed top of Moorish arches'. Modern sources call it 'of uncertain origin' (Klein) or derive it from Vulgar Latin *augīvus / Late Latin augiva, from augēre 'to increase, strengthen' (Wiktionary; cf. Late Latin ogis 'support'). The architectural sense (vault rib, not 'apex') and the 13th-century northern French attestation also argue against a Spanish astronomical term. 'ogee' is the English form, not a French word.\",\n          \"derivation_fa\": \"فرانسوی کهن ogive/augive (رگهٔ چلیپایی طاق گوتیک، سدهٔ ۱۳) را امروز دیگر از اسپانیایی auge و عربی «اوج» نمی‌دانند. این نظر اسکیت (۱۹۱۱) بود که نورایی از او گرفته است. کلاین ریشه را «نامعلوم» می‌داند و ویکی‌واژه آن را از لاتین عامیانهٔ *augīvus، از augēre «افزودن، استوار کردن» می‌داند. معنای معماری واژه و پیدایش آن در شمال فرانسه هم با اصطلاح نجومی اسپانیایی نمی‌خواند. ogee هم صورت انگلیسی است نه فرانسوی. پژوهش امروزی ادعای نورایی را نمی‌پذیرد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ogive\",\n            \"https://en.wiktionary.org/wiki/ogee\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SKT:357\", \"status\": \"supports\", \"note\": \"SKT.txt l.12701: 'O.F. augive, ogive, an ogive or ogee (Cot.) — Span. auge, highest point; from the pointed top of Moorish arches, which have doubly-curved sides. — Arab. auj, summit.' Skeat says exactly what the arrow says, but the view is outdated.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. ogive (KLN_1966.txt l.26151)\", \"stance\": \"contradicts\", \"note\": \"'ogive ... F. ogive, earlier also spelled augive; of uncertain origin. Cp. ogee.'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 135\", \"stance\": \"silent\", \"note\": \"Lists Romance auge 'Apsiden' from Arabic auǧ but does not mention ogive.\"},\n            {\"src\": \"DEV\", \"where\": \"grep 'ogive'\", \"stance\": \"silent\", \"note\": \"Devic has no ogive entry, i.e. does not count it among French words of Oriental origin.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"ogee, ogive\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English ogive (late ME ogif, egeve) and its doublet ogee (shortened from ogive, 16th-17th c.; Minsheu 'an ogiue or ogee') come from Old French ogive/augive. The English sense 'S-shaped, double-curved molding/arch' developed in English. This French → English step is correct. The ultimate Spanish/Arabic origin claimed upstream is disputed (see node #9).\",\n          \"derivation_fa\": \"انگلیسی ogive (انگلیسی میانهٔ ogif، egeve) و صورت دوگانه‌اش ogee از فرانسوی کهن ogive/augive وام گرفته شده‌اند. معنای «قوس یا ابزار S‌شکل» در خود انگلیسی پدید آمد. گام فرانسوی ← انگلیسی درست است، ولی ریشهٔ اسپانیایی و عربی که نورایی در بالاتر آورده پذیرفته نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ogee\",\n            \"https://en.wiktionary.org/wiki/ogive\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SKT:357\", \"status\": \"supports\", \"note\": \"'Ogee, Ogive, a double curve (F. — Span. — Arab.) \\\"An ogiue or ogee, a wreath, circlet, or round band in architecture\\\", Minsheu.'\"},\n            {\"ref\": \"TYL:568\", \"status\": \"not_checked\", \"note\": \"Taylor's 'Arabic Words in English' (S.P.E. Tract XXXVIII) is not on disk; HathiTrust is browser-only.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. ogee\", \"stance\": \"supports\", \"note\": \"'ogee, n., 1) a molding having an S-shaped curve ... — F. ogive. See ogive' — the F → E step holds; for ogive itself Klein says 'of uncertain origin'.\"},\n            {\"src\": \"SKT\", \"where\": \"p.580 list of French-from-Spanish-from-Arabic words (SKT.txt l.23699)\", \"stance\": \"supports\", \"note\": \"Lists 'ogee (ogive)' among words that are 'French from Spanish from Arabic' — Skeat's own (outdated) classification.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Germanic\",\n          \"words\": \"ŭt\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *ūt 'out' < PIE *ud with lengthened grade (*ūd), Grimm's law d > t. Reflexes are Gothic ūt, Old Norse út, Old English ūt, Old High German ūz (> German aus). Extended *uds gives Germanic *uz- (Gothic us-, German er-/ur-).\",\n          \"derivation_fa\": \"ژرمنی آغازین *ūt «بیرون» از هندواروپایی *ud (با واکهٔ کشیده *ūd) است. d بنا بر قانون گریم به t بدل شده. بازمانده‌هایش گوتی ūt، نوردی کهن út، انگلیسی کهن ūt و آلمانی aus است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/úd\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.1102: 'ud- ... 1. Germanic *ūt, out, in: a. Old English ūt, OUT ...'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p.1103\", \"stance\": \"supports\", \"note\": \"'Gothic ūt Adv. \\\"out, heraus\\\". Old High German ūz ... Old Saxon Old English ūt'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.190\", \"stance\": \"supports\", \"note\": \"'Got. ūt Adv. „hinaus, heraus“, ahd. ūʒ, nhd. aus, as. ags. ūt'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. udn\", \"stance\": \"supports\", \"note\": \"'udn (ūd-ono) \\\"out, outside\\\" ... OE ūtan(e) \\\"from outside\\\"; ON útan'.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"out, but, about\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"out < OE ūt (ME out by the Great Vowel Shift ū > /aʊ/). but < OE būtan 'outside, without, except' < West Germanic *bi-ūtana 'at the outside' (bi 'by' + ūtana). about < OE onbūtan 'on the outside of' (on + be + ūtan). All three contain Germanic *ūt.\",\n          \"derivation_fa\": \"out از انگلیسی کهن ūt است و ū در جابه‌جایی بزرگ واکه‌ها به /aʊ/ بدل شد. but از انگلیسی کهن būtan «بیرون از، جز» و از ژرمنی غربی *bi-ūtana «در بیرون» است. about از انگلیسی کهن onbūtan «بر بیرونِ». هر سه از ژرمنی *ūt‌اند و ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"No reference is cited on this node; checked against AHD (the parent's reference) instead.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"s.v. ud-\", \"stance\": \"supports\", \"note\": \"'g. Germanic compound *bi-ūtana (*bi-, by, at ...) \\\"at the outside,\\\" in Old English būtan, būte, outside (adverb): BUT; ABOUT.'\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Out (SKT.txt l.12930)\", \"stance\": \"supports\", \"note\": \"'Out, without, abroad. (E.) M.E. ut, ute, adv. A.S. ūt, ūtan ... Icel. út, G. aus, Goth. ut ... Skt. ud, up, out.'\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Greek\",\n          \"words\": \"hus-teros\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek hústeros 'latter, later, behind' < PIE comparative *ud-tero-, with -dt- > -st- and initial u- aspirated to hu-. It is cognate with Skt. úttara- 'upper, later' (Pokorny; Watkins).\",\n          \"derivation_fa\": \"یونانی باستان hústeros «پسین، دیرتر» از صفت تفضیلی هندواروپایی *ud-tero- است. -dt- به -st- بدل شده و u- آغازی دمیده (hu-) شده. با سنسکریت úttara- «بالاتر، پسین» هم‌ریشه است و ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/hysteresis\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"'3. Suffixed (comparative) form *ud-tero- in Greek husteros, later, second, after: HYSTERESIS, HYSTERON PROTERON.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p.1104\", \"stance\": \"supports\", \"note\": \"'2. Kompar. Old Indic uttara- \\\"the höhere, obere, spätere\\\" = gr. hysteros \\\"the spätere\\\"; ... gr. hystatos \\\"last\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. hysteresis\", \"stance\": \"supports\", \"note\": \"'Gk. hysterēsis \\\"shortcoming, deficiency\\\", fr. hysterein \\\"to be behind, come late, lag\\\", fr. hysteron \\\"later\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"English\",\n          \"words\": \"hysteresis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English hysteresis was coined in 1881 by the physicist J. A. Ewing for the lag of magnetisation behind the magnetising force. It comes from Greek hystérēsis 'a coming short, deficiency', from hysteréō 'to be late, fall short', from hústeros 'later'.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی hysteresis را فیزیک‌دان اسکاتلندی جیمز یوینگ در ۱۸۸۱ برای «پس‌ماند مغناطیسی» ساخت. از یونانی hystérēsis «کوتاهی، عقب‌ماندن»، از hysteréō «دیر رسیدن» و hústeros «پسین» است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/hysteresis\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"No reference is cited on this node; AHD (on the parent node) names HYSTERESIS explicitly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. hysteresis (KLN_1966.txt l.18547)\", \"stance\": \"supports\", \"note\": \"'hysteresis, n., the lagging in the magnetic force behind the magnetizing force — Gk. hysterēsis ... fr. hysteron \\\"later\\\".'\"},\n            {\"src\": \"AHD\", \"where\": \"s.v. ud-\", \"stance\": \"supports\", \"note\": \"'*ud-tero- in Greek husteros ... HYSTERESIS'.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-15T02:51:07.365Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-516.json (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:51:12.637Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; sed -i 's/والde-پوکورنی/والده-پوکورنی/; s/\"pp\\. 3, 97 s\\.vv\\. abespurdan, zahābag, zahag\"/\"p. 3 s.v. abespurdan; s.vv. zahābag, zahag (PHD.txt l.166, 673)\"/; s/\"p\\.580 list of French-from-Spanish-from-Arabic words (SKT\\.txt l\\.23699)\"/\"appendix list of French-from-Spanish-from-Arabic words (SKT.txt l.23699)\"/; s/POK_full.txt l.93560:/POK_full.txt l.93520ff:/' page-516.json; python3 -m json.tool page-516.json >/dev/null && echo OK; python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 516",
 "description": "Fix small errors, validate JSON, run check"
}
```


### [2026-10-15T02:51:13.398Z] TOOL RESULT

```
OK
nodes verified: 14/14
node verdicts: {'disputed': 3, 'confirmed': 10, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 10, 'partial': 5, 'not_checked': 7}
books consulted: {'partial': 9, 'contradicts': 5, 'supports': 19, 'silent': 6} | by book: {'AHD': 4, 'LKT': 4, 'KLN': 4, 'BRT': 3, 'WLD': 3, 'POK': 3, 'DEV': 3, 'CHEUNG': 2, 'NYB': 2, 'KNT': 2, 'IEC': 2, 'SKT': 2, 'HRN': 1, 'HUB': 1, 'PHD': 1, 'ARY': 1, 'MON': 1}
```


## [2026-10-15T02:51:21.501Z] TOOL CALL #68: SubagentHandback

```json
{
 "message": "PDF page 516 (book page 486) is verified. I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-516.json`, and `python3 tools/verify_check.py 516` reports 14/14 nodes and 0 PROBLEM lines.\n\nThere is one entry, Ud 1; I skipped Ud 2 because it only redirects to Wed.\n\n- **Root:** confirmed. PIE *ud \"up, out\" matches Pokorny 1103–1104, Walde-Pokorny I 189–190 and Watkins.\n- **Nodes:** 10 confirmed, 1 plausible, 3 disputed, 0 transcription_suspect.\n- **Plausible, #6 Arabic awj:** this is generally treated as a loan from Middle Persian *awg (Mo'in marks it as Arabicised). The step back to Sanskrit ucca is a hypothesis, and the chart leaves out the Persian link in between.\n\n**Disputed:**\n- **#1 Avestan us-spar and uz-ah \"give birth\":** neither is attested in those meanings. uz-ah- exists, but it means \"throw/send out\" (Bartholomae, Cheung). The us-/uz- prefix itself and *us-tavah- (Nyberg) hold up.\n- **#2 Persian sepârdan and zeh \"give birth\":**\n  - sepârdan comes from Middle Persian abespārdan < *upa-spar- (MacKenzie, Cheung, and Mo'in's own footnote). Horn p.154, which Nourai cites, gives us- + par- but calls it \"sehr unsicher\".\n  - zah \"birth\" goes with *zan-/zā- \"to bear\", as Wiktionary and Farahvashi (IRN:108) have it.\n  - sotuh and nastuh < *us-tavah- are confirmed by Nyberg and Mo'in (BQT:1102).\n- **#9 French ogive < Spanish auge < Arabic awj:** this is Skeat's 1911 view. Klein says \"of uncertain origin\" and Wiktionary derives it from Latin augere. The French → English step at #10 is confirmed.\n\n**Extraction errors:** none; the JSON matches the printed page.\n\nThese cited references could not be checked: DZA:57, MON:1763, MON:399 (I used the online Mo'in instead) and TYL:568. All 13 web sources are archived with `fetch_source.py`."
}
```


### [2026-10-15T02:51:21.784Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
