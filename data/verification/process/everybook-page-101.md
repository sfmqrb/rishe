# Verification process log — everybook-page-101


## [2026-09-04T18:24:56.751Z] INPUT

Task: bring an existing verification file up to the "consult every relevant book" rule. File: /home/sfmqrb/git/rishe/data/verification/page-101.json (roots B.r.k "to bless" and B.r.q "to shine", 22 nodes). The chart with Nourai's citations is /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-101.txt.

Read /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md, in particular the sections "Use EVERY relevant book on disk", "Checking Nourai's OWN cited references" and "Process documentation", and the source matrix /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md (file paths of every local book — they all exist under /home/sfmqrb/git/rishe/data/verification/sources/refs/; the reference table /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json gives page offsets and lookup hints; scanned pages via tools/ref_page.py, e.g. BQT:1500 or BQT5:12).

For each root entry and for EVERY node: grep the books the matrix lists for that node's language (Semitic/Arabic: Klein KLN, Jeffery FVQ, Addi Shir AFM, Asbaghi PLA, Fraenkel AFA, Zimmern AKD, Lokotsch LKT, Jawaliqi ARB, al-Unaysi TAD; Persian: Horn HRN, Hübschmann HUB, Borhan BQT vols 1-5, Mo'in MON, Aryanpur ARY; Greek/Latin/English: Klein, Skeat SKT, Funk & Wagnalls FSD, Webster WEB, Watkins AHD, Ernout-Meillet LAT, Walde LEW; Sanskrit: Buck SYN, Mann IEC, Hobson-Jobson HJB), and add a `consulted` array to the node exactly as specified: {"src","where","stance" (supports/contradicts/partial/silent),"note" with the quoted phrase}. At least two different books per node where the matrix lists two or more; "silent" entries count. Do not duplicate what is already in `ref_check` (Nourai's own citations) — but if a `ref_check` item is `not_checked` and the book is NOW on disk, re-check it and update its status/note. Do NOT change verdicts, derivations or sources unless a book plainly overturns the existing verdict; in that case update the verdict, append one sentence to `derivation`, and say so in your summary. If you use a web page, archive it with tools/fetch_source.py and add it to `sources`.

Write the file back in place (valid JSON, UTF-8). Run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 101` (0 PROBLEM lines; "books consulted" tally non-empty). Reply with a short summary: number of consulted entries by stance, which books were used, any ref_check upgrades, and any verdict changes with reasons.


## [2026-09-04T18:24:58.383Z] AGENT

I'll start by reading the instructions and context files.


## [2026-09-04T18:25:00.853Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:25:00.878Z] TOOL RESULT

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


## [2026-09-04T18:25:01.004Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T18:25:01.017Z] TOOL RESULT

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


## [2026-09-04T18:25:05.158Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-101.txt"
}
```


### [2026-09-04T18:25:05.210Z] TOOL RESULT

```
=== PDF page 101 (book page 71) ===
--- entry 0 ---
ROOT [Semitic] B.r.k : originally "to kneel" used of the camel. Eventually the root developed the sense of "to bless".  (refs FVQ:75)
#1 (parent #0) [Arabic] refs=KLN:164; FVQ:75 | b.r.k : to bless ; barakat : blessing
  #2 (parent #1) [Persian] refs=FVA:45 | barekat «برکت» : blessing | extra: تبریک ، تبرّک ، مبارک
#3 (parent #0) [Akkadian] refs=KLN:164; AHD:579 | karâbu : to bless (letters are interchanged)
#4 (parent #0) [Hebrew] refs=KLN:164, 274 | berâkah : blessing ; kerŭbh : a winged angel (consonants R & B are reversed)
  #5 (parent #4) [Arabic] refs=MON:2958 | karŭbiyy : a winged angel
    #6 (parent #5) [Persian] refs=MON:2958 | karrŭbî «کرّوبی» : angel | extra: کروبیان، کروبیون
  #7 (parent #4) [English] refs=AHD:231 | cherub : a winged angel (of love)
  #8 (parent #4) [Greek] refs=AHD:579; KLN:680 | gruphos, grups : an eagle-headed lion
    #9 (parent #8) [Latin] refs=AHD:579 | gryphus
      #10 (parent #9) [Old French] refs=KLN:680 | grifion
        #11 (parent #10) [English] refs=AHD:579 | griffin
--- entry 1 ---
ROOT [Semitic] B.r.q : to shine  (refs KLN:514)
#1 (parent #0) [Arabic] refs=KLN:514 | b.r.q : to shine
  #2 (parent #1) [Persian] refs=FVA:45; SOR:35 | barq «برق» : lightning, electricity | extra: برّاق ، بارقه
#3 (parent #0) [Akkadian] refs=KLN:514 | baraqtu : lightning
#4 (parent #0) [Greek] refs=KLN:514 | smaraldos : a shiny stone, emerald
  #5 (parent #4) [Arabic] refs=MON:1746 | 
    #6 (parent #5) [Persian] refs=MON:1746; KLN:514 | zomorrod «زمرّد» : emerald
  #7 (parent #4) [Latin] refs=KLN:514 | smaragdus
    #8 (parent #7) [English] refs=AHD:427 | smaragdite : a green mineral
    #9 (parent #7) [Old French] refs=KLN:514 | esmeralde
      #10 (parent #9) [English] refs=AHD:427 | emerald
#11 (parent #0) [Sanskrit] refs=SKT:163; KLN:514 | marakata : emerald
```


## [2026-09-04T18:25:05.514Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-101.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:12000])\n\""
}
```


### [2026-09-04T18:25:08.794Z] TOOL RESULT

```
{
 "pdf_page": 101,
 "book_page": 71,
 "verified_by": "claude-fable-5-1",
 "verified_on": "2026-09-04",
 "entries": [
  {
   "entry": 0,
   "root": "B.r.k",
   "verdict": "confirmed",
   "modern_form": "Semitic root b-r-k: Proto-Semitic *birk- 'knee' / West Semitic brk 'to kneel; to bless' (AHD Semitic roots brk)",
   "note": "The root is real and its label 'Semitic' is right. Wiktionary reconstructs Proto-Semitic *birk- 'knee' (Akk. birkum, Heb. berekh, Ug. brk, Syr. burkā, Ge'ez bərk) with a metathetic variant *rukbat- (Ar. rukba). The 'kneel (of a camel) > bless' story is the traditional Gesenius/BDB account and matches Arabic baraka 'to kneel (camel)' / bāraka 'to bless'. The AHD Semitic appendix (Nourai's own AHD source) instead treats brk 'to bless' as 'probably a metathesized variant of krb' (Akk. karābu 'to praise, bless') — that is the hypothesis underlying Nourai's Akkadian/Hebrew cherub branch; it is accepted by AHD and Klein but rejected by recent Hebrew lexicography (SAHD, citing Mitchell: metathesis of first and third radicals is extremely rare). The griffin sub-branch is speculative (Klein) and not adopted by AHD's own griffin entry.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/birk-",
    "https://ahdictionary.com/word/semitic.html",
    "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%83%D8%A9"
   ],
   "ref_check": [
    {
     "ref": "FVQ:75",
     "status": "supports",
     "note": "FVQ_pages.txt leaf 92 (Jeffery p. 75), s.v. Baraka: 'To bless. ... The primitive verb b-r-k, which is not used in the Qur'an, means to kneel, used specially of the camel, so that baraka is the technical word for making a camel kneel. In this primitive sense it is common Semitic ... It was in the N. Semitic area, however, that the root seems to have developed the sense of to bless, and from thence it passed to the S. Semitic area. Thus we have Heb. bērēk, and Phon. brk to bless; Aram. brk to bless or praise; Syr. barrek ... From this N. Semitic sense we find derived the Sab. brk, Eth. bāraka to bless, celebrate the praises of, and Ar. bāraka as above.' — exactly Nourai's 'kneel (of the camel) → bless' story."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Arabic",
     "words": "b.r.k; barakat",
     "verdict": "confirmed",
     "derivation": "Arabic root b-r-k: baraka 'to kneel (of a camel)' (verbal noun burūk), Form III bāraka 'to bless', Form II barraka, Form VI tabāraka 'be blessed'; the noun baraka(t) 'blessing, divine favour' is the maṣdar-type noun of the root, with tāʾ marbūṭa -at (hence the transliteration barakat). Cognate with Hebrew bērēkh 'to bless' / bərākhā 'blessing'. Wiktionary lists 11 Arabic derivatives of the root.",
     "sources": [
      "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%83%D8%A9",
      "https://en.wiktionary.org/wiki/%D7%91%D7%A8%D7%9B%D7%94"
     ],
     "ref_check": [
      {
       "ref": "KLN:164",
       "status": "supports",
       "note": "KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, from the stem of bērākh, he blessed, which is rel. to Aram. bārākh, Arab. bāraka, Ethiop. bārāka, he blessed, Akkad. karābu (a metathesis form), to bless, Ethiop. mekrab (metath.), temple. Cp. cherub, griffin.' Gives Arab. bāraka 'he blessed' under the Semitic root and the Akkadian metathesis, as the chart does."
      },
      {
       "ref": "FVQ:75",
       "status": "supports",
       "note": "Same page as the root: 'Ar. bāraka as above' derived from the N. Semitic sense 'to bless' (FVQ_pages.txt leaf 92)."
      }
     ]
    },
    {
     "id": 2,
     "lang": "Persian",
     "words": "barekat",
     "verdict": "confirmed",
     "derivation": "New Persian barakat برکت is a direct loan of Arabic baraka(t) with the Arabic construct/pausal -at preserved as -at (a regular treatment of Arabic feminine nouns in Persian, cf. رحمت, نعمت); Wiktionary derives Urdu barkat from Classical Persian barakat < Arabic. The extra forms are all Arabic derivatives of the same root borrowed into Persian: tabrīk تبریک (Form II maṣdar 'congratulation'), tabarruk تبرّک (Form V maṣdar 'seeking blessing; blessed object'), mubārak مبارک (Form III passive participle 'blessed').",
     "sources": [
      "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%DA%A9%D8%AA",
      "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%83%D8%A9"
     ],
     "ref_check": [
      {
       "ref": "FVA:45",
       "status": "not_checked",
       "note": "FVA (Nahvi, Farhang-e vazheha-ye arabi dar farsi) has no digital copy (refs_online.json)."
      }
     ]
    },
    {
     "id": 3,
     "lang": "Akkadian",
     "words": "karâbu",
     "verdict": "plausible",
     "derivation": "Akkadian karābu 'to pray, bless, greet, praise' (participle kāribu 'one who blesses/intercedes', diminutive kurību, a protective genius) is a real word of root k-r-b. Its connection to b-r-k is the metathesis hypothesis (Dhorme; Klein 164; AHD Semitic roots: 'krb, to praise, common Semitic root, with West Semitic metathesized variant brk'). So Nourai's cited sources (KLN, AHD) do assert this, and AHD still does; but the Semantics of Ancient Hebrew Database (Mitchell) rejects it because metathesis of the first and third radicals is extremely rare, and Wiktionary's Proto-Semitic *birk- page lists no Akkadian karābu. Verdict: accepted by some, rejected by others.",
     "sources": [
      "https://ahdictionary.com/word/semitic.html",
      "https://sahd-online.com/words/krub/",
      "https://www.etymonline.com/word/cherub",
      "https://ahdictionary.com/word/search.html?q=griffin"
     ],
     "ref_check": [
      {
       "ref": "KLN:164",
       "status": "supports",
       "note": "KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, from the stem of bērākh, he blessed, which is rel. to Aram. bārākh, Arab. bāraka, Ethiop. bārāka, he blessed, Akkad. karābu (a metathesis form), to bless, Ethiop. mekrab (metath.), temple. Cp. cherub, griffin.' Klein calls Akkad. karābu 'a metathesis form' of b-r-k — Nourai's 'letters are interchanged'."
      },
      {
       "ref": "AHD:579",
       "status": "partial",
       "note": "AHD:579 is the 1976 dictionary page (griffin); the current AHD griffin entry (archived, https://ahdictionary.com/word/search.html?q=griffin) derives griffin only 'from Greek grūps' with no Semitic link, but the AHD Semitic-roots appendix (archived, https://ahdictionary.com/word/semitic.html) s.v. krb: 'Common Semitic root, with West Semitic metathesized variant brk. cherub, from Hebrew kərûb, cherub; akin to Akkadian karābu, to praise, bless. Compare also brk' and s.v. brk: 'West Semitic, to bless. Probably a metathesized variant of krb.' — so AHD supports the Akkadian karābu ~ brk metathesis."
      }
     ]
    },
    {
     "id": 4,
     "lang": "Hebrew",
     "words": "berâkah; kerŭbh",
     "verdict": "plausible",
     "derivation": "bərākhā בְּרָכָה 'blessing' (root b-r-k, verb bērēkh 'to bless', berekh 'knee') is a straightforward member of the root and is confirmed (cognate with Arabic baraka). kərūḇ כְּרוּב 'cherub' (pl. kərūḇīm; Gen. 3:24, Ex. 25:18) is by the mainstream view a loan from Akkadian kāribu/kurību 'intercessor; protective winged genius' (root k-r-b, karābu 'to bless') — so it belongs with Akkadian karābu (node 3), and the chart's placing of it under b-r-k stands or falls with the krb/brk metathesis hypothesis: endorsed by Klein and AHD, rejected by SAHD/Mitchell. Robert Alter's alternative ('hybrid' or, by consonant inversion, rkb 'mount/steed') is also on the table. Worst verdict for the node: plausible.",
     "sources": [
      "https://en.wiktionary.org/wiki/%D7%91%D7%A8%D7%9B%D7%94",
      "https://en.wiktionary.org/wiki/%D7%9B%D7%A8%D7%95%D7%91",
      "https://sahd-online.com/words/krub/",
      "https://ahdictionary.com/word/search.html?q=cherub"
     ],
     "ref_check": [
      {
       "ref": "KLN:274",
       "status": "supports",
       "note": "KLN_1966.txt leaf 155 (printed pp. 274-275), s.v. 'cherub': 'Heb. kerūbh, winged angel, prob. rel. to Akkad. karābu, to bless, karibu, one who blesses, epithet of the bull-colossus, and to Heb. bērēkh, he blessed, berākhāh, blessing. See berakah and cp. griffin.' Klein connects kerūbh with Heb. bērēkh/berākhāh via Akkad. karābu, i.e. the reversed consonants Nourai notes."
      },
      {
       "ref": "KLN:164",
       "status": "supports",
       "note": "KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, from the stem of bērākh, he blessed, which is rel. to Aram. bārākh, Arab. bāraka, Ethiop. bārāka, he blessed, Akkad. karābu (a metathesis form), to bless, Ethiop. mekrab (metath.), temple. Cp. cherub, griffin.'"
      }
     ]
    },
    {
     "id": 5,
     "lang": "Arabic",
     "words": "karŭbiyy",
     "verdict": "confirmed",
     "derivation": "Arabic karūbī كَرُوبِيّ 'cherub, archangel' (pl. karūbiyyūn, as in al-malāʾika al-karūbiyyūn) is, per Wiktionary, borrowed from Hebrew kərūḇ (in practice through Jewish Aramaic/Syriac kərūḇā, the vehicle of most biblical vocabulary into Arabic) with the Arabic nisba suffix -iyy added to form an adjective/noun of relation; the word appears in early Islamic tradition (hadith and tafsīr) for the highest angels. Not from the Akkadian directly.",
     "sources": [
      "https://en.wiktionary.org/wiki/%D9%83%D8%B1%D9%88%D8%A8%D9%8A",
      "https://en.wiktionary.org/wiki/%D7%9B%D7%A8%D7%95%D7%91",
      "https://vajehyab.com/?q=کروبی&d=moein"
     ],
     "ref_check": [
      {
       "ref": "MON:2958",
       "status": "supports",
       "note": "vajehyab.com (Mo'in) s.v. کروبی: '(کَ یّ) [ع.] (اِ.) فرشتة مقرب درگاه. ج. کروبیون' — tagged Arabic; Mo'in's page numbers cannot be mapped online. Archived https://vajehyab.com/?q=کروبی&d=moein."
      }
     ]
    },
    {
     "id": 6,
     "lang": "Persian",
     "words": "karrŭbî",
     "verdict": "confirmed",
     "derivation": "Persian karrūbī کرّوبی is Arabic karūbī taken over unchanged (Persian writers often geminate the r, karrūbī, as Nourai's spelling shows); the plurals karrūbiyān کروبیان (Persian -ān) and karrūbiyūn کروبیون (Arabic sound plural) are both used. Attested in classical poetry, e.g. Sa'di's Bustan (13th c.), as quoted in the chart. Gloss 'angel' is loose: the word means specifically 'cherub, one of the highest angels'. Nourai's source MON (Mo'in) is the standard Persian dictionary for this and Wiktionary's Arabic entry confirms the Arabic base; no independent Persian etymological page was found, but the Arabic loan is uncontroversial.",
     "sources": [
      "https://en.wiktionary.org/wiki/%D9%83%D8%B1%D9%88%D8%A8%D9%8A",
      "https://vajehyab.com/?q=کروبی&d=moein"
     ],
     "ref_check": [
      {
       "ref": "MON:2958",
       "status": "supports",
       "note": "vajehyab.com (Mo'in) s.v. کروبی [ع.] 'فرشتة مقرب درگاه، ج. کروبیون'; also کروبیان 'فرشتگان مقرب درگاه' and کروبیون 'جِ کروبی' — the Persian word is marked as an Arabic loan, as the arrow says (archived https://vajehyab.com/?q=کروبی&d=moein)."
      }
     ]
    },
    {
     "id": 7,
     "lang": "English",
     "words": "cherub",
     "verdict": "confirmed",
     "derivation": "Hebrew kərūḇ was transliterated in the Septuagint (3rd–2nd c. BCE) as Greek χερούβ (pl. χερουβίμ), taken into Late Latin as cherub (pl. cherubim, Vulgate), and borrowed into Middle English in the late 14th c. as cherub 'an order of angels'; the sense 'winged child, putto' (the '(of love)' in Nourai's gloss) is Renaissance art usage, in English from c. 1705. The chart correctly draws it from Hebrew, not through Arabic. AHD's entry: 'from Late Latin, from Hebrew kərûb; see krb'.",
     "sources": [
      "https://www.etymonline.com/word/cherub",
      "https://ahdictionary.com/word/search.html?q=cherub",
      "https://en.wiktionary.org/wiki/%D7%9B%D7%A8%D7%95%D7%91"
     ],
     "ref_check": [
      {
       "ref":
```


## [2026-09-04T18:25:12.619Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-101.json'))\nfor e in d['entries']:\n    print('ENTRY',e['entry'],e['root'],'consulted' in e)\n    for n in e['nodes']:\n        print('  ',n['id'],n['lang'],n['words'],'| ref_check:',[(r['ref'],r['status']) for r in n.get('ref_check',[])],'| consulted:',len(n.get('consulted',[])))\n\""
}
```


## [2026-09-04T18:25:13.424Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-101.json'))\nprint(json.dumps(d['entries'][0]['nodes'][6:],ensure_ascii=False,indent=1))\n\" | head -200"
}
```


### [2026-09-04T18:25:14.601Z] TOOL RESULT

```
ENTRY 0 B.r.k False
   1 Arabic b.r.k; barakat | ref_check: [('KLN:164', 'supports'), ('FVQ:75', 'supports')] | consulted: 0
   2 Persian barekat | ref_check: [('FVA:45', 'not_checked')] | consulted: 0
   3 Akkadian karâbu | ref_check: [('KLN:164', 'supports'), ('AHD:579', 'partial')] | consulted: 0
   4 Hebrew berâkah; kerŭbh | ref_check: [('KLN:274', 'supports'), ('KLN:164', 'supports')] | consulted: 0
   5 Arabic karŭbiyy | ref_check: [('MON:2958', 'supports')] | consulted: 0
   6 Persian karrŭbî | ref_check: [('MON:2958', 'supports')] | consulted: 0
   7 English cherub | ref_check: [('AHD:231', 'supports')] | consulted: 0
   8 Greek gruphos, grups | ref_check: [('KLN:680', 'supports'), ('AHD:579', 'partial')] | consulted: 0
   9 Latin gryphus | ref_check: [('AHD:579', 'supports')] | consulted: 0
   10 Old French grifion | ref_check: [('KLN:680', 'supports')] | consulted: 0
   11 English griffin | ref_check: [('AHD:579', 'supports')] | consulted: 0
ENTRY 1 B.r.q False
   1 Arabic b.r.q | ref_check: [('KLN:514', 'supports')] | consulted: 0
   2 Persian barq | ref_check: [('FVA:45', 'not_checked'), ('SOR:35', 'not_checked')] | consulted: 0
   3 Akkadian baraqtu | ref_check: [('KLN:514', 'partial')] | consulted: 0
   4 Greek smaraldos | ref_check: [('KLN:514', 'supports')] | consulted: 0
   5 Arabic  | ref_check: [('MON:1746', 'supports')] | consulted: 0
   6 Persian zomorrod | ref_check: [('MON:1746', 'supports'), ('KLN:514', 'partial')] | consulted: 0
   7 Latin smaragdus | ref_check: [('KLN:514', 'supports')] | consulted: 0
   8 English smaragdite | ref_check: [('AHD:427', 'partial')] | consulted: 0
   9 Old French esmeralde | ref_check: [('KLN:514', 'supports')] | consulted: 0
   10 English emerald | ref_check: [('AHD:427', 'supports')] | consulted: 0
   11 Sanskrit marakata | ref_check: [('KLN:514', 'supports'), ('SKT:163', 'partial')] | consulted: 0
```


### [2026-09-04T18:25:16.200Z] TOOL RESULT

```
[
 {
  "id": 7,
  "lang": "English",
  "words": "cherub",
  "verdict": "confirmed",
  "derivation": "Hebrew kərūḇ was transliterated in the Septuagint (3rd–2nd c. BCE) as Greek χερούβ (pl. χερουβίμ), taken into Late Latin as cherub (pl. cherubim, Vulgate), and borrowed into Middle English in the late 14th c. as cherub 'an order of angels'; the sense 'winged child, putto' (the '(of love)' in Nourai's gloss) is Renaissance art usage, in English from c. 1705. The chart correctly draws it from Hebrew, not through Arabic. AHD's entry: 'from Late Latin, from Hebrew kərûb; see krb'.",
  "sources": [
   "https://www.etymonline.com/word/cherub",
   "https://ahdictionary.com/word/search.html?q=cherub",
   "https://en.wiktionary.org/wiki/%D7%9B%D7%A8%D7%95%D7%91"
  ],
  "ref_check": [
   {
    "ref": "AHD:231",
    "status": "supports",
    "note": "AHD online s.v. cherub (archived, https://ahdictionary.com/word/search.html?q=cherub): '[Middle English, from Late Latin, from Hebrew kərûb; see krb in the Appendix of Semitic roots.]' — Hebrew → (Latin →) English as in the chart; AHD:231 is the 1976 page of this entry."
   }
  ]
 },
 {
  "id": 8,
  "lang": "Greek",
  "words": "gruphos, grups",
  "verdict": "plausible",
  "derivation": "Greek γρύψ grȳps, gen. γρυπός grȳpós 'griffin' (Herodotus, Aeschylus) — the second form Nourai gives, 'gruphos', is not a Greek nominative but reflects the genitive grypos / Latin gryphus. Its origin is unsettled: one view links it to γρυπός 'hook-nosed, curved' (PIE *ger- 'to bend'); Klein (KLN:680, Nourai's source) and Beekes allow a Pre-Greek/Anatolian loan ultimately from Semitic (Akkadian karūbu/kāribu, Hebrew kərūḇ) 'through the medium of the Hittites', making it a doublet of χερούβ. Wiktionary reports both; AHD's own griffin entry gives no Semitic source, and SAHD notes Brown's kərūḇ–γρύψ link 'finds minimal scholarly acceptance'. So the edge Hebrew kerubh → Greek gryps is a respectable but minority hypothesis.",
  "sources": [
   "https://en.wiktionary.org/wiki/%CE%B3%CF%81%CF%8D%CF%88",
   "https://www.etymonline.com/word/griffin",
   "https://ahdictionary.com/word/search.html?q=griffin",
   "https://sahd-online.com/words/krub/"
  ],
  "ref_check": [
   {
    "ref": "KLN:680",
    "status": "supports",
    "note": "KLN_1966.txt leaf 367 (printed p. 681), s.v. 'griffin, griffon, gryphon': 'ME. griffon, fr. OF. grifoun (F. griffon), fr. Late L. gryphus ..., fr. Gk. grūps, gen. grūpos, which was prob. borrowed from the Semites through the medium of the Hittites. Cp. Heb. kerūbh, a winged angel, Akkad. karibu, epithet of the bull-colossus, lit. one who blesses, and see cherub.' — Klein does derive Gk. grūps from the Semitic kerūbh/karibu word (via Hittite), Nourai's arrow."
   },
   {
    "ref": "AHD:579",
    "status": "partial",
    "note": "AHD online s.v. griffin (archived, https://ahdictionary.com/word/search.html?q=griffin): '[Middle English griffoun, from Old French griffon, from grif, from Latin grȳpus, grȳphus, variants of grȳps, grȳp-, from Greek grūps.]' — the chain below Greek is there, but AHD does not derive Greek grūps from Hebrew kerūbh; the Semitic appendix s.v. krb lists only cherub."
   }
  ]
 },
 {
  "id": 9,
  "lang": "Latin",
  "words": "gryphus",
  "verdict": "confirmed",
  "derivation": "Latin grȳps, grȳpis (Vergil, Pliny) was borrowed from Greek γρύψ; Late Latin created the thematic variants grȳpus and grȳphus (the -ph- is a hypercorrect spelling, etymonline: 'misspelling of grypus'), and it is the Late Latin gryphus/grifus that the Romance forms continue.",
  "sources": [
   "https://www.etymonline.com/word/griffin",
   "https://ahdictionary.com/word/search.html?q=griffin"
  ],
  "ref_check": [
   {
    "ref": "AHD:579",
    "status": "supports",
    "note": "AHD online s.v. griffin (archived, https://ahdictionary.com/word/search.html?q=griffin): 'from Latin grȳpus, grȳphus, variants of grȳps, grȳp-, from Greek grūps' — Latin gryphus from Greek."
   }
  ]
 },
 {
  "id": 10,
  "lang": "Old French",
  "words": "grifion",
  "verdict": "plausible",
  "derivation": "Old French grifon / griffon (12th c.; Anglo-Norman grifun, griffoun) is Late Latin gryphus with the augmentative/derivational suffix -on (< Latin -ōnem), i.e. from a Late Latin *grifonem; AHD: 'Old French griffon, from grif, from Latin grypus, gryphus'. The edge Latin → Old French → English is certain. The spelling 'grifion' printed here is not a standard attested Old French form (expected grifon/griffon); it may be Nourai's or the scan's slip for grifon, but since Klein's page could not be checked it is left as plausible rather than transcription_suspect.",
  "sources": [
   "https://www.etymonline.com/word/griffin",
   "https://ahdictionary.com/word/search.html?q=griffin"
  ],
  "ref_check": [
   {
    "ref": "KLN:680",
    "status": "supports",
    "note": "KLN_1966.txt leaf 367 (printed p. 681), s.v. 'griffin, griffon, gryphon': 'ME. griffon, fr. OF. grifoun (F. griffon), fr. Late L. gryphus ..., fr. Gk. grūps, gen. grūpos, which was prob. borrowed from the Semites through the medium of the Hittites. Cp. Heb. kerūbh, a winged angel, Akkad. karibu, epithet of the bull-colossus, lit. one who blesses, and see cherub.' Klein: 'ME. griffon, fr. OF. grifoun (F. griffon), fr. Late L. gryphus' — OF from Latin; the OF spelling grifion in the chart is Nourai's/OCR's."
   }
  ]
 },
 {
  "id": 11,
  "lang": "English",
  "words": "griffin",
  "verdict": "confirmed",
  "derivation": "Middle English griffoun, griffon (c. 1200 as a surname, 14th c. as the beast) from Old French grifon; the modern spelling griffin/gryphon settled in the 16th–17th c. (gryphon re-Latinised after Latin gryphus). Sense: the eagle-headed, lion-bodied guardian of Scythian gold in Greek legend.",
  "sources": [
   "https://www.etymonline.com/word/griffin",
   "https://en.wiktionary.org/wiki/%CE%B3%CF%81%CF%8D%CF%88",
   "https://ahdictionary.com/word/search.html?q=griffin"
  ],
  "ref_check": [
   {
    "ref": "AHD:579",
    "status": "supports",
    "note": "AHD online s.v. griffin (archived, https://ahdictionary.com/word/search.html?q=griffin): '[Middle English griffoun, from Old French griffon ...]' — English from Old French."
   }
  ]
 }
]
```


## [2026-09-04T18:25:31.272Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-101.json'))\ne=d['entries'][1]\nprint(e['root'],e['verdict']); print(e['note'][:800]); print(json.dumps(e['ref_check'],ensure_ascii=False))\nfor n in e['nodes']:\n    print('---',n['id'],n['lang'],n['words'],n['verdict'])\n    print(n['derivation'][:600])\n\""
}
```


### [2026-09-04T18:25:32.871Z] TOOL RESULT

```
B.r.q confirmed
Root, label and gloss are correct: Wiktionary reconstructs Proto-Semitic *baraḳ- 'lightning' (Akk. birqum, Heb. bārāq, Aram. barqā, Ar. barq, Ge'ez bärḳ), from Proto-Afroasiatic *bǐrk'-/*bǎrk'- 'to flash'; AHD Semitic appendix brq 'to flash (especially of lightning)' with emerald as its English derivative. The emerald branch (Semitic barraqtu/bāreqet → Greek smaragdos → Latin → Romance/English; Greek → Iranian/Arabic zumurrud) is standard (AHD, etymonline, Beekes, Noonan 2012). Two problems in this chart: the Greek form is misprinted/misread ('smaraldos' for smaragdos), and the Arabic → Persian direction for zumurrud is reversed relative to Wiktionary/MacKenzie (Middle Persian uzumburd is pre-Islamic).
[{"ref": "KLN:514", "status": "supports", "note": "KLN_1966.txt leaf 280 (printed pp. 514-515), s.v. 'emerald': 'ME. emeraude, fr. OF. esmeralde, esmeraude (F. émeraude), fr. L. smaragdus (whence also It. smeraldo, Sp. esmeralda), fr. Gk. smaragdos, maragdos, emerald, which is of Sem. origin. Cp. Heb. bāreqeth, Akkad. barraqtu, emerald, lit. something flashing, a derivative of Heb. bārāq, resp. Akkad. birqu, lightning, which are rel. to Aram. beraq, barqā, Arab. barq, lightning, Heb. bāraq, Aram. beraq, Arab. baraqa, Ethiop. baraqa, it flashed, glistened, Akkad. barāqu, to flash. Cp. OI. marakatam, Pers. zumurrud (whence Turk. zümrüd, whence Russ. izumrud), emerald, which are also Sem. loan words. Cp. also smaragd, which is a doublet of emerald.' Klein gives the whole Semitic b-r-q 'flash, lightning' family under 'emerald'."}]
--- 1 Arabic b.r.q confirmed
Arabic root b-r-q: baraqa 'to flash (of lightning), shine, glitter', noun barq 'lightning' (Qur'an 2:19–20 yakādu l-barqu yakhṭafu abṣārahum); Wiktionary: from Proto-Semitic *baraḳ-, noting the Arabic noun may be a deverbal formation rather than a direct inheritance. Derivatives barrāq 'glittering' (intensive faʿʿāl), bāriqa 'flash' (active participle).
--- 2 Persian barq confirmed
Persian barq برق is borrowed from Arabic barq 'lightning' (Wiktionary: 'Persian borrowed the term directly from Arabic'); attested in Ferdowsi's Shahnameh (c. 1000 CE) in the sense 'lightning', as the chart's quotation shows. The sense 'electricity' is a 19th–20th-c. semantic extension in Persian (cf. barqī 'electric', barq-kār 'electrician'), paralleled by Arabic barq 'telegraph'. The extras barrāq برّاق 'glittering' and bāriqa بارقه 'flash, gleam' are further Arabic derivatives of the root borrowed into Persian.
--- 3 Akkadian baraqtu plausible
The Akkadian word for 'lightning' is birqu (Proto-Semitic *baraḳ-, Wiktionary lists Akkadian birqum); the form Nourai prints, baraqtu, corresponds to Neo-Babylonian barraqtu 'emerald, a flashing green stone' (AHD: 'akin to Akkadian barraqtu and Hebrew bāreqet, a kind of gemstone (probably emerald)'), a -t- derivative of barāqu 'to flash'. So the word is real and belongs to this root (KLN:514 s.v. emerald cites it), but the gloss 'lightning' is a conflation: barraqtu is the gem-name, and it is precisely the form from which Greek smaragdos is derived, so it ought to sit as the parent of the Gree
--- 4 Greek smaraldos transcription_suspect
The Greek word is σμάραγδος smáragdos (also μάραγδος máragdos), 'emerald, green gem' (Herodotus, Theophrastus; Marcus Aurelius); 'smaraldos' with -ld- is not a Greek form and is almost certainly a misreading of the -gd- cluster (gd → ld) in the scan, since Klein (KLN:514) prints smaragdos. Etymology as drawn is confirmed: Wiktionary, AHD, etymonline and Beekes derive smaragdos from a Semitic source, Akkadian barraqtu / Hebrew bāreqet (Ex. 28:17) 'flashing gem', root b-r-q; the initial s- and the -agd- are the Greek adaptation of the Semitic b-r-q-t cluster (Noonan 2012 on Northwest Semitic loa
--- 5 Arabic  plausible
Pass-through node: Arabic zumurrud زُمُرُّد 'emerald' does go back to Greek smaragdos, but not directly: Wiktionary derives Arabic zumurrud from Persian zumurrud (< Middle Persian ʾwzmbwlt /uzumburd/ < Greek), i.e. Persian is the intermediary into Arabic rather than the reverse; another route often cited is Syriac zmaragdā. Arabic zabarjad 'peridot' is a doublet. The chart's Greek → Arabic → Persian ordering reverses the direction Wiktionary/MacKenzie give, so the Arabic node's parent is right in substance (Greek origin) but its child edge is not.
--- 6 Persian zomorrod disputed
Persian zumurrud/zomorrod زمرّد 'emerald' is, per Wiktionary, inherited from Middle Persian uzumburd (Book Pahlavi ʾwzmbwlt), itself borrowed from Greek σμάραγδος in the Sasanian period; the prothetic u-/i- (cf. Early New Persian uzmurud, Russian izumrud, Turkish zümrüt) reflects the un-Persian initial cluster sm- (s- > z- by voicing before m, -gd- > -rd/-rrd). Arabic zumurrud is then a loan FROM Persian (Wiktionary), not its source; etymonline likewise gives Persian zumurrud as the source of Turkish and Russian without an Arabic step. Modern sources therefore reverse the chart's Arabic → Pers
--- 7 Latin smaragdus confirmed
Latin smaragdus (m./f.), Pliny, Vulgate — a direct borrowing of Greek σμάραγδος with Greek -os rendered by the Latin 2nd-declension -us. In Vulgar/Medieval Latin it became smaralda, smaraldus, esmaraldus (with -gd- > -ld- by dissimilation and a prothetic e- before the s+consonant cluster), the source of all Romance forms.
--- 8 English smaragdite confirmed
smaragdite 'a green foliated amphibole found in eclogite/gabbro' is a learned mineralogical coinage (French smaragdite, H.-B. de Saussure, 1796) from Latin smaragdus + the mineral suffix -ite (< Greek -ītēs), named for its emerald-green colour; English from French in the early 19th c. The Latin → English edge is via scientific French, with no Old French step.
--- 9 Old French esmeralde confirmed
Old French esmeraude (12th c.), with the variants esmeralde, esmeragde, smaralde listed by Wiktionary, from Vulgar Latin *smaralda/*smaraldus (< Latin smaragdus): prothetic e- before s+C, -gd- > -ld- > -ud- (vocalisation of l before a consonant gives the standard esmeraude), so esmeralde is the conservative form; Modern French émeraude.
--- 10 English emerald confirmed
Middle English emeraude (c. 1300) from Old French esmeraude; the modern spelling emerald with -ld restored (after Medieval Latin esmaraldus / Old French esmeralde) appears from the 15th–16th c. AHD: 'Middle English emeraude, from Old French, from Medieval Latin esmeralda, esmeraldus, from Latin smaragdus, from Greek smaragdos'.
--- 11 Sanskrit marakata plausible
Sanskrit marakata (n.) 'emerald' (Pali marakata, Prakrit maragaya; hence Tamil marakatam, Thai morakot, Tibetan mar gad) is a genuine word and, as the chart implies, ultimately of Semitic origin; Wiktionary labels it 'from Semitic', linking it with Greek σμάραγδος. But the immediate source is debated: Noonan and the classicists (Chantraine, Beekes, Mayrhofer) treat marakata as a late loan from Greek smaragdos (loss of initial s-, -gd- > -k-t-), i.e. Greek rather than the Semitic root directly; older scholarship (still echoed in some sources) even took Sanskrit as the source of the Semitic word
```


## [2026-09-04T18:25:34.200Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['FVA','SOR','MON','BQT','AFM','PLA','AKD','LKT','TAD','ARB','SKT','FSD','WEB','LEW','LAT','HJB','SYN','IEC','ARY','HRN','HUB','AFA','KLN','FVQ']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-04T18:25:35.933Z] TOOL RESULT

```
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
SOR {"title": "K. Akhavan Zanjani — title unknown (Table IV entry for SOR lost in OCR; listed under Persian authors)", "kind": "none", "url": null, "lookup_hint": "Author search on archive.org/web found nothing.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online; title unidentified."}
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verif
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; t
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_f
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnair
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
```


## [2026-09-04T18:25:42.932Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT cherub ===\"; grep -n -i \"cherub\" SKT.txt | head -20\necho \"=== SKT griffin ===\"; grep -n -i \"griffin\\|gryphon\\|griffon\" SKT.txt | head -20\necho \"=== SKT emerald ===\"; grep -n -i \"emerald\\|smaragd\\|marakata\\|maragd\" SKT.txt | head -20"
}
```


### [2026-09-04T18:25:43.020Z] TOOL RESULT

```
=== SKT cherub ===
3361:Cherub.  (Heb.)  The  inie  pi.  is  iMentb- $m,  «  Hcb.  k'nlv  ^pl.  k^nivim),  a  mystic ficure.
=== SKT griffin ===
7999:OrifSn.  GrifTon.  iF.-L.-Gk.)  Bet- ter gfiff^n..  M.  E.  griffon.  ^V.  griffon  \ form'.'d  from  Low  L.  griffus,  a  gnflbn.  <- L.  gryphus,  extended  lonn  of  gryft^  a griffon. —  Gk.  ypif4>  i.stcm  upvw-)^  a  griffon, a  fabulous  animal  sup|>osed  to  nave  a hooked  beak.  —  Gk.  7^11^,  curved,  hook- beaked.
=== SKT emerald ===
5794:Emerald,  a  green  gem.  (F.  —  L.  — Gk.) M.E.  emeraude  —  O-  F.  esmeraude,  —  L. sviara^um^  ace.  of  smansgdm.^GV.  afii' payiios,  an  emerald.  Cf.  Skt.  marakata (the  same>.
5795:smaragduB.  (L.  —  Gk.)  \*,smara^dm (nbove).
17556:SmaragduB:  see  Smerftld.
22889:emerald—  smaragdM^H
```


## [2026-09-04T18:25:45.332Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AKD karabu/karibu ===\"; grep -n -i \"karâbu\\|karabu\\|kâribu\\|karibu\\|kurîbu\\|kerub\\|kerûb\" AKD.txt | head -30\necho \"=== AKD baraqtu/barqu ===\"; grep -n -i \"barraqtu\\|baraqtu\\|birqu\\|barâqu\\|smaragd\\|zumurrud\\|zamurrud\" AKD.txt | head -30"
}
```


### [2026-09-04T18:25:45.413Z] TOOL RESULT

```
=== AKD karabu/karibu ===
=== AKD baraqtu/barqu ===
964:sändii,  ein  Edelstein  (eig.  der  rotbraune)  :  dazu  wolü  hebr.  suham. [akk.  barraqtu  ein  Edelstein,   auch  im  Akk.  Fremdw.,  spät  und  vereinzelt
967:belegt  :  zunächst  viell.  >  späthebr.  iäräqet,  bänjat,  angeblich  Smaragd. Fraglich,  ob  das  Wort  semit.  Ursprungs  (dann  zu  St.  brq  blitzen);  idg. entspricht  skr.  maralcata,  griech.  fiÜQuySog,  of^dgaySog  usw.,  Smaragd.]
```


## [2026-09-04T18:25:55.348Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['AKD','AFA','SKT','LKT','FSD','WEB','LEW','LAT','HJB','SYN','IEC','KLN','TAD','AFM','ARB','PLA','MON','ARY','BQT','HRN','HUB','FVQ']:\n    print(k, d[k].get('page_offset'))\n\"\necho \"--- AKD context ---\"\nsed -n '955,975p' AKD.txt"
}
```


### [2026-09-04T18:25:56.988Z] TOOL RESULT

```
AKD leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
AFA leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SKT leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
LKT leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
FSD vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
WEB not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
LEW 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
LAT leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HJB leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SYN leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
TAD 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
AFM 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
ARB None
PLA 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
MON None
ARY printed page = pdf page + 1
BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HUB leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
FVQ printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
--- AKD context ---
auf  den  bab.  Mondgott  Sin,  dem  das  Silber  als  Metall  eignet.
akk.  eril,  älter  auch  warn,  urspr.  wohl  Kupfer,  dann  Bronze  (wohl ■<^  sum.  urtid);  damit  viell.  zus.  hängend  idg.  Wörter  wie  mittelpers.  röd, altind.  lohd-,  lat.  raiidus  Kupfer.  akk.  siparrii  Kupfer  :  >  viell.
hebr.  sej^er  an  einigen  Stelleu  (Jes.  30,  8;  Hi.  19,  23;  Ex.  17,  14);  ferner arab.  sifr,  sufr.
akk.  anaJiu  Zinn  (wohl  <^  sum.  *anag,  belegt  anna,  amma,  nagga, niggi)  :  hebr.  'annk,  syr.  'anJchä  O  wohl  arab.  'finuk),  äth.  na'sk.  Dazu jedenfalls  armen,  anag,  skr.  näga.     Unsicher,  wo  ursprünglich  heimisch.
akk.  jmrzillu  Eisen  :  daraus  zunächst  wohl  ]>  hebr.  barsei,  in  N. pr. harsill-,  aram.  parsel,  })arz9lä  O  arab.  firzil  Eisenfessel),  südarab.  frzn. Unsicher,  wo  ursprünglich  heimisch,  viell.,  worauf  auch  die  Endung  -ill weisen  könnte,  im  nordösü.  Kleinasien.  akk.  suhhi  Rost  :  ]>  wohl  syr.
suhtä,  mand.  sfitä.
akk.  abcirti  angeblich  Magnesit i,  aber  wohl  doch  besser  Blei  :  ]>- wohl  aram.  'äbärä,  'ahbärä  Blei  O  arab.  'abär).  Hebr.  'öpäret  Blei,  das sicher  auch  dazu  gehört,  steht  formell  etwas  abseits,  desgl.  armen,  kapar Blei.     Unsicher,  wo  das  Wort  ursprünglich  heimisch.
akk.  esniarfi  wahrsch.  Bez.  eines  Edelmetalls  :  dazu  vieU.  hebr. Ijasmal  bei  Ez.,  sowie  ägypt.  hsrnn,  beides  vieU.  Silbergold,  Elektrum.
akk.   siibil   ein   Edelstein    :  >   wohl   hebr.   .idbö.  akk.  sämtu,
sändii,  ein  Edelstein  (eig.  der  rotbraune)  :  dazu  wolü  hebr.  suham. [akk.  barraqtu  ein  Edelstein,   auch  im  Akk.  Fremdw.,  spät  und  vereinzelt
1)  Daß  die  eine  Pariser  Sargontafel  aus  Magnesit  besteht,  ist  m.  E.  kein  zwingender Beweis  für  abäru  =  Magnesit;  denn  vgl.  neben  der  Aufzählung  in  dieser,  der  Silber- und Goldtafel  auch  diejenige  in  Khors.  159  f.  und  Ann.  420  f.  Es  könnte  daher  z.  B. auch  aspü  =  Magnesit  sein.
      60      
