# Verification process log — verify-page-37


## [2026-09-04T18:46:06.054Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 37 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-37.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-37.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-37.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 37` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T18:46:07.286Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-04T18:46:09.131Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:46:09.144Z] TOOL RESULT

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


## [2026-09-04T18:46:09.950Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-37.txt"
}
```


### [2026-09-04T18:46:09.962Z] TOOL RESULT

```
1	=== PDF page 37 (book page 7) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Agh, Aghlo : to be depressed, to be afraid; disagreeable, adverse  (refs POK:7,8)
4	#1 (parent #0) [Avestan] refs=POK:8 | ağô, ağâ : bad, ugly
5	  #2 (parent #1) [Pahlavi] refs=SNS:38 | âğ, âk : trouble, ugliness
6	    #3 (parent #2) [Persian] refs=SNS:38; BQT:52 | âk, ak «آک ، اک» : trouble, deficiency
7	    #4 (parent #2) [Persian] refs=SNS:38; BQT:90 | âx, ax «آخ ، اخ» : a word of rejection, disgust and grief
8	#5 (parent #0) [Old English] refs=AHD | eglan : to trouble
9	  #6 (parent #5) [English] refs=AHD | ail, ailment
10	#7 (parent #0) [Old Norse] refs=AHD | agi : frightened
11	  #8 (parent #7) [English] refs=AHD | awe, awesome
12	--- entry 1 ---
13	ROOT Aghlo -> redirect to Agh
14	--- entry 2 ---
15	ROOT Agros -> redirect to Ag
16	--- entry 3 ---
17	ROOT A-gur-ru -> redirect to Agurru
18	--- entry 4 ---
19	ROOT [Akkadian] Agurru, A-gur-ru : baked clay, brick  (refs AKD:31; KNT:165)
20	#1 (parent #0) [Old Persian] refs=KNT:165; PLA:6 | aguru : brick
21	  #2 (parent #1) [Pahlavi] refs=PLA:6 | âgur
22	    #3 (parent #2) [Persian] refs=PLA:6; AFA:5; MON:78 | âgur «آگور» : brick | extra: آگورگر ، آگورگری
23	      #4 (parent #3) [Arabic] refs=AFA:5; PLA:6; AKD:31; AFM:7 | âjur : brick | NOTE: This word could have entered Arabic directly from Akkadian / Aramaic (AFA:5)
24	        #5 (parent #4) [Persian] refs=MON:78 | âjor «آجر» : brick
25	
```


## [2026-09-04T18:46:11.560Z] AGENT

I'll read the supporting context files.


## [2026-09-04T18:46:13.751Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T18:46:13.790Z] TOOL RESULT

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


## [2026-09-04T18:46:16.563Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','AHD','SNS','BQT','AKD','KNT','PLA','AFA','MON','AFM','WLD','IEC','SYN','KLN','HRN','HUB','PHD','NYB','BRT','SKT','FSD','WEB','LKT','FVQ','DOZ','ARY','CHEUNG']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False))\n    else: print(k, 'MISSING')\n\""
}
```


### [2026-09-04T18:46:18.333Z] TOOL RESULT

```
<persisted-output>
Output too large (41.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b08yzjm2n.txt

Preview (first 2KB):
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_0
...
</persisted-output>
```


## [2026-09-04T18:46:23.672Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['AHD','SNS','BQT','AKD','KNT','PLA','AFA','MON','AFM']:\n    v=d.get(k,{})\n    print('==',k)\n    for f in ['title','kind','local_file','local_files','page_offset','lookup_hint','url']:\n        if f in v: print('  ',f,':',str(v[f])[:600])\n\""
}
```


## [2026-09-04T18:46:23.855Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-37.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:8000])\n\""
}
```


### [2026-09-04T18:46:25.580Z] TOOL RESULT

```
== AHD
   title : W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)
   kind : archive_djvu+website+archive_restricted
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 
   url : https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only
== SNS
   title : Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt']
   page_offset : 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
   lookup_hint : grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
   url : https://archive.org/details/VajnameShayest
== BQT
   title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
   kind : archive_djvu+local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh
   url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1
== AKD
   title : H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt
   page_offset : leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Organised by semantic field; Akkadian words in transliteration with Aramaic/Arabic/Persian loans. grep the word.
   url : https://archive.org/details/akkadischefremdw00zimmuoft
== KNT
   title : R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
   page_offset : leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
   url : https://archive.org/details/oldpers
== PLA
   title : A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt']
   page_offset : 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
   lookup_hint : HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
   url : https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)
== AFA
   title : S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt
   page_offset : leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.
   url : https://archive.org/details/diearamischenfr00fraegoog
== MON
   title : Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)
   kind : website+archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
   page_offset : None
   lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a
   url : https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)
== AFM
   title : Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt']
   page_offset : 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
   lookup_hint : Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
   url : https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)
```


### [2026-09-04T18:46:27.573Z] TOOL RESULT

```
{
 "pdf_page": 37,
 "book_page": 7,
 "entries": [
  {
   "root": {
    "name": "Agh, Aghlo",
    "lang": "Indo-European",
    "refs": "POK:7,8",
    "gloss": "to be depressed, to be afraid; disagreeable, adverse"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:8",
     "words": [
      {
       "translit": "ağô, ağâ",
       "gloss": "bad, ugly",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Pahlavi",
     "refs": "SNS:38",
     "words": [
      {
       "translit": "âğ, âk",
       "gloss": "trouble, ugliness",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 2,
     "lang": "Persian",
     "refs": "SNS:38; BQT:52",
     "words": [
      {
       "translit": "âk, ak",
       "gloss": "trouble, deficiency",
       "script": "آک ، اک"
      }
     ],
     "note": null,
     "quote": {
      "text": "آکی نرسید بر تو از من - صدبار مرا زتو رسید آک",
      "poet": "Sûzanî"
     }
    },
    {
     "id": 4,
     "parent": 2,
     "lang": "Persian",
     "refs": "SNS:38; BQT:90",
     "words": [
      {
       "translit": "âx, ax",
       "gloss": "a word of rejection, disgust and grief",
       "script": "آخ ، اخ"
      }
     ],
     "note": null,
     "quote": {
      "text": "زهری که او چشاند چه جای اخ، که بخ بخ - تیغی که او گذارد چه جای اه ، که به به",
      "poet": "Loghatnâmeh"
     }
    },
    {
     "id": 5,
     "parent": 0,
     "lang": "Old English",
     "refs": "AHD",
     "words": [
      {
       "translit": "eglan",
       "gloss": "to trouble",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 5,
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "ail, ailment",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 0,
     "lang": "Old Norse",
     "refs": "AHD",
     "words": [
      {
       "translit": "agi",
       "gloss": "frightened",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 8,
     "parent": 7,
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "awe, awesome",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    }
   ]
  },
  {
   "root": {
    "name": "Aghlo",
    "redirect": "Agh"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Agros",
    "redirect": "Ag"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "A-gur-ru",
    "redirect": "Agurru"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Agurru, A-gur-ru",
    "lang": "Akkadian",
    "refs": "AKD:31; KNT:165",
    "gloss": "baked clay, brick"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Old Persian",
     "refs": "KNT:165; PLA:6",
     "words": [
      {
       "translit": "aguru",
       "gloss": "brick",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Pahlavi",
     "refs": "PLA:6",
     "words": [
      {
       "translit": "âgur",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 2,
     "lang": "Persian",
     "refs": "PLA:6; AFA:5; MON:78",
     "words": [
      {
       "translit": "âgur",
       "gloss": "brick",
       "script": "آگور"
      }
     ],
     "script_extra": "آگورگر ، آگورگری",
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Arabic",
     "refs": "AFA:5; PLA:6; AKD:31; AFM:7",
     "words": [
      {
       "translit": "âjur",
       "gloss": "brick",
       "script": null
      }
     ],
     "note": "This word could have entered Arabic directly from Akkadian / Aramaic (AFA:5)",
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "Persian",
     "refs": "MON:78",
     "words": [
      {
       "translit": "âjor",
       "gloss": "brick",
       "script": "آجر"
      }
     ],
     "note": null,
     "quote": null
    }
   ]
  }
 ]
}
```


## [2026-09-04T18:46:31.398Z] AGENT

Now let me check the local reference texts.


## [2026-09-04T18:46:33.532Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: agh\" POK_full.txt | head -20; echo \"---POK_01 leaf 15/16 (p.7,8)---\"; awk 'BEGIN{RS=\"\\f\"} NR==16 || NR==17' POK_01.txt | head -80"
}
```


## [2026-09-04T18:46:34.524Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD agh ===\"; grep -n -i \"^agh\\|^ag-\\|agh-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-04T18:46:35.491Z] TOOL RESULT

```
1787:Root / lemma: agh-(lo-) 
1793:Root/ lemma: agh-(lo-)\ "disgusting' derived from an extended Root/ lemma: agos-\ " 
1815:Root / lemma: aghl(u)-{*heghel-) 
1831:Root / lemma: agh- {*hegh-) 
1935:Root / lemma: agh- 
8801:Root / lemma: agher-, aghen-, aghes- (or oghereic) {*daghen) 
8825:From Root/ lemma: d'^eg'^h-: "to burn, *day' derived Root/ lemma: agher-, aghen-, aghes- 
8892:Root/ lemma: aier-, aien-\ "day, morning' derived from a reduced Root/ lemma: agher-, 
19998:from Root/ lemma: 6!^eg''h-\ "to burn, *day' derived Root/ lemma: agher-, aghen-, aghes- 
25266:brown (in names of trees and animals), derived from Root/ lemma: aghl(u)- {* heghel-): 
---POK_01 leaf 15/16 (p.7,8)---
  ahd.  egl;  mhd.  ege  f.  , Furcht,  Schrecken, Strafe';  got.  -agan  in  un-agands  ,sich  nicht  fürchtend',  af-agjan  ,ängstigen', us-agjan  ,jemanden  erschrecken',  in-agjan  .jemanden  anfahren';  Präterito- präsens  got.  ög  (ögum)  ,fürchte  mich';  ni  ögs  ,fürchte  nichts'   (alter   kurz-
vokalischer  Konjunktiv  *ögiz),  anord.  öa-sk  ,sich  fürchten^;  g'ot.  ögjan jemanden  schrecken'  =  anord.  cegja  .erschrecken';  anord.  ögn  f.  .Schrecken', ötti  m.  .Furcht',  ags.  öga  f.  .Schrecken'.
Air.  ad-ägor,  -ägicr  .fürchte'  (wegen  der  Ablautgleichheit  mit  got.  ög vermutet  Brugmann  Grdr.  IP  3.  484  Ursprung  aus  einem  altern  Perf.). Verbalnomen  äigthiu.
WP.  I  40.  Feist  14.  380.
Hierzu  gehört  wohl  auch:
agh-(lo-)  .widerwärtig'.
Got.  agls  yalaxQOS  .schimpflich',  agli^a,  aglö  .Drangsal',  us-agljan .bedrängen',  ags.  eg{e)le  .widerwärtig,  beschwerlich,  bedauerlich',  eglan .Schmerz  zufügen'  (engl,  all  .schmerzen;  unpäßlich  sein'),  eglian  .schmerz- lich empfunden  werden',  mnd.  egelen  .Gram  verursachen',  got.  aglus  Adv. agluha  ,6vG'/.oIoq,  dvG'Aolwg,  schwierig';  auch  (mit  rätselhaftem  Suffix)  got. aglaitei  f..  -i  n.  jäaelyeia,  Unzucbt'.  ahd.  agaleizi  f..  -i  n.  .Unbequemlich- keit; Eifer',  agaleizo,  as.  agleto,  agaleto  Adv.  .emsig,  eifrig'.
Möglicherweise  hierher  ai.  aghä-  (=  av.  cxyö-)  .böse',  n.  .Übel.  Schaden'. aghald-  .schlimm'.
Hierher  vielleicht  mir.  älad  n.  .Wunde'  i^agloton),  mcymr.  aele{u)  .schmerz- haft', aeleu  m.  .Schmerz'  (^^aglou-).
WP.  I  41.  Feist  loa.  Specht  Dekl.  136.  Loth  RC.  38.  56.
aghl(u)-  etwa  .dunkle  Wolke,  regnerisches  Wetter'.
Gr.   äx^ig  .Nebel.  Dunkel',  apr.   aglo  n.    .Regen'   (?/-St.).   arm.   *alj-  in aijaij,  aijamuijhh  .Dunkel'  (Meillet  MSL.  10.  279). WP.  I  41.  Vgl.  Petersen  Ar.  und  Arm.  Stud.   126.
agos-  .Fehl.  Schuld.  Sünde'.
Ai.  ägas-  n..  ablautend  mit  gr.  Uyoq  .schwere  Schuld.  Blutschuld';  ai. dnägas-,  ^v.  dvayrjg  .schuldlos';  (Jy?Jc.  irayrjg  .verflucht',  äyiog'  i-naqog.
Diese  entschieden  ins  sittliche  Gebiet  gewendete  Bed.  .Schuld.  Frevel' ist  vielleicht  aus  sinnlicherem  .Schaden.  Wehtun'  entwickelt:  ags.  acan, öc  .schmerzen'  (engl,  ache)^  ndd.  äÄ;en  .schmerzen,  eitern
,  beulen',  mndl.  akel .Leid.  Unrecht.  Schade',  nfries.  akelig,  aeklig  .horridus.  miser.  vehemens'.
WP.  I  38.
agro-  (egro-?)  .Spitze,  oberstes,  erstes.  Anfang'.
Ai.  dgra  n.  .Spitze',  agre  (Lok.)  .an  der  Spitze',  auch  zeitlich  .im  Anfang zuerst',  agrimd-  .der  erste',  av.  ayra-  .der  erste,  oberste  nach  Zeit   Raum
usw/;  1).  ; Anfang-;  das  oberste^  Spitze^;  lett.  agrs  (Adj.)  ^frühe^;  agri  Adv. früh;  frühzeitig-;  agrums  ^die  Frühe^
Ob  hierher  der  lat.  MN  Ägrlppa  aus  '^•agri-jp{e)d-  ^der  mit  den  Füßen zuerst  zur  Welt  kommt%  W.  Schulze  KZ.  32,  Vi2\  zweifelnd  Lat.  Eig.  230^?
Falls  ai.  dgra-  auf  *ogro-  oder  *egro-  zurückginge;  könnte  man  hitt. he-kur,  he-gur  ;Felsgipfel'  vergleichen.
WP.  I  38  f.;  Federsen  Hitt.  183.
agro-s  s.  ag-.
agu.(e)si,  aksi  ;Axt^
Got.  aqizij  anord.  ex,  ags.  acus,  cex,  as.  acits,  accus,  alid.  achhus,  accus, aclies,  nhd.  Axt  (die  gerra.  Formen  *aqwizi  und  *aJcusi  sind  vielleicht nach  Zupitza  GG.  89  aus  einem  abstufenden  *agiiesi:  ^agusiäs  geflossen); gr.  ä^tvr]  ;Axt;  BeiU;  lat.  ascia  ;Axt  der  Zimmerleute'^  (aus  "^acsiä  wie visciis:  i^ög,  vespa  aus  *vepsa).
WP.  I  39,  WH.  I  71;  Feist  54  b;  Specht  Dekl.  150;  Schwyzer  Gr.  Gr. I  465^.
ag^h-no-s  (z.  T.  auch  *agV:nosf)  ;Lamm'.
Gr.  duvög  m.  f.;  dfivrj  f.  ;Lamm^;  lat.  agnus,  -t,  fem.  -a  ;Lamm''  (agnlle ^Schafstall'^;  ohne  Suffixverwandtschaft  mit  aksl.  jagnilo  ;locuS;  ubi  oves parturiunt^;  einer  Ableitung  vom  Verbum  jagniti  ,lammen^);  air.  üan  cjmr. oen,  acorn.  oin,  bret.  oan  ;Lamm^  (urk.  *ognos  mit  -gn-  aus  ^-g'ihn-,  nicht -*-g'^n-,  das  trotz  Pedersen  KG.  I  109  -bn-  ergeben  hätte;  o-  wohl  Einfluß von  "^ Ollis  ;Schaf^);  ags.  eanian,  engl,  to  yean  flammen'';  ndl.  oonen  ds.  (aus *aunön  von  ^auna-  =  idg.  "^agl'hno-)]  aksl.  (j)cign^  ;Lamm^  (um  das  bei Bezeichnungen  junger  Tiere  beliebte  Formans  -et-  erweitert);  (j)agnbci) ;Lämmchen^  enthalten  Dehnstufe.  Oder  ist  idg,  *ög'i(h)no- :  *dg'-i(h)no-  an- zusetzen?
Die  durchs  Germ,  und  Kelt.  vorausgesetzte  Media  aspirata  kann  auch den  lat.  und  slav.  Formen  zugrunde  liegen;  so  daß  gr.  äf-ivög  (zunächst  aus *dßvög)  der  einzige  verläßliche  Hinweis  auf  Media  g^:  bleibt.  Wenn  umbr. habina(f
```


### [2026-09-04T18:46:35.536Z] TOOL RESULT

```
=== AHD agh ===
134:The most widespread of the words for “night” was nek’-t-. Words for “day” include amer- and agh-? and such dialectal creations as Latin diés; ayer- refers to the morning. The old word for “darkness,” reg”es-, shows up in Greek as a term for the underworld.
198:kagh-. To catch, seize; wickerwork, fence. pele-2. Flat; to spread. mu-', Imitative of inarticulate sounds.
261:ag-. To drive. 1. Latin agere, to do, act, drive, conduct, lead: ACT, AGENDUM, AGENT, AGILE, AGITATE; (ALLEGE), AMBAGE, AMBIGUOUS, (ASSAY), (CACHE), COAGULUM, COGENT, ESSAY, EXACT, (EXAMINE), (EXIGENT), FUMI- GATE, INTRANSIGENT, LEVIGATE, LITIGATE, NAVIGATE, OBJURGATE, PRODIGAL, RETROACTIVE, SQUAT, TRANS- act. 2. Greek agein, to drive, lead: -AGOGUE, AGONY; ANAGOGE, (ANTAGONIZE), CHORAGUS, DEMAGOGUE, EPACT, GLUCAGON, HYPNAGOGIC, MYSTAGOGUE, PEDA- GOGUE, PROTAGONIST, STRATAGEM, SYNAGOGUE. 3. Suf- fixed form *ag-to- in Celtic *amb(i)-ag-to-, “one sent around” (*ambi, around; see ambhi), in Latin ambactus, servant (> Medieval Latin ambactia, office): AMBASSA- DOR, EMBASSAGE, (EMBASSY). 4. Suffixed form *ag-men- in Latin agmen, a train, a moving forward, a marching column, group: AGMINATE. 5. Suffixed form *ag-ti-, “weighing” (Greek agein, “to lead,” has a sense “to weigh”), whence adjective *ag-ty-o-, “weighty,” in Greek axios, worth, worthy, of like value, weighing as much: AXIOM; AXIOLOGY, CHRONAXY. 6. Possibly suffixed form *ag-ro-, driving, pursuing, grabbing, in Greek agra, a seizing: PELLAGRA, PODAGRA. Derivative agro-. [Pok. ag- 4]
262:ag-es-. Fault, guilt. Possibly Old English acan, to ache (perhaps < “to cause mental pain”): ACHE. [Pok. agos- 8.]
263:agh-1. To be depressed, be afraid. 1. Suffixed form *agh-lo- in Old English egian, eglian, to trouble, afflict: AIL. 2. Suffixed form *agh-es- in Old Norse agi, fright- ened: AWE. [Pok. agh- 7.]
264:agh-?. A day (considered as a span of time). Germanic *dagaz (with initial d- of obscure origin), day, in: a. Old English deg, day: DAY; (DAISY), TODAY; b. Old English denominative dagian, to dawn: DAWN. [Pok. agher- 7.]
341:bhlagh-men-
342:flagitdre, to demand importunately: FLacitious. [Pok. bhlag- 154.] bhlagh-men-. Form, ritual form. Sanskrit brahmd, brah- man-, priest, and brahma, bréhman-, prayer: BRAHMA!, BRAHMAN, (BRAHMIN). [Pok. bhlagh-men- 154.] bhlé-1. To howl. Probably imitative. 1. Germanic suffixed form *blé-t- in Old English b/gtan, to bleat: BLEAT. 2. Germanic suffixed form *b/é-r- in Middle English bleren, to roar: BLARE. 3. Latin flére, to weep: FEEBLE. [Pok. bAlé- 154.] bhié-2, Also bhla-. To blow. 1. Germanic suffixed form *blé-w- in Old English blawan, to blow: BLow!. 2. Ger- manic suffixed form *blé-dram, “something blown up,” in: a. Old English blZdre, blister, bladder: BLADDER; b. Old Norse bladhra (noun), bladder, and bladhra (verb), to prattle: BLATHER. 3. Germanic extended form *blés- in: a. Old English b/ést, a blowing, blast: BLAST; b. Middle Dutch blas(e), a bladder: stncLass. 4. Variant form *bhid- in Latin flare, to blow (> flabellum, fan): FLABELLUM, FLATUS, FLAVOR; AFFLATUS, CONFLATE, (DEFLATE), INFLATE, SOUFFLE. [In Pok. 3. bhel- 120.] bhlei-. To blow, swell. Extension of bhel-2. 1. Germanic *blajjinén-, a swelling, in Old English blegen, a boil, blister: BLAIN. 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhiei- 156.] bhleu-. To swell, well up, overflow. Extension of bhel-?. 1. Possibly Germanic *b/aut- in Old Norse blautr, soft, wet: BLOAT. 2. Extended form bhleug~- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (IN- FLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS. 3. Zero-grade form *bhlu- in Greek phluein, phluzein, to boil over: PHLYCTENA. 4. Possibly Greek phloos, phioios, tree bark (< “swelling with growth”): PHLOEM. [Pok. bhileu- 158.] bhlig-. To strike. Latin fligere, to strike: AFFLICT, CON- FLICT, INFLICT, PROFLIGATE. [Pok. bhlig- 160.] bhoso-. Naked. Germanic *bazaz in: a. Old English bzr, bare: BARE!; b. Old Swedish and Old Danish bar, bare: BALLAST. [Pok. bhoso-s 163.] bhrag-. To smell. 1. Germanic *brak- in Old High Ger- man bracc(h)o, dog that hunts game by scent: BRACH. 2. Suffixed form *bhrag-ro- in Latin fragrdre, to smell: FLAIR, FRAGRANT. [Pok. bhrag- 163.] bhrater-. Brother, male agnate. 1. Germanic *brdthar- in Old English bréthor, brother: BROTHER. 2. Latin frdter, brother: FRA, FRATERNAL, FRIAR; CONFRERE, FRATRI- CIDE. 3. Greek phratér, fellow member of a clan: PHRATRY. 4, Sanskrit bhratd, bhrdatar-, brother: PAL. [Pok. bhrdater- 163.] bhreg-. To break. 1. Germanic *brekan in: a. Old English brecan, to break: BREAK; b. Old English bréc, a break- ing: BREACH; c. Old High German brehhan, to break, akin to the Germanic source of Italian breccia, breccia: BRECCIA; d. Old French breier, to break: BRAY?; e. Old French brier (dialectal) and broyer, to knead: BRIOCHE. 2. Germanic *brak-, bushes (< “that which impedes motion”), in Old Norse *brakni, undergrowth, akin to the probable Scandinavian source of Middle English brake(n), bracken: BRACKEN, BRAKE’, BRAKE‘, 3. Nasal- ized zero-grade form *bhr-n-g- in Latin frangere, to break: (FRACTED), FRACTION, (FRACTIOUS), FRACTURE, FRAGILE, FRAGMENT, FRAIL!, FRANGIBLE; ANFRACTU- OUS, CHAMFER, DIFFRACTION, (INFRACT), INFRANGIBLE, INFRINGE, OSSIFRAGE, REFRACT, (REFRAIN?), (REFRIN- GENT), SAXIFRAGE, SEPTIFRAGAL. 4, Latin suffrdgdri, to vote for (? < “to use a broken piece of tile as a ballot”), hence suffrdgium, the right to vote: SUFFRAGAN, SUF- FRAGE. [Pok. 1. bhreg- 165.] bhréi-. Also bhri-. To cut, break. 1. Possibly Latin fricdre (> French frotier), to rub: FRAY?, FRICATIVE, FRICTION, FROTTAGE; AFFRICATE, DENTIFRICE. 2. Possi-
386:dhragh-. To draw, drag on the ground. Rhyming variant tragh-. 1. Germanic *dragan in: a. Old English dragan, to draw, pull: pRaw; b. Old Norse draga, to draw, pull (or Old English dragan): DRAG; c. Old English drexge, dragnet: DRAY; d. Old Norse *drahtr, drdttr, act of drawing, akin to the source of Middle English draught, a pull: DRAFT. 2. Russian drogi, a wagon: DROSHKY. See also variant form dhreg-. [Pok. dheragh- 257.]
387:dhreg-. To draw, glide. Variant form of dhragh-. 1. Na- salized Germanic form *drinkan, to draw into the mouth, drink, in Old English drincan, to drink: DRINK. 2. Nasal- ized Germanic form *drankjan, “to cause to drink,” in: a. Old English drencan, to soak: DRENCH; b. Scandina- vian *drunkna, drugna, to drown, akin to the Scandina- vian source of Middle English drounen, to drown: DROWN. [Pok. dhreg- 273.]
566:kae-id-. To strike. 1. Latin caedere, to cut, strike: CAE- SURA, CEMENT, CESTUS2, CHISEL, -CIDE, SCISSORS; AB- SCISE, CIRCUMCISE, CONCISE, DECIDE, EXCISE2, INCISE, PRECISE, RECISION. 2. Latin caelum (? < *caedum), sculptor’s chisel: CAELUM. [Pok. (s)k(h)ai- 917.] kagh-. To catch, seize; wickerwork, fence. 1. Germanic *hag- in: a. Old French hagard, wild, wild hawk (< “raptor”): HAGGARD; b. Germanic *hagén- in Old Eng- lish haga, hedge, hawthorn: HAW?; c. Germanic *hagj6é in Old English hecg, hedge: HEDGE. 2. Suffixed unaspirated form *kag-yon- in Gaulish caio, rampart, retaining wall (> Old French quai, quay): (CAY), KEY?, QUAY. 3. Possi- ble variant *kogh- in: a. Latin cohum, strap from yoke to harness: INCHOATE; b. possibly Latin cdlum, sieve (< wickerwork), and its derivative céldre, to filter: COLAN- DER, COULEE, (COULOIR), CULLIS; PERCOLATE. [Pok. kagh- 518.]
710:magh-'. To be able, have power. 1. Germanic *snag- in: a. Old English magan, to be able: May; b. Old French esmaier, to frighten: DISMAY. 2. Germanic suffixed form *mah-ti-, power, in Old English miht, power: MIGHT!. 3. Germanic suffixed form *mag-inam, power, in Old English mzgen, power: MAIN}. 4. Suffixed length- ened-grade form *magh-and-, “that which enables,” in Greek (Attic) mékhané, (Doric) madkhand, device: MA- CHINE, MECHANIC, (MECHANISM), (MECHANO-). 5. Possi- bly suffixed form *magh-u- in Old Persian magus, member of a priestly caste (< “mighty one”): (MAGI), (MAGIC), MAGUS; ARCHIMAGE. [Pok. magh- 695.]
711:magh-. To fight. Hypothetical Old Iranian *ha-maz-an-,
712:“warrior” (*ha-, with < *sm-; see sem-'), possibly borrowed into Greek as Amazén, Amazon: AMAZON. [Pok. magh- 697.]
1037:(s)wagh-. To resound. 1. Germanic *swdégan in Old English swégan, to resound: souUGH. 2. Suffixed form *wagh-d- in Greek ékhé, sound: CATECHIZE. 3. Suffixed form *wdgh-di- in Greek ékhd, noise, echo: ECHO. [Pok. udgh- 1110.]
1094:tkei-. To settle, dwell, be home. 1. Suffixed o-grade form *()koi-mo- in Germanic *haimaz, home, in: a. Old Eng- lish hdm, home: HOME; b. Old Norse heimr, home: NIFLHEIM; C. Middle Dutch hame, hame (< “covering”): HAME; d. Old French ham, village, home: HAMLET; e. Germanic *haimatjan, to go or bring home, in Old French hanter, to frequent, haunt: HAUNT. 2. Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHYCTYONY. 3. Probable zero-grade form *tki- in Latin si- in suffixed form *si-tu- in situs, location: SITUATE, SITUS. [Pok. 1. hei- 589, Athei- 539.] to-. Demonstrative pronoun. For the nominative singular see so-. 1. Germanic *thé- in: a. Old English thé, thy (instrumental case), by the: THE!, THE?; NATHELESS; b. Middle Dutch de, the: pEcoy. 2. Germanic *thauh, “for all that,” in Old Norse thd, though, akin to the Scandinavian source of Middle English though, though: THOUGH. 3. Germanic *thasi- in Old English thes, this, this: (THESE), THIS. 4. Germanic *thana- in Old English thanne, thenne, thenne, than, then: THAN, THEN. 5. Ger- manic *thanana- in Old English thanon, thence: THENCE. 6. Germanic *thér in Old English ther, thér, there: THERE. 7. Germanic *thathro in Old English theder, thider, thither: THITHER. 8. Germanic nomina- tive plural *thai in Old English tha and Old Norse their, they: THEY. 9. Germanic genitive plural *thaira in Old Norse their(r)a, theirs: THEIR. 10. Germanic dative plural *thaimiz in Old Norse theim and Old English thém, them: THEM. 11. Extended neuter form *tod- in: a. Ger- manic *that in Old English thet, that: THAT, (THOSE); b. Greek to, the: TAUTO-. 12. Germanic *thus- in Old English thus, thus: THUS. 13. Adverbial (originally accu- sative) form *tam in Latin tandem, at last, so much (> Anglo-Norman tant): TANDEM, TANTAMOUNT. 14. Suf- fixed reduced form *t-dli- in Latin tdlis (plural tdlés), such: TALES. [Pok. 1. to- 1086.] tolky-. To speak. Metathesized form *tlokv- in Latin loqui, to speak: LOCUTION, LOQUACIOUS; ALLOCUTION, CIRCUMLOCUTION, COLLOQUIUM, (COLLOQUY), ELOCU- TION, GRANDILOQUENCE, INTERLOCUTION, MAGNIL- OQUENT, OBLOQUY, PROLOCUTOR, SOLILOQUY, VENTRILOQUISM. [Pok. tolk¥- 1088.] tong-. To think, feel. 1. Germanic *thank6n in: a. Old English thancian, to thank: THANK; b. Old English thencan, to think: THINK. 2. Germanic *(ga)thauht- (*ga-, collective prefix; see kom) in Old English (ge)- thoht, thought: THOUGHT. 3. Germanic factitive *thunk- Jan in Old English thyncan (third person singular present indicative thyncth), to seem: METHINKS. [Pok. 1. tong- 1088.] tragh-. To draw, drag, move. Rhyming variant dhragh-. Latin trahere, to pull, draw: TRACT!, TRACTABLE, TRAC- TION, TRAIL, TRAIN, (TRAIT), TREAT; ABSTRACT, AT- TRACT, CONTRACT, DETRACT, DISTRACT, EXTRACT, PORTRAY, PROTRACT, RETRACT, SUBTRACT. [Pok. tragh- 1089.] treb-. Dwelling. 1. Zero-grade form *trb- in Germanic *thurp- in Old English thorp, village, hamlet: THORP. 2. Latin trabs, beam, timber: TRABEATED, TRABECULA, TRAVE; ARCHITRAVE. [Pok. treb- 1090.] trei-. Three. I. Nominative plural form *treyes. 1. Ger- manic *thrijiz in Old English thrie, thréo, thri, three, with its derivatives thriga, thriwa, thrice, and thritig, thirty, and thréotine, thirteen: THREE, THRICE, THIRTY, THIRTEEN. 2. Latin trés (> Italian tre and French trois), three: TREY, TRIO; TRAMMEL, TRECENTO, TREPHINE, TRIUMVIR, TROCAR. II. Zero-grade form *tri-. 1. Suffixed form *tri-tyo- in: a. Germanic *thridjaz, third, in (i) Old English thrid(d)a, thirdda, third: THIRD (ii) Old Norse thrithi, third: RIDING?; b. Latin tertius (neuter tertium), third: TERCEL, TERCET, TERTIAN, TERTIARY, TIERCE; SESTERCE. 2. Latin évi-, three: TRI-, TRIPLE. 3. Greek t7i-, three: TRI-; TRICLINIUM, TRICROTIC, TRIDACTYL, TRI- GLYPH, TRITONE. 4. Sanskrit tri, three: TRIMURTI.
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1222:AIL agh-! AIOLI elaia AIR wer-2 AIRPLANE pelo-2 AISLE aks- AITCHBONE not-
1235:AMATIVE amma AMATORY amma AMAZON magh-2 AMBAGE ag- AMBASSADOR ag- AMBERGRIS gher-3 AMBI- ambhi AMBIDEXTROUS deks- AMBIENT ei-1 AMBIGUOUS ag- AMBITION ei-1
```


## [2026-09-04T18:47:03.607Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK p.7 (leaf14/15) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==15' POK_01.txt | tail -30; echo; echo \"=== POK_full 1787-1850 ===\"; sed -n '1780,1850p' POK_full.txt"
}
```


## [2026-09-04T18:47:04.427Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT agur ===\"; grep -n -i \"agur\\|a-gu-ru\\|brick\" KNT.txt | head -30"
}
```


### [2026-09-04T18:47:05.221Z] TOOL RESULT

```
=== POK p.7 (leaf14/15) ===
ndlich,  bäurisch,  derb'.  (Über  got.  akran,  dt.  Eckern  s.  aber  unter  *ög- . wachsen'.)
WP.  I  35  f..  WH.  I  22  f..  89.  H.  Reichelt  WuS.   12.  112.
ag-  .Ziegenbock.  Ziege'.
Ai.  ajd-h  .Ziegenbock,  ajd  ;Ziege'.  mpers.  azak  .Ziege',  npers.  azg  ds.;
alb.  dht  ,Ziege'  (G.  Meyer  BB.  8,  186,  Pederseii  KZ.  36,  320,  335;  wohl aus  *adliiy  wie  sii  ,Auge^  aus  asii)]
lit.  üzys  {*agios)  , Ziegenbock^,  ozkä  , Ziege',  apr.  wosee  ,Zieg-e^,  loosux , Ziegenbock';
ai.  ajina-m  ,Felk;
lit.  ozinis  ,zum  Ziegenbock  gehörig',  oziena  , Ziegenbockfleisch';
ksl.  (j)azno  (*azhno)  ,Haut,  Leder'.
WP.  I  38,  TrautQiann  22.    Vgl.  auch  aig-.
agh'  ,trächtiges  Tier'.
Ai.  ahi  ,Kuh',  av.  azl  L  Adj.  ,trächtig'  (von  Kühen  und  Stuten)_,  mir. ag  (s-St.)  n.,  f.  ,Rind,  Kuh',  ag  allaid  ,Hirsch'  (eigentlich  ,wilder  Ochse'j, dl  ,Brut,  Wurf  (^aglo-),  cjmr.  ael  ds.,  mcymr.  aelaw  ,Reichtum',  eilion (^agliones)  ,Damwild,  Pferde';  hierher  mit  e-Vokalismus  arm.  ezn  ,Rind'?
WP.  I  38,  Loth  RC.  38,  55.
agher-,  nghen-,  Eghes-  (oder  ogher  usw.)  ^Tag'.  Heteroklit.  Neutrum.
Ai.  dha7^,  dhahy  Gen.  dhn-as,  av.  Gen.  PI.  asn-qm  ^Tag'.  Im  Gei-m.  findet sich  anlaut.  d-  durch  Einfluß  von  urgerm.  *da^icaz  (idg.  "^dhogV^ho-,  s. ^dheg'^h-  ,brennen')  , warme  Jahreszeit'  (:lit.  dägas  , Sommerhitze'):  Der o-St.  got.  dagsy  aisl.  dagr,  ahd.  tac  m.  ,Tag'  ist  aus  neutr.  es-St.  umge- bildet (got.  PN  Jayia-d-eog  =  *Dagls-pius,  ahd.  Dagl-ber^t  usw.),  der  auch im  ablaut.  ags.  dceg  (*dö%iz),  PI.  dögor  n.  ;Tag'  (got.  fidur-dögs  ,viertägig'), aisl.  degr  n.  ;Tag  oder  Nacht'  neben  w-St.  adän.  degn  n.  ;Tag  und  Nacht' vorliegt.
WP.  I  849  f.,  WH.  I  467,  Feist  113  f.,  Sievers-Brunner  121,  243,  Wacker- nagel-Debrunnerlll  310f.
agh'  ,seelisch  bedrückt  sein,  sich  fürchten'.
Gr.  l)cxog  n.  , Beängstigung,  Schmerz,  Leid',  äx^viiai,  Hyo^-iai  ,betrübt sein,  trauern'  (Aor.  ^'x«x£;  '^Kaxöf.irjv,  Perf.  d:y,dxf]f^cct},  dxsvojv,  ayicov ,trauernd,  ächzend',  dxccxi^o)  ,betrübe';  hierher  wohl  äxO^og  ,Last,  Kummer' (*aXTOg),  davon  äxd^sa&ai  ,beladen  sein,  bedrückt  sein'.
Ags.  ege  m.  ,Furcht',  egisi-grima  gl.  larvula,  einst  n.  es-St.  *agiz  =  gr. ^/o.",  vgl.  ahd.  egis-llh  ,schrecklich',  egisön  ,erschrecken'  und  die  zu  o- und  e/z-Stämmen  erweiterten  got.  agis  n.  ,Furcht,  Angst,  Schrecken',  ahd. agiso,  egiso  m  ,  egisa  f.  , Schrecken,  Schreckgestalt',  ngs.  egesa  m.  , Furcht'; anord.  agi  m.  (-e^-St.)  ,FLircht',

