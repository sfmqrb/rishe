# Verification process log — verify-page-62


## [2026-09-04T23:02:57.980Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 62 only (note the recently added requirements: `derivation_fa`/`note_fa` Persian explanations, and `error_in`/`book_prints`/`correct_form` on any transcription flag). Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-62.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-62.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-62.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 62` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T23:02:59.323Z] AGENT

I'll start by reading the instructions file.


## [2026-09-04T23:03:01.355Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T23:03:01.371Z] TOOL RESULT

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


## [2026-09-04T23:03:02.195Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-62.txt"
}
```


### [2026-09-04T23:03:02.215Z] TOOL RESULT

```
1	=== PDF page 62 (book page 32) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ar, Are : to fit together  (refs POK:55)  PART 2
4	#1 (parent #0) [Avestan] refs=WLD:74; POK:56 | ratu : judge, religious leader
5	  #2 (parent #1) [Pahlavi] refs=SNS:226 | rad : leader, master, Sir
6	    #3 (parent #2) [Persian] refs=BQT:943; MON:1645; FSF:199 | rad «رَد» : leader, judge, hero, wise
7	#4 (parent #0) [Avestan] refs=POK:56 | arânte : puts in order ; aram, arem : suitable
8	  #5 (parent #4) [None] refs=None | 
9	#6 (parent #0) [Old Persian] refs=WLD:74; POK:56; KNT:205 | râd 1, râdiy : cause, reason because of, due to
10	  #7 (parent #6) [Persian] refs=NYB:164; BQT:926; AEF:250 | râ «را» : due to, for ; čerâ «چرا ؟» : for what ?
11	#8 (parent #0) [Greek] refs=AHD; POK | harmos : joint ; arthro-itis : inflammation of joints, arthritis ; arithmus : number ; logos-arithmus : ratio number, logarithm ; arma : arms, weapons
12	  #9 (parent #8) [French] refs=None | harmonie ; arthrose ; logarithme
13	    #10 (parent #9) [Persian] refs=MON:3619,5082; AMD:24 | hârmonî «هارمونی» ; ârtotoz «آرتروز» ; logaritm «لگاریتم»
14	  #11 (parent #8) [Arabic] refs=BQT:96 | arbah, arobeh : arms, war chariot
15	    #12 (parent #11) [Persian] refs=BQT:96; MON:2286 | arrâbeh «ارّابه» : cart, war chariot | extra: عرّاده
16	  #13 (parent #8) [English] refs=None | harmony, arthritis, arithmetic, logarithm, arms, army, alarm
17	#14 (parent #0) [Latin] refs=AHD | ars : skill ; reri : to consider ; ôrdô : row of threads in loom
18	  #15 (parent #14) [French] refs=AHD | 
19	    #16 (parent #15) [Persian] refs=MON:41 | ârtîst «آرتیست»
20	    #17 (parent #15) [English] refs=AHD | art, artist
21	  #18 (parent #14) [English] refs=None | order, coordinate, ordinary, reason, ratio, rate
22	#19 (parent #0) [Germanic] refs=AHD | 
23	  #20 (parent #19) [English] refs=None | read, arm
24	--- entry 1 ---
25	ROOT Araq -> redirect to A.r.q
26	
```


## [2026-09-04T23:03:05.313Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-62.json",
 "description": "Read source JSON for page 62"
}
```


### [2026-09-04T23:03:05.356Z] TOOL RESULT

```
{
  "pdf_page": 62,
  "book_page": 32,
  "entries": [
    {
      "root": {
        "name": "Ar, Are",
        "lang": "Indo-European",
        "refs": "POK:55",
        "gloss": "to fit together"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "WLD:74; POK:56",
          "words": [
            {"translit": "ratu", "gloss": "judge, religious leader", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:226",
          "words": [
            {"translit": "rad", "gloss": "leader, master, Sir", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:943; MON:1645; FSF:199",
          "words": [
            {"translit": "rad", "gloss": "leader, judge, hero, wise", "script": "رَد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "دل بخردان داشت و مغز رَدان - دو کتف یلان و هُش موبدان",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:56",
          "words": [
            {"translit": "arânte", "gloss": "puts in order", "script": null},
            {"translit": "aram, arem", "gloss": "suitable", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "WLD:74; POK:56; KNT:205",
          "words": [
            {"translit": "râd 1, râdiy", "gloss": "cause, reason because of, due to", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "NYB:164; BQT:926; AEF:250",
          "words": [
            {"translit": "râ", "gloss": "due to, for", "script": "را"},
            {"translit": "čerâ", "gloss": "for what ?", "script": "چرا ؟"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "دشمن به قصد حافظ اگر دم زند چه باک - منّت خدای را که نیم شرمسار دوست",
            "poet": "Hâfez"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD; POK",
          "words": [
            {"translit": "harmos", "gloss": "joint", "script": null},
            {"translit": "arthro-itis", "gloss": "inflammation of joints, arthritis", "script": null},
            {"translit": "arithmus", "gloss": "number", "script": null},
            {"translit": "logos-arithmus", "gloss": "ratio number, logarithm", "script": null},
            {"translit": "arma", "gloss": "arms, weapons", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "harmonie", "gloss": null, "script": null},
            {"translit": "arthrose", "gloss": null, "script": null},
            {"translit": "logarithme", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:3619,5082; AMD:24",
          "words": [
            {"translit": "hârmonî", "gloss": null, "script": "هارمونی"},
            {"translit": "ârtotoz", "gloss": null, "script": "آرتروز"},
            {"translit": "logaritm", "gloss": null, "script": "لگاریتم"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 8,
          "lang": "Arabic",
          "refs": "BQT:96",
          "words": [
            {"translit": "arbah, arobeh", "gloss": "arms, war chariot", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "BQT:96; MON:2286",
          "words": [
            {"translit": "arrâbeh", "gloss": "cart, war chariot", "script": "ارّابه"}
          ],
          "script_extra": "عرّاده",
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "harmony, arthritis, arithmetic, logarithm, arms, army, alarm", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ars", "gloss": "skill", "script": null},
            {"translit": "reri", "gloss": "to consider", "script": null},
            {"translit": "ôrdô", "gloss": "row of threads in loom", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "French",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:41",
          "words": [
            {"translit": "ârtîst", "gloss": null, "script": "آرتیست"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 15,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "art, artist", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 14,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "order, coordinate, ordinary, reason, ratio, rate", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
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
            {"translit": "read, arm", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Araq",
        "redirect": "A.r.q"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-04T23:03:07.126Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T23:03:07.190Z] TOOL RESULT

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


## [2026-09-04T23:03:14.034Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','WLD','SNS','BQT','MON','FSF','KNT','NYB','AEF','AHD','AMD','FVQ','KLN','HRN','HUB','PHD','BRT','ARY','LKT','SKT','LAT','LEW','IEC','SYN','AFM','PLA','TAD','ARB']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-04T23:03:14.875Z] TOOL CALL #6: Bash

```json
{
 "command": "grep -n -iE '^(POK|WLD|SNS|BQT|MON|FSF|KNT|NYB|AEF|AHD|AMD)\\b' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -60"
}
```


### [2026-09-04T23:03:16.097Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

AMD {"title": "Hasan Amid, Farhang-e Farsi-ye Amid, 2 vols, Amir Kabir 1369/1990", "kind": "website", "url": "https://vajehyab.com/?q=<word>&d=amid ; https://abadis.ir/fatofa/<word>/ (فرهنگ عمید) ; scan on noorlib: https://noorlib.ir/book/view/28973?pageNumber=<N>&viewType=pdf", "lookup_hint": "Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Entry-level verification only."}

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo
```


### [2026-09-04T23:03:16.151Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T23:04:03.611Z] TOOL CALL #7: Bash

```json
{
 "command": "ls site/pages/62.jpg 2>/dev/null; pdftoppm -f 62 -l 62 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg62 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg62.png",
 "description": "Render PDF page 62 to PNG"
}
```


## [2026-09-04T23:04:05.494Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=60 && NR<=72' POK_01.txt | grep -n \"\" | sed -n '1,40p' | head -5; echo \"=== find ar- root page\"; grep -n \"zusammenfügen\" POK_01.txt | head -20",
 "description": "Find Pokorny ar- root"
}
```


### [2026-09-04T23:04:06.364Z] TOOL RESULT

```
site/pages/62.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 80701 Sep  4 19:04 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg62.png
```


### [2026-09-04T23:04:08.143Z] TOOL RESULT

```
1: Zusammenhang  mit  lat.  *a2nö,  *apere  ^comprehendere vinculO;  verbinden,  umbinden^  (imper.  ape  ,prohibe,  compesce'^),  aptus ^verknüpft,  ausgestattet  mit^,  cöpula  (co-apida)  ,Band*  steht  wohl  fest. Vielleicht  ist  von  einer  gemeinsamen  Grundbedeutung  ^fassen,  zusammen- fassen^ auszugehen.
2:Auch  lat.  apud  ,bei^  wird  am  besten  hierherzustellen  sein.  Die  Grund- bedeutung wäre  ,in  naher  Verbindung^  (vgl.  juxta).  Man  hat  vom  Part. Perf.  neutr.  *apiwd  (aus  *apuot  ^erreicht  habend^  auszugehen.  Die  Neben- form apor,  apur  (mars.-lat.  apur  finem)  weist  auf  ursprüngl.  -d]
3:lat.  apeXy  -icis  ,Spitze^,  bes.  ,stabartiger  Aufsatz  auf  der  Priestermütze*^; gehört  vielleicht  zu  *apw]  vgl.  auch  EM.  60;
4:toch.  A  oppäcgi  ^geschickt^  (Van  Windekens  Lexique  82);
5:hitt.  e-ip-mi  (epmi)  ,nehme^,  3.  PI.  ap-pa-an-zi  (^apanzi).
=== find ar- root page
773:Lat.  artus  ,eng  in  Raum  und  Zeit,  straff'  (Adv.  arte,  ursprüngl.  Instru- mental wie  ä(.Lagzrj)]  ars,  -tis  ,die  Geschicklichkeit,  Kunst,  Art  und  Weise' (eigentlich  , Zusammenfügung,  Gabe  richtig  zusammenzufügen'  =  mhd. art),  dazu  die  Komposita  in-ers  ,kunstlos,  träge',  soU-ers  ,geschickt',  allers, alers  ,gelehrt';  artlö,  -Ire  ,fest  zusammenfügen,  zusammenpressen'  (jünger artäre)]  artus,  -üs  , Gelenk,  Glied',  articulus  ,ds.;  Augenblick,  Wende- punkt';
```


## [2026-09-04T23:04:12.990Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=63 && NR<=65 {print \"=== LEAF \" NR \" (printed p.\" NR-8 \") ===\"; print}' POK_01.txt",
 "description": "Print Pokorny pages 55-57"
}
```


### [2026-09-04T23:04:15.309Z] TOOL RESULT

```
=== LEAF 63 (printed p.55) ===
dd.  ebbe,  woher  nhd.  Ebbe  entlehnt,  als  , Abfluten'^).
Ai.  dpäka-  ,abseits  liegend,  entfernt,  von  vorn  kommend^,  arm.  haka- als  1.  Kompositionsglied  ,entgegen'^,  hakem  ,piegare  ad  una  parte,  inclinare^, aksl.  opaky  ,wiederum'^,  ksl.  opako,  opaky,  opace  ,zurück,  verkehrt^  in welchen  freilich  z.  T.  auch  zu  *opi,  gr.  otil^bv  gehörige  Formen  stecken können  (vgl.  lat.  opäcus  ,schattig^  =  ,von  der  Sonne  abgewendet^;  Liter, zur  Bildung  bei  Brugmann  Grdr.  IP  1,  482).  Daneben  anord.  ofugr  ,nach rückwärts  gekehrt^,  as.  abuh,  avuh,  ahd.  abuh,  abah  ,abgekehrt,  verkehrt, böse^  (nhd.  äbig,  äbicht),  ags.  *afoc  in  engl,  awkicard,  aus  *apu-ko-s  (oder aus  "^opu-ko-s :  ojtL&sv,  so  daß  im  Ablaut  zu  got.  ibiiks  ,rückwärts  gehend^, ahd.  ippihhön  ,zurückrollen^?  Johansson  PBrB.  15,  230,  im  Konsonanten auf  Ttv-yrj  verweisend,  s.  auch  Falk-Torp*  u.  avet).
po:
av.  pa-zdayeiti  ,läßt  wegrücken,*scheucht'^;  lat.  2:)o-sitiis,pönö  aus  *po-s[{]nö, po-liö,  po-lübrum,  pörcet  aus  *po-arcet]  alb.  pa  m.  Akk.  ,ohne-,  pa-  ,un-^ (Gl.  Meyer  Alb.  Wb.  317);  afries.  fän  ,von',  as./awa,  /an,  ahd./ona,  fon m.  Dat.  (=  *Abl.)  ,von^  (das  ahd.  -o-  ist  nach  Persson  IF.  2,  215  aus  idg. *pu  neben  *po  herzuleiten).  Eine  ähnliche  Form  sucht  Trautmann  Apr.  389 in  apr.  pan-s-dau  ,danach'^.  GänzKch  unsicher  ist,  ob  arm.  olork  ,poliert, schlüpfrig,  glatt'  nach  Liden  Arm.  St.  60  ff.  o-  aus  ""po-  enthält.  Dagegen hierher  trotz  vielfach  abweichender  Bed.  (Brugmann  Grdr.  II ^  2,  808 erwägt  Aufsaugung  von  idg.  "^upo,  und  für  sl.  po  in  der  Bed.  ,hinter, nach'  m.  Lok.  wohl  richtig  Entstehung  aus  '^pos):  aksl.  po  ,nach,  an,  bei, über  etwas  hin'  (lit.  pö  mit  Gen.  u.  Dat.  ,nach',  mit  Instr.  ,unter'),  als wesentlich  nur  mehr  perfektivierendes  Verbalpräfix  lit.  pa-,  aksl.  po-  (als Nominalpräfix  aksl.  pa-,  lit.  pa  und  pö-,  vgl.  z.  B.  aksl.  pamhnUi  ,sich erinnern',  pa772^^6  ,Andenken');  apr.  pa-  wesentlich  in  nominaler,  pö-  in verbaler  Kompos.,  vgl.  Trautmann  203,  Meillet  Slave  comm.^  505.
55
Über  slav.  po-d^  ^unterhalb,  unter^  s.  Brugmann  Grdr.  IP  2,  733  f.  — S.  noch  idg.  ""po-ti  und  "po-s.
ap-u  steht  neben  ^ajw  (Lit.  s.  u.  *pu)  in  ark.  kjpr.  lesb.  thess.  äftv^'  in alid  abo  ='  ciba,  anord.  au-virdi  n.  ^verächtliche  Person^  (Falk-Torp  HL), yo-l,  auch  oben  *a'pu-ro-  neben  '^^apero-,  *apu-ko-,  und  *pu  neben  *po.  Das -u  vielleicht  enklit.  Partikel  ;,und,  au
=== LEAF 64 (printed p.56) ===
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
=== LEAF 65 (printed p.57) ===
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
```


## [2026-09-04T23:04:35.740Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK radiy ===\"; grep -n -iE 'r[aä]diy' POK_01.txt | head -20; echo \"=== POK arithm/harmos/harma ===\"; grep -n -E 'ägi&fiog|dgi&fiog|agid|arithm' POK_01.txt | head -10; echo \"=== POK leaf 66-67 (p58-59) ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=66 && NR<=68 {print \"=== LEAF \" NR \" (p.\" NR-8 \") ===\"; print}' POK_01.txt | head -80",
 "description": "Search Pokorny for radiy, arithmos"
}
```


### [2026-09-04T23:04:38.037Z] TOOL RESULT

```
=== POK radiy ===
794:Ai.  rädhnöti,  rädhyati  ;macht  (passend)  zurecht;  bringt  zustande;  gerät; gelingt;  hat  Glück  womit;  befriedigt;  gewinnt  jemanden';  rädhayati  ;bringt zustande;  befriedigt';  rädha-h  m.,  rädhah  n.  ;Segen;  Gelingen;  Wohltat, Gabe;  Freigebigkeit';  av.  rädaiti  ;macht  bereit',  rada-  m.  ;Fürsorger'; rädah-  n.  , Sichbereitstellen,  Bereitwilligkeit  (in  religiöser  Hinsicht)',  apers. rädiy  (Lok.  Sg.)  , wegen'  (vgl.  aksl.  radi  s.  unten),  npers.  äräyad,  ärästan ,schmücken';  air.  imm-rädim  ;überlege;  überdenke';  acynir.  amraud  ;mens'; ncymr.  amrawdd  ;Gespräch'  mit  ders.  Bed.  wie  air.  no-räidiu,  no-rädi^n jSage',  mcjmr.  adrawd  ,erzählen'  und  got.  rödjan^  anord.  reda  ,reden^ (vgl.  auch  oben  nhd.  Rede,  reden]  no-räidiu  und  rödjan  setzen,  wie  sL, raditi,  ein  kaus.-iter.  *rödheiö  fort);  got.  garedan  ,worauf  bedacht  sein, Vorsorge  treffen',  urredan  ,urteilen,  bestimmen'  (vgl.  zur  Bed.  bes.  lat. rerl),  undredan  , besorgen,  gewähren',  ahd.  rätan  , raten,  beratschlagen, worauf  sinneu;  anstiften,   deuten  (Rätsel),    auffordern,  wofür  sorgen,  ver-
=== POK arithm/harmos/harma ===
320:Lat.  occa  ,Egge^  aus  *otikä  durch  Umstellung  aus  *okitä  (Hirt  IF.  37, 230)?  Vgl.  das  anders  gebildete  gr.  ö^Ivt]  ,Egge^;  acymr.  ocet,  corn.  ocet^ bret.  oguet:  ahd.  egida,  mhd.  eg{e)de,  ags.  eg{e)de  f.  (nhd.  Egge  geneuert mit  dem  Verbum  eggen  aus  ahd.  egen,  ecken,  urgerm.  *agjan,  das  seiner- seits erst  aus  dem  Subst.  *agidö  rückgebildet  ist);  lit.  akecios,  ekeölos ,Egge^,  apr.  aketes  ,Eggen'^,  das  e  statt  e  stammt  von  dem  Verbum  *a/mö in  lit.  akeju,  aketi,  daneben  akeju,  eketi]  das  anlautende  a-  ist  in  unbe- tonter Stellung  vor  palatalem  Vokal  oft  zu  e  geworden  (Endzelin  Lett. Gr.  36).
635:Ai.  ärdgam  ^Glied',  ai9güli-h,  aidgüri-k  f.  ^Finger,  Zehe'  (davon  aTagidlyam ^Fingerring');  cmgustha-h  ,große  Zehe,  Daumen'  ==  av.  angusta-  m.  ;Zehe', arm.  ankiun,  angiun  ^W^inkel'  und  anjali-h  m.  ;die  beiden  hohl  aneinander, gelegten  Hände';
=== POK leaf 66-67 (p58-59) ===
=== LEAF 66 (p.58) ===
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
=== LEAF 67 (p.59) ===
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
=== LEAF 68 (p.60) ===
;  nhd.  gerad  (nur  von  durch  2  teilbaren  Zahlen;  verschieden von  gerad  =  geradeaus);  mit  neuem  Ablaut  anord.  tl-redr  eigentlich  ;nach Zehnern  gezählt'  (Fick  III^  336);  got.  rapjö  ;Zahl;  Rechnung;  Rechen- schaft'; as.  rethia  jR^chenschaft';  ahd.  radja,  redea  ;Rechenschaft;  Rede und  Antwort;  Rede,  Erzählung';  afries.  hirethia  ;anklagen';  as.  rethiön^ ahd.  red(i)ön  , reden'  (die  genaue  Übereinstimmung  von  rapjö  mit  lat. ratio  bestimmt  z.  B.  Kluge  ^^  s.  v.  ,Rede'  zur  Annahme  von  Entlehnung des  germ.  Wortes  unter  Einfluß  von  garapian,  richtiger  scheint  mir Falk-Torp  886  rapjö  als  primäre  -löTi-Ableitung  von  der  germ.  Wz.  *rap- [garapjan]  zu  bestimmen).
Ob  hierher  auch  anord.  rgd  ;Reihe;  bes.  dem  Strande  entlang  ziehende Erhöhung^;  mnd.  rat  f.  ;Reihe'?  (Fick  IIP  337;  ;Reihe'  als  ;aneinander Gefügtes,  Geschichtetes'?).
Ahd.  rämen  ;nach  etwas  trachten,  streben,  zielen';  as.  römon  ^streben'; mhd.  mnd.  räm  ,Ziel'  kann  als  ;geistig  zurechtlegen;  berechnen'  unserem *re-  zugehören,  wenn  auch  dabei  das  (erst  jünger  belegte)  Subst.  räm als  Bildung  mit  Formans  -mo-  der  Ausgangspunkt  gewesen  sein  muß.
dh-Erweiterung  re-dh-,  rö-dh-,  rs-dh-:
Ai.  rädhnöti,  rädhyati  ;macht  (passend)  zurecht;  bringt  zustande;  gerät; gelingt;  hat  Glück  womit;  befriedigt;  gewinnt  jemanden';  rädhayati  ;bringt zustande;  befriedigt';  rädha-h  m.,  rädhah  n.  ;Segen;  Gelingen;  Wohltat, Gabe;  Freigebigkeit';  av.  rädaiti  ;macht  bereit',  rada-  m.  ;Fürsorger'; rädah-  n.  , Sichbereitstellen,  Bereitwilligkeit  (in  religiöser  Hinsicht)',  apers. rädiy  (Lok.  Sg.)  , wegen'  (vgl.  aksl.  radi  s.  unten),  npers.  äräyad,  ärästan ,schmücken';  air.  imm-rädim  ;überlege;  überdenke';  acynir.  amraud  ;mens'; ncymr.  amrawdd  ;Gespräch'  mit  ders.  Bed.  wie  air.  no-räidiu,  no-rädi^n jSage',  mcjmr.  adrawd  ,erzählen'  und  got.  rödjan^  anord.  reda  ,reden^ (vgl.  auch  oben  nhd.  Rede,  reden]  no-räidiu  und  rödjan  setzen,  wie  sL, raditi,  ein  kaus.-iter.  *rödheiö  fort);  got.  garedan  ,worauf  bedacht  sein, Vorsorge  treffen',  urredan  ,urteilen,  bestimmen'  (vgl.  zur  Bed.  bes.  lat. rerl),  undredan  , besorgen,  gewähren',  ahd.  rätan  , raten,  beratschlagen, worauf  sinneu;  anstiften,   deuten  (Rätsel),    auffordern,  wofür  sorgen,  ver-
60
schaffen',  as.  rädan,  anord.  räda,  ags.  7'zdan  (letzteres   auch  ,Iesen',  eno read),  Subst.  ahd.  rät  m.  ^vorhandene  Mittel,  Rat,  Ratschlag,  Überlegung Entschluß,   Absicht,  Vorsorge,  Vorrat',   ähnlich   as.    räd,   anord.  räd,  ag rxd]   aksl.    raditi   ,sorgen'   (serb.    rädim,    rdditi   ,arbeiten,    trachten',   rai , Geschäft,  Arbeit';    s.   ühlenbeck  KZ.  40,  558  f.),   radi   ,wegen',    woneben *raJA-  in  aksl.  nerod^  ,Vernachlässigung',  sloven.  rqdim,  rqditi  , so
```


## [2026-09-04T23:05:00.456Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=69 && NR<=70 {print \"=== LEAF \" NR \" (p.\" NR-8 \") ===\"; print}' POK_01.txt; echo \"###### ordo search\"; grep -n -E \"ordö|ordo,|,Reihe.*ordo|ordior\" POK_01.txt | head",
 "description": "Pokorny pages 61-62 and ordo"
}
```


### [2026-09-04T23:05:03.035Z] TOOL RESULT

```
=== LEAF 69 (p.61) ===
rgen,  sich kümmern'.
Wzf.  {a)rl-,  rei-  (s.  Person  Wzerw.  102,  162,  232;  Beitr.  741):
Gr.  dgaglayiw  (wenn  nicht  Neubildung,  s.  oben  S.  56),  äoLd-^dg  ,Zahl',  vi^giroq , ungezählt',  arkad.  ircdgirog  ^iTtlXs'ATog,  auserlesen',  dQLjxd^SL'  äQ^xot^ei  Hes. lat.  rltuSj  -üs  ,hergebrachte  Art  der  Religionsübung,  Gebrauch,  Sitte,  Ge- wohnheit, Art',  nie  ,in  passender  Art,  nach  dem  rechten  religiösen  Ge- brauch^ (Lok.  eines  neben  rl-tu-s  liegenden  kons.  St.  *7'I-^);  air.  rim  ,ZahP, äram  (*ad-ri-ma)  ds.,  do-rimu  ,zähle',  cymr.  rhif  ,Zahl',  anord.  nm  n. , Rechnung,  Berechnung',  as.  unrim  , Unzahl',  ags.  rm  n.  ,Zahl',  ahd.  rim m.  ,Reihe,  Reihenfolge,  Zahl'  (die  Bed.  ,Vers,  Reim'  von  anord.  und  mhc rim  wohl  nach  Kluge  ^'^  s.  v.  Beim  aus  frz.  rime,  das  aus  rythmus  her- zuleiten ist).
Vielleicht  ist  auch  *m-  , Sache'  (lat.  res  usw.)  nach  Wood  a^  226  an- zureihen als  Wznomen  der  Bed.  , aufgestapeltes  Hab  und  Gut'.
Dazu  wahrscheinlich  als  JA-Erweiterung  rei-dh-  (vgl.  oben  re-dh neben  re-):
Got.  garaips  , angeordnet,  bestimmt',  raldjan,  garaidjan  ,verordnen,  he- stimmen',  anord.  g-reidr  , bereit,  leicht,  klar',  greida  , auseinanderwickeln ordnen,  zurechtlegen,  zustande  bringen,  entrichten,  zahlen',  mhd.  reiten ,zurüsten,  bereiten,  zählen,  rechnen,  berechnen,  bezahlen',  reite,  gereite bereite,  ahd.  hireiti  ,bereit',  antreltl  ,series,  ordo',  lett.  riedu,  rizt  , ordnen raids  ,bereit,  fertig',  ridi,  ridas  , Gerät,  Kram'.
Ganz  fraglich  ist  die  von  Persson  aaO.  erwogene  Zugehörigkeit  von aksl.  orqdije  ,apparatus,  instrumentum'  (nicht  aus  ahd.  ärunti  , Botschaft' entlehnt,  s.  Pedersen  KZ.  38,  310),  red^  ,Ordnung',  lit.  rinda  ,Reihe', lett.  rinda  ,Reihe,  Zahl'.  Unter  der  Voraussetzung,  daß  diese  idg.  d,  nicht dh  fortsetzen  (*re-n~d-),  reiht  man  (z.  B.  Fick  I*  527,  Pedersen  aaO., s.  auch  EM.  711)  auch  die  folgende  Sippe  an:  Sgöeo)  ,lege  ein  Gewebe an',  6qölx6v'  töv  x^tcüvIg-aov.  Rägioi,  h'QÖrjua'  fj  toIvtct]  t&v  iglcov  Hes., lat.  ördior,  -iri,  örsus  sum  (aus  der  Webersprache,  Breal  MSL.  5,  440) , anzetteln,  anreihen,  anfangen,  beginnen',  exördior  ,zettle  ein  Gewebe  an'. redördior  ,hasple  ab',  ördo,  -inis  ,Reihe,  Ordnung'  (auch  umbr.  urnasier scheint  =  ordinariis  zu   sein,  Linde   Glotta  3,  170 f.;  anders  Gl.  5,  316),
61
T-ifft  der  Zusammenhang  mit  ar-  ^fügen'^  das  dann  auch  von  der  Weberei <r  braucht  gewesen  wäre^  zu  (Persson  Wzerw.  26^  Thurneysen  Thes. 
=== LEAF 70 (p.62) ===
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
###### ordo search
```


## [2026-09-04T23:05:13.939Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls; grep -n \"pdf page\" WLD_Bd1_pages.txt | head -3; echo \"---\"; grep -n \"ratu\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20",
 "description": "Explore WLD Band 1"
}
```


### [2026-09-04T23:05:14.036Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
---
84:neten Literaturangaben. Die vom Vf. als druckfertig angesehenen Zettel 
91:seiuein Sinne die iibrige Literatur herangezogen habe. 
3592:Zusammenstellungen vgl. die Literatur in LEWb. 2 unter amo, -are und 
3725:KZ. 43, 276 und die dort angegebene Literatur; vgl. weiterhin lat. anus, 
3754:altere Auffassung (vgl. die Literatur bei Hermann aaO.) ist beachtenswert. 
4692:richter (vgl. z. Bed. u. gr. aoivvag); Richterspruch", ratu- .,Zeitabschnitt, 
4699:KZ. 32, 3) z- at cl „apparatus, ornatus", ard „soeben, jetzt“ (Bartholomae 
4879:begleitet), Ptc. ratus „in der Meinung", aber auch „berecht. bestimmt, 
5015:aksl. orqdije apparatus, instrumentum" (nicht aus ahd. urunti j.Botschaft" 
5431:„Silber“, gall. Argcnto-ratum, -magus u. dgl., arm. arcat „Silber“, mit anderer 
7664:Literatur). 
17540:porcus eastratus"). 
27987:ags. Milan „grunzen"; ahd. hluoticla ,.latratus“: mit Hochst. der ersten Silbe 
28674:„curaverunt“, u. kuratu „curato“; dazu allenfalls got. ushaista „diirftig“ als 
34034:Memoire 53 A. 1, oft nachgesprocken, s. die Literatur bei Boisacq 9) vgl. 
34369:air. goife ,,vulneratus“, mir. gaetas „qui occidit - ' ( *yhoizd-\ Fick II 4 
35502:unter yeeia zitierte Literatur (Petersson KZ. 47, 279 f. stellfc fovea zw. zu 
36496:umbr. naratu „narrato“, naraklum „nuntiatio" ; als Endglied von Zs. ai. 
36827:Literatur). 
37805:Air. gor „fromm“, goire „Frommigkeit, Pietiit" (s. Yf. LE\Vb. 2 unter gratus
```


## [2026-09-04T23:05:18.964Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '4660,4720p' WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== check page marker near\"; sed -n '4620,4665p' WLD_Bd1_1930_dli_70244_djvu.txt | grep -nE '^\\s*[0-9]{1,3}\\s*$'",
 "description": "Read WLD Bd1 ar- entry"
}
```


### [2026-09-04T23:05:22.031Z] TOOL RESULT

```
an ardm , arante anzuschliefien, vgl. Scheftelowitz ZDMG. 59, 693“ [der aber 
Jra- als „Schar“ mit air. tall „Trupp, Herde“, lit. eile „Reihe, Schicht“ 
vergleicht; fur letztere steht ei- „gehn“ als Wz. zur Erwagung], 

Mit Zerdehnung opr]oos „Gatte; Geisel, Unterpfand", ourjor.co „treffe zu- 
sanimen'''. 

Aus dem Slav, vielleicht poln. ko-jarzyc „kniipfen, verbinden, vereinigen“ 
(z. B. Miklosich EWb. 100, Berneker 31, 532). 

Uber das vielleicht verwandte gr. doa, lit. ir s. *ar „nun, also". — Zur 
Bed. „Fuge — Gelenk, Glied" ( ao&oov ) vgl. auch u. die Worte fur „A.rm“. Da- 
gegen bleiben trotz Persson Beitr. 634 f. besser bei der Sippe von c btevt] 
die Worte ai. aratni-h , ratni-li „Ellenbogen, Elle, Arm“, Ctni-h „der un- 
mittelbar liber dem Knie liegende Teil des Beines“ (mind, aus *arni - ; 
die Bed. ,in der Nabe laufender Achsenzapfen 1 beweist nicht fur Yer- 
wandtschaft mit ard-h j: Radspeiche“ und arpayati , sondern geht auf das 
Bild des in der Gelenkpfanne sich drehenden Knochenkopfes), av. ars&na- 
„Ellenbogen“, frurCi&ni- „Elle“ ( rcina - „Oberschenkel“?? I)och s. Fick 
I 4 339). 

t- Bildungen: 

Ai. rta- ,,passend, recht“, rtdm „\vohlgefiigte heilige Ordnung" (zur Bed. 
s. Oldenberg GGN. 1915, 167 — 180; nicht „Opfer“), rtena „rite“, av. cirota-, 
srata- n., ap. art a- (in Zs.) „Gesetz, Recht, heiliges Recht“, av. asa- n. 
,was recht, wahr ist“, ai. rtavan(t)- „ordnungsgemaB, gerecht", av. asavan(t)--, 
ai. rtu-h „bestimmte Zeit, Ordnung, Regel“, rtt-h „Art, Weise“ (zu unserer 
Wz. nach Kluge PBrB. 9, 193, s. auch Meringer IF. 17, 125; nicht besser 
nach Uhlenbeck Ai. Wb. 34 als „Lauf, Gang" zu Yr-, *or- „sich bewegen", 
was Oldenberg aaO. auch fur rta- zur Wahl stellt). av. aipi-mtu- „bestimmt, 
fest zugewiesen" ; mit themat. Yokal (*r-e-) av. vatu- m. „Richter, Schieds- 
richter (vgl. z. Bed. u. gr. aoivvag); Richterspruch", ratu- .,Zeitabschnitt, 
Zeitraum" (gemeinsame Gdbed. etwa „Zurechtlegung“, woraus „Zurecht- 
legung des Rechts“ und „richtiger Zeitpunkt"; formell vgl. zu ra-tu- auch 
o. ra-pi&icu): 

arm. aril, gen. -u (=gr. dgxvg, lat. artus, -us, vgl. auch o. ai. rtu-h) 
„struttura, costruzione, ornamento“ (Hiibschmann Arm. Gr. I 423, Bugge 
KZ. 32, 3) z- at cl „apparatus, ornatus", ard „soeben, jetzt“ (Bartholomae 
Stud. II 23, Bugge aaO.), ardur „gerecht“ (Hiibschmann Arm. St. I 21, 
Arm. Gr. 1 423; Persson Beitr. 636 a 2 erwagt dafiir auch idg. dh, vgl. 
av. arodra- „getreu, zuverlassig, glaubenstreu, fromm“ und die andern u. 
genannten f///- Ableitungen), arcliun „struttura“ (Pedersen KZ. 40, 210): 



ai- 


71 


gr. u/uagxrj „gleichzeitig“ (instr. eines *dfi-agx6g „zusammengefugt, zu- 
sammentreffend", Wackernagel GGN. 1902, 742 Anmert. 1, Brugmann 
Grdr. II 2 1, 29, Bechtel Lexil. 34), opagxeco „sich an jemanden an- 
schlieliien, begleiten 11 (auf Grund eines *o/u-agxog; nicht hesser nach Prell- 
witz 2 329 zu *er- „bewegen“) ; kons. St. *ar-t in bau-ao „Hausfrau“ („die 
des Hauses \valtende“ nach Schulze KZ. 28, 281, Qu. ep. 37, J. Schmidt 
Pl. 221 f., oder eher „Hausgenossin“, alter vermutlich Abstraktum „Haus- 
genossenschaft“ nach Brugmann IF. 28,294; -ag kaum bloB suffixales -rt, 
=== check page marker near
25:70
```


## [2026-09-04T23:05:29.112Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && awk 'NR>=4700 && NR<=5100' WLD_Bd1_1930_dli_70244_djvu.txt | grep -n -E '^\\s*7[0-9]\\s*$'; echo \"--- locate line of '74'\"; awk 'NR>=4700 && NR<=5200 && /^[[:space:]]*7[0-9][[:space:]]*$/ {print NR+4699\": \"$0}' WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Locate page 74 in WLD Bd1"
}
```


### [2026-09-04T23:05:30.808Z] TOOL RESULT

```
11:71 
69:72 
136:73 
199:74 
264:75 
323:76 
389:77 
--- locate line of '74'
9409: 71 
9467: 72 
9534: 73 
9597: 74 
9662: 75 
9721: 76 
9787: 77 
9848: 78
```


## [2026-09-04T23:05:40.854Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '4830,4905p' WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Print WLD Bd1 p.74"
}
```


### [2026-09-04T23:05:40.946Z] TOOL RESULT

```
ar- 


73 


groBen, miBgestalteten. crmingas „unformlich“, lett. (inns „Affe, Possen- 
reiBer, wunderliche Erscheinung"? [oder Lw. aus gr. agtjuogl]), das als 
„emporgeschossen“ zu *er~, *or- (prior usw. ; vgl. formell oopsvog), nicht 
als „festgefiigt, rnassiv" zu *ar- „fiigen“ gehort. — Koch fraglicher ist 
Wood’s Mod. langu. notes 21, 39 auf ai. ar-p-ayati gestiitzte Anreihung von 
anord. arfr „Ochs“, ags. icrfe, orf „Yieh, Hornvieh" („unters Joch ge- 
fiigtes"??; lit. arbonas (?) „Ochs“ = anord .arfnni, das idg. bh erwiese, konnte 
freilich germ. Lehnwort sein), s. u. orbho-. 

Aksl. jantm „Joeh“ (z. B. Miklosich EWb. 100, Berneker 31 ; wie sloven. 
jermen „Jochriemen, Riemen“ mit Anlautdehnung nach Pedersen KZ. 3S, 
311 — 318, wo auch iiber die trotz Reichelt KZ. 46, 319 vielleicht auf 
*ar(d)men- zuriickfiihrbaren aksl. rcment , serb. remen usw. „Riemen“, die 
also ebensowenig wie germ. *ermana s. o., als Zeugen fur vereinzelten 
e-Yokalismus der Wz. or- „fugen“ gelten konnen. 

Yon der set-Basis (wie oben si. *ar(d)men-) auch: 

ai. Irmd-h „Arm, Yorderbug" (ursprgl. „Achselgelenk“, vgl. ag&gov, lat. 
artus) = av. aroma- „Arm‘ . osset. arm „hohle Hand", dlm-drin , drm-drin 
„Ellenbogen“, apr. irmo „Arm“, lit. 'irmidc („ArmfraB“, d. i. :) ,,Gicht in 
den Gelenken", irm-liga „Gicht“ (s. Trautmann Apr. 347), hochstufig lit. 
zem. pi. tant. anna i „Yorderarm am Wagen" (ibd.), aksl. ramo, ram e, serb. 
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
wird vom Aufeinanderlegen oder -schichten der zu ziihlenden Stiicke 
begleitet), Ptc. ratus „in der Meinung", aber auch „berecht. bestimmt, 
giltig, rechtskriiftig" (vgl. auch random, rabamini Loewe Prodr. 346. fur 
die das it von rahis der Ausgangspunkt war), ratio „Berechnung, Erwii- 
gung, Yernunft, Beweggrund, Grund" 1 ); 

got. *garapjan (nur ptc. yarapana) ziihlen", an. handcart, nhd. Ifimdert 
(*rada- n. „Zahl“ = lat. ration; s. Fick III 4 336): ahd. yi rad „gerad (nur 


*) Uber lat. ratis „Flo&“ („Gefuge von Stammen“ ? ?) und retae (e nur vermutungs- 
weise angesetzt) 7 aus dem Ufer des Flusse.s liervorragende oder aus dem Flufibett her- 
vorstehende Baurne 1 " s. u. *rct- ,Stange, Stamm". Lit. riekh's ,Stangengcriist zum Trocknen, 
Raucbern' zu anord. ra ..Stange in einem Stangengeriist zum Trocknen, SchitRraa", 
mhd. rcihe „Stange, Sckiftsraa", mhd. rectc(e) „lange diinne Stange. bes. zum Uberhiingen 
von Kleidern*, Wz. *rek- „steif J (Persson aaO., Falk-Torp 8t‘8, 910). — Uber lat. rite 
(von Reichelt KZ. 4ti, 318 zu *ar-c n fugen' 1 gestellt) s. *er- n locker“. 



74 


ar- 


von Zahlen)**, nlid. gerad (nur von durch 2 teilbaren Zablen; verschieden 
von gerad = geradeaus) mit neuem Ablaut anord. ti-rpdr eigentlicb ,.naeh
```


## [2026-09-04T23:05:51.372Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '4963,5030p' WLD_Bd1_1930_dli_70244_djvu.txt | grep -n -iE 'radiy|rädiy|ap\\.|apers|wegen' ; echo \"=== full p75-76 excerpt\"; sed -n '4965,5025p' WLD_Bd1_1930_dli_70244_djvu.txt | head -45",
 "description": "Look for OP radiy in WLD Bd1 p.75-76"
}
```


### [2026-09-04T23:05:51.445Z] TOOL RESULT

```
44:fung der germ. Worte an *reidh- „fahren, sich bewegen", dt. reiten , so 
=== full p75-76 excerpt

verschiedenen Wz. radii- „sprecken“ nach Fick III 4 347. Falk-Torp 886, 
sondern setzen wie si. raditi ein kaus.-iter. *rodheio fort); got. garedan 
„worauf bedacht sein, Yorsorge treffen 11 , urredan „urteilen, bestimmen“ 
(ygl. zur Bed. bes. lat. rerl), undredan „besorgen, gewahren", ahd. redan 
„raten, beratschlagen, worauf sinnen, anstiften, deuten (Riitsel, auffordern, 
wofiir sorgen, verschaffen", as. radan, anord. rada , ags. radan (letzteres 
aucb „lesen“, engl. read ), Subst. ahd. rat m. „vorhandene Mittel, Rat, 
Ratschlag, Uberlegung, EntschluB, Absicht, Yorsorge, Yorrat“, ahnlich as. 
rad , anord. rad, ags. reed. 

Wzf. (a)rei-, ( a)rl - (s. Persson Wzerw. 102, 162, 232, Beitr. 741): 

gr. agagiaxm (wenn nicht Neubildung, 8. o.), doi&juog „Zahl“, vggnog „un- 
gezahlt", arkad. bidoaog (Schulze BPhYV. 1890, 1406! „lmkexxog, aus- 
erlesen“, doiud’Qu • doiioQn Hes.; lat. ritus, -us „hergebrachte Art der Reli- 
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

Yielleicht ist auch *rci- „Sache“ (lat. res usw.) nach Wood a 1 226 an- 
zureihen als Wznomen der Bed. „aufgestapeltes Hab und Gut“. 

Dazu nach Wood a x 227, Persson Beitr. S56f. wahrscheinlich als dh- 
Erweiterung (vgl. oben *re-dh- neben rc-): 

got. garaips „angeordnet, bestimmt", raidjan, garaidjan „verordnen, be- 
stimmen", anord. g-reidr „bereit, leicht, klar i£ , greida „auseinander\vickeln, 
ordnen, zurechtlegen, zustandebringen, entrichten, zahlen 1 , mhd. reiten „zu- 
riisten, bereiten, zahlen, reehnen, berechnen, bezahlen", rcite, gcreite, be- 
reite, ahd. bireiti „bereit“, antreiti „series, ordo‘‘, lett. riedu, rizl „ordnen“, 
raids „bereit, fertig", ridi , ridas „Geriit, Kram‘‘ (der bisherigen Ankniip- 
fung der germ. Worte an *reidh- „fahren, sich bewegen", dt. reiten , so 
daB z. B. bereit eigentlich „fahrbereit“ ware, fugen sich wenigstens nicht 
alle Bedeutungen, wahrend bereit andrerseits aus ,,passend hcrgerichtet" 
ohne weiteres zu gewinnen ist;. — Ob mit diesen germ. Worten gr. egldog
```


## [2026-09-04T23:05:57.541Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n -E 'ap\\. radii|radiy|radiij|rndiy|„wegen' WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"---- around 4940\"; sed -n '4930,4965p' WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Find OP radiy in WLD Bd1"
}
```


### [2026-09-04T23:05:57.618Z] TOOL RESULT

```
4949:Arbeit - *; s. Uhlenbeck KZ. 40, 558 f. ', radi „wegen“, woneben *radh- in 
29933:s. noch Berneker 128 iiber slav. *cet'a „wegen‘‘. 
52226:m. gen. „wegen“, lit. del, del , delicti, lett. del’ mit Gen. „wegen, nm willen". 
---- around 4940
ram als Bildung mit Formans -mo- der Ausgangspunkt gewesen sein muB. 

fZ/i-Erweiterung *re-dh-, ro-dh- (vgl. Persson Wzerw. 46, Brugmann Grdr. 
II 1 1047. Ygl. von nr- oben av. arodra-, ferner gr. dodoov, ag&fiog , 
wenn letztere nicht gr. Aeuschopfungen mit dem fertigen Suffixkonglutinat 
-{too-, -Pfio- sind. ebenso aoi&uog; aber ai. rdliati , rdhyati, rdhnoti , rnnddlii 
„gedeiht, gelingt, macht gelingen, bringt zustande“, Desid. Irtsati , ardlmka- 
„gedeihend - *, av. arodaiti , oroduiti ,,laBt gedeihen, fordert**, die Brugmann 
tfoyvg wegen der zu ru-dh- stimmenden Bed. aus *ar-dh- deutet, gehoren 
zu gr. aWoyai, at- „wacksen“; ferner unten got. garaips usw.); 

ai. radJnidti, rddhyati „macht (passend) zurecht, bringt zustande; gerat, 
gelingt, hat Gluck womit; befriedigt, gewinnt jemanden**, rudhayati „bringt 
zustande, befriedigt* 1 , radha-h ni., rfidhah n. „Segen, Gelingen, Wohltat, 
Gabe, Freigebigkeit'*, av. radaiti ,.macht bereit“, m. Dativ vurai ,.jemands 
YYi lien erfiillen, zu Willen sein“, rada- m. „Fursorger“, radah- n. „Sich- 
bereitstellen, Bereitwilligkeit (in religioser Hinsicht**, ap. rildiy (loc. sg.) 
„\vegen“ i vgl. aksl. radi s. u. , npers. arfiyad, arastan „schmiicken“; aksl. 
radii i „sorgen“ (serb. rddlm, rdditi „arbeiten, trachten**, rad „Geschaft, 
Arbeit - *; s. Uhlenbeck KZ. 40, 558 f. ', radi „wegen“, woneben *radh- in 
aksl. nerodz „Yernachlassigung“, sloven, rodim, r'oditi „sorgen, sich kiim- 
mern“ (lett. rrdit ,,ordnen, auszahlen, ausstatten** ist aber Lehnwort aus 
der Sippe von slav. rah „Ordnung“, z. B. Miklosich EWb. 276 i; air. imm- 
nldini „iiberlege, iiberdenke**, acymr. amraud „mens“, ncymr. amratodd 
jGesprach * mit ders. Bed. wie air. noraidiu, norudim ,.sage“, mcymr. 
adr aied „erzahlen“ und got. rddjan, anord. rpd.a ,,reden“ (vgl. auch oben dt. 
Jhdc. reden ; noraidiu und rddjan erfordern also nicht den Ansatz einer 



ar- 


75
```


## [2026-09-04T23:06:07.124Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT radiy ===\"; grep -n -iE 'radiy' KNT.txt | head -20",
 "description": "Kent radiy"
}
```


### [2026-09-04T23:06:07.169Z] TOOL RESULT

```
=== KNT radiy ===
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
1648:radiy; fra-haravam.
2345:The adverbs from this stem are атайй, avadā, ava-pard, avahya-radiy, pasdva (from *pasd ava).
2573:fer from the sigmatic aorist, where the termina- tions would be pIE -?s-m -is-s -is-t, pAr. -isam -iš -1&; the identity of second and third personal forms gives an analogy to the 2d sg. imperfect in -1-$# (no examples extant in OP), whence impf. 3d sg. in 4$. After u the phenomena are the same.? The OP examples are àt$ ‘went’, 0170-07 ‘went past’, aku- naus ‘паде’ (Skt. ékynot), adarsnaus ‘dared’ (Skt. ddhrgnot); and the thematic optatives active vi- ndlayars, passive kariyars fradiyars (cf. for ending Gk. $€po,, Skt. bhdret).
2811:§264. Tug DEMONSTRATIVE ava- ‘that’ is simi- larly either pronoun or adjective; it commonly refers to something already mentioned, but some- times has a forward reference, as in naimd ava ката tya tunuvd skaubars radiy miła kariyars ‘that is not my desire, that the mighty should have wrong done to him by the weak’ (DNb 10f; also DB 3.58, 5.21, DNa 39, DNb 20, 53, 55, 57, DSa 4, DSe 34, XPh 49, 51f). It has also the meaning ‘yonder’ as applied to the sky: Auramazdà hya imam bümim ada hya атат asmdénam айй ‘Ahura- mazda, who created this earth, who created yonder sky’ (DNa 1-3, eto.).
2829:verb. yàlà, prep. w. loc. уйй à, prep. w. abl. radiy, postp. w. gen.
3963:8 Cispi$ ; CispaiS : pita : Haximanis: 4 9 0atiy : Darayavaus : xšāyaðiya : avahya ^ ^^ 10 radiy : vayam : Haxamanisiyà : баһуй 11 mahy : hacá : paruviyata : àmàtà 12 : amahy ; haca : paruviyata : hyà 13 xam : taumá : xšāyaðiyā : dha : 6a 14 бу : Darayavaus : xSdyafiya : ҮНІ : ma 15. nà : taumiya : tyaiy : paruva
```


## [2026-09-04T23:06:08.377Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT ratu ===\"; grep -n -E 'ratav|ratu-|ratu\\b' BRT.txt | head -20; echo \"=== PHD rad ===\"; grep -n -E '^rad|\\brad \\[|ratu' PHD.txt | head -20",
 "description": "Bartholomae ratu, MacKenzie rad"
}
```


### [2026-09-04T23:06:08.439Z] TOOL RESULT

```
=== BRT ratu ===
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2552:direkte Rede  oder  Zitat;  a)  adjektivisch:  kochersoll  man  niederschlagen,  den  Kessel usia  ahmni  (usw.,  Y.4J-I)  ■  ■  ciit  °taya  sollen  sie  .  .,  den  Aufbau  ,  ."  V,(V.73f.; paiti.vaca paityümraoti  Y,2/,4;  ■ —  kini  zl  — ■  "//  jrVr.ji./  y^aratu  °i^  vasträ  i-iiv än4  (usw.,  Y.4Ö.6)  .,  'te  zT  väcö  ..  mazdä  katu  V.J.  19;  —  asta-ja  hz  'te  mazäayasna frii mrao tY.yi.i^t-jy. 4.  i^üZ.;- — arrum'a  °t»m  iristam  nidanzaym  "da  sollen  (sie) „afrJnSmi  ..'tarn  mq^nm  fradaisayöH ..  die  J/l  (ihn)  den  Toten  .,"  V.  6'.46;_;.  18, Yti4-46;  benutzt  Y'l4-9.  b)  substan-  5.13,  14,  41,  61,  6.7,  51'.  7-i2i  t''-S,  10, tivisch,  in  Kongruenz  mit  dem  Praedikat:  9.39',  '4-7,  iö-z,  12,  A.3.^  falsVok.?); am?mca  .,  Sfrlnämi  ..  'taSca  tivlcö  yöi  —  'tanhqm  astqmca  var»sqm:a  .,\.h;-; ".  .  und  das  sind  die  Worte,  die  .  ."  Yl  —  'te  ratavö  .  .  'ta£sqm  ra>wam  'S.i'o 14-46'.  1)    vorausweisend    (öfters   -82;  Vd.  2;    —    'ts  ja'iä  V.A16-22S;
2556:fraea  'tat  vacb  vaoce yat  akumat yat  ratu-  zurückweisend,  s.  I  i  a  a);  a)  adjektivisch: mat  Y.jp.8;  Yt.  /p.47;  —  °tat  dät»m  yim  °ipm  aism>m  yÖ  7-aoU  . .  '-tay,i  urvaray,i vtdöyum  "das  GeseU  wider  die  Z»."  V.  yä  vao.'e  Yt  i4-%5',  V.  74.4;  —  *'te  vacö 5.22;  —  'tahe  nars  .  .  yat  paiti.iristahe  . .  yöt  hinti  . .  N.jj;  V.;o.i6,  17;  —  *ta V.J.  15;  JÄ29;  —  'taaha  äpö  yat  ar-  dämqn  ..  *yqm  dj'iat  ahurö  .,  Vr. /2. 4; maistayä  V.  6. 30;  33,  36,  39;  —  'lahmi  —    'tanham    diimanqtn  yöi    Amti  .  .    V,
2578:31;  3''.  35'*. "^-85;  —  tts  haca  nassvö  °vat  •  j.  aeJa-m.,  Plur.  'Kopfhaut';  '',a  ..*kay:i apat Aaca ni:iiiraj-fnV.6.$if?); — asH.masÖ  fi^nti  masyat»hd  'r,a  *ydi  *aparaya  paiti xraoidi'aAe  bis  'rate  lar^AaAe  "..h\s^3iXtto  *)tiastrfynaya..*kaya  kasya/i/t^  *yüi  *paou- mollisligni"  V.  jj.  30;  —  'val  apayaiia  H.  ruya  paiti  *mastrr/nya  "Kopfhaut.  — iog(X).  a)  mit  dem  Korrelat  _v(K'a«/- :  Welcher TeilderKopfhautistdergrössere? ^t/ (sd.)  °vat  htT^r»m  yaval  tacantn  F. '  Der  an  der  hiotera  Schädelwand.  Wel- 27a;  a;  ■ —  yavat-  hatca  hl  sastaiibya  eher  der  kleinere?  Der  an  der  vordem hangturvayqn  'vat  apat  haca  nizbärayfn  Schädelwand."  F.jc. \.ti.2t);  —  'imt  npö  yavat ,  .  J^.ioX;  — 'foiö  zaota  (iäm\.  ratu/rii)  yajat ß-ama- raiti  "mit  so  vielem  ist  der  Z.  r.,  als  .  -^  „  . n  (selber)  .ufsagt-  N.  2,1  2,,  23,  »>',  \  )■  if^  'a.«,y<,il„t  pa,U  afa  .  .  N. j'P.  Aa)  GS.  'vatö  als  .\dv.  'quantum  ^  j-  .  j^j^j^ sat  est,  in  hinreichendem  MassM?):  hura-  "  ^^.^  ^  ^  ^^^  ^^^^^ ysscti  (sd.)  a(.a  Tato  datdyat  A.j.4;  —  .   ^i%y^_^.^^,„„  -(.^5.  y^s  ka^i^yStarlum.
2873:girfsaite  akur.li ..  uiti  aojanö  Yt/0.53; — yö  aoxta  a/iiiräi  ..uity aojanö''  Yt.  Ä 10;  J0.73,_V.2.io,j.2o;  —  fravasayö  .  .^ uityaojana^'  \\,tj.(>(>;  —  uifyaojana (NPm.)'>  mi>rHi  Yt.ro.41;  —  ätar! . . uiti  vacibii  aojanö  Yt.  19. 49;  5.76;  — ; aus. .uiti  vaülns  aojana  Yt/7.17;  22;i —  bulyqsta  . ,  uiti  aej^mna  uiti  daomna FrW.  10.  42.  2)  'verkünden,  nennen, bezeichnen  ab  — ,  wovon  sprechen  als  — ', mit  dopp.  Akk.:  ratavö  .  .  y5i  (als  AP.) aoxta  ahurö ..zaraiustrrd  yasnylca  i<ahm- yica  "..  die  AA.  dem  Z.  als  verehrungs- und  preiswürdig  nannte"  Vr.  2. 3;  —  staei.l- nm  vatthanhm  aoxta  ahurö  . .  ya'^a  . . V.  ro.9;  —  yi  aastfm  *Ta^aiiA0  (sd.) aog?äJ  (3SPr.)  £am  asibyä  Avaniä  Y._j2. 10.  a)  statt  des  praed.  Akk.  steht  "der Nora.  3*;   yim    m^iyüka    ifil  (sd.)    n<ima
3232:S ;  aJiaoyo.xratav-
3234:•  j.  adaoyöjiratav-  Adj.  'des  Verstand untrüglich  ist':  maoyö  aki  •tus  . .  vispö.- vinvh  Vt.  i2.i'K
3286:•  j.  a-8äityo.]fratav-  Adj.  'der  nicht  den gehörigen  Verstand  besitzt,  nicht  recht  bei Verstand  ist'  (vom  Hund):  yat..  sp3  avacä (sd.)  V1I  bavat  "/wx"  V.  y,  29;  31;  — yat .  .  spii    a/iqm.baoii>mn5  vä   bavat  "tu/  V.
3295:'  reihend  'und':  yß  aH'ö  ha'je.gal^anqm  yS j  barfsmaca  "frastir^rüe  . .  a</°  anye  .  .  *7'a- '.  Ci'sca  framravainti , .  vTspe  ratu/ryö  "wenn einer  allein  . .  es  ist,  der . .,  und  die  an- dern . .,  so  sind  alle  r."  N.  Oo;  —  tavat paoirTm  An^rjm  /rasa  a'j°  ta:'sif  "ein erstes  J/.  weit  laufe  er  und  weiter  soll  er laufen"V.Ä  100;  io3,-'N.7/T.  a)  ver-
3368:—  yaisa  ni  d.ltl  . .  ''i^a  nä  >rJedüm  V. 5^-5>35-^'> — yit^ä  iä^aca  dahms  staota yesnya  haurva  daoaiti  '%a  ratu/rii  N. 3~;  —  yd^a  . .  nminopaitlm  paiti  tard.- pi'iw>m  dai'hyat  'ia  astryäH  "als  ob  er
3531:•  j.  ratu/ri/ apaityBliö  kaAya  N.55:  -?-.
3702:•  j.  n^it  "apita"'  nsit  *paiiikaya  (sd.)  ratu-
3738:•  j.  aipi.äütay-  f  'Verschieben,  Versetzen' von  Worten  (beim  Gebet) :  kä  . .  baya ahunake  vairyehe  anaJyBxoa{sd.)°ia{LS.y> srävayamna    dasa  faiH    artye    ratavS  Y.
3905:•  j.  "^aiwisrüSrima- ''  Adj.  (fem.  -mä-') 'den  Aiwisrü^rima  betreffend,  ihm  ge- bührend': kahmäi  ißaca)  *°>rimanqm'> ga>anqm  ratu/ris  frajasatti  N.5;.
4173:•  j.  anhu'S'wa-  n.  '.^Aflschaft,  Amt  des ^:iÄ(sd.)':  phnhahe  '%w?m^a  ratu'^w?m^a "du  (Zara^uära)  sollst  des  jlhB-  und /iatav-Amtts  walten"  Yt.  S.  i .
4380:•  j.  aii-a'haxta-'>  Adj.  'der  nicht  berech- tigt (geeigenschaflet  und  ermächtigt)  ist {etwas  zu  tun)':  yS  anyahe  ^apynnäyüka ^'lä'^  a'^aurufiTttt  paraahacäiti  "wenn einer  eines  andern  Kind  unberechtigt  3'  zu priesterlichem  Dienst  mit  sich  wegfiihrt" N.7;  6;  —  'tö.  .  ahaxts  (sd,)  N.tf;  — haxts . .  'ts  N.  6-,  — yasta  aSlalsam  mazda- yasnanqm  tnyazdavanam  aüanhqm  yat myazdanam  "ts  parabaraiH  nsit  täyul ,  . bavat  .  ,  ainyi}  kasat  .  .  "und  wer  von den  ,  .  M.  etwas  von  den  My.  wegnimmt, auch  ohne  berechtigt  zu  sein,  der  , . ;  aber irgend  ein  andrer  .  ."  N.  6^;  —  yezt^a *aile  ratavö  *'ta*^  *para.iyayanH  "und wenn  die  R.,  weil  (zu  ihrem  Amt)  nicht qualifizirt,  weggehen"  N.  ^o;  —  zaota  (sd.) *-ßS)  parayat  N,  So.
4650:äahtmm  gä'^anqm  sraohrät  pairistaytili  N.^'<>;  —  mmS  ahuräi  mazdai  mmö N.4^;45^*fH.2.i3; — yd  'nyehe  dahmahe  amisaiibys spintaHbyS mmS'nyagsqm  asao- bansma  *frast»r3nfe  ii.104;  lOi;  —  bsöalnqm  V.i^. 25:32;  —  »üi/  xsnSvayeiti  ahu- iia  hislahe  ..  'nyehe  dvan  (sd)  srayatül  r?m  mazdam  tUSit  °nye  (als  AP.)  amisO. V.j.zg;  N.6',7; —  hvSiits  vä  ySiitö  (i'3)  |  ¥1,70.139;'  '39;  —  hapta  hanti  *käva- yim  vä  'inim  *hais^aeTia  (sd.)  .  .  cayqn ,  iiayS  ratavS  .  .  aai  'nyahu  ralu/risü  N. N./;  — ]avada  'niyam  md^ifia/fi  . .  Bh.  102.  a)  mit  ciV'' :  saoiyanlqm  vfn'üra- 5.  4(?);  —  "nyqmca  suttm  ..  N.ff2(,?);  — jamm  Uta  "nyasHt  (als  APn.)  haxayS  Yt. ^rayS 'nya  (als  APm.)  maya  nihwirgsöU  /p.S9'*'.  NSm.  "/yJ,  ASm.'fiim,  ASn.
4652:26; — yeti^a  hl  °«va(NPn.)  aya  fyaoUna /raz'arsia  Y.J.21;  21;  —  MAj  ..  vas»ml\ (sd)    'nyacä  (APn.)   viduyS  Y.44.3;    — | paitica  (sd.)    hl  °nya  (NDm.)    dva atshtn  patüa  v3  V.5.27;  —  ha  mg  baya , .  sai»m  paiti  'nyaHqm  räi:Wqfn  . .  dasa paiti  °nye  ratavaY.ig.$;  —  ka  aPva  alö.- stüitis  ya  dasa  'nyaisqm  (als  GPf.)  asö.- stäitinqm  artjaiii  lLi,6; — alt a  ..*' inim  ^°> a^rapaitim    upBisdil   a%a    %ritTm  .  .    N. II.         a)  Siog.  und  Plur.  mit  folg.  eiy,  eii'> 'auch  ein  anderer':  *uta»iaiy  'niya/äy  (SSu.) vasiy  astiy  kartam  Bk^S;  —  \vasiy yasiiy  naibam (sd.)  hartem  X.i. 3;  —  h^nii 'fiyäscit  asasca  /m^ras/a  srTrh^a gibt  auch  noch  andre  schöne  .  .  Stätten und  Wohoplätze"  V. /,  28.         b)  mit  folg. ia-    und    /ii    'irgend    ein    anderer' iasat   aafiSus    asti-ats   N.  6^.  c)    mit
4787:yaica  aBe  vacö  apayatili"''  ySi  A)nti  *g3- %ahva  bisJmrüta  .  .  "und  wenn  er  die Worte  auslässt,  die  . ."  N.  jj;  —  yS  gä- %anqm  Sy>m  väüim  apayäiti  (3SK,)'i' alvqm  vä  vacasiastlm  N.  ^3;  —  yezi arastr»m  (sd.)  pairi-äoa  vä  "vacat  '^afa- yanta^^  (lies:  vala  v3  apayoHti"^  "oder wenn  er  Worte  auslässt"?)  aratu/rya  (ND.)
4814:mit  "p.parü,  y  parai''>  'weg-,  fortgehen, sich  entfernen';  a)  absol.:  natrya-san/ta . . para.ili'ii  (2SIA.)  upa.vazanuha  avi  ntnä- n>m  airyamaifii  (sii.)  V,  22.  7;  —  *para.- äip^^  upa.vazala  nairy3.sa»hs  avi  . .  V. 22. 13;  —  zaota  (sd.)  anakaxtö  par^at dqhiUäi  .  .  zao^r)m  raSxsaiti  N.  A'o;  — yezica  *alte  ratavö  *anahaxta  para.tya- yanti^^^  N,  Ai?;  —  uzayeni  psrayaii  V,  2-2. I.  a)  II  militärisch  'ausrücken,  ins  Feld ziehen':  avd^ä/aiy  a'iaAam  paraidiy (2SIA.)  avam  käram  jadty  Bh,_^.3;  2.7, 10; — ara^äsam  a>aA<im  piirait>l(iP'PTA.) avam  käram  . .  jatä  Bh._y.14_:  9,  2,6,14;
=== PHD rad ===
555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
3315:radiance brāzīšn; v. brilliance.
3316:radiant brāzišnīg.
4378:Zaratustra, у. Zoroaster.
4907:rad radunay radag саас
4908:radpassig
4943:rad
```


## [2026-09-04T23:06:19.347Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT lexicon r section ===\"; grep -n -E \"rādiy|rüdiy|radiy.*postp|because of\" KNT.txt | head; echo; grep -n \"ratu/rav\\|ratav-.*Richter\\|'Richter'\" BRT.txt | head -5; echo \"=== BRT arem ===\"; grep -n -E \"ar\\?m|arim.*passend|passend,\\s*entsprechend\" BRT.txt | head -5",
 "description": "Kent rādiy lexicon, Bartholomae ratav"
}
```


### [2026-09-04T23:06:19.453Z] TOOL RESULT

```
=== KNT lexicon r section ===
587:tarsatiy with Iran. tars- because of NPers. (0708, $ despite Av. drasaiti, from is-, both with IE Ж suffix -ske-; but Skt. trásati from "ireseti. 1 cartanaty: the c shows that a front vowel formerly 3 stood immediately after it; therefore car- from Ж *cer- from *ker-. 4 Karka, Gk. Каре, Kapuol; Elam. kur-ga-ap seems ' to have no evidential value. E | valrtaiyaty, if identical with Skt. variaye; see $ Lex. s.v. vart- for reff. ; | $32. Отр Persian ara seems to be established * in the following: E i By cognates in Skt. and Avestan: apataram, $ aparam, para, hamarana-, partaram, and the * verbal nouns -kara- and -bara- as second ele- ments of compounds. | $ By Elamite and other transcriptions: Arakadri $ (or Ark- ?), Arabäya, the final of Nabukudra- ° cara.
984:§70. Tue PIE Snort Рірвтномоѕ IN и, namely eu ои au, all became pAr. au, which remained in OP? but became Av. ao or du, and Skt. o; they remained essentially unchanged in Greek, and appeared in Latin as й 4 au respectively. These diphthongs are less frequent of occurrence than the é-diphthongs, and the distinction of them from one another is more difficult because of the lack of obvious evidence. But in OP, a diphthong is definitely proved by the use of an a-inherent consonant before u, if there is a cor- responding u-inherent consonant (k gid n m r); and as k and g would be palatalized before original e ($98), the au after Ё or g must be from plE ou or au. suffix -neu- m OP kunautiy ‘he makes’, Av.
2075:айа DB 1.28, XPh 49, 52, when used with pari-ay- ‘respect’, is probably inst. rather than abl., because of the lack of prep. Ласа; note that the text of DSe 37-9, as now restored, gives no support for the abl. in the other passages, despite my remarks JAOS 54.46, Lg. 13.308, JAOS 58.117. On inst. sg. karšā, loc. sg. karšayā, nt. асе. casam, acc. pl. ufrasta-diy, see Lex. s.vv.
2139:* Variation between -4- and -4- by Sievers’ Law (cf. Edgerton, Lg. 10.235-65); differentiation between pIE ё and pIE à cannot be made because of lack of adequate non-Aryan cognates. *pAr. d, ef. preceding note;
2228:rüdiy, -padiy in ni-padiy, vasiy (but cf. Lex. s.v.) “have the regular pIE endings of their cases: acc.
2231:Stem, because of the final short vowel ($86.11), but is саат, ace. nt. of an -a- stem. ? Bv. Gr. $290 takes as stem XSaydrSah- because of the gen. -aha, the second ele- ment being arSa- ‘just’ made into an (Ar.) -ds- stem; the objection to this is that -ds- stems are hardly made upon -4- Stems. Cf. also $162 note. * Lg. 15.175-6; for other in- terpretations of these two forms, see Lex. s.vv. * Lg. 15.170.
2612:$240. Tas Present Active PanTICIPLE hasthe suffix -ni-, before which the thematic vowel is -o-: nom. masc. pIE -én or -ont-s, fem. -опй or -ontza, nt. -ont; Gk. ¢ép-wv -woa -ov; Skt. bhdran, bháranti or bhárati, bhárat. Where (Aryan) thematic forms have -al- rather than -ant-, it is by extension from non-thematic forms, where- nf- became -nf- because of the preceding consonant; conversely, non-the- matic forms might have (Aryan) -ani- by imita- tion of thematic forms or because the suffix, when accented, took the pIE value -ent- or -ont-. The OP examples are nsm. tunuvd, from -ónt, probably with added -s in Iranian ($188.11), to present *funau-li; asm. lunwa^lam; gsm. tunwa*tahyd, with thematic declension: the nom. -s and the -ant- of the stem agree with the Avestan formations. There is also an uncertain restored asf. yaulda"- fim], regularly formed to pres. *yaudati.
2700:К. With prepositions, the mixed use with -ройу (see E); DB 3.32 pasa mand ‘behind me’; with anu- ‘according to’, in DNb 16, 18; with following rüdiy, to express agent, in DNb 9, 10f; with encli- tic -rddiy, in avahyarddiy ‘on account of this’.
2705:B. Expressing place to which, with prep. уйй ‘as far as’, in DSf 32 abara yata Bābiraw ‘carried as far as Babylon’, 34 у010 Сй {уа ‘as far as Susa’; perhaps also, because of the idea of motion which seems to be in the verbs, in gátavà avástáyam (DB 1.62f), güfavü niyaSadayam (РМа 36), maškđuvā avükanam (DB 1.86), uzmayà-patiy (DB 2.76, etc.).
2829:verb. yàlà, prep. w. loc. уйй à, prep. w. abl. radiy, postp. w. gen.

13123:*)  Die  einerseits  mit  FrädaLvira,  anderieits mit  Usaytirina  in  Beiiebung  gebracht  wird. Ableit.  —  Ableit.  aus  daMyav-;  s.  No.  1.  — Pü.  (ZU  V.  ig):  dehupal,  (zu  A):  dih,  erL: marlum  i  andar  j^eiiärTA  *mafi  iattdanfal; s.  dazu  DsT.  ZA.  /,  30,  31  "t.  —  ')  So,  mit Vrddhi/i,  hat  NA.  überall  ausser  G.;  s.  aber Ableit.  und  Var.  —  ")  JelM  fassen  die  Parsen das  Wort  als  'Richter';  s.  JUSTI  PrJ.  SS.  j6o No.   109  (wo  n  statt  IV  zu  lesen).
25030:KompA.,  E;  Ableit.  —  Vgl.  h-alav.  ~  Et.? Wohl  lu  *atla-,  iBild.  vgl.  xralav-.—  Gdn.s Versuch,  iwitchen  '?■■  'Zeit'  und  =r"  'Richter' eine  Brücke  zu  schlagen,  KZ.  jo.  325,  halte ich  für  verfehlt.  —  Pü.:  ral,  raßh,  erl.  (oft): datlmaar;  Sü.!  gu'i'fy,  gurutä,  gututvam\  s. noch  No.  2-7,  9,  13  f.  —  't  So  luletit  Gdk. KZ.  $0.  325;  aber  BB.  1$.  252  übersetit  er wieder  'Meister';  i.  ferner  Haug  Essays' 327 Cjadge'),  JN.  A  hymn  23,  DsT.  ZA. /.  7,  123. Vgl.  ^ähü-  mit  No.  1.  —  ')  Pü.:  ii  tö  sösfand\
25032:•  g.  3ratav-m.  'Judicium,  Richterspruch': aiibyS  (Sp.  5  m.)'*  HBs  singhaiti  ärmaitii "^wahyä  xrat^us  ylm  naiHi  däbayätl  {?,A.) "die  von  ihnen  gefällten  Richtersprüche wird  Arm.  verkünden,  die  deiner  Weis- heit . ."  Y.4s.^.
=== BRT arem ===
2801:Irrlehrer,  der  . ."  \.g,$i{.;  —  yavat  °fa *gaintii  upankacaili  (sd.)  V.  7.  56;  — yavat  'sa  ilß  bySrixfi  (sd.)  .  ,  frabavai \.i4.\y,  — yavat  -lö  spä  anya{sA.) )asö V./5.48,  a)mitrelativischemAnschIuss: "jS  zT  asti  baslazyö.t3mö  .  .yal  *mahnm.- sppni»m.baei'azyd  (sd.)  V.  7.44;  —  '/a  bi~ paitisiana  (sd.)  y3  kaine  V.  75. 19;  19;  — vXsp»m  ä  ahmst.,  yat  -ia  yö  apsntinyBkB uxjasnf  (sd.)  "bis  es,  das  Kind  . ,"  V.  75. 15;  —  'sa  yS  *ar?mBiidd'a.W3.  2)  auf ein  Relativum  als  dessen  Korrelat,  sub- stantivisch: ci'at  dra)ö  avaMUlüt  '^a  yö näirikaya  . .  !^ar>^3tn  frabamt  V.  /J.  4 1 ; —  °sö  .  .  aitayä  vihrkayh  (sd.)  Jq'^-wS.' tarö  *at3kat  . .  ya^a  spä  vtkrkake  k»r?- naoiti  V.  y .  4 1 ;  — "/?  ratufris  *yö  jayara N.if};  24,  60;  —  'sa  yetjhe  apirinSyükö ^•9i  7;  —  °^'''  zaoiranqm  tnaziltaca  . . yiJ  *naire  asaone  *daste  N.^4.  III)  In
4679:tsin  aiare^  utä  'niyä  bagäA^  lyaty  At^tiy Bh.  4-  ■  2  >  13;  —  "^'"i  vahistsm . .  'iiya^qm yat  anifsanqm  spmtanqtn  YL_j,3;  —  yetii zT  MS  maiysia  .  .  yazayanta  yak:a  'nye yazaiinhe  . .  yazinti  ". .  wie  dae  andern y.  verehrt  werden"  YtÄii;  —  ahe  nars asaofiB  ..  äai  'nyazsqm  asaonqm  Yti.30; i3-  ^Ti  —  airime  gstüm  kl  nUhka^a  .. *par^itar?m  kala  'uyalibyd  mazdayas- f>aiibysY.(}.^y, —  'nye  aaksus /rals.iar^ %ra  Aog.65(?)'';  —  \'.ulä  pärsJ' uls  msdt^ utä  "niyS  dahySve^  Bh. /.  13,  14;  11;  — psrsaiy . .  msdaiy  utä  'niy^uvä  dakyusuvä Bh.  J.  10;  —  ahmäi  nmsnäi  daaäiti  gBu^ca vq^iwa  . .  upa  'nya  (APn.)  sHndayäti  Yt /o,  2  8 ;  —  vätB  , ,  AubaoioitarS  . .  'nyalifyö vstaeihyö  H.2.7;  25,  V.j.ss,  ^,29,  Vyt. 45i  —  ""^  a%ra  frakavB  mä  apakavB  . . maia.cim  'nyqm  (GPn.)  daxstanqm  V,  2. 29;  —  ahtnavaila  (sd.)  gäkanqm  .  . uilavaitTm  hsitlmca  , .  av5  yS  °nya  (näml. gä'^h)  srSvaydii  N.  46.  a)  Plur.  mit folg.  äi  'auch  die  andern' :   tl  mqm  ava%a
4997:yS  nar?m  "tim  *avai>urvalsayeiti  (sd.)  V. 4.22,  26.
5458:•  j.  arsSa-,  p.  arda-  i)  Adj.  'halb' (nur  Komp.).  2)  m.  'Seite':  *atitar?m (sd.)  'tijm  mayaAe  V.p.29;  —  antar?m 'fam  nmanaheV.6.i,y,  — dasinim  (vair- yastärtm)  hl  upa  "htm  Yt.  10. 100';  — visps  he  upa  'wun  (lies  -o!)  \tio.ioo; —  äasimm  hl  'Öe..  Aävöya  hl  "%€  "rechts (links)  ihm  zur  Seite", Yt. /o.  ia6;  —  ww- %asö  (sd.)  gairis  parmtarim  °c,5  (AD.) manuiahe  YL/p.i.  [V.  5.19,  5.33,  Yl j".6o:  lies  antar».am>m^
5522:•  j,  ar?ma-,
```


## [2026-09-04T23:06:20.799Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD ar-1 ==\"; grep -n -A40 -E \"^ *ar-1|ar-1\\.? To fit together|ar- *To fit\" AHD_watkins1985.txt | head -80",
 "description": "AHD Watkins root ar-"
}
```


### [2026-09-04T23:06:20.886Z] TOOL RESULT

```
== AHD ar-1 ==
```


## [2026-09-04T23:06:27.909Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25020,25035p' BRT.txt",
 "description": "BRT ratav entry"
}
```


### [2026-09-04T23:06:27.965Z] TOOL RESULT

```
1502
12*,  23,  Vr.2.2f.  (oft),  14.0,  3,  16.0,  iS. o,  20.0,  21.0,  23.0,  Ny.4.  9,  G. /,  6,  7, 2.8,  ^.sff.,  4.6ff„  5.sff.,  Yt.7.3,  FrW. 2.  2 ;  —  gai'itanam  ätihairyehe  aiaono aiafu  '%w5  Vr./.j;  2*,  48".  (oft),  Y.;.  17, :;2. 3, 4,  "Ji.y,  —  AävanJe  aSäum  asahe 'tvB  (VS.)  Y.  i.  20;  20',  *Extr.  4'\  —  vTspe alalu  'tavS  Y.2. 18;  /.  10.  17,  22  (Vok.), 2.3,  8,  9,    10,  71.4,  Vr.2.6,  A.^.  I,   S.
2.  6,  Vyt  18;  —  vtspaiily3  atake  °lubyö Y.i.19;  3,  8,  g=,  Vr.7.2,  4,  S./.6;  — vispanamca  spmtahe  mainySus  damanqm .  .  asahe    ''^wqm    V.  /.  lö;  yi.  3,    Vr.  /.  1,
3,  5,  6.  II)  imjAw.  Bezeichnung  der beim  Gottesdienst  neben  dem  Zaotar (Oberpriester)  und  unter  dessen  Leitung beschäftigten  sieben  Unterpriester  (Hel- fer)*': yasca  aetaeiam  °%wqm  paotryS ajass^  h3vanäii3irt  (sd,)  aWm  aslayäti (näml.  Züolä)  li.S2;  —  aoä^  anyaisqm ''hwqm  paitLäiaySit  (näml.  zaota;  Sp.  55 m.)  N.  i¥y; — yedca  alte  'tavS  *anahaxta fsd.)  *para.iyaya?iii  zaota  vlspe.ratu^wais (sd.)  ^ ras'i:-wayeiti  N.  iö.
Undeutlich:  'tui astZ'aiiyS  gasUayä  Yt. 5.89;  —  nairyS  °tus  kara  N.  5;  i^j,  pj;
—  anahunaca  °tusca  stitätas^a  Vr.  10.  z ;  — ratukwtm  aliqtn  'tus  Vyt  42;  —  'tüs Vyt.  /tf;  —  havSi  '%we  N.  lo^;  —  dataia ..  a!t3m    °lümia    myazd3m{%A.)ca    A.^.  3;
—  "^wal^a  myasdaiM  '^waSca  ratufrita- yalia  Vt.4.2;  ti.Sl';  —  x^aA/zii  'tav5 'Vr.14.3;  —  aSaisqm  'tavö  azdai  N.  5j; 102.         \S..iQ.  17;    lies    ratus.m?rrta\    —
—  Y. 5/.  s :  lies  tnlratüm ;  —  Y.44.16: lies  akam.bis.ratüm\  —  V.gS:  lies  ra/u- /ris.]         vlspe   ratavS  s.  auch   bes.    (Sp.
1467  0.).
*)  Ihre  Namen  sind  Vr.  3.  \,  V.  5.  57  usw. und  mit  Angabe  ihrer  Tätigkeil  N.  72  ff.  »uf- geiählt.  In  nRchchristlicher  Zeil  tritt  an  die Stelle  der  sieben  Helfer  ein  einziger,  der  Ra%ioik. Aber  insbesondere  N.  /J  ff.  und  82  bestätigen noch  mit  voller  Deutlichkeit  die  alle  Sieben- lahl.  Vgl.  daiu  Tiele  GescbRelAlt.  2.  313, S.  femer  lu  upa-sraotar-.
KompA.,  E;  Ableit.  —  Vgl.  h-alav.  ~  Et.? Wohl  lu  *atla-,  iBild.  vgl.  xralav-.—  Gdn.s Versuch,  iwitchen  '?■■  'Zeit'  und  =r"  'Richter' eine  Brücke  zu  schlagen,  KZ.  jo.  325,  halte ich  für  verfehlt.  —  Pü.:  ral,  raßh,  erl.  (oft): datlmaar;  Sü.!  gu'i'fy,  gurutä,  gututvam\  s. noch  No.  2-7,  9,  13  f.  —  't  So  luletit  Gdk. KZ.  $0.  325;  aber  BB.  1$.  252  übersetit  er wieder  'Meister';  i.  ferner  Haug  Essays' 327 Cjadge'),  JN.  A  hymn  23,  DsT.  ZA. /.  7,  123. Vgl.  ^ähü-  mit  No.  1.  —  ')  Pü.:  ii  tö  sösfand\
rat,  erl,:  tut  m  djiasiän  eigön  und  kul  ral  , gespandän  ke.  —  J)  Pü.;  ratlh  (erl.;  awdiK)  , öhrmaid.  —  4)  Vgl.  zu  st3tä.ratav:  —  !)  Pü. ral,  erl.:  tardär  i  muri  kisän.  —  6)  PüErL dailawar  *ie  an  gu/t  iartan  Säyet.  —  7)  Pü. : raiihj,  erl.:  frärömhi;  a.  zu  ri^wyor.  — ^)  Uzw,  zu  A.  im  Gegensatz  zu  den  beim GäiäHiärfest  beteiligten  Laien  (raiimaya-),  zu N.  -  als  Zelebrant  -  im  Gegensatz  zu  dem  - als  Ministranten  -  verwendeten  Knaben.  — 9)  Pü.  (ta  Vr.  /.  i)  gibt  an,  wer  die  Ä.  der sieben  Klassen  sind;  nimlicb:  Birmazd-sara- luSl  -  iar  I  mäAii  -  iäiumai  -  iarsift  -  fehlt (Bd.  14.  9:  xargSl  i  Sär)  -  xariiiz.  —  »)  An den  Parallelstellen  S.  2.  6,  7  steht  amihm spitiUm  statt  wie  lu  erwarten™//;™. —  i')  Es ist  nicht  deutlich,  wer  damit  gemeint  isL  — ■»  S.  zu  den  33  R.  DsT.  ZA.  /.  13.  — I])  Pü.:  katär  ratikän  SSmurilnTk.  —  M)  Pü.: ahräklh  ral,  %\s..:  puayaguruh.
•  g.  3ratav-m.  'Judicium,  Richterspruch': aiibyS  (Sp.  5  m.)'*  HBs  singhaiti  ärmaitii "^wahyä  xrat^us  ylm  naiHi  däbayätl  {?,A.) "die  von  ihnen  gefällten  Richtersprüche wird  Arm.  verkünden,  die  deiner  Weis- heit . ."  Y.4s.^.
Vgl.  'ratav;  von  dem  es  durch  den  Wort- akzent geschieden  gewesen  sein  wird.  —  Pü.: pj,i»  6t  ral  ämScet  fa  havandak  menUnlh  - söSyins.  —  ')  Ablativ  (oder  Dativ)  in  praeg- nantem  Sinn;  s.  zu  däahä-.  —  *'»  Gntd.s Über- setzung, KZ.  30.  318,  verstehe  ich  nicht, j.  rali's  P.  32:  lies  rälii.
•  j.  ratu-xsa^ra-  Adj.  (fem.  'ra-')  i)  'die Henschaft  des  Ratav  innehabend,  als  R. herrschend' :  ahuräi  mazdai  . .  yaj  Auxfa- ^rtJi  . .  yat  'rät  Vr.  11. 1;  —  gä'hs  sp>nta •rä  \.54.  2;  —  ffä^äby^  spuitabyB  'rabyd Y.jv  i,7i.  II,  V.  79.38,  A.2.I.  1)  'die Herrschaft  des  Ratav  über  sich  habend, dem  R.  untenan';  näirikqmca  ..  hus.hqm.- sästqm  °rqm  Vr,_J.  4;  —  nätrikaySt  .. hus.hqmjästayili  'rayäi  H.  2.  18,
KompE.  —  Pü.i  ral  x'atil;  erl.  (zu  V.  /p): ral  j'j/iiZi  e  ia  afärikr'i  pa  tn  söyit  yastan, (lU  H.):  /flä  pa  lardär  dSrrl.
```


## [2026-09-04T23:06:28.621Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"to fit together\" AHD_watkins1985.txt | head; echo \"---\"; grep -n -i \"arithmetic\" AHD_watkins1985.txt | head",
 "description": "AHD search fit together"
}
```


### [2026-09-04T23:06:28.706Z] TOOL RESULT

```
287:ar-. Also are-. To fit together. I. Basic form *are-. 1. Suf- fixed form *ar(g)-mo- in: a. Germanic armaz in Old English earm, arm: ARM}; b. Latin arma, tools, arms: ARM?2, ARMADA, ARMADILLO, ARMATURE, ARMOIRE, ARMY; ALARM, DISARM; C. Latin armus, upper arm: ARMILLARY SPHERE. 2. Suffixed form *ar(e)-smo- in Greek harmos, joint, shoulder: HARMONY. 3. Suffixed form *ar()-ti- in: a. Latin ars (stem art-), art, skill, craft: ART!, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA); b. fur- ther suffixed form ‘*ar()-ti-o- in Greek artios, fitting, even: ARTIODACTYL. 4, Suffixed form *ar()-tu- in Latin artus, joint: ARTICLE. 5. Suffixed form *ar()-to- in Latin artus, tight: COARCTATE. 6. Suffixed form “*ar(e)-dhro- in Greek arthron, joint: ARTHRO-; ANARTHROUS, DIAR- THROSIS, ENARTHROSIS, SYNARTHROSIS. 7. Suffixed (su- perlative) form *ar(g)-isto- in Greek aristos, best: ARISTOCRACY. II. Possibly suffixed variant form (or separate root) *dr-dh-. 1. Latin drdé, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINA- TION, INORDINATE, SUBORDINATE. 2. Latin drdiri, to begin to weave: EXORDIUM, PRIMORDIAL. 3. Latin or- ndre, to adorn: ORNAMENT, ORNATE; ADORN, SUBORN. III. Variant or separate root *ré- (< *reo-). 1. Latin réri (past participle ratus), to consider, confirm, ratify: RATE!, RATIO, REASON; (ARRAIGN). 2. Suffixed form ré-dh- in: a. Germanic *rédan in (i) Old English rédan, to advise: READ, REDE (ii) Old English réden, condition: HATRED, KINDRED; b. Germanic *rédaz in (i) Old High German rat (> German Rat), counsel: BUNDESRAT, RATHSKELLER (ii) Old English rédels(e), opinion, riddle: RIDDLE?. 3. Zero-grade form *ra- in Germanic *radam, number (see dekm). IV. Variant (or separate root) *ri-. 1. Suffixed form *ri-tu- in Latin ritus, rite, custom, usage: RITE. 2. Suffixed form *(a)ri-dhmo- in Greek arithmos, number, amount: ARITHMETIC, LOGARITHM. [Pok. 1. ar- 55.]
373:dhabh-. To fit together. 1. Germanic *dab-, to be fitting, in participial adjective *gadaftaz, fitting, becoming (*ga-, collective prefix; see kom), in Old English gedzfte,
---
287:ar-. Also are-. To fit together. I. Basic form *are-. 1. Suf- fixed form *ar(g)-mo- in: a. Germanic armaz in Old English earm, arm: ARM}; b. Latin arma, tools, arms: ARM?2, ARMADA, ARMADILLO, ARMATURE, ARMOIRE, ARMY; ALARM, DISARM; C. Latin armus, upper arm: ARMILLARY SPHERE. 2. Suffixed form *ar(e)-smo- in Greek harmos, joint, shoulder: HARMONY. 3. Suffixed form *ar()-ti- in: a. Latin ars (stem art-), art, skill, craft: ART!, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA); b. fur- ther suffixed form ‘*ar()-ti-o- in Greek artios, fitting, even: ARTIODACTYL. 4, Suffixed form *ar()-tu- in Latin artus, joint: ARTICLE. 5. Suffixed form *ar()-to- in Latin artus, tight: COARCTATE. 6. Suffixed form “*ar(e)-dhro- in Greek arthron, joint: ARTHRO-; ANARTHROUS, DIAR- THROSIS, ENARTHROSIS, SYNARTHROSIS. 7. Suffixed (su- perlative) form *ar(g)-isto- in Greek aristos, best: ARISTOCRACY. II. Possibly suffixed variant form (or separate root) *dr-dh-. 1. Latin drdé, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINA- TION, INORDINATE, SUBORDINATE. 2. Latin drdiri, to begin to weave: EXORDIUM, PRIMORDIAL. 3. Latin or- ndre, to adorn: ORNAMENT, ORNATE; ADORN, SUBORN. III. Variant or separate root *ré- (< *reo-). 1. Latin réri (past participle ratus), to consider, confirm, ratify: RATE!, RATIO, REASON; (ARRAIGN). 2. Suffixed form ré-dh- in: a. Germanic *rédan in (i) Old English rédan, to advise: READ, REDE (ii) Old English réden, condition: HATRED, KINDRED; b. Germanic *rédaz in (i) Old High German rat (> German Rat), counsel: BUNDESRAT, RATHSKELLER (ii) Old English rédels(e), opinion, riddle: RIDDLE?. 3. Zero-grade form *ra- in Germanic *radam, number (see dekm). IV. Variant (or separate root) *ri-. 1. Suffixed form *ri-tu- in Latin ritus, rite, custom, usage: RITE. 2. Suffixed form *(a)ri-dhmo- in Greek arithmos, number, amount: ARITHMETIC, LOGARITHM. [Pok. 1. ar- 55.]
1258:ARCHON arkhein -ARCHY arkhein ARCIFORM = arku- ARCTIC rtko- ARCTURUS rtko-, wer-4 ARCUATE = arku- ARDENT as- ARDOR as- ARDUOUS erad- ARE! er-1 ARGAL? reg-! ARGENT arg- ARGENTINE arg- ARGIL arg- ARGININE arg- ARGON werg- ARGONAUT nau-2 ARGUE arg- ARHAT alg’h- ARIA wer-2 ARID as- ARIES er-3 ARISE risan ARISTOCRACY ar- ARITHMETIC ar-
```


## [2026-09-04T23:06:47.453Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT v1 ارابه ==\"; grep -n \"ارابه\\|ارّابه\\|عرابه\" BQT_v1_pages.txt | head -10; echo \"== BQT v1 عراده ==\"; grep -n \"عراده\\|عرّاده\" BQT_v1_pages.txt | head -5; echo \"== SNS rad ==\"; grep -n -E \"\\brad\\b|ratu\" SNS.txt | head -10",
 "description": "BQT arrabe, SNS rad"
}
```


### [2026-09-04T23:06:47.594Z] TOOL RESULT

```
== BQT v1 ارابه ==
10314:ارابه - بر وزن فرابه ۰ گردون را
20985:و گردون (۱) و ارابه راندن با هم بدارند. ۱۷-
== BQT v1 عراده ==
== SNS rad ==
3963:GUW»,535) xrat^S^j/ kratav-: ^j^ xratu- ife 
8968:iAiWb. 897)p3sav/paratu : L. 
9282:'pratuafca- pratyafic- . ** ^ * p . tytta - : ^ ,, , 
10183:^ ^artuitratumc-^W'" 
12925:;r. dyl:^<* U^*>- 1692) hrd: ****** z^rad- :b- i 
29239:ratu- 226/3 
29394:pasav/paratu 137/7 
29412:pratuaka-pratySnc- 142/6 
29512:z^rad- 225/7 
29703:xratu- 40/17
```


## [2026-09-04T23:06:48.759Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FSF rad ==\"; grep -n \"رد\\b\" FSF_pages.txt | head -20; echo \"== NYB rad/ray ==\"; grep -n -E \"\\brāy\\b|\\brad\\b|ratu\" NYB_vol2_glossary.txt | head -15",
 "description": "FSF rad, Nyberg ray"
}
```


### [2026-09-04T23:06:48.859Z] TOOL RESULT

```
== FSF rad ==
28:‫واژه‌نامه‌ها‪ 12 .‬فارسی س‬     ‫ق‪ .‬شاهنامه‬    ‫ابوالقاسم‪۹۵-۶۱۴۲ .‬‬    ‫‪ .‬فردوسی‪.‬‬
69:‫جامعی در دست نیست آنچه توانسته‌ايم بهطورناقص گردآوری کنیم از اینقراراست‪:‬‬
77:                           ‫فرانسه بهتحصیل هنر نمایش پرداخت‪ .‬در سال ‪۱۳۱‬‬
88:  ‫«میرزاکمال‌الدین» نوشتة محمدعلی فروغی را در سالن سیرک به روی صحنه آورد‪.‬‬
95:‫ودیب خوانساری شکل گرفته بود‪ .‬که بهامردکورسازی در‬
99:‫«کلوپ حزب» به تشکیل کلاس حصوصی نمایش پرداخت‪ .‬مجدداً در سال‌های‬
101:         ‫نو‬‫میچکرد‬
122: ‫در زندان کتابیبه نامهنرتتاترتألیف کرد کهدر سال ‪ ۰۳۳۱‬منتشر شد این کتاب در سال‬
124: ‫پنهانی بهادار؛ تثاتر سعدی پرداخت تااینکه پلیس تهران تئاتر سعدی رابهآتش کشید‪.‬‬
125:  ‫نوشین در سال ‪ ۱۳۳۱‬باناممستعار فردوسی در تثاتر دولتی آکادمی تاجیکستان‬
126: ‫مشغول بهکارشدو نیزدر تصحیح و نشر شاهنامة فردوسی چاپ فرهنگستان علوم‬
133: ‫مجلهٌ مردمنیزبهجامانده است‪ .‬سرانجام اینمحقق گرانمایه و بی‌ادعا در اردیبهشت‬
139: ‫فردوسی مارا بر انداشت که در این چاپ باتوجهبهاینکه مدت‌های مدیدی است که از‬
166:‫از نمونه‌های فراوانی که در پیش آورده شد شیوه کاراینجانب آشکار است‬
168: ‫‪-۱‬نام‌های خحاص را نیاورده‌ام‪ .‬چون برای هر خواننده شاهنامه به خوبی روشن‬
170:‫هستند» و برای کسی که باشاهنامه سرو کاری ندارد از دانستن ایننام‌ها چه سود؟‬
173:‫باد سرد‪-‬نیکی دهش ‪-‬نیکی گمان ‪-‬از در ‪-‬خیره پرتاب _گذشته ز من‪-‬ز توبگذرد‬
180:‫شن شنت ان سر ‪-‬گرد برآوردن‬         ‫نیده‬
186:‫دیدن ‪-‬سر سوی کسی نهادن ‪-‬روز فریاد ‪-‬رخت بستن‪ ...‬آورده شده است‪.‬‬        ‫روی‬
188:‫‪- ۵‬در آوردن شاهد بهیک بیت قناعت نکرده‌ام» بلکه هرجا لازم بوده است‬
== NYB rad/ray ==
321:ahü [’hw] paramount chief, overlord, borrowed from Av. (281 sq.) ahü-, in the combination ahü-ca ratus-ca overlord and chief judge, transposed into Phl ahu u rat (g. v.), whence the abstr. noun
593:api-spartan ['psp'ltn'], often with bé: to hand over (6 to) 147. 3213; to consign to, to lay down in (6) 111°; to give up (one’s honour) 4?!; to give (one’s life, rad for) 1119; to commit (oneself to death)
1137:ham ~ rād 51. 671, han ~ rād 34?, pat han ~ rdd 104?! for this, or that, reason; hac han ~ rad... tāt with the intention that 118?!; — condition, matter 1184-17-20, 1217-11; pat ~ i kārēcār homānāk 119 ; — the subject 625; — vas ~ many things 3716, — < Olr. *cahmät ‘wherefore?’, Skr kasmát; MPrs cym ‘reason, cause,
1223:mw: v. these ws.; — gö& ~, (apar) nikäh ~: v. these ws. — apdc ~ to keep back (hac from), to avert, to repulse 495-9. 702°, 739-10, 8719-20, 9619. 10272; to abjure 19! (cf s. v. rad); — apar ~ to lift up from (hac damik) 3318-19; — bé ~ to take away, to tear off (hac from) 1029; — 6 ham ~ to hold together, *to radiate an unbroken ray (hac õi be starting from him) 5125-27, 525; — peš ~ to sacrifice, to make a sacrifice of 1174; — as a sort of auxiliary vb. denoting the duration of the act: -m pat drinišn däret u drinet he keeps tear- ing me up 1027-5; dašt guft kept saying 1019-20, — Av. (690 sq.) ®dar-; MPrth dyrdn d r-; MPrs d'šin d?r-; Paz. NP dästan dar-.
1421:rad (v. below). 1. HN’: ~ nāmaky this inscription (here above) P 2:3; ~ vizand hac yātūkēh i ~ kanik 373: ~-ic évak hac avdéh the following is one of the miracles 4474; kē hac ~ aštak, veh he
1451:age DkM 6989; tat pat dātistān(ūman>- deh či veh tuvän zatan u éraxtan cigón ka-š pat davreh u drusteh apäk gēbāh through righteousness thou art better able to defeat him and make him lose the case than if thou speakest to him coarsely and roughly (cf s. v. davr) PR 573; — pres. pass. 3d p. sg. éraxtét he is pronounc- ed guilty, opp. buxtet he is acquitted, v. Bthl, ZsR IV, 8; Paz. buxted ... érexted SGV III, 26; kē rāstēh rad pat xudstak eraxtet, ah veh cigon kē družeh rād pat ruvān éraxtét he who suffers loss of prop- erty because of his righteousness is better than the one who suffers the loss of his soul (forfeits his soul) because of his falsity PR 26$-9.] — Two vbs. seem to have coalesced here: 1) črtatan ērēc-, cf Paz. érexted and the caus. érezinidan ‘to condemn’ SGV XI, 257, most probably < abi- + Av. (1479 sq.) raék- ‘to leave in the lurch, to abandon to destruction’ (Bthl IF XII, 112sqq.); 2. éraxtan érang-, most probably a denom. of érang, črangčh 'trouble, delusion' (Paz. ŠGV X, 58 ete.) < *abi-ranga-, cf. an-črang, ranj, ranjak; MPrs ‘yrat, “yrnz- ‘to combat’, Verbum 199. (Bthl, l.c. adopted the reading érazt).
1788:ham fhm; HWH-m 20°. 2525, 287] 1. the same, e.g. passax" han ~ guft he gave the same answer (as before) 549.19; (an- dar) ~ zaman at the same time, at this very moment 12?9. 16%; ~ cim rad for this very reason 67! 8015 (hamcim); (the one) just mentioned 1119-17; often only emphasizing a following dem. pron.: ~ či rād for this (child) just mentioned 44%; ~ pat et dāram I do think 2525, 282-3; 6 han
2029:Hróm [hlwm] Rome, in the Phl literature designating the Byzantine empire: 17*. 1090, — Cf Schaeder, IB II, 24 sqq. hrömäyik [hiwm’yk, hlwm'dyk] Romaic, Byzantine 1?. 1075-12. 1145; pl. cas. obl.
2334:c) či rad ... ~ because 5177-52 passim; nē hast ki... tarsitan there is no reason why .. . should fear 61%; pat et kū ...
2731:nikéritan [nkdlytn'] to look, to watch, to notice; to consider, to reflect: nikér ku nē... take care not to... 45; api-š bé-c nikerit kū ... and she reflected, think- ing (+ dir. speech) 38; apfr rāyēnītan i Zartuxst nikérit he pondered as to how to do away with Z. 501%; — apāc ~ to look up 233-318; — tō an... apar nikéram pat apazonikeh u bavandak-menišneh kū-t pat han xānak nikéram i-t hast as for thee, with (my) heavenly powers and perfect thinking I see through thee, namely, I see thee in that house which is thine [1. e. Hell] 5324-26, cf s. v. aržan- tkénitan. — Paz. nigerīdan, nigaridan ; NP ntgarīdan, -istan. The spelling nkdl is attested by FrP 10. As the spelling -dl- regularly denotes -ér- we have to establish
3195:rad 164
3270:rat [lt'] "genius", divinity or tutelary spirit presiding over one of the categories or classes into which all beings and things of the good creation are divided: ap?-Sün ~ Gēpet and their genius is G. 8674-25; Zartuxšt is ašūkān ~ the genius of (all) the Righteous 106!; he is in Avestan terminology the ahü and ratu of the world, hence the abstr. ahü-u-ratü-eh 4 gēhān 55%. — Av. (1498 sqq.) ?ratu-; NP rad ‘intelligent, learnd', ‘a high priest of the Magi'. As to the doctrine, v. Modi, Ceremonies 330—334.
3295:Rax"at [Ihwt'] a town 11572. — According to Cat. 84 < Av. (1788) Haraxuati-, OP Haratuvati-; Ruxxaj Yàqüt 2, 770?
3296:rāyēnāk  [Pdyn?'k] manager, furtherer 7722, - MPrs r’yn’g (A-H. II); Paz. raina.
3297:rāyēnišn [l?dynšn'] the act of arranging, of managing, or of caring for: xrat har-2- axvānīk ~ Wisdom means caring for both forms of existence (the spiritual and the material) 66!?; kē vinds pat ~ ddrét he who considers Sin worth his care 83°; kar u ~ (hendiadys) mission, task, function 872; — directions 132%,
```


## [2026-09-04T23:06:59.721Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== NYB rad entry ==\"; grep -n -E \"^rād |rād \\[|rād\\b.*postp|rād \\(\" NYB_vol2_glossary.txt | head -10; echo; sed -n '3190,3200p' NYB_vol2_glossary.txt",
 "description": "Nyberg rād entry"
}
```


### [2026-09-04T23:06:59.826Z] TOOL RESULT

```
== NYB rad entry ==
1720:guftan [gwptn'] gēb- [YMLLWN-,YMR- RWN-; 3d p. sg. gwbyt 128%, gwbyt' 9923, 1021, gwpyt' 2315 göbet], opt. 2nd p. sg. gobeš [YMRRWN-yš] 6012, pt. always gwpt' = guft: to say, to tell, to utter, to pronounce, to recite, passim; with 6 ‘to’, apar, rād (53) ‘concerning, of’ (patiš 6614); followed by direct speech introduced by ku, passim; with a
3008:homänäk, pat mānākēh similar(ly); pat nazdikéh i 7418 (pat han + fraškart nazdikéh 106%); apar pat han jaman ka 4123, adak apar pat jamān 61°; pat yuvat hac; — frame prep.: pat... rād (g. v.). — ll. in composition with a subst., forming adjectives with the sense of ‘provided, connected with’: yam i pat-göhr set with jewels 6°; (murvdn i) pat-àp aquatic 93°; zan i pat-göhr a woman of good birth 69%; cigon andar hindükän pat-vicin but high of station 11819-11; — enlarged with the adj. ending -ömand: ka krisäsp pat-tanómand u (pat-)janomand ne bit hah if K. had not been endowed with body (pat-tan) and life (pat-jān) 342. — B. adv. (rare): in addition, moreover 96%; u pat-ic and furthermore 904. The proper adv. be- longing to pat is patiš (g. v.). - OIr *patt (Skr prati), Av. (822 sqq.) pasti, OP patiy; MPrthPrs pd, pt; Paz. pa. In all prob- ability this pa was since old in common use alongside of pač as its sandhi form (cf passaxt, passand etc.), and on it the spelling of the prep. was based by analogy with the Semitic prepositions b-, k-, l-. As however, contrary to the Sem. ws., it maintained its character of an independ- ent w., and independent ona-consonantic
3030:rād hac Ohurmazd patigrift these have.
3199:the virtual dir. obj. which grammatically ought to be the formal subj. of a pret. pass. (mixed act.-pass. construction): Sähpuhr varzēkar ~ frac xuand 15” sq.; api-§ han zan ~ ne ēzat 10°? ; cand dastava- ran... u dānākān i Bran šahr ~ bē kust 10718-14. — OP rād- ‘reason, cause’ in radiy postpos. 'on account of', avahya- rüdiy ‘for this reason’; MPrth r’d, MPrs ry; Paz. NP rd.
3275:rād ‘liberal, munificent’; < *rātā, nom.

puštčpinakčh protection, defence 8514. — Paz. puštaspānī, v. above.
pūt [*pwt'] putrid matter 76%, — MS pwn, but Paz. pid, Skr. v. durgandhi; Av. (909) pūti- *putrescence'.
pūtakēh [pwtkyh] decomposition, decay 112°.
Piitik [pwtyk] the name of a lake, “the Purifying,, 861%. — From pü-, v. pak. Av. (909) pūttika- ‘purifying’, zrayo puitikom ‘the purifying lake’.
www .parsianjoman.org | oe zl wk
rad 164
raftan
iršd (rà?) [Pd] comprehension, intelli- gence, intellect, is to be restored, with the MS, 4813, instead of +L’: kē (for ki) ~ <i> Pourušāsp hac višopišn i haciš apécür bavet (better but) for P.’s intelli- gence fails (failed) to grasp the destruc- tion emanating from him. (gl.). - MPrth red ‘reason’; MPrs ry ‘insight, intelli- gence’ (A-H II; 8, 97d 18, not recognized by S who was, however, very near to hitting upon it); NP rà? ‘knowledge, wis- dom, belief', which is not borrowed from Arab ra’y- (on the contrary, the mean- ing of this w. is influenced by the Iran- ian one); etymologically identical with the following w.; ef nikeräi.
2räd [l’d; inser. and Ps. Pdy] postpos. l. for the sake of, because of, for, on behalf of, in favour of (7220-21), con- cerning (37?. 2919 etc. passim); ham cim ~ for that very reason 512-13, 671-2; han cim ~ 342, & ~ 795. 9626, 982° for that reason; ēt ~ cé because (conj.) 773-5; ce ~ why? 3511. 795; õi ke ~ for whom 183; — preceded by an inf. or a v. n.: in order to, for the purpose of, because: ditan i Zartuxšt ~ (in order) to see Z. 4777, 5218-19; ves avis matārēh i xrat ~ because more wisdom had been allotted to him 9041-12; — forms together with hac or pat a frame preposition: hac bim i Artaxšēr ~ for fear of A. 1525; 3719. 4612-19; hac hin cim ~ 118%; kirpak i pat dat ~ kart for the sake of Law 6419; pat omet +... ~ in hope of 1211917; pat hän cim ~ cé because (conj.) 10421-22, — 2. used as in NP: a) ‘to, for’: cahārpādān ~ ap hamë dat 1419; Papak ~ héc fradand ne būt P. had no child 19; 32-4, 422;  ménam to ~ nevakeh 4771, v.s. v. méni- tan; 427; frazand i zu&s m kar u kirpak bē- dimoxtan 652-23; — b) denoting the dir. obj. of the pres. tense: hakar né han ~ <apdc> dārēt if you do not abjure that (religion) 191; 2520-21; 453; — c) denoting
the virtual dir. obj. which grammatically ought to be the formal subj. of a pret. pass. (mixed act.-pass. construction): Sähpuhr varzēkar ~ frac xuand 15” sq.; api-§ han zan ~ ne ēzat 10°? ; cand dastava- ran... u dānākān i Bran šahr ~ bē kust 10718-14. — OP rād- ‘reason, cause’ in radiy postpos. 'on account of', avahya- rüdiy ‘for this reason’; MPrth r’d, MPrs ry; Paz. NP rd.
raftan [SGYTN-tn'; Iptn'] rav- [SGYTN-; lwb-, cf ravišn; lw-], imp. rav [SGYTN] 38° etc., ravé [SGYTN-yd] 44!; pres. 3d p. pl. SGYTN-nd = ravénd, e. g. 87°, but lwnd = ravand 20%: to go, to walk, to proceed, passim; with prep.: apak kurti- kānšu pānān raft he lived among the slave shepherds 19-10 (cf s.v. kurtīk); apak
```


## [2026-09-04T23:07:00.148Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" SNS_pages.txt | head -3; echo \"---\"; grep -n \"ratu\" SNS_pages.txt | head -10",
 "description": "SNS pages"
}
```


### [2026-09-04T23:07:00.225Z] TOOL RESULT

```
---
2409:                                                                                                                                            xratu- ife     ^j^
5871:                                 iAiWb.    897)p3sav/paratu                   :        L.             ^^'j.,^^,,,, nQn fraz:                                        ^^
6060:                                                                                       'pratuafca- pratyafic- .
6976:                                 ^   ^artuitratumc-^W'"
15149:raainyav- 255/2            royazda- 238/15-253/1                   ratu- 226/3                  vahu. xsaflra-' 262/7
15199:                                      141/21-144/15          pasav/paratu 137/7         bayo.baxta 101/12
15217:                                                             pratuaka-pratySnc- 142/6   barasnQ-baralnav-   9
15297:                                                              xratu- 40/17             x v astan5m 175/7
15911:pursld 141/10              ratustaitlh 226/6                 ravisn 229/7           rOzag 230/12
```


## [2026-09-04T23:07:10.319Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 SNS_pages.txt; echo; echo \"=== markers ===\"; grep -n -E '^\\[|\\[page|\\[leaf' SNS_pages.txt | head -5; echo \"=== ff count ===\"; python3 -c \"\nd=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nprint(d.count(chr(12)))\"",
 "description": "SNS file format"
}
```


### [2026-09-04T23:07:12.607Z] TOOL RESULT

```
    A
>l»>'i




 O^t'

        /
« *>&
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
U*'^ J^»t ^Sj (jl3T v U». ^jb.1^ ^jjt



 tr-w^-r




                                               DP



                                        c-IAjU-vW^
      ^L-tf-JU- o-*i


          4,
                                                      ,la^
          *j             
=== markers ===
9921:[
=== ff count ===
242
```


## [2026-09-04T23:07:20.750Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['SNS','FSF','BQT','MON']:\n    print(k, d[k].get('page_offset'), '|', d[k].get('lookup_hint'))\n    print()\n\"",
 "description": "Check page offsets"
}
```


### [2026-09-04T23:07:23.026Z] TOOL RESULT

```
SNS 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.

FSF 484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking | grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

MON None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
```


## [2026-09-04T23:07:30.292Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport io\np='BQT_v1_pages.txt'\nd=open(p,encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i,pg in enumerate(pages):\n    if 'ارابه' in pg:\n        print('=== leaf',i,'approx printed p.',i-210,'===')\n        print(pg[:2500])\n        print('---------')\nEOF",
 "description": "BQT v1 arrabe page"
}
```


### [2026-09-04T23:07:31.886Z] TOOL RESULT

```
=== leaf 306 approx printed p. 96 ===
-9--
درودگری باشد . ومضفقف اکر هم هست که‌آن
کلمةٌ حرط است - و جاره را نیز گویند که
وید که در مقابل زن است
ارابه - بر وزن فرابه ۰ گردون را
گویند ٩‏ . ۱
اراقو بفتح اول و قاف و واو بالف
کشیده » بلفت رومی
نام تضمی است بشکل
دور و برنگه سیاء و
بفایت‌سلب ؛ و درمیان
کندم و علان. پسیاز
میباشد ؛ و انرا به
شيرازی‌سيمك‌خواند . #ق
آرد تن که و اف
پسرشند و بر ورمهای
کرم و صلب ضماد
کنند نرم ساژد .
ار اهو فی » با میم بر وزن فلاطونی»
- بلغت پونانی لاله را کونند . و آن باغی و
صحرابی هردو می باشد ۰ و بعربی شقایق النعمان
خوانند ۰ و نوعی دیگر هم مت که آنرا
آتربون گوند .
)۱ چش : است .
(:( چك : - وافه اعلم .
اد ان » بتشدید انی بر وزن بران » نلم
ولایتی است از آنریاجان که کنجه و بردع
ازاعمال آن است . گوند سعدن طلا و نفره در
آنجا هست (۱)؛ و می تشدید عم گفته اند ۴ -
و حنارا نیز گونند که بدان دست و پای
ار او فك ه بر وزن دماوند . بععنی
حصرت و آرژو باشد - ودجلة بفدادرا یز گویند»
وبعریی شط خوانند - وبممنی فروشن وشوکت
نیز آمده است - و نام کوهی است در نواحی ‏
همدان مشهور بالوند .
ار ا۲(۵)* بفتح اول و انی بالف کشد.
و های ساکن . بلفت رومی مسطکی را گوبند
و ابا سربی علك رومی خواند .طبیت آن
کرم و خشك است .
از بو - با بای ابجد بر وزن مهرو ؛
میوهُ ات که آنرا امرود کویند ۴ .
ار بو جینا . بکسرجیم وسکون‌تحتالی
و بالف کشیده , بلفت زند و پازند (۳) بمعتی
خربزه باشد ؟ . و آن میوه‌است عمروف و در
نختدیگر جزیره نوشته بودند که خشکی‌میان
دربا باشد وال اعلم (ع) .
اد و داد - بر وزن پهلودار , درخت
شید راگوند چه اربوامرود است ودار درخت.
) چك : ژند و باژند ۰
بطوطه این لفت را درعربی وارد کرد .
وشبةالدهر ولفث و آران وآلان.
دنایتی ۹+
---------
=== leaf 525 approx printed p. 315 ===
ی ۵( ح
نو هه » با نای فرشت بروزنمصومه,
نبانی است که مانند کشوث بردرخت زون‌وبادام
و انجیر پیچیده میشود. گرم و خشك است.
لنچ - بفتح اول بروزن رنج » دو ز ن که
بك شوهر دافته باشند هی يك مردیگربرا بنج
بافند ٩‏ - و نام وستئی هم هست که تفر آرا
بذرالبنج گوبند" وجربی شیکران خوانشد ۴ .
انحشات ۴ ه بکر اول و تالث.بمعنی
کتسداك [ ست که بمربی عصفور خوانند .
پنحشاك‌ رو ان ۴ - نم زای حوز
و واو بالف کشیده و بنون زده . لشان‌الصافیر
است و آن دوایی باشد تند و نیز شبیه بزبان
کنشك 4
تشه - بنم اول بر وزن تنبك » پنبة
محلوح و کلوله کرده را گونند بجهت رشن .
بنچه - نم اول و کسر انی و فتح‌جيم
فارسی » جمعی باشند مراصناف حرفت ورعیت‌را.
فا * ح بروزن چند » چند معنی‌دارد :
٩‏ - فاصلهٌ میان دو عنو که آنرا بعربی
متصل خوانند . ۲ - زنجیری که‌برهای‌دبوانگان
و کنهکاران نهند ۳.٩‏ - تنگهٌ آهنی که بجهت
استکام بر صندوق و کشتی و امثال آن زنند .
- ققل را گوبند . ه - مکر و حیله و زرق
رفرینو سالوسی‌باشد. ٩‏ - عهد و بیمان‌وشرطرا
(۱) چش :  -‏ وگردون .
۱ - رله: بناغ وینانج.
کویند « ثابتی ۱۹۷ ۰ .
گویند .
عقده و گره - وحبس بود ٩۰‏ - سدی کهدرییش
آپ بندند . ۱۰ - بمعنی خبال و مقام است‌مثل
آیکه کوبند «فلان در بند آزار فلان است؟ با
«دربند سفراست» بمنی در خیال آزار فلان و در
مقلم مفر است ۰ ۱۳
باشد . ۱۲ - ربسمان و طناب را گوبند . ۱۳ -
بند ترجیم و تر کیب بود» و آن یتی باشد که
۷ غم وه و محنت باشد . 4۸-
شه‌را بمد از چند بیت بردیف و قافِةٌ دبگر
بیاورند .۰ ۱6 - رهن و کرو را گویند
۵ - حیله و فن کشتی کیری باشد ۷ . ٩‏
جفت کاوبرا کویند که بجهت زراعت کردن
و گردون (۱) و ارابه راندن با هم بدارند. ۱۷-
طومار کاغذ باشد . و هر ده دسته از کاغذ را نیز
مك بندگوبند . ۱۸ - پی گرفتن آنجه عنیم
برده باشد و آنسه از غنیم در دارالحوب گیرند.
٩‏ - جمیم بندهارا کوبند همچو بند کارد
و بندششیر و بلد چافشور و شدخبا و ند تثبان
و امثال آن . _--
طمع و توقم را گوبند . ۲۲ - غلیواج بشد
و آن پرنده‌است ممروف . *
پنفاث ه نم اول » بروزن و معنی‌شاد
و پشتیبان باشد - واصل هرچیزرا نیز کوبند۸ .
بندار بم اول بروزن کل زار ۰ کسه
دار و خانفوار و صاحب تجمل و هکنت باشد -
۶ - نام ولاشی است ۰
: ۲ ص ۹۵ و ۷۱ .۰
٩ ابلم...‎
۸ رگ : شاد .
<گاه‌شماری»۲۰*.
---------
```


## [2026-09-04T23:07:45.149Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg62.png"
}
```


### [2026-09-04T23:07:45.515Z] TOOL RESULT

```

```


## [2026-09-04T23:07:45.512Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-04T23:07:59.570Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 62 -l 62 -r 450 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg62hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg62hi.png'); print(im.size)\nw,h=im.size\n# arabic node region: y approx 0.44-0.48 of page (from 200dpi image y~950-1010 of 2200) -> fraction .43-.47\nim.crop((int(w*0.20),int(h*0.415),int(w*0.80),int(h*0.47))).save('crop_arab.png')\nim.crop((int(w*0.50),int(h*0.33),int(w*0.80),int(h*0.41))).save('crop_pers.png')\n\"; ls -la crop_*.png",
 "description": "Crop regions of page 62 at high res"
}
```


### [2026-09-04T23:08:03.076Z] TOOL RESULT

```
(3825, 4950)
-rw-rw-r-- 1 sfmqrb sfmqrb 39743 Sep  4 14:13 crop_abu.png
-rw-rw-r-- 1 sfmqrb sfmqrb  9680 Sep  4 19:08 crop_arab.png
-rw-rw-r-- 1 sfmqrb sfmqrb 14004 Sep  4 19:06 crop_arx.png
-rw-rw-r-- 1 sfmqrb sfmqrb 17079 Sep  4 19:06 crop_as.png
-rw-rw-r-- 1 sfmqrb sfmqrb  6370 Sep  4 14:09 crop_ml.png
-rw-rw-r-- 1 sfmqrb sfmqrb  5941 Sep  4 14:09 crop_names.png
-rw-rw-r-- 1 sfmqrb sfmqrb  9267 Sep  4 19:08 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12980 Sep  4 19:06 crop_zoom.png
```


## [2026-09-04T23:08:05.913Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_arab.png"
}
```


### [2026-09-04T23:08:06.001Z] TOOL RESULT

```

```


## [2026-09-04T23:08:05.998Z] INPUT

[Image: original 2295x272, displayed at 2000x237. Multiply coordinates by 1.15 to map to original image.]


## [2026-09-04T23:08:16.723Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg62hi.png'); w,h=im.size\nim.crop((int(w*0.22),int(h*0.455),int(w*0.82),int(h*0.50))).save('c1.png')\n\"",
 "description": "Crop Arabic/Persian arrabe row"
}
```


### [2026-09-04T23:08:19.416Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T23:08:22.485Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c1.png"
}
```


### [2026-09-04T23:08:22.561Z] TOOL RESULT

```

```


## [2026-09-04T23:08:22.558Z] INPUT

[Image: original 2295x223, displayed at 2000x194. Multiply coordinates by 1.15 to map to original image.]


## [2026-09-04T23:08:33.494Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON ارابه ==\"; grep -o -n \".\\{0,180\\}ارابه.\\{0,220\\}\" MON_part1.txt | head -6; echo \"== MON آرتیست ==\"; grep -o -n \".\\{0,80\\}آرتیست.\\{0,180\\}\" MON_part1.txt | head -4; echo \"== MON هارمونی ==\"; grep -o -n \".\\{0,60\\}هارمونی.\\{0,160\\}\" MON_part2.txt MON_part1.txt | head -4; echo \"== MON لگاریتم ==\"; grep -o -n \".\\{0,60\\}لگاریتم.\\{0,160\\}\" MON_part2.txt MON_part1.txt | head -4",
 "description": "Grep Mo'in for the Persian words"
}
```


### [2026-09-04T23:08:51.325Z] TOOL RESULT

```
== MON ارابه ==
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,220}
                            \___exceeds complexity limits


== MON آرتیست ==
ugrep: error: error at position 89
x80-\xbf][\x80-\xbf]*){0,180}
exceeds complexity limits___/


== MON هارمونی ==
ugrep: error: error at position 91
n\x80-\xbf][\x80-\xbf]*){0,160}
  exceeds complexity limits___/


== MON لگاریتم ==
ugrep: error: error at position 91
n\x80-\xbf][\x80-\xbf]*){0,160}
  exceeds complexity limits___/
```


## [2026-09-04T23:09:00.798Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nwords=['ارابه','آرتیست','هارمونی','لگاریتم','آرتروز','عرابه','رَد']\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    d=open(f,encoding='utf-8',errors='replace').read()\n    for w in words:\n        idxs=[m.start() for m in re.finditer(re.escape(w),d)][:3]\n        for i in idxs:\n            print(f,w,'::',d[max(0,i-120):i+250].replace('\\n',' '))\n            print()\nEOF",
 "description": "Search Mo'in abridgement"
}
```


### [2026-09-04T23:09:02.898Z] TOOL RESULT

```
MON_part1.txt ارابه ::  عقرب و حوت.    آبی فرهنگ فارسی معین ۳۳    گیاه یا جانوری که در آب زیست کند؛ مق.  خاکی» بری: نباتات آبی. آنکه با چرخ و  ارابه آب به خانه‌ها رساند. (.) یکی از سه  رنگ اصلی (زرد» قرمز» آبی) که رنگ‌های  دیگر از آنها ترکیب می‌شود. (گیا.) به؛  سفرجل. (گیا.) قسمی انگور که دانه‌های آن  مدور و پوستش سخت است و از غورةً آن  گله‌ترشی سازند.   آبی: 55-1 [- آبو] (ص. ا.) برادر مادر

MON_part1.txt ارابه :: ه باشد. (شیم.) عناصر. اجسام  شاف (فز.): اجنامی هنتد که تور آز آنها  عبور می‌کند و حاجب ماوراء نیستند و اشیاء  پشت سر آنهارابه خوبی می‌توان دید. مانند:  شمشه» آب زلال» هوا و غیر ه. اجسام کدر  (فز.): اجسامی را گویند که نور از آنها عبور  نمی‌کند و بطور کلی حاجب ماوراء هستند.  مانند: سنگگ و چوب. اجسام طبیعی (فد.):  مرکب از ماده و صورت جسمیه طبعبه  می‌باشند در مقابل صورت ت

MON_part1.txt ارابه :: اد آهنین: عزم جبزم و  استوار» خواست و قصد و مر دانه.  اراده: (0-)2۲۲802[قس. است. گر دو نه» چرح»  قس. عراده] (.) گردونه» ارابه. (مکن.)  قسمت زیرین هواپیما که چرخ‌ها به آن  پیوسته و هنگام فرود آمدن هواییما نخست  به روی زمین قرار می‌گیرد.   ارادی: 0 (ص نسد.) منسوب به اراده»  واسته به اراده» از روی اراده» کاری که از  رزوی لصا او عزم سور گیرد. فعل ارادی:  فعلی است که پس از

MON_part2.txt ارابه :: 7  فشار دهند؛ قارمن» قارمان.   گاری: (ص.) بی شات؛ ناپایدار.    ۱  ۱  1  ۱  ۱  ۱    گاری  گاری: آءةه (هند. گر دونه] (ا.) ارابه‌ای که با  اسب کشیده شو د.   گاز: و دندان. به دندان گرفتن. به گاز  کردن: به دندان زدن» با دندان گز بدن. سر  کسی به گاز آمدن (اندر آمدن): سر وی  بریده شدن» نزدیکك مرگ رسیدن. دندان  نیش؛ ناب. (قس. گازانبر) آلتی که بدان  چیزها را سرند؛ مقراض. الف -

MON_part2.txt ارابه :: ‌گراینده] ( (ص‌فا.) آنکه میل صعو د به  آسمان دارد» کسی که بخواهد آسمان را  گردونه: (۵-)2۳01102ع (.) ارانه کاری؛  گردون. ارابه‌ای که توپ را حمل کند.  کر دونة داود: نات النعش کبری. (اح.) نعش  (از سنات النعش).   گرده: (ه-) ۲2ج (امر .) زغال سوده‌ای که در  پارچه بندند و بر کاغذی سوزن زده طراحی  کر ده مالند تا از آن طرح و نقش بجای دیگر  نشیند و آن کاغذ سوزن را نیز گویند؛ خا

MON_part2.txt ارابه :: منسوب به  لشکر» مربوط به نظام. زو ایک  سیاهی؛ سر باز ؛ مق. , شهری+ ج. اکن  لش کش : (۱۸3-5۸8):08 [- لش کشسسنده]  (ص‌فا.) ارابه و جز آن که با آن لش گوسفند  را به دکان‌های قصابی برند. مردی که لش  گوسفند را به دوش در لش‌کش نهد يا از آن  برگیرد و بدکان قصابی برد (لغ.)   لص: (و)عع۱ ,(و)عها ,(۱۵5)5 ۳8 (ص. 1.) دزد  سارق؛ ج. لصو ص. الصاص.   لصق: ۱۵ [ع.] (مصم.) چسباندن. پیوند  

MON_part2.txt هارمونی ::  مسحصوص روی درجه دوم گام توقف  می‌نماید و این درجه حالت دومین شاهد را  بیدا می کند. توقف ماهور روی درجة دوم  که از لحاظ هارمونی جزو نوت‌های متوسط  کام است؛ حالت خاصی دارد. البته توقف  روی این درجه زباد دوام ندارد و مجددا به  تیک فرود می‌آید. در ماهور کمتر روی  درجةٌ سوم گام توقف می‌شود ولی ایست  روی درجهة چهارم ممکن است. پس از آن  روی درجهة ۳ می‌شود که نوعی  تغسر مقام

MON_part2.txt هارمونی :: تیمتر است.   4 و هورت: ۱2۲0-10۳7 (امر. آد.)  داد و بیداد تصنعی» ی داد و فریاد تو  خالی و آمیخته به تظاهر و گرافه گوبی.  هارمونی: 0 (.) (مس.) صداهای    رسد و با هم تناسب و ارتباط داشته باشد؛  هماهنگی.    هاروت: 5۳5۰( نام یکی از آدو فرشته   است که در چاه بابل سرازیر آویخته به   عذاب الهی گر فتارند اگر کسی بر سر آن   ج لب جادری زود اور تیم ده   (لف.) فرشته زردشتی که اکنو

MON_part2.txt لگاریتم :: ید در مانا باید جستجو کرد.   مانتو: 0 (.) جامة کشادی که روی  لباس‌های دیگر پوشند (زن و مرد).  مانتیس: 25 [(۱.) (رض.) در لگاریتم  یر ارم وی ون  اعشاری 1" را افانتتس: کوسد: . ضصح.- با  توجه به معنی لگٌاریتم و صفر و مفسر و  مانتیس» همواره مفسر اعداد از یک تانه  صفر و مانتس کلهة قوای صحیح ده نیز  صفر می‌باشد.   مانداب: 22870-0 [مانده آب] (امر.) جابی  که آب آن را کد و متعف

MON_part2.txt لگاریتم ::  سیاسی را  شرح و تفسیر کند. مفسر نظامی: کسی که در  روزنامه؛ مجله و غیره اخبار نظامی را شرح و  تفسیر کند. (رض.) جرو صسیح لگاریتم  اعداد را مفسر و جزو اعشاری لگاریتم اعداد  را رمانتمس» می‌گو یند.   مسفسری: آ-0۱0]25561 [ع. ف.] (حامص.)  تفسیر کردن» تفسیر» گزارش.   مفصل: [22]56 [ع.] (.) (بز.) محل اتصال  دو با چند استخوان به یکدیگر؛ محلی که دو  سر استخوان هم مروط شوند» تعدا

MON_part2.txt لگاریتم :: می: کسی که در  روزنامه؛ مجله و غیره اخبار نظامی را شرح و  تفسیر کند. (رض.) جرو صسیح لگاریتم  اعداد را مفسر و جزو اعشاری لگاریتم اعداد  را رمانتمس» می‌گو یند.   مسفسری: آ-0۱0]25561 [ع. ف.] (حامص.)  تفسیر کردن» تفسیر» گزارش.   مفصل: [22]56 [ع.] (.) (بز.) محل اتصال  دو با چند استخوان به یکدیگر؛ محلی که دو  سر استخوان هم مروط شوند» تعداد  مفاصل در بدن انسان زیاد است و مهم
```


## [2026-09-04T23:09:10.403Z] TOOL CALL #38: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T23:09:10.411Z] TOOL RESULT

```


```


## [2026-09-04T23:09:17.549Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-",
 "prompt": "What does this page say about Persian ارابه — its etymology, meaning, and any Arabic connection?</prompt>\n</invoke>\n"
}
```


### [2026-09-04T23:09:23.242Z] TOOL RESULT

```
# Response to Your Query

The webpage you provided does not contain information about Persian ارابه (araба, a carriage/wagon). 

The page discusses the Proto-Indo-European root **\*h₂er-**, meaning "to fit, to fix, to put together, to slot." While it traces numerous descendants across Indo-European languages—including Persian terms related to "arm" (arm, from \*Hr̥Hmás)—it makes no mention of ارابه or any carriage-related vocabulary.

There is also no discussion of Arabic connections on this etymological reconstruction page. To find information about ارابه's etymology and potential Arabic links, you would need to consult a different etymological resource specifically covering that term.
```


## [2026-09-04T23:09:31.457Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-",
 "prompt": "Etymology and meaning of Persian ارابه (and any Arabic/Turkish entries on the page). Quote the etymology sections verbatim.</prompt>\n</invoke>\n"
}
```


### [2026-09-04T23:09:36.170Z] TOOL RESULT

```
I've reviewed the Wiktionary page on Proto-Indo-European *h₂er-, but it does not contain any entries for Persian ارابه (araba/carriage), Arabic, or Turkish words.

The page focuses exclusively on the reconstructed PIE root *h₂er- meaning "to fit, to fix, to put together, to slot" and its descendants across various ancient and modern Indo-European languages (Greek, Latin, Sanskrit, Germanic, Armenian, etc.).

To find etymology for Persian ارابه or related Arabic/Turkish terms, you would need to consult:
- Wiktionary entries specifically for those words
- Persian etymological dictionaries
- Resources covering Turkic loanwords in Persian

This particular page does not address those terms.
```


## [2026-09-04T23:09:40.990Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-",
 "prompt": "List the root's reconstruction, glosses, derived terms and the Indo-Iranian/Avestan/Persian, Greek, Latin and Germanic descendants given, verbatim where possible.</prompt>\n</invoke>\n"
}
```


## [2026-09-04T23:09:42.248Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%A7%D8%A8%D9%87",
 "prompt": "Give the Persian entry for ارابه verbatim: etymology, meaning, and any related Arabic or Turkish forms.</prompt>\n"
}
```


### [2026-09-04T23:09:47.394Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂er-

## Reconstruction and Meaning

The root is reconstructed as **\*h₂er-**, with an alternative form **\*h₁ar-**. It carries the meaning: "to fit, to fix, to put together, to slot."

## Key Derived Terms and Descendants

**Greek descendants:**
- Ancient Greek ἅρμα (hármă, "chariot")
- ἁρμός (harmós, "joint; fitting")
- ἁρμόζω (harmózō, "to fit together")
- ἁρμονία (harmoníā, "harmony")

**Latin descendants:**
- arma ("arms, weapons")
- artus ("joint; close, firm")
- ars ("art, skill")

**Germanic:**
- Proto-Germanic \*armaz (arm-related terms)

**Indo-Iranian:**
- Sanskrit ईर्म (īrmá, "arm; forequarter")
- Persian ارم (arm, "arm")
- Avestan forms meaning "arm" or "fitting"

**Baltic-Slavic:**
- Lithuanian ir̃ ("and")
- Old Prussian irmo ("arm")

The root demonstrates semantic development from physical "fitting/joining" to concepts like "harmony," "joints," "arms," and even "weapons."
```


### [2026-09-04T23:09:48.437Z] TOOL RESULT

```
# Persian Entry for ارابه

**Etymology:**
The term was "Borrowed from Turkic, from the same source as Turkish _araba_."

**Meanings:**
The word has three primary definitions:
1. Carriage
2. Chariot (example: "arâbe-ye asr-e boronz" = Bronze Age chariot)
3. A colloquial term for a run-down car

**Related Forms:**
The entry notes a Tajik spelling variant: **ароба** (aroba).

The word demonstrates Persian's linguistic borrowing from Turkic languages, with the Turkish cognate _araba_ sharing the same etymological root.
```


## [2026-09-04T23:09:56.859Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/araba",
 "prompt": "Give the Turkish entry for araba verbatim: etymology (including any Arabic, Persian, Aramaic or Turkic source) and descendants.</prompt>\n"
}
```


## [2026-09-04T23:09:58.489Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/araba",
 "prompt": "Give Nişanyan's etymology of Turkish araba verbatim (origin, earliest attestation, and any Arabic عربة or Greek connection).</prompt>\n"
}
```


### [2026-09-04T23:10:04.310Z] TOOL RESULT

```
I appreciate your question, but the webpage content provided does not include the actual etymology entry for "araba" from Nişanyan Sözlük. The page shows only the header, navigation elements, and footer of the dictionary site, not the word entry itself.

To find the etymological information you're seeking—including the origin, earliest attestation, and any connections to Arabic عربة or Greek—you would need to visit the actual dictionary entry page at Nişanyan Sözlük by searching for "araba" directly on their website.
```


### [2026-09-04T23:10:06.345Z] TOOL RESULT

```
# Turkish Entry for "Araba"

## Etymology

The entry states: "Inherited from Ottoman Turkish عربه (araba). Ultimate origin uncertain."

The detailed etymology notes the word originally meant "a two-wheeled cart" and is now used generically for all vehicles and bicycles. Scholars debate whether it derives from Turkic or Arabic origins. The entry mentions borrowing into Iranian languages (Afghan, Shugni, Kurdish), Arabic عَرَبَة (ʕaraba), and Uralic/European/Caucasian languages. A connection to Burushaski arabá is also discussed, though the exact donor language remains unclear.

## Descendants

According to the Wiktionary entry, there is one documented descendant:

**→ Swedish: araba**

This represents the word's transmission into Swedish, where it entered as slang terminology for "car" (automobile).
```


## [2026-09-04T23:10:20.601Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,os\ntargets={\n 'AFM_pages.txt':['عربة','عرابة','عرادة','ارابه'],\n 'incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt':['araba','ʿaraba','arraba','arrāba','عربة','عراده'],\n 'LKT.txt':['araba','Araba','arabe'],\n 'TAD_pages.txt':['عربة','عرادة'],\n}\nfor f,ws in targets.items():\n    if not os.path.exists(f): print('MISSING',f); continue\n    d=open(f,encoding='utf-8',errors='replace').read()\n    for w in ws:\n        for m in list(re.finditer(re.escape(w),d))[:2]:\n            i=m.start()\n            print('###',f,w,'::',d[max(0,i-200):i+300].replace('\\n',' '))\n            print()\nEOF",
 "description": "Search Arabic-loan books for araba"
}
```


### [2026-09-04T23:10:22.703Z] TOOL RESULT

```
### AFM_pages.txt عربة :: صوصض المزوز» ٠‏ اه ٠‏ واعلم ان العرب قد ابقوا. بعض الالفاظ الاعجمية على صورتها 7397 - غيّروها قدلا ٠‏ واكثرها صكّفوها اقح تصحيف او جعاوا فيها القاى والابدال. ونهذا قد صار البحث في محقيق اصل الالفاظ العربة من اصعب وادق الساحث ܠܐܝل وقد ܫܒܐ هذه ܠܐܝܐ الفارسة المعر بة 'منذ سئة 1407 15 101 ` 0065 5 اللغة 393 550 063 غير الى 33130 راجعت كتالي هذا وادغلت فنه كرات كثيرة كانت 5 99 100 ممعت كرات اخرى عديدة غيرها ٠‏ واللي مقر بوعورة الطريق التى سلكت فيها وارجو من علياء اللغة ان ينتقدوا علي 6 لحم للدمقاة ا"

### AFM_pages.txt عربة ::  في ريون ܐ ٠وفي‏ ܪܘܝ جرديل ܙ › ܬܢ كندهبار ܐܝܐ وي ;1 رقلة: وفي كرم جرم . ا باء ٠وثي‏ ܨ ܢ فرند او برند ٠وفي‏ كته قرط ق ٠‏ وف ܥܕ به صو بج أو ܟ ܢ ܢ ابره حبارى فهلم +| : يزيدون جيماً او ܐܪ في ܫ الالفاظ المعربة وذلك يجري غالا في الالفاظ التتهية بالهاء فتالوا ܣ في كوذ ينه ٠‏ دق ربج دقر بق في ك به 0 9 ¶ اللفظة الواحدة بصور 109 10306 الاصل قليلا ܝ منها قرهم في « روتكل » زودكل وزونرك وزَوك وزواك ܝܝ وزون٠وفي‏ . , ܢܐܝ ܨܐܐ ܚܠ 03 ܐ 5 ܨ جار ܕܥ( وجعدر ܕܫ ܚ وجعبر وجعظار الخ لخ :.(طالع 06031 : : لس فقط 5( افعالا 

### AFM_pages.txt عرابة :: حو اربعة وعشر ين رطا فارسي ١س‏ لط فر 0 اسان لاه وزن (0ܣ $ ( ا سقلة > )ܝ تعر يب ܨ وهو ܚܐ ܡ 0 ومقوي المعدة الماردة ا ا لك الس الشتديد ܐܥܪ من سيقت وممناء'الشديد 5 ينوا ` 00 ܨ بيه ول لوا قا 1 9 ® ات قبل معرابة 917 000 9 3 الغليل) : ܣܡܘ 5 مقطوعة ¶( 62 ܨܒ تقد ܝ 1 واصل ܀ ܫܐ ܐܦܐ ܨ ܨ دذاخل البساط وهي لعمة يقال لها بالتركة « يتكزى بوز ® 37 ان احد الصبانܣܘܠ ܛܬܐ حلفت يشد عينَّيهِ بنديل ويتكئ على صدر واحد من 540 5 ان سار الصيان : ܝ ويذهب كل واحد منهم الى (! ܕ % فيلتحف بساط او حاف بأو مسح فيئام ٠‏ وحينئدك ال

### incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt araba ::   gl - ädarahs = ägargafn a. v.  on. - ädaryün = ädargün q. v.  weyt -’adgän: Pl. v..5; dagan q. v.  6451 -’adnaba: Pl. v. _, danb q. v.    li - ’aräba: "Wagen" pers. 7, die arabisierte Form heißt As araba u.  Carabäna, davon russ. serb. arab "Wagen" 8,   Der Verfasser v. Bahär ul-CAam ist der Ansicht, daß araba eigentl.   Sarräda "Geschützlafette, Wurfgeschoßrad" heißt. °c ap. rada, aw.    rava 10 mand. arada 11,    al - ’aräßa: "Steuer; Archiv" pers. 12 wahrscheinlich ist es eine  kontrahierte

### incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt araba :: adnaba: Pl. v. _, danb q. v.    li - ’aräba: "Wagen" pers. 7, die arabisierte Form heißt As araba u.  Carabäna, davon russ. serb. arab "Wagen" 8,   Der Verfasser v. Bahär ul-CAam ist der Ansicht, daß araba eigentl.   Sarräda "Geschützlafette, Wurfgeschoßrad" heißt. °c ap. rada, aw.    rava 10 mand. arada 11,    al - ’aräßa: "Steuer; Archiv" pers. 12 wahrscheinlich ist es eine  kontrahierte Form v., abär bzw. ’awärka s. äbär u. ’awärda .    \; > - —,, - 3 -  lt - ”aräyik: Pl. v. ol ’arika s. arik

### incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt arraba :: en, Mannheim 1979.    Rida, Ahmad: Matn al-lußa, 5 Bde., Beirut 1960.    ZabidlI, Sayyid Muhammad Murtada: Täg al-CArüs, 10 Bde., Benghazi 1966.    II. wörterbücher  Addai Scher: Kitab al-Alfäz al-Mu°arraba, Beirut 1908.    Alavi, Bozorg ; Junker, Heinrich: Persisch-deutsches Wörterbuch, München  1968.    Caläyill, CAbdallah: al-Marfa°; Mu°gam al-wasit, 1. Bd., Beirut 1964.  Asadi Tüsi: Logat al-Foros, Teheran 1957, Nachdruck, Teheran 1987.    Asbaghi, Asya: Die semantische Entwicklung der arabi

### LKT.txt araba :: n  und  Zeichen. GRM  =  Germanisch-Romanisrhe  Monatsschrifl.    Heidelberg.    I,  1909  l'f. GrSVociSic    -  G.  de  Gregorio  e  Chr.  F.  Seybold,  Glossario  delle  voci  sicilani di  origine  araba.    Jn  SlGlIt  III,  225/251.    Palermo  1903. GSAI  =  Giornale  dclla  Societä  Asiatica  Italiana.  Roma. HArHebrAn  =  Joseph  Hyrtl.  Das  Arabische  und  Hebräische  in  der  Anatomie. Wien  1879. Herrigs  Archiv  =  Archiv  für  das  Studium  der  neueren  Sprachen  und  Literaturen. 

### LKT.txt araba ::  Ganzseide  [auch  ins  Semitische  über- gegangen :  syr.  abräsom,  ahr'isüm  BrLex- Syr  ob;  ar.  ibnsam,  ibrisum,  schon häufig  mit  der  Bedeutung  'Seidenfaden, Seidenzwirn',  vgl.  Joseph  Karabacek, Über  einige  Benennungen  mittelallei'- 1  icher  Gewebe  I.  Wien  1882.  S.  21 bis  2'2.].  Ins  Tk.  übergegangen  als  ibri- sim  [offenbar  mit  Anlehnung  an  die Wurzel  ip,  ib  'winden'  Vämbeiy  Tkt- EtWb  Nr.  37].  Aus  dem  Tk.  wurde  rum. ibri^im,  ibri^in  'Seidenfaden,  

### LKT.txt Araba :: a]  'Wagen',  urahagij  'Kutscher, Fuhrmann'.  Hieraus  rum.  araha,  ha- raba  'Leiterwagen',  arabagiü,  harahagiu 'Fuhrmann';  russ.  arbn,  lilruss.  harha, hu\g.  serb.  araba  'Wagen'.  —  ,üie Arabas  werden  von  Ochsen  gezogen und  finden  sich  in  der  ganzen  Berg- landschaft des  Kaukasus  [in  weilen Teilen  Vorderasiens  und  der  Balkan- halbinsel] wieder.  Die  beiden  Räder derselben,  große  plumpe  Holzscheiben, sitzen  fest  an  der  Achse  und  drehen sich  mit  derselben 

### LKT.txt arabe ::   Alters und  vieler  falscher  Etymologien  immer  noch  höchst  werlvoll  für  die  genaue Feststellung  der  Wortbedeutungen.] DE  =  Glossaire  des  Mots  Espagnols  et  Portugals  derives  de  l'arabe  par  R.  Dozy et  W.  H.  Engelni ann.    2i' edition.    Leyde  1869. Del  HWB  =  Friedrich  Delitzsch,  Assyrisches  Handvvöiterbuch.    Leipzig  1896. De  Sacy  ChrAr  =  A.  J.  Silvestre  de  Sacy,  Chrestomathie  arabe  ou  extraits  de divers  ecrivains  arabes,  tant  en  prose  qu'e

### LKT.txt arabe ::   H.  Engelni ann.    2i' edition.    Leyde  1869. Del  HWB  =  Friedrich  Delitzsch,  Assyrisches  Handvvöiterbuch.    Leipzig  1896. De  Sacy  ChrAr  =  A.  J.  Silvestre  de  Sacy,  Chrestomathie  arabe  ou  extraits  de divers  ecrivains  arabes,  tant  en  prose  qu'en  vers,  ä  l'usage  des  6l6ves  de l'ecole  speciale  des  langues  orientnles  Vivantes.    3  Bde.    Paris  1806. Devic  DEt  =  L.Marcel  Devic,  Dictionnaire  etymologique  des  mots  fran^ais d'origine  Orientale  (Ara

### TAD_pages.txt عربة ::                    ‫ال‬                                  ‫املنقوة الى الثملالفصل ليرد الفرع إاللىاصل‬  ‫أمابعد فيقول كانتب هذه السطور انه فسيئة ‪5١51‬‏ عنيت جممشمل الالفاظ‬   ‫لفغية العرية والاافاظ العربة الننشرة افليابطالية واخوامها من لغات‬                                                                   ‫للة‬                                                                     ‫ادخي‬                                                                        ‫ال‬  ‫أنوشربساروتها إذ ذاك با بعكللفظة

### TAD_pages.txt عربة :: فته قد أمعانيداشأوقالي ولقيت منه عنتا شاقا‬    ‫‪85‬‬‫عريةوموقك‬             ‫دلا وات نهمش أحرف‬                             ‫ة‬ ‫مش حروو‬                  ‫أضله بمارستان وهل جر ا‬          ‫ام "ترس وعربة أصابا ا‬                                                                    ‫أصله !‬   ‫الذبيه ‪ :‬اعمأرلاوفقفك اللهأ فسرت اكات الدخيلةعمناها الاصل اللغوي‬  ‫فقط معرضياً عن المعاني النيتوسم القوم فنها أوحصروها وثانيا إني انتقيت الالفاظ‬  ‫النداولة التيهي أ كثشريوعا ب الالفاظ الفارسية إلتى يلسات
```


## [2026-09-04T23:10:38.024Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('LKT.txt',encoding='utf-8',errors='replace').read()\ni=d.find(\"'Wagen',  urahagij\")\nprint(d[max(0,i-900):i+1200])\nEOF",
 "description": "Lokotsch Araba entry"
}
```


### [2026-09-04T23:10:39.804Z] TOOL RESULT

```
bsüchtig,  geizig',  prov.  arabe  'hab- gierig, geizig',  alabre  'gefräßig'.  Die ar.  Adjektivform  'arabl  'arabisch'  liegt vor  in  sp.  alarbe  'roher,  ungebildeter Mensch'  [mit  ar.  Art.],  pg.  alarre  'dass.', kat.  alarb  'd:iss.'.  —  c)  Bezeichnung des  arabischen  Pferdes  im  engl,  angloind. arah  [für  an  Arab  horse],  dtsch.  Araber, so  schon  bei  Marco  Polo:  de  bons  des- triers  arrabins.  Weitere  Belege  bei Hobson-Jobson  33/34.  —  d)  Mit  roma- nischer Endung  -iscus  wird  it.  arabeseo, rabesco  'Schnörkelzeichnung  nach  arab. Weise',  frz.  arabcsque,  rum.  aräpesc, dtsch.  Arabeske  usw.  —  e)  Zur  Bezeich-
9
[Tk.  araba.
nung  des  'Mais'  im  bulg.  arapka  be- nutzt [wie  im  ngr.  äpaßöaTo;].  [DE  5(i bis  57.  ZromPh  XXIX,  418.  ML  58'.) und  590.    Roth  ViFr  38.
90.  Tk.  araba:
[Mit  falsrher  arabisierender  Schreibung 'araha]  'Wagen',  urahagij  'Kutscher, Fuhrmann'.  Hieraus  rum.  araha,  ha- raba  'Leiterwagen',  arabagiü,  harahagiu 'Fuhrmann';  russ.  arbn,  lilruss.  harha, hu\g.  serb.  araba  'Wagen'.  —  ,üie Arabas  werden  von  Ochsen  gezogen und  finden  sich  in  der  ganzen  Berg- landschaft des  Kaukasus  [in  weilen Teilen  Vorderasiens  und  der  Balkan- halbinsel] wieder.  Die  beiden  Räder derselben,  große  plumpe  Holzscheiben, sitzen  fest  an  der  Achse  und  drehen sich  mit  derselben  herum.  Auf  der Achse  ruht,  leicht  und  ohne  anderen Halt  als  den,  welchen  die  oben  liegende Last  des  Wagens  dem  Zapfen  gewährt, das  eigentliche  Gestell.  Mit  diesem höchst  einfachen  Fahrzcufre  wird  durch Dick  und  Dünn,  durch  Täler  und  auf Bergen,  durch  Flüsse  und  durch  Moräste gefahren,  ohne  daß  je  die  Gefahr  des Umwerfens  einträte."  Heinrich  Brugsch, Reise  der  K.  Preußischen  Gesandtschaft nach  Persien  1860  und  1861.  Leip- zig 1862.  I,  51.  [Sain  16.  Gorjajew  5. Mikl  SlEtWb  3.
91.  Tk.  aralas: 'Durcheinander'  [Stamm  ara,  s.  hier Nr.  88],  Vb.  aralasdyrnmk  'mischen'. Hieraus  russ../e;  «/«.s  'Kartenspiel,  Whist'. [Gorjajew  1
```


## [2026-09-04T23:10:50.128Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor leaf in (398,399,400,401,402):\n    t=d[leaf]\n    print('=== leaf',leaf,'approx p.',leaf+543,'===')\n    print(t[:1400])\nEOF",
 "description": "BQT v2 page ~943 for rad"
}
```


### [2026-09-04T23:10:52.040Z] TOOL RESULT

```
leaves 684
=== leaf 398 approx p. 941 ===
  ‫—‪—Ara‬‬                                                                                                         ‫ربوسه‬

 ‫برون؟ ‪ -‬بفتح اول بر وزن زبون ‪.‬‬                              ‫ومجاممت بهم رسد خصوصاً ؛ و باینه‌عنی با زای‬
‫پیش مزد وبیعانه راکوبند » وآن زری باشد که‬                                   ‫‪¥.‬‬         ‫تقطمرار وجیم هم ‪E‬‏‬

 ‫بش ازکار کردن نمز دوردهند؛ ویعضی گونند رری‬
‫باشد که درقیمت متاعی‌داده‌باشند مشروط بابنکه‬                 ‫‏‪e‬‬                                     ‫‏‪ EEE‬باشد‬

‫بد نگاهدار ندوألا یس دهند و زر‬
                             ‫اکر خوش آ‬                       ‫امتال‬   ‫و روباك و‬    ‫د هفنعه‬      ‫وچادر‬    ‫کویندعموما‬


‫خود را بگیرند و درخربزه وهندوانه بشرط کارد‬
   ‫ون‬‫ر)بکه‬‫یضیگر گفته اند (‪۲‬‬    ‫دبع‬
                                 ‫کویند و‬
                                                             ‫باشین ننةقطه دار(‪ ۱)۰‬بر‬            ‫‪8‬‬       ‫ور‬
 ‫زری است که ژ باده از | نجه نمز دور قرار داده‌اند‬
                                                             ‫وچادروهقلعه‬         ‫است که میروش‬          ‫ورال وهعنی‌ربوسه‬
                                                ‫‪.‬‬   ‫ضف‬
                                                     ‫بت‬
                                                             ‫ورویاك زنان باشد وآن دراصل رویوشه بود که‬
 ‫ر ثا = با نای مثلئه(‪ )۳‬بروزن مسیحاء‬                         
=== leaf 399 approx p. 942 ===
                                                                                                     ‫‪ 4۳‬هت‬
                                                  ‫که کیاهی باشد که چرنده را خوردن آن مت کند ‪.‬‬




                                                ‫بیان جهارم‬

                 ‫مشتمل برچهار لغت‬                   ‫فرشت‬
                                                       ‫یه‌با‬
                                                           ‫اقط‬
                                                             ‫دررای بتی ن‬
 ‫رنگه‌میباشد ونرآادرآب کنند ودست‌برآن زد‬                      ‫»رهنه و عریاترا‬
                                                                            ‫ه بفتح اول ‪ ۱‬ب‬                ‫رت‬
 ‫چون‌صابون کف بآروردجامه بدان شویندخصوصاً‬                     ‫گوبند ‪ -‬وم اول تهی دست وبینوا ‪ -‬وبرهنه‬
                                                             ‫وخالی گروابند ‪ -‬و بمعنی‌کاغذ هم بنظر آمده‬
‫جامة ابرشمی‪ .‬وچون باسرکه برختازیر طلا‬
‫کنند تحلیل دهد » و اکر بماآربزنگوش در‬                        ‫است ‪ - ۴‬و همه را نیزگوبند و بعربی کل‬
                                                                                                          ‫خوانند ‪.‬‬
 ‫فندق‬      ‫بوی‬
             ‫رد »‬
                ‫صپبر‬
                   ‫کبوری را‬
                          ‫چشم کشند ش‬
                                 ‫خوانند ‪. ۴‬‬     
=== leaf 400 approx p. 943 ===
    ‫سس‬                                                                                                      ‫رجوعام‬
 ‫ا او ماندند»‬   ‫تف و دوسہط‬    ‫سر دسل‬   ‫از مطاوعش‬        ‫رونك‬   ‫حمام‬   ‫ددوارهای‬     ‫و‬    ‫زم اه‬   ‫زعمن‬   ‫در‬   ‫که‬   ‫است‬


 ‫وسبط بکسر اول در عربی گروه وقبیله و فرزند‬              ‫صر دهد »‬          ‫أحنلای‬       ‫و شر‬      ‫مخورند‬          ‫وا‬

‫زاده گروابند؛ ورجوعا بحذف میم هم‌بنظر ا مده‬                                            ‫وبعربی خرفه رگاویند ‪.‬‬
                                                        ‫جروعام" ‪ -‬بفتح‌اول وثانی‌بواورسیده‬
                                           ‫‪.‬‬   ‫است‬

 ‫رجه ‪ - ۴‬بفتح اول وانی ‪ ۰‬طنابی‌باشد‬                    ‫می‌نقطه ( ‪ )۱‬بالف کشیده ویمیم زده » بلفت‬                  ‫رعن‬

‫کجهامه و لنکی و چیزهای دیگر بربالای آن‬                  ‫سربانی نام پسر سلیمان علیه‌اللام است » چون‬
                                       ‫انداز ید ‪.‬٭‬      ‫ولیمهد پدر شدیسیب هوا و وی بسیار ده سبط‬


                                               ‫سان ششم‬     ‫ص‬




     ‫ووو لغت و کنات‬              ‫در رای بی نقطه باخای نقطه دار مشتمل بر ست‬

 ‫ديهم هم هت که تاج بادشاهان باشد ‪ -‬وسوی‬
                                                        ‫رخ = بفتح ارل وسکون انی » بمعنی‬
 ‫وطرف وجاب رایز گفته‌الس وکنایماهی است ‪۷‬‬                 ‫شکاف‌ررخنه وچاك ‪ -۴‬وغ‌ونصه واندوه‌باشد؟ ‪-‬‬
          
=== leaf 401 approx p. 944 ===
 ‫رخش‬                                                                                             ‫~‪t‬‬


                             ‫مرده را نز گفته‌اند‬         ‫رخبین ‪ » ۷‬اول وبای‌ابجد بتحتالی‬
‫کنابه ازمقیم‌شدن‬        ‫رحت افکندن‬                       ‫رسیده بروزن خرجین » دوغ ترش سخت نشدمرا‬
                           ‫_ وعاجز آمدن باشد ‪.‬‬            ‫گوبند» وبعضی کوبند چیزست کهآ ترا اکزشك‬
                                                         ‫آوردوشیرسازند وترش مزه باشد مانند قراقروت‬
‫رحت بلرست ک=نابه ازسفر کردن‪.‬‬
                                                         ‫ترش سخت شده همچو‬           ‫غ‬
                                                                                    ‫‪-‬و‬‫ددو‬
                                                                                        ‫سياه رنگه بو‬
                                    ‫ومردن باشث ‪.۰‬‬
                                                         ‫پنیر را گنفزته‌اند ؛ وبکراود هم‌آمده است»‬
‫شی!دن ه کنابه از‬
               ‫کحر‬
                 ‫خت بص‬
                     ‫ر‬                                   ‫وبعضی گوبند هرچیز که آنرا ازدوغ ترش سازند‬
                ‫مردن باشد که سفر آخرت است ‪.‬‬                                      ‫رخبین ورخبینه خوالند ‪.‬‬

‫خت لستی» کنابهاز سفر کردن دیا‬
                            ‫ر‬                            ‫رخیینه ‪ = ۴‬بنماول‪,‬بمعنیآخررخیین‬
    
=== leaf 402 approx p. 945 ===
  ‫‪4 ) ۰۷‬‬                                                                                 ‫رخعا‬


‫وئالث بالف کشیده» بمعئی رخشان ورخشندموتابان‬      ‫واحب رستم‌را لیزباین اعتبار رخش میگفته‌اند ‪١‬۔‏‬
               ‫باشد ؛ ویضم اول نگیفزته‌اند ‪.‬‬    ‫ومطلق اسب را هممیگوبند ‪ - ۴‬و بمعنی ابتدا‬
‫رخشان ‪ = ۱‬بم اول بروزن هتان ‪۰‬‬                      ‫دوب‬
                                                     ‫نزک‬
                                                       ‫کردن هم‌هست ‪ - ۴‬و قوس قرح را نی‬
     ‫بمعنی رخشا است که تابان وروشن باشد ‪.‬‬        ‫ریمعتی هبارکي وفرخند کی ومبارك ومیمون هم‬
                                                  ‫را نیزکوبند ‪-‬‬   ‫وبا گونه وعکس‬    ‫آمده است ‪-‬‬

‫رخش بهار ‪ -‬کنابه از باد بهاری‬                    ‫و م اول روشنی و شعاع وپرتو دورخشند کی‬
                         ‫وابر بهاری باشد‪.‬‬   ‫‪2‬‬     ‫اشد وبکی ازنامهای آفتاب عالمتاب است ‪. ۴‬‬
‫خش خور شید وماه ک‪-‬نابه‬
                     ‫ر‬                           ‫وکون ثانی‬
                                                         ‫رخشا ؟ ‪ -‬بفتح اول س‬

 ‫‪ ۰ ۱‬چنانکه مشهور است رخش رستم مر کب بود ازرنگه قرمز وزردة تخم مرغ‬
  ‫وسفیدی و کلهای بیار کوچك میان زرد وقرمزداشت وبیضه وزیر دم و از زبرچشم تا دهن سفید‬
  ‫بود که اورا بورابرش بضه سفید میگفتند > « فرسنامةٌ اسداله خواناری بقل نمعلیقات نوروزنامه‬
 ‫(ماسة ملی ابران ‪ .‬ترجمةٌ بزر که علوی‪ .‬تهران ‪ ۷۲۳۱‬ص‌‪۸۱‬ح ‪:)
```


## [2026-09-04T23:11:05.088Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(pages):\n    if 400 <= i <= 415:\n        # look for rad-like headwords\n        if 'مهتر' in p or 'دستور' in p or 'موبد' in p:\n            print('=== leaf',i,'p.~',i+543)\n            for line in p.split('\\n'):\n                if 'مهتر' in line or 'دستور' in line or 'موبد' in line or 'سرور' in line:\n                    print('   ',line.strip()[:300])\nEOF",
 "description": "Find rad entry in BQT v2"
}
```


### [2026-09-04T23:11:07.268Z] TOOL RESULT

```
=== leaf 408 p.~ 951
    ‫که هوبشمان در دستور ارمنی‬         ‫‪ ۳۳۳‬و تاریج بلیام سربالی‬       ‫میلادی) چاپ ‪ecineV‬‏ ‪۶ ۰‬ص‬
=== leaf 413 p.~ 956
    ‫کردید و بی دستوری در آمد " و داخل کرد (سك) سرخود درآود » < منتهی‌الارب > ‪.‬‬
```


## [2026-09-04T23:11:12.336Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\npages=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (406,407,408):\n    print('=== leaf',i,'p~',i+543,'===')\n    print(pages[i][:2600])\nEOF",
 "description": "Read BQT leaves 406-408"
}
```


### [2026-09-04T23:11:14.442Z] TOOL RESULT

```
=== leaf 406 p~ 949 ===
      ‫‪- 6‬‬                                                                               ‫رژیدن‬

‫رر بدن "ت بورژن رسیدن » بمعنی‬                      ‫اندازند وبعربی شربط کوبند وبزبان دیگر سازو‬
                      ‫رنگه کردن باشد ‪.‬‬             ‫خوانند ‪ -‬وسکه انگور را کیفزته‌اند که بتازی‬
‫ددلن » بر وزن امین ‪ ۰‬بمعنی محکم‬                    ‫عنب‌الملب کوبند = و باتشدید ثالی در عربی‬
                                                  ‫حلقه‌ای که برآستان درس کنند ‪ ۱‬و‪-‬ققل را‬
‫واستوار ومضبوط باشد؟ ‪ -‬ودرعربی‌به‌عتی آرمیده‬
‫و آرامکرفته و کرامایه وچیزبکه بوزن کران‬             ‫لیز کوبند‪ .‬وبمعنی زدن‌هم‌هست که بعربی ضرب‬
                                ‫وسنکن باشد ‪۴‬‬                                            ‫خوانند ‪.‬‬



                                         ‫بیان نهم‬
                  ‫غوت‬
                    ‫لد‬‫ررای بنیقطه با زای فارسی مشتمل بر‬
                                                      ‫د‬

‫ررد (‪ »)۱‬بفتح اول وسکون انی بر | براستی‌آن دبوار سازد وآنرا رزه‌بهنایز کوبند‪-‬‬
‫ورسمالی که هر دو سر آ را برجایی نشدلد ویر‬          ‫درهمه چیز را‬   ‫‪ ,‬سيار خوار وحر‪.‬ص‬     ‫وزن وجد‬

‫ومثال آن اندازند و آنرا‬
                      ‫آن رخوت پوشیدلی ا‬                                              ‫کوبند ‪: ۷‬‬




                                                                    ‫(‪ )۱‬چك‪ :‬رزد ()‬
  ‫از ‪ :‬رز (ه‪.‬م‪٣ ) .‬‏ يدن‬    ‫‪-‬‬    ‫‪۳‬‬             ‫امروز « چفته ورزه » مستعمل است ‪.‬‬   ‫‪- ۱‬‬

                    ‫‪ ۴‬ماخون از (عی) «ناطمالاطبا» رك‪ :‬حاشية ‪: 4‬‬               ‫(پونه مصدری) ‪.‬‬
         ‫چون عهد ٽو ليکو وچوحلم "و رزین‌است‪.‬‬            ‫چون قدر تو عالی وچو روی توکشاده‬
  ‫د منوچهری دامفانی ‪.* ۶۷۱‬‬
      ‫(عر) ‏ رزن ازباب کرم بعنی آهسته و بآرام شد ووصف آن د«ررمزکیرن»‪...‬‬             ‫‪۴‬‬
  ‫® _ رك ‪:‬‬              ‫و «درزین » چیزکرانمابه و تقیل و باسنگه است‪ « » .‬شرح قاہوی *‪.‬‬
                                                                                   ‫رزد » ری ‪.‬‬
           ‫ز چشم است کوبد رژدی گلوی‪.‬‬                   ‫ز دبدار خیزد هزار آرزوی‬      ‫‪۱‬‬
   ‫ابرشکور بلخی «لفت‌فری‪٩۸۹-۹‬‏ ‪.‬‬
   ‫ویایگانی ودامالی‬
                  ‫‪ ۷‬ط‪-‬بری ‪( 2۲‬قطار) د ساب طبری ‪ ۱۹۳‬گ‪۰‬یلکی و تهرانی کل‬
 ‫از‬     ‫نرا‬
          ‫زفاهای‬
               ‫ار ص‬
                  ‫روزبصو‬
                       ‫سمر‬
                         ‫‪ ۸‬ا‬                            ‫[‪( 8۲‬ردیف ‪ .‬صف )‪ .‬رك‪ :‬رده » رجه ‪.‬‬
                                                                  ‫برایررفرمانده «رژه » گوبند‪.‬‬

=== leaf 407 p~ 950 ===
                                                    ‫بیان دهم‬
          ‫رای می نقطه باسین بی نقطه مشتمل بر ببست وبك لفت و کنایت‬                                  ‫در‬

  ‫ویت‬ ‫چیوزی باشد از خحبرکا‬    ‫اضداد است ‪-‬‬                    ‫ر سس س بفتح اول وسکون‌ئالی ‪ ۰‬بمعنی‬
 ‫وامثال آن ‪ -‬ومقدمةٌ ابتدای نب ‪ -‬وبهم رسیدن‬                 ‫رسیدن و وارسدن باشد ‪ - ۱‬و بمعتی فاعل که‬
‫حرارت را نیز گویند ‪ -‬و نامکوهی هم هٽ ‪۹‬‬                       ‫وارسنده باشد ‪ - ۴‬وامربرسدن هم هت بعنی‬
‫رسام = با تشدید ثالی بر وزن قام »‬                           ‫ری ‪٩‬‏ و‪-‬طناب و کمند ورسن را لیز‬
                                                                                          ‫ویاو‬
                                                                                             ‫بر‬
 ‫نآاهمنگری است که تدبیرسکندرآینه ساخت_‬                       ‫کوبند‪ - ۴‬وطلا و لقره ومس و سیماب وسرب‬
          ‫وئام نقاشی که درخدمت بهرامگور میبود ‪.‬‬              ‫وآهن وهرچیز از فلزات که آنراکشته باشند ‪-‬‬
 ‫رسانه = بروزن‌بهانه» حسرت وافوی‬
                                                             ‫ودرهادی شیر هرچیزوهربك از فلزات کشتهرا‬
                                                             ‫رس« یگویند وجمع آن‌رساین‪ -‬ونام رودخانه‌است‬
                                       ‫وتاسف را گونند‬
                                                             ‫که به اری اشتهار دارد ‪ - ۴‬کولوبند زانرالیز‬
 ‫رسپبنا ‪, = .‬ابای فارسی بروزن‌تخمناء‬                        ‫گفتها ند ‪ -‬و یمعنی مفسد وفاد کننده هم‌آمده‬
  ‫بلضت زند وبازند (‪ » )۲‬قصل بابیز رگاونند ‪.‬‬                  ‫است ‪ -‬وشکم خواره وپرخور وحریص درهرچیز‬
‫هفتح اول بروزن مت » ماضی‬   ‫رست ب‬                             ‫خوردلرا نیز گویند‪ .‬وبعربی!کول‌خوانند‪ .‬وبمعنی‬
‫رستن است یعنی خلاص شد و لجات بافت *‪-۷‬‬                        ‫آرخکه کاول وشکم خواره حوریص باشد بم‬
‫حدققین بر کسی اطلاق کنند که از صراط‬
                                  ‫ومنز‬                       ‫و کلونند را لیز گوبندا ‪۳‬‬   ‫اول‌هم | مده‌است ‪۳‬‬
 ‫خواهش‌ضالی رسته باشد واز دوزځ قید به‌بهشت‬                  ‫ومحکم وسخت‪,‬ر | همگفته‌اند‪ ۷‬وبکر اول اهر‬
‫لجات پیوسته ‪ -‬وبمعتی زمین ‪ -‬و صفه وابوان‬                     ‫‪ -‬ودر‬   ‫برسیدن ورشتن (‪ )۱‬است ينی بریس‪۸‬‬
‫شیده را یز‬
         ‫صف‬‫ههمست (‪ - )۳‬و راسته و ک‬                          ‫عربی بفتح اول وثالی مشدد ساکن ‪ ۰‬بمنی صلاح‬
‫کوبند ‪ -۱۷‬وبضم اول ماشی روبیدن باشد معنی‬                    ‫وفساد کردن در ميان مردم باشد و ایذجا بطریق‬
  ‫(‪ )۳‬چك‪ :‬همآ مده است ‪.‬‬                   ‫(‪ )۲‬چك ‪ :‬ژد و بازند ‪.‬‬               ‫(‪ )۱‬چك ‪ :‬رستن‬


      ‫‪ - ۳‬قس‪
=== leaf 408 p~ 951 ===
 ‫—‪AtA-‬‬                                                                                          ‫رستاخیز‪‎‬‬
 ‫رستگار است کهبمعنی خلاص و فجات باشد ‪-‬‬                    ‫بموط هم‬     ‫ضحک‬
                                                                        ‫می م‬‫وعت‬
                                                                              ‫روبید وبرآمد ‪ - ۱‬وی‬
 ‫و تزد محققین صاحب دولتی است که زخارف‬                      ‫آمده است ؟ ‪ -‬و نوعی از خاك سخت باشد ‪-‬‬
‫او‬   ‫دامنگیر حال‬   ‫وممنوی‬       ‫و تملقات موری‬    ‫دلوی‬
                                                           ‫ومطلق خاکه را نکیفزته اند‪ -‬و بمعنی شجاع‬
                                                ‫نباشد ‪.‬‬    ‫ودلیر ‪ -‬وچیره وغالب آمدن ومتولی شدن هم‬
                                                                                                  ‫‪۰‬‬   ‫صبت‬
‫‏‪ o‬بروزن افلااء ‪ ۰‬شاج ءازه ای‬        ‫رستاك‬

‫راکومند که ازبیخ درخت برآبد ؛ و پاین معنی‬                   ‫‪)۱‬‬
                                                             ‫رستاخیژ ‪ ۴۰‬با خای قطه د(ار‬
                 ‫بشاین قطه دار هم آمده است‪.‬‬                ‫بر وزن دستاویز ‪ ,‬قیامت را گوبند که محشر‬
‫رستخیز ‪ = ۱‬بنتح اول وثالك » بمعنی‬                                                                  ‫باشث ‪.‬‬
 ‫؛بم اول بمعنی‬
             ‫رستاخیز است که فیامت باشد و‬
                                                            ‫رستاد ‪ - ۴‬بر وزن هقتاد ‪ .‬مخفف‬
                                       ‫لوخیز باشد ‪.‬‬
 ‫رستگار ‪ ۲۰‬با ان فارسی بر وزن‬                              ‫راستاد است که بمعنی وظیفه و راب و روزباله‬
                                                                                                   ‫باشك ‪.‬‬
‫قندهار » بمعتی خلاص ونجات وفیروزی بابنده‬
                                            ‫باشد ‪¥.‬‬         ‫رستار * ‪ -‬بر وژن دستار ‪ .‬مخفف‬

                                                                            ‫(‪ )۱‬چك ‪ :‬باخا ‪.‬‬

                                                ‫هکر ‪‎ :‬یر ‪.‬‬      ‫‪۰‬‬        ‫‪ :‬رستن ‪.‬‬     ‫رکه‬
                                                                                         ‫‪١‬‬
     ‫‪.‬دذرشته) ‪ .‬بهلوی ‪ + 451۲‬خیز (رك ‪ :‬خاستن) ‪,‬‬
                                              ‫‪1‬ست‪۳‬ا‪ ( 805-1‬مرده گ‬
                                                                ‫‪ - ۴‬از او‬
     ‫‪,‬ازند ‪ 012۵58051۲‬داسشق ‪ ۳۱۱2‬؛ بنابرین رستاخیز (مخفف آن » رستخیز)‬
                                                                    ‫پهلوی ‪ 2072۱51۲‬پ‬
         ‫رك‪ :‬راستاد ‪.‬‬   ‫‪۴‬‬
```


## [2026-09-04T23:11:25.926Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\npages=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (403,404,405):\n    print('=== leaf',i,'p~',i+543,'===')\n    print(pages[i][:3000])\nEOF",
 "description": "BQT leaves 403-405 for rad"
}
```


### [2026-09-04T23:11:27.890Z] TOOL RESULT

```
=== leaf 403 p~ 946 ===
 ‫ردای لیل‬                                                                                   ‫م‪ ۳‬پهب‬
‫واگر پراو را درخانه بخور کنند جمیم جانوران‬                           ‫از شماع وپرتوآ فتاب وماه باشد ‪.‬‬
                                 ‫کزنده بگریزند ‪.‬‬        ‫وسرفا ورای‬
                                                                 ‫دح فرود = بضم اول ک‬
‫رنه = بفتح اول ونون وسکون الی»‬
                             ‫ح‬                          ‫یقطه (‪ )۱‬بواو کشیده و بزای نقطه دار زده »‬ ‫ا‬
‫باشد ‪2‬‬     ‫راهی را گونند که در دیور واقع شه‬             ‫نام روز هفتم ازماه های ملکی‌باشد ‪ -‬وبفتح اول‬
‫وسوراخ هرچیز را یز گفته‌اند ‪ -‬وبمعنی دربچه‬              ‫دستینه راکوبند که آنرا چهار تو همچورسمان‬
‫بت وم‬      ‫وشکاف وجاك وامثال آن م آمده ات‬                                             ‫تأده باشند!ا ‪.‬‬
        ‫اول‌کاغن رگاویند وبمربی قرطاس خوانند ‪.‬‬          ‫رخ گیر ‪۵‬سبنتح اول کوسرکاف بروزن‬
‫رخنه رده ربزان کنابه ازمطمون‬                            ‫همشیره » بمعنی آخر رخ فروز است که دستینه‬
                                                        ‫باشد که آنرا چپار تو مالند رسمان تایده‬
                                      ‫خلایق باشد ‪.‬‬                                              ‫باشند ‏ ‪.‬‬
‫‪ -‬بر وزن رسدن » بمعنی‬               ‫رخدن‬                                        ‫ر حمه صیفتح‬
‫فس کشیدن‌باشدببب برداشتن و کشیدن‌بار کران‬                                       ‫اولومیم وسکون‌الی»‬
                                          ‫ومشقت ده‬                              ‫مرغی است که آرا‬
  ‫خرینه‪- ۴‬بروز نکمینه‪.‬بمعنیرعیته؟‬                                                 ‫‪۴‬‬    ‫رد‬
                                                                                        ‫بان‬
                                                                                          ‫وخو‬
                                                                                            ‫کدار‬
                                                                                               ‫مر‬
‫است که صم درخت صنوبر باشد وبعربی رائینج‬                                         ‫اکر سر کین او را در‬
‫خوانندوبعضی کوبند راتینج‌لفتی است‌رومی وبسنی‬                                    ‫زیر زن آبستن بخور‬
                 ‫دیکرکوشب ههرب رخینه است ‪.‬‬                                      ‫بیندازد ‪,‬‬       ‫کننه بچه‬



                                                ‫بیان هفتم‬
               ‫در رای بی‌نقطه با دال ابجد مشتمل بر شش لغت و کنات‬
                       ‫‪.‬‬   ‫واز لظر افتاده فود‬   ‫مردود‬   ‫‪ -‬بقتح اول وسکون ٹانی ‪ 0‬حکیم‬        ‫رده‬

‫است ‪-‬‬    ‫تیل ت کنابه از آسمان‬         ‫ردای‬              ‫وداشمند ‪ -‬و خواجه ‪ -‬وپهلوان ودلاور و بهادر‬
                              ‫وب را لکیوزبند ‪.‬‬
                                             ‫ش‬             ‫نی‬
                                                            ‫عربی‬
                                                               ‫مر ع‬
                               
=== leaf 404 p~ 947 ===
   ‫‪—ttA‬‏‬                                                                            ‫رد کا‬
 ‫رده ‪ - ۴‬تح اول وثالی » صف ورستة‬                ‫ردک ‪١‬ہ‏ بفتح اول وسکون ثالی وکاف‬
 ‫آدمی وحیوانات دیگر‪ -‬وهرچیز که وربكراسته‬       ‫بالف کشیده » بلغت زند و پازند ( ‪ ) ۱‬بمعنی‬
 ‫باشد حمچو دندان و دکان و خاله و برح وامثال‬    ‫راست و درست باشد که درمقابل کج و درد غ‬
 ‫آن‪ ۴‬وچوبیرا یز گوبند که درزبرآن غلطکها‬                                              ‫است ‪.‬‬
‫راست کنند وبر گردن گاوبندند وبربالای غلهکه‬      ‫رد نحو ؟ ‏ باجیم بروزن سمن بو ‪۰‬‬
             ‫ازکاه جدا شده باشد بگردانشد ‪.‬‬
                                                ‫ام کرمیست که پشمینه راخراب میکند وبعربی‬
                                                ‫واين ممنی بجای حرف ثالی‬
                                                                      ‫ارضه گوبند ؛ ب‬
   ‫است که یکی از دوازده برج قلکی است ‪.٩‬‏‬                                   ‫واو هم آمده است‬



                                       ‫بیان هشتم‬
             ‫‪۱‬هر سنرده لغت‬        ‫‪۳‬‬     ‫در رای بی‌نقطه بازای نقطه دار‬


‫وحرباغ را گونند‬   ‫وبمعنی انگورهمآمده است ‪-‬‬      ‫مفتح اول و سکون تالی » درخت‬     ‫=‬   ‫رز‬

  ‫انکور باشد ® و بمرپی‌کرم خوانند یفتح‌کاف ‪ | -‬عموماً ‪٦‬‏ ‪ -‬و باانعکور را خصوصاً و‪-‬مطلق‬

                                                          ‫‪ :‬رتد ویاژند ‪.‬‬   ‫)‪ (۱‬چك‬


      ‫‪ ۱‬هز ‪ , 2120۵۲‬پهلوی ‪ ۰ 452۲‬راست «یونکر ‪ ۵۰۱‬بی‌اصل « رادکا » امت‬
    ‫‪ ۴‬ظ » ازیهلوی ‪ « # 61202۲‬حوشمان‬           ‫‪ - ۴‬مصحف « روئجو » (ھ‪.‬م‪. ).‬‬
           ‫‪ 6‬ورکه ‪ :‬استق ‪ » ۹۰‬در اوراق مالوی (پهلوی) ‪( 80۲‬سطر » صف ؛ ردیف)‪:‬‬              ‫‪۹‬‬
           ‫‪(Henning,‬‬      ‫‪A list of Middle‬‬         ‫‏)‪Persian..., BSOS ,lX,1,p.87.‬‬
  ‫ودو جزو مکی برین کنار‬      ‫‪۰:‬‬       ‫را‬               ‫کے کو‬
   ‫* گیلکی ‪ 22۳‬ازتبره رزها است ودر‬              ‫نپی ویکی بنرکآناراهی ‪« »...‬داشنامه ‪.*۷۷‬‬
                                  ‫تمام لقاط ‪ 8‬سطح زمی‌کاشته میشود ‪.‬گلهای آن دارای ه‬
                                  ‫کاسبر که سبزاست که بریوشی متصل شده‌اند وهنگام باز شدن‬
                                  ‫کل سر پوش از پابین جدا میشود وه پرچم ونخمدالی با دوبا‬
                                  ‫بنج برچه جم چسبیده ازآن بیرون ميآد ومیوه ای میسازد که‬
                                  ‫‪ 2۲61101۷‬زا‪۷‬‬        ‫آنراسته‌باانگورمیگوینده کل کلاب ‪۱۳۲‬‬
                                ‫‪ - ۱‬در خواداری‪.‬‬             ‫‪ :‬رزبان ‪.‬‬      ‫ه‬
                                                                           ‫کو‬‫ر‪۳‬‏‬
                                                                               ‫ث«ابتی ‪۸۱٩‬‬
                                  ‫‪ 2‬بمضی باغ‌است «سالنامة فرهنگه کلپایگان ‪ » ۷4‬ودرطبری‬
                                  ‫‪۶‬رمه وز“ بمعنی‌باغ خرم آ مده‪ .‬رکه ‪ :‬واژه شناسی ص ‪:۸۳۲‬‬
                                                                                      ‫خ‬

                                  ‫‪ 2‬یکی را در رز درخت انجیر بود و
=== leaf 405 p~ 948 ===
  ‫رزه‬                                                                                               ‫‪‎-‬ی ) ‪“A‬‬


 ‫مکان‌جنکه‬      ‫زرمگاه‪ -‬بروزن گا‬                         ‫رنگضرا کننزته‌اند ‪-‬و‪٩‬ی‏معنی رنگ کننده ‪- ۴‬‬
                                                         ‫وامر برنگ کردن هم هت ‪٩‬‏ ‪ -‬و زهر هلاهل‬
                                                          ‫را کیویزند ‪ -‬ویکس اول مخقف ریز باه‬
                       ‫گاه باشد ‪۲‬‬   ‫کردن وجنگ‬

   ‫مت‬      ‫که‬         ‫ون‬     ‫ررمگه ‪-‬‬
             ‫رزمگاه است که جنک گاه باشد ‪۹‬‬                ‫ازریختن مشتق است ‪ -۴‬ودرعربی شالی راگوبند‬
 ‫بروزن گرم سیر ‪ ,‬لامروز‬
                                                         ‫کبهرنج پوست دباارشد ‪ ۴‬چرهزاز براج کوب‬
                        ‫مگیر =‬            ‫رد‬
                   ‫بازدهم باشد از ماهپای ملکی ‪۱‬‬
                                                                                      ‫رکاویند ‪.‬‬
 ‫ررمه = بفتح‌اول والك وسکون ثالی»‬                       ‫ربران * د بباای ابجدبالف کشیده‬
  ‫ایند*‪ -۱‬وبك لنگه بار واسباب‬
                            ‫رو‬‫بوفچرخت ک‬                                  ‫بروزن بزدان ‪ .‬باغبانرا گویند ‪.‬‬
 ‫وقماش را نکیفزته‌اند » و بکضویبند ابن لفت‬               ‫ررد ‏‪ = ٩‬بقتح اول وسکون نالی ودال‬
                    ‫غرمی است‪ »:‬وبکسی اول ات‬                     ‫ابجد (‪ » )۱‬پرخور وشکم خوار کروایند ‪.‬‬

 ‫دزم یوز بوامبیامی حطی (»)‬                               ‫ررده ‪ = ۷‬بقتح اول بر وزن زرده »‬
                                                              ‫بمعنی «انده وکوفته شده وآزرد‪ :‬راه باشد ‪.‬‬
‫جوز بمعنی تفحص و تجسی و جستجو کردن حم‬                    ‫درم = بفتح اول وسکون الی و میم »‬
                                    ‫‪٣‬‏‬    ‫آ مده ات‬       ‫بمعتی جنک و جدال باشد ‪ - ۸‬و هیمه وهیزم‬

    ‫زره د بنتح اول وتخفیف ثالی » ن‬                       ‫وی »‬
                                                            ‫طعام پختن را نیزگوند ‪ -‬و بفتحاتولال‬
‫‪۱‬ت‪ .۴‬وآن ناي ا هردوسوآیرا‬                 ‫‪E‬‬             ‫رنگه هم‌آمده‬     ‫بعنیر نگه میکنم‪٩‬‏ چه ربزمعتی‬




                                         ‫(‪ )۲‬چك ‪ :‬بامیم ویا‪.‬‬               ‫امد‬       ‫‪:‬‏‬   ‫(‪ )۱‬چك‬


   ‫رکه ‪:‬‬     ‫‪۴‬‬           ‫‪ ۴‬در ‪ :‬رنگرز ( رنگگ رزنده ) ‪.‬‬                  ‫‪ :‬رزیدن ‪.‬‬         ‫رکه‬
                                                                                            ‫‏‪٩‬‬
   ‫*‏ از ‪ :‬رز‬            ‫وید دوم) برنج ( منتهی الارب ) ‪۰‬‬
                                                       ‫اتولشد‬               ‫م‬
                                                                            ‫(ضرز‬
                                                                               ‫‪۴‬‬                     ‫ربخن ‪.‬‬
                                                   ‫(باغ وباغ انگور) (ه‪.‬م‪ ).‬بت بان (یسوند حفاظت ) ‪:‬‬
         ‫مادر ایز‪ ,‬بچگکایرا ندهد شیر همی ‪...‬‬                  ‫رزبان گفت چه رابت وچه ندییرهمی‬
    ‫«م
```


## [2026-09-04T23:11:42.785Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\npages=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(378,390):\n    p=pages[i]\n    if 'را ' in p[:400] or 'بیان اول' in p or 'حرف الراء' in p or 'باب الراء' in p:\n        print('=== leaf',i,'p~',i+543)\n        print(p[:1200]);print()\nEOF",
 "description": "Find BQT ra section"
}
```


### [2026-09-04T23:11:44.740Z] TOOL RESULT

```
=== leaf 379 p~ 922
  ‫ديو دولت‬                                                                               ‫‪٩۱‬‬
‫باشد ساء رتگك ‪ .‬چون‬       ‫کفته‌اند » و آن‌کرهی‬        ‫دیو پا ‪ - ۱‬با نانی مجهول وبای فارسی‬
                                                      ‫بالف کشیده » عنکیوت‌را کو‌ند و نگایماهی‌هم‬
 ‫ه شور کنند هر‬ ‫اهنگر‬
                   ‫خشبش‬
                      ‫را خشك کرده در‬                 ‫هت که آنرا انده قوفو و حندقوقی خوالند ‪٩‬‏‬
  ‫شرشه کهدنرجااباشد بشکند وگیاهی همهت‬                       ‫ودیو پای نگیفزتداند باضافةٌ تحتالیآخر ‏‬

                                                     ‫دیو باد ‪ ۱‬با نانی مجهول وبای ابجد‬
                             ‫ِ‬   ‫مدان اندام خار اد‬
                                                     ‫بروزن دبوزاد ؛ بمعنی گردباد است ‪ -‬وبادنندی‬
 ‫دیو خار ‪ ۰ ۱‬با خای شطه دار(‪ )۱‬بر‬                    ‫ویند که هوا را تاريبك سازد ‪ -‬و جنون‬  ‫گز‬
                                                                                           ‫را ل‬
 ‫پرخار؟ وآراسفید‬      ‫وزن پیشکار " درختی است‬                              ‫ودیوانگی را گنفزته‌اند ‪-‬‬
      ‫خار وخفچه گوبند وبعربی عوسج خوانند‪.‬‬            ‫جنهیول و بای ابجد‬
              

=== leaf 380 p~ 923
  ‫‪۳‬‬                                                                                                     ‫ديو دید‬


 ‫‪ = °‬بمعتی دیواسیت است‬       ‫د دوست‬                      ‫ت کنانه از دبواله ومحنون‬              ‫دلو د‬
                                                                                              ‫بد‬
 ‫که آنرا حندقوقی خرانند ‪ .‬کلف وبهق راضماد‬                                                                   ‫باشد ‪.‬‬
                                   ‫آن نافع است ‪.‬‬
                                                        ‫ديو ده = بمهنی دیو دید است که‬
 ‫پ‪۵‬وسیلت = بکررابم و نکون بای‬                                       ‫کنابه از دبواله ومجنون باشد ‪.‬‬
‫ابجد ولام مفتوح بقوقانی زده گ‪.‬یاهی است که‪.‬‬
 ‫آنرا بعریی خنراف کوبند ؛ وبا بای فارسی هم‬
                             ‫‪.‬‬     ‫سظر امده است‬
                                                                                               ‫ثیطان لعین است‬
                                                        ‫خانه‬    ‫صاحب‬   ‫‪۰‬‬   ‫ز دور‬   ‫ورن‬   ‫بر‬    ‫=‬   ‫د نو ر‬
 ‫با انی مجهول و کسر‬         ‫د لو سيك‬
                                                         ‫وسرایرا گونند‪٩‬‏

=== leaf 384 p~ 927
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
                                                          ‫سر

=== leaf 387 p~ 930
   ‫راست‬                                                                                          ‫سوه‬
‫رارقی ه بر وزن عاشقی ‪ ۰‬نوعی از‬                               ‫بکیوزبند‪ ۱‬و‪-‬امر برنگه کردن همهت عنی‬
 ‫انگور است که دانهای آن کوچك میباشد ؛‬                        ‫رمك کن ‪ -‬و خاریشت را دز گفته اند ‪ ,‬و آن‬
 ‫وبعضی کویند نم کتان‌است واز آن روغ نگیر ند؛‬                 ‫جافورست معروف ‪ -‬وبمعنی زلبورسرخ وبز رکه‬
 ‫وبعضی دیگرکویند سوسن‌سفید است؛ ودیگری‬                       ‫و‌کار رایز گوبند وبعربی‬
                                                                                   ‫همآمده‌است‪ -‬وبنا گل‬
           ‫میکوید رازفی زنبق سفید امت ‪. ۴‬‬                    ‫ی‌اند راز درعربی کلاش‬
                                                                                 ‫طیان خوانند‪ -‬وکبفسته‬
 ‫راز نهان خا د کنابه از انات‬                                 ‫وبزر که بنایان باشد‪ -‬وبعضی گویند رازی معرب‬
           ‫است که بتدریج از خاکه بره‌ی‌آبد ‪.‬‬                 ‫رازاست چنانکه بازی معرب باز وتام قربه‌است‬
 ‫راره ‪ = ۴‬بر وزن نازه ‪ .‬بمعنی راز‬
                                                             ‫تزديك بسبزوار‪ -‬ونام پادشاهزاده‌ای هم بوده‌است‬
           

=== leaf 389 p~ 932
                                                                                        ‫‪۲4‬‬
‫خوانند ‪ ۰‬اکر درون وبرا پراز گشنیز کنند‬                 ‫استیثه ‪ = ۲‬بروزن ماستینه ‪ .‬بمعنی‬
 ‫و خشك سازند خوردن قدری از آن کزندکی‬                                     ‫راسترن باشد که حقیقی ‪۳‬‬

‫جالوران زهردار را نافع باشد ‪ .‬کوبند اک رکب‬            ‫اسحت ؟ ب=ضم ثالث و سکون خای‬
                                                                                ‫ر‬
‫باشد بیرون آورند و بریای‬     ‫دهه‬
                               ‫نک‬‫زقتی‬
                                    ‫آنرا بو‬           ‫قطه دار (‪ )۱‬و تای قرشت ‪ .‬سمسوخته باشد‬
‫راست زن بندلد وباو جماع کنند آستن گردد ‪.‬‬
                                                       ‫و آلراروی‌سوخته‌یز کویندومعر آن‌روسختج(‪)۲‬‬
‫و گویندطمامی که زهرداشته باشد همین که‌ببیند‬
‫موهای‌خود راست(‪ )۵‬کند وبفرمادآ بد‪ .‬اگرخون‬
                                                      ‫|‬
                                                                                 ‫است درسم (‪. )۳‬‬
‫او را مبفراصل وخنازیر طلاکنند نافع باشد ‪.‬‬
                                                      ‫= بروزن دامن‪ .‬نام درخت پیل‬    ‫راس"‬
‫راش ه بورزن م
```


## [2026-09-04T23:11:52.830Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\npages=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (385,386):\n    print('=== leaf',i,'p~',i+543,'===')\n    print(pages[i][:2600]);print()\nEOF",
 "description": "BQT leaves 385-386"
}
```


### [2026-09-04T23:11:54.697Z] TOOL RESULT

```
=== leaf 385 p~ 928 ===
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
  ‫‪.» ۹۱‬رك ‪:‬‬    ‫(فر) ‪ ۶‬دزی ج ‪ ۱‬ص‪٤۳4‬‏ ‪ « ۰‬لك ‪ ۲‬ص‬           ‫درخت جاری شود تفر“ = ‪6‬‬
                                                     ‫‪ :‬رانیانج ‪.‬‬   ‫رك‬   ‫‪۴‬‬             ‫‪.‬‬   ‫راطننی‬


        ‫آبستنی دختر انگور بجاست‪.‬‬                ‫‪ ۴‬آببتنی دختر عمران بپسر بود‬
  ‫حرهٌ ‪5۷٩‬‏‬
          ‫بصيهف د‬


=== leaf 386 p~ 929 ===
      ‫==‬                                                                                      ‫راغ‬


‫راد بوی » بابایابجد بر وزن ماه‬                    ‫‪٤‬‏ غم و الذوه‬     ‫بر ورن شان‬        ‫راح‬


                   ‫‪.‬‬   ‫ورناند‬
                            ‫عگود‬    ‫چیو»ت‬
                                        ‫رو‬                                       ‫یند ‪.‬‬
                                                                                     ‫بکاوربرا‬
‫راذهنش ‪ « ۴‬بنتحمیمو کر نون‬                       ‫بروزن شاد » کریم و جوالمرد‬          ‫راك ه‬
‫وسکون شین قرشت »کرم طبع وسخا پیشه را‬             ‫وصاحب‌همت وسخاوت‌را کویند‪٩‬‏ ‪ -‬وبمعنی‌شجاع‬
                                   ‫کونند ‪*.‬‬     ‫و حکیم و دانشمند را نز‬       ‫‪-‬‬   ‫و دلاور هم هت‬

 ‫راز = بر وزن قاز ‪ .‬بمعنی پوشیده‬                 ‫سخن کوی و سخن گزار‬        ‫و دیمهم‬    ‫‪-‬‬   ‫گفته اند‬

 ‫وپنېان‌ونېفته واسرار دل‌باشد‪ - ۴‬ورنگه ولوزرا‬                     ‫و قصه خوان حمآمده است (‪. )۱‬‬

                                                                    ‫(‪ )۱‬جك ‪ - :‬است ‪.‬‬



               ‫‪ ۰.‬قی ‪ :‬اوستا _ ‪itiûra.‬‏ هندی باستان _ ‪tûr‬‏ (خواحان دادن) اسشق ی‬                ‫‪۰‬‬

   ‫ابرست تيخ‌نيزش‪ .‬اپری که فطر او خون‪.‬‬             ‫بحریست دست رادش " بحری که موج او در‬
             ‫تش‬        ‫وراد‬
                          ‫‪۳‬‬                 ‫‪= ۴‬رد(ھم‪.).‬‬               ‫‪ ۵‬معزی لشابوری ‪٩ ۹۳۵‬‏ ‪.‬‬
  ‫)‬     ‫»ی‬‫ور‬
           ‫دابی‬
              ‫‪ 82‬ا(تزوا › ننه‬  ‫‪۲‬تا‪-2‬‬
                                   ‫‪ ۴‬پ‪-‬ھلوی ‪ « 28۲‬تاوادیا ‪٤ ۲ : ۶۹۱‬ء‏ او‬
      ‫که ‪ ۵۹۱‬ساسکریت ‪58۵۲‬‬   ‫« بارتولمه ‪ 6۱۵۱‬آرامیع ‪ ( 8287‬سربالی ‪« ) "82۵۲۵‬ریب‬
  ‫) از‬    ‫(خفیانه‬
                ‫در اوراق مالوی ( بپارتی ) ‪ 86215۷۳‬م‬          ‫ا(تروا» سر » راز) « اسشق ‪۲۰٩‬‏‬
                                                 ‫( قی ‪ :‬اوستا ‪ ,01222-۲‬فارسی ‪:‬‬                ‫چ‬
                                                                                          ‫راز ) ‪٩‬‏‬
                                                      ‫‏‪(Henning , A list of Middle‬‬
                                                 ‫‏‪Persian ..., BSOS, IX, 1,0. 87.):‬‬
                                                              ‫راز نپان خویش جپان کرد شآکار‬
                                                   ‫در ماصب وزارت دستور شپربار ‪.‬‬
                                                   ‫«معزی لیشابوری ‪۹۶۳٩‬‏ ‪.‬‬
                                                  ‫‪010۵۲‬‬    ‫رادیو ‪ -‬از فرانوی‬          ‫‪#‬‬
```


## [2026-09-04T23:12:19.161Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if re.search(r'رد\\s*[:：]|\\bرد\\b.*پهلوان|موبد.*رد',p) and 190<=i<=260:\n        pass\n# just show leaves near 199+offset guesses\nfor i in range(200,215):\n    t=pages[i]\n    if 'رد' in t:\n        head=[l.strip() for l in t.split('\\n') if 'رد' in l][:4]\n        print(i, ' || '.join(h[:120] for h in head))\nEOF",
 "description": "FSF pages near 199"
}
```


### [2026-09-04T23:12:21.194Z] TOOL RESULT

```
leaves 485
200 ‫که بخشایش آرد به ما برمگر‬ || ‫بکار می‌برد‪:‬‬ || ‫تو را هرچ بر چشم سر بگذرد‬ || ‫گرسنه شدی دست به دریا فرو کردی و‬
201 ‫به قیصر سپارد همه یک به یک‬                          ‫از پنج نسخه معتبر و قدیمی که در اساس‬ || ‫ازین پس نوشته فرستیم و چک‬                           ‫این واژه‌نامه قرار دارد‪ .‬این بیت تنها در دو‬ || ‫زردنده خورشید تاتیره خاک‬
202 ‫خردمند مهتر به گشتاسب گفت‬                               ‫کنون چنبری گشت یال یلی‬ || ‫کردند و چندین مردم آنجا بکشتند‪.‬‬                       ‫وان چون چنار قد تو چنبر شد‬ || ‫چنین با و بی بت برهمن مباد‬                          ‫ببست گردن صبرم به ریسمان فراق‬ || ‫فرشیدورد در جنگ با ارجاسپ زخم‬                      ‫کجامر تو رابر سر افسر بود‬
203 ‫همی یاد کرد آن کجا رفته بود‬                          ‫یکی دخمه چون برفرازم؟‬ || ‫پرد‬ || ‫به زیراندر آورد اسب نبرد‬                                     ‫ستودن نداند کس او را چو هست‬ || ‫چخهوبیاشتن کرد باید ستیز؟‬                                     ‫چنو بست بر کوة پیل کوس‬
204 ‫همی تا آز باشد بر جهان چیر‬               ‫نبینی باغبان چون گل بکارد‬ || ‫نگردد جان مردم از گنه سیر‬                   ‫چه مايه غم خورد تاگل برآرد؟‬ || ‫هردو به معنی‪ :‬سخنور» خوش‌سخن»‬               ‫(مرکب از چیره ‪ +‬ی مصدری‪ :‬های آخر‬ || ‫یکی پاکدل مرد چیره زبان‬                                  ‫همه چیرگی با منوچهر بود‬
205 ‫به حقه درون پارسی رقعه‌ای‬                                              ‫پرده‌دان دربان‪:‬‬ || ‫بدادی درم مرد گوهر شمار‬                                   ‫کهن بود و هم حاجب شاه بود‬ || ‫درخت بلا حنظل آورد بار‬                              ‫معاجین و عطر و غیره نهند» (غیات)‪:‬‬
206 ‫کردار موم‬       ‫رگابه‬ || ‫(‪)۶-۱۷۱-۰4‬‬                                   ‫پیوند اوی‬     ‫بیفشاردم سخت‬
207 ‫میانش به حلقه درآورد گرد‬                                  ‫فسرتاد کس نزد خاقان چین‪...‬‬ || ‫تگوفتی خم اندر میانش فسرد‪.‬‬                         ‫‏)‪(AF۶-TFF-O‬‬ || ‫‪«-۳‬جرم دباغت نکرده» (برهان)‪:‬‬                                                     ‫خاکسار‬ || ‫را دستگیر کرده ولی‬       ‫افراسیاب‬    ‫هوم‬            ‫بون» خوار‪:‬‬
208 ‫فرو برد مسمارهای گران‬                           ‫همی در نهان شوی را برشمرد‬ || ‫کهرد اول آهنگری چون نبودست‬                ‫در چند جای شاهنامه واژة خاور دکرنار‬ || ‫تآخدممی و پرنده و چارپایان‪:‬‬                  ‫همه گرد برگرد مالشکرست‬ || ‫خورش زردۀ خایه داداش نخست‬              ‫خور بارگی خار گرخاورست‬
209 ‫ز شهر وز لشکر خحییر ه شدند‬                   ‫همی کرد خیره بدیشان نگاه‬ || ‫‏)‪(VO04-1۲۴-1‬‬                                               ‫وشیروانبه شکل «خبیره» کرد ات‬
210 ‫مصحح لغت فرس بهاین شکل ضبط کرده‬           ‫تیر حدنگ و زین خدنگ به این اعتبار‬ || ‫شاهنامه را خراب کنرده است‪ .‬از داستان‬     ‫(‪۷۵ -۲-۷۶‬‬ || ‫طاعتی مصحح صحاح الفرس نیز به عنوان‬          ‫ردتاجای گردان کجاست‬ || ‫پاورقی نقلکردهاست‪.‬‬         ‫سپر به پیش کشیدم خدنگ قهر تو را‬
211 ‫نجستم همی زین سخن کامو نام‬                                             ‫لغت فرس نقل کرده است‪.‬‬ || ‫نکردم تو را رنجه تندی مساز‪.‬‬                                                                  ‫برهان)‪:‬‬ || ‫*خردک‬              ‫چنان ساخت جای خرام و خورش‬ || ‫جرعه؟‬              ‫کسه تن بسابد از خوردنی پرورش‬
212 ‫خشت و کتاب» (رشیدی)‪« ,‬پهلوی هم‬                      ‫به خرسندی اگزرد خود بشکریم‬ || ‫همه رزمگه شد ک‬                                                ‫ر]ا‪:‬پرده و چادر بزرگ‪:‬‬ || ‫کردن‪.‬‬                                            ‫خروار‬ || ‫(ناصر ‪١۱-۴):‬‏‬                   ‫بانگ زدن‪ ,‬فریادبرآوردن‪ .‬غریدن‪:‬‬
213 ‫ابا خلعت خسروانی و تاج‬                     ‫فرمانبردار آمتاده است (ویس‬     ‫مععنی‬ || ‫ز بهرش بسی خسروی هدیه ساخت‬                                                    ‫افرار کردن‪:‬‬ || ‫در آن حلقه کرده‪ ,‬دست راتاب داده نیزه‬ || ‫به آورد خشت افگند بردو میل‬                        ‫اگر کشته گر خحستةً تير بود‬
214 ‫خورش کرد و پوشش همانجا یله‬                     ‫به معنی سپید ‪+‬سار =سر) امده و در‬ || ‫خله کردن = پاروزدن‬            ‫خشیسار دید اندر آن رودبار‬ || ‫فرو کردن [سوزن‪ .‬خار‪ ]...‬زخ‬ || ‫خسته‪ ,‬زخم برداشته‪ .‬ریش شده‪:‬‬
```


## [2026-09-04T23:12:30.481Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(pages):\n    if 'ردان' in p or 'مغز رد' in p:\n        print('=== leaf',i,'===')\n        for l in p.split('\\n'):\n            if 'ردان' in l or 'رد' == l.strip():\n                print('   ',l.strip()[:200])\nEOF",
 "description": "FSF search radan"
}
```


### [2026-09-04T23:12:33.318Z] TOOL RESULT

```
=== leaf 12 ===
    ‫سپس در بیت نهم «بدوگفت» را [کهفاعل گفت رودابه است] تکراردانسته‌اند و‬
=== leaf 16 ===
    ‫کت رگانی (ویس و رامین‬             ‫از خر‬               ‫بشد آگبردان مازندران‬
=== leaf 37 ===
    ‫در نام جستن به گردان سپرد‬                         ‫همی تافت زو فرشاهنشهی‬
=== leaf 39 ===
    ‫سرگردان‪ ,‬از مرز و بوم حود دور افتاده‪,‬‬
=== leaf 48 ===
    ‫ببرایدینو دانمآیینو فر‬                                            ‫ببستند گردان ایران میان‬
=== leaf 54 ===
    ‫یکی بادپایی گشاده بری‬                                        ‫بگویم بدان کاردان پسوزشم‬
=== leaf 57 ===
    ‫(‪(1-41-1£‬‬                                    ‫ز انگنده مردان نیابند راه‬
=== leaf 64 ===
    ‫که‌ای شاه پیروز جاوید زی‬                  ‫بگرداندش پشت و بگریزند‬
=== leaf 69 ===
    ‫کپههدلووان آامیددر به‌جنگ‬         ‫گرداوژن گردانکن‪ ...‬پهلوی ‪:02۵‬‬
=== leaf 74 ===
    ‫کرت ا‬                                                 ‫بگیرند گردان پس پشت اوی‬
=== leaf 81 ===
    ‫بیامد کتهوید گنزردان برد‬                       ‫می‌گشاید‪ .‬سام نرم می‌شود و می‌گوبد‪:‬‬
=== leaf 94 ===
    ‫چو نامه سوی رادمردان رسید‬
=== leaf 98 ===
    ‫یکی انجمن کردم از بخردان‬                            ‫چه مايه بدو اندرون کشتزار‬
=== leaf 109 ===
    ‫که آید ز گردان بدینکار پیش‬                             ‫سر افراز گردان بسی دیده‌ام‬
=== leaf 110 ===
    ‫بگرداندش پشت و بگریزند‬                            ‫ز دیبای زربفت و چسینی حریر‬
=== leaf 125 ===
    ‫(‪)۴-۷۸۱-۳۴۱۱‬‬                                                         ‫روگردان‪ .‬دلچ رکین متنفر‪:‬‬
=== leaf 127 ===
    ‫شیرویه دزنردانست» دربار؛ شیرویه گوید‪:‬‬                                      ‫ناآشناء غریب‪:‬‬
=== leaf 131 ===
    ‫دستور سلطان محمود برمی‌گر دد‪] .‬‬                   ‫ز نیروی گردان دوال رکیب‬
=== leaf 133 ===
    ‫(‪)۲-۰۱۲۰-۳۱۵‬‬                                  ‫بگردان به هر پاس شب پاسبان‬
=== leaf 138 ===
    ‫که هرکس کهسر بکرشد ز انجمن‬                       ‫[کاوه] خروشید کای پایمردان دیو‬
=== leaf 144 ===
    ‫با راکو با ری ردان‬                                  ‫خود [‪ :‬سلم]و تور بنشست بارایزن‬
    ‫ردان از کین ایوا بانب‬                                               ‫بپردازم ز رسوایی جهان را‪...‬‬
=== leaf 146 ===
    ‫(به واه پرنداور‬      ‫جوهردان‬    ‫‪-۱‬شمشیر‬         ‫به پرسیدن مهتر اندر گرفت‬
=== leaf 152 ===
    ‫هشماهدمانی شد از درد پست‬                        ‫که رستم نگرداند از رخش زین‬
    ‫مرکب از پس ی‬                                                ‫پستکرداندن‬
=== leaf 157 ===
    ‫عقل اگردانکه دل دربندزافشچوننموشست‬
=== leaf 159 ===
    ‫بیارم گزردان هزاران هزار‬
=== leaf 168 ===
    ‫سرو پای گیتی نیابم همی‬                         ‫‪-۱‬روی گردانیدن‪ ,‬انحراف جستن»‬
    ‫چو تابند گردان ازین سو عنان‬        ‫)‪(1-0۴-۰1‬‬
    ‫‪ ...‬بباید یکی شاه بیداربخت‬                    ‫‪-_۲‬چرخاندن» برگرداندن (روی» سر» دل)‬
=== leaf 171 ===
    ‫‪-۱‬سرپیچی کردن‪ .‬روی گرداندن (بر اثر‬                     ‫ز مرغان مر آن را کهبد نیک‌تاز‬
=== leaf 172 ===
    ‫بسرفتند گردان کابلستان‬                                       ‫زگوهر که پرمایه‌تر یافتند‬
=== leaf 175 ===
    ‫(در فهرست ولف تنهابه معنی تیردان‬                  ‫لگدزنست» (صحاح) کشک سیاه باشد و‬
    ‫تیردان‪ .‬شدر‬
=== leaf 184 ===
    ‫بگردان عنان تیز و لختی ممان‬
=== leaf 187 ===
    ‫به مردان بخندد همی روز رزم‬        ‫)‪۵41-۴۵-۶‬‬
=== leaf 191 ===
    ‫کمان‌دان تیردان ترکش (جهانگیری ‪-‬‬                     ‫(‪)۱-۷۶-۲۴۸۲‬‬
=== leaf 198 ===
    ‫نگه کرد تا جای گردان کجاست‬                       ‫دگر دارد بهشت آبادناهید‬
=== leaf 208 ===
    ‫در توصیف رخش رستم‪:‬‬                      ‫گرفتند گرداندرش چارسوی‬
=== leaf 210 ===
    ‫طاعتی مصحح صحاح الفرس نیز به عنوان‬          ‫ردتاجای گردان کجاست‬
=== leaf 217 ===
    ‫وردان آن انسجمن‬
=== leaf 218 ===
    ‫زردان کوچ و بلوچ‬
    ‫مردانی که‬        ‫وتان‬
=== leaf 220 ===
    ‫‪-۲‬مرکب از خوش ‪+‬مش [ا‪:‬ندیشه ]‪:‬‬                      ‫کههردانه‌ای قطرء آب بود‬
=== leaf 222 ===
    ‫خیره پرتاب‬         ‫‪-۲‬شگفت‌زده سرگردان‪ ,‬حیران» بهت‌زده‪:‬‬
=== leaf 228 ===
    ‫ز گردان که رستم بداند همی‬
=== leaf 233 ===
    ‫تخوار نامو نشان گردان ایران را می‌پرسد‪.‬‬             ‫بریزد بر ان مرز بار درخت‬
=== leaf 235 ===
    ‫‪61‬‬   ‫(ویس» ‪۶-۱‬‬           ‫بهگرداندرش تیغ‌ها در نشاخت‪.‬‬
=== leaf 239 ===
    ‫(‪٩‬شیرویه‏ ‪)۵۹۱‬‬                                              ‫چنین گفت با بخردان شهریار‬
    ‫(بخشش داد اینزد‪ .‬خسواست خحدا‬                                    ‫مگردان به ما بر دژم روزگار‬
=== leaf 240 ===
    ‫چه فرزانگان و چه مردان گرد‬                                    ‫(ویس ‪:)۹۹۲-۰۷‬‬
    ‫در نام جستن به گردان سپرد‬                                                ‫داستان‪:‬‬   ‫مخفف‬
=== leaf 246 ===
    ‫تو مردان جنگی کجا دیده‌ای‬
=== leaf 247 ===
    ‫افراسیاب باردان و موبدان انجمن می‌کند و از‬
=== leaf 250 ===
    ‫(‪-‬پرویز ‪)۸۷۴‬‬                                               ‫نه خورشید شمشیر گردان بدید‬
=== leaf 251 ===
    ‫که پیروز بودند گردان ما‬
=== leaf 263 ===
    ‫رخانش چگولنار و لب ناردان‬
    ‫ز سیمین برش رسته دو ناردان‬
    ‫(به وارْه ناردان نگاه کنید)‪.‬‬
=== leaf 264 ===
    ‫چون خانة کردان ×‬
=== leaf 265 ===
    ‫فریدون ز ضحاک گیتی بشست‬                            ‫دل بخردان داشت و مغز ردان‬
=== leaf 292 ===
    ‫بسازید سام و برون شد به در‬                     ‫ازین بیش مردان وزین بیش ساز‬
=== leaf 293 ===
    ‫بگردان زمن دیو را دستگاه‬
=== leaf 295 ===
    ‫(‪)۳-۸۲۰-۷۸۳‬‬                                                ‫بهگردان سپهر اندر آری سرم‬
=== leaf 300 ===
    ‫سر‬   ‫برفتند گردان پراندوه‬                               ‫اوی‪‎‬‬     ‫جید‬
=== leaf 302 ===
    ‫چو ماچرخ گردان فراوان سرشت‪...‬‬
=== leaf 304 ===
    ‫زردان ایشان فراوان نماند‬
=== leaf 307 ===
    ‫همه برکشیدند گردان سلیح‬                    ‫دورة ساسانیان مانده و پاره‌ای کتیبه‌ها هم در‬
=== leaf 314 ===
    ‫نشست و نگه کرد مردان سور‬                             ‫(‪)۱-۷۳۱-۰۲‬‬
=== leaf 321 ===
    ‫تیردان» ترکش‪ .‬کیش‪:‬‬            ‫خرد را بدینگونه بسفریفتی‬
=== leaf 322 ===
    ‫شمارنده‬    ‫فردوسی گاه ترکش رانیز که تیردانست‬
=== leaf 324 ===
    ‫گر ایدونک بامنتوپیمان کنی‬                                             ‫شمع گردان سپهر‬
    ‫(‪)۳-۱۸-۷۴۲۱‬‬                                                ‫همی بود تاشمع گردان سپهر‬
=== leaf 337 ===
    ‫تو را باد جاوید تخت ردان‬                ‫اولی نزدیک است به لهج فرس هخامنشی‬
=== leaf 339 ===
    ‫به انگشت چون چرخ گردان بگاشت‬                                                ‫بکاری یا چیزی‬
=== leaf 351 ===
    ‫درس‬                      ‫جنگاورند‬       ‫شیرمردان‬       ‫کا‬
=== leaf 353 ===
    ‫نمی‌دانسته آنرابه «تورانیان» برگردانده‬           ‫به‌معنی آموزگار‪( »...‬تاریخ اجتماعی ایران‬
=== leaf 357 ===
    ‫روان یابد از ک‌البدتان رها‬                           ‫وزو چون ناردانه خون جکیده‬
=== leaf 363 ===
    ‫بسبردی وکرم آن پسردانختی‬                             ‫در نسخه قاهره و نسخه دوم لنینگراد بجای‬
=== leaf 365 ===
    ‫ورزیدن]‪ :‬برزگر» کشاورز‪:‬‬           ‫به مردی مگردان سر خویش کش‬
=== leaf 367 ===
    ‫همه گیل مردان چو شیر یله‬             ‫(‪)۲-۰۲-۸۵۳‬‬
=== leaf 369 ===
    ‫کندو خوانند» (صحاح)‬            ‫ردان و بزرگان با آفرین‬
=== leaf 370 ===
    ‫(ویس ‪:)۴۸۳-۰۲-‬‬                      ‫همان ارزن و پسته و ناردان‬
    ‫بیارد یکی موبدی کاردان‬
=== leaf 372 ===
    ‫وردان به جایست نوز‬ ‫نشد پست گ‬                                 ‫سیه مار کو را سرآید به کوب‬
=== leaf 373 ===
    ‫به هستی ‪.‬یردان نیوشان‌ترم‬                                  ‫دخهد‪:‬‬
=== leaf 377 ===
    ‫‪(-۲‬مصدر متعدی)‪ :‬برگرداندن‪:‬‬
=== leaf 378 ===
    ‫گاودم‬         ‫به انگشت چون چرخ گردان بگاشت‬
=== leaf 383 ===
    ‫ردان ایران نماییم راه‬
=== leaf 385 ===
    ‫(ویس ‪:)۴۶۴-۴۲۲‬‬                   ‫مخفف گردان گردونء چرخ» فلک‪:‬‬
    ‫(‪(۶-۵۲۲-411‬‬                                                 ‫‪ ...‬نیاساید این چرخ گردان ز گرد‬
    ‫جهان از بدی‌ها بشویم به رای‬                                       ‫گردان (بازبر اول)‬
    ‫(‪)۱-۶۲-۵‬‬                                               ‫کزویست گردون گردان به پای‬
=== leaf 387 ===
    ‫اگزرد [مخفف گردان قید حالت] ‪+‬گرد‬                    ‫درگهی‪ ,‬خانگی‪ ,‬اهلی می‌کنم‪ .‬و تاحلقطعی‬
    ‫[مخفف گردان ]‪ :‬گردان گردان» چرخان‬                 ‫مسئله این تعبیر درست‌تر از انچه که در‬
=== leaf 388 ===
    ‫(مولوی‪ ,‬دستور همایونفرخ ‪)۲۷۵‬‬                                ‫گرد گردان (با زبر هر دوگاف پارسی)‬
    ‫غلط غلطان (قید مرکب حالت)‪:‬‬           ‫اگزرد [مخفف گردان‪ .‬صفت فاعلی از‬
    ‫گوی شو می‌گرد بر پهلوی صدق‬                  ‫گردان‌گردان‪.‬‬      ‫گکردیدن] ‪+‬گردان‪:‬‬
    ‫(مولوی» دستور همایونفرخ ‪)۲۷۵‬‬                                  ‫دگر آنک این گرد گردان سپهر‬
    ‫برخی برآنند که«گردگردان» مرکب است‬                    ‫همی نو نمایدت هر روز چهر‬
    ‫اگزرد [با زیر اول] ‪+‬گردان‪.‬‬          ‫(‪)۴-۲۰۳-۵۱‬‬
=== leaf 392 ===
    ‫دلیران گوردان خنجر گزار‬                            ‫و رسوم سفارت آنست که سخن بر حدت‬
    ‫سپه داشت گردان خنجر گزار‬                               ‫سرت‬
=== leaf 399 ===
    ‫به زیرش بگسترد گستردنی‬                  ‫رابه «گست» برگردانده در گمذتانرده‌ام‪.‬‬
=== leaf 402 ===
    ‫بگشتند با‬                        ‫‪-۱‬روی گردانیدن‪ ,‬سرپیچی کردن‪:‬‬
=== leaf 417 ===
    ‫پرستنده و پاکدل بخردان‬
=== leaf 418 ===
    ‫(منوچهری ‪:)۱۳‬‬           ‫بی‌آزار گردان ‪ 0‬مرقد گنت‬
=== leaf 419 ===
    ‫آزادمردان به مس مار دارد‬                 ‫کے‬       ‫(‪(۲-۷-4۱‬‬
=== leaf 424 ===
    ‫مهست و سرافراز و گیرنده شهر‬                                       ‫خداوند کیوان و گردان سپهر‬
=== leaf 425 ===
    ‫(‪)۱-۶۸۴۱۱۱‬‬                                                     ‫بسبردند میتین و مردان کار‬
=== leaf 430 ===
    ‫ناردان‬                                         ‫‪۳۳۷‬‬
    ‫«ناردان» در‬                                          ‫قلعه شدند»‬
    ‫در مصراع اول به‌معتی ناردانه است و در‬                ‫گاهنیزبه جای ناچیز و چیز نیست و‬
    ‫کگفهتی زمین شد سبهر روان‬                                                     ‫ناردان‬
    ‫)‪(A-FA-Y‬‬                                                        ‫رخانش چگولنار و لب ناردان‬
    ‫بستان چو ناردان گ‬
    ‫نارون را به معنی درخت انار می‌آورد‪:‬‬              ‫چلونار و ناردان‬
    ‫وان نارها بین ده‌رده بر نا‬                        ‫رخانش چگلونار و لب ناردان‬
    ‫و لف در این بیت شاهنامه («در داستان‬                  ‫ز سیمین برش رسته دو ناردان‬
=== leaf 431 ===
    ‫«ناردان» [دباال] نوشته شده آن را درست‬             ‫در همین بیت در مصراع دوم بجای ناردان‬
    ‫نخوانده‌اند و بجای ناردان «ناروان» چاپ‬                      ‫«ناروان» [با واو ] به چاپ زده‌اند‪.‬‬
    ‫«ناردان» ضبط است‪.‬‬           ‫ورداود در کستاب خود بسه‌نام‬
    ‫(‪)۶-۶۳۳-۰۶۲‬‬                                        ‫«چو دل قدح بخندند ز شراب ناردانی‬
=== leaf 441 ===
    ‫(‪)۱-۰۷۱-۰۳۵‬‬                                        ‫خرس گردان» و زن در وقت خرس گشت‬
=== leaf 442 ===
    ‫‏(‪ ٩‬پرویز ‪)۶۳۱۱‬‬                                                 ‫یکی تیز گردان و دیگر بهجای‬
    ‫بسخردان و مسوبدان از زال جیستان‬                                 ‫دو اغات بر آورداز زر پاک‬
=== leaf 445 ===
    ‫ز گردان که رستم بداند همی‬                                                     ‫نمکت سود‬
=== leaf 446 ===
    ‫نوازش‌کننده و نسوازندة سازء در‬                 ‫(سیاست‌نامه ‪۳٩):‬‏ امیران عرب وکردان و‬
=== leaf 448 ===
    ‫چنین بودتابودگردان سپهر‬                                 ‫برین بارةگامزن بر نشین‬
    ‫(‪)۵-۲۲-۵۳۲‬‬                                  ‫نشد پست و گردان به جایست نوز‬
=== leaf 450 ===
    ‫به نزدیک شهر دلیران رسید‬                               ‫اباموبدان و ردان تسیز گشت‬
=== leaf 454 ===
    ‫ز مردان و ز گنج و نیروی دست‬               ‫(بادداشت‌های گات‌ها ‪ .)۱۷۲‬پهلوی‬
=== leaf 461 ===
    ‫ز پروازش آورد گردان فرود‬                   ‫(‪)۱-۵۳-۸۲‬‬
=== leaf 462 ===
    ‫‪-۱‬از دیباچۀ داستان سیاوش‪:‬‬                       ‫برون رفت با ویژه گردان خویش‬
=== leaf 464 ===
    ‫تن این دو فریشته مرکب گردانید و‬                ‫گهی مگیسارید و گهچنگ ساخت‬
=== leaf 466 ===
    ‫به خوبی ز ره باز گردانمش‬                               ‫روغن درست کنند (غیاث)‪:‬‬
=== leaf 467 ===
    ‫هم ردان] کهیکی از پنج جزء اوستاست‬                  ‫که تا بگسلاند میانش ز هم‬
=== leaf 471 ===
    ‫فرو مانده اسپان ز مردان جنگ‬                      ‫ببخشید یکسر همه بر سپاه‬
=== leaf 476 ===
    ‫(‪)۳۰۱۹۱-۰۳۹۲‬‬                                      ‫ببينيم تادست گردان سپهر‬
=== leaf 478 ===
    ‫دوست باید که باشد‪ .‬و مردان ان مرد و‬
=== leaf 479 ===
    ‫اسم فاعل مرخم از ياختن‪ :‬یازنده در‬                  ‫بگردانم این رنج و درد و گزند‬
```


## [2026-09-04T23:14:30.460Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\npages=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(pages[265][:2500])\nEOF",
 "description": "FSF leaf 265 rad entry"
}
```


### [2026-09-04T23:14:32.626Z] TOOL RESULT

```
                                                 ‫‪۹۳‬‬                                            ‫رد‬




                    ‫رده (بازبر اول و زیر دوم)‬         ‫این واژه فدرهنگ‌ها نیست‪ .‬در‬
                                      ‫صف‪:‬‬          ‫فرهنگ‌های جهانگیری و رشیدی و برهان‬
              ‫ز لشگرگه پهلوان تا دو ميل‬            ‫رخیدن بهمعنی «نفس زدن از برداشتن بار‬
‫کشیده دو رویه رده ژنده پیل‬                                    ‫گران و مشقت» آمده ولی بی‌گواه‪.‬‬
‫(‪)۱-۹۱۱-۱۶۶‬‬                                             ‫گومان نمی‌رود کهرخته از رخیدن باشد‪.‬‬
               ‫رده بربکسشیدند ایرانیان‬                ‫ووللرس در فرهنگ خود معنی رخته رااز‬
‫چنانچون بودساز جنگ کیان‬                           ‫فرهنگ پارسی ‪-‬ترکی شعوری چنین نقل‬
‫(‪)۲-۰۲-۸۱۲‬‬                                        ‫نام را از‬    ‫نظمی‬
                                                                  ‫ریت‬
                                                                    ‫ین ب‬
                                                                       ‫مای‬
                                                                         ‫می‌کند‪« .‬خسته و‬
                   ‫(رودکی ‪-‬نفیسی ‪:)۹۸۱‬‬
                                                  ‫همان فرهنگ گواه می‌آورد‪« :‬دل و دیده شد از‬
 ‫مرابسود و فرو ريخت هرچ دندان بود‬                 ‫آلامبسته× تنزار و زبونش بود رخته» اما‬
‫نبود دندان لابل چراغ تابان بود‬
                                                  ‫فرهنگ شعوری اعتباری نندامردی‌وتوان به‬
 ‫سپید سیم رده بود در و مرجان بود‬                  ‫آن اعتماد داشت‪( .‬دربار؛ فرهنگ شعوری به‬
‫ستارة سحری بود قطره باران بود‬                         ‫نوشته دهخدا در صفحهٌ شصت مقدمة برهان‬
                                ‫رز(با زبر اول)‬
                                                        ‫قاطعبهتصحیح دکتر معیننگاهکنید)‪.‬‬
                                    ‫‪-۱‬باغ‪.‬‬
                                                      ‫دشرهلغنتامة عبدالقادر رخته «بیمار و‬
                                 ‫‪-۲‬انگور‪:‬‬
                                                      ‫مریض» معناشده و همین بیت شاهنامه‬
               ‫چو ببرید رستم تن شاخ گز‬                ‫گواه آورده شده است‪ .‬و لف نیز در‬
‫بیامد ز دریابه ایوان و رز‬
                                                      ‫فهرست خود همین معنا را [بیمار] از‬
 ‫(‪)۶-۸۹۲-۷۰۳۱‬‬
                                    ‫دا‬
                                     ‫س=‬‫را‪۵‬‬
                                         ‫رس‬           ‫لشغهتن
```


## [2026-09-04T23:14:43.198Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\npages=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nt=pages[265]\ni=t.find('مغز ردان')\nprint(t[max(0,i-1800):i+900])\nEOF",
 "description": "FSF rad entry full"
}
```


### [2026-09-04T23:14:45.068Z] TOOL RESULT

```
                                            ‫مریض» معناشده و همین بیت شاهنامه‬
               ‫چو ببرید رستم تن شاخ گز‬                ‫گواه آورده شده است‪ .‬و لف نیز در‬
‫بیامد ز دریابه ایوان و رز‬
                                                      ‫فهرست خود همین معنا را [بیمار] از‬
 ‫(‪)۶-۸۹۲-۷۰۳۱‬‬
                                    ‫دا‬
                                     ‫س=‬‫را‪۵‬‬
                                         ‫رس‬           ‫لشغهتنامه نقلکرده است‪ .‬معلوم نیست‬
‫از رسد [رسیدن] ‪+‬الف آروزمندی و دعا‪:‬‬               ‫عبدالقادر این معنا را ازفرهنگی گرفته و یا‬
      ‫چنین گفت کاین بد به دشمن رساد‬                                    ‫بگهمان خود نوشته است‪.‬‬

‫که بر من رسید از بد بدنژاد‬                                                         ‫رد (بازبراول)‬
 ‫(‪۶-۵۹۲-۷۴۲۱۱‬‬                                         ‫از ريشه اوستابی رتو ‪ 02۲‬پهلوی رت ‪1۵۲‬‬

                           ‫رست (باپیش اول)‬            ‫مینوی (پورداود‪.‬‬     ‫ای‬
                                                                           ‫وو‬‫شزرگ‬
                                                                                ‫یی ب‬
                                                                                   ‫پمعن‬
                                                                                      ‫به‬
          ‫ادوه فرزند‪ .‬تخم و ترکه‪:‬‬
                                ‫ززه‬
                                  ‫‪-۱‬‬                  ‫ویسپرد ص ‪٩۱).‬‏ در گات‌ها به معنی داور‬

 ‫منوچهر از زناشویی زال بارودابه‪ ,‬دختر مهراب‬           ‫(پورداود یادداشت‌های گات‌ها ‪« .)۱۲‬دانا‬
     ‫کابلی از نژاد ضحاک بیمناک است و گوید‪:‬‬                          ‫و بخرد» (لغت فرس‪ :‬صحاح)‪:‬‬
             ‫فریدون ز ضحاک گیتی بشست‬                            ‫دل بخردان داشت و مغز ردان‬

 ‫بترسم کهآیداز آن تخم رست‬                               ‫دان‬
                                                          ‫بهش‬
                                                            ‫وو‬‫مان‬
                                                                ‫دکوتف یل‬
 ‫(‪)۱-۲۹۱-۹۶۸‬‬                                          ‫(‪)۲۹۷-۱۵۵-۱‬‬
```


## [2026-09-04T23:15:05.063Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\npages=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (263,264,265,266,267):\n    head=pages[i][:200].replace('\\n',' ')\n    print(i,'|',head[:160])\nEOF",
 "description": "FSF page headers"
}
```


### [2026-09-04T23:15:06.764Z] TOOL RESULT

```
263 |                                                ‫‪۰۹۳‬‬                                                 ‫رخ‬      ‫همی گفت و لب راپر ازخنده داشت‬                
264 | ‫رخته؟‬    ‫بهغایتکنند‪ .‬عماره گفت‪ :‬بینیت همی بینم‬                ‫دو رخساره چون لاله اندر سمن‬  ‫هآرماسوتهاره به شیراز‬                     ‫چون خانة کردان
265 |                                                  ‫‪۹۳‬‬                                            ‫رد‬                         ‫رده (بازبر اول و زیر دوم)‬     
266 | ‫رطل‬                                          ‫‪۳۹‬‬             ‫چرا چون پلنگان به چنگال تیز‬                                    ‫‪-۲‬سرزمین خاک‪:‬‬       ‫یز
267 |                                              ‫‪۳۹۴‬‬                                            ‫رعا‬                                ‫رمه‪:‬‬     ‫مخفف‬
```


## [2026-09-04T23:15:28.328Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,os\ndef show(f,pats,ctx=(200,320),n=2):\n    if not os.path.exists(f): print('MISS',f); return\n    d=open(f,encoding='utf-8',errors='replace').read()\n    for w in pats:\n        c=0\n        for m in re.finditer(re.escape(w),d):\n            i=m.start(); print('###',os.path.basename(f),repr(w),'::',d[max(0,i-ctx[0]):i+ctx[1]].replace('\\n',' ')); print()\n            c+=1\n            if c>=n: break\nprint('======= HRN')\nshow('HRN.txt',['rad ','rā ,','čirā','tschirā','čarā'],n=2)\nprint('======= HUB')\nshow('HUB.txt',['rād','čirā','rad,'],n=2)\nprint('======= TTS araba')\nshow('incoming/TTS/TTS_vambery1878_uoft_djvu.txt',['araba','arba'],n=3)\nEOF",
 "description": "Horn, Hübschmann, Vámbéry lookups"
}
```


### [2026-09-04T23:15:31.089Z] TOOL RESULT

```
======= HRN
### HRN.txt 'rad ' :: r keine Izäfe steht (vergl. pus) ; sonst kommt sie neupersiseh nur in den Patet's vor. 287. pidräm 'schön, fröhlich' (Sahn. III, 1803, V. 372). aw. *2)aiti.raman' ; vergl. np. räm (No. (504). 288. pedrad 'Heil, Lebewohl*. phlv. pa i]^t) + drüt (Nöldeke, Kam. 65). Vergl. np. durüd (No. 555). 289. pedJd 'sichtbar. phlv. pa du {^\y\rr^^\ ps), Nöldeke, Karn. 40; also aw. Sipa.dHi-, 290. peölruften 'empfangen, annehmen', jüd.-pers. J nenne, Praes. peöJr-em, peSlr, ap. *patit/ -f- i/^grufj-; phlv. patgriffan bezw. « pati

### HRN.txt 'rad ' :: Objekts dienende Partikel, rdl * wegen', beräl^ ez her dl. ap. rad' in -radiy Vegen* ; phlv. ra%^ aj rai (Gemme, ZDMG. 44, 676 No. 141). aty. lar^ lara (beim Dativ); kurd. ärai *für (H.- Sch.) ; oss. rad ^Ordnung, Reihe (209) (?). Aus der ursprünglichen Bedeutung *für, wegen, was anlangt* erklärt sich auch das Vorkommen von rä vor dem Nominativ. In Vis und Rämln ist dieser Gebrauch nicht selten, z. B. gleich im ersten Verse, ferner S. 16 Vers 7 b v. u., 73 Vers 2 u. ö. Vergl. auch Salemann, Litbl. f. or. Phil. II, 

======= HUB
======= TTS araba
### TTS_vambery1878_uoft_djvu.txt 'araba' :: =  aufsteigen,   Jüz  —  »«e«j5r«>  =  Aussenseite,  Antlitz,   8ÜS  —  manglai  —  ütiTn.    WOETEEGISTER.*    «c  1.   achlarmak  7.   aci  (Bruder)  2().   acik  1.   aimak  1.   addk  4.   «dnt  (araba)  27.   adasmak  \   azasmdk  I   adim  27.   «g'a  5.   agh,  aa  6.   a(//ür  8.   agil  5.   o^i!>,  aj>,  ai'j«  f.   aglamak  141.   aijir»,  agrimak  9.   ajr«  9.   oj  (luna)  5.   aj«  1.   nya/;  27.   ajamak,  ajanc  3.   ajartvmk  31.   «Ja«  1.   ajdinlik  179.    aJiTJ/-  14.   <yV,  ttjift  26.   a

### TTS_vambery1878_uoft_djvu.txt 'arba' ::  hervorgehoben  werden,  dass  tef  nicht  dem  Persischen  entlehnt  ist,  vielmehr  das  umgekehrte  das  Wahrscheinlichere  ist.   Tev,  tir,  unrein,  migeschickt,  umgekehrt.   uig.   <e/*s  =  barbarisch,  schlecht,  ungeschickt.   duv.  fj'r/s=Unrath.   osm.  tercs,  teree==schlecht,  unrein,  ungeschlacht;  #ej'5= verkehrt,  schlecht,  ungerathen  (hiervon  /ers-cÄawe  =  Arsenal,  d.h.  das  Haus  der  Unreinen,  weil  in  demselben  anfänglich  nur  Un-  gläubige verwendet  wurden).   Tcrs  =  verkehrt
```


## [2026-09-04T23:15:42.146Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read()\ni=d.find(\"Objekts  dienende  Partikel\")\nif i<0: i=d.find(\"Objekts dienende Partikel\")\nprint(d[max(0,i-1500):i+900])\nEOF",
 "description": "Horn ra entry context"
}
```


### [2026-09-04T23:15:44.191Z] TOOL RESULT

```
en, paz. diu, dlmk,
arm. LW. den.
Allgemein entlehnt*'^).
598. dev 'Dämon, Teufel', dcväne Verrückt*, n^NDH (Jer.
29, 26.) 3).
aw. daeva- 'Dämon'; phlv. dev; ai. devd- 'Gott'.
599. dlvär 'Mauer, Wand'.
ap. ^deghavära- (vergl. gr. th/o^-, osk. felhuss).
Nöldeke (mündliche Mitteilung), unter der Voraus-
setzung, dass die np. Grundform '^devür lautete, was
die Zusammenstellung mit dev (8ähn. I, 24 Vers 86)
wahrscheinlich macht.
kurd. LW. dwär; wa;^. LW. dival^ sar. delvül 'Mauer,
Wand, Umwallung.
*) Der Majhül vokal ist nicht mehr in der Aussprache erhalten.
') College Jensen hat din sogar im Verdachte, babylonisch zu
sein. Er äussert sich in folgender WeiBe über diese Ansicht:
y»Üe(i)nim in der elamitisohen Version = framänä, de(i)Him-
dattira ibid. = framätaram, beides in der Inschr. von Naqs-i-Rustani.
iJeCOnhn unmöglich = daina, muss vielmehr = babyl. dinim sein,
welches in der babyl. Version der Achämonideninschriften vorkommt.
iHiiii = 'Gesetz, Recht* könnte sehr wohl persisches daina übersetzen,
das im Altpersischen nicht vorhanden. Ich halte es daher für möglich
(falls nichts Entscheidendes dagegen einzuwenden), dass daina durcli
elamitischcs den- mit assyr.-babyl. dlmi zu verknüpfen ist."
Vergl. Geldner's Etymologie von aw. dapiä- unter No. 413.
Jensen nimmt als Grundbedeutung *Recht, Gesetz' an, Geldner da-
gegen *Glaube, Religion*, wie im Neup.
^) Ursprünglich natürlich 'teuflisch , dämonisch*, vergl. Sahn. 1,
)5? Vers 408, 413.- 134 —
R
600. -m, zur Bezeichnung des Objekts dienende Partikel,
rdl * wegen', beräl^ ez her dl.
ap. rad' in -radiy Vegen* ; phlv. ra%^ aj rai (Gemme,
ZDMG. 44, 676 No. 141).
aty. lar^ lara (beim Dativ); kurd. ärai *für (H.-
Sch.) ; oss. rad ^Ordnung, Reihe (209) (?).
Aus der ursprünglichen Bedeutung *für, wegen, was
anlangt* erklärt sich auch das Vorkommen von rä
vor dem Nominativ. In Vis und Rämln ist dieser
Gebrauch nicht selten, z. B. gleich im ersten Verse,
ferner S. 16 Vers 7 b v. u., 73 Vers 2 u. ö. Vergl.
auch Salemann, Litbl. f. or. Phil. II, 84.
Einzelne Redensarten siehe noch bei Salemann-
Shukovski, Neup. Gramm. § 13 b Anm. 1, sowie
die syntaktische Bemerkung bei Rückert, ZDMG.
8, 258, 264.
601. räd 'freigebig.
aw. vergl. aräiti-^); ai. rati- Villig zu geben'; phlv.
rat (auch Titel, vergl. Hörn, Mitteilungen, Heft IV,
27), ratth.
602. räz geheim, verborgen'.
aw. razah' (vd. 8, 97); phlv. raz^ vergl. Qaovav^
Chron
```


## [2026-09-04T23:15:55.290Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS && python3 - <<'EOF'\nd=open('TTS_vambery1878_uoft_djvu.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=d.find('27.')\n# find entry '27' heading pattern\nfor m in re.finditer(r'\\n\\s*27\\.\\s', d):\n    print('---',m.start())\n    print(d[m.start():m.start()+900])\n    print()\n    break\nEOF",
 "description": "Vambery entry 27"
}
```


### [2026-09-04T23:15:57.097Z] TOOL RESULT

```
--- 95266


27. 

At,  €fj,  CIZ,  CtT,  schreiten,  Schritt,  Fuss,  Stütze. 

jak.  «<a7i;  =  Bein,  Fuss,  Stütze;  rt^27?a  =  schreiten ,  einen  Schritt 
machen. 

uig.  afa/i;  =  Fuss;  ataJcun  =  &ui  den  Füssen. 

alt.    ajak  =  ¥uss,  Stütze;  «i/a  =  schreiten ;  a^iam  =  Schritt. 

cag.  fyaÄ;  =  Fuss;  adaJc  ara&a  =  Gehwagen ,  Rollwagen,  mittelst 
dessen  die  Kinder  gehen  lernen;  a^m  =  Schritt. 

CUV.  o<?a  =  schreiten ;  of  =  gehen;  ora  =  Fuss;  o>'aZaw  =  sich  auf 
die  Füsse  stellen. 

kk.    a^alc  =  Fuss. 

Atak,  ajah  steht  zu  atamak  (schreiten)  in  einem  solchen 
Verhältniss  wie  elih  (Hand)  zu  almaJc  (nehmen);  JculaJc  (Ohr) 
zu  Jcul  (hören)  u.  s.  w.  Einen  fernem  Beleg  liefert  noch 
das  jaJc  ata  =  seiend  (?  stehend) ,  ungefähr  gleich  dem  ro- 
manischen stare— stehen  und  sein,  nicht  minder  aber  auch 
zum  gege
```


## [2026-09-04T23:16:04.539Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('KNT.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer(r'r[aâáàäü]diy', d):\n    i=m.start()\n    seg=d[max(0,i-260):i+360].replace('\\n',' ')\n    if 'postp' in seg or 'account' in seg or 'sake' in seg or 'Av.' in seg:\n        print('::',seg); print()\nEOF",
 "description": "Kent lexicon radiy entry"
}
```


### [2026-09-04T23:16:06.230Z] TOOL RESULT

```
:: ransfer to -o- stem ending, and retention of the -ant- of the suffix as in Av. gsm. fSuyanté ‘cattle-raising’, despite Av. hato = Skt. sat-ds, pIE gsm. *sntés (ог *sytds) ‘bemg’ with strong grade in пета, *sent-s. ПІ. Асе. багдат, gen. Barda, gen. х$ара, loc. rüdiy, -padiy in ni-padiy, vasiy (but cf. Lex. s.v.) “have the regular pIE endings of their cases: acc. ~; gen. -es or -o$; loe. -i, without added -à because the forms function as preposition, phrasal adverb, . adverb respectively. Stem, because of the final short vowel ($86.11), but is саат, ace. nt. of an -a- stem. ? Bv. Gr. $290 takes as stem XSaydrSah- b

:: asmád, with the regular pronominal ending of the abl., as in Av. ahmáf, Skt. asmát, to stem a-; whence OP *ava^má?, remade to avand after inst. атата. The remaining forms show no new peculiarities. The adverbs from this stem are атайй, avadā, ava-pard, avahya-radiy, pasdva (from *pasd ava). 8201. THE IwTERROGATIVE-INDEFINITE PIE *g**o- /*q*i- occurs only sparingly іп ОР. Nsm. kaš- ciy ‘anybody’ is *q*o-s, Skt. kas, Av. kas-, + enci. -cly; asn. сі&-сїу ‘anything’ is *g%i-d, Gk. т, Lt. quid, + епо. -ciy: both with Median sandhi-de- velopment ($105). Enclitic -ciy is pIE *q*id, Skt. cid, Av. -cit, Lt. quid, etc. See

:: f the genitive after the adjectives sug- gests that this is a dative use rather than a true genitive use (cf. §309)? К. With prepositions, the mixed use with -ройу (see E); DB 3.32 pasa mand ‘behind me’; with anu- ‘according to’, in DNb 16, 18; with following rüdiy, to express agent, in DNb 9, 10f; with encli- tic -rddiy, in avahyarddiy ‘on account of this’. $251. Tue Locarive Case appears іп OP in the following uses: A. Expressing place where, without a preposi- tion, as in DB 1.34f pasdva drauga dahyauvā vasiy abava щй Parsaty ша Madaty ша aniyãwā dah- yusued ‘afterwards the Lie waxed great in the country, both

:: s prefix in nouns. : para, postp. w. асе.; prefix w. verbs. E pariy, prep. w. aec.; pref. w. verbs; used as root of derivative noun. pasă, prep. w. aec. and gen. fra-, pref. w. verbs and nouns, and in phrasal ad- verb. yàlà, prep. w. loc. уйй à, prep. w. abl. radiy, postp. w. gen. vi-, pref. w. verbs and nouns. hacà, prep. w. abl., loc., instr., adv. hadā, prep. w. instr. The inseparable prefixes are the following: a- an-, the common negative prefix. u- (= *u-) ‘well’, duš- ll’. ha- ham-, equal in meaning to Gk. civ and Lt. com- as prefixes. The uses as prepositions (and postpositions) will be discussed in the fo

:: ave replaced the s* was wrongly substituted for the a, and this falsely cor- rected orthography was inscribed on the rock). ‘ava- demonst. adj. and pron. ‘that’ (5260.11, $264): Av. ava-, Skt. gen. du. avós, oCS орй; see also avd, араба, avadà, avapard, avahyarüdiy, pasiva. Decl., $200. avam asm. DB 1.21, 22, 31, 40, 49, 57, 76, 80, 84, 88; 2.4, 4f, 12, 17, 20, 25, 30, 31, 35, 40f, 46, 50, 51, 55, 61, 84, 87, 94, 97; 3.4, 7, 12, 14, 14f, 17, 27, 38, 45f, 47f, 50, 56f, 58, 62, 67, 82, 85, 89; 4.38, 66 bis; 5.6°, 27; DNa 2; DSe 2; DSf 2°; DSt 2°; рле, 1; DE 3; XPa 2; XPb 3; XPe 2; XPd 2; XPf 2, 28; XPh 2, 37; XE 4;

:: RV 1.116.283), to Av. avah- ‘aid’, Skt. dvas- (Jn. JAOS 27.190, MB Gr. §209, Bv. Gr. $193). pali- + avahya- ‘ask for help’: patiydvahyaty ($140.11) Ist sg. imf. mid. DB 1.55. avahyarddty phrasal adv. (§191.1V) ‘for this reason’: avahyd ($185) gen. of !ava-, + rüdiy ‘on account of’, q.v. For phrasing, cf. Gk. rovrov évexa, robvexa, Lt. huius ret causd; JAOS 35.322-9. DB 1.6f, 51; 4.47, 62; DBa 9f. asa- sb. ‘horse’ (590, $143.IIT): Med. aspa-, Av. aspa-, Skt. déva-, Lt. equos, pIE *ekyos. See also Asagarta-, asabüra-, aspa-. asam asm. (col- lective, $255) DB 1.87. Asagarta- sb. ‘Sagartia’, a northwestern prov- ince

:: rious uses, often affixed to direct object for elarity; also OCS radi, postpos. with gen., “оп account of’; 10е, sgoof räd- (5188111), io root in Ski. radh- ‘effect; complete! (not to 206 "rad-, pIE *rej-, with Hz. ApI 280). DB 4.54; DNb 9, 10f; also in avahyarádiy, q.v. ram- vb. ‘be at peace’, with prefix d, in Arüjyüramna-, q.v. rasa- present stem of vb., see ar-. rüsla- adj. ‘straight, right, true’, with nt. as Sb.; ріс. of ?^rad-: Av. réSta-, Turfan РЫ. тай ‘true’, Lt. réctus ‘straight’, pIE *rékto- (593, §93.- n1-2, $106, $122, 5126, $24211). Cf. arštā-. таӣз- iam asf. DNa 59. rdstam usn. DNb 11; asn. DNb 7.
```


## [2026-09-04T23:16:23.040Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%AF",
 "prompt": "Give the Persian entries for رد verbatim, especially any entry meaning \"chief, master, sage\" with an etymology from Middle Persian rad / Avestan ratu. Also list other Persian رد entries (Arabic radd etc.).</prompt>\n"
}
```


## [2026-09-04T23:16:24.394Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%A7",
 "prompt": "Give the Persian entry for را (the postposition/particle) verbatim: etymology (Middle Persian, Old Persian rādiy), and usage notes.</prompt>\n"
}
```


### [2026-09-04T23:16:31.969Z] TOOL RESULT

```
# Persian entries for رد

Based on the Wiktionary content provided, here are the Persian entries:

## Etymology 1
**Noun: رد (rad)**
- "(archaic) sage (wise person)"
- "an important person in Zoroastrianism"
- References "راد" (râd) for further information

## Etymology 2
**Noun: رد (rad)**
- "track"
- "trace"
- "footprint"
- Derived term: رد پا (radd-e pâ)

## Etymology 3
**Noun: رد (radd)**
- "rejection"
- Borrowed from Arabic رَدّ (radd)
- Derived term: رد کردن (radd kardan)

The page does not provide explicit Middle Persian or Avestan etymology for the "sage/chief" sense. The archaic meaning appears in Etymology 1 but lacks the detailed etymological chain you requested.
```


### [2026-09-04T23:16:34.284Z] TOOL RESULT

```
# Persian Entry for را

## Etymology
From Middle Persian _lʾd_ (rāy), from Old Persian _𐎼𐎠𐎭_ (ra-a-da, rād, "cause, reason, because of, due to"), ultimately from Proto-Indo-European _*h₂er-_ ("to fit together").

## Usage Notes

The particle serves multiple functions:

**Direct Object Marker:** "Used to mark certain noun phrases as the direct object. Since it is obligatory for all definite direct objects, it is often called the 'definite object marker'..."

**Contraction:** In literary Persian, _من را_ (man râ, "me") typically contracts to _مرا_ (ma-râ). Colloquial Iranian forms use _من رو_ (man ro) or _منو_ (man-o).

**Semantic Factors:** The particle applies to indefinite objects based on context—particularly when actions are unusual, objects are human rather than inanimate, or with "intense" verbs like _کشتن_ (koštan, "to kill").

**Tehrani Pronunciation:** In colloquial speech, _رو_ (ro) typically triggers word-final _ـه_ to be pronounced as _ـَه_ (\-a) rather than _ـِه_ (\-e).
```


## [2026-09-04T23:16:40.852Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D8%B1%D8%A7",
 "prompt": "Give the Persian entries for چرا verbatim: etymology of the interrogative \"why\" (چه + را), and the other homograph (grazing).</prompt>\n"
}
```


## [2026-09-04T23:16:41.453Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/arithmetic",
 "prompt": "Give the etymology of arithmetic and logarithm verbatim, including the PIE root cited.</prompt>\n"
}
```


### [2026-09-04T23:16:47.732Z] TOOL RESULT

```
# Persian Entries for چرا

## Etymology 1: Interrogative "Why"

The adverb meaning "why" derives from Middle Persian, ultimately from Proto-Iranian. By surface analysis, it combines "چه" (čé, "what") + "رای" (râ, "reason"). The word appears in various Persian dialects with slight pronunciation variations.

## Etymology 3: Grazing/Pasturing

The noun چرا (čarâ) meaning "pasturing" or "grazing" originates from the present stem of چریدن (čaridan, "to graze, pasture") plus the nominal suffix ـا (-â).

**Key derived terms** include:
- چراگاه (čarâ-gâh, "pasture, grassland")
- چرا کردن (čarâ kardan, "to graze, pasture")

These represent two distinct homographic entries with completely different etymological origins.
```


### [2026-09-04T23:16:47.854Z] TOOL RESULT

```
# Etymology Requested

Based on the provided webpage content:

## Arithmetic

**Etymology:** The word comes from "mid-13c., _arsmetike_, from Old French _arsmetique_ (12c.), from Latin _arithmetica_, from Greek _arithmetikē (tekhnē)_" meaning "(the) counting (art)."

**PIE Root:** The Greek _arithmos_ ("number, counting, amount") derives from "PIE _\*erei-dhmo-_, suffixed variant form of root _\*re-_ 'to reason, count'."

## Logarithm

Unfortunately, the webpage provided contains **no information about logarithm's etymology**. The content focuses exclusively on the word "arithmetic" and related terms. To provide the etymology and PIE root for "logarithm," a different source document would be needed.
```


## [2026-09-04T23:16:55.974Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/harmony",
 "prompt": "Give the etymology of harmony verbatim, including Greek harmos/harmonia and the PIE root cited.</prompt>\n"
}
```


## [2026-09-04T23:16:56.828Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/army",
 "prompt": "Give the etymology of army verbatim, including Latin arma and the PIE root cited. Also anything on alarm and arms.</parameter>\n"
}
```


### [2026-09-04T23:17:01.966Z] TOOL RESULT

```
# Etymology of Harmony

According to the Online Etymology Dictionary, harmony originates from late 14c. English, derived from "Old French _harmonie_, _armonie_" and ultimately from "Latin _harmonia_, from Greek _harmonia_."

The Greek term _harmonia_ meant "agreement, concord of sounds" and literally signified "means of joining," relating to ship-planks and joints. It connects to the Greek word _harmos_, which denoted "fastenings of a door; joint, shoulder."

The ultimate source traces to a Proto-Indo-European root: "PIE _ar(ə)-smo-_, suffixed form of root *ar-" meaning "to fit together."

The modern musical sense—"combinations of notes to form chords"—emerged in the 16c., while the figurative meaning of "agreement of feeling, concord" appeared by late 14c.
```


### [2026-09-04T23:17:04.192Z] TOOL RESULT

```
# Etymology of Army

**Army** originates from late 14th century Old French *armee* ("armed troop, armed expedition"), derived from Medieval Latin *armata* ("armed force"). This traces back to Latin *armatus* ("armed, equipped"), the past participle of *armare* ("to arm").

The root term is Latin *arma*, defined as "tools, arms" and ultimately connected to the PIE root **\*ar(ə)mo-**, a suffixed form of **\*ar-** meaning "to fit together." The concept suggests "that which is fitted together."

Originally referring to expeditions by sea or land, the term's restriction to land forces occurred by the late 18th century. Its figurative meaning of "host, multitude" appeared around 1500, while "body of men trained and equipped for war" emerged in the 1550s.

**Arms** (weapons) comes separately but relatedly from Old French *armes* (plural), also from Latin *arma*. The heraldic meaning in "coat of arms" dates to the early 14th century.

The page does not provide specific etymological information for **alarm**.
```


## [2026-09-04T23:17:09.096Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/order",
 "prompt": "Give the etymology of order verbatim, including Latin ordo \"row of threads in a loom\" and the PIE root cited.</parameter>\n"
}
```


## [2026-09-04T23:17:10.099Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/read",
 "prompt": "Give the etymology of read verbatim: Old English rædan, Proto-Germanic *redan, and the PIE root cited.</parameter>\n"
}
```


### [2026-09-04T23:17:14.538Z] TOOL RESULT

```
# Etymology of Order

The word "order" originates from Old French *ordre*, stemming from Latin *ordinem* (nominative *ordo*). According to the source, Latin *ordo* originally meant "a row of threads in a loom," and more broadly referred to "row, line, rank; series, pattern, arrangement, routine."

The ultimate origin traces to Proto-Italic *\*ordn-*, meaning "row, order." Etymologists propose this derives from the Proto-Indo-European root *\*ar-*, meaning "to fit together," though the source acknowledges this origin remains uncertain.

The Latin root also connects to *ordiri*, meaning "to begin to weave," which appears in related words like "primordial."
```


### [2026-09-04T23:17:16.632Z] TOOL RESULT

```
# Etymology of "Read"

Based on the Online Etymology Dictionary entry, here's the verbatim etymological chain:

**Old English:** "rædan, gerædan (West Saxon), redan, geredan (Anglian)"

**Proto-Germanic:** "*redan"

**PIE Root:** "*re-" meaning "to reason, count"

The entry explains that the Old English forms meant "to advise, counsel, persuade; discuss, deliberate; rule, guide; arrange, equip; forebode; to read (observe and apprehend the meaning of something written)." The sense-transfer to "interpret and understand the meaning of written symbols" is noted as "unique to English and (perhaps under Old English influence) Old Norse raða," distinguishing it from most other languages that use words rooted in concepts like "gather up" for "read."
```


## [2026-09-04T23:17:26.803Z] TOOL CALL #70: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%A7%D8%A8%D9%87\" \\\n \"https://en.wiktionary.org/wiki/araba\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%DA%86%D8%B1%D8%A7\" \\\n \"https://www.etymonline.com/word/arithmetic\" \\\n \"https://www.etymonline.com/word/harmony\" \\\n \"https://www.etymonline.com/word/army\" \\\n \"https://www.etymonline.com/word/order\" \\\n \"https://www.etymonline.com/word/read\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 62, root Ar/Are (PIE *h2er-), verification of nodes 1-20\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources used"
}
```


### [2026-09-04T23:17:33.454Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a2a15d9c88ae752f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d9f99415246a8d20.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d0aeae5024190578.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/713778ea5383a983.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8e8811afbef3261f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77192b6674ecd434.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/01326eac7cfcce41.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dc0f7910efaccced.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/44f46336881ac9da.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9e7573c7814bdcff.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fb963b4b7d56245c.txt
```


## [2026-09-04T23:17:41.926Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,os\ndef g(f,pat,n=1,ctx=(150,400)):\n    if not os.path.exists(f): print('MISS',f); return\n    d=open(f,encoding='utf-8',errors='replace').read()\n    c=0\n    for m in re.finditer(pat,d):\n        i=m.start(); print('###',os.path.basename(f),pat,'::',d[max(0,i-ctx[0]):i+ctx[1]].replace('\\n',' ')); print()\n        c+=1\n        if c>=n: break\n    if c==0: print('--- SILENT',os.path.basename(f),pat)\nprint(\"=== KLN harmony/army/art/read/arithmetic\")\ng('KLN_1966.txt',r'harmony,\\s*n')\ng('KLN_1966.txt',r'arithmetic,\\s*n')\ng('KLN_1966.txt',r'\\barmy,\\s*n')\nEOF",
 "description": "Klein lookups"
}
```


### [2026-09-04T23:17:44.877Z] TOOL RESULT

```
=== KLN harmony/army/art/read/arithmetic
### KLN_1966.txt harmony,\s*n :: .,  an  instrument  for  measuring the  harmonic  relations  of  musical  sounds.  — F.  harmonomdtre.  See  harmony  and  meter, ‘poetical  rhythm’. harmony,  n.  —  ME.  harmonie,  fr.  F.  harmonie,  fr. L.  harmonia,  fr.  Gk.  appovta,  ‘a  fitting  together, joining,  proportion,  concord,  agreement,  music¬ al  harmony’,  which  is  rel.  to  appo^eiv,  ‘to  fit together,  adapt,  accomodate’,  appo?,  ‘a  join¬ ing’,  fr.  I.-E.  base  *ar-,  ‘to  join’.  See  arm,  ‘the upper  limb’,  and  cp.  words  there  referred  to. Cp.  also  H

### KLN_1966.txt arithmetic,\s*n ::  of  niccolite  (mineral.)  — Named  after  montagne  d'Ar  in  the  dept.  Basses Pyrenees,  in  France.  For  the  ending  see  subst. suff.  -ite. arithmetic,  n.  —  ME.  arsmetike,  fr.  OF.  aris- metique,  fr.  L.  arithmetica,  fr.  Gk.  dpiffpnrjxixr] (scil.  styyr),  'the  art  of  counting’,  fr.  apiU- jietv,  ‘to  number,  count,  reckon’,  fr.  dpi-Ofiop, ‘number’,  fr.  I.-E.  base  *rf-,  ‘to  count,  number’, whence  also  Gk.  v()-pi-xo4,  ‘numberless’,  OE., OHG.  rim,  ‘number’,  Olr.  rim,  ‘number’,  do- rimu,  ‘I  count,

### KLN_1966.txt \barmy,\s*n :: tively.  —  A  blend  of OF.  armoierie,  ‘coat  of  arms’,  and  OF.  almarie, armarie,  ‘a  place  where  arms  are  kept’.  See armor  and  ambry. army,  n.  —  F.  armee,  fr.  L.  armata,  fem.  pp.  of armare,  ‘to  furnish  with  weapons’.  See  armada and  -y  (representing  F.  -ee). Derivative:  armi-ed,  adj. Amebia,  n.,  a  genus  of  plants  of  the  borage family  (bot.) — Arab,  arnabtya *,  name  of  a  plant, lit.  ‘hare  plant’,  fr.  drnab,  ‘hare’,  which  is  rel. to  Heb.  arnebheth,  Arm.  arnabhtd,  Syr.  ar- nlbhA,  Ug
```


## [2026-09-04T23:18:13.991Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,os\ndef g(f,pat,n=1,ctx=(120,420)):\n    if not os.path.exists(f): print('MISS',f); return\n    d=open(f,encoding='utf-8',errors='replace').read()\n    c=0\n    for m in re.finditer(pat,d):\n        i=m.start(); print('###',os.path.basename(f),'/',pat,'::',d[max(0,i-ctx[0]):i+ctx[1]].replace('\\n',' ')); print()\n        c+=1\n        if c>=n: break\n    if c==0: print('--- SILENT',os.path.basename(f),pat)\ng('KLN_1966.txt',r'\\bart,\\s*n\\.\\s*—')\ng('KLN_1966.txt',r'\\bartist,\\s*n')\ng('KLN_1966.txt',r'\\bread,\\s*(tr\\.|v)')\ng('KLN_1966.txt',r'\\barm,\\s*n\\.,\\s*the\\s*upper')\ng('SKT.txt',r'READ,')\ng('LAT.txt',r'ordo,\\s*-inis')\ng('LEW_1910.txt',r'ordo')\nEOF",
 "description": "Klein/Skeat/Latin dictionaries"
}
```


### [2026-09-04T23:18:16.126Z] TOOL RESULT

```
### KLN_1966.txt / \bart,\s*n\.\s*— :: o burn’.  See  ardent. arsonium,  n.,  the  radical  AsH4  ( chem .)  —  ModL., compounded  of  arsenic  and  ammonium. art,  n.  —  OF.  (=  F.),  fr.  L.  artem,  acc.  of  ars, ‘skill,  handicraft,  trade,  occupation,  art',  which is  rel.  to  L.  artus,  ‘joint’,  and  cogn.  with  OI. rtih,  ‘manner,  mode’,  Gk.  apxi,  ‘just’,  fipxiop, ‘complete,  perfect  of  its  kind,  suitable;  even (said  of  a  number),  ap-rf^eiv,  ‘to  prepare’, apxuEtv,  apruvsiv,  ‘to  arrange,  prepare,  make ready’,  Lith.  arti,  ‘near’,  MHG

### KLN_1966.txt / \bartist,\s*n :: pp.  of  artire,  ‘to  instruct in  arts’,  fr.  ars,  gen.  artis,  ‘art’.  See  art.  For  the ending  cp.  partisan. artist,  n.  —  F.  artiste,  fr.  It.  artista,  which  is formed  fr.  L.  ars  gen.  artis,  ‘art’.  See  art  and  -ist. artiste,  n.  —  F.  See  prec.  word, artistic,  adj.  —  F.  artistique,  fr.  artiste.  See  prec. word  and  -ic. Derivative:  artistic-al-Iy,  adv. artistry,  n.  —  Coined  by  Browning  fr.  artist  and suff.  -ry. Arum,  n.,  a  genus  of  plants;  (not  cap.)  any  plant of  this  genu

### KLN_1966.txt / \bread,\s*(tr\.|v) ::  and  n.,  reaction- ari-ness,  n.,  reaction-ar-ism,  n.,  reaction-ar-ist, n.,  reaction-ism,  n.,  reaction-ist,  n. read,  tr.  and  intr.  v.  —  ME.  reden,  fr.  OE.  rsedan, ‘to  advise,  counsel,  discuss,  deliberate,  rule, guess,  interpret,  read’  (whence  OE.  rS-d,  ‘advise, counsel’),  rel.  to  OS.  rddan,  ON.  rada,  Swed. iouo  - 1307 rdda,  OFris.  reda,  Du.  raden,  OHG.  ratan, MHG.  raten,  ‘to  advise,  counsel’,  G.  raten,  ‘to advise,  counsel,  guess’,  erraten,  ‘to  guess’, Goth,  -redan  (e.g.  in  ga

### KLN_1966.txt / \barm,\s*n\.,\s*the\s*upper :: y  (Scot.)  —  OF.,  fr.  L. *arrhula,  dimin.  of  arrha,  ‘pledge’.  See  arrha and  cp.  words  there  referred  to. arm,  n.,  the  upper  limb.  —  ME.,  fr.  OE.  earm, arm,  rel.  to  OS.,  Dan.,  Swed.,  MDu.,  Du., MHG.,  G.  arm,  ON.  armr ,  OFris.  erm,  OHG. arm,  aram,  Goth,  arms,  ‘arm’,  and  cogn.  with OI.  irmah,  Avestic  arlma-,  ‘arm’,  Arm.  armukn, ‘elbow’,  Osset,  arm,  ‘palm  of  the  hand’,  Gk. appio;,  ‘a  joint’,  L.  armus,  ‘shoulder’,  OSlav. ramo,  OPruss.  irmo,  ‘arm’.  All  these  words  de¬ ri

--- SILENT SKT.txt READ,
--- SILENT LAT.txt ordo,\s*-inis
### LEW_1910.txt / ordo :: os Il 774 otddoc I 818, IT 599 otoua IT 73, 228 otopuor II 228 otovayy IT 691 OTOVOELC, OTOVOS IT 691 otogévvvpt IT 590 ordovopt IT 590, 607 oteapoc, otedBpwv IT 601 oteayydadn II 601, 605 otoayyahifw II 601 oteayyadcw IT 601, 605 oteayydc, oteay- yevouat II 605 otoayé IT 601 oteatia, otoatela IT 590 oteatoc II 590 oteePAdc II 601 otoeyyic Il 670 otoevyoua IT 605 oteégocs (dor.) IT 589, 670 otenryic IT 590, 602 otenvoc II 602 otenvilw II 602 otelyhocg II 603 otoiyé ,,Reihe, Zeile*‘ IT 604 otelyé ,,ein Nacht- vogel IT 603, 606 Griechis
```


## [2026-09-04T23:18:25.837Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,os\ndef g(f,pat,n=2,ctx=(120,450)):\n    if not os.path.exists(f): print('MISS',f); return\n    d=open(f,encoding='utf-8',errors='replace').read()\n    c=0\n    for m in re.finditer(pat,d):\n        i=m.start(); print('###',os.path.basename(f),'/',pat,'::',d[max(0,i-ctx[0]):i+ctx[1]].replace('\\n',' ')); print()\n        c+=1\n        if c>=n: break\n    if c==0: print('--- SILENT',os.path.basename(f),pat)\ng('LAT.txt',r'ordior')\ng('LAT.txt',r'reor,\\s')\ng('LEW_1910.txt',r'ars,\\s*artis')\nEOF",
 "description": "Ernout-Meillet ordior/reor"
}
```


### [2026-09-04T23:18:28.213Z] TOOL RESULT

```
### LAT.txt / ordior :: a : poires aures A 1 '^poque ou l'on fauche 1 'orge; hordiarium aes, quod pro hordeo equiti Romano dabatur, P.F.91,10; hordior, -aris "etre gonfle par un exces d'orge" (Pelag.). Cf.v.h.a .gersta "orge" et hom.xpL, gr.xpL 0 i] (de *ghr° zdh -1 ), alb. driQ, driQe "orge". Le -d- latin est ambigu; le germanique a *-t- ou *-d- et le grec - 0 - issu de *-dh~. - Arm. gari "orge" a une forme encore plus differente. hdria, -ae f.(horeia,oria): barque de p&cheur. Diminutif horiola. Rare et artihalque (Plaute).'Origine inconnne. horior et hortor (horitor et horto, arch.), -

### LAT.txt / ordior :: par testament apros la mort de leur maitre"; d'oii Orci¬ nianus (Mart. ). fitymologie inconnue. Sur orcib&ta, v. b~sta. ordior, -Iris, orsus sum ( orditus sum Sid., Vulg.), -Iri; ourdir [une trame], commencer a tisser; puis par extension, "commencer, entre- prendre"; en particulier "commencer a parier". Le sens de "commencer" a du se d^velopper par un rapprochement de orior et de ordior. Des confusions ont eu lieu entre les deux verbes; cf. aborior, abortus, adortus, s.u. orior et la glose ortus est: ingressus est CGL IV 37«, qui se rapporte plutot k orsus. Ancien

### LAT.txt / reor,\s :: stimare. Par suite "faire cas de"; puis par affaibl.i sseraent de sens, "juger, penser" (comme arbitror, censeo, -puto, reor, tous verbes qui avaient aussi a 1'origine un sens technique, concret et fort). On rapport avec aes a ete senti par les anciens; cf.P,F., 33,1, aestimata poena ab antiquis ab aere dicta est, cui cam aestimauerunt aere, ouem decussis, bouem centussis, hoc est iecem uel centum assilws. - Ancden, usuel. M.L., 346. Les derives de aestimo n'appellent pas de remarque, sauf aestima¬ bilis, creation de Ciceron pour rendre le tene stolcien grec (xl-i

### LAT.txt / reor,\s ::  qui est different pour le sens, ou got. smarna "axupaXov" qui ne rend pas compte du d. mereo, -es, -ul, -Itum, -ere; mereor, -eris, -itus sum, -eri: recevoir comme part ou comme prix, e.g. Cic. Verr. II 4,135 quid ar¬ bitramini Reginos... merere ueIle ut ab is marmorea Venus illa auferatur ?, et la n. d^m. Thomas ad Z.; se faire payer; gagner [un salaire], merere (-rl) stipendia "gagner sa solde", expression de la 1. mili¬ taire, d'ou, absolument, merere (-rl) "servir a 1'armee", deja dans Varr. ap. Non.344,40, qui in exercitu donati essent et equo publico merere

--- SILENT LEW_1910.txt ars,\s*artis
```


## [2026-09-04T23:18:29.341Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nd=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nfor w in ['ارابه','رَد','هارمونی','آرتیست']:\n    for m in list(re.finditer(re.escape(w),d))[:2]:\n        i=m.start(); print('###',w,'::',d[max(0,i-250):i+350].replace('\\n',' ')); print()\nd2=open('ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nfor w in ['ARABE','RAD','RA ','ARABA']:\n    for m in list(re.finditer(re.escape(w),d2))[:2]:\n        i=m.start(); print('=== idx',w,'::',d2[max(0,i-120):i+200].replace('\\n',' '))\nEOF",
 "description": "Aryanpur lookups"
}
```


### [2026-09-04T23:18:31.523Z] TOOL RESULT

```
### ارابه :: ۸1/1724) اگر حوزه‌ی گسترش یکه زبان زیاد شود» گویش‌های فرعی آن هر یک تبدیل به زبان جداگانه‌ای می‌شوند (همانطور که مثلاً لاتین تبدیل شد به فرانمه و اسپانیایی و غیره). ولی چون هند و اروپایی‌ها در اصل از طریق شکار و دامداری و شبانی زیست می‌کردند و دارای ارابه و اسب پودند» تحرکك آنها از کشاورزان روستانشین بیشتر بود و در ناحیه‌ی وسیع‌تری کوج می‌کردند. بدین دلیل» فرض بر این است که گهواره هند و اروپایی‌ها وسیع تر از حد معمول بود و شامل سرزمین‌های شمال دریای سیاه و دریای خزر می‌شد. همین خوی کوچگری و تحرکك (به علاوه‌ی مجهز بودن به اسب و ارابه و سلاح‌ها و ترفندهای رزمی پیشرفته و دارا بودن خصلت رزم آوری) 

### ارابه :: کشاورزان روستانشین بیشتر بود و در ناحیه‌ی وسیع‌تری کوج می‌کردند. بدین دلیل» فرض بر این است که گهواره هند و اروپایی‌ها وسیع تر از حد معمول بود و شامل سرزمین‌های شمال دریای سیاه و دریای خزر می‌شد. همین خوی کوچگری و تحرکك (به علاوه‌ی مجهز بودن به اسب و ارابه و سلاح‌ها و ترفندهای رزمی پیشرفته و دارا بودن خصلت رزم آوری) آنها را قادر کرد که طی موج‌های متوالی در ظرف حدود دو هزار سال اروپا و آسیای صغیر و فلات ایران و هندوستان را زیر مهمیز خود درآوردند. طی این کوچ‌های مرکز گریزانه (107۸710075/ ب273877817170۸3) هندوار وپایی‌ها. زبان خود را در نواحی تسخیر شده رواج دادند. ولی در هر ناحیه» زبان مردم بومی (

=== idx RAD :: ) 51 yLah OPES VY 9 VY (2S): abi olny UGNIS -(LITHUANIAN) gly) leadloal tage Aa "GAT YL oda ool GU olay 24h adem RATAN ARADH, -RADH —«(AVESTAN) pl 3\ RATEN H(GERMAN) aT ARASTAN (PAHLAVI) 5 shy RADAN, (OLD ENGLISH) oS gS! RADHNOTI, — (SANSKRIT) cy Suse REDAN, RED RAHYATI, RADH- esa x READ HENGLISH) 1S) PERI LATIN) oa (T
=== idx RAD :: ah OPES VY 9 VY (2S): abi olny UGNIS -(LITHUANIAN) gly) leadloal tage Aa "GAT YL oda ool GU olay 24h adem RATAN ARADH, -RADH —«(AVESTAN) pl 3\ RATEN H(GERMAN) aT ARASTAN (PAHLAVI) 5 shy RADAN, (OLD ENGLISH) oS gS! RADHNOTI, — (SANSKRIT) cy Suse REDAN, RED RAHYATI, RADH- esa x READ HENGLISH) 1S) PERI LATIN) oa (TIL)RADE
=== idx RA  ::  lala Ad galy 2 ale dow cand cle by cs ews GA) pg) NATRIX 2gdV) Cath &S pte tose GELS A 39 13h 505)3 (Sup Jud cond INATARA io. ill (NADRE 653 £ NAEDDRE: 34S .,Sil (NATHIR 45° (POKORNY, 767 :4 ©2831 ¢ NADR 24S gah! ash agrg tptlen gla) 32 (Cu! “NETR oT ah aslyee sets, S)o5ly oul ds “Gly, MAR 2g3,5 b igo) Col ype ct edly
=== idx RA  :: slyee sets, S)o5ly oul ds “Gly, MAR 2g3,5 b igo) Col ype ct edly onl lal s oo Blobs 22 Se “(VA ginko «ght olay 4 CAF MIARA 64 SL MAIRYA ; gle MAR SMaedly cal eaten gl BHU oles fl y0 qetlen gdb Sash cpl crglis gph cle cal Saw PS dled shyt gla gh 5) wegen y a gh 9 gle ghd ye SNL ga SHYT Geta begber a5ly GAs 3 Oy Cael J J
```


## [2026-09-04T23:18:40.953Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nd=open('ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\ni=d.find('ARADH, -RADH')\nseg=d[:i]\ntags=re.findall(r'\\[pdf page (\\d+)\\]',seg)\nprint('index pdf page:',tags[-1] if tags else '?')\nprint(d[max(0,i-1400):i+700])\nEOF",
 "description": "Locate ARY index page"
}
```


### [2026-09-04T23:18:42.588Z] TOOL RESULT

```
index pdf page: 51
 APUS (OLD PERSIAN) gal go,
AB, AP (PAHLAVI) 6 shy,
REFERENCES eh ‘AY, DjYRAV KURDISH) 3,5
POKORNY: . 51-52 Ae, APA (SANSKRIT) 2 Sie
MACKENZIE: (WATER) 139 APIA GREEK) gli
BUCK: (WATER) 34-35 AMNIS LATIN) 3
MALLORY 129 EAV APRENCH) si
1 igbG ob, UPE A(LITHUANIAN) gigs
ro sfaseos al cai UPE ALATVIAN) (3) is)
_ ATER ATARSH —(AVESTAN) gus)
‘REFERENCES breathy ATUR, ATAXSH (PAHLAVI) by
POKORNY, ar) AGIR (KURDISH) 52,5
DELAMARRE: (BEU) 179 ATHARVAN, — (SANSKRIT) © Site
MACKENZIE: (FIRE) 114 EDHOS, HUTASH u<o5
BUCK: n AIREM ARMENIAN) gs,\
AMINDAROV: (BIRE) 247 AITHOS GREEK) li
Ir-tF iebG oly ATER _— ALATINY a3 “a
FO-PF Mes eal cid EIT HOLD FRISIAN) (75 523
AITH OLD IRISH) S43 p
detlooy
oF AS SHA Oly al ee
a tole tad 3 dle ool ee
wth A ws (ARDENT ¢ ARID <) ARDERE 2 oj} VATER ys isojly lt -¥
re |
[pdf page 51]
» UGNUS * (LATVIAN) (33) 93) ATHRAVAN, ADAR, :(AVESTAN) gl!
ZJARR ALBANIAN) gidT ATUR, ATHRA-
AGNIS _ ABITTITE) cox ATER {OLD PERSIAN) jheuly
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
BARNHART: (READ) 891 RADIT (SLOVAK) f\gLel
| MACKENZIE: (ADORN) 101 IMMRADIM (OLD IRISH) 45 545)
| BUCK: 1285 AMRAUD (WELSH) «$5
ONIONS: (READ) 743
SKEAT: (READ) 502
tr sbi oby
lethal
sagas iy 5 ydal
```


## [2026-09-04T23:18:53.609Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nd=open('ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nfor w in ['RATU','HARMOS','ARTHRON','ARITHMOS','ARMA','RADIY']:\n    for m in list(re.finditer(w,d))[:2]:\n        i=m.start()\n        seg=d[:i]; tags=re.findall(r'\\[pdf page (\\d+)\\]',seg)\n        print('###',w,'pdfpage~',tags[-1] if tags else '?')\n        print(d[max(0,i-700):i+500])\n        print()\nEOF",
 "description": "ARY index for ratu/harmos"
}
```


### [2026-09-04T23:18:55.437Z] TOOL RESULT

```
### RATU pdfpage~ 117
C) S38
BRALIS (LATVIAN) (9) is) (OLD SCANDINAVIAN) 455-2)
BRATI (OLD PRUSSIAN) S53. BRODHIR
BRATHAIR (OLD IRISH) 545 6) 2! BROTHIR (OLD NORSE) oS x29
BRAWD (WELSH) 65 BROTHAR (OLD SAXON) iS gi -S
BREUR ABRETON) 3.2 BOTHER — (OLD FRISIAN) eS 623
BRATHAIR GAELIC) SIE (OLD HIGH GERMAN) 4S gil

BRUODAR

‘REFERENCES chan BRUDER (GERMAN) galt
poKoR, SOSOSC*~<CS*~*~<‘“CS:*«sa BROTHOR,(OLD ENGLISH) oS 3S!
BARNHART (BAOTHER) 120 BROTHER ENGLISH) ,-3&3\
DELAMARRE (FRERE) 38 BRODER DANISH) Sjlail>
MACKENZIE: (BROTHER) 105 BRODER SWEDISH) Sy
BUCK: 107-108 BROR H(NORWEGIAN) «533
ONIONS: (BROTHER) 121 BRODER, BROEDER (DUTCH) sala
AMINDAROV: (BROTHER) 194 (OLD CHURCH SLAVIC) oS 535+!
rer sebG oly BRATRU, BRATU

PALK :(TOKHARIAN B) B 5,63 BRAZAITI, BRAZA, (AVESTAN)  pkms!
BHRAJATEM, (SANSKRIT) < Suite BARAZA

BIRIAHA, BHARGAS BRAZAITI (OLD RERSIAN) dibs .go3\

PHLEGO GREEK) gb y BRAZIDAN, BRAZ — (PAHLAVI) 15 shy

PULGO LATIN) 53 PALK (TOKHARIAN A) A $3
[pdf page 118]
i,
U8 1 Cosh aS ek elo
BLESK (CZECH) So, BAfRHTS GOTHIC) 6
BRESK (SLOVENIAN) gy hal (OLD SCANDINAVIAN) S,5the\
BREKSHA, —-(LITHUANIAN) .gi 3 BJARTR, BLIK BLIK
BLIZGU _ BUARTR (OLD NORSE) AS p3
BREKSHA, (LATVIAN) (3) gy BERHT, — «(OLD

### RATU pdfpage~ 234
e
WI SoS iV Ib5 22 59 cel
bh
[pdf page 234]
yo | See
eR teenage |
R&KE (NORWEGIAN) $335 (PAHLAVI) 5 shay
OLD CHURCH SLACIC) 25 5 3%! KARCANG, KARZANG
RAKU KARKATA (SANSKRIT) ny Sibe
RAK (POLISH) iglong! KHCHAPAR ARMENIAN) gs)
RAKO(VINA) (CZECH) Soy (GREEK) gly
PAK (SLOVAK) \ glel XARKINOS, KARKINOS
CANCER ALATIN) 5
‘REFERENCES both, CANCER, CANCRE — (FRENCH) a1 3
POKORNY. SSS™~wS*~*«S SPANISH) libel
BARNHART: (CANCER) 139 CANGREJO, CANCER,
‘MACKENZIE: AITALIAN) pie)
(CRAB) 109, (CANCER) 106 CANCRO, GRANCHIO
ONIONS: (CANCER) 140 CANCER (RUMANIAN) ley)
SKEAT: (CANCER) 88 (PORTUGUESE) Js 4
vYA . sab wb, CTARANGUEIO, CANCER
seatlaal
238 Lb" edly ctl ghastly Shdks IPA?
HERD OLD FRISIAN) AS 523 XRATUSH, XRATU :(AVESTAN) pito3\
HART :(OLD HIGH GERMAN) yf gldT XRAT, XVART, XRAD:(PAHLAV) 6 3, |
HART GERMAN) gait » SgASANSKRIT) ea oie
HEARD — (OLD ENGLISH) wf Ki! KRATU., KATHINA
HARD ENGLISH) 5S KHELK ARMENIAN) gs!
HAARD (DANISH) S\asl3 KRATUS (GREER) gli
HARD (SWEDISH) Say HARDUS GOTHIC) S$
BAARD NORWEGIAN) 15$33 OLD SCANDINAVIAN) pS 52h}
HARD (DUTCH) 52k HARDER
. HARD = (OLD SAXON) oS gS
[pdf page 235]
a rcKrY.---  @°; 2 2& ©.
Cpa Sa 8 pe ae | |
BUCK: REFERENCES [ron ny
1200-1202 , 1064-

### ARMA pdfpage~ 24
GLUE w ys
5 pS UeHSTs eal abet GasU aT St dy Lab shee cx alow pap wa} 29 als
tig ah3
Saal 088 cee AM had se a7 AS ELS 29 Gor Glrojly oye
cate 32.9044 gl 2 yhy DLL! 3I JS Gate 1 Ky SS gt Akin Slates hy
TT NA OLS S ager id File tim Go j8b at Slat Uo eye Sl aves
le bey cx seillge 32 Ga Obj shld y WUT gly 3 FI aly!
(IRANIAN LANGUAGES) «thule
DESY 6 AU slaty 9 ESL y lel ySIyla asim glalsleljgisyl
SLT poli pe 33 lp ell al SYELS 30 gly ly ye ASF aK y de lat y
2A IS 9 SIT po 99 SET Myo otis, sire lew 9 93% Sh y2 lab Shag jm 9 ETP
Shaul s3T 3k) 6 SEIS 9 thd SEE; 9 (Ep 9 SH) shoe CUE 4 em Cl
Flake Gla) ops oaks gj BCA KS Syd, f AF y Spt YT « Gy sly
ly sae 99305 2 Shy isd oti @ Sosa 29) GAS y2 {gs 6 (SARMATIAN)
[pdf page 25]
cL
1185 Ob5 ah ste cleat, | re
LT 52 Dhey pladaeal 4 SIKH Jat 59 (92 Sahel sld5 » Golde
IS jee 151 Leal 9 dL (ALANS) Vi So gal ¢.3 (MALLORY, 48.49)
Wad b atte b losin) So gla! (8 IF Chae IE 12.4 Sobyl jyAS le il Lat 59
22 tlewleSe SESE i aptby 52 bib pT lie! jy pI (9 429 gs (SOGDIANS
| ANTS 2 Lact (KHOTANESE SAKA) (28 cll L(g Sal oe OES) oT Sp
"eh po aiayl Ue Ul y cash oat 2ST Ob; 4 pas gain 5 I bs oT a
: Sg Su
JOLIET BT cay (62D pa jar phd cleo) obj uy (lene
JF Shae 3 s

### ARMA pdfpage~ 41
I)
tala gaegn gle lays 2b Gly alesyg 9 (YASHTS) lectin ly jaT ls olaay yo gale
O99 99 9d Lim gas yg bs glands y2 Lergl aye ye gs cl (VIDEVDAD)
eel eal a ppd Seedy 4 (62% 1 YYF) LIL.
BBE NL AFB Vel yet slg abs iI J pbs oS eu al
destin Obyya sleet gi Kew 59 bj oul agar Glas ga ot WF ta 59 Sy gailan oslo
Deo pe Ose ot 19 a phage CHL lie Gets (Gall yo y (hy Lt 4) Sy
eoeh odd $3 thy Fata yh a AS esl, sleoSNy Sl led 5 oy lo
he Bal Wks 4 BAS cell 4 AS Als! GUL; Obslole y SLIKEI algo 5
PAE eS geal I are SY say le ej) dyke USL oul gy age tid
{KHOTANESE) 224 (lp) OG 6 sgt Jd Glrgeej pe ¢27 0b5) Bab (col
tale MBACTRIAN) oh 5 (SOGDIAN) (sie (TUMSHUGUESE) (ft 9
5 Ghaw ASLe) das y thos yo Lab} ou) 5 sp (SARMATIAN) «sll. (CHORESMIAN)
[pdf page 42]
. ie
Fr / plas
lea 5 SS A te (lly
IT GES Sole oy So3 el OH LWT Vb CE lel pre
29 lal SOL; say cory Wes 6 55 JE 9 Oy ellen oy ala! Gls SIs
ined 99 3b NB Bb eos sly age y lal slabs Kh at dbul ST y GS p clel
BOS 3 GEN 53 oy 33 NSF Y oe cee lb Aj ITY Head 9 ey yl
LD y od cleo 5 Guise Cyl Apt sbabs ji oF Gly S51 95 9 ley
52590 38) 537 Gilg) GOL; a sath 9 ging Shar ob ple Jy Curl 03 Srl wore y
Ghy GREL Ss yoo Shi Los ghyly oe yricwb (ody eh yeshy
weary GSI, s
```


## [2026-09-04T23:19:16.508Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B1%D8%A7%D8%A8%D9%87/",
 "prompt": "Quote the فرهنگ معین and لغت‌نامه دهخدا entries for ارابه, including any origin tag such as [ع.] (Arabic), [تر.] (Turkish), or an etymological note about عربة / عراده.</prompt>\n"
}
```


### [2026-09-04T23:19:23.417Z] TOOL RESULT

```
# ارابه - Dictionary Entries

## فرهنگ معین
"(اَ رّ بِ ) (اِ. ) گاری با دو چرخ که از چوب می ساختند و برای حمل بار از آن"

This entry describes a wooden two-wheeled vehicle traditionally used for cargo transport.

## لغت‌نامه دهخدا
"گردون که از چوب سازند و بر آن بار کشند"

The Dehkhoda dictionary identifies this term with a wooden wheel-based transport mechanism designed for hauling loads. The entry also notes that scholars debated the correct spelling, with some arguing for عراده (with specific diacritical marks) as the authentic form.

**Etymology note:** Both sources trace the word through Persian linguistic tradition as a vehicle pulled by animals, particularly horses or mules, distinct from four-wheeled variants like کالسکه (carriages designed for passengers).
```


## [2026-09-04T23:19:31.692Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D8%B1%D8%AA%DB%8C%D8%B3%D8%AA/",
 "prompt": "Quote the فرهنگ معین and فرهنگ عمید entries for آرتیست, including the origin tag (e.g. [فر.] French).</prompt>\n"
}
```


## [2026-09-04T23:19:33.526Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A7%D8%B1%D8%A7%D8%A8%D9%87/' --note 'page 62, node 12: Moin & Dehkhoda entries for ارابه (no Arabic/Greek origin tag)' 2>&1 | tail -2",
 "description": "Archive abadis arabe"
}
```


### [2026-09-04T23:19:37.733Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T23:19:41.941Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ec1cfc60b91d7745.txt
```


## [2026-09-04T23:19:47.546Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A2%D8%B1%D8%AA%DB%8C%D8%B3%D8%AA",
 "prompt": "Quote the Mo'in (and any other) dictionary entry for آرتیست, including the origin tag such as [فر.] (French).</prompt>\n"
}
```


### [2026-09-04T23:19:51.674Z] TOOL RESULT

```
# Mo'in Dictionary Entry for آرتیست

According to the Mo'in Publishing Dictionary:

**[فر.] (ص .)** "هنرمند، هنرپیشه" (artist, performer) and "کنایه از: آدمی که برای رسیدن به خواسته هایش نقش بازی کند" (an allusion to someone who acts out a role to achieve their desires).

The origin tag **[فر.]** indicates this is a French loanword.
```


## [2026-09-04T23:19:58.534Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D9%84%DA%AF%D8%A7%D8%B1%DB%8C%D8%AA%D9%85",
 "prompt": "Quote the Mo'in dictionary entry for لگاریتم, including the origin tag such as [فر.] (French).</prompt>\n"
}
```


## [2026-09-04T23:19:58.980Z] TOOL CALL #82: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://vajehyab.com/moein/%D8%A2%D8%B1%D8%AA%DB%8C%D8%B3%D8%AA' --note 'page 62, node 16: Moin tags آرتیست [فر.] French loanword' 2>&1 | tail -1",
 "description": "Archive vajehyab artist"
}
```


### [2026-09-04T23:20:02.423Z] TOOL RESULT

```
# Mo'in Dictionary Entry for لگاریتم

According to the Mo'in Publishing Dictionary (فرهنگ انتشارات معین), the entry reads:

"(لُ) [فر.] (اِ.) نمادی است در ریاضی که نشان می دهد عدد A (مبنای لگاریتم ) به چه توانی برسد تا عدد معینی به دست آید."

This defines logarithm as a mathematical symbol indicating the power to which a base number (A) must be raised to produce a specific result. The origin tags indicate French [فر.] and English [اِ.] sources.
```


### [2026-09-04T23:20:04.875Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3b8fee1bca437562.txt
```


## [2026-09-04T23:20:19.011Z] TOOL CALL #83: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/fetch_source.py 'https://vajehyab.com/moein/%D9%84%DA%AF%D8%A7%D8%B1%DB%8C%D8%AA%D9%85' --note 'page 62, node 10: Moin tags لگاریتم [فر.] French loanword' 2>&1 | tail -1; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,os\ndef g(f,pat,n=1,ctx=(120,400)):\n    if not os.path.exists(f): print('MISS',f); return\n    d=open(f,encoding='utf-8',errors='replace').read()\n    c=0\n    for m in re.finditer(pat,d):\n        i=m.start(); print('###',os.path.basename(f),'/',pat,'::',d[max(0,i-ctx[0]):i+ctx[1]].replace('\\n',' ')); print(); c+=1\n        if c>=n: break\n    if c==0: print('--- SILENT',os.path.basename(f),pat)\ng('AFA.txt',r'[Aa]raba')\ng('FVQ.txt',r'araba')\ng('SYN.txt',r'arm.*Goth.*arms',1)\ng('IEC.txt',r'ar[eə]?-?mos|harmos|arithmos',2)\nEOF",
 "description": "Fraenkel/Jeffery/Buck/Mann checks"
}
```


### [2026-09-04T23:20:21.426Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6cd9f6aa35992d1f.txt
### AFA.txt / [Aa]raba :: i laa Almonrido. IBSI. 4 >ol. 8*. -- laiu J-Al-Makkari. 1871. S-...fS.Ta. La ealaDdricr- da CordMa da TaMia ' 9St. Täta Araba at amA Latiaa. 187S. 8>. Dia IwaÜilaa n Uakka, tob' DBtik'- Zat Um in'a t&ifta Jabrbaadvt «mmt ZailraehBBDg. Au dcta HnlUad. IbMaltf. ' iiS4. 8". , . . ii.7a. ■- Em! anr l'biMoif« da ritteitaM. Trad. da HoUiadabpar V. Cuimv. 1879. . 8». . . -. I8.TS bat 1880. 8 ToL nüii 4'. . . ITO.— . •: CumctloB« aar Im tattaa da BniM -' 1.Hi>r<b d-lba-Adkdrf <da Manrt. daa ^ ft^maat* da U «braniqua d'Atfb

### FVQ.txt / araba ::  xvii,  p. 140. Theso converts of Simeon are said to have been brought back to the orthodox  faith by the preaehing of Maraba (Labourt, Le. rhristianisme flans VEinpire perse,  p. 191). Assemani, liibl. Or., iii, 2, 606, mentions Monophysite Bishops of al-Hira.   4 Andrae, I'rsprung, 25; Lammens in K0(\ ix, 32 ff.   b See the long account of them in Andrae, rraprtiny, 7-24.   6 Sura, Ixxxv, 4 ff. It is only fair, however, to state that Western seholars are  not unanimous in accepting this as a reference to the pers

### SYN.txt / arm.*Goth.*arms :: o)- in Grk. dpapicnw ‘fit’, &p8pov ‘joint’, Lat. artus ‘joint’, etc. Walde-P. 1.73. Er- nout-M. 74, Walde-H. 1.69. Lat. armus mostly ‘shoulder, fore- quarter’ of animals, rarely ‘arm’ of men; Goth. arms, etc., general Gmc.; OPruss. armo ‘arm’; ChSl. ramo, rame, SCr. rame ‘shoulder’, Boh. rdmé, rameno, mostly ‘arm’, Pol. ramie, ‘shoulder, arm’; Skt. trma- ‘forequarter’ of an animal; Av. arama- in aramd-Sita- ‘thrown by the arm’; Arm. armuka ‘elbow’. 2. IE *bhaghu-. Walde-P. 2.130. Grk. rixus, Dor. raxus, mostly ‘for

### IEC.txt / ar[eə]?-?mos|harmos|arithmos ::  karm, m. Lat: MHG karmen ‘weep, moan’; WG and Du. kermen, id.; Li. nu-garmu, -garmeti 'echo', cf. garmaluoti ‘burble’ garmos, is ‘cry, wail’. Cf. garmó, garsmos, gharm- Mir. gairm; Cor. Br. W garm fr. Ir.?; OS karm, gargolo, ið (gorgol-) — gauros 15 20 25 30 35 40 45 266 OE cearm, cierm; Li. cf. gafsmas ‘rumour; talk; glory? beside nu-garmeéti ‘echo’ garos, see garā gars- ‘shout, cry, resound, echo’. Cf. gouor-, gar-, garm-, gers- and see WP I, 537, 609 & 686 Arm. kar-a£, anc o-st. “shout, shouting’; Lat. garriō, 

### IEC.txt / ar[eə]?-?mos|harmos|arithmos :: kérren, OE ceorran & cierran ‘creak’, see gers-) garsmos, is (garsmn-) ‘cry, call’, etc. See gars-, garā, etc. and cf. garmos Mir Ir. gairm, pl. garma, garmanna “call; praise; fame’; W, Br. Cor. garm ‘shout’; OS karm, i-st.; OE cearm, cierm; cf. Du. kermen ‘wail’; Li. gafsmas ‘rumour; talk; glory’ (The Ir. W. & Gmc. forms ambig.) garst- (gars-) (1) ‘rocky massif, dry rock’ (Celtic variant gart-) Ir. gart “crack in dried earth’; Gaul. garta-; OW garth ‘mountain — ridge’; W. Cor. ‘head- land’; G Karst ‘limestone rang
```


## [2026-09-04T23:22:19.360Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(pages))\n# index near the end lists 'ratu- 226/3'; glossary pages numbered; find leaf whose text has 'rat' and page-num 226\nfor i,p in enumerate(pages):\n    if re.search(r'\\b226\\b',p) and i<200:\n        print('leaf',i,'::',p[:300].replace('\\n',' '))\nEOF",
 "description": "Find SNS page 226"
}
```


### [2026-09-04T23:22:21.469Z] TOOL RESULT

```
leaves 243
leaf 62 :: \x                               Ui c*-.b *.b «jl,                                                                                         U; ii—«U««bajtj                              (                                                                                                                   
leaf 144 ::                                                                                                                                                 bjc-,U«.U«i1j                                                        TOT                                                  b 4.U »v|j
```


## [2026-09-04T23:22:27.638Z] AGENT

Now I'll write the verification file.


## [2026-09-04T23:31:33.639Z] TOOL CALL #85: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-62.json <<'JSONEOF'\n{\n  \"pdf_page\": 62,\n  \"book_page\": 32,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ar, Are\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂er- (older notation *ar-, *arə-) 'to fit together, join'\",\n      \"note\": \"Pokorny IEW 55-61 heads the article '1. ar-, themat. (a)rē-, schwere Basis arə-, rē- und i-Basis (ə)rī-, rei- ... \\\"fügen, passen\\\"'; Watkins/AHD prints 'ar-. Also arə-. To fit together. [Pok. 1. ar- 55.]' — Nourai's root name, language label, gloss and page reference are copied from AHD and are correct. In current laryngealist notation the root is *h₂er-. Two cross-cutting caveats: (a) most of Nourai's Latin/Greek/Germanic material is lifted verbatim from the 1975 AHD appendix (the gloss 'ôrdô: row of threads in loom' is Watkins' own wording), and where Watkins hedges ('Possibly suffixed variant form (or separate root) *ōr-dh-'; 'Variant or separate root *rē-') Nourai drops the hedge — the *rē-dh- branch that carries Old Persian rādiy, Persian rā and English read is reconstructed by most current handbooks as an independent root *Hreh₁dʰ-, and Pokorny himself calls the link of Latin ōrdō to ar- 'ganz fraglich' (IEW 61). (b) The whole Greek→Arabic→Persian branch (harma → 'araba → ارابه) is rejected by every reference consulted: Lokotsch files araba as Turkish, Wiktionary as Turkic of uncertain ultimate origin, Asbaghi as a Persian word arabicised, and Borhan-e Qate' gives no etymology at all.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₂er- (در نگارش قدیم‌تر *ar-/*arə-) به معنی «جور کردن، به هم پیوستن، سامان دادن» است؛ پوکورنی آن را در فرهنگ ریشه‌شناسی هندوژرمنی، صفحات ۵۵ تا ۶۱، با معنی «fügen, passen» آورده و واتکینز در پیوست فرهنگ American Heritage عیناً «to fit together» را با ارجاع به «Pok. 1. ar- 55» ثبت کرده است؛ پس نام ریشه، برچسب زبانی و معنی در نمودار نورایی درست است. دو نکتهٔ کلی: نخست آنکه شاخهٔ *rē-dh- (که پارسی باستان rādiy و «را»ی فارسی و read انگلیسی از آن می‌آید) در پژوهش امروزی غالباً ریشه‌ای جداگانه (*Hreh₁dʰ-) شمرده می‌شود و حتی خود پوکورنی پیوند ōrdō لاتینی را با این ریشه «کاملاً مشکوک» می‌خواند؛ دوم آنکه شاخهٔ یونانی ← عربی ← فارسی (harma ← عربة ← ارابه) را هیچ‌یک از مآخذ تأیید نمی‌کند و لوکوچ، ویکی‌واژه و اصباغی آن را واژه‌ای ترکی (یا فارسی معرَّب) می‌دانند نه یونانی.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:55\",\n          \"status\": \"supports\",\n          \"note\": \"POK_01.txt leaf 64 (printed p.56, article opening; standard citation of the article is 'Pok. 1. ar- 55'): 'I. ar-), themat. (a)rē-, schwere Basis arə-, rē- und i-Basis (ə)rī-, rei- ... \\\"fügen, passen\\\", mehrfach und vielleicht ältest vom planmäßigen Aufeinanderlegen beim Holzbau ... aber auch vielfach auf geistiges Zurechtlegen, Berechnen übertragen.' AHD_watkins1985.txt line 287 closes its entry with '[Pok. 1. ar- 55.]', which is exactly Nourai's page.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"Band I pp. 55-62 (POK_01.txt leaves 63-70)\",\n          \"stance\": \"supports\",\n          \"note\": \"The article runs pp. 55/56-62 and contains, in order, the Avestan, Greek, Latin, Germanic and Old Persian material Nourai charts.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I pp. 69-77 (WLD_Bd1_1930_dli_70244_djvu.txt lines ~4600-5050)\",\n          \"stance\": \"supports\",\n          \"note\": \"Walde-Pokorny's 'ar-' article, of which Pokorny's IEW entry is the abridgement; running head 'ar-' on pp. 71-77.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 s.v. ar-\",\n          \"stance\": \"supports\",\n          \"note\": \"'ar-. Also arə-. To fit together. I. Basic form *arə-...' — Nourai's root box is a transcription of this headword.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck s.v. 'arm' (SYN.txt)\",\n          \"stance\": \"supports\",\n          \"note\": \"'*ar(ə)- in Grk. ἀραρίσκω \\\"fit\\\", ἄρθρον \\\"joint\\\", Lat. artus \\\"joint\\\", etc. Walde-P. 1.73. Ernout-M. 74, Walde-H. 1.69.'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, searched for harmos / arithmos / ar-mo-\",\n          \"stance\": \"silent\",\n          \"note\": \"No usable entry retrieved from the OCR.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"ratu\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan ratu- m. is the thematic t-stem *r̥-tu- built to the zero grade of *h₂er- ('that which is set right / put in order'), the exact formal counterpart of Vedic r̥tú- 'fixed time, order, rule' and of Latin artus, -ūs 'joint'. In the Gathas it is 'judge, arbiter, one who pronounces the ratu (judgement)'; in the Younger Avesta it is the 'Ratu', the model or patron of each class of beings and, in the liturgy, the priestly office paired with the ahu- (ahu-ca ratu-ca 'overlord and chief judge'). Bartholomae AiW cols. 1498-1500 gives ¹ratav- 'Richter, Meister' and ³ratav- 'Judicium, Richterspruch'; Pokorny 56 quotes it as 'ratu- m. \\\"Richter, Schiedsrichter\\\" und \\\"Zeitraum\\\" (gemeinsame Grundbedeutung etwa \\\"Zurechtlegung\\\", woraus \\\"Zurechtlegung des Rechts\\\" und \\\"richtiger Zeitpunkt\\\")'. Nourai's gloss 'judge, religious leader' covers both the Gathic and the Younger-Avestan usage and is accurate.\",\n          \"derivation_fa\": \"اوستایی ratu- ستاکی است بر پایهٔ درجهٔ صفر ریشهٔ *h₂er- با پسوند ‑tu‑ (یعنی *r̥-tu-)، هم‌ریشه و هم‌ساخت با سنسکریت r̥tú- «هنگام مقرر، نظم» و artus لاتینی «بند، مفصل». در گاهان به معنی «داور» و در اوستای نو به معنی «رَتو»، یعنی سرور و نمونهٔ هر ردهٔ آفرینش و نیز مقامی دینی که در کنار «اهو» می‌آید (ahu-ca ratu-ca). بارتولمه در «فرهنگ ایرانی باستان» ستون‌های ۱۴۹۸ تا ۱۵۰۰ آن را «داور، سرور» و «حکم، رأی داوری» معنی کرده و پوکورنی نیز در صفحهٔ ۵۶ همین را با معنی بنیادین «سامان‌دادن» آورده است. بنابراین برچسب زبانی و معنایی که نورایی داده درست است و ادعای او پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"WLD:74\",\n              \"status\": \"partial\",\n              \"note\": \"The right article, the wrong page: in WLD Bd. I the passage 'mit themat. Vokal (*r̥-e-) av. ratu- m. \\\"Richter, Schiedsrichter (vgl. z. Bed. u. gr. ἀρτύνας); Richterspruch\\\", ratu- \\\"Zeitabschnitt, Zeitraum\\\" (gemeinsame Gdbed. etwa \\\"Zurechtlegung\\\")' stands on p. 71 (WLD_Bd1_1930_dli_70244_djvu.txt line 4692, page marker '71' at line 4710); p. 74 is the *rē-/rō- section (Lat. reor, rērī, ratio).\"\n            },\n            {\n              \"ref\": \"POK:56\",\n              \"status\": \"supports\",\n              \"note\": \"POK_01.txt leaf 64 (printed p. 56): 'ratu- m., \\\"Richter, Schiedsrichter\\\" und \\\"Zeitraum\\\" (gemeinsame Grundbedeutung etwa \\\"Zurechtlegung\\\", woraus \\\"Zurechtlegung des Rechts\\\" und \\\"richtiger Zeitpunkt\\\")' — with an explicit reference to 'Bartholomae Airan. Wb. 189/1509'. Exactly Nourai's arrow.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW cols. 1498-1500 s.v. ratav- (BRT.txt lines 25020-25032)\",\n              \"stance\": \"supports\",\n              \"note\": \"'¹ratav-' with the Pahlavi rendering noted in the apparatus: 'Pü.: rat, ratīh, erl. (oft): dastwar' — and separately '³ratav- m. \\\"Judicium, Richterspruch\\\"'; also 'ratu-xšaθra- \\\"die Herrschaft des Ratav innehabend\\\"'.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p. 56\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check; the t-formations rt-, art- 'zusammengefügt' with av. arəta-, ap. arta- follow on p. 57.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Manual of Pahlavi II, s.v. rat (NYB_vol2_glossary.txt line 3270)\",\n              \"stance\": \"supports\",\n              \"note\": \"'rat [lt\\\\'] \\\"genius\\\", divinity or tutelary spirit presiding over one of the categories ... he is in Avestan terminology the ahū and ratu of the world ... — Av. (1498 sqq.) ²ratu-; NP rad \\\"intelligent, learned\\\", \\\"a high priest of the Magi\\\".'\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"rad\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan ratu- > Middle Persian rad by the two regular Middle Iranian changes: intervocalic/post-vocalic -t- is voiced to -d- (Av. pitar- > MP pidar, Av. ratu- > MP rad) and the final -u of the u-stem is lost with the collapse of Old Iranian nominal inflection. MacKenzie's Concise Pahlavi Dictionary p. 70 gives 'rad [ltl] (spiritual) chief, master. ~īh: office of rad' and, on the same page, the derivative 'radunay [/twny = Av. ratunaya-] one under the guidance of a rad', which makes the Avestan source explicit. Nyberg's glossary s.v. rat spells the Book Pahlavi ⟨lt'⟩ and glosses it '\\\"genius\\\", divinity or tutelary spirit presiding over one of the categories ... into which all beings of the good creation are divided ... Av. ²ratu-; NP rad'. The word is a technical term of the Zoroastrian priesthood (Pahlavi rad = the dastwar), which is why Nourai's 'leader, master, Sir' is right for the Middle Persian stage.\",\n          \"derivation_fa\": \"پهلوی rad بازماندهٔ مستقیم اوستایی ratu- است: «ت» ایرانی باستان در جایگاه پس‌واکه‌ای در فارسی میانه به «د» نرم شده (مانند pitar → pidar) و واکهٔ پایانی ستاک u با از میان رفتن صرف اسمی ایرانی باستان افتاده است. مکنزی در «فرهنگ کوچک پهلوی» صفحهٔ ۷۰ می‌نویسد rad ⟨ltl⟩ «سرور و پیشوای (مینوی)» و در همان صفحه radunay را «= اوستایی ratunaya-» می‌آورد که پیوند اوستایی را آشکار می‌کند؛ نیبرگ نیز در واژه‌نامهٔ خود ذیل rat می‌گوید «اوستایی ratu-، فارسی نو رد». این واژه اصطلاحی دینی است و در ترجمه‌های پهلوی اوستا معادل «دستور» به کار رفته است؛ پس معنی «سرور، پیشوا» که نورایی داده درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SNS:226\",\n              \"status\": \"partial\",\n              \"note\": \"Checked through the book's own Avestan index, which is legible in the OCR: SNS.txt line 29239 'ratu- 226/3' (and line 29394 'ratustaitīh 226/6'), i.e. Tavoosi's Šāyast nē Šāyast glossary refers a headword on p. 226, line 3 to Avestan ratu-. The Persian OCR of the glossary page itself is unusable (SNS_pages.txt has 243 leaves with no readable printed page numbers), so I could not quote the entry text.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p. 70 s.v. rad (PHD.txt line 555)\",\n              \"stance\": \"supports\",\n              \"note\": \"'rad [ltl | N —] (spiritual) chief, master. ~īh: office of rad.' — note the separate entry 'rad [Pu | P rd, N ~] generous, liberal' which is a different word (< *rāta-).\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Manual of Pahlavi II s.v. rat\",\n              \"stance\": \"supports\",\n              \"note\": \"'rat [lt\\\\'] ... Av. (1498 sqq.) ²ratu-; NP rad \\\"intelligent, learnd\\\", \\\"a high priest of the Magi\\\".'\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW apparatus to ratav-\",\n              \"stance\": \"supports\",\n              \"note\": \"'Pü.: rat, ratīh, erl. (oft): dastwar' — Bartholomae records the Pahlavi translation of Av. ratu- as rat, glossed dastwar.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"rad\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian رَد rad continues Middle Persian rad unchanged (no further sound change is involved; the word survives mainly as an archaism of the Zoroastrian and epic register). Nushin's Vāzhe-nāmak, the Shahnameh glossary, states the chain outright: 'رد (با زبر اول) از ریشهٔ اوستایی رتو ratu، پهلوی رت rat، به معنی بزرگ و سرور مینوی (پورداود، ویسپرد ص ۹۱). در گات‌ها به معنی داور (پورداود، یادداشت‌های گات‌ها ۱۲). \\\"دانا و بخرد\\\" (لغت فرس، صحاح)', and it quotes exactly the Ferdowsi line Nourai reproduces ('دل بخردان داشت و مغز ردان'). Borhan-e Qate' glosses رد 'حکیم و دانشمند - و خواجه - و پهلوان و دلاور و بهادر', which matches Nourai's 'leader, judge, hero, wise' term for term. Wiktionary's Persian رد (etymology 1) has '(archaic) sage (wise person); an important person in Zoroastrianism'. The only complication is that Horn (no. 601) files Pahlavi rat (as a title) under رَاد rād 'generous' (Av. rāiti-, Skt. rāti-); Bartholomae, MacKenzie and Nyberg keep the two apart, and Nushin's Avestan derivation is the one modern scholarship follows.\",\n          \"derivation_fa\": \"«رَد» فارسی دنبالهٔ بی‌واسطهٔ rad فارسی میانه است و دگرگونی آوایی تازه‌ای در آن روی نداده؛ این واژه بیشتر در متون زردشتی و حماسی مانده است. نوشین در «واژه‌نامک» (فرهنگ واژه‌های دشوار شاهنامه) همین زنجیره را می‌آورد: «رد (با زبر اول) از ریشهٔ اوستایی رتو ratu، پهلوی رت rat، به معنی بزرگ و سرور مینوی (پورداود، ویسپرد ص ۹۱)؛ در گات‌ها به معنی داور؛ \\\"دانا و بخرد\\\" (لغت فرس، صحاح)»، و دقیقاً همان بیت فردوسی را گواه می‌گیرد که نورایی نقل کرده است. برهان قاطع نیز رد را «حکیم و دانشمند و خواجه و پهلوان و دلاور و بهادر» معنی کرده که با معنی‌های نمودار می‌خواند. تنها نکته آنکه هُرن (شمارهٔ ۶۰۱) rat پهلوی را ذیل «راد» (از rāiti- اوستایی) آورده و این دو واژه را یکی گرفته است، حال آنکه بارتولمه، مکنزی و نیبرگ آنها را جدا می‌دانند و رأی اخیر پذیرفته‌تر است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:943\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' (Mo'in's ed.), 'بیان هفتم: در رای بی‌نقطه با دال ابجد', BQT_v2_pages.txt leaf 403 (printed page ≈ 946 on the scan's leaf+543 mapping, which refs_online.json rates as ±3): 'رد - بفتح اول وسکون ثانی، حکیم و دانشمند - و خواجه - و پهلوان و دلاور و بهادر ... مردود و از نظر افتاده'. No Mo'in etymological footnote is attached to this headword.\"\n            },\n            {\n              \"ref\": \"MON:1645\",\n              \"status\": \"not_checked\",\n              \"note\": \"Only a 2-volume abridgement of Mo'in (MON_part1/2) is on disk, without page mapping to the 6-volume 1363 print; abadis/vajehyab reproduce entry text but no page numbers (refs_online.json: 'Page numbers cannot be mapped online').\"\n            },\n            {\n              \"ref\": \"FSF:199\",\n              \"status\": \"supports\",\n              \"note\": \"Nushin, Vāzhe-nāmak, FSF_pages.txt leaf 265 (running head 'رد'; the printed folio numeral OCRs as ۹۳/۱۹۹): 'رد (با زبراول) از ریشه اوستایی رتو ratu پهلوی رت rat به معنی بزرگ و سرور مینوی (پورداود، ویسپرد ص ۹۱). در گات‌ها به معنی داور (پورداود یادداشت‌های گات‌ها ۱۲). \\\"دانا و بخرد\\\" (لغت فرس: صحاح): دل بخردان داشت و مغز ردان / دو کتف یلان و هش موبدان.' This is Nourai's whole chain plus his verse, in one entry.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 2, leaf 403 s.v. رد\",\n              \"stance\": \"supports\",\n              \"note\": \"'حکیم و دانشمند - و خواجه - و پهلوان و دلاور و بهادر' = Nourai's 'leader, judge, hero, wise'.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"leaf 265 s.v. رد\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check; gives Av. ratu > Phl. rat > NP rad explicitly.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 601, p. 134\",\n              \"stance\": \"partial\",\n              \"note\": \"'601. rād \\\"freigebig\\\". aw. vergl. rāiti-; ai. rāti- \\\"willig zu geben\\\"; phlv. rat (auch Titel, vergl. Horn, Mitteilungen, Heft IV, 27), ratīh.' Horn puts the Pahlavi title rat under rād 'generous', not under Av. ratu- — a conflation the later dictionaries reject.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part1/2 (Adena abridgement), searched رد\",\n              \"stance\": \"silent\",\n              \"note\": \"The abridgement has only the Arabic رد 'rejection'; the archaic Zoroastrian رد is not carried.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"arânte; aram, arem\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both forms are real and both stand on Pokorny's p. 56, but the labels are not quite right. (a) Av. arəṇte (Nourai's 'arânte') is the 3rd plural present middle of ar- and Pokorny glosses it 'sie setzen sich fest, bleiben stecken' — 'they set themselves firmly, stay put', i.e. the intransitive/middle 'fit oneself in place', not the transitive 'puts in order' of the chart; it is the Iranian counterpart of Greek ἀραρίσκω 'I fit together' and of Skt. r̥ṇóti/r̥ccháti. (b) 'arem' is Avestan arəm, an adverb 'passend, entsprechend' ('fittingly, properly', e.g. in arəm-piθwā 'meal-time, the time fitting for a meal'), from the zero grade with the adverbial ending -əm; but 'aram' with plain -a- is the Sanskrit twin áram/álam 'fittingly, enough' (whence álaṃ-kar- 'to adorn'), which Pokorny lists in the same breath — Nourai has silently put a Vedic form in an Avestan box. The derivation from *h₂er- is not in doubt for either word; only the gloss of arəṇte and the language label of aram are loose.\",\n          \"derivation_fa\": \"هر دو صورت واقعی‌اند و هر دو در صفحهٔ ۵۶ پوکورنی آمده‌اند، ولی برچسب‌ها دقیق نیست. نخست، arəṇte اوستایی سوم‌شخص جمع حال میانه از ستاک ar- است و پوکورنی آن را «استوار می‌نشینند، بر جای می‌مانند» معنی کرده، یعنی معنایی لازم و میانه، نه «سامان می‌دهد» که در نمودار آمده؛ همتای یونانی آن ἀραρίσκω است. دوم، «arem» همان arəm اوستایی است، قیدی به معنی «به‌جا، درخور» (مانند arəm-piθwā «هنگام خوراک»)، ولی «aram» صورت سنسکریت áram/álam «به‌اندازه، بسنده» است که پوکورنی در کنار آن آورده؛ یعنی نورایی یک واژهٔ ودایی را در جعبهٔ اوستایی نشانده است. اشتقاق هر دو از *h₂er- مسلم است و تنها معنی arəṇte و برچسب زبانی aram با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:56\",\n              \"status\": \"partial\",\n              \"note\": \"POK_01.txt leaf 64 (p. 56): 'Av. arənte \\\"sie setzen sich fest, bleiben stecken\\\", ai. arā-h \\\"Radspeiche\\\", aram, álam Adv. (áram-kar-, alaṃkar- \\\"zurechtmachen\\\") \\\"passend, genug\\\", av. arəm \\\"passend, entsprechend\\\" (arəm-piθwā \\\"Mittag\\\" = \\\"die zum Mahle passende Zeit\\\")'. The page supports the forms and the root but glosses arənte differently from Nourai and marks aram/álam as Sanskrit, arəm as Avestan.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p. 56\",\n              \"stance\": \"partial\",\n              \"note\": \"See ref_check.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 70 (line 4660): 'an arəm, arənte anzuschließen, vgl. Scheftelowitz ZDMG. 59, 693'\",\n              \"stance\": \"supports\",\n              \"note\": \"Walde-Pokorny cite the pair arəm / arənte together in the same article, confirming both belong to *ar-.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW s.v. arəm- / ar- (BRT.txt line 5522 'ar?ma-', line 2801 '*arəm-...')\",\n              \"stance\": \"partial\",\n              \"note\": \"Bartholomae has the forms, but the 1904 Google OCR of the column text is too corrupt to quote a continuous gloss.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"An empty pass-through box. The printed page (pdf p. 62, rendered at 450 dpi) really does show a blank rectangle drawn to the right of the 'Avestan arânte / aram, arem' box, with the connecting arrow, but with no language label, no reference and no word inside it — Nourai's layout left the descendant slot empty (compare part ONE of the same root, to which the root box refers). The extraction is faithful to the page; there is nothing to verify.\",\n          \"derivation_fa\": \"این گره جعبه‌ای تهی است. در تصویر صفحهٔ چاپی (صفحهٔ ۶۲ پی‌دی‌اف، با تفکیک ۴۵۰) به‌روشنی دیده می‌شود که در برابر جعبهٔ «اوستایی: arânte / aram, arem» چهارگوشی خالی با پیکان رسم شده که نه برچسب زبانی دارد، نه ارجاع و نه واژه؛ یعنی نویسنده جای بازماندهٔ آن شاخه را نانوشته گذاشته است (بخش نخستِ همین ریشه را بنگرید). استخراج داده‌ها با صفحهٔ چاپی می‌خواند و چیزی برای راستی‌آزمایی وجود ندارد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference in the book.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW pp. 55-62\",\n              \"stance\": \"silent\",\n              \"note\": \"No descendant can be checked because the box is empty.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins s.v. ar-\",\n              \"stance\": \"silent\",\n              \"note\": \"Same.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Old Persian\",\n          \"words\": \"râd 1, râdiy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Persian rādiy (𐎼𐎠𐎭𐎡𐎹) is the locative singular of a stem rād- 'reason, cause', used as a postposition governing the genitive, 'on account of, for the sake of'. Kent's Lexicon (Old Persian, p. 205) reads: 'rādiy ... various uses, often affixed to direct object for clarity; also OCS radi, postpos. with gen., \\\"on account of\\\"; loc. sg. of rād- (§188.III), to root in Skt. rādh- \\\"effect, complete\\\" ... DB 4.54; DNb 9, 10f; also in avahyarādiy'; the compound avahya-rādiy 'for this reason' is a stock formula of Darius' Bisotun inscription (DB 1.6f, 51; 4.47, 62). Pokorny files it in the dh-extension of *ar-: 'apers. rādiy (Lok. Sg.) \\\"wegen\\\"' under *rē-dh-, *rō-dh-, *rə-dh- alongside Skt. rādhnóti, Av. rādaiti 'macht bereit', NP ārāstan. Nourai's box, gloss and language label are all correct; the one live scholarly question is whether *reh₁dʰ-/*Hreh₁dʰ- is really an extension of *h₂er- (Pokorny, Walde-Pokorny, Watkins 1975) or an independent root (LIV, Etymonline, current AHD), and Kent himself pointedly separates it from '²rad-, pIE *rej-'.\",\n          \"derivation_fa\": \"پارسی باستان rādiy صورت «در جای» (لوکاتیو) ستاک rād- «سبب، علت» است و همچون پس‌واژه با اضافه به کار می‌رود: «به سبب، به خاطر». کِنت در واژه‌نامهٔ «پارسی باستان» صفحهٔ ۲۰۵ می‌نویسد rādiy پس‌واژه با اضافه، «به سبب»، و آن را «لوکاتیو مفرد rād-» و هم‌ریشه با rādh- سنسکریت «به انجام رساندن» می‌داند؛ ترکیب avahya-rādiy «از این روی» از عبارت‌های پرکاربرد سنگ‌نبشتهٔ بیستون داریوش است (DB ۱٫۶، ۴٫۴۷ و …). پوکورنی نیز در صفحهٔ ۶۰ همین را ذیل گسترش *rē-dh- از ریشهٔ ar- می‌آورد. بنابراین گزارهٔ نورایی درست است؛ تنها بحث زندهٔ امروزی این است که آیا *Hreh₁dʰ- براستی گسترشِ *h₂er- است یا ریشه‌ای جداگانه — که پژوهش نو بیشتر به جدایی گرایش دارد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"WLD:74\",\n              \"status\": \"partial\",\n              \"note\": \"Right article, one page off: 'ap. rādiy (loc. sg.) \\\"wegen\\\" (vgl. aksl. radi ...), npers. ārāyad, ārāstan \\\"schmücken\\\"' stands in WLD Bd. I on p. 75 (WLD_Bd1_1930_dli_70244_djvu.txt line 4946; the page-75 marker follows at line 4963). Page 74 is the *rē-/rō- section with Lat. reor, rērī.\"\n            },\n            {\n              \"ref\": \"POK:56\",\n              \"status\": \"partial\",\n              \"note\": \"The form is in Pokorny's ar- article but on p. 60, not 56: POK_01.txt leaf 68 (p. 60), dh-Erweiterung rē-dh-: 'av. rādaiti \\\"macht bereit\\\", rada- m. \\\"Fürsorger\\\" ... apers. rādiy (Lok. Sg.) \\\"wegen\\\" (vgl. aksl. radi s. unten), npers. ārāyad, ārāstan \\\"schmücken\\\"'. Page 56 has ratu-/arəm, not rādiy.\"\n            },\n            {\n              \"ref\": \"KNT:205\",\n              \"status\": \"supports\",\n              \"note\": \"Kent, Old Persian, Lexicon (KNT.txt): 'rādiy ... often affixed to direct object for clarity; also OCS radi, postpos. with gen., \\\"on account of\\\"; loc. sg. of rād- (§188.III), to root in Skt. radh- \\\"effect; complete\\\" (not to ²rad-, pIE *rej-, with Hz. ApI 280). DB 4.54; DNb 9, 10f; also in avahyarādiy, q.v.' The Lexicon's page numeral 206 appears immediately after, so the entry sits on p. 205 as cited.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Lexicon s.v. rādiy and §251, §191.IV\",\n              \"stance\": \"supports\",\n              \"note\": \"Also 'avahyarādiy phrasal adv. \\\"for this reason\\\": avahyā gen. of ¹ava-, + rādiy \\\"on account of\\\" ... DB 1.6f, 51; 4.47, 62; DBa 9f.'\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p. 60\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 75\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW s.v. rād- / rādah-\",\n              \"stance\": \"partial\",\n              \"note\": \"Bartholomae has Av. rādaiti 'macht bereit', rāda- 'Fürsorger' (quoted second-hand by Pokorny p. 60 and WLD p. 75); the Avestan side of the same stem.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"râ; čerâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Persian rādiy > Middle Persian rāδ/rāy ⟨l'd⟩, spelled ⟨rʾdy⟩ in inscriptional Middle Persian and Psalter Pahlavi and rendered r'd in Parthian, > New Persian را rā. The final -d, already a fricative δ in Middle Persian, is lost in New Persian, exactly as in MP pāδ > NP pā(y). Nyberg's glossary p. 164 is the key witness: '²rād [lʾd; inscr. and Ps. rʾdy] postpos. 1. for the sake of, because of, for ... 2. used as in NP: a) \\\"to, for\\\" ... b) denoting the dir. obj. of the pres. tense ... — OP rād- \\\"reason, cause\\\" in rādiy postpos. \\\"on account of\\\", avahya-rādiy \\\"for this reason\\\"; MPrth rʾd, MPrs rʾy; Paz. NP rā'. Horn no. 600 (p. 134) says the same: 'rā, zur Bezeichnung des Objekts dienende Partikel, rā \\\"wegen\\\" ... ap. rād- in -rādiy \\\"wegen\\\"; phlv. rāδ, rāi'; he adds that the object-marking use grows out of the original 'for, on account of, as regards'. چرا čerā 'why?' is the transparent compound če 'what' + rā 'for the sake of' = 'for what?', a Middle Persian formation (Nyberg: 'čē rād ... why? 35¹¹, 79⁵'); Wiktionary analyses it as چه (če) + رای (rā) 'reason'. Nourai's glosses are exact.\",\n          \"derivation_fa\": \"«را»ی فارسی از rādiy پارسی باستان است: در فارسی میانه rāδ/rāy (نوشتهٔ ⟨lʾd⟩، در کتیبه‌ها و زبور پهلوی ⟨rʾdy⟩، در پارتی rʾd) و در فارسی نو «را»، با افتادن «د» سایشی پایانی درست همان‌گونه که pāδ پهلوی به «پا(ی)» بدل شده است. نیبرگ در واژه‌نامهٔ پهلوی، صفحهٔ ۱۶۴، آن را چنین می‌آورد: «²rād پس‌واژه: به خاطرِ، به سببِ، برای … و کاربرد فارسی نو: نشانهٔ مفعول بی‌واسطه»، و می‌افزاید «پارسی باستان rād- در rādiy، پارتی rʾd، فارسی میانه rʾy، پازند و فارسی نو rā». هُرن نیز در شمارهٔ ۶۰۰ (صفحهٔ ۱۳۴) همین را می‌گوید و توضیح می‌دهد که کاربرد نشانهٔ مفعولی از معنی نخستین «برای، به سبب» برآمده است. «چرا» ترکیب روشن «چه + را» است، یعنی «برای چه؟»، که ساختی است از دورهٔ فارسی میانه (čē rād). گزارهٔ نورایی کاملاً درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7\",\n            \"https://en.wiktionary.org/wiki/%DA%86%D8%B1%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"NYB:164\",\n              \"status\": \"supports\",\n              \"note\": \"Nyberg, Manual of Pahlavi II, p. 164 (NYB_vol2_glossary.txt; the running head 'rad 164' stands immediately before the entry): '²rād [lʾd; inscr. and Ps. rʾdy] postpos. 1. for the sake of, because of, for, on behalf of ... ham cim ~ for that very reason ... čē rād why? ... — OP rād- \\\"reason, cause\\\" in rādiy postpos. \\\"on account of\\\", avahya-rādiy \\\"for this reason\\\"; MPrth rʾd, MPrs rʾy; Paz. NP rā.' Exactly Nourai's arrow, and it also documents čerā.\"\n            },\n            {\n              \"ref\": \"BQT:926\",\n              \"status\": \"not_found\",\n              \"note\": \"Checked BQT_v2_pages.txt leaves 383-390 (printed pp. ≈ 926-933, the opening of حرف الراء, 'گفتار دهم ... در حرف رای بی‌نقطه'): the first entries are رابو، راتیانج، راح، راد، راز ... There is no headword را as a postposition and no etymological footnote on را in that range.\"\n            },\n            {\n              \"ref\": \"AEF:250\",\n              \"status\": \"not_checked\",\n              \"note\": \"Khaleqi Motlaq's Asās-e Eshteqāq-e Fārsi (the Persian translation of Horn+Hübschmann) is not online; refs_online.json marks it 'catalog' only. Its German original, Horn no. 600, is quoted under consulted.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 600, p. 134 (HRN.txt)\",\n              \"stance\": \"supports\",\n              \"note\": \"'600. rā, zur Bezeichnung des Objekts dienende Partikel, rāi \\\"wegen\\\", barāy, az bahr-i rā. ap. rād- in -rādiy \\\"wegen\\\"; phlv. rāδ, rāi (Gemme, ZDMG. 44, 676 No. 141). afgh. lar, lara (beim Dativ); kurd. ārāi \\\"für\\\". Aus der ursprünglichen Bedeutung \\\"für, wegen, was anlangt\\\" erklärt sich auch das Vorkommen von rā vor dem Nominativ.'\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"p. 164 s.v. ²rād\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 2 leaves 383-390\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry for the postposition را.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Greek\",\n          \"words\": \"harmos; arthro-itis; arithmus; logos-arithmus; arma\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Four of the five items are sound, one gloss is wrong and one 'Greek' word is not Greek. (a) ἁρμός harmós 'joint, fastening' < *h₂er-smo-, and its derivatives ἁρμόζω 'fit together', ἁρμονία 'joining, concord' — Pokorny 58-59 'gr. ἁρμός \\\"Fuge, Zusammenfügung, Gelenk\\\" ... ἁρμονία \\\"Verbindung, Bund, Ebenmaß, Einklang\\\"'; Watkins 'Suffixed form *arə-smo- in Greek harmos, joint, shoulder: HARMONY'. (b) ἄρθρον árthron 'joint' < *h₂er-dhro- + the Greek disease-suffix -ῖτις, hence ἀρθρῖτις 'arthritis' — Watkins 'Suffixed form *arə-dhro- in Greek arthron, joint: ARTHRO-'. (c) ἀριθμός arithmós 'number' — Watkins does place it here ('Variant (or separate root) *rī-. 2. Suffixed form *(ə)rī-dhmo- in Greek arithmos: ARITHMETIC, LOGARITHM') and Pokorny 61 lists it under the (ə)rī-, rei- base of ar-, but Klein derives it 'fr. I.-E. base *rī-, \\\"to count, number\\\"' and Etymonline from '*erei-dhmo-, suffixed variant form of root *re- \\\"to reason, count\\\"' — i.e. a base most current authorities keep separate from *h₂er-. (d) 'logos-arithmus' is not a Greek word at all: logarithmus is John Napier's Neo-Latin coinage of 1614 (Mirifici logarithmorum canonis descriptio) from λόγος 'ratio' + ἀριθμός 'number'; putting it in a Greek box is an anachronism. (e) ἅρμα hárma is a real Greek word, but it means 'chariot, war-car' (Pokorny 59: 'gr. ἅρμα \\\"Wagen\\\"'), not 'arms, weapons'; 'arms, weapons' is Latin arma, -ōrum, which Pokorny lists on the same page and which Watkins files under I.1.b. Nourai has given the Greek word the Latin word's meaning — and it is that mistake that lets him hang the Arabic 'chariot' branch and English arms/army/alarm off this box.\",\n          \"derivation_fa\": \"چهار مورد از پنج مورد این جعبه درست است، یک معنی نادرست است و یک واژه اصلاً یونانی نیست. ἁρμός «بند، درزِ به‌هم‌پیوسته» از *h₂er-smo- و مشتق آن ἁρμονία «هماهنگی» درست است (پوکورنی صفحات ۵۸ و ۵۹؛ واتکینز). ἄρθρον «مفصل» از *h₂er-dhro- با پسوند بیماری‌ساز یونانی ‑ῖτις به ἀρθρῖτις «آرتریت» رسیده و آن هم درست است. ἀριθμός «شمار» را واتکینز و پوکورنی ذیل همین ریشه (پایهٔ (ə)rī-) آورده‌اند، ولی کلاین و اتیمانلاین آن را به پایهٔ جداگانهٔ *rī-/*rē- «شمردن، اندیشیدن» می‌برند؛ پس با احتیاط پذیرفتنی است. «logos-arithmus» یونانی نیست: logarithmus ساختهٔ لاتینی نو جان نِیپِر در سال ۱۶۱۴ میلادی است از λόγος «نسبت» و ἀριθμός «عدد». و سرانجام ἅρμα در یونانی «ارابه، گردونهٔ جنگی» است نه «سلاح»؛ معنی «سلاح» از آنِ arma لاتینی است. همین جابه‌جایی معنایی است که به نورایی اجازه داده شاخهٔ عربی «ارابه» و نیز arms/army/alarm انگلیسی را از این جعبه بیاویزد.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/harmony\",\n            \"https://www.etymonline.com/word/arithmetic\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. ar-: '2. Suffixed form *arə-smo- in Greek harmos, joint, shoulder: HARMONY ... 6. Suffixed form *arə-dhro- in Greek arthron, joint: ARTHRO- ... IV.2. Suffixed form *(ə)rī-dhmo- in Greek arithmos, number, amount: ARITHMETIC, LOGARITHM.' Nourai's Greek box is a transcription of these lines — but Watkins lists arma under 'b. Latin arma, tools, arms', not under Greek.\"\n            },\n            {\n              \"ref\": \"POK\",\n              \"status\": \"partial\",\n              \"note\": \"POK_01.txt leaf 66/67 (pp. 58-59): 'gr. ἁρμός \\\"Fuge, Zusammenfügung, Gelenk\\\" ... (ἁρμόζω \\\"verbinde, füge zusammen\\\", ἁρμονία \\\"Verbindung, Bund, Ebenmaß, Einklang\\\"), ἅρμα \\\"Wagen\\\" ... lat. arma, -ōrum \\\"Gerätschaften, Rüstzeug, Waffen\\\"'; leaf 69 (p. 61): 'ἀριθμός \\\"Zahl\\\"'. Pokorny thus supports every form but glosses ἅρμα 'Wagen' (chariot), contradicting Nourai's 'arms, weapons'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. ar-\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW pp. 58-59, 61\",\n              \"stance\": \"partial\",\n              \"note\": \"See ref_check; ἅρma is 'Wagen'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. harmony, arithmetic\",\n              \"stance\": \"partial\",\n              \"note\": \"'harmony, n. — ME. harmonie, fr. F. harmonie, fr. L. harmonia, fr. Gk. ἁρμονία \\\"a fitting together, joining, proportion, concord\\\" ... fr. I.-E. base *ar-, \\\"to join\\\"' — supports. But 'arithmetic, n. — ... fr. Gk. ἀριθμός \\\"number\\\", fr. I.-E. base *rī-, \\\"to count, number\\\"' — Klein separates arithmos from *ar-.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, searched harmos / arithmos\",\n              \"stance\": \"silent\",\n              \"note\": \"Nothing retrievable from the OCR.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"French\",\n          \"words\": \"harmonie; arthrose; logarithme\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are the ordinary learned French continuations. harmonie: Old French harmonie / armonie (12th c.), a Latinism taken from Latin harmonia, itself the Greek loan ἁρμονία; Klein: 'harmony, n. — ME. harmonie, fr. F. harmonie, fr. L. harmonia, fr. Gk. ἁρμονία'. arthrose: a 19th-20th c. French medical neologism (osteo-arthrose), Greek ἄρθρον 'joint' + the pathology suffix -ose (Greek -ωσις) used in French for non-inflammatory degenerative conditions, deliberately opposed to arthrite (-ῖτις, inflammatory). logarithme: French adaptation of Napier's Neo-Latin logarithmus (1614), current in French from the 1620s. Only the middle and last of these three actually pass through Greek as words; arthrose and logarithme are modern European coinages made out of Greek material.\",\n          \"derivation_fa\": \"هر سه واژه صورت‌های عالمانهٔ فرانسوی‌اند. harmonie از فرانسوی کهن (سدهٔ دوازدهم میلادی) و آن وام از harmonia لاتینی است که خود وام‌واژهٔ یونانی ἁρμονία است؛ کلاین همین زنجیره را می‌آورد. arthrose ساخته‌ای است پزشکی در فرانسهٔ سدهٔ نوزدهم و بیستم از ἄρθρον یونانی «مفصل» با پسوند ‑ose (از ‑ωσις یونانی) که در فرانسه برای بیماری‌های فرسایشیِ غیرالتهابی به کار می‌رود، در برابر arthrite با پسوند التهابی ‑ite. logarithme نیز برگردان فرانسوی logarithmus لاتینی نوِ نِیپِر (۱۶۱۴ میلادی) است. پس تنها harmonie واقعاً از راه یونانی به فرانسه رسیده و دو تای دیگر ساخته‌های نوِ اروپایی از مصالح یونانی‌اند. ادعای نورایی دربارهٔ این گره درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/harmony\",\n            \"https://www.etymonline.com/word/arithmetic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference for this node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. harmony\",\n              \"stance\": \"supports\",\n              \"note\": \"'ME. harmonie, fr. F. harmonie, fr. L. harmonia, fr. Gk. ἁρμονία' — the French link is explicit.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins s.v. ar-, II/IV\",\n              \"stance\": \"supports\",\n              \"note\": \"Lists HARMONY and LOGARITHM among the English reflexes, which reach English through French.\"\n            },\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale\",\n              \"stance\": \"silent\",\n              \"note\": \"None of the three is oriental, so Devic (and Pihan) have nothing on them — as expected.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Persian\",\n          \"words\": \"hârmonî; ârtotoz; logaritm\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The three words are genuine 20th-century French loans in Persian and the arrows are right, but the second transliteration is corrupt. هارمونی hārmoni ← French harmonie (musical term, borrowed with the Western conservatoire vocabulary from the 1930s; Mo'in has هارمونی as a headword, '(مس.) صداهایی که ... با هم تناسب و ارتباط داشته باشد؛ هماهنگی'). لگاریتم logāritm ← French logarithme, in Persian from the modern mathematics curriculum; Mo'in tags it '[فر.]' (French). آرتروز ← French arthrose, a 20th-century medical loan; the Persian is pronounced ārt(e)rōz. But the book prints the transliteration 'ârtotoz', which cannot correspond to آرتروز: it has -to- where the script has -ro- (ر). This is a misprint in the book itself, not an extraction error — the 450-dpi rendering of pdf page 62 clearly shows 'ârtotoz' next to آرتروز. Separately, and this one IS an extraction slip: the book prints 'logârîtm' (with both circumflexes) while the JSON has 'logaritm'.\",\n          \"derivation_fa\": \"هر سه واژه وام‌واژه‌های فرانسویِ سدهٔ بیستم در فارسی‌اند و پیکان‌ها درست است، اما آوانویسی دومی خراب است. «هارمونی» از harmonie فرانسوی است و از راه آموزش موسیقی غربی از دههٔ ۱۳۱۰ خورشیدی وارد شده؛ معین آن را با معنی «هماهنگی» سرواژه کرده است. «لگاریتم» از logarithme فرانسوی است و معین آن را با برچسب «[فر.]» آورده است. «آرتروز» نیز از arthrose فرانسوی و وامی پزشکی است و تلفظ آن ārt(e)rōz است؛ ولی کتاب آوانویسی «ârtotoz» را چاپ کرده که با «آرتروز» نمی‌خواند، زیرا به‌جای «ر» یک «ت» دارد. با نگاه به تصویر صفحهٔ چاپی روشن شد که این غلط از خودِ کتاب است نه از استخراج داده؛ در عوض «logârîtm» کتاب در فایل داده به «logaritm» بدل شده که خطای استخراج است. حکم: خطای چاپی کتاب.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"ârtotoz\",\n          \"correct_form\": \"ârterōz (ârtrōz), Persian آرتروز, from French arthrose\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/%D9%84%DA%AF%D8%A7%D8%B1%DB%8C%D8%AA%D9%85\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:3619,5082\",\n              \"status\": \"not_checked\",\n              \"note\": \"The 6-volume Mo'in pagination cannot be checked: only the 2-volume Adena abridgement (MON_part1/2) is on disk and the online copies (vajehyab, abadis) carry entry text without page numbers. The entries themselves exist: MON_part2 has 'هارمونی: (ا.) (مس.) صداهای ... با هم تناسب و ارتباط داشته باشد؛ هماهنگی' and لگاریتم appears in the definitions of مانتیس and مفسر.\"\n            },\n            {\n              \"ref\": \"AMD:24\",\n              \"status\": \"not_checked\",\n              \"note\": \"Amid's 2-volume 1369 print is not paginated online (refs_online.json: 'page numbers of the 2-vol 1369 print not mappable').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part2 s.v. هارمونی; vajehyab/Mo'in s.v. لگاریتم\",\n              \"stance\": \"supports\",\n              \"note\": \"Mo'in s.v. لگاریتم: '(لُ) [فر.] (اِ.) نمادی است در ریاضی ...' — the '[فر.]' tag is Mo'in's own mark for a French loan.\"\n            },\n            {\n              \"src\": \"AMD\",\n              \"where\": \"Amid via vajehyab/abadis\",\n              \"stance\": \"silent\",\n              \"note\": \"Amid carries the same words with the same [فرانسوی] tag but no page reference is recoverable.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Arabic\",\n          \"words\": \"arbah, arobeh\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Arabic word intended is عَرَبَة ʿaraba(t), pl. ʿarabāt, 'cart, wagon' (Nourai's 'arbah, arobeh' transliterates it, and its Persianised عربه, without marking the initial ʿayn). It cannot come from Greek ἅρμα: a Greek initial h-/spiritus asper is never rendered by Arabic ʿayn, and the Greek stem is harm-, not ʿ-r-b. Modern references route the word the other way and outside Greek altogether. Lokotsch's Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs no. 90 files it as Turkish: 'Tk. araba: [Mit falscher arabisierender Schreibung ʿaraba] \\\"Wagen\\\", arabagï \\\"Kutscher, Fuhrmann\\\"' — i.e. the Arabic spelling with ʿayn is a false Arabicising orthography of a Turkish word (whence also Romanian araba, Russian arba, Serbian araba). Wiktionary's Turkish araba: 'Inherited from Ottoman Turkish عربه (araba). Ultimate origin uncertain', with Arabic عَرَبَة listed among the borrowings out of Turkic. Asbaghi's Persische Lehnwörter im Arabischen treats ʿarāba as a Persian loan in Arabic ('ʿarāba: \\\"Wagen\\\" pers., die arabisierte Form heißt عربه araba u. ʿarabāna, davon russ. serb. arab \\\"Wagen\\\"') and reports the Bahār-e ʿAjam view that the real word behind it is ʿarrāda 'Geschützlafette, Wurfgeschoßrad'. Vámbéry's Turco-Tatar dictionary already has Chagatai adak araba 'Gehwagen, Rollwagen'. No source consulted connects it to *h₂er-.\",\n          \"derivation_fa\": \"واژهٔ عربی مورد نظر «عَرَبة» (جمع: عَرَبات) به معنی «گاری، گردونه» است؛ آوانویسی «arbah, arobeh» در کتاب همان است بدون نشان‌دادن «ع». این واژه نمی‌تواند از ἅρμα یونانی آمده باشد، زیرا «ه»ی دمیدهٔ یونانی هرگز در عربی به «ع» بدل نمی‌شود و ستاک یونانی harm- است نه ع‑ر‑ب. مآخذ امروزی مسیر را وارونه و بیرون از یونانی می‌دانند: لوکوچ در شمارهٔ ۹۰ آن را واژه‌ای ترکی می‌شمارد و می‌نویسد املای عربیِ «عربه» «املای عربی‌نمای نادرست» است؛ ویکی‌واژه ریشهٔ ترکی araba را «نامعلوم» می‌داند و عربیِ عَرَبة را وام‌گرفته از ترکی می‌آورد؛ اصباغی در «وام‌واژه‌های فارسی در عربی» عَرابه را وام فارسی در عربی می‌داند و رأی «بهار عجم» را نقل می‌کند که اصل آن «عرّاده» است؛ وامبری هم چغتایی adak araba را ثبت کرده است. هیچ مأخذی آن را به ریشهٔ *h₂er- نمی‌رساند؛ پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/araba\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:96\",\n              \"status\": \"partial\",\n              \"note\": \"BQT_v1_pages.txt leaf 306 (printed p. 96 on the scan's leaf−210 mapping; the running-head text matches) has only the Persian headword: 'ارابه - بر وزن فرابه، گردون را گویند' — 'ārābe, on the pattern of farābe: they call a chariot'. There is no Arabic form, no ʿayn, no Greek and no Mo'in etymological footnote on the entry, so the page cannot support an Arabic node at all.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch no. 90 (LKT.txt)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'90. Tk. araba: [Mit falscher arabisierender Schreibung ʿaraba] \\\"Wagen\\\", arabagï \\\"Kutscher, Fuhrmann\\\". Hieraus rum. araba, haraba \\\"Leiterwagen\\\" ...; russ. arba, ukr. harba, bulg. serb. araba \\\"Wagen\\\".' Lokotsch files the word under Turkish and calls the Arabic spelling false.\"\n            },\n            {\n              \"src\": \"PLA\",\n              \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, s.v. ʿarāba\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'ʿarāba: \\\"Wagen\\\" pers., die arabisierte Form heißt عربه araba u. ʿarabāna, davon russ. serb. arab \\\"Wagen\\\". Der Verfasser v. Bahār ul-ʿAǰam ist der Ansicht, daß araba eigentl. ʿarrāda \\\"Geschützlafette, Wurfgeschoßrad\\\" heißt. Vgl. ap. rāda, aw. raθa, mand. arada.' Asbaghi makes the Arabic word a loan FROM Persian and compares Av. raθa- 'chariot' (root *Hret-), not *h₂er-.\"\n            },\n            {\n              \"src\": \"TTS\",\n              \"where\": \"Vámbéry no. 27 (TTS_vambery1878_uoft_djvu.txt)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'čag. ajak; adak araba = Gehwagen, Rollwagen, mittelst dessen die Kinder gehen lernen' — araba is used as an ordinary Chagatai word for 'wheeled vehicle'.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir, Kitāb al-alfāẓ al-fārisiyya al-muʿarraba, searched عربة / عرابة / عراده\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry for the word among Addi Shir's Persian Arabicisms in the OCR.\"\n            },\n            {\n              \"src\": \"FVQ\",\n              \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\",\n              \"stance\": \"silent\",\n              \"note\": \"The word is not Qur'anic and Jeffery has no entry.\"\n            }\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Persian\",\n          \"words\": \"arrâbeh\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Persian word is real: ارابه arrābe / ārābe 'cart, wagon, war-chariot', in Borhan-e Qate' (p. 96) 'ارابه - بر وزن فرابه، گردون را گویند' and in Mo'in '(اَ رّ بِ) (اِ.) گاری با دو چرخ که از چوب می‌ساختند و برای حمل بار از آن [استفاده می‌کردند]'. Nourai's parenthetical عرّاده is the rival spelling Dehkhoda records (Arabic ʿarrāda 'mangonel, siege engine, gun-carriage'), and Mo'in's اراده entry likewise cross-refers 'قس. عراده'. What is wrong is the route. Wiktionary derives Persian ارابه straight from Turkic: 'Borrowed from Turkic, from the same source as Turkish araba' (with the Tajik doublet ароба). Asbaghi runs it the opposite way, Persian → Arabic ʿarāba, and offers as the older Iranian comparison Av. raθa- / OP *rāda 'chariot' — a word of PIE *Hroth₂o- 'wheel' from the root *Hret- 'to run', which has nothing to do with *h₂er- 'to fit together'. Neither Borhan-e Qate' nor Mo'in nor Dehkhoda gives any Greek or Arabic origin tag. Greek ἅρμα → Arabic ʿaraba → Persian arrābe is therefore an etymology unique to Nourai, and it is phonetically impossible on the Arabic side (see node 11).\",\n          \"derivation_fa\": \"خودِ واژهٔ «ارابه» اصیل و ثبت‌شده است: برهان قاطع در صفحهٔ ۹۶ می‌نویسد «ارابه ـ بر وزن فرابه، گردون را گویند» و معین آن را «گاری دوچرخ چوبی برای حمل بار» معنی می‌کند؛ صورت «عرّاده» که نورایی در کمانک آورده همان املای رقیبی است که دهخدا یاد می‌کند (عربیِ عرّاده «منجنیق، ارابهٔ توپ») و معین نیز ذیل «اراده» می‌نویسد «قس. عراده». آنچه نادرست است مسیر اشتقاق است. ویکی‌واژه «ارابه» را وام‌واژه‌ای از ترکی می‌داند، هم‌ریشه با araba ترکی (و دوگانهٔ تاجیکی «ароба»). اصباغی راه را وارونه می‌بیند (فارسی ← عربی عَرابه) و برای مقایسه raθa- اوستایی و *rāda پارسی باستان «گردونه» را پیش می‌کشد که از ریشهٔ *Hret- «دویدن/چرخیدن» است نه *h₂er-. نه برهان، نه معین و نه دهخدا هیچ نشانِ یونانی یا عربی برای این واژه نمی‌دهند. پس زنجیرهٔ «harma یونانی ← عربة ← ارابه» ویژهٔ نورایی است و پژوهش امروزی آن را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%A7%D8%A8%D9%87\",\n            \"https://abadis.ir/fatofa/%D8%A7%D8%B1%D8%A7%D8%A8%D9%87/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:96\",\n              \"status\": \"partial\",\n              \"note\": \"BQT_v1_pages.txt leaf 306 (printed p. 96): 'ارابه - بر وزن فرابه، گردون را گویند' — the word and the gloss 'chariot/cart' are exactly as Nourai has them, but the page carries no etymology and no Arabic/Greek antecedent, so it supports only the existence of the Persian word, not the arrow.\"\n            },\n            {\n              \"ref\": \"MON:2286\",\n              \"status\": \"not_checked\",\n              \"note\": \"6-volume Mo'in pagination unavailable (see node 10). The entry itself, via abadis: 'فرهنگ معین: (اَ رّ بِ) (اِ.) گاری با دو چرخ که از چوب می‌ساختند و برای حمل بار از آن' — no origin tag, i.e. Mo'in treats it as native Persian.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 1 p. 96 (leaf 306)\",\n              \"stance\": \"partial\",\n              \"note\": \"Word confirmed, etymology absent.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in via abadis s.v. ارابه; MON_part1 s.v. اراده\",\n              \"stance\": \"partial\",\n              \"note\": \"Mo'in's ارابه has no origin tag; his اراده entry reads '[قس. است. گردونه، چرخ، قس. عراده] (اِ.) گردونه، ارابه' — he compares عراده, never Greek.\"\n            },\n            {\n              \"src\": \"PLA\",\n              \"where\": \"Asbaghi s.v. ʿarāba\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Persian → Arabic, with Av. raθa- / OP rāda offered as the Iranian comparison.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch no. 90\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Turkish araba, the Arabic ʿaraba spelling 'falsch arabisierend'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"harmony, arthritis, arithmetic, logarithm, arms, army, alarm\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All seven words are listed by Watkins under ar-, so the root attribution is his; but the chart's arrow, which makes them all descend from the Greek box, is right for only four of them. harmony (late 14c.) ← Old French harmonie ← Latin harmonia ← Greek ἁρμονία; arthritis (1540s) ← Latin arthritis ← Greek ἀρθρῖτις; arithmetic (mid-13c. arsmetike) ← Old French arismetique ← Latin arithmetica ← Greek ἀριθμητική (τέχνη); logarithm (1610s) ← Napier's Neo-Latin logarithmus. But arms (early 14c.) and army (late 14c.) come from Latin arma through French — Klein: 'army, n. — F. armée, fr. L. armata, fem. pp. of armare, \\\"to furnish with weapons\\\"'; Etymonline: 'Latin arma \\\"tools, arms\\\" ... PIE *ar(ə)mo-, suffixed form of root *ar- \\\"to fit together\\\"' — and alarm (late 14c.) is Old French alarme from Italian all'arme! 'to (the) arms!', again Latin arma. None of the last three touches Greek. Note also that Etymonline and Klein trace arithmetic to a base *re-/*rī- 'to reason, count' rather than to *ar- proper.\",\n          \"derivation_fa\": \"هر هفت واژه در پیوست واتکینز ذیل همین ریشه آمده‌اند، پس نسبت‌دادن آنها به ریشه از آنِ اوست؛ اما پیکان نمودار که همه را از جعبهٔ یونانی می‌آویزد تنها دربارهٔ چهار واژه درست است. harmony از فرانسوی کهن و لاتینی و در نهایت ἁρμονία یونانی؛ arthritis از ἀρθρῖτις یونانی از راه لاتینی؛ arithmetic از فرانسوی کهن arismetique و لاتینی arithmetica از یونانی؛ و logarithm از logarithmus لاتینی نو. ولی arms و army از arma لاتینی از راه فرانسه آمده‌اند (کلاین: army از armée فرانسوی، از armata لاتینی) و alarm از all'arme ایتالیایی «به سلاح!» است که آن هم به arma لاتینی برمی‌گردد؛ هیچ‌یک از این سه به یونانی نمی‌رسد. افزون بر این، کلاین و اتیمانلاین ریشهٔ arithmetic را پایهٔ جداگانهٔ *rī-/*rē- «شمردن» می‌دانند. پس این گره با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/army\",\n            \"https://www.etymonline.com/word/harmony\",\n            \"https://www.etymonline.com/word/arithmetic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference for this node; the material is Watkins' (see the parent Greek box, refs 'AHD; POK').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. harmony, arithmetic, army\",\n              \"stance\": \"partial\",\n              \"note\": \"'army, n. — F. armée, fr. L. armata, fem. pp. of armare, \\\"to furnish with weapons\\\". See armada' — Latin, not Greek. 'arithmetic ... fr. I.-E. base *rī-, \\\"to count, number\\\"' — a base Klein keeps apart from *ar-.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins s.v. ar-\",\n              \"stance\": \"supports\",\n              \"note\": \"All seven English words appear in the entry (ARM², ARMY, ALARM under 'Latin arma'; HARMONY, ARTHRO-, ARITHMETIC, LOGARITHM under the Greek forms).\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, searched READ/ARM/ARMY\",\n              \"stance\": \"silent\",\n              \"note\": \"The one-volume Concise Skeat on disk yielded no retrievable entry for these headwords in the OCR.\"\n            }\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Latin\",\n          \"words\": \"ars; reri; ôrdô\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two of the three are secure, the third is contested. (a) ars, gen. artis 'skill, craft' is *h₂er-ti-, formally the exact match of Skt. r̥tí- 'manner' and Middle High German art; Pokorny 58: 'lat. ars, -tis \\\"die Geschicklichkeit, Kunst, Art und Weise\\\" (eigentlich \\\"Zusammenfügung, Gabe richtig zusammenzufügen\\\" = mhd. art)'; Watkins '*arə-ti- in Latin ars (stem art-), art, skill, craft'. (b) reor, rērī 'to reckon, think', p.p. ratus, whence ratiō 'reckoning, reason' — Pokorny 59 puts them under the variant *rē-, rō-, with the nice observation that 'das primitivste Zählen wird vom Aufeinanderlegen oder -schichten der zu zählenden Stücke begleitet'. (c) ōrdō, -inis 'row, order', with ōrdior 'to begin to weave' — Nourai's gloss 'row of threads in loom' is Watkins' own wording ('Latin ōrdō, order (originally a row of threads in a loom)'), but Watkins prefixes it 'Possibly suffixed variant form (or separate root) *ōr-dh-', Pokorny 61 introduces the whole group with 'Trifft der Zusammenhang mit ar- \\\"fügen\\\" ... zu' (i.e. 'if the connection holds'), and Etymonline calls the *ar- origin 'uncertain', preferring Proto-Italic *ordn- 'row, order'. Hence the node as a whole is plausible rather than confirmed.\",\n          \"derivation_fa\": \"دو واژه از سه واژهٔ این جعبه استوارند و سومی محل بحث. نخست ars (اضافی artis) «هنر، مهارت» از *h₂er-ti- که همتای دقیق r̥tí- سنسکریت و art آلمانی میانه است؛ پوکورنی در صفحهٔ ۵۸ معنی بنیادین آن را «به‌هم‌پیوستن، توانِ درست جفت‌وجورکردن» می‌داند. دوم reor/rērī «شمردن، پنداشتن» با اسم مفعول ratus و مشتق ratiō «شمار، خرد»، که پوکورنی در صفحهٔ ۵۹ ذیل گونهٔ *rē-, rō- آورده و می‌افزاید که ابتدایی‌ترین شمارش با روی‌هم‌نهادن چیزها همراه بوده است. سوم ōrdō «رده، نظم» با فعل ōrdior «آغاز به بافتن»؛ معنیِ «رشته‌های تار در کارگاه بافندگی» که نورایی نوشته عیناً عبارت واتکینز است، ولی واتکینز خود می‌افزاید «شاید گونه‌ای از ریشه یا ریشه‌ای جداگانه»، پوکورنی در صفحهٔ ۶۱ با «اگر پیوند با ar- درست باشد» آغاز می‌کند و اتیمانلاین این پیوند را «نامطمئن» می‌خواند. از این‌رو حکم این گره «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/order\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. ar-: '3. Suffixed form *arə-ti- in: a. Latin ars (stem art-), art, skill, craft: ART, ARTEL, ARTISAN, ARTIST; INERT ... II. Possibly suffixed variant form (or separate root) *ōr-dh-. 1. Latin ōrdō, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL ... III. Variant or separate root *rē- (< *reə-). 1. Latin rērī (past participle ratus), to consider, confirm, ratify: RATE, RATIO, REASON.' All three of Nourai's Latin words, and his ōrdō gloss verbatim — but with Watkins' hedges removed.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW pp. 58, 59, 61\",\n              \"stance\": \"partial\",\n              \"note\": \"p. 58 'lat. artus \\\"eng in Raum und Zeit\\\" ... ars, -tis \\\"die Geschicklichkeit, Kunst\\\"'; p. 59 'Lat. reor, rērī \\\"berechnen, meinen, dafürhalten\\\" ... ratiō'; p. 61 files ōrdior/ōrdō here only conditionally ('Trifft der Zusammenhang mit ar- \\\"fügen\\\" ... zu, so wäre der Vokal von *or-d-eiō als Kausativ-Iterativ-Vokalismus zu rechtfertigen').\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 74\",\n              \"stance\": \"supports\",\n              \"note\": \"'Lat. reor, rērī \\\"berechnen, meinen, dafürhalten\\\" (das primitivste Zählen wird vom Aufeinanderlegen oder -schichten der zu zählenden Stücke begleitet), Ptc. ratus ... ratio \\\"Berechnung, Erwägung, Vernunft, Beweggrund, Grund\\\"' — this is in fact the page Nourai cites as WLD:74 for the Avestan and Old Persian nodes.\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet s.v. ordior\",\n              \"stance\": \"partial\",\n              \"note\": \"'ordior, -īris, orsus sum ... ourdir [une trame], commencer à tisser; puis par extension \\\"commencer, entreprendre\\\" ... Le sens de \\\"commencer\\\" a dû se développer par un rapprochement de orior et de ordior' — Ernout-Meillet describe the weaving sense (Nourai's gloss) but do not commit to *ar-.\"\n            },\n            {\n              \"src\": \"LEW\",\n              \"where\": \"Walde 1910, searched ars/artis\",\n              \"stance\": \"silent\",\n              \"note\": \"The 1910 scan's OCR yielded no retrievable ars entry.\"\n            }\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An unlabelled pass-through box standing for French art and artiste. Old French art (11th c.) is the direct popular continuation of Latin ars, accusative artem (with the regular loss of Latin final -m and of the unstressed final syllable); modern French art keeps the form. artiste is a 16th-century borrowing into French of Italian artista, itself Medieval Latin artista 'one skilled in the (liberal) arts', a -ista derivative of ars, artis. Klein: 'artist, n. — F. artiste, fr. It. artista, which is formed fr. L. ars gen. artis, \\\"art\\\". See art and -ist.' The two words then go on to English (node 17) and to Persian (node 16).\",\n          \"derivation_fa\": \"این جعبهٔ بی‌واژه نمایندهٔ art و artiste فرانسوی است. art فرانسوی کهن (سدهٔ یازدهم میلادی) دنبالهٔ مستقیم و مردمیِ artem لاتینی (حالت مفعولی ars) است، با افتادن «م» پایانی و هجای بی‌تکیهٔ آخر که در گذر لاتین به فرانسوی قاعده است. artiste وامی است در سدهٔ شانزدهم از artista ایتالیایی، و آن خود از artista لاتینی میانه «آشنا به هنرهای آزاد» است، ساخته با پسوند ‑ista از ars/artis. کلاین همین را می‌گوید. این دو واژه سپس به انگلیسی (گرهٔ ۱۷) و به فارسی (گرهٔ ۱۶) راه یافته‌اند. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. ar- I.3.a lists 'ART, ARTEL, ARTISAN, ARTIST' as the English reflexes of Latin ars — all of which reach English through French, which is what this box represents.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. art, artist\",\n              \"stance\": \"supports\",\n              \"note\": \"'art, n. — OF. (= F.), fr. L. artem, acc. of ars, \\\"skill, handicraft, trade, occupation, art\\\", which is rel. to L. artus, \\\"joint\\\"'; 'artist, n. — F. artiste, fr. It. artista, which is formed fr. L. ars gen. artis, \\\"art\\\".'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins s.v. ar-\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check.\"\n            }\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Persian\",\n          \"words\": \"ârtîst\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"آرتیست ārtist is a direct 20th-century borrowing of French artiste, taken over with the imported theatre and cinema (the word is at home in Persian from the 1300s Sh./1920s-30s onward, and in colloquial Persian it has developed the extra sense 'poseur, one who plays a part to get his way'). The French final -e is not represented in Persian; the initial ā- is written آ; the -is- of artiste is kept as ـیس, which shows the loan came through the French spelling/pronunciation rather than through English artist (which would have given *ârtist with a different vowel value in the second syllable). Mo'in tags the word '[فر.]', his own mark for a French loan: '[فر.] (ص.) هنرمند، هنرپیشه؛ کنایه از: آدمی که برای رسیدن به خواسته‌هایش نقش بازی کند'.\",\n          \"derivation_fa\": \"«آرتیست» وام‌واژه‌ای است مستقیم از artiste فرانسوی که در سدهٔ بیستم همراه با تئاتر و سینما وارد فارسی شد و از دههٔ ۱۳۰۰ خورشیدی به بعد کاربرد یافت؛ در فارسی گفتاری معنی افزوده‌ای هم پیدا کرده است: «کسی که برای رسیدن به خواستهٔ خود نقش بازی می‌کند». «ـه»ی پایانی فرانسوی در فارسی بازتاب نیافته، «آ» آغازین با الف مدّه نوشته شده و بخش «ـیس» نشان می‌دهد که وام‌گیری از راه فرانسوی بوده نه انگلیسی. معین این واژه را با برچسب «[فر.]» یعنی «فرانسوی» آورده است: «[فر.] (ص.) هنرمند، هنرپیشه». پس ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/%D8%A2%D8%B1%D8%AA%DB%8C%D8%B3%D8%AA\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:41\",\n              \"status\": \"partial\",\n              \"note\": \"The entry exists and says what Nourai needs — Mo'in s.v. آرتیست: '[فر.] (ص.) هنرمند، هنرپیشه' — but the page number cannot be verified: only the 2-volume Adena abridgement is on disk and the online Mo'in (vajehyab/abadis) carries no pagination. p. 41 is at least alphabetically plausible, since آر- falls in the first pages of vol. 1.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in via vajehyab s.v. آرتیست\",\n              \"stance\": \"supports\",\n              \"note\": \"The '[فر.]' origin tag is Mo'in's explicit statement that the word is French.\"\n            },\n            {\n              \"src\": \"AMD\",\n              \"where\": \"Amid via vajehyab/abadis\",\n              \"stance\": \"supports\",\n              \"note\": \"Amid likewise marks آرتیست as [فرانسوی]; no page reference recoverable.\"\n            }\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"English\",\n          \"words\": \"art, artist\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"art entered Middle English about 1200 from Old French art, from Latin artem (nominative ars) 'skill, craft, trade'; the sense narrowed from 'skill acquired by learning' (still in 'the liberal arts', 'artful') to 'fine art' only in the 18th century. artist is first recorded in the 1580s, from French artiste (Italian artista, Medieval Latin artista), at first 'one skilled in the learned arts', then from the 17th century 'practitioner of the fine arts'. Klein: 'art, n. — OF. (= F.), fr. L. artem, acc. of ars ... which is rel. to L. artus, \\\"joint\\\", and cogn. with OI. r̥tíḥ \\\"manner, mode\\\", Gk. ἄρτι \\\"just\\\", ἄρτιος \\\"complete, perfect of its kind, suitable\\\"'; 'artist, n. — F. artiste, fr. It. artista, which is formed fr. L. ars gen. artis'.\",\n          \"derivation_fa\": \"«art» انگلیسی حدود سال ۱۲۰۰ میلادی از art فرانسوی کهن و آن از artem لاتینی (حالت فاعلی ars) «مهارت، پیشه، هنر» وارد انگلیسی میانه شد؛ معنی آن از «مهارتِ آموختنی» (که هنوز در ترکیب liberal arts مانده) در سدهٔ هجدهم به «هنرهای زیبا» محدود شد. «artist» نخستین بار در دههٔ ۱۵۸۰ میلادی از artiste فرانسوی (و آن از artista ایتالیایی و لاتینی میانه) به کار رفته و نخست به معنی «آشنا به دانش‌های آزاد» و از سدهٔ هفدهم به معنی «هنرمند» بوده است. کلاین همین زنجیره را می‌آورد و ars را با artus لاتینی «مفصل» و r̥tíḥ سنسکریت هم‌ریشه می‌داند. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. ar- I.3.a: 'Latin ars (stem art-), art, skill, craft: ART¹, ARTEL, ARTISAN, ARTIST; INERT, (INERTIA)' — precisely the two English words in Nourai's box.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. art, artist\",\n              \"stance\": \"supports\",\n              \"note\": \"See derivation; Klein gives OF → L. artem for art and F artiste → It. artista for artist.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins s.v. ar-\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check.\"\n            }\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"English\",\n          \"words\": \"order, coordinate, ordinary, reason, ratio, rate\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All six are Latinate and all six come from the two Latin stems in the parent box. From ōrdō, ōrdinis: order (c. 1200) ← Old French ordre ← Latin ōrdinem; ordinary (early 15c.) ← Latin ōrdinārius 'of the usual order'; coordinate (1640s) ← Medieval Latin coordinare 'to set in the same order' (co- + ōrdinare). From reor, ratus: reason (c. 1200) ← Old French raison ← Latin ratiōnem; ratio (1630s) is the Latin word taken over unchanged in its mathematical sense; rate (early 15c.) ← Old French rate ← Medieval Latin rata (pars) 'reckoned (part)', from ratus, the past participle of rērī. Watkins lists exactly this set: 'ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINATION, INORDINATE, SUBORDINATE' and 'RATE¹, RATIO, REASON; (ARRAIGN)'. (Whether ōrdō itself belongs to *h₂er- is the open question flagged at node 14; the Latin→English step charted here is not in doubt.)\",\n          \"derivation_fa\": \"هر شش واژه لاتینی‌تبارند و از همان دو ستاک جعبهٔ بالادست می‌آیند. از ōrdō/ōrdinis: order (حدود ۱۲۰۰ میلادی) از ordre فرانسوی کهن و ōrdinem لاتینی؛ ordinary (اوایل سدهٔ پانزدهم) از ōrdinārius لاتینی؛ coordinate (دههٔ ۱۶۴۰) از coordinare لاتینی میانه «در یک رده نهادن». از reor/ratus: reason (حدود ۱۲۰۰) از raison فرانسوی کهن و ratiōnem لاتینی؛ ratio (دههٔ ۱۶۳۰) خودِ واژهٔ لاتینی است که در معنی ریاضی وام گرفته شده؛ و rate (اوایل سدهٔ پانزدهم) از rata (pars) لاتینی میانه «بخشِ شمرده‌شده» از اسم مفعول ratus. واتکینز دقیقاً همین مجموعه را برمی‌شمارد. تنها پرسش باز، همان تردید دربارهٔ تعلق ōrdō به ریشهٔ *h₂er- است که در گرهٔ ۱۴ گفته شد؛ گذر از لاتینی به انگلیسی در اینجا تردیدی ندارد و ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/order\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference; the material comes from the parent Latin box (refs 'AHD').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins s.v. ar-, II.1 and III.1\",\n              \"stance\": \"supports\",\n              \"note\": \"'Latin ōrdō, order (originally a row of threads in a loom): ORDAIN, ORDER, ORDINAL, ORDINANCE, ORDINARY, ORDINATE, ORDO; COORDINATION, INORDINATE, SUBORDINATE'; 'Latin rērī (past participle ratus), to consider, confirm, ratify: RATE¹, RATIO, REASON'.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW pp. 59, 61\",\n              \"stance\": \"partial\",\n              \"note\": \"reor/ratio p. 59 firmly under the root; ōrdō p. 61 only conditionally.\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet s.v. ordior\",\n              \"stance\": \"partial\",\n              \"note\": \"Confirms the Latin weaving sense underlying ōrdō but not the PIE affiliation.\"\n            }\n          ]\n        },\n        {\n          \"id\": 19,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An unlabelled pass-through box for the two Germanic stems Watkins derives from this root: Proto-Germanic *armaz 'arm' (< PIE *h₂erH-mo- 'joint, upper arm', the exact match of Skt. īrmá-, Av. arəma-, Latin armus, Old Prussian irmo, OCS ramo) and Proto-Germanic *rēdaną 'to advise' (< the *rē-dh- variant), whence OHG rātan, Gothic garēdan, Old Norse ráða, Old English rǣdan. Pokorny 59 sets out the first ('B. Von der schweren Basis arə-mo-: r̥-mo- \\\"Arm\\\". Ai. īrmá-ḥ \\\"Arm, Vorderbug\\\" = av. arəma- \\\"Arm\\\" ... got. arms, ahd. usw. arm \\\"Arm\\\"') and p. 60 the second ('ahd. rātan \\\"raten, beratschlagen\\\" ... as. rādan, anord. ráda, ags. rǣdan (letzteres auch \\\"lesen\\\", engl. read)').\",\n          \"derivation_fa\": \"این جعبهٔ بی‌واژه نمایندهٔ دو ستاک ژرمنی است که واتکینز از این ریشه می‌گیرد: ژرمنی آغازین *armaz «بازو» از *h₂erH-mo- «مفصل، بازو» که همتای دقیق īrmá- سنسکریت، arəma- اوستایی، armus لاتینی و ramo اسلاوی کهن است؛ و ژرمنی آغازین *rēdaną «اندرز دادن» از گونهٔ *rē-dh-، که rātan آلمانی علیای کهن، garēdan گوتی، ráða نورس کهن و rǣdan انگلیسی کهن از آن است. پوکورنی در صفحهٔ ۵۹ دستهٔ نخست و در صفحهٔ ۶۰ دستهٔ دوم را می‌آورد و در همان‌جا می‌نویسد rǣdan انگلیسی کهن «خواندن» هم معنی می‌دهد (read امروزی). ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. ar-: 'I.1.a. Germanic *armaz in Old English earm, arm: ARM¹' and 'III.2. Suffixed form *rē-dh- in: a. Germanic *rēdan in (i) Old English rǣdan, to advise: READ, REDE'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW pp. 59-60\",\n              \"stance\": \"supports\",\n              \"note\": \"p. 59 'got. arms, ahd. usw. arm \\\"Arm\\\"'; p. 60 'ags. rǣdan (letzteres auch \\\"lesen\\\", engl. read)'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I pp. 73, 75\",\n              \"stance\": \"supports\",\n              \"note\": \"p. 73 'got. arms, ahd. usw. arm \\\"Arm\\\"'; p. 75 'as. rādan, anord. rāda, ags. rādan (letzteres auch \\\"lesen\\\", engl. read)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 20,\n          \"lang\": \"English\",\n          \"words\": \"read, arm\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"arm (the limb) is beyond doubt: Old English earm, from Proto-Germanic *armaz, from PIE *h₂erH-mo- 'joint, upper arm'; Klein 'arm, n., the upper limb. — ME., fr. OE. earm, arm, rel. to OS., Dan., Swed., MDu., Du., MHG., G. arm, ON. armr, ... Goth. arms, \\\"arm\\\", and cogn. with OI. īrmáḥ, Avestic arəma-, \\\"arm\\\", Arm. armukn, \\\"elbow\\\", Osset. arm, \\\"palm of the hand\\\", Gk. ἁρμός, \\\"a joint\\\", L. armus, \\\"shoulder\\\"'; Buck (Selected Synonyms 4.30) lists the same set under '*ar(ə)-'. read is the doubtful half: Old English rǣdan 'to advise, counsel, interpret, guess', Proto-Germanic *rēdaną, and the specialisation to 'interpret written signs' is a shared English-Norse innovation (OE rǣdan, ON ráða) alongside the noun rǣd 'counsel'. Watkins (1975/1985) does file it here, under 'Variant or separate root *rē- (< *reə-) ... Suffixed form *rē-dh-'; but the hedge in that heading is real: Etymonline gives read a root of its own, '*re- \\\"to reason, count\\\"', and current reconstructions posit *Hreh₁dʰ- 'to succeed, accomplish' independent of *h₂er-. So the arm arrow is confirmed and the read arrow is only plausible.\",\n          \"derivation_fa\": \"«arm» انگلیسی به معنی بازو تردیدناپذیر است: از earm انگلیسی کهن، از *armaz ژرمنی آغازین، از *h₂erH-mo- «مفصل، بازو»؛ کلاین آن را با īrmá- سنسکریت، arəma- اوستایی، armukn ارمنی «آرنج»، arm آسی «کف دست»، ἁρμός یونانی و armus لاتینی هم‌ریشه می‌داند و باک نیز همین گروه را ذیل *ar(ə)- می‌آورد. اما «read» نیمهٔ مشکوک این گره است: از rǣdan انگلیسی کهن «اندرز دادن، تفسیر کردن، حدس زدن» و *rēdaną ژرمنی آغازین؛ تخصیص معنایی آن به «خواندنِ نوشته» نوآوریِ مشترک انگلیسی و نورس است. واتکینز آن را ذیل همین ریشه ولی با قید «گونه یا ریشهٔ جداگانهٔ *rē-» آورده؛ اتیمانلاین ریشهٔ آن را جداگانه *re- «شمردن، اندیشیدن» می‌داند و بازسازی‌های امروزی *Hreh₁dʰ- را مستقل از *h₂er- می‌گیرند. پس پیکانِ arm درست و پیکانِ read با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/read\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82er-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference; the material comes from the parent Germanic box (ref 'AHD').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. arm ('the upper limb'), read\",\n              \"stance\": \"supports\",\n              \"note\": \"'arm, n., the upper limb. — ME., fr. OE. earm ... cogn. with OI. īrmáḥ, Avestic arəma-, \\\"arm\\\" ... Gk. ἁρμός, \\\"a joint\\\", L. armus'; 'read, tr. and intr. v. — ME. reden, fr. OE. rǣdan, \\\"to advise, counsel, discuss, deliberate, rule, guess, interpret, read\\\" (whence OE. rǣd, \\\"advise, counsel\\\"), rel. to OS. rādan, ON. ráða ... Goth. -rēdan'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 4.30 'arm'\",\n              \"stance\": \"supports\",\n              \"note\": \"'*ar(ə)- in Grk. ἀραρίσκω \\\"fit\\\", ἄρθρον \\\"joint\\\", Lat. artus \\\"joint\\\", etc. ... Lat. armus ... Goth. arms, etc., general Gmc.; OPruss. armo \\\"arm\\\"; ChSl. ramo ... Skt. īrma- \\\"forequarter\\\"; Av. arəma-'.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, root entry on pdf pp. 51-52 of ARY_latin_index_pages.txt\",\n              \"stance\": \"supports\",\n              \"note\": \"Aryanpur's entry groups '(AVESTAN) ARĀDH, -RĀDH / (PAHLAVI) ĀRĀSTAN / (SANSKRIT) RĀDHNOTI, RĀDHYATI / (LATIN) RĒRĪ / (GOTHIC) GARĒDAN, RĒDAN / (OLD ENGLISH) RĀDAN, RĒDAN, RĒD / (ENGLISH) READ', with references 'POKORNY ..., MACKENZIE (ADORN) 101, BUCK 1285, ONIONS (READ) 743, SKEAT (READ) 502' — the same *rē-dh- family Nourai charts, and the same one that also yields Persian آراستن.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins s.v. ar-, I.1.a and III.2\",\n              \"stance\": \"supports\",\n              \"note\": \"See node 19 ref_check.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-62.json > /dev/null && echo \"JSON OK\"",
 "description": "Write page-62.json and validate"
}
```


### [2026-09-04T23:31:36.681Z] TOOL RESULT

```
JSON OK
```


## [2026-09-04T23:31:42.360Z] TOOL CALL #86: Bash

```json
{
 "command": "python3 tools/verify_check.py 62",
 "description": "Run verify_check for page 62"
}
```


### [2026-09-04T23:31:44.250Z] TOOL RESULT

```
nodes verified: 20/20
node verdicts: {'confirmed': 11, 'plausible': 5, 'unverified': 1, 'transcription_suspect': 1, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 9, 'supports': 10, 'not_checked': 10, 'not_found': 1}
books consulted: {'supports': 33, 'partial': 13, 'silent': 11, 'contradicts': 5} | by book: {'POK': 8, 'AHD': 8, 'KLN': 6, 'BRT': 4, 'MON': 4, 'WLD': 4, 'NYB': 3, 'BQT': 3, 'HRN': 2, 'AMD': 2, 'LKT': 2, 'PLA': 2, 'LAT': 2, 'PHD': 1, 'FSF': 1, 'KNT': 1, 'IEC': 1, 'DEV': 1, 'TTS': 1, 'AFM': 1, 'FVQ': 1, 'SKT': 1, 'LEW': 1, 'SYN': 1, 'ARY': 1}
```


## [2026-09-04T23:32:01.796Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-62.json` written; `verify_check.py 62` reports 20/20 nodes, no PROBLEM lines.

**Page 62 (book p. 32), root `Ar, Are` [PIE *h₂er- "to fit together"] — root: confirmed (POK 55-61, verbatim in Watkins/AHD).**

Node verdicts: 11 confirmed · 5 plausible · 2 disputed · 1 transcription_suspect · 1 unverified.
Ref checks: 10 supports · 9 partial · 1 not_found · 10 not_checked. 25 different books consulted (33 supports / 13 partial / 11 silent / 5 contradicts).

Disputed / suspect items:
- **#11 Arabic `arbah, arobeh` "arms, war chariot" — disputed.** Greek ἅρμα cannot give Arabic عَرَبة (h- never → ʿayn). Lokotsch no. 90 calls the Arabic spelling "falsch arabisierend" for Turkish *araba*; Wiktionary: Turkic, ultimate origin uncertain, Arabic borrowed from it; Asbaghi (PLA) makes it Persian→Arabic. Borhan p. 96 gives no etymology at all.
- **#12 Persian `arrâbeh` ارّابه — disputed.** Word is real (BQT 96, Mo'in), but Wiktionary derives it from Turkic; Asbaghi compares Av. *raθa-* (root *Hret-*, not *h₂er-*). No source supports Greek→Arabic→Persian.
- **#10 Persian `ârtotoz` آرتروز — transcription_suspect, `error_in: "book"`.** The 450-dpi page image shows the book itself printing "ârtotoz" beside آرتروز; correct form ârterōz/ârtrōz < French *arthrose*.

Extraction error to fix in the data (JSON differs from the page): node #10 third word — the book prints **`logârîtm`**, `page-62.json` (batch) has `logaritm` (circumflexes dropped).

Other notable findings: #8 Greek `arma` is glossed "arms, weapons" but Greek ἅρμα = "chariot" (Pokorny 59); the English *arms/army/alarm* of #13 come from Latin *arma*, not from the Greek box. Nourai's page refs WLD:74 and POK:56 are article-correct but page-off for ratu- (WLD 71) and rādiy (WLD 75, POK 60). NYB:164, KNT:205, FSF:199, BQT:943/96 all check out verbatim; BQT:926 not found (no را headword in that range). Node #5 is a genuinely empty box on the printed page — extraction faithful.