belegt  :  zunächst  viell.  >  späthebr.  iäräqet,  bänjat,  angeblich  Smaragd. Fraglich,  ob  das  Wort  semit.  Ursprungs  (dann  zu  St.  brq  blitzen);  idg. entspricht  skr.  maralcata,  griech.  fiÜQuySog,  of^dgaySog  usw.,  Smaragd.]
[akk.  aJpü,  auch  jasupü  und  jos^m  eine  Steinart,  viell.  Magnesit  (s. S.  59  Anm.  1)  :  dazu  wohl  späthebr.  jclspe  ein  Steinname,  und  doch  wohl auch  griech.  Xaam?  usw.,  Jaspis^  [akk.  algnmisu  eine  Steinart,  auch  im
Akk.  wohl  Fremdw.  :  dazu  wohl  späthebr.  'älgahts,  schwerlich  „Eisstücke", bei  Ez.  u.  vieU.  Sir.  46,  5  und  ägypt.  "rqhS  eine  besonders  harte  Steiuart.
[akk.  burallu^  eine  Steinart,  vieU.  Berj^ll,  dann  zu  :  griech.  ß^Qvlloe, deutsch  auch  noch  in  Brille,  sanskr.  vrlidüriya,  praki\  verulia,  Pali  velu- riya  (syr.  hellüra  und  heridlä,  arab.  ballftr,  äth.  hereile  und  hellnr).
[akk.  sassu  wohl  weißer  Marmor  bezw.  Alabaster  :  dazu  späthebr. sajis,  ses,  syr.  slsä,  ägypt.  ss.]  akk.  p%lu,  pidu  Kalkstein  :  dazu
wohl  armen,  hur  Kalk,  sowie  griech.  nüQog  eine  Kalksteinart.
akk.  gassu  Gips  s.  oben  S.  31  f.  akk.  hipru  Erdpech,   As-
phalt^ :  >  hebr.  Icöper  Gen.  6,14,  aram.  hiprä  O  arab.  kufr,  sowie armen.  fe«pr,  falls  nicht  direkt  <[  akk.).  Ygl.  noch  unten  zu  hipr7hi. Da  akk.  Mm  Ofen  (s.  oben  S.  32)  speziell  gerade  vom  Asphalt-,  Pechofen des  Schiffers  gebraucht  wird,  wäre  es  nicht  unmöglich  daß  :  >  syr.  und jüd.-aram.  qträ^  Asphalt,  Pech  (>>  arab.  qlr  und  qär);  desgl.  dann  aber wohl  auch  aram.  gir,  gträ  Kalk  O  wohl  späthebr.  gtr,  sowie  arab.  gajjär, aber  auch  glr,  auch  südarab.  gjr  und  äth.  in  gajjara  tünchen).
alck.  naptu  Erdöl,  Naphtha  :  >  aram.  naptä,  neptä  O  arab.  naft, pers.  neft,  sowie  griech.  vätpfia^  usw.,  NapJdha).  akk.  etrdnu  wohl
```


## [2026-09-04T18:26:15.469Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /barraqtu/{print NR}' AKD.txt\necho \"=== AFA (Fraenkel) brk / baraka / karub ===\"\ngrep -n -i \"barak\\|berak\\|kerub\\|karub\\|kerûb\\|Segen\" AFA.txt | head -30\necho \"=== AFA smaragd/zumurrud ===\"\ngrep -n -i \"smaragd\\|zumurrud\\|zamurrud\\|barq\" AFA.txt | head -30"
}
```


## [2026-09-04T18:26:17.001Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT smaragd/emerald ===\"; grep -n -i \"smaragd\\|zumurrud\\|zümrüd\\|izumrud\\|marakata\" LKT.txt | head -30\necho \"=== LKT baraka/barq ===\"; grep -n -i \"baraka\\|barakat\\|barq\\|kerub\\|karub\" LKT.txt | head -30"
}
```


### [2026-09-04T18:26:17.097Z] TOOL RESULT

```
70
=== AFA (Fraenkel) brk / baraka / karub ===
=== AFA smaragd/zumurrud ===
```


### [2026-09-04T18:26:17.157Z] TOOL RESULT

```
=== LKT smaragd/emerald ===
4973:'Smaragd'  [vielleicht  aus  gr.  oiudtpaYboQ, wahrscheinlich  beides  aus  dem  Ind.], ebenso  tk.  ziimriid  [Kelekian  Kämüs 646  b];  hieraus  hu\^.  zumrtui,  russ.  izum- rud  'Smaragd'.  [Gorjnjew  122.  Mikl SlEtWb  404  b.    Bern  SlEtWb  441.
=== LKT baraka/barq ===
719:222.  Ar.  baraka:
760:'Grober  Stoff  oder  Mantel  daraus'  [Wohl aus  Kamelhaar,  vgl.  Dozy  DV  68  sq.); hieraus  mlat.  barracänus,  frz.  harracan 'grober  Stoff',  bouracan,  sp.  kat.  barra- gan,  sp.  pg.  barragana,  it.  baracane; engl,  huckram  [mit  Angleichung  an  buck, das  auch  im  Stotfnamen  bucJtskin  vor- liegt], barchant,  ndl.  barkan,  mhd.  bar- chät,  dtsch.  Barchent,  Berkan;  russ. barham  'Samt',  barakun,  barkan  'Bar- chent'; klr.  barchat  'Samt',  barakan 'Art  Wollstoff';  poln.  barakan,  poln. cech.  barchan  'Barchent'.  [Dozy  Oost  24. DE  237.  ML  941.  Kluge  38.  Gorja- jew  12.  Bern  SlETWb  44.  Lammens Rem  55/56.
773:257.  Ar.  barük: [Vom   Vb.   baraka    'sejrnen':  vulgär:] 'Geschenk';  hieraus  mit  dem  ar.  Art.  sp. alboroc,  alboroque  'Maklergebühr,  Trink- geld' [Dicc  Gast  107  a].    [DE  73/74.
2016:[Aus  aram.  liärü^ä  <[  assyr.  harühu,  vgl. ZAkkFW  55]  'Johaimisbrot,  Ceratonia siliqua' ;  hieraus  lat.  caruba,  cartimba, gr.  xapoüßa,  it.  carruba  'Johannisbrot', carrubo  'J.-Baum',  frz.  carotibe,  carouge, prov.  garrova,  sp.  garroba(o),  algarro- ba(o),  pg.  alfarroba  'Johannisbrot',  al- farrobeiro  'J.-Baum';  sp.  algarrobilla, pg.  algarroba  'eine  Erbsenart,  Ervum monanthos';  engl,  carob,  dtsch.  Karöbe, Karube  'Johannisbrot'.  [DE  121.  Egui- laz  178.  RomForsch  IV,  355.  ML  1864 und  4680  (gehören  natürlich  zu  einer Nummer  zusammen).
2936:Vb.  karuba  'nahe  sein'],  im  Dial.  von Algerien  kurbi  y  gurbi  [vgl.  güm  <^ kaum,  hier  Nr.  747] ;  hieraus  frz.  gourbi, (/ojtrö/rHütte,  Zeltdort',  scherzhaft 'Woh- nung' [wie  etwa  im  Dtsch.  das  india- nische Wort  Wigwam  benutzt  wird]. [Devic  DEt  132.
4812:'Kahn  der  Sonne  oder  des  Sonnengottes Ra',  auch  barl;  nach  Herodot  II,  96 nicht  nur  der  hlg.  Kahn,  aut  dem  der Gott  der  Sonne  über  den  Himmel  fährt, sondern  jedes  große  ägyptische  Schiff: gr.  ßäpi?,  lat.  barca ;  hieraus  zur  Bezeich- nung eines  gewöhnlich  dreimastigen Seglers  it.  barca,  sp.  pg.  barca,  Irz.  bar- que;  engl,  barque;  dtsch.  Barke.  Aus it.  barcarolo  'Barkenfülirer'  wurde  it. harcaruola  'einfaches  Lied',  engl,  bar- carolle,  dtsch.  Barkarole.  In  Anlehnung an  engl,  brigantine  'Piratenschiff  [<;  frz. brigand,  it.  brigante]  wurde  engl,  bar- quantine  'der  Barke  ähnliches  Segelschiff' gebildet.  —  [Abltg.  aus  nordischem  börkr 'Boi  ke'  scheint  unberechtigt  trotz  nord. barkr  'Schiff'.]
5119:baraka  222
5285:A;«^«?'«  1002 ka'fihn  1002 ÄrrtÄA-rt/ur  1003 kahwa  1005 k'i^  1006 A;«*/*  1007.  1173 kail  1 174  a kä^iininnkäm  1010 katsänia  1011 kaitus  273 Ä-«)i;ö(i  lol3 käkang  1016 ter«  1021 kala'a  1036 kalaba  1376 kalada  1505 fcatofa  1022 Ä-aZ«w  1023 Ä:ffZ6  1025 A-a/ö  1026 teZ»  1029 k^/ö  1030 Ä;fl?«»iffl  1032 A;a?tö'  1036 A-aWfli  1037 A;rt>Hä  1157 käma  1010.  1999 if«H!7  1044 kammün  1046 kand(l)  10.52 kandara  1051 kandil  1053 kantara  1057.  1506 kanz(lja)  1059 Ä;ar«  1181.  1507 A;ßm  1071.  1072 A-ar'^a  689 kaya'a  1250 karam  1083 karawän  1086 karawijä'  1087 kafija  1094 karlwija  1095 A;ar>«  1096 Ä-flrA-rti  1096  b Ä:a»-n  1098 karräza  1101 karsana  1 103 A-a;YSs  1104 karuba  1252 Ära's  1105 A-äsa  1174 kas^a  1106 iW&ff  1108.  1118 Ä-asa/'a  1109 kasama  1187 kasara  1575 Ä;as(i  1110 kasdlr  1111 Ä-ßs/r  1575 A-as/s  1114 fcasr  1117
5927:barquantine  2148
5929:barque  2148
6352:baragouin  256 I  barbacane  197 I  bardache  afz.  229 ]  barde(au)  228 i  ftarc^of  228 ,  baroque  364 I  barque  2148 i  barracan  250 I  basane(r)  afz.  316 ^  basane  316 I  basanier  316 !  basiUqtie  (vemej  262
7355:barakan  250
7642:(na)  balykti  208 baragola  145d barakan  250 haran  219 barasnik  258 barasznik  258 barchan  250 bastramy  261 ias^/(/Ä;  260 fcasa;-  278 *     bedew  164 b§dzwim  1332 benzoes  1332 bezestan  280 bezmian  272 biczak  311 hisurman  1516  a ^>o&a^•  181 bohatyr  IIb boraks  356 borsuk  254 borysz(nik)  258 bronz  1657 6mö/v/L-  337 bugaj  339 buhaj  339 bujurdan  346 butany  350 iM?a<  1672 bunczuczny  354 bunczuk  354 &MrÄ;a  221 burnus  365 bursztyn  1004 ftwara  376 buzdygan  333
```


## [2026-09-04T18:26:23.292Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- LKT 222 baraka ---\"; sed -n '715,730p' LKT.txt\necho \"--- LKT smaragd ctx ---\"; sed -n '4960,4985p' LKT.txt\necho \"--- LKT karuba 1252 ---\"; grep -n \"1252\\.\" LKT.txt | head"
}
```


### [2026-09-04T18:26:23.361Z] TOOL RESULT

```
--- LKT 222 baraka ---
220.  Syr.  Bar-abba:
N.  pr.  Nach  den  Evangelien  Mt  27  u. Mc  15  ein  jüdischer  Verbrecher,  den die  Juden  am  Passahfeste  an  Jesu  Stelle losbaten  [aus  syr.  bar  'Sohn'  und  abba 'Vater',  s.  hier  Nr.  1,  also  'Sohn  des Vaters';  dagegen  scheint  die  Deutung bar  rabbän  'Sohn  ihres  Herrn  oder  Leh- rers' kaum  wahrscheinlich];  gr.  Bapaß- ßa?,  lat.  Barabhas ;  hieraus  triest.  baraba 'Taugenichts',  genues.  barbau,  prov. barban,  barbau  'Schreckgespenst  für Kinder'.    [ML  940.
221.  Pers.  bärk:
'Blatt'  [Horn  NpEt  S.  47,  Nr.  203] ;  hier- aus über  die  kaukasischen  Sprachen russ.  burka  'runder,  kurzer  Filzmantel', wie  er  bei  den  Kosaken  und  Kaukasiern üblich  ist.    Poln.  burka.   [Gorjajew  34.
222.  Ar.  baraka:
'Segen  (nämlich  Gottes)',  ebenso  tk. bereket  'dass.,  Fruchtbarkeit';  hieraus rum.  berechet  'Fülle,  Fruchtbarkeit'; bulg.  bereket  'Überfluß',  serb.  bericet 'Glück,  Überfluß'.  [Sain  47.  Bern SlEtWb  49.
223.  Sskr.  baranda:
[Vielleicht  selbst  vom  pers.  bär-äniädä 'heraufgekommen,  d.  h.  mit  einem  Dach versehen'],  neuindisch  varanda  'ein  be- deckter, nach  vorne  offener  Vorraum, Altan';  hieraus  pg.  varanda,  sp.  baranda, harandilla,  kat.  barana,  frz.  veranda, it.  Veranda;  dtsch.  Veranda,  engl,  veran- dah  [jedoch  amerikanische  Schreibung Veranda  Herrigs  Archiv  CXLI.  195], schwed.  Veranda.  [Hobson-Jobson  964  u. 965.    ML  9151.
224.  Ar.  baras:
'Weißer  Aussatz,  Lepra';  hieraus  mit ar.  Art.  sp.  albarazo,  pg.  alvaraz  'dass.', frz.  albara,  albora.  [DE  65.  Devic DEt  6.    Lammens  Rem  5.
225.  Ar.  baras:
'Bunte  Flecken  bei  Pferden'  [daher  ar. abras  'Schecke'];  hieraus  sp.  barajado, pg.  baralho  'bunt'  und  als  Verb  sp.
2*
Ar.  barTil.]
20
barajar,  pp.  baralhar  'misilieir,  woraus schließlich  sp.  baraja,  pg.baralha  'Spiel', vielleicht  auch  it.  sbaraiß/o  'Zerspreu- guiig\  Vb.  sbaragliare  sowie  sbaraglino 'Pufispier.
--- LKT smaragd ctx ---
ven,  nennt;  es  sind  gewisse  Regimenter leichter  Infanterie  in  einer  tast  ganz orientalischen  Uniform,  die  ursprünglich aus  eingeborenen  Algeriern  rekrutiert wurden,  heutzutage  aber  nur  noch  aus Franzosen  bestehen.  [Devic  DEt  230. Eguilaz  5:!1.
2226.  Ar.  zuS)b:
'Männliches  Glind';  hieraus  siz.  zubbu 'dass.'.    [GrSVooiSic  251.
2227.  Ar.  zubja: 'Löwengrube;  tiefer  Graben  voller  Was- ser, um  Tiere  zu  fangen';  hieraus  siz. zübbiu  'Abgrund,   Graben'.  [GrSVoci Sic  251.
222S.  Ar.  zufaizaf: 'Brustbeere'  [wahrscheinlich  aus  gr.  ti- Zuqpov,  lat.  ziziphum] ;  hieraus  mit  ar. Art.  sp.  azilfaifa,  azofeifa,  pg.  agofeifa 'dass.'.    [DE  229.    Eguilaz  .323.
2229.  Ar.  znharl: 'Geomantiker'  [von  zuhra  'Planet  Ve- nus', welches  ar.  Wort  über  die  Form Azofra  hinüber  in  der  durch  den  Reim bedingten  Verunstaltung  Alligafir  auch in  Wolframs  Parzival,  Ausgabe  von Lachmann.  ^.  (1854),  782  Eingang  ge- funden hat,  vgl.  ZfdWf  VIH,  149];  hier- aus sp.  zaliori  'Wahrsager'.  [DE  361 u.  362.
2230.  Pers.  zulf:
'Haarlocke',  ebenso  tk.  zi'df  oder  mit Stützvokal  zülüf;  hieraus  rum.  zuluf 'Haarwickel,  Locke'.  —  „Die  Perser  ra- sieren sich  wie  alle  Muhammedaner  den Kopf.  Sie  lassen  jedoch  hinter  jedem Ohre  einen  Haarschopf  stehen,  der  lang herabhängt  und  das  Aussehen  der  alt- ägyptischen Kinderlocke  hat."  Brugsch, Reise  nach  Persien  I,  157.
2231.  Ar.  zulla:
'Sonnendach'  [von  zill  'Schatten'] :  hier- aus kat.  sp.  pg  told-o  'Zeltdach',  toldillo 'Sonnendach,  Markise'  [mit  eingescho- benem d  wie  in  sp.  humilde  <^  lat.  hti- milis].  [DE  351.  Eguilaz  507  (wo  als Grundwort  gr.  öö\o<;  angegeben  wird).
2232.  Ar.  zürn :
Vulg.  TrucIilsafV:  hieraus  sp.  zumo 'Saft'.  [ZfromPh  .\XX1V,  568.  Eguilaz 532  [mit  gr.  I\u)x6<;  als  Grundwort.]  ML 9632.
2233.  Pers.  zniniirud:
'Smaragd'  [vielleicht  aus  gr.  oiudtpaYboQ, wahrscheinlich  beides  aus  dem  Ind.], ebenso  tk.  ziimriid  [Kelekian  Kämüs 646  b];  hieraus  hu\^.  zumrtui,  russ.  izum- rud  'Smaragd'.  [Gorjnjew  122.  Mikl SlEtWb  404  b.    Bern  SlEtWb  441.
2234.  Ar.  zmära: 'Giraffe,  Cameloparilwlis  giraffa'  [sicher- lich selbst  ein  Fremdwort  und  wie  das
Ar.  zurziil.
174
Tier  aus  Zentralafrika  stainuiend];  hier- aus it.  i/iraffa,  Irz.  girafe,  kat.  sp.  pg. (firafa,  runi.  girafä;  engl.  ndl.  giraffe, dtsch.  Giraffe  [älteste  Belege  s.  ZfdWf Xi,  3041'.];  russ.  i»ro/'.  [ÜE  218.  Egui- laz  413.    ML  9602.
2235.  Ar.  /nrzäl: 'Drossel',   auch   zurzür   [KM  II,  839, Z.  G  V.  u.] ;  hieraus  sp.  pg.  zorzal  'dass.'. [DE  369.    Eguilaz  .531.    ML  9629.
176
Sach-  und  Namensverzeichnis.
'Abbäs  I.  4 'Äbbäs  Pascha  507 Äbutilon  14 Adamsapfel  19 Ädenia  venenata  20 Adhatoda  1161 Ägypten  1222 Ailantus  glandulosa  1141 ^Zc«Z(J  1021 Alcdntara  1057 .4Zei)^;o  792 Algarve  674 Alhambra  882 Aljarafe  (de  Sevilla)  1840 ^/fco/jo/  1227 Almagra  1349 Amber  78 Amocklaufen  71 Anakonda  74 Antiaris  toxicaria  2136 Antilope  saiga  1774 .4rafta  90 ^rec«  1 7 Argali  96
Arrecife  (Cördoba)  1704 ^4ssassmeM  839 ^<o«  132 '4«äö  133 Averroes  1084 ^OTcmna  579.  893. Bagdad  170 Bairam  183 Bakkam.  190 jBa/^is  203 Bartole  259 Baumwollpapier  1723 jBeÄen  176 Belsazar  1456  a Beriberi  291 £ete  sicula  1907
318.  2149 Boehmeria  nivea  1697 Bolgar  351 Bougie  340 Brindisi  1657 Brundisium  1657 Brunfels  1570 Bungalo  214
Bürän  358 ^Msa  376 Busbeck  544 Casuarina  1119 Casuarius  galeatus  1119 Cagatai  639 Ca/a  (Sizilien)  1036 Calamus  rotang  1724 Camelopardalis  giraffa
2234 Camphora  1100 Cannabis  indica  839 Carrfoib  397 Ceratonia  siliqua  1182 Cercopitheciis  1 422 «.  Chamisso  1623.  1882. Chavica  belle  2149 Chedive  876 C/*mrt  841 Cochenille  1219 Collocalia  esculenta  1844 Constantin  VI.  1388 Corchorus  capsularis  693 Crataegus  azarolus  2206  ' Cypraea  moneta  1 133 Daimio  1992 Dante  1305
--- LKT karuba 1252 ---
```


## [2026-09-04T18:26:24.105Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -c AFA.txt; head -c 1500 AFA.txt; echo; echo \"=== grep smar ===\"; grep -n -i \"smar\\|marakat\\|zumur\\|Blitz\" AFA.txt|head"
}
```


### [2026-09-04T18:26:24.173Z] TOOL RESULT

```
600115 AFA.txt
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
prcvcnt abuse by commercial parties, including placing lechnical restrictions on automated querying.
We also ask that you:
+ Make non-commercial use ofthefiles We designed Google Book Search for use by individuals, and we request that you use these files for
personal, non-commercial purposes.
+ Refrain fivm automated querying Do not send automated queries of any sort to Google's Sy
=== grep smar ===
```


## [2026-09-04T18:26:35.881Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA arabic zumurrud/barq/baraka ===\"; grep -n \"زمرد\\|برق\\|بركة\\|كروب\" AFA.txt | head -20\necho \"=== AFA latin-ish ===\"; grep -n -i \"brk\\|Smaragd\\|maragd\" AFA.txt | head -20\necho \"=== AFA sample body ===\"; awk 'BEGIN{RS=\"\\f\"} NR==60' AFA.txt | head -40"
}
```


### [2026-09-04T18:26:37.812Z] TOOL RESULT

```
=== AFA arabic zumurrud/barq/baraka ===
=== AFA latin-ish ===
5642:1) Vgl. meine Beitrige sur BrkL der mehrt Bild, im Arab. p. 1, S.
=== AFA sample body ===
29
dagegen ist syr. 1*^,1^ ^) zu [373 ^ zu stellea. (Hierher
wird gewöhnlich anch von den alten Lexicographen noch
7mU73 (^Irüch) gezogen ; diese Schreibung aber mit w
beweist deutlich, dass wir es hier nicht mit einem sonst
überhaupt nicht nachweisbaren ^xxkxTxpizv zu thun haben,
sondern dass in dieser Form nichts Anderes vorliegt, als
eine durch pü^3 vielleicht beeinäusste, im Übrigen aber
auch rein durch d:is Princip der Dissimilation zu erklärende
Umformung des Wortes praetorium Tpxtrxpis'j , das jedes
lateinische Lexicon schon in der Bedeutung »fürstliches
Gebjiude" keuut; vgl. ebenso n^»73 = ^•'•'•et/aW/w ^); "^p3^3
= Kffißtxxptc'j^); } '^ ' ' PSra. 1405 = 'jy jTj^ » umgekehrt
im Syrischen {flii^s ') für zxXxizxpiov ; Holländisch ta/ereel
.*• 9
aus tabidarium), Ueber das hierher gehurige <^*oly^ , das sich
auch im Maudiilschen findet , und dessen persischen Ursprung
vgl. schon Nöldeke Mand. Gramm, p. XXXI. Es findet
sich schon Div. Lebid 121, 11. — ^JL^ Dozy I. 219,
hat schon de Goeje Gl. geogr. 208 zu syr. pv^ gestellt.
Natürlich ist aber die arabische Form nicht direct aus JLa^,
sondern aus dervon diesem Worte gebildeten,in unseren Lexicis
noch fehlenden Diminutivform auf )iJ^<}*)i ^Va^ entstanden.
Wir haben noch einige Wörter zu erwähnen, die sehr
einfache, auf dem Felde errichtete Hütten bezeichnen und
fremder Herkunft zu sein scheinen. Da ist zunächst zu
nennen ^.j »eine kleine Hütte**; es könnte identisch sein
iiüt l^^s^, als dessen Aequivalent es schon B6. bei PSm.
1) PSm. 533; ich halte diese Form für die artprünglichere gegenüher
P ^ ^ PSm. 612, da sie durch das Jüd. armm. gesichert ist.
2) Vgl. Lery TWB. I, 9G; es trird ron Arbeiten in Haotrelief gebnneht.
3> Schon Mossatiia bei ^Arüch.
4) Perles Eiymol. S(iid. p. 6. Anm.
5) «Arüch 8. T. nn^p IL
6) Nöldeke Syr. Grammatik ) 131.
```


## [2026-09-04T18:26:38.082Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM (Addi Shir) zumurrud ===\"; grep -n \"زمرد\\|الزمرد\\|برق\\|كروبي\" AFM_pages.txt | head -20\necho \"=== TAD ===\"; grep -n \"زمرد\\|كروب\\|بركة\\|برق\" TAD_pages.txt | head -20\necho \"=== ARB ===\"; grep -n \"زمرد\\|كروب\\|الزمرد\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -20"
}
```


### [2026-09-04T18:26:38.187Z] TOOL RESULT

```
=== AFM (Addi Shir) zumurrud ===
510:ܕ ܐ تعريب برشامه وهو البرقع
837:و( المَيرَقدَار) 0 من برق ومن دار اي حامل النيرق
2487:كان اطول من اسان 1 بإربعة اسمار وكات كبرق كه إلى سكن يلد الروم ٠‏
3302:ܝܢ ܘ و 0 اميا ا مشجيع ٠‏ .1 ابرق 50 10700
=== TAD ===
192:                                     ‫استبرق ‪ -‬فارسي معناه الديباج الغديظ‬
604:  ‫تق من برق أي لمم فنقل من العربية الى اللاتينية وبناا »«ة؟وط‬
1273:          ‫تزرَجد‪ -‬في الفارسية ‪ 9‬زبرجد » وهو حجر يم بشبه الزمرد‬
1997:                                                                              ‫حوض وبركة وقبوة‬
2403:‫واروسميهة وكروبين وشارويين ‪ -‬فاىلعيرانية « كووب ‪3‬‬                        ‫‪1‬‬
2658:    ‫مكروب ‪ -‬وثانى منحوت من "‪ 804116‬أي صغير و ‪ 5101015‬أي جى وهو‬
=== ARB ===
ARB_mo3rb.txt:13050:الوزن فى ضبط « زمردة » يكسر الزاى ٠‏ ثم إنبسا ضبطت اقم فى شرح التير يزى بفتح العين وسكون
```


## [2026-09-04T18:26:44.481Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- TAD 595-615 ---\"; sed -n '595,615p' TAD_pages.txt\necho \"--- TAD 2395,2410 ---\"; sed -n '2395,2412p' TAD_pages.txt\necho \"--- TAD 1268,1280 ---\"; sed -n '1268,1280p' TAD_pages.txt\necho \"--- TAD grep zumurrud ---\"; grep -n \"الزمرد\\|زمرذ\\|زمرّد\" TAD_pages.txt|head"
}
```


### [2026-09-04T18:26:44.561Z] TOOL RESULT

```
--- TAD 595-615 ---
                     ‫كهأاعما‬
                           ‫الدراءمويرادبهفي زماننامجلس التجاريجري في‬
                                                      ‫اولرابتحجار السفنالخ‬
 ‫وتقة وودقة ودوطة وبوانة ‏ فارسي ‪ 2‬لوده » وهو وعاء يديب الصائغ‬



             ‫وق ‪ -‬لاتيني ودأءعمط مرادفه الصور والناقور والتقير تفخ فيها‬

  ‫تق من برق أي لمم فنقل من العربية الى اللاتينية وبناا »«ة؟وط‬
         ‫‪5‬‬       ‫‪03‬‬       ‫‪5‬‬             ‫‪0‬‬      ‫‪ 59‬ع‬   ‫‪-‬‬     ‫‪75‬‬       ‫ع‬

                                                            ‫مرقش‪-‬‬
                                                                ‫بو‬
 ‫الحامض البورفي والنطرون منهطبيعي‬   ‫والىالفارسية « بوره ‪ 6‬وهو ملح حاصل من‬


  ‫وقد بوجدعلىضفاف الامبر في فارص وتيبت وكاليفورنيا ومنه ما حصل باعمال‬
 ‫النطرون فدعي كذ! هن وادي النطرون في‬
                                   ‫كياوية وهو خلاف اللطرون ‪ .‬أم ا‬

--- TAD 2395,2410 ---
                              ‫فلارامية «كرفسا »( بات)‬
                                                    ‫كرفس ا‬
                               ‫نات )‬          ‫الآراية ناه‬            ‫"كر حاف‬
      ‫ايطالى فوعامج رونو معناة اونشوك نومامرادقه الجر الصحي‬                ‫ال‬

‫كرنيتة ‪7‬س ايطالى هااءد‪.‬ده معناه قرن صغير وهو بوق تحيف ينفخ فيْه‬
                                                                            ‫كازمارة‬

‫واروسميهة وكروبين وشارويين ‪ -‬فاىلعيرانية « كووب ‪3‬‬                        ‫‪1‬‬

‫كع » وثم بمثلون الملاتكة الغير المنظورين الا ان صورتهم الحسوسة انما هي‬
‫‪ 85:91‬حزقيال ‪١٠:١١‬‏ الك‬              ‫ور دو أربعة أجدحة تكوين م ‪:‬خ‪4‬روج‬
 ‫أصل هذا اللفظ أشوري ومعناه حارس لان سكان شنعار فىبكابالنوا يصورون‬
                 ‫حفراً فى جدران الدور ثورا ذا أجنحة ايحرس الانواب والمداخل‬
                         ‫سب ايطالى ‪822‬ه‪ ©223‬معناه عربة وعجلة‬                 ‫>‬

 ‫كرون سديوناق وها زعو نات ووو عر عداو ا قل انيما‬
‫الكرويا نبات معروف يشبه أغصانه وورقه بالرجلة‪.‬الا ان لون أغصانه وورقه الى‬
--- TAD 1268,1280 ---

 ‫زئبق وبق وزاووق ”‪ 2‬س فارسي « زيوه » وهو سال معدلى لياله‬
                                                     ‫بالزجاج‬
‫زاروب سعامي ‪ -‬ارام ‪ 7‬زريبا » معناه ضددق مرادفه لقب والأزم‬

          ‫تزرَجد‪ -‬في الفارسية ‪ 9‬زبرجد » وهو حجر يم بشبه الزمرد‬
                                   ‫سرسي « زبان » معناه لسان‬
                                                          ‫زيان فا‬
                         ‫ون ‪ -‬فارسي « زون ‪ 4‬معناه ضعيف أبله‬
    ‫ون ‪ -‬لفظة أراميةمشتقةمن« زكن ‪ 6‬أي اشترى مرادفه المشتري‬
            ‫اب أى ماء‬
                    ‫»ى ذوهب‬
                          ‫ابر‪-‬سي مركب من « زر أ‬
--- TAD grep zumurrud ---
1273:          ‫تزرَجد‪ -‬في الفارسية ‪ 9‬زبرجد » وهو حجر يم بشبه الزمرد‬
```


## [2026-09-04T18:26:45.995Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- ARB mo3rb ctx ---\"; sed -n '13035,13060p' ARB_mo3rb.txt\necho \"--- ARB abdulraheem zumurrud ---\"; grep -n \"زمرد\\|الزمرذ\" ARB_abdulraheem.txt|head"
}
```


### [2026-09-04T18:26:46.064Z] TOOL RESULT

```
--- ARB mo3rb ctx ---

69 بكس الحاء المهملة » ودو القصير الدييم ٠‏ رقى ح خ باللاء المعجمة » وهو غطأ ٠‏ 

(4) بكس القاف »6 وقها لفات أخر . وفسرت ف المعاجم بأنه يقال « مالفلان قرطعية » أى : 
اله قليل ولا كثر ٠‏ ( أنظر المهرة ع : ه ٠‏ 5 ) وغيرها ٠‏ ولكن التير يزى ذ5 الكدة بلفظ « قرطعب » 
وقسرها بأنا « داية » رأظن أنه خطأ منه ٠‏ 

(5) بفتم اتقاء المعجمة » وضيط فى ب يكمرها » وهو خطأ ٠‏ 

(0 فى ح » 6 «الإزاى ٠.»‏ 

() فى ” «وكون »ه 

(0) ضبطت ق< » ب بفتح العين وتشّد يد اللام وسكون الكاق ٠‏ ودو القلاهى أيضا هن سياق 
المؤاف وشيخه ٠‏ ولكن الذى فى 0 بكسر العبن فقط » وكذلك صنم صاحب اللسان » إذ 1 هذا 
الوزن فى ضبط « زمردة » يكسر الزاى ٠‏ ثم إنبسا ضبطت اقم فى شرح التير يزى بفتح العين وسكون 


اللام رفت اللكاف ومشديد الدالع 5 مطبعى واضم . 


6 قْ مس « ويكسر الم » 0 




--- ARB abdulraheem zumurrud ---
```


## [2026-09-04T18:27:06.610Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt; do\necho \"########## $f\"\necho \"--cherub--\"; grep -n -i \"cherub\" $f | head -5\necho \"--griffin--\"; grep -n -i \"griffin\\|gryphon\\|gryphus\" $f | head -5\necho \"--emerald--\"; grep -n -i \"emerald\\|smaragd\" $f | head -6\ndone"
}
```


### [2026-09-04T18:27:08.560Z] TOOL RESULT

```
########## FSD_vol1.txt
--cherub--
15003:eonvE)  —   Ant.:  penalty,  punishment,  retaliation,  retrlbu-  —   am  o-ri  no,  n.  1-ni,  pi.]  [It.]  A   cupld:  a   little  love- tlon  venceance  -   Prep  :   an  amnesty  to  all  the  Insurgents  god:  a   cherubic  child:  used  as  a   figure  In  decorative  art. for  all  oflenses  a-mo'ra,  n.  Singular  ot  fMOr.MV. .
16581:to  8   feet  long,  of  temperate  Eeas,  with  very  large  wlng-llko pectoral  fins  encroaching  forward  and  reminding  one  of  an Imaginary  cherub,  monk'-  • fish"*;  fld'dIe*fisb"L  2.
16603:Seraphim.  Cherubim. Thrones;  Dominations. Principalities,  ka-  ?SiS|Vi-ra  „   t   a
64009:or  characteristic  of  a   cherub:  angelic;  as.  cherubic  Innocence-
64326:&   Poet.  The  representation  of  a   beautiful  winged  child, or  the  winged  head  of  a   child,  the  accepted  type  of  the angelic  cherub;  any  beautiful  angel.  In  this  sense  the plural  is  always  cherubs.
--griffin--
2249:Grlf.  A   Co..  .C.  Griffin  A   Co.
24852:the  griffins;  hence,  in  Greek  art.  a   figure  in  Oriental  dress,  Ar"ls-tlp'pus,  1   ar  is-tip  ns  2   ar  is-up  ib.  n.  a   Greek lighting  with  a   griffin,  occurring  on  some  vases,  etc.  [<  L.  philosopher  t425r-36TC  B   C.t .   founder  oi  tne  Gyrcnaic
57911:carl'Isb,  1   korl'i&h;  2   cSrl'lsh,  a.  Churlish;  boorish;  rude. Car-lisle',  1   kar-lall' ;   2   car-ill',  n.  1.  Earls  of,  see  Howard. 2.  John  Griffin  (Vsl835-»/il910),  an  American  statesman; Speaker  of  U.  S.  House  of  Representatives,  18S3;  Secretary of  the  Treasury  under  President  Cleveland,  1893.  3.  A
71465:Obverse:  Head  of  Pallas,  wearing  a   crested  Athenian  27.  Egyptian  Octadrachm. helmet,  on  which  is  Scylla,  with  dogs’  heads  Bpringing  Gold;  429  grains  285-247  B   C from  her  waist;  , on  the  neck-piece,  n   griffin.  Obverse:  Head  of  Arsinoe  II.,  sister  and  second  wife  of
76263:con'dor,  1   ken’der;  2   c6n'd5r,  n.  1.  A   very  large  South* American  cathartoid  vulture  (Sarcorhamphus gryphus),  dwelling  principally  in  the  high Andes,  about  3   feet  long,  and  with  a   wing^ex- panse  of  sometimes  9   feet.
--emerald--
13192:A'Ium*IJagh,  l   u'lum-bag;  2   a'lfim-bag,  rz.  A   fort  near Lucknow,  India;  captured  by  the  British,  1857-1858. A"lum-bra'do,  1   S’lum-bra'do;  2   alum-brS'da,  n.  [Sp.J Ch.  Hist.  One  of  a   Spanish  sect  of  the  I6th  century.  Sea Illuminati.  A"Iom-bra'dot. a-lu'men,  I   a-lifl'men;  2   a-lfl'mgn,  n.  [L.]  Pharm.  Alum, al'um *feath"er,  7z.  See  iron  alum,  under  alum. a-lli'inl-an,  1   a-liO'mi-an;  2   a-lfi'mi-an,  n.  Mineral.  A white  aluminum  sulfate  (AIiSjOs). a-Iu'mi-na,  I   a-Iiu'mi-na;  2   a-lu'mi-na,  n.  Chem • Aluminum  oxid  (AhOs).  Alumina  Is  the  most  abundant of  all  the  earths,  and,  being  a   common  constituent  of  the silicate  minerals,  forms  the  basis  of  many  rocks  and  soils. In  its  amorphous  form  It  is  a   soft  white  insoluble  powder. When  crystallized  it  is  intensely  hard,  and  It  Is  found  nearly pure  as  sapphire  (ruby,  topaz,  emerald,  etc.),  corundum, and  emery-  (<  L.  alumen,  alum.J  al'u-mlnj;  al'u- mlnef.—  alumina  cream,  a   precipitate  of  aluminum  hy- drate. suspended  In  water  when  fresh.—  a-lu'ml-nate,  vt. I-nat*ed;  -natTng.)  To  combine  or  saturate  with  a   salt of  aluminum  (as  alum),  as  in  the  treatment  of  paper  with alum-water  to  prevent  the  Ink  from  running  when  engrav- ings are  printed.--  a-lu'ml-nate,  n.  Chem.  A   salt  formed from  alumlnic  hydrate  (Ah(HO)e)  by  substituting  a   metal for  the  hydrogen.
40560:ber'yl,  1   bcr'il;  2   bSr'vI,  n.  1.  Mineral.  A   vitreous to  rerinous,  green  or  emerald-green,  light-blue,  j'ellow, pink,  orw-hite  glucinum  aluminum  silicate  (GhAl-SieOis) that  crystallizes  in  the  hexagonal  system.  When  trans-
40567:Siberia,  Brazil,  Ceylon,  and  the  United  States, marine  and  emerald  are  gera  varieties.  See  table  under stone.
42589:—   a   fancy  derived  from  the  fact  that  the  first  skins  sent  to Europe  had  been  deprived  of  feet.  The  great  emerald bird  of  paradise  (Paradisca  apoda )   has  a   dense  erectile  tuft of  golden-orange  plumes  about  2   feet  long  growing  from  un- der the  shoulder,  and  elongated  wlre-llke  central  tail-feath- ers. The  lesser  emerald  (P.  minor )   furnishes  most  of  the paradise-plumes  used  for  ornamenting  ladles’  head-dresses. The  red  (P.  sangulnea)  nnd  the  king  (Clncinnurus  regius ) are  other  species.  The  twelve  .wired  ( Seleucides  nigra )   Is long-billed  or  eplmachtnc.
42730:Emerald  
42763:Emerald. . .   .
########## FSD_vol2.txt
--cherub--
45446:,   Dionysius,  one  of  those  emanations  from  the  Divine wliich  the  cabala  calls  Sephiroth;  a   function  or  dis- tinction. They  are  angels,  archangels,  princedoms,  powers, virtues,  dominions,  thrones,  cherubim,  and  seraphim,  the last  order  being  nearest  the  Trinity.
51242:Thy  timorouB  vales  responsively  would  hymn Like  swect-lipRcd  Cherubim.
72642:■"  re  read  of  imaeos  of  cherubim  in  tho  Old  Toafamant,  as  wo
--griffin--
37048:griffJ,  1   grif:S  grli.  K.  Textile.  A   SDriea  of  hortzontal  bars,  in a   reciprocating  frame,  to  raise  and  lovfor  the  shedding mechanism  of 'a  .Tactiuard  loom  in  forming  the  pattern. { <   F.  eriffe;  see  grifpe^.] grifl-’,  n.  Same  as  griffin.  4. gri  ffs  n.  [Local.  Eng.]  A   steep,  roolcy  glen, griffs,  [So.  IT.  S.l  A   dark  reddlsh»brown  mulatto:  also, according  to  some  authorities,  a   penson  of  mixed  Indian  and negro  blood,  or  the  o£fS[)rinp  of  anegroandamulattress.  [   < S’,  uri/rc;  ep.  GRiPFiN.l  griffeit.
37054:5.  (1)  Agriffin'Viilture.  (2)  The  lammergeier.  6.  [Eng.] A   variety  of  apple.  [   <   P.  orijfon,  <   EL.  wiffo{n-),  < pryphus,  <   L.  gryps,  fabulous  creature,  <   Gr.  erj/ps,  < grypos,  hookeci.l  grlf'fonf;  grlf'fount.—  bearded  grif- fin, the  lammergeier.— griPfinsinale",  n.  Her.  A   wingless griianwltu  largeears.— griffin’s  foot,a  surgical  instrument: so  called  from  its  shape.— g.»vulture,  n.  An  Old  World vulture  ((Jyps/nlt'us).— grlt'fln-age,  B.  [Anglo*lnd.]  The condition  of  a   newcomer:  greenness.— grlFfln-esque',  a. grlPfin-lsh,  a.  1.  Vigilant  like  a   grlftln.  2.  [Anglodnd.J Haw  and  inexperienced,  like  a   grlffln.  grlf'fisht.—  grlf'fin-
37055:l.sra, ».  1.  Vlgllanoe,  like  that  of  the  griffin.  2.  Grlfflnage. Grlf'flna,  n.  1.  See  GBipmH.  2.  Gerald  (>»/i3I803-Vij 1840).  an  Irish  novelist  and  poet.  3.  A   city:  county*seat at  Spalding  county,  Ga.
37212:grlptb  «.  A   griffin  or  vulture.
37833:gru'nau-ite,  1   grfl'nau-ait;  2   ^u'nou-It,  n.  Mineral.  An  Im-  oyster,  or  o.strcoid  bivalve  (genus  Grpphiea),  having  a   shell  !t"®Ol,?s.  them.  A.  colorless  fluid  compound  (CrHtOz) pure  variety  of  polyUymlte  containing  blsmuthlnlte,  ehal-  of  uneoual  valves,  the  larger  with  a   curved  umbo.  [<  LL.  obtaineu  by  (listUiing  guaiacum  and  found  in  wood*tar copyrlte,  and  galena.  [<  Griinaw.  Germany.]  ffryphu,?,- see  griffin.!— gryph'ltc,  n.  creosote;  the  methyl  ether  of  pjTocatocWn.  {<  guaiacum
--emerald--
2247:An  Irish  poet:  originator  of  the  phrase  the  Emerald  Isle, Dren'te,  l   dren'ta:  2   drfin'te,  n.  A   province  in  the  Nether- lands; 1,030  SQ.  m.;  capital,  Assen. drep'a-ni”,  1   drep'a-ni-;  2   drep'a-ni-.  Derived  from Greek  drepanS,  sickle  ( <   drepo,  pluck) :   a   combining  form.— Bre-pan'l-dset,  ».  pi.  Ich.  A   f.-imily  of  scombroldean  fishes, having  a   compressed  body,  scales  extending  on  the  vertical fins,  the  dorsal  with  a   short  spinous  portion,  and  slelde* shaped  pectorals.  Drep'a-ne,  tf.  (t.  g.)  — drep'a»nid>,n,— drep'a-noid,  a.-  Dre-pan'l-dses,  n.  pi.  Entom.  A   family of  small  moths,  the  hook»tlps,  characterized  by  having  the tips  of  the  fore-wings  somewhat  recurved.—  drep'a-nld^,  a. &   n.~  Drep"a-nld'i-di!e,  n.  pi.  Ornith.  A   family  of  passer- ine birds  with  nine  primaries  and  long  tubular  brush  tongue, lEcmding  many  Hawaiian  birds.  Drep'a-nls,  ?i.  <t.  g.)— dre-pan'I-dld,  a.  &n.~  Drep"a-ni-di'n»,  n.pl.  The  Drep- anldidse  as  a   subfamily.—  dre-pan'l-dinfes,  a.  &   n.—  drep'- a-n!n(eR,  a.— drep"a-nldT-«iii,«.  [-i-a,  pi.]  Protoz.  The sickle-sshaped  young  of  certain  gregarlnes.  as  coecidlideans.— drep'a-nl-form,  a.  Sickle-shaped;  falciform.— dre-pa'nl- um,  n.  [-NI-A,  pi.]  Bat.  A   sickle-shaped  cymose  inflorescence. Brc-pa'num,  n.  An  ancient  town  in  Sicily.  See  Thapani. Dres'den,  1   drez'den  or  (G.)  drez'den;  2   drgg'dSn  or  (G.) dr«-g'd6n,  «.  1.  .4.  circle  in  Saxoriy  kingdom,
4926:Ec'lo-ga  I.e'gnm,  1   ek'lo-ga  li'gom;  3   6e'lo-2a  le'gum.  iL.] The  Isaurian  laws.  See  under  law. ee'lo-ge,  1   eh'lo-]l :   3   ee'Io-g?,  ti.  iihctoric.  The  .selection, description,  or  narration  of  .such  details  a.s  are  calculated  to make  the  greatest  impression.  [   <   Gr.  eldogi ;   see  ECLOGtiE.l ■«c'lo-gite,  lek'lo-jait;  Sec'lo-git,  n.  Petrol.  A   rock  consisting of  red  garnet,  omphacite,  and  emerald-green  smaragdlte. [<  Gr.  eUogos,  picked  out,  <   ei,  out,  +   logo,  choose.] ec'lcg®,  1   l   ek'lo.g;  2   ec’log,  7i.  i.  A   iioeia  containing •ec'logue, )   discourses  or  dialogs,  with  shepherds  as principal  speakers;  as,  the  Eclogues  of  Vergil,  2.  A short  poem  upon  rural  life  and  scenes;  pastoral  poem; bucolic.
7601:ihc  wife  of  Cuciadr.ln. cni'cr-ald,  1   ein'sr-eld;  2   fin'er-ald.  n.  1.  Of,  pertain- ing to,  or  like  the  emerald,  c   pi'cinliy  in  eo!  ir:  hence,  of a   rich  and  vivid  green  color.  2.  Printed  with  or  desig- nating the  f   j-pe  called  eniernli!;  as,  an  cm/  rnbl  edition.— emerald  eoppor,  same  as  mi  u'-r  tsr .   -   em'i'r-ald  dish",  n. .1  goby  if7oblr,iif}!-js  oecar.iat.'.'t  of  tii';-  IVts!,  Iralifs  ;ind  Gulf of  Mexico,  leaving  the  b.ase  of  the  tongue  eWnliig  with  re- llecSlons  iiiic  it  gem.— e.  green.  1.  A   lirilHant  .wt  on  ra-cm- f/ilng  the  emc!  ud.  fi/'i'  cui  i   v,  71.  2,  A   jdguie.it  m.tiie  of Paris  grtsm.-  B.  Isle,  Ireliintl;  so  f-a!U'ii  t,y  WiJliitm DrenriiUi,  17ril-l,S2il, In  liii  poem  B'in)  bocam.e  nf  the  rlcts- nuHsof  Its  vonliirc.-  e.mioth,  n.  A   moth  of  t hf' genus //iy- parchim.—  e.  niche!  (Mineral.),  same  as  z.aba'J'itb.— e. spmlnntene,  .s:
7607:hardnes.s,  T.,3  to  7.8;  sp.  gr.  2.7,  iie.ariy.  Emeraifls  are found  in  Viiriim.s  p.art3  of  the  world,  including  ligyrit. Plberla,  and  North  Carolina.  The  moat,  beautlfui,  tiio  not the  largest,  emeralds  come  from  Colombia.
7610:An  emerald  of  light.
7613:They  traded  for  thy  wares  with  emerald*.
########## FSD_vol3.txt
--cherub--
5100:glory, surrounded by the cherubim and the symhola of
--griffin--
--emerald--
8908:oarbonlte — niaQ''ga-no'slte, n A vitreous emerald-
44977:emerald to blutsh«grocn, transluc cut, hydrated, ha^ii (upper*
55230:m. •of •emerald, n Prose nnc«i tiellavod to bo the mother
55231:ruck of emerald - M. of Qod, a title given t<o the Virgin
144421:emerald, and peacock-bluo tints. Reeves's Pheas- wL
226290:ruby, emerald, gurnof , ugute, rubcdllie, cllamoiid - ri*-gard'*>
########## FSD_vol4.txt
--cherub--
7292:the  cherubim  in  the  celestial  hierarchy,  and  ha■v^ng  six wings,  represented  in  Isaiah  as  beside  the  throne  of God,  praising  him  and  active  in  his  service  Jsaxah
7293:VI,  1-^  2.  In  art  and  poetry,  one  of  the  highest  orders of  angels,  excelling  in  wisdom,  might,  swiftness  of  move- ment and  action,  and  zeal  in  the  service  of  God  3. Her  Same  as  cherub,  1   [<  Heb  seraphim,  <
11845:two  cherubs  below  looking  up  (Bulgaria  Sls'tovt.  chicflj  in  the  past  participle
--griffin--
6004:■4.  Biol  (1)  One  of  the  serial  divisions  of  an  animal,  appUed  usuaUy  to  a   griffin  [Perhaps  «   surgest )
15724:chine  — rotary  spader,  a   digging-machine  having  a   large  5   A   county  In  W   Georgia,  203  sq  m   county-seat,  Griffin
20326:A   diplomatic  ataff  for  the  Last  should  be  trained  in  the  Eait L   Griffin  m   Nxneleenth  Century  Nov  ,   1893,  p   6S3.
49956:The  wings  are  very  long  and  strong,  giving  great  powers of  flight  The  turkey*buzzard  iCatharles  aura)  (see  Ulus under  turkey-buzzard),  the  carrion-crow  or  black  vul- ture iCatharista  atrata),  the  klug^T.  {Sarcorhamphus papa),  the  California  v.  {Pseudogryphus  calif ornianus) , and  the  condor  {Sarcorhamphus  gryphus)  (see  Ulus  imder CONTIOR)  are  examples  Both  the  Old  World  vultures  and the  American  find  their  prey  bj  sight  [   <   F   oautour,  < L   xiuUuT,<vuhus,pp  of  rri/o.tearl  — vul'ture'hock",n  In fancy  poultry,  an  undesirable  growth  of  straight  stiff feathers  on  the  back  of  the  thighs  — v.»raven,  n   An African  cor\lne  bird  (genus  CotvxiUut)
49975:The  crested  black Arabian  vulture  iVultur vwnachus),  the  griffin  or  ful- vous V,  (Gvpj /«!««), the  Nu- bian created  v.  lOtogypsauri- cularls) ,   and  the  small  Egyp- tian V.  or  Pharaoh’s  chicken (Neophron  perenopterus). sometimes  called  the  wbite V.  or  wbJte  crow,  which  to  v-,„-  viutnrp  i about  two  feet  high,  and  to  a   ^   King  Vulture  Vn typical  scavenger,  are  found
--emerald--
2420:Sap-phl'ra,  1   sa-fal'ro,  2   eA-fl'ra,  n   Bib  The  wife  of Ananias  She  fell  dead  after  lying  to  Peter  Acts  \ ,   1 sap'pbirc, )   1   saf'ojr,  2   sif'Ir,  n   1,  Mineral  Any  ono saf'Jlre**,  j   of  the  hard,  transparent,  colored  varieties  of corundum  which  when  cut  are  used  as  gems  usually and  specifically ,   the  blue  \   arlct  j   The  yellow  stone  Is  known, ns  Oriental  topaz,  and  the  green  x   arlet j   as  Oriental  emerald In  the  Authorized  Version  the  word  translates  the  Hebrew sappir,  a   stone  In  the  breastplate  of  the  high  priest
3912:schroet'ter-lte,  1   ^rOt'sr-alt,  2   shrflt'er-It,  n   Mineral  A pale  emerald  to  leek-green,  gum-like,  hydrous  aluminum silicate  (HeoAluSUOto).  found  as  an  Incrustation  l<
13310:emerald  f<or  smara^de,  <   L   see  smaraq-  Wild,  fast  gay-smasli'Jng»ma-cIilDc",  n   A   press  for
13313:a   Of  thecolorof  thesmaragd  cmorald-colorcd,  green  smash'»up",  1   sma^li'-up',  2   smllsh'-Op*,  n   (Colloq]  A The  Ileavenb  1   arthAfftofoadine  smash,  especially,  a   dcstnictlve  collision  Oh  a   railway
13315:(<  L   smaragdinus,  <   smaragdus  (<  Gr  smaragdos),  taste  hav’e  a   taste  of  smack
13316:smaragd  smatcli*,  n   [Dial  or  Obs  ]   1   Taste,  tincture  smack  2.
########## WEB_vol1.txt
--cherub--
31959:cher’ry lau’rel, an e laurc-cerasus, of thie fasion shrub, Pr ive of Asia Minor. y Rosáceas cher’ry pep’pér, a speci * mali, cherry-shaped peat capsicum, having cher’ry pit, 1. the seed of 2. achild’s game played wines cher’ry stone, 1. the seed of the he Stones, _2. a small quahog, a variety of 7 í chér’s6-nése, n. [Gr. chersonésos: chan; land, and 2ésos, an island.) a } va RE Gl tract of land nearly surrounded by poula; a chent, n. Pa ceart, a stone.] y waver . a _dull-colored, flintlik tonnid in poe flintlike quartz often . any of certain similar r hydrated silica and containing imu of chert’y, a.; comp, chertier; superl. ch a like chert; full of chert; flinty. ` Suar cher’ub, .; pl. cher’ubș or, for 1, 2, 3, cher’. u-bim, also, in the Vulgate, chera bi : Tite. cherub; O2 keritb, a cherub.] ae . a winged heavenl i i i Bezel. i. 5-11. apane desc
31961:3. a representation of one of the cherubim as a winged angel clothed in red, as in early art, or a chubby, rosy-faced child with wings, as in later art.
31964:che-ru/bic, che-ru/bic-4l, a. 1. pertaining to or resembling cherubs; angelic.
31967:che-ru’bic-Al-ly, adv. in a cherubic manner; angelically.
31968:cher’/u-bim, n. alternative paral and, former- ly, alternative singular of cherub (in senses
--griffin--
39965:‘con/dbr, n. [Sp., from Peruv. cuntur, condor.} 1. a large vulture, Sarcorhamphus gryphus, found in the most elevated parts of the South American Andes, with black plumage, bare head and neck, and a ruff of downy white feathers
65669:ep/i-ld-guize (-giz), v.t. and v.i. to epilogize. Obs. : Ep’i-ma-chi’nae, n.pl. [L., from Gr. epimachos, assailable, easy to attack; epi, on, upon, and machesthai, to fight, from maché, a battle.) a sober of pes oscine birds, including birds of paradise. > e- DACUS n. (Gr. epimachos, equipped for attle.] a heraldic griffinlike monster.
84558:griff, n. same as griffin.
84581:grif/fin, n. (prob. from griffin (animal), in- fluenced by native word.}
84583:z H ; race horse making its first race. [Anglo- nd. frif’fin-Age, n. in India, the condition of being a griffin or newcomer, grif’fin-ism, n. 1. griffinage; hence, lack of experience. 2. griffinlike vigilance. grif/fon, n. 1. a griffin.
--emerald--
5429:of Al-ex-an‘drine, a. of an Alexandrine or Alex- andrines. Ss, al-ex-an/drite, n. [named after Alexander II, 'h- Czar of Russia.] a variety of chrysoberyl, emerald-green by daylight and deep red by in- artificial light. ch a-lex/i-a, n. [L., from Gr. a priv., and lexis, speech, from legein, to speak.] inability to SS, read, caused by lesions of the brain; word blindness. as a-lex/in, n. [Gr. alexein, to ward off.] a sub- stance found in the blood, capable of destroy- ly. ing bacteria. k; ht- a-lex-i-phar’mic, ålexiphär’mac, a. [L., from Gr. alexipharmdkon; alexein, to ward off, Ing and pharmakon, poison.] expelling or resist- ts. ing poison; antidotal, ted alex-i-phar’mic, a-lex-i-phar’mac, n. an old antidote. q 5 a-lex-i-phar’mic-al, a-lex-i-phir’/mac-Al, a. ind same as alexipharmic.
18612:ee of beryllium: emerald and aquama-
19617:tates. bird of ill omen; (a) a bearer of bad news; 6) an unlucky person. ird of Jove; the eagle. bird of Juno; the peacock. | bird of Minerva or bird of night; the owl. bird of paradise; (a) a beautiful bird of the enus Paradisea, native in the Orient and ‘ew Guinea. One of the better known species has the head and back part of the neck.lemon- colored, the throat emerald green, the breast black, and the wings of a chestnut color. (b) in : Australia, the lyrebird, so named by early Gaps settlers; (c) in astronomy, a small constella- tion of the southern heavens. | bird of passage; a bird that migrates at the changes of season in spring and autumn; hence, anyone who roams about constantly. bird of peace; the dove. : bird of prey; any of a number of flesh-eating birds, as the eagle, hawk, owl, vulture, etc. birds of a feather; persons having like tastes or characteristics. : : $ early. bird; one who arrives or rises early. [Colloq.] 3 3 ; man-of-war bird; a raptorial sea bird, Fre- gata aguila, with a strong hooked bill and small webbed feet. bird, v.7. to catch or shoot birds. bird’bath, n. a basinlike garden ornament for birds to bathe in. bird’bolt, n. an arrow, broad and blunt at the end, for KUDE birds by concussion, without injuring the plumage. bird cage, a cage made of wires, small sticks, or wicker, for confining birds. : bird/call, n. 1. the sound or song of a bird. 2. an imitation of this. 3. a device for imitating bird sounds. ; bird cher’ry, a European tree or shrub, Pru- 2 nus Padus, bearing small black fruit; also, the i fruit of this tree. : bird dog, any dog trained to hunt birds, as a pointer, setter, or retriever. bird duf’fér, one who alters the color or form of living or stuffed birds by artificial processes, usually with intent to deceive. bird’-eyed, a. quick-sighted; catching a glance as one goes. bird fan’ci-Er, one who is interested in birds; parnadany, one who keeps, breeds, or trains irds, especially cage birds. bird’-foot, n. bird’s-foot. bird grass, a weed of the buckwheat family, with jointed stems, narrow leaves, and spikes of tiny, greenish flowers; knotgrass. bird’house”, n. 1. a small box, often resem- bling a house, for birds to live in. 2. a building for exhibiting birds. bird’ie, n. 1.a small bird: a child’s word. 2. in golf, a score of one stroke under par for any hole. bird/i-kin, n. one of the young of a bird. bird’ing, n. the hunting of birds. bird‘let, n. a small or very young bird. bird/like, a. resembling a bird. bird/lime, n. 1. a sticky substance, usually made of the juice of holly bark or mistletoe berries, extracted by boiling. It is used to pest birds by smearing it on the twigs of a sh. _ 2. anything that ensnares or prevents “escape. bird’lime, v.t. to ensnare and capture by the use of birdlime. bird/ling, n. same as birdlet. bird louse, a parasitic wingless insect infesting birds and some mammals. bird’man, x.; pl. bird’men, 1. a person whose work deals with birds, as an ornitholo- ‘gist or taxidermist. ___ 2. an aviator. [Colloq.] bird mite, a small parasitic mite, occurring in species and mainly infesting birds. rd pep’pér, a species of Capsicum (Capsicum baccatum), a pepper g small red fruit. Pant a plant flourishing in Mexico, | bears a yellow flower suggestive of a
19692:birth stone; a precious or semiprecious stone which symbolizes the month of one’s birth. The usual list is as follows: January, garnet, February, amethyst; March, bloodstone; April, diamond; May, emerald; June, pearl; July, ruby; August, sardonyx; September, sapphire; October, opal; November, topaz; December, turquoise. oe
32709:produce the green tinge of the blood in certain marine worms. chlo’/ro-dyne, 7. a powerful anodyne remedy “formerly much used, containing opium, chlo- roform, Indian hemp, etc. chld’ro-form, n. [chloro-, and formyl, from L. * formica, an ant.) trichloromethane, or formyl trichloride, CHCls; a colorless, volatile liquid of a sweetish taste. It is used as an anesthetic in surgical operations, and as a solvent. chlō’rö-fọrm, v.t.; chloroformed, pt., $$; chloroforming, ppr. 1. to anesthetize with chloroform. 2, to kill with chloroform. chlō”rö-fọr’mic, a. containing or pertaining to chloroform or its use. chld/r6-form-ism, n. in medicine, the un- healthy condition resulting from the habitual use of chloroform. chlo/ro-form/ist, n. the person giving chloro- form as an anesthetic. chld’rd-gen/ic, a. in chemistry, pertaining to or designating a crystalline, colorless, tan- ninlike acid obtained from coffee berries or a similar source. chlo’rd-hy’dro-car’/bdn, n. in chemistry, any chlorine derivative of a hydrocarbon. chlo'ro-1/6-dide, n. in chemistry, an iodochlor- e: chlōrö’må, n. [Gr. chlöros, yellowish green.] a fleshy tumor of a greenish color, occurring usually in the membranes of the skull. chlo-rom/e-tér, n. [chloro-, and Gr. metron, a Measure.] an instrument for testing the bleaching powers of chloride of lime. chlo-rom’e:try, n. the process for testing the bleaching power of any combination of chlo- chlo’rd.my-cé/tin, 2. [chloro-, and -mycete, fad -in.] a synthesized antibiotic drug used in hig treatment of rickettsial and virus diseases. £hlo-ro/pal, n. [chloro-, and L. opalus, opal; gre opallios, a rock, stone, precious stone.] a Sesh earthy mineral, consisting of silica oxide of iron, with eighteen to twenty per aoe of water. = ay do phāne, n. [chloro-, and Gr. -phanés, f nt; from phainein, to show.] z When Nay of fluor spar, from Siberia. eautifnl aced on a heated iron it gives a iful emerald-green light. cones © pigment in the inner portion of the 3. Of the retina, yellowish-green in color. aCe Pa. @-ae (-fis/é-€), ».pl. [chloro-, and alga YROs, seaweed.] a large group of green chls € Or seaweeds. ihe Oh oN ceous (fish’us), a. pertaining to Chid/r6. es Phyo PAYU, chis/r6-phyl, n. [Fr. chloro- ile; Gr. chlg d phyllon, leaf the green col Gros, green, and phyllon, le: .] in the or fe) oring matter contained in plants: dioxid, 2 €sence of sunlight it converts carbon and water into carbohydrates. It is
33245:lan, to weld.] a silicate of copper of a fine emerald-green color.
```


## [2026-09-04T18:27:21.354Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB cherub entry ===\"; sed -n '31964p;31959p' WEB_vol1.txt | cut -c1-1200\necho \"=== WEB griffin ===\"; sed -n '84575,84590p' WEB_vol1.txt | cut -c1-1500\necho \"=== WEB emerald ===\"; grep -n \"smaragdus\\|esmeraude\\|em’ér-ald\\|em/ér-ald\\|emeraude\" WEB_vol1.txt | head"
}
```


### [2026-09-04T18:27:21.510Z] TOOL RESULT

```
=== WEB cherub entry ===
cher’ry lau’rel, an e laurc-cerasus, of thie fasion shrub, Pr ive of Asia Minor. y Rosáceas cher’ry pep’pér, a speci * mali, cherry-shaped peat capsicum, having cher’ry pit, 1. the seed of 2. achild’s game played wines cher’ry stone, 1. the seed of the he Stones, _2. a small quahog, a variety of 7 í chér’s6-nése, n. [Gr. chersonésos: chan; land, and 2ésos, an island.) a } va RE Gl tract of land nearly surrounded by poula; a chent, n. Pa ceart, a stone.] y waver . a _dull-colored, flintlik tonnid in poe flintlike quartz often . any of certain similar r hydrated silica and containing imu of chert’y, a.; comp, chertier; superl. ch a like chert; full of chert; flinty. ` Suar cher’ub, .; pl. cher’ubș or, for 1, 2, 3, cher’. u-bim, also, in the Vulgate, chera bi : Tite. cherub; O2 keritb, a cherub.] ae . a winged heavenl i i i Bezel. i. 5-11. apane desc
che-ru/bic, che-ru/bic-4l, a. 1. pertaining to or resembling cherubs; angelic.
=== WEB griffin ===
Ha Wings of an eagle.
TAT valtsentation of this aa heraldry, ture, Gyps fulvus, found in the
üse, bull, brite, tam. up;
Digitized by Arya Samaj Foundation
mountainous parts of Europe, North Africa, he Petia , ac
watcher or guard, as of a person; specifically, a chaperon or duenna.
grif/fin, n. (prob. from griffin (animal), in- fluenced by native word.}
1. an Occidental recently arrived in the East, especially India.
z H ; race horse making its first race. [Anglo- nd. frif’fin-Age, n. in India, the condition of being a griffin or newcomer, grif’fin-ism, n. 1. griffinage; hence, lack of experience. 2. griffinlike vigilance. grif/fon, n. 1. a griffin.
2. one of a breed of wire-haired European dogs, usually of a grayish color, used in hunt- ing game birds.
grif’ tēr, n. (prob. altered from grafter.| a petty grafter; one who runs a gambling device at a carnival, re , ete. (Slang.}
grig, n. [ME. grege, anything diminutive, dwarf; prob. from ON.]
1. a lively, animated person.
2. a small eel. {Obs. or Dial.]
DA ® a grasshopper; (b) a cricket. [Obs. or ial.
as merry as a grig; a saying supposed gen- erally to have reference to the mirth and cheerfulness ascribed to the grasshopper.
=== WEB emerald ===
63553:em/ér-Ald, n. (ME. emeraude; OFr. esmeraude, esmeralde; L. smaragdus; Gr. smaragdos, maragdos, a precious stone supposed to be the emerald.] p í
```


## [2026-09-04T18:27:22.790Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD vol4 smaragdite ===\"; grep -n -i \"smaragdite\\|smaragdine\\|smarag\" FSD_vol4.txt | head\necho \"=== FSD vol2 emerald etym ===\"; sed -n '7601,7612p' FSD_vol2.txt | cut -c1-1500\necho \"=== FSD vol1 cherub etym ===\"; sed -n '64009,64020p;64320,64330p' FSD_vol1.txt | cut -c1-1200"
}
```


### [2026-09-04T18:27:22.926Z] TOOL RESULT

```
=== FSD vol4 smaragdite ===
13313:a   Of  thecolorof  thesmaragd  cmorald-colorcd,  green  smash'»up",  1   sma^li'-up',  2   smllsh'-Op*,  n   (Colloq]  A The  Ileavenb  1   arthAfftofoadine  smash,  especially,  a   dcstnictlve  collision  Oh  a   railway
13315:(<  L   smaragdinus,  <   smaragdus  (<  Gr  smaragdos),  taste  hav’e  a   taste  of  smack
13316:smaragd  smatcli*,  n   [Dial  or  Obs  ]   1   Taste,  tincture  smack  2.
=== FSD vol2 emerald etym ===
ihc  wife  of  Cuciadr.ln. cni'cr-ald,  1   ein'sr-eld;  2   fin'er-ald.  n.  1.  Of,  pertain- ing to,  or  like  the  emerald,  c   pi'cinliy  in  eo!  ir:  hence,  of a   rich  and  vivid  green  color.  2.  Printed  with  or  desig- nating the  f   j-pe  called  eniernli!;  as,  an  cm/  rnbl  edition.— emerald  eoppor,  same  as  mi  u'-r  tsr .   -   em'i'r-ald  dish",  n. .1  goby  if7oblr,iif}!-js  oecar.iat.'.'t  of  tii';-  IVts!,  Iralifs  ;ind  Gulf of  Mexico,  leaving  the  b.ase  of  the  tongue  eWnliig  with  re- llecSlons  iiiic  it  gem.— e.  green.  1.  A   lirilHant  .wt  on  ra-cm- f/ilng  the  emc!  ud.  fi/'i'  cui  i   v,  71.  2,  A   jdguie.it  m.tiie  of Paris  grtsm.-  B.  Isle,  Ireliintl;  so  f-a!U'ii  t,y  WiJliitm DrenriiUi,  17ril-l,S2il, In  liii  poem  B'in)  bocam.e  nf  the  rlcts- nuHsof  Its  vonliirc.-  e.mioth,  n.  A   moth  of  t hf' genus //iy- parchim.—  e.  niche!  (Mineral.),  same  as  z.aba'J'itb.— e. spmlnntene,  .s:
h.  faro,  bear.)
ein"bry-on'l-forin,  1   em'bn-on'i-forra:  2   ErnTtry-Sn'i-form, I   a.  Having  the  form  or  character  of  an  embryo,
■   em"bry-o-pa“tb:ol'o-gy,  1   em'bn-o-pa-fhero-ji;  2   6m'T)ry-
His  harvest  fields  and  hia  orchards  ’   hang  the  heavy  head,’  1 their  fruitage  wore  indeed  embrautnina  in  the  sun.
Obaik  Ena.  Lit.  and  Lana.,  Thomson  in  vol.  ii.  p.  286.  [a.  1869.] im-brown't.— em-brown'ment,  n. em-brue't,  vt.  To  imbrue. m-brute%  1   em-brdt';  2   6m-brut'.  n.  &   vi.  To  Imbrute.
hardnes.s,  T.,3  to  7.8;  sp.  gr.  2.7,  iie.ariy.  Emeraifls  are found  in  Viiriim.s  p.art3  of  the  world,  including  ligyrit. Plberla,  and  North  Carolina.  The  moat,  beautlfui,  tiio  not the  largest,  emeralds  come  from  Colombia.
I   mark  the  Blow-worm,  as  I   pass.
Move  with  ‘green  radiance’  through  the  rrasa.
An  emerald  of  light.
CoLEBinoi:  Linee  at  Shurtan  Ban  st.  1 ,
2.  In  the  Bible,  an  unidentified  precions  stone  (Hebrew nophek), probably  a   carbuncle,  used  in  the  breastplate  of the  high  priest.
=== FSD vol1 cherub etym ===
or  characteristic  of  a   cherub:  angelic;  as.  cherubic  Innocence-
are  self-explaining;  as.  cherrystone,  c.*tree,  etc. Soue  Vaeiettes  of  Cherries  Cultivated  ix  the Uxited  States.
EXPLANATION.
a   -   amber  e   =   early  o   =   oblate  v,  =   very
&   —   black  h»  heart-  p   —   purple  w   =   white  *
c   «■  com-  shaped  r   =   red  y   =   yellow
pressed  l   =   late  r   =   round
d   =   dark  m   =   medium  e   =   small
For  names  of  places,  the  regular  abbreviations  are  used.
HEART  AND  BICARREAU  CHERRIES.
Names.
c
Cher'sl-dac,  X   kurist-dl;  2   cerisl-dS.  n.  pi.  Herp.  The  Testu - dlnidse.  Cherisus,  n.  (t.  g.)  l<  Gr.  chersos,  dry.]  — eherisld,  n.— cherisold,  a.  &   n.
Cber'sl-phron,  1   kurisi-fren;  2   cerisI-frOn,  n.  A   Cretan architect,  Gih  or  7th  century  B.C«  designed  the  temple  of Diana  at  Ephesus.
eher'sl-um,  1   kur'a-um;  2   cSrisi-Gm,  n.  Ecol.  A   dry waste  formation.
_   tfhes'm;  2   chSs'ny.  n.  1.  Charles  Cornwallis (*/s»182G-Vul876),  an  English  soldier  and  writer;  Military Ylexc  of  Recent  Campaigns  in  Virginia,  etc.  2.  Francis RawdonfiySO-VislSyj).  3   British  general,  born  In  Ireland: chief,  Euphrates  Valley  Exploration  Expedition.  1S35.  3. Sir  George  Tomkyns(‘/«IS30-ViilS95),  an  English  gen- eral and  author.  The  Battle  of  Darting,  etc.
A   land-tortoise,  chess1, 1   <fhes;  2   cbfe,  n.  A   game  played  by  two  or  more persons  on  a   checkered  board  divided  into  64  squares alternately  light  and  dark,  with  lG  men  or  pieces  on each  side,  arranged  at  the  beginning  as  shown  in  the  il- lustration. The  term  piece  in  Its  restricted  sense  designates each  of  the  eight  men  in  the  first  row,  namely,  a ting,  a   Queen,  two  bishops,  two  tnights,  and  two  castles  or roots,  of  which  the  king,  queen,  and  castle  are  known  as major  pieces  and  the  bishop  and  knight  as  minor  pieces. The  second  row  contains  eight  patens.  The  opposing  pieces
are  distinguished  by  their  color,  those  on  one  side  being white  and  those  on  the  other  either  black  or  red,  now usually  the  former.  The  rows  of  squares  running  perpen- dicularly, or  from  one  player  toward  the  other  as  they  sit at  the  board,  are  termed  files,  those  running  horizontally, routs.  The  squares  are  numbered  from  the  players  along  the files,  those  in  each  file  taking  the  name  of  the  major  piece occupying  the  first  square:  thus,  the  square  on  which  the king  stands  Is  called  the  ting's  square,  the  next  in  front ting's  2,  the  next  ting’s  3,  and  so  on.  As  the  board  Is numbered  from  one  side  for  one  player  and  from  the  other side  for  the  other.  It  will  be  noted  that  black  ting’s  6   will be  the  white  ting’s  4,  and  so  on.  The  values  of  the  pieces are  graded  according  to  their  mobility,  which  i3  the  measure
&   Poet.  The  representation  of  a   beautiful  winged  child, or  the  winged  head  of  a   child,  the  accepted  type  of  the angelic  cherub;  any  beautiful  angel.  In  this  sense  the plural  is  always  cherubs.
He  eeemed  a   cherub  who  had  lost  his  way.
And  wandered  hither.  Lowell.  Threnodia  st.  7.
2.  A   beautiful  child  or  infant:  in  allusion  to  the artists'  type  described  above.  3.  One  of  an  order  of angelic  being3  ranking  second  to  the  seraphim  in  the celestial  hierarchy,  and  held  to  excel  in  knowledge; also,  in  Scripture,  the  symbolic  representation  of  such a   being,  as  on  the  ark  of  the  covenant,  typifyi?S  the presence  and  power  of  the  Deity.  See  Ps.  xviii,  10; Ezeh.  x;  Heb .   ix,  5.  [LL.,  <   Heb.  h'rubh,  cherub.]
And  the  Cherubic  host  in  thousand  quires Touch  their  immortal  harps  of  golden  wires.
```


## [2026-09-04T18:27:37.352Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW smaragdus/gryps ===\"; grep -n -i \"smaragd\\|gryps\\|gryphus\\|grypus\" LEW_1910.txt | head -10\necho \"=== LAT smaragdus/gryps ===\"; grep -n -i \"smaragd\\|gryps\\|gryphus\\|grypus\" LAT.txt | head -10\necho \"=== HJB emerald/marakata/zumurrud ===\"; grep -n -i \"marakata\\|zumurrud\\|emerald\\|smaragd\" HJB.txt | head -12"
}
```


### [2026-09-04T18:27:37.446Z] TOOL RESULT

```
=== LEW smaragdus/gryps ===
=== LAT smaragdus/gryps ===
27069:gryphus, -I a .(grifus, etc.): latinisation tardive et vulgaire
27070:du noa grec du griffon, YP 0 '!'» transerit gryps par la 1 . litteraire
58762:smaragdus (zna-), -I m.: emeraude. Emprunt au gr. CTp,dpay6oc, de¬
58763:puis Varr. et Lucr., M.L.8041; smaragdinus,-dineus.
=== HJB emerald/marakata/zumurrud ===
14194:1568.  —  "  The  value  of  stones  is  only because  people  desire  to  have  them,  and because  they  are  scarce,  but-  as  for  virtues, those  of  the  loadstone,  which  staunches blood,  are  very  much  greater  and  better attested  than  those  of  the  emerald.  And yet  the  former  sells  by  maoe,  which  are  in Cambay  .  .  .  equal  to  26  arnUds  each,  and the  latter  by  ratUy  which  weigh  8  grains  of wheat." — Oarciot  f.  169i>.
14592:c.  A.D.  350. — "Cocks  too  are  produced there  of  a  kind  bigger  than  any  others. These  have  a  orest,  but  instead  of  being  red like  the  crest  of  our  cooks,  this  is  variegated like  a  coronet  of  flowers.  The  tail-feathers moreover  are  not  arched,  or  bent  into  a curve  (like  a  cook's),  but  flattened  out. And  this  tail  they  trail  after  them  as  a peacock  does,  unless  when  they  erect  it, and  set  it  up.  And  the  plumage  of  these Indian  cocks  is  golden,  and  dark  blue,  and of  the  hue  of  the  emerald."  —  De  Nat, Animal,  zvi.  2.
15850:1586. —  "I  answered  that  I  was  from Venice,  that  my  name  was  Gasporo  Balbi .  .  .  and  that  I  brought  the  emeralds  frofoo Venice  expressly  to  present  to  his  mojestj* whose  fame  for  goodness,  ooortesy,  and g^reatness  flew  through  all  the  world  .  .  » and  all  this  was  written  down  on  on  dllm* and  read  by  the  aforesaid  'Master  of  the Word*  to  his  Majesty."— (?.  JBottt,  f.  104.
16159:1871.— "In  Ireland  Paddy  makes  riots, in  Bengal  raiyats  make  paddy ;  and  in  thia^ lies  the  difference  between  the  paddy  of green  Bengal,  and  the  Paddy  of  the  Emerald \A\Q,**—Govinda  SamanjUi,  ii.  25.
21221:1857.—"  We  met  Wilby  at  the  advanced post,  the  *  Sammy  Hoose/  within  600  yards of  the  Bastion.  It  was  a  curious  place  for three  brothers  to  meet  in.  The  view  was charming.  Delhi  is  as  green  as  an  emerald just  now,  and  the  Jumma  Musjid  and  Palace are  beautiful  objects,  though  held  by infidels.*' — Lettert  icritUn  during  the  Siege  of Delhi,  by  Hervey  GreaUud,  p.  112.
```


## [2026-09-04T18:27:38.402Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN emerald ===\"; grep -n -i \"emerald\\|smaragd\\|marakata\" SYN.txt | head -10\necho \"=== IEC ===\"; grep -n -i \"smaragd\\|marakata\\|gryps\\|grup\" IEC.txt | head -10\necho \"=== WEB range ===\"; tail -c 800 WEB_vol1.txt"
}
```


### [2026-09-04T18:27:38.479Z] TOOL RESULT

```
=== SYN emerald ===
=== IEC ===
=== WEB range ===
apel or church erected in memory of a martyr or confessor.
mé-m0/ri-4l, a. [OFr. memorial; L. memorialis, of or pertaining to memory, from memoria, memory.]
1. serving to help people remember some person or event; commemorative.
2. of memory.
mé-m0/ri-Al, n. 1. anything meant to help people remember some person or event, as a statue, holiday, etc.
2. a note or hint to assist the memory; a memorandum. [Obs.]
3. a written statement of facts submitted to a person or persons in authority, as to Congress; a statement of facts accompanied with a petition. à
4. memory; remembrance; that which is or may be remembered. [Obs.]
5. in diplomacy, an informal state paper, used in negotiations, and containing such documents as circulars sent to foreign agents, answers to the communications of amba
```


## [2026-09-04T18:27:51.562Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN ===\"; grep -n -i \"smaragd\\|zumurrud\\|zumurud\\|barq\\|baraka\\|kerub\" HRN.txt | head -15\necho \"=== HUB ===\"; grep -n -i \"smaragd\\|zumurrud\\|zumurud\\|barq\\|baraka\\|kerub\" HUB.txt | head -15\necho \"=== LEW size/S ===\"; wc -l LEW_1910.txt; grep -n -c \"^\" LEW_1910.txt; grep -n \"smaragd\\|zmaragd\" LEW_1910.txt|head; grep -n -i \"^s.macer\\|smilax\\|sm\" LEW_1910.txt|head -3"
}
```


### [2026-09-04T18:27:51.685Z] TOOL RESULT

```
=== HRN ===
1389:hambarakapet; ai. sam-r- V^par-.
8799:1011. niTnö {*menö) Himmel, Paradies; Smaragd', vergl.
8811:2) Np. mwö *Smaragd', minä *Emair (kurd. LW. mtnä)^ *hiinmel-
22243:i hambarakapet 111.
=== HUB ===
=== LEW size/S ===
14865 LEW_1910.txt
14866
251:TaxFnig IIT 231 pat IT 404 pan I 326, If 397 Patanai ITI 262 patensins, pat<tt> II 262 patir IT 263 peeskxum> II 346 meked IT 312 perek<ats> II 292 peremust I 400, II 284 Pernat I 485, 11 275, 286 perom II 285, 287 pert II 284 pertemest I 400 pertemust I 400, II 284 pertumum I 400, IT 284 pestlim II 346 petiropert II 284, 285, 400 petora II 400 Pikufn... II 300 -pid, -pid I 310, II 410 pidum, pidum I 380, 390, I1 410 pieisum I 301 piihiit IT 312 Pustiat II 308, 406 pis, pis, pid, pispis, pitpit, pisptd ITI 410 mo IT 312 pud II 404 piveh I 301 puiiu I 301, II 404 pomptis, ITopstes II 408 yin, pon I 310, 326, II 397, 411, 412 Pintiis II 408 puinttram IL 337 Pupidiis, Pupdiis II 338 <purtam IT 343 posmom II 349
275:et I 421 faber I 437 famel I 452 fertlid I 485, 486 fesn. I 454 firata I 486, 498 forte I 484 hanustu I 454, 656 Herentas I 658 hospus I 660 ' ancubat I 298, 687 anim, inom I 404 Joviois I 732 ap I 670 lexe I 780, 789 lifar I 790 locatin I 817 loufir I 791 media II 56 Minerva II 90 Nounis IT 179 Pacia, Pact II 231 pacri- II 231, 232 Perseponas II 375 pes II 312 Plauties II 320 pracom I 256 praicime I 687, II 351, 352 Prismu II 868 pristafalacirix IT 285, 584 pritrome I 687, II 285, 357, 363
313:aruettu II 742 arvia, aruvia I 71 ar-, ars-, af I 11 afkant I 154 arfertur, arsfertur I 13, 484, 843 arsie I 12, II 487 arupes. arepes I 12 arsir I 30 arsmatiam I 12 Afmune I 12, 32, 843 arsmor I 12, 36 arpeltu I 11, 59, TCA) arpes I 12 arputraty I 62 afvettu, arsueitu, aruettu I 12, Th 42 ase I 61 aseceta I 686 asnata I 686, IGE aso I 65 aterafust I 361 atero I 33, 845 atru I 75 avie, aviekla, aviekate I 84 avif, avef I 84 berva, berus II 766 bio II $09 bum, bue, buf I 112 cabriner, kabru LI 157 kalefuf I 139 kanetu I 154 capif, kapire I 160 kaprum I 157 karne I 170 kartu I 170, 198 karu I 170, 855 kafetu, karitu, carsitu I 15, 137, 141, 180 kastruvuf, castruo I 180 katel, katles I 183 kateramu, catera- hamo I 181
```


## [2026-09-04T18:27:53.608Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY barakat/barq/zomorrod/karrubi ===\"; grep -n \"برکت\\|برق\\|زمرد\\|کروبی\" incoming/ARY/ARY_pages.txt | head -15\necho \"=== MON part1 ===\"; grep -n \"زمرد\\|کروبی\\|برکت\" MON_part1.txt | head -10\necho \"=== MON part2 ===\"; grep -n \"زمرد\\|کروبی\\|برکت\" MON_part2.txt | head -10"
}
```


### [2026-09-04T18:27:53.699Z] TOOL RESULT

```
=== ARY barakat/barq/zomorrod/karrubi ===
311:صادق است. واژه‌ی «یخچالء (چاله‌ی یخ) را برای ابزار سرد ساز برقی بکار می‌پریم. واژه‌ی «سپر» را ۰۹ 48۶
2625:فارسی (۳87514): افسردن, افسرده (یه چم اپزمرده, آدلسرد, آسرد؛)
10389:چم این واژه در زبان‌های ژرمنی: سکان؛ (باسکان يا فرمان) راندن» برقرار کردن
=== MON part1 ===
5337:مانند الماس و زمرد و غیره -بر حلقة 
19367:ایلغار: :1.2 [- یلغار. تر.] (امر.) حبرکت 
28370:پا کان خطهٌ اول: (کد.) ملایکه و کروبیان و 
31454:پزمردد: 022010۲-0 [- سژمربدن |] 
36774:مق. بزمرده» خشکد. بد یع. بارونق» باجلو ه. 
37379:گرفتن به چیزی. بلند شدن. با برکت شدن. 
37904:مثلا زمردای) که مان دق مردای ص مره 
54674:نعمت الله ۸۷ فرع. سج.) خاتم زمردین: 
58527:برکت. (ص.) صواب. با فیض؛ با برکت. 
61911:درود. برکت. صیفغهٌ دعاء: (دس.) فعلی است 
=== MON part2 ===
22552:کروبی: ۱۰50 [ع. آشوری» پاسبان] (.) 
22553:در تورات کروب (ج. کروبیم) به فرشتگانی 
22558:تابوت سکینه قرار داشتند و بال‌های کروبی 
22561:کروبیون» کر وبیین. ضصح. در شعر به تشدید 
28432:کوه زمرد: (کد.) چبزی که حصول آن 
30660:گر د زمرد: تودة زمرد. ( کد.) سبزة نورسته» 
39543:شراب: می. لعاب زمرد نقاب: ( کد.) شراب 
40251:تناسلی قرار دارند» لگن. لکن زمردی: ( کد.) 
42085:در حبرکت حیوان عمل مهمی انجام 
50927:مکانی که در آن خیر و برکت و فراوانی
```


## [2026-09-04T18:28:08.458Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '22548,22566p' MON_part2.txt\necho \"=== page markers? ===\"; grep -n \"^\\[pdf page\\|\\f\" MON_part2.txt | head -3; awk 'BEGIN{RS=\"\\f\"} END{print \"leaves:\",NR}' MON_part2.txt; awk 'BEGIN{RS=\"\\f\"} END{print NR}' MON_part1.txt"
}
```


## [2026-09-04T18:28:10.200Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON zomorrod headword ===\"; grep -n \"^زمرد\\|زمرد:\\|زمرّد\" MON_part1.txt MON_part2.txt | head -10\necho \"=== MON barq ===\"; grep -n \"^برق\\|برق:\\|برق‌\" MON_part1.txt | head -10\necho \"=== MON barakat headword ===\"; grep -n \"برکت:\\|^برکت\" MON_part1.txt | head -10"
}
```


### [2026-09-04T18:28:10.412Z] TOOL RESULT

```
کرو: (0۷-) ۵۲۵۷ (.) فرهنگ نو بسان به 
معنی کشتی و جهاز کوچک و زورق 
نو شته‌اند. 

کروبی: ۱۰50 [ع. آشوری» پاسبان] (.) 
در تورات کروب (ج. کروبیم) به فرشتگانی 
اطلاق شده که از حضور خدا فرستاده 
می‌شوند با آنکه همواره در نزدش حاضرند 
و گفته شده است که ابشان دارای دو بال 
هستند اما تمثال آنان از طلا بود و در زیر 
تابوت سکینه قرار داشتند و بال‌های کروبی 
بر تابوت سایه می‌افنکند. در اسلام آن را 
مهتران فرشتگان یا ملائکة مقرب دانند؛ ج. 
کروبیون» کر وبیین. ضصح. در شعر به تشدید 


راء آید و در تداول فار سی نیز مشدد تلفظ 
شود. 

=== page markers? ===
leaves: 1
1
```


### [2026-09-04T18:28:10.500Z] TOOL RESULT

```
=== MON zomorrod headword ===
MON_part2.txt:28432:کوه زمرد: (کد.) چبزی که حصول آن 
MON_part2.txt:30660:گر د زمرد: تودة زمرد. ( کد.) سبزة نورسته» 
MON_part2.txt:93412:زمرد در لابه‌های قلع‌دار بدست می آورند» 
MON_part1.txt:71485:زمرد: 2000۳704 (.) (زه.) یکی از 
=== MON barq ===
4414:برقوق. 
7260:برق وصل می‌شود و پس از رفع حاجت از 
10074:ارعد: ۵ (ع.] (ص.) رعدزده برق‌زده. 
11396:استبرق: رجرطاهای هر ِ- استبرکث| ۰( 
12570:برقرار» پابدار» ثابت» بای بر جا. محکم؛ 
16282:می‌رود؟ برق‌سنج. 
22037:درخشنده» برق‌دار. 
22544:برق: او [ع.] .( درخش» درخشندگی» 
22550:ببرق‌اسا: 2:5 (ع. ف.] (قمر.) مانند 
22551:برق» بسیار تند و تیز. 
=== MON barakat headword ===
58527:برکت. (ص.) صواب. با فیض؛ با برکت.
```


## [2026-09-04T18:28:16.550Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- MON barq ---\"; sed -n '22540,22552p' MON_part1.txt\necho \"--- MON zomorrod ---\"; sed -n '71483,71500p' MON_part1.txt\necho \"--- MON barakat grep ---\"; grep -n \"برکت\" MON_part1.txt | head -20"
}
```


### [2026-09-04T18:28:16.639Z] TOOL RESULT

```
--- MON barq ---

بسرفنجک: 1 [۲2۱ دا [- درفنحک 2 
ولیک ده سک بان رو 
فرهانج] ((.) بختکك» کابوس عبدالجنه. 
برق: او [ع.] .( درخش» درخشندگی» 
درخشش. جلای فلز. (فز.) جرقه‌ای که در 
اثر نزدیکك شدن الکتريسيتة منفی و مثبت 
تولید شودء نوری که در اثر برخورد ابرها (به 
علت دارا بودن الکتريسيتة مثبت و منفی) 
تولید شود. برق خاطف: (طبی.) برق. 
ببرق‌اسا: 2:5 (ع. ف.] (قمر.) مانند 
برق» بسیار تند و تیز. 

--- MON zomorrod ---
در دمك. 

زمرد: 2000۳704 (.) (زه.) یکی از 
سنگ‌های قیمتی به رنگ سبز و آن هر چه 
پر رنگتر باشد گرانبهاتر است. ضح.- قدما 
می‌پنداشتند که نظر بر زمرد چشم افعی را 
کور کند. 

زمره (ع)هصم2 [ع. زمر ة] (.) گروه» 
جماعت» دسته. 

زمزم: تعتهده [- زمزمه] (اصت.) ترنم به 
آهستگی. دعائی که زردشتبان آهسته و زیر 
لب خوانند (به هنگام طعام خوردن و غیره) 
زمزمه: (22072012)6 [سعر. زمزمه. قس. 


زمزم] (مصل.) ترنم کردن» تغنی کردن. (.) 
--- MON barakat grep ---
19367:ایلغار: :1.2 [- یلغار. تر.] (امر.) حبرکت 
37379:گرفتن به چیزی. بلند شدن. با برکت شدن. 
58527:برکت. (ص.) صواب. با فیض؛ با برکت. 
61911:درود. برکت. صیفغهٌ دعاء: (دس.) فعلی است 
78661:کی تل: برکت. رحمت. (.) ۳ دوزح»
```


## [2026-09-04T18:28:27.537Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '22552,22620p' MON_part1.txt | grep -n \"برک\" \necho \"--- range dump ---\"; sed -n '22552,22600p' MON_part1.txt | head -50"
}
```


### [2026-09-04T18:28:27.613Z] TOOL RESULT

```
7:برک: ۲ (- پرکث] (اخ.) ستارة سهیل. 
10:برک: (.) نوعی بارچة ضخیم که در 
15:ببرکایوز: 7- 0۵۲۰۵6 [< بر کابوس ِ- 
19:نیکختی» » سعادت؛ ج. برکات. 
22:با نزنذن اش افروختن. از بیخ برکندن. از 
34:برکی: ۲۵1-1 ها (ص ‌نس. امر.) کلاه درازی 
35:که از برک یا نمد دوزند» زاهدان و 
--- range dump ---

برفع: "و0۵ [ع.] (.) قطعه‌ای پارچه که 
زنان صورت خود را سدان پوشانند؛ 
روی‌بند» رود نقاب» ج. بر اة 

برقوق: هد" (.) (گی.) آلو. (گیء.) آلوچه 
برک: ۲ (- پرکث] (اخ.) ستارة سهیل. 
بر کك. 

برک: (.) نوعی بارچة ضخیم که در 
رن رای ری کب بر ز با دست افند 
و از آن جامه زمستانی دوزند. قسمی از 
گلیم. ‏ جامةٌ کو تاهی که تا کمرگاه را بوشاند و 
مردم گیلان 1 را می بو شید ند. 
ببرکایوز: 7- 0۵۲۰۵6 [< بر کابوس ِ- 
بر کافوز] (امر.) پیرامون دهان؛ پکث و پوز. 
بسرکت: 32( [ع. ی 2 (مسص‌ل ( 
گوالیدن. فزونی» بسیاری. خجستگی» یمن. 
نیکختی» » سعادت؛ ج. برکات. 

بر کردن: ۸۵۵ (مصم.) بلند کر دن» 
با نزنذن اش افروختن. از بیخ برکندن. از 
بر کردن. 

بر کشیدن: ۸۲-2)6(5-20ظ (مص م.) بالا 


کشیدن چیزی. نز وان کمن ) استخراج 
کرون سرون ات .برهم کشیدن» چین‌دار 
کرد ترقی دادن بر مرتبة کسی افزودن. 
ترییت کردن؛ پروردن. 
بر که: (۵-) 3۵۲62 [ع.] .( آیگن آسدان؛ 
استجر » تالا 
برکی: ۲۵1-1 ها (ص ‌نس. امر.) کلاه درازی 
که از برک یا نمد دوزند» زاهدان و 
درویشان بر سرگذارند؛ برنس. 
پرگ: ۵ (.) (گیا.) جزوی از گیاه که 
از ک و پهن است و از کنارهای ساقه با 
شاخه‌ها روید و بیشتر به رنگ سبز است» 
اندافی از کاه که اغلت تمورت ارت 
پهن و سبز بر اثر رشد و نمو جوانهٌ انتهایی با 
جوانه‌های محوری بر روی ساقةٌ گیاه ظاهر 
می‌شود: غالا این قضم دای خقازن دو 
طرفی است. برگ‌ها به اشکال گوناگون در 
گیاهان مختلف دیده می‌شوند؛ ورق» ورقه» 
بلگ. . نوعی درفش برای قطع کردن کرباس 
در طول تخت کبوه. ساز؛ نوا استات؛ 
دستگاه» سامان (خصوصاً مهمانی). توشه 
آزوقه. قصد» عزم. التفات» توجه» پروا.
```


## [2026-09-04T18:28:29.759Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 برق/برکت ===\"; grep -n \"برق\\b\\|برکت\" BQT_v1_pages.txt | head -20\necho \"=== BQT v2 زمرد ===\"; grep -n \"زمرد\" BQT_v2_pages.txt | head -10\necho \"=== BQT v3 زمرد/کروبی ===\"; grep -n \"زمرد\\|کروبی\" incoming/BQT/BQT_v3_pages.txt | head -10\necho \"=== BQT v4 کروبی ===\"; grep -n \"کروبی\\|زمرد\" incoming/BQT/BQT_v4_pages.txt | head -10"
}
```


### [2026-09-04T18:28:29.867Z] TOOL RESULT

```
=== BQT v1 برق/برکت ===
77:وارایعوازن در تیان و موز نوبرق مرو مسر عبت
3407:سبرقند ماست را گو یند » ومعرب آن سقرات است > و ذبل < روف»> گوید:
3468:افر نجشك]» بدران (ذیل: دوقوس ۰ وذیل: وشك )۰ برقك (ذیل:ایر‌سون)»
4111:آزر» آزرمیدخت » آینه سکندری » ابغاز » ابرشپر » ابرقباد » ابسرقوه »
6220:و آن شیشه ماتندی باشد که یشتر برقت باریدن
6540:40 < ۵ .۲ س ۱۸۰ و ۱۷۹۰ * » اشکاشکمی و وخی 116 ( برق ) «کربرسن ۷۳ ۰
6618:کاف » بمعنی برق باشد  -‏ وکرم شب تاب را یز
6835:و صاعقه و رعد و برق ماشد .
7149:کویند - و بمعنی برق هم آمده است- و آتش-
7155:ببرق دارد .
8574:۴ - تاب قپرش تیغ را الماس کرد برق خشمش کوه را آلا کرد
8799:۴ - برقلهٌ فاف بخت واقبال 7 آموت عقاب دولت شت . منجيك
9474:ابابرقی وبلجسن صاعقه ابا غلغل رعد در کوهار. رود کی.
9647:۰ الراهیم ‏ رك : اپرهام . زا ابرقو , ایرقوه , امرقویه رک : اب کوه -
9908:کرده بودند بانابکی بعنی سریرستی شاهزادگان جوان ملجوقی برقرارشدند و شد بتدریج در این‌ثفل
10126:از ریفه‌هابی که برای زینت برق آویشته بودند بضویی نمابان است انسا .که شهر ممیتی در
10376:برق برادر رعد را کوشد » و بکسر جیم حم
14035:و بکوبند وبا عصل برقضیب مالند سطب کرداند .
15432:ابادي - بررزن لمازی » برقع سیاعی
15441:باشد که نوعی از برقع سیاه است که زنان بر
=== BQT v2 زمرد ===
2382:       ‫ز زمرد ‪.‬‬     ‫و اندر دم اوسبز جلیلی‬         ‫‪ -۳۴۲‬بر گردرخش(سیب)یر‪ ,‬قطی‌چند زد‬
2518:‫است معروف که او را عربان متوشلخ کویند ‪.‬‬         ‫مائند لمل ‪ - ۱‬کونایه ازمردم بداسل و جاهل‬
2726:‫و يك‬    ‫لك‬    ‫کنند ‪ -‬و کتابه ازمردم تاتراشدة‬
3249: ‫حو شده مغر = کنابه ازمردم خشمناك‬                                                                 ‫جوشیدن باشد ‪.‬‬
5543:                                                    ‫دیدن وتعریف کردن بعضی ازمردم بهم‌میرسد‪. .‬‬
7053:‫وغبر معین ‪ -‬و بمعنی هرچند وهرچه لیزآمده‬               ‫است ‪ --‬و کنانه ازمردم ناهه‌وار و درشت باشد ؛‬
8493:                                                    ‫حته نی هقز ‪ -‬کنابه آزمرده دل بودن‬
9715:‫تاخلف وخانه براندازباشد‪ .‬و کنابه آزمردم مذ بر‬                    ‫آخر شدن وبانتها رسیدن باشد ‪.‬‬
14824:‫ونابه ازمردم‬
15483:                                                                     ‫ازمردم همان‌دایره میگوید که «برخیزوبگیر»‬
=== BQT v3 زمرد/کروبی ===
453:وکنایه ازمردم دبوث وبچشم خودبن باشد ۴ .
2619:‏يك ازمردم محله را نام ‎al pa‏ ووهاکنند تابایغان
8825:‏شیر ‎SO‏ ۰ با نالی مجپول, کنایه ازمردم
10504:و خشكاست (۲)-ر کنابه‌ازمردم کند ‎hs ab‏
11169:‎aml‏ , جماعتی و کروهی ازمردم را کوبند که
12370:ازمردم معزول شده هم هست.
14643:‎». ‏زمرد اندر تاکم؛ عقیقم اسر غژب یلم اسر خم,آفتابم اسر جام‎
15106:‏ازمردم بگیرند درآن کوزمریزند؛‎ Soi ‏عحلقی 4 ۴ - بروزن و ممنی کلکونه | وغیرهم‎
17380:ازمردم ‎sey‏ - وبکس اول بمعنی‌فرست‌بافتن
20440:‎JO 09 pad‏ ینم اول ,کنابه آزمرده
=== BQT v4 کروبی ===
661:هلیون کوبند (۱). دفع‌سموم جانوران کز ندمومار مار دو ز بان «کنایه ازمردم منافق
690:زین فلك زمردین بهرچه مار میخوری ؟
2516:تا مورد سبز باشد چون زمرد تا لاله سرخ باشد چون مرجان.»
3375:(بوسی)» پسرخرگان ازمردم پسا(فا) که مانوی بود؛آبینی بنام « دربست دین » 0488 107181
6093:وکنایه ازمردم رش سفید محله و بلزار واستاف | درلقصان نباشدآنرا بگیرند نامنفمت بخشد وآنرا
6622:فارسی 13188 (زمرد). 88168 (مینا ) ( کردی ع 33188 ) (آبی آسمانی ) باوستایی-198181
6624:همربشةٌ « مینو » بمعنی آسمان و بهشت وزمرد داسته است . - جهانگیری برای این
6640:والوان باشد۴ - وزمرد وزبرجد را نیز کوبند۴ . | موی باشد که عربان شمرخوانند ‎٩‏ - و جر بسنی
8876:درحدود ۳۸۰ ومتوفی‌درلیبی‌درحدود*۶4. وی شا کرد تئودور ازمردم 8/108516516(8/1009138)
9549:بمربی لیل کوبند ۴ . فقد گیر ان ‎٩‏ «کنایه ازمردمانی باشد
```


## [2026-09-04T18:28:52.903Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA zumurrud ===\"; grep -n -i \"zumurrud\\|zumurud\\|Smaragd\\|zamurrad\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20\necho \"=== PLA pages ===\"; grep -n \"زمرد\" incoming/PLA/PLA_pages.txt | head -10"
}
```


### [2026-09-04T18:28:52.963Z] TOOL RESULT

```
=== PLA zumurrud ===
10661:32, - zabarfad: '"Chrysolith, Smaragd" pers. 9, wahrscheinlich aus pers. 
11107:2, - zumurud: "Smaragd" pers. 5 aus pers. E95 zomurrod mp. wDlsı 
11111:griech. nAdfargoE ‚ syr. zmargda, ar. zumurrud, russ. izmrud 
11117:2 - zumurrud = zumurud q. V. 
11119:San - zumurrudi: Nisba v. zumurrud "smaragdgrün" 
=== PLA pages ===
```


## [2026-09-04T18:28:54.958Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ barq/zumurrud/karub ===\"; grep -n -i \"zumurrud\\|karubi\\|kerub\\|cherub\\|Baraqa\\|smaragd\" FVQ_pages.txt | head -20\necho \"=== AFM zomorrod variants ===\"; grep -n \"الزمرد\\|زمرذ\\|( زمرد\\|زمرد )\" AFM_pages.txt | head -10\necho \"=== AFM سmore ===\"; grep -c \"\" AFM_pages.txt"
}
```


### [2026-09-04T18:28:55.073Z] TOOL RESULT

```
=== FVQ barq/zumurrud/karub ===
=== AFM zomorrod variants ===
=== AFM سmore ===
6684
```


## [2026-09-04T18:29:01.710Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11098,11125p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt\necho \"=== find printed page ===\"; awk 'BEGIN{RS=\"\\f\"} /zumurud: \"Smaragd\"/{print \"leaf\",NR}' incoming/PLA/PLA_pages.txt\ngrep -n \"zumurud\" incoming/PLA/PLA_pages.txt | head"
}
```


### [2026-09-04T18:29:03.910Z] TOOL RESULT

```
2 


. . . 4 
Er zamag : "Gummjiarabicum" aus pers. «,; zame = samg . 


2, - zumurud: "Smaragd" pers. 5 aus pers. E95 zomurrod mp. wDlsı 
uzmburt < *zmaurd zmagrd mit Metathese v. zmargd s. zibargad, 


griech. nAdfargoE ‚ syr. zmargda, ar. zumurrud, russ. izmrud 


= 


2 - zumurrud = zumurud q. V. 

San - zumurrudi: Nisba v. zumurrud "smaragdgrün" 

@%- zaman: Pl. v. yL,; zamän q. v. 

as) - zumna: "von einer chronischen Krankheit :befallen" « 
av - zamani: "zeitlich, vergänglich" 

=== find printed page ===
8368:2,         -       zumurud:                 "Smaragd"             pers.        5 aus        pers.               E95 zomurrod                  mp.    wDlsı
8373:2          -       zumurrud                 =    zumurud          q.     V.
```


## [2026-09-04T18:29:08.773Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /zumurud:/{print NR; exit}' incoming/PLA/PLA_pages.txt\necho \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==0' incoming/PLA/PLA_pages.txt >/dev/null\npython3 - <<'EOF'\np=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,pg in enumerate(p,1):\n    if 'zumurud:' in pg:\n        print('leaf(1-based)',i,'printed',i-15)\n        print(pg[:200])\n    if 'zabarfad' in pg or 'zibargad' in pg:\n        print('ZAB leaf',i,'printed',i-15)\nEOF"
}
```


### [2026-09-04T18:29:10.695Z] TOOL RESULT

```
162
---
ZAB leaf 155 printed 140
ZAB leaf 156 printed 141
leaf(1-based) 162 printed 147
zambaq                                                                               147                                                              zanädiga



3»,        - zambag:                  
ZAB leaf 162 printed 147
```


## [2026-09-04T18:29:55.969Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AKD cherub/kerub ===\"; grep -n -i \"Cherub\\|kerûb\\|k.rûb\\|karibu\\|kâribu\\|kuribu\\|Segen\\|segnen\" AKD.txt | head -20\necho \"=== AKD brk ===\"; grep -n \"brk\\|barâku\\|baraku\" AKD.txt | head -10"
}
```


### [2026-09-04T18:29:56.053Z] TOOL RESULT

```
=== AKD cherub/kerub ===
1032:akk.  loräbu-  segnen,  beten  :  ^  viell.  doch,  ti'otz  anderer  Möglich- keiten, südarab.  krb  segnen,  shrb  weihen,  mkri  (auch  noch  heute  mikräb) Heiligtum,   Tempel  (>  wohl  äth.  mekwräb  Heiligtum).  akk.  aräru
1094:akk.  Mribu  wörtl.  segnend.  Bez.  der  Stierkolosse  :  >  wohl  (aus einer  Kebenf.  karülni)  hebr.  korüb  Cherub.  Fi'aglich,  ob  dazu  auch  ygvtp, griplius,   Greif  gehört.  akk.  seäu  Name  eines  Dämons  :  >  hebr.
=== AKD brk ===
```


## [2026-09-04T18:29:57.779Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD vol4 smaragdite ===\"; grep -n -i \"smarag\" FSD_vol4.txt | head -20\necho \"=== FSD vol2 eclogite ctx ===\"; sed -n '4926p' FSD_vol2.txt | cut -c1-600\necho \"=== ARY latin index ===\"; grep -n -i \"BARQ\\|ZOMORROD\\|ZUMURRUD\\|EMERALD\\|KARRUBI\\|BARAKAT\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-04T18:29:57.880Z] TOOL RESULT

```
=== FSD vol4 smaragdite ===
13313:a   Of  thecolorof  thesmaragd  cmorald-colorcd,  green  smash'»up",  1   sma^li'-up',  2   smllsh'-Op*,  n   (Colloq]  A The  Ileavenb  1   arthAfftofoadine  smash,  especially,  a   dcstnictlve  collision  Oh  a   railway
13315:(<  L   smaragdinus,  <   smaragdus  (<  Gr  smaragdos),  taste  hav’e  a   taste  of  smack
13316:smaragd  smatcli*,  n   [Dial  or  Obs  ]   1   Taste,  tincture  smack  2.
=== FSD vol2 eclogite ctx ===
Ec'lo-ga  I.e'gnm,  1   ek'lo-ga  li'gom;  3   6e'lo-2a  le'gum.  iL.] The  Isaurian  laws.  See  under  law. ee'lo-ge,  1   eh'lo-]l :   3   ee'Io-g?,  ti.  iihctoric.  The  .selection, description,  or  narration  of  .such  details  a.s  are  calculated  to make  the  greatest  impression.  [   <   Gr.  eldogi ;   see  ECLOGtiE.l ■«c'lo-gite,  lek'lo-jait;  Sec'lo-git,  n.  Petrol.  A   rock  consisting of  red  garnet,  omphacite,  and  emerald-green  smaragdlte. [<  Gr.  eUogos,  picked  out,  <   ei,  out,  +   logo,  choose.] ec'lcg®,  1   l   ek'lo.g;  2   ec’log,  7i.  i.  A   i
=== ARY latin index ===
```


## [2026-09-04T18:30:08.895Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    for key in ['karābu  segnen','loräbu-  segnen','Mribu  wörtl','barraqtu']:\n        if key in p:\n            print('leaf(0-based)',i,'-> printed approx',i-8,'| key',key)\n            # show any standalone number\n            nums=re.findall(r'\\n\\s{4,}(\\d{1,4})\\s{4,}\\n',p)\n            print('   nums:',nums[:5])\nEOF"
}
```


### [2026-09-04T18:30:10.799Z] TOOL RESULT

```
leaf(0-based) 69 -> printed approx 61 | key barraqtu
   nums: ['60']