=== POK_full 1787-1850 ===

PI., Arist. etc.) and 'ATAavT£iO(; (Kritias). 

References: VasmerZslPh. 8, 114 f., Pokorny Urill. 4, 70, 93, 109, 124. 

Page(s): 4 

Root / lemma: agh-(lo-) 

Englisli meaning: disgusting 

Note: 

Root/ lemma: agh-(lo-)\ "disgusting' derived from an extended Root/ lemma: agos-\ " 

fault, sin' produced. 

Material: Gothic 5^/s "opprobrious, ignominious', aglil=>a, aglo^ hardship ', us-agljan^ press 
', Old English eg(e)le^ offensive, unwieldy, unfortunate ', eg/an a66 " pain ' (engl. a/7' hurt; 
indisposed his '), eglian' to be felt painfully ', Middle Low German egelen' cause grief, 
Gothic aglusMy. agluba' SugkoAo^, difficult '; also (with puzzling suffix) Gothic aglaiteii. 
-/n. " licentiousness, wanton violence, insolence, sexual offense ', Old High German 
agaleizii.,-iv\. " discomfort; zeal ', agaleizo. Old Saxon agleto, agaleto Mn . " sedulous, 
keen '. 

Possibly here ow. agha- (=Avestan ayo^ "nasty', n. " horrible, damage ', aghala- 'bad '. 

Here maybe to Middle Irish aladu. "wound' {*agloton), mcymr. ae/e{u) 'pa\nM', ae/eum. 
"pain' {*aglou-). 

References: WP. I 41, Feist 15 a, Specht Dekl. 136, Loth RC. 38, 56. 
Page(s): 8 



Root / lemma: aghl(u)-{*heghel-) 

English meaning: rainy weather 

Material: Gr. axAu(; " fog, darkness ' 

Maybe alb. agu//'ba6 vision', agu ' dawn ' 

Old Prussian ag/on. 'rain' {u- stem), Armenian *a//- in afjafj, afjamufjkh ^ darkness' (Meillet 

MSL. 10,279). 

References: WP. I 41. compare Petersen Aryan and Armenian Stud. 126. 

Page(s): 8 

Root / lemma: agh- {*hegh-) 

English meaning: to fear 

Material: Gr. axo(; n. " fear, pain, grief, axvu|jai, axopai " grieving, sorrowing, mourning ' 

(Aor. HKaxE, nKaxopnv, Perf. aKaxniJC(i), axsuwv, ax£U)v " mourning, groaning ', OKaxi^u) 

"sadden'; here probably ax6o(; ' load, grief ' (* axTO(;), thereof axSsaGai ' to be loaded, be 

depressed '. 

Maybe nasalized alb. {*aghos) ankth "fear' [common alb. -s > -//?]. 

Old English egerc\. "fear', egisi-grima q\. " ghost, spectre, evil spirit ', n. es- stem *agiz = 
gr. a^oc, 'get a fright'; 

Note: common gr. -gh- > -x- 

compare Old High German egis-ITh' dreadful ', egison^ get a fright ' and to o-and en
```


### [2026-09-04T18:47:05.271Z] TOOL RESULT

```
=== KNT agur ===
1838:I. Stems in -й-: adj. par-u-, ard-u- in personal name Ardu-mants-, va-u- in personal names Déraya-vau- Vau-misa- Vahau-ka-; substantives baru- in Gau-barw-a-, maršiy-u- ‘death’ in adj. uvd-marSiyu-, mard-u- in Marduniya-, Mag-u-, Hitd-u-, Marg-u-, Kür-u-, uncertain bat-u- in bátu- gara-; loanwords pir-u-, Ufrat-u-; restored loan- word agur-u-; uncertain as to stem, Qatag-u-, sikabr-u-.
2157:Асе. Sg. Masc.: magum, zrafum, gidum; Dära- yava’um; Babirum, Margum; visadahyum; per- haps [agurum].
3338:DSk = Dars, Susa к: OP only, in 5 lines, stamped on a baked clay brick. Scheil 21.50 No. 9 (1929); Kent, JAOS 51.216-7 (1981); Brd. WZKM 39.53 (1932); Sen, OPI 130 (1941); Hinz, ZDMG 95.242 (1941).
3339:DSI = Darius, Susa 1: OP only, in 5 lines, stamped on a baked clay brick. Scheil 21.51 No. 10 (1929); Bv. BSLP 30.1.64-5 (1930); Kent, JAOS 51217 (1931); Brd. WZKM 39.54-5 (1932); Sen, OPI 130-1 (1941); Hinz, ZDMG 95.242-3 (1941).
3340:DSm =,-Darius, Susa м: Trilingual, on enameled’ bricks forming-a frieze in one of the
3342:halls; one line only to the brick, and the fragments very limited їп quantity. Scheil 21.53-6 No. 12 (1929); Brd. WZKM 39.55-8 (1932); Sen, OPI 131 n 1 (1941).
3367:XPg = Xerxes, PEnsEPOLIS а: An ornamental plaque in colored enameled bricks, intended to be placed on the wall of the palace, and found in fragmentary condition; 2 copies of the OP, in 14 lines, a number of fragments of the Akk. version, and a very few of the Elamite. Ill. London News, April 8, 1933 (colored illustration on page 488); Bv. BSLP 34.1.32-4 (1933) ; Kent, Lg. 9.229- 31 (1933); Hz. ApI 38-41 No. 16 and Plate 15 (1938); Sen, OPE 147 (1941).
3425:Spur. g: OP only, in 14 lines interrupted by figures in hollow relief, on а red brick tablet in à small private museum in Philadelphia. Dyen, JAOS 56.91-3 (1936); Eilers, ZDMG 91.407-20 (1937); Kent, JAOS 58.327 (1988); Sen, OPI 180 (1941).
4273:58 : agurum : akunava&a : avaiy : Babiruviy
4293:§3f. 28-30. And that the earth was dug down- ward, and that the rubble was packed down, and that the sun-dried brick was molded, the Baby- lonian people—it did (these tasks).
4301:§3k. 49-55. The goldsmiths who wrought the gold, those were Medes and Egyptians. The men Who wrought the wood, those were Sardians and Egyptians. The men who wrought the baked brick, those were Babylonians. The men who adorned the wall, those were Medes and Egyptians.
4943:aguru- sb. ‘baked brick’ (8158.1). lagurum] asm. DSf 53, supplied by König, Burgbau 52, after a-gur-ru of the АКК. text, ef. NPers. ágür in the same meaning. alg|ura[và] Ism. DB 4.89 (restored by Kent, JAOS 62.267, after König, Klotho 4.45); but read амуй аһа with Cameron.
5155:isti- sb. ‘sun-dried brick’ (5152.11, 5179.11): Av. tštya-, NPers. 110, Skt. istaka-, Medieval Skt. isttka- (König, Burgbau 51-2; Wb. AfOF 7.41; Hz. AMI 3.57-8; W. N. Brown, Lg. 8.13). 2328 nsf. DSf 29.
5399:jan- vb. ‘strike; smite, defeat (enemy ш. battle); mould (brick)’: Av. Jan- (gan-, Bthl. AW
```


## [2026-09-04T18:47:18.332Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT leaf of line 4943 ===\"; awk 'NR<=4943{if($0 ~ /\\f/) n++} END{}' KNT.txt; python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt'\nt=open(p,errors='replace').read()\ni=t.find('aguru- sb.')\nprint('leaf(0-based):', t[:i].count('\\f'))\nprint(t[i-1500:i+900])\nEOF"
}
```


## [2026-09-04T18:47:18.602Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AKD agurru ===\"; grep -n -i \"agurru\\|agurru\\|Ziegel\" AKD.txt | head -30"
}
```


### [2026-09-04T18:47:20.113Z] TOOL RESULT

```
=== KNT leaf of line 4943 ===
leaf(0-based): 187
| Auramazdáhà DPd 4,9; DPe 6f; DNa 16, 35, 49, 56{; DNb 6, 47f; DSe 15, 35, 42; XPa 12, 16f; А?Не 16. Auramazdahà (852.1II; $131; $185.IV) X Pf 34, 43; XPh 14, 33, 37, 44; A'Pa 18f.
AM nsm. (842) DSe 50°; DSi 3°; DS} 4, 6°; DSk 4; DSn 2^; D'Sa 3; A*Sa 4° (as gen., 5818.1), 4; A’Sd 3; А?На 5° (as gen), 6. АМташ DSk 5; D8m 3. AMm asm. DSk 4. AMha gsm. DSa 4; ligature ($42) DSk 4. AMha DS] 3°, 5; Аа 3. AMha or АМ№ DSd 3°; DSi 4°; DSm 5°; D8o 3°; D’Sb 4°.
165
Akaufaciya- adj. sb. ‘man of Akaufaka’; pl. a province of the Persian Empire: АКК. a-ku-pi-i-1$. Deriv. of * Akaufaka- ‘Kohistan’, prefix à + kaufa- ‘mountain’ + adj. suffix ($113, 814411; ef. Hz. AMI 8.72; Kent, Lg. 13.298-9). Akaufaciyd npm. XPh 27. |
akarta- adj. ‘not made, not built, unrepaired’; neg. a- + pte. of kar- ‘make’. {akarta] nsf. DSe 47 (conj. of Kent, JAOS 54.43).
azíaina- adj, with kdsaka-, ‘turquois’ (so Bleichsteiner, WZKM 37.103-4, and Konig, Burg- bau 63-4, but considered dubious by Hinz, ZDMG 95.235-6; hardly ‘gray amber’, with Hz. AMI 3.05—7, ApI 232; not ‘hematite’, with Scheil 21.29- 30): Av. arSaéna- ‘dark-colored’, borrowed in Gk. Порто “Atevos ‘Black Sea’ (‘in-hospitable’, by Gk. popular etymology, and euphemistically changed to Еф о), from neg. a- + z&atna-, cf. Av. xSaéta- ‘shining’ (§102, 5147.1). azšaina nsm. DSf 39.
axsata- adj. ‘unhurt, undisturbed’: neg. a- + pte. of xSan- ($102, §242.1), Skt. ksanóti ‘injures’, Gk. ктен, ‘kills’ (otherwise Foy KZ 35.49, Hz. Apl 70-1). azšałā nsf, DPe 23.
aguru- sb. ‘baked brick’ (8158.1). lagurum] asm. DSf 53, supplied by König, Burgbau 52, after a-gur-ru of the АКК. text, ef. NPers. ágür in the same meaning. alg|ura[và] Ism. DB 4.89 (restored by Kent, JAOS 62.267, after König, Klotho 4.45); but read амуй аһа with Cameron.
agriya- adj. ‘topmost, excellent, loyal’: Av. ayrya- ‘first in quality, etc.’, Skt. agriyd- agryd- ‘foremost, principal, etc.’, deriv. ($144.1V) to Av. ayra ‘der erste, oberste; (nt.) Anfang, Spitze’, Skt. dgra- ‘foremost, prominent, best; (nt.) tip, sum- mit, best part’ ($148.I). agriya пет. DB 1.21, as read by Cameron, replacing KT’s ag*r^ ++ (and the restorations thereof: dgar[ia] Wb. ZDMG 61.725, Tm. Vdt. Stud. 1.9, ef. Bthl. WZKM 22.72; ágra"|6a] Jn. Indian Stud. Lanman 255-7; ügr[mata] Konig, RuID 65; ágr[mà] Hz. Арі. 59- 62).
aciy adv. ‘then, at that time’ ($291.1V): Av. ajčit ‘and indeed’, Lt. ecquid (interrog.
```


### [2026-09-04T18:47:20.152Z] TOOL RESULT

```
=== AKD agurru ===
347:akk.  rat!dpu  zusammenfügen,  bautechn.  Bez.  für  das  Zusammen- fügen von  Mauern,  Häusern  usw.  aus  Ziegelsteinen  :  >  wohl  die  teclin. Bed.  von  späthebr.  rä-scq)  Steine  einlegen,  W-s^w  Pflaster,  aram.  r3mp pflastern,  rlspatä  Pflaster  O  arab.   ramfa,  rasafat).  akk.  kahiisu
428:akk.  libiMn,  st.  c.  libnat  Ziegelstein  :  >  hebr.  hbcnd,  aram.  hbentd^ Idiettü  O  arab.  libnat,  labinat)^  südarab.  Ibt,  sowie  wahrsch.  griech.  /;  Jillv&oi.
429:akk.  agurru  gebrannter  Ziegelstein  :  ^  aram.  'ägurd  O  arab. 'ägurr,  ^dgdr,  desgl.  pers.  dgdr,  armen,  agur,  griech.  ayovQog).  akk.
430:natbuhu,  nadbalm  wahrsch.  (Ziegel) schiebt  (neben  einem  natbalai,  nadbalai Gießbach,  von  tabdhi  gießen)  :  >  bibl.-aram.,  jüd.-aram.  nidbdl;  auch  midbdJc Bauschicht,  Steinlage  (>  arab.  midmdk).  akk.  gnssu  Gips  :  >
```


## [2026-09-04T18:47:30.880Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,pat,off in [('AKD.txt','agurru gebrannter',8),('AFA.txt','gurr',30)]:\n    t=open(f,errors='replace').read()\n    i=t.find(pat)\n    print('==',f,'idx',i,'leaf',t[:i].count('\\f') if i>0 else None, 'printed', (t[:i].count('\\f')-off) if i>0 else None)\nEOF\necho \"=== AFA leaf 35 (p.5) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==36' AFA.txt | head -60"
}
```


## [2026-09-04T18:47:32.690Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN agur/ajur ===\"; grep -n -i \"âgûr\\|agur\\|âǵûr\\|ājur\\|Ziegel\" HRN.txt | head -20; echo \"=== HUB ===\"; grep -n -i \"agur\\|Ziegel\" HUB.txt | head -20; echo \"=== PHD ===\"; grep -n -i \"ʾgwl\\|agur\\|brick\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-04T18:47:33.005Z] TOOL RESULT

