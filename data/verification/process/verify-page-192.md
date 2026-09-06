# Verification process log — verify-page-192


## [2026-09-06T02:14:30.432Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 192 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-192.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-192.json. Write /home/sfmqrb/git/rishe/data/verification/page-192.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 192` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:14:31.999Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:14:32.878Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:14:32.894Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
225	
226	```json
227	{
228	  "pdf_page": 126,
229	  "book_page": 96,
230	  "verified_by": "claude-opus-5",
231	  "verified_on": "2026-09-05",
232	  "entries": [
233	    {
234	      "entry": 0,
235	      "root": "Dheigh, Dhigha",
236	      "verdict": "confirmed",
237	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
238	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
239	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
240	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
241	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
242	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
243	      "nodes": [
244	        {
245	          "id": 6,
246	          "lang": "Avestan",
247	          "words": "pairi-daeza",
248	          "verdict": "confirmed",
249	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
250	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
251	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
252	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
253	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
254	        }
255	      ]
256	    }
257	  ]
258	}
259	```
260	
261	Rules:
262	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
263	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
264	- `words` = the transliterations of the node joined by "; " (copy from the chart).
265	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
266	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
267	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
268	- If a node lists several words, cover each word; if they differ in verdict, use the worst
269	  verdict for the node and explain per word in `derivation`.
270	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
271	  scholarship takes.
272	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
273	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
274	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
275	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
276	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
277	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
278	  any extraction errors (JSON differs from the printed page) the owner must fix.
279	  Do not paste the JSON back into your reply.
280	
```


## [2026-09-06T02:14:32.904Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-192.txt"
}
```


### [2026-09-06T02:14:32.916Z] TOOL RESULT

```
1	=== PDF page 192 (book page 162) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gheu 1 : to pour  (refs POK:447)
4	#1 (parent #0) [Avestan] refs=POK:447 | zaothra, zaothar, zaothr : holy water
5	  #2 (parent #1) [Pahlavi] refs=None | zôt : holy water
6	    #3 (parent #2) [Persian] refs=MON:1761; BQT:1043 | zawr «زور٢» : holy water (in Zoroastrian religion)
7	#4 (parent #0) [Avestan] refs=POK:447; SOD:184 | âzŭtay : melted butter or fat ; zav 2 : a kind of alcoholic beverage
8	#5 (parent #0) [Germanic] refs=AHD | 
9	  #6 (parent #5) [English] refs=KLN | geyser, gust, ingot, nugget
10	#7 (parent #0) [Latin] refs=AHD | fundere : to pour
11	  #8 (parent #7) [English] refs=None | funnel, fuse
12	    #9 (parent #8) [Persian] refs=MON:2599 | fiyŭz «فیوز» : fuse
13	  #10 (parent #7) [French] refs=AHD | refuse : poured back, rejected
14	    #11 (parent #10) [Persian] refs=MON:1665 | refŭzeh «رفوزه» : failed
15	    #12 (parent #10) [English] refs=AHD | refuse, confuse, refund, font
16	#13 (parent #0) [Greek] refs=OEW:124; FSD:66 | xymeia : infusion by pouring (mixing) liquids | NOTE: KLN:45 does not accept this derivation (folk etymology)
17	  #14 (parent #13) [Arabic] refs=OEW:124; FSD:66 | al-kimyâ : chemistry | NOTE: KLN:45; OEW:182 & AHD:30 derive this word from the Egyptian word "khem: black". See root "Kers 2".
18	    #15 (parent #14) [Persian] refs=BQT:1759 | kîmîyâ «کیمیا» | extra: کیموس | NOTE: See "Kers 2" for another possible root.
19	    #16 (parent #14) [Latin] refs=AHD | alchymia
20	      #17 (parent #16) [French] refs=None | 
21	        #18 (parent #17) [Persian] refs=MON:2115 | šîmî «شیمی»
22	        #19 (parent #17) [English] refs=KLN:45 | alchemy, chemistry, chemical
23	--- entry 1 ---
24	ROOT Gheu 2 -> redirect to Ghu 1
25	--- entry 2 ---
26	ROOT Gheu-bh -> redirect to Ghu 1
27	--- entry 3 ---
28	ROOT Gheue -> redirect to Ghu 1
29	
```


