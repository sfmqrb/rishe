# Verification process log — verify-page-517


## [2026-10-15T02:44:16.751Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 517 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-517.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-517.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-517.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 517` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.814Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:20.055Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:20.167Z] TOOL RESULT

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


## [2026-10-15T02:44:22.279Z] TOOL CALL #2: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-517.txt; cat /home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md | head -80; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ | head -100; ls /home/sfmqrb/git/rishe-private/data/verification/ | tail -5"
}
```


### [2026-10-15T02:44:22.917Z] TOOL RESULT

```
=== PDF page 517 (book page 487) ===
--- entry 0 ---
ROOT [Indo-European] Udero, Uedero : abdomen, stomach, womb  (refs POK:1104)
#1 (parent #0) [Avestan] refs=POK:1104 | udara : abdomen
#2 (parent #0) [Latin] refs=POK:1104 | uterus : womb
  #3 (parent #2) [English] refs=None | uterus
--- entry 1 ---
ROOT Uĕ -> redirect to I 2
--- entry 2 ---
ROOT Uedero -> redirect to Udero
--- entry 3 ---
ROOT Ues -> redirect to Yu
--- entry 4 ---
ROOT Ug -> redirect to Aueg
--- entry 5 ---
ROOT Ugw -> redirect to Wegw
--- entry 6 ---
ROOT Uks -> redirect to Wegw
--- entry 7 ---
ROOT Uksen -> redirect to Wegw
--- entry 8 ---
ROOT [Turkish] Ul, Ol 2, Jol, Jor, Jur : to go, to step  (refs KLN:857; TTS:134)
#1 (parent #0) [Turkish] refs=KLN:857; TTS:134 | ulak : runner, courier, messenger, donkey
  #2 (parent #1) [Persian] refs=MON:3334; BQT:157 | olâğ «الاغ» : courier, load carrier, donkey
  #3 (parent #1) [Greek] refs=KLN:857 | oulakis : courier
    #4 (parent #3) [Italian] refs=None | 
      #5 (parent #4) [Spanish] refs=None | 
        #6 (parent #5) [French] refs=KLN:857 | laquis : courier, footman
          #7 (parent #6) [English] refs=None | lackey : servant
--- entry 9 ---
ROOT Ulp -> redirect to Wel 2
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
.rw-r--r--   60k sfmqrb 14 Oct 22:14  page-495.json
.rw-r--r--   66k sfmqrb 14 Oct 22:14  page-496.json
.rw-r--r--   35k sfmqrb 14 Oct 22:14  page-497.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-498.json
.rw-r--r--   49k sfmqrb 14 Oct 22:33  page-499.json
```


## [2026-10-15T02:44:27.374Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; sed -n 80,200p sources/SOURCE_MATRIX.md | grep -E '^\\- \\*\\*|refs/' | grep -iE 'TTS|LKT|MON|ARY|HJB|SKT|FSD|WEB' ; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','KLN','TTS','MON','BQT','AHD','WLD']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:700])\n\"; python3 -c \"\nimport json;d=json.load(open('page-499.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in d.items() if k!='entries'}));print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2500])\""
}
```


### [2026-10-15T02:44:28.001Z] TOOL RESULT

```
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
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
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based lea
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966:
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "No
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
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
   "stance": "supports
```