```
== AKD.txt idx -1 leaf None printed None
== AFA.txt idx -1 leaf None printed None
=== AFA leaf 35 (p.5) ===
die sich bei diesem Worte zeigt. Echt arabische Worter
uraltester Herkunft pflegeu derartigen Wandel nicht zn
zeigen. Auch ist Sjui in alten Gedichten kaum anzutreffen.
Es fehlt auch im Äthiopischen. Auch verdient wohl Er-
wiigung, dass Lehm zu Ziegeln in Arabien nicht so häufig
ist, um allgemeines Baumaterial zu sein. Anders war es
bekanntlich in Babylon (Gen. 11, 3; Ovid Metamorph. Lib.
IV. 58). Aber zum Bau der ersten Moschee werden schon
Ziegeln gebraucht Belad. 6, 9.
Ebenfalls von den Aramaeru den Arabern zugeführt ist
1^1 , ;«^l 9 dessen verschiedene Yocalisatiousmoglichkeiten
zugleich mit dem Maugel einer Ableitung, der unarabi-
sehen Form und demPlur. ^«w^l Mu arrab 16, 7 auf fremde
Herkunft hinweisen. Es soll schon im Assyrischen vor-
kommen; vgl. Guidi Delhi sede. p. 16. Die Araber selbst
halten es für ein persisches Lehnwort; vei*gl. schon Gauh.
8. V. In Wirklichkeit aber ist yj^\ auch im Persischen ein
aramäisches Lehnwort , und dass die Araber es von *den
Persem übernommen haben sollten, ist nach sonstigen
Analogieen nicht wahrscheinlich. Es findet sich schon bei
Nabiga 7, 16; Div. Hufj. 66, 10; Agäni XVL 43, 3, wo
eine Hütte aus Rohrgeflecht einem Hause, das aus Oyps
und Ziegeln gebaut ist, gegenübergestellt wird. —
Deutlich fremd und als Fremdwort schon von den Ara-
bern erkannt ist JuyJ? (so in den Lezx ; in Wahrheit) Jua Ji
Nabiga 7 , 16; Tar. 4, 22; Mu'arr. 116, 14 Plur. Tab. L
852, 7. (davon denominativ jualS Nab. 7 , 31 ; 'Antara. 21,
36) = Kspxfuiij übernommen durch Vermittelung von
N"l^np lr-«^i-s- ^S^' Sachau zum Mu^arrab 52. Die
Form mit langem i der zweiten Silbe ist durch die Accen-
tuation des griechischen Originals xipxßiiiov schon in
Jen aramäischen Dialekten hervorgerufen worden, in denen
```


### [2026-09-04T18:47:33.071Z] TOOL RESULT

```
=== HRN agur/ajur ===
4431:488. x^Ht 'Ziegel, Backstein'.
4432:aw. istya- 'Ziegel, Backstein' ; phlv. /ist ; skr. isfakOr-
=== HUB ===
1938:488. Lies afgh. LW. xa^ta 'Ziegel*.
9512:aresa-, skr. rksa-; xist 'Ziegel', phi. oHst = zd.istya-; xism,
=== PHD ===
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:1086:brick xišt.
PHD_mackenzie.txt:5562:xl§t [hstl I (P hystyg), N . . . . ] brick.
PHD_mackenzie.txt:6079:bold wistax; v. brave.                 brick xist.
```


## [2026-09-04T18:47:49.260Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in HRN.txt HUB.txt NYB_vol2_glossary.txt; do echo \"=== $f ===\"; grep -n -i \"âgûr\\|âgur\\|agûr\\|ágúr\\|âǵûr\\|agûr\\|ājurr\\|âǧûr\\|Backstein\" $f | head -15; done"
}
```


## [2026-09-04T18:47:50.098Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM p.7 area ===\"; grep -n \"الآجر\\|آجر\\|آگور\" AFM_pages.txt | head -20"
}
```


### [2026-09-04T18:47:51.093Z] TOOL RESULT

```
=== HRN.txt ===
4431:488. x^Ht 'Ziegel, Backstein'.
4432:aw. istya- 'Ziegel, Backstein' ; phlv. /ist ; skr. isfakOr-
4433:'Backstein'.
=== HUB.txt ===
=== NYB_vol2_glossary.txt ===
```


### [2026-09-04T18:47:51.143Z] TOOL RESULT

```
=== AFM p.7 area ===
```


## [2026-09-04T18:47:55.937Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- AFM sample leaf 15 ---\"; awk 'BEGIN{RS=\"\\f\"} NR==16' AFM_pages.txt | head -30; echo \"--- grep aguru in AFM ---\"; grep -n -i \"ajurr\\|agurru\\|آجرّ\" AFM.txt | head"
}
```


## [2026-09-04T18:47:55.972Z] TOOL CALL #18: Bash

```json
{
 "command": "python3 tools/ref_page.py --help 2>&1 | head -30"
}
```


### [2026-09-04T18:47:57.698Z] TOOL RESULT

```
--- AFM sample leaf 15 ---
اصغر من ورق الفجل وهو حاذ الى الغابة ويستى ` 9 والقسم الاخر عدي
.| ܢ ورقه ܐ لبن قليل الحدة وزهره احمر٠‏ ٠اذا‏ سقيت سحرة ان ܐܝܒܨ عاء 25
.79 ܐܟܝ ܬ ܦܐ ܐ كثيرا »
ار 1 وان عا
باب الب
( 715 ) الفلا ل فارسي 0 ܐ له ܢܡܒ
س سر
ܟ <
( الما .© والمابوش ) معرب ابوج واصل ܐ 3 مغطي الرجل ܕ( نا نوس
بالتركية والكرد %
£ الم ونم ) تعر يب بابونه او يابونلك وهي حشيشة ذات زهر كتير النفع‎ ١
التحليل . ومنها السر ܨ ܒܒܘܝܐ‎
( المج .1 1 ܨ ܕ( | ܐܰܝ
( لبأ ) = لا اتاد 0
00 ب كيرة ة النفع في الأمرا ض السوذاوءة ܨܦ الأترجية
والتر ان رهي ܨ 09 11 ظات وهو ضرب من 1 ومن بوله 5 ܪ
2 اوغل 51
( 5 4 0 ܝ( تنفع من لدغ العقرب ܣ
09 فارساتها 0 البرهان 3130
2 من لدغ العقرب يقال له بالعر 032 ومفرح القلب > 0 بيك
ܡܠ 100 » وقمل انه اسم رنحان جبلي ورقه - ورق الريحان ورائحته
تضارع رانحة الاترجج »
( الباوزكر والبأزهر) حجر ينسّب اليه قوى غريبة في مقاومة السموم وهر
ܐ
ب لاف
--- grep aguru in AFM ---
```


### [2026-09-04T18:47:59.220Z] TOOL RESULT

```
Fetch ONE cited page of a scanned reference, on demand.

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
```


## [2026-09-04T18:48:08.151Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 9 10 11 12 13; do echo \"===== NR==$n =====\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' AFM_pages.txt | head -40; done"
}
```


### [2026-09-04T18:48:09.894Z] TOOL RESULT

```
===== NR==9 =====
حت آي ܝ
3 وهو ذو لسان 003 فبه ܨ )1 . ܣ(¿ فارسي مسرن >1 ٠وقال‏ ܝ
سفاء ܣ 6 تكون في السرج وغيذه ج أباذيم ويقال أبزين. .
وهو من ¥ بمنى ܢ عض فليس معرب لك :إبزيم ܐ £ حديدة في طرف اللزام
< :ܐ ويقال له ܐܢܐ زرفن وزرفين فين»٠قات‏ ان صعة هذا 3 ܚܨ على كإنه
0( معراقك اما عن 05 وهو المعماز او عن الفارسي ابزن وعر 1
من حديد اومن ܡ مصاوع ء! < ܝܝ على قدرقامة الانساناو 26
منها عليه غطاء ع مثقوب يضع شه الاطاء المريضُ و2 ,ܕܝ ن راسة من !ܝܢ 273
بصب 3 1:39 ܨ بالأدوية ܐ ` ابزن بالفارسة على
ܐܬܕܩ الصغير ايضا ومنهُ عرب (|% بزن ) وهو حوض يتس فيه ويعرف بالمغطس
وقد سحل من ܝ واهل ܦ يقولون بازاناً الحوض الذي 5 العين عند
الصفاء ٠‏ لانة شبه حوض ١‏ شنفاء » الغليل )
+ ( )¥ ]5 ) الطاعة ‏ تتول جات |( من الناس ْ 07 5371
الأخلاط والرعاع 0 البوش ) الماعة المختالطة 199 ܗ )0 0
اختلطوا فضِجُوا و( 6 القوم ¬ ٠‏ كل ذلك ماخوذ من أبأش ` ® دهي
جماغة مره "كل يشكال الناس ٠.‏ وقالوا فيها 06 01 ,01 ) النثتيء اي جمعة
9)
*< ܐ( مق السحاب تعريب ابْر ويرادفة الأرمني ودس 6: بأوت
والكردي 5 0 راو تور والروسي 064310
+ لي العظمة والبهجة معرب أب بآ 16031
ܕ | ܟ بالارامية ܦܐܢܐ ܦܐܐ ° ® بهي وبالفرنسية 18811
ܨ (( 56( الحارض الضعيف من القوم و عو لجل 955
ܐܝܟ المعاول والظاهر ان الفاسي ماخوذ من اليونالي :ܘܡܐ
( إلا جور اليا عور والا جور والا جر 0 وال جرون) قري ١‏ "لوز دعو
تراب يحكم عجلة وتقريصة 2 2 5 'وقالوا فيه أ جر الطين ٠‏ وييرادفة بالارمشة
سدمارس وقال )ܡܢܐ (ص 09110 اصل اللفظة ارا ى ܐܓܪܐ وهو موحود :
اللغة 32 القدعة ٠واما‏ العُرميد فهو @ 7
===== NR==10 =====
لكر له
| 0 13110 و 0 2 000 نالع ٠‏ ومئنهة الفرني ¢¢
والايطا ليائي - 0 3430 بالسر ± الدارجة 36
والكردنة ٠‏ وام الاصطبل فهو تعريب الرومى 562111111153
( إلا درون ) المثلفٍ والارى والوطن وهر إما معرب 50 80350 ,<
ماخوذ عن اليونائي ا ثاريه وهر القسم من ܝܗ الختص باارجال ܢ܆ܐ ܐܢܝܕܪܘܢܐ
11:20 ® ܕ[ 0 والقليد فاخوذان عن بسجده»: وعن 0 اي المخدع
وسبه مخدع
( الاذرريون ). زهر اضفر في 71005 5957 الذذ كو راصل 11 ]ا
شمه الثار. وآذر يون اغة فيه ± ` 096( حيجكى ( زهر القمر )
وقره كز ( العين السوداء )
3( الأرجان ) ,شر 4033( :3( 600390550901017 ا
ارجن وهو الفستق البري وقيل الاوز المر واسمة 6 9 اي لوز الل
( الترهان القاطع )
590 معرب )6.35 وهو سّحر له ورد 0 به 0
ويطلق 9 على 0 حمر والشاب الخمر والصبغ الأخر ٠وقيل‏ 0 عوده اذا احصارق
تفع لاإننات ܚܟ .ܕܟܕ بالارامية ܐܪܥܘܝܐܝ ܙ( 5 6( و 6 1
اللفظة سنسكر ܝܬ 10 ܐܦܬ نه من 5282 اي احمر ومن 724 وهى اداة
النسة ( القاموس العبرالي الكلداني تأليف جسنيوسء ضن : + ) (4) :
الأوارجة ) 5755 جسات الدخل والخرح يدون 3 )ا 1
مسدنّا من حسابات الديوان
+ ( الأرش ) ما 'يدفع بين السلامة والعيب في السلعة معرب رز وهو القيمة
5" (الأرْضي 039 ننات معروف ٠‏ .نا الصيغة غر يبة ٠‏ فلوو كان الاسم عربيا
لقمل الشوك الأرضي فهو عا 17 م 4 الفرني 56 ܐ( ܢܘܟ به
-210231طن) ]@ 1:31111123آط ع1 1231111216 1.2101 :115 1 موه ©
11121... 1125122 1847.
===== NR==11 =====
اليو نبا ܒ
(الأرغس) ' ور اشر أصل سح < ܨ 2 أرغش وفسره 5
القاطع 1ل شعرة اللا رياس (المسماة في الترمّة قادين طأوزلنى ) يدخل في
0 02 العيون ٠‏ 9 ܐܐܬ 0 اتلد 0 ® !¢ § (631032)
0 (الأريكة) ܐܝܟ ܨ اند ܝ ܢ أورنك وهو 041 ' أي
ܠ ومن 01
0 191 نت 00 0 كر ٠‏ والسريالي ماخوذ من الفارسي
2 وهو بعناه ويطاق ايضاً على سقف المت 8 قرن .0 به اليونالي 00
اي البيت والانكليزي 11146 ܐܨ 2
( الأزادرغت) تعر يبب 033 اي ور 50 “قال في البرهان القاط لع هي 3
مادة أزاد:< آزاد شجر يقال له 37 بكاين »> 3 بازادرغت » 380
أزاددرخت ما ܣܨ ܝ : *آزاددرخت * سجر يقال له في بلاد جرجان « زهر زمين > ( سم"
الأرض) ܢܢ فارس _يستى « طاق وطءك » 5 له ` ® ܐܢ̈ܕܐ وشجرة 3
ܝܬ للك واختلف كثيرًا في ماهيّة هذا الشجر. وقد قن اراي اكه مر ون
سجر الشييخ عاص لاد الفرس ورقة ܠܝܬ ورق الدذا لى مسموم قاتل اللموانات.
فقيل ان شجر «طاق » هو .الشجر المسى 96 «سكبيك اغاجى © ويعد شير ]
للنار وناره ܗܣ ويقال له ` ® غضا » ٠‏ وكتاب الفرائد 2 الطموع في
بيردت ܝ بالافرنسية ° 11125
2 307 تعر يب راس وهما < ٠‏ ومئة 0
ܐܙܒܐ
( لأسا بذة) ܝ ܨܝ 5 وهو ܣ > 3 حصان ومن ناد
أي حارس ٠‏ و باد تطلق ايضا على اعيان الملد وعمد نه
( الاوسينداج والاوسفيداج ) بياض.الرضاص 3 تعريب سيد نلك وممناء”
الانك الابيض ٠‏ ومنه 4 الارسي 6« | دي سياف
* :ܠܘ الذي يلف عليه الغزل ܐܟ 24008
اصن
===== NR==12 =====
ܗܕ ¢ ܙܝ
(الأستاذ) ܐܬܢ )ܪ الصناعة ورنسها ܠܚ 31 ܣܣ 4 سا <
والكركثة
( )ܠ ܚܡܕ الديياج الغليظ وقيل ديباج يعمّل بالذهب او ثاب + ܨ صفاق
ܨܝ عن استَبْر واصل ܢܓ الغليظ ^ الارامي ات دم
سر الأصاص او الرصاص 3:31 الردي نعر بب 8 ويرادفهة
ܝ 5 01 و0 : اي النحاس فاخوذ 9 ܥܨ 501 (فرتكلٌ
ضص: : ܐܘ ܙ ) والأبار من الاراءى ` ܐܒܪܐ
ܟ ܐ ©) 20 !ܥ ܀ ܨܣ 90 سر نبج وهو صبغ
ادر مصنوع من حريق الا نك والقلى وهو مركب من سسرخ 3 ® ومن 9¬=
0 نات تعلفة الدوات ܨܝ 1 ٠والفقصفصة‏ لغة ܦ ٠‏ .وقد
استعارتة السر ܬ ايضاً وهر فيها ܐܣܦܣܬܐ
* ( 9 والسقّند) الخردل الابيض وقيل 95 الابيض ٠والاول‏ ܟܝ
7 ܙ 5 الشطر ”` 9 الخردل وسفيك
الايض
ܐ `
الرصاص والانك تعريب اسفيداب واصل معناه الماء الابيض ومنة السسربالي
ܐܣܦ ܕܒܩܥܐ ش
( الأسكرجة والسم جة » إناء صغير مساه امقرنك اللزا :10
الغايل) .قا ܝܝ وفارسيتة 1 ١‏
0 ١الأسرّة)‏ القدوة «اخوذة 0 اسأً ومعئاها القاعدة والقانون وهي من ܪܕܐ
النشسه ايضاً . وقالت فيها 393 به اي اقتدى ٠‏ واما الآمي بعنى الطبيب فهو
و 5.5 1ل يك »هيع (فرنكل ض : \ \ ¥)
( |( > 9 نندت طويل الشوك ترعاه الإرئل ® من اند اي جسل ومن
غاز اي شوك
د 3 © < جدًا . يجتمل ان يكون ماخودًا 0"
المشرو بة لبلا
===== NR==13 =====
9 037 ` مط با كنا لاق
الذهب لانة يلحمة ٠‏ وبال له 28 « جادر اوشاغى »
١‏ الأسْتاقل ) ܣ .27 10 سش قاقل ويقال له بالتركة مبر ساجان
وجرخ فلك. ٠والششقاقل‏ ܕܐ‫ لعتان فيه
( £ ) ܨ݀ ܨܘ الابيض ܗ به السروح مغرب ادرنج ( اقرب
لموارد )
(الإشنآن) 8 .37 كنات
د لجع ١‏ يء يلتف على شجر الوط والصنو بر كأنة مقشود من عرق وهو
عطر ابيض ܘܐ )6 وعر باه - العجوز ومسواك القرود
× الأو الذي يزيين الرجل ܙ ܐܬ̈ܫ ܘܚܘ على ماده يأكل طعامه (اللشيان):
2 أشنا وهو الصاحب ܣܝ عريف ومن أ سنا 6 3
الا ماران والأسطوانة لطر الدعامة وقوا الدابة معرب ܐܝܝ
ومنه 4 الترى ܓ ردي 010 وا يا ܐܣܛܘܢܐ . ومن 4 ايضأ ماخوذ الأسطوان
ܗ الحمل ܐ العنق او ܢܟ ٠و‏ برادفه اليونالي. 00000 واطرمالي 506111
او 561155 و الادمني 7 ,ܨ ع 01701117
+ ( | ܟܐܝܐ واللأطبوط والأطبوط ) اللندق 00 157 قسن
9 3 مع الككحل يدفع 000 ان ܝ لو بماء رفيعة 0
١‏ البرهان اقاطم)
+ܨ )` ܨ 1050 00 .ܐ| مقطوع م من افروخان 7 لحارق ٠‏
و بوافقة اليونالي 2 اي ܨ والاتكايزي. 6 | 4 آنا والارمى 9 “̈§<
7ل معزب ܨ 8 هذه اللفظة موحودة في جميع ܠܐܝܐ المعروفة
واصلها ܨܝ 4:00 ܘ من :ܘ 5 العصير
(الأقنة) ات معرب عن خانه *ث 0 به الروسي. 60 اي 3
0 ܠ بمصر حجر الماسككة نافع 5 لعسر الولادة.
وقال !)ܝܣ : هو دواء هندي يشبه المندق الاان فيه ;; ,80 قليلا الى الغسبرة ما هو
واذا > 2 2 رك في وسطه ل واذا كسرتة اتفلق 0 سَبيه بام `
```


## [2026-09-04T18:48:33.429Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA leaf 21 (p.6) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==21' incoming/PLA/PLA_pages.txt | head -60"
}
```


### [2026-09-04T18:48:35.186Z] TOOL RESULT

```
=== PLA leaf 21 (p.6) ===
ägur                                                                             6                                                                ’adab


         - äßur:           "Backstein"                 pers.        I aus        dem       pers.       „ei Bßor Ip.                 >ur    ägur
             <      ap.        aguru        "Backstein"                2 <       akk.        aguru

disl - ”aßnäd: PL. v. „2 Zund s. Zund.

Aupı -         ’aßna:           "Wange"              aus     dem    pers.        &    f güne 3 "farbig;                     Wange"          mp. 3ır
             gonak       am.               gaona       "Farbe".             4    syr.        » wu,          hebr.     11T.


4isi- ”ifna = ”aßna
                 a. v.

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


„bi- Bdäb: Pl. v. _,ı adab q. v.

1        -’adab:           "gute          Sitten,           Anstand,            Höflichkeit"                aus   dem       pers.    _ı    adab     u.
              wei ayin <a.    IYpow                              alven       air.           *abi-dagna            8, (wahrscheinlich                eine
             ältere Entlehnung)-



1.       al-     Marta“             s.v
2.       Kent       S.     165,          Mayrhofer            S.    101
3.       Kiyäs.           v.
4.       Nyberg          Bd.        IIs,        v.
5.       Wahrmund              s.    v.,       LD.     s.     v.,      Addai         Scher       s.    v.
6.       Nyberg          Bd.        II    s.    v,
7.       Brockelmann                 s.    v.
8.       Nyberg          Bd.        II    s.    v.
```


## [2026-09-04T18:48:35.715Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT aγa ===\"; grep -n \"aγō\\|ayo-\\|aγa-\\|aya- \\[\" BRT.txt | head -20; echo \"--- BRT search 'schlecht' near a---\"; grep -n \"^aya-\\|^ayo\\|^ayö\" BRT.txt | head -20"
}
```


### [2026-09-04T18:48:35.782Z] TOOL RESULT

```
=== BRT aγa ===
--- BRT search 'schlecht' near a---
```


## [2026-09-04T18:48:47.581Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 BRT.txt; echo; echo \"=== grep aya- ===\"; grep -n \"aγ\\|aya-\" BRT.txt | head -10; echo \"=== grep 'böse' first 30 ===\"; grep -n \"böse\" BRT.txt | head -10"
}
```


### [2026-09-04T18:48:47.655Z] TOOL RESULT

```
Google
This  is  a  digital  copy  of  a  book  that  was  prcscrvod  for  gcncrations  on  library  shclvcs  bcforc  it  was  carcfully  scannod  by  Google  as  pari  of  a  projcct
to  make  the  world's  books  discoverablc  online.
It  has  survived  long  enough  for  the  Copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject
to  Copyright  or  whose  legal  Copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books
are  our  gateways  
=== grep aya- ===
2706:•  j,  aevo.gaya-  n.  'Längenausdehnung  |(>ij«(i">  me  yaoidäiUm  "ihr  könntet  mich eines  Schritts,  eine  Schrittlänge';  Äa/ ^«i-a  ,  purifiziren"  V.Äioo.  1,2  a)  mit  Gen. anys.anyaeibyö}  ya^a  'gatm  iu^a  (sd.) '  und  Inf.:  naj/a  .  .  Aäu  ni  ahmat  haca •gsimi  ,  .  "Wie  weit  von  einander?  "SiQ  gstaot  isalta  frasBtÖit  »eil  apasüföil  (sd.) viel  als  eine  Schrittlänge  beträgt  .  ."  "^  .{'^rayamcina  gämanam  P.  2jj>.  3)  '(es) p.  S.                                                                     I  können,  vermögen,  (dazu)  im  Stand  sein',
2731:Zum  V.  äs-;  s.  unter  ana-,  —  aL  ihm-  n.  — )  VgL  iKoDstT.  Dbr.  AiS.  185. j-,  g.  'aeä-  V.  'suchen'.  Praes.  3  isa-, a  isa-,  *»Ja-'',  14  b  tfasa-,  aisasa-", 17  (Fut)  aifya-,  30  (Iter.)  aSsaya-;  Perf. iyals-^,  yals-i\  —  PPfP.  isla-,  PFP.  k><7-;
2777:(Kaus.)  aisaya-,  adaya-.  —  Inf.  'istS;  Absol.  |  np.  xn,  KSs.  ii;  vgl.  tfi-  f.  'Deichsel'.  —  Pü. : 'ihmnitn.  \      "i  so  nach  Ga.  (und  Dst.),
3188:*J  Gemeint  ist  die  Zerstörung  des  Thebens  und alles  was  daiil  dient:  die  äaimichc  Gegen- achöpRing  [fiailyäta-)  in  dem  «Äunschen  gaya-. Vgl-  Bd.  I.  [ ;  iuadahiimk  i  ehrmazii  u  palyätak i  süräk  mrniii,  was  wesentlich  das  selbe  besagt wie  g'  ajy'.  Ohne  pa'ilyära-  wären  alle  aiiiri- sehen  Wesen  unsterblich.  S.  noch  Bd.  i.  6: kar  S  Hl  amiar  dahün  i  Shrmatd  tanärakömaH,!  u akanätakSmand  ei  en  an  i  andar  har  2än  meniik patmäii  ('Verlrag'}  däii/iid.  —  Pü.  beiiehl  die Stelle  auf  die  Schiffung  und  Tötung  des  Gaya Maritan.
3210:•  j.  ad-  V.  'sagen'.  Praes.  24  aoaya-,^ 30  (Iter.)  aiaya-,  PrP.  J»w;  Perf.  nJ:
3220:der  Spitze  des  Satz(teü)es  stehend  (s.  No. 5,6);  i)  zeitlich 'dann,  darauf,  da';  ''fra- yaire  ayati  .  .  "oa  apare  ayqn  "am  Vor- mittag . .,  dann  (aber)  am  Nachmittag" Aog.5^;  V.  ii.4,  20.4,  N.5J,  F.7,Vt/9. 48;  —  -da  tala  giul  pir>sat  aspm  "da fragte  der  Schöpfer  des  Rinds  das  A."  Y. 2^.2;  — 'da  sl''  ,.  bavaiti  sk>ndö  spaya- %raAyil  (sd)  Y.jo.io;  —  ya%a  va/i  iäd.) ..*''öai^  aaAö  a/ava'V.yi.16.  a)  hinter yäoi:  yet'A  sT  hvar»  nöit  uzttxlyeiti  °oa  . . "wenn  (erst)  die  Sonne  nicht  mehr  auf- geht, dann  . ."  Yt.  6.3.  b)  "oo  .  .  °cit °'6a  'dann  wenn  .  .  dann':  "aa  syäscif pairipataili  'oa  fraistim  vöiynanqm  (sd.) V.  7.3.         a)  anreihend  'und,  und  auch':
3413:•  j.  *a-ftTvayaDha-  n. 'NJchtgefahr,  Gefahr- \a%\^^\'C:*a'i:ra'"tih}m>''ya'i:raratui'i:wa- yar)k?m  ya^ra  apprmaynkö  3  *hg  "aini- iritim  starydti  ar,a  yat  v3  ya'^ra  '^waya- n/um  va  "»fum'^  t^S  "(ist)  daNichtgefahr, wo  der  R.,  Gefahr,  wo  der  Knabe  (sich befindet),  so  begeht  er  Sünde,  wenn  er ihn  (dem  Ratav)  nicht  anvertraut;  und (auch)  wenn  beide  (sich  an  einem  Ort befinden),  wo  sei  es  Gefahr  oder  Nicht- geiahr  (ist)"  N. /o'\
3473:20  afa-  (mit  <i)'>,  24  apaya-;  Perf.  3  ap'.
3503:apa-gaya-
3506:•  j.  apa-gaya-  m.  'Ausscheiden  aus  dem LebcQ,  Ableben':  'gayehe  Y.  46.  4  PUZ,, 4g.  10  PiiZ.,  41.  3  PQZ.,  5j.  8  PüZ.,  16. 10  PüZ.,  62.  4  PiiZ.JJ
=== grep 'böse' first 30 ===
3003:—  at  ..  dr?grai5  akäU  ^arihäii  (sd.)  •  j-  aka'tara-  Adj.  '(der  bösere,)  beson- paitiurvanöpaityeintl\.40-i\.  a)mitjders,  überaus  böse  (in  Wille  und  Tat) DaL  'Jmdm.  (gegenüber)  böse  (in  Wille  gegenüber-'  (Gen.)":  mtirim  ..  kam}- und  Tat)"':  tum  -kö  rahislasla  mi^ra  rs'.ö.jamm  daevanam  'nm  sraosyanqm ahi  masyJkaHbyS  "du  bist  (je  nachdem)  "■  ■  der  denen  überaus  böse  ist,  die  sich böse  und  (auch)  sehr  gut  gegenüber  den ,  strafbar  machen  .  ."  Yt.  10. 26. Menschen,  a  M»  Yt. /o.agijg;  — oiS«/«|  "  ^e'-  '"*"■  «■  F»Isch  KZ.  jo.  517. klil  {hd.)  aahat  ..  -kb  dngväitl  Y.47.  •  j-  aka'tas-  m.  Name  emes  Daiva: A)   in    religiös-moralischem    Sinn:  °tahm  daium  Y. 10.13,  '5  43-
3012:"aber   ihr    seid    dem   schlechlen  Denken :  •   j-  »tav-   m.  'Scheere,   scheerenartige entsprossen,  ihr  Z>a^t■a  alle,  und  er,  der  . .,   Waffe' :    nött   dtm  .  .  avasy/tl  notl    'Aavo und   der   Lüge   und   der  Hoffart"  Y.js.KNP.)  nSil  ..  Yt.I.iS. 3').         A  a)  mit  mainyav  m.  'der  bösei     ?';'  -?•■•*»•'/.  ^p«--  »»**.  "!•:  *''« Geist,  sva.  anra- matnyav:  hyat  vä  aka\      .       ,  ,  ■,.    ,r  ■,!>,,
3065:•  j.  aj-a-  i)  Adj.  (fem.  -ya-')  'schlecht, böse,  schlimm';  a)  von  Lebenden:  vJsp?n crf>m  tbisyantpm  A./.  10;  —  aivaAe  *aä maoyahe  °7«&V. /Äia;  11; — °7fl(NPm,)..  •  j.  afaäay-  £  'böser  Blick'  als  i/(it7Tsches Ryaottatfhö  YL/<>.37; —  "yais  dasi'äis  \ .  Leiden:  paitiltStie  °ly?i  pnUyä  äkityh  V. i-.i,;  —  -yanqmca    *5i/ranqm    'yanam/a  .  20.3; — ayase(\S.^)'iwqm  paiti.sanhsmi
3072:böse  Menschheit  sollen  die  Winter  kom- 1
3082:x''afitafutm     'yanqmca    daisanatn    "böser      gig.  'das  schkchie  Pein'.  —  Vi.:  rnnar  7sH-
3165:■übelste,  böseste"*:  dva  yaska..  -«(NDm.) I  V.  7. 70;  —  sHptibyasca  (sd.) . .  vispalibyasLa pairi  'taeibyö  \.  14.17;  —  °to«  rfuirfw- Aavö  'P.14;  —  nöil  hl . .  bvat  . .  zahistiJ anhuL.bi'ai  TTspariqm  *°/jm'^  *paosisl>mcix ya^  »riyat  daozaishum'^ . .  sondern  es  wird
3333:*)Den  nützlichen  wilden  Tieren  l/tä»'  ra/lärän ■ar'  (f-]>  all  deren  Ralati  der  Hase  gilt  (s.  unier dafliia-),  werden  Bd.  24.  10  die  daläa  ne  dasi Bmöiämn/io' gegenübergestellt  (nach  West  "which have  no  dread  whalever  of  tbe  band"),  die  ali 'böse'  (fii/)  bezeichnet  werden.  Aufs  Gleiche läuft  wohl  auch  die  Yt.  8.  36  getroflfene  Schei-
4112:•  j.  aDra-'>,  g.  angra-  Adj.  'feindlich; Feind';  katär^m  ä  'rS  vä  hi-S  va°rS  y3.. cyaithat  hvS  ndit  ayjm  'rB  mainyet!  "bei welchem  von  beiden  ist  der  Feind?  Oder ist  der  der  Feind,  der  .  .  Wie  ists?  Soll dernicht  für  einen  Feind  gehalten  werden?" Y.  44- 12;  —  al  tsi  vJsp^ng  -ring  *asaonS adarS  "denn  alle  ..^iaanhänger  machen die  (ja)  zu  Feinden"  Y.  43- 1 5-  a)  mit mainyOT-  m.  'der  arge,  böse  Geist'  ^Ahri- man')  im  Gegensatz  zu  spanyah-,  sp^ttia—. mainyü  .  .  yayä  spanyä  (sd.)  üitl  mraval ySm  'r»m  Y.  45-  2',  —  tä  i/raiasays) '■  taaa  wvMfJ  hist>nia  yat  *mainyu  däman
4117:•  j.  aBr5.mainyav-  Adj,  'dem  bösen Geist  entstammt,  zur  Schöpfung  des  bösen Geists  gehörig' :  iaAe  vaca  vanai  . .  kana zaya  mana  dqma  'yus  (IP,  als  APn.) ''  V. /»).8;  —  -ffl/  tat  dqma  spmfs.matnyava ailauhqm  dämanam  .  .  Aazatpraja  "yus (nämb  dama;  IP.  als  APn.)''  paiti.jasaiti V.13.1.  '
4119:•  j.  aorBjnainyava-    Adj.    'dem   bösen
```


## [2026-09-04T18:48:58.949Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',errors='replace').read()\ni=t.find(\"j.  aj-a-  i)  Adj.\")\nprint('leaf', t[:i].count('\\f'))\nseg=t[i-200:i+1200]\nprint(seg)\nEOF"
}
```