leaf(0-based) 75 -> printed approx 67 | key loräbu-  segnen
   nums: []
leaf(0-based) 78 -> printed approx 70 | key Mribu  wörtl
   nums: ['69']
```


## [2026-09-04T18:30:18.210Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (74,75,78):\n    p=pages[i]\n    print('=== leaf',i,'===')\n    print(p[:400].replace('\\n',' | '))\n    print('...')\n    print(p[-400:].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-04T18:30:20.226Z] TOOL RESULT

```
=== leaf 74 ===
ae  dies  usw.,  Jfowtag,  3)  fifiiga  'Aqiws,  Martis dies  usw.,  fi'anz.  marä\,  engl,  thtiesdaj,  deutsch  (dial.)  Äestag,  und  viell. doch  auch  Dienstag,  4)  ?/^/pa  'Egf/ov,  Mercurii  dies  usw.,  franz.  mercreAi, engl.  wednesAaj,  5)  nfxiqa  Ai.ög,  Jovis  dies  usw.,  engl,  thiirsdaj,  Donners- tag, 6)  ijf^^ga  'Aq)QoSlT>]g,  Veneris  dies  usw.,  i^mtag,  7)  i'jfii'^a  Kqöv
...
ach  Sechzigern  allerdings  im  letzten  Grunde  auf das  babylonische  Sexagesimalsysteni  zui'ückgehen  wird. | 17.   Religion,  Kultus  und  Mythus. | akk.  palähu  sich  fürchten  vor,   dann  spez.   (die  Götter)   fürchten, verehren,  ihnen  dienen  :  >-  wohl  aram.  pdlah  (Gott)  verehren,  dienen, akk.  amäru  pän  ili  (wörtl.   das  Antlitz   des   Gottes  sehen)  vor  dem  Gotte ersche
=== leaf 75 ===
inen    :    davon   vieU.   beeinflußt    hebr.    raä   panim  in    Verb,    mit Jahwe.     Vgl.  auch  oben  S.  10  zu  akk.  dagälu  pän.  Zu  pers.-arab. | den,  dm  Keligion  s.  oben  S.  24  unter  akk.  denu. | akk.  Pa.  sullü  anflehen,  (^u  den  Göttern)  beten  :  (in  dieser  Bed.) ^  aram.  Pa.  salll  beten,  sdlötä^  Gebet  O  arab.  sallä  u.  salät,  äth.  sallaja u.  salöt).  ak
...
viell.  aram.  zalah  sprengen, und  viell.  darauf  zurückgehend  auch  hebr.  sälah  .(Sünde)  vergeben. | akk.  l:ap<rru  bestreichen  (z.  B.  mit  Erdpech,  laipru  s.  oben  S.  60), abwischen  (z.  B.  Tränen),  kulttechn.  l-uppiini  wischen,  bestreichen  (z.  B. einen  Kranken  mit  einer  Teigmasse),  dann  wohl  auch  in  allgemeinerem Sinne  reinigen  u.  ä.  :  darauf  wahrsch.  zurück
=== leaf 78 ===
 | akk.  eJcurru  Tempel  (<<  sum.  e-kur) :  >>  mand.  ehürä  (Götzen)tempel, ägypt.-aram.,  jüd.-aram.  'egOrä  Heiligtum,  Götzenaltar.  Zu  hebr.  usw. | heJcäl  i.  d.  (sekundären)  Bed.  Tempel  s.  oben  S.  8  zu  alvk.  eJcallu  Palast. | aklv.  asirtu,  esirtu  Heiligtum,  Tempel  (St.  wohl  wsr)  :  ]>  wohl  phön. 'srt  Heiligtum,  hebr.  'äserä  kultischer  Pfahl  u.  Bez.  für  eine  G