## [2026-09-06T02:14:35.636Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-192.json",
 "description": "Read source JSON for page 192"
}
```


### [2026-09-06T02:14:35.672Z] TOOL RESULT

```
{
  "pdf_page": 192,
  "book_page": 162,
  "entries": [
    {
      "root": {
        "name": "Gheu 1",
        "lang": "Indo-European",
        "refs": "POK:447",
        "gloss": "to pour"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:447",
          "words": [
            {"translit": "zaothra, zaothar, zaothr", "gloss": "holy water", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "zôt", "gloss": "holy water", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:1761; BQT:1043",
          "words": [
            {"translit": "zawr", "gloss": "holy water (in Zoroastrian religion)", "script": "زور٢"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:447; SOD:184",
          "words": [
            {"translit": "âzŭtay", "gloss": "melted butter or fat", "script": null},
            {"translit": "zav 2", "gloss": "a kind of alcoholic beverage", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN",
          "words": [
            {"translit": "geyser, gust, ingot, nugget", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "fundere", "gloss": "to pour", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "funnel, fuse", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:2599",
          "words": [
            {"translit": "fiyŭz", "gloss": "fuse", "script": "فیوز"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 7,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "refuse", "gloss": "poured back, rejected", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON:1665",
          "words": [
            {"translit": "refŭzeh", "gloss": "failed", "script": "رفوزه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 10,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "refuse, confuse, refund, font", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Greek",
          "refs": "OEW:124; FSD:66",
          "words": [
            {"translit": "xymeia", "gloss": "infusion by pouring (mixing) liquids", "script": null}
          ],
          "note": "KLN:45 does not accept this derivation (folk etymology)",
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Arabic",
          "refs": "OEW:124; FSD:66",
          "words": [
            {"translit": "al-kimyâ", "gloss": "chemistry", "script": null}
          ],
          "note": "KLN:45; OEW:182 & AHD:30 derive this word from the Egyptian word \"khem: black\". See root \"Kers 2\".",
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Persian",
          "refs": "BQT:1759",
          "words": [
            {"translit": "kîmîyâ", "gloss": null, "script": "کیمیا"}
          ],
          "script_extra": "کیموس",
          "note": "See \"Kers 2\" for another possible root.",
          "quote": {
            "text": "آنچه زر میشود از پرتو آن قلب سیاه - کیمیائیست که در صحبت درویشانست",
            "poet": "Hâfez"
          }
        },
        {
          "id": 16,
          "parent": 14,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "alchymia", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "Persian",
          "refs": "MON:2115",
          "words": [
            {"translit": "šîmî", "gloss": null, "script": "شیمی"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 17,
          "lang": "English",
          "refs": "KLN:45",
          "words": [
            {"translit": "alchemy, chemistry, chemical", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gheu 2",
        "redirect": "Ghu 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gheu-bh",
        "redirect": "Ghu 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gheue",
        "redirect": "Ghu 1"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T02:14:36.343Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T02:14:36.389Z] TOOL RESULT

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


## [2026-09-06T02:14:46.771Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','MON','BQT','SOD','AHD','KLN','OEW','FSD','WLD','BRT','PHD','NYB','HRN','HUB','IEC','SYN','LEW','LAT','SKT','WEB','ARY','PLA','AFM','FVQ','LKT','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600]); print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-06T02:14:49.129Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

CHEUNG null
```


## [2026-09-06T02:14:54.055Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nprint(json.dumps(d['POK'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SOD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\"",
 "description": "Get POK/SOD/MON/BQT offsets"
}
```


### [2026-09-06T02:14:56.080Z] TOOL RESULT

```
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
 "scans": [
  {
   "volume": "3",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
   "first_printed": 1208,
   "last_printed": 1925,
   "pdf_offset": -1205,
   "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json",
   "lang": "fas",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
   "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"
  },
  {
   "volume": "4",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
   "first_printed": 1920,
   "last_printed": 2475,
   "pdf_offset": -1917,
   "lang": "fas",
   "offset_note": "printed = pdf+1917, checked at pdf 150 and 500",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"
  },
  {
   "volume": "5",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
   "first_printed": 1,
   "last_printed": 290,
   "pdf_offset": 5,
   "lang": "fas",
   "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
   "requires_volume": true
  }
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
```


## [2026-09-06T02:15:03.851Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: ĝheu\\|lemma: gheu\\|ĝheu-\" POK_full.txt | head -40",
 "description": "Grep Pokorny full for gheu"
}
```


### [2026-09-06T02:15:03.899Z] TOOL RESULT

```
33191:Root / lemma: gheub(h)- 
33234:Root / lemma: gheugh-, ghugh- 
33261:Root / lemma: gheueja {gheueji) 
37235:Root / lemma: gheu- 
37257:lemma: gheu- : to pour + -tra suffix. 
37346:Root / lemma: gheu-, gheu-d- 
37664:Root / lemma: gheu- : ghd(u)- : ghau-
```


## [2026-09-06T02:15:04.366Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==104' POK_02.txt | head -80",
 "description": "Print POK page 447 area"
}
```


### [2026-09-06T02:15:05.840Z] TOOL RESULT

```
(dial.  fordeum)  n.  ,Gerste'  (aus  *ghxzd{h)eiom  ^Grannen- getreide',  substantiviertes  Stoffadjektiv) ;
hochstufig:  ahd.  gersta  ^Gerste'  (* gherzdä).
Dazu  vielleicht  gr.  ä-x^gSog  f.  ,wilder  Birnbaum,  Hagedorn',  maked. ä-ysQÖaj  gr.  d-xQ(xg  ,wilder  Birnbaum'  (d  <  *s^-),  alb.  dardhe  ,Birne,  Birn- baum' (*ghor-d-)  und  der  antike  VN  JagöavoL  5
nur  unter  Annahme  eines  Gutturalwechsels  (oben  S.  18,  Anm.  1)  läßt sich  lit.  girsa  ,Trespe'  hierher  stellen  (s.  unter  2.  ghers-).
WP.  I  611,  WH.  I  414,  657,   Specht  Indog.  Dekl.
§h6slO'  ,tausend'.
Ai.  sa-hdsram  n.  ,Tausend'  (sm  -gheslom^  zu  sem-  ,eins'),  sa-hasriya-  ,tausend- ^ fach',  av.  hazarirdm  n.  ,Tausend',  npers.  hazär,  woraus  arm.  hazar  entlehnt;  ^ sogd.  2V  (=  *zär),  afgh.  z^r;
gr.  ion.  %eilioL,  äol.  xelXioi  (xeXkr^axvg  ,Tausendschaft'),  att.  yrthoi  (^xialioC),  m
Das  Grundwort  *yßo'ko-  findet  sich  in  sakisch  ysära  und  in  Lehnwörtern    1 finnisch-ugrischer  Sprachen  (Jacobsohn  Arier  und  Ugrofinnen   105  ff.).
Vielleicht  auch  lat.  mille  ,tausend;  ein  Tausend',  falls  aus  *sml  gzhll (ghsll)  ,eine  Tausendheit' ;  *sml :  gr.  ^/a.
WP.  I  633,  II  488,  491,  WH.  II  88  f.,  Schwyzer  Gr.  Gr.  I  593.
447
1.  ghesor-,  ghesr-  ,Hand'?
Arm.  jern  (*ghes-r-7n),  PI.  jer-k'  ,Hand^  (Meillet  P]squisse  83) ;
o-v.  x^iQ   f-  ,Hand^,   Gen.  xeiqdgj  dor.   xVQog,   Dat.  PI.  x^odt   (danach  die
Form  yjQ-)',
tocb.  A  tsa)%  B  sar  ,Hand^  (nach  Pedersen  Tochar.  236  aus  *kesar  =) bitt.    ki-es-sar    (kessa?-)    n.  und    ki-es-si-ra-as    (kesseras)    tu.,  i..    Dat.    Sg.
ki-ls-sa-ri  (kesri  =  gr.  x«^^^'?);
über  lat.  Jr,  hir  ,hohle  Hand^  (aus  osk.-umbr.  *Äer  <  ^ghesrä?)  s.  WH.  I  649.
2.  ghesto-  ;Hand;  Arm^
Ai.  hdsta-h  m.  ,Hand^,  av.  zasta-,  apers.  dasta-  ds. ; lat.  praestö  ,zur  Hand'  aus  ^^prae-liestod  (EM  805  f.)?;  anders  s.  unter  stä-] lit.  pa-zastZ,  pa-zastis  f.  ,Raum  unterm  Arm,  Acbselböhle^ Da  arm.   jefn  auch   auf  *gher-7n   zurückgehen   könnte  und   ebenso    die o-r.  Formen  besser  aus  *gher-s  erklärt  werden  können,  da  ferner  alb.  dor'6 f.  ^Hand',  PI.  konson.  duar  eine  Grundform  *gher-  erfordert  (ghesr-  hätte *dostr6  ergeben),  wäre   mit  Belardi   (Riv.  Studi  Orient.  23,  69  ff.)   zu   er- wägen,  ob   nicht   fürs   Hitt.   und   Tech.   Metathese  von   -rs-   zu   -sr-  anzu- nehmen sei,   und   die   Gruppe  1  von  2  zu   trennen  un
```


## [2026-09-06T02:15:11.986Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 37235 37346 37664; do sed -n \"${L},$((L+45))p\" POK_full.txt; echo \"-----\"; done",
 "description": "Print Pokorny gheu entries"
}
```


### [2026-09-06T02:15:13.665Z] TOOL RESULT

```
Root / lemma: gheu- 

Meaning: to pour 

Material: Old \x\^\z juhoti, juhute^ pours in fire, sacrifices ', Passiv huyate, huta-h^ 

sacrificed ', homan-u. " sacrificial downpour, sacrifice, oblation' (= gr. xsujja), homa-hm. 

6s., hotar- " offerer, sacrificer, priest', hotrai. " oblation ', hav/s-n. 6s., havanamn. 

"sacrifice, oblation'; 

maybe alb. d/y'ame lat' : gr. 5r|M6(; "fat' [common alb. gh- > d-]; 

Avestan zaotar, zao&r-m. "priest, priest of sacrifice ', Middle Persian zot, Avestan 
zao&rau., zao&rai. " liquid sacrificial donation, sacrificial drink, sacrificial downpour', 
npers. zor^ holy water', Avestan azutay-t "fat, lard, luxuriance, abounding fullness, 
wealth'; 

Note: 

First of all Old Indie then Avestan, Middle Persian, npers. and alb. seem to employ Root / 
lemma: gheu- : to pour + -tra suffix. 

Armenian yby/" poured' (< gheu/o-), Jew lorm, shape'; here also yb/"" valley' (< ghouer- 
o)l 

Phrygian ^supav nnynv Hes. (= gr. x^upa); thrak. ^srpaia xuTpn ( *gheutr-), FIN r£u5i(;, - 
o<;; 



gr. X£(F)w pour', Aor. horn. £X£ua < *£X£uaa, Perf. kexukq, xut6(; " poured ', xsupa " 
that which is poured, stream, cast vessels, bowls, river, libation, drink offering made to the 
gods ', xoavoc;, xwvo(; ' a copper cup, mold ', xon " libation for the dead', xosuc; m., f. " 
measure for fluids ', xouq ds.. Gen. x^oq and xoO(;, older dial, xou m., f. " heaped earth', 
XU)|ja ' earthwair, xow ' pile up earth, pour '; xuTpoc;, xuTpa " earthen pot, pan, xutAov " 
anything that can be poured, liquid, fluid, water for washing, the bath, a mixture of water 
and oil, running water, stream ', xu5r|v " as if poured out, in floods or heaps: without order 
or system, promiscuously, indiscriminately, in unfettered language, i.e. in prose, 
abundantly, rich ' (to 5 compare the root extension gheud-), koxuSeTv " stream forth 
copiously ', Koxu noAu, nAr|p£(; Hes.; xucn<; " shedding, pouring out or forth, diffusion, e.g. 
of nutriment, melting, liquid poured forth, flood, stream, of dry things, heap, of fluency or 

copiousness of speech, quantity, abundance ', xu^O(; "juice, sap' (< *ghuslo-, W. Schuize 

-----
Root / lemma: gheu-, gheu-d- 

Meaning: to disappear, get away 

Material: Middle Irish guassi. {*ghoud-tS) "danger', guss ds. = cymr. gwst' evil, 

wickedness, disease, malady' ( *ghud-tu-s); 

Old English gietan, a-g/etan "\n]ure, slay'; 



Lithuanian zuvli, zutr perisli ', zudau, zudytr s\ay'; Latvian zudu, zusV disappear, get 
lost ', zaudet lose'. 

References: WP. I 564, WH. I 568, Lotli RC 45, 193 ff. 
Page(s): 448 

Root / lemma: ghe-1, ghei- 

Meaning: to be empty, lack; to leave, go out 

Note: perhaps to ghe-, ghei- ' yawn, gape' (compare " yawning emptiness '); from ' stand 

gapingly ' can also be changed ' leave, depart '. 

Material: With the meaning- coloring B: 

Old \n6'\cjahaf/" leaves, gives up, abandons, leaves behind ' ijahimah, \fr\per. Jah/h/, 
Aor. ahat, ahayi, participle hTna-h), jfhTte^Qoes, run into, bump into, come up against ', 
hJyate' become abandoned, falls behind '; hani-ht " lack; release, giving up, giving way, 
conceding ' {vihayas- " empty room' because of prefixes, that also in vi-ha- " gape '); 
compare S. 427; 

Latin hems " heir ' {*ghero- + e-c^d\-, " das verwaiste Gut an sich nehmend '?, s. about 
the ending under e-particle); 

Note: 

Common Old Indie : Latin gh-> h-. 

Avestan zazamil dismiss from, fire from ', with ava-^ leave, go away, scare, frighten ', 
with upa-3iU6 fra-^ leave, allow here, lead here, conduct here '; a-za- ' go near, approach 
', uz-za- " jump, be elevated ' {uzayanto par\.\c\p\e Nom. PI.); 

Maybe alb. Geg me zane' quarrel, capture, occupy ' 
-----
Root / lemma: gheu- : ghd(u)- : ghau- 

Meaning: to yawn, gape 

Note: (see above ghe/-) 

Material: Gr. X'^oq n. 'the empty room, airspace' (later also "cleft, gap'; probably from 

*xaFo(;), xc(uvo(; ' gaping, lax ', xc(uAi-65ovt- 'with spread teeth'; 

whether here also Gothic ^an// "land, region'. Old High German gaw/, Modern High 
German Gau, Old English ge, etc. from *gh9u/omw\t\r\ similar meaning-development as by 
gr. xwpo(;, x^pa (see below ghei-^ lack; abandon ') and Armenian gavar^ portion of land, 
area, region'? or from Germanic *ga-awja{\.o ak"a, above S. 23) ' scenery in the water'? 



Old High German goumovn. {*gh9U-men-), giumo {*gheu-men-) " palate ', ablaut. Old 
Norse gomr^Qums, palate', Old English gdma{ev\Q\. ^^/77s 'gums'), Old High German 
guomo {* gh^u]-m-) " roof of mouth = palate'; about Lithuanian gomurys see below; 

in addition probably Old Icelandic geyja'bark, bay, scold, chide, mock ', Old English 
g/egan ^cry', Old Icelandic god-ga' blasphemy ', hund-ga^ bark ' and further formations 
Old Icelandic gauta^ babble, chatter, brag, boast', ndld. guiten^ scold, mock ', Modern 
High German dial, gauzen, gauzen^bark, bay, cry', Gothic gaunon' wail, grieve ', Old 
Icelandic gau/a'\r\o\N\'; about Lithuanian gaustisee below ^o^-'call, shout, cry'. 

In spite of the non-palatal root initial sound (see above about Lithuanian gomurys) it could 
belong here, because many originally palatal gutturals appear in Lithuanian as g, k. 

further in the meaning " yawn ' with Aforms (: gr. xauAi-) perhaps here Middle High 
German gielm. " jaw, gullet'. Old Norwegian -gjdr\v\ place names? as well as Norwegian 
dial. gyrc\ei\, gap, cliff gap ' {*gulja-\ so also Swedish ^o/'puddle, slop, pond'. Middle 
High German ^J//e "puddle, pool, slop'. Middle Low German gole, goe/^ swamp, marsh' as 
" the cavity in which water is collected '?). 

Modern High German Gosche, Gusche, ndd. goske, guske^b\g muzzle' as s/r-formation 
belongs here however, they would possibly be used with Old Indie ghosat/" calls, shouts, 
howls' are related (see Persson Beitr. 116 f.), it is not likely a trivial expression without 
pursueable history; 

Maybe alb. gusha'tbroat' 

Baltic *gamur/a-m. " palate' in Lithuanian gomurys, Gen. gomur/om., also gomere {Akk. 
gomer^) f.; Latvian gamursm. ' windpipe, larynx' (only by Miezinis doubtful guomurs); a 
sound equivalent to Modern High German (Sa^/77e/7 produced Lithuanian Latvian i/o (Baltic 
-----
```


## [2026-09-06T02:15:17.372Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=37235 && NR<=37350 && (/Page\\(s\\)/||/References/)' POK_full.txt",
 "description": "Get page for gheu- to pour"
}
```


### [2026-09-06T02:15:18.820Z] TOOL RESULT

```
References: WP. I 563 ff., WH. I 563 f. 
Page(s): 447-448
```


## [2026-09-06T02:15:22.944Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==105' POK_02.txt | head -60",
 "description": "Print POK leaf 105"
}
```


### [2026-09-06T02:15:24.514Z] TOOL RESULT

```
d  zu  glier-  , greifen' zu  stellen  sei.
WP.  I  541,  603,  WH.  I  243,  Trautmann  367,  Duchesne-Guillemin BSL.  39,  211,  Schwyzer  Gr.  Gr.  I  446,  569,  Specht  Idg.  Dekl.  75.
gheu-  .gießen' ;  gheu-mn  , Opferguß'.
Ai.  juhöti,  juhuti  , gießt  ins  Feuer,  opfert',  Passiv  hüydte^  huid-h  , ge- opfert', höman-  n.  , Opferguß,  Opfer'  (=  gr.  x^v^a),  höma-h  m.  ds.,  hötar- , Opferer,  Priester',  hötra  f.  , Opfergabe',  havis-  n.  ds.,  hdvanam  n.  ,Opfer';
av.  zaotar,  zaod-r-  m.  , Priester,  Opferpriester',  mpers.  zöt,  av.  zaod-ra \\.,  zaod-rä  f.  , flüssige  Opferspende,  Opfertrank,  Opferguß',  npers.  zör ,Weihwasser',  av.  äzutay-  f.  ,Fett,  Schmalz,  Üppigkeit,   strotzende  Fülle' ;
arm.  joyl  , gegossen'  (<  gheulo-),  jeiv  ,Form,  Gestalt';  hierher  auch  Jor ,Tal'  (<  ghouero)  ?
phryg.  ^evLidy  rtrji^v  Hes.  (==  gr.  x^vi^a)',  thrak.  ^ergaia'  xvxqri  {*gheutr'\ FIN  Fsvöig,  -og]
gr.  xf(/)w  , gieße',  Aor.  hom.  ex^va  <  ^exsvaa,  Perf.  xf/vKoc,  x^'^oc;  , ge- gossen', xfr^/a  ,Guß,  Fluß,  Trankopfer',  x^^^^S»  X^^^g  , Schmelzgrube, Gußform',  x^V  ,Trankopfer  für  Tote',  xofivg  m.,  f.  ,Maß  für  Flüssigkeiten', Xovg  ds.,  Gen.  x^^S  ^^^  X^^g,  älter  dial.  x^^  °^'>  ^-  ,aufgebäufte  Krde', XOJI-KX  ,ErdwaU',  x^f^  , schütte  Erde  auf;  x^'^Qog,  x^'^Q^  , irdener  Topf, X<Ji^lov  ,Waschwasser',  x^^V^  , reichlich,  hingeschüttet'  (zum  d  vgl.  die Wurzelerweiterung    gheud-),    -KoxvSelv    ,in    Menge    hervorströmen',    xoxv*
448  9
noU,    Ttlfjgeg   Hes. ;    x^^^tS   ,Guß\    x^^^S    .Saft'   (<  *ghuslo-,   W.  Schulze^t'^ mündl),   X'GiJLÖg   ds.   (<ghu-smo)',    weiter   hierher   xwo^iai   ,zürne,    bin   u^,  ^' willig'  {xo)6iisvog  =  avyx^o^isvog  Aristarch)  ?
Lsitfä-tis  f.  , Gießkanne',  fü-tilis,  futtilis  gleicht  ausgießbar,  zerbrechlich, eitel,  unnütz',  eaj/«^i  =  effüsi,  effütiö  ,schwatze  heraus'.
Sehr  zweifelhaft  ist   die  Zugehörigkeit  von  mhd.  gül  ,männliches  Tier, Eber,  Pferd',  nhd.  Gaul  (im  Bayr.  ^Deckhengst',  Schweiz,  gül  ,Hahn',  vglj ndl.  guil  ,Stute,  die  noch  nicht  geworfen  hat*,  s.  Sommer  IF.  31,  362  ff.)^ ,Samengießer^
"VVurzeler  Weiterungen:
gheud-:
lat.  fundö,  -ere,  füdl,  füsum  ,gieße,  lasse  fließen,  schütte  aus'  (übei füsus  ,Spindel'  s.  WH.  I  474)  ;
got.  giutan  ,gießen',  aisl.  gjöta  , (Junge)  werfen',  ags.  geotan  ,gießen,^ fließen,  schütten',  afries.  jäta,  as.  giotan,  ahd.  giozzan  ds.,  nisl.  gjöut. ,Höhle,  enge  Gasse^,  aschwed.  giuta  , Gußform',  ahd.  giozo  ,fließende^ Wasser',  ags.  gyte  ,Guß,  Flut',  ahd.  guz  ,fusio',  ndd.  gete  ,niedrige  Wasser- straße', norw.  gota  , eingeschnittene  Rinne',  as.  gota  ,canalis',  holl.  gooi jGosse,  Rinne',  nhd.  Gosse,  ags.  gutt,  en
```


## [2026-09-06T02:15:35.775Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT zaoθra ===\"; grep -n \"zao&r\\|zaoOr\\|zaoθr\\|zaotar\\|zaotar-\" BRT.txt | head -30; echo \"=== BRT azuti ===\"; grep -n \"āzūti\\|azuti\\|äzütay\\|azutay\\|äzuiti\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-06T02:15:35.861Z] TOOL RESULT

```
=== BRT zaoθra ===
4055:afryö.zaotar-  101
4075:•  j.  a'fryo.zaotar-  Adj.  'der  einen  (den
4147:Wesenheit,  Menschheit,  alle  Welt':  tarn  . . alva  vispahe  'nhlui  astvatS  anaiwyästis iunahiY,  18.^0;  31;  —  :^aSaya  .  .  vispd 'jtkui  astvä  *)vaiti  anläse  framiryeite  Y.3. 33;  J-i.  5-4,  Y./p.io,  F.^h;  —  zam  .  . yä  vTspsm  °hBm  astvant>m  baraiti  jumca iristitnifaYl.  13.^;  129,  JO.51,  ;(),94,  Y./"?. 2,  57.16,  Y.  18.16,  A.4.6;  —  vjspähe 'lik^ul  asti'ais  sragstim  Y.O.  i;  Yt7.  2', ÄS4,  y.152,  75.79,  P.2.^  ^-84,  Vyt. 36.  ß)  insbes.  von  der  Gesammtheit  der nichtpriesterlichenOemeindeangehörigen**: zaotars{^d.)  iairim  .  .vacimca  °wÄf(DS.)'^ astvaite  paiti.dhayai  N.  72.  b)  'das  erste, d.  i.  das  materielle  Dasein,  Leben':  yaii ä  °rihul  *pa<mruyS  bavat  (sd.)  Y.  2S.11; — *_j'((^ö  äis  i^ä  vansaitg  yä  data  'uAiuf paouruyehyä  ratul iyao^ana  rasistä(sd.) .  . Y.33.1;  zit.  55.6;  —  °uASus  sq>di  (sd.) paouruyehyäY.  48.(>.  c)  'dieses,  d.  i.  das irdische  Leben,  Dasein':  "»hSus  maraxtärö (sd.)  ahyä  Y. 32.\^'>'i;  —  'ijAjus  ahyü paourrtm  *yqm  mSi  vtdvä  (sd.)  .  .  "was zu  Anfang  dieses  Lebens  .  ."  4^5-3;  4;  — ahyä  'uhiuif  vtspa  maS>ä  (sd.)  Y.J4-6; —  ahmäicä  °huyg(Xi5-)  manahyäicäY.  4f>. 2;  —  aliKa  °uh}us  manahyeheca  'uhsus Vyt  32;  —  s.  noch  unter  a.  d)  'das
7034:kniipfiiDg  eines  adversativen  Satzes  'aber; sondern;  vielmehr;  gleichwohl':  iha  main- yete  dus:^armä  .  .  ä'  az3M  manya  Yt.  10. losf.;  —  nöil  .  .  vispa  yasathahs  .  .  ä' .  .  aÄ'J  zara%uitro  Vt.  IJ.  ig;  5,  55  aSt^', N.55,  Y./0.8,  ig.  5;  —  iä  fi-avasays  .. aojistä  hinti  .  .  yä  .  ,  saosyaniqm  ä° anyalsqm  fravasayö  (sd.)  ,  ,  Yt.  jj.  17; N.  102;  —  nabänazdists  ä'  kavatqm  nana (sd.)  N.  Ig;  g,  67;  —  «/  zaotars  (sd) kairim  avAap. .  3'  AävanänS  (näral.  kairim a»Aat)  yat .  .  N.  72;  73-'j6,  66'';  —  apqm . .  yä  para  ahmäi  hist>nta  .  .  ä°  th  nüram p-aiacin/i  Yt.  13. 5:i(.;  56,  5S;  —  aat{^.  8) yahmäi  xsnBtS  bavaiti  mi^rS  ahmäi  jasaiti avaiäAe  ä'  yahmal  ibistd  bavaiti  . .  akmüi früiiinäayeiti  nmämmca  ..  Yt/o.S?; yaike  xsa'hriäa  nStt  aotfiri  ar?ka  . .  para akmat  yat  . .  ä°  yat  ..  ". .  bevor  . aber  als  . ."  Ytig.$$f.;  — yat  hf puhi iissaySi^e  .  .  ikaisö  anyö  .  .  ä°  anys Y.g.ia;  —  tarS.d»nanS  (sd.,  näml.  urv rayä  aahari)  .  .  ä°  up»ma  aisöJräjanAa N.po; —  navajcsaparfm  ..  aivii^äi kama  mazäräjaAlmW.^.^2;'^.46,47,5o; —  nöit  ahmt  nmäne  *sänaite  ä^rava  .  . ä'  .  .  sayänie  dahaksea  "nicht  werden  .  , geboren  .  .,  sondern  es  sollen  geboren werden  .."  Y.  //.6;  —  käu  .  .  yff  .  .  van- tasea  Aqm.räzayeili  .  .  aha  diin  upaJaosa^ yati  .  .  raZiayaca  (sd.)  .  .  ä'  yat  .  .  var>- saica  *hqm.räzayar>Aa  .  .  aat  (s.  7)  .  . pascana  apa.baröis  ". .  vielmehr  wenn  du dir  die  Haare  ordnest  .  .,  so  sollst  du dann  . ."  V.iy.2—4;  —  attm  vispanqm dämanqm  nipäta  ahmi  .  .  ä'  ('gleich- wohl') ma  nöit  masyäka  .  .  yazante  YL 10. 54.  a)  bes.  mit  a)  folgendem  _ya/  oder
7261:ya().         b)   eines  Nebensatzes:  yöi  nmäna kam.barSfnahi  (sd.)  .  ,  ätrsmca  .  ,  W  pas- ciota  ahe  nmänake  spä  vä  nä  va  in%yäi iüia  .  .  "wenn  wir  . ,  und  es  stirbt  dann . ., wie..?"  V.5.39;  Vd./();   —  yS  itarö  .. mpaidyeinte    .  .    ä'    ae^am    naram    afvS irtiyat    cvat  ..  V.5.27.'         3)  'lur    An- knüpfung eines  adversativen  Satzes  'aber; sondern;  vielmehr;  gleichwohl':  i'äa  main- yäe  dus^artnä^  .  .  ä°  azitn  manya  Yt.  10. 105  c;  —   nöii  .  .  vjspa  yazatinhö  .  .  ä' ..  aevd  zarä^usürä  Yt.  ij.  ig;  5,  55  aSt^^ ti-S3<  V-io.S,  ig.  5;  —  iä  fravasayS  . . acjifta     h^nti    .  .    yi    .  .    saosyantqm    ä° ai^alsqm  Jravasayö  (sd.)    .  .    Yt.  1^,  17; N,  I02;  — -  nahänazdiStö  ä'  havatam (sd.)  N.  i^;  p,  6-];    —    äs    zaotars  (sd.) kairim  ar^hath.ä'  AävanänS  {vä.m\.  kairim auAat)  yal .  .  N.  ■J2;  yS—yO,  66';  —  apa. •  •  y^  pora  ahmat  hiit?nta  .  .  3*  W  nürqm fratoHnü  Yt.ij.53f.;  $6,  5S;  —  aai{%'.Z) yakmai  xstiüts  Öavaiti  mihrS  ahmäi  jasaiti avairiie  ü.'  yahmäi  ßistS  bavatH  . .  ahmäi frasciruiayeiti  nmätamca  ..  YL/0.87, yeiihe  x^akrä^ia  nsU  aoüin  änAa  . .  para tthmat  yat    , .    ä°  yal    . .    ",  .  bevor  . aber  als  .  ."  Yt./().33f.; — yaj  Ae pu%, usjaysi^e  .  .  ikalsB  anyS  .  .  ä°    anyS  .  . \.g.io;    —  tar5.d»nanB  (sd.,  näml.  urva- rayä  ar^han)  .  .   ä'   vp?ma  agis.drajaT3h& N.90;  —  navajcsaparim  ..  aiwi^äme  ä' hama  mäzdräjakim  V.J.  42;  N,  4Ö,  4~>5'i; —  nsil    ahmi  nmäne  *sanaile  ä%rava  . ä'  .  ,  sayänie  dahakäca  "nicht  werden  . geboren  - .,   sondern    es    sollen   geboren werden  . ."  Y.  //.  6 ;  —  hau  .  .  yO  .  .  varg- thfca  Aqm.rüzayeiti .  .  a'ia  dim  upa-taala^ ydii  . .  raesayacä  (sd.)  , .  ä°  yat  . .  van- iäsca    *hqm.räzayaaha   .  .   äat    (s.   7)    .  . fascaSa  apa.bardi!  ". .  vielmehr  wenn  du dir  die  Haare    ordnest  . .,   so  sollst  du dann  .  ."  V.iy.z-i,;    —    a%>m  vTspanqm damanqm    nipäta    ahmt    .  .    ä"    ('gleich- wohl') mä  nSil  masyäka  .  .  ya'^nte  Yt  10. 54.        a)  bes.  mit  a)  folgendem  _j'iii  oder ye:i,  ß)  vorausgehendem  yezi  "wenn  aber, wenn  jedoch",  kondiz.:  a)  *yujyaslil  haca *nmänät  .  ,  ä'  yal  h!  aoxte  .  .   d^a  *hil *xiayete  ..  haxtSii  (sd.)  N.<Vf.;  V.7.3; all  (s.  8)  yS  . .  upairi  hunanm  (sd.)  mc iarät  .  .  ä°  yat  .  .  paiti  barJt  äaj  (s.  2) yal  .  .  ara  baraite  "wer  .  .  aber  wenn  er ■ .  und   wenn   er   ■  ."   P.j7f.;
8392:•  j.  upa^sraotar-  m.  Bezeichnung  derer, die  beim  Gottesdienst  den  (Gaia-) Vortrag des  Zaotar,  soweit  vorgeschrieben,  nach- beten oder  respoDSorisch  ergänzen":  *'ianu,- pir3i:S  laota  dahma  "tarS  yasi  dim  tanu.- p?r?i:fm  *vT'iian  aSavatö  *ratuffyö  yaval framarfiOi  yai  aal  dim  nsit  ianu.pirJSiim *vi'jar>  vTspanam  glihanqm  *ratufryS  "Der Z.  ist  /,  die  Ü.  sind  d.  Wenn  sie  wissen,  | dass  er  (L  ist,  sind  sie  nur  für  das  r.,  was ' sie  (selber)')  aufsagen.  Wenn  sie  aber nicht  wissen,  dass  er  /.  ist,  so  sind  sie  für alle  Gahaz  r."  'S. 3g;  38,  3g''>]  —  sum- fuioiti  saota  'faranam'^  rtöit  'tärS  zaotarö xaata  ratufris  altavats  'tärSyavat  *frama- r^nti  "Es  hört  der  Z.  die  Ü.,  nicht  die  U. den  Z.;  darin  ist  der  Z.  r.,  die  U.  aber nur  filr  das,  was  sie  (selber)''  aufsagen" N.2/;  27 J.
9343:Hs  zaotar^  (sd.)   'rXm   atihat  N.  72.  |      Vgl.  Itor-  and  iMltari-;  \\ii. kiraydii itaTsia-
10300:hvialia  V.O.33,  /tf.8;  —  hiku  pqsitu  (sd.) °tu  (IS.)  tihayaaa  Y.16.2;  —  nsit  Alm  'tvd (GS.)  vindm  pasvasca  . .  "es  fanden  nicht mehr  Platz  .."  V.2.8;  9.  a)  mit  misvan- Adj,  (sd.,  auch  fdSt.):  misvärum  'tarn  S. 2.^0;  — misvänahe  'tvaie(GS.)^>  S./.30; usw.  2)  sva.  'festbestimmter,  vorge- schriebener, richtiger  Ort  (usw.)';  iva aHahe  nars  'tu^  anhat  ya£  irisis.kasahe ^■,?-^5i  —  y^S  "^'''^  zaota  (sd.)  /r3ya- zititi ..zaotars  "lai-a^  (IS.) .. syae^nöJätfya .  .  paiti.jatfkdit  hävanänö  -taiii'  .  .  N.  Si;
10301:—  II  adam  käram  *»:;(«'.?  (LS.)*>  avasiäyain "ich  stellte  das  Volk  (wieder)  an  seinen richtigen  Platz"  Bh. /.  14;  14'; —  .\ismim ..  adamsim  *°^avä'''>  tnyasädayam  ",  .  ich stellte  sie  (die  Erde)  wieder  an  ihren richtigen  Platz"  Q.6.^.  a)  mit  däitya- Adj.:  *zaotars  (sd.)  duityS  'tus  mawinya nmänahe  N.  ;<?;  J^J;  —  ys  ätnm  nasu- piihin  däitim    -tum   avi  ava.baraiti  V.S.
13880:1  (IS.)   ".  .  der  bei  seinem   Aufgang'"  j- «^"z-zaotar- Adj. 'der  einen  schlechten,
13882:heraufbringt"  Yt  8. 36.  a/rySjzaoläro  -taro  31  a/imat  afryo.zaotarS
16924:•  j.  barat-äyspta-  Adj.  (fem.  •«-)  'Gliicks- gllter,Herrlichkeiten  bringend,  vers  chaffend': saoiqmca  barat.avantqm  'tarn  Vl  /J.  4a. ■  j.  baratzao&rä-  Adj.  'Z.  bringend,  dar- biingend':  raästam  astqm  'hrqm  Ytio. 126,16.1.
26514:Ständlich. •  j.,  g.  staotar-  m.  'Lobsänger':  fra- varäni  .  .  'tä  amtlanqm  spmianqm  yaitä amtlanqm  .  .  Y.  i2.  i ;  —  frä  t!  vTsäi urva'hif  'ta  V.io.g;  14.  i  (VJ),  Vr.5.  i;  — urva'h^m  'tar>m  »«»^«»^^«(Sp.  1405  u.) da'is  apxta  ahurS  .  .  yaiha  .  .  Y.  /O,  9; sara~^u!tra    'tanca    zaotarica  .  .  Yt  7.
27357:dass  es  , .  ist,  bekannt  werden  als  . .'"': mal  vi  padäil  (sd.)  ya  frasrütä  (NSn.)  '3> Jsayt  pairijasai  ".  .  mit  den  Versen, die  bekannt  sind  als  die  des  frommen Eifers  . ."  Y.  50. 8.  b)  PPfP.  s.  auch bes.  n)  Kaus.'*>;  t)  dnwS.  U  2;  Med. (ausser  N.20)  in  pass.  Sinn;  als  PPfP. dient  frasruta-;  a)  vom  AhunaVairya: tarn  . .  zaroäiuitra  ahumm  vairim  fra- irävayS  .  .  apar»m  xraoidythya  (sd.)  fra- srSiti  Y.5. 14;  Yt.  IQ.  81,  V.  j^j.  2 ;  —  %ris ahm  vpa-stuyät  .  .  ca^wsrs  .  .  ahumm vairim  frasrävaySit  V.  18.  43;  11.  3,  i-j.  6, 7p.az,  N.ÄJ;  —  yezi . .  aAunqscä  vairyqn fi-asrävayeili  N. 50; — yasca..bayqm  ahu- nahe  vairyehe ..  srHvayäl  frä  va  sravayB yazäite  Y.  ig.(>;  —  ahunahe  vairyehe  alaya frasratake/rasrävayamnahe"A.^AV., das  wie  sichs  gehört  vorgetragen  worden ist  und  vorgetragen  wird"  Vr.  12.  a's';  — ahunahe  vairyehe  asaya  frasrätahe  Y. 27.  7 ;  —  yöi  kl  *'ma%>mya  vaca  frasrä- vayamnahe  (näml.  ahumm  vatrlm)  vä vpa.srunvanH  *yat  vä  *yasn?m  ''yazamnahe "die  ihn  (näml,  den  Zaotar)  hören,  wenn er  mit  mittelstarker  Stimme  (den  AAV.) oder  aber  den  Y.  betet"  N. b)  von  den  Gä%äs:  sraosö  .  .  yö paoiryS  g^ä  frasrävayai  yä  panca  Y. 57.  S;  —  zaotar^ (id.)  kairim  ..*gä%asca frasrävayaiti  N,  72 ; "  Vd.  12 ;  —  käia  zaota (sd.)  gäiiä  frasrävayaiti  N.  j_j,  c)  ohne Objekt  sva.  'die  vorgeschriebenen  Gebete Lufsagen':  */rasravay5'^'>  ratufris  nsil asrävayS  N. /04;  Vd,  2/(?).  2)  'etwas
27523:•  ].,  g.  zaotar- ;  zaoSr-  m. 'Priester,  Ober- pricster';  y7  (näml.  zara'husirö)  *fä  a/ä tnzü/  .  .  kaya  (Sp.  46a  m.)  S.. 33.it;  be- nutzt Yt.  4.T.  yi  °ta  sarähustrS.  A)  im jAw.  Name  des  vornehmlich  mit  dem Vortrag  der  Gä'iäs  betrauten  Oberprie- sters, der  den  Gottesdienst  zusammen  mit sieben" Unterpriestem  (s.  'raiav-),  im  Not- fall aber  auch  allein  (s.  N.  Si,  Sp.  1653  ra.) vollzieht:    'lanm    asavanim    aiahe  ratäm
27524:zaotar- A
27529:zaotar-  Noten
27566:•  j.  'zaoöra-  n.  'Amt  des  Zaotar,  zaotar- amtliche  VenichtUQg':  zaota  (Sp.  1653  u.) anahaxiS  . .  dqkistäi . .  °r»m  raixiaiti  N. 80;  —  ''kahyäcii  nä  dahmanam  (Sp.  705  0.) •rlSu  raiu/ris  näirikasat  aptrmäyBka- keHt  yesi  vaiha  h3%anqm  . .  *'/raiauru- nss(sd.ya  N.40.
=== BRT azuti ===
8079:J5.94.         a)  in  Verbindung  mit  azutay-  säspun  Az,  _j.  ^)  fravasis  .  .   °rä  ..
10985:•  j.,  g.  xSvid-  m.  'Milch';  im  Gegensatz zu  axBtay-  (sd.)  überhaupt  'flüssige  Nah- rung' im  Gegensatz  zu  fester:  pars  °isca (NS.)  äsaitisca'^  gsui  mal  "hervor  (geholt werde)  Milch  und  Fett  samrat  Fleisch" V.13.2%;  —  ■ilaica  (DS.)  azStayalFa''> Y.ßS.ii  —  am  äiStBis(sd.)  aAurB mohnm tasat  .  .  gavSi  'lihmlä'''  * AvS urusalibyS V.  25,  7;  —  *mmdäidyäi  (sd.)  «ftfem^)  Y. 1/.9.  a)  Du.  in  Verbindung  mit  äsütay- Du.:  "röa  (AD.)  äzuiti  yazamaiäeY.iG.Z; zit.  *F,5.  a)  pasca  xsavaidlm  ayara- namca  (soll  heissen)  "nach  sechs*'  Tagen" Vd.5.
```


## [2026-09-06T02:15:37.267Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD zot ===\"; grep -n -i \"zōt\\|zot \" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB zot ===\"; grep -n -i \"zot\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg for zot"
}
```


### [2026-09-06T02:15:37.384Z] TOOL RESULT

```
=== PHD zot ===
=== NYB zot ===
```


## [2026-09-06T02:15:43.283Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27560,27600p' BRT.txt",
 "description": "BRT zaothra entry"
}
```


### [2026-09-06T02:15:43.333Z] TOOL RESULT

```
disa  das  Wort  ursprünglich  nur  Neatmm  wai
und    nur   im  Plural    gebraucht  wuide;    dann
stellte  sich  zu  :ao%ti  APn.  der  ASf.  ziu%rqm
ein  uiw.   Der  feminine  Gebrauch  ist  weitaus
der  gevöbnlichere.    Dem  entsprechend  habe
ich  die  Komposita  angesetzt.  —  3)  S. :
•  j.  'zaoöra-  n.  'Amt  des  Zaotar,  zaotar- amtliche  VenichtUQg':  zaota  (Sp.  1653  u.) anahaxiS  . .  dqkistäi . .  °r»m  raixiaiti  N. 80;  —  ''kahyäcii  nä  dahmanam  (Sp.  705  0.) •rlSu  raiu/ris  näirikasat  aptrmäyBka- keHt  yesi  vaiha  h3%anqm  . .  *'/raiauru- nss(sd.ya  N.40.
Ableit.  aus  taetar-.   —   ai.  hoträ-  n.    —    Pü.:
•  j.  zao^ö.bara-  Adj.  'der  Z.,  Trank- opfer  darbringt':  avat»he  °räi  ar»drai  ya- MsmnUi  jatftyantai  dJ^ri/  (näinl.  aridvi) Syaphm  Ytj.  133;  1$.  i,  20,  *5. 19'',
KompE.  —  Vgl.  6arS.sa<&tä:   —    >)  S.  unlei
•  j.  zao9TÖ.barana-  Adj.  'die  Z.  enthal- tend, aufnehmend"*:  taääi  *°näi  "der Tasse,  die  die  Z.  enthält"  Vr.io. »;  — tasta  'na  J^.66.
Pü. !  lall  i  xSArbaran.  —  0  DST.  ZA.  l.  LXIV sieht  in  laiia-  und  <*  zwei  verschiedene  Kul- luagerätscharten.  Aber  Pü.  hat  beide  Male deutlich  das  relative  i  dazwischen.
•  j.,  g.  zaoya-  Adj.  (fem.  'yä-)  'zu  rufen, der  sich  rufen  lässt,  invocandus',  von  Gott- heiten: yaesqm  *yahliwaca  urvqns  "yäsca
fravalays  Yt.13. 148;  —  fravasayS  .  .  yä
'yd   viriiirir^nyaeiu  Yt.  y.  33'';  23*,  27;
—  yadä  as>m  ztvlm  (NSn.)  *  aahsn  mat'
däüa  akuranhs {^^.  29s  m.)  asicä  Srmain
"wenn  Asa  zu  rufen  und  MAh.  und  die
übrigen  Götter  sich  rufen  lassen  und  Äsay
und  Arm"  Y.31.  4;  —  °yehe  V.  i.  14GL
PFP.    zum   V.  tav-;   vgl.  S   i^S.  13,  21    und
Me[LLET  bei  BCU.  Grdr.'  I.  1091.  —  ai.  häjiya-
Adj.  —  Pü.  {luV.  J/):  ia-alavaÄüt  ^ändär
hänl  u  BArmaaiä  -  Sü.  r  yndi  . .  nimattlraiäh
tmah  ..  -,  erl.:  ium  vehik  I  eldn  iaväl  -  So.: tiläsmäiam  Hllamam  rvam  ailu  —  yam  Öhr- matd  u  aSavahal  brx-an  bavil  i^änd;  (zu  V.  I) : dail(f).  —  ■)  Vgl.  rSt.  RV.  4.  3^  3.  — 1)  Falsch  PlSCHZL  VSt.  /.  44;  i.  IF.  3,  19.
•  j.  zaoyint-  Adj.  (auch  fem.)  'auf  den Ruf  hin  sich  vi&m^jAxad!:  fravasayö ..ya u^rantS  .  .  taxmäntd  yh  'tö  (NP£)  Vt 13.  23.
Komp.  i   *saeyä-  f.    "Ruf    (zum    V,    tav-;     »L hävyä.  f.)+»fl«/.. j.  zao:äaiye:  i.  zav-,
•  j-  (1  g-)  zao5-,  p.dau&-  V.  'Geschmack finden  an  — '.  Fraes.  5  zisus-;  j-Aor.  i daui:  —  PPfP.  Musla-.
'Geschmack,  Gefallen  haben,  finden  an  — (Akk,),  gern  haben,  lieben':  *vays  *suits F.  27  b;  —  tu^ta  F.  20.  a)  D  'Jemanden (Akk.)  liebevoll  behandeln,  ihm  Liebes, Gunst  erweisen':  marfiy<^  hy<^  draujan<^ ahatiy  Ayt^3  ^startä  ahatiy  avaiy  mJ äattitä{2is-Aotyi.,)avaiy  aÄi/rattädiy parsä Bh.4. 14.
mit  ä  'sich  einer  Sache  (Akk.)  zu  er- freuen haben,  erfreuen  können':  ndi^ nmane.baxhm  .  .  näii  framanjm  brä%ra- nqm  ätlsusle  nBit  astö  *huiastim  T.4.3.
uiitjrä  'lieben':  ys janal  an^Jamafum
taxtmm  frasuitim  4*  itsUm  (Sp.  420) Yt./p.4a.
ai.  JMJUflana,  jili}ai,  ju}(äh ;  mp.  dSsltan,  — Pü.  (zu  P.):  u  nc  ki  ..  pa  döiSn  tadSiU  etlit; (tu  F.  30):  drani(?),  (zu  F.  27):  fehlt.  — O  S  Jl5-  2.  Ich  bleibe  dabei  trotz  FoY  KZ. 35.  46.  Wäre  dtastä  hier  das  selbe  Wort vie  Bh.  4.  10,  16,  so  würde  ich  auch  das selbe  Verbum  dabei  e
•  j.,  g.  'zaoäa-  m.  'Gefallen',  uzw.  i)  'Be- lieben, Neigimg;  Wille,  Absicht':  kvqm anu  ultXm  'bmca  yaha  Aa'^aca  fa  'sS V.  2. 1 1 ;  Yt.  75. 8  2 ,  F.  20 ;  — >7. .  altyä  •Shig ustis  i/afVÄÄ^f  (sd.)  kacaitl  Y.  4Ä4;  — %wakmt   hxl  '}e  ^äboxssMai^A^^  ^-SS-
—  Aanarf  (sd.)  %7vaÄmät  '/SJ  Y.  4j.
~  haväi  kamaica  °säila  YL/j.  33;  — :^akmi  °ie  Vr.  J«/.  2 ;  —  larasia  aarahe mainy!ui ..  'Iq  YL/0.118;  — yai  %uiä didva^a..  yai  'sa  yai  aiaosa"..  ahsichüicii oder  unabsichtlich"  Y.  J,  ai,  2)  'Wohl- gefallen' :  /ai  värüi  (sd.)  radmfl  ahurakya •si  mazdi  Y.33.  2; —  'Äfi  ahurahe  matdä 'M  amfsanqm  spmtanqm  YtÄ  35;  — kihrpa  avavatqm  sraya  yaha  dthayatqm ■/i  "von  der  Körperschöne  solcher,   wie
Uiflitizea  by  VjOOQ  IC
1657
'zaoäa-
'zan-  Noten
1658
```


## [2026-09-06T02:15:45.676Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- PHD grep zwt/zot ---\"; grep -n \"zōd\\|zōt\\|zwt\\|^zot\\| zot\\b\" PHD.txt | head; echo \"--- PHD_mackenzie ---\"; grep -n \"zōd\\|zōt\\|zwt\" PHD_mackenzie.txt | head; echo \"--- NYB ---\"; grep -n \"zōt\\|zōd\\|zwt\" NYB_vol2_glossary.txt | head",
 "description": "Grep Pahlavi dicts for zot"
}
```


### [2026-09-06T02:15:45.762Z] TOOL RESULT

```
--- PHD grep zwt/zot ---
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
5078:zūr, zūr zoromand zūrgugāy zūrgugāyīh zorig Zurwün zofāy zofāyīh zofr zofrāy zofr-pāyag zanjīr zanišn zētīh, zūdīh zot, zūd wahīgt ant
--- PHD_mackenzie ---
844:abziidan, abzay- [lpzwtn l , 'pz'd- I M )bz)y-, N afzudan, afzay-] in-
5506:wiziidan [wyzwtn'] = wizistan.
5851:z~t [zwt = Av. zaotar-] first officiating priest.
5859:ziid [zwt l I M zwd, N . . . . ] quick(ly).
--- NYB ---
566:apa-zütan ["pzwtn'], apa-zāyītan [’pz’dy- tn'], apazäy- ['pz?d-], to increase, to augment, pt. = pret. pass. 3d p. sg. apa- züt 109%, apazäyit ['pz'dt'] 925. — < *abi-jav-, in SW with api- substituted for abi- (v. s. v. apa-) < abi-+ Av. (504) !gav- ‘to procure’; MPrth "bgwdn *bg*w- ‘to increase, to add to’, ?bg^w ‘increase’; Arm lw. augut ‘profit’; — OP caus. abi- jävaya- ‘to add’; MPrs pres. ’bzw- intr., ’bz’y- trans. ‘to increase’; Paz. awazūdan awazüed. Henning, A-H III Gloss. s. v. ’bgwdn; Benveniste, JA 228, 1936, 203- 204; Ghilain 76.
1579:Frazišak [Paz.] n. pr. 47*. — BdA p. 230? plzwtk; BdJ 782% Frazušag [Paz.].
4573:zat [zwt'] swift, prompt, quick 74; adv. quickly 181%, 1912. — MPrs zwd; NP zūd.
```


## [2026-09-06T02:16:02.163Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 502 503 504; do echo \"=== leaf $n (printed ~$((n+540))) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -60; done",
 "description": "BQT vol2 around p.1043"
}
```


### [2026-09-06T02:16:03.749Z] TOOL RESULT

```
=== leaf 502 (printed ~1042) ===
   ‫‪ ۵‬اس‬   ‫و‬




 ‫زگله * ‪ -‬بفتح اولوآخ رکهلام باشد‪.‬‬
                                 ‫ن‬                          ‫واکفرا‬
                                                                 ‫میرسد ویحربی رمس میگویند ‪ -‬ز‬
 ‫درا وجلاجل و زنگه را کویند ‪ -‬وهام مبارزی‬                                 ‫نگیفزته‌اند که دستك زن باشد‪.‬‬
 ‫است تورانی که درجن‌گدوازده رخ‌بردست فروهل‬
 ‫ایرانی کشته شد ‪ -‬ونام مقامی‌است از موسیقی‪-‬‬
                                                        ‫نزگان د با کاف فارسی بروزن البان »‬
                                                            ‫وا‬
                                                             ‫در‬‫دم شهرست ما بینقروین و تبآریز‬
‫و بکر اول و الث‪.‬خوشة کوچکیرا گوبند از‬                      ‫آردشیر بابکان‌بنا کرده‌است ومعرب آن زنجان‌است‪.‬‬
 ‫انگورکه جزو خوشة بزر که باشد ؛ وباینمعنی‬
   ‫بجای لام رای بی نقطه (‪ )۱‬هآمده (‪)۲‬است‪.‬‬
 ‫ازآ فتاب‌عالمتاب‌است‬
                    ‫ز تکگلنۀاربوهره‬                                  ‫موسیقی ‪ -‬وتام رودخاله‌ای هم هست‪.‬‬
‫رای قرشت وسکون واو و دال » نام سازیست که کنابه اذزندنیاکوعاولمچ سقلبیاسباتذادن ‪ - .‬بک ار‬
                                                        ‫رنکانه‌رود ‏‪ em‬زنانه معلوم‌است رضم‬


                                                           ‫گان درروز جنکه نوازند ‪ -‬ونام رودخاله‌است‬
                                                                                                    ‫زی‬
 ‫رگو له‪ ۱‬ب=روزن مرغوله ؛ بمعنی‬
                             ‫ن‬                                             ‫که از بپلوی زنگان مبگذرو‪.‬‬
‫زنگله است که جلاجل ‪ -‬و نام بهلوانی باشد‬
                                                        ‫پس دادن ‪۰‬‬      ‫زرتگاهی = با ها پروزن‬
         ‫تورالی ‪ -‬ونام مقامی است از موسیقی‪.‬‬                ‫چیزیت که آنرا بمربی زهفران‌الحدبدمیگویند‬
 ‫رنگه (‪ )۳‬د بنتح اول وثالك و سکون‬
‫ثانی» نام ولابتی‌است ‪ -‬ونام پهلوانی هم بوده که‬          ‫وباآب لمکنند وبرروی صفحه آحنی تنك سازند‬
                      ‫پدر اورا شاوران خوانشد ‪.‬‬          ‫وبگذارندتاخشك شود‪ .‬بمدازآن یکوبند و سر لد ‪۰‬‬

 ‫نزگی دار و ‪ -‬بااات بتحتالیرسیده‪.‬‬
‫دوابی است کهآنرا بعربیمقربان خوانند وآن‬                 ‫تاهمه برنگه زعفران گردد‪.‬طبیعت تاز آن‌سرد‬
 ‫بیخکبر رومی‌است؛وبعضی گوبند لوعی از اسقیل‬             ‫وشك شود و در‬
                                                                  ‫باشد وچون کهنه کردد گرم خ‬
  ‫را‬
   ‫لو‬‫آشد‬
       ‫یند حشثشةالطحال با‬
                        ‫| است؛ وگجمومن‬                                                   ‫قابات بکار برد‬
 ‫حثيثة الدودبه نیز گفته اند و بیوداسی‬                   ‫رنگیار ‪ -‬بروزن کار «دوات‌سیاهی‬
                     ‫اسقولوقندربون ‪ ۷‬خوانند ‪.‬‬                        ‫را کویند ‪ -‬وهام ملکی هم هت ‪۳‬‬

 ‫نرگی مزاج س کنابه ازشضصی باشد‬                             ‫زگباری؟ »بروزن سنگاری»معروف‬
                                                                                     ‫ن‬
 ‫که پبوسته خوشحال است چه زنگیان را طرب‬
                       ‫وخوشحالی ذانی میباشد ‪.‬‬
                                                       ‫است که مردم زار باشد ‪ -‬وصمغی رایز گونه‬

                                                                         ‫صاه که از درخحت صنوی رگیر ند‪.‬‬

 ‫رنمتان = بائای قرشت بروزن قلمدان‪.‬‬                      ‫رنگدان = بر وزن سنکدان ‪ .‬زنگله‬
‫دویوستك دراز را گوشد مانند سرپتان که از‬                                                ‫وجلاجل راکویند ‪۰‬‬
      ‫زمر کلوی کوسفند ویز آوبخته میباشد ‪.‬‬
 ‫صمند ‪ ۰‬بمعئی آراسته‬    ‫ر نند = بروزن‬                      ‫وسکون‌الی ولام » زنکه ودرا وجلاجل‌وزنگلوله‬
                              ‫وآراش باشد ‪.‬‬                                                       ‫را گویند‪.‬‬

   ‫(‪ )۳‬چب‪» ۲‬چش‪:‬ز نگله‪.‬‬               ‫او‬          ‫)<( خم‪۱‬‬               ‫‪ - :‬مى نقطه ‪.‬‬   ‫(‪ )۱‬چك‬
=== leaf 503 (printed ~1043) ===
                                                                                                 ‫—‬    ‫‪64 ۱‬‬   ‫س‬




‫و دیات را همگفته‌اند ‪ -‬وبمعنی ترس و میم حم‬
                                                       ‫رلو » بروزن زلو » جانوری است که‬
   ‫هدیز‬
      ‫راش‬
        ‫پب‬‫وایت‬
             ‫شکوءسوشک‬            ‫نی‬
                                  ‫عو‬‫بتم‪-‬‬
                                       ‫ه‬               ‫و زلو را هم‬            ‫خ‌والند ‪-‬‬   ‫آ را بعر نی ارضه‬
 ‫مرت‬      ‫و اجتناب را نیز گونند ‪ - ۱‬و بمعنی‬                                                   ‫میگوبند ‪٩‬‏ ‪#.‬‬
‫و افوس باشد ‪ -‬و بمعنی شتاب وتعجیل‌هم آمده‬
                                                     ‫ر نور = بروزن تنور » بن خوشة خرما‬
           ‫‪-‬هوش وکآاهی را هم گویند‪.‬‬
                                  ‫است و‬
                                                     ‫باشد ‪ -‬ونامکرم سیاه رنگی هم‌هست کهآ را زلو‬
‫شله دار‬         ‫ارخ‪-‬ای‬
                     ‫ز نهاربخوا‬                                ‫میگوبند » خون از بدن میمکد ‪. ۴‬‬
‫و وأو معدوله ‪ .‬عد کل و پیمان شکن را‬
                                     ‫گویشد ‪.‬‬
                                                       ‫باشد وثالی بواو مجهول رسیده » موبه والسگه‬
‫بیاقطه ‪ .‬امان‬    ‫ت با دال‬   ‫رنهاردار‬
                                                                         ‫راکوبند و پتازی هربر خوانند ‪.‬‬
                    ‫و مهلت دهنده رگاونند ‪. ۷‬‬
                                                       ‫للیودان = بفتح اول بروزن ببویدن‬  ‫ر‬
 ‫نهبادیرر‪-‬زن بیاری ‪ .‬کیرا‬             ‫ز‬                ‫بمعنی زلوبه است که ناله وموبه و زوزه کردن‬
 ‫کونند که شرط وعهد کند وامان ومپلت‌طلبد »‬                                                     ‫سک باشد ‪. ۴‬‬
                      ‫و زهاربان جمم آن است‪.‬‬
                                                     ‫= بکس اول وسکون ثالی و‬                          ‫رز‬
‫‪ -‬بکر اول و سکون ثاتی بر‬          ‫زان‬                ‫های (‪ )۱‬بااف کشیده بروزن بیار » بمعنی امان‬
 ‫وزن بربان » نایشواه را گویند»وآن تخمی است‬             ‫ادلرا لگیوزبند ‪ -‬و در‬‫معه‬
                                                                              ‫‪-‬و‬‫پی‬‫وشد‬
                                                                                    ‫ومهلت با‬
 ‫که برروی خمیر نان پاشند ؛ و با زای‌فارسی‌هم‬           ‫«لهار‬‫مقام تاکیدهم کفته میشرد چنانکه ز‬
                                   ‫آمده ات ‪.‬‬
                                                       ‫شراب نخوری» یمنی البته ضواهی‌خورد ‪-‬وامات‬


                                           ‫هزم‬
                                             ‫بیان شدان‬
                ‫کغتنوات‬
                      ‫در زای نقطه داریا وأو مشتمل بر نجاه و دو ل‬
 ‫خوانند ‏‪ - ٩‬وم اول » مخفف زود است که‬                ‫رو = بفتح اول و سکون انی » نامپسس‬
‫تمجیل وشتاب باشد *‪ -‬ونام ولابتی‌هم هست که‬              ‫طهماسب است که در ابران پنج سال پادشاهی‬
                 ‫آنرا زوزن بروزن سوزن کوبند ‪.‬‬          ‫بحر‬         ‫ی‬‫بو‬
                                                                     ‫رند‬
                                                                       ‫عگوی‬
                                                                          ‫بنیز‬
                                                                             ‫کرد ‪ - ۵‬و دربا را‬
                                          ‫مبگو نشف ‪3‬‬    ‫)<( چش‪:‬‬                   ‫(‪ )۱‬چك ‪ :‬وها ‪.‬‬

                         ‫»رو ‪.‬‬
                             ‫ز‬    ‫زلو‬
                                    ‫زیروك؛‪۰:‬‬
                                           ‫‪۴‬‬                      ‫‪ - ۱‬رك ‪ :‬زلو » زئور » زرو ‪.‬‬
   ‫اسشق ‪ ۰‬هوبشمان‬       ‫‪:‬‬
                        ‫ك‪.‬‬‫ردن‬
=== leaf 504 (printed ~1044) ===
                   ‫وبفتح اول نام داروبی است که‬                  ‫خادم راکوبند عموماً وخادم بیماران وزنداتیانر‬
                  ‫باکر کرد بربهق‌طلا کنندنافع‬
                                                                ‫رات ‪ - ۱‬و زواره برادر رستم زال ‪ -‬وزنده‬
                   ‫باشد و دآرا شلمك وشیلم نیز‬                   ‫وار ند ونر‬          ‫وصدا ر‬      ‫را یز گوبند‬         ‫وزسیات‬
                                   ‫کون ‪: ۷‬‬
                                                                ‫باشد ‪ -‬و زن پیر فرتوت سال خورده را هم‬
                                                                                                           ‫گفته‌اند (‪. )۱‬‬
                  ‫بر وزن و معنی زباله است که‬
                  ‫زبانة آتی و زبانة شاهن ترازو‬                ‫=فتح اول بر وزن هزاره‪ .‬نام‬
                                                                                       ‫رواده ب‬
                                 ‫وامثال آن باشد ‪۰‬‬               ‫برادر رتم زال است ‪ -‬و نام قصبه‌ای همرت‬
                                                                        ‫از عراق در توابع‌کاشان که او بکنراده‌است‪.‬‬
‫رواووق ‏‪ = ٩‬پا واو و قاف بر «زن‬
‫جیوه است‬     ‫باشد که‬       ‫‪a‬‏ بمعنی زاووق‬    ‫صماروع‬             ‫رواغار = با غین قطه‌دار (‪ )۲‬بر وزن‬

‫بزبان ارباب عمل که کیمیا گرانند وعربان زیبق‬                     ‫در‬
                                                                 ‫معلوم؟ = و‬           ‫غر‬     ‫است‪.‬‬     ‫حوادار ‪ ۰.‬بام مرعی‬

                                            ‫خوانند ‪.‬‬            ‫مۇبدالفضلا میگوبد دام مفی است یعنی آتش‬
‫رواه ‌ نکن اول بروزن سناه "طعامی‬                                                                                  ‫پرسنی ‪. ۴‬‬

                                                                ‫آرد خمیر کرده راکوند که بمقدار بك ته بان‬
                           ‫از کل بمقدارفندقی‪٩٩‬‏ ‪.‬‬               ‫کمان گروحه را یز‬              ‫و مپرء‬       ‫ساخنه باشند ‪-‬‬

‫رو با"‪ -۷‬بااول بثالی رسیده و بای‬                                ‫‪6‬‬        ‫زندتی‬
                                                                             ‫راف‬
                                                                               ‫ااشد‬
                                                                                  ‫دی‌ب‬
                                                                                     ‫قه‌ا‬
                                                                                        ‫بنمکلول‬
                                                                                              ‫‌‪.‬وآ‬
                                                                                                 ‫لاند‬
                                                                                                    ‫کته‌‬
                                                                                                       ‫کف‬
                                                              ‫که‬        ‫را یز کوند‬     ‫دراز‬    ‫مالِدة‬     ‫خمیریارهای‬   ‫و‬    ‫ت‬
‫أ جف بالف کشده ‪ ۰‬بلفت زند و ماز ند )‪ (۳‬دزد‬

                ‫وراهزن وقطاع‌الطربق راگوبند ‪.‬‬                   ‫بجهت بغرا مهباکنند » و بعضی کوبند طمامی‬
                                                                                      ‫است که بعربی فرزدقه خوانند‪.‬‬
‫بضم اول و سکون انی (‪)4‬‬           ‫زو باع‬
‫وبای انجد(ه) بالف کشیده ویغین نقطه‌دار رده »نام‬                 ‫روان = بفتح اول » بروزن ومعنی‌زبان‬

       ‫(‪)۳‬چك ‪ :‬ژند ویاژند ‪.‬‬          ‫دار ‪۰‬‬    ‫بهطه‬       ‫‪—:‬‬   ‫( )جك‬                   ‫(‪)۱‬چش ‪ :‬میگوبند‬
                                                 ‫‪ :‬وبا ‪۰‬‬      ‫‏(‪ )e‬چك‬                 ‫(‪ )4‬چك ‪ - :‬ثانی ‪.‬‬
           ‫برده با خویشتن بجمله براه ‪.‬‬                                      ‫‪ - ۱‬دیان داشت بی زوار و یناه‬
  ‫عنصری بلخی‪«.‬لفت قرس ‪۰۳۱٩‬‏ ‪.‬‬
  ‫‪ -‬ظ«مرغ» مصحف هع * است کهدرجملهةٌ مدمو لفن کر کرده‪.‬‬                                        ‫رك‪ :‬زواره‪.‬‬       ‫‪-‬‬

                                                                                       ‫رك ‪ :‬ژواغار ‪.‬‬          ‫‪۴‬‬
      ‫زحلق‌مرخ‌باعت فروچکیدی گل(خون‪.‬دهشدا)‪.‬‬                     ‫® ‪ -‬زواله‌اش‌چوشدی‌از کمانگروهه‌برون‬
  ‫‪۲‬‬    ‫«لفت فرس‪٩۳۰۵‬‏‬   ‫کسایی مروزی‪.‬‬

                ‫‪( ]612۲۷ = ۷‬فر) «لك ‪۲‬س ‪. )۵۲۲‬‬                                   ‫‪.‬‬     ‫فنا»ن‬
                                                                                          ‫زبا‬
                                                                                            ‫‪ ۷‬رك ‪ :‬ز‬
  ‫‪۰‬‬     ‫‪ °‬رك‪ :‬لفت فرس ص‪41‬‬                     ‫رك‪ :‬زاووق‪. ‎‬‬              ‫‪٩‬‬            ‫زیانه (ه‪.‬م‪‌ ).‬‬       ‫ص‬   ‫‪۸‬‬

           ‫«رواله» (هم‪).‬‬    ‫‪ -‬ظ ‪ ,‬مسحف‬       ‫‪۱‬‬       ‫‪۰‬‬    ‫‪۰۳۱‬‬       ‫ص‬   ‫‪ ۶‬زوار» است ‪ .‬رك‪ :‬لفت فری‬             ‫مصحف‬     ‫وظ‬

      ‫‪۴‬هز‪ .20۵2,20012 .‬بپلوی ‪ 012111‬دزد« بودکر‪ ۸۰۱‬قراتمجاغلیط‪«2068‬رهارله‪.*۲۵۲‬‬
```


## [2026-09-06T02:16:13.655Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==506' BQT_v2_pages.txt | head -70",
 "description": "BQT vol2 leaf 505"
}
```


### [2026-09-06T02:16:15.561Z] TOOL RESULT

```
  ‫زورق‬                                                                                                    ‫ت‬
                                                                                                          ‫اع‬‫سم‬
 ‫زود خیز‪ -‬زود مملوم است » با خای‬                            ‫کسی‌است که حیزی و مخنشی را اوبنانهاد و ازو‬
‫نقطمدار بتحتاتی‌رسیده ویزای اقطهدار زده‪ ,‬کنابه‬                                                   ‫رانیده شد ‪۱‬‬

                  ‫از فرمانبردار وخدمتکار باشد‪.‬‬              ‫رو به = صم اول وفتح مای‌فارسی‪ .‬بلفت‬
‫زود سبره کنابه کایز‌است که از‬                                ‫نزدوپازند(‪)۱‬؛به‌عنی‌قرض بباشید‌ودبعنر‌خوانند‪.‬‬
             ‫زودسر شود ودلگر کردد‪.‬‬         ‫صصت‬
                                                            ‫‪ = ۴‬با ثالی مجپول‌وبای‌فارسی‬         ‫دون‬
                                                            ‫‪ ۰‬حربة مردم گیلان است» وان‬           ‫بر ورن چوبین‬
                        ‫وصاحب جمعیت باشد ‪.‬‬                  ‫ران دوشاخ باشد و در‬          ‫کده‬
                                                                                           ‫نیز کوچکی بو‬
 ‫رور = بفتح‌اولوثانی بروزن نظرءیمعنی‬                        ‫و نام سرکاوی‬    ‫‪-‬‬   ‫فدرم بدان جنگ مکرده‌اند‬


‫زبر است ‪ ۱‬که بالا باشد چه درفارسی بای ابجد‬                                                            ‫‪.‬‬   ‫هم هت‬


                  ‫و واو بهم تبدیل مییابند ‪. ۷‬‬               ‫روخ ‪ - ۴‬بروزن شوخ ‪ .‬کوشت‌پاره‌ای‬
‫رورا = بفتح اول وسکون انی و وای‬                             ‫که بر تن مردم بروید و آن را بسربی ولول‬
‫کشده ‪ ۳‬دح له بغداد ‪۳‬‬       ‫(( بالف‬      ‫بی نقطه‬                                                       ‫خوانند ‪۲#.‬‬
‫کوبندو بعضیکوبند زورا‪,‬فداداست وعربی‌است‪. ۷‬‬                  ‫دواشنا ؟ ‪ -‬باشین نقطه‌دار ونون بر‬‫‪ ۱‬ز‬
‫رورانه* = فبتحر‌وآوزلن‌همخانه‪ ,‬بندی‬                         ‫وزن زود ار جا » نذر و نذوراتیرا کونند که‬
          ‫باشد آهنین که بر پای بندبان گذارند‪.‬‬                                   ‫خاتها اور لد ِ‬    ‫فارسان بش‬


‫زودفین ‪ ۳‬با فا بر وزن دوربین ‪.‬‬                              ‫رود‪۵‬اندار * ‪-‬زود معلوم است »‬
                                                            ‫باهمزة مفتوح و نون ساکن و دال بی‌نقطه‬
‫چارچوب در وصندوق وامتال آن زلند وزنسصر بر‬                   ‫بالف کشیده و بزای نقطه‌دار زده › لففای است‬
                      ‫آن اندازند وقفل کنند ‪.‬‬            ‫که حربی بدیپه گوبند و تفیر آن سخن بی‬
 ‫رورگ = بفتح اولونالك وسکون قاف»‬                                                                  ‫اندیشه است‪.‬‬

                                 ‫‪.‬‬   ‫بی نقطه‬   ‫‪-‬‬   ‫‪:‬‬   ‫چك‬     ‫(‪)۲‬‬           ‫(‪ )۱‬چك زد ویاژند‬
         ‫ژوبن = ژوین ‪٠‬‏ رك ‪ :‬اسشق ‪. ۹۸۱‬‬                ‫‪-‬‬‫‪۴‬‬           ‫‪.‬‬   ‫رك ‪ :‬لغت فرس ‪۶ ۲‬‬          ‫‪۱‬‬


   ‫‪ - ۴‬جزو اول کلمه رقاای پورداود «زور»‬                       ‫رك ‪:‬رح ‪ ۰‬رخ »آزخ ‪ ۰‬آژخ‬              ‫‪۳‬‬

   ‫بفتح اول(اوستا‪ )2]211022‬دانندبمعنی آب مقدس که درجشنهای‌زردشتیان بکارروده وشابد جزودوم‬
    ‫® ‪ -‬ازدساتیر«فرهنك دساتیر ‪۹۶۲‬‬          ‫مصحف «اشتنام» (دعایی که دارسممر‌زورخوانند) باشد‪.‬‬
   ‫‪ - ۷‬زور (درزبان کتولی‌بض‌اول ودرقدیم با واومجهول) پهلوی‬                        ‫‪ - ۱‬رك ‪ :‬زر ‪.‬‬
  ‫(قوت) ‪ .‬از اوستا ‪ ( 12۷82-‬قوت) « بارنولمه ‪ ۹۸5۱۰‬آرمنی ع تلا‪ 22‬دیبرک ‪»۵۲۷‬‬                                   ‫‪۲‬‬
                            ‫توالابی ‪:‬‬    ‫در فارسی « زاور؟ («‪.‬م‪ ).‬بهمن معنئی آمده ؛ قوت » نبرو ‏‬
         ‫«کلتان ‪. ۸4‬‬           ‫با خداوند غيب دان لرود ‪.‬‬                    ‫زورت ار بیش مهرود با ما‬
                                       ‫مرجم البلدان *زوراء » نام بفداد است ‪.‬‬     ‫‪-‬د‬
                                                                                  ‫‪ ۸‬م‬
                              ‫‪ °‬رك ‪ :‬زلفن ‪.‬‬             ‫زولانه ‪ .‬ورك ‪ :‬زاولاله ‪.‬‬    ‫‏‪٩‬‬
   ‫©ود ‪ -‬نم اول ‪ .‬پهلوی )‪( 002‬تند؛ سریم ) «ییب که ‪« ۷۵۲۰‬تاوادیا ‪> ۲ :۷۹۱‬‬
                                                                       ‫ز‬
   ‫پازند ‪402۰‬ساسکرت ‪ » [40 -‬اوستا و بارسی باستان ‪* 2000-2‬‏ کردی ‪ , 02‬بلوچی)‪»02‬‬
    ‫‪ 6‬و‪ « 1412‬اسشق و هوبشمان ‪ . ۳۷۰‬اورامالی نات د ‪ .‬اورامان ‪ ۰ ۸۲۱‬شهمیرزادی ‪02‬‬
      ‫‪.-‬‬
       ‫را‬‫وعت‬
           ‫فبسر‬
              ‫دکه‪۰ ۹۹۱ ».‬ک‪۰‬یلکی ‪ 002‬؛ تند ت»یز ‪ ۰ .‬سریم » جلد ‪ -‬بشتاب »‬
```


## [2026-09-06T02:16:39.936Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==504' BQT_v2_pages.txt | tail -25; echo \"=====LEAF504=====\"; awk 'BEGIN{RS=\"\\f\"} NR==505' BQT_v2_pages.txt | tail -25",
 "description": "Footnotes of BQT leaves 503-504"
}
```


### [2026-09-06T02:16:41.519Z] TOOL RESULT

```
                         ‫»رو ‪.‬‬
                             ‫ز‬    ‫زلو‬
                                    ‫زیروك؛‪۰:‬‬
                                           ‫‪۴‬‬                      ‫‪ - ۱‬رك ‪ :‬زلو » زئور » زرو ‪.‬‬
   ‫اسشق ‪ ۰‬هوبشمان‬       ‫‪:‬‬
                        ‫ك‪.‬‬‫ردن‬
                            ‫‪ = ۴‬زو‬              ‫‪ - ۳‬اسم مصدر از « زرلوددن ‪( ¢‬ه‪.‬م‪۰ ).‬‬

                ‫‪ ۲‬؛در تاح‌المصادر بهقی آمده ‪« :‬هربر » زلوبیدن» (از افادات علامه دعشدا) ‪.‬‬
  ‫‪ - ۱‬درمقام تحذیر ‪:‬زنههار تابدین طمع گرد‬                        ‫‪ 3‬زنهار» («‪.‬م‪).‬‬       ‫مضفف‬      ‫‪۵‬‬

                                  ‫ولر انات دار نده ‪۰‬‬         ‫‪۷‬‬           ‫‪۰.‬‬   ‫‪۱‬‬   ‫‪۴‬‬   ‫ولع بگردی» «کلتان‬

          ‫‪٩۸‬‏ ‪. °‬‬   ‫ی ستها ‪۲‬ص‬   ‫) لخة باری کننده) از بادشاهان بیشدادی سر توماسب ‪apsãmuT‬‏‬

                                                 ‫‪ :‬زود ‪.‬‬     ‫رك‬     ‫‪ - ٩‬رك ‪ :‬ژو‪. ‎‬‬
                                                                     ‫‪°‬‬


                                  ‫؛ رك ‪ :‬زلوییدن ‪.‬‬      ‫رم‬
                                                         ‫اتح‬
                                                           ‫چلهوف‬
                                                               ‫‪-‬کسر او‬‫‪#‬ز لودی ب‬

=====LEAF504=====

                ‫وراهزن وقطاع‌الطربق راگوبند ‪.‬‬                   ‫بجهت بغرا مهباکنند » و بعضی کوبند طمامی‬
                                                                                      ‫است که بعربی فرزدقه خوانند‪.‬‬
‫بضم اول و سکون انی (‪)4‬‬           ‫زو باع‬
‫وبای انجد(ه) بالف کشیده ویغین نقطه‌دار رده »نام‬                 ‫روان = بفتح اول » بروزن ومعنی‌زبان‬

       ‫(‪)۳‬چك ‪ :‬ژند ویاژند ‪.‬‬          ‫دار ‪۰‬‬    ‫بهطه‬       ‫‪—:‬‬   ‫( )جك‬                   ‫(‪)۱‬چش ‪ :‬میگوبند‬
                                                 ‫‪ :‬وبا ‪۰‬‬      ‫‏(‪ )e‬چك‬                 ‫(‪ )4‬چك ‪ - :‬ثانی ‪.‬‬
           ‫برده با خویشتن بجمله براه ‪.‬‬                                      ‫‪ - ۱‬دیان داشت بی زوار و یناه‬
  ‫عنصری بلخی‪«.‬لفت قرس ‪۰۳۱٩‬‏ ‪.‬‬
  ‫‪ -‬ظ«مرغ» مصحف هع * است کهدرجملهةٌ مدمو لفن کر کرده‪.‬‬                                        ‫رك‪ :‬زواره‪.‬‬       ‫‪-‬‬

                                                                                       ‫رك ‪ :‬ژواغار ‪.‬‬          ‫‪۴‬‬
      ‫زحلق‌مرخ‌باعت فروچکیدی گل(خون‪.‬دهشدا)‪.‬‬                     ‫® ‪ -‬زواله‌اش‌چوشدی‌از کمانگروهه‌برون‬
  ‫‪۲‬‬    ‫«لفت فرس‪٩۳۰۵‬‏‬   ‫کسایی مروزی‪.‬‬

                ‫‪( ]612۲۷ = ۷‬فر) «لك ‪۲‬س ‪. )۵۲۲‬‬                                   ‫‪.‬‬     ‫فنا»ن‬
                                                                                          ‫زبا‬
                                                                                            ‫‪ ۷‬رك ‪ :‬ز‬
  ‫‪۰‬‬     ‫‪ °‬رك‪ :‬لفت فرس ص‪41‬‬                     ‫رك‪ :‬زاووق‪. ‎‬‬              ‫‪٩‬‬            ‫زیانه (ه‪.‬م‪‌ ).‬‬       ‫ص‬   ‫‪۸‬‬

           ‫«رواله» (هم‪).‬‬    ‫‪ -‬ظ ‪ ,‬مسحف‬       ‫‪۱‬‬       ‫‪۰‬‬    ‫‪۰۳۱‬‬       ‫ص‬   ‫‪ ۶‬زوار» است ‪ .‬رك‪ :‬لفت فری‬             ‫مصحف‬     ‫وظ‬

      ‫‪۴‬هز‪ .20۵2,20012 .‬بپلوی ‪ 012111‬دزد« بودکر‪ ۸۰۱‬قراتمجاغلیط‪«2068‬رهارله‪.*۲۵۲‬‬
```


## [2026-09-06T02:16:54.930Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"alchemy\" KLN_1966.txt | head -10; echo \"---1971---\"; grep -n \"alchemy\" KLN_1971.txt | head -10",
 "description": "Grep Klein for alchemy"
}
```


### [2026-09-06T02:16:55.004Z] TOOL RESULT

```
2129:Alcestis,  n.,  wife  of  Admetus,  one  of  the  Argo¬ nauts  ;  she  offered  her  life  for  her  husband  but was  rescued  from  the  lower  world  by  Heracles (Greek  mythol.)  —  L.  Alcestis,  fr.  Gk.  ’'AXxy)<m;, lit.  ‘valiant,  courageous’,  fr.  d Xxtj,  ‘protection, help,  strength,  power,  courage’.  See  Alexander, alchemist,  n.  —  OF.  alqemiste  (F.  alchimiste),  fr. alqemie.  See  alchemy  and  -ist.
2130:Alchemilla,  n.,  a  genus  of  plants  of  the  rose  family ; the  lady’s-mantle  (bot.).  —  ModL.,  fr.  Port. alchimelech,  fr.  Arab,  iklil  al-mdlik,  ‘the  crown of  the  king’.  The  first  element  is  prob.  a  loan word  fr.  Aram.  kelil,  kllild,  ‘crown’.  For  the second  element  see  malik,  Mameluke, alchemy,  n.  medieval  chemistry.  —  OF.  alquemie (13th  cent.),  alchimie  (14th  cent.)  (F.  alchimie), fr.  ML.  alchemia,  fr.  Arab,  al-kimiyd,  fr.  al-, "the’,  and  MGk.  yr(uda,  a,  prop,  ’the  art of  the  black  land  (Egypt)’,  fr.  Gk.  Xrjuta,  ‘Black- land,  Egypt’,  fr.  Egypt,  khem,  khame,  ‘black’. The  derivation  from  Gk.  x'JireiS,  ‘pouring’, from  the  stem  of  y_£e iv,  ‘to  pour’,  is  folk  ety¬ mology.  See  W.  Muss-Amolt,  Transactions  of the  American  Philological  Association,  vol.
4294:yawn’,  which  also  derive  fr.  VL.  bataeulare,  and see  bay,  ‘part  in  the  wall’, bain-marie,  n.  double  pan  for  holding  food.  — F.,  ‘water  bath’,  fr.  ML.  balneum  Mariae,  lit. ‘bath  of  Mary  (sister  of  Moses)’,  to  whom  var¬ ious  works  dealing  with  alchemy  were  attributed. See  balneal.
7329:Derivative:  chelonian,  a  tortoise,  turtle, chemic,  adj.  —  See  alchemy  and  -ic  and  cp. chemist.  Derivatives:  chemic-al,  adj.  and  n., chemic-al-  ize,  tr.  v.,  chemic-al-ly,  adv. chemico-,  combining  form  meaning  ‘chemically, in  connection  with  chemistry’.  —  Formed  fr. chemic.
7333:chemist,  n.  —  F.  chimiste,  fr.  chimie,  ‘chemistry’. See  alchemy  and  -ist.  Derivative:  chemist-ry,  n. chemo-,  combining  form  denoting  relation  to chemical  actions  or  chemicals.  —  See  chemic. chemosis,  n.,  swelling  of  the  conjunctiva  (med.)  — Medical  L.,  fr.  Gk.  yfioiaic,  ‘affection  of  the eye  in  which  the  cornea  swells  like  a  cockle¬ shell’,  fr.  yj],u. r],  ‘a  yawning,  gaping:  cockleshell’, which  is  rel.  to  yatvsiv,  ‘to  yawn,  gape’;  fr. I.-E.  base  *ghei-,  *ghi-,  ‘to  gape,  yawn’.  See chaos  and  -osis  and  cp.  chela,  ‘claw’, chemotherapy,  n.,  —  Coined  by  the  Jewish  bac¬ teriologist  and  chemist  Paul  Ehrlich  (1854-1915) fr.  chemo-  and  therapy.
7385:chiastolite,  n.,  a  variety  of  andalusite  (mineral.) —  Compounded  of  Gk.  yla.a'coc,  (see  prec. word)  and  Xt&o;,  ‘stone’.  See  -life,  litho-. chiaus,  n.,  a  Turkish  messenger.  —  Turk,  chd- wush,  chaush.  See  chouse, chiave,  n.,  clef  (music).  —  It.,  ‘key’,  fr.  L.  clavem, acc.  of  clavis,  ‘key’,  whence  also  F.  clef,  ‘key’. See  clavicle  and  cp.  clef,  conclave, chibouk,  chibouque,  n.,  a  Turkish  tobacco pipe.  —  F.  chibouque,  fr.  Turk,  chubuq,  chibuq, ‘pipe’,  prop,  meaning  ‘stick,  staff,  tube’,  and rel.  to  chub,  ‘stick,  staff’, chibrit,  n.,  elemental  mercury  supposed  to  pro¬ duce  metals  (alchemy).  —  Arab,  chibrtt,  ‘sulfur’, rel.  to  Heb.  gophrith,  Jewish-Aram.  guphrithd, kubhrithd,  Christ.-Palest.  Aram,  guphri,  Syr. kebhrithd,  Akkad,  kupritu,  ‘brimstone,  sulfur’, chic,  n.,  style,  elegance.  —  F.,  prob.  fr.  G.  Schick, ‘fitness,  tact,  skill’,  fr.  MHG.  schicken,  ‘to  ar¬ range,  set  in  order’,  whence  G.  schicken,  ‘to send',  Geschick,  ‘fitness,  aptness,  fate,  destiny’, Schicksal,  Schickung,  ‘fate,  destiny’. Derivatives:  chic,  adj.  and  tr.  v.
16012:geocronite,  n.,  a  lead  antimony  sulfide  (mineral.) — -  Compounded  of  geo-,  Gk.  Kpovo;,  ‘Cronus’ — here  used  in  its  alchemistic  sense  ‘lead’ — and subst.  suff.  -ite.  Cp.  Saturn ,  which  is  the  Roman equivalent  of  Cronus  and  is  used  in  alchemy  in the  same  sense,  and  see  Cronus.
23017:martite,  n.,  ferric  oxide  (mineral.)  —  Formed with  subst.  suff.  -ite.  fr.  L.  Mars,  gen.  Martis, the  Roman  god  of  war,  whose  name  was  used  in alchemy  as  the  symbol  of  iron.  For  the  ending see  subst.  suff.  -ite.
23484:Derivative:  menstruat-ion,  n. menstruous,  adj.,  pertaining  to,  or  having,  the menses.  —  L.  menstruus;  see  menstrual.  For  E. -ous,  as  equivalent  to  L.  -us,  see  -ous. menstruum,  n.,  a  liquid  dissolving  a  solid  body (originally  a  term  of  alchemy).  —  ML.,  prop, neut.  of  L.  menstruus,  ‘monthly’.  See  menstrual, mensurable,  adj.  —  Late  L.  mensitrabilis,  ‘that which  can  be  measured’,  fr.  mensurare,  ‘to  meas¬ ure’,  fr.  L.  mensura.  See  measure  and  -able  and cp.  measurable.
33814:Satureia,  n.,  a  genus  of  plants,  the  savory  (hot.) —  L.  satureia,  ‘the  savory',  a  foreign  word. Saturn,  n.,  1)  the  god  of  agriculture  in  Roman mythology;  identified  later  with  the  Greek Kpovo?;  2)  name  of  a  planet;  3)  (in  alchemy) lead.  —  L.  Saturnus,  a  word  of  Etruscan  origin. The  usual  derivation  of  Saturnus,  as  ‘the  god  of sowing’,  fr.  L.  serere,  pp.  satus,  ‘to  sow’,  is  er¬ roneous;  it  is  due  to  folk  etymology. Derivatives:  Saturn-al,  Saturn-ian,  Saturn-ic, adjs.,  saturnine  (q.v.),  saturnism  (q.v.) Saturnalia,  n.  pi.,  the  yearly  festival  of  Saturn  in Roman  religion.  —  L.  Saturnalia,  prop,  subst. use  of  the  pi.  of  Saturnale,  neut.  of  the  adjective
---1971---
10624:alqemie. See alchemy and -ist. 
10632:alchemy, n. medieval chemistry. — OF. alquemie 
24948:ious works dealing with alchemy were attributed. 
44799:chemic, adj. — See alchemy and -ic and cp. 
44827:See alchemy and -ist. Derivative: chemist-ry , n. 
45087:duce metals (alchemy). — Arab, chibrft, ‘sulfur’, 
101650:equivalent of Cronus and is used in alchemy in 
145856:alchemy as the symbol of iron. For the ending 
148972:(originally a term of alchemy). — ML., prop, 
213147:Kp6vo<;; 2) name of a planet; 3) (in alchemy)
```


## [2026-09-06T02:17:24.801Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"geyser\" \"^gust\" \"ingot\" \"nugget\" \"funnel\" \"fuse,\"; do echo \"=== $w ===\"; grep -n \"$w\" KLN_1966.txt | head -3; done",
 "description": "Grep Klein for Germanic derivatives"
}
```


### [2026-09-06T02:17:26.274Z] TOOL RESULT

```
=== geyser ===
15274:found,  tr.  v.,  to  cast.  —  F.  fondre,  fr.  L.  fundere, ‘to  pour,  melt’,  fr.  I.-E.  base  *ghu-d-,  ‘to  pour’, whence  also  Goth,  giutan,  OS.  giotan,  OFris. giata,  OE.  geotan,  OHG.  giotan,  MHG.  giegen, G.  giefien,  ON.  gjota,  Swed.  gjuta,  Tt&n.gyde,  ‘to pour’;  cp.  ingot,  and  gut.  Base  *§hu-d-,  is  a  -d- enlargement  of  base  *ghu-,  ‘to  pour’,  for  the derivatives  of  which  see  chyle.  Cp.  circumfuse, confound,  confuse,  diffuse,  effuse,  funnel,  fusel  oil, fusible,  fusion,  futile,  infundibulum,  infuse,  in¬ fusion,  interfuse,  profuse,  refound,  refund,  refuse, ruse,  rush,  v.,  transfuse.  Cp.  also  geyser, found,  adj.,  provided,  equipped,  with.  —  Prop, pp.  of  find.
16094:geyser,  n.  —  Icel.  Geysir,  name  of  a  geyser  in Iceland,  lit.  meaning  ‘the  gusher’,  fr.  geysa,  ‘to gush’,  which  is  rel.  to  ON.  gjosa,  ‘to  gush*,  freq. of  gjota,  ‘to  pour’.  See  found,  ‘to  cast’,  and  cp. gust,  ‘blast  of  wind’.
16095:Derivatives:  geyser-ic,  adj.,  geyserite  (q.v.) geyserite,  n.,  a  variety  of  opal  ( mineral .)  — Formed  fr.  prec.  word  with  subst.  suff.  -ite. gharry,  gharri,  garry,  n.,  cart,  carriage  ( Anglo- Indian ).  —  Hind.  gari.
=== ^gust ===
16893:gust,  n.,  a  sudden  blast  of  wind.  —  ON.  gustr, ‘gust,  blast’,  formed  with  suff.  -t  from  gus-, weak  grade  of  gjosa,  ‘to  gush’.  See  geyser. Derivatives:  gustful  (q.v.),  gust-y,  adj.,  gusti-ly, adv.,  gust-i-ness,  n.
16894:gust,  n.,  relish.  —  L.  gustus,  ‘tasting,  taste’.  See choose  and  cp.  gout,  gustation,  gusto,  degust, disgust,  ageustia,  ragout.
16896:gustative,  adj.,  pertaining  to  the  sense  of  taste. Formed  with  suff.  -ive  fr.  L.  gustatus,  pp.  of gustare.  See  gustation.
=== ingot ===
5840:bulletin,  n.  —  F.,  fr.  It.  bullettino,  dimin.  of  bulla, ‘an  edict  of  the  pope’.  See  bull,  ‘edict’, bullion,  n.,  uncoined  gold  or  silver.  —  Du.  buli- oen,  ‘alloy  of  gold  and  silver’,  fr.  F.  billon,  ‘lump, ingot,  alloy  of  silver  with  a  preponderating amount  of  copper’,  fr.  bille,  ‘block  of  wood’. See  billet,  ‘a  stick’.
15274:found,  tr.  v.,  to  cast.  —  F.  fondre,  fr.  L.  fundere, ‘to  pour,  melt’,  fr.  I.-E.  base  *ghu-d-,  ‘to  pour’, whence  also  Goth,  giutan,  OS.  giotan,  OFris. giata,  OE.  geotan,  OHG.  giotan,  MHG.  giegen, G.  giefien,  ON.  gjota,  Swed.  gjuta,  Tt&n.gyde,  ‘to pour’;  cp.  ingot,  and  gut.  Base  *§hu-d-,  is  a  -d- enlargement  of  base  *ghu-,  ‘to  pour’,  for  the derivatives  of  which  see  chyle.  Cp.  circumfuse, confound,  confuse,  diffuse,  effuse,  funnel,  fusel  oil, fusible,  fusion,  futile,  infundibulum,  infuse,  in¬ fusion,  interfuse,  profuse,  refound,  refund,  refuse, ruse,  rush,  v.,  transfuse.  Cp.  also  geyser, found,  adj.,  provided,  equipped,  with.  —  Prop, pp.  of  find.
18717:Derivatives :  illaudabl-y,  adv. ille,  pron.,  that  one,  he.  —  L.,  altered — prob. under  the  influence  of  is,  ‘he’,  iste,  ‘this,  that’ — fr.  OL.  ollus,  olle,  ‘that  one,  he’,  which  is  rel. to  Oscan  utleis,  ‘his’  (corresponding  to  L.  illius, gen.  of  ille),  and  to  L.  ol-im,  ‘formerly’,  ul-tra, ‘on  the  other  side,  beyond’,  prob.  also  to  al-ius, ‘another’,  and  cogn.  with  OSlav.  lani,  Czech loni,  Pol  loni  (for  *olnei),  ‘last  year’  (lit.  ‘in that  year’),  OIr.  oil,  ‘large,  wide,  ample’,  lit. ‘beyond  (measure)’.  The  personal  pronouns: It.  egli,  ella,  ‘he,  she’,  Rum.  el,  ea,  Proven?,  el, ila,  F.  il,  elle,  Catal.  ell,  ella ,  Sp.  el,  ella.  Port. elle,  ella,  ‘he,  she’,  and  the  defin.  articles:  It. il,  lo,  la,  Rum.  -le,  Proven?,  to,  to,  to,  F.  to,  to, Sp.  el,  lo,  la.  Port,  o,  a,  ‘the’,  all  derive  fr.  L.  ille, ‘he’,  resp.  ilia,  ‘she’.  See  else,  ultra  and  cp.  a  la, alarm,  alfresco,  Algernon,  alligator,  al  segno, dal  segno,  del  credere,  El  Dorado,  lagniappe, langue  d’oil,  lierre,  lingot,  louver,  postil, illegal,  adj.  —  F.  illegal ,  fr.  ML.  illegalis,  ‘un¬ lawful,  illegal’,  which  is  formed  fr.  in-,  ‘not’, and  L.  legalis,  ‘pertaining  to  law,  legal’.  See legal.
=== nugget ===
25746:nugget,  n.,  a  lump  of  metal;  esp.  a  lump  of  gold. —  For  niggot  (so  spelled  in  North’s  Plutarch), fr.  a  niggot,  misdivision  and  corruption  of  an ingot.  See  ingot.
=== funnel ===
7484:choana,  n.,  a  funnel-shaped  opening  (anal.)  — Medical  L.,fr.Gk.  yoavr, ‘funnel,  funnel-shaped hollow  in  the  brain’,  a  derivative  of  yofj,  ‘a  pour¬ ing  out’,  from  the  stem  of  ysiv,  ’to  pour’,  which is  cogn.  with  L.  fundere,  ‘to  pour’.  See  found, ‘to  cast’,  and  cp.  chyle.  Cp.  also  the  first  element in  chonolith.
7642:Derivatives:  chute,  tr.  and  intr.  v.,  chut-er,  n. chutney,  n.,  a  strong  pickle.  —  Hind,  chatni. chyle,  n.,  fluid  formed  from  the  chyme  in  the small  intestine(p/!  w/o/.) — LateL.  chylus,  fr.  Gk. yfiXoc,,  ‘juice’,  from  the  stem  of  yew,  ‘to  pour’, whence  also  xufl-<k>  ‘juice’,  yyaiq,  ‘effusion’, yuTpa,  y'jTpoT.  ‘earthen  pot’,  yjT/.ov,  ‘a  liquid’ (lit.  ‘anything  that  may  be  poured’),  yfiS vjv,  ‘in a  stream’,  yor\,  ‘a  pouring  out’,  yoi-rt),  ‘funnel’, yuwuvat,  ‘to  throw  up,  heap  up’,  fr.  base  yu-, corresponding  to  I.-E.  base  *ghu-,  *gheu-,  ‘to pour’,  whence  OI.  ju-hdti,  ju-hutc,  ‘pours  into the  fire,  sacrifices’,  hdtar,  ‘sacrificer,  priest’, hitrah,  ‘offering,  oblation’.  Arm.  joyl,  ‘poured’, jew,  ‘form,  figure’,  h.fiitis,  ‘a  water  vessel,  pit¬ cher’,  Jutilis,  ‘that  pours  out  easily;  vain,  futile’. Cp.  chyme.  Cp.  also  choana,  chonolith,  chytra, chytridium,  diachylon,  ecchymosis,  synchytrium, urachus.  For  base  *ghu-d-,  *gheu-d-,  a  -d-e n- largement  of  the  above  base,  see  found,  ‘to  cast’, and  cp.  words  there  referred  to. chyli-,  combining  form  meaning  ‘pertaining  to chyle’.  —  See  chylo-.
15274:found,  tr.  v.,  to  cast.  —  F.  fondre,  fr.  L.  fundere, ‘to  pour,  melt’,  fr.  I.-E.  base  *ghu-d-,  ‘to  pour’, whence  also  Goth,  giutan,  OS.  giotan,  OFris. giata,  OE.  geotan,  OHG.  giotan,  MHG.  giegen, G.  giefien,  ON.  gjota,  Swed.  gjuta,  Tt&n.gyde,  ‘to pour’;  cp.  ingot,  and  gut.  Base  *§hu-d-,  is  a  -d- enlargement  of  base  *ghu-,  ‘to  pour’,  for  the derivatives  of  which  see  chyle.  Cp.  circumfuse, confound,  confuse,  diffuse,  effuse,  funnel,  fusel  oil, fusible,  fusion,  futile,  infundibulum,  infuse,  in¬ fusion,  interfuse,  profuse,  refound,  refund,  refuse, ruse,  rush,  v.,  transfuse.  Cp.  also  geyser, found,  adj.,  provided,  equipped,  with.  —  Prop, pp.  of  find.
=== fuse, ===
1189:Derivative:  ablution-ary ,  adj. abnegate,  tr.  v.,  to  deny,  give  up.  —  L.  abnegdtus, pp.  of  abnegare,  ‘to  refuse,  deny’,  fr.  ab-  and negare,  ‘to  say  no,  deny’.  See  negate, abnegation,  n.  —  L.  abnegatio,  gen.  -onis,  ‘re¬ fusal,  denial’,  fr.  L.  abnegdtus,  pp.  of  abnegare. See  prec.  word  and  negation.
1878:of  affronter,  ‘to  affront’.  See  affront, affuse,  tr.  v.,  to  pour  upon.  —  L.  affusus,  pp.  of affundere,  ‘to  pour  upon’,  fr.  ad-  and  fundere, ‘to  pour’.  See  fuse,  ‘to  melt’  and  cp.  confuse,  in¬ fuse,  refuse,  suffuse,  transfuse. afTusion,  n.  —  L.  affusid,  gen.  -onis,  ‘a  pouring upon’,  fr.  affusus,  pp.  of  affundere.  See  prec. word  and  -ion.
4346:Derivative:  bamboo,  tr.  v. bamboozle,  tr.  v.,  1)  to  hoax;  2) to  confuse,  puzzle. —  Of  uncertain  origin.
```


## [2026-09-06T02:17:26.374Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD page 184 (leaf 250) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==251' SOD_pages.txt | head -40; echo \"=== SOD grep zw ===\"; grep -n \"^184 \\| 184 \" SOD_pages.txt | head",
 "description": "Look at SOD around 184"
}
```


### [2026-09-06T02:17:28.140Z] TOOL RESULT

```
=== SOD page 184 (leaf 250) ===
                                                                                                                   k'm
 185

                                                                   future particle
         zyst- hated
        ugly,                                                      GMS 448, 646; C2 p85, 184
        BBB p77, 633; GMS 451
                                                   aj t<~S
                                                              4627 kJp- B '                   (^^O^jOoJtjacja^
4614 jyst'wc M                                                     kap/f ^kpt-                 /
                                    tSJj* <&j*
     zistauc (jystwc) ^zyst'wc
     hatred                                                        (^)split
                                                                   TSP 21iii 3 n p234
     BBB 633 bl8; GMS 1080; Hen. Cosm. 307, 49;
                                                              4628 q>pt M => kpt-
       Magi. 140 n 2                                          4629 k>8n B                                        S£ <Jt
4615 jystm'nky'Ch) M                                               ka5/0an (q>t) ®<*ka0amai Ska =>k>t
     zist-man(a)kya                             ts&i'J**           dumb
                                                                     very
     bad intentioned
                                                                   SCE 81, 367; Schwartz. BSOAS 34, 1971, 414
       BBB p75.693; GMS 1147                JiJU v
                                                              4630 k>5y B, S        *                  jj^^^U,
4616 jystrw}n M                   s                                ka5y/e/i ©<*kaSiya
     zist-r(u)wan
     bad intentioned, ill will
                                                                   EGSii 160; TSP 5.71, 87; VJ 10, 3-; -w, Anc. Lett.
     BBB 606, 691
                                                                     1.3
4617 jystrw,ndy> M                                            4631 kYkh B                                         j^lT
     zist-rwandya                                                  kaxa(k) -»k»Yk(h)
     bad intention
       BBB 606, 712; GMS 291, 1147                                 TSP 7.55 np211
                                                        o>j
4618 jystwc =» jysVwc                                              palate
                                                              4632 k^' B                                            Wf
4619 jyt- M                                                        kaya5a   (q'ySO ©f.n; ob. -yh, -y'; abl. ->
                                                                     -^k'y^kh
     zot ©pt. st. -»zyt-\ jn-, jt-
=== SOD grep zw ===
4304:                                                          184 Vnt^ B                     (Ujoh/fr        jJLfb)\xi\
7988:         cahier 7, 1989, 184                                     1480 >rtJ =* »srwc(yy)
9877:       Anc. Lett. 2.4, 52; S W, CI, 1991, 184                 2110 'xsywnymync M                                         ^U.
14077:         184                                                               Srzc, dr(a)zy ? (Srzyh) ©drzaya-, Khwar.
16254:     F. Grenct. SI cahicr 7, 1984, 167, 184               4403 Ywnty C                                       jU >jy tffi
17735:     TSP 2.1019; Vim. 11, BSTBL; BBB 570 alO                        GMS 1581, 1604, 1680; C2 gloss, n p66, 84, 184 n
22600:       -?, Dhu. 184                                          6582 pc'w'kryCy) M                       j^o^'J**!-*
27630:          1974, 3R 2; impf. p>xw>y, MSP b 184                             GMS  892
29253:     STi 19.11, 64.3; Sund. AI 1988, 177.39, 184                   sang (snk7, snkh) ©<SkUamgha
30756:        Sund. AI 28, 1988, 184                                        Sogdica 36.25
```


## [2026-09-06T02:17:44.051Z] TOOL CALL #22: Bash

```json
{
 "command": "ls site/pages/192.jpg 2>/dev/null; pdftoppm -f 192 -l 192 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg192\" && ls -la \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/\"",
 "description": "Render PDF page 192"
}
```


### [2026-09-06T02:17:46.400Z] TOOL RESULT

```
site/pages/192.jpg
total 26120
drwx------ 2 sfmqrb sfmqrb   12288 Sep  5 22:17 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74140 Sep  5 16:56 build160.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53286 Sep  5 16:55 build161.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67253 Sep  5 16:56 build162.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   82221 Sep  5 16:56 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53542 Sep  5 16:57 build169.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58105 Sep  5 17:02 build171.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51583 Sep  5 17:08 build173.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59926 Sep  5 17:11 build174.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64448 Sep  5 17:12 build175.py
-rw-rw-r-- 1 sfmqrb sfmqrb   69033 Sep  5 17:13 build177.py
-rw-rw-r-- 1 sfmqrb sfmqrb   75374 Sep  5 17:12 build180.py
-rw-rw-r-- 1 sfmqrb sfmqrb   43965 Sep  5 17:11 build181.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64481 Sep  5 17:11 build182.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47920 Sep  5 17:11 build183.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62604 Sep  5 17:16 build184.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63773 Sep  5 17:17 build186.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62923 Sep  5 22:13 build189.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5391 Sep  5 17:02 g2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2929 Sep  5 17:02 g3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5607 Sep  5 17:02 g4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14924 Sep  5 17:01 geus_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10247 Sep  5 17:01 ghaido_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4197 Sep  5 17:01 ghaido_low.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3536 Sep  5 17:04 jang.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     310 Sep  5 22:16 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56703 Sep  5 16:54 mk166.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61790 Sep  5 16:57 mk167.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb   84301 Sep  5 17:17 mk176.py
-rw-rw-r-- 1 sfmqrb sfmqrb   68808 Sep  5 17:15 mk178.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24939 Sep  5 17:01 n14.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3293 Sep  5 17:01 n17b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17771 Sep  5 17:01 n17c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6463 Sep  5 17:01 n17.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7472 Sep  5 17:01 n19.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3278 Sep  5 17:01 n5b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2334 Sep  5 17:01 n5c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  5 17:01 n5.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35268 Sep  5 16:59 p162a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14337 Sep  5 16:59 p162b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:59 p162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161412 Sep  5 17:01 p174hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  173427 Sep  5 17:01 p176hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2762 Sep  5 17:02 p189_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24596 Sep  5 17:02 p189_greek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20222 Sep  5 17:02 p189_khoris.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33994 Sep  5 17:02 p189_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1093 Sep  5 22:17 p190_emptybox.png
-rw-rw-r-- 1 sfmqrb sfmqrb  102711 Sep  5 22:17 p190hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5540 Sep  5 22:17 p190_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1189 Sep  5 16:57 p600_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73400 Sep  5 16:56 pg172.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70664 Sep  5 17:00 pg174.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83583 Sep  5 17:00 pg176.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88207 Sep  5 17:02 pg177.png
-rw-rw-r-- 1 sfmqrb sfmqrb   98352 Sep  5 17:01 pg178_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66020 Sep  5 17:01 pg182.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53414 Sep  5 17:03 pg183.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79537 Sep  5 17:09 pg185.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72425 Sep  5 17:08 pg186.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53749 Sep  5 17:02 pg187.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77516 Sep  5 17:01 pg189.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65970 Sep  5 22:17 pg190.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71828 Sep  5 22:17 pg192.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
-rw-rw-r-- 1 sfmqrb sfmqrb     738 Sep  5 17:04 xang.txt
```


## [2026-09-06T02:17:49.555Z] TOOL CALL #23: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg192.png"
}
```


### [2026-09-06T02:17:50.177Z] TOOL RESULT

```

