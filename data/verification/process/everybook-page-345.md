# Verification process log — everybook-page-345


## [2026-09-04T19:16:27.142Z] INPUT

Task: bring an existing verification file up to the "consult every relevant book" rule. File: /home/sfmqrb/git/rishe/data/verification/page-345.json (roots Murvârît "pearl" — morvârîd, marjân, margarites, Margaret; and M.v.t "to die" — mawt, mât, kîš-mât/checkmate, Latin mattus, French mat, matador; 19 nodes). The chart with Nourai's citations is /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-345.txt.

Read /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md, in particular the sections "Use EVERY relevant book on disk", "Checking Nourai's OWN cited references" and "Process documentation", and the source matrix /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md (file paths of every local book — they all exist under /home/sfmqrb/git/rishe/data/verification/sources/refs/; the reference table /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json gives page offsets and lookup hints; scanned pages via tools/ref_page.py, e.g. BQT:1997 or BQT5:12).

For each root entry and for EVERY node: grep the books the matrix lists for that node's language (Pahlavi: MacKenzie PHD, Nyberg NYB; Persian: Horn HRN, Hübschmann HUB, Borhan BQT vols 1-5, Mo'in MON, Aryanpur ARY; Arabic/Aramaic loans: Klein KLN, Jeffery FVQ, Addi Shir AFM, Asbaghi PLA, Fraenkel AFA, Lokotsch LKT, Pihan PHN, Devic DEV, Lammens LAM; Greek/Latin/Romance/English: Klein, Skeat SKT, Funk & Wagnalls FSD, Webster WEB, Ernout-Meillet LAT, Walde LEW, Pokorny POK, Walde-Pokorny WLD, Watkins AHD; Sanskrit: Buck SYN, Mann IEC), and add a `consulted` array to the node exactly as specified: {"src","where","stance" (supports/contradicts/partial/silent),"note" with the quoted phrase}. At least two different books per node where the matrix lists two or more; "silent" entries count. Do not duplicate what is already in `ref_check` — but if a `ref_check` item is `not_checked`/`not_found` and the book is NOW on disk (Borhan vols 3-5, Asbaghi PLA, Walde-Pokorny 1-2; Ibrahim KGW and Nahvi FVA are not), re-check it and update its status/note. Do NOT change verdicts, derivations or sources unless a book plainly overturns the existing verdict; in that case update the verdict, append one sentence to `derivation`, and say so in your summary. If you use a web page, archive it with tools/fetch_source.py and add it to `sources`.

Write the file back in place (valid JSON, UTF-8). Run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 345` (0 PROBLEM lines; "books consulted" tally non-empty). Reply with a short summary: consulted entries by stance, books used, ref_check upgrades, and any verdict changes with reasons.


## [2026-09-04T19:16:28.896Z] AGENT

I'll start by reading the instructions, source matrix, and the target file.


## [2026-09-04T19:16:30.846Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:16:30.862Z] TOOL RESULT

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


## [2026-09-04T19:16:31.686Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T19:16:31.699Z] TOOL RESULT

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


## [2026-09-04T19:16:35.830Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-345.txt"
}
```


### [2026-09-04T19:16:35.893Z] TOOL RESULT

```
=== PDF page 345 (book page 315) ===
--- entry 0 ---
ROOT [Pahlavi] Murvârît : small pearl  (refs PLA:247; FVQ:261)
#1 (parent #0) [Persian] refs=BQT:1997; FVQ:261; KGW:112 | morvârîd «مروارید» : pearl | NOTE: BQT derives this word from Greek
#2 (parent #0) [Aramaic] refs=FVQ:261 | 
  #3 (parent #2) [Arabic] refs=FVQ:261; PLA:247 | mardjân : pearl, coral
    #4 (parent #3) [Persian] refs=BQT:1981 | marjân «مرجان» : coral
#5 (parent #0) [Greek] refs=AHD:1527; KGW:111; FVQ:261 | margarites : pearl
  #6 (parent #5) [Latin] refs=None | 
    #7 (parent #6) [Old French] refs=None | 
      #8 (parent #7) [English] refs=None | margarite, margarine, Margaret, Marjorie, Margarita, Maggie, Rita
--- entry 1 ---
ROOT Mus -> redirect to Mu
--- entry 2 ---
ROOT [Arabic] M.v.t : to die  (refs FVA:384; KLN:946)
#1 (parent #0) [Arabic] refs=FVA:387 | maot : death
  #2 (parent #1) [Persian] refs=FVA:387; MON:3678,4421 | mawt, mowt «موت ( مَمات )» : death ; mayyet «میّت» : dead person ; mât «مات» : dead, dull, confused ; kîš-mât «کیش مات» : "king is dead", checkmate ☞Ksei 1
    #3 (parent #2) [Latin] refs=FSD:1526 | mattus : dull, dead | NOTE: POK:694 derives Latin "mattus" from Indo-European root "Mad: wet".
      #4 (parent #3) [French] refs=FSD:1526 | mat : dull
        #5 (parent #4) [English] refs=FSD:526 | mat 1 : dull | NOTE: AHD:805 derives English "mat" from root "Mad".
      #6 (parent #3) [French] refs=PHN:257; DEV:159 | mat : defeated ; e'chec et mat : checkmate | NOTE: "checkmate" reached Europe through debatable paths
        #7 (parent #6) [English] refs=LKT:115; KLN:946 | mate 2 : to overcome ; checkmate
#8 (parent #0) [Spanish] refs=KLN:946 | matar : to kill ; matador : (bull) killer
  #9 (parent #8) [French] refs=MON:3678 | matador
    #10 (parent #9) [Persian] refs=MON:3678 | mâtâdor «ماتادُر»
  #11 (parent #8) [English] refs=KLN:946 | matador
```