...
  wohl  südarab.  Mondgott  Sin;  auch im  aram.  (mand.,  liarran.)  ist  der  bab.  Gottesn.  noch  mehrfach  erhalten; vgl.  auch  oben  S.  59  zu  syr.  slnä  Süber. | akk.  EresJcigal  Name  der  ünterweltsgöttin,  als  'Egta^iyal  in  griech. Zauberpapyrus  erhalten. | Zu  akk.  Siris.  eine  Göttin,  s.  oben  S.  40  unter  siröMu  Most. | akk.  Mribu  wörtl.  segnend.  Bez.  der  Stierkolosse
```


## [2026-09-04T18:30:37.560Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 برکت ===\"; grep -n \"برکت\\|برکات\" BQT_v1_pages.txt | head\necho \"=== BQT v2 letter range sample ===\"; sed -n '1,5p' BQT_v2_pages.txt; grep -n \"زمرد\\|ز مرد\\|زمر د\" BQT_v2_pages.txt|head -3\necho \"=== BQT v2 headword-ish زمرد ===\"; grep -c \"\" BQT_v2_pages.txt\necho \"=== BQT v3 کروبی ===\"; grep -n \"کروبی\\|کروبیان\\|کروبیون\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt | head"
}
```


### [2026-09-04T18:30:37.694Z] TOOL RESULT