## [2026-09-04T18:49:00.075Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS grep āk/āγ ===\"; grep -n -i \"āk\\b\\|āγ\\|ʾk\\|ahōg\\|āhōg\" SNS.txt | head -30; echo \"--- SNS_pages leaf count ---\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' SNS_pages.txt"
}
```


### [2026-09-04T18:49:00.585Z] TOOL RESULT

```
leaf 64
 erlaubt  wird,  die Wahrheit  des  Gesagten  durch  ein  (>ottes- urteil  tu  erhärten;   vgl.  die  SS-  und  NpüErl.
•  j.  barata   birttim   "akyasdaoha    äfarl aesmtm  N.  /OJ,
Pü.:  fehlL
•  j.  aj-a-  i)  Adj.  (fem.  -ya-')  'schlecht, böse,  schlimm';  a)  von  Lebenden:  vJsp?n crf>m  tbisyantpm  A./.  10;  —  aivaAe  *aä maoyahe  °7«&V. /Äia;  11; — °7fl(NPm,)..  •  j.  afaäay-  £  'böser  Blick'  als  i/(it7Tsches Ryaottatfhö  YL/<>.37; —  "yais  dasi'äis  \ .  Leiden:  paitiltStie  °ly?i  pnUyä  äkityh  V. i-.i,;  —  -yanqmca    *5i/ranqm    'yanam/a  .  20.3; — ayase(\S.^)'iwqm  paiti.sanhsmi
Pairikanqm  Yty.104;  —  avi  ahum  ast-\Y.20.y.
Komp.;  aia-^asay.;  ^  26S.  $.  —  Bed.  und  Et. nach  Pü. ;  ayiii  i  fiilni  i  Sfi'JiPnilJr,  erL:   j
■iml/t-,  vgl.  Bd.  iS.  33,  ■
■    -«  dniz  i  s.wi.nm.-n  Kf  matnim i.  auch  Bd.  2S.  36  und  SBE.
■   •  j.  ayä-varBz-    Adj.    'der   Böses,    Übles
vanitm  "ygm^  *t^mö  jan/untu    "über    die !
böse  Menschheit  sollen  die  Winter  kom- 1
men"  V.i;.2i";  —  M  drvatqm    *°yqm'>
urvilnö    tffKö.hva    *mxansaiti   "der   zerrt
der  Ungläubigen  schlechte  Seelen  in  die
Finsternis  hinab"  V. /*j.  30;  —    mit  Dat.:
zTm  dakttktm  ..  'y»m  ^gai'^avayö  ". .  den   wirkt' :'</tt:i^(7  ..yö  'vari>/(NS.)''>  Yt  10.52.
für     die     Lebenden     schlimmen"     Y.  (/.      i)  iF.  9.  261.
```


### [2026-09-04T18:49:02.088Z] TOOL RESULT

```
=== SNS grep āk/āγ ===
--- SNS_pages leaf count ---
242
```


## [2026-09-04T18:49:08.256Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- SNS leaves 40-45 sample ---\"; for n in 42 43 44; do echo \"== NR==$n ==\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SNS_pages.txt | head -25; done"
}
```


### [2026-09-04T18:49:09.924Z] TOOL RESULT

```
--- SNS leaves 40-45 sample ---
== NR==42 ==
                                                                                                                                                          ,lu c-*ta **U •jlj                                 do
      Ot                                           r
                                                       Uit   c-^U *-L ijlj


                                                                                                                           .**»Lm     .   >£-*S « *jjli* ',j-jtf*A     iharapursaglh: -*CJA*W4>4?
                                                                                                                                          •   YA/1*»^    -TV**5 .(ij±>~sj hampursal:^


                                                  L-«l       :amiaspand:                        ji«j-**-hjo
                                                                                                                            .ay-a-t-r-i/T* 5 **                      (V):fca//        ka r'MT.         >*    r^
                                                                                                            :^                                       .6f_tr-f/Y^                .4i#5iJ ,«s-.KiA. 0>? (t)
                                                                    A/IT J
                                                                                                                                                                                                       .

                                                                •                 (   -*»«*>*•,£•
                                                                                                                                 ./,j j jr y«° jli#«>VA-rT-Vr-VY-V«/Y^ 'j^(Y)

                                                                                                                        Yr-YY-\6/r^ -ai/y^                      .^ji.^i^sbBka:                       **r-^>

                                                                                                                                                                         If/IY*-*          1Y/1- ^    -Y/Y^

               T©/tfi^       .   \»/!«S     ^U-j'j           *& amihraspand                 :          jio^c^t
                                                                                                                            -o            yi**:^:       lj jl   /I .gljSI       ka-s , *MT,s:              -u^*   -

== NR==43 ==
  ar                               Ll. c^-,Li uL*}\
                                                        }
                                                                                                                                                                  ,Uj^b*.L.;i                                 OT

Haurvatat       S Ameretat by       y- ,J                         .bS        *JLI*..
                                                                        ir
tlirji P.     y/adia. Bombay. 1888.
 amardat      :^    {AiWb 143-4) amaratStSt,-amaratat:-i
   i/TT ^.Y/TV^.T1-T6-6-r/)0^               1   t />T   ^   •
                                                                A/1 ^ -f J,* ^./
     -_t+ j'jj.1) .ojljj.ljj^l      l>i jUj«I
                                                                                                                                                                     1/6 <S ./->>>*-;       BaBxt&rls V
                                                :araurd3d-it                  f*- "

                                                                                                                                               (o-ib-iW                  I***) o^>» T ramoxtan:              mcyix
                                                                                                     ilWii*.                ^rawxtn            :    >;L           (wir.        Wan.   1,40) hmwxth: J**              A
                       rA. >i«.
            .*A^i£                li-ljaA :haradadist3n:
                          l
                                                                            \vw"H*»             fr




  TD2
== NR==44 ==
     £Q                                    U_   __U 4.L    «;i                                                                                                             • l'
                                                                                                                                                                            j'J                            OT



                                                                                                                                                                      .*.,»» :ham§lag:            A*oXC
                                 •   T1/W ^ .tfljo^^ian                             I:        «    w                                      Yr-tA-^/YY^ .(jjo-y^) hamdsa                            :   L


                                                                                                                                                .
                                                                                                                                                    ^ ^j
                                                                                                                                                       j .            .
                                                                                                                                                                          J W*a : hamemai :        XslS-^
                                                                                                              ham5m51 :^ C/KW>. 1776)haraSmar :** ham-<»ra0a-: t-



                                                 (   jjL. o^j.       .   &j 5 Uj v>* *^**
      U-r/n^         TT/1T^ UiW>.1817)su                         :       Lhu, hu :.k-                                                       (tt      ^ v^o*** ;ii                 )
                                                                                                                                                                                            .*£U*j5-<
                                                •f-r/TT^ -To/TT^ -VA/TaiM                                     I               To^^'a'j^^'O^WAthamSmaian:                                     >$>-»$X?
                                                                                                              I                                                                       w-16-U-V^
                                                                                     3
            aita:^ aeta-: tm .^1; gd / e,                                       HN       :    >»
```


## [2026-09-04T18:49:21.855Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ak:\\|āk:\\|ag:\\|āg:\\|akih\\|ākīh\\|ahok\\|āhōk\\|ahog\" SNS.txt SNS_pages.txt | head -30; echo \"--- python scans key ---\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d.get('SNS'),ensure_ascii=False)[:2000])\""
}
```


### [2026-09-04T18:49:23.517Z] TOOL RESULT

```
SNS_pages.txt:371:                                                                                                                   :hildag:                     3^^                  ,       b.       b^b :h5raln:                      *$t> Ifj* Jjp'al* j
SNS_pages.txt:1644:la              awaspfirand :L                               {Gkilain.                 75)     *bysp'r:^i             (^Pff.igjazdahak:^/ U£W>. 266) aziidahako                                                                :   L.
SNS_pages.txt:1651:                                                             3l  avistag/abistag: A*.ytM<
SNS_pages.txt:1683:         isti&Aji) •£t±-^*±'M±<*4*                              (pr.j>u)AAi.:              xafag/xapag: Jc#*
SNS_pages.txt:1695:                                                                                                                                                           HA-A/T** -*irf T '*^S-T:5bg5nag:                            s^v
SNS_pages.txt:1801:                                                                           :ab$zag/avSzag: •>«...          /\»*S   .   jp^i-wT .j^ji^T : 3pus bav£d:                  **«**-> -oie^*
SNS_pages.txt:1816:                                                                                                                                      1Y/Ifi^ -*^*ajJjj :appurdag:                   j»^>
SNS_pages.txt:1834:         mOzag +tf, ab§         -*i**b «j^oj->* -*i>\*                       :ab§mOzag: 4«.
SNS_pages.txt:1949:                           .^IjJ.ijU^.jrf^.^ xak: >* HZWRY*: -^                                                                                    r                         :
SNS_pages.txt:2007:                                                                                         *i-A   :astag:             li« M
SNS_pages.txt:2009:        (CiVPF. 20)stag: J-7asthi,asthan                                                 s   j|Sj^ast-i             <fl
SNS_pages.txt:2185:                                                                                                                      .AiiloJ^T :3hen I vidaxtag: j>4h/)«i ^ i^»j»
SNS_pages.txt:2241:      tj(,fc   :&)    .   W   ^ityfc . cxKi'jJ • *fi^ « j'j^                       :ajrryak: -3-^>"
SNS_pages.txt:2420:To        y»3^*Jti t, 4jl5 ,^,1 .aii wlrf-.T^Uailj j^L L |«air jjT :              ardag:^^*
SNS_pages.txt:2940:                                                                                                                                                                      .*.,»» :ham§lag:            A*oXC
SNS_pages.txt:2970:                                                                                                                                                      n^jSlUa .jjiyift :haragonag:                    -9tV-tf   ^
SNS_pages.txt:3034:         •   YA/.Y^             ojjljii . x^ii                       :m a   g nihend:3mo*v -j*c- i^                                                   :   ^ji^o*:^)                .•a#;I>* .*j>-b         :an-afsudag:             3r»VO*V
SNS_pages.txt:3036:     *ipr "UiU»-»l30 ^LwiUi« 4l4j :n ihadag:                     l
SNS_pages.txt:3042:     :        sud be nihadag:                                                9)*ii>e>**f -^»j        i-ihSi
SNS_pages.txt:3053:                                                                                                                      -^»>oVA>>J^ .^y*«*iP'J<» '*-*»* :xva stag:
SNS_pages.txt:3188:                                                                                                                               to/r^        .*a» Sl> i*o~ j^fcauai JV                          :havasldag:              qw***-V3V           \
SNS_pages.txt:3360:                                                                                                                                                               •6J*'*i*ja   :uzSnag: »3«««f
SNS_pages.txt:3461:         {Mir.      hwsgz^L                (cu-l*-U.          ^       J3  ^) *i>> :xOsag:                   3-«o*       CMan.
SNS_pages.txt:3512:                            •^*£'j**b «*a>, 4>                        :    x v ardag:    *J»**»
SNS_pages.txt:3516:                               •   J-i^ai.         ^j Y J>*W x Qrdak: ^                                                      :«*#& *,!•*>                 (                                     .JVfc
SNS_pages.txt:3536:                                                                                                      ..oUT^i^-^/^j,*: xvardlg I kardag: j*»-*w
SNS_pages.txt:3980:                                             ,   Tt/T i             (^^'•^ou^ :andarOn: ^.*             1                                          fr/fetf     -T/^ CCffPff.            27)afldak       :           L   hindak:^
SNS_pages.txt:3982:           sfn S .U.                     V        vfinag +          ^^a                          U.b:av 5 nag:                  *"«*
SNS_pages.txt:4259:                                                .^.•jljjT:    Srvarag:        *W*"
SNS_pages.txt:4364:                                                         (       \j_»-    :^) yak / Svak: JIM                                     >!* :o-jli .w^^tfjl^i; €v3rag-gah: -o-O^-*^                                         Y<
--- python scans key ---
{"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "covers_etymology": true, "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."}
```


## [2026-09-04T18:49:35.623Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && grep -n -i \"SNS\\|AKD\\|AFA\\|AFM\\|PLA\" bibliography_raw.txt | head -20"
}
```


### [2026-09-04T18:49:35.671Z] TOOL RESULT

```
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
6: TABLE IV - Reference Abbreviations 1 AEF 2 AFA 3 AFM 4 AHD 5 AHM 6 AID 7 AIN 8 AKD 9 AKM 0 AMD i ARB 2 ARK 3 ARM 4 ARP 5 AVG 6 AWH Jalal KhaleqT Motlaq, Asas Eshteqaq Farsi, ^j1* JISsAl o"1-'' Vol. I (a - kh), Bonyad Farhang Iran, 1977. Siegmund Fraenkel, Die Aramaischen Fremdworter im Arabischen, Hildesheim, 1962. Addi Shir, Al-Alfaz Al-Farsiyya Al-Mu'arraba, (A Dictionary of Persian Words in the Arabic Language), Library of Lebanon, 1980.. W. Morris, The American Heritage Dictionary, New College Edition, 1975, Appendix on Indo-European Roots, pp 1505-1550. I. Gershevitch, The Avestan Hymn to Mithra, Oriental Publications No.4, Cambridge University Press, 1959. G. C. Withworth, Anglo-Indian Dictionary. Kegan Paul, Trench &amp; Co, London 1885. E. Liden, Studien zur Altindischen und Vergleichenden Sprachgeschichte , Almqvist &amp; Wiksells, Upsala 1897. H. Zimmem, Akkadische Fremdworter Als Beweis Fur Babylonischen Kultureinfluss, Leipzig 1917. Amir J. ATam, Farhang A'alam Ketab Moqaddas or, A Dictionary of Proper Names in the Bible, English - Persian, Iran University Press, Tehran 1988. H. A" mid, Farhang Farsi Amid, Two volumes, Amir Kabir Press, Tehran, 1369 (1990). Jawaliqi, Al-Mu'arrab, Tehran 1966. M. H. Rokn Zadeh - Adammiyat, Arkan Sokhan, Sharq Press, Tehran 1347 (1968). ^W-\A£ h_)UT joMc' OwJbjd -W*c ^— *&gt;jl^ OwJfcjd £^~&gt; O^j' A. Aryan, ks~'j'* lSj^ ^)~&gt;^ ^*j' -ujUa ^la o^lj oiajs Farhang Vajheh-hay Hamanand, Armani - AvestaT, Pahlavi, FarsT, Vol. I (a), Bonyad Nayshabflr, Tehran 1363 (1984). F. Spiegel, Die Arische Periode und ihre Zustande, Leipzig ,1887. A. V. W. Jackson, An Avesta Grammer, W. Kohl Hammer, Stuttgart 1892. H. Kinder &amp; W. Hilgemann, Atlas of World History. 2 vol., Anchor Books, 1974. A-9 
12: TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll 
18: TABLE IV - Reference Abbreviations (continued ...) 64 MMF 65 MON 66 MPP 67 MZF 68 NAT 69 NFI 70 NYB 71 OEW 72 OXF 73 PEI 74 PHD 75 PHN 76 PLA 77 POK 78 PRT 79 RCH K. Khalili, Dictionary of Derivatives of the Persian ^wjls jiLa* ol£ii* &gt;_£^&amp;ji Infinitives or Farhang Moshtaqqat Masader FarsT, Institute of Cultural Studies and Research, Tehran, 1993. M. Mo" in, Farhang FarsT MoT'n, Six volumes, Amir Kabir press 1363 (1984). O^*® ^ ^-a-L!* Honari darbareh Zaban Farsi, Sokhan press, Tehran 1340 (1961). C. Berlitz, Native Tongues, Grosset &amp; Dunlapp Publishers, New York, 1982 F. Jonaydi, Nameh Farhang Iran, ^Ijjl ^»js i*b Bonyad Nayshabfir, Tehran 1368 (1989). Section 4, translated from C.H. Rempis' "Persische Worter im Deutschen," in Mitteilungen, Institut fur Auslands-Beziehungen, Iran-Nummer, 3/4, Stuttgart, 1960, S.229-233. H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1974. J. T. Shipley, The Origins of English Words, The John Hopkins University Press, Baltimore 1984. Jennifer Speake, Oxford Dictionary of Foreign Words and Phrases, Oxford University Press, New York 1997 M. Pei, The Families of Words, Harper &amp; Brothers press, New York 1962. D. N. MacKenzie, A Concise Pahlavi Dictionary. Oxford University press, London 1971. A. P. Pihan, Dictionnaire Etymologique des Motes de la Langue Francaise Derives de L'Arabe, du Persan ou du Turc, Paris 1866. Asya Asbaghi, Persische Lehnworter im Arabischen. Otto Harrassowitz, Wiesbaden 1988 J. Pokorny, Indogermanisches Etymologisches Worterbuck, Two volumes, Francke verlag, Bern 1959. E. Partridge, Origins - A short Etymological Dictionary of Modern English, MacMillan Co., NewYork 1958. J. Richardson, Dictionary, Persian, Arabic and English with Dissertation on the Languages, Literature and Manners of Eastern Nations, Sange-e-Meel Publications, Lahore 1829-1984. A-13 
21: TABLE IV - Reference Abbreviations (continued...) 80 ROE 81 SAP 82 SBK 83 SDQ 84 SHP 85 SIN 86 SKT 87 SLW 88 SNB 89 SNS 90 SOD 91 SOG 92 SOR 93 SPG 94 SYN 95 TAD R. Caliborne, The Roots of English, A Reader's Hanbook of Word Origins, Anchor Books, New York, 1989. A. Sayyah, Farhang Sayyah, Arabic - Persian Dictionary, ^}~&gt; «^a&gt;Js Three volumes, Translation of the Arabic "Al-Monjed" Dictionary, Eslam Publications, Tehran 1368 (1989). M. T. Bahar, Sabk ShenasT - Tarikh Tatawor Nasr Farsi, ^Ls ._£_&gt; Vol I, Tehran 1321 (1942). A. Siddiqi, Studien uber die Persischen Fremdworter im Klassischen Arabisch, Vandenhoeck &amp; Ruprecht, Gottingen 1919. J. T. Shipley, Dictionary of Word Origins, Philosophical Library press, New York 1945. G. Laufer, Sino-Iranica, Chinese Contributions to the History of Civilization in Ancient Iran, Field museum of natural History, publication 201, Anthropological Series, Vol XV, No. 3, Chicago 1919. W. W. Skeat, A Concise Etymological Dictionary of the English Language, Clarenden press, Oxford 1882-1967. W. B. Henning, "Sogdian Loan-words in New Persian", Bulletin of the School of Oriental and African Studies (BSOAS XT939-42) pp 93-106, University of London H. Kowsar, Sang Nebeshteh-ha Sokhan Miguyand, *ujj£~«&gt; Military Public Relations, Iranian Military Press, Tehran (1960's). M. Tavoosi, A Glossary of Shayast Ne Shayast, Shiraz University publications, 1986. B. Ghanb, Sogdian - Persian - English Dictionary, Farhangan Press, Tehran, 1374 (1995). jLw ^uu oV ijij ^imI^I - ^wjli -
```


## [2026-09-04T18:49:37.106Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT_v1 آک ===\"; grep -n \"آک\\b\" BQT_v1_pages.txt | head -20; echo \"=== BQT leaf for p.52 (leaf ~262) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==263' BQT_v1_pages.txt | head -40"
}
```


### [2026-09-04T18:49:38.793Z] TOOL RESULT

```
=== BQT_v1 آک ===
6612:آکش فروذ -ب بسن آش افرز اس
7099:خالی بات کل آدمی و حقیفت آن مر « آکی
7661:(۱) چب ۲ , چش : آکندن .
8378:آکی نرسید برتو ازمن سدبار مرا زتو وسید آلك . سوزنی.
8441:جلاب و کاهی خلاب خوانده اند . « لفت نامه >. ۴ - رله ۳ ِ_ رك:آ کح وآکج.
8448:0اعناا2 ( ۹8115022 ) در بهلوی بمعنی آوختن است * اوتوالا ۲۹۸ »؛ وآکته (آکته)
8454:آکندنی باشد مثل آنچه درجامه و لحافوباش
8493:قاسد و عمیوب و بیهوده . ۴ ره : اکح وآکج. ۴ - درکلمات مر کب مانند:
8494:جگر آکنج ( جگرآکند ) . رك : لت نامه : ۱ کنج .
8503:در خوب جامه خوب شوذ آکنش .
8505:آکیشید پمنی الدر آوشت - و چنکه درچیزی
8537:۱ - نیزآکنه: شد زمستان و زجودت بنه ای میخواهم ابرء و آستر وآکنه‌ای میخواحم.
8539:۴ نیز آکنیدن. . ۴ - یز بممنی جای دادن و دفن‌کردن ؛ زبر خاك کردن .
8541:این کسه جزدر حال ت رکب مستعمل نست ۶ لفت نامه *. ۱ - یزیمعنی حشوه آکنه :
8544:همچون : زهرا کین . کوهرآ کین » ضیقآ کین , طلسم آکین » عشرتآ کین » زرا کین . ر:
8551:« جنالی ۲٩‏ . ۵ آکنیده - ] کنده :
8552:منم در کشور عشقت خنیده دلی از مهر روت آکنیده شاکربخاری « لفت نامه * .
8554:۰ آگیبیفی - و آکیشبدن بممنی آویختن و پیچیدن . رك : کش .۲ ۰ وا
8927:آکندن (۲) است که پرساختن وانباشتن باشد .
9825:الیژ ه یر وزن تمیز ۰ شرارة آکش دا
=== BQT leaf for p.52 (leaf ~262) ===
آقای ۱ هت
آقال ۱ - بر وزن پاماا , افکندنی | وکنابه ازآفتاب هم هست؛ کوبند این‌لفت ت کی
ویکار نیامدنی‌وسقط را کوبند . یت
]قستقر ۴ . ۷ سین می‌نفطه و قاف بی ]. ]2 (۱) - بروزن چاك. بمعنی‌عیب وعار
وزن چارعنصر , مرغی باشدشکاری‌از جنس شاهین | باشد و آسیب و آفت‌را نیز کویند؟ - وبا کاف
و چر غویحری - ولف‌پادشاهان ترثهم‌بوده است.. | فارسی‌ام درختی است در هندوستان که شیرءآن
(4۱ چش : آ گه. ۱
متت: اخا دقرت ره ۲ کبک زد ان از تفا + مقر (شنگار
وشتفار یکی ازجوارح طیور) « لفت‌نامه ۰. ۰ ۴ - اوستا 38 بمعنی بد » شربر» بدی. < هرن»
آب۲۲۰» <بارتو لمهه 4 ۸۸۷8۲041 بمعنی‌بدهنش امت‌دربرابر وهومن (پاكمنش)«مزدسنا ٩۱۹۸‏
و این کلمه هیچ موستگی لفظی با نام آژی‌دهاك ( ضحاك ) ندارد «فاب ا : ۷ :
آکی نرسید برتو ازمن سدبار مرا زتو وسید آلك . سوزنی.
آگاه - اوستا 25 - 2 بممنی مكّفت شدن. مشاهده کردن؛ سان‌کریت 125246
« ظاهر شد * ؛ استی شرقی 0 < نگاء دن » , اهقه « چشم 0 » و نگاه در فارسی ازهمن
ریشه است « بارتولمه 404 » پهلوی 2۵125« نی رکه ٩‏ ات ۵ ۰ « اونوالا ۲۹۵ »؛
بمعنی مطلع » حستحطی » باخبر :
بی ۲ اه کردند از آن کارزار پی شاه را » فرخ اسفندبار. فردوسی ۶ لفت نامه *.
۰ آگ۴اهانیدن - رك : آ گاء » پهلوی ۵1625601020 « منلی ۲۵ »؛ یمعتی اعلام؛
تنبیه , آگاه‌کردن . خبر دادن : « ببامدم تاترا بیاگاهام. » تاریخ بیهقی « لفت نامه *.
۵ آگاهی - رف : آگاه . پهلوی "2261 « بب رکه ٩‏ » «مناي 6۲۹۵ < اونوالا
۰ بمعتی شناخت, خبر, اطلاع: معرفت: « این‌ملکه صیحتی کرده اسث وسخت وف گامی
ل طریح هقی » ۶« لت نامه ».
بقه از سفحهة ۵۱
جه ها تا بجای کلم اجه 8308 (عملاقل و رش سنید و ورگه قوم ) استسال شد چنانکه
در قرن هفتم غیر از برادران ۰ دمگران هم < باتو » و «ارفون» را باتوآقا و ارغون آفا میگفتداند
دروشتالسفا چاپ ببی ج ه ص ۵۷ و*۷ و حبیب‌السیرج ٩۳‏ . دراین قرن «آقا» ط با اسامی
مفولی تر کیب میشده ولی, در قرن هشثم با اسامی غیر مفولی نیز نی‌کیب می‌بافت مثلا «عانل آقا»
حا کم سلطانیه و سردار سلطان حسین ابلخانی (۷۸4-۷۷۹) که گاهی عم اورا «آقا» بطور اطلاق
میگفتند « روضةالسفاج ۵ ۱۷۸-۱۷۲ ِ» درقرن نهم علاوه برمردان ؛ زنانی بودند که < آغا »
در عنوان اسم آنان آمده مانند : « خدیجه بگم آقا » دختر حسن ببگه ثرکمان - بهر حالاین
کلمه خواه باول اسم درآید بابآخر آن . مقصود ازآن تعظیم وتجلیل است. «قل باختصار ازلمةٌ
آقا» بقلم کیوان سمیمی . مجلة آبنده ح ۳ شمار؛ ۲۱۳ . آقا که بدیبال با ابتدای اسامی خواجه
سرابان افزوده مبشده مثل * مبارككآقا» و «آفاالمای* و غیره » سد ها آنرا برای تمیز با «آفاه‌ی
علامت تفخیم و احترام دراسامی مردان باغین بعتی صورت «آغا» نوشته‌اند و آن در حفیقت‌ترجمة
کی هخواجه » است و آغا باشی معنی بز رکه خواجه نولیان را : دارد . «مجلهٌ باد کار سال سوم
شمارژ ٩۷ص‏ ۱۳۱-۱۳۰ .
```


## [2026-09-04T18:50:02.407Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT p.90 (NR==301) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==301' BQT_v1_pages.txt | head -45"
}
```


## [2026-09-04T18:50:03.213Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON آگور / آجر ===\"; grep -n \"آگور\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -20"
}
```


### [2026-09-04T18:50:04.286Z] TOOL RESULT

```
=== BQT p.90 (NR==301) ===
ست و 4 سب
#احر یض « بکر اول و دای بی نقطه
و سکون ثانی وتحتانی و صاد تقطه دار ء دآروبی
است که کلف را زابل کند » و انرا صفاهانی
«گل‌کافشه» (۱) کوبند وحربی «عصفر» خوانند .
احب ۵ » بکسر اول و سکون تانی
و فتح لام سگرن بای‌اپجد و کر دال بی‌قطه
و تحتانی بالف کشیده » بسربانی کیاهی است
شیر دار که در صراها و بختر در کنار جویها
وآوا بشیرازی «کاو -
نبطويك > خوانند . و
گوشد اگر کاو قدری
از آن بخورد بمیرد .
و کومفند را مضرتی
نرساند . شیر آن قلع
ددان میکند بی درد ۰ ۰ ۷ 46
اکر دو درم از شیر آن
بکی دهند البته مکشد. احلب دیا :
قوبا (۲) وجربدا نافم الف» کل؛ ب» میوه؛
باشد ٩‏ ۶
ج » دانه
اج « بنتح اول و سکون ثانی » بمعنی
آفرمن باشد که از تحسین است ۴ - ودر ترحم
وتأسف‌نیز کونند؟ ودرعرمی بمعنی‌بر ادرباشد *
اخج اخ ه بنتح هر دو همزه و سکون
هردو خا » بعمنی خوش خوش باشد که بعربی
طوبی و بخ‌یخ کوبند (۳)- و کاهی درمقام تسف
و تحر هم گفته میشود - و بضم هر دو همزه
در وقت نهایت حظ و لذت و خوش یگویند .
آخبون » با بای ابجد بروزن مجنون؛
میو نباتی است صحرایی مانند سر افعی و مبخ
آن از انگشت باربکتر باشد و برنگه سیاه بود.
کویند کزبدن جاوران را تافع است و جریی
(۱) خم ۳ : کاوشه . (۲) خم ۳ :- قوبا. (۳) چك , چب»: -گویند -
۱ ۱۱۳۵0۲۳5۵ < لف‌نامه»
قدیم باین عمی دیده نشده است. «لغت نامه».
۴ زهر یکه ارچشاند چه جای اخ؛ که خریخ
تیفی که او گذارد چه جای ام که به به < لفت نامه »,
۴ - حزوارش 3 « دهارله۷4 : آشوری بابلی ناک8» عبریاح. ۵, آرامی‌اها ۵12,
لغات جنوب الجزیره وحبشه احو لا810 « ولفنسون۲۸۳ *.
۵ احد - عربی بمعني‌يك » یکی. آشوری بابلی ۸000 ؛ عبری احد 21020 , آرامی
حد ۱۵20 . لفات جئوب الجزبره و حبشه احد 14 ولهنسون ۲۸۳ *.
‌ احبون - رك ؛ آخبون .
۴ - درزبان فارسی حاضر وهمچنین در ادبیات
```


### [2026-09-04T18:50:04.351Z] TOOL RESULT

```
=== MON آگور / آجر ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:2150:آجر: 2 (معر. آگور] (.) خشتی که در 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:4151:آگور: ۲اع [- [- آجر](.) خشت بخته» آجر, 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:4153:آگوری. 
MON_part1.txt:2150:آجر: 2 (معر. آگور] (.) خشتی که در 
MON_part1.txt:4151:آگور: ۲اع [- [- آجر](.) خشت بخته» آجر, 
MON_part1.txt:4153:آگوری.
```


## [2026-09-04T18:50:22.692Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2145,2158p' MON_part1.txt; echo \"...\"; sed -n '4145,4158p' MON_part1.txt; echo \"=== page markers? ===\"; grep -n \"\\[pdf page\" MON_part1.txt | head -3; awk 'BEGIN{RS=\"\\f\"} END{print \"leaves:\",NR}' MON_part1.txt"
}
```


### [2026-09-04T18:50:24.250Z] TOOL RESULT

```
آثار سفلی: اثرهای طبایع و آثار چها رگانه. 
آثار علوی [ع. الا ثار العلوية] (امر.) نزد قدما 
یکی از شعب طبیعی» در معرفت علل 
حدوت حوادث جوی. 

آجر: 2 (معر. آگور] (.) خشتی که در 
کوره پخته باشنده خشت بخته. 

اجل: ا2[2 ,101 ( 0( 2 با صدا! از گلو 
بر آید» آروع. آرغ. 

اجل: اه ل. ۰ (ص.) آبنده» يس آینده. 
مدت‌دار) دیرآینده. آخرت؛ مق. عاجل. 
آجودان: 2012۳ افسری (صاحب منصبی) 
...
آ گنده باشدء جگر آ گنده» جر غند. 

آ گنه 8 [ - آکنه) (ا.) آکنه. (گیا.) 
برجستگی کو چکك در سافه با ريشة کیاه 
(فره.) 

آگور: ۲اع [- [- آجر](.) خشت بخته» آجر, 
اگورگر: 5.7 (ص‌شغا.) آجرپز» آجری» 
آگوری. 


آ گاهانیدن 
و مدصقط2ع [د آگاهاندن - 
آ کهانیدن] (مسص م.) (] گهاند. آ گهاند؛ 
=== page markers? ===
leaves: 1
```


## [2026-09-04T18:50:31.336Z] TOOL CALL #32: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T18:50:31.341Z] TOOL RESULT

```


```


## [2026-09-04T18:50:35.346Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ail",
 "prompt": "Full etymology of \"ail\": Old English eglan/eglian, Proto-Germanic *azljaz, PIE root, and any cognates (Gothic agls, Sanskrit aghah). Quote verbatim."
}
```


## [2026-09-04T18:50:36.406Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/awe",
 "prompt": "Full etymology of \"awe\": Middle English aue, Old Norse agi, Proto-Germanic *agiz-, PIE root *agh-es-, cognates (Old English ege, Gothic agis, Greek akhos). Quote verbatim."
}
```


### [2026-09-04T18:50:40.969Z] TOOL RESULT

```
# Etymology of "Ail"

**Origin Chain:**
The word "ail" traces back through Middle English *eilen/ailen* to Old English *eglan*, meaning "to trouble, plague, afflict."

**Proto-Germanic Root:**
From Proto-Germanic *azljaz*, which also produced related forms like Old English *egle* ("hideous, loathsome") and Gothic *agls* ("shameful, disgraceful").

**Proto-Indo-European Root:**
The ultimate source is PIE *agh-* (1), meaning "to be depressed, be afraid," yielding the suffixed form *agh-lo-.

**Notable Cognates:**
- Gothic *agls* ("shameful, disgraceful")
- Gothic *agliþa* ("distress, affliction, hardship")
- Old English *egle* ("hideous, loathsome, troublesome, painful")

**Historical Usage:**
The phrase "what ails you?" dates to around 1300, originally appearing as "what eileth the?" By the late Old English period, the word extended to describe mental states and moods in addition to physical afflictions.
```


### [2026-09-04T18:50:42.201Z] TOOL RESULT

```
# Etymology of "Awe"

The word "awe" has ancient roots in Germanic and Indo-European languages. According to the Online Etymology Dictionary, it emerged around 1300 from Scandinavian sources, particularly Old Norse *agi* meaning "fright."

## Linguistic Ancestry

The term traces back through Proto-Germanic *agiz-* to the Proto-Indo-European root *agh-*, which carries the sense of "to be depressed, be afraid." Related words appear across multiple language families: Old English *ege* and Gothic *agis* (both "fear"), plus Greek *akhos* ("pain, grief").

## Semantic Evolution

Originally, "awe" simply denoted "fear, terror, great reverence." The modern meaning—combining dread with admiration—developed through biblical usage referring to divine reverence. The phrase "to stand in awe" emerged in the early 15th century, initially as merely "to stand awe."

## Modern Usage

The adjective "awe-inspiring" first appeared in written records around 1814, while related forms like "awesome," "awestruck," and "awful" evolved from this central concept.
```


## [2026-09-04T18:50:47.160Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%AC%D8%B1",
 "prompt": "Persian آجر (âjor) 'brick' — give the full etymology section verbatim, including any Arabic آجر, Middle Persian, Akkadian agurru, Aramaic mentions. Also list the Arabic entry آجر if present."
}
```


## [2026-09-04T18:50:47.593Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/agurru",
 "prompt": "Akkadian agurru — etymology, meaning, descendants. Quote verbatim."
}
```