## [2026-09-04T19:16:36.709Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-345.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:200])\nprint('entries',len(d['entries']))\nfor e in d['entries']:\n    print(e['entry'], e['root'], e['verdict'], 'nodes', len(e['nodes']))\n\""
}
```


### [2026-09-04T19:16:38.394Z] TOOL RESULT

```
{
 "pdf_page": 345,
 "book_page": 315,
 "verified_by": "claude-fable-5-1",
 "verified_on": "2026-09-04",
 "entries": [
  {
   "entry": 0,
   "root": "Murvârît",
   "verdict": "confirmed",
   "modern_f
entries 2
0 Murvârît confirmed nodes 8
2 M.v.t confirmed nodes 11
```


## [2026-09-04T19:16:40.513Z] TOOL CALL #5: Bash

```json
{
 "command": "cat data/verification/page-345.json"
}
```


### [2026-09-04T19:16:40.576Z] TOOL RESULT

```
<persisted-output>
Output too large (38.2KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bazzwq71m.txt

Preview (first 2KB):
{
  "pdf_page": 345,
  "book_page": 315,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "Murvârît",
      "verdict": "confirmed",
      "modern_form": "Middle Persian murwārīd (Book Pahlavi mwlwʾlyt', Manichaean mwrwʾryd) 'pearl' < Old Persian *margārīta- < Proto-Iranian *mŕ̥ga-ahri-ita- 'born of the (sea-)bird's shell, oyster'",
      "note": "Pahlavi murwārīd 'pearl' is real (MacKenzie 1971/1986; Nourai's -t reflects the Pahlavi spelling -yt'); gloss 'small pearl' is slightly narrow — MacKenzie simply 'pearl'. Modern scholarship (Wiktionary, Beekes s.v. μαργαρίτης, Encyclopaedia Iranica 'Greek loanwords in Middle Iranian') agrees the Iranian word is the SOURCE and Greek margaritēs the loan, so the chart's direction is right and the Borhan-e Qate' note (Persian from Greek) is rejected. One caveat: Greek margaritēs is already in Theophrastus (4th c. BCE), so the actual donor was Old Iranian *margārīta-, not Middle Persian proper; and the Aramaic/Arabic marjān branch runs through Greek (Syriac margānīṯā < Greek), not straight from Pahlavi. English margarine, Margarita and Rita do not pass through Old French.",
      "sources": [
        "https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%88%D8%A7%D8%B1%DB%8C%D8%AF",
        "https://en.wiktionary.org/wiki/%CE%BC%CE%B1%CF%81%CE%B3%CE%B1%CF%81%CE%AF%CF%84%CE%B7%CF%82",
        "https://www.etymonline.com/word/Margaret"
      ],
      "ref_check": [
        {
          "ref": "PLA:247",
          "status": "not_checked",
          "note": "PLA (Asbaghi, Persische Lehnwörter im Arabischen) is not online in full text (HathiTrust search-only)."
        },
        {
          "ref": "FVQ:261",
          "status": "supports",
...
</persisted-output>
```


## [2026-09-04T19:16:44.722Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-345.json'))\nfor e in d['entries']:\n    print('=== ENTRY',e['entry'],e['root'],e['verdict'])\n    print('ROOT ref_check:',json.dumps(e.get('ref_check'),ensure_ascii=False,indent=1))\n    print('ROOT consulted:',json.dumps(e.get('consulted'),ensure_ascii=False))\n    for n in e['nodes']:\n        print('--- node',n['id'],n['lang'],n.get('words'),n['verdict'])\n        print('  deriv:',n['derivation'][:400])\n        print('  refc:',json.dumps(n.get('ref_check'),ensure_ascii=False))\n        print('  cons:',json.dumps(n.get('consulted'),ensure_ascii=False))\n        print('  src:',n.get('sources'))\n\""
}
```


### [2026-09-04T19:16:46.533Z] TOOL RESULT

```
=== ENTRY 0 Murvârît confirmed
ROOT ref_check: [
 {
  "ref": "PLA:247",
  "status": "not_checked",
  "note": "PLA (Asbaghi, Persische Lehnwörter im Arabischen) is not online in full text (HathiTrust search-only)."
 },
 {
  "ref": "FVQ:261",
  "status": "supports",
  "note": "FVQ_pages.txt leaf 278 (Jeffery p. 261), s.v. Marjān: 'Small pearls. The word occurs only in a description of Paradise, and was early recognized as borrowed from Persia, but it is certain that it did not come directly from Iranian into Arabic. We find in Phlv. murvārīt, a pearl used, e.g. in the Gōsht-i-Fryānō, ii, 13 ... From Middle Persian the word was borrowed widely, e.g. Gk. margarites; Aram. margānītā; Syr. margānītā, and from some Aram. form it came into Arabic. It would have come at an early date for it is used in the old poetry ...' (fn. 5: 'In spite of Addai Sher, 144, and his attempted derivation from ...'; fn. 6 cites Horn, Grundriss 218 n.). Jeffery's Phlv. murvārīt is Nourai's root form."
 }
]
ROOT consulted: null
--- node 1 Persian morvârîd confirmed
  deriv: New Persian morvārīd مروارید continues Middle Persian murwārīd (mwlwʾlyt' / mwrwʾryd) unchanged apart from vowel adjustment; Parthian morγārīd, Sogdian mrγʾrt, Khotanese mrāhe are cognates, all from Old Iranian *margārīta-, which Beekes analyses as *mŕ̥ga-ahri-ita- 'oyster', literally 'born from the shell of a (sea-)bird' (*mr̥ga- 'bird', cf. Av. mərəγa-). Attested throughout classical poetry (Haf
  refc: [{"ref": "BQT:1997", "status": "not_checked", "note": "Borhan-e Qate' (Mo'in ed.) vols 3-5 are not online in full text (only vols 1-2 on archive.org). (BQT:1997 would be vol. 4)."}, {"ref": "FVQ:261", "status": "supports", "note": "FVQ_pages.txt leaf 278 (Jeffery p. 261), s.v. Marjān: 'Small pearls. The word occurs only in a description of Paradise, and was early recognized as borrowed from Persia, but it is certain that it did not come directly from Iranian into Arabic. We find in Phlv. murvārīt, a pearl used, e.g. in the Gōsht-i-Fryānō, ii, 13 ... From Middle Persian the word was borrowed widely, e.g. Gk. margarites; Aram. margānītā; Syr. margānītā, and from some Aram. form it came into Arabic. It would have come at an early date for it is used in the old poetry ...' (fn. 5: 'In spite of Addai Sher, 144, and his attempted derivation from ...'; fn. 6 cites Horn, Grundriss 218 n.). (Persian morvārīd is the NP continuation of the Phlv. murvārīt Jeffery quotes; fn. 6 cites Horn, Grundriss 218 n.)"}, {"ref": "KGW:112", "status": "not_checked", "note": "KGW (Ibrahim, Kulturgeschichtliche Wortforschung, 1991) is in copyright; Google Books preview only."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%88%D8%A7%D8%B1%DB%8C%D8%AF', 'https://en.wiktionary.org/wiki/%CE%BC%CE%B1%CF%81%CE%B3%CE%B1%CF%81%CE%AF%CF%84%CE%B7%CF%82', 'https://www.etymonline.com/word/Margaret']
--- node 2 Aramaic  plausible
  deriv: Pass-through node: the Aramaic word is Jewish Aramaic מַרְגָּנִיתָא / Syriac ܡܪܓܢܝܬܐ margānīṯā 'pearl' (with -n- for the Greek/Iranian -r-; dissimilation r…r > r…n). Wiktionary derives it from Greek μαργαρίτης, which in turn is the Iranian loan, so the ultimate source is the Iranian word as the chart says, but the immediate parent should be Greek rather than Pahlavi (a direct Iranian → Aramaic bor
  refc: [{"ref": "FVQ:261", "status": "supports", "note": "FVQ_pages.txt leaf 278 (Jeffery p. 261), s.v. Marjān: 'Small pearls. The word occurs only in a description of Paradise, and was early recognized as borrowed from Persia, but it is certain that it did not come directly from Iranian into Arabic. We find in Phlv. murvārīt, a pearl used, e.g. in the Gōsht-i-Fryānō, ii, 13 ... From Middle Persian the word was borrowed widely, e.g. Gk. margarites; Aram. margānītā; Syr. margānītā, and from some Aram. form it came into Arabic. It would have come at an early date for it is used in the old poetry ...' (fn. 5: 'In spite of Addai Sher, 144, and his attempted derivation from ...'; fn. 6 cites Horn, Grundriss 218 n.). 'From Middle Persian the word was borrowed widely, e.g. ... Aram. margānītā; Syr. margānītā, and from some Aram. form it came into Arabic' — the Aramaic intermediary of this empty node."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/%DC%A1%DC%AA%DC%93%DC%A2%DC%9D%DC%AC%DC%90', 'https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AC%D8%A7%D9%86']
--- node 3 Arabic mardjân confirmed
  deriv: Arabic marjān مَرْجَان 'small pearls; coral' (collective; unit noun marjāna) is borrowed from Classical Syriac margān 'pearl-like' / margānīṯā 'pearl' (Wiktionary), with Syriac g > Arabic j regularly. It is Qur'anic (55:22, 55:58 lu'lu' wa-l-marjān), where commentators already waver between 'small pearls' and 'coral' — the source of the double gloss. So the edge Aramaic → Arabic is confirmed.
  refc: [{"ref": "FVQ:261", "status": "supports", "note": "FVQ_pages.txt leaf 278 (Jeffery p. 261), s.v. Marjān: 'Small pearls. The word occurs only in a description of Paradise, and was early recognized as borrowed from Persia, but it is certain that it did not come directly from Iranian into Arabic. We find in Phlv. murvārīt, a pearl used, e.g. in the Gōsht-i-Fryānō, ii, 13 ... From Middle Persian the word was borrowed widely, e.g. Gk. margarites; Aram. margānītā; Syr. margānītā, and from some Aram. form it came into Arabic. It would have come at an early date for it is used in the old poetry ...' (fn. 5: 'In spite of Addai Sher, 144, and his attempted derivation from ...'; fn. 6 cites Horn, Grundriss 218 n.). Arabic marjān 'small pearls' from an Aramaic form of the Middle Persian word."}, {"ref": "PLA:247", "status": "not_checked", "note": "PLA (Asbaghi, Persische Lehnwörter im Arabischen) is not online in full text (HathiTrust search-only)."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AC%D8%A7%D9%86', 'https://en.wiktionary.org/wiki/%DC%A1%DC%AA%DC%93%DC%A2%DC%9D%DC%AC%DC%90']
--- node 4 Persian marjân confirmed
  deriv: Persian marjān مرجان 'coral' (also the female name Marjan) is borrowed from Arabic marjān, keeping only the 'coral' sense (Wiktionary: Persian and Ottoman Turkish 'adopted the Arabic term to mean coral specifically'); attested in Hafez alongside lu'lu' 'pearl' as in the chart's line. This is an Iranian → Greek → Aramaic → Arabic → Persian round trip, so morvārīd and marjān are doublets in Persian.
  refc: [{"ref": "BQT:1981", "status": "not_checked", "note": "Borhan-e Qate' (Mo'in ed.) vols 3-5 are not online in full text (only vols 1-2 on archive.org). (BQT:1981 would be vol. 4)."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AC%D8%A7%D9%86']
--- node 5 Greek margarites confirmed
  deriv: Greek μαργαρίτης (λίθος) margarítēs 'pearl' (first in Theophrastus, De lapidibus 36, 4th c. BCE; also μάργαρον) is, per Wiktionary/Beekes, a loan from Indo-Iranian, specifically the Old Iranian ancestor (*margārīta-) of Middle Persian murwārīd, with the Greek agent/material suffix -ίτης substituted for the Iranian ending; etymonline: 'from some Oriental language, most likely Iranian; cf. Middle Pe
  refc: [{"ref": "AHD:1527", "status": "supports", "note": "AHD_watkins1985.txt line 725: '[margarītēs. Pearl. Greek noun of Oriental origin (probably immediately from Iranian). Greek margarītēs, margaron, pearl: MARGARIC, MARGARIC ACID, (MARGARINE), MARGARITE1, MARGARITE2.]' Online AHD s.v. margarite (archived): 'Ultimately from Greek margarītēs, pearl, perhaps of Iranian origin; perhaps akin to Avestan mərəγa-, bird'. AHD:1527 is the 1976 appendix page of this same entry."}, {"ref": "KGW:111", "status": "not_checked", "note": "KGW (Ibrahim, Kulturgeschichtliche Wortforschung, 1991) is in copyright; Google Books preview only."}, {"ref": "FVQ:261", "status": "supports", "note": "FVQ_pages.txt leaf 278 (Jeffery p. 261), s.v. Marjān: 'Small pearls. The word occurs only in a description of Paradise, and was early recognized as borrowed from Persia, but it is certain that it did not come directly from Iranian into Arabic. We find in Phlv. murvārīt, a pearl used, e.g. in the Gōsht-i-Fryānō, ii, 13 ... From Middle Persian the word was borrowed widely, e.g. Gk. margarites; Aram. margānītā; Syr. margānītā, and from some Aram. form it came into Arabic. It would have come at an early date for it is used in the old poetry ...' (fn. 5: 'In spite of Addai Sher, 144, and his attempted derivation from ...'; fn. 6 cites Horn, Grundriss 218 n.). 'From Middle Persian the word was borrowed widely, e.g. Gk. margarites' (fn. 7: 'Also margaris ..., from which comes the Arm. margarit and the European forms')."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/%CE%BC%CE%B1%CF%81%CE%B3%CE%B1%CF%81%CE%AF%CF%84%CE%B7%CF%82', 'https://www.etymonline.com/word/Margaret']
--- node 6 Latin  confirmed
  deriv: Pass-through node: Latin margarīta 'pearl' (Cicero, Pliny; Vulgate Matt. 13:45–46 'pretiosa margarita'), a direct loan of Greek margarítēs with the Greek masculine -ítēs re-shaped as a Latin 1st-declension feminine -īta; Late Latin also as the female name Margarita.
  refc: [{"ref": "none", "status": "not_checked", "note": "Nourai cites no reference for this node. Klein (KLN_1966.txt leaf 504, s.v. margarite): 'ME., fr. OF. margarite (F. marguerite), fr. L. margarita, fr. Gk. margarites'."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/margarita', 'https://www.etymonline.com/word/Margaret']
--- node 7 Old French  confirmed
  deriv: Pass-through node: Old French margarite / marguerite 'pearl' and the name Margarete/Marguerite (12th–13th c.) from Latin margarīta (regular -a > -e, Latin g kept before a); Old French is the channel for English margarite, Margaret and Margery, but not for margarine, Margarita or Rita (see node 8).
  refc: [{"ref": "none", "status": "not_checked", "note": "Nourai cites no reference for this node. Klein (KLN_1966.txt leaf 504, s.v. margarite/Margaret): 'OF. margarite (F. marguerite), fr. L. margarita'; 'Margaret ... OF. Margaret, fr. L. margarita, pearl'."}]
  cons: null
  src: ['https://www.etymonline.com/word/Margaret', 'https://en.wiktionary.org/wiki/margarite']
--- node 8 English margarite, margarine, Margaret, Marjorie, Margarita, Maggie, Rita confirmed
  deriv: All seven go back to Greek margarítēs/Latin margarīta, but by different routes: margarite — Middle English 'pearl' (obsolete) from Old French margarite; the modern mineral sense (a calcium mica, 1820s) is a learned re-use with -ite. margarine — French margarine, coined by Chevreul (1813, acide margarique 'pearly acid', for the lustre of the crystals) from Greek margarítēs, then Mège-Mouriès' butte
  refc: [{"ref": "none", "status": "not_checked", "note": "Nourai cites no reference for this node. AHD_watkins1985.txt line 725 lists MARGARIC, MARGARINE, MARGARITE under margarītēs; Klein (leaf 504) s.v. Margaret 'fr. L. margarita, pearl' and s.v. margarine 'F.; ... fr. margarique ... fr. Gk. margaron, pearl'."}]
  cons: null
  src: ['https://www.etymonline.com/word/Margaret', 'https://www.etymonline.com/word/margarine', 'https://en.wiktionary.org/wiki/margarite', 'https://en.wiktionary.org/wiki/Marjorie', 'https://en.wiktionary.org/wiki/margarita']
=== ENTRY 2 M.v.t confirmed
ROOT ref_check: [
 {
  "ref": "FVA:384",
  "status": "not_checked",
  "note": "FVA (Nahvi, Farhang-e vazheha-ye arabi dar farsi) has no digital copy (refs_online.json)."
 },
 {
  "ref": "KLN:946",
  "status": "supports",
  "note": "KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj., dull': 'F., dull, lusterless, unpolished, fr. OF. mat, defeated, afflicted, depressed, dejected; dull, fr. Arab. māt in the sentence māt ash-shāh, the king has died. The word mat, orig. used only as a term of chess, gradually developed also the meanings faint, feeble, dull-colored. See checkmate and cp. matador, mate, adj.'; s.v. 'matador': 'Sp., killer, murderer, fr. matar, to kill, murder, fr. Arab. māta, he died. Cp. checkmate. Cp. also mat, dull'; s.v. 'mate, tr. v.' (checkmate): 'ME. maten, fr. OF. mater, to defeat, overcome, fr. mat, checkmated; defeated, overcome'; 'mate, n., checkmate. — ME. mat, fr. MF., fr. OF.' Same leaf. Klein derives mat, matador, mate (checkmate) from Arab. māt/māta 'he died'."
 }
]
ROOT consulted: null
--- node 1 Arabic maot confirmed
  deriv: Arabic mawt مَوْت 'death' is the verbal noun (maṣdar) of the hollow verb māta / yamūtu 'to die', root m-w-t, from Proto-Semitic *mawt- (Wiktionary; cognates Akk. mūtu, Heb. māweṯ, Syr. mawtā). 'maot' is simply Nourai's rendering of mawt (aw diphthong).
  refc: [{"ref": "FVA:387", "status": "not_checked", "note": "FVA (Nahvi, Farhang-e vazheha-ye arabi dar farsi) has no digital copy (refs_online.json)."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%AA', 'https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AA']
--- node 2 Persian mawt, mowt; mayyet; mât; kîš-mât plausible
  deriv: mawt/mowt موت 'death' — borrowed from Arabic mawt, Iranian pronunciation mowt (Wiktionary); mamāt ممات is the Arabic maṣdar mīmī of the same verb, also borrowed: confirmed. mayyet میّت 'dead person' — Arabic mayyit, a CaCīC adjective of m-w-t (*mawīt > *mayīt > mayyit by assimilation), borrowed as a noun into Persian: confirmed. māt مات 'dead, dull; stunned, confused' — Wiktionary gives two views:
  refc: [{"ref": "FVA:387", "status": "not_checked", "note": "FVA (Nahvi, Farhang-e vazheha-ye arabi dar farsi) has no digital copy (refs_online.json)."}, {"ref": "MON:3678,4421", "status": "supports", "note": "vajehyab.com (Mo'in) s.v. موت: '(مَ) [ع.] (اِ.) مرگ' (tagged Arabic; archived https://vajehyab.com/?q=موت&d=moein); s.v. مات: '(ص.) ۱- حیران، سرگشته. ۲- (اِ.) وضعیتی در بازی شطرنج که شاه قادر به هیچ حرکتی نیست و بازی به اتمام می‌رسد' and 'شاه مات: هنگامی که شاه شطرنج مات شود' (no origin tag shown online; archived https://vajehyab.com/?q=مات&d=moein)."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%AA', 'https://en.wiktionary.org/wiki/%D9%85%D9%8A%D8%AA', 'https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AA', 'https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%87%E2%80%8C%D9%85%D8%A7%D8%AA', 'https://www.etymonline.com/word/checkmate', 'https://vajehyab.com/?q=موت&d=moein', 'https://vajehyab.com/?q=مات&d=moein']
--- node 3 Latin mattus disputed
  deriv: Latin mattus (also mātus) 'drunk, maudlin; sodden, dull' is attested in Petronius (Satyricon 41, 1st c. CE) — six centuries before any Arabic contact — so it cannot derive from Arabic/Persian māt. The standard etymology (Pokorny IEW 694 s.v. mad-, de Vaan, Wiktionary) is *maditus 'wetted' (past participle of madēre 'to be wet, be drunk', PIE *meh₂d-, cf. Skt. mattá- 'drunk') with syncope and assim
  refc: [{"ref": "FSD:1526", "status": "partial", "note": "FSD_vol3.txt leaf 51 (printed p. ~1517; Nourai 1526), s.v. mat (dull surface) — OCR badly garbled, but the etymology bracket reads '[< F. mat(t), dull, < L. mattus; see MATE2]'. Funk & Wagnalls thus takes French mat from Latin mattus and refers the reader to the checkmate word (mate2) for the Arabic origin. It gives Latin mattus as the source of French mat, but does not itself derive mattus from Arabic māt."}, {"ref": "POK:694", "status": "contradicts", "note": "POK_02.txt leaf 355 (IEW pp. 694-695), s.v. mad-: 'naß, triefen; auch von Fett triefen, vollsaftig, fett, gemästet' ... 'lat. madeō, -ēre naß sein, von Nässe triefen, reifen, voll sein, mattus trunken (*madi-to-s)'. Pokorny derives Latin mattus 'drunk' from *madi-to-s (root mad- 'wet'), not from Arabic — the dissent Nourai records in his NOTE."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/mattus', 'https://www.etymonline.com/word/matte', 'https://ahdictionary.com/word/indoeurop.html']
--- node 4 French mat plausible
  deriv: French mat 'matte, dull, without lustre' continues Old French mat 'beaten down, withered, dejected; dull' (12th c.), which Wiktionary and TLF derive from Latin mattus 'sodden, dull' — so the edge Latin mattus → French mat is the majority view and is right as drawn; etymonline adds the alternative that the Old French adjective is a transferred use of chess mat 'checkmated' (from Arabic šāh māt), in
  refc: [{"ref": "FSD:1526", "status": "supports", "note": "FSD_vol3.txt leaf 51 (printed p. ~1517; Nourai 1526), s.v. mat (dull surface) — OCR badly garbled, but the etymology bracket reads '[< F. mat(t), dull, < L. mattus; see MATE2]'. Funk & Wagnalls thus takes French mat from Latin mattus and refers the reader to the checkmate word (mate2) for the Arabic origin. French mat 'dull' from Latin mattus, as the arrow says."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/mat#French', 'https://www.etymonline.com/word/matte', 'https://en.wiktionary.org/wiki/mattus']
--- node 5 English mat 1 confirmed
  deriv: English mat/matte 'dull, lustreless' (1640s) is borrowed from French mat; the spelling matte was not standardised until the 20th c. AHD:805 (the chart's NOTE) refers it to the IE root mad- 'wet' via Latin mattus — which, as with node 3, is the modern consensus; the French → English edge itself is uncontroversial.
  refc: [{"ref": "FSD:526", "status": "not_found", "note": "FSD_vol1.txt: printed p. 526 (leaf ~575) is in the C's ('coerce' etc.) and has no 'mat'; the checkmate entry is at p. 457 (leaf 511): 'check'mate, v. ... Chess. To put (an opponent's king) in a check from which no escape is possible ... 2. Hence, to discomfit or defeat'. Nourai's 526 is probably a misprint for 1526 (vol. 3, the mat entry)."}, {"ref": "AHD:805", "status": "contradicts", "note": "AHD online s.v. mat 2 (archived, https://ahdictionary.com/word/search.html?q=mat): '[From French, dull, from Old French, defeated, withered, perhaps from Latin mattus, stupefied, senseless, possibly from *maditus, past participle of madēre, to be wet.]' — English mat from French mat is confirmed, but AHD traces the word to Latin madēre (root mad-), not to Arabic māt; Nourai's NOTE acknowledges this. (AHD s.v. matte 2, archived https://ahdictionary.com/word/search.html?q=matte: 'from Old French, dull, from Latin mattus, stupefied; see MAT2'.)"}]
  cons: null
  src: ['https://www.etymonline.com/word/matte', 'https://ahdictionary.com/word/search.html?q=mat', 'https://ahdictionary.com/word/search.html?q=matte']
--- node 6 French mat; e'chec et mat disputed
  deriv: Old French mat 'checkmated, defeated' (12th c.; verb mater 'to checkmate, overcome') and the phrase eschec mat > Modern French échec et mat are the chess term, from Arabic šāh māt (Persian šāh māt 'the king is stunned/helpless', re-read in Arabic as 'the king is dead'), which reached the Romance languages with chess itself through Muslim Spain and Sicily in the 10th–11th c. (Spanish jaque mate, It
  refc: [{"ref": "PHN:257", "status": "supports", "note": "PHN.txt leaf 288 (Pihan p. 257): 'MAT, adj. m. (p.) [māt] défait, réduit à l'extrémité. — Faire mat ou mater veut dire, au jeu d'échecs, mettre le roi dans l'impossibilité de changer de place, ce qui termine la partie. Voyez Échec. — Par extension, le verbe mater s'emploie aussi au figuré, dans le sens de dompter, humilier, affaiblir, abattre'. Pihan tags the word '(p.)' = Persian."}, {"ref": "DEV:159", "status": "supports", "note": "DEV.txt leaf 192 (Devic p. 159): 'Mat. Terme du jeu des échecs. (Voy. Échec.) Mat, adjectif, au sens de terne, vient du mat des échecs. « Dans les anciens auteurs, dit M. Littré, mat signifie las, humilié; c'est de ce sens qu'on est allé au sens de terne, qui paraît très-récent. » ... Il est remarquable qu'en hindoustani le terme māt, importé du persan, a aussi les deux sens'."}]
  cons: null
  src: ['https://www.etymonline.com/word/checkmate', 'https://en.wiktionary.org/wiki/mat#French', 'https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%87%E2%80%8C%D9%85%D8%A7%D8%AA', 'https://ahdictionary.com/word/semitic.html']
--- node 7 English mate 2; checkmate confirmed
  deriv: English mate (v.2) 'to checkmate; to overcome, confound' (c. 1300) from Old French mater 'to checkmate, defeat' (< mat); mate (n.2) 'checkmate' likewise c. 1300 from Old French mat; checkmate (mid-14th c.) from Old French eschec mat, ultimately Arabic šāh māt. The figurative 'to thwart' sense is late-14th-c. AHD Semitic roots mwt lists exactly these two English derivatives.
  refc: [{"ref": "LKT:115", "status": "supports", "note": "LKT.txt leaf 142 (Lokotsch p. 115), No. 1443: 'Ar. māt(a): Er ist gestorben, tot; als Fachausdruck der Schachspieler šāh māt vom pers. šāh König [Horn NpEt S. 170, Nr. 772]: Der König ist tot; hieraus ist mit dem Schachspiele selbst der Ausdruck international geworden, vor allem it. scacco matto schachmatt, prov. mat, frz. échec et mat, sp. jaque y mate ..., pg. chaque e mate, rum. mat; dtsch. schachmatt, engl. checkmate ... Dazu die Vb. it. mattare, frz. mater, prov. kat. sp. pg. matar mattsetzen, überwinden, besiegen und schließlich sp. pg. matar töten [und nicht etwa < lat. mactare ...]'."}, {"ref": "KLN:946", "status": "supports", "note": "KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj., dull': 'F., dull, lusterless, unpolished, fr. OF. mat, defeated, afflicted, depressed, dejected; dull, fr. Arab. māt in the sentence māt ash-shāh, the king has died. The word mat, orig. used only as a term of chess, gradually developed also the meanings faint, feeble, dull-colored. See checkmate and cp. matador, mate, adj.'; s.v. 'matador': 'Sp., killer, murderer, fr. matar, to kill, murder, fr. Arab. māta, he died. Cp. checkmate. Cp. also mat, dull'; s.v. 'mate, tr. v.' (checkmate): 'ME. maten, fr. OF. mater, to defeat, overcome, fr. mat, checkmated; defeated, overcome'; 'mate, n., checkmate. — ME. mat, fr. MF., fr. OF.' Same leaf. Also KLN s.v. check (KLN_1966.txt leaf 154 (printed pp. 272-273), s.v. 'check' (chess): '... fr. Pers. shāh, king (in the Arab.-Pers. phrase shāh māt, the king is dead) ... cp. checkmate, chess, checker, exchequer'; 'checkmate' on the same leaf ends '(cp. also It. scaccomatto). See check, a sudden stop, and cp. mate, checkmate.')."}]
  cons: null
  src: ['https://www.etymonline.com/word/mate', 'https://www.etymonline.com/word/checkmate', 'https://ahdictionary.com/word/semitic.html']
--- node 8 Spanish matar; matador plausible
  deriv: Spanish matar 'to kill' (also Portuguese, Catalan) is of disputed origin. Wiktionary: 'most likely from Latin mactāre (through a Vulgar Latin *mattāre)', alternatively from Late Latin mattus 'drunk, stupefied' (*mattāre 'to stun'), or influenced by Arabic māta 'to die'; RAE likewise prefers Vulgar Latin *mattare < mattus. Etymonline notes the phonological difficulty of mactāre (expected *mechar) a
  refc: [{"ref": "KLN:946", "status": "supports", "note": "KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj., dull': 'F., dull, lusterless, unpolished, fr. OF. mat, defeated, afflicted, depressed, dejected; dull, fr. Arab. māt in the sentence māt ash-shāh, the king has died. The word mat, orig. used only as a term of chess, gradually developed also the meanings faint, feeble, dull-colored. See checkmate and cp. matador, mate, adj.'; s.v. 'matador': 'Sp., killer, murderer, fr. matar, to kill, murder, fr. Arab. māta, he died. Cp. checkmate. Cp. also mat, dull'; s.v. 'mate, tr. v.' (checkmate): 'ME. maten, fr. OF. mater, to defeat, overcome, fr. mat, checkmated; defeated, overcome'; 'mate, n., checkmate. — ME. mat, fr. MF., fr. OF.' Same leaf. 'matador ... fr. matar, to kill, murder, fr. Arab. māta, he died' — Nourai's arrow. (AHD s.v. matador, archived https://ahdictionary.com/word/search.html?q=matador, prefers 'possibly from Vulgar Latin *mattāre, to beat senseless, perhaps from Latin mattus'; Lokotsch 1443 sides with Klein: 'sp. pg. matar töten' from the chess word.)"}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/matar', 'https://www.etymonline.com/word/matador', 'https://en.wiktionary.org/wiki/matador', 'https://ahdictionary.com/word/search.html?q=matador']
--- node 9 French matador confirmed
  deriv: French matador is borrowed from Spanish matador in the late 17th–18th c. with the bullfighting vocabulary (Wiktionary: 'Borrowed from Spanish matador'); form unchanged.
  refc: [{"ref": "MON:3678", "status": "supports", "note": "vajehyab.com (Mo'in) s.v. ماتادور: '(دُ) [فر.] (اِ.) کسی که در میدان عمومی با گاو مبارزه می‌کند، گاوباز' — Mo'in marks the Persian word as a French loan, i.e. the French node is the immediate source. Archived https://vajehyab.com/?q=ماتادور&d=moein."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/matador', 'https://www.etymonline.com/word/matador', 'https://vajehyab.com/?q=ماتادور&d=moein']
--- node 10 Persian mâtâdor plausible
  deriv: Persian mātādor ماتادور (the chart's spelling ماتادُر marks the short o) is a 20th-c. loan; Wiktionary labels it 'borrowed from Spanish matador', whereas Nourai (following Mo'in, MON:3678) routes it through French, which was the usual channel for European words into Persian in that period and is phonetically indistinguishable here. Both routes are compatible; the immediate donor cannot be decided 
  refc: [{"ref": "MON:3678", "status": "supports", "note": "vajehyab.com (Mo'in) s.v. ماتادور [فر.] 'گاوباز' — French → Persian as drawn. Archived https://vajehyab.com/?q=ماتادور&d=moein."}]
  cons: null
  src: ['https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AA%D8%A7%D8%AF%D9%88%D8%B1', 'https://vajehyab.com/?q=ماتادور&d=moein']
--- node 11 English matador confirmed
  deriv: English matador (1670s) is borrowed directly from Spanish matador 'killer', agent noun of matar; also used from 1730s for the top trump cards in ombre/quadrille (Spanish card games).
  refc: [{"ref": "KLN:946", "status": "supports", "note": "KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj., dull': 'F., dull, lusterless, unpolished, fr. OF. mat, defeated, afflicted, depressed, dejected; dull, fr. Arab. māt in the sentence māt ash-shāh, the king has died. The word mat, orig. used only as a term of chess, gradually developed also the meanings faint, feeble, dull-colored. See checkmate and cp. matador, mate, adj.'; s.v. 'matador': 'Sp., killer, murderer, fr. matar, to kill, murder, fr. Arab. māta, he died. Cp. checkmate. Cp. also mat, dull'; s.v. 'mate, tr. v.' (checkmate): 'ME. maten, fr. OF. mater, to defeat, overcome, fr. mat, checkmated; defeated, overcome'; 'mate, n., checkmate. — ME. mat, fr. MF., fr. OF.' Same leaf. 'matador, n. ... Sp., killer, murderer' — English from Spanish."}]
  cons: null
  src: ['https://www.etymonline.com/word/matador', 'https://en.wiktionary.org/wiki/matador']
```


## [2026-09-04T19:17:01.248Z] AGENT

Now let me start grepping the books. First the pearl branch — Pahlavi/Persian.


## [2026-09-04T19:17:04.778Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n -i -E 'murw|mwlw|murvar|marvar' PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"; grep -n -i -E 'murw|mwlw|murvar|marw.rid' NYB_vol2_glossary.txt NYB_vol1.txt | head -20\necho \"=== HRN ===\"; grep -n -i -E 'murw|marw|murv|margar' HRN.txt | head -30\necho \"=== HUB ===\"; grep -n -i -E 'murw|marw|margar|murv' HUB.txt | head -20"
}
```


### [2026-09-04T19:17:04.873Z] TOOL RESULT

```
=== PHD ===
PHD.txt:333:fra$(a)murw [plfmwlw! | M fréymwrw] peacock.
PHD.txt:398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
PHD.txt:426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
PHD.txt:491:méx [myh | P myx, N ~] peg, nail. ~ ī gàh: astr. Polaris, pole star. 1-3méz-, v. mézidan, mëzišn, mistan. mēzd [my()zd | № тёз] offering, meal. „bān [-p’n' | N ~] host. mézidan, 'méz- [myc-ytn!] suck. *mézisn [myckn'] blinking, twinkling. mih [mt!] false, contrary, opposite. mihēxt [mytwht!] falsehood. imihr [mtr! | M myhr, N —] Mithra; sun; cal. 7th month; 16th day. tmihr [mtr!, etc.] contract, bond. šmihr [mtr!, etc.] love, friendship. mihrbān [mtr'p?n! | Р myhrb’n, N ~] friendly, kind. mihr-dróz [mtr'dhwc] = mihródruj. mihródruj [mtr?w-, mtrwk-diwe = Av. mitlyo.drujim] contract-breaker. ~th: breaking faith. mihr-zan [mtr'zn'] = mihródruj. mij(ag) [myc(k') | N muz(a)] eyelid; eyelash. mijüg (myc-, myšwk! | IN mizü] lentil. mir-, v. murdan. mistan, 3mëz- [mstn', myc- | N mézidan] urinate. -i$n(ih): urination. mizag [m(y)ck! | N maza] taste. ~darih [-d’lyh] (sense of) taste. ~ӧтапа [отпа] tasty. mizd [m(y)zd | N muzd] reward, hire, pay. ~war [-wbl | N -àr] hireling. *mizné [m(y)znydy] mist, dew. mög [mwk!] shoe. 5 *moy-mard [mgw-mit', -gGBRA | N muy) magus. mör [mwl | N <) ant. mórd [mwlt! | N ~] myrtle. morwārīd [mwlw'lyt! | M mwrwryd, N ~] pearl. *mowbed [mgwpt' | N móbad] Mazdean priest. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (made of) hair. moz [mwe | N ~] banana. mózag [mzvck! | N тоха] shoe. *mūdag [mwtk'} spoilt, destroyed. muy [DKRA < А dgP | N mux] date-palm. muhr [muwdl | M mwhr, N ~] seal. Сар [mwhlk! | P mwhrg, N ~a] bead, vertebra, piece (in backgammon, etc.). *muhrišn [*mwtl$n!] excrement. mulān [mwi?n'] belly (daevic).
PHD.txt:493:Р murd [то | P mort !] death. murdan, mir- (YMYTWN-tn! < A ymwtwn, V mwt; mulin' | M murd, myr-, N ~] die. murdār [mwrt?], mwld?l | N ~] carrion. murnjénidan, murnjén- (mwlncyn-ytn'] destroy. murw [mwlw! | M mwrw, (N mury)] bird. murwāģ [mwlw’k' | M mwrw’, N murwd] omen. murwizag [mwlwyck'] little bird. murw-nīš [mwlwnys] augur, soothsayer. must [mwst'] force, violence. ž*must [mwst'] = must. *must [mwst'] complaint. must|-abarmānd [mwst!’plm’nd] aggressive, aggressor. ~gar [-kl] violent, rebellious, mustómand [mwst?wmnd | N mustmand] complaining, unhappy. ImuSk [отео | N ~] musk. 2mušk [mwsk! | (N mis)] mouse, rat. must [mzvšt! | N ~] fist. muštan, māl- [mwéstn', wl- | N ~] rub, sweep.
PHD.txt:563:sang 74 sén murw
PHD.txt:564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
PHD.txt:894:augur murw-nis.
PHD.txt:895:auspicious humurwag.
PHD.txt:999:bird murw, way, wayendag; little ~ murwizag ; ~ of good omen humāy; ~ of prey škarag.
PHD.txt:2699:magpie kaskén(ag) murw.
PHD.txt:2975:omen jadag, jahišn, murwāg.
PHD.txt:3066:peacock fra&(a)murw.
PHD.txt:3661:simurgh sén-murw.
PHD.txt:4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
PHD.txt:4808:sen murw sezd sézdén haftād*
PHD.txt:4853:[138] mese murdir aay’ AV murwag 26 morwārīd -O*6 murwizag _ m» 55 murw wy Ww $6 murwnīš we NV 5G murnjén- 51136 murnjēnīdan 131936 mērd, murd
PHD_mackenzie.txt:2331: fral(a)murw [pllmwlw I M frlymwrw] peacock.
PHD_mackenzie.txt:2953:hu-murwag [hwmwlw)k ] auspicious.
PHD_mackenzie.txt:3253: -(ag) murw [_kl I N kaskina] ·magpie.
=== NYB ===
NYB_vol2_glossary.txt:2474:Marv [mlw'] 1144, Murv [mwlw'] 1921, the town of Marv. — Av. (1147) Maryu-, Mčuru-, OP Margu-. Cf EI, Suppl. 159- 162: called by the Arab. geographers Marv šāhijān (= Pers. šāhgān < šahakan ‘royal’).
NYB_vol2_glossary.txt:2592:imurv [mwlw' mwrw 404] bird; sg. with indef. art. ~+1 = murv-é 21%; pl. cas. rect. ~ 40? (after dö)-*1; pl. cas. obl. ~-dn 401%, 802, 863; — ~ in coll. sense 942°, — SW form with -v < -y: Av. (1172) maraya-; MPrth mwrg, NP mury, but MPrs mwrw, Paz. muri.
NYB_vol2_glossary.txt:2593:2murv [mwlw'] herb, grass, pl. cas. obl. ~-dn 9326, — MPrs mrw (A-H I); a SW form; the NW form in NP mary ‘a species of grass’.
NYB_vol2_glossary.txt:2594:3Murv [mwlw'] v. Marv. murvak [mwlwk'] 2624, v. s. v. sen.
NYB_vol2_glossary.txt:2595:murvik [mwlw'k] an augury, an omen 181. - MPrth mwrgw’g (S); MPrs mwrw’; nyw-murwh ‘of good augury’ (A-H II); Paz. murväi; NP murvà.
NYB_vol2_glossary.txt:2596:murvārīt [mwlw’lyt'] pearl, coll. pearls 1215, 294. 118°. 12026, — MPrth mwrg’r‘yd (A-H III), mwrgryd (MHC), borrowed from Gr uapyaplrnc; murvärit with -v- < -y- = NP murvārīd, SW form.
NYB_vol2_glossary.txt:2597:murvčeak [mwlwyck'] chicken 92%. — Demin. of !murv.
NYB_vol2_glossary.txt:2598:murv-niš [mwlwnyš] soothsayer fore- telling the future by the flight or other tokens of the birds, an augur, pl. cas. obl. ~-dn 535. — murv + niš, the pres. st. of MPrs nyyšydn, nyyš- ‘to see’ (A-H I, Verbum 168); cf nišan.
=== HRN ===
8472:aw. mereya- 'Vogel'; phlv. mury, murv (auch Papyrus,
10598:(H. No. 10), amarw 'Sommer (H. No. 12); ahd. an. sumar
=== HUB ===
8864:47, 11, Shk. 258, vgl. paz. tmirvai = np. murvCl 'omen
8865:bonum*, phi. murvak Yatk. i. Zar. p. 46, Anm.; marvarld
```


## [2026-09-04T19:17:07.005Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN margarite ===\"; grep -n -i 'margarit\\|margaron\\|margaric' KLN_1966.txt | head -20\necho \"=== SKT ===\"; grep -n -i 'margarit\\|marguerite\\|pearl' SKT.txt | head -20\necho \"=== LAT ===\"; grep -n -i 'margarita\\|margarit' LAT.txt | head -20\necho \"=== LEW ===\"; grep -n -i 'margarita\\|margarit' LEW_1910.txt | head -20\necho \"=== LKT ===\"; grep -n -i 'margarit\\|marjan\\|marǧān\\|Perle' LKT.txt | head -30"
}
```


### [2026-09-04T19:17:07.115Z] TOOL RESULT

```
=== KLN margarite ===
14439:feta  morgana,  mirage.  —  It. ;  a  name  orig.  given to  the  mirages  that  are  often  to  be  seen  in  the streets  of  Messina.  The  name  lit.  means  ‘the fairy  Morgana’ ;  Morgana  itself  derives  fr.  Arab. mar  jin,  ‘pearl’,  used  also  as  a  female  name,  and is  to  be  explained  from  the  Arabic  popular belief  which  ascribes  mirages  to  the  work  of  the sorceress  Marjdn.  See  feiry  and  margaric, marguerite.
22917:It.,  fr.  L.  maritima,  neut.  pi.  of  maritimus,  ‘per¬ taining  to  the  sea,  near  the  sea’,  fr.  mare,  ‘sea’. Cp.  OF.  maresme,  Catal.  maresma,  ‘marsh’, which  are  of  the  same  origin,  and  see  maritime. Margaret,  fem.  PN.  —  OF.  Margaret  (F.  Mar¬ guerite),  fr.  L.  margarita,  pearl  .  See  margarite and  cp.  Margery.
22918:margaric,  adj.,  pertaining  to  a  white  fatty  acid C^H^CO.H  ( chem .)  —  F.  margarique,  fr.  Gk. papyapov,  ‘pearl’.  See  margarite  and  -ic. margarin,  n.,  a  fatty  substance  found  in  animal fats  and  vegetable  oils  (chem.)  —  F.  margarine , fr.  margarique,  lit.  ‘of  a  pearl-like  color  (see margaric  and  chem.  suff.  -in) ;  coined  by  the French  chemist  Marie-Eugene  Chevreul  (1786- 1889).
22919:margarine,  n.,  artificial  butter.  —  F. ;  see  prec. word.  The  name  arose  from  the  erroneous  no¬ tion  that  all  oils  and  fats  contain  margaric  acid, margarite,  n.,  1)  a  pearl  (archaic)',  2)  a  basic aluminum  calcium  silicate  (mineral.)  —  ME.,  fr. OF.  margarite  (F.  marguerite),  fr.  L.  margarita, fr.  Gk.  papyapfxT)?  (scil.  Xiffop),  ’pearl’,  which is  of  uncertain  origin.  It  possibly  derives  fr.  OI. mahjaram,  mahjari,  ‘bud,  pearl  .  Gk.  pxpyapov is  prob.  a  back  formation  fr.  uxpyapf-nr,;.  Cp. Margaret,  margaric,  margarin,  marguerite.  For the  ending  see  subst.  suff.  -ite. margaritiferous,  adj.,  producing  pearls.  —  Com¬ pounded  of  L.  margarita,  pearl  ,  and  the  stem of  ferre,  ‘to  bear,  carry’.  See  prec.  word  and -ferous.
22924:margarita,  ‘pearl’.  See  Margaret, margin,  n.  —  ME.  margine,  fr.  L.  margo,  gen. marginis,  ‘edge,  brink,  border’,  which  is  cogn. with  Goth,  marka,  ‘boundary,  frontier’,  OE. mearc,  ‘boundary,  boundary  sign,  sign,  mark’. See  mark,  ‘boundary;  sign’,  and  cp.  marge, margent.
22930:marguerite,  n.,  oxeye  daisy.  • —  F.,  ‘pearl; daisy’,  fr.  OF.  margarite,  ‘pearl’,  resp.  OF. margerite,  ‘daisy’,  fr.  L.  margarita,  ‘pearl’,  fr. Gk.  papyapf-nj?.  See  margarite.
=== SKT ===
10884:name,  due  to  the  existence  of  such  terms madtx-jc/va,  honeysuckle  (lit.  moth wood),  madrrdHitiv,  worxibine  (lit  molV bush),  madrt-pcrla,  mother  of  pearl.  Hcri ma*frt  is  from  L.  mafrtm,  ace  <4  maftf mother;  see  Mother.  Pora  U  from  Gl wSipoz,  a.  light  friable  stone,*  also  a  stalid tile.  ^  Itut  the  word  has  certainly  bed mtdefstaiHi  (prob.  misundtrttocd)  as  coa nccted  witn  pert,  whence  na  merool scientific  terms  such  as  taitm-pora.  tnbi pora^  dfnti-fora. gtmmUporn,  'Scientific' etymology  is  usually  clumsy,  and  frC quently  wrong.  We  may  conclude  t E.  fere  has  been  substituted  for  Gk. by  conftision.
10928:mietreea.  a  lady  of  a  household.  (F.  • L.^     0.  F,  maistresse.  '  a  raiatress,  dame  ; ' Cot.  {F.mai/resse.)   Fcta.  of  O.V.maistre, a  master  ;  mtc  niaater  (above). AlagnoUa.    (K.)      A  genua  of  plants named  after  Pierre  jI/e^^w/,  of  MootpcUier, in  i- ranee;  died  a.i..  1715. Magpie,  a  bini.  (F.-L.-Gk. ;  a«</ F. —  L . )     A  Uo  ca  1 1  ed  Bnagpt-pU,  ^i^gg^^y  -/". Mag  is  short  for  Magoi  -  F.  Afargof,  a familiar  form  of  F.  Margverite,  alsu  used to   denote  a  magpie.      This  ii  from   L. Margarita^    fik.  fuxfrfapirrftf   a   pearl ;  cC Pers.    muruftirii/.  a   fiearl.     /W  ■»  F.  /i>, from  L.  fica,  a  magpie ;  see  Pie  (x). Mahogany,  a  trc«.   (W.  Indian.)    The native  S.  American  name  (Webster). Mahometan ;  see  Mohammedao. Maid.  Maiden:  see  May  {,i). Mail  (I),  »tccl  network;  sec  Maculate. Mail    (3),  a   letter-bag.    (F.-U.  H.  G.) M.  E.  mo/f.  — O.  F*.  ma/e  {¥.  ma/Ze),  a  bag. wallet  —  O.  H.  G.    malaho,    a    leatheni wallet. +Gae].  and  Iri:>h  jwo/a,  a  bag:  Gk. /i«A7'.'F,  hide,  skin.
13564:PEARL.
13576:PearL  ^K.-L)     U.'E. perU.-^V. perU. 'a   i>carl,   a  berrie;'    Cot.      Of  disputea' origin;    we   find   also    Ital..   Span.    ProV. ptrta.  Port,  pereta^  peria ;  Low  L.  pernio (7lh  cent),     Prob.  put  for  L.  fiiruia  •,  i.  e. a  little  pear,  from  h.  finem,  a  pear ;  ef. Span.^r»7/a,  (1)  a  little  pear,  [2)  a  pear- shaped  ornament,   O.  Ital.  peroU,  a   little button   00   a  cap.     I'cihaps  suygested the  various  senses  of  L.  Isxica,  (1)  a \i)  olive-berry,  ^3)  round  fruit,  U)  a ^  Horace).     Set  P>ttl  \^lY
13578:PEARL-BARLEY.
13579:Pearl-barley.   (F.  -  L,:  and  E.)    F. ■*^  per!^,  pearl  barley   (Hamilton) ;    but jthis  seems  to  be  a  comiption  of  orge p<li, •billed  barley/  Cot.     See  Peel  (i).
15201:Purl  {7),  spiced  beer.  (F.  -  L.)  lo Fhillips,  ed.  1 70^1.  But  it  should  be  pearl. It  was  a  term  in  cookery;  thus  sue  re  per U is  sugar  boiled  twice,  bcuillen  perU^  jelly- broth.  Cf.  Q.  perleUy  to  pearl,  rise  in  small bubbles  like  pearls.     See  Pearl.
20451:union  (2).  a  large  pearl.  (F.-L.)  The same  wonl  as  the  above ;  the  L.  unts means  oneness,  also  a  single  pearl  of  a  large size,  also  a  kind  of  onion.
=== LAT ===
36571:margarita, -ae (-tum n.)f.: perle. Emprunt au gr. masc. (AapY«.pCTr)C
36573:margarltVrius,-tus, margaritifer, M.L.535ia; got . marikreitus', celt.:
69809:est margarita, empruntd au grec.
=== LEW ===
=== LKT ===
684:'Kristall';  hieraus  sp.  abalorio  'kleine Glasperle',  pg.  avelorios,  avellorios  'Glas- perlen, wertlose  Kleinigkeiten'.  [DE  31.
978:[Fehlt  in  Kelekian  Kämüs,  jedoch  bei A.  Hindoglu,  Dictionnaire  Turc-Franqais. Vienne  1838.  S.  135b:  bungiik  'falsche oder  Venezianer  Glasperlen',  also  wohl allgemeiner  'Schmuck'];  hieraus  russ. bulg.  buncuk,  poln.  bunczuk  'der  Tug,  d.  h. Stange  mit  Roßschweif'  [Genaueres  hier- über s.  ZDMG  XI,  547/549],  Adj.  bun- czuczmj  'prunkhaft'.  Karlowicz  423  gibt als  Grundwort  ein  pers.  mängük  'Gold- knauf auf  der  Standarte'  [vielleicht unsere  Nr.  1396  V]  an.
999:'Schlechter  Boden  aus  Sand,  Lehm  und Steinen;  unbebautes  Gelände';  hieraus pg.  barroca  'unebenes  Gelände,  sandiger Boden  mit  Lehm  und  Steinen',  barroco ein  Kunstausdruck  der  pg.  Perlenfischer und  -bändler  für  'eine  doppelkugelige, höckerige,  verwachsene  Perle'  [Con- stancio  Dicc  163  b],  dann  verallgemei- nert: 'schiefrund,  unregelmäßig',  sp. barroco  'unregelmäßig'  (in  der  Baukunst vom  Herkömmlichen  abweichend),  frz. baroque,  it.  barocco;  dtsch.  Barock,  ba- rock. [Ableitungen  aus  lat.  bisverruca 'Doppelwarze',  bisrocca  'Doppelstein',  it. barrochio  <^  lat.  bisrotulus  'Doppelrolle' sind  unbegründete  Verlegenheitsetymo- logien.]
1014:'Nachgemachte  Perlen,  Glasperlen',  Ein- heitsnomen busra,  tk.  ebenso  bäsre; hieraus  russ.  busy,  biser,  klruss.  buseV, biser,  bulg.  serb.  biser  'Glaskorallen, Glasperlen'.  [Gorjajew  17  und  35. Bern  SlEtWb  5S.
1095:'Stahl';  hieraus  rum.  cilic  'dass.,  Stahl- perlen'; bulg.  serb.  celik  'Stahl'.
1408:552.  Ar.  durr  uinfassal: 'Gesonderte  Perlen'  [aus  durr  'Perlen, Musiknoten' und  »««(/"assa?  Kunstausdruck für  die  regelmäßige  Ünterbrechung  je zweier  Perlen  der  Perlenschnur],  viel- leicht mit  pers.  sog.  Izäfät:  dtirr-i- nmfassal;  aus  diesem  Grundwort  sind die  Tonbezeichnungen  der  sog.  Solmi- sation  do  re  mi  fa  so  Z«  entstanden,  die man  gewöhnlich  als  von  GUIDO  VON AREZZO  [995—1050]  erfunden  erklärt; offenbar  hat  er  sie  aber  einem  orienta- talischen  Notensystem  entnommen.  Der angeblich  von  PAUL  DIAKONUS  stam- mende bekannte  Hymnus  Ut  queant laxis  Resonare  fibris  Mira  gestorum Famuli  tuorum  Solve  polluti  Labii
1671:'Hals,  Nacken'  [Horn  NpEt  S.  201 ,  Nr.  903], ebenso  tk.  gerden  'dass.,  Halsband'; hieraus  rum.  gherden,  ghiordan  'Hals- band, Perlenschnur',  bulg.  gerdan,  serb. dierdan  'Halsband',  kliuss.  garda 'Schmuck,  Zierat'.
1711:694.  Ar.  ganimr: 'Edelstein,  Juwele'  [ursprünglich  pers. göhär  'Edelstein'  Horn  NpEt  S.  211, Nr.  948] ;  hieraus  mit  ar.  Art.  sp.  aljöfar 'schief  und  unregelmäßig  gebildete, kleine,  echte  Perle;  Samenperle',  pg. aljofre.  Aus  dem  ar.  plr.  gatmhir  wurde tk.  gewahir  als  Sgl.  gebraucht,  gewahirgi Juwelier';  hieraus  Tum.  giuvaer  ^ix\.vi&\, Kleinod',  giuvaericä  'Geschmeide, Schmucksache',  giuvaergiü  'Juwelier, Juwelenhändler'.  [DE  145.  Eguilaz203. ML  3945.
2193:Terle',  auch  in  nichtosmanischen  Dia- lekten inci,  jinci  [vom  Stamme  jeiii, s.  hier  Nr.  954,  vgl.  Cag.  inci  'Zierat, kokettes  Weib'  Värabery  TktEtWb  S.  83] ; hieraus  vielleicht  russ.  zemcug,  zemcu- äina  'echte  Perle'.
2516:schon  früh  lat.  gaza  'Schatz';  hieraus it.  gazzetta,  ursprünglich  eine  kleine Münze,  die  man  für  ein  Zeitungsblatt hingab,  dann  'Zeitung'[die  ersten  geschrie- benen Zeitungen  erschienen  im  Jahre 1560  in  Venedig],  frz.  gazette,  sp.  gaceta, pg.gazeta  'Zeitung'  [Körting  4117  a  leitet dagegen  vom  Demin.  von  gazza  'Elster' ab,  weil  die  Zeitungsbiätter  so  schwatz- haft seien  wie  dieser  Vogel;  noch  merk- würdiger ist  die  hier  nur  als  Kuriosum angeführte  Etymologie  in  Gonstancio Dicc  587  b  aus  dtsch.  Ganz-zeit.'];  engh gazette,  ndl.  gazet;  russ.  bulg.  poln.  ga- zeta  'Zeitung'.  —  Aus  dem  pers.  Grund- wort und  pers.  Suffix  -bär  'Träger'  [Horn NpEt  S.  36,  Nr.  158]  ergibt  sich  *gazbär 'Schatzträger,  -meister'  und  hieraus  Kas- par, der  König  aus  dem  Morgenlande; da  er  komisch  wirkte,  entstand  die  Figur des  Kasperle.  Dagegen  geht  gauner- deutsch kaspern  'betrügen'  auf  hehr. käza^  'lügen'  zurück.
2560:Die  lustige  Figur  des  tk.  Schattenspiels, etwa  'Kasperle'  [aus  tk.  kara  'schwarz' und  göz  'Auge'  vom  Stamme  kar,  kor, kör,  köz  'Auge,  blicken'  Vämbery  Tkt EtWb  S.  79,  Nr.  83 II];  hieraus  rum. caraghios  'Possenreißer,  närrisch',  ca- raghioslic  'Possenhaftigkeit,  Spaß' ;  frz. caragueiise  'Marionettenfigur'.  [Ausführ- liches über  die  Figur  des  Karagöz  s. Georg  Jacob ,  Türkische  Literaturge- schichte in  Einzeldarstellungen.  Heft  1. Das  tk.  Schattentheater.  Berlin  1900. S.  19  ff.,  sowie  G.  Jacob,  Die  tk.  Volks- lileratur.  Berlin  1901.  S.  33/34  ]
4151:Ebenso  bind,  sankh  'Muschel';  hieraus angloind.  engl,  chank,  chunk  'eine  große Art  Muscheln,  Turbinella  rapa',  die  von den  Hindus  sehr  geschätzt,  als  Tempel- horn oder  in  Stücken  geschnitten  als Armband  oder  anderer  Schmuck  benutzt oder  zu  Opferungen  verwandt  wird.  Be- sondei's  im  Golf  von  Manaar  wird  die Fischerei  nach  dieser  Muschel,  die  frü- her wie  die  Perlenfischerei  Regierungs- monopol war,  beirieben.  Abnorme  For- men mit  der  Spiralöffnung  nach  rechts wurden  bis  zu  100000  Rupien  geschätzt. [Hobson-Jobson  184/185.
4350:1926.  Tk.  sorgiig: 'Helmbusch,    Perleiistrauß'  [Kelekian Kämüs  771b];  hieraus  rum.  surgucnt
5791:Karett(schildkröte)  1073 harmin  1219 Äaro6<;  832 Aantie  832 Za/w  1087 ÄrtsacÄ;  1143 ka  sacke  mhd.  1143 iTäsf/j  1102 Kaschemme  ].  1129 Kaschmir  1116 Kasimir  1116 Kasperle  1059 kaspern  J.  1059 Kassiber  1168 üfa.wär  1119 kasugele  mhd.  1143 Katesberger  j.  845 Katschäume  j.  1129 Kat(t)un  1272 Katzoff  ].  1107 Kauri(mtixchel)  1133 K'iviar  851 Af/ü«  1176 Keschengannef  j.  659 ifessfZ  j'.  1166 ÄÄaiti  787 ZvV/'er  727 AiVs  j.  1185 Kimono  1177 iC/osfc  732 je*«»)««  1187 KitUchen)  j.  1190 Ai^^eZ  1272 Klabautermann  1022 AZMf<  j.  1154 knassen  j.  1050 Änasi  j.  1050 AocTiafe  St.  1132 kochem  j.  788 kochemer  Loschen  j.  788 A'o/f«-  1225 ATo/t/  j.  1194 A^ofroH  1170 Kolkothar  1236 Komitadschi  781 Konditor  1052 Aopefce  1204 Köpernick  1159 Aojsm  1169 Aoran  1250 Korund  1263
```


## [2026-09-04T19:17:23.320Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB ctx ===\"; sed -n '8855,8880p' HUB.txt\necho \"=== HRN marvarid ===\"; grep -n -i -E 'marvar|marwar|murwar|Perle' HRN.txt | head -20"
}
```


### [2026-09-04T19:17:23.391Z] TOOL RESULT

```
=== HUB ctx ===
^mazya- zuriickgefiihrt werden. Wurde schon ap. mazga-
in "^magza- = ^mayza- umgestellt? Np. taj 'Krone' ist
arabisirt aus tay. Np. jihan 'Welt' kann nicht arabisirtes
gehan sein , da Jifian im Arabischen nicht vorkommt. So
bleibt jihan, besser jahan, zunachst dunkel.
*j Wechsel von y und g bei VuUers, Gram. p. 31.- 248 -
§ 140. Fiir ap. g erscheint v in:
Marv =^ ap. Margu-, gr. I\Ja(}yiav7J, zd. mduru-; paz.
phi. muru ^Vogel', pi. murmn Min. 61. 141, Phi. Min. 31, 2;
47, 11, Shk. 258, vgl. paz. tmirvai = np. murvCl 'omen
bonum*, phi. murvak Yatk. i. Zar. p. 46, Anm.; marvarld
Terle* (marvarldln *of pearl' JRAS. 1894, p. 488), phi. mar-
vdrlt etc. (NSldeke, Pers. Stud. II, 44) = juapyagirTjg ;
mdbad = phi. magupat,
Aber neben Marv (dazu np. Maro i rod 'Fluss-Merv',
Noldeke, syr. Ghron. 39, arab. Marvarrud bei Yaqut =
arm. Marvirot Laz. Pharp. 233 im Unterschied von der
Hauptstadt, arab. Marv as-sdhijan (Yaqut) = np. Marv
i sdhagcLn *das konigliche Merv) stehen die Formen Marg
und Margrot (als Distrikte von Chorasan) bei Sebeos p. 67
sowie np. marydb =^ *Mervwasser ^) ; neben paz. murU 'Vogel'
steht np. mury\ neben mdbad = syr. mOwed, arm. movpet
(EliSe 124, 4 v; u. , vgl. movan handerjapet EliSe 124,
Laz. Pharp. 262) steht arm. mogpet (Elise u. s. w., vgl.
mogac anderjapet bei Faustus 157), ^YA.magupat, vgl.
ap. magu- *Magier' = phi. mag, np. muy,
=== HRN marvarid ===
233:aber längst nicht alles umfassen. Von dem Versuche, Perles'
3326:kurd. LW. pirun, perlen 'Hemd'; wa/. parhän, sar.
```


## [2026-09-04T19:17:25.519Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA (Fraenkel) ===\"; grep -n -i -E 'marg.n|marjan|marǧān|margarit' AFA.txt | head -20\necho \"=== AFM (Addi Shir) ===\"; grep -n -E 'مرجان|مرواريد|مروارید' AFM.txt | head -20\necho \"=== FVQ marjan ===\"; grep -n -i 'marjan\\|marjān' FVQ.txt | head -20"
}
```


### [2026-09-04T19:17:25.589Z] TOOL RESULT

```
=== AFA (Fraenkel) ===
=== AFM (Addi Shir) ===
954:+ (السمد) لس القرول زه اسم 150 المرجان وفرعه ٠٠‏ بعضهم ܚܨܢ 
955:م بالمرحان ٠‏ ܫܝ 6 المرجان ܐܚܐ ܣ ܝ م 70 ' 3 
957:بالمرجان ويقال له ܝ الشجري 9 "| ܨ 030 لكان علي 
1684:روسة 19 فرنكل ( ܟ : \ ܘ) 1 خمفة من ܐܟܐܠ 0 اي المرجان ٠‏ 
4567:على وزن مرجان هو الذي يكون الساظنان.قد خعلة ܨ 7 فرفع علة جميع 
5849:مرجان ܙܡ 40 والكر د و تش لحدداة ܐܐ بالارامية 0 أو 03 
5851:(ننات) بالفرنسة ٠‏ ومرواريد بالنارسة و ܡܪܓܠܝܬ و ܡܪܓܠܝܬܐ ܨ 1 
5990:خرزة لوا ` كاون المرجان 
=== FVQ marjan ===
```


## [2026-09-04T19:17:35.745Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5840,5860p' AFM.txt\necho \"--- page tag ---\"\ngrep -n '\\[pdf page' AFM_pages.txt | head -3\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt').read()\ni=t.find('مرواريد')\nprint('idx',i)\nfor m in re.finditer(r'\\[pdf page (\\d+)\\]',t):\n    if m.start()>i:\n        print('next tag',m.group(1)); break\nEOF"
}
```


### [2026-09-04T19:17:37.415Z] TOOL RESULT

```
* ( !]ܨ ܢ ܣܣ رس ج فقيل ܝܣܝܣ ܤܣ 
قات فان كان ܥܠ المرداسنج فهو ܨ عن ܗ ع ܕܬܕ | ܝ امرداسنج ٠‏ وان كان 
ون و اموه رج ار ܣ اطبا رن 
الفارسى عروه تصحيف العرلي الأروح 

15 صغار ,+ شيل كيار الدر ܡ وقبل 2 جان 1 , 0 : 
وقال 3990 لا ܨ تانق هو ام م داعي ܨ تقدير زيادة < ܝ 3 
5 58 الاصل ٠‏ قلت 0 1 قيل هو مر ‫ من مر وهي من ادوات 
التريين ومن جان ومعثاها الروح ٠‏ وهده لكايه موحودة 0 اللغفات فى 
مرجان ܙܡ 40 والكر د و تش لحدداة ܐܐ بالارامية 0 أو 03 
15 .2 ( 5 : ` 1 ܕܢ 95:5 00 5 26 ܕ 1113101101116 
(ننات) بالفرنسة ٠‏ ومرواريد بالنارسة و ܡܪܓܠܝܬ و ܡܪܓܠܝܬܐ ܨ 1 
باللعة ;+ والم ابلمة 5 ܐܠܘ ٠‏ ܢܦܐ 9 اصلها فارسي ܨ 87 
اله ول. ܚܝ .1 وهو ܥܐ من 00000 5 15 ܀ وعنلدي 0 اصل الكلمة 
ܨ ܢܨ ܐ ܡܝ فعل © < 5 35 289 وا سم الفاعل لودل 
دح حنسط »ع فخدفت الماء ونقات ܐ الى > وحركة الراء الى اليم فصارت 
3 1 7 عن 9 صبغة }1 9 
المحرق 

( الرْرَئحوسُ ) من الرياحين دقيق الورق بزهر ابض عطري تعريب عرزن كرش 

--- page tag ---
idx 161586
```


## [2026-09-04T19:17:37.599Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ_pages marjan ===\"; grep -n -i 'marj\\|marg[aā]n' FVQ_pages.txt | head -20\necho \"=== FSD margarite ===\"; grep -n -i 'margarit\\|margarin\\|margaric' FSD_vol3.txt | head -20\necho \"=== WEB ===\"; grep -n -i 'margarit\\|margarin' WEB_vol1.txt | head -20"
}
```


### [2026-09-04T19:17:37.683Z] TOOL RESULT

```
=== FVQ_pages marjan ===
9401:(Marjdn).
=== FSD margarite ===
55235:lieurbovsters iMargaritana) and the abalunes. nacre Bee
=== WEB ===
25534:but’tér-fly fish, any of various fishes resem- i = bling butterflies in coloring or in having wing- like fins, as the blenny, the flying gurnard, or the angelfish. ‘i R but’tér-fly plant, a West Indian orchid, hav- ing flowers resembling butterflies; also, an East Indian orchid having similar flowers. but/ter-fly-shell, n. a shell belonging to the genus Voluta; also, a ptero 6 but’tér-fly ta’ble, a small drop-leaf table with leaf supports shaped like a butterfly’s wings. but/tér-fly weed, a common weed, Asclepia tuberosa, of the milkweed family, used in medicine, as a cathartic, for increasing per- spiration, etc.; the pleurisy root. _ but’tér-ine (or -in), n. [butler, and -ine.} 1. a substitute for butter made from oleo- margarine, or animal fat, with milk, coloring matter, etc.
31834:filled cheese; a kind of cheese made from skim milk: so called because a fatty filling, as lard or oleomargarine, is used as a substi- tute for the cream. 3
110563:nõret address. [Cola] n. madam: used in äarà E Ë - anal PE Soe eee margaritaceus, ab, n. k z
112825:(margaric and -ale.) a com- pound of margaric acid with a base. mär’gå ret grunt, same as margate fish. mir-gar’ic, a. [Fr. margarique, from Gr. mar- garon, a pearl: so called from the pearly luster of its crystals.) designating a white, crystal- line fatty acid, CisHssCO.H, obtained from lichens or synthetically. mir/ga-rin, n, [Fr. margarine, rique, margaric.] 1. a fatty com mal and vegetab ture of stearin and palmitin. 2. the glyceride of margaric a 3. margarine. miar’ga-rine (or -rén), 7.[ use of the chemical term, margaric acid was con oils.] a blend of refine meat fat or both, churned milk to the consistency 0: ally fortified with a minimu units of vitamin A per poun
112833:also marzipan. butter prices Pere, marb ward, one who acts as warden of the mar-ga-ri’ta, n. [L.Gr. margarilés, a crumb of to remain unused until better land is very TPS EEA. : sacramental bread, from Gr. mar. rilés, scarce. a F i Maraiin, man [Obs.] pearl.]in the Orthodox Eastern Church, (a) A 5. in botany, having a line or nerve sure rete nae ee us, withered, from mar- esse] used in administering the sacrament; parle! to the edge of a leaf but some . to wither. : : S ` As ars rom it. y inis), a ETRLERS 24 (tah Ret Tet np i tes written 2. causing emaciation body of Jesus. a margin.] no ae A re i miar’?a-ri-ta’ Z books. z ok: aes -cid/i-ty, n. the condition or quality of aE Pence a. relating to pearl or miar’gin-Al-ly, adv. in the margin, aS cae NEES withered or emaciated. [Rare.] miir/ga-rite, n. [L. margarita; Gr. margarilés, mar/gin-Al w-til/i-ty, in economics activity ar/cion-ite (-shun-), n. a follower of Mar- a pearl.] ain degree of utility, below Wr ed. ee a Gnostic of the second century, who 1. a pearl. [Obs.] is not profitable enough to be continues. Fae opid ihe Oriental idea of the two conflict- _ 2. a hydrated silicate of calcium and alum- mär'ğin-āte, v.l.; marginated, pe ain 5 EES aod amapined that between inum, found as scales with a pearly luster. ginating, ppr. to provide we h 3 ing 2 OS: Roly god cane w third power, neither 3. tiny, round crystals forming a beadlike miir/gin-ate, mär’ğin:ä:ted, a. ha ; & NALS design in glassy igneous rocks. tinct margin. r being
112870:Miar-co-brun/nér, n. a German wine: named miar’ga-ri-tif’é i inā L : 1 miar’¢4-ri-tif’ér-ous, a. [L. margarita, a pearl, mär: in-ā’'tion, 7. Fom BEG doustain Markbrunnen, near which ma ferre, to pear bearing, producing, or fur- aren : aaa margins q bat at a ETT 3 nishing pearls. mär’'ġined, a. 1. possessive red bot maoni DA fie LET and -gram.] a mir-gar/o-dite, n. [Gr. margarddes, pearllike 3 in zoology, having 4 distinct coia ewan a PAs ee rue yamo es and ile.| a hydrous mica resembling musco- _ der. : L. marso (zinis), -colnisye! gram: formerly so called. vite in crystallization and physical character Mar-gi-nel/la, 7. [dim. from L. me Marei" zS ern icaricour aioe peiicies® teleerophy. and having a pearly luster. edge, margin.] the typical genus i ual ma a , n. |L. marcor, from mar- mär’'gà: ATA TO A idz. : nd -108 Be ee heng ox vast- mär'gàron, mär'gåtone, 4: lmarearic end mar ginerlidae, ntl [Marein ehis fonti Mir-co’six ene of flesh, [Rare.] pearly scales, produced by the distillation of afamily of Gastropoda, ST Siphon a pow ugh Marco $i me n), ”. a follower of Marcus, a mixture of margaric acid and lime. warm seas, having asimPi= sral, a few ene a Gnostic o the second century. mir/ga-rous, a. same as margaric. oval shell, more or less STe columella leri (gra), [Fr., lit., fat Tuesday, from miar/ga-ry-ize, vt.; margaryized, pt., pp.; mar- teeth on the edge, at £0 (inis). uesday, and gras, fat; so called from garyizing, ppr. (so called from the inventor of miar/gin-i-ci/dal, a. [L. marii potany: ach 5 : pr g t] inb ee custom of paradingafatoxduring the process, J. J. Lloyd Margary.) to make border, and czdere, to Cut- poo 7 3 t; moD: bird, pin; note, move, for, atom, 20” i
112884:ingle flower. a Marlay-ri-cAr’Pus, n. (Gr. margarités, a pearl, aad karpos, fruit.] a genus of South American aceous plants. he p märiäge dé con-ve-niince’ (äzh’), [Fr.] a “narriage of convenience; marriage entered in- to from calculated self-interest or expediency. ma-ri/a lite, n. [after Marie Rose, wife of the German mineralogist G. von Rath.] in min- eralogy, a highly siliceous scapolite, crystal- lizing in the tetragonal system. Mar/i-tin, a. 1. of the Virgin Mary. 2. of Queen Mary of England. 3. of Mary, Queen of Scots. Mar/i-tin, 2. 1. a worshiper or devotee of the Virgin Mary. t ea follower or defender of Mary, Queen of Scots. > : Mar-i-anne’, n. a personification of the French Republic, as on coins. ma-ric’6-lous, a. [L. mare, the sea, and colere, to dwell,] in zoology, sea-dwelling; pelagic; marine. mar/i-et, n. (OFr. marietle, dim. of Marie, Mary.] a plant, Campanula urticifolia, or Canterbury bell. [Obs.] ma-rig/é-nous, a. [L. mare, the sea, and -genus, produced.] produced in or by the sea. mar’i-gold, z. [Mary (prob. the Virgin Mary), and gold.]} 1. any of several plants of the composite family, with red, yellow, or orange flowers. 2. the flower of any of these plants. mar/i-graph, n. [L. mare, the sea, and Gr. graphein, to write.] an automatic tide gauge for making a continuous record of the height of the tide. ma-ri-jud/na, mä-rihuä’nä (-hw4’), n. [Am. Sp.] 1. the hemp plant. x 2 a narcotic obtained from its dried leaves AR n smoked in cigarettes by addicts. So the Ane? n. [from native name.] a small, Bee merican monkey with fine, silky hair the golden-yellow color and a mane about Page :also called silky tamarin. Sona ede Afr. (Bantu) marimba, Sail : tm- a, a kind of musical
```


## [2026-09-04T19:17:46.116Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt'\nimport re\nt=open(p,encoding='utf-8',errors='replace').read()\nprint(len(t))\ntags=re.findall(r'\\[pdf page (\\d+)\\]',t)\nprint('tags',len(tags),tags[:5])\ni=t.find('المرجان')\nprint('idx marjan',i)\ni2=t.find('ومرواريد')\nprint('idx morvarid',i2)\nfor m in re.finditer(r'\\[pdf page (\\d+)\\]',t):\n    if m.start()>i2:\n        print('page containing:',m.group(1)); break\nEOF"
}
```


### [2026-09-04T19:17:47.734Z] TOOL RESULT

```
206047
tags 0 []
idx marjan 24540
idx morvarid 161585
```


## [2026-09-04T19:17:47.894Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD all vols margarite ===\"; grep -n -i 'margarite\\|margarine\\b' FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt | head -10\necho \"=== FVQ_pages leaf 278 context ===\"; awk 'BEGIN{RS=\"\\f\"} NR==278' FVQ_pages.txt | head -40"
}
```


### [2026-09-04T19:17:49.618Z] TOOL RESULT

```
=== FSD all vols margarite ===
FSD_vol4.txt:64651:oleic,  O-lFik,  E   7   57  *   IF  *.  1,  2,  3,  6,  C.  8   9. 12. 13, 15. 17, 18  19,20,22, 23.21. 25.-0'li- ik.C  57tS  IF*  Ilr,4,7. 11. 10.21 oleomargarine,  0   li-o-ra6r'ga«rln,  C   E   J 57*  E   IF*  IFr  1.  3.  4,  5.  6.  7,  8.  9, 11.  12.
FSD_vol2.txt:3401:Elizabeth.  11.  Thomas  (1576-7/311652).  English  soldier- non>*coTifonnist;  thrice  povernor  of  iMassachu^jetts  13,  \ mining  and  manufacturing  town  in  Worcesterahire  ’   England* castle.  13.  A   town  in  Worcester  county.  Mass {lud'ley-lte,  1   dnd'li-ait;  2   dhd'ly-It,  b.  Mineral.  An  altera- tion product  of  margarite.  [<  JOudleyville,  Ala.] dud'leysnosed",  1   dud'lwiBzd";  3   ddd'ly«n6.3d",  a.  Kennel.
=== FVQ_pages leaf 278 context ===
260 FOREIGN VOCABULARY OF THE
though Vollers, ZDM G, li, 303, follows him in this there is little to be
said in its favour. The word was well known in pre-Islamic days and
occurs in the old poetry, 1 and so may quite well have come direct
from Middle Persian, though it is also a possibility that it may have
come through the Syr.
x.^
/j JL* (Madyan).
vii, 83 ; ix, 71 ; xi, 85, 98 ; xx t 42 ; xxii, 43 ; xxviii, 21, 22, 45 ;
xxix, 35.
Midian.
The references are all to the stories of Moses and Shu'aib, and the
place is clearly the Biblical *"!??, but derived through a Christian
channel. (Noldeke, Ency. Bill, iii, 3081.) -^
Some of the early authorities endeavoured to derive it from j A^
(LA, xvii 9 289), but al-Jawaliqi, Mu'arrab, 143, is inclined to take it as
a foreign borrowing.
The presumption is that it came to Arabic through the Syr.
fj
* >* ^
AJjJb* (Madina).
s v '
vii, 108, 120 ; ix, 102, 121 ; xii, 30 ; xv, 67 ; xviii, 18, 81 ; xxvi,
35, 53 ; xxvii, 49 ; xxviii, 14, 17, 19 ; xxxiii, 60 ; xxxvi, 19 ; Ixiii, 8.
A city.
The popular derivation among the Lexicons is that it is a form
from jX to settle, though others considered that it
was from jlS to possess (LA, xvii, 288, 289). The great argument
*" *
. ^s . . >> . . *K^
in favour of a derivation from jX* is the plu. JA* beside ^ lA^,
for, said the philologers (cf. Ibn Bar! in LA), how could it have such
a plu. form if the J were not part of the root ?
1 Vide Horovitz, KU, 137.
8 Mingana, Syriac Influence, 95 ; Ahrens, Muhammad, 9.
8 See the discussion in Horovitz, K U, 138 ; JPN, 153, 154, where he would
draw a distinction between the Madyan of the early Suras of the Qur'an where it
means Midian, and the Madyan of later passages where it refers to the Arabian Madyan
opposite the Sinai peninsula, the MoSiava of Ptolemy.
```


## [2026-09-04T19:17:58.248Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['AFM','PLA','BQT','MON','ARY','LKT','PHN','DEV','LAM','FSD','WEB','KLN','SKT','LAT','LEW','POK','WLD','AHD','IEC','SYN','PHD','NYB','HRN','HUB','FVQ','AFA','LKT']:\n    if k in d:\n        r=d[k]\n        print(k, {kk:vv for kk,vv in r.items() if kk in ('kind','page_offset','local_file','lookup_hint','scans','title')})\nEOF"
}
```


### [2026-09-04T19:17:59.791Z] TOOL RESULT

```
AFM {'title': "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", 'kind': 'archive_djvu', 'lookup_hint': "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'], 'page_offset': "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image"}
PLA {'title': 'A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988', 'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'], 'page_offset': '301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).', 'lookup_hint': 'HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)', 'scans': [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', 'first_printed': 1, 'last_printed': 300, 'pdf_offset': 0, 'lang': 'deu+ara'}]}
BQT {'title': "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", 'kind': 'archive_djvu+local_scan_ocr', 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'scans': [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]}
MON {'title': "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", 'kind': 'website+archive_djvu', 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None}
ARY {'title': "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه\u200cهای هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", 'kind': 'local_scan_ocr', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'scans': [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt'}]}
LKT {'title': 'K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt', 'page_offset': 'leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."}
PHN {'title': "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt', 'page_offset': 'leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc."}
DEV {'title': "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt', 'page_offset': 'leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': 'French headword in caps at line start.'}
LAM {'title': "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt', 'page_offset': 'leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "French headword in caps at line start with running heads like '2 ABRI'."}
FSD {'title': 'Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt', 'page_offset': 'vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file."}
WEB {'title': "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt', 'page_offset': 'not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': 'Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.'}
KLN {'title': 'E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
SKT {'title': 'W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
LAT {'title': 'A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt', 'page_offset': 'leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'."}
LEW {'title': 'A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt', 'page_offset': '1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': 'Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.'}
POK {'title': 'J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
WLD {'title': 'A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32', 'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
AHD {'title': "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", 'kind': 'archive_djvu+website+archive_restricted', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
IEC {'title': 'S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
SYN {'title': 'C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
PHD {'title': 'D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
NYB {'title': 'H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
HRN {'title': 'P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
HUB {'title': 'H. Hübschmann, Persische Studien, Strassburg 1895', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
FVQ {'title': "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", 'kind': 'archive_djvu', 'lookup_hint': 'Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).', 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'], 'page_offset': 'printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)'}
AFA {'title': 'S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt', 'page_offset': 'leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': 'Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.'}
LKT {'title': 'K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927', 'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt', 'page_offset': 'leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."}
```


## [2026-09-04T19:18:09.696Z] TOOL CALL #16: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py <<'EOF'\nimport sys,re\nf=sys.argv[1]; pat=sys.argv[2]\nt=open(f,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nstarts=[];pos=0\nfor p in pages:\n    starts.append(pos); pos+=len(p)+1\nfor m in re.finditer(pat,t,re.I):\n    # find leaf\n    lo=0\n    for i,s in enumerate(starts):\n        if s<=m.start(): lo=i\n        else: break\n    print('leaf(0-based)=%d  match=%r  ctx=%s'%(lo,m.group(0)[:40], t[max(0,m.start()-100):m.start()+200].replace('\\n',' ')))\nEOF\ncd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### AFM marjan leaf\"; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py AFM.txt 'ومرواريد'\necho \"### HUB marvarld leaf\"; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py HUB.txt 'marvarld'\necho \"### NYB murvarit leaf\"; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py NYB_vol2_glossary.txt 'murvārīt'\necho \"### PHD morwarid leaf\"; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py PHD.txt 'morwārīd'"
}
```


### [2026-09-04T19:18:11.305Z] TOOL RESULT

```
### AFM marjan leaf
leaf(0-based)=0  match='ومرواريد'  ctx=تش لحدداة ܐܐ بالارامية 0 أو 03  15 .2 ( 5 : ` 1 ܕܢ 95:5 00 5 26 ܕ 1113101101116  (ننات) بالفرنسة ٠‏ ومرواريد بالنارسة و ܡܪܓܠܝܬ و ܡܪܓܠܝܬܐ ܨ 1  باللعة ;+ والم ابلمة 5 ܐܠܘ ٠‏ ܢܦܐ 9 اصلها فارسي ܨ 87  اله ول. ܚܝ .1 وهو ܥܐ من 00000 5 15 ܀ وعنلدي 0 اصل الكلمة  ܨ ܢܨ ܐ ܡܝ فعل © < 5 35 289 وا سم الفاعل لودل  
### HUB marvarld leaf
leaf(0-based)=258  match='marvarld'  ctx=, 11, Shk. 258, vgl. paz. tmirvai = np. murvCl 'omen bonum*, phi. murvak Yatk. i. Zar. p. 46, Anm.; marvarld Terle* (marvarldln *of pearl' JRAS. 1894, p. 488), phi. mar- vdrlt etc. (NSldeke, Pers. Stud. II, 44) = juapyagirTjg ; mdbad = phi. magupat, Aber neben Marv (dazu np. Maro i rod 'Fluss-Merv',
leaf(0-based)=258  match='marvarld'  ctx=gl. paz. tmirvai = np. murvCl 'omen bonum*, phi. murvak Yatk. i. Zar. p. 46, Anm.; marvarld Terle* (marvarldln *of pearl' JRAS. 1894, p. 488), phi. mar- vdrlt etc. (NSldeke, Pers. Stud. II, 44) = juapyagirTjg ; mdbad = phi. magupat, Aber neben Marv (dazu np. Maro i rod 'Fluss-Merv', Noldeke, syr. Gh
### NYB murvarit leaf
leaf(0-based)=148  match='murvārīt'  ctx=n 181. - MPrth mwrgw’g (S); MPrs mwrw’; nyw-murwh ‘of good augury’ (A-H II); Paz. murväi; NP murvà. murvārīt [mwlw’lyt'] pearl, coll. pearls 1215, 294. 118°. 12026, — MPrth mwrg’r‘yd (A-H III), mwrgryd (MHC), borrowed from Gr uapyaplrnc; murvärit with -v- < -y- = NP murvārīd, SW form. murvčeak [mwl
### PHD morwarid leaf
leaf(0-based)=80  match='morwārīd'  ctx=shoe. 5 *moy-mard [mgw-mit', -gGBRA | N muy) magus. mör [mwl | N <) ant. mórd [mwlt! | N ~] myrtle. morwārīd [mwlw'lyt! | M mwrwryd, N ~] pearl. *mowbed [mgwpt' | N móbad] Mazdean priest. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (made of) hair. moz [mwe | N ~] banana
leaf(0-based)=219  match='morwārīd'  ctx=! marz marz- marcabukih marčābuk marzīdan marzangūš PAHLAVI KEY [138] mese murdir aay’ AV murwag 26 morwārīd -O*6 murwizag _ m» 55 murw wy Ww $6 murwnīš we NV 5G murnjén- 51136 murnjēnīdan 131936 mērd, murd Ne murdan Ae mustomand 1-3must mustgar Se F” ^ ale mozag ^ de 96 "пик mustan oe müdag muhrig
```


## [2026-09-04T19:18:20.565Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds',t.count('\\f'))\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'ومرواريد' in p or 'مرواريد' in p:\n        print('leaf',i)\nEOF"
}
```


### [2026-09-04T19:18:22.298Z] TOOL RESULT

```
formfeeds 197
leaf 145
```


## [2026-09-04T19:18:23.564Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN pearl ===\"; grep -n -i 'pearl' SYN.txt | head -10\necho \"=== IEC margar ===\"; grep -n -i 'margar' IEC.txt | head -5\necho \"=== POK margar ===\"; grep -n -i 'margarit\\|margaron' POK_full.txt POK_01.txt POK_02.txt POK_03.txt | head -5\necho \"=== WLD band3 margar ===\"; grep -n -i 'margarit' WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt | head -5\necho \"=== AHD margarites ===\"; grep -n -i 'margar' AHD_watkins1985.txt | head -5"
}
```


### [2026-09-04T19:18:23.690Z] TOOL RESULT

```
=== SYN pearl ===
9428:ut), prob. (though disputed) the same word as unié (fr. anus ‘one’) commonly applied to a single large pearl, and so not improbably by farmers to the onion. Ernout-M. 1126. REW 9073. Peder- sen 1.207. Franck-v. W. 12,716.
11164:1 (6. es G iaqormment ( G kleinot NH : i Keinood, eee (in general), 6. SCr. dragulj, Boh. drahokor (ef. Heinod, © ‘a “ae cpd. of klein in | kdmen ‘stone’), Russ. dragocennost’, fr. ep (MHG) “a ance elegant, fine’ ChSI. dragi, etc. ‘dear, costly’ (11.88). ? lier ae clene, NE clean) and (0HG Kleint 0) Lad (Pras possession’ 7. Skt. ratna- (also ‘treasure, goods’), OHG “id; aes ‘a ad ‘possession’, perh. fr. *rgtno- : Ir. rét ‘thing’ (*rentu). ), OS p (Lat. ue ‘eiches’ Hence Lith. | Walde-P. 2.374. Uhlenbeck 243. OB éad, ee but not in NSB), Skt. mani-, esp. ‘pearl’, etym.? Leinolas . 2.295. inh Pol, klejnot. Walde-P. 2.295 6.73 RING (For Finger)
11167:Fr. bague, fr. Prov. baga, Lat. bdca, bacca ‘any small round fruit, berry, a pearl’ (Fr. baie ‘berry’). REW 859. Wartburg 1.196.
11207:1, Grk. dpuos, fr. the root of etpw ‘string together’, Lat. serere ‘bind together, en- twine’, ete. Cf. ON sérvi ‘necklace of ae pearls, or the like’. Walde-P.
15009:scr. burg Miklosich, Tirk. El. 7. Skt. vedhaka-, vedhanika- ‘instru- purge Be ich 363) ment for piercing pearls’ : vidh- ‘pierce’
34947:4. Goth. sarwa (pl.; renders dma, mavordia), OE searu (also ‘cunning’), OHG saro, gisarawi, MHG sar, geserwe, cf. ON sgrvi ‘necklace’ (of pearls or precious stones), prob. : Lat. serere ‘join, compose, contrive’, Ir. sreth ‘row, serics’, Grk. dpyos ‘necklace’, etpw ‘fasten to- gether in rows, string’, etc. Walde-P. 2.500. Falk-Torp 960. Feist 411.
=== IEC margar ===
=== POK margar ===
=== WLD band3 margar ===
=== AHD margarites ===
725:[margarités. Pearl. Greek noun of Oriental origin (prob- ably immediately from Iranian). Greek margarités, mar- garon, pearl: MARGARIC, MARGARIC ACID, (MARGARINE), MARGARITE!, MARGARITE?.]
1818:MARE? mori- MARGARIC margarités MARGARIC ACID margarités MARGARINE margarités MARGARITE! margarités MARGARITE2 margarités MARGIN merg- MARGRAVE gravo-, merg- MARICOLOUS mori- MARICULTURE mori- MARINARA mori- MARINE mori- MARITAL mari- MARITIME mori- MARK! merg-
```


## [2026-09-04T19:18:32.021Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM leaf 145 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==146' AFM_pages.txt | head -30"
}
```


## [2026-09-04T19:18:33.338Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA (Asbaghi) ===\"; grep -n -i -E 'murwarid|morvarid|marǧān|marjan|marġān|Perle' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -30"
}
```


### [2026-09-04T19:18:33.581Z] TOOL RESULT

```
=== AFM leaf 145 ===
ܓ 1 ܐܐܠ
( ܕܙ يون ) سجر ورقة ܐ الزيتون وزهره الى !ܐܩ له ثر كالكير تعريب
2س © ܣܦ
مازر بون
83 اكرت) . 5( بلا ننات وقتل الارض لا مجن 355 ` مرعاها‎ (١+
ܨܝ‎ 3
> ماخوذة عن مرده ܕܘܫܐܐܬܐ‎
* ( !]ܨ ܢ ܣܣ رس ج فقيل ܝܣܝܣ ܤܣ
قات فان كان ܥܠ المرداسنج فهو ܨ عن ܗ ع ܕܬܕ | ܝ امرداسنج ٠‏ وان كان
ون و اموه رج ار ܣ اطبا رن
الفارسى عروه تصحيف العرلي الأروح
15 صغار ,+ شيل كيار الدر ܡ وقبل 2 جان 1 , 0 :
وقال 3990 لا ܨ تانق هو ام م داعي ܨ تقدير زيادة < ܝ 3
5 58 الاصل ٠‏ قلت 0 1 قيل هو مر ‫ من مر وهي من ادوات
التريين ومن جان ومعثاها الروح ٠‏ وهده لكايه موحودة 0 اللغفات فى
مرجان ܙܡ 40 والكر د و تش لحدداة ܐܐ بالارامية 0 أو 03
15 .2 ( 5 : ` 1 ܕܢ 95:5 00 5 26 ܕ 1113101101116
(ننات) بالفرنسة ٠‏ ومرواريد بالنارسة و ܡܪܓܠܝܬ و ܡܪܓܠܝܬܐ ܨ 1
باللعة ;+ والم ابلمة 5 ܐܠܘ ٠‏ ܢܦܐ 9 اصلها فارسي ܨ 87
اله ول. ܚܝ .1 وهو ܥܐ من 00000 5 15 ܀ وعنلدي 0 اصل الكلمة
ܨ ܢܨ ܐ ܡܝ فعل © < 5 35 289 وا سم الفاعل لودل
دح حنسط »ع فخدفت الماء ونقات ܐ الى > وحركة الراء الى اليم فصارت
3 1 7 عن 9 صبغة }1 9
المحرق
( الرْرَئحوسُ ) من الرياحين دقيق الورق بزهر ابض عطري تعريب عرزن كرش
```


### [2026-09-04T19:18:33.630Z] TOOL RESULT

```
=== PLA (Asbaghi) ===
17952:ob. _ marfän: "kleine Perle" aus pers. +1. morwarid Io mp. ae 
18612:L>- mina: "Glasperlen" aw. minu °.
```


## [2026-09-04T19:18:40.552Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17930,17975p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt\necho \"=== page via PLA_pages.txt ===\"\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'marfän' in p or 'marǧān' in p or 'marğān' in p or 'morwarid' in p or 'morwārīd' in p:\n        print('--- leaf(1-based)',i+1,'printed',i+1-15)\n        print(p[:1500])\nEOF"
}
```


### [2026-09-04T19:18:42.481Z] TOOL RESULT

```
6. Nyberg Bd. II s. v. 

7. ebda. 

8. Mayrhofer S. 130. 

9. Brockelmann s. v. 

10. Macuch s. v. 

11. Wahrmud s. v. 

12. Muhit s. v. 

13. al-MuCarrab s. v. 

14. Mackenzie s. v. 


marän 247 marzubän 


ob. _ marfän: "kleine Perle" aus pers. +1. morwarid Io mp. ae 
morwärid 2, murvärit, mprth. mwrg’rOyd re griech.napyaffr}$ 3, 
mand. marg(a)nita 4, 


d 
ab - murdärsang: "Bleiglätte" < pers. u) murdarsang > mp. 
Id, murdär v. om Mmurdan Ber sang MP. „„ sang 7, 


er - murdäsang = murdärsang q. v. 


ul _ murdasank = murdärsang q. v. 


“ 
VI - murdaquS: "Majoran'"' pers. 8 u mp. wis marzangoS 9 syr. 
10 
Es x 1,9 . 


3, 
Or»2r - mardandüs = mardagüs Ss. % 11, 
=== page via PLA_pages.txt ===
leaves 302
--- leaf(1-based) 262 printed 247
marän                                                                        247                                                      marzubän


ob. _ marfän:                      "kleine             Perle"        aus pers.               +1.            morwarid      Io mp.           ae
       morwärid           2, murvärit,                        mprth.        mwrg’rOyd             re griech.napyaffr}$                     3,
       mand.       marg(a)nita                      4,

                                                                                                        d
ab             -   murdärsang:                      "Bleiglätte"                 <        pers.   u)              murdarsang          >        mp.
        Id,          murdär v.                    om          Mmurdan Ber                   sang MP.               „„ sang       7,

er          - murdäsang                      = murdärsang                  q. v.

ul          _ murdasank                      = murdärsang                  q. v.

 “
VI          - murdaquS:                   "Majoran'"'           pers.           8 u        mp.    wis            marzangoS       9      syr.
                         10
       Es   x      1,9         .




 3,
Or»2r - mardandüs                            = mardagüs              Ss.    %        11,


—Ii--       mirzäb:                "Wasserleitung,                     Kanal"             pers.     12 eg mp.        oM marz              aw.
       marsaza
```


## [2026-09-04T19:18:52.746Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\n# find pdf page tags\nfor i,p in enumerate(pages[:3]):\n    print(repr(p[:120]))\nEOF"
}
```


### [2026-09-04T19:18:54.599Z] TOOL RESULT

```
leaves 553
'[pdf page 1]\n'
'[pdf page 2]\nه\nو سم\n۰ و\nالب\nاس ی 9 ۱\nعه ر جر ن\u200cخلف بربری لیر رها\nّف\u200cبال ۱۰۶۲ #کک .\nناس مد ی «چا لد ولوح ا!\n۰ ً ّ ۰ ,7 اس'
'[pdf page 3]\nاداره کل نکا زشن"\nساره ۰۱/۹/) \u200e٩۰9\u200f ی\nثاریم موم : ار\n۴ رِ وزارت میت\nد انشمند محتر \u200f آقای د کتوحمد معین\u200cاستا'
```


## [2026-09-04T19:18:57.980Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor pdf in 79 80 81 63 64 65; do\necho \"===== pdf page $pdf (printed $((pdf+1917))) =====\"\nawk -v n=$((pdf+1)) 'BEGIN{RS=\"\\f\"} NR==n' incoming/BQT/BQT_v4_pages.txt | head -50\ndone"
}
```


### [2026-09-04T19:18:59.465Z] TOOL RESULT

```
===== pdf page 79 (printed 1996) =====
[pdf page 80]
-۱۹۹۷- مرولرید بتن
و عربان رسان‌الیوخ وحبق‌الفیوخ خواشد ۱ - مرو - بنم اول بروزن خرما. فالنيك
وسنگه آتش زنه را نیز گفته‌اند ۴ - ونام‌شهری و دعای خیر باشد ۴ .#8
هم هت در خراسان مشهور بمرو شاهجان ۳ . مرواردید بسن - کنایه از خدمت

۹ - پهلوی 132۳۵ « اوتوالا ۴۵۱۷ * مرویه . خوحبق‌الشیوخ . وخوالمرو . وحوالشناره
وهوالشر بت » وحوالزغبر ( الزعتن ؟ ) واسمه ,مجمیةالاندلی منتراشة .» « عقاره ۲۳ » لوق کوید:
8۷ نام سربانی- فارسی(قولری]1 ۰ ۱۱۹۸) 47882016 0۲:82 با 8۲۷ 08890
( .رآ 12۲۵ 0۲188080 ) است که نیز در فارسی مرماحوز با مرماخور نامیده میشود « عقاو

۳۵۱ ف > ۴ - دزی (ج ۲ اس ۵۸۵ :۲ ) حجرالمرو را بسنی 00866 016۲76
(سنگه پا ) آورده است - ۴ - ودیداد آ:٩‏ 31005۷ ۰ در پهلوی 31۵۲۷ , پشکل

لهجه‌بیی« مرغ > ( رك : مرغز ) نیز آمده . رك : مار کوارت . شهرستانهای ابراشهر 4۹-460

دو شهر در خراسان قدیم « مرو » نامیده شده‌اند : مروالروذ » شهرست نزديك مرو الغاهجان و

بین‌آندو پنج روزه مصافت است. ومروالرون برکنار نپریست عظیم . وبدین جهت باین نام خوانده

شده و این مرو دبت پمرو دیگن کوچکتر است و دبت بدان مرو روذی و مروذی است -

مروالشاهجان ۰ مرو بزرکست ومشهورتربن شهرهای خراساست وسبت بدان مروزی است‌برخلاف

قیالی و « وب مروی » طبق فیلی کویند . بین مرو و لیشابور هفتاد فرسنگه است و از آنجا با

سرخسی سی فرسنگه و تا بلخ صد وبیست و دو فرسنگه است « ممجم‌البلدان ».

۴ - شد : مرغوا (ه.م.) [ شاهد در مرغوا آمده ] -

۵ مروارید - بنم اول پپلوی 130۳۷2۴14 «تاوادیا۱۹۴* ۰ ازیونانی 228780251185
« ابا س ۳۹۳ » بعریی لوْلو « تحفةٌ حکیم موّمن » , در ! جسمی‌است سخت , درخشان, صدفی ‏
و هدور در درون بعی حیوانات صدفی مخصوصاً صدفهای مرواربدی تکوین میشود وآن در اول
نغوء سبلان دارد »سپس منجمد و سخت کردد . برنگه سپید دری درآید. نو کیبات آن عبارتت
ازآب, موادآلی وکاربنات دکالسیوم . و آنرا غواصان‌ازاعماق درباها ( از بحراحمرتا استرالیامخسوماً
حوالی سراندیب و خلیج فاری ) صید‌کنند. درافانه‌های‌قدما
آمده که صدف‌بهنگام ان ببالای آب آید و دان بگشاید / ات
وقطره باران را ببلمد وهمان قطره پمروارید بدل شود . رك : 7
الجماهر, تمه کناب ۰۷-۱ ورك : بوستان سعدی چاپ‌قرب 9 ها
سا اک

۳۴ 5ج : ۳ : ِا کت

2 یا هب 13 2 اسیه وی
ی خرن ۱ ۱ و
۱۹ 17 ری ۹۹ ۰ جاک
یت سک آهسشگکگ

مرواریدهای درخشان داغل صدف صید مروارید وغوامان

===== pdf page 80 (printed 1997) =====
[pdf page 81]
مروای ليك ۱۹۹۸
و منصب لو یافتن و ترقی دز احوال بهم رسیدن | حطی . لغتی است.یونانی بممتی مرزنگوش وآن
بلشد - وکتایه از خجل شدن و خجالت کشیدن | دوائی است که عربان آذان‌الفار خوانند -
هم‌هست. . مروسیدن - با وار مجهول و سین‌بی

همروای فیک < بسسنی ذفال نیک | نقطه بر وزن خموشیدن , بممنی اعادت کردن
باشد ‎٩‏ - و نام لخن بیست و دویم است از سی | بچیزی باشد۸ - ورنج بردن بکاری دروقت مفلسی
لحن بارید ۴ . و بی‌چیزی ۸ .

مروخوش - بسمنی اول مرو است مرش - بروزن خموش . منم‌ازروشن
وآن کیاهی باشد خوشبوی . کردن است بعنی روشن مکن ‎٩‏ .

مرود؟ - جم اول بر وزن سرود ۰ مروشهجان * بمعنی مروشاهجان
مخفف امرود است وآن میوه‌ای باشد معروف که ات که شهر مرو باشد و آن شهرست از
عربان کمثری گویند . خراسان .

مرودشك؟ سبکسررای بی‌نقطه‌وسکون هروه جم اول وفتح‌نالت مشدد وظهور
شین نقطه‌دار وکاف . تشم مرو راکویند و بعربی | ها » پمعنی‌مروج است که سخت خوشبوی ومعطر
بزر المرو خوانند ۰ کننده باغد واین دراصل‌مروح ۱۱ بوده. فارسیان

مرو دود * - رودخانٌ مرغاب است - | بجعت استقامت قافیه حای حطی‌را بهای عوزبدل
وشهر مرو در کنار آن واقع شده ء و نام جایی کرده اند» همچنانکه در قفص صاد بسین بی‌نقطه
هم‌هت . بدل شده است .

مروری۹ - بر وزن ارمنیه . نوعی از مریگ -« بکر اول و تحتانی مجهول بر
کاستی صحرائی باشد ۰ و بسنی کوبند نوعی از | اوزن هری . بمعنی کوشیدن وبرابری کردن باشد
کاهوی تلخ است ‎٩‏ باکی در قدر و مرتبه و بزرکی ۱۳- و بمعنی

هراس اقطی ۷ « بفتح اول و کسر خصومت کردن و بکدله بودن در بد کرداری هم
سین بی نقطه و همزه و اسکون قاف و طاوابای | کفته‌اند ۱۴- ویمهنی‌مژ دگانی‌نیز آمده است۱۴-

۹ -ر4: مزوا ۴ - درخسرو وشیرین نظامی‌نام لحن‌چپاردهماست . ر: آوازهای

قدیمی ایران‌بقلم جمال‌زاده مجلةٌ موسیقی ۲۷: ص4-۳- ۴ - ر4: امرود .

۴ - از : مرو(ه.م )+ رشك (ه.م.) * - پپلوی 1۴ ]۸12۳۷۳۵4 «اونوالا6۱۹

8 . معرب آن مروالروذ . رك: ح۳ صفحهٌ قبل . ‎٩‏ - «مروربه » نزد بعتی‌خند ریلی
(«.م.)ونزد بسی‌کاهوی تلخ‌شیرداراست #تحقة حکیم مژمن» دزی (ج۲ ص۷۷) گوید: مروزیه
قمی ازکاسنی بری» با کاهوی دشتی‌است ؛ هندیا! خی‌بری. ۷ - جزء اول مصحف‌پونانی
0۶8 لانینی 232۳3018 ( مرزنگوش ) است « مرچنت ۳۳ > جزء دوم اقطی . در
بوئانی 81616 بممانی ذبل است : دماغه , ساحل » کنار رود - غله - آرد « لیدل واسکات >.

۸ - ر4 : جهانگیری » رشیدی . ‎٩‏ - رل : روش .
۹ مروشاهجان . رك : ح۳ صقحهٌ قبل ۰ 9۱- (ع) اسم فاعل از ترویج -
۴۳ عمال «* مراء > (یکر اول) بمعنی‌پیکار کردن و جدال نمودن ( راه :منتهی‌الارب)

ورك : رشهدی :

===== pdf page 81 (printed 1998) =====
[pdf page 82]
-۱۹۹۹- هز
و در عربی پا تشدید ثانی ۰ ارکی را کویند که | مریح ذلب‌فعل زحل سیما هم میگویند.
گذرگاه آب و نان است ۱ - و بضم اول:آنکه مریخ زحل‌خو اد -کنابه ازآش
نوبت خود را در شراب خوردن بدبگری ایثار | انگشت وزغال‌است‌بمنی‌زغالی که اخگرشده باشد
کند - و در عربی با تشدید انالی » آبکامه را | نه چوب وهیزم ‏
گوبند و آن خورشی است مشهور خصوصاً در مریخ سلب - بفتح سین بی‌نقطه ولام
سفاهان ۴ . و سکون بای ابجد , کنایه از لبلی سرخ است-

مریافلن ۴ « جنم اول وسکون نانی | وسرخ پوش: را نیز کوبند .
و تحتانی بال فکشیده وکسر فا ولام مضموم بنون مریخ و کیوان دیدن «کنابه از
زد » لفتی است بونانی و ممنی آن‌بمربی ذوالف | انگشت و زغال نیم سوخته در منقل دیدن باشد.
ورقه باشد » ون پیخکیاهیست که از شام وبیت مری ز بافات - بنم اودونانی بتحتانی
المقدسآورند وآنرا حز ببل‌نیز کویند. کزن کی رسیده وقتح زای تقطه‌دار وپای ابجد پالف کفید.
مار وعقرب را نافع است . و نون مفتوح بکاف زده . نام دوائی است که
مرخ -بکر اول . نام کوکبی است تخم آن رابار تنگه خوانند و خوب کلان همان
ازجملة سبعةٌ سیاره ودرآسمان پنعم میباشد۴ - | است ‎٩‏ .
و کنایه از انگشت و زغال افروخته است ‎٩‏ - مر یشم - بنتح اول و نانی به نحتانی
.وباسطلاح اهل صنمت که کیمیاکران باشندآهن | مجهول کشيده وشین نقطه‌دار مضموم بمیم زده »
وفولاد - خسته بندرا کویند وآن چیزی‌باشد که برجراحت
هریخ آفقاب علم - کنابه از آش بندند ۷ .
شمله‌ناك است ۰ مریم و2 - باعین بی نقطه و ولو
مریح "ذنب فعل < کنابه از حلقة | ورای قرغت .کنایه از شاخ درخت انگور است
زنجیر است که بر پای, ستوران گذارند وآن را | در ایام خزان و برکك ریزان .
بیان دوازدهم
درمیم با زای نقطه‌دار مشتمل بربست وشش لفت و کقایت
هز « بنتح اول و سکون ناتی . بمعنی | بمك ۸ - و بشم اول و اسکون ثالی مشعدد , در
مکیدن باشد ۸ - و ار بمکیدن هم‌هست بمتی | اعربی بمعنی ترش وشیرین باشد که آلرا میخوش
۱- (عر) « مری+کامیر .کلوی سرخ مردم وگوسیند وج زآن و آن سرمعده و شکنبه
است چبیده بحلقوم. » * منتهی‌الارب *» درفارمی بدون همز‌آخر تلفظ شود .
۴ - رك : .منتهی‌الارب . اقرب‌الموارد . محیطالمحیط .
۴ - از یونانی ۸]۵۳1۵00۱1100 > عاازباه۴ - 6اه (فر) « دزی ج؟ ۹۸۹ >
۴ -عربی امت و بفارسی بهرام کویند . 8 - رك : مریخ زحل‌خوار .
‎٩‏ - آنرا خوب کلان و بهندی خوب کلا خوانند « رشیدی » .
۷ - رك : جهانگیری ۰ رشیدی . ۸ رد4 : مزیدن .

