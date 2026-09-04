# Verification process log — verify-page-61


## [2026-09-04T23:02:28.897Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 61 only (note the recently added requirements: `derivation_fa`/`note_fa` Persian explanations, and `error_in`/`book_prints`/`correct_form` on any transcription flag). Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-61.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-61.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-61.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 61` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T23:02:31.001Z] AGENT

I'll start by reading the instructions file.


## [2026-09-04T23:02:33.174Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T23:02:33.185Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which
5	this repository (`/home/sfmqrb/git/rishe`) turned into JSON
6	(`data/extracted/batch/page-<pdf>.json`). Compact text renderings of the charts
7	are in `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-<pdf>.txt`.
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
38	   - `transcription_suspect` — the JSON data looks like a transcription error from the scan
39	     (a misread letter, an impossible form, a wrong Persian script); say what you think the
40	     book actually printed and why.
41	4. Record sources as URLs (Wiktionary page, Etymonline page, AHD appendix entry, archive.org
42	   page of Klein/Horn/Bartholomae, etc.). Also note when Nourai's own cited reference
43	   (KLN, POK, AHD, BQT, MON, HRN, HUB…) is itself the modern standard for that claim.
44	
45	
46	## Checking Nourai's OWN cited references (required)
47	
48	Every node carries `refs=` — Nourai's citations, e.g. `KLN:164; FVQ:75` (abbreviation:page;
49	`MON5:528` = MON vol. 5 p. 528). The author claims each arrow is supported by those pages.
50	You must check them:
51	
52	- The bibliography key (abbreviation → book) is in
53	  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt`.
54	- Where each reference can be read online is in
55	  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json`
56	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`).
57	- If `local_file` is set, the OCR text of that book is on disk: grep it for the headword
58	  (try several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and,
59	  if `page_offset` is given, locate the cited page (pages are separated by form-feeds; use
60	  `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one page). Read the entry and judge whether
61	  it actually says what Nourai's arrow says.
62	- **Scanned references without OCR text** (Borhan-e Qate' vols 3-5 = BQT pages ~1208-2475,
63	  Farahvashi's Iranvij = IRN, and any entry whose table record has a `scans` list): do NOT
64	  OCR whole books. Fetch only the cited page:
65	  `python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:918 --image`
66	  It renders that one page to PNG, OCRs it (Persian OCR is rough), caches both under
67	  `data/verification/sources/refs/ocr/`, and prints the text plus the PNG path. If the OCR
68	  is unreadable, Read the PNG (you can read Persian print directly), and then SAVE what you
69	  read: write the entry/entries you used (headword, Mo'in's etymological footnote, and any
70	  surrounding lines you relied on) verbatim to the companion file
71	  `data/verification/sources/refs/ocr/<ABBR>/<page>.vision.txt` (the tool prints the exact
72	  paths). The tool prefers that file next time, so nobody pays for reading the image again.
73	  If the printed page number on the image is off, re-run with `--pdf-page <n>` adjusted, and
74	  note the correct pdf page in your ref_check note.
75	- If `kind` is `website`, use the `lookup_hint` URL pattern with WebFetch.
76	- Do this for at least ONE cited reference per node (the most authoritative available:
77	  POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM/PLA for Semitic,
78	  BQT/MON for Persian). If none of a node's references is accessible, say so.
79	
80	Add to every node a `ref_check` array:
81	
82	```json
83	"ref_check": [
84	  {"ref": "KLN:164", "status": "supports", "note": "Klein s.v. 'cherub': Heb. kerūbh, prob. rel. to Akkad. karābu 'to bless', metathesis of b-r-k — exactly Nourai's claim."},
85	  {"ref": "FVQ:75", "status": "not_checked", "note": "no online copy"}
86	]
87	```
88	
89	`status` ∈ `supports` (the page says what the arrow says) · `partial` (the reference has the
90	word but a different/looser derivation) · `contradicts` (the reference says something else)
91	· `not_found` (checked the text, could not find the entry/page) · `not_checked` (reference
92	not accessible online). Quote the key phrase of the reference in `note` when you can.
93	
94	Also add to each entry a root-level `ref_check` for the root's own refs (e.g. `POK:244`).
95	
96	
97	
98	## Transcription flags: say WHERE the error is (required)
99	
100	For every node you mark `transcription_suspect`, look at the printed page itself — render it
101	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg<pdf page>`
102	(or open `site/pages/<pdf page>.jpg`) and Read the image — and add to the node:
103	
104	```json
105	"error_in": "book",            // "book" = the printed book has the odd form (author's misprint); the extraction is faithful
106	                               // "extraction" = the book prints the correct form; the JSON misread it
107	                               // "unknown" = could not decide from the image
108	"book_prints": "borrāgō",      // what the printed page actually shows
109	"correct_form": "borrāgō"      // the form that should stand (per the sources)
110	```
111	
112	Usually the extraction is faithful and the problem is in the book itself; say so plainly in
113	`derivation` too ("the book prints X; this is Nourai's misprint for Y"). Only when the JSON
114	differs from the page is it an extraction error (report those separately in your summary — the
115	owner fixes the data).
116	
117	
118	## Persian explanation (required): `derivation_fa` on every node, `note_fa` on every root
119	
120	Write the derivation a second time IN PERSIAN, for a Persian reader — not a translation of the
121	English sentence. Think about how a Persian etymologist (حسن‌دوست، ابوالقاسمی، معین در حواشی
122	برهان قاطع) would explain it to an educated Persian reader:
123	
124	- Use the established Persian terminology: هندواروپایی آغازین، ایرانی باستان، اوستایی، پارسی
125	  باستان، فارسی میانه (پهلوی)، پارتی، سغدی، فارسی نو/دری؛ وام‌واژه، وام‌گیری، دگرگونی آوایی،
126	  قلب (metathesis)، ابدال، همگونی، پیشوند، پسوند، ریشه، ستاک، تحول معنایی، معرّب، ریشه‌شناسی
127	  عامیانه (folk etymology)، هم‌ریشه (cognate)، دوگانه (doublet).
128	- Give the Persian word first in Persian script, then the older forms in Latin transliteration
129	  as Persian philology does (e.g. «آب» از فارسی میانهٔ āb / āp، از ایرانی باستان *āp-، هم‌ریشه با
130	  سنسکریت āp-). Persian-script forms for Arabic words; Greek/Latin words in Latin letters.
131	- Explain the sound changes in the way a Persian reader expects (e.g. «پ ایرانی باستان در میان
132	  دو واکه در فارسی میانه به ب نرم شده»؛ «ای کشیدهٔ فارسی میانه در فارسی نو به ی بدل شده»).
133	- Say clearly, in Persian, what the verdict means for the reader: ادعای نورایی درست است / با
134	  احتیاط پذیرفتنی است / پژوهش امروزی آن را رد می‌کند و به جای آن … می‌گوید / خطای چاپی کتاب.
135	- Keep it 2–5 sentences, formal but readable (نه ترجمهٔ لفظ‌به‌لفظ، نه ماشینی). Numbers in
136	  Persian digits are fine. Mention the key sources by their Persian-usable names (پوکورنی،
137	  بارتولومه، هرن، هوبشمان، مکنزی، نیبرگ، چونگ، معین، برهان قاطع، ویکی‌واژه).
138	
139	Field names: `derivation_fa` (node) and `note_fa` (root entry). Both required.
140	
141	## Process documentation (required)
142	
143	The owner wants to be able to audit every step later. Therefore:
144	
145	- **Every web page you rely on must be archived**: after you read a page (WebFetch or
146	  curl), run
147	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
148	  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
149	  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
150	  one Bash command to save time.)
151	- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` include
152	  the exact phrase(s) you found (with the grep pattern or page you used, e.g.
153	  "KLN.txt p.164 (ff-page 178): 'cherub … prob. rel. to Akkad. karābu'"), so the finding can
154	  be re-run.
155	- Your full transcript (every tool call and result) is exported automatically by the
156	  coordinator; nothing else needed for that.
157	
158	
159	## Use EVERY relevant book on disk (required)
160	
161	Checking only the reference Nourai cites is not enough. For every node, also consult the
162	other books in the local library that could speak to that claim, and record what each says.
163	The list of which books cover which kind of node, with file paths, is
164	`/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md`
165	(also `data/verification/sources/SOURCE_MATRIX.md`). Minimum per node:
166	
167	- an Indo-European node or root box: Pokorny (POK) AND Walde-Pokorny (WLD) AND Watkins/AHD,
168	  plus Mann (IEC) or Buck (SYN) when the word is a common noun;
169	- an Avestan / Old Persian node: Bartholomae (BRT) or Kent (KNT);
170	- a Pahlavi / Middle Persian node: MacKenzie (PHD) and Nyberg (NYB);
171	- a New Persian node: Horn (HRN), Hübschmann (HUB), Cheung (CHEUNG, for verbs), Borhan-e
172	  Qate' with Mo'in's footnotes (BQT), Mo'in (MON), and Aryanpur (ARY, once its text exists);
173	- a Sogdian node: Gharib (SOD); a Khotanese one: Bailey (ISS_alt_DKS);
174	- an Arabic node or a Persian/Arabic loan in either direction: Klein (KLN), Jeffery (FVQ),
175	  Addi Shir (AFM), Asbaghi (PLA), Fraenkel (AFA), Lokotsch (LKT); for French/Spanish
176	  Arabisms Pihan (PHN), Devic (DEV), Lammens (LAM), Dozy (DOZ);
177	- an English / Romance node: Klein (KLN), Skeat (SKT), Funk & Wagnalls (FSD), Webster (WEB);
178	  Anglo-Indian words: Hobson-Jobson (HJB), Whitworth (AID);
179	- a Turkic node: Vámbéry (TTS), Lokotsch (LKT).
180	
181	Grep each file for the headword (several spellings; Latin transliteration for the Western
182	books, Persian script for BQT/MON/ARY, Pahlavi transliteration for PHD/NYB). A grep that
183	finds nothing is also a result ("silent"). Record everything in a `consulted` array on the
184	node (separate from `ref_check`, which is only for the references Nourai himself cites):
185	
186	```json
187	"consulted": [
188	  {"src": "HRN", "where": "no. 3, p. 1", "stance": "contradicts", "note": "Horn separates āb 'Glanz' from āb 'water' and derives āftāb from the former"},
189	  {"src": "PHD", "where": "p. 5 s.v. ābād", "stance": "supports", "note": "'ābād [ʾpʾt] populous, thriving' — no water element"},
190	  {"src": "WLD", "where": "Bd. I p. 46", "stance": "silent", "note": "root ap- listed, no Persian compound"}
191	]
192	```
193	
194	`stance` ∈ supports / contradicts / partial / silent. Quote the key phrase. Books consulted
195	via the web (vajehyab for Mo'in, AHD online) go here too, with the URL archived via
196	fetch_source.py and listed in `sources`. Every node must have at least two `consulted`
197	entries from different books whenever the matrix lists two or more books for its language.
198	
199	## Sources to use (in roughly this order)
200	
201	- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
202	  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
203	  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
204	  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
205	  Use URL-encoded Persian/Arabic script for those pages.
206	- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
207	- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
208	  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
209	  appendix; the online appendix is the updated edition of the same list.
210	- **Pokorny** — via indo-european.info, starlingdb.org, or Wiktionary's Pokorny citation;
211	  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
212	- **Klein's Comprehensive Etymological Dictionary** (KLN) and **Horn's Grundriss der
213	  neupersischen Etymologie** (HRN), **Hübschmann's Persische Studien** (HUB),
214	  **MacKenzie's Concise Pahlavi Dictionary** (PHD), **Bartholomae AiW** (BRT) are on archive.org
215	  if needed for a hard case.
216	- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
217	- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
218	- Use WebSearch when you don't know the right page; use WebFetch to read a page.
219	
220	Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
221	If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
222	source covering the chain is enough; spend your effort on the Iranian and Semitic links,
223	which are where errors are likelier.
224	
225	## Output — write ONE file per page
226	
227	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
228	
229	```json
230	{
231	  "pdf_page": 126,
232	  "book_page": 96,
233	  "verified_by": "claude-fable-5-1",
234	  "verified_on": "2026-09-04",
235	  "entries": [
236	    {
237	      "entry": 0,
238	      "root": "Dheigh, Dhigha",
239	      "verdict": "confirmed",
240	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
241	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
242	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
243	      "nodes": [
244	        {
245	          "id": 6,
246	          "lang": "Avestan",
247	          "words": "pairi-daeza",
248	          "verdict": "confirmed",
249	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' (PIE *dʰeyǵʰ-, o-grade *dʰoyǵʰ-o- > Iranian *daiza-). Attested in the Vidēvdād (pairi-daēzaiiąn) …",
250	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza", "https://www.etymonline.com/word/paradise"]
251	        },
252	        {
253	          "id": 9,
254	          "lang": "Greek",
255	          "words": "paradeisos",
256	          "verdict": "confirmed",
257	          "derivation": "Borrowed from Old Iranian *paridaiza- (Median/Old Persian form with -d-, cf. Elamite par-te-taš, Akkadian pardēsu) in the 5th c. BCE; first in Xenophon (Anabasis 1.2.7) for the Persian kings' walled hunting parks. Greek -ei- renders Iranian /ai/ ~ /ē/; -os is the Greek nominative ending. The Septuagint (3rd c. BCE) used it for the Garden of Eden, whence the 'heaven' sense.",
258	          "sources": ["https://en.wiktionary.org/wiki/παράδεισος"]
259	        }
260	      ]
261	    }
262	  ]
263	}
264	```
265	
266	Rules:
267	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
268	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
269	- `words` = the transliterations of the node joined by "; " (copy from the chart).
270	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
271	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
272	- Keep `note` on the entry for root-level comments and for anything cross-cutting
273	  (e.g. "Nourai's whole Semitic branch here is rejected by Klein …").
274	- If a node lists several words, cover each word; if they differ in verdict, use the worst
275	  verdict for the node and explain per word in `derivation`.
276	- Where the chart's own NOTE already records a dispute (e.g. "POK:694 derives Latin mattus
277	  from root Mad"), evaluate it: say which side modern scholarship takes.
278	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted` (array) AND `derivation_fa` (string); every entry has `note_fa`.
279	- Valid JSON only. Test it with `python3 -m json.tool` before finishing.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason).
282	  Do not paste the JSON back into your reply.
283	
```


## [2026-09-04T23:02:33.587Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-61.txt"
}
```


### [2026-09-04T23:02:33.598Z] TOOL RESULT

```
1	=== PDF page 61 (book page 31) ===
2	--- entry 0 ---
3	ROOT [Semitic] A.q.r : to sting, injure  (refs FVA:278)
4	#1 (parent #0) [Arabic] refs=FVA:278; KFL:427 | aqrab : scorpion
5	  #2 (parent #1) [Persian] refs=FVA:278 | aqrab «عقرب» : scorpion | extra: عقربه ، عقارب
6	#3 (parent #0) [Hebrew] refs=KLN:1404 | aqrabh : scorpion
7	  #4 (parent #3) [Greek] refs=KLN:1401 | skorpios
8	    #5 (parent #4) [Latin] refs=AHD:1164 | scorpius
9	      #6 (parent #5) [French] refs=None | scorpion
10	        #7 (parent #6) [English] refs=KLN:1401; AHD:1164 | scorpion
11	--- entry 1 ---
12	ROOT [Indo-European] Ar, Are : to fit together  (refs POK:55)  PART 1
13	#1 (parent #0) [Avestan / Old Persian] refs=POK:56; IRN:28 | arta 2, areta : just, holy ; arata, aradra : true ; arta-arân : holy Aryan land ☞Al 1 ; arta-pa : protector of justice ☞Pa ; arta-xšathra : just king ☞Ksei 1 ; aipi-areta : determined ☞Epi
14	  #2 (parent #1) [Persian] refs=BQT:98-101; IRN:28 | ard «ارد ۱» : just ; ard «ارد۲» : 25th day of each Persian month ; Ardalân «اردلان» : a male name, "holy land of Aryans" ; Ardavân «اردوان» : a male name, "protector of justice" ; Ardešîr «اردشیر» : a male name, "just king" ; nard 1 «نَرد ۱» : backgammon | extra: آرد۲ | NOTE: "nard" is a distorted form of "Nîv-Ardešîr". See "Nei 1"
15	#3 (parent #0) [Sogdian] refs=SOD:58 | `rt`w : righteous, holy
16	#4 (parent #0) [Avestan] refs=POK:56; BQT:142 | aša 3 : true ; aša-vahišta : best justice ☞Su 1 ; arta-vah-išta : best justice ☞Su 1,Isto ; aša-van, ša-vant : determined, in order ; asvan : holy, sacred
17	  #5 (parent #4) [Pahlavi] refs=BQT:101,142; SNS:5 | aš-vahišt : best truth ; urt-vahišt : best truth ; ahru, ahrav, ašôg : sacred
18	    #6 (parent #5) [Persian] refs=BQT; MON:289; TZF:26 | Ordîbehešt «اردیبهشت» : "best truth" ; ašŭ «اشو» : true, heaven
19	#7 (parent #0) [Avestan] refs=WLD:74; POK:56 | râd 1 : right, correct, proper ; â-râd, â-râiti 1, â-râs- : to set up ☞Apo ; pati-râd : to trim ☞Per 1 ? ; vi-râiti, vi-radh : set apart ☞Wi
20	  #8 (parent #7) [Persian] refs=BQT:30,437,926,927; AEF:428; FFD:24 | râd «راد ۱» : liberal, brave ; ârâstan «آراستن» : decorate ; pîrâstan «پیراستن» : to trim (add or cut) ; vîrâstan «ویراستن» : to edit | extra: آرایش ، آرای ؛ پیرایه
21	
```


## [2026-09-04T23:02:36.082Z] AGENT

I'll start by gathering context files and the source JSON.


## [2026-09-04T23:02:36.958Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-61.json | head -200",
 "description": "Read source JSON for page 61"
}
```


### [2026-09-04T23:02:37.002Z] TOOL RESULT

```
{
  "pdf_page": 61,
  "book_page": 31,
  "entries": [
    {
      "root": {
        "name": "A.q.r",
        "lang": "Semitic",
        "refs": "FVA:278",
        "gloss": "to sting, injure"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVA:278; KFL:427",
          "words": [
            {"translit": "aqrab", "gloss": "scorpion", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:278",
          "words": [
            {"translit": "aqrab", "gloss": "scorpion", "script": "عقرب"}
          ],
          "script_extra": "عقربه ، عقارب",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:1404",
          "words": [
            {"translit": "aqrabh", "gloss": "scorpion", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Greek",
          "refs": "KLN:1401",
          "words": [
            {"translit": "skorpios", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": "AHD:1164",
          "words": [
            {"translit": "scorpius", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "scorpion", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "KLN:1401; AHD:1164",
          "words": [
            {"translit": "scorpion", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ar, Are",
        "lang": "Indo-European",
        "refs": "POK:55",
        "gloss": "to fit together"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:56; IRN:28",
          "words": [
            {"translit": "arta 2, areta", "gloss": "just, holy", "script": null},
            {"translit": "arata, aradra", "gloss": "true", "script": null},
            {"translit": "arta-arân", "gloss": "holy Aryan land", "script": null, "see": ["Al 1"]},
            {"translit": "arta-pa", "gloss": "protector of justice", "script": null, "see": ["Pa"]},
            {"translit": "arta-xšathra", "gloss": "just king", "script": null, "see": ["Ksei 1"]},
            {"translit": "aipi-areta", "gloss": "determined", "script": null, "see": ["Epi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:98-101; IRN:28",
          "words": [
            {"translit": "ard", "gloss": "just", "script": "ارد ۱"},
            {"translit": "ard", "gloss": "25th day of each Persian month", "script": "ارد۲"},
            {"translit": "Ardalân", "gloss": "a male name, \"holy land of Aryans\"", "script": "اردلان"},
            {"translit": "Ardavân", "gloss": "a male name, \"protector of justice\"", "script": "اردوان"},
            {"translit": "Ardešîr", "gloss": "a male name, \"just king\"", "script": "اردشیر"},
            {"translit": "nard 1", "gloss": "backgammon", "script": "نَرد ۱"}
          ],
          "script_extra": "آرد۲",
          "note": "\"nard\" is a distorted form of \"Nîv-Ardešîr\". See \"Nei 1\"",
          "quote": {
            "text": "نهادیم بر جای شطرنج نرد - کنون تا به بازی که آرد نبرد",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:58",
          "words": [
            {"translit": "`rt`w", "gloss": "righteous, holy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:56; BQT:142",
          "words": [
            {"translit": "aša 3", "gloss": "true", "script": null},
            {"translit": "aša-vahišta", "gloss": "best justice", "script": null, "see": ["Su 1"]},
            {"translit": "arta-vah-išta", "gloss": "best justice", "script": null, "see": ["Su 1", "Isto"]},
            {"translit": "aša-van, ša-vant", "gloss": "determined, in order", "script": null},
            {"translit": "asvan", "gloss": "holy, sacred", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "BQT:101,142; SNS:5",
          "words": [
            {"translit": "aš-vahišt", "gloss": "best truth", "script": null},
            {"translit": "urt-vahišt", "gloss": "best truth", "script": null},
            {"translit": "ahru, ahrav, ašôg", "gloss": "sacred", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT; MON:289; TZF:26",
          "words": [
            {"translit": "Ordîbehešt", "gloss": "\"best truth\"", "script": "اردیبهشت"},
            {"translit": "ašŭ", "gloss": "true, heaven", "script": "اشو"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
```


## [2026-09-04T23:02:38.620Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T23:02:38.688Z] TOOL RESULT

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


## [2026-09-04T23:02:42.104Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-61.json'))\nprint(json.dumps(d['entries'][1]['nodes'][6:], ensure_ascii=False, indent=1))\nprint('entries:', len(d['entries']))\nfor e in d['entries']:\n    print(e['root'], len(e.get('nodes',[])))\n\""
}
```


### [2026-09-04T23:02:44.384Z] TOOL RESULT

```
[
 {
  "id": 7,
  "parent": 0,
  "lang": "Avestan",
  "refs": "WLD:74; POK:56",
  "words": [
   {
    "translit": "râd 1",
    "gloss": "right, correct, proper",
    "script": null
   },
   {
    "translit": "â-râd, â-râiti 1, â-râs-",
    "gloss": "to set up",
    "script": null,
    "see": [
     "Apo"
    ]
   },
   {
    "translit": "pati-râd",
    "gloss": "to trim",
    "script": null,
    "see": [
     "Per 1 ?"
    ]
   },
   {
    "translit": "vi-râiti, vi-radh",
    "gloss": "set apart",
    "script": null,
    "see": [
     "Wi"
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
  "lang": "Persian",
  "refs": "BQT:30,437,926,927; AEF:428; FFD:24",
  "words": [
   {
    "translit": "râd",
    "gloss": "liberal, brave",
    "script": "راد ۱"
   },
   {
    "translit": "ârâstan",
    "gloss": "decorate",
    "script": "آراستن"
   },
   {
    "translit": "pîrâstan",
    "gloss": "to trim (add or cut)",
    "script": "پیراستن"
   },
   {
    "translit": "vîrâstan",
    "gloss": "to edit",
    "script": "ویراستن"
   }
  ],
  "script_extra": "آرایش ، آرای ؛ پیرایه",
  "note": null,
  "quote": {
   "text": "رخ دختران را بیاراستند - سر زلف بر گل بپیراستند",
   "poet": "Ferdowsî"
  }
 }
]
entries: 2
{'name': 'A.q.r', 'lang': 'Semitic', 'refs': 'FVA:278', 'gloss': 'to sting, injure'} 7
{'name': 'Ar, Are', 'lang': 'Indo-European', 'refs': 'POK:55', 'gloss': 'to fit together'} 8
```


## [2026-09-04T23:02:44.566Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['FVA','KFL','KLN','AHD','POK','IRN','BQT','SOD','SNS','MON','TZF','WLD','AEF','FFD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False))\n\""
}
```


### [2026-09-04T23:02:46.460Z] TOOL RESULT

```
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
KFL {"title": "Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885", "kind": "archive_djvu", "url": "https://archive.org/details/20260705_20260705_0657 (an Indian/other printing; OCR poor) ; better: text on shamela.ws (search 'فقه اللغة وسر العربية الثعالبي') with edition page numbers", "lookup_hint": "Look up by chapter/word on shamela; the 1885 Beirut pagination is not reproduced online.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/KFL.txt"], "page_offset": null, "covers_etymology": false, "notes": "Archive OCR of this copy is very poor; use shamela text."}
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"], "cites": "page number, continuous across the two volumes (1966–67)"}
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).", "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.", "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"}
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"], "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"}
IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"], "page_offset": "222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368.", "covers_etymology": true, "notes": "Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); (only the 'fas' pass was run for IRN.) Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. | OCR text, printed = pdf-11", "scans": [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "first_printed": 1, "last_printed": 210, "pdf_offset": 11, "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"}]}
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"], "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", "covers_etymology": true, "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209", "scans": [{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920, "last_printed": 2475, "pdf_offset": -1917, "lang": "fas", "offset_note": "printed = pdf+1917, checked at pdf 150 and 500", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"}, {"volume": "5", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf", "first_printed": 1, "last_printed": 290, "pdf_offset": 5, "lang": "fas", "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt", "requires_volume": true}], "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"}
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"], "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)", "covers_etymology": true, "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.", "cites": "entry number / page in Gharib's Sogdian dictionary"}
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "covers_etymology": true, "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."}
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"], "page_offset": null, "covers_etymology": true, "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).", "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"}
TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadable without login."}
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"], "page_offset": "Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).", "lookup_hint": "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.", "notes": "Tried IA (several queries), Google Books API (quota exceeded / not full view), HathiTrust (blocks automated access, 403). Band 2 (1927) is US public domain; Band 1 (1930) became US PD in 2026, so HathiTrust full view may exist - check manually at https://catalog.hathitrust.org/Search/Home?lookfor=walde+pokorny+vergleichendes. || UPDATE 2026-09: Bände I and II obtained in full from the Digital Library of India scans on archive.org (open, OCR layer in the _text.pdf).", "cites": "volume (WLD1 / WLD2) and page of Walde–Pokorny"}
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه‌شناختی فارسی' (Mehrafarin), also not online.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "none online; proxy via HRN/HUB. || RE-SEARCH 2026-09: still catalogue/purchase only (Open Library record; iketab second-hand; digikala dkp-3058984 for the 2015 ed.). Publisher of the 2015 ed. is مهرافروز."}
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"], "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).", "covers_etymology": true, "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Entries: headword, then 'فارسی میانه ... < ایرانی باستان *...' with Latin transliterations (best read in *_pages_faseng.txt or on the page image). | OCR text, printed = pdf-5"}
```


## [2026-09-04T23:02:55.990Z] AGENT

Now let me start the reference lookups. First, Klein on "scorpion" and Hebrew.


## [2026-09-04T23:02:57.566Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^scorpion\" KLN_1966.txt KLN_1971.txt | head -20; echo ---; grep -n \"scorpion\" KLN_1966.txt | head -40"
}
```


### [2026-09-04T23:02:57.663Z] TOOL RESULT

```
KLN_1971.txt:215336:scorpion, n. — ME. scorpioun , fr. OF. (= F.) 
KLN_1971.txt:215337:scorpion , fr. L. scorpidnem , acc. of scorpio, a col- 
KLN_1966.txt:34173:scorpion,  n.  —  ME.  scorpioun,  fr.  OF.  (=  F.) scorpion,  fr.  L.  scorpionem,  acc.  of  Scorpio,  a  col¬ lateral  form  of  scorpius,  fr.  Gk.  axopruoc,  which is  prob.  ult.  connected  with  Heb.  ‘ aqrabh , ‘scorpion’.  See  Albert  Schott,  Indogermanisch- semitische  Studien,  p.  77. scortation,  n.,  fornication.  —  Formed  with  suff. -ation  fr.  L.  scortari,  ‘to  associate  with  harlots', fr.  scortum,  ‘harlot’,  prop,  ‘skin’,  fr.  I.-E.  base *(s)qer-,  ‘to  cut’.  See  cortex.
---
2080:alacran,  n.,  scorpion.  —  Sp.  fr.  Arab,  al- aqrab, ‘the  scorpion’  fr.  al-,  ‘the’, and ‘aqrab,  ‘scorpion’, which  is  rel.  to  Fleb.  ‘aqrdbh,  Aram.  ‘ aqrabbd , Syr.  ‘ eqqarbd ,  Ethiop.  ‘aqrab,  'arqab,  Akkad. aqrabu,  ‘scorpion’.
25227:Nepa,  n.,  a  genus  of  insects,  the  water  scorpion (zool.)  —  L.  nepa,  ‘scorpion’,  of  African  origin, nepenthe,  n.,  a  drug  that  relieves  grief  and  causes forgetfulness,  —  Gk.  v/]7r£vffe?,  neut.  of  v7]7rev- frjj?,  ‘fee  from  sorrow,  soothing  pain’,  occur¬ ring  in  the  Odyssey,  IV,  221,  as  the  attribute  of cpippaxov,  ‘drug’,  formed  fr.  negative  particle VTj-  (see  no,  adv.,  and  cp.  nay)  and  Ttevffoc,  ‘pain, grief’,  which  is  rel.  to  r.i.&oc,  ‘a  suffering’.  See pathos.
34169:Scorpaenidae,  n.  pi.,  a  family  of  spiny-finned fishes  ( ichthyol .)  —  ModL.,  formed  with  suff. -idae  fr.  L.  scorpaena,  a  loan  word  fr.  Gk. axipnociva,  ‘a  kind  of  fish’,  lit.  ‘scorpion  fish’, fr.  oxop7tLo;,  ‘scorpion’.  See  scorpion  and  ep. sculpin.
34170:Scorpio,  n.,  1)  a  zodiacal  constellation;  2)  the eighth  sign  of  the  zodiac.  —  L.  Scorpio,  ‘scor¬ pion’.  See  scorpion.
34171:scorpioid,  adj.,  resembling  a  scorpion  or  its  tail.
34172:—  Gk.  axop7uo£tSY)<;,  compounded  of  axopmop, ‘scorpion’,  and -oeiSr,;,  ‘like’,  fr.  clSoq,  ‘form, shape’.  See  scorpion  and  -oid.
34173:scorpion,  n.  —  ME.  scorpioun,  fr.  OF.  (=  F.) scorpion,  fr.  L.  scorpionem,  acc.  of  Scorpio,  a  col¬ lateral  form  of  scorpius,  fr.  Gk.  axopruoc,  which is  prob.  ult.  connected  with  Heb.  ‘ aqrabh , ‘scorpion’.  See  Albert  Schott,  Indogermanisch- semitische  Studien,  p.  77. scortation,  n.,  fornication.  —  Formed  with  suff. -ation  fr.  L.  scortari,  ‘to  associate  with  harlots', fr.  scortum,  ‘harlot’,  prop,  ‘skin’,  fr.  I.-E.  base *(s)qer-,  ‘to  cut’.  See  cortex.
34282:sculpin,  n.,  any  of  a  group  of  spiny,  usually scaleless  seafishes.  —  Prob.  a  corruption  of  F. scorpene  or  It.  scorpina,  fr.  L.  scorpaena,  ‘the sea  scorpion’.  See  Scorpaenidae. sculpsit,  n.  —  L.,  ‘he  carved’,  3rd  pers.  sing.  perf. indie,  of  sculpere.  See  next  word, sculptor,  n.  —  L.,  ‘one  who  cuts  or  carves’,  fr. sculptus,  pp.  of  sculpere,  ‘to  carve’,  which  is  rel. to  scalpere,  ‘to  cut,  carve,  scrape’.  See  scalpel and  agential  suff.  -or.
```


## [2026-09-04T23:02:57.860Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"aqrab\\|'aqrābh\\|aqrabh\\|ʿaqrab\" KLN_1966.txt KLN_1971.txt | head -30"
}
```


### [2026-09-04T23:02:57.946Z] TOOL RESULT

```
KLN_1966.txt:2080:alacran,  n.,  scorpion.  —  Sp.  fr.  Arab,  al- aqrab, ‘the  scorpion’  fr.  al-,  ‘the’, and ‘aqrab,  ‘scorpion’, which  is  rel.  to  Fleb.  ‘aqrdbh,  Aram.  ‘ aqrabbd , Syr.  ‘ eqqarbd ,  Ethiop.  ‘aqrab,  'arqab,  Akkad. aqrabu,  ‘scorpion’.
KLN_1966.txt:34173:scorpion,  n.  —  ME.  scorpioun,  fr.  OF.  (=  F.) scorpion,  fr.  L.  scorpionem,  acc.  of  Scorpio,  a  col¬ lateral  form  of  scorpius,  fr.  Gk.  axopruoc,  which is  prob.  ult.  connected  with  Heb.  ‘ aqrabh , ‘scorpion’.  See  Albert  Schott,  Indogermanisch- semitische  Studien,  p.  77. scortation,  n.,  fornication.  —  Formed  with  suff. -ation  fr.  L.  scortari,  ‘to  associate  with  harlots', fr.  scortum,  ‘harlot’,  prop,  ‘skin’,  fr.  I.-E.  base *(s)qer-,  ‘to  cut’.  See  cortex.
KLN_1971.txt:10208:alacran, n., scorpion. — Sp. fr. Arab, al-aqrab, 
KLN_1971.txt:10209:‘the scorpion’ fr. al-, ‘the’, and < ‘aqrab, ‘scorpion’, 
KLN_1971.txt:10210:which is rel. to Heb. ‘ aqrdbh , Aram. ‘ aqrabbd , 
KLN_1971.txt:10211:Syr. ‘ eqqarbd , Ethiop. ‘ aqrab , l arqab, Akkad. 
KLN_1971.txt:10212:aqrabu, ‘scorpion’. 
KLN_1971.txt:215339:is prob. ult. connected with Heb. ‘ aqrabh ,
```


## [2026-09-04T23:03:06.516Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'scorpion,  n.  —  ME.' in l or 'scorpioun' in l:\n        print('leaf',i)\n        break\n# alacran\nfor i,l in enumerate(leaves):\n    if 'alacran' in l:\n        print('alacran leaf',i); break\nprint('total leaves',len(leaves))\nEOF"
}
```


### [2026-09-04T23:03:09.152Z] TOOL RESULT

```
leaf 744
alacran leaf 34
total leaves 903
```


## [2026-09-04T23:03:15.665Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (712,713,714,744,745):\n    t=leaves[i]\n    print('=== leaf',i, repr(t[:300]))\nEOF"
}
```


### [2026-09-04T23:03:17.762Z] TOOL RESULT

```
=== leaf 712 'uff.  -ary. Derivative:  retiary,  n.,  a  retiary  spider, reticence,  n.  —  F.  reticene,  fr.  L.  relicentia,  ‘si¬ lence’,  fr.  reticens,  gen.  -entis.  See  next  word and  -ce.\nreticent,  adj.,  inclined  to  keep  silent.  —  L.  reti¬ cens,  gen.  -entis,  pres.  part,  of  reticere,  ‘t'
=== leaf 713 '.  retrover- sus,  ‘turned  backward’.  See  retrorse. retroversion,  n.,  a  turning  backward.  —  Formed with  suff.  -ion  fr.  L.  retroversus.  See  prec.  word, retrovert,  tr.  v.,  to  turn  backward.  — -  Formed  fr. retro-  and  L.  vertere,  ‘to  turn’.  See  version, retrude,  tr.  v.,'
=== leaf 714 ' L.  revivere,  ‘to  live  again’,  fr. re-  and  vivere,  ‘to  live’.  See  vital.\nDerivatives:  reviv-able,  adj.,  reviv-abil-ity,  n., reviv-abl-y,  adv.,  reviv-al,  n.,  reviv-al-ism,  n., reviv-al-ist,  n.,  reviv-er,  n. revivification,  n.  —  Late  L.  revivificatio,  gen.  -onis, fr.  rev'
=== leaf 744 ' n.  —  It.  scopo,  ‘mark,  target,  thing  aimed at,  aim",  goal,  object’,  fr.  Gk.  avoitoq,  mark  to shoot  at,  watcher,  examiner,  spy,  scout’,  in  gra¬ dational  relationship  to  axcTnxor&at.,  ‘to  look about,  look  carefully  at’.  See  species  and  cp. spy.  Cp.  also  the  secon'
=== leaf 745 '.  escourgee,  ecourgee,  ‘whip, scourge’),  fr.  VL.  *ex-corrigiata,  ‘whip’,  fr.  L. ex-  (see  1st  ex-)  and  corrigia,  ‘shoestring,  strap’, which  is  cogn.  with  OIr.  cuimrech,  ‘fetter’.  Both L.  corrigia  and  OIr.  cuimrech  are  compound words.  For  the  first  element  of  these  '
```


## [2026-09-04T23:03:38.872Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in range(740,750):\n    t=leaves[i]\n    nums=re.findall(r'\\b1[34]\\d\\d\\b',t)\n    print(i, nums[:6], t[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T23:03:40.892Z] TOOL RESULT

```
740 [] ades,  shoulders’,  which  is of  uncertain  origin.  It  po
741 ['1394', '1393']  the  Tower  under  Henry  VIII. scazon,  n.,  1)  a  cholia
742 [] 91) fr.  schizo-  and  Gk.  p.uxY]Tei;,  pi.  of  ‘fun¬ gus’
743 [] ic  Greek  calendar  (corresponding  to  the  sec¬ ond  half
744 ['1401', '1402']  n.  —  It.  scopo,  ‘mark,  target,  thing  aimed at,  aim"
745 ['1405'] .  escourgee,  ecourgee,  ‘whip, scourge’),  fr.  VL.  *ex-c
746 []   referred  to. scriptorium,  n.,  a  writing  room  esp.  t
747 ['1406']   ON.  skarpr, OE.  scearp ,  ‘sharp’  (see  sharp).  Cp.  D
748 ['1408', '1409'] ence  also Swed.  sate,  Dan.  sxde;  rel.  to  OHG.  saze, 
749 ['1410'] second'.  See  second,  adj. securable,  adj.  —  Formed  fr
```


## [2026-09-04T23:03:49.635Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint(leaves[745][:3000])\nEOF"
}
```


### [2026-09-04T23:03:51.741Z] TOOL RESULT

```
.  escourgee,  ecourgee,  ‘whip, scourge’),  fr.  VL.  *ex-corrigiata,  ‘whip’,  fr.  L. ex-  (see  1st  ex-)  and  corrigia,  ‘shoestring,  strap’, which  is  cogn.  with  OIr.  cuimrech,  ‘fetter’.  Both L.  corrigia  and  OIr.  cuimrech  are  compound words.  For  the  first  element  of  these  words  see com-.  The  second  element  derives  fr.  I.-E.  base *reig-,  *rig-,  ‘to  bind’,  whence  also  W.  rhwym, ‘fetter’,  perh.  also  MHG.  ric,  gen.  rickes,  ‘band, fetter’,  ricken,  ‘to  tittup’, scourge,  tr.  v.  —  ME.  scorgen,  scourgen,  fr.  scorge, scourge.  See  scourge,  n.
scouse,  n.,  a  sailor’s  dish.  —  Short  for  lobscouse. scout,  n.,  spy,  watchman.  —  ME.  scoute,  fr.  OF. escoute,  ‘listener,  scout,  spy’,  fr.  escolter,  escou- ter  (F.  ecouter),  ‘to  listen’,  fr.  VL.  ascultare,  the beginning  of  this  word  having  been  mistaken  for the  pref.  ad-,  a-  (see  ad-),  and  changed  into  ex-, e-  (see  1st  ex-),  ult.  fr.  L.  auscultare,  ‘to  hear with  attention,  listen  to’.  See  auscultation. Derivative:  scout,  intr.  v.  (q.v.) scout,  intr.  v.,  to  act  as  a  scout.  —  ME.  scouten, fr.  scoute,  ‘scout’.  See  prec.  word.
Derivatives:  scout-er,  n.,  scout-ing,  n.  and  adj., scout-ing-ly,  adv.
scout,  tr.  v.,  to  treat  as  absurd,  to  reject.  —  Of Scand.  origin.  Cp.  ON.  skuta,  ‘a  taunt . scout,  n.,  the  guillemot,  the  puffin.  —  Prob.  a  var. of  scoter.
scout,  n.,  a  Dutch  vessel.  —  MDu.  schute  (Du. schuit).  Cp.  schuit.
scow,  n.,  a  large,  flat-bottomed  lighter.  —  Du. schouw,  fr.  MDu.  scouwe,  related  to  MDu. scolde,  scoelde ,  scoude ,  of  s.m.,  and  to  OS. scaldan,  ‘to  push  a  boat  from  the  shore’.
scowl,  intr.  v.,  to  frown.  —  ME.  scoulen,  sculen, of  Scand.  origin;  cp.  Dan.  skule,  ‘to  scowl’, which  is  prob.  rel.  to  OE.  sceolh,  ‘wry,  oblique’, sceoleagede,  ‘squint-eyed’,  OHG.  scelah,  ‘curv¬ ed’  (whence  MHG.  schelch,  G.  scheel,  ‘squint- eyed’),  fr.  I.-E.  base  *sqel-,  ‘crooked,  curved, bent'.  See  scalene  and  cp.  skulk.  Cp.  also Schiller.
Derivatives:  scowl,  n.,  scowl-er,  n.,  scowl-ing, adj.,  scowl-ing-ly,  adv.
scrabble,  intr.  v.,  to  scrawl.  —  Du.  schrabbelen, ‘to  scratch’,  freq.  of  schrabben,  ‘to  scrape’.  See scrape  and  verbal  suff.  -le  and  cp.  scramble. Derivatives:  scrabble,  n.,  scrabbl-er,  n. scrag,  n.,  1)  a  lean  person  or  animal;  2)  anything thin.  —  Prob.  of  Scand.  origin.  Cp.  Norw. skragg,  ‘a  lean  person’,  skraggen,  ‘lean,  scraggy’, Dan.  skrog,  ‘a  carcass’,  Icel.  skroggsligr,  ‘lean, scraggy’,  and  E.  shrink.
Derivatives:  scragg-y,  adj.,  scragg-i-ly,  adv., scragg-i-ness,  n.
scramble,  intr.  and  tr.  v.  —  A  nasalized  form  of scrabble.
Derivatives:  scramble,  n.,  scrambl-er,  n., scrambl-ing,  adj.,  scrambl-ing-ly,  adv.,  scrambt- y,  adj.
scran,  n.,  broken  victuals.  —  Of  uncertain  origin.
Cp.  ON.
```


## [2026-09-04T23:04:03.936Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in range(742,748):\n    t=leaves[i]\n    for m in re.finditer(r'\\b1[34]\\d\\d\\b',t):\n        print(i, m.group(), '...', t[max(0,m.start()-60):m.end()+60].replace('\\n',' '))\n    print('--- leaf',i,'len',len(t))\nEOF"
}
```


### [2026-09-04T23:04:05.695Z] TOOL RESULT

```
--- leaf 742 len 11865
--- leaf 743 len 11979
744 1401 ... s.  — -  See  scoria and  -fy. Derivative:  scorifi-er,  n. 1401 scorn,  n.  —  ME.  scam,  scorn,  fr.  OF.  esearne,  var.
744 1402 ...  Late  L.  Scoticus,  Scotticus.  See  prec. word. Scottish 1402 Scottish,  adj.  and  n.  —  ME.  Scoltisc,  fr.  Late  OE.
--- leaf 744 len 11391
745 1405 ...  metathesized  fr.  L.  scirpea,  ‘basket  made scrip 1 4U4 1405 scupper of  rushes’,  subst.  use  of  the  fem.  of  the  
--- leaf 745 len 11402
--- leaf 746 len 11779
747 1406 ... o  called  in allusion  to  the  appendage  of  the  calyx. 1406  ’ seat scutellate,  adj.,  covered  with  scutella  (bot. 
--- leaf 747 len 11890
```


## [2026-09-04T23:04:26.725Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins scorpion\"; grep -n -i \"scorpion\" AHD_watkins1985.txt | head; echo \"=== SKT\"; grep -n -i \"^scorpion\\|scorpion\" SKT.txt | head -5; echo \"=== KFL aqrab\"; grep -n \"عقرب\" KFL.txt | head -20; echo \"=== KFL size\"; wc -l KFL.txt"
}
```


### [2026-09-04T23:04:26.849Z] TOOL RESULT

```
=== AHD watkins scorpion
=== SKT
16669:•fion.  iF.-L.-Gk.)  F.  scorpion.^ HoHem^  ace.  of  storfio,  the  lame  as r,  —  Gk.  CKopm'itA,  a  scorpion,  also  a Ma6sh.  (^SKARP.)  See  Sharp. ih,  to  cut  with  narrow  incisions, )    Seoteh.  sb.,  is  a  slight  cut,  >uch
17038:old  word.  Supposed  to  be  derived  from L.  carchanu,  a  kind  of  dog'li&h  (perhaps through  an  O.  F.  form,  not  now  found).  ~ Gk.  impxQfifu,  a  kind  of  shark  ;  from  its sharp  teeth.  •»  Gk.  itapx^pos,  jagged  (as teeth).  Cf.  Skt.  karkara,  hard.  Der. jAari-rW^,  voracious,  prowling;  shark  up, to  snap  up ;  also  shirk,  better  sherk,  an- other spelling  of  iJuirkt  verb,  to  act  as  a shark,  to  prowl,  cheat,  avoid,  slink  from. Sharp.  (.E.)  A.  S.  jfrar/.  +  Du.  stktrp, Icel.  skarpr,  Swed.  Dan.  ikarp.  G.  siharf. Allied  to  L.  sc&iptre,  to  cut,  Gk.  aitopwiot, scorpion.     (V^KARP.)
=== KFL aqrab
6500:كُُ ضارب بِمُوَّخَرِهِ : يَْسَعٌ كالعقرب والزُثبُورٍ (0) 
24269:الصَّئِيْ : للعقرب والفأره . 
31670:-١‏ بعده فى ( ل ) : وصيحها » شكك العنكبوت » والعقرب. 
=== KFL size
37589 KFL.txt
```


## [2026-09-04T23:04:28.888Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW scorpius\"; grep -n \"scorpi\" LEW_1910.txt | head -10; echo \"=== LAT\"; grep -n \"scorpi\" LAT.txt | head -10; echo \"=== FSD\"; grep -n -i \"scorpion\" FSD_vol4.txt | head -5; echo \"=== WEB\"; grep -n -i \"scorpion\" WEB_vol1.txt | head -5"
}
```


### [2026-09-04T23:04:29.018Z] TOOL RESULT

```
=== LEW scorpius
=== LAT
5844:aceruatim congestae, quos scorpiones appellant, aut in effigie •mace¬
37051:docent ; 11,87, semper cauda scorpionis in ictu est, nulloque momento
41128:nepa, -ae {nepas,-ae Coi.) m.: scorpion, animal et constellation.
50591:pinSca, Apul., Herb.18, cf .scorpio), proserpinalis herba dans Mare.
56315:scorpiS, -Suis m. (et doublets podtiques scorpios, scorpius) :
56316:i° scorpion, et "raseasse"; a° non de plantes diyerses; 3 0 objets dvoquant
56317:le scorpion, nachine de guerre, fonet k pointea de fer, tas de pierres.
56319:Ddr. lat.: scorpionius, scorpiacum. De scorpionem pravient gat. skaurpjo.
=== FSD
2827:land ]   A   large  grasshopper  (Deinacrida megacephala)  resembling  a   scorpion,  that lives  under  decayed  trees  and  stones 6.  (Local,  U   SI  Thebowfin
4143:Scolecomorplia  Ket  l:  artistic,  art,  fat,  fare,  fast,  get,  prey;  hit,  police;  obey,  go;  not,  Cr;  full,  rOIe;  btrt,  bOm,  a   =   flnal,  i   =   hablt,  renew; scorpion  EetS  art,  ape,  fat,  X.ire,  fast,  what,  all;  me,  get,  prey,  fcm,  hit,  Ice,  1   =   5;  r=o,  go,  not,  or,  won,  wolf,  do.
4260:pios,  scorpion )   -   scor-pm'nld,  n   -   scor-pce'nold,  a   &   n Scor"pa>-norde-a,  1   skor  pI-nordw'*;28c6r'p5-nordc-a.n  pi Jeh  A   supcrfamlly  of  mall-cheeked  fishes,  especially  those with  normal  hypcrcoracotd,  hypocoracold,  and  posttemporal bones  including  Scorpsnidse,  Hexagrammldx,  etc  [< SCORPiEVA  +   -OID  1   —   toCOf''p{l>DOl'dD-aD,  fl  &n seor'pcnc,  1   skSr'pln,  2   8c6r'x>Cn,  n   A   fish  of  the  genus Scorpxna,  ns  the  European  hogflsh  (S  scrofa),  or  S   guttata of  southern  California  (<  It  scorpina,  <   L   scorpxna, see  ScoBP-ENv  1
4263:Scor'pi-o,  1   sker'pi-o,  2   acor'pi-o,  n   1.  Astron  (1) The  Scorpion,  a   constellation  of  the  zodiac  See  con- stellation (2)  The  eighth  sign  of  the  zodiac  Com- pare SIGN,  n   ,   7   Scor'pl-ust.  2.  A   genus  typical  of Scorpionidx  [   <   L   scorpion  j scor'pl'-old,  1   skor'pi-eid,  2   scor'pi-Sid,  a   1.  Scorpion* Id  e   2.  Rolled  or  curled  like  tho  tail  of  a   scorpion specifically  said  of  a   terminal  umlateral  iniaoresccnce that  18  circinate  or  coded  at  the  end,  as  m   the  borage family  l<  Gr  slorpioeldes  <   ♦ierpfoj,  scorpion,  4-  eidos, form  1   scor"pl-oi'daU;  scor'pI-on"lct. scor'pl-on,  1   skor'pi-en,  2   seor'pi-on,  n   1.  Any  one  of many  arachnids  of  the order  Scorpionidea,  from 2   to  8   inches  long,  resem- bling mimature  fiat  lob-  ^ sters  in  shape,  having  \ powerful  chelate  pcdi- palpa,  and  a   long  narrow flexible  abdomen  capable of  being  curled  up  over the  back  and  terminating  Scorpion  (Scorpio  afer).  ift In  a   poisonous  sting  They  Inhabit  warm  and  tropical  coun- tries, arc  nocturnal  In  habit,  viviparous,  and  prey  upon  other Insects,  killing  them  with  their  sting
4264:2.  Some  ammal  mistaken  for  or  likened  to  a   scorpion
=== WEB
3863:Avér-6-braii/chi-a, n. pl. [aero-, and Gr. branchia, gills.] a former subclass of Arach- nida, including the scorpions and spiders.
8348:An-ta/rés, n. [Gr. Antarés; anti, against, re- sembling, and Arés, Mars, so called from its resemblance to Mars in color.] a star of the first magnitude in the constellation Scorpio: also called the Scorpion's Heart.
10114:„Altar, south of the Scorpion.
10163:a-rach/nid, n. any of a large group of arthro- pods with four pairs of legs, lunglike sacs or breathing tubes, and a body usually divided into two segments: spiders, scorpions, an mites are arachnids. 5
11380:Ar-thro-gas/tra, n.pl. [arthro-, and Gr. gastér, the belly. an order of Arachnida in which the abdomen is distinctly divided into somites, or segments, as in the scorpion. a
```


## [2026-09-04T23:04:43.036Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '56310,56325p' LAT.txt; echo \"=== LEW\"; grep -n \"scorpio\" LEW_1910.txt | head"
}
```


### [2026-09-04T23:04:43.119Z] TOOL RESULT

```
avec de 1'ail", et par suite "exciter, aigrir, exaspdrer" (Aristo¬
phane). ,
scordlscus, -I,n.: selle de cheyal; scordiscum , cuir cru: scor-
discarius. Mots tardifs, de Scordisci, peuple d^llyrie.
scoria, -ae f.: scorie (Plin.). Enpr. au gr. axocpioc; M.L.773y.
scorpiS, -Suis m. (et doublets podtiques scorpios, scorpius) :
i° scorpion, et "raseasse"; a° non de plantes diyerses; 3 0 objets dvoquant
le scorpion, nachine de guerre, fonet k pointea de fer, tas de pierres.
Enpr. au gr.crxopTuoc, cntopmwv. M.L. 7741, 774 ia et 7740 scor poena, Trl.scoirp.
Ddr. lat.: scorpionius, scorpiacum. De scorpionem pravient gat. skaurpjo.
scortum, -I n.: i°peau, cuir; 3°prostitud, prostitude (cf. le
fr. vulgaire "peau") "quia ut pelliculae subiguntur", cf. Hqnnarstron ,
Eranos 33 (1935), i04sqq. ; et aussi Don. in Eu.434 abdomen in corpore
f eminarum patiens iniuriae coitus scortum dicitur. Une forne scortis
(d'hprbs pellis ?) est supposde par la glose; scortes ; i.e. pelles
testium arietinorum, ab eisdem pellibus dicti, P.F.443,8. - Ancien;
=== LEW
```


## [2026-09-04T23:04:43.793Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: ar-\" POK_full.txt | head -20; echo \"=== pages\"; grep -n -A3 \"lemma: ar-\" POK_full.txt | head -60"
}
```


### [2026-09-04T23:04:43.883Z] TOOL RESULT

```
6588:Root/ lemma: ario-?: master, lord, derived from Root/ lemma: ar-1', themat. (a)re-, 
6622:Root / lemma: ar-1', themat. (a)re-, heavy basis are-, re- and /-basis (a)n-, rei- 
6628:Root/ lemma: ar-V, themat. (a)re-, heavy basis are-, re- and /-Basis (a)n-, rei-\ "to move, 
6967:Root / lemma: ar-2ex er- 
7000:Root / lemma: ar-3 
7021:Root / lemma: ar-5 
27925:Root/ lemma: ar-l', themat. (ajre-, heavy basis are-, re- and /-Basis {ajn-, rei-\ "to move, 
=== pages
6588:Root/ lemma: ario-?: master, lord, derived from Root/ lemma: ar-1', themat. (a)re-, 
6589-
6590-schwere Basis ara-, re-und /-Basis (a)n-, rei-\ to move, pass: gr. apiaroq " best in birth 
6591-
--
6622:Root / lemma: ar-1', themat. (a)re-, heavy basis are-, re- and /-basis (a)n-, rei- 
6623-
6624-Meaning: to move, pass 
6625-
--
6628:Root/ lemma: ar-V, themat. (a)re-, heavy basis are-, re- and /-Basis (a)n-, rei-\ "to move, 
6629-
6630-pass' 
6631-
--
6967:Root / lemma: ar-2ex er- 
6968-
6969-Meaning: to distribute 
6970-
--
7000:Root / lemma: ar-3 
7001-
7002-l\^eaning: nut 
7003-
--
7021:Root / lemma: ar-5 
7022-
7023-Meaning: to refuse; to lie 
7024-
--
27925:Root/ lemma: ar-l', themat. (ajre-, heavy basis are-, re- and /-Basis {ajn-, rei-\ "to move, 
27926-
27927-pass' 
27928-
```


## [2026-09-04T23:04:54.918Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (63,64,65):\n    print('=== leaf',i)\n    print(leaves[i][:4000])\nEOF"
}
```


### [2026-09-04T23:04:57.000Z] TOOL RESULT

```
=== leaf 63
ch^  (Feist  Sa^  508  a^  WH.  I  87). Y«fl.  auch  Schwyzer  Gr.  Gr.  1  182.
pu  (s.  o.'^apu)  meist  in  der  Bed.  (,abge wendet^  =)  ^hinter^  zurück^*
ahd.  fona   (s.  o.);,   ai.  punar  ^wieder  zurück^^   gr.  nviiarog   ^der   letzte^ ;
o-anz  unsicher  lat.  puppis  ^Hinterteil  des  Schiffest o
WP.  I  47  ff.,  WH.  I  If.,  842,  Feist  3  a,  Trautmann  11.
apsä  ,Espe^
Ahd.  aspa,  nhd.  Espe,  ags.  cespe,  anord.  (^sp  L  ds.,  lett.  apse  (aus  *apuse), apr.  abse  ds.,  nordlit.  apitsis  f.,  lit.  apuse,  epuSe  f.  ,Espe,  Zitterpappel^ (nach  Bezzenberger  BB.  23,  298  angeblich  eine  freie  Deminutivbildung aus  *apsa),  russ.  osina  (*opslna)  ,Espe'^,  poln.  osa,  osika,  osina  ,Espe^ Daß  in  diesen  Espennamen  die  Lautfolge  -ps-,  nicht  -sp-  das  Ursprüngliche ist,  bestätigen  u.  a.  tiirk.-osm.  apsak  ,Pappel^,  tschuw.  eives  ,Espe^  als Lehnwörter  aus  dem  Urarmenischen  nach  Pedersen  KZ.  30,  462.  Specht setzt  wegen  gr.  dfteXXöv  aiyeigog,  8  ian  eidog  divSoov  Hes.  ein  Wurzel- nomen ap-  an.
WP.  I  50,  Specht  Dekl.  60.
I.  ar-^),  themat.  (a)re-,  schwere  Basis  ars-,  re-  und  i-Basis  (a.)ri-,  rei-  (ent- weder aus  dem  lo-Präs.  *(a)re-iö  entwickelt  oder  ursprünglich,  so  daß *(a)re-  vorkonsonantische  Entwicklung  daraus)  ,fügen,  passen^,  mehrfach und  vielleicht  ältest  vom  planmäßigen  Aufeinanderlegen  beim  Holzbau (auch   Steinbau??    Meringer   IF.  17,    124)   und  vom  Aufstapeln   von Hölzern,  aber  auch  vielfach  auf  geistiges  Zurechtlegen,  Berechnen  über- tragen. Ausführlich  bes.  Persson  Beitr.  632  f.,  666,  741  f.,  856. Av.  aränte  ,sie  setzen  sich  fest,  bleiben  stecken^,  ai.  ard-h  ,Radspeiche^, aram,  dlam  Adv.  {dramkar-,  alamkar  ,zurechtmachen^  und  ,dienen^,  wozu wohl  ara-ti-  ,Diener'^  und  rä-ti-  ,bereitwillig'^,  av.  räiü  ,dienstwillig,  Diener^) ,passend,  genug'^,   av.  ardm   ,passend,    entsprechend'^  (ardm-pid-tvä   ,Mittag^
^)  E.-M.  74  will  wegen  arm.  eri  ,Bug,  Schulter  von  Tieren',  y-eriurel  , anpassen'  eine Grundform  *er-  postulieren.  Aber  arm.  eri  geht  nach  Lidön  Mel.  Pedersen  88  f.  auf  idg. *reito-,  *reiti  zurück!     Vgl.  Trautmann  242.
56
=  ^die  zum  Mahle  passende  Zeh'^  woneben  ra-pid-wä  ds.  mit  Schwund- stufigem  ra-  neben  ^ara-,  wovon  ardin  Adv.^  Bartholoraae  Airan.  Wb.  189/ 1509)^  ratu-  m.,  ^Richter^  Schiedsrichter^  und  ^Zeitraum^  (gemeinsame Grundbedeutung  etwa  ^Zurechtlegung^^  woraus  .Zurechtlegung  des  Rechts^ und  ^richtiger  Zeitpunkt^);  ai.  ar-p-dyati  ^steckt  hinein^,  befestigt^;  über hett.  har-ap-  (karp-)  jhinstellen*^?  vgl.  Couvreur  H  114  f.;
arm.  arnem   ^mache^;,   y-ar   ^consentaneo^   congiunto^  contiguO;,    appresso' (arar  ^hat  gemacht^  =  gr.  Hoage),  wovon  yarem  ^aggiungere^  congiungere^ (Bugge  KZ.  S2,  21)^  car  ,schlecht^  mit  negativem  c  [=  oc]  ^nicht  passend'  | (Bugge  aaO.  23);
gr.  ägaglayicü,  Perf.  llgäga  ;,füge  zusammen'^,  Ugiisvog  ^angefügt^  passend'^ 'oag  ^Gattin'   (wohl  nach  Brugmann  IF.  2'S,  
=== leaf 64
293,    Schwyzer  Gr.  Gr.  I  434 hierher  mit  Präf.  *o-,  kaum  zur  Wz.  *ser-  oder  Wz.  *?^er-,  d-J^eigo))]   dazu öagl^ü)  ^liabe  vertrauten  Umgang'^;  auch  ^plaudere  vertraulich';  x^^'^^'^Q^^S ;,erzgefügt,   gepanzei't',   auch  xsQi-dgag   Ti%Vü)v   Pind.,   ^g-d-gov  , Glied,  Ge-  < lenk',  ägd-^ög  , Verbindung,  Freundschaft',  icgd-fiiog  ,vereint';  mit  ^-Suffixen  • homer.  dafi-or^-r- , Hausfrau'  (,die  des  Hauses  Waltende'),  äol.  doixogvLq  Hes. ;  ' Ttvlccgvrjg  , Hades  als  Verschließer  des  Unterweltstores'  (Schwyzer  Gr.  Gr. I  451,  5);    äge-   in  ägsaxco   ,gleiche   aus,    mache   gut,   befriedige',   dg€(Ty,EL IXOL  ,es  paßt,  gefällt  mir',  ägsaKsad-ccL,  dgsaaaa&ca  ,sich  verständigen,  einig werden  mit  jemandem;    sich  geneigt   machen,  versöhnen',   ägerrj  ,Tüchtig- keit',    dgsujüv  ,besser'  (in   Beziehung   steht  wohl  dgi-  ,sehr'  in   Kompositis, womit   Reuter  KZ.  31,  594  a  1  auch   ai.  ari-gürtd-,  -stutd-    als   ,eifrig  ge- priesen' vergleichen    möchte;    unsicher    wegen    gr.  igt-  ,sehr'   s.   Boisacq s.v.,  oben  S.  24  Anra.);  Icgiazog  ,besser,  best',  dgiGTsgög  ,links'.
Mit  Dehnung  d^vjx-rjgrjg  ,wohlgefällig',  oixrjgog  ,Gatte;  Geisel,  Unterpfand', ö(X7]gsa}  ,treffe  zusammen' ;  nach  Birt  Philol.  87,  376  f.  wäre  '^'Of.irjgog  eigentl. ,Begleiter,  der  Blinde,  der  mit  seinem  Führer  geht'.
Aus  dem  Slav.  vielleicht  poln.  ko-jarzyc  ,knüpfen,  verbinden,  vereini- gen' (z.  B.  Miklosich  EWb.  100,  Berneker  31,  532).
Über  das  vielleicht  verwandte  gr.  Uga,  lit.  ir  s.  4.  ar  ,nun,  also'.
Toch.  A  äriuar,  B  äricer,  ärivar  ,bereit',  A  ai^äm,  B  ere  ,Gesicht'  (vgl. lat.  figura).  Van  Windekens  BSL.  41,  56,  Duchesne-Guillemin  ebenda  173.
t-Bildungen:  rt-,  art-  ,zusammengefügt'.
Ai.  rtd-  n.  ,passend,  recht',  rtdm  n.  ,wohlgefügte,  lieilige  Ordnung'  (zur Bed.  s.  Oldenberg  GGN.  1915,  167—180;  nicht  .Opfer'),  rtena  ,rite',  av. ardta-,  dvdta-  n.,  apers.  arta-  (in  Kompos.)  , Gesetz,  Recht,  heiliges  Recht', av.  asa-  n.,  ,wa3  recht,  wahr  ist',  ai.  Ttävan{t)-  , ordnungsgemäß,  gerecht', av.  asävan{t)-]    ai.   rtü-h  ,bestimmte    Zeit,   Ordnung,    Regel',   rti-h   f.  ,Art,
57
Weise'  (zu  unserer  Wz.  nach   Kluge  PBrB.  9^  193;  s.  auch  Meringer  IF. l"    125    B.  Geiger  WZ  KM.  41,  107),  av.    aipi-drdta-  ^bestimmt,    fest   zu-
crewiesen^;
arm.  cird,  Gen.  -iL  (=  gr.  äoxvg^  lat.  artus,  -üs,  vgl.  auch  oben  ai.  T^u-h) <;truttura  costruzione,  ornamento'  (Hiibschmann  Arm.  Gr.  I  423,  Bugge KZ.  3'^^  3);  z-ard  ,apparatus,  ornatus^;  ard  , soeben,  jetzt'  (=  gr.  Icqti) ( Bartholomae  Stud.  II  23,  Bugge  aaO.;  Meillet  Esquisse  36),  ardar  , ge- recht' (Hübschmann  Arm.  St.  I  21,  Arm.  Gr.  I  423;  Persson  Beitr.  636  a  2
=== leaf 65
 eru'ilo't  dafür  auch  idg.  cZ/i;  vgl.  av.  arddra-  ,getreu,  zuverlässig,  glaubens- treu fromm'  und  die  anderen  unten  genannten  6?7i-Ableitungen),  ar^diun ,struttura   (Pedersen   KZ.  40,  210);
gr.  äixaoriq  ,gleichzeitig-  (Instr.  eines  *a(j.-aQT6g  , zusammengefügt,  zu- sammentreffend'), öj-L-aozecü  , schließe  mich  an  jemanden  an,  begleite'  (auf Grund  eines  *6'^-a^Tog) ;  ti-St.  in  do-cL-ßsTti^g  (,des  Wortgefüges  kundig'), C(QTL-Tto(v)g  ;mit  gesunden  Füßen*",  äoti-cpowv  ,mit  fest  (gefügt)  em  Verstände' (vermutlich  auch  in  ä'^ra^aog , Schlächter;  Mörder^,  wovon  äqua^xeo)  , schlachte, zerstückle',  nach  J.  Schmidt  Krit.  83  f.  aus  *a^rt-  oder  allenfalls  *äQTo- lauog  , kunstgerecht  zerschneidend'^  vgl.  ai.  rta-ni-  , richtig  führend',  rta- yuj  , richtig  eingeschirrt');  wohl  auch  ägTSf^r^g  , frisch  und  gesund',  ver- mutlich dissimiliert  aus  ^äQTL-öearjg  zu  difj^ag  ,mit  wohlgefügtem  Körper'; liOTL  ,eben,  gerade'  von  der  Gegenwart  oder  nächsten  Vergangenheit (vgl.  oben  arm.  ard  , soeben,  jetzt'  und  ard-a-cin  , neugeboren'  wie  gv. dQTL-yevrjg]  morphologisch  noch  nicht  ganz  klar,  vielleicht  Lokativ);  djr- aoTL  .genau,  gerade',  äoriog  , angemessen,  gerade,  vollkommen',  dgridLo) , spiele  gerade  oder  ungerade',  dgri^o)  , mache  fertig,  bereite',  ^gaiov  6i- vMLOv  Hes.,  dvdQGiog  ^feindlich',  i/raQzrjg  ,gerüstet';
dgTvv  (piXiav  %al  Gv^ßaaiv^  dozvg'  GvvTa^ig  (=  lat.  artus)  Hes.,  dQTvo)^ doTvvcü  ,füge  zusammen,  bereite',  dozvvag,  lHqzvvog,  dgzvrriQ  Beamtentitel von  Argos,  Epidauros,  Thera.
Lat.  artus  ,eng  in  Raum  und  Zeit,  straff'  (Adv.  arte,  ursprüngl.  Instru- mental wie  ä(.Lagzrj)]  ars,  -tis  ,die  Geschicklichkeit,  Kunst,  Art  und  Weise' (eigentlich  , Zusammenfügung,  Gabe  richtig  zusammenzufügen'  =  mhd. art),  dazu  die  Komposita  in-ers  ,kunstlos,  träge',  soU-ers  ,geschickt',  allers, alers  ,gelehrt';  artlö,  -Ire  ,fest  zusammenfügen,  zusammenpressen'  (jünger artäre)]  artus,  -üs  , Gelenk,  Glied',  articulus  ,ds.;  Augenblick,  Wende- punkt';
lit.  arti  ,nahe'  (Lok.  des   ^i-St.);
mhd.  art  f.  ,Art  und  Weise',  anord.  ein-ardr  , einfach,  aufrichtig',  eingrd ,  Zuverlässigkeit';
toch.  B  ar{t)lcye  ,reich,  wertvoll' (?).
58
jm-Bildungen:
A.  Von  der  leichten  Basis  ar-. Arm.  y-armar  ^passend,  angemessen^  (Bugge  KZ.  32^  21);
gr.  &Q!J.ög  ;Fuge;,  Zusammenfiigung,  Gelenk^,  &o fxot  ,ehen,  jüngst'  (ägfiö^o) ^verbinde,  füge  zusammen,  passe  an,  ordne',  &Q(.iovia  ,Verbindung,  Bund, Ebenmaß,  Einklang'),  ^Qf-
```


## [2026-09-04T23:05:22.689Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in range(66,70):\n    t=leaves[i]\n    print('=== leaf',i,'(p.',i-8,')')\n    print(t[:5000])\nEOF"
}
```


### [2026-09-04T23:05:25.002Z] TOOL RESULT

```
=== leaf 66 (p. 58 )
ia  , Wagen'  (über  den  *  dieser  Worte  s.  Sommer Gr.  Lautst.  133,  Meillet  BSL.  28,  c.-r.  21  f.  [*arsmo-?l  Schwyzer  Gr. Gr.  I  306;  weitere  Lit.  bei  Boisacq  79),  äqualia  ,zugeteilte  Nahrung,  Pro- viant' ;
lat.  arma,  -örum  ,  Gerätschaften,  Rüstzeug,  Waffen',  armentum  ,Rudel von  Pferden  oder  Rindern'.
Daran  klingt  an  a^nor d.  jgrmuni  ,Rind,  Pferd'  und  die  PN  got.  *Airmana- reiksj  ags.  Eormenrlc,  aisl.  Jqrmunrehr,  mhd.  Ermenrlch-^  dasselbe  erste Glied  zur  Bezeichnung  von  etwas  großem  auch  z.  B.  in  Ermunduri , Groß- thüringer', anord.  jqrmungrund  ,die  weite  Erde'  ==  ags.  eormengrundj ahd,  irmindeot,  as.  Irmin-sül^  und  in  der  Kurzform  Herminones.  Doch  be- streitet Brückner  KZ.  45,  107  mit  Recht,  daß  , Großvieh'  die  ursprüng- liche und  ,groß'  die  daraus  abgeleitete  Bed.  sei  und  entscheidet  sich  um- gekehrt für  ;groß,  erhaben*  als  Ausgangspunkt  wegen  slav.  ramem  ,ge- waltig,  stark,  heftig,  plötzlich'  (ob  hierher  lit.  ermas  , Ungeheuer',  lett. erms  ,Af£e,  Possenreißer,  wunderliche  Erscheinung'?),  das  als  , empor- geschossen' zu  *er-,  *o?'-  (onor  usw. ;  vgl.  formell  OQ^svog),  nicht  als  , fest- gefügt, massiv'  zu  *ar-  , fügen'  gehört.
Aksl.  jarbm%  ,Joch'  (z.  B.  Miklosich  EWb.  100,  Berneker  31),  sloven. jermen  , Jochriemen,  Riemen';  mit  schwundstufigem  Anlaut  und  themat. Vokal:  aksl.  remem,  serb.  remen  usw.  ,Riemen';  Specht  Dekl.  149  f.
Toch.  B  yarm,  AB  yärm  ,Maß'.
B.  Von  der  schweren  Basis  ar^-mo- :  r-mo-  ,Arm'.
Ai.  irmd-h  ,Arm,  Vorderbug'  (ursprüngl.  ,Achselgelenk',  vgl.  Ixq&qov, lat.  artus)  =  av.  ardma-  ,Arm',  osset.  arm  ,hohle  Hand',  älm-ärin,  ärm-äiin , Ellenbogen',  lat,  armus  .der  oberste  Teil  des  Oberarms,  Schulterblatt,  bei Tieren  der  Vorderbug'  (aus  *ar(d)mos),  gall.  aramö  , Gabelung',  *aramones ,Scherenarme  der  Deichsel'  (Wartburg  I  119,  Jud  bei  Howald-Mejer  Rom. Schweiz  374ff.),  apr.  irmo  f.  ,Arm',  lit.  irmede  (,Armfraß',  d.  i.:)  , Gicht  in den  Gelenken',  irm-liga  , Gicht'  (s.  Trautmann  Apr.  347);  hochstufig  lit. zem.  PL  tant.  armai  ,Vorderarm  am  Wagen'  (ibd.),  aksl.  ramo,  rame, serb.  räme  ,Schulter',  got.  arms,  ahd.  usw.  arm  ,Arm',  arm.  armukii  ,Ellen- bogen'  (Hübschmann  Arm.  Stud.  I  21).
59
AVzf.  re-,  ro-:
Lat.  reo7',  rei-l  _,berechnen;  meinen;  dafürhalten^  (das  primitivste  Zählen ^jrd  vom  Aufeinanderlegen  oder  -schichten  der  zu  zählenden  Stücke  be- trleitet)  Partiz.  ratus  ,in  der  Meinung^,  aber  auch  ^berechnet,  bestimmt, Z\x\iW,  rechtskräftig^;  ratio  ^Berechnung;  Erwägung;  Vernunft';  Beweggrund; Grund''  nach  EM.  793  hierher  (prö)portiö  aus  jportiöne  =  pro  ratiöne]
o-ot.  *garapjan  (nur  Partiz.  garapana)  ;Zählen';  an.  hundradj  nhd.  Hundert (*rada  n.  ;Zahl'  =  lat.  rätum;  s.  Fick  IIP  336);  ahd.  girad  ;gerad  (nur von  Zahlen)^
=== leaf 67 (p. 59 )
;  nhd.  gerad  (nur  von  durch  2  teilbaren  Zahlen;  verschieden von  gerad  =  geradeaus);  mit  neuem  Ablaut  anord.  tl-redr  eigentlich  ;nach Zehnern  gezählt'  (Fick  III^  336);  got.  rapjö  ;Zahl;  Rechnung;  Rechen- schaft'; as.  rethia  jR^chenschaft';  ahd.  radja,  redea  ;Rechenschaft;  Rede und  Antwort;  Rede,  Erzählung';  afries.  hirethia  ;anklagen';  as.  rethiön^ ahd.  red(i)ön  , reden'  (die  genaue  Übereinstimmung  von  rapjö  mit  lat. ratio  bestimmt  z.  B.  Kluge  ^^  s.  v.  ,Rede'  zur  Annahme  von  Entlehnung des  germ.  Wortes  unter  Einfluß  von  garapian,  richtiger  scheint  mir Falk-Torp  886  rapjö  als  primäre  -löTi-Ableitung  von  der  germ.  Wz.  *rap- [garapjan]  zu  bestimmen).
Ob  hierher  auch  anord.  rgd  ;Reihe;  bes.  dem  Strande  entlang  ziehende Erhöhung^;  mnd.  rat  f.  ;Reihe'?  (Fick  IIP  337;  ;Reihe'  als  ;aneinander Gefügtes,  Geschichtetes'?).
Ahd.  rämen  ;nach  etwas  trachten,  streben,  zielen';  as.  römon  ^streben'; mhd.  mnd.  räm  ,Ziel'  kann  als  ;geistig  zurechtlegen;  berechnen'  unserem *re-  zugehören,  wenn  auch  dabei  das  (erst  jünger  belegte)  Subst.  räm als  Bildung  mit  Formans  -mo-  der  Ausgangspunkt  gewesen  sein  muß.
dh-Erweiterung  re-dh-,  rö-dh-,  rs-dh-:
Ai.  rädhnöti,  rädhyati  ;macht  (passend)  zurecht;  bringt  zustande;  gerät; gelingt;  hat  Glück  womit;  befriedigt;  gewinnt  jemanden';  rädhayati  ;bringt zustande;  befriedigt';  rädha-h  m.,  rädhah  n.  ;Segen;  Gelingen;  Wohltat, Gabe;  Freigebigkeit';  av.  rädaiti  ;macht  bereit',  rada-  m.  ;Fürsorger'; rädah-  n.  , Sichbereitstellen,  Bereitwilligkeit  (in  religiöser  Hinsicht)',  apers. rädiy  (Lok.  Sg.)  , wegen'  (vgl.  aksl.  radi  s.  unten),  npers.  äräyad,  ärästan ,schmücken';  air.  imm-rädim  ;überlege;  überdenke';  acynir.  amraud  ;mens'; ncymr.  amrawdd  ;Gespräch'  mit  ders.  Bed.  wie  air.  no-räidiu,  no-rädi^n jSage',  mcjmr.  adrawd  ,erzählen'  und  got.  rödjan^  anord.  reda  ,reden^ (vgl.  auch  oben  nhd.  Rede,  reden]  no-räidiu  und  rödjan  setzen,  wie  sL, raditi,  ein  kaus.-iter.  *rödheiö  fort);  got.  garedan  ,worauf  bedacht  sein, Vorsorge  treffen',  urredan  ,urteilen,  bestimmen'  (vgl.  zur  Bed.  bes.  lat. rerl),  undredan  , besorgen,  gewähren',  ahd.  rätan  , raten,  beratschlagen, worauf  sinneu;  anstiften,   deuten  (Rätsel),    auffordern,  wofür  sorgen,  ver-
60
schaffen',  as.  rädan,  anord.  räda,  ags.  7'zdan  (letzteres   auch  ,Iesen',  eno read),  Subst.  ahd.  rät  m.  ^vorhandene  Mittel,  Rat,  Ratschlag,  Überlegung Entschluß,   Absicht,  Vorsorge,  Vorrat',   ähnlich   as.    räd,   anord.  räd,  ag rxd]   aksl.    raditi   ,sorgen'   (serb.    rädim,    rdditi   ,arbeiten,    trachten',   rai , Geschäft,  Arbeit';    s.   ühlenbeck  KZ.  40,  558  f.),   radi   ,wegen',    woneben *raJA-  in  aksl.  nerod^  ,Vernachlässigung',  sloven.  rqdim,  rqditi  , so
=== leaf 68 (p. 60 )
rgen,  sich kümmern'.
Wzf.  {a)rl-,  rei-  (s.  Person  Wzerw.  102,  162,  232;  Beitr.  741):
Gr.  dgaglayiw  (wenn  nicht  Neubildung,  s.  oben  S.  56),  äoLd-^dg  ,Zahl',  vi^giroq , ungezählt',  arkad.  ircdgirog  ^iTtlXs'ATog,  auserlesen',  dQLjxd^SL'  äQ^xot^ei  Hes. lat.  rltuSj  -üs  ,hergebrachte  Art  der  Religionsübung,  Gebrauch,  Sitte,  Ge- wohnheit, Art',  nie  ,in  passender  Art,  nach  dem  rechten  religiösen  Ge- brauch^ (Lok.  eines  neben  rl-tu-s  liegenden  kons.  St.  *7'I-^);  air.  rim  ,ZahP, äram  (*ad-ri-ma)  ds.,  do-rimu  ,zähle',  cymr.  rhif  ,Zahl',  anord.  nm  n. , Rechnung,  Berechnung',  as.  unrim  , Unzahl',  ags.  rm  n.  ,Zahl',  ahd.  rim m.  ,Reihe,  Reihenfolge,  Zahl'  (die  Bed.  ,Vers,  Reim'  von  anord.  und  mhc rim  wohl  nach  Kluge  ^'^  s.  v.  Beim  aus  frz.  rime,  das  aus  rythmus  her- zuleiten ist).
Vielleicht  ist  auch  *m-  , Sache'  (lat.  res  usw.)  nach  Wood  a^  226  an- zureihen als  Wznomen  der  Bed.  , aufgestapeltes  Hab  und  Gut'.
Dazu  wahrscheinlich  als  JA-Erweiterung  rei-dh-  (vgl.  oben  re-dh neben  re-):
Got.  garaips  , angeordnet,  bestimmt',  raldjan,  garaidjan  ,verordnen,  he- stimmen',  anord.  g-reidr  , bereit,  leicht,  klar',  greida  , auseinanderwickeln ordnen,  zurechtlegen,  zustande  bringen,  entrichten,  zahlen',  mhd.  reiten ,zurüsten,  bereiten,  zählen,  rechnen,  berechnen,  bezahlen',  reite,  gereite bereite,  ahd.  hireiti  ,bereit',  antreltl  ,series,  ordo',  lett.  riedu,  rizt  , ordnen raids  ,bereit,  fertig',  ridi,  ridas  , Gerät,  Kram'.
Ganz  fraglich  ist  die  von  Persson  aaO.  erwogene  Zugehörigkeit  von aksl.  orqdije  ,apparatus,  instrumentum'  (nicht  aus  ahd.  ärunti  , Botschaft' entlehnt,  s.  Pedersen  KZ.  38,  310),  red^  ,Ordnung',  lit.  rinda  ,Reihe', lett.  rinda  ,Reihe,  Zahl'.  Unter  der  Voraussetzung,  daß  diese  idg.  d,  nicht dh  fortsetzen  (*re-n~d-),  reiht  man  (z.  B.  Fick  I*  527,  Pedersen  aaO., s.  auch  EM.  711)  auch  die  folgende  Sippe  an:  Sgöeo)  ,lege  ein  Gewebe an',  6qölx6v'  töv  x^tcüvIg-aov.  Rägioi,  h'QÖrjua'  fj  toIvtct]  t&v  iglcov  Hes., lat.  ördior,  -iri,  örsus  sum  (aus  der  Webersprache,  Breal  MSL.  5,  440) , anzetteln,  anreihen,  anfangen,  beginnen',  exördior  ,zettle  ein  Gewebe  an'. redördior  ,hasple  ab',  ördo,  -inis  ,Reihe,  Ordnung'  (auch  umbr.  urnasier scheint  =  ordinariis  zu   sein,  Linde   Glotta  3,  170 f.;  anders  Gl.  5,  316),
61
T-ifft  der  Zusammenhang  mit  ar-  ^fügen'^  das  dann  auch  von  der  Weberei <r  braucht  gewesen  wäre^  zu  (Persson  Wzerw.  26^  Thurneysen  Thes. 
=== leaf 69 (p. 61 )
^  ter  artuSj  -üs),  so  wäre  der  Vokal  von  "^or-d-eiö  als  Kausativ-Iterativ- Vokalismus  zu  rechtfertigen.
jSToch  fraglicher  ist^  ob  nach  Reichelt  KZ.  46^  318  als  ^-Erweiterungen der  Basen  ar9-,  ar-  mit  derselben  Anwendung  auf  die  Weberei  auch  an- zureihen seien:
Gr.  dcodxyfj  , Spinne^,  lat.  aräneics  ^zur  Spinne  gehörig^;  aränea,  -eus Spinne^  i^ard-k-snä]  der  Wortausgang  zu  *s72e-  ,nere^  als  ^Netzspinnerin^?); nuo-eblich  dazu  (Walter  KZ.  12,  377,  Curtius  KZ.  13,  398)  gr.  ^Q-Avg  ,Netz', ao'/Mvfj'  tb  qdufxa  (ft  tov  aTrjf.tova  iyy,aTa7tlsy,ov(nv  al  ÖLa^öf^evai  Hes.  (s.  auch Boisacq  79),  wozu  nach  Bezzenberger  BB.  21,  295  lett.  er  hüls  , Spindel; Wickel  von  Heede  zum  Spinnen^  (das  für  '^■arkuls  stehen  kann).  Liden IF.  18,  507  f.  stellt  besser  ^o'/.vg  zu  slav.  "^orkyta,  serb.  räkita  , Rotweide' und  lett.  erciSj  gr.  Ixgxsvdog  ,Wacholder'  als  Sträuchern  mit  zum  Flechten verwendbaren  Zweigen.    S.  unten  arkii-  und  erk-.
WP.  I  69  ff.,  WH.  I  69,  70,  Trautmann  13  f.
2.  ar-  oder  er-  ,zuteilen;  (med.)  an  sich  bringen^,  mit  idg.  n?t-Präs.
Av.  ar-  (Präs.  drdnav-^  drdnv-,  Prät.  Pass.  drdnävi)  ,gewähren,  zuteil werden  lassen;  gewährleisten',  mit  us-  und  frä  ,(als  Anteil)  aussetzen und  zuweisen^,  frdrdta-  n.  ^Zuweisung  (von  Opfern  u.  dgl.),  Darbringung^ (Bartholomae  Altiran.  Wb.  184 f.);
arm.  afnum  ,ich  nehme',  Aor.  ar  (Hiibschmann  Arm.  Gr.  I  420;  die Bed.  aus  medialem  , teile  mir  zu'  vgl.  ai.  ddlämi  ,gebe^ :  ä  date  ,nehme an  mich,  empfange';  ebenso  in:)
gr.  lcovvf.iai  , erwerbe,  suche  zu  erreichen,  empfange,  bes.  als  Preis  oder Lohn';  durativ  gegenüber  äoea-d-ac  , erwerben,  gewinnen*^,  Aor.  äoö^rjVj 7]qö^7]v]    ixiad-dQVTjg^  (.iia-d-agvog   , Lohnarbeiter',    liQog   n.    ,Nutzen^   (Aesch.);
hitt.  ar-nu-mi  ,ich  bringe'^  (Schwyzer  Gr.  Gr.  I  696)  gehört  wohl  eher als  Kausativ  zu  3.  er-  ,sich  in   Bewegung  setzen'.
Den  Hochstufenvokaligmus  der  Wz.  sicherstellende  Formen  fehlen.
WP.  I  76  L
3.  ar-  (durch  -ei-,  -öi-,  -u-  erweitert)  ,Nuß^
G.  Meyer  Alb.  Wb.  17  vereinigt  gr.  l^ovcc'  zä  ''HQa'^lscjTi'/.ä  '/.dova  Hes., alb.  arre  f.  , Nußbaum',  aksl.  orech^  ,Nuß^  Beziehung  zu  lit.  riesutas, ruo^utys  , Haselnuß',  lett.  rieksts  ,Nuß,  Haselnuß',  apr.  huccareisis  , Buch- ecker' (s.  Trautmann  Apr.  314)  nimmt  Specht  Dekl.  62  an.
WP,  I  77.
62  '
4.  ar  (er,  or?),  r  etwa  ,nun,  also^,  auch  als  Fragepartikel.
Gr.  ä'o«;  äo,  Qa  (aus  r)  ,nun,  also^  folglich',  kjpr.  «^,  ^ö«  Fragepartikel (*^  ä'^a;  ya^,  vielleicht  aus  /  Uq);  ebenfalls  schwundstufig  lit.  ir  ,und,  auch'^; lett.-  ir  ,auch',  apr.  ir  ,und,  auch'  (=  gr.  ga),  hochstufig  lit.  ar,  lettj ar  als  Einleitung  eines  Fragesatzes,  alit.  auch  er  mit  demselben  halt. Schwanken  von  a-  und
```


## [2026-09-04T23:05:35.981Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint('n leaves',len(leaves))\nfor i in (81,82,83):\n    print('=== 0-based leaf',i)\n    print(leaves[i][:3500])\nEOF"
}
```


### [2026-09-04T23:05:38.162Z] TOOL RESULT

```
n leaves 895
=== 0-based leaf 81
                                 i




                                                     ar-                                 73

groBen,   miBgestalteten. crmingas „unformlich“, lett. (inns „Affe, Possen-
reiBer,  wunderliche Erscheinung"? [oder Lw. aus gr. agtjuogl]), das als
„emporgeschossen“ zu *er~, *or- (prior usw. vgl. formell oopsvog), nicht
                                                                    —
                                                              ;


als „festgefiigt, rnassiv" zu *ar- „fiigen“ gehort.       Koch fraglicher ist
Wood’s Mod. langu. notes 21, 39 auf ai. ar-p-ayati gestiitzte Anreihung von
anord. arfr „Ochs“, ags. icrfe, orf „Yieh, Hornvieh" („unters Joch ge-
fiigtes"??; lit. arbonas (?) „Ochs“              =
                                    anord .arfnni, das idg. bh erwiese, konnte
freilich germ. Lehnwort sein), s. u. orbho-.
   Aksl. jantm „Joeh“ (z. B. Miklosich EWb. 100, Berneker 31        wie sloven.  ;


jermen „Jochriemen, Riemen“ mit Anlautdehnung nach Pedersen KZ. 3S,
311   —318, wo auch iiber die trotz Reichelt KZ. 46, 319 vielleicht auf
*ar(d)men- zuriickfiihrbaren aksl. rcment , serb. remen usw. „Riemen“, die
also ebensowenig wie germ. *ermana s. o., als Zeugen fur vereinzelten
e-Yokalismus der Wz. or- „fugen“ gelten konnen.
   Yon der set-Basis (wie oben si. *ar(d)men-) auch:
  ai.  Irmd-h „Arm, Yorderbug" (ursprgl. „Achselgelenk“, vgl. ag&gov, lat.
artus) = av. aroma- „Arm‘ osset. arm „hohle Hand", dlm-drin drm-drin
                                        .
                                                                                     ,

„Ellenbogen“, apr. irmo „Arm“, lit. 'irmidc („ArmfraB“, d. i. :) ,,Gicht in
den Gelenken", irm-liga „Gicht“ (s. Trautmann Apr. 347), hochstufig lit.
zem. pi. tant. anna „Yorderarm am Wagen" (ibd.), aksl. ramo, ram e, serb.
ri'une „Schulter“. got. arms, ahd. usw. arm „Arm“, arm. armabn „Ellen-

bogen“ (Hubschmann Arm. Stud. I 21), lat. annus „der oberste Teil des
Oberarms, Schulterblatt, bei Tieren der Yorderbug" (lctzteres aus *ar(o)mos
oder * a romos herleitbar).
   Aber lat. ramus „Ast, Zweig“ ist trotz Hirt Abl. 76 (und Charpentier Gl. 6,
192) viel eher zu radix, als unter einer Basis *ara- „armformige Astgabelung"
zu diesen Worten fiir Arm zu stellen, unter welcher Meringer IF. 17, 121
dann auch die Sippe von a rare anschlieBen wollte, indem der Stamm mit
einem Aste das Knieholz abgab, das man zum Pfluge brauchte. Noth
luftiger ist die Annahme, daB *ur- „fugen“ mit *ar- „pflugen“ in der Weise
zu vereinigen sein konne, daB ersteres aus dem Holzbau stamme, wo man
durch Armholzer ein festes Hausgertist gefiigt habe.
  Wzf. *rc-, ro-:
  Lat. reor, rcrl „berechnen, meinen, dafiirhalten" (das primitivste Ziihlen
wird      vom Aufeinanderlegen oder                 -schichten der zu ziihlenden Stiicke
begleitet),      Ptc.       ratus „in       der Meinung", aber auch „berecht. bestimmt,
giltig,rechtskriiftig" (vgl. auch random, rabamini Loewe Prodr. 346. fur
die das it von rahis der Ausgangspunkt war), ratio „Berechnung, Erwii-
gung, Yernunft, Beweggrund, Grund" 1 );
   got. *garapjan (nur ptc.                 yarapana) ziihlen", an. handcart, nhd. Ifimdert
(*rada-     n.   „Zahl“         = lat. ration;   s. Fick III
                                                             4
                                                               336): ahd. yi rad „gerad (nur

   *) Uber lat. ratis „Flo&“ („Gefuge von Stammen“ ? ?) und retae 
=== 0-based leaf 82
           i




74                                                                   ar-



von Zahlen)**, nlid. gerad (nur von durch 2 teilbaren Zablen; verschieden
von gerad = geradeaus) mit neuem Ablaut anord. ti-rpdr eigentlicb ,.naeh
Zebnern gezahlt" (Fick III 4 336); got. rapjo „Zahl, Recbnung, Rechen-
schaft**, as. retina „Rechenschaft“, ahd. redea „Rechenschaft, Rede und
Antwort, Rede, Erzahlung**, afries. birethia .,anklagen“, as. rcthion ahd.                                       ,


red{i)T>n „reden“ (die genaue Gbereinstimmung von rapjo mit lat. ratio be-
stimmt z. B. Kluge 8 s. v. Rede zur Annabme von Entlebnung des germ.
Wortes unter EinfluB von gar apian richtiger scheint mir Falk-Torp 886
                                                                     :



rapjo als primare -ipn -Ableitung, vgl. garunjo „t)bersch\vemmung“, sakjo
„Streit“ Brugmann Grdr. II 2 1, 317 von der germ. Wz. *rap- { garapjan )
zu bestimmen, die von den idg. Nominalbildungen               *r$-ti- ihren
Ausgangspunkt genommen liatte, with rend lat. rat- id direkt aus *ro-ti-
weitergebildet ist    Brugmann aaO. 313, 319 lieB auch rapjo in letzterer
                                           ;


Weise erwachsen sein).
   Ob hierlier auch anord. rod „Reihe, bes. dem Strande entlang ziehende
Erhohung**, mnd. rat f. „Reihe“? (Fick III 4 337; „Reihe“ als „aneinander
gefiigtes, geschichtetes“?).
  Ahd. rumen „nach etwas trachten, streben, zielen“, as. rdmon „streben“,
mhd. mnd. ram „Ziel“ (s. Yf. LEWb. 2 649, Falk-Torp 871) -will van Wijk
IF. 28, 132 f. zu Wz. *rem-
                          „(ruhen) sieh aufstutzen“ stellen (vgl. z. Bed.
lat.   nitor )             doch
                   „stemrnen“ als KraftauBerung nicht der Bedeutungs-
                                           ist

kern dieser Wz. und kann rumen als „geistig zurechtlegen, berechnen“
unserem *rC- zugehoren, wenn auch dabei das (erst jiinger belegte) Subst.
ram als Bildung mit Formans -mo- der Ausgangspunkt gewesen sein muB.
     fZ/i-Erweiterung *re-dh-, ro-dh- (vgl. Persson Wzerw. 46, Brugmann Grdr.
II 1 1047.                          Ygl.    von nr- oben av. arodra-, ferner gr. dodoov, ag&fiog                         ,

wenn letztere nicht gr. Aeuschopfungen mit dem fertigen Suffixkonglutinat
-{too-, -Pfio- sind. ebenso aoi&uog; aber ai. rdliati rdhyati, rdhnoti rnnddlii     ,                       ,


„gedeiht, gelingt, macht gelingen, bringt zustande“, Desid. Irtsati ardlmka-                            ,


„gedeihend   av. arodaiti oroduiti ,,laBt gedeihen, fordert**, die Brugmann
                           -
                               *,
                                                         ,


tfoyvg wegen der zu ru-dh- stimmenden Bed. aus *ar-dh- deutet, gehoren
zu gr. aWoyai, at- „wacksen“; ferner unten got. garaips usw.);
     ai.       radJnidti, rddhyati                       „macht (passend) zurecht, bringt zustande; gerat,
gelingt, hat Gluck womit; befriedigt,                                gewinnt jemanden**, rudhayati „bringt
                                                 1
zustande, befriedigt*    radha-h ni., rfidhah n. „Segen, Gelingen, Wohltat,
                                                     ,


Gabe, Freigebigkeit'*, av. radaiti ,.macht bereit“, m. Dativ vurai ,.jemands
YYi lien erfiillen, zu Willen sein“, rada- m. „Fursorger“, radah- n. „Sich-
bereitstellen,                       Bereitwilligkeit         (in   religioser Hinsicht**,   ap.   rildi
=== 0-based leaf 83
                                                   ar-                                               75

verschiedenen Wz. radii- „sprecken“ nach Fick III 4 347. Falk-Torp 886,
sondern setzen wie si. raditi ein kaus.-iter. *rodheio fort); got. garedan
                                                         11
„worauf bedacht sein, Yorsorge treffen       urredan „urteilen, bestimmen“
                                                              ,


(ygl. zur Bed. bes. lat. rerl), undredan „besorgen, gewahren", ahd. redan
„raten, beratschlagen, worauf sinnen, anstiften, deuten (Riitsel, auffordern,
wofiir sorgen, verschaffen", as. radan, anord. rada ags. radan (letzteres    ,


aucb „lesen“, engl. read ), Subst. ahd. rat m. „vorhandene Mittel, Rat,
Ratschlag, Uberlegung, EntschluB, Absicht, Yorsorge, Yorrat“, ahnlich as.
rad anord. rad,
   ,
                      ags. reed.

  Wzf.   (a)rei-, ( a)rl (s. Persson Wzerw. 102, 162, 232, Beitr. 741):

  gr. agagiaxm   (wenn nicht Neubildung, 8. o.), doi&juog „Zahl“, vggnog „un-
gezahlt", arkad. bidoaog (Schulze BPhYV. 1890, 1406! „lmkexxog, aus-
erlesen“, doiud’Qu doiioQn Hes.; lat. ritus, -us „hergebrachte Art der Reli-
                       •



gionsiibung, Gebrauch, Sitte, Gewohnheit, Art“ (Fick I 4 528, Meringer IF.
17,124; nicht wahrscheinlicher nach Vanicek LEWb. 2 235, Osthoff MU.
4, 109f. zu *rei- „flieBen)“, rite „in passender Art, nach dem rechten reli-
giosen Gebrauch" (formell von Brugmann Grdr. II 2 2, 710 als Lok. eines
neben rl-tu-s liegenden kons. St. *rl-t aufgefaBt, von andern als Lok. *rl-
       des f«-St., s. z. B. Meringer aaO.j; air. rim „Zahl“, a ram i*ad-rJ-ma)
ds., dorimu „zahle“, cymr. rhif „Zahl“, anord. rim n. „Rechnung, Berech-
nung“, as. unran „Unzahl‘‘, ags. rim n. „Zakl“, ahd. rim m. „Reihe, Reihen-
folge, Zahl" (die Bed. „Yers, Reim" von anord. und mhd. rim wohl nach
Kluge 10 s. v. Reim aus frz. rime, das aus rytlirnus lierzuleiten ist: kaum
das frz. Wort umgekehrt aus dem Ahd., vgl. Persson Beitr. 741, Meyer-
Lubke RomEWb. 549 und die Bed. „Yers“ auch von gr. dgi&/.<6g).
  Yielleicht    ist   auch   *rci-         „Sache“ (lat. res usw.) nach Wood a 1 226 an-
zureihen als Wznomen der Bed. „aufgestapeltes                              Hab und Gut“.
  Dazu nach Wood             ax
                       227, Persson Beitr. S56f. wahrscheinlich                            als       dh-
Erweiterung (vgl. oben *re-dh- neben rc-):
   got. garaips „angeordnet, bestimmt", raidjan, garaidjan „verordnen, be-
                                                                  i£
stimmen", anord. g-reidr „bereit, leicht, klar       greida „auseinander\vickeln,
                                                                       ,

ordnen, zurechtlegen, zustandebringen, entrichten, zahlen          mhd. reiten „zu-
                                                                                 1

                                                                                     ,

riisten, bereiten, zahlen, reehnen, berechnen, bezahlen", rcite, gcreite, be-
reite, ahd. bireiti „bereit“, antreiti „series, ordo‘‘, lett. riedu, rizl „ordnen“,
raids „bereit, fertig", ridi ridas „Geriit, Kram‘‘ (der bisherigen Ankniip-
                                     ,


fung der germ. Worte an *reidh- „fahren, sich bewegen", dt. reiten so                            ,

daB z. B. bereit eigentlich „fahrbereit“ ware, fugen sich wenigstens nicht
alle Bedeutungen, wahrend bereit andrerseits
```


## [2026-09-04T23:05:49.349Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT arta\"; grep -n \"Artaxšaça\\|artācā\\|arta-\\|Artabānu\\|rādiy\" KNT.txt | head -30"
}
```


### [2026-09-04T23:05:49.406Z] TOOL RESULT

```
=== KNT arta
934:$66. PIE у AND | fell together in pAr. in the sound у, which remained unchanged in Skt., and so apparently in OP, though its written rep- resentation is by т° preceded by a or by an g-inherent consonant: thus A"r:^m*, normalized karlam, is Кат, Skt. kytém; ar*t"-, normalized arta-, is rla-, Skt. ті4-. For details, see $29- $35.
1153:possibly in Asa-garta- (see Lex. s.v.). Cf. also aec. asmdnam ‘sky’, Av. asman- ‘sky, stone’,
1689:‚ү. Final m of the prior element was of course not written before an initial eonsonant of the second part: ha™-gmatd, ha"-karta-, ha"-dugà, but ham-aranam. ha™-taxSatavy, but ham-atax Sala.
1792:Ш. Forming ethnics: Akaufac-iya- to * Akau- faka-; Aéur-iya- to Aéurd-; Armin-iya- to Ar- mina-; Asagart-iya- to Asagarta-; U(v)j-iya- to 0(0)ја-; Uvürazmiya-; Küfiya- to Küša-; Ga"dara-ya- (possibly error for -riya-) to Ga"dara-; Gatagu-iya- (error for -uviya- or -udaya- or -udiya- ?) to 8alagu-; Pulü-ya-; Bäbiruv-tya-; Mac-iya- to Maka-; Spard-iya- to Sparda-; Haxámanis- iya-; Harawati-ya-; Hi"du-ya (error for Hi"duv- iya- ?).
1793:IV. Other formations, ineluding some personal names: agr-iya- to agra- (5148.1), батшап-їуа-, daran-ija-, brazman-iya-, mart-iya- to marta-, haš- iya- to hat- (8240), ha-mic-iya- to mitra-; Artavard- iya-, Ka"büj-iya-, Bard-iya-, M ardun-tya-.
1902:asa-bdra- ‘borne by horses’; uša-bart- ‘borne by camels’; [dasta]karta- ‘done by hand’.
1914:b. Genitive: Arta-xéaga- ‘Having a kingdom of justice’; Aršāma- (from *aría-ama-) ‘Having the might of a hero’; Haxd-manis- ‘Having the mind of a friend’; Garma-pada- ‘(Month) having the place of heat’; Asa-garta- (Тапа) having caves of stone’. :
2608:$238. THe INFINITIVE occurs in OP only in the present active, with the suffix -tanazy, the ancestor of the NPers, infinitive ending -tän or -ddn: carta- naiy ‘to do’, to kar-; ka*tanaty ‘to dig’, to kan-, cf. NPers. kdndén; bartanaiy ‘to bear’, to bar-; тїраї {апаш ‘to engrave’, to nt-paid-. The c- of cartanaty is evidence for the -e- ablaut-grade in this formation ($98); NPers. kárdün ‘to do’ has k- gen- eralized from the rest of the paradigm.-In form,
2620:I. The participial suffix -lo- is accented, and the Ж verbal root is therefore regularly in the zero grade: $ thus para-ità, Skt. itd-, to ay- ‘go’; [phištā ni-pitta-, $ Skt. pistd-, to pai- ‘adorn’; sinuta- to zšnav-; a- $ тфай, Skt. kgala-, to zšan-; ava-jata, Skt. hatd-,to 4 jan-, karta-, Skt. kytd-, to kar-; u-barta- pard- 4 ратат, Skt. bhriá-, to bar-; maria-, Skt. mytd-, to Г | mar-; aría-, Skt. rtd-, to ar-; perhaps parta[m] to `
2640:pIE *ghrebh- ‘seize’: pAr. grbhi-la- (on -2-, §217), Skt. grbhiid-, OP a-garbila. Here belong, probably, also garta- їп Asagarta
2642:(see Lex. s.v.), mata- in Gaumáta (hardly the same as müla- in dmáld, above); marta- as base for martiya- (see Lex. s.v.).
2723:dám . . . artācā. Apparently two locutions have 24 been contaminated: ‘Ahuramazda along with
2948:(a) as direct object of verbs meaning ‘order’, ‘dare’, ‘be able’: niyastiyam . . . katanaty DZe 9 “Т ordered to dig’; niyaStayam . . . при Чопату XV 23f ‘I ordered to inscribe’, ef. the restorations in DSn 1 and DSf 19f (subject of passive framátam); kaSciy пату adar šnauš сї$єїү dastanary DB 1.53f ‘no one dared say anything’; utädiš atàvayam barta- айу DNb 46f ‘and I had the strength to develop them’.
3076:IV. The postpositions are upariy ($269; only once postposed, as separate word); рата, only in ava-parā; rādiy, in avahya-rddiy and separately; patiy, as enclitic postposition, as separate post- position, and also as preposition; -à, as formative of the locative case; kacã once (DB 1.50), separ- ately, governing a preceding enclitic. Position in the clause varies.
3133:Агатай... Dāraywaušahyā X Shyà puça Daraya- vaušahyā Artaxsagahya XShyà puça Artaxšaçahyű XSayarcahya XShyà puça Xšayäreahyä Dāraya- vaušahyā XŠhyā puça D{éralyavausahya Vš- láspahya puça Haxamán?siya! In this the first phrase of parentage is grammatically correct; in the second, the gen. DarayavauSahyd is repeated аз a basis for clarity, and the appositive puça is in the nom. (see above), with proper depending
3856:62 5 :х$йуайуа : avahyarādiy : Auramazdà : upastàm : арага : uta : ani
4917:! a- neg. prefix before consonants (867, 67.1, 0182.1; an- antevocalie, q.v.): Av. Skt. a-, Gk. a~, Lt. ?n-, Сте. un-, pIE *n-. See akarta-, ax áaina-, axsata-, Anümaka-, ayaumani-.
4940:akarta- adj. ‘not made, not built, unrepaired’; neg. a- + pte. of kar- ‘make’. {akarta] nsf. DSe 47 (conj. of Kent, JAOS 54.43).
5041:Skt. r-, Lt. oritur ‘rises’; pres. inchoative (897), OP rasa-, NPers. räsäë, Skt. rechdti, pIE *rske- (and *re-ske-, $32). See also arta-, hamarana-. arasam \st sg. imf. (§212) DB 1.54; 2.28, 48, 63.
5060:arta- sb. ‘Law, Justice’, an archangel attend- ing Ahuramazda: pte. to ar- as sb., Av. aša- and arata-, Skt. rid- ‘cosmic order’, Lt. ortus -‘risen, originated’, pIE *rto- ($30, $66, 5242.1). See also Artaxsaca-, arlavan-, Artavardiya-. ^ arid-cà isn. (8252.1, Lg. 21.223-9) XPh 41, 50f, 531 (not with Hartmann, OLZ 40.145-60; nor with Nyberg, Rel. 367, 478; Bailey ap. Nyberg, Rel. 478; Henning, TPS 1944.108; hardly, with Sen 155, artäcã braz- maniy apn. ‘and the divine fulfillments’; nor with Pisani, Riv. Stud. Or. 19.85-8, as elliptic dual ‘Arta and Brazman’, the -cé connecting with the preceding Auramazdém, and Brazman being the OP for the Av. vohü man ‘Good Thought’).
5064:Атах$аса- sb. ‘Artaxerxes’ (Т, son of Xerxes; П, son of Darius II; III, son of Artaxerxes II): Elam. ir-tak-Sa-a8-Sa, Akk; ar-tak-Sat-su, Gk. ’Aprakeptns (§29.n2, 530). From arta- ‘justice’ + т$аса- ‘kingdom’, ‘Having a kingdom of justice’ (hardly, with Nyberg, Rel. 352, ‘whose zšaça- de- rives from aría-); imitation of Xšayāršā, acc. -üm, explains the long vowel of the ultima in the nom. and acc. ($78, §161.[b; decl, §172, $187). Artazšaçã nsm. А:Ра 9°, 17°; АЧ; D'Sb 3°; A’Sa 1; A’5b; A*8c 1°; А4 1, 2; А? На 1; A*Hb; Ае 7, 156; A*Pa 5 (as acc., 52476), 8, 12 (as gen., $313.IT), 13 (as gen.), 14f (as gen.), 15f (as gen.), 21, 231; AVsb-d. — Ardaxcasca ($49; or -Sda) AVsa. Arlax áagüm asm. АІРА 51°; А%8а 4; A?He 5; S£ 2-4. ArtaxSacahyé gsm. D'Sb 2°; Artaxíafrahyà (Tm. Lex. 54) A?Ha 2f, 3; Arlazíagühya ($53) A’Sa 2 bis; A?He 101, (аз nom., 5313.1) 11.
5065:ariàvan- adj. ‘righteous, blessed’, denoting the blissful state of the true religionists after death: identical with Av. asavan- ‘characterized by Arta or Asha, righteous’, Skt. rldvan- ‘true to sacred Jaw’ (cf. Hz. Ар! 289-93); from *ria-, OP arta-, with lengthened final vowel, + ad]. suffix -van- ($30, $155.IV). атара nsm. (8124.5, $187) XPh 48, 55.
5066:Artavardiya- sb. ‘Artavardiya’, one of Darius’s generals: Flam. ?r-du-mar-ti-ja, АКК. ar- ta-mar-2i-ja. From arta- + vard- ‘to work’ + adj. suffix ($80, §31, §144.1V, S160.Ia): ‘Doer of Jus- tice’ (not from vard- ‘to increase’, Skt. vardh-, be- cause of -z- in АКК. and in Aram. "rívrzy, аз Bv. BSLP 31.2.66-7 shows). Artavardiya пет. DB 3.30f, 33. Artavardiyam asm. DB 3.36, 43.
5112:asa- sb. ‘horse’ (590, $143.IIT): Med. aspa-, Av. aspa-, Skt. déva-, Lt. equos, pIE *ekyos. See also Asagarta-, asabüra-, aspa-. asam asm. (col- lective, $255) DB 1.87.
5113:Asagarta- sb. ‘Sagartia’, a northwestern prov- ince of the Persian Empire (§29.n2, $81): Elam. ad]. a&-Sa-kar-tt-a, Akk. adj. sa-ga-ar-ta-a-a, Gk. Yayapria. Probably asan- ‘stone’ (with Med. s < pIE Ё; $9.1, 587) + *garta- ‘cave’ (Skt. gdria-), ‘Land of Stone-Cave Dwellers’ ($161.10, §166.1; Bthl. AiW 207, zAiW 119-20); hardly asa- ‘horse’ (with OP s < plE ky, §90) + *garta- ‘wagon’ (Skt. gária-), ‘Land of Horse-drawn Wagons’. See also Asagartiya-. Asagartansm. DPe 15. Asagartam asm. DB 4.23. Asagartaty lsm. DB 2.80f; 4.22; DBg 8f.
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5191:ubarta- adj. ‘well-borne, lifted, esteemed’: u- well’ + barta- ‘borne’, pte. to bar- ‘bear’, pIE *su-bhrio- (830, $122, §242.1). ubartam asm. DB 1.21f;4.66.  ubartàm asf. DB 4.88. On meaning, cf. Altheim, ZII 3.33-5: hardly as taken by König, RulD 69.
5252:karonaoitt, Skt. kr-, pres. krndti karóti (809, $122, $132.2, 5182.3). See also akarta-, ucára-, kara-, dastakarta-, duskarta-, hakarta-.
5366:garta- sb., either ‘cave’ or ‘wagon’, see Asa- garla-.
5537:dasta- sb. ‘hand’: Av. zasta-, N Pers. 0051, Skt. hdsta-, pIE *ghosto- (§88, $116, $145). See also dastakarta-. даѕіауа ism. DR 4.35. dastaibiya idm. (§189) DNb 41.
```


## [2026-09-04T23:05:50.975Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT rad\"; grep -n \"rād-\\|rāδ\\|rādaiti\\|rāta-\" BRT.txt | head -20; echo \"=== BRT arəta\"; grep -n \"arəta\\|aṣ̌a\\|ašavan\\|arədra\" BRT.txt | head -20"
}
```


### [2026-09-04T23:05:51.057Z] TOOL RESULT

```
=== BRT rad
=== BRT arəta
```


## [2026-09-04T23:05:55.486Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c BRT.txt && head -50 BRT.txt && echo \"...\" && grep -n -i \"ratu\\|asavan\\|arta\" BRT.txt | head -10"
}
```


### [2026-09-04T23:05:55.540Z] TOOL RESULT

```
4803500 BRT.txt
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
+  Make  non-commercial  use  ofthefiles  We  designed  Google  Book  Search  for  use  by  individuals,  and  we  request  that  you  use  these  files  for personal,  non-commercial  purposes.
+  Refrain  fivm  automated  querying  Do  not  send  automated  queries  of  any  sort  to  Google's  System:  If  you  are  conducting  research  on  machinc translation,  optical  character  recognition  or  other  areas  where  access  to  a  laige  amount  of  text  is  helpful,  please  contact  us.  We  encouragc  the use  of  public  domain  materials  for  these  purposes  and  may  be  able  to  help.
+  Maintain  attributionTht  GoogXt  "watermark"  you  see  on  each  flle  is essential  for  informingpcoplcabout  this  projcct  and  hclping  them  lind additional  materials  through  Google  Book  Search.  Please  do  not  remove  it.
+  Keep  it  legal  Whatever  your  use,  remember  that  you  are  lesponsible  for  ensuring  that  what  you  are  doing  is  legal.  Do  not  assume  that  just because  we  believe  a  book  is  in  the  public  domain  for  users  in  the  United  States,  that  the  work  is  also  in  the  public  domain  for  users  in  other countries.  Whether  a  book  is  still  in  Copyright  varies  from  country  to  country,  and  we  can'l  offer  guidance  on  whether  any  speciflc  use  of any  speciflc  book  is  allowed.  Please  do  not  assume  that  a  book's  appearance  in  Google  Book  Search  mcans  it  can  bc  used  in  any  manner anywhere  in  the  world.  Copyright  infringement  liabili^  can  be  quite  severe.
Äbout  Google  Book  Search
Google's  mission  is  to  organizc  the  world's  Information  and  to  make  it  univcrsally  accessible  and  uscful.   Google  Book  Search  hclps  rcadcrs discover  the  world's  books  while  hclping  authors  and  publishers  rcach  ncw  audicnccs.  You  can  search  through  the  füll  icxi  of  ihis  book  on  the  web
at|http: //books.  google  .com/l
db,Google
db,Google
db,Google
db,Google
db,Google
db,Google
db,Google
db,Google
ALTIRANISCHES  WÖRTERBUCH
CHRISTIAN  BARTHOLOMAE
STRASSBURG
VERLAG   VON   KARL   J.   TRÜBNER
1904
db,Google
PK
db,Google
Vorwort.
Mein  Altiranisches  Wörterbuch  (AirWb.)  erhebt  den  Anspruch,  eine leidUch  vollständige  und  eimgermassen  wissenschatüiche  Zusammenstellung  des altiianischen  Sprachstoffs  zu  sein,  soweit  er  in  den  bis  jetzt  bekannten  Denk- mälern der  awestischen  und  altpersischen  Sprache  enthalten  ist
Für  die  altpersischen  Keilinschriften  habe  ich  die  Ausgabe  von  FHWeissbach und  WBang  zu  Grunde  gelegt  die  sich  in  Band  X,  Lieferung  i  der  'Assyrischen Bibliothek'  findet  Die  zweite  Lieferung  mit  Kommentar,  Wörterbuch  usw.,  die nach  der  Versprechung  auf  dem  Umschlag  der  ersten  schon  1894  fertig  sein  sollte, ist  bisher  nicht  erschienen.
In  der  Bezeichnung  der  Inschriften  habe  ich  aus  praktischen  Gründen  meine eigenen  Wege  gehen  müssen;  sie  waien  von  dem  Bestreben  bestimmt,  möglichst kurz  und  doch  deutlich  zu  sein.  Für  die  Inschriften  von  Bahistän  habe  ich  darum die  herkömmliche  Bezeichnung  durch  Bh.  belassen;  alle  übrigen  dagegen  —  mit Ausnahme  der  Siegelsteine  von  Privatpersonen,  auf  die  ich  mit  S.  /,  2  usw.  verweise —  bezeichne  ich  mit  dem  Namenssigel  ihres  Urhebers  —  K.  ^  Kyros,  D,  =  Darius, X.  -=  Xenes,  Am.  ■=  Artaxences  Mnemon,  Ao.  — '  Artaxences  Ochus  ■=—  und,  sofern er  mehr  als  eine  hinterlassen  hat,  einer  beigesetzten  Nummer,  wobei  mir  die  Reihen- folge bei  W.-B.  massgebend  war,  nur  dass  ich  zwischen  NRa  =  D,  6"  und  NRc  = D.  J  ein  D.  7  eingeschoben  habe,  das  die  bei  W.-B,  fehlende  zweite  Inschrift  von Xaki  i  üustam  meint  Praktische  Gründe  waren  es  auch,  die  mich  veranlasst habgn,  alle  Verweise  statt  wie  bisher  üblich  nach  Zeilen  vielmehr  nach  Abschnitten (Paragraphen)  zu  geben,  und  zwax  für  die  fünf  Inschriften  von  Bahistän  mit  je gesonderter  —  nicht  durchlaufender  —  Numerirung.  Ich  biete  im  folgenden  eine Cbersfcht  über  die  verschiedenen  Arten  der  Bezeichnung  (und  Anführung)  bei  W.-B., Spiegix  und  bei  mir.
Sp.  W.-B.  AirWb.
M  Kyr.  Murgh.  K.
Bh-Xi-19  Bh.L    1-19  I
n.  I— 16  n.  20—35
HL  1—14  in.  36-49  3. 1
IV.  1-19  lV.50-68
V.  1-6  V.69-74
172C09
db,Google
VI
SP.
W.-B.
AirWb
...
37:In  der  Bezeichnung  der  Inschriften  habe  ich  aus  praktischen  Gründen  meine eigenen  Wege  gehen  müssen;  sie  waien  von  dem  Bestreben  bestimmt,  möglichst kurz  und  doch  deutlich  zu  sein.  Für  die  Inschriften  von  Bahistän  habe  ich  darum die  herkömmliche  Bezeichnung  durch  Bh.  belassen;  alle  übrigen  dagegen  —  mit Ausnahme  der  Siegelsteine  von  Privatpersonen,  auf  die  ich  mit  S.  /,  2  usw.  verweise —  bezeichne  ich  mit  dem  Namenssigel  ihres  Urhebers  —  K.  ^  Kyros,  D,  =  Darius, X.  -=  Xenes,  Am.  ■=  Artaxences  Mnemon,  Ao.  — '  Artaxences  Ochus  ■=—  und,  sofern er  mehr  als  eine  hinterlassen  hat,  einer  beigesetzten  Nummer,  wobei  mir  die  Reihen- folge bei  W.-B.  massgebend  war,  nur  dass  ich  zwischen  NRa  =  D,  6"  und  NRc  = D.  J  ein  D.  7  eingeschoben  habe,  das  die  bei  W.-B,  fehlende  zweite  Inschrift  von Xaki  i  üustam  meint  Praktische  Gründe  waren  es  auch,  die  mich  veranlasst habgn,  alle  Verweise  statt  wie  bisher  üblich  nach  Zeilen  vielmehr  nach  Abschnitten (Paragraphen)  zu  geben,  und  zwax  für  die  fünf  Inschriften  von  Bahistän  mit  je gesonderter  —  nicht  durchlaufender  —  Numerirung.  Ich  biete  im  folgenden  eine Cbersfcht  über  die  verschiedenen  Arten  der  Bezeichnung  (und  Anführung)  bei  W.-B., Spiegix  und  bei  mir.
2064:ABKÜRZUNGEN. I.    In  den  Litteraturnachweisen  und  Stellenangaben.
2067:(nxwA     Bombay  188$. ABajiAW.:  AbhuKÜungen  der  k.  Bayemchen  Akademie  dei  Wiiiens chatten.     I.  Klasse. AfR. :  Archiv  für  Religionswissenschaft.     Herausgegeben  von  ThAcHEUS  u.  A.     Leipzig. AJPh.:  American  Journal  of  Philology. An.-.  Artaxeixes  Mnemonf-Inschrift);  s.  S.  v.
2068:AnaL  Graec.:  Anatecta  GraeciensJa.    Festschrift  zum  43.  Pbilologentag  in  Wien.    Graz  1893. Abj.:  {Atai  Nyäyiht  =1  Niran^  t  Atai;  s.  S.  IX.  9. Ao.:  Artaxcrxes  Ochu('Iascbrir(J ;   s.  S.  v, Aog. :  An^imadaecä ;  s.  S.  ix.  4.
2089:Dk. ;  Deitiarl.     Zilirl  nach  den  Übersetzungen  von  EWWest  in  SBE.  j^,  4^. DkB,;  Z?m^iw(-Bombay.     The  pinkarij  ..  by  PeshotunBSuhjana.    Bombay  1874^. DkB.131:  Zitat  des  Zten^arl-^omh^y;  s.  S.  ix.   10  i. DL.i  Deutsche  Ljteraturseitnng.    Leipzig. DST.:  JDabmestetek.
2122:(PH'Kufes  Perser:  Die  Perser  des  Äschylos.    Erlangen  1877. KI-:  Literaturblatt  für  orientalische  Philologie.     Herausgegeben  von  EKuilN.     Leipzig.
2129:Bild,  der  Nom.:  Die  Bildung  der  Nomina  im  Litauischen.     Leipzig  1S91. (ESJ)Lsu»lANN  EtWb. :  Etymologisches  Sanskrit- Wörterbuch.  Strassburg.  [Unvollendet;  S.  1-112.] LGÄRPh.:  Ijteraturblatt  für  germanische  und  romanische  Philologie.    Leipzig. (E)LlDtM  Stud.:  Studien  zur  attindischen  und  vergleichenden  Sprachgeschichte.    Upsala  1S97.
2151:Leipiig. PBrB. :  Beiträge  lur  Geschichte  der  Deutschen  Sprache  und  Litteratur.    Herausgeg.  von  HFaul
2185:V.  ..  PüZ.:  Zitat  der  PahlariüberseUung  (Pü.)  »um  Yasn. Y. ..  SöZ.:  Zitat  der  Sanskritübersetsung  (Sä.)  tum  Yasn. YL:  Yait;  %.  S.  vm.    1, ZDA:  Zeitschrift  für  Deutsches  Altertum  undDentscheLitteratur.  Herausgegeben  von  ESCHROEDES
2308:Litt.:  Litteratur.
```


## [2026-09-04T23:06:02.594Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"vahiSta\" \"vahista\" \"vahišta\" \"asavan\" \"aSavan\" \"ratu-\" \"arSta\" \"rädaiti\" \"radaiti\"; do echo \"--- $p\"; grep -c \"$p\" BRT.txt; done"
}
```


### [2026-09-04T23:06:04.598Z] TOOL RESULT

```
Exit code 1
--- vahiSta
4
--- vahista
52
--- vahišta
0
--- asavan
44
--- aSavan
4
--- ratu-
36
--- arSta
24
--- rädaiti
0
--- radaiti
0
```


## [2026-09-04T23:06:07.175Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"asa-vahista\\|asa  vahista\\|vahista-\\|asavan\" BRT.txt | head -20"
}
```


### [2026-09-04T23:06:07.223Z] TOOL RESULT

```
2711:übergeben  und  im  Mondlicht  geliutert.  Darauf  — yes'    isfai'   [yezt)  nöit    tsia"'  (3SPrM.) gingen    aus    ihm    die   vielen  Arien   von  Tieren  |  bäV   asavanam    *aimllil  ästäratti   t^.to^; hervor,  vgl.  /.ruru^ar.ia-.    S.  noch  SEE.  ^7-33- ,  —haiiyöJvalsä(sd.)  kyat  «V>'.l(iSPM.)'> Pu.;  tvai  Jäi.  ^        \dr»goäitS  ai  alaong  ra/»nS  hySm  Y.Jj.S;
3151:•  j.  a-x§yamna-,  a-xsyamana-  Adj.  'ohn- mächtig': xlayammm  asavan^m  däyata *tnn>m'^  drvantfm  Y. Ä5;  —  ydi^a  Alm janama  xiayamnö  *'in»qm'>'>Y.6i.5;  — frJnamjtti  .  .   atfrv    maitiyus    "manö    Yt.
3899:•  j.  'aiwi-srüSrima-  m,  Gottheit  der vierten  der  fünf  (priesterlichen)  Tages- abteilungen'*, beigenannt  aib:.gaya-  (sd.): 'm^m  aibi.gaim  asavan^m  aSake  ratüm  Y. 2.6;  G..^.5;    —    'mäi  aibi^ayilt  Y. /.  6;
4376:•  j.  an-aSavan-  Adj.  'nicht  rechtgläubig, ungläubig,  glaubensfeindlich' :  vTsße  asraosö yS  'Sai'anö  (NP.)  vlspe  'iavanS  yS  tanu,- p>r?%B  \.  16.18;  —  zao/a  'sava  adahmd atanu.mO^rd  Yi.  yo.  138.  a)  sonst  von as^maaya-  (sd,  auch  fdSt.):  "sava,  -saonS (GS-),  'saonqm.        [N.  lOg:  lies  asavanim^
4799:ajasa  andvl . .  Yt5.8s;  —  fiiirim  .. yS  aßcCiraiibyS  ätti  raoxinuha  lazfmnS "..der  mit  den..  (Sternen)  im  Lichtglanz dahergefahren  kommt"  Yt.  Ä45.  7)  mit Akk,  des  Ziels:  ä  mJ  aidäm""^  vahiltä  a ^^at^yacJ  (sd.)  mazdil  Y.j^,  7;  —  at  vä vTsp7ng  ayti'"^  "so  komme  ich  zu  euch allen"  Y.  j/.  2.  a)  in  feindlichem  Sinn, a)  vom  Feindesheer:  späopm  . .  dOräi ayanttm  rasmaoyS  . .  daniayasnanqm  Yt. 5. 68.  p)  'sich  machen  an  — ,  hermachen über  — '*J':  pairikqm  yä  aiti  airim  äpm sqm  .  ,  V.  //.  9.  b)  in  freundlichem, a)  'zur  Seite  treten,  stehen':  at yastsm nsit  na  issmrUS  Syät'*^  (Opt)  "wer  dem aber,  wenn  er  (drum)  angegangen  wird, nicht  zur  Seite  steht"  Y.  46. 6.  ß)  'auf Jemands  Seite  treten,  übei^ehen  zu  — ' (Akk,):  _v7  ayat  (Konj.)  asavanim  divam- wm  (sd.)  ..  Y.j/.  20.  ßß)   mit  Abi.
5901:•  j.  asnya-  Adj.  'auf  den  Tag  bezüglich': °yehe  pascaSa  anyehe  ra'^ivü  "im  nächst- folgenden Tagesabschnitt"  V.  7.4,  A)  m. Name  der  Gottheiten  der  fünf  Tagesab- teilungen**  und  derentsprechendenGebete: •ya  asavana  asake  ratavS  Y.  2.3;  17;  — 'yaeibyS  aiahe  ratubyS  Y.  /.  3 ;  —  ra'iivqm ayaranqmca  'yanqmca  Y.  r.  17.
6073:—  yS  möi  'säi  haülm  (sd.)  hatä  var9saiti\hnii  'sähe  yat  vahistahe  (näml.  ratavö) Y.  46.  19;  —  spinia  mainyB  vahiiiäcä  \  mazds.frasästa  .  .  Y.  7. 10;  usw.  0)  GS. manatjhä  'säl  haiä  lyaohanäcä  valaahälä  ,  mit  gai'^ä-  (sd-,  auch  fdSt)'*:  'sähe  gatia ahmäi  dqit  .  .  mazda  "für  den  heiligen  |  Y.  ^.  3 ;  usw.  e)  AbL  mit  haca  dnw. Geist  und  für  das  nach  dem  göttlichen!  2  a  ß,  mit  vahista-,  yazatoHbyB  . .  y5i Recht  beste  Denken,  Handeln  und  Reden  I  h^nii  yasnyäca  vahmyäca  'sül  haca  yat wird  uns   -"  Y,  47.  i.         b)  im  jAw.:  1  vahiltät  Y,  1. 19;  77.  10,  V.  j.  2,  Yt  8. 15,
6301:KoiDpA.,  E.  —  Vgl.  aJävairi-,  —  ai.  vgt flavan-  Adj.  —  Pü.:  ahrav"'};  SB.!  fa^yälmä, muklälmä,  muklimin-,  £.  noch  No.  ^.  —  ■)  Mit ä  nnr  in  aiävaoyö  DP.  (Vt  J.  4t  'S-  88)  und im  VS.  aiJ««  (SJOJ.7);  s-  noch  <üäv^r: ■>  Die  Hds.  schwanken  zwischen  aiaen' aiäjiH'.  Die  Gründe  für  die  Wahl  der  Lesung in  der  NA.  sind  mir  öfters  nicht  erkennbar. Im  Y.  habe  ich  mich  meist  nach  Pt4  gerichtet, iB.  gegen  NA,:  Y.ja.  11,  33.  1,  43-0,  IS  uö. S.  übrigem  auch  S  ^68.  33.  —  J>  Im  Gegen- satz in  dip/.arila:  —  4)  Die  attrib.  Bestim- mang  eines  Nomens  durch  asavan-  und  aiaii rata.--  m.  iat  ungemein  häufig.  Dabei  erscheint hinler  femininem  und  neutralem  Nomen mehrere  Male  die  mask.  Form  von  aiavan-, in  Anschlns»  an  das  folgende  ralav-:  V.  7/. 12',  Vr.  /.  5,  G.  4-  8;  V.  7/.  23,  Vr.  /.  4, 2.  6;  s.  Ho.  5.  —  i>  Mask-,  weil  auf  ta%-a'qni belogen,  1.  N0.4.  —  *)  Hds.  airaiaf';  s.  aber Pa.  —  J)  Als  Vok.i  aber  Pü.:  ahräilA.  — O  Vgl.  u/ajraoUr-*}.  Pü.  hat  den  Flur.  — 91  Streri,  —  '•')  Gleichklang  der  Auslaute!  — ">  Die  Verwendung  von  alavanä  als  N-APn. {\'r.  7.  4,  7p.  I,  Vr.  S.  33)  kann  durch  den Zniammenfall  des  NPm.,  APni.  und  APn.  bei der  d-DeklinatioD  hervorgerufen  sein;  s.  Vt. 8. 33.  —  '")  Das  ein  allir.  *arla^an-  voraas- seilt,  *gl.  Hbu.  FSt.  195.  Dagegen  führt mp.  artäk,  ahrät^fÜ)  (mit  ä  aus  äud)  itii'artäffan- ; iD  i-äl  i  artäk  des  Gl.,  worauf  JirSTI  NB.  33 Terweist,  s.  valahe  aSaenä  unter  I  Z.
6307:KompA.  —  Ableit.  aus  aiievanl-,  ei g. 'Zustand des  asavant-'.  —  Pü.!  ahraulk  (zu  Y.  11  erl. ; epeeailh),  akräklk.  —  ')  Pü.j  a  hua:fih  u ahravlh  'lur  Seligkeit  und  Gerechtheit'. SOLMSEMS  Adj.  ajavasla  (Stud.  83)  steht  auf sehr  schwachen  Füssen.
6375:•  j.asavan-:  j.,  g.aM««-;  s.  unter  ajai'an-.i     .      t  w    —    t^     ■  j  , ,  t.„
6391:Y.p,  18;  —  sonst  mit  anasavan-  verbunden yri  aahal  mairyl  drvh  biiangrS  avaia •yö  anasava  V.5. 3S;p-52,  56,  21.J,  Y.Ö5. 8,  Yl_5.  7,  10,  14';  —  "y^m  anasavansm "kumliarjstUim  V.4.49i  Yt/J.  51;  — paiti  'yake  anasaonS*ahU.m>r?ni5  k^krpi
6572:mg  tisit  ärshät  {3S0PfA)*'  spä  pasi haurvB  vä  . .  "wenn  mir  nicht  der  Schäfer- hund da  wäre  oder . ."  V.  /  9.  49 ;  —  s.  noch Inf.  Sil.  —  PPA.  und  PPfA.:  asavanmi Apntpmat  bavaiitimca  (sd.)  büryanttmca Vr.  i8.  2,   Y.  27.  4;   —    vUpqm  .  .    stim
7306:•  j.  I-fyei5yäi  Inf.  'Sorge  zu  tragen  fiir  -, zu  helfen,  zu  unterstützen';  asavan^m  ts asao/ial  a/y  mraomi  urra'^ym  urva^ilt "justum  tibi  a  justo  curandum  declaro amicum  ab  amico"  Y.  7/,  13'^
7751:•  g.  «rasya-  Adj.  'recht  handelnd,  ge- recht''*: aäiä  vS  Uta  hyamil  ..  asavanJ -yl  (NP.)  istsm  rsitx  (sd.)  y.^0.4.
9048:•  j.  kaoba-  m,  Name  eines  Lands*':  upa dvarnn  xsairö.sukjm  (sd.)  apanöJtmjm 'hitva  *birizantaya  asavanaya  "bei  dem Pass  -Vj^,  dem  liöchstgelegenen  in  dem hochragenden  heiligen  K."  Yt5.  54.
10286:•  j.  yaäay-  f.  Name  einer  Dasin:  nasam janat . .  'ii  Janai  Yt  4. 2 ;  —  bujat  naram asavan^m  haca  ttasäm  . .  Aa&i  'si  Yl.  4.3.
11915:j  machen  (Jmdn.  sva.  es  Jmdm.)':  täpayäii mqm  asa  vahista  mqnayfn  ahe  ya%a nyaoxivst)m  Hx.1-.2q.  a)  absolut  'Wärme bringen,  schaffen',  von  Sonne  und  Mond: yai  hvara  raoxlne  täpayatt  \t6.i\  i,  7.4.
12847:(Akk.)  festhalten,  es  beobachten,  nicht davon  abgehen':  \datant  tyJ'  mans  atti^ *adariy''^  "das  Gesetz,  das  meine,  es  wurde gehalten"  D.  6'.  3 ;  —  Ayat  aksyü  (sd.)  ults yS  ahm  dadrl  Y._5J.8;  —  nanm  asavan^m dalrän^m^^  Aumahm^a  maus  .  .  Vr.  2. 5.  a)  fest  im  Gedächtnis  behalten, immer  daran  denken':  siaeta  yemya  .  . dadräna^*  paid/äna  Y.55.6; — yal  dim (nämt,  ahutum  vairTm)  .  .  aakus  .  .  asa- xtai  (sd.)  *sa^qs  dadrän5'°'^  ..  Y.  sg. 10.  3)    'darauf   halten,    dass  — ',    mit
13073:—  yäiia  kaiaca  'tnS  staota  yesnya  haurva *da'iäiti  .  .  aia  ratufris  N.J7;  —  nSit kl  *''mö''  aiiavahjm  (sd.)  Vaya/  P-56";  — "mö  asava  P.j2;~ya'ia  'maiäj  asaoneY. /^.  35;~/ar<i  kaAmaiat asavanasca  V,  7,  7i(?);  — asavaium  V.2.15; —  'tnakeca  nars  asaottö
13122:j.  'dahyu'ma-,  "dähymna-'*  Adj.  'der I  Provinz,  dem  Land  an-,  zugehörig,  Land-': kaya  ratavS?  nmänyS  vlsyU  zantumS  'mB zardhuärö ptixlöY-ig-iB.  A)  m.Name der  Gottheit  der  Länder*':  "mtm/a  aia- vamm  asahe  ratam  G.3. 7 ;  —  'mähe  ra%wS 0.3.7;  —  uzayeirin^m  .  ,  frädaLvirtm 'trmnca  asavanim  Y.  2,  5;  —  laayeirinai .  .  ß-ädat.vTrai  'mäica  asaone  Y,  /.  5 ;  — ähurBiS  °mahe  Vr.  1. 9.
```


## [2026-09-04T23:06:15.035Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6296,6302p' BRT.txt | cut -c1-2000"
}
```


### [2026-09-04T23:06:15.086Z] TOOL RESULT

```
"aäavE^
354
steht,  dem  das  Paradies  sicher  ist';  im jAwf.:  yaia  i>aH  (sd.)  a^äum  *a<ia  atiAs 'sota  . .  z'ahiäa/u  atihSus  °sava  jasB  Y. j/,i6;  —  jvasHt  nöit  dval  °sava  miSascit fwii  ^axsaitHsd.)  vahistahe  ataksu^"^^  lang er  lebt,  erwirbt  er  sich  das  Anrecht  nicht, ood  - ,"  V,5,6ii — /si!mä{sä.)  asil 'fava ■nrüraja  vaktäd  \.s8.i,^
Uodeutlich:  Y.  77.2,  G.  2.6  {amisS spfnt5 'saonqm).  [P.  2^:    lies  aiüw»  st  'iava;
—  N.  75:  lies  asaya  st  °saom;  —  Y.  //. V.7.52PliZ.:  lies  hati:mt.al':^
KoiDpA.,  E.  —  Vgl.  aJävairi-,  —  ai.  vgt flavan-  Adj.  —  Pü.:  ahrav"'};  SB.!  fa^yälmä, muklälmä,  muklimin-,  £.  noch  No.  ^.  —  ■)  Mit ä  nnr  in  aiävaoyö  DP.  (Vt  J.  4t  'S-  88)  und im  VS.  aiJ««  (SJOJ.7);  s-  noch  <üäv^r: ■>  Die  Hds.  schwanken  zwischen  aiaen' aiäjiH'.  Die  Gründe  für  die  Wahl  der  Lesung in  der  NA.  sind  mir  öfters  nicht  erkennbar. Im  Y.  habe  ich  mich  meist  nach  Pt4  gerichtet, iB.  gegen  NA,:  Y.ja.  11,  33.  1,  43-0,  IS  uö. S.  übrigem  auch  S  ^68.  33.  —  J>  Im  Gegen- satz in  dip/.arila:  —  4)  Die  attrib.  Bestim- mang  eines  Nomens  durch  asavan-  und  aiaii rata.--  m.  iat  ungemein  häufig.  Dabei  erscheint hinler  femininem  und  neutralem  Nomen mehrere  Male  die  mask.  Form  von  aiavan-, in  Anschlns»  an  das  folgende  ralav-:  V.  7/. 12',  Vr.  /.  5,  G.  4-  8;  V.  7/.  23,  Vr.  /.  4, 2.  6;  s.  Ho.  5.  —  i>  Mask-,  weil  auf  ta%-a'qni belogen,  1.  N0.4.  —  *)  Hds.  airaiaf';  s.  aber Pa.  —  J)  Als  Vok.i  aber  Pü.:  ahräilA.  — O  Vgl.  u/ajraoUr-*}.  Pü.  hat  den  Flur.  — 91  Streri,  —  '•')  Gleichklang  der  Auslaute!  — ">  Die  Verwendung  von  alavanä  als  N-APn. {\'r.  7.  4,  7p.  I,  Vr.  S.  33)  kann  durch  den Zniammenfall  des  NPm.,  APni.  und  APn.  bei der  d-DeklinatioD  hervorgerufen  sein;  s.  Vt. 8. 33.  —  '")  Das  ein  allir.  *arla^an-  voraas- seilt,  *gl.  Hbu.  FSt.  195.  Dagegen  führt mp.  artäk,  ahrät^fÜ)  (mit  ä  aus  äud)  itii'artäffan- ; iD  i-äl  i  artäk  des  Gl.,  worauf  JirSTI  NB.  33 Terweist,  s.  valahe  aSaenä  unter  I  Z.
•  j.  *asa'vaat-'*  Adj.  i)  'rechtschaffen' (nur  Ableit).  i)  'der  das  (höchste) Anrecht  a)  besitzt':  haurvafsavS  .  .  drvä Maurva  -vantö  (NP.)  Y.jÄiS.  b)  'ver- schafft':  hadiiasca  (sd.)   'vaiS  vOstravatS
```


## [2026-09-04T23:06:15.985Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rt.w\" SOD.txt | head -30; echo \"=== righteous\"; grep -n -i \"righteous\" SOD.txt | head -20"
}
```


### [2026-09-04T23:06:16.060Z] TOOL RESULT

```
4141:northward  across  the  Oxus.  One  might  assume  that 
12793:819  'krt'wcy    B  ju^"  j>ju /un- 
16105:(o)fratamu   Cprtmw)   ©adv. 
16118:1293  ^rtmw  =*  'prtm'wh,  'prtm- 
17371:1483  'rt'w    B,  M,  C  ajujf  ***/ y  <Jfji*y,  <^> 
17372:artaw   ©MP  ahlaw;  Parth.  Vrf'w;  OP  artawan; 
17382:1484  »rt'w  frwrtyy    M  '^jJ)JjYJ<j^  jr-*± 
17385:artaw-frawarti 
17391:1485  'rt'wsp'y   B,  S  ^U<flx  jf^jV^Ujl 
17404:artawaspya   Ort'wspy'kh,  'rtwspyO 
17409:1488  'rt'wspy'kh   S  =>  Wwspy'h 
17415:artawoxst,  artuxst,  artawoxust  (Wxwst,  Wwxst 
17416:rwc)  ©*artaw9xust;  <*rtahe  wahistahe  ©inst. 
17417:*artaxwdst   ^'rtxwst,  Jrtyw  rwc,  'rtywst  rwc 
17434:artawya    ^rtwy* 
17442:artawyak    ^rt'wy'Ch) 
17447:artawyamenc 
17454:artaw  zrusc 
17460:1495  Yt'xwst  =>  >rt>wxwst  rwc 
17465:<*rtivahvi   -^'rt'wxwst  rwc 
17471:artxwost,  artxust    ©*artwahist   ^Wwxwst  rwc 
17481:MDii,  >rtkw;  MDiii  p30,  }rtw 
17492:artaw   ^rt'w 
17498:1502  Ytwsp'y    B  =>  'rt'wsp^ 
17500:1503  Ytwspy*    M  =»  >rt,wspy,h 
17504:arawya   ^rt'wy'Oi) 
17510:artxwost,  artxust   Ortxwwst)  ©*rta  vahista-, 
17512:>*artavahist>*artxw9st   ^rtywst  rwc, 
17522:1506  Ytxwwst  =*>  'rtxwst 
17542:artcwan    ^'rSp'n 
=== righteous
17375:faithful,  clcctus,  righteous 
17395:righteous 
17405:righteousness,  Manicheaism,  electi 
17436:righteousness,  state  of  electus 
17443:community  of  clccti,  righteousness 
17449:righteousness 
17456:righteous  Zoroaster 
17506:righteousness 
50524:righteous,  honest,  humble 
50529:righteousness,  good  reputation 
74712:righteous  wind 
93167:righteous     1483,  1485,  6362 
93168:righteousness     1487,  1491,  1492, 
93171:righteous  wind     9873 
93172:righteous  Zoroaster     1494
```


## [2026-09-04T23:06:24.076Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i,l in enumerate(leaves):\n    if \"1483\" in l and \"rt'w\" in l:\n        print('leaf',i,'-> printed approx',i-66)\n        print(l[:2500])\n        break\nEOF"
}
```


### [2026-09-04T23:06:27.522Z] TOOL RESULT

```
leaf 123 -> printed approx 57
  'rp'st'wyh                                                                                                             58


       wealthy, precious, powerful                                     flour
       Karab. Insc. 21.21, -w 16.7; MDii apud. S W, SI                C2, 94 V 21
         cahier 7, 1989, 184                                     1480 >rtJ =* »srwc(yy)

 1465 Yp'st'wyh        S                                 ^3J     1481 Yt'kCw) => >rtk
      arpastawe                                                  1482 'rt't rwc M, S
      wealth                                                                            (W^j^jj^'^"^^                    Jjj
                                                                      artat roc ©<haruvatdt
       Hen. Talcs. 486.12
                                                                       sixth day of the month
 1466 Yp\vy        B                     (^^rj^o)^^                    GMS 86 n 1; Hen. Oricntalia. 8, 94; Magi. 149.10;
       arpux Orp'wx, >rpwx, }rpwy)                                       MDiii
       penetrating, profit
                                                                 1483 'rt'w    B, M, C          ajujf ***/ y <Jfji*y, <^>
       BSTBL, Dhu. 74; Bcnv. Notesii 214; Mack.
                                                                      artaw    ©MP    ahlaw; Parth. Vrf'w; OP artawan;
            BSTBL n p49; Hen. LW     102; S W, BSOAS
                                                                         Av.asavan ©pi. ~t-y ob. pL -ty =>}rtw
            1975, 133, }rp+-wxt < axu                                  faithful, clcctus, righteous
 1467 }rp}wx =* 'rp'wy                                                GMS 91, 1076; TSP; Tales. 469.4, 476; Frag. Lcn.;
 1468 Ypst>k => Yp'st'k                                                 STi 45.14; Sund. AoF 1981 p2l3; C2, 39V6,
                                                                        54R19; BBB; MSP
 1469 Vpsty       C, S                                   \+jf
       arpastc ©pi. -t ^'rp'st'k                                 1484 »rt'w frwrtyy     M         '^jJ)JjYJ<j^      jr-*±
       precious
                                                                                warti
       STii 18,3.41, 5.13; MSP b80                                    artaw-fra
                                                                      first clement
 1470 Ypwy =» *rp*wy
 1471 Ypwx => 'rp'wy
```


## [2026-09-04T23:06:37.248Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ahlaw\"; grep -n \"ahlaw\\|ahlay\\|Ardwahi\\|ardwahi\\|ahrav\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB\"; grep -n \"ahlaw\\|ahlav\\|artav\\|Ardwahi\\|ardvahi\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-04T23:06:37.338Z] TOOL RESULT

```
=== PHD ahlaw
PHD.txt:184:аһа PAPy | (M ~hr’y)] righteous (of Sros). ahlaw Phlwb! | M ?hlw] righteous.
PHD.txt:185:~ih: righteousness. ahlaw-dād Phlwb d”t'] alms, charity. ahlayih [kl dyh] righteousness. AN 7 ШЕ, * Md ahlomby [hlmwk' | M ?hImug] heretic. 3
PHD.txt:191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
PHD.txt:214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
PHD.txt:221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
PHD.txt:306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
PHD.txt:599:u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATWNPn!',*wl?mt?n") astr. ascendant. *ul-drafš, v. xurdrus. ummēd Pwmyt! | N ~] hope. ~war [-w?/ | N ~] hopeful. Urdwahišt Pertwhst'] = Ardwahist. Urišlīm Pwlyštym | N ~] Jerusalem. urmód Pwlmwt! | (N amród)] pear. *uruspar Pwlwspl = Av. uru0Bar-] intestines, womb; core, essence. urwahm(an) [wig hm(n') | M ?wrw’hm-] joyful. ~ЛЬ : joy, pleasure, delight. urwar Pwlwl | M ?wrwr] plant(s), vegetable.
PHD.txt:771:alms ahlawdad.
PHD.txt:1205:charity ahlawdād.
PHD.txt:3029:Pahlavi pahlawig.
PHD.txt:3044:Parthian pahlawig.
PHD.txt:3448:righteous аһа, ahlaw, ardā, ašē, frārēn. righteousness  ahlawīh,  ahlāyīh,
PHD.txt:4384:Amahraspandan Wahman Ardwahišt (Urd-, Ašwahišt) Šahrewar Spandarmad Hordād Amurdād
PHD.txt:4388:I Frawardin II Ardwahišt III Hordad IV Tir V Amurdad VI Sahrewar
PHD.txt:4760:1 3pahréxtan pahrez l-pahréz- pahlawig pahlüg pahlom pahlomih paygālgar pahast lpüy-
PHD_mackenzie.txt:941:               ahlawehlwb' I M )hhv] righteous.
PHD_mackenzie.txt:943:                ahlaw-did ehlwb d)t l ] alms, charity.
PHD_mackenzie.txt:1023:  e.g. an i ahlawiin ruwan = ruwiin i ahlawan, the souls of the
PHD_mackenzie.txt:1171:Ardwahist prtwhlt l I M 'rdywhy!t, (N urdibihift)] Right, the second
=== NYB
18:The second volume of my Manual of Pahlavi appears at quite a long interval: ten years after the first. The main reason has been the extraordinary amount of fundamental linguistic problems presenting themselves within almost every word, each requiring lengthy and painstaking research. My advanced age has also somewhat impaired my efficiency. -
20:Throughout the text— wherever it has been possible—I have confronted the Book Pahlavi words with their equivalents in Manichean West Iranian, Old Iranian (Avestan, which must in absence of other sources stand for Old Iranian in general) and Old Persian. They have been measured against other West Iranian languages and dialects down to New Persian; last but not least against the Middle Iranian loanwords in Armenian and Aramaic. Etymologies are given only within this framework; other Indo-European languages have been only occasionally quoted.
21:My linguistic analysis has been greatly aided by ihe new and revolutionary insight into the character of Middle Iranian bestowed by the Turfan texts. Thanks to them we have an incomparably firmer grasp of Book Pahlavi than was ever possible before. This glossary is therefore closely linked to the epoch-making research done by the generation of W. B. Henning, H. W. Bailey, E. Benveniste, H. H. Schaeder and others.
24:It goes without saying that I have taken advantage of the useful Special vocabularies composed by Kapadia (Vendidad) and by Dhabhar (Yasna- Visperad), beside his very solid and reliable investigations on Book Pahlavi, and of the special glossaries produced during the new phase of Iranology heralded by the Turfan texts.
38:The Aramaic ideograms used in this Manual are listed here, together with a pre- liminary analysis of the Aramaic lexical material from which they derive. From an Aramaic point of view, most of the forms in which the verbal ideograms appear in Book Pahlavi (as well as in the inscriptions and in the Psalter) are spurious, fabricated as they are by Iranian-speaking scribes and hence without any linguistic foundation. In fact, only impf. forms of the type YKTLWN = YIQT'LUN and some few other forms can claim to be genuine Aramaic. The intricate process by which the Iranian scribes transformed Aramaic forms into purely graphic signs will be dealt with in my new edition of the Frahang i Pahlavik. Here such ideographical forms as have totally fallen out of the Aramaic verbal system will be explained merely by reference to the closest corresponding Aramaic forms or simply to the triconsonantal root, from which the 3d p. sg. perf. can be easily seen, e. g. NKS, pf. N'KAS (NB: — roots as BNY, HZY have the perf. B'NA, HAZA; HDY has HADI).
282:ahlav
300:ahlav ['hlwb'] 1. holy, of the gods 5912;
304:ahlav
305:subst. the pious, righteous man 651%, 732.24; pl. cas. obl. ~-dn: ~-dn marian zanān 53%; ~-dn alone 634, 7322, 8835, 10121, — 3. blessed, of those in Paradise 8624; subst. pl. cas. obl. ~-dn the blessed 87%, — Borrowed from Av. (246 sqq.) ašāvan-, nom. ašavā; MPrthPrs (Zoro- astrian term) ’hlw, pl. ’hlw’n (A-H II); as to the correspondence -š-: -hl- v.s.v. Mahlāh; Paz. ašē, pl. ašēg. V. ahlav-dät, ahlài, ahlayéh. The genuine WIr form is OP artdvan ‘blessed’, whence MPrth ?rd^w ‘righteous, veracious’, also borrowed in MPrs (A-H II); v. further artäk.
306:ahlav-dat [~-d’t'] a th. given to fulfil righteousness or piety; charity 9214-15, — Paz. ašūdād, Skr. v. puņyadāna. In mod- ern Parsism ‘the fees to the priests’, Modi, Ceremonies 407, 441-442.
307:ahlài Phl’y] = ahlav, v.s.v. Sroš. — SW development of *ahläv < Av. nom. sg. *ašāvā of ašāvant-, v.s.v. ahlav and cf artäk.
315:ahramög [hlmwk'] heretic, apostate 1074, — Borrowed from Av. (257) ašomaoya-; Paz. āšmēg. As to -š-: -hr- ef s.v. Mahlah and ahlav. .
320:Ahrišvang ['hlyšwng] a female deity 5915. — Phl. transliteration of Av. (243) Ašiš vanuhi; on -hr- : -&- v.s.v. Mahlah and cf s.v. ahlav.
380:639. 742. (after hämöden). 8922, 919. 992.5; — the agent of a pret. pass. 3822, 3919.21; — dir. obj. of an inf. 857-11, of a trans. pret. pass. (mixed act. and pass. construc- tion) 7621, 772; — governed by a prep. 1222, 3918, 43? ete.; — for the cas. rect. pl., be- ing the subj. of a vb. in pres. 104%. — Av. (145 sq.) amasa- sponta-; Paz. amešāspand (or similar forms), Skr. v. transliterates, or translates amara-guru; MPrs ’mhrspnd’n ‘the elements of Light’; as to -š-: -hr- v.s.v. ahlav; Av. amoša- < *a-mrta-.
646:artži [’lt’y], artäk [*lt*k] righteous 2214, 239. 249. 128%; vāt 1 ~ the good wind (wind sent by the Righteous Powers) 717.23 Plek]. — artāi < *artāv < OP artävä, the nom. sg. of artävan-, is the genuine Prs form of the w. which appears in the religious language as ahlav (q. v.); final -v > -y is the common rule in SW. — artak is only a secondary spelling of artāi; Ps. also ’U’dy = artäi. MPrs abstr. Pyy (S) = Ps. "'lP?dyhy, v. Sogd 504 (and 31). — Artäk Virdz n. pr.: v. Viraz.
655:Art-vahišt [?rtwhšt'] 402; Urt-vahiSt Pwrtwhst'] 39%,  A&a-vahist [?šwhšt'] 394-5, 401-4, 589. 593, 9727 one of the Amahraspands (g.v.). — art, urt < OlrSkr rta- ‘the right cosmic order, the divine law’, Av. (192) arata-, (349) orota-, (229 sqq.) aša- + vahista- (v. vahišt) 'the best, the heavenly law'. Asa-vahist is directly borrowed from Av. (233 sgg.); also the name of the 2nd month of the year and the 3d day of the month; MPrs ’rdywh<yst> Sogd. 2771; NP ardi- (urdi-)bihišt. Cf ahlav, ahläi, artči; Arta-xšahr "he whose dominion is (de- termined) by the divine law’.
748:ašok Pšwk] = ahlav, g. v.; pl. cas. obl. ~-dn 1061. — A learned w., taken over as a religious term from Av. ašava, nom. of ašavan-, v. s. v. ahlav.
2282:ken andar). — 8. as a kind of izäfat, mostly introducing an apposition: hán mart ... ke ahlav Zartuxšt 4919-17, 4317-18, adak-iš čišan guft ke dätär Ohurmazd 58°; han vartēnišn ... ke fraškart-kartārēh i veh 9921-22.25—26. without an antecedent: bavēt . ke Spitāmān Zartuxšt it may be S. Z. 6023; 597: an. imitation of the Av. idioms azom yö ahurö mazdå; hanjamanam fra- barata yo dadvd ahurö mazda ete.; — seldom introducing a gen.: han x¥arrah ke ... Eran dēhān ké-c ahlav Zartuxst
2386:2. with -s- for -hr-: Misē; msyd msy’ny DkM 59314-15; with -rs- for -hr- : mrsy’ny (Tanbih, l.c., var. of Cod. L). — C. In Khwarizm mrd — mrd?nh (Birüni, l.e.); MPrs mwrdy’ng (A-H I, p. 220). Cf Chri- stensen, Le premier homme I, p. 9-10. The forms reconstructed and used by him: * Masyay — *Masyānay, are nowhere to be found, and fictitious. The forms Khwar. Mard ("Man") and MPrs fem. Murdiyänag are clearly WIr, and so are also Mihreh < NW *Midriya- and Misēh < SW "miciya-. The other forms are typical EIr, and betray the difficulty WlIranians felt in rendering the sound developed in EIr from -rt-, -r0-, -0r-, which must have been something like an unvoiced -r- or -l-, and which they analyzed as -hr-, -hl-, -rh-, -lh- or simply identified with their -§-. Cf the spellings of pahlom (g. v.); Av. agavan-, BP ahlav < artavan-; Av. ašsmaoya-, BP ^hlmwk: ahlamög, but KZK 1. 13 'iswmwky (in the parallel text SM 1. 20 ’himwky); hence the inverse spelling pwlsy for puhl ‘bridge’ (q. v.), SM 1. 43 (Arab mrsy’ny, v. above, is a mechanical rendering of a written BP form *mlsy’ny = mihriyäne). Consequent- ly, mahlé malhé māšē are Elr develop- ments of *martiya-; miše EIr develop- ment of *mißriya-, ci Sogd mys < midra. We have to do with two forms of different origin: 1. *martiya-, 2. *mi@riya-; as to this problem, cf Sven Hartman, Gayo- mart (1953), 45-64.
2401:pret. pass.: ~ en dam dāt 10312313 (on 3%: ~ kart AWH-wm v. s. v. k- and -m); — my: a) izdfat + ~: kanicak i ~ 7!; b) placed before its headw.: cif i ~ fradandčin the conditions of my children 559; Hamāk i ~ duxt 261; ē (lo) ~ pit u € ~ brat 10018; c) definite rel. attr.: ēt i ~ zan 3215; õi 4 ~ mart i ahlav 3914-15, Ot i ~ pus 5118-19; elliptically: han i ~ my house (family) 3717-18; én i ~ my religious duty 535; — after prepositions: apük, apar, hac, 6, pat ~; ~ rād. — 2. the form normally used as the cas. rect. ‘I’: man Šāhpuhr hom 1514; ~ dānēm 21? etc. — 98° STHn-yt' (imp.) L: if an imp. has
```


## [2026-09-04T23:07:07.472Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Ard \\|^Ard\\[\\|Ard \\[\\|arti-\\|Ašiš\\|asis vanuhi\" NYB_vol2_glossary.txt | head -20; echo \"=== nard\"; grep -n -i \"nard\\|new-ardaxs\\|Ardaxšahr\\|Ardavan\\|Artabanu\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-04T23:07:07.576Z] TOOL RESULT

```
320:Ahrišvang ['hlyšwng] a female deity 5915. — Phl. transliteration of Av. (243) Ašiš vanuhi; on -hr- : -&- v.s.v. Mahlah and cf s.v. ahlav.
1557:fravahr [plw’hl] the heavenly and im- mortal counterpart of the earthly beings, their tutelary genius 31? etc. passim; also fravaš (g. v.). — Av. (992 sqq.) fra- vaši- < "fravarti-, cf OP n. pr. Fravarti- = Gr Öpaöprns; MPrs pr’whr ‘ether’
1564:fravartin [plwltyn'; inser. prwrtyn] 1. the name of the first month of the year SPrthPrs: 1; 952°. — 2. the name of the 19th day of the month 30%. — < *fravarti- nam, Av. (994) fravašinam, gen. pl. of fravarti-, v. fravahr.
4101:Dhabhar vētvar, without etymology, in the sense of ‘contented, contentment, forbearance, patient, consoling oneself (‘consoling’ already West), resigned to the will of God’ (~ dätan ‘to console’); Hormazdyar with the same etymology as Bailey, but giving the same senses as Dhabhar (‘one who endures grief, en- during, patient, consoling, persevering’). Both lay stress on the close parallelism with a%ansand (x"arsand), of which it sometimes seems to be a mere synonym. However, the original idea underlying it must be looked for from another angle. I read it, with Dhabhar, vēt-var and derive it from OTr *vaiti-bara- ‘the willow- bringer [Av. (1314) vaéti-, NP bed, ’willow’] originally an epithet of Airyaman, the god of healing, and going back to the myth told in Vd. 22: Ahuramazdah, badly wounded and struck with 99999 maladies by Ahriman on his first on- slaught on the heavenly creation, pro- mised 1000 horses, 1000 camels, 1000 heads of cattle, 1000 sheep and “the beautiful Benediction of the Righteous" (dahma äfriti) to the god who could heal him. All declined except Airyama tišyē *Airyaman the desired(?)": he brought (barat) hair from 9 horse stallions, hair from 9 camel stallions, hair from 9 bulls, hair from 9 rams, and brought 9 willow twigs (nava vačtayo barat) and drew 9 furrows — the Phl v. adds: “and made a nirang (g. v.)”, a magic spell intended ‘to heal the wounds and stop the maladies. Apparently the willow twigs played the chief part in this nirang (of whose parti- culars we know of course nothing), thus it was quite natural to form out of it the epithet *vea$-bara- of Airyaman in his quality of the healing and relieving god. Later, Airyaman having faded away, the usage took a wider range and developed secondary nuances, but the original meaning ‘healing’ is still fairly transpar- ent in many passages, e.g. DD 36? (quoted both by Dhabhar and Hormazd-
4889:fra0-: pursitan Fravarti-: fravahr fravatah: fröt
5021:aša + vahišta-: Artvahišt ašāvan-, ašavā: ahlav ašemaoya-: ahramēg Ašišvaņuhi: Ahrišvang ašta-: aštak
=== nard
2693:dashir"; Talm. nrdšyr, Arab nardasir, Telegdi 249; Goldziher, MSt I, 168, n. 3.
4157:vinäristan [wyn'lstn'], vinärtan [wyn’ltn'] pres.: read vindrénd 106%? for virdyénd, to put in order, to arrange, to array, to organize 13?(-2stan)??(-rtam). 85”. 86% (-rt). — MPrth wyn’r’d, wyn'r- (MHC); MPrs wyn'rdn w(y)n’r-; Paz. vinardan, vinärastan, Bailey, JRAS 1953, 106; Henning, TPhS 1954, 175 n. 1. Pass. v. above
4554:ziyinak [zyd’nk'] (young) woman, of Ardavan’s daughter (even after she had
```


## [2026-09-04T23:07:09.164Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN arastan\"; grep -n -i \"arastan\\|ârâstan\\|piräst\\|pirastan\\|virast\" HRN.txt | head -20; echo \"=== HRN rad\"; grep -n \"^[0-9]*\\..*râd\\|rād \" HRN.txt | head -10"
}
```


### [2026-09-04T23:07:09.245Z] TOOL RESULT

```
=== HRN arastan
4713:(188)), vergl. arm. LW. darastan 'Garten'; ai. därtt-
=== HRN rad
```


## [2026-09-04T23:07:14.453Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2688,2698p' NYB_vol2_glossary.txt | cut -c1-3000"
}
```


### [2026-09-04T23:07:14.544Z] TOOL RESULT

```
Nēvak-gāv [ndwk' TWR?»] n. pr. one of the Ātwiyān (Aspikän) family 47°. névak-gohréh [ndwkgwhlyh] the quality of being of good substance 793.
nevakök [ndwkwk'; NKD?N] beautiful, lovely, nice, pretty 7!9 ete. passim; gl. of NKD?N 57%. — NP niki < nēkē. Cf Benveniste, Modi Vol. 1930, 3. The con- tracted form is surely old.
névakokeh beauty 15?!.
névakokiha nicely 14°.
nčv-artaxščr [ndw'lthšdl] the game of tric-trac 31». 1201-2-15, 1217. — “Brave Ar-
dashir"; Talm. nrdšyr, Arab nardasir, Telegdi 249; Goldziher, MSt I, 168, n. 3.
Nēv-Šāhpuhr  [ndwšhpwhl] 11419, — “Brave Shapur”.
Nishapur
nézak [nyck'] lance, javelin 201° and passim. — Av. (1037) naéza-; MPrth nyzg
(S); Paz. neža; NP mizah; Arab lw. naizak-. nifrin [nplyn'] curse 9717”. — ni + Av.
(1016 sq.) frāy-, opp. dfrin (q. v.); MPrs nfryn (S); Paz. nifrin; NP nafrin.
```


## [2026-09-04T23:07:16.261Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 1500 HRN.txt; echo; echo \"=== search\"; grep -n \"ârâstan\\|ārāstan\\|araj\\|pirajstan\\|piraj\" HRN.txt | head; echo \"=== grep â\"; grep -n \"râd\" HRN.txt | head"
}
```


### [2026-09-04T23:07:16.371Z] TOOL RESULT

```
Google
This is a digital copy of a book that was prcscrvod for gcncrations on library shclvcs bcforc it was carcfully scannod by Google as pari of a projcct
to make the world's books discoverablc online.
It has survived long enough for the Copyright to expire and the book to enter the public domain. A public domain book is one that was never subject
to Copyright or whose legal Copyright term has expired. Whether a book is in the public domain may vary country to country. Public domain books
are our gateways to the past, representing a wealth of history, cultuie and knowledge that's often difficult to discover.
Marks, notations and other maiginalia present in the original volume will appear in this flle - a reminder of this book's long journcy from the
publisher to a library and finally to you.
Usage guidelines
Google is proud to partner with libraries to digitize public domain materials and make them widely accessible. Public domain books belong to the
public and we are merely their custodians. Nevertheless, this work is expensive, so in order to keep providing this resource, we have taken Steps to
prcvcnt abuse by commcrcial parties, including placing technical restrictions on automatcd qucrying.
We also ask that you:
+ Make non-commercial use ofthefiles We designed Google Book Search for use by individuals, and we request that you use these files for
personal, non-commercial purposes.
+ Refrain from automated querying Do not send aulomated queries of any sort to Google's Sy
=== search
400:(in Muhammed Ja'far Qarajadäyl^s Lustspielen, z. B. öfter im
=== grep â
```


## [2026-09-04T23:07:22.919Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN آراستن\"; grep -n \"آراستن\\|پیراستن\\|راد\" HRN.txt | head -20; echo \"== HUB\"; grep -n \"آراستن\\|ârâst\\|arâst\\|rādh\\|rād-\" HUB.txt | head -20"
}
```


### [2026-09-04T23:07:23.000Z] TOOL RESULT

```
== HRN آراستن
== HUB
```


## [2026-09-04T23:07:26.708Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c HRN.txt HUB.txt; echo \"== sample HRN\"; sed -n '380,400p' HRN.txt; echo \"== grep arast variants\"; grep -n -i \"arâs\\|aras[tk]\\|ârâ\" HRN.txt | head -20"
}
```


### [2026-09-04T23:07:26.773Z] TOOL RESULT

```
 688044 HRN.txt
 527491 HUB.txt
1215535 total
== sample HRN
hält den Autor für einen Azerbäijäner) oder auch mit Druck-
fehlem in der Seligmann*schen Ausgabe resp. Schreibfehlern
der Handschrift zu thun haben können".
Aber nicht nur bei den kurzen Vokalen linden sich
bei den Dichtern unreine Reime, sondern auch, wennschon
viel seltener, bei den langen. Da reimt z. B. 'arüs auf
/urös (äähn. 7, 109) und hös (70, 153) oder s^r auf zerir
(110 Anm. Vers 8, Calc), Zerf'r auf tir (1536, 705), Ardes^^
auf hustr (1523, 473). In den letzten drei Fällen nimmt
Nöldeke, Persische Studien II, 2 Anm. 2, allerdings Text-
verderbnisse oder ünechtheit der betreffenden Verse an ; er
äussert jedoch zugleich seinen Zweifel, ob nicht auch die
alten Dichter in seltenen Fällen ö auf ü, e auf t gereimt
haben mögen ^). Ebenso giebt Nöldeke wenig auf die An-
^) Vergl. auch Gulistän (Sprenger J 26 Zeile 8: ptl — bei.
Nur für einen Türken ist es aber begreiflich, wenn Südl, der
bekannte Qäfizkommentator , einen Reim wie rät (das soll röyet *dein
Gesicht' sein!) auf Härüt ^ Märüt für möglich hält fGhazel No. 17).
Dialektisch begegnet zwar auch in der Literatur die Form rüt statt rüyet
V
(in Muhammed Ja'far Qarajadäyl^s Lustspielen, z. B. öfter im
== grep arast variants
1079:aw. araska- 'Neid') ^) ; phlv. arsk^ rask, arSktn, arsklh,
2894:phlv.paras^* Verehrer, parastar,parastakzh, i)arast(i)sn
4713:(188)), vergl. arm. LW. darastan 'Garten'; ai. därtt-
4922:bei. ver^l. druck, dräc, n. drask, darask 'J^aum* (82).
9776:71. Bartholomae's Übersetzung von slw. araska- durch
11114:bild', nzd{i)stparast(i)&nlh 'Götzenanbetung (Men.),
```


## [2026-09-04T23:07:33.464Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"schmücken\\|schmuecken\" HRN.txt | head -20; echo \"=== HUB struct\"; grep -n \"ārā\\|arā\\|rād\" HUB.txt | head -20"
}
```


### [2026-09-04T23:07:33.555Z] TOOL RESULT

```
581:11. är asten 'schmücken', Praes. üLräy-em^ ärayis,
3320:352. pmrästen schmücken, anordnen , Praes. peiray-em.
9103:|X/>e^-, pincdti bedeutet nur 'schmücken'^); phlv.
=== HUB struct
```


## [2026-09-04T23:07:36.128Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '575,595p' HRN.txt; echo \"==== 352 pirastan\"; sed -n '3315,3330p' HRN.txt"
}
```


### [2026-09-04T23:07:36.184Z] TOOL RESULT

```
verschwundenen Verwandten anzuschliessen.
Dazu efröiZiden 'ordnen, das aber ebenfalls unbelegt
ist; heraz 'Schmuck', beräztdeM (No. 193) können wegen
phlv. hräzisak, hräzisakth nicht zu [^räz- gestellt werden,
zu der sie sonst sehr gut passen würden {upa + räz).
äöm s. äyin (No. 61).
11. är asten 'schmücken', Praes. üLräy-em^ ärayis,
ap. l/^räd' in rästa- Vichtig'; aw. [^rad- zurecht
machen', radaiti; phlv. ärästan, äray(i)sn^); ai. [/^rädh-,
rädhati 'zu Stande bringen'.
oss. arazi 'schmückt, kleidet', aräfif geschmückt' (28).
Vergl. Bartholomae, BB. 10, 269. Die falsche, laut-
1) Im ÄYestakommentar stehen immer Formen von ärästan^
vir äst an,
2) Vgl. auch phlv. vlrästav^ viräyOßn ; hamrästcni.5 -
gesetzlich unmögliche Etymologie Spiegel' s (Keil-
inschriften 2, 238, Ar. Periode 284) findet sich noch bei
Bechtel, Hauptprobleme, 163.
12. äräm *Ruhe*, ärarmden, arätnis, nu^'0'nN (jüd.-pers.
Bibelübs. ^).
aw. äramayat *er erfreute'; phlv. aramUan, äräni
==== 352 pirastan
kurd. afy. LW. pTr; hei, ptrük, n. plrük 'Grossvater'
(300).
Vergl. aw. parö^ "^parya- 'früherer 2).
351. pfrär, pirar[sal *das vor vergangene Jahr.
aw. '^para,yär' (+ säl),
352. pmrästen schmücken, anordnen , Praes. peiray-em.
pati+ [/'räd- (s. ärästm No. 11); phlv. peray(i)sn;
arm. LW. patrast,
353. perähen 'Hemd*.
phlv. patrahan *ßock' (Yätkär-T Zarir. 64 Note 53),
perähen (PPGL).
kurd. LW. pirun, perlen 'Hemd'; wa/. parhän, sar.
harhän 'Weiberhemd'.
354. perö^, arab. LW. ß:rüz 'siegreich' ; j^frö^e 'Türkis,
arab. LW. flröze, fairüzaj,
aw. "^paiti.raocah-; iphlv, peröd, peröÖkar, päz. |?eröi.
```


## [2026-09-04T23:07:47.514Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"freigebig\\|edelmütig\" HRN.txt | head -10; echo \"=== ordibehesht\"; grep -n -i \"ardib\\|urdib\\|ardīb\\|behist\\|bihist\" HRN.txt | head -10; echo \"=== HUB head\"; sed -n '1,40p' HUB.txt"
}
```


### [2026-09-04T23:07:47.596Z] TOOL RESULT

```
5391:601. räd 'freigebig.
=== ordibehesht
2518:246. bihiSt^ behist ^Paradies'.
2520:LW. kurd. behist.
2521:Die Aussprache behist ist die ursprüngliche ; in bihist
=== HUB head
Google
This is a digital copy of a book that was preserved for generations on Hbrary shelves before it was carefully scanned by Google as part of a project
to make the world's books discoverable online.
It has survived long enough for the copyright to expire and the book to enter the public domain. A public domain book is one that was never subject
to copyright or whose legal copyright term has expired. Whether a book is in the public domain may vary country to country. Public domain books
are our gateways to the past, representing a wealth of history, culture and knowledge that's often difficult to discover.
Marks, notations and other maiginalia present in the original volume will appear in this file - a reminder of this book's long journey from the
publisher to a library and finally to you.
Usage guidelines
Google is proud to partner with libraries to digitize public domain materials and make them widely accessible. Public domain books belong to the
public and we are merely their custodians. Nevertheless, this work is expensive, so in order to keep providing this resource, we liave taken steps to
prevent abuse by commercial parties, including placing technical restrictions on automated querying.
We also ask that you:
+ Make non-commercial use of the files We designed Google Book Search for use by individuals, and we request that you use these files for
personal, non-commercial purposes.
+ Refrain fivm automated querying Do not send automated queries of any sort to Google's system: If you are conducting research on machine
translation, optical character recognition or other areas where access to a large amount of text is helpful, please contact us. We encourage the
use of public domain materials for these purposes and may be able to help.
+ Maintain attributionTht GoogXt "watermark" you see on each file is essential for informing people about this project and helping them find
additional materials through Google Book Search. Please do not remove it.
+ Keep it legal Whatever your use, remember that you are responsible for ensuring that what you are doing is legal. Do not assume that just
because we believe a book is in the public domain for users in the United States, that the work is also in the public domain for users in other
countries. Whether a book is still in copyright varies from country to country, and we can't offer guidance on whether any specific use of
any specific book is allowed. Please do not assume that a book's appearance in Google Book Search means it can be used in any manner
anywhere in the world. Copyright infringement liabili^ can be quite severe.
About Google Book Search
Google's mission is to organize the world's information and to make it universally accessible and useful. Google Book Search helps readers
discover the world's books while helping authors and publishers reach new audiences. You can search through the full text of this book on the web
at |http : //books . google . com/|V
I fI--
X(
PERSISOHE STUDIEN
VOX
]]. HUBSOHMANN.
STRAHSBUKi.i.
VRKhACi vox KARL J. TRCBNBH.
1895.PERSISCHE STUDIEN
VON
H^HtlBSOHMANN.
STRASSBURG.
```


## [2026-09-04T23:07:50.883Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5388,5400p' HRN.txt; echo \"=== HUB rad/arast\"; grep -n -i \"rät\\|räd\\|arast\" HUB.txt | head -30"
}
```


### [2026-09-04T23:07:50.947Z] TOOL RESULT

```
Shukovski, Neup. Gramm. § 13 b Anm. 1, sowie
die syntaktische Bemerkung bei Rückert, ZDMG.
8, 258, 264.
601. räd 'freigebig.
aw. vergl. aräiti-^); ai. rati- Villig zu geben'; phlv.
rat (auch Titel, vergl. Hörn, Mitteilungen, Heft IV,
27), ratth.
602. räz geheim, verborgen'.
aw. razah' (vd. 8, 97); phlv. raz^ vergl. Qaovav^
Chron. Pasch. I, 730, 14, 15 (de Lagard e, Ges. Abh.
192) ; skr. rdhas- 'Einsamkeit, Geheimniss'.
603. rast recht, wahr, rechts*, 7'äste^ rastl, rästln (Sahn. I,
123 Vers 1070).
=== HUB rad/arast
1309:aiis *paristam (fur parastatn)^ inf. *paristadan (fiir
1310:parastidan). Vgl. estadan und firistadan,
10623:parastidan 39.
```


## [2026-09-04T23:08:06.454Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"RAD\\|\\*rād\\|rāδ\\|RĀD\" CHEUNG.txt | head -20; echo \"=== ar 'fit'\"; grep -n \"ārāy\\|ārāstan\\|ārāst\" CHEUNG.txt | head -20"
}
```


### [2026-09-04T23:08:06.526Z] TOOL RESULT

```
=== ar 'fit'
```


## [2026-09-04T23:08:09.315Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c CHEUNG.txt; grep -n -i \"arastan\\|araya\\|rad-\\|radaiti\" CHEUNG.txt | head -20"
}
```


### [2026-09-04T23:08:09.382Z] TOOL RESULT

```
1769485 CHEUNG.txt
4796:2.75, DB 2.90); Caus.: pres. IND. darayamiy <d-a-r-y-a-mi-i-y> (DB 1.26, DNb 14, AsH 11, etc.), 
4797:<d-a-r-y-a-mi-i-y> (DPh 4), <d-a-r-y-a-mi-i-y> (AmH 5), 3sg. darayatiy <d-a-r-y-t-i-y> (DNd 2), 3pl. 
4798:daraya'tiy <d-a-r-y-t-i-y> (XPh 23), <d-a-r-y-t-i-y> (XPh 24), impf. med. lsg. hamadarayaiy 
6579:*AVESTAN: frad- (fräö-) ‘to increase’ = Liste: 35f. 
8126:*MIDDLE PERSIAN: MMP gry-, BMP gl(y)dy- /griy-/ ‘to weep’ (< OP *grad-ya-) || 
11413:*NEIR: ? Yzgh. raö-/rost, Wa. rad-, roó-/ron- ‘to flee, run away’, Oss. D. randa (in 
13113:pirad-/pirüst ‘to burst, tear [intr.]’, Sh. pirénd-/pirént, Rosh. parend-/parent, Bart. 
13115:*rad- (i.e. *(H)ra(n)d), pace Morgenstierne, EVS\: l.c. Most, if not all, intransitive 
13399:Pst /arast/, BMP "l'stk /arastag/; Inf.: BMP "Tom /arastan/ || (+ *pati-) Pres.: IND. 1р1. MMP pdr’ywm; 
13442:?), NP afraz ‘exalted’ (LW ?) || (+ *а-) NP arastan/aray- ‘to adorn’ || (+ *ui-) Zaz. 
13473:*AVESTAN: YAv. sparaya- (m.) ‘sprout (at the point of an arrow)’ (Yt 10.129) || (+ 
14056:*AVESTAN: varad- (varoó-) ‘to grow, enlarge’ = Liste: 51 
17635:Avestan verb marad-’, on the basis of the Skt. cognate root mardh ‘to neglect, 
21158:*OLD PERSIAN: (+ *aua-) avarad- ‘to leave, abandon’. Ф See most recently R. Schmitt 
21198:added as cognates, Skt. rah, OP rad-, MP rastan [wrongly cited: rastan], NP rastan. 
23210:Caus.: impf. IND. 1sg. niyacarayam <n-i-¢-a-r-y-m> (DB 1.64) 
24814:Caus.: impf. IND. 15р. viyatarayam <vi-i-y-t-r-y-m> (DB 5.24 f.), 1pl. viyatarayamä <vi-i-y-t-r-y-a-m-a> 
28160:*NWIR: (+ *ui- ?) Bal. grast, gradit/grad- (intr.) ‘to cook (in oil or water), be fried’, 
28161:(EHB) grast’, gras6/grad- (orig. caus., tr.) ‘to boil food’. 0 The etymologies 
28163:rad- ‘to prepare oneself’) are unconvincing, as observed by Shahbakhsh: s.v. grad-.
```


## [2026-09-04T23:08:12.042Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13380,13460p' CHEUNG.txt"
}
```


### [2026-09-04T23:08:12.099Z] TOOL RESULT

```
prepare’ (LW), ВМР wyl'dyh- /wirayih-/ (pass.) ‘to be arranged, etc.’ || (+ *ham-) 
MMP hr’s- (pret. stem) ‘to arrange, prepare’. 0 MMP hr’s- with *-mr- > MMP -rr- 
<-r->, also in MMP hrwb- ‘to collect, gather; receive’ (< *ham-raup). Incorrect 
Henning 1933: 187: < *uhrastan < *uzrästanai. || Klingenschmitt (Congress Graz 
2002) compares the WIr. forms wnyr-, etc. to Lat. norma ‘ruler’. It is more 
preferable though to look for a provenance within (Dlr. rather than to rely on an 
obscure and isolated form that is Lat. norma (e.g. no Italic cognates). Perhaps, 
wnyr-, etc. derive from a nasal pres. stem *ui-Hrnza- (cf. Skt. RV rñjá-) > OP 
*vi-Hrnda-, which subsequently shows metathesis and simplification/assimilation of 
the apparently awkward consonant cluster: > win(n)ir- ? > DMMPP: 294a, 290a, 
270b, 277b, 344a, 354b f. 356 

Partic.: pres. caus. MMP r’yn’g ‘leader, guide’, perf. pass., MMP r’st ‘correct, true’, caus. BMP I’dynyt 
/rayénid/; Caus.: pres. IND. 3sg. BMP I’dynyt /rayénéd/, ВМР I’dynnd /rayénénd/, IMPV. 258. MMP 
r’yn-; Inf.: caus. BMP I’dynytn /rayénidan/; Pass.: pres. IND. 3pl. MMP r’yyhynd || (+ *api- ?) Partic.: 
perf. pass. BMP pdl’stk /payrastag/, MMP “pyr’st; Inf.: caus. ВМР pyl’dynytn /payrayenidan/ || (+ *abi-) 
Partic.: perf. pass. MMP *’br’st || (+ *a-) Pres.: IND. 3р1. BMP ’r’dynd /arayénd/; Partic.: perf. pass. BMP 
Pst /arast/, BMP "l'stk /arastag/; Inf.: BMP "Tom /arastan/ || (+ *pati-) Pres.: IND. 1р1. MMP pdr’ywm; 
Partic.: perf. pass. MMP pdr’st || (+ *fra-) Pres.: IND. 1р1. MMP fr’r’zwm, SUBJ. 1р1. MMP pr’r’z’m; 
Partic.: perf. pass. MMP pr’r’st || (+ *ui-) Pres.: IND. 3sg. MMP wnyryd, SUBJ. 1sg. MMP wnyr’n, 35р. 
MMP wnyr’d, etc. Caus.: pres. IND. 1sg. BMP wyl’dym /wirayém/, 3sg. MMP wyr’yd, BMP wyl’dyt 
/wirayéd/, 3pl. BMP wyl’dynd /wirayénd/, etc. || (+ *ham-) Inf.: MMP hr’stn 

*PARTHIAN: r’st ‘true’ || (+ *pati-) pdrz- ‘to rise up’, (caus.) pdr’z- ‘to raise up’, ? 
pdr’y- ‘to prepare, make ready; to achieve’ (< MP ?) || (+ *ui-) wyr’z- ‘to complete, 
arrange’, wyn’r- ‘to put in order, arrange, array’, wyn’r’g ‘arranger’ (< MP) 
= Ghilain: 69 f., 52, 70, 75 | DMMPP: 293a, 270b, 356b, 344a, 354b f. 

(+ *pati-) Pres.: IND. 3sg. pdrzyd, 3pl. pdrzynd; Partic.: perf. pass. pdr’st, caus. H pdr’z’d; Caus.: pres. 
IND. 3sg. pdr’zyd, 3pl. pdr’zynd, SUBJ. 2sg. pdr’z’h || (MP LW ?) Pres.: IND. 3pl. pdr’ynd; Partic.: perf. 
pass. pdr’st, П pdr’y’d || (+ *ui-) Pres.: IND. 35р. “wyr’zyd, 3р1. *wyr’zynd, SUBJ. *wyr’z’, IMPV. 2pl. 
wyr’zyd; Partic.: pres. wyr’z’n, perf. pass. wyr'st; Inf.: *wyr'stn || Pres.: IND. 3pl. wyn’rynd, SUBJ. 2sg. 
wyn’r’h, 3р1. wnyr'nd; Partic.: perf. pass. "wyn’r’d 

*KHOTANESE: Khot. rras- (denomin. ?) ‘to rule’ || (+ *aua-) varas- (varas-) ‘to 
experience’ || (+ *fra-) harays-, (caus.) һагаѕ- ‘to extend’ || (+ *ш-) birays- (biras-) 
‘to extend, spread’ = SGS: 115, 119 f., 149 f., 98 

*SOGDIAN: BSogd. rsth, CSogd. rst’ (f.) ‘truth’ || (+ *uz-) CSogd. zrys(-) ‘raise, lift 
up’ || (+ *pati-) BSogd. ptryz- ‘to rise’, CSogd. ptrz- ‘to become exalted, be proud’, 
(caus.) BSogd. ptr’yz- ‘to raise, erect’ || (+ *fra-) SSogd. Br’s- ‘to conclude a treaty 
(?)’, BSogd. fr’yz-, CSogd. fryZ- ‘to straighten, make straight’ 

(+ *uz-) ’z-Impf.: IND. 35р. CSogd. zrys’z || (+ *pati-) Pres.: SUBJ. 35р. BSogd. ptryz’t, OPT. 35р. 
CSogd. ptrzy; Fut.: IND. 35р. CSogd. ptrztyq’; Caus.: pres. IND. 35р. BSogd. ptr’yzt, POT. 3sg. BSogd. 
ptr’yztwnty || (+ *fra-) Pres.: SUBJ. 35р. BSogd. fr'yz't; Pret.: tr. IND. 35р. SSogd. Br’stw Ai ‘he 
concluded a treaty (?)’; Partic.: perf. pass. CSogd. frst- ‘straight, upright’ 


198 *(H)spar(H)j 


*CHORESMIAN: "rz- (TZ-) ‘to be straight, just, in order; ‘to be extended’, (caus.) r’zy- 
‘to make straight; to demand (justice from)’; to arrange’ || (+ *abi-) m/’brzy- ‘to feel, 
sense, observe’ || (+ *fra-) hr’zy- ‘to grab, stretch out to’, hr’zyk ‘extended (string)’ 
(74.1) || (+ *ui- ог? *aua-) wr’ry- ‘to sweep’ (diff. MacKenzie I: 546) = Samadi: 
177, 2, 168, 91, 216 

*NWIR: Awrom. (awa-)faznay/(war-)fazn- ‘to adorn’ || (+ *api- ?) NP pérastan/péray- 
‘to adorn, decorate, ornament’ || (+ *abi-) NP afraxtan, afrastan/afraz- ‘to raise’ (LW 
?), NP afraz ‘exalted’ (LW ?) || (+ *а-) NP arastan/aray- ‘to adorn’ || (+ *ui-) Zaz. 
virastis/virazen- ‘to prepare, restore, build’, Awrom. wırästay/wıräz- ‘to sew’, Gur. 
(Kand.) -uraz-, (impv.) viraz- ‘to sew, attach’ 

*NEIR: (+ *aua- or *ui-) ? Yi. uriz-/urizd ‘to spread manure’ (Morgenstierne, IFL 
Ile Rather *Hraiz ?) || (+ *а-) Oss. І. arzzyn/araezt, D. ar&zumarzzt ‘to be 
arranged, done’, I. arazyn/areezt, D. arazun/arzzt (caus./tr.) ‘to direct to; to 
construct, build, make; to adorn’, ? Pash. ar(a)t ‘wide, expanded’ || (+ *uz-) Sh. Xáz-/ 
xäzd ‘to darn, mend (shoes, etc.)’, Wa. Saz-/Sazd- ‘to darn’ || (+ *pati-) Sariq. 
padráz-/padrázd, Wa. рыігы2-/роігоға- ‘to lean on, against, support on’ || (+ *ui-) 
Oss. I. ræzyn/ræzt, D. irezun/irezt ‘to grow, gain in length; to be arranged’, Rosh. 
wiréz-/wiroxt, Bart. wiroz-/wiróXt ‘to make, build’ 

*MISC: Par. réz-/rast ‘to make, build, prepare’ || (+ *pati-) Arm. (LW) patrast ‘ready’, 
Arab. (LW) fihrist ‘index, table of contents, catalogue’ (Bailey 1935: 762 f.) || (+ 
*fra-) Par. rhiz- ‘to lie down’ || (+ *ui-) Arm. (LW) varsa-viray ‘hair-dresser’ 
*SANSKRIT: raj ‘to stretch, direct’ (RV) = EWAia II: 425 

«PIE *H3reg- ‘to stretch, direct’ = LIV: 304 f. | Pok.: 854 f.
```


## [2026-09-04T23:08:19.378Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13340,13382p' CHEUNG.txt"
}
```


### [2026-09-04T23:08:19.448Z] TOOL RESULT

```
*NEIR: (+ *4-) Oss. І. areexsyn/araxst, D. arzexsun/araxst ‘to fit, match; to deal, cope 
with; to be able’ 

*MISC: Arm. (LW) erasxi-k‘ ‘warrant, security’ (Benveniste 1945: 71) 

*SANSKRIT: raks” ‘to protect, guard’ (RV+) > EWAia II: 422 

9 This root goes back to an apparently old ingress. stem, which has a cognate in Gr. 
*PIE ingress. *Holek-s^/;- ‘to defend, protect” = LIV: 278 | Pok.: 32 


*IE COGNATES: Gr. &A€Ew ‘I ward off, defend’ 
*REFERENCES: Abaev, Slovar’ I: 59; DKS: 233b f.; Werba 1997: 468 


*Hraz ‘to draw a line; to direct, richten’ 
*AVESTAN: Y Av. raz- ‘to draw a line; to direct, richten’ || (+ *ham-) ‘[med.] to rise, 


become erect; to comb’ = Liste: 56f. 

Caus.: pres. IND. 3sg. Y Av. "razaiieiti (Yt 4.9), med. 3sg. YAv. ham.räzaiiete (V 17.2), 3р1. ҮАУ. 
razaileinti (Yt 14.56), med. 3pl. YAv. razaiiente (Yt 10.14), INJ. med. 2sg. YAv. ham.razatianha (V 
17.4), med. 3sg. YAv. ham.razatiata (Yt 19.47); Partic.: pres. caus. razaiiant- (V 8.100 ff.) 


*OLD PERSIAN: rasta- < r-a-s-t-°> (ppp.) ‘right, straight, true’ = Kent: 206a 

*MIDDLE PERSIAN: MMP r’yn-, BMP I’dyn- /rayén-/ ‘to arrange’, MMP r’yyhy- 
(pass.) ‘to be prepared’ || (+ *api- ?) MMP *pyr’st- (pret. stem), BMP pyl’d-, pdl’d- 
/péray-/ ‘to adorn’ || (+ *abi-) MMP ’br’st- (pret. stem) ‘to raise up, exalt’ || (+ *a-) 
ВМР ’I’d- /aray-/ ‘to prepare, arrange, adorn’ || (+ *pati-) MMP pdr’y- ‘to prepare; 
to rise’ || (+ *fra-) MMP pr’r’z- ‘to stretch out’ (LW) || (+ *ui-) 2. MMP wnyr-, BMP 
wynl- /win(n)ir-/ ‘to be arranged, put in order, be prepared’, MMP wyn’r-, BMP 
wyn'l- /winär-/ (sec. caus.) ‘to put in order, arrange’, MMP wyr’y-, BMP wyl’d- 
/wiray-/ ‘to arrange, adorn, prepare’, BMP wl’c- /wiraZ-/ (caus.) ‘to arrange, 


*Hraz 197 


prepare’ (LW), ВМР wyl'dyh- /wirayih-/ (pass.) ‘to be arranged, etc.’ || (+ *ham-)
```


## [2026-09-04T23:08:34.426Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T23:08:34.436Z] TOOL RESULT

```


```


## [2026-09-04T23:08:38.853Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%A7%D8%B3%D8%AA%D9%86",
 "prompt": "Give the full etymology of Persian آراستن (ārāstan) — Middle Persian form, Proto-Iranian root, PIE root, and any cited references (Cheung, MacKenzie, Hasandust)."
}
```


## [2026-09-04T23:08:41.265Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%BF%CF%81%CF%80%CE%AF%CE%BF%CF%82",
 "prompt": "Give the full etymology of Ancient Greek σκορπίος 'scorpion' — what origin do modern sources (Beekes) give? Is a Semitic (Hebrew ʿaqrāb) origin mentioned?"
}
```


### [2026-09-04T23:08:46.350Z] TOOL RESULT

```
# Etymology of Persian آراستن (ārāstan)

**Middle Persian Form:**
"From Middle Persian _𐭠𐭫𐭠𐭮𐭲𐭭𐭩_ (ʾlʾstny /⁠ārāstan⁠/), prefixed form"

**Proto-Iranian Root:**
The term derives from "Proto-Iranian _*Hraz-_"

**Proto-Indo-European Root:**
The ultimate source is "Proto-Indo-European _*h₃reǵ-_ ('to straighten')"

**Referenced Cognates:**
The entry identifies related Persian verbs _پیراستن_ (pirâstan, "to embellish") and _افراختن_ (afrâxtan, "to hoist"), plus distant connections to Sanskrit _राजति_ (rājati, "to direct"), and Latin _regō_ ("to rule; to steer").

**Note on Sources:**
The Wiktionary entry does not cite Cheung, MacKenzie, or Hasandust by name in the visible etymology section, though such scholarly references may inform the underlying linguistic reconstruction presented here.
```


### [2026-09-04T23:08:46.578Z] TOOL RESULT

```
# Etymology of Ancient Greek σκορπίος

According to the Wiktionary entry, modern sources reject the Proto-Indo-European origin theory. Beekes argues that σκορπίος "is more likely a Pre-Greek loanword instead, with a pre-form along the lines of *karaᵐp-" and potentially related to other Greek terms for insects like κάραβος (beetle) and κεράμβυξ (longhorn beetle).

The entry does not mention a Semitic origin (such as Hebrew ʿaqrāb) as a possibility.
```


## [2026-09-04T23:08:53.148Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D9%82%D8%B1%D8%A8",
 "prompt": "Give the etymology sections for Arabic عقرب and Persian عقرب — Proto-Semitic reconstruction, root, and whether the Persian is a borrowing from Arabic. Also any note on the Arabic root ع ق ر."
}
```


## [2026-09-04T23:08:53.968Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/scorpion",
 "prompt": "Give the full etymology chain for English 'scorpion' — Old French, Latin, Greek, and any suggested ultimate origin (Semitic? PIE?)."
}
```


### [2026-09-04T23:09:01.635Z] TOOL RESULT

```
# Etymology of عقرب (Scorpion)

## Arabic عقرب

**Proto-Semitic Root:** The word derives from Proto-Semitic "*ʕaḳrab-" meaning "scorpion."

**Etymology:** "Inherited from Proto-Semitic" *ʕaḳrab-*, attested since Akkadian times. Cognates appear across Semitic languages including Aramaic, Syriac, and Hebrew with similar forms.

## Persian عقرب

**Etymology:** The Persian term is "Borrowed from Arabic عَقْرَب (ʕaqrab)," which itself traces to the same Proto-Semitic root.

**Relationship:** Persian's عقرب represents a loanword adoption from Arabic rather than independent inheritance from Proto-Semitic.

## Note on Root ع ق ر

The page does not provide specific etymological analysis of the individual root letters ع ق ر. It only documents that the complete form *ʕaḳrab-* appears consistently across ancient Semitic languages, suggesting this root is ancient in origin but offering no breakdown of component semantic elements.
```


### [2026-09-04T23:09:01.856Z] TOOL RESULT

```
# Etymology Chain for "Scorpion"

Based on the Online Etymology Dictionary entry, here's the documented etymological path:

**English → Old French → Latin → Greek → PIE**

- **English** (c. 1200): *scorpioun*
- **Old French** (12c.): *scorpion*
- **Latin**: *scorpionem* (nominative *scorpio*), extended from *scorpius*
- **Greek**: *skorpios* "a scorpion"
- **Proto-Indo-European**: "*sker-" root meaning "to cut"

**Regarding Semitic origins:**

The document notes an alternative source for Spanish: "The Spanish *alacran* 'scorpion' is from Arabic *al-'aqrab*." However, no Semitic origin is proposed for the English word itself—only the Indo-European lineage through Greek and Latin.

The PIE connection suggests the Greek term derives from the root meaning "to cut," likely referencing the creature's cutting/stinging capabilities, rather than from Semitic languages.
```


## [2026-09-04T23:09:15.548Z] TOOL CALL #49: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-04T23:09:15.588Z] TOOL RESULT

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
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-04T23:09:21.278Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor fn in ['BQT_v1_pages.txt']:\n    data=open(fn,encoding='utf-8',errors='replace').read()\n    leaves=data.split('\\f')\n    print(fn,'leaves',len(leaves))\n    for i,l in enumerate(leaves):\n        if 'اردیبهشت' in l or 'ارديبهشت' in l:\n            print('leaf',i, [w for w in l.split() if 'ارد' in w][:10])\nEOF"
}
```


### [2026-09-04T23:09:23.097Z] TOOL RESULT

```
BQT_v1_pages.txt leaves 777
leaf 312 ['ارد', 'اردی', 'اردیهشتگان', 'اردیبهشت', 'اردیبپشت', 'اردو']
leaf 693 ['اردیبهشت']
```


## [2026-09-04T23:09:26.416Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (310,311,312,313):\n    print('======= leaf',i)\n    print(leaves[i][:3000])\nEOF"
}
```


### [2026-09-04T23:09:28.407Z] TOOL RESULT

```
======= leaf 310
اردشیران
" قهر وخشم یز آمده است٩‏ ؛ و فلم پسر ساسان
این همن که اول ماسانان بوده ات و او را
اردشیر بایکان میگفته اند ۰ واک‌لسره ابشان
اند - و تلم پسر شیروبه بن پرویز هم هست - و
کی را نیز گوبند که در قوت و شجامت بی
تهپور و جبن باشد .
اردشیر ان ۴ - بالف و نون » نوتی
از مرواست و آن گیاهی باشد خوشبوی لیکن
ار دشیر جر ه ضم خای نقطه دار
و فتح رای بی‌نقطهٌ مشدد » نام‌الکه‌ایست بز رکه
از ولات فار ی که شیراز و میمند وس‌منکان(۱)
)۱ صیمکان * لفت‌نامه * .
مج وه اح
و برخان (۷) و سیراف و کازرون و کم فیروز
از آن الکه است و رسم کرد؛ اردشیر باشد » و
بحضنی گویند رسم کرد نمررود بن کنمان است؟ .
ار ذشیر ۵ارو « با دال بی شله
بالف کشیده و رای بی تقطه‌بواو رسیده ؛ بمعنی
اردشیران است وآن داروبی باشد درنهایت تلخی.
اردفناقی « بح اول و کس انی و
سکون * اث و فتح فا و نون نالف کشیده ‏ وکس
فای دیگر شحتانی رسده ۰ بللت بوهانی نباتی
است صحرابی , جهت کزند کی جانوران خصوصاً
زئبور طللا کنشد نافم باشد . و آثرا یعربی قثاه
الحمار خوانند . #
م کب بمنی اه آردشیر واردشیر پادشاهی است
کیت
ارو
۵ اردل ماهی - نوعی ازماهیان
۰ ۹ ۱
استخواندار , که در آب های ابران چندان ‌
زباد نت کلا۱6 850 « دربای خزر ‌
۷ > .
بقبه از صفحه ٩٩‏
است »متیر از مقدی . اما وبراف مشق از وبر بمعنی مرد و هوش و خرد است » کلمه بمعنی
======= leaf 311
آردسهشت
او س باکاف‌فارسی بروزن‌پهلوان,
بمعئی اردجان است و ها ور
سرار ۳ و 4
بر از جداول و اشکال و !
وباکاف تازی‌نام موضعی است
ونام دهی است از ی
ار دم بفتح اول و الك و سکون‌نانی
و میم , نام سوره‌های زر که است از کتاب زند
و یازند )۱( - و بممنی‌کار وهثر خوب هم آهده
ابت - و بممنی آذربون هم هست که نوعی از
افحوان باشد .
اد ذهی « بکس میم و سکون تحتانی»
نام جانورست نامعلوم ؛ و بجای حرف انی زای
نقطه دار هم بنظر آمده است .
ادذن « بنتح اول دثالث و سکون انی
و نون » تلم ولابتی است - و نام رودخاله‌ای هم
حست تزديك بدمشق 8 ؟. گوند رم عیسی‌علبه
السالام را قزر ان رود غانه عست بو کشک و
ثرشی پالا را نیز کفته اد » و باین معنی بضم
اول هم آعده است - و در عربی نام شهرست
بزرکه از نواحی شام . گویند قبر حضرت بمقوب
عو چاه یوسف درآ نجاست ؛ و آورده اند کهمشن
حضرت عقوب بر دوازده فرسنگی اردن بوده »
و در وید الفتلا نم همزه وذال نقطه دار آمده
(۱) چله : ژند باژند .
است وافة اعل . *
اد دون - بروزن پهلران , نلپلدشامی
بوده از نسل کشتاسب ۴ - و ناپولایتی هم‌هست
بسیار وسیم - و مضفف اکردوان هم باشد .
ازذو 4 » بر وزن مرغوله . نلم آشی
است مانشد کاچی و آنرا از آرد عیده پزند .
ار دی .- «نم اول , مخغف اردی بپشت
باشد . و آن نام ماه دوم است ازسال‌شمسی ۴
از ۵ یبهشت * « بن‌اول » بمعنیآتش
است که بعربی نار خوانند . و تام عاه حوم(»)
است از سال شمسی و بودن آفتاب در برح تور
و نام روز سیم از هر ماه شمسی باشد - و نام
فرشته‌ای هم هست که محافظت کوحها کند و
ندييي آمور و مصالح ماه اردی بهشت و روز
اردی‌بهشت تملق بدو دارد » و بتابر فاعدث کلی
که نزد فارسیان مقرر است که چون تام ماه با
نام روز موافق آ ید آنروز راعد کنند وجشن
مازند. دربن ماه این روز را عید کنند و جشن
نمایند و آنرا اردی بپشتگان همم خوانند جتح
اول . درین روز نك است بعصبد و آتشکنتنم
رفتن و از بادشاهان حاجت خود خواستنر گت
وکارزار شدن! »ومعنی‌تر کیبی‌این لفت‌مانندبهشت
سیاسی . کیهان. ۲۷۷ .
«هیرون * گونند .
که از شمال بچنوب ۹
سدوم ریزد « فاعوس مقدس۲ ۳۹-۲ .
۴ پپلوی ۸۲۵۳۵0 نلم پنج تن از
۴۳ رك : اردببهشت .
است . شا وهیشته مکی از
فبه + صفیحة ۱۰
======= leaf 312
بخشایش » بمعنی خیر و خیرات و چیزی در راه
خدا بمردم دادن باشد .
. اددانی معروف است که فقیض
گرانی باشد ۵ - ومردم دروش و فقیر ومستحق
را نیز گونند - و بمعنی ملم بتشدید لام هم
امده اسمت . 4
ار « با زای فارسی بر وزن مخزن»
نوعي از درخت بادام کوهی است: و ثمر آن‌سپار
تلخ می باشد و آن رادر دواها بکار برنه وچوب
آبرا عصاکنند و پوست‌انرا بر‌کمان بیچندا .
باشد ٩‏ ؛ چه ارد بععنی شبیه وحانشف ؟حدداست
و چون این ماه وسط فصل بهار است و نبانات‌در
غات نثو و نما و کلها و رداحن تمام شکنته
و هوا در نهات اعتدال » بنایراین اردی بهشت
خوانند  .‏
اد -بوزن طرز » بستی قیمت و بها
و ارزش باشد ۴ - و قدر و مربه را نیز گویند
- ویمعتی درخت صنویر هم هست - ودرخت انار
- و درخت سرورا نیز گفته‌اند - و در عربی برنج
طعام باشد؟ ۴«
اررانش ۴ - بکس نون بر وزن اددن ذدین - کنایه از جرعةُ
۱ - اشتباه است چنانکه گفته شد . ۴ - پهلوی 2۳21 مشثق ازاوستابی 3۳۵[2
« پارتولمه ۱٩۱‏ « تب رک ۲۲ » وتیز 272 درپهلوی آمده ۶ منای ۲۹۷ : ۲ 4 .
۴ - در عربی ارز در لائیتی ۲۷2۵( . ۴ رگ : فزهنگ دساتیر ص ۲۳۲ ۰
شاهد برای آن بافته تشد . ۵ - بهلوی 2۳2201 (دارای ارزتی) و 2۳28۳16 ( عفت )
« مثای ۲۹۷ : ۲ * . - ۵۵6۲ ۸۳۷۵۵ د یاتی ۰.۱۰ ۸62012
ا2ع5۵06 درختی از کل پروانه‌ها که از آن صمغ عربی گیرند ۶ فرهنگه روستابی ۲ _--
نیز نام دشتی درفاری که آنرا ارزن وارجن وارجنه هم کفته‌اند . این‌البلخی در فارسنامه (ص۱۵)
گوبد : مرغزار دشت ارزن » این مرغزارکه برکنار بحیره ارزن است وببشه است ومعدن شیر »
طول آن ده فرسنگه درعرض مك ۹
۵ اردیهشتگان - جشنی که ابرآنیان‌باستان در روز اردیبهشت (سوم) از ماه
اردیبپشت بریا میکردند . « بشت ۱ : ٩۲‏ « خرده اوسنا ۲۲۰4 « روزشماری
۵۸ * ارزان - دزمهلوی 2۳2۵0 (باارزی » فیمتی) «بونکر ۸ >
کیذکی 2۲720. فریز ندی و. بر ای ونطنزی 2۳2110 « ۱.۵ ص۲۹ »> سمنانی
0 , سنگسری وشهمیرزادی 212110 , سرخ ولاسگردی 8۲228 2 .۲:
ص ۱۹۵ ۵ ادن - نباتی‌اس که درنواحی سردسی رک هکندم عمل نمیآید
بعنی در فسمت های کوهستانی برای مصرف اهالی با دانةٌ مرغ کاشته شود و آن
پت وکم ارز است . < لفتِ نامه » و رك : فرهنکهه روستابی ۱۵۱ . اب نکلمه
در پهلوی هم 272۵0 ( هز 028 ) آمده . « بونکر ۰۱۲۱ ۱۷/10
« کل کلاب * ۱ ارزن
یه ازصفحه ۱۶۱
یا کی ونقدس وفالون اهورامزداست ودرجهان خاکی نگیبانی آتش بدو سپرده است ( وبهمین‌جهت
مولف کلمه را سممنی آتش گرفته !) « روزشماری ۱۹-۸ . ۷ رك : روزشماری ۷٩‏ .
8۵ اردو - مجموع میاهیان , مجموعةٌ فشون و لوازم او - لشکرگاه < کاشفری ج ۱
ص۱۱۲ » - نام زبان مردم پا کستان که ممزوجی است از فارسی وخربی و هندی و ترکی . ره :
داثرةالمعارف اسلام ولفت‌نامه .
======= leaf 313
مه موم ما ی > ج با
کل فا
درل مخرفا
اردو
```


## [2026-09-04T23:09:39.561Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (307,308,309):\n    print('======= leaf',i)\n    print(leaves[i][:3200])\nEOF"
}
```


### [2026-09-04T23:09:41.620Z] TOOL RESULT

```
======= leaf 307
ی
"ار پیاسیوس - با تحتانی و سین بی
نقطه و تحتالی دبکر بروزن مرد چایلوی . نام
حکیمی بود (۱) از یونان . گویند در علم طب
مپارنی تمام واخته است ۷ .
ار بیان س بر وزن بهلوان » علخ آبی
باشد و بعربی جرادالبحر
گوند . قوت, باه دهد
وبلفت اهل شام کل‌بابه نه
را گویند . اربیان
از تا - با نای قرشت پروزن برصیصاء
بلفت زند و پازند (۲) بام خانه را کوبند ۴ .
اد فا ه با تای قرشت بروزن فردا , بلفت
زند و پازند (۲) بوم و زمين را کویند ۴ .
ار تحك « بنتح جم بر وزن اسپرك :
برق برادر رعد را کوشد » و بکسر جیم حم
شظن آمده است . ۶ه
ار نگ » بر وزن فرهتگه » نگارخانة
مانی نقاش باشد - و نام بتخانةٌ چين هم هست -
و کی لت که لا مایت ما من
تقش است ؛ و بضی این لفت دا بجای حرف
ئالك ثای مثلثه آورده اند و کفته اند کهدرافت
فارسی بغیر از اين لفت و لغت ثغ بثای سه نقطه
)۱( چك : بوده .
و غین قطه دار دیگر لفتی بثای سه نقطه نبامده
است ۰ وئغ‌بت را کویند وعربان صنم خوانند .
ار تشدار * - با :حتالی مجهول
وشین فرشت و دال ابجد بر وزن پرهیز کار ؛
لشکری و سیاهی را گونند - ونم رود خاله‌ایست
بسپار بزرکث در حدود قبجاق .
از ث_بانای مثلئه بر وزن ابجد . نام
بیخی است که تخم آنرا فلفل بری و حب‌الفقد
خوانند و بات آنرا پنجنگشت و ذوخمة اوراق
ادج - بفتح اول و سکون الی و جیم
بمشی قدرو قیمت ومرتبه و حد واندازه‌باشد ۷
چه ارجمند صاحب فدر وقیمت و مرتبه را گویشد
و مند بمعتی صاحب و خداوند آمده اه نت
وبمعتی کندن و جدا کردن هم هست - ونامعرغی
است که پرهای او بسیار نرم میباشد و در میان
بالش کنند و بترکی قو ۷ خواند - وک رکدن
را نیز گفته اند وآن جانوری است درهندوستان-
شبیه بکاومیش لیکن برسر بینی شاخی دارد -
و بمعنی قیمت و بها و آرزش هم هت .
از جاسپ+۸ ۰ بر وزن طهماب ۰ نام
برة فراسياب است که در تون پدتاه ی کرد
و درروینه دژ (۳) ٩‏ مسکن داشت وچندین یس
(۳) چش : رومینه دژ .
9
۴ - رك : ارژنك .
دراوسثا ۲2۲26510412 و در گزارش بهلوی
استاده ۰ مهبای جنگ
س ۵۱6-۵۰4 * .
بقه در صفحهٌ ٩۸‏
======= leaf 308
ارجالون
کثتاس را در جنگه کشته بود و لهراسب پدر
کتتاس راکه تركه پادشاهی کرده در بلخ‌بعبادت
مشغول بود بقتل در آورد و به آفرین و همای
راکه دختران کشتاسب بودند گرفته در دوینمدژ
محبوس داشت عافبت اسفندبارین کشتاسب روئه
دژ را کرفته ارجاسپ را کشت و خواهران خود
را نجات داد - و نام پهلوانی عم بوده تورانی .
ار جالون » با لام بر وزن افلاطون .
گیاهی است که مانند عشقه بر درخت ها ید
و آنراکرم دشتی و بعرب یکرمةالبیضا خوانند .
ار جان - بر وزن مرجان , بلفت اهل
مفرب چلفوزه‌باشد ؛ و بسنی گویند لوعی ازبادام
کوهی است و این اسح است .
بمعنی عزیز و گرامی و صاحب فدر و خداوند
(۱) مرتبه باشد چه ارج بمنی قدر و مرنبه و
مند یمعتی صاحب و خداوت است - و دادا و
دانشمشد را هم کنته اند- وهر چیز قیمتی رائیز
کوند . وبممنی بی همثا و غلبه کننده هم‌آهده
است . 4
ار جن بر وزن آرزن » درخت بادام
(4۱) چش : - خداوند .
تلغ را گویند ۲ ۰
از جنگ - بر وزن خرچنگه » نگار
ار جنه » بقئح اول و ثالث و نون » تام
دشتی است. درفاري . کوبندامیرالممنن‌علی(۷)
علیه اللام (۳) سلمانرا در آندشت بزور ولابت
از چنگ شیر نجات داد ۴ - ونام نوابی ولحنی
است از موسیقی .
ار چمون - باجیم فارسی بروزن خرچین؛
زینه پابه و نردبانرا گوشد .
از جینی - باجیم فارسی‌بزوزن‌خرچینی»
نام کوهی است از توابع صفاحان .
ار حبقنه بفتح اول و سکون ثانی و
کسر حای حطی‌بتحتانی رسیده و کسر فاف وفتح
نون ؛ بلفت دومی بمعنی‌اسپرك است وآن کیاهی
باشد که بدان چیزها رنگه کنشد .
الرث « بفتح اول و سکون ثانی‌ودال ابجد
۴ بمعنی خثم و قهر و نخب باشد ۵ - وعخفف
آرد هم هت - و بضم ارل مانند و نی وشبه
را کونند - و بکس اول نام فرشته ایست که
هو کل بر دین و مذهب است ؛ و تدییر و مصالح
)۳ چك : عم -
اصاف < بارتولمه ۱۹۱ ۰ .
3 « ثابتی ۱۵٩‏ *.
۴ - دراوستا 2۳12 و2162 ودر
واردسهشت آعده , ۶ فابی۱ ص۵۵ * .
بیدا شده. رك : اردشیر.
یه از صفحهٌ ٩۷‏
از مولف است « حاشه چك ص44 * .
. درشاهنامه : روین دژ‎ ٩
جزء لامنفك کلمه است .9 مزدستا 4۰4 >.
======= leaf 309
خوانندش, وبعض ی کویند منسوب‌باردیل‌ین ارمنین
است وتا کردة اوست .
اردجان س با جیم بر وزن همزبان»
از جد اول اهل نجوم است و در احکام مرقوم.
ار دش 7 س بفتح اول و ثانی وضم‌دال
می نفطه و سکون‌شن نفطه دار , نام مقدارععینی
است از کناهان بزعم فارسیان .»
از ۵ شیر - نام بهمن بن‌اسفندبار پدرداراب
است. کوش
چون جدش
او را سیار
دلیروشجاع
یک
روز آرد که بست ویذجم از هر ماه شمسی‌است
پدو تعلق داردا .نيك است درین روز نو بریدن
و پوشیدن , و بداست لقل و تحوبل کردن ۴ .
اددا ه بر وزن فردا » تلم موبدی و
دانشمندی است ۰ و او در زمان اردشیر بابکان
بوده و فارسان او را سقمس دانشته اند و او را
ار داد بر ون فر‌هاد نبز کفته اند و پدر او
وبراف نلم داشته بکسی واو ۴ .
ار ۵اه - بر وزن مردانه . کلی است
محرایی که آنرا خیری بری گویند ت
"ارب ه بروزن‌هرشب , جنگه وجدال
را گوند ۴ .
ار3لیل ۰ بر وزن زجیل » نام پس
آرمنین بن لنطی بن بونان ۱( است - و نام نام موسوم
شهربست معروف . گونند آن شپر را فیروژ جد .| ماخت. . سکه‌های اردشیر بایکان
انوشیروان بنا کرده و از آن جهت فیردذ کرد | ومعنی ترکیبی آن شیر خشمنالك» چه ارد بمعنی
(۱) چش : بونابی . ۱ ۱ ۰
٩‏ .در اوستا آتأدا(۷2:0)8 ت۸۵ , در پهلوی 271 . کلمةٌ ونگوهی صفت است بمعنی
تيك و خوب و کلمةٌ م کب مزبور بمعنی اشی نيك وهمين ت رکیب درپهلوی ۲9250۷2۳۵ .
( وصور دیگی) بهمین معنی آمده . دراوستا اشی کاهی اسم حجرد است بیمشی توافگری وبخاش
وی رکت و نعمت و مزد و بپره؛ و گاه اسم خاص ابزدی که نگهبان مال وخواسته است . در جهان
«ینوی ودر روز واسین باداش کارهای نبلك و سزای کردار زشت باری او افجام خواهد شد .
«روزشماری ۵٩-۵۷‏ » . ايشکه درمتن ارد بکسر اول بادشده برای استممال آن دراشمار فردوسی
است که با « سیاوش کرد » و « ایزد کرد » قافیه شده . ۴ رك : روز شماری ۸۳ .
۴ اردا بممنی ارد « مقدس » است . راك : ارد » ارداوبراف . ۴ اردب (بفتح
اول وتشدید با) عربی, آزبونانی 870406 » سربانی 2۳06102 با :2۳4602. مکیالی درمصی حمادل
۷۷ لبیتر . « دائرة المعارف اسلام * . ۵ این لفت در پپلوی 2701511 است »
و در اوستا 22005 و آن خریتی ات بسلاح با سوه قسد ) از بادداشت های وندیداد
آفای پورداود ). ۱
* اردا و راف - دریاب این‌نام اختلافاست . بارتلمی و وست بیروی ازسنت زرتشتیان
آنرا ۷۲۵۲ ۸۱۵ و)۷۱۲2 ۸۲2 وگاء جزه دوم‌را ۷1720 وبعی‌مانند بارتولمه‌و کرستنسن
۵2 ۸۲488 رد۷۱۵2 ۸۳۱۵8 وهرتفلد۷۱:82 ۸۳2 خوانده. منای قولدستة اول را
تأیید میکند و هنینگه قول دستذ دوم را - جزه اول اردا بمعنی مقدس است - وبراز بمعثیکراز
هه درصفحةٌ ۷۰۰
```


## [2026-09-04T23:10:21.858Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'اردلان' in l:\n        print('leaf',i)\n        import re\n        j=l.find('اردلان')\n        print(l[max(0,j-600):j+600])\nEOF"
}
```


## [2026-09-04T23:10:22.957Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint('leaves',len(leaves))\nhits=[i for i,l in enumerate(leaves) if 'نرد' in l]\nprint(hits[:40])\nEOF"
}
```


### [2026-09-04T23:10:23.944Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-04T23:10:25.804Z] TOOL RESULT

```
leaves 684
[57, 77, 166, 167, 209, 215, 262, 281, 288, 289, 337, 357, 366, 369, 404, 424, 448, 495, 500, 516, 529, 534, 570, 581, 605, 636, 654, 664]
```


## [2026-09-04T23:10:37.253Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON اشو\"; grep -o -n \".\\{200\\}اردیبهشت.\\{300\\}\" MON_part1.txt | head -4; echo \"=== MON اشو2\"; grep -o -n \".\\{120\\}«اشو».\\{200\\}\\|.\\{120\\} اشو .\\{250\\}\" MON_part1.txt | head -5"
}
```


### [2026-09-04T23:10:37.329Z] TOOL RESULT

```
=== MON اشو
=== MON اشو2
```


## [2026-09-04T23:10:39.137Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('incoming/IRN/IRN_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint('leaves',len(leaves))\n# printed = pdf - 11 ; pdf page N = leaf index N-1 (0-based). printed 28 -> pdf 39 -> leaf idx 38\nfor i in (37,38,39):\n    print('=== leaf',i,'printed',i+1-11)\n    print(leaves[i][:2000])\nEOF"
}
```


### [2026-09-04T23:10:41.096Z] TOOL RESULT

```
leaves 222
=== leaf 37 printed 27
[pdf page 38]
کر رد۳
و تم ی ها مر 2و ور رز
چوک ی ا وک 12
ص ری اک و رو ی 0 0 ۳ زر
و وگ وی هت رد کی ده روش یک ری ۲ کون ان
وان 4 و و ی نک هر
تجح کدی رد سس تور از ام
۳۱ و نا 9 زر 9
اه 1 و ۱ ی 1 ۳ 4 ۷۱۵ ۸
ویر ام 2 چا ی روز زا ود
ی ۹ ۱ ار ‎ -‏ و یا ی 1 ۴ ار
۵ ۹ ۸ ۱ ی ی 8/۵ و۵ ۹۹۱۱۵
جرا او وود هه 1 ۱
2 فور ۵1
دج هه 5 مزر ۹ ی : 0 رو 1
ار 0 ۸ 1 1 ۱ چا وم | در ی
: و ۳ 1 6 هد
: [ 5 9 4 7 :۹ ۸ لا ۷ از ۷ ۱ 4 ۱ج
کض و ور سل ۵ ۹ و۲ اس
ی : و سا 1 از ْ ۱ و 1 زا رن بو
5 و 1 / ۵ هر ۳ سا ی با مس ما
را ۰ ری 2 ۱ 0 7 2 ور ری اس ۸ 32
ون 2 1 1 ها زَا 1 ره
مر رمم ‏ خر مه کی تسش زا ۱ ما
وا 1 ال من رپس
1 ۹/1 7( ۳ 1 پر ۲ ۵ 0 مورا ۳
اف : 7 1 ام ها سود 0 ههد
و هه ی ار ۳ مرو ور این ۱ چ
1 ارم رز ال مس ی ۳ رح
۷/۸ / ۳ ام 17 ۳ ی یگ از اک
8 رجا 1 0 و اه ما ۹ ی ام ۸ اش 1
مب ۳ ام اد رک وی رم )بر
ول ها بای و ریک
ار وی 4 رک 0 لاد ارس 0
۸ ۹ # بر و ۷ ۹ ۳ اد شک ۳ 5 هر 9 ۹
منت ۶ تسا ۰ ار
۱ 9 6 ورن سا دی هه ۱ ۵ ( :ها
۵ و کش ۸ ۸۹۸۲ ما اد
رن ۰ ار 8 ار سوام اس :۱
ام اس ان ۴ سر ۹ 1 ۱ 0 نو 1
پشه هس ۲ و 5 مرو ی ۳ 1 20 سا
8 سروس رک و 2 او
ی وک وا ۱( کت ماو
شم و ار رو 1 3 1۵ هک ۹ ۹ ۱ ۳ ام ۷ شا
۴ 1۱ دوجو اه
هت ۵ 4 ید ات :2 20 سمص نا مر 9 ی ۹
و 7۳ ام :۹ اوخت: 7۹ 7
وک 8 او ۹ 2 ۵ اک ان
نا فا 9 بو رکش رات ها ی
آفنر ون او و و و او اب ۳ تن
شک ی و و و ار اش و اب
1 ی رز ی ی پر نا و ۸ 0 11
و ۹ امه ( موی وین اون ار و ماه با و
( ۰ ی ی 9 ی ۵ پا ‌ نی 1 اج 1
و۹ مرا او 4 ریت خر :۳
۸ 0 ۵ خبط ی نا
او نان رو ی سای که یا زب 1 1 ِ
خر ره ی اه 0 ین و 7 ۱
در ۵۱ ۵ ۱ 5 1 ۹ ۹
1 مس یه وکا 8
ز 7 سا ها ها سا
ره را ماو ما وان ۱ 8 ۱ سم 1 9
: ی رد 3 ۳ و غ 9 :
۳ :1 ار 0 ی 0

=== leaf 38 printed 28
[pdf page 39]
۲۸ ایرانویج

این‌دو تیرة بزرگك باهمة طایفه‌های خودکه نام برده شد» بسوی نواحی
حاصلخیز پیرامون درياچهُ رضائیه (اورمیه-شهرآب) فرودآمدند, یره مادی در
نواحی جنوب شرقی دریاچه بین همدان وتبریز جای گرفت وبعدها تا اصفهان پیش
رفت وقبیله‌های پارسی درمغرب وقسمت‌های جنوب غربی دریاچه» درناحیةٌ اردلان
کنونی جای گرفت . واه اردلان را میتوان بصورت کهن آن «قله*2 بازسازی
کرد: 271-۳30 ومعنی‌آن «ایران مقدس» است.

این‌قبیله‌ها با یکدیگر باصلح وآرامش زندگی م ی کردند و به دامداری و
تربیت اس بکه یکی از مهمترین پیشه‌های آنها بود می‌پرداختند. یکی از علل
برتری آنها نیز در دوران تاریخی داشتن اسب‌های تربیت شدهٌ خوب بودکه در
جنگها عامل مهم پیروزی بشمار میرفت .

اینان » نخست به خدمت امیران بومی درآمدند وسپس خود سالار و سرور
روستا ها گشتند .
قبیله‌ای از مهاجران هند و اروپائی که در پی‌یانتن سرزمین ها و چراگاه‌های جدید مهاجرت
م یکنند (نقل ا زکتاب عنسصده[1۳3)
ی

=== leaf 39 printed 29
[pdf page 40]
برخورد اير آنیان وبومیان
قبیله‌های جنگجو وگله پرور ایرانی به سرزمین ی که بعدها بنام آنان ایران
خوانده شد روی آوردند وبصورت دسته‌ها ی کوچ نشین کوچک وبتفرق در پهنةٌ
با بومیان آرام وصلحجویانه بود و همچون عموزادگان هندی خود ناچاربه‌جنگهای
بومیان ایرانی دشمنی‌سرسخت و دیرینه چون آسوریان در برابر خود داشتند
که هرچندگاه برای غارت دارایی‌آنها چون سیلی‌خروشان فرود می‌آمدند و هرچه
داشتند با خود می‌بردند. ورود این جنگجویان پشتیبان خوبی برای نگهبانی‌دارایی
و روستای آنها بود» ازاینرو درپیرامون روستای خود به‌آنها جای دادند, آنان به
5 ۱ ۹۳۵۱۱ ۱0۱ ایو
۱ ۱۳۹/7 ۹۹ ی ۹۱۱۱ ۱ ۲۳۱
۹ 1 ۷ ۱ 1 : ۷ ۴ ۱ 1
وس هو هه
سا درا و ی ۴
و
ار ام گس تست >
2 دام ۱7۱0 میس سنج در
8 اه روا ی لب
رک کت نوا مرواب 1 1 ۱۲/۱۱ 8 ره بر ۱1زا
کت ره او اک اک ی
رل و نک کرد ۳۵ رصع
دس امین ره دیاس بر یک سا
حطس پچ س ی و
ج 3/ اد و وی 2 یج روص 0
واه ر همست کت کاس
اه اک مر تسکت
رد کر ا ی
دژ پیش از تاریخ ایرانیان در سیلکه (کاشان)
```


## [2026-09-04T23:10:52.549Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c MON_part1.txt MON_part2.txt; head -c 400 MON_part1.txt; echo; echo \"=== grep ارد\"; grep -c \"ارد\" MON_part1.txt; grep -c \"بهشت\" MON_part1.txt"
}
```


### [2026-09-04T23:10:52.625Z] TOOL RESULT

```
4377831 MON_part1.txt
4331421 MON_part2.txt
8709252 total
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
=== grep ارد
1308
39
```


## [2026-09-04T23:10:54.577Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('incoming/FFD/FFD_pages_faseng.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint('leaves',len(leaves))\n# printed = pdf - 5 ; leaf idx N-1 for pdf N. printed 24 -> pdf 29 -> idx 28\nfor i in (27,28,29):\n    print('=== idx',i,'printed',i+1-5)\n    print(leaves[i][:1800])\nEOF"
}
```


### [2026-09-04T23:10:56.808Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'incoming/FFD/FFD_pages_faseng.txt'
```


## [2026-09-04T23:11:00.146Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/FFD/; python3 - <<'EOF'\ndata=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint('leaves',len(leaves))\nfor i in (27,28,29):\n    print('=== idx',i,'printed',i+1-5)\n    print(leaves[i][:1800])\nEOF"
}
```


### [2026-09-04T23:11:01.971Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
leaves 115
=== idx 27 printed 23
[pdf page 28]
ماده‌های ماضی
و
مضارع فارسی دری

=== idx 28 printed 24
[pdf page 29]
در شرح ریشه‌شناختی فعلهاء نخست مادهٌ ماضی و آنگاه مادهٌ مضارع آمده است.
گاهی هم نخست مادهٌ مضارع و پس از آن ماده ماضی آورده شده است. در شرح.
صورتهای ایرانی باستان و گاهی همراه با آن» صورتهای فارسی باستان ماده‌ها ذکر شده

آراستن

آراست + فارسی میانه 3738۳ + ایرانی باستان 12 - 739 - 3*. 8 پیشوند فعلی است که
در اصل بر انجام گرفتن کار به سوی متکلم دلالت می‌کرده است. 734 صورت اصلی 739
است. 7 پیش از 1 به 8بدل شده است. 734 به معنی «منظم کردن» است. 18 پسوندی بوده
که از ریشهٌ لازم» صفت فاعلی گذشته, و از ريشهٌ متعدی» صفت مفعولی گذشته
می‌ساخته است.

آرای + فارسی میانه 273 < ایرانی باستان 2 - 734 - 3*. 2 برای ساختن ماده از ريشه
به کار می‌رفته است.

آرامیدن. آرمیدن
«آرامید» مادةٌ ماضی جعلی است» از مادةٌ مضارع ساخته شده است.
آرام < ایرانی باستان 2 - 1308 - 3* برای 8 > آرای. 5 پیشوند فعلی است.

=== idx 29 printed 25
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


## [2026-09-04T23:11:28.509Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS\"; grep -n -i \"vahist\\|ahlav\\|ahlaw\\|artvah\\|urtvah\\|asvah\" SNS.txt | head -20; echo; echo \"=== SNS pages leaf count\"; python3 -c \"\nd=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f'); print(len(d)); print(d[10][:1200])\""
}
```


## [2026-09-04T23:11:28.873Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \".\\{100\\}اردیبهشت.\\{250\\}\" MON_part1.txt | head -3; echo \"=== اشو\"; grep -o \".\\{80\\}اشو .\\{200\\}\" MON_part1.txt | head -3"
}
```


### [2026-09-04T23:11:30.369Z] TOOL RESULT

```
=== SNS
45:A pahlavi - persian Glossary 
408:rivSyat dar pahlavl az avistS ud zand. 
505:Tfte Proper and Improper. An OZd Pahlavi Rivayat . 
680:J.C. TAVADIA: $ayaet-n3 "Sayaet. A Pahlavi Text on 
990:Nyb. (Nyberg) : H.S. Nyberg, A Manual of Pahlavi 
999:Pahl. V.: Dastoor Hoshang Jaraasp, Pahlavi Vendi- 
1005:Pahl. y. Vr.: B.N. Dhabhar,' Pahlavi Yasna and 
1036:FrP.: H.F.J. Junker, The Farhang i Pahlavik, 
1115:B.N. Dhabhar, The Pahlavi Rivayat accom- 
1293:Pahlavi Fragments with text, trannlti 
1298:: Pahlavi Vendidad, Bombay i •> 
1308:: The Pahlavi texts, vols 1, M 1 
1432:: The Pahlavi RivSyat accompanying 
1435:: Pahlavi Yasna and Visperad, Bom- 
1459:Nyberg, H.S.: A Manual of Pahlavi, Part II Germany, 
1504:Hoshang, D.J.J : Pahlavi Vendidad with Glossarial 
1520:Junker, H.F.J. : The Frahang i Pahlavik, Heidel- 
1531:Kapadia, D.D.: A Glossary of Pahlavi Vldevdat. 
1808:.^il .y-jJu LjL .j^ftl .:ahrav/ahlav 
1817:CoJ^t-jL :ahraven/ahlaven : QjrWy 

=== SNS pages leaf count
243
               ::

1-1 jtf-                                                ^Ujl^yi^          ,




                    Etymologie. Strassburg 1893 new ed.,         Nt

                    York 1974.
Hymn       .        M. Boyce,        The Manichaen Hymn Cycles in hit
                    thian, London Oriental Series Oxford         l«*li
                                                                              AiWb.:    C. BartholoiQae, A Itiranisahes Wdrterbuoh,
JA.:                Journal Asiatique.
                                                                                        Strassburg. 1904 new ed., Berlin 1961.
JRAS.:              Journal of the Royal Asiatic Society.
                                                                              Armen. Gram.:      H. Hubschraann, Armenisohe Gramma-
List.               W.B. Henning, "A List of Middle-Persi.n.
                                                                                        tik,   Germany 1962.
                    and Parthian Words", BSOS. 9-1937-39-79-'
                                                                              BBB.:     W.B. Henning, Ein Maniohaisches Bet-und
Man. Stud.:
```


### [2026-09-04T23:11:30.435Z] TOOL RESULT

```
=== اشو
```


## [2026-09-04T23:11:33.153Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1800,1830p' SNS.txt"
}
```


### [2026-09-04T23:11:33.198Z] TOOL RESULT

```
• Ji/\r £ \r-\\/\*s -^U <f~jb^ p>r^\^ 



ytW 



.^il .y-jJu LjL .j^ftl .:ahrav/ahlav 
asavay 1* asSg *j'^ j-ati* iSf^H oy* j J *3'.j cw' isW** « •=—' »^- i - s 

(M.F. .rtavan ;tf i/j-/ja^ artavan •'»> aiavan- .'£- 

Ctfir.tfan.11,45) >hlw.>;fc (Kent. 170-171), Kanga,32) 

1Y/YY-* ^f-y-^/To J .A-Y-6/lfi^-fl-n-U-A 

CoJ^t-jL :ahraven/ahlaven : QjrWy 
u^* -*>*■ if^^o'jo- 1 ) .<^-^jjj-,en +(«ji 50 -*ftJj): ahrav 
■f1/1T«* (Kapadia: 255 : ,£; .j,b Lj^ 



t>i*0' : *& . c*#iU i |.Uilj- i^^u pas-iz, ^HR, yz •>& O**o» 



-*&*_y
```


## [2026-09-04T23:11:41.349Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(d):\n    if 'ahrav/ahlav' in l or 'ahlav' in l:\n        print('leaf',i)\n        print(l[:1500]); print('---')\n        if i>60: break\nEOF"
}
```


### [2026-09-04T23:11:43.391Z] TOOL RESULT

```
leaf 1
                              Shiraz University Publication




     A GLOSSARY OF
SAYIST NE SAYIST
 A pahlavi persian Glossary
             -




       and Six indexes

         '




                      By

        Mahmood Tavoossi




                 * Z 2 2 7 7 6 O*

---
leaf 4
                                                                                         Index

                                                                                                           wbS,jjl„ is** 'A ^-.rt-*
                                                                                  2-44
                                                                                 45-52           tfil*>5   ^U <*->   ^ oVc-^i
                                                                                 53-65                        ^U-^^U *;'*      ^^
                                                                                 66-68                 ob-l^.j-jU^U •;'* C~*J
                                                                                                             ^jS-i-csU •3 > ^__^i
                           j^,\^ »>» P U
                                                                                                                           l

                                                                                 69-74




«   .S^^^lt-a , »=-*; f U »>l ^V-J -»^^ *^-* oT   ;'   *yrr ^ '* ">»"> J J


         rivSyat dar pahlavl az avistS ud zand.



en riv5yat ast az avista ud zand                               :   (s^V-^-)^

.   *xi ^IS &\ j j   ^ J*
                      j3    o>^J* JA>' ** i/ u ^'wj
                                                        U J*   ^     ***" ** *



                                                 
---
leaf 6
                            J                                                                                                                                                 ,
                                                                                              I*^v,
                                                                                 »b*«

                                                                                              jjlj
                                                                                                     'jtf •*/•»>   Yffc'^^^^tf'tO M51             J               u
                                                                                                                                                          *J A ryj^
                                                                                                                                                               C-j >

                                                                                                                                                                       :&»-*>*«
                                                                                                                       (o^b^bj^



                                                                     ^Uj/^U, U,                                                /
utuMd^                «&ha»"j ^Ujjj-* *JlU-^k; 3!^ *S*
                                                     
---
leaf 7
                                                                                                                     »


                                                                                                        jLiS^
                                                                                                                                                                                                                             oU
     i^   ^  m
                 Ij-n 4-t •j^i       u »A o^vr Ki* j j A-** 3 Ub - ***** *         1




^     OJ ^( aj*) *jUjy» ts^it
                                              Jii l* i^     *fr o*i*V Jlfri '**** *-Vj      -*




                                                                                                                                                                                   &c«l«a^ jlB Ajj, .jl^ 4.L .jl3 o,!
j^.Aitii^lAj^^s hast                               :   -^ + lt + -*       '•
                                                                                   fctiu-*       OW           >'«*•(
                                                                                                                          J.C. TAVADIA: $ayaet-n3 "Sayaet. A Pahlavi Text on
                                                                                                                          Religious Customs. Hamburg 1930.
                                                                .   jj5   1^
---
leaf 10
               ::

1-1 jtf-                                                ^Ujl^yi^          ,




                    Etymologie. Strassburg 1893 new ed.,         Nt

                    York 1974.
Hymn       .        M. Boyce,        The Manichaen Hymn Cycles in hit
                    thian, London Oriental Series Oxford         l«*li
                                                                              AiWb.:    C. BartholoiQae, A Itiranisahes Wdrterbuoh,
JA.:                Journal Asiatique.
                                                                                        Strassburg. 1904 new ed., Berlin 1961.
JRAS.:              Journal of the Royal Asiatic Society.
                                                                              Armen. Gram.:      H. Hubschraann, Armenisohe Gramma-
List.               W.B. Henning, "A List of Middle-Persi.n.
                                                                                        tik,   Germany 1962.
                    and Parthian Words", BSOS. 9-1937-39-79-'
                                                                              BBB.:     W.B. Henning, Ein Maniohaisches Bet-und
Man. Stud.:                C. Saleraan, Manichaeische Studien,
                                                                                        Beichtbuch, APAW. 1937
         Saint-Petersburg 1908.
                                                                              BSL.:     Bulletin de la   S
---
leaf 11
                                                     :   ;::    .:               .


                          j-j^iAj   4*   *»t   ^jU. ^ty^^jS                                                   •j.i^-



Paris 1960                                     Pahl. y                Vr. Glos.:     ibid.   (vol.   2)

Zeitschrift der Veutschen morgenl&ndU          PRivDd                  B.N. Dhabhar, The Pahlavi Rivayat accom-
en Gesellschaft.                                                     panying The badistan i binik. Bombay 1913.
C. Bartholomae, Zur Kenntnis dor Mi/t.         Ps.                   F.C. Andreas and K. Barr., Bruchstucke
iranischen Mundarten I -VI SHAW, HQdoll- rq                          einer Pehlevi Ubersetzung der Psalmen SPAW
1916-25.                                                             1933
C. Bartholomae, Zum Sasanidischen U»oht\       P.V         Gl ,:          CSee: Pahl. y. Vr. Glos.)

Heidelberg 1918-1928.                          SBE. V                    E.W. West. The Sacred Books of the East.
                                                                     vol. V India 1965.
                                               §GV                   Dastoor Hoshang Jaraaspji and E.W. West,
                                                                     Shikand Gumanik Vigar. Bombay 1887
                                               5n5.                  J.C. Tavadia. $ayat ne-Sayaet edited, trans-
                                         
---
leaf 13
                                                                                .                         ,




                     t^   W   ^ U^k* *i ^^ j c u

                                                                                                                                                         '(^(j5
Andreas, F.C.-Barr, K.:              flruchiwcfce einar                        /
                                                                                                               t^ traa o'^ »^ ,j ^W-* 4-— r
                                                                                                              .I
                                                                                                                                                 s


        t/fcersetsMrtff       der Peatmen.         SPAW   1   ')   I       i




Andreas, F.C.-Henning, W.B.:               Mittelirani o.-h.
        niohaica aus Chine&isch-Turkeu an                 t            .            I        »




        Berlin 1932-34.             (Mir. Man.)                                             {
                                                                                                                .   j^JL. ^li.   J}U ^lio^'o-l-      1


Andreas, F.C.-Henning, W.B.:
        telpersisahen der Tut fan fragment
                                            bas Verbum                 .1.



                                                         
---
leaf 14
                                       .                                                ,                                           .



*i                                            ji^l^V-U^i*!.                                         ,   yW   ^Iq*« ^t» > c<i»

                Translation of Zand-i Khurt-ii
                  :
                                                                                                                  BSOAS       XXIV,

        tak. Bombay 1936.
                                                                                                                  BSOAS. XXVI, 1963
Gershevitch, i.: A Grammar of Mania he an                     .'<'                                               Opera Minora, ed. by, Y.M. Nawabi. vol. 1.
        Publications of the Philological                      ::                i
                                                                                            .
                                                                                                                 Froozangah Publishers. Shiraz-Iran 1982.
        Oxford 1954 (GMS)                                                                                         TPS. 1956.
                                                                                                                          c:
                                                                                    |




                  :     Unvala Memorial Volume.     
---
leaf 15
                       )                                                                                                     .




  Mirza, H.K.;
                                                                       ^   W   is^Uj «* J^T. s ^U.                         y>3
                       Jackson memorial volume, Bombay,
          1954.                                                        Horn, p.:  Grundriss der neupersisohen Etymologic,
 Modi, j.j.:   The Religi OUB Ceremonies                                       Strassburg 1893. new ed., 1974 (GNPE)
                                         and Customa
          of the Persees, 2nd. ed., Bombay                             Hoshang, D.J.J : Pahlavi Vendidad with Glossarial
                                            1937
          CTRCCP .                                                             Index. Bombay 1907 (Pahl. v.).
 Morgenstierne, G.: An Etymological                                    Hoshang, D.J.J. -West, e.: Shikand Gumanik Vijar.
                                      Vocabulary of
         Pashto. Oslo 1927.                                                    Bombay 1887    (SGVl.
 Muller, P.M. Ceditorl:                                                Hubschraann, H. :        Armenisahe Grammatik, Leipzig,
                         The Sacred Books of the
                                                                                     1897    new ed., Germany 1962. (Arm. Gram).
         East. V new
---
leaf 18
                                                                                         'J')
                                                                                                                                                                                                                                                          V
                                                                                                                                                                                            f
                                                                                                                                                                                                Ui c-,1: *-L*3lj

                                        •
                                            Ji/\r            £    \r-\\/\*s -^U <f~jb^ p>r^\^

                                                                                                                                           t>i*0' : *&      .   c*#iU i |.Uilj- i^^u                      pas-iz, ^HR, yz                           •>&      O**o»
                                       .^il .y-jJu                LjL .j^ftl .:ahrav/ahlav                                  ytW
     asavay            1*   asSg            *j'^ j-ati* iSf^H oy* j J *3'.j cw' isW** « •=—' »^-i-s


                                                                                                                                
---
leaf 34
     rY                                                  ,u a-U »;lj
                                                                                                                                                                            b«*L «;lj                                r?


      ft/fl^.j'^ tr&T Jl-T • J       U st-t*— ytotiftj^jj
                                           tf                                         ^e^myp/iM
                                                                                                         (AiWb. istaka:L i!tya-:/i- «*-- j»T,c*i» :xilt:                                                          t^^^O-

                                                                                                                                                                                       •r*/T^       378.)
                                     -^ «>A il :asemvohQg: l^Vi
                                illf«jl,                 Jjfc



                              1/ir ^ .U-Yt/U^ .T6-TT/W^ Y-6/fiJ
                                                                                                        IviskSra- L*avisk3ra- : L»
                                                                                                                       :                                    .   *,KiT , _,KiT: 5sk3rag : ^Wflao-M

                                                                                                                        
---
leaf 51
                                                                                                                                               ,Li*.L.;l,                           Yo
                               IfcJ .-,-j
                                          l^ 4.U *^1^
Yl



.^^Jb^iAjftf- :x v arsSd ul mad:               i*l««*>-^       ^^ *
                                                                                                         Vf/T.^ (WPS.          112,    4i^.l866)o^^ <^ Var l^»=




                                                                                                      ..oUT^i^-^/^j,*: xvardlg I kardag: j*»-*w
l^^oi* ^-*«^ :xv ars§d yasta ivlhj* *>-«jV                                                               brothi^^'/c.,^                        ifahlavi Text p. 30.)
          v
10^a^>.; x arsed
                 yastan , -n/U ^ t^*3 * : ***)                           l


                                                                                                                                                 No. 7        •.*£         .o-io Jj5T    a
                                                                                        j                .YA/T^ LDahbhar. PHivDd.

,*>.«u>jfc*Aj** :xv a rsed
                           nigirisn:                       v^***"^*                                                                                                ^yuyO^f
                                                    
---
leaf 103
                                                         '       :


                                       tu^tn-L.jlj                                                                                 c-^Lul-^L^U^Ij                                                       \Vt
YA


                                                      .(Kotwai.       P- 169)                                                                  (Jlb.jfi^-,       :sast5r:        1a*»«*xx_w
                   .Y-p-6-T-l/" ** -6/T^
                                             *                                              !.P$           •(/Kk'fc.       1573)sastar-                   :   i^tf-**    sastar-:*5"
                                                                                                                      U/1fl^           (Mir. Man.             Ill, 61)-;s*st*r                      :




                                                         .j-V-       :spas:o"e>JJ            "-JjIj^a^-jVJU^jI^^j.i^^i^Ujj^"                                             .jL   :sar:\<o»
                  (AiJ/fc.    1614) spas i&SiS**             /spas-          :&-


                                                                                                                                                              .JL.aJL :salag: l9J-*<_v

^^.T^V^^^                 ***<* :x v ast ? :                            ,*mvW
 T4j^ffj.A.T
                               v
             w«*m*>o nsjlwO * x as
---
```


## [2026-09-04T23:12:12.569Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd1=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(d1):\n    if 'آراستن' in l or 'آراستَن' in l:\n        print('v1 leaf',i, 'approx printed', i-210)\nd2=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(d2):\n    if 'راد' in l and i>350 and i<400:\n        print('v2 leaf',i,'approx printed',i+543)\nEOF"
}
```


### [2026-09-04T23:12:14.763Z] TOOL RESULT

```
v1 leaf 138 approx printed -72
v1 leaf 238 approx printed 28
v1 leaf 241 approx printed 31
v1 leaf 316 approx printed 106
v1 leaf 331 approx printed 121
v1 leaf 362 approx printed 152
v1 leaf 363 approx printed 153
v1 leaf 604 approx printed 394
v1 leaf 605 approx printed 395
v1 leaf 667 approx printed 457
v2 leaf 351 approx printed 894
v2 leaf 353 approx printed 896
v2 leaf 355 approx printed 898
v2 leaf 356 approx printed 899
v2 leaf 357 approx printed 900
v2 leaf 363 approx printed 906
v2 leaf 364 approx printed 907
v2 leaf 369 approx printed 912
v2 leaf 378 approx printed 921
v2 leaf 379 approx printed 922
v2 leaf 380 approx printed 923
v2 leaf 386 approx printed 929
v2 leaf 387 approx printed 930
v2 leaf 390 approx printed 933
v2 leaf 391 approx printed 934
v2 leaf 393 approx printed 936
v2 leaf 398 approx printed 941
```


## [2026-09-04T23:12:18.244Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd1=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (238,239,240,241):\n    t=d1[i]\n    j=t.find('آراستن')\n    print('=== leaf',i)\n    print(t[:1600] if j<0 else t[max(0,j-1200):j+1400])\nEOF"
}
```


### [2026-09-04T23:12:20.174Z] TOOL RESULT

```
=== leaf 238
آرا
آداه بروزن خارا . آرایش. وآرایش
کننده و آراینده را کویند همچو خن آرا
و بزمآرا وامی باینمعتی هم هت ممنیآرایم
کن و بارا .
9
و پنجم است از هرماه شمی - و ام فرشته ای
باشد (۱) که حوکلست بر روز آراد . و اسور
ومصالح این روز تعلق باو دارد . کوبند: درایتروز
جامةٌ نو (۲) پوشیدن بیار خوست وسفر کردن
بیار بد .
آر ازذش » بکس زای هوز بر وزن
آسایش » بمعنی خیر وخیرات کُردن و درراء خدا
چیزی بکی دادن باشد (۳) ۶
1 مر رز تلم : بش
سکون و فرار - و طاقت - و اطاعت باشد .
و نی اکن شنت و فا گرفتن هم هست جت
ساکن شو وقراربگیر . - و بمعني جا و مقلم هم
امه کت < و کی با بر م۳ مر رین
شهر و صبه و ده باشد .
]رام لن - .بفتح بای ابجد و سکون
نون . بمعنی آخی آرام است که باغ میان شهر
و قصبه و ده باشد . ۱
ادامش س بی‌وزن ومعنی آمایش‌است
آد ات » بروزن باران . تام ولایتی‌است۴
وارنج را نیز کویند که مرفق باشد ۴
آرای بروزن بارای»آرایش وآراش
کتنند و آراننه وا کرد - و امر به آراستن
هم هت یعنی بیارا و آرایش کن ‏ :
آدایش ۹- بر وژن آصایش ه بمعنی
زب وزینت باشد - و رسم و عادت وآیین را نیز
کویند - و نام نوابی است از موسیقی .
] ر اش خور شید - نام لسن اول
ست از سی لحن باربد و خطی که بي عارض
7 3
آرت . بقتح ثالث و سکون فوفانی .
آرنج را گوشد که‌بند گاه ساعد وبازوست وبعریی
مرفق خوانند ۴ .
دج - ختح. ناك
فآ ات کم باشد ۷ - ونامپر ندم‌ای
آرد. بتح نله و ال ان
؟ ‏ رك : 1
آرت ۰ رد : : آرن
۰ رك : آرمیدن
۹ - رك:آران ۰
کردن » مهیا سلختن .
۳ هاده
کردن » آسودن . ساکن شدن .
=== leaf 239
ت برایو بی اه آرامی
رة حواشی صفحة .۳
۵ آرامی_نام قومی از فبایل بدوی سامی ناد سوربه که درجنوب فلسطین در پبرامون
کوبر ومشرق رود اردن وبحرالمیت میزیستند. اين شبانان چلدرنشین ویابان نورد ازخوشاوسان
تزديك اسرائیلیان بودند و بغلط برخی آنان را کلدانی خوانده‌اند . ازفرن ۱۶ق.م.. آرامیان به
سرزحی‌های عتمدن همایبة خودروی آوردند ودست بفارث زدند. سوربه وشماق سسن‌النهرین میدان
تاخت‌وتاز آنان گردید. در کتیبه‌های آشور متملق بال۱۳۲۰ ق.م. این قبابل اخلایه ۸۵۵۵6
ودرآ تار متاخرنر آرامه ۳81796 خوانده شده‌اند . شلمااسر 51181۳1310366 اول, پلدشاه آ شور
در سال ۱۲۸۰ ق .م. با آراهیان در
زد وخورد برد . انان بهرجاکه روی
۳۳ «مم [ ۵ | رارق انید ییا رید وی | دسج | مین
کردند کتاورزان را بفرمان خود
در آورده و بازر گانی ر بدست گر فتند ۳۰ جاوما جوا مج چ + | »|
و بر راهپای کارواغی تسلط بافتند و در و اووا و ادووا <وا و :| و | و | دا
سرزهین هابی که بچنگه آوردته از | و | همم ۱ ها دا
جااب خود شهربارانی گماشتند . در و بو + ۳۰۹5 ۱۱۱۰۱۶
حدود مال۱۲۰۰ ق.م بی‌دمشق وحلب ۸ ۰۱4۵8۵۱7 4 ور ۹ ۳
ی 4 3 تا ۱ ۱۲۱ ۲۶۱۱۱ #۶ 1 1 1
کیره صفد و۵ مرح رات حود ۱ ۰ 1۱۱2711۱ 3 | وه 2-2 ]| ۲ 5 ۱
از میان بردند . هجوم آرامیان دز 9۱9۱۱۱ جوا چا هه ۷ ]۲
بین‌التهر ین‌چند ان‌شدید بود که خاندان ‌ 1 ۰ ۳۹۹ 1
بادشاهی آن دبار را برانداختند وخود 4« و | | ۲۶ ۶ ]<< ۱
ی 3 ۱ #7 7 ب
ی ات ۱۲۱۰
وت در برد ی ور روواها جوا وواج یخلت دا واه
چنانکه پس ازفینیقیان, رامیان . ه (۰ ۱ < ۱۱۱ (9 ادر.سی -مجز | < | ۵ | 9
فوم‌سامی نژاد بودند که بانفون بازر کانی دود + + | و ]هب |9۱8۶
خود همهحا راءه بافتند . #ه | ت ! ب ای | هی | تن ]۵ او |
درنینوا مایشخت آشور ودربابل / 1 اود ۱ ر || و |
تجلرتآ نان روتق داشت و نفون سیادت ی ی مق و ی
اش انا نع خر ویاا ر ف ۳ «ع ۳ وی ج 54| ۰
بدان باتج
=== leaf 240
آرامی - پرایی ۷۲٩‏ س
آرامی بکاربردند. بدبنوجه زبان آرام یکه اززبانهای سامی‌است وآموختنش برای‌هزدم مأی زبان
دشوار یست باخط آرامی که الفبابی.ساده بود سراسر کشورهای اقولم سامی نژاد را فرا کرفته از
بلحرالروم نایشتکوه (زاگری) وخلیج قاری زبان. بین‌المللی محصسوب حیشد.
هنگامیکه ابرانبان بسرزمین‌های آشور وبابل وآسبای صفیر وسوربه وعصر دست بافتند
باافوامی سروکار پیدا کردند که زبان وخط وسیلهٌ ارتباط دبوان های دولتی هشامثشیان و متصرفات
غربی ابران‌شد. درتوراة , کتاب عزرا باب4 بند۷ آمده: #در روز کار اردشیر اول(هخامنشی) بشلام
21520 ر مهرداد وئبیل [۲20 وباران دیگر آنان مخط آرامی و با ترجمةٌ آرامی نامه‌ای
باردشیر یادشاه ابران نوشتند. »
ازفرائن پیداست که خط میخی برای‌حوائج روزانه بکاردمیرفت" واین‌خط برای کنده کری
اختصاص داشت " اماالفبایآرامی با ۲۴ حرف برای کتابت آسانتر بود . خط سکه‌های محلی دور
حضامنشی و وزنه‌هابی که رویآ نبا خط آرامی نوشنه‌شده وخط بیاری ازمهرهای ابرانبان که ,خطا
آرام یکنده کری‌شده » بخوبی دواج این خطرا درایران میررساند .
کتیبه‌ای «رجيهةٌ آرامگاه داربوش ازنفش رستم بزبان پارسی باستان وبخط آرامی موجود
است وآن‌بنام اردشیر اولاست. یس‌از انقراض سلسلهٌ هخامنشی خطآرامی که در آن‌روز کار هممجا
رخنه بافبه‌بود همچنان راء خودرا پیمود تابجابی رید که چندی پس‌از آن بنام خط پهلوی‌خوانده
شده است. ۱
آار عمدث آرامی- دوبخش ازتوراة بزبانآرامی است: بخشی از کتاب دانیال که درژمان
ااقیوخس‌اییفانوی ۳۵/0205 ۸۱۷۵11:05 (۱۷۵-۱۹ ق.م. ) توشته‌شده وبداتیال تسبت
داده‌شده» دیگر بخثیا ز کتاب عزرا که درحدود فرن سوم ق.م. نوشته شدم همچنین تر گوم
0 (ترجوم - ترجمه) نضبری که بتوراة نوشته‌شده واز فرن‌دوم ق.م. آغا زگردیده است؛
بزمان آرامی است - نیز نلمود (آموزش) بدین زبان است که بخشی از آن‌دا در آغاز قرن چهارم
مبلادی د
=== leaf 241
مخفف آوداس تکه نام روز بیست و پنجم از هر
ماه شمی باشد ۱- و ممکون ثالث معروف است
که له آسیا کرده باشد ۴ - و بمعنی تقصیر هم
ات
آ رث و له - (۱) بش فوفانی و سکون
واو و فتح لام ء آشی باشد مانندکاچ یکه از آرد
پزند و بیشتی مردم درویش و ففبر خورند وآنرا
جریی «سخینه » گویند .
ومشی آرد توله اس ت که آش کاچی مانند باشد .
]ددم - بنتح رابم و سکون عیم ۰
نام کل آذربون است که نوعی از شقایق وکل
همیشه بهار باشد .
] ذن - بفتح رابم و سکون نون »
,کفگیر سوراخپا دارد وبدلن چیزها صافیکنند.
وکفگیی را نی زکوبند - و نم ولاشی هم
ضت . ؟ *#
]رذهاله - بیای (») بالف کشیده
و فتح لام » بمعنی آرد توله است که آش کاچی
ماتثف باشنه.
آرش
]رده جتح زای حوز , کاحگل را
کوبند . و آن خاکی است که با کاه آمیزند
وگل سازئد و بر دبواز وبام خانه مالند .
آرژه گر - بفتحم کاف فارسی
و سکون رای فرشت . شنصی را کون که کاه
کل عاو...
| دست ع بروزن وارست. بمعنی‌توانت
باشد که ماضی تواشتن است - و مضفف آراست
هم هست که از آراستن باشد . ۴
۲ دسته - مسر وزن وارسته مخفف
آراسته باشف .
دش ٩‏ - بنتح ثاك و سکون شین
شطه دار ۰ نام پهلوانی بوده ابرانی از لشکی
منوچهر و در صنصت تبراندازی عدیل و نظیر
نداشته چنانچه تیری از آمل بمرو انداخته که
قربب بچهل روزه (۳ ) راء است ۰ وکونند آن
تبر مجوف بودماست وآنرا از شبنم پ رکرده‌بود »
و بوفت طلوع آفتاب بجاب مشرق اداخت *-
و نام پسردوم کیقباد هم است که او را «کی‌آرش»
گفتندی ۷ - و یکس ثالث ۸ - بععنی «معنی*
"4
۹ بونکر ۱۱۲ *.
؟ - پپلوی )27 « تاوادبا
۴ - ول : آرستن ۵ اوستا
۱ - از آن خوانند آرش را کمانگیر
که از آمل بمرو انداخت يك نی
و ۱۶۲
شتین چوکاوس با آفرین
2 مزدسنا ۷ ۰
مراد - معشوق » موب :
```


## [2026-09-04T23:12:33.241Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd1=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(234,244):\n    t=d1[i]\n    for j in [m for m in range(len(t)) if t.startswith('آراستن',m)]:\n        print('leaf',i,'::',t[max(0,j-300):j+700].replace('\\n',' | '))\n        print('-----')\nEOF"
}
```


### [2026-09-04T23:14:03.276Z] TOOL RESULT

```
claude-sonnet-5[1m] is temporarily unavailable (timed out), so auto mode cannot determine the safety of Bash right now. Wait a moment and then try this action again. If it keeps failing, continue with other tasks that don't require this action and come back to it later. Note: reading files, searching code, and other read-only operations do not require the classifier and can still be used.
```


## [2026-09-04T23:14:15.317Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-",
 "prompt": "Give the reconstruction, meaning, Pokorny reference, and the list of derived terms/descendants, especially any *h₂r-to- 'fitted, right' forms in Indo-Iranian (Sanskrit ṛta-, Avestan aša-/arəta-, Old Persian arta-)."
}
```


## [2026-09-04T23:14:17.236Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AF%DB%8C%D8%A8%D9%87%D8%B4%D8%AA",
 "prompt": "Give the etymology of Persian اردیبهشت (Ordibehešt) — Middle Persian form, Avestan source, and meaning."
}
```


### [2026-09-04T23:14:22.298Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂er-

**Reconstruction:** *h₂er- (alternative: *h₁ar-)

**Meaning:** "to fit, to fix, to put together, to slot"

**Pokorny Reference:** Pages 55-58 in Indogermanisches etymologisches Wörterbuch (1959)

## Key Derived Terms

The root generated numerous descendants across Indo-European languages, including:

- *h₂ér-mn̥ "chariot" → Greek harma, Latin armenta
- *h₂er-mó-s "fitting, joint" → Greek harmós, Latin arma (weapons)
- *h₂ér-ti-s "art, skill" → Latin ars
- *h₂érti "now, near" → Greek árti, Lithuanian arti

## Indo-Iranian *h₂r-tó-s Forms

The webpage documents the reflex *h₂r-tó-s meaning "fitted":

- **Sanskrit:** ṛta- (also álam from áram)
- **Avestan:** arəta- (Younger Avestan: aṣ̌i)
- **Old Persian:** *arta- (reconstructed)

These forms appear in the section discussing Proto-Indo-Iranian *Hr̥tás and its descendants across the Indo-Iranian language family.
```


### [2026-09-04T23:14:23.051Z] TOOL RESULT

```
# Etymology of اردیبهشت (Ordibehešt)

**Middle Persian Form:**
The term derives from Middle Persian "𐭠𐭥𐭲𐭥𐭧𐭱𐭲𐭩" (Ardwahišt).

**Meaning:**
The word means "right" and serves as the name of the second Amahraspand, a divine deity in Zoroastrianism.

**Components:**
The term combines two elements: "ارد" (ard, meaning "truth") and "بهشت" (behešt, meaning "heaven").

This etymological structure reflects the religious and philosophical significance of the term within the Persian calendar and Zoroastrian cosmology.
```


## [2026-09-04T23:14:32.157Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%A7%D8%B3%D8%AA%D9%86' --note 'page 61, root Ar/Are node 8: Persian arastan etymology (Proto-Iranian *Hraz-, PIE *h3reg-)' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%BF%CF%81%CF%80%CE%AF%CE%BF%CF%82' --note 'page 61, root A.q.r node 4: Greek skorpios, Beekes Pre-Greek origin' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B9%D9%82%D8%B1%D8%A8' --note 'page 61, root A.q.r nodes 1-2: Arabic/Persian aqrab, Proto-Semitic *3aqrab-' 2>&1 | tail -3"
}
```


### [2026-09-04T23:14:36.772Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/34a3f4738c689cb0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d60074cfa935881a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fcf6537952dadac5.txt
```


## [2026-09-04T23:14:41.178Z] TOOL CALL #70: Bash

```json
{
 "command": "for u in 'https://www.etymonline.com/word/scorpion' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-' 'https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AF%DB%8C%D8%A8%D9%87%D8%B4%D8%AA'; do python3 tools/fetch_source.py \"$u\" --note 'page 61 verification' 2>&1 | tail -1; done"
}
```


### [2026-09-04T23:14:44.000Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/088e805a2eba63b2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a2a15d9c88ae752f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ecc18995313c60ba.txt
```


## [2026-09-04T23:14:49.696Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%B1%D8%AF",
 "prompt": "Give the etymology of Persian نرد (nard) 'backgammon' — is it derived from Nēw-Ardaxšīr / nardašīr, or from Sanskrit? Quote what is said."
}
```


## [2026-09-04T23:14:51.147Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D8%AF",
 "prompt": "Give the etymology of the Persian word راد (rād) 'generous, liberal' — Middle Persian, Old Iranian, and PIE root; any cited sources."
}
```


### [2026-09-04T23:14:56.125Z] TOOL RESULT

```
# Etymology of Persian نرد (nard)

According to the Wiktionary entry, Persian نرد derives from Middle Persian, not Sanskrit. The document states:

"From earlier نردشیر (nardašir), from Middle Persian nywʾlthšyl (nēw-ardaxšīr, 'backgammon')."

The term originates from the Middle Persian compound meaning "backgammon," with no mention of Sanskrit derivation in this source.
```


### [2026-09-04T23:14:59.101Z] TOOL RESULT

```
# Etymology of Persian راد (rād)

The Persian adjective **راد** (rād) meaning "generous" traces back through several ancient language layers:

## Language Lineage

**Middle Persian**: Inherited from Middle Persian *rād*

**Old Persian**: Derived from Old Persian *rā́daʰ*

**Proto-Iranian**: From Proto-Iranian *HráHdah*

**Proto-Indo-Iranian**: From *HráHdʰas*

**Proto-Indo-European Root**: *h₂réh₁dʰ-o-s*, ultimately from the PIE root *h₂reh₁dʰ-* meaning "to care"

## Cognate Words

The entry notes related words in other ancient languages sharing this root:
- Old Avestan *rādah* ("generosity, care; generous")
- Vedic Sanskrit *rā́dhas* ("favour, generosity, gift")
- Proto-Slavic *raditi* ("to care about, to heed")
- Proto-Germanic *rēdaną* ("to decide, advise")

## Source

The etymological information is cited from Wiktionary's entry, which references reconstructions of Proto-Indo-European, Proto-Iranian, and Old Persian linguistic forms.
```


## [2026-09-04T23:15:16.272Z] TOOL CALL #73: Bash

```json
{
 "command": "for u in 'https://en.wiktionary.org/wiki/%D9%86%D8%B1%D8%AF' 'https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D8%AF'; do python3 tools/fetch_source.py \"$u\" --note 'page 61, root Ar/Are: Persian nard and rad etymologies' 2>&1 | tail -1; done"
}
```


## [2026-09-04T23:15:17.682Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6495,6505p' KFL.txt; echo \"=== pagemarks\"; grep -c $'\\f' KFL.txt; python3 -c \"\nd=open('KFL.txt',encoding='utf-8',errors='replace').read().split('\\f'); print(len(d))\nimport re\nfor i,l in enumerate(d):\n  if 'العقرب' in l: print('leaf',i)\""
}
```


### [2026-09-04T23:15:18.895Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0a9557299970eee3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bcd404de5727dc7d.txt
```


### [2026-09-04T23:15:20.708Z] TOOL RESULT

```
44( 

[ يَسَحُ ] 

كُُ ضارب بِمُوَّخَرِهِ : يَْسَعٌ كالعقرب والزُثبُورٍ (0) 
[ يَلدَعُ ] 

وكلٌ ضارب بفمه (4) : يَلدَعْ » كالحيه فقا ارط 
[ يَنْقِش ] 

=== pagemarks
0
1
leaf 0
```


## [2026-09-04T23:15:29.495Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=6400 && NR<=6520' KFL.txt | grep -n \"^[۰-۹0-9٠-٩][۰-۹0-9٠-٩ ()]*$\" | head -20; echo \"---\"; sed -n '6440,6500p' KFL.txt | grep -n \"4\\|3\\|٤\" | head -20"
}
```


### [2026-09-04T23:15:31.362Z] TOOL RESULT

```
97:44( 
---
51:وكل 3 كو لقوي وو كل أض: تنيي 
57:44(
```


## [2026-09-04T23:15:37.838Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nd1=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(234,244):\n    t=d1[i]\n    k=0\n    while True:\n        j=t.find('آراستن',k)\n        if j<0: break\n        print('leaf',i,'::',t[max(0,j-250):j+500].replace('\\n',' | '))\n        print('-----')\n        k=j+1\nPY"
}
```


### [2026-09-04T23:15:39.737Z] TOOL RESULT

```
leaf 238 ::  .بفتح بای ابجد و سکون | نون . بمعنی آخی آرام است که باغ میان شهر | و قصبه و ده باشد . ۱ | ادامش س بی‌وزن ومعنی آمایش‌است | آد ات » بروزن باران . تام ولایتی‌است۴ | وارنج را نیز کویند که مرفق باشد ۴ | آرای بروزن بارای»آرایش وآراش | کتنند و آراننه وا کرد - و امر به آراستن | هم هت یعنی بیارا و آرایش کن ‏ : | آدایش ۹- بر وژن آصایش ه بمعنی | زب وزینت باشد - و رسم و عادت وآیین را نیز | کویند - و نام نوابی است از موسیقی . | ] ر اش خور شید - نام لسن اول | ست از سی لحن باربد و خطی که بي عارض | 7 3 | آرت . بقتح ثالث و سکون فوفانی . | آرنج را گوشد که‌بند گاه ساعد وبازوست وبعریی | مرفق خوانند ۴ . | دج - ختح. ناك | فآ ات کم باشد ۷ - ونامپر ندم‌ای | آرد. بتح نله و ال ان | ؟ ‏ رك : 1 | آرت ۰ رد : : آرن | ۰ رك : آرمیدن | ۹ - رك:آران ۰ | کردن » مهیا سلختن . | ۳ هاده | کردن » آسودن . ساکن شدن .
-----
leaf 241 :: وز , کاحگل را | کوبند . و آن خاکی است که با کاه آمیزند | وگل سازئد و بر دبواز وبام خانه مالند . | آرژه گر - بفتحم کاف فارسی | و سکون رای فرشت . شنصی را کون که کاه | کل عاو... | | دست ع بروزن وارست. بمعنی‌توانت | باشد که ماضی تواشتن است - و مضفف آراست | هم هست که از آراستن باشد . ۴ | ۲ دسته - مسر وزن وارسته مخفف | آراسته باشف . | دش ٩‏ - بنتح ثاك و سکون شین | شطه دار ۰ نام پهلوانی بوده ابرانی از لشکی | منوچهر و در صنصت تبراندازی عدیل و نظیر | نداشته چنانچه تیری از آمل بمرو انداخته که | قربب بچهل روزه (۳ ) راء است ۰ وکونند آن | تبر مجوف بودماست وآنرا از شبنم پ رکرده‌بود » | و بوفت طلوع آفتاب بجاب مشرق اداخت *- | و نام پسردوم کیقباد هم است که او را «کی‌آرش» | گفتندی ۷ - و یکس ثالث ۸ - بععنی «معنی* | "4 | ۹ بونکر ۱۱۲ *. | ؟ - پپلوی )27 « تاوادبا | ۴ - ول : آرستن ۵ اوستا | ۱ - از آن خوانند آر
-----
```


## [2026-09-04T23:15:47.045Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nd1=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,t in enumerate(d1):\n    if 'پیراستن' in t or 'پیراست' in t or 'پیرایه' in t:\n        print('v1 leaf',i,'approx printed',i-226)\nPY"
}
```


### [2026-09-04T23:15:48.808Z] TOOL RESULT

```
v1 leaf 183 approx printed -43
v1 leaf 248 approx printed 22
v1 leaf 420 approx printed 194
v1 leaf 603 approx printed 377
v1 leaf 661 approx printed 435
v1 leaf 663 approx printed 437
v1 leaf 664 approx printed 438
```


## [2026-09-04T23:15:52.142Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nd1=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (661,663):\n    t=d1[i]\n    for w in ('پیراستن','پیراست','پیرایه'):\n        j=t.find(w)\n        if j>=0:\n            print('leaf',i,w,'::',t[max(0,j-400):j+500].replace('\\n',' | '))\n            print('---')\n            break\nPY"
}
```


### [2026-09-04T23:15:53.830Z] TOOL RESULT

```
leaf 661 پیرایه :: بای مجهول بروزن قیجك ۰ | (۱) چك: ژد و پاژند : | ۱ ‌- ره 5 آهویای. | ۶ اسشق+ ۳4عرك : بیام. | و مربی آن دا عشقه و لبلاب خوانند ۷ - | و کرو ابرشم و رسمانب و سربند زن را | دا | لین » بروزن ربوند . عصانه ویتانی | بند زنان را گومند . | لیچه » با نانی مجهول بوزن رشه . | و عذقه کویندشی  .۷‏ و زلف عملی دا نیز | گویند- و طر؛ زلف و کا کل را حم کقتماند که | پیچند و برمکدیگر گرء زتند - وموی بلف وا | نیز گفنه‌اند و بعربی عفاص خوانند- و پیرایهای | هم هست از عرصع که برسی عووی بتد کنتد - | و بوشش بالای در خائه را تیز کفتماند- و سعتی | رمز وایىا و اشارء عم حست ۸ 3 | یچیه سحرچیز را که یچیده باشتد | عموما ودست برنجا ی که آنرا چها رکوشه اه | تام و متا | لیخ بکر اول و سکون تانی و خای | نقطم‌دار , چرك کوشپا و کنجهای چشم را گوبند | ۳ آبی که از چشم بی آید و مر کانها را برحم | چسباند, وبعربی‌رمص‌خوانتد. ۱ | بخال"- بروزن قتال. فنأة حرتاتوا | که عربان رمص خوانند - و بسی درد و ه | بگفتش همه راز , بایور شپ | ۴ - امروز سد 10( :م) گویند ۰ | ۳ رك : سك . | ت _ اسم مفعول از: بیج
---
leaf 663 پیراستن :: چیزی‌را | از عیب خالی نمودن هم هست . | ثیر استو۱ « کم کردن چیزی باشد | بواسطه زبابی و خوش آیند کی همچو بربدن | ذاخهای زبادئی آزدرخت وموی زبادنی از بدن. | کوبند شبی اباز بامر سلطان محمود در حالت | مستی زلف خویش را بربد. روز دیگر سلطان | از آن حالت پریتان خاطر گفت. عنصری باین | رباعی سلطان را از کدورت بسرون آورد : | ر باعی | هنن زلف بت‌از کاسنن است | چه جای بفم نشتن و خاستن است | جای طرب ونثاط ومی خواستن است | کاراستن سرو ز پیراستن است. | سو دیاغت دادن چرم را نیز گویشد. | ۳ | بر استه؟ بروزن بی‌خواسته » به‌عتی | مرتب گردانیده و ساخته و پرداخته باشد - | و باغی که شاخهای زبادنی درختان آن را بریده | وعلفهای زبادنی آن‌را چده و صفا داده باشند - | و درخت ی که آن را پر کاوش کرده باشند » بعنی | شاخهای زیادتی آن را بریده باشند - ودهی را | معتی بابای ابجدهم بنظر آمده است. | نون و دال ابجد , ماضی متفرق ساختن | وافشاندن باشد بعنی متفرق ساخت ویریشان کرد | و افشانید ۰ | یر آهن» با انی مجهول و میم بروزن | پیراهن» اطراف و کردا گرد چیزی را گونده . | پر اهون ,ائا
---
```


## [2026-09-04T23:16:02.178Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nd2=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (382,383,384,385):\n    t=d2[i]\n    print('=== leaf',i,'approx printed',i+543)\n    print(t[:1800])\nPY"
}
```


### [2026-09-04T23:16:03.990Z] TOOL RESULT

```
=== leaf 382 approx printed 925
                                                     ‫ن|حام‬

        ‫در حرف ذال نقطه دار‪.‬با حروف تپحی مشتمل بر سزده لغت‬
‫بل د بکراول وسکون بای ابجد ‪۴‬‬                                 ‫* ذاقنو بداس ‪ ۱‬سبکرفان ونون‬
‫ولام" بوست لاك بشت‌هندی باشد؛ وبعضی گویند‬                    ‫مواو رسیده و کت بای اند ودال بنوقعاه بالف‬
‫آن با‬   ‫است؟ ‪.‬خاکنتر‬         ‫دكربیشتابی‬
                                      ‫بوست لا‬                ‫کیت ورین مه زود امسانتبای‬
                                                             ‫وویند نوعی‬
                                                                      ‫بعنی مانند غار »آون داروبی‌است گ‬
 ‫‪ ۰ °‬بر وزن و معنی درخش‬                                            ‫از مازربون است وبرکث آن یهن مبباشد‪.‬‬
                                  ‫ذر خش‬
          ‫است که برق وتابندن وروشنی باشد ‪.‬‬                   ‫ذاقی ‪ = ۴‬بروزن سافی؛ بیونالی درخت‬

 ‫ذرع = بروزن‌سرع ک‪.‬نارو گوشة کشت‬                                                         ‫غار را گونند ‪٤‬‏‬
‫بمعنی کز باشد؛‬    ‫و درعری‬    ‫‪-‬‬   ‫وزراعت راگورند؟‬                                         ‫وآن درختیاست‬

   ‫وآن چوبی است که چیزها بدان پیمایند ‪. ۷‬‬                                                ‫که برکش از‬
                                                                                         ‫گبهر‌بید درازتر‬
  ‫ذر یس ‪ -‬ببایس‌ینقطه (‪ )۱‬بورزن‬
                                                                                          ‫واز برگے مورد‬
                                                                                          ‫برزکتر ولرمتر‬
                                            ‫ات ‪. ۸‬‬                                        ‫وسقیدتر میباشد‬
                                                                                         ‫و مو
=== leaf 383 approx printed 926
‫‪Go‬‬                                                                                     ‫‪-۲۳-‬‬
                                                                           ‫بقمه از صفحٌ ‪۲۲٩‬‏‬
 ‫است ( ‪ » ) 80303186 . ]6156‬و لیزیمعنی پوست کرتنکله بعتی تمساح است‪)662۳27۵6-‬‬
 ‫(‪6[۵‬ع‪ 61 0۲6‬و باز بمعنی استخوان لان البحر نی ارب بحری و دمیاست‪6620۵72‬ع)‬
 ‫ذ)ر»خش‪ ,‬برق اکستووبند‬     ‫«‪.‬م‪.‬‬
                              ‫فش (‪۵‬‬  ‫دخشر »‬‫‪ = ۵9‬در‬           ‫(‪« . 61 ۱6126‬لت نامه» ‪.‬‬
‫که در زبان پارسی هیچ‌کلمه نیت که اول او ذال بود جزاین‌کلمه ‪ ,‬ایوشکور (بلخی) کوبد ‪:‬‬
            ‫همانا نگرید چنی ابرزار‪.‬‬               ‫ذرخشی ار شندد بگاه بهار‬
 ‫« لفت فری ‪٩ ۸۶۲‬‏ ‪.‬‬
 ‫‏‪« - ٩‬نرع > كوشة کشت بود وزرع بتازی کشت راکوبند ‪ .‬رود کی (سمرقندی) کوبد‪:‬‬
     ‫زرع کشت است و ذرع کوشۀ کشت ‪€.‬‬                   ‫شوت‬‫هشدچ‬ ‫بار‬
                                                               ‫نرع وزرع ازبپ‬
‫« لفت فری ‪ » ۸۲۲‬این کلمه و معنی با همین شاهد در لغت امه عجیبی که در حاشيةٌ لغت لام‬
  ‫هبماین‬‫اسدی آقای نخجوانی است دیده میشود و لغوبین دیگر لیز عین آنرا بپمین صورت و‬
‫شاهد می‌آورند » لکن بگمان من اکر شمرواقعاً از رودکی باشد (وکمان لمیکنم که باشد ) در‬
 ‫این لفت ومعنای آن پیدا شده است ‪ +‬و عصبت بودن‬          ‫داده » و ازآن تصحف‬     ‫روی‬    ‫شمر صصفی‬

 ‫لغت نامه بموزرازین است که برای همه حروف هشتگانه‌ای که درعربی‌هست ودرفارسی لیست امثلة‬
                 ‫بسباری ازکلمات ناشنوده] ورده ومدعی است که همه آنها فارسی است‪« .‬لغت نامه»‪.‬‬
 ‫‪-( ۷‬عر) بککرزدن ‪ .‬بتاراشجپی‌موادنلن(صادر بیپقی) ‪ -‬کز » ارش » رش ‪ -‬فرع »‬
      ‫تكر‬
        ‫مه ب‬
           ‫چون مطلق کوبند ممادل شانزده کره است عنی مك متر وچپارصد بك متر و درنرع شا‬
  ‫ودوازده صد بك متر است (وبیشتر درتبریزمتداول است) * و ذرع مقصرصاوی بك متر وچهارصد‬
                                    
=== leaf 384 approx printed 927
    ‫‪۷‬‬                                                                                  ‫فکران مرئوما‬

                    ‫ذ کران از مرتبة عید فروتراست ‪.‬‬       ‫در مقابل ماده است‪,‬وبعربی لیزهمین معتی دآرد‪-‬‬
    ‫رواق » با واو و را و قاف وحرکت‬
                                 ‫د‬                        ‫ولوعی از عود الصلیب هم هت وآن نر و ماده‬
‫مجهول؛ طعامی‌است که آرا ازارد کندم پرلد ‪۲‬‬                 ‫میباشد وبعربی ورد الحمیر خوانند‪ .‬وگآیناهی‬
                                          ‫‪۳‬‬                                              ‫است دوایی ‪.‬‬
    ‫ذوش ‪ - ۲‬بروزن‌هوش»تندخووبدخلق‬
                                          ‫‪۳‬‬   ‫را گوند‬    ‫» بکس ون ‪.‬‬           ‫اا‬
                                                                               ‫ونهمر‬
                                                                                   ‫ذتکرا‬
                                                         ‫روز سیم (‪ )۱‬نموز باشد » و كران بمعنی باد‬
‫ذیا نیطی ‪ - ۲‬بکر اول و تحتانی‬                            ‫و مرئوما نام داث‌ندی بوده است بلغت‬     ‫کردن‬
 ‫بالف کشیده ولون بتحتانی‌رسیده وضم طای حطی‬
                                                          ‫سربالی» وآن چنان‌است که چند مود بوده اند‬
‫وسکون سین بی نقطه » بیونالی کوفتی است که‬                 ‫که هر بك چند روز ارزوز های دیگر افنل‬
                      ‫آنرا بعربی سلسالبول کوبند ‪.‬‬         ‫میداسته اند و مردمان در عبادتغانهای خود‬
 ‫د با اول بتحتالی رسیده‬            ‫فینوس‬
                                       ‫ذ‬                  ‫روزهاییکه منوب بهربك ازایشان بوده ابشاترا‬
‫‪۲‬‬    ‫بی‌نقطهٌ زده‬   ‫وضم فاولون بواو کشده و سین‬           ‫باد میکرده اند تا توت بذکران دبگری بر سد‬
‫فلقر اط‬     ‫در خدمت‬       ‫رامشگر‬   ‫بوده‬   ‫مردی‬    ‫نام‬
                                   
=== leaf 385 approx printed 928
                                 ‫گفتار دهم‬
                             ‫اکزاب برهان قاطم د‬
   ‫حررف رای بی‌قطه باعروف تبجی‬
     ‫مبتنی بر ببست وصه بیان و محتوی بر بانصد و هشتاد وسه‬                        ‫»‪ow‬‬

                                                                                      ‫‪۰‬‬




                                 ‫لفت و کنات‬



                                    ‫بیان او ل‬


 ‫نازگیب‪:‬اری‬
          ‫زیر‬
            ‫نوع را قلفویا کوبند و بش‬        ‫‪۰‬‬   ‫با بای أبد بواو کذیده‬    ‫بِ‬   ‫رابو‬        ‫‪#‬‬

                                ‫خوانند ‪.‬‬                      ‫نامگلی است اکزلهای بپاری ‪.‬‬
‫رالینج ‪ ۲‬با فوقالی بتحتانی کشیده‬            ‫بکر فوقالی و تحتانی‬         ‫راتيا نج =‬
‫و نون مفتوح بجیم زده ‪ ۰‬بمعنی راتیانج امت‬    ‫بالف کشیده و نون مفتوح‪ .‬بجیم زده » بمعنی‬
‫که صمغ‌درخت صنوبر باشد ‪ .‬گوبند رومی‌است‪.‬‬    ‫راتینج است که صمغ درخت صنویر بادد ‪ ۰‬وآن‬

 ‫= بسکون حای بی لقطه ‪٠‬‏ لام‬                 ‫سه لوع است‪ :‬بکی روان که منعقد شود‪ .‬ونوع‬
                                            ‫‪N‬‬                                   ‫‏‪E‬‬
                              ‫داح‬
‫یکی از‬   ‫لوایی است امزوسیقی = و دعرربی‬
                                                ‫راا ی‬                          ‫ای‬
                                                                   ‫(‪ )۱‬چك ‪ :‬موم ‪.‬‬
  ‫‏‪ ٩‬د حرف دوازدهم از الفبای فارسی وحرف دهم ازالفبای عربی (ابتث) وحرف بستم‬
  ‫از حروف ابجد ‪ ,‬وآنرا ر ‪ ۵۲‬وراه ‪ ۰۵۲‬نامند و درحساب جمل دویست گر ند‪ .‬این حرف به «ل»‬
                                  ‫[ك ‪ :‬س بح از ديباچة مولف ] ‪ .‬و «ن» تبدیل شود ‪.‬‬
                                                                               ‫ر‬
 ‫(عرب ) ابوزنانی ‪ 0016۸‬بمعنی صمفی که از‬ ‫‏‪ = ۱١‬رانینا = رائینا ‏ راتینج م‬
  ‫
```


## [2026-09-04T23:16:16.619Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nd2=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(385,400):\n    t=d2[i]\n    if 'راد' in t:\n        # find headword-ish\n        m=re.search(r'صفح\\S*\\s*([۰-۹0-9]+)',t)\n        print('leaf',i,'contin-page',m.group(1) if m else None)\n        for k in [x.start() for x in re.finditer('راد',t)][:6]:\n            print('   ...',t[max(0,k-120):k+180].replace('\\n',' | '))\n        print('======')\nPY"
}
```


### [2026-09-04T23:16:18.736Z] TOOL RESULT

```
leaf 386 contin-page None
   ...       ‫==‬                                                                                      ‫راغ‬ |  |  | ‫راد بوی » بابایابجد بر وزن ماه‬                    ‫‪٤‬‏ غم و الذوه‬     ‫بر ورن شان‬        ‫راح‬ |  |  |                    ‫‪.‬‬   ‫ورناند‬ |                             ‫عگود‬    ‫چیو»
   ... ‪tûr‬‏ (خواحان دادن) اسشق ی‬                ‫‪۰‬‬ |  |    ‫ابرست تيخ‌نيزش‪ .‬اپری که فطر او خون‪.‬‬             ‫بحریست دست رادش " بحری که موج او در‬ |              ‫تش‬        ‫وراد‬ |                           ‫‪۳‬‬                 ‫‪= ۴‬رد(ھم‪.).‬‬               ‫‪ ۵‬معزی لشابوری ‪٩ ۹۳۵‬‏ ‪.‬‬ |   ‫)‬     
   ...  ‫ابرست تيخ‌نيزش‪ .‬اپری که فطر او خون‪.‬‬             ‫بحریست دست رادش " بحری که موج او در‬ |              ‫تش‬        ‫وراد‬ |                           ‫‪۳‬‬                 ‫‪= ۴‬رد(ھم‪.).‬‬               ‫‪ ۵‬معزی لشابوری ‪٩ ۹۳۵‬‏ ‪.‬‬ |   ‫)‬     ‫»ی‬‫ور‬ |            ‫دابی‬ |               ‫‪ 82‬ا(تزوا
   ...                            ‫«معزی لیشابوری ‪۹۶۳٩‬‏ ‪.‬‬ |                                                   ‫‪010۵۲‬‬    ‫رادیو ‪ -‬از فرانوی‬          ‫‪#‬‬ |                                                  ‫( بی‌سيم ‪ .‬پرتو مجهول ) ؛ ابزاری برقی‬ |                                                  ‫( ا
   ...  برقی‬ |                                                  ‫( الکتریکی) که سوت را ازفواصل دور ضبط‬ |                        ‫رادیو‬                                                      ‫‪ ۳‬مشش کند ‪2‬‬ |  |                                                                              ‫بقيه از صفحة ‪e‬‏‬ |     
======
leaf 387 contin-page None
   ... ك بسبزوار‪ -‬ونام پادشاهزاده‌ای هم بوده‌است‬ |                                                              ‫کوبند او را برادری بود که ری نام داشت هر‬ |   ‫امت که بوشیده ۽ بنهان ولهفته واسرار (‪ )۱‬دل‬ |                                           ‫باشد ‪.‬‬             ‫دو باتفاق شهری بنا کردند چون بانمام 
   ...      ‫دام‬ |                                                                ‫هر‬‫ميان هردو در‪:‬سمیهٌآن مناقشه شد چه ک‬ |  ‫راد یام‪ -‬با میم» بروزن موعنی بادبان‬ |   ‫است که رازبانه‌باشد ومعرب‪.‬آن رازبالج ات ‪۵‬‬ |                                                               ‫ان‬ |                         
======
leaf 390 contin-page None
   ...                                                     ‫ر‬ | ‫وبزرن کام‪ ۰‬شض وحش امت‬      ‫رام =‬                        ‫برادرپیاز‪ ,‬وآنرابربان کرده بخورند بفایت لذین‬ | ‫که الفت گرفته وآموخته وفرمان بردارباشد؟ ‪-‬‬               ‫باشد؛ وباین معنی با زای نقطه دار آهممده‌است؛‬ | ‫وهام روزییست وبکم است ازم
   ...      ‫عربان )‪ .‬پشتو ‪ 21182۲‬که ‪ ۷1000‬باکدرده محتملا ازفارسی‪.‬گرفته شده‪ .‬ماکلمة ابرانی‌باستان‬ |         ‫‪ 282۲#-‬راداريم کهشاید مرتبط باکلمۂ اوستابی ‪( 01۵۷2۲ -‬فضای باز) و (دشت) است(چنانکه‬ |                 ‫ماخوذاست ‪ ۰‬در بلوچی واستی ‪ 11821‬آمده ‪.‬‬ ‫در )‪ )2۲۵65۵۷2۲‬با از ‪112۷82۲‬‬ |     
======
leaf 391 contin-page None
   ...  نام شهرست که‬ |                          ‫خمة مترفهً سال ملکی ‪.‬‬                                     ‫آردشیر بابکان بکنراده بود ©‬ | ‫رامش حجان = بکررابع» تاماوابی‬                                   ‫رام بردیی = بمایم وبای‌ابجد وزای‬ | ‫است از ءوسیقی ‪ -‬و ناملحن هشتم است از سی‬                        
======
leaf 393 contin-page None
   ... زفره ی‬ |  |   ‫‏‪ . bérãbt . bérãwên . bérãw‬بهلوی ‪natînîydr‬‏ ‪ nhs)i(niyãT« . ۵81۷۵۲ ۰‬روشن‬ |  |     ‫ست‪ * .‬اسشق‪ :»۰۱‬کخرادرنج»ببرون کرد ‪-‬ن دکقردعنه اغراجبلدکردن‪ ,‬مرکدورددن۔‬ |  ‫‪ ۰‬اعتغال داشتن ‪;0D‬‏ هیچ حال ننده بدرگاه تباید وشفل وزارت براند که‬                 ‫ورزسن‬    ‫آوردن ك‬   ‫اسهال‬ |  | 
======
leaf 398 contin-page None
   ... اشد ‪ ۴‬که‬                                                                     ‫گفته‌اند ‪.‬‬ |  | ‫ازجااب هرموز آورند وآ نرادر گرسیر (‪ )4‬ماهی‬                   ‫ر بوله = بنتح اول وآخر که لام باشد‬ |  ‫ادنه گوبند وماهیانه اآنز‌پزند وهمجذان خشك‬                  ‫وثانی بواو رسیده" بلفت اندلس رستذیی باش
======
```


## [2026-09-04T23:16:38.574Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins ar-\"; grep -n \"^ar-\\|^arə-\\|^ar- \" AHD_watkins1985.txt | head; echo; grep -n -A18 \"^ar- To fit\\|^ar-$\" AHD_watkins1985.txt | head -40"
}
```


## [2026-09-04T23:16:39.097Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC\"; grep -n \"^ar-\\|^arə\\|^artos\\|^rādh\" IEC.txt | head -20; echo \"=== SYN scorpion\"; grep -n -i \"scorpion\" SYN.txt | head -5"
}
```


### [2026-09-04T23:16:40.716Z] TOOL RESULT

```
=== AHD watkins ar-
287:ar-. Also are-. To fit together. I. Basic form *are-. 1. Suf- fixed form *ar(g)-mo- in: a. Germanic armaz in Old English earm, arm: ARM}; b. Latin arma, tools, arms: ARM?2, ARMADA, ARMADILLO, ARMATURE, ARMOIRE, ARMY; ALARM, DISARM; C. Latin armus, upper arm: ARMILLARY SPHERE. 2. Suffixed form *ar(e)-smo- in Greek harmos, joint, shoulder: HARMONY. 3. Suffixed form *ar()-ti- in: a. Latin ars (stem art-), art, skill, craft: ART!, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA); b. fur- ther suffixed form ‘*ar()-ti-o- in Greek artios, fitting, even: ARTIODACTYL. 4, Suffixed form *ar()-tu- in Latin artus, joint: ARTICLE. 5. Suffixed form *ar()-to- in Latin artus, tight: COARCTATE. 6. Suffixed form “*ar(e)-dhro- in Greek arthron, joint: ARTHRO-; ANARTHROUS, DIAR- THROSIS, ENARTHROSIS, SYNARTHROSIS. 7. Suffixed (su- perlative) form *ar(g)-isto- in Greek aristos, best: ARISTOCRACY. II. Possibly suffixed variant form (or separate root) *dr-dh-. 1. Latin drdé, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINA- TION, INORDINATE, SUBORDINATE. 2. Latin drdiri, to begin to weave: EXORDIUM, PRIMORDIAL. 3. Latin or- ndre, to adorn: ORNAMENT, ORNATE; ADORN, SUBORN. III. Variant or separate root *ré- (< *reo-). 1. Latin réri (past participle ratus), to consider, confirm, ratify: RATE!, RATIO, REASON; (ARRAIGN). 2. Suffixed form ré-dh- in: a. Germanic *rédan in (i) Old English rédan, to advise: READ, REDE (ii) Old English réden, condition: HATRED, KINDRED; b. Germanic *rédaz in (i) Old High German rat (> German Rat), counsel: BUNDESRAT, RATHSKELLER (ii) Old English rédels(e), opinion, riddle: RIDDLE?. 3. Zero-grade form *ra- in Germanic *radam, number (see dekm). IV. Variant (or separate root) *ri-. 1. Suffixed form *ri-tu- in Latin ritus, rite, custom, usage: RITE. 2. Suffixed form *(a)ri-dhmo- in Greek arithmos, number, amount: ARITHMETIC, LOGARITHM. [Pok. 1. ar- 55.]
```


### [2026-09-04T23:16:40.778Z] TOOL RESULT

```
=== IEC
662:ar- (2) (radical) “join, fit. WP I, 73. Cf. år- (2), ar-nv-, arar- Skt. cf. mom: Arm. h-arem “join, fix’, fr. *en-ar-, cf. Gk. énara “arms, spoil, of ambig. origin; Lat. cf. arma ‘arms’; Ir. oirim (for *airim) ‘suit, fit
663:ar- (3) (radical) “do, make (same as ar- (2)?)
674:ar- (2) “join, tie'. Cf. ar- (2). WP I, 73 Oss. ar ‘shaft of cart’; OCS cf. jarímü ‘yoke’; Pol. po-jarzyć, v. ‘to join’
675:ar- (3), cf. ario-
678:ar-bho. Cf. ar (1), bhā (bho) Slovene jerbo ‘because’; Li. arba or
685:arədā, see ardā
686:arədhlom ‘plough, ploughshare’. WP I, 78. Cf. arātrom, aro, io (1) MHG arl; Austro-Ger. Arl; OCS oralo, ralo; Cz. rádlo *ploughshare'; Slovene orálo ‘plough’; ralo *ploughshare'; oral ‘acre’, ral 'arable field"; Li. arklas; Latv. arkls
717:ar-ne “indeed not’. Cf. ar (1), È Gk. cf. arnéomai; MIr. éraim, Ir. éaraim ‘deny’. (The vocalism of Arm. uranem ‘I deny’ is Obscure)
737:artos (1) ‘ploughed; ploughed field’. WP I, 78. See aro (1) Arm. art, o-st. ‘field’; art-, arta-, px. "out: Gk. cf. (deverb.) arotós ‘arable’; árotos “field, crop’; Lat. cf. (deverb.) aratus; OE eard (fr. *artós); yrp (fr. *ártis); OFris. erd; MHG art; Li. ártas; Latv. arts, pp.
738:artos (2) "done, made, prepared'. Cf. ar- (3), arar- Pehl. art, ard ‘wheat’; Per. àrd ‘flour’, Myc. Gk. ártos "bread:
739:artos (3), ios, us (beside adv. arti, arté) joined; adjoining; join’. Cf. rtos, rtis, -us, etc. WP I, 70, 71 Skt. cf. rtáh, rtám (adj. s. ‘right’, etc.); rtüh “fitness, rule’); Av. aroto ‘perfect’; Ober arta- ‘law, justice" (cf. the name Artaxerxes); Oss. (?) al (duty. Phonology as in müålin ‘die’, fr. mrt-); cf. also ard-àm ‘up to here’; ard- igài ‘henceforth’; Tokh. A. cf. argo ‘today’; Arm. ard ‘now’; arden must: ardi (adj. *mo- dern'. WSP -d- for -t- as in du 'thou'; da "het: Phryg. (Iranian?) cf. artádes ‘justices’; Gk. árti must: ártios; Hes. artüs; cf. also
14387:rādh- ‘show, tell, declare, speak’. WP I, 429 Olr. ro-radid, 3s. (speaks': Li. pra-ródyti 'in- dicate, suggest); Ir. rádh, pl. ráidhte, m. ‘speech, word, expression’; rádhaim, ráidhim, v. “speak, say’; OBr. cf. am-raud, s. ‘thought’; W rhawdd, m. 'clarity, perspicacity'; cf. ad- rodd, v. (tell, relate’: Li. at-Cródyti *appear); Go. rōdjan, v. ‘talk, speak’; bi-rodjan, v. *mur- mur’; ON ræða, v. ‘speak’; f. ‘conversation’; Li. ródau, yti, v. ‘show’; Latv. rādu, it, id.
=== SYN scorpion
```


## [2026-09-04T23:16:56.222Z] TOOL CALL #83: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/ardasir-i-general-index",
 "prompt": "What is the Old/Middle Iranian etymology of the name Ardašīr / Artaxerxes given here (Artaxšaça-, arta- 'truth' + xšaça- 'kingdom')?"
}
```


## [2026-09-04T23:16:57.990Z] TOOL CALL #84: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BFaqrab-",
 "prompt": "Give the Proto-Semitic reconstruction *ʿaqrab- 'scorpion': its descendants and any statement about its origin or root (is it derived from a triliteral root ʿ-q-r?)."
}
```


### [2026-09-04T23:16:58.379Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T23:17:00.284Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T23:17:04.448Z] TOOL CALL #85: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AF%D8%B4%DB%8C%D8%B1",
 "prompt": "Give the etymology of Persian اردشیر (Ardašir) — Middle Persian, Old Persian Artaxšaça-, components arta- and xšaça-."
}
```


## [2026-09-04T23:17:05.585Z] TOOL CALL #86: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D9%82%D8%B1%D9%8E%D8%A8",
 "prompt": "Arabic عَقْرَب: etymology and any mention of the root ع ق ر (ʿaqara 'to wound, hamstring'). Also list Semitic cognates."
}
```


### [2026-09-04T23:17:08.591Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T23:17:10.382Z] TOOL RESULT

```
# Etymology of Persian اردشیر (Ardašir)

According to the Wiktionary source, this name has an ancient pedigree:

**Middle Persian origin:** The term derives from Middle Persian *Ardaxšīr*, which itself came from Old Persian *Artaxšaçā*.

**Components:** The Old Persian form breaks down into two elements: *arta-* and *xšaça-*, which combined to create this royal name.

**Broader transmission:** This Persian term was subsequently borrowed into multiple languages. It entered Ancient Greek, Latin, and English as "Artaxerxes," and also made its way into Sanskrit as *ṛtakṣayarṣa* and *artakṣayarṛ*.

The name represents a remarkable example of linguistic diffusion across ancient empires and cultures, maintaining recognizable form across vastly different language families over millennia.
```


## [2026-09-04T23:17:30.012Z] TOOL CALL #87: Bash

```json
{
 "command": "for u in 'https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AF%D8%B4%DB%8C%D8%B1'; do python3 tools/fetch_source.py \"$u\" --note 'page 61: Persian Ardashir < OP Artaxsaca-' 2>&1 | tail -1; done; ls site/pages/61.jpg 2>/dev/null; pdftoppm -f 61 -l 61 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg61 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg61.png"
}
```


### [2026-09-04T23:17:32.710Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2bde84e9ebffae8f.txt
site/pages/61.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 95078 Sep  4 19:17 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg61.png
```


## [2026-09-04T23:17:35.345Z] TOOL CALL #88: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg61.png"
}
```


### [2026-09-04T23:17:35.817Z] TOOL RESULT

```

```


## [2026-09-04T23:17:35.815Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-04T23:18:22.062Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT\"; grep -n -i \"alakran\\|alacran\\|akrab\\|'aqrab\" LKT.txt | head -10; echo \"=== RCH\"; grep -n \"aqrab\\|'akrab\" RCH.txt | head -5; echo \"=== TAD/AFM\"; grep -n \"عقرب\" AFM.txt TAD.txt ARB_mo3rb.txt 2>/dev/null | head -8; echo \"=== FVQ\"; grep -n -i \"aqrab\" FVQ.txt | head -5"
}
```


### [2026-09-04T23:18:22.166Z] TOOL RESULT

```
=== LKT
320:47.  Ar.  'akrab:
321:'Skorpion'.  Hieraus  sp.  alacran  'dass.' [mit  ar.  Art.  und  Änderung  des  Schluß  b in  einen  anderen  Konsonanten,  vgl. dazu  z.  B.  Calatayud  aus  ar.  KaVat Ajjüh  'Hiobsburg';  Zocodover  (Baedeker, Spanien  u.  Portugal.*  Leipzig  1912. S.  135),  Hauptplatz  in  Toledo,  aus  ar. sük  ad-dawib  'Tiermarkl'] ;  pg.  alacral, alacräo,  lacräo  'dass.'.    [DE  53.
2445:'Herz';  kalb  al-asad  'Herz  des  Löwen', hieraus  der  Sternname  Kalbehasit  'Re- gulu.s'.  Aus  kalb  al-'akrab  'Herz  des Skorpions'  wurde  Kalbolacrab  a  Scor- pionis,  d.  h.  Antares.  —  Devic  DEt  42.
5069:'ain  38.  402.  1994 'ajjük  41 'akär  43 akbar  121 "aMda  44 'akika  45 'äkir  karhä  46 'akrab  47 'äla  559 'alaka  904 'alam  53 'a/^'  57 'a^iw  2131 'aZiwa  2008,  2131 'alkam  58 a?;i?Ä  59.  1986
9796:arfor  501 adraja  485 aduana  526 aduar  502 adufa  538 adufe  537 agengibre  1930 oguajaque  2168 aguanafa  1535 ahorrar  886 ajarafe  1840 «;e&e  1735 ajedrea  1872 ajedrez(atama)  1871 ajimenez  1815 ajimiz  1816 ajonjoU  744 ajorca  1951 ajovar  1959 ajuar  1959 alabarda  823 alabega  761 alacena  871 alacran  4:1 alafia  24 alahilca  904 alamar  67 alambar  78 alambique  79 alambre  78 alameda  1364 alamud  72 alancel  1428 alaqueca  45 alarbe  89 alarde  94 aZaWf^o  59  d.  100 I  alarife  99 alatar  134 alazan(o)  870 albacea  2158 albaheca  761 «Zöate  226 albanilear  216 albanal  204 nlbanar  204 albani(r)  216 albanil(esco)  216 alhaqida  188 albaran  226 albarazo  224 ffife«r(/a  228 albardän  241 a/fcarrfi  dial.  242 albardin  242 albaricoque  247 albarrada  249 albarrän  251 albarrana  251 albarraz  762 albayaldar  6 albayalde  6
=== RCH
=== TAD/AFM
AFM.txt:580:( 5 4 0 ܝ( تنفع من لدغ العقرب ܣ 
AFM.txt:582:2 من لدغ العقرب يقال له بالعر 032 ومفرح القلب > 0 بيك 
AFM.txt:2578:تعريب دَرَونك ٠‏ ويقال لها 22 « جبان اولى وعقرب اولى » ٠‏ وهي عقر ܬ ب الكل 
AFM.txt:3010:(الشغك) فادسق ححض وقو العقرب 
AFM.txt:3992:(الشتدع ) العقربٍ«الداهية مركب من شب اي ليل ومن دعا 5 
AFM.txt:4022:+ (الشّأة ) العقرب ساعة تولد وقيل عقرب صفراء تعريب شيبا وهي الأننى 
AFM.txt:4263:قرين الليّة ܝ احدهم ܐ وطعنة بالعقرب وأتوا بها عند انوشروان 
AFM.txt:4265:العقرب ٠و‏ بعد سنة في نفس اليوم الذكور ظهرت ثانية تلك الّة وفي فها قليل 
=== FVQ
```


## [2026-09-04T23:18:23.686Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index\"; grep -n -i \"ARASTAN\\|ARAY\\|ORDIBEHESHT\\|ARD\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -15; echo \"=== ARY fa\"; grep -c \"آراستن\" incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-04T23:18:23.744Z] TOOL RESULT

```
=== ARY latin index
115:cabal 9 ba gbgb5 Saray DE pol obey got tet 2 2F hay) eh
343:got eahsls ab DU3 cal BF Gels cals yl gta OUT jl Saray abs
1095:SLgI OW 4 ae GSM! 22 wlsal yea pay jNed 39 gil Saray DS So oye
1398:RATEN H(GERMAN) aT ARASTAN (PAHLAVI) 5 shy
2913:BREME, BARD ARMENIAN) 5+)
3076:OLD NORSE) Sp,  VARD (PAHLAVI) 5
3110:WILLA, WELLA VARASA, VARAYATI, VRTA, VRNATI
3151:SAEs ges} sadly 2 oot gard
3429:‘REFERENCES be theg BEREM, BARD —(ARMENIAN) gu!
3554:ward MEV a set ga so Sil "ge Si et gt 3
3901:BS ean AS AST aap gy Seglig 9 a Sate yo 05ly gal gard
4257:(PARD) 757, (LEOPARD) 589] | PRANG AFGHAND) (4) gil
4258:MACKENZIE: (LEOPARD) 121 PRDAKU (SANSKRIT) 2 Suite
4260:(PARD) 651, (LEOPARD) 523 PARDUS (LATIN) ys
4262:(PARD) 429, (LEOPARD) 337 PERDE (OLD ENGLISH) aS Ji
=== ARY fa
0
```


## [2026-09-04T23:18:30.268Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1385,1410p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== find pdf page tag\"; awk 'NR<=1400 && /\\[pdf page/{p=$0} END{}' incoming/ARY/ARY_latin_index_pages.txt; grep -n \"\\[pdf page\" incoming/ARY/ARY_latin_index_pages.txt | awk -F: '$1<1400' | tail -3"
}
```


### [2026-09-04T23:18:32.344Z] TOOL RESULT

```
REFERENCES beh ADUR PAHLAVI) 5 shy
0) a) Acar (KURDISH) «52,5
BARNHART: (IGNEOUS) 506 AGNI, AGNIS (SANSKRIT) cy Suite
DELAMARRE: (LE FEU) 182 IGNIS LATIN) ys
MACKENZIE: 5, (FIRE) 114 HOLD CHURCH SLAVIC) 45g sl
BUCK: n OGNT ,
ONIONS: (IGNEOUS) 461 OHEM AARUSSIAN) yu
SKEAT: (IGNEOUS) 286 OHEN CZECH) Sy
RAMAT: tT OHEN (SLOVAK) 51 yLah
OPES VY 9 VY (2S): abi olny UGNIS -(LITHUANIAN) gly)
leadloal
tage Aa "GAT YL oda ool GU olay 24h adem
RATAN ARADH, -RADH —«(AVESTAN) pl 3\
RATEN H(GERMAN) aT ARASTAN (PAHLAVI) 5 shy
RADAN, (OLD ENGLISH) oS gS! RADHNOTI, — (SANSKRIT) cy Suse
REDAN, RED RAHYATI, RADH- esa x
READ HENGLISH) 1S) PERI LATIN) oa
(TIL)RADE DANISH) Sails GAREDAN, REDAN (GOTHIC) eng
RADEN (DUTCH) fiche (OLD SCANDINAVIAN) :pSS-e\
(OLD CHURCH SLAVIC) p53 +l RADHA
RADITI OLD HIGH GERMAN) iS galt
[pdf page 52]
- . os
OF | deal ipl eal eal To
REFERENCES both, RADIETE (RUSSIAN) 525,
POKORNY, ——Ss=S—*~=<CS~S~S*~«~ OO RADIT CZECH) Sor
=== find pdf page tag
1333:[pdf page 49]
1351:[pdf page 50]
1381:[pdf page 51]
```


## [2026-09-04T23:18:40.890Z] TOOL CALL #92: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B4%D9%88/",
 "prompt": "What do Dehkhoda and Farhang-e Mo'in say about the Persian word اشو (ašu)? Give the definition and any etymological note (Avestan ašavan?)."
}
```


### [2026-09-04T23:18:51.045Z] TOOL RESULT

```
# Persian Word اشو (ašu)

## Dehkhoda Dictionary

According to Dehkhoda, اشو is "مخفف آشوب" (an abbreviation of āšub). The entry notes the word appears primarily in compound forms, and its independent use depends on finding additional evidence. Dehkhoda also records an Avestan/Pahlavi origin, stating it means "بهشتی" (heavenly/blessed), contrasting with "دوزخی" (hellish).

## Farhang-e Mo'in

Farhang-e Mo'in provides a more concise definition: "مقدس، پاک" (sacred, pure).

## Etymological Note

Multiple sources reference Avestan origins. The Dehkhoda entry notes: "بلغت زند و پازند بمعنی بهشتی باشد که در مقابل دوزخی است" (In Zend and Pazend it means heavenly, contrasting with hellish). User submissions further elaborate that اشو derives from اشا/اشه (ašā), representing cosmic order in Zoroastrianism, with the root potentially connecting to Proto-Indo-European origins meaning "proper" or "fitting."
```


## [2026-09-04T23:18:55.958Z] TOOL CALL #93: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A7%D8%B4%D9%88/' --note 'page 61, root Ar/Are node 6: Persian ašu in Dehkhoda/Moin' 2>&1 | tail -1; sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-04T23:18:59.974Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/58b2a75f15a4910a.txt
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


## [2026-09-04T23:19:03.558Z] TOOL CALL #94: Bash

```json
{
 "command": "sed -n '80,160p' tools/verify_check.py"
}
```


### [2026-09-04T23:19:03.613Z] TOOL RESULT

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


## [2026-09-04T23:19:29.938Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nimport re\nd=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(d):\n    if 'عقرب' in l:\n        m=re.search(r'\\[pdf page (\\d+)\\]',l)\n        j=l.find('عقرب')\n        print('idx',i,'pdf',m.group(1) if m else '?', '::', l[max(0,j-200):j+300].replace('\\n',' | '))\n        print('---')\nPY"
}
```


### [2026-09-04T23:19:34.241Z] TOOL RESULT

```
idx 22 pdf 23 :: ‏ | ‏بر اثر او برفتند بکنار چاهی رسیدند . مار بر | کنار چاء حلقه زد (۱) ‎AIT.‏ بدرون رفت وبر | ‎aT‏ . چون درآن چاه دگاه کردند ماری دید لد | مرده افتاده وعفربی لیش برو بند کرده » لیزهء‌ای | ازبالای چاه برپشت آن عقرب فرو بردندوهه‌چنان | پنزديك مك آوردند , واز حال هار ولیشعقرب | ملك راآ گاه گردانیدند . چون یکال بگذشت | ‎e‏ در آن روز ملك شسته ‎ay‏ ودیوان مظالم | می‌پرسید (۲) 6 همان مار بنزديك‌سربرملك آمد | و از دهن خود قدری تخم ‎clam‏ بریخت وبرفت. | ‎SS‏ فرمود آن‌نشم را کاشتند » ازآن شاب | اسپرغم بر آمد و انوشیروان پبوسته 
---
idx 43 pdf 44 :: راگوبند - و دو چیژی (۱) را لیز | شتر گربه کوبند که در غابت بلندی و بستی | و کوچکی ویزرگی باشد. |  | ‎OE se‏ - معروف است ۰ و آن | مرفی‌باشد شبیه بشتر وعربان نعامه خواننه ‎٩‏ - |  | ‏شتر مود « کوبنددرجنگلی ازجنگلهای | عقرب زمین درختی هست که برکهای آن | کارا کیر میکند و در آن جنگل مورچة ‎“pb‏ | ‏میباشد ببز رکی بزغالةً بزرکیو ‎DLS‏ کوچکی. | کی که پدان جنگل در آید مورچگان بدو | آویزند و دريك لحظه پاره پاره‌ا شکنشد, |  | ‏شتر ‎CS‏ = بر وزن (۷) ‎kes‏ » اقسام | غله راکویند که بهم آميخته باشند واکر ازآن | آشی ‎ate‏ آن آش را آش شترنجی (
---
idx 130 pdf 131 ::  . ام ولایتی است ازملك فاری. |  | ‏0( چك : - است. |  | ‎٩‏ -۱کتون 510۳0260 تلفط کنند .,رآن شپربت بفاری بطول. 4۸ وعرض ۳۰ کیلو | متر » از شمال محدود بخفرومیمند واز مشرق ببلوك جهرم و از جنوب یلو ‎sb‏ وکارزین و از | عقرب بچپار ناحیه ۰ آب و هوایآنکرم و زمین ‎OT‏ پرآب و دارای میوه وم ر کبات وبرنج‌است | چمیت آن ۱۰۰۰۰ تن وم کزش «دوره» و۳۷ قربه دارد. « کیهان . جفرافیای طبیمی ۴۲۳۵. | 
---
idx 139 pdf 140 :: دد | چوب است که آنرا باحاقه‌های آهنین تعبیه ‎oS‏ | ‏بهم پیوسته اند و شاطران بردست گیرند ومرغان |  | طبع کافوری | است ۴ ‎OT.‏ عیوه‌ای باشد دوابی‌شبیه‌بسنجد.* | طبر به بر وزن حنفیه ۰ شهری‌است |  | در ‎le‏ مقرب . گویند عقرب درآن شهر بیار | ‎e‏ |  | طبطو ۱ » ‎sb‏ حطی بروزن بدبوه |  | لام لوعی از مرغانی باشد , |  | طبع کاقوری «کنایه از مزاج سرد |  | است |  | و جالوران را بدان زاند و شکارکنند - ورنکه | سرخ را ‎ys‏ گفته‌اند ‎ F‏ ویمءتی عناب یز آمده |  | و خشكاست (۲)-ر کنابه‌ازمردم کند ‎hs ab‏ | وبارد وبخ سته‌هم‌هست_ و ‎eather pager go HOLS‏ |  | (۱) چ
---
idx 170 pdf 171 ::  پهلوان ۰ دوابی است که آبرا | ‎ints‏ الطحال خوانند ۵ ؛ و بمسی گونددوابی | است که ‎(YT‏ بشیرازی زنکی‌دارو خوانند؛وبعضی | ‎aay So‏ بخ کبررومی است ۰ الاعلم. |  | ‏عقر بخا نه کنابه از سوز ‎Olu‏ | ‏وانگشتدان باشد . |  | ‏عقرب زلوفری کنابه از برچ | عقرب است » و آن برج هشتم باشد از بروج |  | ‎- ٩ ‏قلکی‎ |  | ‎. ‏چش: باه‎ (x) | . ‏چك : بارا‎ )4( |  | ‎Tanke ‏چش:‎ )۱( |  | ‏(۳) چك: وها . (ه) چك : |  | ‏۱ - رك. منتپی الارب : عفراو . ؟ - (عر) «عفة ‎pall,‏ (وتشدید دوم) باقی شیر | دریستان - و گنده پبر- رماهبی‌است بی پشیز کوچکه مپیدرنگ . مطبوخ ‎Uta O
---
idx 228 pdf 229 ::  . | ‎GL gly cab‏ است ک هگل ‎OT‏ مانند سوسن | ‎pts‏ آن میاه ببزرگی عدس میباشد و چون از | زمین بر کتند زرد میباشد و بسد ازآن‌سفید گردد | ویوسته در تلپای ‎ME‏ روک . ‎Sy‏ و تخم وگل | آفرا بکوبند وبباشامند. کزندگی عقرب و رتیلا | را فافع بود . |  | ‏فالود ‎ee ٩‏ بروزن فابود , معرب | پالود است که ماضی پالودن باشد بعنی صاف کرد |  | ‏(۳) چش : فالرفی . |  | ‏۱ - رك : فافره . فاغیه . « فاغر . قبل انهاصل.النیلوفرالهندی » « عقار ۳۰۷ ۰ . | نام عریی این دارو عموماً صورت منت « فافرة » ( دهان باز ) نوشته میشود و مابرهوف کمان |  | ‏میبرد که «ف
---
idx 295 pdf 296 :: اصلی باشد - | ویکس اول نام شاعری است ۴ . |  | قندر سك بقتح اول ودال ابجدورای | قرشت و سکون ثالی وسین بی نقطه وکاف. نام | شهربت از ‎OY,‏ استراباد ۵ . |  | فندق 1 - بن اود و ثالك و سکون | ثانی و قاف » معروف است. گویند عقرب از آن | میگریزد ۰ ‎Si‏ مغز آنرا ‎poll‏ وسداب‌بخورند | زهرکار نکن » و معرب ‎Gay OT‏ باشد و آنرا | فندقه نیز گونند - و کنابه از لب ‎Sete‏ هم | هت ۷ ‎Ar)‏ |  | فندق ردن - آن باشد که دست‌چپ | را مشت سازند و سرانگشت سبابةً دست راست | را بنوعی(4) درمایین انگشت سبابه ووسطای‌دست |  | 0 خم۱: + ودروغ ۰ | (4) خم۳ : نوعی . |  | ۰ ‏
---
idx 298 pdf 299 :: بلم | جشنهای عظیم تماند و شادی کنند و آترا جشن | ‎Wary‏ هم میگوبند و ‎OT ope‏ فوررجان | است . | قوددیان ۴ با ‎de sh‏ » بروزن | ومعتی فوردگان است که پنج روز ‎OT AT‏ ماه | با خسة مسترقه باشد و آفتاب درآن ایلپدربرج | عقرب میباشد» ‎OT,‏ ایام جشن فارسیان و مضان | است . |  | ‏فوددین ه بفتح اول و ثانی بروزن | تبرزین » ‎se‏ فروردین است که ماء اول سال | شمی‌باشد ؛ وطم اول بروزن‌پوستین‌هم آمده‌است. |  | ‏(۱) چش : بکس . |  | ‏۱ - بمناست ‎SOT‏ پادشاه قنوج را « فور » میخواندند . |  | ‏پوربان . | وفروردیان + | ۱ - دختر رای هند فورک نام |  | ‏۴ = پروردگ
---
idx 323 pdf 324 :: مرنگه | .است و بوی صبر از ‎oT‏ میآید . بهترین ‎OF‏ | ‎uae‏ و فربه و تازه باشد بعدازآن ‎the‏ و سبك | و هندی »گرم و خشك است در چهارم وسیم(۱) | و فاید ‎oT‏ بپار است. اگريك درم با شراب |  | ‎ceil‏ بخورندکزندکی افعی وعقرب ومجموع | کز ند کانرا نافع است |  | ‏قسطل ۴ © بم‌اول و ثالث و سکون | تانی و لام » ‎cab‏ رومی شاء بلوط را کوشدوآن | را ‎ew‏ بلوط الملك خوانند . |  | ‏خظین * - بسن اول و فتح الث |  | ‏وطای حطی‌بروزن‌پرتمکین»نام‌شهری است مشهور | از ملك روم بنایت‌عظیم بنام بالی‌آن شه رکه‌پسس | هرقل پادشاه روم باشد و آبرا فطنطنیه لیز | ‎Vas
---
idx 357 pdf 358 :: ئیات | ‎ahs‏ بی‌بهره‌باشد - و کنابه ازمرده ومیت (۱) | آدمی‌هم هست - ومردم گوزپشت رانیز گوبند. |  | ‎OF‏ درو یشان ۴ - اکیرسایر۱ | کوبند ‎Mar SF‏ چهل وهشت‌سورت فلکی‌است» | وآن هشت ستاره ‎ash wth‏ تاجی متصل‌بمیزان | وعقرب . |  | ‏کاسه دود - نام رودخاه‌اییت فیر | معلوم ‎٩‏ . | کاسه سر نگون = کنابه از مردم | صاحب همت و جوانمرد ‎ath‏ وبکسرهاء کنابه | ازآسمانت . |  | ‏کاسه شیاه ۷ » پیمنی سیاکانه‌انت | که کنایه از مردم سك و ‎ate‏ وگرفته )4( | وکاسه سیه نیز گوبند . | کاسه شدن ‎ale‏ از کوشیدن ‎Fy‏ | ‏لمودن باشد - وبمعنی کوزشدن وخمیده گردیدن | ى
---
idx 380 pdf 381 :: وافام | آن درک و کرد مذ کور میشود = و زر خالص را | نیز گفته‌اند . عربی‌است |  | کیست © بفتح اول وثانی بروزن ‎oS‏ | ‏رستنیی‌باشد تلخ شبیه بدستنبوی که بعربی‌حنظل | وبفارسی خربزهتلخ گویند؟ . و ‎aah‏ چارموضع | شخصی را عقرب گزید دو درم حنظل بآن شخص | دادند تا مخورد. همن که خورد درد بررطرف شد. |  | (۱) خم۱ : خنس |  | . ‏(هم)‎ b= ۱ |  | رو اس |  | اکر حنظل را بمقدار ‎ety‏ ناختی سوراخ کنند | و پراز دوغن زبق ‎Wik‏ و سوراخ ‎LT‏ باخمیر | محکم بگیرند و بر بالای آنش نهند تا جوشی | چند بزند و بعد از ‎OF‏ بردارند و برموی سفید | مالند سیام کند. ‎oly‏
---
idx 404 pdf 405 ::  دای نو ‎LS‏ | ‏+رودکی . ج ۳ ص ۱۰۵۹ > | ۵ - کرباسکه ‏ کربانو  ‎MAS ESR Se SOUS‏ | کرپاشه ‏ کربایس ۳ کربایش ‏ کربی < کریش ‏ کرفش ‎tbe‏ ؛ در اوستا ‎kabrpu‏ | ‏در پپلوی ‎karpu‏ . | . ۱ - مبکند هم نپنگرا رامو "مره عقرب بود زکرباسو ۰ آتری طوسی « فرهنگه نظام >. | ۷ - رك : کریاسو . ۸ یکی از ‎Las OLY, oly‏ فاری بطول ۷۲ وعرض | ‎Vo‏ کیلومتر ۰ از شمال محدود است بارسنجان وه‌رودشت و از مشرق بدريلچة بختکان وازجنوب | ‎Oey‏ و از مغرب ‎Lage‏ شیراز , جمعیت ‎OT‏ ۱۵۰۰ نن و دارای ‎٩٩‏ قربه است « کیهان. | جفرافیای سیاسی ص ۲۶۱ ). ‎٩‏ -
---
idx 417 pdf 418 :: شاء مخاط یکه ‎Bae‏ چشم را ‎UCL‏ متصل‌سازد . ‎A‏ < کرمانتاهان, ناحیتی‌است‌درمفرب | ‎ol!‏ . از شمال محدود بکوههایی که ‎ge We‏ رود دباله و گاماسب میباشد و آزمشرق‌بکوههای | کنکاور و از جنوب بکرههای کلهر و از عقرب بخا که عراق , و تفیمات حکومتی آن ساب | ازینقرار ‎LL SN: oy‏ وحومه ۲ سنقر وکیائی ۳- ‎Ole‏ دربند و بالا دربند و زیر دربند | ۶- دینور و کنگاور ‎-٩‏ ماهیدشت وهارونآ باد و فیروزآ باد ۷ سحنه ۸-کرند 4- زهاب | رقصر *۱- هرسین ۶ کیپان . جفرافیای سیاسی ص ۵۷-4۵۱ » ‎Ay‏ : کرمانشاه . (س2۱۹۲۹). |  | ‏۵ کرم - ‎JG‏ پهلوی
---
idx 430 pdf 431 :: ون ؛ داروبی است که | آنرا عاقرفرحا خوانند. قوت‌بامدهد؛ وباطای‌حطی | م‌آمده است. |  | ‏که خاطران « کنابه از مردم‌ناموزون | ‎o>‏ طبیعت باشد . |  | ‎vo ‏دال ابجد بروزن‎ be APO | UsT ‏جانورست کزنده و‎ | ‏ونام‎ - SS ‏بعربی‌عقرب‎ |  | ‏یکی از دوازده برج فلكهم |  | ‏مرفان باشد و بعریی حوسله کوبند ؛ و باین | معنی در فرهد هنگ جهانگیری ‎SEL‏ و زای‌فارسی | آمده است, اطاعلم ۱ -وبقتح اول بمعنی پاره | باشد که از دربدن است- وامرباین‌معنی هم‌هست | ‎te‏ پاره کن . |  | ‏کار یهن = ‎Sieh‏ بروزن‌تراشیدن, | بععنی پاره کردن و دربدن باشد . |  | ‏کر آغخا ۴ - با غ
---
idx 431 pdf 432 :: د که ‎fay‏ گر کین مالند- وسواد | زرگربرا یز کفته‌اند . |  | ‎ath ‏بر وزن فلك » آهنی‎ IT | ott ‏بدان فیل را‎ GULLS ‏و دستهدار که‎ or | Ye ‏و چوب‎ -٩۴ ‏جانب که خواهند برند‎ |  | ‏۱ - مسحف «کرژدم ‎oe‏ © (رك: رشیدی) ‏ عقرب ‎ole‏ . شاهد « کردم جراره» در |  | ‎bein‏ قبلح۹آمده . یاقوت درمج‌البلدان درذ کر «اهواز» وید : « وللك کثرت بسوق‌الاهواز |  | ‏الافاعی فی‌جبلهاالطاعن‌فی‌منازلهاالمطل علیهاوالجرارات فی‌بیوتها ومنازلها ومقابرها ولوکان فی‌العالم |  | ‏شیءشر من‌الافاعی والجرارات موهی عقارب‌قتالة تجر ذنبپا اذامشت لاترفعه کماتفعل 
---
idx 464 pdf 465 :: al‏ هند » قنای‌ستیرکونند فقط. » «چك | ‎kalba. A‏ , ۵۱8 , سک « ‎Gy‏ ۱۱۲ * قس:عرییکلب. | ‎ *‏ کربانو ‏ کربنو ‏ چلیاسه ‏ کلبو . | دشمن مار ها ‎oy‏ راسو . | آ ری طوسی « رشيدي ‎٩‏ . |  | ‎Ho OWN | . ‏فپرمت ولف‎ 8 | ‏همچو عقرب عدوی کلباسو‎ |  | ‏کلپ م رك :کلب . | 
---
idx 465 pdf 466 ::  (x) |  | ‏(4) چش :- است | - از کار ‎jb‏ مانده . |  | ‏۱ - (عر) «کلبتان بالفتح, ابور آهتگران » « منتهی‌الارب > . | - او تراک ی کفتکاین کلبتره ها را جمع کن | ‎IL‏ لازم شود چندین شکایت گستری . |  | ‏۴ رك : کلباسو : | همچو عقرب که کلسو بیند |  | ‎. ‏عجم » قس : کلبه‎ aly « ‏کليك‎ mF |  | ‏آنوری ابیوردی «رشیدی» «فرهنگه ‎ells‏ |  | ‏قبل از ‎Vaal‏ همی رود از خود + | آذری طوسی « رشیدی» « فرهنگه‌نظام *. |  | ‏د = کربه , از پهلوی ‎=o kurpak‏ ارمنی 6۲826 ( کارخانه ‎Obs.‏ » میخانه) | « هوبتمان ‎CANE‏ معرب آن‌کریق » 5.3 ( 0.73 , ۳۳6۳۷۵۳۵6۲ ‎Say ) 
---
idx 475 pdf 476 :: م ) . | شکته ) « علی‌اسفر فقیهی ۰ . |  | ‏شرف شفروه « رشیدی *. |  | ‏کلوخح خشکه را مالیده بر لب. | جامی « فرهنگه نظام »۰ |  | ‏© = کلوز در ‎ing‏ قمی 21022 ( کوزء ‎oles‏ |  | ‏1 کلوس (و) کژدم وچپ شوره پشت وآدم گیر | مبار و عقرب و چل سم سفید و کام ‎ham‏ . | ‎Jas‏ رشیدی در «چل» ورك : فرهنگه نظام + | ۷ - مت م کلوك خر افشار و کنگه ختك سپوز | حرامزاده و قلاش و رن عالم سوز + | سوزلی سمرقندی فرشیدی» وه فرهنگه نظام >. | 
---
idx 518 pdf 519 :: IS‏ - ینم حر درتاف وسکون | هردو ‎aly‏ مجهول و رای قرشت » بمعنی غلیواج | باشد که مر گوشت‌رباسته و ‎IT‏ بعربی‌حداة | بکس حای بی‌نفطه خوانتد . کوند اکر ‎Bes‏ | ‏آنرا خشك کنند و با آب ‎Jo‏ سازند چون کسی | رامار با عقرب کزیده باشد اکر زخم در طرف | راست باشد سه میل ازآن بچشم چپ و اکر در |  | ‏(۱) چش ‎JOS)‏ باعاف فارسی . |  | ‏۱ - رك : رشیدی. |  | ‎AVS |  | ‏طرف چپ باشد ‎pte‏ راست کشند البته خلاس | ‎ak‏ | ‏کود گیاه ۲ - بنتح اووننی‌وسکون | ثاث و کسر ‎GE‏ فارسی و تحتانی بالف کشیده | وبهای زده » درخت و میوه و بارکور است که | ‎LT‏ بعربی خرنوب 
---
idx 609 pdf 610 :: [pdf page 610] | one males |  | ‎a‏ » بنتح اول و کسر ‎gE‏ (۱) بر | وزن یزید » مای گزبدن است ‎٩‏ خواه عقرب | وخواه مار و خواه کسی بدندان بگزده با شخصی | سخن‌درشتی بگوید - وبمعلی هدیبه ومعفه‌ورتوت | و پاره ومالی که اژرعایا همه سال میگیرند ۱ - | و زری که از کفار ذمی میستانند هم هست ۷ - | ویضم اول, یعنی اختبار کرد و پسندید و برچید | و انتخاب لمود و بز رکه ساخت ۷ - و پسندیده | و کزین رده شم را هم ‎SS en‏ | ‎a= Vast‏ نا
---
```


## [2026-09-04T23:20:38.731Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'PY'\nd1=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,t in enumerate(d1):\n    if 'اشو' in t and 300<i<420:\n        j=t.find('اشو')\n        print('leaf',i,'approx printed',i-215,'::',t[max(0,j-400):j+600].replace('\\n',' | '))\n        print('---')\nPY"
}
```


### [2026-09-04T23:20:40.642Z] TOOL RESULT

```
leaf 358 approx printed 143 :: اشو ی | که کمانگران بر باژوی از جابدر رفته ‏ بندند | واشق معربآشت . | اشتاف مامثا بنتح اول و کسرفاه | یعنی عصاره مامثا ومامیئا بلغت سربانی‌نام رستنی | باشد که آنر! درفااضات بکاربرند وآنرا زهبانالی | که درئواحی موصل میباشند سازند . درد چشم | و ناقم افننت. ‏ | اشیهه - بفتح اول وکسر‌انی بتحانی. | رسیده و های مقتوح » آواز هو شيهه اسب را | قز بر 9 | هم حست خوشبوی که آنرا دواله میگوینه | وبعربی شبیه‌السجوز ومكك‌القرود خوانند» مانند | عثقه ولبلاب بردرخت یچد و اکر بسایند و ور | چشم کشند چشم‌را جلادهد. *# | اشو۱ بفتح‌اول وضم‌ثانی بواو رسیده, | بلخت زند ویازند (۱) بمعنی بهشتی باشد که در | حقایل دوزخی است ۷ | اه ۳ ی یی | شوع < بضم اول بروزن 
---
leaf 361 approx printed 146 ::  ‌ َنح اول,قلف سحتا سدكهه | بلفت بونانی؟ ترکیبی است کهآ نرا بغارسی پخته | جوشانیده‌اند ومیفختج همان است » وبکسر اول | نیز آعده شتگن « | اغول ه بر وزن ملول » از روی خشم | وفهر بگوث؛ چشم نگریستن باشد . | اغیرس < بنتح اولوثانی‌بتحتانی رسیده | و کسر رای قرشت و سکون سین سعفص ؛ جوز | رومی است و آن بار درختی باشد که صمغ آن | کهرباست ؛ و بعضی گویند چوب آن درخت | کهرباست . | اغیسی ‏ بروزن نفیس , نخمی اس ت که | آنرا بشیرازی تخم دلاشوب کونند » و ری | افتاد جنم اول بروزن استاد ۰ بعنی از | بای درآمد - و کنابه از دور شد هم هست که | ماضی دورشدن است . | افتاث گان » کاب از مظلومان | ویر بشان شدکان‌باشد .3۶ | افتاده ممعثی عاجز و سقط وخراب | که و ژبرن گردننه باخد.. | اقتال ‏ یک راون بروزن اقبال . به‌عنی | برا گنده وباشیده - وشکاقه ودریده باشد . | افتا ليفن « بکراول مصدر افتالاست | که بمعنی پراکندن و یائیدن و افشاندن - | وشکافتن ودربدن باشد . | افتان و خیز ان - کنابه از آحته | ودیر براه رفن باشد . | افقد - بنتم اود و کسر الث مر وژن | محجد ؛ و بمعنی ستاننده و متایش. کنده. باق ت | وبععنی شگفت وعجب ونعجب هم‌هسته . | افتدستا - کلمه ابیت مرکب از افتد | ستایش‌عجب وئیکوتری
---
leaf 382 approx printed 167 ::  بته | شده را کومند ۷ . | | ثیسقه - بر وزن برجسته ,هر چي زکه | آن بته و سخت شده باشد و بدشواری وا شود | و حل گردد - و شبر و ماست و خون بستهرانیز | گوبتد ٩‏ . | اثبله - بنتح اول و الث بروزن‌حنظله, | تمر هندی رأگویند و بهندی ابلی خوانتد ۰۷ | انیمی ۸ س بکسر ثالث وقتح میم‌بروزن | صف‌شکن , بلفت زند و بازند (۳) انگور باشد | و بعربی علب گویند . | افیق یه - بروزن میغوب . فرش وساط | و گتردنی را گومشه. : | اثبو 4 - بر وزن منصوبه . ماشوره را | گویند - و وله آشابه و مانئد آنرا نیز | کفته‌اند . | ۴ - پهلوی ۵:۳۰98۵1, 20۵۵2۵۷ | ۲ | ۴ ات ود اون | ت۱۳ تم ستد. | ۸ حز2(8021130),
---
```


## [2026-09-04T23:20:49.643Z] AGENT

Now I'll write the verification file.


## [2026-09-04T23:29:02.081Z] TOOL CALL #97: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build61.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 61,\n \"book_page\": 31,\n \"verified_by\": \"claude-fable-5-1\",\n \"verified_on\": \"2026-09-04\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"A.q.r\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Proto-Semitic *ʿaqrab- 'scorpion' (a primary quadriradical noun); Arabic ʿ-q-r (ʿaqara 'to wound, hamstring, cut the hocks of') is a real root but is not demonstrably the source of the noun\",\n   \"note\": \"The word is real and the meaning is right, but the ROOT BOX is only half right. Comparative Semitics reconstructs *ʿaqrab- as an inherited quadriradical animal name (Akkadian aqrabu, Hebrew ʿaqrāḇ, Aramaic ʿaqrabbā, Syriac ʿeqqarbā, Ethiopic ʿaqrab beside metathesized ʿarqab) and does not analyse it as ʿ-q-r + -b; the link to ʿaqara 'to wound' is the traditional analysis of the Arab lexicographers, echoed by Thaʿālibī, who files the scorpion under the verb yalsaʿu 'stings'. Klein gives the cognate list with no internal derivation. Separately, the whole right-hand branch of this chart (Hebrew ʿaqrāḇ → Greek skorpios → Latin → French → English) is rejected by modern scholarship: Klein 1401 himself only says 'prob. ult. connected with Heb. ʿaqrābh' on the authority of A. Schott (1936), and Beekes, Etymonline and Skeat all keep Greek skorpíos away from Semitic (Pre-Greek, or PIE *(s)ker- 'to cut'). Only the Arabic→Persian arrow on the left is secure.\",\n   \"note_fa\": \"ریشهٔ سامی *ʿaqrab- «کژدم» به‌راستی بازسازی‌پذیر است و در اکدی aqrabu، عبری ʿaqrāḇ، آرامی ʿaqrabbā، سریانی ʿeqqarbā و حبشی ʿaqrab/ʿarqab بازتاب دارد؛ اما زبان‌شناسان سامی آن را نامی چهارحرفی و بسیط می‌دانند، نه برساخته از ریشهٔ سه‌حرفی «ع‌ق‌ر» (عَقَرَ «زخم زدن، پی کردن»). پیوند با «ع‌ق‌ر» تحلیل لغویان قدیم عرب است (ثعالبی هم عقرب را در باب «یلسع» آورده) و ریشه‌شناسی عامیانه‌وار می‌نماید. افزون بر این، شاخهٔ راست نمودار — یعنی رفتن عبری ʿaqrāb به یونانی skorpios و از آنجا به لاتین و فرانسه و انگلیسی — را پژوهش امروزی (بیکس، اتیمانلاین، اسکیت) رد می‌کند؛ تنها پیکان «عربی ← فارسی» در سمت چپ استوار است. ادعای نورایی در کلیت خود با احتیاط پذیرفتنی است.\",\n   \"sources\": [W+\"%D8%B9%D9%82%D8%B1%D8%A8\", \"https://www.etymonline.com/word/scorpion\"],\n   \"ref_check\": [\n    {\"ref\": \"FVA:278\", \"status\": \"not_checked\", \"note\": \"S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi — no digital copy exists on archive.org, ketabnak, noorlib or the open web (refs_online.json records only an OpenLibrary catalogue entry, OL2012991M). Cannot be consulted.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Arabic\", \"words\": \"aqrab\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic عَقْرَب ʿaqrab 'scorpion' is not derived inside Arabic: it continues Proto-Semitic *ʿaqrab-, already Akkadian aqrabu (2nd millennium BCE), with Hebrew ʿaqrāḇ, Aramaic ʿaqrabbā, Syriac ʿeqqarbā, Ethiopic ʿaqrab / ʿarqab. Klein s.v. 'alacran' gives exactly this cognate set. The Arabic root ʿ-q-r ('to wound, to hamstring an animal') that Nourai makes the root box out of does exist and gives the semantic motivation the Arab lexicographers assumed, but the noun is quadriradical and is treated as primary. As a word of Arabic, the form and meaning drawn in the chart are correct; only the internal derivation from ʿ-q-r is uncertain.\",\n     \"derivation_fa\": \"واژهٔ عربی «عَقْرَب» در خودِ عربی ساخته نشده، بلکه میراث سامی آغازین *ʿaqrab- است و همتاهای دقیق آن در اکدی aqrabu، عبری ʿaqrāḇ، آرامی ʿaqrabbā، سریانی ʿeqqarbā و حبشی ʿaqrab (و صورت مقلوب ʿarqab) دیده می‌شود؛ کلاین در مدخل alacran همین فهرست هم‌ریشه‌ها را می‌آورد. ریشهٔ سه‌حرفی «ع‌ق‌ر» به معنی «زخم زدن، پی کردن» در عربی هست و انگیزهٔ معنایی مورد نظر نورایی را تأمین می‌کند، ولی این اسم چهارحرفی است و در ریشه‌شناسی سامی بسیط شمرده می‌شود. پس صورت و معنای این گره درست است و تنها اشتقاق درونی آن از «ع‌ق‌ر» قطعی نیست.\",\n     \"sources\": [W+\"%D8%B9%D9%82%D8%B1%D8%A8\"],\n     \"ref_check\": [\n      {\"ref\": \"FVA:278\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi's dictionary anywhere (see root ref_check).\"},\n      {\"ref\": \"KFL:427\", \"status\": \"partial\", \"note\": \"Tha'alebi, Fiqh al-lugha, local KFL.txt line 6500 (running number '44_' on the page, i.e. c. p.440 of THIS Indian printing, not the 1885 Beirut pagination Nourai cites): '[يَلسَعُ] كل ضارب بمؤخره: يلسع كالعقرب والزنبور' — the scorpion is indeed filed under 'stings with its hindmost part', which supports Nourai's 'to sting' gloss, but Tha'alebi gives no etymology and the page number cannot be matched to the Beirut edition.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 44 s.v. alacran (leaf 34 of KLN_1966.txt)\", \"stance\": \"supports\", \"note\": \"'Sp. fr. Arab. al-ʿaqrab, \\\"the scorpion\\\" ... which is rel. to Heb. ʿaqrābh, Aram. ʿaqrabbā, Syr. ʿeqqarbā, Ethiop. ʿaqrab, ʿarqab, Akkad. aqrabu, \\\"scorpion\\\"' — Semitic, inherited, no root analysis.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 47 (LKT.txt line 320)\", \"stance\": \"supports\", \"note\": \"'Ar. ʿakrab: \\\"Skorpion\\\". Hieraus sp. alacran ... pg. alacral, alacrão, lacrão' — Lokotsch treats ʿaqrab as the Arabic base word.\"},\n      {\"src\": \"AFM\", \"where\": \"grep 'عقرب' in AFM.txt (lines 580, 2578, 3992, 4022 …)\", \"stance\": \"silent\", \"note\": \"Addi Shir's book of Arabicised Persian words has عقرب only inside other entries (drug names, الشبدع etc.), never as a headword — i.e. he does NOT consider ʿaqrab a Persian loan, consistent with its being native Semitic.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"aqrab «عقرب»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian عقرب ʿaqrab is a plain Arabic loanword taken over after the Islamic conquest (7th c. CE), used both for the animal and for the eighth zodiac sign (برج عقرب). The extra forms in the chart are Arabic morphology carried over with it: عقارب ʿaqāreb is the Arabic broken plural (faʿāʿil pattern), and عقربه ʿaqrabe 'clock hand' is a later Persian use of the Arabic feminine, the hand being pictured as a scorpion's tail. The inherited Iranian word for the animal is quite different — Middle Persian gazdum > NP کژدم každom — and Borhan-e Qateʿ still defines کژدم as 'بعربی عقرب'.\",\n     \"derivation_fa\": \"«عقرب» در فارسی نو وام‌واژه‌ای عربی است که پس از فتح اسلامی (سدهٔ نخست هجری) وارد شده و هم برای جانور و هم برای برج هشتم فلکی به کار می‌رود. صورت‌های افزودهٔ نمودار نیز صرف عربی‌اند: «عقارب» جمع مکسّر عربی است و «عقربه» (شاخکِ ساعت) کاربرد متأخر مؤنّث عربی است که در آن، عقربکِ ساعت به دُم کژدم مانند شده است. واژهٔ ایرانیِ اصیل این جانور چیز دیگری است: فارسی میانه gazdum > فارسی نو «کژدم»؛ برهان قاطع نیز «کژدم» را با «بعربی عقرب» معنی می‌کند. ادعای نورایی درست است.\",\n     \"sources\": [W+\"%D8%B9%D9%82%D8%B1%D8%A8\"],\n     \"ref_check\": [\n      {\"ref\": \"FVA:278\", \"status\": \"not_checked\", \"note\": \"Nahvi's dictionary of Arabic words in Persian is exactly the right kind of source for this arrow, but no copy is available digitally.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 3, pdf pages 171 and 431-432 (BQT_v3_pages.txt idx 170, 430-431)\", \"stance\": \"supports\", \"note\": \"Borhan has no headword عقرب (it is Arabic) but has the compounds 'عقرب‌خانه' and 'عقرب زلوفری: کنایه از برج عقرب است، و آن برج هشتم باشد از بروج فلکی'; s.v. کژدم it glosses 'جانورست گزنده … بعربی عقرب' — i.e. Persian's own word is každom and ʿaqrab is the Arabic equivalent.\"},\n      {\"src\": \"AFM\", \"where\": \"AFM.txt, no headword\", \"stance\": \"silent\", \"note\": \"not listed among the Persian words Arabicised — confirming the loan runs Arabic → Persian, not the reverse.\"},\n      {\"src\": \"KLN\", \"where\": \"p. 44 s.v. alacran\", \"stance\": \"supports\", \"note\": \"same Semitic pedigree; Persian is not mentioned as a source.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Hebrew\", \"words\": \"aqrabh\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Biblical Hebrew עַקְרָב ʿaqrāḇ 'scorpion' (Deut. 8:15; 1 Kings 12:11 'I will chastise you with scorpions') is the regular Hebrew reflex of Proto-Semitic *ʿaqrab-: the *b is spirantized to /v/ after the vowel, whence Nourai's transliteration 'aqrabh'. As drawn — Hebrew descending directly from the common Semitic root box, in parallel with Arabic — the node is correct; what is wrong is the arrow that leaves it (see node 4).\",\n     \"derivation_fa\": \"«עַקְרָב» (ʿaqrāḇ) در عبری کتاب مقدس (سِفر تثنیه ۸:۱۵ و اول پادشاهان ۱۲:۱۱) بازتاب منظم سامی آغازین *ʿaqrab- است؛ /b/ پس از واکه نرم شده و به /v/ بدل گشته و از همین‌روست که نورایی آن را aqrabh می‌نویسد. جایگاه این گره در نمودار — یعنی بازگشت مستقیم عبری به ریشهٔ مشترک سامی، هم‌تراز با عربی — درست است؛ آنچه نادرست است پیکانی است که از این گره بیرون می‌رود (نگاه کنید به گرهٔ ۴).\",\n     \"sources\": [W+\"%D8%B9%D9%82%D8%B1%D8%A8\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1404\", \"status\": \"not_found\", \"note\": \"Klein 1966 p.1404 (KLN_1966.txt leaf 745, whose running heads read 'scrip 1404 | 1405 scupper') covers scourge–scran: nothing Semitic there. Klein's statement about Heb. ʿaqrābh is on p.1401 (leaf 744, running heads '1401 scorn | 1402 Scottish'), s.v. 'scorpion', and the cognate list is on p.44 s.v. 'alacran'. KLN:1404 is a wrong page number — most likely a slip for 1401.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1401 s.v. scorpion; p. 44 s.v. alacran\", \"stance\": \"supports\", \"note\": \"'Heb. ʿaqrabh, \\\"scorpion\\\"' with the Semitic cognates; Klein has the Hebrew word and its Semitic family.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. 4, s.v. scorpion (line 4263)\", \"stance\": \"silent\", \"note\": \"gives only '< L scorpion' — no Semitic material at all.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Greek\", \"words\": \"skorpios\", \"verdict\": \"disputed\",\n     \"derivation\": \"Ancient Greek σκορπίος 'scorpion' (Aeschylus, Aristotle; also a sea-fish and a siege engine) is NOT accepted today as a borrowing of Hebrew ʿaqrāḇ. Nourai's own reference is the source of the claim: Klein p.1401 writes 'fr. Gk. σκορπίος, which is prob. ult. connected with Heb. ʿaqrabh, \\\"scorpion\\\". See Albert Schott, Indogermanisch-semitische Studien, p. 77' — a 1936 pan-comparatist pamphlet, and Klein hedges it with 'prob. ult.'. Phonetically the equation is hopeless: ʿ-q-r-b would have to yield s-k-o-r-p- with a prothetic s-, loss of the pharyngeal, and b > p. Beekes (Etymological Dictionary of Greek, and Wiktionary following him) takes σκορπίος as a Pre-Greek word, comparing κάραβος 'beetle' and κεράμβυξ, from a pre-form of the shape *karaᵐp-; the older Indo-European handbooks (Skeat s.v. scorpion: '(√SKARP.) See Sharp'; Etymonline: PIE *sker- 'to cut') attach it instead to *(s)ker- 'to cut'. Either way, the Semitic arrow drawn here is rejected.\",\n     \"derivation_fa\": \"واژهٔ یونانی باستان σκορπίος «کژدم» (نزد آیسخولوس و ارسطو، و نیز نام ماهی و منجنیق) را امروز وام‌گیری از عبری ʿaqrāḇ نمی‌دانند. سرچشمهٔ این ادعا خودِ مأخذ نورایی است: کلاین در صفحهٔ ۱۴۰۱ می‌نویسد «σκορπίος که احتمالاً در نهایت با عبری ʿaqrabh مرتبط است» و به رسالهٔ آلبرت شوت (۱۹۳۶) ارجاع می‌دهد؛ حتی خود او با «احتمالاً» آن را مشروط کرده است. از دید آوایی این برابرنهاد ناممکن است: باید حرف حلقی «ع» بیفتد، «س» آغازین افزوده شود و «ب» به «پ» بدل گردد. بیکس در فرهنگ ریشه‌شناختی یونانی این واژه را پیش‌یونانی (Pre-Greek) می‌داند و با κάραβος «سوسک» و κεράμβυξ می‌سنجد؛ اسکیت و اتیمانلاین آن را به ریشهٔ هندواروپایی *(s)ker- «بریدن» می‌بندند. به هر روی، پژوهش امروزی این پیکان سامی را رد می‌کند.\",\n     \"sources\": [W+\"%CF%83%CE%BA%CE%BF%CF%81%CF%80%CE%AF%CE%BF%CF%82\", \"https://www.etymonline.com/word/scorpion\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1401\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 744 (printed p.1401): 'scorpion, n. — ME. scorpioun, fr. OF. (= F.) scorpion, fr. L. scorpionem, acc. of Scorpio, a collateral form of scorpius, fr. Gk. σκορπίος, which is prob. ult. connected with Heb. ʿaqrabh, \\\"scorpion\\\". See Albert Schott, Indogermanisch-semitische Studien, p. 77.' Klein does say it — hedged — so the page supports Nourai's arrow, but Klein is the ONLY support and is not followed today.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"s.v. scorpion and s.v. sharp (SKT.txt lines 16669, 17038)\", \"stance\": \"contradicts\", \"note\": \"'Gk. σκορπίος, a scorpion … (√SKARP.) See Sharp'; s.v. Sharp: 'Allied to L. scalpere, to cut, Gk. σκορπίος, scorpion. (√KARP.)' — Indo-European, not Semitic.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. scorpio (LAT.txt line 56315 ff.)\", \"stance\": \"silent\", \"note\": \"'Emprunt au gr. σκορπίος, σκορπίων' — Latin from Greek, with no comment on where Greek got it.\"},\n      {\"src\": \"KLN\", \"where\": \"p. 1401\", \"stance\": \"partial\", \"note\": \"the only book on the shelf that entertains the Semitic link, and only as 'prob. ult. connected'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Latin\", \"words\": \"scorpius\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin scorpius (poetic also scorpios, and the collateral n-stem scorpiō, gen. scorpiōnis) is a straightforward Hellenism: Ernout–Meillet s.v. scorpiō say 'Emprunt au gr. σκορπίος, σκορπίων', and beside the animal Latin uses the word for the fish 'rascasse' and for the torsion catapult (Vitruvius, Caesar). Borrowed in the literary period, with the Greek nominative -os regularly latinized to -us in the 2nd-declension form. The one thing the chart flattens is that the Romance descendants come not from scorpius but from the accusative scorpiōnem of the n-stem doublet (Ernout–Meillet: 'De scorpionem provient le gat. skaurpjo').\",\n     \"derivation_fa\": \"لاتینی scorpius (و صورت شاعرانهٔ scorpios و نیز ستاک نونیِ همراه scorpiō، مضاف‌الیه scorpiōnis) وام‌واژه‌ای یونانی است؛ ارنو و مِیه در مدخل scorpiō می‌نویسند «وام‌گرفته از یونانی σκορπίος، σκορπίων». در لاتین این واژه جز جانور، بر ماهی «راسکاس» و بر منجنیق پیچشی (نزد ویتروویوس و کایسار) نیز اطلاق می‌شده است. وام‌گیری در دورهٔ ادبی رخ داده و پایانهٔ یونانی ‎-os‎ به‌قاعده در صرف دوم لاتین ‎-us‎ شده است. تنها نکته‌ای که نمودار نادیده گرفته این است که بازماندگان رومی از scorpius نمی‌آیند، بلکه از حالت مفعولی scorpiōnem از همان ستاک نونی برخاسته‌اند.\",\n     \"sources\": [\"https://www.etymonline.com/word/scorpion\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1164\", \"status\": \"not_checked\", \"note\": \"Nourai's AHD page numbers are those of the 1975/76 New College Edition, which is lending-only on archive.org and has no open scan; p.1164 would fall in the sc- range of the main dictionary (not the IE-roots appendix, pp.1505-1550). The local proxy AHD_watkins1985.txt (the IE roots only) has no 'scorpion' entry, as expected.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout–Meillet, s.v. scorpiō (LAT.txt lines 56315-56319)\", \"stance\": \"supports\", \"note\": \"'scorpiō, -ōnis m. (et doublets poétiques scorpios, scorpius): 1° scorpion … Empr. au gr. σκορπίος, σκορπίων. … De scorpionem provient le got. skaurpjo.'\"},\n      {\"src\": \"KLN\", \"where\": \"p. 1401 s.v. scorpion\", \"stance\": \"supports\", \"note\": \"'fr. L. scorpionem, acc. of Scorpio, a collateral form of scorpius, fr. Gk. σκορπίος'.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. 4 s.v. Scorpio / scorpaena\", \"stance\": \"supports\", \"note\": \"'[< L scorpio]', 'L. scorpaena … lit. scorpion fish, fr. Gk. σκορπίος'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"French\", \"words\": \"scorpion\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Old French (12th c.) and Modern French scorpion continues Latin scorpiōnem, the accusative of the n-stem scorpiō — the same word as scorpius, of which it is the 'collateral form' (Klein). The Latin -ōnem regularly gives French -on (cf. leōnem > lion), and the learned-looking sc- was kept because the word belongs to the semi-learned stratum transmitted through ecclesiastical Latin (the scorpions of Revelation 9). No Arabic route is involved here: the Arabic-mediated Romance word for the animal is the separate Spanish alacrán < al-ʿaqrab (Klein p.44; Lokotsch no. 47).\",\n     \"derivation_fa\": \"واژهٔ فرانسویِ کهن (سدهٔ دوازدهم) و امروزی scorpion دنبالهٔ لاتینی scorpiōnem است، یعنی حالت مفعولیِ ستاک نونی scorpiō که خودْ صورتِ همراهِ scorpius است. پایانهٔ لاتینی ‎-ōnem‎ به‌قاعده در فرانسه ‎-on‎ می‌شود (مانند leōnem > lion) و آغازِ ‎sc-‎ به‌سبب آنکه واژه از لایهٔ نیمه‌عالمانه و از راه لاتینِ کلیسایی (کژدم‌های مکاشفهٔ یوحنا، باب ۹) رسیده، دست‌نخورده مانده است. در اینجا هیچ واسطهٔ عربی در کار نیست؛ واژهٔ رومیِ عربی‌تبارِ این جانور جداگانه است: اسپانیایی alacrán از «العقرب» (کلاین ص۴۴، لوکوچ شمارهٔ ۴۷).\",\n     \"sources\": [\"https://www.etymonline.com/word/scorpion\"],\n     \"ref_check\": [\n      {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"Nourai cites no reference for the French node; the link is covered by his KLN:1401 on the neighbouring boxes.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1401 s.v. scorpion\", \"stance\": \"supports\", \"note\": \"'ME. scorpioun, fr. OF. (= F.) scorpion, fr. L. scorpionem'.\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. scorpion (SKT.txt line 16669)\", \"stance\": \"supports\", \"note\": \"'(F.–L.–Gk.) F. scorpion … acc. of scorpio, the same as scorpius'.\"},\n      {\"src\": \"DEV\", \"where\": \"DEV.txt / PHN.txt (French words of oriental origin)\", \"stance\": \"silent\", \"note\": \"scorpion is not in Devic's or Pihan's lists of French Arabisms — correctly, since it came from Latin.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"scorpion\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle English scorpioun (c.1200, e.g. the Ancrene Riwle and the Wycliffite Bible) was taken from Old French scorpion; the modern spelling and stress follow the French. It entered English chiefly through Bible translation (Luke 10:19, Rev. 9:3-10) and through astrology (the sign Scorpio), which is why the word is attested so early for a Mediterranean animal unknown in Britain. The chain Greek → Latin → French → English is uncontroversial; only the Semitic step above the Greek is not.\",\n     \"derivation_fa\": \"صورت انگلیسی میانه scorpioun (حدود ۱۲۰۰ م.، برای نمونه در Ancrene Riwle و ترجمهٔ ویکلیف از کتاب مقدس) از فرانسویِ کهن scorpion گرفته شده و املا و تکیهٔ امروزی نیز از فرانسه است. راه ورود واژه بیش از همه ترجمهٔ کتاب مقدس (لوقا ۱۰:۱۹ و مکاشفه ۹:۳-۱۰) و احکام نجوم (برج عقرب) بوده است؛ ازاین‌روست که نام جانوری مدیترانه‌ای که در بریتانیا یافت نمی‌شود، چنین زود در انگلیسی گواهی شده. زنجیرهٔ یونانی ← لاتین ← فرانسه ← انگلیسی بی‌مناقشه است؛ تنها پلهٔ سامیِ بالای یونانی پذیرفته نیست.\",\n     \"sources\": [\"https://www.etymonline.com/word/scorpion\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1401\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 744 (p.1401): 'scorpion, n. — ME. scorpioun, fr. OF. (= F.) scorpion, fr. L. scorpionem, acc. of Scorpio, a collateral form of scorpius, fr. Gk. σκορπίος' — the whole English chain, exactly as drawn.\"},\n      {\"ref\": \"AHD:1164\", \"status\": \"not_checked\", \"note\": \"the 1975/76 AHD New College Edition is not open online; the page would be the ordinary dictionary entry 'scorpion'. Not verifiable.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"s.v. scorpion\", \"stance\": \"supports\", \"note\": \"'(F.–L.–Gk.) F. scorpion … Gk. σκορπίος, a scorpion, also a sea-fish.'\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. Scorpio/scorpion\", \"stance\": \"supports\", \"note\": \"records the animal, the constellation and 'the Scorpion's Heart' (Antares) — the astrological route by which the word became familiar in English.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. 4 s.v. scor'pi-on\", \"stance\": \"supports\", \"note\": \"long zoological entry; etymology '[< L scorpion]'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Ar, Are\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂er- (older notation *ar-, *arə-) 'to fit together, to join' — Pokorny I 55-61 '1. ar-, themat. (a)re-, schwere Basis arə-, rē- und i-Basis (a)ri-, rēi- … fügen, passen'\",\n   \"note\": \"Root name, language label, gloss and page reference are all exactly right: Pokorny p.55 opens the entry with '1. ar-, themat. (a)re-, schwere Basis arə-, rē- und i-Basis (a)ri-, rēi- … \\\"fügen, passen\\\"', i.e. 'to fit together', and Watkins/AHD heads the same root 'ar-. Also arə-. To fit together. … [Pok. 1. ar- 55.]'. Nourai's second citation form 'Are' = Pokorny's arə-. One caveat that affects the two lower branches: Pokorny himself files the rē-/rē-dh- material (Av. rādaiti, NP ārāstan, Lat. rērī, Germ. raten) under this root, but flags it as 'Wzf. rē-, rō-'; Watkins prints it as 'III. Variant or separate root *rē-', and current IE practice separates *h₂reh₁dʰ- 'to care for, arrange' from *h₂er- altogether. So the chart's root box is right, while the rād branch (nodes 7-8) hangs on an equation that is now usually not made.\",\n   \"note_fa\": \"نام ریشه، برچسب زبانی، معنا و شمارهٔ صفحه همگی درست‌اند: پوکورنی در صفحهٔ ۵۵ مدخل را چنین می‌گشاید: «1. ar-، شکل مضاعف (a)re-، پایهٔ سنگین arə-، rē- و پایهٔ i-دار (a)ri-، rēi- … fügen, passen» یعنی «جفت‌وجور کردن، به‌هم‌پیوستن»؛ واتکینز نیز در پیوستِ ریشه‌های هندواروپاییِ AHD همین ریشه را «ar-. Also arə-. To fit together» می‌آورد و به «Pok. 1. ar- 55» ارجاع می‌دهد. صورت دوم نورایی یعنی «Are» همان arə- پوکورنی است. تنها هشدار — که بر دو شاخهٔ پایینی اثر می‌گذارد — این است که خودِ پوکورنی زیرمجموعهٔ rē-/rē-dh- (اوستایی rādaiti، فارسی «آراستن»، لاتین rērī، آلمانی raten) را ذیل همین ریشه آورده ولی آن را «صورت ریشه‌ایِ rē-» نامیده، واتکینز آن را «صورت دگرگون یا ریشهٔ جداگانهٔ *rē-» می‌خواند و هندواروپایی‌شناسی امروز ریشهٔ *h₂reh₁dʰ- را یکسره از *h₂er- جدا می‌کند.\",\n   \"sources\": [W+\"Reconstruction:Proto-Indo-European/h%E2%82%82er-\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:55\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 63 = printed p.55: '1. ar-), themat. (a)re-, schwere Basis arə-, rē- und i-Basis (a)ri-, rēi- … \\\"fügen, passen\\\", mehrfach und vielleicht ältest vom planmäßigen Aufeinanderlegen beim Holzbau'. Exactly the root and gloss of the chart's root box.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Band I pp. 55-61 (POK_01.txt leaves 63-69)\", \"stance\": \"supports\", \"note\": \"the full entry, ending 'WP. I 69 ff., WH. I 69, 70, Trautmann 13 f.'\"},\n    {\"src\": \"WLD\", \"where\": \"Walde–Pokorny Bd. I pp. 69-77 (WLD_Bd1_pages.txt leaves 78-86)\", \"stance\": \"supports\", \"note\": \"the older version of the same article, cited by Pokorny as 'WP. I 69 ff.'; p.74 carries the rē-dh- section.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ar- (AHD_watkins1985.txt line 287)\", \"stance\": \"supports\", \"note\": \"'ar-. Also arə-. To fit together. … [Pok. 1. ar- 55.]' — but note 'II. Possibly suffixed variant form (or separate root) *or-dh-' and 'III. Variant or separate root *rē-'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. ar- (2) 'join, fit' and artos (3) (IEC.txt lines 662, 739)\", \"stance\": \"supports\", \"note\": \"'ar- (2) (radical) \\\"join, fit\\\". WP I, 73'; 'artos (3) … joined; adjoining … Skt. ṛtáh, ṛtám … Av. arəto \\\"perfect\\\"; OPer. arta- \\\"law, justice\\\" (cf. the name Artaxerxes)'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"arta 2, areta; arata, aradra; arta-arân; arta-pa; arta-xšathra; aipi-areta\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Old Persian arta- and Avestan arəta-/ərəta- 'truth, right order, divine Law' are the Indo-Iranian to-participle *H̥r-tá- 'fitted, put in order' of *h₂er-, matching Vedic ṛtá- 'cosmic order'; Kent p.171 s.v. arta-: 'sb. \\\"Law, Justice\\\" … pte. to ar- as sb., Av. aša- and arəta-, Skt. ṛtá- \\\"cosmic order\\\" … pIE *ṛto-'. Pokorny 56-57 has the same set verbatim: 'av. arəta-, ərəta- n., apers. arta- (in Kompos.) \\\"Gesetz, Recht, heiliges Recht\\\"'. 'aradra' = Av. arədra- 'getreu, zuverlässig, glaubenstreu, fromm' (Pokorny p.58), a -dhro- derivative. Of the compounds: arta-xšaθra- is genuine Old Persian Artaxšaça- 'having a kingdom of justice' (Kent p.171; Elamite ir-tak-ša-aš-ša, Akkadian ar-tak-šat-su, Greek Artaxérxēs); aipi-arəta- 'bestimmt, fest zugewiesen' is quoted by Pokorny on p.57. Two are weaker. 'arta-pa' (*Ṛta-pāna- 'protected by Arta'), the source of Artabānu/Ardavān, competes with *Ṛta-bānu- 'the splendour of Arta', which many Iranists prefer. 'arta-arân \\\"holy Aryan land\\\"' is not an attested Old Iranian word at all: it is Farahvashi's ad-hoc reconstruction for the district name Ardalān (Iranvij p.28, 'واژهٔ اردلان را می‌توان به‌صورت کهن آن … بازسازی کرد … و معنی آن «ایران مقدس» است'), and 'one can reconstruct' is as far as the evidence goes.\",\n     \"derivation_fa\": \"پارسی باستان arta- و اوستایی arəta-/ərəta- به معنی «راستی، نظم درست، قانون ایزدی» همان صفت مفعولی هندوایرانی *H̥r-tá- «جفت‌وجورشده، سامان‌یافته» از ریشهٔ *h₂er- است و با ودایی ṛtá- «نظم کیهانی» برابر می‌ایستد؛ کِنت در صفحهٔ ۱۷۱ می‌نویسد: «arta- اسم، \\\"قانون، داد\\\" … صفت مفعولی ar- در نقش اسم، اوستایی aša- و arəta-، سنسکریت ṛtá-». پوکورنی نیز در صفحهٔ ۵۶ همین مجموعه را می‌آورد. صورت «aradra» همان اوستایی arədra- «باوفا، درست‌پیمان، پرهیزگار» (پوکورنی ص۵۸) است. از میان ترکیب‌ها، arta-xšaθra- به‌راستی پارسی باستانِ Artaxšaça- «دارندهٔ شهریاریِ دادگرانه» است (نزد عیلامی ir-tak-ša-aš-ša و اکدی ar-tak-šat-su و یونانی Artaxérxēs)، و aipi-arəta- را خود پوکورنی گواه آورده است. اما دو مورد سست‌اند: arta-pa (بازسازیِ *Ṛta-pāna- «در پناه اَرتَه») در برابر *Ṛta-bānu- «فروغ اَرتَه» قرار دارد که بسیاری از ایران‌شناسان آن را ترجیح می‌دهند؛ و arta-arān «سرزمین مقدس آریایی» اصلاً واژه‌ای گواهی‌شده نیست، بلکه بازسازی فرضیِ فره‌وشی برای نام «اردلان» است (ایرانویج ص۲۸). پس ادعای نورایی در هستهٔ خود درست و در دو ترکیب پایانی با احتیاط پذیرفتنی است.\",\n     \"sources\": [W+\"Reconstruction:Proto-Indo-European/h%E2%82%82er-\", W+\"%D8%A7%D8%B1%D8%AF%D8%B4%DB%8C%D8%B1\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:56\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 64 (printed pp.56-57): 't-Bildungen: r̥t-, art- \\\"zusammengefügt\\\". Ai. r̥tá- n. \\\"passend, recht\\\", r̥tám n. \\\"wohlgefügte, heilige Ordnung\\\" …, av. arəta-, ərəta- n., apers. arta- (in Kompos.) \\\"Gesetz, Recht, heiliges Recht\\\", av. aša- n. \\\"was recht, wahr ist\\\"'; p.57 adds 'av. aipi-ərəta- \\\"bestimmt, fest zugewiesen\\\"' and p.58 'av. arədra- \\\"getreu, zuverlässig, glaubenstreu, fromm\\\"'. Every Nourai form except the two compounds is on the cited pages.\"},\n      {\"ref\": \"IRN:28\", \"status\": \"supports\", \"note\": \"Farahvashi, Iranvij, printed p.28 (IRN_pages.txt pdf page 39): 'قبیله‌های پارسی … در ناحیهٔ اردلان کنونی جای گرفت. واژهٔ اردلان را می‌توان به‌صورت کهن آن … بازسازی کرد: Arta-Aryāna و معنی آن «ایران مقدس» است.' This is the source of Nourai's 'arta-arân: holy Aryan land' — a reconstruction, presented as such.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.171 s.v. arta-, Artaxšaça-, artāvan- (KNT.txt lines 5060, 5064, 5065)\", \"stance\": \"supports\", \"note\": \"'arta- sb. \\\"Law, Justice\\\" … pte. to ar- as sb.'; 'Artaxšaça- … From arta- \\\"justice\\\" + xšaça- \\\"kingdom\\\", \\\"Having a kingdom of justice\\\"'; 'artāvan- adj. \\\"righteous, blessed\\\" … identical with Av. ašavan-'.\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 254 ff. s.v. ašavan- (BRT.txt lines 6296-6301)\", \"stance\": \"supports\", \"note\": \"the ašavan- article ends 'Das ein altir. *artavan- voraussetzt … Dagegen führt mp. artāk, ahrāv(?) … auf *artāvan-' — i.e. Bartholomae reconstructs Old Iranian *arta-van-.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, artos (3) (IEC.txt line 739)\", \"stance\": \"supports\", \"note\": \"'Av. arəto \\\"perfect\\\"; OPer. arta- \\\"law, justice\\\" (cf. the name Artaxerxes)'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\",\n     \"words\": \"ard «ارد ۱»; ard «ارد۲»; Ardalân «اردلان»; Ardavân «اردوان»; Ardešîr «اردشیر»; nard 1 «نَرد ۱»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Most of this box is sound. Ardašīr is New Persian for Middle Persian Ardaxšīr < Old Persian Artaxšaça- 'having a kingdom of justice' (Kent p.171; Wiktionary اردشیر), with OP -ta- > MP -d- and the loss of the final syllable; Greek took the same name as Artaxérxēs. Ardavān continues Parthian/Middle Persian Ardawān, Greek Artabanos, from *Ṛta-pāna- (or *Ṛta-bānu-), so 'protector of justice' is a defensible if not certain reading. Ardalān is a Kurdish princely house and district: Nourai's gloss follows Farahvashi's reconstruction *Arta-Aryāna 'holy Aryan land' (Iranvij p.28), which is a guess, not a documented etymology. nard 'backgammon' is right and well documented: it is shortened from nardašīr, from Middle Persian nēw-Ardaxšīr 'brave Ardašīr' — Nyberg II s.v. nēv-artaxšēr: 'the game of tric-trac … \\\"Brave Ardashir\\\"; Talm. nrdšyr, Arab nardašīr'; Wiktionary agrees. But 'ard, 25th day of each Persian month' is wrong for THIS root, and Nourai's own reference says so: Mo'in's footnote in Borhan-e Qateʿ (vol. 1 p.98, BQT_v1_pages.txt leaf 309) derives the day-name from 'در اوستا Ašay (vaŋuhī)' — Avestan Aši/Arti, goddess of reward and fortune, MP Ard — and Av. aši- < *ṛti- 'share, reward' belongs to Pokorny's 2. ar- 'zuteilen, an sich bringen' (IEW 61), a different root from 1. ar- 'fügen'. MacKenzie likewise separates 'Ard [ʾrd | M ʾyrd] a goddess; cal. 25th day' from 'ardā righteous'. The 'ard 1: just' of Borhan itself is even odder: Borhan glosses ارد as 'خشم و قهر و غضب' (anger, wrath), and Mo'in's note there refers to Av. arəta-/aša-, so 'just' is Nourai's harmonisation.\",\n     \"derivation_fa\": \"بیشتر این جعبه درست است. «اردشیر» صورت فارسیِ نوِ فارسی میانهٔ Ardaxšīr است از پارسی باستان Artaxšaça- «دارندهٔ شهریاری دادگرانه» (کنت ص۱۷۱)، با تبدیل ‎-t-‎ ایرانی باستان به ‎-d-‎ در فارسی میانه و افتادن هجای پایانی؛ یونانیان همین نام را Artaxérxēs گرفتند. «اردوان» دنبالهٔ پارتی/فارسی میانهٔ Ardawān (یونانی Artabanos) از *Ṛta-pāna- (یا *Ṛta-bānu-) است، پس معنای «نگهبان داد» پذیرفتنی است هرچند قطعی نیست. «اردلان» نام خاندان و ناحیه‌ای کردنشین است و معنایی که نورایی می‌دهد بازسازی فره‌وشی (*Arta-Aryāna) است، نه ریشه‌شناسیِ مستند. «نرد» به‌درستی کوتاه‌شدهٔ «نردشیر» از فارسی میانهٔ nēw-Ardaxšīr «اردشیرِ دلیر» است؛ نیبرگ در واژه‌نامهٔ خود می‌نویسد «nēv-artaxšēr: بازی تخته‌نرد … \\\"اردشیر دلیر\\\"؛ تلمودی nrdšyr، عربی نردشیر». اما «ارد ۲، روز بیست‌وپنجم هر ماه» به این ریشه بازنمی‌گردد و خودِ مأخذ نورایی این را می‌گوید: حاشیهٔ معین بر برهان قاطع (ج۱ ص۹۸) نام روز را از «اوستا Ašay (vaŋuhī)» می‌گیرد، یعنی ایزدبانوی «اَشی» (پاداش و بهره)، و اوستایی aši- از *ṛti- «بهره، پاداش» است که به ریشهٔ دومِ پوکورنی ar- «بخش کردن» (ص۶۱) تعلق دارد، نه به ar-1 «جفت‌وجور کردن». مکنزی نیز «Ard: ایزدبانو، روز بیست‌وپنجم» را از «ardā راست‌کردار» جدا می‌کند. پس این یک واژه را پژوهش امروزی رد می‌کند.\",\n     \"sources\": [W+\"%D8%A7%D8%B1%D8%AF%D8%B4%DB%8C%D8%B1\", W+\"%D9%86%D8%B1%D8%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:98-101\", \"status\": \"partial\", \"note\": \"BQT_v1_pages.txt leaves 309-312 = printed pp.97-101 carry ارد، اردشیر، اردوان، اردی، اردیبهشت، اردیبهشتگان. But Mo'in's footnote on ارد (leaf 309) reads: 'در اوستا Ašay (vaŋuhī) اشی، در پهلوی Ard … دراوستا اشی گاهی اسم مجرد است بمعنی توانگری و بخشش و برکت و نعمت و مزد و بهره؛ و گاه اسم خاص ایزدی که نگهبان مال و خواسته است' — i.e. the 25th-day Ard is Avestan Aši, NOT arta-; and Borhan's own headword ارد is glossed 'بمعنی خشم و قهر و غضب باشد', not 'just'. اردلان does not occur in Borhan at all, and نرد is in a later volume, so the cited pages support only اردشیر / اردوان.\"},\n      {\"ref\": \"IRN:28\", \"status\": \"supports\", \"note\": \"Iranvij p.28: 'واژهٔ اردلان را می‌توان به‌صورت کهن آن … بازسازی کرد … و معنی آن «ایران مقدس» است' — the exact source of Nourai's Ardalān gloss, offered by Farahvashi as a reconstruction.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. nēv-artaxšēr (NYB_vol2_glossary.txt line 2693)\", \"stance\": \"supports\", \"note\": \"'nēv-artaxšēr [ndwʾlthšdl] the game of tric-trac … \\\"Brave Ardashir\\\"; Talm. nrdšyr, Arab nardašīr; Telegdi 249; Goldziher, MSt I, 168' — confirms Nourai's NOTE that nard is shortened from Nīv-Ardašīr.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.12 (PHD.txt line 214)\", \"stance\": \"contradicts\", \"note\": \"two separate headwords: 'Ard [ʾrd | M ʾyrd, N ~] a goddess; cal. 25th day' and 'ardā [ʾrdʾy | (M rdʾw)] righteous, truthful' / 'ardāyīh righteousness' — the calendar name Ard is the goddess (Aši), not arta- 'truth'.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 1 pp. 97-101\", \"stance\": \"partial\", \"note\": \"see ref_check; Mo'in's own note assigns ارد ۲ to Avestan Aši.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"`rt`w\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Sogdian ʾrtʾw /artāw/ 'righteous, one of the Elect' is attested in all three scripts (Buddhist, Manichaean, Christian) and is the Sogdian continuation of Old Iranian *ṛtāvan-, the *-van- derivative of arta- — hence 'possessing arta, righteous'. Gharib's dictionary gives precisely that: no. 1483, p.58, 'ʾrtʾw B, M, C — artaw; MP ahlaw; Parth. ʾrtʾw; OP artawan; Av. ašavan — faithful, electus, righteous'. In Manichaean Sogdian it is the standard term for the Elect. Strictly the box hangs one step lower than drawn: the word comes from the *ṛtāvan- derivative (Nourai's own arta- node), not straight from the bare root.\",\n     \"derivation_fa\": \"سغدی ʾrtʾw (خوانش artāw) «پرهیزگار، برگزیده» در هر سه خطِ بودایی و مانوی و مسیحی گواهی شده و دنبالهٔ ایرانی باستان *ṛtāvan- است، یعنی مشتقِ ‎-van-‎دارِ arta-، به معنی «دارندهٔ اَرتَه، راست‌کردار». بدرالزمان قریب در فرهنگ سغدی، شمارهٔ ۱۴۸۳، صفحهٔ ۵۸، دقیقاً همین را می‌آورد: «ʾrtʾw؛ artaw؛ فارسی میانه ahlaw؛ پارتی ʾrtʾw؛ پارسی باستان artawan؛ اوستایی ašavan — مؤمن، برگزیده، پرهیزگار». در سغدیِ مانوی این واژه اصطلاح رسمیِ «برگزیدگان» است. تنها نکتهٔ خردهٔ نمودار آن است که این واژه یک پله پایین‌تر می‌ایستد: از مشتق *ṛtāvan- می‌آید نه یکراست از ریشهٔ برهنه.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:58\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 123, whose running head shows the printed page number 58: entry '1483 ʾrtʾw B, M, C — artaw ©MP ahlaw; Parth. ʾrtʾw; OP artawan; Av. ašavan ©pl. ~t-y … faithful, clectus [electus], righteous' (refs GMS 91, 1076; TSP; Tales 469.4; BBB; MSP). The page number, the form and the gloss all match the chart.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib no. 1483, p.58; also nos. 1505/1510 ʾrtxwwst < *ṛta-vahišta-\", \"stance\": \"supports\", \"note\": \"Gharib derives ʾrtʾw from OP artāvan-/Av. ašavan-, and separately gives ʾrtxwst 'artxwōst, artxust ©*ṛta vahišta-' — the Sogdian counterpart of Ordibehešt.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. ahlav\", \"stance\": \"supports\", \"note\": \"'The genuine WIr form is OP artāvan \\\"blessed\\\", whence MPrth ʾrdʾw \\\"righteous, veracious\\\"' — the same *ṛtāvan- formation across the Middle Iranian languages.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Avestan\",\n     \"words\": \"aša 3; aša-vahišta; arta-vah-išta; aša-van, ša-vant; asvan\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"aša-van, ša-vant : determined, in order / asvan : holy, sacred\",\n     \"correct_form\": \"aša-van, aša-vant- 'possessing aša, righteous' / ašavan- (the same word; there is no Avestan *ša-vant- or *asvan-)\",\n     \"derivation\": \"The substance of the node is right: Avestan aša- n. 'what is right and true, Truth, cosmic Order' is the Younger-Avestan (dialectally Median-influenced) counterpart of arəta-, both from *ṛtá-; Pokorny p.56 has 'av. aša- n. \\\"was recht, wahr ist\\\"' beside 'av. arəta-, ərəta- n.' in the same paragraph, and aša-vahišta- 'Best Truth' is the name of the second Aməša Spənta, exactly as the chart says (arta-vahišta- is the same compound in its Old-Persian-looking shape, cf. Sogd. ʾrtxwst). But two of the printed forms are corrupt IN THE BOOK — the extraction is faithful to page 31. 'ša-vant' is impossible Avestan: the word is ašavant- / ašavan- (Bartholomae AiW s.v.), and the initial a- has simply dropped out in Nourai's typesetting. 'asvan', printed as a separate line glossed 'holy, sacred', is not an Avestan word either; it duplicates ašavan- with the š lost. Bartholomae's gloss for ašavant- ('der das höchste Anrecht besitzt') is also nearer 'righteous, entitled' than Nourai's 'determined, in order'.\",\n     \"derivation_fa\": \"جانِ این گره درست است: اوستایی aša- (خنثی) «آنچه راست و درست است، اَشَه، نظم کیهانی» همتای اوستایی نو (با رنگ گویشیِ مادی) برای arəta- است و هر دو از *ṛtá- می‌آیند؛ پوکورنی در صفحهٔ ۵۶ در یک بند «av. aša- n. \\\"was recht, wahr ist\\\"» را در کنار «av. arəta-, ərəta- n.» می‌آورد، و aša-vahišta- «بهترین راستی» نام دومین امشاسپند است، درست همان‌گونه که نمودار می‌گوید (arta-vahišta- همان ترکیب با صورت پارسی‌باستان‌نماست؛ سنجیدنی با سغدی ʾrtxwst). اما دو صورت چاپی در خودِ کتاب مغلوط است و استخراج داده وفادار به صفحهٔ ۳۱ است: «ša-vant» در اوستایی ناممکن است و صورت درست ašavant-/ašavan- است (بارتولمه، فرهنگ ایرانی باستان) که «اَ»ی آغازین در حروف‌چینی نورایی افتاده؛ و «asvan» که در سطری جداگانه با معنی «مقدس» آمده اصلاً واژهٔ اوستایی نیست و تکرارِ همان ašavan- است با افتادن «ش». افزون بر این، معنای بارتولمه برای ašavant- («دارندهٔ برترین حق») به «پرهیزگار، بهره‌مند» نزدیک‌تر است تا «determined, in order» نورایی. خطای چاپی کتاب.\",\n     \"sources\": [W+\"Reconstruction:Proto-Indo-European/h%E2%82%82er-\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:56\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 64 (p.56): 'av. arəta-, ərəta- n., apers. arta- (in Kompos.) \\\"Gesetz, Recht, heiliges Recht\\\", av. aša- n. \\\"was recht, wahr ist\\\", ai. ṛtāvan(t)- \\\"ordnungsgemäß, gerecht\\\", av. ašāvan(t)-'. Note that Pokorny prints ašāvan(t)- WITH the initial a-, which is further evidence that Nourai's 'ša-vant' is a misprint.\"},\n      {\"ref\": \"BQT:142\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 358 (printed p.143, i.e. Nourai's 142 ±1): headword 'اشو ۱ بفتح اول و ضم ثانی بواو رسیده، بلغت زند و پازند بمعنی بهشتی باشد که در مقابل دوزخی است' — Borhan's اشو entry, the Persian reflex of ašavan-, which is what Nourai uses this page for (see node 6).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. ašavan- / ašavant- (BRT.txt lines 6296-6307)\", \"stance\": \"partial\", \"note\": \"'ašavan- Adj. … Pü.: ahrav … Das ein altir. *artavan- voraussetzt'; and '*aša-vant- Adj. 1) \\\"rechtschaffen\\\" 2) \\\"der das (höchste) Anrecht a) besitzt\\\"'. The forms are ašavan-/ašavant-, never *šavant- or *asvan-.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. Art-vahišt (line 655)\", \"stance\": \"supports\", \"note\": \"'art, urt < OIr/Skr ṛta- \\\"the right cosmic order, the divine law\\\", Av. arəta-, ərəta-, aša- + vahišta- (\\\"the best\\\"), \\\"the heavenly law\\\"' — Nourai's aša-vahišta / arta-vahišta pair exactly.\"},\n      {\"src\": \"POK\", \"where\": \"p.56-57\", \"stance\": \"supports\", \"note\": \"as quoted above.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Pahlavi\", \"words\": \"aš-vahišt; urt-vahišt; ahru, ahrav, ašôg\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Book Pahlavi has exactly this triple set of spellings for the second Aməša Spənta: Nyberg II lists 'Art-vahišt [ʾrtwhšt], Urt-vahišt [ʾwrtwhšt], Aša-vahišt [ʾšwhšt] — one of the Amahraspands … art, urt < OIr ṛta- … + vahišta- \\\"the best\\\"; Aša-vahišt is directly borrowed from Avestan; also the name of the 2nd month of the year and the 3rd day of the month; MPrs ʾrdywh<yšt>; NP ardi- (urdi-)bihišt'; MacKenzie has 'Ardwahišt [ʾrtwhšt' | M ʾrdywhyst, (N urdībihist)] Right, the second Amahraspand' with cross-references 'Ašwahišt = Ardwahišt' and 'Urdwahišt = Ardwahišt'. The adjective is the same word as Sogdian ʾrtʾw: Book Pahlavi ⟨ʾhlwb'⟩, read ahlaw or (with the l/r ambiguity of the script) ahrav, plus the SW doublet ahlāy/ahrāy and the learned Avestanism ašō(g) ⟨ʾšwk'⟩ — Nyberg: 'ašōk [ʾšwk] = ahlav … A learned w., taken over as a religious term from Av. ašava'. The -hl-/-hr- for Avestan -š- is the regular Book Pahlavi treatment of inherited *-rt- via the Eastern-Iranian-mediated religious vocabulary (Nyberg s.v. Mahlāh).\",\n     \"derivation_fa\": \"پهلویِ کتابی دقیقاً همین سه املا را برای دومین امشاسپند دارد؛ نیبرگ می‌آورد: «Art-vahišt، Urt-vahišt، Aša-vahišt … art، urt از ایرانی باستان ṛta- … + vahišta- «بهترین»؛ Aša-vahišt یکراست از اوستایی وام گرفته شده؛ نام ماه دوم سال و روز سوم ماه نیز هست؛ فارسی میانه ʾrdywhyšt؛ فارسی نو اردیبهشت/اردی‌بهشت». مکنزی نیز «Ardwahišt» را با ارجاع‌های «Ašwahišt = Ardwahišt» و «Urdwahišt = Ardwahišt» ثبت کرده است. صفتِ همراه، همان واژهٔ سغدی ʾrtʾw است: در پهلوی ⟨ʾhlwb'⟩ که به‌سبب یکسانیِ نگارشِ «ل» و «ر» هم ahlaw و هم ahrav خوانده می‌شود، به‌همراه دوگانهٔ جنوب‌غربیِ ahlāy/ahrāy و صورت عالمانهٔ ašō(g) ⟨ʾšwk'⟩؛ نیبرگ: «ašōk = ahlav … واژه‌ای عالمانه که همچون اصطلاحی دینی از اوستایی ašava گرفته شده». تبدیل ‎-š-‎ اوستایی به ‎-hl-/-hr-‎ پهلوی، دگرگونی آواییِ منظمِ واژگان دینیِ برگرفته از *-rt- است. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"BQT:101,142\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 311-312 (printed pp.100-101) has اردی / اردیبهشت / اردیبهشتگان with Mo'in's notes ('پهلوی … نام پنج تن از …'; 'اردیبهشتگان: جشنی که ایرانیان باستان در روز اردیبهشت (سوم) از ماه اردیبهشت برپا می‌کردند … بشت ۱:۹۲، خرده اوستا …'); leaf 358 (printed p.143 ≈ 142) has اشو. So both cited pages carry the material the Pahlavi box rests on.\"},\n      {\"ref\": \"SNS:5\", \"status\": \"supports\", \"note\": \"Tavoosi, Glossary of Šāyest nē Šāyest (SNS.txt line 1808 ff., SNS_pages.txt leaf 18, the first leaf of the glossary proper): 'ahrav/ahlav … ašavay, ašāg … < Av. ašavan-; artāvan (Kent 170-171); ʾhlwb'. The entry says exactly what Nourai's box says. The OCR of the printed page numerals is too poor to confirm '5' itself, but the entry stands on the opening leaf of the alphabetically ordered glossary, which is consistent with p.5.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 8, 12, 15 (PHD.txt lines 184, 214, 221)\", \"stance\": \"supports\", \"note\": \"'ahlaw [ʾhlwb' | M ʾhlw] righteous. ~ih: righteousness'; 'ahlāyīh righteousness'; 'Ardwahišt [ʾrtwhšt' | M ʾrdywhyst, (N urdībihist)] Right, the second Amahraspand'; 'Ašwahišt = Ardwahišt'; 'Urdwahišt = Ardwahišt'; 'ašō [ʾšwk' = Av. ašawa] righteous'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg II s.vv. ahlav, ahlāi, ašōk, Art-vahišt (lines 300-307, 655, 748)\", \"stance\": \"supports\", \"note\": \"'ahlav … Borrowed from Av. ašāvan-, nom. ašavā … The genuine WIr form is OP artāvan'; 'Art-vahišt … Urt-vahišt … Aša-vahišt … NP ardi-(urdi-)bihišt'.\"},\n      {\"src\": \"SNS\", \"where\": \"Tavoosi, glossary s.v. ahrav/ahlav\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Persian\", \"words\": \"Ordîbehešt «اردیبهشت»; ašŭ «اشو»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian اردیبهشت Ordībehešt / Ardībehešt, the second month of the solar year and the third day of every month, is the regular continuation of Middle Persian Ardwahišt < Avestan aša-vahišta- 'Best Truth' (Nyberg: 'NP ardi- (urdi-)bihišt'; MacKenzie: '(N urdībihist)'). The -i- of ardi- is the Middle Persian variant spelling ʾrdywhyšt of the Manichaean texts; the second element was assimilated to the familiar Persian word بهشت behešt 'paradise' (itself MP wahišt 'best'), so that Persian speakers hear it as 'like paradise' — Borhan-e Qateʿ already offers the folk explanation 'چه ارد بمعنی شبیه … و چون این ماه وسط فصل بهار است … بنابراین اردیبهشت خوانند'. اشو ašū is the learned Zoroastrian word taken over from Pahlavi ašō(g) < Av. ašavan- 'righteous'; Nourai's odd second gloss 'heaven' is faithful to the Persian dictionary tradition — Borhan p.143: 'اشو … بلغت زند و پازند بمعنی بهشتی باشد که در مقابل دوزخی است', and Mo'in glosses it 'مقدس، پاک'.\",\n     \"derivation_fa\": \"«اردیبهشت» در فارسی نو، نام ماه دوم سال خورشیدی و روز سوم هر ماه، دنبالهٔ منظم فارسی میانهٔ Ardwahišt از اوستایی aša-vahišta- «بهترین راستی» است (نیبرگ: «فارسی نو ardi-/urdi-bihišt»؛ مکنزی: «(N urdībihist)»). «ی» در «اردی-» بازتاب املای فارسی میانهٔ ʾrdywhyšt در متون مانوی است، و جزء دوم به واژهٔ آشنای «بهشت» (خودْ از فارسی میانهٔ wahišt «بهترین») همگون شده، چنان‌که فارسی‌زبانان آن را «مانند بهشت» می‌شنوند؛ برهان قاطع نیز همین ریشه‌شناسی عامیانه را می‌آورد: «چه ارد بمعنی شبیه … و چون این ماه وسط فصل بهار است … بنابراین اردیبهشت خوانند». «اشو» واژه‌ای عالمانه و زرتشتی است از پهلوی ašō(g) از اوستایی ašavan- «پرهیزگار». معنای دومِ عجیبِ نورایی («heaven») نیز وفادار به سنّت فرهنگ‌نویسی فارسی است: برهان در صفحهٔ ۱۴۳ می‌نویسد «اشو … بلغت زند و پازند بمعنی بهشتی باشد که در مقابل دوزخی است» و معین آن را «مقدس، پاک» معنی می‌کند. ادعای نورایی درست است.\",\n     \"sources\": [W+\"%D8%A7%D8%B1%D8%AF%DB%8C%D8%A8%D9%87%D8%B4%D8%AA\", \"https://abadis.ir/fatofa/%D8%A7%D8%B4%D9%88/\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 311 (printed p.100) s.v. اردی بهشت: 'نام ماه دوم است از سال شمسی … و نام روز سیم از هر ماه شمسی باشد - و نام فرشته‌ای هم هست که محافظت کوه‌ها کند …', with Mo'in's footnote giving the Pahlavi form; leaf 358 (p.143) s.v. اشو as quoted in the derivation.\"},\n      {\"ref\": \"MON:289\", \"status\": \"not_checked\", \"note\": \"Mo'in's six-volume Farhang-e Farsi is not digitised (only the two-volume Adena condensation, without page numbers, is on archive.org). The Mo'in text for اشو is however retrievable through abadis.ir, which quotes it as 'مقدس، پاک' — compatible with the chart.\"},\n      {\"ref\": \"TZF:26\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi: PDF exists only behind a ketabnak login; not accessible.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. Ardwahišt\", \"stance\": \"supports\", \"note\": \"'(N urdībihist)' explicitly gives the New Persian outcome.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. Art-vahišt\", \"stance\": \"supports\", \"note\": \"'also the name of the 2nd month of the year and the 3d day of the month; MPrs ʾrdywh<yšt>; Sogd. 2771; NP ardi- (urdi-)bihišt'.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 1 pp. 100, 143\", \"stance\": \"supports\", \"note\": \"both headwords present, with Mo'in's Pahlavi footnotes; Borhan's own 'ارد = شبیه' explanation is a folk etymology.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir s.v. اشو\", \"stance\": \"supports\", \"note\": \"'مقدس، پاک'; Dehkhoda adds 'بلغت زند و پازند بمعنی بهشتی باشد که در مقابل دوزخی است' — the source of Nourai's 'heaven'.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Avestan\", \"words\": \"râd 1; â-râd, â-râiti 1, â-râs-; pati-râd; vi-râiti, vi-radh\", \"verdict\": \"plausible\",\n     \"derivation\": \"Nourai is reproducing Pokorny faithfully, but the page and the modern standing both need qualifying. Pokorny does put an Avestan rād- here — not on p.56 but on pp.59-60, under the 'dh-Erweiterung rē-dh-, rō-dh-, rə-dh-': 'ai. rādhnóti, rādhyati \\\"macht (passend) zurecht\\\" … av. rādaiti \\\"macht bereit\\\", rāda- m. \\\"Fürsorger\\\"; rādah- n. \\\"Sichbereitstellen, Bereitwilligkeit\\\"; apers. rādiy (Lok. Sg.) \\\"wegen\\\"; npers. ārāyad, ārāstan \\\"schmücken\\\"'. Walde–Pokorny I 74 (the page Nourai cites) has the same paragraph. So the Avestan verb, the prefixed ā-, pati- and vi- compounds and the Persian outcomes are all in his sources. Two reservations. (1) The root equation is now usually abandoned: Watkins already prints this material as 'III. Variant or separate root *rē-', and Wiktionary/LIV treat *h₂reh₁dʰ- 'to care for, arrange' as an independent root, not an extension of *h₂er-. (2) The forms with -s- (ā-rās-) and the -āiti- nouns really belong with a different Iranian verb: Cheung's Etymological Dictionary of the Iranian Verb (2007) pp.196-198 files YAv. raz- 'to draw a line; to direct', OP rāsta- 'right, straight, true', MP ārāy-/ārāst, pēray-, wirāy- under *Hraz < PIE *h₃reǵ-. Nourai's box therefore merges two roots.\",\n     \"derivation_fa\": \"نورایی در اینجا وفادارانه پوکورنی را بازمی‌گوید، اما هم شمارهٔ صفحه و هم اعتبار امروزیِ این پیوند نیازمند قید است. پوکورنی به‌راستی فعل اوستایی rād- را ذیل همین ریشه آورده، ولی نه در صفحهٔ ۵۶ بلکه در صفحه‌های ۵۹-۶۰، زیر «گسترشِ dh-دار rē-dh-, rō-dh-, rə-dh-»: «سنسکریت rādhnóti, rādhyati \\\"سامان می‌دهد، به انجام می‌رساند\\\" … اوستایی rādaiti \\\"آماده می‌کند\\\"، rāda- \\\"سرپرست\\\"؛ rādah- \\\"آمادگی، دهش\\\"؛ پارسی باستان rādiy \\\"به‌سبب\\\"؛ فارسی نو ārāyad، ārāstan \\\"آراستن\\\"». والده-پوکورنی جلد یکم صفحهٔ ۷۴ — همان صفحه‌ای که نورایی یاد کرده — همین بند را دارد. دو نکته اما هست: نخست آنکه این یکی‌انگاری امروز غالباً کنار گذاشته شده؛ واتکینز خودْ این بخش را «صورت دگرگون یا ریشهٔ جداگانهٔ *rē-» می‌نامد و ریشهٔ *h₂reh₁dʰ- «سامان دادن، پروا داشتن» را مستقل می‌شمارند. دوم آنکه صورت‌های ‎-s-‎دار (ā-rās-) و اسم‌های ‎-āiti-‎دار در حقیقت به فعل ایرانیِ دیگری تعلق دارند: چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (۲۰۰۷، ص۱۹۶-۱۹۸) اوستایی نو raz- «خط کشیدن، راست کردن»، پارسی باستان rāsta- «راست، درست» و فارسی میانهٔ ārāy-/ārāst و pēray- و wirāy- را ذیل *Hraz از *h₃reǵ- می‌آورد. پس این جعبه دو ریشه را درهم آمیخته است.\",\n     \"sources\": [W+\"%D8%B1%D8%A7%D8%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"WLD:74\", \"status\": \"supports\", \"note\": \"WLD_Bd1_pages.txt 0-based leaf 82 = printed p.74: 'dh-Erweiterung *rē-dh-, rō-dh- … ai. rādhnóti, rādhyati \\\"macht (passend) zurecht, bringt zustande\\\" … av. rādaiti \\\"macht bereit\\\", m. Dativ … rāda- m. \\\"Fürsorger\\\", rādah- n. \\\"Sichbereitstellen, Bereitwilligkeit (in religiöser Hinsicht)\\\", ap. rādi…' — exactly the Avestan material Nourai's box claims, on exactly the cited page.\"},\n      {\"ref\": \"POK:56\", \"status\": \"partial\", \"note\": \"p.56 (POK_01.txt leaf 64) is the t-formations (arta-, aša-), not the rād- material. Pokorny's rē-dh- section with 'av. rādaiti … npers. ārāyad, ārāstan' is on pp.59-60 (leaves 67-68). Right root, wrong page.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"Band I pp. 59-60\", \"stance\": \"supports\", \"note\": \"'av. rādaiti \\\"macht bereit\\\", rāda- m. \\\"Fürsorger\\\"; rādah- n. \\\"Sichbereitstellen, Bereitwilligkeit\\\" … npers. ārāyad, ārāstan \\\"schmücken\\\"'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ar-, section III\", \"stance\": \"partial\", \"note\": \"'III. Variant or separate root *rē- (< *reə-) … 2. Suffixed form rē-dh-' — Watkins keeps the material under ar- but flags it as possibly a separate root.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, root *Hraz, pp. 196-198 (CHEUNG.txt lines 13349-13400)\", \"stance\": \"contradicts\", \"note\": \"'*Hraz \\\"to draw a line; to direct, richten\\\". AVESTAN: YAv. raz- … OLD PERSIAN: rāsta- (ppp.) \\\"right, straight, true\\\" … MIDDLE PERSIAN … (+ *ā-) BMP ʾlʾd- /āray-/ \\\"to prepare, arrange, adorn\\\" … PIE *h₃reǵ- \\\"to stretch, direct\\\" = LIV: 304 f. | Pok.: 854 f.' — a different root for the ārās- forms.\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae AiW 1512 (grep of the poor Google OCR of BRT.txt could not isolate the rād- article)\", \"stance\": \"silent\", \"note\": \"the local scan's OCR does not render the Avestan headwords legibly enough to quote the rād- entry; Pokorny and Walde–Pokorny both cite Bartholomae for these forms.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Persian\", \"words\": \"râd «راد ۱»; ârâstan «آراستن»; pîrâstan «پیراستن»; vîrâstan «ویراستن»\", \"verdict\": \"plausible\",\n     \"derivation\": \"Two different things are put in one box. (a) راد rād 'generous, liberal, brave' is securely of this family in the modern reconstruction too: Wiktionary derives NP rād < MP rād < OP *rādah < Proto-Iranian *HráHdah < PIE *h₂réh₁dʰ-o-s (root *h₂reh₁dʰ- 'to care'), cognate with Old Avestan rādah- 'generosity', Vedic rā́dhas- 'favour, gift', Gothic garēdan, OHG rāt. Horn, Grundriss no. 601, has 'rād \\\"freigebig\\\": aw. vergl. arāiti-; ai. rāti- \\\"willig zu geben\\\"; phlv. rat (auch Titel), ratīh'. (b) آراستن ārāstan 'to adorn', پیراستن pīrāstan 'to trim', ویراستن vīrāstan 'to arrange, edit' are prefixed forms (ā-, *pati-, *vi-) of one Middle Persian verb ārāy-/ārāst, pēray-/pērāst, wirāy-/wirāst. Nourai's older-school authorities all take them from *rād-: Horn no. 11 'ārāsten \\\"schmücken\\\" … ap. √rād in rāsta- \\\"richtig\\\"; aw. √rād- \\\"zurechtmachen\\\", rādaiti; phlv. ārāstan, ārāy(i)šn; ai. √rādh-' with footnote 'Vgl. auch phlv. vīrāstan, vīrāyišn; hamrāstan', and no. 352 'pīrāsten … pati + √rād- (s. ārāstan No. 11)'; Abolghasemi 1995 p.24 spells out 'آراست ← فارسی میانهٔ ārāst ← ایرانی باستان *ā-rād-ta … d پیش از t به s بدل شده است. rād به معنی «منظم کردن» است'; Aryanpur's index page 52 files ārāstan with Av. ARADH/-RADH, Skt RĀDHNOTI, Lat. RĒRI, Goth. GAREDAN, Germ. RATEN. Against them, Cheung 2007 and Wiktionary put ārāstan/pīrāstan under Proto-Iranian *Hraz- < PIE *h₃reǵ- 'to straighten' (the root of Latin regō, Skt rājati), which also explains MP wirāy-/winnār- and Parthian wyrʾz-. So the box is defensible but no longer the standard account for three of its four words. Semantically all three are transparent: ārāstan 'to put in order' > 'decorate'; pīrāstan 'to set right around' > 'prune, trim'; vīrāstan 'to set apart in order' > (20th-century revival) 'to edit'.\",\n     \"derivation_fa\": \"در این جعبه دو چیز جداگانه کنار هم نشسته است. نخست «راد» به معنی «بخشنده، دلیر»، که در بازسازی امروزی نیز به همین خانواده تعلق دارد: ویکی‌واژه فارسی نو rād را از فارسی میانهٔ rād، از پارسی باستان *rādah، از ایرانی آغازین *HráHdah و سرانجام از هندواروپاییِ *h₂réh₁dʰ-o-s (ریشهٔ *h₂reh₁dʰ- «پروا داشتن») می‌گیرد، هم‌ریشه با اوستایی گاهانی rādah- «دهش»، ودایی rā́dhas- «بخشش» و گوتی garēdan؛ هرن نیز در شمارهٔ ۶۰۱ می‌نویسد «rād \\\"بخشنده\\\"؛ سنجیدنی با اوستایی arāiti-؛ سنسکریت rāti-؛ پهلوی rat و ratīh». دوم «آراستن، پیراستن، ویراستن» که صورت‌های پیشونددارِ (ā-، *pati-، *vi-) یک فعل فارسی میانه‌اند: ārāy-/ārāst، pēray-/pērāst، wirāy-/wirāst. مأخذهای سنّتیِ نورایی همه اینها را از *rād- می‌گیرند: هرن شمارهٔ ۱۱ «آراستن … پارسی باستان √rād در rāsta- «درست»؛ اوستایی √rād- «سامان دادن»، rādaiti؛ پهلوی ārāstan» و شمارهٔ ۳۵۲ «پیراستن … pati + √rād-»؛ ابوالقاسمی در «ماده‌های فعل‌های فارسی دری» ص۲۴ می‌نویسد «آراست ← فارسی میانهٔ ārāst ← ایرانی باستان *ā-rād-ta … d پیش از t به s بدل شده است؛ rād به معنی «منظم کردن» است»؛ آریان‌پور نیز در فرهنگ ریشه‌های هندواروپایی، آراستن را با اوستایی ARADH و سنسکریت RĀDHNOTI و آلمانی RATEN می‌سنجد. در برابر اینان، چونگ (۲۰۰۷) و ویکی‌واژه آراستن و پیراستن را ذیل ایرانی آغازین *Hraz- از *h₃reǵ- «راست کردن» (ریشهٔ لاتین regō و سنسکریت rājati) می‌آورند. پس ادعای نورایی با احتیاط پذیرفتنی است، ولی برای سه واژه از چهار واژه دیگر روایت رسمی نیست. تحول معنایی هر سه روشن است: آراستن «سامان دادن» ← «زینت کردن»؛ پیراستن «گِردِ چیزی را سامان دادن» ← «هرس کردن»؛ ویراستن «جدا و مرتب کردن» ← (احیای سدهٔ چهاردهم خورشیدی) «ویرایش کردن».\",\n     \"sources\": [W+\"%D8%A2%D8%B1%D8%A7%D8%B3%D8%AA%D9%86\", W+\"%D8%B1%D8%A7%D8%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:30,437,926,927\", \"status\": \"supports\", \"note\": \"All four are right, within the ±2 drift of the OCR leaf→page mapping. BQT_v1_pages.txt leaves 238-241 (printed pp. 28-31) carry آرا، آرای، آرایش، آراست، آراسته (Nourai's script_extra آرایش، آرای); leaf 663 (p.437) has 'پیراستن: کم کردن چیزی باشد بواسطه زیبایی و خوش‌آیندگی همچو بریدن شاخه‌های زیادتی از درخت و موی زیادتی از بدن' with Onsori's quatrain 'کاراستن سرو ز پیراستن است', and leaf 661 (p.435) پیرایه; BQT_v2_pages.txt leaves 386-387 (printed ≈926-929) carry راد، رادبوی. Only ویراستن is not covered by any cited page (it stands in vol. 4, letter و).\"},\n      {\"ref\": \"AEF:428\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asās-e Eštéqāq-e Fārsi is the Persian translation of Horn's Grundriss and is not digitised. Checked its original instead: Horn no. 11 (ārāsten) and no. 352 (pīrāsten), quoted below — which is what AEF:428 must reproduce.\"},\n      {\"ref\": \"FFD:24\", \"status\": \"supports\", \"note\": \"Abolghasemi, Māde-hā-ye Feʿl-hā-ye Fārsi-ye Darī, printed p.24 (FFD_pages.txt pdf page 29): 'آراستن — آراست ← فارسی میانهٔ ārāst ← ایرانی باستان *ā-rād-ta. ā پیشوند فعلی است … rāš صورت اصلی rād است؛ d پیش از t به s بدل شده است؛ rād به معنی «منظم کردن» است … آرای ← فارسی میانهٔ ārāy ← ایرانی باستان *ā-rād-a.' Exactly Nourai's derivation, from a modern Iranian handbook.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss nos. 11, 352, 601 (HRN.txt lines 581, 3320, 5391)\", \"stance\": \"supports\", \"note\": \"no. 11 'ārāsten \\\"schmücken\\\" … ap. √rād in rāsta- \\\"richtig\\\"; aw. √rād- \\\"zurechtmachen\\\", rādaiti; phlv. ārāstan, ārāy(i)šn; ai. √rādh-' (footnote: 'Vgl. auch phlv. vīrāstan, vīrāyišn; hamrāstan'); no. 352 'pīrāsten \\\"schmücken, anordnen\\\" … pati + √rād- (s. ārāstan No. 11); phlv. pērāy(i)šn; arm. LW. patrast'; no. 601 'rād \\\"freigebig\\\": aw. vergl. arāiti-; ai. rāti-; phlv. rat, ratīh'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupāyi, printed p.52 (ARY_latin_index_pages.txt, pdf page 51)\", \"stance\": \"supports\", \"note\": \"the آراستن article's comparanda column reads 'ARADH, -RADH (AVESTAN) / RADHNOTI, RADHYATI, RADH- (SANSKRIT) / RĒRI (LATIN) / GAREDAN, REDAN (GOTHIC) / RĀDAN, RǢDAN, READ (OLD ENGLISH) / RATEN (GERMAN) / ARASTAN (PAHLAVI) / RADITI (OLD CHURCH SLAVIC)' — the Horn/Pokorny account.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *Hraz, pp. 196-198\", \"stance\": \"contradicts\", \"note\": \"'*NWIR: … (+ *api- ?) NP pērastan/pēray- \\\"to adorn, decorate\\\" … (+ *ā-) NP ārastan/āray- \\\"to adorn\\\" … *PIE *h₃reǵ- \\\"to stretch, direct\\\" = LIV: 304 f. | Pok.: 854 f.' — a different PIE root for three of the four words.\"},\n      {\"src\": \"FFD\", \"where\": \"Abolghasemi p.24\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 1 pp. 28-31, 435, 437; vol. 2 pp. ≈926-929\", \"stance\": \"supports\", \"note\": \"all the headwords present; Borhan gives no etymology of its own, only Mo'in's cross-references.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-61.json','w',encoding='utf-8') as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build61.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-61.json > /dev/null && echo \"JSON VALID\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 61"
}
```


### [2026-09-04T23:29:05.602Z] TOOL RESULT

```
ok
JSON VALID
nodes verified: 15/15
node verdicts: {'confirmed': 9, 'disputed': 2, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'not_checked': 8, 'partial': 3, 'not_found': 1, 'supports': 14}
books consulted: {'supports': 33, 'silent': 6, 'contradicts': 4, 'partial': 4} | by book: {'KLN': 6, 'NYB': 5, 'BQT': 4, 'FSD': 3, 'SKT': 3, 'BRT': 3, 'PHD': 3, 'AFM': 2, 'LAT': 2, 'POK': 2, 'CHEUNG': 2, 'LKT': 1, 'DEV': 1, 'WEB': 1, 'KNT': 1, 'IEC': 1, 'SOD': 1, 'SNS': 1, 'MON': 1, 'AHD': 1, 'HRN': 1, 'ARY': 1, 'FFD': 1}
```


## [2026-09-04T23:29:29.674Z] AGENT

Written and validated: `/home/sfmqrb/git/rishe/data/verification/page-61.json` (`verify_check.py 61` → 15/15 nodes, no PROBLEM lines).

**Page 61 (book p.31), 2 entries, 15 nodes**
- Node verdicts: 9 confirmed, 3 plausible, 2 disputed, 1 transcription_suspect
- Root verdicts: 1 confirmed (`Ar, Are` = PIE *h₂er-, POK:55 verified verbatim), 1 plausible (Semitic `A.q.r`)
- Ref checks: 14 supports, 3 partial, 1 not_found, 8 not_checked (FVA, AHD 1976 ed., MON 6-vol, TZF, AEF — none digitised)

Disputed / suspect items:
- **A.q.r · #4 Greek `skorpios`** — disputed. Klein:1401 does say "prob. ult. connected with Heb. ʿaqrabh" (citing A. Schott 1936), but he is the only support; Beekes/Wiktionary call σκορπίος Pre-Greek, Skeat and Etymonline attach it to PIE *(s)ker- "to cut". The Semitic→Greek arrow is rejected today.
- **Ar, Are · #2 Persian `ard` «ارد۲» (25th day)** — disputed. Nourai's own reference contradicts him: Mo'in's footnote in Borhan-e Qateʿ vol.1 p.98 derives the day-name from Av. *Aši (vaŋuhī)* (MP Ard), i.e. Pokorny's **2.** ar- "to allot" (IEW 61), not ar-1 "to fit"; MacKenzie likewise keeps "Ard, a goddess; cal. 25th day" apart from "ardā righteous". (The rest of the box — Ardašīr, Ardavān, nard < nēw-Ardaxšīr per Nyberg — is sound.)
- **Ar, Are · #4 Avestan** — transcription_suspect, `error_in: "book"` (page image checked; the JSON is faithful). The book prints "aša-van, **ša-vant**" and a separate line "**asvan** : holy, sacred"; both are misprints for *ašavan-/ašavant-* (Pokorny p.56 prints ašāvan(t)- with the a-; Bartholomae has no *šavant-/*asvan-).

Also worth the owner's attention (not flagged as errors):
- **KLN:1404** (Hebrew node) is a **wrong page number** — Klein p.1404 is "scourge–scran"; the ʿaqrābh statement is on p.1401. Likely a slip for 1401.
- **POK:56** on node #7 is the wrong page: Pokorny's Av. *rādaiti* / NP *ārāstan* material is on pp.59-60 (WLD:74, the other citation, is exactly right).
- Nodes #7/#8 marked *plausible*: Horn (nos. 11, 352, 601), Pokorny, Abolghasemi (FFD p.24, quoted) and Aryanpur all derive ārāstan/pīrāstan/vīrāstan from *rād-, but Cheung 2007 (pp.196-198) and Wiktionary refer them to Proto-Iranian *Hraz- < PIE *h₃reǵ-. `راد` itself is fine (< *h₂reh₁dʰ-).

No extraction errors found: every questioned form matches the printed page.
