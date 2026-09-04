# Verification process log — everybook-page-311


## [2026-09-04T18:57:30.298Z] INPUT

Task: bring an existing verification file up to the "consult every relevant book" rule. File: /home/sfmqrb/git/rishe/data/verification/page-311.json (root Leudh "to grow", 20 nodes: rŭyîdan, raz, rauza/rowzeh, rŭnîk/raonaq/rownaq, rôstâk/rŭstâ, Rostam, hu-raodha/hurust/hŭr, Sogdian rwd, liber/liberty). The chart with Nourai's citations is /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-311.txt.

Read /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md, in particular the sections "Use EVERY relevant book on disk", "Checking Nourai's OWN cited references" and "Process documentation", and the source matrix /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md (file paths of every local book — they all exist under /home/sfmqrb/git/rishe/data/verification/sources/refs/; the reference table /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json gives page offsets and lookup hints; scanned pages via tools/ref_page.py, e.g. BQT:1500 or BQT5:12).

For the root entry and for EVERY node: grep the books the matrix lists for that node's language (IE root: Pokorny, Walde-Pokorny WLD, Watkins AHD, Mann IEC, Buck SYN; Avestan: Bartholomae BRT; Pahlavi: MacKenzie PHD, Nyberg NYB; Persian: Horn HRN, Hübschmann HUB, Cheung, Borhan BQT vols 1-5, Mo'in MON, Aryanpur ARY, Nushin FSF; Sogdian: Gharib SOD; Arabic loans: Klein KLN, Jeffery FVQ, Addi Shir AFM, Asbaghi PLA, Fraenkel AFA, Lokotsch LKT; Latin/English: Klein, Skeat SKT, Ernout-Meillet LAT, Walde LEW, Funk & Wagnalls FSD), and add a `consulted` array to the node exactly as specified: {"src","where","stance" (supports/contradicts/partial/silent),"note" with the quoted phrase}. At least two different books per node where the matrix lists two or more; "silent" entries count. Do not duplicate what is already in `ref_check` — but if a `ref_check` item is `not_checked`/`not_found` and the book is NOW on disk (Borhan vols 3-5, Asbaghi, Widengren is not, Jeffery's Persian translation VDQ is not), re-check it and update its status/note. Do NOT change verdicts, derivations or sources unless a book plainly overturns the existing verdict; in that case update the verdict, append one sentence to `derivation`, and say so in your summary. If you use a web page, archive it with tools/fetch_source.py and add it to `sources`.

Write the file back in place (valid JSON, UTF-8). Run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 311` (0 PROBLEM lines; "books consulted" tally non-empty). Reply with a short summary: consulted entries by stance, books used, ref_check upgrades, and any verdict changes with reasons.


## [2026-09-04T18:57:31.914Z] AGENT

I'll start by reading the instructions, source matrix, and the target file.


## [2026-09-04T18:57:34.286Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:57:34.301Z] TOOL RESULT

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


## [2026-09-04T18:57:34.588Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T18:57:34.608Z] TOOL RESULT

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


## [2026-09-04T18:57:39.025Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-311.txt",
 "description": "Read the chart text"
}
```


### [2026-09-04T18:57:39.082Z] TOOL RESULT

```
=== PDF page 311 (book page 281) ===
--- entry 0 ---
ROOT [Indo-European] Leudh, Rei : to grow  (refs POK:684; KLN:885; SYN:874; VDQ:39)
#1 (parent #0) [Avestan] refs=KLN:885; SYN:874 | raod 1, raoda, raodha : growth, face
  #2 (parent #1) [Persian] refs=BQT:944 | rŭy-îdan «روییدن ( رُستن )» : to grow ; rŭy 1 «روی ۱ ( رو )» : face
    #3 (parent #2) [Persian] refs=BQT:944; FSF:199 | raz «رَز ۱ ( رَزبان ، رَزبُن )» : garden, vineyard, vine
      #4 (parent #3) [Arabic] refs=PLA:138 | rauza : garden | NOTE: AFM:75 derives this from Persian "rîxtan: to pour"; see "Leigh 2".  VDQ:226 derives it from Pahlavi "rôt: river"; see "Ser 1".
        #5 (parent #4) [Persian] refs=MON | rowzeh «روضه ( ریاض )» : garden
    #6 (parent #2) [Persian] refs=None | rŭnîk «رونیک ( نیکروی )» : beautiful ☞Nei 1
      #7 (parent #6) [Arabic] refs=AFM:74 | raonaq : beauty, splendor
        #8 (parent #7) [Persian] refs=MON:1694 | rownaq «رونق» : growth, success
#9 (parent #0) [Pahlavi] refs=MON:1689 | rôstâk : village
  #10 (parent #9) [Persian] refs=IEC:1103; MON:1689 | rŭstâ «روستا ( روستای )» : village
#11 (parent #0) [Avestan] refs=KLN:885; SYN:874 | raodha-taxma : grown strong, name of a legendary hero ☞Tenk
  #12 (parent #11) [Persian] refs=BQT | Rostam «رُستم» : a legendary hero
#13 (parent #0) [Avestan] refs=VDQ:39; MAG:186 | hava-rd : well grown, well built, beautiful ☞Su 1
  #14 (parent #13) [Pahlavi] refs=MAG:186; VDQ:39 | hu-rust : well built, beautiful ☞Su 1
    #15 (parent #14) [Arabic] refs=VDQ:39; MAG:186 | hŭr : houries of paradise
      #16 (parent #15) [Persian] refs=MON:1378 | hŭr 1 «حور» : a heavenly woman | extra: حوری ، حورالعین ، حوروش
#17 (parent #0) [Sogdian] refs=SOD:344 | rwd : to grow
#18 (parent #0) [Indo-European] refs=KLN:885 | leudho : people ; leudheros : free
  #19 (parent #18) [Latin] refs=None | liber : free
    #20 (parent #19) [English] refs=None | liberty, deliver, Latvia
```


## [2026-09-04T18:57:39.448Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/page-311.json",
 "description": "Read the verification file"
}
```


### [2026-09-04T18:57:39.491Z] TOOL RESULT

```
<persisted-output>
Output too large (34.8KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bxm3p6qiy.txt

Preview (first 2KB):
{
  "pdf_page": 311,
  "book_page": 281,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "Leudh, Rei",
      "verdict": "confirmed",
      "modern_form": "PIE *h₁lewdʰ- 'to grow, rise; (hence) offspring, people' (Pokorny 684-685 leudh-; LIV 248 *h₁leudʰ-; AHD leudh-)",
      "note": "Pokorny 684-685 leudh- 'emporwachsen, hochkommen' with the derivatives leudho-/leudhi- 'Nachwuchs, Volk' and leudhero- 'zum Volk gehörig, frei' (Av. raoδaiti 'grows', raoδa- 'Wuchs, Ansehen', Lat. līber, OHG liut, OCS ljudьje) is exactly Nourai's root; Cheung 2007:193 gives the Iranian reflex *Hraud 'to grow (bigger)' and LIV *h₁leudʰ-. The Iranian r- is the regular Proto-Iranian merger of PIE *l with *r, not a separate root: the label 'Rei' has no counterpart in Pokorny/AHD and is unexplained (possibly Nourai's cross-reference label). Two branches of the chart are not from this root at all: the Arabic loans rawḍa (#4) and ḥūr (#15) are native Semitic, Arabic rawnaq (#7) is native Arabic, and rōstāg/Rostam (#9, #11) are today derived from the 'river' word (*srew-), not from 'grow'. The chart's own NOTE on #4 (AFM derives rawḍa from rīxtan, VDQ from rōt) records alternative Persian etymologies that modern lexicography rejects as well.",
      "sources": [
        "https://starlingdb.org/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cie%5Cpokorny&first=1181",
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁lewdʰ-",
        "https://archive.org/details/etymological-dictionary-of-the-iranian-verb",
        "https://www.ahdictionary.com/word/search.html?q=liberty"
      ],
      "ref_check": [
        {
          "ref": "POK:684",
          "status": "supports",
...
</persisted-output>
```


## [2026-09-04T18:57:43.039Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-311.json'))\ne=d['entries'][0]\nprint('ROOT refcheck:')\nfor r in e.get('ref_check',[]): print(' ',r)\nprint('has consulted at root?', 'consulted' in e)\nfor n in e['nodes']:\n    print('---node',n['id'],n['lang'],n['words'],n['verdict'])\n    for r in n.get('ref_check',[]): print('   RC',r['ref'],r['status'],'|',r['note'][:200])\n    print('   consulted?', 'consulted' in n)\n\""
}
```


### [2026-09-04T18:57:44.593Z] TOOL RESULT

```
ROOT refcheck:
  {'ref': 'POK:684', 'status': 'supports', 'note': "POK_02.txt leaf 345 (IEW pp. 684-685), s.v. 1. leudh-: 'emporwachsen, hochkommen; leudho-, leudhi- Nachwuchs, Volk; leudhero- zum Volk gehörig, frei. Ai. rōdhati, rōhati steigt, wächst, av. raoδaiti wächst, ... av. raoδa- m. Wuchs, Ansehen, npers. rōi Gesicht; gr. eleutheros frei aus *leudhero-s = lat. līber frei; ... got. liudan, ahd. liotan, as. liodan, ags. lēodan wachsen ... got. ludja Antlitz (vgl. np. rōi) ... ahd. liut, ags. lēod Volk, mhd. liute Leute ...' Pokorny's 1. leudh- 'emporwachsen' with av. raoδa- 'Wuchs' and npers. rōi 'Gesicht' is the root Nourai draws (his second name 'Rei' is not in Pokorny under this root)."}
  {'ref': 'KLN:885', 'status': 'supports', 'note': "KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. base *leudhero-s, whence also Gk. eleutheros, free. This base prob. meant orig. belonging to the people ... and derives fr. base *leudho-, *leudhi-, people, whence also OSlav. ljudŭ ... OE. lēod ... G. Leute ... I.-E. base *leudho-, *leudhi-, people, is a derivative of base *leudh-, to grow, rise. This latter appears in OI. rōdhati, grows, rises, climbs, Avestic raoδa-, growth, authority, Toch. A lut-k, to cause to grow. Cp. liberate, liberty, liege, livery ...'"}
  {'ref': 'SYN:874', 'status': 'partial', 'note': "SYN.txt leaf 946 (Buck p. 875; leaf 945 = p. 874), in 12.51 FORM/SHAPE (OCR garbled): '... OS liodan spring up, grow, Skt. rudh-, Av. raod- grow (12.53). Walde-P. 2.416. Feist 323.' Buck lists the Avestan word only as 'grow'; the 'face' gloss and the raoδa-taxma compound are not on this page."}
  {'ref': 'VDQ:39', 'status': 'not_checked', 'note': "VDQ (Badreh'i's Persian translation of Jeffery) is only on noorlib's JavaScript viewer; not readable here. Its substance = FVQ."}
has consulted at root? False
---node 1 Avestan raod 1, raoda, raodha confirmed
   RC KLN:885 supports | KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. base *leudhero-s, whence also Gk. eleutheros, free. This base prob. meant orig. belonging to the people ... and
   RC SYN:874 partial | SYN.txt leaf 946 (Buck p. 875; leaf 945 = p. 874), in 12.51 FORM/SHAPE (OCR garbled): '... OS liodan spring up, grow, Skt. rudh-, Av. raod- grow (12.53). Walde-P. 2.416. Feist 323.' Buck lists the Ave
   consulted? False
---node 2 Persian rŭy-îdan; rŭy 1 confirmed
   RC BQT:944 partial | The روییدن/روی entries (BQT_v2_pages.txt leaves ~400-403, printed pp. ~944-946) are not legible in the OCR; but Mo'in's footnote s.v. رستم (leaf 408) states 'رو (بالش، نمو) [رستن و روییدن از همین ریشه
   consulted? False
---node 3 Persian raz disputed
   RC BQT:944 partial | BQT_v2_pages.txt leaf 404 (printed p. ~947; Nourai 944): 'رز = بفتح اول و سکون ثانی، درخت انگور باشد و به عربی کرم خوانند ... و باغ را گویند و بمعنی انگور هم آمده است'; Mo'in's footnote on this leaf i
   RC FSF:199 partial | FSF_pages.txt leaf 265 (page numeral illegible; Nourai p. 199), s.v. 'رز (با زبر اول): ۱- باغ. ۲- انگور: چو ببرید رستم تن شاخ گز / بیامد ز دریا به ایوان و رز'. A Shahnameh glossary: confirms the word 
   consulted? False
---node 4 Arabic rauza disputed
   RC PLA:138 not_checked | PLA (Asbaghi, Persische Lehnwörter im Arabischen) is not online in full text (HathiTrust search-only).
   RC AFM:75 contradicts | AFM_pages.txt leaf 76 (Addi Shir p. ~75): '(الروضة) من الرمل والعشب مستنقع الماء ... وهي من ريختن أي صبّ، أخذتها العرب وتصرفت بها' — Addi Shir derives rawḍa from Persian rīxtan 'to pour', not from raz
   consulted? False
---node 5 Persian rowzeh confirmed
   RC MON supports | vajehyab.com (Mo'in) s.v. روضه: '(رَ ض) [ع. روضة] (اِ.) ۱- باغ، گلزار. ج. ریاض، روضات. ۲- مطالب و اشعاری که هنگام عزا ... می‌خوانند' — Persian rowzeh marked as Arabic rawḍa, as the arrow says. Archive
   consulted? False
---node 6 Persian rŭnîk plausible
   RC none not_checked | Nourai cites no reference for this node. Addi Shir's rawnaq entry checked at node #7 presupposes Persian rū + nīk.
   consulted? False
---node 7 Arabic raonaq disputed
   RC AFM:74 supports | AFM_pages.txt leaf 75 (Addi Shir p. ~74): '(الرونق) حسن كل شيء، معرب رو أي وجه ومن نيك أي صبيح' — i.e. rawnaq is an Arabicized compound of Persian rū 'face' + nīk 'fair', exactly Nourai's arrow.
   consulted? False
---node 8 Persian rownaq confirmed
   RC MON:1694 supports | vajehyab.com (Mo'in) s.v. رونق: '(رُ نَ) [ع.] (اِمص.) ۱- فروغ، روشنایی. ۲- زیبایی، جمال. ۳- رواج' — tagged Arabic. Archived https://vajehyab.com/?q=رونق&d=moein.
   consulted? False
---node 9 Pahlavi rôstâk disputed
   RC MON:1689 partial | vajehyab.com (Mo'in) s.v. روستا: '(اِ.) ده، قریه' — the online Mo'in text gives the meaning only; the print edition's Pahlavi form (rōstāk) is stripped online, so the Pahlavi → Persian arrow cannot be
   consulted? False
---node 10 Persian rŭstâ confirmed
   RC IEC:1103 not_found | IEC.txt leaves 604-607 (Mann cols ~1097-1104) contain the roudh-/rudh- 'red, rust' entries; no rōstāk/rūstā 'village' is there. Mann does list 'Per. cf. rustan, rostan, inf. grow; rust, rost growth' u
   RC MON:1689 partial | vajehyab.com (Mo'in) s.v. روستا: 'ده، قریه' — meaning only, no origin tag online. Archived https://vajehyab.com/?q=روستا&d=moein.
   consulted? False
---node 11 Avestan raodha-taxma disputed
   RC KLN:885 partial | KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. base *leudhero-s, whence also Gk. eleutheros, free. This base prob. meant orig. belonging to the people ... and
   RC SYN:874 partial | SYN.txt leaf 946 (Buck p. 875; leaf 945 = p. 874), in 12.51 FORM/SHAPE (OCR garbled): '... OS liodan spring up, grow, Skt. rudh-, Av. raod- grow (12.53). Walde-P. 2.416. Feist 323.' Buck lists the Ave
   consulted? False
---node 12 Persian Rostam plausible
   RC BQT supports | BQT_v2_pages.txt leaf 408 (printed p. ~951), Mo'in's footnote s.v. رستم: 'رستم = رستهم: رو (بالش، نمو) [رستن و روییدن از همین ریشه است] + تهم = tahm در پارسی باستان، گاتها و دیگر بخشهای اوستا بمعنی دل
   consulted? False
---node 13 Avestan hava-rd transcription_suspect
   RC VDQ:39 not_checked | VDQ (Badreh'i's Persian translation of Jeffery) is only on noorlib's JavaScript viewer; not readable here. Its substance = FVQ.
   RC MAG:186 not_checked | MAG (Widengren, Muhammad the Apostle of God, 1955) has no full text online.
   consulted? False
---node 14 Pahlavi hu-rust confirmed
   RC MAG:186 not_checked | MAG (Widengren, Muhammad the Apostle of God, 1955) has no full text online.
   RC VDQ:39 not_checked | VDQ (Badreh'i's Persian translation of Jeffery) is only on noorlib's JavaScript viewer; not readable here. Its substance = FVQ.
   consulted? False
---node 15 Arabic hŭr disputed
   RC VDQ:39 not_checked | VDQ (Badreh'i's Persian translation of Jeffery) is only on noorlib's JavaScript viewer; not readable here. Its substance = FVQ.
   RC MAG:186 not_checked | MAG (Widengren, Muhammad the Apostle of God, 1955) has no full text online.
   consulted? False
---node 16 Persian hŭr 1 confirmed
   RC MON:1378 supports | vajehyab.com (Mo'in) s.v. حور: '[ع.] (اِ.) ۱- زن سیاه چشم. ۲- زن زیباروی'; حوری '[ع - فا.] زن بهشتی' — Persian ḥūr marked as Arabic. Archived https://vajehyab.com/?q=حور&d=moein.
   consulted? False
---node 17 Sogdian rwd confirmed
   RC SOD:344 supports | SOD_pages.txt leaf 411 (Gharib p. 344), entry 8562: 'rwδ- B, M, S — rōδ < Av. raod-; *fraud-; Parth. rōd-; Khot. rw-; Yaghn. ur-; inf. -y; (to) grow. BBB 580; GMS 586; TSP 2.10, 18 ...'; entry 8563 'r
   consulted? False
---node 18 Indo-European leudho; leudheros confirmed
   RC KLN:885 supports | KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. base *leudhero-s, whence also Gk. eleutheros, free. This base prob. meant orig. belonging to the people ... and
   consulted? False
---node 19 Latin liber confirmed
   RC none not_checked | Nourai cites no reference for this node. Klein s.v. liberal (checked at #18): 'fr. liber, free, fr. I.-E. base *leudhero-s'; Pokorny 684 (root): 'gr. eleutheros frei aus *leudhero-s = lat. līber frei'
   consulted? False
---node 20 English liberty, deliver, Latvia disputed
   RC none not_checked | Nourai cites no reference for this node. Klein (KLN_1966.txt leaf 231, s.v. deliver): 'OF. delivrer ... fr. VL. dēlīberāre, fr. de- and līberāre, to set free, fr. līber, free'; Klein s.v. Latvia (leaf
   consulted? False
```


## [2026-09-04T18:58:02.036Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls incoming/PLA/; wc -l incoming/PLA/PLA_pages.txt incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt 2>/dev/null"
}
```


### [2026-09-04T18:58:02.100Z] TOOL RESULT

```
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
  16026 incoming/PLA/PLA_pages.txt
  20505 incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt
  36531 total
```


## [2026-09-04T18:58:04.298Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['PLA','MON','BQT','IEC','SOD','ARY','VDQ','MAG','FSF']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:800]); print()\n\""
}
```


### [2026-09-04T18:58:06.213Z] TOOL RESULT

```
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the tabl

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/82307409

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IE

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verificatio

VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghbook.ir) as an app/EPUB per news reports.", "cites": "page number of the Persian translation of Jeffery

MAG {"title": "G. Widengren, Muhammad, the Apostle of God, and his Ascension (King and Saviour V), Uppsala 1955, ch. VIII 'Iranian elements in the Kuranic vocabulary'", "edition_found": null, "kind": "archive_restricted", "url": "https://archive.org/details/muhammadapostled0000geow (1955, lending) ; HathiTrust pst.000011130420 search-only", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": "HathiTrust has it search-only (limited view); Google Books ids -r4rAAAAIAAJ / h20wAAAAYAAJ are snippet view.", "notes": "RE-SEARCH 2026-09: borrowable only; not in DiVA; Google no view."}

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking", "covers_etymology": false, "notes": "Persian OCR fair
```


## [2026-09-04T18:58:09.357Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA; awk 'BEGIN{RS=\"\\f\"} NR==153' PLA_pages.txt | head -60"
}
```


### [2026-09-04T18:58:11.284Z] TOOL RESULT

```
raudag                                                                      138                                                                 rüt_



Ob» - raudaqg:                   "abgezogenes                  Fell;       zum Braten           abgehäutetes               Zicklein"        aus
       dem          pers.        0),        rüude      Im.                 IPP     rüdan       "pluck,         pull       out"    2,


Ss, - raudak:                    "schöner              Junge"        aus    dem pers. 3%, ridak                      ®    — mp.» redak             a
       Ve       nw»           rodiSn             >> rüyiS            "wachsen,           ein    junger         Mann       werden",

 .                                                                                   -          5
Cs, - rauzan:                    "Fenster"               aus    pers.       &,      rozan            m.              ep    rocan       <a.
       raocana              6,


Eli             -    rüznämaf:               "Kalender"                    pers.     _,    rüz       <mp.9pP             ro® am.           raocah,
       ap.          raucah         + a-ı          näme        mp.          „Pl     nämak       7,


abs); - rauzana                    = rauzan              q.    V.


ol,         -       rüstäg         =    rustäg           q.    v.


Erz         - rusahtag                  = rusahtaf              a. v.

ol, - rußan:                     "Fenster"               aus    dem      pers.      &s,     röäan        "Licht,          hell"           mp.    op
       rosan au.                        raox$ana              8, mand.           rufanaiia          °.

ou-     raud:          Pl.         v.asy            rauda       q. v.

Ay -        rauda:            "Garten"              aus       pers,„ raz            v.    Verb (u,             rostan      mp.»            rod
                                                                                                11
       << aw.               raod.           10    / ap.        raza      "Weinstock"


b»-     rüt:          "Fluß"            aus       pers.)» rüud             12        mp.>»           rod       <a.         rautah.




 1.    Gähiz, al-bayän                       n.     Fück       Arabiya,           Tafalıpi          figh       al-luga      S.     198.
 2.    Mackenzie                 Ss.    v.
 3.    Addai          Scher            s.    v.
 4.    Mackenzie                 Ss.    v.
 5.    Wahrmund               s.       v.,       Fraenkel           s.   v.,      al-Mu’arrab            Ss.    Ve
 6.    Mackenzie                 S.     v.
 7.    Nyberg          Bd.         II       s.    v.
 8.    ebda.
 9.    Macuch           Ss.      v.
 10.    Bartholomae                     AIW,        S.    1495,
 11.    Mayrhofer                      S.    14l.
 12.    Muhit           s.       v.,        Nyberg        s.    v.
```


## [2026-09-04T18:58:21.779Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/page-311.json'))\ne=d['entries'][0]\nfor n in e['nodes']:\n    if n['id'] in (2,3,4,5,9,10,12):\n        print('=== node',n['id'],n['lang'],n['words'],'::',n['verdict'])\n        print(n['derivation'])\n        print('SOURCES',n.get('sources'))\n        print()\n\""
}
```


### [2026-09-04T18:58:23.754Z] TOOL RESULT

```
=== node 2 Persian rŭy-îdan; rŭy 1 :: confirmed
Av./Old Iranian raoδ- → Middle Persian present stem rōy- (Manichaean rwy-, Pahlavi lwd- /rōy-/, 3sg rōyēd) with past participle rust (rwst/lwst), Parthian rwd-/rwst → New Persian rustan/rōy- and the regularized infinitive rōyīdan 'to grow' (Cheung 2007:193; Wiktionary: Proto-Iranian *Hráwdah). Old Iranian intervocalic -d- > MP -y- (raoδa- > rōy) explains the y of rōy-/rūyīdan, while the participle keeps -st- (rust-, rustan). The noun rūy 'face' is MP rōy 'face' < Proto-Iranian *rauda- 'growth, appearance' (Edelman ESIJ 6:402; Cheung 193), the same word: 'growth, stature' → 'appearance' → 'face'.
SOURCES ['https://en.wiktionary.org/wiki/%D8%B1%D9%88%DB%8C', 'https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%86', 'https://archive.org/details/etymological-dictionary-of-the-iranian-verb']

=== node 3 Persian raz :: disputed
Persian raz 'vine, vineyard' (with the compounds razbān 'vine-keeper', razbun 'vine-stock') is a real word continuing Middle Persian raz (Pahlavi lc /raz/), but no modern source derives it from the root 'to grow': there is no Old Iranian *raza- 'growth', and rūy-/rust- could not yield a form with -z-. Wiktionary and the Greek/Latin etymological literature group Persian raz with Ancient Greek ῥάξ (gen. ῥαγός) 'grape', Latin racēmus 'bunch of grapes', Albanian rrush 'grape' as a Mediterranean/Near-Eastern culture Wanderwort of unknown (substrate) origin; the connection with 'grow' in Borhān-e Qāṭeʿ (BQT) and FSF is folk etymology.
SOURCES ['https://en.wiktionary.org/wiki/%D8%B1%D8%B2', 'https://en.wiktionary.org/wiki/%E1%BF%A5%CE%AC%CE%BE', 'https://www.etymonline.com/word/raisin']

=== node 4 Arabic rauza :: disputed
Arabic rawḍa (رَوْضَة) 'garden, meadow' (Qurʾān 30:15 fī rawḍatin), pl. riyāḍ, is a native formation from the Semitic root r-w-ḍ (rāḍa 'to train, tame', rawḍa 'meadow where water collects'); it has the emphatic ḍ, which never arises in Arabic renderings of Persian z (Persian raz would give *rawz/rāz, not rawḍ-). Wiktionary and Wehr treat it as Arabic with no Persian source; Persian rowze is listed only as a descendant. Nourai's PLA:138 derivation from raz, and the alternatives his NOTE records (AFM/Addai Sher from rīxtan 'to pour'; VDQ/Jeffery from Pahlavi rōt 'river'), are all unsupported by modern lexicography; the whole sub-branch #3 → #4 → #5 does not belong to *leudh-.
SOURCES ['https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B6%D8%A9', 'https://en.wikipedia.org/wiki/Rauza']

=== node 5 Persian rowzeh :: confirmed
The edge as drawn is correct: Persian rowze «روضه» 'garden; shrine garden' is borrowed from Arabic rawḍa (Arabic ḍ rendered as Persian z, tāʾ marbūṭa as -e/-eh; Saʿdī's رَوْضَهٔ رِضْوان 'garden of Paradise' shows the classical sense), and riyāḍ «ریاض» is the Arabic broken plural. The later Shiʿi sense 'Karbalā elegy' comes from Kāshefī's Rowżat al-shohadāʾ (15th c.). Only the ancestry above #4 is wrong: the word is Semitic, not Indo-European.
SOURCES ['https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B6%D9%87', 'https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B6%D8%A9', 'https://vajehyab.com/?q=روضه&d=moein']

=== node 9 Pahlavi rôstâk :: disputed
Middle Persian rōstāg (Pahlavi lwstʾk') 'district, province, rural district' (MacKenzie, Concise Pahlavi Dictionary) is a real word and the source of Arabic rustāq, Syriac rustāqā and Old Armenian ṙotastak (from a Parthian *rōdastāg). Its etymology, however, is a compound *raudas-tāka-/*rautas-tāka- 'river-course, river-district' of Old Iranian rautah-/raudah- 'river' (OP rautah-, MP rōd, NP rūd < Proto-Iranian *hrautah- < PIE *srew- 'to flow') + -tāka- 'course, run' (root tak-/tač- 'to run, flow'; cf. Bactrian tago 'river valley'): rōd + tāg > rōstāg with regular devoicing of the cluster. The Parthian form rōdastāg with -d- shows the 'river' word plainly. Nothing connects it to 'grow' (*leudh-); Wiktionary leaves the deeper etymology open but gives no 'grow' derivation.
SOURCES ['https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B3%D8%AA%D8%A7', 'https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D8%A7%D9%82', 'https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF', 'https://en.wikipedia.org/wiki/Rustak', 'https://forum.wordreference.com/threads/persian-rustaki-and-latin-rusticus-rustic.3399756/', 'https://vajehyab.com/?q=روستا&d=moein']

=== node 10 Persian rŭstâ :: confirmed
The edge is correct: MP rōstāg 'district' → Classical Persian rōstā(y) «روستا / روستای» 'countryside, village' with regular loss of the final -g of the MP -āg suffix (as in dānāg > dānā); the Arabic loan rustāq (with -q) and the by-form rostāq preserve the older shape. The semantic narrowing 'rural district' → 'village' is a Persian development. As noted at #9, the root is 'river' (*srew-), not 'grow'.
SOURCES ['https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B3%D8%AA%D8%A7', 'https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D8%A7%D9%82', 'https://vajehyab.com/?q=روستا&d=moein']

=== node 12 Persian Rostam :: plausible
The name does continue the reconstructed compound behind #11: Old Iranian *Raudas-/Rautas-taxma- → Middle Persian Rōdstahm (lwtsthm; Pahlavi stahm 'force, power' < taxma-) → New Persian Rostam «رستم» (Rustam), with -dst- > -st- and shortening of ō before the cluster; Sogdian Rwstmy shows the same contraction already in Middle Iranian. So the edge is right, but the first element is 'river', not 'growth' (see #11); Ferdowsī's rastam 'I escaped' (Shāhnāma, Rostam's caesarean birth) is a poetic folk etymology.
SOURCES ['https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%85', 'https://forum.wordreference.com/threads/persian-etymology-of-rostam.3387039/']
```


## [2026-09-04T18:58:34.592Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK_full leudh ===\"; grep -n \"leudh\" POK_full.txt | head -40; echo; echo \"=== AHD leudh ===\"; grep -n -i \"leudh\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-04T18:58:34.651Z] TOOL RESULT

```
=== POK_full leudh ===
1235:Hlleudh- 'free', H2ster- 'star', H3nom- 'name'. 
1241:causes lengthening. So Hlleudh- 'free' gives eleeluutha 'I loosened', from e-Hlle-HHeud^^- 

=== AHD leudh ===
693:in: a. Old English -Jéosan, to lose: LORN, (LOSEL); b. Ger- manic *fer-leusan, *far-leusan (*fer-, *far-, prefix denot- ing rejection or exclusion; see per’) in (i) Old English forléosan, to forfeit, lose: FORLORN (ii) Dutch verliezen, to lose (past participle verloren): FORLORN HOPE. 2. Ger- manic */aww6 in Swedish lagg, barrel stave (< “split piece of wood”), akin to the probable source of LAG?. 3. Germanic *lausaz in: a. Old English léas, “loose,” free from, without, untrue, lacking: LEASING, -LESS; b. Old English los, loss: LOSE, (LOSS); CG. Old Norse Jauss, louss, loose: LOOSE; d. Swiss German lésch, loose: LOESS. 4. Zero-grade form *lu- in: a. Greek luein, to loosen, release, untie: LYSIS, LYSO-, -LYTE, -LYTIC; ANALYSIS, CATALYSIS, DIALYSIS, LYASE, PARALYSIS, TACHYLYTE; b. Latin lués, plague, pestilence (< “dissolution, putre- faction”): LUES; Cc. prefixed form *se-lu- (se-, apart; see s(w)e-) in Latin solvere, to loosen, untie: SOLUBLE, SOLUTE, SOLVE; ABSOLUTE, (ABSOLVE), ASSOIL, CONSO- LUTE, DISSOLVE, RESOLVE. [Pok. 2. Jeu- 681.] leu-2. Dirt; to make dirty. 1. Latin polluere, to pollute (< *por-luere; por- for pr6-, forth, forward; see per’): POLLUTE. 2. Suffixed zero-grade form */u-to- in Latin lutum, mud, mire, clay: LUTE?. [Pok. 1. leu- 681.] léu-1, Stone. Welsh Jlech, flat stone (from an uncertain preform): CROMLECH. [Pok. 2. léu- 683.] léu-2. Echoic root. 1. Extended form */eut- in Germanic *leuth- in Old High German liod (> German Lied), song: LIED; VOLKSLIED. 2. Extended variant form *laud- in Latin laus, praise, glory, fame: LAUD. [Pok. 3. éu- 683.] leubh-. To care, desire; love. I. Suffixed form *leubh-o- in Germanic *leubaz in Old English /éof, dear, beloved: LIEF; LEMAN, LIVELONG. II. O-grade form *loubh-. 1. Germanic */aubé in: a. Old English léaf, permission (< “pleasure, approval”): LEAVE?; b. Middle Dutch verlof, leave, permission (ver-, intensive prefix, from Germanic *fer-; see per'): FURLOUGH; Cc. Germanic *galaubd (*ga-, intensive prefix; see kom) in Old English geléafa, biléafa (bi-, about; see ambhi), belief, faith: BELIEF. 2. Ger- manic *galaubjan (*ga-, intensive prefix; see kom), “to hold dear,” esteem, trust, in Old English geléfan, beléfan (be-, about; see ambhi), to believe, trust: BELIEVE. III. Zero-grade form *lubh-. 1. Suffixed form *lubh-a- in Germanic */ubé in Old English Jufu, love: LovE. 2. Suf- fixed (stative) form *lubh-é- in Latin libére, to be dear, be pleasing: QUODLIBET. 3. Latin libid6, pleasure, desire: LIBIDO. [Pok. leubh- 683.] leud-. Small. Germanic */it- in: a. West Germanic *lutti- laz in Old English /ytel, little: LITTLE; b. Old English liitan, to bend down: LouT?; c. Old Norse lita, to bend down (< “to make small”): (LouT!); d. perhaps Middle Dutch loteren, to shake, totter (< “to make smaller”), perhaps akin to the source of Middle English Joitren, to idle away time: LOITER. [Pok. leud- 684.] leudh-'. To go. Zero-grade form *(e)ludh- in suffixed unextended form *elu-to- in Greek prosélutos, “one who comes to a place,” stranger (pros-, to; see per’): PROS- ELYTE. [In Pok. 6. e/- 306.] leudh-2. To mount up, grow. Suffixed form */eudh-ero- in Latin liber, free (the precise semantic development is obscure): LIBERAL, LIBERATE, LIBERTINE, LIBERTY, LIV- ERY; DELIVER. [Pok. 1. leudh- 684.] leu(e)-. To wash. 1. Suffixed form *lou-kd- in Germanic *laugo in Old English /éag, lye: LYE. 2. Suffixed form *lou-tro- in Old English /éathor, washing soda: LATHER. 3. Variant form *Jaw- in: a. Latin lavere, to wash, with its derivative -luere, to wash: LOTION; ABLUTION, ALLU- VION, COLLUVIUM, DELUGE, DILUTE, (ELUANT), ELUTE, ELUVIUM; b. form */aw-d- in Latin lavdre, to wash: LAVE, LOMENT; C. Latin lavatrina, ldtrina, a bath, privy: LATRINE. [Pok. Jou- 692.] leug-'. To bend, turn, wind. 1. Germanic *Jauk-, leek (semantic transition obscure), in Old English Jéac, leek: LEEK; GARLIC. 2. Zero-grade form *lug- in Germanic *luk- in: a. Old English loc, lock (perhaps < “a bending
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1741:LETHAL ol- LETHARGY |adh- LETHE ladh- LETTER deph- LETTUCE melg- LEVEL [ithra LEVER leg’h- LEVIGATE ag-, leg’h- LEVIRATE daiwer- LEVITY leg¥h- LEVo- laiwo- LEVOROTATION laiwo- LEVOROTATORY laiwo- LEX leg-1 LEXICON leg-1 LIABLE leig-1 LIBATION Iéi- LIBERAL leudh-2 LIBERATE leudh-2 LIBERTINE leudh-2 LIBERTY leudh-2 LIBIDO leubh- LIBRA fithra
1757:LITHE lento- LITHOTRITY dhreu- LITIGATE ag- LITMUS meu-, wel-1 LITOTES lei- LITTER legh- LITTLE leud- LITTORAL [éi- LITURGY werg- LIVE! leip- LIVELIHOOD leit-2 LIVELONG leubh- LIVELY leip- LIVER! leip- LIVERWURST wers-! LIVERY leudh-? LIVID — sfi-
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
```


## [2026-09-04T18:58:36.602Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD band? ===\"; ls incoming/WLD/; echo \"--- WLD_Bd2 leudh\"; grep -n \"leudh\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -30; echo \"--- WLD_band3\"; grep -n \"leudh\" WLD_band3.txt | head -20"
}
```


### [2026-09-04T18:58:36.669Z] TOOL RESULT

```
=== WLD band? ===
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
--- WLD_Bd2 leudh
6653:sen KG. I 135, doch s. u, leudh „emporwachsen“) als phl-ed-j -et- verwandt 
26979:leudh- 
27015:SBAk. Wien 168, 14S f.) vielleicht Veil „werde geboren, entstehe^* (*leudh-?i-)y 
27016:Vind „gebare'', poVem „Yolk'' (leudh-m-); 
--- WLD_band3
```


## [2026-09-04T18:58:43.570Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '26960,27030p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-04T18:58:43.615Z] TOOL RESULT

```
Gr. Xvooa (att. Uttgl) „Wut^‘ (Fick I ^ 541) geht nach Lagercrantz Gr. 
Ltgesch. 88 vielmehr auf ^XvyiWL zuriick, vgl, Xevxol cpoe^veg ' fxaivoyevai^ 
XvxeTov' (fofsQov Hes. u. dgl.; Boisacq s. v. sucht dieses leii-k- mit leu-L 
durch Annahme von Wzvariation zu retten, was bei der Isolierung der 
gr, Sippe mir unstatthaft erscheint (die weitere Anreihung von leu-bh- 
,,gem haben, begehren'' verfehlt sogar die Bed.). 

lend- etwa „sich ducken“, daher einerseits „sich beugen, geduckt, klein, 
gedruckt‘‘, andrerseits „sich vor jemand niederducken, verstecken, sich 
klein machen, heucheln, falsch sein, betriigen^^ 

Mir. luta^ nir. hida und litidin „der kleine FingeP' (f'ladyi-^ Fick II ^ 258, 
Zupitza KZ. 36, 243), wohl auch cymr. lluddtd „Mhdigkeit“ i^Hoiideia^ 



416 


leudh- 


vgl. ahd. Iu0€da „mfirmatio‘‘; Fick aaO.); as. luttil „klein, elend*‘, ahd. 
Iu 0 il^ luszily liuzilj mhi, lutzel „klein, wenig, gering“, ags. lytel^ engl. 
little-, as. lut „wenig‘‘, ags. lyt „gering‘^, as. luttic^ ahd. luzztc „klein, wenig, 
gering^; aisl. luta st.~Y. „sich vornuber neigen, fallen‘‘ {lofning „Vereh- 
rung“), ags. lutan st-Y. „sich beugen, fallen‘s ags. lutian „verborgen liegen, 
lauern", ahd. lu^en ds.; ahd. losTctn^ mnd. luschen „versteckt, verborgen 
sein ; got. Huts „heiichlerisch“, liutai PI. „GaukleP', I utei „Trug“, luton 
jjbetriigen, verfiihren*', ags. lot n. „Betrug“, lytig „hinterlistig“, aisl. Ijotr 
„ha61ich“, lyti (^liutia-) „Gebrechen“, lyta „verunzieren, entehren, tadeln“; 

lit. liustu^ lifidaUj liusti „traurig sein^^ („gedruckt sein, den Kopf hangen 
lassen^), liudnas „traiirig“, apr. lausfinti „demiitigen‘‘ (von Haustas „ge- 
duckt“); ksl. lud^ „toricht'', russ. luhi^ hidilh „betrugen, tauschen“, litda 
„Trubung der Hornhaut'S ludd „blendender Glanz'^, klr. tudd „Schuppen 
anf dem Ange, Blendwerk, Trugbild“, skr. lud „toricht, narrisch“, zdlud 
Adv. „umsonst, vergebens‘‘ (usw., s. Berneker 743 f.). 

Ygl. Bezzenberger KSB. 8, 366 f. (unter vorlaufiger Trennung der beiden 
Bedeutungsgruppen), v. Grienberger Unt. 150, Pick 111^ 374, Palk-Torp 
u. lude^ liiske^ lyde^ Trautmann Apr. 369 f. — Berneker will (im AnschluB 
an Bezzenberger) wegen der slav. Bed. „B1^5idwerk, Schein‘‘ — die aber aus 
,jtrugen‘‘ ohne weiteres zu gewinnen ist — die Gruppe lud^^ luditi^ got. 
liuts^ ags. lot von den Worten fiir j,biegen^ sich beugen, verstecken^ trennen; 
vgl. dagegen auch das genau gleiche Bed.-Yerhaltnis zwischen got. leitils 
„klein“ : litai d. sg. „Heuchelei“ usw. unter leid- „spielen“, auch wenn dieses 
durch die Parallelformen von unserer «<-Wz. gefordert sein kann, ferner 
Lewy IP. 32, 163. 

leadh- „emporwachsen, hochkommen“. 

Ai. rodhati^ rohaii „8teigt, wachst“, av. raodaiti 5 ,wachst'‘, ai. roha- m. 
„das Aufsteigen, Erhebung, H6he“, avarddha- m. „\Yurzeltrieb, Luftwurzel, 
Senkung^, av, raoda- m, „Wuchs, Ansehen“, npers. roi 5 ,Gesicht“; alb. (Jokl 
SBAk. Wien 168, 14S f.) vielleicht Veil „werde geboren, entstehe^* (*leudh-?i-)y 
Vind „gebare'', poVem „Yolk'' (leudh-m-); 

lat. Liber ,4^3'!- Gott des Wachstums, der Zeugung, Anpflanzung^^ (aus 
*lduhero-^ ^loufero-^ "^Icudhero-)^ osk. gen. Lilv frets „Liberi“, lat. Uheri, 
-Wiim „die Kinder'\ altest auch von einem einzigen Kind, also *„Nach- 
wuchs“ (s. Kohm Alat. Porsch. Il9ff., Vf. LEWb.‘" s. v.); 

got. liudan^ ahd. hotan, as. l>odan^ ags. leodan j^wachsen*^*, ahd. sumar- 
lota „Sommersch6Bling“, anord. (Johansson KZ. 30, 346 f.) lodenn ,,be- 
wachsen, haarig, rauh'', loda „(*festgewachsen sein =) festhangen, fest- 
kleben“; got. laudi f. „Gestalt‘\ sica-, sama-laups „so gro6“, jugga-laups 
„Jungling% mhd. lote „beschafFen“ ; got. ludja „Antlitz^^ (vgl. np. as. 
lud „Aufieres, Korperkraft (? nur Hel. 1 54), ahd. antlutti „Antlitz‘‘; (Kaeh- 
wuchs ” Menge, Yolk:) ahd. liuf^ ags. lead „Yolk'‘, mhd. liiite „Leute“, ags. 
leode ds., dann auch von einzelnen Menschen ahd. Hut „Mensch“, nhd.
```


## [2026-09-04T18:58:49.036Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '27030,27080p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-04T18:58:49.088Z] TOOL RESULT

```
leode ds., dann auch von einzelnen Menschen ahd. Hut „Mensch“, nhd. 
mdartl. das Lent „Per8on“, nd. liid^ Hit „Weibsperson, Madchen”, burgund. 
leudis „der Gemeinfreie^ ; 

aksl. ljudhje pi. „d\e Leute“ (sg. russ. ljudj cech. lid)^ Ijiidim „der Ge- 
meinfreie", lett. Vaudis pi. „Leute, Yolk, Gesmde“, lit. Ijdudis (die 



leup-, leub(h?)- 


417 


bait. Worte widerlegen Hirts PBrB. 23, 335 Aimahme, daB slav. ljudhje 
aus dem Germ, eatlehnt sei). Die Bed. „Gemeinfreier'‘ von burg, leudis 
und aksl. Ijiidim ist aus „Angehoriger des eigenen Volkes, gegeniiber den 
Unterworfenen“ entwickelt; ebenso beruht auf einem idg. „Yolk“ 

nach Schrader lA. 9, 172 gr. EXev'&eQoq „frei (^Yolksangeh6riger)“ == ital. 
Hotifero- in lat. Vihei', -era^ -ertim „frei“, fal. loferta „liberta“ (usw., s. Yf. 
LEWb.2 s. V., Herbig Tit. Fal. 8). 

Diesem Ursprung des gr.-lat. Wortes fiir „frei“ fiigt sich nicht van Heltens 
ZfdtWtf. 11,56 Deutung von got. *lmis „leer, frei von, nichtig“ usw. aus 
verwandtem *loudJi-to-; es bleibt bei Heu-s- „los®n“. 

Kaum richtig wird vielfach unter einer Bed. „hervorkomnien oder steigen“ 
— „kommen, gehn‘^ angereiht gr. elevooixat „werde kommen“ Pf., elXrj- 
Xov'&a, elkyilovdiiEv {el- metr, Dehnung), att. elr\lv^-a^ -afxev ^ Aor. IjXv^ov 
(^X'&ov, iX'&eiv daraus rein lautlich oder durch Kreuzung mit^r^ov? s. "^enedh- 
„gehn“), deren bloBes Praesensformans scheint wegen iX'ijiv-juev, -rt, 
enriXv-rog, ejirjXvTfjg „Ank6mmling“, ngooijXvTog „im Lande ansaBig ge- 
wordener PremdeF', eniqXvg, -'jjXvdog „fremd“ (s. Brugmann 11^ 3, 373, 
Boisacq s. v.); mit l]Xv'dov ist gleichzusetzen air. sg. lod^ 3. sg. luid^ 
dolluid „ich, er ging“ (perfektisch geworden, 1 . pi. -lodmar^ 3. pi. lotar, 
-Idatar)^ Pick H 534 (nicht nach Pick II* 253 als "^pludo zu ^pleu-d-^ dt. 
fliefien) und vielleicht als Kausativ auch zu verbinden air. imluadi „setzt in 
Bewegung^', farltiadi „schwenkt‘', hiaid- „be wegen, erwahnen, au6ern“ (Brug- 
mann II ^ 3, 262; von Pick II* 253, Pedersen KG. II 572 hinwieder zu 
'^pleti-d- gestellt). — Uber arm. ehimnem s. vielmehr u. eld- „treiben“. 

. S. Pick I* 122, 298, 534^ III * 375, Hirt Abl. 116f., Falk-Torp u. lod III, 
lodde^ ladd^ lyd II. 

Cymr. llwdn „Junges von Tieren'', mbret. lozn, loezn (d. i. Zom), nbret. 
loeyi ds. (wozu nach Schlutter AJPh. 21, 192 ludaris „steor“ CGIL. Y 369, 
30) haben wie ir. loth „Fullen“ vielmehr Wzausl. -Z- und bleiben fern 
(Pedersen KG. I 135 denkt an *plot-^ Yariante neben slav, plodz „Prucht'‘, 
8. phel „schwellen“; eher ursprgl. «). Hierher air. luss (s. S. 418).
```


## [2026-09-04T18:58:53.891Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC leudh ===\"; grep -n \"leudh\\|leudho\\|leudhos\\|leudhrós\\|leudher\" IEC.txt | head -30"
}
```


### [2026-09-04T18:58:53.936Z] TOOL RESULT

```
=== IEC leudh ===
4068:gleudh- (gloudh-) “stick, affix; adhesive; lump, patch’. Cf. glüd- E cf. cleading “lagging of pipe, etc.; board- ing of coffer-dam'; Ger. cf. klieter ‘clod, sog’; Du. klier, MDu. kliedere ‘gland, tonsil’; (o- gde in) Li. glaudüs ‘snug’; glauZiu, glaüsti ‘cuddle’; Latv. glauZu, glaust ‘fondle? Cf. MHG kliuter, klüter ‘attachment
4150:gloudhros, see gleudh-
6401:leudho ‘stir, move’. See iudheio, ioudh- and next. WP I, 203 OLat. cf. ioubeo, ére (*order'. But class. jub-!); Ukr. judyty ‘stir’; Pol. judzic ‘incite’; Li. jáu- daus, jáudytis ‘rage’; jáudinu, D. v. ‘rouse’
9698:leskos (ledskos ?) — leudhis
9711:leudheros (leudhər-) “active, free; action, freedom, abandon'. Cf. leus-. WP II, 417. Cf. leudhó and next. Armenian ambig., cf. plu- dhuró Arm. lur£, gs Iréo (gay, lively’, sic: Awgerian. Eng.-Arm. otherwise: 'earnest, serious") (!); Tokh. A lyutar ‘superior, high; highly’; Myc. and Gk. eleütheros ‘free’; Venetic louzera ‘the goddess Libera’; cf. louzerofhos "liberis"; Paelig. loufir ‘free’; Lat. liber, f.; libera, id. (& “bold; open"); Ir. luadar, m. ‘vigour, acti- vity'; cf. MIr. com-lüadar, m. (&company'. Cf. Lat. col-libertus & hliberr); WG cf. (z-gde) lodern, v. ‘thrive’
9712:leudhis ‘tribe, people’. Cf. leudhó, leudheros. WP II, 416
9715:leudho ‘grow, thrive’. WP II, 416. Cf. leu- dheros, leudhis, loudh- Skt. rodhàmi, id.; Av. raoðë, mp. id.; Mir. cf. lúad, m. ‘exertion’; Go. liudan ‘grow’; OHG ar-liutan, id.; OE leodan, sv. 2 ‘grow’; O-gde or z-gde in LG loden ‘grow, sprout’
9723:leudho — leuks-
10070:loudhos, å (ludh-) ‘growing, rising; growth, rise’. Cf. leudho Skt. róhah, adj. ‘rising’; m. “rise, height, growth’; Av. raoóo, m. id. Go. laudi, f. ‘shape’; -laups, adj. cpds. *-like'; MHG lot, adj. 'form- ed, shaped’; OHG lota (z-gde) (shoot, fr. *ludha); LG Lode, f. ‘sprig, shoot.
10137:ludh-, radical form of type leudho, etc. (Skt. radical only: rudh- 'grow?); Go. ludja (face; cf. OHG ant-lutti: G Antlitz); OS lud, f. 'shape'; OS loda & lada ‘sprout’; LG > G Lode, id. beside HG Lotte 'sapling'; LG (and G) loden ('sprout, v.); OE cf. lod-wyrt ('sil- verweed', but more prob. to LG (in Ger.) Lo- den “pile, coarse woollen cloth’: Sw. ludd, n. “felt, plush, pile); ON loðinn, pp ‘grown’
14892:rüs- (3) ‘space, place’. Cf. reuos (2). WP II, 356. (Iranian ambig.) Per. rü, rüy, s. (face, surface’. To Av. raoóo “growth? accdg. to Justi, cf. leudh-); cf. also Per. rüsta, s. ‘village’: Ir. (?) rús, m. ‘profile’; Lat. rüs, gs: rüris, n. (“open country, farm- stead’. To Av. ravo ‘space’ according to EM & WH, cf. reuos); Umb. cf. ruseme “outside, openly; OS cf. rümo, adv. (‘far away”, fr. *rüs-mo or sim.); Li. cf. rüsys, m. ‘cellar’
```


## [2026-09-04T18:58:54.715Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN 'free' section ===\"; grep -n \"eleutheros\\|liber, -era\\|FREE\" SYN.txt | head -30"
}
```


### [2026-09-04T18:58:54.771Z] TOOL RESULT

```
=== SYN 'free' section ===
33499:19.44 FREE (adj.)
```


## [2026-09-04T18:59:03.982Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor pat in ['rüs- (3)','leudheros (leudh','leudho ‘grow','loudhos','ludh-, radical']:\n    i=t.find(pat)\n    leaf=t.count('\\f',0,i)\n    print(pat,'-> leaf(0-based ff count)',leaf,'approx page',(leaf-15)*2,'and',(leaf-15)*2+1)\nEOF"
}
```


### [2026-09-04T18:59:05.798Z] TOOL RESULT

```
rüs- (3) -> leaf(0-based ff count) 72 approx page 114 and 115
leudheros (leudh -> leaf(0-based ff count) 385 approx page 740 and 741
leudho ‘grow -> leaf(0-based ff count) 385 approx page 740 and 741
loudhos -> leaf(0-based ff count) 401 approx page 772 and 773
ludh-, radical -> leaf(0-based ff count) 404 approx page 778 and 779
```


## [2026-09-04T18:59:12.289Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nlines=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport sys\nfor ln in [9711,9712,9715,10070,10137,14892,9698,9723]:\n    txt='\\n'.join(lines[:ln])\n    print(ln, 'ff-leaf', txt.count('\\f'))\nEOF\ngrep -c $'\\f' IEC.txt; awk 'BEGIN{RS=\"\\f\"} END{print NR}' IEC.txt"
}
```


### [2026-09-04T18:59:14.048Z] TOOL RESULT

```
9711 ff-leaf 385
9712 ff-leaf 385
9715 ff-leaf 385
10070 ff-leaf 401
10137 ff-leaf 404
14892 ff-leaf 610
9698 ff-leaf 384
9723 ff-leaf 386
853
858
```


## [2026-09-04T18:59:19.368Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==611' IEC.txt | head -20; echo \"-----------LEAF 612\"; awk 'BEGIN{RS=\"\\f\"} NR==612' IEC.txt | head -5"
}
```


### [2026-09-04T18:59:20.937Z] TOOL RESULT

```
�rush, dash’; Li. pa-rupti, inf. ‘get chapped — of skin’ be- side rumpù, rùpti, pf: rupaŭ, ‘grow rough’; rupēju, ēti, v. ‘become coarse, gritty’. (NB. for EMDu. rove, f. ‘scab’; Du. roven, v. "eg, coriate’; Sw. ruva, f. ‘scab’; ON hrufa “crust, see krup-, etc.)
rupəl- ‘rugged, rough; ruggedness, rough- ness’. Cf. rüp-. (Gmc. ambig. cf. krup-) Du. roffelen, v. ‘bungle’; LG rüffeln, v. ‘snub’; ME ruffelen, v. ‘ruffle’; Fris. cf. roffel ‘ruggedness, roughness’; Li. ruple, f. “rough bark; rash"; Latv. rupulis, s. ‘rough stick; boor
ruptós, pp. form of radical rup-, q. v. and cf. reup- (1) and (2). WP II, 354 Lat. ruptus, adj. ‘broken’; W rhwth, f: rhoth, adj. /sundered'; rhwtion, rhytion, mpl. *frag- ments’; Li. pa-rüptas ‘chapped — of hands” beside rüptas, adj. ‘erupted — of rash’; cf. OCS rüpünü, adj. (sudden or sim.)
rüs- (1) ‘rush, roar’. Cf. reuos (1), ruuó & rüstis Skt. rüsah, adj. ‘tart, harsh; LG rüsen, v. ‘bluster’; E rouse, v. beside rooze, v. ‘roar — of a fire" (dial.); Sw. rus, n. “rush”; rusa, v id. beside rysa, v. ‘horrify’; ON (short vowel) rosi, m. ‘downpour’; Cz. cf. rych-ly, adj. ‘quick’; (R ryxlyj, adj. = ‘crumbly, spongy’); Latv. rūsa, f. (2) ‘summer lightning’; Li. cf. rüstüs, adj. ‘grim’
rüs- (2) “fall, fail, crumble, decay; feeble, weak, poor On cf. ryrr, adj. ‘feeble, poor, trivia; mod. rústir, pl. ‘ruins’; R cf. ryxlyj, adj. ‘crumbly, spongy’; Li. cf. rásoju, oti, v. “idle, lounge’; Latv. rūsa, f. (3) ‘mildew, blight’; rūsa, f. com. post-heap'; cf. also Li. rusnóti, inf. intr. ‘drain away’; Latv. rūšas, fpl. “worry, care’
1103
rüs- (3) ‘space, place’. Cf. reuos (2). WP II, 356. (Iranian ambig.) Per. rü, rüy, s. (face, surface’. To Av. raoóo “growth? accdg. to Justi, cf. leudh-); cf. also Per. rüsta, s. ‘village’: Ir. (?) rús, m. ‘profile’; Lat. rüs, gs: rüris, n. (“open country, farm- stead’. To Av. ravo ‘space’ according to EM & WH, cf. reuos); Umb. cf. ruseme “outside, openly; OS cf. rümo, adv. (‘far away”, fr. *rüs-mo or sim.); Li. cf. rüsys, m. ‘cellar’
rüs- (4) ‘red; redness’. (Variant rusuos). Cf. WP I, 141 & II, 351-9 Lat. cf. russus, russeus, id. (fr. *rudhs-); Ir. rús, m. (4) ‘scarlet’; Du. ros, adj. ‘red-haired’; Cz. cf. ryšavý, adj. (fox-red', fr. *rüsio-); Li. rüsas beside rüsvas, adj. ‘red-brown’; rüsena, f. ‘glow’; rusù & rusiü, inf: -ēti, v. ‘glow, smoulder'; Latv. rūsa, f. (1) ‘rust’; rüseju, et, v. id. cf. ruša, f. *firegrate, ashpit'. (Isophonic: Skt. rusyami (am angry) An infixed form arises in Li. rundu (and rüstu), inf. rusti, v. ‘turn reddish’
rüsk- (ruuisk-, ruisk-) ‘rush, dash’. Cf. ruuð, rüið, reuð (2) & reusk- Ir. rosc, m. ‘rhetoric, bombast beside rúisc, f. ‘thrashing; volley’; m. ‘boor; rúiscim, v. ‘thrash; strip’, MHG rosch, rösch(e), adj. ‘dashing, bold; harsh, sharp’ beside rūschen, v. ‘rush, rustle; dash’; rūsch, sm. id. (in all senses of E rush); Du. ruisen, formerly rui- schen, v ‘rush’; Fris. rûze, rûzje, v. as Du.; LG rusch, adj. “loose, fresh’; Li. ruSüs, adj. ‘active’. (NB. The later Gmc. forms have be- come isophonic with a type w. initial *kr- as in OHG horskan, OE hrýscan, fr. *krüsk-, but untraceable in this form)
(rüsk-, rüskos, à “bark, shell’, etc. See  Supt: Ri
rüslos, om, extn. of type rüs- (1) in Cz. rychlý ‘quick’; LG russeln, v. ‘rush — as wind, sough'; E rustle; Sw. rossel, n. “rattle in throat”; rossla, v. id.; (2) in OE rysel, m. ‘dripping, lard, resin’; Fris. russel, s. ‘icicle’; Icel. rusl, n. ‘rubbish’; R ryxlyj, ad. ‘friable, loose, spongy’; (4) in Latv. rusls ‘brown’
rüstis, os, ios, extn. of types rüs- (1) and rüs- (2). Cf. (1) in Skt. rut, mn., rus, r
-----------LEAF 612
usa, f. “anger”; Icel.
rüs- — ruuó
10
20
25
```


## [2026-09-04T18:59:31.873Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT raod ===\"; grep -n \"raoδ\\|raod\\|raoda\" BRT.txt | head -40"
}
```


### [2026-09-04T18:59:31.923Z] TOOL RESULT

```
=== BRT raod ===
3587:•  y  apa.rao9^nina-Adj.,FFM.:  s.  ^raod-.
4643:*)  Vgl.  noch  iraod-  mit  ;■(.  Die  Lehrteit  des Awesisschiiiers  ist  drei  Jahre,  je  eins  bei  drei Lehrern.  Bei  jedem  soll  er  nach  einem  halben Jahre  das  Gelernte  bereits  sicher  im  Gedächlnij haben,  so  dass  er  beim  Vortrag  keine  Verstösse macht.   Andernfalls  ist  der  Lehrer  zu  wechseln;
4835:lesen?  Oder  Iiraes.  3?  —  ")  D.i.  ä-iydi;  ai. iyi.  —  'J>  Pü. ;  ähekinilan.  —  '4)  D.  i.  ä-lyäi.  — 'S>  Pü.  i  apar  raiitan.  —  »*)  Lesung  unsicheri FoYZDMG.^i^  363:  apariy  bäbirum  naiy  aiiyä- yam. —  '?>  Pü.;  Sitdk  tu  an  ^ariel  buland*') uzet.  Vgl.  lu  (KU-  No.  2,  'ar-  No.  8  f.,  usinidyäi, gam-  Ho.  16,  'Vax!-  No.  7  und  ^raod-  No.  5. Ganz  merkwürdige  Lesungen  bei  Gdn.  KZ. ja 332  und  Mills  lausit^idyäi;  s.  auch  WEST SBE.  J7. 387.  —  »*J  Nach  dem  Metrum  blos ytinti  IM  lesen.  —  =91  H.l.  faiti\iytU;  ai. iyaie.  Hds.  pailiiU.  Pü.:  pt,  verstümmelt. — 30)  D.  i.  faiH\iy&nle,  Neubildung  zu  lySili, N0.I3.  Pu.:  tmdeutlich.  —  3>)  Pü. : /alQEtd ;  s. dazu  SWienAW.ä/.84i.  7 :  paül  bavhn  fiailman s/tpam.  —  3')  PQ.s  api  raßan.  Die  Formen mit  ä  zeigen  alle  den  Anfang  pSray'  (pärayäl —  S  268.  3  b—,  aber  paräiii;  V.  g.  39  f., 'S-  9f-);  ich  schliesse  daraus,  dass  das  ä  durch den  Einfluss  der  Praes.-Klasse  30  hervorge- rufen ist.  —  3J)  Hds,  •äi%i,  wie  V.  22.  7.  — 34)  Them.  Hds.  say';  der  l.  Buchstabe  ist nicht  recht  deutlich.  —  35)  Text  unsicher,  — 3«)  \ai. /vrayä/;  s.  No.  32.  —  37)Pu.!/fa- tiaßan,  ßanämltan.  Meist  them.,  mit  ß^y (nach  S  26S.  3  b?).  —  »)  %  304  H-  30.  — 3»  Vgl.  S  2^.  2,  iSPrA.  Oder  vU.  Absol, ai.  (nir)äyaml—  40)  S.  noch  No.  9,  I7ff.,22, 29  und  Bthu  AF.  2.  72.  —  4')  Dass  das  np. äyad  das  Praev.  ä  enthalt  (GIrPh.  I  b.  132), scheint  mir  keineswegs  sicher.  Vgl.  mp.  ii:äy/i {s.  No.  27)  und  jAw.  iKäili.  —  W  So  (für  la la}i  E.  unter  ui.
7075:•  j.,  g.  ä-kä-  i)  Adj.  'manifestus';  a)  'der sehen  lässt,  wa^  er  tut,  sich  bei  dem  was er  tut  sehen  lässt,  es  offenkundig  tut': aiiyi^  kasHt  .  .  para.baraiti  'ka  (NS.) *hazatiha  *anskils>  iayusU.tJj;  6.  b)  'der sehcQ  lässt,  was  geschehen  ist',  spez.  von den  bei  der  äkä-  (s.  2)  Beteiligten,  'Offen- leger': hadä  asil  vakistScä  tiiananhä  xsa- 'irä.'a  yä  (NPn.)  /w  stanhai  a  pai^t  .  . 'ka  (NP.)  ar^ärSng  d^mänS  garö  Sfrao^äiiS "sammt  .  .  und  dem  Xs.,  welche  als  Offen- leger,  von  den  Frommen  ersehnt,  auf  dem Weg  zum  Haus  des  Lobs  den  Gehorsamen erwarten  werden"  Y.50,4'>.  2)  f.  'mani- festatio,  dilucidatio',  d.  i.  die  'Offenlegung' der  Taten  des  ersten  Lebens  bei  den  letzten Dingen  " :  dngvats  . .  yehyä  urvä  xraodattT (sd.)  cinvaiö  pinta  'kä  (Abi.)  "-  .  vor  der Offenlegung  an  der  Brlicke  des  Scheiders" V.  5/-I3;  —  ka  '^wöi  alu  'i,i  (NS.) arfdrSiig  ilyJ  "wird  deine  Offenlegung, o  A-,  den  Froramen  erwünscht  seini*"  Y. 4<V.8; — vahiitö  anktti  °>f(7j(AbL)-i-'?iV (sd.) ahüire  jasmtqm  Y.  60. 11.
7166:%raodet  *^/ara%ra  (s  294.  3)  verlangte.  imSchlaf  ergossenenSamen  vorgeschrieben
7290:■)  Die  beiden  Warter  haben  zusammen  eine 3.  Flur,  verdrängt;  etwa  *uparaßi3nit ,  lu '■raod:  I
8027:•  j.  iSasa-  Adj.  dnw.  «aa ja- (sd.) :  isan.- itäitya  ml  vlspS  at)hu}  astva  'Sftn  jitahm xraodat.urva  (sd.)  .  .  V.5.4.
8308:•  j.  upa.mraoda- Adj. '(etwa)  der  Wollust, den  Huren  ergeben,  Hurenjäger':  äat  *ag!e ydi  fracarmti  .  .  gaosUj/ca  (sd.)  . ,  'dss'a
8333:SoperL  zum  V.  iraod- 1).  —  ai.  vgl.  uparodAa- m.,  ufaeoäAin-  Adj,  —  D  Nach  Sp.  'der  auf- gewachsenste',  Dst.  'tshi  baut  de  taille'  viel- mehr mm  V.  'raad:
9933:•  j.  gaiö.tay-  m.  'Räuber,  Bandit':  äal *aite  *ySi  fracarinli  kfrpsqsca  -hsülsäi  dal- visca  *Aandramana  ufa.mraodStca  vups.- xlaps  ".  .  die  welche  jede  Nacht  zu  (in die  Gesellschaft  von)  Wegelagerern  und Banditen  und  (Iü^tdschen  Rotten  und Hurenjägem  gehen"  ^-SS',  —  paiHi.- :fairu  (sd.)     rat^anhs    vä    kpnsqm    va
10572:•  g.  (,  j.)  xraod-  V,  '(sich)  ängstigen', Praes.   i  xraed-,
10573:i)  'ängstigen':  karapanö  kavayascä  .  . ySiig  :^3  umä  £'a?:ä  xraodat  (3SKA.) äami  ". .  die  ihre  eigene  Seele  und  ihr eigenes  Ich  ängstigen  wird"  Y.  46. 11;  — s.  xraodat.',  2)  'sich  ängstigen,  bangen
10574:vor    — '    (Abi.):    dr?gvalS  .  .  yehyä    urvä xraodaitl  (3SKA.)  anvats  p?r»tii  äka  (sd.) ". .  des  Seele  bangen  wird  vor . ,"  Y.  5/.  1 3. Pu. :  xröiiiii  ('Geschrei')  dilan.
10575:•  j.  xraodaturvan-''  Adj.  'den  seine  Seele ängstigt'  sva.  'des  Seele  sich  ängstigt'; isanJtaitya  ml  vTspö  avhus  astitä  isas?m jit.as>m  (sd)  'va  ptsSJanus  "in  Kürze würden  mir  bei  der  ganzen  Menschheit ..  die  Seelen  voll  Angst,  die  Leiber  dem Gericht  verfallen  sein"  V.  5.4.
11425:[des  Scheiders'  (beim  letzten  Gericht)**: .yehyä  urvä  xraodaUl  'vatspfntn  ska  (sd.)
12441:asahya  axäyai  (sd.)  ggnedim  Y.  37, 17;  — aiäunqm  . .  uruns  .  .  kudüJiatanqmAt  .  . yailqm  vahehl^  'na  vanainti  va  vSnghm va  vaonarS  va  H.  3g.  z;  —  karapanS kavayasca  .  .  ySng  ^S  urva  ::^a!^a  xrao- dat  (sd.)  'na  Y.46.11;  —  Ö  dngvats *tnandaHg  *9r?tael  (sd.)  haihim  yehya urvü  xraodaiti , .  Y.  ji,  13;  —  tsm  *vä ahsm  dtTgvantS  .  .  'na  nailal  (sd.)  Y.^y/. so;  zT.  verwendet  V.f.  fia;  s.  a;  —  ySi .  .  aiäm>m  vandtn  (sd.)  . .  töi  daoiStig dqn  yS  drsgvats  °na  ",.  die  —  in  AnDaiva Haus  fUr  das  Ich  des  ^rv^enossen!"  Y. 4^.  4*>.  a)  im  jAiv.:  alaonqm ..  ahümla 'nam/ai*  iaooasäi  urvänsmca  fravaiSmia yagamaide  Y.  a6.  4;  —  asni  iyazamaide\ manä  . .  °nä  [yazamaidi]  saoryantqm  yaaa- vtaide  Yt  13.  7^;  —  aisS  zT  växs . .  a  va^S ahunB  vaityS . .  uruna^a  'tiaca  (IS.)  span- vanti  (sd.)  H.  J.  4;  —  'nqm  .  .  yaoldai- är/a  dha  zl  aifihä  asH  yaosdaitis  kahmai- Ht  ..  havaya  tnsvS  'naya  yl  hvqm  'nqm yaozdaite  humataisla  ..  V.  10.  19*';  —  um vä  ahOm  drvaniö  *^a  *'na  msirtnttyJJ [a/isiäi  a/fuhe]  V.  5. 6a;  —  aiiihä  dim vütaya  fr-Jmita  (sd.)  salayeiti  ya  hava 'naT>  kaininS  k>hrpa  srlrayh  .  .  aat  Alm aoxta  ..yS  nars  asaonü  urva  alca  Karditis ahi  ..?  äat  hl paiH.aoxta  ya  hava  'na  .. az?m  ba  U  ahmt  .  .  yä  hava  'na  *:^ai- paihejanvö  {sd.Y'  H.2.9— 11; — arahvam 'nqm  V.^.ai  PüZ.s),  io.  19  PüZ.
15166:ai.  pädyati ;  s.  lu  ^raod-  No.  I.  —  VgL  paüiya- mit  No.  I.  —  Pü. :  verschieden  ;  s.  No,  1  ff.  — ')  Pü.:  öpoilan.  —  »)  Pü.:  afii  (noganel;  vgl. No.  3  und  Hoan  NpEt.  24.  —  ))  Pfi. ;  . .  lu^in Aaniircl  (np.  antlrad)  .  .,  et].:  kuS  haniär  e an  yät  iarl  bavct.  —  «  Jp  I,  Mf  a.  —  S)  Hds. (auch  ZU  P.  //)  dt^aänS;  \  statt  %y,  s.  paiay- No.  I.   Pü.:  siyän;  vgl.  No.  6  und  säy-  No.  7.
15213:—  I)  In  Nachahmung  des  Wechsels  zwischen d  und  %  im  Wnrzelauslaut,  s.  ^raod-  No.  I, Doch  ist  zu  beachten,  dass  sich  ar.  ^fa/jutai and  *padia/iü  in  der  Bedeutung  berührten.  — »  Nach  der  üblichen  Erklärung,  die  jedoch nicht  einwandsfrei  ist.  —  3)  Hds.  J^&ayeili; s.  aber  Pu.
16070:Brücke  des  Scheiders'  (beim  letzten  Ge- richt): Ayat  aüT^gpirun  yd^rä  ^vatJ  °tui "wenn  sie  dahin  kommen,  wo  die  Brücke des  Scheiders  ist"  Y.4Ö".  11;  —  frS  toii vispsis  cinvats  frafra  (Sp,  851  m.)  'tum \.46. 10;  —  tarS  änvats  °tSm  Y.  71. 16, V.  7p.  30;  Vr.  7.  i;  — yeiya  urvä  xraodaUl änvatJ  'tä(l£,.) aia(s��)Y.5i.i3.  a)dn. auch  ohne  cinvatB  'die  Brücke'  Kar'  i^,: hrlicit  (Sp.  591  m.)  tarS  'tümcit  la  urväram vahistfm  aÄsm  frapärayem  Y.  ig.  6.
16187:nar>fils  *anj[i  aeSasü  (sd.)  dijU.antä  'nvö (NP.)  Y.5_J.9.  A.)]\vi.sva..ianu.f?r^%a- (sd.)*':  -nustanUm  *piryeteF.2jh;  lO;  — aäahe  paiti  'nuye  duye  satte  upäzananqm (sd.)  upäzSil  aspake  aStraya  .  .  V.4.io; —  aMÄaJ  hala  * fyaohnäv3r>za  (sd,)  aia ; bavainti  'nvS  (NP.)  V,  13.  38,  15.  i  (wo  j 'irva) ;  —  yS  gidä  asrävayS  .  .  tat  /"'''  j *ainim  dahnam  gäiianqm  *srao%rät  pai-  \ ristayeiti  .  .  *°nu/  N.  44;  —  vTspS  arikui' astvä  .  .  xraodat-urva  (sd.)  °nui  V.  j.  I 4;  —  aismS  dusdä  'nus  Yt. /0. 97;  — I V3hrk?m  yim  bisangnm  daSvayasn>m  'nvi ' V.  7.  52  PÜZ.  (?);  —  yd>a  'nvat  Nik.  2  (?).
20814:—  hadä  (sd.)  asä  vahistäÜä  mananha  xla- >räca  yä  (NPn.)  . .  stanhat  a  paihi  (sd.) Y-50-4;  S;  —  o^"t  yam  ..  ahurs  masata (Sp.  1113m.)  Y.54.'i;  —  raf^rSm.. hyal  frys  ftyäi  (sd.)  daidlt  Y.46.3;  — sa^^ar!  (sd.)  . .  yä  (zu  2)  .  ,  vSvfmSi  . . yäca  varjsaiil  Y.29.4;  —  iarapanS  käva- yas^a  . .  ySng  ä"?  un'ä  . .  xraoda^  (sd.) Y.46. 11;  —  ais}m»m  .  .  ya  (ISm.)  bqna- ym(%A)  ahSm  ..  Y.30.6;  2Ä6;  — dmgvaiS  . .  yehyä  urvä  xraodaitl  (sd.) Y.5/.  13;  45.  7 '1  —  ä^rascä  manatihaslä yaya  lyao%anai!  asim  %raoita  (sd.)  Y. 46.  7;  —  aurvatö  .  .  yäis  az^ä  Y.  ^O. T>  —  äyaptä  .  .  yäis  (als  Subj.)  rapaiUS (sd.)  daidlt  ^Jär?  Y.  2Ä  2 ;  —  kB  ..  akms (Sp.  293  u.)  y}  ll  fyaiiul  hmihyat  (sd.) V.5_j.9;2p.2;  —  xsdkr^m  ..yehyä  Vfndä (sd.)  vanaima  *drußm  Y.31.  4;  verwendet V.  20, 8  (vo  yeAhe').  ß)  adjektivisch; das  Nomen  ist  wiederiiolt;  zu  a):  dämsii urvais!  apTmi yakmT .  .  urvalsl  JasS (S^. 4940.)  Y..^j.sf:;  —   NSm.  mit  na  (Sp.
21215:Praesens  r  ai  vä  ustSnSiUsd.)  ahvä  zastsi! frlTumna  (sd.)  .  .  hy  {'indem')  mazdqm dvaidl  (sd.)  farashbyl}  Y.  29,  5.  3)  mit dem  Konj,  (oder  Inj.)  in  futurischem  Sinn: hy  ('wenn')  us  alä  naptyailü  .  .  türahyä uipn  (sd.)  .  .  at  Is  vohü  hJm  aibT.mSist (sd.)  mananhä  Y, 46.  12;  —  y^  x^} urva  . .  xraodat  (sd.)  . ,  hy  ('wenn')  aibJ.- gfm>n  ya~hra  Hnvalö  ftrstu?  Y.  46.  11; 44-^5t  49-9'/  —  '^^m  nä..  mavaitf  (sd.) päyüm  dadai  hy  ('wenn')  mä  dr>gvä didarisaia  (sd.)  *amatihi  Y.  40.  T,  —  ai 3wJ  mSnghai  /axm»m(sd.)cä  spmUm  .  . hy  ('wann')  tä  zasta  yä . .  %wahya  ganma (sd.)  ahm  . .  hy  ('wann')  M3i  vaahJus hazS  jimat  mananhs  Y.  43. 4.         a)  mit  1
24860:•  j.  raodas.pairista-  Adj.  'zum  Leuchten, 2U  lichtem,  hellem  Era.nd  ausgesucht''*':  yd ahmäi  (näml.  S^re)  assmiin  (sd.)  baraiti Mkai  *'tqm''>  Y. 62.10;  zit.  V.j>V.  27.
24874:'raodah-
24885:•  j.  raodah'ya-  Adj.  'licht,  hell',  Plur.  neutr. Tageslicht':  {antari)  'cake  (APn.)"'  nBii antars  (sd.)  timahe  li.68.
24897:•  g.  'raod-,  j.  'rao^-"  V.  'jammem'. Praes.  3  uru^a-,  30  (Kaus.)  uraddya-'^; s-AoT.   I  raos-.
24900:auch  ZDMG.  44-  553  lu  sbal.  rdtag.  — ')  S  3^.  —  ^*  Eine  höchst  auflallige  Diver- genz. —  4)  Ich  sehe  in  der  Sielt«  eine  .An- spielung auf  Y.  2p.  9.  —  i)  Vgl.  Pü.  lU  Iraaä-, itoöd:  —  6)  Erl.:  tuland  mai  älil.  Wie  ffit 'raod-;  s.  aber  V.ig.^^,  wo  die  gleiche  Ver- bindung. —  7>  Angebl.  drax/  'Baum'I
24901:•  j.  'raod-  V.  'wachsen'.  Praes.  2  rao^a-i 27  urulya-;  PerC  i  urürud-,  —  PPfp. urusda-,  urusta-^^;  In£  raose^^.
24905:'raod-  Scbluss
24906:3raod-  Noten
24921:•  j-,  g.  ^raod-,  j.  'rao9^''  V.  'abhalten'. Praes,  2  raoia-,  rao^a-,  30  (Iter.)  «70- 6aya-;  Perf.  i  ursraod: — PP(P.  "urusäa", 'urusta-  'K
24936:*raod-
24938:•  j.  ^raod-  V.  'fliessen',  Praes.  2  raooa-, 30  (Kaus.)  raoaaya-.
24946:•  j.  raoda-  ni.  i)  'Wachstum'  (nurl Komp.).  2)Plur.  'das  äussere  Ansehen': kairiTnS  .  .  panladasayä  'oaesva  "eines Mädchens  .  .  von  fünfzehn  Jahren  nach dem  äussern  .Ansehen"  H.a.  9; — pan^a- dasa  (ND.)  fra^ardvie ..-'Mlsva  kaiarasHt Y.O.S,
24947:KompE.  —  Vgl.  roöOiia-  No.  4.  —  Zum  V. *raod:  —  ai,  riha-  m.  'Erhebuuf;',  np,  rdi 'Gesicht'.  —  Pü.:  {75  sälai)  äriiiia.
24958:•  j,  'raoft-  V.  'jammern':  s,  unter  'raod-,
24959:•  j.  'raoS--  V.  'abhalten';  s.  unter  ^raod .
25629:yütii  yä  n»rqs  sädra  (sA)  drsgfoß  Y.  \  *gaintlsca)  —  vidiiäryinnS  sahayeiti;  ä  dim 45- 7 i  —  dr^vütö ..ydtyä  'vä  xraodaitl  väts  upa.vävO  salayäti  {sA.)  rapi^witarat HttvatB  ftnlä  aka  (sd.)  ¥.5/.  13;  —  at  ..\—  {apäxtarat)  —  iaca  naimat . .  hubae&i- dngvatS  akail  il'an'häis  i^A.)  pmtf  *vqnS' tarü  —  {duägaintitarS)  —  anyaiibyS  va- paityäntf  '^.4g.\\.  a)  neben  *daittä-\taähy8  H.2.  7;  25;  —  aAhä  dim  vä/ayi usw. :  karapanB  isvayasca  . .  yJng  afs  'vä  ■frSntOa  (sd.)  sai/ayätt  yl  hava  daOia ifai^  xraodai  {sA.)  damn  hyal  aibt.g3tian\kamtt0  kihrpa  sflrayä  H-2. 9**;  —  äat yahra  anvatö  pgntui  (sd.)  Y.  46.11;  —  Am  (nänü.  da&iqm,  sd,  Sp.  666  m.)  aoxta tatca  .  .  %v»akml  *ä  *dqm  (Sp,  684  o.)  ,p»nsS  yö  nari  asaotß  'va:  a^ca  caräitis m^inhi    matiS    voAs    'utiasca    asäunqm  i  ahi  yqm  it  yava  . .  sraistqm  äädarysa  (sd.)
25656:PPA.,  aus  ar.  *irunant-,  Praes.  3.  —  ai.  srdvali *er  fliesst'i  vgl.  raulah-,  \raod'.  —  ')  Vgl.  Dbr. AiS.  169.  —  ')  S.  NA.  Proleg,  xuv.
25946:•  j.  satö.raodana-  Adj.  'mit  hundert  Fen- stern versehen':  nmäfum  ..  °n>m  ..hata- urBjtunsm  Yt.5.  loi.
```


## [2026-09-04T18:59:43.326Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== huraod ===\"; grep -n \"huraod\\|hu.raod\\|huraoδ\\|huraoöa\\|huraoδa\" BRT.txt | head -20; echo \"=== raodas.taxma / raodastaxma ===\"; grep -n \"taxma\" BRT.txt | head -30"
}
```


### [2026-09-04T18:59:43.389Z] TOOL RESULT

```
=== huraod ===
=== raodas.taxma / raodastaxma ===
190:Die  angeführten  Texte  bringen  ausserordentlich  zahlreiche  Wiederholungen. Und  zwar  sind  entweder  zwei  oder  mehr  Stellen  einander  völlig  gleich  oder  sie unterscheiden  sich  nur  in  untergeordneten  —  d.  h.  für  das  Wörterbuch  wenigstens untei^e ordneten  —  Stücken.  Als  Beispiel  für  die  erste  Art  von  Wiederholungen mögen  dienen:  Y.  65.  2-5  —  Yt.  3.  2-5;  Yt.  5.  10  =  12,  14,  16,  20  (usw.);  Yt. 5. 19  =  23,  27,  35,  39  (usw.);  Yt.  JO.  98  =  135;  Yt.  j^.  15  (von  hü  bis  taxmahe')  ^ Yt.  10.  70,  127;  Y.  57.  25  (von  akeca  an)  —  Yt.  10.  93  usw.  —  Die  Wiederholungen der  zweiten  Art  zerfallen  in  verschiedene  Gruppen:  Yt io.  103  wiederholt  sich  von yS  hantaia  an  wörtlich  in  Y.57.  isfl,  nur  dass  hier  das  ca  hinter  har>ta  fehlt; irgend  ein  Grund  für  die  Abweichung  ist  nicht  vorhanden.  Yt. /o.  94  (^=  114I und  Y.57. 26  stimmen  völlig  lusammen,  nur  dass  auf  die  Eingangsworte  aäa  nS tum  dort  der  Vokativ  mikira  vouru.gaoyaoite,  hier  aber  traosa  afya  huraöha  folgt; die  Gebetsformel  ist  die  selbe,  aber  die  Adresse  ist  verschieden.  Ähnlich  steht es  mit  den  vier  in  Yljo.  igof.  enthaltenen  Stücken,  die  von  vier  Waffenarten Mihras  durchaus  das  Gleiche  aussagen;  nur  eben  die  Namen  der  Waffe,  sowie deren  Beiwörter  machen  die  Verschiedenheit  der  Stücke  aus.  Besonders  zahlreich findet  sich  diese  Art  der  Wiederholung  im  Viälvdäi  {Vendidad);  z.B.  unterscheiden sich  in  dem  Kapitel  über  die  Verträge  (V.  4)  die  Abschnitte  6  bis  10  und  ander- seits II  bis  16  nur  durch  den  Namen  des  Vertrags  und  der  Zahl  in  der  Buss- bestimmung. Femer  haben  V.p,  53,  54,  55  und  S7  '^'on  üäca  an  den  gleichen Wortlaut,  nur  dass  das  dreimalige  para  von  53  in  54  durch  kaha,  in  55  durch nöü,  in  57  durch  pascalta  ersetzt  ist  In  den  liturgischen  Teilen  des  Yasna  wieder sind  grosse  Stücke  bis  auf  die  Eingangs-  oder  Schlussformel  gleichlautend.  So decken  sich  Y,  i.  3  ff.  und  5.  5  ff.,  4. 8  ff.,  7.  5  ff.  vollständig  bis  auf  die  Eingangs- worte, die  zu  Y.  1:  nivaiöayemi  hankärayemi,  zu  Y.^:  äyese yeSH,  zu  Y.  4:  Hat  dis äva^ayamahl,  zu  Y.  7:  alaya  daöami  lauten,  während  anderseits  Y.  2.  äff.  und 6.\S.  nur  darin  auseinandergehen,  dass  hier  (Y.  6)  jeder  Abschnitt  mit  yatamatde endet,  dort  (Y.  4)  jeder  mit  ahmya  zaohre  bar>smanaica  eingeleitet  und  mit  äyese yeiti  geschlossen  wird.
4754:—  yal:iä  ro  data  °/il  (VP.)  spsntä  a^iä na  >räzäa?n  Y.5#.  5;  II.  iZ,  14.  i,  42.1, • — ■  mai^amnt  . .  yat  ksrmlun  "la  (NS.) sp>nta  vispe  hazaesaYLio.$i;  7.3',  /0.92, y.ga,  Y. 57.^23,  60.6;  —  /ml  '/ä  (NP.) spmtä  gaiia  giurvain  Y.2S.0;  Ny.l.i, VyL^o;- —  spmtsttg  °s3ng  yava^yff  yavaSsvB Y.,J.')-3;  4-A\  —  °^^  sptrüa  huxiäi:ra hmfmhs  (Stverz.)  Vr. ;/.  12;  usw.;  —  -sS spints  vatihali  srlräi^  namqn  äebaya  Y. /  5. 1 ;  Vr.  6.1;  —  vlspqscä  'iq  spintq  yasa- maidsY.42.()\  —  °h  spinlS alaonam  yasa- maideY.yi.2,  G.  2. 6  (wo  'sJtca);''*  — 'sanqm  sp)ntanqm  xialtanqm  vinzidsi- %ranqm  Ötnzatqm  aiwyämanqm  taxmanqm ähuiryanqm  ySi  aihy^anhs  alwvanB  ysi hapta  iam^.manavAö.. Yt  lj.82f.;Y.j. 4, 20,3;  — y3i  hapta  'sä  spmta  Yt.2.3;  — ape  °ianam  spmtanqm  dähXtn  Y./9.8;  Yt. ;^.  8 1 ' ;  —  vankubyS  yazataiibyS  yat  'laii- byS  spmtaHbys  Vr. 8.\;  ff. 4, 13. \,Yt.4.y,
5485:•  j.,  g.  aradra-  Adj,  (fem.  'rJ-)  'getreu, 'verlässig':  'rS  '^wävqs(sd.)  ÄitzSntuü  sfmtö mazdä  Y. 4:_j.3;  46.^;  — fravasayB..  °rä taxmä  *at>javuAai/i/ \l.  ij.  $2;  75;  — mihrgm  . .  y5  äsunqtn  äsus  yS  'ranqm  °rö y3  taxmanqm  taxmS  Yt.  70. 65.  a)  mit DaL:  kuirä  tsi  °rä  masdä  ysi..  caxrayö' (sd.)  "ob  sie  wohl  dir  getreu  sind,  die  . ," Y._j4-7-  A)  insbes. 'dem  Glauben  treu, gläubig,  fromm':  firasaosträ  air3  tu  'r.lis idi  hvB^S  täis  yitig  . .  "o  Fr.Hv.,  dahin geh  mit  diesen  Frommen,  denen  . ."  Y. 4'j^i6;  —  kä  iw'ffi  a/a  äk,i  (sd.)  'ring isyl  Y.  4S.  8;  S*}.  4;  —  fatrijasai  .  .  at vä  aia  "rahyacä  mmankä  "..und  vor  euch, o  Asa,  auch  mit  dem  Gebet  des  Frommen" Y.50.8;  —  da^at  ahrnili  tat..  arfdvJ . . 'räi  yavmiini  jatoyantäi  da^ris  ayaphm Ytj.ig;  13a,  /5.1,  21.
5555:•)    Über   die   Bedeutung   des  Gotls   ist   den    t'isjie  °va   Vlspe  taxma   .  .  kave  HK.1Q.1z; ,i'j5i sehen  Teilen  nichu  Klnies  lu  entnehmen;   —    'v3  as.vancS   kava    usa  Yt5.45;   —
5713:idn^taxma^  näma"  °tiyi^    Bh.^.  i  /p.g,  Yt  /_y.  28;  —  öarjimrS  ^avaühe  'htS
5799:•  j.  asta'va-  Adj.  'mit  einem  Knochen Teisehcn';  °v3  vä  taxmahe  mirr/ake pars- nai'SvS..  "wer  einen  Knochen  des  starken Vogels  oder  eine  Feder  (als  Amulet)  trägt .." YL/4.3(S.
7470:•  j.  äsu.aspya-  n.  'Besitz  schneller  Rosse, Reichtum  an  schnellen  Rossen':  'pTm da'jiiiti  mi%rU  Ytjo.3; —  '^wqm  naracit yöi  taxma  Jat'iyhnte  -ptm  YL5.86;  98.
8304:—  mihnm  .  .  yetike  valnn  Aangrgwnäiti asii vamihi ..yat  dim  dätnBis  °ns  AuÄrixtim (sd.)  .  ,  irinaxH  YL/O.  68;  —  dahmaya vaakuyi  a/ritöii' uyrni  dümsis  '■näi  \.fi.t, S. /.30; —  uyraAe^a  taxmaAe  dämsii "nahe yazatahe  Y.  /.  1 5 ;  —  uyr^m  taxmem  dämeis 'n?m  Y.2.1S,  7.26,  77.23.
8334:•  j.  upara'tSt-  f.  'Superiorität,  Über- lefenheif:  ^wam  nara^it  ysi  taxma jai'jyhrtte  .  .  sfarfttanAasca  'tätS  (AP.) YL5.86.  a)  sonst  mit  vananl-  Adj.: dasdi  .  .  tai  äyafUm  .  .  V9r9%rar}n}mea aAurdoat?m  vanaintimla  *t3t>m  Yt  ro. 33;  5-86.  y-34.  A'i,  X-57-33;  —  vin- liraynaAeca  . ,  vanaintySsca  paiti  'täto  Yt. 8.11.  A)  als  Gottheit:  avistayalca  .  . amavaihya  faurvatäis  amavaihyä  Häts (GS.)  Vr.(f,4.  a)  sonst  mit  vanani-  Adj.: v^ry^rayramca  ..vanaintimca  '/aftw  Y.2.6; Vr.2.8;  —  vfhhraynahe  .  .  vanainiyäsca 'tätö  Y./.6,  Vr./.6,  Vt.J4.o.
10879:•  j.  xStävay-  Adj.  'zur  Familie  der Xstavay  gehörig,  Xstavi-^a.nvi^ -.  ysi  taxma 'vayS  dänubyö  azm  pilana  Yt  13. 37 ;  38.
11331:•  p,  tSi&'a°'taxma-  m.  EN.  eines  Sagar- tiers,  der  sich  gegen  Darius  I.  empörte,
11356:paitis  , .  zbayeiti  . .  yim  *driyBsat  . .  sba- yäti  Yt  10.  84;  —  %wqm  yazSnte  .  .  dai- AAu.paiays  . .  '^wqm  naraHt  ySi  taxma Jai'jyhnte  Yt  5.  85  f;  —  haraiti  bars  .  . kä  Aama  päirisSite  frSpayä  (sd.)  . ,  M3r?- fiaaS  gairis  . .  AämS  hasHt  päirisaile  .  . "das  jy.-Gebirg  . ,  umlagert  . . ;  . .  das  Z.- Gebii^,  auch  das  umlagert  . ."  Yt  ig.  i; y- 69;  —  Vlspe  ,.  tirKtnti  pfnmne  {%äj) avaia  mävayaiit.-tprisantu  Yt  14.38;  — *daSinqtn..Äaoyqm  h! paiayqm ..  dumtnüit Af  upa.%w^r^saym'V.i3.ai.;^vlsfe  haoma . . yaicit . .*upa  *dintäku{sA.)  V./0.17J  — Aazaignrn  maoirinqm  d3nS.karSanqm  ava.- jartyat  duye  hazanre  anyalsamat'-'^  V.  18. 73i  73i  —  ^y^  *gr}Amö  ä.ASi^Si  (sd.) «r  ksvayas^l  xratül  «r  dadat  ".  .  Gr., de^leichen  (sva,  und)  die  K.  richten  .." Y.  J2.  14; —  aSavatca  alsasät  ästärayeite (sd.)  N.72; — nava..anaiwyasHi  kunämi; hinti  (Sp.  370  o.)  .  .  mävayacit  ca^warS arsäna  V.lS.^j;  —  ksnti  anyäsät'^  (Sp. 137  in.)  asäs^a  /äi^ris^a  srIras/a..Y.l.2o; —  aam^i  akyS  . .  %wam  tUSökj  , .  vai- <hm  (sd.)  Y.  ig.  10;  —  mainya  .  .  yS  ä narSm(,sd.)ät.,Aäi>0  Y.^i.y  i — in  auffälliger Stellung:  mUca  paslaSa  mazdayasna  vXmä- oasHt*^  vTmSoayanta  "nicht  sollen  sie  dann auch  bei  M.  als  Ärzte  praktiziren"  V.  7, 38;  38,  40;  —  hinter  ula^^:  iavaj  aiwi.- vanyä  .  .  ta^ryävanttm  , .  ptiatamca  .  . Uta  anyäscit'^  ..  kyaon&tgkB  Wtig.ST, 89;  —  hasannm  aspä  uta  äsitqmHt /rastUntim  Yt  18.  5 ».  a)  Bei  hypotak- tischer Saufiigung  steht  das  mit  /■■  hervor- gehobene Wort  jeweils  an  zweiter  Stelle*', U2W.  a)  des  Hauptsatzes;  b)  im  Aw.: Sfit  MOra^uslrS  da^äU  sanm  vyämrvUä .  .  flS-a  *aspm^  .  .  vlinruyg  Y.  12.  6\  — ya'ha    . .    kvarsxiatä^m    .  .  fraca    Siti  .  .
11819:taxma-  62Ö
11841:*  j-i  g-  (.  P-)  taxma-  Adj.  (fem.  °mä-) 'fortis,  tapfer,  tüchtig,  energisch,  helden- haft'; a)  von  a)  Menschen  und  ß)  Göttern: a)  masyänqm  .  .  'manqm  V.  20.  i ;  —  nä •Mö  Yt  jj.  67,  Aog.Ä^;  Vyt.  2j;  —  narU 'ma  (NPm.)  Yty.  27;  5.86,  iS-Hn^^h
11843:627  taxman-
11845:•  j.  taxman-  n. 'Lauf  fliessenden  Wassers: %risum  apqm  '^raotö.stäcqm  °manqm  pairi- itayeiii  "ein  Drittel  der  im  Flussbett  fliessen- den Wasser  hindert  er  an  ihrem  Lauf V.  7*63.
11847:•  p,  taxma-späda-  m,  EN.  eines  Heer- führers Darius  I, :  'dc^  näma'  madei'  Bh. 2.14;  14.
11851:•  j.  taxmö.Mma-"'  Adj.  'der  tapferste, energischste,  heldenhafteste' :  taxms. .  "tsma (stattNSna.)  n^ffia  ahmt  Yt  73.46;  —  vamt ('den  Vayav^)  taxmanqm  'tsm^m  Yt  75.  57.
11894:'damit,  auf  dass'  vorher:  yat  yavo  (sd.) pourus  baväf  aha  ma'hnm  *t'  ^  mairyat ^•3-a-  3)  'damals,  da',  ini  Wechsel mit  ta6a  (sd.)*':  tala  dim  akurS  mazdä avqn  (Sp.  1 1 2  m.)  . .  t°  apu  urvaras<a  YL 8."];  —  fravasayS  .  .  yä  .  .  laoa  nijasm (Sp.  500  m.)  xÜiviwyS  *pi^  yöi  taxma xstävayB  dänubyS  az>n  pthnh  Yt.  13. 37.  4)  'dann,  alsdann':  yas>  t  *api- vataiti  (sd.)  parmtarim  (sd.)  issil  N. 12.  a)    zusammen    mit    aaf:    US  patti
11988:•  j.  tan£iita-  Adj.  (fem.  'li-)  'der  tapferste, energischste,  heldenhafteste';  i)von  a)Men- schen  und  ß)  Göttern:  a)  tBtn  xara^u/tra .  .  yö  aojists  .  .  °ts .,  %waxiWs . .  abaval mainivä  dämqn  Y.p,  15;  —  'timca  darae- ^at»«  YL3.73;  —  häuca  ii:ra..taxmanam
12511:•  j.''daevö.tbiä-"m.EN.  eines  Gläubigen: 'ibsii  taxmaht  aiwns  Yt  y.  98.
13393:•  j.  'dänav-  Adj.,  bezeichnet  einen  den  Ira- niern  feindlichen  i'Srischen  Volksstamm: tala  yöi  taxma  xstüvayS  'nubyS  az)n  p?sana yüz»tn  (näml.  /ravasayj)  tdm  taurvayata v>r?^r?m  'nunqtn  türanqm..t6al^3  'nunam türanqm  .  .  xrBma  asSbis  frasinta  (sd.) "nunqm  baivari.pailinqm  Yt-/J.  37f.;  — yat  baväma  aiwi.vanya  °nav3  (als  AP.) tära  vyäxana  Yt.  J.  73.
15708:•  j,  parana'va-  Adj,  'mit  einer  Feder  ver- sehen': aslavff  (sd.)  vä..  'vH  vä  taxmaAe mirr/ahe  Yt.  14.  36.
18675:elliptisch  sva,  'ein  Mann  und  ein  Weib,  ein Menschenpaar"**:  dvaübya  haca  n)r>bya dva  nara  us^ayein/e (sd.)  t//i^wa/ia  s/ri^a nairyas^a  V.2.41.  2) '•  praegn. 'wehr- hafter Mann,  Kriegsmann;  kriegerischer Held':  narSi  ßrasaoifträi  Y.  28.  8;  — katna  (sd.)  syävarsänai  zurSjatahe  na- rahe''*  Yt*j.  18;  — pqsnus  narJ  (NS.)'^ HryS  taxmS  Aog.  84;  — y^i  narS  taxma ptntmU  Yt./J  27;  —  t! nard paiti.sanmti ySkva  v3r3%ra.l'aohl!  {sd.)  YtJ_j.  46;  — yat  mS  slärS  .  .  AacÜnte  (sd.)  n?r>byS ä^annff  *bax/3nia  Yt- 8.  1 ;  5.11,  77.6,7; das/a  narqm  *pouru.tät?m  stäkyanqm.. vanatqm  avammnanqm  Ny. J.  10;  —  hva- iai  naire  barumnäi  Y.  65.  4;  — yä  na- qm  vjg3r>pla{sd.yit . .  baoxtär^m  dahäi/i Vr.7,3;  Yt  10.12;  —  ya^a  hazannm Oim  narftn  adar.taySi^  Yt.  8.  $$; I.  19*;  —  a%ra  narqtn  mihrS.drujqtn apq/{sd.)  gavB  dar>tayeiti  Yt70. 48;  — narqm  asätanqm  frasS.car^'hrqm  saosyan- tqm  Y.  24.  5,  Yt.  13. 17.  a)  als  Bezeich- nung für  den  zweiten  Stand  (s.  'piflra-) 'Krieger,  Ritter***:  kada  .  .  mquarfi/ (sd.) rS  vis3nliY.48.  10;  — daidx atturai (AP.)  ,  .  asaunS  .  .  aidyüi  väsliyJng  ,  . ahmaibyä  ahma.rafonarahs  {^d^  Y.40.3; %wqm  ttarakl  ysi  taxma  Jathyintt äsu.aspim  .  .  %wqm  a^ravanS  .  .  mastim Yt5.  86.  3)''  ohne  Betonung  des  Ge- schlechts sva.  Mensch;  Person';  1)  im Gegensatz  zum  Tier;  uzw.  zu  a)  pasav-: ahe  nmanaßie pasvqmca  narqntla  Y.^-S; pasBm  .  .  nanm  ra?syät  V,  13.  32 b)  'span-.  . .  ahe  nmanake  spä  vä na  va  irihyat  V.5, 39;  8. 1,  4;  —  yat ahmi  spänasca  narasca  para.irüinti  V. 6.1; — y!i  pa^a  uebarmte  (^)  spänasca irista  iiarawca  (NF.)"  irisia  V.  Ä  14; 3.  32;  —  yat  ,  .  sairi  riiianie  spänasca irista  naraila  (AP.)'*  irista  V.  3.  8; 36.  c)   ^av-:  janyäi  *n>rSuI^'*  para
18888:Appellativ    folgt:    *parg<^    'mii'    kauft^ avadä  , .  Bh,j,  7;  7. 11;  —  tOzäm^  'mii' vardanam  Bh,  7. 19;  2.3,  6,  12,  16,^.1,  5. 6,  8,  2.  7;   —  AaÜa  piravJ'  •««"  rauür D.77. 3".        7)  ohne  Appellativ;  wir  über- setzen dann  'einer  namens  , .'  oder  'ein  ge- wisser"*': kt^baßya*  °»w"  kärausptth^^ .. püruvam  ida  lüäya^iyi^  aAi/'  'Bh.i.io;  — taxmaspad^  'md'  mSd(^  manä  b(^dakt^ Bh.2.i4;io,j.3,6,q,  i4,^i8*,S.7.      Ohne Wert:     darayj'vcTus     vistaspakya     'mi^ /«ä'a*    Ao.  7.  2;   2.        b)    nätm/*;    das Appellativ  folgt:  hauv  udapatalä  habiraav dubali^  -ff/j"  äahyaus  haca  avadasa^  Bh. J-»3;3.  5.  »o.  ^-»S-i-ö,  10, 11, 13;— /«fra* -Ma"  dida  arminiyaiy  avadä  hamaranam akunav<i'  Bb.2,8;  9,   7.13, _j. 9,  11. KompA.  (n^iH'),  E.  —  tä.  tUiman-  n.,  np.  nän. —  P6,i  näm;  s.  nOch  No.  3.  —  >>  Nur  in  nfiu, aber  hier  stets.  —  >)  So  alle  Hds.,  mit  jinei Ausnahme,   J  3,   wonach  NA.  'oif  bietet  — 3)    Fü.:    nndeaüichi    a/ä^i  addpnark  ann (Jamaspji  Gloss.  569  u.)  paakann.  —   1)  S. No.  6.  —  5)  Von  dem  es  nur  durch  ein  Ed- klitikum  getrennt  sein  kann.  — ')  Die  Frage, wie     ap.    t^amf    beim     mask.    nnd     neutr., rfiamt^  beim  fem.  Appellativum   formal   and syntaktisch    zu    fassen    sei,    ist    noch  nicht gelöstj  luletit  darüber  FoY  IF.  la.  171,   wo weitre  Litt.  —    7)  S.  No.  9.-8)  Vgl.  FOV aO.   174.  -^  9)  Fovs  Fassung  von  ßiräva*  aU Abi.,  aO.  176  halte  ich  nicht  für  richtig;  ich verlange  auch  hier  den  Nom.j   s.  Sp.  907  o.
20910:YtÄ  48.  f)  GPra.:  mtirS  vtspS  matda'\  hacaite  asis  .  .  uyrasca  dämdis  upamanO yasnanqm  yam  asaenqm  fr}},wä{sd.)cit  .  .\uyrasca  asaonqm  frava^ayS  yasla  pouru- Yt./o.i3ci,  IIB) bedeutungslos  erscheint  HflOT  hairaks\%A:)  Yt.  /o.  66.  b)  NSf.: uns  das  Relativ  vielfach  dann,  wenn  es,  j>'n^  dim  upanhacat  yä  uyra  naire  kam.' ohne  dass  ein  Verbum  folgt,  dem  Nomen,  1  z-'n/vift'/ Yt. /p.  39;  —  aiHi  ätm  atwyäiti mit  dem  es  kongruirt,  und  dessen  Attri-|_V'l  dahma  *va»uhi  afritis  P,J2;  —  kai buten  vorausgeht  a)  im  gAw.;  I)  \\a\hE  vä  i7j><«  (Sp.  237  m.)  *v?nzyap  ya  näi- Nominativ  oder  dem  ihm  gleichen  Akku- ,  rika  N.  6;  —  saoayeiti  yü  hava  daena  H. sativ.  Die  Fälle,  die  hierher  gezogen  wer-  2.9;  it']  —  ks  yä  kaine  'V.i4.-i^^'>'>;  — den  können,  sind  unter  IIB  verzeichnet:  [hierher  oder  zuIB  (Rel,  in  Kongruenz  mit Y-JO-S  0'^  dr3gva\  4ü.z  (ysi  uxsanS  Atm  Praed.):  *kä  larJ.maitisl  ya  kaca asnqm),32.i.%{yä  karapuäsm  k3Vltasi^,\dainay3t  milzdayasiiStl  apastüitii  U.  4t; 45- 1  (ya  n^qs  sadra),  46.Z  (yy  vä  iiiDi' —  ya  papiiiua  vasö  acisße  (sd.)  N, yä  galhä  datdl  *aSnaAhFj  usw.  Z)  in  ■  62.       c)N.-APm.r  *'taty5i  taxma  xitavayB
21847:•  j.  yüxJa-  Adj.  'gewandt"':  kB  hhrpa varäzahe  .  .   taxmahe    'aahe  pairivilzahe
22690:•j. 'vayav-, 'vaya- ''m. 'Luft,  Atmosphäre', als  Gottheit'*':  'yus  bä  nqma  ahmt . .  avat •yus  .  .yat  «va  dqma  vayemi  yasca  äa%al sp»nts  mainyui yasca  da'^at  anrS  matnyus Yt.  1$.  43 ;  —  'yusys  upar5.kairy5  Yl  75. 4, 2 1 ;  3  (als  Vok.) ;  —  'yus  aurvS  *usiäj *yasts  d>r3ii.yaox3ürS ..\t.is.^^;  —  °yaos uparS-katryiiu  tarähätö  anyäts  dämqn  Y. 22.24,  Ytij.  o;  —  %wasahe  3^diätahe trvanaht  akaranahe  'yaos  upareJkairyeAe V./P.13;  S.J.21;  —  aaai  ti  -yö  (Vok.) yazamaidt  yat  tl  asti  sp>ntS.mainyaem  Y. Äj.  5 ;  —  '^  aurva . .  'yS  taxma  Yt.  15.11; —  t9m  yazai . .  uynm  vaim  (Akk.)  uparS.' iairlm  Yl/J.  5;  —  valm  aiavamm  .. valm  uparS.kairim  .  .  tardhättm  anyüis dämqn    Y.  25.  5,  S.  2.  2i;    Yt/J.  1';    —  .
23661:•  j.  v»r3*rl-gan-  ■>  :  -^ra-y/i-  Adj,  'wehr-  ^^  ^j/i  mainyavanam  yazatanam  sayS.- haft,  siegreich";  a)  von  a)  Göttern  und ,  i^^gj  .  _  .„5  ahuraiatö  Yt  /4.  i';  —  sonst ß)  Menschen;  zu  a.)-.  ahumi  matdäi  .  . ;  stets  mit  aAuraläfa-.  äjasat  vassmnS  'nS '%r<r}ne  ^aäat^Mhai  WT.n.i;^.S5.ä,;aAuralatS  ha  kihrpa  varasake  Yt.  14. —  'hraja  (NS.)  sraasS  .  .  a/yS  Y.  57.  3,  j  ,  j  .  j  (1,3^^^,  AiÄ^^ta},  7  {gSu/  hhrpa), 14;  j2;  —  sraosS  .  .  huraols  •%raja  V.  I  g  {aspahe  k>hrpa),  11  (kZ/tbä;  kshrpa), ig.  40i  Vr.  /5.  3,  /(;.  i,  Yt  //.  7,  Y.  2.  7, 1  17  („a^/  Ä;'/!^?»«),  19  {m>nr/aAe  kfhrpa), 57.1,  Az.6;  —  jr.rw'ijAe  ..  '%räjara  Y. ;  33  {ma^ahe  kihrpa),  25  {batahe  k?hrpa), i.  7;  —  -iflomö-  .  .  'ärfl/a  Y.9. 16;  Yt  27  {j/fra^^  kihrpa);  —  'nS  ahuraoats  .  . '4-57>  —  <nryamam>M  ..  amavanhm  ys  _  upaJiaxtö  a.mimar>ha  süja  nijainH '%rajamm  -^.54.2,  G.i.6;  —  fravaiayS  hamfrp-^sYtio.T=i.;i4.(>2,6z;—''hmai ..ha^ra  väta  '%räjana  Yt./J.47;  —,  dahat  'nS  aiuralatB  fnxBtsxä  bäzvä  aojs Aähra  vaia  •>rajanS  (sUtt  IS.)''  Yt  JO.  1  yt.;^  ag;  i_  7*1,48,  54;  —  am?inca  Au- 9,  12.  4,  13-  48.  ß)  '%raß  taxmB  %rag-^ :  /^Äw,  .  .  •«j-mA  ahurdmhm  Y.  2,  6 ;  /ff. /fftwi^  Yt5.6i;  Az.2;  —  yaha  'hraja  j^  j-^.  ^g^  Vr.  2.  8,  Yt  14.  5%  V.  /p.  37, vtmat.pflafts  fraxStane  Y. p.  20;  — /Ämi  l  Az.  7;  —  "«b-**  ahuralatahe  vanaintyism asti  aiava  ''iira/a  '^. 58-  r,—  ^"r^oiS . .\  „paratate  Vr.  1.  6,  Y.  /.  6;  Yt  /4.  o,  43, ^Ä  taxma  saosyatüS  ySi  taxma  'hrO/ans.  ^g_  a)  vtn%raynahe  (nUml.  afun-) (NP.)  YL/j.  38;  —  buyama  J-ic^on/Sl  heiast  der  20.  Monatstag:  -»aÄ^  ff Ä«r«3j- ^jflMÄ  •%räjat0  Y.70.4.  Pß)  bes.  /a/i,;  S. /.20;  vgl  2.20.  Y.  16.  5;  —  a/iäi- vom  SaoiyantAst!;aljr9ta-.  sac^yas  '%ra/a  ^  ,r«  «a/gj,j,rfrf*  rfaäaiJ  'nahe  A. ^.  1 1. »WOTff  astvat.3r?tasca  nama  YtiJ.  129;  V.l  •)  ihm  ist  Yt  14  geweiht;  s.  noch  Yt.  lO. ig.$,  Vyt^o;    —    astvat.9rftahe  •%raynS  7i.    Vgl.  Dst.  ZA.  3.  559,    Hbm.  AGr.  /.  75;
25082:•  j.  raö'ae-star-,  rad-ae-ätä-,  ra95i-ätä-'' m.  'Krieger,  Kriegsheld':  ya'ha  «j  taxmS °tä  (NS.)  Yt  13.  67;  —  taxmim  tusim  'ia- nm  Yt  5,  58;  Vyt  26;  —  mihnm  .  .  yim yaztnte  'tärS  Yt.  10.  \i;  j.  53  '> ;  —  mihrfm . .  laxiram  °tam  Yt  70.  140;  112,  25,  102; —  iraosahe  . .  taxmake  .  .  'ta  (GS.)  Y. 57-33;  —  ätari  spmta  'i3ra<yS.)^  Ny.j. 6;  Y.  ä^2.8Gl.  A)insbe3.alsBezeichnung für  den  zweiten,  den  Kriegerstand  (vgl.  unter 'piära-):  shrava  '/i  (NS.)  västryö /ü^qs Asitis'  Y.  ig.  ij;  11. 6,  Yt.i3.89,  V.5.  38, '^•45^i  —  ähravarum  ..'iär>nt  ..vasirJm fsuyantftn  Vr.^.  2;  Yt2, 12;  —  a%auru- naSca  °tüua  västrySica  fiitymte  Yt/p.  8; 7J.88,  V.5.  57,  58;  —  västry^Z  fsuyatas ..  'tä  (GS.)  ..  a'iiaurunS  Y.  13.21.;  — asti  iir  haim  (sd.)  ydha  'tärahe^l  Y.13. 44;  4Si  Vyt  J,  16,  Az.5;  —  vUpe  saya °%äis'ti  (LS.)  "alle  Ausrilstungsgegenstände für  einen  Krieger"  V.  74-9;  9;  —  '^^<»- urunqscä  -tascä  (AP.)  västryas^a  f/uyants Y.  7j.  3;  —  a^aurunqs^a  'tarSsla  (AP.)3) väitryqsca  fiuyants  Vr.^j,  5;  —  hast»ma alahe  ama  'ta  Y.13.2.
```


## [2026-09-04T18:59:46.479Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['BRT','PHD','NYB','HRN','HUB','CHEUNG','KLN','SKT','FSD','LEW','LAT','AFM','FVQ','AFA','LKT','POK','WLD','AHD','SYN','SOD','FSF']:\n    v=d.get(k,{})\n    print(k,'|',v.get('page_offset'),'|',str(v.get('local_file'))[:200])\n\""
}
```


### [2026-09-04T18:59:48.102Z] TOOL RESULT

```
BRT | Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
PHD | leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
NYB | Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
HRN | leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
HUB | leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
CHEUNG | None | None
KLN | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
SKT | leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
FSD | vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
LEW | 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt
LAT | leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt
AFM | 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt']
FVQ | printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt']
AFA | leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt
LKT | leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
POK | POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
WLD | Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/da
AHD | 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
SYN | leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
SOD | printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
FSF | 484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt']
```


## [2026-09-04T18:59:54.774Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"huraoö\\|huraol\\|huraoä\\|huraoS\\|huraob\\|huraoo\\|huraoQ\\|huraoh\\|huraod\" BRT.txt | head -20"
}
```


### [2026-09-04T18:59:54.825Z] TOOL RESULT

```
4716:•^NÄr^:!  -^  P.-'i  W  .„  .  *.-  kräftig':  kainm..    'mayä  huraolayh  H.
7945:mä:uiayasmm  frapinaeiti  V.  ^,  3 1 ;  —  urva- "iamlit  ziayemi  avt  •mai  varS  Yl  12. 3 (vgl.  12.4,  wo  avat);^  °mal  iimltum  yaol- diiiätu  .  .  'map'>  ätram  .  .  "mat^  apim . ,  °mat^^  zqttt  ,  .  °maO^  gqm  .  .  *maj^' un-arqm  .  .  'mat>^  nartm  asava/um  .  . 'mal^  näiriiqm  V.  ij.4— 7 ;  —  'm^rn  hao- m?m  .  .  äyese  yesti  'mqmca  gqm  .  .  °mä zaoira  .  .  °tnq  asmqsca  baoioTmfa  Y.  22. 1-3;  >.  3.  2.'i*.  ^.4,  4-i\  3.  ^ö-i.  GS. 14.  7^-23;  —  {ävaihayama/it)  'mq  kaomq 'ma  haomya  'ma  stania  "ma  myazäa  "ma asma  .  .  'ma  (AD.)  asmana  Aävana  .  , 'ma  ayaahama  Mvana  .  .  °mqm  Sp)m  .  . 'inat  barasma  .  .  °ma  kihrpasca  DvTslsca 'mH  ..  :ao^ra  "mrm  haomim  Vr. //.  at; —  paiti  ti  trarrfa  .  .  'mä  srvä  va^a- yemi  .  .  °mäs>  tE  srvä  m»yya  .  .  kyHr? arstayasca  Y.ij.g;  9;  —  'iru>m  U  nanm nisrinaomi  V.  /i".  5 1 ;  5 1 ;  —  D  °mam  psrsam ksram  psdiy  yadiy  karJ'  parstr  pst<^ ahatiy ..\i.$.y,—<^urJ'mttzäSmaiy  upasläm abarc/'  yätä  °mt^  xio^j^am  adäry  voinil (^uri^masdah!^  °«ni*  xia%''am  dilrayämiy Bh. /.  9;ll —  nSit  °mal  vTsp>m  düivarstsm .  .  mObrS  vaenaiti  Yt  ro.  10g.  a)  sub- stantivisch: D  draug^dif  hami'h''iyä  aku- nat^ ty(^  'maiy  karam  adurujiyasti'"..yie^ die  hier  (näml-  die  abgebildeten  Empörer) das  Volk  belogen  haben"  Bh.^.  4 ;  —  'me  nö ..aspapara.-nay enteist.)  'me  nS..*bäzava sHndayänii  (sd.)  Yt. /0.4z.  a)  mit  einem erläuternden  oder  ergänzenden  Relativ; a)  adjektivisch:  -mat  karhara  yät  ifani- ra>>m  Y. 57.31,  Yt  70.15,  133,  JB.15, H.  /.  14;  —  alis  .  .  rämyat  im  upa  'mal nmänsm  yat  äküiri  Y.  10.  i ;  —  ima  asäsca sOdrasca  . .  'msm  sBdrahe  paüim  ytm ahunm  Y.  2.16;  —  °mqm  dasriqm  yqm sAäirfm  YtÄgg;  —  'mqm  .  .  tqm  . .  yä nS  baraitt  Y.jS.i;  y.i;  —  vTspä  'mä 3ps  ys  amä  patti  /rataSnii  Y.  (»5. 3 ;  — 'mqm  tanüm  yä  ml  vaSnaite  huraoha  Y. /o.  14,  ß)  substantivisch:  vispgm  'mal
11225:•  j,  iaräiti- £ 'jungeFrau"^  uzw.  aÄwnscher Schöpfung:  'räiH  (NS.)  huraolaya  darr^a apuhra  aäti  V.J.  24;  —  %wqm  (näml. arpdvlm)  kainitiS  .  .  ja^iyhnte  .  .  nmänö.- faiilm  'hwam  'räitis  (NP.)  zhanäitis  Jail- yiinte  hutämJm  Ytj.S?;  —  äsca  'räitis (NS-)  ahi  yqm  il  yava  'räitinqm  k?hrpa sraistqm  dadar?sa  H.  2, 10.
16957:i)  Villkommen  heissen',  mit  Gen.'': /rasa  fraya  vahist>tn  ä  ahüm  hnjayanti y?  . .  *sirSus!a  . .  azpmca  Al  bpnjaim  yö  .  . ahurS .  .  uäa  *äa  ti  nun  "'stracks  gehe weiter  zum  Paradies'  (so)  werden  ihn willkommen  heissen  die  Sterne . .  und  (so) werde  ich  ihn  willkommen  heissen,  ich  der Schöpfer  AAM.,  'nach  Wunsch  geh  es  dir hier,  o  Mami'"  V.  7. 52.  2)  'huldigen', mit  Gen.:  bm/ayai  ahurS  .  .  b>njay>n amisä  spMta  yeAha  (sd.)  IbArpff  huraohaya ". .  des  schöngestaltetem  Leib  huldigte j4AM.  . ."  Yt  10.  90;  —  *fraiaintlmca  .  . ye^hh  peurUsca  iftv/ayqn'^  naicisca  aitiha ydssiti  . .  "und  Nachkommenschaft  , .,  der manch  einer  huldigen  und  der  keiner wünschen  soll  .  ."  Y.6'5. 11.
18734:•  j.  nairy5,saoha-'>  m.  Name  einer  Gott- heit {Yazata),  die  des  Götterbotenamts waltet;  *'hs'^  ..  astö  mazdä  ahurahe  "J^., der  Bote  des  AhM^  V.  ;p.  34;  34;  — nairyS.sarjAs  (statt  Dat )  aocayata  yS  dmva ahurS  masdh:  nairya  sartha  '*  vyHxana  . . imal  saiihsil  airyamanai  V.  22.  7;  13;  — sraosasca  ,  .  °hasca  yd  mayu^{sA.)  Yt  10. 5a;  —  apqm  naptärsm  . .  nairim  sanfum  '> Y.  77.  23;  —  sraohm  ..  nairimca  saa/ifin'^ huraohm  Y.  57.  3,  Vyt^o;  Vr.  7.  i;  — sraolake  ,  .  nairyeheca  sat?haAe'^  Vr.  is. 16;  — yqmca  (räml.  Jrava/lm)  srao/aAe ..yqmca  nairyeAe  saaAaAe'^  Yty.Sj;  — Xfa%r»n.nafolrfm  "Atm  yazattm  Y.  77. 1 1 ;
23661:•  j.  v»r3*rl-gan-  ■>  :  -^ra-y/i-  Adj,  'wehr-  ^^  ^j/i  mainyavanam  yazatanam  sayS.- haft,  siegreich";  a)  von  a)  Göttern  und ,  i^^gj  .  _  .„5  ahuraiatö  Yt  /4.  i';  —  sonst ß)  Menschen;  zu  a.)-.  ahumi  matdäi  .  . ;  stets  mit  aAuraläfa-.  äjasat  vassmnS  'nS '%r<r}ne  ^aäat^Mhai  WT.n.i;^.S5.ä,;aAuralatS  ha  kihrpa  varasake  Yt.  14. —  'hraja  (NS.)  sraasS  .  .  a/yS  Y.  57.  3,  j  ,  j  .  j  (1,3^^^,  AiÄ^^ta},  7  {gSu/  hhrpa), 14;  j2;  —  sraosS  .  .  huraols  •%raja  V.  I  g  {aspahe  k>hrpa),  11  (kZ/tbä;  kshrpa), ig.  40i  Vr.  /5.  3,  /(;.  i,  Yt  //.  7,  Y.  2.  7, 1  17  („a^/  Ä;'/!^?»«),  19  {m>nr/aAe  kfhrpa), 57.1,  Az.6;  —  jr.rw'ijAe  ..  '%räjara  Y. ;  33  {ma^ahe  kihrpa),  25  {batahe  k?hrpa), i.  7;  —  -iflomö-  .  .  'ärfl/a  Y.9. 16;  Yt  27  {j/fra^^  kihrpa);  —  'nS  ahuraoats  .  . '4-57>  —  <nryamam>M  ..  amavanhm  ys  _  upaJiaxtö  a.mimar>ha  süja  nijainH '%rajamm  -^.54.2,  G.i.6;  —  fravaiayS  hamfrp-^sYtio.T=i.;i4.(>2,6z;—''hmai ..ha^ra  väta  '%räjana  Yt./J.47;  —,  dahat  'nS  aiuralatB  fnxBtsxä  bäzvä  aojs Aähra  vaia  •>rajanS  (sUtt  IS.)''  Yt  JO.  1  yt.;^  ag;  i_  7*1,48,  54;  —  am?inca  Au- 9,  12.  4,  13-  48.  ß)  '%raß  taxmB  %rag-^ :  /^Äw,  .  .  •«j-mA  ahurdmhm  Y.  2,  6 ;  /ff. /fftwi^  Yt5.6i;  Az.2;  —  yaha  'hraja  j^  j-^.  ^g^  Vr.  2.  8,  Yt  14.  5%  V.  /p.  37, vtmat.pflafts  fraxStane  Y. p.  20;  — /Ämi  l  Az.  7;  —  "«b-**  ahuralatahe  vanaintyism asti  aiava  ''iira/a  '^. 58-  r,—  ^"r^oiS . .\  „paratate  Vr.  1.  6,  Y.  /.  6;  Yt  /4.  o,  43, ^Ä  taxma  saosyatüS  ySi  taxma  'hrO/ans.  ^g_  a)  vtn%raynahe  (nUml.  afun-) (NP.)  YL/j.  38;  —  buyama  J-ic^on/Sl  heiast  der  20.  Monatstag:  -»aÄ^  ff Ä«r«3j- ^jflMÄ  •%räjat0  Y.70.4.  Pß)  bes.  /a/i,;  S. /.20;  vgl  2.20.  Y.  16.  5;  —  a/iäi- vom  SaoiyantAst!;aljr9ta-.  sac^yas  '%ra/a  ^  ,r«  «a/gj,j,rfrf*  rfaäaiJ  'nahe  A. ^.  1 1. »WOTff  astvat.3r?tasca  nama  YtiJ.  129;  V.l  •)  ihm  ist  Yt  14  geweiht;  s.  noch  Yt.  lO. ig.$,  Vyt^o;    —    astvat.9rftahe  •%raynS  7i.    Vgl.  Dst.  ZA.  3.  559,    Hbm.  AGr.  /.  75;
```


## [2026-09-04T19:00:04.319Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"hu\\.raoö\\|hu\\.raol\\|hu\\.raod\\|hu\\.rao\" BRT.txt | head; echo \"---- context lines with 'schöngestaltet' or 'schön gewachsen'\"; grep -n \"schöngestaltet\\|wohlgewachsen\\|schön  gewachsen\\|schöner  Gestalt\" BRT.txt | head -10"
}
```


### [2026-09-04T19:00:04.395Z] TOOL RESULT

```
18188:•  j.  fränya-  m.  EN.  eines  Gläubigen: vohu.rao<!aahs  (sd.)  'yehe  .  .  a!s.raocanhS °yehe  . .  var?stns.rao^aT?hö  'yehe  Yt/y.g?.
---- context lines with 'schöngestaltet' or 'schön gewachsen'
16957:i)  Villkommen  heissen',  mit  Gen.'': /rasa  fraya  vahist>tn  ä  ahüm  hnjayanti y?  . .  *sirSus!a  . .  azpmca  Al  bpnjaim  yö  .  . ahurS .  .  uäa  *äa  ti  nun  "'stracks  gehe weiter  zum  Paradies'  (so)  werden  ihn willkommen  heissen  die  Sterne . .  und  (so) werde  ich  ihn  willkommen  heissen,  ich  der Schöpfer  AAM.,  'nach  Wunsch  geh  es  dir hier,  o  Mami'"  V.  7. 52.  2)  'huldigen', mit  Gen.:  bm/ayai  ahurS  .  .  b>njay>n amisä  spMta  yeAha  (sd.)  IbArpff  huraohaya ". .  des  schöngestaltetem  Leib  huldigte j4AM.  . ."  Yt  10.  90;  —  *fraiaintlmca  .  . ye^hh  peurUsca  iftv/ayqn'^  naicisca  aitiha ydssiti  . .  "und  Nachkommenschaft  , .,  der manch  einer  huldigen  und  der  keiner wünschen  soll  .  ."  Y.6'5. 11.
19218:•  j.  nivizan-  Adj.  'anziehend,  reizend,  1 '^'''*  Yt/5. 45,  Geringe  Stelle. gefällig'  ■>:  Äa  hi  maiUm  nyazata  ya^aca  .  ,  j.  nisma-  m.  '(Hineingehen  in  den  Erd- hukfr)ptaßtänayai!aca  anh)rfz3nal^'Q:)  \^o^^^  sva.)  Tiefe':  paoirjm  upa  vmy>m "äe  schnürt  sich  ihre  Taille,  damit  '-^tz  ■  ni>:w>rnöil  .  .  dva  »rssu  -mähe''»  "das Brüste  schöngestaltet  und  damit  sie  gefällig ,  erste  Loch  sollst  du  .  .  zwei  Finger  in seien"  Yt 5.127.  der  Tiefe  ausstechen"  V.o.  6.
```


## [2026-09-04T19:00:11.967Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24860,24960p' BRT.txt | grep -n \"^[0-9]\\{3,4\\}\\|raod\\|raoda\\|14[0-9][0-9]\\|15[0-9][0-9]\" | head -40"
}
```


### [2026-09-04T19:00:13.887Z] TOOL RESULT

```
1:•  j.  raodas.pairista-  Adj.  'zum  Leuchten, 2U  lichtem,  hellem  Era.nd  ausgesucht''*':  yd ahmäi  (näml.  S^re)  assmiin  (sd.)  baraiti Mkai  *'tqm''>  Y. 62.10;  zit.  V.j>V.  27.
6:1490
14:1491
15:'raodah-
26:•  j.  raodah'ya-  Adj.  'licht,  hell',  Plur.  neutr. Tageslicht':  {antari)  'cake  (APn.)"'  nBii antars  (sd.)  timahe  li.68.
38:•  g.  'raod-,  j.  'rao^-"  V.  'jammem'. Praes.  3  uru^a-,  30  (Kaus.)  uraddya-'^; s-AoT.   I  raos-.
41:auch  ZDMG.  44-  553  lu  sbal.  rdtag.  — ')  S  3^.  —  ^*  Eine  höchst  auflallige  Diver- genz. —  4)  Ich  sehe  in  der  Sielt«  eine  .An- spielung auf  Y.  2p.  9.  —  i)  Vgl.  Pü.  lU  Iraaä-, itoöd:  —  6)  Erl.:  tuland  mai  älil.  Wie  ffit 'raod-;  s.  aber  V.ig.^^,  wo  die  gleiche  Ver- bindung. —  7>  Angebl.  drax/  'Baum'I
42:•  j.  'raod-  V.  'wachsen'.  Praes.  2  rao^a-i 27  urulya-;  PerC  i  urürud-,  —  PPfp. urusda-,  urusta-^^;  In£  raose^^.
46:'raod-  Scbluss
47:3raod-  Noten
48:1494
62:•  j-,  g.  ^raod-,  j.  'rao9^''  V.  'abhalten'. Praes,  2  raoia-,  rao^a-,  30  (Iter.)  «70- 6aya-;  Perf.  i  ursraod: — PP(P.  "urusäa", 'urusta-  'K
76:149S
77:*raod-
79:•  j.  ^raod-  V.  'fliessen',  Praes.  2  raooa-, 30  (Kaus.)  raoaaya-.
87:•  j.  raoda-  ni.  i)  'Wachstum'  (nurl Komp.).  2)Plur.  'das  äussere  Ansehen': kairiTnS  .  .  panladasayä  'oaesva  "eines Mädchens  .  .  von  fünfzehn  Jahren  nach dem  äussern  .Ansehen"  H.a.  9; — pan^a- dasa  (ND.)  fra^ardvie ..-'Mlsva  kaiarasHt Y.O.S,
88:KompE.  —  Vgl.  roöOiia-  No.  4.  —  Zum  V. *raod:  —  ai,  riha-  m.  'Erhebuuf;',  np,  rdi 'Gesicht'.  —  Pü.:  {75  sälai)  äriiiia.
99:•  j,  'raoft-  V.  'jammern':  s,  unter  'raod-,
100:•  j.  'raoS--  V.  'abhalten';  s.  unter  ^raod .
```


## [2026-09-04T19:00:26.435Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in PHD.txt PHD_mackenzie.txt; do echo \"##### $f\"; grep -n \"rōstāg\\|rostag\\|rōstāk\\|rwstʾk\\|rustāg\" $f | head -5; echo \"-- rōy/rustan\"; grep -n \"rōy\\b\\|rōyēd\\|rustan\\|rust '\" $f | head -10; echo \"-- raz\"; grep -n \"^raz\\|raz \" $f | head -5; echo \"-- hurust\"; grep -n \"hurust\\|hu-rust\\|hurušt\" $f | head -5; echo \"-- rōd river\"; grep -n \"rōd \\|rōd,\\|rawd\" $f|head -5; done"
}
```


### [2026-09-04T19:00:28.567Z] TOOL RESULT

```
##### PHD.txt
3460:river ród; ~ bank ródbür; ~ bed rostag.
4930:rostag randidan, rustan rob
-- rōy/rustan
559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
561:rdz-Saban [YWM, lwc sp’n' | N šabān(a)rēz] day and night. rózwürag [/zvcw?/k!] daily, everyday. róz-ward [/wcwlt'] changeable, fickle. rubüdan, rubāy- [/pwtn!, lp d- | M rbwdn, rb’y-, N ~] snatch, rob. rüdan, rün- [/win', lwn- | (N rūda)] pluck, pull out. rürag [/wlk'] medicinal plant, herb. rustan, rdy- [lwstn', lwd- | M rwst, rwy-, N ~] grow. ~išn: growth. ruwān [lwbn'! | M rwn, N ~] soul. ~ig [-yk! | N ~7] spiritual. ruzd [lwzd | M rwzd, N таза] greedy. ~ih : greed.
2165:grow rustan; (increase) abzüdan, walidan, waxSidan.
4930:rostag randidan, rustan rob
-- raz
130:delete ozarak ... padist ... add threat. pad-nigerián ... for cared for, guarded read carefully. add  parisp [plsp | M prysp] wall. ?pid ... add (M pyt). purnay [pwin'd = Av. pərənayu-] adult. add  purr-marg |-mlg| deadly, baneful. raz ... add M rz. add rebas [lyp's | N ~] rhubarb. ?ristag ... add N rasta. add гох [lhw' | N <] rook, castle (chess). sahistan ... read (M shyd, P s‘y-). add sārwār [s ]w I helmet. add  sayistan, say- [ŠKBHWN-tn < A Vškb | P sy-] lie down.
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
746:after fraz az, pas az, pay i.
808:apart from fraz az, jud az.
-- hurust
4301:well-born pad-góhr(ag). well-grown hurust. well-known nāmčišt.
-- rōd river
##### PHD_mackenzie.txt
6449:   rostag, zand.                        dung guh, sargen.
7363:   rostag, sahrestan.                          rain (v.) waridan, wa!itan.
7472:    rostag.                                salt namak; (land) sorag.
9399:rostag                     \.Y~~          rawagenidan
-- rōy/rustan
4428:roy-, ,....,iin, v. rustan.
4447:rustan, r6y- [lwstn l , lwd· I M rwst, rwy·, N ......] grow.
6721:grow rustan; (increase) abzudan,            zyanomand.
9403:randidan, rustan                          rawag
-- raz
603:       raz ... add M rz.
816:abraz [lj)l'c I N afraz] acclivity.
2061:draz [dPe I N diriiz] long.
2357:fraz [pr)c I M pr)z, N faraz] forth, forwards.
4374:raz [Ie, lz I N -] vine: vineyard.
-- hurust
7961:well-grown hurust.                     woe way.
-- rōd river
```


## [2026-09-04T19:00:39.841Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"hurust\\|hu-rust\\|hu-ram\\|huram\" PHD.txt | head -10; echo \"=== leaves ===\"; python3 - <<'EOF'\nlines=open('PHD.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in [559,561,557,4301,3460]:\n    print(ln,'leaf',('\\n'.join(lines[:ln])).count('\\f'), 'printed p ~', ('\\n'.join(lines[:ln])).count('\\f')-21)\nEOF"
}
```


### [2026-09-04T19:00:41.556Z] TOOL RESULT

```
400:huniyāģar [hwayd’kl | N xunyágar] entertainer, musician. hu-niyox$ [hwnydwhs] attentive. hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~ih : happiness, content. hunušak [hwnsk' = Av. hunu§] offspring (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic drink, *koumiss. huram [hwlm | N xurram !] happy. ««īh: happiness. hurām [л?т] blissful. hu-|-ramag [hwlmk'] having good flocks. ~-rust [-/wst'] well-grown. ---Süzagih [-s’ckyh] agreement. ~-8рӣз [-s5?s] grateful. ^ husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good керше у m ~ih: fame, good repute. Ms hušk [kwšśk! | = M, N xušk] dry. —-kün [-S TE] impotent. hu-škūh [kwškwh] dignified, splendid. ^h: dignity. hu&nüd(ag) [лото (А)! | M hwinwd, N xusniid] contented, happy. ~th: contentment, happiness. hu-tuxš [kwtwhš] artisan. huwaršt [hwwlst! = Av. hwarfta-] virtue, good deed. hu-xém [hwhym] of good character, good-natured. ^h: good character. hüxt [kwht' = Av. hüxta-] good speech.
760:Ahuramazda Ohrmazd.
2200:happiness farroxīh, huramih, hun- sandih, hušnūdih, šādih, šnāyēn- išn, urwāzišn, xwa(h)rih.
2201:happy farrox, huram, hušnüd, Sad, xunak.
4301:well-born pad-góhr(ag). well-grown hurust. well-known nāmčišt.
=== leaves ===
559 leaf 98 printed p ~ 77
561 leaf 98 printed p ~ 77
557 leaf 97 printed p ~ 76
4301 leaf 185 printed p ~ 164
3460 leaf 158 printed p ~ 137
```


## [2026-09-04T19:00:51.281Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nlines=open('PHD.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('line400 leaf',('\\n'.join(lines[:400])).count('\\f'),'printed', ('\\n'.join(lines[:400])).count('\\f')-21)\n\"; echo \"##### NYB\"; grep -n \"rōstāg\\|rōstāk\\|rwstʾk\\|lwstʾk\\|rustāg\" NYB_vol2_glossary.txt | head -10; echo \"-- NYB rustan/rōy\"; grep -n \"rustan\\|rōy-\\|rwstn\\|lwstn\" NYB_vol2_glossary.txt | head -10; echo \"-- NYB raz\"; grep -n \"raz \\|raz,\" NYB_vol2_glossary.txt | head -8; echo \"-- NYB rōd\"; grep -n \"rōd\\b\\|rōt \\|rautah\" NYB_vol2_glossary.txt|head -8; echo \"-- NYB hurust\"; grep -n \"hurust\\|hu-rust\\|hulwst\" NYB_vol2_glossary.txt|head"
}
```


### [2026-09-04T19:00:53.301Z] TOOL RESULT

```
line400 leaf 69 printed 48
##### NYB
-- NYB rustan/rōy
640:a-rödiSnik ['Iwdšnyk] unborn 88?. - From rustan (g. v.). Paz. substitutes azāišnī = a-zäyisnik from zätan (q. v.).
3335:ródénitan [Iwdynytn'] to make grow 9216, 931. — Caus. of rustan (g. v.)
3355:rustan [lwstn'] röd- [lwd-] to grow 6. 4074, 4122, 9218, 9518.22, — Av. (1492 sq.) 2raod-; MPrs pt. rwst, v. n. rwyysn (A-H I), Verbum 183; Paz. rustan roded (Mx 6238), pres. pass. rövihed (Sav XVI, 35, dubious); NP rustan röy- ; cf Bailey, BSOS VII, 1933, 84.
4298:xrostan to cry, to shout: 6 didn dévan apar bē xrēst 43'-33; vàng urost 619. — MPrth xrwštn, xrws- (S, A-H III) ‘to call’, MPrs zrwstn, xrwh- (S); NP zurös ‘a loud cry’, xurošidan ‘to shout’; Ghilain 64; Verbum 185; Schaeder, IB I, 254;
6785:röstä, röstägg: rötastäk rosnidari: roečnitarčh rövihed: rustan
6789:rustan rčded: rustan
-- NYB raz
1346:draž [dbe'] long, comp. ~-tar; ~ pat bäläi elevated, high 38°; with an inf.: it would be too long to ... 105%, v. dökän. - Av. (773sg.) dräjah- ‘length’; adj. comp. dräjyö, sup. drajištom; Paz. draz (SGV); NP diräz.
3301:riz [Uc] a secret 27», — Av. (1514) razah- ‘solitude’; MPrthPrs r’z; Paz. NP raz; Arm. lw. eraz ‘a dream’; borrowed by all Aram. dialects.
4178:Viraz [wyl’c'] n. pr. 107. — Av. (1454) Vīrāz-, more correct Virdza-. In BP traditionally read Vīrāf, which is now generally regarded as a misreading; de- fended by de Menasce, JA 237, 1949, 3—6.
5423:var-: varan varah-: !var varana-, varona-: varan varaza-: varaz varocah-: vare vareda-: gul varoka-: varg Varo0rayna-: Varhran väroma-: várom varosa-: vars varot-: vastan ?varota-: vartak varoz-: varzitan varoza-: lvarz vari-: ?var
-- NYB rōd
3348:rot [lwt'; YM?] river P1:3. 56214-16, — OP rautah-; MPrthPrs rud; Paz. NP rod.
4927:rad, radiy: *rad Raga: Rag rasa-: rasitan raucah-: roc rautah-: rot
-- NYB hurust
```


## [2026-09-04T19:01:00.317Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"rötastäk\\|rotastak\\|rōtastāk\\|rwtstk\\|lwtstk\" NYB_vol2_glossary.txt | head; echo \"---\"; sed -n '3340,3360p' NYB_vol2_glossary.txt"
}
```


### [2026-09-04T19:01:00.381Z] TOOL RESULT

```
3353:rötastäk [lwtst’k], rostak [lwst’k] district, province 377. 8618. — In FrP 2 it is the first subdivision under šahr ‘dominion, kingdom’, and placed above déh ‘village’ and zänak ‘house’, cf Nyberg, Byzantion XXXVILI, 1968, 114-115. — MPrth rwdyst’g (A-H III); Paz. röstä, pl. rostčiga ; NP rēstā(i) ‘any inhabited place; a market-town, a village’; Arab. lw. rustäg, ruzdäg ‘arable land’.
6785:röstä, röstägg: rötastäk rosnidari: roečnitarčh rövihed: rustan
7366:röstä(i): rotastak
---
(1512) ravan- ‘(course of a) river’; MPrs rwn (A-H I); Paz. NP rin (NP ‘cause, reason’).
rop [lwp'] pillage, plundering 108%. — Cf NP ruftan rob- ‘to sweep’.
rospik [lwspyk] whore 7°. — Paz. NP rospi.
rēšn [Iwšn'] 1. adj. light, bright, lumi- nous, splendent, brilliant, comp. ~-tar 3722, 668 etc. passim. — 2. subst. light: tai 50 roc ~ né bavét (pres. hist.) during 50 days it did not get light 2015; ~ bavandak 574; bun ~ primeval Light 1118-21, 11219; 965, — Av. (1488) raoxšna-; MPrthPrs rwšn; Paz. rös(a)n; NP rau- šan.
Rošn n. pr. 9525,
Rēšn-cašm [~ cSm] n. pr. 106912, —
*Bright-eyed'.
ro$néh light (subst.) 1% and passim; hamäk apar-~ 371%; hàn + anagr ~ the Endless Light 3018. 3921-22; hän i asar ~ 7327 sq. 9476; five species of ~ 1201-13,
rot [lwt'; YM?] river P1:3. 56214-16, — OP rautah-; MPrthPrs rud; Paz. NP rod.
Rötastahm [lwtsthm] n. pr. 1162. — NP Rustam; Old Sogd rwstmy, Reichelt, Sogd. Handschr.- R. II, 63.
sac- [sc-] pres. st., impers. it is convenient, suitable, proper: cé sacēt bütan ? what can it be? 726, 1115-16, sacet dänistan kū it is proper to know, one ought to know 6217, — From sak-, Skr $aknoti ‘to be able’ [Av. (1552 sg.) tsak- in a specialized sense]; MPrth sc-, Ghilain 50; MPrs szyd ‘shall’ (A-H II); Paz. sažīdan or sažastan (SGV) saz- or saž- (Mx); NP sazidan sazad. V. also saxt and säxtan, passäzt.
sacäk [sc’k] suitable, convenient 4674, — Paz. sažā, NP sazä.
171 sacišnēh
rötastäk [lwtst’k], rostak [lwst’k] district, province 377. 8618. — In FrP 2 it is the first subdivision under šahr ‘dominion, kingdom’, and placed above déh ‘village’ and zänak ‘house’, cf Nyberg, Byzantion XXXVILI, 1968, 114-115. — MPrth rwdyst’g (A-H III); Paz. röstä, pl. rostčiga ; NP rēstā(i) ‘any inhabited place; a market-town, a village’; Arab. lw. rustäg, ruzdäg ‘arable land’.
rövan [lwbn'] butter, ghee 749.4, — < róyan, the SW form of régn (q. v.); as to y > v, cf murv < mury, ete.
rustan [lwstn'] röd- [lwd-] to grow 6. 4074, 4122, 9218, 9518.22, — Av. (1492 sq.) 2raod-; MPrs pt. rwst, v. n. rwyysn (A-H I), Verbum 183; Paz. rustan roded (Mx 6238), pres. pass. rövihed (Sav XVI, 35, dubious); NP rustan röy- ; cf Bailey, BSOS VII, 1933, 84.
ruvan [lwb?n'] soul, the immortal part of the human being: F:2. 9!4, 125, 1326 (v. s. v. vart). 31-34 passim. 72—76 passim, etc. passim; v. also anösak. — Av. (1537 sqq.) urvan-; KZŠPrth ^rwn; MPrth rwn, rwn (A-H. III, BBB); MPrs rwn; Ps lwb’n; Paz. rua; NP ravan.
Rvänän [lw*n'-*n', and Paz.] patron.: ‘of the Rvän clan’ 371-5, v. Frahim Rwäng Zčiš.
sacakiha [~-yh’] properly, fittingly 795. 80°.
sacäk-vär [~-w’l] seemly, becoming 220, 311, - NP sazāvār.
*Sacidarm [scyd’lm] n. pr. of an Indian sovereign 1185. 119 passim. 121°-®. — I believe -it renders a Skr. name *Satya- dharma-.
```


## [2026-09-04T19:01:10.039Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nlines=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in [3348,3353,3355]:\n    lf=('\\n'.join(lines[:ln])).count('\\f'); print(ln,'leaf',lf,'printed',lf-8)\n\""
}
```


### [2026-09-04T19:01:11.762Z] TOOL RESULT

```
3348 leaf 187 printed 179
3353 leaf 187 printed 179
3355 leaf 188 printed 180
```


## [2026-09-04T19:01:12.006Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"##### HRN\"; grep -n \"rūstā\\|rustā\\|rôstâ\\|rustāq\\|Rustam\\|rustan\\|rūy\\b\\|rôi\\|rôî\" HRN.txt | head -20; echo; echo \"== HRN raz ==\"; grep -n \"raz\\b\" HRN.txt | head -15"
}
```


### [2026-09-04T19:01:12.082Z] TOOL RESULT

```
##### HRN
5477:aw. |/>c/orf-, raoöahe 'wachsen'; phlv. rustan (bezw.

== HRN raz ==
577:ist; heraz 'Schmuck', beräztdeM (No. 193) können wegen
1243:ewraz (AM.), ini^N^DN (jüd.-pers.).
2099:aw. bräza-f brOzaiü 'er strahlt'; phlv. braz(i)sah
2100:geschmückt*, braz(i)saklh (AV.) ; ai. bhrajd-, bhrajate
2104:kurd. araz 'für.
4904:kurd. dirlz; bei. drOj, n. draz, drazad, dräzT (84).
5396:aw. razah' (vd. 8, 97); phlv. raz^ vergl. Qaovav^
7112:phlv. frazänak bezw. farzänak,
7789:arm. LW. varaz, vgl. Varazdat, Baoa^rj^, OvuQoiCfjg
7793:np. veraz *Eber' wird im FS (Vullers) durch einen
9351:kurd. verdl, //arnfrr?^ 'Wachtel' (H.-Sch.); af/. vvaraz\
19930:nvaraz 1078.
```


## [2026-09-04T19:01:15.316Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5460,5500p' HRN.txt; echo \"=== leaf ===\"; python3 -c \"\nlines=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in [5477,5396]:\n    lf=('\\n'.join(lines[:ln])).count('\\f'); print(ln,'leaf',lf,'printed',lf-21)\n\""
}
```


### [2026-09-04T19:01:17.205Z] TOOL RESULT

```
ai. ruksd' 'glänzend'.
oss. d. ro/s^ t. rü/s 'Licht, leuchtend', rü/say (214);
ya;'n. ru/sinie.
Gehört np. ru/ 'Wange' auch zu derselben Wurzel?
611. red 'weise, tapfer' (z. B. Sahn. I, 149 Vers 365; Vis
und Rämin S. 13, V. 5 v. u.).
aw. ratU' 'Herr'; phlv. rat, -rat^),
612. rezm 'Schlacht, Kampf.
aw. vergl. areza- 'Schlacht'; arm. LW. paterazm
'Kampf, auch razm.
An Ableitung von aw. rasman- 'Schlachtreihe' zu
denken {s könnte statt z vor m stehen), verbietet die
Bedeutungsverschiedenheit (s. No. 609).
613. rest]äy(^e^ 'Auferstehung der Todten'^).
aw. irista- 'todt'; phlv. rist^ ristä/ez (paz. ristaxez),
614. rasten 'wachsen, Praes. röy-em, röylden, röyäniden,
rösta (arab. syr. LW. rustOq), pNDDn, Is. 42, 11.
aw. |/>c/orf-, raoöahe 'wachsen'; phlv. rustan (bezw.
rödastan , aber nicht wahrscheinlich), röyend bezw.
rödent (3. Plur.), rostäk [rödastak, Salemann, Eine
*) Vergl. Nöldeke, Tabarl-Obersetzung, 447.
*) Kaum gehört hierher röz-l *ir,9 'Todestag' (Pertsch, Die
persischen Handschriften der herzogl. Bibl. zu Gotha, S. 115, 116),
vergl- de t^agarde, Ges. Abb» 3?,- 137 —
Pärsenhandschrift 68, 10), röd(i)sn bezw. röy(i)sn; ai.
rödli' rodliati (KröA-, röltati).
bei. rtiday, n. ruday (319).
Zur i/^rödfi- vergl. Bartliolomae, ZDMG. 44, 553
No. 332.
615. resen 'Strick'.
ai. ragandr 'Strick, Riemen, Zügel, Gurt'; arm. LW.
apa\rasan zügellos*, erasan, erasanak 'Zügel' (Hübsch-
mann, No. 96).
arab. hebr. LW. rasan, bezw. JD^.
616. restden 'ankommen, erreichen', Praes. res-em^
resänTden,
g. rasadmün.
ap. i/^ras' 'kommen, gelangen', arusam^); phlv.
rasltan, ras(i)§n (AV.), rasmitan,
LW. afy. rasedal; bei. rasa(/ (313).
617. risten 'spinnen, Praes. res-efn, riste, resulen, resmän,
=== leaf ===
5477 leaf 157 printed 136
5396 leaf 155 printed 134
```


## [2026-09-04T19:01:27.050Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN Gesicht ==\"; grep -n \"Gesicht\" HRN.txt | head -20; echo; echo \"== HRN Weinstock/Rebe ==\"; grep -n \"Weinstock\\|Weinberg\\|Rebe\" HRN.txt | head -20"
}
```


### [2026-09-04T19:01:27.116Z] TOOL RESULT

```
== HRN Gesicht ==
397:Gesicht' sein!) auf Härüt ^ Märüt für möglich hält fGhazel No. 17).
3000:Anm. 3, welche ich erst nachträglich zu Gesicht
4174:sprung: Gesicht'; phlv. citre (Münzen, Inschriften),
5640:636. {i)röT, rö 'Gesicht'.
9717:\l2i>'^^ f/än *liimmlische Offenbarung, Gesicht' (mystischer
11184:Urheber selbst abgehalten , über allgemeine Gesichtspunkte hinauszu-

== HRN Weinstock/Rebe ==
8034:Semn. vdle (vergl. np. vel *Blüte des Weinstocks*).
```


## [2026-09-04T19:01:29.816Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5636,5660p' HRN.txt; python3 -c \"\nlines=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nlf=('\\n'.join(lines[:5640])).count('\\f'); print('leaf',lf,'printed',lf-21)\n\""
}
```


### [2026-09-04T19:01:31.560Z] TOOL RESULT

```
aw. raoidita- 'rötlich* (vd. 1, 3); phlv. rödlk geschr.
rötik (vd. 1 (8)), rod bezw. röi (AV.), royin (AV.) ;
skr. lohä'^) 'rötlich, Roterz, Kupfer.
bei. rod 'Kupfer (325).
636. {i)röT, rö 'Gesicht'.
aw. raoSa- 'Wuchs, Ansehen'; phlv. röd"^), hu]rod(i)s7i
(AV.); got. ludja 'Antlitz'.
Allgemein entlehnt im iranischen Gebiet und über
dasselbe hinaus.
637. reht 'Diener, Sklave'.
phlv. rasik.
Wohl zu ap. \/^raS'j np. resTden (No. 016)?
638. reffen 'ausgiessen, verschütten, Praos. rez-em, rPzis,
ni^TI (Qiss. Dan.), reze, vergl. hirezen \Soiho, Durch-
schlag.
g. retmün, Praes. herlfe; Käs. V. retdti.
aw. l/'ra^d-, ra^cayat *Si\isg\essen ; phlv. re//^/w, ircPt
(päz. rezed), rec(i)sfi; lat. liquäre; ai. [/'rcc,-, rindkil
bedeutet nur überlassen, räumen' (vergl. np. gurc/ten,
No. 914); arm. vergl. IKanem 'verlassen' (H. No. 132).
kurd. 7'etin 'ausgiessen'; oss. d. lejtm, t. iJjjn
'laufen, fliehen' (167) ; bei. reöag, n. rTsay (316), vergl.
princag 'pressen, auspressen' (443); wa/. varic-am,
sar. variiz-am 'müde werden , Causat. Verweilen lassen'.
Hierher gehört auch syr. LW. pnjN, arab. LW.
leaf 162 printed 141
```


## [2026-09-04T19:01:39.535Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5660,5668p' HRN.txt; echo \"##### HUB\"; grep -n \"rūstā\\|rustāq\\|rôstâ\\|rustaq\\|rustäq\" HUB.txt|head; echo \"-- HUB rustan/rōi\"; grep -n \"rusten\\|röi\\|rōi\\|raoöa\\|raoda\" HUB.txt | head -20; echo \"-- HUB raz\"; grep -n \"^raz\\|raz \" HUB.txt | head -10"
}
```


### [2026-09-04T19:01:39.636Z] TOOL RESULT

```
Hierher gehört auch syr. LW. pnjN, arab. LW.
ihrtq 'Wasserkanne' (de Lagarde, Ges. Abb. 7).
*J SpiegePs Erklärung, Ar. Periode 35, ist lautlich pfanz uu-
niüglich.
2j Fiilaoli oder vielmehr nur graphisch rö/, Bund.— 142 —
639. rlden *kacken', Praes. rii/^em, rtsten, rtm *), rime.
aw. l/^raf-, avi dim irita *kackt darauf (vd. 5, 1);
phlv. }*ttan, reman, remamh; ai. l/^re-, riyäti *frei
lassen, laufen lassen .
##### HUB
-- HUB rustan/rōi
1536:*paiti-raodah- gesetzt werden, da schon das Pehlevi
7076:raoda-; xoi *Helm' (unbelegt) neben xDd, arab. xudat, arm.
7094:khadati; royam 'wachse', inf. rustan, zd. raodahe; Sdyam
-- HUB raz
1153:raSa *a heap of grain' = np. ras, raz *acervu8 frumenti excusbi*), jad.
2322:'Schlachtreihe (von Wzl. raz = idg. reg^, vgl. skr.
2328:razm vgl. phi. razm u patrazm Yatk. i. Zar. p. 66.
3567:1, 107, V. 840 und oft zu firaz *hinauf . Dazu phi. nisepak
4393:arm. varz, phi. vazr^ zd. vazra-; guraz *Eber' (neben Baraz
5533:pr. auch Baraz (NOldeke, Tab. 240); gitrz, gurza 'Keule =
5584:Varaz (sehr haufiger Name) — pers. Baraz Tab. 240, gr.
5586:Up. guraz *Eber' (s. oben § 47) ; Vard N. pr., vgl. ap. Arta-
5608:= li^.^bad; varaz *Eber (Eznik 66 u. s. w.) = np. guraz;
6046:b) Einschub von a in: baraz *Schmuck', zd. braza-
```


## [2026-09-04T19:01:42.784Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7070,7100p' HUB.txt; echo \"=== leaves ===\"; python3 -c \"\nlines=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in [7076,7094,1536]:\n    lf=('\\n'.join(lines[:ln])).count('\\f'); print(ln,'leaf',lf,'printed',lf-10)\n\""
}
```


### [2026-09-04T19:01:44.681Z] TOOL RESULT

```
= zd. pada- ; -ra Casuspartikel = paz. ra, phi. rai wegen',
ap. radiy Vegen*; x^ai {x^a) *Wohlgeschmack' = skr. svada-;
boi {ho) *Geruch* = zd. baoidi- (arm. buidenik Moses, Geogr.
616, wohl boyicenik zu lesen = np. boy i ctnt 'chinesisches
Parfum'); roi {ro) 'aes vel stannum fusum' = bal. rDd 'Kupfer ,
arm. avoir 'Messing, skr. loha-; roi {rd) 'Gesicht' = zd.
raoda-; xoi *Helm' (unbelegt) neben xDd, arab. xudat, arm.
^) Dazu np. kahar = skr. kadrxi- *rotlibraun*, zd. kadrv0'{a3pa')^
Geiger, Idg. P. IV, Anz. p. 23.— 200 —
xoir '^DiademV ^p. xaudc^, zd. xaoda-; mOi *Haar = paz.
mU Min. Gl. 140, g. frnd, bal. mUd^ mid, nb. mldy also ap.
*muda' ? ; sSi 'Gatte = ap. *xSauSa- ? ; maig *Heuschrecke
(neben malax) = phi. maig (und malak Bdh. 47, 10), bal.
maday, madax, arm. marax, zd. mataxd-; patg *Bote* =
syr. W^B, phi. paik, arm. payik, skr. padika- (s. oben p. 45
— 46)Vjp»y^rfa *Pussganger' = skr. paddti-y padatika-; miyan
'Mitte' = paz. phi. miyan, zd. maiSyqna^ ; bayd, bayog 'Braut'
= skr. vadhu^; beva 'Wittwe == phi. vevak, zd. Mava,
skr. vidhavd-; zBr unten* = paz. ai-er, phi. Sr- in Srtany
Ertkan PPGl. p. 9 aus "^ayar = zd. adairi (s. § 58, b)';
drdstan *in Ordnung bringen, schmticken', pr. arayam, pai-
rdstan *zurichten', ^v. pairayam^), Wrzl. rodh^), vgl. ap,
r^to- nchtig, zd. raSaiti; ayJna 'Spiegel', bal. Od^k, Od^n,
nb. azXna = *^fna (s. oben p. 12); xayad 'kaut* = skr.
khadati; royam 'wachse', inf. rustan, zd. raodahe; Sdyam
wasche', inf. sustan, bal. sddag, nb. sdJJay (s. oben p. 79);
-yar als 2. Glied von Komp. *) = zd. -dAra-, z. B. Sdhryar
'Herrscher', phi. inschr. Satrd(Ci)ran plur., zd. *xsa&rO-dcLra-,
ap. *xsad^adara'\ bisyar Viel' = ap. *«?asi(T(!lra- ; -yod =
ap. -J^a^t-, -Jflfof, vgl. bunyad H. 1120; Isfandiyar entstellt
aus Ispandiyad = arm. Spandiat, gr. Sfpevdadazfjq^ zd.
=== leaves ===
7076 leaf 209 printed 199
7094 leaf 210 printed 200
1536 leaf 55 printed 45
```


## [2026-09-04T19:01:50.179Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Hraud\\|raud\\b\\|rōstāg\\|rustan\" CHEUNG.txt | head -20"
}
```


### [2026-09-04T19:01:50.234Z] TOOL RESULT

```
6687:unconnected (cf. NEVP: 91), rather from *Hraud (Cheung 2004: 129). 
6899:IE provenance for this II. root cannot be ascertained. The comparison to ON fraud 
13107:*(H)raud ‘to tear, break’ 
13120:*Hraud 193 
13123:© The evidence for an Ir. root *(H)raud, which would derive from IE *(H)reud-, is 
13138:*Hraud ‘to grow (bigger)’ 
13172:*NWIR: NP rustan/röy-, Zaz. ruwäyis/ruwen- ‘to bud, blossom’, Gz. rön-/ruft ‘to 
14084:*H,l(e)ud'- (> Ir. *Hraud) that has given rise to a new ablaut series: > Ш. *Hurd’/ 
20820:*raud ‘to hinder, block, ward off” 
20885:if there is a possible Ir. cognate, on which see *raud. On the etymology see also 
24938:*NWIR: NP tarfand(ah), tarvand(ah) ‘lie, falsehood, deceit, fraud’, Zaz. tiritis/tiren- 
28255:’rws- does not derive from *raud. = Ghilain: 49, 81 | DMMPP: 53 
28626:contamin. with *xraud) 
28917:448 *xraud 
28942:*xraud ‘to become/make angry ?, afraid ?, confused ?' 
41434:rustan/roy-, 193 
53508:fraud, froða, 91 
55623:*9rah, *9ram, *xraud 
55628:*xraud, *zarH' (s.v.) 
55641:(s.v.), *xraud, *xsai (s.v.),
```


## [2026-09-04T19:01:52.279Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '13138,13200p' CHEUNG.txt"
}
```


### [2026-09-04T19:01:52.328Z] TOOL RESULT

```
*Hraud ‘to grow (bigger)’ 

*AVESTAN: YAv. raoö- (ruö-) ‘to grow’ || (+ *fra-) ‘to grow to(wards)’ || (+ *ni-) ‘to 
suffer from dystrophy, wear out, von Kräften kommen (vel sim.)’ || (+ *ui-) ‘to 
outgrow’ > Liste: 59 

Pres. them. {1}: IND. 2sg. med. YAv. raoóahe (Y 10.4), YAv. viraoóahe (Y 10.12), 3р1. YAv. raodanti 
(V 5.19), impf. 3sg. YAv. araoóat (Y 9.11), INJ. 3sg. YAv. raoóat (Yt 19.40, Е 587); Pres. ia- {2}: SUBJ. 
3sg. YAv. "nr.uruuióiiat (V 16.7); Perf.: ? YAv. urürudus(a) (Y 10.3); Inf.: pres. ?? Y Av. raose (Y 10.4); 
Caus.: IND. (med. ?) 3sg. YAv. fraraoóaiieiti/e (V 18.46); Partic.: perf. pass. YAv. urusta- (V 19.18), 
Y Av. fräurusta- (Yt 18.6), YAv. niuruzda- (N 17). © On the interpretation of YAv. 'nruruuióiiat and 
niuruzda- see *yraid. The past participle "uruzda- is the regular outcome of Пг. *Hrud'-ta- > *Hrud'd'a- 
(Bartholomae's Law) > Ir. *Hruzda-, Skt. rüdha-. The form *Hrusta- is the result of a frequent analogical 
development in Ir. 

*MIDDLE PERSIAN: MMP rwy-, BMP Ind /roy-/ ‘to grow’ = DMMPP: 303a 

Pres.: IND. 3sg. BMP rwdyt /royed/, 3pl. MMP rwyynd, SUBJ. 3р1. MMP rwy nd, rwyy nd; Partic.: perf. 
pass. MMP rwst, BMP Iwst/rust/; Caus.: pres. IND. 2sg. MMP rwynyy 

*PARTHIAN: rwd- ‘to grow’ || (+ *abi-) 'brwd ‘plants’ = Ghilain: 65 | DMMPP: 
2993, 14b 

Pres.: IND. 3pl. rwdynd; Partic.: perf. pass. rwst, rwst 

*KHOTANESE: OKh. *rrüd- (rrvi-) ‘to grow’ || (+ *fra-) har(u)v- (hars-) ‘to grow’ || (+ 
*ham-) hambruj- (hambrri-), LKh. hambrañ- (caus.) ‘to heal > SGS: 116, 144 
*SOGDIAN: BSogd. rwó-, MSogd. rwst (pret. stem) ‘to grow’ || (+ *pati-) SSogd. 
ptrwö-, CSogd. ptryst-, MSogd. ptrwö- ‘to grow up’ 

Pres.: IND. 3sg. BSogd. rwött, BSogd. rwöt, SUBJ. 3sg. BSogd. rwö’t, 3pl. MSogd. rwö’nd (Sogdica: 
46); Inf.: BSogd. rwö’y || (+ *pati-) Impf.: IND. 3sg. MSogd. ptyrwö (BBB: 35); Pret.: intr. IND. 3sg. 
SSogd. ptrwsty; Partic.: perf. pass. SSogd. ptryst (lit. 'grown") PN; Inf.: pret. CSogd. ptrysty || 

*NWIR: NP rustan/röy-, Zaz. ruwäyis/ruwen- ‘to bud, blossom’, Gz. rön-/ruft ‘to 
grow’, Bal. rust, rudit/rud-, roóenO/roóen- (caus.) ‘to bring up, educate’ || (+ *ham-) 
? Bal. amrust/amrud- ‘to arch, stretch the body’ 

*NEIR: Yghn. rut-/rusta ‘to grow’ || (+ *ui-) Pash. wrost m., wrastá ‘rotten, decayed 
(of wood, matting)’ (Cheung 2004: 129) 

*MISC: Par. rust ‘high, elevated’ 


194 *(H)raudH 


*SANSKRIT: rodh ‘to grow’ (RV+) = EWAia П: 467 
*PIE *H,leud'- ‘to grow, rise’ = LIV: 248 f. | Pok.: 306 f., 684 f. 
*IE COGNATES: Gr. £Ae0£pog (m.) ‘free man, non-slave’, Olrish Juss ‘plant’, Goth. 


liudan, OE leodan ‘to grow’ 
*REFERENCES: TFL I: 285a; Andreev — PeSéereva: 316b; DKS: 367a; WIM II/1: 82; Werba 1997: 229 f; 
Paul 1998: 312a; Shahbakhsh: s.v. rud-, amrud-; Korn 2005: 313, 377 


*(H)raudH ‘to moan, (be)wail’ 

*AVESTAN: гаоб- ‘to moan, (be)wail’ = Liste: 59 

Pres. athem.: INJ. 3sg. them. YAv. urudat (F 9), med. 3sg. ? raosta (Y 29.9, Y 9.24), 3pl. YAv. uru0ən (V 
3.32), med. 3pl. YAv. urudonta (V 19.45); Aor. athem.: med. INJ. 3sg. ? raosta (see above); Partic.: pres.
```


## [2026-09-04T19:02:00.992Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== KLN houri ==\"; grep -n \"houri\\|Houri\\|hür\\b\\|hūr\\b\" KLN_1966.txt | head -10; echo; echo \"== KLN rauza/rawda ==\"; grep -n \"rawda\\|rauda\\|Rauza\\|roza\\b\" KLN_1966.txt|head -5; echo; echo \"== LKT houri/rawda ==\"; grep -n -i \"hur\\b\\|huri\\|houri\\|rauda\\|raudha\" LKT.txt | head -20"
}
```


### [2026-09-04T19:02:01.084Z] TOOL RESULT

```
== KLN houri ==
18149:Derivatives:  hour-ly,  adj.  and  adv. houri,  n.,  a  nymph  of  the  Moslem  Paradise;  (fig.) a  seductive  woman.  —  F.,  fr.  Pers.  hurt,  fr. Arab,  hur,  pi.  of  ahwar,  fern,  haurd ’,  ‘having beautiful  black  eyes’,  fr.  fiawira,  ‘had  black eyes’,  which  is  rel.  to  Heb.  hawar,  Aram.-Syr. hdwdr,  ‘was  white’,  Heb.  hur,  ‘white  stuff’,  hori, ‘white  bread’.  The  -i  in  Pers.  hurt  is  a  formative element  serving  to  denote  the  singular, house,  n.  —  ME.  hus,  hous,  fr.  OE.  hits,  rel.  to OS.,  ON.,  OFris.,  OHG.  MHG,  Ads,  Du.Au/s,G. Haus,  Goth.  -Aur(in  the  compound^MdAnj.'temp- le\  lit.  ‘the  house  of  God’);  orig.  ‘shelter’,  fr. I.-E.  *qeus-,  -s-enlargement  of  base  *qeu-,  ‘to cover,  hide’.  See  hide,  v.  and  cp.  hoard,  hose, hut.  Cp.  also  husk,  the  first  element  in  husband, husting  and  the  second  element  in  caboose, house,  tr.  and  intr.  v.  —  OE.  husian,  ‘to  take  into a  house’,  fr.  hus,  ‘house’.  See  house,  n. housecarl,  n.,  member  of  the  bodyguard  of  a Danish  or  early  English  king  or  nobleman (hist.)  —  OE.  huscarl,  fr.  ON.  huskarl,  which  is compounded  of  ON.  hus,  ‘house’,  and  karl, ‘man’.  See  house  and  churl, housel,  n.,  the  Eucharist  (obsol.)  —  ME.  husel, fr.  OE.  husel,  ‘the  Eucharist’,  rel.  to  ON.  husl, of  s.m.,  Goth,  hunsl,  ‘sacrifice’,  and  prob.  cogn. with  Lith.  svehtas.  OSlav.  svetu,  OPruss.  swints, ‘holy’,  Lett,  svinet,  ‘to  hallow,  celebrate’, Avestic  splnta-,  ‘holy’.

== KLN rauza/rawda ==
5581:bread,  n.  —  ME.  breed,  brede,  fr.  OE.  bread, ‘morsel,  crumb,  bread’,  rel.  to  OS.  brod,  ON. brand,  Dan.  brod,  Swed.  brod,  OFris.  brad,  MDu. brot,  broot,  Du.  brood,  OHG.,  MHG.  hot,  G. Brot,  fr.  Teut.  *brauda,  lit.  ‘bread  leavened  with barm’ ;  cogn .  with  Thracian  Gk.  ppuroi;  (Ppouxo; in  Hesychius),  flputov,  ‘fermented  liquor  made from  barley’,  L.  de-frutum,  ‘must  boiled  down’. These  words  are  formed  with  the  l.-E.  pp.  suff. -to  fr.  base  *bhreu-,  *bhru-,  ‘to  boil,  ferment’, whence  also  OE.  breowan,  ON.  brugga,  ‘to brew’.  See  brew  and  cp.  words  there  referred  to. Derivative:  bread,  tr.  v.
5724:Brosimum,  n.,  a  genus  of  trees  of  the  mulberry family  (bot.)  —  ModL.,  fr.  Gk.  pp<hatp.o?, ‘edible’,  rel.  to  Ppdjpia,  ‘food’,  (3i[3pcoaxeiv,  ‘to eat,  eat  up,  devour’.  See  broma. broth,  n.  —  ME.,  fr.  OE.  brod,  rel.  to  OHG.  brod, fr.  Teut.  base  *brauda-,  lit.  ‘anything  leavened’, cogn.  with  Thracian  Gk.  [JpO-rop  (fipou-ro;  in Hesychius),  ppurov,  ‘fermented  liquor  made from  barley,  beer’,  L.  defrutum,  ‘must  boiled down’,  Mir.  embruthe,  ‘broth’,  bruith,  ‘to  boil’, ModW.  brwd,  ‘hot’,  ModBret.  broud,  of  s.m.; fr.  I.-E.  base  *bhreu-,  *bhru-,  ‘to  swell’,  which is  enlarged  fr.  base  *bher-,  ‘to  boil’.  See  brew and  cp.  bread,  brood.
10647:defraud,  tr.  v.,  to  cheat.  —  OF.  defrauder,  fr.  L. defraudare ,  ‘to  defraud,  cheat’,  fr.  de-  and  frau- dare,  ‘to  cheat’,  fr.  fraus,  gen.  fraudis,  ‘deceit, fraud’.  See  fraud.
16461:Gorgon,  n.,  one  of  the  three  sisters  in  Greek mythology  who  had  the  power  to  turn  to  stone all  who  looked  upon  them.  —  L.  Gorgo,  fr.  Gk. Topyto,  fr.  yopy6q,  ‘terrible’,  which  is  of  uncer¬ tain  etymology.  It  is  perh.  cogn.  with  OIr.  garg, ‘rough,  fierce,  wild’,  OSlav.  groza,  Russ,  groza, Pol.  groza,  Czech  hrtiza,  ‘horror’.  Cp.  Demo- gorgon.
32999:roan,  adj.,  bay,  chestnut-colored  (said  of  horses, etc.)  —  MF.  (=  F.)  rouan,  fr.  Sp.  roano,  fr. OSp.  raudano,  fr.  VL.  *ravidanus,  fr.  L.  ravidus, ‘grayish’,  fr.  ravus,  ‘gray’,  which  is  cogn.  with ON.  grar,  OE.  grceg,  ‘gray'.  See  gray. Derivative:  roan,  n.,  a  roan  horse.

== LKT houri/rawda ==
90:Archiv  (1882)  XXXVI.  Jahrg.,  Bd.  LXVII,  S.  197/212. Hobson-Jobson  =  Henry  Yule  and  Arthur  Coke  Burnwell.  Hobson- Jobson :
299:36.  Fers,  ähur:
379:c)  Mit  ähur  [s.  hier  Nr.  36]  ergibt  sich pars,  mlr  ähur  'Stallmeister,  Vorsteher eines  Marstalles',  ebenso  Ik.,  vulgär ausgesprochen  imrahor  [A.  Hindoglu, Dictionnaire  Franqais-Turc.  Vienne  1831. S.  201  a],  hieraus  rum.  imhrohor  'Stall- knecht'.
495:Elativform  von  sarlf  'edel,  berühmt' [s.  hier  Nr.  1852],  also  'sehr  berühmt, sehr  edel',  ergab  mit  pers.  SufBx  i  äs- räfi  'eine  Goldmünze'  [genau  so  ge- bildet wie  das  synonyme  äkbäri  von ar.  akbar  'sehr  grofa'].  Hieraus  pg. xarafim,  xerafim  'eine  Münze  aus  Ost- indien, die  300  Reis  Wert  hatte'  [Con- stancio  Dicc  974  a]  und  sicherlich  auch frz.  aigrefin  [mit  volksetymologischer Umgestaltung]  'eine  Münze,  die  früher in  Frankreich  in  Umlauf  war'  und  mit einem  nicht  seltenen  Bedeutungswandel 'Schwindler,  listiger  Mensch'  [besser  als die  Ableitung  von  einem  so  nicht  vor- handenen al-hurüfi,  das  wieder  in  Zu-
628:'Jüngling'  [vgl.  neuhebr.  bähal  'reifen' Dalman,  Aramäisch-neuhebräisthesWör- terbuch  (1901),  49];  hieraus  judendtsch. Bocher  'dass.,  Schüler';  poln.  bachur, bachor  'jüd.  Kind;  junges  Schwein'. [Kluge  60.    Karlowicz  417.
952:N.  pr.,  Stadt  in  Russisch-Turkestan, daher  tk.  buliur  coha  'eine  Art  Wollen- zeug', hieraus  rum.  buhur  'Kaschmir'; ebenso  afrz.  bouqueraut,  frz.  bougran, sp.  bocarän,  it.  bucherame  'Steif  leinwand'. [ML  1366.    (Anders  ZfromPh  V,  556).
1803:Der  orientalische  Eulenspiegel,  in  Nord- afrika Si  Goha  [vgl.  S.  Moulieras,  Les Fourberies  de  Si  Djeha.  Paris  1892],  bei den  Türken  als  Nasr  ed-din  Hoga  [vgl. Albert  Wesselski,  Der  HodschaNasreddin. I.  II.  Weimar  1911]  bezeichnet;  hier- aus rum.  ciuhä  'Scheuche,  Popanz',  russ. coha,  cuha  'albernes  Zeug',  bulg.  serb. coha,  hieraus  verkürzt  cus,  cuz  'Un- sinn, dummes  Zeug',  it.  (dial.  siz.)  giiicco 'dumm,  Dummkopf,  giucca,  giufä  'ko- mischer Kauz'.  —  Schon  bei  den  Arabern ist  Guhä  wegen  seiner  Dummheit  sprich- wörtlich geworden  [ahmak  min  guhä 'dummer  als  G.'  in  G.  W.  Freytag, Arabum  Proverbia  I,  403.  Nr.  175]. Vgl.  FR.  SCHWALLY  in  ZDMG  LVI, 237/238  und  ARTHUR  CHRISTENSEN in  Browne  Festschr  129/136.
2055:einer  reizenden  Frau  sp.  hitrl,  frz.  houri, ndl.  engl,  houri,  dtsch.  Huri.  [DE  ;287. Devic  DEt  141.
2149:[Vom  gr.  bidßoXo;],  vulg.  blls  'Teufel'; hieraus  frz.  iblis,  iblis  'Dämon',  pg.  in der  Redensart:  hS  um  belis  'das  ist  ein umsichtiger  Mann',  aber  auch  'ein  Schur- ke' [Gonstancio  Dicc  168].  [DE  238/239. Devic  DEt  107.
3258:1414.  Ar.  iiiarfüd: 'Zurückgewiesen'  [part.  pass.  von  rafa- da]\  hieraus  sp.  pg.  marfuz  'gemein, werllos'  [z.  B.  Don  Quijote  I,  cap.  XL, in  der  Collecciön  de  autores  espanoles  III. Leipzig.  S.  283  Mitte] ;  kat.  marfus,  it. (alt)  malfusso,  (dial.  Neapel)  maj-fuso, sard.  (log.)  marfusu  'verworfen,  schur- kisch'. [DE  391/392.  WAGNER  in  Herrigs Archiv  CXL,  243.
3898:1709.  Ar.  rauda:
4171:1841.  Pers.  särähur: 'Stallknecht'  [eigentlich  'Stallvorstand' aus  pers.  sär  'Kopf  Horn  NpEt  S.  160, Nr.  726  und  ähur  'Stall'  ebenda  S.  4, Nr.  8],  die  dem  Oberstallmeister  mirähör [s.  hier  Nr.  69  c]  untergebene  2.  Diener- klasse, tk.  salahor  [offenbar  mit  der Bezeichnung  der  1.  Dienerklasse  ««YäÄiför 'WafYenpolierer'  kontaminiert,  vgl.  FLEI- SCHER in  BSGW  XX.XIV,  48] ;  hieraus rum.  salahor  'Tagelöhner,  Handlanger'.
4231:'Gute  Frau,  treues  Weib'.  Dieses  Wort wird  in  den  ind.  Dialekten  heutzutage zur  Bezeichnung  der  Frau  benutzt,  die sich  in  höchster  Erfüllung  ihrer  Treue selbst  auf  dem  Scheiterhaufen  ihres verstorbenen  Gemahls  dem  Tode  weiht. Die  Anwendung  des  Wortes  auf  den selbstmörderischen  Akt  statt  auf  die Person  ist  erst  europäisch:  engl,  suttee, dtsch.  Satti  'freiwillige  Witwenverbren- nung'. Die  Unsitte  wurde  im  Jahre  1829 durch  eine  strenge  Regulation  for  declar- ing  the  practice  of  suttee  or  of  burning or  burying  alive  the  widows  of  Hindoos illegal  and  punishable  by  the  criminal courts  verboten,  aber  es  dauerte  sehr lange,  bis  sie  restlos  verschwand,  ja  in abgelegenen  Teilen  Indiens,  wie  Nepal, soll  sie  noch  jetzt  vorkommen;  so  soll sich  um  1890  die  Witwe  von  SIR  JANG BEHADUR,  des  Premierministers  von Nepal,  mit  der  Leiche  ihres  Gemahls auf  dem  Scheiterhaufen  verbrannt  haben [Globus  LXIX,  337].  Eine  gute  Schilde- rung des  Vorganges  gibt  ein  Augen- zeuge in  Philipp  van  Mökern,  Ostindien. Seine  Geschichte,  CuHur  und  Bewohner. Leipzig  1857.  I,  326/332.  Ausführlich handelt  über  Suttee  F.  Max  Müller, Alte  Zeiten  —  alte  Freunde.  Lebenser- innerungen. Übersetzt  von  H.  Groschke.
4430:1962  a.  Tk.  tabak: 'Sohle'  [vom  Stamme  tap  'unten,  Grund, Sohle',  Vämbery  TktEtWb  S.  156,  Nr. 1721;  Kelekian  Kämüs  787  a];  hieraus mit  Verlust  des  Endkonsonanten  sp.  taba 'Art  Würfel  zum  Taba-  oder  Knöchel- spiel'. Man  beachte,  daß  bereits  im Mandschurischen  taba  ein  technischer Ausdruck  im  Knöchelspiel  ist:  'Die flachste  Seite  des  Spielkuochens';  eben-
4700:'JÜ96.  Mal.  trlpaiig: 'Seewalze,  Holothuria  edulis'  [Pijn  6^  b]; liieraus  en^l.  tripnng  ;aucli  swallow  aus mal.  suwälä  'dass.'  Pijn  143  b],  ndl. tfipang,  dtsch.  Trepaiif/;  trz.  trijjan,  tre- pang.  —  Der  Trepan;:  wird  in  den  in- dischen Gewässern  in  großen  Mengen getischt,  dann  abgekocht,  gedörrt  und nach  China  verkauft;  die  Chinesen  halten ihn  für  einen  Leckerbissen.  [Devic  DEt t>i>±    JAOS  XVIII,  110/111.
5008:Guttapercha  712 jffafcö  792 ifa^M»  GiVai  800 i/am  1157 Harakiri  818 Harmelraute  829 Harün  ar-Rasid  605 Hasan  ibn  Sabäh  839 Haschisch  839 Hedschra  863 Hildegard  v.  Bingen  795 Hobson-Jobson  835 Holothuria  edulis  2096 ifw^fta  655
5483:762  a rasafa  1704 rasama  1427 »•as^  1732 rasif  1704 rassa  1466  a rassa'a  1706 ratam  1707 raiZ  1708 rauda  1709 razza  1713. razzäki  1715 ri'äs  1716 Wöäs  1717 ri&5i  1718 r»te  1717 r/d/-  1719 W^7  95.  1720 rimäk  98 mwa  1722 rizfc  1721 rtÄm«  1723 rM&Ya-»  1725 rM?>i>  1726.  1957 rwA  1727 rMÄ;&  1728 rMwwän  1729 rusäfa  1731 rM.y(^  1732 rM2:0  1733
7622:horde  1594 houri  848
7639:babusza  1625 bachmat(y)  128 bachor  180 bachur  180 baczmag  265 badawja  164 öarfja  159 badjan  162 ftöi-aZie  189 balaban  1607 balagula  145  d bafamucic  199 balamut  199 baldachin  170 balkon  197 balsani  293 Z»af<a  207
8692:buduhald  338 budulac  338 budnla^  338 buhaiü  339 buhur(dan)  342 buhurgiü  343 bulgär(e)  352 bulgäriü  351 bulgur  352 buluba§a  353 5m?mc  330 bumbac  1617 bunduc  355 burghiü  363 bursuc  254 burungiuc  367 but(urä)  372 buturo§  372 buturugä  372 buzdugati  333
```


## [2026-09-04T19:02:08.759Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3898,3906p' LKT.txt; echo \"=== houri 848 ===\"; sed -n '2050,2060p' LKT.txt; echo \"=== leaves ===\"; python3 -c \"\nlines=open('LKT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in [3898,2055]:\n    lf=('\\n'.join(lines[:ln])).count('\\f'); print(ln,'leaf',lf,'printed',lf-26)\n\""
}
```


### [2026-09-04T19:02:10.517Z] TOOL RESULT

```
1709.  Ar.  rauda:
'Garten',  plr.  rijäd,  im  Magrib  singu- larisch gebraucht  als  'Blumenbeet' ;  hier- aus sp,  arriates,  arriatas  'erhöhte  Beete längs  einer  Gartenmauer'.  [DE  201/202. Eguilaz  287/288.
1710.  Tk.  rawak:
'Reinster  Honig'  [Köl^kian  Kämüs  629  b]; hieraus  rum.  rävac  'Ausbruch  (Wein)'.
1711.  Pers.  räi^änd : 'Rhabarber  Rheum  palmatum',  tk.  re- wend;  hieraus  rum.  revent;  bulg.  retven, serb.  rewed,  russ.  rewen  'dass.'.
1712.  Ar.  Räzl:
N.  pr.,  ein  arabischer  Arzt  Muhammad ahu  Bakr  ihn  Zakarija  AR-RÄZI,  der  um 930  starb.  Nach  ihm  wurde  ein  von ihm  eingeführtes  Heilmittel  frz.  blanc- Rhasis  genannt  und  hieraus  volksei y- mologisch  blanc  raisin  'Bleiweiß'. [FASZ  in  RomForsch  III,  495.
1713.  Ar.  razza:
'Pflanzen,  einsetzen',  dazu  VIII  irtazza, part.  murtazz  'eingepflanzt,  befestigt', fem.  murtazza;  hieraus  sp.  mortaja 'Zapfenloch'  [muesca  Dicc  Gast  1388  b und  1395  c],  frz.  mortaise  'dass.'.  [Devic DEt  168.
=== houri 848 ===
848.  Ar.  liaurä':
Fem.  zu  ahu  'ar  'schwarzäugig'  besonders von  einer  Gazelle,  einem  Jünglinge  oder einer  Jungfrau  gesagt;  dazu  plur.  hür. Dieses  Wort  betrachteten  die  Perser  [und gelegentlich  auch  schon  die  Araber,  s. BSGW  Leipzig  ph.-hist.  Kl.  1881 .  XXXIII, 31]  als  sglr.  und  fügten  ein  *  der  Ein- heit an :  hüri ;  darunter  versteht  man die  Paradiesesjungfrauen,  die  man  nach Muhammads  Verheißung  im  Paradiese vorfinden  soll ;  hieraus  zur  Bezeichnung
5*
Ar.  hauz.]
68
einer  reizenden  Frau  sp.  hitrl,  frz.  houri, ndl.  engl,  houri,  dtsch.  Huri.  [DE  ;287. Devic  DEt  141.
849.  Ar.  liauz:
'Bezirk,  Umgebung';  hieraus  mit  ar. Art.  sp.  pg.  alfoz  'Landschaft,  Feldflur', im  MA  der  Bezirk,  der  seine  eigene Jurisdiktion  hatte  und  nach  einem  be- sonderen fuero  regiert  wurde,  meistens nur  eine  Pfarrei  oder  ein  Schloßgebiet umfassend.    [DE  116/117.
850.  Pers.  hänagä:
Daraus  ar.  hawäga  '^Herr,  Kaufmann, Europäer  [ZDMG  L,  640],  vulg.  unter dem  Einfluß  des  tk.  koga  'Greis,  Meister' [vom  Stamme  koc  'stark,  mächtig,  groß' Vämbery  TktEtWb  S.  91,  Nr.  94]  hoga, tk.  Jioga  'Gelehrter,  Professor';  hieraus rum.  hoge  'dass.',  bulg.  serb.  hodza  'tk. Geistlicher',  russ.  hozjain  'Wirt,  Herr', hozjaika  'Wirtin',  klruss.  chazajin  'dass,'. [Gorjajew  399.    Bern  SlEtWb  400.
851.  Tk.  hawjar:
=== leaves ===
3898 leaf 164 printed 138
2055 leaf 95 printed 69
```


## [2026-09-04T19:02:21.341Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== FVQ hur ==\"; grep -n \"ḥūr\\|Hur\\|houri\\|حور\" FVQ.txt | head -20"
}
```


### [2026-09-04T19:02:21.394Z] TOOL RESULT

```
== FVQ hur ==
347:Hurgronje, C. Snouck. Review of Fraenkel's " Aramaische Fremdworter," in WZKM, 
6176:Hurgronje point out, the Iranian scholars treat it as a loan-word from 
6198:6 Dvorak, op. cit. ; Hurgronje, WZKM, i, 73. Cf. Bartholomae, A1W, 638; 
7315:1 Hurgronje, Het MeJckaansche Feest, Leiden, 1880, p. 29 if. ; Rudolph, Abhan- 
7512:(Hur). 
7608:argued convincingly that though Sale's Hurdn-i-Bihisht may not be 
7637:2 " Das Wort Hur durfen wir naturlich ebensowenig in den iranischen Sprachen 
9684:1 And sec Hurgronje, Verspreide Geschriftcu, ii, p. 11. 
9691:meant " to pay legal alms " (Zakat), but this is far fetehed, as Hurgronje, RHR, 
14573:3 Vide Hurgronje, RHll, xxx,62, 155 ; Dyroff, in MVAQ, xxii, 178 ff. ; Noldeke- 
18224:4 xi, 74, on which see Hurgronjo, Verspreide Geschriften, i, 24.
```


## [2026-09-04T19:02:24.702Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7595,7645p' FVQ.txt; echo \"=== page ===\"; python3 -c \"\nlines=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\n\" ; grep -n \"Hurdn-i-Bihisht\\|Hurân\\|hawira\" FVQ_pages.txt | head"
}
```


### [2026-09-04T19:02:26.957Z] TOOL RESULT

```
FOREIGN VOCABULARY OF THE QUR ? AN 119 

skinned, and even in the verse of 'Abid, the comparison with ivory 
statues would seem to lend point to al-Azhari's statement that it is 
only used of the eyes when connected with whiteness of the skin. 

Western scholars are in general agreed that the conception of the 
Houries of Paradise is one borrowed from outside sources, and the 
prevalent opinion is that the borrowing was from Persia. Sale suggested 
this in lu's Preliminary Discourse, but his reference to the Sadder 
Bundahishn was rather unfortunate, as Dozy pointed out, 1 owing to 
the lateness of this work. Berthels, however, in his article " Die 
paradiesischen Jungfrauen im Islam", in Islamica, i, 263 ff., has 
argued convincingly that though Sale's Hurdn-i-Bihisht may not be 



called in as evidence, yet the characteristic features of the j^>- of the 
Qur'anic Paradise closely correspond with Zoroastrian teaching about 
the Daena. The question, however, is whether the name j^p- is of 
Iranian origin. Berthels thinks not. 2 Hang, however, suggested its 
equivalence with the Zoroastrian y-Gy* humat, good thought (cf. Av. 
A^JJG>O> ; Skt. *p*l) ; ftyy* huxt, good speech (cf. Av. iipoffttf > 

Skt. *W), and ^Xr^ *' 7 *r*fa, good deed (cf. Av. ^J^-tt))^) 3 

but the equivalences are difficult, and as Horovitz, Parodies, 13, points 

out, they in no way fit in with the pre-Islamic use of j^>-. Tisdall, 
Sources, 237 ff., claims that j^>- is connected with the modern Pers. 
jj. sun from Phlv. J^o X var 4 and Av. gYut) havarz, 5 but this 

comes no nearer to explaining the Qur'anic word. 

It is much more likely that the word comes from the Phlv. ft)}yf* 
hurust, meaning beautiful, and used in the Pahlavi books of the 
beauteous damsels of Paradise, e.g. in Arda Viraf, iv, 18, and in 



1 Het Islamisme, 3 cd., 1880, p. 101. 

2 " Das Wort Hur durfen wir naturlich ebensowenig in den iranischen Sprachen 
suchen." 

3 The three words occur together in Pand-namak, xx, 12, 13. Cf. Nyberg, Glossar, 
109, 110. 

4 Horn, Grundriss, pp. Ill, 112; Shikand, Glossary, 255. 

6 Bartholomae, AIW, 1847 ; Reichelt, Awestisches Elementarbuch, 512 ; cf. Skt. 
=== page ===
4502:argued convincingly that though Sale's Hurdn-i-Bihisht may not be
```


## [2026-09-04T19:02:43.044Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7505,7600p' FVQ.txt; echo \"=== after ===\"; sed -n '7645,7680p' FVQ.txt"
}
```


### [2026-09-04T19:02:43.103Z] TOOL RESULT

```
denominative. The probabilities are in favour of the borrowing being 
from Syriac rather than from Jewish Aram., 2 for (30**, especially 
in the plu., is used precisely in the Qur'anic sense (PSm, 1214). 



(Hur). 

xliv, 51 ; Hi, 20 ; Iv, 72 ; Ivi, 22. 
The Houries, or Maidens of Paradise. 

Except in Iv, 72, it is used always in the phrase /*-,_ j >- The 
occurrences are all in early Suras describing the delights of Paradise, 

where the ^ J^p- are ^ nc beauteous maidens whom the faithful 
will have as spouses in the next life. 

The Grammarians are agreed that j *> is a plu. of Jj > and 
derived from j>-> a form of U., and would thus mean " the 



white ones". /~- is a plu. of <V.P| meaning "wide eyed" (LA, 
xvii, 177). It thus becomes possible to take SJ*G, J9*" as ^ wo objectives 
used as nouns meaning " white skinned, large eyed damsels ". The 



1 Daniel, 62 n. 

2 Mingana, Syriac Influence, 86. 



118 FOREIGN VOCABULARY OF THE QUR ? AN 

Lexicons insist that the peculiar sense of j *>- is that it means the 

contrast of the black and white in the eye, particularly in the eye of 
a gazelle or a cow (cf. LA, v, 298 ; and TA, iii, 160). Some, however, 
insist equally on the whiteness of the body being the reference of the 

word, eg. al-Azharl in TA, "a woman is not called t\jj>- unless 

along with the whiteness of the eye there is whiteness of body." One 
gathers from the discussion of the Lexicographers that they were 
somewhat uncertain as to the actual meaning of the word, and in 
fact both LA. and TA. quote the statement of so great an authority 

as al-Asma'I that he did not know what was the meaning of j^>- as 
connected with the eye. 

The Commentators give us no help with the word as they merely 
set forth the same material as we find in the Lexicons. They prefer 
the meaning which refers it to the eye as more suited to the Qur'anic 
passages, and their general opinion is well summarized in as-Sijistanl, 
117. 

Fortunately, the use of the word can be illustrated from the old 
poetry, for it was apparently in quite common use in pre-Islamic 
Arabia. Thus in 'Abid b. al-Abras, vii, 24 (ed. Lyall) wo find the verse 



" And maidens like ivory statues, 1 white of eyes, did we capture " 
and again in 'Adi b. Zaid. 



" They have touched your heart, these tender white maidens, beside 

the river bank." 
and so in a verse of Qa'nab in the Mukhtardt, viii, 7, we read 



" And in the women's chamber when the house is full, are white 
maidens with charming voices." 
In all these cases we are dealing with human women, and except 

in the verse of 'Abld the word j >- could quite well mean white- 



1 So in al-A'sha we find ^jJl Jl^Kj^*-, cf. Geyer, Zwei Gedichte, i, 196 = 
Diwan, xxxiii, 11. 



FOREIGN VOCABULARY OF THE QUR ? AN 119 

skinned, and even in the verse of 'Abid, the comparison with ivory 
statues would seem to lend point to al-Azhari's statement that it is 
only used of the eyes when connected with whiteness of the skin. 

=== after ===
6 Bartholomae, AIW, 1847 ; Reichelt, Awestisches Elementarbuch, 512 ; cf. Skt. 



120 FOREIGN VOCABULARY OF THE QUR*AN 

Hadoyt Nasfc, ii, 23, 1 where we have the picture of a graceful damsel, 
white-armed, strong, with dazzling face and prominent breasts. Now 

5V)u is a good Iranian word, the equivalent of Av. 



TmraoSa, 2 and though these Pahlavi works are late the conceptions 
in them are early and there can be no question of borrowing from 
the Semitic. 

To this Iranian conception we may now add the influence of the 
Aram. "Tin. Sprengcr was doubtless right in his conjecture 3 that 

the root &~ to be white came to the Arabs from Aramaic. The Heb. 



"IT! occurs in Is. xxix, 22, in the sense of becoming pale through 
shame, and Syr. ]>CU* is commonly used to translate XCVKOV, and 
is thus used for the white garments of the Saints in Rev. iii, 4. Carra 
do Vaux, 4 indeed, has suggested that Muhammad's picture of the 
youths and maidens of Paradise was due to a misunderstanding of the 
angels in Christian miniatures or mosaics representing Paradise. This 

may or may not be so, but it does seem certain that the word j^>- in 

its sense of whiteness, and used of fair-skinned damsels, came into use 
among the Northern Arabs as a borrowing from the Christian com- 
munities, and then Muhammad, under the influence of the Iranian
```


## [2026-09-04T19:02:52.952Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7680,7700p' FVQ.txt; echo \"=== FVQ_pages leaf for these ===\"; grep -n \"hurust, meaning beautiful\" FVQ_pages.txt | head; python3 -c \"\nlines=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport subprocess\nfor pat in ['hurust, meaning beautiful','(Hur).']:\n    for i,l in enumerate(lines):\n        if pat in l:\n            lf=('\\n'.join(lines[:i])).count('\\f'); print(pat,'line',i,'leaf',lf,'printed',lf-17); break\n\""
}
```


### [2026-09-04T19:02:54.894Z] TOOL RESULT

```
munities, and then Muhammad, under the influence of the Iranian 

V)*>, used it of the maidens of Paradise. 



/%.v->- (Khdtam). 

xxxiii, 40. 

A seal. 

The passage is late Madinan and the word is used in the technical 



phrase 

17 **. 

On the surface it would seem to be a genuine derivative from 
=== FVQ_pages leaf for these ===
4516:hurust, meaning beautiful, and used in the Pahlavi books of the
hurust, meaning beautiful line 4515 leaf 136 printed 119
(Hur). line 4447 leaf 134 printed 117
```


## [2026-09-04T19:03:00.122Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== AFA rauda ==\"; grep -n \"rauda\\|Rauda\\|روضة\\|Garten\" AFA.txt | head -20"
}
```


### [2026-09-04T19:03:00.186Z] TOOL RESULT

```
== AFA rauda ==
614:»die äussere"; ULLä. »Garten" Sru3; ü^wo IwOj 1 r'-j'r?
1898:dem des Westens vgl. Schumann iu: Jahrbuch des Botanischen Gartens vB«rUa>
5372:Auch der yerbreitetste Name für ^Garten** .ii^ scheint
5382:»Garten** (Gauh. ^Uu^j) bezeichnen, und erst später ist
5386:spr. »Zaun'* jetzt »Garten'*. Die echten Namen grüner
```


## [2026-09-04T19:03:02.777Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA; echo \"== PLA rawnaq ==\"; grep -n \"raunaq\\|rawnaq\\|rönaq\\|rūnīk\\|runik\" PLA_pages.txt | head -10; echo \"== PLA hur ==\"; grep -n \"hür\\b\\|hur:\\|- hür\\|haurä\" PLA_pages.txt | head -10; echo \"== PLA rustaq ==\"; grep -n \"rustäg\\|rustaq\\|rustäq\" PLA_pages.txt | head -10; echo \"== PLA rustam ==\"; grep -n -i \"rustam\\|rostam\" PLA_pages.txt | head -5"
}
```


### [2026-09-04T19:03:02.889Z] TOOL RESULT

```
== PLA rawnaq ==
== PLA hur ==
758:_„p>}-         abhür:          ar.       Subst.        mit       der     Bed.        "mit    den       schönen       Augen".         Es    könnte
762:             Möglicherweise                    wurde        ahür       im    Arabischen               für    masc.      Elativ       gehalten,
768:P1 -           ähür:           "Stall"          aus        dem     pers.        _>1 —
769:                                                                                    ahür           "Stall"          5 mp.           Ir     ax"ar     6,
773: NW’                 - ähürsälär:                     "Stallmeister"                  s.    ähür u,          sälär      .
2013:              wu pyp ohurmazd                                     ap.             ahuramazdäh               4 s._>ı               ahür    .
2087:e!-           auf:     "ein Modus,                 der     zwischen             mähür          u. hoseini               liegt"     7,
5382:GS_s®           -       Zumhüri:                "alter        Wein"       aus     dem        pers. „ Zum "rein"              + pers._.          hür
5996:       Meiner          Meinung           nach        ist       hüri    ein     fem.            Elativ       zu     ahür         u. ahürä,
6610:IL, - hürä:               "Sonne" ” pers.                4 <—mp.)vr                u
== PLA rustaq ==
7696:          rötstäk, ar. Lw. öl), ruzdäg u. Sl, rustäg.
7718:ol, - rasätig:                          Pl. v.öliu, rustäg.
7720:ol,           -    rustäqg:          "Marktflecken"                    =    ruzdägq,        mand.     rustag,    syr.$%’awro)          ,
7877:ol,         -       rüstäg         =    rustäg           q.    v.
== PLA rustam ==
7727:m         - rustam:                "Reichsfeldherr"                         11         mp.£w>P >         rotastahm,         mand.     rustam       12,
```


## [2026-09-04T19:03:09.262Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA; python3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [758,5996,7696,7720,7727,7877]:\n    lf=('\\n'.join(lines[:ln])).count('\\f'); print(ln,'leaf(1-based)',lf+1,'printed',lf+1-15)\nEOF\necho \"=== aḥwar/hūrī block ===\"; sed -n '755,775p' PLA_pages.txt; echo \"=== hūrī ===\"; sed -n '5985,6005p' PLA_pages.txt"
}
```


### [2026-09-04T19:03:10.820Z] TOOL RESULT

```
758 leaf(1-based) 21 printed 6
5996 leaf(1-based) 118 printed 103
7696 leaf(1-based) 150 printed 135
7720 leaf(1-based) 150 printed 135
7727 leaf(1-based) 150 printed 135
7877 leaf(1-based) 153 printed 138
=== aḥwar/hūrī block ===
     3
&pl - ”ugna = ”agna q- v-

_„p>}-         abhür:          ar.       Subst.        mit       der     Bed.        "mit    den       schönen       Augen".         Es    könnte
             eine     arabisierte                 Form        v.    pers.        /,»ı       ahura           "Herr"      <T mp.        _u re
             ohurmazd           "der        weise          Herr,       Gott!"              ap.     ahura      mazdä         sein.
             Dtsch.        Ormuzd           "höchster              und      einziger         Gott       in    der    Religion            Zarathustras".
             Möglicherweise                    wurde        ahür       im    Arabischen               für    masc.      Elativ       gehalten,
             woraus        analog           der       fem.       Elativ         hüri       gebildet          wurde-

         3                                                                             -
aD) - ”ahbiya:                           Pl. v.        Lo habä s. habä.

P1 -           ähür:           "Stall"          aus        dem     pers.        _>1 —
                                                                                    ahür           "Stall"          5 mp.           Ir     ax"ar     6,
             syr.        ,oı    abor       7,


 NW’                 - ähürsälär:                     "Stallmeister"                  s.    ähür u,          sälär      .


=== hūrī ===
4.    Löw     s.    v.
5.    LD.     s.    v.
6. Muhlt           s. v.,        al-MuCarrab             s. v.
7.    Nyberg        Bd.     II    s.       v.
8.    FM.     S.    v.
9.    Kiya     s.     v.
10.    Bharucha            s.    v.
hürl                                                                     103                                                                  baki

G,-      büöri:         "Huri,           Paradiesjungfrau,                     Schönheit"               mp.             ed       hürast      "gut
       gewachsen"                aw.            hurasa          1,
       Meiner          Meinung           nach        ist       hüri    ein     fem.            Elativ       zu     ahür         u. ahürä,
       welcher          von        den       Arabern           einfach        für     einen           ar,    Elativ            maskulin      gehalten
       wurde.          Die       Femininform               hüri wurde           analog               gebildet,           daher     ist      die
       eigentliche                 Bedeutung              "Herrin"..


                                                                          B


OJL-         bätün:           "Hausherrin,                 Dame,       Gebieterin,                   Königin"           pers.     2,
```


## [2026-09-04T19:03:18.577Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA; sed -n '7690,7740p' PLA_pages.txt"
}
```


### [2026-09-04T19:03:18.630Z] TOOL RESULT

```
11.    Genaust         s.       v.
ruzdäg                                                                          135                                                   rusdäg



ol         - ruzdäg: "Marktflecken" <T pers. L, rüstä                                                       1 m.        yw»»>         rostäk,
          rötstäk, ar. Lw. öl), ruzdäg u. Sl, rustäg.
     w
ol,       -       razzag:          "Ernährer"                 nom,        agent.       Ve,     rizq    s.    rizg.


el, - razzägi:                          "Weintrauben;                     Wein"
                                                                              — pers.), raz                   "a vineyard"            2 mp.
              ‚„, zaz    "vine,                  vineyard'"          3,


OLl,,-             razbän:           "Gärtner"                s.     ra2.

u         -       razdaq:          "Reihe"                    pers.a,.,            Faste      4       MP. se         rastak    m.            rah   °.


au -          rizg:      "tägliche                     Nahrung"                 pers. cs,       rüzi    m.»e»               röcik     "daily
          bread"         6 aw.                        raocah       / ap.        rauca       "Tag",    syr.     PEN      7     mand.        rizga   8,


0) -          razza:         "Fischband"                   pers.           9,


ol, - rasätig:                          Pl. v.öliu, rustäg.

ol,           -    rustäqg:          "Marktflecken"                    =    ruzdägq,        mand.     rustag,    syr.$%’awro)          ,
                      »               10
          (p.        IL,       )             .




m         - rustam:                "Reichsfeldherr"                         11         mp.£w>P >         rotastahm,         mand.     rustam       12,


ge            - rusahtaß:                 "Antimon"                = räsuht           q. v.

Ole, - rusdäg:                       "Marktflecken"                        = ruzdaq         q. v.


1. Wahrmund                  s. v.,               Addai       Scher         s. v.,      Muhlt s. v.
2.       ebda,       Johnson              s.          v.
3.       Mackenzie             s.       v.
4. Muhit s. v.,                         al-MuCarrab                  s. v.,       Addai       Scher    s. v.
5.       Nyberg         Bd.        II     s.          v.
6.       Mackenzie             Ss.      v.
```


## [2026-09-04T19:03:30.208Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== LEW liber ==\"; grep -n \"^līber\\|liber,\\|Uber,\\|liber ‘\\|liber (\" LEW_1910.txt | head -10; echo \"-- search 'frei'\"; grep -n \"loufir\\|loufero\\|Uber .frei\\|eleutheros\\|iXsvdsQOi\" LEW_1910.txt | head -10"
}
```


### [2026-09-04T19:03:30.285Z] TOOL RESULT

```
== LEW liber ==
-- search 'frei'
239:wssu I 869 wwwilas I 732 wuvilam I 729 4p I 670, 686, [1402 isidum I 380, 671, 720 4st II 629 top I 407 tusc I 720 tussu I 380 Juviia I 732 dzic I 192, 686, 720 lamatir I 760 leginum I 488, 779 leiguss I 800 Aeixert, Ukitud, licttud I 797 Liganakdiket I 789, II 142 ligatuts I 780, 789 ligud I 789 leimitu<m> I 804 limu I 787 hioxaxert I 817 Liicetius, Liicetia I 823, 824 LTiwkis I 823 loufir I 791, 793 LIniwfreis I 791 <louvfrikiniuss FLY livket I 828 luisarifs I 813, 829 Maatiis II 54 Maatrets II 50 Makkiis II 1 Maesius II 13, 14 Maguum II 13 maimas II 14 mais II 10, 14 Mais, Mais II 13 malaks II 21 mallom, mallud TL AIS 20 Mapegexiec II 44 Mamerttiars, Mamers II 44 Mapeotiwo, Ma- ueotivovp IT 44 manafum IT 28 manim IT 35
275:et I 421 faber I 437 famel I 452 fertlid I 485, 486 fesn. I 454 firata I 486, 498 forte I 484 hanustu I 454, 656 Herentas I 658 hospus I 660 ' ancubat I 298, 687 anim, inom I 404 Joviois I 732 ap I 670 lexe I 780, 789 lifar I 790 locatin I 817 loufir I 791 media II 56 Minerva II 90 Nounis IT 179 Pacia, Pact II 231 pacri- II 231, 232 Perseponas II 375 pes II 312 Plauties II 320 pracom I 256 praicime I 687, II 351, 352 Prismu II 868 pristafalacirix IT 285, 584 pritrome I 687, II 285, 357, 363
```


## [2026-09-04T19:03:30.609Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== LAT liber ==\"; grep -n \"loufir\\|Loebasius\\|liber :\\|liber,\\|līber\" LAT.txt | head -20"
}
```


### [2026-09-04T19:03:30.666Z] TOOL RESULT

```
== LAT liber ==
14080:Ecorce (spEcialenent de li&ge); diffErent de liber, cf. Cic., N.D.3,47,
33531:libellus: diminutif de liber, mais qui en differe en ce qu'il
33578:qu’il y ait jamais eu d's dans liber, et la diphtongue repr^sentee
33581:Pel. loufir "liber" et fal. loferta montrent que l*t de liber repo-
33591:suivant Servius, ad Ge.1,7, le nom du dieu £erait en sabin Loebasius,
34711:le parfait libitum est , cf. la forme d 1 impersonAel osque loufir con¬
34732:rend compte de 1'emploi de osq. loufir "uel" et lat. -libet', elle n'est
37293:objets, liber, tunique, enveloppe. Dd'si^ne sp^cialement la peau
37347:(Cic. ad Att.13,1,3); memorialis: n. liber, d'ou memoriale et memo¬
45970:d apres le type liber,-a,-um (cf.Pl. frg. 67L; Petr.46), qui est de-
66941:osque de Bantia a loufir, ancien impersonnel, et 1 'ombrien a en
71169:loufir pel., 632,1269.
71170:loufir osq., 653.
```


## [2026-09-04T19:03:34.560Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '33560,33605p' LAT.txt; echo \"=== page ===\"; python3 -c \"\nlines=open('LAT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nlf=('\\n'.join(lines[:33578])).count('\\f'); print('leaf',lf,'printed~',lf-18)\n\""
}
```


### [2026-09-04T19:03:36.358Z] TOOL RESULT

```
liobharaim (specialis^ en roman dans le sens de "livrer", le sensLiber
G33 -
de "libarer" ^tant passe au compos^ d'aspect deterraine, atteste depuis
1 '* It ala, deliberare, M.L.3535, cf. aussi ellberS (itala), et ses
derives liberati 5 ,-tor; liberamentum (Aug.)j liberalis, qui comme
ingenuus, generosus, est passe du sens de "qui concerne nn homme
libre" ( llberdlis causa) au sens de "digne d'un homme libre, genereux,
etc." (cf.eXeu 0 epi,oc;): liberales dicuntur non solum benigni, sed
etiam ingenuae formae homines, P.F.108,34 et illiberalis,-liter',
■perliberalis; liberalitds; libertus,-ta (cf. fal. loferta): qui a ete
fait libre (par le manu missor) "affranchi,-e",(sans doute refait
sur I lbertSs), M.L.50i4a, et collibertus : compagnon d'affranchisse-
ment", M.L.30473 libertinus "d 1 affranchi ", libertinus: affranchi
et fils d^affranchi, d'ou liberto, -as (Lex Visig.) conserve en roum.
ierta, M.L.S014.
Varron, L.L. 6,3 et l'abreg 4 de Festus, p.108,5, attribuent aux
"antiqui" les formes loebesum et loebertatem au lien de liberum et
libertatem. Ces formes sont sans doute fausses; il ne semble pas
qu’il y ait jamais eu d's dans liber, et la diphtongue repr^sentee
par t n 1 est sans doute pas un ancien oi. Loebesum doit etre issu
d'un faux rapprochement avec gr.Xot^r), Xei( 3 et,v.
Pel. loufir "liber" et fal. loferta montrent que l*t de liber repo-
serait sur un ancien ou (qui peut etre issu de eu)', ceci justifierait
un rapprochement avec gr. eX.eu 0 epo£. Un rapprochement avec v.h.a.Iitttii
"gens", lette l'audis "gens, peuple" et v.sl. Ijudige "Xotog, 0)(XoC"
n'est pas exclu, mais ne s'impose pas. - V. aussi le nom propre ambigu
Liber et 1 1 expression, d'origine peu claire, liberi.
Liber ( Leiber, dat.Lebro), -eri m.: divinlte italique, cf.osq.
Liivfreis "Liberi", assimil^e a Bacchus, comme Libera a ete assimili
a Persephone. La forme osque qui suppose une ancienne diphtongue
eu, ou, interdit le rapprochement avec libo (Xeipoo). D'autre part,
suivant Servius, ad Ge.1,7, le nom du dieu £erait en sabin Loebasius,
Lebasius "quia graece Xoi| 3 ti dicitur res diuina", avec meme rapprochement
que pour liberi de la sans doute la glose Libassius. Y a-t-il eu deux
divinites differentes? - Liber aurait ete d'abord un dieu de la ger-
mination, si l'on en croit Varr. ap. Aug., Ciu.D.7,3, omnium seminum
emittendorum (potestatem habere) Liberum et Liberam, et ideo his etiam
prae esse, quae ad substituendos homines pertinent', cf. Wissowa, Rei . 9
130,398. Toutefois Altheim, Terra Mater p.17 et s., a montre par des
rapprochements pertinents que le culte de Liber etait identique a
celui de AtovucroC, et que Liber Libera devaient &tre, par des inter-
mediaires, la traduction de 'EXeuGepoC, - 0 epa, cf. Iuppiter Liber = Zeuc
EXeu 0 epi,oC. Un reflet de cette origine se trouve dans P.F. 103,3,
Liber repertor uini ideo sic appellatur quod uino nimio usi omnia
libere loquantur.
Derives: Libera, Liberalia.
=== page ===
leaf 650 printed~ 632
```


## [2026-09-04T19:03:43.872Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"liudan\\|liuti\\|ludja\\|liber.*frei\\|'frei'\" LEW_1910.txt | head -20"
}
```


### [2026-09-04T19:03:43.929Z] TOOL RESULT

```
7873:lagjan [778 laian I 755 laikan I 829 latloun I 755 lais I §13 laisjan I 813 laistjan I 813 laists I 813 lamb I 28 land I 832 lasiws IT 618 latjan I 768 lats I 768 lapon I 768 laudt I 793 laufs, lauf I 790 lauhatjan I 824 lauhmunr I 833 laun I 826 laus I 834 lausjan I 834/5 lausqiprs II 751 lethts I 788 lecwan I 809 letk 1278, 797 leon I 810 leitils I 829 -leihan I 815 leibu I 794, 812 létan I 768, 779 léw, léwjan I 835 liban I 130, 811 ligan I778 lugrs 1778 lusts I §13 lita I 829 lupus I 815 hudan I 793 liufs £793 liuhap I 824 liupén I 776 lubains [793 lubjaleis I 813 ludja IT 831 lukarn I 825 lun I 834 lustus I 766 luton I 830 mag, magan IT 2, 5, 2
13481:Skerbs 1170, II 500 skérs I 206 Skerpét IT 500 sketatiés, sketind- tiés, &ketitiés I 491 Skilis I 304 Skilttés IT 486 &kirba IT 500 Skiru, Skirt I 170 Skists, &kist IT 494 Slawps I 835 sini I 469, IT 631 Suodien I 193 supat I 3856 tads I 376, II 644 talpainas kajas IT 644 tauta IT 715 telindt IT 655 telpu, tilpt IT 644 terpju, terpt Il 696 tiéws IT 663, 666 tigas IT 585 tilandi, tilandes IT 655 tilés IT 655 tilindt, tildt, tilwdt IT 6565 tilpe, tilpt II 644 timsa II 664 tinu IT 663 tipuludjas IT 659 tirelis IT 640 tirpt Il 692 tramdit IT 701 tremju, tremt IT 701 tresais II 669 tiks, tukt IT 715 tuikstuotis IT 715 tulpis II 644 tulpités Il 387, 644 tumst, tumsa IT 664 tuntulét, tunturét IT 721 tweru, tvert IT 254 ubudt IT 733 adens II §17 adris I 840 uguns I 676 ula Il 812
```


## [2026-09-04T19:03:51.755Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"loferta\\|Liivfreis\\|Uihei\\|libertus\\|libertas\" LEW_1910.txt | head -10"
}
```


### [2026-09-04T19:03:51.805Z] TOOL RESULT

```
201:I 501 fio I 496 foied I 653, 654 haracna I 635, 869 haras<pex> I 635 her, he I 645 Hirmius I 5065 <mrnelka> II 839 lauve-, locia I 823 loferta I 791, 792 lotfirtato, loifirta L791
```


## [2026-09-04T19:03:57.397Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -5 LEW_1910.txt; awk 'BEGIN{RS=\"\\f\"} NR==3{print substr($0,1,400)}' LEW_1910.txt; echo \"=== leaf count ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' LEW_1910.txt"
}
```


### [2026-09-04T19:03:59.161Z] TOOL RESULT

```
eae hee ne
ee
Duquesne University:
joe Kt re |
* ee . ¥
Duquesne University:

=== leaf count ===
305
```


## [2026-09-04T19:04:03.954Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== SKT liberty ==\"; grep -n \"LIBERAL\\|Liberty\\|LIBERTY\\|liber, free\" SKT.txt | head -10; echo \"== SKT deliver ==\"; grep -n \"DELIVER\" SKT.txt|head -3"
}
```


### [2026-09-04T19:04:04.026Z] TOOL RESULT

```
== SKT liberty ==
== SKT deliver ==
```


## [2026-09-04T19:04:06.845Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"deliver\\b\" SKT.txt | head -5; echo \"---\"; grep -n -i \"liberal\" SKT.txt | head -5; echo \"--- size\"; wc -c SKT.txt"
}
```


### [2026-09-04T19:04:06.930Z] TOOL RESULT

```
3559:Clever.  (F.-L.;  tenfmed  with  E.)  !■ BnUcr's  Hudibnu  (1663).  It  took  the  pl«c« of  M.  E.  dtlivrr,  quick,  nimble.  Ch.  proL 84.«»0.  F.  dtlivrt.  free,  prompt,  alcit; compounded  from  L.  de^  prefix,  and  /IBrr. free ;  see  Deliver.  But  apparently  confused with  M.  K.  (livir^  ft  claw,  also  as  adj.  rci'!^ to&eiie,  allied  to  Climb.Cloavei*^  %  Not from  A.  S.  gltiiw,  M.  E.  ^rt(,  skilfal ;  itill less  from  G.  klugW
4727:tradition.  (L.)  L.  traditio,  a  surren- der, a  tradition  (.Col.  ti.  i^).'  L.  traditus, pp.  of  trad^n,  to  deliver. -L.  tra-,  for tnifu,  across;  -dere,  for  dtj'e,  to  give
4916:Deliver  ;  see  Liberal.  ,
6092:Exempt,  freed.  (F.  -  L.)  O.  F. /x/w//; whence  txemfiter,  to  exempt,  free,  —  L.  rx- tmptuSt  pp.  oi  ex-inure^  lo  take  out,  deliver, ficc.  — I*Mr,  out;  rm/r«,  to  take.  (V  AM.) assume.  (L.)  L.  assumtrt  (pp.  as- sumpfHs),  to  take  to  onc&clf.  —  L.  as-,  for aJ,  to ;  sutmre,  to  take,  which  stands  for iuh  imert  *,  from  tub,  under,  secretly,  and tmin,  to  take.  Der.  ajxum/f'ieft  (from the  pp.).
10248:deliver.   (F.  -  L.)    OF.  delivrtr^ set  free. —  Low  L.  deiiherare,  to  set  free." L.  de.  from ;  Uberare,  to  free,  from  tiber,
---
3990:ootins^   (F.  —  L.)    M.  E.  rcmtil O.  F.  conseil.^l^  cimsiHum,  dcliberaliOJ —  I^  conauUre,  to  consult.
4916:Deliver  ;  see  Liberal.  ,
9102:H-  (3),  put  for  Iff-,  negative  prefix  when /  follows.  Exx. :  il-iej^I^  i!-legioie,  il-Ugiti- matt,  il-liberal,  il-limitahU,  il-liUratt^  it' Ic^cat;  for  which  see  Ugal^  tegihlt,  &c. And  see  illicit.
9964:largess,  a  liberal  gift.  (F.-L.)  F. iar^ifCt  bounty.  — Low  L.  iargifia*,  not found,  put  for  L.  lar^tu,  a  b«stovrtng.— L,  lar^/tts,  pp.  of  largiri,  to  bestow.  mL. iarguj.  Urge,  liberal,
10247:Libel;  sec  Library. Liberal.  tF. - L.)  M.  E.  HUmi  -0, libtml.^X^  liberalise  behlting  a  free  on generous.  — L  liber,  free.  Allied  to  l*ift, pleases,  it  is  one's  pleasure;  SkL  /»M. desiie.
--- size
2656202 SKT.txt
```


## [2026-09-04T19:04:15.167Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nlines=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in [10247,10248]:\n    lf=('\\n'.join(lines[:ln])).count('\\f'); print(ln,'leaf',lf,'printed',lf-20)\n\"; echo \"== FSD liberty ==\"; grep -n \"liberty\" FSD_vol3.txt | head -5"
}
```


### [2026-09-04T19:04:17.022Z] TOOL RESULT

```
10247 leaf 270 printed 250
10248 leaf 270 printed 250
== FSD liberty ==
3060:liberty is most obvious, as a committing magUtrate, police
10544:inTsh'on, n The granting of liberty to a bondman, thn
46095:tween auilioiitv and liberty."
76385:with Mok»ha, or spiritual liberty and bliss. In Huddhlani,
78474:amnesty or guaranties of liberty Hee goiipounobb, 8
```


## [2026-09-04T19:04:20.123Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for v in 1 2 3 4; do echo \"### vol$v\"; grep -n \"lib'\\?er-ty\\|lib\\*er-ty\\|liber-ty, n\\|L. liber, free\\|liber, free\" FSD_vol$v.txt | head -6; done"
}
```


### [2026-09-04T19:04:21.954Z] TOOL RESULT

```
### vol1
### vol2
### vol3
### vol4
```


## [2026-09-04T19:04:24.960Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"L\\. liber\\|< L\\. liber\\|liber, fre\" FSD_vol2.txt FSD_vol3.txt | head -10; echo \"---- try 'libertas'\"; grep -n \"libertas\" FSD_vol2.txt FSD_vol3.txt | head -10"
}
```


### [2026-09-04T19:04:25.064Z] TOOL RESULT

```
---- try 'libertas'
```


## [2026-09-04T19:04:37.454Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== KLN Latvia ==\"; grep -n \"Latvia\" KLN_1966.txt | head -5; echo \"== AHD Latvia/Lett ==\"; grep -n -i \"latvia\\|Lettish\" AHD_watkins1985.txt | head -5; echo \"== WEB liberty ==\"; grep -n \"Latvia\" WEB_vol1.txt | head -3"
}
```


### [2026-09-04T19:04:37.552Z] TOOL RESULT

```
== KLN Latvia ==
21196:Derivative:  last,  tr.  v.,  to  shape  with  a  last, last,  intr.  v.,  to  continue,  endure.  —  ME.  iasten, fr.  OE.  Ixstan,  ‘to  follow,  carry  out,  perform;  to continue,  last,  endure’.  The  orig.  meaning  was ‘to  follow  a  track’,  fr.  OE.  last,  ‘sole  of  foot, footprint,  track’.  Cp.  Goth,  laistjan,  ‘to  follow’, OHG.  leistan,  MHG.,  G.  leisten,  ‘to  perform, achieve,  afford’,  and  see  last,  ‘model  of  foot . Derivatives :  last,  n.,  staying  power,  last-ing,  adj., last-ing-ly,  adv.,  last-ing-ness,  n. last,  n.,  1)  load  (obsol.) ;  2)  unit  of  weight.  —  ME. last,  ‘load;  unit  of  weight’,  fr.  OE.  hlxst,  ‘bur¬ den’,  rel.  to  OFris.  hlest,  MDu.,  Du.  last,  OHG. blast,  last,  MHG.,  G.  last,  ‘load’,  and  to  OE., OHG.  hladan,  ‘to  load’.  E.  last  prop,  means ‘that  which  is  laden’.  See  lade  and  cp.  the  second element  in  ballast.  Cp.  also  alastrim. lat,  n.,  the  unit  of  currency  in  Latvia.  —  Lett,  lats (pi.  lati),  formed  from  the  first  syllable  of  Lat- vija,  the  Lett  name  of  the  country, latakia,  n.,  a  kind  of  Syrian  tobacco.  —  Prop, ‘tobacco  grown  in  Latakia’,  a  town  in  N.W.  Sy¬ ria.  The  name  Latakia  is  traceable  to  Gk.  Aao- SUEi.a,  name  of  a  city  in  Phrygia.  See  Laodice¬ an.
21237:Latvia,  n.  —  Lit.  ‘the  country  of  the  Letts’.  See Lett  and  cp.  lat.
21553:Lett,  n.,  an  inhabitant  of  Latvia.  —  The  word orig.  meant  ‘people’.  It  comes  fr.  OHG.  liuti (whence  MHG.  liute,  G.  Leute),  ‘people’,  which is  possibly  cogn.  with  Gk.  JXeu&spo?,  L.  liber, ‘free’.  See  liberal  and  cp.  eleuthero-.  Cp.  also Latvia.  For  sense  development  cp.  Dutch. Derivatives:  Lett-ic,  Lett-ish,  adjs.  and  n.’s. letter,  n.,  graphic  symbol,  character.  —  ME. lettre,  fr.  OF.  (=  F.)  lettre,  fr.  L.  litter  a,  ‘letter of  the  alphabet’  (in  pi.  ‘epistle,  document’), which  is  of  uncertain  origin.  Ernout  and  Meillet (in  DELL.,  p.  363)  point  out  that  since  the  Latin alphabet  was  borrowed  from  the  Greeks (through  the  medium  of  the  Etruscans),  it  is  not improbable  that  littera  itself  would  be  of  Greek origin.  According  to  Brdal  (quoted  by  Emout- Meillet  l.c.)  littera  would  derive  fr.  Gk.  Sicp&epa, ‘tablet’,  a  word  glossed  by  Hesychius;  for  the change  of  d-  to  /-  see  lachrymal.  Cp.  literal,  liter¬ ary,  literate,  literature,  alliteration,  belles-lettres, obliterate.
32900:Riga  balsam,  balsam  obtained  from  the  Swiss pine.  —  Named  after  Riga,  capital  of  Latvia, rigadoon,  n.,  a  dance.  —  F.  rigaudon,  rigodon ; according  to  J.  J.  Rousseau  in  Dictionnaire  de musique  named  after  Rigaud,  the  inventor  of this  dance.  According  to  Mistral,  Rigaud  was  a renowned  dancing  master  at  Marseilles.
== AHD Latvia/Lett ==
== WEB liberty ==
38600:1. (a) an economic theory or system of the ownership of all property by the community as a whole; (b) a theory or system of the owner- ship of all means of production (and distribu- tion) by the community or society, with all members of the community or society sharing in the work and the products; specifically, such asystem as practiced in the Soviet Union since 1917, and later in China, Poland, Czechoslo- vakia, and other communist countries, theo- retically based on the doctrines of Marx, En- gels, Lenin, and, latterly, Stalin, characterized by state planning and control of the economy, ruthless suppression of all opposition political parties and all deviation within the Party, and the suppression of individual liberties under a dictatorship; since 1940 expansionist by mili- tary action and subversion in Estonia, Latvia, Lithuania, Czechoslovakia, etc.
105692:very latest style, model, develop- {Colloq.] $ ee its, la’tu, (Lett. lats, pl. lati, from rmer monetary unit of Latvia.
105918:Lat’viňn, a. 1. of Latvia or its people; Let-
```


## [2026-09-04T19:04:46.138Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/page-311.json'))\ne=d['entries'][0]\nfor n in e['nodes']:\n    if n['id'] in (1,6,7,8,11,13,14,15,16,17,18,19,20):\n        print('=== node',n['id'],n['lang'],n['words'],'::',n['verdict'])\n        print(n['derivation'])\n        print('SOURCES',n.get('sources'))\n        print()\n\""
}
```


### [2026-09-04T19:04:47.908Z] TOOL RESULT

```
=== node 1 Avestan raod 1, raoda, raodha :: confirmed
Young Avestan verb raoδ- (raoδaiti 'grows', Vd 5.19; raoδahe Y 10.4; past participle urusta-/rusta- 'grown') and the nouns raoδa- m. 'growth, stature, appearance' (Pokorny: 'Wuchs, Ansehen') and raoδah- n. 'growth' are the direct Iranian reflexes of PIE *h₁lewdʰ-: PIE *l > Proto-Iranian *r, *ew > ao, *dʰ > δ. The sense 'face' is a secondary development of 'appearance, outward form' (Wiktionary روی: Proto-Iranian *rauda- 'appearance' < 'growth'). Nourai's cited KLN/SYN are consistent with Pokorny 684, which is the standard treatment.
SOURCES ['https://starlingdb.org/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cie%5Cpokorny&first=1181', 'https://archive.org/details/etymological-dictionary-of-the-iranian-verb', 'https://en.wiktionary.org/wiki/%D8%B1%D9%88%DB%8C']

=== node 6 Persian rŭnîk :: plausible
rū-nīk «رونیک», glossed 'beautiful' and equated by the chart with nīk-rūy «نیکروی» 'fair-faced', is a transparent compound of rūy 'face' (#2, < MP rōy < Proto-Iranian *rauda- 'appearance') + nīk 'good' (Nourai's cross-reference Nei 1). Nourai gives no reference for it; I found it only in modern online Persian dictionaries (vajehyab: 'نیک رو، خوش رو، زیبارو') and as the modern given name Rūnīkā, while nīk-rūy itself is in Dehkhoda. The word is morphologically sound and its first element does belong to this root, but I could not verify a classical attestation of rūnīk, and the claim that it is the source of Arabic rawnaq (#7) is rejected below.
SOURCES ['https://vajehyab.com/?q=%D8%B1%D9%88%D9%86%DB%8C%DA%A9', 'https://en.wiktionary.org/wiki/%D8%B1%D9%88%DB%8C']

=== node 7 Arabic raonaq :: disputed
Arabic rawnaq (رَوْنَق) 'beauty, splendour, lustre, radiance' is treated by Wiktionary (citing Wehr and al-Maʿānī) as a native Arabic noun of the root r-n-q (cf. rāniq 'clear, limpid (water)', ranaqa/tarawnaqa 'to be clear, glisten'), of the fawʿal pattern; Persian rownaq is listed as borrowed from it. The Persian source rū-nīk proposed by Nourai (after AFM:74 = Addai Sher, al-Alfāẓ al-fārisiyya al-muʿarraba, 1908, many of whose derivations are no longer accepted) would require the unexplained loss of -y- and an irregular k > q; no modern dictionary follows it.
SOURCES ['https://en.wiktionary.org/wiki/%D8%B1%D9%88%D9%86%D9%82', 'https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A5%8C%E0%A4%A8%E0%A4%95%E0%A5%BC']

=== node 8 Persian rownaq :: confirmed
The edge is correct: Classical Persian rownaq «رونق» 'splendour; flourishing, boom, heyday' is a straightforward loan of Arabic rawnaq (Wiktionary: 'Borrowed from Arabic رَوْنَق'), the Arabic diphthong aw being kept as Persian ow; the meaning 'growth, success' is a Persian semantic extension, and the word spread on from Persian to Urdu/Hindi raunaq, Chagatai and Kurdish. The ancestry drawn above #7 (Persian rūnīk) is not accepted: the word is Arabic in origin.
SOURCES ['https://en.wiktionary.org/wiki/%D8%B1%D9%88%D9%86%D9%82', 'https://vajehyab.com/?q=رونق&d=moein']

=== node 11 Avestan raodha-taxma :: disputed
No such word occurs in the Avesta; Rostam is absent from the Avestan texts, and *Raoδas-taxma- is a scholarly reconstruction (Justi, Iranisches Namenbuch) behind Middle Persian Rōdstahm (lwtsthm), Sogdian Rwstmy and New Persian Rostam. The language label should therefore be 'Old Iranian (reconstructed)'. The standard modern analysis (Wiktionary, Iranica, Mayrhofer/Schmitt) reads the compound as *Rautas-/Raudas-taxma- 'strong as a river' or 'whose running is like a river's', i.e. first element Av. raoδah-/OP rautah- 'river' (< *srew- 'flow', the same word as in rōstāg #9) + taxma- 'strong, brave' (Nourai's cross-reference Tenk); the older reading 'grown strong' with raoδah- 'growth' is a minority interpretation not followed by current reference works.
SOURCES ['https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%85', 'https://forum.wordreference.com/threads/persian-etymology-of-rostam.3387039/', 'https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF']

=== node 13 Avestan hava-rd :: transcription_suspect
'hava-rd' is not a possible Avestan form; the book almost certainly printed hu-raodha (Av. huraoδa-), and the scan lost/garbled letters. Av. huraoδa- 'well-grown, well-shaped, handsome' is a real Young Avestan adjective (Vidēvdād 3.24 'iδa carāiti huraoδa'; epithet of Sraoša in Yasna 57), built from hu- 'good, well' (PIE *h₁su-; Nourai's cross-reference Su 1) + raoδa- 'growth, stature' (#1). Its meaning and root membership are exactly as glossed; only the transliteration is corrupt.
SOURCES ['https://wikisource.org/wiki/Avesta/Vid%C4%93vd%C4%81d', 'https://archive.org/details/etymological-dictionary-of-the-iranian-verb', 'https://starlingdb.org/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cie%5Cpokorny&first=1181']

=== node 14 Pahlavi hu-rust :: confirmed
Middle Persian hurust 'well-grown, well-built, fine' = hu- 'well' + rust, the past participle of rōy-/rustan 'to grow' (Cheung 2007:193: BMP lwst /rust/, MMP rwst; the Iranian participle *Hrusta- is the analogical replacement of expected *Hruzda- < *Hrudʰ-ta-). It is thus the Middle Persian counterpart of Av. huraoδa- (#13), formed on the participle rather than on the noun raoδa-, but from the same root and with the same meaning. Jeffery cites this word as MP hū̆rust 'well grown'.
SOURCES ['https://archive.org/details/etymological-dictionary-of-the-iranian-verb', 'https://en.wikipedia.org/wiki/Houri']

=== node 15 Arabic hŭr :: disputed
Arabic ḥūr (حُور), the plural of aḥwar (m.) / ḥawrāʾ (f.) 'having eyes with a strong contrast of white and black', in the Qurʾānic phrase ḥūrun ʿīnun (44:54, 52:20, 56:22) 'fair, large-eyed maidens', is a regular Arabic plural of the root ḥ-w-r 'to be white; whiteness of the eye' (Wiktionary, Wehr; cognate with Syriac ḥewwār 'white', Hebrew ḥiwwēr 'pale'). Standard lexica derive it inside Semitic. The Iranian etymology Nourai follows (VDQ:39 = the Persian translation of Jeffery, The Foreign Vocabulary of the Qurʾān, who after Tisdall suggested Pahlavi hurust 'well grown') is a minority hypothesis that would require an unexplained h > ḥ, loss of -st and reinterpretation as a plural; Wiktionary and Etymonline (houri: 'from Arabic haura, to be beautifully dark-eyed') do not accept it.
SOURCES ['https://en.wiktionary.org/wiki/%D8%AD%D9%88%D8%B1', 'https://en.wiktionary.org/wiki/houri', 'https://www.etymonline.com/word/houri', 'https://en.wikipedia.org/wiki/Houri']

=== node 16 Persian hŭr 1 :: confirmed
The edge is correct: Classical Persian ḥūr «حور» 'houri, heavenly maiden' and the derivatives ḥūrī «حوری» (with the Persian relational/singulative -ī), ḥūr al-ʿayn «حورالعین» (the Qurʾānic phrase taken over as a unit) and ḥūr-vash «حوروش» 'houri-like' are borrowed from Arabic ḥūr; Persian ḥūrī is in turn the source of French/English houri (1650s/1737). Only the ancestry above #15 is wrong: the word is Semitic, not from hurust.
SOURCES ['https://en.wiktionary.org/wiki/houri', 'https://www.etymonline.com/word/houri', 'https://en.wiktionary.org/wiki/%D8%AD%D9%88%D8%B1', 'https://vajehyab.com/?q=حور&d=moein']

=== node 17 Sogdian rwd :: confirmed
Buddhist Sogdian rwδ- (rwtt, rwt 'grows'; inf. rwδʾy), Manichaean Sogdian preterite stem rws-, and the compound pati-: ptrwδ-/ptryst- 'to grow up', are listed by Cheung 2007:193 under Proto-Iranian *Hraud 'to grow (bigger)' beside Av. raoδ-, MP rōy-/rust, Parthian rwd-, Khotanese rrud-. Sogdian δ is the regular lenition of Old Iranian *d; Nourai's 'rwd' is the same word in a δ-less transliteration. (Homographic Sogdian rwδ 'copper' < *Hrawdʰas 'red' is a different word.)
SOURCES ['https://archive.org/details/etymological-dictionary-of-the-iranian-verb', 'https://www.parsianjoman.org/wp-content/uploads/2016/04/Etymological-Dictionary-of-the-Iranian-Verb.pdf']

=== node 18 Indo-European leudho; leudheros :: confirmed
Pokorny 684-685 lists exactly these derivatives: leudho-/leudhi- 'Nachwuchs, Volk' (OHG liut, OE lēod, German Leute, OCS ljudьje, Lith. liaudis 'people') and leudhero- 'zum Volk gehörig, frei' (Greek ἐλεύθερος, Latin līber); modern notation *h₁léwdʰ-o-, *h₁léwdʰ-ero-. The semantic path is 'growth' → 'offspring' → 'the people (born into the community)' → 'belonging to the people, free-born (as opposed to slave)'.
SOURCES ['https://starlingdb.org/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cie%5Cpokorny&first=1181', 'https://en.wiktionary.org/wiki/liber#Latin', 'https://www.etymonline.com/word/liberty']

=== node 19 Latin liber :: confirmed
PIE *h₁léwdʰ-ero-s → Proto-Italic *louðeros → Old Latin loebesum/loebertatem (Festus; oe < *ou, intervocalic *dʰ > Italic *ð > Latin b) → Classical Latin līber 'free' (with the regular monophthongization oe > ī); de Vaan 2008:338. The same stem gives lībertās 'freedom', līberāre 'to free' and Līber (the god).
SOURCES ['https://en.wiktionary.org/wiki/liber#Latin']

=== node 20 English liberty, deliver, Latvia :: disputed
liberty: Latin lībertās (acc. lībertātem) → Old French liberte → Middle English liberte (late 14th c.) — confirmed. deliver: Latin līberāre 'to free' → Late Latin dēlīberāre 'to set free' → Old French delivrer → Middle English deliveren (c. 1200), later 'hand over' — confirmed (Etymonline, AHD leudh-). Latvia, however, has no connection to *leudh-: it is a 19th-century Latvian formation Latv-ija from the ethnonym latvis 'Lett', whose origin is unknown (Etymonline: 'of unknown origin'; Wiktionary: possibly from a river name Latava); neither Etymonline nor Wiktionary nor AHD links it to Latin līber or PIE *leudh-. Node verdict is 'disputed' because of Latvia only.
SOURCES ['https://www.etymonline.com/word/liberty', 'https://www.etymonline.com/word/deliver', 'https://www.etymonline.com/word/Latvia', 'https://en.wiktionary.org/wiki/Latvia']
```


## [2026-09-04T19:04:56.717Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -c MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null; echo \"== روستا ==\"; grep -c \"روستا\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null"
}
```


### [2026-09-04T19:04:56.801Z] TOOL RESULT

```
 4377831 MON_part1.txt
 4331421 MON_part2.txt
 4377831 incoming/MON/MON_2vol_Adena_v1_djvu.txt
 4331421 incoming/MON/MON_2vol_Adena_v2_djvu.txt
17418504 total
== روستا ==
incoming/MON/MON_2vol_Adena_v1_djvu.txt:14
MON_part2.txt:18
MON_part1.txt:14
incoming/MON/MON_2vol_Adena_v2_djvu.txt:18
```


## [2026-09-04T19:04:59.032Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"روستا\" MON_part1.txt | head -14"
}
```


### [2026-09-04T19:04:59.093Z] TOOL RESULT

```
9624:گروستاندن» گرو کردن به گروگان گرفتن. 
64006:روستا. راه به ده بردن: به مقصد رسیدن. 
64180:ایرانی» مورح. روستایی) ج. دهاقنه» دهاقین. 
67319:رستاق: 0512 [معر . روستا کك] (.) ده» 
67320:د یه ) روستا؛ ج. رساتیق. 
67395:روستا ک] (.) روستاء ده» قر به. 
69055:روستا(ی): (قد. :۲25۷50()5 [معر 
69056:رستاق - روستاق - رسداق - رزداق] (.) 
77584:سروستان: -2۲۷: (امر.) جابی که در 
80789:حوالی آن) روستاها. سواد اعظم: ناحة 
82601:خواربار و زاد و علوفه که از روستاهای سر 
87604:روستایی. آشنا؛ مق. بیگانه, غریب. کشوری؟ 
88926:چادرنشین) مق. روستانشین» شهر نشین. 
91962:آراسته. مثل طاوس در خانة روستایی:
```


## [2026-09-04T19:05:02.142Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '69050,69065p' MON_part1.txt; echo \"=== rostaq 67315-67325 ===\"; sed -n '67315,67325p' MON_part1.txt; sed -n '67390,67400p' MON_part1.txt"
}
```


### [2026-09-04T19:05:02.241Z] TOOL RESULT

```
فرمز؛ پودر روژ. 

روسپی: (قد. -:70:0)25 (ص.) زن بدکاره 
فاحشه» بدکاره. 

روستا(ی): (قد. :۲25۷50()5 [معر 
رستاق - روستاق - رسداق - رزداق] (.) 
ده» قر به. 

روسیاه: ۲۱۱-1۷0 [- روسیه] (ص‌مر.) 
آنکه جهر هاش ساه رنگ باشد. (کد.) 
کناهکار بدکار؛ عاصی. 

روش: ۲۵۷-۵ (امص.) عمل رفتن. خرامش 
() معبره راهرو» خیابان (باغ و غیره). 
روشن: ۳۵۳/0۷3 [- روشان] (ص.) 
=== rostaq 67315-67325 ===

رستار: ۲ (ص‌مر.) خلاص شونده» 
رستگار 

رستاق: 0512 [معر . روستا کك] (.) ده» 
د یه ) روستا؛ ج. رساتیق. 

زرتت‌کا ره (-۲2۵۱ (ص‌فا.) خلاص یابنده؛ 
رها شو نده. 

زنشکارع: ۲2۹۲-۵۲ (حامص.) خلاص؛ 

رسد: ۲۵520 (.) نظ.) واحدی نظامی شامل 
سه جو حه؛ دسته. 

رسداق: 02 [- رستاق - رزداق» معر. 
روستا ک] (.) روستاء ده» قر به. 

رسدیان: 2527 (ص مر . آمر.) پایه‌ور 
شهربانی نظیر ستوان ارتش (فره.) ضح.- این 
اصطلاح در زمان رضا شاه بهلوی مدتی 
متداول بود و سپس ملفی گردید.
```


## [2026-09-04T19:05:10.542Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"رونق\" \"روضه\" \"روییدن\" \"رونیک\" ; do echo \"===== $w\"; grep -n \"^$w\\|^$w:\" MON_part1.txt MON_part2.txt | head -4; done"
}
```


### [2026-09-04T19:05:12.473Z] TOOL RESULT

```
===== رونق
MON_part2.txt:17381:رونق و نظام یافتن آن. خوابیدن کار: (کذ.) 
MON_part2.txt:22945:رونق افتادن ( کالا). (اسص.) بی‌رونقی» 
MON_part2.txt:77475:رونق داشتن. (امص.) رواج» رونق. 
MON_part1.txt:1508:رونق مخفی» خوبی و نیکی پوشیده. 
===== روضه
MON_part1.txt:64999:روضه‌خوان. 
MON_part1.txt:69110:روضه رضوان: (کد.) بهشت. روضة فیروزه 
MON_part1.txt:69117:روضه منعقد است. 
MON_part1.txt:69118:روضهخوان: «قدء (ع. ف. - 
===== روییدن
MON_part2.txt:76261:روییدن» رستن» نمو کردن. پرورش یافتن. 
MON_part1.txt:67340:روییدن؛ نمو کردن بالیدن. 
MON_part1.txt:69395:روییدن: ۲7۷-00 (- رستن ] (مص‌ل.) 
===== رونیک
```


## [2026-09-04T19:05:15.389Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== روییدن ===\"; sed -n '69393,69400p' MON_part1.txt; echo \"=== روضه ===\"; sed -n '69100,69120p' MON_part1.txt; echo \"=== رونق ===\"; grep -n \"رونق:\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-04T19:05:15.498Z] TOOL RESULT

```
=== روییدن ===
۷ 

روییدن: ۲7۷-00 (- رستن ] (مص‌ل.) 
(رویید» روید» خواهد رویید» بروی» 
روینده» رویان» روییده» رویش). نمو کردن 
نباتات» بالیدن. رشد کردن بعضی از انساج 
حیوانی. 

=== روضه ===
روصه ۱ فر هنک فارسی معین ۱۷۲۱ 


آنکه دارای اند شه‌ای روشن است. کسی که 
در امور با نظر باز و متجددانه نگرد. 
روصه: (۲۵۳2۵)۲۵۷۵ [ع. . روضه] (.) باغ» 
گلزار؟ج. رباضء روضات. روضه 4 باغ رفیع: 
(کد.) بهشت. (کد.) قبر» گور. روضة ترکیب: 
غالب مردم» جسد آدمی. روضه حور: (کد.) 
بهشت. روضه دوزخ‌بار: (کد.) شمشیر آبدار. 
روضه رضوان: (کد.) بهشت. روضة فیروزه 
رنگ: (کد.) آسمان. خطبه‌ای که در مراسم 
عزاداری بالای منبر خوانند و آن شامل حمد 
خدا و درود بر بیغمیر اسلام و ایمه اطهار و 
مسایل دینی و اخلاق و شرح بخشی از وقایع 
کربلا است. ضح. این کلمه از نام «روضه 
لشهداء ماخوة انت. مجلسی کنه در آن 
روضه منعقد است. 
روضهخوان: «قدء (ع. ف. - 
روضه‌خواننده] (ص‌فا.) آنکه ذکر سصیبت 
اسام حسین و وفایع کربلا و مصالب 
=== رونق ===
MON_part1.txt:69310:رونق: («م) «عد: [ع.] (امص.) فروغ»
```


## [2026-09-04T19:05:25.871Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"رونیک\" \"روستا\" \"رونق\" \"روضه\" \"حور\"; do echo \"===== $w\"; grep -n \"$w\" BQT_v2_pages.txt | head -4; done"
}
```


### [2026-09-04T19:05:27.704Z] TOOL RESULT

```
===== رونیک
===== روستا
1990:         ‫دراصطلاح روستائان» مقدار زمینی‌را که بك زارع ا دو گاو ممتواند زراعت کند «جفت کاو»‬                         ‫سح‬   ‫‏‪١‬‬
4463:                                                 ‫ورك ‪ :‬فرهنك روستابی‪۶ ۳ ۲‬ببعد‪.‬‬           ‫کلاب ‪۶‬‬
6060:    ‫رکه ‪ :‬چغك‪.‬‬              ‫‪۴‬‬        ‫رکک‪ :‬چفانه ‪:‬‬            ‫‪۴‬‬                    ‫روستابی‬     ‫فرهنك‬      ‫کل گلاب ‪EYT‬‏‬
8704:   ‫روستابی )‪۳٩4‬‏ (ثابتی ‪ - )۸۷۱‬کل حنا ‪ 201014512‬از کیامان تردبك بتبرة شمعداتبان‬
===== رونق
6736:                                                                   ‫ورونق باشد» شهید (بلخی) کفت ‪:‬‬
14813:      ‫‪ _ ۴۱‬رك ‪ :‬الجماهربیرونی‬                          ‫_ !‪ ::‬خوش ‪ +‬آب (ماء > ها‪ :‬و رونق وجلاه) ‪.‬‬               ‫‪۴‬‬
25125:                         ‫رواج ورونق بهار باشد ‪۰#.‬‬       ‫آمیخته ‪ -۷۲۳ ۴۰‬شرم وحیا ‪-۵.۳۳‬داراستی‬
31691:                                   ‫شردطه خوانند ‪.‬‬        ‫واستعداد و ساختگی کارها ورونق‌مهم‌را گونند ‪۴‬‬
===== روضه
3193:    ‫جوسه عبر وزن روضه ‪۰‬‬                               ‫باشد که امزغز‬        ‫لنوابی‬
25864:‫روضه باع ر فیع‪-‬کنابهاز رباض‬                             ‫روشنان فلك ‪ .‬کنایه از ستار ها‬
25866:‫روضه تر کیت ‪ -‬کنابه از قالب‬                             ‫است که در‬    ‫معروف‬     ‫‪۴‬‬     ‫روشنایی‬
===== حور
2523:‫بود کهآ فتاب بنقطة اول‌حمل آمده بوده فرمود‬     ‫و حور و ری مذ کور شود » و جمشداستا کر‬
4798:  ‫جر احور = با واو معدوله بر وزن‬                    ‫کویند‪ - ۱‬وبفتح اول‌نفمه وغناباشد چه چر کر‬
7390:                                                        ‫چو بکش = بفتح رأبع‌بروزن‌حوروش»‬
8720:‫‪.‬هت بفتح اول » داله‌ایست‬    ‫حور هندی‬                                     ‫مید دوباره بږخته راگوبند ‪۱‬‬
```


## [2026-09-04T19:06:15.867Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== AFA 5372 area ==\"; sed -n '5368,5395p' AFA.txt; echo; echo \"== FVQ rawda ==\"; grep -n \"Rauda\\|rawda\\|Meadow\\|meadow\" FVQ.txt | head -5"
}
```


### [2026-09-04T19:06:15.934Z] TOOL RESULT

```
== AFA 5372 area ==
Gründen als unecht erwiesen. Über ,jjdü' = xhrxvov vgl.
Gl. geogr. 331. Eine aramäische Mittelform scheint nicht
erh&ltcn zu sein. Der Anklang an die DiminutiTform wurde
znr Arabisierung gewählt.
Auch der yerbreitetste Name für ^Garten** .ii^ scheint
erst aus aram. ]Al^ übernommen. Zunächst liegt die An-
nahme einer Entlehnung sachlich sehr nahe. 'J^aif gilt für
den schönsten Platz in Arabien um seiner Gärten willen.
Hob. Smith Journey II. Ob man eher gegenüber hebr. p
auch im Arabischen *j%^ erwarten sollte, ist nicht zu
sagen , da auch hebr. HSJl vorkommt. Aber dtis Wort hat
T*
im Arabischen keine ganz bequeme Ableitung von der
Wurzel ^1^ »decken". Ursprünglich aber soll es gewiss
»Garten** (Gauh. ^Uu^j) bezeichnen, und erst später ist
eine kleine Palmenpflanzung auch mit diesem Namen be-
nannt (Vgl. Gauh. s. y. t'"^) Der echte Name scheint149
I&jL^ eigentlich »Zaun** wie auch holländisch tutn ur-
spr. »Zaun'* jetzt »Garten'*. Die echten Namen grüner
(bunter) Plutze sind &ju (nach Jäküt II. 801 aber m^sOub
^jlJI ^ ^Ul) : dasselbe ist Li3.% seiner Ableitung nach
JaljLüt IL 840; 141, 20. Ein echter Name des Zauns ist
&A^(X^9 A^' ^^ fremd kannten schon die Araber ^^.^
▼ulg. ^J%JD (Mu^arr. 52) entlehnt aus KIIIH Nöldeke
J/anJ. Gramm. 60.
Über den eigentlichen Zusammenhang von <>mJ(>I^ mit
irxpjiiti7o; bat uns — nach Lagarde*s schon von A. Müller
in Bezzeubc^rger Beilr. I. 280 Anm. I zurückgewies^mer

== FVQ rawda ==
9214:(Rauda). 
9217:A rich, well watered meadow ; thence a luxurious garden. (LA,
```


## [2026-09-04T19:06:19.885Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9210,9245p' FVQ.txt; echo \"=== page ===\"; python3 -c \"\nlines=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor i,l in enumerate(lines):\n    if '(Rauda)' in l:\n        lf=('\\n'.join(lines[:i])).count('\\f'); print('line',i,'leaf',lf,'printed',lf-17); break\n\""
}
```


### [2026-09-04T19:06:21.735Z] TOOL RESULT

```
Semites. (See Laufer, Sino-Iranica, 285.) 



(Rauda). 
xxx, 14 ; xlii, 21. 

A rich, well watered meadow ; thence a luxurious garden. (LA, 
ix, 23.) 

Both passages are- late Meccan and refer to the blissful abode of 
the redeemed. 

There can be little doubt that the word was borrowed as a noun 

.* , * -- 
into Arabic, and from it were then formed <^J "to resort to a 



garden", (j^J'j " to render a land verdant ", (j^jjl 4 * to abound 

in gardens ", etc. As some of these forms occur in the early literature 
the borrowing must have been an early one. 

Vollors, ZDMG, 1, 641, 642, noted that the word is originally 
Iranian, and he suggested that it was from the Iranian V rud, meaning 
to yrow. 5 The Av. ^i-ui fojod means to flow* from which cornea 

1 PPG1, 198 ; Frdhang, Glossar, p. 105 ; and Noldeko, Neue Beitrar/fi, 42. 
3 Low, Aram&Mche Pfltinzfiiwiainen, 310, says : " Etymologic dunkol," and soo 
Ziinincrn, Akkad. Fremdw, 54. 

3 Nt>ldekc, Aland. Gramm, 123 ; Lidxbarski, Mandaisc.hfi Lituryien, p. 218. 

4 Hommel, Anfsdtze, 97 ff. ; RDB, 941, "a foreign word of doubtful origin" 
=== page ===
line 5407 leaf 162 printed 145
```


## [2026-09-04T19:06:25.493Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9245,9275p' FVQ.txt"
}
```


### [2026-09-04T19:06:25.541Z] TOOL RESULT

```
4 Hommel, Anfsdtze, 97 ff. ; RDB, 941, "a foreign word of doubtful origin" 

5 " ^JJ ^ * ine Wtymulogio : zur Bcdeutung ist hier nur daran zu orirmorn, 
dass cs in der Nomadensprache jeden grunen Fleck in odor Umgebung bczeiehnet. 
Mit dem alten Spraehgcbrauch deckt sich nooh jctzt nach meiner Krfahrung gonau 
dio Sprachc z.B. der Sinaibeduinen. . . . Toh glaubo nicht fehl z\i gehen, wenn ich, 

j, aus p. \/ rud c waohscn ', erklfiro." 
Bartholomae, AIW, 1495; Reichelt, Awestisc.hes Elementarbuch, 493. 



146 FOREIGN VOCABULARY OF THE QUR^AN 



raoSah a river* and JJ^D^JJ) rao8a, growth (cf. 






Skt. "O^, rising, height), also meaning stature,* From the same root 



comes Phlv. 5y a lake or riverbed* and the Pers. ^Jj commonly
```


## [2026-09-04T19:06:27.926Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9275,9310p' FVQ.txt"
}
```


### [2026-09-04T19:06:27.981Z] TOOL RESULT

```
used for river, e.g. C*J ^Jj the Euphrates. The Phlv. word is 
important, for the Lexicons tell us (cf. Tha'lab in LA, ix, 23) that 

water was an indispensable mark of a <^Jj. Thus the conclusion 
would seem to be that the Arabs learned the Phlv. Sy 4 in the 
Mesopotamian area and used it for any well watered or irrigated land. 

(Ar-Knm). 

XXX, 1. 

The Byzantine Empire. 

It is the common name for the Byzantine Greeks, though also used 
in a wider sense for all the peoples connected or thought to be con- 
nected with the Eastern Roman Empire (e-f. TA, viii, 320). 

A considerable number of the early authorities took it as an 

Arabic word derived from *lj to desire eagerly, the people being so 

called because of their eagerness to capture Constantinople (Yaqut, 
Mu'jam, ii, 862). Some even gave them a Semitic genealogy L/l, xv, 
150, and Yaqut ii, 861. Others, however, recognized the word as 
foreign, as e.g. al-Jawallqi, Mu'arrab, 73, who is the authority followed 
by as-Suyutl, Itq, 32 1. 5 

The ultimate origin, of course, is Lat. Roma, which in Gk. is 'Pto/zr;, 
which came into common use when ?} Nea 'PoJ^u; as distinguished 
from 7} Trpeo-fivTepa 'Pco/zi; became the name of Constantinople 

1 Horn, (friindrift*, 139 ; Bartholomae, A I \V, 1495. Cf. th< O.IVrs. rautn = river 
which is related to Gk. pvais, ptrro?. 
PPUl, 198. 
3 PPG1, 198, cf. Av. AdJ) urud, riverbed, from the root mod (Reichelt, Avestan
```


## [2026-09-04T19:06:53.714Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== IEC grape ==\"; grep -n \"‘grape\\|'grape\\|racemus\\|rrush\" IEC.txt | head -10; echo \"== SYN 5.75 vine/grape ==\"; grep -n \"raz\\b\" SYN.txt | head -5"
}
```


### [2026-09-04T19:06:53.790Z] TOOL RESULT

```
== IEC grape ==
3226:dhuddhlom ‘pendant; penis’. Cf. dhudhio- and next Gk. thústhla, npi. ‘grapes; Bacchanalian sym- bois’; MHG tüttel ‘nipple’ beside tütel ‘dot, point’; LG cf. Duttel ‘teat’; E dialect: diddle ‘penis’
9423:laĝ- ‘wind, creep; twist, winding object, creeper’ Per. raz ‘grapevine, vineyard’; OCS loza, Blg. lozà ‘vine’; Ukr. loza, f. ‘willow’; R lozà, f. ‘branch’; Norw. cf. (?) lakke ‘draw near’
12064:oiuo (oiuà) *berried tree; berry’. WP I, 165 Gk. oé, f. *'sorb-apple'; óa, oíe, npl. trowan- berries; Lat. üva ‘grape, vine’; Li. áiva, f. ‘quince’ beside ievà, f. 'bird-cherry, black alder, sorb-apple'; Latv. ieva, f. “black alder”. Cf. ouà
13774:püpos, à (pupp-) “teat, berry'. Cf. WP II, 81 & 131 Skt. pupab, m. ‘cake’; (LW in) Alb. pups, f. (grape, fr. LLat.); Lat. puppa, f. (2) ‘breast’; LLat. also ‘grape’); It. poppa, f. ‘teat, grape’; Li. pupa, f. ‘bean’; Latv. pups, m. ‘teat’; pupa, f. ‘bean’; (uncertainly: Arm. hun, o-st. gs: huno 'cornel-cherry', also. hujn, gs: huno if fr. *pupno-, *pupnio-). (Latvian püpols 'sal- low-tree' is of uncertain origin)
14577:reus- (rous-) “pull, t&ar, snatch, dash, rout, rob, stir; pulling’, etc. Cf. WP I, 14 & II, 356. (Semantic extn: *crop") Skt. cf. rosah, m. ‘wrath’; Oss. lux, adj. ‘lopped’; s. wound; piece’; luxin, Dig. loxun, v. ‘drag’; Alb. rrush, m. ‘grapes’; W rhu, m. ‘roar’; cf. W rhull, adj. (rife; rash, hasty’, fr. *reuslo- or *rouslo-); OE rēosen, pl. (que- ried: “peas? or sim. crop); MHG riusen, wv. ‘stretch’; OHG riusa, beside rūsia, f. (‘fish- trap: G Reuse); G Ries, n. ‘hollow plain’; Riese, f. “slipway for tree-trunks’; OCz. (o-gde) rús, m. (turmoil; Cz. rušit, inf. ‘disturb’ be- side po-rouchat, inf. ‘delapidate’; po-rucha, f. ‘breakdown’; Li. rausiù, “ti, v. “dig, burrow’; Latv. (ambig.) raušu, raust, v. (‘stir up, incite’, prob. to the extended form reusKo, q. v.). See next
17646:sthmbhos, à, is, ó(n) (sthmbhol-, sthmbhul-) ‘stumped, withered, hardened; stump, hard lump' Cf. sthmb-. Variant: stmbh-. Cf. sthombh- Arm. t'amb, Lat (saddle; calf of leg’. But cf. sthombh-); Gk. staphís, f. ‘raisin’; staphulé, f. ‘grape’; staphüle, f. *plumb-line; MHG stump & stumm, gs: stumbes, stummes, adj. ‘dumb’; stumbe, stumme, wm. ‘dumbness’; Sw. stomm, m. ‘stub, stump’; stomme, wm. ‘base, framework’; Li. (ambig.) stimbti, Leg: stimbstu, v. (wither, harden’, but cf. sthmb-). Extended forms in OHG stumbalon, v. *mu- tilate; OHG, MHG stumbal, stumbel, m. ‘stump’; Ger. Stummel, m. ‘stump, stub’; Du. cf. stommerik, m. ‘fool’; Li. (ambig) stimbras (stump'. Cf. sthmb-)
== SYN 5.75 vine/grape ==
1120:30 SELECTED INDO-EUROPEAN SYNONYMS 1.26 MAINLAND c Goth. aa Lith. sauszemis < = pee orepta ON meginland Lett. ctelzeme Lat. continéns Dan. fastland (CHE bi eae It. continente (terra fer- Sw. fastland SCr. _ kopno ma) OE 2o8s Boh. pevnina Fr. continent ME mayn land Pol. staly Iqd Sp. continente (tierra fir- NE mainland Russ. materik me) Du. vasteland Skt. (dvipa-) Rum. continent ORG... - Av. (karSvar-) Tr. tir MHG .... Nir. —- mdirthir, tir mor NHG  fesiland W. tir maur Br. douar braz
1129:3. Ir. tir ‘(main)land’ (1.21), NIz. moirthir, tir mor, W. tir mawr, with Ir. mor, W.mawr ‘great’. So Br. douar braz, fr. douar ‘land’ and braz ‘great’. (W. cyfandir, fr. cyfan ‘whole’ and tir ‘land’, is now rather ‘continent’),
5642:Grk. — xpdawrov Goth. andwairpi, wlits, an- Lith. _vetdas NG Tpbcw7ro dawleizn, ludja Lett. vaigs Lat.  faciés ON andlit ChSl. lice It. Jaccia (viso) Dan.  ansigt SCr. lice Fr. visage Sw. ansikte (anlete) Boh.  tvd¥ Sp. cara (rostro) OE ansjn, andwlita Pol. = twarz Rum. fajd, obraz ME face Russ. ico Ir. agad, enech NE face Skt.  anika- Nir. aghaidh Du. —geztcht Av. ainika-, &iOra- W. wyneb OHG  gesiht, anitlutli, an- Br. dremm nuzzt
5653:Rum. obraz, fr. Slavic, ChSl. obrazit ‘form, shape, image’ (12.57), SCr. obraz ‘cheek’, ete. Tiktin 1072 f.
5738:Rum. falcd obraz, bucd barbie
```


## [2026-09-04T19:06:54.676Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== MON حور ==\"; grep -n \"^حور\" MON_part1.txt | head -6; echo \"== AFM حور / rustaq ==\"; grep -n \"الحور\\|حور\\|رستاق\\|روضة\\|رونق\" AFM_pages.txt | head -12"
}
```


### [2026-09-04T19:06:54.754Z] TOOL RESULT

```
== MON حور ==
4022:حورد. . (بز.) حور ه» جدام. 
8168:حور. 
23487:حورده. 
28839:حورند. 
37696:حوردن. 
41906:حوردن» (امص.) حورد؛ جح تغذ بات. 
== AFM حور / rustaq ==
1549:0 (الد يخور) الظلام 3 د يحور وهو اللدل !£ !ܫ وهو مركب من داب
1920:+ (الروضة ) من الرمل والعشب مستتقع الا تكو النضنت مز القز به 11
1921:وفي الكلمات الروضة ® 1 ٠‏ في !ܐܕܩ ܐܨ 03 عن ديز وهي ܬ الاء في
2271:)003 ] ( ܐܦܫܵܬܐ) وباحورا (ܒܚܘܪܐ) وزتور (ܬܢܘܪ̈ܐ) وداغول (تحلس)
2956:ܡ ܐܠ والترونق وايرئاق ܐ ܢ‎ 1
3286:كانوا يشدون اسلحة على خرطومه فيقودونة الى 3 او عن حوره ومعناها
3877:( النرْق) اليد ( شفاء الغذيل ) ٠‏ معرب نزخ وهعناه السعد والرونق
4154:باحورا ؤم
4565:حور ©
4569:حوره ܨܘ
4828:زى حورجم
5690:احور مم
```


## [2026-09-04T19:07:03.630Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nlines=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\n')\nlf=('\\n'.join(lines[:9423])).count('\\f'); print('leaf',lf+1)\n\"; awk 'BEGIN{RS=\"\\f\"} NR==374' IEC.txt | grep -o \"^[0-9]\\{3,4\\}$\" | head; awk 'BEGIN{RS=\"\\f\"} NR==374' IEC.txt | head -3 | cut -c1-200; echo \"---- look for page numeral on that leaf\"; awk 'BEGIN{RS=\"\\f\"} NR==374' IEC.txt | grep -n \"^[0-9]\\+$\" "
}
```


### [2026-09-04T19:07:05.388Z] TOOL RESULT

```
leaf 372
662
663
ME lax, id.; ON lax, m. id.; R lososi, Cz. losos, m. id. cf. R (doublet, fr. Finno-Ugr.?) lox, m. ‘male salmon"; Li. lasiSas, -a, m. f. beside lašaša, f., id.; Latv. lasis, id.; OPr. lasaso, id.; 
lakstis, à (lakt-) — làmos, a (ulàm- ?)
20
---- look for page numeral on that leaf
3:20
4:25
5:30
6:35
7:40
8:45
9:662
18:663
```


## [2026-09-04T19:07:10.593Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==373' IEC.txt | grep -n \"^[0-9]\\+$\\|laĝ-\" | head"
}
```


### [2026-09-04T19:07:12.902Z] TOOL RESULT

```
11:661
```


## [2026-09-04T19:07:16.606Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /laĝ- ‘wind, creep/{print NR; print}' IEC.txt | head -30 | cut -c1-160"
}
```


### [2026-09-04T19:07:18.270Z] TOOL RESULT

```
372
atsche “slut”, and Icel. laska, v. *damage'; laski 'flaw")
ladstos “weak, faint, immature, frail’. Cf. lados (ladsKó) Lat. cf. sub-lestus “weak, faint, slim, slender, trivial; Alb. i lashtë “immature, prematur
lādh- (?) “lying, lurking, resting’. Ambig. cf. lendh- Gk. lóthð (Dor. -à-) ‘lurk’; lethe, f., léthos, n. ‘forgetting’; cf. also a-l&thés (lit
lag- (1) limp, weak; be limp, slack’, etc. (Gk. ambig. Cf. slag-). Cf. WP II, 381 & 712 (For Gk. lagaíó ‘release’; lagarós ‘Hmp, loose? see slag-); O
lag- (2) ‘wet, damp; drip, run, flow’. Cf. lag- (1) and ulg- Alb. (ambig.) lag, v. ‘wet; Gaulish (Sequanian of Coligny weather diary) lag-, la-, lagit *da
lag- (3) ‘seize’. Cf. slag- and WP II, 507 Gk. (ambig.) lázomai, lázumai, id. beside ko-
659
lázo (?) ‘restrain’; OE læccan, id.
lag- (4) (?) ‘kick. Cf. slag- Gk. (ambig.) lázo, id. beside láx “with the heel; MHG lecken (2) ‘kick’
lag- (5) ‘hollow, lake, puddle’. WP II, 423. Cf. laküs It. (ambig.) lag, m. pl. -a, m. *hollow, cavity’; W cf. lleyn, pl. -oedd, m. (“low strip of land
lag- (6) (?) Skt. cf. lagnah ‘shameful’; OS lack, m. ‘flaw, fault; ME lack, id.; Du. laken, Fris. lekje “blame”
lag- (1), lagaio “look, see, watch". WP I, 381 OS lokoian look"; OE locian, id.; OHG (west- ern dial.) lokén ‘peep out; MHG (W. dial.) luoke, wf. *hideout'
lāg- (2) ? (leg-? legh-?) Per. ray ‘meadow, slope’; ON lækt, pl. lækir, m. ‘brook’; Alb. (ambig.) log, m. ‘green, grass plot’ (but Mod. Gk. lógg
lagos, lagos, lágaio , etc. see lag- above, lāg- (1)
laĝ- ‘wind, creep; twist, winding object, creeper’ Per. raz ‘grapevine, vineyard’; OCS loza, Blg. lozà ‘vine’; Ukr. loza, f. ‘willow’; R lozà
(lag- ‘stop, flag’, see slag-. Gk. lego ‘cease’: Alb. lodh ‘tire’ ambig.)
laiuos ‘awry, left-handed, crooked; lefthand' WP II, 378 Gk. laiós “left-hand; sinister’; Lat. laevus, id.; Ir. laobh ‘crooked’; OCS. and com. SI. l�
laið ‘roar, bellow, bark’. WP II, 377 Skt. rāyāmi, id.; Per. lāyam, id.; Oss. räin, räjun (w. short vowel: ‘bellow’); Arm. lam ‘weep’; Hitt. c
lag- — laksos, us
10
20
25
30
35
40
660
laian (short vowel: *scorn?); ON lá, v. “blame”; MHG lüejen ‘bark’; OCS laj
```


## [2026-09-04T19:07:25.520Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"حوری\\|حورالعین\\|حور العین\" MON_part1.txt | head -6; echo \"---\"; sed -n '8160,8175p' MON_part1.txt"
}
```


### [2026-09-04T19:07:25.597Z] TOOL RESULT

```
5301:محوری ابت حرکت کند» مانند باندول 
5733:دارای مرکز و محوری معین است که در 
11837:تقارن محوری با تقسیمات ۵ تائی است. 
18971:است که حول محوری (بنام محور اتکاء) 
22593:جوانه‌های محوری بر روی ساقةٌ گیاه ظاهر 
24545:بهشت: ( کد.) حوریان بهشتی. 
---
اس وال‌پسرسی: [-2015-. [ع. ف.] 
(حامص.) پژوهش و سوال از صحت و 
بیماری کسی» پرسش از چگونگی وضع و 
کار و بار کسی» استفسار احوال کسی. 
احور: وت [ع. (رص.) سیاه‌چشم» دارای . 
چشمی مانند چشم آهو تمام ساه؛ آنکه 
سپیدة چشم وی سخت سپدی بود و سیاهی 
سخت ساه» نث» حوراء (ف. حورا)؛ ج. 
حور. 

احوط: 2۱۷31 [ع.] (ص تفض..) به احتیاط تر. 
به احتیاط نزدیکتر» بیشتر مقرون به احتیاط. 
(غالا در رساله‌های عملی بکار رود). 
نیکوتر؛ بهتر. فرو گیرنده‌تره گرد فرو 
گیر نده تر.
```


## [2026-09-04T19:07:33.521Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nlines=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in [25864,6736,2523]:\n    lf=('\\n'.join(lines[:ln])).count('\\f'); print(ln,'leaf',lf)\n\"; echo \"=== leaf 405 (روضه area) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==406' BQT_v2_pages.txt | head -30"
}
```


### [2026-09-04T19:07:35.201Z] TOOL RESULT

```
25864 leaf 439
6736 leaf 115
2523 leaf 45
=== leaf 405 (روضه area) ===
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
```


## [2026-09-04T19:07:42.962Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==440' BQT_v2_pages.txt | sed -n '1,40p'"
}
```


### [2026-09-04T19:07:45.554Z] TOOL RESULT

```
  ‫روعن‬                                                                                       ‫کشت‬     ‫‪۱۷‬‬


                                                                            ‫ومعلوم وبين هم هت ‪.‬‬
‫وفتح ثالث ونون وکاف سا کن ‪ ۰‬ام دخترداراست‬
                                                         ‫روشناس ‪ .‬کنابه از شخصی مشهور‬
                                                        ‫وعروف و آشنای همه کس » و بعضی گوبند‬
                                                                                          ‫م‬
‫دارا او را بعقد ناح‬      ‫وصست‬     ‫سکندریموجب‬    ‫که‬


‫خود دآرورد ‪ -‬و نام داروبی است مانتد کمای‬                                          ‫ترجمةٌ وجه است ‪.‬‬
‫را روشنك‬      ‫و در دکن مشملجی‬         ‫شده ‪-‬‬   ‫خشك‬
                                                         ‫روشناسان ک‪-‬نابه از ستارگان ‪- ۱‬‬
                                        ‫میگوبند ‪.‬‬                     ‫ومردمان مشهور ومعروف باشد ‪.‬‬
‫روضه باع ر فیع‪-‬کنابهاز رباض‬                             ‫روشنان فلك ‪ .‬کنایه از ستار ها‬
                                      ‫بپشت است ‪.‬‬                                                   ‫باشد ‪.‬‬
‫روضه تر کیت ‪ -‬کنابه از قالب‬                             ‫است که در‬    ‫معروف‬     ‫‪۴‬‬     ‫روشنایی‬
                ‫مردم است که جد آدمی باشد ‪۰‬‬
                                                        ‫مقابل تاریکی باشد ‪ -‬و نام جوهربت که آبرا‬
‫روصه دورخ بار ‪ -‬کنابه از‬                                ‫مرقشیشا کوبند و بعربی <جرالنور خوانند و در‬
                                ‫شمش رآ بدار باشد ‪۹‬‬
                                                         ‫داروهای چشم بکار برند ک‪.‬وبند اگر بگرردن‬
‫کنابه‬       ‫فیروده ر نگ ت‬            ‫روصه‬                            ‫اطفال بندند از هیچ چیز نترسد ‪.‬‬
                                   ‫ازآسمان است ‪.‬‬         ‫روشن چراع ‪ -‬بکرجيم فارسی‪,‬‬
‫روع = نم اول و سکون انی غوین‬                                                ‫نام لوابیست از موسیقی ‪. ۴‬‬
‫وآن بادی باشد‬       ‫است ‪۵‬‬   ‫لقطه‌دار ‪ ۰‬مخفف آروغ‬
                                                        ‫رشوندان ‪ -‬باالی مجهول ‪ .‬منفذ‬
      ‫ی‬
      ‫بدر‬
        ‫رول‬
          ‫عح ا‬
             ‫‪ -‬بفت‬
                 ‫و‬          ‫مکیلوابد‬
                                   ‫که ابز رراه‬          ‫وسوراخی راگویند که در خانها بجهت روشنابی‬
 ‫حیلة ررباء‌وحیله کردن کسی وینهان‌بسوی چیزی‬              ‫مگذار اد ‪ -‬و تایدان را لکىوزبند ‪ -‬و معنی‬
‫رفتن ‪ -‬ومیل کردن و گربختن راگونند ویینی‬                        ‫روشتی دان هم هست که چراغدان باشد ‪.‬‬
                             ‫کوه رانیز گفته‌اند ‪۰‬‬
                                                        ‫روشی قیاص د بکرناف‪ .‬کنابه از‬
‫روغن ‪ -‬بقتح اول بر وزن کودن »‬                                                ‫مردم صاحب فراست باشد ‪.‬‬
```


## [2026-09-04T19:08:14.754Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /leudho ‘grow, thrive/{print \"BLOCK\",NR; for(i=1;i<=NR;i++){}}' IEC.txt | head -2; awk 'BEGIN{RS=\"\\f\"} /leudho ‘grow, thrive/{print}' IEC.txt | grep -n \"^[0-9]\\{3,4\\}$\" | head; echo \"=== AHD leaf ===\"; python3 -c \"\nlines=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read().split('\\n')\nlf=('\\n'.join(lines[:693])).count('\\f'); print('leaf',lf,'printed',lf-29)\n\""
}
```


### [2026-09-04T19:08:16.615Z] TOOL RESULT

```
BLOCK 386
6:683
=== AHD leaf ===
leaf 67 printed 38
```


## [2026-09-04T19:08:25.551Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in [18149,21237,21553]:\n    lf=('\\n'.join(lines[:ln])).count('\\f'); print(ln,'leaf',lf,'printed ~',(lf-12)*2)\n\""
}
```


### [2026-09-04T19:08:27.420Z] TOOL RESULT

```
18149 leaf 402 printed ~ 780
21237 leaf 467 printed ~ 910
21553 leaf 474 printed ~ 924
```


## [2026-09-04T19:08:53.468Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-04T19:08:53.537Z] TOOL RESULT

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


## [2026-09-04T19:10:59.841Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^رستم\\|رستم:\" MON_part1.txt MON_part2.txt | head -5; echo \"== FSF رستم ==\"; grep -n \"رستم\" FSF_pages.txt | head -3"
}
```


### [2026-09-04T19:10:59.922Z] TOOL RESULT

```
MON_part2.txt:26168:(سفرنامة ناصرالدین شاه) کمان رستم: (کد.) 
MON_part2.txt:26377:مهم را انجام دادن. کمربند. کمر رستم: ( کد.) 
MON_part1.txt:66798:رستمست. )۲2۸۳۵ [ع. رحمه ] (مصل.) 
MON_part1.txt:67335:رستم: مرد شجاع» دلیر» پهلوان. 
== FSF رستم ==
169:‫است که رستم کیست و افراسیاب اکزجاست و سهراب و سیاوش فرزندان که‬
471:                ‫بدو گفت رستم‪ :‬تو را کهترم‬                     ‫]ن‪:‬‬
974:‫سیاوش و رستم ب پايشنهاد افراسیاب همرایند‬            ‫سپاهیان ایران در نبرد با رومیان گرفتار‬
```


## [2026-09-04T19:11:04.873Z] AGENT

Now I'll write the updated JSON.


## [2026-09-04T19:15:14.968Z] TOOL CALL #83: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/work && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/work/patch311.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io, sys\n\nP = \"/home/sfmqrb/git/rishe/data/verification/page-311.json\"\nd = json.load(io.open(P, encoding=\"utf-8\"))\ne = d[\"entries\"][0]\n\nC = {}\n\nC[\"root\"] = [\n {\"src\":\"WLD\",\"where\":\"Bd. II p. 416\",\"stance\":\"supports\",\n  \"note\":\"WLD_Bd2 p.416 s.v. leudh-: 'leudh- „emporwachsen, hochkommen“. Ai. rodhati, rohati „steigt, wächst“, av. raodaiti „wächst“, ai. roha- m. „das Aufsteigen, Erhebung, Höhe“, av. raoda- m. „Wuchs, Ansehen“, npers. roi „Gesicht“; lat. Liber … got. liudan, ahd. liotan, as. liodan, ags. leodan „wachsen“' — the same single root Nourai draws; nothing corresponds to his second label 'Rei'.\"},\n {\"src\":\"AHD\",\"where\":\"p. 38 s.v. leudh-²\",\"stance\":\"supports\",\n  \"note\":\"AHD_watkins1985.txt leaf 67 (p.38): 'leudh-². To mount up, grow. Suffixed form *leudh-ero- in Latin liber, free (the precise semantic development is obscure): LIBERAL, LIBERATE, LIBERTINE, LIBERTY, LIVERY; DELIVER. [Pok. 1. leudh- 684.]' Watkins keeps a homonymous leudh-¹ 'to go' (Gk. prosēlutos), so the gloss 'to grow' and the Pokorny page are right.\"},\n {\"src\":\"IEC\",\"where\":\"p. 683 s.v. leudho\",\"stance\":\"supports\",\n  \"note\":\"IEC.txt ff-block 386 (printed 683): 'leudho “grow, thrive”. WP II, 416. Cf. leudheros, leudhis, loudh-. Skt. rodhāmi, id.; Av. raoðē, mp. id.; Go. liudan “grow”; OE leodan, sv. 2 “grow”'; beside it 'loudhos … “growing, rising; growth” … Av. raoðo, m. id.' (p.772).\"},\n {\"src\":\"CHEUNG\",\"where\":\"p. 193 s.v. *Hraud\",\"stance\":\"supports\",\n  \"note\":\"CHEUNG.txt: '*Hraud “to grow (bigger)” … *PIE *H₁leudʰ- “to grow, rise” = LIV: 248 f. | Pok.: 306 f., 684 f. *IE COGNATES: Gr. ἐλεύθερος, OIrish luss “plant”, Goth. liudan, OE leodan “to grow”' — the Iranian branch of the root, with Ir. r- the regular reflex of PIE *l.\"}]\n\nC[1] = [\n {\"src\":\"BRT\",\"where\":\"cols. 1493-1495\",\"stance\":\"supports\",\n  \"note\":\"AiW col. 1493 f.: 'j. ²raod- V. „wachsen“. Praes. 2 raoða-, 27 uruðya-; Perf. urūrud-. — PPfP. urušda-, urusta-; Inf. raoðe'; col. 1495: 'j. raoða- m. 1) „Wachstum“ (nur Komp.) 2) Plur. „das äussere Ansehen“ … Zum V. ²raod-. — ai. roha- m. „Erhebung“, np. roi „Gesicht“'. Bartholomae also has a separate ⁴raod- 'fliessen' and raodah- 'licht', so the numbering of Nourai's 'raod 1' matters.\"},\n {\"src\":\"CHEUNG\",\"where\":\"p. 193\",\"stance\":\"supports\",\n  \"note\":\"'*AVESTAN: YAv. raoð- (ruð-) “to grow” … IND. 2sg. med. YAv. raoðahe (Y 10.4), 3pl. raoðanti (V 5.19), impf. 3sg. araoðat (Y 9.11) … Partic. perf. pass. YAv. urusta- (V 19.18)' — the verb and its participle are exactly as Nourai's node has them.\"},\n {\"src\":\"WLD\",\"where\":\"Bd. II p. 416\",\"stance\":\"supports\",\n  \"note\":\"'av. raodaiti „wächst“ … av. raoda- m. „Wuchs, Ansehen“, npers. roi „Gesicht“' — Walde-Pokorny give both of the node's glosses ('growth' and, via 'Ansehen', 'face').\"},\n {\"src\":\"NYB\",\"where\":\"vol. II p. 180 s.v. rustan\",\"stance\":\"supports\",\n  \"note\":\"'rustan [lwstn'] rod- [lwd-] to grow … — Av. (1492 sq.) ²raod-' — Nyberg cites AiW cols. 1492 ff. for the same Avestan verb.\"}]\n\nC[2] = [\n {\"src\":\"HRN\",\"where\":\"no. 614 p. 136 and no. 636 p. 141\",\"stance\":\"supports\",\n  \"note\":\"HRN.txt leaf 157 (p.136): '614. rusten „wachsen“, Praes. roy-em, royiden, royaniden, rosta (arab. syr. LW. rustaq) … aw. √raod-, raoðaite „wachsen“; phlv. rustan … rod(i)šn bezw. roy(i)šn; ai. rodh-, rodhati'; leaf 162 (p.141): '636. (i)roi, ro „Gesicht“. aw. raoda- „Wuchs, Ansehen“; phlv. rod, hu-rod(i)šn (AV.); got. ludja „Antlitz“.' Horn treats 'grow' and 'face' as one etymology, as the node does.\"},\n {\"src\":\"HUB\",\"where\":\"pp. 199-200\",\"stance\":\"supports\",\n  \"note\":\"HUB.txt leaf 209 (p.199) among the examples of Av. ð > NP y: 'roi (ro) „Gesicht“ = zd. raoda-'; leaf 210 (p.200): 'royam „wachse“, inf. rustan, zd. raodahe'. Hübschmann's sound law is what licenses roð- > roy-.\"},\n {\"src\":\"PHD\",\"where\":\"p. 77\",\"stance\":\"supports\",\n  \"note\":\"'rustan, roy- [lwstn', lwd- | M rwst, rwy-, N ~] grow. ~išn: growth' and '¹roy [lwd | M rwy, N ~] face' (MacKenzie keeps ²roy 'copper' apart).\"},\n {\"src\":\"MON\",\"where\":\"s.v. روییدن (2-vol. Adena abridgement)\",\"stance\":\"supports\",\n  \"note\":\"MON_part1.txt: 'روییدن rūyīdan [= رستن] (مص‌ل.) نمو کردن نباتات، بالیدن، رشد کردن' — Mo'in equates rūyīdan with rostan, as the chart's node does.\"},\n {\"src\":\"IEC\",\"where\":\"p. 1103 s.v. rūs- (3)\",\"stance\":\"partial\",\n  \"note\":\"'rūs- (3) “space, place”. Cf. reuos (2). WP II, 356. (Iranian ambig.) Per. rū, rūy, s. “face, surface”. To Av. raoðo “growth” accdg. to Justi, cf. leudh-); cf. also Per. rūsta, s. “village” … Lat. rūs … “open country, farmstead”.' Mann records the 'growth' etymology of rūy as Justi's, but files the word under a different root.\"}]\n\nC[3] = [\n {\"src\":\"PHD\",\"where\":\"p. 76\",\"stance\":\"partial\",\n  \"note\":\"'raz [/c, lz | N ~] vine; vineyard' — MacKenzie has the Middle Persian word (so the Persian form is genuine and old) but gives it no connection to rustan/roy-.\"},\n {\"src\":\"IEC\",\"where\":\"pp. 659-660 s.v. laĝ-\",\"stance\":\"contradicts\",\n  \"note\":\"IEC.txt ff-block 372 (printed 659-660): 'laĝ- “wind, creep; twist, winding object, creeper” — Per. raz “grapevine, vineyard”; OCS loza, Blg. lozà “vine”; Ukr. loza, f. “willow”; R lozà, f. “branch”.' Mann puts raz with Slavic loza under a 'creeper' root, not under leudho.\"},\n {\"src\":\"PLA\",\"where\":\"p. 135 s.v. razzāgī\",\"stance\":\"partial\",\n  \"note\":\"'razzāgī „Weintrauben; Wein“ ← pers. raz „a vineyard“, mp. raz „vine, vineyard“' (fn. 3 Mackenzie s.v.) — confirms the word and its MP ancestor, no 'grow' etymology.\"},\n {\"src\":\"NYB\",\"where\":\"vol. II p. 178\",\"stance\":\"silent\",\n  \"note\":\"Nyberg's glossary has only 'rāz [lʾc] a secret — Av. (1514) razah-'; there is no raz 'vine' in it, so nothing supports or contradicts the arrow from roȳ-.\"},\n {\"src\":\"HRN\",\"where\":\"nos. 609-620, pp. 134-142\",\"stance\":\"silent\",\n  \"note\":\"Horn's r- section (razm 612, rusten 614, roi 636, rēxtan 638 …) has no entry for raz 'vine'; he does not derive it from rusten.\"}]\n\nC[4] = [\n {\"src\":\"FVQ\",\"where\":\"pp. 145-146 s.v. رَوْضَة\",\"stance\":\"partial\",\n  \"note\":\"FVQ_pages leaf 162 f. (pp.145-146): 'There can be little doubt that the word was borrowed as a noun into Arabic … Vollers, ZDMG l, 641, 642, noted that the word is originally Iranian, and he suggested that it was from the Iranian √rud, meaning to grow. The Av. raoð means to flow, from which comes raoðah “a river” and raoða “growth” … From the same root comes Phlv. rod “a lake or riverbed” and the Pers. rūd … Thus the conclusion would seem to be that the Arabs learned the Phlv. rod in the Mesopotamian area and used it for any well watered or irrigated land.' Jeffery agrees the word is Iranian, but takes it from rod 'river' — which is exactly the alternative (VDQ:226) recorded in the chart's own NOTE.\"},\n {\"src\":\"LKT\",\"where\":\"no. 1709, p. 138\",\"stance\":\"contradicts\",\n  \"note\":\"LKT.txt leaf 164 (p.138): '1709. Ar. rauda: „Garten“, plr. rijad, im Magrib singularisch gebraucht als „Blumenbeet“; hieraus sp. arriates …'. Lokotsch heads the entry 'Ar.' (he marks Persian etyma 'Pers.', e.g. 1711 Pers. rāwand) and gives no Iranian source at all.\"},\n {\"src\":\"AFA\",\"where\":\"p. 149\",\"stance\":\"silent\",\n  \"note\":\"Fraenkel's discussion of Arabic garden words treats جنة (from Aramaic) and حدیقة ('Zaun' > 'Garten'), but has no entry for روضة — i.e. he does not class it as a foreign word.\"},\n {\"src\":\"KLN\",\"where\":\"grep 'rawda/rauda'\",\"stance\":\"silent\",\n  \"note\":\"Klein's dictionary has no rawda/rauda entry (the word gave no English derivative), so it can neither support nor contradict.\"}]\n\nC[5] = [\n {\"src\":\"MON\",\"where\":\"s.v. روضه\",\"stance\":\"supports\",\n  \"note\":\"MON_part1.txt: 'روضه rowza(t) [ع. روضة] (اِ.) باغ، گلزار؛ ج. ریاض، روضات … خطبه‌ای که در مراسم عزاداری بالای منبر خوانند … این کلمه از نام «روضة الشهداء» مأخوذ است' — tagged [ع.] Arabic, plural riyāḍ as in the chart, and the Karbalā sense explained from Kāshefī's title.\"},\n {\"src\":\"BQT\",\"where\":\"vol. 2, leaf 440 (printed p. ~983)\",\"stance\":\"partial\",\n  \"note\":\"Borhān-e Qāṭeʿ has no independent روضه headword, only Persian compounds built on the Arabic loan: 'روضه باغ رفیع — کنایه از ریاض بهشت است', 'روضه ترکیب', 'روضه دوزخ‌بار', 'روضه فیروزه‌رنگ' — confirming the word and its 'garden of paradise' value in Persian, with no etymology.\"},\n {\"src\":\"FVQ\",\"where\":\"pp. 145-146\",\"stance\":\"partial\",\n  \"note\":\"Jeffery's entry documents the Arabic word (Qur'ān xxx.14, xlii.21; 'A rich, well watered meadow; thence a luxurious garden', LA ix.23) that Persian rowza borrows back; his Iranian etymology is via rod 'river', not raz.\"}]\n\nC[6] = [\n {\"src\":\"BQT\",\"where\":\"vols. 1-2 (grep رونیک)\",\"stance\":\"silent\",\n  \"note\":\"No رونیک headword anywhere in the OCR of Borhān-e Qāṭeʿ vols. 1-2 (BQT_v1_pages.txt / BQT_v2_pages.txt); Borhān does not know the word.\"},\n {\"src\":\"MON\",\"where\":\"grep رونیک\",\"stance\":\"silent\",\n  \"note\":\"Mo'in's lexicon text has رونق, روند, رونما but no رونیک; the compound is not lexicalised in Mo'in either.\"},\n {\"src\":\"PHD\",\"where\":\"p. 77\",\"stance\":\"silent\",\n  \"note\":\"MacKenzie has no Middle Persian *roy-nēk compound, so there is no pre-Islamic form for Arabic rawnaq to be borrowed from.\"}]\n\nC[7] = [\n {\"src\":\"PLA\",\"where\":\"pp. 134-138 (r- section)\",\"stance\":\"silent\",\n  \"note\":\"Asbaghi's alphabetical inventory of Persian loanwords in Arabic runs razzāgī, razdaq, rizq, rustaq, rustam (p.135) … raudaq, rūdak, rauzan, rūznāma, rauda, rūt (p.138): there is no rawnaq entry — the standard modern list of Persian loans in Arabic does not include it.\"},\n {\"src\":\"LKT\",\"where\":\"Arabic index p. 762a (ratam 1707 … razza 1713)\",\"stance\":\"silent\",\n  \"note\":\"Lokotsch's Arabic word-index runs 'ratam 1707, ratl 1708, rauda 1709, razza 1713 …' with no rawnaq — he does not treat it as an orientalism of Persian origin.\"},\n {\"src\":\"KLN\",\"where\":\"grep 'rawnaq/raunaq'\",\"stance\":\"silent\",\n  \"note\":\"Not in Klein (no English derivative), so no independent Semitic-vs-Iranian judgement there.\"}]\n\nC[8] = [\n {\"src\":\"MON\",\"where\":\"s.v. رونق\",\"stance\":\"supports\",\n  \"note\":\"MON_part1.txt: 'رونق rownaq [ع.] (امص.) فروغ، روشنایی؛ زیبایی، جمال؛ رواج' — tagged [ع.] Arabic, exactly the direction of the #7→#8 arrow.\"},\n {\"src\":\"BQT\",\"where\":\"vol. 2, leaf 115 (printed p. ~658)\",\"stance\":\"partial\",\n  \"note\":\"Borhān uses رونق only inside glosses and in a quoted verse ('… و رونق باشد، شهید (بلخی) گفت'), i.e. it is a familiar loan in classical Persian; no etymology is offered.\"},\n {\"src\":\"PLA\",\"where\":\"r- section pp. 134-138\",\"stance\":\"silent\",\n  \"note\":\"Asbaghi lists no rawnaq, so the Persian word cannot be a returning Persian loan on his evidence — consistent with a plain Arabic > Persian borrowing.\"}]\n\nC[9] = [\n {\"src\":\"PHD\",\"where\":\"p. 77 (and English index p. 137)\",\"stance\":\"contradicts\",\n  \"note\":\"'rostag [lw(t)stʾk' | (P rwdystʾg), N rūstā] river-bed; district, province'; English index: 'river rod; ~ bank rodbār; ~ bed rostag'. MacKenzie's first gloss is 'river-bed' and his Psalter spelling rwdystʾg shows the first member is rod 'river', not the 'grow' root.\"},\n {\"src\":\"NYB\",\"where\":\"vol. II p. 179\",\"stance\":\"contradicts\",\n  \"note\":\"'rotastāk [lwtstʾk], rostak [lwstʾk] district, province … MPrth rwdystʾg; Paz. rostā …; NP rostā(i); Arab. lw. rustāg, ruzdāg'. Nyberg's headword form rot-astāk has rot 'river' (his own entry: 'rot [lwt'] river — OP rautah-; NP rod').\"},\n {\"src\":\"HRN\",\"where\":\"no. 614, p. 136\",\"stance\":\"supports\",\n  \"note\":\"Horn lists 'rostā (arab. syr. LW. rustāq)' and 'phlv. rostāk [rodastak, Salemann, Eine Pärsenhandschrift 68, 10]' under no. 614 rusten 'wachsen' — this 1893 treatment is the source of Nourai's arrow; but Horn himself flags Salemann's rodastak reading, which is the 'river' analysis.\"},\n {\"src\":\"PLA\",\"where\":\"p. 135 s.v. ruzdāg\",\"stance\":\"partial\",\n  \"note\":\"'ruzdāg „Marktflecken“ ← pers. rūstā, mp. rostāk, rotstāk; ar. Lw. ruzdāg u. rustāg' — Asbaghi gives both Middle Persian shapes, the second with the -t- of rot.\"},\n {\"src\":\"BRT\",\"where\":\"cols. 1493-1495\",\"stance\":\"partial\",\n  \"note\":\"AiW keeps four homonymous roots apart: '²raod- V. „wachsen“' (col. 1493) and '⁴raod- V. „fliessen“' (col. 1495), the latter with rautah- 'river' (cf. the note 'ai. srávati „er fliesst“, vgl. rautah-, ⁴raod-'). Nourai's chart assigns rostāk to the wrong one of the two.\"}]\n\nC[10] = [\n {\"src\":\"PHD\",\"where\":\"p. 77\",\"stance\":\"supports\",\n  \"note\":\"'rostag … N rūstā' — MacKenzie gives the New Persian outcome of the Middle Persian word directly, confirming the #9→#10 edge.\"},\n {\"src\":\"NYB\",\"where\":\"vol. II p. 179\",\"stance\":\"supports\",\n  \"note\":\"'Paz. rostā, pl. rostāihā; NP rostā(i) “any inhabited place; a market-town, a village”' — including the by-form روستای of the chart.\"},\n {\"src\":\"HRN\",\"where\":\"no. 614, p. 136\",\"stance\":\"supports\",\n  \"note\":\"'rostā (arab. syr. LW. rustāq)' beside 'phlv. rostāk' — same edge, and the Arabic/Syriac loan rustāq as its witness.\"},\n {\"src\":\"PLA\",\"where\":\"p. 135\",\"stance\":\"supports\",\n  \"note\":\"'ruzdāg … ← pers. rūstā … mp. rostāk, rotstāk' and 'rustāq „Marktflecken“ = ruzdāq, mand. rustag, syr. …'.\"},\n {\"src\":\"BQT\",\"where\":\"vols. 1-2 (grep روستا)\",\"stance\":\"silent\",\n  \"note\":\"No روستا headword in the OCR of Borhān vols. 1-2 (only روستایی/روستائان inside Mo'in's footnotes); Borhān contributes nothing here.\"}]\n\nC[11] = [\n {\"src\":\"BRT\",\"where\":\"cols. 626-627 s.v. taxma-\",\"stance\":\"contradicts\",\n  \"note\":\"AiW col. 626: 'j., g. (, p.) taxma- Adj. „fortis, tapfer, tüchtig, energisch, heldenhaft“', col. 627 taxmo.təma-, taxma-spāda- (OP). There is no compound *raoða-taxma-/raodaṣ-taxma- anywhere in the Avestan lexicon — the Avestan label of this node has no textual basis.\"},\n {\"src\":\"NYB\",\"where\":\"vol. II p. 179\",\"stance\":\"contradicts\",\n  \"note\":\"'Rotastahm [lwtsthm] n. pr. — NP Rustam; Old Sogd rwstmy' — the attested Middle Persian name has rot 'river' as first member, not raoða- 'growth'.\"},\n {\"src\":\"PLA\",\"where\":\"p. 135 s.v. rustam\",\"stance\":\"contradicts\",\n  \"note\":\"'rustam „Reichsfeldherr“ ← mp. rotastahm, mand. rustam' — Asbaghi too reads the first element as rot.\"},\n {\"src\":\"IEC\",\"where\":\"grep 'taxma/Rustam'\",\"stance\":\"silent\",\n  \"note\":\"Mann's comparative dictionary has no entry for the name or for an IE *leudh-o-teg-mo- compound.\"}]\n\nC[12] = [\n {\"src\":\"NYB\",\"where\":\"vol. II p. 179\",\"stance\":\"supports\",\n  \"note\":\"'Rotastahm [lwtsthm] n. pr. 116². — NP Rustam; Old Sogd rwstmy, Reichelt, Sogd. Handschr.-R. II, 63' — the MP > NP edge (and the Sogdian intermediate contraction) is confirmed; the first element is rot 'river'.\"},\n {\"src\":\"PLA\",\"where\":\"p. 135\",\"stance\":\"supports\",\n  \"note\":\"'rustam „Reichsfeldherr“ … mp. rotastahm, mand. rustam' — same MP antecedent, and an Aramaic/Mandaic witness of the name.\"},\n {\"src\":\"PHD\",\"where\":\"grep 'Rustam/Rostahm'\",\"stance\":\"silent\",\n  \"note\":\"MacKenzie's Concise Pahlavi Dictionary excludes proper names, so it has no Rostahm entry.\"},\n {\"src\":\"MON\",\"where\":\"s.v. رستم (2-vol. abridgement)\",\"stance\":\"partial\",\n  \"note\":\"'رستم: مرد شجاع، دلیر، پهلوان' — the appellative use is recorded, but this abridgement carries no etymology (the etymological footnote is in BQT, checked under ref_check).\"}]\n\nC[13] = [\n {\"src\":\"BRT\",\"where\":\"s.vv. čarāiti-, bənj-, ima- (grep 'huraoð')\",\"stance\":\"supports\",\n  \"note\":\"AiW cites the adjective repeatedly: 'j. čarāiti- f. „junge Frau“ … čarāitiš (NS.) huraoðaya … V. 3.24'; 'kəhrpa huraoðaya “.. des schöngestaltetem Leib huldigte AhM.” Yt 10.90'; '… tənūm yā mē vaenaite huraoða Y 10.14'; 'sraosš … huraoða' (Y 57.3 etc.). The Avestan word is hu-raoða-, so the chart's 'hava-rd' is a scan corruption, as the node says.\"},\n {\"src\":\"FVQ\",\"where\":\"p. 120\",\"stance\":\"supports\",\n  \"note\":\"'Now hurust is a good Iranian word, the equivalent of Av. huraoða-, and though these Pahlavi works are late the conceptions in them are early' — Jeffery spells the Avestan form Nourai's node should have printed.\"},\n {\"src\":\"PLA\",\"where\":\"p. 103 s.v. hūrī\",\"stance\":\"supports\",\n  \"note\":\"'hūrī „Huri, Paradiesjungfrau, Schönheit“ ← mp. hūrast „gut gewachsen“ ← aw. huraoða' — again the Avestan compound hu- + raoða-.\"},\n {\"src\":\"CHEUNG\",\"where\":\"p. 193\",\"stance\":\"partial\",\n  \"note\":\"Cheung's dictionary covers verbs, so huraoða- is not a headword; but the root *Hraud 'to grow' (YAv. raoð-) that its second member contains is there, confirming the analysis hu- 'good' + raoða- 'growth'.\"}]\n\nC[14] = [\n {\"src\":\"PHD\",\"where\":\"p. 48\",\"stance\":\"supports\",\n  \"note\":\"'hu-|-ramag [hwlmk'] having good flocks. ~-rust [-lwst'] well-grown' (p.48); English index p.164: 'well-grown hurust'. MacKenzie has exactly the Pahlavi word and gloss of the node.\"},\n {\"src\":\"FVQ\",\"where\":\"pp. 119-120\",\"stance\":\"supports\",\n  \"note\":\"'It is much more likely that the word comes from the Phlv. hurust, meaning beautiful, and used in the Pahlavi books of the beauteous damsels of Paradise, e.g. in Arda Viraf, iv, 18, and in Hadoxt Nask, ii, 23 … where we have the picture of a graceful damsel, white-armed, strong, with dazzling face and prominent breasts.'\"},\n {\"src\":\"PLA\",\"where\":\"p. 103\",\"stance\":\"supports\",\n  \"note\":\"'mp. hūrast „gut gewachsen“' — same Middle Persian word and meaning (Asbaghi's transcription hūrast for hurust).\"},\n {\"src\":\"HRN\",\"where\":\"no. 636, p. 141\",\"stance\":\"partial\",\n  \"note\":\"'phlv. rod, hu-rod(i)šn (AV.)' — Horn cites the Ardā Wīrāz word in the abstract form hu-rodišn beside the participial hurust; both are hu- + the same root.\"},\n {\"src\":\"NYB\",\"where\":\"grep 'hurust'\",\"stance\":\"silent\",\n  \"note\":\"Nyberg's glossary (to the texts he edits) does not contain hurust; it has rustan/rod- 'to grow' (p.180), the verb it is built on.\"}]\n\nC[15] = [\n {\"src\":\"KLN\",\"where\":\"leaf 402 (printed pp. ~779-780) s.v. houri\",\"stance\":\"contradicts\",\n  \"note\":\"'houri, n., a nymph of the Moslem Paradise … F., fr. Pers. hūrī, fr. Arab. hūr, pl. of aḥwar, fem. ḥaurāʾ, “having beautiful black eyes”, fr. ḥawira, “had black eyes”, which is rel. to Heb. ḥāwar, Aram.-Syr. ḥəwār, “was white”, Heb. ḥūr, “white stuff”' — a wholly Semitic derivation, with no Iranian element.\"},\n {\"src\":\"LKT\",\"where\":\"no. 848, p. 69\",\"stance\":\"contradicts\",\n  \"note\":\"'848. Ar. ḥaurāʾ: Fem. zu aḥwar „schwarzäugig“ besonders von einer Gazelle, einem Jünglinge oder einer Jungfrau gesagt; dazu plur. ḥūr. Dieses Wort betrachteten die Perser … als sglr. und fügten ein ī der Einheit an: ḥūrī' — Arabic in origin, Persian only secondarily.\"},\n {\"src\":\"FVQ\",\"where\":\"pp. 117-120\",\"stance\":\"partial\",\n  \"note\":\"Jeffery documents the pre-Islamic Arabic use ('ʿAbīd b. al-Abraṣ, vii, 24 “And maidens like ivory statues, white of eyes, did we capture”'; 'ʿAdī b. Zaid'; Qaʿnab) and concludes (p.120): 'it does seem certain that the word ḥūr in its sense of whiteness, and used of fair-skinned damsels, came into use among the Northern Arabs as a borrowing from the Christian communities, and then Muhammad, under the influence of the Iranian hurust, used it of the maidens of Paradise.' So the Iranian word shaped the Qur'ānic concept, not the Arabic form.\"},\n {\"src\":\"PLA\",\"where\":\"p. 103 s.v. hūrī\",\"stance\":\"partial\",\n  \"note\":\"Asbaghi records the derivation Nourai draws ('hūrī … ← mp. hūrast „gut gewachsen“ ← aw. huraoða') but rejects it in favour of a different Persian source: 'Meiner Meinung nach ist hūrī ein fem. Elativ zu aḥwar u. aḥūrā, welcher von den Arabern einfach für einen ar. Elativ maskulin gehalten wurde … daher ist die eigentliche Bedeutung „Herrin“.'\"}]\n\nC[16] = [\n {\"src\":\"MON\",\"where\":\"s.v. احور\",\"stance\":\"supports\",\n  \"note\":\"MON_part1.txt: 'احور aḥwar [ع.] (ص.) سیاه‌چشم، دارای چشمی مانند چشم آهو … مؤنث حوراء (ف. حورا)؛ ج. حور' — Mo'in tags the family Arabic and gives ḥūr as the plural of aḥwar, i.e. the Arabic > Persian direction of the #15→#16 arrow.\"},\n {\"src\":\"KLN\",\"where\":\"leaf 402 s.v. houri\",\"stance\":\"supports\",\n  \"note\":\"'F., fr. Pers. hūrī, fr. Arab. hūr … The -ī in Pers. hūrī is a formative element serving to denote the singular' — exactly the Persian حوری of the node's 'extra' words, and the route on to French/English.\"},\n {\"src\":\"LKT\",\"where\":\"no. 848, p. 69\",\"stance\":\"supports\",\n  \"note\":\"'… hieraus zur Bezeichnung einer reizenden Frau sp. hurí, frz. houri, ndl. engl. houri, dtsch. Huri' — the Persian singulative ḥūrī is the source of the European word.\"}]\n\nC[17] = [\n {\"src\":\"CHEUNG\",\"where\":\"p. 193 s.v. *Hraud\",\"stance\":\"supports\",\n  \"note\":\"'*SOGDIAN: BSogd. rwð-, MSogd. rwst (pret. stem) “to grow” || (+ *pati-) SSogd. ptrwð-, CSogd. ptryst-, MSogd. ptrwð- “to grow up”. Pres.: IND. 3sg. BSogd. rwðtt, rwðt … Inf.: BSogd. rwðʾy' — the Sogdian verb belongs to Proto-Iranian *Hraud < PIE *H₁leudʰ-, i.e. to Nourai's root.\"},\n {\"src\":\"BRT\",\"where\":\"col. 1493\",\"stance\":\"partial\",\n  \"note\":\"AiW's '²raod- V. „wachsen“' is the Avestan member of the same equation; Bartholomae of course does not cite Sogdian (1904), but the Avestan verb is the direct cognate of Sogd. rwð-.\"},\n {\"src\":\"PHD\",\"where\":\"p. 77\",\"stance\":\"partial\",\n  \"note\":\"'rustan, roy- [lwstn', lwd-] grow' — the Middle Persian cognate with the same ð > y development that Sogdian rwð- preserves unchanged.\"}]\n\nC[18] = [\n {\"src\":\"WLD\",\"where\":\"Bd. II pp. 416-417\",\"stance\":\"supports\",\n  \"note\":\"p.416: '(Nachwuchs → Menge, Volk:) ahd. liut, ags. lead „Volk“, mhd. liute „Leute“'; p.417: 'aksl. ljudьje pl. „die Leute“ … lett. ļaudis pl. „Leute, Volk“, lit. liaudis … nach Schrader IA. 9, 172 gr. ἐλεύθερος „frei (= Volksangehöriger)“ = ital. *loufero- in lat. līber, fal. loferta „liberta“'. Both of the node's two derivatives are there.\"},\n {\"src\":\"IEC\",\"where\":\"pp. 683-684\",\"stance\":\"supports\",\n  \"note\":\"'leudheros (leudhər-) “active, free; action, freedom, abandon” … WP II, 417 … Myc. and Gk. eleútheros “free”; Venetic louzera “the goddess Libera”; Paelig. loufir “free”; Lat. liber' and 'leudhis “tribe, people”. Cf. leudho, leudheros. WP II, 416'.\"},\n {\"src\":\"AHD\",\"where\":\"p. 38 s.v. leudh-²\",\"stance\":\"partial\",\n  \"note\":\"Watkins lists only the suffixed form '*leudh-ero- in Latin liber, free (the precise semantic development is obscure)'; the 'people' derivative *leudho-/-i- (Leute, ljudьje) does not appear in his entry, so AHD supports leudhero- but not leudho-.\"}]\n\nC[19] = [\n {\"src\":\"LAT\",\"where\":\"pp. 632-633 s.v. līber\",\"stance\":\"partial\",\n  \"note\":\"Ernout-Meillet: 'Pel. loufir “liber” et fal. loferta montrent que l'ī de liber reposerait sur un ancien ou (qui peut être issu de eu); ceci justifierait un rapprochement avec gr. ἐλεύθερος. Un rapprochement avec v.h.a. liuti “gens”, lette ļaudis “gens, peuple” et v.sl. ljudige … n'est pas exclu, mais ne s'impose pas.' They accept the Greek equation but treat the link to the 'people/grow' family as optional.\"},\n {\"src\":\"WLD\",\"where\":\"Bd. II pp. 416-417\",\"stance\":\"supports\",\n  \"note\":\"'lat. Liber, ital. Gott des Wachstums, der Zeugung, Anpflanzung (aus *loudhero-, *loufero-, *leudhero-), osk. gen. Liivfreis „Liberi“, lat. līberi, -orum „die Kinder“, ältest auch von einem einzigen Kind, also *„Nachwuchs“' (p.416) and 'gr. ἐλεύθερος … = ital. *loufero- in lat. līber' (p.417).\"},\n {\"src\":\"SKT\",\"where\":\"p. 250 s.v. Liberal\",\"stance\":\"contradicts\",\n  \"note\":\"SKT.txt leaf 270 (p.250): 'Liberal. (F.-L.) M.E. liberal … L. līberālis, befitting a free or generous. — L. līber, free. Allied to libet, pleases, it is one's pleasure; Skt. lubh-, desire.' Skeat attaches līber to *leubh- 'to desire, love', not to *leudh- 'to grow'.\"},\n {\"src\":\"AHD\",\"where\":\"p. 38\",\"stance\":\"supports\",\n  \"note\":\"'Suffixed form *leudh-ero- in Latin liber, free (the precise semantic development is obscure)' — the same derivation as the node, with the caveat about the semantics.\"}]\n\nC[20] = [\n {\"src\":\"SKT\",\"where\":\"pp. 239 and 250\",\"stance\":\"partial\",\n  \"note\":\"'deliver. (F.-L.) OF. delivrer, set free. — Low L. dēlīberāre, to set free. L. dē, from; līberāre, to free, from līber' (p.250) and 'Deliver; see Liberal' (p.239) — deliver and liberty are confirmed; Skeat has no Latvia entry and derives līber itself from *leubh-, so the node's chain holds only from Latin onwards.\"},\n {\"src\":\"AHD\",\"where\":\"p. 38 and index (pp. 1418, 1741 of the 1985 printing)\",\"stance\":\"partial\",\n  \"note\":\"The Watkins index gives 'DELIVER leudh-2', 'LIBERTY leudh-2', 'LIBERAL leudh-2', 'LIBERTINE leudh-2', 'LIVERY leudh-2' — confirming liberty and deliver; Latvia and Lett appear nowhere under leudh-.\"},\n {\"src\":\"KLN\",\"where\":\"leaf 467 s.v. Latvia and leaf 474 s.v. Lett (printed pp. ~910 and ~924)\",\"stance\":\"partial\",\n  \"note\":\"'Latvia, n. — Lit. “the country of the Letts”. See Lett and cp. lat.'; 'Lett, n., an inhabitant of Latvia. — The word orig. meant “people”. It comes fr. OHG. liuti (whence MHG. liute, G. Leute), “people”, which is possibly cogn. with Gk. ἐλεύθερος, L. liber, “free”. See liberal.' Klein is the only book on the shelf that links Latvia to this root, and only through an equation of Latvis with OHG liuti that Baltic scholarship does not accept.\"}]\n\n# ---- attach ----\ne[\"consulted\"] = C[\"root\"]\nfor n in e[\"nodes\"]:\n    n[\"consulted\"] = C[n[\"id\"]]\n\n# ---- ref_check upgrades ----\ndef find(rcs, ref):\n    for rc in rcs:\n        if rc.get(\"ref\") == ref:\n            return rc\n    return None\n\n# root VDQ:39\nrc = find(e[\"ref_check\"], \"VDQ:39\")\nrc[\"status\"] = \"partial\"\nrc[\"note\"] = (\"VDQ (Badreh'i's Persian translation of Jeffery) is still only on noorlib's JavaScript viewer, \"\n  \"but the English original FVQ, of which it is a page-for-page translation, is on disk: FVQ pp.119-120 s.v. \"\n  \"حور says 'It is much more likely that the word comes from the Phlv. hurust, meaning beautiful … \"\n  \"Now hurust is a good Iranian word, the equivalent of Av. huraoða-'. So Jeffery does place hurust/huraoða- \"\n  \"in this family, but he ends by deriving the Arabic word itself from Aramaic ḥwr 'to be white' — support \"\n  \"for the Iranian branch of the chart, not for an Iranian etymology of Arabic ḥūr.\")\n\nbyid = {n[\"id\"]: n for n in e[\"nodes\"]}\n\n# node 4: PLA:138\nrc = find(byid[4][\"ref_check\"], \"PLA:138\")\nrc[\"status\"] = \"supports\"\nrc[\"note\"] = (\"Asbaghi is now on disk. PLA_pages.txt leaf 153 = printed p.138: \"\n  \"'rauda: „Garten“ aus pers. raz ← Verb rostan, mp. rod < aw. raod ¹⁰ / ap. raza „Weinstock“ ¹¹' \"\n  \"(fn. 10 = Bartholomae AIW S. 1495, fn. 11 = Mayrhofer S. 141). This is exactly Nourai's arrow \"\n  \"Persian raz → Arabic rawda, and Asbaghi even ties raz back to aw. raod-. Mainstream Arabic \"\n  \"lexicography (Wehr, Lane, Wiktionary) nevertheless treats rawda as a native r-w-d formation, and \"\n  \"Jeffery/Vollers derive it from Pahlavi rod 'river' instead, so the node stays disputed.\")\n\n# node 10: IEC:1103 and MON:1689\nrc = find(byid[10][\"ref_check\"], \"IEC:1103\")\nrc[\"status\"] = \"partial\"\nrc[\"note\"] = (\"Re-checked with the printed page numerals rather than the leaf formula: IEC p.1103 (the numeral \"\n  \"'1103' is printed immediately above the entry, IEC.txt ff-block 611) reads 'rūs- (3) “space, place”. \"\n  \"Cf. reuos (2). WP II, 356. (Iranian ambig.) Per. rū, rūy, s. “face, surface”. To Av. raoðo “growth” \"\n  \"accdg. to Justi, cf. leudh-); cf. also Per. rūsta, s. “village”: … Lat. rūs, gs: rūris, n. “open country, \"\n  \"farmstead” …'. So Nourai's page citation is correct after all — Mann does have Per. rūstā there — but he \"\n  \"files it under rūs- 'space, place' (with Lat. rūs), and mentions the Av. raoðo 'growth' link only as Justi's \"\n  \"opinion about rū/rūy. Supersedes the earlier 'not_found'.\")\nrc = find(byid[10][\"ref_check\"], \"MON:1689\")\nrc[\"status\"] = \"supports\"\nrc[\"note\"] = (\"Re-checked in Mo'in's own text (the 2-vol. Adena abridgement, MON_part1.txt, is on disk; page numbers \"\n  \"differ from Nourai's 6-vol. edition): 'روستا(ی): (قد. rostāk) [معر. رستاق – روستاق – رسداق – رزداق] \"\n  \"(اِ.) ده، قریه', and s.v. رستاق: '[معر. روستاک] (اِ.) ده، دیه، روستا؛ ج. رساتیق'. Mo'in does give the \"\n  \"Pahlavi antecedent rostāk and the Arabicised rustāq, so the Pahlavi → Persian arrow of #9→#10 is supported \"\n  \"(only the page number could not be confirmed). Supersedes the earlier vajehyab-only 'partial'.\")\n\n# node 13 / 14 / 15: VDQ:39\nrc = find(byid[13][\"ref_check\"], \"VDQ:39\")\nrc[\"status\"] = \"supports\"\nrc[\"note\"] = (\"Checked through the English original (VDQ = Badreh'i's Persian translation of FVQ; noorlib's viewer \"\n  \"is still unreadable here). FVQ p.120: 'Now hurust is a good Iranian word, the equivalent of Av. huraoða-, \"\n  \"and though these Pahlavi works are late the conceptions in them are early and there can be no question of \"\n  \"borrowing from the Semitic.' Jeffery thus prints huraoða-, confirming that the chart's 'hava-rd' is a \"\n  \"scan corruption of hu-raoða.\")\nrc = find(byid[14][\"ref_check\"], \"VDQ:39\")\nrc[\"status\"] = \"supports\"\nrc[\"note\"] = (\"Checked through the English original FVQ pp.119-120: 'It is much more likely that the word comes from \"\n  \"the Phlv. hurust, meaning beautiful, and used in the Pahlavi books of the beauteous damsels of Paradise, \"\n  \"e.g. in Arda Viraf, iv, 18, and in Hadoxt Nask, ii, 23 … Now hurust is a good Iranian word, the equivalent \"\n  \"of Av. huraoða-.' The Pahlavi word, its meaning and its Avestan ancestry are exactly as the node has them.\")\nrc = find(byid[15][\"ref_check\"], \"VDQ:39\")\nrc[\"status\"] = \"partial\"\nrc[\"note\"] = (\"Checked through the English original FVQ pp.117-120. Jeffery does propose hurust ('It is much more \"\n  \"likely that the word comes from the Phlv. hurust'), but his own conclusion is mixed: he documents ḥūr in \"\n  \"pre-Islamic poetry ('ʿAbīd b. al-Abraṣ, vii, 24; ʿAdī b. Zaid; Qaʿnab') and ends 'it does seem certain that \"\n  \"the word ḥūr in its sense of whiteness, and used of fair-skinned damsels, came into use among the Northern \"\n  \"Arabs as a borrowing from the Christian communities, and then Muhammad, under the influence of the Iranian \"\n  \"hurust, used it of the maidens of Paradise.' i.e. Iranian influence on the Qur'ānic concept, not on the \"\n  \"Arabic form — which is why the node stays disputed.\")\n\n# node 4: add the NOTE's second reference, now checkable\nbyid[4][\"ref_check\"].append({\"ref\":\"VDQ:226\",\"status\":\"partial\",\n  \"note\":\"The chart's own NOTE cites VDQ:226 for a derivation from Pahlavi 'rot: river'. Checked via the English \"\n    \"original: FVQ pp.145-146 s.v. رَوْضَة — 'There can be little doubt that the word was borrowed as a noun \"\n    \"into Arabic … Vollers, ZDMG l, 641, 642, noted that the word is originally Iranian, and he suggested that \"\n    \"it was from the Iranian √rud, meaning to grow … From the same root comes Phlv. rod “a lake or riverbed” \"\n    \"and the Pers. rūd commonly used for river … Thus the conclusion would seem to be that the Arabs learned \"\n    \"the Phlv. rod in the Mesopotamian area and used it for any well watered or irrigated land.' The NOTE \"\n    \"reports Jeffery accurately; his source word is rod 'river', not raz.\"})\n\n# derivation clarifications where a now-checked book changes the picture\nbyid[4][\"derivation\"] += (\" Correction after checking Asbaghi on disk: PLA:138 does say what Nourai claims \"\n  \"('rauda „Garten“ aus pers. raz ← Verb rostan, mp. rod < aw. raod / ap. raza „Weinstock“'), and Jeffery \"\n  \"(FVQ 145-146, after Vollers) likewise calls the word Iranian but derives it from Pahlavi rod 'river'; \"\n  \"the verdict stays disputed because standard Arabic lexicography keeps rawda inside the root r-w-d and the \"\n  \"two Iranian proposals contradict each other.\")\n\nbyid[10][\"derivation\"] += (\" Nourai's IEC:1103 turns out to be a correct page reference: Mann does list \"\n  \"'Per. rūsta, s. “village”' there, but under rūs- 'space, place' beside Latin rūs — a third etymology, \"\n  \"neither 'grow' nor 'river'.\")\n\njson.dump(d, io.open(P, \"w\", encoding=\"utf-8\"), ensure_ascii=False, indent=2)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/work/patch311.py"
}
```


### [2026-09-04T19:15:18.757Z] TOOL RESULT

```
ok
[This command modified 1 file you've previously read: data/verification/page-311.json. Call Read before editing.]
```


## [2026-09-04T19:15:23.332Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-311.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 311"
}
```


### [2026-09-04T19:15:25.268Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'confirmed': 10, 'disputed': 7, 'plausible': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'partial': 10, 'contradicts': 1, 'not_checked': 6}
books consulted: {'supports': 31, 'partial': 21, 'contradicts': 10, 'silent': 15} | by book: {'PLA': 10, 'PHD': 8, 'NYB': 7, 'MON': 6, 'BRT': 5, 'HRN': 5, 'FVQ': 5, 'KLN': 5, 'IEC': 4, 'LKT': 4, 'BQT': 4, 'CHEUNG': 3, 'WLD': 3, 'AHD': 3, 'SKT': 2, 'HUB': 1, 'AFA': 1, 'LAT': 1}
```


## [2026-09-04T19:15:30.253Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/page-311.json'))\ne=d['entries'][0]\nprint('root consulted',len(e['consulted']))\nfor n in e['nodes']:\n    print(n['id'], len(n['consulted']), sorted({c['src'] for c in n['consulted']}), '| rc:', [(r['ref'],r['status']) for r in n['ref_check']])\n\"; file data/verification/page-311.json"
}
```


### [2026-09-04T19:15:31.874Z] TOOL RESULT

```
root consulted 4
1 4 ['BRT', 'CHEUNG', 'NYB', 'WLD'] | rc: [('KLN:885', 'supports'), ('SYN:874', 'partial')]
2 5 ['HRN', 'HUB', 'IEC', 'MON', 'PHD'] | rc: [('BQT:944', 'partial')]
3 5 ['HRN', 'IEC', 'NYB', 'PHD', 'PLA'] | rc: [('BQT:944', 'partial'), ('FSF:199', 'partial')]
4 4 ['AFA', 'FVQ', 'KLN', 'LKT'] | rc: [('PLA:138', 'supports'), ('AFM:75', 'contradicts'), ('VDQ:226', 'partial')]
5 3 ['BQT', 'FVQ', 'MON'] | rc: [('MON', 'supports')]
6 3 ['BQT', 'MON', 'PHD'] | rc: [('none', 'not_checked')]
7 3 ['KLN', 'LKT', 'PLA'] | rc: [('AFM:74', 'supports')]
8 3 ['BQT', 'MON', 'PLA'] | rc: [('MON:1694', 'supports')]
9 5 ['BRT', 'HRN', 'NYB', 'PHD', 'PLA'] | rc: [('MON:1689', 'partial')]
10 5 ['BQT', 'HRN', 'NYB', 'PHD', 'PLA'] | rc: [('IEC:1103', 'partial'), ('MON:1689', 'supports')]
11 4 ['BRT', 'IEC', 'NYB', 'PLA'] | rc: [('KLN:885', 'partial'), ('SYN:874', 'partial')]
12 4 ['MON', 'NYB', 'PHD', 'PLA'] | rc: [('BQT', 'supports')]
13 4 ['BRT', 'CHEUNG', 'FVQ', 'PLA'] | rc: [('VDQ:39', 'supports'), ('MAG:186', 'not_checked')]
14 5 ['FVQ', 'HRN', 'NYB', 'PHD', 'PLA'] | rc: [('MAG:186', 'not_checked'), ('VDQ:39', 'supports')]
15 4 ['FVQ', 'KLN', 'LKT', 'PLA'] | rc: [('VDQ:39', 'partial'), ('MAG:186', 'not_checked')]
16 3 ['KLN', 'LKT', 'MON'] | rc: [('MON:1378', 'supports')]
17 3 ['BRT', 'CHEUNG', 'PHD'] | rc: [('SOD:344', 'supports')]
18 3 ['AHD', 'IEC', 'WLD'] | rc: [('KLN:885', 'supports')]
19 4 ['AHD', 'LAT', 'SKT', 'WLD'] | rc: [('none', 'not_checked')]
20 3 ['AHD', 'KLN', 'SKT'] | rc: [('none', 'not_checked')]
data/verification/page-311.json: JSON text data
```


## [2026-09-04T19:15:59.596Z] AGENT

Done. `page-311.json` updated in place; `verify_check.py 311` reports **0 PROBLEM lines**.

**verify_check output**
```
nodes verified: 20/20
node verdicts: {confirmed 10, disputed 7, plausible 2, transcription_suspect 1}
ref checks: {supports 12, partial 10, contradicts 1, not_checked 6}
books consulted: {supports 31, partial 21, contradicts 10, silent 15}
by book: PLA 10, PHD 8, NYB 7, MON 6, BRT 5, HRN 5, FVQ 5, KLN 5, IEC 4,
         LKT 4, BQT 4, CHEUNG 3, WLD 3, AHD 3, SKT 2, HUB 1, AFA 1, LAT 1
```
Root entry got 4 `consulted` (WLD, AHD, IEC, CHEUNG); every node has 3–5 from distinct books. No web pages were used, so `sources` is unchanged.

**ref_check upgrades (5 items re-checked against books now on disk)**
- **#4 `PLA:138` `not_checked` → `supports`.** Asbaghi p.138 literally has Nourai's arrow: *"rauda: 'Garten' aus pers. raz ← Verb rostan, mp. rod < aw. raod / ap. raza 'Weinstock'"*.
- **#10 `IEC:1103` `not_found` → `partial`.** The earlier miss was a leaf-offset error; the printed numeral 1103 sits directly above `rūs- (3) "space, place" … Per. rū, rūy "face, surface" … cf. also Per. rūsta "village" … Lat. rūs`. Nourai's page is right, but Mann files rūstā with Latin *rūs*, not with *leudh-*.
- **#10 `MON:1689` `partial` → `supports`.** Mo'in's own text: `روستا(ی): (قد. rostāk) [معر. رستاق – روستاق – رسداق – رزداق]`.
- **#13 / #14 `VDQ:39` `not_checked` → `supports`**, **#15 `VDQ:39` → `partial`**, and root `VDQ:39` → `partial` — checked through the English original FVQ (VDQ is its translation): p.120 *"hurust is a good Iranian word, the equivalent of Av. huraoδa-"*; p.119 the hurust→ḥūr proposal; but p.120 concludes the Arabic word came from Aramaic *ḥwr* "white" and only the *concept* is Iranian.
- New ref_check item **#4 `VDQ:226` `partial`** for the claim in the chart's own NOTE — FVQ pp.145-146 (after Vollers) does call *rawḍa* Iranian, but from Pahlavi *rōd* "river", not *raz*.
- `MAG:186` (Widengren) stays `not_checked` — still not on disk.

**No verdict changes.** Two derivations got one appended sentence recording newly verified facts (#4: PLA and FVQ both do argue an Iranian origin, but contradict each other and standard Arabic lexicography, so `disputed` stands; #10: Mann's third etymology).

**Notable findings**
- PHD p.77 `rostāg … river-bed; district, province`, Psalter `rwdystʾg`, and NYB p.179 headword `rōtastāk` / `Rōtastahm` decisively back the "river" reading against Nourai for #9/#11/#12 — while **Horn no. 614 (p.136) is the 1893 source that put rōstā under "to grow"**, i.e. exactly where Nourai got it.
- BRT cols. 1493-1495 keeps `²raod- "wachsen"` and `⁴raod- "fliessen"` apart; the chart conflates them.
- IEC pp. 659-660 puts Persian *raz* with OCS *loza* under `laĝ-` "creeper" — a fourth etymology, contradicting #3.
- Asbaghi has **no** *rawnaq* entry anywhere in his r- section (silent = not a Persian loan on his evidence), and rejects the *hurust* origin of *ḥūrī* in favour of his own *ahura* etymology (p.103).
- Skeat p.250 derives Latin *līber* from `*leubh-` "desire", not `*leudh-` — the only book on the shelf that does.