===== pdf page 63 (printed 1980) =====
[pdf page 64]
-۱۹۸۱- مرجان
و بای آبجد بواو رسیده ویای حطی بالف کشیده, مرج - بغتح اول وسکون نانی و جیمء
بلفت زند وپازند (۱) بمعنی‌خریزه شیرین باشد. | بمعنی مرز است که زمین باشد ‎٩‏ - و زمینی را
ودر نخةٌ دیگر خربزة میان دربا ۱ نوشته شده | نی زکویند که کنارهای آنرا بلند ساخته دردرون
بود ویرهیج يك شاهد تیاورده بودند » ااعلم . آن چیزی بکارند (۷) - ونام شهری هم هست در

مرت - بفتح اول وسکون ثانی‌وفوقانی. | کوهتان سمرقند ۷ ؛ وباین معنی چم اول لیز
بمعنی زنده باشد که درمقابل مرده است ۳ . آمده است - ددرمر ی بمعنی‌ازهم کشودن وبچرا

داد دادن دواب و چراگاه و مرغزارباشد - وبغت
مرقلش ۴ - بنم اول و نت فوقانی او وتالی هم درعیبی خطمی سحرانیراکوبنگ

و سکون ثانی و کاف ۰ چیزی است. که ادا | و بیعنی جنبیدن انگشترباشد درانگشت- ویممنی:
مرداسنگه خوانند ومعرب‌آن مرداسنج است۴ ۰ | جنییده شدن و تباه کردیدن و آشفته کشتن هم
در مرهمها بکار برند . اکرقدری ازآن درسر که | یت ۸ .
اندازند رکه را شیرینکند . مرحجان - بر وزن ارزان . بسمنی جان