```
=== BQT v1 برکت ===
20283:فلناق‌است که طاقبه و کلامو فرجی- وبرکتوان
=== BQT v2 letter range sample ===
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
601: ‫شرابخوارهم هت‬         ‫و کنانه از مردم‬             ‫گونند‬        ‫(‪)۱‬‬     ‫میشود و در آبپای استاده روید و»‏گل آن‬
2382:       ‫ز زمرد ‪.‬‬     ‫و اندر دم اوسبز جلیلی‬         ‫‪ -۳۴۲‬بر گردرخش(سیب)یر‪ ,‬قطی‌چند زد‬
2518:‫است معروف که او را عربان متوشلخ کویند ‪.‬‬         ‫مائند لمل ‪ - ۱‬کونایه ازمردم بداسل و جاهل‬
=== BQT v2 headword-ish زمرد ===
41071
=== BQT v3 کروبی ===
incoming/BQT/BQT_v4_pages.txt:21409:-1۳-< یکروبی
```


## [2026-09-04T18:30:39.064Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD 600-610 raw ===\"; sed -n '598,610p' TAD_pages.txt\necho \"=== AFM ز section ===\"; grep -n \"زبرجد\\|الزبرجد\\|زمر\" AFM_pages.txt | head -10\necho \"=== AFM karubi ===\"; grep -n \"كروب\\|كاروب\" AFM_pages.txt | head"
}
```


### [2026-09-04T18:30:39.205Z] TOOL RESULT

```
=== TAD 600-610 raw ===
 ‫وتقة وودقة ودوطة وبوانة ‏ فارسي ‪ 2‬لوده » وهو وعاء يديب الصائغ‬



             ‫وق ‪ -‬لاتيني ودأءعمط مرادفه الصور والناقور والتقير تفخ فيها‬

  ‫تق من برق أي لمم فنقل من العربية الى اللاتينية وبناا »«ة؟وط‬
         ‫‪5‬‬       ‫‪03‬‬       ‫‪5‬‬             ‫‪0‬‬      ‫‪ 59‬ع‬   ‫‪-‬‬     ‫‪75‬‬       ‫ع‬

                                                            ‫مرقش‪-‬‬
                                                                ‫بو‬
 ‫الحامض البورفي والنطرون منهطبيعي‬   ‫والىالفارسية « بوره ‪ 6‬وهو ملح حاصل من‬

