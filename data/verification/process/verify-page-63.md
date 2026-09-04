# Verification process log — verify-page-63


## [2026-09-04T23:03:52.163Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 63 only (note the recently added requirements: `derivation_fa`/`note_fa` Persian explanations, and `error_in`/`book_prints`/`correct_form` on any transcription flag). Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-63.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-63.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-63.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 63` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T23:03:53.922Z] AGENT

I'll start by reading the instructions file.


## [2026-09-04T23:03:56.276Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T23:03:56.293Z] TOOL RESULT

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


## [2026-09-04T23:03:56.367Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-63.txt"
}
```


### [2026-09-04T23:03:56.380Z] TOOL RESULT

```
1	=== PDF page 63 (book page 33) ===
2	--- entry 0 ---
3	ROOT [Old Persian] Ardha : swept, moved, pushed  (refs BQT:1445)
4	#1 (parent #0) [Old Persian] refs=NYB:23,76; BQT:1445 | fra-ardha, frârdha, frârdha-van : pushed forward, correct, right ☞Per 1 ; apa-ardha : pushed back, backward, wrong ☞Apo
5	  #2 (parent #1) [Pahlavi] refs=BQT:1445,2246; NYB:23,76 | frârôn : right, honest, upright ; apârôn : wrong, bad, upside down
6	    #3 (parent #2) [Persian] refs=MON:2499 | frârŭn «فرارون» : correct, honest | extra: فریرون ، فیرون
7	    #4 (parent #2) [Persian] refs=MON:4941 | vârŭn «وارون» : upside down, wrong, evil | extra: وارونه
8	--- entry 1 ---
9	ROOT Are -> redirect to Ar
10	--- entry 2 ---
11	ROOT [Arabic] A`.r.f, Ta`rîf : to know; information  (refs KLN:1573; AHD:1317)
12	#1 (parent #0) [Persian] refs=FVA:267 | erfân «عرفان» : knowledge, gnosticism ; ta`refeh «تعرفه» : a list of duties imposed on imports or exports | extra: عارف ، معرفت ، عُرف ، عرفات ، تعریف؛ معروف ، مُعرّف ، تعارف ، متعارف ، اعتراف
13	#2 (parent #0) [Turkish] refs=AHD | ta`rifa
14	  #3 (parent #2) [Spanish] refs=None | tariff
15	    #4 (parent #3) [English] refs=AHD:1317 | tariff
16	
```


## [2026-09-04T23:03:59.603Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-63.json",
 "description": "Read page-63 source JSON"
}
```


### [2026-09-04T23:03:59.651Z] TOOL RESULT