### [2026-09-04T18:50:53.103Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T18:50:53.713Z] TOOL RESULT

```
# Etymology of Persian آجر (âjor) - "brick"

## Persian Etymology Section

From the Wiktionary entry, the Persian etymology states: "Borrowed from Arabic آجُرّ (ʔājurr)."

## Arabic Etymology Section

The Arabic noun آجُرّ (ʔājurr) meaning "burned brick" has this etymology:

"From Classical Syriac ܐܲܓܘܼܪܵܐ (ˀăḡurrā), from Akkadian 𒅇𒆪𒊒𒌝 (agurru, ukurru)."

## Complete Etymology Chain

The Persian word ultimately traces back through three ancient languages:
1. **Persian** (modern): آجر (âjor)
2. **Arabic**: آجُرّ (borrowed from Syriac)
3. **Classical Syriac**: ܐܲܓܘܼܪܵܐ (ˀăḡurrā)
4. **Akkadian**: 𒅇𒆪𒊒𒌝 (agurru/ukurru) — the oldest attestation

This demonstrates the word's journey through multiple linguistic families over millennia, originating in ancient Mesopotamia.
```


## [2026-09-04T18:50:58.533Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%DA%AF%D9%88%D8%B1",
 "prompt": "Persian آگور — is there an entry? Give etymology and meaning verbatim."
}
```


## [2026-09-04T18:50:59.267Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%DA%A9",
 "prompt": "Persian آک — is there an entry? Give etymology and meaning verbatim. Also any mention of Avestan aγa- or Middle Persian."
}
```


### [2026-09-04T18:51:00.658Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T18:51:03.038Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T18:51:08.587Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82e%C7%B5%CA%B0-",
 "prompt": "Is there a Proto-Indo-European reconstruction page for a root meaning 'to be afraid / distress' (*h2egh-)? Give the entry verbatim with descendants."
}
```


## [2026-09-04T18:51:09.070Z] TOOL CALL #40: WebSearch

```json
{
 "query": "Wiktionary Proto-Germanic *agaz \"fear\" Old Norse agi Gothic agis Avestan aγa Sanskrit agha"
}
```


### [2026-09-04T18:51:11.966Z] TOOL RESULT

```
Web search results for query: "Wiktionary Proto-Germanic *agaz "fear" Old Norse agi Gothic agis Avestan aγa Sanskrit agha"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T18:51:12.324Z] TOOL RESULT

```
Based on the content provided, I cannot find a Proto-Indo-European reconstruction page for a root meaning 'to be afraid / distress' (*h2egh-). 

The webpage shown is exclusively about **\*h₂eǵʰ-**, which means "cow," not a root related to fear or distress. The entry contains descendants in Armenian, Celtic, and Indo-Iranian languages, but none of these relate to the semantic field you're asking about.

To locate the entry you're seeking, you would need to search Wiktionary's reconstruction section directly for that specific root.
```


## [2026-09-04T18:51:17.696Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/agiz",
 "prompt": "Proto-Germanic *agiz 'fear' — etymology (PIE root), descendants (Old Norse agi, Old English ege, Gothic agis). Quote verbatim."
}
```


## [2026-09-04T18:51:19.256Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%98",
 "prompt": "Sanskrit अघ (agha) — meaning and etymology; any mention of Avestan aγa- or Proto-Indo-Iranian *agHás. Quote verbatim."
}
```


### [2026-09-04T18:51:20.344Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T18:51:27.845Z] TOOL RESULT

```
# Sanskrit अघ (agha): Meaning and Etymology

## Meaning
The Sanskrit word **अघ (agha)** functions as both an adjective and noun:

- **As an adjective**: "bad; evil; sinful; dangerous"
- **As a noun**: "evil; mishap; sin"

## Etymology and Proto-Indo-Iranian Connection

According to the Wiktionary entry, अघ derives from Proto-Indo-Iranian origins. Here's the relevant etymological information:

The word comes from Proto-Indo-Iranian **\*Hagʰás** ("bad; evil"), which itself derives from Proto-Indo-European \*h₂egʰ-ós.

**Regarding Avestan:** The entry notes that अघ is cognate with Avestan **aγa** ("evil"), demonstrating the word's ancient Indo-Iranian heritage alongside Ancient Greek ákhos and Old English eġle.

The documented usage appears in the Ṛgveda (circa 1500-1000 BCE), establishing this as one of Sanskrit's oldest attested terms for negative moral or unfortunate concepts.
```


## [2026-09-04T18:51:41.733Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.etymonline.com/word/ail' --note 'page 37, root Agh, node 6: English ail < OE eglan < PIE *agh-lo-' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/awe' --note 'page 37, root Agh, node 8: English awe < ON agi < PIE *agh-es-' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A2%D8%AC%D8%B1' --note 'page 37, root Agurru, node 5: Persian ajor < Arabic ajurr < Syriac agurra < Akkadian agurru' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%98' --note 'page 37, root Agh, node 1: Skt agha, Av. aga, PIE *h2egh-os' 2>&1 | tail -3"
}
```


## [2026-09-04T18:51:43.898Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ag/ak evil ===\"; grep -n \"^ag \\|^ak \\| ag \\[\\|agdēn\\|akoman\\|ak \\[\" PHD_mackenzie.txt | head -20; echo \"=== NYB ag ===\"; grep -n \"^ag\\b\\|'ak'\\|akōman\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-04T18:51:44.498Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/33872d7220e9ef48.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/420ba5a919cf3a63.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/def111c9b760eba7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0a3a9c6bab1ab3e.txt
```


### [2026-09-04T18:51:44.568Z] TOOL RESULT

```
=== PHD ag/ak evil ===
967: ak ['kl I N dk] evil, harm.
968: -ak [-kl IN.....,] diminutive suffix.
1080:andak ['ndk l I = M, N .....,] little, few.
1884:·darak [dlk l ] section, paragraph.
2967:hunusak [hwmk = Av. hunu/] offspring (daevic).
3206:karak [krk IN ......] quail.
3265:·kawadak [kw)tk l ] young; baby; v. kodak.
3269: -ak [_kl] ruler hostile to Zoroaster.
3323:kodak [kwtk I M qwdk, N --] young, small; baby.
3347: .......ak [-k l ] I N -hak] little cap; calyx.
3510:  . . . . ag [-k I N ........a] middling, average.
3653:namak [nmk ' I M nmyhk, N .....] salt.
3884:ozarak ['we'lk I M hwz'rk] little, small, few.
3992:pak [DKYA < A dky'; p'k I = M, N --] clean, pure, holy.
4381:redak [lytk I N ---] lad, page.
5153:wak [wk' I N bak] frog.
5573:xrohak [hlwhk' IN.......,] coral.
5584:xunak [hwnk I M xwnk, N xunuk] happy; cool.
5775:zardak [zltk l IN ......] safflower.
5828: zirak [zylk ' I M zyr, N . . . . ] wise, clever.
=== NYB ag ===
```


