# Verification process log — verify-page-538


## [2026-10-16T05:13:02.195Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 538 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-538.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-538.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-538.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 538` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:02.247Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:07.084Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:07.153Z] TOOL RESULT

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


## [2026-10-16T05:13:07.463Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-538.txt"
}
```


### [2026-10-16T05:13:07.478Z] TOOL RESULT

```
1	=== PDF page 538 (book page 508) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wekw, Weqw : voice, to speak  (refs POK:1135)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:1135 | vak, vačah, vaxš 1 : word, voice, sound
5	  #2 (parent #1) [Persian] refs=BQT:204,218,2260; FSF:64; ZMA:28 | vâk «واک» : sound ; vâžeh «واژه» : word ; vâžgân «واژگان» : any word (original or borrowed) used in a language ; vâž «واژ ، باژ ۳ ، باج ۲» : quietly said prayers
6	#3 (parent #0) [Avestan / Old Persian] refs=POK:1135; KLN:1719; SYN:26 | â-vač : voice, song ; fra-vaxš : call out, sell ☞Per 1 ; paurvatâ-vac : mountain voice, echo ☞Parvan ; vi-vačah : to speak out ironically ☞Wi
7	  #4 (parent #3) [Persian] refs=BQT:401,1473,2260; HRN:263 | âvâ «آوا ( آواز )» : voice, song ; forŭxtan «فروختن» : to sell ; pažvâk «پژواک» : echo ; govâžeh «گواژه ( گواژیدن )» : blame, sarcasm
8	#5 (parent #0) [Avestan] refs=HRN:241 | vaxš-ô-bara : voice carrier ☞Bher 1
9	  #6 (parent #5) [Pahlavi] refs=MON:4992 | vaxš-war : messenger
10	    #7 (parent #6) [Persian] refs=MON:4992; BQT:2260; HRN:241; VSF:17 | vaxšŭr «وَخشور» : prophet, Zoroaster
11	#8 (parent #0) [Avestan] refs=BQT:2174 | ni-vak : sound, music ; hu-ni-vak : good sound ☞Su 1
12	  #9 (parent #8) [Persian] refs=BQT:2174,2178 | navâ «نوا» : sound, melody ; xonyâ «خنیا ( خنیاگر )» : melody, music | extra: نوازیدن ، نواختن ، نوازش ، نوازشگر
13	#10 (parent #0) [Old Persian] refs=ETM:61 | wâk : to speak ; wânk : call, called
14	  #11 (parent #10) [Pahlavi] refs=BQT:229 | vang : call, loud sound, crying
15	    #12 (parent #11) [Persian] refs=ETM:61; BQT:229 | vang 2 «وَنگ ۲» : call, crying ; bâng «بانگ» : call, loud sound
16	#13 (parent #0) [Avestan / Old Persian] refs=ETM:72 | ux : word ; hu-ux-tay : good words ☞Su 1
17	  #14 (parent #13) [Persian] refs=ETM:72; BQT:2388 | hŭxt «هوخت ( هوخ ، هوخست )» : good words, prayer, prayer house
18	#15 (parent #0) [Latin] refs=AHD | vox, voc : voice ; vocâre : to call
19	  #16 (parent #15) [English] refs=None | voice, vocabulary
20	
```


## [2026-10-16T05:13:08.192Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-538.json"
}
```


### [2026-10-16T05:13:08.269Z] TOOL RESULT

```
1	{
2	  "pdf_page": 538,
3	  "book_page": 508,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wekw, Weqw",
8	        "lang": "Indo-European",
9	        "refs": "POK:1135",
10	        "gloss": "voice, to speak"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan / Old Persian",
17	          "refs": "POK:1135",
18	          "words": [
19	            {"translit": "vak, vačah, vaxš 1", "gloss": "word, voice, sound", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Persian",
28	          "refs": "BQT:204,218,2260; FSF:64; ZMA:28",
29	          "words": [
30	            {"translit": "vâk", "gloss": "sound", "script": "واک"},
31	            {"translit": "vâžeh", "gloss": "word", "script": "واژه"},
32	            {"translit": "vâžgân", "gloss": "any word (original or borrowed) used in a language", "script": "واژگان"},
33	            {"translit": "vâž", "gloss": "quietly said prayers", "script": "واژ ، باژ ۳ ، باج ۲"}
34	          ],
35	          "note": null,
36	          "quote": {"text": "پرستندهٔ آذر زردهشت - همی رفت با باژ و بَرسَم بمشت", "poet": "Ferdowsî"}
37	        },
38	        {
39	          "id": 3,
40	          "parent": 0,
41	          "lang": "Avestan / Old Persian",
42	          "refs": "POK:1135; KLN:1719; SYN:26",
43	          "words": [
44	            {"translit": "â-vač", "gloss": "voice, song", "script": null},
45	            {"translit": "fra-vaxš", "gloss": "call out, sell", "script": null, "see": ["Per 1"]},
46	            {"translit": "paurvatâ-vac", "gloss": "mountain voice, echo", "script": null, "see": ["Parvan"]},
47	            {"translit": "vi-vačah", "gloss": "to speak out ironically", "script": null, "see": ["Wi"]}
48	          ],
49	          "note": null,
50	          "quote": null
51	        },
52	        {
53	          "id": 4,
54	          "parent": 3,
55	          "lang": "Persian",
56	          "refs": "BQT:401,1473,2260; HRN:263",
57	          "words": [
58	            {"translit": "âvâ", "gloss": "voice, song", "script": "آوا ( آواز )"},
59	            {"translit": "forŭxtan", "gloss": "to sell", "script": "فروختن"},
60	            {"translit": "pažvâk", "gloss": "echo", "script": "پژواک"},
61	            {"translit": "govâžeh", "gloss": "blame, sarcasm", "script": "گواژه ( گواژیدن )"}
62	          ],
63	          "note": null,
64	          "quote": {"text": "گواژه همی زد پس او فرود - که این نامور پهلوان را چه بود", "poet": "Ferdowsî"}
65	        },
66	        {
67	          "id": 5,
68	          "parent": 0,
69	          "lang": "Avestan",
70	          "refs": "HRN:241",
71	          "words": [
72	            {"translit": "vaxš-ô-bara", "gloss": "voice carrier", "script": null, "see": ["Bher 1"]}
73	          ],
74	          "note": null,
75	          "quote": null
76	        },
77	        {
78	          "id": 6,
79	          "parent": 5,
80	          "lang": "Pahlavi",
81	          "refs": "MON:4992",
82	          "words": [
83	            {"translit": "vaxš-war", "gloss": "messenger", "script": null}
84	          ],
85	          "note": null,
86	          "quote": null
87	        },
88	        {
89	          "id": 7,
90	          "parent": 6,
91	          "lang": "Persian",
92	          "refs": "MON:4992; BQT:2260; HRN:241; VSF:17",
93	          "words": [
94	            {"translit": "vaxšŭr", "gloss": "prophet, Zoroaster", "script": "وَخشور"}
95	          ],
96	          "note": null,
97	          "quote": {"text": "به گفتار وَخشور خود راه جوی - دل از تیرگیها بدین آب شوی", "poet": "Ferdowsî"}
98	        },
99	        {
100	          "id": 8,
101	          "parent": 0,
102	          "lang": "Avestan",
103	          "refs": "BQT:2174",
104	          "words": [
105	            {"translit": "ni-vak", "gloss": "sound, music", "script": null},
106	            {"translit": "hu-ni-vak", "gloss": "good sound", "script": null, "see": ["Su 1"]}
107	          ],
108	          "note": null,
109	          "quote": null
110	        },
111	        {
112	          "id": 9,
113	          "parent": 8,
114	          "lang": "Persian",
115	          "refs": "BQT:2174,2178",
116	          "words": [
117	            {"translit": "navâ", "gloss": "sound, melody", "script": "نوا"},
118	            {"translit": "xonyâ", "gloss": "melody, music", "script": "خنیا ( خنیاگر )"}
119	          ],
120	          "script_extra": "نوازیدن ، نواختن ، نوازش ، نوازشگر",
121	          "note": null,
122	          "quote": null
123	        },
124	        {
125	          "id": 10,
126	          "parent": 0,
127	          "lang": "Old Persian",
128	          "refs": "ETM:61",
129	          "words": [
130	            {"translit": "wâk", "gloss": "to speak", "script": null},
131	            {"translit": "wânk", "gloss": "call, called", "script": null}
132	          ],
133	          "note": null,
134	          "quote": null
135	        },
136	        {
137	          "id": 11,
138	          "parent": 10,
139	          "lang": "Pahlavi",
140	          "refs": "BQT:229",
141	          "words": [
142	            {"translit": "vang", "gloss": "call, loud sound, crying", "script": null}
143	          ],
144	          "note": null,
145	          "quote": null
146	        },
147	        {
148	          "id": 12,
149	          "parent": 11,
150	          "lang": "Persian",
151	          "refs": "ETM:61; BQT:229",
152	          "words": [
153	            {"translit": "vang 2", "gloss": "call, crying", "script": "وَنگ ۲"},
154	            {"translit": "bâng", "gloss": "call, loud sound", "script": "بانگ"}
155	          ],
156	          "note": null,
157	          "quote": null
158	        },
159	        {
160	          "id": 13,
161	          "parent": 0,
162	          "lang": "Avestan / Old Persian",
163	          "refs": "ETM:72",
164	          "words": [
165	            {"translit": "ux", "gloss": "word", "script": null},
166	            {"translit": "hu-ux-tay", "gloss": "good words", "script": null, "see": ["Su 1"]}
167	          ],
168	          "note": null,
169	          "quote": null
170	        },
171	        {
172	          "id": 14,
173	          "parent": 13,
174	          "lang": "Persian",
175	          "refs": "ETM:72; BQT:2388",
176	          "words": [
177	            {"translit": "hŭxt", "gloss": "good words, prayer, prayer house", "script": "هوخت ( هوخ ، هوخست )"}
178	          ],
179	          "note": null,
180	          "quote": null
181	        },
182	        {
183	          "id": 15,
184	          "parent": 0,
185	          "lang": "Latin",
186	          "refs": "AHD",
187	          "words": [
188	            {"translit": "vox, voc", "gloss": "voice", "script": null},
189	            {"translit": "vocâre", "gloss": "to call", "script": null}
190	          ],
191	          "note": null,
192	          "quote": null
193	        },
194	        {
195	          "id": 16,
196	          "parent": 15,
197	          "lang": "English",
198	          "refs": null,
199	          "words": [
200	            {"translit": "voice, vocabulary", "gloss": null, "script": null}
201	          ],
202	          "note": null,
203	          "quote": null
204	        }
205	      ]
206	    }
207	  ]
208	}
209	
```


## [2026-10-16T05:13:10.988Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; ls data/verification/page-5*.json | tail -5"
}
```


## [2026-10-16T05:13:11.377Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat tools/verify_check.py | head -150"
}
```


### [2026-10-16T05:13:11.696Z] TOOL RESULT

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


### [2026-10-16T05:13:11.706Z] TOOL RESULT

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
.rw-r--r--   40k sfmqrb 14 Oct 22:50  data/verification/page-514.json
.rw-r--r--   22k sfmqrb 14 Oct 22:47  data/verification/page-515.json
.rw-r--r--   36k sfmqrb 14 Oct 22:51  data/verification/page-516.json
.rw-r--r--   32k sfmqrb 14 Oct 22:48  data/verification/page-517.json
.rw-r--r--   20k sfmqrb 14 Oct 22:48  data/verification/page-518.json
```


## [2026-10-16T05:13:15.396Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','FSF','ZMA','KLN','SYN','HRN','MON','VSF','ETM','AHD']:\n  v=d.get(k); print(k, json.dumps(v,ensure_ascii=False)[:700] if v else None); print()\n\""
}
```


### [2026-10-16T05:13:15.819Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based lea

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset fr

ZMA {"title": "Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian, Bonyad-e Neyshabur 1374/1995", "kind": "purchase", "url": "https://www.gisoom.com / iketab.com listings (Balkh / Bonyad-e Neyshabur, in print)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only; no open or lending copy (grey PDF sites exist, not used)."}

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966:

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/de

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or g

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

VSF {"title": "K. Mehravand, Vazhe-sazi dar Zaban-e Farsi, Rasti 1349/1970", "kind": "none", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
```


## [2026-10-16T05:13:17.976Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','KLN','MON']:\n  print(k, json.dumps(d[k],ensure_ascii=False)[700:2500]); print()\n\""
}
```


### [2026-10-16T05:13:18.349Z] TOOL RESULT

```
POK f index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)", "local_files": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt"], "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"}

BQT om (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/

KLN  TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)", "local_files": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt"], "cites": "page number, continuous across the two volumes (1966–67)"}

MON abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"], "page_offset": null, "covers_etymology": true, "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/
```


## [2026-10-16T05:13:20.929Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-515.json'))\ne=d['entries'][0]; print(json.dumps({k:v for k,v in d.items() if k!='entries'})); print(json.dumps(e,ensure_ascii=False,indent=1)[:5000])\""
}
```


### [2026-10-16T05:13:21.446Z] TOOL RESULT

```
{"pdf_page": 515, "book_page": 485, "verified_by": "claude-opus-5.5", "verified_on": "2026-10-14"}
{
 "entry": 0,
 "root": "Twerk, Twrk",
 "verdict": "confirmed",
 "modern_form": "PIE *twerḱ- 'to cut, carve, trim' (Pokorny tu̯erk̂- 1102; LIV² 656 *tu̯erk̑- 'schnitzen, zurechtschneiden')",
 "note": "Pokorny 1102 tuerk- 'schneiden' (WP I 751) gives exactly Nourai's three branches: Av. θwarəs-, Skt. Tvaṣṭar (from *Tvarṣṭar) and 'probably' Gk. σάρξ with σαρκάζειν. Modern sources (LIV², Mallory-Adams, Beekes 2010, Wiktionary, Watkins) all keep the root and the Greek link. Root, language label and gloss correct. 'Twrk' is the zero grade *twr̥ḱ- (Watkins), not a different root; the redirect entry 1 is skipped.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *twerḱ- (درجهٔ صفر *twr̥ḱ-) به معنای «بریدن، تراشیدن» در پوکورنی (ص ۱۱۰۲، tuerk-)، والده-پوکورنی (ج ۱، ص ۷۵۱)، واتکینز و فرهنگ فعل‌های هندواروپایی (LIV) آمده است. بازمانده‌های آن اوستایی θwarəs- «بریدن، آفریدن»، نام ایزد ودایی Tvaṣṭṛ «سازنده» و یونانی σάρξ «گوشت» (در اصل «تکهٔ بریده») است که واژه‌های انگلیسی sarcasm و sarcoma از آن آمده‌اند. ادعای نورایی دربارهٔ ریشه، زبان و معنا درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/twerḱ-"
 ],
 "ref_check": [
  {
   "ref": "POK:1102",
   "status": "supports",
   "note": "POK_full.txt l.87790 \"Root / lemma: tuerk- / Meaning: to cut / Material: Avestan θwarəs- 'cut, clip, schnitzend gestalten', participle θwarštа-, θwōrəštar- 'creator, god, molder': Old Indic GN Tvaṣṭā (-ar-) from *Tvarṣṭar, in addition probably gr. σάρξ, -κός 'flesh' ... σαρκάζειν 'tear, sich auf die Lippen beißen, mock' ... References: WP. I 751 ... Page(s): 1102\""
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 751",
   "stance": "supports",
   "note": "WLD_Bd1_pages.txt l.71143 'tuerk- „schneiden\". Av. θwarəs- „schneiden\" (θwarəsaiti, Ptc. θwaršta-) ... gr. σάρξ, -κός „Fleisch\", pl. „Fleischstücke\" ... Zu σάρξ auch σαρκάζειν in allen, auch der Bed. „höhnen\"'"
  },
  {
   "src": "AHD",
   "where": "Watkins 1985 s.v. twerk-",
   "stance": "supports",
   "note": "AHD_watkins1985.txt l.1100 \"twerk-. To cut. Zero-grade form *twrk- in Greek sarx, flesh (< 'piece of meat'): SARCASM, SARCO-, (SARCOMA) ... [Pok. tuerk- 1102.]\""
  },
  {
   "src": "IEC",
   "where": "s.v. tuerK-",
   "stance": "partial",
   "note": "IEC.txt l.19432 \"tuerK- 'athwart, across; cross, transverse; crosscut, section'. Cf. WP I, 751 Av. (z-gde) θwarəs-, v. 'resect, cut off'; θwarəsa, m. 'section'\" -- Mann files the Avestan verb here but lists no Greek σάρξ and no Sanskrit Tvaṣṭar"
  },
  {
   "src": "SYN",
   "where": "4.13 FLESH",
   "stance": "supports",
   "note": "SYN.txt l.5351 (4.13 FLESH) \"2. Grk. σάρξ : Av. θwarəs- 'cut', with development as in Lat. caro. Walde-P. 1.751. Boisacq 854.\""
  }
 ],
 "nodes": [
  {
   "id": 1,
   "lang": "Avestan",
   "words": "thwares",
   "verdict": "confirmed",
   "derivation": "Avestan θwarəs- (Nourai's 'thwares') 'to cut, carve; fashion, create', present θwarəsaiti, ppp. θwaršta-, agent noun θwōrəštar- 'fashioner, creator'. It continues Proto-Iranian *θwarc- < Proto-Indo-Iranian *twarć- < PIE *twerḱ-: PIE *t before *w gives Iranian θ (as in θwąm 'thee' < *twām), and the palatal *ḱ gives Avestan s (satem treatment). Meaning 'cut' is primary, 'shape by carving > create' secondary.",
   "derivation_fa": "فعل اوستایی θwarəs- «بریدن، تراشیدن؛ شکل دادن، آفریدن» (با صفت مفعولی θwaršta- و نام‌کنندهٔ θwōrəštar- «سازنده، آفریدگار») از ایرانی باستان *θwarc- و هندوایرانی *twarć- و سرانجام از ریشهٔ هندواروپایی آغازین *twerḱ- «بریدن» است. در ایرانی، t پیش از w به θ دگرگون شده و ḱ کامی هندواروپایی (چنان‌که در زبان‌های ساتم) به s بدل شده است. بارتولومه و پوکورنی و ویکی‌واژه همگی همین را می‌گویند؛ ادعای نورایی درست است.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/twerḱ-"
   ],
   "ref_check": [
    {
     "ref": "POK:1102",
     "status": "supports",
     "note": "POK_full.txt l.87790 \"Root / lemma: tuerk- / Meaning: to cut / Material: Avestan θwarəs- 'cut, clip, schnitzend gestalten', participle θwarštа-, θwōrəštar- 'creator, god, molder': Old Indic GN Tvaṣṭā (-ar-) from *Tvarṣṭar, in addition probably gr. σάρξ, -κός 'flesh' ... σαρκάζειν 'tear, sich auf die Lippen beißen, mock' ... References: WP. I 751 ... Page(s): 1102\""
    }
   ],
   "consulted": [
    {
     "src": "BRT",
     "where": "col. 795-796",
     "stance": "supports",
     "note": "BRT.txt col. 795-796 (l.14392-14400) \"θwarəs- V. 'schneiden' ... 1) '(schnitzen sva.) schneidend gestalten, schaffen, hervorbringen' ... PPfP. θwaršta-\"; \"θwōrəštar- m. 'Bildner, Schöpfer'\" (Y. 29.6)"
    },
    {
     "src": "WLD",
     "where": "Bd. I 751",
     "stance": "supports",
     "note": "WLD_Bd1_pages.txt l.71143 'tuerk- „schneiden\". Av. θwarəs- „schneiden\" (θwarəsaiti, Ptc. θwaršta-) ... gr. σάρξ, -κός „Fleisch\", pl. „Fleischstücke\" ... Zu σάρξ auch σαρκάζειν in allen, auch der Bed. „höhnen\"'"
    },
    {
     "src": "IEC",
     "where": "p. s.v. tuerK-",
     "stance": "par
```


## [2026-10-16T05:13:24.944Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'lemma: wekʷ\\|lemma: u̯ekʷ\\|lemma: uek' POK_full.txt | head; grep -n -i '^ *u̯ekʷ\\|uek[ʷu]-\\|u̯eku̯' AHD_watkins1985.txt | head; grep -n '^wekw\\|^ *wekʷ' AHD_watkins1985.txt|head"
}
```


### [2026-10-16T05:13:25.330Z] TOOL RESULT

```
8170:common Armenian Celtic lllyrian * hue- > gw- > g-{see Root / lemma: uek"-: to speak]. 
90042:Root / lemma: uek-ti- 
90060:Root / lemma: uek-, ue-n-k-
```


## [2026-10-16T05:13:27.355Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'lemma: uek' POK_full.txt; grep -n -i 'speak' AHD_watkins1985.txt | head -20"
}
```


### [2026-10-16T05:13:27.666Z] TOOL RESULT

```
8170:common Armenian Celtic lllyrian * hue- > gw- > g-{see Root / lemma: uek"-: to speak]. 
90042:Root / lemma: uek-ti- 
90060:Root / lemma: uek-, ue-n-k- 
44:This dictionary is designed and written for the general English-speaking public and not, needless to say, for specialists in the field of Indo-European. With the indispensable and able assistance of Marion Severynse, the staff etymologist of The American Heritage Dictionary, I have tried to put some order into the presentation of a vast amount of linguistic information. I have also tried to introduce only as much technical background explanation as is required without burdening the reader with unnecessary detail. The amount in fact introduced may seem overmuch to some; but human language is not simple, and a part of the fascination of the study of human language lies in the recognition of its complexity.
48:Speaking to the Asiatick Society in Cal- cutta on February 2, 1786, the English orien- talist and jurist Sir William Jones uttered his famous pronouncement:
56:It should be pointed out that the Indo- European family is only one of many lan- guage families that have been identified around the world, comprising several thou- sand different languages. We have good rea- son, however, to be especially interested in the history of the Indo-European family. Our own language, English, is the most prevalent member of that family, being spoken as a native language by nearly 350 million people and being the most important second lan- guage in the world. The total number of speakers of all Indo-European languages amounts to approximately half the popula- tion of the earth.
60:But it must be stressed that linguistic heri- tage, while it may well tend to correspond with cultural continuity, does not imply ge- netic or biological descent. That is, there is no more reason to suppose that we, as speak- ers of an Indo-European language, are de- scended biologically from the speakers of Proto-Indo-European, than that the English- speaking population of Nigeria is Anglo- Saxon. The transmission of language by con- quest, assimilation, migration, or any other ethnic movement is a complex and enigmatic process which this discussion does not pro- pose to examine, beyond stating the general proposition that in the case of Indo- European no genetic conclusions can or should be drawn.
66:A number of Indo-European languages show a similar word for the kinship term “daughter-in-law”: Sanskrit snusd, Old Eng- lish snoru, Old Church Slavonic snikha (Russian snokhd), Latin nurus, Greek nuos, and Armenian nu. Albanian has nuse in the meaning “bride,” a meaning shared by the Armenian form. In a patrilocal and patriar- chal society (such as most, if not all, early Indo-European-speaking societies), where the bride went to live in her husband’s fa- ther’s house, “daughter-in-law” and “bride” were equivalents.
84:A characteristic feature of Indo-European was the system of vocalic alternations termed apophony or ablaut. This was a set of internal vowel changes expressing different morphological functions. A clear reflex of this feature is preserved in the English strong verbs, where, for example, the vocalic alter- nations between write and wrote, give and gave express the present and past tenses. Ablaut in Indo-European affected the vowels e and o. The fundamental form was e; this e could appear as o under certain conditions, and in other conditions both e and o could disappear entirely. On this basis we speak of given forms in Indo-European as exhibiting, respectively, the e-grade (or full grade), the o-grade, or the zero grade. The e and the o might furthermore occur as long é or 6, termed the lengthened grade.
108:Language is intimately linked to culture in a complex fashion; it is at once the expression of culture and a part of it. Especially the lexicon of a language—its dictionary—is a face turned toward culture. Though by no means a perfect mirror, the lexicon of a lan- guage remains the single most effective way of approaching and understanding the cul- ture of its speakers. As such, the contents of the Indo-European lexicon provide a remark- ably clear view of the whole culture of an otherwise unknown prehistoric society.
111:Consider the case of religion. To form an idea of the religion of a people, archaeologists proceed by inference, examining temples, sanctuaries, idols, votive objects, funerary offerings, and other material remains. But these may not be forthcoming; archaeology is, for example, of little or no utility in under- standing the religion of the ancient Hebrews. Yet of the Indo-European-speaking society we can reconstruct with certainty the word for “god,” *deiw-os, and the two-word name of the chief deity of the pantheon, *dyeu-pa- ter- (Latin Jupiter, Greek Zeus patér, San- skrit Dyaus pitar, and Luvian Tatis Tiwaz). The forms *dyeu- and *deiw-os are both de- rivatives of a root deiw-, meaning “to shine,” and appearing in the word for “day” in nu- merous languages (Latin diés; but English DAY is not related). The notion of deity was therefore linked to the notion of the bright sky.
113:The comparative method enables us to construct a basic vocabulary for the society of speakers of Proto-Indo-European that ex- tends to virtually all aspects of their culture. This basic vocabulary is, to be sure, not uni- form in its attestation. Most Indo-European words are found only in certain of the at- tested languages, not in all, which suggests that they may well have been formed only at a period later than the oldest common Indo- European we can reconstruct. There exist certain dialectal words that are limited in the area of their extension, as in the case of such an important sociological term as the word for tribe, teuta-, which is confined to the western branches Italic, Celtic, and Ger- manic. (It is the base of German Deutsch and of DUTCH and TEUTONIC.) In cases such as
128:Man and His Physical Environment. A large number of terms relating to time, weather, seasons, and natural surroundings can be reconstructed from the daughter lan- guages, some of which permit certain infer- ences about the homeland of the Indo-European-speaking people before the period of migrations took them to the differ- ent localities where they historically appear.
148:The names for a number of insects can be reconstructed in the protolanguage, includ- ing the wasP (wopsa), the hornet (*kras-ro-, a derivative of ker-', “head,” from the shape of the insect), and the fly (mu-2). The BEE (bhei-') was particularly important as the producer of honey, for which we have the common Indo-European name melit-. Honey was the only source of sugar and sweetness (swad-, “sweet,” is ancient), and notably was the base of the only certain Indo-European alcoholic beverage, MEAD, medhu-, meaning in different dialects both “mead” (“wine” in Greece) and “honey.” The Germanic lan- guages have innovated, perhaps from a taboo on speaking the name while gathering wild honey; the common Germanic English word HONEY is from an old color adjective for “yellow,” k(e)neko-.
165:Terms for the furrow are perk-? and selk-; wog”h-ni- designated the wedge-shaped plowshare. Other related roots are yeug-, “to yoke,” serp-', “sickle, hook,” and kerp-, “to gather, pluck” (HARVEST). The root g”ere-?, “heavy,” is the probable base of *g”ero-nd-, “hand mill” (QUERN). The term is found throughout the Indo-European-speaking world, including India.
166:Stockbreeding and animal husbandry were an important part of Indo-European eco- nomic life. The names for all the familiar domesticated animals are present throughout the family: gvou-, “cow and bull,” owi-, “sheep,” ag“h-no-, ‘lamb,’ aig- and ghaido-, “goat,” sd-, “swine,” and porko-, “farrow.” The domestic dog was ancient (kwon-); its name may underlie the common Indo-European word for horse, ekwo-. The expansion and migration of the Indo- European-speaking peoples in the later third and early second millennia B.c. is intimately bound up with the diffusion of the horse. The verbal root deme-?, “to force,” acquired the special sense of “‘to tame horses,” whence English TAME. Stock was a source and meas- ure of wealth; the original sense of peku- was probably “wealth, riches,” as in Latin pecu- nia, whence “wealth in cattle” and finally “cattle” proper. The same evolution from the general to the particular may be observed in the root neud-, “to make use of,” whence English NEAT?.
194:Archaeologists have not in fact succeeded in locating the Indo-Europeans. An artifact other than a written record is silent on the language of its user, and prehistoric Eurasia offers an abundant choice of culture areas. Archaeologists are generally agreed that the so-called Kurgan peoples, named after the Russian word for their characteristic “bar- row” or “tumulus” grave structure, spoke an Indo-European language. Some time around the middle of the fifth millennium B.c., these people expanded from the steppe zone north of the Black Sea and beyond the Volga into the Balkans and adjacent areas. These Kur- gan peoples bore a new mobile and aggressive culture into Neolithic Europe, and it is not unreasonable to associate them with the coming of the Indo-Europeans. But the Kur- gan peoples’ movement into Europe took place in distinct waves from the fifth to the third millennium B.c. The earliest so far discovered might be compatible with a rea- sonable date for Proto-Indo-European, that is, a date sufficiently long ago for a single language to develop into forms as divergent as Mycenean Greek and Hittite as they are historically attested by the middle of the second millennium B.c. But the later Kurgan immigrations after 4,000 B.c. are too late to be regarded as incursions of speakers of un- differentiated Proto-Indo-European. The archaeological evidence for the later waves of Kurgan migrations points to their having had an Indo-European culture, but the lan- guages spoken by the later Kurgan peoples must have been already differentiated Indo- European dialects, some of which would doubtless evolve into some of the historical branches of the family tree. We must be content to recognize the Kurgan peoples as speakers of certain Indo-European languages and as sharing a common Indo-European cultural patrimony. The ultimate “cradle” of the Indo-Europeans may well never be known, and language remains the best and fullest evidence for prehistoric Indo- European society.
207:Every boldface form appearing in the text of an entry is such a cross-reference. In the example pa- the form *pag- represents an older root form; the nature of these contrac- tions is explained in the preceding essay un- der ‘‘Phonology and Morphology.” The entries kak-? and mas are not strictly speak- ing Indo-European, since they are repre- sented in only one branch of the family. There is a relatively small number of such entries in this Dictionary; they are included because of the number of English words among their descendants. Boldface brackets are placed around these entries, and they are explicitly identified.
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
321:yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
323:outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
420:@g-. To speak. Suffixed zero-grade form “*ag-yo- in: a. Lat- in adagium, saying, proverb, “a speaking to” (ad-, to; see ad-): ADAGE; b. Latin prodigium, a portent, “a foretell- ing” (préd-, variant of pré-, before; see per'): PRODIGY. [Pok. @g- 290.]
492:TION), GENERIC, GENEROUS, GENRE, GENUS; CONGENER, (CONGENIAL), DEGENERATE, (ENGENDER), MISCEGENA- TION; b. Greek genos and genea, race, family: GENEAL- OGY, GENOCIDE, GENOTYPE, HETEROGENEOUS; c. Greek suffix -genés, ‘‘-born’”: -GEN, -GENY. 4. Suffixed full-grade form *gen-yo- in: a. Latin genius, procreative divinity, inborn tutelary spirit, innate quality: GENIAL!, GENIUS; b. Latin ingenium (in-, in; see en), inborn character: ENGINE, INGENIOUS. 5. Suffixed full-grade form *gen-d- in Latin indigena (indu-, within; see en), born in (a place), indigenous: INDIGEN, (INDIGENOUS). 6. Suffixed full-grade form *gena-wo- in Latin ingenuus (in-, in; see en), born in (a place), native, natural, freeborn: INGENUOUS. 7. Suffixed full-grade form *gen- men- dissimilated in Latin germen, shoot, bud, embryo, germ: GERM, GERMAN?, (GERMANE), GERMINAL, GERMI- NATE. 8. Suffixed full-grade form *gena-ti- in Greek genesis, birth, beginning: GENESIS, -GENESIS. 9. Redupli- cated form *gi-gn- in: a. Latin gignere (past participle genitus), to beget: GENITAL, GENITIVE, GENITOR, GENT!, (GINGERLY); CONGENITAL, PRIMOGENITURE, PROGENI- TOR, (PROGENY); b. Greek gignesthai, to be born: EPI- GENE. 10. Suffixed zero-grade form *-gn-o- in Latin benignus (bene, well; see deu-?), good-natured, kindly, and malignus (male, ill; see mel-5), evil-natured, malevo- lent: BENIGN, MALIGN. 11. Zero-grade form *gna- becom- ing *gnda- in Latin praegnds (prae-, before; see per’), pregnant: PREGNANT!. 12. Suffixed zero-grade form *gna-sko- becoming *gnd-sko- in Latin gndsci, ndsci (present participle ndscéns, past participle gndtus, nd- tus), to be born: NAIVE, NASCENT, NATAL, NATION, NA- TIVE, NATURE, NEE, NOEL; (ADNATE), AGNATE, COGNATE, CONNATE, ENATE, INNATE, NEONATE, PUISNE, (PUNY), RENAISSANCE. 13. Suffixed o-grade form *gon-o- in Greek gonos (combining form -gonos), child, procre- ation, seed: GONAD, GONO-; ARCHEGONIUM, EPIGONE. 14. Zero-grade form *gn- in Sanskrit ja- in krmi-ja-, “produced by worms” (see k*rmi-). [Pok. 1. gen- 373.] genu-'. Knee; also angle. 1. Variant form *gneu- in: a. Germanic *knewam in Old English cnéo, knee: KNEE; b. Germanic *knewljan in Old English cnéowlian, to kneel: KNEEL. 2. Basic form *genu- in Latin genii, knee: GENICULATE, GENUFLECT. 3. Suffixed variant form *gon-ya- in Greek gdnia, angle, corner: -GON, GONION; AMBLYGONITE, DIAGONAL, GONIOMETER, GONIOMETRY, ORTHOGONAL. [Pok. 1. genu- 380.] genu-2. Jawbone, chin. 1. Form *genw- in Germanic *kinnuz in Old English cin(n), chin: CHIN. 2. Basic form *genu- in Greek genus, chin: GENIAL. 3. Suffixed variant form *gna-dho- in Greek gnathos, jaw: GNATHIC, -GNATHOUS; CHAETOGNATH 4, Variant form “g(h)enu- in Sanskrit hanu, jaw: HANUMAN. [Pok. 2. genu- 381.] gep(h)-. Also gebh-. Jaw, mouth. 1. Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF!, 2. Germanic *kabraz, “gnawer,” in Old English ceafor, ceafer, beetle: CHAFER; (COCKCHAFER). 3. Ger- manic *kéfalaz in Old English céafl, jaw, cheek: JOWL!. [Pok. geph-, gebh- 382.] ger-'. To gather. 1. Extended form *grem- in Germanic *kram- in Old English crammian, to stuff, cram: CRAM. 2. Reduplicated form *gre-g- in Latin grex (stem greg-), herd, flock: GREGARIOUS; AGGREGATE, CONGREGATE, EGREGIOUS, SEGREGATE. 3. Earliest forms “ager-, *ggor-d-, in Greek ageirein, to assemble, and aguris, agora, marketplace (> agoreuein, to speak): AGORA}; (AGORAPHOBIA), ALLEGORY, CATEGORY, PANEGYRIC. [Pok. 1. ger- 382.] ger-2. Curving, crooked; hypothetical Indo-European base for a variety of Germanic words with initial kr-. I. Words meaning to bend, curl; bent, crooked, hooked; something bent or hooked. 1. Germanic *krdpp6n-, a hook, especially one used in harvesting grapes, in: a. Old High German krapfo, a hook: AGRAFFE; b. Old French graper, to harvest grapes, hence (back-formation) grape,
```


## [2026-10-16T05:13:31.946Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o -i 'wek[^.]\\{0,3\\}\\. To speak.\\{0,900\\}' AHD_watkins1985.txt | head -3; sed -n 90042,90120p POK_full.txt"
}
```


### [2026-10-16T05:13:32.615Z] TOOL RESULT

```
wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will po
Root / lemma: uek-ti- 
Meaning: thing 
Note: {uek'^-ti-1) 

Material: Gothic wafhtsi. "thing'. Old Icelandic vettr, vge(t)r, vitri. " living being, 
ijbermenschliches creature, thing'. Old English wihti. "thing, entity, demon'. Old Saxon 
wikt. Middle Low German tv/ic/?/ "entity, creature'. Old High German wiht^ living being, 
demon, thing'. Modern High German Wicht^ living creature, goblin, ugly mischievous sprite 
'; Gothic /7/-M/a/77/"nichts', Old English na-wiht {ev\i^\. naught, not) Old High German niwiht 
and neowiht^v\o{, nichts'; 

Old Church Slavic vestbi. " thing '; compare wruss. recb "thing': russ. recb " discourse, 
word'. 

References: WP. I 246, Vasmer 1, 196; 
See also: perhaps to uek'^- "speak'. 
Page(s):1136 

Root / lemma: uek-, ue-n-k- 
Meaning: to bend 



Material: Old Indie vancat/'geht. crooked or slant, skew', vacyate 'sch\N'\ng\. sich, flies', 
vakra- "gebogen, crooked', vank'u- "fliegend', vaiikri-i. " rib ', vaiika-, vankara- m. 
Tluftkrummung', va/iksana-m. " groin, flank', vaksana^beWy, groin, flank, riverbed '; 
Avestan -vasta- " writhed, crooked, humped '; common Old Indie -gh- > -ks- : Avestan -gh- 
> -xs- > -s- 
Armenian ^a/T^^r'crispus, flexus' {*unkuro)\ 

Latin convexus^ arched, writhed, crooked, humped ', 5^,6* i/ex^s "sch rag aufwarts 
fijhrend'; 

Middle Irish feccaid^bucVX sich', with the preposition for. 'wendet sich gegen, beginnt to' 
(with expressive -kk-)\ gall. FIN * Vocalus {Uaires Vocallinehae), germanisiert Vacalus, 
Va{c)ha//s ^VJaaV; Lithuanian FIN Vbke {* uokia); 

Indo Germanic uonko- in Old Indie vaiika-, Gothic i//>M/a/7s"untadelhaft', Old English 
14/0/7 'crooked, inverted ', Old Saxon wahn. " evil, wickedness ', Old Icelandic vai. 
( *uonkd) ' angle, mischief '. 

References: WP. I 246, WH. I 268 f.: after Kuiper, Nasalpras. 142 zur root t/a-(see above 
S. 1108), where besides dem present *ua-n-ek-mi e\v\ Konj. *u (9)-9n u-ko s\.av\&, 
consequently further zur root ua-, uag-, uak-, ueng(h)-, see there. 
Page(s): 1134-1135 

Root / lemma: ueR- 
Meaning: to wish 

Material: Old Indie vas-mi, vast/, us-masi, Avestan vasamT, usamahrwant, desire, will, 
wish', participle Old Indie usant-, f. ^sa/r willing', Avestan an-usant-, -i/5a///"'widerwillig, 
ohne es to want, desire, will', Avestan vasah- (Nom. vasa) 'wollend = after seinem Willen', 
vaso, i/asa 'after wish, beliebig' (Akk. Sg. of n. * vasah-), vaso-xsa^ra-^aiier QeiaWeu 
schaltend' etc.. Old Indie vasi-tva-v\. 'Willensfreiheit'; ap. vasna, Avestan i/as/75(lnstr. Sg.) 
'after dem Willen' (Armenian i/as/? 'because of loanword); 

gr. (previous participle) ekojv (Cretan Fskojv), SKOuaa 'freiwillig' (the Asper afters 'sich', 
as though 'from sich selbst heraus'), qekcjov, qkcjov 'wider Willen, ohne Vorsatz', f. Doric 
asKaaaa, compare Cretan ysKaGa SKOuaa Hes., Fskq in oucpsKa ouk apsaTux; Hes., i.e. ou 
Fekq, in £V£Ka, hom. sTvsKa 'because of (*£vF£Ka; £v is die preposition £v), hom. £Ka-£pYO(; 
'after Belieben wirkend', £Kr|-poAo(; 'after Belieben treffend' (metr. lengthening for *£Ka- 
(3oAo(;), out of it extended £KaTr|-p6Ao(;, -p£A£Tr|<;; Boeotian F/7£Ka-5a|JO(; (with versch. 



assimilation out of it thes. FsKsSapot;, Attic 'AKa5r||J0<;); £Kr|Ti, Doric skqti "after dem Willen, 
because of, (unclear)', asKa^opsvoc; 'not wollend, widerstrebend' (after avavKa^opEvoc;); 

Hittite uek- "wish, arrogate'. 

References: WP. I 244 f.. Frisk 473 f., 477, 479. 
Page(s):1135 

Root / lemma: ueic- {*huek"'-) 

Meaning: to speak 

Note:
```


## [2026-10-16T05:13:34.586Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90120,90175p POK_full.txt"
}
```


### [2026-10-16T05:13:35.326Z] TOOL RESULT

```
labialized old laryngeals {*hue-) 

Material: Old Indie vakti, vfvakti^ says, talks, speaks', Aor. avdcam{= sTnov, see below), 

participle ukta-, Kaus. vacayati, Avestan 1/5/r- "speak', uxta-. Old Indie vacas-v\. = Avestan 

vacah{= gr. luo(^) " discourse, word'. Old Indie Kac5/75-"redend, sagend', vac-, Nom. Sg. 

vak= Avestan vaxs{= Latin vox) "voice, discourse, word'. Old Indie vacala- " gabby, 

gossipy, loquacious, garrulous, blithering ', i/a/ry5/r7"Aussprueh, discourse '; vaktram 

"mouth'; 

Armenian gocem^cry, shout, shout to mir, lade ein, name' (?); 

Note: 

labialized old laryngeals {*hue-) 

common Armenian Celtic *hue- > gwo- > go-. 

gr. ETTOc;, el. Cypriot Fettoc; n. "word', Aor. slnov "sprach', Lesbian Fsinnv etc. (= Old 
Indie avocam, Indo Germanic *e-ue-uk"-om\N\\h Diss, from -FsF- to -Fei-), ona Akk. "voice' 
(also probably supuona as "den weithin schallenden'), oaaa f. "voice', svonn "shout, call, 
clamor '; 

Maybe alb. fem, them " say ' 

Latin vox, i/dc/s "voice', voco, -are'caW, shout, cry', Umbrian sub-ocau, -ocanu, -oco^ 
call, anbeten'; 

Old Irish foccu/'word' (= Old Indie i/5/r//'a/77 "mouth') < *uok"'-t/o-m = cymr. gwaethi 
"fight'; fua/mm'd\n, fuss, noise' {*uok"-smn); common lllyrian-celt. -k > -th. 

gall. Vepo-litanos^ breitgesichtig ', cymr. gweJblace'; 



Old High German giwahanen, -inen^ mention, commemorate ' {*gawahnjan, Denom. 
*uok"-no-, compare Old Indie vacana-; in addition tread in paradigm connection old 6- 
grade Pf.:) giwuog. Middle High German wuegen^ commemorate make, in Erinnerung 
bringen'. Old Icelandic i/a///'"Zeugnis' {*wahtaz, compare Old High German giwahtxr\. " 
mentioning, Ruhm'), i/a//a"bezeugen'; Old Icelandic omunt 'voice', nisi. dmur'soun6', 
Old English wdm{a)'d\n, fuss, noise' {*wdhm-)\ 

Old Prussian wackTtweT entice ', enwackemai^ we rufen an'; 
Note: 
The origin of labialized old laryngeals: 

Hittite huek-, huk- " adjure ', Tocharian A waki., B wek^yo\ce\ 

References: WP. I 245 f., WH. II 823 ff., Trautmann 339 f., Vasmer 1, 196, Bergin Eriu 12, 

136f.
```


## [2026-10-16T05:13:38.517Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'ueq\\u\\|u̯eq\\|ueq\\(u\\|ŭ\\)' incoming/WLD/WLD_Bd1_pages.txt | head; grep -n 'vaxš\\|vacah' incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-10-16T05:13:39.019Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:13:41.404Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'vox\\b\\|vöx\\|vocare\\|vöcäre' incoming/WLD/WLD_Bd1_pages.txt | head -20"
}
```


### [2026-10-16T05:13:41.690Z] TOOL RESULT

```
10278:das in seinem Nasal unklare gloss, anxare „vocare, nominare" s. Yf. LEWb. 2
22863:— av. va.is (=               lat.    vox) „Stimme,                    Rede, Wort'       1
22881:   lat. vox voc is „Stimme“ (s. o.), vocu. -arc ,,rufen“, nmbr. snb-ocan
```


## [2026-10-16T05:13:44.237Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22845,22885p incoming/WLD/WLD_Bd1_pages.txt; awk 'NR<22863 && /\\[pdf page/ {l=$0} END{print l}' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-10-16T05:13:44.886Z] TOOL RESULT

```
I 4 545f.   doch s. Pedersen KG. I 75, 74 und *tiesu- „gut“i, aksl. vest ho
              ;


„froh“ (s. *ues- „schmauson. sicli freuen“).


uek“- „sprechen“.
      Ai. vdkti, vicakti „sagt, redet. spricht". Aor.                                   dvocam (— hoi', s. u.), Ptc.
uktd -, Kaus. vncai/ati                                                                    ai. mats- n, = av. vucah
                                                                             1

                                       ,
                                           av. vac- .,sprechen' , Tixta-,
i== gr.      snog) „Rede,              Wort       fi
                                                       ,
                                                            ai.   vacanu- „redend, sagend'                           1
                                                                                                                             vac-, n. sg      .   vak
— av. va.is (=               lat.    vox) „Stimme,                    Rede, Wort'       1

                                                                                            ,
                                                                                                    ai.
                                                                                                                         ,


                                                                                                            vacald - „geschwatzig“
(ohne geschichtlichen Zshang mit lat. vocalis ), vakyum „Ausspruch, Rede -;
arm. govern „schreie, rufe, rufe zu mir, lade ein, nenne“ (Hvibschmann KZ.
23, 29       —
           allerdings widerrufen Aim. St. I 12, Arm. Gr. I 436      weitere                                                       —
Lit.       bei Liden         Arm. St. 70);
  gr. e'jiog, el. kypr. ye.-i og „Wort-‘ (s. o,), Aor. elnov „sprach‘\ lesb. ptmgv
usw. (= ai. dvocam, idg. *e-ue-U'/'t-om mit Diss. von -yey- zu -}si-, siehe
Solmsen Unt. 237 m. Lit.; verfehlt Siitterlin IF. 4, 100 f. und Hirt Abl. 132),
oTi   Akk. ,,Stimme“ (aucli wohl evovorta als „den weithin schallenden“,
s. Boisacq s. v., Bechtel Lexil. 145), dr, on f. ,,Stimme“, troy /j ,.Ruf. Larm“;
   lat. vox voc is „Stimme“ (s. o.), vocu. -arc ,,rufen“, nmbr. snb-ocan
                  ,                                                        -octiuu,                                                   ,


-oco (zur grainin Beurteilung s. v. Planta IT 361. Buck Gramm. 3<>3) „an-
```


## [2026-10-16T05:13:47.771Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR<=22850 && /pdf page/ {l=NR\": \"$0} END{print l}' incoming/WLD/WLD_Bd1_pages.txt; grep -n 'pdf page' incoming/WLD/WLD_Bd1_pages.txt | head -2; grep -n -i \"uek\\`\\|uek[\\\"'’]-\\|uekw-\\|uek\\^\" IEC.txt | head"
}
```


### [2026-10-16T05:13:48.116Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:13:56.601Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -22850 incoming/WLD/WLD_Bd1_pages.txt | tr -cd '\\f' | wc -c; awk 'BEGIN{RS=\"\\f\"} NR==NR {}' /dev/null; grep -n -i 'vox\\b' IEC.txt | head; grep -n -i '\\bvox\\b' SYN.txt | head"
}
```


### [2026-10-16T05:13:57.168Z] TOOL RESULT

```
253
11825:noktis, nokts ‘night (ultimately *noqutis, *noquís (?) in view of the vocalism of Gk. nux and Li. nakvóti, v. ‘spend the night, with an echo in Hitt. nekuc “evening, night- fall’, e-gde indicating the approach to night, as also in Tokh. B nekciye “in the evening, For a possible u-affection in Gk. cf. püksis under poks- below, and híppos (?); -u- and -i- for *-o- & *-e-. The i-stem seems to denote ‘night when counted; the consonantal form a familiar entity, as in Lat. vox, dux, lex, sol ‘the voice’ etc. I-stem in Skt. (Vedic) náktih, f.; Ober naktin, acc. sg.; Tokh. noktin and niktin ‘toward evening’; Lat. nox, gp noctium, but OLat. nox ‘by night; Ir. a nocht, in nocht 'to- night; W nôs, Br. noz, pl. nosiu, f.; Cor. nos; OCS oos Cz. noc, npl. noci; Latv. nakts, gp: nakéu. Cons.stem in Vedic nak, m.; Gk. nux; Alb. natë, pl: net; cf. nádje “in the morn- ing; Go. nahts £.; OHG naht, npl. id., gp: nahto; OE niht (fr. *nekt- or *nequt-); ON. nátt, nótt; Cz. veliko-noce, pl. (great nights? = *Easter); Li. naktis, gp naktü. Cf. also Go.
20478:ulg- *wet, damp; dampen'. WP I, 306. Cf. uelg-, (variant uolg-) Alb. lag, v. (^wet', via a type *ulog-, cf. valë ‘wave’ and i parë 'first); W glaw (occasionally gwlaw), m. ‘rain’; Cor. glaw, m., Br. glað, m. id.; MHG cf. wolken, wulken, s & wf. “cloud, welkin'; cf. wolkern, wulkern, sf. ‘cloudy urine’; Du. wolk, f. ‘cloud’; OE wolcen, m & n. (2), id.; Fris. wolk, wolke, wolken & wolkem, id.; Norw. ulka, ulke, f. ‘slime’; cf. OCS vlügü- kú, adj. (^wet, fr. *ulguko-); Cz. vlhký, id.; Pol. cf. wilgnac, intr. ‘grow damp’; Ukr. vox- kyj, adj. “wet, damp”; Li. cf. vilgstu, vilgti, intr. grow damp’ beside vilgau, yti, tr. *dam- pen’. (O-gde in OCS, R vlága, Cz. vláha, f.
12008:ON reykberi, -hafr, skor- Lith. kaminas 00X71 Ce re sleinn Lett. skurstenis ok vox (lit.), Kap Dan. _ skorsten SCr. dimnjak (odZak) NG iby gouyape Sw. skorsten Boh. komin (eamins) ME chimney Pol. honin Jat amino NE chimney Weave peaulare! It cheminée Du. schoorsteen “4 chimenca OHG scor(en)stein ia a MHG schor(n)stein y Nie ee emnai NHG  schornstein (kamin, V. simdde, oe rauchfang) Br. siminal
31758:18.26 WORD Grk.  pfjua, dékts, eros Goth. waurd Lith. Zodis NG ékis ON ord Lett. vards Lat. verbum, vox Dan. ord ChSl. glagolii, slovo It, parola Sw. ord SCr. rajeé Yr, mot, parole OE word Boh. _ slovo Sp. palabra ME word Pol.  slowo Rum. cuvint NE ‘word Russ. _ slovo Ir, briathar, focal Du. woord Skt.  gabda-, pada-, vacas-, Nir. focal, briathar OHG wort etc. W. gair MHG wort Av. vat-, vatah-, urxéa-, Br. ger, komz NHG ~ wort sravah-, ma§ra-
32138:2. Lat. vocare : vox ‘voice’ (18.11).
```


## [2026-10-16T05:14:01.141Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '18\\.11 VOICE\\|^18\\.11\\|18\\.21 SPEAK\\|18\\.26 WORD' SYN.txt | head; sed -n 31758,31775p SYN.txt | cut -c1-1500"
}
```


### [2026-10-16T05:14:01.615Z] TOOL RESULT

```
31450:18.11 WOICE (sb.)
31563:vyocAL UTTERANCE, SPEECH; READING AND WRITING 1253 18.21 SPEAK, TALK Grk. deve (aor. enor, fut. Goth. rddjan, mapljan Lith. kalbéti ; toa, etc.), ayopebw, ON mala, reéa, tala Lett. rundat Nard Dan. tale, snakke ChSl. glagolati, vétali
31758:18.26 WORD Grk.  pfjua, dékts, eros Goth. waurd Lith. Zodis NG ékis ON ord Lett. vards Lat. verbum, vox Dan. ord ChSl. glagolii, slovo It, parola Sw. ord SCr. rajeé Yr, mot, parole OE word Boh. _ slovo Sp. palabra ME word Pol.  slowo Rum. cuvint NE ‘word Russ. _ slovo Ir, briathar, focal Du. woord Skt.  gabda-, pada-, vacas-, Nir. focal, briathar OHG wort etc. W. gair MHG wort Av. vat-, vatah-, urxéa-, Br. ger, komz NHG ~ wort sravah-, ma§ra-
18.26 WORD Grk.  pfjua, dékts, eros Goth. waurd Lith. Zodis NG ékis ON ord Lett. vards Lat. verbum, vox Dan. ord ChSl. glagolii, slovo It, parola Sw. ord SCr. rajeé Yr, mot, parole OE word Boh. _ slovo Sp. palabra ME word Pol.  slowo Rum. cuvint NE ‘word Russ. _ slovo Ir, briathar, focal Du. woord Skt.  gabda-, pada-, vacas-, Nir. focal, briathar OHG wort etc. W. gair MHG wort Av. vat-, vatah-, urxéa-, Br. ger, komz NHG ~ wort sravah-, ma§ra-
Words for ‘word’ originally denoted Something said, ‘saying, utterance’ (and Several of the words listed are quotable Mostly in this general sense), and only Secondarily the individual ‘word’. Many re connected with verbs for ‘speak, say’,
though in some cases not the one current in the same language.
1. Derivs. of IE *wek- ‘speak, say’ (18.21). Walde-P. 1.245 f.
Grk. éros; Lat. vdr (also ‘voice’), Skt. vacas-, Av. vacah-, Av. vdé- (also
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1262
‘voice, speech’), wxéa- (also ‘saying’, pl. ‘speech’).
Here also Lat. vocabulum (more di- rectly fr. vocdre ‘call’) ‘appellation, name’, later also ‘substantive’ and in MLat. ‘word’.
2. Derivs. of IE *wer- in Grk. fut. épS, etc. ‘speak, say’ (18.21), esp. IE *wer-dh- (*wy-dh-, *wor-dh-) ‘word’. Walde-P. 1.2833. Ernout-M. 1088 f. |
Grk. Aqua (orig. ‘word, saying’, later gram. term. for ‘verb’); Lat. verbum, Goth. waurd, OE word, etc., general Gme.; OPruss. wirds, Lett. vards (latter also ‘name’, as Lith. vardas).
3. Grk. défs, orig. ‘speech, diction, style’, whence ‘single word or phrase’ (Aristot., etc.), then usual gram. term for ‘word’ and so in NG : déyw ‘speak, say’ (18.21). Hence also Grk. déyos, used of a, verbal expression or utterance, but rarely of a single word and never a gram. term in this sense.
4. It. parola, Fr. parole (now mostly ‘saying, utterance’; for the individual ‘word’ replaced by mot), Sp. palabra, fr. VLat. parabola, fr. Grk. rapaBon4 (orig. ‘juxtaposition, comparison’ : mapaBanrw ‘set beside’) in its biblical sense of ‘parable, saying’. Wackernagel, IF 31.262f. REW 6221. Ernout-M. 731.
Fr. (Prov., Cat.) mot, fr. VLat. mut- tum ‘a grunt’, back-formation to mut- tire, mutire ‘mutter, grunt’. REW 5795. Gamillscheg 625.
Rum. cuvint, also ‘(one’s) word, prom- ise, agreement’, fr. Lat. conventum ‘agreement, compact, accord’. Cf. NG kouBévra ‘conversation’, kouBevriatw ‘con- verse’. REW 2194.
5. Ir. briathar, formally = W. brwydr ‘battle’ (orig. ‘word-battle’?), but root
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
```


## [2026-10-16T05:14:04.608Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 31450,31470p SYN.txt | cut -c1-1500; awk 'BEGIN{RS=\"\\f\"} NR==51' SYN.txt | head -c 1500"
}
```


### [2026-10-16T05:14:05.115Z] TOOL RESULT

```
18.11 WOICE (sb.)
Grk. dw Goth.  stibna Lith. balsas NG gw ON rodd, raust Lett. balss Lat. vor Dan.  stemme, r¢st ChSl.  glasi It. voce Sw. rést, stamma SCr.  glas Fr. voix OE stefn, reord Boh. hlas Sp. voz ME vois, steven Pol. gtos Rum. voce, glas NE voice Russ. golos Ir. guth Du. stem Skt. vac- Nir. — guth, glor OHG _ stimma, stimna, rarta Av. vdé- W. ais MHG ss stimme
Br. mouez NHG = stimme
Words for ‘voice’ are mostly connect- ed with verbs for ‘speak, say’ (18.21, 22) or are words for the more generic ‘sound’ (15.44), several of which (besides those repeated here) are, as including vocal
-sound, also frequently ‘voice’.
1. Derivs. of IH *wekv- ‘speak, say’ (18.21). Walde-P. 1.245f. Ernout-M. 1185 f.
Grk. dy (poet.); Lat. vdx (> It. voce, Fr. voiz, Sp. voz, Rum. lit. voce); Skt. vdc-, Av. vié- (nom. sg. Skt. vak, Av. vars); Toch. A wak, B wek.
2. Grk. guava : dnl ‘say, speak’ (18.21).
Grk. $0éyyos, see ‘sound’ (15.44).
3. Rum. glas, fr. Slavic (below, 7), but largely replaced in modern lit. lan- guage by voce (above). Tiktin 686.
4. Ir. guth, etym. dub., perh. : Skt. havate, Av. zavaiti ‘calls’, etc. (18.41). Walde-P. 1.529 (vs. Pedersen 1.108).
NIj. glor, see ‘sound’ (15.44).
W. llais, etym.?
Br. mouez, moez for *vouez, *voez, fr. OFr. vois. The initial vy was considered a mutated consonant, e.g. da vouez ‘thy voice’; hence also with the other possible reconstruction Van. boeh. Henry 207.
5. Goth. stibna, OF stefn, stemn, ME
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar ss
steven, Du. stem, MLG stemme (> Dan, stemme, Sw. stémma), OHG stimma stimna, MHG, NHG stimme, etym. dub, relation to Grk. o7éua ‘mouth’ (as Weig- and-H. 2.973, Kluge-G. 595) improb- able. Walde-P. 2.648. Falk-Torp 1156f. Feist 452.
ON rodd, OE reord (mostly ‘speech, language’), OHG rarta (also ‘melody, rhythm’) : Goth. razda ‘speech, lan- guage’, Skt. rés- ‘roar, yell, cry, sound’, rasita- ‘noise, roar, cry, etc.’. Walde-P. 2.342, Falk-Torp 873.
ON raust, Dan. r¢st (rhet.), Sw. rést : ON raus ‘loud talk’, rausa ‘talk loudly and rapidly’, ODan. ruse ‘roar, hurry’, MHG rischen, NHG rauschen ‘rush, roar’, outside connections dub., prob. of imitative origin. Walde-P. 1.142, 2.351. Falk-Torp 938. Hellquist 876.
ME voiz, vois, etc., NE voice, fr. OFr. voiz, vois, etc. (above, 1). NED s.v. voice, sb.
6. Lith. balsas, Lett. balss : Lith. biliti, byloti, Lett. bilst, formerly com- mon words for ‘speak, say’ (18.21). _
, NHG berg, etc., the most widespread Gmce. word for ‘mountain’ (but ON bjarg ‘rock, precipice’; in Goth. only bazrga- het = dpewh ‘hill country’) : Skt. brhant- ‘high, great’, Av. barazant- ‘high’, bara- zah- ‘height, mountain’, Arm. berj ‘height’, Ir. bri, ace. brig, W., Br. bre ‘hill’. Walde-P. 2.172 ff. Falk-Torp 77.
OE din ‘mountain, hill’ (NE down), ODu. dina (> Du. duin ‘sandhill’, Fr., NE dune), formerly believed to be a loanword fr. Celtic (Ir. din ‘fortified place’), but this is now generally doubt- ed; perh. fr. the root seen in Skt. dhu- ‘shake’, etc., with development similar to that in Grk. 6ts, @tvds ‘sandbank’ (*Of-tv-). Walde-P.:1.837. Falk-Torp 171. Franck-v. W.141. NED sv. down, sb.
OE munt fr. Lat. méns, montis; ME mount, mountain fr. OFr. mont, mon- tat(g)ne (above, 2).
OK hyll, ME, NE hill : Grk. xodwvés, Lat. collis, etc. (above, 1).
Dan. bakke, Sw. backe ‘hill’ : ON bakki bank’, NE bank, etc. (1.33). Walde-P. 2.148,
Du. heuvel, MAG hiibel ‘hill’ : OHG hovar, OE hofer ‘hump’, Lith. kupra ‘hump’. Here also Av. kaofa- ‘mountain peak, camel’s hump’, OPers. kaufa Mountain’ (NPers. kwh ‘mountain’) : Lith. kaupas, ChSl. kupt, NE heap, NHG haufe ‘heap’, Grk. xidés ‘bent’, all fr. TE *keup-, *keub-, *keubh- in words for ‘bend, curve’. Walde-P. 1.372 ff. oh ha a Gor, pe mound’, fr, the adj. seen in
- hauhs, OHG hoh, ete. ‘high’
(12.31), ultimately connected wit
```


## [2026-10-16T05:14:26.581Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^ *vak\\|^ *vāk\\|^ *vač\\|^ *vac\\|^ *vax\\|^ *vāx\\|^ *vāč\\|^ *hūxt\\|^ *uxδa\\|^ *uxta\\|^ *vīvač\\|^ *fravaxš' BRT.txt | head -50"
}
```


### [2026-10-16T05:14:26.909Z] TOOL RESULT

```
2691:vacim*aiwyäs-i^.l4.  2)     als    unbest        Eig.  Bcd.?    ->)   NA.   tr^nt.     Meine    Auf-
6134:vakiltfm  Yt/7.18;  V. /Äi6;  —  'hm  vahi- shm  staohwfm  (sd)  Vr.  2.6;  —  'saie  vahi- itahe  staokwahe  Vr./.4;  —  taraiuiirahe .  .  yim  slaotarTm  'sähe  yal  mazistahäa vahislakeca  sralstakeca  YtJj.  9z;  91;  — vanainitmcä  uparatäbm  yam  °sahe  vahi- HaAe  paiti.parstlmca  ■ma^rahe  ipmtahe Yt.  }o.  zz-  S.  noch  'a/a-  aK  mit  No. 30.  [Yt/J.91:  lies  awm^rav3\  —  H. 1.3:  lies  ahniJtuts^
19615:vaca  'S.  26;* 26''*.        A)  ISn.  °tpmya  als
20648:vacS  sara%usira  FrW.  /,  a;  Vt._j.  a,  V.  2.  5 PiiZ.;  —  yezi  humatsm  mainyät  kOxtim vääm  mrvUt  kvarstim  virizyät  ^aöhi Gs. /ö^;  — yüi  narS . .  humatais  mainit. Aaxfäis  (statt  AP.)  mrvai3l,NP.)  hvarsfüiS vimyantd  V.  70. 4 ; — manya . .  htzva  hUxtym mrSiti  Aog.  2(*fF.;  —  nsit  ma^ö ..  mraoiti duiuxhm  ya%a  mihrasat  mraoiti  hüxtim Yt  10. 106;  —  mazds  data  mraei  gayekyä (sd.)  syao^anais  vahyBY.  ^1.  19.  a)  mit Dat.  dcrPersoa:  sä:^}nl . .  kainibyB  mraomX ^-  53-  5  i  —  ^'*  '^'  "^'f  y^  ^^^i  S^'*^  '^■f'* (sd.)  mraot  Y.  46.  9;  —  aHbyS  mazdä  aka (sd.)    mraot  ysi  .  .  Y.  _J2.  12.  4)    mit
21383:vakma-i  fira  vS  rahi  ami^ä  ipmiS  'mmca vahtnfmÜl  Y. //.  18;  —  avi  apqtn&t urvaranqmca  asaonqmla  fravaHnqm  'rata g»r3hmahi  vahimm^a  Vt.si.i;  if.*;  — 'nsmca  vahmtmla  .  .  a/rlnami  ahurahe matdä  \.y2.6;  62.1,  P..J9,  F.^g: v^v3  aliqm  (n'äml.  des  ÄhM.  usv.)  'nfmia vahmtmca  Vr,  ir,  19;  — frä  *lg*siaomaide ,  .  ^vanküs  'nasla  *vahmqsca  N.  4^; yaita  . .  anuia  spmta  ,  .  paitisqn  vaahUs (AP.)  'nqsca  vahmqüa  vohü  (AD.)  'nsmci vahmftnca  Y.  60. 6 ;  — yal . .  sacyär>l  ääitTn 'n^mü  vahimmca  yaha  Al  asti  äaityd. timS'nasca  vahmascaYl.8.<,(i\  Y.ÖS.j;  — yä  *aiwinas>nU  vatahüS  'nqsca  vahmqsüa Y-  -J-  3;  —  vlspasla  apS  yaiamaide  . .  a 'näaiia  vahmäaica  yaia  ankam  asti (s.  eben)  Y.6Ä6f.(?);  —  aäa  'na  a vahma  ..  avajasa  YL5. 13a;  —  yat  ti aitihe  ava.urürao^a  yat  'naheia  vakma- kela  Y.i.  21,  o)  insbes.  DS.  in  infini- tivischem Sinn  (s.  Sp.  1270  u.):  mrHioi vacil  zara%ustra  ahmSktm  'näi^a  vakmäica yai  antfsanqm  spgntanqm  FrW. /.  2;  G./.  7 j.  7,  ^9,  5'.  6,  YL/o.iaz,  Vr.5.6,  Y.i^.i', ^y^47i  —  daevanqm  'nüUa  vahmäüa  V, i6.\\-, — staotaca'näica  vakmäica  frasasta- yal^a  yai  a^a  akurake  Vr.  (J.  6;  —  kävanse .  .  'ttäica  vakmäica  xsnadi^räH^tveiz.)^a frasastayatla  Y.  J.  23;  usw.  c)  in  Ver-
22213:vaxsmtl  (Konj.)  daivs^uita  (sd.)  Y.^e. 4;  —  yd  nä  iltasca  .  .  vaoee  Yt.  13. 152;  —  urvarayä  yä  vaoce  haäänal- fäta  V./4.4;  —  dahinter  nama:  urvarayä ya  vaoce  hap?r)si  nqma  Yt  14.  55;  55, Z0.88,  /2. 17.  in)'  'etwas  (Akk.)  be- haupten': mä  gius  mä  vastrahe  kaiö aläitlm  (sd)  vao^öit  V.  4. 46.  IV)  'er- klaren etwas  zu  tun,  tun  zu  wollen'  (Inf): ahyä  vanhiul  manataAs  syadhanä  vaocat girtbam  (sd.)  huxraluiY. 34.10.  Undeut- lich:'Vaojcft  F.80;  —  vavaxla{ii?,'Pi\.) F.S;  —  vaacim  FrW.5,  2.
22270:vax»8ra-
22354:vacah-
28600:vacqm  Yt  2. 1 1 ;  —  ha  va  nsip  na . .  Vjt 26.        S,  noch  zu  "halca.
```


## [2026-10-16T05:14:29.243Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22150,22175p BRT.txt | cut -c1-600; echo ----; sed -n 22340,22370p BRT.txt | cut -c1-500"
}
```


### [2026-10-16T05:14:29.716Z] TOOL RESULT

```
1337
vaes-  mit  paiti
vaesma-
1328
nehmen':  vJsmU  aval  vlssnta^a  *mazyasat . .  fravaiayS  "sie  stellen  sich  dazu,  sie stellen  sich  auch  zu  noch  grösserem  be- reit . ."  YLiy.73;  —  at»m  aita  zaota  vUäi staotanqm  yesnyanam  frasraohnm^a . .  "ich will  es  als  Z.  übernehmen:  das  laute  Auf- sagen . ."  Vr._j.  7.  3)  '(herantreten  um zu  —  sva.)  sich  bereit  stellen,  dran,  drauf aus  gehen  (etwas)  zu  (tun),  es  übernehmen zu  — ,  bereit  sein  zu  — ',  mit  Inf.:  visaraha mi  .  .  mprvis  ifri/a(sd.)ca  dalnayili  V. 2. 3 ;  —  vlsaiti^''  dim  frayrSrayS  nStt frayräyräyätiisä.)  N.  ig;  
"Yt.5.g5:  s.  gleich,  hc\  paiti.\
mit  paiti  'sich  emstellen  bei  — '  (Akk.) : paili  nS  sao^ri  visa»uAa  paiii  hlS  yasta vTsatiuha  W,lQ.xi;  —  nSit  ava  zaoira paiti.vise  (iS.)  _v^. .  YL5.  93;  —  nfvayaka . .  imä  (n'äml.  zad^ra)  paiti.vlsfttte  yä  . .  Yt.
595;  —  y^  (1- .y^?)  «^f?  ^"'^ (i- /«»'fti')
vispn/i  (für 'sinii,  Pass.?)'*  äaRanqm  haiti (1.  paitt)  yasna  "welche  nicht  (von  mir) besucht  werden,  die  dienen  zur  Verehrung der  n."  Yt5.95(?).
mit/^j 'sich  bereitstellen  a)  als-' (Nom.): frS  tl  vUäi  urvahS  staota  Y.io.  9;  — j/a/  vihaäa  a%aeyamnö  frä  *a>iAe  visaiii^^ mi^rff  . .  yakmäi  . .  Yt.  w.  46.  b)  (um)
zu  — '  (Inf.) :  T^J  ai/yS  tanubyS  haomS  visäite balla%äi  "denen  wird  sich  H.  bereit  stellen ihren  Leib  zu  heilen"  Y.  10.  S.
ai.  viiäli  'er  tritt  ein',  PDy.  vlsäm  'ich  gehe'; Tgl.  mp.  3^ar-ätän  'Sonnenaufgang'  (am •-ä-{(u'),  —  Pü.!  patgri/lan;  Sü.:  praHiarlum, (lu  Y.57):  fToOktanam  äsle;  s.  noch  No.  6.  — 1)  Nur  im  Inf.  —  D  In  ^paäi  visinti(}),  in  $  jaj No.;  ».  ^^X  hiniiav-'iia.-l.  —  Stiiiiailt  Yt  to.^, N.  tg,  P.  57  und  viiäili  N.  /j  sind  die  ein- »igen  aktiven  Formen.  Der  Fehler  -ä  «tott •tt  ist  beim  Verbum  häufig.  S.  No.  5.  — «)  Hds.  vaisafle,  —  i)  So,  mit  schliessendem e,  Pt4;  s.  No.  3.  —  6)  püErl.:  tuiän  aiär kartan  nS  luvän.  — 
•  '].  vaesa-  m.  'Knecht',  der  im  Herrenhof seine  feste,  dauernde  Wohnung  hat'*:  a%ra- varam..nman5.pailTm..nmanspaitTm  nairi- kqm..  'sJs/a  ^pairyaarSusca yaozda%d gSuI
paiti  vazya  nitumamcit  apirmäyBApm  .  . "einen  Priester .,  einenHausherrn ..  die  Frau eines  Hausherrn  . .  Knechte  und  TaglÖhner sollst  du  heilen  um  .  .,  geringster  Leute Kind  , ,"  V.  g.  37  f.;  —  c^andrakarS  (nämL ist  der  Hund)  ya'ka  °SB  V.  y.  46;  46'. KompE.  —  Ableit.  ans  vis-%    zu    S  -/oo  a.  a.
—  ai.  veiä-  m.  —  Vgl.  vaisav-.  —  Pu. ;  tranukr. Weiteres  bei  DsT.  ZA.  3.  206.  —  »)  Im  Gegen- satz ztl  pairyiitlar;
j.  vaiia^lr  P.  5:r:  lies  vhaFlc;  s.  W«-.
•  j.  vaesacpan-  Adj.  -  ?  -:  nBit  sat?m /ainti  viraja  nBil  halanl  jainti  'pa  (NS.) Yt.74.37.
Npü.:  liest  vispa\
•  j.  vaesakay-  patr.  Adj.  'von  VaSsaka stammend,  dessen  Nachkomme':  tarn yasmia  aurra  hunavB  'iaya{li¥.)Yt^.S7; —  hunavB  'kaya  (als  AP.)  Ytj.  54.
Ableit  aus  "vatsaka-  m.  EN.,  Feldherr  de* Fraarasyan  (mp.  veiak,  np.  i'iSra);  vgl.  Bd.  J/. 16,  Ük.  s-   15.  a  (,  23.  6),  JusTi  NB.  366.
•  j.  vaesaSa-  m.  £N.  eines  Gläubigen: 'üahe  asaonö  Yt. /J.  iio.
Eig.  Bed.?  Uhlenbeck  WAiSpr.  vergleicht u.  viiada-  Adj.  'klar'.  Eher  wohl  •Mwo-iö- Adj.
•  j.  vaesav-  m.  sva.  vaüa-'>:  asti  Ä Äa^  (sd.)  ya^a  'säus' (GS.)  V.y.  44;  — aiti  se  Aaim  ya^a  'saus  V.  13. 46.
Ableit.  aus  vir-.  —  Vgl.  vaüa-  —  Pü. :  traiiMkr.
—  1)  Unrichtig  Ludwig  Rigv.  4.  413.
•  j.  vaesina-  m.  'Wohnung":  iaha  ttif ■fraourvaüayäiti  .  .  drujB  'mmda  (AS.  4- 'äay^  azomnqm{%A.)  Yt  70.86.
----
•  j.  yttvat  nü  ala  "Vacaiti  . .  vupa  tarsuca xiudraca    "vnatH  *ana   *masanaca   .  .  P.
42: -?-■>.
Pü. :  an  and  ahraJttk  vittdet  .  .  d!än  i  tdr  (Sp. 644  m.l  u  hur  vindät.  —  1)  Nach  Pü.  sollte man  lowohl  für  vaiaiti  als  für  vtuöH  vielmehr
•  j.  yai  .  .  "vadat  apayanta"  N.32.
I       PiL :   g^wiitt  S  gäoän  \    s.  Sp.  749  o.,  wd  die
Lesung  vaia  vä  apayaeiä  vermutet  wild. '  j.  va/aita  N.  34:  lies  t/aäulaifivaf/a, I  •  j.  vacas-taStay-  i  'Stiophe'  der  G3>äs  ■': *spfniä.mainyem  *'-llm  '>  xrvai  vahistfm sravayeiti  "die  mit  Sp.M.  beginnende Strophe  (und)  sechs  Asa^^bext  soll  er aufsagen"  N.  50;  —  yö  gä^anqm  Syfm väam  apayäiti  atvqm  vil  'tim  'ii.42;  — apanö.tjmaya  paitl'ta  (LS.  als  Instr.)  Y. $8. 8;  —  tisranqm  haurva.paoiryanqm\sA.) .  .  häiiisca  afsmanaca  vacasca  'timia'* "v
KoropE.;  Ableit.  —  Eig,  'Kedegebilde',  zum V.  tai-;  d-  lailay.  f.  —  Pü.:  miÄ«/,  (zu  Vr.) : iiaciasl  naniimh,  —  ')  Im  Ganzen  278. Falsch  Gdn.  VSt.  1.  2S7;  vgl.  N.  33.34,33, 43,50  und  SBayrAW,  18^3.  97,  SBE.  ^/. 401,  ferner  SWienAW.  67.  850.  14:  "vicail karda  •  aaimlä  u  xand  güyand.  —  ')  Hds- 'tiiUm.  —  äl  Man  verlangte  Plnr.  —  J)  S. No.  2.  —  0  Geschr.  n  £  dddt  (patdasl)  oder ndpdddt,  ndpddL
•  j.  va£asta§tivat  Adv.  'strophenweise': yJ  gä^ä  frasrävayal  *afsmaimvqn  (sd.) 'vat  Y.  57.  8 ;  N.  23,  24,  24  ■>.
ASn.  aus  'varaslastiK-anl-  Adj.  'so  wie  die Strophen  (der  Gä%ä%)  sind';  vgl.  zBed, Wh.  Gr."  S  1107.  —  PiL:  /a  vaaail.  — 'I  Hds.  nur  varaila  (sUlt  'lailaraiid).
•  ji  g-  vafah-  n.  i)  'Sprechen,  Rede, Wort (als  Tätigkeitsbezeichnung)';  im  Gegensatz zu  Denken  und  Handeln  (oder  äbnl.),  A)  im gA^.:  at  til  mainyä  ..  manahicä  'cahicä syaohansi  hT  vahyS  ai>M(sd.)cä  Y.30.3;
—  ipgrttä  mainys  vahistäcä  mananhä  . . fyaoianäcä  'canhacä  ahmSi  dqn  (Sp. 7120.)  .  .  Y.  4-].  1 ;  —  yS  ahm  dngväitl 'catshä  vä  at  vä  mananhä  tastdibjä  (sd.) vä  vaniaitt  Y.jy, »;  —  yS  dät  mono vahyB  . .  asyasisd.yä  hvS  daOtqm  ffoe- %anäca  'catfhäca  Y.  46. 4;  —  hyüt  va akä  mananhä  .  .  akä  fyadhatum  'canhä yäjracinas  dr?gvatttim  x^ayS('SÄ.)  Y.J2.S;
—  yä  syadhariä  yä  'canhä  yä  yasnä amfnfatätfm  .  .  dänkä  (sd.)   Y.J4.  1;  —
dby  Google
I34I
vacah-
va£ö.mar9ta-
134a
voha  hvS  x/a^rä  ahm  'catikä  ^ao%attala Aaptl  (sd.)  Y.J1.22;  —  vatikuys  "^wa ästöis  syao%anaii^a  'cSbTscä  pairijasa- maidl  '^.36.  4.  b)   im  jAiw.;    narsm
asavatum  .  .  yd  anhat  °/j  arsvacH  (sd.) V.  ^.  2;  —  sonst  nur  neben  manah- (zum  Wortlaut  der  Stellen  s.  Sp.  11 39 unter  o)  und  ^aohna-:  yänJm  manö  .  , •CS  ,  .  ^ae%p>m  zar^uitrahe  Y.  i8.  o; V.7.  51',  Äioo,  Yty.  83; — ma  apama .  .  mä  manaaha  .  .  'canha  ,  ,  Syao%na ^mäha  ka%acina  *paiti.jime  Vr.  22,  a;  Y. 1.21,  Ji.  18  (•caaAä);  —  vJ  Jasväi/ .  . iarim  mruyl  .  .  vT  matisbli  .  .  °cSbll  ,  . ^ao%anaU  Y. /2. 4;  —  pairl  manä  .  . °
Diktum'  (sva.  'vak-  a);  a)  im  gAw.:  °(5 srüidyäi  (sd.)  Ayat  mar>talibyS  vahisUm Y.*(5-5;  —  agusts{%A.')  'ch  sPnghämaht aHbys  ysi  . .  at'it  aHbys  vahüta  yöi  .  . Y.31.1;  —  yastum  mazdn  xsmävats  at vä  ala  staomyä  (sd.)  'ca.  Y._jy.  8;  — »niuxhäi  'catshqm  xsayamnd  (sd.)  hiwS vasS  Y.ji.  19;  —  imH  at  uc^ä  °M  .. fravaocämä  Y,_J5.  9;  —  at  vJ  vayci  (sd.) aKkaitt  apSmtm  'csX.^.l.  B)imjAw.'. ahe  'cB paityesti ..upa.vazata  *nairy3.sat»Ad \ V.  22. 13
J7. 17,  22\  —  eil  ^'""i  °^^  ^^  ■  •  y^t  '"^i
frävaocs  Y.ig.i''>;  8;  —  aitaica  nS  •ci>\ /rävao^e  *sixsaeml%d.)ca  .  ,  Y.  ig.ji;  — imat  -/s/ramrB:  mmö  .  .  V.  iff.  18;  FrW.  | /,  3 ;  —  ff  ?/5 .  ■  v3x/ ..  ä  'c5  oAunS  vairyö  \
fraoxtö  .  .  spanvanii  H. ;.  4;  —  yasca  .  . imat  uxtpm  'tB  fravaocat  YL 11. 4;  — ..  anye.**cäsca^^  */ramravainH gavSstryäfa vartinä  vjnunti  N.  ö'o;  —  imai  uxorm '^ /ramruyä  Yt.ii.6;  VyL  20,  22,  26,  28, 55;  —  aha  zl  mraot  akurS . .  zarähuftrSi raprhwinahe  ra%wö  uxb?m  'cB  A.  4-  3;  Yt J.  a ;  —  altalca  'cS  mazdaoxt»m  ^ri.a/itrDm iahrupistrim  panca.ratu  Y.  75. 16;  FrW. g.i;  —  vTspam  'cff  fravä&im  (sd.)  kaurum 'CS  ahurake  mazdä  Y.ig.14;  —  ye
Sinn  von  Versprechen ,  mündliche  Zu- sicherung: ''s  paoirXm  miirvm  (sd.)  hr?- naoiti  V.  4. 35',
Undeutlich:  yniAe  'cataks  n»mavhs  .  . P.  26.  [Y.  57. 28,  F.  je',  f  •:  lies  •vac%] KompA.i  E.;  Ableit  —  Zum  V.  vai-.  —  u. vätas-  n.  —  Pu. ;  gdtoßn ;  s,  auch  Nu.  3,  5.  — ')  Hds.  i/fl/fljrti.—  J)  PQ.:  sai^an.—  3)  Hda. va!äs^a.  —  1)  An  der  ParaUelslelle  S,  i.  18 steht  väSm.  —  S]  Pü, :  pa  gStoisn  /ralum  mihr kunend,  mit  mir  unverständlicher  Erläuterung. Vgl.  lu  vacahina:
■  j.  vacahina-  Adj.  'durch  das  blosse Wort  geschlossen',  von  mi^ra-  m.'Vcrtrag': paeirys  (näml.  mi>rs)  'nS  "die  erste  (Art des  Vertrags  wird)  durch  das  blosse  Wort geschlossen"  V.  4.  2;  —  aisS  mi^rö  yS 'riS  V,  4.  s;  —  yö  mihnrm   aiwiJruzaiti
Ableit.  aus  valah-.  —  Pü. :  («lif)  i  pa  gduiisn, —  1)  Vgl.  V.  4.  3;  vaB  faoirim  m^tim  km- naoiti  und  apa.m}r>ta-  5p.  1143  m.
•  j.  vatSah'ya-  n.  —  ?  — :  paiti.asti  gSul
'yeheca  Aa'liravataAeca ..Ytis.i.     Wertlos.
•  j.  vaäö.marata-  Adj.  'mit  (vernehm- baren) Worten  aufgesagt,  rezitirt';  manS.- Mar^tanniiica'tanqmcaitiä.xai.sravarjAqmy^ "der  in  Gedanken  und  der  laut  rezitirten (Gebete)"  N.22.
pü.:  fehlt.  —  ')  Die  Worte  stehen  in  Fä.i ■"■?  marl  .  .  fa  . .  a/räi  öimurihüh  äslaret  ka mariö.mar?/anifmca    nc    kunll  agdn  ^änS  ia
```


## [2026-10-16T05:14:33.005Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"'Stimme\\|„Stimme\\|Stimme'\" BRT.txt | head -20"
}
```


### [2026-10-16T05:14:33.383Z] TOOL RESULT

```
17225:weise,    mit  lauter  Stimme':  b'  vacö  rasa-
22236:•  j.,  g.  »vak- :rd^*-m.,f.'>'vCHc';l) 'Stimme';
22237:1)  der  Menschen  (und  Götter)  'Stimme'
22273:KompA.  (vaxl'),  E.  —  Zum  V.  vai-.  —  at, väi-  f.  (vai,  väeä);  mp.  vä/  'leises  Gebet', i^/  B  mSriiän  'Satie  und  Wörter'  (F.  O; Tgl.  Zs.  4,  Dk.  8.  46.  1),  v3iak  'yak  stamn  i awaitä'  (SWienAW.  6/.  850.  16);  np.  äväz 'Stimme',  ävä  i  iöi  'Trommelgetön',  guväia 'Schelten';  a.  dazu  Hbm,  PSl.  104,  idq.  — P6,i  gdwün,  (lu  Y.  31,  V,  rS.  IS,  F.  ^  e i.Sl):  väng;  %.  noch  No.  5,  7-  —  "  So  wohl »icher  FtW.  /.  I.  -»)  So  Pl  4.  NA.s.üV>m.  — 3)  S  '94-  3.  —  <)  Wo  vajcs  hinter  m&aexto ausgefallen  isL  —  i)  Vgl.  die  öfter  wieder. kehrende  Erläuterung  lu  göwSn  in  Pü. :  apa- stak;  iB.  Y.  16.  1,  Ny.  /.  18.  —  6)  Bthl. Stud. /.  79.  —  7)  Hds.  vana;  Pü.:  ffu/tif).  — 8)  Pt  4.  NA.  paumacqm.  —  9)  Aus  dem  NS. gebildet,  der  -uüxi  und  poii  (FrW.  9.  l)  ge- lautet haben  mag;  er  erscheint  auch  amAn- fang  des  KompoBitums;  weniger  wahrschein- lich IF.  5,  59,  —  'o)  An  der  Parallel  st  eile S.  /.  18  steh!  vaAiaAS.  —  ")  Deren  Zahl auf  5567  und  6666  angegeben  wird;  vgl. SEE.  J7.  404.  —  I»)  Im  Fahl.-Text  ent- spricht: 3  gdTeUn;  DsT.  ZA.J.  104  sieht  darin eine  Anspielung   auf   die   bekannte   Dreiheil
22287:ist  die  Zerlegung  in  'fai-  ('Stimme')  +d:
```


## [2026-10-16T05:14:37.478Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22230,22300p BRT.txt | cut -c1-700"
}
```


### [2026-10-16T05:14:37.945Z] TOOL RESULT

```
vaeiämi  des  Vyt.    —    3>  S  ti^-  4i  337-     rrH
ist   nach   dem  Metrum   als   massige  Wieder-
hotang  zu  itreichea.    Pü.  -.  paart  t  rast  OVismAi
vgl.     die     Var.    }r>ijqm     und    zu    tribjl-.  —
<)Hds.  vaohxteM.nAvaohaxU.Vä.-.guft.  —  tiZ'a
streichen.  —  *)  S.  Yt.  //.  32.  —  ?)  S,  V.  ig.  25.
•  j.,  g.  »vak- :rd^*-m.,f.'>'vCHc';l) 'Stimme';
1)  der  Menschen  (und  Götter)  'Stimme'
ohne   Rücksicht   auf  den   Inhalt  des  zu
Gehör  Gebrachten:  yasata  taota  ..btmi.-
gä'^rS  barxata  vaca  .  .  hs  vax^  us  ava
raoca   amaot  Yt/o.  89;  F.^^e;  —  *ama-
vala  vaca    F._je;    —  fra    staot^m    vaä
yesnltn  atar^mya  (sd.)  vaca  mrvyi  FiVi.
dby  Google
1333
'vak-  1  1
'vak- 4
1334
1. 1;  —  maiamya  vaca  frasrävayamnahe N,  20;  *26,  26,  33;  —  nitima  vaca  gäiiä srävayH  N.  27;  —  mt^rsm  ..yeiihe  vSxS gfmänahe  .  .  vi  Äafta  karhiqn  /asaiti yatcit  mmartka  vsHm  iaraiti  {Sp.  ^^sf.) yai  gaoi(sA.)ät  Yt/0.85;  73;  —  tmrr/S yS  parSäars  .  .  ä%rS  vScim  sururtaeiti FrW.  10.  41 ;  —  b»r3Z>m  barSi  zaota  välim Yt.  17. 61;  Y.  70.4,  Yt5. 123;  —  yat  bä faiti . .  näirikaca  apinnSyükasca .  .Janilm baraiti  väcim  V.J.  11;  —  yS  mq'hrä  (sd.) *vacim'''  ..  baraiti  V.  50.  6;  —  a^rä *väcim'''  baraitj  mihaAvacä  vä  *»n{.- vaeä  (sd.)  vä  Y.31.J2;  —  yeriAe /räyB (sd.)  sbaymtam  sraistfm  susruye  väHm Yt  i7. 1 7 ;  — *GS.  mit  
anhat  .  J    (yat)    gä%äsü    frasrävayaiti'-framruyi    varahraynX^ ai»ke  .  .  paiti.a%t!yäl    N.  ']2\\frava!ayS  stacmP  Yt.  y.
v»r>%rajqsttmS  artuxts  växf  yäAi  v)r>- 'hraJqstymS  Yt. //,  3;  Y.  7.  26;  —  ahu- nahe  vairyehe  arsuxhahe  "i'äj: /(statt GS.)" Y.  Ä  i;  —  *imqm  vacS  (AP.)  dnmjaySil ySi  ankin  vär)hrarjnyB.t»m>mca  baiiazy5J>- mptttla:  yd^ä  ahU  vairyS  V.  p.  z  7 ;'  2  8,  «y.  1 9 ;
—  imqm  gä^Tvyqm  vais  srävays'ü.  2.  20;
—  ha%ra  ana  gä^aiya  (sd.)  r'a«i  Ny.  4.  8, Y.  JO,  19;  65. 14;  —  *g3'äw3i//aai  *va^a^> P.  50;  —  ime  vaca  framrva  ysi  hanti gU%ähva  bisümrüta  (sÄ)  "^risämruta  (sd.) c'a'^ru/ämrata(sd.}  V.10.2;  if.,  5,  7,9,  11, 15-17,5.12,  rf.4,  77.5,  N.j.tf;  —yaica *alte  V  a  cB  apayaHH  ysi  h>nti . .  ^bi/ämrsta .  .  aSafiqm  vacqm  *aralufn^  'S. 33;  73;
—  aiwyS  zaoäirä  frabarsil  imq  vats framrü:    ^ap5   yärtjm    vS  ySsämi   .    '    Y.
65.  lof.;  8.  4,  N.  7/;   —   yas)   %wa  . .
pa%qm   (sd.)   jasäiti    va^waisö  .  .   a%a
imqm    valB  dnn/aygil  alba   imqm    val5
'aiäunqm  .  .
alte  zl
y3.  a)  der  Tiere:  m>rrfS  väcim  baraili '  vä^  (AP.)  vahisfa  ahurö  mazdä  främraot upa  uiäahpm  V.  /*,  1 5 ;  —  yasca  hi  .  .  \  zarakiuiträi  .  .  yeiai  zl  alte  väcS  usbme väcim  paiti  zamÜ  (sd.)  anhai  (näml.  |  urvaise  gayehe  framravai  .  .  Y.  7/.  14  £; der  Hund)  V. /j.  40;  —  vayqm  i'.scim  ;  Yt  15.  56;  —  vaca  (NP.)  mazdö.fraoxta susrusfmn5Yt.i4-2i-  3)  der  Peitsche:   mana  taya  .  .  ana  vaca  (IS.)  vanani   V.
yat  btnzim  barät  astra  väcim  Yt.  10. '  ig.g;  8f.3;  —  vaüs  mazdd.fraoxta  .  .  ySi 113.  2)  'Rede,  Wort   (als  Tätigkeits- 1  ^j«//    dusmatim   jayni^ta  .  .   vispanqmla
bezeichnung)':  hyatcümSi  hyat  vaxi also .aSaw^qm  vacqm  aojasca  vin^nmta  .. (Sp.  32  m.)    Y.44.17;    —  y?    anai£>m  yasamaide'^.ji.-}i.;'SyX.3g;  —  aita^ca  te
xsqnmJnl (sd.)  radpm  *vacim''>  mril  asu- rahyä  Y.2g.g;  —  ainiti/  aisff  *växs F.  26.  3)  'Rede,  Wort  (in  koU.  Sinn), (Plur.)  Worte':  fravasayS  . .  yi  masyehli ahmät  .  .  ya'ha    va^a  (IS.)  /ramraväire
'c5  ySi  pisimcit  sanm  (Sp.  898  o.)  bun- Jainii  YL/4-46;  46;  —  havaram  va!a ipa.staomi  Y.  lO.  2';  F.  8\  —  varatayanuha nana  vaca  Y.  ro.  5;  Vr.  Ä  r=;    —   ku-^^ra
'cd  aoübOia  (sd.)  *yqm  hE  iaxse  at^ra.-
(sd.)  Yt7J.  64;  —  nSit  dim  bitlm  väcim  paiti£\.6^.q;  —  kaha  zaota  xsäta  vaca faiti.p?r>simnB  bva  (Sp.  929  u.)  V.  18.  29 ; '  apB  .  .  yazaite  Y.  ^5.  9 ;  —  yasi  %wa  .  . —  a  dim  tä  vaca  rämayat  {sd.)V.ß.  21 ; —  rdhwya  vaca  yazaite  Yi.10.30;  31,  56; yezica  Aj  narö  irisia  kva  Aisva  uxh)m  —  yakmäi  zaota  ..mikrahe  vaca  yazäite vahm  ..paiti  dyatti  vlspanqm  vacam  Yt.  70.137;  —  vacqmca  vänikrayninqm uxoanqmca  .  .  hary^nm  barät  Vd.2;  ■ —  fraväkäi  Vr.75.3;  —  väca  humata  küxta yai  Alm  afm  *draogpm  väcim  arahat^lm  kvarita  ayese yeiti  Y.J.4;  Ji.  18;  —  mit änmäne  (sd,)  paiti  barata  Yt,  79. 33;  —  dem  Beiwort  ar/
dby  Google
»335
•vak- 5
vax»8ra-
1336
pars  vay&ibyö^'*  YLjo.88; —  *ao^rab}'B ariuxialibyasca  vSyiibyB^^  vufitn  .  . yazatitn  yasamaide  Y,i6.  i;  Vi.  6.  i,  Ny, J.  1 6;  —  Avamxiaft?m .  .yaxamaide  vacaca ^ao^naca  sao^rabyasca  N.1.16.  5)  Sing. JcaT*  K.  oder  mit  arsuxZa-,  miuxZa-  sva. mq'^ra-  (Sp.  1178  o.),  'das  Wort,  das wahlgesprochene  Wort':  yä^a  lia  väHm Milma  (Sp.  1067  o.)  ya'^a  vä  saoiyatits Y.  70. 4;  —  zara%uitrahe  .  .  yS  paoiryS vacim  aoxta  vldsyum  akurS.tkaistnt  Yt. y.go;  90;  —  ^TKuxlam  vacim  yat  frä- dai^gat^gm  yasamaide  S.  2.  iS'"';  G.  2.  6; —  uita  tl  nsii  pairi.frasa  (sd.)  >rpzuxhm *p?rgsahi  VäHm  Y.g.as.  6)  "Einzel- wort,  (Plur.)  Wörter'  uzw. 
KompA.  (vaxl'),  E.  —  Zum  V.  vai-.  —  at, väi-  f.  (vai,  väeä);  mp.  vä/  'leises  Gebet', i^/  B  mSriiän  'Satie  und  Wörter'  (F.  O; Tgl.  Zs.  4,  Dk.  8.  46.  1),  v3iak  'yak  stamn  i awaitä'  (SWienAW.  6/.  850.  16);  np.  äväz 'Stimme',  ävä  i  iöi  'Trommelgetön',  guväia 'Schelten';  a.  dazu  Hbm,  PSl.  104,  idq.  — P6,i  gdwün,  (lu  Y.  31,  V,  rS.  IS,  F.  ^  e i.Sl):  väng;  %.  noch  No.  5,  7-  —  "  So  wohl »icher  FtW.  /.  I.  -»)  So  Pl  4.  NA.s.üV>m.  — 3)  S  '94-  3.  —  <)  Wo  vajcs  hinter  m&aexto ausgefallen  isL  —  i)  Vgl.  die  öfter  wieder. kehrende  Erläuterung  lu  göwSn  in  Pü. :  apa- stak;  iB.  Y.  16.  1,  Ny.  /.  18.  —  6)
Denken,  Sprechen  und  Handeln ;  s.  No.  13.  — <i)  Fü.:  rehlL  DST.  ZA.  j.  124  meint,  es  seien die  Worte  aia.sara  manaaha  aSa.sara  vacaaka ajajara  fyas'i.na  damit  gemeint,  die  allerdings lu  N.  67  kurz  zuvor  litirt  sind.  —  MJ  Was ist  unter  den  "beiden  Worten'  oder  'Wörtern' lu  verstehen?  Pü.  (für  V  f):  apdi  giaiiniA fa  faliaäii  iiiämrül,
•  j.  vaiqm?
KompA.  —  AS.  zu  'vaiä-  f.  oder  Adv.
•  j.  *vakam.varay-*>  Adj.  —  ?  -:  •rBis' F.  Ä
Komp.  mit  AS.  oder  Adv.  im  1.  Glied.  — Pü. ;  n  dd  an  n  t  m  da  (^  vät  3p  'gereinigtes Wasser'?).  —  >)  Hds.  vaki^'ar*,  auch  das zweite  v  mit  dem  Anlaut szeicben.
•  j.  *vakqrn.sav-" ''  Adj.  —  ?  — ,  vom bilinstigenKamelhengst:  u/jya^f . .  *vaZair- yaol  'sat>/'>  aiwi.tacinahe  Yt.  14.11  ■
Komp.    mit    AS.    oder  Adv.  im   i.  Glied.  —
Npii, :  räA  ränanda  u  lüd  dihanda.  —  <)  So Pt  1 ;  F  I  htt  iiaiifiaos  mit  nachträglich  ein- gefügtem m.  NA.  düdqsaoi.  Dass  vai'  lu  lesen, gebt  aus  F.  ifhervor,  wo  aufi'aiai>nj™{richtig raiairyaiiS)  vaiquvarSi  folgt  —  ')  Oder  auch 'IUI;  Tgl.  daevd^iöii.
•  j.  vaf'dana-  n.  1}  'Kopf  uzw.  ahurischtr ;  Wesen'';  a)  des  Menschen:  nar^ maomyehe I  'Uim  F^a;  ^b,  V.5. 11,  (5.  aa;  —  pasca
j  hs  'mm  "hinten  auf  seinen  Kopf"  V,  8. 43, g.  16;  —  yat  ht  upfm  m  (sd.)  paiti  'nahe up?mat  varsa  hiku  bavatV.S.$B; — asne (sd.)  "nJ/  H.  2. 2;  —  bansnüm  hi  'mm pourum  "sein  Oberstes,  den  Vorderkopf V,i?.4o;  41;  —  ^baninvB  .  .  paiti  'nahe "zu  Oberst  des  Kopfes"  N.  6^.  b)  des Kamels:  ys  (nämL  uitrs)  kafim  aipi.- spaynti  . .  vpa  'mm  Yt  14. 13.  2)  'Kopf- stück, Oberstes'  (nur  Komp.).  Wertlos: tiamB  avi  xsmS  °rum  haha  urva  barmtt Vd.7.  [F.^g,  V.Ä43,  ().i6  i.St:  lies pasca.vayl':\
KompE.  — mp.  va-fijn,  wohl  gelW.  —  Et.?«.
—    Pu. ;    jiir,  virfiän.    —    ')   Im  Gegens.  zu
iam^rita-;  t.  H.  2.  z  und  20.  —  *)  Wertlos
ist  die  Zerlegung  in  'fai-  ('Stimme')  +d:
j.  vaxäl  N.  5/:  lies  vaxSät.
■  j.  vax^JIwa-  Adj.  'was  zu  sagen  is^:  huma-
töibyasca  hüxtöibyascä . .  mq^wBibyasca  (sd.)
'üwBilyas^a  Y.  //,  1 7 ;  —  datnayasca  mazäa-
yamöii  mq%wanqmca  (sd.)  'Itwanqmia  Vr.
12.  Z.
PFP.  zum  V,  vak-.  —  ai.  väiiva-  Adj.—  Pä.: pa  gffWÜHt
•  g.  vaxaSra-  n.  'Sprechen,  Rede':  hyat
dby  Google
'337
'vaxä-
•vaxS-
1338
```


## [2026-10-16T05:14:48.497Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'waxswar\\|vaxsvar\\|vaxSvar\\|vaxsur\\|vaxsür\\|vaxäür\\|waxsür\\|vax[sšS]u[rr]\\|vaxs[ßb]ar\\|xsvar' BRT.txt HRN.txt HUB.txt PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20"
}
```


### [2026-10-16T05:14:49.095Z] TOOL RESULT

```
HUB.txt:4420:vaxsUr = vuxmr 'Prophet' = phi. vaxSvar u. s. w.
HUB.txt:5797:nus? (oben p. 104); vaxsur ^Prophet' =- paz. vaxsur Shk.
HUB.txt:8334:raoxsna-- glanzend'; vaxsur 'Prophet' H. 1076; daxs 'Ge-
PHD_mackenzie.txt:7333:prescribed zamanig.                            prophethood waxswarih.
BRT.txt:27368:•  j.  sravanhav-  Adj.  'schleichend':  yi^a asayS  xsvarwäahö  ya%a  vS  vphrkiaAs 'ttkavs  V.iS.öS-
```


## [2026-10-16T05:14:52.139Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'waxšwar\\|waxsw\\|wxšwl\\|prophet' PHD_mackenzie.txt PHD.txt | head; sed -n 4410,4425p HUB.txt; sed -n 5790,5800p HUB.txt; grep -n '^ *1076\\.\\|^ *241\\.' HRN.txt"
}
```


### [2026-10-16T05:14:52.547Z] TOOL RESULT

```
PHD.txt:648:waxšwar 89 wénagih
PHD.txt:649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
PHD.txt:3254:prophet waxšwar; v. apostle.
PHD.txt:3255:prophethood waxšwarīh.
PHD.txt:5262:waxšwar
PHD_mackenzie.txt:5273:wax~war [whfwll N waxsur] prophet.
PHD_mackenzie.txt:5274: ......ih: prophethood.
PHD_mackenzie.txt:7332:   wirastan.                                   prophet wadwar; Y. apostle.
PHD_mackenzie.txt:7333:prescribed zamanig.                            prophethood waxswarih.
syr. mowed = np. mobad).
*) In der Kegel bleibt aber a bei Labialen.
*) Muwaffaq hat duvam *der zweite* 4, 16, 17; 5, 18 neben
say urn *der dritte' 263, 11, caharum *der vierte' 5, 9.
*) Anlaut. va- ist sonst zu ba- geworden.
*) So bei Sal. Shuk. p. 39, bei Vullers navad.
^) Aber np. nau *neu' = zd. nava- etc.- 127 -
b) Einigemal durch Assimilation an folgendes u :
ustux^an *Knochen', phi. astiix^'an zu zd. ast- 'Knochen ;
huzurg 'gross' aus ^h\,^vuzurk = *vazurk (§ 53) = ap. vazrka-;
vaxsUr = vuxmr 'Prophet' = phi. vaxSvar u. s. w.
c) einigemal nach Analogie?
ptixtan *koehen fiir *paxtan zum pras. pazam gebildet
nach dem Muster: hurdan'^): pras. baratn etc.?; kudam
'welcher, was fiir einer?' = paz. kaddm, skr. kalamd-
(vgl. zd. kataro = skr. katards) nach kuja wo?', vgl. paz.
ap. ?>r vor Yokalen = np. gu^ hi,
§ 55. Ap. V im Anlaut bleibt v bis ins Neupersische
in : vcij 'sprich !' (dialektisch), vaz *6emurmel, das leise Reci-
tiren religioser Formeln der Persei' (Noldeke, Tab. 353)
= phi. vac Gl. and Ind. 228, daneben haj bei Vullers;
vasama velum' (Vis u Kamm 856, 1 nach v. Stackelberg)
neben bascttna^ =■ arm. varsamak\ valdna *Wunde': lat. vol-
nus? (oben p. 104); vaxsur ^Prophet' =- paz. vaxsur Shk.
270, zd. "^vaxsahara- ; varj 'Grosse, Wiirde' = phi. varc Guj.
Abal. 73, skr. vdrcas- ; vardij ^Wachtel', skr. vdrtika-, var-
taka^; vary = bary *Wasserwehr, skr. varga- 'Abwehrer ;
2458:241. bih 'besser, gut', bihln.
9321:1076. veyiMür^ vu/sür 'Prophet' ).
11381:241. i^tnitan 'wegnehmen'; zlmtär (ZPGL). Selten.
```


## [2026-10-16T05:14:57.609Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 9315,9330p HRN.txt; echo ====; awk 'BEGIN{RS=\"\\f\"} NR==263' HRN.txt | head -60"
}
```


### [2026-10-16T05:14:57.876Z] TOOL RESULT

```
Exit code 1
Richtung zu bedeuten scheint), also eigentlich 'ab-
seits ; vergl. phlv. frarün.
1075. valäne, velane (so im Gazophylacium S. 389)
'Wunde*.
skr. rrand' Wunde* , wozu doch gewiss auch lat.
volmts^) gehört.
1076. veyiMür^ vu/sür 'Prophet' ).
phlv. va/sivar (Denkart); de Lagarde, Ges. Abh.
164 nimmt als Grundform aw. "^va/sahara- an (vergl.
va/sem möi asqsatj vd. 19, 15).
1077. vefif 'Grösse, Würde'.
aw. *tmrecah- in asvaredah-, varei^afihvanf- 'glanz-
reich, prangend*; phlv. varc bezw. varj, varcömamJ
bezw. varjömand (vergl. Salemann, Mel. asiat. IX,
235 Note 35); ai. vdrcas- 'Glanz.
Den von Salemann a. a. 0. citirten FirdüsT-Vers
(eval):1: === not found
```


## [2026-10-16T05:15:04.125Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==263' HRN.txt | head -30; echo '-----'; grep -n 'guväza\\|guvaza\\|guväz\\|äväz\\|äva \\|äwäz' HRN.txt | head"
}
```


### [2026-10-16T05:15:04.494Z] TOOL RESULT

```
— 241 -
Nicht hierher gehören die Suffixe -var in seriär
löwenhaft' (Sahn. I, 253 Vers 166) oder in selvär
(No. 789) u. a. m.
Das Suffix -awer (z. B. np. jengäwer) ist erst neu-
persisch.
1074. wäriin unglücklich, elend, schlecht*, tcärilne^).
phlv. apärün, aparumh.
Zusammengesetzt aus apa und phlv. rün (das 'Seite,
Richtung zu bedeuten scheint), also eigentlich 'ab-
seits ; vergl. phlv. frarün.
1075. valäne, velane (so im Gazophylacium S. 389)
'Wunde*.
skr. rrand' Wunde* , wozu doch gewiss auch lat.
volmts^) gehört.
1076. veyiMür^ vu/sür 'Prophet' ).
phlv. va/sivar (Denkart); de Lagarde, Ges. Abh.
164 nimmt als Grundform aw. "^va/sahara- an (vergl.
va/sem möi asqsatj vd. 19, 15).
1077. vefif 'Grösse, Würde'.
aw. *tmrecah- in asvaredah-, varei^afihvanf- 'glanz-
reich, prangend*; phlv. varc bezw. varj, varcömamJ
bezw. varjömand (vergl. Salemann, Mel. asiat. IX,
235 Note 35); ai. vdrcas- 'Glanz.
Den von Salemann a. a. 0. citirten FirdüsT-Vers
konnte mir Herr Dr. Landauer nicht nachweisen.
H Häufig mit wazün in den Handschriften verwechselt. Dieses,
sowie wäzüue ist sicher aus bäzyüne (Öähn. I, 197 Vers 1220) ent-
standen, rergl. cün etc. s. v. yün (No. 946).
2) tJber dieses Wort vergl. 0. Hoffmann, BB. XVIir, 291,292.
-----
915:54. üväz 'Stimme*, äväze, äväzlden,
3021:ap. pasa, 'hinter', pasäva 'nachher ; aw. pasda 'nach',
4698:äväz däden 'rufen', ferämös daden 'vergessen' u. v. a. m.
9286:guväze 'Schmähung*, gtwäSzden, schelten' (unbelegt).
14271:pasäva 315.
```


## [2026-10-16T05:15:07.882Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 912,925p HRN.txt; echo '-----'; sed -n 9278,9295p HRN.txt; echo '----'; awk 'BEGIN{RS=\"\\f\"} NR==285' HRN.txt | head -40"
}
```


### [2026-10-16T05:15:08.680Z] TOOL RESULT

```
'Raub, Beute*, ayarem 'rauben, plündern* (nach S. Bugge,
Indog. Forsch. I, 454 vielleicht statt ^anar aus gr.
svuQa; aber warum so gekünstelt?).
54. üväz 'Stimme*, äväze, äväzlden,
aw. ai. ä + [/^vac-, s. np. vaj (No. 1072) ; phlv. aväj
bzw. äväc 'Stimme , arm. LW. avaj\ avac,
afr. kurd. bei. LW. avüz,
55. ärverdeti (AM. ; im Reim Sahn. I, 4 Vers 66 ; heutige
>j Mittlerweile auch KZ. 32, 578, No. 3; vergl. auch F. Solmsen ,
KZ. 31, 472.- 14 -
Aussprache : äivtirden), Praes. äwerem^ är-em^ ätrertden ;
jüd.-pers. Bibelübersetzung: pTI2X neben TIIN.
ap. *^+|/6ar-; päz. äwardan, ätvurdan, äivar-am,
beL (LW. ?) ärag, n. aray, awarta (14).
-----
vergl. z. B. S. 82, Zeile 3 v. u.) ist Nachahmung des
arab. va und* oder dieses ist selbst entlehnt worden.
Oder gehört np. ü und' zu gr. av, got. auk etc.
(vergl. Kluge, Wörterbuch s.v. auch)? Man sollte
aber doch wohl eine Anknüpfung der Partikel im
iranischen Gebiete erwarten können.
wä *offen', siehe baz (No. 163).
1072. väj 'sprich', vergl. vat 'Wort, Rede' (dialektisch^),
guväze 'Schmähung*, gtwäSzden, schelten' (unbelegt).
g. vätrnun 'sprechen' (vergl. Justi, ZDM6. 36,
403, 404) ; Käs. Q. K. vöj^ 7j, vaz (s. v. f^eda kerden),
Käs. V. bivötdn, Impt. böj, Q. vötin, bavöten, Praes.
avöjün, K. vötmün^ Impt. hSvöJtd^ Z. bSvöt, Praes. vözön
'sprechen' (s. v. giiften).
aw. {/"vac-y vaocat 'sprechen' ; phlv. väöak 'Stimme',
väc (päz. väz) *Gebet'; ai. l/vac-^ vivakti, vdc- *Wort\
kurd. vdtin, vergl. bezium 'ich sage, spreche' etc.
(Justi, No. 408.)
----
A, A').
1. a-, a//-, un-, nicht-' (« privativumj. Sehr häulig, z. B.
asnr endlos*, a/^ar(i)sn *das Nichtessen , aguftar 'nicht
sprechend' u. v. m.
ap. a- in Anämaka' Monatsname (?) ; aw. a-, an- ;
ai. a-, an-; arm. aw- (H. No. 20).
oss. d. t. «-, ä- (1).
Das Neupersische hat a-, an- aufgegeben (Fälle wie
näb, oben No. 1015, und nägäh, oben No. 1021, sind ver-
einzelt) und ersetzt dieses Praefix durch vorgesetztes
nä' (oben No. 1014) , z. B. phlv. anspä$ 'undankbar
gegenüber np. näsipüs, oder durch be- (247).
2. afd 'trefflich; Wunder (AV., Men.), päz. awd,
np. tifde 'wunderbar , efdlden 'staunen, bewundern* sind
nicht belegt. Ist phlv. afd nur eine Umschreibung von
aw. abda- (vergl. abdötema-, Epitheton der Savanhaväc
und Erenavaö) und die np. Worte wiederum nur falsch
aus dem PehlevT transcribirt ? Der BQ und durch
diesen der PS enthalten eine Menge niemals im Neu-
persischen vorhanden gewesener PehlevT- und Päzend-
worte.
3. äfräH 'Mitteilung, Belehrung (Men.).
aw. ^afrasa-, vergl. paitifrasa', phlv. patfräs (oben
No. 154).
*) Die einzelnen Worte sind in diesem Abschnitt nach unserem
Alphabet angeordnet.
```


## [2026-10-16T05:15:12.312Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^.\\{0,3\\}263 -\\|- 263 -\\|— 263' HRN.txt; grep -n 'fur[oö]xtan\\|ferö/ten\\|ferö.ten\\|furöxtan\\|ferö' HRN.txt | head"
}
```


### [2026-10-16T05:15:12.667Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:15:15.435Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=282 && NR<=286 {print NR\": \"substr($0,1,80)}' HRN.txt; grep -n \"verkaufen\" HRN.txt | head"
}
```


### [2026-10-16T05:15:15.742Z] TOOL RESULT

```
282: 
283: VERLORENES SPRACHGÜT.
284: 
285: A, A').
1. a-, a//-, un-, nicht-' (« privativumj. Sehr häulig, z. B.
asnr endlos
286: - 264 —
4. afsTultan Vernichten; abnehmen', awsiuitan, afstn-
(i)sn.
Scheint ein
7176:kurd. LW. frütm, difrüsim 'verkaufen'; af/. prölal,
7177:prövul; bei. savaskay, söskay 'verkaufen', p. p. §ava/fa
7182:np. /enden ('kaufen und verkaufen*) entstanden die
```


## [2026-10-16T05:15:19.240Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7160,7185p HRN.txt"
}
```


### [2026-10-16T05:15:19.629Z] TOOL RESULT

```
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
```


## [2026-10-16T05:15:23.483Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -7171 HRN.txt | tr -cd '\\f' | wc -c; grep -n 'frox\\|fröx\\|frōx\\|frōš\\|frox-' PHD.txt | head -5; grep -n -i 'frōxtan\\|froxtan\\|frōš' CHEUNG.txt | head"
}
```


### [2026-10-16T05:15:23.865Z] TOOL RESULT

```
204
3913:sweetmeat royn-xwardig; afrōšag, gēzēnag, lawzénag, Šiftēnag, watrēnag.
20795:|| (+ *abi-) NP afroxtan/afroz- ‘to set alight, kindle’ || (+ *fra-) NP furöxtan/furöz- 
40693:afroxtan/afroz-, 316
```


## [2026-10-16T05:15:30.896Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"to sell\" CHEUNG.txt | head; grep -n \"^\\*\\(u̯\\|w\\|u\\)a[cč]\\|\\*u̯ac\\|\\*waxš\\|\\*u̯axš\" CHEUNG.txt | head"
}
```


### [2026-10-16T05:15:31.206Z] TOOL RESULT

```
2517:*NEIR: Yzgh. vas-/vast ‘to sell’ 
3987:*SOGDIAN: (+ *para-) SSogd. pr'ó, BSogd. pr'yó, CSogd. pry@ ‘to sell’, BSogd. 
3995:*CHORESMIAN: (+ *para-) p’rö- ‘to sell’ = Samadi: 137 
3997:*BACTRIAN: àa- ‘to give, assign, grant, allot, assign’ || (+ *para-) napaña- ‘to sell’ 
4019:M. polör-/parist-, Y ghn. pirónt-/pirónta- ‘to sell’ 
4021:*MISC: Par. dah-/dä ‘to give’ || (+ *para-) Orm. pray-/prak/, pra-/prawak ‘to sell’ = 
9361:‘to bring, sacrifice’, ON selja, OE sellan ‘to hand over, sell’, Engl. to sell, etc. 
12735:child); to build’ || (+ *para-) Yghn. piront-, Wa. рыгыпа-/рогоі- ‘to sell’. Ф The 
19181:aged by Bailey, l.c., i.e. Pokorny: 817: ‘to sell, assign’ is semantically impossible. 
27727:(caus.) “to light a fire’ || (+ *fra-) ? MMP frwxs- ‘to sell’. 0 The verb ВМР whs- is 
57953:*uac, *zrad
```


## [2026-10-16T05:15:34.171Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27700,27745p CHEUNG.txt; grep -n '^\\*u[aā]c\\|^\\*uac\\|^\\*u̯ac\\|\\*ua[cč]1\\|^\\*uak' CHEUNG.txt | head"
}
```


### [2026-10-16T05:15:34.498Z] TOOL RESULT

```
*SANSKRIT: vat ‘to appropriate spiritually’ (RV+) = EWAia П: 494 

«PIE *uet- ‘to be informed, acquainted’ — LIV: 694 | Pok.: 346 

*IE COGNATES: Olrish fethid ‘notices, expects’ 


*REFERENCES: DKS: 498a f.; Sims-Williams 1985: 96 ad 26; Abaev, Slovar’ IV: 6 f.; Werba 1997: 232; 
Cheung 2002: 233; NEVP: 12 


*uaxš ‘to grow; increase’ 

*AVESTAN: vaxs- ‘to grow’ || (+ *abi-) ‘to let grow, spoke (the fire)’ || (+ *uz-) ‘to 
grow up(wards)’ || (+ *fra-) ‘to grow forth’ = Liste: 48 

Pres. them. ja-: IND. 3sg. OAv. uxsileiti (Y 44.3), YAv. uxsüeiti (Y 10.6, Yt 7.2, Yt 8.43, etc.), ҮАУ. 
uzuxsiieiti (Yt 6.2 f., Yt 7.4, Ny 1.12, etc.), 3pl. YAv. uzuxsiüieinti (Yt 13.10, Yt 13.14), INJ. 2sg. OAv. 
uxsiio (Y 31.7), 3pl. YAv. uxsin (Yt 13.93, Yt 17.18), SUBJ. 3pl. YAv. fra uxsiian (V 5.12 f., V 8.9 £); 
Fut.: med. 3pl. ? YAv. vaxsiiente (Yt 8.42); Aor. athem.: INJ. 3sg. vaxst (Y 34.11, Vr 12.4), SUBJ. 3sg. 
OAv. vaxsat (Y 31.6, Y 48.1, Y 48.6), med. 3pl. OAv. vaxsonte (Y 32.4), OPT. med. 1sg. OAv. uxsiia (Y 
33.10); Partic.: pres. YAv. uzuxSiiant- (V 18.63), med. YAv. uzuxsiiamna- (Yt 4.8); Caus.: IND. 3du. 
Y Av. vaxsaiiato (Y 10.3), SUBJ. 3sg. ҮАУ. aißi.uuaxsaiiät (N 73), ОРТ. 35р. Y Av. aifi.vaxsaiioit (N 81). 
© Kellens – Рігаг 1991: 106 interpret OAv. uxsiia differently: pres. IND. 1sg. 

*MIDDLE PERSIAN: BMP whs- /waxs-/ ‘to grow; to blaze’, BMP whsyn- /waxsen-/ 
(caus.) “to light a fire’ || (+ *fra-) ? MMP frwxs- ‘to sell’. 0 The verb ВМР whs- is 
always used in connection with "twr/'dwr ‘fire’. Several semantic shifts need to be 
assumed for MMP frwxs-, not all of which are evident: **to grow’ > *‘to prosper’ > 
*'to prosper through trade’ > *‘to sell’. = DMMPP: 158a 

Pres.: IND. 1sg. BMP whsym /waxsém/, 3sg. BMP whsyt /waxséd/, 3р1. BMP whsynd /waxsend/ ‘(the 
fires of plwb’g and gwsnsp) are blazing’; Partic.: perf. pass. BMP whsyt /waxsid/, BMP whsytk 
/waxSidag/; Caus.: pres. IND. 3sg. BMP whsynyt /waxsénéd/; Inf.: BMP whsytn /waxsidan/ ‘to grow’, 
caus. BMP whsynytn /waxsénidan/ || (+ *fra-) Pres.: IND. 3sg. MMP frwxsyd 

*PARTHIAN: 1. wxs- ‘to grow’ || 2. wxs- ‘to be kindled, blaze; to kindle? = Ghilain: 
59 | DMMPP: 349b 

1. Partic.: pres. wxsg || 2. Pres.: IND. 35р. wxsyd, 1р1]. wxs^m, 3р1. wxšynd, SUBJ. 3sg. wxs’; Partic.: 
pres. wxSyndg 

*KHOTANESE: hus(s)- ‘to grow’ = SGS: 154 

*SOGDIAN: CSogd. xws- ‘to grow, grow up, become full-grown’ 
57953:*uac, *zrad
```


## [2026-10-16T05:15:39.395Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^\\*ua[cč] \\|^\\*uac\\b\\|^\\*uač' CHEUNG.txt | head; grep -n \"‘to speak\" CHEUNG.txt | head"
}
```


### [2026-10-16T05:15:39.826Z] TOOL RESULT

```
57953:*uac, *zrad 
1571:abhandana-’. Ф The comparison of Khot. ban- to Skt. bhan? ‘to speak’, cited in SGS: 
1573:presumed shift from ‘to speak’ to ‘to cry out, lament’ needs an explanation, having 
3038:ptskwy ‘to speak, say’ || (+ *ui-) CSogd. wyc’w’, CSogd. wyc’wyt ‘martyr(s)’, 
5261:*MIDDLE PERSIAN: BMP dw- /daw-/ ‘to speak [daevic]' (< Av. ?) 
5265:*NWIR: Kurd. (Sor.) duwan/dü-, diwan/diwé- ‘to speak, talk’, Awrom. duay/du- ‘to 
5274:derivation from Av ‘du ‘to speak (daevic)’ ... is misplaced. MK]". 
6022:*NWIR: ? NP darayidan ‘to speak aloud, call’ (alternatively < *zräd) 
6516:*far? ? ‘to speak’ 
6518:*KHOTANESE: LKh. pher- (denomin.) ‘to speak’, pharä- ‘speech, language’ (SVK II: 
6525:9 The evidence for an Ir. root *far ‘to speak’ (only EIr.) is limited, with may suggest
```


## [2026-10-16T05:15:43.298Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^\\*u[aā]c\\|^\\*uac\\|uac ‘to\\|uaé\\|^\\*uat\" CHEUNG.txt | head; grep -n \"w'c\\|wāxtan\\|wāz-\\|vaxtan\" CHEUNG.txt | head"
}
```


### [2026-10-16T05:15:43.797Z] TOOL RESULT

```
13540:*(H)uaé ‘to let go, release’ 
13619:derivation from *(H)uaé ‘to leave behind, let’ or *uaz “to drive (a chariot)’ for w’zy- 
18184:OAv. mrüite (Y 49.6), Y Av. framrüite (Y 8.4, ? N 71). 0 On the attested forms with *ni- cf. *ni-uac ‘to 
26739:impf. 3sg. Y Av. pairi.auuaénat (Yt 5.68), INJ. 1sg. YAv. paiti.vaenom (Yt 7.3, Ny 3.5), 3sg. YAv. vaenat 
26744:Inf.: pres. OAv. уаёпађћг (Y 32.10). © The initial a^ of OAv. auuaéna is the result of shortening in front 
27627:*uat 427 
27669:*uat ‘to inspire, be informed, acquainted’ 
28181:*AVESTAN: YAv. uruuaöö- ‘to blame, condemn ?’, “uruuaédam (Asg f.) ‘blame, 
28195:urvaéd- ‘stürzen’), viz. Е 450 f. “uruuaédam and *uruuiöiieiti. These forms are 
28238:*AVESTAN: YAv. uruuaés- ‘to twist, turn’ || (+ *abi-) ‘to turn to’ || (+ *aua-) ‘to turn 
13542:*SOGDIAN: SSogd. w’c ‘to let go, send (off)’, BSogd. w'c, CSogd. w’c, MSogd. w'c 
26178:*MIDDLE PERSIAN: MMP w’c, w z, ВМР w'c /waz/ ‘word, speech’ || (+ *abi-) BMP 
26188:*PARTHIAN: w’c- ‘to say, talk’ || (+ *a-) ”’w’c- ‘to call’ || (+ *pati-) pdw'c- ‘to 
26192:Pres.: IND. 1sg. w’c’m, 25р. w’cyh, 3sg. w’cyd, 2р1. w'cyd, 3р1. w’cynd, SUBJ. 15р. w’c’n, 2sg. wich, 
26193:IMPV. 2р1. w'cyd, OPT. *w’cyndyh; Partic.: perf. pass. w’xt, II w’c’d; Inf.: w’xtn, w’xt || (+ *a-) Pres.: 
26194:IND. 3pl. *""w'cynd || (+ *pati-) Pres.: IND. 35р. "pdw'cyd, 2pl. pdw'cyd, SUBJ. 2sg. pdw’c’h, IMPV. 
26195:2sg. pdw’c, 2pl. pdw'cyd; Partic.: perf. pass. II pdw'c'd || (+ *ni-) Pres.: IMPV. 2pl. nw’cyd; Partic.: perf. 
26233:navaxtan/navaz- ‘to caress; treat with kindness’; to play (an instrument)’ 
28005:*MIDDLE PERSIAN: ВМР w'c- / waz-/ ‘to play’, BMP w’cyk /wazig/ ‘game, play’ 
28006:Partic.: perf. pass. BMP w’cyt/wazid/; Inf.: BMP w'cytn /wazidan/
```


## [2026-10-16T05:15:46.522Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 26150,26260p CHEUNG.txt"
}
```


### [2026-10-16T05:15:46.864Z] TOOL RESULT

```
*REFERENCES: EVP: 9; IIFL I: 255a, 395b, 405a; IIFL II: 261a, 535a; Bailey 1936: 344; Andreev — 
PeSéereva: 352; EVS: 89a, 60a; WIM I: 66; Abaev, Slovar' IV: 40; Werba 1997: 418 f; 


Steblin-Kamenskij 1999: 284 f, 455; Lecoq 2002: 121, 126; Kiefer 2003: 197; NEVP: 12, 67; 
Shahbakhsh: s.v. gwap-; Korn 2005: 99, 398 (passim) 


*uaá ‘to say, speak’ 
*AVESTAN: vaoc- (väc-) ‘to say’ || (+ *4-) ‘to say to’ || (+ *fra-) ‘to proclaim’ 
c» Liste: 48f. 


*yad 403 


Fut.: IND. 15р. OAv. vaxsiia (Y 30.1, Y 46.15, Y 51.8), med. 35р. YAv. frauuaxsiieite (Vr 15.3); Aor. 
them. red.: IND. Isg. them. YAv. frauuaocami (Nat 46, Vyt 52), 1р1. ? OAv. ()Jauuaocama (Y 38.5), INJ. 
1sg. YAv. frauuaocam (Y 19.3), 2sg. YAv. frauuaocö (Y 19.1), 3sg. OAv. vaocat (Y 29.6, Y 34.10, Y 
45.3), 1р1. OAv. frauuaocama (Y 35.9), YAv. frauuaocama (Y 70.2, Vyt 13, Vyt 20, etc.), ? OAv. 
auuaocamä (Y 38.5), SUBJ. lsg. OAv. vaoca? (Y 45.3), 35р. vaocat (Y 31.6, V 8.11, V 15.13), OPT. 3sg. 
Y Av. vaocöit (V 4.46), 1р1. OAv. à vaocoima? (Y 35.3), IMPV. 25р. OAv. vaoca, 2pl. YAv. vaocata (P 
16, P 38); Perf.: IND. 2sg. YAv. vauuaxóa (F 8), 3sg. YAv. vauuaca (Y 19.9, Yt 13.90), med. 3sg. YAv. 
vaoce, 3du. YAv. vaocatard (Y 13.4), 1р1. OAv. vaoxomä (Y 34.5); Partic.: perf. YAv. vaokus- (Yt 
13.88), perf. pass. uxóa- (Y 32.9, Y 33.14, Y 45.8, etc.); Inf.: aor. OAv. vaocanhé (Y 28.11); Pass.: aor. 
IND. 35р. OAv. auuäci(Y 36.6), INJ. 35р. OAv. vaci (Y 43.13), IMPV. 35р. OAv. ücam (Y 48.9). 0 The 
past participle uxóa- can also belong to the root *Hauj. 

*MIDDLE PERSIAN: MMP w’c, w z, ВМР w'c /waz/ ‘word, speech’ || (+ *abi-) BMP 
’yw’c, ’dw’c /ewaz/ ‘word, utterance’ || (+ *a-) MMP ’w’c- ‘to call’, MMP ’’w’g 
‘voice, speech’, BMP ’p’c /awaz/ ‘sound, voice, language’ || (+ *pati-) MMP 
pyw’c-, BMP ptw’c- /paywaz-/ ‘to answer’ || (+ *ni-) MMP nw’cysn ‘kind 
utterance; honouring; hospitality ?°, MMP nw’g ‘melody, tune? = DMMPP: 333b, 
64b, 291a, 5b, 246a f. 

(+ *а-) Pres.: IND. 3pl. MMP ’w’cynd || (+ *pati-) Pres.: IND. 3sg. MMP pyw’cyd-, IMPV. 2sg. MMP 
pyw’c 

*PARTHIAN: w’c- ‘to say, talk’ || (+ *a-) ”’w’c- ‘to call’ || (+ *pati-) pdw'c- ‘to 
answer’ || (+ *ni-) nw’c- ‘to speak kindly to, treat kindly, honour’, nw’g ‘melody’ 
c» Ghilain: 68 | DMMPP: 333b f., 5, 271a, 246a 

Pres.: IND. 1sg. w’c’m, 25р. w’cyh, 3sg. w’cyd, 2р1. w'cyd, 3р1. w’cynd, SUBJ. 15р. w’c’n, 2sg. wich, 
IMPV. 2р1. w'cyd, OPT. *w’cyndyh; Partic.: perf. pass. w’xt, II w’c’d; Inf.: w’xtn, w’xt || (+ *a-) Pres.: 
IND. 3pl. *""w'cynd || (+ *pati-) Pres.: IND. 35р. "pdw'cyd, 2pl. pdw'cyd, SUBJ. 2sg. pdw’c’h, IMPV. 
2sg. pdw’c, 2pl. pdw'cyd; Partic.: perf. pass. II pdw'c'd || (+ *ni-) Pres.: IMPV. 2pl. nw’cyd; Partic.: perf. 
pass. II nw’cyd 

*KHOTANESE: LKh. vamjamayyau ‘dispute’ {hapax} || (+ *pati-) pyumj- ‘to deny’ || 
(+ *ш-) ОК. byüj- ‘to abuse’ = SGS: 87, 105 

*SOGDIAN: BSogd. wxs-, MSogd. wxs- (pass./inch.) ‘to be said, mentioned’ || (+ 
*us-fra-a-) CSogd. sfr’cy (m.) ‘speech, word’ (cf. Schwartz 1967: 126) || (+ *pari-) 
BSogd. prw’’c- ‘to slander’ 

Pres.: IND. 35р. BSogd. wxsty, MSogd. “wxstyy (Kaw.: 74); Pret.: tr. IND. 3sg. SSogd. wytw ö’rt, 3pl. 
SSogd. wytw 6’r’nt, Partic.: perf. pass. SSogd. wyt, MSogd. wyt’k; Inf.: pret. MSogd. wytyy || (+ *pari-) 
Pres.: IND. 3sg. BSogd. prw’’ct 

*CHORESMIAN: ws- ‘to say, speak’. 0 The seemingly endingless impf. ws is perhaps 
a generalized allegroform (Skjarve apud Samadi, l.c.). = Samadi: 219 

*BACTRIAN: (+ *pati-) лібооос- (orig. caus.) ‘to declare, make a declaration or 
contract” = S-W, Bact.: 218b 

*NWIR: Widely attested: Bal. gwast/gwas-, Zaz. vatis/van-, Abyan. vatan, Anar. 
-Iwat/ewoj-, Awrom. watáy/wac-, Fariz. -vät-/-väj-, Yar. -vat-/-vaj-, Gz. va-/vat, 
Gur. (Kand.) vat-/-(v)ac-, Ham. vatän/va-, Isfah. vatän/va-, Jow. bam-vot/ a-vod3- 


404 *uadH 


(also supplet. aggor- < *ham-Hgar-), Meim. bem-va/a-vod3-, Khuns. vaZ-/vat, Mah. 
vätän/väj-, Nn. väte/väj-, Natan. -vat-/vaj-, Qohr. vata/vaj-, Sang. -vät-/vän-, Siv. 
vas-/vat, Soi vat-/a-voj-, Sorkh. -vät-/ (subj.) -vaZ- (ind. supplet. (de)nomin. ván- ?), 
Lasg. -vát-/ (ind. supplet. (de)nomin. ván-) ‘to speak’, Zaz. vaziyayis/vaZin- (caus. 
-iter. ?) ‘to scold at’, Bal. gwänjat/gwänjan- (denom.) ‘to cause to sound’, NP bang, 
Kurd. bang (m.), Zaz. veng (m.) ‘voice’, Siv. vang ‘scream’, Bal. gwank ‘voice’ 
(LW ?) || (+ *anu- ?) NP (Tadj.) nawoxtan ‘to curse’ || (+ *a-) NP avazidan ‘to cry 
out, make a noise, vociferate’, Kurd. (Kurm.) axaftin, axavtin/axev-, axaftin, axaftin/ 
axiv-, (Sor.) axaftin, axawtin/axew- ‘to announce, speak, tell, converse’ (with meta- 
thesis: *u ... x > x... f/v/w), NP avazah ‘voice, sound, loud talk? || (+ *ni-) NP 
navaxtan/navaz- ‘to caress; treat with kindness’; to play (an instrument)’ 

*NEIR: Sh. wäy-/wäyd, Sarig. woy-/woyd, Yzgh. way-/wüyd, Wa. way-/wayd- ‘to 
cry, roar, scream’ (early LW), Wa. woy-/woyd-, Ishk. bay-, voy-, M. bey- ‘to roar’ 
(LW), Oss. І. wac, D. wace “message, news; deity, divine, holy’ || (+ *anu- ?) Yzgh. 
nowaz-/nowext ‘to swear, curse’ (< NP Tadj.) || (+ *4-) Sariq. awuj ‘voice, sound’ (< 
early Pers. ?), ? Wa. awöy ‘voice, sound’ (< Sariq. ?) 

*MISC: Огт. yus-/yok, ywac-/ywek ‘to say, speak’ = -803-/-gök, Par. yax ‘voice, 
sound' 

*SANSKRIT: vac ‘to speak, tell, say, call’ (RV+) = EWAia II: 489 

«PIE *uek”- ‘to speak, to say’ > LIV: 673 f. | Pok.: 1135 ff. 

*IE COGNATES: Gr. etmetv (aor.) ‘to speak, to say’, Olrish foccul ‘word’, MHG 
gewahenen ‘to mention, tell’, ON vättr ‘witness’, etc. 

*REFERENCES: KPF I: 84a, 146a f., 249a Ё; Ivanow 1926: 420; IIFL I: 258a, 396a; KPF II: 221 f.; 
Christensen, Contributions I: 172 f., 263; Christensen, Contributions II: 63, 118; Abrahamian 1936: 123, 
133; Lambton 1938: 42b, 77b, 78b; MacKenzie 1966: 112; Gershevitch 1971: 279 Ё; EVS: 16b, 89; 
Lecoq 1974: 60; WIM I: 73; Lecoq 1979: 348; WIM II/1; WIM III: 118, 348; Abaev, Slovar’ IV: 26 ff.; 
Werba 1997: 397; Paul 1998: 316b; Steblin-Kamenskij 1999: 386, 390; Cabolov 2001: 99 f., 149; Cheung 


2002: 235 f.; Lecoq 2002: 176, 179 (passim); Kiefer 2003: 198; Shahbakhsh: s.v. gwas-, gwanjan-; Kom 
2005: 137, 317, 398
```


## [2026-10-16T05:15:51.855Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o '.\\{0,10\\}\\(wāng\\|wang \\|bāng\\|nawāg\\|hunīyāg\\|huniyāg\\|hunyāg\\|āwāz\\|frōxtan\\|frōš\\|wāzag\\|gōwāz\\|hūxt\\|nwāz\\|nawāz\\).\\{0,160\\}' PHD.txt | head -30"
}
```


### [2026-10-16T05:15:52.355Z] TOOL RESULT

```
122:add \Ahliswang |*hlygwng] = Ard. delete Khriswang ... for alum ... read „alum |? № | N <] millet. Vāsnūd(ag) ... delete noble. aswür [|PR/LSYA < A pršy';.. āšnāg ... add acqua
261:borz-wang [bwlcw’ng] loud. ~iha [-уА?] aloud.
605:pe, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
649:. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trad
705:šnām, wad-wāzag.
773:aloud borzwāngīhā.
1546:delight huniyāgīh, urwahm(an)ih.
1776:tertainer huniyāgar.
1777:rtainment huniyāgih.
2218:ken društ-āwāz | -ēwāz.
2238:ng (a.) āšnawāg.
2239:ng (n.) āšnawāgīha, āšnawišn, niyo(x)šišn.
3441:yūmand, tuwāngar, was-xwāstag.
3442:ichness tuwāngarīh; v. wealth.
3913:xwardig; afrōšag, gēzēnag, lawzénag, Šiftēnag, watrēnag.
4239:voice āwāz, wüng.
4286:ngadīh, tuwāngarīh, xwastag.
4496:tuwānīg tuwāngar tuwāngarīh tuwān tuwānsāmān tambūr tambūrag did!, tand, tang tandih, tangih tanigardig tanigard tan
4681:- PO o parwāngāh 595 ep o parwanagih ^5 e» Ф parwanag 13 ? o frawār, parwāl M o frawār-, parwāl- ANN CH parwālišn e» O frawārdan wed > оу franàm- - PO v franāmišn Irv’ > vo p
5109:st wad wadwāzag widang wadkāmagīh wadkāmag wadagīh wadag wider- widarag L2pày- 1-2радап! widardan widest
5292:wiyābāngarīh Ss эү” GUI
5356:w dz društāwāz društīh društ
5423:dušhūxt
```


## [2026-10-16T05:15:58.462Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'huniy\\|hunyā\\|^h[uū]xt\\|frōxtan\\|froxtan\\|frōs\\b\\|nawāg\\|nawag \\|āwāz \\[\\|ãwãz\\|awaz \\[\\|w[aā]ng \\[\\|w[aā]z \\[\\|wāzag' PHD_mackenzie.txt | head -30"
}
```


### [2026-10-16T05:15:58.820Z] TOOL RESULT

```
501:add v.Ahliiwang [' hlyswng] = Ard.
819:abroxtan, abrl>z- [lplwhtn', )plwe- I M )brwxt, 'brwc-, N afroxtan,
1274:Asnawag [)!nw)k' I M '!nw'g, N lunawa] hearing•
1586:borz-wang [btvlcw)ng] loud.
2094:  .....-awaz, -..-ewaz [-)p)c, ~)yw)c] harsh-spoken.
2255:lewAz [)yw)c] word,        utterance.
2256:lewAz [)yw)c] sole, only.
2404:froxtan, fro(x)s- [MZBNW-tn l < A mzbn, ...; zbn I M prwxl-, N
2905:hi)                                44                       huniyagih
2941:  ---ewaz [-)yw)c] of good speech, affable.
2960:huniyag [hllmyd)k l , N xun)O(l] delightful.
2962:huniyi'll1ar                        45                            im roz
2963:huniyi~ar [/mmyd)kll N xU1Jyagar] entertainer, musician.
4069:parwaz [plw'c IN ......] flight.
5168:wang [KALA < A ql'; w)ng I = M, N bang] voice, cry.
5289:waz [w)e I = M, (N haJ)] word, speech; 'grace' (before meals).
6012:attentive huniyoxs.                      basis miidayan, padisar.
6375:delight huniyiigih, urwahm(an)ih.          detriment (astr.) petyiirag.
6376:delightful huniyiig.                       devil dew.
6474:easy asan, sabuk, xwar.                      entertainer huniyagar.
6475:eat xwardan; cause to ,....., xwaren-.       entertainment huniyagih.
7109:Mithra Mihr.                                   musician huniyagar.
7545:sell froxtan.                             sheepfold, -pen pahast.
9149:marzangos             "'\\,.-, ~    froxtan I
12017:huniyagih                ~yd\'"                hangirdcn-                -~~t'"
12018:huniyag                     \~\t"              hangirdcnidan           "~"'~t"'
12019:huniyagar                  \.Y'U',....         hangirdigih             "U ~~.. t»
12022:huniyoxs                 ~ta.t\l""             xwistan                   \\\UVl""
```


## [2026-10-16T05:16:06.281Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'waxšwar\\|vaxšvar\\|waxsvar\\|vaxsvar\\|hunīy\\|hunīāk\\|hunyāk\\|frōxt\\|frōxtan\\|vāng\\|wāng\\|āvāč\\|āwāč\\|vāčak\\|vāžak\\|vāč\\b\\|hūxt' NYB_vol2_glossary.txt | head -30"
}
```


### [2026-10-16T05:16:06.584Z] TOOL RESULT

```
1044:burtan [bwltn'; YBLWN-, YDLWN-tn'; forms v. I, 178] bar-, to carry, to bring, to bear, to wear, to procure; to take away, to remove (6 or pat ‘to’); arišk ~ to bear envy 691. 8419; !a&, bes, dast, dašn, gobišn, nam, namāc, nipart, paitäk, srav, stēžak, vāng, pat xrat ~: v. these ws.; bahr ~ v. barišneh; — to place on the top of (apar) 444; to lay a p. on (6) 4720-21; — andar 6 tan ~ to bring into corporeal existence 92t; — andarg ~, v. göbisn; — apar ~ to send out against 3711; to bring 6016; dmdcisn apar ~ to give instruction, to teach 80%; v. also apar-barisneh and apar-burtäreh ; — frac ~ to bring, to present 411; to bring forth, to light (a fire) 44°; — fröt ~ to bring down, to shed (water) 417°; v. also fröt- barišneh; — 6 ham ~ to collect, to amass 4815; pret. construed as an act. 187% Common Iranian; Av. OP (933 sqq.) also — (act. and middle) ‘to ride’, cf barak and asvār; cf also apar-barišneh from bar- ‘to move’.
1394:duš-hūxt [dwšhwht'] evil speech 63°’. 6510; Evil Speech, the second stage down to Hell 7524, — The negative of hüxt (q. v.). Av. (756 sq.) duž-ūxta-; Paz. dūžūst corresponding to Phl *dusüzt. duš-kām-kartārēh [dwSk’mkrt’lyh] bad exercise of authority, outrage, violence 7211. — Cf kam.
2089:"huvaršt [hwwlšt'] what is well done, good deeds, the third and last station preced- ing Paradise 632%. 7316-27, 8916, 1209, cf humat and hūxt. — Borrowed from Av. (1850) hvarsta-, ci varzitan.
4057:vaxšvarčh prophethood 454-7,
5144:dvar-: dar duš-mainyu-: duš-mčn du$-manah-: duš-man duš-mata-: duš-mat duš-x"aronah-: duš- xUarr(ah) dužda.fedrē: dušdaft duž-dačna-: dus-dén duz-däy-: duž, dužd duž-vacah-: duš-gobišn duž-varšta-: duš-huvaršt duž-ūxta-: duš-hūxt dvaēšah, tbaēšah: 'bēš dvar-, dvāristan
```


## [2026-10-16T05:16:10.632Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4050,4060p NYB_vol2_glossary.txt | cut -c1-600; grep -n '^hūxt\\|^\"hūxt\\|^hūxt\\|hūxt \\[' NYB_vol2_glossary.txt | head; grep -n '^vāng\\|^vāč\\|^vāžak\\|^vāčak\\|^āvāč\\|^āvāz\\|^hunī\\|^frōxt\\|^frōš\\|^navāk\\|^vāž' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-16T05:16:11.212Z] TOOL RESULT

```
?vaxš [whš] flame, blaze 3718, with the gl. han i ātaxš paitak rošneh. — V. *vax- šitan.
vaxščnitan [whšynytn'] to light a fire 3722.23, — Caus. of 2vaxsitan.
vaxšišn [whššn'] growth 89%. — From loaxsitan.
vaxšišneh det. v. n. of *vaxšītan: ul ~ the flaming up, the shining forth, of the dawn 44!?,
lyaxšitan to grow 40". — Av. (1337 sq.) Iyaxs-, v. also varšišn.
2vaxSitan to flame, to blaze 1%, — Av. (1338) *vaxš- ‘to sparkle’ (of fire), ‘to spurt’ (of water); MPrth was ‘to be kindled, blaze’ (MHC); v. ?vax$, vaxšiš- néh, vaxsénitan.
vaxš-var [whšwl] prophet 1115. — ‘Bearer of the Word, or the (divine) message’, v. lvaxš.
vaxšvarčh prophethood 454-7,
vāyēndak [w'yndk'] flying creature, pl. cas. obl. —-än, enumerated after murvān 802. — Pres. pt. of Av. (1356) Wvay- ‘to fly’.
vizčnitan [w’cynytn'] to bring, to take a p. to a place (andar) 49?’; to lead (a horse) up to (0) a p. 5413-15; à tē pat ulēh ul vāzēnēm we shall carry thee up in the air 60%. — Caus. of väzitan.
vāzēnītār one who draws, pulls: asp i rahy ~ a chariot-horse 581”.
1394:duš-hūxt [dwšhwht'] evil speech 63°’. 6510; Evil Speech, the second stage down to Hell 7524, — The negative of hüxt (q. v.). Av. (756 sq.) duž-ūxta-; Paz. dūžūst corresponding to Phl *dusüzt. duš-kām-kartārēh [dwSk’mkrt’lyh] bad exercise of authority, outrage, violence 7211. — Cf kam.
```


## [2026-10-16T05:16:14.369Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^1vaxš\\|^lvaxš\\|^Ivaxš\\|vaxš \\[' NYB_vol2_glossary.txt | head; grep -n 'hūxt\\b' NYB_vol2_glossary.txt | head -5; grep -n -i 'vāng\\b\\|vāng \\[' NYB_vol2_glossary.txt | head -5"
}
```


### [2026-10-16T05:16:14.707Z] TOOL RESULT

```
1022:Brātarūrēš [bl’tIwkly$] n. pr. 5022, 5112.20, 5218, — A karap (g. v.) of the Tur people, hostile to Zartuxst; his proper name was Brātar-vaxš [bl’tlwhs] ‘furthering the brothers’, DkM 79412, DD ch. 715 = Cod. K 22115; Brātarē-rēš ‘injuring the brothers’ is a malicious distortion. V. also Brātērēš.
3440:Siyā-gāv [--TWR”] n. pr. 477. — ‘Having black cattle’. | Siyämak [—-mk']n. pr. 471%. — Av. (1631) Syämaka- the name of a mountain. Siyāvaxš [—-whš] n. pr. 113%. — Av. (1631) Syävarsan- ‘having black stallions’.
4050:?vaxš [whš] flame, blaze 3718, with the gl. han i ātaxš paitak rošneh. — V. *vax- šitan.
1394:duš-hūxt [dwšhwht'] evil speech 63°’. 6510; Evil Speech, the second stage down to Hell 7524, — The negative of hüxt (q. v.). Av. (756 sq.) duž-ūxta-; Paz. dūžūst corresponding to Phl *dusüzt. duš-kām-kartārēh [dwSk’mkrt’lyh] bad exercise of authority, outrage, violence 7211. — Cf kam.
2089:"huvaršt [hwwlšt'] what is well done, good deeds, the third and last station preced- ing Paradise 632%. 7316-27, 8916, 1209, cf humat and hūxt. — Borrowed from Av. (1850) hvarsta-, ci varzitan.
5144:dvar-: dar duš-mainyu-: duš-mčn du$-manah-: duš-man duš-mata-: duš-mat duš-x"aronah-: duš- xUarr(ah) dužda.fedrē: dušdaft duž-dačna-: dus-dén duz-däy-: duž, dužd duž-vacah-: duš-gobišn duž-varšta-: duš-huvaršt duž-ūxta-: duš-hūxt dvaēšah, tbaēšah: 'bēš dvar-, dvāristan
1044:burtan [bwltn'; YBLWN-, YDLWN-tn'; forms v. I, 178] bar-, to carry, to bring, to bear, to wear, to procure; to take away, to remove (6 or pat ‘to’); arišk ~ to bear envy 691. 8419; !a&, bes, dast, dašn, gobišn, nam, namāc, nipart, paitäk, srav, stēžak, vāng, pat xrat ~: v. these ws.; bahr ~ v. barišneh; — to place on the top of (apar) 444; to lay a p. on (6) 4720-21; — andar 6 tan ~ to bring into corporeal existence 92t; — andarg ~, v. göbisn; — apar ~ to send out against 3711; to bring 6016; dmdcisn apar ~ to give instruction, to teach 80%; v. also apar-barisneh and apar-burtäreh ; — frac ~ to bring, to present 411; to bring forth, to light (a fire) 44°; — fröt ~ to bring down, to shed (water) 417°; v. also fröt- barišneh; — 6 ham ~ to collect, to amass 4815; pret. construed as an act. 187% Common Iranian; Av. OP (933 sqq.) also — (act. and middle) ‘to ride’, cf barak and asvār; cf also apar-barišneh from bar- ‘to move’.
```


## [2026-10-16T05:16:20.437Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4040,4049p NYB_vol2_glossary.txt | cut -c1-400; grep -n 'hūxt \\[\\|^hūxt\\|hūxt\\s*\\[' NYB_vol2_glossary.txt; grep -n '\\[w.ng\\|vāng \\[' NYB_vol2_glossary.txt|head -3"
}
```


### [2026-10-16T05:16:20.872Z] TOOL RESULT

```
vat-kamakéh [wtk'mkyh] ill will, spite- fulness 4".
vat-kart [wt' krt'] evil deed 4523. vattaréh [SLY”-tlyh, SLY-tlyh] wickedness 6314. 642-7-8 ete. passim.
evil,
vat-xém [wthym] ill-disposed, bad-tem- pered 9111.
Vaurubaršt [w^wlwblst'] the name of the north-western continent (kišvar, g.v.) 1064, — Borrowed from Av. (1430 sq.) Vouru.baraštī-.
Vaurujaršt [w'wlweclšt'] the name of the north-eastern kišvar 10614. — Borrowed from Av. (1430) Vouru.jaraštī-.
lyaxš [whš] word, message 44%. — Av. (1339) vaxša-. On the psychological notion vaxš v. de Menasce, SGV p. 75. V. vaxš-var.
www.parsianjoman.org | oe zl ejt
vaxš
207
1394:duš-hūxt [dwšhwht'] evil speech 63°’. 6510; Evil Speech, the second stage down to Hell 7524, — The negative of hüxt (q. v.). Av. (756 sq.) duž-ūxta-; Paz. dūžūst corresponding to Phl *dusüzt. duš-kām-kartārēh [dwSk’mkrt’lyh] bad exercise of authority, outrage, violence 7211. — Cf kam.
3933:vàng [w?ng, Ps. w’ngy; K?L?] voice, sound, shout, cry: ~ kartan to give a shout 1616; to shout; to sound, of a musical instrument 201%; of a horse’s call: to neigh 282; ~ burtan to shout 469; ~ be burtan 6 to shout to a p. 388. 4326; ~ zxröstan to yell, of Hešm 615; — war-cry 25%; — invocation (Christian) 1281; — pat buland ~ be grist burst out crying loudly 1112-13, — MPrs wng; NP bang.
```


## [2026-10-16T05:16:24.857Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22300,22330p BRT.txt | cut -c1-500 | grep -n -i 'vaxs\\|wort\\|vaxša' | head -20"
}
```


### [2026-10-16T05:16:25.196Z] TOOL RESULT

```
5:"  j>  g-  'vaxS-  V,  'wachsen;  wachsen lassen'.  Praes.  i  vax^-'^,  4  växiä-'\ 24  uxfaya-i^,  27  uxiya-i'',  30  (Kaus,?) vaxiaya-'^.  —  Inf.  'vaxlyai,  uxme.
7:fl/a  matdä  urvarh  vaxiai  (Konj.)  ahurS "aber  ihm  (dem  Rind)  lässt  MAh.  durch Aia  die  Pflanzen  wachsen"  Y.^i?.  6;  — staomi  matfim^a  vänmca  yä  tt  (nämL haomah^  kihrpjm  vaxsayats  (3D,)  Y. 10.  3.  2)  'erhöhen'  in  es chatologis ehern
8:Sinn,  sva.  'zu  höchster  Entfaltung,  Grösse und  Schöne  bringen'" :  vakislim  . .  maedai oval  xsdirgm  hyat  ksi  voha  vaxsal{?io'üy') manatihä  ". .  das  Beste  ,  .:  jenes  Reich des  M.,  das  ihm  VM.  erhohen  wird"  Y. J/.  6;  —  vatahsul  xSa^rä  manavhs  asä mat  ärmaiti}  vaxft  utayBill  tpvlil  "die Reiche  des  VM.  wird  zusammen  mit  Ala Arm.  erhöhen,  den  Bestand  und  die  Kraft" Y.j.^.  11;  — ya  (nämi.  *"3i^rJ)  därayat vahütim  manS  tä  masds  tnainyB  uxiyS 
19:mit  ä  'besprühen,  sprühend  benetzen': i  iaia  xä  . .  ä  i^ansajU  urvaranam  sBra vaxsyente'^  vaxSa  "wann  werden  die Quellen  . .  die  Wurzeln  der  Pflanzen  mit starkem  Netzen  benetzen?"  Yt.  Ä  42.
26:KompE.  —  Zum  V.  'vaxs-,
28:KompE.  —  Znm  V.  'vaxS:  —  Pü.  r  tiaxhin,  ■ (in  V.  xr):  fehlt;  b.  noch  No.  I.  —  ')  Man  1 TCrlangtc  -  auch  nach  Pu.:  fa  vaxiisn  -  einen infinitiviscfaen  Daliv.  —  '>  Pü.:  tran$skr-  —  , 1)  Sinnwidrig  and  zu  streichen;  fehlt  auch' in  Pü.
29:•  j.  *vaxSa-  m.  'Besprühen,  Benetzen': sBra  vaxiyente  (sd.)  vax^a  Yt  S.  42.
31:•  j.  ivax6a-  n, 'Wort,  Geheiss':  'um  ml asqsai  (sd.)  zara%ustrB  V.  ig.  15,
```


## [2026-10-16T05:16:30.778Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 204 218 229 401; do echo \"=== BQT:$p\"; python3 tools/ref_page.py BQT:$p 2>&1 | head -80; done"
}
```


### [2026-10-16T05:16:31.653Z] TOOL RESULT

```
=== BQT:204
no scan of BQT covers printed page 204 (see 'scans' in refs_online.json)
=== BQT:218
no scan of BQT covers printed page 218 (see 'scans' in refs_online.json)
=== BQT:229
no scan of BQT covers printed page 229 (see 'scans' in refs_online.json)
=== BQT:401
no scan of BQT covers printed page 401 (see 'scans' in refs_online.json)
```


## [2026-10-16T05:16:38.463Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; f=BQT_v1_pages.txt; for w in 'باژ' 'باج' 'بانگ' 'پژواک' 'آوا' 'آواز' 'خنیا'; do echo \"== $w\"; grep -n \"^ *$w\\b\\|$w *[-–:]\\|^$w\" $f | head -5; done; grep -c $'\\f' $f; grep -n 'pdf page' $f | head -3"
}
```


### [2026-10-16T05:16:38.884Z] TOOL RESULT

```
== باژ
4914:باژ ( فارسی ) .۰ ۵221 ژ‌ 2
16621:باژه - بر وزن‌خاره ؛ دیوار و حمارقلمه
16739:باژ بان ۳ - بازای فارسی و بای ابجد
16769:باژ۵اد - بای فارسی بر وزن تانجداره
16794:باژر نگ - با کلف‌فارسی» بر رزنومعنی
== باج
11586:باجیم مر وزن اصفهانك »
27729:باجام از از آن جک محصوي مقداری ّ
== بانگ
7727:بانگه و فرباد کرد است
16685:بانگه پای مورچه در زبر چاه‌شست باز
17294:بانگشت گر تن ه کتابه از شمردن
21198:بانگه است که کشیدن واز باشد.
29998:بانگگ رود وبان گکبك وبانگه ثز .
== پژواک
== آوا
7336:آواعی شرقی است.. «فان ٩ص‏ ۱۵۶ - ۰۱۱ ۶« کتبه‌های پهلوی. هننگ . ترحمهة تگارنده
8950:آواد - بسکون زای‌قطه دار.عمروف
8967:آواز باشد لهذا هزار دستان را هزار آوا تسیز
8972:آواد » بر وزن ناچار . مخذف آواره
9003:آوارجه - رکه : آورجه .عمتی هم هست معنی بیاور - و بمنی صاحب و
== آواز
8967:آواز باشد لهذا هزار دستان را هزار آوا تسیز
17901:آواز ؛ دس بدسرشت و بدذات باشد .
25137:آوازاورا شنیده
== خنیا
766
```


## [2026-10-16T05:16:42.058Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nfor k in ['page_offset','scans','notes']: print(k, json.dumps(d.get(k),ensure_ascii=False)[:1500])\""
}
```


### [2026-10-16T05:16:42.542Z] TOOL RESULT

```
page_offset "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...')."
scans [{"volume": "3", "file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920, "last_printed": 2475, "pdf_offset": -1917, "lang": "fas", "offset_note": "printed = pdf+1917, checked at pdf 150 and 500", "ocr_text": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"}, {"volume": "5", "file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf", "first_printed": 1, "last_printed": 290, "pdf_offset": 5, "lang": "fas", "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", "ocr_text": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt", "requires_volume": true}]
notes "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng,
```


## [2026-10-16T05:16:46.911Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 422 423 424 425 426; do echo \"## leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -4; done"
}
```


### [2026-10-16T05:16:47.456Z] TOOL RESULT

```
## leaf 422
۱ بابادشاه دست زدن ۱ متشه د<
است؛ و این صفیر بجهت تعظیم است .
پا یل » یکر الك بر وزن قابل , بلفت
بونانی نام ستار هشتری بباشد ۵ - و بسنی
## leaf 423
بت ۷۲۰۳ ح-
قلعهٌ آن شهر بوده چاهی است عمیق . گویندحاروث
و ماروت در اتحاه محبوی آند» و جضم الث حم
هقلح آنتتته. :
## leaf 424
ودریجة کوچك را گوند» وظاهراً ابن لفت‌باجهك
است که مصفر باجه باشده و باجه مخفف بادجه
و پادجه بمعنی باد گیر و باد گیر جایی و دوزنی
را کویند که باد از آنآمدو شد نماید واله‌اعلم .
## leaf 425
ی ۷۰ ‌-
پاخر و بنتحالت وسکون رای‌بی‌هطه
و زای نقطه‌دار , نام فصبهابست در خراسان ونم
کوشه‌نی باشد از چهل و حشت کوش موسیقی .
## leaf 426
نکن مم ینظر آعده است ٩‏
ادا فنجیر - نومی از درخت انجیراست
که یش از هم درختان موه دهد و انجیر آن
کاواك و پرباد میباشد .
```


## [2026-10-16T05:16:51.067Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==424 || NR==425' BQT_v1_pages.txt | grep -n -i 'باج\\|باژ\\|vāc\\|vac\\|vāz\\|vaz\\|زمزمه\\|اوستا\\|پهلوی' | head -30"
}
```


### [2026-10-16T05:16:51.422Z] TOOL RESULT

```
52:ودریجة کوچك را گوند» وظاهراً ابن لفت‌باجهك
53:است که مصفر باجه باشده و باجه مخفف بادجه
56:۱ باجه پفتح جیم بروزن راجه ؛ دربچه
79:«قطرالمحیط» .۰ ۴ - دراوستا 202764872 :ا 2020001020072 «معنی‌شمال آمده وآنجا جایگاه
80:اهر یمن و دیوان و مکان درزخ دانسته شده « خرده اوستا ۸۷ ح ۲ » . در پپلوی نبز کق2021
88:بقلم آ قای اقبال وداثرةالمعارف اسلام. ‏ ۷ - رل: بابوئه . ۸ - باج و باژ و باز باین معنی
89:از ریشه 08 پارسی‌بامتان مشتق است «مزدیسنا ۵4-۲۵۳ » وآن از ريشة 2 اوستایی بمعنی
90:بخش کردن وقسمت کردن‌است . ٩‏ - باح وبا وباز وواج و واژ باین‌معنی ازريشة اوستابی ۷۵6
91:( گفتن)» سان‌کریت ۷۵6 ۰ درپهلوی [۷2 با ۷۵8 ۰ درلاتینی ۷۵۴ , درفرانه ۷۵۷۴ » در
92:انگلیسی ۷۵۱6۶ . باژ بممنی کلمه و سخن و گفتار است . کليةٌ دعا های مختصر راکه زرتشتیان
93:آهته بزبان میرانند باژ گویند :
94:پرستندة آذر زردهشت. همی‌رفت باباژ و برسم بمشت . فردوسی‌طوسی «مزدیسنا۲۵۳ببمد»
95:اجثاق _ ترکی, دومردراکه دو خواهررا درازدواج دارند نبت‌بهم باجناق گویند .
```


## [2026-10-16T05:16:57.913Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in $(seq 434 456); do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | grep -n 'بانگ\\|vāng\\|vang\\|۷۵۵8\\|واژ\\|vāč\\|۷۵6' | sed \"s/^/leaf $n: /\" | head -5; done"
}
```


### [2026-10-16T05:16:59.406Z] TOOL RESULT

```
leaf 434: 56:«منای ۰۲۷۲ «تیبر که ۰۳۲ طبری ۷2۲ «واژه‌نامه ۰۰۷۷۲ کیلکی ۷8۴ . بهلوی
leaf 437: 53:بانگه پای مورچه در زبر چاه‌شست باز
leaf 448: 40:و امثال آن ٩‏ - و بمعنی بانگ و فرباد وآواز
leaf 449: 11:-و بانگی را یز کویند که در پیشا پیش پادشاه
leaf 449: 13:. بانگ‌ردن « کنابه ازبازداختن‌رنگاه
leaf 449: 15:بانگشت گر تن ه کتابه از شمردن
leaf 449: 37:طبری ۷۵۵8 (صدا) دراژه‌نامه ۸۰4 کیلکی ۷۵0۵ (کربة توام با نلله), ۳ - عطف‌مفرد
leaf 449: 45:۰- مخنف بانگه. رك چ بانگه.
```


## [2026-10-16T05:17:02.150Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==450' BQT_v1_pages.txt | sed -n 1,50p; echo '----'; awk 'BEGIN{RS=\"\\f\"} NR==438' BQT_v1_pages.txt | sed -n 40,70p"
}
```


### [2026-10-16T05:17:02.726Z] TOOL RESULT

```
بالف کشینه » بلفت زند ویلزند (۱) فبل‌را کوشد
و آن ۱۳ در هندوستان .
باهش 9 سکون ثالث و فاف مکسور
مشین فرشت زدهه دانهٌ کوچکی است که براون-
وین گونند و آلرا شوربا کرده خورند» و ممربی
جیلخ را خوانند .
بافنگه » بسکون ثاك و کاف فارسی .
حب‌البان راوشد وآنرا در دواحابکار دارند ٩‏ -
و بممنی فرباد و آواز بلند حم هست ۴ .
پانگ‌ر و ارو » کناب از دمصورباشد
-و بانگی را یز کویند که در پیشا پیش پادشاه
و سلاطین ۴ دروقت سواری و رفتن بای‌زاشد ۲
. بانگ‌ردن « کنابه ازبازداختن‌رنگاه
داشئن‌چیزی- ر اندن‌ودور کردن کسی ازیش باشد.
بانگشت گر تن ه کتابه از شمردن
وحاب کردن باشد .
بانو ۴ ینم نون و سکون واو»یبی
باه
و خاتون خانه - وعروس را گویند ۵ - و ظرف
کلاب و صراحی شراب‌را نی زکنته اند .
باوج ۷ - بسکون جیم فلرسی , جای
,| خوایی باشد که بجهت اطفال سازند و از جابی
آویژزند و طفل را در آن‌خوابانند و حر کتدهند
تا در هوا آجد و رود - و رسمانی را نیز کوبند
که در ایام عید نوروز از جای بلندی با شاخ.
درختی آویزند و زنان و دخثران برآن شسته‌در
هوا آیند و ژولد ,
با نو گشسب . بفتح کاف فارسی‌وشین
فوشت وسکون سین‌بی فطه وبای ابجده نم دخش
رستم ژال باشد . #۶
بانوی‌مشرق ه کنابه از آفتاب
هالمتاب است .
است و آن جایی باشد در زیر ناف متصل بات
مردی وزنی که موی از آ نجا برمیاًبد وآنرابحریی
عانه میگوبند .
اب ۴ بهلوی ۷208 «بندهشن 6۱۸۷ دتیب ر کك ۲۳۲ «تاوادبا ۲:۱۹
طبری ۷۵۵8 (صدا) دراژه‌نامه ۸۰4 کیلکی ۷۵0۵ (کربة توام با نلله), ۳ - عطف‌مفرد
بجمح 3 2۳ بپلوی بانوك ((0206) «بوستی . بندهش ۸٩۱‏
تراخسرویدر ۰ بانوت مادر
چنین کفت‌یس بانوی‌بالوان
بقیه ازصفحه ۲۲۸
از مصدر 82 یادن
* و رك: باز پیج .
۹ فردوسی‌طوسی.
۰- مخنف بانگه. رك چ بانگه.
۲ - باین ممنی عربی و فارسی : مأخون از هندی بهن 06020 . بول ابو حنیفه و دیسقوریدی
درخت‌بان شبیه بائل مشرقی 00۳360۸ 12708115 وبلند ومرتفم است وچوب آن نرم وشاخه
های وی‌سبز ولطیف‌است*داثرقالمعارف اسلام؟.. ممفناووع2 »ت52 دتایتی۱۹*
۴۳ 2 حز 0۵00270102 «یاروچا ۰۳۸4 0600۲7۲۸2 (ییل) دبوستی . بندهش۸۷*.
----
«قابل بسته باشد- وشیب رائیز کوبند *۱ که
؟ -_ پپلوی02۲2](مر کوب):
۵ - رك:پارو وبار.. ٩‏ - ر:بار.
۳
7 «قاب ۱
بش نگار. فرخی.
آمدت نوروز و آعد جشن نوروزی فراز
شاخ کل‌شطرنج‌سیمین وعقیقین گشتهاست
ای خداو ندی که تا تو ازعدم «ىدا شدی
آفرین زآن مر کبی کو بشنود در تیم‌شب
کامگارا !کار کیتی نازه از س رکیر باز
وفت شبگیران بنطع سبز برشطرنج باز
بته‌شد درهای‌بد, خما تلا گت باز
بانگه پای مورچه در زبر چاه‌شست باز
بقه در سفحهٌ ۲۱۸
```


## [2026-10-16T05:17:08.263Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==439' BQT_v1_pages.txt | grep -n 'باز\\|گفتن\\|vāč\\|۷۵\\|سخن\\|دعا\\|زمزمه' | head -20"
}
```


### [2026-10-16T05:17:08.575Z] TOOL RESULT

```
5:دوشو بازوویك‌بندانگشت‌هم‌همت ۴ -وخاموشيی
7:بعد از زمزمه آختبار کنند ۴ ونام فربه ابست
13:یمنی بازیا . *#
14:باز آزردن. کابه از فابدث خاط
16:باز ار خاك - بکررای‌بی‌هطه وخای
17:قض فراز باشد - وبازماندن و واماندن بمعنی
25:بازای فارسی هم‌درست ات
26:باز س بنزای فارسی » بروزن و «حنی‌باج
32:ن‌ بازار - در پهلوی و [در: هوحتان واچار ‌ سوق‌الاحواز ۰ رك 0 خوزستان ]
34:۲ منگری ۷۵28۲ , سرخه ؛ لاسگردی و شهمیرزادی 08226 « د . ۲ ص ۱۸۸
39:همچنان‌سنگ یکه اوراسیلکرداند زکوه ‏ کاء زین‌سوگاه آ نس وکه فرازوگاه باز
40:کامرهواری‌چ و کبك و کامجولان‌چونفاب ‏ گاه‌برجستن چوباشه گاءب رکشتن‌چوباز.
42:2 باریدت - پپلوی ۷۵1020 «بندهش۱۳4» مشتق ازمسدر اوستابی۷۵۲ (باریدن)«بارنولمه
43:۰ استی ۱۷۵۲15 «. است۱۳۸»» کیلکی 1#46600؛ فرودآ مدن قطراتآب ازابر» بارش, آعدن,
```


## [2026-10-16T05:17:12.841Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==439' BQT_v1_pages.txt | sed -n 1,30p"
}
```


### [2026-10-16T05:17:13.244Z] TOOL RESULT

```
با ۱ - ۷۱۸ -
و باع و قلاح راکوند . وآن مقداری باشد از
سرانگشت میانین دست راست ناسر انگشت‌میافین
دست چپ وقترکهرستهاراازهم بگشایند ۴ - وجمعنی
دوشو بازوویك‌بندانگشت‌هم‌همت ۴ -وخاموشيی
باشد که فان در وفت بدن شستن وچیزی‌خوردن
بعد از زمزمه آختبار کنند ۴ ونام فربه ابست
از قرای طوی ومعرب آن فاز است . گویند تولد
۱ حکیم فردوسی از ] تجاست .
پاد اه با زای بالف کشیده . نود استیی
باشدبموجب‌قرارداد زراشت‌بهرام ۵, وهراسنیری
چهارمتفال است -٩‏ وبممنی دیگر ییا هم هست
یمنی بازیا . *#
باز آزردن. کابه از فابدث خاط
خواه کردن باشد ۷ . ۱
باز ار خاك - بکررای‌بی‌هطه وخای
قض فراز باشد - وبازماندن و واماندن بمعنی
طرمیدن هم هست- و بمعنی تمیز کردن وغرقه
لمودن میان درچیز باشد - و پمعتی جداه‌عت
_که بربی فصل کوبند - و بمعنی عکس و قلب
نیزآمده است - وشراب راهم میگوبند که‌بعریی
خمر خواشد - و سوی و طرف و جالب را یز
کنته اند - و پیعتی گذر کاه سل هم آمده
است - وباج وخراج‌را لیز کویند, و باینمعنی
بازای فارسی هم‌درست ات
باز س بنزای فارسی » بروزن و «حنی‌باج
و خراج باشد. و آن زرست که زبر دستان از
زبردسان گپررند بمنی پادشاهان یزركك ازیادشاهان
کوچك‌سنانند ؟ ؛ومالیکه حکام از رعابا وراهدار
از سودااگر گرند - و جزبه را نز گفته اید»
```


## [2026-10-16T05:17:18.770Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in $(seq 615 635); do h=$(awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -2 | tr '\\n' ' ' | cut -c1-70); echo \"$n: $h\"; done"
}
```


### [2026-10-16T05:17:20.134Z] TOOL RESULT

```
615: و قری وییم وباگك٩‏ -و سروب رکه را نی زکوین و بمعنی داشتن (۱) و فرات - 
616:  یلووپ‎ پرواص » بر وزن المای,بنمنیلاسه 
617: رو دش" « بر وزن سرزش » بمعنی پروردن - و پرسنش و پرسنیدن باشد - و کتابه
618: پروش : روش < بر وزن خموش » جوششی 
619: همت و مضاوت وخوش رفتاری و جلوه کردن‌هم اه اطع 
620: پرهازه . و پر؛ آسیا (۱) و دولاب و امثال آن باشد - 
621: ومشفف پربر هم هست که پربروز باشد که روز پیش‌دیروز است؟ سومضارع مخاطی‌پ
622: ح‌ِ ۰ 4 بت . سازد ٩‏ , 
623: ۵ بفتح اول وسکون‌ثانی ودالابجد, بمعنی خون باشد که بعرچی دم گویند , و ب
624: ی کاله: ۱ 2 ۱ سب هه سس هردو زای عجمی, کلمهای باشد که شبانان بز را 
625: ات برخست باشد ۰ و آن کیاهی است خود روی 
626: وتجسی وجستجوی را کوبندب وبمعنی مصدر نیز آمده است که جستجوکی زن باشد. 
627: لس ۱ « جنم اول و سکون ثالی مخفف بسر است که درمقابل دختر باشد . #۶ 
628: سا نیدن- بروزن «سانیدن, آب دادن باغ وزراعت را کویند ۱ . 
629: حمشوق است. بی جانشین ۳ ۳ 
630: پربچه ی ۱ ۱ وت مخنور " مخذف پسواندو است که پسر ژن باشد 
631: ییان سیزدهم در بای فارسی باشین نقطه دار مشتمل برشصت لغت د کداهت 
632: پشت پاخارمدن شدن و خوش آمدن و خوشحال کردبدن 
633: مِِ ۳ ار ها کلیس 
634:  
635: 4 سس ارل و واو عمروف مرطبان سقالین باشد, ومعرب
```


## [2026-10-16T05:17:31.013Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 623 624 625; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | grep -n 'پژ\\|۴۰۱\\|۴۰۰\\|۴۰۲\\|vāk\\|۷۵۲' | sed \"s/^/$n: /\"; done"
}
```


### [2026-10-16T05:17:31.471Z] TOOL RESULT

```
623: 33:۳ ‌- رژد: پژاگن.
623: 35:اکر سراسرکوه وپژ آبدش هزپیش.
624: 37:۱ - مصحف‌پرمابه؛ رك : پرمابه و پرمابون . ۲ - اسم مفعول از پژمردن, رك : پژمردن .
624: 38:پزمرالدن و پزمرالیدی - بکسس اول و ضم سوم و فتح هشتم , متمدی پژمردن ‏
624: 39:پژُمرده کردن ۰ اذبال :
624: 40:همی پژمرانه رخ ارغوان کند نیره دبدار روشن روان .
624: 43:0 )+--8031. پز ظاهرا اشتبا‌فدمی ا-ت بجای‌یژ 0120 . ویزدر پژوهیدن ویژمان هم
624: 45:۲ - 2 با 10[۲ - 2 5 ۲۱۴1۲0 -2 (یحی شدن) «یب رکه ۲۳۸ :۰ ۷۵۲۵8۵۶).  .‏
625: 10:پژولش ۲ ۰ بکر اول بر وزن
625: 11:نکوهش , بمعنی پژهرده و پربشان و درهم
625: 13:پژ و لیف ۴ - بر وزن نکوهید » یعنی
625: 16:پرمرده شدن- و پژمرده کردن- ودرهم آمیختن
625: 30:پژو مان - بايم بر رزن خموشان ؛
625: 31:جمعم پژوم ات نی فقیران و درویشان
625: 46:۴ - انم مصتر از : پژولیدن .
```


## [2026-10-16T05:17:40.994Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==626' BQT_v1_pages.txt | sed -n 1,60p"
}
```


### [2026-10-16T05:17:41.524Z] TOOL RESULT

```
ات
برخست باشد ۰ و آن کیاهی است خود روی
و خوشبوی مانند اسفناج که داخل آش کنند
چون در کوه و کنبذ باواز بلند چیزی بگویند
در جوا ب‌همانرا نو ند » وآن‌را بمرمی‌صد اخو انند.
یر ول - بروزن‌قبول, کمب پا واسشخوان
۱ شتالنگه را کوش وستان زنان راهم گفتهاند-
و گلوله‌ا ی که طفلان بدان بازی کنند - وبمعنی
فندق هم هست و آن را هفزی باشد که بخورند
پژولش ۲ ۰ بکر اول بر وزن
نکوهش , بمعنی پژهرده و پربشان و درهم
شده باشد .
پژ و لیف ۴ - بر وزن نکوهید » یعنی
عزمرده شد وآب وئاب در وی نماند .
بر و لیدن بکراول‌بروزن‌نکوهیدن:
پرمرده شدن- و پژمرده کردن- ودرهم آمیختن
ویرثان کردیدن بود ۵ - و بمعنی تداخل هم
آمده‌است که درهم‌شدن‌باشد. وباین‌معنی بفتح‌اول
هم گفته‌اند وصیحت کردن - وجم‌تجو وبازیری
(۱) خم۳ : گزند .
و تفحص نمودن را نیز گویند .
لیدم ۴
و له " - بر وزن تکوهیده »
یز مرده شده ونرم گردیده شدت و بی‌اب و تاب
شدم و ابترشده- وصیحت کرده شدموبازیری
کرده شده باشد .
بزوم هتح اول بر وزث سموم ه
فقبر و دروش و کدا و خوار و ی اعشبار را
ند
پژو مان - بايم بر رزن خموشان ؛
جمعم پژوم ات نی فقیران و درویشان
و کدابان! .
فر و لاس ح بروزن دربند » چوبی باشد
که درپس در گذارند تادر کشوده نگردد- وچوب
کازران را نیز گویند ۷ - و کنابه از مردم
پس درنشین ودیوت باشد, و باین معنی بفتح اود
وئالی همآمده است ِ
بزوه ۸ بکسر اول وضم‌ثانی وسکون
هاء بممتی تفحص_ و تجسی و بازجمتن - و باز
خواست باشد- و جوندم و طالب و خواعنده را
نیز گوبند ٩‏ - و اهر باین معنی هم‌هست معنی
لفحص وتجسی بکن وبطلب وبخوام ويتتَهة بلند
وآمتر قبا ومانند آندا لیز کویند *۱.
یزرو شم 1 بروژن نکوهش,: تفحص
ص؟ ۲۷۷ اف نامد» .
۴ - انم مصتر از : پژولیدن .
٩‏ وه : برّمان () .
۵ رك : مدولیدن .
بزوه. «لفت نامه».
وفتح واو باشد. «لفت ناعه».
گرددان من بدولاند زود
صد ور محنت برایشان بر گشود .
مولوی بلخی‌رومی. «لفت‌نامه*.
```


## [2026-10-16T05:17:45.675Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==625' BQT_v1_pages.txt | sed -n 1,12p; echo ...; awk 'BEGIN{RS=\"\\f\"} NR==625' BQT_v1_pages.txt | sed -n 30,50p"
}
```


### [2026-10-16T05:17:46.277Z] TOOL RESULT

```
ی کاله: ۱ 2 ۱ سب هه سس
هردو زای عجمی, کلمهای باشد که شبانان بز را
بدان نوازتی کنند وبوی خود خوانند و آن را
پزیژی هم کوبند ٩‏ .
بز کاله بفثح اول بروزن ی رکاله ؛
بععنی حصه وبهرء ولخت وپاره باشداز هرچیز -
وپاره و وسلهرا تیز گوبند که برجامه دوزند ودر
عربی رقعه خوانتد ؟ .
فر ۵ - بفتح اول و سکون ثانی و هیم .
ببعنی کوه باشد که بعربی جبل خوانند. وبکسر
اول حم آخفة 0
۳ مان ۴ « بکسراول بروزن کرمان»
...
غلیواج باشد.
۱ - شود دل بحرف فرآن به نشود بز به جزیژی فربه. سنابی غزنوی. «لفت نامه» .
۳۳ بر کاله, وظاهراً همین صورت صحیح است. «لخغت نامه». ‏ و
۴ - پارسی باستان_ 00202 ۵ + تافقا2 ؛ پپلوی 25۳15020 ( بازند 0ناعدم) ,
هندی باستانی ۳20 ۲+ 0224 (مخالت کردن » اعتراض کردن ) «اسشق ۳۱۷». رك: بشیمان.
ه‌ بت آندرین خانه بوده‌ام عپمان کرده ام شاد اژو دل بزعان ِ
عتصری بلخی. «لفت ناهه؟.
۱ - مصحف‌پرمابه؛ رك : پرمابه و پرمابون . ۲ - اسم مفعول از پژمردن, رك : پژمردن .
پزمرالدن و پزمرالیدی - بکسس اول و ضم سوم و فتح هشتم , متمدی پژمردن ‏
پژُمرده کردن ۰ اذبال :
همی پژمرانه رخ ارغوان کند نیره دبدار روشن روان .
فردوسی طوسی. «لغت نامد» , رك: بزمردن.
* پزمر دن و پزمریدن - بکسر اول و ضم سوم و فتح پنجم » پارسی باستان أکقا08 ( اوستا
0 )+--8031. پز ظاهرا اشتبا‌فدمی ا-ت بجای‌یژ 0120 . ویزدر پژوهیدن ویژمان هم
دیده میشود «اسشق ۰۳۱۳ درهندی باستان ۵۵۷۱ ( سفت #دن » سحی شدن) » ارمنی
۲ - 2 با 10[۲ - 2 5 ۲۱۴1۲0 -2 (یحی شدن) «یب رکه ۲۳۸ :۰ ۷۵۲۵8۵۶).  .‏
بقبه اسف ۳۵٩‏
کنندچنانك نن‌مردم مر پزشکی‌را وچنانك اندازه مرهندسد را...» «دانشنامه ی۵۷*.
۵ پزیدن - بفتح اول وچهارم. پختن («.م) - پخته‌شدن:
هرمیوم که ذرباغ جبان‌بد همه پخته‌است ای غورة چون سنگه تخواهی‌توزبدن.
مولوی بلخی رومی . ذلفت نامه * .
```


## [2026-10-16T05:17:55.485Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 1473 2174 2178 2260 2388; do echo \"=== BQT:$p\"; python3 tools/ref_page.py BQT:$p 2>&1 | grep -v '^\\s*$' | head -120; done > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-538.txt; wc -l /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-538.txt; grep -n '^===\\|png\\|PNG\\|vision' /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-538.txt"
}
```


### [2026-10-16T05:18:31.889Z] TOOL RESULT

```
192 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-538.txt
1:=== BQT:1473
36:=== BQT:2174
76:=== BQT:2178
116:=== BQT:2260
152:=== BQT:2388
```


## [2026-10-16T05:18:34.016Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-538.txt"
}
```


### [2026-10-16T05:18:34.035Z] TOOL RESULT

```
1	=== BQT:1473
2	REF: BQT:1473  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 266  OCR-lang: fas
3	-۱8۳- فروخته
4	از پوستین روباه باشد وآن کرم‌ترین پوستی‌روباه | اطراف‌آن درها و پنجره‌ها دارد -
5	است بعد ازآن سمور ودیگر قاقم ‎٩‏ - فرواله ۱ - بر وزن پرکاله . بمعنی
6	فروار ۲ بروزن پروارخانةٌ تآبستانی فروال است که خانةٌ تابستانی و بالاخانهٌ اطراف
7	راگویند عموماً و بالاخانه‌ای که اطراف آن‌ورها | کشاده باشد . ۱
8	و پنجره‌ها داشته باشد خصوصاً - و بمعنی خانهٌ فروت - بفتح اول وئانی وسکون ثالث
9	زمتانی هم بنظرآمده است . وفوقانی» بمعنی بسیار باشد و بعربی کثیرخوانند؛ ‏
10	۰ نا ۰ اه
11	فرواده ۴ - بر وزن کهواره بمعنی وجتم اول هم گفتهاند :
12	فروار است که خانةٌ تابستانی و بالاخانهٌ چپار ور ۱ فرولن * « بکر اول وافتح تای
13	وبادگیر باشد - وبمعنی کنجینه هم‌آمده‌است. فرشت وسکون نونء تواضع کننده ومتواضع را
14	فرواز - بروزن انداز , چوب کوتاهی و و تنده ۸ زار دید
15	باشد بمقداردو بدست بعنی دوشبر وآنرادرپوشش ۱ فرو ه_- م‌اول بروزن‌خروشنده.
16	و بوربا بر بالای آن کسترانیده کل وخاریزند فروختاد؟ - بکسر اول وثانی بواو
17	و اندایند - و خانةٌ تابتانی و بالاخانه را هم | رسیده وسکون خای نقطه‌دار (۱) و فوقانی بالف
18	فرواره است کهخانةٌ تابتانی‌وبالاخانه‌ای باشد که فروخته *۱-,کراولبیم کزده شدسرا
19	۱- باین معنی «فرو» ( بفتح اول وسکون دوم وعربی است» جمع‌آن فراء (بکسر اول)
20	وفراء ۱ بح اول وتشدید دوم ( پوستین دوزاست اما« فرو یا درفارسی ۳ فرود ۰ پهلوی ۵1
21	ابرانی باستانی 05۳8۷812 [ رلك: فرود ] « نیب رکه ۷۹ برسرافعال مرکب درآید مانند : فرو
22	ربختن » فروخواندن » فرو کوفتن [ رك : دیباچهٌ مولفح‌لد ] و نیز براسماء درآید : فروتن -
23	۴ - اوستا- ۹۵۳2۷2۳888 1۳2۷8۵۲۵ » پهلوی 1۳2۷2۲ معنی « فروارنه »
24	اوستایی‌مشخص نیست . فروار فارسی با 2102171۷2۳2112 (بروار) (۸.م.) منطبق‌است . بعلاوه
25	هممکن اآست «فروار شکل همعرب «یروار» باشد ویهلوی و۱۱ فقط در کتیبه‌ها آمده «اسشق
26	۳ ورك : هوبشمان ۸۲۳. ورك : فروال » فرواله. ۴ - رد4 : فروار » فرواله »فروال.
27	۴ سد یمه آخر مصحف 7« قروار» (هم.). ه‌ قرواره («.م.) که فرواره.
28	‎٩‏ * فرواله ‏ فرواره * ۷ - از: فرو تن - ۸ - ازدساتیر «فرهنگه
29	دساتیر ۲۵۸ ۰ ‎٩‏ - از : فروخ ( فروختن ) + تار ( پسوند کار ورزی ) « دارمتش .
30	تعات ۳۱ ورك : سم مصدرص ۱*۵ ۰ ۹۰ آسم مفعول ازه فروختن » (و.م.) ۰
31	فر وختن - بنم اول ودوم وفتح پنجم ( درزبا ن کنونی ) ؛ اوستا ۷2۳90۰ ل 01۳۲2
32	( توسعهٌ - ۷26 چنانکه 8278 از - 386 ) ( صداکردن » بمعرض فروش گذاشتن) ؛ پهلوی
33	48 آاسشق - هوبشمان ۸۲۶« منای ۲۷۶ > ؛کردی 5۷70118 » کردی ع5۳۱۸112
34	( فروش ) « ژابا ص ۲۹۱ > » کردی ۶۷۳۵510 (فروشنده) « ژابا ۲۹۲ > + گلکی۳0۳0(:128؛
35	واکذارکردن‌چیزی يکي باگرفتن بهای‌آن - پزمخف افروختن (هم.).
36	=== BQT:2174
37	(no exact page map; using offset -1917 -> pdf page 257; check the printed number and re-run with --pdf-page if off)
38	REF: BQT:2174  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 257  OCR-lang: fas
39	نو -۱۷-
40	اول هم درست است - و دلیر و پپلوادرا نیز | « بروزن هوا . چند معنی دارد :
41	کنتهاید ۱ - وبمعتی باله کردن وزاری هم آمده - هرلغمه وآهنگه و آواز وباله را کوبند۴
42	[ ی - و اهر باین معنی هم هست بمنی ناله | عموما خواه از اسان باشد و خواه ازمرغان 8 .
43	و زار ی کن ۴ - و حرکت وجنبش ولرزه رانیز | ؟-لام مقامی‌است ازجمله‌دوازده مقام موسیقی۹ .
44	کوبند؟ - وامربلرزیدن وجنبانیدن هم‌هت ۴ ۱ ۳- جمعیت و سامان و سرانجام و کثرت مال
45	بمنی بلرز ویجنب وبلرزان وبجنبان ۰ و توانگری و نیکوبی حال و رولق‌کار باشد ۷
46	۱ - رشیدی کوید: « و پهلوان ودلیر که نیو نی زکوبند . فردوسی کوید:
47	اگر چند بیژن جواست ولو , بهن کار دارد خرد پیش رو
48	وله : جهاندار کاوس شان پیش رو زلشکر بی رزم سازان نو . »
49	(و رك : جهانگیری ایضا) اما «نو» درین اشعار بممنی جوان است ونورسیده (رك : فهرست ولف)
50	ولی‌ممکن است « نو > یکسراول مضشذف «نیو» (ه.م.) باشد ولی‌نه در اشمار مذ کور.
51	۲ - رشه ‎٩‏ نویدن » (ه.م.) ۴ - رك : نودن .
52	۴ - پهلوی 01۷815 [21۷26 - ۵1۷ خوش نوا ] « اوتوالا ۰۵ 2 -
53	8 - قی : ارمنی 8128 ( آهنگه . شمه , سرود) » 3188612 ( من مینوازم )
54	« هویشمان ۱۶۸۹ : :
55	فغان ازین غراب بین و وای او که در نوا فکندمان نوای او.
56	« متوچهری دامغانی ص۷۲ ۶ .۰
57	نوا بازی کنان در پردهة ننکه غزل کی و کشان در دامن چنکه.
58	نظامی کنجوی «کنجینه س ۱۵۹ >
59	. نوا یکی از اسطلاحات موسیقی‌است و چنان مینماید که بمعنی‌پرد؛ موسیقی ومقام باشد ,چتانکه
60	در الحان قدیم نام « نوای چكارك > » « نوای خارکن > » « لوای خسرواتی» آمده ( رك : عريك
61	از کلمات هد کور). «نواکر» و «نوا زن» لیز بمعنی زندة‌آهنگه موسیقی است. *نفیسی. تملیقات
62	تاریخ بیهقی ج ۲ ص ۸۹۱ . رك : لواختن . ۹ -« بام مقامی است از جملهٌ دوازده
63	مقام موسیقی , چنانکه شاعر در مقامات شعبه‌هایی بنظم آورده :
64	نوا آمد مقام و هست مشهور زوی نوروز خارا هست وماهور...» « جهالگیری .
65	« هنوز یکی از آهنگهای موسیقی کنونی بنام « نوا » معروفت ... عبدالقادر بغدادی در « لغت
66	شهنامه » (چاپ پطرزبو رک ۱۸۹۵ ص ۲۱۹) تصربح میکند که نوا نام نغمه‌ای در پردء*صفاهان»
67	است و ماند حسینی * در پرده صفاهان زده میدود » رك : نفیسی . تعلیقات تاریخ بهقی ج
68	ص ۸۹۱. نوا یکی ازهفت دستگاه ابرانی‌است. فواصل درجات «کام»آن مانند شور است ولی
69	«تنیث» ( پم اول ) ( مبداٌ ) آن درجةٌ چهارم گام شور میباشد ( از افادات استاد ابوالحن‌سبا ).
70	۷ - «اسلا نوا بعنی وسایل زندکی و آنچه زندکی را درخور است » چنانکه امروز
71	« بنوا رسیدن » بعنی‌در زند کی کشایش بافتن » و«یی‌نوا» بعنی کسی که تنگه دستست ودرزند کی
72	ا وکشایشی نیست ... اما « جمعیت وسامان وسرانجام وتوانگری » معانی ازديك و با معانی‌مجازی
73	«مان کشاد کی‌وفراخی درزند کی است » چنالکه این کلمه را با « بر که » که اسلا بمعنی‌استطاعت
74	مادی وتوالایی مادی است مرادف می‌آورند و۶ بر که ونوا » می گوبند؛ ودرفرهنگه اسدی (چاپ
75	آقای اقبال صس ۸ ) « توانگری وساز کار وشفل هردم» معنی کرده‌اند. > « لفیسی . تعلیقات تاریخ
76	=== BQT:2178
77	(no exact page map; using offset -1917 -> pdf page 261; check the printed number and re-run with --pdf-page if off)
78	REF: BQT:2178  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 261  OCR-lang: fas
79	بواختن ۱ -
80	نواختن ۱ - بفتح اول‌بروزن بباختن. | وظاهراً دربن دو معنی تصحیف خوانی شده باشده
81	بمعلی سرابیدن و بانگه زدن - وخوش کردن - | ال اعلم .
82	ولوازش مودن ۴ - و بمراد رسانیدن باشغد . نواده ۷ < بروزن قلاده » بمعنی‌لبیره
83	نواخته ۴ - بنتح اول بروزن تباخته, | باشد که فرزند زاده است عموماً و پس زاده را
84	بمعنی خیر و خیرات - و تکلفات و انسامات | گوبند خصوصاً - و فرزند عزیز وکرامی را نی
85	باشد . گفته‌اند .
86	نو اخسته ی « پروزن و معنی‌لواجسته نوار ۸ « بفتح اول بروزن هزارء‌چیزی
87	ات که باغ لو تشانده باشد . باغد پغن که آنرا از ریمان بافند و بر خیمه
88	و43 « بروزن سواد. سوراخی‌راگوبنن | دوزند وکاهی بار را بدان بر پشغت چاروا محکم
89	مانند مغزلی‌بجهت پنهان کردن چیزها وبسمنی | بندند ؛ وجضم اول هم آمده است .
90	زیان هم هست که بعربی‌نقصا ن کوبند* -وبیعتی نوارس * - بنم اول وکسررای‌قرشت
91	زیان هم‌بنظرآمده است که‌عربان لان‌خواش۹ ؛ | وسکون سبن بی‌نقطه . خیار دراز راکویند.
92	۱- از : نواخ (نواز) ۳-تن (پسوند مصدری) . نواختن اسلا بمعنی نوازش کردن » دست
93	کشیدن » زدن ؟ و نیز بمعنی زدن یکی ازآلات موسیقی, وسرابیدن آمده ۰ رك : نوا «هوبشمان
94	۹ از - 31۳۷80 درهندی ( سخن کفتن » تکلم کردن , قحتی دادن ) « اسشق 2۱*4۹
95	و ر4 : نازك ( منقول از نیب رکه) .
96	۴ - بنشده حلقه بگوش ار شوازی برود"
97	لطظف کن‌لطف, که بیگانه شود حلقه بگوش.
98	«دکلتان ص ۲۹ >.
99	۴ - اسم مفعول از « فواختن » . ۴ -رك : نواجسته . * - سرفی‌است
100	در معنی آبنده : «زبان» . ‎٩‏ - از دساتیر « نواد » بفتح اول بمعنی زبان که بتازی لسان
101	کوبند .» ۶ فرهنگه دساتیر ۲۷۱ ورك : فاب 4۷:۱ ۷ -قن : لوه » لیس » لبیره,
102	له : نواسه - پارسی باستان 888021 ( نوه) » اوستا - ۰88021 هندی باستان - 24021
103	« اسشق ۱۰۸۷ . شکل پهلوی 880 ( که درکتیبهٌ حاجی آباد 2 4۰ 3801 نوشته شده : با
104	فارسی جدید 32۷8 ( نوه ) ۳ بهودی 6۷۷6 (نوه) (0.74 ۸116۴ ) از پهلوی 88081 *.
105	از حالت فاعلی پارسی باستان3284 ناشی است . فارسی 32۷2018 * پپلوی 88041-21* از
106	حالت مفءعول صربح پارسی‌باستان 21288182 ۳ اوستایی 1328021610 آمده «هوبشمان۱*۸۸*.
107	۸ - « نوار . رشته ای باشد پهن چهاریایان را بدان استوا رکنند » عباسی گوید :
108	توکه سردی کنی ای خواجه بکون پسرت
109	آن که بالای رسن دارد و یهنای نوار . »
110	« لغت قرس ص ۱۸۷ >
111	‎٩‏ - (عر) « نوارس . اسم نوی از قتاد است . شاخهای او دراز و باربك و تا بقدر سه
112	ذرع و برکش ریزه و مستدیر و جمیم اجزای او زغب دار شبیه به پشم و گلش زرد و خوشبو
113	وطممش تند و حار و مانند سوزن و صمغ او مابین‌سفیدی وسرخی؛ و در روم وحلب کثیرالوجود
114	است . .>« تحفةٌ حکیم موّمن > .
115	(برهان قاطع د۳۷)
116	=== BQT:2260
117	(no exact page map; using offset -1917 -> pdf page 343; check the printed number and re-run with --pdf-page if off)
118	REF: BQT:2260  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 343  OCR-lang: fas
119	وخشت اد هه خطا
120	سوبمعنی آغاز وابتد! هم بنظرآمده است۱ . وخشور ؟- بنتح اول بروزن دستوده
121	وخشت؟ « بنتح اول و ناك وسکون پیغمبر ورسول را گوبند » وم اول هم آمدة
122	ثالی وفوقانی, نام روزچهارم است ازخمةمترقهٌ | است .
123	قدرم ۰ : وخشور پند؟ سا بفتح‌اول وبای‌فارسی
124	۹ - پرساختهٌ دساتیر « فرهنگه دساتیر سس ۴.۹۷۷۳ - پنج روزآخرسال راکه
125	درعربی خمةٌ مسترفه ودرفارسی پنجهٌ دزدیده و بهپيزك و پنجه و پنج وه نامیده شده باسم‌پنج ‌فصل
126	«کانها > [ قدیه‌ترین بخش اوستا ] نامزدکرده‌اند» یعنی‌بهر يك آزاین پنج روزاسم بکی از پنج
127	فصل کاتها را داده‌اند : از آنجمله نام روز چهارم بنام بخش چپارم کاتها 908111۳8 - ۷۵0
128	و نام روز پنجم بنام بخش پنجم کانپا ‎1٩1‏ ۷8۳1۶۸۵ نامیده شده « خرده اوستا . پورداود
129	۲۱۱ و رك : مزدیناص ۳۹۲,۳۰۱:۱۲۸.- «وخشت» متن * وهشت (رك : کربیتشن. شعر
130	پهلوی وشعر فارمی قدرم . مجلدّکارة قدم ۰۵ ۵ ۲) * فوهشت اعت» ( روز چهارم » درمتن
131	غلط و « روز پنجم » صحیح است ). ۴ - در اوستا ۳2۲8 - ۷83880 مر کب‌از«وخشن»
132	از ربشهٌ ۷81 (کفتن ) و« بره» از ريشهٌ 087 ( بردن ) که در فارسی بدل به «ور» ( بفتج اول )
133	شده و از پسوندهای اتصاف پشمارمیرود» پس وخشور ( که در پارسی همانند کنجور ورنجورومز دور
134	7 آن بدل به ۵۲ شده ) لغة بمعنی‌حامل لام (سخن)آسمانی واصطلاحاً بمعنی پیامبر است .
135	« مزوینا ص ۰۱۰۷-۱۰۹ پهلوی ۷8358۷۷87 ( دینکرت ) * اسشق ۱۰۷۹ درکتاب هفتم
136	دینکرت عبارتی آمده که درآیین مزدسنای پیشین سابقه ندارد . در این عبارت از ۷825[3۷2۲
137	سخن میرود , واین کلمه فقط بزرتشت اطلاق میشود . ازآغاز » از پیامبران وسولان دیگراوهرمزد
138	( اهورمزدا ) که پیش از زرتشت زندگی میکردند » وبوسيلةٌ ممجزانی که نشان داده‌اند ؛ رسالت
139	( ۷۵388۷8۲1۵ ) خود را در جهان ثابت کرده‌اند » باد میشود . (3 .7.1 .6ا0)
140	ورك : ابا (.1 .0۷65 )
141	نگهپای آب با اوست , مخصوصاً اسم فرشتةٌ موکل رود جیحون است.» «آثلرالباقیه س ۲۳۷* ر:
142	پور داود . سنا ۱ص *9- ۵۱ .- وخش ۷5 در ابرالی میانه بدو معنی «روح» و «کلمه»
143	آمده . در مانویت 9۵2۳4817۲ ۷8۳810 « روح القدسی > راکوبند .
144	-2070 0710406 1۳ 6ل ۲۳۵۵۵ :1 عل مامهم‌عد 0۵۷ ,۱/۹|۵ ۸۰
145	1۰ )و17 27 ۲ .انط7 06 11290 6 ۸00۰ 0617 از 87) 831۳60265۰
146	۰( .0 ,۱953 وه‌اآه8۲07 (۱952) ]2011 ۵۵6 ,فاد اع
147	رك : وخشور . ,اقرت کوید : « وخش ( بفتح اول ) شهری است از لواحی بلخ از ختلان » و آن
148	کوره است متصل بختل و جمماً تشکرل يك کوره دهند » و آن بر کنار اهر جیخون است . >
149	« ممجم‌البلدان ».
150	شاکر بخاری « لفت فری ی ۲۱۷ ۰
151	مصراع اول در سحاح‌الفرس : بگامی شمرد لزخطا با چگل . «طاعتی > .
152	=== BQT:2388
153	(no exact page map; using offset -1917 -> pdf page 471; check the printed number and re-run with --pdf-page if off)
154	REF: BQT:2388  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 471  OCR-lang: fas
155	هویمن ۳
156	هو ٍمی!۱ - با پای فارسی‌وميم بروزن | وبعربی عمی‌الراعی خوانند؛ وبسی کوبن دگیاعی
157	سوختن » بلغت زند و پازند (۱) رو را کوبند است وآن میشتر در تبریز بهم رسد و بیخ آرا
158	وجه خوانند . درمرهمها داخل سازند وسیاء پلاورا بدان رنگه
159	ی ۲ ۹ کنند؛ وبعضی کوبند کاوزبان تلخ ات۲ ‎٩.‏
160	‏هو به < بضم اول وئانی مجپول وفتح 1 :
161	بای ابچد, دوش و کتف را گوبند - وبمعنی‌پشتی هوخ؟ -بنم اول وثانی مجهول وخای
162	وحمایت هم هست؛ وباین «عنی بجای بای ابجد نقطه دار سا کن,نام بیت‌المقدس‌است » ودر قدیم
163	بای حطی هم آمده است. قبله بوده است والحال قبلهٌ نصاری است .
164	هوجره - بنم ارل وفتح جیم و رای هموخت؟ - با نالی مجهول بر وزن
165	فرشت, کیاهی است که آن را سرخ مرد کویند | سوخت. بمعنی هوخ است که بیت‌المقدی‌باشد .
166	(۷) چك : زند ویاژند .
167	۱ - هز. ۵)8(۲۵ ۰ ۵۵۵)2(۳۳2۵8 » پهلوی 1۵0 » روی «یونکرس۹۱ .
168	۴ - این کلمه صورب « هوبر > (ه.م.) و « هوبه > (ه.م.) هم ضبط شده . لقب شاپور
169	ذوالاکتاف را « هویه سنبا » نوشته‌اند . حمزءٌ اصقهانی در سنی ملول‌الارش ( ص ۳۹ ) آرد :
170	«شاپور ذوالاکتاف » وسموه شابور غوبه سنبا. «هویه» اسم لکتف » وساها ای‌نقاب . قیل له ذلك
171	لانه لماغز! المرب, کان پنقب اکنافهم, فیجمع ین کتفی‌الرجل منم بحلقة ویابیه » فمته‌الفری
172	بهذاالاسم, وسمته‌العرب ذاالاکتاف.». درمجمل‌التواریخ والقهص (ص۳۶) آمده: «واورا (شاپور را)
173	عرب ذوالاکناف لقب کردند؛ زبرا کتفهای عرب سوراخ کردء وحلقةٌ آهنین درآن کشید, بعد از
174	آنکه بی‌اندازه قتّل کرده پارسیان‌اورا شاپور هوبه منیا خواندندی.» کریتدن « ساسان. ترجمه
175	چاپ دوم ص۲۹۱ح» نوبد: «مصنفین عرب, که نوشته‌های آنما ازمنابم ساسالی اخذ شده, بطور
176	کلی لقب‌شاپوررا بلفظ عربی ذوالاکتاف (صاحب شانه‌ها) ترجمه کرده‌اند. ند که برین عقیده‌است
177	که اصل این لفظ یك‌لغبی اس-ت بمعنی چهارشانه, یمنی کسی که بارهای بسیار دولت را میکشد »
178	معذلك حمز؛ اصفهانی و «سنفین دیسگر که پیرو او هستند » لفظ فارسی این لفت را هوبه سنبا
179	062-2 نوشته‌اند که بمعنی « سوراخ کننده شانه ها > است . نلد که کمان میکند
180	(طبری۱ ص۵۲» بادداشت ۱) که این‌لفظط مجهول امت واز روی کلمهٌ عربی ذوالاکتاف ساخته شده
181	امت. اما اینکه بجای‌کلمةٌ « کتف» لفظ عتبق فارسی نی «هوبه» را که نمعنی شانه‌بود؛ آورده‌اند»
182	«اظرمن دول حمزه صحیح آست. وهوبه سس نقل ازکلمهٌ پپلوی شده ومءنأیی‌هم که‌از آن کرده‌اند»
183	مطابق روابات فدیمه است, وانگهی‌درتار.خ ساسالیان این‌تنها اوشی نیست که صحبت ازین‌مجازات
184	شده باشد. خسرو دوم که نسبت بمنجمان خشمگین گردید. آنها را نهدید مود که استخوان‌دانه
185	آنهارا یرون خواهد کشد (طبری ۰۱۶۱۲ نلد که ص۳۰۷).>کلمة منبا » صفت فاعلی (هفت
186	مشهه) ازسنبیدن است بمعنی سوراخ کردن. ر4: هوبه ورك : هوس.
187	۴ - ۰ هوجره. وهی ففبدای, مزمارالراعی است » «تحفة حکیم موّْمن».
188	۴ - رك: دژهخت, دژهخت کنگه. دژهوخ ( در: دژهرج! ,گنگه دژهرج) ورك:هوخت
189	۴ - ر4: هوخ وح۳. - هوخت در بهلوی 12154 (کفتار نيك) * مناس ۲۷۷ ۰ ازآوستا
190	۳2 (گفتاردِك) که درپهلوی به 100-0(هر کوش) ت رجمه‌شده. ر4: مزدیناص**4.
191	۰ هوپهسبا - ر4: ح؟۷ .
192	‎٩‏ هوچی - ر4: هر.
193	
```


## [2026-10-16T05:18:46.154Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in 'باژ' 'گواژه' 'وخشور' 'خنیاگر' 'خنیا'; do echo \"== $w\"; grep -n \"$w\" FSF_pages.txt | head -4; done"
}
```


### [2026-10-16T05:18:46.488Z] TOOL RESULT

```
== باژ
2516:                                               ‫وگر برنهم باژو ساو گران‬
3738:                                            ‫باژ‬
3748:                                      ‫باژبان ب‬           ‫مکاسنم بهمازندران‬
3753:                                                          ‫گباژ‬
== گواژه
2414:      ‫گواژه بسی بایدت بافسوس‬                          ‫‏)‪(AF-V1-۴‬‬
2430:‫بر خریدار فنون سخره و افسوس کنند‬                   ‫گواژه همی زد چنین وز فسوس‬
2432:           ‫از حافظ (غزل ‪۵‬بیت ‪۳‬و ‪۵۳-۷‬‬               ‫نباید گواژه زدن بر فسوس‬
19906:             ‫همی زد پس او فرود‬      ‫گواژه‬             ‫نریمان چو زین مژده آگاه گشت‬
== وخشور
== خنیاگر
11912:                                                           ‫به هر برزن آواز خنیاگران‬
== خنیا
10604:                            ‫خنیا (باپیشاو)‬           ‫نگ ماراتامیان آید همی‬
10616:               ‫که چون آب یابد بنیرو شود‬        ‫اینچند خنیایی همه خوش و نیکو [ست]‬
10620:‫جهان از ستمکاره بی خو کنیم‬                     ‫جهان شد پرآواز خنیا و نوش‬
11912:                                                           ‫به هر برزن آواز خنیاگران‬
```


## [2026-10-16T05:18:49.479Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2405,2435p FSF_pages.txt | sed 's/  */ /g'; echo ---; sed -n 3735,3760p FSF_pages.txt | sed 's/  */ /g'; head -2414 FSF_pages.txt | grep -o 'pdf page [0-9]*' | tail -1; head -3738 FSF_pages.txt | grep -o 'pdf page [0-9]*' | tail -1"
}
```


### [2026-10-16T05:18:49.786Z] TOOL RESULT

```
 ‫اان‬
 ‫زمست‬
 ‫ریشخند تمسخر‪:‬‬
 ‫که برنیزه‌ها گردد افسرده دست‬
‫[گردآفرید] بخندید و او [سهراب]را به افسوس گفت‪:‬‬ ‫(‪)۵-۵۰۳-۲۷۱۱‬‬
‫که ترکان زایران نیابند جفت‬
 ‫یکی ابرتند اندر آمد چو گرد‬
 ‫(‪)۲-۹۸۱-۹۵۲‬‬
 ‫ز سرما همی لب به دندان فسرد‬
 ‫گواژه بسی بایدت بافسوس‬ ‫‏)‪(AF-V1-۴‬‬
 ‫ووس‬
 ‫نمهرد نبردی کووپال ک‬
 ‫بگهوش تو گرنام من بگذرد‬
 ‫(‪)۳-۶۱۲-۹۹۲۳‬‬
 ‫دم و جان و خون و دلت بفسرد‬
 ‫کشانی بدو گفت باتو سلیح‬ ‫(‪)۲-۱۰۱-۲۶۲‬‬
 ‫نبینم همی جز فسوس و مزیح‬ ‫هم از گنج صددانه خوشاب جست‬
 ‫(‪)۴-۵۹۱-۸۸۳۱‬‬
 ‫که آب فسردست گفتی درست‬
 ‫اازسدی ( گرشاسب‌نامه ‪ ۲۰۱-۱۳‬و ‪)۴۳۴-۱۲‬‬
 ‫(‪)۴-۲۲-۲۳۲‬‬
‫افشاندن‬



‫بر خریدار فنون سخره و افسوس کنند‬ ‫گواژه همی زد چنین وز فسوس‬
‫وانگهی‪ .‬جزکههمهتنبل و افسون نخرند‬ ‫همی خواند مهراج را نوعروس‬
 ‫از حافظ (غزل ‪۵‬بیت ‪۳‬و ‪۵۳-۷‬‬ ‫نباید گواژه زدن بر فسوس‬
 ‫ده روز مهر گردون افسانه است و افسون‬ ‫نه بر یافه گفتن شدن چاپلوس‬
‫نیکی بجای یاران فرصت شمار یارا‬ ‫انزاصر حسرو (دیوان ‪)۲۴-۱۱‬‬
 ‫برو فسانه مخوان و فسون مدم حافظ‬ ‫خویشتن رابه زه بهمان و احسنت فلان‬
---
 ‫(‪)۱-۰۲۱-۱۹۶‬‬
 ‫دو بهره نیامد به خرگاه باز‬
 ‫(‪)۲-۷۶۱-۳۱۶‬‬
 ‫باژ‬
‫از‬ ‫ههان‬
 ‫ات ک‬
 ‫شریس‬
 ‫دنز‬
 ‫اوآ‬
 ‫پاح‬
 ‫‪-۱‬ب‬ ‫بازحستن (با پیش جیم)‬
 ‫شاهان زیردست می‌گر فتند‪:‬‬ ‫پرسیدن‪ ,‬تحقیق کردن‪:‬‬
 ‫=اژخواه ب=اژدار‬
 ‫باژبان ب‬ ‫مکاسنم بهمازندران‬
 ‫(کاوس)‪ :‬انگر‬
‫ویند راهداری کهاز مسافر‬
 ‫یجا‬
 ‫با‬ ‫روان‬
 ‫گباژ‬
 ‫وهم‬
 ‫ار ن‬
 ‫سر ب‬
 ‫وگ‬
‫و راهگذر پولی می‌گرفت و اجازۂ گذر از‬ ‫(‪)۲-۲۸-۱۳۱‬‬

 ‫مرز يااز دریا را می‌داد‪:‬‬ ‫(ویس ‪:)۵۹۴-۸۱‬‬
```


## [2026-10-16T05:19:03.802Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'pdf page' FSF_pages.txt | head -3; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json'))['FSF'];print(d.get('page_offset'))\"; awk 'BEGIN{RS=\"\\f\"} {if (index(\\$0,\"باژ\")>0) print NR-1}' FSF_pages.txt | head"
}
```


### [2026-10-16T05:19:04.168Z] TOOL RESULT

```
484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
awk: cmd. line:1: BEGIN{RS="\f"} {if (index(\$0,"باژ")>0) print NR-1}
awk: cmd. line:1:                           ^ backslash not last character on line
```


## [2026-10-16T05:19:11.884Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} index($0,\"باژ\")>0 {print NR-1}' FSF_pages.txt | head; awk 'BEGIN{RS=\"\\f\"} index($0,\"گواژه\")>0 {print NR-1}' FSF_pages.txt | head"
}
```


### [2026-10-16T05:19:12.559Z] TOOL RESULT

```
57
81
82
201
208
259
266
282
293
335
55
56
406
```


## [2026-10-16T05:19:16.221Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==82' FSF_pages.txt | sed 's/  */ /g' | grep -v '^\\s*$' | head -60"
}
```


### [2026-10-16T05:19:16.624Z] TOOL RESULT

```
 ‫‪۷۸‬‬ ‫بازارگاه‬
 ‫مرآن نامور پهلوان را تونام‬ ‫نیرو قودرت برمی‌آید‪:‬‬
‫شوی بازجویی فرستی پیام‬ ‫شدند انجمن دیو بسیار مر‬
 ‫(‪۴-۲۱۲-۲۷0‬‬ ‫کهپردخته مانندازو تاجو فر‬
 ‫نهفته همه کارشان باز جست‬ ‫چتوهمورت آگه شد از کارشان‬
 ‫بر آشفت و بشکست بازارشان‬
 ‫(‪)۵-۳۲-۲۵۲‬‬ ‫(‪)۱-۷۳-۱۳‬‬
 ‫باز خوردن‬ ‫‪-۵‬و در بیت زیر از بازار معنی سامان و‬
 ‫شدن‪:‬‬ ‫برخوردن‪ ,‬روبرو شدن‪ .‬مصادف‬
 ‫کارو بار برمی‌آید‪:‬‬
 ‫چو هامون ویسه بدان رزمگاه‬ ‫زال آرزوی همسری بارودابه را دارد سام‬
‫که گودرز کشواد بد با سپاه‬
 ‫همرای نیست‪ .‬زال لب بگهله و شکایت‬
 ‫بیامد کتهوید گنزردان برد‬ ‫می‌گشاید‪ .‬سام نرم می‌شود و می‌گوبد‪:‬‬
 ‫نگهبان لشکر بدو باز خورد‬ ‫مشو تيز نا چاره کار تو‬
 ‫(‪)۵-۱۱۱-۲۵۳‬‬
 ‫بسازم کنون نیز بازار تو‬
 ‫بازداشتن‬
 ‫)‪(1-11-۶4‬‬
 ‫جلوگیری کردن‪ ,‬مانع شدن‪:‬‬
 ‫بازارگاه‬
 ‫هم بیم جانست و هم جای ننگ‬
 ‫وروش‪:‬‬
 ‫جای داد و ستد و خرید ف‬
 ‫چرا باز داری سرم راز جنگ‬
 ‫(‪)۱-۹۸۱-۶۲۸‬‬ ‫ووی و بازارگاه‬
 ‫ز بس برزن ک‬
 ‫تگوفتی نماندست بر خاک راه‬
 ‫بداازنستن‬
 ‫(‪۸‬نوشیروان ‪)۵۷۶‬‬
 ‫دادن‪:‬‬ ‫شناختن‪ .‬تمیز و تشخیص‬
 ‫بآازمدن‬
 ‫گنت چون پر زاغ‬ ‫جهان سربهسر‬
‫ز هامون ز راغ‬ ‫نسداستت‬
 ‫مرکب از باز [پیشوند بهمعنی دیگر باراز‬
 ‫(‪)۶-۷۸۱-۴۵۳‬‬
 ‫‪+‬دن ب=رگشتن» بازگشتن‪:‬‬
 ‫نو] آم‬
 ‫ز نخچیر کامد سوی خانه باز‬
 ‫درفشیدن تیغ‌های بنفش‬
 ‫به دلش اندر اندیشه آمد دراژ‬
 ‫چو بینید باکاویانی درفش‬
 ‫(‪۱-۰۸۱-۹۸‬ع)‬
 ‫بدرد دل و مغزتان از نهیب‬
 ‫سداز‬
 ‫گه ب‬
 ‫نک‬‫جکس‬
 ‫زشکر هر آن‬
 ‫ل‬
 ‫بلندی ندانید باز از نشیب‬
 ‫(‪)۱-۰۲۱-۱۹۶‬‬
 ‫دو بهره نیامد به خرگاه باز‬
 ‫(‪)۲-۷۶۱-۳۱۶‬‬
 ‫باژ‬
‫از‬ ‫ههان‬
 ‫ات ک‬
 ‫شریس‬
 ‫دنز‬
 ‫اوآ‬
 ‫پاح‬
```


## [2026-10-16T05:19:22.224Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==68' FSF_pages.txt | sed 's/  */ /g' | grep -v '^\\s*$' | head -40"
}
```


### [2026-10-16T05:19:22.581Z] TOOL RESULT

```
 ‫‪۴‬‬ ‫اوباردن‬
 ‫پس از پرورش تن روانتان را پرورش‬
‫گوید کایدون نماند جای نیوشه‬ ‫ادر‬
 ‫دور‬ ‫دهید و اندیشۂ نابکار ج‬
 ‫بنگرباپ‬
 ‫در فکند سرخ ملبهرطل دو گوشه‬ ‫راازک س‬
 ‫نر د‬
 ‫یور‬
 ‫د‪.‬‬
‫روشن گردد جهان ز گوشه بهگوشه‬ ‫به معنی‪ :‬خنک‪ .‬خوشاء خرم‪:‬‬
 ‫گوید کاین می مرانگردد نوشه‬ ‫گیو به دستور پدرش گودرز به جستجوی‬
‫تانخورم ياد شهریار عدو مال‬ ‫یاوش به توران زمین رفته‬ ‫خسرو پسسر‬
 ‫*اوباردن‬ ‫است و پس از هفت سال رنج و سختی و‬
 ‫یلعیدن‪ .‬ناجو يده خوردن "‪42‬م ‪:0‬‬ ‫نیافتن خسرو بهخودگوید‪:‬‬
 ‫اگر مرگ کس را نیوباردی‬ ‫همانا که خسرو ز مادر نزاد‬
 ‫رکدی‬
 ‫ا خا‬
 ‫پوان‬
 ‫سو ج‬‫بیر‬‫زپ‬ ‫وگر زاد‪ .‬دادش زمانه په باد‬
‫‏)‪(TAF-1‬‬
 ‫ز جستن مرا رنج و سختیست بهر‬
 ‫آورمرد» ارمزد‪ ,‬ارمز» هرمزد» هرمز‬ ‫انوشه کسی کو بمیرد به زهر‬
‫همه این‌ها شکل‌های دیگری از «اهورا‬ ‫(‪)۳-۵۰۲-۶۲۱۳‬‬
 ‫مزدا»‌ی اوستایی است که نام ایزد است‪:‬‬ ‫کیخسرو از رستم می‌پرسد‪:‬‬
‫از دو واژه است‪ :‬ا‬ ‫مرکب‬ ‫اهورامزدا‬
 ‫زواره فرامرز و دستان سام‬
 ‫درستند؟ ازیشان چه داری پیام؟‬
‫‪۲‬مزدا به معلی داناء‬
 ‫سرور بزرگ» ‪-‬‬ ‫سهخ می‌دهد‪:‬‬ ‫اب‬ ‫رس‬
 ‫پتم‬
‫‪ ۲۲‬به‬ ‫‪۱‬ص‬ ‫خر دمند‪( .‬یورداود‪ .‬یشت‌هاج‬
 ‫به بخت تو هر سه درستند و شاد‬
 ‫بعد)‬ ‫انوشه کسی کش کند شاه یاد‬
‫‪-۱‬اورمزد در آیین مزدیسنا نام روز اول‬ ‫‏)‪(VAY-OF-0‬‬
 ‫هر ماه است‪:‬‬
 ‫‪-۳‬به معنی گواراء نوش جان‪:‬‬
 ‫همان اورمزد و مه و روز مهر‬ ‫چنین گفت خحسرو به یزدان پرست‬
‫بشوید به آب خرد جان و چهر‬ ‫که از خوردنی چی‬
 ‫بست‬
 ‫د کا‬
```


## [2026-10-16T05:19:28.845Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -50"
}
```


### [2026-10-16T05:19:29.135Z] TOOL RESULT

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


## [2026-10-16T05:19:37.995Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=tools/fetch_source.py; for u in \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-' \\\n'https://en.wiktionary.org/wiki/آواز' \\\n'https://en.wiktionary.org/wiki/واژه' \\\n'https://en.wiktionary.org/wiki/فروختن' \\\n'https://en.wiktionary.org/wiki/بانگ' \\\n'https://en.wiktionary.org/wiki/نوا' \\\n'https://en.wiktionary.org/wiki/خنیاگر' \\\n'https://en.wiktionary.org/wiki/پژواک' \\\n'https://en.wiktionary.org/wiki/وخشور' \\\n'https://en.wiktionary.org/wiki/voice' \\\n'https://www.etymonline.com/word/voice' \\\n'https://www.etymonline.com/word/vocabulary' \\\n'https://en.wiktionary.org/wiki/vox' \\\n'https://en.wiktionary.org/wiki/hūxta-' ; do echo \"## $u\"; python3 $S \"$u\" --note \"page 538, root Wekw: etymology check\" 2>&1 | tail -1; done"
}
```


### [2026-10-16T05:19:44.324Z] TOOL RESULT

```
## https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0898c1b35e41e61a.txt
## https://en.wiktionary.org/wiki/آواز
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d082fb7f4ff31d5a.txt
## https://en.wiktionary.org/wiki/واژه
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d7f584e33089b31a.txt
## https://en.wiktionary.org/wiki/فروختن
/home/sfmqrb/git/rishe-private/data/verification/sources/web/369f221e7c9a84f0.txt
## https://en.wiktionary.org/wiki/بانگ
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2f2c4bfa34f4683a.txt
## https://en.wiktionary.org/wiki/نوا
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6e4fbd8837b107b8.txt
## https://en.wiktionary.org/wiki/خنیاگر
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6a3bce4daf1bcf4b.txt
## https://en.wiktionary.org/wiki/پژواک
/home/sfmqrb/git/rishe-private/data/verification/sources/web/607d8bb4c4b93f16.txt
## https://en.wiktionary.org/wiki/وخشور
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f3c21eae0a57bdc8.txt
## https://en.wiktionary.org/wiki/voice
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8b0e91af1f892d36.txt
## https://www.etymonline.com/word/voice
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0558662caeadb188.txt
## https://www.etymonline.com/word/vocabulary
/home/sfmqrb/git/rishe-private/data/verification/sources/web/99321a4ff2055709.txt
## https://en.wiktionary.org/wiki/vox
/home/sfmqrb/git/rishe-private/data/verification/sources/web/67b3ff4090a96b56.txt
## https://en.wiktionary.org/wiki/hūxta-
/home/sfmqrb/git/rishe-private/data/verification/sources/web/baf4a49155f3508c.txt
```


## [2026-10-16T05:19:48.095Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -14 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'], d['bytes'], d['url'])\"; for f in d082fb7f4ff31d5a d7f584e33089b31a 369f221e7c9a84f0 2f2c4bfa34f4683a 6e4fbd8837b107b8 6a3bce4daf1bcf4b 607d8bb4c4b93f16 f3c21eae0a57bdc8; do echo \"#### $f\"; grep -A6 -m2 '^Etymology' $f.txt | head -14; done"
}
```


### [2026-10-16T05:19:48.557Z] TOOL RESULT

```
200 4200 https://en.wiktionary.org/wiki/نوا
200 2968 https://en.wiktionary.org/wiki/خنیاگر
200 2655 https://en.wiktionary.org/wiki/پژواک
-1 39 https://en.wiktionary.org/wiki/وخشور
200 18531 https://en.wiktionary.org/wiki/voice
-1 39 https://www.etymonline.com/word/voice
-1 39 https://www.etymonline.com/word/vocabulary
200 11076 https://en.wiktionary.org/wiki/vox
200 4171 https://en.wiktionary.org/wiki/بیوه
-1 39 https://en.wiktionary.org/wiki/hūxta-
200 13333 https://en.wiktionary.org/wiki/آویختن
200 813 https://vajehyab.com/moein/آونگ
200 640 https://vajehyab.com/moein/بیختن
200 6122 https://archive.org/details/SogdianDictionary
#### d082fb7f4ff31d5a
#### d7f584e33089b31a
#### 369f221e7c9a84f0
#### 2f2c4bfa34f4683a
#### 6e4fbd8837b107b8
#### 6a3bce4daf1bcf4b
#### 607d8bb4c4b93f16
#### f3c21eae0a57bdc8
```


## [2026-10-16T05:20:01.358Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 0898c1b35e41e61a d082fb7f4ff31d5a d7f584e33089b31a 369f221e7c9a84f0 2f2c4bfa34f4683a 6e4fbd8837b107b8 6a3bce4daf1bcf4b 607d8bb4c4b93f16; do echo \"#### $f $(wc -c < $f.txt)\"; grep -i -A4 'Etymology' $f.txt | grep -v '^\\s*$' | head -12; done"
}
```


### [2026-10-16T05:20:01.893Z] TOOL RESULT

```
#### 0898c1b35e41e61a 7066
#### d082fb7f4ff31d5a 18171
 Etymology 
 1.2 
 Pronunciation 
--
 Etymology 
 2.2 
 Pronunciation 
--
 Etymology 
 4.2 
 Noun 
--
#### d7f584e33089b31a 7377
 Etymology 
 1.2 
 Noun 
--
 Etymology 
 2.2 
 Pronunciation 
--
 Etymology
 [ edit ] 
 Etymology tree
 Middle Iranian 
#### 369f221e7c9a84f0 23420
 Etymology 1 
 1.2.1 
 Pronunciation 
--
 Etymology 2 
 1.3.1 
 Pronunciation 
--
 Etymology 1
 [ edit ] 
 Inherited from Middle Persian plwhtn' ( frōxtan , “ to sell ” ) , from Proto-Iranian *fra- ( “ toward, pro- ” ) + *vaxš- ( “ to grow, increase ” ) , the latter from Proto-Indo-European *h₂weks- . [ 1 ] Alternative theories link the second component to Proto-Iranian *wā́xš , from Proto-Indo-Iranian *wā́kš ( “ voice ” ) (whence آواز ( âvâz , “ voice ” ) ), taking the original meaning as "to cry out".
--
#### 2f2c4bfa34f4683a 6750
 Etymology 
 1.2 
 Noun 
--
 Etymology 
 2.2 
 Noun 
--
 Etymology 
 3.2 
 Pronunciation 
--
#### 6e4fbd8837b107b8 4491
 Etymology 
 1.2 
 Verb 
--
 Etymology 1 
 2.1.1 
 Noun 
--
 Etymology 2 
 2.3.1 
 Noun 
--
#### 6a3bce4daf1bcf4b 3239
 Etymology 
 1.2 
 Pronunciation 
--
 Etymology
 [ edit ] 
 From Middle Persian hwnydʾkl ( huniyāgar , “ entertainer, musician ” ) , equivalent to خنیا +‎ ـگر .
#### 607d8bb4c4b93f16 2938
```


## [2026-10-16T05:20:06.711Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in d082fb7f4ff31d5a d7f584e33089b31a 2f2c4bfa34f4683a 6e4fbd8837b107b8 607d8bb4c4b93f16; do echo \"#### $f\"; grep -i -A3 'Etymology$\\|Etymology [0-9]$' $f.txt | grep -i 'from\\|inherit\\|borrow\\|coin\\|cognate' | head -6; done; grep -i 'Derived terms\\|Descendants' -A30 0898c1b35e41e61a.txt | grep -i 'iran\\|avest\\|persian' | head -20"
}
```


### [2026-10-16T05:20:07.119Z] TOOL RESULT

```
#### d082fb7f4ff31d5a
 From Middle Persian ʾwʾz ( āwāč, āwāz , “ voice, sound, tune ” ) , from 𐭥𐭠𐭰 ( wāč, wāz , “ word, speech ” ) , from Proto-Iranian *wā́xš , from Proto-Indo-Iranian *wā́kš , from Proto-Indo-European *wōkʷs . Cognate with Sanskrit वाच् ( vā́c ) and Latin vōx .
#### d7f584e33089b31a
#### 2f2c4bfa34f4683a
 Borrowed from Pashto بانگ or Urdu بانگ , from Persian بانگ .
 From Middle Persian 𐭥𐭠𐭭𐭢 ( ʿʾng /⁠vāng⁠/ ) , probably from Proto-Indo-European *wṓkʷs ( “ voice, speech ” ) . [ 1 ] Akin to Old Armenian վանգ ( vang ) , an Iranian borrowing.
 Borrowed from Classical Persian بانْگ .
 From Classical Persian بَانْگ ( bāng ) .
#### 6e4fbd8837b107b8
 From Middle Persian [Book Pahlavi needed] ( nwʾk' /⁠niwāg⁠/ ) . Compare Old Armenian նուագ ( nuag ) , an Iranian borrowing.
#### 607d8bb4c4b93f16
 Proto-Indo-Iranian: *wíwakti 
 Proto-Indo-Iranian: *wawā́ča ( see there for further descendants )
 Proto-Indo-Iranian: *wáčas ( see there for further descendants )
 Proto-Indo-Iranian: *uktíš ( see there for further descendants )
 Proto-Indo-Iranian: *waktrám 
 Proto-Indo-Iranian: *uktás ( see there for further descendants )
 Indo-Iranian:
 Proto-Indo-Iranian: *uktʰám 
 Proto-Iranian: *uxθám 
 Avestan: 𐬎𐬑𐬜𐬀 ( uxδa , “ word ” ) 
 Proto-Indo-Iranian: 
 Proto-Iranian:
```


## [2026-10-16T05:20:15.335Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 1,200p 607d8bb4c4b93f16.txt | grep -v '^\\s*$' | head -60; echo ----; grep -v '^\\s*$' d7f584e33089b31a.txt | sed -n 1,80p | grep -i -B2 -A4 'middle persian\\|from' | head -30"
}
```


### [2026-10-16T05:20:15.628Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/پژواک
FETCHED: 2026-10-16T05:19:41Z
STATUS: 200
TITLE: پژواک - Wiktionary, the free dictionary
پژواک - Wiktionary, the free dictionary 
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
 Persian 
 Toggle Persian subsection 
 1.1 
 Pronunciation 
 1.2 
 Noun 
 1.2.1 
 Derived terms 
 Toggle the table of contents 
 پژواک 
 4 languages 
 العربية 
 فارسی 
 Malagasy 
 Русский 
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
----
```


## [2026-10-16T05:20:19.269Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' d7f584e33089b31a.txt | sed -n 60,140p"
}
```


### [2026-10-16T05:20:19.655Z] TOOL RESULT

```
 العربية 
 Euskara 
 فارسی 
 Français 
 Magyar 
 Kurdî 
 ລາວ 
 Lietuvių 
 Malagasy 
 Polski 
 Português 
 Русский 
 Sängö 
 中文 
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
 Printable version 
 In other projects
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 Azerbaijani
 [ edit ] 
 A user suggests that this Azerbaijani entry be moved, merged or split, giving the reason: “Latin script”.
 Please see the discussion on Wiktionary:Requests for moves, mergers and splits ( + ) for more information and remove this template after the request has been fulfilled.
 Etymology
 [ edit ] 
 Etymology tree
 Middle Iranian 
 Classical Persian واژه ( wāža ) bor. 
 Azerbaijani واژه 
 Borrowed from Classical Persian واژه ( wāža ) , from a Middle Iranian language.
 Noun
 [ edit ] 
 واژه ( vajə ) ( plural واژه‌لر ) 
 ( South Azerbaijani , semantics ) word 
 Synonym: söz 
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: واژه 
 Wikipedia fa 
 Etymology
 [ edit ] 
 Middle Iranian . Compare Middle Persian [script needed] ( wʾck' /⁠wāzag⁠/ , “ utterance, saying ” ) , Avestan 𐬬𐬀𐬗𐬀𐬵 ( vacah , “ word ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /waː.ˈʒa/ 
 ( Dari, formal ) IPA ( key ) : [wɑː.ʒá] 
 ( Dari, formal ) IPA ( key ) : [wɑː.ʒá] 
 ( Kabuli ) IPA ( key ) : [wɑː.ʒá] 
 ( Hazaragi ) IPA ( key ) : [wɔː.ʒá] 
 ( Iran, formal ) IPA ( key ) : [vɒː.ʒé] 
 ( Tajik, formal ) IPA ( key ) : [vɔ.ʒá] 
 Rhymes: -a 
 Readings
 Classical reading ? 
 wāža
```


## [2026-10-16T05:20:29.733Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=tools/fetch_source.py; for w in واک واژه واژگان واژ گواژه پژواک وخشور خنیا نوا هوخت ونگ بانگ فروختن آوا; do u=\"https://vajehyab.com/moein/$w\"; f=$(python3 $S \"$u\" --note \"page 538, root Wekw: Mo'in entry for $w\" 2>&1 | tail -1); echo \"## $w $f\"; grep -v '^\\s*$' \"$f\" 2>/dev/null | sed -n 5,14p | cut -c1-400; done"
}
```


### [2026-10-16T05:20:35.390Z] TOOL RESULT

```
## واک /home/sfmqrb/git/rishe-private/data/verification/sources/web/83fe640c39ca2682.txt
FETCH FAILED: HTTP Error 404: Not Found
## واژه /home/sfmqrb/git/rishe-private/data/verification/sources/web/efff24733c5427c5.txt
معنی واژه | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 واژه
 فرهنگ انتشارات معین
 (ژِ) [ په . ] (اِ.) لغت ، کلمه .
 واژه در فرهنگ‌های دیگر
 معنی واژه در لغت‌نامه دهخدا 
 معنی واژه در فرهنگ فارسی عمید / قربان‌زاده 
## واژگان /home/sfmqrb/git/rishe-private/data/verification/sources/web/1f5c6939bb731158.txt
معنی واژگان | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 واژگان
 فرهنگ انتشارات معین
 (اِ.) فهرستی از مجموعة واژه های یک کتاب ، یک موضوع یا یک زبان .
 واژگان در فرهنگ‌های دیگر
 معنی واژگان در دیکشنری فارسی به عربی 
 معنی واژگان در دیکشنری فارسی به انگلیسی 
## واژ /home/sfmqrb/git/rishe-private/data/verification/sources/web/82cd38333d3b983b.txt
معنی واژ | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 واژ
 فرهنگ انتشارات معین
 (اِ.) نک . باژ؛ باج .
 واژ در فرهنگ‌های دیگر
 معنی واژ در لغت‌نامه دهخدا 
 معنی واژ در فرهنگ فارسی عمید / قربان‌زاده 
## گواژه /home/sfmqrb/git/rishe-private/data/verification/sources/web/7c941912d1f24bb6.txt
معنی گواژه | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 گواژه
 فرهنگ انتشارات معین
 (گُ ژَ یا ژِ) (اِ.) 1 - طعنه ، سرزنش . 2 - شوخی ، مزاح .
 گواژه در فرهنگ‌های دیگر
 معنی گواژه در لغت‌نامه دهخدا 
 معنی گواژه در دیکشنری فارسی به انگلیسی 
## پژواک /home/sfmqrb/git/rishe-private/data/verification/sources/web/02308b5effdee626.txt
معنی پژواک | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 پژواک
 فرهنگ انتشارات معین
 (پِ) (اِ.) بازتاب صدا در کوه ، طنین .
 پژواک در فرهنگ‌های دیگر
 معنی پژواک در لغت‌نامه دهخدا 
 معنی پژواک در فرهنگ فارسی عمید / قربان‌زاده 
## وخشور /home/sfmqrb/git/rishe-private/data/verification/sources/web/bc35278a932a5501.txt
معنی وخشور | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 وخشور
 فرهنگ انتشارات معین
 (وَ یا وُ) (اِ. ص .) پیغمبر، رسول .
 وخشور در فرهنگ‌های دیگر
 معنی وخشور در لغت‌نامه دهخدا 
 معنی وخشور در فرهنگ فارسی عمید / قربان‌زاده 
## خنیا /home/sfmqrb/git/rishe-private/data/verification/sources/web/586a60fc5fa5ab0d.txt
معنی خنیا | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 خنیا
 فرهنگ انتشارات معین
 (خُ) (اِ.) سرود، نغمه ، آواز.
 خنیا در فرهنگ‌های دیگر
 معنی خنیا در لغت‌نامه دهخدا 
 معنی خنیا در فرهنگ فارسی عمید / قربان‌زاده 
## نوا /home/sfmqrb/git/rishe-private/data/verification/sources/web/d4f8ea3e29a92673.txt
معنی نوا | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 نوا
 فرهنگ انتشارات معین
 (نَ) [ په . ] (اِ.) 1 - نغمه ، سرود. 2 - مال ، دارایی . 3 - نام مقامی از دوازده مقام موسیقی . 4 - گرو، گروگان . 5 - رونق .
 نوا در فرهنگ‌های دیگر
 معنی نوا در لغت‌نامه دهخدا 
 معنی نوا در فرهنگ فارسی عمید / قربان‌زاده 
## هوخت /home/sfmqrb/git/rishe-private/data/verification/sources/web/9d80a951be204e88.txt
FETCH FAILED: HTTP Error 404: Not Found
## ونگ /home/sfmqrb/git/rishe-private/data/verification/sources/web/b476974b1cfa1b76.txt
معنی ونگ | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 ونگ
 فرهنگ انتشارات معین
 (وَ) (اِ.) (عا.) صدای گریة بچه .
 ونگ در فرهنگ‌های دیگر
 معنی ونگ در لغت‌نامه دهخدا 
 معنی ونگ در فرهنگ فارسی عمید / قربان‌زاده 
## بانگ /home/sfmqrb/git/rishe-private/data/verification/sources/web/ffcbada19176db88.txt
معنی بانگ | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 بانگ
 فرهنگ انتشارات معین
 ( اِ.) آواز بلند، فریاد.
 بانگ در فرهنگ‌های دیگر
 معنی بانگ در لغت‌نامه دهخدا 
 معنی بانگ در فرهنگ فارسی عمید / قربان‌زاده 
## فروختن /home/sfmqrb/git/rishe-private/data/verification/sources/web/1bc0dc98c34ccdad.txt
معنی فروختن | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 فروختن
 فرهنگ انتشارات معین
 ( ~ .) (مص مر.) نک افروختن .
 فروختن در فرهنگ‌های دیگر
 معنی فروختن در لغت‌نامه دهخدا 
 معنی فروختن در فرهنگ فارسی عمید / قربان‌زاده 
## آوا /home/sfmqrb/git/rishe-private/data/verification/sources/web/a80c93d105d66e81.txt
معنی آوا | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 آوا
 فرهنگ انتشارات معین
 ( اِ.) آواز، بانگ .
 آوا در فرهنگ‌های دیگر
 معنی آوا در لغت‌نامه دهخدا 
 معنی آوا در فرهنگ فارسی عمید / قربان‌زاده
```


## [2026-10-16T05:20:41.778Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=tools/fetch_source.py; for u in 'https://vajehyab.com/dehkhoda/واک' 'https://vajehyab.com/dehkhoda/هوخت' 'https://vajehyab.com/dehkhoda/پژواک' 'https://en.wiktionary.org/wiki/وخشور' 'https://en.wiktionary.org/wiki/خنیا' 'https://en.wiktionary.org/wiki/گواژه' 'https://www.etymonline.com/word/voice' 'https://www.etymonline.com/word/vocabulary'; do f=$(python3 $S \"$u\" --note \"page 538, root Wekw\" 2>&1 | tail -1); echo \"## $u $f\"; grep -v '^\\s*$' \"$f\" 2>/dev/null | grep -i -v 'jump\\|menu' | sed -n 4,9p | cut -c1-700; done"
}
```


### [2026-10-16T05:20:44.529Z] TOOL RESULT

```
## https://vajehyab.com/dehkhoda/واک /home/sfmqrb/git/rishe-private/data/verification/sources/web/f39dcc1a70e1ea74.txt
TITLE: معنی واک | لغت‌نامه دهخدا | واژه یاب
معنی واک | لغت‌نامه دهخدا | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 واک
## https://vajehyab.com/dehkhoda/هوخت /home/sfmqrb/git/rishe-private/data/verification/sources/web/3ed6fed5d2a1362a.txt
TITLE: معنی هوخت | لغت‌نامه دهخدا | واژه یاب
معنی هوخت | لغت‌نامه دهخدا | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 هوخت
## https://vajehyab.com/dehkhoda/پژواک /home/sfmqrb/git/rishe-private/data/verification/sources/web/42c3159ade3be024.txt
TITLE: معنی پژواک | لغت‌نامه دهخدا | واژه یاب
معنی پژواک | لغت‌نامه دهخدا | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 پژواک
## https://en.wiktionary.org/wiki/وخشور /home/sfmqrb/git/rishe-private/data/verification/sources/web/f3c21eae0a57bdc8.txt
TITLE: 
FETCH FAILED: HTTP Error 404: Not Found
## https://en.wiktionary.org/wiki/خنیا /home/sfmqrb/git/rishe-private/data/verification/sources/web/25cd08a9673859d4.txt
TITLE: خنیا - Wiktionary, the free dictionary
خنیا - Wiktionary, the free dictionary 
 move to sidebar 
 hide 
 Navigation
 Main page 
## https://en.wiktionary.org/wiki/گواژه /home/sfmqrb/git/rishe-private/data/verification/sources/web/77313273dc72f0db.txt
TITLE: 
FETCH FAILED: HTTP Error 404: Not Found
## https://www.etymonline.com/word/voice /home/sfmqrb/git/rishe-private/data/verification/sources/web/0558662caeadb188.txt
TITLE: 
FETCH FAILED: HTTP Error 403: Forbidden
## https://www.etymonline.com/word/vocabulary /home/sfmqrb/git/rishe-private/data/verification/sources/web/99321a4ff2055709.txt
TITLE: 
FETCH FAILED: HTTP Error 403: Forbidden
```


## [2026-10-16T05:20:47.302Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in f39dcc1a70e1ea74 3ed6fed5d2a1362a 42c3159ade3be024; do echo \"## $f\"; grep -v '^\\s*$' $f.txt | sed -n 9,30p | cut -c1-900; done; grep -i -A3 'Etymology' 25cd08a9673859d4.txt | grep -i 'from\\|middle' | head"
}
```


### [2026-10-16T05:20:47.662Z] TOOL RESULT

```
## f39dcc1a70e1ea74
 واک
 لغت‌نامه دهخدا
 واک . (اِ) پرنده ای است کبودرنگ و اکثر در کنارهای آب نشیند و معرب آن واق است . (برهان قاطع) (آنندراج ) (از جهانگیری ) (از فرهنگ نظام ) (از انجمن آرا) (ناظم الاطباء). اسم طایری است از طیور آبی که در کنارهٔ آب می باشد خاکستری رنگ مایل به سیاهی و مخلوط به سفید و سر آن سیاه و در قمهٔ آن سه چهار تا پنج عدد پر مثل موی به شکل کاکل رسته بسیار سفید و نرم و در غایت ملاست و لطافت و حسن و دراز و قریب به یک شبر، و مردم ترک بر کلاه می آویزند.(محیط اعظم ، از حاشیهٔ برهان قاطع دکتر معین ). واک نام جانوری است کبودرنگ که اکثر و اغلب در کنارهای آب نشیند و آن را عوام «واق » گویند. مجد همگر راست :
برف است ریزان در پای گلبن 
زاغ است نالان بر جای بلبل 
در حلق نخجیر آب است زنجیر
در گردن واک موج است چون غل .
(از جهانگیری و رشیدی ، از حاشیهٔ برهان قاطع چ معین ).
 واک در فرهنگ‌های دیگر
 معنی واک در فرهنگ فارسی عمید / قربان‌زاده 
 معنی واک در واژه‌های مصوب فرهنگستان 
 واژه‌های مشابه
 واکن کردن 
 واکنة 
 واکنش 
 واکس زن 
 واکسن زدن 
 واکردنی 
 واکس زنی 
 واکس خورده 
 واکس 
 واکاویدن 
## 3ed6fed5d2a1362a
 هوخت
 لغت‌نامه دهخدا
 هوخت . (اِخ ) هوخ . بیت المقدس باشد. (از برهان ). رجوع به هوخ شود.
 واژه‌های مشابه
 هوختن 
 هاختور 
 هختن 
 هوت 
 هوتان 
 هوتانه 
 هوتخش 
 هوتخشبد 
 هوتس 
 هوتسما 
 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدید
## 42c3159ade3be024
 پژواک
 لغت‌نامه دهخدا
 پژواک . [ پ َژْ / پ ِژْ ] (اِ) آوازی که در کوه و گرمابه و دره و گنبد و مانند آن پیچد. صدا. آواز منعکس . عکس الصوت .
 پژواک در فرهنگ‌های دیگر
 معنی پژواک در فرهنگ انتشارات معین 
 معنی پژواک در فرهنگ فارسی عمید / قربان‌زاده 
 معنی پژواک در دیکشنری فارسی به عربی 
 معنی پژواک در دیکشنری فارسی به انگلیسی 
 معنی پژواک در واژه‌های مصوب فرهنگستان 
 معنی پژواک در فرهنگ مترادف و متضاد 
 معنی پژواک در فرهنگ نام‌ها 
 واژه‌های مشابه
 پچواک 
 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدید
 Inherited from Middle Persian [Book Pahlavi needed] ( hwnydʾk' /⁠huniyāg⁠/ , “ joyful ” ) , from Proto-Iranian *xwan-iyā-ka- , from the same root as خواندن ( xândan , “ to sing ” ) , ultimately from Proto-Indo-European *swenh₂- ( “ to sound ” ) .
```


## [2026-10-16T05:21:08.159Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'pa[zž]v[aā]k\\|pafwäk\\|pazväk\\|pa[zž]wāk\\|pazwak' HRN.txt HUB.txt PHD.txt CHEUNG.txt BRT.txt | head; grep -n \"pauruuatā\\|paurvatä\\|paurvata\\|pauruvat\" BRT.txt | head -3; grep -n '^ *vīvā\\|vi.vā[cč]\\|vivä[cč]' BRT.txt | head"
}
```


### [2026-10-16T05:21:08.487Z] TOOL RESULT

```
4698:\)amm  Y.$4.2,  G,  j.6; — yä  {ar?ävi) 'vaiti fratalaili  Y.  Ö5. 3 ;  Yt.  5. 1 5 ;  —  a^tn  vatau- hlm  .  .  hrpsailTm  'vattTm  Y.  3. 14;  Yt /J. I,  7;  —  drvaspqm  . .  'vaitlm  YL9.2;  — fravaiayö  .  .  yä  'vaifli  Yt  13.  29;  —  at töi  atrjm  . .  *asXsttin  'vanhm  Y.j^4;  — tiiirim  .  .  'vant?m  YtÄ4;  —  vatianttm 'vant»m  Yt  21.  i;  —  °vatS  amai  'vatÖ virp^raynäi  'vat^yO.  »rütyi  'vai'iya aiöii  'vai^ya  astdil  'vaüyä  paurvatälo 'vai'i'yB  uparatälö  'va^byä  yazatoAbyö  Vr. g.i,.  b)  sonst;  uströ . ,  b)r?zB  "vä  Yt i.^.  1 2 ;  —  srlra  urusta  'vaiti  (VSf.)  .  . UfTaireY.it^.iB,Vyt22; — srayarfhö  vouru- ka?ahe  'vatö  Yt.<S.46;  —  vasnm..  zaröil ayanhö  frahixt»m  'vatö  \L  10.96;  —  'vat iimäfum  Y.  57. 10;  —  ptiüm . .  yim  aiwatö 'vantim  Vyt.^;  —  'vaitlm  sitiqin  dävöi (sd.)  dr»gvasa  Y.  44. 14.  —  IstJm  . .  pouru.- sarioam  'vaitlm  Y.  65. 1 1 ;  —  hazö  "vat  Y. jj^.  iz;  —  yahmi  maza  'va  (NSn.l')J' '  iiiäälpm  Yt  10. 64  (?) ;  —  *°vata  vaca  F.3  e. AbleiL  —  ai.  dmm-ant-  Adj.;  vgl.  mp.  (PS.) amäz-nnd.  —  ')  %  jg4.  —  •)  Zur  Zusammen- Stellung  von  amai'aaf-  mit  ^'/ri^ravan ,  viri- %rasan-  s.  'amn-  2.-3)  Wenn  richtig,  wohl Neubildung  lum  NSm.  'va  nach  der  n-Dekt.
7251:zu  *  myaso-ä. Sarana-  und  ♦i^nira-.  —  '«  In  |  Nachsatz  r  cim  Aoxa  . .  ^baraiU  .Ja'  ym Pü.  scheint  *aoM*tD  entsprechen, —  w)  Wennjj'^  glm  baraifi  agsttum  ..  ä  kl  pascalta nicht  -  mp.  äk;  s.  »u  J™.  -  •')  Geschr.  f^^atti  aiar/  .  .  ".  .  wenn  er  ihm  drauf Brennholz  bringt,  alsdann  segnet  ihn  Ä." Y.62.8f.  I  A)  'seit  dem':  äal  (s.i)  ^aiä •  j.,  g,'>  aat  Adv,,  meist  an  der  Spitze  ..  varrfa  viiar^n . .  a-  ahva  paurvatähi-a des  Satzes  stehend'*;  1)  zum  Ausdruck  ,.  vTraö^ahe  Y.io.iii.;  — frä  il  mazdä zeitlicher  Folge 'darauf,  dann,  alsdann,  da' :  i  Mm/  ,.  atmyatahajam  ..  ä°  aiiike  ahi pfnsal  zard^ultrS  ahumn  mazdqm  .  ,  3° .  aiwyäslö  V.p.  26,  2)   zur  Anknüpfung
8751:Lebenskraft'^':  hyat  astvant»m  (sd.)  dada 'tatum  y.j/.  ij;  —  tal  ii  .  .  vairim  ast- rwV?  (sd.)  'tänäi''''  data  Y.^j.,^.  14;  —  at rätqm  zara'^uÜrö  tanvascti  x^ahya  'tattpm dadaiti  paurvatätpm\.33.i^;  —  f^ra  vS rahl  .  .  tanvasclt  c^'ahyS  'tatum  V.  //.  18; /_9.4;  — darsyö.xia'irpm  xsa'^raAe  dury/ö.- jUim  'tilnahe  A.  1.8]  Y.  17. 19;  —  m-^irpswa slün'i  gayehe  mprpzu^a (sd.)  xa  'tänahe  Yt. JO.  7 1 ;  —  avai  he  astt  masyö  ar^i^pm  yat \  'tatum  bttnjayüt  (sd.)  V.  7.  7 1 ;  —  ava \  apamm  (sd.)  gayehe  *frasatu>m  'tanahe  Yt.
```


## [2026-10-16T05:21:12.562Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^voice,\\|^vocabulary,\\|^vocal,\\|^vox,' KLN_1966.txt | head; n=$(grep -n '^voice,' KLN_1966.txt | head -1 | cut -d: -f1); head -$n KLN_1966.txt | tr -cd '\\f' | wc -c; sed -n \"${n},$((n+12))p\" KLN_1966.txt"
}
```


### [2026-10-16T05:21:12.930Z] TOOL RESULT

```
Exit code 1
0
sed: -e expression #1, char 1: unknown command: ','
```


## [2026-10-16T05:21:15.254Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^ *voice\\b\\|^ *vocabulary\\b' KLN_1966.txt | head; grep -n -i 'vox, gen. v\\|vōx, gen\\|vox, vocis' KLN_1966.txt | head"
}
```


### [2026-10-16T05:21:15.575Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:21:18.164Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'voice' KLN_1966.txt | grep -i 'vox\\|vöx\\|vox\\b\\|L. v' | head -10; grep -n -i 'vocabul' KLN_1966.txt | head -5"
}
```


### [2026-10-16T05:21:18.608Z] TOOL RESULT

```
1764:or  counsel)’,  pp.  of  advocare ,  ‘to  call  to  (esp.  ‘to call  to  a  place  for  counsel’)’,  fr.  ad-  and  vocare, ‘to  call’,  fr.  vox,  gen.  vocis,  ‘voice’.  See  voice and  verbal  suff.  -ate  and  cp.  vocation,  avouch, avow.
2653:Anaphe,  n.,  a  genus  of  moths  (700/.)  —  ModL., fr.  Gk.  avx 97,9,  ‘impalpable’,  fr.  av-  (see  priv. pref.  an-)  and  dcp^,  ‘touch,  grip’,  from  the  stem of  aTtTEiv,  ‘to  fasten,  usually  in  the  middle voice  dtcxeaffai,  ‘to  touch'.  See  apsis  and  cp. words  there  referred  to.
4129:Derivative:  avoirdupois,  adj. avouch,  tr.  and  intr.  v.  —  ME.  avouchen,  fr. OF.  avochier,  fr.  L.  advocare,  ‘to  summon  to  a place’,  fr.  ad-  and  vocare,  ‘to  call’.  See  vouch, avoui,  n.,  lawyer,  solicitor.  —  F.,  ‘solicitor’,  fr. L.  advocatus,  ‘advocate’,  prop,  ‘one  called  to aid’,  pp.  of  advocare.  See  next  word, avow,  tr.  v.  —  OF.  avoer,  avouer  (F.  avouer),  fr. L.  advocare,  ‘to  call  to ;  to  summon  to  a  place’, fr.  ad-  and  vocare,  ‘to  call’,  which  is  rel.  to  vox, gen.  vocis,  ‘voice’.  See  voice  and  cp.  advocate, advowee,  avoue.
6211:Calliope,  n.,  the  Muse  presiding  over  epic  poetry 0 Greek  mythol.)  —  L.,  fr.  Gk.  KxXXtoTrrj,  lit.  ‘the beautiful-voiced  one’,  compounded  of  xdXXoi;, ‘beauty’,  and  oip,  gen.  ono?,  ‘voice’.  The  first element  derives  fr.  xaXo?,  ‘beautiful’ ;  see  calo-. The  second  element  stands  for  fr.  *F6ty,  fr.  I.-E. *woqw-s,  whence  also  Gk.  ’inoc,  (Cypriote  rziz’jc), ‘word’,  L.  vox,  ‘voice,  sound,  tone,  call’.  See voice  and  cp.  epic,  epos, calliper,  n.  —  See  caliper.
9070:convicium,  n.,  the  offence  of  reviling  a  person ( civil  law).  —  L.  convicium,  ‘a  loud  noise,  out¬ cry,  reviling,  insult’,  for  *con-vec-iom,  lit.  ‘a speaking  together’,  fr.  con-  and  a  gradational variant  of  vox,  gen.  vocis,  ‘voice,  sound’.  See voice  and  cp.  convoke,  convocation, convict,  tr.  v.,  to  find  guilty.  —  L.  convictus,  pp. of  convincere,  ‘to  prove  guilty’.  See  convince. Derivatives:  convict-able,  convict-ible,  adj.,  con¬ viction  (q.v.),  convict-ive,  adj.,  convict-ive-ly, adv.,  convict-ive-ness,  n.
13451:epos,  n.,  a  primitive  epic  poem.  —  L.,  fr.  Gk.  guop, ‘word,  speech,  tale,  song,  heroic  poetry’,  rel. to  Cypr.  Gk.  f stiop,  of  s.m.,  Gk.  ofy  (for  *r6^), ‘voice’,  Sacra  (for  *foxia),  'voice,  tale’,  ev-ottv;, ‘crying,  shouting,  voice’,  eIttov  (for  ‘ezeittov, fr.  *£-.cE-’jr:-ov),  ‘I  spoke’,  and  cogn.  with  L. vox,  gen.  vocis.  ‘voice’.  See  voice  and  cp.  words there  referred  to.  Cp.  also  epyllion  and  the  se¬ cond  element  in  cacoepy,  orthoepy, epris  (fern,  eprise),  adj.,  enamored.  —  F.,  pp. of  eprendre,  fr.  OF.  esprendre,  ‘to  seize,  kindle’, fr.  es-  (fr.  L.  ex)  and  prendre,  ‘to  take’,  fr.  L. prehendere,  prendere,  ‘to  grasp’.  See  1st  ex-  and prehensile.
13488:Derivative:  equivalent,  n„  1)  something  equi¬ valent;  2)  (chem.)  equivalent  weight, equivocal,  adj.,  dubious,  ambiguous.  —  Formed with  adj.  suff.  -al  fr.  Late  L.  aequivocus,  ‘of equal  voice,  of  equal  significance,  ambiguous.
13489:equivocal’,  which  is  compounded  of  L.  aequus, ‘equal’,  and  the  stem  of  vox,  gen.  vocis,  ‘voice’. See  equal  and  vocal  and  cp.  equivoque.  Late  L. aequivocus  is  prop,  a  loan  translation  of  Gk. 6|xo'jvu(io<;,  ‘having  the  same  name;  equivocal, ambiguous’.
13493:equivoque,  n.,  an  equivocal  term,  a  pun.  —  Late L.  aequivocus,  ‘of  equal  voice,  ambiguous’ (whence  also  F.  equivoque,  adj.,  ‘ambiguous’, equivoque,  n.,  ‘ambiguity’).  See  equivocal, equoid,  adj.,  resembling  a  horse  ( zool .)  • —  A hybrid  coined  fr.  L.  equus,  ‘horse’,  and  Gk. -oeiSyj 5,  ‘like’,  fr.  eTSo?,  ‘form,  shape’.  See equine  and  -oid.  The  correct  form  is  hippoid,  in which  both  elements  are  of  Greek  origin. Equus,  n.,  the  typical  genus  of  the  horse  family (zool.)  —  L.  equus,  ‘horse’,  whence  equinus, ‘pertaining  to  horses’.  See  equine.
13897:evoke,  tr.  v.,  to  call  forth.  —  F.  evoquer,  fr.  L. evocdre,  ‘to  call  out,  summon’,  fr.  e-  and  vocare, ‘to  call’,  from  vox,  gen.  vocis,  ‘voice’.  See  voice, evolute,  n.,  a  curve  which  is  the  locus  of  the  cen¬ ter  of  curvatures  of  another  curve  (geom.)  — L.  evolutus,  pp.  of  evolvere.  See  next  word  and cp.  involute.
431:J.  F.  Bense,  Dictionary  of  the  Low  Dutch  element  in  the  English  Vocabulary.
6688:cassowary,  n.,  a  large  ostrichlike  bird  of  Australia and  New  Guinea.  —  Fr.  Malay  kasuari ,  through the  medium  of  Dutch.  See  F.  Bense,  A  Diction¬ ary  of  the  Low-Dutch  Element  in  the  English Vocabulary,  p.  39.
14884:flfcche,  n.,  an  arrow;  a  spire  (archit.)  —  F.,  ‘ar¬ row’,  prob.  fr.  Frankish  *fliugica,  which  is  rel.  to OLG.  fliuca,  MDu.  vliecke,  of  s.m.  See  Bloch- Wartburg,  DELF.,  p.254,  s .v.fliche.  It.  freccia, OProven?.  flec(h)a  and  Sp.  flecha,  ‘arrow’,  are Teut.  loan  words.  Cp.  fletcher.  Cp.  also  parfleche. fleck,  n.,  spot,  freckle.  —  MDu.  vlecke  (Du. vlek),  rel.  to  ON.  flekkr,  OHG.  flee,  fleccho, MHG.  vlec,  vlecke,  G.  Fleck,  and  cogn.  with L.  plaga,  ‘a  flat  surface;  district,  region’.  See plagal  and  cp.  words  there  referred  to.  For  the Dutch  origin  of  the  English  word  see  Bense, Dictionary  of  the  Low  Dutch  Element  in  the English  Vocabulary,  p.99.
15756:Goth,  gamains,  OHG.  gimeini  (whence  MHG., G.  gemeiri);  see  Bense,  Dictionary  of  the  Low Dutch  Element  in  the  English  Vocabulary, p.  1 1 7.  The  above  words  are  formed  fr.  Teut. pref.  ge-  (see  y-),  and  I.-E.  base  *mei-,  ‘to change’.  See  common,  adj.,  and  cp.  words  there referred  to.
16302:Derivative:  gloss,  tr.  and  intr.  v.,  to  polish, glossary,  n.,  a  collection  of  glosses;  a  partial dictionary.  —  L.  glossarium,  ‘vocabulary  of antiquated  or  foreign  words,  glossary’,  formed with  suff.  -arium,  fr.  glossa.  See  gloss,  ‘inter¬ pretation’,  and  subst.  suff.  -ary.
```


## [2026-10-16T05:21:21.817Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -c $'\\f' KLN_1966.txt; grep -n 'voice,  n\\.\\|voice, n\\.' KLN_1966.txt KLN_1971.txt | head -3; grep -n 'vocabulary,  n\\.\\|vocabulary, n\\.' KLN_1966.txt KLN_1971.txt | head"
}
```


### [2026-10-16T05:21:22.141Z] TOOL RESULT

```
902
KLN_1971.txt:126395:invoice, n. — Fr. earlier invoyes, pi. of obsolete 
KLN_1971.txt:263481:voice, n. — ME. vois, voice , fr. OF. voiz, vois 
KLN_1966.txt:19843:Derivatives:  invit-er,  n.,  invit-ing,  adj.,  invit-ing- ly,  adv.,  invit-ing-ness,  n. invocation,  n.  —  ME.  invocacioun,  fr.  MF.  (=  F.) invocation,  fr.  L.  invocationem,  fr.  invocatus,  pp. of  invocare,  ‘to  invoke’.  See  invoke  and  -ation. invocative,  adj.  —  Formed  with  adj.  suff.  -ive fr.  L.  invocatus,  pp.  of  invocare.  See  invoke, invocatory,  adj.  —  Formed  with  adj.  suff.  -ory fr.  L.  invocatus,  pp.  of  invocare.  See  invoke, invoice,  n.  —  Fr.  earlier  invoyes,  pi.  of  obsolete invoy,  ‘anything  sent’,  fr.  F.  envoy,  now  spelled envoi,  ‘a  sending’,  fr.  envoyer,  ‘to  send’.  See envoy.
KLN_1971.txt:263398:vocabulary, n., 1) a list of words; 2) all the words
```


## [2026-10-16T05:21:24.316Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 263398,263410p KLN_1971.txt; echo ---; sed -n 263481,263500p KLN_1971.txt"
}
```


### [2026-10-16T05:21:24.760Z] TOOL RESULT

```
vocabulary, n., 1) a list of words; 2) all the words 
of a language; 3) all the words used by a person, 
class or people. — ML. vocabuldrium, ‘list of 
words’, fr. L. vocdbulum. See prec. word and 
subst. suff. -ary. 

Derivatives : vocabular-ian, adj. and n. 
vocal, adj. — ME., fr. L. vocal is, ‘uttering a 
voice, sounding sonorous*, fr. vox, gen. vocis , 
‘voice’. See voice and adj. suff. -al and cp. equi- 
vocal, univocal. 

Derivatives: vocal, n., vocal-ism, n., vocal-ist , 
---
voice, n. — ME. vois, voice , fr. OF. voiz, vois 
(F. voix), fr. L. vdeem (whence also It. voce. 
Proven^, votz , Sp., Port, voz), acc. of vdx, 
‘voice, sound, tone, call’, rel, to voedre , ‘to call’, 
fr. I.-E. base * weq w -, * woq w -, ‘voice; to speak’, 
whence also OI. vdcas-, ‘sound, word’, Avestic 
vacah-, of s.m., OI. vakti, vivakti , ‘says, speaks’. 
Toch. A wak, B wek, ‘voice*, Gk. inoq, Cypr. 
Ferros, ‘word, song, narrative’, 6^ (for 
‘voice’, 6oaa (for * Fox i;a), ‘voice, tale’, &v-07nf), 
‘crying, shouting, voice*, OPruss. wackis, 
‘shouting, noise*, wackitwei , ‘to call’, OHG. gi- 
wahan(en), MHG. ge-wdhenen, G. er-wahnen, ‘to 
mention*. Cp. vox, vocal, vocation, vocative, vo- 
ciferate, vowel, advocate, advowee, advowson, 
avocation, avouch, avoue, avow, convicium, con- 
vocate, convoke, equivocal, equivoque, evocation, 
evoke, invocation, invoke, irrevocable, provoca- 
tion, provoke, revocation, revoke, semivocal, tele- 
vox, univocal, viva voce. Cp. also epic, epopee,
```


## [2026-10-16T05:21:28.292Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in $(seq 866 878); do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | grep -o -i '.\\{0,60\\}vox.\\{0,60\\}\\|17[0-9][0-9]' | head -3 | sed \"s/^/$n: /\"; done"
}
```


### [2026-10-16T05:21:50.586Z] TOOL RESULT

```
ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/


ugrep: error: error at position 93
][\x80-\xbf]*){0,60}|17[0-9][0-9]
    exceeds complexity limits___/
```


## [2026-10-16T05:21:52.860Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in $(seq 864 880); do t=$(awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | head -c 120 | tr '\\n' ' '); echo \"$n: $t\"; done"
}
```


### [2026-10-16T05:21:53.717Z] TOOL RESULT

```
864:  relief,  chased’,  verbal  adj.  of  xopsii- siv,  ‘to  work  in  relief,  bore  through’,  fr.  xo- peii?,  ‘s
865: fr.  OProven?.  tartuga,  fr.  It.  tartaruga, which  derives  fr.  VL.  tartaruca,  lit.  ‘the  infernal animal’,  
866:  tornare,  ‘to  turn  in  a  lathe;  to  turn,  fashion’.  See turn  and  -ure  and  cp.  tour, touse,  tr.  and  in
867:  Compounded  of  trachelo-  and  Gk. -xopia,  ‘a  cutting  of’,  fr.  xoprj,  ‘a  cutting’.  See -tomy. tracheo-
868: ain. Cp.  also  trail. Derivatives:  train,  n.  (q.v.),  train-age,  n.,  train¬ ed,  adj.,  train-ing,  n.  and  adj.
869: L.  transfor- matus,  pp.  of  transformdre.  See  prec.  word  and -ation. Derivative:  transformation-al,  adj., trans
870: ,  v.,  and  -ation  and cp.  L.  transportatio,  gen.  -dnis,  ‘migration’. Derivatives:  transportation-al,  adj. 
871: t.,  lit. ‘the  woman  led  astray’,  pp.  of  traviare,  ‘to  lead astray’,  lit.  ‘to  lead  beyond  the  wa
872: ,  Tremandra,  Tremella,  tremulous,  tro¬ mometer.  Cp.  also  terrible  and  words  there  re¬ ferred  to.  Base  *t
873: rank (Roman  antiq.)  —  L.  triarii,  formed  fr.  tres, neut.  tria,  ‘three’  with  suff.  -drii  (sing,  -ariu
874: ivision  of  their  in¬ testines. triclinic,  adj.,  having  three  axes  interesecting  at oblique  angles  (crystallo
875: gonometric,  trigonometr-ic-al, adjs. trigonous,  adj.,  having  three  angles;  triangular. —  L.  trigonus,  fr.  Gk
876: x,  gen.  tripli- cis.  See  triplex  and  -ity  and  cp.  duplicity. triplo-,  before  a  vowel  tripl-,  combining  fo
877:   pp.  of  terere  ‘to  rub, thresh,  grind’.  See  trite  and  cp.  trigo.  For  sense development  cp.  L.  granum
878: T),  ‘tongue  of  the  balance,  balance  ,  orig. ‘the  hole  in  which  the  tongue  of  the  balance moves  about
879: � I.-E.  base  *tro-g-,  *tri-g-  is  an  enlargement  of base  *ter-,  *tr-,  ‘to  go  through,  pass  beyond’. S
880: orcer,  trusser,  trousser,  torser  (F.  trousser), ‘to  pack,  bind,  truss,  fr.  VL.  *torciare,  ‘to  twist’,
```


## [2026-10-16T05:21:57.837Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /voice,  n\\.  —|vocabulary,  n\\./ {print NR-1}' KLN_1966.txt | head; for n in 893 894 895 896 897 898; do t=$(awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | head -c 100 | tr '\\n' ' '); echo \"$n: $t\"; done"
}
```


### [2026-10-16T05:21:58.943Z] TOOL RESULT

```
437
893: id.  Cp.  also uvea,  uvula. uvanite,  n.,  a  hydrous  uranium  vanadate  (min¬ eral.)  —  Coine
894: andering’,  formed with  gerundive  suff.  -bundus  fr.  vagari.  See  va¬ gary.  Derivatives:  v
895: ,  bodies  of  those  who were  slain  in  battle’,  wol,  ‘pestilence’,  OHG., MHG.  wal,  �
896: ��,  nr^  (Hesychius), ‘web’,  L.  pannus,  piece  of  cloth’.  See  pane. Derivative:  va
897:   —  A  hybrid  coined  fr.  vari¬ ola  and  suff.  -ite  (representing  Gk.  -Tty)?  ) ;  so cal
898: agential  suff.  -or. vau,  also  waw,  n.,  the  sixth  letter  of  the  Hebrew alphabet.  —  Heb
```


## [2026-10-16T05:22:04.501Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^ *voice[,.]\\|^ *vocabulary[,.]' SKT.txt | head; grep -n -i 'lemma: \\|^vox' LAT.txt | head -0; grep -n '^ *u[oō]x\\b\\|^uox\\|^vox\\|^ *uōx' LAT.txt | head"
}
```


### [2026-10-16T05:22:04.952Z] TOOL RESULT

```
21012:voice.  (F.-L.)  M.  E.  bw.  O.  F. cvtV  (F.  fw'jr).  —  L.  uocem,  occ  of  Mur, voice,  sound.
```


## [2026-10-16T05:22:07.654Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 21012,21016p SKT.txt; grep -n -i 'vocabulary' SKT.txt | head -3; grep -n -i 'uōx, uōcis\\|uox, uocis\\|vōx, vōcis' LAT.txt | head -3"
}
```


### [2026-10-16T05:22:07.973Z] TOOL RESULT

```
voice.  (F.-L.)  M.  E.  bw.  O.  F. cvtV  (F.  fw'jr).  —  L.  uocem,  occ  of  Mur, voice,  sound.
vouch,  to  warrant.  (F.— L.)  O.  F. VQuchtr^  'to  vouch,  cilc.  pray  in  aid  in  a suit  ;•  Cot.-L.  uccare,  lo  call,  call  upon M/Rikiitft.  — i.  M9I-,  ateu  oi  mac,  voice.
VOLTAIC.
vouchsafe.  cF.— L.)    Fo ta/e^  i.e.  warrant  as  safe;  from  mm M/e.
vowel.  (F.  -  U )  F.  twrr^A, ' «  n Cot.  — L.  uo(aiem,  ace.  of  uecaiis  ( a  vowel,  vocal  letter;  »ee  Vooal.
```


## [2026-10-16T05:22:11.229Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"'voice\\|‘voice\" IEC.txt | head -8 | cut -c1-400"
}
```


### [2026-10-16T05:22:11.517Z] TOOL RESULT

```
2967:dhoin- (1) ‘voice, singing, revelry, song’. WP I, 830 Skt. dhenā (2) queried: ‘speech, voice’; Gk. thoíne ‘feast, sacrifice’; Li. dainà ‘folksong’; Latv. daiņa, id. (*-13)
3993:gəuəros, à, us ‘noise, chatter’. Cf. g2år-. (Gk. and W. Ir. ambig.) Gk. gërus, Doric -à- ‘voice, speech; OW gawr ‘shout, battle’; MIr. gáir ‘laughter’; OCS govorü ‘din, tumult’; Cz. hovor ‘speech’
4812:gholsos, à ‘sound, voice. WP I, 538. Cf. gholdhos, gholio, gholos G Gelse ‘gadfly’; gelsen, v. “hum”; OCS glasü, R gólos ‘voice’; (The G forms are ambig. cf. *ghelsos: Cz. hles)
5592:$aros, is, us ‘voice, noise, cry’. (cf. gouor- for alternatives). WP I, 537 Skt. (-ă-) cf. járe, mp., Av. jar- ‘cry, bawl; creak’; Per. zar? (lamentation’. Ambig. cf. guel-); Oss. zar ‘singing, song"; zarin, v. ‘sing’; Arm. cf. (?) ci-carn (‘swallow — bird”, in view of ci- cayim, v. ‘laugh’, as an extn. of cay laughter"); Gk. (ambig.) gérus, (Dor. -à-) ‘voice’; Ir. gáir ‘cry, laugh”; gáire ‘l
5900:$£uhen- (guhon-, guhn-) ‘sound; resound’. See next & ĝuenghõ, &uhon- Skt. jhanarni, v. id.; Alb. zâ, gs záni (T: zë, gs zëri) ‘voice, sound’; cf. pé-zàj, bzáj ‘bawl’; për- zâj (2), id.; Lat. (o-gde) honos, honor beside hones-tus (*&uhonos, -es-; OCS zvonů “sound, bel; Pol. dzwon, id. beside OCS (z-gde in i-basis) zvínjo, -čti ‘resound’ and zví- nú, pl. zvir évy ‘noise’; Latv. zvans "bell" WP 
5910:voice’. WP I, 642. Cf. 8uhen- Skt. cf. jbanàmi “sound”, v.; Av. hizu, gs hiz- vð & hizva, f., hizvo, gs hizváh-, n. ‘tongue’; Ober, hazána-, m., id.; Pers. hazvàn, zabàn, id. (and speech: Arm. dzajn, i-st. ‘voice’ be- side dzoni, vo, eav, adj. ‘consecrated’; s. ‘idol; Alb. zâ, gs zàni “voice, sound"; (T zë, gs zëri); Lat. honos & honor ‘honour’; OCS and com. Sl. zvonü ‘sound, bell": Pol. dzwo
5919:$uhutos (8hütos) ‘called’, etc. See ĝuhuð, £uhuos Skt. hütáh; Av. züta-; MIr. guth ‘voice’; MHG guft ‘shout’
6341:ialo ‘exult, revel. Cf. WP I, 775 Gk. cf. denom. zelóo *be zealous' beside Hes. ialía ‘voice’; OBr. iol- ‘pray’; W ioli “praise, worship’; MLG jolen ‘exult’; Du. joelen “re- vel, exult’. See next
```


## [2026-10-16T05:22:17.388Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^uoq\\|^ueq\\|^uōq\\|^uok\" IEC.txt | head -8 | cut -c1-500"
}
```


### [2026-10-16T05:22:17.699Z] TOOL RESULT

```
20012:uequó (uequmi, uiuéqumi) “call, say, speak, ask’. Cf. uoóqu-. WP I, 245 Skt. vátmi, vakmi, vívakmi, 2, 3s: vaksi, vakti, *say, speak, tell, name, call, announce, des- cribe, reproach’; pp: uktáh, inf: váktum; Av. vað-, v. ‘talk’; Per. güvam, inf: guftan, v. ‘say’; Tokh. B wek-, v. ‘say, speak’; Arm. (?) goéem, v. Cer, if to Skt. vivaksami ‘wish to say"); Gk. eípo, v. ‘say’; Olr. cf. in-fét, 3s. ‘tells’; pf: in-féccid (sic) “he told’; OCz. vece Che said”: inf: vecéti); OPr. wack-, v. ‘cal? 
20013:uequtió cf. uequó
```


## [2026-10-16T05:22:28.316Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n 'WEKW\\|WEKʷ\\|WEK' ARY_latin_index_pages.txt | head; for w in آواز واژه بانگ فروختن نوا وخشور گواژه; do echo \"== $w\"; grep -n \"$w\" ARY_pages.txt | head -3; done"
}
```


### [2026-10-16T05:22:28.842Z] TOOL RESULT

```
1848:*KWEK., *KWOK-, *KWEKS (INDO-EUROPEAN) ,s2layy 9 4
4484:KWEKW, CUCHTAR COCERE AUTALIAN) gis!
10979:j SHEST AARUSSIAN) guys HEKS, WEKS, HEX (GREEK) gly
14963:HWEK HITTITE) nen WAK (TOKHARIAN A) A 6555
14964:WEK :(TOKHARIAN B) B jis"
15224:FEN HOLD IRISH) 45 5-4) 2 WEKHTO, OCHEIN (GREEK) gli»
== آواز
2061:ِ آواز | ۷۳
13333:۰ | لالايي لای لای (به چم "آواز برای خواباندن کودک»)
15208:چم اين واژه در زبان‌های رومانس: صداء آوازه,
== واژه
14:هدف این کتاب نشان دادن ریشه‌ی هند و اروپایی واژه‌های فارسی ناب است. این هدف موجب
17:۱- هیچ واژه‌ی فارسی که ریشه‌ی هند و اروپایی آن ناشناخته است آورده نشده است. صدها
18:واژه‌ی فارسی وجود دارد که ریشه‌پابی آنها تا حد پهلوی و اوستایی و حتی پارسی‌باستان پیگیری
== بانگ
554:در سال ۱۸۱۳ ناماس بانگك (۷01-۸60 171011۸8) واژه‌ی «هند و اروپایی»
== فروختن
4390:چم این واژه در زبان یونانی؛ فروختن.
== نوا
47:«هند و اروپایی» نامی است که به خانواده‌ی بزرگی از زبانها داده می‌شود. این خانواده شامل
75:خانواده‌ی بزرگك از هندوستان و فلات ایران تا باختر اروپا و بریتانیای کبیر گسترش دارند. برخی
82:تنها در اشاره به یک خانواده‌ی بزرگك زبانها بلکه در اشاره به تیره‌ی بخصوص از نژاد سفید بکار
== وخشور
== گواژه
```


## [2026-10-16T05:22:32.727Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 14955,14970p ARY_latin_index_pages.txt; sed -n 2050,2070p ARY_pages.txt; head -14963 ARY_latin_index_pages.txt | grep -o 'pdf page [0-9]*' | tail -1; head -2061 ARY_pages.txt | grep -o 'pdf page [0-9]*' | tail -1"
}
```


### [2026-10-16T05:22:33.199Z] TOOL RESULT

```
|
|
HOLD HIGH GERMAN) yf lS HAVESTAN) glee 31
GIWAHNEN VAXSH, VAK., VACHAH
(GERMAN) glJT (PAHLAVI) 65 gla
ERWAHNEN, GIWAHT WAZ, VACHAK, WAZAG, VAJ,
VOICE, (il j!}(ENGLISH) lS) VAK, VACAK. HOSSETIC) ix gh
WACKIS —:(OLD PRUSSIAN) oS gs 4 BEJE, VATIN (KURDISH) 52,5
HWEK HITTITE) nen WAK (TOKHARIAN A) A 6555
WEK :(TOKHARIAN B) B jis"
REFERENCES entKeay SANSKRIT) cy Sle
POKORNY, «11384136. VK, VAKAS, VAKTI, VIVAKTI
BARNHART: (WoICE) 210 cociey ARMENIAN) «s,)
DELAMARRE: (PARLER) 293 EPOS, E(W)EIPON (GREEK) oly
MACKENZIE: VOX, VOCEM LATIN) 3
(WORD) 140, (SAYING) 131 voIx AFRENCH) Wil
,۸۷۷۸8 ,ش۲7۸8لم۸ م۸ دانمارکی (0۸271874): ۸
یونانی (7)0677 لاد | سرئدی (81780[157): ۸۳۸
لانین (/710مل): 1 نروژی (/۸/0737801۸): ۸
گرنبکه (007112): 3 هلندی (1[ج017): و ادزرن ۹

ابسلند یگهن (10۸1۸۸7 یه صاه): اسلاوی کهن (314۲76 بل #نال) صان):

۸ ,0752
ساکسونی کهن (54200۸0 ۰:02 بال۸711۸
[pdf page 72]
1 :
ِ آواز | ۷۳
۱ لینرانی (۸/1۵00تالل )+ ,۸1۸5 پسگشت‌ها شمیت ۲
۸۲۳۸2۸8 97 ۸0805200
لتونی (لتی) (7۷1494): 1028 9 (077183) +8۸77
پروسی کهن ((2255 صام. ,۸۷1۳85 6 (7غ75۸) :15 ۸۸22/2
نی انا 6 (07583)
5 (07337) :01025
7 (07852) 3537
4 (07358) ۸0400
برهان قاطع + ۶۳
pdf page 512
pdf page 72
```


## [2026-10-16T05:22:37.364Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 14925,14955p ARY_latin_index_pages.txt; awk 'BEGIN{RS=\"\\f\"} /pdf page 512\\]/' ARY_pages.txt | head -50"
}
```


### [2026-10-16T05:22:37.674Z] TOOL RESULT

```
seth
WET olay sea sates 9 coe Ab ol lanl Sia bee pi ool y Sky lal glenfly Gell
eal aed ant (LE) lh yy! y te Set ely she ya eel SS i
[pdf page 511]
(Sg opal Cally” CNet pi 4) 95 [ONT
> NOIB,NIA = :(OLD IRISH) 5543p) NAIBA- ——:(OLD PERSIAN) kel) gs),
NWYF, NWYD (WELSH) $3) NEV PAHLAVI) «5 shay
- LATIN) 3
‘REFERENCES eh NITEO, NITERE, NITIDUS, NITOR
POKORNY, 7600S NEITH GOTHIC) 3,6
‘MACKENZIE: (BRAVE) 105 NID (OLD SCANDINAVIAN) 4S 514!
rry tabi oly NITH {OLD SAXON) oS gf SL
NID HOLD ENGLISH) oS gJS
Jeetlaok
seed 9 Bore Sb hr 2egy} Sbasly 52 Sy ge mY
andy (Dba (Sate iV GWG 22 05s Gal
etl tals oat 3t "SS" "SS" lenjly LEY
NGVALAL, NGHVATAL AVESTAN) glen)
"YSANSKRIT) ey Sunil GUSHAYAT., NI-GAOSH
GHOSHATI, GHOSAYATI GAUSHA- :(OLD PERSIAN) ime go
HEUS LATIN) gd PAHLAVD <3 Jy
NIGHOSHITAN, NIOXSHIDHAN
‘REFERENCES bey QUSIN, GHOSSUN — :(OSSETIC) 5)
POKORNY: 454 BALUCHD gz ge
MACKENZIE: (HEAR) 117 NIGOSHAG, NIGHOSHAGH
vera tabi dey MAFGHANI) (4) gl!
Jeetheal
foay tata abs 22 3s cel
[pdf page 512]
ONT I gly ccly ceils
|
[pdf page 512]
واژه وات» واج / ۵۱۳
ا
ا
اوستایی (/۸۷:87۸4۸): آلمانی کهن ((08704۸ الا 02):
7 ۷۸6 ,۷۸84 0
پهلوی (/۷ل۳۸): آلمانی (/0870):
,۵ ,۷۷27۸0 ,۷۸۲۸4 ۷/۸ 7 ,33۷/21105
اومنتی (083387/6): ۷۸۸ ,۷۸ انگلیسی (ن5ل0/0ق)(از فرانسه) ۷۵168
کردی (7/015): ,85[5 پروسی کهن (للماکونا ۲۲ ۰:۵۵ ۷۷۸۲۴۶
تخاری ۸4 (۸ (4ل1۸7ل707)+ ۷۸ هنیت (۷/77/78]): رانا
*تخاری 8 (8 [(4ل7۸7ل70): ۷
سانسکریت (5۸۸/5/7): پسگشت‌ها اش بر ردنا
5 ۷۸ رکشل ۷ بل 11351136 ۸0/0700
ارمتی (474827]400): 00057 0 ۷۵۲۴۵ 7
بونانی ۰۰۲۵۵۵ ۸8۲۳۵۲ ,۸805 3 (۳۸۲۴3) :0525
لاتین (/710صا): 7 ,۷0۵ لت مان شا
فرانسه (۳8۵(/1)+ ۷ 1 (5۸130) ,140 (۷۵32)
اسپانیایی (5۳۸//8): ۷085 1248 مناه
ایتالیایی (/4ا7۸)): ۷0 5 (۷۵]۳5) +02/100/5
رومانی ((۸4۸(/]4): ۷0 8 (۷0۵165) +547
پرتفالی (00870011858)+ ۷2 1 (۷۵۴۵) امزکن ا درد
ایسلندی کهن (/(070۸14/همک (0): 137 تخا اس
۷۸۳7۸ برهان قاطع + ۳ ۲۲۴۴و ۲۲۴۸
4 8 پیوداشت:
7 چم این واژه در زبان‌های اریچیو پروسی کهن: فریاد» داد زدن.
چم این واژه در زبان‌های تب و ایسلندی کهن: گواهی» شهادت دادن.
چم‌اين واژه در زبان‌های آلمانی: ذ کر کردن» گفتن.
چم اين واژه در زبان‌های رومانس: صداء آوازه,
```


## [2026-10-16T05:22:44.980Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 72\\]/' ARY_latin_index_pages.txt | head -40"
}
```


### [2026-10-16T05:22:45.283Z] TOOL RESULT

```
[pdf page 72]
|
wf ht |
‘REFERENCES bethany ANTRAS, LITHUANIAN) «i }
POKORNY ~S~S~*~*«SS*CT ANTARAS
BARNHART: (OTHER) 739 UOTRS (LATVIAN) (3) gis
‘MACKENZIE: (THAT) 136 ANTERS, (OLD PRUSSIAN) eS 3.4
(OTHER) 126, ANTARS
ONIONS: (OTHER) 635
SKEAT: (OTHER) 417
AMINDAROV: (OTHER) 264
Pr seb ily
leatloal
Farce th oth shanty Soo 9 Sa 9 A Ng ees! SOILS 22 cal
WACKITWEI, EN-WACKEMAL (AVESTAN) esl
(OLD IRISH) oS 434) UXTA., VAC, A-VAXSH
FDAIM, FOCCUL ‘AWAZ, AVAC (PAHLAVI) 5 3h,
AASANSKRIT) ey Sail
REFERENCES tek] AVEC, VAVacA, VicavaTy, AVOcAM
POKORNY, —~=~=S~S*C«SMSSAALG OPA * GREER) pliy
DELAMARRE: (VOIX) 110 VOX, VOCARE. (LATIN) oa
‘MACKENZIE: (VOICE) 139 VOISER ERENCH) wij aq
BUCK: (VOICE) 1248 OLD SCANDINAVIAN) “Sissel ‘
2) 1 bu dy OMUN :
LATVIAN) (2) 33
leetloal
ashy 4 Sy
```


## [2026-10-16T05:22:51.306Z] TOOL CALL #93: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe-private/site/pages/538.jpg 2>&1"
}
```


### [2026-10-16T05:22:51.656Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   80k sfmqrb 14 Oct 22:15  /home/sfmqrb/git/rishe-private/site/pages/538.jpg
```


## [2026-10-16T05:22:54.098Z] TOOL CALL #94: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/538.jpg"
}
```


### [2026-10-16T05:22:54.130Z] TOOL RESULT

```

```


## [2026-10-16T05:23:11.456Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; grep -v '^\\s*$' web/25cd08a9673859d4.txt | grep -i -A3 'Inherited\\|References\\|Hasandust\\|Cheung' | head -20; grep -n 'خنیا' refs/BQT_v2_pages.txt | head"
}
```


### [2026-10-16T05:23:11.807Z] TOOL RESULT

```
 Inherited from Middle Persian [Book Pahlavi needed] ( hwnydʾk' /⁠huniyāg⁠/ , “ joyful ” ) , from Proto-Iranian *xwan-iyā-ka- , from the same root as خواندن ( xândan , “ to sing ” ) , ultimately from Proto-Indo-European *swenh₂- ( “ to sound ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /xun.ˈjaː/ 
--
 Categories : Persian terms inherited from Middle Persian 
 Persian terms derived from Middle Persian 
 Persian terms inherited from Proto-Iranian 
 Persian terms derived from Proto-Iranian 
 Persian terms derived from Proto-Indo-European 
 Persian terms with IPA pronunciation 
5256:‫و خنیا کر باشد ‪٩‬‏ ‪ -‬و بضم اول رسول و پیقمبر‬            ‫چرغند است که چراغ ‪ -‬وچراغدان وچراغ پابه‬
13891:‫حنیدن = شتح اول بر وزن رسدن »‬                             ‫خنیا‪ - ۲‬نم اول بر وزن دیا » سرود‬
13893:     ‫پیچیدنآواز گروایند درکوه وحمام کن‬                   ‫و ساز واغمه باشد ‪ .‬جه خنیا گرخو اننده وساز الم‬
13922:                             ‫_ رك‪ :‬خنیدن‪.‬‬    ‫‪۳‬‬       ‫خنیاکرادت ‪ »..‬لفت فرس ‪ . » ۸‬رك ‪ :‬خنیاگر ‪.‬‬
13940: ‫‪ #‬خنیاگر ‪ -‬بم اول و فتحپنجم از‪ :‬خنیا (ه‪.‬م‪ + ).‬کر ( پوددفاعلی و مبالفه )ء‬
13943:                                                                       ‫مقنی » خواننده [ رك ‪ :‬خنیا] ‪:‬‬
13944:          ‫بشکست نای دکرف وطنبور کدنرار‪.‬‬                       ‫خنیا کرات فاخته و عندلیب را‬
23132: ‫رسیده وفوقانی مفتوح بنون زده » نام قصبه‌ایست‬                              ‫مطرب و خنیا کر راکوبند که خواننده وسازنده‬
30395:        ‫چه ستارگزهره ربةالنوع خنیا کرت‬                     ‫‪۴‬‬          ‫ستارةآسمان‌سوم_وشکوفه» « منتهی الارب» ‪.‬‬
35395: ‫خنیا گر ومطربی‌بوده بی‌عدبل ولظیر ‪ ۷‬کونابه‬                ‫‪-‬‬       ‫شد‬
```


## [2026-10-16T05:23:14.555Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 13885,13945p BQT_v2_pages.txt | sed 's/  */ /g' | grep -n 'خنیا\\|hu\\|nivāk\\|نوا\\|پهلوی\\|اوستا\\|۷۵' | head -20; head -13891 BQT_v2_pages.txt | tr -cd '\\f' | wc -c"
}
```


### [2026-10-16T05:23:14.900Z] TOOL RESULT

```
7:‫حنیدن = شتح اول بر وزن رسدن »‬ ‫خنیا‪ - ۲‬نم اول بر وزن دیا » سرود‬
9: ‫پیچیدنآواز گروایند درکوه وحمام کن‬ ‫و ساز واغمه باشد ‪ .‬جه خنیا گرخو اننده وساز الم‬
37: ‫= خوش نوا] ( خوش آهنکه » موسیقی )‪ .‬اسدی کوبد ‪ « :‬دواء یکی ‪ :‬نوای‬ ‫‪۱‬‬
38: ‫_ رك‪ :‬خنیدن‪.‬‬ ‫‪۳‬‬ ‫خنیاکرادت ‪ »..‬لفت فرس ‪ . » ۸‬رك ‪ :‬خنیاگر ‪.‬‬
56: ‫‪ #‬خنیاگر ‪ -‬بم اول و فتحپنجم از‪ :‬خنیا (ه‪.‬م‪ + ).‬کر ( پوددفاعلی و مبالفه )ء‬
58: ‫پهلوی ‪ < 621۵۷10۱‬اوبوالا ‪[ »۷۰۲‬رك ب‬
59: ‫مقنی » خواننده [ رك ‪ :‬خنیا] ‪:‬‬
60: ‫بشکست نای دکرف وطنبور کدنرار‪.‬‬ ‫خنیا کرات فاخته و عندلیب را‬
235
```


## [2026-10-16T05:23:16.366Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 13915,13925p BQT_v2_pages.txt | sed 's/  */ /g'"
}
```


### [2026-10-16T05:23:16.791Z] TOOL RESULT

```
 ‫مان‬
 ‫ا)لد‬
 ‫زوا‬
 ‫‪+‬راك (ب‬
 ‫< اوىرالا ‪ | »۵۰۲‬از ‪ :‬هو ) بيك ) ب‬ ‫نصا‬ ‫‪-‬هلوی‬
 ‫‪ ۱‬ب‬
 ‫= خوش نوا] ( خوش آهنکه » موسیقی )‪ .‬اسدی کوبد ‪ « :‬دواء یکی ‪ :‬نوای‬ ‫‪۱‬‬
 ‫_ رك‪ :‬خنیدن‪.‬‬ ‫‪۳‬‬ ‫خنیاکرادت ‪ »..‬لفت فرس ‪ . » ۸‬رك ‪ :‬خنیاگر ‪.‬‬
 ‫‪210‬‬
 ‫‪,-‬‬‫‪2110‬‬ ‫_سم مفمول از «خنیدن» ‪022‬‬
 ‫‪01-0‬‬ ‫‪ ۴‬ا‬ ‫‪8‬‬ ‫رك‪ :‬خشده‬ ‫‪۳‬‬
```


## [2026-10-16T05:23:35.649Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'paurvat\\|pauruuat\\|parvat' SYN.txt | head -5 | cut -c1-300; awk 'BEGIN{RS=\"\\f\"} NR==51' SYN.txt | grep -o 'Skt[^.]*parvata[^.]*\\.' | head; awk 'BEGIN{RS=\"\\f\"} NR==50' SYN.txt | head -c 600"
}
```


### [2026-10-16T05:23:35.987Z] TOOL RESULT

```
955:line hill Pol. gora; pagérek, Sp. montajia; colina, cerro Du. berg; heuvel wzg6rek Rum. munte; deal, colina OHG _ berg; buhil, houc Russ. gora; cholm Ir. sliab; telach, cnoc, bri MHG berg; biihel, hiibel, Skt. giri-, parvata-, acala-, NIr. — sliabh; cnoc (tulach) houc etc. W. mynydd; bryn (bre) 
1016:Skt. parvata- ‘mountain, mountain range, rock’, Av. paurvata- ‘mountain range’, fr. adj. Skt. parvata- ‘knotty, rugged’, fr. parvan- ‘knot’.
acq 128 f.
2. Lat. mons, montis (> It. monte, etc.), W. mynydd, Corn. meneth, Br. menez ‘mountain’, Av. mati- ‘mountain top’, fr. the root seen in Lat. é-, pré- mineére ‘stand out, project’ (cf. NE eminence, prominence in physical sense), minae ‘projecting points, threats’. Walde-P. 2.263. Ernout-M. 628 f.
Lat. adj. monténus, VLat. *mon- taneus (cf. subterrdneus, etc.), neut. pl. *montanea ‘mountainous regions, moun- tain chain’, whence It. montagna, OFr. montai(g)ne (> ME mountain), Fr. montagne, Sp. montafia, which have en- croached on the shorter form or even displac
```


## [2026-10-16T05:23:42.319Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; head -5 0898c1b35e41e61a.txt; grep -v '^\\s*$' 0898c1b35e41e61a.txt | grep -i 'speak\\|wṓkʷs\\|Latin\\|Avestan\\|Persian' | head -15; grep -i 'from Middle English\\|Old French\\|Latin vōx\\|vōcem' 8b0e91af1f892d36.txt | head -3; grep -i 'vocabular' 67b3ff4090a96b56.txt | head -3"
}
```


### [2026-10-16T05:23:42.610Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-
FETCHED: 2026-10-16T05:19:38Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/wekʷ- - Wiktionary, the free dictionary

 to speak , to sound out
 Avestan: 𐬎𐬑𐬜𐬀 ( uxδa , “ word ” ) 
 ^ De Vaan, Michiel ( 2008 ), Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN 
 From Middle English voice , voys , vois , borrowed from Anglo-Norman voiz , voys , voice , Old French vois , voiz (Modern French voix ), from Latin vōcem , accusative form of vōx ( “ voice ” ) .
 From Middle English voysen , voicen , from the noun (see above).
 English terms inherited from Middle English
```


## [2026-10-16T05:23:46.095Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/vocabulary' 'https://en.wiktionary.org/wiki/vocabulum' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wáčah' 'https://en.wiktionary.org/wiki/هوخت'; do f=$(python3 tools/fetch_source.py \"$u\" --note \"page 538, root Wekw\" 2>&1 | tail -1); echo \"## $u $f\"; head -3 $f | tail -1; grep -i 'from \\|borrowed' $f | head -3 | cut -c1-300; done"
}
```


### [2026-10-16T05:23:48.451Z] TOOL RESULT

```
## https://en.wiktionary.org/wiki/vocabulary /home/sfmqrb/git/rishe-private/data/verification/sources/web/f5244b27a9b4de84.txt
STATUS: 200
 From Wiktionary, the free dictionary
 Learned borrowing from Medieval Latin vocābulārium . Doublet of vocabularium .
 2018 , Clarence Green, James Lambert, “Advancing disciplinary literacy through English for academic purposes: Discipline-specific wordlists, collocations and word families for eight secondary subjects”, in Journal of English for Academic Purposes , volume 35 , →DOI , page 106 : Vocabulary provides 
## https://en.wiktionary.org/wiki/vocabulum /home/sfmqrb/git/rishe-private/data/verification/sources/web/25011dcbe524880a.txt
STATUS: 200
 From Wiktionary, the free dictionary
 From voc(ā) ( “ to call ; to summon ” ) + -bulum .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=vocabulum&oldid=90316541 "
## https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wáčah /home/sfmqrb/git/rishe-private/data/verification/sources/web/cb295e1cf95f9c8c.txt
STATUS: -1
## https://en.wiktionary.org/wiki/هوخت /home/sfmqrb/git/rishe-private/data/verification/sources/web/63648ad3f959d45b.txt
STATUS: -1
```


## [2026-10-16T05:27:26.939Z] TOOL CALL #101: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-538.json",
 "content": "{\n  \"pdf_page\": 538,\n  \"book_page\": 508,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-16\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Wekw, Weqw\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *wekʷ- 'to speak' (Pokorny 1135-1136 u̯ekᵘ-; LIV² 673f.; Watkins wekw-; o-grade root noun *wṓkʷs 'voice')\",\n      \"note\": \"Root, label and gloss are correct: Pokorny 1135 u̯ekᵘ- 'sprechen' with Skt. vakti, vāc-, vacas-, Av. vac-, vacah-, vāxš, Gk. épos, ops, Lat. vōx, vocāre (WP I 245f.). Cheung 2007 (*u̯ač) and Wiktionary agree. The Latin/English branch and the Avestan vāč-/vacah-/uxδa- branches are textbook. The weaker parts of the chart are the Iranian compounds Nourai reconstructs or invents to reach particular New Persian words: 'paurvatâ-vac' (for pažvāk), 'hu-ni-vak' (for xonyā), Avestan 'vaxš-ô-bara' (only a reconstruction *vaxša-bara- behind MP waxšwar) and 'Old Persian wâk/wânk' (not attested). The derivation of xonyā (MP huniyāg) from *hu-ni-vāka- is opposed by the Middle Persian form, which has no -w- (see node 9). forūxtan 'sell' is linked to vac- by Justi/Horn/Mo'in, but Cheung puts it under *waxš- 'grow' (see node 4). The extraction matches the printed page (checked against site/pages/538.jpg).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *wekʷ- «سخن گفتن» با بالاگونهٔ o در نام‌واژهٔ *wṓkʷs «آواز، صدا» در پوکورنی (ص ۱۱۳۵-۱۱۳۶)، والده-پوکورنی (ج ۱، ص ۲۴۵)، واتکینز و چونگ آمده است. بازمانده‌های آن سنسکریت vāc- و vacas-، اوستایی vāč- (حالت فاعلی vāxš) و vacah- «سخن»، یونانی épos و لاتینی vōx و vocāre است. ریشه و زبان و معنایی که نورایی داده درست است. ولی چند ترکیب ایرانی در این نمودار ساختهٔ خود اوست و در متن‌ها نیامده، مانند paurvatâ-vac و hu-ni-vak و vaxš-ô-bara. پیوند «خنیا» با این ریشه هم با پژوهش امروزی سازگار نیست.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:1135\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt l.90116ff. 'Root / lemma: ueḱ- (*hueḱᵘ-) / Meaning: to speak / Material: Old Indic vakti, vivakti says, talks, speaks ... Avestan vac- speak, uxta-. Old Indic vacas- = Avestan vacah (= gr. épos) discourse, word ... vāk = Avestan vāxš (= Latin vox) voice, discourse, word ... Latin vox, vocis voice, voco, -are call ... References: WP. I 245 f.' Page(s) 1135-1136.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I 245-246 (WLD_Bd1_pages.txt l.22850ff., leaf 253)\",\n          \"stance\": \"supports\",\n          \"note\": \"'uekᵘ- „sprechen“. Ai. vákti, vivakti „sagt, redet, spricht“ ... av. vac- „sprechen“, uxta- ... ai. vacas- n. = av. vacah- (= gr. épos) „Rede, Wort“ ... ai. vāc-, n. sg. vāk = av. vāxš (= lat. vox) „Stimme, Rede, Wort“ ... lat. vox vocis „Stimme“, voco, -āre „rufen“'.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 s.v. wekw-\",\n          \"stance\": \"supports\",\n          \"note\": \"AHD_watkins1985.txt: 'wekw-. To speak. 1. O-grade form *wokw- in: a. Latin vox (stem voc-), voice: VOCAL, VOICE, VOWEL ... 2. Suffixed o-grade form *wokw-a- in Latin vocare, to call: VOCABLE, VOCATION ... 3. Suffixed form *wekw-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekw- 1135.]'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"s.v. uequó\",\n          \"stance\": \"partial\",\n          \"note\": \"IEC.txt l.20012 'uequó (uequmi, uiuéqumi) call, say, speak ... WP I, 245 Skt. vakti ... Av. vač-, v. talk; Per. gūyam, inf: guftan, v. say' -- Mann has the root but wrongly files Persian guftan here (that verb is from *gaub-).\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"18.11 VOICE; 18.26 WORD\",\n          \"stance\": \"supports\",\n          \"note\": \"SYN.txt l.31455 '1. Derivs. of IE *wekʷ- speak, say (18.21). Walde-P. 1.245f. ... Grk. óps (poet.); Lat. vōx ...; Skt. vāc-, Av. vāč- (nom. sg. Skt. vāk, Av. vāxš); Toch. A wak, B wek'; l.31765 'Skt. vacas-, Av. vacah- ... Lat. vocabulum (more directly fr. vocāre call)'.\"\n        },\n        {\n          \"src\": \"CHEUNG\",\n          \"where\": \"pp. 402-404 s.v. *u̯ač\",\n          \"stance\": \"supports\",\n          \"note\": \"CHEUNG.txt l.26156ff. '*uač to say, speak / AVESTAN: vaoc- (vāč-) to say || (+ *ā-) to say to || (+ *fra-) to proclaim ... PIE *uekʷ- to speak, to say > LIV: 673 f. | Pok.: 1135 ff.'\"\n        },\n        {\n          \"src\": \"ARY\",\n          \"where\": \"p. 513 (pdf 512) s.v. واژه، وات، واج\",\n          \"stance\": \"supports\",\n          \"note\": \"ARY_latin_index_pages.txt l.14955ff.: Avestan 'VAXSH, VAK, VACHAH', Pahlavi 'WAZ, VACHAK, WAZAG, VAJ', English VOICE, Latin VOX, VOCEM; references 'POKORNY 1135-1136'.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"vak, vačah, vaxš 1\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan has the verb vac- / vaoc- 'to speak' (Indo-Iranian *wak-, *wač- < PIE *wekʷ-, with the labiovelar becoming k and then č before a front vowel), the neuter s-stem vacah- 'speech, word' (= Skt. vacas-, Gk. épos < *wekʷ-os) and the root noun vāč- 'voice, word', nominative vāxš (= Skt. vāk, Lat. vōx < *wōkʷs). Nourai's 'vak' is the root and 'vaxš' is that nominative (Bartholomae writes it vāxš with a long vowel). All three forms and the glosses are correct. The words are Avestan; Old Persian has no attested form of this root.\",\n          \"derivation_fa\": \"در اوستایی فعل vac- / vaoc- «گفتن»، نام‌واژهٔ vacah- «سخن، گفتار» (برابر سنسکریت vacas- و یونانی épos) و نام‌واژهٔ vāč- «آواز، سخن» با حالت فاعلی vāxš (برابر سنسکریت vāk و لاتینی vōx) آمده است. kʷ هندواروپایی در هندوایرانی به k و پیش از واکهٔ پیشین به č بدل شده است. بارتولومه و پوکورنی و چونگ همین را می‌گویند و ادعای نورایی درست است. تنها این صورت‌ها اوستایی‌اند و در پارسی باستان گواهی ندارند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-\",\n            \"https://en.wiktionary.org/wiki/آواز\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:1135\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt l.90122 'Avestan vac- speak ... Old Indic vacas- n. = Avestan vacah (= gr. épos) discourse, word ... vāk = Avestan vāxš (= Latin vox) voice, discourse, word'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1333-1336 s.v. vāk-; col. 1340-1341 s.v. vacah-\",\n              \"stance\": \"supports\",\n              \"note\": \"BRT.txt l.22236 'vāk- (vāxš) m., f. 1) Stimme; 1) der Menschen (und Götter) Stimme ... 2) Rede, Wort ... Zum V. vak-'; l.22355 'vacah- n. 1) Sprechen, Rede, Wort ... im Gegensatz zu Denken und Handeln'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 245\",\n              \"stance\": \"supports\",\n              \"note\": \"'ai. vacas- n. = av. vacah- „Rede, Wort“ ... ai. vāc-, n. sg. vāk = av. vāxš (= lat. vox) „Stimme, Rede, Wort“'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"18.11 VOICE\",\n              \"stance\": \"supports\",\n              \"note\": \"'Skt. vāc-, Av. vāč- (nom. sg. Skt. vāk, Av. vāxš)'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 402 s.v. *u̯ač\",\n              \"stance\": \"supports\",\n              \"note\": \"'AVESTAN: vaoc- (vāč-) to say' with forms vaocat, uxδa- etc.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"vâk; vâžeh; vâžgân; vâž\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"vāž / bāž / bāj 'the murmured Zoroastrian prayer, grace' continues MP wāž [wʾc] 'word, speech; grace (before meals)' < Old Iranian *wāč- (Av. vāč-). Initial w- became b- in standard New Persian (bāž, bāj), while the variant vāž keeps the older w-. The Ferdowsi line quoted on the page uses exactly this ritual sense. vāže 'word' matches MP wāzag [wʾckʾ] 'utterance, saying' < *wāčaka-. Because of its -ž- it is classed as a word from another Middle Iranian language (Wiktionary: 'Middle Iranian'); inherited MP would give -z-. Both are confirmed. vâk 'sound' and vâžgân 'vocabulary' are not old words but 20th-century learned formations. Dehkhoda knows واک only as the name of a water bird, and Mo'in gives واژگان only in its modern sense 'list of words'. Their link to the root is etymologically sound, but they are revivals, not inherited forms.\",\n          \"derivation_fa\": \"«باژ / باج / واژ» به معنی زمزمهٔ آهستهٔ دعای زرتشتیان از فارسی میانهٔ wāž «سخن، دعای پیش از خوراک» و ایرانی باستان *wāč- (اوستایی vāč-) است. w آغازی در فارسی نو به b بدل شده («باژ»، «باج»)، ولی صورت «واژ» w کهن را نگه داشته است. «واژه» با فارسی میانهٔ wāzag «گفته» و *wāčaka- برابر است، ولی به سبب ž احتمالاً از یک گویش دیگر ایرانی میانه آمده است. بارتولومه و برهان (حاشیهٔ معین) و ویکی‌واژه این‌ها را تأیید می‌کنند. اما «واک» به معنی صدا و «واژگان» ساخته‌های نوین سدهٔ بیستم‌اند و واژهٔ کهن موروثی نیستند: دهخدا «واک» را تنها نام پرنده‌ای آبی آورده است. پس ادعای نورایی در کل با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/واژه\",\n            \"https://vajehyab.com/moein/واژه\",\n            \"https://vajehyab.com/moein/واژگان\",\n            \"https://vajehyab.com/moein/واژ\",\n            \"https://vajehyab.com/dehkhoda/واک\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:204\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v1_pages.txt leaf 423 (p. 203/204), Mo'in's note 9 on باج: 'باج و باژ و باز و واج و واژ باین معنی از ریشهٔ اوستایی vāč (گفتن)، سانسکریت vāc، در پهلوی vāž یا vāč، در لاتینی vox ... در انگلیسی voice. باژ بمعنی کلمه و سخن و گفتار است. کلیهٔ دعاهای مختصر را که زرتشتیان آهسته بزبان میرانند باژ گویند' + the Ferdowsi line 'پرستندهٔ آذر زردهشت ...'.\"\n            },\n            {\n              \"ref\": \"BQT:218\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v1_pages.txt leaf 438 (running head ۲۱۸): باز '... و بمعنی خاموشیی باشد که مغان در وقت بدن شستن و چیزی خوردن بعد از زمزمه اختیار کنند' and 'باژ - بزای فارسی، بروزن و معنی باج' -- the ritual murmur sense.\"\n            },\n            {\n              \"ref\": \"BQT:2260\",\n              \"status\": \"partial\",\n              \"note\": \"BQT vol. 4 pdf 343 (p. 2260) is the وخشور page: Mo'in derives vaxš from the root vak 'گفتن'. Relevant to the root but not to vâk/vâže themselves.\"\n            },\n            {\n              \"ref\": \"FSF:64\",\n              \"status\": \"not_found\",\n              \"note\": \"FSF_pages.txt: the scan's printed p. 64 (leaf 67) is اوباردن/انوشه; Noushin's باژ entry (leaf 81, p. 78) treats only باژ 'tribute', a different word. Pagination of Nourai's edition is evidently different.\"\n            },\n            {\n              \"ref\": \"ZMA:28\",\n              \"status\": \"not_checked\",\n              \"note\": \"Jonaydi, Zendegi va Mohajerat-e Aryaian: no digital copy (refs_online.json).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1336 s.v. vāk-\",\n              \"stance\": \"supports\",\n              \"note\": \"BRT.txt l.22273 'mp. vāž leises Gebet, vāž u mārīkān Sätze und Wörter ..., vāžak ...; np. āvāz Stimme, āvā i kōs Trommelgetön, guvāža Schelten'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"s.v. wāž, wāzag\",\n              \"stance\": \"supports\",\n              \"note\": \"PHD_mackenzie.txt l.5289 'wāž [wʾc | = M, (N bāj)] word, speech; grace (before meals)'; PHD.txt l.649 'wāzag [wʾckʾ] utterance, saying'.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"§ 55, p. 127\",\n              \"stance\": \"supports\",\n              \"note\": \"HUB.txt l.5795 'vāž Gemurmel, das leise Recitiren religiöser Formeln der Perser (Nöldeke, Tab. 353) = phl. vāc ... daneben bāj bei Vullers'.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"no. 1072, p. 240\",\n              \"stance\": \"supports\",\n              \"note\": \"HRN.txt l.9285 '1072. vāj sprich, vergl. vāž Wort, Rede (dialektisch), guvāže Schmähung ... aw. vac- ... phlv. vāčak Stimme, vāč (pāz. vāž) Gebet'.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Glossary p. 207 s.v. 1vaxš\",\n              \"stance\": \"silent\",\n              \"note\": \"Nyberg has no separate wāž/wāzag lemma in the OCR; only vaxš 'word, message' (Av. vaxša-).\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"vajehyab s.v. واژه, واژگان, واژ\",\n              \"stance\": \"partial\",\n              \"note\": \"واژه '(ژِ) [په.] لغت، کلمه' (Pahlavi tag); واژگان 'فهرستی از مجموعهٔ واژه‌های یک کتاب ... یا یک زبان' (modern sense, no origin tag); واژ 'نک. باژ؛ باج'.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"p. 513 s.v. واژه، وات، واج\",\n              \"stance\": \"supports\",\n              \"note\": \"Aryanpur files واژه under PIE wekʷ- (Pokorny 1135-1136), Pahlavi 'WAZ, VACHAK, WAZAG, VAJ'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"â-vač; fra-vaxš; paurvatâ-vac; vi-vačah\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two of the four forms are attested. Avestan ā + vac- 'to say to, call to' (Cheung: '(+ *ā-) to say to'; Horn: 'aw. ai. ā + √vac-') is the source of āvāz. fra-vaxš- appears in Avestan as the future stem of fra-vac- 'to proclaim' (YAv. fra-vaxšyeite, Vr 15.3; Cheung). The other two are Nourai's own constructs. Avestan has paurvatā- 'mountain range' (Buck 1.22), but no compound 'paurvatā-vāč-' 'mountain voice' is attested in Bartholomae. 'vi-vačah' 'speak out ironically' is likewise unattested; it is a reconstruction (*vi-vāčaka-) set up to explain NP guvāže. The labels 'Old Persian' and the glosses 'echo', 'ironically' belong to these reconstructions.\",\n          \"derivation_fa\": \"از چهار صورت این خانه دو صورت در اوستا گواهی دارد. یکی ā + vac- «به کسی گفتن، خواندن» است که «آواز» از آن آمده (چونگ، هرن). دیگری fra-vaxš- است که ستاک آیندهٔ فعل fra-vac- «اعلام کردن» است (frauuaxšiieite در ویسپرد ۱۵.۳). اما «paurvatâ-vac» به معنی «آواز کوه، پژواک» و «vi-vačah» ساختهٔ خود نورایی‌اند. اوستایی واژهٔ pauruuatā- «رشته‌کوه» را دارد، ولی چنین ترکیبی نه در بارتولومه آمده و نه در متن‌ها. vi-vačah هم بازسازی‌ای است برای توضیح «گواژه». پس این خانه با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/آواز\",\n            \"https://en.wiktionary.org/wiki/فروختن\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:1135\",\n              \"status\": \"partial\",\n              \"note\": \"POK 1135 gives Av. vac-, vacah-, vāxš but none of the compounds with ā-, fra-, paurvatā-, vi-.\"\n            },\n            {\n              \"ref\": \"KLN:1719\",\n              \"status\": \"partial\",\n              \"note\": \"KLN_1966.txt stops in 'va-' (902 leaves), so p. 1719 cannot be opened; the same entry in KLN_1971.txt l.263481 s.v. voice: 'fr. I.-E. base *weqʷ-, *woqʷ-, voice; to speak, whence also OI. vacas-, sound, word, Avestic vacah-, of s.m., OI. vakti, vivakti' -- supports the root, not the Avestan compounds.\"\n            },\n            {\n              \"ref\": \"SYN:26\",\n              \"status\": \"partial\",\n              \"note\": \"SYN.txt leaf 50 = p. 26 (1.22 MOUNTAIN), l.1016: 'Skt. parvata- mountain, mountain range, rock, Av. paurvata- mountain range' -- confirms the first element only, no 'voice' compound.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 402-403 s.v. *u̯ač\",\n              \"stance\": \"supports\",\n              \"note\": \"'AVESTAN: vaoc- (vāč-) to say || (+ *ā-) to say to || (+ *fra-) to proclaim ... Fut.: ... med. 3sg. YAv. frauuaxšiieite (Vr 15.3)'.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1333-1341 (vāk-, vacah-); grep for paurvatā-vāk-, vīvāč-\",\n              \"stance\": \"partial\",\n              \"note\": \"vāk-, vacah- present; no compound *paurvatā.vāk- or *vi.vacah- found (grep 'vīvāč|vi.vā[cč]' empty; paurvatā- occurs only as the mountain word).\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"no. 54, p. 13\",\n              \"stance\": \"supports\",\n              \"note\": \"HRN.txt l.915 '54. āvāz Stimme, āvāze, āvāzīden. aw. ai. ā + √vac-, s. np. vāj (No. 1072); phlv. āvāj bzw. āvāč Stimme, arm. LW. avaj'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"1.22 MOUNTAIN (p. 26)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Av. paurvata- mountain range' -- no compound with vāč-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"âvâ; forŭxtan; pažvâk; govâžeh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"āvāz / āvā 'voice, song': MP āwāz, āwāč [ʾpʾc] < *ā-wāča-, built on *wāč- 'voice'. Final -z is the regular MP outcome of postvocalic č; āvā is the shortened form. Confirmed. govāže / guvāžīdan 'taunt, mockery' (Ferdowsi): Bartholomae and Horn list NP guvāža 'Schelten' among the derivatives of vāč-. It is best taken as *vi-wāčaka-, with vi- > gu- as in gumān < *vi-mān-. The ž again points to a non-southwestern form. Plausible. forūxtan / forūš- 'to sell' < MP frōxtan, frōš-: Justi, Horn and Mo'in derive it from *fra-waxš- 'to call out, offer for sale', an s-extension of vac-. Cheung (under *u̯axš) and Wiktionary instead put it first under *waxš- 'to grow' (> 'prosper' > 'trade, sell') and give the 'cry out' theory as the alternative, so this word is plausible but disputed. pažvāk 'echo' is a real New Persian word (Dehkhoda, Mo'in; BQT p. ~401 defines it). Its second part may be *-wāka- 'sound', but the first element paž- is unexplained. Nourai's Avestan paurvatā- 'mountain' cannot give paž- phonetically (it would give MP *parwad-), so that route is unsupported.\",\n          \"derivation_fa\": \"«آواز / آوا» از فارسی میانهٔ āwāz / āwāč و ایرانی باستان *ā-wāča- است و درست است. č پس از واکه در فارسی میانه به z بدل شده و «آوا» صورت کوتاه‌شدهٔ آن است. «گواژه، گواژیدن» به معنی طعنه و سرزنش را بارتولومه و هرن زیر vāč- آورده‌اند. احتمالاً از *vi-wāčaka- است، با دگرگونی vi- به gu- چنان‌که در «گمان». «فروختن» را یوستی و هرن و معین از *fra-waxš- «بانگ زدن، به فروش عرضه کردن» می‌دانند، ولی چونگ و ویکی‌واژه آن را بیشتر از *waxš- «بالیدن» می‌گیرند. پس این پیوند مورد اختلاف است. «پژواک» واژه‌ای واقعی است و جزء دوم آن شاید *-wāka- «آواز» باشد. اما جزء نخست روشن نیست و pauruuatā- «کوه» از نظر آوایی نمی‌تواند «پژ» شود. در مجموع این خانه با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/آواز\",\n            \"https://en.wiktionary.org/wiki/فروختن\",\n            \"https://vajehyab.com/moein/آوا\",\n            \"https://vajehyab.com/moein/گواژه\",\n            \"https://vajehyab.com/moein/پژواک\",\n            \"https://vajehyab.com/dehkhoda/پژواک\",\n            \"https://vajehyab.com/moein/فروختن\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1473\",\n              \"status\": \"supports\",\n              \"note\": \"BQT vol. 3 pdf 266 (p. 1473) s.v. فروختن: 'اوستا fra-vaxš- (توسعهٔ vač- ...) (صدا کردن، بمعرض فروش گذاشتن)؛ پهلوی frōxtan «اسشق»، هوبشمان ۸۲۶ ... کردی ...' -- exactly Nourai's arrow.\"\n            },\n            {\n              \"ref\": \"BQT:401\",\n              \"status\": \"partial\",\n              \"note\": \"BQT_v1_pages.txt leaves 624-625 (p. ~401): the پژواک entry defines it as 'چون در کوه و گنبد بآواز بلند چیزی بگویند در جواب همانرا شنوند، وآنرا بعربی صدا خوانند'; the headword line and any etymological note are illegible in the OCR.\"\n            },\n            {\n              \"ref\": \"BQT:2260\",\n              \"status\": \"partial\",\n              \"note\": \"BQT vol. 4 pdf 343 = وخشور page (root vak 'گفتن'); not about the node 4 words.\"\n            },\n            {\n              \"ref\": \"HRN:263\",\n              \"status\": \"not_found\",\n              \"note\": \"HRN.txt leaf 284 (p. 263) is the start of 'Verlorenes Sprachgut' (a-, afd ...), none of the node 4 words; Horn treats āvāz at no. 54, furōxtan at p. 183 and guvāže at no. 1072.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"no. 54 (p. 13); p. 183 s.v. furōxten; no. 1072 (p. 240)\",\n              \"stance\": \"supports\",\n              \"note\": \"l.915 'āvāz Stimme ... aw. ai. ā + √vac-'; l.7171 'furōxten, firōxten verkaufen, Praes. furōš-em ... aw. *fra + √vaxš- (Erweiterung von vac- wie haxš- von hac-) ausrufen, ausbieten; phlv. frōxtan ... Die Etymologie stammt von Justi'; l.9286 'guvāže Schmähung, guvāžīden schelten'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 403 (*u̯ač) and p. 427 (*u̯axš)\",\n              \"stance\": \"partial\",\n              \"note\": \"*u̯ač: 'BMP ʾpʾc /āwāz/ sound, voice, language ... NP āvāzah voice, sound'; *u̯axš 'to grow': '(+ *fra-) ? MMP frwxš- to sell ... Several semantic shifts need to be assumed ... to grow > to prosper > to prosper through trade > to sell' -- Cheung prefers 'grow' for forūxtan, against Nourai.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"s.v. āwāz, frōxtan\",\n              \"stance\": \"supports\",\n              \"note\": \"PHD.txt l.4239 'voice āwāz, wāng'; PHD_mackenzie.txt l.2404 'frōxtan, frō(x)š- [MZBNW-tn' ... M prwxt-, N ...] sell'.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1336\",\n              \"stance\": \"supports\",\n              \"note\": \"'np. āvāz Stimme, āvā i kōs Trommelgetön, guvāža Schelten' listed under vāk-.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"no. 826 (cited by Mo'in)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for furōxtan/pažvāk in HUB.txt found nothing usable in the OCR.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"vajehyab s.v. آوا, گواژه, پژواک, فروختن\",\n              \"stance\": \"partial\",\n              \"note\": \"آوا 'آواز، بانگ'; گواژه '1- طعنه، سرزنش 2- شوخی'; پژواک 'بازتاب صدا در کوه، طنین'; no etymologies online.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"p. 73 (pdf 72) s.v. آواز\",\n              \"stance\": \"supports\",\n              \"note\": \"ARY_latin_index_pages.txt pdf 72: Avestan 'UXTA, VAC, A-VAXSH', Pahlavi 'AWAZ, AVAC', Latin 'VOX, VOCARE', Pokorny reference.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Avestan\",\n          \"words\": \"vaxš-ô-bara\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"No Avestan *vaxšō.bara- is attested. It is a reconstruction (Lagarde, quoted by Horn; Mo'in) to explain MP waxšwar 'prophet': Av. vaxša- n. 'word, command' (Vd 19.15 vaxšəm mōi asąsat; Bartholomae col. 1339) + -bara- 'bearing' (PIE *bʰer-). Intervocalic -b- > -w- in Middle Persian (as in -war 'bearing' in ganjwar, ranjwar), giving waxšwar. The reconstruction is reasonable, but the form should be starred, not presented as attested Avestan.\",\n          \"derivation_fa\": \"ترکیب اوستایی «vaxš-ô-bara» در متن‌ها نیامده و بازسازی است (لاگارد به نقل هرن، و معین). جزء نخست آن vaxša- «سخن، فرمان» در وندیداد ۱۹.۱۵ گواهی دارد (بارتولومه، ستون ۱۳۳۹) و جزء دوم -bara- «برنده» از ریشهٔ bar- است. b میان دو واکه در فارسی میانه به w بدل شده و waxšwar «پیامبر» پدید آمده است (همانند پسوند -ور در «گنجور» و «رنجور»). این بازسازی پذیرفتنی است، ولی باید با ستاره آورده شود.\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/وخشور\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:241\",\n              \"status\": \"supports\",\n              \"note\": \"HRN.txt leaf 262 (p. 241) no. 1076 'vaxšūr, vuxšūr Prophet. phlv. vaxšvar (Dēnkart); de Lagarde, Ges. Abh. 164 nimmt als Grundform aw. *vaxšahara- [= *vaxša-bara-] an (vergl. vaxšəm mōi asąsat vd. 19, 15)' -- reconstruction marked with *.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1339 s.v. 1vaxša-\",\n              \"stance\": \"partial\",\n              \"note\": \"BRT.txt l.22331 'vaxša- n. Wort, Geheiss: vaxšəm mōi asąsat V. 19.15' -- the first member is attested, the compound is not.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Glossary p. 207\",\n              \"stance\": \"supports\",\n              \"note\": \"NYB_vol2_glossary.txt l.4049 '1vaxš [whš] word, message 44. — Av. (1339) vaxša-'; l.4056 'vaxš-var [whšwr] prophet. — Bearer of the Word, or the (divine) message, v. 1vaxš'.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"§ 55, p. 127\",\n              \"stance\": \"supports\",\n              \"note\": \"HUB.txt l.5797 'vaxšūr Prophet = pāz. vaxšur Shk. 270, zd. *vaxšabara-'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"vaxš-war\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Book Pahlavi waxšwar [whšwr] 'prophet' (MacKenzie), with waxšwarīh 'prophethood'. Nyberg explains it as 'bearer of the Word, of the divine message', from vaxš 'word' (Av. vaxša-) + -war < *-bara-. In Dēnkard VII the word is used of Zoroaster and of earlier messengers of Ohrmazd. Nourai's gloss 'messenger' is a fair literal rendering.\",\n          \"derivation_fa\": \"پهلوی waxšwar «پیامبر» (مکنزی)، با اسم معنای waxšwarīh «پیامبری». نیبرگ آن را «حامل کلام، پیام ایزدی» معنا کرده است: از vaxš «سخن» (اوستایی vaxša-) و پسوند -war از *-bara- «برنده». در دینکرد هفتم این واژه برای زرتشت و پیام‌آوران پیشین اورمزد به کار رفته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/وخشور\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:4992\",\n              \"status\": \"partial\",\n              \"note\": \"Mo'in's 6-vol. dictionary is not online; vajehyab's Mo'in s.v. وخشور gives only '(وَ یا وُ) (اِ. ص.) پیغمبر، رسول' without the Pahlavi form. Mo'in's own Pahlavi note is in BQT:2260 (see node 7).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"s.v. waxšwar\",\n              \"stance\": \"supports\",\n              \"note\": \"PHD_mackenzie.txt l.5273 'waxšwar [whšwr | N waxšur] prophet. ~īh: prophethood'.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Glossary p. 207\",\n              \"stance\": \"supports\",\n              \"note\": \"'vaxš-var [whšwr] prophet 111. — Bearer of the Word, or the (divine) message, v. 1vaxš'; 'vaxšvarīh prophethood'.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"no. 1076, p. 241\",\n              \"stance\": \"supports\",\n              \"note\": \"'phlv. vaxšvar (Dēnkart)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"vaxšŭr\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP vaxšūr / vuxšūr 'prophet' (Ferdowsi; much used in the Dasātīr literature) < MP waxšwar. The cluster -šw- > -šū- (w vocalised to ū after a consonant) and the a ~ u variation in the first syllable come from assimilation to the following labial (Hübschmann § 54b: vaxšūr = vuxšūr). Applied above all to Zoroaster, hence Nourai's gloss.\",\n          \"derivation_fa\": \"«وخشور» (وَخشور / وُخشور) به معنی «پیامبر» از پهلوی waxšwar است و در شاهنامه و بیشتر در ادبیات دساتیری به کار رفته است. خوشهٔ -šw- به -šū- بدل شده است، یعنی w پس از همخوان به واکهٔ ū تبدیل شده. دوگونگی وَ/وُ در هجای نخست از همگونی با واکهٔ لبی پسین است (هوبشمان). معین در حاشیهٔ برهان آن را «حامل کلام آسمانی» معنا کرده و هرن و مکنزی هم همین را آورده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/وخشور\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:2260\",\n              \"status\": \"supports\",\n              \"note\": \"BQT vol. 4 pdf 343 (p. 2260), Mo'in's note 2 on وخشور 'پیغمبر و رسول را گویند': 'در اوستا vaxša-bara- مرکب از «وخش» از ریشهٔ vak (گفتن) و «بره» از ریشهٔ bar (بردن) که در فارسی بدل به «ور» شده ... پس وخشور ... لغةً بمعنی حامل کلام (سخن) آسمانی و اصطلاحاً بمعنی پیامبر است. «مزدیسنا ص ۱۰۷-۱۰۹»؛ پهلوی vaxšvar (دینکرت)'.\"\n            },\n            {\n              \"ref\": \"HRN:241\",\n              \"status\": \"supports\",\n              \"note\": \"HRN no. 1076 'vaxšūr, vuxšūr Prophet. phlv. vaxšvar'.\"\n            },\n            {\n              \"ref\": \"MON:4992\",\n              \"status\": \"partial\",\n              \"note\": \"vajehyab Mo'in: 'وخشور (وَ یا وُ) (اِ. ص.) پیغمبر، رسول' -- meaning confirmed, print page not accessible.\"\n            },\n            {\n              \"ref\": \"VSF:17\",\n              \"status\": \"not_checked\",\n              \"note\": \"Mehravand, Vazhe-sazi dar Zaban-e Farsi: no digital copy (refs_online.json).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HUB\",\n              \"where\": \"§ 54b, p. 127; § 55\",\n              \"stance\": \"supports\",\n              \"note\": \"HUB.txt l.4420 'vaxšūr = vuxšūr Prophet = phl. vaxšvar u. s. w.'; l.5797 'vaxšūr Prophet = pāz. vaxšur Shk. 270, zd. *vaxšabara-'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"s.v. waxšwar\",\n              \"stance\": \"supports\",\n              \"note\": \"'waxšwar [whšwr | N waxšur] prophet'.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"vajehyab s.v. وخشور\",\n              \"stance\": \"supports\",\n              \"note\": \"'(وَ یا وُ) (اِ. ص.) پیغمبر، رسول'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Avestan\",\n          \"words\": \"ni-vak; hu-ni-vak\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Neither form is attested in Avestan; both are reconstructions. *ni-wāka- / *ni-wāč- (prefix ni- 'down' + wāč- 'voice') is well grounded in Middle Iranian: Parthian nwʾc- 'to speak kindly to, honour', nwʾg 'melody'; Manichaean MP nwʾg 'melody, tune'; NP navāxtan/navāz- (Cheung, under *u̯ač with *ni-). It is therefore a sound reconstruction behind navā. *hu-ni-wāka- 'good sound' is Nourai's (and Mo'in's) construct to explain xonyā. Since the Middle Persian word is hunīyāg without any -w- (see node 9), this compound is not supported.\",\n          \"derivation_fa\": \"هیچ‌یک از این دو صورت در اوستا نیامده و هر دو بازسازی‌اند. *ni-wāka- / *ni-wāč- (پیشوند ni- و wāč- «آواز») در ایرانی میانه پشتوانهٔ استوار دارد: پارتی nwʾc- «نواختن، گرامی داشتن» و nwʾg «نوا»، فارسی میانهٔ مانوی nwʾg «آهنگ»، و فارسی نو «نواختن / نواز-» (چونگ). پس برای «نوا» بازسازی درستی است. اما *hu-ni-wāka- «خوش‌نوا» را نورایی و معین برای توضیح «خنیا» ساخته‌اند. چون صورت فارسی میانه hunīyāg است و w ندارد، این ترکیب پشتوانه‌ای ندارد. پس خانه تنها در بخش نخست پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/نوا\",\n            \"https://en.wiktionary.org/wiki/خنیا\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:2174\",\n              \"status\": \"partial\",\n              \"note\": \"BQT vol. 4 pdf 257 (p. 2174) s.v. نوا: Mo'in's note 4 'پهلوی navāk [hu-navāk خوش نوا] «اونوالا»؛ قس: ارمنی nvag (آهنگ، نغمه، سرود)، hnvagel (من مینوازم) «هوبشمان ۱۶۸»' -- gives the Pahlavi and Armenian forms, no Avestan *ni-vāk.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 403 s.v. *u̯ač\",\n              \"stance\": \"supports\",\n              \"note\": \"'(+ *ni-) MMP nwʾcišn kind utterance; honouring ..., MMP nwʾg melody, tune ... PARTHIAN ... (+ *ni-) nwʾc- to speak kindly to, treat kindly, honour, nwʾg melody ... NP navāxtan/navāz- to caress ... to play (an instrument)'.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1333-1336 (vāk-)\",\n              \"stance\": \"silent\",\n              \"note\": \"no Avestan *nivāk- / *hunivāk- listed.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"s.v. huniyāg\",\n              \"stance\": \"contradicts\",\n              \"note\": \"PHD_mackenzie.txt l.2960 'huniyāg [hwnydʾk, N xunyā] delightful'; l.2963 'huniyāgar [hwnydʾkl, N xunyāgar] entertainer, musician' -- no -w- that *hu-ni-wāka- would need.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"navâ; xonyâ\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"navā 'melody, tune' < MP nawāg / niwāg (Manichaean MP and Parthian nwʾg 'melody'; Armenian loan nuag) < *ni-wāka-. Cognate with navāxtan / navāz- 'to play (music); caress', nawāziš etc. (the extra forms on the page). Confirmed. xonyā 'song, music' (xonyāgar 'minstrel') < MP huniyāg [hwnydʾk] 'delightful', huniyāgar 'entertainer, musician'. Mo'in (BQT note on خنیا) analyses it as hu- 'good' + navā. But the Middle Persian form shows no w: *hu-ni-wāka- would have given MP *hunwāg, NP *xunvā. Wiktionary instead derives it from Proto-Iranian *xwan-iyā-ka-, from the root of xwāndan 'to sing, recite' (PIE *swenh₂- 'to sound'). The link of xonyā to *wekʷ- is therefore disputed; navā is fine.\",\n          \"derivation_fa\": \"«نوا» از فارسی میانهٔ nawāg / niwāg است (فارسی میانهٔ مانوی و پارتی nwʾg «آهنگ»، و وام‌واژهٔ ارمنی nuag) و به *ni-wāka- برمی‌گردد. «نواختن، نواز-، نوازش» که در نمودار آمده هم‌ریشهٔ آن‌اند. این بخش درست است. «خنیا» (و «خنیاگر») از فارسی میانهٔ huniyāg «خوشایند» و huniyāgar «رامشگر» است. معین در حاشیهٔ برهان آن را «هو + نوا = خوش‌نوا» دانسته و نورایی از او پیروی کرده است. ولی در صورت پهلوی w نیست: از *hu-ni-wāka- باید *hunwāg و «خُنوا» پدید می‌آمد. ویکی‌واژه آن را از ایرانی آغازین *xwan-iyā-ka- می‌داند، یعنی از همان ریشهٔ «خواندن» (هندواروپایی *swenh₂- «صدا دادن»). پس پیوند «خنیا» با این ریشه را پژوهش امروزی نمی‌پذیرد، اما «نوا» درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/نوا\",\n            \"https://en.wiktionary.org/wiki/خنیا\",\n            \"https://en.wiktionary.org/wiki/خنیاگر\",\n            \"https://vajehyab.com/moein/نوا\",\n            \"https://vajehyab.com/moein/خنیا\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:2174\",\n              \"status\": \"supports\",\n              \"note\": \"BQT vol. 4 pdf 257 (p. 2174) نوا 'هر نغمه و آهنگ و آواز و ناله را گویند'; note 4 'پهلوی navāk ... ارمنی nvag (آهنگ، نغمه، سرود)، hnvagel (من مینوازم) «هوبشمان ۱۶۸»' -- supports navā; xonyā not on this page.\"\n            },\n            {\n              \"ref\": \"BQT:2178\",\n              \"status\": \"supports\",\n              \"note\": \"BQT vol. 4 pdf 261 (p. 2178) نواختن: 'از: نواخ (نواز) + تن (پسوند مصدری). نواختن اصلاً بمعنی نوازش کردن، دست کشیدن، زدن؛ و نیز بمعنی زدن یکی از آلات موسیقی ... رک: نوا «هوبشمان»' -- links navāxtan with navā (the extra script forms).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 403 s.v. *u̯ač\",\n              \"stance\": \"supports\",\n              \"note\": \"'MMP nwʾg melody, tune ... Parthian nwʾg melody ... NP navāxtan/navāz-' -- for navā only; xonyā is not listed under *u̯ač.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"s.v. huniyāg, huniyāgar\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'huniyāg [hwnydʾk, N xunyā] delightful'; 'huniyāgar [hwnydʾkl, N xunyāgar] entertainer, musician' -- no -w-, against *hu-ni-wāka-.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 2, BQT_v2_pages.txt leaf 235 s.v. خنیا\",\n              \"stance\": \"supports\",\n              \"note\": \"Mo'in's note: 'پهلوی ... «اونوالا ۵۰۲» [از: هو (نیک) + نوا = خوش نوا] (خوش آهنگ، موسیقی)' -- Mo'in is Nourai's source for the hu + navā analysis.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"vajehyab s.v. نوا, خنیا\",\n              \"stance\": \"partial\",\n              \"note\": \"نوا '(نَ) [په.] 1- نغمه، سرود ...'; خنیا '(خُ) (اِ.) سرود، نغمه، آواز' (no origin tag).\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Old Persian\",\n          \"words\": \"wâk; wânk\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Neither 'wâk' nor 'wânk' is attested in the Old Persian inscriptions; Kent's lexicon has no such entries. They are Nourai's (after Abolghasemi) reconstructions of the Old Iranian *wāk-/*wāč- 'voice' and a nasalised *wānka- behind MP wāng. Cheung lists NP bāng, Kurdish bang, Zazaki veng, Sivandi vang 'scream' and Balochi gwank 'voice' under *u̯ač, and Wiktionary derives MP wāng 'probably' from PIE *wṓkʷs. The nasal is unexplained (perhaps expressive). The derivation is acceptable as a reconstruction, but the 'Old Persian' label is not.\",\n          \"derivation_fa\": \"صورت‌های «wâk» و «wânk» در سنگ‌نبشته‌های پارسی باستان نیامده‌اند و در واژه‌نامهٔ کنت هم نیستند. این‌ها بازسازی‌های نورایی (به پیروی از ابوالقاسمی) از ایرانی باستان *wāk-/*wāč- «آواز» و صورت خیشومی‌شدهٔ *wānka- هستند که پهلوی wāng از آن آمده است. چونگ «بانگ» فارسی، bang کردی، veng زازاکی، vang سیوندی «جیغ» و gwank بلوچی را زیر *u̯ač آورده است. ویکی‌واژه هم پهلوی wāng را «احتمالاً» از *wṓkʷs می‌داند. خیشومی‌شدن آن روشن نیست. بازسازی پذیرفتنی است، ولی برچسب «پارسی باستان» نادرست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/بانگ\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"ETM:61\",\n              \"status\": \"not_checked\",\n              \"note\": \"Abolghasemi, Risheh-shenasi (Etimoloji): no digital copy (refs_online.json).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KNT\",\n              \"where\": \"lexicon (KNT_full.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"no Old Persian entry wāk-/wānk-/vāč- in Kent's lexicon (OP attests no form of the root vac-).\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 404 s.v. *u̯ač\",\n              \"stance\": \"supports\",\n              \"note\": \"'NP bang, Kurd. bang (m.), Zaz. veng (m.) voice, Siv. vang scream, Bal. gwank voice (LW?)' listed among the reflexes of *u̯ač.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1336\",\n              \"stance\": \"partial\",\n              \"note\": \"the Pahlavi gloss of Av. vāk- in Y. 31 etc. is 'vāng' ('Pü. gōwišn ... : vāng') -- the MP word glosses the Avestan one, no OP form.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"vang\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Book Pahlavi wāng [wʾng; ideogram KʾLʾ < Aramaic qāl 'voice'] 'voice, cry, shout', Manichaean MP wng, also in borz-wāng 'loud'. Nyberg: 'vāng voice, sound, shout, cry ... MPrs wng; NP bāng'. Nourai writes it with a short a ('vang'), but the word is wāng; the meanings are right.\",\n          \"derivation_fa\": \"پهلوی wāng (با هزوارش KʾLʾ از آرامی qāl «آواز») به معنی «آواز، فریاد، بانگ» است و در ترکیب borz-wāng «بلندآواز» هم آمده. فارسی میانهٔ مانوی آن را wng نوشته است. نیبرگ و مکنزی هر دو آن را نیای «بانگ» فارسی می‌دانند. نورایی آن را با a کوتاه نوشته (vang)، ولی صورت درست wāng است. معنا درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/بانگ\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:229\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v1_pages.txt leaf 449 (p. 229) بانگ 'و بمعنی فریاد و آواز بلند هم هست'; Mo'in's note: 'پهلوی vāng «بندهشن ...»، طبری vāng (صدا)، گیلکی vāng (گریهٔ توأم با ناله)'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"s.v. wāng\",\n              \"stance\": \"supports\",\n              \"note\": \"PHD_mackenzie.txt l.5168 'wāng [KʾLʾ < A qlʾ; wʾng | = M, N bāng] voice, cry'; l.1586 'borz-wāng loud'.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Glossary s.v. vāng\",\n              \"stance\": \"supports\",\n              \"note\": \"NYB_vol2_glossary.txt l.3933 'vāng [wʾng, Ps. wʾngy; KʾLʾ] voice, sound, shout, cry: ~ kartan to give a shout ... — MPrs wng; NP bāng'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Persian\",\n          \"words\": \"vang 2; bâng\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"bāng 'loud call, cry' < MP wāng with the regular New Persian change of initial w- > b- (as in bād < wād, bahār < wahār). Confirmed by MacKenzie, Nyberg, Mo'in and Wiktionary. vang 'crying (of a baby)' is colloquial (Mo'in marks it عا.). It may be a dialectal form that kept initial v- (Cheung: Sivandi vang 'scream', Zazaki veng 'voice'; Mo'in quotes Tabari vāng 'sound', Gilaki vāng 'crying with moaning'), but it could equally be an onomatopoeia for a baby's wail. Its link to wāng is plausible, not certain.\",\n          \"derivation_fa\": \"«بانگ» از پهلوی wāng است، با دگرگونی قاعده‌مند w آغازی به b در فارسی نو (چنان‌که «باد» از wād و «بهار» از wahār). مکنزی، نیبرگ، معین و ویکی‌واژه این را تأیید می‌کنند. «ونگ» به معنی گریهٔ بچه واژه‌ای عامیانه است (معین: «عا.»). شاید صورت گویشی‌ای باشد که v آغازی را نگه داشته (طبری vāng «صدا»، گیلکی vāng «گریه با ناله»، سیوندی vang «جیغ»). ولی ممکن است تنها نام‌آوا برای گریهٔ نوزاد باشد. پس این بخش با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/بانگ\",\n            \"https://vajehyab.com/moein/بانگ\",\n            \"https://vajehyab.com/moein/ونگ\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:229\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v1_pages.txt leaf 449 (p. 229): بانگ 'فریاد و آواز بلند'; Mo'in: 'پهلوی vāng ... طبری vāng (صدا)، گیلکی vāng (گریهٔ توأم با ناله)'.\"\n            },\n            {\n              \"ref\": \"ETM:72\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai cites ETM:61 here; Abolghasemi's book has no digital copy.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"s.v. wāng\",\n              \"stance\": \"supports\",\n              \"note\": \"'wāng ... N bāng voice, cry'.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Glossary s.v. vāng\",\n              \"stance\": \"supports\",\n              \"note\": \"'MPrs wng; NP bāng'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 404\",\n              \"stance\": \"supports\",\n              \"note\": \"'NP bang, Kurd. bang, Zaz. veng voice, Siv. vang scream'.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"grep bāng\",\n              \"stance\": \"silent\",\n              \"note\": \"no entry for bāng found in HRN.txt OCR.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"vajehyab s.v. بانگ, ونگ\",\n              \"stance\": \"partial\",\n              \"note\": \"بانگ '(اِ.) آواز بلند، فریاد'; ونگ '(وَ) (اِ.) (عا.) صدای گریهٔ بچه' -- no origin tags.\"\n            }\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"ux; hu-ux-tay\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan uxδa- n. 'word, utterance' (< Indo-Iranian *uktʰa-, zero grade *ukʷ- + -tʰa-; Skt. ukthá-) and the past participle uxta- 'spoken' (Skt. uktá- < PIE *ukʷ-tó-). With hu- 'good' (Skt. su-) this gives hūxta- 'good word', one of the triad humata- hūxta- hvaršta- 'good thought, good word, good deed'. Nourai's 'hu-ux-tay' is this compound (Avestan also has an i-stem abstract in -ti-). The words are Avestan, not Old Persian.\",\n          \"derivation_fa\": \"اوستایی uxδa- «سخن، گفته» (برابر سنسکریت ukthá-) و صفت مفعولی uxta- «گفته‌شده» (برابر سنسکریت uktá-) از درجهٔ صفر ریشه، یعنی *ukʷ-، ساخته شده‌اند. با پیشوند hu- «نیک» ترکیب hūxta- «گفتار نیک» پدید آمده که جزء دوم سه‌گانهٔ humata- hūxta- hvaršta- «اندیشه، گفتار و کردار نیک» است. hu-ux-tay در نمودار همین ترکیب است. ادعای نورایی درست است، جز اینکه این صورت‌ها اوستایی‌اند و پارسی باستان نیستند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"ETM:72\",\n              \"status\": \"not_checked\",\n              \"note\": \"Abolghasemi, Risheh-shenasi: no digital copy (refs_online.json).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1336-1337 s.v. vāk-, vacah-\",\n              \"stance\": \"supports\",\n              \"note\": \"BRT.txt l.20648 'yezi humatəm mainyāt hūxtəm vā mrvāt hvarštəm vā vərəzyāt' and l.22270 'humatōibyasca hūxtōibyasca ... (Y. 11.17)'; vaxδa- 'Sprechen, Rede' PFP. zum V. vak-.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Glossary s.v. duš-hūxt, huvaršt\",\n              \"stance\": \"supports\",\n              \"note\": \"NYB_vol2_glossary.txt l.1394 'duš-hūxt [dwšhwht'] evil speech ... — The negative of hūxt. Av. duž-ūxta-'; l.2089 'cf humat and hūxt'.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 1135\",\n              \"stance\": \"supports\",\n              \"note\": \"'Avestan vac- speak, uxta-' (participle).\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"p. 402\",\n              \"stance\": \"supports\",\n              \"note\": \"'perf. pass. uxδa- (Y 32.9, Y 33.14 ...)' under *u̯ač (with a note that uxδa- could also belong to *Hauj).\"\n            }\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Persian\",\n          \"words\": \"hŭxt\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Pahlavi hūxt [hwxt] 'good speech' < Av. hūxta- is certain, and Mo'in (BQT note on هوخت) gives exactly 'هوخت در پهلوی hūxt (گفتار نیک) از اوستا hūxta'. In New Persian, however, هوخت / هوخ appears only as a dictionary word: Borhan and Dehkhoda define it as 'Bayt al-Maqdis' (Jerusalem, 'the old qibla'). The sense 'good words' is a learned borrowing from Zoroastrian Pahlavi, not a living inherited word. Nourai's 'prayer, prayer house' mixes the two. The etymology of the 'good word' sense is right; the New Persian status and the 'prayer house' meaning are doubtful.\",\n          \"derivation_fa\": \"پهلوی hūxt «گفتار نیک» از اوستایی hūxta- قطعی است. معین در حاشیهٔ برهان هم همین را آورده: «هوخت در پهلوی hūxt (گفتار نیک) از اوستا hūxta». اما در فارسی نو «هوخت / هوخ» تنها در فرهنگ‌ها آمده و برهان و دهخدا آن را «بیت‌المقدس» (قبلهٔ پیشین) معنا کرده‌اند. معنای «گفتار نیک» وام‌گیری فاضلانه از پهلوی زرتشتی است و واژهٔ زندهٔ موروثی نیست. نورایی دو معنا را درآمیخته است («دعا، پرستشگاه»). ریشه‌شناسی معنای «گفتار نیک» درست است، ولی جایگاه واژه در فارسی نو و معنای «پرستشگاه» جای تردید دارد.\",\n          \"sources\": [\n            \"https://vajehyab.com/dehkhoda/هوخت\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:2388\",\n              \"status\": \"supports\",\n              \"note\": \"BQT vol. 4 pdf 471 (p. 2388): هوخ 'نام بیت‌المقدس است، و در قدیم قبله بوده است'; هوخت 'بمعنی هوخ است که بیت‌المقدس باشد'; Mo'in's note: 'هوخت در پهلوی hūxt (گفتار نیک) «مناس ۲۷۷» از اوستا hūxta (گفتار نیک) که در پهلوی به hu-gōwišn ترجمه شده' -- supports the etymology but shows that Borhan's meaning is different.\"\n            },\n            {\n              \"ref\": \"ETM:72\",\n              \"status\": \"not_checked\",\n              \"note\": \"no digital copy.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Glossary s.v. duš-hūxt\",\n              \"stance\": \"supports\",\n              \"note\": \"'The negative of hūxt (q. v.). Av. duž-ūxta-'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"s.v. dušhūxt\",\n              \"stance\": \"supports\",\n              \"note\": \"PHD.txt l.5423 index 'dušhūxt' (with hūxt 'good speech' as base).\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"vajehyab (Dehkhoda) s.v. هوخت\",\n              \"stance\": \"partial\",\n              \"note\": \"Dehkhoda: 'هوخت (اِخ) هوخ. بیت المقدس باشد (از برهان)' -- only the Jerusalem sense; vajehyab's Mo'in page for هوخت returned 404.\"\n            }\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Latin\",\n          \"words\": \"vox, voc; vocâre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin vōx, gen. vōcis 'voice, sound, word' continues the PIE lengthened-o-grade root noun *wṓkʷs (= Skt. vāk, Av. vāxš). Latin keeps the labiovelar as qu/c (vōc-). The denominative/o-grade verb vocāre 'to call' (*wokʷ-eh₂-) belongs with it (Umbrian subocau 'invoke'). Both are standard (Pokorny, Watkins, de Vaan).\",\n          \"derivation_fa\": \"لاتینی vōx (حالت اضافی vōcis) «آواز، صدا، سخن» دنبالهٔ نام‌واژهٔ هندواروپایی *wṓkʷs با بالاگونهٔ کشیدهٔ o است (برابر سنسکریت vāk و اوستایی vāxš). فعل vocāre «صدا زدن، خواندن» هم از همین ریشه است (اومبری subocau «فراخواندن»). پوکورنی، واتکینز و دو وان همه این را تأیید می‌کنند و ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/vox\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. wekw-: 'O-grade form *wokw- in: a. Latin vox (stem voc-), voice ... Suffixed o-grade form *wokw-a- in Latin vocare, to call'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 1135-1136\",\n              \"stance\": \"supports\",\n              \"note\": \"'Latin vox, vocis voice, voco, -are call, shout, cry, Umbrian sub-ocau'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 246\",\n              \"stance\": \"supports\",\n              \"note\": \"'lat. vox vocis „Stimme“ (s. o.), voco, -āre „rufen“, umbr. sub-ocau'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1971.txt l.263481 s.v. voice\",\n              \"stance\": \"supports\",\n              \"note\": \"'L. vōcem ... acc. of vōx, voice, sound, tone, call, rel. to vocāre, to call, fr. I.-E. base *weqʷ-, *woqʷ-, voice; to speak'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"18.11 VOICE\",\n              \"stance\": \"supports\",\n              \"note\": \"'Lat. vōx (> It. voce, Fr. voix, Sp. voz ...)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"voice, vocabulary\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"voice: Middle English vois, voice < Anglo-Norman/Old French voiz, vois (Mod. Fr. voix) < Latin vōcem, accusative of vōx. It came into English after the Norman Conquest (c. 1300). vocabulary (16th c.): a learned borrowing of Medieval Latin vocābulārium 'list of words', from Latin vocābulum 'appellation, name, word' = vocā(re) 'to call' + instrumental suffix -bulum.\",\n          \"derivation_fa\": \"انگلیسی voice از انگلیسی میانه vois / voice آمده، و آن از فرانسوی کهن (و انگلو-نورمان) voiz / vois و سرانجام از لاتینی vōcem (حالت مفعولی vōx) است. این واژه پس از فتح نورمان به انگلیسی راه یافت. vocabulary در سدهٔ شانزدهم از لاتینی میانه vocābulārium «فهرست واژه‌ها» وام گرفته شده، و آن از vocābulum «نام، واژه» است که از vocāre «خواندن» و پسوند -bulum ساخته شده. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/voice\",\n            \"https://en.wiktionary.org/wiki/vocabulary\",\n            \"https://en.wiktionary.org/wiki/vocabulum\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference for this node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1971.txt l.263398, l.263481\",\n              \"stance\": \"supports\",\n              \"note\": \"'vocabulary, n. ... ML. vocabulārium, list of words, fr. L. vocābulum'; 'voice, n. — ME. vois, voice, fr. OF. voiz, vois (F. voix), fr. L. vōcem'.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"s.v. voice\",\n              \"stance\": \"supports\",\n              \"note\": \"SKT.txt l.21012 'voice. (F.-L.) M.E. vois. O.F. vois (F. voix). — L. uōcem, acc. of uōx, voice, sound'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins s.v. wekw-\",\n              \"stance\": \"supports\",\n              \"note\": \"'Latin vox ...: VOCAL, VOICE, VOWEL; ... Latin vocare: VOCABLE, VOCATION'.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-16T05:27:26.983Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-538.json (file state is current in your context — no need to Read it back)
```


## [2026-10-16T05:27:44.418Z] TOOL CALL #102: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\nimport json\np='data/verification/page-538.json'\nd=json.load(open(p))\nfor n in d['entries'][0]['nodes']:\n    if n['id']==12:\n        for r in n['ref_check']:\n            if r['ref']=='ETM:72':\n                r['ref']='ETM:61'; r['note']=\"Abolghasemi, Risheh-shenasi (Etimoloji): no digital copy (refs_online.json).\"\n    if n['id']==13:\n        for c in n['consulted']:\n            if c['src']=='BRT':\n                c['where']='col. 1336 s.v. vaxəδwa-; col. 1333-1336 vāk-'\n                c['note']=\"BRT.txt l.20648 (Gs. 16) 'yezi humatəm mainyāt hūxtəm vā mrvāt hvarštəm vā vərəzyāt'; l.~22296 s.v. vaxəδwa- 'was zu sagen ist': 'humatōibyasca hūxtōibyascā ... (Y. 11.17) ... PFP. zum V. vak-' -- hūxta- 'well spoken' attested.\"\njson.dump(d,open(p,'w'),ensure_ascii=False,indent=2)\nEOF\npython3 -m json.tool data/verification/page-538.json >/dev/null && echo ok; python3 tools/verify_check.py 538"
}
```


### [2026-10-16T05:27:45.294Z] TOOL RESULT

```
ok
nodes verified: 16/16
node verdicts: {'confirmed': 7, 'plausible': 8, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'partial': 9, 'not_found': 2, 'not_checked': 7}
books consulted: {'supports': 45, 'silent': 5, 'partial': 10, 'contradicts': 2} | by book: {'PHD': 9, 'BRT': 8, 'CHEUNG': 8, 'NYB': 7, 'MON': 6, 'HRN': 5, 'HUB': 4, 'SYN': 3, 'WLD': 2, 'ARY': 2, 'POK': 2, 'KLN': 2, 'BQT': 1, 'KNT': 1, 'SKT': 1, 'AHD': 1}
```


## [2026-10-16T05:27:57.910Z] TOOL CALL #103: SubagentHandback

```json
{
 "message": "PDF page 538 (book p. 508) is done. The file is at /home/sfmqrb/git/rishe-private/data/verification/page-538.json and `verify_check.py 538` reports 16/16 nodes with 0 PROBLEM lines.\n\nIt has one entry, Wekw, Weqw (PIE *wekʷ- 'to speak', Pokorny 1135). The root is **confirmed**.\n\n**Node verdicts:**\n\n| Verdict | Count | Nodes |\n|---|---|---|\n| confirmed | 7 | 1, 6, 7, 11, 13, 15, 16 |\n| plausible | 8 | 2, 3, 4, 5, 8, 10, 12, 14 |\n| disputed | 1 | 9 |\n| transcription_suspect | 0 | – |\n\n**Disputed:**\n- **#9 navâ; xonyâ.** navā < Middle Persian nawāg < *ni-wāka- is fine. The problem is xonyā: its Middle Persian form huniyāg (MacKenzie hwnydʾk) has no -w-, so it cannot come from *hu-ni-vāka-. Wiktionary derives it from *xwan-iyā-ka-, the root of xwāndan 'to sing'. Nourai is following Mo'in's note in Borhan-e Qate' (hu + navā).\n\n**Other weak points, left as plausible:**\n- Several Iranian forms are reconstructions or Nourai's own inventions, not attested Avestan or Old Persian:\n  - 'paurvatâ-vac', which Nourai uses for pažvāk; paurvatā- 'mountain' cannot give paž- by regular sound change.\n  - 'vi-vačah'.\n  - 'hu-ni-vak'.\n  - 'vaxš-ô-bara', which is really a reconstruction *vaxša-bara- behind Middle Persian waxšwar.\n  - Old Persian 'wâk/wânk', which is not in Kent.\n- forūxtan 'to sell': Justi, Horn and Mo'in derive it from *fra-vaxš- 'cry out'. Cheung and Wiktionary instead put it first under *waxš- 'to grow'.\n- vâk 'sound' and vâžgân 'vocabulary' are 20th-century learned coinages. Dehkhoda knows واک only as the name of a water bird.\n- In Borhan and Dehkhoda, هوخت means 'Jerusalem'. The sense 'good words' is a learned revival from Pahlavi.\n\n**Extraction errors:** none. The JSON matches the printed page (I checked site/pages/538.jpg).\n\n**References I could not check:** ZMA, VSF and ETM have no digital copy (not_checked). KLN 1966 stops in \"va-\", so I checked the same entry in the 1971 edition. FSF:64 does not match this scan's pagination, and HRN:263 does not contain these words; both are recorded as not_found."
}
```


### [2026-10-16T05:27:58.200Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