```
{
  "pdf_page": 63,
  "book_page": 33,
  "entries": [
    {
      "root": {
        "name": "Ardha",
        "lang": "Old Persian",
        "refs": "BQT:1445",
        "gloss": "swept, moved, pushed"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "NYB:23,76; BQT:1445",
          "words": [
            {"translit": "fra-ardha, frârdha, frârdha-van", "gloss": "pushed forward, correct, right", "script": null, "see": ["Per 1"]},
            {"translit": "apa-ardha", "gloss": "pushed back, backward, wrong", "script": null, "see": ["Apo"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:1445,2246; NYB:23,76",
          "words": [
            {"translit": "frârôn", "gloss": "right, honest, upright", "script": null},
            {"translit": "apârôn", "gloss": "wrong, bad, upside down", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2499",
          "words": [
            {"translit": "frârŭn", "gloss": "correct, honest", "script": "فرارون"}
          ],
          "script_extra": "فریرون ، فیرون",
          "note": null,
          "quote": {
            "text": "حسودت در ید بهرام فیرون - نظرزی تو ز برجیس فرارون",
            "poet": "Daqîqî"
          }
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:4941",
          "words": [
            {"translit": "vârŭn", "gloss": "upside down, wrong, evil", "script": "وارون"}
          ],
          "script_extra": "وارونه",
          "note": null,
          "quote": {
            "text": "پس ابلیس وارونه آن ژرف چاه - به خاشاک پوشید و بسترد راه",
            "poet": "Ferdowsî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Are",
        "redirect": "Ar"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "A`.r.f, Ta`rîf",
        "lang": "Arabic",
        "refs": "KLN:1573; AHD:1317",
        "gloss": "to know; information"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "FVA:267",
          "words": [
            {"translit": "erfân", "gloss": "knowledge, gnosticism", "script": "عرفان"},
            {"translit": "ta`refeh", "gloss": "a list of duties imposed on imports or exports", "script": "تعرفه"}
          ],
          "script_extra": "عارف ، معرفت ، عُرف ، عرفات ، تعریف؛ معروف ، مُعرّف ، تعارف ، متعارف ، اعتراف",
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Turkish",
          "refs": "AHD",
          "words": [
            {"translit": "ta`rifa", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Spanish",
          "refs": null,
          "words": [
            {"translit": "tariff", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD:1317",
          "words": [
            {"translit": "tariff", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-04T23:04:01.073Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T23:04:01.144Z] TOOL RESULT

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


## [2026-09-04T23:04:22.162Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['BQT','NYB','MON','KLN','AHD','FVA','FVQ','PHD','HRN','HUB','BRT','KNT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:900])\n    print()\n\""
}
```


## [2026-09-04T23:04:24.080Z] TOOL CALL #6: Bash

```json
{
 "command": "grep -n -i -E '^\\s*(FVA|BQT|NYB|MON|KLN|AHD)\\b' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -40; echo ---; grep -n -i 'FVA' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head"
}
```


### [2026-09-04T23:04:24.854Z] TOOL RESULT

```
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.", "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (19

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; sec
```


### [2026-09-04T23:04:24.949Z] TOOL RESULT

```
---
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
12: TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll
```


## [2026-09-04T23:04:30.489Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==31' NYB_vol2_glossary.txt | head -60",
 "description": "NYB glossary page 23"
}
```


## [2026-09-04T23:04:31.503Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==84' NYB_vol2_glossary.txt | head -70",
 "description": "NYB glossary page 76"
}
```


### [2026-09-04T23:04:35.202Z] TOOL RESULT

```
 —-aš pat asp nišast estat 89: as prepositions do not govern an encl. pron. ~ must be the adv., and -aš refer to the following pat asp or to the whole sentence. — b) prep. together with, with, in all its senses, passim; in spite of 118; ~ man 5?*; ~ amäh 19, ~ smäh 1918, ~ disin 82; ēvak ~ dit with each other 7818. 799. 1071, — 2. adj. prostrate, knocked down, lying on one’s back: čvak apar, ~ dit, apar ēstūt hend o en kar they set about this act (making coition), the one above, the other lying on her back 4314-4; ka Ahriman ~ A. being knocked down (lying senseless) 914 (the enel. -4 after ~ belongs to the following, taking up the preceding subj. Ohurmazd which begins the period), a wordplay — not understood by the Pazandist — with — hämöden yazdan u amahraspandän |. 5—6, the first
~ (l. 4) being a synonym of start (1. 2), ^
cf BdA, p. 712-81, and the second (1. 5) the prep. ‘with’; — adv. back, again: ka Zartuxst hāmēš ~ būt when Z. became
silent again, ceased speaking 342°; — 1. < *upäkä alternating with *upäcä, v. apäc 2; — 2. < *apdka- alternating with apäca-, v. apāc (1). MPrs ’b’g; Paz. awä; NP bä, prev. vä-.
3a-pàk unclean, soiled, turbid: LWTH dp be *šēpēnd (q. v) 2016-17: LWTH wrongly substituted for ’p’k = a-päk?
apa-kandan [LMYTN-tn'; Prth RMY-] pt. = pret. pass. 3d p. sg. apakand, written LMYTN without complement HajB:8, books LMYTN-t', Prth RMY-t HajA:7; LMYTN without complement = opt. apakané HajB:15; subju. 2nd p. sg. LMYTN-h = apakanäh 1009; cond. 2nd p. sg. LMYTN-t' HWH'-? = apakand hà 2226: to throw; bē ~ to throw away, with 6 or andar 6 to, into, against 2226 etc. passim; to throw (a bucket into the well) 142°. 151; to drive (a horse) against (6) 1145; to shoot (an arrow) HajA: 7. B: 8.15; - to arouse (fear) 5278; 6 miyān ~ to provoke (enmity) 10715; pat menišn 1... m to suggest to a p.’s mind 3712-13; — pt. apakand fallen, slain 2626. — < Olr *apa-kan- and *upa-kan- (v.s. v. apa-), from kandan, q.v.; MPrthPrs >bgndn; Verbum 172, Ghilain 55; Paz. pt. awagad, pres. awa-gan- (SGV); NP afgan- dan, augandan. V. also apa-cand, frakan- dan, pargandak.
apākēh [’p’kyh] 1. company; pat ~ together 5712, — 2. backward movement: pat ~ back 418; v. pat-apākēnītan. — 3. help, assistance 5919-20, 729-26 (opp. ha- mēstārēh). — V. lapāk and ?apäk. Paz. āvāgī. V. also apar-apākēh.
apäkenitan [—-ynytn'] to make a p., or a th., one's helper, or companion, or help: hakar vēnākēh apakéné [-yd] (if thou wilt make Clear Vision thy helper
==) if thou wilt have recourse to Clear
Vision 595, with the gl. ku-t dančikeh bavet ‘that is: (if) knowledge is to be thine’. — Cf also pat-apäkenitan.
www.parsianjoman.org NO
apäk-puhr
apäk-puhr [LWTH pwhl] he who has a son 22%. - Cf the NP compounds with bà: bā-āb ‘having water’ and the like.
apam [’p’m] debt 70%. — < Olr *apamna- ‘that which a p. (the lender) has to obtain (from the borrower), middle pt. of Av. (70 sqq.) ap- (v. ayāftan); as to the form, cf garämik. Paz. dwam; NP vam, āvām.
lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’
```


### [2026-09-04T23:04:37.184Z] TOOL RESULT

```
therwise ... 1181-15, as in Arab in halla wa'illa; hac Armail ~ except (by) Armail 1151-11, — Av. (138) anyādā, Gath. for anyd@G, Skr anydtha; Paikuli, Prs ’yny’ (Herzfeld p. 132); FrP
éraxtan
25 ’yny’ (in most MSS marked 'dny?), with the gl. ’ny’, read anyā, qniä etc.; Paz. ainā.
. ér [’yl] Aryan, Iranian 26%; pl. cas. rect.
~ 4511, obj. 6175; pl. cas. obl. ~-dn: inser. ’yrn  HajB:2.3. SPrs:5.7.12. P 1:1.3; in the books ?yPn' 1118 ete. passim (2072 for cas. rect.). — Av. (198) airya-, OP ariya-; Prth aryän (q.v.); Paz. ērg; NP Iran only as a geographical name. V. also an-érdn.
eränak [’yl’nk'], pl. cas. obl. ~-dn the Iranians 228. — Paz. érqnagq (Mx). Cf s. v. Wwäspuhrakän.
Ērān-gušasp ['yPn'gwésp'] n. pr. of a general in Azarbaijan 1171, — V. gusnasp.
Eran-Sahr PyPn' štr'] the empire of the Iranians, the official name of the Sassa- nian empire, 17. 61:29 etc. passim. — V. Sahr.
eran-šahrik pl. cas. obl. ~-dn the inhabi- tants of Ērān-šahr 118°.
Erän-vöj Pyl’nwye'] n. pr. a mythical country 8612-13.17, 9325, 945-5. — Av. (1313 sq.) Airyanam vaējē; in Manicheism bor- rowed as ’ry’nwyjn, v. Henning, ZDMG 90, 1936, 5; BSOAS XI, 1943, 55; Paz. Erqvéé. Very much has been written on this country, v., e. g., Benveniste, BSOS
VII, 1934, 265-274; Nyberg, Rel., v. Index. Eran-x"arrah-kart-Sahpuhr [-GDH- =
z"arrah added by Markwart] ‘“Shapur has made glorious Eran" 116?? is according to Markwart the official name of the town called in Syriac Karka d-Ledän and by Tabari Īrān-xurrah-Sābūr, in the neighbourhood of Susa (Cat. 97. 98).
éraxtan ['dlhtn'] to inflict damage, or loss; (as a legal term) to condemn, to convict: tur éraxt hénd the Turs were condemned, they lost the case 4513; — [pres. črang-: äyözend 6 bazak, marnjēnd gehän, érangénd they are intent upon sin, they destroy the world, they inflict dam-
www.parsianjoman.org | col wok
éraxtan
age DkM 6989; tat pat dātistān(ūman>- deh či veh tuvän zatan u éraxtan cigón ka-š pat davreh u drusteh apäk gēbāh through righteousness thou art better able to defeat him and make him lose the case than if thou speakest to him coarsely and roughly (cf s. v. davr) PR 573; — pres. pass. 3d p. sg. éraxtét he is pronounc- ed guilty, opp. buxtet he is acquitted, v. Bthl, ZsR IV, 8; Paz. buxted ... érexted SGV III, 26; kē rāstēh rad pat xudstak eraxtet, ah veh cigon kē družeh rād pat ruvān éraxtét he who suffers loss of prop- erty because of his righteousness is better than the one who suffers the loss of his soul (forfeits his soul) because of his falsity PR 26$-9.] — Two vbs. seem to have coalesced here: 1) črtatan ērēc-, cf Paz. érexted and the caus. érezinidan ‘to condemn’ SGV XI, 257, most probably < abi- + Av. (1479 sq.) raék- ‘to leave in the lurch, to abandon to destruction’ (Bthl IF XII, 112sqq.); 2. éraxtan érang-, most probably a denom. of érang, črangčh 'trouble, delusion' (Paz. ŠGV X, 58 ete.) < *abi-ranga-, cf. an-črang, ranj, ranjak; MPrs ‘yrat, “yrnz- ‘to combat’, Verbum 199. (Bthl, l.c. adopted the reading érazt).
Erče [’lyc] n. pr. 4714. — Paz. Braz; NP fraj.
éréh [’ylyh] coll. the Aryans, or Iranians 6413.15.
éstatan (YK-YMWN-tn', yst'tn'; forms v. I, 177] 1. As an independent vb.: to stand 78. 1112, 2012. 3812, 7214; with prep. andar 9571-22; with apar 2874, 389; with pat to get up on 33%, in a figurative sense: to remain in, to live in 7419-16, to abide by, to stick to 58°. 6419.17; pat ravisn ~ to be in continual movement 9318-19;
```


## [2026-09-04T23:04:46.644Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E 'fr[āa]r[oō]n|apār[oō]n|ap[āa]r[oō]n|frârôn' NYB_vol2_glossary.txt | head -30",
 "description": "grep NYB for frārōn"
}
```


### [2026-09-04T23:04:46.704Z] TOOL RESULT

```
1539:frärön [pl’lwn'] righteous, upright, hon- est 18%, 6919.22.23, 7516. 843, 9024; comp. ~ -tar 552°. — Paz. frürün, Skr v. sadā- cārin; Olr *frürda-van- < *fra-arda-, cf aparon.
6566:frārūn: fraron
7493:värun: aparon
```


## [2026-09-04T23:04:47.752Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E 'fr[āa]r[oō]n|ab[āa]r[oō]n|apar[oō]n|^r[oō]n |rōn ' PHD.txt | head -40",
 "description": "grep PHD MacKenzie"
}
```


### [2026-09-04T23:04:47.820Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T23:04:54.358Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"aparon\\|apar[oō]n\\|ap'rwn\" NYB_vol2_glossary.txt | head -20",
 "description": "find aparon in NYB"
}
```


### [2026-09-04T23:04:54.460Z] TOOL RESULT

```
1539:frärön [pl’lwn'] righteous, upright, hon- est 18%, 6919.22.23, 7516. 843, 9024; comp. ~ -tar 552°. — Paz. frürün, Skr v. sadā- cārin; Olr *frürda-van- < *fra-arda-, cf aparon.
7493:värun: aparon
```


## [2026-09-04T23:04:56.249Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aparōn\\|apar¯on\\|aparön\\|aparôn\\|apar6n\\|aparon\" NYB_vol2_glossary.txt | head; echo \"=== search 'wrong, bad'\"; grep -n -i \"upside down\\|perverse\\|improper\" NYB_vol2_glossary.txt | head -20",
 "description": "search aparon variants"
}
```


### [2026-09-04T23:04:56.343Z] TOOL RESULT

```
1539:frärön [pl’lwn'] righteous, upright, hon- est 18%, 6919.22.23, 7516. 843, 9024; comp. ~ -tar 552°. — Paz. frürün, Skr v. sadā- cārin; Olr *frürda-van- < *fra-arda-, cf aparon.
7493:värun: aparon
=== search 'wrong, bad'
521:apürón ['p'lwn'; Ps. *p’lwny] 1. adj. wrong 664-11, 691, etc., opp. frärön (g.v.). — 2. adv. backward (= apäc) 1281, — Paz. dwārūn, Skr. v. asadācārin (Mx); NP vārūn ‘inverted, turned upside down’; < OIr apdrda-van-, derived, by means of the suff. -van-, from *apärda- < *apa- arda- ‘whose side is turned away’ (HP II, 15). V. ärak; cf apärik and frärön.
2700:*nigné-sar [*ngnys'1] *annihilated, *pow- erless 902%. — Reading quite hypothetical; Paz. substitutes nazär ‘thin, emaciated’, Skr. v. krsa. The last element may be -sär as in NP nigü-sür ‘turned upside down’, but the first element, which allows a great many other readings, can by no means be identified with NP nigü <
```


## [2026-09-04T23:05:07.937Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor pat in ['frärön [pl','apürón','ärak [','arak [']:\n    i=t.find(pat)\n    if i<0: print(pat,'NOT FOUND'); continue\n    leaf=t.count('\\f',0,i)\n    print(pat,'leaf',leaf,'printed page',leaf-8)\nEOF",
 "description": "Find NYB printed pages"
}
```


## [2026-09-04T23:05:09.397Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E \"^[0-9]*[[:space:]]*[āaà]r[āa]k \\[\" NYB_vol2_glossary.txt | head; echo ===; grep -n \"'lk'\\]\" NYB_vol2_glossary.txt | head",
 "description": "find arak entry in NYB"
}
```


### [2026-09-04T23:05:13.249Z] TOOL RESULT

```
frärön [pl leaf 88 printed page 80
apürón leaf 32 printed page 24
ärak [ leaf 21 printed page 13
arak [ leaf 69 printed page 61
```


### [2026-09-04T23:05:13.311Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-04T23:05:20.476Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 32 88; do echo \"--- leaf $n\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' NYB_vol2_glossary.txt | head -4; echo; done",
 "description": "check leaf headers"
}
```


## [2026-09-04T23:05:21.454Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==22' NYB_vol2_glossary.txt | grep -n -i -A4 \"ärak\"",
 "description": "arak entry"
}
```


### [2026-09-04T23:05:23.236Z] TOOL RESULT

```
--- leaf 32
; u ~ and others (z who) 10812; ‘ete.’ 11015. 12119; u ~-dn ‘et ceteri’ 11017; sak u dalman tdi <... except for dogs ... and vultures, (all the) other (animals) 9421-22, — MPrthPrs bryg (S, A-H II); apär- < *upārda < Olr upa- + *arda- ‘side’ (v. ärak): ‘standing by a p.s side, placed at the side of a th.’ = ‘his, its counterpart’ (HP II, 14); cf apärön. Paz. aware, which must be another w.: < *awarrég < *apar- rek < *upari-raika- ‘left over, remainder’ (from reztan, g. v.)?
U oc
apar-kär [”*plk”1] sovereign 5823. — ‘Whose work (office, kär) is supreme’.
apar-mänd ['plm?nd], v. must-aparmänd. aparnāi ['pln?y], v. apurnāt.

--- leaf 88
is vazurg ~ F:
1-2. — Arm. lw. vzruk hramatar; Talm hrmdr. V. Christensen, Sass. 114 sqq., 518 sqq.
trimoš [plmwš, plmwš] forgotten: ~ kartan to forget 875.99; ~ būtan to be forgotten, neglected 6816, — MPrs fr’mws (S); Paz. frāmēš, farmoš; NP faramoš, farmös. Cf Verbum 185, where the com- mon derivation from Skr mrsyate ‘he neglects’ is douted.
franaftan [plnptn'] franäm- to come, to go, step forward, to appear 40H. 519-10; frāc ~ id. 565. — Av. (1041) fra-nam-; MPrth pt. frnft, pres. caus. (!) frn’m-, Ghilain 73; MPrs prnptn prnm-, Verbum 173; Paz. farnaft. Cf ayinaftan.
```


### [2026-09-04T23:05:25.408Z] TOOL RESULT

```
13:a-kanärak [?kn’1k'] boundless, unlimited,
14:infinite 6714; of Zurvàn 773-4-12; of Time 778, — V. kanärak. |
15-a-kanārakēh boundlessness, endlessness, of Ohurmazd 637-28,
16-a-kar [’k’1] ineffective, powerless: ~ kar- tan to incapacitate 4218-19, 10320-21; ~ būt mar u start 5476-10. — V, kar, Paz. agar; Skr. v. an-upakürin- (Mx), ägär, Skr. v. aksama (SGV).
17-akārēnītan [~-ynytn'] to incapacitate, to destroy 42%, — Paz. ägärined, Skr. v. vināšayati (SGV XII, 43).
18-akärihistan [~-yhstn'] pass. of the pre- ceding vb.: Ahriman bē akārihēt A. will be incapacitated, powerless 7719-11,
```


## [2026-09-04T23:05:30.532Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rak \\['1k'\\]\\|ärak \\['\\|arak \\['\" NYB_vol2_glossary.txt | head; echo \"===\"; grep -n \"side, half\\|‘side’\\|'side'\" NYB_vol2_glossary.txt | head -20",
 "description": "find arak 'side'"
}
```


### [2026-09-04T23:05:30.627Z] TOOL RESULT

```
616:ärak ['k'; Prth STR’] side: ‘L LBR’ STR? outwards HajA:9 = 0 beh ärak, MPrth ^w byh rg (A-H III s. v. byh); tar matist — in the line of his maternal grandmother 3610-11; cas. obl. ~-éh: 6 dašn ārakēh + . . from Av. (193) arada-; MPrthPrs ?rg, ?rg.
===
516:apārīk [’p’ryk; Prs inser. ’p’lyk] other l. attribute, placed before its subst., passim; seldom inflected in pl. before a subst. in pl. cas. obl.: hac ~-dn giyākān u röstäkän 8617-18, — 2. independent: ~ other people 5026-27; han i evak ... the one ... and the other 1093; ēvak-ē ... u ~ one... and another 12115; ~ har cé all other things that ... 862. 10411, 1211; u ~ and others (z who) 10812; ‘ete.’ 11015. 12119; u ~-dn ‘et ceteri’ 11017; sak u dalman tdi <... except for dogs ... and vultures, (all the) other (animals) 9421-22, — MPrthPrs bryg (S, A-H II); apär- < *upārda < Olr upa- + *arda- ‘side’ (v. ärak): ‘standing by a p.s side, placed at the side of a th.’ = ‘his, its counterpart’ (HP II, 14); cf apärön. Paz. aware, which must be another w.: < *awarrég < *apar- rek < *upari-raika- ‘left over, remainder’ (from reztan, g. v.)?
2193:kanürak [kn'lk'; ŠTL”] boundary 512’. 529.11, — MPrs kn’rg ‘side’; Paz. kanāra; NP kanärah ‘side, shore’.
2355:kust [kwst'] side, direction; region, dis- trict 113-115.117 passim; pat [kwst! + 1] aside 14%. — Paz. kūst, cf MPrt kws ‘country, countryside’ (A-H TIT); Arm. lw. ko?s ‘side’, kust ‘the waist, the belly’ = NP kust.
2963:parón [plwn', inser. plwny] on the other, the reverse side; in the other direction Vd. 214; comp. ~-tar further beyond ibd. 92%; on the opposite side, opp. örön Y. 537; — beyond, in the other world, opp. örön in this world, very often in the Kartér inscriptions: plwny ‘L yzd’n lwny, L wtlt’n lwny = parönY 6 yazdān ron", 6 vitartān rönY in the beyond, on the side of the gods, of the departed. — < *para-rón (para v.s. v. par-bütan; rön ‘side’, v.s. v.) whence either pardon through haplology, or parrén with syn- cope of the second a; a trace of the latter form perhaps in *hu-parrön (g.v.).
3079:patran [ptl’n'] resistant, refractory, of the boar 262°. — Corresponds to the Av. (828) epithet of the boar pattt.srona- (var. paiti.rana-, paitirena-) which has been remodelled under the influence of ran ‘side’ (q. v.).
3237:ran [Pn'] the thighs 2818; side 5421, 6129, — Av. (1523) Iräna- ‘the outer part of the thigh’, but *rdna-, rqna-, which Bthl translates ‘combatant, champion’, is more likely to signify, at least originally, ‘side’; ef next w.
```


## [2026-09-04T23:05:45.920Z] TOOL CALL #18: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1445 --image 2>&1 | tail -60",
 "description": "Fetch BQT page 1445"
}
```


### [2026-09-04T23:05:52.527Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1445.png
REF: BQT:1445  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 238  OCR-lang: fas

-<وعی:۱- فرارون

قراخ دفتن - کنایه ازبتتاب‌وسجیل ۰| فراخا است که فراخی وکشادکی- ومحل فراخی
رفتن باشد . وکشاد کی باشد .

فراخ دو ۱ - بنتی‌رای بی نقطه,,تمجیل فراخود ؟۴ » با واو ممدوله بر وزن
و شتاب رونده راکوبند - وکنایه ا زکسی اب | تفاخر ۱ نی شایسته ولایق وسزآوار باشد .8
که ازحد خود بیرون رود ومسرف وهرزه‌خرج فراخیدن بر وزن دوائیدن ۰ موی
را نیز کوبند ۳ - وبضم رای قرشت (۱). مردم | دربدن برخاستن وراست استادن‌باشده - وبمعتی
کشاده رو وشکفته وخندان باشد و کیکه‌پیوسته | ازهم جداکردن هم هست۹ .
بعش و اعشرت گذراند و با مردم خوش خلقی فرادد ۷ - بفتح اول بر وزن برادد ؛
کند .ع چوبی را کوبند که در پس در(۲) اندازند .

فر اخنا ؟۴ - بانون پروزن هز ارپا بممنی فر آدون ۸ - با رای بی نقطه بر وزن

(۱) چك : وم را . (۲) چك : کوچه .

۹ از: فراخ ۳ رو (رونده ). رك: فراخ رفتن . ۲ - ر4: فراخ روی .(حاشه)

۴ - از: فراخ نا (پوندساختن‌اسم ازصفت) [قی:ژرفناء تنگنا] ۳ فراخی * فراخا .

۴ - از:فرا (پیشوند) 4 خور (خورنده) ۳ درخورءدرخورد ورك: اسشق۸*۹ور4: فرا .۰

6 -قی : خیدن . ‎٩‏ از : فراخ #ایدن (پوند مصدری ) .

۷ - از : فرا در * فردر** فردره . ی : فراوند .

۸ - پپلوی ۶۳2۲۵ ( عالی » مستقیم » راست ) و ۳27۵8110] ( تفوی » استقامت )
« منای ۲۷۳ :۲ » در لفت فرس ص ۳۷۸ آهده : * فرارون» کوا کب بیابانی‌است 1۰ نکه‌رفتنشان
باز پیش بود . دقیقی (طوسی) کوید :

حوفت در ید ( بد . دهغدا ) بهرام فیرون نظر زی تو از برجیس فرأرون . >
فرارون بمعنی پاکدامن ونیک و کردار وپرهیز کار درمقابل لفت « اوا رون > بمعنی کناهکاروشربر
آمده , هیچ ربطی با کواکب ببابانی ندارد . ( صادق هدایت . مجلةٌ موسیقی سال ۲ شمارة ۸ )
و رك: بشتها ۲ ص ۱۷۹ متن و حاشیه . نیب رکهص ۷۲ - ۷۳ کوبد : پهلوی ۳8۲۵0 (راست.
درست, درستکار )» پازند ۶۳2۳۵ » از ابرانی باستان - 5۶۳270112۷28 از ۳۵1۳270112
- 21۳2-27488 ( بجلو جاروب کرده )» قن 203721 و 202100 . رك: فربرون .

5 فراخ روی - بفتح اول و دوم و پنجم » از : فراخ رو ی ( اسم مصدر ) ؛ زیاده
روی خرج کردن بهوده » اسراف :

مکن فراخ روی درعمل» اکرخواهی که وقت رفع توباشد مجال دشمن تنگه.
۰« کلتان ۳۹ .

5 فراخی - بغتح اول » از: فراع ی ( اسم مصدر) * فراخا* فراخنا. پهلوی
0 نیب رکه ۷۱ >. کردی ۴۵۲۵1 . ۲6۳201 ( عرض » فراوانی ) « ژابا ص ۲۹ >؛
کفادکی » وسمت . عریضی ۰ پهنا . اشد : تنگی :

فراخیها وتنگیپای اطراف ز رای پادشاه خود زند لاف.
نظامی گنجوی ( لفت نامه : لاف زون ).
```


## [2026-09-04T23:06:10.259Z] TOOL CALL #19: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:2246 --image 2>&1 | tail -50",
 "description": "Fetch BQT page 2246"
}
```


### [2026-09-04T23:06:18.093Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2246.png
REF: BQT:2246  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 329  OCR-lang: fas

وارث داود -۲۲)۹-
بسیار ومکررهم هست چنانکه « وارها کنته‌ايم » | کنده‌میباشد وخمیرنار! بدان‌تنك‌سازندء وعریان "
یمنی بارها وبسیار و مکرر کفته‌ايم ۱ - وبارشتر | نوبنا بانای مثلنه ونون بروزن هویدا میگونند.
و خر رانیز کوبند ۴ همچو خرواری کندم و وارع؟۲ - بکر ناك بر وزن فارغ »
شترواری جو- وبمعنی‌مقدارهم آمده‌است همچو بمعنی برغ است وآن بندی باشد که درییشآب
يك جامه وار ويك کلاء وار پمنی بقدر يك جامه ) ازچوب و کل بندند - ولحیم را دیز کوبند وآن

ويك کلاء ۴ - وبممنی لیاقت هم کفته‌اند هنچو | چیزی باشد که طلا ونقره وامثالآنر! بدان‌پیوند
شاهوارو کوشواریمنی‌لایق پادشاء ولایق کوش؟* - | کننده ویضم ثالث وافتح ثالك هم آمده است -
و بمعنی مهر ومحبت هم بنظر آمده است ۴ - | وچوب بندی وجفت انگور را نیز کفته‌اند ۸ .
ودرتر کی بمعنی هست باش د که نقیض‌لیست‌است- وارن - بفتح ثالك بروزن قارن» آراج
وامر برفتن هم هست یعتی برو - را کوبند که بندگاه ساعد وبازو است و بعریی
وارث داود - کنابه ازسلیمان(۱) | مرفق‌خوانند؛ وبکرئالك هم باین‌معنی‌است۹ -
علیه‌اللام است . و بم ثالك مخفف وارون است که با ژکونه ()
و ارخد سیفتم‌ناك‌وسکون‌خای شطه‌رار ۱ باشد وبعربی عکس کوبند*۱."
ودال بی‌نشطه ۰ هردم کاهل وتتبل را کوبند ۵ ۰ وارنج۱۱- بروزن ومعنی آرنج‌است که
واردن! « بفتح دال آیجد بر وزن خار. | بندگاه میان‌ساعدوبازو باشد وعربان‌مرفق کوبند.
کن » چوبی است که دوسرآن باربك ومیان آن وارون؟۱- بروزن‌قارون, معروف‌است
(۱) چش : سلمان . () چك ۰ چش : با زکونه .
۹ * بار ( چنانکه کوبند: بارها ...) و صورت جمع معنی متن مستفاد است. ۱
۲ « بار (ه.م.) [ممنی۱] ۰ ۳ - « خانه‌ای دید... وخانه واری حصیر از خوشهة
زرکشیده افکنده ...> مرحوم قزوینی نوشته: « غانه وار ظاهراً بممنی مقدار يك خانه باشد ...>
ومرحوم بهار نوشته: «خانه واری حصیر» یمنی فراخور يك خانه حصیر» ... «وار» و «واره» پساوند
لیافت است , مانند شاهوار وکوشوار یمنی لابق شاه ولایق کوش» رك : چهارمقاله مسحح نگارنده

چاپ ۲ ص ۰.۳۵ ۴ - یز بمعنی توبت وبار ۳ واره :

کل کوره‌بگلتان‌آمد وارة باغ,بوستان‌آمد ‏ وارآذر گذشت وشملةآن شملةٌ لاله‌را زمان‌آمد.
2 رود کی سمرقندی شرح‌احوال. نفیسی ج۳ راید را ها

ورك : رشیدی . 8 - ۶ وارخد » مرد لوند راکوبند » « جهانگیری >.

. > ‏عوردنه (ه.م.) . گلپایگانی نیز ۸۷6۵۳۲۵4606 قاسمی‎ ٩

۷ ورغ (ه.م.) * برغ (« م.) ۸ - ر4 : رشیدی : در موْیدالفسلا وازع بزاه
آمده و هيجچيك شاهد نیاورده‌اند » ظ مصحف ۶ وآذیج لظ۱ وادیج [«م 1 ) است . ره : واژغ -

‎٩‏ «آرن (وم)» آران («.م )> آرج (م) *وارنج («م.) * وارن » بند دست
باشد میان ساعد وبازو. آغاج ی گفت :
زمانی‌دست کرده جفت‌رخار ‏ زمانی‌جفت‌زان و کرده وارن .> «صعاح‌الفرس‌نسخهٌ آقای طاعتی >.

‏۴ مخفف « وارون»(۸ م.) ۹- آریج(«م ) #وارن (هم ) * آرن («م)<
آران (وم.) ؛ بحی تصور کرده‌اند که « وارنج » مصحف «آرب» است با ۶« و » عطف. درین‌صورت
«وارن» نیزمصحف «آرن» (ه.م.) بایدباشد ار4: وارن. ۹۴ * وارونه (۸م )» پهلوی888702 ۰
203۳8018 مرک از : 204 ( پیشوند ) و پهلوی 108 ( طرف » جپت ) اسلا بمعتی کنار :
قی : پهلوی ۶۲۵۲۵80 « اسشق ۰۱۰۷۸
```


## [2026-09-04T23:06:31.926Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD rōn\"; grep -n -E \"^r[oō]n|rw'n|^rōn\" PHD.txt | head -10; echo \"=== PHD frārōn / abārōn\"; grep -n -i \"frārōn\\|frārōn\\|abārōn\\|frʾrwn\\|pl'lwn\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "grep MacKenzie"
}
```


### [2026-09-04T23:06:32.035Z] TOOL RESULT

```
=== PHD rōn
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
=== PHD frārōn / abārōn
PHD_mackenzie.txt:2321:fraron [pl'lwn l ] righteous, honest.
```


## [2026-09-04T23:06:33.487Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"فرارون\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"=== varun\"; grep -n \"وارون\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10",
 "description": "grep Mo'in for farārūn / vārūn"
}
```


### [2026-09-04T23:06:33.610Z] TOOL RESULT

```
=== varun
MON_part1.txt:18048:وارون شدن. آوازه شدن» شهرت یافتن. 
MON_part1.txt:18050:(امص.) باژگونگیء وارونی؛ ج. انعکاسات. 
MON_part1.txt:20512:باشگونه] (ص‌مر.) سرنگون» وارون. 
MON_part1.txt:77446:کردن: (عم.) (کذ.) کار وارونه کردن. 
MON_part1.txt:92539:چنانکه هست يا وارونهٌ آن خواندن. 
MON_part1.txt:97682:را وارونه به کاغذ دیگر چسبانند و با رطوبت 
MON_part2.txt:14065:وارونه کردن حروف یک کلمه. . صسح.- 
MON_part2.txt:20878:آن را وارونه در ظرفی برمی‌گردانند و به 
MON_part2.txt:33634:می‌شوند و در انتهای ساقه بطور وارونه قرار 
MON_part2.txt:61061:سرنگون, واژگونه. وارونه. تسرتیب
```


## [2026-09-04T23:06:41.019Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"abaron\\|ab'lwn\\|'p'lwn\" PHD_mackenzie.txt | head -10; echo \"=== ron\"; grep -n -E \"^ron |^ron\\[|ron \\[lwn\" PHD_mackenzie.txt | head -10; grep -n \"lwn'\\]\" PHD_mackenzie.txt | head -10",
 "description": "grep MacKenzie for abaron and ron"
}
```


### [2026-09-04T23:06:41.130Z] TOOL RESULT

```
704:abaron ['p'lwn' I N warun] contrary, wrong, sinful.
6241:confidence wistaxih.                         contrary abaron, mih.
7587:sin abaronih, astar, bazag(ih), man-          smaller keh(tar).
8004:wrong abaron, zefiin.                   youth Juwan; juwanih.
11557:abaronih
=== ron
```


## [2026-09-04T23:06:42.470Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"MON_part1 size:\"; wc -l MON_part1.txt MON_part2.txt; echo \"--- first lines part1\"; head -3 MON_part1.txt; echo \"--- part2\"; head -3 MON_part2.txt; echo \"=== grep فرارون anywhere\"; grep -rn \"فرارون\" MON_part1.txt MON_part2.txt | head",
 "description": "inspect MON files"
}
```


### [2026-09-04T23:06:42.576Z] TOOL RESULT

```
MON_part1 size:
  99339 MON_part1.txt
  94500 MON_part2.txt
 193839 total
--- first lines part1
0 
2 

--- part2
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


=== grep فرارون anywhere
```


## [2026-09-04T23:06:51.178Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ron entry\"; grep -n \"ron \\[lwn\\|^ron\\b\\|rōn \\[\" PHD.txt PHD_mackenzie.txt | head; echo \"=== PHD_mackenzie context around 'roz'\"; grep -n -E \"^r[oō0]n\" PHD_mackenzie.txt | head; echo \"=== search 'direction' in PHD_mackenzie\"; grep -n \"direction\" PHD_mackenzie.txt | head -20",
 "description": "find rōn in MacKenzie"
}
```


### [2026-09-04T23:06:51.275Z] TOOL RESULT

```
=== PHD ron entry
PHD.txt:559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
PHD_mackenzie.txt:9380:ron
=== PHD_mackenzie context around 'roz'
9380:ron
=== search 'direction' in PHD_mackenzie
3363:lkust [kwst ] side, direction; district.
3705: --ag [1zymk ' I N --a] half, side, direction.
3755: --ih: depth, downward direction.
4371:rayenidarih [l'dynyt'lyh I M r'ynyd'ryh] direction, organization.
4417:r6n [lwn l I M rwn] direction.
4568:ssog [swh I N so(y)] side, direction.
5055: -ih: upward direction.
6408:direction kust(ag), nemag, ron, sog;    doer kardar, kunisngar.
7864:  pardaxtan o.                           upward ul; ,.,., direction ulih.
```


## [2026-09-04T23:06:53.008Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT arəδa\"; grep -n \"areda-\\|arəδa\\|arэδa\\|ar9δa\\|aroda-\" BRT.txt | head -20",
 "description": "grep Bartholomae for arəδa"
}
```


### [2026-09-04T23:06:53.075Z] TOOL RESULT

```
=== BRT arəδa
```


## [2026-09-04T23:06:58.772Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Seite, Hälfte\\|Hälfte\" BRT.txt | head -20",
 "description": "grep BRT for Hälfte"
}
```


### [2026-09-04T23:06:58.855Z] TOOL RESULT

```
3894:Hälfte  der  Nacht'>:  -rsm  Y.-ijh.  [N.
4257:■Wortl.''eo  prias',  IS.  aus  aita-.  —  Pii, :  \.  Hälfte fehlt,    dann;    ätigäh    an    pa  mäiiit  rf^nd  afF
4577:•  j.  'an'tara-  Adj.  'der  andere,  zweite': "  rizanmaEm  .  .  'rat  tiaSmat  aHahe  (ha- "krähe)  ". .  von  der  zweiten  Hälfte  dieser Frist  an"  N.//;  //;*'  —  pashSa .. uis/ü- (iBit  ..  *'r3m  arKi^m  tnayaAe(sd.)  ^parm- tarim  ..  V.^, 29;  —  yim  antar)  PTta (sd.) *°/-(j//''  ^r.iyj  maya  V.p.ii;   11*.
4642:•  j,  'an'tara-  Adj.  'der  andere,  zweite': hrizarpmalm  .  .  'rat  naSmäl  ailaAe  {Aa- hraAe)  ". .  von  der  zweiten  Hälfte  dieser Frist  an"  N.7/;  ;/;*'  —  pascaita ..niSAi- oöit  . .  *°r}m  arS(i?m  mayaAe  (sd.)  *par3ii- tarpm  ..W.g.aq;  — yim  antar?  vi/a(sd.) *'/■«//''  7}rjy:!  maya  V.ij.ii;  11',
5459:KonipA.,E.  —  «i.aj-aMfl- Adj. 'halb',  m. 'Hälfte', ördha-  m.  'Sei(e';  oss.  ärdäg  'halb,  Hälfte'.  — Vgl.  arilah:  —  Pö. :  kanär  (dat  n  a,  vgl.  dal  r ; bei  Salemann  Porsenhdschr.  öS  II  Z.  5,  6).
7711:•  }.  »rszaurvaesa-  m.  Name  des  zweiten Abschnitts  der  ersten  Hälfte  der  Nacht*'; 'Sät  F.  27  b.
10599:-yekya  (ISf,)  frasrnUi  "..  die  zweite  Hälfte  1  mazää  yasamaiäe  dar»%rai  .  .  'tum  ('Ge- mit  lauterem  Vortrag"  Y.ß.  i4'>.  dächtniskraft')    ..  marf^rJt  ..  hitvqm  ..
13484:•  j.  dästra.ma3ah-  Adj.  'von  der  Grösse der  Hälfte,  halbsoviel':  äaj  nSvayayäl (näml.  ape)  avatgs  aSanha  *frab»r3ta  's6 paitiMrg  "aber  schiffbarem  Wasser,  ohne sich  zu  versündigen  kann  ihm  der  Fr. halbsoviel  darbringen"  N.  Ö7.
15728:väiam  (sd.j  vazaUi  YL  ü.  33;  —  mmsu  (sd.) *°f^fl">(ADm.)a:"ak/?V./p.42.  2)9)  der Reihenfolge  (und  dem  Rang)  nach,  'der erslere':  ttaola  (sd.)  yanya  .  ,  'va/^^  vä naemat  aparät  vä  N._37;  —  yai  ki  avßi •rum'>  ubjyäite  (sA.)  V.j-sa  PQZ.;  —  cva^ haca  'rvaiibya*^  (läxcA.  majaHfya)?  ya%a %rig3im  V.p.  9;  Ä  39; —  aiwUa  apanm (sd.)  apäla  'voHbyai'i  V.iß.^S; — 'rvä^^ äätä  dämqn  aiaonXsY.iÖ.^;  —  upa  vä mq%r?m  sp^niitn  maraSa..  'rutiüa'^  naime asne  apanmca  ".  ,  die  erste  Hälfte  und die  zweite"  V.4.4S;  45;  —  'ruin*>  vä na^m^m  ^yän  apanm  väü.44; — mitAbl.: näirivaite..afimäi  •rum''>  {SSx\.)/ramraomi ya%a  May avB^sd.)^. 4.47.  A)iSTLpcururva als  Adv.  'zuerst';  'rva  hl  tamS  baraiti •n>a  oTannä  Yt/4^36.  3)9)  der  Zeit nach  'der  frühere,  erstere':  Xtyaiy  'ruvä xsäyähiyä  Eh.  4. 9;  —  anuzvarstä^  (sd.) paiü  'rvät^  V.4.  ao;  —  yafärS  *rvS^ uifhistaiti  "qui  prior  surgit"  V.iS.a6;  26, Yt  14.  44');  —  yatära  (sÄ)  vä  als  °rva'> (^Pm.) /räyatmU  Yt.rj.47;  lO.g  (NSf.); —  yahmal  hala  'rvS'ä  snao%S  (sd.)  .  . inalzät  V.2.  32;  —  'rvai'>  (NPol)  täyüm . .  bU^ySima&e  mä  Ä/  'rv5^''  büSiyaifa  nS Y.  p.  2 1 ;  a  I  \  F.  1 3»;  —  iaiärif  'rvö  (NPm.)J* amayäntei^)  V.7.36;37j  —  ava.jasnm (sd.)  -rvqm^  äpB  JaÜiyöt^  .  .  pasiaSa aiwyS  zaohrä  frabarOis  Y.  6^5. 1  o.  a)  Das Praesens  hat  dabei  den  Sinn  der  Ver- gangenheit"); j'?«  Toa^'f  (NPm.)  mihrwt druiinti  "die  zuvor  den  M.  belogen  haben" Yt  10. 45;  —  atibyS  .  .  ysi  vB  vanuhls  . . nHiJ  °rva^  (ASf.)")  äzärayente  "denen, die  euch,  ihr  guten, . .  nicht  zuvor  erzürnt haben"  YLy.30; — tä  sravä  ..yä'rva'^ al^rapalays  dnnjayan  (Sp.  773  o.)  V. 4.45;  —  ä  äim  aoxta..'rv3'*  asavapara.- iri^yB  (PPA.)  ". .  ein  früher  gestorbener Gläubiger"  H.  2.  16.  —  Aber:  ä  dim aoxta  .  .  'rv5''>  drvö  ava.mtrm  (PPfP.) ". .  ein   früher   gestorbener  Ungläubiger"
16639:ava^a  hl  ^^ato  (sd.)  puhnm  atskat  aOiS 'ytm  haca  avantanqm  nisrinuyät  äat  yezi Avant  näirika  bavaiti(%A^  alu§ 'y>m  paiti nidanäiti  yezt  du-j'irqm  (sd.)  fanü  tialm>m •y>m  frajasät  Vd,2  (der  Sinn  ist:  Frau und  Söhne  des  Erblassers  sollen  aus  der Erbschaft  den  gleichen  Teil,  die  Töchter die  Hälfte  davon  bekommen);  —  ytmasät ys  matyfng  cixinusS  akmakSng  gaus  -gä (APn.)  «"JwMWii  (sd.)  V.  J2.  8;  ~  'ya Y.16^''.  a)  bes.  'günstiges  Los,  Glück': yazäi  *apqmca  'y»mca  YL  /j.  i.  o)  bes.  1 vom  Glück  in  der  Ehe,  'Eheglück'  (nur Komp.)'*.         [Yt/6".  15:  lies  voku.b'.\
17762:*)  Nach  F.  37  b  ist  (mp.)  frayarSi  die  ersle Hälfte  des  Tags  (im  Gegensatz  lar  Nacht);  vgl. usayara: Ableil.  iB  •//■fl+aj-flr.  (s  36S.  3);  eig.  'voni am  Tag,  lu  Anfang  des  Tags  liegend';  vgl. iBed.  ai.  frähfif  Adv,  'vormittags',  —  Pü.  (zu l);  /raläif)  andar  räc  (,  SQ.:  dhiasamaifhv'), (lu  2y./rayarit.  (in  2  a.):  fraläi \).  —  ■)  Hds. 'yofrf.  —  ')  Hds.  /r  yaräl.  —  S  gelW.  — 4)  D.  i.  V^./ardä;    mp.  fratai  scheint  'matte'
18281:•  j.  fräsmö.dätay-  f.,  mit  /lä  (GS.,  sd.) 'Sonnenuntergang':  Aaca  hü  vaxsäl  ä  hü °lSii  Yt  j.  91,  *N.4*;  —  pasca  ha  'däi- tlm  Y.57.10,16,  Yt.^8,  5.94,  /0.9s. V.  7.  58,  N.  ^48,  58,  ♦(j.V;  —  para  hU  'ISil N.  jo ;  —  hu  'däiti  Vd.  5 ;  —  haca  *piaioyäJ *uzayarai  *hB  *'tSe  N.50'';  —  haca  hü [*vaxi'ai\''^  *•/» (statt Abi.)  mathyat  xSape N.  5i'>.  a)  Name  des  ersten  Abschnitts der  ersten  Hälfte  der  Nacht":  *'daiim F27b;  —  s.  noch  N.50,  5/  mit  No.  i.
18490:•  j.  naema-  1)  Adj.  'halb':  '«am  bay^m Vd.  2;  —  'nam  ySr»  "ein  halbes  Jahr (lang)"  N.45i*44'^;  —  'mmi  yJn.drä/ä "eine halbe  Jahreslänge  (hmdurch)"  V. j.gö, ti.44i  42;  —  paourwn  va  'm^m  yän apar?m  va  "das  erste  Halbjahr  oder  das zweite"  N.  44)  —  pimrumca  'me  asne (bz.  xia/ne)  aparvmca  "die  eiste  Hälfte  des Tags  (bz.  der  Nacht)  und  die  zweite"  V. 4. 45*>.  3)  m.  a)  'Hälfte,  latus  alterum': ya(  vS  'mim  yat  va  'hri^wi  .  .  V,  if ,  32, 16.  2,  Y.  Jp.  7;  V.Äioi;  — aWsr  'mat.. uparät  *mat  y.i4.T,  6'.  8,  N.5_j,  P.  23;  — haoyat  hol  +*mS/3' . .  dalinat  hat  *'mai^ N.  75;  —  '^fraoirilarai  'mat  N.fi?;  — *aevahmat  'mat  N.  7p;  —  paurvat  va 'mat  aparät  va  ^.Jj;  —  antarä^  (sd.) 'm^  V.5.43»,  51,  6.2,  3,  7.77,  8.^1,  42, 104,5.15,  16,  N.öo,  6p',  *7jT,  54,  104^; II';  —  *va  *'ma  N.pp*';  —  vaHbya 'maltiya  "von  beiden  Seiten"  V./_y.3 1—37 PüZ.*;  —  apaxtarat  haca  *mat  V.ig.i, H.2.25,  FrW,/o.43";  V.j^.s,  H.2.7,  A. 4.6.  b)  'Seite'  überhaupt:  vlspe  'mq (AP.)  F.jg;  —  vlspa^työ  'maübys  Yl /0.41;  —  ahmst  'mäi ..yahmäi  'tnanqm YtJO.  19;  y.  3,  V.Ä80;  —  usastaratibyö haca  'maiiiys  V./p.5;  1,  H.2.  35,  V.7.  2, *i6,  FrW.JO.42.
18491:KompA.,  E.  —  aL  ntina-  Adj.  'der  eine  —  der andere;  hilb'i  np.  nfm  'halb;  Hälfte'.  —VgL iBed.  ai.  flW*a-  i)  Adj.,  a)  m.  und  got  Aifii '^lucvf',  ia&a  'iiipa^.  ■ —  Pü, ;  nem,  neinai.  — 1)  Hdi.  «aem.  —  *)  Gramm,  nndeutlich.  Gdm. Stod.  I.  93  übersetzt  falsch.  —  i)  Hda.  Jkae- naimäj;  t.  zn  Aa-.  —  1)  Hds.  vanaJna.
18502:•  j.  naemi.räO«-"  m.  'halber  Pflichtteil"*; _f«»  sai/g  at?hat  '^a  pu%ra  da^aifi  'äa anyöJkaiia  nairi/ta  dalaiti  (soll  heissen) "wenn  Vermögen  da  ist,  gibt  man  einen Fäichtteil  zur  Hälile  dem  Kind,  zur  Hälfte der  ,  .  Frau"  Nik.j.
18662:•  j.  navät  Part,  'oder  nicht";  airihä  äpg paraJiincaym  yat  va  nafmim  yat  vä  'Srri- sum  .  .  yezi  tütava  n'  tälava  "sie  sollen von  dem  Wasser  fortgiessen  die  Hälfte oder  ein  Drittel  .  .,  je  nachdem  es  mög- lich ist  oder  nicht"  V.  (J.  32;  A.J.  5;  — yesi  lat  yayala  n'  tal  yayata(sd.)  A.J.  3,
19662:*)  Ursprünglich  Sommersannwendfest  ist  es später  dem  Andenken  an  die  Schaffung  des Wassers  geweiht. Der  leuteTag(iS. des 4.Monats) ist  der  105.  Tag  des  Jabrs;  mit  ihm  schliesst die  erste  Hälfte  der  auf  310  Tage  (7  Monate) gerechneten  warmen  Zeit;  »gl.  V,  /.  3  Gl.,  Bd. 35.  7.  Heutzutage  ffillt  er  auf  Anfang  Janaar. War  er  in  alter  Zeit  der  Sommersonnwendtag (30.  Jani),  so  begann  das  alte  Jahr  am  g.  Man. So  Roth.  West  und  Dst.  dagegen  setzen  den Jahresanfang  auf  den  Tag  nach  der  Frlihlings-
24416:*päku  (fem.  statt  ntr.)  kar^Shu  Ytio. 16.  Anhang.  vXspa-  mit  Gen.  part"; a)  Sing,  mit  Gen.  Sing.:  %rilüin  . .  nagm?m ..vTspfm  aitake  syao%nahe"€\a.T>r\\\e\.. die  Hälfte  . .  das  Ganze  dieser  Tat"  V. Ä  100-102.  b)  Plur.  mit  Gen.  Plur,: ks  *fe  (APm.)  vtrnhinqm  (sd.)  vanat  nl •pe  v?r3tbinqm  janai  Y.  5. 14.
24924:hatten,  beim  Vortrag  auslassen':  yasca  mS\ . .  bayqm  ahuiiake  vaityehe  dr?njay5  *apa.-  \ raooayett  yat  vil  nasm?m  yat  vä  .  .  "und wer  mir,  das  Stück  AF.  leise  hersagend, (davon)  auslässt  sei  es  die  Hälfte  oder  , ." Y.  79.  7 '',  3)  'ausser  Acht  lassen,  ver-
24932:mit  VI  '(beim  Vortrag)  einbehalten,  aus- lassen' :  ye-A  antarSt  (sd.)  nalmät  aHaAe (näml.  Aä^rahe)  dniijayeiti  para  paUySiti vlrao'iayäli  "wenn  er  in  der  zweiten  Hälfte dieser  Frist  leise  hersagt  (und  dabei  etwas) übergeht,  auslässt"  N.  ;;'^>;  —  yezi.. aniarät  (sd.)  nafmat  {astaAe)  hiikraAe drtiijayäatia  *naf^a  pascalta  *viraöoayai^^ "wenn  er  .  .  leise  hersagt  und  (dabei) nichts  mehr  auslässt"  N.  11.
```


## [2026-09-04T23:07:04.364Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5450,5462p' BRT.txt",
 "description": "BRT context around arəδa"
}
```