```


## [2026-09-06T02:17:50.148Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T02:18:02.313Z] TOOL CALL #24: Bash

```json
{
 "command": "grep -ril \"\\\"zav\" data/extracted/batch/ | head -20; echo \"---\"; grep -rn \"zav 2\\|zav 1\" data/extracted/batch/*.json | head -20",
 "description": "Search extraction for zav"
}
```


### [2026-09-06T02:18:02.391Z] TOOL RESULT

```
data/extracted/batch/page-195.json
data/extracted/batch/page-177.json
data/extracted/batch/page-192.json
data/extracted/batch/page-137.json
---
data/extracted/batch/page-137.json:19:            {"translit": "zav 1, zbâ", "gloss": "call", "script": null},
data/extracted/batch/page-192.json:53:            {"translit": "zav 2", "gloss": "a kind of alcoholic beverage", "script": null}
```


## [2026-09-06T02:18:03.481Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD entry 184 context ===\"; sed -n '4295,4315p' SOD_pages.txt; echo \"=== SOD beverage/wine ===\"; grep -n \"beverage\" SOD_pages.txt | head -10",
 "description": "SOD entry 184 and beverage glosses"
}
```


### [2026-09-06T02:18:03.575Z] TOOL RESULT

```
=== SOD entry 184 context ===
                                                              mixed, dirty
    (to)plough                                                BBB b30; S W, C2 p97.4
    GMS 634
                                                          183 wn S                     ((j--^-^ ifUtiljjU- jl (J^j fk)uT
168 "ms' M,C                           *r y i<j J>j^*j*       an
     amsa ©ob. -yy ^ms*                                       An(a Sogdian family name)
     obedience, attention
                                                              Hen. BSOAS 11.736, 12.603 n 2; Sogdica. 59
     GMS 973, 1265; BBB 687; STii 4.37; WJfcr "to
                                                          184 Vnt^ B                     (Ujoh/fr        jJLfb)\xi\
       observe" Benv. J A 1951, 118; BSL 53 p57f
                                                              Ananda
169 "ms* frm'y- M                             o^4y            VJ; SCE; BSTBL
    amsa-framay
    (fo)take care                                         185 *nH(i) B                                      jwlj.SuiT
                                                              anat ©Khot. anata
    Sund. Man. Lett. 310.17; Frag. Len. 37.18
                                                              perfectly, clearly
170 "ms'k S                        ? u-> <a*s&a               TSP 6.109, 10.11, Vf; BSTBL; S W, C2 n p55.10;
    amsak ? ©<*hama-sahaka-t Pahl. hmys^k                       Bailey. Prolexis. 95
    list?
=== SOD beverage/wine ===
```