مر تکو؟* - با کاف بر وزن لبلبو » | است که با لفظ من که آن از الفاظ زایده است

کنجعك راکوبند و بعربی عصفور خوانند. ملحق شده ‎٩‏ - و درعربی جوهرست سرخ *۱.

() چك : ژند وپاژند . (۷) چش : بکاربرند .

۱-ظ . « خربزه » را درمأخذی بتصحیف « جزیره» نوشته بودند وبرای توضیح «میان
دربا » را بدان افزودند » برهان « جزبرء میان دربا » را ( که آنهم غلط است ) * خریزه مان
دربا » خوانده ‎٩‏

۲ - پهلوی 12871 . اوستایی - 1327312 * بارتولمه ۱۱۶۸ » ورك : لیب رکلس ۰۱۶۹
بمعنی هرد » مردتی ( رك : مرد ) و اظ. عوّلف در تخه‌ای جملةٌ « بمعنی مرده باشد که درمقابل
زنده است > را دیده بوده و اشتباهاً صورت متن درآورده است . ۴ - پپلوی کاها1207
( مرده ) + ۴ - رك : مرداسنگه » مرده سنگه . رك : مرگو.

‎٩‏ <مرز (هم.) ۷ - چند موضع درمعجم‌البلدان بنام « مرج *آمده آماشهری
در سمرقند ذ کرشده . در حدودالعالم ( ص ۸۳ ) در ( سخن اندر ناحیت جبال و شهرهای ری )
آمده : « اساباد . کرمانقاهان » مرج » شهر کهایی‌اند برره حجاج انبوه وآبادان و با نعمت >

‏۸ - رك : منتهی‌الارب , محیطالمحیط . ‎٩‏ - درین صورت « مر > متمم هعنی
« را > است و با « جان > ترکیب نشده . ۴ مرجان كلمة مخفف عردی از لغت سربانی
878۸2 < دزی ج ۷ ص ۵۷۸ که لت بمعنی مروارید بوده واسپس به بد اطلاق
شده است . ۳161801067 در ۶ تبعات در بارة ذیل قوامیی عرب تألیف دزی > ۱۸۸۹ ان ۱۷۹
تغییر الغت بونانی 1278271188 را به 13878611108 و در آرامی به - 1327881114 و
44 که ازآن شکل عربی 17127[28 اتخان شده » شرح میدهد « عقار ۲۲۷ اف هتن
و حاشیه » . ورك : نخب الذخاثر صس ۸۸- ‎۸٩‏ . - مرجان بممنی متداول ( 00781 ) قسمی از
جانوران مرجانی ( 0010167 ) است که بدن آنپا بر اصل تقارن شعاعی ساخته شده است,یمتی
اعضنای مختلف آنها دبت بيك محور قربنه میباشد . مرجانها غالباً در دربا زندکی میکنند. بدن
آنها شبیه بکیسه‌ای دو جداره است . حفرة داخلی‌بدن مر‌جانها بوسیلةٌ سوراخی بخارج راء دارد.
این سوراخ هم بمنزلةٌ دهان و هم بجای مخرج جانور است. .

===== pdf page 64 (printed 1981) =====
[pdf page 65]
مرجان_پرورده -۱۹۸۲
گوبند از دزیا میروید ‎٩‏ - و مروارید ریژه را بنظرآهده است .
نیز کوبند ۰ 8 مرجمك ۳ « بروزن مردمك,غله‌است
مرجان‌پروارده- ورهار :را که بعربی عدس خوانندش .
کنایه از لب ممشوق رن مرخُشه - باخاوشین
ومحبوب‌است- و کنایه ۳ قطه دار بر وزن اقمشه » در
از شراب انگوری هم 09 با فرهنگه ۴ بمعتی سخن باشد
هست .. ۰ ط که کلام است. ودرجایی دیگر ۰
مرجاده()- 2 : بر وزن طبقچه بمعنی نحس
بفتح اول ودال ایجد » ونامبارگوشوم نوشته‌اند » واین ‏
آلتی‌باشد کهآ تراماند مرجان اسح است چه گفته‌اند که : َ
جوال بزرگی از چرم میدوزند وپرازگاه میکنند آمد نورو ی پا 1 مرجم
و بربالای آن اسباب میگذارتد و مردم هم سوار برئو خجسته بخضم باد مرخشه
میشوند و ازآب میگذرند ؛ و بجای دال واوهم مرداب - با دال|بجدپروزن‌چرخاب9 »
() چنین است درت نسخ ولی کلمه درردیف خود نیامده امت . ۰
۱ -« مرجان » بد باشد و تازبان کوبند لوْلوْ باشد . فرخی ( سیستانی ) گفت :
تا مورد سبز باشد چون زمرد تا لاله سرخ باشد چون مرجان.»
« لغت فرسی *۳۹ -
۲ <مرجومك « فرهنگه نظام > < مرجو < مرو « مقدمة الادب زمخشری اس ۰*۱۶
طبری 73871 ( عدس ) . مازندرانی کنونی 722 « واژه نامه ۷۱۵ > : کیلکی 131121772
( عدس ) . رك : هرمزدنامه ی ۱۶۹ حخ۱ - ۴ - مراد فرهنگك جهانگیری است .
۴ - « مرخشه . نحس باشد . منجيك ( ترمذی ) گفت :
آمد توروز و نو دمید بفشه برها قرخنده ناد و بر تو مرخشه . >
و بنابرین «سخن» در متن مصحف « نحس > است . لغت فری‌س5۹۱ >
- رشیدی وجهانگیری وانجمن‌آر! بفتح میم ضبط کردماند » ولی درتداول0 1220۳42
کویند . رضاقلی هدایت نوشته : «غالباً در آب غیر روان استممال میشود که ایستاده و ح رکت
تمیکند ... ومیتواند شد که پم میم مرداب گفته باشند یمنی آب مرده وبیخ ر کت» «انجمنآرا».
۵ هرد - بفتح اول. پپلوی 133871 ۰ اوستابی - 17187918 « بارتولمه ۱۱۶۸ «نیی رکه
۰۱۶۹ قی : پارسی باستان - 12871198 ( انان » بشر ) . عندی باستان - 1338712 ۰
ارمنی 3870 ( انان ) , بلوچی 13387 «اسشق۹۷۲ لغة این کلمات بمعنی‌در گذشتن وفناپذبرند
ازربشه 3387 ( مردن ) [ ر4: مردن ] درگانها 1718۳318 و 13328802 ( ازهمان ريشه ) بعمنی
اسان وبشر و در گذشتنی‌آمده * بشتها ۱ص ۹۹ کردی ع 3267 ( مضی . جوانمرد ) « ژابا
می ۳۹۸ 017 ( انان ) « ژابا س ۰۳۹۲ ۰ اورامانی 3217081۳86 « 4 . اورامان ۰۴۱۲۶
کیلکی2376 ۰ فربزندی 33270 ۰ برنی 33678 ۰ نطنزی 2178 43 . ۱ص ۲۸۸ *صمنانی
4 و سنگری 336786]0 ۰ سرخه‌بی ۳1741 . 3370 ۰ لاسگردی 117086 ۰
شهمیرزادی 23870 ۸« 4 . ۷ س۱۸۵ > ؛ جنش نرینه از انان ( مقابل : زن ) - دلیر؛شجاع-
سخی . جوانمرد - شوه .

===== pdf page 65 (printed 1982) =====
[pdf page 66]
۱۹۸۳۳ مرداسفرمٍ

تالاب و استخر وآبگیر عمیق پرعرض و طول را | واين جشن را جشن لیلوف خوانند ودرین روزهی

گویند . حاجتی از پادشاه خواستی(٩)‏ البته روا شدی .3
مردا3 ۱ - بنم اول بر وزن خرداد , مر دار خانه - خانه ای راگویند در

نام فرشته ایست موکل بر قصل زمستان و ندبیر بازی نرد که مغرء در آن خانه در ششدر باهقدر

امور ومصالح ی که در ماه مرداد وروز مرداد واقع | افتد و نتواند بیرون آید () .

سامت راو من اج ی ۱ هردامفر دب ان ۲ کر

کوس ص و

شمسی ؛ و بعضی روز شم ند؛ و قاری

بنایر قاعده‌کلی این روز را عید کنند وجشن‌سازند مرد اسپر ۴ هم میکویند با بای فارسی.

(۱) چنین است درنسخ » وصحیح : خواستندی. () چك : یرون آمدن .

۱ - اسح « امرداد » است. در اوستا ۸۸7۳36۳6121 مرکب از دو جزه : جزه اول خود
آازدو جزء تر کیب شده :8۱ ( ادات نفی بمعنی نه )+ 126۳018 ۳ 11127312 ( مردتی ودر
گذشتنی ونیست شدنی و مردم ) از مصدر 3387 اوستایی و پارسی باستان پمعنی مردن . جزعدوم
« امرتات » 181 است که پوند و دال بر اسم مجرد موت است . پس امزداد یعتی بی مر که و
سیب ندیدنی یا جاودانی, بنابرین « مرداد > با حذف <۱ > درست معنی‌مخالف امرداد رامیدخد,
ولی گویندگان و نویسند کان در شس ونثراستعمال کرده‌اند . امردا دکه پنجمین ماه سال وهفتمین
روز ماه بدو سپرده شدهء از امشامپندان و مظپن جاوبدانی اهورمزدا و در جهان مینوی بخشایش
ایزدی جزای کارهای نیکو کارانست . در جهان خاکی نگهبانی گیاه با امرداد است . استرایون
مورخ پونانی معبد آمر‌داد را درآسیای صفیردیده است. امرداد روز ازماه امرداد جشن«امردادکان»
بریا میشده . بیرونی در فهرست روزهای ایرانی این روز را * مرداد ؟ و درسقدی «* مردد » و در
خوارزمی ۸« همدان » بادکرده . زرتشتیان ایران هم آترا « امرداد » خوانند :

مرداد مهست سخت خرم می نوش پیاپی و دمادم -
* مود سعد همدانی لاهوری اس ۹۵۹ ۰
روز مرداد مژده داد بدان : که جهان شد بطبع باز جوان -
‎٩ ۲‏ مفود قداص *۹۹ 6

۴ ۳ مورداسپرم » از : مرد (< مورد )+ اسفرم ( ۳ اسپرم ۳ اسپرهم [هم.] ) <
06 139۷۲6« دزی ج ‎٩‏ ص ۹۲۳ :۰.۲ ۴ - اسح جم میم است .

2 مردار - بم اول » از : مرد ( از « مردن > بضم میم ) + ار ( یوند ) » پهلوی
7 ۵ دارمتتن . تبعات ج ۱ص ۲۸۳ > کردی 1331۳78۲ ( مزیله ) « ژاباص ۳۹۳ ۰4
کردی ع 1307487 (کلیف . پلید ) « ژاباص ۳۹4 ؛ جانور مرده ( که ذبح شده باشد ) ۰
جد مرده :
هر که چون کر کس بمرداری فرود آورد سر کی تواند همچو طوطی طمع شکر داشتن ؟

۱ « سنائی غزلوی ص ۳۹۷ -
```


## [2026-09-04T19:19:26.211Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON morvarid ===\"; grep -n -o -E '.{120}مروارید.{200}' MON_part2.txt MON_part1.txt | head -8\necho; echo \"=== MON marjan ===\"; grep -n -o -E '.{100}مرجان.{200}' MON_part2.txt MON_part1.txt | head -6"
}
```


### [2026-09-04T19:19:26.313Z] TOOL RESULT

```
=== MON morvarid ===

=== MON marjan ===
```


## [2026-09-04T19:19:28.512Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index margarit/pearl ===\"; grep -n -i 'margarit\\|morvarid\\|marvarid' incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== ARY pages مروارید ===\"; grep -n -o -E '.{80}مروارید.{160}' incoming/ARY/ARY_pages.txt | head -6\necho \"=== ARY مرجان ===\"; grep -n -o -E '.{60}مرجان.{120}' incoming/ARY/ARY_pages.txt | head -4"
}
```


### [2026-09-04T19:19:28.595Z] TOOL RESULT

```
=== ARY latin index margarit/pearl ===
=== ARY pages مروارید ===
=== ARY مرجان ===
```


## [2026-09-04T19:19:33.227Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt incoming/ARY/ARY_pages.txt; do\necho \"--- $f size $(wc -c <$f)\"; grep -c 'مروار' $f; grep -c 'مرجا' $f; done"
}
```


### [2026-09-04T19:19:34.697Z] TOOL RESULT

```
Exit code 1
--- MON_part1.txt size 4377831
28
3
--- MON_part2.txt size 4331421
52
25
--- incoming/MON/MON_2vol_Adena_v2_djvu.txt size 4331421
52
25
--- incoming/ARY/ARY_pages.txt size 960497
1
0
```


## [2026-09-04T19:19:37.610Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON2 مروار ===\"; grep -n -o -E '.{60}مرواری?[دد].{200}' MON_part2.txt | head -12\necho; echo \"=== MON2 مرجا ===\"; grep -n -o -E '.{60}مرجا.{180}' MON_part2.txt | head -10"
}
```


### [2026-09-04T19:19:37.708Z] TOOL RESULT

```
=== MON2 مروار ===

=== MON2 مرجا ===
```


## [2026-09-04T19:19:41.042Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'مروار' MON_part2.txt | head -12\necho \"-----\"\ngrep -n 'مرجا' MON_part2.txt | head -12"
}
```


### [2026-09-04T19:19:41.114Z] TOOL RESULT

```
1140:مرواریدهای بهتر و برگزیده. (کد.) سخنان 
2316:غلتیدن. هر چیز گرد و مدور. مروارید 
2317:علتان: مروارید کاملا گرد. 
3142:برای طلب مرواربد. مرجان و غیره فرو 
3165:مروارید؛ مرجان و عیره. 
3169:آب فرو رفتن به طلب مروارید» مرجان و 
4263:مروارید و جز آن در رشته کشند. آخر اية 
10471:مرواریدی است که نصفی مدور و نصفی 
12872:می‌بافتند. مروارید تر و آبدار. زبرجد و 
22973:مروارید. 
30681:مروارید که زنان گرد چهرةٌ خود بندند. 
36711:مروارید بزرگی که در صدف جز آن یکث 
-----
3142:برای طلب مرواربد. مرجان و غیره فرو 
3165:مروارید؛ مرجان و عیره. 
3169:آب فرو رفتن به طلب مروارید» مرجان و 
19443:فرامی‌نی‌فرها و اسفنج‌ها و مرجان‌ها و 
52627:مرجان: ره [ع. مح. مر وار بد» سب ] 
52629:مرجان‌ها که دارای پایةٌ آهکی است و در 
52633:آهکی مرجان قرمز که جزو احجار کریمه 
52636:شده). مرجان برورده: (کن.) لب معشوق. 
52638:مرجان] رده‌ای است از کسه‌تنان که دربازی 
52640:می‌کنند. مرجان‌ها از جانوران گیاهی شکلند 
52643:مرجان‌ها بندرت دیده می‌شود و غالبا 
52645:شکل خارجی مرجان استوانه‌یی است که در
```


## [2026-09-04T19:19:46.149Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON marjan entry ===\"; sed -n '52620,52650p' MON_part2.txt\necho; echo \"=== MON morvarid headword search ===\"; grep -n 'مروارید:' MON_part2.txt | head; grep -n 'مروارید' MON_part2.txt | sed -n '1,40p'"
}
```


### [2026-09-04T19:19:46.250Z] TOOL RESULT

```
=== MON marjan entry ===
مروج. . (مص‌م.) به چراگاه ۱ 
(مص‌ل.) چریدن چرنده. 


مرج: ۸۲ (ع.] (مصم.) درهم و برهم 
کردن» آشفتن. ابحاد شاد کردن. . هرج و 
مرج. 
مرجان: ره [ع. مح. مر وار بد» سب ] 
(جان.) جانوری است دربازی از رده 
مرجان‌ها که دارای پایةٌ آهکی است و در 
دریاهای گرم می‌زید و دارای انواع و 
گونه‌های بسیار است؛ قورال؛ قرلیون» 
خراهک؛ حجر شجری. (جاذ.) (زم.) پاية 
آهکی مرجان قرمز که جزو احجار کریمه 
است و در جواهر سازی مورد استعمال دارد؛ 
بسد. مروارید (به اين معنی در عربی استعمال 
شده). مرجان برورده: (کن.) لب معشوق. 
(کد.) شراب انگوری. کرجان‌ها: [ج. 
مرجان] رده‌ای است از کسه‌تنان که دربازی 
هستند و اکثر بصورت اجتماع زندگی 
می‌کنند. مرجان‌ها از جانوران گیاهی شکلند 
و بر روی تخته سنگ‌ها در نقاط کم عمق 
دریاهای گرم می‌ز بند. کر انفرادی در 
مرجان‌ها بندرت دیده می‌شود و غالبا 
مستعمره‌های بسیار بزرگی درست می‌کنند. 
شکل خارجی مرجان استوانه‌یی است که در 
قاعده به صفحه‌ای هن روم بصع 
بایی ختم می‌شو د. . سلول‌های صفحه بایی 
جهت ات نگهداشتن حوان مواد کته 
ترشح م‌کند. از تجمع این مواد آهکی 
تدر یجاً پایه‌ای آهکی برای حیوان بوجود 