## [2026-09-04T18:51:53.217Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '960,972p' PHD_mackenzie.txt; echo \"=== PHD.txt ak ===\"; grep -n \"ak \\['k\\|] evil, harm\" PHD.txt | head -5"
}
```


### [2026-09-04T18:51:53.278Z] TOOL RESULT

```
 Ahila [TYBA < A Iby'; 'hwk' I M (')'hwg, N tihu] gazelle.
 ahunawar phnwl] the holiest prayer, beginning Ya8a ahu wairyo.
 a-hunsand ['hwnmd] dissatisfied.
    .....ih: dissatisfaction.
 ahy [KZY < A k-zy I M 'hy] soon(est), first.
 ajgahAn ['fgh'n' I M 'jg'h'n, N azgahtin] lazy, indolent.
    .....,ih: laziness, indolence.
 ak ['kl I N dk] evil, harm.
 -ak [-kl IN.....,] diminutive suffix.
 a-kAma~l)mand ek'mh'wmnd] unwilling.
 a-kanara~ ['kn'lk l I M 'qn'rg] unlimited, boundless.
    .....,lh: boundlessness.
 a-kard ['krt' I (M 'gyrd)] not done, undone.
=== PHD.txt ak ===
189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
```


## [2026-09-04T18:51:55.456Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN ail ===\"; grep -n \"^ail\\b\\|ail, v\\.\\|ail (\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== KLN awe ===\"; grep -n \"^awe\\b\\|awe, n\\.\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== SKT ail/awe ===\"; grep -n \"^AIL\\|^Ail\\|ail, to\\|^AWE\\|^Awe\\|awe, dread\" SKT.txt | head -10"
}
```


### [2026-09-04T18:51:55.559Z] TOOL RESULT

```
=== KLN ail ===
KLN_1966.txt:2041:ail
KLN_1966.txt:2042:ail,  tr.  and  intr.  v.  —  ME.  eilen,  alien,  fr.  OE. eglan ,  ‘to  molest,  trouble’,  rel.  to  Goth,  agls, ‘shameful’,  agio,  ‘distress,  oppression’,  us-agljan ,
KLN_1966.txt:8061:Coccus,  n.,  a  genus  of  insects  of  the  family  Coc- cidae.  —  See  prec.  word, coccyg-,  form  of  coccygo-  before  a  vowel, coccygeal,  adj.,  pertaining  to  the  coccyx  ( anat .) —  Formed  with  adj.  suff.  -ai  fr.  Gk.  xoxxui;, gen.  xoxxoyoc.  See  coccyx, coccygo-,  before  a  vowel  coccyg-,  combining  form denoting  the  coccyx  (med.)  —  Fr.  Gk.  xoxxui;, gen.  xGixxOyog.  See  next  word, coccyx,  n.,  the  end  of  the  vertebral  column  in nan  and  in  some  apes ;  the  rudiment  of  a  tail (anat.)  —  Gk.  x6xxu5,  gen.  x6xxuyo<;,  ‘cuckoo;
KLN_1966.txt:17848:hippopotamic,  adj.,  pertaining  to,  or  resembling, a  hippopotamus.  —  See  next  word  and  -ic. hippopotamus,  n.  —  L.,  fr.  Gk.  177770776x0:0.05,  lit. ‘horse  of  the  river’,  fr.  (717101;,  ‘horse’  and  770- xa(xo;,  ‘river’.  See  hippo-  and  potamo-. Hipposelinum,  n.,  a  genus  of  plants,  the  lovage (hot.)  —  ModL.,  fr.  Gk.  iTnroaiXEvov,  ‘coarse parsley’,  lit.  ‘horse  parsley’,  fr.  (777704,  ‘horse’, and  <r£X(vov,  ‘parsley’.  See  hippo-  and  parsley and  cp.  the  second  element  in  Petroselinum. hippuric,  adj.,  pertaining  to  the  acid  C9H9N03 (1 chem .)  —  Compounded  of  Gk.  (777704,  ‘horse’, and  oupov,  ‘urine’  (see  hippo-,  urine  and  adj. suff.  -ic).  This  acid  was  so  called  because  it  was first  found  (by  Rouelle)  in  the  urine  of  horses. Hippuris,  n.,  a  genus  of  plants,  the  mare’s  tail (bot.)  —  ModL.,  lit.  ‘horse’s  tail’,  fr.  hippo- and  Gk.  oupd,  ‘tail’.  See  uro-,  ‘tail-’.
KLN_1966.txt:24835:Myosurus,  n.,  a  genus  of  plants,  the  mousetail (hot.)  —  ModL.,  lit.  ‘mouse’s  tail’,  fr.  Gk.  |xup, gen.  [xuop,  ‘mouse’,  and  oupS,  ‘tail’.  See  myo- and  uro-,  ‘tail-’.
KLN_1966.txt:26111:ail,  ‘eye’,  fr.  L.  oculus.  See  ocular  and  -ade. oen-,  form  of  oeno-  before  a  vowel.
KLN_1966.txt:33836:Saururus,  n.,  a  genus  of  plants,  the  lizard’s  tail (hot.)  —  ModL.,  lit.  ‘lizard’s  tail’,  fr.  sauro-  and Gk.  oupx,  ‘tail’  (see  uro-,  ‘tail-’) ;  so  called  from the  appearance  of  its  crowded  flowers.
KLN_1966.txt:40501:Tumix,  n.,  a  genus  of  birds,  the  button  quail (ornithol.)  —  ModL.,  aphetic  for  L.  eoturnix,  ‘a quail’,  which  is  dissimilated  fr.  earlier  cocturnix, quocturnix,  from  base  *qwok-,  imitative  of  the quail’s  cry.  Cp.  Cotumix.  For  a  similar  imitative base  cp.  quail,  the  bird.
KLN_1971.txt:10041:ail, tr. and intr. v. — ME. eilen , alien, fr. OE. 
KLN_1971.txt:41375:a variant of wail (q.v.) 
=== KLN awe ===
KLN_1971.txt:24095:awe, n. — ME. agke, awe, fr. ON. agi , rel. to OE. 
KLN_1971.txt:126902:awe of’. See reverent. 
KLN_1971.txt:206198:awe’, gerundive of revereri, ‘to revere’, see re- 
KLN_1966.txt:4145:awe,  n.  —  ME.  aghe,  awe,  fr.  ON.  agi,  rel.  to  OE. ege,  ‘fear’,  OHG.  agiso,  ‘fright,  terror’,  Goth. agis,  ‘fear,  anguish’,  prob.  also  to  OHG.  z-agen, MHG.,  G.  zagen,  ‘to  fear,  hesitate’,  and  cogn. with  Gk.  ‘pain,  grief’,  dyopai,  ‘I  am  af¬ flicted’,  Olr.  -agor,  ‘I  fear’.
=== SKT ail/awe ===
485:AIL. ■ad  i$mart,  to  help.  pp. •-  — L.  a/fiufant;
1229:Awe.    (Scand.)     M.  £.  ay,  a^he,  awi: also  /v,  t^Af,  eyt;   all   orig.  di      "  * The  latter  5«t  arc  from  A.S.  ^^    ^
```


## [2026-09-04T18:52:23.617Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 agh ===\"; grep -n \"agh-(lo-)\\|aghlo\\|agh- (lo\\|agh-\" incoming/WLD/WLD_Bd1_pages.txt | head -10; echo \"=== IEC agh ===\"; grep -n \"^agh\\|^aghos\\|^aghlo\\|^agh-\" IEC.txt | head -10; echo \"=== SYN fear/evil agh ===\"; grep -n \"ON. agi\\|OE. ege\\|Goth. agis\" SYN.txt | head -10"
}
```


### [2026-09-04T18:52:23.715Z] TOOL RESULT

```
=== WLD Bd1 agh ===
3090:                                                                                                     .    agh-borre ds., vgl. z. Bed. auch
3708:40                                                 agh-   — agh-
3710:agh- „seelisch bedriickt sein,                    sich ffirchten".
3745:ganz fraglich. Beziehung unseres *agh- zu *angli- „eng, einengen, schnfiren"
3754:agh- „bedurfen, begehren" (aigh-l                      s. u.).
3794:                                         agh-(lo-)   — aghl-(u)-                                                     41
3820:agh-(lo-) „widerwartig“.
3853:  Beziehung zu *agh- „seelisch bedriiekt sein, furchten“ ist nicht sehr walu--
10296:auch Boisacq 1095; Coilitz Grm. Praet. 79 erklart g aus *sagh-t oder
10297:*sagh-s-t zu dt. sagen gr. gyg „Schall, Geton, Gerausch,,; Bechtel Lexil. 45
=== IEC agh ===
241:agh- ‘dread, terror’. Cf. aghos, aghtis Cf. Olr. ághathar ‘he fears’; OE öga; ON ógn, ógna, œgr, ægja, ægir, oegi-.
242:aghəlos, aghulos “evil, sorrow’. Cf. aghos, oghlos Skt. aghalab, ahurab; cf. W aeleu ‘sad; grief’, aeled ‘ailment’; Go. agls, aglus; OE egle, egile
243:aghi “but, yet, indeed”. Cf. a, ghi Skt. a + hi; OCZ. a£, aže; Li. ogi
244:aghná, aghinà, aghənå, us ‘awn, chatt. WP I, 30 Gk. ákhna, ákhnē; OHG agana; OE egenu;
247:aghó, io 'groan, fear, sorrow'. WP I, 40. Cf. aghos, agh-, ngh. Gk. ambig. Gk. ákhomai, ákhos; Go. agan, us-agjan; ON agir 55.; inf. aga; G egen, v.
248:aghos, -es- “evil, harm, grief, pain, horror.
250:aghtis, ios “horror”. Cf. agho, aghos Cor. óth; ON ótti, id.
281:agheros “lake, pond’ Gk. cf. Akhéron (a river in Epirus); OCS jezero; R ózero; Li. é-Zeras; Latv. ezers
282:aghios, io “edge, border OHG egga, ecka; OE ecg; Li. ee and eZia; cf. ant-eZis; Latv. eža
=== SYN fear/evil agh ===
29058:16.53 FEAR, FRIGHT Goth. agis, faurhtei Lith. baimeé, bailé, i8gqstis rk §to5, oe st ON atti, dgn, hrezla, Lett. bailes ; NG $6805, ai tus, pavor, skelkr ChSl.  strachit, bojaznt ot. timory Dan. frygt, skrak SCr.  strah, bojazan terror iinore;_ spe Sw. fruktan, skraéck Boh. _ strach, bdzer It. paura, d OE ege, egesa, fyrhto Pol. bojazi, strach, trwoga vento ainte, effrot ME fere, eye, frizt Russ. strach, bojazn’ peur ria pavura, NE fear, fright, terror Skt.  bhaya-, bhiti-, bhi-, Sp. pieeee ’ Du. vrees, schrik trasa- oe teamd, spaimd OHG  forhta, egi, egiso Av. Owaésah-, byah-, Rum. Ug ia MHG  vorht(e), ege, eis, tarSti- I ae faitcheas, schreke Nir. age han NHG _ furcht, schrecken
29091:5. Goth. agis (ON agi ‘terror’), OF ege, egesa, ME eye (NE awe), OHG egi egiso, egisa, etc., MHG ege, eis, ON aut, ogn, with vbs. Goth. dg (pret. pres.) ‘be afraid’, dgjan and us-agjan ‘frighten’, ete. : Grk. &xos ‘pain, distress’, Ir, -dgur ‘I fear’, vbl. n. dighthiu ‘fear’. Walde-P. 1.40. Falk-Torp 37. Feist 14, 380.
32231:ON gna, fr. dgn ‘dread, + ‘threats’ : Goth. agis ‘fright? afraid’, etc. (16.53).
```


## [2026-09-04T18:52:25.860Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON آخ ===\"; grep -n \"^آخ:\\|آخ:\" MON_part1.txt | head -10; echo \"=== TAD/ARB ajurr ===\"; grep -n \"آجر\" TAD_pages.txt ARB_mo3rb.txt ARB_abdulraheem.txt 2>/dev/null | head -10; echo \"=== LKT agurru ===\"; grep -n -i \"agurru\\|adschurr\\|ajurr\" LKT.txt | head"
}
```


### [2026-09-04T18:52:25.959Z] TOOL RESULT

```
=== MON آخ ===
2219:آخ: »2 (صت.) کلمه‌ای ۱۳ 
=== TAD/ARB ajurr ===
ARB_mo3rb.txt:16970:6 فى اللسات : « والطوب ؛ الآبر' بلق أهل مصرء والطوبة الآجرةة ؛ ذ كزها الشاذعى » ٠‏ 
ARB_mo3rb.txt:18465:8 قال ابن درييد - 2 الفرميد “قالوا : هو الآجر بالرُومية»] و دشّىء اي 
=== LKT agurru ===
```


## [2026-09-04T18:52:39.506Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3845,3860p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== WLD 3820-3840 ===\"; sed -n '3820,3845p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-04T18:52:39.576Z] TOOL RESULT

```
                                                                               :
                                                             der sich hingegen     ,


lit.      aglumu „in Bausch und Bogen, in Summa“ (Prellwitz, Fick III 4 9)
        agh'i,

gut fiigt (ware also ein idg. *oghlos „zusammengedrangt, Haufe“).
  Beziehung zu *agh- „seelisch bedriiekt sein, furchten“ ist nicht sehr walu--
scheinlich.

aghl(u)- etwa ,,dunkle Wolke, regnerisches Wetter“.
   Gr. dyXvg „Hebel, Dunkel“, apr. agio   n. ,,Regen“ (a-St., Pauli KSB. 7,
158f.), arm. *alj- in aljamiljlcli „Dunkel“ (Meillet Msl. 10, 279).
   Andere Deutungen von uyjIvg verzeichnet Boisacq 10S.

=== WLD 3820-3840 ===
agh-(lo-) „widerwartig“.
   Got. agls „alayg6g, schimpflieh“, aglipa , agio „Drangsal“, ns -agljan „be-
drangen, plagen", ags. eg(e')Ie „widerwartig, beschwerlich, bedauerlich",
eglan „Schmerz zufiigen“ (engl. ail „schmerzen        unpiifilich sein“), eglian
                                                                   ;


„schmerzlich empfunden werden“, mud. egelcn „Gram verursachen“, got.
aglus Adv. agluba „dvoy.o2og, dvay.62.cog, schwierig“ l ) auch (mit forman-
          ,                                                                    ;



tischem -aita-1 Wiedemann BB. 28, 50) got. aglaitei f., -i n. „dasXysia,
Unzucht“, ahd. agalei-p, f., -i n. „Unbequemlichkeit; Eifer“, agaleijO as.
agleto, agaleto Adv. „emsig, eifrig“;
   air. ail ( *agli -) „Schimpf‘ (Pick II 4 S;.
   Moglicherweise hierher (z. B. Pick I 4 14, 367, Feist Got. Wb. 9, Prell-
witz 2 347) ai. aglul- (= av. aya-) „bose“, n. „t)bel, Schaden“, agltalu-
„schlimm“ (der Wert dieses Suffixes -la- fur den Vergleich darf nicht iiber-
schatzt werden; anders, aber nicht besser vergleicht Siitterlin IF. 4, 92 f.
aghd- als *nyli<>- mit -nac in dt. Schabcrnad:, necken „qualen, peinigerf ').
   Aber gr. dylog ,,gro6er Ilaufe, Liirm, Belastigung", oyXito belastige,
drange von der Stelle“ (Fick, Prellwitz aaO.), stiinmt weder im Vokal o-
(: air. a-), noch in der Bed. „sich driingender IIaufe‘
                                                                               :
```


## [2026-09-04T18:52:41.276Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2216,2224p' MON_part1.txt; echo \"=== ARB آجر main ===\"; grep -n \"الآجُرّ\\|الآجر\\b\\|أجر' فارسي\\|آجُرّ\" ARB_mo3rb.txt | head -10"
}
```


### [2026-09-04T18:52:41.358Z] TOOL RESULT

```
و تانبه .)٩‏ ۲ - دستگاه ۱/65 (آحاد اصلی 
در این دستگاه عبار تند از: متر 0 کیلوگرم 
و تانبه 6). 
آخ: »2 (صت.) کلمه‌ای ۱۳ 
افسوس» احساس درد و رنج یا تحسین 
گویند؛ وای؛ اف. 
اخال: 21 (.) هر چبز دور انکندنی» 
سقطء آشغال. . تراشة چوب و قلم. . حس و 
خاشا کث. آب آورد؛ حجفاء. 
=== ARB آجر main ===
16970:6 فى اللسات : « والطوب ؛ الآبر' بلق أهل مصرء والطوبة الآجرةة ؛ ذ كزها الشاذعى » ٠‏ 
18465:8 قال ابن درييد - 2 الفرميد “قالوا : هو الآجر بالرُومية»] و دشّىء اي
```


## [2026-09-04T18:52:59.947Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AKD.txt',errors='replace').read()\ni=t.find(\"agurru  gebrannter\")\nif i<0: i=t.find(\"agurru\")\nprint('idx',i,'leaf',t[:i].count('\\f'),'printed',t[:i].count('\\f')-8)\nEOF\necho \"=== TAD آجر ===\"; grep -n \"آجر\\|الآجور\" TAD_pages.txt | head -10"
}
```


## [2026-09-04T18:53:01.471Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD/WEB ail awe ===\"; grep -n \"^ail\\b\\|ail (al)\\|OE. eglan\\|AS. eglan\" FSD_vol1.txt WEB_vol1.txt 2>/dev/null | head -8; echo \"--- awe ---\"; grep -n \"ON. agi\\|Icel. agi\\|awe (a)\\|AS. ege\" FSD_vol1.txt WEB_vol1.txt 2>/dev/null | head -8"
}
```


### [2026-09-04T18:53:02.722Z] TOOL RESULT

```
idx 83978 leaf 40 printed 32
=== TAD آجر ===
```


### [2026-09-04T18:53:02.905Z] TOOL RESULT

```
=== FSD/WEB ail awe ===
WEB_vol1.txt:1542:ail,
WEB_vol1.txt:4973:ail, n. indisposition or disease. TES z
WEB_vol1.txt:4983:ail/ing, a. sickly; ill. Bes S.
WEB_vol1.txt:18128:ail; to moan or wail
WEB_vol1.txt:18625:ail- be-scratch’, v.t. to scratch; to tear with the nails,
WEB_vol1.txt:61151:ail, or tail.
WEB_vol1.txt:90925:ail. The hip- hīr’sūte (or hir-siite
WEB_vol1.txt:104318:ail, native nomolgus, n, enclos- or enclos-
--- awe ---
WEB_vol1.txt:5101:ait, n. (ME. eyt, gil; in comp. eytlond; AS. egel, iget, an island.] an islet, or little isle, ina river or lake; an eyot.
WEB_vol1.txt:14287:away-going crops; in law, crops sown during the last year of a tenancy, but not ripe until after the expiration of it. The right which an outgoing tenant has to take an away-going crop is sometimes given to him by the express terms of the contract, but where this is not the case he is generally entitled to do so by the custom of the district. a-way’ward, adv. away. [Obs.] awe (a), n. [ME. aw, awe, from Ice. agi, awe,
WEB_vol1.txt:14300:awe’less, a. [ME. awles; AS. egeleas, aweless; ege, awe, and -leas, less.] lacking awe; also, lacking the ability to inspire awe.
WEB_vol1.txt:14307:aw’ful, a. (ME. awful, agheful; AS. egeful, awful]
```


## [2026-09-04T18:53:08.809Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==41' AKD.txt | head -6; echo \"...\"; awk 'BEGIN{RS=\"\\f\"} NR==41' AKD.txt | tail -4; echo \"=== WEB ail entry ===\"; sed -n '4970,4985p' WEB_vol1.txt"
}
```


### [2026-09-04T18:53:10.367Z] TOOL RESULT

```
 s.  oben  S.  14.  akk.
saniHu  ein  Teil  der  Mauer  :  >  viell.  aram.  sdwJtd  Ecke  O  arab. sdivijai,  auch  wohl  späthebr.  PI.  zdwijjöt).  akk.  zirrn  Einfassung
od.  ä.  :  >  viell.  hebr.  ser,  jüd.-aram.  zirä  Kranzleiste.  Vgl.  auch  noch unten  S.  38  zur  Bed.  Halskette.
akk.  qariiu  Kornboden,  eig.  wohl  Gebälk  :  ^  wohl  hebr.  qord Balken,  denom.  qcrä  bälken,  mdqdre  Gebälk,  aram.  qäritä  Balken  O  arab. qarijjat).  akk.  gimiru  Balken  :  ^  aram.  gdSürd  u.  Jca.snrd.  —  Vgl.
auch  unten  S.  44  zu  gisru  Brücke.  akk.  gas  im  Stange,  vieU.  auch
Querbalken  :  >  neuhebr.  ^«.«.s  Brett,  Querstange,  wohl  auch  jüd.-aram. gäSOsä  Schiffsstange.
...
Fenster,  Öffnungen  in  einem  Hause  (viell.  <[  sum.  ah)  :  >  viell.  hebr. "ab,  PI.  "iibhhn  als  bautechn.  Ausdr.,  und  wohl  sicher  jüd.-aram.  'aptci  Erker, Vorbau.  [Dagegen  ist  akk.  Iiillnni  Öffnungen  in  dem  Vorbau  eines
Hauses  <  westsemit.  (hebr.)  hidlun  Fenster.]  akk.  jiuraSdinnu
Loch  od.  it.  :  ;>  viell.  hebr.  parsddön  Eicht.  3,22  (falls  eine  Räumlichkeit im  Hause  und  nicht  vielmehr  einen  Körperteil  bedeutend).
akk.  kutallu  Rückseite,  Hinterseite  des  Körpers,  dann  auch  eines Gebäudes  :  >  wohl  aram.  kutlä  Wand,  Seite  O  wohl  späthe
=== WEB ail entry ===
Ai/nu, n. [Ainu, lit.. man
air
il, v.i. to be ill or indis. |; to be al with pain or uneasiness; to be in ible; one day the child began to ail.
ail, n. indisposition or disease. TES z
fi-lan’thic, ai-lan’tic, a. of or resembling an
_ ailanthus. 3 ee
Ai-lan’thus, Ai-lan’tus, n. [L., from ailanto, tree of heaven; Malacca name.] a genus of — trees native to the East Indies and cultivated in America and Europe for their leaves, which are fed upon by_silkworms; tree of
heaven; also [a-], a tree of this genus. rae
ailan/thus moth, a large siik-producing moth native to China and cultivated in the eastern United States: its larvae feed on ai- lanthus leaves. R f
āi-lan’tine, n. silk obtained from the silkworm that feeds on the ailantus. , E
āi-lao’tine, adj. of or pertairing to the Ailan- thus or to the silkworm that feeds on it. :
ai/lér-on, n. [Fr.] a movable Binge section of s the wing of an airplane, for banking in turns.
āi-lette’ (Z-let’), n. E ailette, dim. of aile, wing; L. ala, wing.| a metal shield formerly worn upon the shoulder by knights: the original form of the modern epaulet.
ail/ing, a. sickly; ill. Bes S.
4il/ment, x. any bodily or mental disorder; noi
_ illness, especially one that is not severe. F:
```


## [2026-09-04T18:53:24.783Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ak:\\|:ak \\|ak :\\|akih\\|ak-\\|aka-\\|aya-\" SNS_pages.txt | head -20; echo \"---\"; grep -n \"AiWb\" SNS_pages.txt | head -20"
}
```


### [2026-09-04T18:53:24.850Z] TOOL RESULT

```
535:                  banak-u Mainyo-i Khard, Bombay 1913.
1644:la              awaspfirand :L                               {Gkilain.                 75)     *bysp'r:^i             (^Pff.igjazdahak:^/ U£W>. 266) aziidahako                                                                :   L.
1949:                           .^IjJ.ijU^.jrf^.^ xak: >* HZWRY*: -^                                                                                    r                         :
2241:      tj(,fc   :&)    .   W   ^ityfc . cxKi'jJ • *fi^ « j'j^                       :ajrryak: -3-^>"
3516:                               •   J-i^ai.         ^j Y J>*W x Qrdak: ^                                                      :«*#& *,!•*>                 (                                     .JVfc
3980:                                             ,   Tt/T i             (^^'•^ou^ :andarOn: ^.*             1                                          fr/fetf     -T/^ CCffPff.            27)afldak       :           L   hindak:^
4266: ,/•->>*-/          xlm    ^ WiVfc- 1781) haya-, haSm-                            :
4364:                                                         (       \j_»-    :^) yak / Svak: JIM                                     >!* :o-jli .w^^tfjl^i; €v3rag-gah: -o-O^-*^                                         Y<
4372:                                .U+Ur.t5<4i :                            5vak Svak:      ***   9V                  \
4388:                                                            Af-AA-fP-fT/T 4                                                           •^jA«*io*       :   har Svak:              JW^'S
4444:                      J0^»:i)vi                  y       evak:   3*V tfWv        :    «t*i                  1A/H *$ .jiAi-^.j-*^^,:          Svkardagtar:^^^**^
5173:                                                           .^:pak:              iw|j]                                              :
5180:     (Mr. Han.      p*k :>;* CGiVPS. 62)pavaka- i^^^m
5487:                                                                                                      M*«>. 881)sak-I-rama:
5904:                  .f/lf^ .<***** ^-ci- :panj ^ vak:                      ^<»«
6072:    ,_,.,., i,   % *u. *- <«•"* * 5§ak: ^'J'**
6314:                        UiWfc.    643 > taranak: l5*j«*                   (**-*W
6665:                                                                        ca0rusutak        !   ^jWj WW-i^-V :catrusQtak:9*^^-
6786:                                                           531,   (I/eat.    .-il.AiU ,^           UI, kiharak: l/c,
7021:                                                                                                                     11/ITrf    Mifi*.       449)   karaya-,
---
510:                                                                              AiWb.:    C. BartholoiQae, A Itiranisahes Wdrterbuoh,
994:      Caiman-          jl   ^U f£**fyAiWb                    .    310.( o ^) axs-      |
1020:                                                                                                           f/H ^ AiWb.                 1756           {   ha + uxta-ji) ha<faoxta-            t-
1146:                           ^ \*/a^ {AiWb
1158:                                                                                                                                                           h'rayn         :^k {AiWb                  .    1809)     hamina-        ,   hami: fc»
1222:                                                                                                              A1-lfi/r^ (AiWb.                                 284)ahunavaitl-g30a-                                      :   £~             lo
1229:                                                                                                        khan : *» {AiWb. 532i) xan     **-^j xanya-: £-                    :
1970:10    tWir.          Man.             II, 60) my                            :   ^           {AiWb 1113 ) /mad.
2192:                                                                                                         (AiWb. istaka:L i!tya-:/i- «*-- j»T,c*i» :xilt:                                                          t^^^O-
2396:      tWir.              'rdykr yA .^i.         {AiWb   .   1506) rathestha-
2535:           (Mir. Man.             II,         56)           hrwysp                   fb     (AiWb.        1328)
2604:                                                                                                                        gCs + tAiWb. 532)khara-                                     :L xara-: is* .j* :X ar                           j   1
2626:                                                                                                                                                          Y/n <*        (AiWb.          19'4)        aradvl sQra-                 :   t*
2642:U        {Mir. ,bja*qijsli (AiWb.               1773)            saraa :£.        hama          :4t*i<L-
2858: amardat      :^    {AiWb 143-4) amaratStSt,-amaratat:-i
2923: -il>:l 'CJ> J 3 C4i^OwrJ u                                                                                                     mwrz : jilt {AiWb 1152.)
2984:                          hQxt           :    V {AiWb.                      1819)sukta        :     L huxta-i                      1                     -^ ir" y>*» •J^'j^'j'rt «** :§/ed: «***r
3084:hn'm         i.jtU   {AiWb. 1772)sandhay                        :    Lhandama-               :           0.            +   ^j n+ ^a             )
3175:            L (AiWb.        918)    bSdhay- : L                      {o=y-tf>*)         bao<fay-            :iu
3235:            >T-A-r/16^ -if/ir^ {AiWb.                                     229)asa.vahista-i                                                      jfiil^o-L/ :^ »^i *)l3 o* 1 oifS ^U Jit 5 *^j .jl, jj «5 ^W*--^ tflr)
```


## [2026-09-04T18:53:58.603Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB agur ===\"; grep -n -i \"agur\\|'gwl\\|ʾgwr\" NYB_vol2_glossary.txt NYB_vol1.txt | head -10; echo \"=== HRN ajur/agur loose ===\"; grep -n -i \"âǵûr\\|âgûr\\|agur\\|â\\ggûr\\|ājur\" HRN.txt HUB.txt | head -10; echo \"=== HRN 'agur' via nr search: 'Ziegel' in HUB ===\"; grep -n \"Ziegel\" HUB.txt | head; echo \"=== RCH agur ===\"; grep -n -i \"agur\\|ajur\" RCH.txt | head -8; echo \"=== FVQ ajurr ===\"; grep -n -i \"ajurr\\|agurru\" FVQ.txt | head -5"
}
```


### [2026-09-04T18:53:58.745Z] TOOL RESULT

```
=== NYB agur ===
=== HRN ajur/agur loose ===
ugrep: error: error at position 31
(?mi)âǵûr\|âgûr\|agur\|â\ggûr\|ājur
       invalid escape___/


=== HRN 'agur' via nr search: 'Ziegel' in HUB ===
1938:488. Lies afgh. LW. xa^ta 'Ziegel*.
9512:aresa-, skr. rksa-; xist 'Ziegel', phi. oHst = zd.istya-; xism,
=== RCH agur ===
2468:A ajurr  (or jS^\  djurr),  A   brick  or  tile.
2655:A jy^\  djur  (or ajur),  A   brick,  or  bricks.  An  odorife- rous apple,  nosegay,  or  any  thing  held  in  the  hand  on  account  of its  pleasant  smell.
2657:A   ajurah,  A   reward,  hire,  fare,  wages.  pjIj  A labourer  for  hire.
6693:AjUr**!  as-hdr^  (pi.  of  sahr)  The  lungs  (of  animals). Is^hdr^  (iv  of  jSf^)  Rising,  goii]g,  or  coming,  in  tlie  morning.
9149:AjUr*!  ffkhdr,  (IV  of^^)  Preferring,  promoting.
10204:t   iguj^  A   j^rch,  B   hook,  agraj^ing-iron. p t   agur  (orjt\  Sgur)y  A   burnt  brick, p   Sgo$h  (or  nghoBh)^  An  embrace.  The  bosom
11177:AjUr«l  imghdrj  (iv  of (A  sheep)  eeinitting,  (whilst  milk- ing),  blood  (along  with  the  milk).  .   *
13967:AjUrl  ujdry  (iv  Letting  out  on  hire.  Prostitution  for
=== FVQ ajurr ===
```


## [2026-09-04T18:54:06.680Z] TOOL CALL #56: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-04T18:54:06.726Z] TOOL RESULT

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


## [2026-09-04T18:55:20.665Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON آک ===\"; grep -n \"^آک:\\|آک: \" MON_part1.txt | head -5; echo \"=== BQT آجر ===\"; grep -n \"آجر\" BQT_v1_pages.txt | head -8; echo \"=== TLM agur ===\"; grep -n -i \"agur\" TLM.txt | head -5"
}
```


### [2026-09-04T18:55:20.766Z] TOOL RESULT

```
=== MON آک ===
=== BQT آجر ===
1200:آجر؛ وروایث درست اشت که سجیل یعنی‌سنگ و کل بیم آمیخته. ودر افظ
20930:داشتن چیزی باشد دزجایی» مثل .آنکه آجرا جر
28044:ونان هم بربالای آن پزند۴ -وخشت پختهوآجر
28569:وخشت يخته وآجر بز رکهرا نز گوشد .
=== TLM agur ===
```


## [2026-09-04T18:55:25.604Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (28044,28569):\n    idx=sum(len(l)+1 for l in lines[:ln-1])\n    leaf=t[:idx].count('\\f')\n    print('line',ln,'leaf',leaf,'printed~',leaf-210,leaf-220)\n    print('  ...',lines[ln-3:ln+2])\nEOF"
}
```