## [2026-09-06T02:18:17.463Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT zav ===\"; grep -n \"j\\.,\\? g\\.\\? \\?zav-\\|• j\\. zav-\\|zav-  V\\|zav- V\" BRT.txt | head; echo \"=== BRT 'zav' generally ===\"; grep -n \"zav-\" BRT.txt | head -20",
 "description": "BRT zav-"
}
```


### [2026-09-06T02:18:17.550Z] TOOL RESULT

```
=== BRT zav ===
=== BRT 'zav' generally ===
5388:auniäa.bäzav-
5397:•  j.  auru5a.bäzav-    Adj.    (auch   : 'weissarmiß':  kaininö  kihrpa  . .  "Zfh  \^o.,  .  ^  ,,     ,
6493:die  Peitsche  knaÜt'  Yt,  /o.  1 1 3 ;  —  j«/ . . , ,  j.  as.bazav-  Adj.  'mit  tUchtigen,  starken 'rä  kakvqn  (sd)  Vtio.113;    —   Ja/  -4?  Vorderbeinen,  -schenkein':    uströ .  .   'zSus iyimai)  zaya  frabanm^  aum  y5  ahurö  .  .    (fjs.)  aii.kaüß  Vt  14- 12. suwram   (sd.)  .  .    'ramca  '>   zaramo.paisim  I      Kpü.;  läMib  biryär  zur  az-ar  bäsuvän. V.2.6;-»^Ä0,™)  .,y«/(sdL)  -ra,^  .    -    ^.t,„,.   ^dj.    (auch    fem.)    'rid, V.2  10.  .)    inb»    dit    pntsteihcht   ,^iai\A   bringsnd':  /r.valml .  .    ,4    ■Is
7662:■»«zav-
7692:•  g.  '«razav-  (,  p.  aräav-)  Adj.  'gerade, richtig,    recht',    vom   Weg;   yJ   «./    °züi
7697:"arazav-
7701:•  j,  'arazav-  m,  EN.  eines  Gläubigen' Bruders  des  Sra/öjpada  (sd.):    'ma  (GD.) srBtöjfädä  ahonä  Yty,  115.
7705:•  j.  ^razav-  m.  'Finger":  °zu  F.jg;  — ci'al  gaonahe  (sd.)  . .  ya  dvaHbya  "zubya *hiing3riwn,lt  N.  Ö5;  —  avaval  tafta  ydha kasistahe  (,  mawmaAe,  masistahe)  °svB sisV.6.10,  12,  14, /Ä44  PüZ.  a)  die Breite  der  Finger  als  Maasseinheit:  dva 'ZU  nismaAe  (sd.)  V.(j.6;  —  avavat  aipi yd^a  caiwärS  °zavö\.g.2();  —  cd^wSrö 'zvö  V.  6.  43,  f).  6.  [V.  iS.  2  PüZ. :  lies bai.intu\
8118:•  j.  Ujra.bäzav-  Adj.  'starkarmig':  {iiit^r?) ':,iu/ (NS.)  Yt.  70.  75.  [Vt  70.42:  lies ujra  dinara.]
8660:•  j.  uzbäta-  Adj.  (fem.  'ta-),  PPf  P. :  s,  zav-. w+^-.  S  ja*  n.  36.
8661:•  j.  uz-bäzav-  Adj.  (auch  masfc.)  'die Ajme  emporhebend';  °zäus  (NS.)  fiaiii attunxllm  (sd.) /ravazai/e  mi^rS  Yt,/o.ia4.
11601:•  y  Jazav-  m,  (auch  mit  'spart-  m.)  Name einer  Art  des  Hundegeschlechts:  hau  °z3us (GS.)  hau  visäui  . .  hau  vTspanam  . .  spa- ct^ranam  V. /J.  16;  —  spä  *ius  V.^.^j.
12894:')  Ein  Schönheitsieichen;  vgl.  Artaxerxts  L Beiwort  Longimaiios,     S.  in  dar>-fö,bäzav-.
12906:darttgö.bazav-
12909:•  g.  darsgö.bäzav-,  j.  dar^ö.bäzav- Adj.  (auch  fem.)  langannig':  hukmlB  ahi
17125:•  j,  bäzav-  m.  i)  'Ann'  der  Menschen  und       '  5'  '*     ..  ..r,    _  .   i-n^    ,  *j:  -.^  « i-M^         i-,   -r  ,/TL'      .    Tc-v.i   j   <■      ■         Komp.  mit  ND.  im  l,  Glied;  s.  ituan-  A. Gotter:  ÄJtJv« '«i'jfLb.  als  IS.)'' j(jn«aiv)        .     /_      ■      v  ^      .  j-     (^    .     -       j ./aÄ«.-«.ä*te.«,*5,"milde,»li,JimAnn  •   !■   bs^-s-aolah-   Ad,.    Oak    m    den «.d  dem  «cht«,  mit  de«,  rechten  Ar»  m,d  '^f  "»  *^'  "^'  '""• '  -»ß-»«. . . deoh»kei."V.j.>5i-j...,yü!j»,,;7™i,  V»«"!'"  '?*''/'/?;  \t.,o.,y,-«-a^,aAr
20163:•  j.  mazav-  Adj.  'acht  habend  auf  — ',  mit Gea:  a^a  spamm  nida%}m  yat  dim  'zacs (NS.)  k)hrps  türahe  "den  Hund  habe  ich dazu  bestimmt,  dass  er  acht  habe  auf  die Person  des   Tärere"  V.  13.  39.
20395:•  j.  'msrszav-  n.  'Wirbel'  des  Halses  und Rückens:  yavata  . .  tii/ainti  °tu/a  ttünB gayehe  'sula  x&  uimnahe  "bis  er  entzwei
20399:j.  'iD'Srazav-  in.,  Du.  Bezeichnung iner  a frischen  Schöpfung,  vll.  eines Sternbilds:  nizbayemi  'zu  ^pourvs  *:^a%/ltd yüßis/ff  mairtivä  *d3mqn  'ich  rufe  an  die beiden  M.  im  Süden,  die  ewigen,  die  am besten  kämpfen  von  der  Schöpfung  der beiden  Geister"  V.  ig.  42.
20401:•  j.  Jm»r»zav-  Adj.  (fem.  'zvt)  —  ?— : zaya  ava%a  staxr!>{sA.)  yat  ha  druxsaHH 'ZVT  FrW.  S.  2  '>.         Vgl  '^mjnzu.
```


## [2026-09-06T02:18:18.115Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"intoxicating\\|a kind of drink\\|liquor\\|of wine\\| wine$\\|wine,\" SOD_pages.txt | head -20",
 "description": "SOD wine glosses"
}
```


### [2026-09-06T02:18:19.674Z] TOOL RESULT

```
18741:                                                                         wine
18799:                                                                         wine
19416:5479 mrx- M, C                c^ljJL i^L-toUtjl^                        intoxicating
37199:      beer, liquor
38620: in excess 4008                              insolent     8586, 9358                  intoxicating    5491
38775:     liquor   11503                         Lord Jesus     10679
```


## [2026-09-06T02:18:25.199Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '37190,37205p' SOD_pages.txt; echo \"===\"; sed -n '18730,18750p' SOD_pages.txt; echo \"===\"; sed -n '18790,18805p' SOD_pages.txt",
 "description": "SOD beer/wine entries"
}
```


### [2026-09-06T02:18:25.290Z] TOOL RESULT

```
      sacrifice
                                                                     11513 zwyrt-      C                                  &&>£ ji
      BSTi 213, 223, 293 A24; BSTii 849.12: C2, 12R
                                                                            zwert ©<*uz-wartaya- ^zw'rt-, zw»yrt-
        12, ace. p84 n 62; GMS 229 A; Ben v. J A
                                                                            (to)make return
        1951,119                                                            STi 5.7 apud. Sund. AoFiii 85.7 nl44; C2, pres.
11503 zwt'k B, S               J<«vj^(u^>)«>wT                                102R19, 68V16, fut. 68R15; impv. 69V24
      zute ? (zwtk, z'wy* ?) ^jwty*                                  11514 zwyz-     C                             o>fSs\tj*~
      beer, liquor
      TSP 2.388, 599, 607, 664, 890, 959, 988, 1001,                        zwez ©<*uz-waija; S"waik          «»wyc
                                                                            (to)sift, OcOwinnow
        1010, 1024, 1035, 1049, 1118, 1188, 1202,
                                                                           S W, C2, 40R11 p84-5
        1217, 21 iii 8, 10, 14; SCE 412; Frag. Len.
                                                                     11515 zwz- C                                       o^Xj'j^
===
          ay a)nu ^m'hjmnw                                                    SCE 25, 342; BSTBL, Dhy. 16; O3 5; EGSii 13
                                                                         5272 m'ytr'k B                            b^vaiJ>ui*
       BBB 724; GMS 63; Hen. JRAS 1945, 155                                   maitre/i (m'ytry) -^mytr'k/'y
                                                                              Maitriya
5259 m'xnc S              ^T ^<L-j * «U L^j> fyl jl U
     max-(an)c ? -^mV                                                         TSP 8.5, 200; Bailey. Prolexis. 28 1; Benv. TSP
     we from him, we from them
                                                                                6.150 "friendship"; Hen. Texts. 735, maitrl
     m'ytry                                                                                                                 210


                                                                         wine
     5273 m'ytry => m'ytr'k
                                                                         Anc. Lett. 5.8
     5274 m'zych m'th B, S    (-kP^jj^J^J^jsU
          mazec-mat ©Shugh. ndn-ej, mdd-ij                          5286 m5'n B, M                                          ju,
          stepmother                                                     m(i)San ^myS^y, m8y}ny
                                                                         middle
          SCE 242; Hen. Tales. 483, 14, 16, 484.4; VJ n
                                                                         TSP2.1106-, ob.-y, BBB 574?
            p!35
===
         macrencik, mscrencik ?
         (c?/)Egypt                                                      MSP bl60
         Sund. AI 28, 1988, 182                                     5294 mStnpV B                           ^jj'^t/ (^>)
                                                           ^Sj-o*
    5282 m5' B                                                           (a kind c»/)herb
                                                                         TSP 19.7
         ma8 -tm'5
         thus                                                       5295 mSw B, M, S                                  (ji)^
         VJ 1075
                                                                         wine
                                                                         maou (mdw) =*m8Jk, mw62
    5283 m52 S                                            bo!
         ma&a =»mrS, m8y, mSp'r, 'mS^                                    TSP 2.388, 2 Hi. 4; GMS 408, 1171; Hen. BSOAS
         here                                                              10, 98; Anc. Lett. 4.6; MDii A-16, 6, STi 36.1;
         Anc. Lett. 4.8; mSK MDii                                          Sund. AoFiii 14R1; BSTii: C2, 57R18
    5284 -m5   B                                     t'.v
```


## [2026-09-06T02:18:37.124Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find leaf containing entry 11503\nfor i,p in enumerate(pages):\n    if '11503 zwt' in p:\n        print('leaf',i)\n        print(p[:400])\n        break\nEOF",
 "description": "Find leaf of SOD entry 11503"
}
```


### [2026-09-06T02:18:38.905Z] TOOL RESULT

```
leaf 536
469

       102R21, fut. 51R10, pret. 87V 12; impf. zywrt,                          pi. -tl}\ ob. pi. -fy> =»?Ywsk-, jwxsk/q          ?y
                                                                             disciple
         C2, 105R7; BSTii 835.7; BSTii 835.7
                                                                             STi 8.10, 12, 6.6, 17.1, 13.7, 22.15, 33.12, 21 34.2,
1
```


## [2026-09-06T02:18:45.872Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (248,249,250):\n    print('==== leaf',i,'====')\n    print(pages[i][:1600])\nEOF",
 "description": "SOD leaves 248-250"
}
```


### [2026-09-06T02:18:47.675Z] TOOL RESULT

```
==== leaf 248 ====
 183                                                                                                              jn'ptnym


 4569 j'rnyy M                                   jb^Aj ttfjAj          hard, cruel
      zarne                                                            BBB 510, Hen. Tales. 473.28; BSOAS 11, 66.9;
        poisonous                                                        GMS 410n 1
        BBB b36
                                                                 4580 jyyr-   M                               q*j\x* < jxl^-
 4570 j^rynyh       M                            J*y>j <i$j*j
                                                                       zyer   Ojyyr-) ©impf. jyYyr =^zy>yr-, zyyr-,
                                                                         >Zy)yr„
      zarene
        poisonous
        GMS 1058                                                      (/o)call
                                                                      GMS 629, 706, 730-, W-Li; Cropp. p39
4571 j>y- M                                i>jo^ ^ i            4581 jyyrt- M                         j-^o/i tdxiy-
     zay ©<*dray-\ MP dray                                           zyert ©pt. st.
     Go)speak, (ro)talk                                              (to)call, (to )be called
     BBB pl26; GMS 285; AVS 92                                       GMS 537; pp. jYyrtyfyh W-Li, ii; BBB cl5
4572 jp- M                      ^        Ox^^/jlT               4582 jkrystr M                        jlJJ?*> «>X*
     za/iP =»zyP-, zyP-                                 
==== leaf 249 ====
            i in -: ii ■ i mium^^man^mmtmtmmmmammm
                                                                                                   mn

 jnwq

                                                                                                              184
                                                                   BBB 516; Hen. Cosm. 307.46; W-Li, Gropp. p39
        injunction
        BBB 64; Gersh. Sogd. Cpds. 138; Advice. 79ff
                                                             4601 jwky'mync      M                                   ^JU
 4590 jnwq => jnwwq                                               zukyamenc      (jwqy'mync)
 4591 jnwwq      M                                     y\j        safe, sound
                                                                   GMS    1103; BBB 516
        znuk   (z'nwk^, jnwq) ©Av. znu; Pahl. snwk
        knee
                                                             4602 jwqy'mync =* jwky'mync
        Sogdica. 49.8, 50 n p50, CMS 264, 978                4603 jwndty =* jwndyy/h
 4592 jt- M                                            O^j   4604 jwndyy/h      M                                        *xj
        zot ®<*jata ©pt. st. =»jyt-, zyt-3                        zwande
                                                                  living     (jywndyy, jwndty) ^jw'ndyCyX
        GcOstrike                                                   'zw'nt'k, zw'ntk, zwnty
        GMS 108, 577, 925; AVS 98; inf. jtyy, Hen.
          Tales. 46730
                                                     
==== leaf 250 ====
                                                                                                                   k'm
 185

                                                                   future particle
         zyst- hated
        ugly,                                                      GMS 448, 646; C2 p85, 184
        BBB p77, 633; GMS 451
                                                   aj t<~S
                                                              4627 kJp- B '                   (^^O^jOoJtjacja^
4614 jyst'wc M                                                     kap/f ^kpt-                 /
                                    tSJj* <&j*
     zistauc (jystwc) ^zyst'wc
     hatred                                                        (^)split
                                                                   TSP 21iii 3 n p234
     BBB 633 bl8; GMS 1080; Hen. Cosm. 307, 49;
                                                              4628 q>pt M => kpt-
       Magi. 140 n 2                                          4629 k>8n B                                        S£ <Jt
4615 jystm'nky'Ch) M                                               ka5/0an (q>t) ®<*ka0amai Ska =>k>t
     zist-man(a)kya                             ts&i'J**           dumb
                                                                     very
     bad intentioned
                                                                   SCE 81, 367; Schwartz. BSOAS 34, 1971, 414
       BBB p75.693; GMS 1147                JiJU v
```


## [2026-09-06T02:19:02.798Z] TOOL CALL #31: Bash

```json
{
 "command": "grep -n \"zav\" data/extracted/batch/page-195.json data/extracted/batch/page-177.json data/extracted/batch/page-137.json | head -20",
 "description": "Other zav mentions"
}
```


### [2026-09-06T02:19:02.935Z] TOOL RESULT

```
data/extracted/batch/page-195.json:91:            {"translit": "zavaiti", "gloss": "invoked, God", "script": null}
data/extracted/batch/page-137.json:19:            {"translit": "zav 1, zbâ", "gloss": "call", "script": null},
data/extracted/batch/page-177.json:164:            {"translit": "zavah, zâvar", "gloss": "power, force", "script": null},
data/extracted/batch/page-177.json:192:            {"translit": "zava", "gloss": "haste", "script": null},
```


## [2026-09-06T02:19:14.498Z] TOOL CALL #32: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T02:19:14.504Z] TOOL RESULT

```


```


## [2026-09-06T02:19:18.704Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ew-",
 "prompt": "Give the reconstructed root, its meaning, and all listed descendants (Indo-Iranian, Avestan, Greek, Latin, Germanic). Quote the derived-terms list."
}
```


## [2026-09-06T02:19:19.714Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/alchemy",
 "prompt": "Quote the full etymology of alchemy and any note about the Greek 'to pour' vs Egyptian 'black land' theories. Also quote chemistry/chemical if present on the page."
}
```


### [2026-09-06T02:19:26.583Z] TOOL RESULT

```
# Etymology of Alchemy