## [2026-10-15T02:44:30.084Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-517.json'));print(json.dumps(d,ensure_ascii=False)[:4000])\"; ls site/pages/517.jpg; cat tools/verify_check.py | head -60"
}
```


### [2026-10-15T02:44:30.654Z] TOOL RESULT

```
{"pdf_page": 517, "book_page": 487, "entries": [{"root": {"name": "Udero, Uedero", "lang": "Indo-European", "refs": "POK:1104", "gloss": "abdomen, stomach, womb"}, "nodes": [{"id": 1, "parent": 0, "lang": "Avestan", "refs": "POK:1104", "words": [{"translit": "udara", "gloss": "abdomen", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 2, "parent": 0, "lang": "Latin", "refs": "POK:1104", "words": [{"translit": "uterus", "gloss": "womb", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 3, "parent": 2, "lang": "English", "refs": null, "words": [{"translit": "uterus", "gloss": null, "script": null}], "script_extra": null, "note": null, "quote": null}]}, {"root": {"name": "Uĕ", "redirect": "I 2"}, "nodes": []}, {"root": {"name": "Uedero", "redirect": "Udero"}, "nodes": []}, {"root": {"name": "Ues", "redirect": "Yu"}, "nodes": []}, {"root": {"name": "Ug", "redirect": "Aueg"}, "nodes": []}, {"root": {"name": "Ugw", "redirect": "Wegw"}, "nodes": []}, {"root": {"name": "Uks", "redirect": "Wegw"}, "nodes": []}, {"root": {"name": "Uksen", "redirect": "Wegw"}, "nodes": []}, {"root": {"name": "Ul, Ol 2, Jol, Jor, Jur", "lang": "Turkish", "refs": "KLN:857; TTS:134", "gloss": "to go, to step"}, "nodes": [{"id": 1, "parent": 0, "lang": "Turkish", "refs": "KLN:857; TTS:134", "words": [{"translit": "ulak", "gloss": "runner, courier, messenger, donkey", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 2, "parent": 1, "lang": "Persian", "refs": "MON:3334; BQT:157", "words": [{"translit": "olâğ", "gloss": "courier, load carrier, donkey", "script": "الاغ"}], "script_extra": null, "note": null, "quote": null}, {"id": 3, "parent": 1, "lang": "Greek", "refs": "KLN:857", "words": [{"translit": "oulakis", "gloss": "courier", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 4, "parent": 3, "lang": "Italian", "refs": null, "words": [], "script_extra": null, "note": null, "quote": null}, {"id": 5, "parent": 4, "lang": "Spanish", "refs": null, "words": [], "script_extra": null, "note": null, "quote": null}, {"id": 6, "parent": 5, "lang": "French", "refs": "KLN:857", "words": [{"translit": "laquis", "gloss": "courier, footman", "script": null}], "script_extra": null, "note": null, "quote": null}, {"id": 7, "parent": 6, "lang": "English", "refs": null, "words": [{"translit": "lackey", "gloss": "servant", "script": null}], "script_extra": null, "note": null, "quote": null}]}, {"root": {"name": "Ulp", "redirect": "Wel 2"}, "nodes": []}]}
Permissions Size User   Date Modified Name
.rw-r--r--   49k sfmqrb 14 Oct 22:15  site/pages/517.jpg
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
```


## [2026-10-15T02:44:31.793Z] TOOL CALL #5: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/517.jpg"
}
```


### [2026-10-15T02:44:31.890Z] TOOL RESULT

```

```


## [2026-10-15T02:44:46.904Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'lackey' KLN_1966.txt | head; grep -n -i -E 'udero|uteru' POK_full.txt | head -20"
}
```


### [2026-10-15T02:44:47.306Z] TOOL RESULT

```
15022:flunky,  flunkey,  n.,  a  lackey.  —  Prob.  meaning lit.  ‘the  man  at  the  side’,  and  rel.  to  flank.  Cp, F.  flanquer,  ‘to  be  at  the  side  of,  to  flank’,  fr. flanc,  ‘side’.
17039:hagioscope,  n.,  an  opening  in  a  church  to  enable the  worshippers  in  the  side  aisle  to  see  the  altar. Compounded  of  hagio-  and  Gk.  -oocotuov,  fr. ctxo7xeTv,  ‘to  look  at,  examine’.  See  -scope, hagride,  tr.  v.,  to  ride  as  a  hag  does,  to  oppress.  — Compounded  of  hag,  ‘witch’,  and  ride;  esp. used  in  the  pp.  hagridden. ha  ha,  interj.  imitative  of  laughter  or  surprise, ha-ha,  n.,  a  sunk  fence,  usually  visible  only  when one  is  close  to  it.  —  F.,  prob.  from  the  inter¬ jection  ha  ha,  expressing  the  surprise  of  him who  faces  suddenly  such  a  fence, haiduk,  heiduck,  n.,  a  brigand  or  bandit  among the  Balkan  Slavs;  a  Hungarian  lackey.  —  G. Heiduck,  fr.  Hung,  hajduk,  pi.  of  hajdu,  but mistaken  for  a  singular.  Hung,  hajdu  is  prob. a  loan  word  fr.  Turk,  haidud,  ‘brigand’.
20968:See  alack  and  day. lacker,  n.  —  A  var.  of  lacquer, lackey,  also  lacquey,  n.  —  MF.  (=  F.)  laquais,  fr. Sp.  lacayo,  fr.  It.  lacche,  fr.  ModGk.  ouXdboji; (read  ulakis),  ult.  fr.  Turkish  ulak,  ‘runner,  cou¬ rier’,  from  stem  ul-,  ‘to  go’.
20969:Derivatives:  lackey,  intr.  v.,  lackey-ed,  adj. Laconian,  adj.,  pertainining  to  Laconia;  n.,  a  La¬ conian  or  Lacedaemonian.  —  See  Laconic  and suff.  -an.
20975:lacquey,  n.  —  A  var.  of  lackey, lacrima],  adj.  —  See  lachrymal, lacrimatory,  adj.  —  See  lachrymatory, lacroixite,  n.,  a  complex  basic  fluophosphate (mineral.)  —  Named  after  the  French  mineralo¬ gist  Frangois-Antoine- Alfred  Lacroix  (1863- 1948).  For  the  ending  see  subst.  suff.  -ite. lacrosse,  n.,  a  game  in  which  a  ball  is  thrown  by means  of  a  long-handled  racket,  the  crosse.  —  F. la  crosse,  ‘the  crozier,  the  racket  used  in  certain games’,  fr.  fern.  def.  article  la  (fr.  L.  ilia,  fem.  of ille,  ‘that’)  and  WTeut.  *krukja,  ‘crutch’.  See ille  and  crutch  and  cp.  crosse,  crossette,  crosier, lactarene,  also  lactarine,  n.,  material  made  from casein  of  milk,  used  in  calico  printing.  —  Form¬ ed  with  suff.  -ene,  resp.  -ine,  fr.  L.  lac,  gen.  lac- tis,  ‘milk’.  See  lacteal.
15595:d[/7]: -n-os), bruach^ big-bellied ' {*brusakos), cymr. brum. " venter, uterus ' (^b'" reuse-); 
30192:Jartu-' womb, uterus'; at most Old Indie gutlka^ pellet, globule, pill, pearl, drinking cup ' 
30361:Maybe alb. {*k)/emce^ womb, uterus (of animals)' : Gothic kilt^eii. 'womb', in-kilt^o 
39086:gr. SsAcpuq, -uoc; f., Doric SsAcpua " womb, uterus' (see below); *5£A(poc; n. ds. as base 
48823:crwthm. " hunch, fiddle, violin', crothi. "belly, uterus, vulva'; 
54121:lair ' (= Old High German lehtai), " womb, uterus, placenta, afterbirth ', Asxw a woman in 
54183:Middle Low German orloge, s. leugh-); Old High German lehter^ womb, uterus, placenta, 
54199:\/b lagatr\n\aY' etc.; laze' lair, womb, uterus', *sg-logb (Serbo-Croatian- Church Slavic 
57735:gr. [jriTpa f. ' womb, uterus, marrow of the plant ', Latin matnx^ a mother in respect to 
67468:pavltar-, p6tar-rc\. "Reiniger, Lauterer', yC>5i//?/'5/r7"Lauterungsmittel, Seihe, sieve '; pavana- 
67471:Lauterung dienend'; 
83083:forms) 'throat, estuary (the bubble, of Uterus); Magenmund, stomach'; lengthened grade 
86605:and "uterus', tunku, tukti'iett become', Latvian tukt6s., /J/rs "swelling, lump, growth', tauks 
88040:Root / lemma: udero-, uedero- 
88045:(because of Asper rather for *u5£po(;); Latin uterus^\ower abdomen, belly, esp. womb, 
88046:uterus' (/for o^am ehesten zugleich with dem phonetic alteration from *udris^\\ose' to 
88052:UGTspa 'womb, uterus' {ud-^ compounds-suffix tero). 
90488:u/tia-m. n. "wrapping of embryo, womb, uterus' (compare Latin vo/va); 
90569:involucre "Serviette', probably also 1/0/1/5, vulva " womb, uterus, Eihaut the Pilze'; 
93528:£uxou(; x^vn ("Trichter') laAafjivioi Hes.; (because of uoioo,, uaT£pa see below udero-
```


## [2026-10-15T02:44:49.971Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 88036,88060p POK_full.txt; grep -n -i -E 'udara' BRT.txt | head; grep -n -E 'udero|uedero|udero-' AHD_watkins1985.txt IEC.txt | head; grep -n -i 'udero\\|uedero' incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-10-15T02:44:50.433Z] TOOL RESULT

```
References: WP. 1193 f., Mayrhofer 1, 107. 
Page(s):1103 

Root / lemma: udero-, uedero- 
Meaning: belly 

Material: 1 . Old Indie udara-m ^beWy, intumescence of Leibes, the thick Teil eines Dinges, 
cavity, the interior', anudara- 'bauchles', Avestan udara-^s.\ gr. 65£po(; yaarrip Hes. 
(because of Asper rather for *u5£po(;); Latin uterus^\ower abdomen, belly, esp. womb, 
uterus' (/for o^am ehesten zugleich with dem phonetic alteration from *udris^\\ose' to 
*utris, ^/eAeingetreten); Old Prussian weders^beWy, stomach', Lithuanian vedaras^ 
intestines, entrails offish, intestines, entrails; Wurstmagen', Latvian veders, vedars^bQWy, 
stomach'; 

zur preposition ^o'belong perhaps gr. uaTO(; yaoTrip Hes. (*^o'-s/c»-s "vor-stehend') and 
UGTspa 'womb, uterus' {ud-^ compounds-suffix tero). 

2. Latin venter, -//7S 'belly' (could be *uend-ri-). 

3. Latin ve(n)sTcai. 'the bubble'. Old Indie vastf-m. 'bubble, bladder' {*undt/-7); 
1/5/7/5//?^- 'Mastd arm, or ein in the Nahe of Netzes liegender Korperteil'; compare 
nvuarpov 'Labmagen', Old High German wan{a)st, i4/^/7/s/' paunch'. Modern High German 
Wansta\so ' psalterium ', ablaut, isl. v/nsfrt ' psalterium ', Norwegian dial, v/nstrt 
'Labmagen' {* uen/strd); compare also Liden KZ 61, 19 ff. 
30377:•  j.  hu•f^ä'yajit1»n'^  •yaStiyn'*  AbsoL  •  j.  bUDara'vant-Adj.  (fem. 'faüT-) 'kirnst- 'mit  guter  Weihe  (an  die  Götter)',  in  Ver-  feitig,  geschickt,  tüchtig':  rtutäam  Hstam bindung  mit  dem  V.  yas—.  yasram  .... 'vaißm  Yt  16.  i ; — Asu  (rämL  iavie)  . . haptanhäitlm  .  .  'ttm  frSjaiiyatittm  "den  •vaiti  V.  i^.  30.
AHD_watkins1985.txt:1103:udero-. Abdomen, womb, stomach; with distantly similar forms (perhaps taboo deformations) in various languages. 1. Latin uterus (reshaped from *udero-), womb: UTERUS. 2. Perhaps taboo deformation *wen-tri- in Latin venter, belly: VENTER; VENTRILOQUISM. 3. Perhaps taboo defor- mation *wns-ti- in Latin vésica, bladder: vEsIca. 4. Vari- ant form *ud-tero- in Greek hustera, womb: HYSTERIC, HYSTERO-. [Pok. udero- 1104.]
AHD_watkins1985.txt:1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
AHD_watkins1985.txt:2441:UTERUS udero- UTMOST ud- UTTER! ud- UTTER? ud- UTTERANCE? _al-1 UVEA 6g-
AHD_watkins1985.txt:2447:VARY wer-? VASSAL upo vaT ped-2 vaTic wet-1 VAULT! wel-3 VAULT2 wel-3 VAUNT eu-2 VEAL wet-2 VECTOR wegh- VEDA weid- VEDANTA ant- VEDETTE weg-2 VEER2 per! VEGETABLE weg-2 VEHICLE wegh- VEIL weg-! VELDT pele-2 VELIGER gerere VELLEITY wel-2 VELOCITY weg-2 VELOURS wel-4 VELUM weg-1 VELVET wel-4 VENAL wes-1 VENATIC wen-1 VEND d6-, wes-! VENDETTA deik- VENEER per! VENERATE wen-! VENEREAL wen-! VENERY! wen-1 VENERY2 wen-! VENIAL wen-! VENIRE gWa- VENISON wen-! VENOM wen-! VENT wé- VENTAIL wé- VENTER udero- VENTILATE weé-
AHD_watkins1985.txt:2448:VENTRILOQUISM tolkw-, udero-
AHD_watkins1985.txt:2449:VENUE gWa- VENUS wen-1 VERACIOUS wéro- VERB wer-6 VERBENA wer-3 VERBOTEN bheudh- VERDANT virére VERDICT deik-, wéro- VERDITER ters- VERGE? wer-3 VERIDICAL deik-, wéro- VERIFY wéro- VERISIMILAR wéro- VERISM Wéro- VERITY wéro- VERMEIL wer-3 VERMI- wer-3 VERMICELLI wer-3 VERMICULAR wer-3 VERMIN wer-3 VERNAL west VERRUCA wer-1 VERSATILE wer-3 VERSE! wer-3 VERSION wer-3 VERST wer-3 VERSUS wer-3 VERTEBRA wer-3 VERTEX wer-3 VERTIGO wer-3 VERVAIN wer-3 VERVE wer-6 VERY weéro- VESICA udero- VESPER weS-pero-
IEC.txt:13191:pludero, pluduro, io “fly, flit, flutter, float about'. Cf. plüd- (2) OE floterian, v. “float about, flutter, flicker'; LG fluttern, f. ‘flutter’ beside flóttern, v. tr. “float — timber”; Fris. cf. flutterich, adj. limp, unstable'; Li. pluduru, -ti, & plüduru, -ti, v. “float about’; plüduras, m. “float, buoy’; plü- dra, f. ‘duckweed’; For Du. vlot, n. ‘raft, float’; adj. ‘fluent’; Fris. flot, id. & for LG flott, n. as Du.; wf. ‘fin’; see plud- (2) above. For Du. (fr. Fris.) flodderen, see next
IEC.txt:13195:pludero, pluduró, ió — plün-
IEC.txt:19518:uderos, om ‘belly, stomach’. WP I, 190 Skt. udáram, m. ‘belly, stomach, womb’; Cy- priot óderos (‘stomach’, Cypr. -o- for Gk. -u-. WP). (Isophone: Fris. otter (2) “stack of cut peat")
17477:190                                                       udero-, uedero-
17542: udero-, liedero- „Bauch“, und gleichbedeutende Worte ahnlichen Anlautes.
17570:                                                            udero-, uedero-                                             191
22414:(doch s. u. udero- „Bauch“).
```


## [2026-10-15T02:44:52.570Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 17540,17560p incoming/WLD/WLD_Bd1_pages.txt; grep -n -a -E 'udara-' BRT.txt | head; grep -n -a -E '^ *udara|udara- n' BRT.txt | head"
}
```


### [2026-10-15T02:44:53.034Z] TOOL RESULT

```
 udero-, liedero- „Bauch“, und gleichbedeutende Worte ahnlichen Anlautes.
   1. Ai. nddra-m ..Bauch, Anschwellung des Leibes, der dicke Teil eines

 Dinges, Hohlung, Inneres". anfidara-h „bauchlos“, av. udarf.-drasa- „auf
 dem Bauch kriechend, von Schlangen": gr. bbegog yarm'/g Hes. (wegen
 des Asper eher fiir *rdeoog. wie kypr. tioyoT fiir fivyoi, als o-stufiges *fo-
 degog);      lat.       uterus „Unterleib, Bauch, bes. Mutterleib, Gebarmutter"                                     (t fiir

 d    am     ehesten zugleich                     mit     dem Lautwandel von               *udris „Schlauch“ zu
 *utris, litereingetreten, Thurneysen KZ. 32, 564; aber nicht nach Wood
 Cl. Phil. 7,335 wirklich zu diesem Worte; andere Erwagungen bei Johans-
 son IF. 2, 5 ff. Bgm. II 2 1, 330; denkbar bleibt auch Kreuzung mit einem
                     1
                               ,


 verlorenen. zu got. qipus gehorigen Worte, mit welchem aber uterus nicht
 nach Fick BB. 1. 332, Wb. I 4 400 als *yYuteros urspriinglich verwandt sein
 kann, s. Yf. LEWb. 2 s. v.); apr. iveders „Bauch, Magen“, lit. vedaras ,.Ein-
```


## [2026-10-15T02:44:55.802Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -i -E 'udar[aä9ə]' BRT.txt | head; grep -n -i -E 'uterus' SKT.txt LAT.txt | head -5; grep -n -i 'uterus' SYN.txt | head -5"
}
```


### [2026-10-15T02:44:56.208Z] TOOL RESULT

```
30377:•  j.  hu•f^ä'yajit1»n'^  •yaStiyn'*  AbsoL  •  j.  bUDara'vant-Adj.  (fem. 'faüT-) 'kirnst- 'mit  guter  Weihe  (an  die  Götter)',  in  Ver-  feitig,  geschickt,  tüchtig':  rtutäam  Hstam bindung  mit  dem  V.  yas—.  yasram  .... 'vaißm  Yt  16.  i ; — Asu  (rämL  iavie)  . . haptanhäitlm  .  .  'ttm  frSjaiiyatittm  "den  •vaiti  V.  i^.  30.
LAT.txt:3111:flux de ventre (Plin.). Se dit aussi pour uterus, c£ P.P.17,18 aluus,
LAT.txt:30269:et S^-j£r6me: uterus insolescens dit ce dernier; tandis que Caton,
LAT.txt:67244:V. uterus', et ueslca.
LAT.txt:70687:uterus ( uter Caec. ap. Non.188, ix; uterum n. dans Pl., Turp., Afr.
LAT.txt:70689:se trouve le foetus, uterus". Ancien et classique.
6530:uterus * 3 Jearne! aN of both forms ? to the influence due like Lat.
```


## [2026-10-15T02:44:58.511Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 70685,70705p LAT.txt; grep -n -a -E 'Bauch' BRT.txt | head -20; grep -n -a -E 'Ddara|dara-0ra|udar' BRT.txt | head"
}
```


### [2026-10-15T02:44:58.983Z] TOOL RESULT

```
II s'agit peut-etre d'un emprunt A un parier indo-europeen, mais
qui aurait pass 4 par 1'etrusque.
uterus ( uter Caec. ap. Non.188, ix; uterum n. dans Pl., Turp., Afr.
ap. Non. 889 , »7 ), -I m.: ventre) en particulier "partie du ventre ou
se trouve le foetus, uterus". Ancien et classique.
Diminutif: uterculus, utriculus (Pline); adj. : uterinus.
On pense naturellement a skr .udaram "ventre", gr.ooepoC’ yaorqp
Hes., v.pruss. weders "ventre". Mais ceci n'explique pas le t. Les
mots de ce groupe ont des formes "populaires" instablea, ainsi qu'il
a 4 t 4 not 4 sous uenter.
utique: yr.ut.
utor, -eris, usus,sum, uti (ancien *oitor encore attest 4 dans
les graphies oeti, oetier = uti, oitile = utile, fournies par les
inscriptions anciennes ou les vieux textes de lois, e.g. CIL I 3
•et 8; S8C,9) Fest.»28,35; quelques emplois passifs de utor, cf.Nov.
ap.Geli.15,is,4): user, faire usage de, se servir, employer. Com-
plement A 1 1 abi.-instrumental (class.), et aussi, A 1 'epoque ancienne,
A 1 1 accusatif, d'oA 1 'expression dare utendum {aliquid), qui est
encore dans Cic. et Ov. - Vtor a aussi le sens derive de "avoir
des rapports avec", e.g. Cat., Agr.143,1, uilica uicinas aliasque
mulieres quam minime utatur-, "avoir A sa disposition, jouir de,
3104:(oder  'Mähnen-)  oder  Bauch-'  (oder ■Schwanz-)haar"  Yt./^.jr,  16.10.
8213:•  j.  udarö.drt^sa-  '>  Adj.  'auf  dem  Bauch sich  bewegend,  kriechend' '',  von  Schlangen: azinqm  °sanqm  Y.i4-S,  'Ä73-
8214:u.  «dära-  n.  'Bauch';  *%rq!a-  m.  'I-nuf,  Tgl. gr.  tpitu  (woiu  Bgm.  Grdr.' /.  690)'). —  Pü.; undeutlich;  ttV:  fa  askam  davarel.—  >) Lesung nicht  sicher;  L4,  K  I  haben  '^nisfanifm.  — ')  Vgl.  ai.  araga-  m.  —  ')  Zur  Nasalirung  »gl. %rq/>ia-.
15318:unihwan  Aqmpä/räiti*'>  "wer  den  Bauch
20104:•  j,  maräü-  f  'Bauch,  Wanst*  uzw.  daiv- ischcr  Wesen'':  nätrya  va  pu%rahe  vS Aaoyä  vä  *hty&  (GS.)*>  "für  des  Weibes
20403:•  j.  msi^zäna-  n.  'Bauch':  'zämii  F.//.
25521:•  j.  umd'wan-,  'iwar-  n.  'Eingeweide, Bauch':  'wan  F._?g;  —  yB  gSus  'wart hqmpnfraiti  (sd.)  V.  4.48;  —  auch  Plur. : astila  gaonala  ^dimohaca  *''wqmca  pah- yasca  fraväxlas^a  YL  /_J.  1 1 ;  —  yB  nars aiaonB  kaca  "wqn  bt/asyät  "der  bei  einem Gläubigen  die  Eingeweide  kurirt"  V.  7. 44(?);  —  alte  äaxma  (sd.)  upanAanzalta an/aräj  naiMät  barp%ri/va  'WBJiva  "die Leicheostätten  soll  sie  (damit)  besprengen innen  im  Mutterleib,   im  Eingeweide"  V.
4673:(es  ist)  .  .  als  sonst  die  Wölfe  (es  s\nA)"^Vfr>nfnU  ya^a  "«y.f  J'Ä/ (NPm.)  arsän5  V. 18.32;  YL/5.54;  —  baval  ai7fi.vanya  . . ta^ryavantfm  . .  piSammca  . .  uta  -nyasät (als  APm.)  .  .  fyaoninhS  Yt/(J,87'>;  — Aazannm  azinqm  udarS^rqsanqm  ..duyt /lazaare'nyaiiqmcii'V.iS.TyiT^.  b)  Plur. mit  vorausgch.  vjspa-  'alle  andern':  vispe ZI  "nye  *maoaKiAs  .  .  äai  Ab  yB  haomahe maoB  Y,  /0.8;  Yt  77.  5;  —  ya%a  azPtn avavata  v}r>^ra  hacfäneyaia  vupe  *'nye^ airt  Ytj.ög;  —  azSm  ..fravBivXd!  vTspSng "nySng  . ,  Y.  44. 1 1.  c)  Sing,  und  Plur.
6536:Vfil.  aiakva-.  —  Pü. :  fehlt. •  j.  azay-  m.  i)  'Schlange',  ein  ^ÄiÄisches Tier:  /<fiws.tara  ya^a  'zayS  xsvoewanhs V.iS.ßs;  —  'Sinam  udarS.>rasanam  .  . °iinam  spakanqm  kahrpunanam  (sd.)  V. 14.%.  a)  Sing,  in  koll.  Sinn:  äat  ahe paityänm  .  .  'zimca  yim  raoioibtn  (sd.) zj'rtM/a..V./.2''; — yai3  '%wä  niHt  aiwi,- Jruzilnti  •iisea  arütuiisca  "damit  dir kein  Arg  antun  können  Schlangen  und  .." YL5, 90.  2)  schlangenähnlichcs  Untier 'Drache,  Ungeheuer'":  'zdis  sairitaAe simahe  vlsS.valpahe  Y.().3o;  —  'zis .  . gäuitava . .  vTraja  Aog.  ~S;  —  'leis  vJlspahe N.  48;  —  ktrasäsps  .  .  yS  jartat  °ilm (sd.)  yim  aspB.garpm  mnganm  ..
8213:•  j.  udarö.drt^sa-  '>  Adj.  'auf  dem  Bauch sich  bewegend,  kriechend' '',  von  Schlangen: azinqm  °sanqm  Y.i4-S,  'Ä73-
11081:Ordnung:  manahicä  vacakicä  syaoiansi Y.30.3.  Bj  zur  Anknüpfung  eines  neuen selbständigen  Satzes  'und'  oder  imüber- setzbar;  m  folgt  dessen  erstem  Wort  b)  im Aw.:  duwar>snat>hs  da/snyä  (sd.)  hsnts xaAyJcä  .  .  xraospTitqm  (sd.)  Ufa  .  .  tratä is  dra/sS{&d.)  ..  momc3(s±)  asta  Y.5J.8; —  atySs, .  akäl  (sd)  mananh3  st3  äirym drBjtucS  pairi.matsiscä  (Sp.564  m.)  syao- tnqm  ..  Y-32-  3;  —  aj  f3  mainyB  ..vaAyi aitmcä  (sd.)  äsca  hudarthS  prj/  vTsyatä "^i-SO-y,  7  (aimaua),  32. 1  {aüyacä),  45.  7, 4-.S  i'äc'a),  49T>  1°  {''^l^^)y  49-  S  {täim, S3-3  C^*"^^);  —  a^äca  "kiwä  Smavantaslä (Sp.  567  a)  buyamä  rapsUca  tä  HS  dan- gStncS  ustäca  (ßp.  568  m.)  Y.4i-4',  —  *i)mS janhtntu  yahmat  haca  ..snatiat,.  'hriiatca (sd.)  &ia  .  .  gStd  apajasat  .  .  aß  paurva 7'aMaKyai(sd.)  ..  aidaca (sd.)  ila  ..  sadayät V.2.22— 24;  —  hö  vTsp>m  ahüm  ..va?nai .  .  darfsta  ddiat  * amir^x^äntim  vispqm ..galiqm  Yt /p.94;  —  (Vnam  ..  sqm' .  . yazamaUe  yä  ni  baraitl  yäslä  tsi  gmi  . . tä  yasamaide  Y.  38. 1 ;  —  kyatca  mSt  tnraos ..at..\. 43.12;—  prssa^a  na  ..  Y.  43- 10;  —  avavaitya  ..ya^a  im  sk  astica  im xä  avaiti..Y.i9.T,  —  *vJsqs  *tac'a'^>  i'taä Mäm^lf  . .  vJsmte  "und  diese  zwanzig Namen  .."  Yt. /.  19;  —  dasa  ..  msrfhö sayana  dva  hamina  talla  fanii  sarata  .  . V.  J.3;  2.41;' JÄ65  (/ijÄi),  YL/5.  51 ifaifa),    Y.  19.  10  f.  {fltiaica),  8.  4,    ig.  6
```


## [2026-10-15T02:45:02.127Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==165' incoming/TTS/TTS_pages.txt | head -80; grep -n -i -E 'ulak|ulag|ulaq' LKT.txt | head"
}
```


### [2026-10-15T02:45:02.544Z] TOOL RESULT

```
                                               135

 ilt.   Jor = gehen; ^'oW = antreiben                  ;
                                                           /«»•   = leben, gehen; jiif-
        üm, jür äs       =
                      Lehen, Gang.
'UV.    s^o»"^ = rennen .»f/«r;           —
                                 leben, gehen, wandeln.
          Abgesehen von der normalen Veränderung des auslautenden
        lin r oder vice versa, sprechen für die hier angegebene Ana-
        logie des Jol und Jor am besten die betreffenden Beispiele
        des Jakutischen, wo sir und sil für denselben Begriff ab-
        wechselnd gebraucht werden.
           In Anbetracht, dass Jür nicht nur laufen, sondern auch
        einen Anlauf nehmen,                  sich    ereifern bedeutet,        würde ich
        jiireJc    — Muth, Herz; JüreMi = mnthig, beherzt auch hier-
        her rechnen.      Es ist ebenso wie Icöngiil nur ein abstracter
        Begriff     und keine directe Interpretirung fraglichen Blut-
        gefässes.



                                               146.


                        Juk, Jify, JUV, ju, waschen.
"ig-        = waschen ^'wMwaZ; — sich waschen.
        Ji*»««/;                  ;


öag.                                      = gewaschen werden.
        junialc, jujmak (viie oben); JttfeaZma/i;
osm. Ji^mnaJc = waschen Jikanmak = sich waschen.
                                      ;
                                                    Uebrigens
        gibt es auch eine ältere              Form mit Ju und Jun.
az.     Jov, JuvmaJc (wie oben).
alt.    ju, Jjew = waschen, sich waschen.
jak.    siti,styailw         =
                     waschen; sun, sunabhi, auch sujun                             = sich
        waschen sußi;         =
                      Waschung.
kk.     t'urhen     = waschen.
CUV.    sJm«; =; waschen          (jput   s/wras     = sich das Gesicht waschen).
          Trotzdem juk die ältere Form zu sein scheint, so ist
        doch in den altern Sprachmonumenten Ju mehr gebräuchlich.
        Der ursprünglichen Bedeutung nach dünkt mir juk nicht der
        Grundbegriff des Waschens, d. h. Reinigens, sondern im Ge-
         gentheil des Sichbefleckens, Sichbeschmierens in sich zu ber-
         gen und scheint demnach mit j'm&                    =
                                               ankleben verwandt zu
         sein.   So vergleicht Budenz in seinem Magyar es finn.-
         ugor. nyelvekbeli szogyczisek, S. 85, ganz richtig das magy.
        fest =n\&\en mit dem linn. j;ese               —
                                           waschen, reiben, und fol-
         gende Wortfamilie gehört entschieden hierher, ja sie ent-
        hält sogar die ältere             und primitivere Form.           So:

331:[Tk.  alak-hulak.
333:52.  Tk.  alak-l)ulnk : 'Verwirrung',  alaga-hulagn  "As.ss.' ;  hier- aus vielleicht  rum.  alabadura,  arahabura 'Unordnung,  Gewirr,  Durcheinander,  Ge- misch'.
857:Auch  bhätä  oder  bhantä  'zinsloser  Vor- schuß an  Bauern';  hieraus  angloind. batta  'ein  besonderer  Zuschuß',  den  man früher  Offizieren,  Soldaten  oder  anderen Beamten  gab,  wenn  sie  ins  Feld  zogen oder  andere  ähnliche  Gründe  vorlagen. Beim  indischen  Militär  ist  das  batta  zur ständigen  Erhöhung  des  üblichen  Offi- ziergehaltes geworden,  also  etwa  'Aus- landszulage'.   [Hobson-Jobson  72/73.
2801:'Arm'  [vom  Stamme  kar,  kor,  kol  'Arm, Hand',  Vämbery  TktEtWb  S.  81,  Nr.  85; vgl.  ßuwasisch  kol  und  kul  'Arm'];  hier- aus russ.  kulak  'Faust,  Faustschlag', poln.  klruss.  kulak  'dass.'.  —  Gorjajew 174.  [M.  E.  ist  estnisch  kulak  erst  aus dem  Russ.  oder  Poln.  übernommen  und nicht,  wie  Mikl  SlEtWb  146  und  danach Bern  SlEtWb  641  haben,  Grundwort.]
2980:'Führer,  Lotse',  vulg.  kylauz  [Kel6kiau Kämüs  986:  kulaguz,  vom  Stamme  kol 'Arm,  Hand',  Vämbery  TktEtWb  S.  91, Nr.  85;  vgl.  Gag.  Ä-o/rfa^'i«? 'Helfer,  Leiter', ujgurisch  kolakuz  'Wegweiser'];  hieraus bulg.  serb.  kulanz,  bulg.  kalawuz,  poln. kalauz  'Führer,  Wegweiser';  rum,  cäläuz 'Führer,  Vorläufer,  Wegweiser'.  [Sain 48.    Bern  SlEtWb  472.
3071:Auch  lailak  [aus  pers.  llläg,  niläg,  s.  hier Nr.  1568]  'Syringa  vulgaris,  spanischer Flieder',  dessen  lilafarbene  Blütensträuße zwar  keinen  Farbstoff  liefern,  aber  einem bestimmten  Blau  seinen  Namen  gegeben haben ;  daher  hieraus  rum.  liliac  'P'lieder', Uliachiü  'lila',  lulachiu  'Indigo',  it.  sp. lilac,  frz.  lilas;  hu\g.  Iii' ak,lulak'^Fl\edev\ Cech.  poln.  lilak  'dass.';  dtsch.  lila  'bläu- lich', engl,  lilac  'Flieder'.  [Ngr.  XouXctKi 'bläuliche  Farbe  oder  Tinte'.]  [DE  297. Eguilaz  439.    Mikl  SlEtWb  169  b.
4771:2130.  Tk.  ulak:
```


## [2026-10-15T02:45:05.016Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4768,4778p LKT.txt; awk 'BEGIN{RS=\"\\f\"} NR==164' incoming/TTS/TTS_pages.txt | head -70; grep -n -i -E 'ulak|ulagh|ulag' incoming/TTS/TTS_pages.txt | head"
}
```


## [2026-10-15T02:45:06.111Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for f in SKT.txt FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt WEB_vol1.txt HJB.txt AID.txt DEV.txt PHN.txt; do echo \"== $f\"; grep -n -i -E '^ *lackey|lackey,|laquais' $f | head -4; done"
}
```


### [2026-10-15T02:45:06.459Z] TOOL RESULT

```
'Sack';  hieraus  russ.  juft',  juhf',  bulg. juft,  serh.  juhta,  6ech. juchta,  ^o\n.  Jucht : dtsch.  Juften,  Juchten  'ein  fernes  Leder', ndl.  juclit.  [Gorjajew  432.  Mikl  SlEtWb lOfia  (wo  ein  wohl  nicht  existierendes russ.  juft'  'Paar'  als  Grundwort  ange- geben wird,  da  die  Stücke  paarweise  ge- gerbt würden  •  wohl  kaum  richtig).
2129.  Tk.  Ujgur:
N.  pr.,  Name  eines  tk.  Volksstammes  im östlichen  Sibirien;  hieraus  frz.  ogre, sp.  ogro  'Popanz'  [Dicc  Gast  1447  c  mit Ableitung  von  skandinav,  Oegir,  einem Riesen  der  nordischen  Mythologie].  — ML  6048
2130.  Tk.  ulak:
'Läufer,  Eilbote'  [vom  Stamme  jol,  ol. ul  'gehen',  Vämbery  TktEtWb  S.  134. Nr.  145  I];  hieraus  [wohl  am  wahrschein- lichsten über  ngr.  oüXdKnt  MSOS  II,  239] frz.  laquois,  it.  lacM,  sp.  pg.  lacayo 'Diener';  dtsch.  Lakai.  Unmittelbar wurde  übernommen  rum.  olac  'Schnell- post', oläcar  'reitender  Eilbote'.
2131.  Ar.  'ulamä':
Plr.  von  '^alim  'Gelehrter'  [part.  psaes. act.  von  'alima  'wissen'],  tk.  ulema  als Sgl.  gebraucht  mit  der  Bedeutung: 'Rechtsgelehrter'  [und  zwar  Imam, Mufti  oder  Kadi,  s.  hier  Nr.  905,  1493 und  9S4];  hieraus  frz.  ouUma,  uUma, sp.  kat.  ulema;  Qi\%\,ulemn,  dtsch.  Ulema
167
[Ar.  'ulafa.
'^niuhaminedaiiischer  Gelehrter'.  [Devic DEt  223.    Eguilaz  510.    MWiD  64.
2 1 32.  Ar.  'ulüfa :
                                                     134



                                                     145.

    Jol, 61, ul, jor, jur, jür, gehen, schreiten, ivandeln,
                                            Gang, Weg.

                                                I.        -~l.

    uig.    jol= Vfeg, "Weise, Art, Sitte, Manier; jolamak, Jolahmuk.
            schicken, senden; Jolaiici, Jolauc = Gesandter   Prophet;',                       ,


            olanmak, jolanmak = sich begeben; olasmah = hin- und''
            hergehen, zueinander gehen, verkehren.
    cag.    ^'0?= Weg, Art, Linie, Richtung;                               ^o^MÄj^Ka/,;     = begegnen;
                 = Reitthier, Esel (eigentl. ein Fahrzeug; vgl. arab. v_*S^
            ««iaÄ;

            = gehen und >_Aiwo = Reitthier, Fahrzeug); jular = Zügel
            (von    = Richtung, folglich Richtunggeber, Lenker).
                     j/oZ

    alt. jol (wie oben); M/a=eine Richtung einschlagen;                                               iilala   —
            =
            den Weg weisen; it?a5'lcl  Wegweiser, Führer. =
    kaz. iilah — Bote   Läufer   tilau
                                 ,       Führung ulauH
                                            ;                 =                 ;                 = Führer,
            Leiter.
    jak.    suol — ^eg; »uollä — einen Weg machen.
    CUV.    Jo^ = Sitte, Gebrauch, Gewohnheit; «Jo^ = Weg, Mal; vUäk
            = Thier.
    kir.    sol — Weg, Art, Mal; «o?a = Gebrauch, Sitte; «o^aÄ = ge-
            streift,        mit Linien versehen.
    kk.     «'o?--=Weg.

                                                IL        —r.
•   uig.    JO'WÄ     = Gang, Weg, Art; Jorimak=:^ gehen, wandeln.
    «^"g-   J*ort(7i; = Schritt, Gang, Weg (jot'uJda jürnmelc = im Schrill
            gehen); Jortniak, Jorgalmak^^ im Trabe gehen oder reiten;
            Jorgun = müde             (eigentl.           abgegangen;               vgl.   stehen,       abge-
            standen); JormaJc =^ ermüden; jürümeJc, Jünümeh, züni'(-
            wieZ;   =
                  gehen, marschiren, herankommen.
    jak.    tsoruola =^ im Passe gehen; ^sorwo    Passgänger; sirif,        =
            sÜtsahin         =
                        gehen reiten fahren
                                       ,      sirl   Gang silai
                                                      ,               ;              =            ;
                                                                                                               —
            müde werden;             si^ä   — Müdigkeit           ;       sür, sürähm—lanien;
            sm>*mZ;=i: laufend, guter Läufer,                     Strömung.
    kk.     t'orormen         — ia.hren; t'oHrbeii ~ gehen; forterben =^ galo-
            piren

3761:       deutet eigentlich ruhig sein.                  Wie aus          Jiulak    =   Oi\iV,   sich
8231:         lalc,   Jaulak^Yt'ild; javuz= grimmig.
```


### [2026-10-15T02:45:06.816Z] TOOL RESULT

```
== SKT.txt
9836:Lookey.  X^acquey.  a  footman,  menial ftttcudant.  (K.  —  Span.?  —  Arab. ?)  From O.  F,  laquay,  •  a  lackey,  footboy ; '  Cot. There  was  also  an  O.  F.  form  aiatay ; Littr^  shews  tba^  in  the  15th  cent.,  a  cer* tnin  class  of  soldiers  (esp.  crossbow-mcn), were  called  alaj^ufs,  alacays,  or  latays.  (The prefix  a-  is  prob.  due  to  Arab,  al,  the  def. article.)  Prob.  from  Span,  hcayo.  Port loiaio,  a  lackey:  Port,  laeaia.,  a  woman- tervaiit  in  dramatic  performances.  *  Arab, luka^  worthless,  servile  :  as  a  sb.,  a  slave  ; laiid.  fern.,  mean,  servile.  Cf.  iakii\  hkC^ servile.  iakSi,  sJovenly.  ^  This  ti>  a  guess; it  is  much  disputed  ;  Diez  connects  it  with Ital.  Uuart,  U.  U(ktn,  to  lick.
== FSD_vol1.txt
== FSD_vol2.txt
== FSD_vol3.txt
== WEB_vol1.txt
== HJB.txt
== AID.txt
== DEV.txt
== PHN.txt
6639:LAQUAIS, &. m. (a.)
6642:suivre partout. — Laquais veut dire, en français, valet de pied^
6644:étymologistes sont peu d'accord sur l'origine de laquais, et ce-
10675:Laquais, s. m. (a.) Page â3&
```


## [2026-10-15T02:45:09.089Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 6639,6665p PHN.txt; grep -n -i -E 'lack-?ey' FSD_vol2.txt FSD_vol3.txt | head -5; grep -n -i -E 'LACKEY' WEB_vol1.txt | head -3"
}
```


### [2026-10-15T02:45:09.635Z] TOOL RESULT

```
LAQUAIS, &. m. (a.)
J^ \lakiyy\^ féminin A-is^ \lakiyyai[^ attaché à quelqu'un ou à
quelque chose; dérivé de J^ ^akà\ s attacher à quelqu'un et le
suivre partout. — Laquais veut dire, en français, valet de pied^
homme attaché au service d'un maître dont il porte la livrée. - — Les
étymologistes sont peu d'accord sur l'origine de laquais, et ce-
pendant ce mot semble calqué sur l'arabe, qui a passé dans
l'espagnol lacayo. Une nouvelle preuve de son origine arabe
est fournie par le portugais lacaio, dont le féminin lacaia (en
arabe a-ÂJ3 lakiyyat) signifie suivante, soubrette. Les Italiens
écrivent lacchè, et les Anglais lackey.LAS 235
LAQUE, 8. f. (a.)
J^ [lâk] et dJ [lak ou /^^] Sorte de gomme ou de «tic ruineux
qui découle dç plusieurs arbres de l'Inde , et dont la sécrétion
est déterminée par la piqûre d'un petit insecte hémiptère; elle
entre dans la composition d'un vernis qui sert pour la peinture.
— Autrefois on ne donnait ce nom qu'à la couleur cramoisie
préparée dans l'Inde avec la résine laque; mais aujourd'hui on
l'étend à plusieurs autres couleurs, et l'on dit laque verte, bleue,
jaune, etc. — Laque est aussi du genre masculin, quand ce
mot désigne spécialement le beau vernis noir ou rouge de la
Chine dont on décore des tables, des vases et autres ustensiles;
mais on ne voit pas bien pour quelle raison il est plutôt du
genre masculin dans ce dernier cas. — Les correspondants de
laque sont, en espagnol et en portugais, laça; en italien, lacca;
en anglais, lac, lake et lacca.
LASSITIJDE,8. f. (a.)
FSD_vol2.txt:23947:—   f.sirou,  re.  1.  shackle  for  the  foot.  2.  A   carriage- step.— f.-it,  n.  [London,  Eng.)  A   boj's’  jumping  game, like  leap-frog.—  f.-jaw,  re.  A   limb modified  into  a   mouth- part;  a   maxllllped.— f.skcy,  n.  An  organ-pedal.— foot'- knave" j,  n.  A   lackey.- r.4am!riiker),  n.  A   t.vamT>; vagrant.— f. -length,  re.  [F.ng,]  .Angling.  A   sncll.— f.i’ level,  re.  A   oomlilnatlon  level.  See  iusvel.-  f. -lever,  re. A   lover  worked  by  the  foot.—  f.  -lickcr,  n.  A   moan  flatterer; toarly:  fawner.—  f.-llnc,  re.  1.  Th('  lower  line  of  a   llshlng- seini';  lead-line.  2.  Z’rlnt.  Tlie  last  line  of  a   page,  particu- larly an  added  line,  as  for  tho  signature.— i'. -lining,  n. Naut.  A   horizontal  stnuigiliening  pliice  of  canvas  on  the
FSD_vol2.txt:23955:—   f.spage.  n.  A   boy  in  waiting:  lackey.— f.  span,  n.  i. A   foot»bath.  3.  A   foot»warmer.—  f.«passengcr,  n.  One who  passes  or  goes  on  foot,  as  over  a   toll-bridge.—  foot'- path",  n.  A   path  for  persons  on  foot.—  f.spavement,  n. A   paved  walk  for  foot-pas.sengers.— f. -phenomenon,  n. •Convulsive,  rhythmical  movements  caused  by  suddenly pushing  up  the  ball  of  the  foot  when  the  limb  is  extended: aslgn  of  spinal  co.  d   disorders:  aaklJC!on.is.— f.«pick,n.  A railroad  pick  with  head  pointed  at  one  end  and  having  a •crosspiece  like  a   toot  at  the  other,  whereby  ballast  may  be packed  under  the  rails  and  ties.— f. -picker,  n.  An  iron for  picking  dirt,  etc.,  from  a   horse's  foot.—  f. -plate,  n.  1. A   carriage-stop.  3.  An  iron  platform  on  a   locomotive  for the  engineer  and  fireman.-  f.  -plow,  n.  A   variety  of  swing- plow.—  f.  -post,  n.  A   post  or  messenger  on  foot,  or  tire  mail carried  la  this  manner.- f. -pound,  n.  Physics.  The  ordi- nary unit  of  mechanical  work,  being  the  W'.  rkdonelnmoving through  one  foot  against  a   resistance  of  one  pound,  as  in raising  a   pound  weight  one  foot.—  f.-ponndal,  n.  An  ab- solute unit  of  work,  being  the  work  done  in  moving  through one  foot  against  a   force  of  one  poundal.  See  poundal.— if. -pound -second,  a.  Physics.  Of  or  pertaining  to  a system  in  which  the  units  are  the  loot,  the  pound,  and  the second.  See  unit.— f. -power,  n.  Power  (as  lor  driving ■a  machine)  furnished  by  muscular  exertion  with  the  foot.
FSD_vol2.txt:70482:lack'ey,  1   lak'i;  2   liik'y , ».  !•  i.  !•  To  wait  on :   perfon mean  services  far;  attend  as  a   lackey.  3.  To furnish  with  lackeys  or  menial  attem dants.  II.  i.  To  act  as  lackey; be  a   servile  attendant, lack'ey,  a.  1,  A   male  servant  who waits  on  a   master;  a   footman  or footboy;  any  servile  attendant or  follower.
FSD_vol2.txt:70485:3.  A   lackey«moth,  [<  P.  fa-  Laokey*moth.  Female, quais,  <   gp,  lacayo,  prob,  <   natural  size.
FSD_vol2.txt:70487:of  a   laokey'moth,  which  is  marked  with  blue,  yellow,  and red  Stripes,  and  a   white  dorsal  line.  Compare  tent»catee- piLiAn.— l.iinoth,  n.  A   bombycid  moth  (genus  Clisio- camva),  especially  0.  neustrla,  with  two  croBs*strlpes  on  each fore  wing,  suggestive  of  a   lackey's  livery.
104635:é č Y of 5 r < $ 3. lakken, to lack, blame; compare D. lac/quér (-kér), n. [Fr. lacr, Moths, fate, from lanchanein, to obtain by lot or fate, ie Mette OLD. lecken to Tai] lac, from Per. lak, lac.] e, from laca, i la in Greek and Roman mythology, laken, ; : eye 1a ales h oes gum to happen.) in Gr í eA ont 1. (a) to be short (with of or in); (b) to . a clear varnish consisting that one ue a pera who measured ou pA el. gum resins dissolved in aha shellac fe z ponpen OT crimoli mali. he young lions do lack and suffer hunger. quick-drying solvents, with or w Pd Othe Jach’ry-mal, a. (ML. lacrimalis, Rogers, The young “APs. xxiv. 10. cellulose: pigments may be u at nee 3 rom L, lacrima, al oe for, or pro £ 2. to be wanting or missing; to be deficient.’ to form lacquer enamels. o lacque tears: Aa See ne aaber of small Peradventure there shall ede DVEF the me a n obtained fr m cert ch’'ry-m? an rri — Gen. xviii. 28. 4 i nd Japa 3 e tagiseefoundin ancient oman sepulchers, pop- lack oN Sees bs deficient in or ventirely smooth, highly polished fant o give a hard. la Tany supposed to have been a receptacle for ESATA OUE. . x 3. a decorative article or artel i la the tears of mourners; a lachrymatory. 4 If any of you lack wisdom, let him ask of wood and coated with this licae made of y 2. [pl.| the lachrymal glands, which produce God. f — Jamesi. 5. i Formerly, also spera lacker as tears. A 2. to want; to need. ac’qu€r, v.l. to varnish; to coat wi Also spelled poem f shedding tears: 3. to blame; to reproach; fo detract, (ObF to Germs with lacquer: formertacae, lach-ry-m4/tion, n. the act of sheddi ` 3. to suffer the absence or deprivation of; — spelled lacker. a la weeping, . o miss. [Obs. lac/quér-ér, n. one who lacquers: lach'ry-ma-tor, n, [from L. lacrima, a tear; jack vt. if PF cal usage, to pierce the hullof | maker. | 4 quers; a lacquer and -alor.| a substance that irritates the n a of (a ship) with shot. [Rare.] lac/quér-ing, n. the act of putting on a and produces tears, as tear gas: also spelled joy" interj. an exclamation of sorrow or re- _ also, the covering of lacquer or varnish Bae lacrimator. _ . pl. lach'ry:ma:to/ries gret; alas!: usually preceded by good. [Obs.] lac’quēr red, a yellowish-red color, often ay le lachy ma COT ys ni o A a. = lack-å-dāi’ṣiçăl, a. showing lack of interest or | in lacquer work. sed lo ML, lacrimatorium, trom lacrima, a tear.}a lacka miancnids listless lac’quér tree, a trec, Rhus vernicife lacheymal yer aa o ee AE ESL] adv. in a lackadaisical , cashew family. era, of the lach’ry:ma-to’ry, a. of, causing, orproducing lack-a-dai’si-cal-ly, - lac/quey (-key), n., v.l. and v.i. lackey [Ob tears: also spelled lacrimalary- lack’a-dai-sy, a. same as lackadaisical. lac'ri:măl, a. and 7. same as lachrymal, A lach’ry-mi-form”, a. shaped like a tear. _ lack’a-dai-Sy, inlerj. same as lackaday. la/cri-miin/d6, a. [It.] in music, plaintive; Ja Tach'ry:möse, a. [L. lacrimosus, from lacrima. ack’à-dāy, interj. àn exclamation of sorrow or menting: a direction to the performer, lz a tear.] } 7 ful regret. [Archaic.] lac’/ri-ma-tor, n. same as lachrymator, Pe een tedtearsicacd, © lacker, n. one who lacks. lac/ri-ma-to"ry, a. and n.; pl. lag’rimatgr x cause to ery and shed tears; sad. lack’ér, 7. and v.t. a ie ries, same as lachrymalory. l EA (DSI Tae eae aaieees lack/ey, 7.; pl. lack’eys, [OFr. laquay, a lack- Jge/ri-mdse, a. same as lachrymose, Bs lac/i-ly, adv. in a lacy manner or pattern. ey, also a soldier; Sp. lacayo, a fackey, fG0t= JAcrimo’so, a. same asilai mia $ lāc’i-ness, n. a lacy quality or T man; compare ae worthless, servile, Pr. la-croix’ite (la-krwiz/ite), n. [named after lac’ing, n. 1. the act of one who laces. lacai, a gormand. 3 K Aa oh Antoine Lacroix, a French mineralogist, 2. ashing. $ f Š 1. a male servant of low rank, usually in basic, hydrous fuophosphaterss ales 3, acord used in drawing tight or fastening; some sort of livery or uniform. + gl. calcium, manganese, and sodium: it is found : laces in general; Toue Gin boo bin ce 2. a follower who has no will of his own; a in yellowish-grecn crystals. i 3 ing, the cords which pass through holes toady. x = I (eos). #. (Er laeront iA pierced in the boards of the book, binding Jack/ey, v.t.; lackeyed, pl., pp.; lackeying, ppr. lacrosse Cee) el e; la, the, and them to the back; O in nautical nane to attend as or as if a lackey; to attend serv- ick Ge aa ct È y ope used to fasten two partsofa jlely. À ck, cros E or rey together or to bind them to lack/ey, v.i. to act as lackey; to pay servile ela abc oe the yard, boom, or gaff; (c) in machinery, a thong “attendance. 3 dians, in which two GU Ue aA of leather by which belts are lackey cat/ér-pil-lar, the larva of a lackey teams of ten men gach, e AN ce tilver brai to tri eg ee using long-handled, i 2 “4. gold or silver braid used to trim a uni- Jack’ey moth, a common European moth of pe eon Derg ry o | form, etc. pee the genus Clisiocampa, especially Clisiocampa $dvance the ball across ti 5. in bridge building, a system of braces joy stria: so called because the forewings, the field into the op- _ which conn sne bars of a truss, without which are striped, are supposed to resemblea Ponents’ goal. It is a lz eonan each other. lackey’s livery. 5 A avorite feld sport in 6. in ornithology, a border of a eae lack/lus’tér, lack’lus”tre (-tér), a. lacking tavenie ee aT leo which differs in color from the web: also, the “brightness; dull; as, lackluster eyes. redin England and i i petant Egioration of the plumage, consid- lack/lus’tér, lack’lus’tre, n. absence of the United States. - | SRS eee brightness; dullness. (Rare. lacrosse’ stick, the | Oh Rogi Be manes: a complex of tores K lac'moid,n [lacmusand-oid. aviolet-bluedye. ` packet used in playing H la FSC OAs AO a fat they e o lac/mus, n. (D. lakmoes, lacmus; lak, lac, and the gamc of lacrosse. separated without breaking, although no two tac ’ s 1 Ki ser are interlinked moes, pulp.) same as litmus. > ae lac/ry DAL e e A ĵ : a-:cin’La, n- pl. la-cin/i-ae, [L., the lappet or La-cO/ni-an, a. [L. Laconia, Laconia, sparta, = same as : as lachrymalory. | ; aan ofa are zt re from Laco (-onis); Gr. Lak6n, a Spartan.) of lac/ry-mar-y, 2 and 1 Seon as lachy- | > 1. in botany, one of the straps or tags form- or pertaining to Laconia in ancient Greece. Jac/ry-ma-to-ry, n. and 4. Y : ing the fringe on the outer portion of tps or to its inhabitants; Spartan; Lacedaemon- eas scratch GENESIO i $ lade of the petals of certain flowers; also, _ ian. > : 4 c/ry: , a. Sa a fi z chest Bye tions making this fringe. La-co/ni-in, n. a native or inhabitant of La- Jact-, same as laclo-. damino.] any of a group f- 2. in entomology, the blade or apex of the conia; a Spartan; a Lacedaemonian. lac/tam, 2. Hadons dS containing m 1 z ate ject Ee ae CEE Oe EREN an oN CO Sip the ring, formed by ti | | la-cin’i-a a-cin/iat-ed, a. [L. lacinia, a taining to Laconia, Laconian, from Lakōn, an -Nt -uv om ihe amino ane m : cen eee ; l inhabitant of Laconia, a Laconian or Spartan. ] elimination of EN oO anhydride of # g 1. adorned with fringes; fringed. 1. same as Laconian. [Rare.] eee aie carboxy eroan ; 5 ei la 2. cut deeply into narrow, jagged seg- 2. [l-] short; brief; pithy; sententious; ex- amino aoga i ee i amide.) ac | ments: said of leaves, petals, bracts, etc. pressing mu in few words Prier me man lac, nm HS nE HNO: R la ini e Laconians; as, Ris p f 3 menr ees fel eaa a hem, and forma, a S pithy, short, brief, curt, epi- Jac/tint, a. m dactans Cry oes ie lactis: f + yö A ammatic, terse. to contain milk, to £ ~ {Rare}. nyo lae, (dim. of onic n. 1.laconism; a brief, pithy mode milk.) suckling; giving suck [Preparation ; of expression. Ra f l aa lac/ta-réne, Hae taine -calico printini la 2. a brief, pithy expression; a laconism: casein or milk ; ee „used chiefly in the plural; as, he spoke in cet the colors. aati : 4 pLose g came as laciale i, O oe lac/ta-ry, 2. A Tactáries, a dairy: ym la cin'ū-lá, 7.; pl. la-cin’u-lae, (dim. from L. 3. a laconic person. | lac’ta-ry, .; pl. lac a diastase.) an. eny es E cinia, a flap, hem.] in botany, (a) a minute 44.con/i-ca, n. pl. of laconicum. Jac/tase, 2. [laci- and G pdin the intr cose i (b) the abruptly inflexed acumen or j4 Con/i-cil-ly, adv. in a laconic manner; “present in certain yeasts anc ose into & nt of each of the petals of an umbelliferous briefly: con cisely: eee nimals, which splits la ; üla i i i a-con/i-cism, n. same as laconism. and galactose. 5 la Besar a: cn botany. (@) pa ving E SA n.; pl. la-con/i-ca, [L.] in an- lac/tate, v.1.; loota tea ey pp con! 5i jo ing la Paernas DE peeso cient Rome, a vapor bath; a chamber either [L: lagali: ER r oe dis, milk.] us = Pee 3 i te ve suck, aC; ME. lak, lac. pereant compan D. ni a bathing cevahishuent or separate, hea givest secrete mill, sae ing. defective. ON else fare ERA z e young. . ilk; poe not having lac/O-nism, n. [Gr. Lakénismos, the imitation nee puck ae convert into m i 3 y. of the Lacedaemonians or Spartans in man- lac RNE (Rare.] sae read wale: Í not having any; ners, dress, etc., from Lak6nizein, to imitate _ milklike. fac, lactis, milk: a t ' the Lacedaemonians, to speak laconically, to lactate n tic acid f milk i Ia 3. the thins d. laconize.]
105526:laq/uay (lak’é), n. a lackey. [Obs.]
```


## [2026-10-15T02:45:12.832Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -50"
}
```


### [2026-10-15T02:45:13.160Z] TOOL RESULT

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


## [2026-10-15T02:45:16.542Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://www.etymonline.com/word/lackey\" \"https://en.wiktionary.org/wiki/lackey\" \"https://en.wiktionary.org/wiki/laquais\" \"https://en.wiktionary.org/wiki/lacayo\" \"https://en.wiktionary.org/wiki/lacchè\" \"https://en.wiktionary.org/wiki/الاغ\" \"https://en.wiktionary.org/wiki/ulak\" \"https://www.nisanyansozluk.com/kelime/ulak\" \"https://en.wiktionary.org/wiki/uterus\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/udéros\" \"https://www.etymonline.com/word/uterus\" \"https://en.wiktionary.org/wiki/udara\"; do python3 tools/fetch_source.py \"$u\" --note \"page 517 lookup\" ; done"
}
```


### [2026-10-15T02:45:24.430Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3e57570338f41c6c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/88f65022abc1f92b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cd7d497ef8ddc70d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/34c44f1071b8697f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/25e70a618a71bfb2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/efc85a25804d619f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8cd399cfbc20568b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b1e71d556641d496.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9599f908e7f3eb61.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5b0cfc1edcfd50ae.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c0328894477fcf9f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/789bcfface76f80d.txt
```


## [2026-10-15T02:45:27.708Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -12 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin: d=json.loads(l); print(d['status'],d['bytes'],d['url'])\"; for f in 3e57570338f41c6c 88f65022abc1f92b cd7d497ef8ddc70d 34c44f1071b8697f 25e70a618a71bfb2; do echo \"=== $f\"; grep -i -A6 'Etymology' $f.txt | head -14; done; grep -i -B2 -A5 'lackey (n' 3e57570338f41c6c.txt | head -20"
}
```


### [2026-10-15T02:45:28.218Z] TOOL RESULT

```
200 6656 https://en.wiktionary.org/wiki/त्वष्टृ
200 3747 https://en.wiktionary.org/wiki/sarcasmus
200 3001 https://en.wiktionary.org/wiki/lacayo
200 5468 https://en.wiktionary.org/wiki/sarcasme
200 2369 https://en.wiktionary.org/wiki/lacchè
200 3825 https://en.wiktionary.org/wiki/الاغ
200 6088 https://en.wiktionary.org/wiki/ulak
200 219 https://www.nisanyansozluk.com/kelime/ulak
200 15005 https://en.wiktionary.org/wiki/uterus
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/udéros
-1 39 https://www.etymonline.com/word/uterus
200 8582 https://en.wiktionary.org/wiki/udara
=== 3e57570338f41c6c
=== 88f65022abc1f92b
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 
--
 Etymology
 [ edit ] 

 Borrowed from Middle French laquais , which is probably (via Old Occitan lacai ?) from Spanish lacayo , itself perhaps from Italian lacchè and Greek λακές ( lakés ) , from Turkish ulak . Another possibility is through French , from Arabic الْقَائِد ( al-qāʔid ) . See French laquais .

 Pronunciation
=== cd7d497ef8ddc70d
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 
--
 Etymology
 [ edit ] 

 Uncertain. Compare English lackey .

 Pronunciation
=== 34c44f1071b8697f
=== 25e70a618a71bfb2
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 
--
 Etymology
 [ edit ] 

 From French laquais .

 Pronunciation
```


## [2026-10-15T02:45:32.042Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -c . 3e57570338f41c6c.txt; grep -i -m3 -A3 'laquais' 3e57570338f41c6c.txt | head -12; for f in 34c44f1071b8697f efc85a25804d619f 8cd399cfbc20568b b1e71d556641d496 9599f908e7f3eb61 789bcfface76f80d; do echo \"=== $f\"; grep -A4 '^ *Etymology *$\\|Etymology [0-9]' $f.txt | grep -v '^\\s*$' | head -16; done"
}
```


### [2026-10-15T02:45:32.660Z] TOOL RESULT

```
5
=== 34c44f1071b8697f
=== efc85a25804d619f
 Etymology 
 1.3 
 Pronunciation 
--
 Etymology
 [ edit ] 
 From Turkic . Compare Azerbaijani ulaq , Chagatai اولاغ ( ulaǧ ) , Uyghur ئۇلاغ ( ulagh ) , ئۇلاق ( ulaq ) , Uzbek uloq , ulov , Ottoman Turkish اولاق ( ulak ) , Turkmen ulag .
=== 8cd399cfbc20568b
 Etymology 
 1.2 
 Pronunciation 
--
 Etymology 
 2.2 
 Noun 
--
 Etymology
 [ edit ] 
 From Western Proto-Malayo-Polynesian *ulak .
--
 Etymology
 [ edit ] 
 From Ottoman Turkish اولاق ( ulak ) , analyzable as ula- +‎ -k . Ultimately from Proto-Turkic *ula- ( “ to attach, join (ends) ” ) .
=== b1e71d556641d496
=== 9599f908e7f3eb61
 Etymology 
 1.2 
 Pronunciation 
--
 Etymology 
 2.3 
 Pronunciation 
--
 Etymology 
 3.2 
 Pronunciation 
--
 Etymology 
 4.3 
 Pronunciation 
--
=== 789bcfface76f80d
 Etymology 1 
 1.1.1 
 Noun 
--
 Etymology 2 
 1.2.1 
 Noun 
--
 Etymology 
 2.2 
 Pronunciation 
--
 Etymology 
 3.2 
 Pronunciation 
--
```


## [2026-10-15T02:45:35.466Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; cat 3e57570338f41c6c.txt; echo; sed -n 1,200p 34c44f1071b8697f.txt | grep -v '^\\s*$' | sed -n 20,60p; echo ====; grep -v '^\\s*$' efc85a25804d619f.txt | sed -n 15,50p"
}
```


### [2026-10-15T02:45:35.870Z] TOOL RESULT

```
Exit code 1
URL: https://www.etymonline.com/word/lackey
FETCHED: 2026-10-15T02:45:17Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
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
 Spanish 
 Toggle Spanish subsection 
 1.1 
 Pronunciation 
 1.2 
 Noun 
 1.2.1 
 Descendants 
 1.3 
 Further reading 
 Toggle the table of contents 
 lacayo 
 9 languages 
 Български 
 Español 
 Suomi 
 Français 
 Ido 
 Malagasy 
 Polski 
 Svenska 
 中文 
 Entry 
 Discussion 
 English 
(eval):1: === not found
```


## [2026-10-15T02:45:38.402Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' efc85a25804d619f.txt | sed -n 20,60p; echo; grep -v '^\\s*$' 8cd399cfbc20568b.txt | grep -n -A12 'Ottoman Turkish اولاق' | head -30"
}
```


### [2026-10-15T02:45:38.785Z] TOOL RESULT

```
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
 Alternative forms 
 1.2 
 Etymology 
 1.3 
 Pronunciation 
 1.4 
 Noun 
 Toggle the table of contents 
 الاغ 
 12 languages 
 Zazaki 
 فارسی 
 Hrvatski 
 Magyar 
 Bahasa Indonesia 
 한국어 
 Kurdî 
 Lietuvių 
 Malagasy 
 Polski 
 Română 
 Русский 

137: From Ottoman Turkish اولاق ( ulak ) , analyzable as ula- +‎ -k . Ultimately from Proto-Turkic *ula- ( “ to attach, join (ends) ” ) .
138- Noun
139- [ edit ] 
140- ulak 
141- courier 
142- Declension
143- [ edit ] 
144- Declension of ulak 
145- singular
146- plural
147- nominative
148- ulak 
149- ulaklar
```


## [2026-10-15T02:45:41.071Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' efc85a25804d619f.txt | sed -n 60,100p; grep -v '^\\s*$' 9599f908e7f3eb61.txt | grep -n -i -A3 'Latin' | grep -i -A3 'etymology\\|from' | head -20"
}
```


### [2026-10-15T02:45:41.762Z] TOOL RESULT

```
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
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: الاغ 
 Wikipedia fa 
 یک الاغ 
 Alternative forms
 [ edit ] 
 الاق ( ulāq  / olâġ ) , اولاغ ( ūlāġ  / ulâġ ) , اولاق ( ūlāq  / ulâġ ) , اولاو ( ūlāw  / ulâv ) 
 الو ( ulaw ) ( Tajik ) 
228: Learned borrowing from Latin uterus .
229- Pronunciation
230- [ edit ] 
231- IPA ( key ) : /ˈjuː.tə.ɹəs/ 
--
289: Borrowed from English uterus , from Latin uterus .
290- Pronunciation
291- [ edit ] 
292- IPA ( key ) : [ˈutɛrus] 
--
335: Learned borrowing from Latin uterus , from Proto-Indo-European *úderos ( “ abdomen, stomach ” ) , from *úd ( “ out, outward ” ) +‎ *-eros ( contrastive suffix ) .
336- Pronunciation
337- [ edit ] 
338- IPA ( key ) : [ˈʊtɛrʊs] 
--
431- Etymology
--
433: From Latin uterus ( “ womb, belly ” ) .
434- Pronunciation
435- [ edit ]
```


## [2026-10-15T02:45:43.963Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' efc85a25804d619f.txt | sed -n 100,125p; grep -v '^\\s*$' 9599f908e7f3eb61.txt | grep -n -B2 -A6 '^ *Latin *$' | head -30; grep -v '^\\s*$' 789bcfface76f80d.txt | grep -n -i -A3 'avestan\\|Sanskrit\\|udara ' | head -30"
}
```


### [2026-10-15T02:45:44.560Z] TOOL RESULT

```
 الو ( ulaw ) ( Tajik ) 
 Etymology
 [ edit ] 
 From Turkic . Compare Azerbaijani ulaq , Chagatai اولاغ ( ulaǧ ) , Uyghur ئۇلاغ ( ulagh ) , ئۇلاق ( ulaq ) , Uzbek uloq , ulov , Ottoman Turkish اولاق ( ulak ) , Turkmen ulag .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ʔu.ˈlaːɣ/ 
 ( Dari, formal ) IPA ( key ) : [ʔʊ.lɑːɣ] 
 ( Dari, formal ) IPA ( key ) : [ʔʊ.lɑːɣ] 
 ( Kabuli ) IPA ( key ) : [ʔʊ.lɑːɣ] 
 ( Hazaragi ) IPA ( key ) : [ʔu.lɔːɣ] 
 ( Iran, formal ) IPA ( key ) : [ʔo.lɒːɢ̥] 
 ( Tajik, formal ) IPA ( key ) : [ʔu.lɔʁ] 
 Rhymes: -aːɣ 
 Readings
 Classical reading ? 
 ulāġ
 Dari reading ? 
 ulāġ
 Iranian reading ? 
 olâġ
 Tajik reading ? 
 uloġ
 Noun
 [ edit ] 
 الاغ • ( ulāġ / olâġ ) ( Tajik spelling улоғ ) 
87- Further reading 
88- 4 
89: Latin 
90- Toggle Latin subsection 
91- 4.1 
92- Alternative forms 
93- 4.2 
94- Etymology 
95- 4.3 
--
353- [ edit ] 
354- “ uterus ”, in Kamus Besar Bahasa Indonesia [ Great Dictionary of the Indonesian Language ] (in Indonesian), Jakarta: Agency for Language Development and Cultivation – Ministry of Education, Culture, Research, and Technology of the Republic of Indonesia , 2016 
355: Latin
356- [ edit ] 
357- Latin Wikipedia has an article on: uterus 
358- Wikipedia la 
359- Alternative forms
360- [ edit ] 
361- uterum 
4:TITLE: udara - Wiktionary, the free dictionary
5:udara - Wiktionary, the free dictionary 
6- Jump to content 
7- Main menu 
8- Main menu
--
110: udara 
111- 30 languages 
112- Azərbaycanca 
113- Banjar 
--
179: udara   inan 
180- ( chiefly Gipuzkoan ) summer 
181- Synonym: uda 
182- Declension
--
184: Declension of udara (inan a-stem) 
185- indefinite
186- singular
187- plural
--
190: udara 
191: udara 
192- udarak 
193- udarok 
194- ergative
--
276: seasons : urtaroa : udaberri · uda ~ udara · udazken · negu  [ edit ] 
277- Etymology 2
278- [ edit ]
```


## [2026-10-15T02:45:47.304Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' efc85a25804d619f.txt | sed -n 125,140p; grep -v '^\\s*$' 9599f908e7f3eb61.txt | sed -n 362,372p; cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/उदर\" --note \"page 517 Udero: Sanskrit udara cognate\"; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/úderos\" --note \"page 517 Udero root\""
}
```


### [2026-10-15T02:45:49.878Z] TOOL RESULT

```
 الاغ • ( ulāġ / olâġ ) ( Tajik spelling улоғ ) 
 ( Iran ) donkey , ass 
 Synonyms: خر ( xar ) , درازگوش ( darāz-gōš  / derâz-guš ) 
 1871 , Niaz-Muhammad ibn Ashur-Muhammad Khoqandi, Tarikh-i Shahrukhi ‎ [1] , page 216 : در آنجا نیز یک هفته مکث نموده، به پیاده‌های قوشین اسب و اولاو داده، و آزوق و اسباب و انجام و سرانجام قوشین را درستی نمودند. dar ānjā nīz yak hafta maks numūda, ba piyāda-hā-yi qōšīn asb u ūlāw dāda, wa āzūq u asbāb u anjām u sar-anjām-i qōšīn rā durustī numūdand. There he bivouacked for one week, gave the army's infantrymen horses and donkeys , and replenished the army's provisions and equipment. 
 ( obsolete ) courier , messenger 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=الاغ&oldid=89639717 "
 Categories : Persian terms derived from Turkic languages 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/aːɣ 
 Rhymes:Persian/aːɣ/2 syllables 
 Persian lemmas 
 Persian nouns 
 Iranian Persian 
 Persian terms with quotations 
 Persian terms with obsolete senses 
 fa:Equids 
 Etymology
 [ edit ] 
 From Proto-Indo-European *úderos ( “ abdomen, stomach ” ) , from *úd ( “ out, outward ” ) +‎ *-eros ( contrastive suffix ) . [ 1 ] [ 2 ] 
 Pronunciation
 [ edit ] 
 ( Classical Latin ) IPA ( key ) : [ˈʊ.tɛ.rʊs] 
 ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈuː.te.rus] 
 Noun
 [ edit ] 
 uterus   m ( genitive uterī ) ; second declension 
 ( anatomy ) womb , uterus 
/home/sfmqrb/git/rishe-private/data/verification/sources/web/df07bd08d2dd76a8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/db1182bb4cbdb67b.txt
```


## [2026-10-15T02:45:52.613Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; head -3 df07bd08d2dd76a8.txt db1182bb4cbdb67b.txt | grep STATUS; grep -v '^\\s*$' db1182bb4cbdb67b.txt | grep -n -i -E 'avestan|latin|reconstruction|úderos|Etymology' -A2 | head -40; grep -v '^\\s*$' df07bd08d2dd76a8.txt | grep -n -A3 'Etymology$\\|Etymology *$' | head"
}
```


### [2026-10-15T02:45:53.189Z] TOOL RESULT

```
STATUS: 200
STATUS: 200
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/úderos
2-FETCHED: 2026-10-15T02:45:49Z
3-STATUS: 200
4:TITLE: Reconstruction:Proto-Indo-European/úderos - Wiktionary, the free dictionary
5:Reconstruction:Proto-Indo-European/úderos - Wiktionary, the free dictionary 
6- Jump to content 
7- Main menu 
--
39: Etymology 
40- 1.2 
41- Noun 
--
49: Reconstruction:Proto-Indo-European/ úderos 
50- Add languages 
51: Reconstruction 
52- Discussion 
53- English 
--
83: Etymology
84- [ edit ] 
85- Deadjectival form of *úd-er-o-s , variant of *údteros ( “ higher, outer ” ) , from *úd ( “ out, outward ” ) +‎ *-teros ( contrastive suffix ) .
--
88: *úderos   m ( non-ablauting ) [ 1 ] [ 2 ] 
89- abdomen , stomach 
90- Inflection
--
95: *úderos 
96- genitive
97: *úderosyo 
98- singular
99- dual
--
102: *úderos 
103- *úderoh₁ 
104- *úderoes 
--
114: *úderosyo 
115- *? 
116- *úderoHom 
--
39: Etymology 
40- 1.2 
41- Pronunciation 
42- 1.3 
--
52: Etymology 
53- 2.2 
54- Pronunciation 
55- 2.3 
--
```


## [2026-10-15T02:45:55.072Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' db1182bb4cbdb67b.txt | sed -n 130,175p; grep -v '^\\s*$' df07bd08d2dd76a8.txt | grep -n -A4 'Proto-Indo-European\\|Avestan' | head -20"
}
```


### [2026-10-15T02:45:55.480Z] TOOL RESULT

```
 *úderoh₁ 
 *? 
 *úderōys 
 Descendants
 [ edit ] 
 Proto-Balto-Slavic: *wēˀdera ( “ belly, stomach ” ) [ 3 ] ( < Winter's law < *udera ) ( see there for further descendants )
 Proto-Hellenic: 
 Ancient Greek: ὕδερος ( húderos ) , ( Hesychius ) ὅδερος ( hóderos , “ dropsy ” ) 
 Proto-Indo-Iranian: *udáras ( “ belly, abdomen, stomach ” ) ( see there for further descendants )
 Proto-Italic: *uderos [ 4 ] 
 Latin: uterus ( “ womb, uterus, belly ” ) ( see there for further descendants )
 References
 [ edit ] 
 ^ Mallory, J. P. with Adams, D. Q. ( 2006 ), “*udero-”, in The Oxford Introduction to Proto-Indo-European and the Proto-Indo-European World (Oxford Linguistics), New York: Oxford University Press, →ISBN , page 517 
 ^ Pokorny, Julius ( 1959 ), “ udero-, u̯ēdero- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 1, Bern, München: Francke Verlag, page 3 
 ^ Derksen, Rick ( 2015 ), “vėdaras”, in Etymological Dictionary of the Baltic Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 13 ), Leiden, Boston: Brill, →ISBN , page 494 
 ^ De Vaan, Michiel ( 2008 ), “ uterus ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 647 : “ *(H)ud-ér-o- ” 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/úderos&oldid=92171720 "
 Categories : Proto-Indo-European terms suffixed with *-teros 
 Proto-Indo-European terms belonging to the word *úd 
 Proto-Indo-European lemmas 
 Proto-Indo-European nouns 
 Proto-Indo-European masculine nouns 
 ine-pro:Anatomy 
 ine-pro:Organs 
 Proto-Indo-European thematic o-stem nouns 
 Hidden categories: Pages with etymon 
 Proto-Indo-European entries with etymon 
 Pages using etymon with no ID 
 Pages with entries 
 Pages with 1 entry 
 This page was last edited on 24 August 2026, at 00:44.
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
 Reconstruction:Proto-Indo-European/ úderos 
376: From Proto-Indo-Aryan *udáram , from Proto-Indo-Iranian *udáras , from Proto-Indo-European *úderos ( “ belly ” ) . Cognate with Avestan 𐬎𐬛𐬀𐬭𐬋𐬚𐬭𐬄𐬯𐬀 ( udarōθrąsa , “ snake creeping on the belly ” ) , Latin uterus .
377- Pronunciation
378- [ edit ] 
379- ( Vedic ) IPA ( key ) : /u.dɐ́.ɾɐ/ 
380- ( Classical Sanskrit ) IPA ( key ) : /u.d̪ɐ.ɾɐ/ 
--
470: Sanskrit terms inherited from Proto-Indo-European 
471: Sanskrit terms derived from Proto-Indo-European 
472- Sanskrit terms with IPA pronunciation 
473- Sanskrit lemmas 
474- Sanskrit nouns 
475- Sanskrit nouns in Devanagari script
```


## [2026-10-15T02:45:59.808Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:157 2>&1 | head -60"
}
```


### [2026-10-15T02:46:00.550Z] TOOL RESULT

```
no scan of BQT covers printed page 157 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:46:02.698Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(d['BQT'].get('page_offset'));print(d['BQT'].get('lookup_hint'))\"; grep -n 'pdf page' BQT_v1_pages.txt | head -3; grep -n -E 'الاغ|اولاغ|الاق' BQT_v1_pages.txt BQT_v1.txt | head"
}
```


### [2026-10-15T02:46:03.194Z] TOOL RESULT

```
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
BQT_v1_pages.txt:1467:0- احسن التقاسیم فی‌ممرفةالاقاليم. چاپ‌دوم مطبعةٌ بربلصسع۳۹۳-۳۳. ۲-مردم خراان
BQT_v1_pages.txt:2336:۰ ۷ قراث‌الاغات از »حمد نیات-
BQT_v1_pages.txt:2496:فاضل دهلوی . ۱ -- مز یل الاغلاط .
BQT_v1_pages.txt:4006:والاقطار تالف شریف ادریس. ‏ ۳۱ نشق الازهار فی‌عجائب الاقطار.
BQT_v1_pages.txt:4209:۴-ا<سن‌التقاسیم فی‌معر فةالاقاليم مقدسی(شمس الدینابو عبدافه
BQT_v1_pages.txt:13541:الاغ - بنم اول بر وزن چلاغ » فاصد
BQT_v1_pages.txt:13756:باشد - و بسکون انی خرالاغ راگویند ۱ .*
BQT_v1_pages.txt:22495:اقة عربی‌ویدرش دو کوهان‌باشد. وکرة خرالاغ‌را
BQT_v1_pages.txt:22498:خر الاغ و مادبان بهم میرسد. گویند از جمله
BQT_v1_pages.txt:25990:بين پشت‌ستود و تنگک بار گذارند وپالان الاغ‌را
```


## [2026-10-15T02:46:04.995Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n=NR-1} index($0,\"الاغ - بنم اول\"){print \"LEAF\",n; print}' BQT_v1_pages.txt | head -120"
}
```


### [2026-10-15T02:46:05.669Z] TOOL RESULT

```
LEAF 375
- ٩ پاي‎ --
الاطینی « باطای‌حطی بر وژن‌قباچینی»
بافت رومی ٩‏ کیاهی است که بر درختها پیچد
ی ای ای
همان است
الاغ - بنم اول بر وزن چلاغ » فاصد
و دك را کوبند - واسب ی که در راهها مجهت
قاصدان گذارند - و بیکار و بزورکارفرمودنرا نیز
کوبند » و بجای غين قاف هم درست است ۴ :
الام - بر وزن علام » پیقام و نوشته را
کوند که زبان بزبان و دست بدست برسانند-
و پیفام رساننده را تیز گفته‌اند؛ وتکرار الام نز
حسن هی دارد ۰
الان « بفتح اولبروزن کلان . تامولابنی
است ازتر کستان, بعضی کونند نام شهری است ۴
و نام کوهی هم هست در عرفات .
الاثبون » بک نون و تحتانی مضموم
بواو و نون دمگر زده » بلفت بوانی * راسن را
کگونند . و ان‌نوعی از فملگوش است. ه بیغ ترا
مرباکنند و آنر! زنجبیل شامی خوانند . نافع
سم دردها و المهاست که از سردی باشد ۰
و بجای نحتائی بای ابجد هم بنظر آمدة است .
زده » اش شمله ناك را کوننه ۵ .
الب - بضم اول وسکون انی و بای ایجد
کی باق برس وا کزند و آن 2
(۱) چك : ژند. و باژند .
۱ - بیونابی 6120106 «انشنگای» .
لد کز
و جگر فیمه کشیده دز ووغن بریان کرده ,اد ۰
و حسرءالملوك همان است - وبفتح تم اول بلغت‌زند
وپازند (۱) بسحتی شیرباشد که عربان لب کویشد
بجای بای ابجد بای حطی هم آعده است
ابا ك - بکر اولبروزن دلشاد, پنبه زن
و حلاح را کوینه «#
الير ۱ بفتح اول و ضم ثالث‌و
ثانی و رای بی نقطه و زای نقطهدار » نام کوهی
است مشهور » مبان ابران وهندوستان ۷ - ونام
بهلوانی حم‌بوده ات ات و کنانه آزمردم بلندقامت
و دلاور باشد .
الچ س بنتم اول و سکون ثانی و جیم ,
مردم صاحب غرور وهتکر را کویند ‏ وخرامیدن
بناز و تنمم را نز گفته‌اند .
الجخت « بفتح اول وجیم فارسی‌بروزن
بدبخت » بمعنی طمع وحاجت‌و امید وچشمداشت
الچیچكگ - بنتح اود و سکون تلی
و جیم فارسی اول بتحتانی رسیده و جیم فارسی
دوم مفتوح بکاف زده » نام بادشاه‌زاده‌ای موده‌است
از ترك .
لد کز 3 بکمراودو دال آبسدوکاف
فارسی و سکون انی و زای هوز » نام پادشاهی
موده است از ترك ۸
۳ هك اولاق؛ ی کی بمحنی کار می‌هر د»
- بونانی 6160108 «اشتینگای»
0 الب ار سلان
```


## [2026-10-15T02:46:11.360Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *الاغ|الاغ \\(|اولاغ' MON_part1.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt | head; grep -n -E 'الاغ|اولاغ|ulagh|ulāɣ|ulaq' HRN.txt HUB.txt incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-10-15T02:46:11.851Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v1_djvu.txt:15959:الاع: [ئسنر. - اولاغ - اولاق - 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:54176:الاغ» ج. حمیر؛ حمور؛ حمر. حمار اهلی: 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:55834:الاغ. آنکه الاغ را کرایه دهد ج. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:95591:الاغ. 
MON_part1.txt:15959:الاع: [ئسنر. - اولاغ - اولاق - 
MON_part1.txt:54176:الاغ» ج. حمیر؛ حمور؛ حمر. حمار اهلی: 
MON_part1.txt:55834:الاغ. آنکه الاغ را کرایه دهد ج. 
MON_part1.txt:95591:الاغ.
```


## [2026-10-15T02:46:13.821Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 15955,15975p MON_part1.txt; cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py \"https://vajehyab.com/moein/الاغ\" --note \"page 517 Ul root: Mo'in s.v. olagh\"; "
}
```


### [2026-10-15T02:46:14.675Z] TOOL RESULT

```
الاخو ن و و لاخو ل: «تاهاددم ماه 
(ص مر .( (عم. .( سرگردان. 

الاع: [ئسنر. - اولاغ - اولاق - 
کاربی مزد» اسب بیکك کشتی کوچکد.» 
قاصد ] .( (حاد.) خر بیکك» چابار» بست. 
حقوق و عوارضی که برای پیک‌ها یا 
چارپایان متعلق به پیک‌ها می‌گرفتند 
(ابلخانان مخول ئ قاجار به) 

الام: ده [تر. مک ] () راهنمایی که مجور 
نود به ما مور دیوان به رایگان خدمت کند. 
پیغام و نوشته‌ای که به زبان و دست ند ست 
ر سانند. (رص.) پغام رساننده. 

الامانچی: آ*-«قسقاه زتر. - المانچی - 


المانچی] (ص‌نسب.) غارتگر. 

/home/sfmqrb/git/rishe-private/data/verification/sources/web/5f2b3fd66c9be6a2.txt
```


## [2026-10-15T02:46:16.417Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; head -4 5f2b3fd66c9be6a2.txt; grep -n -m5 -A3 'تر\\.' 5f2b3fd66c9be6a2.txt | head -20"
}
```


### [2026-10-15T02:46:16.970Z] TOOL RESULT

```
URL: https://vajehyab.com/moein/الاغ
FETCHED: 2026-10-15T02:46:14Z
STATUS: 200
TITLE: معنی الاغ | فرهنگ انتشارات معین | واژه یاب
17: ( اُ ) [ تر. ] = اولاغ . اولاق : (اِ.) 1 - خر. 2 - (عا.) نفهم ، احمق (نوعی دشنام ). 
18- الاغ در فرهنگ‌های دیگر
19- معنی الاغ در لغت‌نامه دهخدا 
20- معنی الاغ در فرهنگ فارسی عمید / قربان‌زاده
```


## [2026-10-15T02:46:35.098Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 517 -l 517 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg517 && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg517.png');w,h=im.size;print(w,h)\nim.crop((int(w*0.2),int(h*0.45),int(w*0.8),int(h*0.55))).save('$S/pg517crop.png')\"; mkdir -p data/verification/sources/refs/ocr/BOOK; cp $S/pg517.png data/verification/sources/refs/ocr/BOOK/517.png"
}
```


## [2026-10-15T02:46:35.955Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg517crop.png"
}
```


### [2026-10-15T02:46:37.233Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'
```


### [2026-10-15T02:46:37.267Z] TOOL RESULT

```
File does not exist. Note: your current working directory is /home/sfmqrb/git/rishe-private.
```


## [2026-10-15T02:46:40.350Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 517 -l 517 -r 300 -x 1100 -y 1950 -W 1500 -H 450 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg517crop; mkdir -p data/verification/sources/refs/ocr/BOOK; cp $S/pg517.png data/verification/sources/refs/ocr/BOOK/517.png; ls $S"
}
```


## [2026-10-15T02:46:41.232Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg517crop.png"
}
```


### [2026-10-15T02:46:41.555Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:46  bqt500
drwxr-xr-x     - sfmqrb 14 Oct 22:29  dl499
drwxr-xr-x     - sfmqrb 14 Oct 22:46  dl512
drwxr-xr-x     - sfmqrb 14 Oct 22:45  dl518
drwxr-xr-x     - sfmqrb 14 Oct 22:45  p509
drwxr-xr-x     - sfmqrb 14 Oct 22:25  tb
.rw-r--r--   440 sfmqrb 14 Oct 22:44  agents.txt
.rw-r--r--   68k sfmqrb 14 Oct 22:45  bqt511-139.png
.rw-r--r--   44k sfmqrb 14 Oct 22:33  gen-499.py
.rw-r--r--   115 sfmqrb 14 Oct 22:34  msg-499.txt
.rw-r--r--   57k sfmqrb 14 Oct 22:26  pg499.png
.rw-r--r--   82k sfmqrb 14 Oct 22:44  pg502.png
.rw-r--r--   74k sfmqrb 14 Oct 22:44  pg506.png
.rw-r--r--   86k sfmqrb 14 Oct 22:44  pg507.png
.rw-r--r--   82k sfmqrb 14 Oct 22:44  pg511.png
.rw-r--r--   59k sfmqrb 14 Oct 22:44  pg512.png
.rw-r--r--   76k sfmqrb 14 Oct 22:44  pg513.png
.rw-r--r--   72k sfmqrb 14 Oct 22:44  pg516.png
.rw-r--r--   60k sfmqrb 14 Oct 22:46  pg517.png
.rw-r--r--  3.0k sfmqrb 14 Oct 22:46  pg517crop.png
```


### [2026-10-15T02:46:41.581Z] TOOL RESULT

```

```


## [2026-10-15T02:46:45.579Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; file $S/pg517.png; pdftoppm -f 517 -l 517 -r 300 -x 1250 -y 1600 -W 800 -H 200 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg517crop"
}
```


## [2026-10-15T02:46:46.067Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg517crop.png"
}
```


### [2026-10-15T02:46:46.335Z] TOOL RESULT

```
/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg517.png: PNG image data, 2550 x 3300, 8-bit/color RGB, non-interlaced
```


### [2026-10-15T02:46:46.350Z] TOOL RESULT

```

```


## [2026-10-15T02:46:53.282Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -m3 '^ *uterus\\|Uterus,' SKT.txt | head; sed -n 19516,19520p IEC.txt | cut -c1-600; grep -n -i 'uterus' KLN_1966.txt | head -3"
}
```


### [2026-10-15T02:46:53.923Z] TOOL RESULT

```
equivalence of Li. tvinkseti: tunkseti ‘pulsate’; tvirsóti: tursóti "lounge"; tviróti ‘enclose’: tu- réti ‘have’. Thus also Lat. festinàre: torrens, festus, in-, mani-: re-, ob-türáre; E twitch: G zwicken, zwacken, zucken etc. sug- gest a parallel evolution of forms with and without *-u-. Cf. also Li. tvyl- :tyl- ‘quiet’
out forth”; Hitt. cf udne, udni, s. country, side’; Gk. cf. hüs-teros, adj. later; OBr. ud-, od-, verbal px.; Ir. úd, üdh, s. “beginning”; OW cf. odd-yma ‘hence’; odd-yna ‘thence’; W cf. oddi, prp. Cfrom', fr. *ud-d&); Go. üt, adv. ‘out’; üta, adv. ‘outside’; OHG us, adv. & prp. id.; OE, LG, Sw. Norw. üt, ut, id.; Du. uit, id.; ON út, adv. id. beside úti, adv. "out, side’
uderos, om ‘belly, stomach’. WP I, 190 Skt. udáram, m. ‘belly, stomach, womb’; Cy- priot óderos (‘stomach’, Cypr. -o- for Gk. -u-. WP). (Isophone: Fris. otter (2) “stack of cut peat")
udor-, see udor
udn (üd-ono) ‘out, outside’. Cf. od. ono Hitt. udne, udni, s. ‘countryside’; OE ütan(e) ‘from outside; MHG üsen, prp. & adv. out, side; ON útan, adv. ‘from outside, away’; OCS vünü, adv. and com. SL, Cz. ven, R von ‘outside, away
10500:decidua  n.,  that  part  of  the  mucous  membrane of  the  uterus,  which  is  cast  off  at  parturition (anat.)  —  Medical  L.,  short  for  membrdna decidua,  ‘the  membrane  that  falls  off’,  fern,  of L.  deciduus,  ‘falling  off’.  See  next  word.
11350:Didelphia,  n.,  the  group  of  marsupials  ( zoo! .)  — ModL.,  lit.  ‘having  a  double  uterus’,  fr.  di-  ‘two, double’,  and  Gk.  SsXtpui;,  ‘womb,  uterus’,  which is  rel.  to  aSeXipop,  ‘brother’,  lit.  ‘from  the  same womb’.  See  adelpho-  and  -ia.
16086:the  Nazis.  —  From  the  abbreviation  of  GVheime •SVaatspoli/ei,  lit.  ‘secret  state  police’, gestate,  tr.  v.,  to  carry  in  the  womb  during  preg¬ nancy.  —  L.  gestatus ,  pp.  of  gestare,  ‘to  carry, carry  about’,  intensive  of  gerere  (pp.  gestus), ‘to  carry’.  See  gerent  and  verbal  suff.  -ate. gestation,  n.,  i)  the  act  of  carrying  in  the  uterus, pregnancy;  2)  the  period  of  gestation.  —  L. gestatio,  gen.  -dnis,  ‘a  carrying  about’,  fr.  ge¬ status,  pp.  of  gestare.  See  prec.  word  and  -ion. gestatorial,  adj.,  used  for  carrying  about  (ap¬ plied  to  the  chair  in  which  the  Pope  is  carried on  certain  occasions.)  —  Formed  with  adj.  suff. -al  fr.  L.  gestatdrius,  ‘that  which  serves  for carrying’,  fr.  gestus,  pp.  of  gerere,  ‘to  carry’.  See gestate  and  adj.  suff.  -ory. gesticulate,  intr.  v.,  to  make  gestures;  tr,  v.,  to indicate  by  gesticulating.  — •  L.  gesticulatus,  pp. of  gesticulari,  ‘to  make  pantomimic  gestures’, fr.  gesticulus,  ‘gesticulation,  gesture’,  dimin.  of gestus,  ‘gesture’,  lit.  ‘carriage,  posture’,  fr.  ges¬ tus,  pp.  of  gerere,  ‘to  bear,  carry’.  See  gerent and  verbal  suff.  -ate.
```


## [2026-10-15T02:46:55.609Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *uterus,|uterus, n\\.' KLN_1966.txt | head -3; grep -n -E 'uterus' SKT.txt | head -3"
}
```


### [2026-10-15T02:46:55.911Z] TOOL RESULT

```
40935:uterus,  n.,  the  womb.  —  L.,  ‘womb’,  cogn.  with OI.  udaram,  ‘belly’.  Maced.  68epo?,  ‘belly, womb’,  Gk.  uo-rpoi ;  (Hesychius),  uoripa.
```


## [2026-10-15T02:48:31.553Z] TOOL CALL #40: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-517.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nPOKN=\"POK_full.txt line 88040 'Root / lemma: udero-, uedero- / Meaning: belly / Material: 1. Old Indie udara-m 'belly ...', Avestan udara- ... Latin uterus 'lower abdomen, belly, esp. womb, uterus' (t for d most likely together with the phonetic alteration from *udris 'hose' to *utris)'; Old Prussian weders, Lithuanian vėdaras.\"\nWLDN=\"WLD_Bd1_pages.txt line 17540ff (Bd. I pp.190-191) 'udero-, uedero- „Bauch“ ... Ai. udara-m „Bauch ...“, av. udarə.θrąsa- „auf dem Bauch kriechend, von Schlangen“ ... lat. uterus „Unterleib, Bauch, bes. Mutterleib, Gebärmutter“ (t für d am ehesten zugleich mit dem Lautwandel von *udris „Schlauch“ zu *utris eingetreten, Thurneysen KZ 32,564)'.\"\nAHDN=\"AHD_watkins1985.txt line 1103 'udero-. Abdomen, womb, stomach; with distantly similar forms (perhaps taboo deformations) ... 1. Latin uterus (reshaped from *udero-), womb: UTERUS ... [Pok. udero- 1104.]'\"\nIECN=\"IEC.txt line 19518 'uderos, om 'belly, stomach'. WP I, 190 Skt. udáram ... Cypriot óderos' (Latin not listed).\"\nBRTN=\"BRT.txt line 8213-8214 (col. 390) 'udarō.θrąsa- Adj. 'auf dem Bauch sich bewegend, kriechend', von Schlangen: azinąm ...sanąm Y.?, V.14.5 ... u. udara- n. 'Bauch'' — the simplex udara- is abstracted from the compound.\"\nKLNU=\"KLN_1966.txt line 40935 s.v. uterus: 'L., 'womb', cogn. with OI. udaram, 'belly'. Maced. (h)óderos 'belly, womb', Gk. hústros (Hesychius), hustera.'\"\nLATN=\"LAT.txt line 70687 s.v. uterus: 'On pense naturellement à skr. udaram „ventre“, gr. hóderos·gastḗr Hes., v.pruss. weders „ventre“. Mais ceci n'explique pas le t. Les mots de ce groupe ont des formes „populaires“ instables.'\"\nKLNL=\"KLN_1966.txt line 20968 s.v. lackey: 'MF. (= F.) laquais, fr. Sp. lacayo, fr. It. lacchè, fr. ModGk. οὐλάκης (read ulakis), ult. fr. Turkish ulak, 'runner, courier', from stem ul-, 'to go'.'\"\nTTSN=\"TTS_pages.txt leaf 164 (printed p.134) no. 145 'Jol, ol, ul, jor, jur, jür, gehen, schreiten, wandeln, Gang, Weg' — I. -l: uig. jol 'Weg', jolamak 'schicken'; čag. ulak 'Reitthier, Esel'; kaz. ulak 'Bote, Läufer', ulau 'Führung'; II. -r: uig. jorï- 'gehen', čag. jürümek ... — exactly Nourai's root box and ulak 'runner, messenger, donkey'.\"\nLKTN=\"LKT.txt line 4771 no. 2130 'Tk. ulak: 'Läufer, Eilbote' [vom Stamme jol, ol, ul 'gehen', Vámbéry TktEtWb S.134 Nr.145 I]; hieraus [wohl am wahrscheinlichsten über ngr. οὐλάκης MSOS II,239] frz. laquais, it. lacchè, sp. pg. lacayo 'Diener'; dtsch. Lakai. Unmittelbar wurde übernommen rum. olac 'Schnellpost''.\"\nSKTN=\"SKT.txt line 9836 s.v. lackey: 'From O.F. laquay ... There was also an O.F. form alacay; Littré shews that in the 15th cent. a certain class of soldiers (esp. crossbow-men) were called alacays or lacays ... Prob. from Span. lacayo ... Arab. lukaʿ worthless, servile ... This is a guess; it is much disputed; Diez connects it with Ital. leccare, to lick.'\"\nPHNN=\"PHN.txt line 6639 s.v. LAQUAIS: derives it from Arabic lakiyy 'attaché à quelqu'un', 'Les étymologistes sont peu d'accord sur l'origine de laquais ... a passé dans l'espagnol lacayo ... Les Italiens écrivent lacchè, et les Anglais lackey.'\"\nFSDN=\"FSD_vol2.txt line 70482-70485 s.v. lackey: '[< F. laquais, < Sp. lacayo, prob. < ...]' — French < Spanish, no Turkish/Greek link.\"\nWEBN=\"WEB_vol1.txt line 104635 s.v. lackey: '[OFr. laquay, a lackey, also a soldier; Sp. lacayo, a lackey, footman; compare Ar. lukaʿ worthless, servile, Pr. lacai, a gormand]'.\"\nBQTN=\"BQT_v1_pages.txt leaf 375 (= printed p.157): 'الاغ - بضم اول بر وزن چلاغ، قاصد و پیک را گویند - و اسبی که در راهها بجهت قاصدان گذارند - و بیگار و بزور کار فرمودن را نیز گویند، و بجای غین قاف هم درست است' with Mo'in's footnote 3 (OCR rough) 'تر. اولاق ...' — Turkish origin, senses 'courier', 'post-horse', 'corvée'; no 'donkey' sense.\"\nMONN=\"MON_part1.txt line 15959 (page not mappable to Nourai's 3334): 'الاغ [تر. - اولاغ - اولاق - ... کار بی‌مزد، اسب پیک، کشتی کوچک، قاصد] ... خر. پیک، چاپار، پست. حقوق و عوارضی که برای پیک‌ها یا چارپایان متعلق به پیک‌ها می‌گرفتند (ایلخانان مغول تا قاجاریه)'; vajehyab Mo'in: '[تر.] = اولاغ، اولاق: 1- خر. 2- (عا.) نفهم، احمق'.\"\ndef nc(r,n=\"not accessible\"): return {\"ref\":r,\"status\":\"not_checked\",\"note\":n}\nout={\"pdf_page\":517,\"book_page\":487,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-14\",\"entries\":[\n{\"entry\":0,\"root\":\"Udero, Uedero\",\"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *úderos / *udero- 'belly, abdomen' (Pokorny 1104 udero-, u̯ēdero-; de Vaan *(H)ud-ér-o-)\",\n \"note\":\"Pokorny 1104 has exactly this lemma (udero-, uedero- 'belly') with Skt. udara-, Av. udara-, Latin uterus, Baltic vėdaras; Watkins AHD udero- 'abdomen, womb, stomach'. Root, label and gloss correct. The Latin -t- (expected *uderus) is the one irregularity, explained as a 'popular' deformation (Thurneysen, Ernout-Meillet, Watkins 'reshaped').\",\n \"note_fa\":\"ریشهٔ هندواروپایی آغازین *udero- / *úderos «شکم، اندرون» در پوکورنی (ص ۱۱۰۴) و واتکینز با همین صورت و معنا آمده و از آن سنسکریت udara «شکم»، اوستایی udara- و لاتینی uterus «زهدان» برخاسته است. برخی آن را از *ud «بیرون» با پسوند مقایسه‌ای -ero- می‌دانند. تنها نکتهٔ ناهموار، t لاتینی به جای d است که آن را دگرگونی عامیانه می‌شمارند. ادعای نورایی درست است.\",\n \"sources\":[W+\"Reconstruction:Proto-Indo-European/úderos\",W+\"uterus\",W+\"उदर\"],\n \"ref_check\":[{\"ref\":\"POK:1104\",\"status\":\"supports\",\"note\":\"Pokorny IEW p.1104 (page block in \"+POKN+\")\"}],\n \"consulted\":[{\"src\":\"WLD\",\"where\":\"Bd. I pp.190-191\",\"stance\":\"supports\",\"note\":WLDN},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. udero-\",\"stance\":\"supports\",\"note\":AHDN},\n   {\"src\":\"IEC\",\"where\":\"s.v. uderos\",\"stance\":\"supports\",\"note\":IECN}],\n \"nodes\":[\n {\"id\":1,\"lang\":\"Avestan\",\"words\":\"udara\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Avestan udara- n. 'belly' continues Proto-Indo-Iranian *udáras < PIE *úderos unchanged (PIE *u, *d, *e > Iranian u, d, a). It is attested only inside the compound udarō.θrąsa- 'creeping on the belly' (epithet of snakes, Vd. 14.5); Bartholomae abstracts the simplex udara- 'Bauch' from it. Exact cognate of Sanskrit udára- 'belly'.\",\n  \"derivation_fa\":\"اوستایی udara- «شکم» بازماندهٔ هندوایرانی *udáras و هندواروپایی *úderos است و e هندواروپایی در ایرانی به a بدل شده است. این واژه تنها در ترکیب udarō.θrąsa- «بر شکم خزنده» (صفت ماران در وندیداد) آمده و بارتولومه صورت ساده را از آن بیرون کشیده است. هم‌ریشه با سنسکریت udara «شکم». ادعای نورایی درست است.\",\n  \"sources\":[W+\"उदर\",W+\"Reconstruction:Proto-Indo-European/úderos\"],\n  \"ref_check\":[{\"ref\":\"POK:1104\",\"status\":\"supports\",\"note\":\"Pokorny p.1104: 'Avestan udara- ds.' — \"+POKN}],\n  \"consulted\":[{\"src\":\"BRT\",\"where\":\"col. 390 s.v. udarō.θrąsa-\",\"stance\":\"supports\",\"note\":BRTN},\n   {\"src\":\"WLD\",\"where\":\"Bd. I p.190\",\"stance\":\"supports\",\"note\":WLDN},\n   {\"src\":\"IEC\",\"where\":\"s.v. uderos\",\"stance\":\"silent\",\"note\":\"IEC lists Skt. udáram and Cypriot óderos only; no Avestan form.\"}]},\n {\"id\":2,\"lang\":\"Latin\",\"words\":\"uterus\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Latin uterus, -ī m. (also uterum n. in Plautus) 'belly, womb' continues Proto-Italic *uderos < PIE *úderos (de Vaan: *(H)ud-ér-o-). The expected outcome is *uderus; the voiceless -t- is unexplained by regular sound law and is ascribed to a 'popular' reshaping (Ernout-Meillet), perhaps under the influence of uter, utris 'leather bag' (< *udris, Thurneysen) — Watkins: 'reshaped from *udero-'. Despite the irregularity the identification is the standard one.\",\n  \"derivation_fa\":\"لاتینی uterus «شکم، زهدان» از ایتالیک آغازین *uderos و هندواروپایی *úderos است. صورت قاعده‌مند باید *uderus می‌بود؛ t به جای d را دگرگونی عامیانه یا اثر واژهٔ uter «مشک چرمی» می‌دانند (تورنایزن، ارنو و میه). با این ناهمواری، این پیوند در پژوهش امروز پذیرفته است (پوکورنی، واتکینز، دِ واآن). ادعای نورایی درست است.\",\n  \"sources\":[W+\"uterus\",W+\"Reconstruction:Proto-Indo-European/úderos\"],\n  \"ref_check\":[{\"ref\":\"POK:1104\",\"status\":\"supports\",\"note\":POKN}],\n  \"consulted\":[{\"src\":\"WLD\",\"where\":\"Bd. I p.190\",\"stance\":\"supports\",\"note\":WLDN},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. udero-\",\"stance\":\"supports\",\"note\":AHDN},\n   {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. uterus\",\"stance\":\"partial\",\"note\":LATN},\n   {\"src\":\"KLN\",\"where\":\"1966 s.v. uterus\",\"stance\":\"supports\",\"note\":KLNU}]},\n {\"id\":3,\"lang\":\"English\",\"words\":\"uterus\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English uterus (late 14th/early 17th c. medical usage) is a learned borrowing of Latin uterus 'womb' with no change of form; it replaced native 'womb' in anatomical language.\",\n  \"derivation_fa\":\"انگلیسی uterus «زهدان» وام‌واژه‌ای دانشورانه از لاتینی uterus است که بی‌دگرگونی در زبان پزشکی به کار رفته و جای واژهٔ بومی womb را در اصطلاح کالبدشناسی گرفته است. ادعای نورایی درست است.\",\n  \"sources\":[W+\"uterus\"],\n  \"ref_check\":[nc(\"None\",\"no reference given by Nourai for this node\")],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"1966 s.v. uterus\",\"stance\":\"supports\",\"note\":KLNU},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. udero-\",\"stance\":\"supports\",\"note\":\"'Latin uterus (reshaped from *udero-), womb: UTERUS' — the English word is listed as borrowed from Latin.\"}]}]},\n{\"entry\":8,\"root\":\"Ul, Ol 2, Jol, Jor, Jur\",\"verdict\":\"disputed\",\n \"modern_form\":\"Old Turkic ulag 'relay horse, post-horse' < ula- 'to join, attach (end to end)' + -g (Wiktionary, after Clauson); not from yol 'road' / yorï- 'to walk'\",\n \"note\":\"The root box is Vámbéry's 1878 grouping (TTS p.134 no.145 'Jol, ol, ul, jor, jur, jür, gehen, schreiten'), repeated by Lokotsch and Klein ('from stem ul-, to go'). Modern Turkology separates yol 'road' and yorï- 'walk' and derives ulak/ulag from Proto-Turkic *ula- 'to join, connect' (the relay animals/couriers 'link' the stations). Nourai's citations faithfully reflect his sources, but the root is outdated.\",\n \"note_fa\":\"این ریشه گروه‌بندی وامبری (۱۸۷۸) است که jol «راه»، jor/jür «رفتن» و ul را یک ریشه به معنای «رفتن، گام برداشتن» می‌گرفت؛ لوکوچ و کلاین نیز از او پیروی کرده‌اند. ترک‌شناسی امروز yol «راه» و yorï- «رفتن» را جدا می‌داند و ulak/ulag «اسب چاپار، پیک» را از فعل ترکی آغازین *ula- «پیوستن، به هم وصل کردن» می‌گیرد. منبع‌های نورایی گفتهٔ او را تأیید می‌کنند، ولی پژوهش امروزی این ریشه را نمی‌پذیرد.\",\n \"sources\":[W+\"ulak\"],\n \"ref_check\":[{\"ref\":\"KLN:857\",\"status\":\"supports\",\"note\":KLNL},{\"ref\":\"TTS:134\",\"status\":\"supports\",\"note\":TTSN}],\n \"consulted\":[{\"src\":\"LKT\",\"where\":\"no. 2130 s.v. ulak\",\"stance\":\"supports\",\"note\":LKTN}],\n \"nodes\":[\n {\"id\":1,\"lang\":\"Turkish\",\"words\":\"ulak\",\"verdict\":\"disputed\",\n  \"derivation\":\"Turkish (Ottoman) ulak 'courier, messenger' and Chagatai/Central Asian ulag/ulaq 'riding or pack animal, post-horse, donkey' are real and well attested (Old Turkic ulag 'relay horse'; Mongolian ulaγa). The word itself is correct, but its derivation from a root 'to go' (Vámbéry's jol/ul) is disputed: Wiktionary (after Clauson) analyses ula- + -k, from Proto-Turkic *ula- 'to attach, join (ends)', i.e. the animal/man of the linked relay system (yam). The senses 'donkey' belong to the eastern (Chagatai) forms, 'courier' to Ottoman.\",\n  \"derivation_fa\":\"ترکی عثمانی ulak «پیک، چاپار» و جغتایی ulag/ulaq «چارپای سواری و باری، اسب چاپار، خر» واژه‌هایی واقعی‌اند (ترکی باستان ulag «اسب چاپارخانه»). اما پیوند آن با ریشه‌ای به معنای «رفتن» (ریشهٔ وامبری) را پژوهش امروزی نمی‌پذیرد و آن را از فعل *ula- «پیوستن، به هم وصل کردن» با پسوند -k می‌داند، یعنی چارپا یا مردی که ایستگاه‌های پیوستهٔ چاپار را به هم می‌رساند. واژه درست است، ریشه‌یابی نورایی مردود.\",\n  \"sources\":[W+\"ulak\",W+\"الاغ\"],\n  \"ref_check\":[{\"ref\":\"KLN:857\",\"status\":\"supports\",\"note\":KLNL},{\"ref\":\"TTS:134\",\"status\":\"supports\",\"note\":TTSN}],\n  \"consulted\":[{\"src\":\"LKT\",\"where\":\"no. 2130\",\"stance\":\"supports\",\"note\":LKTN},\n   {\"src\":\"TTS\",\"where\":\"p.134 no.145\",\"stance\":\"supports\",\"note\":\"čag. ulak 'Reitthier, Esel', kaz. ulak 'Bote, Läufer' listed under jol/ul 'gehen' (Vámbéry's own, now outdated, grouping).\"}]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"olâğ\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Persian الاغ ulāġ (Iranian olâġ), also written اولاغ، الاق، اولاق, is a Turkic loan entering with the Mongol/Ilkhanid relay system (yām): Borhan-e Qate' gives 'courier, post-horse kept on the roads for couriers, corvée', Mo'in adds the Ilkhanid-to-Qajar levy for couriers' animals; the modern sense 'donkey' (and colloquial 'fool') developed from 'pack/post animal'. Source is Chagatai/Eastern Turkic ulag/ulaq rather than Ottoman ulak specifically, but Nourai's arrow (Turkic ulak → Persian olâğ) is correct.\",\n  \"derivation_fa\":\"«الاغ» (ulāġ، در ایران olâġ؛ با صورت‌های اولاغ، الاق، اولاق) وام‌واژه‌ای ترکی است که با نظام چاپارخانه (یام) در روزگار مغول و ایلخانان به فارسی آمد. برهان قاطع آن را «قاصد و پیک، و اسبی که در راهها بجهت قاصدان گذارند، و بیگار» معنی کرده و معین در فرهنگ خود عوارضی را که برای چارپایان پیک می‌گرفتند (ایلخانان تا قاجاریه) یاد کرده است. معنای امروزی «خر» از «چارپای بارکش و چاپار» پدید آمده است. ادعای نورایی درست است.\",\n  \"sources\":[W+\"الاغ\",\"https://vajehyab.com/moein/الاغ\"],\n  \"ref_check\":[{\"ref\":\"BQT:157\",\"status\":\"supports\",\"note\":BQTN},{\"ref\":\"MON:3334\",\"status\":\"supports\",\"note\":MONN}],\n  \"consulted\":[{\"src\":\"HRN\",\"where\":\"grep الاغ/اولاغ/ulag\",\"stance\":\"silent\",\"note\":\"Horn (Iranian-only etymologies) has no entry; no hit for الاغ, اولاغ, ulag, ulaq in HRN.txt.\"},\n   {\"src\":\"HUB\",\"where\":\"grep\",\"stance\":\"silent\",\"note\":\"no hit for الاغ / اولاغ in HUB.txt.\"},\n   {\"src\":\"ARY\",\"where\":\"grep ARY_pages.txt\",\"stance\":\"silent\",\"note\":\"no hit for الاغ / اولاغ — expected, Aryanpur covers only Indo-European roots.\"},\n   {\"src\":\"TTS\",\"where\":\"p.134 no.145\",\"stance\":\"supports\",\"note\":\"čag. ulak 'Reitthier, Esel' — the eastern Turkic form with the 'donkey' sense that Persian shares.\"}]},\n {\"id\":3,\"lang\":\"Greek\",\"words\":\"oulakis\",\"verdict\":\"plausible\",\n  \"derivation\":\"Medieval/Modern Greek οὐλάκης (oulákēs) 'courier' is a loan from Turkish ulak (cited by Klein and by Lokotsch after MSOS II 239), with Greek -ης agent ending. The word is real; whether it is the link to Italian/Spanish lacchè/lacayo is only one hypothesis (Wiktionary s.v. lackey mentions Greek λακές lakés and Turkish ulak 'perhaps', alongside an Arabic al-qāʾid alternative).\",\n  \"derivation_fa\":\"یونانی میانه و نو οὐλάκης «پیک» وام‌واژه‌ای از ترکی ulak است با پسوند -ης. خود واژه واقعی است، اما اینکه حلقهٔ رسیدن واژه به ایتالیایی و اسپانیایی بوده باشد تنها یکی از فرضیه‌هاست (کلاین و لوکوچ آن را می‌پذیرند، ویکی‌واژه با «شاید» آورده است). با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"lackey\"],\n  \"ref_check\":[{\"ref\":\"KLN:857\",\"status\":\"supports\",\"note\":KLNL}],\n  \"consulted\":[{\"src\":\"LKT\",\"where\":\"no. 2130\",\"stance\":\"supports\",\"note\":LKTN},\n   {\"src\":\"SKT\",\"where\":\"s.v. lackey\",\"stance\":\"contradicts\",\"note\":SKTN}]},\n {\"id\":4,\"lang\":\"Italian\",\"words\":\"\",\"verdict\":\"disputed\",\n  \"derivation\":\"Empty Italian pass-through node (= lacchè, as Klein has it: 'Sp. lacayo, fr. It. lacchè'). Modern dictionaries take Italian lacchè 'footman' as a later borrowing FROM French laquais (Wiktionary lacchè: 'From French laquais'); the Italian form, with its final stress, mirrors French -ais, so it cannot be the source of 15th-c. Spanish/Catalan (a)lacayo/alacay. The step Greek → Italian → Spanish is therefore not supported.\",\n  \"derivation_fa\":\"گرهٔ تهیِ ایتالیایی (lacchè). فرهنگ‌های امروزی lacchè «پیشخدمت» را وامی متأخر از فرانسوی laquais می‌دانند (تکیهٔ پایانی آن بازتاب -ais فرانسوی است)، پس نمی‌تواند سرچشمهٔ اسپانیایی lacayo در سدهٔ پانزدهم باشد. مسیر یونانی ← ایتالیایی ← اسپانیایی که نورایی به پیروی از کلاین آورده، امروز پذیرفته نیست.\",\n  \"sources\":[W+\"lacchè\"],\n  \"ref_check\":[nc(\"None\",\"no reference given for this node; Klein s.v. lackey (KLN:857) is the source of the chain: 'fr. It. lacchè'\")],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"1966 s.v. lackey\",\"stance\":\"supports\",\"note\":KLNL},\n   {\"src\":\"LKT\",\"where\":\"no. 2130\",\"stance\":\"partial\",\"note\":\"lists 'frz. laquais, it. lacchè, sp. pg. lacayo' as parallel descendants, without making Italian the intermediary.\"},\n   {\"src\":\"PHN\",\"where\":\"s.v. LAQUAIS\",\"stance\":\"contradicts\",\"note\":PHNN}]},\n {\"id\":5,\"lang\":\"Spanish\",\"words\":\"\",\"verdict\":\"plausible\",\n  \"derivation\":\"Empty Spanish pass-through node (= lacayo, Old Spanish alacayo, Catalan alacay, 15th c., originally a kind of foot-soldier/crossbowman, then 'footman'). Spanish lacayo as the immediate source of French laquais is the common view (Klein, Funk & Wagnalls, Webster, Wiktionary); its own origin is uncertain — Turkish ulak via Greek, Arabic al-qāʾid, Arabic lukaʿ 'servile' (Skeat, Webster) and Arabic lakiyy (Pihan) have all been proposed. The arrow from Italian is not supported (see node 4).\",\n  \"derivation_fa\":\"گرهٔ تهیِ اسپانیایی (lacayo؛ اسپانیایی کهن alacayo، کاتالان alacay در سدهٔ پانزدهم، نخست گونه‌ای سرباز پیاده و کمان‌دار، سپس «پیشخدمت»). اینکه فرانسوی laquais از اسپانیایی lacayo گرفته شده، دیدگاه رایج است؛ اما ریشهٔ خود lacayo روشن نیست و جز ترکی ulak، عربی «القائد» و «لُکَع» (فرومایه) نیز پیشنهاد شده است. با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"lackey\",W+\"lacayo\"],\n  \"ref_check\":[nc(\"None\",\"no reference given for this node\")],\n  \"consulted\":[{\"src\":\"SKT\",\"where\":\"s.v. lackey\",\"stance\":\"partial\",\"note\":SKTN},\n   {\"src\":\"FSD\",\"where\":\"s.v. lackey\",\"stance\":\"supports\",\"note\":FSDN},\n   {\"src\":\"WEB\",\"where\":\"s.v. lackey\",\"stance\":\"partial\",\"note\":WEBN}]},\n {\"id\":6,\"lang\":\"French\",\"words\":\"laquis\",\"verdict\":\"transcription_suspect\",\n  \"derivation\":\"The book prints 'laquis'; this is Nourai's misprint for French laquais 'footman, lackey' (Middle French laquais, earlier alacays/lacays 15th c. for a class of foot-soldiers, Skeat after Littré). Klein, his cited source, has 'laquais'. The JSON reproduces the book faithfully. Derivation: from Spanish lacayo (possibly via Old Occitan lacai), per Wiktionary; ultimate origin uncertain (Turkish ulak hypothesis vs Arabic proposals), so the content of the arrow is only plausible.\",\n  \"derivation_fa\":\"کتاب «laquis» چاپ کرده که خطای چاپی کتاب به جای فرانسوی laquais «پیشخدمت، نوکر» است (فرانسوی میانه laquais؛ در سدهٔ پانزدهم alacays/lacays نام گونه‌ای سرباز پیاده بود). کلاین، منبع خود نورایی، laquais آورده است و استخراج داده با کتاب یکسان است. این واژه از اسپانیایی lacayo (شاید از راه پرووانسی کهن lacai) آمده و ریشهٔ دورتر آن روشن نیست.\",\n  \"error_in\":\"book\",\"book_prints\":\"laquis\",\"correct_form\":\"laquais\",\n  \"sources\":[W+\"laquais\",W+\"lackey\"],\n  \"ref_check\":[{\"ref\":\"KLN:857\",\"status\":\"supports\",\"note\":KLNL+\" — Klein spells it laquais, not laquis.\"}],\n  \"consulted\":[{\"src\":\"PHN\",\"where\":\"s.v. LAQUAIS\",\"stance\":\"contradicts\",\"note\":PHNN},\n   {\"src\":\"SKT\",\"where\":\"s.v. lackey\",\"stance\":\"partial\",\"note\":SKTN},\n   {\"src\":\"LKT\",\"where\":\"no. 2130\",\"stance\":\"supports\",\"note\":LKTN}]},\n {\"id\":7,\"lang\":\"English\",\"words\":\"lackey\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English lackey (also lacquey; 1520s 'footman, running servant', later 'servile follower') is borrowed from Middle French laquais (Old French laquay, Cotgrave), with English -ey for French -ais/-ay. The French → English step is uncontroversial; the earlier history is treated under nodes 3-6.\",\n  \"derivation_fa\":\"انگلیسی lackey (نیز lacquey، سدهٔ شانزدهم، «نوکر پیاده، پیشخدمت» و سپس «چاکر، دنباله‌رو») از فرانسوی میانه laquais (laquay) وام گرفته شده است. این گام از فرانسوی به انگلیسی بی‌گمان است؛ ریشهٔ دورتر در گره‌های پیشین بررسی شد. ادعای نورایی درست است.\",\n  \"sources\":[W+\"lackey\"],\n  \"ref_check\":[nc(\"None\",\"no reference given for this node; Klein s.v. lackey covers it: 'MF. (= F.) laquais'\")],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"1966 s.v. lackey\",\"stance\":\"supports\",\"note\":KLNL},\n   {\"src\":\"SKT\",\"where\":\"s.v. lackey\",\"stance\":\"supports\",\"note\":SKTN},\n   {\"src\":\"FSD\",\"where\":\"s.v. lackey\",\"stance\":\"supports\",\"note\":FSDN},\n   {\"src\":\"WEB\",\"where\":\"s.v. lackey\",\"stance\":\"supports\",\"note\":WEBN}]}]}]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-517.json','w'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-517.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-517.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 517"
}
```


### [2026-10-15T02:48:32.226Z] TOOL RESULT

```
nodes verified: 10/10
node verdicts: {'confirmed': 5, 'disputed': 2, 'plausible': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1, 'disputed': 1}
ref checks: {'supports': 8, 'not_checked': 4}
books consulted: {'supports': 18, 'silent': 4, 'partial': 5, 'contradicts': 3} | by book: {'KLN': 4, 'LKT': 4, 'SKT': 4, 'WLD': 2, 'AHD': 2, 'TTS': 2, 'PHN': 2, 'FSD': 2, 'WEB': 2, 'BRT': 1, 'IEC': 1, 'LAT': 1, 'HRN': 1, 'HUB': 1, 'ARY': 1}
```


## [2026-10-15T02:48:41.943Z] TOOL CALL #41: SubagentHandback

```json
{
 "message": "I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-517.json` for page 517 (book p. 487). `verify_check.py 517` reports 0 PROBLEM lines and all 10 nodes verified.\n\nPage 517 has two real entries (Udero and Ul); the other 8 are redirects and were skipped.\n- **Roots:** 1 confirmed (Udero), 1 disputed (Ul).\n- **Nodes:** 5 confirmed, 2 plausible, 2 disputed, 1 transcription_suspect.\n- **Nourai's own refs:** 8 support his arrows; 4 were not checked because those nodes cite no reference.\n\nDisputed and suspect items:\n- **Root Ul/Jol/Jor (\"to go\"), and node Turkish ulak (disputed):** this is Vámbéry's 1878 grouping (TTS p.134 no.145), which Lokotsch and Klein copy. Wiktionary instead derives ulak from Proto-Turkic *ula- \"to join, attach (ends)\" + -k. Treating \"road\" (yol) and \"walk\" (yorï-) as separate roots, and citing Clauson, are my additions; no source I fetched confirms them. The word ulak itself is genuine.\n- **Italian node, empty in the chart, i.e. lacchè (disputed):** Wiktionary says Italian lacchè comes from French laquais, so it can't be the source of Spanish lacayo. The Greek → Italian → Spanish order is Klein's.\n- **French \"laquis\" (transcription_suspect):** the error is in the book. The printed page reads \"laquis\", a misprint for laquais (Klein, his own source, prints laquais). The JSON copies the book faithfully. The page PNG is saved at `data/verification/sources/refs/ocr/BOOK/517.png`.\n- **Plausible, not disputed:** Greek oulakis and the Spanish node. The origin of lacayo/laquais is still unsettled: the Turkish ulak route competes with Arabic proposals (al-qāʾid, lukaʿ, lakiyy).\n\nUdero entry: Avestan udara-, Latin uterus and English uterus are all confirmed (Pokorny 1104, Walde-Pokorny, Watkins, Bartholomae). The Persian loan olâğ الاغ is confirmed by Borhan-e Qate' p.157 and Mo'in.\n\nThere are no extraction errors for the owner to fix."
}
```


### [2026-10-15T02:48:42.328Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