### [2026-09-04T23:07:04.426Z] TOOL RESULT

```
Zum  V.  'ar-.  —  VgL  aUy  und  S  ^Sg.  4  C mit  No.  —  Pü.:  larsäiäsJh.  ~~  0  Hds.  ä  rii-' lim;  5.  aber  Pii,  und  iSt.  Y.  60.  3,  wo  oioö- w^  xsnülasla  asayasra  . ,  paili.uiiilayasfa.
•  p.  arta'vardiya-  m.  ER  eines  Heer- führers Darius  /.;  "rfiya*  nämi^  pärsJ^ tnünä  ba'dakt^  Bh._j.6;  6;  — patii  "diyam Bh.j.6,  7.
Eig.  'das  heilige  Recht  mehrend',  Ableit.  (ohne Änderung  der  Bed.)  aus  *arta-varda-  Adj.;  s. dazu  Wh.  Gr.»  S  1212  c.')  —  ■>  S.  auch  Foy ZDMG.  S4-  358.  l^Z.  j/.  518.
•  j.  aratö.kar^^na-  AdJ,  'wofür  die  Er- füllung der  religiösen  Pflicht  bezeichnend ist',  von  Hamaspa^maedaya  (sd.)":  ha- maspahmaSdaim  "tum  Vr.  2.  z; —  kama- spdimaldayeAe  'nahe  Vr.  1.2;  —  *'%nö F.7'>.
"jfnrjian-  n,  •perfectio',  zum  V.  '^iar-.  —  Pü. (lu  F.);  yaiiin  iarlär,  (sonst):  /a  yaiUn  kar- tärik.  —  ■)  Weil  in  diesen  Tagen  das  beson- ders gefeierte  Fest  der  Fravaiay%  stattfand; S.    unter    kamaspfiimaedaya:    —  '')    Geschr.
•  g-  (t  j)  arad-  V.  'gedeihen  lassen'. Praes.  i   arid-  :  »rjd-.
'gedeihen  lassen,  fördern':  däiä  ar?h3us andat  (Ko.)  vohü  manaahä  Aathyilvar/- tqm  (sd.)  Y.  50. 1 1 ;  —  >r»dat.'.
u.  ardhma,  j-dhyam\  fdhäniah.  —  Pü.:  bcaian- dai  dahänik  (für  arf+da/i).
•  j.  arsSa-,  p.  arda-  i)  Adj.  'halb' (nur  Komp.).  2)  m.  'Seite':  *atitar?m (sd.)  'tijm  mayaAe  V.p.29;  —  antar?m 'fam  nmanaheV.6.i,y,  — dasinim  (vair- yastärtm)  hl  upa  "htm  Yt.  10. 100';  — visps  he  upa  'wun  (lies  -o!)  \tio.ioo; —  äasimm  hl  'Öe..  Aävöya  hl  "%€  "rechts (links)  ihm  zur  Seite", Yt. /o.  ia6;  —  ww- %asö  (sd.)  gairis  parmtarim  °c,5  (AD.) manuiahe  YL/p.i.  [V.  5.19,  5.33,  Yl j".6o:  lies  antar».am>m^
KonipA.,E.  —  «i.aj-aMfl- Adj. 'halb',  m. 'Hälfte', ördha-  m.  'Sei(e';  oss.  ärdäg  'halb,  Hälfte'.  — Vgl.  arilah:  —  Pö. :  kanär  (dat  n  a,  vgl.  dal  r ; bei  Salemann  Porsenhdschr.  öS  II  Z.  5,  6).
•  p.  arda-stina-  m.  'Halbstand">j  bau- licher Kunstausdruck  "',vlL'Fensterkrönung' oder-  '-sims':  "«a*  a'it^gaini^  därayO^- vahaul  vt^iyä  karta''  Q.^.
>)  Falsch  FrMüiler  WZKM.  3. 149,  Fov  KZ. ^j.48  (vgL  or.'fa;*-,  trizräspa-),  JusTlGlrl'h.  2. 4SI  No-  Choch'  wäre  *ariiin/a-).  —  s)  Eü. umschreibt  blot.
p.  ardiixiastix'   Ao.  3:    s.   arlaxsa%''a-   mit No.  4.
```


## [2026-09-04T23:07:21.811Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"tariff\" KLN_1966.txt | head -10; echo \"=== 1971\"; grep -n \"tariff\" KLN_1971.txt | head -10",
 "description": "grep Klein for tariff"
}
```


### [2026-09-04T23:07:21.964Z] TOOL RESULT

```
1846:‘to  tax’,  fr.  VL.  *afforare ,  fr.  ad-  and  L.  forum, ‘public  place,  market’,  in  VL.  also  ‘market  price, tariff’  (whence  OF.  fuer,  ‘price,  tariff,  tax).  See forum.
38218:tariff,  n.  —  Sp.-Port.  tarifa,  fr.  Arab,  ta'rtf,  ‘a making  known,  information',  verbal  noun  of ‘arrafa,  ‘he  made  known,  he  taught’,  second conjugation  of  'drafu,  ‘he  knew’.  Cp.  It.  tariffa. Derivative:  tariff,  tr.  v.
=== 1971
8765:tariff’ (whence OF. fuer , ‘price, tariff, tax). See 
241463:tariff, n. — Sp.-Port. tari/a, fr. Arab. ta'rif, *a 
241466:conjugation of 'ara/a, ‘he knew’. Cp. It. tariffa. 
241467:Derivative: tariff, tr. v.
```


## [2026-09-04T23:07:22.966Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"tariff\\|ta'rif\\|taʿrīf\" AHD_watkins1985.txt | head -10; echo \"=== SKT\"; grep -n \"tariff\" SKT.txt | head; echo \"=== LKT\"; grep -n -i \"tarif\" LKT.txt | head -20",
 "description": "grep AHD, Skeat, Lokotsch for tariff"
}
```


### [2026-09-04T23:07:23.048Z] TOOL RESULT

```
=== SKT
19202:Tariff.  (F.- Span. -Arab.)  F.  tartfe. a  casting  of  accounts. —  Span,  tarifa,  a  list of  prices,  book  of  rates.  —  Arab,  tariff giving  information,  notification  (because  a tariff  gives  notice}.  — Arab,  'arf,  knowing, knowledge.  — Arab  root  'ara/a,  he  knew.
23699:French  from  Spanish  from  Arabic,  am* ber,  cotton  (i),  fonfnre,  galingale,  garble, garbage,  genet,  ;ennet  (genact),  lackey Jacquey).  mojJc  (masque),  masquerade, mosque,  ogee  (ogive),  racket  (1)  traquct), realgar,  ream,  »umach,  syrup  (sinip),  tabby, talc,  tare  (3),  tariff,  zenith,
=== LKT
3290:'Befehl,  Erlaß",  plr.  maräsim;  hieraus sp.  kat.  orancel,  sp.  alancel,  pg.  aranzel 'Erlaß,  durch  den  der  Preis  einer  Ware festgesetzt  wird;  offizieller  Tarif;  Zoll- tarif.' [DE  l'J7.  Eguilaz  271/!27!2  (wo  als Grundwort  ar.  si'r,  plr.  as'är  'Preis' angegeben  wird).
4580:2037.  Ar.  ta'rif: 'Bekanntmachung'  [subst.  Inf,  II  vom Vb.  'arafa  'wissen'];  hieraus  it.  tariffa 'Warenverzeichnis',  frz.  tarif,  sp.  pg. tarifo,  rum.  tarif,  Vb.  tarif a  'besteuern'; ndl.  tarief,  dtsch.  Tarif,  engl,  tariff 'Warenverzeichnis,  Preisliste';  russ.  tarif, cech.  tarifa,  poln.  taryfa.  [DE  348. Eguilaz  503.    ML  8583.
4645:2070.  Hebr.  terecpä: 'Zerrissenes  Fleisch',  daher  'unreine Speise';  aus  dem  Subst.  wurde  das  Adj. 'rituell  ungenießbar',  daraus  'uni-ein, schlecht,  ungerecht';  hieraus  it.  (Gergo) tarif,  taref  'stinkend'  [vgl.  G.  J.  Ascoli. Studi  orienlali  e  linguistici.  Milano  1854. S.402],  prov.  trefa,  ^ra/'ans 'betrügerisch', sp.  trefe  'falsch,  treulos,  schwach',  pg. treto,  trefego  'verschmitzt,  arglistig'; jiddisch  träif  'rituell  ungenielabar',  mit slav.  Endung  träifnak  'Trefeesser,  d.  h. •Jude'  [Birnbaum  HebrEl  .52  und  53];
5881:Tabaschir  1965 To&m  133 Trtfcor  1974 Trtt^f  1972 Tabnrett  483 Tw/f^i  1981 rrt/-^  1981 TagaK  Stroh)  1982 Taz/Mw  1990 Talisman  2077 TaZfc  2003 Tamarinde  2013 Tamariske  2013 Tamtam  2014 Tarife  2017 Tanner  j.  20 19 T«m  2024 Tarbusch  2031 Trtrty  2037 tärkis  mhd.  2081 ^rtroc^•  2024 2044
```