## Full Etymology

According to the Online Etymology Dictionary, alchemy originated from:

"mid-14c., from Old French *alchimie* (14c.), *alquemie* (13c.), from Medieval Latin *alkimia*, from Arabic *al-kimiya*, from Greek *khemeioa*"

The source traces competing theories about its ultimate origin.

## Origins Theory: "To Pour" vs. "Black Land"

**The "to pour" theory:** The word possibly derives from Greek *khymatos* "that which is poured out," from *khein* "to pour," ultimately from the PIE root meaning "to pour" (though one scholar calls this folk etymology).

**The "black land" theory:** It may come from an old Egyptian name *Khemia*, literally "land of black earth."

The dictionary notes: "The word seems to have elements of both origins," and quotes the OED concluding that Greek *khymeia* was likely original, applied to pharmaceutical chemistry involving plant infusions.

## Chemistry Definition

"*chemistry*(n.): c. 1600, 'alchemy,' from chemist + -ry; also see chemical (adj.). The meaning 'natural physical process' is from 1640s; the sense of 'scientific study of the composition of material things' is by 1788."
```


### [2026-09-06T02:20:00.726Z] TOOL RESULT

```
# Proto-Indo-European Root *ǵʰew-

**Reconstructed Root:** *ǵʰew-

**Meaning:** "to pour"

## Major Descendants Listed:

**Proto-Indo-Iranian/Indo-Aryan:**
- Sanskrit: जुहोति (juhóti), होम (hóma), हव्य (havyá)

**Proto-Hellenic/Ancient Greek:**
- χέω (khéō), χῡμός (khūmós), χυλός (khūlós), χύτρα (khútra)

**Proto-Italic/Latin:**
- fūtis, fūtilis, effūtiō

**Other branches:** Armenian, Albanian, Phrygian, and Tocharian forms are also documented.

## Derived Terms Note:

The page lists "55 c, 0 e" in the derived terms category, indicating 55 terms derived from this root are catalogued. The document presents numerous extensions and formations including "thematic present," "reduplicated present," and "reduplicated stative" formations across multiple Indo-European language families.
```


## [2026-09-06T02:20:08.222Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D9%8A%D9%85%D9%8A%D8%A7%D8%A1",
 "prompt": "Quote the Arabic etymology of كيمياء (kīmiyāʔ) in full, including any Greek source and any Persian/Egyptian discussion, and the descendants list."
}
```


## [2026-09-06T02:20:08.723Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/geyser",
 "prompt": "Quote etymology of geyser. Also anything on the page about gust."
}
```


### [2026-09-06T02:20:14.255Z] TOOL RESULT

```
# Etymology of كيمياء (kīmiyāʔ)

**Etymology:** The word is "Borrowed from Ancient Greek χυμείᾱ (khumeíā), from χῠ́μᾰ (khŭ́mă) + -ία (-ía)."

The etymology tree traces the lineage back through Proto-Indo-European *ǵʰew- ("pour") and shows the development through Ancient Greek formations.

**Note:** The page contains no specific Persian or Egyptian discussion of the etymology—only the Greek source material and linguistic reconstruction.

**Descendants:** The term spread widely, producing forms in:
- Latin variants (alchēmia, chēmia, chimia, chymia)
- Romance languages (French chimie, Spanish alquimia, Italian alchimia, Romanian chimie)
- Germanic languages (German Chemie/Alchemie)
- Slavic languages (Russian химия, Polish chemia, Bulgarian алхимия)
- Asian languages (Turkish kimya, Persian شیمی, Hindi कीमिया, Urdu کِیمیا, Indonesian kimia, Swahili kimya)
- Other languages including Georgian, Armenian, Bengali, and Javanese variants
```


### [2026-09-06T02:20:15.635Z] TOOL RESULT

```
# Etymology of Geyser

The word "geyser" entered English in 1780, derived from the Icelandic name **Geysir**, a specific hot spring in Iceland's Haukadal valley. The term literally means "the gusher," tracing back through Old Norse *geysa* ("to gush") to Proto-Germanic roots meaning "to pour."

As the etymology notes: "Taken by foreign writers as the generic name for spouting hot springs, for which the native Icelandic words are *hverr* 'a cauldron,' *laug* 'a hot bath.'"

# About Gust

The page includes "gust" in its list of words derived from the Proto-Indo-European root **\*gheu-** ("to pour, pour a libation"). Specifically, it's noted as **"gust (n.) 'sudden squall of wind'"** stemming from this ancient root meaning "to pour."
```


## [2026-09-06T02:20:24.396Z] TOOL CALL #37: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py; echo \"=== ref_page ===\"; sed -n '1,30p' tools/ref_page.py",
 "description": "Inspect helper tools"
}
```


### [2026-09-06T02:20:24.463Z] TOOL RESULT

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
=== ref_page ===
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
```


## [2026-09-06T02:20:28.295Z] TOOL CALL #38: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:1759 --image 2>&1 | head -60",
 "description": "Fetch BQT page 1759"
}
```


### [2026-09-06T02:20:36.414Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1759.png
REF: BQT:1759  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 556  OCR-lang: fas

۱۷0۹۳ کین‌سیاوش
کیمخت «بکر اول وشم نالك‌بروزن | خالی از حیله ومکری نیست از این جهت باین
میپخت» معروفت و آن‌پوست کفل وساغری‌اسب | لام خوانند -ولظر پیر ومرشدکامل‌رانیز کون
وخراست که بنوعی خاس دباغت کنند۱ , وبستی | و عشق و عاشقیراکیمیا وکیمیا کری کویند -
گوبند کمخت دانهایی است که در آن پوست وارزیزرا نیز کفته‌اند که بعرییرصاس‌خواننده -
میباشد - و پوست ترنجیده ودره مکشیده را نیز کیمیای جان « بکر بای حطی
گوبند ۰ وجیم بالف کشیده و بنون زده ,کنایه از شراب
کیمخت ماه - بکر فوقانی ومیم | انگوری باشد .
بالف کشیده وبهای زده » کنایه از آسمان است کین - بکر اول وسکون تحتانیونون»
وبعربی سما خوانند . بمعنی کینه است که عداوت و دشمتی باشد ‎٩‏
‏کیمی - بنتح اول وضم ثاك‌وسکون | ومخغف که این م هت وآنرا بالفحم نوسند
سین بی‌قطه » نام مردی بوده * باین صورت «کاین؟ ۰
کیموس؟ - بنتحارل بروز نکیلوی, کینال - بروزن نیتال » هردم شراب
بلفت پوتانی بمعنی دوباره پخته‌باشدوآن دویمین خور وبدمت راگویند.
طبخی است که غذا در جگر مییاید . کین‌ابرج - بکرنون, ام لحن نوزدهم
کیمو نحتن ۴ - بکر اول نون | است از سی لعتن باربد - ونام نوایی هم‌هست .
وسکون سین بی‌نقطه وفتح فوقالی ونون ساکن, کین و۷2 - با تای فرشت بر وزن
بلفت زند وپازند بمعنی خواستن وطلبیدن‌باشد. [ نیمروز » این لغت مرکب است ازکین و توز
کیمیا؟ - بکر اول و ثاك بر وزن | بمعنی کینه‌کش و صاحب کین ه که تلافی کنندء
سیمیا » یمعنی مکر وحیله باشد و عملی است | بدی باشد چه‌کین بمعنی کینه و توز بمعنی
مشهور نزد اهل صنمت که پیب امتزاج روح کشیدن آهده است .
وضی اجاد ناقصه را بمی‌تبهٌ کمال رسانند یعنی کین‌سیاوش - بکر نون, نام‌لحن
قلمی ومس را نقره وطلاکنند و چون این عمل | بیستم است از جملهٌ سی لخن بارید"
‎٩‏ -صبح ازحمابل فلكآهیخت‌خنجری کیمخت کوه ادیم شد ازخنجر زرش.
«خاقابی شروانی ص ۰۲۲۰

۴ - ازبوتانی3۳07716۵5 «لیدلواسکات»«اشتینگاس»(بمعنی سیالوعاره) ودرطب استحالهٌ
طعام است در معده بمد از حضم بجوهری دیگر که ماده‌ای غلیظ مایل برنگه زرد باشد «تفی».

۶ - هز 61۳۵۵9120ا, 6۳۵19128 ,3389128 - (خواستن) «یولکر 4۱۱۱
ظ . مصحف 121325188 پهلوی * ۳31010420 (خواستن) . رك4 : باروچا ۰۲۹۲

۴ - ازیونانی 2630612 «اشتینگای» (بممنی‌اختلاط وامتزاج) «نفض» ,قی:016طآط216
(فر)» زنط (فر) . و691۲ (انگه) . 6 - کیمیا . در برهان بمعنی ارزی ز که
بعریی رصاص کویند . نیز آورده . واین خالی از غرابت نیست» «بس‌اج‌اللقات بنقل فرهنگه نظام
چهص م6 ‎٩‏ #کینه . اوستا - 68602 «بارتولنه ۶۲۹ پپلوی 1680 «نیب رکه
س 3۱۲۸ هنای ۲۷۸ * « اسشق ۸۸۱ »کردیع 518 » بلوچی 548810 (دشمنی» کینه)
«اسشق ۸۹۱ ارمنی ع 1۳60 ( کینه » دشمنی ) » افقانی ع 1۳188 ( کینه ورزی » عداوت )
«هوبشمان ۸۸۱ - ۷ - از :کین (ه.م.) ۳+ توز (توزده) .
```


## [2026-09-06T02:20:50.805Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"رفوزه\" \"فیوز\" \"شیمی\" \"کیمیا\"; do echo \"=== $w ===\"; grep -oh \".\\{0,160\\}$w.\\{0,160\\}\" MON_part1.txt MON_part2.txt 2>/dev/null | head -4; done",
 "description": "Grep Mo'in 2-vol for the loanwords"
}
```


### [2026-09-06T02:21:04.407Z] TOOL RESULT

```
=== رفوزه ===
=== فیوز ===
=== شیمی ===
=== کیمیا ===
```


## [2026-09-06T02:21:06.776Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt && head -c 600 MON_part1.txt",
 "description": "Check MON files"
}
```


### [2026-09-06T02:21:06.843Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
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


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی
```


## [2026-09-06T02:21:13.065Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%B1%D9%81%D9%88%D8%B2%D9%87",
 "prompt": "What does Mo'in's dictionary (فرهنگ معین) say for رفوزه? Quote the entry including any origin tag such as [فر.]."
}
```


## [2026-09-06T02:21:14.367Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%81%DB%8C%D9%88%D8%B2/",
 "prompt": "Quote what فرهنگ معین and دهخدا say about فیوز, especially the origin/language tag (e.g. [فر.] French, [انگ.] English)."
}
```


### [2026-09-06T02:21:16.642Z] TOOL RESULT

```
According to Mo'in's dictionary entry shown, the definition is:

"(رِ زِ) [ فر. ] (اِمف .) رد شده در امتحان"

This indicates the word has a French origin [فر.], is an abbreviation (اِمف.), and means "failed in an exam" or "rejected/dropped from an examination."
```


### [2026-09-06T02:21:20.619Z] TOOL RESULT

```
# فیوز - Dictionary Definitions

## لغت نامه دهخدا (Dehkhoda Dictionary)
**Origin tag:** [انگلیسی] (English)

"سیم فلزی که در مسیر جریان برق تعبیه کنند، اگر جریان بسیار قوی و خطرناک باشد سیم مزبور ذوب میشود"

A metal wire placed in the electrical current path that melts when current becomes dangerously strong, cutting off the flow.

---

## فرهنگ معین (Moein Dictionary)
**Origin tag:** [انگ.] (English)

"اسبابی که جهت جلوگیری از عبور جریان شدید الکتریسته در یک مدار به کار می رود"

An apparatus designed to prevent excessive electrical current from passing through a circuit. This source also notes the colloquial expression "~ پراندن" meaning to be astonished.
```


## [2026-09-06T02:21:24.575Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%DB%8C%D9%85%DB%8C/",
 "prompt": "Quote what فرهنگ معین and دهخدا say about شیمی, especially the origin/language tag (French?)."
}
```


## [2026-09-06T02:21:26.458Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B2%D9%88%D8%B1/",
 "prompt": "List all senses of زور given by دهخدا and فرهنگ معین. Is there a sense 'holy water / آب مقدس' used in Zoroastrian ritual, and what origin (Avestan zaothra?) is given?"
}
```


### [2026-09-06T02:21:31.330Z] TOOL RESULT

```
# Definitions of شیمی (Chemistry)

## لغت نامه دهخدا (Dehkhoda Dictionary)
Origin note: **[فرانسوی]** (French)

Definition: "علمی است که در آن از خواص اجسام طبیعی و تغییرات عمیق گوهرها و عناصر بحث می شود" (a science discussing properties of natural bodies and profound changes in essences and elements)

The dictionary traces the word back to "کیمیا" (kīmīyā), emphasizing chemistry's role in decomposing matter into smallest components and studying their compositions.

## فرهنگ معین (Moein Dictionary)
Language tag: **[فر.]** (French abbreviation)

Brief definition: "علمی است که موضوع آن خواص ماده، ترکیب، تجزیه و تأثیر آنهاست" (a science whose subject is matter's properties, composition, decomposition, and effects)

This entry provides a more concise characterization focused on chemistry's core concerns with material properties and reactions.
```


### [2026-09-06T02:21:33.835Z] TOOL RESULT

```
# Senses of زور (Zur)

## From دهخدا (Dehkhoda Dictionary):
The dictionary lists: "قوت و توانایی" (strength and capability), "قوت، قدرت، نیرو" (power, might, force), and notes historical usage relating to compulsion and physical strength.

## From فرهنگ معین (Moein Dictionary):
This source provides: "توانایی، نیرو، قوه، قدرت" (ability, force, power, might), plus "فشار" (pressure) and "زبردستی" (coercion).

## Holy Water Sense:
Yes, there is mention of a Zoroastrian ritual sense. The Moein dictionary lists: "آبی است که به دست یکی از موبدان پاک و مقدس شده" (water consecrated by a Zoroastrian priest), though this appears as a separate entry rather than a core sense of زور.

**Note on Etymology:** The page attributes the word to Avestan roots ("از اوستا «زاور»"), but does not explicitly cite "zaothra" as a source. However, user comments reference "zōr" in Middle Persian and Avestan "zaurva," suggesting Indo-European origins rather than Avestan "zaothra" (the actual Avestan term for ritual water).
```


## [2026-09-06T02:21:39.548Z] TOOL CALL #45: WebSearch

```json
{
 "query": "Avestan zaoθra Middle Persian zōhr libation Persian zōr holy water etymology"
}
```


### [2026-09-06T02:21:47.288Z] TOOL RESULT

```
Web search results for query: "Avestan zaoθra Middle Persian zōhr libation Persian zōr holy water etymology"

Links: [{"title":"Reconstruction:Proto-Indo-Iranian/ȷ́ʰáwtram - Wiktionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C8%B7%CC%81%CA%B0%C3%A1wtram"},{"title":"Ab-Zohr | Religion Wiki | Fandom","url":"https://religion.fandom.com/wiki/Ab-Zohr"},{"title":"ĀB-ZŌHR - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/ab-zohr/"},{"title":"Ab-Zohr","url":"https://en.wikipedia.org/wiki/Ab-Zohr"},{"title":"SACRIFICE i. IN ZOROASTRIANISM - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/sacrifice-i/"},{"title":"Zoroastrianism - Wikipedia","url":"https://en.wikipedia.org/wiki/Zoroastrianism"},{"title":"Zend","url":"https://en.wikipedia.org/wiki/Zend"},{"title":"Zoroastrian Global Glossary | FEZANA","url":"https://fezana.org/glossary/"},{"title":"Zoroastrian Global Glossary v2 (A-M) | FEZANA","url":"https://fezana.org/zoroastrian-global-glossary-v2-a-m/"},{"title":"HAOMA ii. THE RITUALS - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/haoma-ii/"}]

Based on the search results, here's information about the etymology of these terms:

The word family derives from Proto-Indo-Iranian, with Avestan *zaoθra* appearing as Middle Persian *zwhl* (zōhr) and Persian *zowr*, ultimately descending from Proto-Indo-Iranian *jawθrám*.

The Avestan *zaoθrā* is derived from the root *zau-* meaning "to pour," and was principally a "libation, liquid offering," though it was also employed in the general sense of "oblation."

The technical terms Middle Persian *ab-zohr* and Avestan *apé zaoθra* literally mean "offering to water" (ab = water; zohr = offering), and the words of the expression have Indo-Iranian roots.

Regarding Persian *zōr*, the search results show this term is used in dialectal pronunciation (as in Zoroastrian Dari), but the root terminology maintains the same etymology traced back through the Indo-Iranian language family.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T02:21:59.748Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C8%B7%CC%81%CA%B0%C3%A1wtram",
 "prompt": "Quote the reconstruction, its meaning, etymology (root), and the full descendants list including Avestan, Middle Persian and Persian forms."
}
```


## [2026-09-06T02:22:01.456Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/ab-zohr/",
 "prompt": "Quote what this article says about the terms ab-zohr, Avestan apo zaothra, the meaning of zohr, and the root zav-/zu- 'to pour'. Also anything about the zot priest."
}
```


### [2026-09-06T02:22:03.294Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:22:05.313Z] TOOL RESULT

```
# Proto-Indo-Iranian *ȷ́ʰáwtram

**Reconstruction:** *ȷ́ʰáwtram (neuter noun)

**Meaning:** "libation, offering, sacrifice" (religious context)

**Etymology:** Derived from Proto-Indo-European *ǵʰéw-tro-m, combining *ǵʰew- ("to pour") with the suffix *-trom.

**Descendants:**

- **Avestan:** zaoθra
- **Middle Persian:** zōhr (from Avestan)
- **Persian:** zowr
- **Sanskrit:** hotrá
- **Old Armenian:** zoh
- **Georgian:** zorva
- **Classical Syriac:** zauθrā
- **Northern Kurdish:** gorî ("victim")
- **Hindustani:** Hindi/Urdu źūn (via Persian ژُون)
```


## [2026-09-06T02:22:12.469Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD gheu ===\"; grep -n \"gheu-\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins for gheu-"
}
```


### [2026-09-06T02:22:12.521Z] TOOL RESULT

```
=== AHD gheu ===
523:gheu-
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
526:TRANSFUSE. II. Extended form *gheus-. 1. Germanic zero-grade form *gus- in: a. suffixed form *gustiz in Old Norse gustr, a cold blast of wind: cusT!; b. Icelandic gusa, to gush, perhaps akin to Middle English gushen, to gush: GUSH. 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER. III. Suffixed form *gheu-ti- in Latin fatilis, “(of a vessel) easily emptied, leaky,” hence untrustworthy, useless: FUTILE. IV. Basic form *gheu- in Greek khein, to pour: CHOANA, CHYLE, (CHYME); CHOANOCYTE, ECCHYMOSIS, PARENCHYMA. [Pok. gheu- 447.] ghéu-. To yawn, gape. Compare ghai-. 1. Germanic suffixed form g6-ma- in Old English goma, palate, jaw: GuM?, 2. Variant form *ghau- in Greek khaos, chasm, empty space, chaos: CHAOS, GAS. [Pok. ghéu- 449.] gheu(e)-. To call, invoke. Suffixed zero-grade form *ghu-to-, “the invoked,” god, in Germanic *gudam, god, in: a. Old English god, god: Gop; b. Germanic *gud-igaz, possessed by a god, in Old English gydig, gidig, possessed, insane: GIDDY. [Pok. ghau- 413.] gh6. Behind, after. Slavic *za in Russian za, by, to: SASTRUGA. [Pok. 26 451.] ghos-ti-. Stranger, guest, host; properly “someone with whom one has reciprocal duties of hospitality.” 1. Basic form *ghos-ti- in: a. Germanic *gastiz in Old Norse gestr, guest: GUEST; b. Latin hostis, enemy (< stranger): HOST?, (HOSTILE). 2. Compound “ghos-pot-, *ghos-po(d)-, “guest-master,” one who symbolizes the relationship of reciprocal obligation (*pot-, master; see poti-), in Latin hospes (stem hospit-), host, guest, stranger: (HOSPICE), (HOSPITAL), (HOSPITALITY), HOST!, (HOSTAGE), (HOSTEL), (HOSTLER). See also xenos. [Pok. ghosti-s 453.] ghow-é-. To honor, revere, worship. 1. Germanic *gaw6n in Old Norse gd, to heed: GAWK. 2. Basic form *ghow-é- in Latin favére, to favor, be favorable: FAVOR, (FAVOR- ITE). [Pok. ghou(é)- 453.] ghré-. To grow, become green. Contracted from “ghreo-. 1. O-grade form “ghré- in Germanic *grd(w)an in Old English gréwan, to grow: GROW. 2. Suffixed o-grade form *ghro-nyo- in Germanic *grénjaz, green, in Old English gréne, green: GREEN. 3. Suffixed zero-grade form *“ghro-so- in Germanic *grasam, grass, in Old English grees, grass: GRASS. [Pok. ghré- 454.] ghrebh-'. To seize, reach. 1. Zero-grade form *ghrbh- in Sanskrit grbhndati, grhndati, he seizes: SATYAGRAHA. 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen, to grasp: GRASP; b. Middle Dutch and Middle Low German grab- ben, to seize: GRAB. [Pok. 1. ghrebh- 455.] ghrebh-?. To dig, bury, scratch. 1. O-grade form “ghrobh- in: a. Germanic *graban in (i) Old English grafan, to dig, engrave, scratch, carve: GRAVE3; (EN- GRAVE) (ii) Old High German graban, to dig: GRABEN (iii) Old French graver, to engrave: GRAVURE; b. Germanic *grabam in Old English grzf, trench, grave: GRAVE}. 2. Germanic *grub(byan (with secondary ablaut) in Old English *grybban (> Middle English grubben), to dig: GRUB. 3. Germanic *gr6b6 in Middle Dutch groeve, ditch: GROOVE. 4. Perhaps Germanic *greub- in Low German greven, fibrous refuse of tallow: GREAVES. [Pok. 2. ghrebh- 455.] ghredh-. To walk, go. Suffixed zero-grade form ghrdh-yo- in: a. Latin gradi (past participle gressus), to walk, go: GRESSORIAL; AGGRESS, CONGRESS, DEGRESSION, DI- GRESS, EGRESS, INGRESS, PLANTIGRADE, PROGRESS, RE- GRESS, RETROGRESS, TRANSGRESS; b. Latin gradus (< deverbative *grad-u-), step, stage, degree, rank: GRADE; CENTIGRADE, DEGRADE, DEGREE, RETROGRADE. [Pok. ghredh- 456.] ghréi-. To rub. A derivative of gher-4. 1. Germanic *gris-, to frighten (< “to grate on the mind”), in Old English grislic, terrifying: GRISLY. 2. Germanic *grim-, smear, in Middle Dutch grime, grime, akin to the source of Middle English grime, grime: GRIME. 3. Extended form *ghris-
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1356:CHIRO- ghesor- CHIRURGEON ghesor- CHISEL kaa-id- CHITTERLINGS ku- CHLOASMA ghel-2 CHLORITE! ghel-2 CHLORO- ghel-2 CHOANA gheu- CHOANOCYTE gheu- CHOICE geus- CHOIR gher-1
1358:CHYLE gheu- CHYLOMICRON smé- CHYME gheu- CICHLID ghel-1
1360:CINCH kenk-1 CINCTURE kenk-1 CINDER sendhro- CINEMATOGRAPH kei-3 CINEMATORADIOGRAPHY kei-3 CINERARIUM keni- CINEREOUS_ keni- CINGULUM_ kenk-1 CINQUAIN penkWe CINQUE penkWe CINQUEFOIL bhel-3, penkwe cIRcA sker-3 CIRCADIAN deiw- CIRCLE sker-3 CIRCUIT ei-1 CIRCUM-  sker-3 CIRCUMCISE kae-id- CIRCUMDUCTION deuk- CIRCUMFUSE gheu- CIRCUMLOCUTION  tolkw- CIRCUMSCRIBE skribh- CIRCUMSPECT spek- CIRCUMSTANCE sta- CIRCUMVENT gWa- CIRCUMVOLVE wel-3 cIs- ko-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1426:DIET? deiw- DIFFER bher-! DIFFICULTY dhé-1 DIFFIDENT bheidh- DIFFRACTION bhreg- DIFFUSE gheu- DIG dhigw- DIGEST gerere DIGIT deik- DIGNIFY dek-1 DIGNITY dek-1 DIGRESS ghredh- DIKE dhig¥- DILATE stela- DILATORY tela- DILIGENT leg-1 DILUTE leu(@)- DIME dekm DIMENSION mé-2 DIMER (s)mer-2 DIMINISH mei-2 DIMITY mei-4
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1442:EDIBLE ed- EpicT deik- EDIFICE aidh-, dhé-1 EDIFY aidh-, dhé-1 EDITION d6- EDUCATE deuk- EDUCE deuk- EFFACE dhé-1 EFFECT dhé-1 EFFEMINATE dhé(i)- EFFERENT bher-1 EFFERVESCE bhreu-2 EFFETE dh@(i)- EFFICACIOUS dhé-1 EFFICIENT dhé-1 EFFIGY dheigh- EFFLORESCE bhel-3 EFFLUENT bhleu- EFFLUVIUM bhieu- EFFLUX bhlieu- EFFORT bhergh-2 EFFULGENT bhel-1 EFFUSE gheu- EFTSOONS apo- EGEST gerere EGG! awi-
1525:FOIL? bhel-3 FOISON gheu- FOIST penkwe
1526:FOLIAGE bhel-3 FOLICOLOUS _bhel-3 FOLIO bhel-3 FOLIUM bhel-3 FOLKMOTE mdd- FOLLICLE bhel-2 FOLLICULITIS bhel-2 FOMENT dheg¥h- FOMITE dheg¥h- FOND? bhudh- FONDANT gheu- FONDUE gheu- FONT! dhen-1 FONT? gheu- FOOD pa-
1534:FOUND! bhudh- FOUND? gheu- FOUNDER bhudh- FOUNTAIN dhen-! FOUR kWetwer- FOURTEEN kWetwer- FOURTH kWetwer- FOWL pleu-
1544:FROLIC fik-, preu- FROM per? FRONTISPIECE spek- FROST preus- FROTTAGE bhréi- FROWARD per! FRUCTIFY bhrig- FRUGAL bhriig- FRUGIVOROUS bhrig- FRUIT bhriig- FRUITION bhriig- FRUMENTACEOUS _ bhrig- FRUMENTY bhriig- FRUSTULE bhreus-2 FRUSTUM bhreus-2 FRY! bher-4 FUGACIOUS bheug-1 -FUGE bheug-! FUGITIVE bheug-1 FUGLEMAN man-1, pleu- FUGUE bheug-! FUHRER per-2 FULCRUM bhelg- FULGENT bhel-1 FULGURATE bhel-1 FULIGINOUS dheu-1 FULL! pele-1 FULMAR pu-2 FULMINATE bhel-1 FUMARIC ACID dheu-1 FUMAROLE dheu-1 FUMATORIUM dheu-! FUMATORY dheu-1 FUME dheu-! FUMIGATE ag-, dheu-! FUMITORY dheu-1, ters- FUNAMBULIST al-2 FUNCTION bheug-2 FUND bhudh- FUNDAMENT bhudh- FUNDUS_ bhudh- FUNGIBLE bheug-2 FUNNEL gheu-
1547:FUSE? gheu- FUSILE gheu- FUSION gheu- FUTILE gheu- FUTURE bheue- FUZZY pu-2
1560:GEODE gé GEODESY da- GEOMETRY mé-2 GEOPONIC (s)pen- GEORGIC gé, werg- GERANIUM gera-2 GERENT gerere GERIATRICS gera-1 GERM gene- GERMAN? gena- GERMANDER deru, dhghem- GERMANE gene- GERMINAL gene- GERMINATE gene- GERONTO- gera-1 GERUND gerere GEST gerere GESTALT stel- GESTATION gerere GESTICULATE gerere GESTURE gerere GET ghend- GEYSER gheu- GHAT gher-4 GHOST gheis- GIDDY gheu(e)- Girt ghabh- GILD! ghel-2 GILL! ghel-una GILLS ghai- GILLYFLOWER bhel-3, kar-1 GILT2 ghel-3 GIMMAL yem- GINGERLY gene- GIRASOL sawel- GIRD gher-1 GIRDLE gher-1 GIRTH gher-1 GIST yé-
1572:GUN gWhen-1 GURGITATION gWere-4 GURU gWera-2 GUSH gheu- Gust! gheu- GusT2 geus- GUSTO geus-
1573:GUT gheu- GYMNASIUM nogY- GYMNAST nog¥- GYMNOSOPHIST nogW- GYMNOSPERM nog¥- GYNAECEUM gWen- GYNECOCRACY gWen- GYNECOLOGY gWen- GYNO- gWen- -GYNOUS gWen- -GYNY gWen- GYRE géu-
1678:INERTIA ar- INEXORABLE 6r- INFAMOUS bha-2 INFANT bha-2 INFANTRY bha-2 INFARCT bhrekw- INFECT dhé-1 INFELICITY dhé&(i)- INFER_ bher-1 INFERIOR ndher- INFERNAL ndher- INFERNO ndher- INFEST dhers- INFEUDATION peku- INFIDEL bheidh- INFIRM dher-2 INFIRMARY dher-2 INFIX dhigw- INFLAME bhel-1 INFLATE bhié-2 INFLICT  bhiig- INFLUENCE bhieu- INFLUENZA bhleu- INFRA- ndher- INFRACT bhreg- INFRANGIBLE bhreg- INFRINGE bhreg- INFUSE gheu- INGENIOUS gene- INGENUOUS gene- INGEST gerere INGRATE gWere-3 INGRATIATE gWere-3 INGRESsS ghredh- INGUINAL engW- INGURGITATE gWere-4 INHABIT ghabh- INHERE ghais- INHERIT ghé- INHIBIT ghabh- INHUME dhghem- INIMICAL amma INITIAL ej-1 INITIATE ei-1 INJECT yé- INJUNCTION yeug- INJURY yewes- INK kéu-
```