### [2026-09-04T18:55:27.420Z] TOOL RESULT

```
line 28044 leaf 679 printed~ 469 459
  ... ['ب4 - بنتح ثالث\u200cبروزن لابه , ظرفی\u200cباشد', 'پهن که درآ نک و کو وخا کینه وعاهی\u200cبربان کنند', 'ونان هم بربالای آن پزند۴ -وخشت پختهوآجر', 'بز رکه را نیز کوند - و با بای فارضی: سر گین', 'تا بش۱ بر وزن خواهش » فروغ']
line 28569 leaf 690 printed~ 480 470
  ... ['قاو۵؟ ه بروزن ساوه » ظرفی باش دکه', 'در آن خاکینه پزند و ماهی بربان کنئد ۷ -', 'وخشت يخته وآجر بز رکهرا نز گوشد .', 'تا بروزن کاه. زنگی باشد که بردوی', 'دسانس . ۳ - رك: تاول']
```


## [2026-09-04T18:55:32.491Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آگور\\|آکور\" BQT_v1_pages.txt | head -8"
}
```


### [2026-09-04T18:55:32.549Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:55:43.478Z] AGENT

Now I'll write the verification file.


## [2026-09-04T18:59:53.188Z] TOOL CALL #60: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-37.json <<'JSON'\n{\n  \"pdf_page\": 37,\n  \"book_page\": 7,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Agh, Aghlo\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂egʰ- 'to be depressed, be afraid' (Pokorny agh- p.7), with the l-extension *h₂egʰ-lo- 'disgusting, troublesome' (Pokorny agh-(lo-) p.8) and the s-stem *h₂egʰ-es- 'fear' (Gk. ákhos, Goth. agis)\",\n      \"note\": \"Both the language label and the gloss are right, and Nourai's merging of the two Pokorny lemmas into one root box follows Pokorny himself, who writes at the end of the agh- article (p.7/8): 'Hierzu gehört wohl auch: agh-(lo-) \\\"widerwärtig\\\"'. Watkins/AHD prints the two as a single root with exactly Nourai's two English derivatives: 'agh-1. To be depressed, be afraid. 1. Suffixed form *agh-lo- in Old English eglan, eglian, to trouble, afflict: AIL. 2. Suffixed form *agh-es- in Old Norse agi, frightened: AWE. [Pok. agh- 7.]' Walde-Pokorny I 40-41 has the same two lemmas with the same material. The one substantive weakness in the whole entry is the Iranian branch's third generation: Persian آخ (node #4) is an interjection and does not belong to this root (see that node). Nourai's glosses 'to be depressed, to be afraid' / 'disagreeable, adverse' are literal renderings of Pokorny's 'seelisch bedrückt sein, sich fürchten' / 'widerwärtig'.\",\n      \"ref_check\": [\n        {\"ref\": \"POK:7\", \"status\": \"supports\", \"note\": \"POK_01.txt \\\\f-leaf 15 (= printed p.7), headword: \\\"agh- ,seelisch bedrückt sein, sich fürchten'. Gr. ἄχος n. ,Beängstigung, Schmerz, Leid'… Ags. ege m. ,Furcht'… anord. agi m. (-en-St.) ,Furcht'\\\" — Nourai's gloss is a translation of this.\"},\n        {\"ref\": \"POK:8\", \"status\": \"supports\", \"note\": \"POK_01.txt \\\\f-leaf 16 (= printed p.8): \\\"Hierzu gehört wohl auch: agh-(lo-) ,widerwärtig'. Got. agls … ags. eg(e)le ,widerwärtig, beschwerlich, bedauerlich', eglan ,Schmerz zufügen' (engl. ail …) … Möglicherweise hierher ai. aghá- (= av. aγō-) ,böse', n. ,Übel, Schaden', aghalá- ,schlimm'.\\\" POK_full.txt 'Root / lemma: agh-(lo-) … Page(s): 8' repeats it.\"}\n      ],\n      \"sources\": [\n        \"https://www.etymonline.com/word/ail\",\n        \"https://www.etymonline.com/word/awe\",\n        \"https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%98\"\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"ağô, ağâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan aγa- is a thematic o-stem adjective 'bad, evil, wicked' built to the root *h₂egʰ-; Nourai's two citation forms are its inflected shapes, masc./neut. nom. sg. aγō (< *aγah, older *aγas) and fem. nom. sg. aγā. Intervocalic PIE *gʰ appears in Iranian as the voiced spirant γ, whence the spelling aγa- beside the parallel Avestan doublet aka- 'evil' (with unvoiced k, the form that survives in Middle Persian). It is exactly cognate with Vedic aghá- 'evil, sin' (Ṛgveda), both from Proto-Indo-Iranian *Hagʰás < PIE *h₂egʰ-ós, i.e. the o-grade nominal derivative of the same root that gave Greek ákhos 'pain, grief' and Gothic agis 'fear'. The word is common in Zoroastrian scripture in the compound aγa-manah- 'evil-minded, of evil thought', the antonym of vohu-manah- 'good thought'. Nourai's gloss 'bad, ugly' is a little loose: Bartholomae's AiW gives 'schlecht, böse, schlimm' and Pokorny 'böse'; 'ugly' is not part of the Avestan sense.\",\n          \"ref_check\": [\n            {\"ref\": \"POK:8\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 16 (p.8), under agh-(lo-): \\\"Möglicherweise hierher ai. aghá- (= av. aγō-) ,böse', n. ,Übel, Schaden', aghalá- ,schlimm'.\\\" Pokorny hedges with 'möglicherweise', so the attachment of the Indo-Iranian word to this root is probable rather than certain — Nourai draws it as a plain arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.41, s.v. agh-(lo-)\", \"stance\": \"supports\", \"note\": \"WLD_Bd1_pages.txt: \\\"Möglicherweise hierher (z. B. Fick I⁴ 14, 367, Feist Got. Wb. 9, Prellwitz² 347) ai. aghá- (= av. aγa-) ,böse', n. ,Übel, Schaden', aghalá- ,schlimm'\\\" — same claim, same hedge, with the earlier literature named.\"},\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.v. aγa- (scan leaf 64, AiW col. ~48)\", \"stance\": \"supports\", \"note\": \"BRT.txt (OCR renders γ as j): \\\"j. aγa- 1) Adj. (fem. -ya-) 'schlecht, böse, schlimm'; a) von Lebenden … b) …\\\", with the compound aγa-varəz- 'der Böses, Übles wirkt' immediately following. Confirms the Avestan word, its stem class and its meaning; 'ugly' is not among the senses.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, s.v. aghəlos / agh-\", \"stance\": \"supports\", \"note\": \"IEC.txt: \\\"aghəlos, aghulos 'evil, sorrow'. Cf. aghos, oghlos. Skt aghalaḥ, aghuraḥ; cf. W aeleu 'sad; grief', aeled 'ailment'; Go. agls, aglus; OE egle, egile\\\" and \\\"agh- 'dread, terror'\\\" — Mann keeps the same family together.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. agh-1\", \"stance\": \"partial\", \"note\": \"AHD_watkins1985.txt line 263 gives the root and its Germanic branches but lists no Indo-Iranian cognate, so it neither supports nor contradicts the Avestan node.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. Sanskrit अघ (agha)\", \"stance\": \"supports\", \"note\": \"\\\"From Proto-Indo-Iranian *Hagʰás ('bad; evil'), from Proto-Indo-European *h₂egʰ-ós\\\"; cognates listed are Avestan aγa 'evil', Ancient Greek ákhos and Old English eġle — i.e. modern reconstruction keeps Nourai's whole set together under one root.\"}\n          ],\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%98\"]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"âğ, âk\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian ak, written ⟨ʾk⟩ in Book Pahlavi, 'evil, harm' is the regular continuant of the Old Iranian adjective (Av. aka- / aγa- 'evil'): the thematic ending -a- is lost in Middle Persian, leaving a monosyllable, and the Avestan doublet with γ collapses into the same shape, which is why Nourai gives both āγ and āk. The word is alive in Pahlavi religious vocabulary in Akōman ⟨ʾkwmn⟩ 'Evil Thought' (the arch-demon opposing Wahman, < Av. aka-manah-) and akōmand 'evil, harmful'. MacKenzie's Concise Pahlavi Dictionary makes precisely the link Nourai draws by printing the New Persian reflex in the entry itself: 'ak [ʾk | N āk] evil, harm'. Nourai's long ā is the New Persian orthography (آک, alef-madda) read back into Pahlavi; MacKenzie transcribes short a. His gloss 'trouble, ugliness' is a paraphrase of Borhan-e Qate's Persian definition rather than of a Pahlavi source.\",\n          \"ref_check\": [\n            {\"ref\": \"SNS:38\", \"status\": \"not_found\", \"note\": \"Tavoosi's Šāyast nē Šāyast glossary is on disk only as very poor OCR (SNS.txt / SNS_pages.txt, 242 leaves, printed-page offset undetermined per refs_online.json). Grepped for 'ak:', 'āk:', 'ag:', 'āg:', 'akih', 'ākīh', 'ahok', 'āhōk', 'ahog' across both files — no entry recoverable; the glossary's headwords are printed in Pahlavi script with Latin transliteration in a second column that the OCR mangles. Cannot confirm or refute what p.38 says.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. ak (PHD.txt line 189; PHD_mackenzie.txt line 967)\", \"stance\": \"supports\", \"note\": \"\\\"ak [ʾk | N āk] evil, harm.\\\" — the Pahlavi word and its New Persian outcome āk, exactly Nourai's nodes #2 and #3. Same page: \\\"Akōman [ʾkwmn | M ʾqwmn] Evil Thought, an arch-demon\\\" and \\\"akōmand [ʾkwmnd] evil, harmful\\\".\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary)\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt and NYB_vol1.txt for 'ag', 'ak', 'akōman' returned no usable entry (OCR of the transliterated glossary is thin); no evidence either way.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.1 p.52, Mo'in's footnote to آک\", \"stance\": \"supports\", \"note\": \"Mo'in's etymological footnote on that page derives the Persian word from \\\"اوستا aγa بمعنی بد، شریر، بدی\\\" ('Avestan aγa, meaning bad, wicked, evil') citing Horn and Bartholomae — i.e. the same Avestan→Persian line that Nourai routes through Pahlavi.\"}\n          ],\n          \"sources\": []\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"âk, ak «آک ، اک»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian āk / ak آک 'defect, blemish, harm, calamity' continues Middle Persian ak ⟨ʾk⟩ 'evil, harm' unchanged except for the prosthetic lengthening of the initial vowel normal for Persian monosyllables written with alef-madda; MacKenzie's CPD prints the equation directly ('ak [ʾk | N āk] evil, harm'). Borhan-e Qate' (ed. Mo'in) p.52 defines it 'بمعنی عیب و عار باشد و آسیب و آفت را نیز گویند' — 'it means defect and disgrace, and they also use it for injury and calamity' — which is Nourai's 'trouble, deficiency'; Mo'in's footnote on the same page traces it to Avestan aγa- 'bad, wicked, evil' on the authority of Horn and Bartholomae's AiW, adding that the word has no formal connection with the name Aži Dahāka. The verse Nourai prints under the node, 'آکی نرسید بر تو از من، صدبار مرا ز تو رسید آک' (Sūzanī), is the very shāhed Borhan-e Qate' prints on p.52, so the JSON has transcribed the book faithfully.\",\n          \"ref_check\": [\n            {\"ref\": \"BQT:52\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt \\\\f-leaf 262 (= printed p.52, offset leaf−210): headword \\\"آک (۱) - بروزن چاک. بمعنی عیب و عار باشد و آسیب و آفت را نیز گویند\\\", the Sūzanī verse \\\"آکی نرسید برتو ازمن صدبار مرا زتو رسید آک . سوزنی\\\", and Mo'in's footnote \\\"اوستا aγa بمعنی بد، شریر، بدی «هرن …» «بارتولمه … AiW» … aγa-manah بمعنی بدمنش است در برابر وهومن (پاک‌منش) … و این کلمه هیچ بستگی لفظی با نام اژی‌دهاک (ضحاک) ندارد\\\".\"},\n            {\"ref\": \"SNS:38\", \"status\": \"not_found\", \"note\": \"same as node #2: the Šāyast nē Šāyast glossary OCR yields no retrievable headword for āk/ak and its printed-page offset is undetermined.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. ak\", \"stance\": \"supports\", \"note\": \"\\\"ak [ʾk | N āk] evil, harm\\\" — MacKenzie himself gives New Persian āk as the reflex.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi (MON_part1.txt)\", \"stance\": \"silent\", \"note\": \"grep for a headword آک returned nothing in the two-volume abridgement on disk; Mo'in's etymological note for this word is the one printed as a footnote in his edition of Borhan-e Qate' (see BQT:52).\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"HRN.txt has no recoverable entry for āk (the only nearby item is no. 488 xišt 'Ziegel'); Mo'in's BQT footnote nevertheless cites Horn for this word, so the entry probably exists in a part of Horn the OCR did not resolve.\"}\n          ],\n          \"sources\": []\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"âx, ax «آخ ، اخ»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"آخ / اخ is an interjection, and nothing in the sources supports deriving it from Pahlavi āk 'evil'. Phonologically the chain fails: Middle Persian ak (< Av. aka-/aγa-) gives Persian āک with -k, not -خ /-x/; a New Persian x here would require a different Old Iranian source. Semantically the two are also apart — āk is a noun 'defect, harm', آخ is an exclamation. Mo'in classes it as a صوت (interjection): 'آخ: (صت.) کلمه‌ای [که در] افسوس، احساس درد و رنج یا تحسین گویند؛ وای، اف' ('a word said in regret, in the feeling of pain and suffering, or in praise'). Borhan-e Qate' p.90 — Nourai's own cited page — has اخ and اخ اخ purely as exclamations ('بمعنی آفرین باشد که از تحسین است، و در ترحم و تأسف نیز گویند'; 'بمعنی خوش خوش باشد که بعربی طوبی و بخ بخ گویند') and offers no Iranian etymology; the etymological footnote on that page belongs to the homonym اخ 'brother' and is Semitic (\\\"حزوارش … آشوری بابلی aḫu، عبری āḥ، آرامی …\\\"). Expressive interjections of the shape āx/ax are cross-linguistically formed anew (cf. Turkish ah, Arabic آه, German ach) and are not normally inherited lexemes. The node's word, script and gloss are correctly transcribed from the book; it is Nourai's arrow that is unsupported.\",\n          \"ref_check\": [\n            {\"ref\": \"BQT:90\", \"status\": \"partial\", \"note\": \"BQT_v1_pages.txt \\\\f-leaf 300 (= printed p.90) does contain the entries \\\"اخ - بفتح اول و سکون ثانی، بمعنی آفرین باشد که از تحسین است … و در ترحم و تأسف نیز گویند، و درعربی بمعنی برادر باشد\\\" and \\\"اخ اخ - … بمعنی خوش خوش باشد که بعربی طوبی و بخ بخ گویند\\\", together with exactly Nourai's Loghatnāmeh couplet \\\"زهری که او چشاند چه جای اخ، که بخ بخ / تیغی که او گذارد چه جای اه، که به به «لغت نامه»\\\" — so the page is right, but it gives no derivation from Pahlavi āk. Its etymological footnote there is for the homonym اخ 'brother': \\\"حزوارش … آشوری بابلی aḫu، عبری āḥ، آرامی …، لغات جنوب الجزیره و حبشه\\\".\"},\n            {\"ref\": \"SNS:38\", \"status\": \"not_found\", \"note\": \"Šāyast nē Šāyast glossary OCR unusable, as for nodes #2-3.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi s.v. آخ (MON_part1.txt line 2219)\", \"stance\": \"contradicts\", \"note\": \"\\\"آخ: (صت.) کلمه‌ای [که در] افسوس، احساس درد و رنج یا تحسین گویند؛ وای، اف\\\" — tagged صوت, i.e. an interjection, with no origin tag at all, whereas Mo'in routinely marks Pahlavi ancestry with [په.].\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD\", \"stance\": \"silent\", \"note\": \"no Pahlavi *āx / ax of this meaning; the only relevant entry is 'ak [ʾk | N āk] evil, harm' and the exclamation 'alā [ʾlʾ] oh! alas!', which is unrelated in form.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.1 p.90\", \"stance\": \"partial\", \"note\": \"see ref_check: word and Nourai's shāhed are there, the derivation is not.\"}\n          ],\n          \"sources\": []\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Old English\",\n          \"words\": \"eglan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English eglan (also eglian) 'to trouble, afflict, cause pain to' reflects a Germanic adjective *aglja-/*azlja- 'troublesome, loathsome' verbalised with the weak class-I suffix; the adjective itself is the PIE l-extension *h₂egʰ-lo- of the root. Its Germanic cognate set is exactly Pokorny's: Gothic agls 'shameful' (rendering Gk. aiskhrós), agliþa/aglō 'distress, oppression', us-agljan 'to oppress', Old English adjective eġle 'hideous, loathsome, troublesome', Middle Low German egelen 'to cause grief'. Watkins/AHD prints it as the sole English-relevant reflex of the suffixed form.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 263: \\\"agh-1. To be depressed, be afraid. 1. Suffixed form *agh-lo- in Old English egian [= eglan], eglian, to trouble, afflict: AIL.\\\" The 1985 Watkins text is the revised form of the 1975/76 appendix pp.1505-1550 that Nourai cites; the root entry is unchanged.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. ail (KLN_1966.txt line 2042)\", \"stance\": \"supports\", \"note\": \"\\\"ail, tr. and intr. v. — ME. eilen, ailen, fr. OE. eglan, 'to molest, trouble', rel. to Goth. agls, 'shameful', aglō, 'distress, oppression', us-agljan …\\\"\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny p.8 s.v. agh-(lo-)\", \"stance\": \"supports\", \"note\": \"\\\"ags. eg(e)le ,widerwärtig, beschwerlich, bedauerlich', eglan ,Schmerz zufügen' (engl. ail ,schmerzen; unpäßlich sein')\\\".\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p.41\", \"stance\": \"supports\", \"note\": \"same wording as Pokorny, plus \\\"mnd. egelen ,Gram verursachen'\\\" and Old Irish ail (*agli-) 'Schimpf'.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/ail\", \"stance\": \"supports\", \"note\": \"\\\"from Old English eglan 'to trouble, plague, afflict', from Proto-Germanic *azljaz … from PIE *agh- (1) 'to be depressed, be afraid'\\\", suffixed form *agh-lo-.\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/ail\"]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"ail, ailment\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle English eilen / ailen arises from Old English eglan by the regular loss of the palatal spirant ġ before l with compensatory diphthongisation (eglan > *eġlen > eilen), the same development that gives ME rein < OE regn 'rain'. It is first common in the impersonal construction — 'what eileth the?' c.1300 — which survives as 'what ails you?'; the verb has stayed almost exclusively in that impersonal or intransitive use ever since. 'Ailment', by contrast, is not inherited: it is an English derivative of the 18th century (first recorded 1706) formed from the verb ail with the French-derived noun suffix -ment, so it belongs to the node only as a modern English descendant of the same stem.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 263 lists AIL as the derivative of *agh-lo- via OE eglan; the index (line 1222) confirms \\\"AIL agh-1\\\". AHD does not list AILMENT separately, it being a transparent English formation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. ail\", \"stance\": \"supports\", \"note\": \"\\\"ail, tr. and intr. v. — ME. eilen, ailen, fr. OE. eglan\\\" — the ME→ModE step exactly as drawn.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. AIL (SKT.txt line 485)\", \"stance\": \"supports\", \"note\": \"entry present ('AIL … to help/afflict', OCR damaged) confirming the Old English source; text too corrupt to quote in full.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/ail\", \"stance\": \"supports\", \"note\": \"\\\"The phrase 'what ails you?' dates to around 1300, originally appearing as 'what eileth the?'\\\" — dates the Middle English stage.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict. s.v. ail (WEB_vol1.txt lines 4973-4983)\", \"stance\": \"supports\", \"note\": \"\\\"ail, n. indisposition or disease\\\"; \\\"ailing, a. sickly; ill\\\"; \\\"ailment, n. any bodily or mental disorder; illness, especially one that is not severe\\\" — confirms both words and their senses in modern English.\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/ail\"]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Old Norse\",\n          \"words\": \"agi\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Norse agi is the n-stem masculine noun 'fear, awe; (later) discipline, restraint', continuing Proto-Germanic *agan-, a remodelling of the older neuter s-stem *agiz that is preserved directly in Old English ege 'fear' and Gothic agis 'fear, anguish'; that s-stem is the exact formal match of Greek ákhos (< *agh-es-) and so of PIE *h₂egʰ-es-. Beside it Old Norse has the preterite-present verb (Gothic ōg 'I fear') and ótti 'fear', ógn 'terror'. One caveat on the transcription: Nourai's gloss 'frightened' makes agi an adjective, which it is not — but the slip is inherited from his source, since Watkins/AHD itself prints 'in Old Norse agi, frightened'.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 263: \\\"2. Suffixed form *agh-es- in Old Norse agi, frightened: AWE.\\\" — Nourai's node reproduces this line verbatim, gloss and all.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. awe (KLN_1966.txt line 4145)\", \"stance\": \"supports\", \"note\": \"\\\"awe, n. — ME. aghe, awe, fr. ON. agi, rel. to OE. ege, 'fear', OHG. agiso, 'fright, terror', Goth. agis, 'fear, anguish' … and cogn. with Gk. ἄχος 'pain, grief', ἄχομαι 'I am afflicted', OIr. -agor 'I fear'.\\\" — treats ON agi as a noun.\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny p.7 s.v. agh-\", \"stance\": \"supports\", \"note\": \"\\\"anord. agi m. (-en-St.) ,Furcht'\\\" listed beside \\\"got. agis n. ,Furcht, Angst, Schrecken'\\\" and \\\"ags. ege m. ,Furcht'\\\" — a masculine noun 'fear', not an adjective.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck, Selected Synonyms §16.53 FEAR, FRIGHT (SYN.txt line 29091)\", \"stance\": \"supports\", \"note\": \"\\\"Goth. agis (ON agi 'terror'), OE ege, egesa, ME eye (NE awe), OHG egi, egiso … with vbs. Goth. ōg (pret. pres.) 'be afraid' … : Grk. ἄχος 'pain, distress', Ir. -águr 'I fear'. Walde-P. 1.40.\\\"\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. aghó / agh- (IEC.txt lines 241, 247)\", \"stance\": \"supports\", \"note\": \"\\\"agh- 'dread, terror'. Cf. aghos, aghtis. Cf. OIr. ághathar 'he fears'; OE ōga; ON ógn, ógna …\\\"; \\\"aghó, io 'groan, fear, sorrow'. WP I, 40 … Gk. ákhomai, ákhos; Go. agan, us-agjan; ON agi …\\\"\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/awe\"]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"awe, awesome\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English awe is a Norse loan, not the native word: Middle English aghe / awe (c.1300) was taken from Old Norse agi during the Scandinavian settlement of the Danelaw and displaced the inherited Old English ege, whose vowel would have given ModE *ee. Norse -g- was weakened to a glide and then absorbed (aghe > awe), the same path as ON lagu > ME lawe 'law'. The sense began as plain 'fear, terror', then narrowed under biblical usage to 'reverential dread' of God ('to stand in awe', early 15th c.) and only later softened to admiring wonder. 'Awesome' is a native English formation of the 1590s (awe + -some), i.e. a modern derivative of the loanword rather than an inherited form; 'awe-inspiring' follows c.1814.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 263: \\\"…in Old Norse agi, frightened: AWE. [Pok. agh- 7.]\\\" — AWE is the derivative AHD assigns to this root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. awe\", \"stance\": \"supports\", \"note\": \"\\\"awe, n. — ME. aghe, awe, fr. ON. agi\\\" — Klein makes it a borrowing from Norse, as here.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Awe (SKT.txt line 1229)\", \"stance\": \"supports\", \"note\": \"\\\"Awe. (Scand.) M.E. ay, aghe, awe: also eye, eghe, eye…\\\" — Skeat's '(Scand.)' label marks it a Scandinavian loan; OCR of the rest is damaged.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict. s.v. awe (WEB_vol1.txt line 14287)\", \"stance\": \"supports\", \"note\": \"\\\"awe (a), n. [ME. aw, awe, from Ice. agi, awe …]\\\"; the same column has \\\"aweless, a. [ME. awles; AS. egeleas …]\\\" and \\\"awful, a. [ME. awful, agheful; AS. egeful]\\\", showing the native OE ege- forms alongside the Norse-derived stem.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/awe\", \"stance\": \"supports\", \"note\": \"\\\"it emerged around 1300 from Scandinavian sources, particularly Old Norse agi meaning 'fright' … from Proto-Germanic *agiz- to the Proto-Indo-European root *agh-\\\"; \\\"'awesome' … evolved from this central concept\\\"; 'to stand in awe' early 15th c.\"}\n          ],\n          \"sources\": [\"https://www.etymonline.com/word/awe\"]\n        }\n      ]\n    },\n    {\n      \"entry\": 4,\n      \"root\": \"Agurru, A-gur-ru\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Akkadian agurru (also ukurru), logographic 𒅇𒆪𒊒𒌝, 'kiln-fired brick'\",\n      \"note\": \"The root box is right: agurru is the ordinary Akkadian word for a kiln-baked brick, opposed to libittu/libnu 'sun-dried brick', and Nourai's spelling 'A-gur-ru' is the syllabic cuneiform transcription used in Kent's edition of the Akkadian version of DSf. Both cited references check out. The disputed part of the entry is not the origin but the DIRECTION of one link. Nourai draws Akkadian → Old Persian → Pahlavi → Persian → Arabic → Persian, i.e. the Arabic word is a Persian loan. Of the four books he cites at node #4, only Asbaghi (PLA:6) actually says that; Fraenkel (AFA:5), Zimmern (AKD:31) and Addi Shir (AFM:7) all make Arabic ājurr a direct loan from Aramaic ʾāgūrā, and so does current Wiktionary (Arabic آجُرّ < Classical Syriac ʾăḡurrā < Akkadian agurru). Nourai's own NOTE on that node concedes the point. See node #4.\"\n      ,\n      \"ref_check\": [\n        {\"ref\": \"AKD:31\", \"status\": \"supports\", \"note\": \"Zimmern, Akkadische Fremdwörter, \\\\f-leaf 40 of AKD.txt (printed p.31/32 — the page cites 'oben S.14' and 'unten S.38/44', consistent with Nourai's 31): \\\"akk. agurru gebrannter Ziegelstein : > aram. ʾāgurā (> arab. ʾāgurr, ʾāgār, desgl. pers. āgūr, armen. agur, griech. αγουρος).\\\" Confirms the Akkadian headword and gloss exactly.\"},\n        {\"ref\": \"KNT:165\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon p.165 (KNT.txt \\\\f-leaf 187; the Lexicon runs pp.164-215, leaf = printed + ~22 here): \\\"aguru- sb. 'baked brick' (§158.1). [agurum] asm. DSf 53, supplied by König, Burgbau 52, after a-gur-ru of the Akk. text, cf. NPers. āgūr in the same meaning.\\\" Kent's 'a-gur-ru of the Akk. text' is the source of Nourai's second citation form.\"}\n      ],\n      \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A2%D8%AC%D8%B1\"],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Old Persian\",\n          \"words\": \"aguru\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Old Persian aguru- 'baked brick' would be a straight loan of Akkadian agurru, taken over in the Achaemenid building administration at Susa, where the Babylonian scribes and 'the men who wrought the baked brick, those were Babylonians' (DSf §3k). The crucial caveat, which Nourai's plain arrow hides, is that the word is NOT actually attested in Old Persian: Kent prints it in square brackets — '[agurum] asm. DSf 53' — because the Old Persian text has a lacuna there and König restored the word from the Akkadian version of the same trilingual inscription; Kent's grammar (§158.1) lists it among 'loanwords … restored loan-word agur-u-' and elsewhere writes 'perhaps [agurum]'. The second possible attestation, a[g]ura[vā] at DB 4.89, Kent himself withdraws ('but read avajā aha with Cameron'). The genuinely attested Old Persian word for a brick is išti- 'sun-dried brick' (DSf 29). So the node is a well-motivated conjecture rather than a documented form.\",\n          \"ref_check\": [\n            {\"ref\": \"KNT:165\", \"status\": \"partial\", \"note\": \"KNT.txt leaf 187 (p.165): \\\"aguru- sb. 'baked brick' (§158.1). [agurum] asm. DSf 53, supplied by König, Burgbau 52, after a-gur-ru of the Akk. text, cf. NPers. āgūr in the same meaning. a[g]ura[vā] 1sm. DB 4.89 (restored by Kent, JAOS 62.267 …); but read avajā aha with Cameron.\\\" Kent gives the word and the Akkadian source, so he supports the derivation — but the brackets mark it as restored, not attested, and Kent's §158 list calls it a 'restored loan-word'.\"},\n            {\"ref\": \"PLA:6\", \"status\": \"supports\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen, printed p.6 (PLA_pages.txt \\\\f-leaf 21, offset printed = leaf − 15), s.v. ʾāǧur: \\\"'Backstein' … > NP آگور āgur < ap. aguru 'Backstein'² < akk. agurru\\\", with footnote 2 = \\\"Kent S. 165, Mayrhofer S. 101\\\" — the same chain Nourai draws, resting on the same Kent page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §158.1 and Lexicon p.165\", \"stance\": \"partial\", \"note\": \"\\\"restored loan-word agur-u-\\\" in the list of u-stems (KNT.txt line 1838); \\\"Acc. Sg. Masc.: magum, zrafum, didum; … perhaps [agurum]\\\" (line 2157) — Kent twice flags the form as conjectural.\"},\n            {\"src\": \"AKD\", \"where\": \"Zimmern p.31/32\", \"stance\": \"partial\", \"note\": \"Zimmern routes the Iranian word not through Old Persian but through Aramaic: \\\"akk. agurru … > aram. ʾāgurā (> … desgl. pers. āgūr)\\\" — an alternative to the direct Akkadian→Old Persian loan drawn here.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW\", \"stance\": \"silent\", \"note\": \"no Avestan or Old Persian aguru-; the Avestan brick word is ištya- (cf. Horn no.488, HRN.txt line 4431: \\\"aw. ištya- 'Ziegel, Backstein'; phlv. xišt; skr. iṣṭakā-\\\").\"}\n          ],\n          \"sources\": []\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"âgur\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"A Middle Persian āgur is the intermediate the chart needs between the ancient and the modern form, and it is phonologically unproblematic — Old Persian/Aramaic agur-, ʾāgūr- would pass into Middle Persian unchanged apart from the loss of the case ending — but no Pahlavi text attests it. MacKenzie's Concise Pahlavi Dictionary has no āgur at all; the Pahlavi word for 'brick' in his glossary is xišt [ḥštˀ | N ~], continuing Avestan ištya-, and Nyberg's glossary is likewise silent. Asbaghi, the very reference Nourai cites here, goes straight from Old Persian aguru to New Persian آگور with no Middle Persian stage. Note also that the long ā of the Persian and Arabic forms is not derivable from Old Persian short a-: it points to the Aramaic shape ʾāgūrā, which is the form Zimmern and Fraenkel make the source of the whole western branch.\",\n          \"ref_check\": [\n            {\"ref\": \"PLA:6\", \"status\": \"partial\", \"note\": \"PLA_pages.txt leaf 21 (p.6) gives the chain \\\"aus dem pers. آگور āgur < ap. aguru 'Backstein' < akk. agurru\\\" — it supports the Old Persian and New Persian links Nourai draws around this node, but it contains no Pahlavi form, so it does not support this node itself.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD (PHD.txt line 1086; PHD_mackenzie.txt line 5562)\", \"stance\": \"silent\", \"note\": \"no entry āgur; \\\"xišt [ḥštˀ | (P hystyg), N ~] brick\\\" and the English-Pahlavi index \\\"brick xišt\\\" — MacKenzie's Pahlavi has only xišt for 'brick'.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary)\", \"stance\": \"silent\", \"note\": \"grep for 'agur', 'ʾgwr', 'ʾgwl' in NYB_vol2_glossary.txt and NYB_vol1.txt: nothing.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 488\", \"stance\": \"silent\", \"note\": \"HRN.txt line 4431: \\\"488. xišt 'Ziegel, Backstein'. aw. ištya- 'Ziegel, Backstein'; phlv. xišt; skr. iṣṭakā- 'Backstein'.\\\" Horn's Persian etymological dictionary treats only xišt, not āgur/ājor — consistent with the latter being a Semitic loan and so outside his scope.\"}\n          ],\n          \"sources\": []\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"âgur «آگور»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian آگور āgur 'baked brick' is well attested and is the older, native-looking form beside the Arabic-mediated آجر ājor; Richardson's Persian-Arabic-English dictionary (1829) lists it under 'p' for Persian, 'āgur, a burnt brick'. Mo'in's Farhang-e Fārsi has it with the cross-reference Nourai reproduces: 'آگور [= آجر] (اِ.) خشت پخته، آجر' ('baked brick, ājor'), immediately followed by the occupational derivative 'آگورگر (ص‌شغل.) آجرپز، آجری، آگوری' — 'brick-burner, brickmaker' — which is exactly the script_extra آگورگر / آگورگری printed in the chart, formed with the agent suffix -gar and the abstract -i. Kent, at the Old Persian entry, cites 'NPers. āgūr in the same meaning' as the evidence for his restoration. The word ultimately goes back to Akkadian agurru; whether it reached Persian directly from Old Persian (Asbaghi, Kent) or through Aramaic ʾāgūrā (Zimmern, Fraenkel) is the only point in doubt, and the long ā favours the Aramaic route.\",\n          \"ref_check\": [\n            {\"ref\": \"PLA:6\", \"status\": \"supports\", \"note\": \"PLA_pages.txt leaf 21 (p.6): the New Persian form آگور āgur is the pivot of Asbaghi's entry — \\\"aus dem pers. … āgur < ap. aguru < akk. agurru\\\".\"},\n            {\"ref\": \"MON:78\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi (MON_part1.txt line 4151): \\\"آگور: [= آجر] (اِ.) خشت پخته، آجر\\\", with line 4152: \\\"آگورگر: (ص‌شغل.) آجرپز، آجری، آگوری\\\" — both the gloss and Nourai's extra compounds. (The copy on disk is the 2-volume Adena abridgement, whose pagination differs from the 6-volume Amir Kabir edition Nourai cites, so the page number itself could not be checked.)\"},\n            {\"ref\": \"AFA:5\", \"status\": \"partial\", \"note\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen, \\\\f-leaf 35 = printed p.5 (offset leaf − 30): \\\"In Wirklichkeit aber ist آجر auch im Persischen ein aramäisches Lehnwort\\\" — Fraenkel accepts the Persian word but makes it a loan from Aramaic, not an inheritance from Old Persian.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"RCH\", \"where\": \"Richardson-Johnson, Persian-Arabic-English Dict. (RCH.txt line 10204)\", \"stance\": \"supports\", \"note\": \"\\\"p آگور agur (or آگور āgur), A burnt brick\\\" — flagged 'p' (Persian), against \\\"A آجرّ ajurr (or آجُر ājurr), A brick or tile\\\" at line 2468, flagged 'A' (Arabic).\"},\n            {\"src\": \"KNT\", \"where\": \"Kent p.165\", \"stance\": \"supports\", \"note\": \"\\\"cf. NPers. āgūr in the same meaning\\\" — Kent uses the New Persian word as the anchor for his Old Persian restoration.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.1\", \"stance\": \"silent\", \"note\": \"grep of BQT_v1_pages.txt for آگور / آکور returns nothing recoverable from the OCR.\"}\n          ],\n          \"sources\": []\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"âjur\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Arabic word is آجُرّ ʾājurr (with variants آجُر ʾājur, آجُور ʾājūr, آجُرّة for the single brick, plural أواجير), and it is certainly a loan — the Arab lexicographers themselves treat it as muʿarrab, and the un-Arabic shape and the broken plural give it away. The disagreement is over the lender. Nourai draws it from Persian آگور; Asbaghi (PLA p.6) is the only one of his four references that agrees. Fraenkel, cited by Nourai himself and the first authority on Aramaic loans in Arabic, says the opposite in as many words: 'In Wirklichkeit aber ist آجر auch im Persischen ein aramäisches Lehnwort, und dass die Araber es von den Persern übernommen haben sollten, ist nach sonstigen Analogien nicht wahrscheinlich' — the Persian word is itself an Aramaic loan, and an Arabic borrowing from Persian is improbable; he adds that the Arabs' own claim of a Persian origin (Jawharī s.v.) is mistaken, and cites Nābigha 7,16 and Dīwān Hudhayl 66,10 for early attestation. Zimmern derives Arabic and Persian in parallel from Aramaic: 'akk. agurru gebrannter Ziegelstein : > aram. ʾāgurā (> arab. ʾāgurr, ʾāgār, desgl. pers. āgūr, armen. agur, griech. αγουρος)'. Addi Shir, whose whole book is a catalogue of Persian words in Arabic, nevertheless quotes Fraenkel p.5 for an Aramaic origin at the entry Nourai cites. Wiktionary today: Arabic آجُرّ 'from Classical Syriac ʾăḡurrā, from Akkadian agurru'. The doubled -rr of the Arabic form and the long ā both match the Aramaic emphatic-state ʾāgūrā better than Persian āgur. Nourai's own NOTE ('This word could have entered Arabic directly from Akkadian / Aramaic (AFA:5)') records the objection; the arrow as drawn is nonetheless the minority view.\",\n          \"ref_check\": [\n            {\"ref\": \"AFA:5\", \"status\": \"contradicts\", \"note\": \"AFA.txt \\\\f-leaf 35 = printed p.5: \\\"Ebenfalls von den Aramäern den Arabern zugeführt ist آجرّ, dessen verschiedene Vocalisationsmöglichkeiten zugleich mit dem Mangel einer Ableitung, der unarabischen Form und dem Plur. أواجير Mu'arrab 16,7 auf fremde Herkunft hinweisen. Es soll schon im Assyrischen vorkommen … Die Araber selbst halten es für ein persisches Lehnwort; vergl. schon Ǧauh. s.v. In Wirklichkeit aber ist آجر auch im Persischen ein aramäisches Lehnwort, und dass die Araber es von den Persern übernommen haben sollten, ist nach sonstigen Analogieen nicht wahrscheinlich. Es findet sich schon bei Nābiġa 7,16; Dīv. Huḏ. 66,10; Aġānī XVI. 43,3.\\\" This is the exact reverse of Nourai's arrow.\"},\n            {\"ref\": \"PLA:6\", \"status\": \"supports\", \"note\": \"PLA_pages.txt leaf 21 (p.6), headword ʾāǧur: \\\"'Backstein' pers. — aus dem pers. آجر/آگور … > ur āgur < ap. aguru 'Backstein'² < akk. agurru\\\", fn.2 'Kent S. 165, Mayrhofer S. 101'. Asbaghi is the one cited reference that does make Arabic borrow from Persian.\"},\n            {\"ref\": \"AKD:31\", \"status\": \"contradicts\", \"note\": \"AKD.txt leaf 40 (printed p.31/32): \\\"akk. agurru gebrannter Ziegelstein : > aram. ʾāgurā (> arab. ʾāgurr, ʾāgār, desgl. pers. āgūr, armen. agur, griech. αγουρος).\\\" Zimmern's '>' marks Aramaic as the direct lender to Arabic AND to Persian, in parallel — not Persian to Arabic.\"},\n            {\"ref\": \"AFM:7\", \"status\": \"partial\", \"note\": \"Addi Shir, Kitāb al-alfāẓ al-fārisiyya al-muʿarraba, AFM_pages.txt \\\\f-leaf 8 (printed p.7, offset leaf − 1: the bāʾ chapter opens at leaf 15 = p.14): the entry \\\"( الآجور والآجُور والآجُرّ … والآجرون ) قرميد … تراب يُحكم عجنه وتقريصه … وقالوا فيه آجُرّ الطين\\\" ends \\\"وقال [فرنكل] (ص ٥) أصل اللفظة آرامية ܐܓܘܪܐ وهو موجود في اللغة الأشورية القديمة\\\" — 'Fraenkel (p.5) says the origin of the word is Aramaic ʾgwrʾ and it exists in the old Assyrian language'. Addi Shir has the word on the page Nourai cites, but for an Aramaic, not a Persian, origin.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. Persian آجر, Arabic section\", \"stance\": \"contradicts\", \"note\": \"\\\"The Arabic noun آجُرّ (ʔājurr) meaning 'burned brick': From Classical Syriac ܐܲܓܘܼܪܵܐ (ʾăḡurrā), from Akkadian 𒅇𒆪𒊒𒌝 (agurru, ukurru).\\\" No Persian stage.\"},\n            {\"src\": \"ARB\", \"where\": \"al-Jawālīqī, al-Muʿarrab (ARB_mo3rb.txt lines 16970, 18465)\", \"stance\": \"partial\", \"note\": \"the word figures in the Arabic muʿarrab tradition — \\\"في اللسان: والطوب: الآجُرّ بلغة أهل مصر، والطوبة الآجُرّة\\\" and \\\"قال ابن دريد في القرميد: قالوا هو الآجُرّ بالرومية\\\" — i.e. medieval Arab philologists agreed it was foreign but disagreed among themselves about which language.\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson-Johnson (RCH.txt lines 2468, 2655)\", \"stance\": \"supports\", \"note\": \"\\\"A آجرّ ajurr (or آجُر ājurr), A brick or tile\\\"; \\\"A آجر ājur (or ajur), A brick, or bricks\\\" — confirms the Arabic word, its shape and its meaning as Nourai gives them; says nothing about direction.\"}\n          ],\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A2%D8%AC%D8%B1\"]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"âjor «آجر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Modern Persian آجر ājor 'brick' — today the ordinary word, while آگور has become archaic — is a re-borrowing of the Arabic آجُرّ back into Persian, with the Arabic gemination simplified and the final vowel lowered to -o- in the modern pronunciation. Mo'in marks it exactly so, with the origin tag معرب: 'آجر: [معر. آگور] (اِ.) خشتی که در کوره پخته باشد، خشت پخته' — 'ājor: [Arabicized form of āgur] a brick that has been fired in a kiln'. Wiktionary agrees on the immediate source: Persian آجر 'Borrowed from Arabic آجُرّ'. So the last link of the chart — Arabic → Persian — is uncontroversial and is a genuine round trip in the Islamic period; the only doubt in the entry attaches to the previous link, whether the Arabic word had been Persian before that (see node #4). The technical vocabulary followed: آجرپز 'brick-burner', آجرکاری 'brickwork' are all built on the Arabic-shaped form.\",\n          \"ref_check\": [\n            {\"ref\": \"MON:78\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi (MON_part1.txt line 2150): \\\"آجر: [معر. آگور] (اِ.) خشتی که در کوره پخته باشد، خشت پخته.\\\" The tag معر. (= معرّب) is Mo'in's marker for an Arabicized word, and he names آگور as its base — Nourai's round trip. (Page 78 itself could not be checked: the copy on disk is the 2-volume Adena abridgement, which does not share the 6-volume edition's pagination.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. Persian آجر\", \"stance\": \"supports\", \"note\": \"\\\"From the Wiktionary entry, the Persian etymology states: 'Borrowed from Arabic آجُرّ (ʔājurr).'\\\" — the Arabic→Persian direction of this node confirmed; the chain given there continues آجُرّ < Classical Syriac ʾăḡurrā < Akkadian agurru.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p.6\", \"stance\": \"partial\", \"note\": \"Asbaghi's headword is the Arabic ʾāǧur and he cites the modern Persian آجر آجر as its Persian counterpart, but as a Persische Lehnwörter im Arabischen entry he is concerned with the outward, not the return, journey.\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson-Johnson (RCH.txt lines 2468, 10204)\", \"stance\": \"supports\", \"note\": \"records both the Arabic آجرّ and the Persian آگور side by side in the same dictionary, the standard picture of a doublet.\"}\n          ],\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A2%D8%AC%D8%B1\"]\n        }\n      ]\n    }\n  ]\n}\nJSON\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-37.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-04T18:59:55.349Z] TOOL RESULT

```
JSON OK
```


## [2026-09-04T18:59:58.539Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 tools/verify_check.py 37"
}
```