## [2026-09-04T23:07:37.244Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"tariff,  n.  —  Sp.-Port.\")\nleaf=t.count('\\f',0,i); print('KLN tariff leaf',leaf,'~printed',(leaf-12)*2)\nj=t.find(\"'arafa,  'he  knew'\")\nEOF\necho \"=== WEB tariff\"; grep -n -i \"tariff\" WEB_vol1.txt | head -5; echo \"=== FSD\"; grep -l . FSD_vol*.txt >/dev/null; grep -n -i \"tariff\" FSD_vol4.txt | head -5",
 "description": "Klein page and Webster/FSD tariff"
}
```


### [2026-09-04T23:07:39.055Z] TOOL RESULT

```
KLN tariff leaf 834 ~printed 1644
=== WEB tariff
6089:al’tér-nate, v.t.; alternated, pt., pp.; alterna- ting, ppr. to perform by turns, or in succes- sion; to cause to succeed by turns; to change (one thing for another) reciprocally; as, con- gress allernated a high tariff with a low one.
6613:å-men’ty, n. amentia. [Obs.] am/é-nuse, v.t. to diminish. {Obs.} F å mērce’, v.f.; amerced, pt., pp.: eee Pr. (ME. amercen, amercien; OFr. amercter, from : a merci, at the ey of, liable to punishment. A to fine or inflict other penalty upon as ieg 4 punishment. : 4-mérce’a-ble, a. subject to amercement; jus- tifying amercement. = a-mérce/ment, n. 1. a penalty imposed on an offender at the discretion of the inflicter, specifically, the court. It differs from a fine, in that the latter is, or was originally, a fixed and certain sum prescribed by statute for an offense, while an amercement is at the dis- cretion of the court. 2. the imposing of such a penalty. a-mér’cér, n. one who amerces. a-mér’ci-a-ment (or -sha-), n. same as amerce- ment. A-mer‘i-cin, a. [from America, and -an: de- rived from Americus Vespucius. the Latin name of Amerigo Vespucci (1451-1512), Ital- jan navigator.| 1. of or in North or South America, or North America, South America, and Central America considered together. = 2. of, in, or characteristic of the United States, its people, etc.; as, the American lan- guage. American aloe; a century plant, American Beauty; a variety of hybrid, per- ennial red rose. American cheese; a kind of fairly hard, mild Cheddar cheese, popular in the United States. American eagle: the bald eagle of North America, shown on the coat of arms of the United States. American English; the English language as spoken and writ- ten in the United States: usually dis- tinguished from Brit- ish English. American Indian; a member of any of the aboriginal races of North America, South America, or the West Indies: they were named Indians from the belief, held by early explorers, that these regions were part of Asia. American ivy; the Virginia creeper. American Labor Party; a political party of New York State, founded in 1936. American leopard; a jaguar. American Party; a secret political party in existence from _ 1853 to 1856, whose object was to exclude foreign-born citizens Írom par- ticipating in government: called also the Know-Nothing party because members pro- fessed ignorance of the party's activities. _ American plan; a system of hotel operation 3 in which the price charged to guests covers room, service, and meals: distinguished from European plan. „American Protective Association; a secret so- ciety formed in Iowa, in 1887, for the purpose of keeping Roman Catholics out oF public office, professedly to protect American insti- = tutions. 7 z „American Revolution; (a) a sequence of ac- tions by American colonists from 1763 to 1783 protesting British domination and culmina- ting in the Revolutionary War; (b) the Revo- lutionary War (1775-1783), tought by the American colonies for ind lence from Bago ek merican screw gauge; a stan auge for checking the diameter of wood ee and machine screws. ae American system; the origi nami protective tariff system of the United Si _ Native American Party, a short-lived ical party, organized about 1843, whose was somewhat similar to that of th ican (Know-Nothing) Party. > A-mer‘i-cin, n. 1. a native or inhabit: America; originally, any of the abor EAN o that . a citizen of the Uni i 3. the English language as s eae Sone sas ) : -mer”i-can’a (or -kan-å, -kan-a), n.pl. relating to America, as a ru raphy, geography. litera: A-mer’i-cin Fed ‘tion
47800:cus: to’dés, n. plural of custos. 2 cus-t6/di-a, n.; pl. cus-t6/di-ae, (L., guard, a £ Pat a custodial, sete -ăl, a. relating to custody or custo- ians. 4 cus-t6/di-4l, n. a container for relics. J cus tõ’'di-ăn, n. (L. custodia, a watch, guard; Se custodire, to guard.} i 1. one who has the care of something, as of the exhibits in a museum; a caretaker; a keeper. y 2. one who is responsible for the care and maintenance of a building; a janitor. cus-t0/di-An-ship, n. the position or work of a custodian. =i cus-t0/di-ér, n. a custodian. lom 3 cus’/té-dy, n. pl. cus’t6-dies, {L. custodia, a watch, guard, from custos, a watchman; Gr. keuthein, to hide, conceal, _ 1. a keeping safe or guarding; care; protec- tion; guardianship. $ fe imprisonment; confinement; restraint of iberty. cus’tém, n. [ME. custom, custome; OFr, cos- tume, custom; from L. consuetudo, custom, habit, from consuescere, to accustom, habit- uate, from com-, intens., and suescere, to become accustomed, from suere, to be ac- customed.] 3 1. frequent or common use or practice; a meaai repetition of the same act; usage; abit. = = 2. established usage; social conventions carried on by tradition and enforced by social disapproval of any violation. a, ee 3. a service, rent, etc. regularly paid to a feudal lord. i 4. [pl.] (a) duties or taxes imposed government on impo and, occasior exported goods; (b) the government a; Bots of coucon these duties. . the regular support or patronage ee ratte a > . in law, such usage as by long-estab uniform practice and common consent taken on the force of law. : $ custom of merchants; the code or law in commerce which governs exchange, insurance, etc. x> customs union; a union of twi tions that agree to eliminate tions among them and to | tariff policy toward all oth Syn.—habit, practice, ©
55774:plying any public discriminations in mat- ters of religion. , —Gauden. syn.—discernment, penetration, | clearness, acuteness, acumen, judgment, distinction. dis-crim/i-na-tive, a. marked by or observing discrimination; discriminating; as, a discrimi- native decision, discriminative tariffs. _ i is-crim/i-na tively, adv. with discrimination
77761:free list; the list of articles or goods not sub- aie to import or export tariff duties; also, a list of persons entitled to free admission (as y to an exhibition, a museum, etc.), or entitled ; ee ee copies (as of a book, magazine, etc). ree on board; delivered (by the seller) aboard cas the train, ship, ete. at the point of shipment, ia without further charge to the buyer. 3 free port; a port or guarded district in a port, open equally to ships of all countries, where imported and exported goods are not subject to duties or taxes. free services; in the feudal system, services that might be performed by a soldier or free- man, as to serve under his lord in time of war, to contribute money, etc.
=== FSD
20663:and  carbohydrates  —   Dutch  8.,  a   standard  formerly nized  in  commercial  usage  and  In  tariff  legislation  relating to  qualities  or  grades  of  sugar  It  consLsUd  of  10  samplMp representing  as  many  different  grades  of  puilty  from  tno darkest  to  the  whlicfit,  put  up  In  I'Otlles  under  the  seal  oi the  Dutch  government.
20715:partj  In  power  spMlf  a   iwlitic.an  who  advocates  n^n-  sfa'Dls-lau,’  1   sta'nis-Iou  3   sta'nls-lou.  n   A   town  In  S   E talnlng  the  existing  tariff  schedules  (<  stand  +   pat,  odr  j   pniftnci
23845:one  who  straddles,  a   going,  standing,  or  sitting  with legs  wide  apart  2.  The  space  between  the  feet  or  legs of  one  vho  straddles,  as,  a   small  straddle.  3.  Finance. A   stock-transaction  in  which  the  buyer  obtains  tho privilege  of  either  a   put  or  a   call,  spread  4.  [Slang) An  equiv  ocal  position  in  regard  to  a   question  or  contro- versy, a   hedgmg,  as,  a   straddle  on  the  tariff  5   In poker,  the  doubling  of  a   blind  6-  A   vertical  mine* timber,  especially  one  supporting  a   set —   strad'dle*bug",  n   {U.  S]  1.  A   scarabajld  beetle (genus  Carahyon)  having  long  legs  2.  A   two-faced  poli- tician —   s.degged*  a   Having  the  legs  far  apart  or  astride of  something  —   s.smlll,  n   A   milling-machine  so  made  that Itapartsstraddletheworktobedoncand  finish  sides  and  top atthesometlme  — 8   »plpe,  ft  A   pipe  connecting  uprights, as  the  stand-pipe  from  a   gas-retort  with  the  hj  draullc  main.
29386:neoulaTitp  applies  to  even  disposition  of  objects  or  uniform recurrence  of  acta  in  a   scries  There  may  be  regularUv without  order,  as  In  the  recurrence  of  paroxysms  of  disease or  Insanity,  there  may  be  order  without  regularttp,  as  In  the arrangement  of  lumliuroln  a   room,  where  the  objects  arc placed  at  varying  distances  Order  commonly  implies  the design  of  an  Intelligent  agent  or  the  appearance  or  sugges- tlon  of  such  design,  regularitp  applies  to  an  actual  uniform disposition  or  recurrence  w   Ith  no  suggestion  of  purpose,  and as  applied  to  human  affairs  Is  less  Intelligent  and  more  me- chanical than  order  The  most  perfect  order  Is  often  secured with  least  regularity,  as  in  a   fine  essay  or  oration  The  same may  be  said  of  system  There  Is  a   regularUp  of  dividing  a treatise  Into  topics,  paragraphs,  and  sentences,  that  Is  de- Btructlvc  of  true  rhetorical  aj/rfem  See  body,  economy fraaie,  habit,  inTOTHFsis  —   Ant.,  chaos,  confusion,  de^ rangement,  disarrangement,  disorder.  Irregularity —   Abt  or  Fell  sjstcm,  sec  apt  rvck  under  rack  — American  s   ,   that  tariff  policy  which  alms  to  promote national  prosperity  by  stimulating  and  guarding  home ^dustrlcs  by  means  of  a   high  protective  import  tax  — Berger  s,  (Chess),  a   universal  system  of  chess-nota- tion, in  which  the  moves  arc  desl^aled  by  letters  and numbers  See  Ulus  under  chess  r   —   caring  s   (Min- ing), a   system  pursued  In  mining  whereby  the  wo-ked* out  chambers  are  allowed  to  cave  In  Compare  ixjng- VVALL  8Y8TFM  —   centrobarlc  s   ,   a   rigid  system  or  body In  which  tho  action  of  gravity  Is  reducible  to  a   single force  passing  through  one  point,  fixed  relatively  to  such system,  and  known  as  the  center  of  gravity —   closed  s. (Math ),  a   system  such  that  the  result  of  any  combination  of Its  elements  will  still  be  a   number  of  the  same  system  —   con- densed s   (Phps  Cficm  ),  a   systemwithout  a   gaseousphase
30878:It  u   the  public  that  is  not  represented  m   the  lobby  when  the tanff  IS  undergoing  manipulation  James  Pabtov  Tojnet  of  iho Time,  Log^Rollino  tn  Waihinoton  p   261  [o  «   co  1871 1 2*  A   duty  levied  according  to  such  a   schedule,  or  such duties  collectively,  especially  on  one  class  of  articles,  im- post, as,  the  tariff  on  silk  3.  The  latv  m   which  a   sched- ule of  duties  is  fixed  and  imposed,  also,  the  prmciples, in  general,  governing  the  imposition  of  duties,  as,  the tanff  of  1890,  to  discuss  the  tariff  4.  Any  list  or schedule  of  charges,  as,  a   rmlway  fart^,  a   hotel  tanff 5.  [CoUoq  ]   The  pnee  or  charge  for  an  article  a   humor- ous use,  as,  what’s  the  tanff t   [<  F   tanf,  <   Sp tanfa,  <   Ar  tarif,  <   *arafa,  know  1
```


## [2026-09-04T23:07:47.291Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T23:07:47.298Z] TOOL RESULT

```


```


## [2026-09-04T23:07:50.808Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tariff",
 "prompt": "Full etymology of \"tariff\": what languages are in the chain (Italian, Spanish, Turkish, Arabic), the Arabic form and root, and any note about Medieval Latin or the Spanish port Tarifa folk etymology."
}
```


## [2026-09-04T23:07:51.734Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/tariff",
 "prompt": "Give the full etymology section for the English noun tariff: intermediate languages, Arabic form تعريف, and any mention of Turkish tarife or Spanish tarifa."
}
```


### [2026-09-04T23:07:57.309Z] TOOL RESULT

```
# Etymology of "Tariff"

## Language Chain

The word travels through these languages: **Arabic → Medieval Latin → Italian → English**

## The Etymology Path

The term originates from Arabic **ta'rif** ("information, notification, a making known"), derived from the verb **arafa** ("he made known, he taught"). It passed into Medieval Latin as **tarifa** ("list of prices, book of rates"), then into Italian **tariffa** ("tariff, price, assessment") before entering English around the 1590s.

## Key Details

According to the source, the word entered English "from the commercial jargon of the medieval Mediterranean" and belonged to a group of trade-related terms adopted during this period, including garble, jar, average, orange, and tabby.

## Notable Points

The etymology notes that "a word passed to English from the commercial jargon of the medieval Mediterranean," indicating this was a practical borrowing among merchants rather than a folk etymology tied to the Spanish port of Tarifa. The source makes no mention of Turkish in the chain, and **does not support** the Tarifa port folk etymology sometimes attributed to this word.
```


### [2026-09-04T23:08:00.810Z] TOOL RESULT

```
# Etymology of English Noun "Tariff"

According to the Wiktionary entry, the word originates from Italian *tariffa* ("arithmetical table; list of customs duties"), which derives from Arabic *تَعْرِيف* (taʕrīf, "notification, explanation"). 

The entry notes this is "Equivalent to Portuguese and Spanish tarifa and the French tarif" and states the term was "first attested in 1592."

The etymology section does not mention Turkish *tarife* or provide additional details about the intermediate linguistic pathway beyond identifying Italian and Arabic as the primary sources.
```


## [2026-09-04T23:08:05.650Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=tariff",
 "prompt": "Give the exact bracketed etymology of the noun \"tariff\" as printed in the American Heritage Dictionary, including any Turkish, Italian, Spanish or Arabic forms."
}
```


## [2026-09-04T23:08:07.209Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%88%D8%A7%D8%B1%D9%88%D9%86",
 "prompt": "Give the Persian entry وارون: etymology (Middle Persian form, Old Iranian reconstruction), meaning, and any cited sources (Hasandust, MacKenzie, Nyberg)."
}
```


### [2026-09-04T23:08:10.355Z] TOOL RESULT

```
Based on the dictionary entry provided, the bracketed etymology of "tariff" is:

"[Italian _tariffa_, from Old Italian, from Arabic _ta'rīf_, notification, infinitive of _'arrafa_, to announce, derived stem of _'arafa_, to know; see **ʿrp** in the Appendix of Semitic roots]."

This etymology traces the word through Italian and Old Italian forms back to Arabic origins, with no Turkish or Spanish forms listed in this entry.
```


### [2026-09-04T23:08:13.668Z] TOOL RESULT

```
# Persian Entry: وارون (wārūn/vârun)

## Etymology
The word is inherited from Middle Persian (ʾp̄lʾlwn' /⁠abārōn⁠/, "contrary, wrong, sinful"), as documented in MacKenzie's Pahlavi dictionary.

## Meaning
The Persian adjective has two primary senses:

1. An alternative form of وارونه (wārūna/vârune), meaning "inverted"
2. In Classical Persian usage (figurative): "wicked, evil" or "pitiful"

## Cited Sources
The entry references **MacKenzie, D. N. (1971)**, *A concise Pahlavi dictionary* (Oxford University Press, page 2), which provides the Middle Persian etymological form and its meaning as "contrary, wrong, sinful."

The entry also lists the **Dehkhoda Dictionary** (compiled by Ali-Akbar Dehkhoda, 1931–) as further reading, though specific citations from that source are not detailed in this Wiktionary article.
```


## [2026-09-04T23:08:24.581Z] TOOL CALL #36: Bash

```json
{
 "command": "pdftoppm -f 63 -l 63 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg63 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg63.png",
 "description": "Render PDF page 63"
}
```


### [2026-09-04T23:08:27.782Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 59302 Sep  4 19:08 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg63.png
```


## [2026-09-04T23:08:29.992Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg63.png"
}
```


### [2026-09-04T23:08:30.586Z] TOOL RESULT

```

```


## [2026-09-04T23:08:30.584Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-04T23:08:46.422Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==835' KLN_1966.txt | head -c 1200; echo; echo \"-----\"; awk 'BEGIN{RS=\"\\f\"} NR==835' KLN_1966.txt | tail -c 600",
 "description": "Klein leaf 834 page markers"
}
```


### [2026-09-04T23:08:48.221Z] TOOL RESULT

```
 see  dram  and  cp.  target.  ML. targ(i)a,  OProvenq.  targa  (whence  It.  targa),  Sp. tarja,  ‘shield’,  are  also  Teut.  loan  words.  G. Tartsche,  ‘small  round  shield;  target’,  has  been re-borrowed  fr.  OF.  targa.
targe,  tr.  v.,  to  harass  with  questions  (Scot.)  — Of  uncertain  origin.
target,  n.  —  ME.,  fr.  MF.  targete  (F.  targette),  ‘a small  shield,  target’,  dimin.  of  targe.  See  targe, ‘shield’,  and  -et.
Derivatives:  target,  tr.  v.,  target-eer,  n.
Targum,  n.,  Aramaic  translation  of  the  Bible.  — Mishnaic  Heb.  targum,  ‘interpretation,  transla¬ tion’,  fr.  Heb.  tirgem,  ‘he interpreted,  translated’, which  is  rel.  to  Aram,  targem,  Arab,  tarjama,  of s.m.  All  these  verbs  are  denominated  fr.  Akkad. targumanu,  ‘interpreter’  (fr.  ragamu,  ‘to  call'), whence  also  Aram.  turgi mdna,  ‘interpreter, translated.  Cp.  meturgeman.  Cp.  also  dragoman. Derivatives:  Targum-ic,  adj.,  Targumist  ( q.v.)
Targumist,  n.,  1)  writer  of  a  Targum;  2)  student of  the  Targums.  —  Formed  fr.  Targum  with suff.  -ist.
Derivative:  Targumist-ic,  adj.
tariff,  n.  —  Sp.-P
-----
e  in  a  certain  direction’,  and cp.  ectasis  and  words  there  referred  to. Derivatives:  tasimetr-ic,  adj.,  tasimetr-y,  n. task,  n.  — -  ME.  taske,  fr.  ONF.  tasque,  fr.  OF. tasche  (F.  tache)  fr.  VL.  *tasca,  metathesized  fr. ML.  taxa,  which  is  a  back  formation  fr.  L.  ta- xare,  ‘to  touch  sharply,  handle;  to  appraise, estimate’.  See  tax  and  cp.  tasse  and  the  second element  in  sabretache.
tass,  n. ,  a  drinking  cup ;  a  small  draft.— M  F.  ( =  F.) tasse,  ‘cup’,  fr.  OF.,  fr.  Arab.  tassah,  tass,  fr. Pers.  tdsht,  ’cu
```


## [2026-09-04T23:09:02.070Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 799 800; do echo \"=== leaf $n\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -c 700; echo; done",
 "description": "Klein leaf 799"
}
```


### [2026-09-04T23:09:04.284Z] TOOL RESULT

```
=== leaf 799
��starboard’,  are  Teut.  loan  words.  See  steer,  ‘to direct’,  and  board.
starch,  n.  —  ME.  sterche,  starche,  back  forma¬ tion  fr.  sterchen,  ‘to  starch’,  fr.  OE.  stercan,  ‘to stiffen’,  fr.  stearc,  ‘stiff’.  Cp.  G.  Starke,  ‘strength ; starch’,  and  see  stark.
Derivatives:  starch,  adj.  and  tr.  v.,  starch-ed, adj.,  starch-ed-ly,  adv.,  starch-ed-ness,  n.,  starch- y,  adj.,  starch-i-ly,  adv.,  starch-i-ness,  n. stare,  intr.  and  tr.  v.  —  ME.  staren,  fr.  OE.  sta- rian,  ‘to  look  fixedly  at’,  rel.  to  ON.  stara, MLG.,  MDu.  staren,  Du.  staren,  OHG.  staren, MHG.  starn  (whence  G.  starred),  ‘to  loo
=== leaf 800
ic  and  -ics.
statistology,  n.,  the  study  of  statistics.  —  A  hy¬ brid  coined  fr.  statistics,  a  word  of  L.  origin,  and Gk.  -Xoyia,  fr.  -X6yoc,  ‘one  who  speaks  (in  a certain  manner) ;  one  who  deals  (with  a  certain topic)’.  See  -logy.
stato-,  combining  form  meaning  ‘standing,  fixed’.
—  Gk.  axaxo-,  fr.  axxxo?,  ‘standing’.  See static.
stato-,  combining  form  meaning  ‘state’.  —  See state.
statoblast,  n.,  a  winter  bud  (zool.)  —  Compound¬ ed  of  stato-  ‘fixed’,  and  Gk.  flXaaxd?,  ‘bud, sprout,  shoot’.  See  -blast, stator,  n.,  the  stationary  part  in  a  power  genera¬ tor.  —  ModL.,  formed  fr
```


## [2026-09-04T23:09:14.801Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pat in [\"cherub,  n.\",\"tariff,  n.\",\"paradise,  n.\"]:\n    i=t.find(pat)\n    print(pat, 'leaf', t.count('\\f',0,i) if i>=0 else 'NF')\nEOF",
 "description": "calibrate Klein leaves"
}
```


### [2026-09-04T23:09:16.584Z] TOOL RESULT

```
cherub,  n. leaf 155
tariff,  n. leaf 834
paradise,  n. leaf 600
```


## [2026-09-04T23:09:34.709Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('total leaves',len(pages))\nimport re\nfor n in (154,155,833,834,835):\n    p=pages[n]\n    nums=re.findall(r'\\b1?\\d{2,4}\\b',p[:200]+p[-200:])\n    print(n, repr(p[:80]), '|END|', repr(p[-90:]))\nEOF",
 "description": "Look for page numbers in Klein OCR"
}
```


### [2026-09-04T23:09:36.786Z] TOOL RESULT

```
total leaves 903
154 ' color’,  fr.  T.-E.  base  *ska(i)-, ‘to  shine,  flicker,  glimmer’.  See  ski' |END| 'ise.  See chemise  and  -ette.\nchemist,  n.  —  F.  chimiste,  fr.  chimie,  ‘chemistry’. '
155 'See  alchemy  and  -ist.  Derivative:  chemist-ry,  n. chemo-,  combining  form ' |END| 'Derivatives:  chican-er,  n.,  chicanery  (q.v.) chicanery,  n.,  trickery,  quibbling,  s'
833 'cp.  the  first  element  in tandem.  Cp.  also  taunt.  Cp.  also  the  first  ' |END| 'perly  ’to  en¬ close’,  8pxyjj.7),  ‘drachma’,  Spiyua,  ‘a  sheaf’, lit.  ‘a  handful’; '
834 ' see  dram  and  cp.  target.  ML. targ(i)a,  OProvenq.  targa  (whence  It.  ta' |END| 'F.  ( =  F.) tasse,  ‘cup’,  fr.  OF.,  fr.  Arab.  tassah,  tass,  fr. Pers.  tdsht,  ’cu'
835 'p,  saucer’.  Cp.  OProveng.  tassa, It.  tazza,  Sp.  taza,  ‘cup’,  which  are' |END| 'the  pine  family  (bot.)  —  ModL., formed  fr.  Taxus  with  suff.  -aceae. taxation,  n'
```


## [2026-09-04T23:10:02.599Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"arafa\\|'arrafa\\|‘arrafa\" KLN_1966.txt | head -10; echo \"=== KLN 'Arafat/marifa'\"; grep -n -i \"ma'rifa\\|arif\" KLN_1966.txt | head -10",
 "description": "grep Klein for arafa"
}
```


### [2026-09-04T23:10:02.670Z] TOOL RESULT

```
3613:Derivatives:  ashlar-ed,  adj.,  ashlar-ing ,  n. ashore,  adv.  —  Formed  fr.  a-  ‘on’,  and  shore, ashrafi,  n.,  name  of  various  gold  coins,  esp.  a gold  coin  in  Persia.  —  Pers.,  fr.  Arab. dshraf,  lit.  ‘noble  ones’,  pi-  of  shar.f,  ‘noble’, fr.  sharafa,  ‘he  was  exalted,  he  was  noble  . See  shereef  and  cp.  words  there  referred  to. ashrama,  n„  hermitage  (Hinduism).  —  Ol.  dsrd- mah,  fr.  adnominal  pref.  d-  and  srdmah,  ‘effort, toil,  fatigue’,  whence  srdmyati,  ‘he  becomes tired’,  which  is  rel.  to  OI.  kldmyati,  kldmati,  ‘he slackens,  languishes’  and  cogn.  with  OSlav. kromiti,  ‘to  tame’,  chromii,  ‘lame’.
6490:caracara,  n.,  a  kind  of  large  South  American bird.  —  A  Tupi  word  of  imitative  origin, carack,  n.  —  See  carrack. caracole,  n.,  half-turn  in  riding.  —  F.,  fr.  Sp. caracol,  lit.  ‘snail’,  which  is  prob.  a  blend  of L.  scarabaeus,  ‘a  beetle’,  and  conchylium  (fr.  Gk. xoyxuXiov),  ‘a  shell  fish’.  See  scarab  and  cockle, caracole,  intr.  v.,  to  make  a  caracole.  —  F.  cara- coler,  fr.  caracole.  See  caracole,  n. carafe,  n.,  a  glass  bottle.  —  F.,  fr.  Sp.  garrafa,  fr. Arab,  gharrdf  ‘drinking  jug’,  fr.  gharafa,  ‘he drew  water’.
6735:catafalque,  n.,  a  temporary  structure  used  at  fu¬ nerals.  — •  F.,  fr.  it.  catafalco ,  fr.  VL.  *carafali- cum  (whence  also  OF.  chafaud ,  F.  echafaud , ’scaffold'),  which  is  formed  fr.  cata-  and  L  .fata, ’a  wooden  tower  (from  which  missiles  were thrown  into  a  besieged  city);  scaffolding',  a word  of  Etruscan  origin.  Cp.  scaffold.
34964:sherd,  n.,  a  fragment.  —  A  var.  of  shard, shereef,  sherif,  n.,  1)  a  descendant  of  Mohammed through  his  daughter  Fatima;  2)  the  governor of  Mecca.  —  Arab,  sharif  (in  vulgar  pronuncia¬ tion  sherif),  ‘noble’,  fr.  sharafa,  ‘he  was  exalted, was  noble’.  Cp.  ashrafi,  tashrif,  xerafim. Derivative:  shereef-ian,  sherif-ian,  adj. sheriff,  n.  —  ME.  shereve,  fr.  OE.  scir-gerefa, ‘president  of  a  shire’,  which  is  compounded  of scir,  ‘shire’,  and  gerefa,  ‘officer,  governor’.  See shire  and  reeve,  ‘official’.
35077:shroff,  n.,  name  of  a  money  changer  in  the  Far East.  —  Hind,  sarraf,  fr.  Arab,  sarrdj,  ‘money changer’,  fr.  sarrafa,  ‘he  changed  money’, second  conjugation  of  sarafa,  'he  turned’, shroud,  n.  —  ME.  schrud,  shrud,  shroud,  fr.  OE. scrud,  ‘dress,  garment’,  rel.  to  ON.  skrud,  ’the shrouds  of  a  ship,  ornament,  furniture  of  a church’,  Dan.,  Swed.  skrud,  ‘dress,  attire’,  and in  gradational  relationship  to  OE.  screade, scread,  ‘shred,  paring’.  See  shred,  n. Derivatives:  shroud,  tr.  v.,  shroud-ed,  adj., shroud-ing,  n.,  shroud-less,  adj.,  shroud-y,  adj. Shrovetide,  n.,  the  time  for  confession  before Lent.  —  ME.  shroftide,  schroftide-,  compounded
38218:tariff,  n.  —  Sp.-Port.  tarifa,  fr.  Arab,  ta'rtf,  ‘a making  known,  information',  verbal  noun  of ‘arrafa,  ‘he  made  known,  he  taught’,  second conjugation  of  'drafu,  ‘he  knew’.  Cp.  It.  tariffa. Derivative:  tariff,  tr.  v.
38646:terephah,  n.,  also  spelled  trefa,  rituaUy  undean food  (Jewish  religion).  —  MedHeb.  t  repha  ,  fr. Mishnaic  Heb.,  ‘an  animal  with  organic  defect', fr.  Bibl.  Heb.,  lit.  ‘(an  animal)  torn  (by  wild beasts)’,  fr.  tardph,  ‘tore  to  pieces,  seized,  rent’ (said  esp.  of  a  wild  beast),  whence  also  tereplt, ‘prey’,  tardph,  ‘plucked’  (adj.);  rel.  to  Aram. fraph,  ‘he  tore,  seized’,  Arab,  tarafa,  ‘grazed off’  (said  of  a  camel),  tarufa,  ‘was  freshly  pluck¬ ed’.
=== KLN 'Arafat/marifa'
1302:acarid,  n.,  a  mite.  —  Formed  with  subst.  suff. -id  fr.  Gk.  axapt,  ‘mite’,  which  is  rel.  to  axap^, ‘small,  tiny’,  lit.  ‘too  short  to  be  cut’,  and  in gradational  relationship  to  xcipeiv  (for  *xeptsiv), ‘to  cut’.  See  shear  and  cp.  words  there  referred to.  Cp.  also  Acarina,  Acarus,  carnal, acariform,  adj.,  of  the  shape  of  a  mite.  —  A  hy¬ brid  coined  fr.  Gk.  dxapt,  ‘mite’,  and  L  .forma, ‘form,  shape’.  Sce  acarid  and  form,  n.
1846:‘to  tax’,  fr.  VL.  *afforare ,  fr.  ad-  and  L.  forum, ‘public  place,  market’,  in  VL.  also  ‘market  price, tariff’  (whence  OF.  fuer,  ‘price,  tariff,  tax).  See forum.
7831:claret,  n.,  a  red  wine.  —  ME.,  prop,  ‘a  clarified wine’,  fr.  OF.  claret,  used  as  a  noun  for  vin claret,  lit.  ‘clear  wine’,  whence  F.  (vin)  clairet; dimin.  of  OF.  cler  (F.  clair),  fr.  L.  cldrus.  See
7835:clarification,  n.  —  F.,  fr.  Late  L.  clarificatidnem, acc.  of  eldrificatio,  ‘glorification’,  fr.  clarificatus, pp.  of  clarificdre.  See  next  word  and  -ation. clarify,  tr.  and  intr.  v.  —  OF.  clarifier,  fr.  Late L.  clarificdre,  ‘to  glorify’,  fr.  L.  cldrus,  ‘bright, shining,  clear,  glorious’,  and  -ficare,  fr.  facere, ‘to  make,  do’.  See  clear  and  -fy.
7836:Derivative:  clarifi-er,  n.
7870:Derivatives:  cleanser  (q.v.),  deans-ing,  n. cleanser,  n.  —  OE.  clinsere,  fr.  dinsian.  See prec.  word  and  agential  suff.  -er. dear,  adj.  —  ME.  cler,  deer,  fr.  OF.  cler,  clier (F.  clair),  fr.  L.  clarus,  ‘bright,  shining,  clear, plain,  manifest,  illustrious,  famous,  glorious’, which  stands  for  cla-rus,  and  is  rel.  to  cla-mare, ‘to  call,  cry  out,  shout,  declare’,  fr.  I.-E.  base *kld-,  var.  of  *kal-,  ‘to  shout,  resound'.  See calends,  and  cp.  claim.  Cp.  also  claret,  clarify, Clara,  clarin,  clarinet,  clarion,  clarity,  declare, eclair,  glair,  the  first  element  in  clairaudience, clairvoyance,  chiaroscuro  and  the  second  element in  chanticleer.
16100:Gheber,  Ghebre,n.,  a  member  of  the  Persian  sect of  fireworshipers.  —  F.  guebre,  fr.  Pers.  gabr, ‘fireworshiper’ ;  not  borrowed  fr.  Arab,  kafir, ‘unbeliever’  (as  most  lexicographers  would  have it),  but  a  native  Persian  word.  Cp.  giaour, ghee,  n.,  boiled  butter  {India).  —  Hind,  ghi,  fr. OI.  ghrtdm,  ‘clarified  butter,  ghee’,  which  is cogn.  with  Mir.  gert,  ‘milk’,  and  prob.  rel.  to OI.  jigharti,  ‘besprinkles’.
16414:Gomphrena,  n.,  a  genus  of  plants  of  the  family Amaranthaceae  (hot.)  —  Altered  fr.  L.  grom- phaena,  name  of  a  kind  of  amaranth, gomroon,  n.  —  See  gombroon, gomuti,  n.,  a  palm  growing  in  the  Archipelago (Arenga  saccharifera).  —  Malay  gumuti. gon-,  form  of  gono-  before  a  vowel.
16617:Derivative:  grave-less,  adj. grave,  tr.  v.,  to  clean  (the  wooden  hull  of  a  ship) of  grass,  etc.  —  OF.  grave  (F.  grive),  ‘strand of  sand,  sandbank’.  See  gravel  and  cp.  Graves, grave,  adj.,  weighty.  —  F.,  fr.  L.  gravis,  ‘heavy, weighty;  troublesome,  painful,  grievous,  hard; important,  honorable’,  which  is  cogn.  with  OI. gurufi,  ‘heavy,  weighty’  (compar.  gariyas-; superl.  garifthah),  Avestic  gouru-  (only  in  com¬ pounds),  ‘heavy,  weighty’,  Gk.  (Japoi;,  ‘weight’, ^apu?,  ‘heavy’,  Pptffeiv,  ‘to  be  laden  with’ ,  Ppiffu?, ‘heavy’,  ppuxp6e,  ‘strong’,  Goth,  kaurus,  ‘heavy’, Lett,  grids,  ‘heavy’.  Cp.  gravedo,  gravid,  gravity, grief,  grieve,  grievous,  aggravate,  aggrieve,  in¬ gravescent.  Cp.  also  baro-,  bary,  Briareus,  brute, centrobaric,  charivari,  garce,  guru,  isobar, grave,  n.,  a  count;  used  esp.  of  the  counts  of Nassau.  —  MDu.  grave  (whence  Du.  graaf), ‘count’,  rel.  to  OHG.  gravo  (whence  MHG. grave,  G.  Graf),  MLG.  grive  (whence  ON. greifi,  Dan.,  Swed.  greve),  ‘count’.  The  orig.
20554:Kavi,  Kawi,  n.,  the  ancient  language  of  Java.  — Javanese  kavi,  ‘poetic  (scil.  language)’,  fr.  OI. kavih,  ‘wise,  sage;  seer,  poet’,  which  is  rel.  to kavarifi,  ‘stingy’,  a-kuvate,  ‘intends’,  and  cogn. with  Gk.  xoew  (for  *xoF£u),  ‘I  mark,  perceive, hear’,  fr.  I.-E.  base  *(s)qSu-,  ‘to  look  at,  observe, perceive’,  whence  also  OE.  sceawian,  ‘to  look, see'.  See  show  and  cp.  words  there  referred  to. kayak,  n.,  an  Eskimo  canoe  made  of  sealskin stretched  on  a  wooden  frame.  —  Eskimo, kea,  n.,  a  large  New  Zealand  parrot.  —  Maori, keck,  intr.  v„  to  retch.  —  Imitative.
```


## [2026-09-04T23:10:20.375Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ 'arafa\"; grep -n -i \"arafa\\|ma'rifa\\|'urf\" FVQ.txt | head -8; echo; echo \"=== TAD\"; grep -n \"تعرفه\\|عرفان\" TAD.txt | head -5; echo \"=== ARB\"; grep -n \"تعرفه\\|عرفان\" ARB_mo3rb.txt | head -5; echo \"=== AFM\"; grep -n \"عرفان\\|تعرفه\" AFM.txt | head -5",
 "description": "grep Semitic books for erfan/ta'refeh"
}
```


### [2026-09-04T23:10:20.465Z] TOOL RESULT

```
=== FVQ 'arafa
1417:Tarafa and his uncle Mutalammis, Al-Harith b. Hilliza, ; Amr b. 
7047:and Tarafa, Mrfalkiqa, 38. The sense of to reap, however, is denomina- 
9335:and also in the old poetry, cf. the Mu'allaqa of Tarafa, 1. 23 (Horovitz, 
11809:and in a verse of Tarafa, 
14728:Tarafa in his Mu'allaqa, 1. 31, seems to look on ^u^* as something 
15838:of plank, cf. Tarafa iv, 12 ; Imru'ul-Qais, x, 13, and Zuhair, i, 23 

=== TAD
=== ARB
14637:قصص الأندياء» و يأنى بألفاظ كثيرة لا تعرفها العرب » يأخذها من الككتب اأنق_دمة 6 و بأحاديث من 
17585:كزلك جاء قْ التفسير :5 وقد قيل : ” الف 1 تعرفه ادرب ولممى الموضع 
=== AFM
```


## [2026-09-04T23:10:22.184Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v3 erfan\"; grep -n \"عرفان\" incoming/BQT/BQT_v3_pages.txt | head -5; echo \"=== MON erfan\"; grep -n \"عرفان\" MON_part1.txt MON_part2.txt | head -5; echo \"=== MON tarefeh\"; grep -n \"تعرفه\" MON_part1.txt MON_part2.txt | head -5",
 "description": "grep Persian books for erfan"
}
```


### [2026-09-04T23:10:22.273Z] TOOL RESULT

```
=== BQT v3 erfan
9431:صاحب نظر. کنابه از حاجیان وقیبان- ومعرفان
=== MON erfan
MON_part1.txt:193:فلسفی و عرفانی فارسی و عربی همکاری داشت در نتیجه این همکاری یکت 
MON_part1.txt:3925:آقای محمد عرفانی؛ ولی طق قاعده ندون 
MON_part1.txt:4116:علم» مععرفت» عرفان. (.) اداره‌ای در 
MON_part1.txt:4166:اطلاع» آگاهی. علم؛ معرفت» عرفان. 
MON_part1.txt:94100:ایمان و فتح ابواب عرفان و رفع حجب از 
=== MON tarefeh
MON_part1.txt:41561:تعرفه: (۱۲۵۲۸)۵ [ع. تسعر فه ] (مسصع.)
```


## [2026-09-04T23:10:27.546Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '41558,41566p' MON_part1.txt; echo \"=== headword عرفان\"; grep -n \"^عرفان\\|عرفان:\" MON_part1.txt MON_part2.txt | head; echo \"=== عارف\"; grep -n \"^عارف\" MON_part1.txt MON_part2.txt | head -3",
 "description": "Mo'in tarefeh entry context"
}
```


### [2026-09-04T23:10:27.641Z] TOOL RESULT

```
نعرف. اعدا [ع.] (مص‌ل.) اشنا شدن» 
شناخته گردیدن. شناختن» بژوهیدن. 
(امص.) روشناسی» شناختگی؛ ج. تعرفات. 
تعرفه: (۱۲۵۲۸)۵ [ع. تسعر فه ] (مسصع.) 
معرفی کردنء شناساندن. (امص.) شناسایی. 
(۱.) ورقه شناسابی. فهررست قیمت کالاها. 
سياهةٌ مالیات و عوارضی که به استعه تعلق 
ک 