## [2026-09-06T02:22:14.166Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW fundo ===\"; grep -n \"fundo, -ere\\|fundö\\|fundo,\" LEW_1910.txt | head -6; echo \"=== LAT fundo ===\"; grep -n \"fundo\" LAT.txt | head -6; echo \"=== SYN pour ===\"; grep -n \"ghgeu\\|gheu\\|χέω\" SYN.txt | head -6",
 "description": "Grep Latin dictionaries for fundo"
}
```


### [2026-09-06T02:22:14.248Z] TOOL RESULT

```
=== LEW fundo ===
=== LAT fundo ===
13355:synonyme de corripio, confundo. An sena fignre: composer soignensement
18399:effu(t)tl 5 :v. fut is sous fundo.
19644:ex futi: effusi, ut mertat pro mersat, P.F. 71,13. V. fundo.
19808:gh- devant u: y. fundo.
20826:pente soit encore sensible, e.g. Q.C.4,2,19, iamque a fundo maris in- 389
23354:Rattache par les inciens a fundo, cf.P.F.74,38, sans doute a cause
=== SYN pour ===
14575:with extension *gheud-. cae Ernout-M. 440 f. Walde- ‘ ldo LOST. xbvw (new present to
```


## [2026-09-06T02:22:29.400Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"INGOT [a-z-]*\\|NUGGET [a-z-]*\\|GEYSER [a-z-]*\" AHD_watkins1985.txt | head; echo \"=== SKT ingot/nugget/geyser ===\"; grep -n \"^Ingot\\|Ingot,\\|Nugget\\|Geyser\" SKT.txt | head",
 "description": "AHD index for ingot/nugget"
}
```


### [2026-09-06T02:22:29.466Z] TOOL RESULT

```
1560:GEYSER gheu-
=== SKT ingot/nugget/geyser ===
12501:Nugget,  a  lamp  of  metal.  (E.)  Formefly niggott  sec  Trench,  Eng.  Past  and  Present. Prob.  a  corraption  of  uingot,  pnt  for  ingot  \ sec  Xn^ot.
```


## [2026-09-06T02:22:29.767Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ingot",
 "prompt": "Quote etymology of ingot and any mention of nugget."
}
```


### [2026-09-06T02:22:35.091Z] TOOL RESULT

```
# Etymology of Ingot

According to the Online Etymology Dictionary, **ingot** originates from the late 14th century and comes from a combination of sources:

"late 14c., 'mold in which metal is cast,' probably from in- (2) 'in' + Old English _goten_"

The word's evolution shows that the original sense referred to the mold itself, but this meaning became obsolete. The more familiar modern usage emerged in the early 15th century: the "mass of cast metal" definition that we use today.

The term traces back through Old English _geotan_ (meaning "to pour") to the Proto-Indo-European root *gheu-, which means "to pour, pour a libation."

## Regarding "Nugget"

The provided content does not contain any mention of the word "nugget" or its etymology, so I cannot provide information about that term based on this source.
```


## [2026-09-06T02:22:42.805Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN zor ===\"; grep -n \"zōr\\|zaoθra\\|zaothra\\|Weihwasser\" HRN.txt | head -10; echo \"=== HUB ===\"; grep -n \"zōr\\|zaoθra\\|Weihwasser\\|zaothra\" HUB.txt | head -10",
 "description": "Horn/Hübschmann for zor"
}
```


### [2026-09-06T02:22:42.875Z] TOOL RESULT

```
=== HRN zor ===
5955:675. {^i)zör 'Weihwasser (pärsisch).
5956:aw. zaotirä' 'Weihwasser*; phlv. zölir, zur, arm.
=== HUB ===
7328:'Weihwasser (Parsenwort !) == paz. zor Min. Gl. 225, phi.
7330:kuchen', zd. zao&ra- 'Opferspende, Opfertrank, Weihwasser.
7890:zd. zavare; zDr *Weihwasser' {g^h) H. 675, Parsenwort;
```


## [2026-09-06T02:22:44.100Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"کیمیا\\|زور\" ARY_pages.txt | head -12; echo \"=== latin index ===\"; grep -n -i \"GHEU\\|FUNDERE\\|CHEM\" ARY_latin_index_pages.txt | head -10",
 "description": "Aryanpur for kimiya/zur"
}
```


### [2026-09-06T02:22:44.177Z] TOOL RESULT

```
4401:سنا زورون مس سس
5388:۳۸۸1-۸1727۸7 (به چم "قوت" و "زور") می‌داند (برهان قاطع : ۴۳۹) یی
6572:۲ چم اين واژه در زبان‌های ژرمنی کهن "گرفتن" برده ولی در زبان‌های ژرمی نوین چم آن اپا زور بلند کردن*
9732:۱ واژه‌ی زور" به چم "آب مقدس که در مراسم زرتشتی پاشیده می‌شود" نیز از همین واجریشه است
9754:زور (به چم "نادرست و دروغ") / ۳۳۱
13366:31۸5۵ اسلواکی (51.07420)+ زورید )۱
14394:سغدی (/800/0140): 01 سوئدی (57520/57): زور 1
=== latin index ===
9543:GIOTA (SWEDISH) (543 yo FUNDO, FUNDERE = (LATIN) «3
10138:NIEZEN DUTCH) gala PHARCHEM ARMENIAN) +!
10946:REFERENCES both FUNDERE LATIN) 3
11558:3(OLD SCANDINAVIAN) nS gheu) CARUS LATIN) 3
12785:QUETHAN, QUATH KOCHEM :(ARMENIAN) |g |
12807:GARDLO (POLISH) glo) GERU, GHEURI, GHEURD
```


## [2026-09-06T02:22:52.104Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '9700,9745p' ARY_pages.txt; echo \"--- page tag ---\"; awk 'NR<=9732 && /\\[pdf page/ {p=$0} END{}' ARY_pages.txt; grep -n \"\\[pdf page\" ARY_pages.txt | awk -F: '$1<9732' | tail -2",
 "description": "ARY context for zur holy water"
}
```


### [2026-09-06T02:22:53.780Z] TOOL RESULT

```
ایركدی کهن (#فل#/ 012): ۰ 810 ,8850 256 تلا
ولزی (84 )+ نان 1 (01100) :0/05
برتونی (/87870): 13۸ 2 (01100) 357
گالیکه (0۸81]70): ند 3 (۸778) ۸400
برهان قاطع : 1.۸۳
بادداشت:
۱- چم این واژه در زبان آلمانی نوین؛ سرزنده.
چم این واژه در زبان هلندی: جیره.
۲- یکی از چم‌های واژه‌ی انگلیسی 011101 زنده.
۳ بازگلت به: زیستن.
2۸07۸ ,207
اوستایی (47887۵/۷): فریزی کهن ((۲۷۹1۵ 010): 17۸
خ2۸07118 بال2۸07۸ آلمانی کهن (/(08704۸ 2۷/0 ۵ا۵):
1 پهلوی (1شالتم۳۸): 7207 ۸ ,61022۸
هو «سانسکر یت (8۸/51077): آلمانی (0874۸۷): ود ند ان
20306 ,103011 انگلیسی کهن (2۸0/1 012): ۰ 0807۸05 ۱
ارمنی (۸//8142): 7 ب,08[ انگلیسی (8لا600): 0
یونانی 078850): 60 ,01852۸ دانمارکی (0۸۷/80): 0052
لانین (7/0): ۰ ۲۲۵۲۶۵ ,57۸00 سوئدی (91752154): 207۸
گرتیکد (ع00771): 01137۸ نروژی (/087801۸): 207۸
ایسلندی کهن (/504(/210۸71۸۸ 00): هلندی (0ل07): 0 ,0007
۸ ,978ت0۲ 60107۸ لیتوانی (۸(/1۸/۷تا777):
[pdf page 329]
ُ
ا
۰ زود ۱
6۸1 ,۷۸85 پسگشت‌ها ده اد اد ی
لتونی (لتی) ((477۸ل): ات 48 200200
9 (07) 2 ۸ :22( ها
کک هام ۹ جهمی روم 1
۱ لغت‌نامه دهخدا: ۱۳۲ ا
یادداشت: ی
۱ واژه‌ی زور" به چم "آب مقدس که در مراسم زرتشتی پاشیده می‌شود" نیز از همین واجریشه است
(اوستابی:2۸0711۸؛ پهلری: 2:013). ۱
۲ چم این واژه در زبان‌های ژرملی و زبان لاتین: جاری شدن؛ آبگونه شدن. ۱
۳ چم این واژه در زبان ارمنی: آبکند» دره, :
۳ ا
اوستایی (47887/400): ۸ ,701 ایسلندی کهن (/54(/0/0141 0ا۲)0شاید)
پارسی پاستان (۳8۴۹1۵۸۷ صا0): 717۸ ده
پهثری (1لاماتا۸ه). 0 ,701
کردی (00/5(7): 71711 ,211 ,275 رنآ2 پسگشت‌ها از ادن ۲
بلرچی (//4۲0): ۰ 21773 ,217 ,207 9 ۸0800
اففانی (پشتو) (۸۳017۸(۷1): 2 9 (01166) :2ل52 ۸لز
سانسکریت (84۸/5507): 2.1317771 ب۳۸لآل برهان قاطع : ۱۰۳۳
یادداشت: ۰
شاید این واژه‌ها هم از همین واجريشه باشند: گرتیکه: 8 آلمانی کهن: 98۸7؛ انگلیسی کهن:9021۸ انگلیسی:
--- page tag ---
9692:[pdf page 328]
9722:[pdf page 329]
```


## [2026-09-06T02:23:21.432Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/fuse",
 "prompt": "Quote the etymologies of fuse (n.) and fuse (v.), including the electrical sense date, and mention of Latin fusus/fundere. Also quote funnel if present."
}
```


## [2026-09-06T02:23:22.485Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/refuse",
 "prompt": "Quote the etymology of refuse (v.) and refuse (n.), including Old French refuser, Vulgar Latin *refusare and Latin refundere 'pour back'."
}
```


### [2026-09-06T02:23:27.778Z] TOOL RESULT

```
# Etymology of "Fuse"

## Fuse (noun)
The noun form originated in the 1640s: "combustible cord or tube for lighting an explosive device," derived from Italian *fuso*, meaning "spindle." The term referenced the device's elongated shape, as early versions were thin tubes filled with gunpowder. A later meaning emerged in 1884: "device that breaks an electrical circuit," also named for its shape, though incorrectly attributed to the verb form since it melts.

## Fuse (verb)
Dating to the 1680s, the verb means "to melt, make liquid by heat" (transitive), originating as a back-formation from *fusion*. The intransitive sense ("become liquid") appeared by 1800, while the figurative meaning—"blend different things, blend or unite as if by melting together"—is recorded by 1817.

## Latin Roots
Both forms connect to Latin *fusus* ("a spindle") and *fundere* ("to pour, melt"), linking etymologically to the concept of liquefaction and blending.

**Note:** The provided content does not include an entry for "funnel," so that term cannot be quoted here.
```


### [2026-09-06T02:23:27.836Z] TOOL RESULT

```
# Etymology of Refuse

**Refuse (v.)** derives from Old French *refuser* ("reject, disregard, avoid"), which came from Vulgar Latin *\*refusare*, a frequentative verb. This traces back to Latin *refundere*, meaning "give back, restore, return," literally "pour back, flow back." The Latin term combines *re-* ("back") with *fundere* ("to pour").

**Refuse (n.)** similarly originates from Old French *refus* ("waste product, rubbish; refusal, denial, rejection"), formed as a back-formation from the past participle of *refuser*. It shares the same Vulgar Latin and Latin roots as the verb.

As the source notes: *refuser* stems from "Vulgar Latin *\*refusare*, a frequentative verb from the past-participle stem of Latin *refundere* 'give back, restore, return,' literally 'pour back, flow back.'"
```


## [2026-09-06T02:23:39.839Z] TOOL CALL #57: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵʰew-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/ȷ́ʰáwtram\" \\\n \"https://www.etymonline.com/word/alchemy\" \\\n \"https://www.etymonline.com/word/geyser\" \\\n \"https://www.etymonline.com/word/ingot\" \\\n \"https://www.etymonline.com/word/fuse\" \\\n \"https://www.etymonline.com/word/refuse\" \\\n \"https://en.wiktionary.org/wiki/كيمياء\" \\\n \"https://vajehyab.com/moein/رفوزه\" \\\n \"https://abadis.ir/fatofa/فیوز/\" \\\n \"https://abadis.ir/fatofa/شیمی/\" \\\n \"https://abadis.ir/fatofa/زور/\" ; do\n timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 192, root Gheu 1 (PIE *gheu- to pour): zaothra/zor, fundere/fuse/refuse, Germanic geyser/ingot, Greek khymeia > Arabic al-kimiya > Persian kimiya/shimi\" 2>&1 | tail -2\ndone",
 "description": "Archive all web sources used"
}
```


### [2026-09-06T02:23:49.386Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/818a652f5d00769b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e61e22cbe7449e50.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ed0657329df3c84e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1ead28e37532efad.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8a5527e7580bab74.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/add2081ff3770534.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9b3d646ecdcccebc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/66c3eaba5abf4bda.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a44958ec2072cd4b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d4d0939c301a15da.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/58639a853733ee7e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb01aa8c59580f01.txt
```


## [2026-09-06T02:23:57.105Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD vol1 alchemy ===\"; grep -n \"alchemy\" FSD_vol1.txt | head -3; echo; echo \"=== LKT alchimie/kimiya ===\"; grep -n -i \"alchimie\\|kimija\\|kīmījā\\|kimiya\" LKT.txt | head -6",
 "description": "FSD and Lokotsch for alchemy"
}
```


### [2026-09-06T02:23:57.175Z] TOOL RESULT

```
=== FSD vol1 alchemy ===
11252:to,  or  produced  by  means  of  alchemy.
11256:al'che-mist,  1   al'ki-mist;  2   ftl'ce-mtst,  n.  One  who  was skilled  in  or  who  practised  alchemy.
11258:al'clie-mlst-erf;  al'chy-mlstt.—  a!wcho-inls'tIc,a.  Of  or pertaining  to  alchemy  oralchemlsts;  practlslngalchemy.  al"- che-mls'tl-calt;  al"chy-mls'ticj.  —   al"che-mls'ti-cal- ly,  adr.—  al-chem'Is-try,  n.  Alchemy.  al-chym'Is-tryt.

=== LKT alchimie/kimiya ===
2718:Od.  klmt,  kopt.  kemi  'schwarz'  war  die Bezeichnung  des  Landes  Ägypten  [dar- aus auch  der  Name  des  dritten  Nach- kommen Noas,  Harn  'der  Schwarze', hebr.  allerdings  in  'der  Heiße'  umge- deutet] ;  hieraus  entstand  ar.  ktmija' zunächst  zur  Bezeichnung  des  'Steins der  Weisen'  [also  im  Sinne  von  ikslr, s.  hier  Nr.  903,  gebraucht,  vgl.  GILDE- MEISTER in  ZDMG  XXX,  534/538], dann  'Scheidekunst,  Chemie'.  Aus  dem Ar.  kommt:  it.  alchimia  'Goldmacher- kunst' [fast  synonym  zu  inganno  'Be- trug'], alchimia  'ein  aus  Messing,  Kupfer und  Erz  zusammengesetztes  Metall', modern  chimica,  arte  chimica  'Chemie', frz.  alnhimie,  chimie,  sp.  pg.  alqtdmia; dtsch.  Alchimie  [für  Alchimisterei  heißt es  bei  Schuppius  zur  Verspottung  dieser Afterwissenschaft  ungemein  treffend : 'Allkühmisterei',  vgl.  Andresen  DVE  34], Chemie,  ndl.  alchimie,  engl,  alchemy,  al- chimij,  Vb.  to  alchemise,  chimistry.  — [Die  ar.  Lexikographen  leiten  ar.  kimija' vom  Vb.  kamä  'verbergen'  ab,  also  im Sinne  von  'verborgener  Kunst'.]  [POTT in  ZDMG  XXX,  6/20.  Mahn  EtUnt  81/85. Devic  DEt  7.    Kluge  10.
5708:.4?awrtc  St.  75 Albatros  1)88 Alchabor  St.  12 Alchimie  1157 Aldebaran  St.  451 Aleppin  792 Algebar  St.  629 Algebra  631 Algedi  St.  035 Algenib  St.  664 Algomeiza  St.  749 ^Z^^oZ  St.  741 Algorab  St.  754 Alhabor  St.  12 Alhajoth  St.  41 Alhidade  896 Alizarin  116 Alkakandschi  1016 ^ZA-«?i  1029 ^/fro/io?  1227 Alkoran  1250 Alkoven  1221 ^/^«/t  59 Alleluja  793 alligaßr  mhd.  2229 Abnagest  1348 Almanach  1389 Almemor  j.  1461  a Alphard  St.  587 Alpherath  St.  586 Alpheraz  St.  586 Alpheta  St.  574 ^/<«/r  St.  1575
6240:alchimie  1157
```


## [2026-09-06T02:23:58.835Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC gheu ===\"; grep -n \"ghèu-\\|gheu-\\|gheumn\" IEC.txt | head -8; echo \"=== WLD Bd1 gheu ===\"; grep -n \"ĝheu-\\|gheu-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -8",
 "description": "Mann and Walde-Pokorny for gheu-"
}
```


### [2026-09-06T02:23:58.903Z] TOOL RESULT

```
=== IEC gheu ===
5684:£euos (ĉeu-) ‘rush, gush, flow’. Cf. gheu-,
6135:$hu- radical theme of types gheu-, 8hou-, $huuó, q. V.
6159:8huuo (1) *pour, shed, cast, scatter, destroy'. Form of gheu-, q. v. Gk. cf. khúto “was poured'; khümenos, pt.; cf. khudaios ‘poured; vulgar; Li. Züvu, Son ‘perish’
=== WLD Bd1 gheu ===
33311:182 und Persson Beitr. 118; sonst meist zu gheu- „gie6en 44 gestellt, s. d.), 
33346:LEWb. 2 71. — Unbegriindet ist Hirts Identifizierung von tjhaua- mit gheu- 
33350:seiner Bedeutung wegen nicht hierher, sondern zur ]/" gheu-ghou- zu ziehen ; 
34693:trocken, gelt" von der Basis gheu-11 S. Falk-Torp u. gissen, Persson 
35426:geu- — gheu- 
35459:gheu- ,.gieBen“. 
35473:gheu- „gieBen“ bei Bartholomae BB. 17, 99, 101, Hiibschmann aaO.); hier- 
35555:gheu- : gho(u')- : ghsu-
```


## [2026-09-06T02:24:07.978Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11248,11256p' FSD_vol1.txt; echo \"=== which leaf/page ===\"; python3 - <<'EOF'\nt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read()\nimport re\nidx=t.find(\"al'che-mist\")\nprint('leaf', t[:idx].count('\\f'))\nEOF",
 "description": "FSD alchemy entry"
}
```


## [2026-09-06T02:24:08.564Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '35455,35480p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "WLD gheu- entry"
}
```


### [2026-09-06T02:24:09.846Z] TOOL RESULT

```
Al"ca-Ia',  1   ol'Ka-Id';  2iU'ca-Ui',  n.  1.  A   town  In  Cagayan province,  Luzon,  P.  I.  2.  A   town  In  Pangasinan  province, Luzon,  P.  I.
Al"ca-la'  de  Hc-na'res,  1   dg  e-nfi'rgs;  2   da  fc-n&'res.  A   town in  New  Castile,  Spain,  the  birthplace  of  Cervantes.
Al"ca-la'  la  Re-al',  l   la  rg-ol';  2   la  re-al' .   A   city  in  Andalusia (Jaen  province).  Spain.
al-cal'de,  1   al-kal'ds  or  al-kal'dr,  2   al-cal'de  or  51-cai'de,  n.
to,  or  produced  by  means  of  alchemy.
And  jealousy  Hath  in  it  an  alchemic  force.
Tennyson  Queen  Mary  act  Hi,  sc.  0. al-chem'i-caU;  al-chym'lcj.—  al-chem'I-cal-ly,  adv.
Al"che-mll'Ia,  1   arki-mil'o;  2   fil’ce-mll'a,  n.  A   genus  of plants  of  the  rose  family  ( Rosacex ),  having  compound  or lobed  leaves  and  small  green  or  yellow  flowers:  Including  tho Jady's-mantle.
al'che-mist,  1   al'ki-mist;  2   ftl'ce-mtst,  n.  One  who  was skilled  in  or  who  practised  alchemy.
=== which leaf/page ===
leaf 107
```


### [2026-09-06T02:24:09.900Z] TOOL RESULT

```
Abzulehnen ist die Vereinigung von geul- etwa unter geuel- (Zupitza 
aaO. zw., Uhlenbeck EWb. 104) mit ai. jvalati (s. unter guer-) und aksl. 
glavbnja (s. Berneker, SlEWb. 324 f.). 

gheu- ,.gieBen“. 

Ai . julwti, juhutc „gie£t ins Feuer, opfert", Passiv TiuydtU, hutd „geopfert', 
homan n. „OpferguB, Opfer ', homo, m. ds., Mtr „Opferer, Priester", liotrd 
n. „Amt der Hotr'-, hotra f. .,Opfergabe ', havis n. ds., havu m. „Opfer“, 
hdiana n. ds., ahuti „OpferguB“; av. zaotar , zaoftr- m. „Priester, Opfer- 
priester , mp. zot, av. zaodra n., zaodrd „flussige Opferspende, Opfertrank, 
OpferguB", up. sdr ,,Weihwasser“ (Horn, Np. Etymol. 675), av. azUtuy-f. 
„Fett, Schmalz, Uppigkeit, strotzende Fiille". 

Arm. joyl .,gegossen“ ( <jjheulo -, goulo-), jew .,Form, Gestalt *, s. Meillet 
Hsl. 9, 54, Hiibsckmann Arm. Gr. I 469 (aber jaunem „weihen‘ gehort wie 
n-zovk „Fluch' zu gliau „rufen‘' vgl. Osthoff BB. 24, 182, Persson Beitr. 
118; Zweifel an der iiblichen Einreihung von jaunem in die Sippe von 
gheu- „gieBen“ bei Bartholomae BB. 17, 99, 101, Hiibschmann aaO.); hier- 
her auch jor ,,Tal“ (< ghouero) nach Petersson LUA 1920, 3, 1 06 f. ? 

Gr. ysco ,.gieBe“, Aor. Horn, e'yeva < *syevoa (W. Schulze Quaest. epic. 
62 f.), yvxog „gegossen“, yev/aa ,,GuB, FluB, Trankopfer' (spat yvya „GuB, 
FluB, Strom'), yoavog, y/ovog „Schmelzgrube, GuBform', yoi) „Gu8, Aus- 
gieBung, Libation', yosvg „MaB fur Flussigkeiten'-, you? ds., yoog' yovg, 
yCojxn Hes., darauf beruhend *yooeo (s. W. Schulze KZ. 29, 265) und ycov-
```


## [2026-09-06T02:24:18.758Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"che-my\\|chymia\\|khymeia\\|chemeia\\|Chemeia\" FSD_vol1.txt | head -8",
 "description": "FSD alchemy etymology"
}
```


### [2026-09-06T02:24:18.821Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:24:22.064Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[107]\ni=p.find(\"al'che-mist\")\nprint(p[max(0,i-3000):i+500])\nEOF",
 "description": "FSD leaf 107 context"
}
```


### [2026-09-06T02:24:23.683Z] TOOL RESULT

```
ero,  of  pure,  noble  mind,  sorely  vexed  by  the  sight  of
An  alcalde.  perfidy  and  malevolence  disguised  na  politeness.
Al'cm,  1   al'sl;  2   iU'cS,  n.  pi.  The  Alcidx  as  a   suborder.  Alces'ter,  1   ols'tor  or  Cs'tor;  2   ais'ter  or  as'tcr,  n.  1.  A   town Al-cae'us,  1   al-sl'us;  2   S.l-c5'us,  n.  1.  A   Greek  poet  of  Mity-  in  Warwickshire,  England.  2.  The  ruins  of  a   city  of  Roman
Iene;  lived  about  600  B.  C.  See  Alcaic.  2.  A   Greek  epi-  BrltaiD,  lVa  m.  S.  W.  of  Bicester.
grammatlst  of  Messene  in  the  2d  century  B.  C.  3.  The  A!-ces'tls,  1   al-sos'tls;  2   ftl-cC-s'tls,  n.  Myth.  A   daughter  of pen-name, and  sobriquet  of  James  Montgomery.  [etc.  Pellas  who  voluntarily  died  to  save  the  Ufo  of  Admetus.  her
al'ca-hcst,  al"ca-hes'tlc  or  -tl-cal.  Same  as  alkahest,  husband,  and  was  brought  back  from  Hades  by  Hercules,
Al-ca'Ic,  I   al-ke'ik;  2   ill-ca'ic,  a.  1.  Of  or  pertaining  to Alcaeus,  a   lyric  poet  of  Mitylenc  (about  600  B.  C.).  2.
Pros.  Having  the  characteristics  of  the  meter  of  Al- effius;  as,  the  Alcaic  ode,  an  ode  of  four  strophes,  each
or,  according  to  another  version  of  the  story,  by  Proserpine. The  legend  is  the  subject  of  a   tragedy  by  Euripides,  and  Is mentioned  in  the  Prolog  to  Chaucer’s  Legends  of  Goode  Wo- men, and  In  a   sonnet  by  Milton.
Cious;  na,  uuc  aicuic  uuu,  jiu  uuc  umi  nnuunva,  wuu  -   « .....  n „   ,   \   i   ».i  r,  yi  y   /•  r\t  —   *   -   •  
strophe  containing  four  verses,  and  each  verse  having  al"cheni  lc,  1   al-kem  lk;  2   &l-cSm  tc,  a.  Of,  pertaining
four  accents.
Al-ca'Ics,  n.  pi.  Verses  written  in  Alcaic  strophes,-
al-caldc',  1   al-ked';  2   ill-cild',  n.  1.  The  governor  or  com- mander of  a   Spanish.  Portuguese,  or  Moorish  castle  or  other fortress.  2.  The  warden  of  a   prison:  a   Jailer.  [<  Sp. alcalde,  <   Ar.  al*qdld,  <   al,  the,  -f  qaid,  commander,  < qdda.  lead.]  al-cald'j;  nl-cayde'j.
Al"ca-Ia',  1   ol'Ka-Id';  2iU'ca-Ui',  n.  1.  A   town  In  Cagayan province,  Luzon,  P.  I.  2.  A   town  In  Pangasinan  province, Luzon,  P.  I.
Al"ca-la'  de  Hc-na'res,  1   dg  e-nfi'rgs;  2   da  fc-n&'res.  A   town in  New  Castile,  Spain,  the  birthplace  of  Cervantes.
Al"ca-la'  la  Re-al',  l   la  rg-ol';  2   la  re-al' .   A   city  in  Andalusia (Jaen  province).  Spain.
al-cal'de,  1   al-kal'ds  or  al-kal'dr,  2   al-cal'de  or  51-cai'de,  n.
to,  or  produced  by  means  of  alchemy.
And  jealousy  Hath  in  it  an  alchemic  force.
Tennyson  Queen  Mary  act  Hi,  sc.  0. al-chem'i-caU;  al-chym'lcj.—  al-chem'I-cal-ly,  adv.
Al"che-mll'Ia,  1   arki-mil'o;  2   fil’ce-mll'a,  n.  A   genus  of plants  of  the  rose  family  ( Rosacex ),  having  compound  or lobed  leaves  and  small  green  or  yellow  flowers:  Including  tho Jady's-mantle.
al'che-mist,  1   al'ki-mist;  2   ftl'ce-mtst,  n.  One  who  was skilled  in  or  who  practised  alchemy.
There  was  an  old  belief  that  .   .   .   cunning  afchemiit* Could  recreate  tho  rose.  Longfellow  Palingenesis  st.  4.
al'clie-mlst-erf;  al'chy-mlstt.—  a!wcho-inls'tIc,a.  Of  or pertaining  to  alchemy  oralchemlsts;  practlslngalchemy.  al"- che-mls'tl-calt;  al"chy-mls'ticj.  —   al"che-mls'ti-cal- ly,  adr.—  al-chem'Is-try,  n.  Alchemy.  al-chym'Is-tryt.
-   —   -   “
```


## [2026-09-06T02:24:33.316Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor L in (107,108):\n    p=pages[L]\n    for m in ('chem','chym'):\n        import re\n        for mm in re.finditer(r'.{80}'+m+r'.{200}',p):\n            s=mm.group(0)\n            if '<' in s or 'Ar.' in s or 'Gr.' in s:\n                print(L,'|',s.replace('\\n',' ')[:320]); print('--')\nEOF",
 "description": "FSD alchemy etymology bracket"
}
```


### [2026-09-06T02:24:35.003Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:24:43.714Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM ===\"; grep -on \".\\{0,80\\}كيميا.\\{0,120\\}\" AFM.txt | head -4; echo \"=== TAD ===\"; grep -on \".\\{0,60\\}كيميا.\\{0,140\\}\" TAD.txt | head -4; echo \"=== PLA ===\"; grep -n -i \"kīmiyā\\|kimiya\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -4",
 "description": "Arabic-loan dictionaries for kimiya"
}
```


### [2026-09-06T02:24:51.462Z] TOOL RESULT

```
=== AFM ===
ugrep: error: error at position 87
0-\xbf][\x80-\xbf]*){0,120}
                           \___exceeds complexity limits


=== TAD ===
ugrep: error: error at position 87
0-\xbf][\x80-\xbf]*){0,140}
                           \___exceeds complexity limits


=== PLA ===
17353:Go - kimawi = kimiyawi q. v. 
17363:G,.3- kimaw = kKimiyawi q. v. 
17373:SL. - kimiyawi: Nisba v. kimiya q. v.
```


## [2026-09-06T02:24:54.459Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17340,17395p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== kimiya main ===\"; grep -n \"kimiya:\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head",
 "description": "Asbaghi kimiya entry"
}
```


### [2026-09-06T02:24:54.521Z] TOOL RESULT

```
- _-__ ._n Y - _ 
ob kil-däru: "Farnkräuter" pers. „2° gildäru, aram. 


ı mand. kisa, syr. 


wi 
a5\3- kailaga = kailafa q. v., aram. bo. 


7 -_ = = 102. 
Go - kimawi = kimiyawi q. v. 


Too 5 
<es- kimuht: "Ruhe" pers. ?. 


I. - 


G,.3- kimaw = kKimiyawi q. v. 


>41 


Le» - kimiyä: "Chemie" pers. 675, 


5 - ,_ 
SL. - kimiyawi: Nisba v. kimiya q. v. 


“ -_—_.._ -_ 
sLeJ- kImiyäwiyya: s. I. kimiyä q. v. 


oJ - 


a Pr 
AwS2)- lahsa: "eine Speiseart", pers. 


4 


Wahrmund s. v., Chista Bd. 10 s. 
Macuch S. v. 

Muhit s. v., Fraenkel s. v. 

Löw s. v. 
=== kimiya main ===
```


## [2026-09-06T02:25:05.040Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"fundö\\|fund5\\|fundo, -is\\|fundo,-is\\|^fundo\" LAT.txt | head -8; echo \"---\"; grep -n \"gheu\\|χέω\\|xew\\|giessen\\|gieBen\" LAT.txt | head -8; echo \"=== LEW ===\"; grep -n \"fundo\" LEW_1910.txt | head -8",
 "description": "Ernout-Meillet fundo"
}
```


### [2026-09-06T02:25:05.119Z] TOOL RESULT

```
24821:fundo
24856:fundo, -is, ftidi," fQsura , fundere: verser, repandre. Correspond
24889:fundo, M.L.8054a.
---
24882:(= Trepoxew) > confundi: verser enseable, et "confondre" (cf. o\>YX ew ) >
32504:meme sens; delatro; elatra "crier avec force" (Hor., cf. ef^uAcotxew,
38096:croate miSam ^galement; de meme aussi gr. 0(xlxew, A cot<? de ocp.u!;ai,*
59293:= TtpocrrfxewJ r 4 sonner vers,‘ r 4 pondre en 4 cho, faire retentir; et,
=== LEW ===
```