=== MON morvarid headword search ===
54446:مروارید: ۷۹۵ ۱۱ .۲ ( طبر ِ( جسم جامد 
1140:مرواریدهای بهتر و برگزیده. (کد.) سخنان 
2316:غلتیدن. هر چیز گرد و مدور. مروارید 
2317:علتان: مروارید کاملا گرد. 
3165:مروارید؛ مرجان و عیره. 
3169:آب فرو رفتن به طلب مروارید» مرجان و 
4263:مروارید و جز آن در رشته کشند. آخر اية 
10471:مرواریدی است که نصفی مدور و نصفی 
12872:می‌بافتند. مروارید تر و آبدار. زبرجد و 
22973:مروارید. 
30681:مروارید که زنان گرد چهرةٌ خود بندند. 
36711:مروارید بزرگی که در صدف جز آن یکث 
37007:مروارید رسیده. گوهر شاهوار (شهوار): 
37011:غلطان: در و مروارید. گوهر کان: گوهر 
38413:لول (لولقّی) تر: مروارید آبدار و درخشان. 
38414:کی اکتا للوْی خوشات: مروارید 
38416:مروارید شاهوار» لو فیمتی. لزلق (لولژی) 
38423:(لولژی) مکنون: مروارید پنهان. (کذ 
38427:گوهر او گرد نماید چو ن مروارید 
40296:مروارید است. 
40964:گویند. (زم.) قسمی مروارید به شکل بادام. 
43881:که از آن مروارید بدل می‌سازد از چهل 
47556:مرواریدهایی که بسیار گران باشند با مثقال 
47558:مرواریدها بیشتر در ارو پا مصرف شود. وزن 
47579:متداول‌نیست. مرواریدی که معادل چهار چو 
48886:که غالا مروارید از آن برون آید (فر نظا.) 
52635:بسد. مروارید (به اين معنی در عربی استعمال 
52692:واحد مرجان؛ مرواریدی کوچکد. 
54446:مروارید: ۷۹۵ ۱۱ .۲ ( طبر ِ( جسم جامد 
54449:نرم‌تنان دو کفه‌یی بنام صدف مروارید حول 
54461:مترشحه حول جسم خارجی صدف مروارید 
54471:کونشیولین. پیدايش مروارید در بدن صدف 
54472:مروارید بطور طیبعی کاملا تصادفی است و 
54478:مروارید را در دریا صید کرده داخل بدن 
54481:دانه‌های مروارید را از داخل بدن آنها 
54484:رنگ مرواریدها سفید یا سیاه و با زرد است 
54488:می آور ند. . مروارید سیاه بیشتر در خلیج 
54491:مروارید از احجار کریمه است و در 
54513:تنها مروارید موجود در بدن صدف مروارید 
56904:کشیده (مروارید و جز آن). (شعر.) الف - 
64024:مروارید قیمتی و خوشاب و اعلی
```


## [2026-09-04T19:19:54.054Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '54440,54450p' MON_part2.txt\necho \"=== 52690 ===\"; sed -n '52688,52695p' MON_part2.txt"
}
```


### [2026-09-04T19:19:54.127Z] TOOL RESULT

```
حجرالمرو. 

مروا: 2 اقس. مر غوا] (.) فال نبکك» 
تفأل خیر؛ م. مرغوا. مروای نیک: تفال 
خیر. 

مروارید: ۷۹۵ ۱۱ .۲ ( طبر ِ( جسم جامد 
و کروی شکل و براق نسبةه سختی که از 
انجماد ترشحات مخاط بدن انواعی از 
نرم‌تنان دو کفه‌یی بنام صدف مروارید حول 
اجسام خارجی (یک ریزة شن یا نوزاد 
=== 52690 ===
اشغال شده ابت می‌شود و با آن زندگی 
شترا کی تشحیل می‌دهد. 

مرجانه: (0-)25-2 21۵۲1 [ع. مرجانه ] (ا.) 
واحد مرجان؛ مرواریدی کوچکد. 
مرجچب: 00۵۹2 [ع.] (ص.) بزرک و با 
هیبت» با مهابت؛ مهیب. قربانی شده در ماه 
رجب. ضح. ماه رجب را بدین عنوان
```


## [2026-09-04T19:20:06.255Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'مروار' incoming/ARY/ARY_pages.txt\necho \"=== ARY مات / موت ===\"; grep -n 'مات\\b\\|شاه مات\\|موت' incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY latin index MAT ===\"; grep -n -i '^MAT\\|matador\\|checkmate' incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-04T19:20:06.337Z] TOOL RESULT

```
5549:واژه‌ی فارسی ام" (به چم "تاری چشم" با "آب مروارید") نیز از همین واجریشه است (301۳0143۲۷:1063 و
=== ARY مات / موت ===
245:سارماتی * سغدی * خوازمی + فارسی > پشتو + زبانهای هندوستان شمالی. جهت این موج‌های
279:ویژه سکایی و سارماتی و اوستی)» برعکس لیتوانی و سلتی» دستخوش نو آوری و دگرگونی بیشتری
654:بختیاری ولر) به آنها تحرکك ‏ وگسترش پذیری شگفت‌انگیزی داده بود. ابل‌های سارماتی
1062:رایزنی و اتخاذ تصمیمات مهم از دیرباز رایج بود.
1158:۲170283017۸3 سارماتی (8۸1۸/۸71۸01) برخی از این زبان‌ها مرده‌اند و بقیه (مانند همی .۰
1620:۱ پهلری (ماتلهه): زرا انگلیسی کهن (8#لا80 02): ۰ ۴۲-30
1678:پهلری (7ماتله۳): پسگشت‌ها از ری اد
1903:پهلوی (۲ماتقهه): 3 ار قته9
1983:پپلری (/اماتهم): ۰2۸3۸0 ,۱۸۵۸۵ اسپانبْانیٌ (52۸۸/7877): (شاید) 7 1 8
2075:پپلوی (1/ماتلم۳): 6 ب۸822 ,ات۶0۲۴ ,3۸86
=== ARY latin index MAT ===
367:Mat Sx Fowl Fu Jas
1914:MATTEA {RUMANIAN) ils, MATAYA SANSKRIT) cy Site
1917:MATTOC (OLD ENGLISH) pS padi! MASSE APRENCH) «ii
1918:MATTOCK ENGLISH) gud MAZA LASPANISH) glibysl
13277:MATAR, MATA (SANSKRIT) o4 Sis MADE, MADA, MAD {(OSSETIC) |
13283:MAT’ s(RUSSIAN) (gy 5 MATER HLATIN) 3
13284:MATKA A(CZECH) So MERE FRENCH) Wil
13285:MATL ASERBIAN) «go MADRE SPANISH) lhe!
13286:MATKA, MATT (BOHEMIAN) san y MADRE AUTALIAN) g\Sy\
13287:MATKA (SLOVAK) 1 La} MAMA HRUMANIAN) gley)
```


## [2026-09-04T19:20:07.665Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT mate/checkmate/mat/matador ===\"; grep -n -i '^Mate\\|^Checkmate\\|^Mat\\b\\|^Matador\\|Check.mate\\|shah mat\\|Pers\\..*mat' SKT.txt | head -20\necho \"=== SKT check ===\"; grep -n -i 'checkmate' SKT.txt | head -10"
}
```


### [2026-09-04T19:20:07.741Z] TOOL RESULT

```
=== SKT mate/checkmate/mat/matador ===
3328:Check,  a  sudden  stop,  repulse.  (F.— Pen.)  M.  E.  ehek.  a  stop ;  also  check  I  in playing  chess.  The  word  is  due  to  the game,  which  is  very  old.  The  orig.  sense of  check  was  '  king  1  ie.  mind  the  king«  the king  ii  in  danger.  —  O.  F.  esehec,  '  a  check at  cDe«»-p1ay,'  Cot.  *  Pers.  xAjM,  a  kinc, king  at  chess ;  whence  skAh-mAl,  check- mate, Ut.  *  the  king  is  dead.*  from  m^t,  he is  dead.  Simibrly  we  have  F.  hhte,  a check,  repulse,  defeat,  pi.  iihe<$,  che^ ; Ital.  scatcQ,  a  square  of  a  chess-board,  also a  check,  defeat.     Sec  cheaa  below.
10942:mate  (i),  a  companion,  comrade,  eqtint. (E.)  M.  E.  matt,  a  comipiion  of  the  older form  maie,  a  companion,  which  is  the commoner  form.  (So  also  ^/,  □  mammal, from  M.  E.  6aJk\  and  esp.  note  O.  Fries,  matia (for  rftaJkta*),  to  make,  which  is  a  related word.)*  A.  S.  mofa,  a  companion;  also gemaca.  +  Icel-  wah',  Swcd.  maJtt,  Dan. magt,  O.  Sax.  gimako,  a  mate,  comrade; but  O.  Du.  wait,  Du.  maat,  a  mate,  with  / as  in  English,  douhtic*^  on  O.  Frie-iic  form.
11211:MATERNAL.
11212:Mat  (L.)    M.  E.  matu.    A.  S.
11214:Matador,  the  slayer  of  the  buU  in bull-fight.  (Span.  — L.)  Span  mata^iar,  I slayer.— Span,  motor,  to  kilL^L  macta to  kill.  orig.  to  honour  by  a  sacrifice.  C Skt.  maA,  to  honour.     (y'MAGli.)
11217:Mate  (i).  a  companion  ;  see  Make.
11218:Mate  (3),  to  check-make,  confound. -•Pen.  &  Arab.)  From  the  game  of CAeck-mate  meant  'the  king  ia  dcad.'»(X etcAt<  tt  mai,  check>niate;  Cot-     [Heft is  not  wanted.]  — Pers.  shAk  m4t»  the  ' is  dead,  check -mate.  — Pers.  sA^k,  kinf Oheok) ;  midt,  he  is  dead,  from  Arab. mita^   he  died.    Cf.  Heb.  nuVi,  to %  Hence  Turk,  and  Pers.  mat,  ast' confounded,  amazed,  receiving  check O.  V.  mat,  '  mated,  quelled,  subdued, M.  E.  mate,  confounded,  Ilal.  m$aH9, mad.
11219:Material;  see  Matter.
11220:Maternal.    (F.  -  L.)     F.  matm Low  L.  materttaiis.^X^  mattrmu, ing  to  a  mother.  —  L.  maler,  moKt naie  with  Molhar.
=== SKT check ===
```


## [2026-09-04T19:20:21.552Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py SKT.txt 'Mate  \\(3\\)' 2>/dev/null | head -2\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Matador,  the  slayer' in p: print('matador leaf',i,'printed',i-20)\n    if 'to  check-make,  confound' in p: print('mate2 leaf',i,'printed',i-20)\n    if \"Check,  a  sudden  stop\" in p: print('check leaf',i,'printed',i-20)\n    if 'Margot' in p or 'Magpie,  a  bini' in p: print('magpie leaf',i,'printed',i-20)\nEOF"
}
```


### [2026-09-04T19:20:23.312Z] TOOL RESULT

```
leaf(0-based)=298  match='Mate  (3)'  ctx=ock  of  a  con  hohttof match  i  hence,  the  gun  itselt Mate  (i).  a  companion  ;  see  Make. Mate  (3),  to  check-make,  confound. -•Pen.  &  Arab.)  From  the  game  of CAeck-mate  meant  'the  king  ia  dcad.'»(X etcAt<  tt  mai,  check>niate;  Cot-     [Heft is  not  wanted.]  — Pers.  sh
leaf(0-based)=640  match='mate  (3)'  ctx=iic),  saflron,  sultaa. Persian  from  Arabic,  mussulmati. Frenek  from  Flerrian  from  Arabic ; mate  (3). Turkish  from  Arabic:  coffee,  giaoar. HinJi from  Arabic ;  nabob. Italian  from  Malay  from  Arabic soon. of  ASUTIC  origin,  bat  NEITHER  ARYAN  NOR  SEMITIC h  anna,  bangle,  cowr
check leaf 98 printed 78
magpie leaf 289 printed 269
matador leaf 298 printed 278
mate2 leaf 298 printed 278
```


## [2026-09-04T19:20:23.755Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW mattus ===\"; grep -n -i 'mattus\\|matus\\|madeo\\|madere' LEW_1910.txt | head -10\necho \"=== LAT mattus ===\"; grep -n -i 'mattus\\|madeo' LAT.txt | head -10\necho \"=== WLD Bd2 mattus ===\"; grep -n -i 'mattus' incoming/WLD/WLD_Bd2_pages.txt incoming/WLD/WLD_Bd1_pages.txt WLD_band3.txt | head -10"
}
```


### [2026-09-04T19:20:23.841Z] TOOL RESULT

```
=== LEW mattus ===
=== LAT mattus ===
35615:madeo,-es,-ul,-ere: etre mouille, impregn^, imbu de (sens phy¬
35625:Cf. peut-etre aussi matus, *mattus , M. 1.5428; madulsa,-ae f.: raot
36870:mattus: v. matus.
36911:On lit aussi mattus (natus): tristis, CGL IV 114,4; 337,5; 536,31;
36914:*mattus, 5438.
36915:Mattus peut reprdsenter une prononciation vulgaire (dialectale)
=== WLD Bd2 mattus ===
incoming/WLD/WLD_Bd2_pages.txt:15134:      Lat. madeo,^ -ere ..nab sein, von Kasse triefen", mattus ,jtrunken"                             (s.   zur
```


## [2026-09-04T19:20:33.531Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT matus entry ===\"; sed -n '36900,36925p' LAT.txt\necho; echo \"=== LAT leaf ===\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'mattus: v. matus' in p: print('matus leaf',i,'printed~',i-18)\n    if 'margarita, -ae' in p: print('margarita leaf',i,'printed~',i-18)\nEOF\necho; echo \"=== WLD Bd2 ctx ===\"; sed -n '15125,15145p' incoming/WLD/WLD_Bd2_pages.txt\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'mattus ,jtrunken\"' in p or 'mattus' in p: print('WLD Bd2 leaf(1-based)',i+1,'printed',i+1-5)\nEOF"
}
```


### [2026-09-04T19:20:35.446Z] TOOL RESULT

```
=== LAT matus entry ===
Ancien (Pl.), usuel, classique. Maturus est deriv^ d'un thome en
-u-, natu- non atteste; cf. mdtuta, matutinus . II est demeure dans
les 1 . romanes, M.L.5433 (panroman), comae maturitas id.5433, maturare
5430 (panroman, sauf roumain), maturescere S430a, * naturicdre 5431,
mais seulement avec le sens de "mur".
Cf. mane, au sens de "de bonne heure".
La notion de "mur" est exprimee de maniores diverses suivant les
langues; les expressions ne concordent pas, meme quand elles appar-
tiennent a une meme racine, ainsi skr. pakvah et gr.ueroxV.
matus, -a, -um: ivre. Mot vulgaire (Petr .41), qu 1 on retrouve dans
les gloses: matum est, hunectum est, emollitum, infestum, CGL V 604,41.
On lit aussi mattus (natus): tristis, CGL IV 114,4; 337,5; 536,31;
V 465,6; .543,40. Mais peut-etre sont-ce deux mots differenta. Le
rapprochement de 1 'ital. matto est aujourd'hui conteste; cf.M.L. s.u.
*mattus, 5438.
Mattus peut reprdsenter une prononciation vulgaire (dialectale)
de *naditus', toutefois le rapprochement de nitidum, ital.netfo ne
prouve rien, si l'adj. italien est empruntd au gallo-roman net, comme
l'indique, sana preuve, M.L. s.u. nitidus, 5y3y.
Matuta, -ae f. : ancienne deesse italique, identifide avec l'Au-
rore (Lucr.5,656), puis avec Leucothea. Mdtuta est le f^minin d’un
ancien adjectif mdtu-to-s, cf. acu-tus, etc.; 1'dpithete est gend-
ralement accompagn^e de Mater, cf. CIL XI 63y4,630i.
Derive: matutinus: du matin, d'ou matutinum: le matin, M.L.5434;
celt.: iri. m aten, britt. netin', mdtutlndlis', -drius (tardifs).
Matuta ne differe que par le suffixe de maturus ; tous deux se

=== LAT leaf ===
margarita leaf 707 printed~ 689
matus leaf 713 printed~ 695

=== WLD Bd2 ctx ===
(s.              -.schwellen") erinnert werden darf. Idg. mcd- also etwa ,,schw'ellen".
        mnu {^madnnj) ..maste", maim „fett", matme „Fett" (G. Meyer
      Alb-
Alb. Wb. 259), ynaze „Rahm, Sahne, Haut auf der Milch" (Jokl SBAk.
Wien 68, I 54, ^mndni: nicht besser nach Charpentier KZ. 46, 39 als
             1


"^mazgln zu "^mozgo- ,.Mark").
      Lat. madeo,^ -ere ..nab sein, von Kasse triefen", mattus ,jtrunken"                             (s.   zur
Form Yf. LEAVb.^ s. v., Sommer Hdb.^ ^dl), wohl auch mano^ -are „flie6en,
rinnen" als             Denom.     eines   Adj. "^madsnos   (s.    u.       ^mdq-   „na6*');    iiber       lat.

ynanima          s.   u.
      Ganz
         fraglich ist ob maialis „geschnittenes mannliches Schwein" als
Abl.  von "^madia „Mast", s. Sommer IF. 1      81   Yerb. m. Maias sucht
                                                             1 ,        ;


Leumann -Us 14, 30 zu begriinden.
WLD Bd2 leaf(1-based) 236 printed 231
```


## [2026-09-04T19:20:49.237Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB checkmate/mate/matador/matte ===\"; grep -n -i 'shah mat\\|check.mate\\|matador\\|Pers. shah' WEB_vol1.txt | head -12\necho; echo \"=== FSD checkmate ===\"; grep -n -i 'shah mat\\|shah-mat\\|check.mate' FSD_vol1.txt FSD_vol3.txt FSD_vol4.txt | head -12"
}
```


### [2026-09-04T19:20:49.342Z] TOOL RESULT

```
=== WEB checkmate/mate/matador/matte ===
24731:pull/fight, n. an entertainment in which a bull is first provoked by men on horseback and afoot, who stick lances and darts into it, and is then maneuvered into position for the kill by the matador, who must run his sword skillfully Jombo its neck: popular in Spain and Spanish America.
31744:iung check’hook, n. 1. a hook horse's harness through E the saddle o is fastened. gh which the checks . a device on a hoistin, i SADE I speed, g machine for Check. check’/ing ac-count’, a ban! which the depositor can ae time, without presenting a REE SRS EY ee same as ciclaton oe check’less, a. that cannot be cher strained. be checked or re- check list, a list or catalo; fying or checking. check’mate, n. 1. a move in the chess, that checks the opponent's king ane, of scennel be put into safety, thus ending the ede position of the king resulting from
31747:check/mate, v.t.; checkmated, pt., pp.; check mating, ppr. in chess, to place in check . hence, to arrest and defeat. pa

=== FSD checkmate ===
FSD_vol1.txt:63599:porary  halt  in  the  chase  due  to  the  loss  of  the  scent  check'a-fol(ep,  1   Chek'a-bl;  2   ch&k'a-bl,  a.  Susceptible  of  be-  Check'mate",  n.  1.  Chess.  The  final  position  in  a   game by  the  hounds.  13.  That  part  of  a   substance  under  check'age,  1   tfhek'ij;  2   chSk'ag,  n.  A   checking,  as  of  an  of  chess,  in  which  theki:
```


## [2026-09-04T19:20:50.735Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHN MATADOR ===\"; grep -n -i '^MATADOR\\|MATADOR' PHN.txt DEV.txt LAM.txt | head -10\necho; echo \"=== LKT matador ===\"; grep -n -i 'matador' LKT.txt | head -10\necho; echo \"=== KLN mut/maweth ===\"; grep -n -i 'māweth\\|maweth\\|Heb\\. muth\\|mawt' KLN_1966.txt | head -10"
}
```


### [2026-09-04T19:20:50.829Z] TOOL RESULT

```
=== PHN MATADOR ===

=== LKT matador ===

=== KLN mut/maweth ===
```


## [2026-09-04T19:20:59.279Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT matar ===\"; grep -n -i 'matar\\|mattare\\|scacco matto' LKT.txt | head -10\necho; echo \"=== WEB matador ===\"; grep -n -i \"mat'a.dor\\|ma.ta.dor\\|matador, n\" WEB_vol1.txt | head -6\necho; echo \"=== WEB mate v ===\"; grep -n -i 'from Per. shah mat\\|shah mat\\|Per. shah' WEB_vol1.txt | head -6"
}
```


### [2026-09-04T19:20:59.458Z] TOOL RESULT

```
=== LKT matar ===
3204:1387.  Ar.  luamtar: 'Regenmantel'  [aus  ar.  matar  'Regen' mit  präflgieitem  m  des  Werkzeuges]; hieraus  siz.  mantarru  [aber  Avohl  kaum it.  mantazzo]  'Regenmantel  der  Bauern'. [GrSVociSic  240.
3319:'Er  ist  gestorben,  tot';  als  Fachausdruck der  Schsichspieler  säh  mät  vom  pers. sah  'König'  [Horn  NpEtS.  170,  Nr.  772]: 'Der  König  ist  tot' ;  hieraus  ist  mit  dem Schachspiele  selbst  der  Ausdruck  inter- nal ional  geworden,  vor  allem  it.  scacco matto  'schachmatt',  prov.  mat,  frz.  Schee et  mat,  sp.  jaque  y  mate,  jaqiii  mute,  pg. chaque  i  mate,  rum.  mat;  dtsch.  schach- matt, engl;  checkmate;  russ.  sahmaty 'Schachfiguren',  hulg.  suhmatna  igra 'Schachfigur',  sahmatna  (izska  'Schach- brett'. Aus  dem  Schachspiel  wurde volksctymologisch  parodierend  it.  matto 'verrückt'  genommen.  Dazu  die  Vb.  it. mattare,  frz.  mater,  prov.  kat.  sp.  pg. matar  'matlsetzen,  überwinden,  besiegen' und  schiiefälich  sp.  pg.  matar  'töten' [und  nicht  etwa  <^  lat.  mactari,  worin et  y  ch  geworden  wäre  wie  factum  > hecho],  —  [Henii  Estienne,  Traicte  de la  confnrmite  du  langage  franqais  avec  le grec,  Paris  1569,  führt  trz.  mat  auf  it. matto  und  dieses  auf  gr.  judiTaioc;  zurück!] [Kluge  302.  ML  .5401.  SPITZER  in Herrigs  Archiv  CXLI,  264.  ZDMG XX  Vi  II,  696.
7120:maierasso  1446 '  matraca  1474 j  mattaccino  1525 '  mattare  1443 j  »wa«o  1443
7307:marfus  1414 I  marietta  1417 !  inariposa  1417 j  warioi«  1380 I  maroma  1339 marquesita  1374 mnrras  1426 matafaluga  762  f ;  matdläs  1446 matar  1443 matraca  1474 matutxe  1525 I  maymon  1365 !  mesqui  1470 momia  1510 morabati  1515 moradux  1411 mosdrabe  1523 WMsc  15.5a musti  1493
8288:matar  1443
8560:matar  1443

=== WEB matador ===

=== WEB mate v ===
31671:from Per. shah, king, the principal piece in a game of chess. <
31975:cher:u-bim/ic, a. pertaining to cherubim. cher’ù-bin, a. cherubic; angelic. [Obs.] cher’u-bin, 2. occasional plural and, formerly, Singular of cherub (in senses 1, 2, 3), as in the ulgate. cherup; v.t. and v.i.; cheruped, $t., PP: cher- uping, ppr. [echoic.} to chirrup; to chirp. cher’up, 7. a chirrup; a chirp. LS chēr’vil, n. [AS. cerfille; OFr. cherfuel; ee cerafolio; L. cærafolium, cerafolium; wi chairephyllon, chervil; chairein, to ee phyllon, a leaf.] any of various umbe i IoT plants, as Myrrhis odorata, Swee G ale: Anthriscus sylvestre, COW chervil; eni cially, he) cerefolium, garden used in salads. F 2 cher-vo/nets, 7.; $l. cher-vyont’si, [Russ] iet 1. the former monetary unit of e Ps Union, equal to 10 gold rubles: Tep: March 1, 1936, by the gold ruble. 2. a gold coin of this value. Also spelled ichervone: chése, v.t. to choose. 3. ptt ‘rom Cheshire cat, a proverbial grinning cas Car- Cheshire, England: the one D end (1856) roll’s Alice's Adventures 1% Won Her a fixed that disappeared gradually un rin remained. Cee co, a [Heb] month of the Jewish year. ches/i-ble, 7. see chasuble. , Ry, Czech. ches’key, 7. [from Czech ces a 5 1. a person of Czech extra eai] : ; 2. the Czech language. [Slang |. escasi chess, n. [ME. ches, chesse; OF ©. Sst impo from Per. shah, a king, the i eal) played ve piece in the game.] a game S es to mo two persons, each having 1 6 ivi jn different ways, On 4, oases a dar squares, alternately, Sai S ayer has eight prt «hts, A A, two bishops, two eee phe gam Toks, or castles) and eight P nook not; moo% i
```


## [2026-09-04T19:21:00.712Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD checkmate ctx ===\"; sed -n '63595,63615p' FSD_vol1.txt\necho; echo \"=== FSD mate2/matador vol3 ===\"; grep -n -i \"mate.,.*chess\\|ma'ta.dor\\|matador\" FSD_vol3.txt | head -6"
}
```


### [2026-09-04T19:21:00.803Z] TOOL RESULT

```
=== FSD checkmate ctx ===
-mat  iso.]  1.  Chess.  To  put  (an  opponent  s   king)  m
—   to  take  c.,  to  he  offended.— travelers’  c.  (Banking), check  to  the  order  of  a   traveler  which,  when  endorsed  by the  latter,  serves  as  cash.— waived  storage  c.  (Railroad.), an  order  authorizing  delivery  and  rescinding  storage  charges, where  freight  has  been  stored  by  mistake.
game  thus  diverting  the  hawk.  (2)  Hunting.  A   tem-  check2,  n.  (Scot.]  The  wheatear  or  chack.  ling  checked.
a   check  from  which  no  escape  is  possible,  thus  winning the  game.  See  the  noun.  2.  Hence,  to  discomfit  or defeat  (a  person,  plan,  etc.),  as  by  a   skilful  maneuver; as,  the  diplomatist  was  checkmated  by  the  council.
porary  halt  in  the  chase  due  to  the  loss  of  the  scent  check'a-fol(ep,  1   Chek'a-bl;  2   ch&k'a-bl,  a.  Susceptible  of  be-  Check'mate",  n.  1.  Chess.  The  final  position  in  a   game by  the  hounds.  13.  That  part  of  a   substance  under  check'age,  1   tfhek'ij;  2   chSk'ag,  n.  A   checking,  as  of  an  of  chess,  in  which  theki:  
test  which  is  allowed  to  remain  untreated  for  com-  account  or  the  like,_or  an  entry  that  is  checked, parison  with  the  portion  which  has  been  subjected  check'blrd",  1   dhek'burd';  2   chEk'blxd',  n.  [Brit.  Guiana.I to  the  test.  14.  In  mining,  a   slight  fault.  15.  A   chaek ;   wheatear.  ,   ,
consonant  produced  by  sudden  stopping  of  the  breath;  check  er,  1   tfhek  er;  2   chSk  er,  vt.  1*  To  mark,  deco- a   mute.  1C.  [Local,  U.  S.]aAn  impromptu  meal  of  rate,  or  an-ange  with  squares  or  crossed  lines;  streak.  2.
  king  of  the  losing  player  is  placed
m   check  and  can  not  be  extricated:  commonly  shortened to  mate.  2.  Figuratively,  complete  discomfiture;  final defeat.  [<  F.  ichec  et  mat ,   <   Ar.  shdh*mat,  <   shah  (< Per.  shah),  king,  -f  mat,  Is  dead.j  —   to  give  checkmate or  a   c.  to,  to  effect  defeat  by  checkmating  an  opponent.
cold  provisions.  17 +-’ The  stub  to  which  a   bank-draft  is  To  ml  with  variations  or  vicissitudes;  diversify,  cbeq'uer*.  chcck'mate'%  inter)  An  exclamation  declaring  checkmate.
K   ,   i   1   -.o  h   i   „   ___  _   rhPPk'Prt  -n  1.  Ilnp  nf  fhp  rnpnps  ncprt  in  nf  ChPCk'RronP'M.  1   Chplr'atfin*-  9   oRSlr'ctKn'  n   Bnmn.
sive move;  attack.  19f.  An  insult;  affront.  20  f.  [Eng.] A   fine  to  which  servants  of  a   royal  household  were  sub- ject as  a   penalty  for  neglect  of  duty.  21 1-  Kebuke; reproof.  [   <   F.  echec,  OF.  eschec ,   <   Per.  shah,  king. Tn  sense  8   <   checker1,  n.]  chekt.
Synj  see  animadversion;  cessation*.
—   cashier’s  check  (Banking),  a   check  upon  its  own funds  by  a   bank’s  cashier.—  certified  c.,  see  certify. — check' *band",  n.  Textile.  A   contrivance  used  to  check the  speed  of  a   spindle-carriage  as  it  moves  backward  and forward.— c.sbar,  n.  Harness.  A   metal  rod  having  loops at  either  end  for  holding  a   bridle  chcck-reln  and  one  in the  middle  for  fastening  to  the  check-hook.—  c. -battery, n.  Mining.  A   wooden  contrivance  for  checking  the  out- let ot  a   chute  or  for  closing  an  intake  for  air.—  c.« book,  n.  1.  A   book  of  bank-checks  in  blank,  usually with  marginal  stubs  for  date,  amount,  and  name  of  payee, chequeebookt.  2.  A   book  used  for  checking  or  verifying any  matter,  as  the  record  of  customer’s  checks  kept  In  a bank.—  embrace,  n.  Any  one  of  four  leather  thongs  which check  the  endwise  motion  of  a   chaise  or  phaeton.—  c.» bridge,  n.  Same  as  fire-bridge.—  c.*chaln,  n.  A   chain Irom  the  side  sills  of  a   railroad-car  to  the  side  of  the  truck, to  prevent  the  latter  from  swinging  crosswise  on  the  track if  derailed.—  c.*chamber,  n.  Mech.  The  chamber  or  cav- ity which  contains  the  gate  of  a   check-valve.— c.»clcrk, n.  A   clerk  who  keeps  and  checks  the  time  of  employees, etc.—  c.  *cord,  n.  1.  A   cord  fastened  to  the  collar  of  a   dog, and  held  by  one  who  Is  training  him.  2.  A   check-string. —   c.*damper,  n.  A   contrivance  which  allows  cold  air  to enter  a   door  or  an  opening  at  the  bottom  of  a   chimney  so as  to  prevent  a   direct  draft,  thus  reducing  the  rate  of  com- bustion of  fuel.—  c.rcnd,  n.  The  end  (left)  of  a   bank- check,  engraved  with  special  words  or  devices  to  prevent counterfeiting.— c.sexchangc,  n.  [Colloq.]  Finance.  Sight exchange.—  c.*fiooding»  n.  Irrigation.  A   system  of  dams or  dikes  retaining  water  on  irrigated  fields.—  c.*follo,  n. See  sizes  of  paper,  under  paper.—  c. -gate,  n.  Irriga- tion. A   gate  In  a   low  embankment  or  dam  which  is  built across  fletds  to  hold  back  the  waters  of  irrigation.— c.* grieve,  n.  Mining.  [Scot.]  An  overseer  or  steward who  checks,  for  the  owner,  the  weighing  of  coal  taken from  a   mine.—  c.  shook,  n.  1.  A   check-rein  hook  on  a harness-saddle.  2.  Part  of  a   safety  device  In  a   mine  hoist- ing-apparatus, consisting  of  books  on  the  rim  of  the  rope- drum,  which,  when  the  speed  becomes  excessive,  fly  out and  engage  stop-pins.— c.*kcy,  n.  [Eng.]  A   latch-key.— c.dlnc,  n.  A   check-rein.—  c.’llst,  n.  1.  A   list  by  which something  may  be  checked  or  verified;  specifically,  a   roll  or list  of  voters  used  at  polling-places  on  election-days  for checking  off  the  names  of  those  who  vote,  as  a   guard  against repeating.  2.  A   list  of  genera,  species,  etc.,  usually  limited to  one  natural  dirision,  for  students  and  collectors,  to  check when  recognized  or  acquired c.dock,  n.  A   lock  for  cov- ering the  keyhole  or  for  preventing  a   door-bolt’s  being moved.— c.*loop,  n.  A   metallic  open  loop  for  receiving an  overdrawn  check-rein  where  it  passes  over  the  horse’s head.— c.*nut,  n.  A   nut  for  preventing  the  turning  of another  one;  a   Jam-nut,  lock-nut,  or  plnching-nut.—  c.?out, n.  A   place  in  a   coal-mine  where  the  floor  and  roof  meet and  end  the  seam.—  c.*rall,  n.  1.  A   device  for  permitting railway-trains  to  run  along  a   main  line  or  move  to  a   siding as  desired.  2.  An  auxiliary  rail  placed  just  inside  of  the inner  rail  of  a   railroad  curve  to  relieve  the  outer  rail  of undue  pressure.— c.*re!n,  n.  1.  A   lo.oped  rein  passing from  the  bits  to  a   hook  in  the  Baddle  to  keep  the  horse’s head  up.  2.  The  branch  rein  connecting  a   driving-rein of  one  horse  to  the  bit  of  his  mate  in  a   double  team.— c.*ring,  n.  A   ring  by  which  a   check-brace  is  attached  to a   carriage.—  c.*ro  11,  n.  1.  (1)  Any  check-list.  (2)  Same as  muster-roll.  2.  See  checker-roll.  3.  A   list  of household  servants,  especially  when  numerous.— c.  *row, n.  One  of  the  standing  rows,  as  of  trees,  in  an  orchard  or farm  that  partitions  it  into  squares.—  c.  *rower,  n.  1.  A corn-planter.  2.  An  attachment  to  a   com  planter  by which  It  drops  the  seeds  at  regular  distances  so  as  to  pro- duce check-rows.—  c.«stop,  n.  A   rubber  safety-drum  on a   deep-sea  dredge.—  c.  -stopper,  n.  Naut.  A   light  rope used  to  check  the  run  of  the  cable  or  of  a   rope  In  paying  out. —   c.*strap,  n.  1.  A   strap  connecting  the  collar  and  the belly-band  of  a   harness.  2.  A   strap  coupling  the  hit  of the  off  horse  to  the  gears  of  the  near  one  to  hold  back  the former  when  harnessed  In  the  Western  single-line  method; a   hold-back  strap.  choke»strapt.  3.  A   cord  or  strap by  which  the  occupant  of  a   closed  carriage,  omnibus,  or  car
draughts,  usu- ally a   small disk.  2.  One  of the  squares  or spots  in  a   check- er»  or  chess- board or  other checked  sur- face; a   square  in a   mosaic  or  ar- chitectural de- sign. 3.  pi. The  game  of draughts:  the more  familiar name  in  the United  States. It  Is  played  with 24  pieces,  12  on each  side,  ar- ranged  and moved  upon  a board  divided
chuck1,  n.,  4.
check'stone2,  n.  [Local,  Eng.J  Same  a3  stonechat. checkt,  pp.  Checked.  S   S
check 'work",  1   Chek'wurk*;  2   chek'wurk',  n.  1.  Same  as checkerwork.  2.  Mech.  An  escapement, chcck'y,  1   Chek'i;  2   chfck'y,  a.  Her.  Checked  or  check- ered: said  of  a   field  or  charge.  [   <   OF.  eschecgui,  pp.  of eschecQuer;  see  check1,  v .]
Ched'dar,  l   dhed'ar;  2   chgd'ar,  n.  A   village  in  Somerset - shire,  England,  noted  for  Its  cheese  and  immense  stalactite caverns.
che'der,  1   Hg'der;  2   He'der,  n.  [che'dor-im  or  che'dar-im, 1   -im;  2   “Im,  pi.)  [Heb.]  A   Jewish  elementary  school  where children  are  taught  Hebrew  and  religion. Ched"or-1a-o'mer,  1   ked'er-h-5'mer;  2   cgd'Cr-la-S'mar.  n. Bib.  Gen.  xiv,  1.
Che-dreux',  l   5h5~dru';  2   che-dru',  n.  A   type  of  wig  or peruke  worn  in  the  17th  century,  named  for  Its  maker. Che-du'ba,  1   dhi-dQ'ba;  2   che-du'ba,  n.  An  Island  in  the Bay  of  Bengal,  British  India;  240  sq.  m. chee'cha,  1   Chl'dha;  2   ch5'cha,  n.  [Ceylon.]  A   small  familiar _   gecko-lizard  (Hemidactplus  frenatus) .   easily  tamed.

=== FSD mate2/matador vol3 ===
15828:Tho matador Is s sroAt artist Htrong i
15831:matador DiaKAai .1 Cimicirini Plomtno v 40 |
15849:Matador
15977:ting of rushes or straw 13. Card»playmg A matador a weigh! at the hot torn. It presses out the
16242:mate*, n. in chess, a oheckmate — forced mate, a combina-
17073:matts, n Same as matador, 2.
```


## [2026-09-04T19:21:08.185Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB checkmate ety ===\"; sed -n '31744,31750p' WEB_vol1.txt | cut -c1-2500\necho \"=== WEB search 'is dead' ===\"; grep -n 'mat, he is dead\\|he is dead\\|is dead' WEB_vol1.txt | head -8"
}
```


### [2026-09-04T19:21:08.273Z] TOOL RESULT

```
=== WEB checkmate ety ===
iung check’hook, n. 1. a hook horse's harness through E the saddle o is fastened. gh which the checks . a device on a hoistin, i SADE I speed, g machine for Check. check’/ing ac-count’, a ban! which the depositor can ae time, without presenting a REE SRS EY ee same as ciclaton oe check’less, a. that cannot be cher strained. be checked or re- check list, a list or catalo; fying or checking. check’mate, n. 1. a move in the chess, that checks the opponent's king ane, of scennel be put into safety, thus ending the ede position of the king resulting from
3. figuratively, defeat; overthrow
check’māte, interj. in chess, a call o indi E checkmate. BUEN
check/mate, v.t.; checkmated, pt., pp.; check mating, ppr. in chess, to place in check . hence, to arrest and defeat. pa
check nut, in mechanics, a nut which screws down upon the primary nut to secure it: called also lock nut.
check’/off, n. an arrangement by which dues, assessments, etc. of trade-union members are withheld from wages and turned over to the union by the employer.
check’rein, n. 1. a strap looped around the checkhook to prevent a horse from lowering his head: also called bearing rein.
=== WEB search 'is dead' ===
47694:Cūr-tā’nå, n. the blunt sword di ~ Keble s ispla fore English monarchs at their splayed be- symbolizing mercy: also called the tin ion, gates the Co OT ord of cur'tate, a. [L. curtatus, A shorten’ ] reduced; shortened. ol oer: to curtate gaui, see cycloid. curtate distance; in astronomy, the dj from the earth or sun to that point ese aaa from the planet meets the Dlane e ecliptic. cūr-tã’tion, n. [L. curtatus, pp. of cur shorten.] the interval between a planeta ee from the sun and the curtate dis- ance. clir’té-sy, ».; pl. clir’té-sies, [var. of z : ae = i À ate Cour- A in law, the right that a husband has in the lands of his dead wife, when they have had children capable of inheriting, ctr’tilage, n. [OFr. cortillage, from courtil, a court; L. cohors, a yard.] in law, a yard, gar- den, enaa or field, near and belonging to a dwelling. ctir’tle ax, a cutlass. [Archaic.] ctrt/ly, adv. briefly; in a curt manner, curt ness, z. shortness; the quality of being urt. ctirt/sy, 7.; pl. ctirt/sies, [var. of courtesy] a salutation made by bending the knees and dipping the body slightly, as a mark of re- spect or a step in dancing: now only of women and girls: also spelled curtsey. cirt’sy, v.i.; curtsied, pt., pp.; curtsving, ppr. to make a curtsy: also spelled curtsey. cu’/ru-ba, x. [from native name] the sweet calabash of the West Indies; the fruit of Pas- siflora multiformis. ` cu-ru-cu’cu, n. see bushmaster. cù’rù- cui (-kwi), n. [native Brazilian name.] 4 Brazilian bird, the trogon. _ s ci/rule, a. [L. curulis, pertaining to a chariot, from currus, a chariot, car; currere, torun.] priv- ileged to sit in a curule chair; as, a curule mag- istrate. Pe 3 curule chair; in ancient Rome, a chair or stool without a back, so made as to be folded up and opened in the manner of a campstool, but with heavy curved legs and upholstered seat: used by dictators: consuls, pretors, censors, an ediles. 5 cu-ru/ro, 7.; pl. cu-ru’rés, [native name.] a burrowing rodent of Chile, genus Spalacopus. cūr-vā’ceous, a. [from curve, and -aceous.] having a full, shapely figure: said of a woman. [Colloqg.] cir’val, a. same as curvant. d cūr’vănt, a. in heraldry, bowed or curved. of ciir/yate, ciir’va-ted, a. [L. curvatus, pP: g curvare, to bend.] curved; bent in a re: form. £ ; cir-va’tion, n. the act of bending or cutee ciir’va-tive, a. i boran: i Signy curved, the margins of leaves. [Rare. 3 ciir’va-tire, 7. i curvalura, a bending, from curvare, to bend. E $ 1. the flexure or bending of a line from & rectilinear direction; a curve. Se 2. in geometry, the rate of deviation of 8 curve or Gave surface Eom a straig or plane surface tangent to it. | : 3P the act of curving; the state of being bent. 5 4 ai b- curvature of ihe spine; in megane an ee normal curving of the spinal column, angular or lateral. cūürve, a. [L. curvus, bent, cro d: curved, bent.] bending; crookec i oircle; as, a regular form and forming part o. a curve line. clrve, n. [L. curvum, from c
67390:2. a word or phrase so substituted; as, “she is at rest” is a euphemism for ‘she is dead.”
71100:& With full force his deadly bow he bent, And feathered fates among the mules and
```


## [2026-09-04T19:21:09.870Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD vol3 matador ctx ===\"; sed -n '15845,15860p' FSD_vol3.txt\necho \"=== FSD vol3 mate2 ===\"; sed -n '16240,16250p' FSD_vol3.txt\necho \"=== FSD vol3 mat entry ===\"; sed -n '15975,15985p' FSD_vol3.txt"
}
```


### [2026-09-04T19:21:10.007Z] TOOL RESULT

```
=== FSD vol3 matador ctx ===
spots JSp , mater (< 1, martn) kill j
ma*tie*(»t'cp>By, n. 8 ame as matboi,ociy
mat*a-rtan'da, 1 mat's-fun'dit. 2 ni&t'a-fOn'da. a. An en*
warfan* used for throwing stones by means
Matador
seemliiglv' < 8p malar (see matados) +
fund:
P0U9 (pod-),
Mmunes. asaremedy for dlsuise I v Or maatigosU, a flog- salmon (OnMrAyncAus mason) of the N Asiatic coast rivers
mu’f^p.i., 1 mw-twiMpUr: 2 m««-tl-»owip 8 r. n Any “lu A "blin'SLtartili InTSCiL*"’*”"''""""
plant whose distribution la elTocted by propagating cells In ma*su'lah, n 8 ame as iiAHmuTi? »■«■. »-iuii u«, i i
Volvo?* T<*C?r**»^rtx“^lD* ^^seoRK^l lla*su*ll-pa-Um', 1 ma-sQm-pa-tam'. 2 ma-eull-por-tilm'. glue of mwllevali
1 Siir " mASn anl - a .. .. ^ Seaport town, caplut of Klstna district, Madras of a sling [Id. .
. *** A, dtswd 2*k*su'ren-land,n Hame as Mazuhenlanu I. /uadu. mIIiib 1 niat'a-l __
tiammofiSSsSali 1 miM.lfl'ri-nm; 2 moHiO'rl-uni. n. Chem A Ma*£».gal'pa, 1 mfl'to-garpo. 2 mfl-tll-ftftFptt, » I. A do.
mSSfliSl YSlS’iTfmtenngfn mc^llc^i™.em jll«»vered In 1925 by ICormp. wnmont in cnirnl Nlcawgun. IVnlml Amorto. S. lu
=== FSD vol3 mate2 ===
duty, usually an extra oeoond mate who aaolsto tho captain
In navigation — mate'leas, a
mate*, n. in chess, a oheckmate — forced mate, a combina-
tion of moves by which checkmate Is forced - self' ■male",
n A problem-poalUoD In whloh one side compels the other
to force a mate In a stipulated number of moves sulvm.t.
— amothered m., a oheokmato given when the king can not
move, or Is smothered by his own pieces,
nui'ld, lma'i6 or mat'i, 2m&'tc or m&t'e.n. 1. An infusion
of the prepared leaves of a Brasihau holly {Ilex para-
guayanaia), much used as a beverage by tne Routh-
=== FSD vol3 mat entry ===
layer of color matted evenly over the gloss 3. [I*rov inat'a»pl, 1 mat's-pi, 2 inAi'a-pl, n |M Am ] A pliable
Kngl A mattock 10. Hume as mattoik lit. Mn-- basket so formc-d that, when flilwl with graiwl manioc and
ting of rushes or straw 13. Card»playmg A matador a weigh! at the hot torn. It presses out the
( < A.s meatto, < L matta, mat ^ - abdominal mat, a
padded apparatus adupuvl for aiding gymnastic exercise of * *•
the muscles f the abdomen -charing -mat*, n Hame os 1 ymiftJLrA' n a .i
MAT, 3 Chinese mat. a package In which cassia-bark of ■*Sictorh»g t^«woVhi?u\^ol^^ Bpahi ^
Inferior quality Is marketed -rorif mat {Naut}, a fend- V 1 iiiRt'^ fl a
er filled with cork waste mat'-biMit*, n A large flat- n ■ ' “ ’ " --*• ^ borough
bout ronslHtlng of a platform siiptsiried on scows, used for j 3 HtM.OMuZ
poisonous julcoH Hen Ulus iindnr manpk
```


## [2026-09-04T19:21:23.297Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON ماتادور ===\"; grep -n 'ماتادور\\|ماتادر' MON_part2.txt MON_part1.txt | head -5\necho \"=== MON مات ===\"; grep -n 'مات:' MON_part2.txt MON_part1.txt | head -8\necho \"=== MON کیش مات / شاه مات ===\"; grep -n 'شاه‌مات\\|شاه مات\\|کیش مات\\|کیش‌مات' MON_part1.txt MON_part2.txt | head -8\necho \"=== MON موت ===\"; grep -n 'موت:' MON_part2.txt | head -5\necho \"=== MON میت ===\"; grep -n 'میت:\\|میّت' MON_part2.txt | head -5"
}
```


### [2026-09-04T19:21:23.438Z] TOOL RESULT

```
=== MON ماتادور ===
=== MON مات ===
MON_part1.txt:3834:افتومات: 20-80 [خودکار] () (مکن.) 
MON_part1.txt:24556:بکسمات: ۸۲۰۵78۱« (- بقسمات | (.) 
MON_part1.txt:39560:المات: . برج میزان. عدل» عدالت. 
MON_part1.txt:43848:کلمات: (معا.) آن است که ترکیب کلمات 
MON_part1.txt:50672:معشوق. جشسمه 6 طلمات: جایی که در آن 
MON_part1.txt:54545:زیست» مق. ممات. حیات و ممات: زندگانی 
MON_part1.txt:59945:باشد. مثلاً در کلمات: مایل» شامل» حاصل؛ 
MON_part1.txt:64333:دییلمات: 0۱ (ص مر . آمر .) آنکه از 
=== MON کیش مات / شاه مات ===
MON_part2.txt:28911:حریف» شاه مات می‌شود و بازی را می‌بازد. 
=== MON موت ===
1339:غرموت: اقه:[- - غرمود - قرموت» غذا 
12420:فرموت: ۷۵۷ ا[تر .] (.) مخلو طی از گاه 
34201:کمثری؛ انجاص» ارموت: ارموت. امرو؛ 
43120:ماموت: ۲۲ (.) (زم. جان.) گونه‌ای 
67676:موت: (۵۷۱)۵۵۷۱ [ع.] ).( مرگك. موت 
=== MON میت ===
1782:غسل میت: غسلی که مرده را دهند پیش از 
1783:دفن. سل مس میت: سلی که به سبب 
4955:(التفهیم ۴۹۸). فتح میت: (پز.) کالبدگشایی 
12000:بر این تعریف ایراداتی است. قرار مجرمیت: 
49513:محر میت: ۷۷۱ -1۲:1111 :112 [ع.| (حامص.)
```


## [2026-09-04T19:21:27.563Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON موت entry ===\"; sed -n '67674,67690p' MON_part2.txt\necho; echo \"=== MON shah mat ctx ===\"; sed -n '28900,28915p' MON_part2.txt\necho; echo \"=== MON mat headword (م ا ت) ===\"; grep -n '^مات ' MON_part2.txt | head -5; grep -n 'مات\\b' MON_part2.txt | sed -n '1,6p'"
}
```


### [2026-09-04T19:21:27.691Z] TOOL RESULT

```
=== MON موت entry ===
که موها را آرايش کند. خدمتکار زن. (.) 
شریطه‌ای که به وسیلةٌ آن موها را بندند. 
موت: (۵۷۱)۵۵۷۱ [ع.] ).( مرگك. موت 
ابیض: (تص.) خالی داشتن شکم ۱ 
روشن کننده باطن و منور دل و سفید کنندة 
صورت قلب است. در این هنگام هوش او 
زنده گردد یعنی از خواتب غفلت دار شود 
(فرع. سج.) موت احمر: (تص.) مخالفت با 
نفس. موت اخترامی: (بز. قد.) خاموش 
شدن حرارت غربزی است واسطة عوارض 
و انات نسه به اسباب ضروری. 
(کشاف اصطلاحات ص ۸۱۳۱۲ ۱۳۱۷) 
فرع. سج.) موت اختیاری: (تص.) مفلوب 
کردن هوای نفس و اعراض از لذت‌ها است 
و آن سب معرفت است که به خصوص 
نشاه اتسائیت می‌باشد و انسان در راه تیل به 
مطلوب قطع امیال کند (فرع. سج.) موت 

=== MON shah mat ctx ===
کیش: 5 (صت.) کلمه‌ای که برای راندن 
مرغ استعمال کنند. 

کیش: 5[* (.) (جاد.) جانوری که از پوستش 
پوستین سازند (برهان). ضح.- با مراجعه به 
ماخذی که در دست بود هویت حیوان 
مذ‌کور شناخته نشد. 

کسیش‌مات: :۷152 (امر.) (شطرنج) 
هنگامی است که مهرةٌ شاه به طریقی کیش 
شود که قادر به هیچ نوع حرکتی نباشد. 
حریف» شاه مات می‌شود و بازی را می‌بازد. 

کین (قد. :18 [- کیخ] (.) چ رکث 
گوشه‌های چشم؛ رمص. 


=== MON mat headword (م ا ت) ===
9716:مات )مدش کذار ند 
26363:مات کمرمت بر گس کر تورهاه 
27196:مات ان تشعیل شو د. 
40336:مات کته شتیر 4 نماد آن ویر تلو 
43896:مات ها ف وس اه ات ای ۲۸ 
989:مفقود با ضایع شده) ناوان) ج. غرامات. 
2450:منظور اصلی از جدول مذکور ذکر کلمات و 
2451:جملات صحیح است نه کلمات و جملات 
2718:(غم. بل . غمامات. 
2765:محزون. ماتم‌زده» مصیست رسیده. 
4292:است و معمولا آن را در فواصل بین کلمات
```


## [2026-09-04T19:21:36.349Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v4 مات ===\"; grep -n 'مات ' incoming/BQT/BQT_v4_pages.txt | head -20\necho \"=== BQT v3/v4 کیش مات ===\"; grep -n 'کیش‌مات\\|کیش مات\\|شاه مات\\|شاهمات' incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt | head -10"
}
```


### [2026-09-04T19:21:36.431Z] TOOL RESULT

```
=== BQT v4 مات ===
30:کلیه حقوق‌تجد ید طبع کتاب برهان قاطع باتصمیمات وحواشی و
33:ید ینوسیله ازز<مات شماد رانجام این‌خد مت مهم فرهنگی قد رد انی
34:میکند وموفقیت آن| ستا د م<تر مرا د را ینکونه خد مات خواستا را ست *
64:ونقشه است (صرقنظر ازجدولها و کلیشه‌هایی که برای‌کلمات پپلوک وعبری
230:آموزان متوسطه و دانشکده‌ها و کانی که درین حدود معلومات دارند .
1134:هت مامات اسب و باپا خر تو مشواتر چو خوانمت استن . سنائی غزنوی .
1377:آن پنج عنصر را چون زره برتن راست کرد وبنبرد پادشاه ظلمات - که او نیز پنج عنصر تاريك را
1386:را قرمان داد که ارکان دولت غلمات را بکشند و پوست برکنند و مادر حیات از پوست آنان
1387:آسمان را باخت و جد ایغانر! برزمین تاریکی در سر‌زمین ظلمات افکند وا زگوشت آنها خاك
1390:را بفرزندان ظلمات نشان داده درآنها هوسهای شهوانی برمی‌انگیزد . باین تدبیر فسمتی از نوری
1850:مربا مات ۴ . تحتانی و فوقانی » خانهٌ کرپلی را کوبند پستی
2261:میگفته اند ( ولی ان نام درمتابع موجود » دیده نمیشود ) و کلمات سامی مذ کور ترجمةٌآست.
2364:کلمات زایده هم هست که از برای حسن کلام | الوان مختلفه درو ظاهر میگردد یمنی هر سامت
2529:ارمنی 3870 ( انان ) , بلوچی 13387 «اسشق۹۷۲ لغة این کلمات بمعنی‌در گذشتن وفناپذبرند
2900:« مرغزار» نوعی‌بازی کلمات ( جنای ) را ایجاد میکند. امامی هروی » شاعر قرن۷عچری کوید:
4091:۴۳ اما کلمات دیکری که از ريشة همین کلمه است مکرر در خودگانها آمده است » از آن
4239:مقامات در صو آن -کنایه از هعت | تخم کرفی کوعی‌است وآن سیاء وطولانی میباشد
4451:8 , 2888 ( فقط در غرح کلمات اوستایی ) » بلوچی 2862810 ۰ 181ق338 ۰
4454:«هوبشمان ۹۸۹ . دراوراق مالوی ( پارتی ) 1388 ( مگس ) « هنینگه؛ فهرست کلمات پارسی
4862:در آخر کلمات آید لك ۹ هون اردد
=== BQT v3/v4 کیش مات ===
```


## [2026-09-04T19:21:44.657Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor p in pages[:60]:\n    m=re.match(r'\\[pdf page (\\d+)\\]',p)\n    if not m: continue\n    n=int(m.group(1))\n    head=' '.join(p.split('\\n')[1:3])[:90]\n    print(n, n+1917, head)\nEOF"
}
```


### [2026-09-04T19:21:46.811Z] TOOL RESULT

```
1 1918 
2 1919 ه و سم
3 1920 اداره کل نکا زشن" ساره ۰۱/۹/) ‎٩۰9‏ ی
4 1921 ديباچة مجلد چهادم 5 پس‌ازانتشار برهان‌قاطم ازطرف شر کت معدود
5 1922 سچهارد وبنابرین دورءٌ حاضر جمماً شامل بالخ بر۲۷۵۸صفحه و۱۵٩‏ تصویر
6 1923 سین 
7 1924 شش از بعض دیوانهای گویندگان مشهور) .
8 1925 هت که لازم مینمود - در جدولهای پایان مجلد حاضر افزوده‌ايم .
9 1926 سهعت- 
10 1927 ی 
11 1928 سور دوم کسانی که مطالبی ازمقدمه‌ها وحواشی وتعلیقات مجلدات برهان
12 1929 ۰ ماغذ های اضافی
13 1930 <دوازده < 
14 1931 گقتار یست وچهارم از کناب بردان قاطع درحرف میم با حروف تجی مبتنی
15 1932 مایون ۱۹۳۲۳ و زهر عقرب و مارکند و آنرا بعربی جدوار ‎٩‏ ماج - بسکون جیم . بمعنی ماه باشد
16 1933 -۹۳۳- ماد وکسر رای بی لقطه و تحتانی بواو رسیده وبئون | کویند اسب وراقی است وآنرا عرب پرذون
17 1934 مادر آب وآش -۱۹۳ مادر آب و آتش - بکسر راق ‏ | خوانند . خوردن‌آن قوت باه دهد .
18 1935 -۱۹۳۰- مارامیند وبیمار ومرٍض ومعلول را نی ز کونندچه‌یمارستان مار آپ ‎٩‏ - بروزن فاراب , بد
19 1936 ماراسپندان ۱ ۱۹۳۹۳ نشتن ‎٩‏ - ول ملکی باشد (۱) که موکل‌است ماراقسان ۷ - باهمزءبروزن‌آتشدان
20 1937 -۱۹۳۷- مارشکم سوراخ هلیون کوبند (۱). دفع‌سموم جانوران کز ندمومار مار دو ز بان «کنایه ازمرد
21 1938 مار شحاکی -۱۹۳۸- هفت بند است که استادان تابی فوازند . وآنرا از قفای سراو برمیآورند » وآن س
22 1939 -۱۹۳۹- : ماژوستان ماده - بر وزن چاره » بممنی حاب | که از چوب بردیوار وغیرآن اقتد ۷ - ومخقف
23 1940 مازربون : ۳-۱۹۸۰ و پازند بمعنی دوری از بدرها وپاکیز کیا زکناه ال - بکر ثاك و سکون لام » نا
24 1941 -۱۹۸۱- 1 ماست مرکب همست ۱ - و بمعنی‌مازن هم‌آمده‌است نسخه بحذف دال‌آخر نوشته شده بود که ما
25 1942 ماسوچه -۱۹۸۲- باشد وآن صمقی است که خایند ‎٩‏ . ماسیدن * - با سبن بی نقطه بر وزن
26 1943 -۱۹/۳- ماغه ماشر !۱ < بارای بی‌نقطه پروزن‌ناسزاء | میاغوب هم هست پٍمنیآزرده مشو و شور وغوق
27 1944 ماش‌هندی ۱۹۸4 وآن افزاری است زرگران‌مگران وآهنگران | وکر نون و تحتانی بواوکشیده و بنون زده
28 1945 -۱۹۶۵- ما کول ماکان - بر وزن پاکان . نام یکی از | بمعنی پس فردا باشد که برادر كوچك فردا
29 1946 ماکیان : ۹ ۱۹۶۹۳ ماگیان ۱ - بر وزن مادیان . مزغ | لام حلوائی است که ازبرنج پزند وآن درکیلا
30 1947 ۱۹۵۷ مالخولا کلوبندء را (۱) گوبند و آن غلامی باشد که | مالش ومالندگی‌هم هت ‎٩‏ -
31 1948 مالیطرنا م۱۹۶۸ کوبند بوتانی ات .38 خوانند, وصعترا کرچه باسین بی‌نقطه است لیکن
32 1949 -۱۹4۹- مانا مامیرآن ۱ - با رای بی نقطه پروزن ِ که عربان بیت خوانند ۴ - واسباب وضروریات
33 1950 ماعلق -۹- و یازه(۱) طم خدای عزوجل است ۱ - وبمعتی | چیزی شدن باشد بعنی شبه ومانند ونظیرشدن 
34 1951 ۱۹۱۱۳ مانه 
35 1952 مالی -۱۹۱۲- مافی « بروزن دانی بممتی نادر باشد | و جد از عیسی علیه السلام ظاهر شد و دعوای
36 1953 -۱۹۳- مالی 
37 1954 مایدن -۱۹۵8۶- (پدر عظمت ومادر زندگان و ادان نختین » تثلیث اول .را تعکیل دهند ). پس انان‌خت
38 1955 -۱۹۵۵۰- مانستار .و نهاد و رهاکرد . و چون کسیرا کاری که باید ۲ اوست ۲
39 1956 ماور -۱۹۵۹- و نای قرشت بروزن آمیزکار»‌ش ی کل راگوبند است که يك حسه ازدوازده حسةٌ سال‌باشد 
40 1957 -۱۹۵۷- مامیار پهلوی شهر ومملکت راکویند که عربان مدینه | ازکشته شدن آبرج معلوم کردید که حام
41 1958 هاه بر کوهان -۱۹۱۸- و خوش صورت باشد .3*۴ از طلا و نقره و برنج و مانندآ ن که زنان برس
42 1959 -۱۹۵۹- ماهو کویند وآن حساب نگاه داشتن سال وماه وروز | که ماه سیام باشد؟ وکش شپرست مشهوربشه
43 1960 ماهوار -۱۹۹۰- و زیشت باشد ‎٩‏ - و نام حاکم سیستان هم بوده | معشوق میگوبند .
44 1961 -۱۹۹۱- ماهیان ولیم اس ت که نود وشش حبه باشد ۱ .48 آورند وماهیابه را ازآن سازند و معنی ترکی
45 1962 ماهیانه ۱۹۹۲۳ ماهیانه ۱ < بر وزن رازبانه ۰ آنچه خوانند .
46 1963 ۱۹۹۳۳- مالدماار ماهی‌شور ۱ (۱) - با شین قطمدار مای - بروزن بای . مخقف میای باشد
47 1964 ماکده نه ۱۹۹۸۳- ماه نه - بکر نون وظهورها » | دستگاه و نامان هم هست - و ابنیاد هر چیز را
48 1965 بیان دویم در میم با بای ابجد معتمل بر پنج لغت و کذایت
49 1966 متری ۱۹۹۹۳ مترس - بفتح اول و ثانی و سکون را متولی‌چیره ز بان - کنابه از
50 1967 بیان چهارم در میم با ای مثلثه ۷؟ مشتمل برهشت لغت و کنایت
51 1968 مجاجنگه -۱۹۹۸- راوی شمر .رود کی شاعی هم بوده ۷ - و ماه را وکنلبه از سروزکابنات سلوات‌اطٌ ع
52 1969 -۱۹۹۹- میاهنکه مجسطی ۱ - بکر اول وفتح نانی, هجهر؟ آ آش - ممررف است که
53 1970 مچ رکه ۱۹۷۰ هچرگ ۱ - بفتح اول و(۱) نانی بر مچه ۴ - بنم اول و فتح نالی مشدد ,
54 1971 ۱۹۷۱۳ محلب اباشد ۱ و با تای فرشت هم بنظر آمده.است که بر وژن
55 1972 محمودء -۱۹۳۲- محموده ۱ - بر وزن فرموده . نام | کزندکی عقرب را نافع باشد .
56 1973 ۱۹۳۳ مخلج مختاد حق » بکر رای قرشت . مخسنوس ۴ - بنم اول رکسر سین
57 1974 مخلف -۱۹۷۸- مخلف - ینم اولبروزن مشرف؛ کبوتر | که بر پیراهن و جامه افتد خصوصاً همچوکيك
58 1975 ۱۹۷۰ مداین خلاشند تا اسب تند شود ۱ . دام دارویی است که بفارسی سپستان کویند .
59 1976 مدبران فلك ۱۹۷۹۳ بود آبادان در زمان انوشیروان در حوالی بابل | قرشت‌بروزنلبلبوشکن, بلفت‌زدد
60 1977 ۱۹۷۷ مدین درست است ۱ . دهعت باشد ۴ .
```


## [2026-09-04T19:21:55.858Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 15 16; do echo \"===== pdf $n (printed $((n+1917))) =====\"; awk -v k=$n 'BEGIN{RS=\"\\f\"} NR==k' incoming/BQT/BQT_v4_pages.txt | head -60; done"
}
```


### [2026-09-04T19:21:57.650Z] TOOL RESULT

```
===== pdf 15 (printed 1932) =====
[pdf page 15]
مایون ۱۹۳۲۳
و زهر عقرب و مارکند و آنرا بعربی جدوار ‎٩‏ ماج - بسکون جیم . بمعنی ماه باشد
خوانند . چه درفارسی جیم وها بهم تبدیل مییابد وعربان

مابون ؟ - با بای ابجد بروزن‌سایون, | قمرخوانند ‎٩‏ - و بمعنی راوی و روایت کننده
نام علتی است - و حیز و مخنت و پشت پاییرا | هم هست ۷ - و نام راوی رودکی (۲) شاعرلیز
هم میگورند و در عربی لیز همین معنی‌دارد چه بوده است ۸ .
مفمول ۴ ابنه است, وابنه علتی باشد در موضع ماچ ‎٩‏ - بسکون جیم فارسی » بعمنی
مخصوص . بوسه است که بعربی قبله کوبند ‏

ماقر نگ ؟ « بکر تا ورای قرشغت ماچوچه - با هر دو جیم فارسی بر
و سکون نون و کاف فارسی , چلپاسه را کوبند | وزن ماسوچه (۳) . ظرفی باشد لوله دار که با
و بعضی کوبند سام ابرص اشت که نوعی ازچلیاسه آن (4) شربت و دارو در کلوی اطفال ريزند.
باشد . چون شکم او را بشکافند و بر کزندکی ماچ وموچ *0(۱) ۰ با میم بروزن
عقرب نپند در ساعت درد ساکن شود . قاچ و قوچ ‎)٩(‏ ۰ بممنی بوس و لوی باشد بعنی

ماتور نگ * - با قوقانی بواو رسدء | بوسیدن ولیسیدن چنانکه کربه کند بچه خودرا.
و رای بی نقطةٌ مفتوح بنون وکاف فارسی زده » ماخ - پسکون خای نقطه‌دار ».زر قلب
بمعنی‌سوسمار است وآن جاتوری باشد که شافعی فاسره راکوبند -ومردم سفله ودون همت وکمینه
مذهبان خورند و عربان ضب خوانند . بموش | و خسیس و منافق را نیز کفته‌اند - وبمعنی‌مردم
خرما شاهتی دارد لیکن ازوبزرکه‌تر است . پیه پیر و حقیر هم آمده است ند
اورا (۱) زنان بجهت فربه شدن خورند - ماخادیپون - با ثاك بالف کشدء

() چش :آنرا". () چك : رودگی . () چش : ماسوجه .

() چك : بان . (ه) چك : ماج وموج ؛ چش : ماچ و موج .

() چك : قاج وقوج ؛ چش : فاج وقوح -

۱ رك : جدوار . ۴ - (عر) ابنه بشیه ابنا . متهم کرد او را بچیزی ؛ مابون
متهم » و صاحب قاموی گفته که لفظ مأبون در خین وشر هن دو متعمل میشود ... لیکن اکر
آنرا مطلق استعمال کنند مراد ازآن متهم بشر باشد فقط .> «منتهی آلارب» در فارسی تصرفی در
معنی آن کرده‌اند . ۴ - مراد اسم مفعول است . ۴ -قس : مانورنگه .

8 -قی : مانرنگه ۹ -لفتی در «ماء» (غ.م.) ( رك : فهرست ولف ):

چو تو شاه بنشت بر نخت عاج فروغ ازئ و کررد همه مهر وماج.
«فردوسی طوسی . شاهنامة بخ ج ۵ص ۰5۱۶۶۷

۷ -اظ . بمناسبت اسم راأوی رودکی » این هعنی را ساخته اند .

۸ عمج (هم.) ‎٩‏ - تهرانی ۰1320 بروجردی 1220 «شهیدی»؛ کردی3220.
نیز: ماچپ (بوسه) « ژاباص ۰۳۸۵ کیلکی 328661 . *- در اراك ( سلطان آباد )
‎٩ 3286 0 6‏ مکی‌نژاد > . ۱- ۰« ماخ, نبهره بود از سیم وزر - وعردم دوری رانیز
کوبند .> « لفت فری مصحح اقبال ‏ ۰۷۸ و انخه بدلهای آن چنین است : « ماخ بود ازهی
نوع از سیم و زر و مردم و مانند اینها * و « ماخ سیم ناسره و مردم دون‌همت بود > « ماخ‌سیم
برهنه [ظ ۳ نبهره] بود و مردم دون همت را کویند که همتی ماخ دارد .»:
جوان شد حکیم ما جوانمرد و دل فراخ یکی پیرزن خرید ييك مغت سیم ماخ

عجدی مروزی « لغت فری ص۷۸ ۰

===== pdf 16 (printed 1933) =====
[pdf page 16]
-۹۳۳- ماد
وکسر رای بی لقطه و تحتانی بواو رسیده وبئون | کویند اسب وراقی است وآنرا عرب پرذون ‎٩‏
‏ده , بلفت پونانی نوعی از سوسن محرائی‌است | خوانند ۷ - واسب راهوار ترکی راهم گفته‌اس
که (۱) برکهای دراز دارد و بدین سبب آرا [ و اسب خوش جولایر| نی زگویند .
عربان مسیف‌الغراب ۱ خوانند و بیخ آنرا نافوخ ماخور - بر وزن لاهور . خرابات را
کویند و در بقداد بسیار میباشد . علاج بواسیب | کویند که شراب خانه و بوژه خانه و قمارخانه
کند ‏ , . باشد ۸ .
هاخان < بروزن ماهان . نا‌قربه‌ایست ماخو لیا * -بکرلام.بسنی‌مالیخولیا
از مضافات مروشاهجان ؟ - و نام یهلوانی بوده
ازپهلوانان‌چین؟ - وحاکم چین‌را نیز کویشد۴ | اس ت که خلل وکوفت دماغی و سودا وخیال خام

هماخچی « بسکون اك و جیم فارمی اس وی است و بستی گوبند عبرای
بتختانی کشیده , اسبیرا کوبند که از يك جالب
عربی واز جالب دیگن ترکی باشد وآترادونخمه ماد - بسکون دال . مغقف مادر است
هم میگوبند و بعربی مجتس 9 خوانند و بسنی | که عربان والده و ام کویند 3.۱۶

(۱) خم۱: و

<وژه‌تاهدهه وناوزلهاع < آن‌زدای ( فر ) « دزی ج ۱ص ۲:۷۱۳ ۰

۲ - یکی از قربه های مرو است . وآن جز « ماجان » با جیم است؛ و این که با خاء
است » قربة ابوملم خراسانی صاحب الدوله است « ممدم البلدان » .

۴ - در فپرست ولف نیامده . ۴ -ظ . مسحف «خاقان (چین)» .

8 - بجم اول وفتح دوم وسوم مشدد. ‎٩‏ - بکر اول وقتح سوم -

۷ - يك روز صد فیلهٌ تازی وماخچی با ساز ز رکه داد بمردان کارزار؟

مختاری غزئوی « رشیدی >.

۸ معرب آن نیز « ماخور » « تفس > . ‎٩‏ - رد : مالیخولیا .

۴ در : مادندر ۳ مادراندر - و نیز « ماد » ( پارسی باستان ۸12412 «پهلوی ۸/82
(شهرستانهای ایران بند ۲۷) نام قومی است‌آربایی ایرانی نژاد که در ابتدای قرن هفتم یا آخر
قرن هشتم ق.م. دولت ماد را تأسیس کردند » نختین پادشاه این قوم دیوکی 5ع6اها] (۷۰۸-
۵ قمم. ) و آخرین پادشاه آستیاکی - ایخ توویگو است ( 6۵۶-۵۸۶ قم ) این سلله
پدست کوروش هغامنشی منقرض شد ( ایران باستان ج۱ ص ۱۹۸ بیعد ). - و سکن این قوم

بقیه درحاشيةٌ صفحة۱۹۳۶

۰ مادر - بفتح سوم ۳ ماد ۳ مار (ه.م.). پهلوی 3212۲ ۰ 1221 از010212. حالت
فاعلی از - 32218۲ « بارتولمه ۱۱۹۷ ۲ « تیب رکه اس ۸-۱۶۷ > ۰ اوستا - 122487 » آرهنی ع
کاها22 ( ماده ) , هندی باستان - 132147 , ارمنی ۳281۳ ۰ کردی 6ا2 ( 220۷ ۵ )
(مادر ) » 12246 (کاومیش‌ماده)» افغانی 3307 ۰ استی 2206 , 5224 ۰ 3230 :180
بلوچی 21 ۰ ظ2221 ۰ 28 (مادر) ۰ ع 23428 ۰ ق8452 (مژت) . خغنی 1384
منجی 322 « اسشق ۹۵۹ »کیلکی 12247 ؛ زی که يك با چند بچه زاییده . والده . ام.

* مادرالدر - بقتح دو دال , از: مادر ۳ اندر (پسوند) . لغة بمعتی مادر دیگن (قی:
پدراسر , دختندر ) بمعنی زن پدر . مخفف آن مادندر (ه.م.)
```


## [2026-09-04T19:22:16.767Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ mawt/maut ===\"; grep -n -i 'mawt\\|maut\\b' FVQ_pages.txt | head -5\necho \"=== AFA sterben/tot ===\"; grep -n -i 'sterben\\|Tod\\b' AFA.txt | head -5\necho \"=== WEB matte/mat dull ===\"; grep -n -i \"matt.*dull\\|dull.*L. mattus\\|mattus\" WEB_vol1.txt | head -6\necho \"=== SKT Mat (L.) ctx ===\"; sed -n '11210,11216p' SKT.txt"
}
```


### [2026-09-04T19:22:16.880Z] TOOL RESULT

```
=== FVQ mawt/maut ===
1430:in Margoliouth's fidiweidi Lec-tiitex, p. 55 n., to Jslali al-Mawtiq, p. 168.
6890:" They (the reins) play on the back of the Hacjramaut camel, like a
=== AFA sterben/tot ===
1960:1) Nttürlich «rird dadurch auch die tod de Guignet (bei Richthofen Chi
2277:1) Aiufuhrliche Nachweise über ßtffoc bei WaddingtoD zam Edict. Dioelet
4748:schon TOD Jäküt L 430, IS als äÄJt-kC «aJ beieicfanet
6156:mischen überhaupt. »Den bitteren Tod zu kosten ist süss,
6221:nem Zuge dorthin ereilte ihn der Tod (Strabo Lib. XVI.
=== WEB matte/mat dull ===
28819:cheese. Gi sla Paw art i ; 1 cash’book, n. a book in which a regis Gi-sé-in/6-gen, n. [from casein, and -gen.] that ` account of money received or paid Sesh protein of milk which produces casein when cash’boy, n. formerly, a boy who carried acted upon by rennin, A money received from a customer by a sales- cise knife (nif), 1. a knife carried in a case man to the cashier, and brought back change. or sheath. 2 cash cred/it, in Scottish banking, an account 2. a table knife. : RIT with a bank by which, security having been case law, law based on previous judicial de- given for repayment, the bank may be drawn cisions, or precedents: distinguished from upon to an agreed amount: called also bank statute law. credit. cãse’mäte, n. [Fr. casemate, from It. casa- cash dis’count, a discount from the purchase malla, a casemate, from Gr. chasmate, pl. of price allowed to the purchaser if he pays chasma, a gulf; confused with It. casa, a within a specified period. house, and matto, foolish, dull, dim, dark.) cash’ew, (or ka-sho’), n. [from Fr. acajou, 1. in fortifications, (a) a vault of stone or cajou, from Hind. kaju, the cashew nut.]
59737:. without butter, jam, è it: toast. ? Creon AU Haas dry A solid: oppen ~ liquid. . unemotional; plain; ma ~of- } dry facts. 7 matter-of-fact fas 5. unfruitful; as, a dry interview 6. devoid of interest; barren; jejune: b ing; dull; as, a dry lecture; a dry subject oF 7. devoid of sympathy or cordialit rf sl cold; as, a dry reception; a dry mae . severe; sarcastic; cynical: sering: ‘aa: a ary retort, ynical; ‘sneering ies 9. in art, having a sharp. inflexit i ness of execution; lacking delcie? = Bfe ot ae or nolning stiff; formal; hard = . having little sugar or swe SS? as EEA £ & sweetness; as, a 11. in metallurgy, having more oxygen th
86076:specifically, a notch made in a tree in blazing a path through a forest. 2. a pickax; a mattock; a hack iron. 3. a dry. broken cough. 4. in Rugby football, a kick on the shin; also, a bruise caused by such a kick. hack, z, {abbrev. of hackney.) 1. a horse for hire. a horse for ail sorts of work. a saddle-horse. . an old, worn-out horse. 5. a person hired to de routine, often dull, Writing; literary drudge. t H a carriage or coach for hire; hence, a tax- icab. 7. a hackman. hack, a. 1. employed as a hack; as, a hack writer. 2. done by a hack; as, hack work. 3. stale; trite; hackneyed. hack, v.t. to let out for hire, as a horse or car- riage.
113632:mat, 7. r] spelled malte. 3 roughened; also So dull gilt or white card- 2. a Dort around a picture, either as the pora ry usually, between the picture and ra , the frame. ti atrix in printing, & M = A 3: ie matted, pl.. pp.; matting, ppr. to Peecdace a dull surface or finish on (metal,
113768:youue: superintendent or manager of ae | rangements of a hospital, the domestic arrars ‘son, or other institution, p pe a woman attendant or guard in charge of women or children, as 1n an institution. 5’ tron-age (or mat/run-),#. 1. matrons col- ively. ee E the state of being a matron, 3. matronly care or supervision. alt -à L. matronalis, from matrona, a mi’tron-al, a. aep A married woman.] pertaining to a matron; suitable to an elderly lady or to a married woman; grave; motherly. ma’tron-hood, n. the state of a matron. mi/tron-ize, v-t.; matronized, $t., pp.; ma- tronizing. ppr. 1. to make matronly. | 2. to chaperon; to have charge of, in the place ofa mother. , mi’tron-like, a. having the manners of an elderly woman; grave, sedate; becoming a matron. “ mi’tron-liness, n. the quality or state of being matronly. es. A ma/tron-ly, a. of, characteristic of, like, or suitable for a matron; dignified, sedate, staid, etc. 5 ma’trén-ly, adv. in a matronly manner. ma’trén of hon’ðr (on’), a married woman acting as chief attendant to the bride at a wedding. : p mat-ro-nym/ic, n. and a. metronymic. ma-tross’, n. [D. matroos, a sailor, from Fr. matelot, a sailor, seaman.) formerly, in a train of artillery, an assistant whose duty was to aid the gunners in loading, firing, and swab- bing tl = K ing the guns. marrush, a bulrush, Soupis lacustris, used in making floor mats in Europe. mat’su, z. [from Japan, meis, a pine.] a pine, Pinus massoniana, of Japan and China, which furnishes a tough wood much used in Japan for interior woodwork, the roots being used in maning mpblack: also called Japanese pine Masson’s pine. Bene ee tages mat-ta-gesse’, 7. A fi e. mauta more; n. (Fr. matamore, from Ar. met- a e ouse. [Rare. aS (mat), n. [Fr., from dial. mate, a lump.] in SMENE mixture of sulfides that is produced ead ee the sulfide ores of copper, nickel, ma : 3 matted a TC" a mat (dull finish). _ terless Caco dull, dim] Havinga lus-
113811:matting, n. [G. mati, dull. i
=== SKT Mat (L.) ctx ===
Mastodon,  an  extinct  elephant  (Gk.) Named  from  tlic  nipiile-like  projections  on Its  molar  teeth.  — Glc.  fMurr-^t,  the  female breast;  ddoi*-,  short  for  68oifr-i  stem  of Uffit,  s  tooth;  tec  Tooth.
MATERNAL.
Mat  (L.)    M.  E.  matu.    A.  S.
—  L.  mat/a  (Low  L.  naiia),  a  aiat ; Du.  mat,  G.  ma/fe.  F.  matte,  A:c
Matador,  the  slayer  of  the  buU  in bull-fight.  (Span.  — L.)  Span  mata^iar,  I slayer.— Span,  motor,  to  kilL^L  macta to  kill.  orig.  to  honour  by  a  sacrifice.  C Skt.  maA,  to  honour.     (y'MAGli.)
Match  (I),    an  equal,  a    coutcst;  I Make.
Match  (a),  a  prepared  rope  for  Brtiif cannon.  (F.-L.-Gk.)  M.  £.  macdu* O.  F.  mcscAc,  meicAt  (F.  michc),  wick  of candle,  matiji  to  fire  a  gun,  '  match  ol lampi*  Cot  — LowL.  wyjE3*,nolfoun»Uifl =  Gk.  fiv(a) ;  Low  I^  myxui,  the  .noule  of lamp,  through  which  the  wick also,  a  wick.  —  Gk  /ii'fi.  the  n lamp;  the  more  original  senses mucus  (i)  DOstriL  Allied  to  Mooua match-lcck,  the  lock  of  a  con  hohttof match  i  hence,  the  gun  itselt
```


## [2026-09-04T19:22:19.908Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT leaf for 1443 ===\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Er  ist  gestorben' in p: print('leaf',i,'printed',i-26)\n    if 'Morgana' in p: print('morgana leaf',i,'printed',i-26)\nEOF\necho \"=== LKT 1443 head ===\"; sed -n '3315,3322p' LKT.txt\necho \"=== LKT margarites/Perle Nr ===\"; grep -n -i 'murwarid\\|morvarid\\|Perlmutter\\|margarit' LKT.txt | head -5"
}
```


### [2026-09-04T19:22:21.710Z] TOOL RESULT

```
=== LKT leaf for 1443 ===
morgana leaf 140 printed 114
leaf 142 printed 116
=== LKT 1443 head ===
115
[Ar.  mät{a).
magaroca,  eigentlich  'Spindelvoll',  dann wegen  derselben  Gestalt  'Maiskolben'. Über  tk.  masure,  masra  wurde  rum. mosor,  demin,  mosoras  'Spule,  Rolle'. [DE  312/313.  Eguilaz  449.  Löbel EITAP  65.
1443.  Ar.  inät(a):
'Er  ist  gestorben,  tot';  als  Fachausdruck der  Schsichspieler  säh  mät  vom  pers. sah  'König'  [Horn  NpEtS.  170,  Nr.  772]: 'Der  König  ist  tot' ;  hieraus  ist  mit  dem Schachspiele  selbst  der  Ausdruck  inter- nal ional  geworden,  vor  allem  it.  scacco matto  'schachmatt',  prov.  mat,  frz.  Schee et  mat,  sp.  jaque  y  mate,  jaqiii  mute,  pg. chaque  i  mate,  rum.  mat;  dtsch.  schach- matt, engl;  checkmate;  russ.  sahmaty 'Schachfiguren',  hulg.  suhmatna  igra 'Schachfigur',  sahmatna  (izska  'Schach- brett'. Aus  dem  Schachspiel  wurde volksctymologisch  parodierend  it.  matto 'verrückt'  genommen.  Dazu  die  Vb.  it. mattare,  frz.  mater,  prov.  kat.  sp.  pg. matar  'matlsetzen,  überwinden,  besiegen' und  schiiefälich  sp.  pg.  matar  'töten' [und  nicht  etwa  <^  lat.  mactari,  worin et  y  ch  geworden  wäre  wie  factum  > hecho],  —  [Henii  Estienne,  Traicte  de la  confnrmite  du  langage  franqais  avec  le grec,  Paris  1569,  führt  trz.  mat  auf  it. matto  und  dieses  auf  gr.  judiTaioc;  zurück!] [Kluge  302.  ML  .5401.  SPITZER  in Herrigs  Archiv  CXLI,  264.  ZDMG XX  Vi  II,  696.
1444.  Ar.  matniti>a:
'Erdgrube  für  Getreide,  Keller';  hieraus kat.  sp.  pg.  mazniorra,  pg.  masmorra, matumorra  [mit  Anlehnung  an  matai- 'töten']  'unterirdischer  Kerker,  Verlies, Gelaß'.  [DE  312.  Eguilaz  448/449. ML  ■■^41 4.
144.5.  Tk.  iiüttrabaz: 'Fechtmeister,  Händler,  Schurke,  Betrü- ger' [aus  ar.  motr,  matra  'Öl -oder Wasserschlauch'  und  pers.  häz,  Präsens- stamm von  bähtän  'spielen'  Horn  NpEt S.  35,  Nr.  150),  matrabazlyk  'Handel'; hieraus  rum.  matrapazlic  'Schacher, Hinterlist'.  —  Löbel  ELTAP  62.
=== LKT margarites/Perle Nr ===
828:Auch  bej  'Herr,  Baron'  [Stamm  baj  s. hier  Nr.  260],  eigentlich  Titel  des  mu- hammedanischen  Feudaladels  in  der Türkei,  früher  mit  manchen  eifersüchtig gewahrten  Vorrechten  verknüpft ;  heute oft  vom  Träger  des  Titels  sich  selbst verliehen  und  daher  in  der  Bewertung gesunken.  In  allen  europäischen  Spra- chen als  Fremdwort,  z.  B.  dtsch.  Bei/. Als  Lehnwort  rum.  öem;  betlic  'die Würde  eines  Begs' ;  beizadea  'Sohn  eines Begs'  [zu  zaäea  vgl.  hier  Nr.  69  b]. Bulg.  serb.  beg,  bej  'Fürst,  Herr'.  — Begier  beji  'Herr  der  Herren'  war  der Titel  der  Statthalter  großer  Provinzen; dtsch.  Beglerbeg,  Beilerbet.  —  Eine  be- sonders schmackhafte  Birne  erhielt  den Namen  beg  armudy  'Herrenbirne'  [wie ja  Zusätze  wie  königlich  u.  ähnl.  bei Naturgegenständen  ihren  Vorzug  an Pracht,  Wert  usw.  gegenüber  anderen andeuten  sollen,  vgl.  Basihcum  'Königs- kraut', Königskerze  (Verhascum),  Kpivov ßaaiXiKÖv  (Litium  candidum),  tk.  sultan böreji  (amaranthus)].  Hieraus  mit  fal- scher Bezugnahme  auf  die  Stadt  Ber- gamo it.  bergamotta,  trz.  bergamote.  sp. pg.  bergamota,  rum.  bergamot;  ndl.  engl. bergamot,  dtsch.  Bergamotte  [doch  Ber- gamottknöpfe mit  Volksetymologie  dial. aus  Perlmutterknöpfe  Andresen  D VE  41  ] ; russ.  bergamot.  [POTT  in  ZKM  VII, 107.  Kluge  47.  ZfromPh  XXXII,  41. XXXm,  62.    ML  1019.
3562:'Kleine  Kesseltromniel  oder  Pauke'  [vgl nakir  Lammens  FarOk  Nr.  1484] ;  hieraus mgr.  dvdKapa;  it.  nacchera,  gnacchero, naccaro  'Pauke';  im  Plr.  'Klapper', afrz.  nacaire,  nfiz.  nacre  'Perlmutter', sp.  ndcara,  näcar,  pg.  ndcar  [Constancio Dicc  711b],  VMva.nacaradä  'Pauke';  vgl. auch  frz.  gtiacare  [bei  Moliere].  —  [Das auch  von  ML  5814  gebrachte  Etymon kurdisch  nakera  ist  ein  schon  von  KÖR- TING und  DIEZ  verübter  Unfug,  der  im Anschluß  an  POTTS  ,KurdischeStudien* in  ZKM  entstanden  ist;  wie  sollte  gerade ein  kurdisches  Wort  im  Romanischen Boden  gefaßt  haben?].  —  Über  das  Tk. oder  Tat.  wurde  russ.  nakry  'Trommel', dazu  serb.  nakara  'Klapper'.  [Gorjajew 225.  Mikl  SlEtWb  211.  Eguilaz  462.
3984:1750.  Ar.  sadaf: 'Perlmuschel',  ebenso  tk.  sedef  [Kelekian Kämtis  758a];  hieraus  rum.  sidef,  sedef 'dass.';  serb.  sedef  'Perlmutter'.
```


## [2026-09-04T19:22:31.527Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT leaf 140 (p.114) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==141' LKT.txt | grep -n -i 'marǧ\\|marg\\|Koralle\\|Perle' | head -10\necho \"--- full search LKT Koralle ---\"; grep -n -i 'Koralle' LKT.txt | head -6"
}
```


## [2026-09-04T19:22:32.941Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '113630,113636p' WEB_vol1.txt | cut -c1-1200\necho \"---\"\ngrep -n -o -E \"mat.{0,4}a\\..{0,200}dull.{0,120}\" WEB_vol1.txt | head -6"
}
```


### [2026-09-04T19:22:33.064Z] TOOL RESULT

```
=== LKT leaf 140 (p.114) ===
16:1415.  Ar.  marg:
17:'Wiese,  Sumpf;  hieraus  siz.  margiu 'sumpfiger  Ort,  Sumpf,  früher  'Wald- land' ;  sp.  ahnarcha,  armajal,  pg. almarge,  almargem  'Stadt  in  flachem Lande'.  [Eguilaz  214.    GrSVociSic  240.
19:[Ar.  margan.
21:'Koralle'  [aus  gr.  laapTapiTr^q  ZDMG  LI, 304],  tk.  mergan  'dass.';  hieraus  rura. märgean,  mnrgicä;  bulg.  merdzan  'Ko- ralle'. Mit  ar.  Art.  und  Imäla  [ä  >  e] «rgab  sich  der  alte  pharmazeutische Ausdruck  frz.  almargen:  poudre  d^al- margen  'gepulverte  iioralle',  die  früher in  der  Medizin  benutzt  wurde.  —  Als Fraueiiname  ist  Morgiane  in  der  Ge- schichte von  'ALI  BABÄ  und  den  vierzig Räubern  in  1001  Nacht  zuerst  durch GALLAND  bekannt  geworden.  Er  steckt auch  in  it.  fata  morgana  'Fee  Morgana', dann  'Luftspiegelung  in  der  Wüste', schon  in  Eschenbachs  Parzival  56,  18 mhd.  Fämurgän,  Feimurgan.  —  Man hat  auch  versucht,  auf  das  ar.  Grund- wort margän  das  dtsch.  Meerschaum zurückzuführen,  zuerst  A.  Vambery  in Magyar  Nyelvör  1899,  S.  537 ;  vgl. ZfdWf  I,  361.  II,  345/346.  VII,  79^/796. Da  aber  der  tatsächlich  auf  tk.  Boden bei  Eskisehir  in  Kleinasien  gewonnene Meerschaum  tk.  liile  tisy  oder  dehiz köjmjil  'Pfeifenstein'  oder  'Meeres-, schäum',  niemals  aber  margan  heißt, muß  Meerschaum  [engl,  meerschaum, ndl.  meerschuim,  frz.  Racine  de  mer] deutsch  erklärt  werden,  was  um  so leichler  möglich  ist,  als  auch  die  vier Sorten  in  Eskisehir  an  Ort  und  Stelle mit  dtsch  Namen  „Lager,  Kasten,  Groß- baum
--- full search LKT Koralle ---
518:132.  Malediwisch  atoln: Verwandt  mit  singhalesich  ätul  'Inne- res'. Hieraus  die  europäische  Form engl,  atoll,  dtsch.  Atoll.  Darunter  ver- steht man  eine  Koralleninsel,  die  einen Ring  oder  Kranz,  manchmal  von  vielen km  im  Durchmesser,  bildet  und  in  ihrem Innern  einen  Raum  mit  brackigem Wasser  einschließt.  Die  Malediwen  sind typische  Beispiele  dieses  Baus  und gaben  daher  das  Wort  zu  ihrer  Bezeich- nung her.  Wissenschaftlich  gebraucht wurde  es  zuerst  von  DARWIN  in  seiner Abhandlung  über  The  structure  of  Co- ral  Reefs  1842,  S.  2,  wo  atoll  als  sy- nonym mit  lagoon-island  definiert  wird. Ältere  Belege,  bis  1610  zurückgehend, bei  Hobson-Jobson  40.
1014:'Nachgemachte  Perlen,  Glasperlen',  Ein- heitsnomen busra,  tk.  ebenso  bäsre; hieraus  russ.  busy,  biser,  klruss.  buseV, biser,  bulg.  serb.  biser  'Glaskorallen, Glasperlen'.  [Gorjajew  17  und  35. Bern  SlEtWb  5S.
3084:'Tribut,  Steuer'  [vom  Vb.  ?«s»na  'müssen, obligatorisch  sein'];  hieraus  frz.  lisme 'Gebühr  für  die  Korallenfischerei',  die an  die  Barbareskenstaaten  zu  zahlen  war. [Devic  DEt  152.    Lammens  Rem  147.
3264:'Koralle'  [aus  gr.  laapTapiTr^q  ZDMG  LI, 304],  tk.  mergan  'dass.';  hieraus  rura. märgean,  mnrgicä;  bulg.  merdzan  'Ko- ralle'. Mit  ar.  Art.  und  Imäla  [ä  >  e] «rgab  sich  der  alte  pharmazeutische Ausdruck  frz.  almargen:  poudre  d^al- margen  'gepulverte  iioralle',  die  früher in  der  Medizin  benutzt  wurde.  —  Als Fraueiiname  ist  Morgiane  in  der  Ge- schichte von  'ALI  BABÄ  und  den  vierzig Räubern  in  1001  Nacht  zuerst  durch GALLAND  bekannt  geworden.  Er  steckt auch  in  it.  fata  morgana  'Fee  Morgana', dann  'Luftspiegelung  in  der  Wüste', schon  in  Eschenbachs  Parzival  56,  18 mhd.  Fämurgän,  Feimurgan.  —  Man hat  auch  versucht,  auf  das  ar.  Grund- wort margän  das  dtsch.  Meerschaum zurückzuführen,  zuerst  A.  Vambery  in Magyar  Nyelvör  1899,  S.  537 ;  vgl. ZfdWf  I,  361.  II,  345/346.  VII,  79^/796. Da  aber  der  tatsächlich  auf  tk.  Boden bei  Eskisehir  in  Kleinasien  gewonnene Meerschaum  tk.  liile  tisy  oder  dehiz köjmjil  'Pfeifenstein'  oder  'Meeres-, schäum',  niemals  aber  margan  heißt, muß  Meerschaum  [engl,  meerschaum, ndl.  meerschuim,  frz.  Racine  de  mer] deutsch  erklärt  werden,  was  um  so leichler  möglich  ist,  als  auch  die  vier Sorten  in  Eskisehir  an  Ort  und  Stelle mit  dtsch  Namen  „Lager,  Kasten,  Groß- baumwolle, Kleinbaumwoile"  bezeichnet werden;  vgl.  Hugo  Grothe,  Auf  tk.  Erde. Reisebilder  und  Studien.  ^  Berlin  1903. S.  380,  wo  sich  auch  eine  Schilderung der  Gewinnung  des  Meerschaums  findet: S.  277/281.  Ferner  vgl.  Joseph  Grunze), Die  wirtschaftlichen  Verhältnisse  Klein- asiens. Wien  1897.  S.  34/44;  Dernburg, Auf  dtsch.  Bahn  in  Kleinasien.  Berlin 1892.  S.  51  ff.  „Die  Sladt  des  Meer- schaums*. —  Der  Kuriosität  halber  sei noch  die  Etymologie :  dtsch.  Meerschaum <  ar.  morsüm  [soll  heißen  marsüm] 'gesiegelt'  erwähnt,  s.  J.  G.  Kochs, Vergleichungen  mineralogischer  Benen- nungen des  Deutschen  mit  arabischen Wörtern.  Leipzig  1795.  S.40.  [Kluge  304. Devic  DEt  2.Ö/26.    Lammens  Rem  18.
```


### [2026-09-04T19:22:36.832Z] TOOL RESULT

```
shiny; lusterless; dull: said of a surface, or ;
finish, oF © A a dull surface or finish, often
mat, 7. r] spelled malte. 3 roughened; also So dull gilt or white card- 2. a Dort around a picture, either as the pora ry usually, between the picture and ra , the frame. ti atrix in printing, & M = A 3: ie matted, pl.. pp.; matting, ppr. to Peecdace a dull surface or finish on (metal,
glass, etc.)- pl. Mat-A-be/lé, Mat-a-bé’
Ma tabe nee of a Zulu tribe driyen out of les, A ansvaal by the Boers in 1837.
a chin’, n. [Sp., a buffoon, a grotesque me e old dance with swords and buck-
lers.
---
ugrep: error: error at position 123
bf][\x80-\xbf]*){0,120}
                       \___exceeds complexity limits
```


## [2026-09-04T19:22:43.792Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '113625,113632p' WEB_vol1.txt | cut -c1-1500"
}
```


### [2026-09-04T19:22:43.863Z] TOOL RESULT

```
mat
p.;matting, ppr. 1. to h a mat or mats.
t, vt Povi felt, or tangle together
cover 2. intoa t
OFr. ha ited. from Ar. mat.) not glossy
shiny; lusterless; dull: said of a surface, or ;
finish, oF © A a dull surface or finish, often
mat, 7. r] spelled malte. 3 roughened; also So dull gilt or white card- 2. a Dort around a picture, either as the pora ry usually, between the picture and ra , the frame. ti atrix in printing, & M = A 3: ie matted, pl.. pp.; matting, ppr. to Peecdace a dull surface or finish on (metal,
```


## [2026-09-04T19:23:52.332Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAM mat/echec ===\"; grep -n -i '^MAT\\|ECHEC\\|Échec\\|MATADOR' LAM.txt | head -10\necho \"=== AHD mad- root ===\"; grep -n -i '^mad-\\|^m.d-.*wet\\|MATTE\\|^MAT ' AHD_watkins1985.txt | head -10\necho \"=== AHD mad ctx ===\"; grep -n -i 'mad-' AHD_watkins1985.txt | head -8\necho \"=== WEB matador headword ===\"; grep -n -o -E \"mat.a.dor[^ ]{0,20}\" WEB_vol1.txt | head -5\necho \"=== LEW margarita/mattus recheck ===\"; grep -n -i 'margar' LEW_1910.txt | head -5; grep -c '' LEW_1910.txt"
}
```


### [2026-09-04T19:23:53.975Z] TOOL RESULT

```
=== LAM mat/echec ===
387:matelas, curcuma et culcuma, sensal, fanal, azérole, cara-
455:Au milieu on rend par ch: échecs, pacha ; ^ : usnée,
685:quifoux,foUj (pièce du jeu d'échecs); de JJill al-fil l'élé-
1595:matboâkhj ou iUtjj rou^nâma (2). Ce qui est certain aussi
3226:matif .• Jjiip , il est vrai, ne s^rencontre pas, avec ce sens,
3780:Échecs. Ptg : escaques. /i? ; scacchi. - On a proposé
3782:escaques et scacchi ne le permet pas. Échecs vient de dliJI
3786:La présence du c dans échec s'explique par la manière
3790:L'expression échec et mai est une altération de Cj\a oLlil
3803:OU bien «1»U ©llll echchâh mât, d'où vient notre échec et
=== AHD mad- root ===
558:[hulé. Forest, timber, hence stuff, matter. Greek noun of unknown origin. -YL, YLEM; HYLOZOISM, METHYLENE.]
708:mad-. Moist, wet; also refers to various qualities of food. 1. Sanskrit madati, “it gladdens, it bubbles,” hence madana-, delightful, joyful, hence madanah, a myna bird: MYNA. 2. Suffixed form *mad-i- in Germanic *mati- in: a. Old English mete, food: MEAT; b. Middle Low German (ge)mate (ge-, together, from Germanic *ga-; see kom), “he with whom one shares one’s food,” compan- ion: MATE}, 3. Suffixed form *mad-sto-, becoming *mazdo-, in Germanic *masta- in Old English mest, fodder: MasT?. [Pok. mad- 694.]
730:tive masculus, male, manly: MACHO, MALE, MASCULINE; EMASCULATE.] mat-. A kind of tool. Old English mattuc, mattock (prob- ably borrowed from Vulgar Latin *mattea): MATTOCK. [Pok. 2. mat- 700.] mater-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -fer-. 1. Germanic *méthar- in Old English mddor, mother: MOTHER}. 2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRI- MONY. 3. Greek métér, mother: METRO-; METROPOLIS. 4, Latin mdteriés, materia, tree trunk (< “matrix,” the tree’s source of growth), hence hard timber used in carpentry, hence (by a calque on Greek Aulé, wood, matter) substance, stuff, matter: MATERIAL, MATTER. 5. Greek compound Démétér, name of the goddess of produce, especially cereal crops (dé-, possibly meaning “earth”): DEMETER. [Pok. mdter- 700.] math-. Worm. With uncertain preform, but clearly re- lated, is Old English moththe, moth: motu. [Pok. 1. math- 700.] [Mawort-. Name of an Italic deity who became the god of war at Rome (and also had agricultural attributes), hence also the name of the planet Mars (doubtless from its red color, the color of blood). Latin Mars (stem Mart-), Mars: MARCH, MARS, MARTIAL, MARTIAN.] mazdo-. Pole, rod, mast. Germanic *mastaz in Old Eng- lish mest, mast: MAST}. [Pok. mazdo-s 701.] me-1. Oblique form of the personal pronoun of the first person singular. For the nominative see eg. 1. Germanic *mé- in Old English mé (dative and accusative): ME, MYSELF. 2. Possessive adjective “mei-no- in Germanic *min- in: a. Old English min, my: MINE?, My; b. Middle Dutch mijn, my: MYNHEER. [Pok. 1. me- 702.] me-2, In the middle of. 1. Suffixed form *me-dhi in Germanic *mid- in Old English mid, among, with: MID- WIFE. 2. Suffixed form *me-ta in Greek meta, between, with, beside, after: META-. See also medhyo-. [Pok. 2. me- 702.] mé-1, Expressing certain qualities of mind. Contracted from *meo-. 1. Suffixed o-grade form *mé6-to- in Ger- manic *méthaz in (i) Old English méd, mind, disposition: MooD! (ii) Old High German muot, mind, spirit, in German Gemiit, spirit, feelings, temperament: GEMUT- LICH, GEMUTLICHKEIT. 2. Perhaps Latin més (< *mé-s-), wont, humor, manner, custom: MORAL, (MORALE), MORES, MOROSE. [Pok. 5. mé- 704.] m6-2, To measure. Contracted from *meo-. I. Basic form mé-. 1. Suffixed form *mé-lo- in Germanic *mélaz in Old English m#l, “measure, mark, appointed time, time for eating, meal”: MEAL?; PIECEMEAL. 2. Suffixed form *mé-ti- in Latin métiri, to measure: MEASURE, (MEN- SURAL); (COMMENSURATE), DIMENSION, IMMENSE. 3. Possibly Greek metron, measure, rule, length, propor- tion, poetic meter (but this is referred by some to med-): METER!, METER?, (METER?), -METER, METRICAL, -METRY; DIAMETER, GEOMETRY, ISOMETRIC, METROLOGY, METRO- NOME. 4, Suffixed form *mé-trd- in Sanskrit mdtrd, a measure: MAHOUT. II. Extended and suffixed forms *mén-, *mén-en-, *mén-s-, *mén-dt-, moon, month (an ancient and universal unit of time measured by the moon). 1. Germanic *ménén- in Old English ména, moon: Moon; (Monpay). 2. Germanic *ménéth- in Old English ménath, month: MONTH. 3. Greek mén, méné, month: AMENORRHEA, CATAMENIA, DYSMENORRHEA, (MENARCHE), MENISCUS, MENOPAUSE. 4. Latin ménsis, month: MENSES, MENSTRUAL, (MENSTRUATE); BIMES- TRIAL, SEMESTER, TRIMESTER. [Pok. 3. mé- 703, ménot- 731. fen Big. Contracted from *meo-. 1. Suffixed (compara- tive) form *mé-is- in Germanic *maiz6n- in Old English mara, greater, and madre (adverb), more: MORE. 2. Suf- fixed (superlative) form *mé-isto- in Germanic *maista- in Old English m&st, most: Most. 3. Suffixed o-grade
1829:MATCH2 meug-2 MATE! mad- MATELOTE neud- MATER miater- MATERIAL miater- MATERNAL miater- MATERNITY méater- MATHEMATICAL mendh-1 MATHEMATICS mendh-! MATINEE méa-1 MATINS ma-1 MATRICLINOUS  klel- MATRICULATE miter- MATRIMONY miater- MATRIX miater- MATRON miater- MATTER méater- MATTOCK mat- MATURE ma-1 MATUTINAL ma-1 MAUL mele- MAULSTICK mel-2 MAUVE malakhé MAW mak-2
=== AHD mad ctx ===
708:mad-. Moist, wet; also refers to various qualities of food. 1. Sanskrit madati, “it gladdens, it bubbles,” hence madana-, delightful, joyful, hence madanah, a myna bird: MYNA. 2. Suffixed form *mad-i- in Germanic *mati- in: a. Old English mete, food: MEAT; b. Middle Low German (ge)mate (ge-, together, from Germanic *ga-; see kom), “he with whom one shares one’s food,” compan- ion: MATE}, 3. Suffixed form *mad-sto-, becoming *mazdo-, in Germanic *masta- in Old English mest, fodder: MasT?. [Pok. mad- 694.]
1827:MasT2 mad-
1829:MATCH2 meug-2 MATE! mad- MATELOTE neud- MATER miater- MATERIAL miater- MATERNAL miater- MATERNITY méater- MATHEMATICAL mendh-1 MATHEMATICS mendh-! MATINEE méa-1 MATINS ma-1 MATRICLINOUS  klel- MATRICULATE miter- MATRIMONY miater- MATRIX miater- MATRON miater- MATTER méater- MATTOCK mat- MATURE ma-1 MATUTINAL ma-1 MAUL mele- MAULSTICK mel-2 MAUVE malakhé MAW mak-2
1840:MEAT mad-
1898:MUSTARD meu- MUSTELINE mis- MUSTER men-! MUSTY meug-2 MUTATE mei-1 MUTCHKIN med- MUTE mul- MUTILATE mut- MUTTER mul- MUTTON mel-1 MUTUAL mei-1 MUZHIK man-1 MUZZLE musum MY me-1 MYCELIUM walso- -MYCETE meug-2 MYCO- meug-2 MYCORRHIZA wrad- MYELO- mis- MYIASIS § mu-2 MYLONITE mele- MYNA mad- MYNHEER me-1 MYO- mis- MYOCARDIUM kerd-1 MYOPIA mut-, okw- MYOSOTIS miis-, ous- MYRIAD meu- MYRMECO- morwi- MYROBALAN gWel@-2 MYSELF me-! MYSOPHILIA meu- MYSOPHOBIA meu- MYSTAGOGUE ag- MYSTERY! mut- MYSTERY? mei-2 MYSTIC mul- MYSTICETE miis- MYTHOPOEIC kWeij-2 MYXO- meug-2
=== WEB matador headword ===
113638:mat/a-dor,
=== LEW margarita/mattus recheck ===
14866
```


## [2026-09-04T19:24:06.531Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAM echec ctx ===\"; sed -n '3778,3810p' LAM.txt\necho \"=== LAM leaf ===\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if \"echchâh mât\" in p: print('leaf',i,'printed',i-57)\nEOF\necho \"=== WEB matador ===\"; sed -n '113636,113642p' WEB_vol1.txt | cut -c1-900\necho \"=== LEW coverage ===\"; head -3 LEW_1910.txt; grep -c 'madeo\\|mater,\\|magnus' LEW_1910.txt; awk 'BEGIN{RS=\"\\f\"}END{print NR\" leaves\"}' LEW_1910.txt"
}
```


### [2026-09-04T19:24:08.221Z] TOOL RESULT

```
=== LAM echec ctx ===
arabe il se déclinerait • • «^ I \^\y ùb c^^ ^^ ctA"^'-^
sjj^ ii^ ù^rV St ( Mu*arrab, 17. )
Échecs. Ptg : escaques. /i? ; scacchi. - On a proposé
l'arabe >^* ach^heikh; mais la présence de Va dans
escaques et scacchi ne le permet pas. Échecs vient de dliJI
ach-châh^ formé de l'article arabe et du persan chah] roi.
« Le joueur qui met le roi sous le coup d'une prise avertit
son adversaire en disant: ech-châh, le roi!» (Devic).
La présence du c dans échec s'explique par la manière
dont les Arabes faisaient sentir le o A persan final ; ils lui
donnaient habituellement la valeur d'un J , d'un ^ ou
d'une autre lettre sonore (i).
L'expression échec et mai est une altération de Cj\a oLlil
echrchâh mât^ que M. Dozy avait d'abord traduit par « le
roi est mort » prenant ZX* , mât^ pour le verbe arabe
mourir- Plus tard dans son Supp. il s'est corrigé (2). vIjU
mât serait tout simplement un adjectif persan signifiant
étonné, surpris (jv^ ) On dit indifféremment oU oit
chah mâtj ou cX^ chahmâtn d'où l'ital: scacco matto;
(1) Compar. igiL^ (d'où l6 franc: Belléric, sorte de m^rrobolan) venant de
p6i*8an J^ - et Emblic de ^pXA amlag, da persan ^, amlefu On éciit en-
core Emblique et Amblique, Poui* le changement da y en j comp. JjJyf da
penan , jj^ , et j*^ du pers. «i^ ( Muarrab, 42 ) etc.
(2) Sur les observations de M' G^demeister et de Mirza Kasem-Bey.I04
ÉLIX
OU bien «1»U ©llll echchâh mât, d'où vient notre échec et
mat et Tespagn : xaquey mate. La présence de la particu-
le conjonctive me semble due à l'aspiration médiale (o) de
OUdLltl ech-châhmât^ qui dans la prononciation du peuple
devient ech-chahêmat.
Élizir. Esp. Ptg: elixir. //: elisire. C'était chez les
alchimistes la matière, qu'on répandait sur les métaux,
pour les changer en or ; de jiS)l[al-iksîr, pierre philo-
=== LAM leaf ===
leaf 161 printed 104
=== WEB matador ===
lers.
mat/a-cd, x. [S. Am.] a South American three-
banded armadillo: written also matico. mat/a-dor, 7. [Sp., 2 murderer, slayer, from at’a
malar, to kill, from L. mactare, to sacrifice, im-
molate,) ic shter whose specialty is killing
with a sword thrust at the end of a
A oe after performing a series of formal- ized actions with a cape to anger and tire the animai ard playing, (a) any one of the four jacks or knaves, the highest trumps in skat; (b) any one of the highest three trumps in ombre, solo, or quadrille; (c) a game played with dominoes, in such a manner that the sum of the spots of any two adjacent ends is always seven; also, the 1:6, 2:5, 3:4, or double blank in that game.
=== LEW coverage ===
eae hee ne
ee
Duquesne University:
0
305 leaves
```


## [2026-09-04T19:24:49.066Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'feta  morgana' in p: print('morgana leaf',i,'~printed',(i-12)*2)\n    if 'margarite,  n.,  1)  a  pearl' in p: print('margarite leaf',i,'~printed',(i-12)*2)\nEOF\necho \"=== SKT magpie leaf/printed ===\"\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Magpie,  a  bini' in p: print('magpie leaf',i,'printed',i-20)\nEOF\necho \"=== FSD checkmate leaf ===\"\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Ar.  shdh*mat' in p or 'shdh*mat' in p: print('checkmate leaf',i)\nEOF"
}
```


### [2026-09-04T19:24:51.531Z] TOOL RESULT

```
morgana leaf 313 ~printed 602
margarite leaf 504 ~printed 984
=== SKT magpie leaf/printed ===
magpie leaf 289 printed 269
=== FSD checkmate leaf ===
checkmate leaf 511
```


## [2026-09-04T19:24:57.630Z] AGENT

Now I'll write the updated JSON.


## [2026-09-04T19:27:55.028Z] TOOL CALL #55: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/update345.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nP='/home/sfmqrb/git/rishe/data/verification/page-345.json'\nd=json.load(open(P,encoding='utf-8'))\n\ndef C(src,where,stance,note):\n    return {\"src\":src,\"where\":where,\"stance\":stance,\"note\":note}\n\n# ---------- shared quotes ----------\nPHD_Q = (\"PHD.txt leaf 80 (printed p. 59), s.v. morwārīd: \\\"morwārīd [mwlw'lyt' | M mwrwryd, N ~] pearl\\\" \"\n         \"— MacKenzie's Book-Pahlavi spelling mwlw'lyt' is exactly Nourai's 'Murvârît', and 'N ~' means \"\n         \"New Persian has the same word.\")\nNYB_Q = (\"NYB_vol2_glossary.txt leaf 148 (Glossary p. 140), s.v. murvārīt: \\\"murvārīt [mwlw'lyt'] pearl, \"\n         \"coll. pearls ... MPrth mwrg'r'yd (A-H III), mwrgryd (MHC), borrowed from Gr μαργαρίτης; murvārīt \"\n         \"with -v- < -γ- = NP murvārīd, SW form.\\\" Nyberg makes the Pahlavi word a LOAN FROM Greek, i.e. he \"\n         \"reverses the chart's Pahlavi → Greek arrow.\")\nHUB_Q = (\"HUB.txt leaf 258 (Persische Studien p. 248, §140 'Für ap. g erscheint v in:'): \\\"marvarīd 'Perle' \"\n         \"(marvarīdīn 'of pearl' JRAS. 1894, p. 488), phl. marvārīt etc. (Nöldeke, Pers. Stud. II, 44) = \"\n         \"μαργαρίτης\\\" — NP marvārīd = Pahlavi marvārīt, equated with Greek margarítēs; listed among the \"\n         \"Old-Persian g > v cases (Marv = OP Margu-), which is the -γ- > -v- change behind murwārīd.\")\nPLA_Q = (\"PLA_pages.txt leaf 262 = Asbaghi, Persische Lehnwörter im Arabischen p. 247, s.v. marǧān: \"\n         \"\\\"marǧān: 'kleine Perle' aus pers. morwārīd < mp. morwārīd, murvārīt, mprth. mwrg'r'yd → griech. \"\n         \"μαργαρίτης, mand. marg(a)nīta\\\" — Arabic marǧān 'small pearl' from Persian morwārīd via Middle \"\n         \"Persian murvārīt / Parthian mwrg'r'yd, with Greek margarítēs and Mandaic marganīta as the \"\n         \"intermediate forms. This is Nourai's chart, root gloss ('small pearl') included.\")\nBQT1981_Q = (\"BQT_v4_pages.txt pdf page 64 = printed p. 1981, Mo'in's footnote 10 to مرجان: «مرجان کلمهٔ مخفف \"\n             \"عربی از لغت سریانی MARGANITA «دزی ج ۲ ص ۵۷۸» که لغت بمعنی مروارید بوده و سپس به بسد اطلاق شده \"\n             \"است. Fleischer در «تعلیقات در بارهٔ ذیل قوامیس عرب تألیف دزی» ۱۸۸۹ ص ۱۷۹ تغییر لغت یونانی \"\n             \"MARGARITES را ... و در آرامی به MARGANITA ... که از آن شکل عربی مرجان اتخاذ شده، شرح می‌دهد» \"\n             \"— Arabic marjān is a shortened form of Syriac margānītā 'pearl', later applied to coral; \"\n             \"Fleischer traces Greek margarítēs → Aramaic margānītā → Arabic marjān.\")\nBQT1997_Q = (\"BQT_v4_pages.txt pdf page 80 = printed p. 1997, Mo'in's footnote 5 to مروارید: «مروارید ... \"\n             \"پهلوی MORVĀRĪD ... از یونانی MARGARITES ... بعربی لؤلؤ» — Mo'in has the headword with the \"\n             \"Pahlavi form as Nourai draws it, but derives it FROM Greek margarítēs, which is exactly the \"\n             \"dissent the chart's own NOTE records ('BQT derives this word from Greek').\")\nLKT1416_Q = (\"LKT.txt leaf 140 (Lokotsch p. 114), No. 1416: \\\"[Ar. margān.] 'Koralle' [aus gr. μαργαρίτης \"\n             \"ZDMG LI, 304], tk. mergan 'dass.'; hieraus rum. mărgean, ...; bulg. merdžan 'Koralle'. ... \"\n             \"Als Frauenname ist Morgiane ... Er steckt auch in it. fata morgana\\\" — Lokotsch takes Arabic \"\n             \"margān straight from Greek margarítēs, without Nourai's Aramaic step.\")\nAFM_Q = (\"AFM_pages.txt leaf 145 (≈ Addi Shir p. 144, s.v. مرجان; the file has no printed-page tags): the \"\n         \"entry glosses مرجان as «صغار ... شبیه کبار الدر» (small pearl-like grains), reports the Arabic \"\n         \"philologists' fanciful مر + جان derivation, and then sets beside it «... بالارامیة ... ومروارید \"\n         \"بالفارسیة و ܡܪܓܠܝܬ و ܡܪܓܠܝܬܐ» — i.e. Aramaic/Syriac margālīt(ā) and Persian morvārīd as the \"\n         \"cognate forms, «اصلها فارسی» ('its origin is Persian'). This is the page Jeffery FVQ:261 n. 5 \"\n         \"argues against ('In spite of Addai Sher, 144').\")\nMON_MARJAN_Q = (\"MON_part2.txt line 52627 s.v. مرجان: «مرجان: [ع. مح. مروارید، بسد]» — Mo'in tags the word \"\n                \"Arabic and 'مح.' (muḥarraf, altered) from مروارید; the entry adds «مروارید (به این معنی در \"\n                \"عربی استعمال شده)» ('pearl — used in this sense in Arabic'). MON_part2.txt line 52691 \"\n                \"s.v. مرجانه: «[ع. مرجانه] واحد مرجان؛ مرواریدی کوچک» = 'unit noun of marjān; a small pearl', \"\n                \"Nourai's root gloss.\")\nSKT_MAGPIE_Q = (\"SKT.txt leaf 289 (Skeat p. 269), s.v. Magpie: \\\"Mag is short for Magot, a familiar form of \"\n                \"F. Marguerite, also used to denote a magpie. This is from L. Margarita, Gk. μαργαρίτης a \"\n                \"pearl; cf. Pers. murwārīd, a pearl.\\\" Skeat gives the whole Greek → Latin → French chain and \"\n                \"explicitly compares Persian murwārīd.\")\nKLN_MARGARITE_Q = (\"KLN_1966.txt leaf 504, s.v. margarite: \\\"ME., fr. OF. margarite (F. marguerite), fr. L. \"\n                   \"margarita, fr. Gk. μαργαρίτης (scil. λίθος), 'pearl', which is of uncertain origin. It \"\n                   \"possibly derives fr. OI. mañjaram, mañjarī, 'bud, pearl'. Gk. μάργαρον is prob. a back \"\n                   \"formation fr. μαργαρίτης.\\\" Klein calls the Greek word 'of uncertain origin' and prefers \"\n                   \"an Old Indian, not an Iranian, source — against the chart's Pahlavi → Greek arrow.\")\nWEB_MARGARITE_Q = (\"WEB_vol1.txt line 112833, s.v. margarite: \\\"[L. margarita; Gr. margarítēs, a pearl.] 1. a \"\n                   \"pearl. [Obs.] 2. a hydrated silicate of calcium and aluminum, found as scales with a \"\n                   \"pearly luster.\\\" Same column, margaric: \\\"[Fr. margarique, from Gr. margaron, a pearl: so \"\n                   \"called from the pearly luster of its crystals.]\\\"; margarine: \\\"[Fr. margarine, from \"\n                   \"margarique, margaric.]\\\"; margarita: \\\"[L.Gr. margarités ... from Gr. margarités, pearl.]\\\"\")\nLAT_MARG_Q = (\"LAT.txt leaf 707 (Ernout–Meillet p. 689), s.v. margarita: \\\"margarita, -ae (-tum n.) f.: perle. \"\n              \"Emprunt au gr. μαργαρίτης\\\" — Latin margarīta is a straight borrowing of the Greek word, as the \"\n              \"chart's Greek → Latin arrow says; derivatives margaritārius, margaritifer, Gothic marikreitus.\")\n\nSKT_MATE2_Q = (\"SKT.txt leaf 298 (Skeat p. 278), s.v. Mate (2), to check-mate, confound. (Pers. & Arab.): \"\n               \"\\\"From the game of Check-mate meant 'the king is dead.' ... — Pers. shāh māt, the king is \"\n               \"dead, check-mate. — Pers. shāh, king (see Check); māt, he is dead, from Arab. māta, he died. \"\n               \"Cf. Heb. mūth, to die. Hence Turk. and Pers. mat, astonished, confounded, amazed, receiving \"\n               \"check; O.F. mat, 'mated, quelled, subdued'; M.E. mate, confounded; Ital. matto, mad.\\\"\")\nSKT_CHECK_Q = (\"SKT.txt leaf 98 (Skeat p. 78), s.v. Check: \\\"— O.F. eschec, 'a check at chess-play,' Cot. — \"\n               \"Pers. shāh, a king, king at chess; whence shāh-māt, check-mate, lit. 'the king is dead,' from \"\n               \"māt, he is dead.\\\"\")\nSKT_MATADOR_Q = (\"SKT.txt leaf 298 (Skeat p. 278), s.v. Matador: \\\"Matador, the slayer of the bull in \"\n                 \"bull-fight. (Span. — L.) Span. matador, slayer. — Span. matar, to kill. — L. mactāre, to \"\n                 \"kill, orig. to honour by a sacrifice. Cf. Skt. mah, to honour. (√MAGH.)\\\"\")\nLKT1443_Q = (\"LKT.txt leaf 142 (Lokotsch p. 115), No. 1443: \\\"Ar. māt(a): 'Er ist gestorben, tot'; als \"\n             \"Fachausdruck der Schachspieler šāh māt vom pers. šāh 'König' [Horn NpEt S. 170, Nr. 772]: 'Der \"\n             \"König ist tot'; hieraus ist mit dem Schachspiele selbst der Ausdruck international geworden, vor \"\n             \"allem it. scacco matto, prov. mat, frz. échec et mat, sp. jaque y mate, pg. chaque e mate, rum. \"\n             \"mat; dtsch. schachmatt, engl. checkmate ... Dazu die Vb. it. mattare, frz. mater, prov. kat. sp. \"\n             \"pg. matar 'mattsetzen, überwinden, besiegen' und schließlich sp. pg. matar 'töten' [und nicht \"\n             \"etwa < lat. mactāre, worin ct zu ch geworden wäre wie factum > hecho].\\\"\")\nLAM_Q = (\"LAM.txt leaf 161 (Lammens p. 104), s.v. Échecs: \\\"L'expression échec et mat est une altération de \"\n         \"ech-châh mât, que M. Dozy avait d'abord traduit par « le roi est mort » prenant mât pour le verbe \"\n         \"arabe mourir. Plus tard dans son Supp. il s'est corrigé ... mât serait tout simplement un adjectif \"\n         \"persan signifiant étonné, surpris.\\\" Lammens (after Dozy's second thoughts) detaches the chess mât \"\n         \"from Arabic māta 'he died' and makes it the Persian adjective 'stunned' — the alternative Nourai's \"\n         \"own NOTE alludes to.\")\nFSD_CHECKMATE_Q = (\"FSD_vol1.txt leaf 511 (printed p. 457), s.v. Checkmate, n.: \\\"The final position in a game \"\n                   \"of chess, in which the king of the losing player is placed in check and can not be \"\n                   \"extricated: commonly shortened to mate. ... [< F. échec et mat, < Ar. shāh-mat, < shāh (< \"\n                   \"Per. shāh), king, + māt, is dead.]\\\"; s.v. check: \\\"[< F. échec, OF. eschec, < Per. shāh, \"\n                   \"king.]\\\"\")\nFSD_MATADOR_Q = (\"FSD_vol3.txt leaf ~15845 region, s.v. matador (OCR badly broken): the etymology bracket reads \"\n                 \"\\\"< Sp. matar (< L. mactāre) kill\\\" — Funk & Wagnalls routes Spanish matar to Latin mactāre, \"\n                 \"not to Arabic māta.\")\nWEB_MAT_Q = (\"WEB_vol1.txt line 113629, s.v. mat, a.: \\\"[... OFr. mat, defeated, from Ar. māt.] not glossy or \"\n             \"shiny; lusterless; dull: said of a surface, or finish ... also spelled matte.\\\" Webster takes \"\n             \"the 'dull' adjective straight from Old French mat 'defeated' < Arabic māt, with no Latin mattus \"\n             \"in the chain at all.\")\nWEB_MATADOR_Q = (\"WEB_vol1.txt line 113638, s.v. matador: \\\"[Sp., a murderer, slayer, from matar, to kill, \"\n                 \"from L. mactāre, to sacrifice, immolate.] ... the bullfighter whose specialty is killing \"\n                 \"with a sword thrust.\\\"\")\nWLD_MAD_Q = (\"WLD_Bd2_pages.txt leaf 236 (Walde–Pokorny Bd. II p. 231), s.v. mad- 'naß, triefen': \\\"Lat. \"\n             \"madeō, -ēre 'naß sein, von Nässe triefen', mattus 'trunken' (s. zur Form W. LEWb.² s. v., \"\n             \"Sommer Hdb.² 231), wohl auch manō, -āre 'fließen, rinnen' ...\\\" Walde–Pokorny put Latin mattus \"\n             \"under the IE root *mad- 'wet', i.e. with Pokorny against Nourai's Arabic origin.\")\nLAT_MATUS_Q = (\"LAT.txt leaf 713 (Ernout–Meillet p. 695), s.v. matus: \\\"matus, -a, -um: ivre. Mot vulgaire \"\n               \"(Petr. 41), qu'on retrouve dans les gloses ... On lit aussi mattus (natus): tristis, CGL IV \"\n               \"114,4 ... Mais peut-être sont-ce deux mots différents. Le rapprochement de l'ital. matto est \"\n               \"aujourd'hui contesté ... Mattus peut représenter une prononciation vulgaire (dialectale) de \"\n               \"*maditus.\\\" Ernout–Meillet date mattus to Petronius (1st c. CE) and derive it from *maditus \"\n               \"(madēre), and they explicitly doubt the link with Italian matto (the chess word).\")\nAHD85_Q = (\"AHD_watkins1985.txt line 708, root mad-: \\\"mad-. Moist, wet; also refers to various qualities of \"\n           \"food. 1. Sanskrit madati ... 2. Suffixed form *mad-i- in Germanic *mati- ... MEAT; ... MATE¹ ... \"\n           \"3. ... MAST². [Pok. mad- 694.]\\\" The 1985 Watkins list derives MEAT, MATE¹ and MAST² from mad-, \"\n           \"but does NOT list MAT/MATTE there — the Latin mattus link that Nourai's NOTE quotes from AHD:805 \"\n           \"is in the dictionary entry, not in the root appendix.\")\nMON_MOWT_Q = (\"MON_part2.txt line 67676, s.v. موت: «موت: [ع.] (اِ.) مرگ» ('Arabic, noun, death'), with the \"\n              \"compounds موت ابیض / موت احمر / موت اختیاری etc. MON_part2.txt line 28908, s.v. کیش‌مات: \"\n              \"«کیش‌مات: (امر.) (شطرنج) هنگامی است که مهرهٔ شاه به طریقی کیش شود که قادر به هیچ نوع حرکتی نباشد. \"\n              \"حریف، شاه مات می‌شود و بازی را می‌بازد» — 'checkmate: when the king piece is checked so that it \"\n              \"can make no move; the opponent is šāh māt and loses the game'. Both of Nourai's Persian items \"\n              \"are in Mo'in with the Arabic tag and the chess sense.\")\nBQT_SILENT_Q = (\"BQT_v4_pages.txt pdf pages 15-16 = printed pp. 1932-1933 (the میم+الف bayān, which runs مابون، \"\n                \"ماچ، ماخ، ماد، مادر …): there is no مات headword, and greps of the whole volume for «کیش مات», \"\n                \"«شاه مات» return nothing. Borhān-e Qāṭeʿ largely excludes plain Arabic loanwords, so it is \"\n                \"silent on mawt / māt / kīš-māt.\")\n\n# ---------- assemble ----------\ne0 = d['entries'][0]\ne2 = d['entries'][1]\nassert e0['entry']==0 and e2['entry']==2\n\nn0 = {n['id']: n for n in e0['nodes']}\nn2 = {n['id']: n for n in e2['nodes']}\n\n# ---- ENTRY 0 root ----\nfor it in e0['ref_check']:\n    if it['ref']=='PLA:247':\n        it['status']='supports'\n        it['note']=PLA_Q\ne0['consulted']=[\n C(\"PHD\",\"p. 59 s.v. morwārīd (PHD.txt leaf 80)\",\"supports\",PHD_Q),\n C(\"NYB\",\"Glossary p. 140 s.v. murvārīt (NYB_vol2_glossary.txt leaf 148)\",\"contradicts\",NYB_Q),\n C(\"HUB\",\"p. 248 §140 (HUB.txt leaf 258)\",\"supports\",HUB_Q),\n]\n\n# ---- ENTRY 0 nodes ----\nfor it in n0[1]['ref_check']:\n    if it['ref']=='BQT:1997':\n        it['status']='partial'\n        it['note']=BQT1997_Q\nn0[1]['consulted']=[\n C(\"HUB\",\"p. 248 §140 (HUB.txt leaf 258)\",\"supports\",HUB_Q),\n C(\"PHD\",\"p. 59 s.v. morwārīd (PHD.txt leaf 80)\",\"supports\",PHD_Q),\n C(\"MON\",\"MON_part2.txt line 54446 s.v. مروارید (Adena 2-vol abridgement)\",\"partial\",\n   \"Mo'in has the headword «مروارید» with a long mineralogical description ('جسم جامد و کروی شکل و براق … \"\n   \"که از انجماد ترشحات مخاط بدن انواعی از نرم‌تنان دو کفه‌یی بنام صدف مروارید حول اجسام خارجی …'), but the \"\n   \"bracketed origin tag is OCR-garbled in this abridgement ('۷۹۵ ۱۱ .۲ ( طبر'), so it neither confirms nor \"\n   \"denies the Pahlavi source; the 6-vol print edition's Latin-script Pahlavi form is not in the online text.\"),\n C(\"HRN\",\"HRN.txt, greps 'marvar|marwar|murwar|margar'\",\"silent\",\n   \"Horn's Grundriss has no numbered entry for marvārīd; the only m-r-w hit is no. ~1024 on mury 'bird' \"\n   \"(\\\"aw. mərəγa- 'Vogel'; phlv. murγ, murv\\\"). Jeffery FVQ:261 n. 6 cites 'Horn, Grundriss 218 n.', i.e. a \"\n   \"footnote, not a headword, so Horn is effectively silent on the pearl word.\"),\n]\nn0[2]['consulted']=[\n C(\"PLA\",\"p. 247 s.v. marǧān (PLA_pages.txt leaf 262)\",\"supports\",PLA_Q +\n   \" For this node the operative words are 'mand. marg(a)nīta' — Asbaghi's only Aramaic form is Mandaic \"\n   \"marganīta, the sister of Syriac/Jewish-Aramaic margānīṯā.\"),\n C(\"BQT\",\"vol. 4 p. 1981, Mo'in's footnote to مرجان (BQT_v4_pages.txt pdf page 64)\",\"supports\",BQT1981_Q),\n C(\"AFM\",\"≈ p. 144 s.v. مرجان (AFM_pages.txt leaf 145)\",\"partial\",AFM_Q),\n C(\"AFA\",\"AFA.txt, greps 'marg|marjan|margarit' and German 'Perle'\",\"silent\",\n   \"Fraenkel's Aramaic and Arabic are in unOCR'd script and no German gloss for 'Perle'/'Koralle' turns up; \"\n   \"Die aramäischen Fremdwörter im Arabischen yields nothing usable on margānīṯā.\"),\n]\nfor it in n0[3]['ref_check']:\n    if it['ref']=='PLA:247':\n        it['status']='supports'\n        it['note']=PLA_Q\nn0[3]['consulted']=[\n C(\"LKT\",\"p. 114 No. 1416 (LKT.txt leaf 140)\",\"partial\",LKT1416_Q),\n C(\"AFM\",\"≈ p. 144 s.v. مرجان (AFM_pages.txt leaf 145)\",\"supports\",AFM_Q),\n C(\"MON\",\"MON_part2.txt lines 52627, 52691 s.v. مرجان / مرجانه\",\"supports\",MON_MARJAN_Q),\n C(\"KLN\",\"KLN_1966.txt leaf 313 s.v. 'fata morgana' (printed ≈ p. 602)\",\"partial\",\n   \"Klein: \\\"Morgana itself derives fr. Arab. marjān, 'pearl', used also as a female name … See fairy and \"\n   \"margaric, marguerite.\\\" Klein thus glosses Arabic marjān as 'pearl' and cross-refers it to the \"\n   \"margarite/marguerite family, but gives no Aramaic step.\"),\n]\nfor it in n0[4]['ref_check']:\n    if it['ref']=='BQT:1981':\n        it['status']='supports'\n        it['note']=BQT1981_Q\nn0[4]['consulted']=[\n C(\"MON\",\"MON_part2.txt lines 52627, 52691 s.v. مرجان / مرجانه\",\"supports\",MON_MARJAN_Q),\n C(\"BQT\",\"vol. 4 pp. 1981-1982 s.v. مرجان (BQT_v4_pages.txt pdf pages 64-65)\",\"supports\",\n   \"Borhān's own article: «مرجان … و درعربی جوهرست سرخ» ('in Arabic it is a red gem') and, on the next page, \"\n   \"«مرجان … گویند از دریا می‌روید — و مروارید ریزه را نیز گویند» ('they say it grows out of the sea; small \"\n   \"pearls are also called this'), with Farroxī's line «تا لاله سرخ باشد چون مرجان». Mo'in's footnote 10 \"\n   \"(p. 1981) supplies the Syriac margānītā etymology quoted in ref_check.\"),\n C(\"LKT\",\"p. 114 No. 1416 (LKT.txt leaf 140)\",\"partial\",LKT1416_Q),\n]\nn0[5]['consulted']=[\n C(\"KLN\",\"KLN_1966.txt leaf 504 s.v. margarite\",\"contradicts\",KLN_MARGARITE_Q),\n C(\"SKT\",\"p. 269 s.v. Magpie (SKT.txt leaf 289)\",\"supports\",SKT_MAGPIE_Q),\n C(\"WEB\",\"WEB_vol1.txt line 112833 s.v. margarite / margaric / margarine\",\"partial\",WEB_MARGARITE_Q +\n   \" Webster gives the Latin/Greek chain but no opinion on where Greek got the word.\"),\n C(\"POK\",\"POK_full.txt / POK_01-03.txt, grep 'margarit|margaron'\",\"silent\",\n   \"Pokorny's IEW has no entry for margarítēs — consistent with the word being a non-IE (Oriental) loan in \"\n   \"Greek. Walde–Pokorny (WLD_band3.txt index, WLD_Bd1/Bd2_pages.txt) and Mann's IEC are likewise silent.\"),\n]\nn0[6]['consulted']=[\n C(\"LAT\",\"p. 689 s.v. margarita (LAT.txt leaf 707)\",\"supports\",LAT_MARG_Q),\n C(\"WEB\",\"WEB_vol1.txt line 112833 s.v. margarite / margarita\",\"supports\",WEB_MARGARITE_Q),\n C(\"LEW\",\"LEW_1910.txt, greps 'margarita|mattus|madeo'\",\"silent\",\n   \"The local Walde LEW scan is a 305-leaf partial whose OCR yields no dictionary entries at all (greps for \"\n   \"'madeo', 'mater,', 'magnus' all return 0 hits), so it cannot be consulted for margarīta.\"),\n]\nn0[7]['consulted']=[\n C(\"SKT\",\"p. 269 s.v. Magpie (SKT.txt leaf 289)\",\"supports\",SKT_MAGPIE_Q +\n   \" This is Skeat's evidence for the Old French link: F. Marguerite / Margot from L. Margarita.\"),\n C(\"WEB\",\"WEB_vol1.txt line 112833 s.v. margarite\",\"partial\",\n   \"Webster goes straight from Latin margarita to English margarite and does not name the Old French stage: \"\n   \"\\\"mär'ga-rite, n. [L. margarita; Gr. margarités, a pearl.] 1. a pearl. [Obs.]\\\"\"),\n C(\"FSD\",\"FSD_vol1-4.txt, greps 'margarite|marguerite'\",\"silent\",\n   \"Funk & Wagnalls has no margarite/marguerite entry in the OCR; the only hits are 'Margaritana' (a mussel \"\n   \"genus, vol. 3) and 'dudleyite … an alteration product of margarite' (vol. 2), neither with an etymology.\"),\n]\nn0[8]['consulted']=[\n C(\"WEB\",\"WEB_vol1.txt lines 112825-112884 s.v. margaric / margarin / margarine / margarite / margarita\",\"supports\",\n   WEB_MARGARITE_Q + \" Webster covers four of the node's seven words (margarite, margarine, margaric, \"\n   \"margarita) and traces all of them to Greek margaron/margarítēs 'pearl', with margarine explicitly named \"\n   \"for the 'pearly luster of its crystals' — the chart's chain minus the Old French step for the chemical \"\n   \"terms, which is how the node's derivation already describes it.\"),\n C(\"SKT\",\"p. 269 s.v. Magpie (SKT.txt leaf 289)\",\"partial\",SKT_MAGPIE_Q +\n   \" Skeat has no 'margarite' headword; he covers the family only under Magpie (Margot < Marguerite < L. \"\n   \"Margarita) — supporting Margaret/Marjorie but saying nothing about margarine or Rita.\"),\n C(\"FSD\",\"FSD_vol1-4.txt, greps 'margarite|margarine'\",\"silent\",\n   \"No margarite or Margaret entry surfaces in the Funk & Wagnalls OCR; only 'oleomargarine' (vol. 4 \"\n   \"pronunciation key) and 'Margaritana' (vol. 3).\"),\n]\n\n# ---- ENTRY 2 root ----\ne2['consulted']=[\n C(\"SKT\",\"p. 278 s.v. Mate (2) (SKT.txt leaf 298)\",\"supports\",SKT_MATE2_Q),\n C(\"LKT\",\"p. 115 No. 1443 (LKT.txt leaf 142)\",\"supports\",LKT1443_Q),\n C(\"LAM\",\"p. 104 s.v. Échecs (LAM.txt leaf 161)\",\"partial\",LAM_Q),\n C(\"FVQ\",\"FVQ_pages.txt, greps 'mawt|maut'\",\"silent\",\n   \"Jeffery has no entry for mawt/māta — the root m-w-t is native Semitic and therefore outside the scope of \"\n   \"The Foreign Vocabulary of the Qur'ān; the only hits are 'Haḍramawt' and a bibliographic 'al-Mawāqif'.\"),\n]\n\n# ---- ENTRY 2 nodes ----\nn2[1]['consulted']=[\n C(\"SKT\",\"p. 278 s.v. Mate (2) (SKT.txt leaf 298)\",\"supports\",SKT_MATE2_Q +\n   \" For this node: 'māt, he is dead, from Arab. māta, he died. Cf. Heb. mūth, to die' — the Arabic verbal \"\n   \"root of which mawt is the maṣdar.\"),\n C(\"LKT\",\"p. 115 No. 1443 (LKT.txt leaf 142)\",\"supports\",LKT1443_Q),\n C(\"FSD\",\"p. 457 s.v. Checkmate (FSD_vol1.txt leaf 511)\",\"supports\",FSD_CHECKMATE_Q),\n C(\"FVQ\",\"FVQ_pages.txt, greps 'mawt|maut'\",\"silent\",\n   \"No entry: mawt is native Arabic, not a Qur'ānic foreign word.\"),\n]\nn2[2]['consulted']=[\n C(\"MON\",\"MON_part2.txt lines 67676 (موت) and 28908 (کیش‌مات)\",\"supports\",MON_MOWT_Q),\n C(\"BQT\",\"vol. 4 pp. 1932-1933 (BQT_v4_pages.txt pdf pages 15-16)\",\"silent\",BQT_SILENT_Q),\n C(\"SKT\",\"p. 278 s.v. Mate (2) (SKT.txt leaf 298)\",\"partial\",\n   \"Skeat records precisely the Persian sense the chart gives māt: \\\"Hence Turk. and Pers. mat, astonished, \"\n   \"confounded, amazed, receiving check\\\" — i.e. he treats Persian māt 'stunned, confused' as secondary to \"\n   \"the chess phrase šāh māt, which is the reverse of the ordering implied by the chart's gloss 'dead, dull, \"\n   \"confused'.\"),\n]\nn2[3]['consulted']=[\n C(\"WLD\",\"Bd. II p. 231 s.v. mad- (WLD_Bd2_pages.txt leaf 236)\",\"contradicts\",WLD_MAD_Q),\n C(\"LAT\",\"p. 695 s.v. matus (LAT.txt leaf 713; cf. leaf 707 'mattus: v. matus')\",\"contradicts\",LAT_MATUS_Q),\n C(\"AHD\",\"AHD_watkins1985.txt line 708, root mad-\",\"silent\",AHD85_Q),\n C(\"LEW\",\"LEW_1910.txt, greps 'mattus|matus|madeo'\",\"silent\",\n   \"The local Walde LEW scan is a 305-leaf partial with unusable OCR (no dictionary entries recoverable), so \"\n   \"it adds nothing on mattus.\"),\n]\nn2[4]['consulted']=[\n C(\"WEB\",\"WEB_vol1.txt line 113629 s.v. mat, a.\",\"contradicts\",WEB_MAT_Q +\n   \" Webster's chain has no Latin mattus, so it contradicts the chart's Latin → French edge while agreeing \"\n   \"with Nourai's ultimate Arabic source.\"),\n C(\"LAT\",\"p. 695 s.v. matus (LAT.txt leaf 713)\",\"partial\",\n   \"Ernout–Meillet, after deriving mattus from *maditus, add \\\"Le rapprochement de l'ital. matto est \"\n   \"aujourd'hui contesté; cf. M.L. s.u. *mattus, 5438\\\" — i.e. they doubt that the Romance matto/mat family \"\n   \"comes from Latin mattus at all, which undercuts the chart's Latin parent for French mat.\"),\n C(\"DEV\",\"p. 159 s.v. Mat (DEV.txt leaf 192)\",\"supports\",\n   \"Devic: \\\"Mat, adjectif, au sens de terne, vient du mat des échecs. « Dans les anciens auteurs, dit M. \"\n   \"Littré, mat signifie las, humilié; c'est de ce sens qu'on est allé au sens de terne, qui paraît \"\n   \"très-récent. »\\\" — the 'dull' sense is a development of the chess word, i.e. French mat 'dull' belongs \"\n   \"with the Arabic/Persian branch rather than with Latin mattus.\"),\n]\nn2[5]['consulted']=[\n C(\"WEB\",\"WEB_vol1.txt line 113629 s.v. mat, a.\",\"supports\",WEB_MAT_Q),\n C(\"KLN\",\"KLN_1966.txt leaf 508 s.v. 'mat, adj., dull'\",\"supports\",\n   \"Klein: \\\"mat, adj., dull. — F., dull, lusterless, unpolished, fr. OF. mat, defeated, afflicted, \"\n   \"depressed, dejected; dull, fr. Arab. māt in the sentence māt ash-shāh, the king has died. The word mat, \"\n   \"orig. used only as a term of chess, gradually developed also the meanings faint, feeble, dull-colored.\\\" \"\n   \"Klein confirms the French → English edge and, like Nourai, refuses the Latin mattus route.\"),\n C(\"SKT\",\"SKT.txt leaf 298 (Skeat p. 278), s.v. Mat\",\"silent\",\n   \"Skeat's only 'Mat' headword is the floor-covering: \\\"Mat. (L.) M.E. matte. A.S. — L. matta (Low L. \"\n   \"natta), a mat\\\". He has no entry for mat/matte 'dull', so Skeat is silent on this node.\"),\n]\nn2[6]['consulted']=[\n C(\"LKT\",\"p. 115 No. 1443 (LKT.txt leaf 142)\",\"supports\",LKT1443_Q +\n   \" Lokotsch names exactly this node's two items: 'frz. échec et mat' and the verb 'frz. mater'.\"),\n C(\"SKT\",\"p. 78 s.v. Check and p. 278 s.v. Mate (2) (SKT.txt leaves 98, 298)\",\"supports\",\n   SKT_CHECK_Q + \" and, at Mate (2), \\\"O.F. eschec et mat, check-mate; Cot. … O.F. mat, 'mated, quelled, \"\n   \"subdued'\\\".\"),\n C(\"LAM\",\"p. 104 s.v. Échecs (LAM.txt leaf 161)\",\"partial\",LAM_Q),\n]\nn2[7]['consulted']=[\n C(\"SKT\",\"p. 278 s.v. Mate (2) (SKT.txt leaf 298)\",\"supports\",SKT_MATE2_Q),\n C(\"FSD\",\"p. 457 s.v. Checkmate (FSD_vol1.txt leaf 511)\",\"supports\",FSD_CHECKMATE_Q),\n C(\"WEB\",\"WEB_vol1.txt lines 31744-31747 (checkmate), 31975 (chess)\",\"partial\",\n   \"Webster defines checkmate n./interj./v.t. ('in chess, to place in check … hence, to arrest and defeat') \"\n   \"and, s.v. chess, gives \\\"from Per. shah, a king, the principal piece in the game\\\"; the etymology bracket \"\n   \"of the checkmate entry itself is lost in the OCR, so Webster confirms the Persian šāh element but not, \"\n   \"readably, the māt element.\"),\n]\nn2[8]['consulted']=[\n C(\"SKT\",\"p. 278 s.v. Matador (SKT.txt leaf 298)\",\"contradicts\",SKT_MATADOR_Q +\n   \" Skeat tags the word (Span. — L.) and derives matar from Latin mactāre, not from Arabic māta.\"),\n C(\"WEB\",\"WEB_vol1.txt line 113638 s.v. matador\",\"contradicts\",WEB_MATADOR_Q),\n C(\"FSD\",\"FSD_vol3.txt s.v. matador\",\"contradicts\",FSD_MATADOR_Q),\n C(\"LKT\",\"p. 115 No. 1443 (LKT.txt leaf 142)\",\"supports\",\n   \"Lokotsch expressly rejects the Latin route: \\\"Dazu die Vb. it. mattare, frz. mater, prov. kat. sp. pg. \"\n   \"matar 'mattsetzen, überwinden, besiegen' und schließlich sp. pg. matar 'töten' [und nicht etwa < lat. \"\n   \"mactāre, worin ct zu ch geworden wäre wie factum > hecho]\\\" — the phonological argument (mactāre would \"\n   \"have given Spanish *mechar) that Nourai's chart relies on.\"),\n]\nn2[9]['consulted']=[\n C(\"PHN\",\"PHN.txt, grep '^MATADOR'\",\"silent\",\n   \"Pihan's dictionary of French words from Arabic, Persian and Turkish has no MATADOR article — it treats \"\n   \"MAT (leaf 288, p. 257) only as the chess term; a Spanish-mediated bullfighting word falls outside his \"\n   \"scope.\"),\n C(\"DEV\",\"DEV.txt, grep 'MATADOR'\",\"silent\",\n   \"Devic likewise has no matador entry; his Mat (leaf 192, p. 159) is the chess adjective only.\"),\n C(\"LKT\",\"p. 115 No. 1443 (LKT.txt leaf 142)\",\"partial\",\n   \"Lokotsch's international list under Ar. māt(a) includes 'frz. mater' and 'sp. pg. matar töten' but stops \"\n   \"short of French matador, so he documents the Spanish verb the French noun is built on without confirming \"\n   \"the Spanish → French borrowing itself.\"),\n]\nn2[10]['consulted']=[\n C(\"MON\",\"MON_part1.txt / MON_part2.txt, grep 'ماتادور|ماتادر'\",\"silent\",\n   \"The 2-vol Adena abridgement of Mo'in on disk has no ماتادور headword; the entry Nourai cites (MON:3678) \"\n   \"is in the 6-vol print edition and is only reachable through vajehyab (see ref_check).\"),\n C(\"BQT\",\"BQT_v3/v4_pages.txt, grep 'ماتادور'\",\"silent\",\n   \"Borhān-e Qāṭeʿ (1652, ed. Mo'in 1963) is a dictionary of classical Persian and has no 20th-century \"\n   \"European loanword ماتادور; pp. 1932-1933, where م+ا words run, go مابون، ماج، ماخ، ماد.\"),\n C(\"ARY\",\"ARY_pages.txt / ARY_latin_index_pages.txt, greps 'ماتادور', 'MATADOR'\",\"silent\",\n   \"Aryanpur's Indo-European roots dictionary has no matador entry (its MAT- index lines are all under \"\n   \"'mother' and Sanskrit mātar-).\"),\n]\nn2[11]['consulted']=[\n C(\"SKT\",\"p. 278 s.v. Matador (SKT.txt leaf 298)\",\"supports\",SKT_MATADOR_Q +\n   \" Skeat confirms the node's own claim — English matador is Spanish matador 'slayer' — while routing the \"\n   \"Spanish verb to Latin mactāre rather than Arabic māta (that dispute belongs to node 8).\"),\n C(\"WEB\",\"WEB_vol1.txt line 113638 s.v. matador\",\"supports\",WEB_MATADOR_Q +\n   \" Same picture: Spanish → English confirmed, Latin mactāre preferred for the Spanish verb.\"),\n C(\"FSD\",\"FSD_vol3.txt s.v. matador\",\"supports\",FSD_MATADOR_Q +\n   \" Funk & Wagnalls also has 'matador' among the ombre/quadrille card senses and the bullfighting sense, \"\n   \"both from Spanish.\"),\n]\n\nwith io.open(P,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/update345.py"
}
```


### [2026-09-04T19:27:57.650Z] TOOL RESULT

```
written
```


## [2026-09-04T19:28:00.297Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-345.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 345"
}
```


### [2026-09-04T19:28:02.778Z] TOOL RESULT

```
JSON OK
nodes verified: 19/19
node verdicts: {'confirmed': 12, 'plausible': 5, 'disputed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 2, 'supports': 17, 'not_checked': 7, 'contradicts': 2, 'not_found': 1}
books consulted: {'supports': 28, 'partial': 13, 'silent': 16, 'contradicts': 7} | by book: {'SKT': 10, 'WEB': 9, 'LKT': 6, 'FSD': 6, 'MON': 5, 'BQT': 4, 'KLN': 3, 'LAT': 3, 'AFM': 2, 'LEW': 2, 'DEV': 2, 'HUB': 1, 'PHD': 1, 'HRN': 1, 'PLA': 1, 'AFA': 1, 'POK': 1, 'FVQ': 1, 'WLD': 1, 'AHD': 1, 'LAM': 1, 'PHN': 1, 'ARY': 1}
```


## [2026-09-04T19:28:11.183Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/verify_check.py 345 | grep -i problem; echo \"exit=$?\"\npython3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-345.json',encoding='utf-8'))\nfor e in d['entries']:\n    print('ENTRY',e['entry'],'root consulted:',len(e.get('consulted',[])),[c['src'] for c in e.get('consulted',[])])\n    for n in e['nodes']:\n        cs=n.get('consulted',[])\n        srcs=[c['src'] for c in cs]\n        flag='' if len(set(srcs))>=2 else '  <<< FEWER THAN 2'\n        print('  node',n['id'],n['lang'],len(cs),srcs,flag)\nEOF"
}
```


### [2026-09-04T19:28:13.161Z] TOOL RESULT

```
exit=1
ENTRY 0 root consulted: 3 ['PHD', 'NYB', 'HUB']
  node 1 Persian 4 ['HUB', 'PHD', 'MON', 'HRN'] 
  node 2 Aramaic 4 ['PLA', 'BQT', 'AFM', 'AFA'] 
  node 3 Arabic 4 ['LKT', 'AFM', 'MON', 'KLN'] 
  node 4 Persian 3 ['MON', 'BQT', 'LKT'] 
  node 5 Greek 4 ['KLN', 'SKT', 'WEB', 'POK'] 
  node 6 Latin 3 ['LAT', 'WEB', 'LEW'] 
  node 7 Old French 3 ['SKT', 'WEB', 'FSD'] 
  node 8 English 3 ['WEB', 'SKT', 'FSD'] 
ENTRY 2 root consulted: 4 ['SKT', 'LKT', 'LAM', 'FVQ']
  node 1 Arabic 4 ['SKT', 'LKT', 'FSD', 'FVQ'] 
  node 2 Persian 3 ['MON', 'BQT', 'SKT'] 
  node 3 Latin 4 ['WLD', 'LAT', 'AHD', 'LEW'] 
  node 4 French 3 ['WEB', 'LAT', 'DEV'] 
  node 5 English 3 ['WEB', 'KLN', 'SKT'] 
  node 6 French 3 ['LKT', 'SKT', 'LAM'] 
  node 7 English 3 ['SKT', 'FSD', 'WEB'] 
  node 8 Spanish 4 ['SKT', 'WEB', 'FSD', 'LKT'] 
  node 9 French 3 ['PHN', 'DEV', 'LKT'] 
  node 10 Persian 3 ['MON', 'BQT', 'ARY'] 
  node 11 English 3 ['SKT', 'WEB', 'FSD']
```


## [2026-09-04T19:28:34.507Z] TOOL CALL #58: Bash

```json
{
 "command": "git diff --stat data/verification/page-345.json && python3 - <<'EOF'\nimport json,subprocess\nnew=json.load(open('data/verification/page-345.json',encoding='utf-8'))\nold=json.loads(subprocess.check_output(['git','show','HEAD:data/verification/page-345.json']).decode())\ndef strip(o):\n    import copy\n    o=copy.deepcopy(o)\n    for e in o['entries']:\n        e.pop('consulted',None)\n        for it in e.get('ref_check',[]): it.pop('status',None); it.pop('note',None)\n        for n in e['nodes']:\n            n.pop('consulted',None)\n            for it in n.get('ref_check',[]): it.pop('status',None); it.pop('note',None)\n    return o\nprint('non-consulted/ref_check fields identical:', strip(new)==strip(old))\n# list ref_check status changes\nfor eo,en in zip(old['entries'],new['entries']):\n    for a,b in zip(eo.get('ref_check',[]),en.get('ref_check',[])):\n        if a['status']!=b['status']: print('ROOT',eo['entry'],a['ref'],a['status'],'->',b['status'])\n    for no,nn in zip(eo['nodes'],en['nodes']):\n        for a,b in zip(no.get('ref_check',[]),nn.get('ref_check',[])):\n            if a['status']!=b['status']: print('node',eo['entry'],no['id'],a['ref'],a['status'],'->',b['status'])\nEOF"
}
```


### [2026-09-04T19:28:36.491Z] TOOL RESULT

```
non-consulted/ref_check fields identical: True
```


## [2026-09-04T19:28:45.772Z] TOOL CALL #59: Bash

```json
{
 "command": "git status --short data/verification/page-345.json; git diff --stat -- data/verification/page-345.json; echo \"---\"; python3 -c \"\nimport json\nd=json.load(open('data/verification/page-345.json',encoding='utf-8'))\ne=d['entries'][0]\nprint([ (i['ref'],i['status']) for i in e['ref_check']])\nprint([ (i['ref'],i['status']) for i in e['nodes'][0]['ref_check']])\nprint([ (i['ref'],i['status']) for i in e['nodes'][3]['ref_check']])\nprint('root consulted srcs', [c['src'] for c in e['consulted']])\n\""
}
```


### [2026-09-04T19:28:47.596Z] TOOL RESULT

```
---
[('PLA:247', 'supports'), ('FVQ:261', 'supports')]
[('BQT:1997', 'partial'), ('FVQ:261', 'supports'), ('KGW:112', 'not_checked')]
[('BQT:1981', 'supports')]
root consulted srcs ['PHD', 'NYB', 'HUB']
```


## [2026-09-04T19:28:55.692Z] TOOL CALL #60: Bash

```json
{
 "command": "git ls-files --error-unmatch data/verification/page-345.json 2>&1 | head -2; git check-ignore -v data/verification/page-345.json; echo \"--- diff lines:\"; git diff -- data/verification/page-345.json | head -5; echo \"--- md5 of HEAD vs wt\"; git show HEAD:data/verification/page-345.json | md5sum; md5sum data/verification/page-345.json"
}
```


### [2026-09-04T19:28:57.374Z] TOOL RESULT

```
data/verification/page-345.json
--- diff lines:
--- md5 of HEAD vs wt
a0dcfc8d6ae00f290d61d205f17cbff0  -
a0dcfc8d6ae00f290d61d205f17cbff0  data/verification/page-345.json
```


## [2026-09-04T19:29:02.055Z] TOOL CALL #61: Bash

```json
{
 "command": "git log --oneline -3 && git log -1 --stat | head -20"
}
```


### [2026-09-04T19:29:02.166Z] TOOL RESULT

```
a4b085c Verify page 43 (Ak part 2, Akos)
1ac764a Verify page 42 (Ak/Aq/Aken)
7570e26 Verify page 41 (Aiw)
commit a4b085c66cf77c863406d580c6f9fbd0ae062455
Author: Sajad F. Maghrebi <sajad.faghfoor@gmail.com>
Date:   Fri Sep 4 15:28:15 2026 -0400

    Verify page 43 (Ak part 2, Akos)
    
    Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
    Claude-Session: https://claude.ai/code/session_01DKetdyx7C2nd1JdVw8aVUT

 data/verification/page-345.json                    |  484 ++-
 data/verification/page-43.json                     |  247 ++
 data/verification/process/verify-page-43.jsonl     |  266 ++
 data/verification/process/verify-page-43.md        | 4434 ++++++++++++++++++++
 data/verification/sources/web/09c07f4b665b99de.txt |  797 ++++
 data/verification/sources/web/0e0fcf91a3f27282.txt |  174 +
 data/verification/sources/web/128c1746f3e5b1a1.txt |  342 ++
 data/verification/sources/web/13142f9e8661032d.txt |    6 +
 data/verification/sources/web/1d7f1db934a03f71.txt |  291 ++
 data/verification/sources/web/21290f8fd12b8dce.txt | 1065 +++++
 data/verification/sources/web/32cbedb88926833d.txt |  262 ++
```


## [2026-09-04T19:29:22.225Z] AGENT

Done. `data/verification/page-345.json` now carries a `consulted` array on both root boxes and all 19 nodes.

**verify_check.py 345** — 0 PROBLEM lines.
- nodes verified 19/19; verdicts unchanged (12 confirmed, 5 plausible, 2 disputed; 2 roots confirmed)
- books consulted: **28 supports / 13 partial / 16 silent / 7 contradicts** (node-level tally), plus 7 more on the two root boxes
- ref checks now: 17 supports, 2 partial, 2 contradicts, 1 not_found, 7 not_checked

**Books used** (all local OCR/scans, no new web pages, so nothing to archive): SKT 10, WEB 9, LKT 6, FSD 6, MON 5, BQT 4, KLN 3, LAT 3, AFM 2, LEW 2, DEV 2, and one each of HUB, PHD, NYB, HRN, PLA, AFA, POK, FVQ, WLD, AHD, LAM, PHN, ARY. Every node has ≥3 distinct books.

**ref_check upgrades (books now on disk):**
- `PLA:247` (root + node 3, was `not_checked`) → **supports**. Asbaghi p. 247 s.v. *marǧān*: "'kleine Perle' aus pers. morwārīd < mp. morwārīd, murvārīt, mprth. mwrg'r'yd → griech. μαργαρίτης, mand. marg(a)nīta" — Nourai's whole root chart, "small pearl" gloss included.
- `BQT:1981` (node 4, was `not_checked`) → **supports**. Borhān vol. 4 p. 1981, Mo'in's footnote: Arabic *marjān* is shortened from Syriac *margānītā* 'pearl', later applied to coral; cites Fleischer for Greek → Aramaic → Arabic.
- `BQT:1997` (node 1, was `not_checked`) → **partial**. Mo'in's footnote to مروارید has the Pahlavi form as drawn but derives it *from* Greek — which is exactly the dissent the chart's own NOTE records.
- Still `not_checked`: KGW (Ibrahim) and FVA (Nahvi) — neither is on disk, as expected.

**No verdict changes.** Nothing plainly overturned an existing verdict, but two disagreements are worth flagging:
- Direction of the pearl word: Nyberg (Glossary p. 140) calls Pahlavi *murvārīt* "borrowed from Gr. μαργαρίτης", Mo'in (BQT 1997) and Lokotsch (no. 1416) agree, and Klein (leaf 504) calls the Greek word "of uncertain origin… possibly fr. OI. mañjaram". Against them Asbaghi 1988, AHD ("probably immediately from Iranian") and Hübschmann p. 248 support Nourai's Iranian → Greek arrow. Recorded as `contradicts`/`partial`; entry note already covered the dispute.
- Spanish *matar*/*matador* (node 8, already `plausible`): Skeat p. 278, Webster and Funk & Wagnalls all derive it from Latin *mactāre*; only Lokotsch 1443 backs Arabic *māta*, with the phonological argument (*mactāre* would give \**mechar*). Also new: Lammens p. 104 reports Dozy's retraction — chess *mât* as Persian 'stunned', not Arabic 'he died' — recorded as `partial` on the root and node 6.