=== AFM ز section ===
2276:(ܥܦܪܐ) وا را (ܚܡܪܐ) وتنا ] (ܛܝܢܐ) ;̈ܕ ,0 (ܦܟܬܪ) وزمرونتن (ܙܡܪ)
=== AFM karubi ===
```


## [2026-09-04T18:30:59.414Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '84550,84576p' WEB_vol1.txt | cut -c1-900\necho \"=== WEB emerald full ===\"; sed -n '63553,63558p' WEB_vol1.txt | cut -c1-800"
}
```


### [2026-09-04T18:30:59.515Z] TOOL RESULT

```
2. showing or characterized by grief; as, a grievous cry.
3. causing physical suffering; hard to bear; severe; as, grievous pain.
4. deplorable; atrocious; as, crime.
griév’/ous-ly, adv. in a grievous manner.
griév’ous-ness, 7, the state or quality of being grievous.
griff, n. [G. grif, a grasp, grip.]
1. grasp. [Obs.]
2. a device in a Jacquard loom to shift the Warp threads.
griff, n. same as griffin.
griff, n. a rocky chasm. [Brit. Dial.]
exif, grifi, z. [Fr.; Am. Sp. grifo, orig., grif-
a grievous
Dia child of a Negro and a mulatto. Z a E el . @ person of Ne; i i
cee Dia) gro and American Indian grif fawn’, n. in Ireland, a turf spade hav-
pren iron wing on one side of the blade
so ape the soft peat, as it is dug from the erties into square form before drying.
an pies (OFr. grife, a claw, nail, talon, from
Brifan, cS Sone EraSD GEZE from O.H.G.
base et a eee clawlike ornament at the
griffe, “oe - bottling. ° deposit in new wine soon after
a Gr ture; L. gryps:
ooked beak, f ary, rom curved] ected,
+ m mythol wnaginary animal cea legs of a ioe
nd the hea, ,
d and win
Ha Wings of an eagle.
TAT valtsentation of this aa heraldry, ture, Gyps fulvus, found in the
=== WEB emerald full ===
em/ér-Ald, n. (ME. emeraude; OFr. esmeraude, esmeralde; L. smaragdus; Gr. smaragdos, maragdos, a precious stone supposed to be the emerald.] p í
1. a precious stone of the beryl variety, 01 @ rich green color and highly valued, ranking with the diamond and ruby as one of the most costly gems.
2. a similar variety of corundum.
3. a rich, bright green color. il
4. a printing type, in size between nonparel and minion, about 6!/: point. Ree ai
em/ér-Ald, a. 1. having the characteristics an emerald; especially of a typical Breer nas
```