## [2026-09-06T02:25:07.455Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24856,24895p' LAT.txt",
 "description": "Ernout-Meillet fundo entry"
}
```


### [2026-09-06T02:25:07.507Z] TOOL RESULT

```
fundo, -is, ftidi," fQsura , fundere: verser, repandre. Correspond
a gr.yeu), se dit des liquides, et specialeaent d'un metal en fusion,
de 14 le sens technique de "fondre", conservi dans les 1 . romanes. Par
analogie s'est appliqu^ k toute espfece d'objets, aat^riels ou non,
qui se repandent d'une aanifere r^gulifere et ininterroapue (grains,
sons, laraes, odeurs, paroles, rayons, luaifere, vents, etc.: cf./luo);
d'ofc le sens de "produire en abondance" (se dit de la terre); g° terae
technique de la 1. ailitaire "disperser, aettre en fuite" (souvent
joint k fugdre avec lequel il allitfere). Pronoainal: sd fundere : "se
repandre, s'£tendre au loin". Pcp.: fusus "qui se r^pand, diffus,
prolixe". - Dsit 4 de tout teaps, M.l.3581; celt.: gall. fynnu, etc.;
cf. peut-etre aussi 3583,3584 *fundidre, *fundicdre.
Derives en fund- et en fus-: fundibulum: entonnoir, M.l.3583, sans
doute refait' sur le compos^ plus ancien infundibulum,', fusio (rare);
non atteste avant Cic., N.D.i,15,39, dans un passage sans doute traduit
du grec: Chrysippus ipsum mundum deum dicit esse et eius animi fusionem
(= x UCTI,v ) uniuersam', conservi dans le fr. foison. M.1.3613. les coapo-
ses con-, dif-, ef-, pro-, trdns-fusio sont au contraire usit^s.
Cf. aussi fusiondticum: uXioti,xov (Gloss.); fusor, t. technique: fon-
deur en a^taux; fusilis : fusible; fusura: fonte, fusion (Plin.);fundo
- 4 C 4 -
fusus,-us a.: rare, ne seable pas attestO en dehors de Varr.,L.L.
5,133, fons unde fund-itur e terra aqua uiua, ut fistula a qua fusus
aquae', fusSrius: )(U)v£UTi.x6c, qui se «et en fusion (Gloss.); fusorium i
Ovier.
CoaposOs de fundo' af-fundS ( affuso,-as, M.L.afiya); circumfundo
(= Trepoxew) > confundi: verser enseable, et "confondre" (cf. o\>YX ew ) >
M. L. 3141 confus iS = cruyxucn,c; dSfundi "tirer" du vin (= xa-ta^eto) ,
M.L.3531; dif-fundo ( = 5 id^eo)); effundi (= exyjEM); infundi (= eyxeoj),
M.L.4415; interfundo', offundo "rOpandre devaat soi, envelopper", per¬
fundi "verser Xtravers, inonder" M.L.6410; praefundi (rare, postelass.);
prifundi "rOpandre en abondance" (= 7ipo^ew); refundo "reverser, refou-
ler, rejeter, rendre liquide" M.L.7163; suffundo (= UTiO)(e<jo ); trans¬
fundo, M.L.8054a.
fundito, -as: v. funda.
Dans les foraes procedentes le latin a gOnOralisO le -d- de fundo",
«ais certaines formes ne prOsentent pas cet Olargisseaent. Ainsi:
i° e xfut t: glosO effusi par P.F.71,13 (sans doute lire ecfutl; la quan-
titO de la voyelle intOrieure n'est pas attestOe directement). Le
coaposO suppose ua si«ple *futus, auqnel se rattache peut-etre futare,
```


## [2026-09-06T02:25:51.449Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T02:25:51.490Z] TOOL RESULT

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


## [2026-09-06T02:36:26.757Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵʰew-\"\nW_PII = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/ȷ́ʰáwtram\"\nE_ALCH = \"https://www.etymonline.com/word/alchemy\"\nE_GEY = \"https://www.etymonline.com/word/geyser\"\nE_ING = \"https://www.etymonline.com/word/ingot\"\nE_FUSE = \"https://www.etymonline.com/word/fuse\"\nE_REF = \"https://www.etymonline.com/word/refuse\"\nW_KIM = \"https://en.wiktionary.org/wiki/كيمياء\"\nV_REF = \"https://vajehyab.com/moein/رفوزه\"\nA_FIY = \"https://abadis.ir/fatofa/فیوز/\"\nA_SHI = \"https://abadis.ir/fatofa/شیمی/\"\nA_ZUR = \"https://abadis.ir/fatofa/زور/\"\n\nPOK_Q = (\"POK_02.txt leaf 105 (printed pp.447-448): “gheu- ,gießen'; gheu-mn ,Opferguß'. … \"\n         \"av. zaotar, zaoθr- m. ,Priester, Opferpriester', mpers. zōt, av. zaoθra n., zaoθrā f. \"\n         \",flüssige Opferspende, Opfertrank, Opferguß', npers. zōr ,Weihwasser', av. āzūtay- f. \"\n         \",Fett, Schmalz, Üppigkeit' … Wurzelerweiterungen: gheud-: lat. fundō, -ere, fūdī, fūsum … \"\n         \"got. giutan, ags. geotan”; POK_full.txt ‘Root/lemma: gheu- / Meaning: to pour / Page(s): 447-448’.\")\nWLD_Q = (\"WLD_Bd1 (djvu l.35459 = WP. I 563): “gheu- ,,gießen“. Ai. juhoti … av. zaotar, zaoθr- m. \"\n         \"„Priester, Opferpriester“, mp. zot, av. zaoθra n. … np. zōr „Weihwasser“ (Horn, Np. Etymol. 675), \"\n         \"av. āzūtay- f. „Fett, Schmalz“.”\")\nAHD_Q = (\"AHD_watkins1985.txt l.524: “gheu-. To pour, pour a libation. I. Extended form *gheud-. … \"\n         \"2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, \"\n         \"FOUND2, FUNNEL, FUSE2, FUSILE, FUSION; … CONFUSE, … REFUND1, (REFUSE1), (REFUSE2) … \"\n         \"II. Extended form *gheus-. 1. Germanic zero-grade *gus- … *gustiz in Old Norse gustr … GUST1 … \"\n         \"2. Germanic suffixed o-grade *gausjan in Old Norse geysa … GEYSER. … IV. Basic form *gheu- in \"\n         \"Greek khein, to pour … [Pok. gheu- 447.]”\")\n\ndef nc(ref, note):\n    return {\"ref\": ref, \"status\": \"not_checked\", \"note\": note}\n\nentry0 = {\n \"entry\": 0,\n \"root\": \"Gheu 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ǵʰew- ‘to pour, pour a libation’ (Pokorny ĵheu-, pp. 447–448; extensions *ǵʰew-d- and *ǵʰew-s-)\",\n \"note\": (\"Root, language label and gloss are all correct: Pokorny 447 heads the entry ‘ĵheu- ,gießen’’ and it runs on to p.448 \"\n          \"with the extension gheud- (Lat. fundō, Goth. giutan). Nourai’s Latin-letter spelling ‘Gheu’ hides the palatal *ǵʰ-, \"\n          \"which is what gives satem z- in Avestan zaotar-/zaoθra- beside centum Gk. χέω and Lat. fundere. Two structural \"\n          \"problems in the chart, both discussed at the nodes: (a) the Pahlavi link zōt ‘holy water’ (#2) conflates the priest-word \"\n          \"zōt (< Av. zaotar-) with the libation-word zōhr (< Av. zaoθra-), which is the real ancestor of NP زور; \"\n          \"(b) ‘zav 2: a kind of alcoholic beverage’ (#4) is not attested in Avestan and the SOD:184 citation does not contain it. \"\n          \"The Greek→Arabic branch (#13–#19) is the disputed one, and Nourai’s own NOTE records the dispute fairly; modern \"\n          \"reference works (OED via Etymonline, Wiktionary) side WITH Nourai’s χυμεία derivation and against Klein’s Egyptian ‘black land’. \"\n          \"One printed box is not in the JSON: an entirely blank rectangle to the right of node #4 (no language header, no words) — \"\n          \"it carries no information, so nothing is lost, but the owner may want to know.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *ǵʰew- «ریختن، نثار ریختن» در پوکورنی صفحهٔ ۴۴۷–۴۴۸ آمده و ادعای نورایی دربارهٔ خود ریشه درست است. \"\n             \"این ریشه کامی نرم (پالاتال) دارد؛ از همین رو در زبان‌های ستم (اوستایی) به z و در زبان‌های کنتوم (یونانی، لاتین) به kh/h بدل شده است. \"\n             \"دو لغزش در نمودار هست: یکی آنکه واسطهٔ فارسی میانهٔ «زور» نه zōt (که نام موبد است) بلکه zōhr است؛ دیگر آنکه «zav 2» به معنای نوعی نوشیدنی الکلی در اوستایی گواهی ندارد. \"\n             \"دربارهٔ شاخهٔ یونانی–عربی (کیمیا/شیمی) پژوهش امروزی بیشتر به سود نورایی است و نه کلاین.\"),\n \"sources\": [W_PIE, W_PII, E_ALCH],\n \"ref_check\": [\n   {\"ref\": \"POK:447\", \"status\": \"supports\", \"note\": POK_Q}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 563 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt l.35459)\", \"stance\": \"supports\", \"note\": WLD_Q},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gheu- (AHD_watkins1985.txt l.524-526)\", \"stance\": \"supports\", \"note\": AHD_Q},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.7642 s.v. chyle\", \"stance\": \"supports\", \"note\": \"“Gk. χυλός ‘juice’, from the stem of χέω ‘to pour’ … fr. base χυ-, corresponding to I.-E. base *ghu-, *gheu-, ‘to pour’, whence OI. ju-háti … hótar, ‘sacrificer, priest’ … L. fūtis, fūtilis.”\"},\n   {\"src\": \"IEC\", \"where\": \"IEC.txt l.6159 s.v. ǵhuuo\", \"stance\": \"supports\", \"note\": \"Mann: “ǵhuuo (1) ‘pour, shed, cast, scatter’. Form of gheu-, q.v. Gk. cf. khúto ‘was poured’ …” (l.6135 ‘ǵhu- radical theme of types gheu-, ǵhou-’).\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 329] s.v. ZAV, ZAOTHRA\", \"stance\": \"supports\", \"note\": \"Aryanpur heads the family ‘ZAV, ZAOTHRA’ and lists Avestan ZAOTHRA/ZAOTHR-, Pahlavi ZOHR, Skt. hotar/hotra, Arm. joyl, Gk. kheo, Lat. fundo/futis, Goth. giutan, OE geotan, Germ. gießen, Dutch gieten — i.e. exactly the set Nourai draws.\"}\n ],\n \"nodes\": []\n}\n\nN = entry0[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"zaothra, zaothar, zaothr\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Two distinct Avestan formations of the root are lumped in one box. (a) zaoθra- n. / zaoθrā- f. \"\n   \"= *ǵʰew-tro-m (root + instrument suffix *-tro-), Proto-Indo-Iranian *Ƿʰáwtram, Skt. hotrá-; its meaning in the \"\n   \"Avesta is ‘liquid offering, libation, sacrificial drink’, and it is this word that later means ‘consecrated water’ \"\n   \"in Zoroastrian ritual (āpō zaoθrā ‘libation to the waters’, whence MP āb-zōhr). (b) zaotar- m. = *ǵʰew-tor- \"\n   \"(agent noun, Skt. hótar-) means ‘the pouring priest, chief officiant’, NOT ‘holy water’; ‘zaothr’ is simply the \"\n   \"weak stem zaoθr- of zaotar-. So the single gloss ‘holy water’ is right for zaoθra- and wrong for zaotar-/zaoθr-. \"\n   \"Both derive from the root exactly as drawn: Proto-Iranian *ǵʰaw- > Av. zav- with regular satem depalatalisation \"\n   \"ǵʰ > z.\"),\n \"derivation_fa\": (\"در این جعبه دو ساخت جدای اوستایی یکجا آمده است: zaoθra- (از ریشه + پسوند ابزاری *-tra-) به معنای «نثار آبگین، آب تقدیس‌شده»، \"\n   \"و zaotar- (اسم فاعل با پسوند *-tar-، هم‌ریشه با سنسکریت hótar-) که نام موبد اصلی مراسم است و نه «آب مقدس»؛ zaoθr- نیز همان ستاک کوتاه zaotar- است. \"\n   \"تبدیل *ǵʰ هندواروپایی به z ایرانی قاعده‌مند است (زبان‌های ستم). پس پیوند با ریشه درست است اما معنای یکسان برای هر سه واژه پذیرفتنی نیست.\"),\n \"sources\": [W_PII, W_PIE],\n \"ref_check\": [{\"ref\": \"POK:447\", \"status\": \"supports\", \"note\": POK_Q + \" — note that Pokorny himself glosses zaotar- as ‘Priester’ and only zaoθra- as ‘Opfertrank/Opferguß’.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiran. Wb. col. 1653f. (BRT.txt l.27523, 27566)\", \"stance\": \"partial\", \"note\": \"Bartholomae: “• j., g. zaotar-; zaoθr- m. ‘Priester, Oberpriester’ … im jAw. Name des vornehmlich mit dem Vortrag der Gāθās betrauten Oberpriesters”; separately ‘zaoθrō.bara- Adj. ‘der Z., Trankopfer darbringt’’ and ‘zaoθrō.barana- ‘die Z. enthaltend’’ — i.e. zaoθra = the libation, zaotar = the priest.\"},\n   {\"src\": \"HUB\", \"where\": \"Pers. Studien (HUB.txt l.7330)\", \"stance\": \"supports\", \"note\": \"“zd. zaoθra- ‘Opferspende, Opfertrank, Weihwasser’” — the ‘holy water’ gloss belongs to zaoθra-.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 563\", \"stance\": \"supports\", \"note\": WLD_Q}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"zôt\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"MP zōt [zwt'] is a real Pahlavi word and does continue Av. zaotar-, but it means ‘the first officiating \"\n   \"priest’ (MacKenzie: “zōt [zwt' = Av. zaotar-] first officiating priest. ~ih: office of zōt”) — not ‘holy water’. \"\n   \"The Pahlavi word for the libation/consecrated water is zōhr [zwhl] < Av. zaoθra-, listed by MacKenzie two lines \"\n   \"earlier as ‘zōhr [zwhl | M zwhr] libation, offering’ and by Horn (no. 675) as ‘phlv. zōhr, zūr’. Nourai has taken \"\n   \"Pokorny’s ‘mpers. zōt’, which stands in Pokorny immediately after ‘av. zaotar … m. Priester’ and belongs to that \"\n   \"word, and re-glossed it as ‘holy water’ so as to bridge to NP زور. The correct bridge is zōhr. Av. -θr- > MP -hr \"\n   \"(zaoθra > zōhr) and Av. au > MP ō are both regular; zōt shows the equally regular loss of the agent-suffix -tar > -t.\"),\n \"derivation_fa\": (\"در فارسی میانه zōt واژهای واقعی است و ادامهٔ zaotar- اوستایی است، اما معنای آن «موبد اصلی در مراسم یزشن» است و نه «آب مقدس»؛ \"\n   \"مکنزی در فرهنگ کوچک پهلوی می‌نویسد: zōt [zwt'] = Av. zaotar-، موبد نخست. واژهٔ پهلوی «آب مقدس/نثار» zōhr است (از zaoθra-)، همان که هرن در شمارهٔ ۶۷۵ می‌آورد («phlv. zōhr, zūr»). \"\n   \"پس پژوهش امروزی این حلقه را رد می‌کند و به جای آن zōhr را می‌گذارد؛ تبدیل -θr- اوستایی به -hr- پهلوی قاعده‌مند است.\"),\n \"sources\": [W_PII],\n \"ref_check\": [nc(\"(no refs printed)\", \"Nourai gives no citation for this box; the form is evidently taken over from Pokorny 447 ‘mpers. zōt’, where it glosses zaotar- ‘priest’, not the libation.\")],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dict. s.v. (PHD.txt l.680; PHD_mackenzie.txt l.5851)\", \"stance\": \"contradicts\", \"note\": \"“zōhr [zwhl | M zwhr] libation, offering. … zōt [zwt' = Av. zaotar-] first officiating priest. ~ih: office of zōt.” — zōt is the priest; zōhr is the holy water.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 675 (HRN.txt l.5955-5956)\", \"stance\": \"contradicts\", \"note\": \"“675. zōr ‘Weihwasser’ (pärsisch). aw. zaoθrā ‘Weihwasser’; phlv. zōhr, zūr, arm. …” — Horn’s Pahlavi intermediate is zōhr/zūr, not zōt.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt, greps for zwt/zōt)\", \"stance\": \"silent\", \"note\": \"Nyberg’s glossary has zūd/zat [zwt'] ‘swift, quick’ (l.4573) but no zōt ‘holy water’; the ritual term is not in the texts he glosses.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 563\", \"stance\": \"contradicts\", \"note\": \"Walde-Pokorny put ‘mp. zot’ between ‘av. zaotar, zaoθr- m. „Priester, Opferpriester“’ and ‘av. zaoθra n. …’, and give the ‘Weihwasser’ word separately as ‘np. zōr … (Horn, Np. Etymol. 675)’ — confirming that zōt is the priest-word.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"zawr «زور۲»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"NP زور zōr ‘consecrated water used in Zoroastrian ritual’ is genuine — Mo‘in gives it as a separate \"\n   \"headword ‘آبی است که به دست یکی از موبدان پاک و مقدس شده’, and Mo‘in’s footnote in Borhan-e Qate‘ (at the entry زوراشنا) \"\n   \"reports Purdavud taking the first element as زور = Avestan zaoθra ‘آب مقدس که در جشنهای زردشتیان بکار رود’. \"\n   \"The chain, however, is Av. zaoθra- > MP zōhr (zwhl) > NP zōr, with regular loss of intervocalic/pre-consonantal h \"\n   \"and Av. au > ō: so Nourai’s ultimate source is right but his intermediate (zōt) is not. Horn 675 and Hübschmann \"\n   \"both mark zōr a ‘Parsenwort’, i.e. a term kept alive inside the Zoroastrian community rather than a general New \"\n   \"Persian word; it is a homonym of, and unrelated to, the common زور ‘strength’ (< Av. zāvar-).\"),\n \"derivation_fa\": (\"«زور» ۲ در فارسی به معنای آب مقدّس زرتشتیان واژهای است واقعی؛ معین آن را مدخلی جداگانه آورده و در حاشیهٔ برهان قاطع (ذیل «زوراشنا») \"\n   \"از قول پورداود آن را همان zaoθraی اوستایی دانسته است. ولی زنجیرهٔ درست چنین است: اوستایی zaoθra- < فارسی میانه zōhr < فارسی نو زور، با افتادن قاعده‌مند h. \"\n   \"پس ادعای نورایی دربارهٔ ریشه درست است ولی حلقهٔ میانی او نادرست است. این «زور» هم‌آوای «زور» ۱ (نیرو، از zāvar- اوستایی) است و با آن هم‌ریشه نیست.\"),\n \"sources\": [A_ZUR, W_PII],\n \"ref_check\": [\n   {\"ref\": \"MON:1761\", \"status\": \"partial\", \"note\": \"The paginated 6-vol Mo‘in is not online (refs_online.json MON notes); the entry itself is verifiable via abadis.ir/vajehyab, which gives Mo‘in’s زور ‘آبی است که به دست یکی از موبدان پاک و مقدس شده’ as a separate sense — so the word and gloss are Mo‘in’s, but p.1761 could not be checked.\"},\n   {\"ref\": \"BQT:1043\", \"status\": \"supports\", \"note\": \"Mo‘in’s footnote 4 in Borhan-e Qate‘, BQT_v2_pages.txt leaf 505 (printed ≈ p.1045, i.e. ±2 pages from Nourai’s citation — the leaf→page offset is +540 ±2): ‘جزو اول کلمه را آقای پورداود «زور» بفتح اول (اوستا zaoθra) دانند بمعنی آب مقدس که در جشنهای زردشتیان بکار رود’ (at the entry زوراشنا). Footnote 7 on the same page keeps زور ‘قوت’ apart, from Av. zāvar-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 675, p. ~139 (HRN.txt l.5955)\", \"stance\": \"supports\", \"note\": \"“675. zōr ‘Weihwasser’ (pärsisch). aw. zaoθrā ‘Weihwasser’; phlv. zōhr, zūr”.\"},\n   {\"src\": \"HUB\", \"where\": \"Pers. Studien (HUB.txt l.7328, 7890)\", \"stance\": \"supports\", \"note\": \"“‘Weihwasser (Parsenwort!) == paz. zor Min. Gl. 225, phl. …’” and “zd. zavare; zōr ‘Weihwasser’ (gʰ) H. 675, Parsenwort” — Hübschmann keeps zōr ‘Weihwasser’ apart from zāvar ‘strength’, as Nourai does.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 329], note 1 under ZAV/ZAOTHRA\", \"stance\": \"supports\", \"note\": \"“واژهٔ ‘زور’ به چم ‘آب مقدس که در مراسم زرتشتی پاشیده می‌شود’ نیز از همین واج‌ریشه است (اوستایی: ZAOTHRA؛ پهلوی: ZOHR)” — same root, but Pahlavi ZOHR.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. zōhr\", \"stance\": \"partial\", \"note\": \"“zōhr [zwhl | M zwhr] libation, offering” — supplies the missing Pahlavi step.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Avestan\", \"words\": \"âzŭtay; zav 2\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Word 1 is right: Av. āzūtay- f. ‘fat, lard, abundance’ = ā- + *ǵʰu-ti- (zero grade of the root + abstract \"\n   \"*-ti-), literally ‘that which is poured on/in’; Pokorny lists it in the same paragraph (‘av. āzūtay- f. „Fett, \"\n   \"Schmalz, Üppigkeit, strotzende Fülle“’) and Bartholomae has it beside xšvid- ‘milk’ (‘āsūtay- … flüssige Nahrung’). \"\n   \"Word 2 is not: there is no Avestan zav- meaning ‘a kind of alcoholic beverage’. Bartholomae’s Avestan zav- entries \"\n   \"are ‘to call, invoke’ (Nourai’s own ‘zav 1’ on book p.107 / pdf 137) and the -bāzav- ‘arm’ compounds; the pouring \"\n   \"root appears only in derivatives (zaotar-, zaoθra-). The citation SOD:184 does not help: Gharib’s p.184 (SOD_pages.txt \"\n   \"leaf 249) holds entries 4590–4613 (znuk ‘knee’, zōt ‘strike’, žukyamenc ‘safe’), and Gharib’s entry no. 184 is the \"\n   \"proper name Ānanda. Gharib does have a Sogdian word for a drink — no. 11503 ‘zwt’k B,S zūte? … beer, liquor’, on \"\n   \"p.469 — which is probably what Nourai half-remembered, but that is Sogdian, not Avestan, and its own etymology \"\n   \"(from *jauta-?) is uncertain.\"),\n \"derivation_fa\": (\"واژهٔ نخست درست است: اوستایی āzūtay- «چربی، روغن، فراوانی» از پیشوند ā- و درجهٔ صفر ریشه با پسوند *-ti- ساخته شده؛ پوکورنی و بارتولومه هر دو آن را آورده‌اند. \"\n   \"اما «zav 2» به معنای نوعی نوشیدنی الکلی در اوستا گواهی ندارد؛ zav- در فرهنگ بارتولومه «خواندن، فراخواندن» است (همان zav 1 خود نورایی). \"\n   \"ارجاع SOD:184 هم درست نیست: در صفحهٔ ۱۸۴ فرهنگ سغدی قریب چنین واژه‌ای نیست؛ تنها مدخل شمارهٔ ۱۱۵۰۳ (ص ۴۶۹) سغدی zwt'k «آبجو، می» است که سغدی است نه اوستایی. \"\n   \"پس این بخش از ادعای نورایی پذیرفتنی نیست.\"),\n \"sources\": [W_PIE],\n \"ref_check\": [\n   {\"ref\": \"POK:447\", \"status\": \"partial\", \"note\": \"Pokorny p.447 has āzūtay- (‘av. āzūtay- f. „Fett, Schmalz, Üppigkeit, strotzende Fülle“’) but nothing about a drink called zav.\"},\n   {\"ref\": \"SOD:184\", \"status\": \"not_found\", \"note\": \"Gharib p.184 = SOD_pages.txt leaf 249 (offset printed ≈ leaf − 65): entries 4590–4613, ‘jnwwq znuk … knee’, ‘jt- zōt … (to)strike’, ‘jwky’mync zukyamenc … safe, sound’ — no beverage. Read as an entry number instead, no. 184 = ‘’nt’ Ānanda’ (a name). The only ‘beer, liquor’ word in Gharib is no. 11503 ‘zwt’k … zūte?’, printed p.469.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiran. Wb. (BRT.txt l.10985 s.v. xšvid-; l.8079)\", \"stance\": \"partial\", \"note\": \"“• j., g. xšvid- m. ‘Milch’; im Gegensatz zu āzūtay- … überhaupt ‘flüssige Nahrung’ … Du. in Verbindung mit āzūtay- Du.: … āzūiti yazamaide” — āzūtay- confirmed; Bartholomae’s Avestan zav- entries are ‘to call/invoke’ and ‘-bāzav- arm’, never a drink.\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib, entries 4590-4613 (p.184) and 11503 (p.469)\", \"stance\": \"contradicts\", \"note\": \"The cited page carries no such word; the one ‘beer, liquor’ entry is Sogdian ‘zwt’k … zūte? (zwtk, z’wy’?) → jwty’ — beer, liquor. TSP 2.388…’ at p.469.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 563\", \"stance\": \"partial\", \"note\": \"Walde-Pokorny list only ‘av. āzūtay- f. „Fett, Schmalz, Üppigkeit, strotzende Fülle“’ for this branch.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Germanic\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Empty pass-through box for Proto-Germanic. The relevant forms are *geutaną ‘to pour’ < *ǵʰewd- \"\n   \"(Goth. giutan, ON gjóta, OE gēotan, OHG gioʒan, Germ. gießen) and the *ǵʰews- extension in *gus- (ON gjósa, \"\n   \"gustr). Grimm’s law turns PIE *ǵʰ into PGmc *g and *d into *t, giving g—t where Latin has f—d (fundere).\"),\n \"derivation_fa\": (\"جعبهٔ تهی واسطه برای ژرمنی آغازین. صورت‌های مربوط *geutaną «ریختن» (از *ǵʰewd-) و ستاک *gus- (از *ǵʰews-) هستند. \"\n   \"بر پایهٔ قانون گریم، *ǵʰ هندواروپایی در ژرمنی به g و *d به t بدل می‌شود؛ از این‌رو جایی که لاتین fund- دارد، ژرمنی giut- دارد. ادعای نورایی درست است.\"),\n \"sources\": [W_PIE, E_ING],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_Q}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.15274 s.v. found, ‘to cast’\", \"stance\": \"supports\", \"note\": \"“fr. L. fundere … fr. I.-E. base *ghu-d-, ‘to pour’, whence also Goth. giutan, OS. giotan, OFris. giata, OE. geotan, OHG. giozan … ON. gjota, Swed. gjuta, Dan. gyde, ‘to pour’.”\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 563 f.\", \"stance\": \"supports\", \"note\": \"The Germanic *geut-/*gut- family stands under gheu- in Walde-Pokorny.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"geyser, gust, ingot, nugget\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All four are Germanic offshoots of the root. GEYSER (1780) is the proper name of the hot spring Geysir \"\n   \"in Haukadalur, Iceland, lit. ‘the gusher’, from Icel. geysa ‘to gush’ < PGmc *gausjan, o-grade of *ǵʰews-; it \"\n   \"spread as a common noun through 18th-c. travel writing. GUST (1580s) is Old Norse gustr ‘blast of wind’ < *gus-ti-, \"\n   \"zero grade of the same extension, borrowed in the Danelaw/Norse-contact period. INGOT (late 14c.) is native English \"\n   \"in- + goten, past participle of OE gēotan ‘to pour’, originally ‘the mould into which metal is poured’, then ‘the \"\n   \"cast mass’ (15c.). NUGGET is a 19th-c. re-shaping of ‘an ingot’ by wrong division (a niggot / a nugget), the form \"\n   \"niggot being attested in North’s Plutarch.\"),\n \"derivation_fa\": (\"هر چهار واژه از شاخهٔ ژرمنی همین ریشه‌اند. geyser در ۱۷۸۰ م. از نام چشمهٔ جوشان Geysir در ایسلند گرفته شده که معنای تحت‌اللفظی‌اش «فوران‌کننده» است. \"\n   \"gust وام‌واژه‌ای است از نوردی کهن gustr «تندباد». ingot ساختهٔ خود انگلیسی است: in- + goten (اسم مفعول gēotan «ریختن») یعنی «قالبی که فلز در آن ریخته می‌شود»، و سپس «شمش». \"\n   \"nugget نیز دگرگونی «an ingot» است از راه بخش‌بندی نادرست مرز واژه. ادعای نورایی درست است.\"),\n \"sources\": [E_GEY, E_ING, W_PIE],\n \"ref_check\": [{\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.16094 “geyser, n. — Icel. Geysir … lit. ‘the gusher’, fr. geysa, ‘to gush’, which is rel. to ON. gjosa … freq. of gjota, ‘to pour’. See found, ‘to cast’”; l.16893 “gust … ON. gustr … from gus-, weak grade of gjosa”; l.25746 “nugget … For niggot (so spelled in North’s Plutarch), fr. a niggot, misdivision and corruption of an ingot”; l.15274 s.v. found refers ingot to this base.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gheu- II and index\", \"stance\": \"supports\", \"note\": \"“II. Extended form *gheus-. 1. … *gustiz in Old Norse gustr … GUST1 … 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER”; index l.1560 ‘GEYSER gheu-’, l.1573 ‘GUT gheu-’, l.1572 ‘GUSH gheu- / GUST1 gheu-’.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Nugget (SKT.txt l.12501)\", \"stance\": \"supports\", \"note\": \"“Nugget, a lump of metal. (E.) Formerly niggot; see Trench, Eng. Past and Present. Prob. a corruption of an ingot, put for a ingot; see Ingot.”\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls (FSD_vol2/3, s.vv.)\", \"stance\": \"silent\", \"note\": \"Not consulted for these four — Klein, Skeat, Watkins and Etymonline already agree on the whole chain.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Latin\", \"words\": \"fundere\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Lat. fundō, fundere, fūdī, fūsum ‘to pour, melt’ continues the *ǵʰew-d- extension with a nasal infix in \"\n   \"the present only: *ǵʰu-n-d- > fundō, beside infix-less perfect fūdī and participle fūsum (< *ǵʰud-to-). \"\n   \"PIE *ǵʰ gives Latin f- initially (as in forēs : Gk. θύρα), whence the f—d of fundere against Greek χέω and \"\n   \"Germanic giutan. Ernout-Meillet state the correspondence explicitly.\"),\n \"derivation_fa\": (\"لاتین fundō/fundere «ریختن، گداختن» از گسترش *ǵʰew-d- است؛ در زمان حال میانوند تو دماغی (n) افزوده می‌شود (fundō) ولی در ماضی و اسم مفعول نمی‌آید (fūdī، fūsum). \"\n   \"تبدیل *ǵʰ آغازین به f در لاتین قاعده‌مند است. ادعای نورایی درست است.\"),\n \"sources\": [W_PIE],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins: “2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE2, FUSILE, FUSION…”\"}],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. fundo (LAT.txt l.24856)\", \"stance\": \"supports\", \"note\": \"“fundo, -is, fūdī, fūsum, fundere: verser, répandre. Correspond à gr. χέω, se dit des liquides, et spécialement d’un métal en fusion, de là le sens technique de ‘fondre’, conservé dans les l. romanes. … Dérivés en fund- et en fus-: fundibulum: entonnoir … refundo ‘reverser, refouler, rejeter’.”\"},\n   {\"src\": \"POK\", \"where\": \"p.448 (POK_02.txt leaf 105)\", \"stance\": \"supports\", \"note\": \"“Wurzelerweiterungen: gheud-: lat. fundō, -ere, fūdī, fūsum ‘gieße, lasse fließen, schütte aus’ (über fūsus ‘Spindel’ s. WH. I 474); got. giutan …”\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.15274 s.v. found\", \"stance\": \"supports\", \"note\": \"“F. fondre, fr. L. fundere, ‘to pour, melt’, fr. I.-E. base *ghu-d-, ‘to pour’ … Base *ghu-d- is a -d- enlargement of base *ghu-, ‘to pour’.”\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"funnel, fuse\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"FUNNEL is secure: Middle English fonel (15c.), from Old Provençal fonilh / enfonilh, from Late Latin \"\n   \"fund(i)bulum, a shortening of Latin infundibulum ‘funnel’ (in- + fundere); the word came into English through the \"\n   \"Gascon wine trade, which is why the Provençal form and not a French one lies behind it. FUSE is only half secure. \"\n   \"The verb fuse ‘to melt’ (1680s) is a back-formation from fusion < Lat. fūsiō < fūsus, pp. of fundere — that link \"\n   \"is direct. The noun fuse ‘combustible tube’ (1640s), which is the one behind the electrical sense of 1884 and hence \"\n   \"behind Persian فیوز, comes from Italian fuso ‘spindle’ < Lat. fūsus ‘spindle’; Watkins puts fūsus with this root \"\n   \"(FUSE2 under gheu-), but Walde-Hofmann and Pokorny expressly hold fūsus ‘Spindel’ apart (‘über fūsus „Spindel“ s. \"\n   \"WH. I 474’). So the arrow is right for one sense of fuse and doubtful for the other; also, funnel and fuse did not \"\n   \"come from Latin directly as drawn but via Provençal/Italian.\"),\n \"derivation_fa\": (\"funnel از پروانسالی کهن fonilh و آن از لاتین متأخر fundibulum (کوتاه‌شدهٔ infundibulum «قیف») است؛ راه وام‌گیری بازرگانی شراب گاسکونی بوده است. \"\n   \"اما fuse دو واژه است: فعل fuse «گداختن» از fusion و آن از fūsus (اسم مفعول fundere)، که پیوندش روشن است؛ و اسم fuse «فتیله» از ایتالیایی fuso «دوک» (لاتین fūsus) که پوکورنی و والده–هوفمان آن را از این ریشه جدا می‌دانند. پس این حلقه با احتیاط پذیرفتنی است.\"),\n \"sources\": [E_FUSE, W_PIE],\n \"ref_check\": [nc(\"(no refs printed)\", \"No citation in this box; checked against Watkins (FUNNEL, FUSE2 both under gheu-), Klein (cp.-list under ‘found’ includes funnel, fusible, fusion), Ernout-Meillet (fundibulum/infundibulum) and Etymonline.\")],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gheu- I.2; index l.1526, 1547\", \"stance\": \"supports\", \"note\": \"‘FUNNEL gheu-’, ‘FUSE2 gheu- / FUSILE gheu- / FUSION gheu-’ — Watkins accepts both.\"},\n   {\"src\": \"POK\", \"where\": \"p.448 (POK_02.txt leaf 105)\", \"stance\": \"partial\", \"note\": \"“lat. fundō … (über fūsus ‘Spindel’ s. WH. I 474)” — Pokorny refers fūsus ‘spindle’ away to Walde-Hofmann, i.e. does not put it under this root.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. fundo\", \"stance\": \"supports\", \"note\": \"“fundibulum: entonnoir … sans doute refait sur le composé plus ancien infundibulum” — the etymon of funnel.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"fiyŭz «فیوز»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"فیوز is a 20th-century technical loan taken with the electrical apparatus itself, and Mo‘in tags it \"\n   \"[انگ.] = English, exactly as Nourai draws it (Dehkhoda likewise [انگلیسی]). English fuse in the sense ‘device that \"\n   \"breaks a circuit’ dates from 1884, so the Persian word cannot be older than the electrification of Iran (1900s–30s). \"\n   \"Phonetically English /fjuːz/ is rendered فیوز fiyuz, with یو for the English diphthong /juː/ and final z spelt ز; the \"\n   \"colloquial idiom فیوز پراندن (Mo‘in) shows how thoroughly it was naturalised.\"),\n \"derivation_fa\": (\"«فیوز» وام‌واژه‌ای فنی از سدهٔ بیستم است که همراه خود دستگاه به فارسی آمده؛ معین آن را با نشانهٔ [انگ.] و دهخدا با [انگلیسی] آورده‌اند، یعنی دقیقاً همان مسیری که نورایی کشیده است. \"\n   \"معنای برقی fuse در انگلیسی از ۱۸۸۴ م. است، پس وام‌گیری فارسی نمی‌تواند پیش از برق‌رسانی ایران باشد. ادعای نورایی درست است.\"),\n \"sources\": [A_FIY, E_FUSE],\n \"ref_check\": [{\"ref\": \"MON:2599\", \"status\": \"partial\", \"note\": \"The 6-vol Mo‘in is unpaginated online, so p.2599 itself could not be opened; the entry is verifiable at abadis.ir (فرهنگ معین): ‘[انگ.] اسبابی که جهت جلوگیری از عبور جریان شدید الکتریسته در یک مدار به کار می‌رود’ — the [انگ.] tag is Mo‘in’s and matches the chart.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. فیوز\", \"stance\": \"supports\", \"note\": \"origin tag [انگ.] (English).\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (grep فیوز)\", \"stance\": \"silent\", \"note\": \"Aryanpur’s Indo-European root dictionary does not treat modern technical loans; no entry.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"French\", \"words\": \"refuse\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The French word is refuser (12c.) / the noun refus, not ‘refuse’, and its gloss ‘poured back’ belongs to \"\n   \"the Latin etymon, not to the French word, which already means ‘reject, decline’. Etymologically the box is right: \"\n   \"OFr. refuser < Vulgar Latin *refūsāre, a frequentative built on refūsus, past participle of Latin refundere \"\n   \"‘to pour back, give back, restore’ (re- + fundere) — with semantic and formal contamination from refūtāre ‘to rebut’, \"\n   \"which is what carried the sense from ‘pour back’ to ‘turn down’. So the arrow fundere → French holds; only the \"\n   \"citation form and gloss are Nourai’s shorthand.\"),\n \"derivation_fa\": (\"صورت فرانسوی درست refuser (فعل) یا refus (اسم) است و نه «refuse»؛ معنای «بازریخته‌شده» هم از آن اصل لاتین است نه از آن واژهٔ فرانسوی. \"\n   \"اما ریشه‌شناسی درست است: refuser از لاتین عامیانهٔ *refūsāre، ساخته بر اسم مفعول refūsus از refundere «باز ریختن، پس دادن»، با آمیزش معنایی از refūtāre «رد کردن». با احتیاط پذیرفتنی است.\"),\n \"sources\": [E_REF],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins index l.1392 ‘CONFUSE gheu-’ and the gheu- entry list ‘REFUND1, (REFUSE1), (REFUSE2)’ under *ghu-n-d- > Latin fundere.\"}],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. fundo, composés\", \"stance\": \"supports\", \"note\": \"“refundo ‘reverser, refouler, rejeter, rendre liquide’ M.L.7163” — the Romance continuation of refundere is registered (Meyer-Lübke 7163).\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.15274 s.v. found (cp.-list)\", \"stance\": \"supports\", \"note\": \"Klein’s list of cognates under the *ghu-d- base includes ‘refound, refund, refuse, ruse’.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"Persian\", \"words\": \"refŭzeh «رفوزه»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"رفوزه ‘failed (in an examination)’ is French refusé ‘rejected’, borrowed in the late Qajar/Pahlavi period with \"\n   \"the French-modelled school and Dar al-Fonun examination system; Mo‘in marks it [فر.] = French and defines it \"\n   \"‘رد شده در امتحان’. The French past participle in -é is regularly rendered in Persian by -ه (as in پروانیزه permis, \"\n   \"مانور، دکوره), and French /y/ appears as و u; the emphatic sense ‘failed’ (rather than merely ‘refused’) is a \"\n   \"Persian narrowing to the examination context.\"),\n \"derivation_fa\": (\"«رفوزه» از فرانسوی refusé «ردشده» است؛ معین آن را با نشانهٔ [فر.] و معنای «رد شده در امتحان» آورده است. وام‌گیری از روزگار دارالفنون و نظام آموزشی فرانسوی‌مانند است. \"\n   \"پسوند -é فرانسوی در فارسی به «ه» بدل می‌شود و /y/ فرانسوی به و. ادعای نورایی درست است.\"),\n \"sources\": [V_REF, E_REF],\n \"ref_check\": [{\"ref\": \"MON:1665\", \"status\": \"partial\", \"note\": \"Page not checkable (6-vol Mo‘in not online); the entry is on vajehyab’s Mo‘in: ‘(رِ زِ) [فر.] (اِمف.) رد شده در امتحان’ — the [فر.] tag is exactly Nourai’s French source.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/رفوزه\", \"stance\": \"supports\", \"note\": \"‘[فر.] رد شده در امتحان’.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (grep رفوزه)\", \"stance\": \"silent\", \"note\": \"No entry — Aryanpur covers inherited Indo-European vocabulary, not modern European loans.\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"English\", \"words\": \"refuse, confuse, refund, font\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"All four are listed by Watkins under gheu-, so the root is right; the routes differ. REFUSE (v., early 14c.) \"\n   \"does come through Old French refuser, as the chart draws it. CONFUSE and REFUND, however, come straight from the Latin \"\n   \"verbs confundere ‘pour together, mix up’ and refundere ‘pour back, pay back’ (via their past participles confusus, \"\n   \"refusus and Anglo-French), not through French refuser; hanging them under the French box is a simplification. FONT \"\n   \"is a homonym trap: the typographic font (‘a complete set of type’, 1680s) is French fonte ‘a casting’, from fondre < \"\n   \"fundere — correctly here; but the baptismal font is Latin fons, fontem ‘spring’, which Watkins puts under a different \"\n   \"root (‘FONT1 dhen-1 / FONT2 gheu-’). Nourai does not say which font he means.\"),\n \"derivation_fa\": (\"هر چهار واژه در فهرست واتکینز ذیل gheu- آمده‌اند، پس ریشه درست است؛ اما مسیرها یکسان نیست. refuse از راه فرانسوی کهن refuser آمده، \"\n   \"ولی confuse و refund یکسره از لاتین confundere و refundere گرفته شده‌اند نه از فعل فرانسوی. font نیز دو واژهٔ هم‌نگار است: font چاپی (از فرانسوی fonte «ریخته‌گری») از این ریشه است، \"\n   \"اما font تعمید از لاتین fons «چشمه» و از ریشه‌ای دیگر (*dhen-) است. پس با احتیاط پذیرفتنی است.\"),\n \"sources\": [E_REF, W_PIE],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins index: l.1526 ‘FONDANT gheu- / FONDUE gheu- / FONT1 dhen-1 / FONT2 gheu-’; l.1392 ‘CONFUSE gheu-’; the gheu- entry itself lists REFUND1, (REFUSE1), (REFUSE2).\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.15274 s.v. found; l.1878 s.v. affuse\", \"stance\": \"supports\", \"note\": \"“Cp. circumfuse, confound, confuse, diffuse, effuse, funnel, fusel oil, fusible, fusion, futile, infundibulum, infuse, infusion, interfuse, profuse, refound, refund, refuse, ruse, rush, v., transfuse.”\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. fundo (composés)\", \"stance\": \"supports\", \"note\": \"“confundo: verser ensemble et ‘confondre’ (cf. συγχέω) … refundo ‘reverser, refouler, rejeter’ M.L.7163”.\"}\n ]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"Greek\", \"words\": \"xymeia\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The Greek word is χυμεία (khumeia, later spelt χημεία) ‘the art of pouring/alloying, mixing of \"\n   \"liquids’, from χύμα ‘what is poured, a fluid’ + -εία, ultimately from χέω ‘I pour’ < *ǵʰew-; it is the word used \"\n   \"of Greco-Egyptian metallurgical-pharmaceutical art in Alexandria from about the 3rd–4th c. CE (Zosimus). Nourai’s \"\n   \"‘xymeia’ is the Latin-letter rendering with x = χ. The rival account, which Nourai’s own NOTE fairly reports, \"\n   \"takes the word from Egyptian km.t ‘the black land’ = Egypt (Coptic kēme), whence Gk. Χημία; Klein p.45 declares \"\n   \"the ‘pouring’ derivation folk etymology and Lokotsch (no. 1157) follows the Egyptian account. Modern reference \"\n   \"works go the other way: Wiktionary derives Arabic كيمياء straight from χυμεία < χύμα < *ǵʰew-, and Etymonline \"\n   \"quotes the OED concluding that ‘Greek khymeia was likely original, applied to pharmaceutical chemistry involving \"\n   \"plant infusions’. So Nourai’s branch is the currently better-supported one, not the discredited one; ‘plausible’ \"\n   \"only because the two accounts have long contaminated each other and the η/υ spelling shows it.\"),\n \"derivation_fa\": (\"واژهٔ یونانی χυμεία (بعدها χημεία) از χύμα «آنچه ریخته می‌شود، مایع» و در نهایت از فعل χέω «می‌ریزم» است و بر هنر گداختن و آمیختن فلزات در اسکندریهٔ سدهٔ سوم–چهارم میلادی اطلاق می‌شده. \"\n   \"دیدگاه رقیب آن را از مصری km.t «سرزمین سیاه» می‌داند که کلاین و لوکوچ پذیرفته‌اند؛ اما فرهنگ‌های امروزی (او‌ای‌دی و ویکی‌واژه) همان دیدگاه نورایی را ترجیح می‌دهند. پس ادعای او پذیرفتنی است.\"),\n \"sources\": [W_KIM, E_ALCH, W_PIE],\n \"ref_check\": [\n   nc(\"OEW:124\", \"Shipley, The Origins of English Words (1984) is lending-only on archive.org (refs_online.json OEW: ‘Borrow via IA lending (djvu.txt returns 401/403)’); p.124 could not be opened.\"),\n   {\"ref\": \"FSD:66\", \"status\": \"not_found\", \"note\": \"Funk & Wagnalls vol. I, the alchemic/alchemist/alchemy opening (FSD_vol1.txt leaf 107, printed ≈ p.66) is present, but the OCR of the square-bracket etymology after ‘al′che-my’ is destroyed — no ‘chemy/chymia/Gr./Ar.’ string survives on leaves 107-108, so the claim itself could not be read.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.2130 s.v. alchemy (= p.45)\", \"stance\": \"contradicts\", \"note\": \"“fr. Arab. al-kimiya, fr. al-, ‘the’, and MGk. χημεία, prop. ‘the art of the black land (Egypt)’, fr. Gk. Χημία, ‘Blackland, Egypt’, fr. Egypt. khem, khame, ‘black’. The derivation from Gk. χυμεία, ‘pouring’, from the stem of χέειν, ‘to pour’, is folk etymology. See W. Muss-Arnolt, TAPA …” — exactly the objection Nourai’s NOTE records.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1157 (LKT.txt l.2718)\", \"stance\": \"contradicts\", \"note\": \"“Äg. kimi, kopt. kemi ‘schwarz’ war die Bezeichnung des Landes Ägypten … hieraus entstand ar. kimija’ zunächst zur Bezeichnung des ‘Steins der Weisen’ … dann ‘Scheidekunst, Chemie’.”\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gheu- IV\", \"stance\": \"partial\", \"note\": \"Watkins derives CHYLE, CHYME, ECCHYMOSIS, PARENCHYMA from Gk. khein under this root but does not list ALCHEMY/CHEMISTRY there — i.e. the appendix does not endorse the χυμεία route (consistent with Nourai’s own note that AHD:30 prefers the Egyptian word).\"}\n ]\n})\n\nN.append({\n \"id\": 14, \"lang\": \"Arabic\", \"words\": \"al-kimyâ\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Arabic الكيمياء al-kīmiyāʾ (al- ‘the’ + kīmiyāʾ) is the Greek word taken over by the Arabic translation \"\n   \"movement of the 8th–9th c. (Jabir ibn Hayyan, the Bayt al-Hikma); Greek -εία is rendered by the Arabic pattern \"\n   \"fiʿliyāʾ with final hamza. Wiktionary states plainly: ‘Borrowed from Ancient Greek χυμεία (khumeia), from χύμα \"\n   \"+ -ία’, tracing it to PIE *ǵʰew- — Nourai’s route exactly. It is not a native Semitic root: the Arab lexicographers’ \"\n   \"own derivation from kamā ‘to hide’ (reported by Lokotsch) is itself a folk etymology, and Klein/Lokotsch’s Egyptian \"\n   \"km.t is the alternative that Nourai’s NOTE records. Marked plausible because the Greek word’s own origin is what is \"\n   \"contested, not the Greek → Arabic step, which is undisputed.\"),\n \"derivation_fa\": (\"عربی الکیمیاء (الـ + کیمیاء) وام‌واژه‌ای یونانی است که در نهضت ترجمهٔ سدهٔ دوم و سوم هجری (جابر بن حیّان، بیت‌الحکمه) وارد عربی شده؛ پایانهٔ یونانی -εία به وزن عربی «ـیاء» برگردانده شده است. \"\n   \"ریشه‌شناسی لغویان عرب (از کما «پنهان کردن») ریشه‌شناسی عامیانه است. خود مرحلهٔ یونانی ← عربی مورد اختلاف نیست؛ اختلاف بر سر خاستگاه همان واژهٔ یونانی است.\"),\n \"sources\": [W_KIM, E_ALCH],\n \"ref_check\": [\n   nc(\"OEW:124\", \"Shipley 1984 lending-only on archive.org; not readable.\"),\n   {\"ref\": \"FSD:66\", \"status\": \"not_found\", \"note\": \"See node #13: the F&W alchemy etymology bracket is illegible in the local OCR of vol. I leaf 107.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.2130 s.v. alchemy (p.45)\", \"stance\": \"partial\", \"note\": \"Klein agrees Arabic al-kimiya is the immediate source of the European words but derives the Greek from Egyptian khem ‘black’.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1157\", \"stance\": \"contradicts\", \"note\": \"Derives ar. kimija’ from Egyptian/Coptic kemi ‘black’ and notes “Die ar. Lexikographen leiten ar. kimija’ vom Vb. kamā ‘verbergen’ ab”.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, list p. ~301 (PLA_asbaghi_1988_ia_djvu.txt l.17373)\", \"stance\": \"partial\", \"note\": \"“kimiyä: ‘Chemie’ pers. 675” — Asbaghi records a claim that Arabic kīmiyā is Persian, with derivatives kimiyawi/kimiyawiyya; he offers no Greek route and no support for a Persian one, so this is at most a registered claim, not an endorsement.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur’an (grep kīmiyā)\", \"stance\": \"silent\", \"note\": \"The word is not Qur’anic and Jeffery has no entry.\"}\n ]\n})\n\nN.append({\n \"id\": 15, \"lang\": \"Persian\", \"words\": \"kîmîyâ «کیمیا» (extra: کیموس)\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Persian کیمیا is the Arabic kīmiyāʾ re-borrowed without the article, already fully at home in classical \"\n   \"poetry — hence Nourai’s Hafez line ‘آنچه زر می‌شود از پرتو آن قلب سیاه / کیمیائیست که در صحبت درویشانست’ — with the \"\n   \"characteristic Persian semantic development ‘alchemy’ → ‘the philosophers’ stone’ → ‘something priceless and \"\n   \"unobtainable’ (کیمیا شدن ‘to become unobtainable’). Mo‘in’s footnote in Borhan-e Qate‘ at exactly the cited page \"\n   \"gives the same Greek etymon Nourai claims. The parenthetical کیموس is the neighbouring Borhan entry (Gk. χυμός \"\n   \"‘juice, chyme’, a medical term for the second digestion), a genuine sibling formation from the same Greek stem χυ-.\"),\n \"derivation_fa\": (\"«کیمیا» از عربی الکیمیاء و از راه آن از یونانی χυμεία است؛ معین در حاشیهٔ برهان قاطع (ص ۱۷۵۹) همین را می‌نویسد: «از یونانی … (به معنی اختلاط و امتزاج)». \"\n   \"تحول معنایی در فارسی از «دانش کیمیاگری» به «اکسیر» و سپس «چیز نایاب و گرانقدر» است (کیمیا شدن). «کیموس» هم مدخل همسایهٔ برهان است، از یونانی χυμός «شیره، عصاره» و هم‌ریشه با کیمیا. ادعای نورایی درست است.\"),\n \"sources\": [W_KIM, E_ALCH],\n \"ref_check\": [{\"ref\": \"BQT:1759\", \"status\": \"supports\", \"note\": \"Fetched with tools/ref_page.py BQT:1759 (vol. 3 PDF p.556) — the page carries کیمخت / کیموس / کیمیا / کین in order. Mo‘in’s footnote to کیمیا (OCR): ‘از یونانی … «اشتینگاس» (بمعنی اختلاط و امتزاج) … chimie (فر) … (انگ)’, plus ‘کیمیا. در برهان بمعنی ارزیز که بعربی رصاص گویند نیز آورده’; the footnote to the neighbouring کیموس reads ‘از یونانی χυμός «لیدل و اسکات» «اشتینگاس» (بمعنی سیال و عصاره)’. Both the headword, the parenthetical کیموس and the Greek etymology are on the cited page. Cached at data/verification/sources/refs/ocr/BQT/1759.png/.txt.\"}],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate‘ ed. Mo‘in, p.1759, footnotes to کیمیا and کیموس\", \"stance\": \"supports\", \"note\": \"Greek origin given for both; Mo‘in cites Steingass and Liddell-Scott.\"},\n   {\"src\": \"MON\", \"where\": \"abadis.ir دهخدا/معین s.v. شیمی\", \"stance\": \"supports\", \"note\": \"Dehkhoda’s شیمی entry itself traces the word back to کیمیا, i.e. the two Persian words are recognised as a doublet.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1157\", \"stance\": \"partial\", \"note\": \"Confirms Arabic → European spread but derives the Arabic from Egyptian, not Greek.\"}\n ]\n})\n\nN.append({\n \"id\": 16, \"lang\": \"Latin\", \"words\": \"alchymia\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Medieval Latin alchimia / alchymia ‘alchemy’ is the Arabic al-kīmiyāʾ with the Arabic article agglutinated, \"\n   \"taken over by the 12th-century translators from Arabic in Toledo and Spain (Robert of Chester’s 1144 Liber de \"\n   \"compositione alchemiae is the first Latin text of the art). The y-spelling alchymia is a Renaissance re-Hellenising \"\n   \"after Greek χυμεία, which is also why Klein’s Medieval Latin form is alchemia/alkimia beside it.\"),\n \"derivation_fa\": (\"لاتین میانه alchimia/alchymia همان الکیمیاء عربی است که حرف تعریف «الـ» با آن یکی شده است؛ مترجمان سدهٔ دوازدهم میلادی در طلیطله و اسپانیا آن را وارد کردند. \"\n   \"نگارش y در alchymia بازگشت دوباره به املای یونانی χυμεία در دوران رنسانس است. ادعای نورایی درست است.\"),\n \"sources\": [E_ALCH, W_KIM],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"‘AHD’ without a page here means the main dictionary’s s.v. alchemy (the local file is only the Watkins IE appendix, which has no alchemy entry). Checked instead against Klein p.45 and Etymonline, which give ML. alchemia/alkimia < Arab. al-kimiya.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.2130 s.v. alchemy (p.45)\", \"stance\": \"supports\", \"note\": \"“OF. alquemie (13th cent.), alchimie (14th cent.) (F. alchimie), fr. ML. alchemia, fr. Arab. al-kimiya”.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1157\", \"stance\": \"supports\", \"note\": \"“Aus dem Ar. kommt: it. alchimia … modern chimica … frz. alchimie, chimie, sp. pg. alquimia; dtsch. Alchimie … engl. alchemy”.\"}\n ]\n})\n\nN.append({\n \"id\": 17, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Empty pass-through box for French. The forms are Old French alquemie (13c.), alchimie (14c.), from which \"\n   \"the article-less alchimie → chimie was abstracted in the 16th century, when chemists began to distinguish their art \"\n   \"from alchemy; chimie is the form that both English chemistry and Persian شیمی presuppose.\"),\n \"derivation_fa\": (\"جعبهٔ تهی واسطه برای فرانسوی: alquemie (سدهٔ ۱۳م)، alchimie (سدهٔ ۱۴م)، و سپس chimie در سدهٔ ۱۶م که با افتادن جزء «al-» ساخته شد تا دانش نو از کیمیاگری جدا شود. \"\n   \"همین chimie است که پشت انگلیسی chemistry و فارسی «شیمی» ایستاده است. ادعای نورایی درست است.\"),\n \"sources\": [E_ALCH, W_KIM],\n \"ref_check\": [nc(\"(no refs printed)\", \"No citation in this box; checked against Klein p.45 and Wiktionary’s descendants list for χυμεία (‘French chimie’).\")],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.2130, l.7333 s.v. chemist\", \"stance\": \"supports\", \"note\": \"“chemist, n. — F. chimiste, fr. chimie, ‘chemistry’. See alchemy and -ist.”\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1157\", \"stance\": \"supports\", \"note\": \"“frz. alchimie, chimie” listed among the Arabic-derived European forms.\"}\n ]\n})\n\nN.append({\n \"id\": 18, \"lang\": \"Persian\", \"words\": \"šîmî «شیمی»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"شیمی is French chimie, borrowed in the 19th century with the European sciences taught at the Dar al-Fonun \"\n   \"(founded 1851), where the textbooks and often the teachers were French; Mo‘in tags it [فر.] and Dehkhoda \"\n   \"[فرانسوی]. French /ʃiˈmi/ is rendered شیمی, the initial ch- of the French spelling being read as ش (not کـ, as the \"\n   \"older Arabic-mediated کیمیا has), which is why شیمی and کیمیا are a doublet in Persian: the same Greek word, \"\n   \"once through Arabic in the 9th century and once through French in the 19th.\"),\n \"derivation_fa\": (\"«شیمی» از فرانسوی chimie است که در سدهٔ سیزدهم هجری و با دانش‌های نو در دارالفنون وارد فارسی شد؛ معین [فر.] و دهخدا [فرانسوی] داده‌اند. \"\n   \"این واژه با «کیمیا» دوگانه (doublet) است: یکی از راه عربی در سدهٔ سوم هجری و دیگری از راه فرانسوی در سدهٔ سیزدهم، هر دو از همان χυμείαی یونانی. ادعای نورایی درست است.\"),\n \"sources\": [A_SHI, W_KIM],\n \"ref_check\": [{\"ref\": \"MON:2115\", \"status\": \"partial\", \"note\": \"The 6-vol Mo‘in is not online with pagination; the entry is at abadis.ir (فرهنگ معین): ‘[فر.] علمی است که موضوع آن خواص ماده، ترکیب، تجزیه و تأثیر آنهاست’ — the [فر.] tag matches the chart’s French parent.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. شیمی\", \"stance\": \"supports\", \"note\": \"origin tag [فر.].\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan p.1759, Mo‘in’s footnote to کیمیا\", \"stance\": \"supports\", \"note\": \"The same footnote already links کیمیا to ‘chimie (فر)’ and the English form, i.e. Mo‘in himself connects the Persian pair to the French word.\"}\n ]\n})\n\nN.append({\n \"id\": 19, \"lang\": \"English\", \"words\": \"alchemy, chemistry, chemical\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"ALCHEMY is Middle English (mid-14c.) from Old French alquemie/alchimie, from Medieval Latin alchemia < \"\n   \"Arabic al-kīmiyāʾ. CHEMICAL (1570s) and CHEMIST (from French chimiste) are formed on the article-less stem once \"\n   \"the Renaissance separated the new art from the old; CHEMISTRY is first recorded c.1600 still meaning ‘alchemy’, \"\n   \"narrowing to ‘the study of the composition of substances’ only by 1788. The whole chain is Klein’s p.45 entry, \"\n   \"which is Nourai’s own citation.\"),\n \"derivation_fa\": (\"alchemy در میانهٔ سدهٔ ۱۴م از فرانسوی کهن alquemie و آن از لاتین میانه alchemia و عربی الکیمیاء آمده؛ chemical در ۱۵۷۰ م. و chemistry در حدود ۱۶۰۰ م. هنوز به معنای «کیمیاگری» بوده و تنها از ۱۷۸۸ م. معنای امروزی را گرفته است. \"\n   \"همین زنجیره در کلاین ص ۴۵ آمده که مرجع خود نورایی است. ادعای نورایی درست است.\"),\n \"sources\": [E_ALCH, W_KIM],\n \"ref_check\": [{\"ref\": \"KLN:45\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.2130 (s.v. alchemy, p.45): “alchemy, n. medieval chemistry. — OF. alquemie (13th cent.), alchimie (14th cent.) (F. alchimie), fr. ML. alchemia, fr. Arab. al-kimiya…”; l.7329 “chemic, adj. — See alchemy and -ic and cp. chemist. Derivatives: chemic-al…”; l.7333 “chemist, n. — F. chimiste, fr. chimie … Derivative: chemist-ry, n.”\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Etymonline (OED-based) s.v. alchemy, chemistry\", \"stance\": \"supports\", \"note\": \"“mid-14c., from Old French alchimie (14c.), alquemie (13c.), from Medieval Latin alkimia, from Arabic al-kimiya…”; “chemistry (n.): c. 1600, ‘alchemy’ … the sense ‘scientific study of the composition of material things’ is by 1788.”\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1157\", \"stance\": \"supports\", \"note\": \"“engl. alchemy, alchimij, Vb. to alchemise, chimistry”.\"}\n ]\n})\n\ndoc = {\n \"pdf_page\": 192,\n \"book_page\": 162,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry0]\n}\n\nwith io.open('data/verification/page-192.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", len(N), \"nodes\")\nPYEOF\npython3 -m json.tool data/verification/page-192.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 192",
 "description": "Write and check page-192 verification"
}
```


### [2026-09-06T02:36:29.462Z] TOOL RESULT

```
written 19 nodes
JSON OK
nodes verified: 19/19
node verdicts: {'plausible': 7, 'disputed': 2, 'confirmed': 10}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'not_checked': 6, 'partial': 5, 'not_found': 3}
books consulted: {'partial': 9, 'supports': 30, 'contradicts': 7, 'silent': 5} | by book: {'KLN': 8, 'LKT': 6, 'WLD': 4, 'AHD': 4, 'LAT': 4, 'MON': 4, 'ARY': 3, 'BRT': 2, 'HUB': 2, 'PHD': 2, 'HRN': 2, 'POK': 2, 'BQT': 2, 'NYB': 1, 'SOD': 1, 'SKT': 1, 'FSD': 1, 'PLA': 1, 'FVQ': 1}
```


## [2026-09-06T02:36:49.051Z] AGENT

Page 192 (book p.162) verified — `data/verification/page-192.json`, `verify_check.py 192` reports 0 PROBLEM lines.

**Counts** — root: 1 confirmed. Nodes (19): 10 confirmed, 7 plausible, 2 disputed. Ref checks: 9 supports / 5 partial / 3 not_found / 6 not_checked (OEW is lending-only; MON's 6-vol pagination is not online).

**Disputed**
- `#2 Pahlavi zôt "holy water"` — MacKenzie has `zōt [zwt'] = Av. zaotar-` "first officiating priest"; the Pahlavi word for the libation is `zōhr [zwhl]`. Horn no. 675 (`phlv. zōhr, zūr`), Hübschmann, Aryanpur p.330 and Wiktionary PII all give Av. zaoθra- → MP zōhr → NP زور. Nourai lifted Pokorny's "mpers. zōt", which there glosses zaotar- 'priest', and re-glossed it to bridge to زور. Knock-on: node #3 (زور۲) downgraded to plausible — right root, wrong intermediate.
- `#4 Avestan "zav 2: a kind of alcoholic beverage"` — unattested. Bartholomae's Avestan zav- is 'to call/invoke' (Nourai's own zav 1). SOD:184 is not_found: Gharib p.184 (leaf 249) has znuk 'knee', zōt 'strike', žukyamenc; entry no. 184 is the name Ānanda. Gharib's only "beer, liquor" word is Sogdian `zwt'k` (no. 11503, p.469) — Sogdian, not Avestan, and a different page. āzūtay- in the same box is fine.

**Notable non-flags**
- The alchemy branch (#13–#19) is the one Nourai himself flags as contested, and modern scholarship sides *with* him: Wiktionary derives Arabic كيمياء straight from Gk. χυμεία < χύμα < *ǵʰew-, and Etymonline quotes the OED that "khymeia was likely original". Klein p.45 ("folk etymology") and Lokotsch no. 1157 (Egyptian *kemi* 'black') are the dissenters, both recorded.
- BQT:1759 fetched and cached (`sources/refs/ocr/BQT/1759.png/.txt`): Mo'in's footnote derives کیمیا from Greek χυμεία "اختلاط و امتزاج", and the neighbouring کیموس from χυμός — matching Nourai's parenthetical.
- BQT:1043 lands at printed p.1045 in our scan (Purdavud's زور = Av. zaoθra footnote at زوراشنا); the ±2 is within the leaf→page offset uncertainty, counted as supports.

**Extraction issues for the owner**: none substantive. One cosmetic omission — the printed chart has a completely blank rectangle to the right of node #4 (no language header, no words) that is not in the JSON; it carries no content.