### [2026-09-04T19:00:00.072Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'confirmed': 9, 'disputed': 2, 'plausible': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 11, 'not_found': 3, 'partial': 5, 'contradicts': 2}
books consulted: {'supports': 28, 'partial': 6, 'silent': 9, 'contradicts': 2} | by book: {'PHD': 4, 'KLN': 4, 'Wiktionary': 3, 'BQT': 3, 'Etymonline': 3, 'RCH': 3, 'WLD': 2, 'BRT': 2, 'IEC': 2, 'NYB': 2, 'MON': 2, 'HRN': 2, 'POK': 2, 'SKT': 2, 'WEB': 2, 'KNT': 2, 'AHD': 1, 'SYN': 1, 'AKD': 1, 'ARB': 1, 'PLA': 1}
```


## [2026-09-04T19:00:20.345Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-37.json`; `verify_check.py 37` reports 13/13 nodes, no PROBLEM lines.

**Page 37 (book p.7) — 2 non-redirect entries, 13 nodes**
- Root verdicts: confirmed 2. Node verdicts: confirmed 9, plausible 2, disputed 2.
- Ref checks: supports 11, partial 5, contradicts 2, not_found 3. 21 books consulted (POK, WLD, AHD, IEC, SYN, BRT, KNT, PHD, NYB, HRN, BQT, MON, RCH, KLN, SKT, WEB, AKD, AFA, AFM, PLA, ARB) + 4 archived web pages.

Disputed / flagged items:
- **Agh #4 — Persian آخ/اخ āx** (disputed): an interjection. Nourai's own BQT:90 has only the exclamation and his Loghatnāmeh couplet, with no Iranian etymology (its footnote there is for the homonym اخ 'brother' < Semitic aḫu); Mo'in tags آخ as صوت with no origin. Also phonologically impossible: MP ak > NP āk, not -x.
- **Agurru #4 — Arabic آجُرّ ājurr** (disputed): three of Nourai's own four references reverse his arrow. Fraenkel AFA p.5 verbatim: "In Wirklichkeit aber ist آجر auch im Persischen ein aramäisches Lehnwort, und dass die Araber es von den Persern übernommen haben sollten, ist … nicht wahrscheinlich"; Zimmern AKD p.31 has Akk. agurru > Aram. ʾāgurā > Arab. ʾāgurr / pers. āgūr in parallel; Addi Shir AFM p.7 quotes Fraenkel for an Aramaic origin; Wiktionary: Arabic < Syriac ʾăḡurrā < Akkadian. Only Asbaghi PLA:6 backs Persian → Arabic. Nourai's NOTE already concedes it.

Other notable findings (not flagged):
- **Agurru #1 (OP aguru)** downgraded to plausible: Kent p.165 prints "[agurum] … supplied by König … after a-gur-ru of the Akk. text" — the OP form is restored in a DSf lacuna, not attested (Kent §158 calls it a "restored loan-word").
- **Agurru #2 (Pahlavi āgur)** plausible: unattested; MacKenzie and Nyberg have only *xišt* for 'brick', and Asbaghi's chain has no Middle Persian stage. The long ā points to Aramaic ʾāgūrā rather than OP agur-.
- Strong positives: PHD s.v. "ak [ʾk | N āk] evil, harm" and Mo'in's BQT p.52 footnote (Av. aγa-) confirm the whole Avestan→Pahlavi→Persian آک branch; AHD s.v. agh-1 confirms the ail/awe branch verbatim.
- Transcription note (no suspect flag): Nourai's Old Norse gloss "agi: frightened" is a noun mis-glossed as an adjective — the slip is copied straight from AHD's own wording.
- SNS:38 (Tavoosi, Šāyast nē Šāyast glossary) recorded `not_found` on all three Iranian nodes: the on-disk OCR is unusable and its printed-page offset is undetermined.