## [2026-09-04T18:31:24.999Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef leafof(path, keys, off=None):\n    t=open(path,encoding='utf-8',errors='replace').read()\n    pg=t.split('\\f')\n    for i,p in enumerate(pg):\n        for k in keys:\n            if k in p:\n                print(path.split('/')[-1], '| key',repr(k[:30]),'| leaf(0-based)',i, ('printed %s'%(i-off) if off is not None else ''))\nleafof('SKT.txt',['Cherub.  (Heb.)','OrifSn.  GrifTon','Emerald,  a  green  gem'],20)\nleafof('LKT.txt',['222.  Ar.  baraka','2233.  Pers.  zniniirud','257.  Ar.  barük'],26)\nleafof('LAT.txt',['gryphus, -I a .(grifus','smaragdus (zna-)'],18)\nEOF"
}
```


### [2026-09-04T18:31:26.887Z] TOOL RESULT

```
SKT.txt | key 'Cherub.  (Heb.)' | leaf(0-based) 99 printed 79
SKT.txt | key 'Emerald,  a  green  gem' | leaf(0-based) 156 printed 136
SKT.txt | key 'OrifSn.  GrifTon' | leaf(0-based) 208 printed 188
LKT.txt | key '222.  Ar.  baraka' | leaf(0-based) 46 printed 20
LKT.txt | key '257.  Ar.  barük' | leaf(0-based) 48 printed 22
LKT.txt | key '2233.  Pers.  zniniirud' | leaf(0-based) 206 printed 180
LAT.txt | key 'gryphus, -I a .(grifus' | leaf(0-based) 524 printed 506
LAT.txt | key 'smaragdus (zna-)' | leaf(0-based) 1130 printed 1112
```


## [2026-09-04T18:33:06.658Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt',encoding='utf-8',errors='replace').read()\npg=t.split('\\f')\nfor i,p in enumerate(pg,1):\n    if 'كروبين' in p or 'وشاروبين' in p: print('cherubim leaf',i,'printed ~',i-5)\n    if 'زبرجد' in p: print('zabarjad leaf',i,'printed ~',i-5)\n    if 'مرادفه الصور والناقور' in p: print('buq leaf',i,'printed ~',i-5)\nEOF\necho \"=== MON barakat exact line ===\"; grep -n \"بسرکت\\|برکت: \" MON_part1.txt | head\nawk 'NR>=22566 && NR<=22572 {print NR\": \"$0}' MON_part1.txt"
}
```


### [2026-09-04T18:33:08.391Z] TOOL RESULT

```
buq leaf 18 printed ~ 13
zabarjad leaf 36 printed ~ 31
cherubim leaf 66 printed ~ 61
=== MON barakat exact line ===
22568:بسرکت: 32( [ع. ی 2 (مسص‌ل ( 
22566: ببرکایوز: 7- 0۵۲۰۵6 [< بر کابوس ِ- 
22567: بر کافوز] (امر.) پیرامون دهان؛ پکث و پوز. 
22568: بسرکت: 32( [ع. ی 2 (مسص‌ل ( 
22569: گوالیدن. فزونی» بسیاری. خجستگی» یمن. 
22570: نیکختی» » سعادت؛ ج. برکات. 
22571: 
22572: بر کردن: ۸۵۵ (مصم.) بلند کر دن»
```