=== headword عرفان
MON_part1.txt:95639:عرفان: 5 [ع.] (مص‌م.) شناختن» باز 
MON_part1.txt:95671:عرفان. (به مفهوم اخص) - تصوف (همائی» 
=== عارف
MON_part2.txt:9624:عارف. ضح.. فرق فیلسوف (حکیم) با عالم 
MON_part2.txt:11188:عارف از وارد غیبی غلبه یابد (تعریفات» 
MON_part2.txt:32089:عارفان؛ مراقد.
```


## [2026-09-04T23:10:29.771Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '95636,95648p' MON_part1.txt",
 "description": "Mo'in erfan entry"
}
```


### [2026-09-04T23:10:29.836Z] TOOL RESULT

```
عریف. ضح. در فارسی معمولا (غ. عرفه] 
(اخ.) روز نهم ذی‌الحجه. 

عرفان: 5 [ع.] (مص‌م.) شناختن» باز 
حق. (به مفهوم عام) وقوف به دقایق و رموز 
چیزی است مقابل علم سطحی و قشری» 
مثلاً گویند فلان طبیب عارفی است یعنی به 
سطح خوانده‌ها و نوشته‌ها قناعت نکرده با 
فلان عارف سخن و سخندان عارفی است 
یعنی فقط به تقلید سطحی قانع نشده و دقایق 
سخن و سخندانی را فرا گرفته است (همائی» 
جلوه‌های عرفان ایران. مجلهٌ رادیو شمارة 
۴ ۱ - ۱۷). (به مفهوم خاص) یافتن
```


## [2026-09-04T23:10:37.122Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TTS tarif\"; grep -n -i \"tarif\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -5; echo \"=== DEV tarif\"; grep -n -i \"tarif\" DEV.txt | head -8; echo \"=== PHN tarif\"; grep -n -i \"tarif\" PHN.txt | head -8; echo \"=== LAM\"; grep -n -i \"tarif\" LAM.txt | head -5; echo \"=== DOZ\"; grep -n -i \"tarief\\|tarif\" DOZ.txt | head -5",
 "description": "grep Turkic/French books for tarif"
}
```


### [2026-09-04T23:10:37.224Z] TOOL RESULT

```
=== TTS tarif
=== DEV tarif
405:■'  Mémoire  sur  la  propag.  des  chiffres  indiens ,  dans  le  Journ.  cisial.  1"'  seni. i863,  notamment  p.  519.  Ce  travail  est  postérieur  à  la  remarque  de M.  Defrémery,  Mais  M.  Woepcke  avait  dt*jà  publié  divers  opuscules  sur Tarif limétiquo  indienne,  dans  le  recueil  du  prince  Boncompagni.
1187:CuKcuMA.  Esp.  poiiug.  et  ital.  curcuma.  On  trouve  cul- cuma  clans  un  tarif  français  du  wif  siècle.  (Littré.)  C'est l'arabe  /»^j^.  i^ji  hourhoum ,  kourkomna  (liëb.  DS")?),  même signification.  L'Avicenne  de  Rome  donne  la  leçon  ix^iJi qourqouml' (^\i .  t^Fi),  que  les  dictionnaires  n'ont  pas  relevée.
1319:Fardeau.  Esp.  fardo ,  fardillo  (^haWoi),  fardel  (havre-sac, besace);  portug.  y?/n/o,  fardeJ  (même  sens);  iid\.  fardcUo (\)af[nQ[yfardaggio  (bagage).  On  voit  que  le  vrai  sens  est ballot,  paquet,  et  c'est  aussi  celui  de  notre  vieux  mot fardel,  sens  qui  du  reste  a  persisté  jusqu'au  dernier  siècle, comme  le  montre,  par  exemple,  un  tarif  de  1707  in- diquant les  droits  de  péage  pour  Bléré,  sur  le  Cher: r^Vour  fardeau  cordé  de  draps  de  laine,  pesant  Goo  livres, 12  deniers;  j)our  fardeau  cordé  de  feutres,  pesant  600 livres,  20  sols;  ^our  fardeau  cordé  de  tapis,  etc.  ^  51
1579:JuBis,  Terme  de  commerce.  Raisins  secs  en  caisse.  C'est une  altération  de  l'arabe  L^-y^'^  zebib,  raisin  sec,  comme  le prouvent  les  vieilles  formes  azebit,  auzibet  :  «  Pro  cargua de  azebits  seu  racemis,  ?5  dit  un  vieux  tarif  de  Carcassonne, cité  dans  Du  Gange.  Ces  dernières,  ainsi  que  l'espagnol nzebibe,  acebibr,  ont  gardé  l'article  al^  dont  le  l  s'assimile au  z  suivant  :  az~zebïb.  En  portugais,  acipipe  a  pris  une  si- gnification plus  générale,  celle  de  menues  friandises  propres à  aiguiser  rappétit,  à  rafraîchir.  Diverses  contrées  musul- manes, ne  buvant  pas  de  vin,  livraient  leurs  raisins  séchés au  commerce,  et  cet  aliment  était  fort  estimé  des  Arabes; Razi  le  regarde  comme  plus  nutritif  que  la  datte  :  «-.vH>y^ A^-o  t «xil^  ^^yï]  -«Oi  J^Xi  IX  ^ô^j^_  ^  ff  Le  raisin  sec  n'obstrue point  comme  fait  la  datte,  bien  que  plus  nourrissant qu'elle.:)?  (M an.  arabe  déjà  cité,  fol.  63  verso.)
2202:Tarif.    Esp.  et  portug.   twifa ,  ital.  InriJ/a.   Lr  mot  csl '   Voy.  Engelmaii,  Gloss.  p.  lu.
2204:Iraduit  dans  Boctlior  par  v^ycj  tarif,  qui  est  le  nom  d'ac- tion du  verbe  ôjc  'arraf,  faire  connaître,  publier.  C'est là  l'otymologie.  indiquée  dc'jà  par  le  P.  Ange  de  Saint- Joseph  (  i  6  84  ) '.
4409:Targone,ùa/.  voy.  Estragon. Targum,  voy.  Drogman. Tari,  vov.  Téréniabin. Tarif.
4410:Tarifa,  hisp.  vOy.  Tarif. Tariffa,  ital.  voy.  Tarif. Tap<;)^o5,  voy.  Boutargue. 'ïé.pi-/ov  ^  voy.  Boutargue. TapHoiatov ,  voy.  Carquois. Tarquais,  voy.  Carquois. Tartar,  voy.  Tartre. Tartaro,  hisp.  ital.  voy.  Tarhv. Tartarum,  b.  lat.  voy.  Tartre. Tartre. Tasse.
=== PHN tarif
1120:de Gibraltar, entre Ceuta et Tanger, vis-à-vis de Tarif, h
9607:TARIF, s. m. (a.)
9611:des ouvriers, etc. — De torj/* vient le verbe français tarifer,
9612:appliquer le prix du tarif; mais il faut observer que le c:» ^ du
9616:— Les Espagnols et les Portugais écrivent tarifa, les Italiens
9617:tarifa, et les Anglais tariff.
10907:Tarif, s. m. (a.). — Tarifer, v. a 35a
=== LAM
221:ment et au milieu^ elle est transcrite par t : tarif, térénia-
3528:ma dans un tarif français du XVIP® siècle; de J^f
7090:Tarif. Esp. et Ptg : tarif Esp : latarif Transcription de
7092:En turc A^y^ ta'rîfa a de même le sens de tarif, taxe.
9751:Tarif
=== DOZ
2806:TARIEF.
2807:Ital. tariffay Fr. tarify is het Arab. taWi f of ta' rif a.
2813:maar Bocthor en Marcel vertalen tarif met taWif,
2817:tarif üy maar het schgnt in die talen betrekkelijk jong
```


## [2026-09-04T23:10:45.368Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9605,9620p' PHN.txt; echo \"=== LAM\"; sed -n '7088,7096p' LAM.txt; echo \"=== DOZ\"; sed -n '2805,2820p' DOZ.txt",
 "description": "read Pihan, Lammens, Dozy tarif entries"
}
```


### [2026-09-04T23:10:45.419Z] TOOL RESULT

```
trouve aussi, en espagnol et en portugais, adaraga et adarga,
mots qui contiennent évidemment Farticle al, changé en a.
TARIF, s. m. (a.)
OUg ; .x» [to^rj/*] , nom d'action de ô^ [^arraf]faire connaître,
2" forme de c^ [*^^^] connaître. Tableau indicateur du prix
des marchandises, des monnaies, des impositions, du salaire
des ouvriers, etc. — De torj/* vient le verbe français tarifer,
appliquer le prix du tarif; mais il faut observer que le c:» ^ du
correspondant arabe n'est pas radical, ce n'est qu'une lettre
nécessaire à la formation de l'infinitif ou nom d'action de la
a' forme des verbes arabes, en vertu d'une règle grammaticale.
— Les Espagnols et les Portugais écrivent tarifa, les Italiens
tarifa, et les Anglais tariff.
TARTANE, s. f. (a.)
i^Xi^ [t'arîdat]. Ce mot, en arabe d'Egypte, signifie imsseau
affecté spécialement au transport des c/iei*atur.* Introduit dans plu-
=== LAM
se couvrir le corps de ses bras, en mettant les poignets
sur les flancs.
Tarif. Esp. et Ptg : tarif Esp : latarif Transcription de
wi j«î ta'rîf^ nom d'action de ^f- faire connaître, publier.
En turc A^y^ ta'rîfa a de même le sens de tarif, taxe.
Le dialecte vulgaire de Syrie emploie aussi de préférence
ïi j«o ta^rifa.
- ■ »■ ■ T ..11. I ■ ■ I ■ PII ■ I M — I ■ ■ Il ■ ■ «ai»
(1) Qui dans l^ancieime langue désignait un boucliei\ Targette est-il le
=== DOZ
Zie Taggerijn.
TARIEF.
Ital. tariffay Fr. tarify is het Arab. taWi f of ta' rif a.
De wortel 'arafa (t-Jy:) beduidt kennen; in den twee-
den vorm; 'arrafa, doen kennen ^ bekendmaken; hier-
van de infinitivus ta'rif en ta'rifa, het bekend maken ^
bekendmaking. Bg Freytag staat deze infinitivus niet
in den specieelen zin, dien wg aan ^an>/* hechten ;95
maar Bocthor en Marcel vertalen tarif met taWif,
Berggren met ta'nfa.
Uit het Iberische schiereiland schgnt het woord niet
tot ons gekomen, want het Sp. en Port. hebben wel
tarif üy maar het schgnt in die talen betrekkelijk jong
te zijn; wel geeft Ducange voorbeelden uit een concilie
van Sevilië van 1512, maar 't schgnt toch in Spanje
weinig in gebruik te zgn geweest; althans in oude Sp.
```


## [2026-09-04T23:10:57.430Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN\"; grep -n -i \"vārūn\\|varun\\|frārūn\\|frarun\\|wārūn\" HRN.txt | head -10; echo \"=== HUB\"; grep -n -i \"varun\\|frarun\\|vārūn\" HUB.txt | head -10; echo \"=== CHEUNG ard\"; grep -n -i \"abārōn\\|frārōn\\|\\*ard\" CHEUNG.txt | head -10",
 "description": "grep Horn/Hübschmann/Cheung"
}
```


### [2026-09-04T23:10:57.501Z] TOOL RESULT

```
=== HRN
11257:214. varun ^Begierde* (AV., Men.).
=== HUB
688:Im Altarmenischen klingt varung *Gurke, Citrone,
=== CHEUNG ard
```


## [2026-09-04T23:10:59.552Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index ARDHA/ARD\"; grep -n -i -E \"^\\s*(ARDHA|ARD|ARDA)\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"=== ARY persian varun\"; grep -n \"وارون\\|فرارون\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== FSF\"; grep -n \"وارون\" FSF.txt | head -5; echo \"=== FRS\"; grep -n \"فرارون\\|وارون\" FRS.txt | head -5",
 "description": "grep Aryanpur, Noushin, Asadi"
}
```


### [2026-09-04T23:10:59.641Z] TOOL RESULT

```
=== ARY latin index ARDHA/ARD
=== ARY persian varun
=== FSF
5905:وارهُ وارون): 
5906:گمان برد کز بخت وارون برست 
5909:نشد بخت وارون از ان یک بدست 
30798:ازنگون [: وارونه» زبر زیر] +سار [: سر ]: 
31842:وارونه 
=== FRS
14016:وارون 
14017:ندانم بخت را با من چه گین است بکه نالم بکه زین بخت وارون" 
14019:کمان برد کز بخت وارون برست 
14020:نشد بخت وارون از آن یك بدست ۲ ] 
14024:ندارند ۰ ۰ 6 س ؛ وارون بدبخت وشوم باشد » در نسخه اساس چاره » و این
```


## [2026-09-04T23:11:05.313Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 214\"; sed -n '11253,11262p' HRN.txt; echo \"=== FSF\"; sed -n '5903,5912p' FSF.txt; echo \"=== FRS\"; sed -n '14014,14026p' FRS.txt",
 "description": "contexts"
}
```


### [2026-09-04T23:11:05.390Z] TOOL RESULT

```
=== HRN 214
(oben No. 178^**) und ijueviden (oben No. 912) erhalten.
Salemann vermutet sie auch in dem unklaren
berberüsäfiy SF pag. 100" (vergl. oben 'Nachträge
No. 122»»^*).
214. varun ^Begierde* (AV., Men.).
aw. varena- *Bekenntniss*, mit Bedeutungswechsel?
np. r£?r^wj^ ^begierig*, worauf West verweist, ist sehr
unsicher, auch in dem bei Vullers angeführten Verse
aus Hekim Sözenl (FR will hier vielmehr ii re/c im
Sinne von mekrüh, zist lesen).
=== FSF
نیزه به پیل اندر شد و برسید تا به دل. از 
ابوشکور (نقل از لغت فرس» شاهد برای 
وارهُ وارون): 
گمان برد کز بخت وارون برست 


نشد بخت وارون از ان یک بدست 


بدسگال (به کسر سین) 
=== FRS
پارمان و اروند مرد هنر فراز آوردگنج‌زر و کهر ] 
6 
وارون 
ندانم بخت را با من چه گین است بکه نالم بکه زین بخت وارون" 
ابوشکو رگوید : 
کمان برد کز بخت وارون برست 
نشد بخت وارون از آن یك بدست ۲ ] 
ِ- این ببت فقط درل و چ هست و اس بیت مد را بجای آن آورده . 
۲ س این افت را ندارد ۳- ک : اره‌ان و اروند اتباعست ارمان رنجکی [ کذا] 
بود و اروند تجربت ( رجوع شود بلفت اروند در ص ۰ ۰ 0۱ » سایرنسخ اين لت را 
ندارند ۰ ۰ 6 س ؛ وارون بدبخت وشوم باشد » در نسخه اساس چاره » و این
```


## [2026-09-04T23:11:13.046Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/tarife",
 "prompt": "Give the etymology of Turkish \"tarife\": Arabic source form, first attestation date in Turkish, and whether it passed on to European languages."
}
```


## [2026-09-04T23:11:14.216Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/tarifa",
 "prompt": "Give the Spanish entry \"tarifa\": etymology (Arabic source, any Italian or Turkish intermediary), and meaning."
}
```


### [2026-09-04T23:11:19.482Z] TOOL RESULT

```
I cannot provide the etymology information you've requested based on the web page content provided. The page appears to be only a header/footer section from Nişanyan Sözlük (Nişanyan Dictionary), containing navigation elements and copyright information, but does not include the actual dictionary entry for "tarife" with its etymological details.

To obtain the etymology of Turkish "tarife," including its Arabic source, first attestation in Turkish, and information about transmission to European languages, you would need to access the full dictionary entry on the Nişanyan Sözlük website.
```


### [2026-09-04T23:11:25.083Z] TOOL RESULT

```
# Spanish Entry: Tarifa

**Etymology:**
The Spanish word traces back through "Andalusian Arabic" to Classical Arabic "تَعْرِفَة" (taʕrifa). The entry shows it was "inherited from Old Spanish," with no Italian or Turkish intermediary mentioned.

**Meaning:**
According to the Wiktionary entry, *tarifa* has two primary definitions:

1. "Money paid for a transport ticket" (fare)
2. "Fee" (with *honorario* listed as a synonym)

**Important Note:**
The entry includes a usage note clarifying that *tarifa* is a "false friend" and does not mean "tariff" in English. The Spanish word for tariff is *arancel*.
```


## [2026-09-04T23:11:31.510Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%B9%D8%B1%D9%8A%D9%81",
 "prompt": "Give the Arabic entry تعريف: root, verbal-noun formation (form II عرَّف), meanings, and the Persian/Ottoman Turkish descendants or borrowings listed."
}
```


## [2026-09-04T23:11:33.046Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D8%B1%D9%81%D8%A7%D9%86",
 "prompt": "Give the entries for عرفان: the Arabic word (root, meaning) and the Persian word (etymology - borrowed from Arabic? meaning 'gnosis, mysticism')."
}
```


### [2026-09-04T23:11:37.449Z] TOOL RESULT

```
# Arabic Entry: تعريف (Ta'rīf)

**Root:** ع ر ف (ʕ r f)

**Verbal Noun Formation:** Form II of عَرَّفَ (ʕarrafa)

**Primary Meanings:**
1. Definition
2. Announcement
3. Instruction
4. Introduction
5. Description
6. Tariff
7. Assertion
8. Guessing

**Persian and Ottoman Turkish Descendants:**

- **Classical Persian:** تَعْرِیف (ta'rīf)
- **Ottoman Turkish:** تعریف, which evolved into modern Turkish tarif

The Persian form subsequently spawned numerous South Asian descendants including Hindi तारीफ़ (tārīf), Urdu تَعْرِیف (ta'rīf), and Bengali তারিফ (tariph).
```


### [2026-09-04T23:11:39.966Z] TOOL RESULT

```
# عرفان (Irfan/Erfan)

## Arabic Entry

**Root:** ع ر ف (ʕ r f)

**Word:** عِرْفَان (ʕirfān) - masculine noun

**Meanings:**
- Verbal noun of عَرَفَ (to know)
- "knowledge, knowing, cognition" particularly within Sufism
- Gnosis - attaining direct spiritual knowledge
- Mysticism, especially Islamic mysticism

**Pronunciation:** /ʕir.faːn/

## Persian Entry

**Etymology:** The term was "Borrowed from Arabic عِرْفَان (ʕirfān)"

**Word:** عرفان (irfān / erfân)

**Meanings:**
- Knowledge and cognition, especially in Sufism
- Gnosis - direct spiritual knowledge attainment
- Mysticism, particularly Islamic mysticism

**Additional Use:** Functions as a masculine given name in Persian

Both entries share identical semantic fields centered on spiritual knowledge and Islamic mystical tradition.
```


## [2026-09-04T23:11:48.823Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ardastāna\\|ardastana\\|^arda-\\|arda-stāna\" KNT.txt | head -10; echo \"=== TLM\"; grep -n -i \"ardastana\\|arda-\" TLM.txt | head -5",
 "description": "grep Kent/Tolman for OP arda-"
}
```


### [2026-09-04T23:11:48.892Z] TOOL RESULT

```
586:ardastana- ‘window-frame’, Elam. har-da-i5-da- па.
1899:arda-stána- ‘place of light’; datva-dána- ‘holder of demons’.
5069:ardastāna- sb. ‘window-frame, window cor- nice’: arda- ‘light’ as in OP ardata- ‘silver’, Skt. rajatd- ‘white’, rjrá- ‘red’, Gk. àpyós ‘shining’ + stāna- ‘place’ (831, §160.Ib; Foy, KZ 35.48; hardly as with Bthl. AiW 193, or Hz. Ар! 74-6); ‘light- place’. ardasténa nsm. DPc.
=== TLM
347:16.  0atiy2  Darayavaus  xsaya0[i]ya  Parflava  uta  Var-93)kana [ham]i[0r]iya  [abajva"  [bacajma  Fravar[tais  aga]u[ban]ta  V's- taspa  mana  pita  ha-94)uv  [Parflavaiy]  aba  a[va]m  kilra  avaba[rja3 ham]i0ri[ya]  abava  pasava  V’staspa  95)[asiyava  bada  kar]a  h[ya- saiy]  anusifya]  aha  Vis[pa]uz[a]tis  nama  varda-96)[nam  Par0a- vaiy]  avada  bamaranam  [a]kunau[s]  bada  Par0avaibi[s]  A[ura- mazdjamaiy  97)[upastam  abara]  vasna  [A]  urama  [zdaha  Y's]ta- [spa]  avam  kara[m  tyam  ha]m[i]0riya-9S)in  [ajan  vasiy  VJiyaxna- hya  m[a]hya  [XXII  raucabis]  Sakata  aba"  avaSasam  bamaranam kartam
663:Ardastana  a0angaina  Darayavahaus  XSbya  vi0iya  karta
1084:a6a”gaina  or  a0a"gaina,  adj.  of  stone.  Nom.  sg.  m.  a$angaina, Dar.  Pei'S.  C.  ardastana  a$a"gaina.  Acc.  Sg.  f .   a6a"gainam,  Al’t.  Sus. c;  a0a"ganam  for  a$angainam,  Art.  Pers.  a,  b,  3.  YAv.  asanga  (New Pers.  sang,  Horn,  NS,  38,  2).  Cf.  KZ.  39,  69.
1154:ardastana,  m.  window-cornice  (?).  Nom.  sg.  ardastana,  Dar. Pers.  C.  ardastana  a#angaina  darayavahaus  XShya  vi0iya  karta.  *arda, half. \   YAv.  arada  -f-  stana,  YAv.  -stana  (New  Pel’s,  stan),  Skt.  sthana; cf.  Bartholomae,  Altiran.  Wb.,  193.  Foy,  KZ,  35,  48.  connects the  first  member  of  the  compound  with  Av.  arazo,  bright ,   Skt. rira.
```


## [2026-09-04T23:11:56.734Z] TOOL CALL #57: WebSearch

```json
{
 "query": "Middle Persian frārōn abārōn etymology *fra-rāwan rōn \"direction\" Nyberg"
}
```


## [2026-09-04T23:11:58.459Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D8%B1%D9%88%D9%86",
 "prompt": "Is there a Persian entry فرارون? If so give its etymology (Middle Persian frārōn) and meaning. If the page does not exist say so."
}
```


### [2026-09-04T23:11:58.583Z] TOOL RESULT

```
Web search results for query: "Middle Persian frārōn abārōn etymology *fra-rāwan rōn "direction" Nyberg"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T23:12:02.404Z] TOOL RESULT

```
Yes, there is a Persian entry for فرارون. According to the Wiktionary page, it is "an adjective with the transliteration farârun." The page lists four obsolete meanings: "forward," "progressive," "auspicious," and "honest."

However, the page does not provide an etymology section mentioning Middle Persian frārōn or any other etymological information.
```


## [2026-09-04T23:12:11.595Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%88%D8%A7%D8%B1%D9%88%D9%86/",
 "prompt": "Show the فرهنگ معین (Mo'in) and لغت‌نامه دهخدا sections for وارون: the origin tag (e.g. [په.] Pahlavi) and the definitions given."
}
```


## [2026-09-04T23:12:13.030Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%81%D8%B1%D8%A7%D8%B1%D9%88%D9%86/",
 "prompt": "Show the فرهنگ معین (Mo'in) and لغت‌نامه دهخدا sections for فرارون: origin tag (e.g. [په.] Pahlavi) and definitions, plus any variant forms فریرون/فیرون."
}
```


### [2026-09-04T23:12:21.184Z] TOOL RESULT

```
# وارون: Lexicographic Entries

## لغت‌نامه دهخدا (Dehkhoda Dictionary)

**Origin tag:** Not explicitly marked with a language origin tag in this section.

**Definitions:** The entry presents وارون as an adjective (ص) with multiple meanings: "reversed, inverted, unlucky, inauspicious." It lists numerous synonyms including "باژگونه" (reversed), "معکوس" (inverted), and "نگون" (ill-fated). The dictionary includes extensive poetic citations illustrating both literal meanings (reversal) and figurative uses (misfortune).

## فرهنگ معین (Mo'in Dictionary)

**Origin tag:** "[په.]" indicating Pahlavi origin

**Definitions:** This entry is notably concise, defining the word as "سرنگون، واژگون" (overturned, inverted), emphasizing the physical reversal sense without the figurative meanings present in Dehkhoda's treatment.

The Dehkhoda entry is substantially richer, incorporating both concrete and metaphorical applications supported by classical Persian poetry, while Mo'in's treatment remains more streamlined and literal.
```


### [2026-09-04T23:12:22.476Z] TOOL RESULT

```
# فرارون

## لغت‌نامه دهخدا

**Origin**: Pahlavi *farārun* (meaning "exalted, direct, straight")

**Definitions**: Something that progresses forward rather than regressing; "پاکدامن و نیکوکردار و پرهیزگار" (virtuous and righteous). Contrasts with "اوارون" (sinful). The term appears in astronomical contexts describing stellar motion, specifically "حرکت سعد" (fortunate motion).

## فرهنگ معین

**(ف) (adj.)**

1. "مترقی، پیش رو" — advancing, progressing forward
2. "خوب، عالی" — good, excellent
3. "راست، مستقیم" — straight, direct
4. In astronomical terminology: "سَعْد، اوج" — fortunate/auspicious, apex

## Variant Forms

The page references **فریرون/فیرون** as contrasting terms in astronomical usage, representing opposing stellar motions, with user suggestions proposing directional associations (north/south).
```


## [2026-09-04T23:12:41.885Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/tariff|page 63, root A'.r.f, English tariff node: Arabic ta'rif > MedLat tarifa > Italian tariffa > English, no Turkish/Spanish\" \\\n \"https://en.wiktionary.org/wiki/tariff|page 63, English tariff node: Italian tariffa < Arabic تعريف, first attested 1592\" \\\n \"https://www.ahdictionary.com/word/search.html?q=tariff|page 63, root A'.r.f and English node: AHD etymology Italian tariffa < Old Italian < Arabic ta'rif, Semitic root 'rp\" \\\n \"https://en.wiktionary.org/wiki/%D9%88%D8%A7%D8%B1%D9%88%D9%86|page 63, root Ardha, node varun: Persian وارون < MP abārōn (MacKenzie)\" \\\n \"https://en.wiktionary.org/wiki/tarifa|page 63, Spanish node: Spanish tarifa < Andalusian Arabic < تعرفة; false friend, not 'tariff' (=arancel)\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D8%B9%D8%B1%D9%8A%D9%81|page 63, root A'.r.f: Arabic تعريف root ع ر ف, form II verbal noun, Ottoman Turkish descendant\" \\\n \"https://en.wiktionary.org/wiki/%D8%B9%D8%B1%D9%81%D8%A7%D9%86|page 63, Persian node erfan: Persian عرفان borrowed from Arabic عِرْفَان\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D8%B1%D9%88%D9%86|page 63, node frarun: Persian فرارون adjective, obsolete senses forward/honest\" \\\n \"https://abadis.ir/fatofa/%D9%88%D8%A7%D8%B1%D9%88%D9%86/|page 63, node varun: Mo'in tags وارون [په.] Pahlavi; Dehkhoda senses\" \\\n \"https://abadis.ir/fatofa/%D9%81%D8%B1%D8%A7%D8%B1%D9%88%D9%86/|page 63, node frarun: Dehkhoda 'from Pahlavi farārun', opposite اوارون; Mo'in senses\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive all cited web sources"
}
```


### [2026-09-04T23:13:13.874Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0ccbd8fbf5d4b77c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9068c98a57e8d8bb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/145c62b5dc9caa63.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/83a48a758af942d9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/76928d2c50d0fd1b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/657799db3ef6c211.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/945e9d4a76f5be1d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/09246d97df40e503.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4cef3878e1cec783.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3e7b96874c8370f7.txt
```


## [2026-09-04T23:13:26.994Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && ls && python3 -c \"\nfrom PIL import Image\nfor p in ['1445.png','2246.png']:\n    im=Image.open(p); print(p, im.size)\n\"",
 "description": "check BQT page images"
}
```


### [2026-09-04T23:13:28.746Z] TOOL RESULT

```
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1455.png
1455.txt
1488.png
1488.txt
1803.png
1803.txt
1878.png
1878.txt
1900.png
1900.txt
1908.png
1908.txt
2143.png
2143.txt
2222.png
2222.txt
2246.png
2246.txt
2407.png
2407.txt
31.vision.txt
58.vision.txt
70.vision.txt
72.vision.txt
1445.png (1650, 2546)
2246.png (1650, 2546)
```


## [2026-09-04T23:13:35.261Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && python3 -c \"\nfrom PIL import Image\nim=Image.open('1445.png')\nw,h=im.size\nim.crop((0,int(h*0.50),w,int(h*0.78))).resize((int(w*1.3),int(h*0.28*1.3))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1445_fn.png')\nim2=Image.open('2246.png')\nim2.crop((0,int(h*0.72),w,h)).resize((int(w*1.3),int(h*0.28*1.3))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2246_fn.png')\nprint('ok')\n\"",
 "description": "Crop footnote regions"
}
```


### [2026-09-04T23:13:38.474Z] TOOL RESULT

```
ok
```


## [2026-09-04T23:13:41.898Z] TOOL CALL #64: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1445_fn.png"
}
```


### [2026-09-04T23:13:42.289Z] TOOL RESULT

```

```


## [2026-09-04T23:13:42.287Z] INPUT

[Image: original 2145x926, displayed at 2000x863. Multiply coordinates by 1.07 to map to original image.]


## [2026-09-04T23:14:05.915Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2246_fn.png"
}
```


### [2026-09-04T23:14:06.194Z] TOOL RESULT

```

```


## [2026-09-04T23:14:06.192Z] INPUT

[Image: original 2145x926, displayed at 2000x863. Multiply coordinates by 1.07 to map to original image.]


## [2026-09-04T23:14:40.711Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > 1445.vision.txt <<'EOF'\n[Read from the page image by Claude (vision), BQT p.1445 = BQT_v3_picofile.pdf page 238.\nEntries on this page: فراخ رفتن … فراخنا … فرارون … فراخ روی … فراخی. Mo'in's numbered\netymological footnotes at the foot of the page. Footnote 8 is the one on فرارون.]\n\nHeadword (body of the page):\n  فرارون - با رای بی نقطه بر وزن ...\n\nFootnote 8 (verbatim):\n۸ - پهلوی frarôn ( عالی ، مستقیم ، راست ) و frarônîh ( تقوی ، استقامت ) « مناس ۲۷۳ :۲ »\nدر لغت فرس ص ۳۷۸ آمده : « فرارون ، کواکب بیابانی است ، آنگه که رفتنشان باز پیش بود » .\nدقیقی (طوسی) گوید :\n    حسودت در ید ( بد . دهخدا ) بهرام فیرون      نظر زی تو ز برجیس فرارون .\nفرارون بمعنی پاکدامن و نیکوکردار و پرهیزگار در مقابل لغت « اوارون » بمعنی گناهکار و شریر\nآمده ، هیچ ربطی با کواکب بیابانی ندارد . ( صادق هدایت . مجلهٔ موسیقی سال ۲ شمارهٔ ۸ )\nو رک: یشتها ۲ ص ۱۷۹ متن و حاشیه . نیبرگ ص ۷۲ - ۷۳ گوید : پهلوی frârôn ( راست ،\nدرست ، درستکار ) ، پازند frârûn ، از ایرانی باستان ⁎frârdhavan - ⁎frârdha -\n⁎fra - ardha ( بجلو جاروب کرده ) ، قس apârak و apârôn . رک: فریرون .\n\n[Note: the Latin-letter forms are printed exactly as frarôn / frarônîh / frârôn / frârûn /\n*frârdhavan / *frârdha / *fra-ardha / apârak / apârôn. The gloss «بجلو جاروب کرده»\n= \"swept forward\" is the source of Nourai's root gloss \"swept, moved, pushed\".]\nEOF\ncat > 2246.vision.txt <<'EOF'\n[Read from the page image by Claude (vision), BQT p.2246 = BQT_v4_picofile.pdf page 329.\nEntries on this page: وارث داود … وارخد … واردنا … وارغ … وارن … وارنج … وارون.\nMo'in's numbered etymological footnotes at the foot of the page; footnote 12 is on وارون.]\n\nFootnote 12 (verbatim):\n۱۲ - وارونه ( ه.م. ) ، پهلوی apârûn ، apârûnîh مرکب از : apa ( پیشوند ) و پهلوی rûn\n( طرف ، جهت ) اصلاً بمعنی کنار ، قس : پهلوی frârûn « اسشق ۱۰۷٤ » .\n\n[i.e. Mo'in analyses MP apārōn as apa- (prefix) + MP rōn \"side, direction\", originally\n\"edge/side\", comparing MP frārōn — NOT as *apa-arda- with *arda- \"side\". The bracketed\nsource siglum is printed « اسشق ۱۰۷٤ ».]\nEOF\nls -la 1445.vision.txt 2246.vision.txt",
 "description": "Save vision transcriptions of BQT pages"
}
```


### [2026-09-04T23:14:58.531Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 1790 Sep  4 19:14 1445.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  805 Sep  4 19:14 2246.vision.txt
```


## [2026-09-04T23:15:17.774Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"وارون\\b\" MON_part2.txt | head -20; echo \"=== pages?\"; grep -c $'\\f' MON_part1.txt MON_part2.txt; echo \"=== letters at end of part2\"; tail -20 MON_part2.txt",
 "description": "check MON coverage"
}
```


### [2026-09-04T23:15:19.634Z] TOOL RESULT

```
14065:وارونه کردن حروف یک کلمه. . صسح.- 
20878:آن را وارونه در ظرفی برمی‌گردانند و به 
33634:می‌شوند و در انتهای ساقه بطور وارونه قرار 
61061:سرنگون, واژگونه. وارونه. تسرتیب 
63370:مقلوب: ۱0۵ [ع.] (امف.) وارونه کرده 
69184:عنوان کسی يا بنگاهی را وارون کنده باشند 
77089:(اژکونه ماشگونه؛ وارون وارونه. 
77094:جا رفته نغل وارونه به اسب خود می‌زد نا 
83342:وارون: «ت22*[- وارونه] (ص.) باژگونه, 
83347:شوم. بخت وارون: بخت بد» طالع شوم. 
83348:واروف: (6-):۷2۳50 [- وارون] (ص.) 
83450:سرنگون» وارون. آنکه رفتارش نادرست و 
=== pages?
MON_part1.txt:0
MON_part2.txt:0
=== letters at end of part2


یو نجه‌رار 
یونجه‌زار: :22 (امر.) (گیء) زمینی که 
زیر کشت یونجه است. 

بهود. ۷۸۳3۵(ع.] (.) کسی که در بهودیه 
متو لد شده باشد. کسی که از اعقاب سا کنان 
1 ناحیت بود. 

یهودی: 01 منسوب به بهو د. متدین به 
دین بهود. (عم.) گاهی به آدم جبان و ترسو 
و مردنی و کم دل و جرأت گفته می‌شود 
(فرعا.جما.) 

یبلاق: ۱۰۰(۷ [تر.] جای‌باش تاستان» 
منطقهٌ خوش آب و هوا که هنگام تابستان 
بدانجا روند» مصطاف.
```


## [2026-09-04T23:15:23.428Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '83340,83352p' MON_part2.txt; echo \"=== فرارون in part2\"; grep -n \"فرارون\\|فرارو\" MON_part2.txt | head -5",
 "description": "Mo'in varun headword"
}
```


### [2026-09-04T23:15:23.507Z] TOOL RESULT

```
زگیل. 
وارون: «ت22*[- وارونه] (ص.) باژگونه, 
واژگون» سرنگون» نگونسار» معکوس. 


بررعکس؛ مخالف. (مج.) ناسا رک نحس» 
شوم. بخت وارون: بخت بد» طالع شوم. 
واروف: (6-):۷2۳50 [- وارون] (ص.) 
بازگونه» وازگون» سرنگون. برعکس» 
مخالف. (مج.) نامبا رکك» نحس» شوم. 
واره: (۷2)۵ [- وار - بار] () نسویت» 
مرتبه. در اراک (سلطان آباد) و برخی از قراء 
=== فرارون in part2
5628:فراروی: ۲-7۷ (ق‌مر.) پیش روی: برابر
```


## [2026-09-04T23:15:41.425Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK ardha\"; grep -n \"ardha-\\|árdha\" POK_full.txt | head -10; echo \"=== WLD\"; grep -n \"ardha-\" WLD_band3.txt incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt 2>/dev/null | head -5; echo \"=== IEC\"; grep -n \"ardha\" IEC.txt | head -5; echo \"=== PLA erfan\"; grep -n \"عرفان\\|تعرفه\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -3",
 "description": "grep IE dictionaries for ardha"
}
```


### [2026-09-04T23:15:41.529Z] TOOL RESULT

```
=== POK ardha
28507:Old Indie /o'/7a/r" especially, peculiar, particular', ardha-h^ part, side, half, ardha-^\\a\f, 
32571:grdhn'u-h^ greedy ', grdhra-h^ greedy; vulture', gardha-h{= Old Church Slavic gladt) m. 
50255:Material: Old Indie sardha-m., sardhas-u. "herd, troop, multitude, crowd', Avestan sarada- 
91103:Material: Old Indie vardhati, vardhate, vrdhat/ 'wachst, mehrt sich', vardha- m. 'das 
=== WLD
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:26717:Ai. rardha- m , cardhas- n. „Herde, Scbar“, av. saroSa -, apers. pard- 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:26751:rardhati ..tritt keck, trotzig auf, schert sich worum nicht - , cardha- ,,frech, 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:39853:grdJinu-h „gierig‘‘, grdhra-h „gierig, heftig wonach verlangend", gardha-h 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:39868:„Hunger“ von ai. gardha-h in der Vokalstellung ab (s. u. gher- „begehren“). 
=== IEC
1515:bhordha, üs (?) ‘axe’. Cf. bherio, bhor- (2) OHG barta; ON baróa; OCS brady, gs -ive; Blg. bradva, id. (association with type *bhardha, bharsdha “beard? may be acciden- tal, cf. however Gk. génus in sense of (1) ‘chin’, (2) ‘hatchet
4797:gholdhos (1) “lack, desire, hunger; lacking, deprived". WP I, 633. (Sl. ambig.) Skt. gardhah “desire? (but cf. gárdah, adj. '"hungry); MHG galt ‘barren, non-milch'; G also Galt “inflammation of the udder’; ON geldr, adj. as MHG; Sw. gall, adj. id.; OCS gladü, R gólod (hunger. Ambig. Cf. Skt. gárdah “hungry”, to which a further variant is possible in OHG kalt, OE ceald *cold', etc. fr. *goldh- ?). Cf. gel-, geldos
7032:A variant arises in Skt. Sardhah *troop") kerep-, kerop- see kerp-
8677:Kerdhos, à “herd, crowd, drove'. Cf. Ker- ‘head’. WP I, 424 Skt. Sardhah “host, army? beside $ardhas, n. id.; Av. saroóo (2) ‘kind, sort’; Go. haírda, f. ‘herd’, wm. ‘herdsman’; OE heord, f., hierde, wm. as Go.; OHG hërta, f., hirti, m. as Go.; ON hjoró, f. ‘herd’; hirðir, gs hiróis, m. ‘herdsman’, cf. hirð, f. ‘bodyguard’. (Gk. kór- thus, f. ‘pile’, and W cordd, m. pl. -ion ‘circle; tribe’ are no more than potential o-gde iso- phones, despite FK: EWDS 17: Herde. OCS éréda (2) “herd” and Li. kerdZius, m. 'shep- herd? are Germanic LWs because of the initial.
11257:mré- (3) ‘harden, solidify, freeze’ Skt. cf. (ambig.) mūrčhāmi ('solidify', if fr. *mr&sko); Gk. margóno, v. “feel numb’; Alb. mardha, aor. ‘froze, felt cold’; cf. mërdhif, mérdhih, v. (*freeze, feel cold’, fr. *mrgisKo); OCS mrüZzo, mrüzati, & mrüzng, -noti, intr. ‘freeze’ beside mrüZza, f. ice; R mérznut, inf. as OCS; Pol. marznac, as OCS. (Variant in Arm. mardzem ‘coagulate’, fr. *mrgh-)
=== PLA erfan
```


## [2026-09-04T23:15:46.017Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28495,28520p' POK_full.txt",
 "description": "POK context for ardha"
}
```


### [2026-09-04T23:15:46.064Z] TOOL RESULT

```
rudzi^ leaking standing rye '; Lithuanian ertas^w\6e, far, spacious ' ("*standing apart '); 



from the light basis retas'\h'\n, spacious, seldom' (from the themat. root form *(e)r-e-, as 
also:) /lesi/^s 'seldom, thin', paresvis^ sparse '; 

Old Church Slavic 0/7// "dissolve, overthrow, destroy' (Kaus. *ore/d'make break up'), 
Serbo-Croatian Oit'd/'/// "prostrate, throw down', Czech obor/t/" destroy' , russ. razonfbds. 

Maybe alb. rrezonj'bnng down' : russ. razorftb 

Old Indie /o'/7a/r" especially, peculiar, particular', ardha-h^ part, side, half, ardha-^\\a\f, 
n. "part, half; 

Lithuanian ardali, -///"separate, split' (Kaus., as Church Slavic oriti) ; erdvas^\N\6e, 
capacious', Latvian ardaws, ifdens^ lax, friable', e/r/s" lax, commodious (capacious '), 
ifdi't, /?d/nat loosen, separate', erzu, erdu, eAs/ "separate'. 

re-dh_. 

Old Church Slavic redhk-b "seldom' (probably shifted stress, compare Czech ridky, 
sloven, redak, in spite of serb.-kroat. rijedkT, rtdkl); 

about ered-see above S. 329 f., about ereu- under different article under S. 337.
```


## [2026-09-04T23:15:51.914Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28455,28497p' POK_full.txt | head -50",
 "description": "POK root header"
}
```


### [2026-09-04T23:15:51.957Z] TOOL RESULT

```
£/o-extension in Old Hoxsq jgrvi {*erwan^ "sand, sandbank', and cymr. erw\. "field', PI. 
erwi, erwydd, corn, erw, ereu6s., abret. Middle Breton eru, nbret. ero "furrow' {*erui-)\ 

Note: 

Those cognates derived from Old Indie arvan-, arvant-: Messapic FIN /I/'ko prove lllyrian 
displayed satem character; there is proof lllyrian belonged to the Celtic family gall.-brit. FIN 
*Arva, engl. Arrow, French Erve, Auve {*rua)\ Messapic FIN Arvo. [see above] 

perhaps Armenian erkir^ earVc\' (Pedersen KZ. 38, 197), if for*^/^- (Indo Germanic *eru-) 
after erkin "sky, heaven'. 

References: WP. I 142, Finzenhagen Terminol. 6, Schwyzer Gr. Gr. I 424. 
Page(s): 332 

Root / lemma: er-5, era-, thematic (e)r-e- 

Meaning: rare, loose, crumbly 

Material: Old Indie //e with Abl., Akk. " with exclusion of, without, except, besides' (Lok. a 

participle *rta- " separated, secluded '), nirrti-h' resolution, decay, downfall, ruin'; ar-ma- 

Pl. " debris, ruins ', armaka-^ trijmmerhaft ' or n. " TriJmmerstatte ' (meaning somewhat 

doubtful); Va-in /?/77a- "wound'; themat. *{e)r-e- in v/ra/a-' standing apart, leaky, rare '; 

Maybe zero grade in alb. {*era/a-) ra/fe'rare'. 

gr. £pr|po(;, Attic spHMO'^ lonely '; 

quite doubtful Latin Aams "having wide interstices between its parts, of a loose texture, 
not thick or dense, thin, loose, scattered, scanty, far apart; milit. in loose order; in gen. 
rare, infrequent; sometimes extraordinary, distinguished. Adv. raro, rare, seldom, rarely ' 
( *er9-rd-s), rather credible rete'net, thread' (compare under Lithuanian ret/s, Latvian refa); 

maybe alb. {*rete) rrJete'neV 

Lithuanian yru, Irt/" separate, resolve, distinguish', pa/ras' lax, loose '; ret/s m. " phloem 
sieve ' (with unoriginal second accent, as often in /-stems), Latvian reta, rete'scar', rem' 
rudzi^ leaking standing rye '; Lithuanian ertas^w\6e, far, spacious ' ("*standing apart ');
```


## [2026-09-04T23:15:58.655Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ardha\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20",
 "description": "grep WLD Bd1 for ardha"
}
```


### [2026-09-04T23:15:58.704Z] TOOL RESULT

```
9664:durch dh (vgl. doo!) vvm usw. vorliegt) (wie bei ai. vardhate : (f)oddlg). s. 
9671:weisenden Proportion rclhati : vardhate = arsati : variati (z. B. Petersson 
18353:Ai. vardhate „erhebt, macht wachsen", av. varod- „augere"'; ai. iirdhva- 
25750:668 f. — S. noch *kerdho- „Reihe, Herde" (wo auch iiber ai. gardhati ,.ist 
26688:Ai. f ardhate „ist frech, trotzt“ bleibt trotz lick 1*44 fern. 
26717:Ai. rardha- m , cardhas- n. „Herde, Scbar“, av. saroSa -, apers. pard- 
26751:rardhati ..tritt keck, trotzig auf, schert sich worum nicht - , cardha- ,,frech, 
39853:grdJinu-h „gierig‘‘, grdhra-h „gierig, heftig wonach verlangend", gardha-h 
39868:„Hunger“ von ai. gardha-h in der Vokalstellung ab (s. u. gher- „begehren“).
```


## [2026-09-04T23:16:03.618Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ardyti\\|ardau\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "grep WLD for Lith ardyti"
}
```


### [2026-09-04T23:16:03.671Z] TOOL RESULT

```
5561:nicht besser nach Leskien Abl. 329 zu ardyti „spalten, trennen“ s. u. er- 
9308:darm, After" (sei *ag&-oxog „der weite, geriiumige" : lit. crdvas, ardyti ;
```


## [2026-09-04T23:16:08.486Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"„Teil, Seite, Hälfte\\|Teil, Seite\\|ardh\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | sed -n '1,20p'; echo \"---\"; grep -n \"er-, ere-\\|er-, era-\\|„selten, locker\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head",
 "description": "locate WLD er- root"
}
```


### [2026-09-04T23:16:08.556Z] TOOL RESULT

```
5550:ardh- — al-, ol- 
5556:ardh- „Stange“? 
5566:*ardh-tro~, -ti- (anders, aber nicht besser Reichelt KZ. 46, 313f.: *azd-ti: 
5781:arodat „er lasse gedeihen 44 , orjilat- „Gedeihen schaffend“, ai. ardhuka- „ge- 
9293:aber wohl fern, s. ardh „Stange". Dazu wohl ai. rdhak „besonders, abge- 
9294:sondert", drdha-h „Teil, Seite, Halfte", ardlui- „halb", n. „Teil, Halfte". 
9664:durch dh (vgl. doo!) vvm usw. vorliegt) (wie bei ai. vardhate : (f)oddlg). s. 
9671:weisenden Proportion rclhati : vardhate = arsati : variati (z. B. Petersson 
9673:setzbarkeit von ardhiika- ,,gedeihend“ mit aisl. qrdagr (ibd., Persson Beitr. 
18303:Speer -1 s. u. ardh- „Stange -1 ;. 
18353:Ai. vardhate „erhebt, macht wachsen", av. varod- „augere"'; ai. iirdhva- 
25750:668 f. — S. noch *kerdho- „Reihe, Herde" (wo auch iiber ai. gardhati ,.ist 
26688:Ai. f ardhate „ist frech, trotzt“ bleibt trotz lick 1*44 fern. 
26717:Ai. rardha- m , cardhas- n. „Herde, Scbar“, av. saroSa -, apers. pard- 
26751:rardhati ..tritt keck, trotzig auf, schert sich worum nicht - , cardha- ,,frech, 
32283:acymr. petuerul : toch. sdardh, itardh , sdhardh; ahd. fiordo, ags. feorda, aisl. 
39853:grdJinu-h „gierig‘‘, grdhra-h „gierig, heftig wonach verlangend", gardha-h 
39868:„Hunger“ von ai. gardha-h in der Vokalstellung ab (s. u. gher- „begehren“). 
---
8839:Bewegung nach abwarts." Basenformen er-, ere-, /„thematisch"), ere (?), 
8845:Basi sformen er-, ere- (einsehlielilich paradigmatisch damit ver-
```


## [2026-09-04T23:16:17.224Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('„Teil, Seite, Halfte\"')\nif i<0:\n    i=t.find('drdha-h')\nprint(i)\nseg=t[:i]\ntags=re.findall(r'\\[pdf page (\\d+)\\]',seg)\nprint('last tag',tags[-3:] if tags else None)\nprint(t[i-300:i+200])\nEOF",
 "description": "find WLD page tag"
}
```


### [2026-09-04T23:16:19.069Z] TOOL RESULT

```
655516
last tag None
ern, trennen", erzu, erdu, erst   trennen" (zur bait. Sippe s.
                                                                      ,,


Leskien Abl. 329; lit. ardai „Stangengeriist zum Flachstrocknen" bleibt
aber wohl fern, s. ardh „Stange". Dazu wohl ai. rdhak „besonders, abge-
sondert", drdha-h „Teil, Seite, Halfte", ardlui- „halb", n. „Teil, Halfte".

      C*re-dh -:)   aksl. rcd-slz „selten“       (wohl       stoliitonig,        vgl.       cech. fidhy, sloven.
```


## [2026-09-04T23:16:24.446Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('drdha-h')\nprint('leaf', t.count('\\f',0,i))\nprint(repr(t[:200]))\n\"",
 "description": "WLD leaf"
}
```


### [2026-09-04T23:16:26.406Z] TOOL RESULT

```
leaf 151
'            GOVERNMENT OF INDIA\n ARCHEOLOGICAL SURVEY OF INDIA\n\n               CENTRAL\n            ARCHEOLOGICAL\n                LIBRARY\nACCESSION NO. jj03?7\nCALL No. gJ3 Wafjpok\n                 f_\nD'
```


## [2026-09-04T23:17:02.447Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FRS فرارون\"; grep -n \"فرارون\\|فریرون\" FRS.txt FRS_pages.txt 2>/dev/null | head -5; echo \"=== SKT context\"; sed -n '19200,19205p' SKT.txt; echo \"=== FSD tariff line 30878 head\"; sed -n '30874,30879p' FSD_vol4.txt | head -c 600",
 "description": "FRS fararun, Skeat, FSD"
}
```


### [2026-09-04T23:17:02.538Z] TOOL RESULT

```
=== FRS فرارون
FRS.txt:14435:فرارون 
FRS.txt:14437:حسودت در ید بهرام رون نظر زی تو ز برجیس فرارون 
FRS.txt:14444:آنرا فرارون گویند آنچه برصلاح بود و آنچه بر صلاح نبود آنرا فربرون" گوابند » 
FRS.txt:21925:فرارون ۳۷۸ 
FRS_pages.txt:16088:                             ‫فرارون‬
=== SKT context
Tar^ti  1  small  shield,  &c.  ;E. ;  with F.  svjix.)  Formerly  also  tergat;  the  -et is  the  F.  dimin.  sufiix.  — A.  S.  targt,  a targe,  shield. +Icel.  targa,  a  target;  O.  H.G. Morga,  a  frame,  side  of  a  vessel,  wall,  G. wargt,  frame,  case,  side,  border.  (The  F. targr^  Span,  tar/a,  &c.,  are  of  Tent,  origin.) Cf.  Lith.  darias,  enclosure,  border,  halo round  the  mooo.  ^  Distinct  from  Arab. darkat,  darakat,  a  shield,  whence  Port,  and Span,  adarga,  a  small  square  target.
Targum,  a  ChaUIcc  paraphrase  of  the Old  Testament  (Chaldee.)  Chaldee  tar- gdm^  an  interpretation.  — Chal.  targhn,\.o interpret.  Cf.  Arab,  tarjum^,  an  inter- preter; see  Dragoman.
Tariff.  (F.- Span. -Arab.)  F.  tartfe. a  casting  of  accounts. —  Span,  tarifa,  a  list of  prices,  book  of  rates.  —  Arab,  tariff giving  information,  notification  (because  a tariff  gives  notice}.  — Arab,  'arf,  knowing, knowledge.  — Arab  root  'ara/a,  he  knew.
Tarn,  a  pool.  (Scand.)  M.  E.  teme.^ Icel.  tjctm  Cgcn.  tjarnar).  a  tarn,  pool ;  Swed, dial,  tjdm,  tam^  a  pool  without  an  outlet
TatTiiah.  (F.  -O.H  G.)  F.  temus-, stem  of  pres.  pt.  of  se  ternir,  to  become  dim, lose  lustre  (Cot.).  -  M  H.G./fr«r«,  O.H  G. tarnjan,  to  obscure,  darken. +A  S.  dernan^ dyrnan,  to  hide,  from  deme,  dyme,  adj., secret  :  ef.  O.  Sax.  derm,  hidden,  secret ; Gk  8aX.afiof,  a  Bccrct  chamber,  lorking- placc.    (VDHAR.)
Tarpaulins ;  see  Tar.
=== FSD tariff line 30878 head
tassel,  also,  a   jeweled omamenthkeashield  9.  Physics,
The  metal  plate  at  the  focus  of  a   Roentgen-ray  tube, usually  made  its  anode,  from  which  the  X-raj's  emanate I<F  targe,  shield,  ofTeut  ongm,  cp  AS  farye,  shield, G   rarpe,  frame  3   tar'guetf- —   tar'gct*card",  n   A   card  ringed  like  a   target  used  for keeping  a   marksmans  score  — t.dantorn,  n   A   railuay elgnal-lantern  for  use  as  a   target  t.dampt.—  t   *rangc,  n A   place  prepared  for  shooting  at  targets,  shooting-range  — t   #rlfle,  n   A   rifle  made  expressly
```


## [2026-09-04T23:17:12.040Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14433,14448p' FRS.txt",
 "description": "FRS fararun entry"
}
```


### [2026-09-04T23:17:12.095Z] TOOL RESULT

```
و و ۷ 
فرارون 
کواکب بیابانیست » آن که رفتنمان باز بیش بود» دقيقی کوید : 
حسودت در ید بهرام رون نظر زی تو ز برجیس فرارون 
.۸ 
گیزوب 
آن ستاره [ ها ] بود که رفتنشان مفسد باشد » خسروانی کفت : 
۱- نقط در ن و چ. ۲- اضاً نقط در ن و چ۰ ۴ - نقط در چ ون 
6 درل ؛ فرخی ۵- چ : چونانك که اعدای‌ترا 1- ایضاً نقط در چ ون ۰ 
ه چ ۰ فرلرون کواکب ییابانبان فریررون [ کذا ] گویند زانکه رفتتشان بازپس‌بود 
آنرا فرارون گویند آنچه برصلاح بود و آنچه بر صلاح نبود آنرا فربرون" گوابند » 
س : این لغت ولنت بد را ندارد ۷ - چ : فیرون مضد بود * 


۳۷۹
```


## [2026-09-04T23:17:34.106Z] AGENT

Now I'll write the verification file.


## [2026-09-04T23:22:38.989Z] TOOL CALL #79: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build63.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_VARUN = \"https://en.wiktionary.org/wiki/%D9%88%D8%A7%D8%B1%D9%88%D9%86\"\nW_FARARUN = \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D8%B1%D9%88%D9%86\"\nW_TARIF = \"https://en.wiktionary.org/wiki/%D8%AA%D8%B9%D8%B1%D9%8A%D9%81\"\nW_ERFAN = \"https://en.wiktionary.org/wiki/%D8%B9%D8%B1%D9%81%D8%A7%D9%86\"\nW_TARIFA = \"https://en.wiktionary.org/wiki/tarifa\"\nW_TARIFF = \"https://en.wiktionary.org/wiki/tariff\"\nETY = \"https://www.etymonline.com/word/tariff\"\nAHD = \"https://www.ahdictionary.com/word/search.html?q=tariff\"\nAB_VARUN = \"https://abadis.ir/fatofa/%D9%88%D8%A7%D8%B1%D9%88%D9%86/\"\nAB_FARARUN = \"https://abadis.ir/fatofa/%D9%81%D8%B1%D8%A7%D8%B1%D9%88%D9%86/\"\n\ndata = {\n  \"pdf_page\": 63,\n  \"book_page\": 33,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ardha\",\n      \"verdict\": \"disputed\",\n      \"modern_form\": \"Old Iranian *arda- 'side, half' (Av. arəδa-, OP arda- only in arda-stāna-, Skt árdha- 'part, side, half'), from PIE *er-dh- 'separate, loosen' (Pokorny 332-333)\",\n      \"note\": \"The morpheme is genuine, but the root box misstates three things. (a) The gloss: 'swept, moved, pushed' is not the meaning of any Iranian *arda-; it is Mo'in's Persian rendering «بجلو جاروب کرده» ('swept forward') of Nyberg's OLD (1931 Hilfsbuch) gloss of the compound *fra-ardha-, copied by Nourai from BQT:1445 and then promoted to the meaning of the bare root. Nyberg himself abandoned it: in the 1974 Manual II glossary he analyses apārōn as < OIr *apārda-van- < *apa-arda- 'whose side is turned away', explicitly cross-referring to ārak 'side' < Av. arəδa-. (b) The language label: 'Old Persian' arda- is not attested as a free word; Bartholomae (AiW 193) posits p. arda- only from the compound arda-stāna- 'window-frame', and Kent (Old Persian, p. 166) rejects even that, taking arda- there as 'light' (cf. OP ardata- 'silver'). Avestan arəδa- is the securely attested form. (c) Mo'in's own second footnote (BQT:2246, on وارون) does NOT use this root at all: it analyses apārōn as apa- (prefix) + MP rōn 'side, direction' — so Nourai's two BQT citations pull in opposite directions and he has silently followed only the first.\",\n      \"note_fa\": \"ریشه‌ای که نورایی «Ardha» می‌نامد در اصل ستاک ایرانی باستان ⁎arda- به معنی «سو، کنار، نیمه» است: اوستایی arəδa-، سنسکریت árdha- «بخش، سو، نیمه»، و در هندواروپایی آغازین ⁎er-dh- «جدا کردن» (پوکورنی، ص ۳۳۲–۳۳۳). معنایی که در کتاب آمده («جاروب‌شده، رانده‌شده») برگردان حاشیهٔ مرحوم معین در برهان قاطع (ص ۱۴۴۵) از نیبرگِ قدیم است: «⁎fra-ardha (بجلو جاروب کرده)»؛ خودِ نیبرگ در واژه‌نامهٔ ۱۹۷۴ این معنی را کنار گذاشت و apārōn را ⁎apa-arda- «آن که سویش برگردانده شده» دانست و آن را به ārak «سو» بازبرد. برچسب «پارسی باستان» نیز دقیق نیست، زیرا arda- در پارسی باستان واژهٔ آزاد نیست و تنها از ترکیب arda-stāna- بازسازی شده و کِنت همان را هم رد کرده است. نتیجه: صورت ریشه پذیرفتنی است ولی معنی و برچسب زبانیِ آن را پژوهش امروزی نمی‌پذیرد.\",\n      \"sources\": [W_VARUN, AB_FARARUN],\n      \"ref_check\": [\n        {\"ref\": \"BQT:1445\", \"status\": \"supports\", \"note\": \"Borhan-e Qate', Mo'in ed., p.1445 (= BQT_v3_picofile.pdf p.238), footnote 8 to فرارون, read from the page image and saved to refs/ocr/BQT/1445.vision.txt: «نیبرگ ص ۷۲ - ۷۳ گوید: پهلوی frârôn (راست، درست، درستکار)، پازند frârûn، از ایرانی باستان ⁎frârdhavan - ⁎frârdha - ⁎fra-ardha (بجلو جاروب کرده)، قس apârak و apârôn». This is verbatim the source of Nourai's root gloss and of his transliterations frârdha / frârdha-van; the page really does say it.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BRT\", \"where\": \"AiW col. 193, s.v. arəδa-\", \"stance\": \"contradicts\", \"note\": \"'j. arəδa-, p. arda- 1) Adj. \\\"halb\\\" (nur Komp.). 2) m. \\\"Seite\\\" ... ai. ardha- Adj. \\\"halb\\\", m. \\\"Hälfte\\\", ardha- m. \\\"Seite\\\"; oss. ärdäg \\\"halb, Hälfte\\\"'. Bartholomae knows no sense 'sweep/push'. (A separate root 'arəd- V. \\\"gedeihen lassen\\\"' stands a few entries earlier and is unrelated.)\"},\n        {\"src\": \"KNT\", \"where\": \"Old Persian, Lexicon s.v. ardastāna- (p.166)\", \"stance\": \"contradicts\", \"note\": \"'ardastāna- sb. \\\"window-frame, window cornice\\\": arda- \\\"light\\\" as in OP ardata- \\\"silver\\\" ... (hardly as with Bthl. AiW 193 ...)'. Kent denies that OP has an arda- 'half/side' at all.\"},\n        {\"src\": \"TLM\", \"where\": \"Ancient Persian Lexicon s.v. ardastana\", \"stance\": \"partial\", \"note\": \"'ardastana, m. window-cornice (?) ... *arda, half. YAv. arəda + stana ... cf. Bartholomae, Altiran. Wb., 193' — Tolman keeps Bartholomae's 'half', still not 'swept'.\"},\n        {\"src\": \"POK\", \"where\": \"IEW p.332-333, root er-5, erə-, extension (e)r-e-dh-\", \"stance\": \"partial\", \"note\": \"'Old Indic ṛdhak \\\"especially, peculiar, particular\\\", ardha-ḥ \\\"part, side, half\\\", ardha- adj. \\\"half\\\", n. \\\"part, half\\\"; Lith. ardyti \\\"separate, split\\\"' — the IE background is 'separate', giving 'part/side/half', never 'sweep/push'.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I p.143 (leaf 151 of WLD_Bd1_pages.txt), root er- 'selten, locker'\", \"stance\": \"partial\", \"note\": \"'Dazu wohl ai. ṛdhak \\\"besonders, abgesondert\\\", árdha-ḥ \\\"Teil, Seite, Hälfte\\\", ardha- \\\"halb\\\", n. \\\"Teil, Hälfte\\\"'.\"},\n        {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. ārak (leaf 21) and apārīk (leaf 32)\", \"stance\": \"contradicts\", \"note\": \"'ārak [\\\\'lk\\\\'; Prth STR\\\\'] side ... from Av. (193) arəδa-'; and s.v. apārīk: 'apār- < *upārda < OIr upa- + *arda- \\\"side\\\" (v. ārak)'. Nyberg's own final position makes *arda- 'side', not 'swept'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Old Persian\",\n          \"words\": \"fra-ardha, frârdha, frârdha-van; apa-ardha\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"These are not attested Old Persian words but Old Iranian reconstructions, copied letter for letter (frârdha, frârdhavan, fra-ardha, apârôn) from Mo'in's footnote in BQT:1445, which in turn quotes Nyberg. The morphology is sound: preverb *fra- 'forward' and *apa- 'away, back' + *arda- 'side' + the possessive suffix *-van-, giving *fra-arda-van- 'having one's side forward' and *apa-arda-van- 'having one's side turned away'; intervocalic loss and contraction of *-ardavan > MP -ārōn. In Nyberg's 1974 Manual (Part II, s.vv. apārōn and frārōn) the gloss is 'whose side is turned away / forward', not 'swept forward, pushed back'; the 'sweep' gloss belongs to his earlier (1931) treatment, which is what Mo'in translated and Nourai reproduced. Old Persian itself has neither compound: the only OP trace of *arda- is arda-stāna- (DPc), and Kent even disputes that. The semantic pair 'forward = right/correct' vs 'backward = wrong/evil' is exactly what the Pahlavi pair shows, so the reconstruction is credible; only the language label and the gloss are off.\",\n          \"derivation_fa\": \"این صورت‌ها واژه‌های ضبط‌شدهٔ پارسی باستان نیستند، بلکه بازسازی‌های ایرانی باستان‌اند که نورایی عیناً از حاشیهٔ ۸ برهان قاطع (ص ۱۴۴۵) — و آن هم از نیبرگ — برداشته است. ساخت آن‌ها درست است: پیشوند ⁎fra- «به پیش» و ⁎apa- «به پس» + ستاک ⁎arda- «سو، کنار» + پسوند دارندگی ⁎-van-، یعنی ⁎fra-arda-van- «آن که سویش به پیش است» و ⁎apa-arda-van- «آن که سویش برگردانده است»؛ با افتادن d میان دو واکه و کشیده شدن واکه، ⁎-ardavan به ‑ārōn فارسی میانه بدل شده است. معنی «جاروب‌شده به پیش/پس» از تحریر کهن نیبرگ (۱۹۳۱) می‌آید؛ در واژه‌نامهٔ ۱۹۷۴ او خود معنی «سو» را جانشین آن کرده است. در پارسی باستانِ کتیبه‌ای هیچ‌یک از این دو ترکیب دیده نشده و تنها نشان ⁎arda- ترکیب arda-stāna- است. پس ادعای نورایی از نظر ساخت‌واژه با احتیاط پذیرفتنی است، اما برچسب «پارسی باستان» و معنیِ آورده‌شده نادرست است.\",\n          \"sources\": [AB_FARARUN, W_VARUN],\n          \"ref_check\": [\n            {\"ref\": \"NYB:23,76\", \"status\": \"partial\", \"note\": \"Nyberg, Manual of Pahlavi II (glossary). apārōn stands on leaf 32 of NYB_vol2_glossary.txt (printed p. ~23-24): 'apārōn [\\\\'p\\\\'lwn\\\\'] 1. adj. wrong ... opp. frārōn ... < OIr *apārda-van-, derived, by means of the suff. -van-, from *apārda- < *apa-arda- \\\"whose side is turned away\\\" (HP II, 15)'. frārōn stands on leaf 88 (printed p. ~75-80): 'frārōn [pl\\\\'lwn\\\\'] righteous, upright, honest ... OIr *frārda-van- < *fra-arda-, cf aparōn'. So Nyberg does give exactly Nourai's reconstructed forms — but glosses them 'side', not 'swept/pushed'. Page numbers are approximately right (the scan's leaf-to-page offset drifts by a few pages).\"},\n            {\"ref\": \"BQT:1445\", \"status\": \"supports\", \"note\": \"See refs/ocr/BQT/1445.vision.txt: '... از ایرانی باستان ⁎frârdhavan - ⁎frârdha - ⁎fra-ardha (بجلو جاروب کرده)، قس apârak و apârôn'. Nourai's node is a straight transcription of this line.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. 193\", \"stance\": \"partial\", \"note\": \"Av. arəδa- 'half; side' is the base; Bartholomae lists no *fra-arəδa- or *apa-arəδa- compound.\"},\n            {\"src\": \"KNT\", \"where\": \"Old Persian, Lexicon p.166\", \"stance\": \"silent\", \"note\": \"No fra-ardha- or apa-ardha- in the Old Persian corpus; the only arda- item is ardastāna-, which Kent analyses differently.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual II, s.vv. apārōn, apārīk, frārōn\", \"stance\": \"partial\", \"note\": \"Gives the reconstructions but with the 'side' semantics: 'apār- < *upārda < OIr upa- + *arda- \\\"side\\\" (v. ārak)'.\"},\n            {\"src\": \"PHD\", \"where\": \"Concise Pahlavi Dictionary, s.v. abārōn\", \"stance\": \"silent\", \"note\": \"MacKenzie gives only the MP forms ('abārōn [\\\\'p\\\\'lwn\\\\' | N wārūn] contrary, wrong, sinful'), no Old Iranian reconstruction.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"frârôn; apârôn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both Middle Persian words are securely attested and mean exactly what the chart says. MacKenzie: 'abārōn [ʾp̄lʾlwn' ] contrary, wrong, sinful' with NP wārūn as its descendant; PHD's English-Pahlavi half glosses 'contrary' and 'wrong' by abārōn, and 'sin' by abārōnīh. Nyberg: 'frārōn righteous, upright, honest', comparative frārōn-tar, Pazand frārūn, rendered in the Sanskrit versions by sadācārin- ('of good conduct'), against apārōn = asadācārin-. The pair is a live antonym pair in Pahlavi books (Dēnkard, Mēnōg ī xrad, Ardā Wirāz). The phonology is regular: *fra-arda-van- > *frārdvan > frārōn, *apa-arda-van- > *apārdvan > apārōn, with the -van- suffix giving MP -ōn. Semantically 'facing forward' → 'right, honest' and 'facing away/backward' → 'wrong, perverse, sinful' — exactly Nourai's glosses. Note that Mo'in in his second footnote (BQT:2246) prefers a different cut, apa- + MP rōn 'side, direction' (a word PHD confirms: 'rōn [lwn'] direction'), which reaches the same meaning by a shorter route.\",\n          \"derivation_fa\": \"هر دو واژهٔ فارسی میانه به‌خوبی گواهی شده‌اند و معنایشان همان است که در نمودار آمده. مکنزی: «abārōn وارونه، نادرست، گناه‌آلود» و فرزند فارسی نوِ آن را wārūn می‌آورد؛ نیبرگ: «frārōn راست، درست، درستکار»، برابر سنسکریتِ ترجمه‌ها sadācārin- «نیک‌کردار»، در برابر apārōn = asadācārin-. این دو در متون پهلوی (دینکرد، مینوی خرد، ارداویراف‌نامه) جفت متضاد زنده‌ای‌اند. دگرگونی آوایی قاعده‌مند است: ⁎fra-arda-van- ← ⁎frārdvan ← frārōn و ⁎apa-arda-van- ← apārōn؛ پسوند ‑van- در فارسی میانه به ‑ōn بدل شده است. از نظر معنایی «روی به پیش» ← «راست، درستکار» و «روی برگردانده» ← «وارونه، بد». مرحوم معین در حاشیهٔ ص ۲۲۴۶ تحلیل دیگری می‌آورد: apa (پیشوند) + rōn پهلوی «طرف، جهت» — که مکنزی هم rōn «جهت» را ثبت کرده است. ادعای نورایی در این گره درست است.\",\n          \"sources\": [W_VARUN],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1445,2246\", \"status\": \"supports\", \"note\": \"p.1445 fn.8 (refs/ocr/BQT/1445.vision.txt): 'پهلوی frarôn (عالی، مستقیم، راست) و frarônîh (تقوی، استقامت)'. p.2246 fn.12 (refs/ocr/BQT/2246.vision.txt): 'وارونه (ه.م.)، پهلوی apârûn، apârûnîh مرکب از: apa (پیشوند) و پهلوی rûn (طرف، جهت) اصلاً بمعنی کنار، قس: پهلوی frârûn'. Both Pahlavi words and both glosses are there; only the internal analysis of the second element differs between the two footnotes.\"},\n            {\"ref\": \"NYB:23,76\", \"status\": \"supports\", \"note\": \"NYB_vol2_glossary.txt leaf 88: 'frārōn [pl\\\\'lwn\\\\'] righteous, upright, honest ... comp. ~-tar ... Paz. frārūn, Skr v. sadācārin'; leaf 32: 'apārōn [\\\\'p\\\\'lwn\\\\'] 1. adj. wrong ... opp. frārōn. — 2. adv. backward (= apāc) ... Paz. awārūn, Skr. v. asadācārin (Mx); NP wārūn \\\"inverted, turned upside down\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"Concise Pahlavi Dictionary p.2 s.v. abārōn (PHD_mackenzie.txt line 704); p.72 s.v. frārōn (line 2321); s.v. rōn\", \"stance\": \"supports\", \"note\": \"'abārōn [\\\\'p\\\\'lwn\\\\' | N wārūn] contrary, wrong, sinful'; 'frārōn [pl\\\\'lwn\\\\'] righteous, honest'; 'rōn [lwn\\\\' | M rwn] direction. ō ... ~: towards'. English-Pahlavi index: 'contrary abārōn', 'wrong abārōn', 'sin abārōnīh'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual II, leaves 32 and 88\", \"stance\": \"supports\", \"note\": \"As quoted above; also gives the Pazand forms awārūn / frārūn that bridge to New Persian.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. وارون (via abadis)\", \"stance\": \"supports\", \"note\": \"Mo'in tags وارون '[په.]' (Pahlavi) and glosses it 'سرنگون، واژگون'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"frârŭn «فرارون»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP فرارون farārūn 'straight, upright, honest' continues MP frārōn without change beyond the regular Middle→New Persian raising of ō to ū (frārōn > farārūn), the same shift that gives MP abārōn > NP wārūn and MP rōn > NP رون. It is one of the oldest attested Persian words of this family: Asadi Tusi's Loghat-e Fors (ed. Mojtaba'i-Sadeqi, p.378-379) already has it, with the very Daqiqi verse Nourai prints — 'حسودت در ید بهرام فیرون / نظر زی تو ز برجیس فرارون' — and with a technical astrological gloss ('planets whose motion is direct'), beside the variant فریرون for retrograde motion. That astrological reading was rejected by Sadeq Hedayat (quoted by Mo'in at BQT:1445), who insisted the word simply means 'chaste, well-doing, pious', the antonym of اوارون; Dehkhoda follows him and derives it 'from Pahlavi farārun'. The chart's variants فریرون and فیرون are exactly the ones Loghat-e Fors and BQT record.\",\n          \"derivation_fa\": \"«فرارون» فارسی نو دنبالهٔ بی‌واسطهٔ frārōn فارسی میانه است؛ تنها دگرگونی، بدل شدن ō کشیدهٔ پهلوی به ū در فارسی نو است (frārōn ← farārūn)، همان تحولی که در abārōn ← وارون و rōn ← رون هم دیده می‌شود. این واژه از کهن‌ترین گواهی‌های این خانواده است: در لغت فرس اسدی (ص ۳۷۸–۳۷۹) آمده، با همان بیت دقیقی که نورایی نقل کرده و با معنی نجومیِ «ستارگان مستقیم‌السیر» و صورت مقابلِ «فریرون» برای رجعت. صادق هدایت (به نقل معین در برهان قاطع ص ۱۴۴۵) این معنی نجومی را رد کرده و گفته است فرارون یعنی «پاکدامن و نیکوکردار و پرهیزکار»، در برابر «اوارون» یعنی «گناهکار و شریر»؛ دهخدا نیز آن را «پهلوی farārun» می‌داند. صورت‌های فرعیِ فریرون و فیرون که در نمودار آمده دقیقاً همان‌هایی است که لغت فرس و برهان قاطع ثبت کرده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [W_FARARUN, AB_FARARUN],\n          \"ref_check\": [\n            {\"ref\": \"MON:2499\", \"status\": \"partial\", \"note\": \"Mo'in's 6-vol Farhang-e Farsi is not paginated online and the local text is only the 2-vol Adena abridgement, which drops فرارون (it has only فراروی). The entry itself was checked on abadis.ir, which reproduces Mo'in: 'فرارون (ف) (ص.) ۱- مترقی، پیش رو ۲- خوب، عالی ۳- راست، مستقیم ۴- (نجوم) سَعْد، اوج', and Dehkhoda on the same page: 'پهلوی farārun ... پاکدامن و نیکوکردار و پرهیزگار ... مقابل اوارون'. Content confirmed; page number 2499 not verifiable.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FRS\", \"where\": \"Loghat-e Fors p.378-379 s.v. فرارون (FRS.txt line 14435)\", \"stance\": \"supports\", \"note\": \"'فرارون: کواکب بیابانیست، آن که رفتنشان بازپیش بود. دقیقی گوید: حسودت در ید بهرام [فی]رون / نظر زی تو ز برجیس فرارون'; the apparatus adds 'آنچه بر صلاح بود ... آنرا فرارون گویند و آنچه بر صلاح نبود آنرا فریرون گویند' — the word, the verse and the variant فریرون all as in the chart.\"},\n            {\"src\": \"BQT\", \"where\": \"p.1445, entry فرارون + footnote 8\", \"stance\": \"supports\", \"note\": \"Body: 'فرارون - با رای بی نقطه ...'; footnote: 'فرارون بمعنی پاکدامن و نیکوکردار و پرهیزگار در مقابل لغت «اوارون» بمعنی گناهکار و شریر آمده ... رک: فریرون'.\"},\n            {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین + لغت‌نامه دهخدا s.v. فرارون\", \"stance\": \"supports\", \"note\": \"Dehkhoda: 'پهلوی farārun (عالی، مستقیم، راست)'; Mo'in: 'مترقی، پیش رو؛ خوب، عالی؛ راست، مستقیم'.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 214\", \"stance\": \"silent\", \"note\": \"Horn's only varun/-rūn item is '214. varun \\\"Begierde\\\" (AV., Men.), aw. varəna- \\\"Bekenntnis\\\"' — a different word entirely; Horn has no entry for فرارون.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"vârŭn «وارون»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP وارون wārūn/vārūn 'upside down, inverted; wrong, ill-omened, evil' continues MP apārōn/abārōn directly: initial ap-/ab- before ā regularly becomes w-/v- in New Persian (cf. MP abām > NP وام, abestā > اوستا, and the Pazand form awārūn quoted by Nyberg, which is the intermediate stage), and MP ō > NP ū. The extended form وارونه (with the adjectival -a) is the common modern word. Both the literal sense ('turned over') and the moral/fatalistic one ('perverse, ill-starred', as in بخت وارون) go back to the Pahlavi sense 'wrong, sinful' (Skr. asadācārin- in the Sanskrit Pahlavi versions). The word is attested from the earliest New Persian: Asadi's Loghat-e Fors glosses it 'بدبخت و شوم' and quotes Abu Shakur ('گمان برد کز بخت وارون برست'), and Ferdowsi's line that Nourai prints is the standard Shahnameh example. Wiktionary and MacKenzie both give exactly this MP > NP line.\",\n          \"derivation_fa\": \"«وارون / وارونه» دنبالهٔ مستقیم apārōn (abārōn) فارسی میانه است. تحول آوایی قاعده‌مند است: ap-/ab- آغازین پیش از ā در فارسی نو به w-/v- بدل می‌شود (قس: abām پهلوی ← «وام»، abestā ← «اوستا») و صورت میانی همان awārūn پازند است که نیبرگ ثبت کرده؛ همچنین ō کشیدهٔ پهلوی به ū فارسی نو بدل شده است. صورت «وارونه» با پسوند صفتی ‑ه ساخته شده است. هر دو معنی — «سرنگون، واژگون» و معنی مجازیِ «نحس، شوم، بدکردار» (مانند «بخت وارون») — از همان معنی پهلویِ «نادرست، گناه‌آلود» می‌آید. واژه از کهن‌ترین دورهٔ فارسی دری گواهی دارد: لغت فرس اسدی آن را «بدبخت و شوم» معنی کرده و بیت ابوشکور را شاهد آورده است، و بیت فردوسی که نورایی نقل کرده شاهد متعارف شاهنامه است. مکنزی و ویکی‌واژه نیز همین سلسله را می‌آورند. ادعای نورایی درست است.\",\n          \"sources\": [W_VARUN, AB_VARUN],\n          \"ref_check\": [\n            {\"ref\": \"MON:4941\", \"status\": \"partial\", \"note\": \"Page not verifiable (the 6-vol Mo'in is not online with pagination; the local 2-vol Adena abridgement has no page markers). The entry was read there: MON_part2.txt line 83342, 'وارون: [= وارونه] (ص.) باژگونه، واژگون، سرنگون، نگونسار، معکوس ... برعکس، مخالف. (مج.) نامبارک، نحس، شوم. بخت وارون: بخت بد، طالع شوم', and on abadis.ir Mo'in's full entry carries the origin tag '[په.]' (Pahlavi). Content matches Nourai's gloss 'upside down, wrong, evil' and the extra form وارونه exactly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"Concise Pahlavi Dictionary p.2 s.v. abārōn\", \"stance\": \"supports\", \"note\": \"'abārōn [\\\\'p\\\\'lwn\\\\' | N wārūn] contrary, wrong, sinful' — MacKenzie himself gives NP wārūn as the descendant.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual II leaf 32 s.v. apārōn\", \"stance\": \"supports\", \"note\": \"'Paz. awārūn, Skr. v. asadācārin (Mx); NP wārūn \\\"inverted, turned upside down\\\"'.\"},\n            {\"src\": \"FRS\", \"where\": \"Loghat-e Fors s.v. وارون (FRS.txt line 14016) and apparatus\", \"stance\": \"supports\", \"note\": \"'وارون: ندانم بخت را با من چه کین است ... ابوشکور گوید: گمان برد کز بخت وارون برست / نشد بخت وارون از آن یک بدست'; apparatus: 'وارون بدبخت و شوم باشد'.\"},\n            {\"src\": \"FSF\", \"where\": \"Noushin, Vazhe-namak s.v. واره/وارون (FSF.txt line 5905)\", \"stance\": \"supports\", \"note\": \"Lists وارون with the same Abu Shakur verse cited from Loghat-e Fors; the Shahnameh glossary treats وارونه as a live Ferdowsi word, supporting Nourai's Ferdowsi quotation.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt line 83342; abadis.ir فرهنگ معین\", \"stance\": \"supports\", \"note\": \"'[په.] سرنگون، واژگون' — Pahlavi origin tag, exactly the chart's arrow.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"A`.r.f, Ta`rîf\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic root ع ر ف (ʿ-r-f) 'to know'; form II عَرَّفَ ʿarrafa 'to make known', verbal noun تَعْرِيف taʿrīf 'notification, definition' (also تَعْرِفَة taʿrifa)\",\n      \"note\": \"The root box is right. What is wrong on this page is the western branch: Nourai routes the word Arabic > Turkish > Spanish > English, and none of his own references says that. Klein (his KLN) gives Spanish-Portuguese > English with no Turkish; AHD (his AHD), which he cites for the Turkish node, gives Italian > English with neither Turkish nor Spanish. Modern consensus (Etymonline, Wiktionary, Lokotsch 2037, Dozy) is Arabic taʿrīf > Medieval Latin/Italian tariffa > French/English, from Mediterranean merchant jargon; Dozy explicitly argues the word did NOT come to Europe through Iberia ('Uit het Iberische schiereiland schijnt het woord niet tot ons gekomen'), and Wiktionary notes that Spanish tarifa is a false friend that does not even mean 'tariff' (Spanish for that is arancel). A Turkish taʿrīfa/tarife does exist (Lammens records it), but as a parallel Arabic loan, not as the link in this chain.\",\n      \"note_fa\": \"خودِ ریشه درست است: ریشهٔ سه‌حرفی عربی ع‑ر‑ف «دانستن»، باب دوم عَرَّفَ «شناساندن» و مصدر آن تَعْریف (و تَعْرِفة). آنچه نادرست است مسیر غربی واژه است: نورایی زنجیرهٔ عربی ← ترکی ← اسپانیایی ← انگلیسی را رسم کرده، حال آن‌که هیچ‌یک از دو مرجع خودش چنین نمی‌گوید؛ کلاین «اسپانیایی‑پرتغالی tarifa» را مستقیم از عربی می‌گیرد و AHD «ایتالیایی tariffa» را. دیدگاه امروزی (اتیمانلاین، ویکی‌واژه، لوکوچ ش. ۲۰۳۷، دوزی) این است که واژه از زبان بازرگانی مدیترانه، یعنی از ایتالیایی tariffa / لاتین میانهٔ tarifa، به زبان‌های اروپایی رفته است؛ دوزی صریحاً می‌گوید واژه از شبه‌جزیرهٔ ایبری به ما نرسیده است. صورت ترکیِ تعرفه/tarife واقعاً وجود دارد (لامنس آن را ثبت کرده) اما وام‌واژه‌ای موازی است، نه حلقهٔ این زنجیره.\",\n      \"sources\": [AHD, W_TARIF, ETY, W_TARIFF],\n      \"ref_check\": [\n        {\"ref\": \"KLN:1573\", \"status\": \"partial\", \"note\": \"Klein has exactly one ʿ-r-f entry and it is the one Nourai wants: 'tariff, n. — Sp.-Port. tarifa, fr. Arab. taʿrīf, \\\"a making known, information\\\", verbal noun of ʿarrafa, \\\"he made known, he taught\\\", second conjugation of ʿarafa, \\\"he knew\\\". Cp. It. tariffa.' (KLN_1966.txt, leaf 834 of the 903-leaf scan, i.e. printed p. ~1641 — p.1573 of that edition falls in the 'starboard–starch' range, so Nourai's page number does not match the 1966-67 Elsevier pagination.) The content supports the root box but NOT the Turkish link.\"},\n        {\"ref\": \"AHD:1317\", \"status\": \"supports\", \"note\": \"The American Heritage etymology, checked in the current online edition, is '[Italian tariffa, from Old Italian, from Arabic taʿrīf, notification, infinitive of ʿarrafa, to announce, derived stem of ʿarafa, to know; see ʿrp in the Appendix of Semitic roots.]' — the Arabic root, the form II verb and the gloss 'information' are all exactly as in the root box.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"s.v. tariff (leaf 834)\", \"stance\": \"supports\", \"note\": \"Quoted above; Arabic root and form-II verbal noun identical to Nourai's box.\"},\n        {\"src\": \"LKT\", \"where\": \"no. 2037\", \"stance\": \"partial\", \"note\": \"'Ar. taʿrīf: \\\"Bekanntmachung\\\" [subst. Inf. II vom Vb. ʿarafa \\\"wissen\\\"]; hieraus it. tariffa \\\"Warenverzeichnis\\\", frz. tarif, sp. pg. tarifa ... engl. tariff' — same Arabic base, but Italian first and no Turkish.\"},\n        {\"src\": \"DOZ\", \"where\": \"s.v. TARIEF\", \"stance\": \"partial\", \"note\": \"'Ital. tariffa, Fr. tarif, is het Arab. taʿrīf of taʿrīfa. De wortel ʿarafa beduidt kennen; in den tweeden vorm ʿarrafa, doen kennen ...' — confirms the root, denies the Iberian route.\"},\n        {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\", \"note\": \"No entry for ʿ-r-f / taʿrīf: Jeffery only treats non-Arabic loanwords, and ʿarafa is native Arabic, which is itself confirmation that the root is Semitic.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"erfân «عرفان»; ta`refeh «تعرفه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are ordinary Arabic loans in Persian, taken over with the Arabic consonant skeleton unchanged and only Persian vowel colouring (ʿirfān > erfân, taʿrifa > taʿrefe). عرفان is Arabic عِرْفَان ʿirfān, the maṣdar of عَرَفَ 'to know'; in Persian it narrowed from 'knowing' to the technical sense 'gnosis, mystical knowledge, Sufism' (Mo'in devotes his entry to precisely this: 'شناختن، بازشناختن ... (به مفهوم خاص) یافتن حق'). تعرفه is Arabic تَعْرِفَة taʿrifa, a form-II verbal-noun variant of taʿrīf, and in modern Persian it acquired the mercantile sense 'schedule of duties, price list' — the same semantic development that produced European 'tariff', but reached in Persian via modern administrative usage, not borrowed back from Europe. The chart's extra forms عارف، معرفت، عُرف، عرفات، تعریف، معروف، مُعرّف، تعارف، متعارف، اعتراف are all regular Arabic derivatives of ع‑ر‑ف used in Persian (عرفات being the toponym traditionally explained from the same root by folk etymology).\",\n          \"derivation_fa\": \"هر دو واژه وام‌واژهٔ عربی در فارسی‌اند و ساختار صامتی عربی خود را دست‌نخورده نگه داشته‌اند و تنها واکه‌ها فارسی‌رنگ شده‌اند (ʿirfān ← عرفان، taʿrifa ← تعرفه). «عرفان» مصدر عربی عِرْفان از عَرَفَ «دانستن» است که در فارسی از معنی عام «شناخت» به معنی خاصِ «شناخت شهودی، تصوف» تخصیص یافته است؛ معین در فرهنگ فارسی همین را می‌آورد: «[ع.] شناختن، بازشناختن ... (به مفهوم خاص) یافتن حق». «تعرفه» صورت تَعْرِفة عربی (گونه‌ای از مصدر باب تفعیل) است که در فارسی امروز معنی «فهرست قیمت کالاها، سیاههٔ مالیات و عوارض» گرفته است — همان تحول معنایی‌ای که در اروپا به tariff انجامید، اما در فارسی از راه کاربرد اداریِ نو، نه وام‌گیری دوباره از اروپا. صورت‌های افزودهٔ نمودار (عارف، معرفت، عُرف، تعریف، معروف، مُعرّف، تعارف، متعارف، اعتراف) همه مشتقات قاعده‌مند همین ریشه‌اند. ادعای نورایی درست است.\",\n          \"sources\": [W_ERFAN, W_TARIF],\n          \"ref_check\": [\n            {\"ref\": \"FVA:267\", \"status\": \"not_checked\", \"note\": \"S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tehran 1368/1989 — no digital copy exists on any accessible platform (refs_online.json records a re-search in 2026 that found only the OpenLibrary catalogue record OL2012991M). Not consultable.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 95639 (عرفان) and line 41561 (تعرفه)\", \"stance\": \"supports\", \"note\": \"'عرفان: [ع.] (مص‌م.) شناختن، بازشناختن ...' and 'تعرفه: [ع. تَعْرِفه] (مصع.) معرفی کردن، شناساندن. (امص.) شناسایی. (اِ.) ورقهٔ شناسایی، فهرست قیمت کالاها، سیاههٔ مالیات و عوارضی که به ...' — Mo'in's '[ع.]' tag is the Arabic-origin arrow Nourai draws, and his gloss of تعرفه is Nourai's 'a list of duties imposed on imports or exports'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. tariff\", \"stance\": \"supports\", \"note\": \"Same Arabic base ʿarrafa / ʿarafa for the taʿrīf family.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"Nothing on عرفان/تعرفه, as expected: Asbaghi lists Persian words borrowed INTO Arabic, and these travel the other way.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-Farisiyya al-Muʿarraba\", \"stance\": \"silent\", \"note\": \"No entry for عرفان or تعرفه — again confirmation that these are not Persian words arabised but Arabic words persianised.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Turkish\",\n          \"words\": \"ta`rifa\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Ottoman Turkish تعرفه taʿrife / taʿrīfa is a real word, borrowed from Arabic تعرفة taʿrifa (and beside it تعریف taʿrīf > modern Turkish tarif 'description, recipe'), with the Arabic feminine ending -a > Turkish -e and the ʿayn lost in pronunciation; modern Turkish tarife means 'timetable, price list, tariff'. Lammens records it in exactly the sense the chart implies: 'En turc taʿrīfa a de même le sens de tarif, taxe.' So the node itself — a Turkish word taʿrifa derived from the Arabic root — is sound. What is not supported is Nourai's use of it as the link to the West, and in particular his citing AHD for it: AHD gives no Turkish form at all, either in the 1975 New College etymology or in the current online edition ('Italian tariffa, from Old Italian, from Arabic taʿrīf'). The Turkish-intermediary story belongs to a different lexicographic tradition (Random House, Collins) and even there it feeds Italian, not Spanish.\",\n          \"derivation_fa\": \"«تعرفه» ترکی عثمانی (taʿrife / taʿrīfa) واژه‌ای واقعی است و وام‌واژهٔ عربیِ تَعْرِفة است؛ در ترکی «ع» تلفظ نمی‌شود و ‑ة عربی به ‑e بدل شده، و صورت امروزی tarife به معنی «جدول زمانی، فهرست بها، تعرفه» است. لامنس همین را ثبت کرده است: «در ترکی taʿrīfa نیز به معنی تعرفه و مالیات است». پس خودِ این گره (وجود واژه‌ای ترکی از ریشهٔ عربی) پذیرفتنی است. آنچه پشتوانه ندارد نقشی است که نورایی به آن می‌دهد، یعنی حلقهٔ انتقال به اروپا؛ و به‌ویژه ارجاع او به AHD نادرست است، چون AHD هیچ صورت ترکی نمی‌آورد و مستقیماً از ایتالیایی به عربی می‌رسد. روایت میانجی‌گری ترکی از سنّت فرهنگ‌نویسی دیگری (رندم‌هاوس، کالینز) می‌آید و در آن‌جا هم واسطهٔ ترکی به ایتالیایی می‌رسد نه به اسپانیایی.\",\n          \"sources\": [AHD, W_TARIF],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"contradicts\", \"note\": \"The American Heritage etymology of tariff, checked online, is '[Italian tariffa, from Old Italian, from Arabic taʿrīf ...]' — no Turkish form is given anywhere in the entry, so AHD cannot be the authority for this node. (Nourai's page reference AHD:1317 is to the same tariff entry in the New College Edition, which he cites for the English node.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAM\", \"where\": \"Lammens, Remarques, s.v. Tarif\", \"stance\": \"supports\", \"note\": \"'En turc تعرفه taʿrîfa a de même le sens de tarif, taxe. Le dialecte vulgaire de Syrie emploie aussi de préférence taʿrîfa.' — the Turkish form the chart prints is real.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 2037\", \"stance\": \"silent\", \"note\": \"Lokotsch's whole chain (Ar. taʿrīf > it. tariffa > frz./sp./pg./engl.) never mentions Turkish, although his dictionary is precisely the one that would flag a Turkish mediation.\"},\n            {\"src\": \"TTS\", \"where\": \"Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen\", \"stance\": \"silent\", \"note\": \"grep -i 'tarif' over TTS_vambery1878_uoft_djvu.txt returns nothing: Vámbéry treats native Turkic stems and does not list this Arabic loan.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. tariff\", \"stance\": \"contradicts\", \"note\": \"Klein goes straight from Arabic to Spanish-Portuguese with no Turkish stage.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Spanish\",\n          \"words\": \"tariff\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"tariff\",\n          \"correct_form\": \"tarifa\",\n          \"derivation\": \"There is no Spanish word 'tariff'. The printed page (pdf p.63, box 'Spanish') really does show 'tariff', so the JSON extraction is faithful and the error is Nourai's own: the Spanish form is tarifa, as every one of his sources spells it — Klein 'Sp.-Port. tarifa', Skeat 'Span. tarifa, a list of prices, book of rates', Funk & Wagnalls '< Sp tarifa', Pihan explicitly 'Les Espagnols et les Portugais écrivent tarifa, les Italiens tariffa, et les Anglais tariff', Devic 'Esp. et portug. tarifa'. He evidently copied the English spelling into the Spanish box. Two further problems ride on this node. First, Spanish tarifa comes from Andalusian Arabic (< Classical Arabic تعرفة taʿrifa) directly, not from Turkish. Second, Spanish tarifa does not mean 'tariff' (customs duty) at all — it means 'fare, fee'; Spanish for a customs tariff is arancel (itself from Arabic, via ʿazl/marāsim per Lokotsch), so even the semantics of the arrow Spanish > English are wrong. Dozy states outright that the word did not reach the rest of Europe from Iberia.\",\n          \"derivation_fa\": \"واژه‌ای به صورت «tariff» در اسپانیایی وجود ندارد. تصویر صفحهٔ چاپی (صفحهٔ ۶۳ پی‌دی‌اف) نشان می‌دهد که در جعبهٔ «Spanish» واقعاً tariff چاپ شده است؛ پس استخراج داده درست بوده و خطا از خود کتاب است: صورت اسپانیایی tarifa است، چنان‌که همهٔ منابع خودِ نویسنده نوشته‌اند — کلاین «Sp.-Port. tarifa»، اسکیت «Span. tarifa»، فانک و واگنالز «Sp tarifa»، و پیهان صریحاً: «اسپانیایی‌ها و پرتغالی‌ها tarifa می‌نویسند، ایتالیایی‌ها tariffa و انگلیسی‌ها tariff». ظاهراً نویسنده املای انگلیسی را در خانهٔ اسپانیایی نوشته است. دو اشکال دیگر هم بر این گره سوار است: نخست آن‌که tarifa اسپانیایی وام‌واژهٔ مستقیم از عربی اندلسی (تَعْرِفة) است نه از ترکی؛ دوم آن‌که tarifa در اسپانیایی اصلاً معنی «تعرفهٔ گمرکی» نمی‌دهد و به معنی «کرایه، دستمزد» است (برابر اسپانیاییِ tariff واژهٔ arancel است). دوزی نیز تصریح کرده که این واژه از راه شبه‌جزیرهٔ ایبری به اروپا نرفته است. کوتاه: خطای چاپی کتاب، و افزون بر آن مسیر نادرست.\",\n          \"sources\": [W_TARIFA, ETY],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives this node no reference of its own.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHN\", \"where\": \"Pihan, Dictionnaire étymologique, s.v. TARIF\", \"stance\": \"contradicts\", \"note\": \"'Les Espagnols et les Portugais écrivent tarifa, les Italiens tariffa, et les Anglais tariff' — the Spanish spelling in the chart is wrong.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, s.v. Tarif and the index entry 'Tarifa, hisp.'\", \"stance\": \"contradicts\", \"note\": \"'Tarif. Esp. et portug. tarifa, ital. tariffa ... nom d'action du verbe ʿarraf, faire connaître, publier. C'est là l'étymologie, indiquée déjà par le P. Ange de Saint-Joseph (1684).' Spanish is tarifa, and it comes straight from Arabic.\"},\n            {\"src\": \"DOZ\", \"where\": \"s.v. TARIEF\", \"stance\": \"contradicts\", \"note\": \"'Uit het Iberische schiereiland schijnt het woord niet tot ons gekomen, want het Sp. en Port. hebben wel tarifa, maar het schijnt in die talen betrekkelijk jong te zijn' — Dozy denies the Iberian transmission route Nourai draws.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary, s.v. Tariff\", \"stance\": \"partial\", \"note\": \"'Tariff. (F.-Span.-Arab.) F. tarife ... Span. tarifa, a list of prices, book of rates. — Arab. taʿrīf ...' — supports a Spanish stage (via French), but spells it tarifa and knows no Turkish.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"tariff\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English tariff (first recorded 1590s, at first 'arithmetical table', then 'schedule of customs duties') is certainly from Arabic taʿrīf through a Romance intermediary, so the ultimate arrow is right; which intermediary is the open question. The older tradition that Nourai follows routes it through Spanish/French: Skeat 'F. tarife ... Span. tarifa'; Klein 'Sp.-Port. tarifa'; Funk & Wagnalls '[< F tarif, < Sp tarifa, < Ar taʿrīf, < ʿarafa, know]'. Modern reference works prefer Italian: AHD 'Italian tariffa, from Old Italian, from Arabic taʿrīf'; Wiktionary 'Italian tariffa ... first attested 1592'; Etymonline 'Italian tariffa, from Medieval Latin tarifa \\\"list of prices, book of rates\\\", from Arabic taʿrif ... a word passed to English from the commercial jargon of the medieval Mediterranean' (alongside garble, average, orange, tabby); Lokotsch 2037 the same. What no source supports is the specific Turkish > Spanish chain drawn here: Nourai's own AHD reference contradicts both intermediate steps. Verdict plausible rather than confirmed: the Arabic origin is beyond doubt, the transmission route as drawn is a minority (and internally unsupported) version.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی tariff (نخستین کاربرد دههٔ ۱۵۹۰ به معنی «جدول حساب» و سپس «فهرست حقوق گمرکی») بی‌گمان از تَعْریف عربی است و در این حد ادعای نورایی درست است؛ اختلاف بر سر واسطه است. سنّت کهن‌تر — که نورایی از آن پیروی کرده — واسطه را اسپانیایی و فرانسه می‌داند: اسکیت «F. tarife … Span. tarifa»، کلاین «Sp.-Port. tarifa»، فانک و واگنالز «< F tarif, < Sp tarifa, < Ar taʿrīf». اما مراجع امروزی ایتالیایی را ترجیح می‌دهند: AHD «Italian tariffa، از ایتالیایی کهن، از عربی taʿrīf»، ویکی‌واژه «ایتالیایی tariffa، نخستین گواهی ۱۵۹۲»، و اتیمانلاین آن را از زبان بازرگانی مدیترانهٔ سده‌های میانه می‌داند (در کنار garble، average، orange، tabby) از راه لاتین میانهٔ tarifa. آنچه هیچ منبعی تأیید نمی‌کند زنجیرهٔ ویژهٔ «ترکی ← اسپانیایی» است؛ حتی همان AHD که نورایی به آن ارجاع داده هر دو حلقه را رد می‌کند. پس: با احتیاط پذیرفتنی است — ریشهٔ عربی قطعی، ولی مسیر انتقالِ رسم‌شده اقلیتی و بی‌پشتوانه است.\",\n          \"sources\": [ETY, W_TARIFF, AHD],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1317\", \"status\": \"partial\", \"note\": \"AHD's tariff entry (checked online; the New College Edition page 1317 is the same entry) reads '[Italian tariffa, from Old Italian, from Arabic taʿrīf, notification, infinitive of ʿarrafa, to announce, derived stem of ʿarafa, to know; see ʿrp in the Appendix of Semitic roots.]' It supports English tariff < Arabic taʿrīf but gives Italian, not Spanish, as the intermediary, and no Turkish stage at all.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. tariff (leaf 834, printed p. ~1641)\", \"stance\": \"partial\", \"note\": \"'tariff, n. — Sp.-Port. tarifa, fr. Arab. taʿrīf ... Cp. It. tariffa.' Supports a Spanish source, contradicts the Turkish stage.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Tariff\", \"stance\": \"partial\", \"note\": \"'(F.-Span.-Arab.) F. tarife, a casting of accounts. — Span. tarifa ... — Arab. taʿrīf, giving information, notification (because a tariff gives notice). — Arab root ʿarafa, he knew.' French, then Spanish, then Arabic.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary, s.v. tariff (FSD_vol4.txt line 30878)\", \"stance\": \"partial\", \"note\": \"'[< F tarif, < Sp tarifa, < Ar taʿrīf, < ʿarafa, know]' — same older Spanish/French route, no Turkish.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 2037\", \"stance\": \"contradicts\", \"note\": \"'hieraus it. tariffa \\\"Warenverzeichnis\\\", frz. tarif, sp. pg. tarifa, rum. tarif ... engl. tariff' — Italian is the source of the whole European family, English included.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nimport io\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-63.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build63.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-63.json > /dev/null && echo \"VALID JSON\"",
 "description": "Write page-63.json"
}
```


### [2026-09-04T23:22:41.769Z] TOOL RESULT

```
written
VALID JSON
```


## [2026-09-04T23:22:46.820Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 tools/verify_check.py 63",
 "description": "Run verify_check for page 63"
}
```


### [2026-09-04T23:22:48.568Z] TOOL RESULT

```
nodes verified: 8/8
node verdicts: {'plausible': 3, 'confirmed': 4, 'transcription_suspect': 1}
root verdicts: {'disputed': 1, 'confirmed': 1}
ref checks: {'partial': 4, 'supports': 3, 'not_checked': 2, 'contradicts': 1}
books consulted: {'partial': 6, 'silent': 7, 'supports': 14, 'contradicts': 5} | by book: {'MON': 4, 'NYB': 3, 'PHD': 3, 'KLN': 3, 'FRS': 2, 'LKT': 2, 'SKT': 2, 'BRT': 1, 'KNT': 1, 'BQT': 1, 'HRN': 1, 'FSF': 1, 'PLA': 1, 'AFM': 1, 'LAM': 1, 'TTS': 1, 'PHN': 1, 'DEV': 1, 'DOZ': 1, 'FSD': 1}
```


## [2026-09-04T23:23:10.072Z] AGENT

Done. `data/verification/page-63.json` written and `verify_check.py 63` reports 8/8 nodes, no PROBLEM lines.

**Page 63 (book p. 33) — verdicts**
- Roots: 1 confirmed (Arabic ʿ‑r‑f / taʿrīf), 1 disputed (Old Persian "Ardha")
- Nodes: 4 confirmed, 3 plausible, 1 transcription_suspect
- Ref checks: 3 supports, 4 partial, 1 contradicts, 2 not_checked (FVA has no digital copy; the Spanish node carries no ref)
- Books consulted: 26 lookups across BRT, KNT, TLM, POK, WLD, NYB, PHD, BQT, MON, FRS, FSF, HRN, KLN, SKT, FSD, LKT, DOZ, DEV, PHN, LAM, TTS, FVQ, PLA, AFM

**Disputed / suspect items**
- ROOT "Ardha" [Old Persian] "swept, moved, pushed" — disputed. The morpheme is real (Av. arəδa-, Skt árdha- 'part, side, half', PIE *er‑dh‑, Pokorny 332‑333) but means *side/half*, not "swept/pushed". Nourai's gloss is a literal rendering of Mo'in's Persian «بجلو جاروب کرده» in BQT:1445, which translates Nyberg's **1931** gloss; Nyberg's 1974 glossary itself replaced it with *apa‑arda‑ 'whose side is turned away'. The label "Old Persian" is also wrong: OP arda‑ is only inferred from arda‑stāna‑, and Kent rejects even that.
- Node #3 entry 2, Spanish "tariff" — transcription_suspect, `error_in: book`. The printed page really shows "tariff" in the Spanish box; correct form is **tarifa** (so it is Nourai's slip, not an extraction error). Compounding it: Spanish tarifa is a direct Andalusian‑Arabic loan, not from Turkish, and does not mean "customs tariff" (that is *arancel*); Dozy explicitly denies the Iberian route.
- The whole western branch Arabic → Turkish → Spanish → English is unsupported by Nourai's own references: AHD (cited for the Turkish node) gives *Italian tariffa* with no Turkish and no Spanish; Klein gives Sp.‑Port. with no Turkish. Hence Turkish and English nodes are "plausible" rather than confirmed.

**Data/reference notes for the owner (no extraction errors found)**
- KLN:1573 does not match the 1966‑67 Elsevier pagination: Klein's *tariff* entry (which does say what Nourai claims minus the Turkish stage) is at printed p. ≈1641 (scan leaf 834); p. 1573 falls in "starboard–starch".
- MON:2499 and MON:4941 could not be page‑verified (the 6‑vol Mo'in is not online with pagination); both entries were verified by content via abadis.ir and the 2‑vol abridgement.
- Saved verbatim page transcriptions to `data/verification/sources/refs/ocr/BQT/1445.vision.txt` and `2246.vision.txt`; 10 web pages archived via `tools/fetch_source.py`.
