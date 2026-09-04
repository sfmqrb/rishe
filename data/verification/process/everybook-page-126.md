# Verification process log — everybook-page-126


## [2026-09-04T18:37:40.097Z] INPUT

Task: bring an existing verification file up to the "consult every relevant book" rule. File: /home/sfmqrb/git/rishe/data/verification/page-126.json (root Dheigh "to knead clay", 16 nodes: divâr, dež, pairi-daeza, pâlîz, pardîs/ferdows, paradeisos, paradise, daika/dîg, dough, figure). The chart with Nourai's citations is /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-126.txt.

Read /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md, in particular the sections "Use EVERY relevant book on disk", "Checking Nourai's OWN cited references" and "Process documentation", and the source matrix /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md (file paths of every local book — they all exist under /home/sfmqrb/git/rishe/data/verification/sources/refs/; the reference table /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json gives page offsets and lookup hints; scanned pages via tools/ref_page.py, e.g. BQT:1500 or BQT5:12).

For the root entry and for EVERY node: grep the books the matrix lists for that node's language (IE root: Pokorny POK, Walde-Pokorny WLD, Watkins AHD, Mann IEC, Buck SYN; Avestan/Old Persian: Bartholomae BRT, Kent KNT; Pahlavi: MacKenzie PHD, Nyberg NYB; Persian: Horn HRN, Hübschmann HUB, Cheung, Borhan BQT vols 1-5, Mo'in MON, Aryanpur ARY; Sogdian: Gharib SOD; Greek/Latin/English: Klein KLN, Skeat SKT, Funk & Wagnalls FSD, Webster WEB, Ernout-Meillet LAT, Walde LEW; Arabic round-trip: Jeffery FVQ, Asbaghi PLA, Addi Shir AFM), and add a `consulted` array to the node exactly as specified: {"src","where","stance" (supports/contradicts/partial/silent),"note" with the quoted phrase}. At least two different books per node where the matrix lists two or more; "silent" entries count. Do not duplicate what is already in `ref_check` — but if a `ref_check` item is `not_checked`/`not_found` and the book is NOW on disk or better indexed (Borhan vols 3-5 with page maps, Asbaghi, Irānvij, Walde-Pokorny 1-2), re-check it and update its status/note. Do NOT change verdicts, derivations or sources unless a book plainly overturns the existing verdict; in that case update the verdict, append one sentence to `derivation`, and say so in your summary. If you use a web page, archive it with tools/fetch_source.py and add it to `sources`.

Write the file back in place (valid JSON, UTF-8). Run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 126` (0 PROBLEM lines; "books consulted" tally non-empty). Reply with a short summary: consulted entries by stance, books used, ref_check upgrades, and any verdict changes with reasons.


## [2026-09-04T18:37:41.638Z] AGENT

I'll start by reading the instructions and context files.


## [2026-09-04T18:37:43.050Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:37:43.066Z] TOOL RESULT

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
97	## Process documentation (required)
98	
99	The owner wants to be able to audit every step later. Therefore:
100	
101	- **Every web page you rely on must be archived**: after you read a page (WebFetch or
102	  curl), run
103	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
104	  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
105	  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
106	  one Bash command to save time.)
107	- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` include
108	  the exact phrase(s) you found (with the grep pattern or page you used, e.g.
109	  "KLN.txt p.164 (ff-page 178): 'cherub … prob. rel. to Akkad. karābu'"), so the finding can
110	  be re-run.
111	- Your full transcript (every tool call and result) is exported automatically by the
112	  coordinator; nothing else needed for that.
113	
114	
115	## Use EVERY relevant book on disk (required)
116	
117	Checking only the reference Nourai cites is not enough. For every node, also consult the
118	other books in the local library that could speak to that claim, and record what each says.
119	The list of which books cover which kind of node, with file paths, is
120	`/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md`
121	(also `data/verification/sources/SOURCE_MATRIX.md`). Minimum per node:
122	
123	- an Indo-European node or root box: Pokorny (POK) AND Walde-Pokorny (WLD) AND Watkins/AHD,
124	  plus Mann (IEC) or Buck (SYN) when the word is a common noun;
125	- an Avestan / Old Persian node: Bartholomae (BRT) or Kent (KNT);
126	- a Pahlavi / Middle Persian node: MacKenzie (PHD) and Nyberg (NYB);
127	- a New Persian node: Horn (HRN), Hübschmann (HUB), Cheung (CHEUNG, for verbs), Borhan-e
128	  Qate' with Mo'in's footnotes (BQT), Mo'in (MON), and Aryanpur (ARY, once its text exists);
129	- a Sogdian node: Gharib (SOD); a Khotanese one: Bailey (ISS_alt_DKS);
130	- an Arabic node or a Persian/Arabic loan in either direction: Klein (KLN), Jeffery (FVQ),
131	  Addi Shir (AFM), Asbaghi (PLA), Fraenkel (AFA), Lokotsch (LKT); for French/Spanish
132	  Arabisms Pihan (PHN), Devic (DEV), Lammens (LAM), Dozy (DOZ);
133	- an English / Romance node: Klein (KLN), Skeat (SKT), Funk & Wagnalls (FSD), Webster (WEB);
134	  Anglo-Indian words: Hobson-Jobson (HJB), Whitworth (AID);
135	- a Turkic node: Vámbéry (TTS), Lokotsch (LKT).
136	
137	Grep each file for the headword (several spellings; Latin transliteration for the Western
138	books, Persian script for BQT/MON/ARY, Pahlavi transliteration for PHD/NYB). A grep that
139	finds nothing is also a result ("silent"). Record everything in a `consulted` array on the
140	node (separate from `ref_check`, which is only for the references Nourai himself cites):
141	
142	```json
143	"consulted": [
144	  {"src": "HRN", "where": "no. 3, p. 1", "stance": "contradicts", "note": "Horn separates āb 'Glanz' from āb 'water' and derives āftāb from the former"},
145	  {"src": "PHD", "where": "p. 5 s.v. ābād", "stance": "supports", "note": "'ābād [ʾpʾt] populous, thriving' — no water element"},
146	  {"src": "WLD", "where": "Bd. I p. 46", "stance": "silent", "note": "root ap- listed, no Persian compound"}
147	]
148	```
149	
150	`stance` ∈ supports / contradicts / partial / silent. Quote the key phrase. Books consulted
151	via the web (vajehyab for Mo'in, AHD online) go here too, with the URL archived via
152	fetch_source.py and listed in `sources`. Every node must have at least two `consulted`
153	entries from different books whenever the matrix lists two or more books for its language.
154	
155	## Sources to use (in roughly this order)
156	
157	- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
158	  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
159	  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
160	  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
161	  Use URL-encoded Persian/Arabic script for those pages.
162	- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
163	- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
164	  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
165	  appendix; the online appendix is the updated edition of the same list.
166	- **Pokorny** — via indo-european.info, starlingdb.org, or Wiktionary's Pokorny citation;
167	  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
168	- **Klein's Comprehensive Etymological Dictionary** (KLN) and **Horn's Grundriss der
169	  neupersischen Etymologie** (HRN), **Hübschmann's Persische Studien** (HUB),
170	  **MacKenzie's Concise Pahlavi Dictionary** (PHD), **Bartholomae AiW** (BRT) are on archive.org
171	  if needed for a hard case.
172	- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
173	- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
174	- Use WebSearch when you don't know the right page; use WebFetch to read a page.
175	
176	Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
177	If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
178	source covering the chain is enough; spend your effort on the Iranian and Semitic links,
179	which are where errors are likelier.
180	
181	## Output — write ONE file per page
182	
183	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
184	
185	```json
186	{
187	  "pdf_page": 126,
188	  "book_page": 96,
189	  "verified_by": "claude-fable-5-1",
190	  "verified_on": "2026-09-04",
191	  "entries": [
192	    {
193	      "entry": 0,
194	      "root": "Dheigh, Dhigha",
195	      "verdict": "confirmed",
196	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
197	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
198	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
199	      "nodes": [
200	        {
201	          "id": 6,
202	          "lang": "Avestan",
203	          "words": "pairi-daeza",
204	          "verdict": "confirmed",
205	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' (PIE *dʰeyǵʰ-, o-grade *dʰoyǵʰ-o- > Iranian *daiza-). Attested in the Vidēvdād (pairi-daēzaiiąn) …",
206	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza", "https://www.etymonline.com/word/paradise"]
207	        },
208	        {
209	          "id": 9,
210	          "lang": "Greek",
211	          "words": "paradeisos",
212	          "verdict": "confirmed",
213	          "derivation": "Borrowed from Old Iranian *paridaiza- (Median/Old Persian form with -d-, cf. Elamite par-te-taš, Akkadian pardēsu) in the 5th c. BCE; first in Xenophon (Anabasis 1.2.7) for the Persian kings' walled hunting parks. Greek -ei- renders Iranian /ai/ ~ /ē/; -os is the Greek nominative ending. The Septuagint (3rd c. BCE) used it for the Garden of Eden, whence the 'heaven' sense.",
214	          "sources": ["https://en.wiktionary.org/wiki/παράδεισος"]
215	        }
216	      ]
217	    }
218	  ]
219	}
220	```
221	
222	Rules:
223	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
224	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
225	- `words` = the transliterations of the node joined by "; " (copy from the chart).
226	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
227	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
228	- Keep `note` on the entry for root-level comments and for anything cross-cutting
229	  (e.g. "Nourai's whole Semitic branch here is rejected by Klein …").
230	- If a node lists several words, cover each word; if they differ in verdict, use the worst
231	  verdict for the node and explain per word in `derivation`.
232	- Where the chart's own NOTE already records a dispute (e.g. "POK:694 derives Latin mattus
233	  from root Mad"), evaluate it: say which side modern scholarship takes.
234	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted` (array).
235	- Valid JSON only. Test it with `python3 -m json.tool` before finishing.
236	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
237	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason).
238	  Do not paste the JSON back into your reply.
239	
```


## [2026-09-04T18:37:43.911Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T18:37:43.946Z] TOOL RESULT

```
1	# Source matrix — which local books to grep for each kind of node
2	
3	All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.
4	
5	ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).
6	
7	
8	## Indo-European roots (any IE node, root boxes)
9	
10	- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
11	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt`
12	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt`
13	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt`
14	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt`
15	- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
16	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt`
17	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
18	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
19	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
20	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
21	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
22	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
23	- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
24	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
25	- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
26	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
27	- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
28	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
29	- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
30	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
31	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
32	- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
33	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
34	- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
35	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt`
36	- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
37	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt`
38	- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
39	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
40	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
41	
42	## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian
43	
44	- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
45	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt`
46	- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
47	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
48	- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
49	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt`
50	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD_mackenzie.txt`
51	- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
52	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt`
53	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt`
54	- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
55	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt`
56	- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
57	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt`
58	- **CHEUNG** — CHEUNG
59	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/CHEUNG.txt`
60	- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
61	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt`
62	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt`
63	- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
64	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt`
65	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt`
66	- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
67	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
68	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
69	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
70	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
71	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
72	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
73	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
74	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
75	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
76	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
77	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
78	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
79	- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
80	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
81	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
82	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
83	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
84	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
85	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
86	- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
87	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt`
88	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt`
89	- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
90	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt`
91	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt`
92	- **HENNING** — HENNING
93	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt`
94	- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
95	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/EAV_studies.txt`
96	- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
97	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ISS_alt_DKS.txt`
98	- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
99	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt`
100	- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
101	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
102	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
103	- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
104	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
105	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
106	- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
107	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
108	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
109	- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
110	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AVG.txt`
111	- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
112	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HID.txt`
113	- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
114	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
115	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
116	- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
117	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TLM.txt`
118	- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
119	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt`
120	- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
121	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SBK.txt`
122	
123	## Semitic / Arabic loans in either direction
124	
125	- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
126	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
127	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
128	- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
129	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt`
130	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt`
131	- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
132	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt`
133	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt`
134	- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
135	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
136	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
137	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
138	- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
139	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt`
140	- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
141	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt`
142	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt`
143	- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
144	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt`
145	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt`
146	- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
147	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KFL.txt`
148	- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
149	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
150	- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
151	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
152	- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
153	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
154	- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
155	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt`
156	- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
157	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt`
158	- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
159	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt`
160	- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
161	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt`
162	- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
163	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
164	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
165	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
166	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
167	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
168	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
169	- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
170	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
171	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
172	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
173	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
174	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
175	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
176	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
177	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
178	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
179	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
180	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
181	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
182	
183	## English / Romance / Germanic
184	
185	- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
186	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
187	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
188	- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
189	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
190	- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
191	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt`
192	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt`
193	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt`
194	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt`
195	- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
196	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt`
197	- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
198	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
199	- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
200	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
201	- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
202	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
203	- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
204	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
205	- **RCH** — J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1
206	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt`
207	- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
208	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
209	- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
210	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
211	- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
212	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
213	- **NAT** — C. Berlitz, Native Tongues, New York 1982
214	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt`
215	- **PEI** — M. Pei, The Families of Words, New York 1962
216	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt`
217	
218	## Turkic / Mongolian
219	
220	- **TTS** — H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)
221	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt`
222	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf`
223	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt`
224	- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
225	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
226	- **VIE** — M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985
227	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_pages.txt`
228	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf`
229	
230	## Sanskrit / Hindustani
231	
232	- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
233	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
234	- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
235	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
236	- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
237	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
238	- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
239	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
240	- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
241	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
242	- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
243	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
```


## [2026-09-04T18:37:47.711Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-126.txt",
 "description": "Read chart file"
}
```


### [2026-09-04T18:37:47.753Z] TOOL RESULT

```
=== PDF page 126 (book page 96) ===
--- entry 0 ---
ROOT [Indo-European] Dheigh, Dhigha : to form out of clay, to knead clay or dough  (refs POK:244; KNT:191; CEL3:203)
#1 (parent #0) [Old Persian] refs=HRN:133; KNT:191; IEC:191 | didâ, děğa-vâra : clay wall ☞Wer 3
  #2 (parent #1) [Persian] refs=BQT:918 | dîvâr «دیوار» : wall
  #3 (parent #1) [Sogdian] refs=SOD:151 | dyz` : fort
#4 (parent #0) [Avestan] refs=POK:244 | daeza : wall, fortification
  #5 (parent #4) [Persian] refs=BQT:851; MON5:528 | dež «دژ ( دژبان، دژدار )» : fort ; dež-pol «دژ پل ( دزفول )» : strong bridge
  #6 (parent #4) [Avestan] refs=POK:244 | pairi-daeza : with walls around it (garden) ☞Per 1
    #7 (parent #6) [Persian] refs=BQT:359; MON:680 | pâlîz, jâlîz «پالیز ، جالیز» : melon farm
    #8 (parent #6) [Persian] refs=BQT:1455 | pardîs, ferdows «پردیس ، فردوس» : heaven
    #9 (parent #6) [Greek] refs=AHD:950 | paradeisos : garden, park
      #10 (parent #9) [English] refs=None | paradise
#11 (parent #0) [Old Persian] refs=HUB:65; KLN:469 | daika : clay pot
  #12 (parent #11) [Persian] refs=BQT:912,914; KLN:469 | dîg «دیگ ( دیزی )»
#13 (parent #0) [Germanic] refs=AHD | daigaz : dough ; dîg : one who kneads dough, lady of the house
  #14 (parent #13) [English] refs=None | dough ; lady, dairy
#15 (parent #0) [Latin] refs=AHD | figŭra : result of kneading, shape
  #16 (parent #15) [English] refs=None | figure, fiction
```


## [2026-09-04T18:37:48.390Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/page-126.json",
 "description": "Read verification file"
}
```


### [2026-09-04T18:37:48.442Z] TOOL RESULT

```
<persisted-output>
Output too large (31.5KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bnkniayu2.txt

Preview (first 2KB):
{
  "pdf_page": 126,
  "book_page": 96,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "Dheigh, Dhigha",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form, build (of clay)'; o-grade noun *dʰóyǵʰos 'something kneaded/formed' > 'wall; dough'",
      "note": "Pokorny IEW 244 dheiĝh- 'Lehm kneten und damit mauern oder bestreichen (Wand, Mauer; Töpferei); auch vom Teigkneten' is exactly Nourai's gloss; AHD dheigh- 'to form, build' cites 'Pokorny dheiĝh- 244'. Wiktionary (Rix LIV 140-141, Kroonen, de Vaan, Beekes) agrees. Nourai's second spelling 'Dhigha' is his rendering of the zero-grade/extended variant (Pokorny gives dheiĝh-, dhoiĝho-s, dhiĝh-lo-s). Two of his branches are weak: the OP 'daika > dīg' branch is rejected by modern Iranian etymology (see nodes 11-12), and the Sogdian, Persian dež and ferdows nodes are cognates/round-trip loans rather than lineal descendants of the parents drawn.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-",
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰóyǵʰos",
        "https://www.thefreedictionary.com/_/roots.aspx?type=Indo-European&root=dheigh-",
        "https://www.etymonline.com/word/*dheigh-",
        "https://starlingdb.org/cgi-bin/etymology.cgi?root=config&basename=%2Fdata%2Fie%2Fpokorny&text_recno=1208&single=1"
      ],
      "ref_check": [
        {
          "ref": "POK:244",
          "status": "supports",
...
</persisted-output>
```


## [2026-09-04T18:37:52.301Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-126.json'))\ne=d['entries'][0]\nprint('ROOT ref_check:', json.dumps(e.get('ref_check'),ensure_ascii=False)[:2000])\nprint('ROOT consulted:', json.dumps(e.get('consulted'),ensure_ascii=False)[:500])\nfor n in e['nodes']:\n    print('---', n['id'], n['lang'], n['words'], n['verdict'])\n    print('  refcheck:', json.dumps(n.get('ref_check'),ensure_ascii=False))\n    print('  consulted:', json.dumps(n.get('consulted'),ensure_ascii=False)[:300])\n\""
}
```


### [2026-09-04T18:37:55.311Z] TOOL RESULT

```
ROOT ref_check: [{"ref": "POK:244", "status": "supports", "note": "POK_01.txt leaves 255-256 (IEW pp. 244-245), s.v. dheiĝh-: 'Lehm kneten und damit mauern oder bestreichen (Mauer, Wall; Töpferei; dann auch von anderweitigem Bilden); auch vom Teig kneten (Bäckerei)'; dheiĝho-s, dhoiĝho-s 'Gebilde, Wall' ... 'ai. dēhmi bestreiche ... dehī f. Wall, Damm, Aufwurf, av. pairi-daēzayeiti mauert ringsum ... uz-daēza- m. Aufhäufung, Wall, pairi-daēza- m. Umfriedigung (daraus gr. paradeisos), apers. didā Festung (aus *dizā-, Wurzelnom. auf -ā), npers. diz, dez ds.; ... gr. teichos n., toichos m. Mauer, Wand; ... lat. fingō ... figūra Bildung, Gestalt, Figur, fictiō ...; got. daigs m. Teig (*dhoighos), anord. deig, ags. dāg, ahd. teig ds.'"}, {"ref": "KNT:191", "status": "supports", "note": "KNT.txt leaf 214 (Kent p. 191): 'didā- sb. wall, stronghold, fortress: NPers. diz, pIE *dhiĝhā-, cf. Skt. dehī- wall, Gk. teichos, NEng. dike, ditch ... Cf. also paradayadām. didā nsf. DB 1.58; 2.39, 44; 3.61, 72; DSe 46; DSf 42. didām asf. DB 2.78; DSe 48; DSf 54.' Kent puts OP didā- under pIE *dhiĝhā- with Skt. dehī-, Gk. teichos."}, {"ref": "CEL3:203", "status": "not_checked", "note": "CEL3 is not in refs_online.json (no online copy located)."}]
ROOT consulted: null
--- 1 Old Persian didâ, děğa-vâra transcription_suspect
  refcheck: [{"ref": "HRN:133", "status": "supports", "note": "HRN.txt leaf 154 (Horn p. 133), No. 599: 'dīvār Mauer, Wand. ap. *deghavāra- (vergl. gr. teichos, osk. feíhúss). Nöldeke (mündliche Mitteilung), unter der Voraussetzung, dass die np. Grundform *dēvār lautete ...; kurd. LW. dīwār; wax. LW. dival, sar. delvūl Mauer, Wand, Umwallung.' Cf. No. 563 (leaf 146, p. 125): 'diz, dez Burg ... ap. didā Festung; aw. daēza-; phlv. d(i)z ... Ascoli's Erklärung von np. dīvār Mauer aus ap. *didavara- Stadtwall ist daher nicht wahrscheinlich'. Nourai's 'děğa-vâra' is Horn's *deghavāra-; his 'didâ' is Horn's/Kent's ap. didā. (Horn himself, No. 563, rejects deriving dīvār from *dida-vara-.)"}, {"ref": "KNT:191", "status": "supports", "note": "KNT.txt leaf 214 (Kent p. 191): 'didā- sb. wall, stronghold, fortress: NPers. diz, pIE *dhiĝhā-, cf. Skt. dehī- wall, Gk. teichos, NEng. dike, ditch ... Cf. also paradayadām. didā nsf. DB 1.58; 2.39, 44; 3.61, 72; DSe 46; DSf 42. didām asf. DB 2.78; DSe 48; DSf 54.'"}, {"ref": "IEC:191", "status": "partial", "note": "IEC.txt leaf 112 (Mann cols ~193-194), s.v. dheigh-: 'shape, earth up; form, wall ... Cf. dhoigh- Skt. dehah shape, body; Av. (pairi-)daēzō surrounding fence beside diz- earth up, cover; LW in Arm. dez mound, dizem pile up; Gk. teikhos outer wall, dam; Osc. feíhúss, acc.pl. walls; Go. digan (z-gde) shape, mould ... For Cz. díže kneading-trough and OHG teic, E dough, etc. see dhoiĝh-.' Mann gives the root and Av. (pairi-)daēza- but does not list Old Persian didā- or *daiga-vāra-."}]
  consulted: null
--- 2 Persian dîvâr confirmed
  refcheck: [{"ref": "BQT:918", "status": "not_found", "note": "BQT_v2_pages.txt leaves 375-378 (printed pp. ~918-921) are the دیو- entries, but the دیوار headword and Mo'in's footnote are not recoverable from the OCR (only the following entry 'دیوال = با لام، بر وزن و معنی دیوار است، چه در فارسی را و لام بهم تبدیل می‌یابند' on leaf 378 is legible). Mo'in's online text (vajehyab) tags دیوار [په.] = Pahlavi (refs_online.json note)."}]
  consulted: null
--- 3 Sogdian dyz` plausible
  refcheck: [{"ref": "SOD:151", "status": "supports", "note": "SOD_pages.txt leaf 216 (Gharib p. 151), entry 3825: 'δyz' M — δiza (dyz') < OP didā, f. n., stronghold, fort. BBB f 57; STii 3.27'; entry 3826 'dyz' C = δyz''. Gharib derives Sogdian δyz' 'stronghold, fort' from OP didā — exactly the arrow drawn from node #1."}]
  consulted: null
--- 4 Avestan daeza confirmed
  refcheck: [{"ref": "POK:244", "status": "supports", "note": "POK_01.txt leaves 255-256 (IEW pp. 244-245), s.v. dheiĝh-: 'Lehm kneten und damit mauern oder bestreichen (Mauer, Wall; Töpferei; dann auch von anderweitigem Bilden); auch vom Teig kneten (Bäckerei)'; dheiĝho-s, dhoiĝho-s 'Gebilde, Wall' ... 'ai. dēhmi bestreiche ... dehī f. Wall, Damm, Aufwurf, av. pairi-daēzayeiti mauert ringsum ... uz-daēza- m. Aufhäufung, Wall, pairi-daēza- m. Umfriedigung (daraus gr. paradeisos), apers. didā Festung (aus *dizā-, Wurzelnom. auf -ā), npers. diz, dez ds.; ... gr. teichos n., toichos m. Mauer, Wand; ... lat. fingō ... figūra Bildung, Gestalt, Figur, fictiō ...; got. daigs m. Teig (*dhoighos), anord. deig, ags. dāg, ahd. teig ds.' Pokorny: 'uz-daēza- m. Aufhäufung, Wall, pairi-daēza- m. Umfriedigung' under dheiĝh-."}]
  consulted: null
--- 5 Persian dež; dež-pol confirmed
  refcheck: [{"ref": "BQT:851", "status": "partial", "note": "BQT_v2_pages.txt leaf 311 (printed p. ~854; Nourai 851): 'دژ = بکسر اول و سکون ثانی، قلعه و حصار باشد' with footnote marker ۱; Mo'in's footnote (Pahlavi/Avestan forms) is not legible in the OCR of this leaf."}, {"ref": "MON5:528", "status": "not_checked", "note": "MON vol. 5 (a'lam / proper names) is not online; vajehyab/abadis carry only the lexicon volumes."}]
  consulted: null
--- 6 Avestan pairi-daeza confirmed
  refcheck: [{"ref": "POK:244", "status": "supports", "note": "POK_01.txt leaves 255-256 (IEW pp. 244-245), s.v. dheiĝh-: 'Lehm kneten und damit mauern oder bestreichen (Mauer, Wall; Töpferei; dann auch von anderweitigem Bilden); auch vom Teig kneten (Bäckerei)'; dheiĝho-s, dhoiĝho-s 'Gebilde, Wall' ... 'ai. dēhmi bestreiche ... dehī f. Wall, Damm, Aufwurf, av. pairi-daēzayeiti mauert ringsum ... uz-daēza- m. Aufhäufung, Wall, pairi-daēza- m. Umfriedigung (daraus gr. paradeisos), apers. didā Festung (aus *dizā-, Wurzelnom. auf -ā), npers. diz, dez ds.; ... gr. teichos n., toichos m. Mauer, Wand; ... lat. fingō ... figūra Bildung, Gestalt, Figur, fictiō ...; got. daigs m. Teig (*dhoighos), anord. deig, ags. dāg, ahd. teig ds.' 'pairi-daēza- m. Umfriedigung (daraus gr. paradeisos)'."}]
  consulted: null
--- 7 Persian pâlîz, jâlîz plausible
  refcheck: [{"ref": "BQT:359", "status": "partial", "note": "BQT_v1_pages.txt leaf 581 (printed p. ~361; Nourai 359): 'پالیز ۱ - بر وزن کاریز، بمعنی باغ و بوستان و کشتزار باشد عموماً و خربزه‌زار و خیارزار و هندوانه‌زار را گویند خصوصاً'; Mo'in's etymological footnote ۱ is not legible in the OCR. The gloss (garden, melon field) matches; the derivation from pairi-daēza- is in Mo'in's note, which the OCR does not preserve."}, {"ref": "MON:680", "status": "partial", "note": "vajehyab.com (Mo'in) s.v. پالیز: '(اِ.) ۱- باغ، بوستان. ۲- کشتزار. ۳- زمینی که در آن خربزه، خیار و مانند آن بکارند' — meaning confirmed; the online text carries no origin tag or Avestan form for this entry. Archived https://vajehyab.com/?q=پالیز&d=moein."}]
  consulted: null
--- 8 Persian pardîs, ferdows plausible
  refcheck: [{"ref": "BQT:1455", "status": "not_checked", "note": "Borhan-e Qate' (Mo'in ed.) vols 3-5 are not online in full text (only vols 1-2 on archive.org)."}]
  consulted: null
--- 9 Greek paradeisos confirmed
  refcheck: [{"ref": "AHD:950", "status": "supports", "note": "AHD online (archived) s.v. paradise: '[Middle English paradis, from Old French, from Late Latin paradīsus, from Greek paradeisos, garden, enclosed park, paradise, from Avestan pairidaēza-, enclosure, park : pairi-, around; see per1 ... + daēza-, wall; see dheigh- ...]'. Nourai's AHD:950 is the 1976 page of this same entry."}]
  consulted: null
--- 10 English paradise confirmed
  refcheck: [{"ref": "none", "status": "not_checked", "note": "Nourai cites no reference for this node. The AHD paradise entry checked at node #9 (archived https://ahdictionary.com/word/search.html?q=paradise) gives 'Middle English paradis, from Old French, from Late Latin paradīsus, from Greek paradeisos'."}]
  consulted: null
--- 11 Old Persian daika disputed
  refcheck: [{"ref": "HUB:65", "status": "partial", "note": "HUB.txt leaf 75 (Hübschmann p. 65), No. 594: 'Wenn dēz, dēza Kochtopf zu got. deigan kneten, aus Thon formen (Wzl. dheigh) gehört, ist es verwandt mit Nr. 563 diz, dēz Burg. Ob auch dēg Kochtopf dazu gehört, ist fraglich, da 1) idg. dhigh durch skr. dēgdhi, digdha- nicht gesichert ist und 2) idg. dhoigho- im Neup. zu *dēy werden müsste. Np. dēg (afgh. LW. dēg Kessel) setzt ap. *daika- voraus. Phl. dēg Kessel (Gl. and Ind. 288) kann eine junge Form sein.' No. 599 (same page): 'Besser *daidavara- (Festungsmauer) als *daigavara- anzusetzen ... Falls dīvār (mit ī) die ursprüngliche Form ist ..., wäre dīvār über *diyvār = *did-vār auf ap. *dida-vara- zurückzuführen. Alles unsicher.' Hübschmann does posit ap. *daika- for np. dēg (Nourai's 'daika'), but he explicitly doubts that dēg belongs to the root dheigh- ('ist fraglich')."}, {"ref": "KLN:469", "status": "supports", "note": "KLN_1966.txt leaf 256 (printed pp. 468-469), s.v. 'dixie, dixy' (mess tin): 'Hind. degchī, a small kettle, fr. Pers. degcha, dimin. of deg, pot, which is rel. to Pahlavi dēg, pot, Arm. dez, heap, and to OI. dihmi, I smear, anoint, fr. I.-E. base *dheigh-, *dhoigh-, *dhigh-, to form out of clay, to knead, form. See dough and cp. next word [dizdar, fr. Pers. diz, castle].' Klein derives Pers. deg 'pot' (Pahlavi dēg) from I.-E. *dheigh- 'to form out of clay' — the arrow from the root; he does not give an Old Persian form."}]
  consulted: null
--- 12 Persian dîg disputed
  refcheck: [{"ref": "BQT:912,914", "status": "partial", "note": "BQT_v2_pages.txt leaves 371-372 (printed pp. ~914-915): the دیگ entry area; leaf 371 footnote cites 'Henning, Two Central Asian words, Hertford 1946' and leaf 372 mentions «دیگه» and دیزی (فرهنگ اسدی); Mo'in's Latin-script Pahlavi/Old Persian forms are not legible in the OCR."}, {"ref": "KLN:469", "status": "supports", "note": "KLN_1966.txt leaf 256 (printed pp. 468-469), s.v. 'dixie, dixy' (mess tin): 'Hind. degchī, a small kettle, fr. Pers. degcha, dimin. of deg, pot, which is rel. to Pahlavi dēg, pot, Arm. dez, heap, and to OI. dihmi, I smear, anoint, fr. I.-E. base *dheigh-, *dhoigh-, *dhigh-, to form out of clay, to knead, form. See dough and cp. next word [dizdar, fr. Pers. diz, castle].'"}]
  consulted: null
--- 13 Germanic daigaz; dîg confirmed
  refcheck: [{"ref": "AHD", "status": "supports", "note": "AHD_watkins1985.txt line 377 s.v. dheigh-: 'To form, build. 1. Germanic *daigjōn in Old English dǣge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound hlǣfdige, mistress of a household (< bread kneader; hlāf, bread, loaf): LADY. 3. Extended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dāg, dough: DOUGH ... 4. Suffixed zero-grade form *dhigh-ūrā, in Latin figūra, form, shape (< result of kneading): FIGURE ... 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: FEIGN, FICTION, FIGMENT; EFFIGY ... 7. Suffixed o-grade form *dhoigh-o- in Avestan daēza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.]' (same list online at ahdictionary.com/word/indoeurop.html#dheigh-). Germanic *daigaz 'dough' and OE dǣge 'bread kneader' (DAIRY), hlǣfdige (LADY) are items 1-3."}]
  consulted: null
--- 14 English dough; lady, dairy confirmed
  refcheck: [{"ref": "none", "status": "not_checked", "note": "Nourai cites no reference for this node. Covered by the AHD dheigh- entry checked at node #13: DAIRY, LADY, DOUGH."}]
  consulted: null
--- 15 Latin figŭra confirmed
  refcheck: [{"ref": "AHD", "status": "supports", "note": "AHD_watkins1985.txt line 377 s.v. dheigh-: 'To form, build. 1. Germanic *daigjōn in Old English dǣge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound hlǣfdige, mistress of a household (< bread kneader; hlāf, bread, loaf): LADY. 3. Extended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dāg, dough: DOUGH ... 4. Suffixed zero-grade form *dhigh-ūrā, in Latin figūra, form, shape (< result of kneading): FIGURE ... 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: FEIGN, FICTION, FIGMENT; EFFIGY ... 7. Suffixed o-grade form *dhoigh-o- in Avestan daēza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.]' (same list online at ahdictionary.com/word/indoeurop.html#dheigh-). Item 4: '*dhigh-ūrā, in Latin figūra, form, shape (< result of kneading): FIGURE'."}]
  consulted: null
--- 16 English figure, fiction confirmed
  refcheck: [{"ref": "none", "status": "not_checked", "note": "Nourai cites no reference for this node. Covered by the AHD dheigh- entry checked at node #15: FIGURE; FICTION (item 5, Latin fingere)."}]
  consulted: null
```


## [2026-09-04T18:38:11.120Z] TOOL CALL #6: Bash

```json
{
 "command": "ls tools/ && python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['BQT','MON','ARY','IRN','PLA','WLD','SOD','FVQ','AFM']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:900]); print()\n\""
}
```


### [2026-09-04T18:38:13.173Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"], "page_offset": "222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368.",

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py P

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.", "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (19

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", "covers_etymology": true, "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.", "
```


## [2026-09-04T18:38:20.087Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"dheiĝh\\|dheigh\\|dhoiĝh\\|dhoigh\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -40\necho \"=== Bd2\"\ngrep -n -i \"dheiĝh\\|dheigh\\|dhoiĝh\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20\necho \"=== band3\"\ngrep -n -i \"dheiĝh\\|dheigh\" WLD_band3.txt | head -20"
}
```


### [2026-09-04T18:38:20.177Z] TOOL RESULT

```
49898:richte“ gehoren jedenfalls zu lat. fmgo usw., s. u. dheigh- „Lehm kneten“, 
52492:zw.), sondern als „streichelnd betasten, wie knetend beriihren ££ zu dheigh- 
52495:dheigh- ..Lelim kneten und damit mauern oder bestreicben (Mauer, Wall; 
52505:sucht Meillet Msl. 16, 3 1 5 f . ein Wznomen *dheigh, *dhi?j Ms zu erschlieBen), 
52554:Aruss. deza , klr. diza usw. „Teigmulde, Backdose“ ( *dhoigh-i-a ; Zubaty 
53846:und dheigh- „Lehm kneten". 
=== Bd2
40332:dheigh- „Lehm kneten'‘); tuige „stramen‘‘, imthuge „Bedeckung, Beklei- 
=== band3
3105:200". modrig sein4, «l- 162. munket qotlo~ 455. Mase he tmer- 272* Molus weg ere J- « G37. niaasjy geri- 421 Pag". risa. Mast mucdo-e 235% Mohrriibo | mpk- 313* noy® 340%, mitt klem 498. | Molken Nadel dhelg- 808 mourc- 223", | Monat mbvica- 271°. (von Pitanzen)  (Ha-} 430", | Morgenriie = aues- 2th. fig oua* Mauer 7. yer- 230. morsch worden ger- G1), Nodelbiume 2. el(ew)- 162. dhaigh $33. | morschon 1b. merg- 281%, | oiben dhergh- 803, MmAGern dheigh- 833. | mucksen s00*, apa- SLs" Maul wf- 200°, Micke sno. aR aud- (fd" Mauleszet mn A = eA | > JTL". ) nhhres 2, al. f $11", iniide werden 4. Bema") 2, Fer- 408 Maus gdi- G30 -  pl- 72" més 312*. | Mahe haben mi 258 Niisse Letap. 706 Meakern . ona" mihen refl, 2. ye 225 - wmely. 207" Moar jot = o ben 308 Nagel - 180 aes oq ma- 201" wet guréugh- WOT, Moh} ve 519, | Méinduny dus 168. nk B60". Mohilj bret) 13. pal. 6 ith*. miirrisch  l, agend- 55d", | nagendes Gewirm |. mal- meinen a 302", | muhen mi. 200°. a ee, tmclken &, o Mi. pi La welled el lial 4 =" a noerien pen 25". Peon) LL to HEME ore. Motall + fer- S00. Cl, Mr Oe ame Milbe pela‘ Milch mdg- 224", lad- 381", inih- 305", L. ee 439". sty 2. ei B07". Thane SM),
```


## [2026-09-04T18:38:21.232Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC dheigh\"; grep -n -i \"dheigh\\|dhoigh\\|dhiĝh\\|dhigh\" IEC.txt | head -30\necho \"=== SYN wall/dough\"; grep -n -i \"teichos\\|daēza\\|daeza\\|paradeisos\" SYN.txt | head -20"
}
```


### [2026-09-04T18:38:21.308Z] TOOL RESULT

```
=== IEC dheigh
2754:dheigh- ‘shape, earth up; form, wall (There is some confusion with dheig- above). WP I, 833. Cf. dhoigh- Skt. (ambig. prob. o-gde) dehah, am “shape, body’; Av. (pairi-) daezo ‘surrounding fence” beside diz- “earth up, cover’; LW in Arm. dez ‘mound’, dizem ‘pile up’; Gk. teikhos “outer wall, dam’; Ose. feíhüss, acc.pl. ‘walls’; Go. digan (z-gde) ‘shape, mould’; OPr. zeidis (metath. *wall') For Cz. dize ‘kneading- trough” and OHG teic, E dough, etc. see dhoiĉh-. The connexion, if any, with OE digan ‘overcome, survive, benefit’ is obscure
2889:dheuos, ios — dhighros
2905:dhighros ‘fixed, certain, right, true’. Cf. dhightos and dhiĝh- Go. *digrs, in digrei ‘abundance’; MHG tiger, tigre ‘entirely’; OFris. diger ‘true, exact’; ON digr, acc. s. digran ‘big, stout; Sw. diger, id.; Ir. déar, déaghair ‘precise, immediate, instant; (Radical probably in Ir. deagh-, cpds. ‘good’:
2908:dhightos, perh. a variant of dhighros in Li. diktas “hard, firm’; Latv. dikts “loud, strong, violent, rough?
2910:dhigh- (radical form of dhei$h-, q.v.) Skt. cf. su-dih ‘shapely’; Ober, dida “wall, fort"; Per. cf. diz-yale ‘citadel’; Gk. cf. ar-sikhos, ar-rikhos (&basket', if for *urs--^); Lat. cf. ef- figies, figulus, figlina (fr. dhig-) beside fingo, ere; Ir. perh. deagh- (cpds. "good" but cf. dhighros above); Go. digan ‘shape, knead’; (here also OHG tihton ‘compose’, MHG tiht, tihte “composition, poem accdg. to FK, though usu. refd. to Lat. dictare as a LW, cf. G Gedicht and E dight. Lat. figulus ‘potter’; figlina ‘pot seem to have an echo in OHG tégal ‘crucible’ ambig. cf. dheguhlo- in view of ON digull, pl. diglar, id. The Ger. wd. survives in Austro-G. Tegal ‘argil, potter's clay’. Cf. also Umb. ficla “cake or mash")
2913:dhiros ‘firm, sure’. Cf. dhighros. WP I, 857 Skt. dhirahb "lasting, steady, firm’; MIr. & Ir. dir “due, fit”, cf. direach ‘direct, straight, sure, exact, right, true’; W dir ‘certain’; (isophonic with Li. dýrinti ‘butt in")
2916:dhightos — dhmb-
2964:dhoigh-, see dheig-, dhig- (Lat. figo is ambig. cf. dhig-); Li. dáigau, yti, freq. ‘stab’; fact. ‘plant’; dáigas ‘shoot beside diegas, id.; Latv. diedzēju, v. ‘make sprouť
2965:dhoiĝhos, om, is, iə ‘shape, mould; shaper’. Cf. dheiĝh-. WP I, 833 Skt. dehah, -am “body, mass, person’; dehth ‘rampart; Av. -daeza, in pairi- ‘rampart’; LW in Arm. dez, gs dizi “pile, rick and par- tez ‘paradise’; Tokh. A tseke ‘plastic figure’; tsek-, B tsaik- ‘to shape’; Gk. toikhos “house- wall’; Myc. to(i)ko-, id.; Gothic daigs, OHG teic, OE dag ‘dough, mass: ON deg id., deigr ‘plastic’; Pol. dzieza, Slovak dieZa, Cz. diže ('kneading-trough'. Isophonic with OE dæge *bread-maker'; ON deigja "mad": Finn. LW taika *magic'; taikina *dough'; Li. (perh. by metath.?) žiedas (fring, thimble, blossom’. Semantics obscure). (W dull *form, shape? seems to represent a type *dhoighlio-)
6096:$hoidh- (2) (?). Cf. dheigh-, dhoigh-
10246:mag. (1) ‘smear; ointment’ Oss. mäz ‘ointment’; Arm. mac, adj. ‘glued, joined’; cf. macuk ‘paste, glue’; macan, adj. ‘slimy’; macun, gs. macno, i-st. ‘curd, clot; Gk. mágma, n. ‘ointment’ cf. also magū-daris, f. ‘gum-tree, benzoin’; maktron, n. ‘towe? and perhaps mas-tíkhë (“gum-mastic', cf. dhiĝh-); Ir. cf. mág-ach, adj. ‘fat, plump’; Icel. maka, v. ‘smear’; OCS (and com. Sl.) mazi, f. *oint- ment. mazo, mazati, v. ‘smear
=== SYN wall/dough
```


## [2026-09-04T18:38:25.798Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '52490,52570p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-04T18:38:25.861Z] TOOL RESULT

```
mit ei :oi:T nach Wiedemann, Praet. 28, vgl. auch Leskien Abl. 271 f. — Gr. 
thyydvca, &tyelv „anriihren ‘ (i !) aber kaum als „betupfen“ hierher (Fick 1 4 462 
zw.), sondern als „streichelnd betasten, wie knetend beriihren ££ zu dheigh- 
,.fingere ££ . — Uber lit. dagys „Kette“ s. u. *dhag- „wetzen“ und *deg- „paeken ££ . 

dheigh- ..Lelim kneten und damit mauern oder bestreicben (Mauer, Wall; 
Topferei; dann auch vonanderweitigem Bilden, Formen, Gestalten;; auch 
vom Teigkneten (Backerei) £ ; s. zum Sachlichen Meringer IF. 17, 147. 

Ai. dchmi „bestreiche, verkitte" (3. sg. degdhi statt *dedhi, ebenso Ptc. 
digdha-; s. auch Meillet IF. 18, 419 f.), deha m. n. .,Korper debt ..Wall, 
Damm, Aufwurf £ , av. pairi-daezayeiti „mauert ringsum ' (= ai. Kaus. dc- 
hayati) nzdista 3. sg. med. ..hat (einen Damm ■ errichtet", Ptc. uzdista-, 
uzdaeza- m. „Aufhaufung, Wall", pairidaezu- m. „Umfriedigung ■ (daraus 
- lagadeioog), ap. dida ,,Festung ££ (daraus und aus andern Nomina unsererWz. 
sucht Meillet Msl. 16, 3 1 5 f . ein Wznomen *dheigh, *dhi?j Ms zu erschlieBen), 
npers. diz, dez ds. Arm. dizanem (Aor. 3. sg. edez) „haufe auf"' (s. zum 
Praesenstypus Bruginann II 2 3, 3 1 5 f. m. Lit.), dizamin ,.hiiufe micli auf, 
sammle inich‘ £ , dez ,.Haufe“ (Hiibschmannn Arm. St. I 27, Arm. Gr. I 439), 
thrak. -dpog, -<5tfa (: ap. dida ) „Burg‘‘ (z. B. Kretschmer Einl. 230). Gr. 
xsTyo? n., toTyog m. (formell = ai. deha-) ..Mauer, Wand -1 ; {hyyava>, aor. 
diyeiv „mit der Hand beriihren' (Bed. wie lat . fingtre auch „streichelnd 
betasten“, Media g bereits ursprachlich aus der nasalierten Pi’aesensform 
nicht nach Meillet Msl. 7, 165 erst griech. vor dem Akzent; nicht zu *dheig- 
„stechen“). Lat. fngo , -ere, finxi, fictum ,,eine Masse gestalten, bilden, 
formen; erdichten; streichelnd betasten' 1 , figulus ,.Topfer“, plum ( *figslom ) 
„Gestalt“, effigies „(plastisches) Abbild £ , figitra „Bildung, Gestalt, Figur' , 
fictio ,,das Bilden, Formen; Bildung, Gestaltung, Erdichtung“, fictilis , aus 
Ton gebildet, irden, tonern £ (zum lat. g statt h s. Brugmann BSGW. 1895, 
36, Hoffmann BB. 26, 134, Herbig IF. 32, 71; nach letzterem stammt aus 
Formen wie fetus auch das k von altfalisk. fifiked „finxit‘ £ , osk. fifikus 
etwa „du wirst ausgedacht haben £ ); wahrscheinlich umbr. filda, ficlam ..fitil- 
lam, libum £ ', lat. ftilla ,.Opferbrei, Opfermus ‘ (wenn mit mdartl. t aus ct , 
s. Yf. FestgruB aus Innsbruck 1909, 97); osk. feihiiss ,.muros : (GraBmann 
KZ. 19, 310). 

Air. digen „fest“ (,,*festgeknetet, kompakt ,£ ; Marstrander ZfceltPh. 1910, 
413); ir. *com-uks-ding- ,.bauen, errichteiP in l.sg. cunutgim , 3.s g. conutuinc 
usw. und vielleicht auch dingim, fordingim „unterdriicke £ , s. u. *dengh- 
„wohin reichen ££ . 

Got. pamma digandin „dem Knetenden“, kasa digana „TongefaBe“, ga- 
digis (Konjektur fur gadikis „er/.daua } Gebilde“ (es - St., ahnlich reiyop) ; 



834 


dheu- 


daigs „Teig“, anord. deig (n.), ags. dag. ahd. teig ds.; anord. digr „dick, 
wohlbeleibt“ (Bed. wie ir. digen), got. digrei „Dichtheit, Menge“, mhd. 
tiger, tigere Adv. „vollig“, norw. mdartl. digna „dick werden“, diga „dicke, 
weiche Masse“ neben mnd. norw. diger; ahd. legal, anord. digull „Schmelz- 
topf, Tiegel w scheint ein echt germ. Wort zu sein, das aber in der Bed. 
das lat. tegula (aus rgyavov) aufgesogen hat (s. Pick III 4 205, Weigand- 
Hirt s. v., Falk-Torp u. digel). 

Lit. diezti , dyzti „priigeln u („*durchkneten, durchwalken, einem eine 
herunterschmieren)“, lett. diezet „aufschwatzen, anbieten“ („*anschmie- 
ren") ; 

Aruss. deza , klr. diza usw. „Teigmulde, Backdose“ ( *dhoigh-i-a ; Zubaty 
AfslPh. 16, 389, Berneker 198, Muhlenbaeh-Endzelin 1 487). 

Eine umgestellte Form ist wahrscheinlich lit. zicdliu, ziesti „formen“, aksl. 
zizdq, sbdati „bauen“, zveh, zixh „Mauer, Wand“ (Hirt BB. 24, 255). 
Curtius 5 182 f., Fick I 4 73, 232, 462, III 4 205f., Buga Kalba ir s. 184f., 
Eine Parallel wz. *dheig- sucht Wood Mod. Phil. 4, 490 f. (zw. auch Fick 
III 4 205) in mhd. tichen „schaffen usw. u , ags. dihtian „dictare‘ £1 ) ahd. tihton 
„erfinden und schaffen; dichten“ (aus spatlat. dictarel Falk-Torp u. digt 
laSt umgekehrt letzteres seine Bed. „yerfassen, komponieren, ausdenken“ 
aus dem Germ, bezogen haben); ganz fraglich. 

1. dheu- „laufen, rinnen“. 

Ai. dhavate „rennt, rinnt u , dehnstufig dhavati ds., dhauti - „Quelle, Bach“, 
ilhdra „Strom, GuBstrahl“ (wenn aus *dho[u]ra; von Fick I 3 115, Schulze 
KZ. 29 261, Bugge BB. 14,78 zu gr . dogog, ■frogw/uai, 'dgmaxco gestellt,
```


## [2026-09-04T18:38:34.941Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN teichos\"; grep -n \"τεῖχος\\|teixos\\|WALL\\b\" SYN.txt | head -20\necho \"=== SYN DOUGH\"; grep -n -i \"^.\\{0,80\\}DOUGH\" SYN.txt | head -10\necho \"=== SYN fingo\"; grep -n \"daēza\\|daeza\\|paradis\\|figura\" SYN.txt | head"
}
```


### [2026-09-04T18:38:36.718Z] TOOL RESULT

```
=== SYN teichos
11473:FLOOR WALL Roor FirEPLACE (Hearth) STovE CHIMNEY FURNITURE BED
11881:7.27 WALL (Of a Town; Partition Wall)
=== SYN DOUGH
2861:NE son doughter
2992:ME sonys sone, neveu (sonys doughter, etc.?) nece
6447:5. Lith. tesmuo, Lett. tesminis : Lith. tesia ‘swells up’, tesla ‘dough’, eto, Mihl.-Endz. 4.168. Leskien, Ablaut
9133:Pol. ciastko, fr. ciasto ‘dough’ (5.53), pl. ciasta ‘cakes’.
9144:2. Lat. massa ‘lump, mass, dough’ (> Sp. masa also ‘dough’), fr. Grk. pata ‘barley-cake’ (5.52). Ernout-M. 594. REW 5396.
9145:It., Sp. pasta, OF. paste (> ME paste), Fr. pdte, fr. late Lat. pasta ‘dough’, this fr. Grk. raoré ‘porridge’, neut. pl. of saorés ‘salted’ : racow ‘sprinkle’. REW 6272.
9154:7. Av. gunda- (NPers. gunda ‘lump of dough’), etym.? Barth. 525.
9158:NG fupéww, fr. class. Grk. fvpdw, de- nom. of {tun ‘leaven’, now ‘dough’ (5.52).
9162:It. impastare, fr. pasta ‘dough’ (5.53).
9164:Sp. amasar, denom. of masa ‘dough (5.52).
=== SYN fingo
83:Commonplace is the figurative use of words like head, foot, mouth, without reference to parts of the body. Such use is, of course, not a rhetorical or poetical device, except in unfamiliar and hence striking figures, but a feature of ordinary speech everywhere.
525:figurative(ly)
1803:The compounds are of obvious make- up, and too numerous to be cited in full (cf. NE thunder-stone, now obs.). Most of them are now poetical or figurative. The tendency is also to use the words for ‘lightning’ instead of those for ‘thunder’, which were more common in the earlier periods. Cf. NE struck by lightning (or NHG von blitz getroffen), though NE thunder was used in this sense down through the eighteenth century and poetically in the nineteenth (cf. NED S.v.).
1860:Most of the words for ‘shade’ are used also, without differentiation, for the image cast, the ‘shadow’. The figura- tive use for ‘disembodied spirit’ is also widespread from Homer on.
2103:1. IE *dhimo-, fr. the root seen in Skt. dhi- ‘shake, agitate’, Grk. diw ‘rush, rage’, bea ‘storm’, etc. Most of the words belonging here are used for ‘vapor, steam’ as well as ‘smoke’, while Grk. §ouds is used only in the figurative sense (mental agitation) ‘spirit, passion’, etc. Walde-P. 1.835f. Ernout-M. 399. Walde-H. 1.561 f.
2165:Hence Rum. arde, the common word for ‘burn’, both a and b, while It. ardere and Sp. arder are mostly used in figura- tive sense.
5268:There is frequent shift of application between words for parts of the body that are adjacent, of similar relative position, associated in function, or through common figurative uses with reference to the emotions. So between ‘head’—‘horn’ (from ‘summit’); ‘head’— ‘skull’—‘brain’; ‘mouth’—‘jaw’, ‘throat’, ‘cheek’, ‘chin’, ‘lip’; ‘neck’—‘throat’; ‘shoulder’—‘shoulderblade’—back’—“‘arm’ ; ‘hand’—‘arm’; ‘foot’—‘leg’; ‘finger’—‘toe’ ; ‘belly’—‘womb’; ‘breast’ as front of the chest—‘woman’s breasts’; ‘heart’ from ‘soul’ (Rum. inimd, 4.44) or ‘bowels’ (W. calon, 4.44).
5705:The majority of the words for ‘eye- prow’ belong to an inherited group. Of the others, some are based on the notion of ‘covering’, and some are compounds of words for ‘eye’ and ‘on, upon’. There ‘s some interchange of ‘eyebrow’ with ‘eyelid’ or ‘eyelash’, and even ‘forehead’ (NE brow). Several show the figurative sense seen in NE brow of a hull.
6473:2. Rum. znimd, fr. Lat. anima ‘soul’, with shift through common figurative uses of ‘soul’ and ‘heart’. REW 475.
6474:3. W., Corn., MBr. calon, Br. kalon, loanword fr. a form like OFr. cauldun, chaudun ‘bowels’ (deriv. of Lat. caldus ‘warm’), with shift through common figurative uses of ‘bowels’ and ‘heart’. Pedersen 1.147.
```


## [2026-09-04T18:38:39.752Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11881,11935p' SYN.txt\necho \"===== 5.53 dough section\"\ngrep -n \"5\\.53\" SYN.txt | head -10"
}
```


### [2026-09-04T18:38:39.818Z] TOOL RESULT

```
7.27 WALL (Of a Town; Partition Wall)
Grk. _—_retxos} rotxos, retxlov Goth. -waddjus Lith. miras; stena NG TotxXos ON mirr; veggr Lett. miiris; siena Lat. mitrus, moenia (pl.); Dan. mur; vag Chl. zidit, sléna paries Sw. mur; vdgg SCr. id, stijena It. muro; parele OE weall; wag Boh. zed’; sténa Fr. mur, muraille ME wall (waw) Pol. mur; Sciana Sp. muro; pared NE wall Russ. stena Rum. id; pdrete Du. muur; wand Skt. dehi-, prakdara-; ky- Ir. mur; fraig OHG mira; want dya~ NIr. muir; falla (fraigh) MHG mir(e); want Av. uzdaézi- W. mur, gwal, magwyr; NHG mauer; wand pared Br. moger
While the notion of the outer ‘wall’ of 8 town, fortress, etc. does not properly belong in this chapter, it must be con- sidered in connection with the partition
‘wall’ of a house, which may be ex- pressed by the same word, asin NE wall.
Where there is a distinctive word for the partition ‘wall’, like NHG wand, this is separated in the table by a preceding semicolon. But even in several of these cases, the distinction is not rigorous, and the word preceding the semicolon may also be used for the partition wall, e.g. OE weall, which glosses both Lat. mirus and Lat. pariés. For the outside wall of a house there is the greatest fluctua- tion, e.g. Lat. pariés, less commonly miurus, but It. muro, not parete,
Most of the words for ‘wall’ reflect in their origin some Special type of con- struction.
1. Grk. retxos (o- stem), totxos (o- stem; both forms and uses merged in NG rotxos) : Ose. acc. pl. fethtiss ‘walls’, Skt. (Ved.) dehi- ‘wall, mound’, OPers, didd- ‘fortress’, Av. uzdaézi- ‘wall’, Toch. A tseke ‘piece of sculpture’, fr,
JE *dheigh- in Skt. dih- ‘smear’, Lat, Jingere ‘mold’, etc. (9.72). Here also prob., with metathesis, ChSl. zidati ‘build’, zidi, zid& ‘wall’, SCr. zid (> Rum. 27d), Boh. zed’, etc. (also OPruss. seydis ‘wall’). Walde-P. 1.833 ff. Walde- H. 1.501 f.
2. Lat. mirus (early moerus) and moenia (pl.) : Skt. mé- ‘fix, build’, etc. Walde-P. 2.239f. Ernout-M. 624 ley 645 (without etym.).
From Lat. mirus come It., Sp. muro, Fr. mur, muraille; Ir. mir, W. mur; ON mirr, Dan., Sw. mur; OE mar (rare), MLG mire (> Lith. miras, Lett. maris, Pol. mur), Du. muur, OHG mira, MHG mir(e), NHG mauer.
Lat. pariés, etym. dub., perh. : Lith. tora ‘fence’, vb. tverti ‘grasp, form’, ete. ; or: ChSl. podt-pora ‘a prop’, za-préti ‘shut’, OHG sparro ‘beam’, etc., and so orig. the supporting struts of a wall. Walde-P. 1.750f., 2.655 f. Ernout-M. 734.
Hence It. parete (Fr. paroi not com- mon; generally mur), Sp. pared, Rum. parete, W. pared.
DWELLI
‘panel, side ‘enclosure’, a ’ shut in or out’, etc.
erseD 1. Br. moger,
, 1’, Pedersen
fr. Lat. macerta 1.199. Loth,
dij (grunduwaddjus addjus ‘town wall’),
" tton?, paurgsw voundation’, baurg Beg OF wi,
irene Lat. pincire ‘bind’, So orig, & W: Walde-P. 1.224.
Feist 538 f. ‘OE weall, ME, NE wall, OF ris., Os,
MLG wal (> Du. wal, Sw. vall, NHG yall ‘rampart, embankment’), fr. Lat. rallum ‘wall of palisades’, coll. of vallus
Falk-Torp. 1400.
NG, HOUSE, FURNITURE
Digitized by Arya Samaj Foundation Chennai and eGangotri
473
‘stake, palisade’ : Goth. walus ‘staff’, Grk. #dos ‘nail’, etc. Walde-P. 1.301. NED s.v. wall, sb.}.
OHG, MHG want, NHG, Du. wand : Goth. wandus, Dan. vaand ‘rod’ (ME, NE wand fr. Norse), fr. the root of Goth., OE windan ‘turn, wind, plait’. So orig. a wall of wattle-work, like ON veggr, etc., above. Falk-Torp 1339, 1382. Walde-P. 1.261.
5. Lith., Lett. stena : Lith. sieti, Lett. siet ‘bind’, Skt. sd-, si- ‘bind’, etc. Walde-P. 2.463 ff.
6. ChSl. zidt, etc., above, 1.
ChSI. sténa, etc., general Slavic : Goth. stains ‘stone’, etc. Walde-P. 2.611. Traut- mann 281. Otherwise Briickner 529.
7. Skt. dehi-, Av. uzdaézi-, above, 1.
Skt. prakdra-, epd. of pra- ‘in front’ and dkdra- ‘form, shape’, fr. a-kr- ‘make’.
Skt. kudya-, etym.? Uhlenbeck 57.
7.28 ROOF Grk. (a)réyos, oréyn, dpod7 Goth. hrot Lith. stogas NG oréyn, axe ON pak (hrot) Lett. jumis Int, — téclum Dan. tag ChSl.  krovit, strécha re lello Sw. tak SCr. _ krov ri i OE pac, hrof Boh. _ strecha, krov a i 0, techado ME rofe Pol. dach, strzecha ih (urge) ue roof Russ. krysa Nit. eeann OHG dan renew pore MHG dach NHG dach Most of the words for ‘roof’ are from | Ir. tuige ‘straw, thatch’ and prob. used
eenmting ‘cover’ (12.26). But a wh a 4 Special material or type of 2 ake and Conversely a general word Special 4 may become restricted to a
eee os NE thatch. hag., atk “(eg ‘cover’, in Skt, Walde-p oreo, Lat. tegere, ete Pedersen 1 4 Emout-M 10 ) 97, Sete
Tk, ore ;
It tate, “pe Cue1t Lat. tectum * tou, Sp. techo, techado) ;
for the ‘thatched roof’, W. to, Br. to; ON pak, Dan. tag, Sw. tak, OE fac (NE thatch), Du. dak, OHG dah, MHG, NHG dach (> Pol. dach); Lith. stogas, OPruss. stogis.
2. Grk. dpo¢7 (so, not oréyn, in Hom. and early Att. inscriptions IG 17.373 and 374; cf. also at Epidaurus dpoda IG 4?.1.106.46, 106. IT. 186 f., vs. oréya ib. 102.293) : gpégw, tpémrw ‘cover with a
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
474
roof’, OHG hirni-reba ‘skull’, OHG rip- pa, OF ribb ‘rib’, etc. Walde-P. 2.371.
NG oxern (or oxérn) ‘cover, shelter’, also used for ‘roof’.
3. Rum. acoperis, fr. acoperi ‘cover’, Lat. coopertre ‘cover’.
4, NIr. ceann ‘head’ (4.20), ‘top’ and ‘roof’.
5. Goth. Arot, ON poet. hrot : OF, OS hrést ‘framework of the roof’, NE roost (in Sc. ‘inner roof of a cottage’, cf. NED s.v., 3), MHG raz ‘funeral pile’, ChSl. krada ‘funeral pile’, root connec- tion? Walde-P. 1.485f. Feist 270 f.
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
‘boat-shed’, MLG réf, Du. roef ‘deck. house’, further connections (Myr. cra ‘stall, hovel’, etc., Pedersen 1.92) dub Walde-P. 1.477. Falk-Torp 917, :
6. Lett. jumts, fr. jumt ‘cover’ connection? Mihl.-Endz. 2.119.
ChSl. krovii, SCr., Boh. krov, Russ, kryga : ChSI. kryti ‘cover, hide’, Berne. ker 632.
ChSl. strécha (Supr.), Boh. sliecha Pol. strzecha (SCr. streha ‘gutter’) i ChSl. strojiti ‘prepare’, Russ, stroit! ‘build’, ete. (9.44). Briickner 529,
7. Skt. chadis-, fr. chad- ‘cover’,
===== 5.53 dough section
9133:Pol. ciastko, fr. ciasto ‘dough’ (5.53), pl. ciasta ‘cakes’.
9138:SY,), : ia 77. Gamillscheg s.v. | er the sacred ‘cake’ : Skt. dravinas- ‘wealth, property’. Barth. 770. Crk ; 5.53 DOUGH ao. Goth. dai Shun, tondpr ON, daigs Lith. minklé, te3la * massa D deig Lett. mikla roe rag dej ChSI.  tésto is é On deg SCr. _tijesto gee masa ME oe Boh.  tésto in : logh, paste Pol. _—_ciasto ais NE dough R test - Du ee fe OHG ti Brodie toae MHG teig pe NHG leig
9150:5. Lith. minklé (NSB), Lett. mika ; Lith. minkytz, Lett. micit ‘knead’ (5.53)
9162:It. impastare, fr. pasta ‘dough’ (5.53).
14559:; SEES Shalt sh out’), SCr. pritisnuti, pritiskivati, Boh lisknoutt (tisniti ‘oppress’), Pol, (ciskag ‘throw’) cisnqé, scisnaé, Russ, (but not the usual words for ‘press’) liskat', tis. nut’, prob. fr. the same root as Chs] tésto, etc. ‘dough’ (5.53). Walde-p 1.702.
25856:15.53 SteuT (subj.)
26327:15.53
```


## [2026-09-04T18:38:43.575Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9139,9152p' SYN.txt"
}
```


### [2026-09-04T18:38:43.633Z] TOOL RESULT

```
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
360
1. Grk. ¢upaua, fr. dipdw, dbpw ‘mix’ : Skt. bhur- ‘move rapidly’, Lat. fervére ‘boil’, etc. Walde-P. 2.157.
NG fun, funépr, fr. class. Grk. téun ‘eaven’ : Lat. dus, Skt. yisd- ‘soup’, etc. (5.64).
2. Lat. massa ‘lump, mass, dough’ (> Sp. masa also ‘dough’), fr. Grk. pata ‘barley-cake’ (5.52). Ernout-M. 594. REW 5396.
It., Sp. pasta, OF. paste (> ME paste), Fr. pdte, fr. late Lat. pasta ‘dough’, this fr. Grk. raoré ‘porridge’, neut. pl. of saorés ‘salted’ : racow ‘sprinkle’. REW 6272.
Rum. aluat fr. Lat. allevatum ‘raised, leavened’, pple. of levare ‘lighten, raise’ (cf. NE leaven), denom. of levis ‘light’. REW 360.
SELECTED INDO-EUROPEAN SYNONYMS
3. Ir. idis, NIr. taos, W. toes, Br, ChSI. tésto, ete., general Slavic also Lith. tesla) : OHG theismo, deismo OE p@sma ‘leaven’, prob. fr. the root of ChSI. tajati, Grk. TKO Melt}, ete Walde-P. 1.702. Pedersen 1.56.
4. Goth. daigs, OE dag, ete., gen. eral Gme. : Goth. digan ‘mold, form’ Lat. fingere ‘mold’, Skt. djh- ‘smear’ (‘fashion, form’ implied by dehi- ‘wall’ like Grk. retxos ‘wall’), IE *dheigh-. Walde-P. 1.833 ff. Feist 118 f.
5. Lith. minklé (NSB), Lett. mika ; Lith. minkytz, Lett. micit ‘knead’ (5.53)
6. ChSI. désto, etc.., above, 3.
toaz,
```


## [2026-09-04T18:38:47.905Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT daeza\"; grep -n \"daēza\\|daeza\\|dae'za\\|daèza\" BRT.txt | head -30"
}
```


### [2026-09-04T18:38:47.969Z] TOOL RESULT

```
=== BRT daeza
8636:•  j.  uz-daeza-  m.  i)  'Aufschütten  von Erde,  Aufmauerung' :  yat . .  paili  . .  daxma -za  kiryeinte  "wo  Leichenstätten  durch Erdaufechüttung  errichtet  werden"  V.j.9 —  y^t  ■  ■  P"'''  •  •  daxma  "-ta'l  *2'7kante
8642:•  j.  uz-daezay-  m.  'Wall,  Damm,  Mauer': yd  aetpm  uzdaizsm   uzdista  yeähh  vB  aSsB
9144:adam  akunavam  iitamaiy  tya""  piiä I  akiiriaui'^^,  tya'paliy  kartam  7'ainatair \mubam  (sd.)  ara"  visam  vasna  af'ura''- mazdä/ia''  akumilX.i.y, — lyi^'iam  hacüma'' a'^ahya"  ava  akunai'o"  D.  6".  3;  Bh.  ;.  7 (wo  *akunai'ara"t,iy\  D.6.4  (wo  akuna- Td'tä)  II  ;  —  yat  b.i  paiti  frac'tjm daxnia    uzdaeza   (sd.)    kiryänte^^    V._j.  9;
15604:•  j.pairi.daeza-m.,Plur.'einerings-,rundura gehende,  sich  zusamuienschliessende  Um- wallung, Ummauerung':  aSa^a  hl  aiie  ySi maxäayains  aiAhä  z»mö  'tan  pairi.dal- sayqn  V.^j.  18.
```


## [2026-09-04T18:38:54.157Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15598,15612p' BRT.txt\necho \"----8630\"\nsed -n '8630,8650p' BRT.txt\necho \"=== grep diz\"; grep -n \"diz-\\|dizh\\|1daez\\|dae'z\" BRT.txt | head -20"
}
```


### [2026-09-04T18:38:54.254Z] TOOL RESULT

```
Zum  V,  fras:  —  Vgl  ai.  fraiam  {prdlipräia jahi;  Bloumfield  5BE.  42.  305),  mp.  äfräs, paiifräs.    —    Vä.:  hal fräi  ptrsakVt.    —    •)  S.
8(?J.
•l  ö  pti;    daiu    i
^  nodeutlichc
•  j.  '^pairi.ta£ahi '>  Inl  'im  Lauf  zu  um- kreisen, zu  umlaufen',  mit  Akk.:  yaval alte  späna  bis  hapta  nmana  f  havqn  \ 'Sobald  die  Hunde  zweimal  sieben  Häuser umlaufen  können"  V.  25. 45.
Zam  V.  tak-,  —  iSynt.  s.  IF.  lO.  193,  —  Pü. : perämen  api  laxlär  hinä.  —  ')  NA.  getrennt.
•  j.pairi.daeza-m.,Plur.'einerings-,rundura gehende,  sich  zusamuienschliessende  Um- wallung, Ummauerung':  aSa^a  hl  aiie  ySi maxäayains  aiAhä  z»mö  'tan  pairi.dal- sayqn  V.^j.  18.
np.  päliz  'Garlen'  [  vgl.  gr.  LW.  iib^!*«o(.  — Pü.  i  pa  pirivtSn  daMimh.
•  j.  pairLdahyav-  Adj,  (auch  mask.)  'der vor  dem  Land  ist':  mi^nm  °yüm  (ASm.) . .  aipiJaRyüm  Yt.  10. 144.
Npfi. :  a  pB  i  Aar  lahr  asl.
•  j.  pairid'wa-  Adj.  'um  was  man  herum- gehen, dem  man  ausweichen,  was  man vermeiden  kann'":  '"hwS  iavaili  panta yim  . .  päiH  . .  hä  dit  aivB  afairihws .  . "vitari  potest  via  quam  . ."  Aog.  77.
Kampfe.— Komp.-.pam+'Awa-, —  tä.-.viiarai- emaiidiM,  Sü.i  parikramariTyah.  —  '>  Falsch Wilhelm  ZDMG.  4^-  96.  vgl.  apairüaya-.
•  j.  pairi^sm  Adv.  'um  und  um,  ganz und  gar':  pairika  yä  duiyairya  vispahe atfA3uI  astvats  parsii  p"  ar?hvqm  ava.- Msflyai  (sd.)  "die  F.  des  Misswachses würde  die  Lebenskraft  der  ganzen  körper- lichen Welt  gani  und  gar  entzwei  spalten" ■ytÄ54;    —    ava    ml  Stil  .  .  paröit  p'
BARTMOLOHAa>  Altiiin.  Wb.
zAusdr. /ro/o-  No.  i
----8630
•  j.  uz-gKi-Bwä-  'Erhebung  (der  Arme), Ausholung  (zum  Schlag)':  'Tiiyilt  pars biizuwe  "(noch)  vor  der  Ausholung  mit den  Armen"  Yt. /_j.  46,
Zum  V.  giali-;  »gl.  giniifin.
•  j.  yai  "uzgtr^snävayö  *niva»A3nii N.f,4.
Vä.:  ösän  kc  fa  i;irt  TUfdiin  ape  diafend' (tfarak  sniarak  .  .  viiiyötmäh  räiijKiii  ..  d.  i. "die  mit  dem  baaschigen  (Kleidungsstück) sich  bekleiden.  A.  (versteht  darunter)  d: lieind,  M.  die  Hose".  Es  ist  :rw..i«  .  .  ; lesen;  Schluss  unklar.    Vgl.  ÜTtll-  IF.  IO.  S.
•  j.  *uz-gr«mbayant-    Adj.,    PPA: grab:
g.  uyhi  Y.  46.   13:  S.  S"»!--
•  j.  uz-daeza-  m.  i)  'Aufschütten  von Erde,  Aufmauerung' :  yat . .  paili  . .  daxma -za  kiryeinte  "wo  Leichenstätten  durch Erdaufechüttung  errichtet  werden"  V.j.9 —  y^t  ■  ■  P"'''  •  •  daxma  "-ta'l  *2'7kante
iizbaodah-  412
(sd.)  V.J.13;  —   aaaih'a  daxmaih-a  .  .
ySi   .  .    bavaitiH  (sd.)    'sa   usdista'^'^  V.  7. 3)  'Wall,  Damm,  Mauer':  yesüa
alsa   gaowa  °zaSh>a  Jrajasät  . .  yS  altern
•Z)m  utäiSta  (sd.)  V. /5.3  s  f. Zum  V.  datz..  —  ai,  vgl.  uddriikä-  f.  'Ter- mite'. —  Pü,i  uidakisi.  —  ')  Ao  V.  3.  9  an- geglichen, statt  Tfldaeia  'durch  Erdabi  ragung'. —  '1  ^g.  'welche  durch  Erdauficbüttang  auf- geschüttet werden';  s.  zAusdr.  yr-ii^ii-  No.  1.
•  j.  uz-daezay-  m.  'Wall,  Damm,  Mauer': yd  aetpm  uzdaizsm   uzdista  yeähh  vB  aSsB
■zi/  a»kat  V,  /5.36  ". S.  EU  iiidaäa-.  —  ')  iSL  e.  unter  us/rSMätiay-.
I   j.    uz-daöhav-,    *uz-dahyav- '>    Adj. (auch  mask.)   'ausserhalb  des  Lands  be- findlich'; a)  'ausländisch':  ädahyunqmta .. 'yunqmüa  (GPm.)  frava^ayS  Y.  2O.  9,  Vr, 16.2.        b)  'ausser  Land  führend';  *xsa- yäe  . .  *'aÄua/  (lSm.)'>  pa^a  AaxlüiJ  {sd.) N.p. Pü.  (w  a):   »M'/i7^,  (lu  b):  /W  u-^/;hltrk.  — ')  NA.  u:diihy-',  s.  aber  J  i,  K  $,  K  7  a  und ädahy.  —  ')  Hd».  daauhulii,  %  löS.  30.
•  j.  uz-daraza-  m.  'Herausfassen,  -ziehen, holen':  .  .  frasaocaySAHsA.)  .  .yat  [;'.;]''
aa^m  äirjm  °za  aslayä  un^araya  atarJ- cdr?^  vTi'a  baröi^  vica  iävaysil  "indem man  das  Feuer  durch  Herausziehen  des lirennmaterials  zerteilt  und  zerstreut"  V. ■^■75.
Pü.:    hanibasf->.     —    J>  Zu  streichen;    s.  die Var.  —  ')  Wie  für  das  folgende  handar/iia.
•  j,  uz-däna-  n.  'Aufrichtung,  Aufbau', um  etwas  drauf  zu  setzen  oder  zu  legen; a)  'Unterbau',  um  den  Kochtopf  drauf zu  stellen'':  apa  aSsiit  ^iism  baray?n  V. 8.  74.  b)  'Aufbau'  zur  Aufnahme  der Gebeine  des  Toten":  *°tut/i"  hl  a'a.Jf kjrmaot  upairi  (sd.)  spämm  .  .  *anaiwi.- värsntJm  (sd.)  . .  "einen  Aufbau  soll  man dann  dafür  (für  die  Gebeine)  errichten . ." V.  6. 50,
"*)  Vgl.  über  die  Ossuarien  der  Parscn  Ger. OK.  370,  JlvAHjl  JAnthrSBombay  1888  'An  old Persian  coffin',  DsT.ZA.2.93,  C^SARTEr.Li  BSOK. i8go.  7.
Pü.:  u:^!tihisl,  (luV.  ö)eri.:  ni/m/J« 'Knochen-
=== grep diz
```


## [2026-09-04T18:39:02.145Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"daez\\|daéz\\|dai z\" BRT.txt | head -40"
}
```


### [2026-09-04T18:39:02.222Z] TOOL RESULT

```
8636:•  j.  uz-daeza-  m.  i)  'Aufschütten  von Erde,  Aufmauerung' :  yat . .  paili  . .  daxma -za  kiryeinte  "wo  Leichenstätten  durch Erdaufechüttung  errichtet  werden"  V.j.9 —  y^t  ■  ■  P"'''  •  •  daxma  "-ta'l  *2'7kante
8642:•  j.  uz-daezay-  m.  'Wall,  Damm,  Mauer': yd  aetpm  uzdaizsm   uzdista  yeähh  vB  aSsB
9144:adam  akunavam  iitamaiy  tya""  piiä I  akiiriaui'^^,  tya'paliy  kartam  7'ainatair \mubam  (sd.)  ara"  visam  vasna  af'ura''- mazdä/ia''  akumilX.i.y, — lyi^'iam  hacüma'' a'^ahya"  ava  akunai'o"  D.  6".  3;  Bh.  ;.  7 (wo  *akunai'ara"t,iy\  D.6.4  (wo  akuna- Td'tä)  II  ;  —  yat  b.i  paiti  frac'tjm daxnia    uzdaeza   (sd.)    kiryänte^^    V._j.  9;
9983:mit  «f  i)  '(eine  Waffe)  niederschlagen, -schmettern  auf—'  {paiti  mit  Lok.):  ks (näml.  mi'hro)..gmqm(%A^  nijainti  aspaSta paiti  vTraii'a  Yt.  10.101,  3)  'nieder-, zu  Boden  schlagen,  er-,  entzweischlagen': yatcit  tdastaire  hindvd  (sd.)  ^ifgiurvayaiti yatcit  daosataire  niyne  (3SPM.)  Y.  57. 29;  —  %wqmca  drupmca  «»'/«« (iSPM,?) Yt.  4-5!  —  yalba  azim  nijanäni  dva 'irisva  .  .  daez'anqm  Yt  5.  22;  9.  22, 31^,  15.  3;  —  yat  niE  avavat  daljia- yasiianqm  nijattm  ya%a  ..  Yt^.  77; —  para  akmät  yat  .  .  aiimaoyB  . . *'ka%ra.jatö  nijanSite'^  V.5.  56;  y.  55;  — yö  .  .  stija  nijainti  kam^rT^l . .  na2',a.cim ymqm  sadayeiti  yavata  alm  nijainti  m>r>- zuca..  Yt,/o.7ij — yat  *n5  nsit  ni/anüt'^ ars'a  ..  Yt/5.  32;—  nij'ann'ctiS.)  buye vTspe  dusmainyü  K.i.\\;  —  yai:a  aspm aom  spähm  nijanäni  yö  .  .  Yt.  14.  58;  5. 54,  58;  —  mit  Dat  incomm. :  kahmäi  .. fraiaintim  kdi:ra.jata  (sd.)  nijanäni  Yt. 10. 110.  a)  sva.  'zerstören,  zu  Grunde richten';    l0   vispe   v^rfioinqm    vanat  nl
12541:•  '}.  daez-  V.  'häufen,  schichten'  (Erde, Steine);  nur  mit  Praev,  Praes.  i  du-, 30  (Iter.)  da&aya-.  —  PPfP.  'dis'ta-'-\
13624:Zum  V.  daez:  —  np.  da ;  ai.  »gl.  dehi-  f. 'Wall'.
15604:•  j.pairi.daeza-m.,Plur.'einerings-,rundura gehende,  sich  zusamuienschliessende  Um- wallung, Ummauerung':  aSa^a  hl  aiie  ySi maxäayains  aiAhä  z»mö  'tan  pairi.dal- sayqn  V.^j.  18.
```


## [2026-09-04T18:39:05.280Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12536,12550p' BRT.txt\necho \"---13615\"\nsed -n '13612,13630p' BRT.txt"
}
```


### [2026-09-04T18:39:05.351Z] TOOL RESULT

```
mit  frä  dnwS.  3 :  koAmäi  fradasayö dalnam  V.  2.  i ;  —  ahmäi  fradalsaim  dag- nam  V.  2. 2;  —  aet?m  mq%nm  ma  fra- daesaysi^  ainyal  pihre  va  .  .  Yt.  14.  4Ö*'. mit  harn  Med.  'sich  weisen  lassen  in  — (Akk.),  sich  etwas  gesagt  sein  lassen': inja  avat  AandalsayaauÄa  .  .  yai  . .  "zu- rück !  lass  dir  das  gesagt  sein,  . . :  wenn . .'' Yt.ig.^8;  50.
ai,  äiiäti,  dldiiai,  diiyaii,  äeiayaä,  adii^i; woss.  äwdttu«.  —  PQ.  (lu  \.43,  Vi.  //,  V.  2, tS,  F.  14) :  nimütan ;  {in  V.  5,  p,  P.  38,  Y.  S) : nikeaian,  (tu  Y.  S)  erl. :  ftäiä*  ape  kartan  %  s. «och  No.  »f.  —  '>  Hds.  daev'.  —  »)  PB.: doMe,  Sa.:  diHL~il  Pfl.:  daAäl,  Sä.:  d^hi. 4)  NäinL  seinei  Tochler  znr  Ehe.  Pü.i niiebin  HÜeiil,  etl. :  iuia  dtal  ianih  afie  dahil. S.  anch  Dk.  g.  44.  17.  —  5)  Zu  S  S^S- ')  Vgl.  Yt.  4.  9,  wo  fradaxscQiö.
•  j.  daesa-  m.  'Zeichen,  Otnea':  pattiHatSe ayanqmca    :^a/nanqm    ayanqmca
VL/J.  104-
Zum  V.  dais-,  —  ai.  deli-  m.  'Gegend';  nip. uidfs  'Gätzenbild',  np.  'des  'ähnlich';  s.  dazu HOKN  GIrPb.  /  b.  35.
•  '}.  daez-  V.  'häufen,  schichten'  (Erde, Steine);  nur  mit  Praev,  Praes.  i  du-, 30  (Iter.)  da&aya-.  —  PPfP.  'dis'ta-'-\
mit  US  -aufhäufen,  -schichten,  -dämmen,
■mauern':  yS  latitn  utäalum  utdiäa'^ (3SPrM.)  "wer  diesen  Damm  (Mauer)  er- richtet haf  V. /5,  36;  —  affaXiva  dax- W  . .  ysi  bavairiti  (sd)  usdagia  us- dista'^  (NPm.)  V.7.S4.
mit  pairi  'rings-,  rundum  aufdämmen, mauern':  altera  he  alte  masdayasna  ai^ha e^rnH  pairi.dalxan  (sd)  pairi.datzayan  V. 3.  18.
Ar.  "dhailh-  {ygl.  oA. /eiAkss);  ai.  dlgdhi*^: diAänIi;  digdAäk').  —  Pii.:  umschreibt  mit däian  oder  kattan.  —  ')  S  5J  n.  —  »)  Mit inalogischem  gdh,  Sp.  413  n.
j.  daiza-  m.   "Häufen,   Schichten'  von Erde,  Steinen. KompE.  —  Zum  V.  dan-,  —  np,  dcz  "Burg', gr.  «rxoe  'Mauer',   osk.  /eihius  (AP.)   'WafP; ü.  deka-  m.  'Körper'.
j.  daoi^ri-  'Spruch,  Rede'uzw.  i/nji/ischer
Wesen,    nur  mit  aya-  Adj.:   frattrase  .  .
ayqm  °rTm  daomnl  Yt  jp.  57;  —    arfqm
■rfm  daunta  daiva  V,  ig.  45.
---13615
mp,  Praes.  {aft)  dandel  'er  ve^isst'  N.  //> (Fol.  ig.  21,  10.  7),  Vr.  2.  8  (Sp-),  Y.  /p.  12 (Sp.).  54. 21  ISp.).  dand'  (wenn  richtig  gelesen -  West  SBE.  37.  455  'i=st  yang-  -)  würde ein  taa.'dam'  venreteui   s.  dazu  %62.  I  No.
•  g.  da^h-  V.  'lehren'.     Praes.  5  dldah-. Med.  in  pass.  Sinn  'von  Jemand  (Instr.)
belehrt,  unterwiesen  werden  in —'  (Instr.): hyat  xsma  u.v',ais  dldaitiAl  (iSPrM.)'> paourvTm  "als  ich  zuerst  von  euch  in euren    Sprüchen    unterwiesen   wurde"  Y.
Vgl.  tdahma-,  dqjfi-ä-,  daora-,  daakak-.  —  gr. *ß«  (USW.);  Litt  IF-  7.  108  No.  I.  —  Pü.: ka  imäk  sax^an  pa  niiiähi  niktzilfratum,  erl.: dSfi.  —  OS  368.  ig;  ihem.
•  j.  dahiäta-  Adj.  'der  (in  Sachen  der Religion)  bestunterrichtete,  sachverstän- digste, im  Ritual  bewandertste';  zao/a  {sd.) anahaxtö  .  .  'tili  ars.vacasi>mäi  zao^rpm ragxiaiii  N.  Ä»;  —  srag^ävamim  ..  °tim *arl.vaca$fytn»m  Vr.j.  i;  —  °ta  (als  AP.) arLvacashma  A.,5.4;  —  saosyantascä  °iq ^ars-vaüastima  Y.  y.  3,  Vr._j.  5  (wo  'fS); —  *'laisva  Yyt.42''>.
SuperL  lu  'daAma-,  —  ai.  dämsiftha-  Adj.  — Pü.:  däaäklum.  Sä.:  jnära/am'ai.  —  »  Hds, daiiA:
•  p.  dita-  Adj.,  PPP.;  s.  tyä-.
g.  dldailihF:  s.  dqh-.
•  g.  didant-  Adj.,  PPA.:  s.  "daiy)-.
•  j.  diJayant-  Adj.,  PPA.;  s.  'ds[y)-.
Wohl  fax  *diliyanl.,  %  268.  IIb;  i.daiiyaat-.
•  p.  didä-  f.  'befestigter  Ort,  Festung; Burg':  tigra^  nämä"  'ds  armamyaiy  Bh. 2,  8 ;  9,  /.  1 3,  _J.  9,  1 1 ;  —  avaiy  kagma- iänaiy  t^tar  °dätn  fr3ha''jam  ".  .  in  der Burg  zu  Hagiii"  Bh. 2. 13.
Zum  V.  daez:  —  np.  da ;  ai.  »gl.  dehi-  f. 'Wall'.
•  j.  didrazva-  Adj.  'sich  (fest)klammemd
an  — '  (Akk.);  mäca  .  .  astvatake  atthsus 'vö  plsa  (sd.)  manaklm  faüi.raixslsa  P, 40;  40.
Zum  V.  dar>:>.   red.  Bildung");  S  ^68.  39.  — Pü.:  o.  —  1)  Ähnliche  Bildungen  des  Ai.  bei Wh.  Gr.*  S  ^f/O,  1193. p.  didiy:  s.  'anter  'dä(y).,
•  j.  dit  Part  der  Hervorhebung:  fairi^wO bavaiti  patttä  yim  äänul  päiü  .  .  h&  d° aivö  apairihwö  ys  vayaos  Ko%.']-]\-]8—8i*.
ASn.  aus  day-,  —  Vgl.  dim.  —  Pü. :  laut  das    1.  St  aus.
dby  Google
```


## [2026-09-04T18:39:16.353Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 12541 13624 15604 8636; do echo \"== around $L\"; awk -v l=$L 'NR>=l-40 && NR<=l+40' BRT.txt | grep -nE \"^[^a-zA-Z]*[0-9]{3}[^0-9]|[a-zäöü-]+-? +[0-9]{3}$|^ *[0-9]{3} \" | head -6; done"
}
```


### [2026-09-04T18:39:18.319Z] TOOL RESULT

```
== around 12541
71:208).  —  mp,  (Pü.)  dösastar;  s.  No.  I.  —  •»  Das
== around 13624
11:745  _  d^m
48:747  dij»-  —  ■*daä>rim  748
== around 15604
== around 8636
42:iizbaodah-  412
```


## [2026-09-04T18:39:22.702Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=12400 && NR<=12600' BRT.txt | grep -nE \"[0-9]{3}\" | head -20\necho \"== 15500-15700\"\nawk 'NR>=15500 && NR<=15700' BRT.txt | grep -nE \"^ *[0-9]{3}|[0-9]{3} *$\" | head -20"
}
```


### [2026-09-04T18:39:25.066Z] TOOL RESULT

```
1:663
8:»/in'jm;    %  268.   12,  22.    —    »    Mit  «  nur  F.
13:iflOÄ     nS   /raourvaaayäiti     drujS    vais- mmda  "  aztmnqm  (sd.)  Yt  10.  86. Vgl.  gr.  *ij  iilKi^i),    ahd.   zuo.   —    ')  S  304-
17:.  .  aspa  'nu  .  .  ustra  °nu  ar»j6  "um den  Preis  flir  eine  Eselstute  . ."  V.  7. 43'J; —  haza»r?m  maisinqm  'nunqm  . .  gavqm nunqm  . .  aspanqm  'nunqm  .  .  u^tranqm nunqm  paitipukranqm  A,_y.  7— 10. Zum  ai.  V.  dhäyaä;  %  /g.  I.  —  ai.  ähineii- 1.  — Pü.:  dhiülak,  Npü.!  la-  dir,  Sü.  r  dugdhavali, —  ')  S-  lu  'arSan-  No.  3  und  den  Gebraucli des  np.  mäda,  sowie  ai.  gävo  dhenävah  und Pänini  3.  I.  65.  —  ')  Anders  Gray  IF.  11. 310.
18:•  j.,  g.  'daenä-  t  'Religion';  i)  im  gAw.'>: tqm  °nqm  ys  Aatqm  (Sp.  268  o.)  vaMstä .'.  3r»s' daidyat  (sd.)  Y..^^.  lo;  —  iaS<7 tSng  a  vtpmyät  (sd)  ärmaitis  yaHbyS masda  %wsi  vasyetE  'nä  ".  .  denen  deine Religion  verkündet  wird,  o  M."  Y.  44. 1 1 ; —  »ns  vTcidyai  (sd)  tqm  °nqm  yä  xsma- vatö  (sd.)  Y.  4:^.6;  — '  a'iw^V  (sd.)  mzüT fa^ö  yqm  'nqm  ahurö  sao^yantd  dadät ^-  53- ''  —  iiiit  vanhav-  Adj. :  ya^S  Asi dab»n  (sd)  . .  'naya  vankuyh  ucSiä  iyao- %anacä  Y.  5_J.  I.  2)  im  jAw.:  aya 'na  (IS.)  disyat  (sd.)  yS  .  .  aiwyir»Aqm (sd)  nöit  aiwyästi  \.  18.^;  —  anraAt mainySus  nasiltqm   'nqm  dalvayasnanqm
20:663
31:V.  18.  \;  —  axstaäta  'naya  vaca framrü  Y.J.  i;  —  zara'ku/trahe  'nqm  .  . lannsmca  tka^jmca  Y.iÖ.a;  —  vaehä •nyä  FrB.;  —  'nqm'^  ..  dät>m  vTdsyBm  V. /p.  16;  —  mq'hraAe  spmtahe  .  .  'nayä  .  . staolanam  yesnyanqm  "Vt-O-T,  —  'nayä .  ,  dhaurunqs^  rähaßtäs^ä  västryqscä fhtyantd  Y,  y,  3 ;  Vr.  J.  5 ;  —  ytzi  'nyä  . . ai»Aai  (Sp.  270  o.)  Nik.  /;  2;  —  AäyaoidA yä  'na  V.5.21;  j.42,  Yt  JI.  3,  Vyt^j; —  °na  . .  nars  aiaonS  fram>maiti  vUpim dulmatimca  . ,  V.  j,  42;  —  'na  . .  p3r?näyul cihqm  %wfnsaiti  W.j.  41  (?).  a)  meist mit  einem  bestimmenden  Dem.-Proa  oder Adj.;  n)  'a-,  ^ada-,  ima-,  Y.  S.  7,  g.  31, 60.  2,  Vr.5. 3.  Yt  y.  99  (Sp.  2  u.,  3  0-); N.  ji  (Sp.  32  «.);  V.J.  30,  Yt  S.  59  (Sp. 368  u.,  369  u.).  ß)  ähuray-  und  sara-
32:%ultray-.  Y.S.  7,  72,9,  60.  2,  Yl5.S9,  y. 99,  V.  2. 1,  2  (Sp.  346  m.).  7)  mäzda- yasnay-,  uzw.:  °nä  'yasni/ W.j.Jii,  43,  5. 21,  Yt  II.  i,  y.  94,  VytJ5;  —  'rtam 'yasnlm  Y.g.  26,  12.  9,  25.  6,  Yt  2.  14, g.  26,  V.  2. 42,  3. 31»,  40',  ig.  2,  6,  7,  16, Vd.  <?;  —  'nayä  ('nayäsca)  'yasnöil  Y, i2.9,  y.3'.  8,  15- 1,  22-25.  J5-I.  Vt;o. 117,  136,  J'9.69,Vr.j.  5,9.7,  ro.3,  72.3, G.  2.  7,  V.J.  30,  g.  2,  47,  52,  P.  i4,  FrB^ Nik.  j,  2;  —  'nayät  'yasnBii  ^.  41';  — •ne  'yasne  (s.  a).  S)  vanhav-  und  mäsda- yasnay-%  vaauAi  'na  °yasnif  Y. 3,42,  Yt. '3-  94;  ~~  vaauhJm  °nqm  'yasnlm  Y. g.  26,  V.19. 16;  —  'nayä  vanAuyä  'yas' nBif  Y.  22. 3.  S.  femer  zu  7  und  0 unter  a.  a)  als  Gottheit",  immer  mit mäzdayasnay- fiäy.  ya%a . .  äs  saoiS  mana yat  ahuraAe  mazdä  'nayäsca  •yasnsii  Yt. ig.Zz;  —  m(hr»m  .  .  yeAAe  °na  'yasnil lfm  (sd.)  pdhs  rähaiti  Vt  10.  68;  —  pUa /?(näml.  asöii)  yS  ahurS..brata..sraolS.. :^at3ha  'na  'yasnis  Yt  ij,  16;  Yyt $2;  — usia  ml  aAura  mazäa  . .  usta  'ne  (VS.) 'yesne  Yt.  Ä  29;  23,  Y.  S.  3;  —  'na  'yasne Yt/Ä8(?);  —  v:>n%ra^n3m  ya^  °nay& 'yasnsis  Vyt  42;  10,  34,  J7.  a)  sonst
38:666
39:nim  Vr.  7.  3 ;  Yt  2.  i  a,  Vyt  i4-  a)  äai^ nayä  (näml.  ayah)  heisst  der  24.  Monats- tag; °nayä  vavhuyJ  mazdayasnUi^S.i.n; vgL  2. 24,  Y.7(».6.  a)  GS.  mit  a^OTOna- m.  Name  cioer  Gottheit:  äat  hl  (näml. mi^raie)  Aävlfya  ar^e  vasatte  .  .  'nayä mäzdayamSiS  upamaram  (statt  NS.;  Sp. 391  u.)  Yt/0.  ia6.
43:*)  Ein  tlieologiscb-philosophitcher  BegrilT,  die Geiammtbeit  der  leeliscben  und  religiüsen Eigenschaften  eines  Menschen,  seine  seelische und  religiöse  Individaalitit  Sie  lebt  nach  seinem Tod  als  selbständiges  Wesen  fort  -  Tgl.  zu  yj-o- vasay--,  um  schliesslich  den  Wiedererstandenen ~  oder  seine  Seele  ~,  nachdem  sie  ihm  -  oder seiner  Seele  -,  gewissermassen  als  Spiegelbild seines  Innern  als  schönes  oder  hässliches  Mäd- chen erschienen  war,  lu  Faradies  oder  Hölle  zu geleiten.  S.  lu  obigen  .Stellen  noch  Av.^.gfT., //, äff.,  Mx.  3.  las  ff-  167 ff-  —  **J  D.  h.  die D,  des  Saafyant  (Zar.)  wird  seiner  (des  Gläubigen) D,  dereinst  (nach  dem  Tod  bei  der  Himmels- reise)  wie  ein  Freund  beistehen;  vgl.   daiu  V.
45:KompE.  —  Et.?  Ob  gleich  'daenä-  (sd.)?  S. No.  I.  —  Pü.:  den;  s.  noch  No.  3,  5.  — >)  Wo  ae  im  Metrum  für  iwei  Silben  rechnet wie  bei  ^daeaS:  —  »  Vgl.  (lu  V.5/.  19,  SS-  S) Y.J/.ai.  — 1)  Pü.;  fl  rfmWä«;  vgl.  PüErl.  zu den  inY.j7.  aj.—  4)DasVerbum,  etwa  atih>n, ist  zu  ergänzen,  yä  drjgvalö  daenä  statt  aKyäi daenayäi  yä  dr'.  Eine  ganz  ähnliche  Ellipse zeigt  V.  4q.  5  d;  5.  Sp.  614  m.  mit  No.  4.  — 5)  Pu.:  den,  erl.i  kiimin;    s.  dazu  No.  7f.  —
50:668
51:6)  An  der  Parallelsl.  V.j.zi  sieht  beidemale aii/ivqm  statl  datnqm ;  I.  No.  9.  — ■  7)  Statt dessen  steht  Av.  4.  18,  77.  13:  an  i  ^cs  dm u  {an  i  x"!!)  haiisn,  aber  Mx.  1.  laj  blos; an  i  ^eskuniin;  s,  No.  5,  8,  —  8)  Statt  dessen Av.  4.  34:  tuniin  i  tö,  r^.  14:  an  i  IS  kuniin i  vat,  Mx.  3.  130:  tuniht  >  Htvmt  i  Id,  171 : duiiuniin  i  tS;  vgl,  No,  5,  7.  —  «  Die  Glosse dazu  erlilärl  beide  WSrter  für  gleichbedeu- tend; s.  aJiküä-  No.  3.
52:•  j.  daenä'vazah-  m.  EN.  eines  Gläubigen : 'zanhs  asaonS  Yt  13. 117.
56:•  j,  daenö.sak-  Adj.  'der  sich  auf  die Religion  versteht,  darin  unterrichtet  ist'; •säcain  ..  asaonam  a^aoninqm  Yt/J,  155; —  *ratui.mirita  'säca  (IS.)  Y, /p.  17.
58:•  j.  daeman-n.  1) 'Auge,  Augapfel';  mi^rd .  .  a%ra  naram  mi^rSJrujqm  .  .  *pairi 'ma  (AP.)  värayeiti  Yt  10. 4*8;  —  yat  .  . uB  pairtjäarayeifttH^ä)  °ma  (als  AD.)  . . pairi.urvaBayänti  Yt  14. 56.  a)  "Blick': irtra  datäiti  •mäna  (AP.?)'>  darätsüka dsi'iräiya  Yt  10. 107  (?).
64:—  'va  Aqm.rae'iui/iyati  (sd.)  Y.ig.20;  — 'va  drvantB  duldanhs  V.  ig.  3,  aS,  44— 47*;  —  'vanqm  da?u9.tim>m  Vtj.  14";  — kS  'vanqm  xawt5  (sd.)  ks  'vanam  xumbö ks  'vanqm  ia.nairls  iB  havqs{sA.)  'vS  in vispö  'vS  kö  para  m^ntö  'vS  k3  pasca m>r)tS  mainyava  'va  /raba7iainlH . .  aria:-a vjptö  ariaca  va^ayS  (sd.)  V.Äsif.;  32'; — ■  'vanqm  rapaks  V.  7.  56;  —  vi  'väiS ayais  *avat>hTs  anantail  aks.dabli  sarvm mruyl  hatqm  draojistais  . .  vT  'vais  vi daFvavatbls  Y.12.4;  6';  —  staoml  ahm ..  näismiisd.)  'vtriAP.")  W.  11.  ig— 12. 1; Yt.  7^.  89;  —  us»M^lala  masyäka  staeta ahm  . .  nTsta  (sd.)  'va  \.  18.16;  —  'va apa.dvaraia  Ytj.  7;  —  vil  apqm  ^a patmtu  vT  'väahs  vT  'vaysil  (NPf.)  Y. 70. 1 ;  —  paitistätSe  t>masciiiranqm  'z-anqm Ytö'.4;  y.  137;  —  duSmainyam  sisdyd 'vqn  apa  "asavqn(sd.)  Yt/p.84; — yaha azpm  uzbanini  hala  'vaHbyB  uyl  lüil'a saokaca..  Ytj.  26;  Jp.  23;  —  AS  (oämL
66:669
69:670
== 15500-15700
31:361.   —   >>   Aus  dem  versleinerlen  NS.  nach    Akk.;  l)  räumlich,  a) 'um  — herum':  tcrf'Hr.i
48:862
62:863  pairiuxSatay-  —  *pairLg^vatah-  864
86:865
89:866
126:867
129:868
175:869
178:870
```


## [2026-09-04T18:39:31.342Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=12470 && NR<=12580 {print NR\": \"$0}' BRT.txt | grep -E \"\\b6[6-9][0-9]\\b\" | head -20"
}
```


### [2026-09-04T18:39:33.933Z] TOOL RESULT

```
12470: —  sraohm  ..yd..yBityeiti..Aata  'vaeibys Y-57-IT, — paiti-pirme  vannya  'z/fffAP."') V.  70. 14;  —  yat  baväni  aiwi.vanyä  vTspe •va  Ytp.  4,  /5.2g;  —  imi  alte  vaca  yoi fanti  vjspanam  'vanqm  snahim  V.io. 16;  16,  Y.27.1',  Y.ig.46';  —  snaihi/.. hvS.vafjim  kam^rihe  patti  "vanqm  Y.  57. 31;  31,  YtÖ-s,  jo.aß,  129,  V.79.15;  — pas^a  jainti  'vanqm  . .  fravaxaiU  mihrS Yt  70. 133;  3. 10,' 4-  2,  5-  2^.  V.J.  32;  — hasat^rayna  paiä./asaiit  aiars  .  .  'vanam mainyavanqm  ..  drvatam  Y.S.So;  Y.io. 6,  YL  13. 4S;  —  asfi»  ,  .  taurvayeintim vTspä  tbalsa  'vanqm  maSyänqmca  Y.52. if.;  5.18,  Yl/.i',  S,  6;  —yat  mqm nalcis  taurcayät  nsit  °vS  na^a  masyS  nöii yäiaz'B »a^a pairikä  YtJ.6;  J5.56,2.n(?); — paitiltätse  'vaheca  tbaiiatahs  ma^eheca Y.6S.S;  5S.3,  VLy.'"i42;  ~y8..ä>,r)m urvaaayata  °väatia  haotäti^A.)  mafyäatca Vt  13.  89;  —  'vanqm  parö  draomBku  Yt. ^3-57!  57-  S.  noch  Y.J5.  2  (Sp.  667 u.).  a)  klassifizirt:  mürym  . .  yahmal haca  frabr^SMii  vTspe  mainyava  (Stverz.) •va  yaica  varsnya  (Stverz.)  drvants  Yl /o.  97;  usw.;  —  paiti^tätJe  mäzanyanqm (Stverz.)  'vanam  varmyanqmca  Yt.  13,1  ^T, usw.  b)  namentlich  bezeichnet:  °vö  ao^O V. /j.  i;  —  akataam  dasum'^'^  V. 79.43  (statt  Nom.);  —  °vasca  yS  apaoSs \X.8.ii;  XI,  22,  28  (daiam^'i),  18.2,  6;  — inärS  °vS  V,  ig.  43;  —  kasvjS  'vS  V.  ig. 43;  —  daium  kund»n  V,  75.41;  —  daiwil 'vS  V.  79. 43;  —  driieis  °vS  V.  iq.  43 bßiti  'vS  Y.ig.  i,  2,  43;  —  paitisJ  °vS 'Z'onqm  da!v3JfmS  V,  7^,43;  — "^jm  dalum  V./0.9;  75.43; —  vätJm  'vö (statt  Akk.)  V.  70. 14;  —  vTzansd  °vS nama  .  .  urvän^m  bast>m  vataydti  V.  ig. 39;  —  saouru  'vS  V.  7_9. 43;  —  ar^rff mainyus   .  .  'vanqm  'vs  Y.ig.  1,  43;  44;
12498: 671  daevayaz-  —  daes-  3  (
12530: 673
12533: 674
12580: 676
```


## [2026-09-04T18:39:44.503Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD\"; grep -n \"diz\\|dēz\\|dēg\\|dywʾl\\|dywār\\|dīwār\\|pardēz\\|pālēz\\|plyc\" PHD.txt PHD_mackenzie.txt | head -40"
}
```


### [2026-09-04T18:39:44.556Z] TOOL RESULT

```
=== PHD
PHD.txt:312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
PHD.txt:314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
PHD.txt:394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audience, presence. handēmānģar [kndym’ nkl] introducer (into the presence). „lt: introduction. handéSidan, handēš- [Ahndyti-ytn! | M hndy§-, N an~] think, consider, reflect. išn: thought, reflection. handēšīdār [hndyfyt?I] thoughtful. handēxtan, handēz- [hndwhtn', hndwc- | N an~] gain, acquire, amass. „-išn(īh): acquisition. handraxtag [hndl htk! | P ?ndrxt] oppressed. ~ih: oppression, suffering. handüdan, *handāy- [hndwtn' | (M ?nwd), N an~] smear, plaster, anoint. hangad [hngt! | P ?ngd] fortunate, rich. ~ih: fortune, wealth. hangām [hng’m | N ~] time, occasion. ~ig [-yk!] timely. hangarag [hng’lk' | N angara] reckoning. hangardan, hangàr- [hng’l-tn' | M hng^r-, N an~] consider, reckon. ~išn: consideration. hang��xtan, hangéz- [hngyhtn', hngyc- | (M hgjyn-), N an~] arouse, stimulate, stir up. ~išn: arousing. hangirdénidan, hangirdén- [hngityn-ytn'] complete, summarize. hangirdig [kngltyk'] complete, perfect; summary. ~ih: completion, summary. hangdSidag [hngw£ytk! | M ”ngwšydg] way, manner, likeness. ~ 1: like. hanģrāyīdan [hngl’dytn'] lament. hangrüdag [hnglwtk'] lamenting. hanj-, v. hixtan. hanjaftan [hncptn' | P hnjft, (M hnzpt)] be finished. hanjāftan, hanjām- [hnc’tn', hnm- | P hnj ft, hnjm-, (M hnzpt, N anjāmīdan)] finish, complete, carry out. hanjām [kne m | N anjám] end, completion, outcome. hanjaman [hncmn! | (P ?njmn, M hnzmn), N anjuman] gathering, assembly, congregation, community. ~ig [-yk'] (notable) member of the community. hanjīdan [hnc-ytn' | N ~] = hixtan.
PHD.txt:536:pa(č)čēn [pcgn!] copy. *pa(č)čībāg [pcyp k', PWNe- | N *pajiw] *deceptive. ^h : deceit, hypocrisy. *pa(č)čībāy- [pcyp'd-, PWNc-] deceive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N pāyēz] autumn. pad-góhr [PW Ngwhl] т. jewelled; 2. of good stock, well-born. padifrah [p’tpl’s | M p'dypr?h, N *pādafrāh] punishment, retribution. padir-, ~išn, v. padiriftan. padirag [ptylk' | M pdyrg, N paóira] towards, against, counter-. (6) — madan: come to mect. ~ih: meeting, opposition.
PHD.txt:542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
PHD.txt:720:acgutsition handēzišn, windišn.
PHD.txt:902:authorized pādixšā(y). autumn pādēz.
PHD.txt:1175:cauldron dēg.
PHD.txt:1683:double dēgānag.
PHD.txt:2017:fortress diz, drubušt.
PHD.txt:4742:padyabib, ALI 00 t€» о) pādāšn VA My o padirán- ` - My yey a pādīrānēn- -p ry yey a pādīrānēnīdan W3 y ry We pādīrānīdan WS wy veyo pādīrān wey yey os paymar Ne теу o pādēz 23 voy o lpādan Y rero) pādofrāh ау\һе» 0) padzahr NS ve» o» pāygūs ISYA padrozag 15 cP rere pāyram » rey’ о
PHD.txt:4993:diz!
PHD.txt:5314:diz, gač, gaz
PHD_mackenzie.txt:2003:diz [KL YTA < A qryt'; de 1 M dyz, N -] fortress.
PHD_mackenzie.txt:2394:frez [plyc] duty, obligation.
PHD_mackenzie.txt:4048:parrextan, parrez- [plyhtn , plyc-] remain over, be superfluous.
PHD_mackenzie.txt:6649:fortress diz, drubust.                          karih.
PHD_mackenzie.txt:9525:kamist               \~~              diz1                 ~~~
PHD_mackenzie.txt:10442:diz, gae, gaz                               V       guftanl '
```


## [2026-09-04T18:39:51.256Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB\"; grep -n \"\\bdiz\\b\\|dēz\\|dyz\\|dywʾl\\|dēwār\\|dyw'l\\|dēg\\b\\|dyk'\" NYB_vol2_glossary.txt | head -20\necho \"=== NYB des\"; grep -n \"dēsīdan\\|dēs-\\|daēza\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-04T18:39:51.324Z] TOOL RESULT

```
=== NYB
1287:distak [dystk'] *treated, manipulated, or the like: pat Hēšm zahr ~ "treated with (the demon) Wrath's poison 2516-17 = 2814, — In the edition the first letter is a marked d, hence the reading dystk' is cogent. Because of -ist- this must be a SW form corresponding to a NW form with -i$t-, but its meaning in this context make it impossible to combine it with NW dištan (v. next w.): a weapon is not “built” or “‘formed’’. It would be tempt- ing to connect it with Skr dih- ‘to daub, to smear', but the corresponding Av. (673) dačz- has other significations (cf diz), and the Phl. renderings of it (Vd 39.13.18, 733. 1536) have run wild and are no more recognizable (they can scarcely be brought together with dés-, v. the next w.).
1302:diz [dc'] castle 2326-27, 241.3-6. 10817. 11111-43, — MPrthPrs dyz (S, A-H II, MHC); NP diz. - NW form, as against OP dida-. From Av. (673 sq.) daēz-; cf s. v. distak.
1607:Kurd. gewr ‘grey, iron grey, black- brown’ or ‘mottled’ (Kurdoev). On the other hand, the other great authority, al- Birüni, gives the name in the form dyzh-k’w (Chronol. 1043), evidently the copyist’s mistake for dbrh-k'w = BP davr-gäv, and in fact BdA 2295 (= BdJ 771° just quoted for gefr-) has as first element [ddpwl! for] davr (q.v.) In BdA 103° = BdJ 354, BdAntiā 7618 transliterates it gfr, but the authority of this text is poor.
2518:mazdčsn [Prs inscr. mzdysn], BP maz- désn [m'zdysn', m'zdsn'; commonly in the distorted graphic form given I, 134, 9 A], Prth. inser. mazdézn [mzdyzn]: Maz- dah-worshipper, adherent of the religion of Ahura Mazdah, in Av. terminology: a Mazdayasnian; in the title of the Sas.
2744:nipast [npst'] place where a thing is deposited, depository, gl. of KLYT’ = gellāitā (v. Ideograms) 107%, — I reject the interpretation of the passage given by Bailey, ZP 152. There is no evidence what- ever of an ideogr. KLYT = QRYT’ being used for diz ‘fortress’. This Aram. w. always signifies ‘village’; in the FrP, ch. 2, it is hidden behind the somewaht be- wildering disguise MRDYN! (-DYN- common. error for -YT-) for MRYT" for QRYT* (cf MDM for QDM) = rētastak (g. v.) A form *ntptst for nipist is no- where attested, so the diz i nipist has to disappear from our context. KLYT? = Aram gellāitā (ultimately from lat. cella) refers obviously in KnS VI, 11 to the sanctuary of the Dragon of Kirman, most probably a cavern. — I deeply deplore the Ahrimanic slip of pen which made me write ntpāst, instead of nipast, as the equivalent of KLYT’ in the Index, I, 160a, 14. A benevolent critic will find the correct reading nipast in I, 157a, 30. - From nipastan; nipast is to nipastan what nisast is to nisastan.
2751:nipišt [npšt'] that which is written, coll. documents: diz i ~ the archive 10817. 1111.13,
3021:pätez [p'tyz] autumn 887. — MPrs p'd(y)z (A-H I), Paz. pādēz, NP payiz. V. Bailey, TPhS 1945, 13.
4885:dida: diz
5109:dačz-: diz
5610:dwjx: ddsax¥ dwšfr: dušparg, dusx"arr(ah) dwsmn: dušman dwšmyn: dušmēn dyb: dipivar dybhr(g): dépahr dydn: ?ditan dydyšn: bastišn dyn: den dyrdn, d’r-: daštan dyštn, dys-: dištan dyz: diz
5949:dyz: diz
6767:pa: pat padafrah: patifras pādāišn, pādāš(a)n: pātdāšin pādan, pāy-: pātan pādēz: pātēz padīra: patīrak padīraftan: patigriftan pādišāh: pātixšāi padix"i: patēxvēh pad-kēs: pātkust
=== NYB des
1316:dösitan [dwsytn'] to milk 429. 10122. — Root "dheugh-, Olr "daug-, Skr duh-, cf NP dy ‘churned sour milk’. dēs- prob- ably < *dör-s- with the Prth. pres. suff. -s-, Ghilain 79 sq. — NP dēšīdan with an unexplained -š-.
3871:uzdés-car [^wzdysc?l, >wedyse’l] temple of idols 7133. 9918, — < uzdēs-tacār, v. uzdaēs-
3877:uzdēs-paristišnēh [—-šnyh] idol-worship, idolatry 711°.
5834:"wzdyser: uzdēs-cār
```


## [2026-09-04T18:39:59.141Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='NYB_vol2_glossary.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nprint('formfeeds', t.count('\\f'))\nlines=t.split('\\n')\n# find numeric-only lines near 1302\nfor i in range(1250,1330):\n    s=lines[i].strip()\n    if len(s)<6 and s: print(i,repr(s))\nEOF"
}
```


### [2026-09-04T18:40:01.181Z] TOOL RESULT

```
formfeeds 294
1254 'dén'
1263 'dév'
1284 'dit'
1290 'dit'
1297 'dokan'
1307 'dókün'
1322 'dranj'
```


## [2026-09-04T18:40:04.286Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='NYB_vol2_glossary.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nimport re\npages=t.split('\\f')\nfor i,pg in enumerate(pages):\n    if 'diz [dc' in pg:\n        print('ff-block',i)\n        print(pg[:300])\n        print('...')\nEOF"
}
```


### [2026-09-04T18:40:06.067Z] TOOL RESULT

```
ff-block 75
 from SW *daid-). Sogd óys- BBB p. 56 ult.
dit [TW B, inscr. TWB] 1. the second, the other: rēc i ~ 83; či 1 ~ the other 12118; &vak apāk ~ 104?* etc. ;évak 6 (61) ~ 1009-13 ete. — 2. adv., also ~-ic, for the second time, again 46*3 etc.; further, then 515; back P2:10; — 1116 v. dit. — Shortened fro
...
```


## [2026-09-04T18:40:12.685Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['NYB','PHD','HRN','HUB','BRT','KNT','TLM','IEC','SYN','WLD','LEW','LAT','KLN','SKT','FSD','WEB','SOD','AFM','ARY','CHEUNG','FRS','MON']:\n    v=d.get(k) or {}\n    print(k,'|',v.get('page_offset'),'|',(v.get('lookup_hint') or '')[:200])\n\""
}
```


### [2026-09-04T18:40:14.469Z] TOOL RESULT

```
NYB | Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
PHD | leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A
HRN | leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered ent
HUB | leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
BRT | Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin glos
KNT | leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall i
TLM | leaf = printed + 20 (e.g. leaf 24 = p.4). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Lexicon headwords are OP words in transliteration at line start.
IEC | TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
SYN | leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed p
WLD | Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, u
LEW | 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
LAT | leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
KLN | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume p
SKT | leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
FSD | vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
WEB | not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabe
SOD | printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD
AFM | 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أ
ARY | printed page = pdf page + 1 | Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword
CHEUNG | None | 
FRS | different edition — no mapping | Look up the headword (entries grouped by final letter); FRS_pages.txt has \f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.
MON | None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Aves
```


## [2026-09-04T18:40:23.212Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ncat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py <<'EOF'\nimport sys,re\npath=sys.argv[1]; pat=sys.argv[2]\noff=int(sys.argv[3]) if len(sys.argv)>3 else None\nt=open(path,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nrx=re.compile(pat)\nfor i,pg in enumerate(pages):\n    if rx.search(pg):\n        pr = (i-off) if off is not None else None\n        print(f'--- leaf {i}' + (f' = printed p.{pr}' if pr is not None else ''))\n        for m in rx.finditer(pg):\n            s=max(0,m.start()-200); print('   ...',pg[s:m.end()+400].replace('\\n',' '))\n            break\nEOF\necho ok"
}
```


### [2026-09-04T18:40:23.261Z] TOOL RESULT

```
ok
```


## [2026-09-04T18:40:27.395Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\necho \"### PHD dewar/deg/diz\"; python3 $S PHD.txt 'd[ēé]wār \\[' 21; python3 $S PHD.txt 'd[ée]g \\[dyk' 21; python3 $S PHD.txt 'diz \\[KLYTA' 21\necho \"### NYB diz\"; python3 $S NYB_vol2_glossary.txt 'diz \\[dc' 8"
}
```


### [2026-09-04T18:40:29.202Z] TOOL RESULT

```
### PHD dewar/deg/diz
--- leaf 49 = printed p.28
   ... , appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing.
--- leaf 48 = printed p.27
   ... ānīh [nyh] | (N dāyagī)] nursing, nurture. dazidan, daz- [dc-ytn'] burn, scorch. --išn : burning. débag 26 dist débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d�
--- leaf 49 = printed p.28
   ...  sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-to
### NYB diz
--- leaf 75 = printed p.67
   ... ble. Possibly < *dipi-vahana- 'docu- ment house', v. dépivar. divar [dyw?l] a wall 39%, — NP divar. V. Hübsehmann, PSt 65, no. 599, whose etymology is quite satisfactory: *dida- vüra-, v. the next w. diz [dc'] castle 2326-27, 241.3-6. 10817. 11111-43, — MPrthPrs dyz (S, A-H II, MHC); NP diz. - NW form, as against OP dida-. From Av. (673 sq.) daēz-; cf s. v. distak. do [TLYN 62". 645. 120%, elsewhere figure] two. - SW form < *däu, Olr *dvāu; MPrthPrs dw. — Cf s. v. vicitan. *dó-apdàn [dw'pd'n'] "he who has two water jugs — "the constellation Aguarius 510, — My guess. On the Dendera picture of the Zodi
```


## [2026-09-04T18:40:38.548Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\necho \"### HRN paliz\"; python3 $S HRN.txt 'p[āaä]l[īi]z' 21 | head -20\necho \"### HRN firdaus\"; python3 $S HRN.txt 'firdaus|firdans|pardis|Paradies' 21 | head -30"
}
```


### [2026-09-04T18:40:40.837Z] TOOL RESULT

```
### HRN paliz
### HRN firdaus
--- leaf 77 = printed p.56
   ... drücken, dass auch np. ber/ Teil' (Sahn. I, 77 Anm. 11, Calc), ber/e hierher gehören ; dann natürlich auch afy. LW. bar/a, bra/a ^Anteil', vergl. Hörn, Indog. Forsch. H, 138 Anm. 246. bihiSt^ behist ^Paradies'. (äw, mhista- 'bester; phlv. vahist; ai. väsistha-. LW. kurd. behist. Die Aussprache behist ist die ursprüngliche ; in bihist ist der erste Vokal dem zweiten angeglichen. 247. be, ehe 'ohne'. phlv. ape- (päz. atve-)^ z. B. ape'\htm, ape]vnäs etc., be (ZPGl.), vergl. arm. LW. ape]niaz, kurd. af/. bei. LW. bt- resp. he-. *) Fr. Müller, WZKM. 5, 186, Anm. vergleicht aw. vahhana' *Kleid\ was ganz un
--- leaf 248 = printed p.227
   ... che Dialektspaltung voraus ; g. watah und oss. mäfix sind wohl erst sekundär (an ein phlv. *mata/, wie von Stackeiberg, ZDMG. 43, 672 es zu tun scheint, glaube ich nicht). 1011. niTnö {*menö) Himmel, Paradies; Smaragd', vergl. mlfiä Emair^). aw. mainyava- geistig, himmlisch' (NB. heisst aw. mainyU' nie 'Himmel'); aw. menö^^) 'Geist; Himmel'. 1012. niehen 'Haus'. aw. maedana- 'Wohnung; phlv. mShan, vergl. Artaky§]midan, Stadt in Chorasmien (Yäqüt), Xas- mi&an^) ib., KvS\mthan, ib. (Nöldeke, ZDMG. 33, 153, de Lagarde, Purim 40, Note 2) 5). bei. metag 'Haus, Wohnung' (241). ') Falsch statt malax- 2) Np.
```


## [2026-09-04T18:40:46.274Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"palez\\|paliz\\|pälez\\|päliz\\|falez\\|jaliz\" HRN.txt HUB.txt | head -20\necho \"=== HUB firdaus\"; grep -n -i \"firdaus\\|firdans\\|pardis\\|paradeisos\" HUB.txt | head -20\necho \"=== HRN deg\"; grep -n -i \"^ *59[0-9]\\. \\|deg 'Kessel\\|dSg\\|dēg\" HRN.txt | head -20"
}
```


### [2026-09-04T18:40:46.348Z] TOOL RESULT

```
HUB.txt:4331:ap. pari' zu par-y vgl. palez aus ^pardcZf s. p. 123;
HRN.txt:2746:279. pälez 'Garten (Sahn. I, 73 Vers 207) ^), palezhan, arab.
HRN.txt:2778:^) Palez soll nach den persischen Original Wörterbüchern mehr
HRN.txt:13257:! pälezbän 279.
=== HUB firdaus
=== HRN deg
5284:590. dT, dtg 'gestern', :m (Is. 30, 33), dme, diröz^ dlseh.
5299:591. debä, debah *Brokat', arab. dliäj; debäce * Vorrede*.
5305:592. dlden 'sehen, dld 'Anblick; sehend', didär,
5310:593. "des, -dis, -des gleichend, ähnlich*.
5317:594. deg *Topf*, vergl. dez, deze,
5324:595. dlger, dediger (Vis und Rämin, S. 29 V. 5 v. u.)^)
5337:596. dltn i^dem) ') *Geöiclit, Waiigun , dliue,
5343:597. dtn 'Glaube, Religion*.
5347:598. dev 'Dämon, Teufel', dcväne Verrückt*, n^NDH (Jer.
5350:599. dlvär 'Mauer, Wand'.
```


## [2026-09-04T18:40:49.120Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2740,2785p' HRN.txt\necho \"=== HRN 594\"\nsed -n '5317,5325p' HRN.txt\necho \"=== HUB 4325-4340\"\nsed -n '4325,4340p' HUB.txt"
}
```


### [2026-09-04T18:40:49.180Z] TOOL RESULT

```
päz. pälJdan, pälaidan (West, Sik. gum.-Gl.).
bei. LW. palayag^ pälenay 'seihen, worfeln, reinigen'
(292).
^j Vergl. Geldner, Studien I, 16. Bartholomae (briefliche
Mitteilung) verweist mich aber auf aw. parendi- (Indog. Forsch. I, 184)
mit der Grundbedeutung 'Füllser.— 63 —
279. pälez 'Garten (Sahn. I, 73 Vers 207) ^), palezhan, arab.
LW. faliz,
ap. nagdÖHöog; aw. pairida^za-,
LW. kurd. päres, arm. partez, syr. Dn*)5?, JDD'^'TlEi.
280. panzde 'fünfzehn , vergl. pänsed 'fünfhundert'.
aw. paücadasa 'fünfzehn; skr. pdflcada^a; phlv.
pancdahion,
kurd. [daupe/ij etc.]; paiizde (LW.); afy. pinjalas;
oss. d. findtäs^ t. findfäs (292) ; bei. panzda (LW.).
281. päl^ pä Tuss ; vergl. paye 'Stufe', päym.
aw. päda- 'Puss* ; phlv. pCLT *Fuss', päyah *Stufe' ; ai.
päda-; arm. otn (H. No. 280).
kurd. pai (LW.) 'Fuss'; bei. päd, n. /xlJ, ^^ö^ (291);
oss. *fad aus bäymmoad-äi 'barfuss*, bäyömbad-äi 'bar-
fuss erschlossen? (267).
282. päyisten 'fest stellen , dauern ; erwarten ; vergl.
päylden 'schützen', päyende.
ap. l/^pä-, pö^wi; schützen; aw. l/^pÄ-, pcf«7e, vergl.
paiti.pait^ (yt. 10, 19) erwartet, versieht sich';
ai. [/'pä-, pdti.
Bei AM. ist päyTden als schützen, conserviren sehr
häufig, z. B. 'schützt vor Zersetzung (191 Zeile 2,
248 Zeile 6), erhält das Haar' (122 Zeile 7), *die
Gesundheit' (237 Zeile 4); auch 'sich halten', z. B.
seine Kraft hält sich nicht länger als ein Jahr (187
Zeile 3 v. u.).
Vullers (Lexicon) nimmt mit Unrecht zwei ver-
schiedene np. päyiden an.
Da für p&yiden (phlv. pöyitan) die Aussprache mit ö
durch den Reim gesichert ist (z. B. Sahn. I, 143, V.
251 — pöt^ röT — II, 962, V. 34 — pöyende^ jöyende
— III, 1096, V. 528 — pöi, jm, Vis und Rämin, S. 48,
^) Palez soll nach den persischen Original Wörterbüchern mehr
*Fruchtgarten' bedeuten; die obige Stelle, sowie Sahn. II, 765, Vers 5,
sprechen nicht dafür. Sahn. II, 626, Vers 1846, III, 1377, Vers 2047
sind zu allgemein.— 64 —
V. 8), so sind meine Bemerkungen, BB. XVII, 258
verfehlt und man kann nicht auf f ermüden, fermayem
verweisen.
283. päyi;^ 'Herbst*.
=== HRN 594
594. deg *Topf*, vergl. dez, deze,
phlv. deg 'Topf; lat. figulus^) Töpfer*; mhd. tigel^
tegel, ahd. tegal 'Schmelztiegel*, an. diguU 'Tiogcl*.
LW. kurd. dizik; af/. deg^ decka; bei. deg, dez, dPd,
Oegci (59); wa/. dlg^ sar. deg.
Zu ai. \/'deh', degdhi 'bestreichen, kitten', got. deignn
'kneten, aus Thon formen*.
595. dlger, dediger (Vis und Rämin, S. 29 V. 5 v. u.)^)
anderer ; sidlger^ süHg ein Drittel* (AM. 110 Zeile 2 v. u.).
=== HUB 4325-4340
standen hatte (vgl. zlnehar^ yadegar Fird. I, 131, 34; name-
var 132, 55 etc.), doch geschieht dies nur metri causa, da
hier iiberhaupt nach uberlangen Silben ein Vokal eingeschoben
werden muss.
Nach dieser Kegel werden auch die Endvokale der
Prapositionen in der Composition behandelt, daher wird:
ap. pari' zu par-y vgl. palez aus ^pardcZf s. p. 123;
ap. para- (in paraitd, poraidiy, pardgmata, parabrtam)
zu par-, vgl. Horn Nr. 292 fig.;
ap. pati- zu phi. pat-^ pa- = np. pai-, pa-, vgl. phi.
patkar = np. paikar; phi. pacen = arm. patcen;
np. pasand u. s. w. ;
ap. tipari- zu phi. *upar, apar = np. bar-, vgl. Horn
Nr. 210; oben p. 28;
ap. tara- zu phL np. tar-, vgl. Horn Nr. 381;
ap. abi' (= atvi-) zu phi. a/-, aw-^ np. a/, av-, vgl.
```


## [2026-09-04T18:41:03.479Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\npython3 $S HRN.txt \"279\\. pälez\" 21 | head -3\npython3 $S HRN.txt \"594\\. deg\" 21 | head -3\npython3 $S HUB.txt \"palez aus\" 10 | head -3\necho \"== HUB p123 area\"\npython3 $S HUB.txt \"pard[eēc]z|pardcz\" 10 | head -20"
}
```


### [2026-09-04T18:41:05.346Z] TOOL RESULT

```
--- leaf 84 = printed p.63
   ... — 63 — 279. pälez 'Garten (Sahn. I, 73 Vers 207) ^), palezhan, arab. LW. faliz, ap. nagdÖHöog; aw. pairida^za-, LW. kurd. päres, arm. partez, syr. Dn*)5?, JDD'^'TlEi. 280. panzde 'fünfzehn , vergl. pänsed 'fünfhundert'. aw. paücadasa 'fünfzehn; skr. pdflcada^a; phlv. pancdahion, kurd. [daupe/ij etc.]; paiizde (LW.); afy. pinjalas; oss. d. findtäs^ t. findfäs (292) ; bei. panzda (LW.). 281. päl^ pä Tuss ; vergl. pa
--- leaf 153 = printed p.132
   ... '-Aussehen; -sehend*. Der r- Vokal ist hier durch e vertreten, wie in heSe (No. 256). Aw. daesa- (yt. 13, 104), das Darmeste- ter als *Traum' nimmt, ist zu unsicher, um ver- glichen werden zu können. 594. deg *Topf*, vergl. dez, deze, phlv. deg 'Topf; lat. figulus^) Töpfer*; mhd. tigel^ tegel, ahd. tegal 'Schmelztiegel*, an. diguU 'Tiogcl*. LW. kurd. dizik; af/. deg^ decka; bei. deg, dez, dPd, Oegci (59); wa/. dlg^ sar. deg. Zu ai. \/'deh', degdhi 'bestreichen, kitten', got. deignn 'kneten, aus Thon formen*. 595. dlger, dediger (Vis und Rämin, S. 29 V. 5 v. u.)^) anderer ; sidlger^ süHg ein Drittel* (
--- leaf 134 = printed p.124
   ... r iiberhaupt nach uberlangen Silben ein Vokal eingeschoben werden muss. Nach dieser Kegel werden auch die Endvokale der Prapositionen in der Composition behandelt, daher wird: ap. pari' zu par-y vgl. palez aus ^pardcZf s. p. 123; ap. para- (in paraitd, poraidiy, pardgmata, parabrtam) zu par-, vgl. Horn Nr. 292 fig.; ap. pati- zu phi. pat-^ pa- = np. pai-, pa-, vgl. phi. patkar = np. paikar; phi. pacen = arm. patcen; np. pasand u. s. w. ; ap. tipari- zu phi. *upar, apar = np. bar-, vgl. Horn Nr. 210; oben p. 28; ap. tara- zu phL np. tar-, vgl. Horn Nr. 381; ap. abi' (= atvi-) zu phi. a/-, aw-^ np. a/, a
== HUB p123 area
--- leaf 270 = printed p.260
   ... Ua 'Klage* = phi. gilak, ap. "^grdor- = zd. gereza- (siehe § 110). Der Uebergang von rd in / fand in sassanidischer Zeit statt; das altere (arsacidische) Pehlevi hatte noch rd, wie arm. partBz (fiir *pardez), sard und vard bezeugen. Man beachte auch rd in arm. Vardan = lat. Vardanes (Tacitus), gr. OiaQSdvriq\ arm. kaxard 'Zauberer = zd. kax^areda-. Ap. ard = np. dl; ap. fd nach Labialen = np. ul, sonst = np. il, vgl. § 9 und 34, a und b. § 158. Ap. rs = np. s. Der Schwund des r in der Lautgruppe rS trat schon im Pehlevi ein, wenn rs vor Eonsonanten {t, n, v) stand, erfolgte aber erst in sassani- dis
```


## [2026-09-04T18:41:09.905Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[133][:3000])\nEOF"
}
```


### [2026-09-04T18:41:11.313Z] TOOL RESULT

```
- 123 -
phi. sardar (s. p. 124 Anm.) ; suvdr *Reiter , nach Vullers auch
asvdr = phi. asbdr (siehe oben p. 77) = ap. asabara- (=
"^asawdra- aus "^aspabara- ; astar 'Maulesel' = ap. *asatara'
SLMs'^aspatara- = skr. agvatara- (aber arm. aspet Sius*as(pa)'
pati'), sahryO/r *Herrscher*, phi. (geschrieben) satrd(a)ran
(plur.), ap. '^xSad^'a-dara- ; gireban *Kragen = phi. grivpan
'Halsberge\ zd. grJva + *pana-^ arm. denpet ^) 'Oberhaupt
der Religion (EliSe) = zd. daena + paiti-.
Ausfall von i und u: zaryCm gelbfarbig* = zd. zairi-
gaona- ; zanbar *Sanfte* = arm. zanuar = zd. "^jainibara- ;
polnz 'Garten = hebr. pardes (Hohelied), arm. partBz^ zd.
pairidaeza-, gr. nuQadsKJog; dihgdn (arab. diliqan) Xand-
edelmann, Bauer , arm. dehkan, vgl. paz. dehvad Xandesherr'
= arm. dehpet (EliSe) = zd. danhupaiti- ; marzban *Mark-
graf, phi. marzpdn, arm. marzpan; mobad == syr. NtCSIQ
(um 400 p. Chr.), gr. ^Mavmrdg BB. 4, 59, arm. movpet
Elise 124, 4 v. u. etc., phi. maupat BB. 4, 59, alter arm.
mogpei EliSe 11, 1. Z. etc., phi. tnagupat Haug, Essay
p. 72 etc. (gesprochen moypet), ap. *magupati-.
Ebenso in Fremdw5rtern und Eigennamen: kdlbitd
*Modeir = paz. kctlbud, phi. kalput = gr. ycalonodiov', Bay-
dad (Stadt) = zd. bayodata- 'gottgeschaflfen* ; sassanid. Hor-
mizd = arm. Ormizd, alter 2J:m,Aramazd --= ai^,A(h)uramazda ;
phi. Nar8ah(f)f syr. Narse, gr. Nagoijq^ arm. Nerseh, vgl.
zd. nairyosanka-, skr. pardfjqsa-; Isfandyar entstellt aus
hfandydd = phi. Spandydt, arm. Spandiat^ zd. spenfoddta-
(obenp. 107); Mlldd (Marquart bei Noldeke, Pers. Stud.
n, 31) aus "^Mihrddt = arm. Mihrdat, lat. Meherdates, gr.
Mid-Qiddrtjc; etc., ap. *Midraddta-; BddySs {Bddyi^s) = phi.
vdtges *6egend ostlich von Herat* Bdh. Gl. 254 , arm. Vatges,
zd. vditigaesa-j etc.
*) Die Komposita mit -pet *Oberhaupt' haben im Armenisohen
meist den Kompositionsyokal a, z. B. dpr-a-pet = phi. ^dipxr-pat (skr.
LW. divirapati-), Mit -pet werden iibrigens (wie mit -pan^ -panah
*hutend') auch neue armenisohe Komposita gebildet, die aUe den Kom-
positionsyokal a haben.
```


## [2026-09-04T18:41:19.014Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\npython3 $S FVQ_pages.txt \"Firdaus|firdaus|Firdaws\" 17 | head -20"
}
```


### [2026-09-04T18:41:22.107Z] TOOL RESULT

```
--- leaf 18 = printed p.1
   ...  Mfisa, Daw (id, Sulaiman, Nuh, 'Isa, are well- known Biblical characters. So also the place-names Babil, Rum, Madyan, Saba', and many of the commonest religious terms Shaitan, Tawral^ Injll, Sakina, Firdaus, Jahannam, are equally familiar to all who know the Jewish and Christian Scriptures. So one is not surprised 1 Convincing proof of this is found in the .statement of the Prophet quoted in Yaqut, Mu'jatn, iii, 664, to the effect that on a certain occasion he sacrificed a ewe to 'Uzza, which he excuses on the ground that at that time he was following the religion of his people. 2 Sura, liii, 10, 20
--- leaf 240 = printed p.223
   ... UR'AN 223 whence the Gk. 'EtvaTrjs. From the Akk. come the Heb. IVIS and Syr. 2;2>, whence in all probability the Ar. Ol^, if indeed this was not an early borrowing from Mesopotamia. J x- . ^ ) }j-$ (Firdaws). xviii, 107 ; xxiii, 11. Paradise. The authorities are agreed that it means a garden jbL*j ( Jawhari, Sihdh, i, 467 ; LA, viii, 43), but they differed considerably as to what sort of a garden it means. 1 There are also divers opinions as to its precise location and significance as referring to the celestial Paradise. It was early recognized as foreign (Siddiqi, Stidien, 13, and note Fraenkel's r
```


## [2026-09-04T18:41:25.052Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ni=t[240].find('Firdaws')\nprint(t[240][i-100:i+2600])\nEOF"
}
```


### [2026-09-04T18:41:26.968Z] TOOL RESULT

```
obability the Ar. Ol^, if indeed this was
not an early borrowing from Mesopotamia.
J x- .
^ ) }j-$ (Firdaws).
xviii, 107 ; xxiii, 11.
Paradise.
The authorities are agreed that it means a garden jbL*j ( Jawhari,
Sihdh, i, 467 ; LA, viii, 43), but they differed considerably as to what
sort of a garden it means. 1 There are also divers opinions as to its
precise location and significance as referring to the celestial Paradise.
It was early recognized as foreign (Siddiqi, Stidien, 13, and note
Fraenkel's remark, Fremdw, 149), though some claimed that it was
genuine Arabic derived from \^*>J* meaning widih or amplitude?
Some said it was Nabataean, 3 where the reference is possibly to
the OTIS of late Jewish legend. 'Ikrima held that it was Ethiopic, 4
and many said it was Syriac, 5 but the favourite theory among the
philologers was that it was of Greek origin. as-Suyutl, Itq, 323 ; Muzhir,
i, 130, 134, gives this as the prevalent theory, it is given by al-Jawaliql,
110 ; ath-Tha'alibl, Fiqh, 318 ; and al-KhafajI, 148, and we learn
from the Lexicons (cf. LA, viii, 44) that it was supported by such
authorities as az-Zajjaj, Mujahid, Ibn Slda, and al-Kalbi.
Obviously ^l^J* represents the Gk. Trapadticro?, and on the
ground of the plu. u^J* G. Hoffmann 6 would derive it directly
from the Greek. It seems, however, merely a coincidence that this
1 Lane, Lex, 2365 ; and Tab. on xviii, 107.
2 Vide Qamus, sub voc. ; LA, viii, 44 ; TA, iv, 205. This was the theory of
al-Farra' and it was supposed to be supported by the fact that it occurs as a name
for Damascus. The verse of Jarir quoted in Bekri, Mu'jam, p. 368, is post-Islamic,
however, and doubtless influenced by the Qur'an.
3 as-Suddi in al-Jawallql, Mu'arrab, 110.
4 Bagh. on xviii, 107.
5 Qamus, sub voc. TA, iv, 105, and al-Jawaliqi.
6 ZDMG, xxxii, 761, n. ; Lagarde, GA, 76 and 210 ; Pautz, Offenbarung, 215, n. ;
but see A. Miiller in Bezzenberger's Beitraye, 280, n.
```


## [2026-09-04T18:41:30.413Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[241][:2600])\nEOF"
}
```


### [2026-09-04T18:41:32.187Z] TOOL RESULT

```
224 FOREIGN VOCABULARY OF THE QUR*AN
plu. form (which is not uncommon in borrowed words, e.g. (J
JL>^r ; j^ju>-, etc.), is so close in sound to the Greek word, and it is
unlikely that it came directly into Arabic from Greek.
The original word is Iranian, the Av. .ut^jjyj^g) pairidaeza,
which in the plu. means a ' ' circular enclosure ". 1 Xenophon introduced
the word into Greek, and uses it of the parks and gardens of the Persian
Kings, 2 e.g. ^fwo6,i,ii,7,etc. After this date it is used fairly frequently,
and in the LXX is sometimes used to translate ]3 or ]HS? ]3. But
it was also borrowed into other languages. 3 In late Akk. we find
pardisu,* and in Heb. OTIS a park or garden, also in Aram, the
KO*mD of the Targums, and Syr. Im^jja commonly mean
garden and are of Iranian origin, 5 like the Arm. i^u
Tisdall, Sources, 126, thought that ^S^J* was borrowed from late
Heb., but in the sense of Paradise it is very rarely used in Heb. 7 Its
origin is almost certainly Christian, and probably Syriac, for \Vb*->\Z>
was very commonly used for the abode of the Blessed, and could
easily have been learned by the Arabs from the Aram, speaking
Christians of Mesopotamia or N. Arabia. 8 Vollers, ZDMG, 1, 646,
suggests that possibly the plu. form ^O'^* was the form that
was borrowed, and ^i^J* later formed from this.
It was a pre-Islamic borrowing, and possibly occurs in the
Thamudic inscriptions. 9
1 Bartholomae, Al W, 865 ; Haug, Parsis, 5. It survives in Mod. Pcrs. jJL garden
(Horn, Grundriss, 279), and Kurdish y j garden, (cf. Justi, Die kurd. Spiranten, 29).
3 This makes it the more strange that Lidrlell and Scott should have considered
the word Semitic.
a Telegdi, in JA 9 ccxxvi (1935), p. 250.
4 ZA, vi, 290. On the suggested Semitic origin of the Avestic word, see Delitzsch,
Paradies, 95, 96, and Noldeke thereon in ZDMG, xxxvi, 182.
5 The Syr. )l2UXL};2>, besides Arm. u^uifiin[i^u^iulj and Pers. ^IjjJi* f r
gardener, is conclusive evidence of the Iranian origin, ^L, being the Phlv.
panak, a protector, or keeper (Horn, Grundriss, 176 ; Nyberg, Glossar, 169).
6 Hiibschmann, Arm. Gramm., i, 229 ; Lagarde, Armenische titudien, 1878.
7 As Horovitz, Paradies, 7, notes. Cf. also Schaeder in Der Islam, xiii, 326.
* Horovitz, Paradies, 7 ; Grunbaum, ZDMG, xxxix, 581 ; Geiger, 48 ; Fraenkel,
Vocab, 25 ; Sacco, Credenze, 163, n.
9 DT1S, cf. Littmann, Entzifferung, 43.
```


## [2026-09-04T18:41:40.624Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\necho \"=== PLA firdaus\"; python3 $S incoming/PLA/PLA_pages.txt \"firdaus|Firdaus|firdaws|pairidae\" 15 | head -30"
}
```


### [2026-09-04T18:41:42.311Z] TOOL RESULT

```
=== PLA firdaus
--- leaf 221 = printed p.206
   ... na                 4  am» - farha:              "junge          Henne"                  pers.c&,          parpahn          ?.   ar     - firdus:;              "Paradies"                a.             pairidaeza          "kreisförmig,            rund"      °—     mp.          abo       paliz           6, ap.         pairidaida             7,         Paradies           kommt           in Farfard’3               Mal       u.   in Bundahiän             18 Mal    vor.     Es     besteht       aus dem Präfix pairi "um" + daeza "füllen",                                                    syr.    IL Y%, ®, ma
--- leaf 292 = printed p.277
   ...  Moin,      M.:    Farhang           Moin,      4 Bde.,       Teheran          1963.   Moinfar,        M.:     Le    vocabulaire        arabe     dans         le    Livre     des     Rois        de   Firdausi,          Wiesbaden           1970,   Moser,     Charles:            Dictionnaire        encyclop&@dique              Francais-Allmand                  et     Allmand-          Francais.           Premiere       Partie      Frangais-Allmand,                Berlin         1961.   Muntasir,        SAbdalhalim,             Ibrähim       Anis:      Mu°gam       al-Wasit,             2 Bde.,        1
```


## [2026-09-04T18:41:45.116Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ni=t[220].find('firdus')\nprint(t[220][max(0,i-300):i+2200])\nEOF"
}
```


### [2026-09-04T18:41:46.645Z] TOOL RESULT

```
rs. _G peykar                 SP     Io    patkar   ap.
      patikara         2, mand.              patkara     3, ar.       Lw.      fatkar       .


amp)» - faräßin:                 Pl.     v. .„o> farfin q. v.

$l>-          faräp: eine Stadt °.

>)’          - farädis:          Pl.     v. or,» firdus              q. v.

Or»          - faräzadaqg:            Pl.     v. c3%5     farzadag            q. v.


ar)» - faräzin:                  Pl.     v.    cr       farzin g. v.

s “
PA  ls ; -          zZatn
                farastük: .           0" "Schwalbe "     pers.               “
                                                                             Sun     parastu
                                                                                            -
                                                                                                 mp.
                                                                                                                 -,
                                                                                                         paristöog
                                                                                                                      6
                                                                                                                          .


zb       -     faräsih:       Pl. v. >            farsah a. v.

>):          - farafir:          Pl.     v.    „5, farfur        q. v.


Grels
 ls   -- farämin:     Pl v. ol.»> £ farmän q. v.
           farämin: Pl.

ol-           faranig:        "Führer,          Leiter"        pers.               als,   parwäna   — mp. sr po
      parwanak         7, syr.           Iw.    Bas,           mand.         paruanga       °.

>12          - faränid:          Pl.     v. »> farand           q. v.

Ge»          - farbiyün          = farfiyun            q. v.



1.   Addai      Scher       s.     v.
2.   Mayrhofer         S.     139.
3.   Macuch      s,    v,
4,   ebda.
5.   Yaqut      Bd.    3 S.        885,       Nyberg     Bd.    II     ss.    v.
6.   Mackenzie         S.     v.
7.   Nyberg      Bd.     II      s.     v.
8.   Macuch      s.    v.
```


## [2026-09-04T18:41:49.329Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ni=t[221].find('firdus')\nprint(t[221][max(0,i-800):i+2400])\nEOF"
}
```


### [2026-09-04T18:41:52.085Z] TOOL RESULT

```
firsär                                                                   207                                                     farzän


                                                                                           1
„les -       £irfär:           "Zirkel"                     pers. „U, pargär                   “.

lb;      - firßärid = firfär q. ve °.


Ssb> - firdäri:                     "mit         dem Zirkel             gemacht"-

I      - farfin:               "Zaun"            ” pers.          un. 3 mp.                yo) pargän             "Wand,      Mauer"
      <       *pari-kana                 4

am» - farha:              "junge          Henne"                  pers.c&,          parpahn          ?.


ar     - firdus:;              "Paradies"                a.             pairidaeza          "kreisförmig,            rund"      °—     mp.
         abo       paliz           6, ap.         pairidaida             7,


      Paradies           kommt           in Farfard’3               Mal       u.   in Bundahiän             18 Mal    vor.     Es     besteht
      aus dem Präfix pairi "um" + daeza "füllen",                                                    syr.    IL Y%, ®, mand.
      pardisa,            bab.       pardisu             9, hebr.         oı79!0,
      aw.    pairidaeza                  >>griech.                paradeisos,           frz.        paradis,      engl.       paradise,
      dtsch. Paradies !!.
      Paradies:               "der       rund       eingefaßte            Garten;          Tierpark         reicher     Perser"        T_ pers.
      griech.           >lat.              12,
      paradiesisch:                  "himmlisch"                  pers.            >    griech.           >lat.       13,
      Paradeiser:                  (österr.)             "Tomaten"            pers.            >> griech. >            lat.     14,

                                                                                               15
ob     - farzän:               "die        Königin           im    Schach"         pers.            s.    farzäna



     Wahrmund           Ss.    v.,       Dozy       s.      V.
     ebda.
     Muhit     s.       v.,        Addai         Scher       s.    v.
     Nyberg        Bd.        II    s.    v.
     Bartholomae               AIW       S.      865.
     Horn     Grundriss              S.       279      n.    Jeffery          s.   v.
     Mayrhofer            S.       137..
     Brockelmann               s.    v.
     Macuch        S.    v.
      Ellenbogen               s.    v.
      BQ.     s.    v.
      Fremdwörterbuch                      Ss.    v.
      ebda.
      ebda.
      Wahrmund
            s. v.
```


## [2026-09-04T18:41:59.140Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"الفردوس\\|فردوس\" AFM_pages.txt | head -10\necho \"=== dig\"; grep -n \"الديك\\|الديگ\\|ديگ\" AFM_pages.txt | head -10\necho \"=== faliz\"; grep -n \"فالیز\\|الفاليز\\|فاليز\" AFM_pages.txt | head -10"
}
```


### [2026-09-04T18:41:59.214Z] TOOL RESULT

```
=== dig
1770:+ (الديك) 3 بالاثافي ܙ ܐܝܐ ععنى ديك افاسي وهو القدر
=== faliz
```


## [2026-09-04T18:42:03.785Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1765,1778p' AFM_pages.txt\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\npython3 $S AFM_pages.txt \"الديك\\) 3 بالاثافي\" 8 | head -5"
}
```


### [2026-09-04T18:42:05.578Z] TOOL RESULT

```
ومما ܨ
* (الدولة ) الداهية وهي لغة في 15 عن اطوهري بال جاء | الدهر ¥ ته
وتولاته اي بدواهيه تعر بب دوله ومعناهما لكر وان ܐܨ الذي تتنشاءم به
العامة قائلة انه عبارة عن الداهية والموت فأطلق `
(الداماً ) 0 قبل ® والاصح 5 5
+ (الديك) 3 بالاثافي ܙ ܐܝܐ ععنى ديك افاسي وهو القدر
عد (الد رين والديانة » المعتقد والمذهم خرن 3 ن الفارسي 50 المعتقد
ويطلق ايضاً على ملاك كان موكلا على حافظظة العالم: وعلى اليوم الرابع والعشر.ين من
كل سهان الذى كان فيه الفرس يرساون اولادهم الى المدرسة ويزوجون و يتزوجون٠‏
وقالتث فيه العرب دان ودين الى غير ذلك 20 :0 1 ,)ܟ 58
ܐܐܐܠ 62020 الذى 36“ 3[ ܐܐܬ أن علخ المكم 810 فهو 1533 من
السريالي. كن 5 500 ܨ )ܪ الارمني ® أي لمكم واليونالي دبز أي
القصد والفكر
5 الثيء علمة وفقه به وذّبر اككتاب كتبة قريب < ومعنى من
--- leaf 70 = printed p.62
   ... داهية وهي لغة في 15 عن اطوهري بال جاء | الدهر ¥ ته وتولاته اي بدواهيه تعر بب دوله ومعناهما لكر وان ܐܨ الذي تتنشاءم به العامة قائلة انه عبارة عن الداهية والموت فأطلق ` (الداماً ) 0 قبل ® والاصح 5 5 + (الديك) 3 بالاثافي ܙ ܐܝܐ ععنى ديك افاسي وهو القدر عد (الد رين والديانة » المعتقد والمذهم خرن 3 ن الفارسي 50 المعتقد ويطلق ايضاً على ملاك كان موكلا على حافظظة العالم: وعلى اليوم الرابع والعشر.ين من كل سهان الذى كان فيه الفرس يرساون اولادهم الى المدرسة ويزوجون و يتزوجون٠‏ وقالتث فيه العرب دان ودين الى غير ذلك 20 :0 1 ,)ܟ 58 ܐܐܐܠ 62020 الذى 36“ 3[ ܐܐܬ أن علخ المكم 810 فهو 1533 من السريالي. كن 5 500 ܨ )ܪ الارمني ® أي ل
```


## [2026-09-04T18:42:16.162Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nfor w in دیوار دژ پالیز پردیس دیگ فردوس دیز; do echo \"### $w\"; grep -c \"$w\" ARY_pages.txt; grep -n \"$w\" ARY_pages.txt | head -3; done"
}
```


### [2026-09-04T18:42:17.762Z] TOOL RESULT

```
### دیوار
9
218:همین علت است که نقش‌های دیواری یافت شده در تورفان و تارم آنها را با موی سرخ و چشمان آبی
700:ایرانی را نشان می‌دهد. گورهای آذربایجان (مثل کورگان‌های اوکرائین) دارای دیواره‌ی چوبی بوده
1284:31۸ (به معنی دیوار)» در آلمانی کهن شده است 7810 (به معنی خمیر)؛ در یونانی شده است
### دژ
4
1283:مثال دیگر: هند و اروپایی 01781017" در فارسی نوین شده است «دژ» در سانسکریت شده است
8180:دش دز (به چم "ید" مثلاً در *دشوار" با *دژخیم) / ۲۷۹
8585:چم‌های برخی از واژه‌های این فهرست: دژ) تهه‌ی شنی» تهه؛ وزیدن» شهر؛ ناحید
### پالیز
2
4469:۴ _/ پالیز» فالیزء جالیز» پردیس (به چم
4489:فارسی (2885]4۸): پالیز, فالیز, جالیز, پردیس (به چم "باغ" ابوستان)
### پردیس
3
4469:۴ _/ پالیز» فالیزء جالیز» پردیس (به چم
4489:فارسی (2885]4۸): پالیز, فالیز, جالیز, پردیس (به چم "باغ" ابوستان)
4513:۱- افردوس "نیز معرب "پردیس" است.
### دیگ
133
87:معتقد بودند که گهواره‌ی آریایی‌های ابرنژاد شمال باختری اروپا بوده و از آنجا به سرزمین‌های دیگر
92:به عبارت دیگر» نازی‌ها واژه‌ی «آریایی» راکه قبلاً په خانواده‌ای از زبانها اطلاق می‌شد به
106:نژاد برخی از آنها سفید و برخی دیگر هندی و بفیه افریقایی است. اکثر مردم کشور پرو از نژاد سرخ
### فردوس
3
1086:‏بررسی قهرمانان حماسه‌های هومر و فردوسی و ورجیل (۷180112) و همچنین اسطوره‌های .|
4513:۱- افردوس "نیز معرب "پردیس" است.
4516:۳ چم.این واژه در همه‌ی زبان‌های غبر ایرانی این فهرست "بهشت"» افردوس" است و ضنناً همه از زبان فارمی
### دیز
1
11288:7۸ ادها دیزی دانمارکی (0۸(/]82): 58 ,8670
```


## [2026-09-04T18:42:21.381Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '4460,4525p' ARY_pages.txt\necho \"=== 1278-1292\"\nsed -n '1278,1292p' ARY_pages.txt"
}
```


### [2026-09-04T18:42:21.450Z] TOOL RESULT

```
5
یونانی (075520): ناند ۱۱۸۸ رومانی ((1۸لهلال۸). 2۸
لائین (770با). ایسلندی‌کهن (1۵0 210۸ید صضام).
0 ۶5 ,ات۳۸۲ خ۸اق7۸
فرانسه (1ح)(۳2): ۱۸3 نررس کهن (۸088 2ا0). ۲۳۵۸
آسپانیایی (8۳۸(//3/7). قا ها سا کسرنیکهن (/54200 0ا0):
ایتالیایی (۸۸اه1/): ادا ۱ رالشآنآ۸70 ,۸1
یمور ۱
[pdf page 153]
۴ _/ پالیز» فالیزء جالیز» پردیس (به چم
فریزی کهن ((۳8/514): #لشآ ۲ بش71 ایرلندی کهن (87ل17 2ا0): 11
آلمانی کهن (08721404 04اب )+ 8
501 پسگشت‌ها ۲ آشک رت دا
آلمانی (08794/(0): ۳1 :۶۵00 1
انگلیسی کهن (8۸/01380 ۰:0۵ ۴8۲۸ 4 (ا۴۴5) 7
انگلیسی (8ا/۵: اد داد ناسنا ِ نا
دانمارکی (0۸(/757): 80 9 (585) :0705
هلندی (ع7ا0): ۷۵8 (ا5ظ۲۴) +347
اسلاوی کهن 7ل0(0376 ملک (0). 81 :که #متتمهد
ت۴۸ ,2۸11 برهان قاطع : ۳۵۹
روسی (/#5514): ۳۸33۴ ,887-8۸817 فرهنگ معین : ۰ ۶۸۰
بلغاری (ا#ملمه.الاه: ۲۸۷ لغت‌نامه دهخدا: ۵۳۸۸
صربی (587814۷): ۳۳ 0
یادداشت:,
۱ معنی این واژه در اپرلندی کهن: کف دست.
۲ معنی این واژه در زبان‌های ژرمنی: احساس کردن» پرماسیدن,
۳- واژه‌ی "پرماس ""پرماسیدن (پهلری: ۳۸188۸8) به چم "با دست احساس کردن" نیز به احتمال ضعیف با این
واجريشه خویشی دارد.
۴ واژه‌ی لاتین ۳01183 به چم اانگشت شست" نیز از همین ربشه است.
فارسی (2885]4۸): پالیز, فالیز, جالیز, پردیس (به چم "باغ" ابوستان)
اوستایی (4ل۸874): ۳۸۸۸ لانین (7700ضا): 05
پارسی باستان (۷مماق۴8۴ صاه): فرانسه ‎ :)۳88(/601(‏ 5
۳105 اسپانبایی (52۸/187): ۳0
کردی (70154): 7 ,8855 ایتالیایی (۸۸لم17): 50
سانسکریت (54۸/58/7): آ۹۳21+05178/1 رومانی (8714۸۸۵/4): ۳5
ارمنی (/448014): 8۸82082 ۳۸752 پر تغالی (۳07701582): زان ات اما
بونانی (0۸54): آلمانی (/05701۸2): ۳5
5 ,۲۸۹08018085 انگلیسی کهن (4ل8الا800 ص۵): ۰8۸۸0188
۹
[pdf page 154]
ی
پانزده / ۱۵۵
انگلیسی (57/.ا8۸0): ان 21 ۱ پسگشت‌ها 5
دانمارکی (0۸/]57): ۳15 10244 ۶0/0700
سوئدی (8175213/7): ۳5 :وچمه
نروژی (0/0750140: نز نا 7 (۳381) ,754 (۳۸330198)
ملندی (ع07): ۳/5 49041 ((0۸308) تاه
: 8 ۳۸۵۵۶۵) +7
9 (۸3050ج) ۸40
فر هنگ معین : ۶۸۰
برهان قاطع + ۳۹
لغت‌نامه دهخدا: ۹ ۵۳۹۵
بادداشت.
۱- افردوس "نیز معرب "پردیس" است.
۲- واژه‌ی اوستایی از دو اجريشه درست شده است: ۳۸13 (به چم "دور" و "پیرامون") و 3۸122۸ (به چم "آدیوار»)
(بازگشت به: دیوار)
۳ چم.این واژه در همه‌ی زبان‌های غبر ایرانی این فهرست "بهشت"» افردوس" است و ضنناً همه از زبان فارمی
گرفته شده‌اند.
اوستایی (4۷87420): 0/۸۸ فرانسه (۳822/074): 05
پهلری (الاماتنمه): ۰ - اسپانیایی (62۸/۷18): 0
. ۶۵۹۷20۸۲ , 8۸۷۲0۸73 ایتالیایی (4(۷ )+ 0010
1 اوستی (0548716): 8 رومانی (/۸/۸/4۸): 0۳087832808
کردی (ب5اصنم: نا پرتغالی (007001895): ۱
بلوچی (171ع/8۸): ۳0۸ 0 05040
۱ افغانی (پشتر) (//4208۸۸): 8شت۳۸۷[۸ گرنیک (00727/0): ۳1
۱ سانسکریت (854۸58277): ۰ ۳۸۳۸۸۳۸ ایسلندی کهن (14(1/ 5001010 052):
=== 1278-1292
نج
۱ دیباچه / ۴۷
سانسکریت شده است 8۸121071 (به معنی توانستن)» در ایرلندی کهن شده است 20177 (به معنی
قدرت). پکرنی (522 ,۳0۳0۸۲9) معتقد است که شاید واژه‌های انگلیسی 11۸7277 و آلمانی
(به معنی هستی دادن و پا روی تخم نشستن و جوجه آوردن) نیز از همین ريشه باشند.
مثال دیگر: هند و اروپایی 01781017" در فارسی نوین شده است «دژ» در سانسکریت شده است
31۸ (به معنی دیوار)» در آلمانی کهن شده است 7810 (به معنی خمیر)؛ در یونانی شده است
58 ب(به معنی کِل)» در ار منی شده است :0332 (به معنی توده). البته تعیین معنی واژه‌های
امروزین نسبتاً آسان است ولی هر چه عقب برویم تعبین معنی دشوارتر و آمیخته با ابهام بیشتری
می‌شود. لذا در این کتاب تاکید روی ردیابی واژه‌های فارسی تا سرچشمه‌ی هند و اروپایی آنها و
همچنین نشان داد خویشی واژه‌های فارسی با واژگان سایر زبانهای هند و اروپایی است. سعنی
واژه‌های مختلف فقط در برخی موارد صرفاً به منظور نشان دادن برخی جنبه‌های معنایی واژگان هند
و اروپایی آورده شده‌است.
۲-مراجع متعدد این کناب هر یک برای نشان دادن املا و آوای واژه‌ها از نشانه‌ها و حروف
متفاوتی استفاده می‌کنند. در این کناب کوشش شده است تا حد امکان املای واژه‌ها یکدست بشود.
```


## [2026-09-04T18:42:33.727Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n \"DHEIGH\\|DAEZA\\|PAIRIDAEZA\\|DIDA\\|DIZ\\b\" ARY_latin_index_pages.txt ARY_pages.txt | head -20\necho \"=== headword lines with divar\"\ngrep -n \"دیوار\\|دیوارها\" ARY_pages.txt | sed -n '1,20p'"
}
```


### [2026-09-04T18:42:33.794Z] TOOL RESULT

```
ARY_latin_index_pages.txt:1253:eh oh ey Stl 52 can Cal 98S yy. 9 gos y9 DHEIGH oly} y ua: Sa dle
ARY_latin_index_pages.txt:4392:PARADISUS (LATIN) 3 PAIRIDAEZA H(AVESTAN) glen!
ARY_latin_index_pages.txt:7057:ve" CACHINNATION, CACHINNATE XANDAK, XANDIDAN, XAND-
ARY_latin_index_pages.txt:7975:DIDA —._ (OLD PERSIAN) slut go 4 UZDAEZA, -DAEZA :(AVESTAN) .ykt5\
ARY_latin_index_pages.txt:7978:DEG (SWEDISH) $4 y+ DIZ APAHLAVD) 5 Jy
ARY_latin_index_pages.txt:7985:. DIDA (OLD PRUSSIAN) 35 +3. Mic. LATIN)
ARY_latin_index_pages.txt:7994:(DOUGH) 180, (DHEIGH) 753 (OLD ENGLISH) 9S efit
ARY_latin_index_pages.txt:8167:TAND SWEDISH) ity DIDAN, DINDAN (KURDISH) 52,8
ARY_latin_index_pages.txt:8519:DIDAN, DITAN>, 3 «PAHLAVD 5h |
ARY_latin_index_pages.txt:8573:ZED x(CZECH) So DAEZAYEITI HAVESTAN) leu
ARY_latin_index_pages.txt:8574:mp SERBIAN) «y no DIDA (OLD PERSIAN) jem 554
ARY_latin_index_pages.txt:12761:a VRATITI, VRUTETI GARDIDAN, GARDANIDAN,
=== headword lines with divar
218:همین علت است که نقش‌های دیواری یافت شده در تورفان و تارم آنها را با موی سرخ و چشمان آبی
700:ایرانی را نشان می‌دهد. گورهای آذربایجان (مثل کورگان‌های اوکرائین) دارای دیواره‌ی چوبی بوده
1284:31۸ (به معنی دیوار)» در آلمانی کهن شده است 7810 (به معنی خمیر)؛ در یونانی شده است
4514:۲- واژه‌ی اوستایی از دو اجريشه درست شده است: ۳۸13 (به چم "دور" و "پیرامون") و 3۸122۸ (به چم "آدیوار»)
4515:(بازگشت به: دیوار)
8169:۱ بازگشت به: دیوار. :
8170:۲ چم این واژه در زبان‌های ایرانی باستان و یرنانی؛ دیوار,
8739:دیوار /] ۲۹۷
11282:چم این واژه در انگلیسی کهن و انگلیسی نوین: تاقچه» شکاف دیوار..
```


## [2026-09-04T18:42:37.358Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '8730,8790p' ARY_pages.txt\necho \"=== 8140-8180\"\nsed -n '8140,8180p' ARY_pages.txt"
}
```


### [2026-09-04T18:42:37.416Z] TOOL RESULT

```
ایتالیایی (۵(۷ال7۸): 210 ایرلندی کهن (570ل12 صا0): 0۸

رومانی ((۵ا ۸1۸2 ): [ا78 گالی (0703[7): -080

پرتغالی (۳071001858): نراد . ولزی (58977): 12

ایسلندی‌کهن (0100/40/هشی5 صا0): برترنی (88870/0): 001
3 أ
[pdf page 296]
دیوار /] ۲۹۷
پسگشت‌ها مرت ی 3 (05770) +57
زا 8 ننک مه
2 (018) :ما05 0 ((0810) 0
0 ((0510) :8 ۲۵(/2 ۸۸ برهان قاطع : ۹1۷
3115 لاه
یادداشت: له پم
چم این واژه در همه‌ی زبان‌های این فهرست: خلل
۲- هلت دگرگرنی چم این واژه در زبان‌های ایرانی این است که پس از ظهور زرتشت و آئین او "آهورامزدا" مورد
پرستش قرار گرفت و واژه‌ی "دی" چم کنونی خود را به دست آورد.

اوستایی (487۸4۸): ابا 23 چکه (280[4): زان ما
پارسی باستان (۲8۸۵(۷ صا0): ۰ 8010۸ صربی (5888142۷): 20
پهلوی (۲7ماللهه): 3 در بوهمی (80/78141421): 20
کردی (60870184): 3 ری لیترانی ((فتبیسانت ۰:5 22118027310۰ ۱
افغانی (پشتو) (//4۳0/۸): داد پروسی کهن (7ل۲3/5514 010):
تخاری ۸ (۸ 10/7۸74(۷): زک ادن با دادن
تخاری 8(8 ۷( 70724۸): ی انیا ایركدی کهن (بزونم/ 2ا0): 00۱100۰016
ساننکریت (5(/80/7): 08731۰ ,10132
ارمنی (494ا۸/04507): - 3233 پسگشت‌ها 0/5
بونانی میم همست فموه که 20000
آست پا ۳105 :ما05
لاین «ورتشم: :313۲088 ,31۸00 دک (72282۵ ها ۲۸۳۵۲۲۵۵)
گرنیکد (007[71۳): " زال نی زا 9 (ل۲۸) :۸/218
۱ اسلاوی کهن (۷ها5 نالا 0 47243 ما8
۱ : دار 7 (لت۲۸) ۸۸102۵0
۱ بادداشت:
۱ بازگشت به: دژ
۱
[pdf page 297]
۸ راست ‏
۲ چم این واژه در نخاری و لاتین: شکل دادن» (از گُل) ساختن.
۳ واژه‌ی انگلیسی 183 و آلمانی 1816(به چم "خمیر) نیز از همین واجریشه‌اند.
:۰ ۳
۳
اوستایی (/4۲8374): -8۸2 ,7۸7۸171 آلمانی (088/۸): 7
پارسی باستان (/فاق۳87 010): ۰ 2۸87۸۰ انگلیسی کهن (8#0لا8(70 صا0): ۰ 1۲7
پهلری (4/1ا۸ه): ان انگلیسی (80/ل8(/01): ان ۱
اوستی (0888712): نت دانمارکی (0۸۸]57): 7
کردی (80157): ۳7 سرثدی (817:157): جق۶
بلوچی (/۲7/ا8۸): 7 نروژی (//۸/00(۷2014): پا این 1
افغانی (پشتو) (/۸707۸2): ان هلندی (۵0767). رد۱1
تخاری 8(8 [(۸ل3ل70). مق لیتوانی (هماللهلال7لا). نا را
سانسکریت (84(88707): ۸ را ابردی کهن (لاقلقا صاه):
۲۸۵0۸ ,5ال۶۸ 7 بل81619
یونانی 088880): ۰ 08867085 ,08600 ولزی (7لک۷87): ۰ ۶۸1
لاتین (/712بما): 5 ,860 برتونی (/87670): ۰ 2
فرانسه (7ل)/۳52): -8807
اسپانبایی (82۸/1874): سایدددا پسگشت‌ها انیت درد
ایتالیایی (۷(له3): ۳7۰ ۳
رومانی ((۸/۸۸۸): شابن 6 (816711) بای ان ان
پرتغالی (۳0871017285): این | :هام02 ً
=== 8140-8180
تاو
بادداشت: ۰ 3 58 :
در برخی از زبان‌های هند و اروپایی این واژه این چم‌ها را هم دارد: پرست کندن (از حبوان).
فارسی (/(4ا2۳876: دز دز 7 ق20۴3
چم انگلیسی سرواژه‌ی فارسی: دا ای (دد ۱
اوستایی (7ل485874): 0۸32۸- ,1720۸32 پارسی پاستان(/(۲87۹14 2ا0): ۰ 80102
[pdf page 277]
۸ است ‏
پهلوی (1/الاوه): 217 سوئدی (5175015). 26
اوستی (0858716): 0 نروژی (۸/08201۸(7. 206
تخاری ۸ (۸ 4(7ل7002۸): ان هلندی (//070اصاث ۹ رو 28860
سانسکریت (8۸(/577): اسلاوی کهن (۲16ها5 0707 طا0). « وی ۰
0۸ ,013 05811 +211 . 052۸ 7100
ارمنی (۸/45(7]47): درز لینوانی (۵1ا(۸تا7ل):
برنانی (07580): 70161108 ,۳7167305 71 ,197117
لاتین (710ما): سااز۱ پروسی کهن ((۶۳۷75314 صا0). 010۸
گرتیک (00710): ۱
6۸7 ,0516۸ ,0۸68 پسگشت‌ها ند ای ادا اد رد۲
ایسلندی کهن (4010۸۷۸۸(ی5 صان): ز 0 2000
َ ,0816 7 (0061) ی سا
فریزی کهن (۲#1540 صا0): دار 5 (۲۵378285) :۸4۸525
آلمانی کهن ((02744۸ 7104 صان): 472 ۸
6 ,11816 6 (001761) :005
آلمانی (0570/۸0): 716 تراد ۱
انگلیسی کهن (7ل5ابا80/0 صان): 3 (01181611) ,اق1 (001613)
6 ولل02 ,0265 5 ,016118 :8للمطه غ لمیر
انگلیسی (8(/01157): 20 برهان قاطع ز ۸۵۰
دانمارکی (0۸۸//374): 216
بادداشت: ۹
۱ بازگشت به: دیوار. :
۲ چم این واژه در زبان‌های ایرانی باستان و یرنانی؛ دیوار,
چم این واژه در زبان‌های اسلاوی و ژرملی:گل» خمیر, ا!
چم این واژه در زبان تخاری ۸: مجسمه‌ی کرچکه. ۱
َ ۰ .
۱
ِ
اوستایی (4۷857۸/۷): ۰ 2۸87۸۰ ,2870 پهلوی (۲1مابلمه): ون ا
پارسی باستان (ل28781۸ 010): کردی (۸(20150). 4 ,0557 ِ
فا مق بلرچی‌روتت‌نزیم: 7
[pdf page 278]
دش دز (به چم "ید" مثلاً در *دشوار" با *دژخیم) / ۲۷۹
```


## [2026-09-04T18:42:53.600Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '8700,8735p' ARY_pages.txt"
}
```


### [2026-09-04T18:42:53.642Z] TOOL RESULT

```
افغانی (پشتو) (۸70[7۸۷7): 1۸ برهان قاطع ‏ ۹۵

آرمنی (445/1۵24): 20 لغت‌نامه دهخدا: 1۱۳۱۴

یادداشت: .

۱ چم اين واژه در زبان پهلوی: پذیرفته؛ برده,

بازگمت به: دیدن

اوستایی (/4۲2974: 0۸3۷۸ ب۸لا0۸ آلمانی کهن (/(06520/۸ ۷/04 صام):

پارسی پاستان (۳87۶4۷ صا0): 0۸1۷۸ 720

پهلری (1ماتلمه): 7 ,25 انگلیسی کهن (للولرا20 صان):

اوستی (0558716): ۰.8۸ 58 ,16

کردی (0201571:): اند اسلاوی کهن (70/ما5 #ل#6نالل صان):

سانسکریت (8445877): 085 2

یونانی (02880): 28 لیتوانی (/(1۸م۸لال771.): نایدا

لاتین (7100ما)د تشه لتونی (لتی) (/7014مل): ند

فرانسه (۳5۸۲[7): 0218 پروسی کهن (7(ف۲۴-551 0ا0).

اسپانیایی (۸/]8ط5): 0085 : 58 و1257۷7۸8

ایتالیایی (۵(۷ال7۸): 210 ایرلندی کهن (570ل12 صا0): 0۸

رومانی ((۵ا ۸1۸2 ): [ا78 گالی (0703[7): -080

پرتغالی (۳071001858): نراد . ولزی (58977): 12
```


## [2026-09-04T18:43:09.001Z] TOOL CALL #45: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py ARY:297 --image 2>&1 | tail -40"
}
```


### [2026-09-04T18:43:14.573Z] TOOL RESULT

```
(no exact page map; using offset -1 -> pdf page 296; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/0297.png
REF: ARY:297  PDF: data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf page 296  OCR-lang: fas+eng

دیوار / ۲۹۷
پسگشت‌ها ار رات دیا 3 (057۷) :57
33333 7
2 (ن018۲) :م05 0 ((053/0) رز را
0 (053/0۸) :2(/2[58 ۸۸۲ برهان قاطع : ۹۷
نا ما۸
یادداشت. ۳ +
۱ چم این واژه در همه‌ی زبان‌های این فهرست: خلل
۲- علت دگرگونی چم این واژه در زبان‌های ایرانی این است که پس از ظهور زرتشت و آئین او "آهورامزدا" مورد
پرستش قرار گرفت و واژه‌ی "دیو" چم کنونی خود را به دست آورد.
اوستایی (87۸/۷): ۵0۵ چکه (250)): 2
پارسی باستان (۳8۶۶۵4/۷ 010): 210۸ صربی (/5588142): 20
پهلوی (47الل۳۸): 0 برهمی (80/78۸/144): 20 !
کردی (0821/874): 0۸ بترانی طبر :۰ 22178027810۰
افغانی (پشتو ) (/4۴0/7۸(۷): 8( پروسی کهن (۲/۹54 00): ۱
نخاری ۸ (۸ [(4ل707۸7): 19 0505
تخاری 8(8 [0ل/۸ل707): 715۸ ایرلندی کهن ربزکتهز ۵ام): 00۱/۹۵۵۰۵1۷6
‌ سانسکریت (54/97/7): ۰ 08731۰ ,081181 ۱
ارمنی (/(0457]4ل۸): - زان )من پسگشت‌ها زرد درد
برنانی 088/0): رک یس
ات 7005 5 ما05
لانین (لراجشم: ۰ :31۷088۴ ,31۸00 3 (783852 ها ۲۸۳0۷8)
گرتیکه (ع/007[7): زرلا قم زا 9 (لتغ۲۸) :۸25215
۱ اسلاوی کهن (0/اها5 تح ۲ ا0): 472473 : 8۸0
. 701 7 (لت۸) مزر ۲ ۱۱/۵/۶۳
یادداشت. ۱ ۱
۱ ۱ بازگشت به: دز
۱
```


## [2026-09-04T18:43:21.707Z] TOOL CALL #46: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/0297.png"
}
```


### [2026-09-04T18:43:22.140Z] TOOL RESULT

```

```


## [2026-09-04T18:43:22.138Z] INPUT

[Image: original 1500x2400, displayed at 1250x2000. Multiply coordinates by 1.20 to map to original image.]


## [2026-09-04T18:43:40.734Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\necho \"### KLN paradise\"; grep -n \"^paradise\" KLN_1966.txt | head -5\necho \"### KLN dough\"; grep -n \"^dough,\" KLN_1966.txt | head -3\necho \"### KLN lady/dairy\"; grep -n \"^lady,\\|^dairy,\" KLN_1966.txt KLN_1971.txt | head -5\necho \"### KLN figure/fiction\"; grep -n \"^figure,\\|^fiction,\" KLN_1966.txt | head -5"
}
```


### [2026-09-04T18:43:40.846Z] TOOL RESULT

```
### KLN paradise
### KLN dough
### KLN lady/dairy
KLN_1966.txt:21000:lady,  n.  —  ME.  lafdl,  lavede,  ladi,  fr.  OE.  hlxf- dlge,  ‘mistress  of  the  house’,  lit.  ‘loaf-maker’.
KLN_1971.txt:63629:dairy, n. — ME. deierie , formed with suff. -erie 
KLN_1971.txt:133043:lady, n. — ME. lafdi, lavede, ladi , fr. OE. hlHef- 
KLN_1971.txt:139335:lady, lord, Lammas. 
### KLN figure/fiction
14673:fiction,  n.  —  F.,  fr.  L.  fictidnem,  acc.  of  fictid,  ‘a forming,  shaping’,  fr.  fictus,  pp.  of  fingere,  ‘to form,  shape’.  The  original  meaning  of  this  verb was  ‘to  knead’.  It  derives  fr.  I.-E.  base  *dheigh-, *dhoigh-,  *dhigh-,  ‘to  knead,  form  out  of  clay, form,  shape’,  whence  also  OE.  dag,  ‘dough’;  see dough  and  -ion.  For  the  change  of  the  concrete meaning  to  the  abstract  cp.  L.  comprefiendere, ‘to  seize,  grasp;  to  comprehend,  understand’ (see  comprehend).
14703:figure,  tr.  and  intr.  v.  —  F.  figurer,  fr.  L.  figurare, ‘to  form,  shape’,  fr.  figura.  See  figure,  n.,  and cp.  configure,  disfigure,  prefigure,  transfigure. Derivative:  figur-ed,  adj. figurine,  n.,  a  small  figure;  a  statuette.  —  F.,  fr. It.  figurina,  dimin.  of  figura,  fr.  L.  figura.  See figure,  n.,  and  -ine  (representing  L.  -inus). fig  wart,  a  condyloma.  -  Cp.  OE./ic,  MHG.  vie, veig,  ‘the  piles’,  fr.  L.  ficus,  ‘fig  tree,  fig;  the piles’  (see  fig,  n  );  so  called  from  its  shape. Filago,  n.,  a  genus  of  plants  of  the  thistle  family (hot.)  —  ModL.,  fr.  L.  filum,  ‘thread’.  See  file, ‘collection  of  papers’.  Cp.  Gifola. filament,  n.,  a  fine  thread,  fiber.  —  F.,  fr.  ModL. filamentum,  fr.  Late  L.  filare,  ‘to  spin’.  See  file, ‘collection  of  papers’,  and  -ment.
```


## [2026-09-04T18:43:44.637Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"paradise\\|Paradise\" KLN_1966.txt | head -8\necho \"---\"\ngrep -n \"^dough\" KLN_1966.txt KLN_1971.txt | head -5\necho \"--- figure n\"\ngrep -n \"figure,  n\\.\" KLN_1966.txt | head -3"
}
```


### [2026-09-04T18:43:44.727Z] TOOL RESULT

```
4891:bheesty,  n.,  a  water  carrier.  —  Hind,  bhisti,  fr. Pers.  bihisti,  ‘one  from  Paradise’,  fr.  bihist, ‘Paradise’,  which  is  rel.  to  Avestic  vahishta-, Pahlavi  vahisht,  OI.  vasisthah,  ‘best’.
10662:‘I  smear,  anoint’,  dehf,  ‘rampart,  dam,  dike’, Avestic  daeza,  ‘wall’,  pairi-daeza,  ‘enclosure’, and  cogn.  with  Goth  daigs,  OE.  dag,  ‘dough’. See  dough  and  cp.  paradise, dehisce,  intr.  v.,  to  gape,  burst  open.  —  L.  de- hiscere,  ‘to  split  open,  gape,  yawn’,  fr.  de- and  hiscere,  inchoative  of  hiare,  ‘to  yawn’. See  hiatus.
11932:diwan,  n.  —  A  var.  of  dewan. diwani,  n.  —  A  var.  of  dewanee. dixie,  also  dixy,  n.,  a  kind  of  mess  tin  (slang).  — Hind,  degcht,  ‘a  small  kettle’,  fr.  Pers.  degcha, dimin.  of  deg,  ‘pot’,  which  is  rel.  to  Pahlavi  deg, ‘pot’.  Arm.  dez,  ‘heap’,  and  to  OI.  dihmi,  'I smear,  anoint’,  fr.  I.-E.  base  *dheigh-,  *dhoigh-, *dhigh-,  ‘to  form  out  of  clay,  to  knead,  form’. See  dough  and  cp.  next  word, dizdar,  disdar,  n.,  the  warden  of  a  castle.  —  Pers. dizdar,  ‘holder  of  a  castle’,  fr.  diz,  ‘castle’,  and -dar,  ‘holder,  possessor’.  The  first  element  is rel.  to  OPers.  dida,  ‘castle’,  Avestic  daeza, ‘wall’,  Arm.  dez,  ‘heap’ ;  see  prec.  word  and  cp. the  second  element  in  paradise.  For  the  second element  see  aumildar  and  cp.  words  there  re¬ ferred  to.
12148:rel.  to  ON.  deig,  Dan  deig ,  Swed.  deg,  MLG. deck,  MDu.  deech,  Du.  deeg,  OHG.,  MHG. teic,  G.  Teig ,  Goth,  daigs,  dough’,  digan,  ‘to knead’,  fr.  I.-E.  base  *dheigh-,  *dhoigh-,  *dhigh-, ‘to  form  out  of  clay,  to  knead,  form’,  whence also  Of.  dehmi,  ‘I  smear,  anoint’,  dehah,  ‘body’, lit.  ‘that  which  is  formed’,  dehi,  ‘rampart,  dam, dike’,  Avestic  daeza,  ‘wall’,  pairi-daeza,  ‘en¬ closure’  (whence  Gk.  TrapaSsiaop,  ‘enclosed park’),  OPers.  dida,  ‘castle’,  Toch.  A  tsek-, tsaik-,  B  tsik-,  ‘to  form’,  tseke,  ‘statue’,  Arm. dez ,  ‘heap,  pile’,  dizanem,  ‘I  heap  up,  pile  up’, Gk.  Tetyo?,  zov/'K  (dissimilated  fr.  *Hixoz, *ffotyo<;),  ‘wall’  (orig.  'clay  wall’),  (Hyyaveiv,  ‘to touch’,  Thracian  -SI£a,  ‘castle’,  L.  fingere,  ‘to form,  shape,  fashion’,  figura ,  ‘form,  shape’,  fi- gulus,  ‘potter’,  Oscan  feihuss,  ‘the  walls’,  ORuss. deza,  ‘baker’s  trough’,  Lith.  diezti,  dyzti,  ‘to cudgel,  thrash’  (lit.  ‘to  knead  thoroughly’),  OIr. digen,  ‘firm,  solid’  (orig.  ‘kneaded  into  a  com¬ pact  mass’).  Cp.  also  the  metathesized  forms: Lith.  ziedziu,  ziesti,  ‘to  form,  build’,  OSIav. zizdp,  zidati,  ‘to  build’,  zidu ,  ‘wall’.  Cp.  dairy, duff,  ‘pudding’,  and  the  second  element  in  lady. Cp.  also  deha,  dixia,  dizdar,  effigy,  faint,  feign, fictile,  fiction,  fictitious,  figure,  thigmo-,  the  first element  in  Tichodroma,  thixotropy  and  the second  element  in  paradise.
12634:edelweiss,  n.,  a  small  Alpine  plant  bearing  white flowers.  —  G.  Edelweifi,  compounded  of  edel, ‘noble’,  and  weifi,  ‘white’.  For  the  first  element see  atheling,  for  the  second  see  white, edema,  oedema,  a  swelling  ( med .)  —  Medical  L., fr.  Gk.  ol'Sr)(jta,  ‘a  swelling’,  fr.  oESoiv,  oESeiv,  ‘to swell’,  which  is  cogn.  with  Arm.  aitnum,  ‘I swell’,  aitumn,  ‘a  swelling’,  L.  aemidus  (for *aidmo-dos  or  *aidsmo-dos ),  ‘swelling’,  ON. eista  (for  *oid-s-to-),  ‘testicle’,  eitill,  ‘swelling’, eitr,  ‘poison’,  OE.  at  or,  attor,  of  s.m.,  and  prob. also  with  OSlav.  jadu ,  ‘poison’,  jadra  (pi.), ‘bosom’.  See  after  and  cp.  the  first  element  in Oedipus  and  the  second  element  in  myxedema. Derivatives:  edem-ic,  oedem-ic,  edemat-ous, oedemat-ous,  also  edemat-ose,  oedemat-ose,  adjs. Eden,  n.,  in  the  Bible,  the  garden  in  which  Adam and  Eve  first  lived;  Paradise.  —  Heb.  * Edhen , name  of  the  region  in  which  lay  the  Paradise (see  Gen. 2:8,  10,  15,  etc.)  The  name  is  usually explained  as  ‘the  place  of  delight’,  and  derived fr.  Heb.  'idhen,  ‘dainty,  delight’;  cp.  Edna.  U. Cassuto  in  his  Commentary  on  the  Book  of Genesis,  Part  One,  From  Adam  to  Noah,  The Hebrew  University,  Jersusalem,  1961,  pp.  107- to8,  explains  the  name  Eden — with  reference to  the  meaning  of  the  base  'dn  in  Ugaritic — as  ‘a  place  that  is  well  watered  throughout’. Derivative:  Eden-ic ,  adj. edenite,  n.,  a  variety  of  aluminous  amphibole (mineral.)  —  Named  after  £(/c'«ville,  New  York. For  the  ending  see  subst.  suff.  -ite.
15144:ford,  former,  forth,  further.  Cp.  also  arpent,  ex¬ perience,  experiment,  expert,  finnan,  paradise, pardao,  parallel,  Perean,  peregrine,  peril,  per¬ oneal,  pilgrim,  poligar,  pore,  ‘opening",  porrect, port,  ‘harbor’,  port,  ‘gate’,  port,  ‘to  carry’,  post, ‘stake’,  Prajapati,  Prakrit,  prakriti,  Pralaya, pram,  ‘a  kind  of  boat’,  prana,  priest,  primary, prime,  prior,  proceres,  procerity,  prodigal,  prone, prose,  proso-,  protero-,  proto-,  province,  prow, ‘fore  part  of  a  ship’,  prowess,  Purana,  and  the second  element  in  reciprocal.
18149:Derivatives:  hour-ly,  adj.  and  adv. houri,  n.,  a  nymph  of  the  Moslem  Paradise;  (fig.) a  seductive  woman.  —  F.,  fr.  Pers.  hurt,  fr. Arab,  hur,  pi.  of  ahwar,  fern,  haurd ’,  ‘having beautiful  black  eyes’,  fr.  fiawira,  ‘had  black eyes’,  which  is  rel.  to  Heb.  hawar,  Aram.-Syr. hdwdr,  ‘was  white’,  Heb.  hur,  ‘white  stuff’,  hori, ‘white  bread’.  The  -i  in  Pers.  hurt  is  a  formative element  serving  to  denote  the  singular, house,  n.  —  ME.  hus,  hous,  fr.  OE.  hits,  rel.  to OS.,  ON.,  OFris.,  OHG.  MHG,  Ads,  Du.Au/s,G. Haus,  Goth.  -Aur(in  the  compound^MdAnj.'temp- le\  lit.  ‘the  house  of  God’);  orig.  ‘shelter’,  fr. I.-E.  *qeus-,  -s-enlargement  of  base  *qeu-,  ‘to cover,  hide’.  See  hide,  v.  and  cp.  hoard,  hose, hut.  Cp.  also  husk,  the  first  element  in  husband, husting  and  the  second  element  in  caboose, house,  tr.  and  intr.  v.  —  OE.  husian,  ‘to  take  into a  house’,  fr.  hus,  ‘house’.  See  house,  n. housecarl,  n.,  member  of  the  bodyguard  of  a Danish  or  early  English  king  or  nobleman (hist.)  —  OE.  huscarl,  fr.  ON.  huskarl,  which  is compounded  of  ON.  hus,  ‘house’,  and  karl, ‘man’.  See  house  and  churl, housel,  n.,  the  Eucharist  (obsol.)  —  ME.  husel, fr.  OE.  husel,  ‘the  Eucharist’,  rel.  to  ON.  husl, of  s.m.,  Goth,  hunsl,  ‘sacrifice’,  and  prob.  cogn. with  Lith.  svehtas.  OSlav.  svetu,  OPruss.  swints, ‘holy’,  Lett,  svinet,  ‘to  hallow,  celebrate’, Avestic  splnta-,  ‘holy’.
27112:adj .  suff.  -ic  fr.  Late  L.  pandemus,  fr.  Gk.  TtavS^- [xo;,  7rxv8f][ii.oe,  ‘pertaining  to  all  the  people’,  fr. 7r<xv-  (see  pan-)  and  8rj[xo<;,  ‘people’.  See  demos. Derivatives:  pandemic,  n.,  pandemic-ity,  n. pandemonium,  n.,  the  abode  of  the  demons.  — ModL.,  the  capital  of  Hell  in  Paradise  Lost,  an epic  poem  by  John  Milton  (1608-74);  coined  by him  fr.  pan-  and  Late  L.  daemonium,  ‘inferior divine  being’,  in  Eccles.  L.  ‘evil  spirit’,  fr.  Gk. 8cap.6vt.ov,  ‘divine  power;  inferior  divine  being’, in  Eccles.  Gk.  ‘evil  spirit’,  prop,  subst.  use  of  the neut.  of  Scapovios,  ‘belonging  to  a  Sodptov’,  fr. Sodpcov,  ‘demon,  devil’.  See  demon.
---
KLN_1971.txt:75818:dough, n. — ME. dog, dogk, dah , fr. OE. dag , 
KLN_1971.txt:75851:doughty, adj. — ME. dohti, duhti, fr. OE. dohtig, 
KLN_1971.txt:75871:dought-i-ness, n. 
KLN_1971.txt:92490:dough and -ion. For the change of the concrete 
KLN_1971.txt:133048:dough and cp. lord. 
--- figure n
8665:configure,  tr.  v.,  to  shape  after  some  model.  — Late  L.  configurare,  ‘to  form  after  something’, fr.  con-  and  L,  fig ur are,  ‘to  fashion,  shape",  fr. figura,  ‘form,  shape’.  See  figure,  n.
11683:Derivative:  disfavo(u)r,  tr.  v. disfigure,  tr.  v.  —  OF.  desfigurer  (F.  defigurer), fr.  VL.  *disfigurare,  fr.  dis-  and  L.  figurare,  ‘to form,  fashion’,  fr.  figura,  ‘form,  shape’.  See figure,  n.
14701:Derivative:  figment-al,  adj. figurant  (masc.),  figurante  (fern.),  n.,  a  ballet dancer.  —  F.,  prop,  masc.,  resp.  fern.,  pres.  part, of  figurer,  ‘to  figure,  shape’,  fr.  L.  figurare,  fr. figura,  ‘shape,  figure’.  See  figure,  n.,  and  -ant. figurate,  adj.  —  L.  figurdtus,  pp.  of  figurare.  See prec.  word  and  adj.  suflf.  -ate. figuration,  n.  —  F.,  fr.  L.  figitratidnem,  acc.  of figuratio,  ‘a  forming,  shaping’,  fr.  figurdtus,  pp. of  figurare.  See  prec.  word  and  -ion. figurative,  adj.  —  F.  figuratif  (fem.  figurative),  fr. Late  L.  figurativus,  ‘figurative’,  fr.  L.  figurdtus, pp.  of  figurare.  See  figurate  and  -ive.
```


## [2026-09-04T18:43:51.362Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"paradise, n\\.\\|^paradise\" KLN_1971.txt | head -5\ngrep -n \"TrapaSeicroi;\\|paradisus\\|TrapaSetao\" KLN_1966.txt KLN_1971.txt | head -10"
}
```


### [2026-09-04T18:43:51.430Z] TOOL RESULT

```
173194:paradise, n. — ME. paradis , fr. OF. (= F.) para- 
173209:paradise. 
KLN_1971.txt:173195:dis, fr. Late L. paradisus , fr. Gk. napotSeiooq, 
KLN_1971.txt:173217:taining to paradise’, fr. Late L. paradisus . See 
KLN_1971.txt:173225:fr. L .paradisus. See paradise and suff. -ac and -al. 
KLN_1966.txt:27260:Derivative:  paradisaical-ly,  adv. paradise,  n.  —  ME .paradis,  fr.  OF.  (=  F .)  para- dis,  fr.  Late  L.  paradisus,  fr.  Gk.  TtapaSeiao?, ‘park,  the  garden  of  Eden,  paradise’,  a  word  of Old  Persian  origin;  cp.  Avestic  pairidaeza,  ‘an enclosure’,  whence  Heb.  pardes,  ‘park,  garden’ (whence  Aram,  pardes,  pardesa,  of  s.m.).  Aves¬ tic  pairidaeza  is  compounded  of  pairi,  ‘around’, and  daeza,  ‘wall’.  The  first  element  is  cogn.  with Gk.  Ttepi,  ‘around,  about’ ;  see  peri-.  The  second element  is  cogn.  with  OIr.  digen,  ‘firm,  solid’ (orig.  ‘kneaded  into  a  compact  mass’),  Gk.  tei- /o;,  ‘wall’,  L .  fingere,  ‘to  form,  fashion’,  Goth. deigan,  ‘to  smear’,  OE.  dag,  etc.,  ‘dough’.  See dough  and  cp.  deha,  fiction  and  the  first  element in  dizdar.  Cp.  also  parvis,  which  is  a  doublet  of paradise.
KLN_1966.txt:27262:Paradisea,  n.,  the  typical  genus  of  birds  of  para¬ dise.  —  ModL.,  fem.  of  ML.  paradiseus,  ‘per¬ taining  to  paradise’,  fr.  Late  L.  paradisus.  See prec.  word.
KLN_1966.txt:27269:paradisiacal,  also  paradisiac  adj.,  pertaining  to, or  resembling,  paradise.  —  Late  L.  paradisiacus, fr.  L. paradisus.  See  paradise  and  suff.  -acand  -al. parados,  n.,  parapet  behind  a  trench.  —  F.,  prop, ‘defense  from  the  rear’,  coined  fr.  para-,  ‘that which  protects’,  and  F.  dos,  ‘back’,  fr.  L.  dor¬ sum.  See  dorso-.
```


## [2026-09-04T18:43:58.291Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor pat in ['paradise,  n.  —  ME','dough,  n','dixie,  also  dixy','fiction,  n','figure,  n.,','deha,  n']:\n    for i,pg in enumerate(pages):\n        if pat in pg:\n            print(pat,'-> leaf',i,'≈ printed p.',(i-12)*2, 'or', (i-12)*2+1)\n            # try find page numbers in the block\n            nums=re.findall(r'\\b(\\d{3,4})\\b',pg[:400])\n            print('   head nums',nums[:6])\n            break\nEOF"
}
```


### [2026-09-04T18:44:00.253Z] TOOL RESULT

```
paradise,  n.  —  ME -> leaf 600 ≈ printed p. 1176 or 1177
   head nums []
dough,  n -> leaf 261 ≈ printed p. 498 or 499
   head nums []
dixie,  also  dixy -> leaf 256 ≈ printed p. 488 or 489
   head nums []
fiction,  n -> leaf 319 ≈ printed p. 614 or 615
   head nums []
figure,  n., -> leaf 320 ≈ printed p. 616 or 617
   head nums ['590']
deha,  n -> leaf 229 ≈ printed p. 434 or 435
   head nums []
```


## [2026-09-04T18:44:07.166Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [255,256,257,260,261,599,600,601]:\n    pg=t[i]\n    nums=re.findall(r'^\\s*(\\d{3,4})\\s*$',pg,re.M)\n    print(i, nums[:8], repr(pg[:80]))\nEOF"
}
```


### [2026-09-04T18:44:09.218Z] TOOL RESULT

```
255 ['466', '467'] 'uish (as  well  as  in  extinguish,  admonish,  astonish)  is due  to  the  infl'
256 ['468', '469'] '�  L.  diuturnitas,  fr. diuturnus.  See  prec.  word  and  -ity. diva,  n.,  a '
257 ['470', '471'] ' on  a  distaff  ( obsol .); 2)  to  bedizen.  —  ME.  disen,  fr.  MLG.  dise, '
260 ['476'] '  —  ML.  dominicalis,  ‘pertaining to  a  master  or  lord’,  fr.  L.  dominicu'
261 ['477'] ' —  F.  dormi,  pp.  of dormir,  ‘to  sleep’.  See  dormant.\nDoronicum,  n.,  a '
599 ['1122', '1123'] '� ed  of  raxv-  (see  pan-)  and  <1096?,  ‘wise,  clever’. See  sophism.\npanso'
600 ['1124', '1125'] 'apilion-aceous,  adj.\nPapilionidae,  n.  pi.,  name  of  a  family  of  butter¬ '
601 ['1126', '1127'] 'fr.  Late  L.  paradisus,  fr.  Gk.  TtapaSeiao?, ‘park,  the  garden  of  Eden,'
```


## [2026-09-04T18:44:17.102Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [261,319,320,600,229,21000//1]:\n    pass\nfor i in [261,319,320,600,229]:\n    pg=t[i]\n    print(i, re.findall(r'^\\s*(\\d{3,4})\\s*$',pg,re.M)[:8])\n# lady leaf\nfor i,pg in enumerate(t):\n    if 'lady,  n.  —  ME.  lafdl' in pg:\n        print('lady leaf',i, re.findall(r'^\\s*(\\d{3,4})\\s*$',pg,re.M)[:8])\n    if 'dairy,  n' in pg:\n        print('dairy leaf',i, re.findall(r'^\\s*(\\d{3,4})\\s*$',pg,re.M)[:8])\nEOF"
}
```


### [2026-09-04T18:44:18.950Z] TOOL RESULT

```
261 ['477']
319 []
320 ['590', '591']
600 ['1124', '1125']
229 ['416', '417']
dairy leaf 219 []
lady leaf 461 ['858', '859']
```


## [2026-09-04T18:44:25.355Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(316,324):\n    print(i, re.findall(r'^\\s*(\\d{3,4})\\s*$',t[i],re.M)[:8], t[i][:50].replace('\\n',' '))\nprint('--- dairy')\nfor i in range(217,222):\n    print(i, re.findall(r'^\\s*(\\d{3,4})\\s*$',t[i],re.M)[:8], t[i][:50].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T18:44:27.029Z] TOOL RESULT

```
316 ['584']  ML.  feltrum,  filtrumf  felt. strainer  of  felt
317 ['585', '586']  ,  Russ,  paporot',  Gaul,  ratis  (for *pratis )
318 ['587', '588', '589'] fetter. Derivative :  fetlock-ed,  adj. feto-,  fo
319 [] ��, haplologic  contraction  of  VL.  *fivibula,  
320 ['590', '591'] alf-ripe  fig’.  Cp. Ficus,  the  first  element  
321 []   folli- culus,  ‘a  little  bag’,  dimin.  of  fo
322 ['596', '597'] .  Cp.  also  therapeutic,  throne, thorax,  dharm
323 []   fr.  L.  flaccidus, fr.  flaccus,  ‘flabby’,  wh
--- dairy
217 ['393', '394'] sure, quinsy,  squinancy. cynocephalic,  n.,  cyno
218 ['396', '397']  See  -cyte. cytology,  n.,  study  of  the  struc
219 [] odel’,  fr. OF.  affrodile,  a  var.  of  asfodile
220 ['400']   form  by  a  con¬ fusion  with  L.  dominus,  ‘l
221 ['401', '402', '403'] ��. Derivative:  dandruff-y,  adj. dandy,  n.,  a
```


## [2026-09-04T18:44:33.905Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^PARADISE\\|^DOUGH\\|^LADY\\|^DAIRY\\|^FIGURE\\|^FICTION\" SKT.txt | head -10"
}
```


### [2026-09-04T18:44:33.953Z] TOOL RESULT

```
6541:FIGURE,
9849:LADY.
```


## [2026-09-04T18:44:37.544Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"PARADISE\" SKT.txt | head -5\necho \"---\"; grep -n -i \"^DOUGH\\|DOUGH,\" SKT.txt | head -5\necho \"---\"; sed -n '6541,6548p' SKT.txt; echo \"---LADY\"; sed -n '9849,9856p' SKT.txt\necho \"--- DAIRY\"; grep -n -i \"^DAIRY\\|DAIRY,\" SKT.txt | head -3"
}
```


### [2026-09-04T18:44:37.645Z] TOOL RESULT

```
8882:Houri,  a  nymph  of  Paradise.  (Peti.^ Fer^.  A$iri,  one  virgin  of  Paradise,  ktird, Atir.  a  virgin  of  Paradise,  black-eyed nymph.  Cf.  Arab.  Aawrd,  fern,  of  akwar, having  fine  black  eyes.
13216:Paradise.  (F.  -  L  -  tik.  - Paradis.  —  L.  paraJisus.  —  Gk.  v park,  pleasure-ground;    art  oru: and  now  a.<>ccrtained  to  be  of  Pcrs,  chij
23151:paradise — parvis.                   L^^^|
---
5352:Dough ;  tec  Dike.
5353:Doughty;  tee  Do  (3).
---
FIGURE,
M9
feoff,  to  invest  with  •  fief.  (F.  - O.  H.  C;.^  Norman  F.  ffcff*-.  O.  ?,Jitfer, vcib   ftom   F  fuf,  a   fiei  (atmvc),      Der.
L  e.  /ej-^t  where  V  is  the  auffix  of
pp.
iBktr       '^^     M.  E.////.    A.S.Atf/; |.  a.  V,  ftb ,  frand.
nati<      .  >  tcura.
rtddto.  a  Woiin,  ^L)  A.  S.  Ji^U, It  /5Ji.  Dan  /./^/.  Du,  iv^/-/.  G id.  Apparently  borrowed  from  L. M^  MtilbLi,  a  riol ;  see  Viol. IddSty;  secVftith. Utcait  (Scifid.)  A  dim  in.  fonn  of fr.  to  t«  cfltUkisaUy  moving  up  and ■m,  tftdt  /i«  to  North  of  Engbnd .^  Jkkfm,  tn  Adgcf,  to  hasten.  — ] eel. V,  to  cUmb  op  nimbly,  aa  a  spider  \ ml  Jtko.  to  h(int  after,  Norw. /-6a,  to kr  trouble,  /ka  tsitr^   lo  hasten  alter.
---LADY
LADY.
LANCE.
I
I
■
I
Allied  to  Russ.  klade^
HLATH.  tolade) K load.
--- DAIRY
4650:Dairy ;  ^ee  Bike.
```


## [2026-09-04T18:44:44.541Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13210,13222p' SKT.txt\necho \"=== DHIGH root list\"; grep -n -i \"DHIGH\\|✓ DIKE\\|Dike,\" SKT.txt | head -20"
}
```


### [2026-09-04T18:44:44.606Z] TOOL RESULT

```
ProT./arsM/a,  Span,  patabra  (  ^ Port  palatira.  —  T  ow  I,.,  pa'.i course ;  L.  parab^la^  a  parable. ble  above.
Parachute :  sec  Paro.
Paraclete,   the  Comforter.    (L-(j\ L.  pamiletuJ.  —  OV.  wap^KijrM,  csditA one's  aid,  the  Comforter  (John,  riv.  ift.'t* Gk.  wapaxaXftv.  to  call  to  oric't  atd,— 01^^ irapa,  beside  :  taXttf.  to  call.
Parade:  f'ce  Pare
Paradigm,  an  example.  oiodeL  (F.
—  Gk.)     F.  paraiU^ine,  —  L.  /Wra/^—'j Gk.  mp&hnyfio^  a  pattern,  model* of  declension.  — Gk.  mpn,  beside;  t^U 1  point  out.  show.     See  Diction.
Paradise.  (F.  -  L  -  tik.  - Paradis.  —  L.  paraJisus.  —  Gk.  v park,  pleasure-ground;    art  oru: and  now  a.<>ccrtained  to  be  of  Pcrs,  chij
—  O.  Ptrs,  vZend)  pairiiliusa,  on  endc place  walltd  in.- U.   Pets,   pairi  \ irepi),  around  ;  tlit  (  »Skt.  ffth\  to  at fortii.  shape  (hence  to  form  a  wall  of VIUIIGK;  KeDUo.
parrla.  a  porch,  room  o?er  a (F.-L.-Gk.-rcrs.)       O.  F.  psrtit, porch,  outer  court  before  a  houce  or  cht
—  Low  L.  paraviiuj,  coim itu,  a  church  porch,  cute'
Paradox.  ( !"  - 1  -  -  Gk  .     i
—  L.  paradexnm.  neut.  of  /Sw  .
—  Gk.    vapaSofor,    contrary    : opinion.  — Gk.  iro/id,  beside  :  Hl^tf^% from  5o«*ri',  to  seem  ;  »rc  Doaraa .
=== DHIGH root list
5078:DUw.  a  trendi,  tzvKh  ad  ttofaHkMCit. buk.  <E.)  U.  E.  iSil;  afao  JfeA  (-»od. t,  dHay  A.  S.  ii&^.  -f.  Dk.  i^i,  IceL diOft.  Dan.  d^.  Swrd.  ^'ir,  G.  teuM,  pood, tank,  Gk.  ruxw,  nil.  nmfiAJt,  Skt.  JM, rampart.  All  from  ^  DHIGH.  to  kMAd. fono.  iBOski ;  ss  u  Cock,  rfywo.
18725:stubborn.  <  E. )  M .  K.  stoburtt,  s/i/vtm ; i]iO  MttbofHtsse,  styfMfmesit.  stubbormiess, |br  which  Fabgrave  has  stubbtenasi.  The loa.!  M  is  due  to  misunderstanding  sfibcr- ft*  as  stihorH'fUsst ;  or.  in  any  case,  has added  ;  cf.  ti/ler-M,  slatttr-n.  Stubat  •, 'i^r*  represent  an  A.S.  form  styb-or*, at  found,  but  of  perfectly  re^^lar  form  : ^r  being  a  common  id},  suffix,  as  in  bit-or, fitter.  Krom  A.  S.  ttyb,  a  stub  Thus M«fw«  stock  dike,  not  easily  moved,  like oid  Mub  or  stump.
```


## [2026-09-04T18:44:56.513Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\npython3 $S SKT.txt \"All  from  .  DHIGH|DHIGH,  to  kMAd\" 20 2>/dev/null | head -3\npython3 $S SKT.txt \"Paradise\\.  \\(F\" 20 | head -3\npython3 $S SKT.txt \"Dough ;  tec\" 20 | head -3"
}
```


### [2026-09-04T18:44:58.410Z] TOOL RESULT

```
--- leaf 140 = printed p.120
   ... t. buk.  <E.)  U.  E.  iSil;  afao  JfeA  (-»od. t,  dHay  A.  S.  ii&^.  -f.  Dk.  i^i,  IceL diOft.  Dan.  d^.  Swrd.  ^'ir,  G.  teuM,  pood, tank,  Gk.  ruxw,  nil.  nmfiAJt,  Skt.  JM, rampart.  All  from  ^  DHIGH.  to  kMAd. fono.  iBOski ;  ss  u  Cock,  rfywo. dAify.  (Scuid.)  M.  £.  i^^wTg.  A  raoa for  a  ^<;v.  i.  &  a  mSk-woauB.  fanB*«erTanC. « Iccl.  >/W£w,  Swcd.  d^  a  maid,  dairy- mud,  who  was  also  tbe  bread-maker ;  the orig.  Kiue  is  *kneader  of  doQ£b.**Ioel. dfir.  Swed.  df^,  dough ;  see  dou^h  below. oiff.  (£.)  M.  E.  diggrm ;  weakened  form of  dikitm.  A.  S.  dici
--- leaf 353 = printed p.333
   ... adigm,  an  example.  oiodeL  (F. —  Gk.)     F.  paraiU^ine,  —  L.  /Wra/^—'j Gk.  mp&hnyfio^  a  pattern,  model* of  declension.  — Gk.  mpn,  beside;  t^U 1  point  out.  show.     See  Diction. Paradise.  (F.  -  L  -  tik.  - Paradis.  —  L.  paraJisus.  —  Gk.  v park,  pleasure-ground;    art  oru: and  now  a.<>ccrtained  to  be  of  Pcrs,  chij —  O.  Ptrs,  vZend)  pairiiliusa,  on  endc place  walltd  in.- U.   Pets,   pairi  \ irepi),  around  ;  tlit  (  »Skt.  ffth\  to  at fortii.  shape  (hence  to  form  a  wall  of VIUIIGK;  KeDUo. parrla.  a  porch,  room  o?er  a (F.-L.-Gk.-rcrs.)    
--- leaf 145 = printed p.125
   ... um). dotard.  {K.  with  F.sujix.)  From  ./tf//, with  F.  mfHx  •ard  {p.  H.  G.  ^^i/V). Double,  Doublet ;  M:e  Dual. Doubloon,  Doubt;  see  Dual. Douceur ;  see  Dnlcat. Douche  ,  sec  Duke. Dough ;  tec  Dike. Doughty;  tee  Do  (3). DOUBO,  to  immcrge.  (Scand.)  Allied  to Swcd.  ditma,  to  pluuipdown,  fkll  clumsily, Dan.  dundse,  to  thump  —S wed.  Axki.duns, adin.  — Swed. dial.  ^MMd,  to  mnkeadtn;  sec Din.  llencc  to  douse  is  prob.  to  (all  plump in.  na  in  liutler,  Hudibras,  pt.  il.  c.  I.  502* Dout ;  sec  Do  ^1 ). Dove,  Dovetail ;  see  DIts. Dowaj^r,  Dower  ;  »
```


## [2026-09-04T18:45:24.380Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\necho \"### LAT fingo\"; python3 $S LAT.txt \"^fingō|^fingo,|fingo, -is\" 18 | head -5\necho \"### LEW fingo\"; grep -n \"^fingo\" LEW_1910.txt | head -5\necho \"### TLM dida\"; grep -n \"didā\\|dida-\\|^didā\" TLM.txt | head -10\necho \"### NYB deg\"; grep -n \"^dēg\\|dēg \\[dyk\\|deg \\[\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-09-04T18:45:26.128Z] TOOL RESULT

```
### LAT fingo
--- leaf 437 = printed p.419
   ... ois" peut reposer sur *bhid-tro~, coaae l'a vu F. de Saussure; d'autre part, le sens de gr. cpe l,6opai, "^'epargne" peut s'expliquer par 1'idee de "se separer"; aais ce sont de siaples possibilitas. fingo, -is, finxi, fictum (finctus 1 basse ipoque, cf.Thes. VI 770,47 et s., et fr .feint, etc.), fingere: propreaent "aodeler dans 1'argile", cf. figulus "potier", fictilis "modeli dans 1'argile", -ia udsa, etc., et substantivi fictilia n.pl. "vaisselle d'argile"; puis "fayonner dans toute matiore piastique, fayonner la pate", cf .fictor "patissier" et "sculp.teur"; fictores dicti a fingendii libis, Varr.,
### LEW fingo
### TLM dida
### NYB deg
```


## [2026-09-04T18:45:29.191Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('LAT.txt',encoding='utf-8',errors='replace').read().split('\\f')\npg=t[437]\ni=pg.find('fingo, -is')\nprint(pg[i:i+3000])\nEOF"
}
```


### [2026-09-04T18:45:30.811Z] TOOL RESULT

```
fingo, -is, finxi, fictum (finctus 1 basse ipoque, cf.Thes. VI
770,47 et s., et fr .feint, etc.), fingere: propreaent "aodeler dans
1'argile", cf. figulus "potier", fictilis "modeli dans 1'argile", -ia
udsa, etc., et substantivi fictilia n.pl. "vaisselle d'argile"; puis
"fayonner dans toute matiore piastique, fayonner la pate", cf .fictor
"patissier" et "sculp.teur"; fictores dicti a fingendii libis, Varr.,
L. L.7,44, cf.Enn., A.131; et fictores dicuntur qui imagines uel signa
ex aere uel cera faciunt, Serv., Ae.8,634; figura f., Varr., L.L.6,78,
fictor cum dicit fingo, figuram imponit-, Isid., Diff., 1,538, figura
est cum impressione formae alicuius imago exprimitur, ueluti si in
cera ex anulo effigiem sumat, aut si figulus in argillam manum uultumque
aliquem exprimat, et fing-endo figuram faciat. Puis par extension;
"favonner" (d'une aanibre ginirale, sens physique et aoral), d'oi "pres¬
ser, toucher", Ov., F.5,40y saepe manus aegras manibus fingebat amicis,
et Her.ao,i37; "reproduire les traits de, reprisenter"; et "iaaginer,
feindre, inventer"; sens particulibreaent frequent dans 1'adjectif
fictus, et qui s'est akintenu dans les langues roaanes, cf.fr. feindre,
M. L.3313. - Usite de tout teaps.
Noabreux dirivis en fig- et pn fiet-: figulus a. et fig(u)llnus
(fig(i)llnus) adj., d'o& fig(u)llna (ars) f.; fig(u)llnum (opus) n.;
figularis (arch.); figulo,-ds (tardif) et ses dirivis, M.L.33yoa.
figulus est un cognomen friquent dans les gentes Marcia et Migidia.
figmen (rare et tardif), figmentum (tardif, appartient surtout k
la 1 . de 1 'tiglise, oi il traduit TtXacyp/x, CTTqJwi, 7 ioirta
710 UTjcn, C> etc.): reprisentation figuree, statue, etc.; iaagination
(sens concret), fable, invention;
figUra (forai avec le suffixe -ura directeaent sur la racine, et
non dirivi du supin coaae les autres noas du meae type): propreaent
"plastique"; d'ob, figure donnie k une chose, configuration, figure;
```


## [2026-09-04T18:45:36.179Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('LAT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor k in (437,438):\n    pg=t[k]\n    for key in ['dheigh','daeza','teichos','Skr.','skr.','av.','Av.','irlandais','gotique']:\n        i=pg.find(key)\n        if i>0: print(k,key,'->',pg[max(0,i-400):i+700].replace('\\n',' ')[:1100]); print()\n        break\nEOF"
}
```


### [2026-09-04T18:45:37.951Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:45:41.079Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('LAT.txt',encoding='utf-8',errors='replace').read().split('\\f')\npg=t[437]+ '\\n@@@\\n' + t[438]\ni=pg.find('fingo, -is')\nprint(pg[i+3000:i+7000])\nEOF"
}
```


### [2026-09-04T18:45:42.978Z] TOOL RESULT

```
ique "supposition, fiction"; a fictione = Ha©’U 7 to 0 e<rt,v;
t. de droit fictio legis. Le non n'apparait paa avant 1 '^poque impe¬
riale; surtout frequent chez Quintilien qui l'a peut-etre inventi,
cf. Inst. 0r.C,3,Ci; ficticius: invente, feint (cf. factIcius ), frelat 4 :
oleum, uinum ficticium', epoque imperiale.
Compoa 4 s: affingo: imaginer en outre, ajouter en inventant, attri-
buer (fauasement ) ; sur lequel Aulu-Gelle a fait affiguro', confingo:
imaginer ensemble, ou concerter; inventer de toutes pieces; defingo:
fayonner ( rare), M.L.3519; diffingo: transformer, refaire; effingo:
i° faire disparaitre, d'oii "eaauyer", Cat.Agr. 67,3 fiscinas spongia
effingant-, Cic.Seat.35 e foro spongiis effingi sanguinem, 3 ° fingendo
exprimere, exp<xcrcrei,v, reproduire, representer en relief; d'ou effigies
(,-gia arch. ) : portrait, image (gen^ralement en relief ), effigie, et
e ffigio,~as (depuis Apul.); in- (M.L.44oqa), per-, re-, trdnsfing 5 ,
rares et tardifa qui aont doubl^s par lea composta de figuro.
La racine i.-e. dheig’h- fournissait un present radical ath£ma-
tique dont le v 4 d. dehmi "je lute, je fixe par du mortier" conserve
la forme ancienne, et dont got. digands "uXaoac" est une trace. La
racine avait deux aspirees, comme on le voit, outre la forme germa¬
nique, par osq. feihuss "mBrOs"'et par la comparaison de gr.TS ZypCj
ToZy^oC "mur, rempart, paroi". Le g latin s'explique dans fingo par
l'n qui procede, dans figura par l'« qui suit (cf. ligurio)', osq. felhuss
(acc.pl.) resuite de la contamination de dheig 'hes- et de *dhoig’ho-
(cf. lea formes grecques xelypi, -ou£ et Ttnx°S.> -ou). Le present fingi 5
eat du type k nasale infixee, comme findo; le latin n'ayant h 4 rit£
d'aucun perfectum, il a 4 t 4 fait une forme finxi toute nouvelle. La
gutturale finale 4 tait une pr^palatale: 1 'Avesta a -daezayeit i "il
entasse", pairi-daeza "enclos" (le mot que lea Grecs ont h£ll£nis£
en TOxpaSe ioo £), et le vieux perse dido, "mur, enceinte". Le thbme latin
*^ e iyP e dhinghe / 0- aemble se retrouver dans une partie au moins dea
formea de 1'irlandaia: com-od-ding- "b&tir" ( cunutgim "je batis"),
v. Pederaen, Vergi. Gr. d. kelt. Spr . II p.505 et suiv. Le sena propre
de la racine est "fayonner (de la terre)". Ce travail de la terre
aboutit A faire un tas, un mur de terre: arm. dizanim "e 7 ttx 0 poC^O(i(xi,"
(verbe radical, surement indigene, et non emprunt^ a 1 1 iranien), dez
"tas", ou de la poterie, ainsi got. daigs signifie "argile". Le latin
a d^veloppe surtout ce second aens, et 1'osque offre le premier.
finis, -is (abl./tni Lucr.3,978, Plaut., Men.859, Caton, Agr.38,
3 ,113,3, mais Varron enseigne fine, Roman. ap. Charis. GLK I 133,38;
```


## [2026-09-04T18:45:49.618Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"fingo\" LEW_1910.txt | head -8"
}
```


### [2026-09-04T18:45:49.665Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:45:52.327Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la LEW_1910.txt; head -c 500 LEW_1910.txt; echo; grep -c \"\" LEW_1910.txt\ngrep -n -i \"figura\\|figulus\" LEW_1910.txt | head -5"
}
```


### [2026-09-04T18:45:52.395Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 627390 Sep  4 14:06 LEW_1910.txt
eae hee ne
ee
Duquesne University:
joe Kt re |
* ee . ¥
c
'DOGERMANISCHE BIBLIOTHEK
-ZWEITE REIHE: WORTERBUCHER
____ Digitized by the Internet Archive in 2023 with funding from No Sponsor — re
mi https://archive.org/details/lateinischesetymO ) any * ; - % MANY ioe hie vel
AN
~ LATEINISCHES: ee “EYYMOLOGISCHES WORTERBUCH ee
A. WALDE Met
3, NEUBEARBEITETE AUFLAGE ron #
VON
J. B. HOFMANN . 2 : * A
REGISTERBAND
ZUSAMMENGESTELLT VON ELSBETH BERGER
HEIDELBERG 1956 1B
: AA. Fs
CARL WINTER: 
14866
```


## [2026-09-04T18:45:56.012Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"fingo\\|fig[uū]ra\\|figulus\\|daeza\\|pairi\" LEW_1910.txt | head -10\necho \"== try loose\"; grep -on \"fing[oe][^ ]\\{0,12\\}\" LEW_1910.txt | head -10"
}
```


### [2026-09-04T18:45:57.913Z] TOOL RESULT

```
1524:paritizanants II 176 pad- II 294 paidyeiti II 295 pada- II 215 padtana- II 262 panta II 407 panta IT 336 par- II 344 para, para- II 285 parana- II 282 parasu- I 257 pard II 285 part IT 284 pariuntya I 49 pairika II 233, 252 pairidaéza- I 501, II 251 pairidaézayertt
1525:pairibrinants I 549 parrifrasa IT 346 pairyante IT 251 paurva- II 357 parsta- II 346, 349 parsti- II 349 pas- II 232 pasu- II 271 pasushaurvé II 525, 526 paskat II 348 pasta II 348 -pasti- II 296 pasne II 335 pazdayeiti I 2, 193 pazdu- Il 273 pasna- II 270 paman- II 234 para- IT 251 pasna- II 290 poratu- II 343 paradan IL 273 parada- ILI 251 paradu- II 316 parana- ,,Keder* II 282 parana- ,,voll* II 322 parana ,,hohle Hand‘ II 240 parasaitt II 346 poraska II 361
== try loose
```


## [2026-09-04T18:46:15.071Z] TOOL CALL #65: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1455 --image 2>&1 | head -60"
}
```


### [2026-09-04T18:46:22.102Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1455.png
REF: BQT:1455  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 248  OCR-lang: fas

-۱:۵۵- فردوی
ثانی بر وزن ‎)٩(‏ بر دمیدن » یراستن درخت کنده‌ای باشد که دریی‌در کوچه‌نهند تادر گشوده
تاك و غیر آن باشد بمنی بربدن شاخهای‌زبادتی | نگردد .
آنرا 7 فر دده ؟ » بروزن مجمره. بمعنی‌فردر

فرد خانه ۱ بر وزن سردخانه , است که چوب کندء پی در کوچه باشد ؛ وباین
خانه ای‌باشد که مردم غریب از راه رسیده‌درآنجا | امعنی با رای نقطه‌دار هم‌آمده است.
فرودآ بند - و خلوت را نیز گوبند وآن‌خانه‌ای فردفر ۴ > بافایروزن کفشگر,رب‌النوع
باشد که در خانقاه سازند بعنی چله خانه ۰ وآن | اسان راگوبند یعنی پرورندة اورا .
خان کوچکی باشد که مردم درآن بچله نشینند. فردوس * ه بکراول وثالك‌وسکون
فردد ۴ - بروزن زرگر, چوب‌بز رکه ثانی و واو و سین بی‌نقطه, بهشت راکوبندوباغ
(۱) چك : بوزن -
۹ -از : فرد ( عربی بمعنی بگانه » تنها )4 خانه .
۴ فرادر (ه.م.) * فردره . ۴ << فردر . ۴ - بر ساخته فرقهٌ
آذ رکیوان . 8 - معرب از ایرانی . در اوستا دوبار بكلمه 381۳1-02622 بر میخورم

) وندبداد فر گرد ۳ بند ۱۸ ؛ فرکرد ه بند ۹ ) وآن مرکست از دوجزو : پیشوند 0271

با [۳0217 بمعنی کردا کرد وپیرامون ؛ دوم 18628 از مصدر 1262 بمعنی انباشتن و روبهم‌چیدن

و دبوار گذاهتن . در زمان هخامنشیان » در ابران زمین بز رکه و درسراس قلمرو آنان خسوص

درآسیای صفیر پلثیری دئزها - با فردوسها - که باغهای بزرکك و «پارك» های با شکوه پادشاه

و خفثریاونها ( حاکمان ) و بزرگان ابران بوده . شهرتی داشت . این محوطه‌ها چنانکهمکرر

کزنفون ( در «کورش‌نامه > و« انباز > ) و پلوتارخس مینوبسند درختان انبوه وتناور داشتندوآب

در میان‌آنها روان بود . چاروابان بسیار برای شکار درآنها پرورش می‌بافتند. شاهنشاهان هخامنشی
خششرپاونهای خود را در ایجاد اینگونه باغها در قلمرو حکومت خود تشویق میکردند . ایشگونه
پا ر کها که در سرزمین بونان وجود نداشت ناکزیر انظار بونایان را متوجه خودکرد وآنان نیز
همان نام ایرانی را صورت 0274061908 بکار بردند . در کدی متأخر 387191 و در عبری

5 ز( پارك یا باغ ) و درآرامی وسربانی نیزهمین‌کلمه با اندك تفاوتی و در ارمنی087088

( باغ ) همه از ره ایرانی هستند . کلمهٌ « پاردی» در زبان عبری پس از مهاجرت بهودیان‌پبابل

در قرن ششم ق.م. بعاریت کرفته شده وچندین بار در قمتهای مختلف توراة پکاررفته . دربخشهای

قدیم توراة - بعنی آن قسمتی که پیش ازقرن پنجم ق.م. نوشته شده بهشت ودوزخ مفپوم‌روشن

وصریحی ندارد . كلمةٌ فردوس که دوبار در قرآن‌آمده » از دین بهود وعیسوی باسلام‌رسیده‌است.
مضران قرآن متفقاً فردوس را بمعنی باغ وبستان کرفته‌اند , اما اختلافشان درین است که آن‌چه

نوع باغ و بوستان پا جنت و حدیقه‌ایست .گفته شدکه درتوراة چندین بار 0876168 عبری بکار

بقیه درصفحةٌ ۱۶۵۹
فردا - فتح اول وسوم «* پردا (و.م.)» پهلوی ۳141 بونکر۱۹ ۹ ه شهمیرزادی

4 دکه. ۷س۱۹۹+گبلکی 1370486 : روزآبنده - روز ی که پی از امروزخواهدآمد.
```


## [2026-09-04T18:46:39.020Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor p in 918 851 359 914; do echo \"########## BQT:$p\"; timeout 900 python3 tools/ref_page.py BQT:$p --image 2>&1 | head -45; done"
}
```


### [2026-09-04T18:46:41.806Z] TOOL RESULT

```
########## BQT:918
no scan of BQT covers printed page 918 (see 'scans' in refs_online.json)
########## BQT:851
no scan of BQT covers printed page 851 (see 'scans' in refs_online.json)
########## BQT:359
no scan of BQT covers printed page 359 (see 'scans' in refs_online.json)
########## BQT:914
no scan of BQT covers printed page 914 (see 'scans' in refs_online.json)
```


## [2026-09-04T18:46:48.031Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,pg in enumerate(t):\n    if 'دیوار' in pg or 'ديوار' in pg:\n        print('leaf',i, pg[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T18:46:49.777Z] TOOL RESULT

```
684
leaf 68     ‫سس‬                                                                                             ‫چار تکبیرزدن‬  ‫چا
leaf 131  ‫چهار کامه‬                                                                                       ‫م‪۷‬‬  ‫چهارذ یوار ج
leaf 136    ‫==‬                                                                           ‫چمته‬   ‫گویند ‪ - ۴‬وهرمرتبه ازکل با
leaf 154       ‫‪-61‬‬                                                                                                 ‫خاتم کوبا
leaf 155 ‫جار خار‬                                                                                                            ‫‪-
leaf 194     ‫‪۷۳۹‬‬ ‫را‬    ‫مدور‬    ‫بز رگ‬    ‫زا کوب شوم ارا‬                   ‫ومع‬    ‫کرمان بیز ند وبخورند وارد نیزسازند
leaf 203  ‫خز مر‬                                                                                                            ‫‏~‪
leaf 205   ‫خس‌در دهان گرقتن‬                                                                              ‫‪1‬ع‬                
leaf 271  ‫دار شش‌دو‬                                                                                      ‫سس‬   ‫‪۱۱‬‬   ‫دارخا
leaf 320       ‫کک‬ ‫دست گز اد ہنم کاف فارسی و زای‬                                     ‫دستگار » باکاف بروزن‌دستبار‪ .‬همکار‪-‬‬
leaf 331                                                                                                ‫رت‬  ‫کوسفند ازآن بغورد 
leaf 370  ‫=‬                                                                                                    ‫دیع‬  ‫دیده بان
leaf 378       ‫اه‬                                                                      ‫دبوار خانه روزن شدن‬  ‫آرا‬   ‫وسکون دو
leaf 405   ‫رزه‬                                                                                               ‫‪‎-‬ی ) ‪“A‬‬    
leaf 411  ‫رشتاك‬                                                                                                       ‫‪-‬ي‬   
leaf 417  ‫رك‬                                                                                         ‫‪۷‬و ‪4‬‬   ‫ومعی‬     ‫پ
leaf 432  ‫‪“AYY‬‬                                                                                                     ‫روز خون‬ 
leaf 517   ‫زين‬                                                                                              ‫‪۵‬‬              
leaf 546      ‫زا‬                                                                                        ‫سبك صابه‬             
leaf 567   ‫سجلاط‬                                                                                       ‫==‬   ‫ونافرمالی نمودن‪
leaf 573                                                                                                   ‫=‬            ‫‪-‬‬  
leaf 590     ‫اس‬      ‫م‪۷‬‬                                                                                      ‫فرشکاهلی‬    
leaf 627   ‫سماررغ‬                                                                            ‫اعد‬   ‫‪۳‬‬                     
leaf 649  ‫سور بای‬
```


## [2026-09-04T18:46:54.019Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata,re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (377,378,379):\n    pg=t[i]\n    # strip bidi/format chars\n    pg=''.join(c for c in pg if unicodedata.category(c)!='Cf')\n    print('=== leaf',i)\n    print(pg[:2500])\nEOF"
}
```


### [2026-09-04T18:46:55.837Z] TOOL RESULT

```
=== leaf 377
                                                                                                            ۱۷


 دی ره  -بضم باوزایفارسی وسکون                                  است چه باز بسیار بزرکه راباونشبت دهند وباز
که نام روز بانزدهم
                 ها مخفف دين پژوه است ۴                          دبتار گویند  .و بعضی کویند دبذار نوعی از باز
                      باشد ازهرماه ملکی .
                                                                  است وآن بیاراصیل کومیابمیباشد وبرخلاف
 دینسافوس  - ٩بکس اول و اك                                      بازهای دیگر بردورمردمك چشم اوتحربرسیاهی
 وسین بینقطه ( )۳بالف کے ده وفای بواو رستده                     هت درغایت تراکت  -ونخم کشوث را بسریانی
وسین بینقطة ()e زده  ۰بلغت بونانی نوعی از                                                                دثار گوبند .
 خار باشد وبر گے آن بککرکاهو میماند و نآرا
 وون ازهم بشکافند
                شبرازی طوسك خوانند  .چ
                                                                 دینار اشمر (-ر دینار شمر سراف
                                                                                                                کوت
                                                                                                                  وا
کرمهای کوچك از مان ساق وبرکهآن برآ ند
 وآنرابتازی خسالکلب کوبند ومشطالراعی همان                       دبنارو له = با رای بینقطه ( )۱بواو
است  .اکر کل وشکوفة آنرا بکوبند و برشیر                          کشیده و فتح بای حطی ( ۰ )۲بسریانی گیاهی
 خواهند        کهعبرضدو
                      وبیند
                          مال
                            گوسفند بمالند درح                    است دوابی  ۴وب رکه آن بکرفی ماند و آنرا
                   بتر نف ضماد کنند بحس گرداند :
                                                                                        بشبرازی آهو دوستك خوانند.
 دیو  = ۲بااول بثالی مجهول رسیده                                 دبنادی  -بر وزن بماری » جشی از
وبواو زده  ۰معروف است وآن نوعی از شباطین
                                                                      جامةٌ اپرشمی  -ونوعی از شراب لعلی باشد.
 باشد  -و کمراه و کج اندیش و کج طبع را نیز
 کوبند  -کونابه ازمردم پهلوان ودلیر وشجاع                        دین پژوه  * ۲بکر بای فارسی
 باشد  -وفوعی ازجامةٌ پشمینه است بمیاردرشت                       وزایفارسی بواوکشیده وبها زده ,نام روزپاتردهم
بوه از  ا-ن۷  کشند
                 ز های جنگه پو    رهودرک                         است ازهرماه ملکی ؛ وحم بایفارسی همآمده
 اسب همهست که بعربیفرس خوانندھ ک-نوایه

     
=== leaf 378
      اه                                                                      دبوار خانه روزن شدن

آرا
  وسکون دوسین و فوقانی  ۰دوابی است که ن                            از قپر وغضب هم نوشتهاند .# ۷
انده قوقو گونند وبرکلف وبهق مالند تبافاعشد »         ررنوشدن ».کناه               نه
                                                                                    خواار
                                                                                        ذی
واگرطفلی دبر بحر کت بد چون برومالند زود                                  از خراب دن خانه باشد .
                                                     ديو ار گر = دبوارساز  وگلکار وینارا
دیوال  ۴سبا لام" بروزن ومعنی دیوار                                                            گونشد .
است» چه درفارسی راولام بهم تبدیل مییایند #.
۰    فرشت     رای   بفتح   دیواله رو
شخصیرا کوبند کهمدابنوندانهاسلوك کند وبراه                                عاجز وزبون هدن باشد .
                                            رود .    همز هو بایفارسی   د یو اسست  ۴یک


     - ۱نظر بتصور مهيب و هولناك بودن دبوان « .هرچیز را که از افراد خودفوی جثهتر
     و بزرکترباشد بدیو اضافت نمابند (با بفول که آنهم دو موهوم است) مثلاکمان بز رکه راکمان
     دیو خوانندیسنی دبورامیدابد .نوعی ازاسیسترا که -اق وبرگهآن ازامتال بزرکنراست دیوامیت
    گوبند  .کلوخ کلانرا دیو کلوخ » عنکبوت برزکه را دیوپا» زبراکه بابپای بزرکه و بلند
     دارده و گردناد را که بلند شود ديو باد گوشد» 9انجمن آرا» ولىز  :دیوحان › دیوچه ,دیوخاره
                       دبودار » دیودل» دیوزای» دیوسار » دیوگ » دیو گندم .ورك :فاب  ۱ص ٩۹۱.
     2وجنگه کرد      دبوار («.م).   -   ۴           امست («.م).    از  :دنو (ھ.م4 (.          ۳

    بسیار بدرارك » و کشتن کرد فراوانی بدر شارستان » در گرکوی عاقبت بستد » و ارك را و قلمة
                             زورین راء بعد ازان دبوالآ قرا ببرید « »...تاریخ سیستان 4۸۳٩ .
     #د یوار بکراول د=بوال د=ی=فال(عامیانه) ,بېلوی « 4۷8تاوادبا *۹۱وجهاشتقاق
      کنومله است .رك :اسشقءهوبشمان  ۹۹؛کردیع «rãvîd وخیع .13۷114سربکلی1۷164           آ
     اسشق  , ۹۹۵۰افقانیع  14۷1هوبمان  4۹۵جداری که دراطراف خانهبنا کنند بجهتمصور
             کردن و حفاظت آن » هرچیزی که ای را محصور کند خواه ازمصالح بنابی با حزآن.
    د#یوان بکر اول » ازکامة مفروض ایرانی  0261همریثة «دبیر ٩ ( نوسنده )
    وبقول اندرآی مرتبط بکامة آسوری « ۳21دائردالمعارف املام» وکلمة أن پارسی باستان که از
     کدی و نال سومری ( لوحه ,خط ) مأخون است « مجلة ابراشهر سال  ۱شمارء ۸       ۷
     ص «٩ ۷۹۱ - ۵۹۱فاب ۱ص . ۲۱۱معرب آن هم «دبوان» «دزی ح ۱ص ۹۷4 -۸۷4؛ دفاتر
     عمومی محاسبات  -موضع حساب -
=== leaf 379
  ديو دولت                                                                               ٩۱
باشد ساء رتگك  .چون       کفتهاند » و آنکرهی        دیو پا  - ۱با نانی مجهول وبای فارسی
                                                      بالف کشیده » عنکیوترا کوند و نگایماهیهم
 ه شور کنند هر اهنگر
                   خشبش
                      را خشك کرده در                 هت که آنرا انده قوفو و حندقوقی خوالند ٩
  شرشه کهدنرجااباشد بشکند وگیاهی همهت                       ودیو پای نگیفزتداند باضافةٌ تحتالیآخر 

                                                     دیو باد  ۱با نانی مجهول وبای ابجد
                             ِ   مدان اندام خار اد
                                                     بروزن دبوزاد ؛ بمعنی گردباد است  -وبادنندی
 دیو خار  ۰ ۱با خای شطه دار( )۱بر                    ویند که هوا را تاريبك سازد  -و جنون  گز
                                                                                           را ل
 پرخار؟ وآراسفید      وزن پیشکار " درختی است                              ودیوانگی را گنفزتهاند -
      خار وخفچه گوبند وبعربی عوسج خوانند.            جنهیول و بای ابجد
                                                                     بلنوك = بما ا
                                                                                 ك
    ن    دیودار  ۰ ۱باانی مجه
    وولزبر                                            بروزن ررشخند  ۰نام روزشانزدهم باشد از هرماه
 و صاوس       سروباشد؟   از درخت    بعلدار  .لوعی     ملکی -ولقب قارن برادر زاد جمشید هم هست
 هندی را نیز گویند و بعربی شجرةااجن خوانند            چه او را فارن دبواند مبگفتهاند و طرمورث-
و دراختبارات شجرةالله نوشتهاند ؛ وبضی گویند          وجمشید را هم میگویند .ونام داروبی همهست.
ای دارد که    درختی امست مانند درخت کاج وشره
                                                      دیو جامه  ۰ ۱با ای مجهول » نوعی
علاح لقوه میکند  -و مردم دیواله و مصروعرا            از جامةٌ پوستین باشد که آنرا واروله میپوشند
                                  لز گفتهاند . ۵
                                                      تا پشمهای آن بربالاآید وپرها برآن پکنندند
                                                     وشبها بشکاركبك روند » وبعضی گوبند جامه ای
 همان ددودارامت که درخت کاحمانند باشد وشیرء          باشد آزیلای انده که درر وزهای جنگ دوشد -
                  آن علاح استرخای اعضاکند .          و پوست شیر و پلنگه را نیز گویند کهبهادران
 بر وزن     دیودل  = ۱با ثالی مجهول                         وپهلوانان در روزمع رکه بردوش اندازند -
 شیردل» هردم شجاع ودلیر ودلاورباشد  -وهردم           دیو جان  -
```


## [2026-09-04T18:47:12.132Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (310,311,312):\n    pg=''.join(c for c in t[i] if unicodedata.category(c)!='Cf')\n    print('=== leaf',i); print(pg[:2200]); print()\nEOF"
}
```


### [2026-09-04T18:47:13.939Z] TOOL RESULT

```
=== leaf 310
                                              يان هفتم
                در دال بینقطه با زای نقطه دار مشتمل بر ده لغت


                          وزهره وعطارد باشد *.           در = بکر اول و سکون ثالی » قلعه
                                                          بالاخاله را   وبفتح اول کوثشك و        ۳ ۱       وحصارباشد
فلك  ,دمتار را گویند      بروژن    =   درك

دستارچه را    و روپاك است ؛ :و بى         که یل            کربند؛ و با زای ( )۱فارسی هم باين دو معنی
                                                                                                آهوه است (<( ۳
              گفتهاند که دستمال وروياك باشد ۰
                                                          رتا  -بکراول وسکون انی وفتح
                                                                                    داف
درمار = طم اول بروزن گلزار  .دام
                                                           لامحصاری     بالف کشیده ۰   وفای ساکن ۳              همر ه
جابی است کهکان سرب در آیجاست وکان نوعی
 لزاجور دهم متصل بدانهاست وآر الاحجو رددزماری
                                            ا
                                                           وقلعهایست که شاپوربنا کرده بودهاست ؛ وبجای
                                                                          فوقانی نون هم بنظرآمده است #.
                                        . ۵   کو
                                                            ۳دال ایح بروزن بیاره          9 ۳    دردار
و دال أ جد    اول   بكر        در ندیس ۰


بروزن فرنگیس  ۰بممنی همانا و ظاهرا و کوبا                             کوتوال وضابط وحافظ قلمه راکویند .

د بکراول وسکون ثالی               درهر چ                             معاون وباری دهنده وثربك دزد باشد .

وهای مفتوح برای فرشت ) (£وجیم رده » له                     دارورای      طینه
                                                                           قحش
                                                                             نبفل
                                                                                در دافشره = ۴
پیشینیان باشد و آنرا بسربالی ایلیا  ۷خواند                 ومماون     a تحعتی دزد افشار است .که عمق          بیقطه


                                                         

=== leaf 311
                                                               يان هشتم
                    در دال بینقطه با زای فارسی مشتمل بر سی وهفت لغت


دزاامه ه = بکر اول وفتح آخر                                                   = ۵بکر اول و سکون ثالی » قلمه
 بمعنی دژکام ات که زاهد ویرهیز کار )(٩ -                                    وحصارباشد - ۱وبمعلی زشت و,دوبدخوی وخشم
وخواجهسرا باشد ؛ وبفتحاول لز درست است.                                        نزد-
                                                                                   انی
                                                                                     را
                                                                                       هکی
                                                                                         تند
                                                                                           فبب
                                                                                             گوچ
                                                                                               وقهر نیزهست - ۴
دز ] اه  ۱ت باها بمعنی درآ پاداست
که سهمگن وخشمآ لود باشد  -وبداندش وتند                                                                                   ۰    است   درست   قىر




شده رانیز کرد  -کووتوال و محافظت کنندة                                       و دال         ایجد     با بای        دژ] باد  ۴ت
                                    ذلعه را هم گفتهاند ۰
                                                                             بر وزن اشارات » بمعنی سهمگین و خشم آلود
دز | گه »مخنف دگژاآه است  ۷که
خشمکن وقهرناك و-بداندیش  -وکوئوال قلمه
                                                                                                                                    &

                                                                             درا گام  = ۴با کاف فارسی بر وژن
                                                               باشف          زاهد         و یمعتی         دلارام »خواجه سرا را کت
بععتی      دل»
             لزونک
                 آبرو
                    دز ] لو  ۸ ۵س                                                                           وی

=== leaf 312
                                                                                                                        جد
      ح
      ب ۷ی                                                                                                           درا لون



دلنواز» بمعنی زشت خوی  -وبدلما و لا زیبا -                                 ۰   وقهر آ لود باشد       ومهم ناك        خشمگین

                                                                                                                 ~~
وخشم| لود وسهمگین  -وخام طمعوعیب جوی                            در | لون  -بروزن طلا کون  ۰تمعتی
باشد ؛ وبفتح انوفلزدرست است ؛ وبابای فارسی                      حیف ودریغ وافوی باشد ودرمۇ,دالفضلا بهمین
                          هم امده است .
                                                                ممنی بعد از واو الف نوشته بودند که دژالوان
دز براران  -و داژتیرابنابای ابجد                                                                                        باد .
 ۱است که بمعنی              از
                             رجمم
                                بی .
                                   ژارس
                                      دای ف
                                          وب                نظام    فارسیبروزن       ماف   a   ۱    درانگاه


               عیب جوبان ولا.زیبایان وغیره بلشد .          و خشمآ لود          گاهاست که سهمگین               بمعنیدژآ    شاه“



دز برو  = ۴بکراول ۸وسکون انی                                                                                    وقپر ناك باشد


واو ساکن » خشمگین
                وضم الث ورای قرشت و                         بهفتح ها و سکون نون                      هرن|ح؟
                                                                                                       ۰

                                                                                                          د      2   ب




وقپرآلود گوره برایرو زننده راگونند » ویفتح                      وجدم» بدخوی وخشمگین وسپمناك  -وکبرددار
                             اوز  ۸هم درست است .                باشد  -وبمعنیتیر تخش  -وژوبین ( )۱که سنان
دز بسن بتح اول  ۸سین بینفطه
                                                                دهرن|گه  « ۴باک
```


## [2026-09-04T18:47:21.482Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\npg=''.join(c for c in t[311] if unicodedata.category(c)!='Cf')\nprint(len(pg)); print(pg)\nEOF"
}
```


### [2026-09-04T18:47:23.375Z] TOOL RESULT

```
5057
                                                               يان هشتم
                    در دال بینقطه با زای فارسی مشتمل بر سی وهفت لغت


دزاامه ه = بکر اول وفتح آخر                                                   = ۵بکر اول و سکون ثالی » قلمه
 بمعنی دژکام ات که زاهد ویرهیز کار )(٩ -                                    وحصارباشد - ۱وبمعلی زشت و,دوبدخوی وخشم
وخواجهسرا باشد ؛ وبفتحاول لز درست است.                                        نزد-
                                                                                   انی
                                                                                     را
                                                                                       هکی
                                                                                         تند
                                                                                           فبب
                                                                                             گوچ
                                                                                               وقهر نیزهست - ۴
دز ] اه  ۱ت باها بمعنی درآ پاداست
که سهمگن وخشمآ لود باشد  -وبداندش وتند                                                                                   ۰    است   درست   قىر




شده رانیز کرد  -کووتوال و محافظت کنندة                                       و دال         ایجد     با بای        دژ] باد  ۴ت
                                    ذلعه را هم گفتهاند ۰
                                                                             بر وزن اشارات » بمعنی سهمگین و خشم آلود
دز | گه »مخنف دگژاآه است  ۷که
خشمکن وقهرناك و-بداندیش  -وکوئوال قلمه
                                                                                                                                    &

                                                                             درا گام  = ۴با کاف فارسی بر وژن
                                                               باشف          زاهد         و یمعتی         دلارام »خواجه سرا را کت
بععتی      دل»
             لزونک
                 آبرو
                    دز ] لو  ۸ ۵س                                                                           ویرهیز گار همآمده است .

                                                      چش  :برهیز کار .              ()۱               .    -ست
                                                                                                             ( )۱چك :ا

   ۹۳ ۳بابن معنی لفة بضم اولسحیح است»                                      اسلام ۰       و دائرة المعارف        دز    رك:      ۱


     .هلوی . 01511 -هندی باستان_ 5100
                                    دژ= دش » پارسی باستان _ 05لا " اوا  5110 -ب
 دشنام  ۰دشمن ) ودو ا گاه) آمده                  ِ دزخیم a           مر کب بل             ۰در کلمات       020 -       _ ۰ durآرئی 2

 آنجاکه از بدی              آباد " لفة »   ) +        ح ۲       از  :دژ (بضم اول  .رك :                   - ۴                اسشق داه“ .
 دژا کام۰         ۳۳ره :   o               ۰   دژکامه     ۰    درکام   ۰     امه
                                                                                رك :دکژا             ۴                وخشم معمور است .
 )      »مر کب از  :دژ( حرش                «مناس YT                   - ۷پهلوی sãkãhsud                                درکام  ۰درکامه ۰




                     چو بل در آ گاه ودرنده شس.                                              سوار جپان نبوزار دلیر
 دقیقی طوسی« .مزدیبنا 4۵۳-۵۵٩ .
                  دژ ( رکه :ج )  +آلود (لوآده) .                            ز:
                                                                             ۸ا_۵                    :د؟آ گاه ۰        رک       ۷


                                                                                                                بقه اصزفحهٌ ۰۵۸
                  (سارق)  ,بپلوی ن0ز2 = ( 60یا ) .                                    اسشق 41۵؛ دراوراقمانوی بپپلوی 20
                  Henning. A list of Middle                                   Persian .. , BSOS                        126, p. 82.
  کسکه        ب    صارق     ِ   ٩zûd ۳           ۳    €       ۸۷     گربرسن          ۶    0۵0۳2          وخی      ,           اشکآشمی 0


 دزدان عرب بر سر کوهی نشته بودند و منفذکاروان بسته »                                               ق:
                                                                                                  ةٌ بزن ط» ر
                                                                                                       ااه     مال مردم را بب
                                                                                                             «رد
                                                                                                                         «گلتان . ۱۲
 #زدیدی  -بض اول و فتح پنجم  ,از  :دزد -۳بدن ( پود مصدری ) ؛ سرقت »
                                                                  د
                                                                                                                       بردن مال مردم .
```


## [2026-09-04T18:47:38.330Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\npg=''.join(c for c in t[310] if unicodedata.category(c)!='Cf')\nprint(pg[2000:6000])\nEOF"
}
```


### [2026-09-04T18:47:43.198Z] TOOL RESULT

```
            در دافشره = ۴
پیشینیان باشد و آنرا بسربالی ایلیا  ۷خواند                 ومماون     a تحعتی دزد افشار است .که عمق          بیقطه


                                                                                           وشربك دزد باشد .
وسکونهابروزن سپرغم همگفتهاند  -وبتخالهرا
             ای فارسی همست -
                           نیزکرنند ؛ وزبا                 ساراترا کویند که زحل ومشتریومریخ و آفتاب

              ( )۳چك + :وقوفالی -                (() چك - :اک                   ( )۱چك :بزای .
                                                                                  ) (4چك :برا .

  = ڑر .).م.ھ( زد و زد نکمم تسا لکش یبهجپل دشاب یفا تیرکساس _ 4601                                   ١
  ( dêzتوده)   (  ۰آرھثی     نهادن   مدنگ    (انباشتن ٠ روی      اوستا_azeadzu     (سده بارو وحصار) ۰

   = ۴از  :دز (۶م +۳ ).دار (دارنده),                     «هوبشمان  ۰ ۳۹۵۰پپلوی « 2(1)0استق ۳و .
                 رك :افثار و دزد افشره ۰        ۴            .   معربآن نیز «رزدار» دزی جح۱ص ۹۴

   ت   دوم) قلمها   و تشد نف   (یکراول    کے درمار   ۵            افثار .   افثره و دزد    رك:         ۴


  » - ۱مدف وهشاف دڑ                           استوار از تواحی آذرباجان قردىك تبریز «ممجم ال لدان»
              :-ابلا .
                     رك۷                e دزهر ح )(۱     .رك :دزهضت  :دژهخت کنك  ۰دز دوست                   هوخت؟

   »nil « hZud ۰ ۷۲:۷ناوادیا ,dhzud« ۰۱:۲                       #دزد  -بضم ارل» پهاوی 7
  اوتا ( 020۳2بدجنس) ک»ردی ( 21سارق)(81210 .سرفت)» بلوچی< ۰ 2۱أا  .رك
  بقیه درصفبحةٌ۱۵۸:
```


## [2026-09-04T18:47:55.120Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (371,372,373):\n    pg=''.join(c for c in t[i] if unicodedata.category(c)!='Cf')\n    print('=== leaf',i); print(pg[1500:5200]); print()\nEOF"
}
```


### [2026-09-04T18:47:56.727Z] TOOL RESULT

```
=== leaf 371
خائة علفیاست بقا وتباتی                         دیده گه = بففتحاکرافسی بورزن
                                                                    نیمه ره » مخفف دبده گاه است که جلی نشستن
                                                     ندارد .

                                                                                                       دیده بان باشد .

 مردن :و فوت شدن باشد  -وکنایه از دورشدن                             دیدهور شدن ه کنابه از رسدن
                                    .       ©        هم هت           بجیز هاباشد چنانکه هت ونظرالداختن چنانکه
 دی مکافات  -کتابه از دبیا عوالم                                                                                باد .
                                            سفلی باشد .              كر ب=فتح اول بر وزن غير » معبد
      -ابه از فلك است .
                      دير میناًکن                                    رهبان راگوبندا  -وبکر اول بمعنی دوراست
                                                                    که اقيض ترديك باشد؟ و-مدت متمادیرا لیز
دار فك  = ۱بر وزن ریوند  .بمعنی
 دبرباز است که دراز - ,ومدت دراز  -ودرازی
زمان باشد  -وبمعتی دهر وزمان که دیا ومقدار                           دير بار س بابای ابجد بروزن پیشوازه
 ح ر کت فلك اعظمباشدهم آ مده ات - ۸وصویذ                             بمعنی درازاست که درمقابل کوتاه باشد  -ودرازی
                         بوازوبند را گیوزبند .                                            رمان ومدت را لیز گویند ۰


    = ۴دور » طبری ( ۲114دور) «ساب                          ( - ۱عی) ازسریالی «دائرةالمعارف اسلام» .
   ۴س-منالی » سنگری » سرخهبی وشهمیرزادی  ۳1دق ۲ .                                           :دور .   رك     طدری ۱

                     ۰    :لسوم»   «الابنيه          گوارر»    در    مود   شفه    مت    کوشت) جون      : ٩)۹٦دو(   ص


   --همرشهة بهلوی                       .       دی   رك:       ۵
                                                                                  _ ۴امر از « دیرزستن» .
                                                                                    « (عهد) طوبل»  .رك:         8
            Henning, Two central Asian words . Hertford . 1946, p.                                                  ۰
            چو نا بینا درو دوچشم مینا ۰                                 - ۲شبی دبرند و ظلمت را مهیا
  رود کی سمرفندی «.لفت فر ۱۰۱٩ .

         چون توبی دید و بیند این ديرد .                                      ۸بافتی تو بمال غره مشو
   دخت فری ۱۰۱
             رود کی سمرقندی .ل


=== leaf 372
و استر     صوص
                                                                                  مدخکه
                                                                                      ان            ه
                                                                                                    تیز
                                                                                                      گلفرا ن
                                                                                                            ماب
دیس د با نانی مجهول بروزن کیس.                               ادات دبگر که از کاکل تا   وخر و بحییواز
همتاومانندوشییهو نظیرباشد- ۸وبهندیبمعنی روز                    عنی م-ب۴ وشد
                                                                           دمش خطی سیاه کشیده شده با
است که بعربی بوم خوانند -وملك وولامت رانیز                       حصار وقلعه  7وجاست  - ۴ونوعی ازدیگه
                                          کوند ٩ .              ويال باشد ۴ونوعی ازشیاف است که درچشم

دیسقوریدوس  ١بکراولوضم                                          رمد کشیده کشند  و چنبر دابره  -و غربال
خامی که واو باشد
               قاف وسکون ثالی و الث و                                                   و پرویزن را دگیوزیند .
بواو   ابجد   دال   رسینه و   بی نقطه بتحتانی   رای   و          دار ندان  = °بروزنبیدندان» سهياية
دحاکمیمی است از                         ا+                       آهنی باشد که دیگه مین رابربالایآن گذارند

                                                                                      ( )۱چك :وزا.

  ازکامة _  2502باشد          آفایپورداود نوشته اند :شاید دیز»           ۴           رك  :ديرد      ۱

   :تمد یس ۰        دادن که در کلمات   وشان   مودن        اوستابی نمعتی       682   بمعنی نما ونشان  ۰ازمصدر -


  فرخاردییوطاقدیس آمده " بنابرین «شبدیز» لفة بمعنی شب نماء وتبدبل سینبزاه درکلمهاسپربی
  = اسپریز دیده ميشود .دیزودیزه جکداانه در ادبیات مابمعنی سیاء آمد وبوبژه ازبرای اسبسیاه
                                                          بکار رفته مانند شبرنگه وشبگون :
               کرو رده زصرصر در تك وتیز.                           یکی شبگون که امش بودشبدیز
                                             آیدز ر
                          .ودی ترديك دزقول ) .                     رك :دز  .دژ ؛ آب دیز (=           ۴
  معنی از باد کلمةٌ « دیگه » («.م ).د قاب اص  ۱۹۲ح» .قس :دیزیی ورك :                             ۴م-اين
  یابه ) |د بگدان  .دیگپابه ] ,ماز سرانی کنونی               س    (            طبری 0       ۶            دىزتدان .
                                                    ر=
                                ان) « راژه نامه . ۷۸۳  +ادان (                       0006211از د:یز 9
  ابا از        رن
                 ه_ھ                    رك  :دوز ١ دز » دژ.          ۴                 - ۱ره  :دیز
  ربشة اوستابی( 56۳20 -کء > نظر) ؛ حندی باستان ( 6۲0رویت » دیده شده )( - 49۴ ۰فظر
                                              ولی ه                           دیده شده ) میداند « اسشق roc
  وتمان آبرا از ره çid ساسکرت ) .شان دادن) 

   (ارائه) دانته «هوبشمان ۳۹٥٠ بر که هر دو                      اوستا کل ش(اندادن» ارائه) ,استی 81511۷3
   رده گووید  :در اوراق مانوی تورفان ( 560شکل .ساختمان)»مفدی 680-                هلوجه مذ کور را ک
   ,8ورك  :دیز» دی »دسهوص :له از 6 6 2 0 - : ۳ ۷ ه م ل ه ت ر ا ب : ك ر و ۹ ه ک رب ی (ساختن) آمده «
     »سلطنت)         ل»
                     ت اهره     ٩ مان کریت ( 456قطه  ,تاحیه »جا »س
                          اهمب» ب                                                                 دىياچة مۇلف .
            _  . sedirocsoiDطبیب بوالی ترن اول مبلادی .                                     « وبلیامز ٩٩4 :۲


=== leaf 373
اد خ
 مأخذ شهرستانی همان کتاب مزدکی یت  ۲ولی ابن امر بنظر مشکل میآبد زبرا اگر چنین
  کتابی در حقیقت وجود داشت چگونه باکمال اهمیت وی هيچبك از مورخان قدیم ابرانی وتازی
  از آن نامی ببردهاند ؟ قبربیبقن است که دبستان از شهرستانی بیروی کرده است  .شهرستانی
  ازفول او ( عنی      ا     نکات مهمی دریاب مزدك آورده وهمه را با حملمهای « وراق مگوید ۰.

  مزدك روایت میکنند » و نظایر آن آغا زکرده است  .از سوی دبکر در کتاب دستان المذاهب
  جملههای < و دربخشی از دیستاد » او (مزدك) میگوید» با  ۶ودرهمین کتاب میگوید  » ...ومانند
  آن تماما مطابق وفائم مقام جمله های مذکور از شهرستانی است  .چون کتاب « دبسناد» وجود
  خارجی نداشته طرز قرائت با منشاه این اسم عجیب برای مااهمیت چندان ندارد .حاعل باجاعلان
  ولمات قدیمی را بکار بردهاند ...پیداست که
                                          لیزکار خود را بکامال مپارت انجام داده و الفاظ ک
                       در برهان «دیسناد» براثر غلط در رسم الخط به «دیتاو» تبدبل شده .ر :
        Christensen, Le Règne du roi 2۷۵۵ 1..., ۵
  1925 p. 86 sqq İyi. p. 89, note 1.
 آبا « دیساد » دبستان مصحف «دربت دبنان» (یهلوی ( ) 4517۵0 _ 0061بعلی دار کان
  رك  :کتاب فوق
              دىن صحبح ) که بهپیروان آبين بوندس زردشت سلف مزدك اطلاق مشده (
       ۴بهلوی ( 62560شکل) «منای .*۱۷۲:۲                 تالف کربتنن ص ۷٩  )۸4 -یت ۲
                           = ۴دیورخش (ه.م ) :            رك :دش .       ۴            ورك  :دىس.


  دامفالی ٩۷٩ .    « منوچپری
  > ردیبرجای           ۲ص   « لك   آن دیفروجچس   مصحف   segyrbpiD    دىفروغس   عه    ©

                                                                                       (ھe.( . ۰
```


## [2026-09-04T18:48:08.267Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata,re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(365,378):\n    pg=''.join(c for c in t[i] if unicodedata.category(c)!='Cf')\n    hits=[m.start() for m in re.finditer('دیگ',pg)]\n    print(i, len(hits), pg[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T18:48:09.957Z] TOOL RESULT

```
365 0                                                             
366 0  =    6 ۵   ۱                                               
367 0 دي                                                          
368 1    سره                                                      
369 0    دور                                                      
370 0  =                                                          
371 0  در ند                                                      
372 4  n     Sh                                                   
373 0  دطروجاش                                                    
374 7  -4۱-                                                       
375 1                                                             
376 2   6                                                         
377 1
```


## [2026-09-04T18:48:12.856Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\npg=''.join(c for c in t[374] if unicodedata.category(c)!='Cf')\nprint(pg)\nEOF"
}
```


### [2026-09-04T18:48:14.413Z] TOOL RESULT

```
 -4۱-                                                                                      دنگ
                           آهنین باشد ٩ .       واز بونه برآورند تفلکه در ته بوته مانده باشد
 د یگ بر دینگ = بکسراولوسکون                     مرقشیشاست » وآنرا دیفروجس بحذف الف یز
                                                کفتهاند  .چون ارا سحق کنند وبرموی غلیظ
کاف آخر بر وزن بیخ ببریخ » م رکه موش                              افشانند رقیق وترم کرداند #.

                                                  دلگ » بکسراول وسکونانی معروف
                                                و کاف فارسی » بمعنی دی باشد که روز گنشته
                                                است  - ۱و بعربی خروس را کوبند  - ۴و با
 خسس   و   و دال بی نقطه  ,کنابه از مردم شل
                                                 تحتالی مجپول» ظرفیکه درآن چیزی پزند؟ -
                                     باشد 3.
                                                 وتوپ بزر که رالیز گویند که بدانکلوله برقلمه
دیل  -بر وزن فل » بمعتی تقعاه است                                                        اندازند .
 که طرف خط باشد چهتعرف نقطه بطرف خط             دیگ افز ار  - ۴افزار دبک را
کرده اند  -ودل را نیز گوبندکه بعربی قلب          گوند .یعنی آنچه دردیگه طمام ریز ندازنشود
                                                 و کشمش وبادام وفلفل ودارچینی وقرلفل وزبره
کوسفندان وکاوان و دیگر چاریابان در آنجا          ومانندآن ویعربی تابل خوانند وجمعآن توّابل
                                     باشند .             است  -ودنگه بزر که را نگیفزتهاند .

 دیلم = با اول بتحتالی مجهول رسینه               دیگ اورار ٩ با واو بوررن
 اکیلان
      وفتح لام وسکون میم ,نام شهپری است ز        ومعنیدیگه افزاراست که نخود وبادام کوشمش-
 وموی مردم! لجاپیچیده ومجد میباشد و یشتر                   ردنگه بز ر گے باشد ی     وداروی کرم ۳


 حربة ایشان تبر هیزم شکنی و زویین ( )۱امت        -عنیدیکدان وسه با
                                                                  دیگ پایه بم

                                                                   ( )۱چك :ژوبین .

                          تازی .   ک)اباف
                                         ( ۴عر                      .    :دی   رك    ۱


   (دبکه)) از بارسی باستان_ 861120     بقول هوبشمان دنگه فارسی (اففالیع ع            ۴
  کردی ع     ید بد آمده .عکل بهلوی gêd (دنگه) هیأت عازه انت از آن د هوشمان >» 14۹۵
   , dîzikافتانی ع  . 26060 , 884بلوچی ع 1862 1064 . 21 4وخیوسر بکلی
        = ۴دیکه اوزار  .رك :افزار.              « 8اسشق  . 4۹۰۰کیلکی  » 81ورك :دیز .
    - ۱ویز نر واقم راگونند (کاه شماری               = ۵دبک افزار  .رك  :اوزار .
   ۵ببنقل آزفپرست کتابخانة مجلس شورای ملی بنقل ازترجمةٌ فارسی صورالکوا کب عبدالرحمن
   = ۲۷عاوناعدا( »2فر) «لك ۲ص - ۸ ۰ .۱2۱کیلکی نبزاقل.رك :مد.                    صوفی).
                                               #دضاقوس  رك :دیشافوی ()
    #دیگر  -بکسر اولوفتح سوم» پهلوی lj_arak :1۱26101 _ « ayîtivd#اسفا»۱
    ۹۸ ۱و ۷0-درکلمه  ل  ,پازند  7381021فارسی دیک .قس  :پهلوی انل دریبکه
   ۷ورك :اسشق وهوشمانه . ۹۵مخفف آن «دکر» (ه.م ).؛ کلمهای که بیان میکند شخص با
  چیزیرا علاوه برشخص و چیزی که پیش بیان کردهاند » علاوه» زباده » باز ج*زازین  .جز از
                                                            آن  .مخفف آن د«دکر» (ه  .م).
```


## [2026-09-04T18:48:27.664Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata,re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in range(576,586):\n    pg=''.join(c for c in t[i] if unicodedata.category(c)!='Cf')\n    print('#',i, 'پالیز' in pg, pg[:70].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T18:48:29.674Z] TOOL RESULT

```
777
# 576 False بر ون دلدگار » بیعتی سار است که فگد باشد؟ _ ولگد کوب راه مگفتماند - و 
# 577 False ۳66 77 و همال پاش ۷ - . . باشنك - بروزنآونگ , خوشه کوچكث انگور را کوین
# 578 False .و شخصبکه اسباب خود را نمام بباژد - و زاهد و مجرد و عاشقی کهبنظر پاك ب
# 579 False ایا پا کنك - بروزن پازند . مطلق باقوتر) کوبند اعم از زرد و سفید و سرخ 
# 580 False پالای باشد » يك حرف را ساقط سازند بثا بر آن .ك الف را حذف کرده پالاهنگ
# 581 True خورند و معربآن فالوزح باشد! - وپاكوساف کرده شده از نش را یز گویند - و 
# 582 False ان » بر وزن جان , برکی باشد که آنرا در حذهوستان باآحك و فوفل خورندلالب
# 583 False ۳ پاهگیدی » با ها بروزن وارسیدن . بىعنی شکنجه کردن باشد . باهنگ بروزن 
# 584 False ۳ پایاوز اده ختح همزه و سکون واو و زای فارسی بالف کشیده و رای بیط مقئو
# 585 False ی پای بست » هرچبز را گوبند که درزمر با کوفته و مالیدهشنه باشد, اعماز ز
```


## [2026-09-04T18:48:32.720Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\npg=''.join(c for c in t[581] if unicodedata.category(c)!='Cf')\nprint(pg)\nEOF"
}
```


### [2026-09-04T18:48:34.516Z] TOOL RESULT

```
خورند و معربآن فالوزح باشد! - وپاكوساف
کرده شده از نش را یز گویند - و بممتی کته
ترازو هم آ هده است .
بالوش- بروزن آغوش؛ کافورمفشوشرا
کوند» و بلین بی قطه هم درست است .
بالو نه هه بر وزن وآژونه. بمضیپالوانه
است که ترشی الا باشد؟ .
با لهنگه ۴ - بممنیبالاهنگهاتوآن
دوالی ورسمانی باشد کهبر کنارلجام اسب جنببت
بندند» وصید و شکار و مجرم و گناهعار را نیز
بدانمحکم بر شدند و کمند دوشاخه وچویکه
بر کردن سکد نهند - ونزد مجردین آنچهباعث
تعلق باشد .
بالیدن؟ بر وزن حالیدن ؛ بمسنی
جستجو کردن و تفحص تنمودن و صاف کردن
باشد.
پالیه * ح بر وزن تا دیده , صاف
شده وصاف کرده . و خلاصه را گوبند - وبمعنی
افزوده حم هت وججو کرده ونف<صلمودمرا
نی زگوبند .
(۱) خم ۳: شبه .
هالیز ۱ ۰ بر وزن کاریز » بمعنی باغ
و وستان و کشت زار باشد عمومات و خریزهزار
وخیار زار و هندوانه زار را گویند خصوسا ۰
پالیز بان۷ - بافبان و بتان بان -
ودهقان و نگاهدارنده فالز را گویند- وتمصوتی
است از موسیقی .
با لیز و ان 2 با واو بروژن وععنی
پالیزبان است که محافظت کننده باغ وبوستان
و فالیز باشد - ونام صوتی است ازموسيقی .
پاليك - بر وزن باربك , پاتابه و پا
پیچ را گوند - و لفافه را نیز گفتهاند - وبمعنی
کفش و بای افزار چردن همآعده ات .
۵ ه بر وزن معنی وام است کهفرض
باشد*٩- و بمعنیشیبه(۱) ونظیرومانند- ورنگگ
ولون عمآمده است ٩۱ #۶
پاهس » بفتح میمبروزن اکس »بمعنی
پای بند باشد بعنی شخصبکه در شهر خود با
مه کر از ترا
بطرف دیگر رفت و در آنجا نز تنواند بود ٩۴
۳ ۳۳ ره 4 مالوانه :
پالودجان خویش بيالونة بلا
۴ رد : بالاهشگه ۰
و هم بمعتی نرأوبدن, زهیدن :
چودید ان بر و چهرء دلیذس
زستان مادر بپالید شیر. فردوسیطوسی.
بیاراست شهری زکاخ بلند
(بسوند حفاظت). ٩ - 4: اغتنامد.
ص : لو از دسباچة مولف .
۸ مر کب از: پالیز ۳ وان
۶۰ له : وام. 2-68 : فام و نیز
بقبه در فص ۳۹۶
```


## [2026-09-04T18:48:41.588Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport unicodedata\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (582,):\n    pg=''.join(c for c in t[i] if unicodedata.category(c)!='Cf')\n    print(pg)\nEOF"
}
```


### [2026-09-04T18:48:43.288Z] TOOL RESULT

```
ان » بر وزن جان , برکی باشد که
آنرا در حذهوستان باآحك و فوفل خورندلالبهارا
سرخ گرداند ِ#
پا نسنك - بنتح نون وسیبی نقطهبر:وزن
اه ۰ معنی فرسسده و احوال کر فتهباشد. #۶
که در ز بر درخانه نهند تادر بسته کشودهنگردد
و درود گران در شعاف چوبی که مشکافند فرو
«ر ند و کفش دوزاندرفاصله کفش و قالب گذار ند.
۹ نقطه دار ار بروزن فالز »
: رس
اکق بحتان  رس مر ارآ
حست؛ و فانین معرب | نت.
پاو « بسکون واو. بمعنیشتنویا کیزه
کردن باشد- وبهندیپایرا گویند که عربان رجل
۱ - تودادی مرا زور وا
۴ وله: پااورنجن . ۳"
دلمان چواب بامی ننمان بهار با دی
6 6 سس
خواننف .
یاو فرح بانح بای فاری بروزنداد گر»
بمعنی قدرت و نوانايي و تاب و طافت باشدا .
باو چك - بفتح جیم فلرسی بر وزن
چاريك » سر گی نکاو خشك شده را کوبند اعم
ازا نکه خود خشاك شدهباشد بادست بهنساخته
وخشك کرده باشنف ۰
پاود نحی  بفتح تاك و رای قرشت
وسکون نون و جیم مفتوح بئون دبثر زده ؛
خلخالرا کر بند, و آن حلقهایست از طلا و نقره
و امثالآنکه زدان در بای کنند ۴ -
باو فك - بروزن پابنده بندی باشد که
در بای کناهکاران و مجرمان قارف ..
باه . بر وزنحك 0 بمعنی شکنجه
باشده و آنآزاری است که دزداترا کنند؟ .
.کش کرده باد باهك. ابوشعدپ.
بفد ازصفحدٌ ۳۵۹
« کل گلاب ۲۵۲ 4 .
» است «لفت نامد؛ .
دقیقیطوسی.
. «لفت نامه؟.
( برهان فاطع ۵۰ )
```


## [2026-09-04T18:48:56.050Z] TOOL CALL #78: Bash

```json
{
 "command": "ls data/verification/sources/web/ | head -5 && python3 -c \"\nimport json,glob,os\np='data/verification/sources/web/index.json'\nprint(os.path.exists(p))\n\" ; ls data/verification/sources/"
}
```


### [2026-09-04T18:48:57.854Z] TOOL RESULT

```
01a350f2398643fc.txt
03ddfbfafbdac423.txt
0420221ac764ad13.txt
0422a99755c9a7d1.txt
08eae3a92d63770a.txt
False
MISSING_REFERENCES.md
refs
refs_online.json
SOURCE_MATRIX.md
web
```


## [2026-09-04T18:49:02.145Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ntimeout 300 python3 tools/fetch_source.py 'https://vajehyab.com/?q=%D8%AF%DB%8C%D9%88%D8%A7%D8%B1&d=moein' --note 'page 126, root Dheigh, node 2 divar: Moin entry' 2>&1 | tail -5"
}
```


### [2026-09-04T18:49:04.088Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/82a264e1e3aab5c3.txt
```


## [2026-09-04T18:49:06.459Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nhead -c 2000 data/verification/sources/web/82a264e1e3aab5c3.txt"
}
```


### [2026-09-04T18:49:06.505Z] TOOL RESULT

```
URL: https://vajehyab.com/?q=%D8%AF%DB%8C%D9%88%D8%A7%D8%B1&d=moein
FETCHED: 2026-09-04T18:49:04Z
STATUS: 200
TITLE: معنی دیوار | واژه یاب

'
 />

 معنی دیوار | واژه یاب 

 26 فرهنگ 
 220 مدخل

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مشابه آوا متن آغاز قافیه 

 دیوار
 divār
 معنی

 آنچه از خشت و گل یا سنگ یا آجر یا چیز دیگر در کنارۀ زمین یا چهار سمت خانه یا حیاط درست کنند و جایی را با آن محصور سازند.
 مترادف

 ۱. جدار 
۲. آوار 
۳. بارو، حصار
 دیکشنری

 enclosure, wall

 جست‌وجوی دقیق

 دیوار
 فرهنگ انتشارات معین
 [ په . ] (اِ.) 1 - جداری از سنگ ، چوب ، آجر و غیره که اطراف خانه ، زمین و باغ و غیره به جهت محصور کردن و حفاظت آن بنا می کنند. 2 - حایل میان دو چیز. ؛ ~ کسی کو

 جست‌وجوی مشابه

 کاغذ دیواری
 فرهنگ انتشارات معین
 ( ~ .) (اِمر.) کاغذ کمابیش ضخیم ، بادوام و معمولاً دارای نقش ، برای پوشش دیوارها.

 گنج دیواربست
 فرهنگ انتشارات معین
 ( ~ِ بَ) (اِمر.) گنجی که در زیر دیواری در حال فرو ریختن قرار داشت ، خضر (ع ) می دانست و آن دیوار را درست کرد.

 دشوار
 فرهنگ انتشارات معین
 (دُ) [ په . ] (ص مر.) سخت ، مشکل .

 دوار
 فرهنگ انتشارات معین
 (دَ وّ) [ ع . ] (ص .) بسیار گردنده .

 دوار
 فرهنگ انتشارات معین
 (دَ یا دُ) [ ع . ] (اِ.) گردش سر، سرگیجه .

 جست‌وجوی متن

 گنج دیواربست
 فرهنگ انتشارات معین
 ( ~ِ بَ) (اِمر.) گنجی که در زیر دیوار
```


## [2026-09-04T18:49:11.535Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor w in دژ دیگ فردوس پردیس; do\n u=\"https://vajehyab.com/?q=$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" \"$w\")&d=moein\"\n echo \"### $w\"; timeout 300 python3 tools/fetch_source.py \"$u\" --note \"page 126, root Dheigh: Mo'in entry for $w\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-04T18:49:14.946Z] TOOL RESULT

```
### دژ
/home/sfmqrb/git/rishe/data/verification/sources/web/3fe779a77ac8e416.txt
### دیگ
/home/sfmqrb/git/rishe/data/verification/sources/web/a7c7baa23c7970eb.txt
### فردوس
/home/sfmqrb/git/rishe/data/verification/sources/web/00738e15ee065d37.txt
### پردیس
/home/sfmqrb/git/rishe/data/verification/sources/web/82811e916d5ded85.txt
```


## [2026-09-04T18:49:18.024Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 3fe779a77ac8e416 a7c7baa23c7970eb 00738e15ee065d37 82811e916d5ded85; do echo \"===== $f\"; sed -n '1,40p' $f.txt | grep -A4 \"جست‌وجوی دقیق\" ; done"
}
```


### [2026-09-04T18:49:19.654Z] TOOL RESULT

```
===== 3fe779a77ac8e416
 جست‌وجوی دقیق

 دژ
 فرهنگ انتشارات معین
 (دِ) = (اِ.) دز: حصار، قلعه .
===== a7c7baa23c7970eb
 جست‌وجوی دقیق

 دیگ
 فرهنگ انتشارات معین
 [ په . ] (اِ.) ظرفی که در آن غذا پزند. ؛ ~را بار گذاشتن کنایه از: کار را شروع کردن .
===== 00738e15ee065d37
 جست‌وجوی دقیق

 فردوس
 فرهنگ انتشارات معین
 (فِ دُ) 1 - باغ ، بوستان . 2 - بهشت .
===== 82811e916d5ded85
 جست‌وجوی دقیق

 پردیس
 فرهنگ انتشارات معین
 (پَ) (اِ.) فردوس ، بستان .
```


## [2026-09-04T18:49:27.383Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -l \"دزفول\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null\necho \"---\"; grep -o \"دزفول[^\\n]\\{0,120\\}\" incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -5\necho \"--- part\"; grep -o \"دزفول.\\{0,150\\}\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5"
}
```


### [2026-09-04T18:49:29.088Z] TOOL RESULT

```
MON_part2.txt
incoming/MON/MON_2vol_Adena_v2_djvu.txt
---
--- part
MON_part2.txt:دزفول - ۳۵ کیلوگرم. ور 
MON_part2.txt:دزفول و شوشتر وجود دارد و «حیز»
```


## [2026-09-04T18:49:34.418Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"دژپل.\\{0,200\\}\\|دز پل.\\{0,200\\}\\|دژ پل.\\{0,200\\}\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v*_djvu.txt 2>/dev/null | head -10\necho \"=== BQT dezful\"; python3 - <<'EOF'\nimport unicodedata\nfor f in ['BQT_v2_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    for i,pg in enumerate(t):\n        p=''.join(c for c in pg if unicodedata.category(c)!='Cf')\n        if 'دزفول' in p or 'دژپل' in p:\n            print(f,i,[l for l in p.split('\\n') if 'دزفول' in l or 'دژپل' in l][:3])\nEOF"
}
```


### [2026-09-04T18:49:36.713Z] TOOL RESULT

```
=== BQT dezful
BQT_v2_pages.txt 2 [' امام (محمدعلی) (دزفولی)؛ لسانسية دانشکده ادیات و دیرادبیات فارسی در', '                                       بغداد (لغات دزفولی وانه کی از لغات شوشتری).']
BQT_v2_pages.txt 12 ['                 - ۳رك  :جال و جاکی .               - ٩۳در دزفولی  216کویند .               ۲۷۰']
BQT_v2_pages.txt 119 ['    - ۸چنانه ,نام یکی ازطوایف اطراف دزفول است                           و رک  :ابتی.*۷۷۱']
BQT_v2_pages.txt 125 ['        - ۴طبری لا» (چوب) «صاب طبری ۰۰۳٩۰ دزفولی ( 6چوب) ر که :چوب .', '  نآ  ,لاسگردی  1۷کدے .ص ۱۹۱دزفولی  ,06طبری!« »1صابطبری .»۰۰۳کینکی 0نا»»']
BQT_v2_pages.txt 184 ['                       نهمرزادی  « 8200721ك ۲ :ص  ۲۸۱۰دزفولی ,2726072:7                         6']
BQT_v2_pages.txt 186 ['      .دزفولی      ۳۲']
BQT_v2_pages.txt 192 ['                                                           ۸ : ۲ص  » > ۸۱۱دزفولی . 80165121']
BQT_v2_pages.txt 228 ['        ۳" ۰۷ر که :خمدان.                      از :خم  +ستان ( پنوند مکان).                        ٩                 دزفولي .871']
BQT_v2_pages.txt 251 ['  اهواز (مرکزاستان)  -شوشتر (کرسی آن نا اواخر عهد قاجاربه) _دزفول-خرعشهر( محمره )-']
BQT_v2_pages.txt 277 ['              کیلگی .4۳2اورامانی « 01۷20182ك .اورامان  ۷۲۱۲۰دزفولی  010ک']
BQT_v2_pages.txt 286 ['                                                            دزفولی » 78060مکر']
BQT_v2_pages.txt 315 ['   ولاسگردی ] , 520شهمیرزادی  , 521سرخهبی ۲. ۰2 4520ص  .» ۹۸۱دزفولی  .524معرب']
BQT_v2_pages.txt 338 ['     ودتبال » چنانکه « نهاوند» فيزمرکب است از نها“ بممنی پیش » واکنون درلهجه های دزفولی']
BQT_v2_pages.txt 412 ['     بلوچی« 97101اسشق شمارء ۱۷وص  ۷۳۱ورك :منای  »)6105172( ۷۲:۲دزفولی « 0156۲امام»:', '     «امام» ک»یلکی ط 5۵۲و درتهرانی  98۴ب(کرراه )                 دزفولی و خواداری که           ۸']
BQT_v2_pages.txt 433 ['  ر(زق یومیه) « هوبتمان  > ۹۲۱دزفولی  « 6120۲امام»؛ رزق » اصیب وقسمت و بهره و حط:']
BQT_v2_pages.txt 555 ['  =یدرود ۴مرادسپید رود (ه.م ).سف             ˆ س .»۵۹۱دزفولی « 06:56امام» ,کمشجه . 856']
BQT_v2_pages.txt 558 ['                    «اسشق  ۰ ۱۱۷۲دزفولی  31252و  8۲2065دامام»  .گیلکی . 2۲8125']
BQT_v2_pages.txt 639 ['   ولاسگردی  » 8085سرخهیی .8085شهمیرزادی .+ « 8025ص,»۱۸۱دزفولی « 8065امام» .']
```


## [2026-09-04T18:49:42.412Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN\ngrep -n \"پردیس\\|پالیز\\|پیرادیز\\|فردوس\\|دژ\\b\" IRN_pages.txt | head -20"
}
```


### [2026-09-04T18:49:42.489Z] TOOL RESULT

```
124:دو دژ مادی ۳۹
448:(شاهنامهٌ فردوسی)
918:دژ پیش از تاریخ ایرانیان در سیلکه (کاشان)
936:خود دژهای‌جنگی با دیوارهای دوگانه وسه گانه وبرج‌های نگهبانی ساختند و در
937:پیرامون دژها خند قکندند,
946:دیده‌می‌شود . درسیلک» نزد یک روستای پیش ازتاریخ بومیان؛» آثار یک دژ مستحکم
1174:دو دژ مادی درسدهٌ هشتم پیش از میلاد - نقش برجستهُ آشوری
1435:از جای سخت گذری بالا رود و قلعهٌ سارد را بگشاید . دژی که تصرف ناشدنی
2265:می‌ساخت وقابی شیشه‌ای برروی نقش استواز میکرد تا بقول فردوسی» «از باد و
2982:کاخهای‌خود باغهای بزرگك پردرخت ایجاد میکردند که بدانها پردیس! می گفتند
2990:شاهنشاه‌هخامنشی» هنگامی که«لیزاندر»" فرستادةٌ متحدان‌راپذیرفت .اورا به پردیس
3006:ا بار دیگر پردیسی بزرگك خواهد گشت.
3038:پردیس (فزدوس) است . این باغ ها پر ازهمةٌ چیزهای خوب وزیبائی اس تکه زمین
3081:نسخه تهیه کنند که یکی‌در دژنهشت و دیگری درگنج شیزیکان نگاهداری‌می‌شد؟ .
3083:دژنپشت بمعنی دز با مامتان و و :
3087:این دژٌ به گمان باستان شناس‌نامی رک
3103:گنج شیزیکان » یکی به دژنپشت داشتن فرمود»
3135:دژنپشت وگنج شیزیکان ۹۷
3159:اندر استخر پاپکان به دژنپشت نهاده بود » او پتیار بدیخت » بی‌دین » دروند »
3192:۱- «درییشت» شکل خراب شدهٌ «دژنهشت» است
```


## [2026-09-04T18:49:44.999Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN\nsed -n '2975,3045p' IRN_pages.txt"
}
```


### [2026-09-04T18:49:45.046Z] TOOL RESULT

```
برهزار وسیصد شتر با رکردند وبه بغداد بردند وهنگامیکه بنزديک بغداد رسیدند

این داستا ن که بسیاری از تاریخ نویسان آن را نقل کرده‌اند هرچند ممکن
است اغراق‌آمیز باشد ولی گویای احترامی اس ت که ایرائیان نسبت به درختان
کهسال داشتند.

پادشاهان هخامنشی به پروردن درختان توجهی ویژه داشتند و در پیرامون
کاخهای‌خود باغهای بزرگك پردرخت ایجاد میکردند که بدانها پردیس! می گفتند

- نگك, گفتار بهشت در کتاب جهان فروری . انتشارات دانشگاه تهران » ص ۱۳۳
[pdf page 102]
درخت ۹۱
وهمین باغهای پردرخت وزیبای دوران هخامنشی اس ت که مفهوم « 28۶288 » بمعنی
بهشت را در یونا ن کهن وسپس درکشورهای اروپایی بوجود آورد . کزنفون مورخ
معروف یونانی‌د رکتاب «۱ کونومیکك»! آورده اس ت که کورش کوچک برادر اردشیر
شاهنشاه‌هخامنشی» هنگامی که«لیزاندر»" فرستادةٌ متحدان‌راپذیرفت .اورا به پردیس
خود که درسارد ایجاد کرده بود برد وآن‌باغ زیبارا باونشان‌داد , «لیزاندر» از دیدن
درختان زیبائ ی که بافاصله های معین در خط مستقیم کاشته شده بودند وبوی عطر
از آنها برمی‌آمد مبهوت ماند وبا شگفتی گفت من از این همه زیبائی در شگفت
مانده‌ام ‏ وکسی‌را که این باغ را برای تو چنین آراسته است تحسین می کنم .کورش
که از این تحسین شاد شده بود گفت «لیزاندر» همه این فاصله‌ها را خود من اندازه
گرفته‌ام وبرخی از این درختان را هم خود مکاشته‌ام .

ایرانیان با احترام ی که به درخت می‌گذاشتند توانسته بودند پهنه‌های سر
سبز وسیعی را در سرزمین ایران بوجود آورند» بطور ی که تا صد سال پیش بسیاری

از سرزمین‌های خشک وبید رخ تکویری پوشیده از جنگل‌های سرسبز وانبوه بود و
جهانگردان خبر از جنگل‌های بزرگی‌میدهن د که در زیر سای آنها راه پیموده‌اند و
امروز از آن جنگل‌ها جز دشت‌های خشک چیزی بجای نمانده است و تنها تک
درخت‌ها ی کهنسال گز یا تاغ گواه روزگاز آبادانی این دشت‌هاست وا گر قانون حفظ
درخت به زندگی صاحب درغت زیانی‌نیاورد چندی بیش نخواهد گذش تکه ایران
ا بار دیگر پردیسی بزرگك خواهد گشت.

ر- صطم22620 بقق 1۷ هن ونهم ۳۵۵2 ۲ 076 نا
[pdf page 103]
[pdf page 104]
کشاورزی
آنگا ه که تو ای مزدا» آن خرد مینوی را آزادگذاشتی‌تا به
دلخواه خود به کشاورزگراید یا به دیگران » پس او »
ازاین دو » کشاورز گله‌پرور را داور درستکردار خویشر
برگزید » آن پاسبان منش نیک را . (یسنا » هات ۳۱)
کشاورزی در ایران باستان از وظایف مهم اجتماعی ومذهبی بود وایرانیان
از سرزمین خشکه وبی‌آب خود همواره بهشتی زیبا می‌آفریدند .
سقراط فیلسوف بزرگك یونان دربارهٌ دلبستگی ایرانیان‌به کشاورزی باشا گردش
کریتویول!» چنین می گوید۲:
شاه ایران توجه بسیار دار د که زین بوسیلةٌ ساکنان آن کشت شود وتوسط
لشکریان محافظت و نگهداری شود و برکشاورزان ولشگریان» هریکك سالاری
جداگانه گماشته است.
برخی از سالاران برافراد غیر لشکری وکارگران گماشته شده‌ان دکه از آنان
مالیات می گیرند . برخی دیگر برلشکریان و بر پاد گان‌ها فرمان میرانند . ا گر فرمانده
لشکر» از سرزمین ی که بدو سپرده شده است خوب نگهبانی نکند » سالار ی که بر
افراد غیر لشکری گماشته شده است وبه کارهای کشاورزی می‌پردازد» از او به شاه
شکایت می‌برد. زیرا» اگر در سرزمینی امنیت نباشد واز روستائی وتحصول او
نگهبانی نشود» وی نمیتواند درکشتزارخود به کار پردازد . اگر به عکس فرمانده
لشکری امنی تکارگران‌مزارع را تأمین کند ولی فرباندار غیر نظامی زمین‌ها را بایر
وناکشته بگذارد» وجمعیت بکاهدء» دراين صورت فرمانده لشکری شکایت پیش
شاه می‌برد . زیرا این محقق اس ت که کشاورزانی که بد زراع تکنند» نمیتوانندغذای
پاد گان را تأمین کنند وقادر به پرداخت مالیات نیستند. در آنجا که شهربی وجود
«- علیامازون0 ۳ 0طم 260 جوم ,1۷ را ونصمدممت
[pdf page 105]
۹ ایرائویج
دارد» اوبرهر دو سالار لشکری و کشوری نظارت می کند . شاه درهر شهر ی که خانه
کند ویا از آن بگذرد» مراقب است تا باغ هائی در آنها بوجود آی د که نام آنها
پردیس (فزدوس) است . این باغ ها پر ازهمةٌ چیزهای خوب وزیبائی اس تکه زمین
می‌تواند در خود بپرورد وشاه بیشتر اوقات فراغت خود را در فصول مناسب دراین
باغ ها میگذراند.

ای کریتوبول: می گویند» هنگامی که شاه جایزه می‌بخشد» نخس تکسانی را
فرا میخوان دکه در جنگك ارزش وارج خود را نشان داده‌اند» زیرا اگر برای. زمین
کشت شده نگهبانی نباشد »کشت و ور پیهوده خواهد بود.
```


## [2026-09-04T18:50:06.910Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"dida\\b\\|didá\\|did[āaà]-\" TLM.txt | head -10\necho \"=== SOD dyz\"; grep -n \"dyz\\|δyz\\|δiz\" SOD_pages.txt | head -15\necho \"=== NYB distan\"; sed -n '1280,1300p' NYB_vol2_glossary.txt"
}
```


### [2026-09-04T18:50:07.001Z] TOOL RESULT

```
225:13.  ft'itiy  Darayavaus  Xsaya^iya  naiy  aha  martiya  49)naiy Parsa  naiy  Mada  naiy  amaxam  taumaya  kasciy  hya  avam  Gau- 50)matam  tyam  magum  xsa0ram  dltam  caxriva  karasim  haca darsma"2  a-51)tarsa  karam  vasiy  avajaniya  hya  paranam  Bardi- yam  adana  avahyar-52)adiy  karam  avajaniya  matyamam  xsnasa- tiv  tya  adam  naiy  Bard-53 )iya  amiy  hya  Kuraus  pu0ra  kasciy naiy  adarsnaus  cisciy  0astana-54)iy  pariy  Gaumatam  tyam magum  yfita  adam  arasam  pasava  adam  Aura-55  )maz[d]am  pati- yavahyaiy3  Auramazdamaiy  upastam  abara  Bagayadais  56)mahya X   raucabis  0akata  ahan  ava0a  adam  hada  kamnaibis  martiyai- bi-57)s  avam  Gaumatam  tyam  magum  avajanam  uta  tyaisaiy fratama  mar-58)tiya  anush'a  ahaDta  Sika[ya]uvatis  nama4  dida Nisaya  na-59)ma  dahyaus  Madaiy  avadasim  avajanam  xsa0ram- sim  adam  adlnam  va-60)sna  Auramazdaha  adam  xsayatfiya abavam  Auramazda  xsa0ram  mana  fr-61)abara
299:8.  0atiy  Da[raya]vau[s  xsa]ya[0]iya  patiy  duv-38)itiyam  harni- 0riya  kangmata  paraitfa  pa]tis  [Dadajrsim  kamaranam  carta- 39)naiy  Tigra  nama  dida  Arm'ni[yaiyJ  avada  kamaranam  aku- nava11 A-40)uramazdamaiy  upastam  abara  vasna  Aura[mazda]ka kara  hya  mana  a-41)vam  karam  tyam  bami0  iyam  ajan  vas[iy ©iiravajkarakya  makya  XVIII  42)raucabis  Sakata  akan  avaftisam hamaranam  ka[rtam]
300:9.  0atiy  Daraya-43)vaus  xsaya0iya  patiy  0’itlyam  ka[m]i0r[iya] hangmata  paraita  pat-44)is  Dadarsim  hamaranam  cartanaiy U[yam]il6  na[m]a  dida  Arm'niyaiy  a-45)vada  kamaranam  aku- nava11 Auramazdamaiy  upastajm]  abara  vasna  Aurama-46)zdaha kara  hya  mana  avam  karam  tyam  ham[i]0ri  [yam]  [a]jan  vasiy ©fiigarca-47)is  makya  IX  raucabis  Sakata  iikau  ava[0as]am  kama- ranam kartam  pasava  48)Dadarsis  cita  mam  amanaya  Ar[m‘]ni- [ya]iy  [y]ata  adam  arasam  Ma-49)dam
394:57) m  utasam  I   martiyam  ma0istam  akunaus  ava0asam  a-58)0aha paraita  Vivanam  jata  uta  avam  karam  hya  Dilraya-59)vahaus xsaya0iyahya  gaubataiy  pasava  hauv  kara  asiya-60)va  tyam  Va- hyazdata  fraisaya  abiy  Vivanam  hamaranam  cartanaiy  K-61)ap- isakanis  nama  dida  avada  hamaranam  akunava"  Auramazdamai- G2)y  upastam  abara  vasna  Auramazdaha  kara  hya  mana  avam karam  tya-63)m  hami0riyam  ajan  vasiy  Anamakahya  miikya  XIII raucabis  0akata  aha"  a-64)va0asam  hamaranam  kartam
415:Vivanam  hauv  amfufe1  ha]da  kamnaib-72)is  asabaribis  asiyava Arsada  nama  dida  [Hajrauvatiya  a-73)vapara2  atiyiiis3  pasava Vivana  hada  kara  nipadi[y]  t[ya]iy4 *  asiya-74)va  avadasim  agar- baya u[t]a  martiya  tyaisaiy  fratama  anusiya  75)aha"ta  avaja"
1181:avapara,  adv.  there  along ,   there  before.  Read  thus  in  Bh.  2. 1.  72  for  avada  of  ed. ;   cf.  KT,  35.  Bh.  3,  12.  arsada  nama  dida [ha] rauvatiya  avapara  atiyais  (Bartholomae,  Gl’undr.  360).  KT plainly  record  the  reading  avapara,  thus  setting  aside  Foy’s  con- jecture avadapara.  ava  (acc.  sg.  n.)  -f-  *para,  before ,   Av.  para,  Skt. pura.
1509:dida,  f.  stronghold .   Nom.  sg.  dida.  Acc.  sg.  didam.  New Pers.  diz;  cf.  YAv.  diz,  heap  up.
=== SOD dyz
9070:                                                                                                                  *wdyz-
9123:     be numbed                                                    1867 Nitfynt     B => >wdyz-
9126:1856 *>wps- S                                                          o5ez ?, o5ez ? =^wdyz-
9146:      o/upde    (>wbty)     ©pp. pi. -t =»}wfc                    1871 Svdyz-      C                              j^^
14546:      demon-like                                                           5iza (dyzO ©<OP dida           ©f. n.
14550:      5cw-mec                                                         3826 dyz> C «* 5yz>
24138:     py8ez (prdyz) ©Av. pari-daeza ©ob. -y; pi.                   parxut ©pt. st. =»prywn-, prywt*k
24145:7104 prdyz C *=» pr8yz                                            parxez ©<* para-hazya- ? =^pryyz-
=== NYB distan
dil [dyl, dl; LBBH] heart 73. 117-21, 2521, 20?, v. also dilé-név. — SW form: MPrs dyl, Paz. NP dil, as against MPrth zyrd; Av. (1692) zarad-, zaradaya-. :
diléh bravery 4!.
dile-nev [dly TB] 231? (2418.20), dil-nēv [dl TB] 297°. (301-5): "good of heart" = brave, gallant. — dile cas. obl. of dil, v. nev.
dipivar [dpywr] secretary ŠPrs: 9. 15. Pl: 7; pl. eas. obl. —-an mahist the chief secretary 1119. 1821. 1925, — FrP 15, MS K dpywl (= dipīvar). Olr "dipi-vara- from OP dipi- ‘inscription’, BP dyp ‘document’, MPrth dyb ‘letter’ + "vara- from Av. (1360) 'var- ‘to cover, to hide, to preserve’, thus ‘he who preserves the documents’. Early contracted to dipir: Arm lw. dpir Yoxupaveóc; KZSPrth 1. 24 dpyrwpt = Prs l. 29 dpyrpt, Gr. trans- literation diBuporr, ‘chief secretary’; M PrthPrs dbyr; NP dibir, dabir (but Paz. "diver, v. next w.). Cf Bailey, BSOS VII, 1933, 76-77.
dipīvarēh [dpywryh] 11311, dipiréh [dpy- ryh] 22%; the art of writing (documents)
dit
226; den ~ the writing down of the sacred texts 113%. — MPrs dbyryy, M Prth dbyryft; Paz. diver? (Mx). Bailey, ZP 177-194.
distak [dystk'] *treated, manipulated, or the like: pat Hēšm zahr ~ "treated with (the demon) Wrath's poison 2516-17 = 2814, — In the edition the first letter is a marked d, hence the reading dystk' is cogent. Because of -ist- this must be a SW form corresponding to a NW form with -i$t-, but its meaning in this context make it impossible to combine it with NW dištan (v. next w.): a weapon is not “built” or “‘formed’’. It would be tempt- ing to connect it with Skr dih- ‘to daub, to smear', but the corresponding Av. (673) dačz- has other significations (cf diz), and the Phl. renderings of it (Vd 39.13.18, 733. 1536) have run wild and are no more recognizable (they can scarcely be brought together with dés-, v. the next w.).
dištan to build, is the probable reading of the Prth ideogr. BNY- HajA:9. I1: pt. —pret. pass. 3d p. sg. BNY-t = dist, cond. BNY-t HWH-ndy = dist ahende. — MPrth dyštn, pres. certainly dys-, cf dysm'n ‘building’; MPrs dysydn dys- (A— H I), which is probably a denom. of des (q. v.) borrowed from NW; BP has desitan, pass. desihistan, désak ‘form’ (Bailey, ZP 94 n. 2), whereas the form dhytk' ‘built? DD 36? seems to represent the true SW form *dahitak < *déhitak (with -ēh -> -ah- cf s. v. uzdahikéh) from SW *daid-). Sogd óys- BBB p. 56 ult.
dit [TW B, inscr. TWB] 1. the second, the other: rēc i ~ 83; či 1 ~ the other 12118; &vak apāk ~ 104?* etc. ;évak 6 (61) ~ 1009-13 ete. — 2. adv., also ~-ic, for the second time, again 46*3 etc.; further, then 515; back P2:10; — 1116 v. dit. — Shortened from **ditī < *ditīya-, SW form of Olr *dvitiya- ‘second’, OP duvitiya-, Gath. Av. (963sg.) daibitya- for *dbitiya-; MPrs dwdy = dudi for *didi through in-
www .parsianjoman.org | ool ak,
dit
fluence of dē; Paz. did, didi-ca, dud; as against NW *bstīya-, Av. (l.c.) bitya-; MPrth byd; cf. s. v. bitaxs. V.also ditikar.
dit [HZYTN-t'; 1116 with wrong ideogr. TWB for dyt' misread as dit] sight: pat ~ visibly 1116; pat ~ ävurtan to make manifest, to give evidence of 4%. — NP padid; p. ävurdan = BP.
1ditan [dytn'; HZYTN-tn', inscr. and Ps. HZYTN-] vén-, 2nd p. sg. HZYTN-yd = vënë 7164. HZYTN-h = venah 31°; subju. lst p. sg. HZYTN-n = vēnān P2: 10: to see, to regard, to catch sight of, to contemplate, to discern, to experience: ayāftan u ~ u dänistan 88°; dänäkıhä ~ 51; pat venisn ~ 5013-1; pat (xves) cašm ~ 7479, 80%; — with ki that 115. 127 ete., with ka that 40%; — with a pt. as its complement: -m murtak dit han tahm spähpat I saw this valiant general slain 2719-11; 2 zan nisastak dit 6"; with an adj. P2:10. 2719. 5776 sq. (purr com- ` plement); — with an indir. interrog. clause: ~ kū . . . cigēn to see how 2518-19; ka-t dīt kū kas kē ... kart 137-9 a contam- ination between ka-t dit ku kas
kart and ka-t dit kē ... kart; — apar m to find out, to discover 39455; to survey 5817; to outwit (pat) 9917; — frde ~ to forebode 4722. 5074. 5112-16.18-19 _ Av. OP (724 sq.) *dāy- and (1323 sq.) vaéna-, vaina-; common. V. also venisn.
2ditan [dytn'] appearance, looks 141°. 1516.21, MPrth dydn ‘sight, phenomenon, aspect’, also spelt dydyn, dyd‘yn (MHC).
ditikar [dtykl] 1. ordinal number: the second: fratom ... <... sitikar etc. 8316-18; regularly placed before its subst., but at times also after: rēc i ~ 1197; säl Ci) ~ 97455; to be noticed : ~ yašt or yašt-ē 10015, 1031-26-27, — 2. pron.: čvak... ~ the one — the other 1815-16; apäk ~ with each other 4!. — 3. adv. secondly 825; for the second time, again 43%. — SW form of OIr. *dvitiya-kara-, v. dit; Paz. dadi- gar, NP digar through haplology. MPrs
dokan
has dwdyg, MPrth b(y)dyg (beside byd); cf dit.
divan [dyw'n'] the government office 11124. 11227-13, — NP divän, Arab. lw. diwän; Arm. lw. diwan already in the Bible. Possibly < *dipi-vahana- 'docu- ment house', v. dépivar.
```


## [2026-09-04T18:50:18.087Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\npython3 $S TLM.txt \"dida,  f\\.  stronghold\" 20 | head -3\necho \"=== SOD 24130-24150\"\nsed -n '24130,24150p' SOD_pages.txt\necho \"=== SOD leaf for prdyz\"\npython3 $S SOD_pages.txt \"py8ez \\(prdyz\\)\" 66 | head -3"
}
```


### [2026-09-04T18:50:19.861Z] TOOL RESULT

```
--- leaf 121 = printed p.101
   ...  sg.  m.  ditam,  Bh.  1.  13. avam  gaumatam  tyam  magum  xsa^’am  ditam  caxriya,  could  make  (7au - mata  the  Magian  deprived  of  the  kingdom.  YAv.  zi  (Middle Pers.  zinltan),  Skt.  ji. dida,  f.  stronghold .   Nom.  sg.  dida.  Acc.  sg.  didam.  New Pers.  diz;  cf.  YAv.  diz,  heap  up. dipi,  f.  inscription.  Acc.  sg.  dipim.  Loc.  sg.  d[i]p[iy]a,  Bh.  4. 8.  New  Pers.  dibir.  Cf.  Assyr.  duppu,  Elam,  tuppi;  Jensen,  ZA, 6, 172;  Foy,  ZDMG,  50,  128;  Pedersen,  KZ,  40, 190.  According to  Husing’s  interpretation  of  the  Elam.  (Bh.  L.)  Darius  declares that  he  made  inscri
=== SOD 24130-24150
                                                                   paryon ? ©Skt. updya ^pry'np^
7102 prSys- M                                a>^Lj<^U              means
     par8es ©<*pari-daisa- =^pr8}ys                               Vim. 112, 176, BSTBL, Benv. TSP n pl68
     (to)build
     BBB 494;
            -/ GMS 668, 914; AVS 125                         7114 pry'wncyk       B -=» prywncyk

7103 prSyz M                      (j*n>)u**J't{!             7115 pry'wt- B                         o^J'^^J'^j
     py8ez (prdyz) ©Av. pari-daeza ©ob. -y; pi.                   parxut ©pt. st. =»prywn-, prywt*k
                                                                  0o)reject, (rc)forbid
     gar       orc                                                TSP 2.1035, 1039; Hen. Texts. 722
         de        h
     BBB n,571 BSTard 877. 878.        C2, 87R 2, 8.11
              ;      ii   2,    8.16
                                     ;                       7116 pry*yz- B          o>^f j>** <J*J'£'J* < j^L-JV~*T
7104 prdyz C *=» pr8yz                                            parxez ©<* para-hazya- ? =^pryyz-
                                                                  (ro)deprive, 0<?)plunder
7105 prSyzp'n S                  (Okj^k)^i3Jl^tS^J
     par8ez-pan                                                   TSP 2.1114; Hen. Texts. 724; AVS 136
     chief of parks
                                                             7117 pry'z- B                      o±jW i&J'&ji
=== SOD leaf for prdyz
--- leaf 351 = printed p.285
   ...  GMS 668, 914; AVS 125                         7114 pry'wncyk       B -=» prywncyk  7103 prSyz M                      (j*n>)u**J't{!             7115 pry'wt- B                         o^J'^^J'^j      py8ez (prdyz) ©Av. pari-daeza ©ob. -y; pi.                   parxut ©pt. st. =»prywn-, prywt*k                                                                   0o)reject, (rc)forbid      gar       orc                                                TSP 2.1035, 1039; Hen. Texts. 722          de        h      BBB n,571 BSTard 877. 878.        C2, 87R 2, 8.11               ;      ii   2,    8.16
```


## [2026-09-04T18:50:26.923Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -on \"paradise[,;]\\? *n\\?\\.\\?[^\\n]\\{0,400\\}Pers[^\\n]\\{0,200\\}\" FSD_vol3.txt WEB_vol1.txt 2>/dev/null | head -4\necho \"--- FSD dough\"; grep -on \"dough[^\\n]\\{0,60\\}AS\\. dag[^\\n]\\{0,200\\}\" FSD_vol1.txt | head -3\necho \"--- WEB dough\"; grep -n \"dough, n\\|^dough \" WEB_vol1.txt | head -5"
}
```


### [2026-09-04T18:50:31.118Z] TOOL RESULT

```
--- FSD dough
ugrep: error: error at position 614
x8f][\x80-\xbf][\x80-\xbf]){0,200}
     exceeds complexity limits___/


--- WEB dough
16601:ato bake.] eae ase (of bread, etc.) produced at pane amount of material, as dough, needed 3. the quantity of anythi i operation ne not of anything made in one + a number of things or n pgicup; lot; oe gs or persons taken as a bate” pe ie; contention; debate. [Obs.] BNO pared bt., pp.; bating, ppr. [ME. strike] . batre, to beat; L. batuere, to beat,
104783:dough and shaped somewhat like a finger: lae-m6-dip’6-dan, a. and n. same as laemod- Lag-é-na/ri-a, n. [L. lagena, a bott
```


## [2026-09-04T18:50:34.816Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"par-a-dise\\|par'a-dise\\|paradeisos\\|Zend pairi\\|pairi-daeza\\|pairidaeza\" WEB_vol1.txt FSD_vol3.txt FSD_vol1.txt 2>/dev/null | head -8"
}
```


### [2026-09-04T18:50:34.901Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:50:38.191Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls FSD_vol*.txt WEB_vol1.txt | while read f; do echo \"== $f\"; grep -c \"paradise\" $f; done\ngrep -on \".\\{0,80\\}paradise.\\{0,250\\}\" FSD_vol3.txt | grep -i \"pers\\|zend\\|aves\\|greek\" | head -3"
}
```


### [2026-09-04T18:50:41.961Z] TOOL RESULT

```
== FSD_vol1.txt
15
== FSD_vol2.txt
13
== FSD_vol3.txt
8
== FSD_vol4.txt
8
== WEB_vol1.txt
12
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,250}
                         \___exceeds complexity limits
```


## [2026-09-04T18:50:54.898Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\npython3 $S IEC.txt \"^dheigh- .shape, earth up\" 15 | head -2\npython3 $S IEC.txt \"^dhoi.hos, om, is\" 15 | head -2\npython3 $S SYN.txt \"7\\.27 WALL\" 24 | head -2\npython3 $S SYN.txt \"5\\.53 DOUGH\" 24 | head -2\npython3 $S incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt \"dheigh- \\.\\.Lelim\" 0 | head -2\npython3 $S FVQ_pages.txt \"Firdaws\\)\" 17 | head -2"
}
```


### [2026-09-04T18:50:56.947Z] TOOL RESULT

```
--- leaf 521 = printed p.497
   ... pread Slavic group), Skt. ULORS ‘board, plank’, ON fjgl ‘thin board’, Grk. odédas ‘footstool, pedestal’, Skt. 7. Skt. bhami- ‘earth, ground’ (1.21) also used for ‘floor’. Other more spe. cific words? 7.27 WALL (Of a Town; Partition Wall) Grk. _—_retxos} rotxos, retxlov Goth. -waddjus Lith. miras; stena NG TotxXos ON mirr; veggr Lett. miiris; siena Lat. mitrus, moenia (pl.); Dan. mur; vag Chl. zidit, sléna paries Sw. mur; vdgg SCr. id, stijena It. muro; parele OE weall; wag Boh. zed’; sténa Fr. mur, muraille ME wall (waw) Pol. mur; Sciana Sp. muro; pared NE wall Russ. stena Rum. id; pdrete Du. muur; wan
--- leaf 404 = printed p.380
   ...  (also ‘meal’), pistaka-, fr. pis- ‘crush, pound’. Av. draonah- ‘portion, offering’, lat- SY,), : ia 77. Gamillscheg s.v. | er the sacred ‘cake’ : Skt. dravinas- ‘wealth, property’. Barth. 770. Crk ; 5.53 DOUGH ao. Goth. dai Shun, tondpr ON, daigs Lith. minklé, te3la * massa D deig Lett. mikla roe rag dej ChSI.  tésto is é 
--- leaf 0 = printed p.0
   ... „betupfen“ hierher (Fick 1 4 462  zw.), sondern als „streichelnd betasten, wie knetend beriihren ££ zu dheigh-  ,.fingere ££ . — Uber lit. dagys „Kette“ s. u. *dhag- „wetzen“ und *deg- „paeken ££ .   dheigh- ..Lelim kneten und damit mauern oder bestreicben (Mauer, Wall;  Topferei; dann auch vonanderweitigem Bilden, Formen, Gestalten;; auch  vom Teigkneten (Backerei) £ ; s. zum Sachlichen Meringer IF. 17, 147.   Ai. dchmi „bestreiche, verkitte" (3. sg. degdhi statt *dedhi, ebenso Ptc.  digdha-; s. auch Meillet IF. 18, 419 f.), deha m. n. .,Korper debt ..Wall,  Damm, Aufwurf £ , av. pairi-daezayeiti „mauert ri
--- leaf 240 = printed p.223
   ... UR'AN 223 whence the Gk. 'EtvaTrjs. From the Akk. come the Heb. IVIS and Syr. 2;2>, whence in all probability the Ar. Ol^, if indeed this was not an early borrowing from Mesopotamia. J x- . ^ ) }j-$ (Firdaws). xviii, 107 ; xxiii, 11. Paradise. The authorities are agreed that it means a garden jbL*j ( Jawhari, Sihdh, i, 467 ; LA, viii, 43), but they differed considerably as to what sort of a garden it means. 1 There are also divers opinions as to its precise location and significance as referring to the celestial Paradise. It was early recognized as foreign (Siddiqi, Stidien, 13, and note Fraenkel's re
```


## [2026-09-04T18:51:08.257Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,pg in enumerate(t):\n    if 'dheigh- ‘shape, earth up' in pg: print('dheigh leaf',i,'-> p ~',(i-15)*2)\n    if 'dhoiĝhos, om, is' in pg or 'dhoi' in pg and 'shape, mould; shaper' in pg: print('dhoighos leaf',i,'-> p ~',(i-15)*2)\nEOF"
}
```


### [2026-09-04T18:51:09.760Z] TOOL RESULT

```
dheigh leaf 112 -> p ~ 194
dhoighos leaf 121 -> p ~ 212
```


## [2026-09-04T18:51:19.820Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py\npython3 $S LEW_1910.txt \"pairidaéza- I 501\" 12 | head -2\necho \"=== HRN 563 diz\"; sed -n '5040,5075p' HRN.txt | head -40\ngrep -n \"^ *563\\. \" HRN.txt"
}
```


### [2026-09-04T18:51:21.589Z] TOOL RESULT

```
--- leaf 58 = printed p.46
   ... - II 294 paidyeiti II 295 pada- II 215 padtana- II 262 panta II 407 panta IT 336 par- II 344 para, para- II 285 parana- II 282 parasu- I 257 pard II 285 part IT 284 pariuntya I 49 pairika II 233, 252 pairidaéza- I 501, II 251 pairidaézayertt pairibrinants I 549 parrifrasa IT 346 pairyante IT 251 paurva- II 357 parsta- II 346, 349 parsti- II 349 pas- II 232 pasu- II 271 pasushaurvé II 525, 526 paskat II 348 pasta II 348 -pasti- II 296 pasne II 335 pazdayeiti I 2, 193 pazdu- Il 273 pasna- II 270 paman- II 234 para- IT 251 pasna- II 290 poratu- II 343 paradan IL 273 parada- ILI 251 paradu- II 316 parana- ,,Keder*
=== HRN 563 diz
32, 589 No. 26).
561. (lerj/ä *Meer; grosser Fluss', jüd.-pors. nxni (Is. 8,
23). '
ap. drayah'^) 'Meer*; aw. zrayah- 'Meer; plilv.
daryapj daryäk (Bund.), ^re; ai. jräyan-,
bei. zirih *Qnell\ zira *Meer (425).
LW. kurd. deryä; af/. daryäh; bei. darya (50);
yidg. däriyow Tluss*.
Die Form deryäb verdankt nur einer Anlehnung an
ah * Wasser ihre Entstehung. Phlv. zful ist entweder
dialektisch oder nur als ursprüngliche und dann weiter
gedrungene Umschreibung von aw. zrayah- anzu-
sehen; np. zeräh ist sicher Dialektforni.
5H2. derriden, deriden 'zerreissen*.
aw. {/'daV'^ dereta- 'spalten'; phlv. darltan bozw.
darritan ; ai. V^dar-^ ddrsi {dpuiti).
kurd. deriyän; af>'. dural; bei. dirag, dirray, n. diray,
dinay (78); sar. z-dard-änam (Caus.).
563. dix, diz, dez-) 'Burg, vergl. dizhäii-^), dlzdär (syr. LW.
n^nn).
ap. didä' Testung', vergl. ncwciduooi^' (No. 279);
aw. daf^za-; phlv. d(i)z (AV. ; Bund.); arm. vergl. dcz
•Jlaufe' (Hübschmann No. 82).
Die neupersischon Formen diz und dcz sind beide
gleich ursprünglich. Ap. dida- steht für dlöä- und
zwar entspricht das ap. d hier einem ar. fA ; in diesem
Falle wird es im Nenpersischen nicht zu y, Ascoli's
Erklärung von np. dwar 'Mauer aus ap. '^didavara-
\Stadtwair ist daher nicht wahrscheinlich, zumal die
ältere Form devar gewesen zu sein scheint, vergl.
No. 599.
») Bartholomae, ZDMa. 46, 29S No. XV.
2) Dez findet sich in einer ganzen Reilie trän soxanisch er
Ortsnamen, die Herr Prof. Nöldeke gesammelt liat und demnächst
anderswo mitteilen wird.
^) Ma\i^rr nl-Umerä.— 126 -
5058:563. dix, diz, dez-) 'Burg, vergl. dizhäii-^), dlzdär (syr. LW.
```


## [2026-09-04T18:51:38.316Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('data/verification/page-126.json'))\ne=d['entries'][0]\nprint('entry keys',list(e.keys()))\nfor n in e['nodes']:\n    print('---',n['id'],list(n.keys()))\n    print('  sources:',n.get('sources'))\n\""
}
```


### [2026-09-04T18:51:40.268Z] TOOL RESULT

```
entry keys ['entry', 'root', 'verdict', 'modern_form', 'note', 'sources', 'ref_check', 'nodes']
--- 1 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://www.livius.org/sources/content/achaemenid-royal-inscriptions/dsf/', 'https://www.avesta.org/op/op.htm', 'https://en.wiktionary.org/wiki/دیوار', 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰóyǵʰos', 'https://www.academia.edu/35394163/_SWIran_didā_fortress_walled_residence_in_Iranian_Toponymy_by_Garnik_Asatrain']
--- 2 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/دیوار', 'https://en.wiktionary.org/wiki/dywʾl']
--- 3 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-', 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰóyǵʰos']
--- 4 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/𐬛𐬀𐬉𐬰𐬀', 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰóyǵʰos']
--- 5 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/دژ', 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-', 'https://en.wikipedia.org/wiki/Dezful']
--- 6 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/𐬞𐬀𐬌𐬭𐬌⸱𐬛𐬀𐬉𐬰𐬀', 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/paridayjah', 'https://en.wiktionary.org/wiki/𐎱𐎼𐎭𐎹𐎭𐎠𐎶', 'https://www.iranicaonline.org/articles/garden-i/']
--- 7 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/پالیز', 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/paridayjah', 'https://en.wiktionary.org/wiki/جالیز', 'https://vajehyab.com/?q=پالیز&d=moein']
--- 8 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/پردیس', 'https://en.wiktionary.org/wiki/فردوس', 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/paridayjah', 'https://en.wiktionary.org/wiki/παράδεισος']
--- 9 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/παράδεισος', 'https://www.etymonline.com/word/paradise', 'https://www.iranicaonline.org/articles/garden-i/', 'https://www.balashon.com/2007/12/pardes-and-paradise.html', 'https://ahdictionary.com/word/search.html?q=paradise']
--- 10 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://www.etymonline.com/word/paradise', 'https://en.wiktionary.org/wiki/παράδεισος', 'https://ahdictionary.com/word/search.html?q=paradise']
--- 11 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/دیگ', 'https://archive.org/details/persischestudie00hbgoog']
--- 12 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/دیگ', 'https://en.wiktionary.org/wiki/دیزی']
--- 13 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/daigaz', 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/daigijǭ', 'https://www.thefreedictionary.com/_/roots.aspx?type=Indo-European&root=dheigh-']
--- 14 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://www.etymonline.com/word/dough', 'https://www.etymonline.com/word/lady', 'https://www.etymonline.com/word/dairy', 'https://en.wiktionary.org/wiki/dough']
--- 15 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://en.wiktionary.org/wiki/figura#Latin', 'https://en.wiktionary.org/wiki/fingo#Latin', 'https://www.etymonline.com/word/figure']
--- 16 ['id', 'lang', 'words', 'verdict', 'derivation', 'sources', 'ref_check']
  sources: ['https://www.etymonline.com/word/figure', 'https://www.etymonline.com/word/fiction', 'https://www.etymonline.com/word/*dheigh-']
```


## [2026-09-04T18:51:44.191Z] TOOL CALL #96: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-04T18:51:44.264Z] TOOL RESULT

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


## [2026-09-04T18:51:46.433Z] AGENT

Now let me save the vision text for the ARY page and write the update.


## [2026-09-04T18:52:03.536Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/ARY\ncat > data/verification/sources/refs/ocr/ARY/0297.vision.txt <<'EOF'\n[read from the page image by claude-fable-5-1, 2026-09-04; ARY printed p. 297 = pdf page 296]\n\n(running head) دیوار / ۲۹۷\n\n-- tail of the preceding entry دیو (DEV) --\nREFERENCES / پسگشت‌ها: POKORNY: 185-186 | DELAMARRE: (DIEU) 72 |\nMACKENZIE: (DEMON) 110 | BUCK: 1464-1465 | SKEAT: (DEIW) 753 |\nRAMAT: 50 | AMINDAROV: (DEMON) 210 | برهان قاطع: ۹۱۷\nیادداشت:\n۱- چم این واژه در همه‌ی زبان‌های این فهرست: خدا.\n۲- علت دگرگونی چم این واژه در زبان‌های ایرانی این است که پس از ظهور زرتشت و آئین او\n\"آهورامزدا\" مورد پرستش قرار گرفت و واژه‌ی \"دیو\" چم کنونی خود را به دست آورد.\n\n-- the entry دیوار --\nفارسی (PERSIAN): دیوار  —  DIVĀR\nچم انگلیسی سرواژه‌ی فارسی: WALL\nهند و اروپایی (INDO-EUROPEAN): *DHEIGH-, *DHEIGHOS-, *DHEIGMI-\n\nاوستایی (AVESTAN): DAĒZAYEITI\nپارسی باستان (OLD PERSIAN): DIDA\nپهلوی (PAHLAVI): DĒWĀR\nکردی (KURDISH): DIWAR\nافغانی (پشتو) (AFGHANI): DEWĀL\nتخاری A (TOKHARIAN A): TSEK-\nتخاری B (TOKHARIAN B): TSAIK-\nسانسکریت (SANSKRIT): DĒHMI, DEHI-\nارمنی (ARMENIAN): DIZANEM\nیونانی (GREEK): TEĪKHOS, TEĪCHOS, TOĪCHOS\nلاتین (LATIN): FINGŌ, FINGERE\nگوتیک (GOTHIC): DIGAND\nاسلاوی کهن (OLD CHURCH SLAVIC): ZĪDŪ\nچکی (CZECH): ZED | صربی (SERBIAN): ZID | بوهمی (BOHEMIAN): ZED\nلیتوانی (LITHUANIAN): ZHIEDZHIU\nپروسی کهن (OLD PRUSSIAN): SEYDIS\nایرلندی کهن (OLD IRISH): COMOD-DING\n\nREFERENCES / پسگشت‌ها: POKORNY: 244-245 | DELAMARRE: (FAÇONNER LA TERRE) 253 |\nMACKENZIE: (WALL) 139 | BUCK: 472-473 | AMINDAROV: (WALL) 307\nیادداشت:\n۱- بازگشت به: دژ\nEOF\necho saved"
}
```


### [2026-09-04T18:52:03.625Z] TOOL RESULT

```
saved
```


## [2026-09-04T18:56:00.203Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ncat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/upd.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io, collections\n\nP = 'data/verification/page-126.json'\nd = json.load(open(P, encoding='utf-8'))\ne = d['entries'][0]\nnodes = {n['id']: n for n in e['nodes']}\n\n# ---------- quotes reused across nodes ----------\nWLD = (\"WLD_Bd1_1930_dli_70244_djvu.txt, Bd. I pp. 833-834 s.v. dheigh-: \"\n       \"'dheigh- \\\"Lehm kneten und damit mauern oder bestreichen (Mauer, Wall; Töpferei; dann auch von \"\n       \"anderweitigem Bilden, Formen, Gestalten); auch vom Teigkneten (Bäckerei)\\\" ... \"\n       \"ai. dehmi \\\"bestreiche, verkitte\\\" ... dehi \\\"Wall, Damm, Aufwurf\\\", av. pairi-daezayeiti \\\"mauert ringsum\\\", \"\n       \"uzdaeza- m. \\\"Aufhäufung, Wall\\\", pairidaeza- m. \\\"Umfriedigung\\\" (daraus gr. paradeisos), ap. dida \\\"Festung\\\", \"\n       \"npers. diz, dez ds. ... gr. teichos, toichos \\\"Mauer, Wand\\\" ... lat. fingo ... figura \\\"Bildung, Gestalt, Figur\\\", \"\n       \"fictio ... got. daigs \\\"Teig\\\", anord. deig, ags. dag, ahd. teig ds.'\")\nAHDROOT = (\"AHD_watkins1985.txt s.v. dheigh-: 'To form, build. 1. Germanic *daigjon in Old English dæge, bread kneader: DAIRY. \"\n           \"2. Germanic *-dig- in Old English compound hlæfdige ...: LADY. 3. Extended o-grade form *dhoigho- in Germanic *daigaz ... DOUGH ... \"\n           \"4. Suffixed zero-grade form *dhigh-ura, in Latin figura ... FIGURE ... 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere ... FICTION ... \"\n           \"7. Suffixed o-grade form *dhoigh-o- in Avestan daeza-, wall ...: PARADISE. [Pok. dheigh- 244.]'\")\nLATFINGO = (\"LAT.txt leaf 437-438 (Ernout-Meillet pp. 419-420) s.v. fingo: 'La racine i.-e. dheig'h- ... \"\n            \"figura (forme avec le suffixe -ura directement sur la racine, et non derive du supin ...) ... \"\n            \"La gutturale finale etait une prepalatale: l'Avesta a -daezayeiti \\\"il entasse\\\", pairi-daeza \\\"enclos\\\" \"\n            \"(le mot que les Grecs ont hellenise en παραδεισος), et le vieux perse dida \\\"mur, enceinte\\\". ... \"\n            \"arm. dizanim ... got. daigs signifie \\\"argile\\\". Le sens propre de la racine est \\\"façonner (de la terre)\\\".'\")\nKLNDOUGH = (\"KLN_1966.txt leaf 261 (printed p. 477) s.v. dough: 'rel. to ON. deig ... Goth. daigs, \\\"dough\\\", digan, \\\"to knead\\\", \"\n            \"fr. I.-E. base *dheigh-, *dhoigh-, *dhigh-, \\\"to form out of clay, to knead, form\\\", whence also OI. dehmi ... dehi, \"\n            \"\\\"rampart, dam, dike\\\", Avestic daeza, \\\"wall\\\", pairi-daeza, \\\"enclosure\\\" (whence Gk. παραδεισος, \\\"enclosed park\\\"), \"\n            \"OPers. dida, \\\"castle\\\" ... Gk. teichos, toichos ... L. fingere ... figura ... Oscan feihuss ...'\")\nKLNPARA = (\"KLN_1966.txt leaf 600 (printed p. 1124-1125) s.v. paradise: 'ME. paradis, fr. OF. paradis, fr. Late L. paradisus, \"\n           \"fr. Gk. παραδεισος, \\\"park, the garden of Eden, paradise\\\", a word of Old Persian origin; cp. Avestic pairidaeza, \"\n           \"\\\"an enclosure\\\", whence Heb. pardes, \\\"park, garden\\\" (whence Aram. pardes, pardesa ...). Avestic pairidaeza is \"\n           \"compounded of pairi, \\\"around\\\", and daeza, \\\"wall\\\".'\")\nBRTDAEZA = (\"BRT.txt col. 674-675: 'daez- V. \\\"häufen, schichten\\\" (Erde, Steine) ... mit pairi \\\"rings-, rundum aufdämmen, mauern\\\" ... \"\n            \"Ar. *dhaigh- (vgl. gr. teichos); ai. digdhi'; and 'daeza- m. \\\"Häufen, Schichten\\\" von Erde, Steinen. — Zum V. daez-. — \"\n            \"np. dez \\\"Burg\\\", gr. teichos \\\"Mauer\\\", osk. feihuss (AP.) \\\"Wall\\\"; ai. deha- m. \\\"Körper\\\".'\")\nBRTPAIRI = (\"BRT.txt col. 866: 'j. pairi.daeza- m., Plur. \\\"eine rings-, rundum gehende, sich zusammenschliessende Umwallung, \"\n            \"Ummauerung\\\": V. 3.18. — np. paliz \\\"Garten\\\" [vgl. gr. LW. παραδεισος].'\")\nBRTDIDA = (\"BRT.txt col. 747: 'p. dida- f. \\\"befestigter Ort, Festung; Burg\\\" ... Bh. 2.8 ... — Zum V. daez-: np. dez; ai. vgl. dehi- f. \\\"Wall\\\".'\")\nFVQ = (\"FVQ_pages.txt leaves 240-241 (Jeffery pp. 223-224) s.v. firdaus: 'Obviously firdaus represents the Gk. παραδεισος ... \"\n       \"The original word is Iranian, the Av. pairidaeza, which in the plu. means a \\\"circular enclosure\\\". Xenophon introduced \"\n       \"the word into Greek ... in the LXX is sometimes used to translate gan ... In late Akk. we find pardisu, and in Heb. pardes ... \"\n       \"Syr. pardaysa ... Its origin is almost certainly Christian, and probably Syriac ... It was a pre-Islamic borrowing.' \"\n       \"Footnote: 'Bartholomae, AiW 865 ... It survives in Mod. Pers. paliz garden (Horn, Grundriss, 279).'\")\nPLA = (\"incoming/PLA/PLA_pages.txt leaf 221 (Asbaghi p. 207) s.v. firdus: 'firdus: \\\"Paradies\\\" aw. pairidaeza ... mp. paliz, \"\n       \"ap. pairidaida ... Es besteht aus dem Präfix pairi \\\"um\\\" + daeza ... syr. pardaysa, mand. pardisa, bab. pardisu, hebr. pardes, \"\n       \"aw. pairidaeza >> griech. paradeisos, frz. paradis, engl. paradise, dtsch. Paradies.' (refs Bartholomae AiW 865, Horn Grundriss 279, Jeffery)\")\nARYPAL = (\"incoming/ARY/ARY_pages.txt pdf pp. 153-154 (printed pp. 154-155), entry پالیز، فالیز، جالیز، پردیس (به چم «باغ، بوستان»): \"\n          \"اوستایی PAIRIDAEZA؛ یونانی PARADEISOS؛ لاتین PARADISUS؛ فرانسه PARADIS؛ انگلیسی PARADISE. \"\n          \"یادداشت ۱: «فردوس» نیز معرب «پردیس» است. یادداشت ۲: «واژه‌ی اوستایی از دو جزء درست شده است: PAIRI (به چم «دور» و «پیرامون») \"\n          \"و DAEZA (به چم «دیوار») (بازگشت به: دیوار)». یادداشت ۳: «چم این واژه در همه‌ی زبان‌های غیر ایرانی این فهرست «بهشت»، «فردوس» است \"\n          \"و ضمناً همه از زبان فارسی گرفته شده‌اند.»\")\n\ndef add(nid, items):\n    nodes[nid]['consulted'] = items\n\n# ---------------- ROOT ----------------\ne['consulted'] = [\n  {\"src\": \"WLD\", \"where\": \"Bd. I pp. 833-834 s.v. dheigh-\", \"stance\": \"supports\",\n   \"note\": WLD + \" — Walde-Pokorny's gloss is verbatim Nourai's 'to knead clay ... or dough', and the article contains every branch of his chart except the 'daika > dig' one.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix s.v. dheigh-\", \"stance\": \"supports\",\n   \"note\": AHDROOT + \" Watkins' headword form and Pokorny reference (244) are exactly Nourai's root box.\"},\n  {\"src\": \"IEC\", \"where\": \"leaf 112 (Mann cols ~193-194) s.v. dheigh-, and leaf 121 (cols ~211-212) s.v. dhoiĝhos\", \"stance\": \"supports\",\n   \"note\": \"IEC.txt: 'dheigh- \\\"shape, earth up; form, wall\\\". WP I, 833. Cf. dhoigh- Skt. dehah ...; Av. (pairi-)daezo \\\"surrounding fence\\\" ...; Gk. teikhos ...; Osc. feihuss ...; Go. digan ...'; and 'dhoiĝhos, om, is, ia \\\"shape, mould; shaper\\\" ... Av. -daeza, in pairi- \\\"rampart\\\"; LW in Arm. dez ... and partez \\\"paradise\\\"; Tokh. A tseke ...; Gk. toikhos; Gothic daigs, OHG teic, OE dag \\\"dough\\\".' Mann's two lemmas together cover Nourai's whole root box.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 7.27 WALL (pp. 472-473) and 5.53 DOUGH (pp. 359-360)\", \"stance\": \"supports\",\n   \"note\": \"SYN.txt 7.27: 'Grk. teichos, toichos : Osc. acc. pl. feihuss \\\"walls\\\", Skt. (Ved.) dehi- \\\"wall, mound\\\", OPers. dida- \\\"fortress\\\", Av. uzdaezi- \\\"wall\\\", Toch. A tseke ..., fr. IE *dheigh- in Skt. dih- \\\"smear\\\", Lat. fingere \\\"mold\\\", etc. ... Walde-P. 1.833 ff.'; 5.53: 'Goth. daigs, OE dag, etc., gen. Gmc. : Goth. digan \\\"mold, form\\\", Lat. fingere \\\"mold\\\", Skt. dih- \\\"smear\\\" (\\\"fashion, form\\\" implied by dehi- \\\"wall\\\" like Grk. teichos \\\"wall\\\"), IE *dheigh-.' Buck confirms both halves of Nourai's gloss (wall-building and dough-kneading) under one root.\"},\n]\n\n# ---------------- node 1 : OP dida / *daigha-vara ----------------\nadd(1, [\n  {\"src\": \"BRT\", \"where\": \"col. 747 s.v. didā-\", \"stance\": \"supports\",\n   \"note\": BRTDIDA + \" Bartholomae has Nourai's OP didā- under the verb daēz-, but has no *daigha-vāra-.\"},\n  {\"src\": \"TLM\", \"where\": \"leaf 121 (Tolman, Ancient Persian Lexicon p. 101)\", \"stance\": \"supports\",\n   \"note\": \"TLM.txt: 'dida, f. stronghold. Nom. sg. dida. Acc. sg. didam. New Pers. diz; cf. YAv. diz, heap up.' Tolman's lexicon confirms the OP word, its inflection and the NP outcome; no compound with -vāra-.\"},\n  {\"src\": \"NYB\", \"where\": \"Part II Glossary p. 67 s.v. divar\", \"stance\": \"partial\",\n   \"note\": \"NYB_vol2_glossary.txt leaf 75: 'divar [dywʾl] a wall 39*. — NP divar. V. Hübschmann, PSt 65, no. 599, whose etymology is quite satisfactory: *dida-vāra-, v. the next w.' Nyberg endorses *didā-vāra- ('fortress-wall'), NOT Nourai's *daigha-vāra- (Horn's *deghavāra-); the two reconstructions differ in the first member.\"},\n  {\"src\": \"LAT\", \"where\": \"leaf 437-438 (Ernout-Meillet pp. 419-420) s.v. fingo\", \"stance\": \"supports\",\n   \"note\": \"Ernout-Meillet cite 'le vieux perse didā \\\"mur, enceinte\\\"' as a direct nominal derivative of *dheiǵh- — the same OP form Nourai draws from the root.\"},\n  {\"src\": \"ARY\", \"where\": \"p. 297 s.v. دیوار\", \"stance\": \"partial\",\n   \"note\": \"ARY_pages.txt pdf p.296 (printed 297; also read from the page image, saved as ocr/ARY/0297.vision.txt): 'دیوار DIVĀR / WALL; INDO-EUROPEAN *DHEIGH-, *DHEIGHOS-, *DHEIGMI-; AVESTAN DAĒZAYEITI; OLD PERSIAN DIDA; PAHLAVI DĒWĀR; KURDISH DIWAR; AFGHANI DEWĀL ... LATIN FINGŌ, FINGERE' (refs Pokorny 244-245, MacKenzie (WALL) 139, Buck 472-473). Aryanpur puts dīvār under this root and gives OP didā-, but no *daigha-vāra- compound.\"},\n])\n\n# ---------------- node 2 : NP divar ----------------\nadd(2, [\n  {\"src\": \"PHD\", \"where\": \"leaf 49 (MacKenzie p. 28) s.v. dēwār\", \"stance\": \"supports\",\n   \"note\": \"PHD.txt: 'dēwār [dywʾl | M dywʾr, N ~] wall.' MacKenzie has the Middle Persian ancestor dēwār (Manichaean MP dywʾr) giving NP dīwār unchanged — the intermediate step Nourai's arrow needs.\"},\n  {\"src\": \"NYB\", \"where\": \"Part II Glossary p. 67 s.v. divar\", \"stance\": \"supports\",\n   \"note\": \"NYB_vol2_glossary.txt leaf 75: 'divar [dywʾl] a wall 39*. — NP divar. V. Hübschmann, PSt 65, no. 599, whose etymology is quite satisfactory: *dida-vāra-.' Nyberg attests the Pahlavi word and accepts an Old Iranian compound whose first element is didā-.\"},\n  {\"src\": \"ARY\", \"where\": \"p. 297 s.v. دیوار\", \"stance\": \"supports\",\n   \"note\": \"ARY_pages.txt pdf p.296 / ocr/ARY/0297.vision.txt: 'دیوار DIVĀR = WALL; INDO-EUROPEAN *DHEIGH-...; OLD PERSIAN DIDA; PAHLAVI DĒWĀR; KURDISH DIWAR; AFGHANI DEWĀL', cross-referenced 'بازگشت به: دژ'. Aryanpur derives NP dīvār from this root, exactly as the chart does.\"},\n  {\"src\": \"MON\", \"where\": \"vajehyab.com, Farhang-e Mo'in s.v. دیوار\", \"stance\": \"partial\",\n   \"note\": \"'دیوار [ په . ] (اِ.) ۱- جداری از سنگ، چوب، آجر و غیره که اطراف خانه، زمین و باغ و غیره به جهت محصور کردن و حفاظت آن بنا می‌کنند.' Mo'in tags the word Pahlavi ([په.]) and gives Nourai's gloss 'wall', but the online text carries no Old Persian antecedent. Archived https://vajehyab.com/?q=دیوار&d=moein\"},\n])\n\n# ---------------- node 3 : Sogdian dyz' ----------------\nadd(3, [\n  {\"src\": \"SOD\", \"where\": \"p. 285, entries 7102-7105 (parδēs / parδēz)\", \"stance\": \"supports\",\n   \"note\": \"SOD_pages.txt leaf 351: '7102 prδys- M parδes < *pari-daisa- (to)build'; '7103 prδyz M parδez (prdyz) © Av. pari-daeza ... garden, orchard'; '7105 prδyzpʾn S parδez-pān chief of parks'. Besides Nourai's δyzʾ 'fort' (entry 3825, < OP didā) Gharib has a whole Sogdian family from Av. pairi-daēza-, which independently confirms the root and the 'walled garden' semantics.\"},\n  {\"src\": \"NYB\", \"where\": \"Part II Glossary s.v. dištan (p. ~68)\", \"stance\": \"supports\",\n   \"note\": \"NYB_vol2_glossary.txt: 'dištan to build ... MPrth dyštn, pres. certainly dys- ... Sogd δys- BBB p. 56 ult.' Nyberg confirms the Sogdian reflex of the verb daēz- 'build (of clay)', the base of Gharib's δyzʾ 'fort'.\"},\n])\n\n# ---------------- node 4 : Av. daeza ----------------\nadd(4, [\n  {\"src\": \"BRT\", \"where\": \"coll. 674-675 s.v. daēz-, daēza-\", \"stance\": \"supports\",\n   \"note\": BRTDAEZA + \" Bartholomae's daēza- is a verbal noun 'heaping, layering (of earth, stones)'; the sense 'wall' that Nourai prints is Bartholomae's own gloss for the derivatives uz-daēza- (col. 411-412 'Wall, Damm, Mauer') and pairi.daēza-.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I pp. 833-834 s.v. dheigh-\", \"stance\": \"supports\",\n   \"note\": WLD},\n  {\"src\": \"IEC\", \"where\": \"leaf 121 (Mann cols ~211-212) s.v. dhoiĝhos\", \"stance\": \"supports\",\n   \"note\": \"IEC.txt: 'dhoiĝhos ... \\\"shape, mould; shaper\\\". Cf. dheiĝh-. WP I, 833 Skt. dehah ...; dehi \\\"rampart\\\"; Av. -daeza, in pairi- \\\"rampart\\\"; LW in Arm. dez ... and partez \\\"paradise\\\"; Tokh. A tseke ...; Gk. toikhos \\\"house-wall\\\"; Gothic daigs, OHG teic, OE dag \\\"dough\\\".' Mann derives Av. daēza- from the o-grade noun, the same step Nourai's arrow makes.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 7.27 WALL (p. 472)\", \"stance\": \"supports\",\n   \"note\": \"SYN.txt: 'Av. uzdaézi- \\\"wall\\\" ... fr. IE *dheigh- in Skt. dih- \\\"smear\\\", Lat. fingere \\\"mold\\\", etc. ... Walde-P. 1.833 ff.' — Buck lists the Avestan word among the IE words for 'wall' under this root.\"},\n])\n\n# ---------------- node 5 : NP dez / Dezful ----------------\nadd(5, [\n  {\"src\": \"HRN\", \"where\": \"no. 563, p. 125\", \"stance\": \"supports\",\n   \"note\": \"HRN.txt leaf 146: '563. diz, dez \\\"Burg\\\", vergl. dizbān, dizdār (syr. LW.). ap. didā \\\"Festung\\\", vergl. παραδεισος (No. 279); aw. daēza-; phlv. d(i)z (AV.; Bund.); arm. vergl. dez \\\"Haufe\\\". Die neupersischen Formen diz und dez sind beide gleich ursprünglich.' Horn confirms both vocalisations and the Avestan/Old Persian antecedents.\"},\n  {\"src\": \"PHD\", \"where\": \"leaf 49 (MacKenzie p. 28) s.v. diz\", \"stance\": \"supports\",\n   \"note\": \"PHD.txt: 'diz [KLYTA < A qrytʾ; dc | M dyz, N ~] fortress.' The Middle Persian link diz > NP diz/dež that Nourai's arrow presupposes.\"},\n  {\"src\": \"NYB\", \"where\": \"Part II Glossary p. 67 s.v. diz\", \"stance\": \"partial\",\n   \"note\": \"NYB_vol2_glossary.txt leaf 75: 'diz [dcʾ] castle ... MPrthPrs dyz; NP diz. — NW form, as against OP didā-. From Av. (673 sq.) daēz-.' Nyberg agrees with the Avestan source but stresses that NP diz/dež is the North-West (Parthian) reflex, not a lineal Persian continuation of OP didā-; that is a nuance Nourai's chart does not draw.\"},\n  {\"src\": \"ARY\", \"where\": \"p. 278 s.v. دژ\", \"stance\": \"supports\",\n   \"note\": \"ARY_pages.txt pdf p.277 (printed 278): entry دژ with AVESTAN UZDAEZA, -DAEZA; OLD PERSIAN DIDA; PAHLAVI DIZ; GREEK TEICHOS/TOICHOS; LATIN FINGO; GOTHIC DAIGS ...; note '۱- بازگشت به: دیوار' and '۲- چم این واژه در زبان‌های ایرانی باستان و یونانی: دیوار؛ ... در زبان‌های اسلاوی و ژرمنی: گِل، خمیر'. Aryanpur groups dež exactly as Nourai does.\"},\n  {\"src\": \"MON\", \"where\": \"vajehyab.com, Farhang-e Mo'in s.v. دژ\", \"stance\": \"partial\",\n   \"note\": \"'دژ (دِ) = (اِ.) دز: حصار، قلعه.' The meaning 'fort, citadel' is confirmed and دژ is equated with دز, but the online Mo'in gives no etymology and nothing on دژپل/دزفول. Archived https://vajehyab.com/?q=دژ&d=moein\"},\n])\n\n# ---------------- node 6 : Av. pairi-daeza ----------------\nadd(6, [\n  {\"src\": \"BRT\", \"where\": \"col. 866 s.v. pairi.daēza-\", \"stance\": \"supports\",\n   \"note\": BRTPAIRI + \" This is the standard reference (Jeffery and Asbaghi both cite 'Bartholomae AiW 865/866' for it).\"},\n  {\"src\": \"KLN\", \"where\": \"leaf 600 (printed pp. 1124-1125) s.v. paradise\", \"stance\": \"supports\",\n   \"note\": KLNPARA},\n  {\"src\": \"HUB\", \"where\": \"p. 123 (§ on loss of i/u in composition)\", \"stance\": \"supports\",\n   \"note\": \"HUB.txt leaf 133: 'pālīz \\\"Garten\\\" = hebr. pardēs (Hohelied), arm. partēz, zd. pairidaeza-, gr. παραδεισος'; and p. 260 §157: 'das ältere (arsacidische) Pehlevi hatte noch rd, wie arm. partēz (für *pardēz) ... bezeugen.' Hübschmann reconstructs the intermediate MP *pardēz that Nourai's chart skips.\"},\n  {\"src\": \"LAT\", \"where\": \"leaf 437-438 (Ernout-Meillet pp. 419-420) s.v. fingo\", \"stance\": \"supports\",\n   \"note\": LATFINGO},\n])\n\n# ---------------- node 7 : palîz / jâlîz ----------------\nadd(7, [\n  {\"src\": \"HRN\", \"where\": \"no. 279, p. 63\", \"stance\": \"supports\",\n   \"note\": \"HRN.txt leaf 84: '279. pālēz \\\"Garten\\\" (Šāhn. I, 73 Vers 207), pālēzbān, arab. LW. fālīz. ap. παραδεισος; aw. pairidaēza-. LW. kurd. pārēz, arm. partēz, syr. prdysʾ.' Footnote: 'Pālēz soll nach den persischen Original-Wörterbüchern mehr \\\"Fruchtgarten\\\" bedeuten.' Horn derives pālīz straight from Av. pairi-daēza-, exactly Nourai's arrow, and records the Arabic loan fālīz that lies behind the jālīz variant.\"},\n  {\"src\": \"HUB\", \"where\": \"p. 123, and p. 124 / §157 p. 260\", \"stance\": \"supports\",\n   \"note\": \"HUB.txt leaf 133: 'pālīz \\\"Garten\\\" = hebr. pardēs, arm. partēz, zd. pairidaeza-, gr. παραδεισος'; leaf 134: 'ap. pari- zu par-, vgl. pālēz aus *pardēz, s. p. 123'; §157: Arsacid Pahlavi still had -rd-, whence *pardēz > pālēz by the Sasanian change rd > l. Hübschmann supplies the sound change (pairi-daiza- > *pardēz > pālēz) Nourai's arrow leaves implicit.\"},\n  {\"src\": \"BRT\", \"where\": \"col. 866 s.v. pairi.daēza-\", \"stance\": \"supports\",\n   \"note\": \"BRT.txt: after the Avestan entry Bartholomae writes 'np. pāliz \\\"Garten\\\" [vgl. gr. LW. παραδεισος]' — the New Persian outcome is given in the Avestan dictionary itself.\"},\n  {\"src\": \"PLA\", \"where\": \"Asbaghi p. 207 s.v. firdus\", \"stance\": \"supports\",\n   \"note\": \"incoming/PLA/PLA_pages.txt leaf 221: 'aw. pairidaeza ... mp. pāliz' — Asbaghi treats pālīz as the Middle-Persian reflex of pairi-daēza-.\"},\n  {\"src\": \"ARY\", \"where\": \"pp. 154-155 s.v. پالیز، فالیز، جالیز، پردیس\", \"stance\": \"supports\",\n   \"note\": ARYPAL},\n])\n\n# ---------------- node 8 : pardis / ferdows ----------------\nadd(8, [\n  {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 223-224 s.v. firdaus\", \"stance\": \"partial\",\n   \"note\": FVQ + \" Jeffery agrees on the ultimate Avestan source but routes Arabic firdaws through Syriac pardaysā (Christian Aramaic), not directly from Avestan or Greek — so New Persian ferdows is a loan back from Arabic, which Nourai's single arrow Av. pairi-daēza- > NP pardīs/ferdows compresses.\"},\n  {\"src\": \"PLA\", \"where\": \"Asbaghi p. 207 s.v. firdus\", \"stance\": \"supports\",\n   \"note\": PLA + \" Asbaghi lists firdaws among the Persian loanwords in Arabic — i.e. the Persian > Arabic > Persian round trip for ferdows.\"},\n  {\"src\": \"ARY\", \"where\": \"pp. 154-155, footnote 1\", \"stance\": \"supports\",\n   \"note\": ARYPAL + \" Footnote 1 ('«فردوس» نیز معرب «پردیس» است') states outright that ferdows is the Arabicised form of pardīs.\"},\n  {\"src\": \"KLN\", \"where\": \"leaf 600 (printed pp. 1124-1125) s.v. paradise\", \"stance\": \"supports\",\n   \"note\": KLNPARA + \" Klein supplies the Semitic side (Heb. pardēs, Aram. pardēsā) through which Arabic firdaws and hence NP ferdows came.\"},\n  {\"src\": \"MON\", \"where\": \"vajehyab.com, Farhang-e Mo'in s.v. پردیس / فردوس\", \"stance\": \"partial\",\n   \"note\": \"'پردیس (پَ) (اِ.) فردوس، بستان.'; 'فردوس (فِ دُ) ۱- باغ، بوستان. ۲- بهشت.' Mo'in equates the two words and gives Nourai's gloss 'heaven/garden', but the online text carries no etymological tag. Archived https://vajehyab.com/?q=پردیس&d=moein and https://vajehyab.com/?q=فردوس&d=moein\"},\n  {\"src\": \"IRN\", \"where\": \"Farahvashi, Iranvij pp. 90-91 and 94\", \"stance\": \"supports\",\n   \"note\": \"incoming/IRN/IRN_pages.txt (pdf pp. 101-105): 'پادشاهان هخامنشی ... در پیرامون کاخهای خود باغهای بزرگ پردرخت ایجاد می‌کردند که بدانها پردیس می‌گفتند ... و همین باغهای پردرخت و زیبای دوران هخامنشی است که مفهوم Paradise به معنی بهشت را در یونان کهن و سپس در کشورهای اروپایی بوجود آورد'; and, quoting Xenophon's Oeconomicus, 'باغ‌هایی ... که نام آنها پردیس (فردوس) است'. Farahvashi confirms the Achaemenid walled park > 'paradise' semantic route and treats pardīs and ferdows as one word.\"},\n])\n\n# ---------------- node 9 : Greek paradeisos ----------------\nadd(9, [\n  {\"src\": \"KLN\", \"where\": \"leaf 600 (printed pp. 1124-1125) s.v. paradise\", \"stance\": \"supports\", \"note\": KLNPARA},\n  {\"src\": \"SKT\", \"where\": \"leaf 353 (Skeat p. 333) s.v. Paradise\", \"stance\": \"supports\",\n   \"note\": \"SKT.txt: 'Paradise. (F. — L. — Gk. — Pers.) F. paradis. — L. paradisus. — Gk. παραδεισος, park, pleasure-ground; ... now ascertained to be of Pers. origin. — O. Pers. (Zend) pairi-daēza, an enclosed place, walled in. — O. Pers. pairi (= Gk. περι), around; diz (= Skt. dih), to ... form, shape (hence to form a wall of ...)'.\"},\n  {\"src\": \"BRT\", \"where\": \"col. 866 s.v. pairi.daēza-\", \"stance\": \"supports\",\n   \"note\": \"BRT.txt: 'np. pāliz \\\"Garten\\\" [vgl. gr. LW. παραδεισος]' — Bartholomae marks παραδεισος explicitly as a loanword (LW.) from the Iranian word.\"},\n  {\"src\": \"FVQ\", \"where\": \"Jeffery p. 224\", \"stance\": \"supports\",\n   \"note\": \"FVQ_pages.txt leaf 241: 'The original word is Iranian, the Av. pairidaeza ... Xenophon introduced the word into Greek, and uses it of the parks and gardens of the Persian Kings, e.g. Anab. i, ii, 7, etc. After this date it is used fairly frequently, and in the LXX is sometimes used to translate gan.' Jeffery dates and sources the borrowing.\"},\n  {\"src\": \"SOD\", \"where\": \"p. 285, entry 7103\", \"stance\": \"supports\",\n   \"note\": \"SOD_pages.txt: Sogdian 'parδez (prδyz) © Av. pari-daeza, garden, orchard' shows the same Iranian word spreading eastward, parallel to its westward loan into Greek.\"},\n])\n\n# ---------------- node 10 : English paradise ----------------\nadd(10, [\n  {\"src\": \"KLN\", \"where\": \"leaf 600 (printed pp. 1124-1125) s.v. paradise\", \"stance\": \"supports\",\n   \"note\": \"KLN_1966.txt: 'paradise, n. — ME. paradis, fr. OF. (= F.) paradis, fr. Late L. paradisus, fr. Gk. παραδεισος ...' — the full Middle English > Old French > Late Latin > Greek chain Nourai's unlabelled arrow assumes.\"},\n  {\"src\": \"SKT\", \"where\": \"leaf 353 (Skeat p. 333) s.v. Paradise\", \"stance\": \"supports\",\n   \"note\": \"SKT.txt: 'Paradise. (F. — L. — Gk. — Pers.) F. paradis. — L. paradisus. — Gk. παραδεισος ... now ascertained to be of Pers. origin.' Skeat's language tags give the same route.\"},\n  {\"src\": \"PLA\", \"where\": \"Asbaghi p. 207 s.v. firdus\", \"stance\": \"supports\",\n   \"note\": \"incoming/PLA/PLA_pages.txt leaf 221: 'aw. pairidaeza >> griech. paradeisos, frz. paradis, engl. paradise, dtsch. Paradies.'\"},\n])\n\n# ---------------- node 11 : OP daika ----------------\nadd(11, [\n  {\"src\": \"HRN\", \"where\": \"no. 594, p. 132\", \"stance\": \"partial\",\n   \"note\": \"HRN.txt leaf 153: '594. dēg \\\"Topf\\\", vergl. dez, deze. phlv. dēg \\\"Topf\\\"; lat. figulus \\\"Töpfer\\\"; mhd. tigel, tegel, ahd. tegal \\\"Schmelztiegel\\\", an. digull \\\"Tiegel\\\". LW. kurd. dizik; afγ. dēg, decka; bel. dēg, dēz ...; Zu ai. √dih-, degdhi \\\"bestreichen, kitten\\\", got. deigan \\\"kneten, aus Thon formen\\\".' Horn does attach dēg to the root dheigh-, but reconstructs no Old Persian *daika-; the OP form is Hübschmann's addition and Hübschmann himself calls the whole connection 'fraglich'.\"},\n  {\"src\": \"PHD\", \"where\": \"leaf 48 (MacKenzie p. 27) s.v. dēg\", \"stance\": \"silent\",\n   \"note\": \"PHD.txt: 'dēg [dykʾ | N ~] cauldron.' MacKenzie records the Pahlavi word and its New Persian continuation but offers no etymology, so he neither supports nor contradicts an Old Persian *daika-.\"},\n  {\"src\": \"BRT\", \"where\": \"coll. 674-675 (daēz-, daēza-) and col. 747 (didā-)\", \"stance\": \"silent\",\n   \"note\": \"Bartholomae's articles on daēz-/daēza-/didā- list np. dez 'Burg' and pāliz among the Iranian reflexes but never a word for 'pot'; no Avestan or Old Persian *daika- exists in the AiW.\"},\n  {\"src\": \"ARY\", \"where\": \"pp. 278 and 297 (دژ, دیوار)\", \"stance\": \"silent\",\n   \"note\": \"Aryanpur's two entries under *DHEIGH- (دژ, دیوار) list Avestan DAĒZAYEITI/UZDAEZA, OP DIDA, Pahlavi DIZ/DĒWĀR, Gk. TEIKHOS, Lat. FINGŌ, Goth. DAIGS — دیگ is not among them, i.e. this modern Persian-IE dictionary does not put dīg under the root at all.\"},\n])\n\n# ---------------- node 12 : NP dig ----------------\nadd(12, [\n  {\"src\": \"HRN\", \"where\": \"no. 594, p. 132\", \"stance\": \"partial\",\n   \"note\": \"HRN.txt leaf 153: '594. dēg \\\"Topf\\\" ... phlv. dēg \\\"Topf\\\" ... Zu ai. √dih-, degdhi \\\"bestreichen, kitten\\\", got. deigan \\\"kneten, aus Thon formen\\\".' Horn connects NP dēg to the dheigh- root through the Pahlavi form, but posits no Old Persian antecedent and offers no derivation of the -g.\"},\n  {\"src\": \"PHD\", \"where\": \"leaf 48 (MacKenzie p. 27) s.v. dēg\", \"stance\": \"supports\",\n   \"note\": \"PHD.txt: 'dēg [dykʾ | N ~] cauldron' — the Pahlavi ancestor of NP dīg is attested (as Hübschmann already suspected, possibly a late form), so the Persian word is at least old Middle Persian.\"},\n  {\"src\": \"MON\", \"where\": \"vajehyab.com, Farhang-e Mo'in s.v. دیگ\", \"stance\": \"supports\",\n   \"note\": \"'دیگ [ په . ] (اِ.) ظرفی که در آن غذا پزند.' Mo'in tags dīg as Pahlavi ([په.]), i.e. inherited Iranian, not an Arabic or other loan. Archived https://vajehyab.com/?q=دیگ&d=moein\"},\n  {\"src\": \"AFM\", \"where\": \"leaf 70 (Addi Shir p. ~62) s.v. الديك\", \"stance\": \"partial\",\n   \"note\": \"AFM_pages.txt: '+ (الديك) ... معنى ديك ... وهو القدر' — Addi Shir lists Arabic dīk/dīg 'cooking pot' among the arabised Persian words, confirming that Persian dīg 'pot' is old enough to have been borrowed into Arabic; he gives no Indo-European etymology.\"},\n  {\"src\": \"ARY\", \"where\": \"pp. 278 and 297 (دژ, دیوار)\", \"stance\": \"silent\",\n   \"note\": \"Aryanpur's entries under *DHEIGH- do not contain دیگ; the modern Persian etymological dictionary does not treat dīg 'pot' as a reflex of this root.\"},\n])\n\n# ---------------- node 13 : Germanic daigaz ----------------\nadd(13, [\n  {\"src\": \"POK\", \"where\": \"IEW pp. 244-245 s.v. dheiĝh-\", \"stance\": \"supports\",\n   \"note\": \"POK_01.txt leaves 255-256: 'got. daigs m. \\\"Teig\\\" (*dhoighos), anord. deig, ags. dāg, ahd. teig ds.' Pokorny reconstructs exactly Nourai's Germanic *daigaz from the o-grade *dhoiĝho-s.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I pp. 833-834 s.v. dheigh-\", \"stance\": \"supports\",\n   \"note\": WLD + \" Walde-Pokorny add 'Got. þamma digandin \\\"dem Knetenden\\\", kasa digana \\\"Tongefäße\\\"' — the verb behind the 'one who kneads dough' sense of Nourai's second word.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 5.53 DOUGH (pp. 359-360)\", \"stance\": \"supports\",\n   \"note\": \"SYN.txt: '4. Goth. daigs, OE dag, etc., gen. Gmc. : Goth. digan \\\"mold, form\\\", Lat. fingere \\\"mold\\\", Skt. dih- \\\"smear\\\" ..., IE *dheigh-. Walde-P. 1.833 ff. Feist 118 f.' Buck's whole Germanic column (Goth. daigs, ON deig, Dan. dej, OE dag, OHG teic) is Nourai's *daigaz.\"},\n  {\"src\": \"KLN\", \"where\": \"leaf 261 (printed p. 477) s.v. dough\", \"stance\": \"supports\",\n   \"note\": KLNDOUGH},\n])\n\n# ---------------- node 14 : English dough, lady, dairy ----------------\nadd(14, [\n  {\"src\": \"KLN\", \"where\": \"leaf 261 (p. 477) s.v. dough; leaf 461 (pp. 858-859) s.v. lady; leaf 219 (pp. ~398-399) s.v. dairy\", \"stance\": \"supports\",\n   \"note\": KLNDOUGH + \" and 'lady, n. — ME. lafdi, lavede, ladi, fr. OE. hlæfdige, \\\"mistress of the house\\\", lit. \\\"loaf-maker\\\"' (Klein's dough entry closes 'Cp. dairy, duff ... and the second element in lady'). All three of Nourai's English words are Klein's own derivatives of the same base.\"},\n  {\"src\": \"SKT\", \"where\": \"leaf 140 (Skeat p. 120) s.vv. Dike, dairy, Dough; leaf 145 (p. 125) 'Dough; see Dike'\", \"stance\": \"supports\",\n   \"note\": \"SKT.txt: 'Dike ... A.S. dīc. + Du. dijk, Icel. díki, Dan. dige, Swed. dike, G. teich \\\"pond, tank\\\", Gk. τεῖχος, Skt. dehī \\\"rampart\\\". All from √DHIGH, to knead, form, mould; as in Dough, Figure.'; 'dairy. (Scand.) M.E. deierie ... dey, i.e. a milk-woman, farm-servant. + Icel. deigja, Swed. deja, a maid, dairy-maid, who was also the bread-maker; the orig. sense is \\\"kneader of dough\\\". Icel. deig, Swed. deg, dough.' Skeat gives Nourai's 'one who kneads dough / lady of the house' semantics verbatim.\"},\n])\n\n# ---------------- node 15 : Latin figura ----------------\nadd(15, [\n  {\"src\": \"LAT\", \"where\": \"leaf 437-438 (Ernout-Meillet pp. 419-420) s.v. fingo\", \"stance\": \"supports\",\n   \"note\": LATFINGO + \" Ernout-Meillet's 'proprement modeler dans l'argile' and 'figūra (formé avec le suffixe -ūra directement sur la racine)' is precisely Nourai's gloss 'result of kneading, shape'.\"},\n  {\"src\": \"LEW\", \"where\": \"Walde-Hofmann, Registerband (1956), Avestan index p. 46\", \"stance\": \"supports\",\n   \"note\": \"LEW_1910.txt leaf 58: 'pairidaēza- I 501, II 251; pairidaēzayeiti ...' — the Latin etymological dictionary treats the Avestan word under the Latin lemma at LEW I 501 (the fingō/figūra article); Buck 7.27 likewise cites 'Walde-H. 1.501 f.' for this group.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I pp. 833-834 s.v. dheigh-\", \"stance\": \"supports\",\n   \"note\": WLD + \" Walde-Pokorny list 'lat. fingō ... figulus \\\"Töpfer\\\", figūra \\\"Bildung, Gestalt, Figur\\\", fictiō, fictilis \\\"aus Ton gebildet\\\"' under the root, with the note that Latin g for expected h needs explaining.\"},\n  {\"src\": \"POK\", \"where\": \"IEW pp. 244-245 s.v. dheiĝh-\", \"stance\": \"supports\",\n   \"note\": \"POK_01.txt leaves 255-256: 'lat. fingō ... figūra Bildung, Gestalt, Figur, fictiō ...' — Pokorny's Latin section is Nourai's node.\"},\n])\n\n# ---------------- node 16 : English figure, fiction ----------------\nadd(16, [\n  {\"src\": \"KLN\", \"where\": \"leaf 319 (p. ~589) s.v. fiction; leaf 320 (pp. 590-591) s.vv. figure, figurate\", \"stance\": \"supports\",\n   \"note\": \"KLN_1966.txt: 'fiction, n. — F., fr. L. fictiōnem, acc. of fictiō, \\\"a forming, shaping\\\", fr. fictus, pp. of fingere, \\\"to form, shape\\\". The original meaning of this verb was \\\"to knead\\\". It derives fr. I.-E. base *dheigh-, *dhoigh-, *dhigh- ... whence also OE. dag, \\\"dough\\\"'; 'figurer, fr. L. figūrāre ... fr. figura'. Klein's 'original meaning ... to knead' is Nourai's gloss for the Latin node.\"},\n  {\"src\": \"SKT\", \"where\": \"leaf 140 (Skeat p. 120) s.v. Dike\", \"stance\": \"supports\",\n   \"note\": \"SKT.txt: '... All from √DHIGH, to knead, form, mould; as in Dough, Figure.' Skeat files English figure under the same root as dough, exactly as the chart does.\"},\n  {\"src\": \"LAT\", \"where\": \"leaf 437-438 (Ernout-Meillet pp. 419-420) s.v. fingo\", \"stance\": \"supports\",\n   \"note\": \"Ernout-Meillet: 'fictiō ... t. de droit fictio legis. Le nom n'apparaît pas avant l'époque impériale; surtout fréquent chez Quintilien' — the Latin source of English fiction, with its date; and figūra, whence F./E. figure.\"},\n])\n\n# ---------------- ROOT ref_check: leave as is ----------------\n\n# ---------------- ref_check upgrades ----------------\ndef setref(nid, ref, status, note):\n    arr = nodes[nid]['ref_check']\n    for it in arr:\n        if it['ref'] == ref:\n            it['status'] = status\n            it['note'] = note\n            return\n    arr.append({\"ref\": ref, \"status\": status, \"note\": note})\n\nsetref(2, \"BQT:918\", \"partial\",\n  \"RE-CHECKED. BQT_v2_pages.txt leaf 378 = printed p. 918 (leaf 379 carries the header 'دیو دولت' and the page numeral ۹۱۹). \"\n  \"The page has 'دیوار گر = دیوارساز و گلکار و بنّا را گویند' and 'دیوال، با لام، بر وزن و معنی دیوار است، چه در فارسی را و لام بهم تبدیل می‌یابند'; \"\n  \"Mo'in's footnote reads '#دیوار به کسر اول = دیوال = دیفال (عامیانه)، پهلوی dēvār ... رک: اشتقاق، هوبشمان ۹۵/۹۹؛ کردی dîwar ...؛ افغانی dēwāl، هوبشمان ۹۵ — \"\n  \"جداری که در اطراف خانه بنا کنند بجهت محصور کردن و حفاظت آن'. So Borhan/Mo'in confirm the word, the gloss 'wall' and a Pahlavi dēvār, and refer the etymology to \"\n  \"Hübschmann (i.e. *didā-vāra-); the page does not itself print Nourai's Old Persian compound.\")\n\nsetref(5, \"BQT:851\", \"supports\",\n  \"RE-CHECKED. BQT_v2_pages.txt leaf 311 = printed p. 851 (leaf 310 = p. 850 ends 'بقیه در صفحهٔ ۸۵۱'). The headword reads \"\n  \"'دژ = بکسر اول و سکون ثانی، قلعه و حصار باشد ۱، و بمعنی زشت و بدخوی و خشم ... نیز هست ۲', and Mo'in's footnote on the facing page (p. 850, s.v. دز) reads \"\n  \"'دز و دژ (ه.م.) ممکن است شکل لهجه‌ای باشد ... ساسانی dēz ... اوستا uzdaēza (سدّه، بارو و حصار) ... از daēz به معنی انباشتن، روی هم نهادن ... \"\n  \"پهلوی diz ... هوبشمان'. Borhan/Mo'in derive dež/dez from Avestan uz-daēza- 'rampart, wall' via Pahlavi diz — Nourai's arrow.\")\n\nsetref(7, \"BQT:359\", \"partial\",\n  \"RE-CHECKED. BQT_v1_pages.txt leaf 581 = printed p. 359 (the next leaf opens 'بقیه از صفحهٔ ۳۵۹'), s.v. پالیز: \"\n  \"'پالیز ۱ - بر وزن کاریز، بمعنی باغ و بوستان و کشتزار باشد عموماً و خربزه‌زار و خیارزار و هندوانه‌زار را گویند خصوصاً'; also 'پالیزبان - باغبان و بستان‌بان ... و نگاهدارندهٔ پالیز'. \"\n  \"Nourai's page number and gloss ('melon farm') are exactly right; Mo'in's etymological footnote ۱ is lost in this OCR, so the Avestan derivation itself is not readable here \"\n  \"(it is however given by Horn no. 279 and Bartholomae col. 866).\")\n\nsetref(8, \"BQT:1455\", \"supports\",\n  \"RE-CHECKED with tools/ref_page.py BQT:1455 (vol. 3 scan, pdf p. 248; image cached at data/verification/sources/refs/ocr/BQT/1455.png). \"\n  \"Headword 'فردوس ۸ - بکسر اول و ثالث و سکون ثانی و واو و سین بی‌نقطه، بهشت را گویند و باغ ...' with Mo'in's footnote 8: \"\n  \"'معرب از ایرانی. در اوستا دوبار به کلمهٔ pairi-daēza برمی‌خوریم (وندیداد فرگرد ۳ بند ۱۸؛ فرگرد ۵ بند ۹) و آن مرکب است از دو جزو: پیشوند pairi ... بمعنی گرداگرد و پیرامون؛ \"\n  \"دوم daēza از مصدر daēz بمعنی انباشتن و روی هم چیدن و دیوار گذاشتن. در زمان هخامنشیان ... پردیس‌ها - یا فردوس‌ها - که باغ‌های بزرگ و «پارک»‌های باشکوه پادشاه ... \"\n  \"یونانیان ... همان نام ایرانی را به صورت παράδεισος به کار بردند. در اکدی متأخر pardēsu و در عبری pardēs (پارک یا باغ) و در آرامی و سریانی نیز همین کلمه ... و در ارمنی partēz (باغ) \"\n  \"همه از ریشهٔ ایرانی هستند ... کلمهٔ فردوس که دوبار در قرآن آمده، از دین یهود و عیسوی به اسلام رسیده است.' \"\n  \"This is exactly Nourai's arrow Av. pairi-daēza- > NP pardīs/ferdows, with the Arabic/Qur'anic mediation spelled out.\")\n\nsetref(12, \"BQT:912,914\", \"supports\",\n  \"RE-CHECKED. BQT_v2_pages.txt leaf 374 = printed p. 914 (leaf 372 = p. 912, the دیز/دیزه and دیگدان entries; leaf 378 = p. 918 fixes the offset). \"\n  \"The headword on p. 914 reads 'دیگ، بکسر اول و سکون ثانی ... و کاف فارسی ... ظرفی که در آن چیزی پزند ۳', and Mo'in's footnote 3 reads \"\n  \"'به قول هوبشمان دیگ فارسی (افغانی dēg) از پارسی باستان *daika (دیگ) ... کردی dîzik ... شکل پهلوی dēg (دیگ) هیأت تازه‌ای است از آن ... هوبشمان ۹۵ ... افغانی dēg, decka؛ \"\n  \"بلوچی dēg, dēz ...؛ وخی و سریکلی ...؛ اشتقاق ۴۹۰ ... ورک: دیز.' Mo'in's note reproduces Hübschmann's Old Persian *daika- — the very form Nourai prints in node #11 — \"\n  \"while flagging (with Hübschmann) that the Pahlavi dēg is a late form.\")\n\nsetref(5, \"MON5:528\", \"not_checked\",\n  \"Mo'in vol. 5 (aʿlām / proper names) is neither on disk nor online (vajehyab/abadis carry only the lexicon volumes 1-3); the two-volume Adena abridgement on archive.org \"\n  \"has no Dezful article and grep for دژپل / دزفول in MON_part1/2 returns only incidental dialect citations. The Dezful < *dež-pol claim therefore remains unchecked in Mo'in, \"\n  \"though it is standard (see the node's sources).\")\n\njson.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/upd.py"
}
```


### [2026-09-04T18:56:02.168Z] TOOL RESULT

```
written
```


## [2026-09-04T18:56:07.195Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -m json.tool data/verification/page-126.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 126"
}
```


### [2026-09-04T18:56:08.933Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'transcription_suspect': 1, 'confirmed': 10, 'plausible': 3, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'partial': 5, 'not_checked': 4}
books consulted: {'supports': 51, 'partial': 10, 'silent': 4} | by book: {'ARY': 7, 'KLN': 7, 'BRT': 6, 'NYB': 4, 'LAT': 4, 'PHD': 4, 'MON': 4, 'HRN': 4, 'SKT': 4, 'WLD': 3, 'PLA': 3, 'SOD': 2, 'SYN': 2, 'HUB': 2, 'FVQ': 2, 'POK': 2, 'TLM': 1, 'IEC': 1, 'IRN': 1, 'AFM': 1, 'LEW': 1}
```


## [2026-09-04T18:56:15.489Z] TOOL CALL #100: Bash

```json
{
 "command": "sed -n '1,50p' tools/verify_archive_sources.py"
}
```


### [2026-09-04T18:56:15.530Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Archive every URL cited in data/verification/page-*.json that is not yet in
data/verification/sources/web/index.jsonl (post-pass, so no cited source is lost
even if an agent forgot to archive it).  Usage: verify_archive_sources.py [pages...]
"""
import sys, os, glob, json, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = os.path.join(ROOT, "data", "verification")
INDEX = os.path.join(VER, "sources", "web", "index.jsonl")

def indexed():
    s = set()
    if os.path.exists(INDEX):
        for line in open(INDEX, encoding="utf-8"):
            try:
                d = json.loads(line)
                if d.get("status") == 200:
                    s.add(d["url"])
            except Exception:
                pass
    return s

def main(argv):
    only = set(argv[1:])
    have = indexed()
    todo = {}
    for f in sorted(glob.glob(os.path.join(VER, "page-*.json"))):
        pg = os.path.basename(f)[5:-5]
        if only and pg not in only:
            continue
        d = json.load(open(f, encoding="utf-8"))
        for e in d.get("entries", []):
            for u in e.get("sources") or []:
                todo.setdefault(u, f"page {pg}, root {e.get('root')} (root-level)")
            for n in e.get("nodes", []):
                for u in n.get("sources") or []:
                    todo.setdefault(u, f"page {pg}, root {e.get('root')}, node #{n.get('id')} {n.get('words','')}")
    missing = [u for u in todo if u not in have]
    print(f"{len(todo)} cited URLs, {len(missing)} not yet archived")
    fails = 0
    for u in missing:
        r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "fetch_source.py"), u, "--note", "post-pass: " + todo[u]],
                           capture_output=True, text=True)
        if r.returncode != 0:
            fails += 1
            print("FAILED", u)
    print(f"archived {len(missing) - fails}, failed {fails}")

if __name__ == "__main__":
```


## [2026-09-04T18:56:21.375Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json\nP='data/verification/page-126.json'\nd=json.load(open(P,encoding='utf-8'))\nn={x['id']:x for x in d['entries'][0]['nodes']}\nadds={\n 2:['https://vajehyab.com/?q=دیوار&d=moein'],\n 5:['https://vajehyab.com/?q=دژ&d=moein'],\n 8:['https://vajehyab.com/?q=پردیس&d=moein','https://vajehyab.com/?q=فردوس&d=moein'],\n 12:['https://vajehyab.com/?q=دیگ&d=moein'],\n}\nfor k,v in adds.items():\n    s=n[k].setdefault('sources',[])\n    for u in v:\n        if u not in s: s.append(u)\njson.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=2)\nprint('ok')\nEOF\npython3 tools/verify_archive_sources.py 126 2>&1 | tail -5"
}
```


### [2026-09-04T18:56:26.657Z] TOOL RESULT

```
ok
44 cited URLs, 22 not yet archived
archived 22, failed 0
```


## [2026-09-04T18:56:29.029Z] TOOL CALL #102: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -m json.tool data/verification/page-126.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 126; echo \"exit=$?\""
}
```


### [2026-09-04T18:56:30.951Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'transcription_suspect': 1, 'confirmed': 10, 'plausible': 3, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'partial': 5, 'not_checked': 4}
books consulted: {'supports': 51, 'partial': 10, 'silent': 4} | by book: {'ARY': 7, 'KLN': 7, 'BRT': 6, 'NYB': 4, 'LAT': 4, 'PHD': 4, 'MON': 4, 'HRN': 4, 'SKT': 4, 'WLD': 3, 'PLA': 3, 'SOD': 2, 'SYN': 2, 'HUB': 2, 'FVQ': 2, 'POK': 2, 'TLM': 1, 'IEC': 1, 'IRN': 1, 'AFM': 1, 'LEW': 1}
exit=0
```


## [2026-09-04T18:56:39.353Z] TOOL CALL #103: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-126.json',encoding='utf-8'))\ne=d['entries'][0]\nprint('root consulted:',len(e['consulted']))\nfor n in e['nodes']:\n    print(n['id'], len(n.get('consulted',[])), sorted({c['src'] for c in n['consulted']}))\nEOF\nhead -c 3 data/verification/page-126.json | xxd | head -1\ngit -C /home/sfmqrb/git/rishe status --short | head"
}
```


### [2026-09-04T18:56:41.180Z] TOOL RESULT

```
root consulted: 4
1 5 ['ARY', 'BRT', 'LAT', 'NYB', 'TLM']
2 4 ['ARY', 'MON', 'NYB', 'PHD']
3 2 ['NYB', 'SOD']
4 4 ['BRT', 'IEC', 'SYN', 'WLD']
5 5 ['ARY', 'HRN', 'MON', 'NYB', 'PHD']
6 4 ['BRT', 'HUB', 'KLN', 'LAT']
7 5 ['ARY', 'BRT', 'HRN', 'HUB', 'PLA']
8 6 ['ARY', 'FVQ', 'IRN', 'KLN', 'MON', 'PLA']
9 5 ['BRT', 'FVQ', 'KLN', 'SKT', 'SOD']
10 3 ['KLN', 'PLA', 'SKT']
11 4 ['ARY', 'BRT', 'HRN', 'PHD']
12 5 ['AFM', 'ARY', 'HRN', 'MON', 'PHD']
13 4 ['KLN', 'POK', 'SYN', 'WLD']
14 2 ['KLN', 'SKT']
15 4 ['LAT', 'LEW', 'POK', 'WLD']
16 3 ['KLN', 'LAT', 'SKT']
00000000: 7b0a 20                                  {. 
 M data/verification/page-126.json
 M data/verification/sources/web/index.jsonl
?? data/verification/sources/web/00738e15ee065d37.txt
?? data/verification/sources/web/16b22d85686859b9.txt
?? data/verification/sources/web/30df29568cb42f71.txt
?? data/verification/sources/web/33872d7220e9ef48.txt
?? data/verification/sources/web/3fe779a77ac8e416.txt
?? data/verification/sources/web/420ba5a919cf3a63.txt
?? data/verification/sources/web/6b3ebb78d9ac530e.txt
?? data/verification/sources/web/71235dba08503be6.txt
```


## [2026-09-04T18:57:02.438Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-126.json` now satisfies the "consult every relevant book" rule; `python3 tools/verify_check.py 126` exits 0 with no PROBLEM lines.

**Consulted entries added** (65 node-level + 4 root-level; every node has ≥2 books, most 4–6)
- by stance: **supports 51, partial 10, silent 4** (root box: 4 more, all "supports")
- by book: ARY 7, KLN 7, BRT 6, NYB/LAT/PHD/MON/HRN/SKT 4 each, WLD/PLA 3, SOD/SYN/HUB/FVQ/POK 2, TLM/IEC/IRN/AFM/LEW 1

**Books used:** POK, WLD (Bd. I 833-834), AHD/Watkins, IEC, SYN (Buck 7.27 WALL, 5.53 DOUGH), BRT (coll. 674-675, 747, 866), TLM, KNT, PHD, NYB, HRN, HUB, SOD, BQT v1-v3, MON (vajehyab), ARY, IRN, KLN, SKT, LAT (Ernout-Meillet), LEW (Registerband), FVQ, PLA (Asbaghi), AFM.

**ref_check upgrades (5 re-checks, all previously not_found / not_checked / thin):**
- `BQT:1455` (node 8, ferdows) `not_checked → supports` — fetched vol. 3 scan via `tools/ref_page.py BQT:1455`; Mo'in's footnote gives the full Av. *pairi-daēza* → παράδεισος → Akk./Heb./Aram./Arm. → Qur'anic firdaws route. Best single find of the pass.
- `BQT:912,914` (node 12, dīg) `partial → supports` — Mo'in's footnote on p. 914 literally prints "به قول هوبشمان دیگ فارسی … از پارسی باستان \*daika", i.e. Nourai's node #11 form.
- `BQT:851` (node 5, dež) `partial → supports` — footnote (p. 850, s.v. دز) derives dez/dež from Av. *uz-daēza-* via Pahlavi *diz*.
- `BQT:918` (node 2, dīvār) `not_found → partial` — page located and quoted; Mo'in gives Pahlavi *dēvār* and refers the etymology to Hübschmann (i.e. *\*didā-vāra-*), not to Nourai's *\*daigha-vāra-*.
- `BQT:359` (node 7, pālīz) note corrected — page number confirmed exactly (next leaf reads "بقیه از صفحهٔ ۳۵۹"); status stays `partial` (gloss confirmed, footnote lost in OCR).
- `MON5:528` re-checked and confirmed still `not_checked` (vol. 5 is aʿlām, absent on disk and online; no Dezful article in the 2-vol abridgement).

**Verdict changes: none.** Nothing overturned an existing verdict. Two things worth flagging that the new material sharpened without changing the call: Nyberg (Part II p. 67) endorses *\*didā-vāra-* for dīvār, confirming node #1's existing `transcription_suspect` reading; and the nodes 11/12 `disputed` verdicts survive — BQT and Horn only relay Hübschmann's *\*daika-*, and Hübschmann himself called the root connection "fraglich", while Aryanpur's modern Persian-IE dictionary omits دیگ from the root entirely (recorded as "silent").

**Also written:** `data/verification/sources/refs/ocr/ARY/0297.vision.txt` (ARY p. 297 دیوار entry, read from the page image); 22 URLs archived via `verify_archive_sources.py` (5 new vajehyab/Mo'in pages added to node `sources`).