## [2026-09-04T18:33:13.471Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 -c \"\nimport json\nd=json.load(open('page-101.json'))\nfor e in d['entries']:\n  for n in e['nodes']:\n    for r in n.get('ref_check',[]):\n      if r['ref'].startswith('MON') or r['ref'].startswith('SKT'):\n        print(e['entry'],n['id'],r['ref'],r['status']); print('   ',r['note'][:400])\n\""
}
```


### [2026-09-04T18:33:15.097Z] TOOL RESULT

```
0 5 MON:2958 supports
    vajehyab.com (Mo'in) s.v. کروبی: '(کَ یّ) [ع.] (اِ.) فرشتة مقرب درگاه. ج. کروبیون' — tagged Arabic; Mo'in's page numbers cannot be mapped online. Archived https://vajehyab.com/?q=کروبی&d=moein.
0 6 MON:2958 supports
    vajehyab.com (Mo'in) s.v. کروبی [ع.] 'فرشتة مقرب درگاه، ج. کروبیون'; also کروبیان 'فرشتگان مقرب درگاه' and کروبیون 'جِ کروبی' — the Persian word is marked as an Arabic loan, as the arrow says (archived https://vajehyab.com/?q=کروبی&d=moein).
1 5 MON:1746 supports
    vajehyab.com (Mo'in) s.v. زمرد: '(زُ مُ رُّ) [معر - یو.] (اِ.) یکی از سنگ های قیمتی به رنگ سبز' — Mo'in tags it 'Arabicized, from Greek' (page numbers of the print edition cannot be mapped online). Mo'in's tag [معر - یو.] = Arabicized (mu'arrab) from Greek, i.e. Greek → Arabic → Persian, which is the route drawn through this empty Arabic node. Archived https://vajehyab.com/?q=زمرد&d=moein.
1 6 MON:1746 supports
    vajehyab.com (Mo'in) s.v. زمرد: '(زُ مُ رُّ) [معر - یو.] (اِ.) یکی از سنگ های قیمتی به رنگ سبز' — Mo'in tags it 'Arabicized, from Greek' (page numbers of the print edition cannot be mapped online). Archived https://vajehyab.com/?q=زمرد&d=moein.
1 11 SKT:163 partial
    SKT.txt leaf 156 (Skeat 1911 p. ~136; Nourai's 163 is another printing), s.v. Emerald: '(F. — L. — Gk.) M.E. emeraude — O.F. esmeraude — L. smaragdum, acc. of smaragdus — Gk. smaragdos, an emerald. Cf. Skt. marakata (the same).' Skeat only compares Skt. marakata with the Greek word; he does not say it is a Semitic loan.
```


## [2026-09-04T18:33:18.231Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,keys in [('FSD_vol1.txt',[\"&   Poet.  The  representation  of  a   beautiful  winged  child\"]),\n               ('FSD_vol2.txt',[\"5.  (1)  Agriffin'Viilture\",\"cni'cr-ald,  1   ein'sr-eld\"]),\n               ('FSD_vol4.txt',[\"(<  L   smaragdinus\"]),\n               ('WEB_vol1.txt',[\"cher’ub, .;\",\"em/ér-Ald, n. (ME. emeraude\",\"grif/fon, n. 1. a griffin.\"])]:\n    t=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/'+f,encoding='utf-8',errors='replace').read()\n    pg=t.split('\\f')\n    for i,p in enumerate(pg):\n        for k in keys:\n            if k in p: print(f,'leaf',i,'key',k[:25])\nEOF"
}
```


### [2026-09-04T18:33:20.514Z] TOOL RESULT

```
FSD_vol1.txt leaf 516 key &   Poet.  The  represent
FSD_vol2.txt leaf 80 key cni'cr-ald,  1   ein'sr-e
FSD_vol2.txt leaf 365 key 5.  (1)  Agriffin'Viiltur
FSD_vol4.txt leaf 154 key (<  L   smaragdinus
WEB_vol1.txt leaf 340 key cher’ub, .;
WEB_vol1.txt leaf 625 key em/ér-Ald, n. (ME. emerau
WEB_vol1.txt leaf 841 key grif/fon, n. 1. a griffin
```


## [2026-09-04T18:33:39.039Z] TOOL CALL #47: Bash

```json
{
 "command": "grep -n \"consulted\" tools/verify_check.py | head -20"
}
```


### [2026-09-04T18:33:39.085Z] TOOL RESULT

```
79:                for c in vn.get("consulted") or []:
86:    print("books consulted:", dict(con_tally), "| by book:", dict(con_books.most_common(40)))
```


## [2026-09-04T18:33:40.679Z] TOOL CALL #48: Bash

```json
{
 "command": "sed -n '55,95p' tools/verify_check.py"
}
```


### [2026-09-04T18:33:40.738Z] TOOL RESULT

```
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
```


## [2026-09-04T18:33:43.322Z] AGENT

Now I'll write the `consulted` arrays into the file.


## [2026-09-04T18:36:37.110Z] TOOL CALL #49: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/add101.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nP = \"/home/sfmqrb/git/rishe/data/verification/page-101.json\"\nd = json.load(io.open(P, encoding=\"utf-8\"))\n\ndef C(src, where, stance, note):\n    return {\"src\": src, \"where\": where, \"stance\": stance, \"note\": note}\n\n# ---------- reusable quotes ----------\nAKD_KARABU = (\"AKD.txt \\\\f-leaf 75 (Zimmern p. ~66, §17 'Religion, Kultus und Mythus'; grep -n 'segnen' AKD.txt): \"\n  \"'akk. karābu segnen, beten : ~ viell. doch, trotz anderer Möglichkeiten, südarab. krb segnen, khrb weihen, \"\n  \"mkrb (auch noch heute mikrāb) Heiligtum, Tempel (> wohl äth. mekwrāb Heiligtum).'\")\nAKD_KARIBU = (\"AKD.txt \\\\f-leaf 78 (Zimmern p. ~69; grep -n 'Mribu  wörtl' AKD.txt): \"\n  \"'akk. kāribu wörtl. segnend. Bez. der Stierkolosse : > wohl (aus einer Nebenf. karūbu) hebr. kərūb Cherub. \"\n  \"Fraglich, ob dazu auch γρύψ, gryphus, Greif gehört.'\")\nAKD_BARRAQTU = (\"AKD.txt \\\\f-leaf 69 (Zimmern p. 59-60; grep -n 'barraqtu' AKD.txt): \"\n  \"'[akk. barraqtu ein Edelstein, auch im Akk. Fremdw., spät und vereinzelt belegt : zunächst viell. > späthebr. \"\n  \"bāraqet, barqat, angeblich Smaragd. Fraglich, ob das Wort semit. Ursprungs (dann zu St. brq blitzen); \"\n  \"idg. entspricht skr. marakata, griech. μάραγδος, σμάραγδος usw., Smaragd.]'\")\nLKT_BARAKA = (\"LKT.txt \\\\f-leaf 46 = printed p. 20, no. 222: 'Ar. baraka: \\\"Segen (nämlich Gottes)\\\", ebenso tk. bereket \"\n  \"\\\"dass., Fruchtbarkeit\\\"; hieraus rum. berechet \\\"Fülle, Fruchtbarkeit\\\"; bulg. bereket \\\"Überfluß\\\", serb. bericet \"\n  \"\\\"Glück, Überfluß\\\".'\")\nLKT_ZUM = (\"LKT.txt \\\\f-leaf 206 (printed p. ~174/180), no. 2233: 'Pers. zumurrud: \\\"Smaragd\\\" [vielleicht aus gr. \"\n  \"σμάραγδος, wahrscheinlich beides aus dem Ind.], ebenso tk. zümrüd; hieraus bulg. zumrud, russ. izumrud \\\"Smaragd\\\".'\")\nSKT_CHERUB = (\"SKT.txt \\\\f-leaf 99 = Skeat p. 79, s.v. Cherub: 'Cherub. (Heb.) The true pl. is cherub-im, = Heb. kərūb \"\n  \"(pl. kərūbīm), a mystic figure.'\")\nSKT_GRIFFIN = (\"SKT.txt \\\\f-leaf 208 = Skeat p. 188, s.v. Griffin, Griffon: '(F.—L.—Gk.) Better griffon. M.E. griffon. \"\n  \"F. griffon; formed from Low L. griffus, a griffon. — L. gryphus, extended form of gryps, a griffon. — Gk. γρύψ \"\n  \"(stem γρυπ-), a griffon, a fabulous animal supposed to have a hooked beak. — Gk. γρυπός, curved, hook-beaked.'\")\nSKT_EMERALD = (\"SKT.txt \\\\f-leaf 156 = Skeat p. 136, s.v. Emerald: '(F.—L.—Gk.) M.E. emeraude — O.F. esmeraude — \"\n  \"L. smaragdum, acc. of smaragdus — Gk. σμάραγδος, an emerald. Cf. Skt. marakata (the same).' and s.v. smaragdus: \"\n  \"'(L.—Gk.) L. smaragdus (above).'\")\nFSD_GRIFFIN = (\"FSD_vol2.txt \\\\f-leaf 365, s.v. griffin: '[< F. griffon, < LL. gryphon-, < gryphus, < L. gryps, \"\n  \"fabulous creature, < Gr. gryps, < grypos, hooked.]'\")\nWEB_GRIFFIN = (\"WEB_vol1.txt \\\\f-leaf 841, s.v. griffin/griffon: '[... L. gryps; ... Gr. grypos, ... hooked beak, \"\n  \"from ... curved] ... in mythology, an imaginary animal with the legs of a lion and the head and wings of an eagle.'\")\nWEB_EMERALD = (\"WEB_vol1.txt \\\\f-leaf 625, s.v. emerald: '[ME. emeraude; OFr. esmeraude, esmeralde; L. smaragdus; \"\n  \"Gr. smaragdos, maragdos, a precious stone supposed to be the emerald.]'\")\nWEB_CHERUB = (\"WEB_vol1.txt \\\\f-leaf 340, s.v. cherub: '[ME. cherub; ... L. cherub; ... [Heb.] kerūb, a cherub.] \"\n  \"a winged heavenly [being] ... Ezek. i. 5-11.'\")\nFSD_CHERUB = (\"FSD_vol1.txt \\\\f-leaf 516, s.v. cherub: '3. One of an order of angelic beings ranking second to the \"\n  \"seraphim in the celestial hierarchy ... [LL., < Heb. kᵉrubh, cherub.]'\")\nLAT_GRYPHUS = (\"LAT.txt \\\\f-leaf 524 (Ernout-Meillet p. ~506), s.v. gryphus: 'gryphus, -ī m. (grifus, etc.): \"\n  \"latinisation tardive et vulgaire du nom grec du griffon, γρύψ, transcrit gryps par la l. littéraire.'\")\nLAT_SMARAGDUS = (\"LAT.txt \\\\f-leaf 1130 (Ernout-Meillet, s.v. smaragdus): 'smaragdus (zma-), -ī m.: émeraude. \"\n  \"Emprunt au gr. σμάραγδος, depuis Varr. et Lucr., M.L. 8041; smaragdinus, -dineus.'\")\nPLA_ZUM = (\"PLA_pages.txt \\\\f-leaf 162 = Asbaghi printed p. 147 (running head 'zambaq 147 zanādiqa'), s.v. zumurud: \"\n  \"'zumurud: \\\"Smaragd\\\" pers. … aus pers. زمرد zomurrod, mp. [ʾwzmbwlt] uzmburt < *zmaurd zmagrd mit Metathese \"\n  \"v. zmargd, s. zibargad, griech. σμάραγδος, syr. zmargdā, ar. zumurrud, russ. izmrud'; and 'zumurrud = zumurud q. v.'\")\nTAD_CHERUBIM = (\"TAD_pages.txt \\\\f-leaf 66 (al-Unaysi printed p. ~61), s.v. كروبيم وكروبين وشاروبين: \"\n  \"'كروبيم وكروبين وشاروبين — في العبرانية «كروب» … وهم يمثلون الملائكة … أصل هذا اللفظ أشوري ومعناه حارس، \"\n  \"لأن سكان شنعار في بابل كانوا يصورون … ثوراً ذا أجنحة يحرس الأبواب والمداخل.'\")\n\n# ---------- entry 0 ----------\ne0 = d[\"entries\"][0]\ne0[\"consulted\"] = [\n  C(\"AKD\", \"p. ~66 (\\\\f-leaf 75) s.v. akk. karābu\", \"partial\", AKD_KARABU +\n    \" — Zimmern keeps k-r-b as an independent Semitic root (Akkadian ~ South Arabian krb 'to bless'); he nowhere \"\n    \"derives it from, or equates it with, b-r-k, so the 'letters interchanged' premise of this chart is absent from him.\"),\n  C(\"LKT\", \"printed p. 20, no. 222\", \"partial\", LKT_BARAKA +\n    \" — Lokotsch confirms Arabic baraka 'blessing (of God)' and its spread (Turkish bereket → Balkan), but says \"\n    \"nothing about an original 'to kneel' sense or about a k-r-b variant.\"),\n  C(\"AFA\", \"whole text (grep -n -i 'barak|berak|kerub|karub|Segen' AFA.txt)\", \"silent\",\n    \"No hit. Fraenkel's 'Aramäische Fremdwörter im Arabischen' has no b-r-k article — consistent with the root \"\n    \"being native common Semitic rather than an Aramaic loan into Arabic, but he offers no independent evidence here.\"),\n]\nn0 = {n[\"id\"]: n for n in e0[\"nodes\"]}\n\nn0[1][\"consulted\"] = [\n  C(\"LKT\", \"printed p. 20, no. 222 and p. 22, no. 257\", \"supports\", LKT_BARAKA +\n    \" Also no. 257: 'Ar. barūk: [Vom Vb. baraka \\\"segnen\\\": vulgär:] \\\"Geschenk\\\"; hieraus mit dem ar. Art. sp. \"\n    \"alboroc, alboroque.' Lokotsch takes Arabic baraka 'to bless' / baraka(t) 'blessing' as the base word, as the chart does.\"),\n  C(\"TAD\", \"grep -n 'بركة' TAD_pages.txt (only line 1997, 'حوض وبركة وقبوة')\", \"silent\",\n    \"Al-Unaysi's dictionary of loanwords in Arabic has no b-r-k headword; the only occurrence of بركة is the \"\n    \"homonym 'pool' inside another article. Treating b-r-k as native Arabic is itself weak confirmation of the chart.\"),\n  C(\"AFM\", \"grep -n 'برك|بركة' AFM_pages.txt\", \"silent\",\n    \"Addi Shir's list of Persian words arabicised contains no b-r-k entry, i.e. he does not regard baraka/barakat \"\n    \"as a Persian loan — compatible with the chart's Semitic root.\"),\n]\n\nn0[2][\"consulted\"] = [\n  C(\"MON\", \"MON_part1.txt line 22568 s.v. برکت\", \"supports\",\n    \"'برکت: [ع. برکة] (مص ل.) گوالیدن. فزونی، بسیاری. خجستگی، یمن. نیکبختی، سعادت؛ ج. برکات.' — Mo'in tags the \"\n    \"Persian headword [ع. برکة], i.e. Arabic baraka(t), exactly the borrowing the chart draws, and gives the plural barakāt.\"),\n  C(\"HRN\", \"grep -n -i 'barak|Segen|barq' HRN.txt\", \"silent\",\n    \"Horn's Grundriss has no barakat article: he deliberately excludes Arabic loanwords from Persian etymology, \"\n    \"so his silence is itself evidence that the word is not inherited Iranian.\"),\n  C(\"BQT\", \"grep -n 'برکت|برکات' BQT_v1_pages.txt (only OCR noise at line 20283)\", \"silent\",\n    \"No headword برکت recoverable from the Borhan-e Qate' vol. 1 page OCR.\"),\n  C(\"ARY\", \"grep -n 'برکت' incoming/ARY/ARY_pages.txt\", \"silent\",\n    \"Aryanpur's dictionary of Indo-European roots of Persian has no entry — consistent with an Arabic, non-IE loan.\"),\n]\n\nn0[3][\"consulted\"] = [\n  C(\"AKD\", \"p. ~66 (\\\\f-leaf 75) s.v. akk. karābu\", \"partial\", AKD_KARABU +\n    \" — the Akkadian verb and its gloss 'segnen, beten' are confirmed, but Zimmern connects it with South Arabian \"\n    \"krb 'to bless' / mikrāb 'sanctuary', i.e. within k-r-b; he gives no metathesis of b-r-k.\"),\n  C(\"AKD\", \"p. ~69 (\\\\f-leaf 78) s.v. akk. kāribu\", \"supports\", AKD_KARIBU +\n    \" — supports the Akkadian → Hebrew cherub step of the chart (node 4), though again from the root k-r-b.\"),\n  C(\"MON\", \"MON_part2.txt line 22552 s.v. کروبی\", \"partial\",\n    \"'کروبی: [ع. آشوری، پاسبان] (اِ.) در تورات کروب (ج. کروبیم) به فرشتگانی اطلاق شده که …' — Mo'in traces the word \"\n    \"to Assyrian (Akkadian) but glosses the Assyrian etymon as پاسبان 'watchman, guard', not 'to bless'.\"),\n  C(\"TAD\", \"printed p. ~61 (\\\\f-leaf 66)\", \"partial\", TAD_CHERUBIM +\n    \" — al-Unaysi likewise makes the Assyrian source mean 'guardian' (of the winged bulls at Babylonian gateways), \"\n    \"not 'one who blesses'.\"),\n]\n\nn0[4][\"consulted\"] = [\n  C(\"AKD\", \"p. ~69 (\\\\f-leaf 78) s.v. akk. kāribu\", \"partial\", AKD_KARIBU +\n    \" — Zimmern derives Hebrew kərūb straight from Akkadian kāribu/*karūbu, so the cherub belongs to k-r-b; \"\n    \"berākhā (b-r-k) is not brought into the article at all.\"),\n  C(\"SKT\", \"Skeat p. 79 (\\\\f-leaf 99) s.v. Cherub\", \"silent\", SKT_CHERUB +\n    \" — Skeat gives the Hebrew word and nothing more; no link to b-r-k or to Akkadian.\"),\n  C(\"FSD\", \"FSD vol. 1, \\\\f-leaf 516, s.v. cherub\", \"silent\", FSD_CHERUB +\n    \" — Funk & Wagnalls stops at Hebrew kᵉrubh and offers no Semitic-root analysis.\"),\n  C(\"TAD\", \"printed p. ~61 (\\\\f-leaf 66)\", \"partial\", TAD_CHERUBIM +\n    \" — supports Hebrew kərūb as the source of the Arabic form and an Assyrian origin behind it, but with the \"\n    \"sense 'guard', which is against the 'bless' semantics of the chart's root box.\"),\n]\n\nn0[5][\"consulted\"] = [\n  C(\"TAD\", \"printed p. ~61 (\\\\f-leaf 66)\", \"supports\", TAD_CHERUBIM +\n    \" — al-Unaysi lists karūbīm/karūbīn among the foreign words of Arabic and takes them 'in Hebrew kərūb', \"\n    \"exactly the Hebrew → Arabic arrow of the chart.\"),\n  C(\"FVQ\", \"grep -n -i 'kerub|karub|cherub' FVQ_pages.txt\", \"silent\",\n    \"Jeffery has no entry: karūbī is not a Qur'anic word, so the Foreign Vocabulary of the Qur'an says nothing about it.\"),\n  C(\"AFM\", \"grep -n 'كروب|كاروب' AFM_pages.txt\", \"silent\",\n    \"Addi Shir does not list karūbī, i.e. he does not treat it as a Persian loan into Arabic.\"),\n]\n\nn0[6][\"consulted\"] = [\n  C(\"TAD\", \"printed p. ~61 (\\\\f-leaf 66)\", \"partial\", TAD_CHERUBIM +\n    \" — confirms the Arabic base karūbīn/karūbīm from Hebrew that Persian karrūbī continues, but adds the \"\n    \"Assyrian 'guard' etymology rather than a b-r-k 'bless' one.\"),\n  C(\"BQT\", \"grep -n 'کروبی|کروبیان|کروبیون' BQT_v3_pages.txt BQT_v4_pages.txt\", \"silent\",\n    \"No کروبی headword recoverable from the Borhan-e Qate' vols. 3-4 page OCR.\"),\n  C(\"ARY\", \"grep -n 'کروبی' incoming/ARY/ARY_pages.txt\", \"silent\",\n    \"Aryanpur has no entry — as expected for a Semitic loan in a dictionary of Indo-European roots.\"),\n]\n\nn0[7][\"consulted\"] = [\n  C(\"SKT\", \"Skeat p. 79 (\\\\f-leaf 99) s.v. Cherub\", \"supports\", SKT_CHERUB +\n    \" — English cherub straight from Hebrew kərūb, with the Hebrew plural kərūbīm behind cherubim, as the chart draws.\"),\n  C(\"FSD\", \"FSD vol. 1, \\\\f-leaf 516, s.v. cherub\", \"supports\", FSD_CHERUB +\n    \" — '[LL., < Heb. kᵉrubh]' gives the Late Latin intermediary of the chain and the same Hebrew source; \"\n    \"F&W also has the sense 'a beautiful child or infant: in allusion to the artists' type', i.e. Nourai's '(of love)'.\"),\n  C(\"WEB\", \"WEB vol. 1, \\\\f-leaf 340, s.v. cherub\", \"supports\", WEB_CHERUB +\n    \" — Webster's chain ME cherub < L cherub < Heb. kerūb, plus 'a representation of one of the cherubim … or a \"\n    \"chubby, rosy-faced child with wings, as in later art'.\"),\n]\n\nn0[8][\"consulted\"] = [\n  C(\"SKT\", \"Skeat p. 188 (\\\\f-leaf 208) s.v. Griffin, Griffon\", \"contradicts\", SKT_GRIFFIN +\n    \" — Skeat derives Gk. γρύψ inside Greek from γρυπός 'hook-beaked, curved'; no Semitic (kerūbh/karibu) source at all.\"),\n  C(\"FSD\", \"FSD vol. 2, \\\\f-leaf 365, s.v. griffin\", \"contradicts\", FSD_GRIFFIN +\n    \" — Funk & Wagnalls likewise ends the etymology at Gr. grypos 'hooked'.\"),\n  C(\"WEB\", \"WEB vol. 1, \\\\f-leaf 841, s.v. griffin/griffon\", \"contradicts\", WEB_GRIFFIN +\n    \" — Webster too traces the Greek noun to grypos 'curved, hook-beaked', with no Semitic step.\"),\n  C(\"AKD\", \"p. ~69 (\\\\f-leaf 78) s.v. akk. kāribu\", \"partial\", AKD_KARIBU +\n    \" — Zimmern, the standard collection of Akkadian loanwords, mentions the γρύψ/gryphus/Greif connection only to \"\n    \"call it 'fraglich' (questionable): the strongest Assyriological statement available is a doubt, not an assertion.\"),\n]\n\nn0[9][\"consulted\"] = [\n  C(\"LAT\", \"Ernout-Meillet s.v. gryphus (\\\\f-leaf 524, p. ~506)\", \"supports\", LAT_GRYPHUS +\n    \" — exactly the chart's Greek → Latin step, and it explains the -us form Nourai prints as the late/vulgar \"\n    \"Latinisation beside literary gryps.\"),\n  C(\"SKT\", \"Skeat p. 188 (\\\\f-leaf 208)\", \"supports\", SKT_GRIFFIN +\n    \" — 'L. gryphus, extended form of gryps' confirms the Latin form and its Greek source.\"),\n  C(\"LEW\", \"grep -n -i 'gryps|gryphus|grypus' LEW_1910.txt\", \"silent\",\n    \"Walde's Lateinisches etymologisches Wörterbuch (1910) has no gryphus article — it omits transparent Greek \"\n    \"loanwords, so it neither supports nor contradicts.\"),\n]\n\nn0[10][\"consulted\"] = [\n  C(\"SKT\", \"Skeat p. 188 (\\\\f-leaf 208)\", \"partial\", SKT_GRIFFIN +\n    \" — the Old French form Skeat gives is griffon (whence M.E. griffon), formed on Low Latin griffus; he knows no \"\n    \"'grifion', which supports treating the chart's spelling as a slip while the Latin → OF → English route stands.\"),\n  C(\"FSD\", \"FSD vol. 2, \\\\f-leaf 365, s.v. griffin\", \"partial\", FSD_GRIFFIN +\n    \" — again F. griffon < LL. gryphon-, i.e. the -on suffix form, not grifion.\"),\n  C(\"WEB\", \"WEB vol. 1, \\\\f-leaf 841\", \"partial\", WEB_GRIFFIN +\n    \" — Webster's separate headword 'griffon, n. 1. a griffin' records only the -on form.\"),\n]\n\nn0[11][\"consulted\"] = [\n  C(\"SKT\", \"Skeat p. 188 (\\\\f-leaf 208)\", \"supports\", SKT_GRIFFIN +\n    \" — 'Griffin. Griffon. (F.—L.—Gk.) Better griffon. M.E. griffon' — English from Old French, as the chart draws.\"),\n  C(\"FSD\", \"FSD vol. 2, \\\\f-leaf 365, s.v. griffin\", \"supports\", FSD_GRIFFIN +\n    \" — F&W's griffin: '5. (1) A griffin-vulture … [< F. griffon …]', the same French → English step, and it also \"\n    \"records the Anglo-Indian homonym griffin 'newcomer', which is a different word.\"),\n  C(\"WEB\", \"WEB vol. 1, \\\\f-leaf 841\", \"supports\", WEB_GRIFFIN +\n    \" — Webster's mythical griffin, 'an imaginary animal with the legs of a lion and the head and wings of an eagle', \"\n    \"matches Nourai's gloss 'an eagle-headed lion'.\"),\n]\n\n# ---------- entry 1 ----------\ne1 = d[\"entries\"][1]\ne1[\"consulted\"] = [\n  C(\"AKD\", \"Zimmern p. 59-60 (\\\\f-leaf 69), gemstone list\", \"partial\", AKD_BARRAQTU +\n    \" — Zimmern accepts a Semitic stem brq 'to flash' but doubts that the gem-name barraqtu belongs to it, and \"\n    \"treats barraqtu as itself a foreign word in Akkadian, which loosens the chart's root → gem chain.\"),\n  C(\"LKT\", \"grep -n -i 'baraka|barq' LKT.txt (b- series jumps 222 baraka → 224 baraṣ)\", \"silent\",\n    \"Lokotsch has no 'Ar. barq' number: no European word of his corpus derives from it, so he says nothing about the root.\"),\n  C(\"AFA\", \"grep -n -i 'smaragd|barq|Blitz' AFA.txt\", \"silent\",\n    \"Fraenkel's Aramaic loanwords in Arabic has no b-r-q article; the root is not an Aramaic loan for him.\"),\n]\nn1 = {n[\"id\"]: n for n in e1[\"nodes\"]}\n\nn1[1][\"consulted\"] = [\n  C(\"AKD\", \"Zimmern p. 59-60 (\\\\f-leaf 69)\", \"partial\", AKD_BARRAQTU +\n    \" — 'dann zu St. brq blitzen' concedes a Semitic root b-r-q 'to flash', the chart's Arabic node, while \"\n    \"questioning whether the gem-word is built on it.\"),\n  C(\"TAD\", \"grep -n 'برق' TAD_pages.txt — only incidental, printed p. ~13 (\\\\f-leaf 18) s.v. بوق\", \"silent\",\n    \"Al-Unaysi's dictionary of foreign words in Arabic has no b-r-q headword (it is native Arabic for him); the \"\n    \"root surfaces only inside the article on بوق: '… من برق أي لمع فنقل من العربية الى اللاتينية …', which at least \"\n    \"attests his gloss برق = لمع 'to gleam'.\"),\n  C(\"FVQ\", \"grep -n -i 'baraqa|barq' FVQ_pages.txt\", \"silent\",\n    \"Jeffery has no entry for barq: he treats it as native Arabic, not a Qur'anic foreign word.\"),\n]\n\nn1[2][\"consulted\"] = [\n  C(\"MON\", \"MON_part1.txt line 22544 s.v. برق\", \"supports\",\n    \"'برق: [ع.] (اِ.) درخش، درخشندگی، درخشش. جلای فلز. (فز.) جرقه‌ای که در اثر نزدیک شدن الکتریسیتهٔ منفی و مثبت تولید \"\n    \"شود، نوری که در اثر برخورد ابرها … تولید شود.' — Mo'in tags the Persian headword [ع.] = Arabic and gives both \"\n    \"'flash/lightning' and the modern physical sense, i.e. precisely the chart's 'lightning, electricity'.\"),\n  C(\"HRN\", \"grep -n -i 'barq' HRN.txt\", \"silent\",\n    \"Horn's Grundriss has no barq: Arabic loans are outside his scope, so its absence corroborates that the word \"\n    \"is not inherited Iranian.\"),\n  C(\"HUB\", \"grep -n -i 'barq|Blitz' HUB.txt\", \"silent\", \"Hübschmann's Persische Studien has no entry for barq.\"),\n  C(\"ARY\", \"grep -n 'برق' incoming/ARY/ARY_pages.txt (only برقی/برقرار in running text)\", \"silent\",\n    \"Aryanpur's Indo-European root dictionary gives برق no headword — consistent with a Semitic loan.\"),\n]\n\nn1[3][\"consulted\"] = [\n  C(\"AKD\", \"Zimmern p. 59-60 (\\\\f-leaf 69), in the list of Akkadian stone-names\", \"partial\", AKD_BARRAQTU +\n    \" — the standard handbook of Akkadian culture-words gives the form as barraqtu 'a gemstone' (not 'lightning'), \"\n    \"calls it late, isolated and itself a loanword in Akkadian, and questions its Semitic origin. That confirms the \"\n    \"verification's two reservations (the printed gloss and the placement of this node) without overturning the node.\"),\n  C(\"LKT\", \"grep -n -i 'baraqtu|barraqtu' LKT.txt\", \"silent\",\n    \"Lokotsch has no Akkadian gem-name entry; he starts the emerald family at Persian zumurrud (no. 2233).\"),\n  C(\"AFA\", \"grep -n -i 'baraqtu|Smaragd' AFA.txt\", \"silent\", \"Fraenkel does not treat the Akkadian gem-name.\"),\n]\n\nn1[4][\"consulted\"] = [\n  C(\"AKD\", \"Zimmern p. 59-60 (\\\\f-leaf 69)\", \"partial\", AKD_BARRAQTU +\n    \" — Zimmern's Greek forms are μάραγδος, σμάραγδος, which independently shows the chart's 'smaraldos' is a \"\n    \"misreading of -gd-; but he calls the Semitic origin of the whole group 'fraglich'.\"),\n  C(\"SKT\", \"Skeat p. 136 (\\\\f-leaf 156) s.v. Emerald\", \"supports\", SKT_EMERALD +\n    \" — confirms Gk. σμάραγδος 'an emerald' as the pivot of the whole branch (and again shows the spelling with -gd-).\"),\n  C(\"WEB\", \"WEB vol. 1, \\\\f-leaf 625, s.v. emerald\", \"supports\", WEB_EMERALD +\n    \" — Webster records both Greek variants smaragdos and maragdos, the pair Klein cites; nothing like 'smaraldos'.\"),\n  C(\"LKT\", \"printed p. ~174/180 (\\\\f-leaf 206), no. 2233\", \"contradicts\", LKT_ZUM +\n    \" — Lokotsch thinks the Greek word itself is 'wahrscheinlich … aus dem Ind.', i.e. Indic rather than Semitic, \"\n    \"which is against the chart's Semitic → Greek arrow.\"),\n]\n\nn1[5][\"consulted\"] = [\n  C(\"PLA\", \"Asbaghi printed p. 147 (\\\\f-leaf 162) s.v. zumurud/zumurrud\", \"contradicts\", PLA_ZUM +\n    \" — Asbaghi's book is a catalogue of PERSIAN loanwords in Arabic, and Arabic zumurrud is one of them: \"\n    \"Greek → (Syriac) → Middle Persian uzmburt → New Persian zomorrod → Arabic, the reverse of this node's outgoing arrow.\"),\n  C(\"LKT\", \"printed p. ~174/180 (\\\\f-leaf 206), no. 2233\", \"contradicts\", LKT_ZUM +\n    \" — Lokotsch files the word under 'Pers. zumurrud', not under Arabic, i.e. Persian is the donor language for \"\n    \"the Turkish/Slavic forms and not a receiver from Arabic.\"),\n  C(\"TAD\", \"printed p. ~31 (\\\\f-leaf 36) s.v. زبرجد\", \"partial\",\n    \"'زبرجد — في الفارسية «زبرجد» وهو حجر ثمين يشبه الزمرد' — al-Unaysi has no زمرد headword, but he classes the \"\n    \"sister gem-name zabarjad as Persian in Arabic, the same direction of borrowing Asbaghi gives for zumurrud.\"),\n  C(\"AFM\", \"grep -n 'زمرد|الزمرد' AFM_pages.txt\", \"silent\",\n    \"No recoverable headword in the Addi Shir page OCR (the ز section OCRs poorly).\"),\n]\n\nn1[6][\"consulted\"] = [\n  C(\"PLA\", \"Asbaghi printed p. 147 (\\\\f-leaf 162) s.v. zumurud\", \"contradicts\", PLA_ZUM +\n    \" — Asbaghi gives the Persian pre-history the chart lacks (Middle Persian ʾwzmbwlt uzmburt < *zmaurd, metathesis \"\n    \"of zmargd, beside Syriac zmargdā) and makes Arabic zumurrud the borrower from Persian. This is exactly the \"\n    \"reversal on which the node's 'disputed' verdict rests, now confirmed from a printed monograph, not only Wiktionary.\"),\n  C(\"LKT\", \"printed p. ~174/180 (\\\\f-leaf 206), no. 2233\", \"contradicts\", LKT_ZUM +\n    \" — the headword is 'Pers. zumurrud', and Turkish zümrüd, Bulgarian zumrud and Russian izumrud are taken from \"\n    \"Persian; no Arabic intermediary anywhere in the article.\"),\n  C(\"HRN\", \"grep -n -i 'Smaragd|zumurrud' HRN.txt (only no. 1011 mynw 'Himmel, Paradies; Smaragd')\", \"silent\",\n    \"Horn has no zumurrud article; his only 'Smaragd' is the unrelated Np. mīnā (no. 1011), so he is silent on this node.\"),\n  C(\"ARY\", \"grep -n 'زمرد' incoming/ARY/ARY_pages.txt\", \"silent\",\n    \"Aryanpur gives no Indo-European root for زمرد — consistent with a Wanderwort, not with an inherited Iranian word.\"),\n]\n\nn1[7][\"consulted\"] = [\n  C(\"LAT\", \"Ernout-Meillet s.v. smaragdus (\\\\f-leaf 1130)\", \"supports\", LAT_SMARAGDUS +\n    \" — Latin smaragdus is a straight borrowing of Greek σμάραγδος, attested from Varro and Lucretius, exactly the \"\n    \"chart's Greek → Latin arrow; the variant zma- also shows the initial-cluster trouble that produced the Romance forms.\"),\n  C(\"SKT\", \"Skeat p. 136 (\\\\f-leaf 156)\", \"supports\", SKT_EMERALD +\n    \" — 'smaragdus. (L.—Gk.) L. smaragdus' plus the emerald article's 'L. smaragdum, acc. of smaragdus — Gk. σμάραγδος'.\"),\n  C(\"LEW\", \"grep -n -i 'smaragd' LEW_1910.txt\", \"silent\",\n    \"Walde (1910) has no smaragdus article; like gryphus it is left out as a transparent Greek loan.\"),\n]\n\nn1[8][\"consulted\"] = [\n  C(\"FSD\", \"FSD vol. 4, \\\\f-leaf 154 (s.v. smaragd, smaragdine); FSD vol. 2, \\\\f-leaf 80 s.v. eclogite\", \"supports\",\n    \"vol. 4: 'smaragdine … Of the color of the smaragd; emerald-colored, green. [< L. smaragdinus, < smaragdus \"\n    \"(< Gr. smaragdos)]'; vol. 2 s.v. eclogite: 'Petrol. A rock consisting of red garnet, omphacite, and \"\n    \"emerald-green smaragdite.' Together these confirm both the Latin smaragdus base of the mineral name and that \"\n    \"smaragdite is the emerald-green amphibole of eclogite, i.e. Nourai's gloss and the naming motive.\"),\n  C(\"SKT\", \"grep -n -i 'smaragdite' SKT.txt\", \"silent\",\n    \"Skeat's concise dictionary has smaragdus but no mineralogical smaragdite.\"),\n  C(\"WEB\", \"WEB_vol1.txt (the local scan runs A–'memorial')\", \"silent\",\n    \"S is not in the available Webster volume, so Webster could not be consulted for this headword.\"),\n]\n\nn1[9][\"consulted\"] = [\n  C(\"WEB\", \"WEB vol. 1, \\\\f-leaf 625, s.v. emerald\", \"supports\", WEB_EMERALD +\n    \" — Webster lists esmeralde beside esmeraude as the Old French form, so the chart's spelling is an attested \"\n    \"variant and not a transcription error.\"),\n  C(\"SKT\", \"Skeat p. 136 (\\\\f-leaf 156)\", \"supports\", SKT_EMERALD +\n    \" — 'M.E. emeraude — O.F. esmeraude — L. smaragdum': the Latin → Old French step of the chart.\"),\n  C(\"LKT\", \"printed p. ~174/180 (\\\\f-leaf 206), no. 2233\", \"silent\",\n    \"Lokotsch follows only the Persian → Turkish → Slavic line and says nothing about the Romance forms.\"),\n]\n\nn1[10][\"consulted\"] = [\n  C(\"SKT\", \"Skeat p. 136 (\\\\f-leaf 156) s.v. Emerald\", \"supports\", SKT_EMERALD +\n    \" — M.E. emeraude from O.F. esmeraude, the chart's Old French → English arrow.\"),\n  C(\"WEB\", \"WEB vol. 1, \\\\f-leaf 625, s.v. emerald\", \"supports\", WEB_EMERALD +\n    \" — the same chain ME emeraude < OFr. esmeraude/esmeralde, with 'a precious stone of the beryl variety, of a \"\n    \"rich green color' for the gloss.\"),\n  C(\"LKT\", \"printed p. ~174/180 (\\\\f-leaf 206), no. 2233\", \"silent\",\n    \"Lokotsch does not treat English emerald (it reaches English through Romance, not through his oriental route).\"),\n]\n\nn1[11][\"consulted\"] = [\n  C(\"AKD\", \"Zimmern p. 59-60 (\\\\f-leaf 69)\", \"partial\", AKD_BARRAQTU +\n    \" — Zimmern puts Skt. marakata in the same group as Gk. μάραγδος/σμάραγδος ('idg. entspricht skr. marakata'), \"\n    \"i.e. he pairs the Sanskrit word with the Greek one rather than deriving it from the Semitic root, and doubts \"\n    \"the Semitic origin of the whole set — which is the reservation behind this node's 'plausible' verdict.\"),\n  C(\"LKT\", \"printed p. ~174/180 (\\\\f-leaf 206), no. 2233\", \"partial\", LKT_ZUM +\n    \" — Lokotsch goes further and suspects an Indian origin for the Greek word too ('wahrscheinlich beides aus dem \"\n    \"Ind.'), the opposite direction from the chart's Semitic → Sanskrit arrow.\"),\n  C(\"HJB\", \"grep -n -i 'marakata|smaragd' HJB.txt\", \"silent\",\n    \"Hobson-Jobson has no marakata article; 'emerald' occurs only inside quotations (e.g. Garcia da Orta 1568), \"\n    \"so it offers nothing on the Indian word's origin.\"),\n  C(\"SYN\", \"grep -n -i 'emerald|smaragd|marakata' SYN.txt\", \"silent\",\n    \"Buck's Selected Synonyms has no gem-name chapter covering 'emerald'.\"),\n  C(\"IEC\", \"grep -n -i 'smaragd|marakata' IEC.txt\", \"silent\",\n    \"Mann's Indo-European Comparative Dictionary has no entry — as expected, since neither he nor anyone else \"\n    \"reconstructs an IE etymon for marakata.\"),\n]\n\n# ---------- ref_check upgrades: MON now readable in the local scan ----------\nMON_KARRUBI = (\"Now checked in the printed text itself: MON_part2.txt line 22552 s.v. کروبی — \"\n  \"'کروبی: [ع. آشوری، پاسبان] (اِ.) در تورات کروب (ج. کروبیم) به فرشتگانی اطلاق شده که از حضور خدا فرستاده می‌شوند … \"\n  \"در اسلام آن را مهتران فرشتگان یا ملائکهٔ مقرب دانند؛ ج. کروبیون، کروبیین. ضبط: در شعر به تشدید راء آید و در تداول \"\n  \"فارسی نیز مشدد تلفظ شود.' The print gives more than the abridged web text: the bracket is [ع. آشوری، پاسبان], \"\n  \"i.e. Arabic, ultimately Assyrian 'watchman' — Mo'in does confirm the Hebrew/Assyrian cherub word behind the \"\n  \"Arabic loan, but glosses the Assyrian etymon 'guard', not 'bless'.\")\nfor nid in (5, 6):\n    for rc in n0[nid][\"ref_check\"]:\n        if rc[\"ref\"] == \"MON:2958\":\n            rc[\"note\"] = rc[\"note\"] + \" || \" + MON_KARRUBI + (\n              \" For node #6 it also settles the spelling: Mo'in states the rā' is geminated in Persian usage, \"\n              \"which is Nourai's karrūbī.\" if nid == 6 else \"\")\n\nMON_ZOMORROD = (\"Local print text located as well: MON_part1.txt line 71485 s.v. زمرد — 'زمرد: (اِ.) (زه.) یکی از \"\n  \"سنگ‌های قیمتی به رنگ سبز و آن هر چه پررنگ‌تر باشد گران‌بهاتر است. ضح. قدما می‌پنداشتند که نظر بر زمرد چشم افعی را \"\n  \"کور کند.' The etymological bracket that vajehyab renders [معر - یو.] is not legible in this OCR of the printed \"\n  \"page, so the 'Arabicized, from Greek' tag rests on the vajehyab text alone.\")\nfor nid in (5, 6):\n    for rc in n1[nid][\"ref_check\"]:\n        if rc[\"ref\"] == \"MON:1746\":\n            rc[\"note\"] = rc[\"note\"] + \" || \" + MON_ZOMORROD\n\nwith io.open(P, \"w\", encoding=\"utf-8\") as f:\n    json.dump(d, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/add101.py"
}
```


### [2026-09-04T18:36:39.592Z] TOOL RESULT

```
written
```


## [2026-09-04T18:36:41.572Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-101.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 101"
}
```


### [2026-09-04T18:36:43.325Z] TOOL RESULT

```
JSON OK
nodes verified: 22/22
node verdicts: {'confirmed': 13, 'plausible': 7, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 20, 'not_checked': 3, 'partial': 6}
books consulted: {'supports': 22, 'silent': 30, 'partial': 16, 'contradicts': 8} | by book: {'SKT': 11, 'LKT': 8, 'AKD': 8, 'WEB': 8, 'TAD': 7, 'FSD': 6, 'ARY': 4, 'AFM': 3, 'MON': 3, 'HRN': 3, 'BQT': 2, 'FVQ': 2, 'LAT': 2, 'LEW': 2, 'PLA': 2, 'HUB': 1, 'AFA': 1, 'HJB': 1, 'SYN': 1, 'IEC': 1}
```


## [2026-09-04T18:36:47.236Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-101.json'))\nbad=0\nfor e in d['entries']:\n    print('ENTRY',e['entry'],e['root'],'entry-consulted',len(e.get('consulted',[])))\n    for n in e['nodes']:\n        srcs={c['src'] for c in n.get('consulted',[])}\n        if len(srcs)<2: print('  !!',n['id'],srcs); bad+=1\n        else: print('  ok',n['id'],n['lang'],sorted(srcs))\nprint('bad',bad)\n\""
}
```


### [2026-09-04T18:36:49.286Z] TOOL RESULT

```
ENTRY 0 B.r.k entry-consulted 3
  ok 1 Arabic ['AFM', 'LKT', 'TAD']
  ok 2 Persian ['ARY', 'BQT', 'HRN', 'MON']
  ok 3 Akkadian ['AKD', 'MON', 'TAD']
  ok 4 Hebrew ['AKD', 'FSD', 'SKT', 'TAD']
  ok 5 Arabic ['AFM', 'FVQ', 'TAD']
  ok 6 Persian ['ARY', 'BQT', 'TAD']
  ok 7 English ['FSD', 'SKT', 'WEB']
  ok 8 Greek ['AKD', 'FSD', 'SKT', 'WEB']
  ok 9 Latin ['LAT', 'LEW', 'SKT']
  ok 10 Old French ['FSD', 'SKT', 'WEB']
  ok 11 English ['FSD', 'SKT', 'WEB']
ENTRY 1 B.r.q entry-consulted 3
  ok 1 Arabic ['AKD', 'FVQ', 'TAD']
  ok 2 Persian ['ARY', 'HRN', 'HUB', 'MON']
  ok 3 Akkadian ['AFA', 'AKD', 'LKT']
  ok 4 Greek ['AKD', 'LKT', 'SKT', 'WEB']
  ok 5 Arabic ['AFM', 'LKT', 'PLA', 'TAD']
  ok 6 Persian ['ARY', 'HRN', 'LKT', 'PLA']
  ok 7 Latin ['LAT', 'LEW', 'SKT']
  ok 8 English ['FSD', 'SKT', 'WEB']
  ok 9 Old French ['LKT', 'SKT', 'WEB']
  ok 10 English ['LKT', 'SKT', 'WEB']
  ok 11 Sanskrit ['AKD', 'HJB', 'IEC', 'LKT', 'SYN']
bad 0
```


## [2026-09-04T18:37:13.512Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-101.json` now carries a `consulted` array on all 22 nodes plus both root entries; `python3 tools/verify_check.py 101` reports **0 PROBLEM lines**.

**Consulted tally (76 entries):** supports 22 · silent 30 · partial 16 · contradicts 8.

**Books used** (20): SKT 11, LKT 8, AKD 8, WEB 8, TAD 7, FSD 6, ARY 4, AFM 3, MON 3, HRN 3, BQT 2, FVQ 2, LAT 2, LEW 2, PLA 2, HUB/AFA/HJB/SYN/IEC 1 each. Every node has ≥2 different books.

**Highest-value new findings**
- **AKD (Zimmern) p. ~66 & ~69**: `karābu segnen, beten : ~ südarab. krb segnen … mikrāb Heiligtum` and `kāribu wörtl. segnend, Bez. der Stierkolosse : > wohl (aus einer Nebenf. karūbu) hebr. kərūb Cherub. Fraglich, ob dazu auch γρύψ, gryphus, Greif gehört.` Zimmern keeps k-r-b as its own root (no b-r-k metathesis) and calls the griffin link doubtful — independent corroboration for the existing `plausible` verdicts on nodes #3, #4, #8.
- **AKD p. 59-60**: `akk. barraqtu ein Edelstein, auch im Akk. Fremdw., spät und vereinzelt belegt … Fraglich, ob das Wort semit. Ursprungs (dann zu St. brq blitzen); idg. entspricht skr. marakata, griech. μάραγδος, σμάραγδος` — confirms the gem-name gloss criticism, the `smaragdos` (not "smaraldos") reading, and the doubt behind node #11.
- **PLA (Asbaghi 1988) p. 147**: Arabic *zumurrud* is listed as a **Persian** loanword in Arabic, `aus pers. زمرد zomurrod, mp. uzmburt < *zmaurd, Metathese v. zmargd; griech. σμάραγδος, syr. zmargdā, ar. zumurrud, russ. izmrud` — printed-monograph confirmation of the `disputed` verdict on entry 1 node #6.
- **LKT no. 2233** files the word as *Pers. zumurrud* (and suspects an Indic source for the Greek), same direction.
- **SKT p. 188 / FSD vol. 2 / WEB vol. 1** all derive Greek γρύψ from γρυπός 'hook-beaked' — three independent `contradicts` for the Hebrew→Greek arrow (node #8), reinforcing but not overturning `plausible`.
- **WEB s.v. emerald** lists `OFr. esmeraude, esmeralde`, so the chart's *esmeralde* is an attested form, not a slip.

**ref_check upgrades** (2 refs, 4 items): `MON:2958` (entry 0 nodes #5, #6) and `MON:1746` (entry 1 nodes #5, #6) were previously checked only via vajehyab; both are now quoted from the local Mo'in text. The print gives more than the web: `کروبی: [ع. آشوری، پاسبان]` (Arabic ← Assyrian 'watchman') and Mo'in's note that the *rā'* is geminated in Persian usage, which validates Nourai's *karrūbī*. Conversely the printed زمرد entry's `[معر - یو.]` bracket is not legible in the local OCR, and I said so. The three `not_checked` items (FVA:45 ×2, SOR:35) stay — neither book has any digital copy.

**Verdict changes: none.** No book plainly overturned an existing verdict; every finding either corroborated the current reading or sharpened an already-recorded reservation. No new web pages were used, so `sources` is unchanged.
